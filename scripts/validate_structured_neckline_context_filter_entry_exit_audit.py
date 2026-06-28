from __future__ import annotations

from pathlib import Path

import pandas as pd

from build_structured_neckline_context_filter_entry_exit_audit import (
    ALL_COHORT_ID,
    DETAIL_COLUMNS,
    EVENT_COLUMNS,
    EXCLUDED_COHORT_ID,
    HISTORY_DETAIL_CSV,
    HISTORY_EVENT_CSV,
    HISTORY_SUMMARY_CSV,
    LATEST_DETAIL_CSV,
    LATEST_EVENT_CSV,
    LATEST_MD,
    LATEST_SUMMARY_CSV,
    PARAMETER_SET_ID,
    PASS_COHORT_ID,
    PRODUCTION_READINESS,
    RESEARCH_ID,
    RESEARCH_VARIANT_ID,
    SUMMARY_COLUMNS,
    TARGET_CONTEXT_EXCLUSION,
    TARGET_CURRENT_EXIT_RULE,
    TARGET_CURRENT_OUTCOME_RULE,
    TARGET_CURRENT_STOP_RULE,
    TARGET_SEGMENT_ID,
)
from build_structured_neckline_retest_entry_exit_grid import EVENT_FAMILY_ID
from build_structured_neckline_retest_review_packet import FORBIDDEN_PRODUCTION_FIELDS


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


def require_columns(frame: pd.DataFrame, columns: list[str], label: str) -> None:
    missing = sorted(set(columns) - set(frame.columns))
    if missing:
        fail(f"{label} missing columns: {missing}")


def validate_constants(frame: pd.DataFrame, label: str) -> None:
    constants = {
        "research_id": RESEARCH_ID,
        "research_variant_id": RESEARCH_VARIANT_ID,
        "parameter_set_id": PARAMETER_SET_ID,
        "advisory_status": RESEARCH_VARIANT_ID,
        "event_family_id": EVENT_FAMILY_ID,
        "segment_id": TARGET_SEGMENT_ID,
        "production_readiness": PRODUCTION_READINESS,
    }
    for column, expected in constants.items():
        values = set(frame[column].astype(str))
        if values != {expected}:
            fail(f"{label} {column} must be {expected}; got {sorted(values)}")
    if not false_only(frame["approved_for_daily"]):
        fail(f"{label} approved_for_daily must remain false")


def main() -> int:
    events = read_csv(LATEST_EVENT_CSV)
    detail = read_csv(LATEST_DETAIL_CSV)
    summary = read_csv(LATEST_SUMMARY_CSV)
    history_events = read_csv(HISTORY_EVENT_CSV)
    history_detail = read_csv(HISTORY_DETAIL_CSV)
    history_summary = read_csv(HISTORY_SUMMARY_CSV)
    if events.empty or detail.empty or summary.empty:
        fail("latest outputs must not be empty")
    if len(events) != len(history_events):
        fail("event latest/history row counts differ")
    if len(detail) != len(history_detail):
        fail("detail latest/history row counts differ")
    if len(summary) != len(history_summary):
        fail("summary latest/history row counts differ")
    if not LATEST_MD.exists():
        fail(f"missing markdown output: {LATEST_MD}")

    require_columns(events, EVENT_COLUMNS, "events")
    require_columns(detail, DETAIL_COLUMNS, "detail")
    require_columns(summary, SUMMARY_COLUMNS, "summary")
    forbidden = sorted((set(events.columns) | set(detail.columns) | set(summary.columns)) & FORBIDDEN_PRODUCTION_FIELDS)
    if forbidden:
        fail(f"outputs must not emit production decision fields: {forbidden}")
    validate_constants(events, "events")
    validate_constants(detail, "detail")
    validate_constants(summary, "summary")

    event_results = set(events["visual_context_filter_result"].astype(str))
    if event_results != {"pass", "excluded"}:
        fail(f"events must contain pass and excluded rows; got {sorted(event_results)}")
    excluded_contexts = set(events.loc[events["visual_context_filter_result"].eq("excluded"), "visual_pre_signal_context"].astype(str))
    if excluded_contexts != {TARGET_CONTEXT_EXCLUSION}:
        fail(f"excluded rows must be exactly {TARGET_CONTEXT_EXCLUSION}; got {sorted(excluded_contexts)}")
    pass_contexts = set(events.loc[events["visual_context_filter_result"].eq("pass"), "visual_pre_signal_context"].astype(str))
    if TARGET_CONTEXT_EXCLUSION in pass_contexts:
        fail("pass rows must not contain bearish visual context")

    expected_cohorts = {ALL_COHORT_ID, PASS_COHORT_ID, EXCLUDED_COHORT_ID}
    if set(detail["cohort_id"].astype(str)) != expected_cohorts:
        fail(f"detail cohort mismatch: {sorted(set(detail['cohort_id'].astype(str)))}")
    if set(summary["cohort_id"].astype(str)) != expected_cohorts:
        fail(f"summary cohort mismatch: {sorted(set(summary['cohort_id'].astype(str)))}")
    event_count = len(events)
    pass_count = int(events["visual_context_filter_result"].eq("pass").sum())
    excluded_count = int(events["visual_context_filter_result"].eq("excluded").sum())
    combos_per_event = int(len(detail[detail["cohort_id"].eq(ALL_COHORT_ID)]) / event_count)
    if combos_per_event <= 0:
        fail("could not infer detail combos per event")
    if len(detail[detail["cohort_id"].eq(PASS_COHORT_ID)]) != pass_count * combos_per_event:
        fail("pass detail row count does not match pass event count")
    if len(detail[detail["cohort_id"].eq(EXCLUDED_COHORT_ID)]) != excluded_count * combos_per_event:
        fail("excluded detail row count does not match excluded event count")

    current = summary[
        summary["stop_rule_id"].eq(TARGET_CURRENT_STOP_RULE)
        & summary["exit_rule_id"].eq(TARGET_CURRENT_EXIT_RULE)
        & summary["outcome_rule_id"].eq(TARGET_CURRENT_OUTCOME_RULE)
    ]
    if set(current["cohort_id"].astype(str)) != expected_cohorts:
        fail("current e04 rule must have all cohorts")
    rate_columns = [
        "pure_win_rate_pct",
        "neutral_inclusive_success_rate_pct",
        "positive_return_rate_pct",
        "avg_return_pct",
        "median_return_pct",
        "avg_mfe_pct",
        "avg_mae_pct",
    ]
    for column in rate_columns:
        if pd.to_numeric(summary[column], errors="coerce").isna().any():
            fail(f"summary column must be numeric: {column}")

    md_text = LATEST_MD.read_text(encoding="utf-8", errors="replace")
    required_text = [
        "visual_pre_signal_context",
        "Current e04 Rule Before/After Filter",
        "Top Non-Bearish Entry/Exit Rows",
        "production impact: `none`",
        PRODUCTION_READINESS,
    ]
    for text in required_text:
        if text not in md_text:
            fail(f"markdown missing required text: {text}")

    print(
        "structured neckline context filter entry/exit audit validation passed "
        f"events={len(events)} detail_rows={len(detail)} summary_rows={len(summary)}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
