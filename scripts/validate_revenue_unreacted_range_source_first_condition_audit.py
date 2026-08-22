from __future__ import annotations

import argparse
from pathlib import Path

import pandas as pd

from revenue_unreacted_range_monthly_revenue_cross_market_resolution import (
    canonical_monthly_revenue_history_table_sha256,
    resolve_monthly_revenue_cross_market_mirrors,
)

from revenue_unreacted_range_source_first_condition_audit import (
    ARTIFACT_VERSION,
    BASELINE_VARIANT_ID,
    CONDITION_SPECS,
    DETAIL_COLUMNS,
    DETAIL_CSV,
    FINANCIAL_STATEMENT_SCOPE,
    LATEST_CSV,
    LATEST_MD,
    MONTHLY_REVENUE_CROSS_MARKET_RESOLUTION_CSV,
    NO_CROSS_MARKET_RESOLUTION_ID,
    PRIMARY_VARIANT_ID,
    REVENUE_HISTORY_CSV,
    SUMMARY_COLUMNS,
)


ROOT = Path(__file__).resolve().parents[1]
SOURCE_SNAPSHOT_PROJECTION_MANIFEST_CSV = (
    ROOT
    / "output/latest/research_backtest/"
    "revenue_unreacted_range_source_snapshot_projection_manifest_latest.csv"
)
SOURCE_SNAPSHOT_PROJECTION_ID = (
    "revenue_unreacted_range_source_snapshot_asof_20260713"
)
SOURCE_SNAPSHOT_CUTOFF_DATE = "20260713"
SOURCE_SNAPSHOT_V1_VERSION = "source_snapshot_projection_v1_20260731"
SOURCE_SNAPSHOT_V2_VERSION = "source_snapshot_projection_v2_20260822"
SOURCE_SNAPSHOT_V1_POLICY = (
    "raw_source_and_price_truncated_before_source_first_episode_assembly_v1"
)
SOURCE_SNAPSHOT_V2_POLICY = (
    "raw_source_and_corrected_official_price_truncated_before_source_first_episode_assembly_v2"
)
SOURCE_SNAPSHOT_V2_LINEAGE_CHANGE_REASON = (
    "corrected_official_pre_cutoff_price_history_lineage_rebaseline_20260822"
)
SOURCE_SNAPSHOT_V2_CANDIDATE_STATUS = "generated_pending_supersede_approval"
SOURCE_SNAPSHOT_V1_MANIFEST_SHA256 = (
    "d2dde5a1f05bc2f15baf4d77f326a7ea90b481492178fa6d2fd6262bf316c79e"
)
SOURCE_SNAPSHOT_V1_DETAIL_SHA256 = (
    "b9784e4df2d2eba2c511b1c87f4255a6485a1fe1d7ac67490802e396614ee49a"
)
RUN_LINEAGE_COLUMNS = (
    "monthly_revenue_history_blob_sha256",
    "monthly_revenue_canonical_table_sha256",
    "cross_market_resolution_registry_canonical_sha256",
)
PROJECTION_FORBIDDEN_TRUE_FLAGS = (
    "formal_model_use_allowed",
    "approved_for_daily",
    "production_change",
    "promotion_evidence_allowed",
    "ranking_consumption_allowed",
    "pdf_consumption_allowed",
)


DETAIL_DTYPES = {
    "stock_id": str,
    "episode_start_source_date": str,
    "episode_start_trade_date": str,
    "latest_qualifying_source_date": str,
    "latest_qualifying_trade_date": str,
    "first_breakout_date": str,
    "launch_date": str,
}


def _boolish(series: pd.Series) -> pd.Series:
    return series.astype(str).str.strip().str.lower().isin({"true", "1", "yes"})


def _number(value: object) -> float | None:
    number = pd.to_numeric(value, errors="coerce")
    return None if pd.isna(number) else float(number)


def _digits(value: object, length: int) -> str:
    return "".join(character for character in str(value) if character.isdigit())[:length]


def _stock_id(value: object) -> str:
    text = str(value).strip().replace(".0", "")
    return text.zfill(4) if text else ""


def _is_sha256(value: object) -> bool:
    text = str(value).strip().lower()
    return len(text) == 64 and all(
        character in "0123456789abcdef" for character in text
    )


def _canonical_projection_version() -> tuple[str | None, list[str]]:
    path = SOURCE_SNAPSHOT_PROJECTION_MANIFEST_CSV
    if path.is_symlink():
        return None, [
            "canonical source projection manifest is unsafe: "
            f"{path} (symlink_not_allowed)"
        ]
    if path.is_dir():
        return None, [
            "canonical source projection manifest is unsafe: "
            f"{path} (directory_not_allowed)"
        ]
    if not path.is_file():
        return None, [f"canonical source projection manifest is missing: {path}"]
    try:
        manifest = pd.read_csv(path, keep_default_na=False, low_memory=False)
    except (OSError, UnicodeError, pd.errors.ParserError) as exc:
        return None, [
            "canonical source projection manifest cannot be parsed: "
            f"{path}: {exc}"
        ]
    if "projection_version" not in manifest.columns:
        return None, [
            "canonical source projection manifest schema is incomplete: "
            "missing projection_version"
        ]
    if len(manifest) != 1:
        return None, [
            "canonical source projection manifest must contain exactly one row"
        ]
    projection_version = str(manifest.iloc[0]["projection_version"]).strip()
    if projection_version not in (
        SOURCE_SNAPSHOT_V1_VERSION,
        SOURCE_SNAPSHOT_V2_VERSION,
    ):
        return None, [
            "canonical source projection manifest has unsupported projection_version: "
            f"{projection_version or '<empty>'}"
        ]
    return projection_version, []


def _resolve_default_projection_manifest_path() -> tuple[Path | None, list[str]]:
    _projection_version, canonical_errors = _canonical_projection_version()
    if canonical_errors:
        return None, canonical_errors
    return SOURCE_SNAPSHOT_PROJECTION_MANIFEST_CSV, []


def _pinned_monthly_revenue_lineage(
    manifest_path: Path,
) -> tuple[dict[str, str], int, str]:
    manifest = pd.read_csv(
        manifest_path,
        keep_default_na=False,
        low_memory=False,
    )
    required = {
        "artifact_version",
        "projection_id",
        "projection_version",
        "projection_policy_id",
        "cutoff_date",
        "full_source_artifact_id",
        "full_source_artifact_version",
        "research_only",
        "cutoff_revenue_subset_row_count",
        "cutoff_revenue_subset_semantic_sha256",
        *RUN_LINEAGE_COLUMNS,
        *PROJECTION_FORBIDDEN_TRUE_FLAGS,
    }
    missing = sorted(required - set(manifest.columns))
    if missing:
        raise RuntimeError(
            "immutable source projection manifest schema is incomplete: "
            f"{missing}"
        )
    if len(manifest) != 1:
        raise RuntimeError(
            "immutable source projection manifest must contain exactly one row"
        )
    row = manifest.iloc[0]
    projection_version = str(row["projection_version"]).strip()
    projection_policy = str(row["projection_policy_id"]).strip()
    if str(row["artifact_version"]).strip() != projection_version:
        raise RuntimeError("immutable source projection artifact/version binding drift")
    if projection_version == SOURCE_SNAPSHOT_V1_VERSION:
        if projection_policy != SOURCE_SNAPSHOT_V1_POLICY:
            raise RuntimeError("immutable source projection v1 policy drift")
    elif projection_version == SOURCE_SNAPSHOT_V2_VERSION:
        candidate_required = {
            "predecessor_projection_version",
            "predecessor_manifest_bytes_sha256",
            "predecessor_detail_bytes_sha256",
            "lineage_change_reason",
            "candidate_status",
        }
        candidate_missing = sorted(candidate_required - set(manifest.columns))
        if candidate_missing:
            raise RuntimeError(
                "source projection v2 candidate schema is incomplete: "
                f"{candidate_missing}"
            )
        expected_candidate = {
            "projection_policy_id": SOURCE_SNAPSHOT_V2_POLICY,
            "predecessor_projection_version": SOURCE_SNAPSHOT_V1_VERSION,
            "predecessor_manifest_bytes_sha256": SOURCE_SNAPSHOT_V1_MANIFEST_SHA256,
            "predecessor_detail_bytes_sha256": SOURCE_SNAPSHOT_V1_DETAIL_SHA256,
            "lineage_change_reason": SOURCE_SNAPSHOT_V2_LINEAGE_CHANGE_REASON,
            "candidate_status": SOURCE_SNAPSHOT_V2_CANDIDATE_STATUS,
        }
        for column, expected in expected_candidate.items():
            if str(row[column]).strip() != expected:
                raise RuntimeError(
                    f"source projection v2 candidate {column} drift"
                )
    else:
        raise RuntimeError(
            f"unsupported immutable source projection version: {projection_version}"
        )
    if str(row["projection_id"]).strip() != SOURCE_SNAPSHOT_PROJECTION_ID:
        raise RuntimeError("immutable source projection id drift")
    if str(row["cutoff_date"]).strip() != SOURCE_SNAPSHOT_CUTOFF_DATE:
        raise RuntimeError("immutable source projection cutoff drift")
    if str(row["full_source_artifact_id"]).strip() != "revenue_unreacted_range_source_first_condition_audit":
        raise RuntimeError("immutable source projection full-source artifact id drift")
    if str(row["full_source_artifact_version"]).strip() != ARTIFACT_VERSION:
        raise RuntimeError("immutable source projection full-source artifact version drift")
    if str(row["research_only"]).strip().lower() != "true":
        raise RuntimeError(
            "immutable source projection research_only must be canonical true"
        )
    noncanonical_formal_flags = [
        flag
        for flag in PROJECTION_FORBIDDEN_TRUE_FLAGS
        if str(row[flag]).strip().lower() != "false"
    ]
    if noncanonical_formal_flags:
        raise RuntimeError(
            "immutable source projection formal-use flags must remain canonical false: "
            f"{noncanonical_formal_flags}"
        )
    lineage = {
        column: str(row[column]).strip().lower()
        for column in RUN_LINEAGE_COLUMNS
    }
    invalid = sorted(
        column for column, value in lineage.items() if not _is_sha256(value)
    )
    if invalid:
        raise RuntimeError(
            "immutable source projection run lineage is not canonical SHA-256: "
            f"{invalid}"
        )
    cutoff_row_count = pd.to_numeric(
        row["cutoff_revenue_subset_row_count"], errors="coerce"
    )
    if pd.isna(cutoff_row_count) or float(cutoff_row_count) < 0 or not float(
        cutoff_row_count
    ).is_integer():
        raise RuntimeError(
            "immutable source projection cutoff revenue row count is invalid"
        )
    cutoff_semantic_sha = str(
        row["cutoff_revenue_subset_semantic_sha256"]
    ).strip().lower()
    if not _is_sha256(cutoff_semantic_sha):
        raise RuntimeError(
            "immutable source projection cutoff revenue semantic SHA-256 is invalid"
        )
    return lineage, int(cutoff_row_count), cutoff_semantic_sha


def _current_monthly_revenue_lineage(
    revenue_path: Path,
    resolution_path: Path,
) -> tuple[int, str, dict[tuple[str, str], dict[str, str]]]:
    if not revenue_path.is_file():
        raise RuntimeError(f"missing monthly revenue history: {revenue_path}")
    raw = pd.read_csv(
        revenue_path,
        dtype=str,
        keep_default_na=False,
        low_memory=False,
    )
    canonical = resolve_monthly_revenue_cross_market_mirrors(
        raw,
        resolution_path,
    )
    cutoff_canonical = resolve_monthly_revenue_cross_market_mirrors(
        raw,
        resolution_path,
        observation_cutoff_date=SOURCE_SNAPSHOT_CUTOFF_DATE,
    )
    by_key: dict[tuple[str, str], dict[str, str]] = {}
    for row in canonical.itertuples(index=False):
        key = (_stock_id(row.stock_id), _digits(row.revenue_period, 6))
        if key in by_key:
            raise RuntimeError(
                f"current canonical monthly revenue repeats a stock-period: {key[0]}/{key[1]}"
            )
        resolution_id = str(row.cross_market_resolution_id).strip()
        by_key[key] = {
            "source_date": _digits(row.source_table_date, 8),
            "cross_market_resolution_id": (
                resolution_id or NO_CROSS_MARKET_RESOLUTION_ID
            ),
            "source_row_canonical_sha256": str(
                row.source_row_canonical_sha256
            ).strip().lower(),
            "canonical_source_table_date": _digits(
                row.canonical_source_table_date, 8
            ),
        }
    return (
        len(cutoff_canonical),
        canonical_monthly_revenue_history_table_sha256(cutoff_canonical),
        by_key,
    )


def validate(
    *,
    revenue_path: Path = REVENUE_HISTORY_CSV,
    resolution_path: Path = MONTHLY_REVENUE_CROSS_MARKET_RESOLUTION_CSV,
    projection_manifest_path: Path | None = None,
) -> list[str]:
    if projection_manifest_path is None:
        projection_manifest_path, routing_errors = (
            _resolve_default_projection_manifest_path()
        )
        if routing_errors:
            return routing_errors
        if projection_manifest_path is None:
            return ["default source projection manifest routing returned no path"]
    projection_manifest_path = Path(projection_manifest_path)
    errors: list[str] = []
    for path in (LATEST_CSV, DETAIL_CSV, LATEST_MD):
        if not path.is_file():
            errors.append(f"source-first revenue condition artifact is missing: {path}")
    if not projection_manifest_path.is_file():
        errors.append(
            "source-first immutable projection manifest is missing: "
            f"{projection_manifest_path}"
        )
    if errors:
        return errors

    try:
        (
            expected_run_lineage,
            expected_cutoff_row_count,
            expected_cutoff_semantic_sha,
        ) = _pinned_monthly_revenue_lineage(projection_manifest_path)
        (
            current_cutoff_row_count,
            current_cutoff_semantic_sha,
            current_source_lineage,
        ) = _current_monthly_revenue_lineage(
            revenue_path,
            resolution_path,
        )
    except (RuntimeError, ValueError, KeyError, pd.errors.ParserError) as exc:
        return [f"source-first current monthly revenue lineage cannot be verified: {exc}"]

    if current_cutoff_row_count != expected_cutoff_row_count:
        errors.append(
            "source-first current cutoff monthly revenue row count drift: "
            f"actual={current_cutoff_row_count}; expected={expected_cutoff_row_count}"
        )
    if current_cutoff_semantic_sha != expected_cutoff_semantic_sha:
        errors.append(
            "source-first current cutoff monthly revenue semantic lineage drift: "
            f"actual={current_cutoff_semantic_sha}; "
            f"expected={expected_cutoff_semantic_sha}"
        )

    summary = pd.read_csv(LATEST_CSV, keep_default_na=False, low_memory=False)
    detail = pd.read_csv(
        DETAIL_CSV,
        dtype=DETAIL_DTYPES,
        keep_default_na=False,
        low_memory=False,
    )
    markdown = LATEST_MD.read_text(encoding="utf-8")
    if list(summary.columns) != SUMMARY_COLUMNS:
        errors.append("source-first revenue condition summary schema drift")
    if list(detail.columns) != DETAIL_COLUMNS:
        errors.append("source-first revenue condition detail schema drift")
    if errors:
        return errors

    expected_variants = {spec.condition_variant_id for spec in CONDITION_SPECS}
    if set(summary["condition_variant_id"].astype(str)) != expected_variants:
        errors.append("source-first revenue condition variant coverage drift")
    if summary["condition_variant_id"].duplicated().any():
        errors.append("source-first revenue condition summary repeats a variant")
    if detail["episode_key"].duplicated().any():
        errors.append("source-first revenue condition detail repeats episode keys")

    for name, frame in (("summary", summary), ("detail", detail)):
        if set(frame["artifact_version"].astype(str)) != {ARTIFACT_VERSION}:
            errors.append(f"source-first revenue condition {name} version drift")
        if _boolish(frame["approved_for_daily"]).any():
            errors.append(f"source-first revenue condition {name} must remain research-only")
        if _boolish(frame["production_change"]).any():
            errors.append(f"source-first revenue condition {name} must not change production")
        if set(frame["financial_statement_scope"].astype(str)) != {FINANCIAL_STATEMENT_SCOPE}:
            errors.append(f"source-first revenue condition {name} financial scope drift")
        for column, expected in expected_run_lineage.items():
            if set(frame[column].astype(str).str.strip().str.lower()) != {expected}:
                errors.append(
                    f"source-first revenue condition {name} immutable capture lineage drift: {column}"
                )

    detail_variants = set(detail["condition_variant_id"].astype(str))
    if not detail_variants <= expected_variants:
        errors.append("source-first revenue condition detail contains an unknown variant")

    for row in summary.itertuples(index=False):
        part = detail.loc[detail["condition_variant_id"].eq(row.condition_variant_id)]
        source_partition_total = (
            int(row.source_missing_price_history_event_count)
            + int(row.source_left_censored_event_count)
            + int(row.source_after_price_history_event_count)
            + int(row.source_already_reacted_event_count)
            + int(row.source_price_unreacted_event_count)
        )
        if int(row.source_event_count) != source_partition_total:
            errors.append(f"source-first source partition does not conserve rows: {row.condition_variant_id}")
        if int(row.source_price_mapped_event_count) != (
            int(row.source_already_reacted_event_count)
            + int(row.source_price_unreacted_event_count)
        ):
            errors.append(f"source-first mapped source partition drift: {row.condition_variant_id}")
        if int(row.source_price_unreacted_event_count) < int(row.candidate_episode_count):
            errors.append(f"source-first lifecycle expands source rows: {row.condition_variant_id}")
        launch = part["episode_status"].eq("launch_within_active_horizon")
        no_launch = part["episode_status"].eq("no_launch_within_active_horizon")
        right_censored = part["episode_status"].eq("right_censored_before_active_horizon")
        classifiable = int(launch.sum() + no_launch.sum())
        if int(row.candidate_episode_count) != len(part):
            errors.append(f"source-first candidate count drift: {row.condition_variant_id}")
        if int(row.launch_count) != int(launch.sum()):
            errors.append(f"source-first launch count drift: {row.condition_variant_id}")
        if int(row.no_launch_count) != int(no_launch.sum()):
            errors.append(f"source-first no-launch count drift: {row.condition_variant_id}")
        if int(row.right_censored_count) != int(right_censored.sum()):
            errors.append(f"source-first right-censor count drift: {row.condition_variant_id}")
        if int(row.classifiable_episode_count) != classifiable:
            errors.append(f"source-first classifiable count drift: {row.condition_variant_id}")
        expected_rate = round(int(launch.sum()) / classifiable * 100.0, 4) if classifiable else None
        observed_rate = _number(row.retrospective_launch_rate_pct)
        if expected_rate is not None and observed_rate != expected_rate:
            errors.append(f"source-first retrospective rate drift: {row.condition_variant_id}")
        first_success = part["first_breakout_outcome"].eq("strict_success")
        first_failure = part["first_breakout_outcome"].eq("mature_failure")
        first_classifiable = int(first_success.sum() + first_failure.sum())
        expected_first_rate = (
            round(int(first_success.sum()) / first_classifiable * 100.0, 4)
            if first_classifiable
            else None
        )
        observed_first_rate = _number(row.first_breakout_strict_success_rate_pct)
        if expected_first_rate is not None and observed_first_rate != expected_first_rate:
            errors.append(f"source-first first-breakout rate drift: {row.condition_variant_id}")
        exclusion_candidate = (
            _boolish(part["qualifying_source_revenue_anomaly_candidate_flag"])
            | _boolish(part["unresolved_price_path_candidate_flag"])
        )
        clean = part.loc[~exclusion_candidate]
        clean_launch = clean["episode_status"].eq("launch_within_active_horizon")
        clean_no_launch = clean["episode_status"].eq("no_launch_within_active_horizon")
        clean_classifiable = int(clean_launch.sum() + clean_no_launch.sum())
        clean_rate = (
            round(int(clean_launch.sum()) / clean_classifiable * 100.0, 4)
            if clean_classifiable
            else None
        )
        if int(row.candidate_exclusion_episode_count) != int(exclusion_candidate.sum()):
            errors.append(f"source-first anomaly candidate count drift: {row.condition_variant_id}")
        if int(row.excluding_candidate_classifiable_count) != clean_classifiable:
            errors.append(f"source-first clean classifiable count drift: {row.condition_variant_id}")
        if clean_rate is not None and _number(
            row.retrospective_launch_rate_excluding_candidates_pct
        ) != clean_rate:
            errors.append(f"source-first clean launch rate drift: {row.condition_variant_id}")
        if int(row.same_stock_overlap_pair_count) != 0:
            errors.append(f"source-first same-stock overlap remains: {row.condition_variant_id}")

    for (variant_id, stock_id), stock in detail.groupby(
        ["condition_variant_id", "stock_id"], sort=False
    ):
        ordered = stock.sort_values("episode_start_sequence_index", kind="mergesort")
        starts = pd.to_numeric(ordered["episode_start_sequence_index"], errors="coerce")
        prior_ends = pd.to_numeric(ordered["episode_end_sequence_index"], errors="coerce").shift(1)
        if starts.le(prior_ends).fillna(False).any():
            errors.append(f"source-first episode overlap: {variant_id}/{stock_id}")

    for row in detail.itertuples(index=False):
        periods = str(row.qualifying_revenue_periods).split("|")
        source_dates = str(row.qualifying_source_dates).split("|")
        resolution_ids = str(row.qualifying_cross_market_resolution_ids).split("|")
        source_row_hashes = str(
            row.qualifying_source_row_canonical_sha256s
        ).lower().split("|")
        canonical_source_dates = str(
            row.qualifying_canonical_source_table_dates
        ).split("|")
        trade_dates = str(row.qualifying_trade_dates).split("|")
        try:
            sequence_indices = [
                int(value) for value in str(row.qualifying_sequence_indices).split("|")
            ]
        except ValueError:
            errors.append(f"source-first qualifying sequence is not numeric: {row.episode_key}")
            continue
        aligned_lengths = {
            len(periods),
            len(source_dates),
            len(resolution_ids),
            len(source_row_hashes),
            len(canonical_source_dates),
            len(trade_dates),
            len(sequence_indices),
            int(row.qualifying_update_count),
        }
        if len(aligned_lengths) != 1 or not periods or any(
            not value
            for values in (
                periods,
                source_dates,
                resolution_ids,
                source_row_hashes,
                canonical_source_dates,
                trade_dates,
            )
            for value in values
        ):
            errors.append(f"source-first qualifying lineage is not aligned: {row.episode_key}")
            continue
        if periods[0] != str(row.episode_start_revenue_period):
            errors.append(f"source-first qualifying lineage start period drift: {row.episode_key}")
        if source_dates[0] != str(row.episode_start_source_date):
            errors.append(f"source-first qualifying lineage start source date drift: {row.episode_key}")
        if resolution_ids[0] != str(row.episode_start_cross_market_resolution_id):
            errors.append(
                f"source-first qualifying lineage start resolution id drift: {row.episode_key}"
            )
        if source_row_hashes[0] != str(
            row.episode_start_source_row_canonical_sha256
        ).lower():
            errors.append(
                f"source-first qualifying lineage start source hash drift: {row.episode_key}"
            )
        if canonical_source_dates[0] != str(
            row.episode_start_canonical_source_table_date
        ):
            errors.append(
                f"source-first qualifying lineage start canonical date drift: {row.episode_key}"
            )
        if trade_dates[0] != str(row.episode_start_trade_date):
            errors.append(f"source-first qualifying lineage start trade date drift: {row.episode_key}")
        if sequence_indices[0] != int(row.episode_start_sequence_index):
            errors.append(f"source-first qualifying lineage start index drift: {row.episode_key}")
        if periods[-1] != str(row.latest_qualifying_revenue_period):
            errors.append(f"source-first qualifying lineage latest period drift: {row.episode_key}")
        if source_dates[-1] != str(row.latest_qualifying_source_date):
            errors.append(f"source-first qualifying lineage latest source date drift: {row.episode_key}")
        if resolution_ids[-1] != str(
            row.latest_qualifying_cross_market_resolution_id
        ):
            errors.append(
                f"source-first qualifying lineage latest resolution id drift: {row.episode_key}"
            )
        if source_row_hashes[-1] != str(
            row.latest_qualifying_source_row_canonical_sha256
        ).lower():
            errors.append(
                f"source-first qualifying lineage latest source hash drift: {row.episode_key}"
            )
        if canonical_source_dates[-1] != str(
            row.latest_qualifying_canonical_source_table_date
        ):
            errors.append(
                f"source-first qualifying lineage latest canonical date drift: {row.episode_key}"
            )
        if trade_dates[-1] != str(row.latest_qualifying_trade_date):
            errors.append(f"source-first qualifying lineage latest trade date drift: {row.episode_key}")
        if sequence_indices[-1] != int(row.latest_qualifying_sequence_index):
            errors.append(f"source-first qualifying lineage latest index drift: {row.episode_key}")
        if sequence_indices != sorted(sequence_indices) or trade_dates != sorted(trade_dates):
            errors.append(f"source-first qualifying lineage is not chronological: {row.episode_key}")
        if any(source_date > trade_date for source_date, trade_date in zip(source_dates, trade_dates)):
            errors.append(f"source-first qualifying source is after mapped trade date: {row.episode_key}")
        if any(
            len(value) != 64
            or any(character not in "0123456789abcdef" for character in value)
            for value in source_row_hashes
        ):
            errors.append(
                f"source-first qualifying source hash is not canonical SHA-256: {row.episode_key}"
            )
        for period, source_date, resolution_id, source_hash, canonical_date in zip(
            periods,
            source_dates,
            resolution_ids,
            source_row_hashes,
            canonical_source_dates,
        ):
            expected = current_source_lineage.get(
                (_stock_id(row.stock_id), _digits(period, 6))
            )
            if expected is None:
                errors.append(
                    f"source-first qualifying row is absent from current canonical monthly revenue: "
                    f"{row.episode_key}/{period}"
                )
                continue
            observed = {
                "source_date": _digits(source_date, 8),
                "cross_market_resolution_id": resolution_id,
                "source_row_canonical_sha256": source_hash,
                "canonical_source_table_date": _digits(canonical_date, 8),
            }
            drift = [
                column
                for column, expected_value in expected.items()
                if observed[column] != expected_value
            ]
            if drift:
                errors.append(
                    f"source-first qualifying row current input lineage drift: "
                    f"{row.episode_key}/{period}/{drift}"
                )

    selected = summary.loc[summary["condition_variant_id"].eq(PRIMARY_VARIANT_ID)]
    baseline = summary.loc[summary["condition_variant_id"].eq(BASELINE_VARIANT_ID)]
    if len(selected) != 1 or len(baseline) != 1:
        errors.append("source-first selected or baseline summary row is missing")
    else:
        selected_row = selected.iloc[0]
        baseline_row = baseline.iloc[0]
        if not _boolish(pd.Series([selected_row["known_success_4916_covered"]])).iloc[0]:
            errors.append("source-first selected condition omits known success 4916")
        if not _boolish(pd.Series([selected_row["known_success_1303_covered"]])).iloc[0]:
            errors.append("source-first selected condition omits known success 1303")
        selected_rate = _number(selected_row["retrospective_launch_rate_pct"])
        baseline_rate = _number(baseline_row["retrospective_launch_rate_pct"])
        if selected_rate is None or baseline_rate is None or selected_rate <= baseline_rate:
            errors.append("source-first selected condition no longer improves retrospective discrimination")
        selected_clean_rate = _number(
            selected_row["retrospective_launch_rate_excluding_candidates_pct"]
        )
        baseline_clean_rate = _number(
            baseline_row["retrospective_launch_rate_excluding_candidates_pct"]
        )
        if (
            selected_clean_rate is None
            or baseline_clean_rate is None
            or selected_clean_rate <= baseline_clean_rate
        ):
            errors.append("source-first selected condition clean sensitivity direction flipped")
        if selected_row["decision_status"] != (
            "research_candidate_selected_for_forward_confirmation_audit"
        ):
            errors.append("source-first selected condition decision status drift")

    known = detail.loc[
        detail["condition_variant_id"].eq(PRIMARY_VARIANT_ID)
        & detail["episode_status"].eq("launch_within_active_horizon")
        & detail["stock_id"].isin(["4916", "1303"])
    ]
    if set(known["stock_id"]) != {"4916", "1303"}:
        errors.append("source-first known success detail coverage drift")
    force_4916 = known.loc[known["stock_id"].eq("4916")]
    force_1303 = known.loc[known["stock_id"].eq("1303")]
    if len(force_4916) != 1:
        errors.append("source-first expected exactly one mature 4916 success episode")
    else:
        row = force_4916.iloc[0]
        if row["launch_date"] != "20260518" or row["first_breakout_outcome"] != "mature_failure":
            errors.append("source-first 4916 launch or first-breakout gap drift")
    if len(force_1303) != 1:
        errors.append("source-first expected exactly one mature 1303 success episode")
    else:
        row = force_1303.iloc[0]
        if row["episode_start_source_date"] != "20260517":
            errors.append("source-first 1303 must be covered before the 2026 launch")
        if row["launch_date"] != "20260527" or row["first_breakout_outcome"] != "strict_success":
            errors.append("source-first 1303 launch path drift")

    if not _boolish(detail["same_stock_non_overlap_applied"]).all():
        errors.append("source-first non-overlap flag is not universal")
    if not _boolish(detail["source_price_unreacted_flag"]).all():
        errors.append("source-first detail contains a reacted source row")
    if not pd.to_numeric(summary["right_censored_count"], errors="coerce").gt(0).all():
        errors.append("source-first condition matrix must disclose right-censored episodes")
    if not summary["sample_policy"].eq(
        "sample_count_disclosed_not_used_as_automatic_rejection"
    ).all():
        errors.append("source-first sample policy drift")
    if any(token in " ".join(summary["condition_rule"].astype(str)) for token in ("lag_d8_14", "consecutive_ge3")):
        errors.append("source-first condition matrix restored the rejected lag or three-month gate")

    required_markdown = (
        "來源優先條件稽核",
        "事後",
        "不是正式買入勝率",
        "事欣科",
        "南亞",
        "第一個突破",
        "EPS、毛利率、營益率、營業利益、業外與淨利均未納入",
    )
    for token in required_markdown:
        if token not in markdown:
            errors.append(f"source-first markdown omits required explanation: {token}")
    return errors


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Validate the revenue source-first condition audit."
    )
    parser.add_argument(
        "--projection-manifest",
        type=Path,
        default=None,
    )
    parser.add_argument("--revenue-history", type=Path, default=REVENUE_HISTORY_CSV)
    parser.add_argument(
        "--monthly-resolution",
        type=Path,
        default=MONTHLY_REVENUE_CROSS_MARKET_RESOLUTION_CSV,
    )
    return parser.parse_args(argv)


def main() -> int:
    args = parse_args()
    errors = validate(
        revenue_path=args.revenue_history,
        resolution_path=args.monthly_resolution,
        projection_manifest_path=args.projection_manifest,
    )
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1
    print("revenue_unreacted_range source-first condition audit validation passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
