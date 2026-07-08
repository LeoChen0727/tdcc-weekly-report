from __future__ import annotations

from pathlib import Path

import pandas as pd

from build_volume_range_breakout_v2_feature_slice_analysis import (
    ADVISORY_STATUS,
    ARTIFACT_VERSION,
    DETAIL_COLUMNS,
    HISTORY_DETAIL_CSV,
    HISTORY_SUMMARY_CSV,
    LATEST_DETAIL_CSV,
    LATEST_SUMMARY_CSV,
    LATEST_SUMMARY_MD,
    MODEL_ID,
    PRODUCTION_READINESS,
    RAW_DETAIL_CSV,
    RESEARCH_ID,
    SEMANTIC_DETAIL_CSV,
    SEMANTIC_SOURCE_RESEARCH_ID,
    SOURCE_RESEARCH_ID,
    SUMMARY_COLUMNS,
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


def require_single(summary: pd.DataFrame, row_type: str, slice_id: str) -> pd.Series:
    rows = summary[summary["row_type"].astype(str).eq(row_type) & summary["slice_id"].astype(str).eq(slice_id)]
    if len(rows) != 1:
        fail(f"expected exactly one {row_type}/{slice_id}; got {len(rows)}")
    return rows.iloc[0]


def numeric(series: pd.Series) -> pd.Series:
    return pd.to_numeric(series, errors="coerce")


def validate_sources(summary: pd.DataFrame, detail: pd.DataFrame) -> tuple[int, int]:
    raw = read_csv(RAW_DETAIL_CSV)
    semantic = read_csv(SEMANTIC_DETAIL_CSV)
    if raw.empty or semantic.empty:
        fail("source details must not be empty")
    if set(raw.get("research_id", pd.Series(dtype=str)).astype(str)) != {SOURCE_RESEARCH_ID}:
        fail("raw detail source research_id mismatch")
    if set(semantic.get("research_id", pd.Series(dtype=str)).astype(str)) != {SEMANTIC_SOURCE_RESEARCH_ID}:
        fail("semantic detail source research_id mismatch")
    if raw["source_event_key"].duplicated().any():
        fail("raw detail source_event_key must be unique")
    if detail["source_event_key"].duplicated().any():
        fail("feature detail source_event_key must be unique")
    if len(detail) != len(raw):
        fail(f"feature detail rows {len(detail)} must match raw rows {len(raw)}")
    missing = set(raw["source_event_key"].astype(str)) - set(detail["source_event_key"].astype(str))
    if missing:
        fail(f"feature detail missing raw source_event_key rows: {sorted(missing)[:5]}")
    baseline = require_single(summary, "performance_slice", "baseline_all_v2_raw_events")
    if int(baseline["sample_size"]) != len(raw):
        fail("baseline sample_size must match raw source rows")
    if baseline["decision_hint"] != "baseline_reference":
        fail("baseline row must be baseline_reference")
    return len(raw), len(semantic)


def validate_common(summary: pd.DataFrame, history: pd.DataFrame, detail: pd.DataFrame, detail_history: pd.DataFrame) -> None:
    if summary.empty:
        fail("summary output must not be empty")
    if detail.empty:
        fail("detail output must not be empty")
    if len(summary) != len(history):
        fail("latest/history summary row counts differ")
    if len(detail) != len(detail_history):
        fail("latest/history detail row counts differ")
    missing_summary = sorted(set(SUMMARY_COLUMNS) - set(summary.columns))
    missing_detail = sorted(set(DETAIL_COLUMNS) - set(detail.columns))
    if missing_summary:
        fail(f"summary missing columns: {missing_summary}")
    if missing_detail:
        fail(f"detail missing columns: {missing_detail}")
    forbidden = sorted((set(summary.columns) | set(detail.columns)) & FORBIDDEN_PRODUCTION_FIELDS)
    if forbidden:
        fail(f"research artifact must not contain production decision fields: {forbidden}")
    for frame_name, frame in [("summary", summary), ("detail", detail)]:
        if set(frame["research_id"].astype(str)) != {RESEARCH_ID}:
            fail(f"{frame_name} research_id must be {RESEARCH_ID}")
        if set(frame["artifact_version"].astype(str)) != {ARTIFACT_VERSION}:
            fail(f"{frame_name} artifact_version must be {ARTIFACT_VERSION}")
        if set(frame["source_research_id"].astype(str)) != {SOURCE_RESEARCH_ID}:
            fail(f"{frame_name} source_research_id must be {SOURCE_RESEARCH_ID}")
        if set(frame["semantic_source_research_id"].astype(str)) != {SEMANTIC_SOURCE_RESEARCH_ID}:
            fail(f"{frame_name} semantic_source_research_id must be {SEMANTIC_SOURCE_RESEARCH_ID}")
        if set(frame["advisory_status"].astype(str)) != {ADVISORY_STATUS}:
            fail(f"{frame_name} advisory_status must be {ADVISORY_STATUS}")
        if set(frame["model_id"].astype(str)) != {MODEL_ID}:
            fail(f"{frame_name} model_id must be {MODEL_ID}")
        if set(frame["production_readiness"].astype(str)) != {PRODUCTION_READINESS}:
            fail(f"{frame_name} production_readiness must be {PRODUCTION_READINESS}")
        if not false_only(frame["approved_for_daily"]):
            fail(f"{frame_name} approved_for_daily must remain false")


def validate_required_slices(summary: pd.DataFrame) -> None:
    required = [
        "baseline_all_v2_raw_events",
        "off60_le50_range60_le45",
        "off60_le40_range60_le35",
        "off60_gt75_or_range60_gt60",
        "range60_le35_narrow",
        "range60_gt60_very_wide",
        "consolidated_any",
        "non_consolidation",
        "locked_limit_up",
        "not_locked_limit_up",
        "overheat_flag_true",
        "overheat_flag_false",
        "low_base_loose_and_consolidated",
        "low_base_loose_not_overheat",
        "high_or_wide_overheat",
        "high_wide_non_consolidation",
    ]
    for slice_id in required:
        require_single(summary, "performance_slice", slice_id)
    row_types = set(summary["row_type"].astype(str))
    for row_type in ["performance_slice", "high_low_feature_share", "high_low_numeric_median", "anomaly_check", "anomaly_extreme_list"]:
        if row_type not in row_types:
            fail(f"summary missing row_type={row_type}")
    if summary[summary["row_type"].eq("high_low_feature_share")].empty:
        fail("feature share rows must not be empty")
    if summary[summary["row_type"].eq("high_low_numeric_median")].empty:
        fail("numeric comparison rows must not be empty")


def validate_metrics(summary: pd.DataFrame, detail: pd.DataFrame) -> None:
    perf = summary[summary["row_type"].astype(str).eq("performance_slice")].copy()
    if perf.empty:
        fail("performance slices must not be empty")
    samples = numeric(perf["sample_size"])
    coverage = numeric(perf["coverage_pct"])
    if samples.isna().any() or samples.lt(0).any():
        fail("performance sample_size must be non-negative numeric")
    if coverage.dropna().lt(0).any() or coverage.dropna().gt(100).any():
        fail("coverage_pct must be within 0..100")
    for col in ["win_rate_pct", "neutral_rate_pct", "loss_rate_pct", "top20_share_pct", "bottom20_share_pct"]:
        values = numeric(perf[col])
        if values.dropna().lt(0).any() or values.dropna().gt(100).any():
            fail(f"{col} must be within 0..100")
    outcomes = set(detail["return_outcome"].astype(str))
    if not outcomes <= {"win", "neutral", "loss"}:
        fail(f"unexpected return_outcome values: {sorted(outcomes)}")
    for flag in [
        "top20_return_flag",
        "bottom20_return_flag",
        "low_base_loose_flag",
        "low_base_strict_flag",
        "consolidated_any_flag",
        "locked_limit_up_flag",
        "overheat_flag",
    ]:
        values = set(detail[flag].astype(str))
        if not values <= {"True", "False"}:
            fail(f"{flag} must be True/False")
    if detail["top20_return_flag"].astype(str).eq("True").sum() == 0:
        fail("top20_return_flag must mark rows")
    if detail["bottom20_return_flag"].astype(str).eq("True").sum() == 0:
        fail("bottom20_return_flag must mark rows")


def validate_markdown() -> None:
    if not LATEST_SUMMARY_MD.exists():
        fail(f"missing markdown output: {LATEST_SUMMARY_MD}")
    text = LATEST_SUMMARY_MD.read_text(encoding="utf-8", errors="replace")
    required = [
        "Research-only artifact",
        "Source population: 808 raw-market events",
        "low-base vs high/extended setups",
        "does not change production model conditions",
        "separate promotion review",
    ]
    for item in required:
        if item not in text:
            fail(f"markdown missing required text: {item}")


def main() -> int:
    summary = read_csv(LATEST_SUMMARY_CSV)
    history = read_csv(HISTORY_SUMMARY_CSV)
    detail = read_csv(LATEST_DETAIL_CSV)
    detail_history = read_csv(HISTORY_DETAIL_CSV)
    validate_common(summary, history, detail, detail_history)
    raw_rows, semantic_rows = validate_sources(summary, detail)
    validate_required_slices(summary)
    validate_metrics(summary, detail)
    validate_markdown()
    print(
        "volume range breakout v2 feature slice analysis validation passed "
        f"summary_rows={len(summary)} detail_rows={len(detail)} raw_rows={raw_rows} semantic_rows={semantic_rows}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
