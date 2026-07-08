from __future__ import annotations

from pathlib import Path

import pandas as pd

from build_volume_range_breakout_v2_overlap_sensitivity import (
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


def numeric(series: pd.Series) -> pd.Series:
    return pd.to_numeric(series, errors="coerce")


def require_single(summary: pd.DataFrame, condition_set_id: str, selection_basis: str) -> pd.Series:
    rows = summary[
        summary["condition_set_id"].astype(str).eq(condition_set_id)
        & summary["selection_basis"].astype(str).eq(selection_basis)
    ]
    if len(rows) != 1:
        fail(f"expected exactly one row for {condition_set_id}/{selection_basis}; got {len(rows)}")
    return rows.iloc[0]


def parse_yyyymmdd(series: pd.Series) -> pd.Series:
    text = series.astype(str).str.replace(r"\.0$", "", regex=True).str.strip()
    return pd.to_datetime(text, format="%Y%m%d", errors="coerce")


def overlap_pair_count(frame: pd.DataFrame) -> int:
    if frame.empty:
        return 0
    work = frame.copy()
    work["_entry_dt"] = parse_yyyymmdd(work["entry_date"])
    work["_exit_dt"] = parse_yyyymmdd(work["exit_date"])
    if work["_entry_dt"].isna().any() or work["_exit_dt"].isna().any():
        fail("detail has unparseable entry_date or exit_date")
    count = 0
    for _, part in work.sort_values(["stock_id", "_entry_dt", "_exit_dt", "source_event_key"]).groupby(
        "stock_id", dropna=False
    ):
        active: list[pd.Series] = []
        for _, row in part.iterrows():
            for prior in active:
                if row["_entry_dt"] <= prior["_exit_dt"]:
                    count += 1
            active = [prior for prior in active if prior["_exit_dt"] >= row["_entry_dt"]]
            active.append(row)
    return count


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


def validate_source_and_detail(detail: pd.DataFrame) -> int:
    source = read_csv(SOURCE_DETAIL_CSV)
    if source.empty:
        fail("source detail must not be empty")
    if source.get("source_event_key", pd.Series(dtype=str)).duplicated().any():
        fail("source detail source_event_key must be unique")
    if len(source) != len(detail):
        fail(f"detail row count {len(detail)} must match source row count {len(source)}")
    if detail["source_event_key"].duplicated().any():
        fail("overlap detail source_event_key must be unique")
    source_keys = set(source["source_event_key"].astype(str))
    detail_keys = set(detail["source_event_key"].astype(str))
    if source_keys != detail_keys:
        fail("overlap detail source_event_key set must match source detail")
    if overlap_pair_count(detail) <= 0:
        fail("detail must preserve event-level overlaps for audit visibility")
    return len(source)


def validate_summary(summary: pd.DataFrame, source_rows: int, detail: pd.DataFrame) -> None:
    if summary.duplicated(["condition_set_id", "selection_basis"]).any():
        fail("summary has duplicate condition_set_id/selection_basis rows")
    required_condition_sets = {
        "baseline_all",
        "off120_le40",
        "off240_le40",
        "range60_le25",
        "range120_le25",
        "off120_le40_range60_le25",
        "off240_le40_range60_le25",
        "limit_up_like",
        "not_limit_up_like",
    }
    required_selection = {"event_level_all_events", "first_event_per_stock", "same_stock_non_overlap"}
    if set(summary["condition_set_id"].astype(str)) != required_condition_sets:
        fail("summary condition_set_id set mismatch")
    if set(summary["selection_basis"].astype(str)) != required_selection:
        fail("summary selection_basis set mismatch")

    samples = numeric(summary["sample_size"])
    baselines = numeric(summary["baseline_event_count"])
    if samples.isna().any() or baselines.isna().any():
        fail("sample_size and baseline_event_count must be numeric")
    if (samples < 0).any() or (samples > baselines).any():
        fail("sample_size must be non-negative and not exceed baseline_event_count")
    if set(summary["baseline_event_count"].astype(int)) != {source_rows}:
        fail("every summary row must carry source baseline_event_count")
    for col in ["coverage_pct", "win_rate_pct", "neutral_rate_pct", "loss_rate_pct"]:
        values = numeric(summary[col])
        if values.dropna().lt(0).any() or values.dropna().gt(100).any():
            fail(f"{col} must be within 0..100")

    event_baseline = require_single(summary, "baseline_all", "event_level_all_events")
    first_baseline = require_single(summary, "baseline_all", "first_event_per_stock")
    non_overlap_baseline = require_single(summary, "baseline_all", "same_stock_non_overlap")
    if int(event_baseline["sample_size"]) != source_rows:
        fail("event-level baseline sample_size must match source rows")
    unique_stocks = detail["stock_id"].nunique()
    if int(first_baseline["sample_size"]) != unique_stocks:
        fail("first-event baseline sample_size must match source unique stock count")
    if int(non_overlap_baseline["sample_size"]) >= source_rows:
        fail("same-stock non-overlap baseline must suppress at least one row")
    if int(non_overlap_baseline["overlap_pair_count"]) != 0:
        fail("same-stock non-overlap baseline overlap_pair_count must be zero")

    non_overlap_rows = summary[summary["selection_basis"].astype(str).eq("same_stock_non_overlap")]
    if numeric(non_overlap_rows["overlap_pair_count"]).fillna(-1).ne(0).any():
        fail("every same_stock_non_overlap summary row must have zero overlap_pair_count")
    if numeric(non_overlap_rows["suppressed_same_stock_overlap_count"]).fillna(0).lt(0).any():
        fail("suppressed_same_stock_overlap_count must be non-negative")


def validate_8454_regression(detail: pd.DataFrame) -> None:
    rows = detail[detail["stock_id"].astype(str).eq("8454")].sort_values(["entry_date", "exit_date"])
    if len(rows) != 3:
        fail(f"expected three 8454 rows in current v2 overlap fixture; got {len(rows)}")
    included = rows["same_stock_non_overlap_included"].astype(str).str.lower().tolist()
    if included != ["true", "false", "false"]:
        fail(f"8454 non-overlap inclusion mismatch: {included}")
    suppressed = rows.iloc[1:]
    if not suppressed["same_stock_non_overlap_suppression_reason"].astype(str).eq(
        "same_stock_active_position_overlap"
    ).all():
        fail("8454 suppressed rows must carry same_stock_active_position_overlap")
    first_key = rows.iloc[0]["source_event_key"]
    if not suppressed["suppressed_by_source_event_key"].astype(str).eq(first_key).all():
        fail("8454 suppressed rows must point to the first accepted event")


def validate_markdown() -> None:
    if not LATEST_MD.exists():
        fail(f"missing markdown summary: {LATEST_MD}")
    text = LATEST_MD.read_text(encoding="utf-8")
    for needle in [RESEARCH_ID, "research-only", "same-stock non-overlap"]:
        if needle not in text:
            fail(f"markdown summary missing required text: {needle}")


def main() -> int:
    summary = read_csv(LATEST_SUMMARY_CSV)
    history = read_csv(HISTORY_SUMMARY_CSV)
    detail = read_csv(LATEST_DETAIL_CSV)
    detail_history = read_csv(HISTORY_DETAIL_CSV)

    validate_common(summary, history, detail, detail_history)
    source_rows = validate_source_and_detail(detail)
    validate_summary(summary, source_rows, detail)
    validate_8454_regression(detail)
    validate_markdown()

    print(f"Validated {LATEST_SUMMARY_CSV} rows={len(summary)}")
    print(f"Validated {LATEST_DETAIL_CSV} rows={len(detail)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
