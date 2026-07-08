from __future__ import annotations

from pathlib import Path

import pandas as pd

from build_volume_range_breakout_v2_deep_low_base_matrix import (
    ADVISORY_STATUS,
    ARTIFACT_VERSION,
    DETAIL_COLUMNS,
    HISTORY_DETAIL_CSV,
    HISTORY_SUMMARY_CSV,
    LATEST_DETAIL_CSV,
    LATEST_MD,
    LATEST_SUMMARY_CSV,
    MODEL_ID,
    PRODUCTION_READINESS,
    RESEARCH_ID,
    SOURCE_DETAIL_CSV,
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


def require_single(summary: pd.DataFrame, condition_set_id: str) -> pd.Series:
    rows = summary[summary["condition_set_id"].astype(str).eq(condition_set_id)]
    if len(rows) != 1:
        fail(f"expected exactly one row for {condition_set_id}; got {len(rows)}")
    return rows.iloc[0]


def numeric(series: pd.Series) -> pd.Series:
    return pd.to_numeric(series, errors="coerce")


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
        if set(frame["advisory_status"].astype(str)) != {ADVISORY_STATUS}:
            fail(f"{frame_name} advisory_status must be {ADVISORY_STATUS}")
        if set(frame["model_id"].astype(str)) != {MODEL_ID}:
            fail(f"{frame_name} model_id must be {MODEL_ID}")
        if set(frame["production_readiness"].astype(str)) != {PRODUCTION_READINESS}:
            fail(f"{frame_name} production_readiness must be {PRODUCTION_READINESS}")
        if not false_only(frame["approved_for_daily"]):
            fail(f"{frame_name} approved_for_daily must remain false")


def validate_source_and_baseline(summary: pd.DataFrame, detail: pd.DataFrame) -> int:
    source = read_csv(SOURCE_DETAIL_CSV)
    if source.empty:
        fail("source detail must not be empty")
    if set(source.get("research_id", pd.Series(dtype=str)).astype(str)) != {SOURCE_RESEARCH_ID}:
        fail("source detail research_id mismatch")
    if source["source_event_key"].duplicated().any():
        fail("source detail source_event_key must be unique")
    if detail["source_event_key"].duplicated().any():
        fail("deep-low detail source_event_key must be unique")
    if len(detail) != len(source):
        fail(f"deep-low detail rows {len(detail)} must match source rows {len(source)}")
    missing = set(source["source_event_key"].astype(str)) - set(detail["source_event_key"].astype(str))
    if missing:
        fail(f"deep-low detail missing source rows: {sorted(missing)[:5]}")
    baseline = require_single(summary, "baseline_prev60_high_next_day_continuation")
    if int(baseline["sample_size"]) != len(source):
        fail("baseline sample_size must match source raw rerun rows")
    if baseline["decision_hint"] != "baseline_reference":
        fail("baseline decision_hint must be baseline_reference")
    if baseline["requires_60d_high_breakout"] != "True" or baseline["requires_next_day_continuation"] != "True":
        fail("baseline must record current v2 population gates")
    return len(source)


def validate_required_conditions(summary: pd.DataFrame) -> None:
    required = [
        "baseline_prev60_high_next_day_continuation",
        "coverage_off120_available",
        "coverage_off240_available",
        "coverage_range120_available",
    ]
    for low_window in [120, 240]:
        for low_threshold in [20, 30, 40]:
            required.append(f"off{low_window}_le{low_threshold}")
            for range_window, widths in [(60, [25, 35]), (120, [25, 35, 45])]:
                for width in widths:
                    required.append(f"off{low_window}_le{low_threshold}_range{range_window}_le{width}")
    for range_window, widths in [(60, [25, 35]), (120, [25, 35, 45])]:
        for width in widths:
            required.append(f"range{range_window}_le{width}")
    for condition_set_id in required:
        require_single(summary, condition_set_id)
    if summary["condition_set_id"].duplicated().any():
        dupes = summary[summary["condition_set_id"].duplicated()]["condition_set_id"].head(5).tolist()
        fail(f"duplicate condition_set_id values: {dupes}")


def validate_metrics(summary: pd.DataFrame, detail: pd.DataFrame) -> None:
    samples = numeric(summary["sample_size"])
    baseline_samples = numeric(summary["baseline_sample_size"])
    if samples.isna().any() or baseline_samples.isna().any():
        fail("sample_size and baseline_sample_size must be numeric")
    if (samples < 0).any() or (samples > baseline_samples).any():
        fail("sample_size must be non-negative and not exceed baseline")
    for col in ["coverage_pct", "win_rate_pct", "neutral_rate_pct", "loss_rate_pct"]:
        values = numeric(summary[col])
        if values.dropna().lt(0).any() or values.dropna().gt(100).any():
            fail(f"{col} must be within 0..100")
    statuses = set(summary["sample_status"].astype(str))
    expected_statuses = {
        "reviewable_sample",
        "thin_but_reviewable_sample",
        "thin_sample",
        "very_thin_sample",
        "insufficient_sample",
    }
    if not statuses <= expected_statuses:
        fail(f"unexpected sample_status values: {sorted(statuses)}")
    for flag in [
        "deep_low_120_le20",
        "deep_low_120_le30",
        "deep_low_120_le40",
        "deep_low_240_le20",
        "deep_low_240_le30",
        "deep_low_240_le40",
        "range60_le25",
        "range60_le35",
        "range120_le25",
        "range120_le35",
        "range120_le45",
    ]:
        values = set(detail[flag].astype(str))
        if not values <= {"True", "False"}:
            fail(f"{flag} must be True/False")
    for col in ["off_120d_low_pct", "off_240d_low_pct", "range_width_120_pct"]:
        if numeric(detail[col]).notna().sum() == 0:
            fail(f"{col} must have numeric coverage")
    if detail["source_high_breakout_60d_met"].astype(str).ne("True").any():
        fail("deep-low source population must preserve high_breakout_60d_met=True")
    if detail["source_next_day_continuation_confirmed"].astype(str).ne("True").any():
        fail("deep-low source population must preserve next_day_continuation_confirmed=True")


def validate_markdown() -> None:
    if not LATEST_MD.exists():
        fail(f"missing markdown output: {LATEST_MD}")
    text = LATEST_MD.read_text(encoding="utf-8", errors="replace")
    required = [
        "Research-only artifact",
        "previous-60-day high breakout and next-day continuation",
        "120/240-day distance from low",
        "Coverage diagnostic rows are included",
        "does not change production model conditions",
        "separate raw producer/backtest",
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
    source_rows = validate_source_and_baseline(summary, detail)
    validate_required_conditions(summary)
    validate_metrics(summary, detail)
    validate_markdown()
    print(
        "volume range breakout v2 deep low-base matrix validation passed "
        f"summary_rows={len(summary)} detail_rows={len(detail)} source_rows={source_rows}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
