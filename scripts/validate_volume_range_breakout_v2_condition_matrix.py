from __future__ import annotations

from pathlib import Path

import pandas as pd

from build_volume_range_breakout_v2_condition_matrix import (
    ADVISORY_STATUS,
    ARTIFACT_VERSION,
    HISTORY_MATRIX_CSV,
    LATEST_MATRIX_CSV,
    LATEST_MATRIX_MD,
    MATRIX_COLUMNS,
    MODEL_ID,
    PRODUCTION_READINESS,
    RESEARCH_ID,
    SOURCE_DETAIL_CSV,
    SOURCE_RESEARCH_ID,
)


FORBIDDEN_PRODUCTION_FIELDS = {
    "trade_decision",
    "action_rating",
    "entry_style",
    "position_sizing",
    "decision_score",
    "daily_candidate_decision",
    "buy_signal",
    "approved_for_daily_true",
}


def fail(message: str) -> None:
    print(f"ERROR: {message}")
    raise SystemExit(1)


def read_csv(path: Path) -> pd.DataFrame:
    if not path.exists():
        fail(f"missing required file: {path}")
    try:
        return pd.read_csv(path, dtype=str, keep_default_na=False)
    except Exception as exc:
        fail(f"{path} is not readable CSV: {exc}")


def false_only(series: pd.Series) -> bool:
    return set(series.astype(str).str.lower().unique()) <= {"false", "0", ""}


def require_single(matrix: pd.DataFrame, condition_set_id: str) -> pd.Series:
    rows = matrix[matrix["condition_set_id"].astype(str).eq(condition_set_id)]
    if len(rows) != 1:
        fail(f"expected exactly one row for {condition_set_id}; got {len(rows)}")
    return rows.iloc[0]


def numeric(series: pd.Series) -> pd.Series:
    return pd.to_numeric(series, errors="coerce")


def validate_common(matrix: pd.DataFrame, history: pd.DataFrame) -> None:
    if matrix.empty:
        fail("matrix output must not be empty")
    if len(matrix) != len(history):
        fail("latest/history matrix row counts differ")
    missing = sorted(set(MATRIX_COLUMNS) - set(matrix.columns))
    if missing:
        fail(f"matrix missing columns: {missing}")
    forbidden = sorted(set(matrix.columns) & FORBIDDEN_PRODUCTION_FIELDS)
    if forbidden:
        fail(f"matrix must not contain production decision fields: {forbidden}")
    if set(matrix["research_id"].astype(str)) != {RESEARCH_ID}:
        fail(f"research_id must be {RESEARCH_ID}")
    if set(matrix["artifact_version"].astype(str)) != {ARTIFACT_VERSION}:
        fail(f"artifact_version must be {ARTIFACT_VERSION}")
    if set(matrix["source_research_id"].astype(str)) != {SOURCE_RESEARCH_ID}:
        fail(f"source_research_id must be {SOURCE_RESEARCH_ID}")
    if set(matrix["advisory_status"].astype(str)) != {ADVISORY_STATUS}:
        fail(f"advisory_status must be {ADVISORY_STATUS}")
    if set(matrix["model_id"].astype(str)) != {MODEL_ID}:
        fail(f"model_id must be {MODEL_ID}")
    if set(matrix["production_readiness"].astype(str)) != {PRODUCTION_READINESS}:
        fail(f"production_readiness must be {PRODUCTION_READINESS}")
    if not false_only(matrix["approved_for_daily"]):
        fail("approved_for_daily must remain false for every matrix row")
    if matrix["condition_set_id"].duplicated().any():
        dupes = matrix[matrix["condition_set_id"].duplicated()]["condition_set_id"].head(5).tolist()
        fail(f"duplicate condition_set_id values: {dupes}")


def validate_source_detail() -> int:
    detail = read_csv(SOURCE_DETAIL_CSV)
    if detail.empty:
        fail("source semantic audit detail must not be empty")
    if set(detail.get("research_id", pd.Series(dtype=str)).astype(str)) != {SOURCE_RESEARCH_ID}:
        fail("source detail must be volume_range_breakout_v2_semantic_audit")
    if not false_only(detail.get("approved_for_daily", pd.Series(dtype=str))):
        fail("source detail approved_for_daily must remain false")
    if detail.get("source_event_key", pd.Series(dtype=str)).duplicated().any():
        fail("source detail must remain deduped")
    return len(detail)


def validate_windows_and_baseline(matrix: pd.DataFrame, source_rows: int) -> None:
    baseline = require_single(matrix, "baseline_all_dedup")
    if int(baseline["sample_size"]) != source_rows:
        fail(f"baseline sample_size {baseline['sample_size']} does not match source rows {source_rows}")
    if baseline["candidate_interpretation"] != "baseline_reference":
        fail("baseline row must be baseline_reference")

    counts: dict[int, int] = {}
    for window in [20, 40, 60]:
        row = require_single(matrix, f"prev{window}_high_only")
        if row["matrix_family"] != "high_window_only":
            fail(f"prev{window}_high_only must be high_window_only")
        if row["promotion_guard"] != "source_signal_only_needs_full_raw_backtest":
            fail(f"prev{window}_high_only must be source-signal research-only")
        counts[window] = int(row["sample_size"])
        for suffix in [
            "high_not_locked_limit_up",
            "high_off60_le50_range60_le45",
            "high_off60_le40_range60_le35",
            "high_consolidated_any",
            "high_short_consolidation",
            "high_volume_ratio_2_to_6",
            "high_signal_return_lt_9_8",
            "high_next_day_continuation",
            "high_pullback_5ma_or_10ma",
            "high_exclude_breakout_failure",
            "high_not_locked_next_day_continuation",
        ]:
            require_single(matrix, f"prev{window}_{suffix}")
    if not (counts[20] >= counts[40] >= counts[60] > 0):
        fail(f"high-window counts must be monotonic 20>=40>=60>0; got {counts}")


def validate_metric_sanity(matrix: pd.DataFrame) -> None:
    samples = numeric(matrix["sample_size"])
    baseline_samples = numeric(matrix["baseline_sample_size"])
    if samples.isna().any() or baseline_samples.isna().any():
        fail("sample_size and baseline_sample_size must be numeric")
    if (samples > baseline_samples).any():
        fail("condition sample_size must not exceed baseline_sample_size")
    if (samples < 0).any():
        fail("sample_size must not be negative")
    for col in ["win_rate_pct", "neutral_rate_pct", "loss_rate_pct", "coverage_pct"]:
        values = numeric(matrix[col])
        if values.dropna().lt(0).any() or values.dropna().gt(100).any():
            fail(f"{col} must be within 0..100")
    required_status = {"reviewable_sample", "thin_sample", "insufficient_sample"}
    if not set(matrix["sample_status"].astype(str)) <= required_status:
        fail("sample_status contains unexpected values")
    if not matrix["matrix_family"].astype(str).eq("low_base_proxy").any():
        fail("matrix must contain low_base_proxy rows")
    if not matrix["matrix_family"].astype(str).eq("confirmation_timing").any():
        fail("matrix must contain confirmation_timing rows")
    diagnostics = matrix[matrix["matrix_family"].astype(str).eq("diagnostic_only")]
    if diagnostics.empty:
        fail("matrix must contain diagnostic_only rows")
    if not diagnostics["candidate_interpretation"].astype(str).eq("diagnostic_only_not_promotion_evidence").all():
        fail("diagnostic_only rows must not be promotion evidence")


def validate_markdown() -> None:
    if not LATEST_MATRIX_MD.exists():
        fail(f"missing markdown output: {LATEST_MATRIX_MD}")
    text = LATEST_MATRIX_MD.read_text(encoding="utf-8", errors="replace")
    required = [
        "research-only",
        "does not change `stock_model_contract_registry.csv`",
        "20/40/60 previous-high windows",
        "Low/base proxies are tested as evidence",
        "not a full raw-market producer rerun",
    ]
    for item in required:
        if item not in text:
            fail(f"markdown missing required text: {item}")


def main() -> int:
    source_rows = validate_source_detail()
    matrix = read_csv(LATEST_MATRIX_CSV)
    history = read_csv(HISTORY_MATRIX_CSV)
    validate_common(matrix, history)
    validate_windows_and_baseline(matrix, source_rows)
    validate_metric_sanity(matrix)
    validate_markdown()
    print(f"volume range breakout v2 condition matrix validation passed rows={len(matrix)} source_rows={source_rows}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
