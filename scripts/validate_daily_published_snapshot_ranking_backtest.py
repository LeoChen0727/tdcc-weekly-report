from __future__ import annotations

import hashlib
import json
import math
import subprocess
import sys
from pathlib import Path
from typing import Any

import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent))

from daily_snapshot_revision_utils import (  # noqa: E402
    normalize_revision_manifest_schema,
    select_latest_snapshot_revisions,
)
from tracking_utils import (  # noqa: E402
    DOCS_LATEST_DIR,
    HISTORY_DIR,
    LATEST_DIR,
    RESEARCH_LATEST_DIR,
    read_csv,
    safe_str,
)


ROOT = Path(__file__).resolve().parents[1]
SNAPSHOT_DIR = HISTORY_DIR / "daily_model_snapshots"
MANIFEST_CSV = SNAPSHOT_DIR / "daily_published_model_snapshot_manifest.csv"
RESEARCH_HISTORY_DIR = HISTORY_DIR / "research"
OUT_CSV = RESEARCH_LATEST_DIR / "daily_published_snapshot_ranking_backtest_latest.csv"
OUT_MD = RESEARCH_LATEST_DIR / "daily_published_snapshot_ranking_backtest_latest.md"
EVENTS_CSV = RESEARCH_HISTORY_DIR / "daily_published_snapshot_ranking_events.csv"
DOCS_CSV = DOCS_LATEST_DIR / OUT_CSV.name
DOCS_MD = DOCS_LATEST_DIR / OUT_MD.name
VOLUME_V2_LINEAGE_AUDIT_CSV = (
    LATEST_DIR / "volume_v2_warrant_lineage_history_audit_latest.csv"
)
VOLUME_V2_LINEAGE_AUDIT_SOURCE_IDENTITY = (
    "output/latest/volume_v2_warrant_lineage_history_audit_latest.csv"
)

SNAPSHOT_REVISION_POLICY = "latest_revision_per_report_date_artifact"
VOLUME_V2_LINEAGE_AUDIT_VERSION = "volume_v2_warrant_lineage_history_audit_v5"
VOLUME_V2_MODEL_IDS = {
    "volume_range_breakout_v2_low_position_volume_attack",
    "volume_range_breakout_v2_mid_position_momentum_attack",
    "volume_range_breakout_v2_high_position_volume_attack",
}
VOLUME_V2_EXACT_PAIRED_SOURCE_RESOLUTIONS = {
    "current_worktree_exact_source_files",
    "current_worktree_pending_same_date_revision_exact_sources",
    "published_snapshot_exact_current_sources_pending_commit",
    "manifest_pipeline_commit_exact_source_blob",
    "snapshot_history_exact_blob_fallback",
    "manifest_history_first_exact_row_same_commit_sources",
    "legacy_git_manifest_recovered_same_commit_exact_sources",
}
REQUIRED_ARTIFACT_IDS = {
    "model_signals_for_report",
    "volume_breakout_operation_section",
}
HORIZONS = (1, 3, 5, 10)


SUMMARY_REQUIRED_COLUMNS = {
    "segment_type",
    "segment_value",
    "source_artifact",
    "model_id",
    "sample_size",
    "report_date_min",
    "report_date_max",
    "snapshot_report_count",
    "evaluated_d1_count",
    "win_rate_d1",
    "avg_return_d1",
    "median_return_d1",
    "evaluated_d3_count",
    "evaluated_d5_count",
    "evaluated_d10_count",
    "confidence_status",
    "lineage_excluded_count",
    "advisory_only",
    "generated_at",
}

EVENT_REQUIRED_COLUMNS = {
    "source_artifact",
    "snapshot_report_date",
    "snapshot_revision",
    "snapshot_revision_policy",
    "published_source_snapshot_sha256",
    "published_source_row_sha256",
    "stock_id",
    "model_id",
    "model_name_zh",
    "report_bucket",
    "mainstream_segment",
    "rank_bucket",
    "score_decile",
    "operation_section",
    "row_action_status",
    "buy_rank_eligible",
    "anchor_date",
    "entry_date",
    "entry_open_price",
    "forward_window_status",
    "return_d1_close_pct",
    "return_d3_close_pct",
    "return_d5_close_pct",
    "return_d10_close_pct",
    "mfe_d1_pct",
    "mae_d1_pct",
    "mfe_d3_pct",
    "mae_d3_pct",
    "mfe_d5_pct",
    "mae_d5_pct",
    "mfe_d10_pct",
    "mae_d10_pct",
    "ranking_evaluation_eligible",
    "trade_eligible",
    "lineage_gate_status",
    "lineage_signal_date",
    "lineage_formal_row_disposition",
    "lineage_evidence_status",
    "lineage_audit_source",
    "lineage_audit_source_sha256",
    "lineage_formal_row_sha256",
    "lineage_observed_formal_row_sha256",
    "lineage_formal_snapshot_sha256",
    "lineage_observed_formal_snapshot_sha256",
    "lineage_paired_source_resolution",
    "lineage_production_code_sha256",
    "lineage_watch_artifact_sha256",
    "lineage_candidate_artifact_sha256",
    "lineage_official_warrant_artifact_sha256",
    "lineage_legacy_precontract_revision_history_status",
    "lineage_historical_promotion_evidence_eligible",
    "lineage_audit_version",
    "lineage_audit_row_type",
    "lineage_formal_snapshot_revision",
    "lineage_snapshot_commit_sha",
    "lineage_paired_source_commit_sha",
    "summary_evidence_eligible",
    "lineage_gate_pass_for_promotion_evidence",
    "research_note",
    "generated_at",
}

LINEAGE_SOURCE_SHA_COLUMNS = (
    "lineage_audit_source_sha256",
    "lineage_production_code_sha256",
    "lineage_watch_artifact_sha256",
    "lineage_candidate_artifact_sha256",
    "lineage_official_warrant_artifact_sha256",
)

AUDIT_REQUIRED_COLUMNS = {
    "audit_version",
    "audit_row_type",
    "snapshot_report_date",
    "snapshot_revision",
    "signal_date",
    "model_id",
    "stock_id",
    "formal_row_sha256",
    "formal_snapshot_sha256",
    "formal_snapshot_path",
    "paired_source_resolution",
    "production_code_sha256",
    "watch_artifact_sha256",
    "watch_artifact_path",
    "candidate_artifact_sha256",
    "candidate_artifact_path",
    "official_warrant_artifact_sha256",
    "official_warrant_artifact_path",
    "formal_row_disposition",
    "evidence_status",
    "legacy_precontract_revision_history_status",
    "historical_promotion_evidence_eligible",
    "snapshot_commit_sha",
    "paired_source_commit_sha",
}

FORBIDDEN_SOURCE_NAMES = {
    "daily_candidate_model_signals_for_report_latest.csv",
    "daily_volume_breakout_operation_section_latest.csv",
    "volume_breakout_operation_pdf_preview_latest.csv",
    "historical_pattern_operation_registry_latest.csv",
    "approved_operation_patterns_latest.csv",
}


def compare_docs_copy() -> list[str]:
    errors: list[str] = []
    for output, docs in [(OUT_CSV, DOCS_CSV), (OUT_MD, DOCS_MD)]:
        if not output.exists():
            errors.append(f"missing output artifact: {output.as_posix()}")
            continue
        if not docs.exists():
            errors.append(f"missing docs/latest copy: {docs.as_posix()}")
            continue
        if output.read_text(encoding="utf-8") != docs.read_text(encoding="utf-8"):
            errors.append(f"docs/latest copy differs from output/latest: {docs.as_posix()}")
    return errors


def validate_summary() -> list[str]:
    errors: list[str] = []
    summary = read_csv(OUT_CSV, dtype=str).fillna("")
    if summary.empty:
        return [f"empty summary artifact: {OUT_CSV.as_posix()}"]
    missing = SUMMARY_REQUIRED_COLUMNS - set(summary.columns)
    if missing:
        errors.append(f"summary missing columns: {sorted(missing)}")
        return errors

    if set(summary["advisory_only"].astype(str)) != {"True"}:
        errors.append("summary must be advisory_only=True for every row")
    required_segment_types = {
        "model_overall",
        "model_mainstream_segment",
        "model_rank_bucket",
        "model_score_decile",
        "volume_operation_section",
    }
    observed_segment_types = set(summary["segment_type"].astype(str))
    missing_segments = sorted(required_segment_types - observed_segment_types)
    if missing_segments:
        errors.append(f"summary missing required segment types: {missing_segments}")

    volume_sections = summary[summary["segment_type"].astype(str).eq("volume_operation_section")]
    if volume_sections.empty:
        errors.append("summary must include volume_operation_section rows")
    else:
        joined_values = "\n".join(volume_sections["segment_value"].astype(str).tolist())
        for section in [
            "confirmed_operation",
            "confirmed_unranked_operation",
            "pending_confirmation",
            "active_operation",
        ]:
            if section not in joined_values:
                errors.append(f"summary must evaluate volume operation section separately: missing {section}")
    return errors


def _pct_text(value: float) -> str:
    if math.isnan(value):
        return ""
    return f"{value:.2f}%"


def _numeric_series(frame: pd.DataFrame, column: str) -> pd.Series:
    if column not in frame.columns:
        return pd.Series(dtype=float)
    return pd.to_numeric(frame[column], errors="coerce")


def _independent_summary_group(
    part: pd.DataFrame,
    segment_type: str,
    segment_value: str,
    generated_at: str,
) -> dict[str, Any]:
    row: dict[str, Any] = {
        "segment_type": segment_type,
        "segment_value": segment_value,
        "source_artifact": safe_str(part["source_artifact"].iloc[0]),
        "model_id": safe_str(part["model_id"].iloc[0]),
        "model_name_zh": safe_str(part["model_name_zh"].iloc[0]),
        "sample_size": len(part),
        "report_date_min": safe_str(part["snapshot_report_date"].min()),
        "report_date_max": safe_str(part["snapshot_report_date"].max()),
        "snapshot_report_count": part["snapshot_report_date"].nunique(),
        "generated_at": generated_at,
    }
    for horizon in HORIZONS:
        returns = _numeric_series(part, f"return_d{horizon}_close_pct").dropna()
        row[f"evaluated_d{horizon}_count"] = len(returns)
        row[f"win_rate_d{horizon}"] = _pct_text(
            returns.gt(0).mean() * 100.0 if len(returns) else math.nan
        )
        row[f"avg_return_d{horizon}"] = _pct_text(
            returns.mean() if len(returns) else math.nan
        )
        row[f"median_return_d{horizon}"] = _pct_text(
            returns.median() if len(returns) else math.nan
        )
        mfe = _numeric_series(part, f"mfe_d{horizon}_pct").dropna()
        mae = _numeric_series(part, f"mae_d{horizon}_pct").dropna()
        row[f"avg_mfe_d{horizon}"] = _pct_text(
            mfe.mean() if len(mfe) else math.nan
        )
        row[f"avg_mae_d{horizon}"] = _pct_text(
            mae.mean() if len(mae) else math.nan
        )
    minimum_evaluated = max(
        int(row["evaluated_d1_count"]), int(row["evaluated_d3_count"])
    )
    row["confidence_status"] = (
        "ok_first_pass" if minimum_evaluated >= 100 else "small_or_early_snapshot_sample"
    )
    row["advisory_only"] = "True"
    return row


def recompute_summary_from_events(
    events: pd.DataFrame,
    generated_at: str,
) -> pd.DataFrame:
    eligible = events[events["summary_evidence_eligible"].astype(str).eq("True")]
    excluded = events[~events["summary_evidence_eligible"].astype(str).eq("True")]
    rows: list[dict[str, Any]] = []
    group_specs = (
        ("model_overall", ("source_artifact", "model_id")),
        ("model_report_bucket", ("source_artifact", "model_id", "report_bucket")),
        (
            "model_mainstream_segment",
            ("source_artifact", "model_id", "mainstream_segment"),
        ),
        ("model_rank_bucket", ("source_artifact", "model_id", "rank_bucket")),
        ("model_score_decile", ("source_artifact", "model_id", "score_decile")),
        (
            "volume_operation_section",
            ("source_artifact", "model_id", "operation_section"),
        ),
    )
    for segment_type, columns in group_specs:
        for key, part in eligible.groupby(list(columns), dropna=False):
            values = key if isinstance(key, tuple) else (key,)
            if (
                segment_type == "volume_operation_section"
                and values[0] != "volume_breakout_operation_section"
            ):
                continue
            if (
                segment_type != "volume_operation_section"
                and values[0] == "volume_breakout_operation_section"
            ):
                continue
            segment_value = "|".join(
                safe_str(value) for value in values[1:] if safe_str(value)
            )
            summary_row = _independent_summary_group(
                part, segment_type, segment_value, generated_at
            )
            summary_row["lineage_excluded_count"] = len(
                excluded[
                    excluded["source_artifact"].astype(str).eq(
                        summary_row["source_artifact"]
                    )
                    & excluded["model_id"].astype(str).eq(summary_row["model_id"])
                ]
            )
            rows.append(summary_row)

    if not excluded.empty:
        exclusion_columns = (
            "source_artifact",
            "model_id",
            "lineage_gate_status",
            "lineage_formal_row_disposition",
        )
        for key, part in excluded.groupby(list(exclusion_columns), dropna=False):
            source_artifact, model_id, gate_status, disposition = key
            row: dict[str, Any] = {
                "segment_type": "lineage_exclusion",
                "segment_value": "|".join(
                    safe_str(value) for value in (model_id, gate_status, disposition)
                ),
                "source_artifact": safe_str(source_artifact),
                "model_id": safe_str(model_id),
                "model_name_zh": safe_str(part["model_name_zh"].iloc[0]),
                "sample_size": len(part),
                "report_date_min": safe_str(part["snapshot_report_date"].min()),
                "report_date_max": safe_str(part["snapshot_report_date"].max()),
                "snapshot_report_count": part["snapshot_report_date"].nunique(),
                "generated_at": generated_at,
                "confidence_status": "excluded_from_summary_and_promotion_evidence",
                "advisory_only": "True",
                "lineage_excluded_count": len(part),
            }
            for horizon in HORIZONS:
                row[f"evaluated_d{horizon}_count"] = 0
                row[f"win_rate_d{horizon}"] = ""
                row[f"avg_return_d{horizon}"] = ""
                row[f"median_return_d{horizon}"] = ""
                row[f"avg_mfe_d{horizon}"] = ""
                row[f"avg_mae_d{horizon}"] = ""
            rows.append(row)

    existing_sections = {
        safe_str(row.get("segment_value")).split("|")[-1]
        for row in rows
        if safe_str(row.get("segment_type")) == "volume_operation_section"
    }
    for section in (
        "confirmed_operation",
        "confirmed_unranked_operation",
        "pending_confirmation",
        "active_operation",
    ):
        if section in existing_sections:
            continue
        row = {
            "segment_type": "volume_operation_section",
            "segment_value": f"volume_range_breakout|{section}",
            "source_artifact": "volume_breakout_operation_section",
            "model_id": "volume_range_breakout",
            "model_name_zh": "",
            "sample_size": 0,
            "report_date_min": "",
            "report_date_max": "",
            "snapshot_report_count": 0,
            "generated_at": generated_at,
            "confidence_status": "empty_section_no_data_rows",
            "advisory_only": "True",
        }
        for horizon in HORIZONS:
            row[f"evaluated_d{horizon}_count"] = 0
            row[f"win_rate_d{horizon}"] = ""
            row[f"avg_return_d{horizon}"] = ""
            row[f"median_return_d{horizon}"] = ""
            row[f"avg_mfe_d{horizon}"] = ""
            row[f"avg_mae_d{horizon}"] = ""
        rows.append(row)
    return pd.DataFrame(rows).sort_values(
        ["segment_type", "model_id", "segment_value"]
    ).reset_index(drop=True)


def validate_summary_against_events(
    summary: pd.DataFrame,
    events: pd.DataFrame,
) -> list[str]:
    if summary.empty or events.empty:
        return []
    required_inputs = {
        "generated_at",
        "summary_evidence_eligible",
        "source_artifact",
        "model_id",
        "model_name_zh",
        "snapshot_report_date",
        "report_bucket",
        "mainstream_segment",
        "rank_bucket",
        "score_decile",
        "operation_section",
        "lineage_gate_status",
        "lineage_formal_row_disposition",
    }
    missing_inputs = sorted(required_inputs - set(events.columns))
    if missing_inputs:
        return [f"events missing independent summary inputs: {missing_inputs}"]
    generated_values = sorted(
        {safe_str(value) for value in events["generated_at"] if safe_str(value)}
    )
    if len(generated_values) != 1:
        return ["events must contain exactly one generated_at for summary replay"]
    expected = recompute_summary_from_events(events, generated_values[0]).fillna("")
    observed = summary.fillna("")
    comparison_columns = sorted(set(expected.columns) - {"model_name_zh"})
    missing = sorted(set(comparison_columns) - set(observed.columns))
    if missing:
        return [f"summary missing independent replay columns: {missing}"]
    sort_columns = ["segment_type", "model_id", "segment_value", "source_artifact"]
    expected = expected.sort_values(sort_columns).reset_index(drop=True)
    observed = observed.sort_values(sort_columns).reset_index(drop=True)
    if len(expected) != len(observed):
        return [
            "summary row count differs from independent event replay: "
            f"expected={len(expected)} observed={len(observed)}"
        ]
    expected_values = expected[comparison_columns].astype(str)
    observed_values = observed[comparison_columns].astype(str)
    mismatches = expected_values.ne(observed_values)
    if mismatches.any().any():
        row_index, column_index = next(
            (row, column)
            for row, values in mismatches.iterrows()
            for column, differs in values.items()
            if differs
        )
        return [
            "summary differs from independent event replay: "
            f"row={row_index} column={column_index} "
            f"expected={expected_values.at[row_index, column_index]!r} "
            f"observed={observed_values.at[row_index, column_index]!r}"
        ]
    return []


def validate_events(events: pd.DataFrame | None = None) -> list[str]:
    errors: list[str] = []
    if events is None:
        events = read_csv(EVENTS_CSV, dtype=str).fillna("")
    if events.empty:
        return [f"empty event artifact: {EVENTS_CSV.as_posix()}"]
    missing = EVENT_REQUIRED_COLUMNS - set(events.columns)
    if missing:
        errors.append(f"events missing columns: {sorted(missing)}")
        return errors

    source_artifacts = set(events["source_artifact"].astype(str))
    expected = {"model_signals_for_report", "volume_breakout_operation_section"}
    if not expected.issubset(source_artifacts):
        errors.append(f"events missing expected source_artifacts: {sorted(expected - source_artifacts)}")

    if events["research_note"].astype(str).str.contains("latest|pdf_preview|registry", case=False, regex=True).any():
        errors.append("events research_note must not reference latest/PDF/research registry sources")

    bad_dates = events[~events["snapshot_report_date"].astype(str).str.fullmatch(r"20\d{6}")]
    if not bad_dates.empty:
        errors.append("events contain invalid snapshot_report_date values")
    if not events["snapshot_revision"].astype(str).str.fullmatch(r"r[1-9][0-9]*").all():
        errors.append("events contain invalid snapshot_revision values")
    if set(events["snapshot_revision_policy"].astype(str)) != {
        SNAPSHOT_REVISION_POLICY
    }:
        errors.append(
            "events must use the explicit latest revision snapshot policy"
        )

    model_events = events[events["source_artifact"].astype(str).eq("model_signals_for_report")]
    if model_events.empty:
        errors.append("events must contain model_signals_for_report rows")
    else:
        bad_model_trade = model_events[model_events["trade_eligible"].astype(str).eq("True")]
        if not bad_model_trade.empty:
            errors.append("model_signals_for_report rows must not be trade_eligible=True")
        non_volume_v2 = model_events[
            ~model_events["model_id"].astype(str).isin(VOLUME_V2_MODEL_IDS)
        ]
        bad_model_ranking = non_volume_v2[
            ~non_volume_v2["ranking_evaluation_eligible"].astype(str).eq("True")
        ]
        if not bad_model_ranking.empty:
            errors.append(
                "non-volume-v2 model_signals_for_report rows must be "
                "ranking_evaluation_eligible=True"
            )

    operation = events[events["source_artifact"].astype(str).eq("volume_breakout_operation_section")]
    if operation.empty:
        errors.append("events must contain volume operation rows")
    else:
        expected_trade_eligible = (
            operation["operation_section"].astype(str).eq("confirmed_operation")
            & operation["row_action_status"]
            .astype(str)
            .eq("confirmed_buy_candidate")
            & operation["buy_rank_eligible"].astype(str).eq("True")
            & operation["summary_evidence_eligible"].astype(str).eq("True")
        )
        observed_trade_eligible = operation["trade_eligible"].astype(str).eq("True")
        if not expected_trade_eligible.eq(observed_trade_eligible).all():
            errors.append(
                "volume operation trade_eligible does not match the complete "
                "confirmed-operation contract"
            )
    return errors


def validate_volume_v2_lineage(events: pd.DataFrame) -> list[str]:
    errors: list[str] = []
    if events.empty:
        return errors
    missing = EVENT_REQUIRED_COLUMNS - set(events.columns)
    if missing:
        return [f"events missing formal-lineage columns: {sorted(missing)}"]
    volume = events[events["model_id"].astype(str).isin(VOLUME_V2_MODEL_IDS)].copy()
    if volume.empty:
        return ["events contain no volume-v2 rows for formal-lineage validation"]

    allowed_status = {"verified_clean", "non_clean_excluded", "uncovered_fail_closed"}
    invalid_status = volume[~volume["lineage_gate_status"].astype(str).isin(allowed_status)]
    if not invalid_status.empty:
        errors.append("volume-v2 events contain invalid lineage_gate_status")

    historical_values = set(
        volume["lineage_historical_promotion_evidence_eligible"].astype(str)
    )
    invalid_historical_values = historical_values - {"True", "False"}
    if invalid_historical_values:
        errors.append(
            "volume-v2 events contain invalid "
            "lineage_historical_promotion_evidence_eligible values"
        )

    clean = volume[volume["lineage_gate_status"].astype(str).eq("verified_clean")]
    if not clean.empty:
        promotion_clean = clean[
            clean["lineage_historical_promotion_evidence_eligible"]
            .astype(str)
            .eq("True")
        ]
        for field in (
            "summary_evidence_eligible",
            "lineage_gate_pass_for_promotion_evidence",
        ):
            if not promotion_clean.empty and not promotion_clean[field].astype(
                str
            ).eq("True").all():
                errors.append(
                    "historically eligible verified_clean volume-v2 rows require "
                    f"{field}=True"
                )
        clean_model_signals = promotion_clean[
            promotion_clean["source_artifact"]
            .astype(str)
            .eq("model_signals_for_report")
        ]
        if not clean_model_signals.empty and not clean_model_signals[
            "ranking_evaluation_eligible"
        ].astype(str).eq("True").all():
            errors.append(
                "verified_clean volume-v2 model signal rows require "
                "ranking_evaluation_eligible=True"
            )
        historical_blocked = clean[
            clean["lineage_historical_promotion_evidence_eligible"]
            .astype(str)
            .eq("False")
        ]
        for field in (
            "summary_evidence_eligible",
            "lineage_gate_pass_for_promotion_evidence",
            "ranking_evaluation_eligible",
            "trade_eligible",
        ):
            if not historical_blocked.empty and not historical_blocked[field].astype(
                str
            ).eq("False").all():
                errors.append(
                    "historically incomplete verified_clean volume-v2 rows require "
                    f"{field}=False"
                )
        if not clean["lineage_formal_row_disposition"].astype(str).eq(
            "verified_clean"
        ).all():
            errors.append("verified_clean volume-v2 rows require verified_clean disposition")
        if not clean["lineage_evidence_status"].astype(str).eq("complete").all():
            errors.append("verified_clean volume-v2 rows require complete evidence")
        if not clean["lineage_paired_source_resolution"].astype(str).isin(
            VOLUME_V2_EXACT_PAIRED_SOURCE_RESOLUTIONS
        ).all():
            errors.append("verified_clean volume-v2 rows require exact paired source resolution")
        if not clean["lineage_formal_row_sha256"].astype(str).eq(
            clean["lineage_observed_formal_row_sha256"].astype(str)
        ).all():
            errors.append("verified_clean volume-v2 formal row SHA must match observed row SHA")
        if not clean["lineage_formal_snapshot_sha256"].astype(str).eq(
            clean["lineage_observed_formal_snapshot_sha256"].astype(str)
        ).all():
            errors.append(
                "verified_clean volume-v2 formal snapshot SHA must match observed snapshot SHA"
            )
        for field in (
            *LINEAGE_SOURCE_SHA_COLUMNS,
            "lineage_formal_row_sha256",
            "lineage_formal_snapshot_sha256",
        ):
            if not clean[field].astype(str).str.fullmatch(r"[0-9a-f]{64}").all():
                errors.append(f"verified_clean volume-v2 rows require canonical {field}")

    excluded = volume[
        volume["lineage_gate_status"].astype(str).isin(
            {"non_clean_excluded", "uncovered_fail_closed"}
        )
    ]
    if not excluded.empty:
        for field in (
            "summary_evidence_eligible",
            "lineage_gate_pass_for_promotion_evidence",
            "ranking_evaluation_eligible",
            "trade_eligible",
        ):
            if not excluded[field].astype(str).eq("False").all():
                errors.append(f"non-clean volume-v2 rows require {field}=False")
    return errors


def _normalize_date(value: Any) -> str:
    digits = "".join(character for character in safe_str(value) if character.isdigit())
    return digits if len(digits) == 8 else ""


def _normalize_stock_id(value: Any) -> str:
    text = safe_str(value)
    if text.endswith(".0"):
        text = text[:-2]
    digits = "".join(character for character in text if character.isdigit())
    if not digits:
        return ""
    return digits.zfill(4) if len(digits) <= 4 else digits


def _is_sha256(value: Any) -> bool:
    text = safe_str(value).lower()
    return len(text) == 64 and all(character in "0123456789abcdef" for character in text)


def _is_git_commit_sha(value: Any) -> bool:
    text = safe_str(value).lower()
    return len(text) in {40, 64} and all(
        character in "0123456789abcdef" for character in text
    )


def _sha256_file(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def _canonical_text_bytes(payload: bytes) -> bytes:
    text = payload.decode("utf-8-sig")
    return text.replace("\r\n", "\n").replace("\r", "\n").encode("utf-8")


def _canonical_file_sha256(path: Path) -> str:
    return hashlib.sha256(_canonical_text_bytes(path.read_bytes())).hexdigest()


def _canonical_row_sha256(row: pd.Series | dict[str, Any]) -> str:
    values = row.to_dict() if isinstance(row, pd.Series) else dict(row)
    normalized = {str(key): safe_str(value) for key, value in values.items()}
    payload = json.dumps(
        normalized,
        ensure_ascii=False,
        sort_keys=True,
        separators=(",", ":"),
    ).encode("utf-8")
    return hashlib.sha256(_canonical_text_bytes(payload)).hexdigest()


def _normalize_bool(value: Any) -> str:
    return (
        "True"
        if safe_str(value).lower() in {"true", "1", "1.0", "yes", "y"}
        else "False"
    )


def _repo_relative_audit_path(value: Any, expected_prefix: str) -> str:
    text = safe_str(value)
    prefix = expected_prefix.strip("/")
    if (
        not text
        or "\\" in text
        or text.startswith("/")
        or (len(text) >= 2 and text[0].isalpha() and text[1] == ":")
        or not (text == prefix or text.startswith(prefix + "/"))
    ):
        return ""
    parts = text.split("/")
    if any(part in {"", ".", ".."} for part in parts):
        return ""
    return text


def _git_blob_at_commit(
    repository_root: Path,
    commit_sha: str,
    repo_path: str,
    cache: dict[tuple[str, str], bytes | None],
) -> bytes | None:
    key = (commit_sha, repo_path)
    if key in cache:
        return cache[key]
    if not _is_git_commit_sha(commit_sha) or not repo_path:
        cache[key] = None
        return None
    completed = subprocess.run(
        ["git", "show", f"{commit_sha}:{repo_path}"],
        cwd=repository_root,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
    )
    cache[key] = completed.stdout if completed.returncode == 0 else None
    return cache[key]


def _git_commit_exists(
    repository_root: Path,
    commit_sha: str,
    cache: dict[str, bool],
) -> bool:
    if commit_sha in cache:
        return cache[commit_sha]
    if not _is_git_commit_sha(commit_sha):
        cache[commit_sha] = False
        return False
    completed = subprocess.run(
        ["git", "cat-file", "-t", commit_sha],
        cwd=repository_root,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
        text=True,
    )
    cache[commit_sha] = (
        completed.returncode == 0 and completed.stdout.strip() == "commit"
    )
    return cache[commit_sha]


def validate_events_against_published_snapshots(
    events: pd.DataFrame,
    *,
    snapshot_dir: Path = SNAPSHOT_DIR,
    manifest_path: Path = MANIFEST_CSV,
    repository_root: Path = ROOT,
) -> list[str]:
    """Bind event rows to the selected immutable published source snapshots."""

    if events.empty:
        return []
    required = {
        "source_artifact",
        "snapshot_report_date",
        "snapshot_revision",
        "published_source_snapshot_sha256",
        "published_source_row_sha256",
        "stock_id",
        "model_id",
        "lineage_signal_date",
    }
    missing = sorted(required - set(events.columns))
    if missing:
        return [f"events missing published snapshot binding columns: {missing}"]
    errors: list[str] = []
    source_usage_key = [
        "source_artifact",
        "snapshot_report_date",
        "snapshot_revision",
        "published_source_snapshot_sha256",
        "published_source_row_sha256",
    ]
    duplicate_usage = events.duplicated(subset=source_usage_key, keep=False)
    if duplicate_usage.any():
        duplicate_keys = (
            events.loc[duplicate_usage, source_usage_key]
            .drop_duplicates()
            .to_dict(orient="records")
        )
        errors.append(
            "published source rows must map to exactly one event: "
            f"duplicates={duplicate_keys}"
        )
    try:
        selected = {
            artifact_id: select_latest_snapshot_revisions(
                snapshot_dir,
                artifact_id,
                manifest_path=manifest_path,
                repository_root=repository_root,
            )
            for artifact_id in REQUIRED_ARTIFACT_IDS
        }
    except Exception as exc:
        return [f"published event snapshot selection failed: {exc}"]
    revision_index = {
        (artifact_id, revision.report_date): revision
        for artifact_id, revisions in selected.items()
        for revision in revisions
    }
    snapshot_cache: dict[tuple[str, str], tuple[str, dict[str, list[pd.Series]]]] = {}
    for index, event in events.iterrows():
        artifact_id = safe_str(event.get("source_artifact"))
        report_date = _normalize_date(event.get("snapshot_report_date"))
        label = (
            f"event_index={index} artifact_id={artifact_id} report_date={report_date} "
            f"model_id={safe_str(event.get('model_id'))} "
            f"stock_id={safe_str(event.get('stock_id'))}"
        )
        revision = revision_index.get((artifact_id, report_date))
        if revision is None:
            errors.append(f"{label}: no selected published snapshot revision")
            continue
        if safe_str(event.get("snapshot_revision")) != revision.revision:
            errors.append(f"{label}: event snapshot_revision is not manifest maximum")
        cache_key = (artifact_id, report_date)
        cached = snapshot_cache.get(cache_key)
        if cached is None:
            try:
                source_frame = pd.read_csv(
                    revision.path, dtype=str, keep_default_na=False
                )
            except Exception as exc:
                errors.append(f"{label}: cannot read published source snapshot: {exc}")
                continue
            rows_by_hash: dict[str, list[pd.Series]] = {}
            for _, source_row in source_frame.iterrows():
                rows_by_hash.setdefault(_canonical_row_sha256(source_row), []).append(
                    source_row
                )
            cached = (_canonical_file_sha256(revision.path), rows_by_hash)
            snapshot_cache[cache_key] = cached
        source_snapshot_sha, rows_by_hash = cached
        if safe_str(event.get("published_source_snapshot_sha256")) != source_snapshot_sha:
            errors.append(f"{label}: published source snapshot SHA mismatch")
        source_row_sha = safe_str(event.get("published_source_row_sha256"))
        source_rows = rows_by_hash.get(source_row_sha, [])
        if len(source_rows) != 1:
            errors.append(
                f"{label}: published source row hash does not resolve exactly once"
            )
            continue
        source_row = source_rows[0]
        if safe_str(source_row.get("model_id")) != safe_str(event.get("model_id")):
            errors.append(f"{label}: model_id differs from published source row")
        if _normalize_stock_id(source_row.get("stock_id")) != _normalize_stock_id(
            event.get("stock_id")
        ):
            errors.append(f"{label}: stock_id differs from published source row")
        if artifact_id == "model_signals_for_report":
            source_signal_date = _normalize_date(source_row.get("signal_date"))
            expected_fields = {
                "model_score": safe_str(source_row.get("model_score")),
                "display_rank": safe_str(source_row.get("display_rank"))
                or safe_str(source_row.get("model_rank")),
                "report_line": safe_str(source_row.get("report_line")),
                "report_bucket": safe_str(source_row.get("report_bucket")),
            }
        elif artifact_id == "volume_breakout_operation_section":
            source_signal_date = _normalize_date(
                source_row.get("signal_date")
            ) or _normalize_date(source_row.get("daily_signal_date"))
            expected_fields = {
                "operation_section": safe_str(source_row.get("pdf_section")),
                "row_action_status": safe_str(source_row.get("row_action_status")),
                "buy_rank_eligible": _normalize_bool(
                    source_row.get("buy_rank_eligible")
                ),
                "display_rank": safe_str(source_row.get("display_order")),
                "model_score": safe_str(source_row.get("research_score")),
            }
        else:
            errors.append(f"{label}: unsupported published source artifact")
            continue
        if source_signal_date != _normalize_date(event.get("lineage_signal_date")):
            errors.append(f"{label}: lineage_signal_date differs from published source row")
        for field, expected_value in expected_fields.items():
            if safe_str(event.get(field)) != expected_value:
                errors.append(f"{label}: {field} differs from published source row")
    return errors


def validate_volume_v2_formal_revision_binding(
    events: pd.DataFrame,
    *,
    snapshot_dir: Path = SNAPSHOT_DIR,
    manifest_path: Path = MANIFEST_CSV,
    repository_root: Path = ROOT,
) -> list[str]:
    """Cross-bind published events and audit evidence to the same max formal revision."""

    if events.empty:
        return []
    required = {
        "source_artifact",
        "snapshot_report_date",
        "snapshot_revision",
        "published_source_snapshot_sha256",
        "published_source_row_sha256",
        "stock_id",
        "model_id",
        "lineage_signal_date",
        "lineage_formal_snapshot_revision",
        "lineage_formal_snapshot_sha256",
        "lineage_observed_formal_snapshot_sha256",
        "lineage_formal_row_sha256",
        "lineage_observed_formal_row_sha256",
    }
    missing = sorted(required - set(events.columns))
    if missing:
        return [f"events missing formal revision cross-binding columns: {missing}"]
    volume = events[events["model_id"].astype(str).isin(VOLUME_V2_MODEL_IDS)].copy()
    if volume.empty:
        return ["events contain no volume-v2 rows for formal revision cross-binding"]
    try:
        revisions = select_latest_snapshot_revisions(
            snapshot_dir,
            "model_signals_for_report",
            manifest_path=manifest_path,
            repository_root=repository_root,
        )
    except Exception as exc:
        return [f"formal revision cross-binding selection failed: {exc}"]
    revision_by_date = {revision.report_date: revision for revision in revisions}
    formal_cache: dict[str, tuple[str, dict[tuple[str, str, str], list[str]]]] = {}
    errors: list[str] = []
    for index, event in volume.iterrows():
        signal_date = _normalize_date(event.get("lineage_signal_date"))
        model_id = safe_str(event.get("model_id"))
        stock_id = _normalize_stock_id(event.get("stock_id"))
        label = (
            f"event_index={index} signal_date={signal_date} model_id={model_id} "
            f"stock_id={stock_id}"
        )
        revision = revision_by_date.get(signal_date)
        if revision is None:
            errors.append(f"{label}: no manifest-max formal snapshot revision")
            continue
        cached = formal_cache.get(signal_date)
        if cached is None:
            try:
                formal = pd.read_csv(revision.path, dtype=str, keep_default_na=False)
            except Exception as exc:
                errors.append(f"{label}: cannot read manifest-max formal snapshot: {exc}")
                continue
            row_index: dict[tuple[str, str, str], list[str]] = {}
            for _, row in formal.iterrows():
                row_key = (
                    _normalize_date(row.get("signal_date")) or revision.report_date,
                    safe_str(row.get("model_id")),
                    _normalize_stock_id(row.get("stock_id")),
                )
                row_index.setdefault(row_key, []).append(_canonical_row_sha256(row))
            cached = (_canonical_file_sha256(revision.path), row_index)
            formal_cache[signal_date] = cached
        formal_snapshot_sha, formal_rows = cached
        row_hashes = formal_rows.get((signal_date, model_id, stock_id), [])
        if len(row_hashes) != 1:
            errors.append(
                f"{label}: formal row does not resolve exactly once in manifest-max revision"
            )
            continue
        formal_row_sha = row_hashes[0]
        expected_pairs = {
            "lineage_formal_snapshot_revision": revision.revision,
            "lineage_formal_snapshot_sha256": formal_snapshot_sha,
            "lineage_observed_formal_snapshot_sha256": formal_snapshot_sha,
            "lineage_formal_row_sha256": formal_row_sha,
            "lineage_observed_formal_row_sha256": formal_row_sha,
        }
        for field, expected in expected_pairs.items():
            if safe_str(event.get(field)) != expected:
                errors.append(
                    f"{label}: {field} is not bound to manifest-max formal revision"
                )
        if safe_str(event.get("source_artifact")) == "model_signals_for_report":
            direct_pairs = {
                "snapshot_report_date": signal_date,
                "snapshot_revision": revision.revision,
                "published_source_snapshot_sha256": formal_snapshot_sha,
                "published_source_row_sha256": formal_row_sha,
            }
            for field, expected in direct_pairs.items():
                if safe_str(event.get(field)) != expected:
                    errors.append(
                        f"{label}: model event {field} differs from formal lineage"
                    )
    return errors


def validate_volume_v2_audit_binding(
    events: pd.DataFrame,
    audit_path: Path = VOLUME_V2_LINEAGE_AUDIT_CSV,
    repository_root: Path = ROOT,
) -> list[str]:
    """Independently bind every promotion-capable event to the canonical audit.

    This validator deliberately does not call the ranking builder's lineage
    functions.  Event flags are treated as untrusted mirrors and are checked
    against the actual audit payload and immutable commit evidence.
    """

    errors: list[str] = []
    if events.empty:
        return errors
    missing_event_columns = sorted(EVENT_REQUIRED_COLUMNS - set(events.columns))
    if missing_event_columns:
        return [
            "events missing canonical audit-binding columns: "
            f"{missing_event_columns}"
        ]
    volume = events[events["model_id"].astype(str).isin(VOLUME_V2_MODEL_IDS)].copy()
    if volume.empty:
        return ["events contain no volume-v2 rows for canonical audit binding"]
    if not audit_path.is_file():
        return [f"missing canonical volume-v2 lineage audit: {audit_path.as_posix()}"]
    try:
        audit = pd.read_csv(audit_path, dtype=str, keep_default_na=False)
    except Exception as exc:
        return [f"failed to read canonical volume-v2 lineage audit: {exc}"]
    missing = sorted(AUDIT_REQUIRED_COLUMNS - set(audit.columns))
    if missing:
        return [f"canonical volume-v2 lineage audit missing columns: {missing}"]
    if audit.empty:
        return ["canonical volume-v2 lineage audit is empty"]
    if set(audit["audit_version"].astype(str)) != {VOLUME_V2_LINEAGE_AUDIT_VERSION}:
        errors.append(
            "canonical volume-v2 lineage audit version mismatch: "
            f"expected={VOLUME_V2_LINEAGE_AUDIT_VERSION}"
        )
    formal_audit = audit[audit["audit_row_type"].astype(str).eq("formal_row")].copy()
    formal_audit["_signal_date"] = formal_audit["signal_date"].map(_normalize_date)
    formal_audit["_stock_id"] = formal_audit["stock_id"].map(_normalize_stock_id)
    actual_audit_sha = _sha256_file(audit_path)
    git_blob_cache: dict[tuple[str, str], bytes | None] = {}
    git_commit_cache: dict[str, bool] = {}

    for index, event in volume.iterrows():
        event_label = (
            f"event_index={index} signal_date={safe_str(event.get('lineage_signal_date'))} "
            f"model_id={safe_str(event.get('model_id'))} "
            f"stock_id={safe_str(event.get('stock_id'))}"
        )
        event_source_identity = safe_str(event.get("lineage_audit_source"))
        if event_source_identity != VOLUME_V2_LINEAGE_AUDIT_SOURCE_IDENTITY:
            errors.append(f"{event_label}: lineage_audit_source is not the canonical audit")
        if safe_str(event.get("lineage_audit_source_sha256")) != actual_audit_sha:
            errors.append(f"{event_label}: lineage audit SHA does not match the actual audit")

        candidates = formal_audit[
            formal_audit["_signal_date"].eq(
                _normalize_date(event.get("lineage_signal_date", ""))
            )
            & formal_audit["model_id"].astype(str).eq(safe_str(event.get("model_id")))
            & formal_audit["_stock_id"].eq(_normalize_stock_id(event.get("stock_id", "")))
        ]
        exact = candidates[
            candidates["formal_row_sha256"].astype(str).eq(
                safe_str(event.get("lineage_formal_row_sha256"))
            )
            & candidates["formal_snapshot_sha256"].astype(str).eq(
                safe_str(event.get("lineage_formal_snapshot_sha256"))
            )
            & candidates["snapshot_revision"].astype(str).eq(
                safe_str(event.get("lineage_formal_snapshot_revision"))
            )
        ]
        gate_status = safe_str(event.get("lineage_gate_status"))
        promotion_claimed = any(
            safe_str(event.get(field)) == "True"
            for field in (
                "summary_evidence_eligible",
                "lineage_gate_pass_for_promotion_evidence",
                "lineage_historical_promotion_evidence_eligible",
                "ranking_evaluation_eligible",
                "trade_eligible",
            )
        )
        if len(exact) != 1:
            if gate_status == "non_clean_excluded":
                errors.append(
                    f"{event_label}: non-clean event does not join exactly one "
                    "canonical audit row"
                )
            elif gate_status == "verified_clean" or promotion_claimed:
                errors.append(
                    f"{event_label}: promotion-capable event does not join exactly one "
                    "canonical audit row"
                )
            if gate_status == "uncovered_fail_closed" and not candidates.empty:
                errors.append(
                    f"{event_label}: event claims uncovered despite canonical audit rows"
                )
            continue

        evidence = exact.iloc[0]
        mirrored_fields = {
            "lineage_audit_version": "audit_version",
            "lineage_audit_row_type": "audit_row_type",
            "lineage_formal_snapshot_revision": "snapshot_revision",
            "lineage_snapshot_commit_sha": "snapshot_commit_sha",
            "lineage_paired_source_commit_sha": "paired_source_commit_sha",
            "lineage_formal_row_sha256": "formal_row_sha256",
            "lineage_formal_snapshot_sha256": "formal_snapshot_sha256",
            "lineage_paired_source_resolution": "paired_source_resolution",
            "lineage_production_code_sha256": "production_code_sha256",
            "lineage_watch_artifact_sha256": "watch_artifact_sha256",
            "lineage_candidate_artifact_sha256": "candidate_artifact_sha256",
            "lineage_official_warrant_artifact_sha256": "official_warrant_artifact_sha256",
            "lineage_formal_row_disposition": "formal_row_disposition",
            "lineage_evidence_status": "evidence_status",
            "lineage_legacy_precontract_revision_history_status": (
                "legacy_precontract_revision_history_status"
            ),
            "lineage_historical_promotion_evidence_eligible": (
                "historical_promotion_evidence_eligible"
            ),
        }
        for event_field, audit_field in mirrored_fields.items():
            if safe_str(event.get(event_field)) != safe_str(evidence.get(audit_field)):
                errors.append(
                    f"{event_label}: {event_field} does not match canonical audit {audit_field}"
                )

        source_hashes_complete = all(
            _is_sha256(evidence.get(field))
            for field in (
                "production_code_sha256",
                "watch_artifact_sha256",
                "candidate_artifact_sha256",
                "official_warrant_artifact_sha256",
                "formal_row_sha256",
                "formal_snapshot_sha256",
            )
        )
        operational_clean = (
            safe_str(evidence.get("audit_version")) == VOLUME_V2_LINEAGE_AUDIT_VERSION
            and safe_str(evidence.get("audit_row_type")) == "formal_row"
            and safe_str(evidence.get("formal_row_disposition")) == "verified_clean"
            and safe_str(evidence.get("evidence_status")) == "complete"
            and safe_str(evidence.get("paired_source_resolution"))
            in VOLUME_V2_EXACT_PAIRED_SOURCE_RESOLUTIONS
            and source_hashes_complete
        )
        snapshot_commit_sha = safe_str(evidence.get("snapshot_commit_sha"))
        paired_commit_sha = safe_str(evidence.get("paired_source_commit_sha"))
        formal_snapshot_path = _repo_relative_audit_path(
            evidence.get("formal_snapshot_path"),
            "output/history/daily_model_snapshots",
        )
        watch_path = _repo_relative_audit_path(
            evidence.get("watch_artifact_path"), "output/latest"
        )
        candidate_path = _repo_relative_audit_path(
            evidence.get("candidate_artifact_path"), "output/latest"
        )
        official_path = _repo_relative_audit_path(
            evidence.get("official_warrant_artifact_path"), "output/latest"
        )
        expected_exact_paths = {
            "watch": "output/latest/volume_breakout_watch_latest.csv",
            "candidate": "output/latest/all_candidates_latest.csv",
            "official": "output/latest/warrant_flow_latest.csv",
        }
        paths_exact = (
            bool(formal_snapshot_path)
            and watch_path == expected_exact_paths["watch"]
            and candidate_path == expected_exact_paths["candidate"]
            and official_path == expected_exact_paths["official"]
        )
        snapshot_blob = _git_blob_at_commit(
            repository_root,
            snapshot_commit_sha,
            formal_snapshot_path,
            git_blob_cache,
        )
        snapshot_blob_matches = (
            snapshot_blob is not None
            and hashlib.sha256(_canonical_text_bytes(snapshot_blob)).hexdigest()
            == safe_str(evidence.get("formal_snapshot_sha256"))
        )
        paired_sources = (
            (
                "output/latest/daily_candidate_model_signals_for_report_latest.csv",
                safe_str(evidence.get("formal_snapshot_sha256")),
            ),
            (
                "scripts/build_daily_candidate_model_layer.py",
                safe_str(evidence.get("production_code_sha256")),
            ),
            (watch_path, safe_str(evidence.get("watch_artifact_sha256"))),
            (candidate_path, safe_str(evidence.get("candidate_artifact_sha256"))),
            (
                official_path,
                safe_str(evidence.get("official_warrant_artifact_sha256")),
            ),
        )
        paired_blobs_match = paths_exact
        for repo_path, expected_sha in paired_sources:
            blob = _git_blob_at_commit(
                repository_root, paired_commit_sha, repo_path, git_blob_cache
            )
            if (
                blob is None
                or hashlib.sha256(_canonical_text_bytes(blob)).hexdigest()
                != expected_sha
            ):
                paired_blobs_match = False
        immutable_commits = (
            _git_commit_exists(
                repository_root, snapshot_commit_sha, git_commit_cache
            )
            and _git_commit_exists(
                repository_root, paired_commit_sha, git_commit_cache
            )
            and snapshot_blob_matches
            and paired_blobs_match
        )
        if (
            safe_str(evidence.get("historical_promotion_evidence_eligible"))
            == "True"
            and not immutable_commits
        ):
            errors.append(
                f"{event_label}: audit promotion claim lacks immutable Git blob proof"
            )
        promotion_eligible = (
            operational_clean
            and safe_str(evidence.get("legacy_precontract_revision_history_status"))
            == "complete"
            and safe_str(evidence.get("historical_promotion_evidence_eligible"))
            == "True"
            and immutable_commits
        )
        expected_gate = "verified_clean" if operational_clean else "non_clean_excluded"
        if gate_status != expected_gate:
            errors.append(
                f"{event_label}: lineage_gate_status does not match independent audit result"
            )
        expected_promotion = "True" if promotion_eligible else "False"
        for field in (
            "summary_evidence_eligible",
            "lineage_gate_pass_for_promotion_evidence",
        ):
            if safe_str(event.get(field)) != expected_promotion:
                errors.append(
                    f"{event_label}: {field} does not match independent audit result"
                )
        if safe_str(event.get("source_artifact")) == "model_signals_for_report":
            if safe_str(event.get("ranking_evaluation_eligible")) != expected_promotion:
                errors.append(
                    f"{event_label}: ranking_evaluation_eligible does not match audit"
                )
        elif safe_str(event.get("ranking_evaluation_eligible")) != "False":
            errors.append(f"{event_label}: operation rows cannot be ranking eligible")
        expected_trade_eligible = (
            safe_str(event.get("source_artifact"))
            == "volume_breakout_operation_section"
            and safe_str(event.get("operation_section")) == "confirmed_operation"
            and safe_str(event.get("row_action_status"))
            == "confirmed_buy_candidate"
            and safe_str(event.get("buy_rank_eligible")) == "True"
            and promotion_eligible
        )
        expected_trade_text = "True" if expected_trade_eligible else "False"
        if safe_str(event.get("trade_eligible")) != expected_trade_text:
            errors.append(
                f"{event_label}: trade_eligible does not match independent "
                "operation and audit replay"
            )
    return errors


def validate_manifest_source_contract() -> list[str]:
    errors: list[str] = []
    if not MANIFEST_CSV.exists():
        return [f"missing manifest: {MANIFEST_CSV.as_posix()}"]
    try:
        selected_by_artifact = {
            artifact_id: select_latest_snapshot_revisions(
                SNAPSHOT_DIR,
                artifact_id,
                manifest_path=MANIFEST_CSV,
                repository_root=SNAPSHOT_DIR.parents[2],
            )
            for artifact_id in REQUIRED_ARTIFACT_IDS
        }
    except Exception as exc:
        return [str(exc)]
    if any(not revisions for revisions in selected_by_artifact.values()):
        return ["manifest contains no required ranking snapshot artifacts"]
    date_sets = {
        artifact_id: {revision.report_date for revision in revisions}
        for artifact_id, revisions in selected_by_artifact.items()
    }
    all_dates = set().union(*date_sets.values())
    for report_date in sorted(all_dates):
        missing_ids = sorted(
            artifact_id
            for artifact_id, dates in date_sets.items()
            if report_date not in dates
        )
        if missing_ids:
            errors.append(
                f"report_date={report_date} missing required snapshot artifacts: {missing_ids}"
            )

    manifest = normalize_revision_manifest_schema(
        pd.read_csv(MANIFEST_CSV, dtype=str, keep_default_na=False),
        source=MANIFEST_CSV.as_posix(),
    )
    manifest["snapshot_revision"] = manifest["snapshot_revision"].map(
        safe_str
    )
    expected_sources = {
        "model_signals_for_report": (
            "daily_candidate_model_signals_for_report_latest.csv"
        ),
        "volume_breakout_operation_section": (
            "daily_volume_breakout_operation_section_latest.csv"
        ),
    }
    for artifact_id, revisions in selected_by_artifact.items():
        for revision in revisions:
            current = manifest[
                manifest["artifact_id"].astype(str).eq(artifact_id)
                & manifest["snapshot_report_date"].map(_normalize_date).eq(
                    revision.report_date
                )
                & manifest["snapshot_revision"].astype(str).eq(revision.revision)
            ]
            if len(current) != 1:
                errors.append(
                    "manifest latest revision cannot be resolved exactly: "
                    f"report_date={revision.report_date} artifact_id={artifact_id}"
                )
                continue
            row = current.iloc[0]
            source_path = safe_str(row.get("source_path", ""))
            snapshot_path = safe_str(row.get("snapshot_path", ""))
            snapshot_name = Path(snapshot_path).name
            if Path(source_path).name != expected_sources[artifact_id]:
                errors.append(
                    f"unexpected source_path for ranking backtest snapshot: {source_path}"
                )
            if snapshot_name in FORBIDDEN_SOURCE_NAMES:
                errors.append(
                    "snapshot path must be date-stamped, not latest/PDF/research "
                    f"source: {snapshot_path}"
                )
            if "output/latest/" in snapshot_path.replace("\\", "/"):
                errors.append(
                    f"snapshot path must not point to output/latest: {snapshot_path}"
                )
    return errors


def main() -> int:
    events = read_csv(EVENTS_CSV, dtype=str).fillna("")
    summary = read_csv(OUT_CSV, dtype=str).fillna("")
    errors = (
        compare_docs_copy()
        + validate_summary()
        + validate_events(events)
        + validate_events_against_published_snapshots(events)
        + validate_volume_v2_formal_revision_binding(events)
        + validate_volume_v2_lineage(events)
        + validate_volume_v2_audit_binding(events)
        + validate_summary_against_events(summary, events)
        + validate_manifest_source_contract()
    )
    if errors:
        print("ERROR: daily published snapshot ranking backtest validation failed")
        for error in errors:
            print(f"ERROR: {error}")
        return 1
    print("daily published snapshot ranking backtest validation passed")
    print(f"summary_rows={len(summary)}")
    print(f"event_rows={len(events)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
