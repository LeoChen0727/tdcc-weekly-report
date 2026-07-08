from __future__ import annotations

from pathlib import Path

import pandas as pd

from build_volume_range_breakout_v2_close_only_confirmation_audit import (
    ADVISORY_STATUS,
    ARTIFACT_VERSION,
    BREAKOUT_THRESHOLDS,
    CLOSE_ONLY_TRIGGERS,
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
from build_volume_range_breakout_v2_lowbase_horizon_audit import mark_non_overlap


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
RETURN_BASES = {
    "close_signal_low_stop_next_open_or_fixed_10d_close",
    "fixed_10d_close_no_stop",
    "fixed_60d_close_no_stop",
}
TRIGGER_SCOPES = {"selected_any_close_only", *CLOSE_ONLY_TRIGGERS}


def fail(message: str) -> None:
    print(f"ERROR: {message}")
    raise SystemExit(1)


def read_csv(path: Path) -> pd.DataFrame:
    if not path.exists():
        fail(f"missing required file: {path}")
    try:
        return pd.read_csv(path, dtype=str, keep_default_na=False, low_memory=False)
    except Exception as exc:
        fail(f"{path} is not readable CSV: {exc}")


def false_only(series: pd.Series) -> bool:
    return set(series.astype(str).str.lower().unique()) <= {"false", "0", ""}


def numeric(series: pd.Series) -> pd.Series:
    return pd.to_numeric(series, errors="coerce")


def require_common(name: str, frame: pd.DataFrame) -> None:
    if frame.empty:
        fail(f"{name} must not be empty")
    if set(frame["research_id"].astype(str)) != {RESEARCH_ID}:
        fail(f"{name} research_id must be {RESEARCH_ID}")
    if set(frame["artifact_version"].astype(str)) != {ARTIFACT_VERSION}:
        fail(f"{name} artifact_version must be {ARTIFACT_VERSION}")
    if set(frame["source_research_id"].astype(str)) != {SOURCE_RESEARCH_ID}:
        fail(f"{name} source_research_id must be {SOURCE_RESEARCH_ID}")
    if set(frame["advisory_status"].astype(str)) != {ADVISORY_STATUS}:
        fail(f"{name} advisory_status must be {ADVISORY_STATUS}")
    if set(frame["model_id"].astype(str)) != {MODEL_ID}:
        fail(f"{name} model_id must be {MODEL_ID}")
    if set(frame["production_readiness"].astype(str)) != {PRODUCTION_READINESS}:
        fail(f"{name} production_readiness must be {PRODUCTION_READINESS}")
    if not false_only(frame["approved_for_daily"]):
        fail(f"{name} approved_for_daily must remain false")


def validate_common(summary: pd.DataFrame, detail: pd.DataFrame, history_summary: pd.DataFrame, history_detail: pd.DataFrame) -> None:
    missing_summary = sorted(set(SUMMARY_COLUMNS) - set(summary.columns))
    missing_detail = sorted(set(DETAIL_COLUMNS) - set(detail.columns))
    if missing_summary:
        fail(f"summary missing columns: {missing_summary}")
    if missing_detail:
        fail(f"detail missing columns: {missing_detail}")
    if len(summary) != len(history_summary):
        fail("latest/history summary row counts differ")
    if len(detail) != len(history_detail):
        fail("latest/history detail row counts differ")
    forbidden = sorted((set(summary.columns) | set(detail.columns)) & FORBIDDEN_PRODUCTION_FIELDS)
    if forbidden:
        fail(f"artifact must not contain production decision fields: {forbidden}")
    require_common("summary", summary)
    require_common("detail", detail)
    if set(summary["return_basis"].astype(str)) != RETURN_BASES:
        fail("summary return_basis set mismatch")
    if set(detail["return_basis"].astype(str)) != RETURN_BASES:
        fail("detail return_basis set mismatch")
    if set(summary["trigger_scope"].astype(str)) != TRIGGER_SCOPES:
        fail("summary trigger scopes must include selected_any and all close-only triggers")
    if set(detail["selected_close_only_trigger_id"].astype(str)) - set(CLOSE_ONLY_TRIGGERS):
        fail("detail contains unexpected selected_close_only_trigger_id")


def validate_source(detail: pd.DataFrame) -> pd.DataFrame:
    source = read_csv(SOURCE_DETAIL_CSV)
    if source.empty:
        fail("source detail must not be empty")
    if set(source["research_id"].astype(str)) != {SOURCE_RESEARCH_ID}:
        fail(f"source detail research_id must be {SOURCE_RESEARCH_ID}")
    if not source["source_event_key"].is_unique:
        fail("source_event_key must be unique in source detail")
    if not false_only(source["approved_for_daily"]):
        fail("source detail approved_for_daily must remain false")
    if not set(detail["source_event_key"].astype(str)) <= set(source["source_event_key"].astype(str)):
        fail("detail source_event_key must be subset of source detail")
    counts = detail.groupby(["source_event_key", "return_basis"], dropna=False).size().reset_index(name="count")
    if not counts["count"].eq(1).all():
        fail("each confirmed source_event_key must have one detail row per return_basis")
    per_event_counts = detail.groupby("source_event_key", dropna=False).size()
    if not per_event_counts.eq(len(RETURN_BASES)).all():
        fail("each confirmed source_event_key must have all return bases")
    return source


def validate_summary_grid(summary: pd.DataFrame, source: pd.DataFrame) -> None:
    expected_rows = len(BREAKOUT_THRESHOLDS) * len(TRIGGER_SCOPES) * len(RETURN_BASES)
    if len(summary) != expected_rows:
        fail(f"summary row count {len(summary)} must equal {expected_rows}")
    thresholds = set(numeric(summary["breakout_threshold_pct"]).dropna().astype(float))
    if thresholds != set(float(item) for item in BREAKOUT_THRESHOLDS):
        fail(f"summary thresholds mismatch: {sorted(thresholds)}")
    if "2.0" not in set(summary["breakout_threshold_pct"].astype(str)):
        fail("summary must include the 2pct threshold baseline")
    for col in ["sample_size", "source_event_count", "close_only_confirmed_count", "simulated_event_count"]:
        values = numeric(summary[col])
        if values.isna().any() or values.lt(0).any():
            fail(f"{col} must be non-negative numeric")
    for col in ["win_rate_pct", "neutral_rate_pct", "loss_rate_pct", "coverage_pct"]:
        values = numeric(summary[col])
        if values.dropna().lt(0).any() or values.dropna().gt(100).any():
            fail(f"{col} must be within 0..100")


def validate_non_overlap_replay(summary: pd.DataFrame, detail: pd.DataFrame, source: pd.DataFrame) -> None:
    source_work = source.copy()
    source_work["breakout_over_prev60_pct"] = pd.to_numeric(source_work["breakout_over_prev60_pct"], errors="coerce")
    for _, row in summary.iterrows():
        threshold = float(row["breakout_threshold_pct"])
        source_keys = set(
            source_work.loc[
                source_work["consolidation_type"].astype(str).eq("non_consolidation")
                & source_work["breakout_over_prev60_pct"].ge(threshold),
                "source_event_key",
            ].astype(str)
        )
        part = detail[
            detail["source_event_key"].astype(str).isin(source_keys)
            & detail["return_basis"].astype(str).eq(str(row["return_basis"]))
            & detail["data_quality_flag"].astype(str).eq("ok")
        ].copy()
        trigger_scope = str(row["trigger_scope"])
        if trigger_scope != "selected_any_close_only":
            part = part[part["selected_close_only_trigger_id"].astype(str).eq(trigger_scope)].copy()
        marked = mark_non_overlap(part)
        metric_part = marked[marked["_non_overlap"]].copy() if not marked.empty else marked
        if int(row["simulated_event_count"]) != len(part):
            fail("simulated_event_count mismatch during non-overlap replay")
        if int(row["sample_size"]) != len(metric_part):
            fail("sample_size mismatch during non-overlap replay")
        if int(row["same_stock_overlap_suppressed_count"]) != len(part) - len(metric_part):
            fail("same_stock_overlap_suppressed_count mismatch during non-overlap replay")


def validate_markdown() -> None:
    if not LATEST_MD.exists():
        fail(f"missing markdown output: {LATEST_MD}")
    text = LATEST_MD.read_text(encoding="utf-8", errors="replace")
    required = [
        "research-only replay on existing v1 formal-operation source events",
        "Candidate population: `consolidation_type=non_consolidation`",
        "Close-only triggers",
        "Intraday high/low are not used as confirmation, entry, exit, stop, or realized return prices",
    ]
    for item in required:
        if item not in text:
            fail(f"markdown missing required text: {item}")


def main() -> int:
    summary = read_csv(LATEST_SUMMARY_CSV)
    detail = read_csv(LATEST_DETAIL_CSV)
    history_summary = read_csv(HISTORY_SUMMARY_CSV)
    history_detail = read_csv(HISTORY_DETAIL_CSV)
    validate_common(summary, detail, history_summary, history_detail)
    source = validate_source(detail)
    validate_summary_grid(summary, source)
    validate_non_overlap_replay(summary, detail, source)
    validate_markdown()
    print(
        "volume range breakout v2 close-only confirmation audit validation passed "
        f"summary_rows={len(summary)} detail_rows={len(detail)} source_rows={len(source)}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
