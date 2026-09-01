from __future__ import annotations

import argparse
import hashlib
import json
import math
import re
import sys
from pathlib import Path
from typing import Any

import pandas as pd


SCRIPT_DIR = Path(__file__).resolve().parent
if str(SCRIPT_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPT_DIR))

from daily_snapshot_revision_utils import (  # noqa: E402
    normalize_revision_manifest_schema,
    select_latest_snapshot_revisions,
    snapshot_file_sha256_candidates,
)
from tracking_utils import normalize_code, normalize_date, safe_str  # noqa: E402


ROOT = SCRIPT_DIR.parent
MODEL_ID = "pullback_short_reclaim"
ARTIFACT_ID = "model_signals_for_report"
ARTIFACT_VERSION = "pullback_short_reclaim_published_signal_replay_v1"
SNAPSHOT_REVISION_POLICY = "latest_revision_per_report_date_artifact"
HORIZONS = (5, 10, 20)
ANOMALY_CANDIDATE_ABS_RETURN_PCT = 80.0
OPERATION_CONTRACT_STATUS = "decision_required"
EVENTS_FILENAME = "pullback_short_reclaim_published_signal_replay_events_latest.csv"
SUMMARY_FILENAME = "pullback_short_reclaim_published_signal_replay_summary_latest.csv"
ANOMALIES_FILENAME = (
    "pullback_short_reclaim_published_signal_replay_anomaly_candidates_latest.csv"
)
REQUIRED_ROOT_CHECKS = (
    "identity_dedup_non_overlap",
    "formal_operation_replay",
    "point_in_time_and_trading_calendar",
    "raw_source_lineage_and_hash",
    "units_formula_and_adjustment_basis",
    "authoritative_business_event_history",
    "independent_source_corroboration",
    "reproducible_evidence_reference",
)
SIGNAL_SEMANTIC_COLUMNS = (
    "signal_date",
    "stock_id",
    "model_id",
    "entry_basis",
    "model_score",
    "main_condition_met",
    "score_components",
    "risk_penalty_tags",
    "next_confirmation",
    "model_main_conditions",
    "model_add_score_items",
    "model_forbidden_veto",
    "model_operation_guidance",
    "selection_semantics",
)
EVENT_REQUIRED_COLUMNS = {
    "artifact_version",
    "model_id",
    "source_artifact_id",
    "snapshot_revision_policy",
    "snapshot_report_date",
    "snapshot_revision",
    "snapshot_path",
    "snapshot_sha256",
    "snapshot_manifest_sha256",
    "snapshot_pipeline_commit_sha",
    "snapshot_total_row_count",
    "snapshot_total_column_count",
    "snapshot_target_model_row_count",
    "snapshot_csv_row_number",
    "target_model_row_ordinal",
    "published_source_row_index",
    "source_row_sha256",
    "signal_semantic_sha256",
    "signal_event_id",
    "signal_date",
    "stock_id",
    "source_duplicate_ordinal",
    "source_duplicate_count",
    "identity_disposition",
    "primary_metric_included",
    "entry_rule",
    "entry_date",
    "entry_open_price",
    "entry_price_row_sha256",
    "price_source_path",
    "price_source_sha256",
    "price_source_sha256_basis",
    "price_source_immutability_status",
    "trading_calendar_status",
    "realized_price_basis",
    "statistical_trigger_status",
    "anomaly_candidate_horizons",
    "anomaly_disposition",
    "anomaly_primary_metric_policy",
    "formal_use_allowed",
    "trade_eligible",
    "promotion_evidence_allowed",
    "operation_contract_status",
    "operation_use_status",
    "producer_source_sha256",
    "generated_at",
}
for _horizon in HORIZONS:
    EVENT_REQUIRED_COLUMNS.update(
        {
            f"d{_horizon}_maturity_status",
            f"d{_horizon}_exit_date",
            f"d{_horizon}_exit_close_price",
            f"d{_horizon}_exit_price_row_sha256",
            f"d{_horizon}_return_pct",
            f"d{_horizon}_outcome",
            f"d{_horizon}_anomaly_candidate",
        }
    )
SUMMARY_REQUIRED_COLUMNS = {
    "artifact_version",
    "model_id",
    "horizon",
    "holding_trading_rows",
    "published_source_row_count",
    "unique_signal_event_count",
    "duplicate_presentation_row_count",
    "snapshot_report_count",
    "source_snapshot_set_sha256",
    "source_price_set_sha256",
    "signal_event_count",
    "mature_count",
    "not_mature_count",
    "right_censored_count",
    "invalid_price_count",
    "win_count",
    "neutral_count",
    "failure_count",
    "win_rate_pct",
    "neutral_rate_pct",
    "failure_rate_pct",
    "average_return_pct",
    "median_return_pct",
    "unresolved_anomaly_candidate_count",
    "sensitivity_sample_count",
    "sensitivity_excluded_anomaly_candidate_count",
    "sensitivity_win_count",
    "sensitivity_neutral_count",
    "sensitivity_failure_count",
    "sensitivity_win_rate_pct",
    "sensitivity_average_return_pct",
    "sensitivity_median_return_pct",
    "sensitivity_analysis_basis",
    "sensitivity_is_corrected_primary",
    "right_censoring_policy",
    "price_source_formal_lineage_status",
    "promotion_blockers",
    "primary_metric_basis",
    "primary_retains_unresolved_anomaly_candidates",
    "excluded_anomaly_candidate_count",
    "formal_use_allowed",
    "trade_eligible",
    "promotion_evidence_allowed",
    "operation_contract_status",
    "interpretation_status",
    "snapshot_revision_policy",
    "entry_rule",
    "exit_rule",
    "stop_rule",
    "generated_at",
}
ANOMALY_REQUIRED_COLUMNS = {
    "artifact_version",
    "anomaly_candidate_id",
    "signal_event_id",
    "model_id",
    "signal_date",
    "stock_id",
    "horizon",
    "realized_return_pct",
    "statistical_trigger_method",
    "statistical_trigger_threshold_pct",
    "statistical_trigger_status",
    "final_disposition",
    "primary_metric_policy",
    "promotion_policy",
    "required_root_checks",
    "completed_root_checks",
    "missing_root_checks",
    "snapshot_sha256",
    "source_row_sha256",
    "price_source_sha256",
    "price_source_immutability_status",
    "retained_in_primary_metrics",
    "formal_use_allowed",
    "promotion_evidence_allowed",
    "operation_contract_status",
    "generated_at",
}


def _canonical_file_sha256(path: Path) -> str:
    payload = path.read_bytes().replace(b"\r\n", b"\n").replace(b"\r", b"\n")
    return hashlib.sha256(payload).hexdigest()


def _raw_file_sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def _canonical_row_sha256(row: pd.Series | dict[str, Any]) -> str:
    values = row.to_dict() if isinstance(row, pd.Series) else dict(row)
    normalized = {str(key): safe_str(values[key]) for key in sorted(values)}
    payload = json.dumps(
        normalized,
        ensure_ascii=False,
        sort_keys=True,
        separators=(",", ":"),
    ).encode("utf-8")
    return hashlib.sha256(payload).hexdigest()


def _aggregate_sha256(values: list[str]) -> str:
    return hashlib.sha256("\n".join(sorted(set(values))).encode("utf-8")).hexdigest()


def _outcome(value: float) -> str:
    return "win" if value > 0 else "failure" if value < 0 else "neutral"


def _float(value: Any) -> float | None:
    text = safe_str(value)
    if not text:
        return None
    try:
        number = float(text)
    except ValueError:
        return None
    return number if math.isfinite(number) else None


def _int(value: Any) -> int | None:
    number = _float(value)
    if number is None or not number.is_integer():
        return None
    return int(number)


def _same_number(left: Any, right: Any, tolerance: float = 1e-6) -> bool:
    left_number = _float(left)
    right_number = _float(right)
    if left_number is None or right_number is None:
        return left_number is None and right_number is None
    return math.isclose(left_number, right_number, abs_tol=tolerance, rel_tol=0.0)


def _price_path_text(path: Path) -> str:
    try:
        return path.resolve().relative_to(ROOT.resolve()).as_posix()
    except ValueError:
        return path.resolve().as_posix()


def _load_price(stock_id: str, price_dir: Path) -> tuple[pd.DataFrame, str, str]:
    path = price_dir / f"{stock_id}.csv"
    if not path.is_file():
        return pd.DataFrame(), _price_path_text(path), ""
    raw = pd.read_csv(path, dtype=str, keep_default_na=False)
    missing = sorted({"date", "open", "close"} - set(raw.columns))
    if missing:
        raise RuntimeError(f"price history missing columns: stock_id={stock_id} {missing}")
    frame = raw.copy()
    frame["_date"] = frame["date"].map(normalize_date)
    if frame["_date"].eq("").any() or frame["_date"].duplicated().any():
        raise RuntimeError(f"price history date contract failed: stock_id={stock_id}")
    frame["_open"] = pd.to_numeric(frame["open"], errors="coerce")
    frame["_close"] = pd.to_numeric(frame["close"], errors="coerce")
    return (
        frame.sort_values("_date").reset_index(drop=True),
        _price_path_text(path),
        _raw_file_sha256(path),
    )


def _price_row_sha256(row: pd.Series) -> str:
    return _canonical_row_sha256(
        {column: row[column] for column in row.index if not str(column).startswith("_")}
    )


def _expected_forward(price: pd.DataFrame, signal_date: str) -> dict[str, Any]:
    expected: dict[str, Any] = {"entry_date": "", "entry_open_price": "", "entry_price_row_sha256": ""}
    if price.empty:
        for horizon in HORIZONS:
            expected.update(
                {
                    f"d{horizon}_maturity_status": "missing_price_history",
                    f"d{horizon}_exit_date": "",
                    f"d{horizon}_exit_close_price": "",
                    f"d{horizon}_exit_price_row_sha256": "",
                    f"d{horizon}_return_pct": "",
                    f"d{horizon}_outcome": "",
                    f"d{horizon}_anomaly_candidate": "False",
                }
            )
        return expected
    future = price[price["_date"].astype(str).gt(signal_date)].reset_index(drop=True)
    if future.empty:
        for horizon in HORIZONS:
            expected.update(
                {
                    f"d{horizon}_maturity_status": "no_forward_price",
                    f"d{horizon}_exit_date": "",
                    f"d{horizon}_exit_close_price": "",
                    f"d{horizon}_exit_price_row_sha256": "",
                    f"d{horizon}_return_pct": "",
                    f"d{horizon}_outcome": "",
                    f"d{horizon}_anomaly_candidate": "False",
                }
            )
        return expected
    entry = future.iloc[0]
    entry_price = float(entry["_open"]) if pd.notna(entry["_open"]) else math.nan
    expected.update(
        {
            "entry_date": safe_str(entry["_date"]),
            "entry_open_price": round(entry_price, 6) if math.isfinite(entry_price) else "",
            "entry_price_row_sha256": _price_row_sha256(entry),
        }
    )
    for horizon in HORIZONS:
        values: dict[str, Any] = {
            f"d{horizon}_maturity_status": "not_mature",
            f"d{horizon}_exit_date": "",
            f"d{horizon}_exit_close_price": "",
            f"d{horizon}_exit_price_row_sha256": "",
            f"d{horizon}_return_pct": "",
            f"d{horizon}_outcome": "",
            f"d{horizon}_anomaly_candidate": "False",
        }
        if len(future) >= horizon:
            exit_row = future.iloc[horizon - 1]
            close_price = float(exit_row["_close"]) if pd.notna(exit_row["_close"]) else math.nan
            values[f"d{horizon}_exit_date"] = safe_str(exit_row["_date"])
            values[f"d{horizon}_exit_price_row_sha256"] = _price_row_sha256(exit_row)
            if not math.isfinite(entry_price) or entry_price <= 0:
                values[f"d{horizon}_maturity_status"] = "invalid_entry_price"
            elif not math.isfinite(close_price) or close_price <= 0:
                values[f"d{horizon}_maturity_status"] = "invalid_exit_price"
            else:
                realized = (close_price / entry_price - 1.0) * 100.0
                values.update(
                    {
                        f"d{horizon}_maturity_status": "mature",
                        f"d{horizon}_exit_close_price": round(close_price, 6),
                        f"d{horizon}_return_pct": round(realized, 6),
                        f"d{horizon}_outcome": _outcome(realized),
                        f"d{horizon}_anomaly_candidate": (
                            "True"
                            if abs(realized) >= ANOMALY_CANDIDATE_ABS_RETURN_PCT
                            else "False"
                        ),
                    }
                )
        expected.update(values)
    return expected


def _manifest_index(manifest_path: Path) -> dict[tuple[str, str], dict[str, str]]:
    manifest = pd.read_csv(manifest_path, dtype=str, keep_default_na=False)
    manifest = normalize_revision_manifest_schema(manifest, source=manifest_path.as_posix())
    work = manifest[manifest["artifact_id"].astype(str).eq(ARTIFACT_ID)].copy()
    result: dict[tuple[str, str], dict[str, str]] = {}
    for _, row in work.iterrows():
        key = (
            normalize_date(row.get("snapshot_report_date", "")),
            safe_str(row.get("snapshot_revision", "")),
        )
        if key in result:
            raise RuntimeError(f"duplicate manifest key: {key}")
        result[key] = {str(column): safe_str(row.get(column, "")) for column in row.index}
    return result


def _semantic_sha(row: pd.Series) -> str:
    payload = {column: safe_str(row.get(column, "")) for column in SIGNAL_SEMANTIC_COLUMNS}
    payload["stock_id"] = normalize_code(payload["stock_id"])
    payload["signal_date"] = normalize_date(payload["signal_date"])
    return _canonical_row_sha256(payload)


def _expected_events(
    *,
    snapshot_dir: Path,
    manifest_path: Path,
    price_dir: Path,
    through_date: str,
) -> pd.DataFrame:
    revisions = select_latest_snapshot_revisions(
        snapshot_dir,
        ARTIFACT_ID,
        through_date=through_date,
        manifest_path=manifest_path,
        repository_root=snapshot_dir.parents[2] if len(snapshot_dir.parents) >= 3 else snapshot_dir.parent,
    )
    metadata_index = _manifest_index(manifest_path)
    manifest_sha = _canonical_file_sha256(manifest_path)
    producer_path = SCRIPT_DIR / "build_pullback_short_reclaim_research.py"
    producer_sha = _raw_file_sha256(producer_path)
    price_cache: dict[str, tuple[pd.DataFrame, str, str]] = {}
    rows: list[dict[str, Any]] = []
    for revision in revisions:
        metadata = metadata_index[(revision.report_date, revision.revision)]
        if safe_str(metadata.get("snapshot_path")) != revision.path_text:
            raise RuntimeError("validator selected snapshot path differs from manifest")
        if safe_str(metadata.get("snapshot_sha256")).lower() != revision.snapshot_sha256:
            raise RuntimeError("validator selected snapshot SHA differs from manifest")
        if re.fullmatch(
            r"[0-9a-f]{40}", safe_str(metadata.get("pipeline_commit_sha")).lower()
        ) is None:
            raise RuntimeError("validator manifest pipeline_commit_sha is invalid")
        if safe_str(metadata.get("source_path")) != (
            "output/latest/daily_candidate_model_signals_for_report_latest.csv"
        ):
            raise RuntimeError("validator manifest source_path is not the published model source")
        if safe_str(metadata.get("purpose")) != "as_published_daily_model_snapshot":
            raise RuntimeError("validator manifest purpose is not as-published")
        if revision.snapshot_sha256 not in snapshot_file_sha256_candidates(revision.path):
            raise RuntimeError("validator snapshot SHA mismatch")
        snapshot = pd.read_csv(revision.path, dtype=str, keep_default_na=False)
        expected_rows = _int(metadata.get("row_count"))
        expected_columns = _int(metadata.get("column_count"))
        if expected_rows != len(snapshot) or expected_columns != len(snapshot.columns):
            raise RuntimeError("validator snapshot row/column count mismatch")
        target = snapshot[snapshot["model_id"].astype(str).eq(MODEL_ID)].copy()
        for target_ordinal, (frame_index, source) in enumerate(target.iterrows(), start=1):
            signal_date = normalize_date(source.get("signal_date", ""))
            stock_id = normalize_code(source.get("stock_id", ""))
            if stock_id not in price_cache:
                price_cache[stock_id] = _load_price(stock_id, price_dir)
            price, price_path, price_sha = price_cache[stock_id]
            forward = _expected_forward(price, signal_date)
            event_id = hashlib.sha256(
                f"{MODEL_ID}|{signal_date}|{stock_id}".encode("utf-8")
            ).hexdigest()
            rows.append(
                {
                    "snapshot_report_date": revision.report_date,
                    "snapshot_revision": revision.revision,
                    "snapshot_path": revision.path_text,
                    "snapshot_sha256": revision.snapshot_sha256,
                    "snapshot_manifest_sha256": manifest_sha,
                    "snapshot_pipeline_commit_sha": metadata.get("pipeline_commit_sha", ""),
                    "snapshot_total_row_count": len(snapshot),
                    "snapshot_total_column_count": len(snapshot.columns),
                    "snapshot_target_model_row_count": len(target),
                    "snapshot_csv_row_number": int(frame_index) + 2,
                    "target_model_row_ordinal": target_ordinal,
                    "published_source_row_index": safe_str(
                        source.get("source_row_index", "")
                    ),
                    "source_row_sha256": _canonical_row_sha256(source),
                    "signal_semantic_sha256": _semantic_sha(source),
                    "signal_event_id": event_id,
                    "signal_date": signal_date,
                    "stock_id": stock_id,
                    "price_source_path": price_path,
                    "price_source_sha256": price_sha,
                    "producer_source_sha256": producer_sha,
                    **forward,
                }
            )
    expected = pd.DataFrame(rows)
    if expected.empty:
        return expected
    expected = expected.sort_values(
        ["signal_date", "stock_id", "snapshot_csv_row_number"]
    ).reset_index(drop=True)
    for _, group in expected.groupby("signal_event_id", sort=False):
        if group["signal_semantic_sha256"].nunique(dropna=False) != 1:
            first = group.iloc[0]
            raise RuntimeError(
                "validator duplicate source rows disagree on signal semantics: "
                f"signal_date={first['signal_date']} stock_id={first['stock_id']}"
            )
        ordered = list(group.sort_values("snapshot_csv_row_number").index)
        for ordinal, index in enumerate(ordered, start=1):
            expected.at[index, "source_duplicate_ordinal"] = ordinal
            expected.at[index, "source_duplicate_count"] = len(ordered)
            expected.at[index, "primary_metric_included"] = "True" if ordinal == 1 else "False"
            expected.at[index, "identity_disposition"] = (
                "canonical_signal_event" if ordinal == 1 else "duplicate_report_presentation_row"
            )
    return expected


def _compare_expected_events(events: pd.DataFrame, expected: pd.DataFrame) -> list[str]:
    errors: list[str] = []
    key_columns = ["snapshot_report_date", "snapshot_revision", "snapshot_csv_row_number"]
    actual_keys = {
        tuple(safe_str(row.get(column, "")) for column in key_columns): index
        for index, row in events.iterrows()
    }
    expected_keys = {
        tuple(safe_str(row.get(column, "")) for column in key_columns): index
        for index, row in expected.iterrows()
    }
    if len(actual_keys) != len(events):
        errors.append("events contain duplicate exact published source-row keys")
    if set(actual_keys) != set(expected_keys):
        errors.append("events do not exactly match latest-revision pullback source rows")
        return errors
    text_fields = {
        "snapshot_path",
        "snapshot_sha256",
        "snapshot_manifest_sha256",
        "snapshot_pipeline_commit_sha",
        "source_row_sha256",
        "signal_semantic_sha256",
        "signal_event_id",
        "signal_date",
        "stock_id",
        "price_source_path",
        "price_source_sha256",
        "producer_source_sha256",
        "entry_date",
        "entry_price_row_sha256",
        "identity_disposition",
        "primary_metric_included",
        "published_source_row_index",
    }
    numeric_fields = {
        "snapshot_total_row_count",
        "snapshot_total_column_count",
        "snapshot_target_model_row_count",
        "target_model_row_ordinal",
        "source_duplicate_ordinal",
        "source_duplicate_count",
        "entry_open_price",
    }
    for horizon in HORIZONS:
        text_fields.update(
            {
                f"d{horizon}_maturity_status",
                f"d{horizon}_exit_date",
                f"d{horizon}_exit_price_row_sha256",
                f"d{horizon}_outcome",
                f"d{horizon}_anomaly_candidate",
            }
        )
        numeric_fields.update(
            {f"d{horizon}_exit_close_price", f"d{horizon}_return_pct"}
        )
    for key, expected_index in expected_keys.items():
        actual = events.loc[actual_keys[key]]
        wanted = expected.loc[expected_index]
        label = f"source_row={key}"
        for field in sorted(text_fields):
            if safe_str(actual.get(field, "")) != safe_str(wanted.get(field, "")):
                errors.append(f"{label}: {field} mismatch")
        for field in sorted(numeric_fields):
            if not _same_number(actual.get(field, ""), wanted.get(field, "")):
                errors.append(f"{label}: {field} mismatch")
        expected_candidate_horizons = [
            f"D+{horizon}"
            for horizon in HORIZONS
            if safe_str(wanted.get(f"d{horizon}_anomaly_candidate")) == "True"
        ]
        expected_trigger = "anomaly_candidate" if expected_candidate_horizons else "not_triggered"
        expected_disposition = (
            "unresolved_anomaly_candidate" if expected_candidate_horizons else "not_applicable"
        )
        if safe_str(actual.get("statistical_trigger_status")) != expected_trigger:
            errors.append(f"{label}: statistical_trigger_status mismatch")
        if safe_str(actual.get("anomaly_candidate_horizons")) != ";".join(expected_candidate_horizons):
            errors.append(f"{label}: anomaly_candidate_horizons mismatch")
        if safe_str(actual.get("anomaly_disposition")) != expected_disposition:
            errors.append(f"{label}: anomaly_disposition mismatch")
    return errors


def _validate_summary(events: pd.DataFrame, summary: pd.DataFrame) -> list[str]:
    errors: list[str] = []
    expected_horizons = {f"D+{horizon}" for horizon in HORIZONS}
    if set(summary["horizon"].astype(str)) != expected_horizons or len(summary) != len(HORIZONS):
        return ["summary must contain exactly D+5, D+10, and D+20"]
    canonical = events[events["primary_metric_included"].astype(str).eq("True")].copy()
    snapshot_hash = _aggregate_sha256(canonical["snapshot_sha256"].astype(str).tolist())
    price_hash = _aggregate_sha256(
        [value for value in canonical["price_source_sha256"].astype(str) if value]
    )
    for horizon in HORIZONS:
        part = summary[summary["horizon"].astype(str).eq(f"D+{horizon}")]
        row = part.iloc[0]
        mature = canonical[
            canonical[f"d{horizon}_maturity_status"].astype(str).eq("mature")
        ]
        returns = pd.to_numeric(mature[f"d{horizon}_return_pct"], errors="coerce")
        expected_counts = {
            "holding_trading_rows": horizon,
            "published_source_row_count": len(events),
            "unique_signal_event_count": len(canonical),
            "duplicate_presentation_row_count": len(events) - len(canonical),
            "signal_event_count": len(canonical),
            "mature_count": len(mature),
            "not_mature_count": len(canonical) - len(mature),
            "right_censored_count": int(
                canonical[f"d{horizon}_maturity_status"]
                .astype(str)
                .isin({"not_mature", "no_forward_price", "missing_price_history"})
                .sum()
            ),
            "invalid_price_count": int(
                canonical[f"d{horizon}_maturity_status"]
                .astype(str)
                .str.startswith("invalid_")
                .sum()
            ),
            "win_count": int(mature[f"d{horizon}_outcome"].astype(str).eq("win").sum()),
            "neutral_count": int(mature[f"d{horizon}_outcome"].astype(str).eq("neutral").sum()),
            "failure_count": int(mature[f"d{horizon}_outcome"].astype(str).eq("failure").sum()),
            "unresolved_anomaly_candidate_count": int(
                mature[f"d{horizon}_anomaly_candidate"].astype(str).eq("True").sum()
            ),
            "excluded_anomaly_candidate_count": 0,
        }
        sensitivity = mature[
            ~mature[f"d{horizon}_anomaly_candidate"].astype(str).eq("True")
        ].copy()
        sensitivity_returns = pd.to_numeric(
            sensitivity[f"d{horizon}_return_pct"], errors="coerce"
        )
        expected_counts.update(
            {
                "sensitivity_sample_count": len(sensitivity),
                "sensitivity_excluded_anomaly_candidate_count": (
                    expected_counts["unresolved_anomaly_candidate_count"]
                ),
                "sensitivity_win_count": int(
                    sensitivity[f"d{horizon}_outcome"].astype(str).eq("win").sum()
                ),
                "sensitivity_neutral_count": int(
                    sensitivity[f"d{horizon}_outcome"]
                    .astype(str)
                    .eq("neutral")
                    .sum()
                ),
                "sensitivity_failure_count": int(
                    sensitivity[f"d{horizon}_outcome"]
                    .astype(str)
                    .eq("failure")
                    .sum()
                ),
            }
        )
        for field, expected_value in expected_counts.items():
            if _int(row.get(field)) != expected_value:
                errors.append(f"summary D+{horizon}: {field} mismatch")
        denominator = len(mature)
        expected_numbers: dict[str, float | None] = {
            "win_rate_pct": (
                expected_counts["win_count"] / denominator * 100.0 if denominator else None
            ),
            "neutral_rate_pct": (
                expected_counts["neutral_count"] / denominator * 100.0 if denominator else None
            ),
            "failure_rate_pct": (
                expected_counts["failure_count"] / denominator * 100.0 if denominator else None
            ),
            "average_return_pct": float(returns.mean()) if denominator else None,
            "median_return_pct": float(returns.median()) if denominator else None,
            "sensitivity_win_rate_pct": (
                expected_counts["sensitivity_win_count"]
                / len(sensitivity)
                * 100.0
                if len(sensitivity)
                else None
            ),
            "sensitivity_average_return_pct": (
                float(sensitivity_returns.mean()) if len(sensitivity) else None
            ),
            "sensitivity_median_return_pct": (
                float(sensitivity_returns.median()) if len(sensitivity) else None
            ),
        }
        for field, expected_value in expected_numbers.items():
            if not _same_number(row.get(field, ""), expected_value):
                errors.append(f"summary D+{horizon}: {field} mismatch")
        if safe_str(row.get("source_snapshot_set_sha256")) != snapshot_hash:
            errors.append(f"summary D+{horizon}: source_snapshot_set_sha256 mismatch")
        if safe_str(row.get("source_price_set_sha256")) != price_hash:
            errors.append(f"summary D+{horizon}: source_price_set_sha256 mismatch")
        expected_blockers = [
            "operation_contract_decision_required",
            "mutable_price_source_unpinned",
            "market_calendar_proof_missing",
        ]
        if expected_counts["unresolved_anomaly_candidate_count"]:
            expected_blockers.append("unresolved_anomaly_candidate")
        if safe_str(row.get("promotion_blockers")) != ";".join(expected_blockers):
            errors.append(f"summary D+{horizon}: promotion_blockers mismatch")
    return errors


def _validate_anomalies(events: pd.DataFrame, anomalies: pd.DataFrame) -> list[str]:
    errors: list[str] = []
    canonical = events[events["primary_metric_included"].astype(str).eq("True")]
    expected: dict[tuple[str, str], pd.Series] = {}
    for _, event in canonical.iterrows():
        for horizon in HORIZONS:
            if safe_str(event.get(f"d{horizon}_anomaly_candidate")) == "True":
                expected[(safe_str(event["signal_event_id"]), f"D+{horizon}")] = event
    actual: dict[tuple[str, str], pd.Series] = {}
    for _, row in anomalies.iterrows():
        key = (safe_str(row.get("signal_event_id")), safe_str(row.get("horizon")))
        if key in actual:
            errors.append(f"duplicate anomaly candidate row: {key}")
        actual[key] = row
    if set(actual) != set(expected):
        errors.append("anomaly artifact does not exactly match numerical trigger candidates")
        return errors
    required_checks = ";".join(REQUIRED_ROOT_CHECKS)
    for key, event in expected.items():
        row = actual[key]
        horizon = int(key[1].split("+")[1])
        candidate_id = hashlib.sha256(f"{key[0]}|d{horizon}".encode("utf-8")).hexdigest()
        exact = {
            "anomaly_candidate_id": candidate_id,
            "model_id": MODEL_ID,
            "signal_date": safe_str(event["signal_date"]),
            "stock_id": safe_str(event["stock_id"]),
            "statistical_trigger_method": "abs_realized_return_ge_threshold",
            "statistical_trigger_status": "anomaly_candidate",
            "final_disposition": "unresolved_anomaly_candidate",
            "primary_metric_policy": "retain_in_primary_metrics_and_allow_exclusion_sensitivity_only",
            "promotion_policy": "blocked_pending_root_cause",
            "required_root_checks": required_checks,
            "completed_root_checks": "",
            "missing_root_checks": required_checks,
            "snapshot_sha256": safe_str(event["snapshot_sha256"]),
            "source_row_sha256": safe_str(event["source_row_sha256"]),
            "price_source_sha256": safe_str(event["price_source_sha256"]),
            "price_source_immutability_status": "mutable_current_file_unpinned",
            "retained_in_primary_metrics": "True",
            "formal_use_allowed": "False",
            "promotion_evidence_allowed": "False",
            "operation_contract_status": OPERATION_CONTRACT_STATUS,
        }
        for field, expected_value in exact.items():
            if safe_str(row.get(field, "")) != expected_value:
                errors.append(f"anomaly {key}: {field} mismatch")
        if not _same_number(
            row.get("realized_return_pct"), event.get(f"d{horizon}_return_pct")
        ):
            errors.append(f"anomaly {key}: realized_return_pct mismatch")
        if not _same_number(
            row.get("statistical_trigger_threshold_pct"),
            ANOMALY_CANDIDATE_ABS_RETURN_PCT,
        ):
            errors.append(f"anomaly {key}: threshold mismatch")
    return errors


def validate_replay_bundle(
    events: pd.DataFrame,
    summary: pd.DataFrame,
    anomalies: pd.DataFrame,
    *,
    snapshot_dir: Path,
    manifest_path: Path,
    price_dir: Path,
    through_date: str = "",
) -> list[str]:
    errors: list[str] = []
    missing_events = sorted(EVENT_REQUIRED_COLUMNS - set(events.columns))
    missing_summary = sorted(SUMMARY_REQUIRED_COLUMNS - set(summary.columns))
    missing_anomalies = sorted(ANOMALY_REQUIRED_COLUMNS - set(anomalies.columns))
    if missing_events:
        errors.append(f"events missing columns: {missing_events}")
    if missing_summary:
        errors.append(f"summary missing columns: {missing_summary}")
    if missing_anomalies:
        errors.append(f"anomalies missing columns: {missing_anomalies}")
    if errors:
        return errors
    if events.empty:
        return ["events are empty"]
    for name, frame in (("events", events), ("summary", summary), ("anomalies", anomalies)):
        if not frame.empty and set(frame["artifact_version"].astype(str)) != {ARTIFACT_VERSION}:
            errors.append(f"{name} artifact_version mismatch")
        if not frame.empty and set(frame["model_id"].astype(str)) != {MODEL_ID}:
            errors.append(f"{name} contains another model")
        if not frame.empty and set(frame["formal_use_allowed"].astype(str)) != {"False"}:
            errors.append(f"{name} formal_use_allowed must remain False")
        if not frame.empty and set(frame["promotion_evidence_allowed"].astype(str)) != {"False"}:
            errors.append(f"{name} promotion_evidence_allowed must remain False")
        if not frame.empty and set(frame["operation_contract_status"].astype(str)) != {OPERATION_CONTRACT_STATUS}:
            errors.append(f"{name} operation_contract_status must be decision_required")
    if set(events["trade_eligible"].astype(str)) != {"False"}:
        errors.append("events trade_eligible must remain False")
    if set(summary["trade_eligible"].astype(str)) != {"False"}:
        errors.append("summary trade_eligible must remain False")
    if set(events["snapshot_revision_policy"].astype(str)) != {SNAPSHOT_REVISION_POLICY}:
        errors.append("events snapshot revision policy mismatch")
    if set(events["source_artifact_id"].astype(str)) != {ARTIFACT_ID}:
        errors.append("events source artifact must remain model_signals_for_report")
    if set(events["entry_rule"].astype(str)) != {
        "signal_date_next_trading_day_open"
    }:
        errors.append("events entry rule mismatch")
    if set(events["price_source_sha256_basis"].astype(str)) != {"raw_file_bytes"}:
        errors.append("events price SHA basis mismatch")
    if set(events["price_source_immutability_status"].astype(str)) != {"mutable_current_file_unpinned"}:
        errors.append("events must disclose mutable/unpinned price inputs")
    if set(events["realized_price_basis"].astype(str)) != {
        "next_open_to_fixed_future_close_no_intraday_high_low"
    }:
        errors.append("events realized price basis mismatch")
    if set(events["trading_calendar_status"].astype(str)) != {
        "stock_price_row_sequence_only_no_market_calendar_proof"
    }:
        errors.append("events must disclose missing market-calendar proof")
    if set(events["anomaly_primary_metric_policy"].astype(str)) != {
        "retained_in_primary_metrics"
    }:
        errors.append("events anomaly candidates must remain in primary metrics")
    if set(events["operation_use_status"].astype(str)) != {
        "research_outcome_replay_only_no_operation_contract"
    }:
        errors.append("events operation use status mismatch")
    try:
        expected = _expected_events(
            snapshot_dir=Path(snapshot_dir),
            manifest_path=Path(manifest_path),
            price_dir=Path(price_dir),
            through_date=through_date,
        )
    except Exception as exc:
        errors.append(f"independent source replay failed: {exc}")
        return errors
    errors.extend(_compare_expected_events(events, expected))
    errors.extend(_validate_summary(events, summary))
    errors.extend(_validate_anomalies(events, anomalies))
    if set(summary["primary_retains_unresolved_anomaly_candidates"].astype(str)) != {"True"}:
        errors.append("summary must retain unresolved anomaly candidates")
    if set(summary["primary_metric_basis"].astype(str)) != {
        "unique_signal_event_including_unresolved_anomaly_candidates"
    }:
        errors.append("summary primary metric basis mismatch")
    if set(summary["interpretation_status"].astype(str)) != {
        "research_only_operation_decision_required"
    }:
        errors.append("summary interpretation_status mismatch")
    if set(summary["right_censoring_policy"].astype(str)) != {
        "per_horizon_incomplete_forward_price_excluded_from_horizon_metrics"
    }:
        errors.append("summary right-censoring policy mismatch")
    if set(summary["sensitivity_analysis_basis"].astype(str)) != {
        "excluding_unresolved_anomaly_candidates_sensitivity_only"
    }:
        errors.append("summary anomaly sensitivity basis mismatch")
    if set(summary["sensitivity_is_corrected_primary"].astype(str)) != {"False"}:
        errors.append("summary sensitivity must not be labeled corrected primary")
    if set(summary["price_source_formal_lineage_status"].astype(str)) != {
        "mutable_current_files_unpinned_block_formal_use"
    }:
        errors.append("summary must preserve mutable price-source blocker")
    if set(summary["snapshot_revision_policy"].astype(str)) != {
        SNAPSHOT_REVISION_POLICY
    }:
        errors.append("summary snapshot revision policy mismatch")
    if set(summary["entry_rule"].astype(str)) != {
        "signal_date_next_trading_day_open"
    }:
        errors.append("summary entry rule mismatch")
    if set(summary["exit_rule"].astype(str)) != {
        "fixed_future_close_research_comparison"
    }:
        errors.append("summary exit rule mismatch")
    if set(summary["stop_rule"].astype(str)) != {
        "undefined_decision_required"
    }:
        errors.append("summary stop rule must remain undefined/decision_required")
    return errors


def _read_csv(path: Path) -> pd.DataFrame:
    try:
        return pd.read_csv(path, dtype=str, keep_default_na=False)
    except Exception as exc:
        raise RuntimeError(f"failed to read replay artifact: {path}") from exc


def validate_files(
    *,
    events_path: Path,
    summary_path: Path,
    anomalies_path: Path,
    snapshot_dir: Path,
    manifest_path: Path,
    price_dir: Path,
    through_date: str = "",
) -> list[str]:
    return validate_replay_bundle(
        _read_csv(events_path),
        _read_csv(summary_path),
        _read_csv(anomalies_path),
        snapshot_dir=snapshot_dir,
        manifest_path=manifest_path,
        price_dir=price_dir,
        through_date=through_date,
    )


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Independently validate pullback_short_reclaim published-signal replay."
    )
    parser.add_argument(
        "--snapshot-dir",
        type=Path,
        default=ROOT / "output/history/daily_model_snapshots",
    )
    parser.add_argument("--manifest", type=Path, default=None)
    parser.add_argument(
        "--price-dir", type=Path, default=ROOT / "data/stock_price_history"
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=ROOT / "output/latest/research_backtest",
    )
    parser.add_argument("--through-date", default="")
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    manifest_path = args.manifest or (
        args.snapshot_dir / "daily_published_model_snapshot_manifest.csv"
    )
    errors = validate_files(
        events_path=args.output_dir / EVENTS_FILENAME,
        summary_path=args.output_dir / SUMMARY_FILENAME,
        anomalies_path=args.output_dir / ANOMALIES_FILENAME,
        snapshot_dir=args.snapshot_dir,
        manifest_path=manifest_path,
        price_dir=args.price_dir,
        through_date=args.through_date,
    )
    if errors:
        print("ERROR: pullback_short_reclaim research replay validation failed")
        for error in errors:
            print(f"ERROR: {error}")
        return 1
    print("pullback_short_reclaim research replay validation passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
