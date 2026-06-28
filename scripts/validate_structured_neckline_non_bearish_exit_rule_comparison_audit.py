from __future__ import annotations

from pathlib import Path

import pandas as pd

from build_structured_neckline_non_bearish_exit_rule_comparison_audit import (
    CLOSE_NEUTRAL_RULE_ID,
    COMPARISON_COLUMNS,
    COMPARISON_SCOPE_ID,
    HISTORY_COMPARISON_CSV,
    HISTORY_SUMMARY_CSV,
    INTRADAY_RULE_ID,
    LATEST_COMPARISON_CSV,
    LATEST_MD,
    LATEST_SUMMARY_CSV,
    PARAMETER_SET_ID,
    PRODUCTION_READINESS,
    RESEARCH_ID,
    RESEARCH_VARIANT_ID,
    RESEARCH_SELECTION_REASON,
    SELECTED_EXIT_RULE_COMPARISON_ID,
    SUMMARY_COLUMNS,
)
from build_structured_neckline_context_filter_entry_exit_audit import (
    EVENT_FAMILY_ID,
    PASS_COHORT_ID,
    LATEST_DETAIL_CSV as CONTEXT_FILTER_DETAIL_CSV,
    TARGET_SEGMENT_ID,
)
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
        "comparison_scope_id": COMPARISON_SCOPE_ID,
        "production_readiness": PRODUCTION_READINESS,
    }
    for column, expected in constants.items():
        values = set(frame[column].astype(str))
        if values != {expected}:
            fail(f"{label} {column} must be {expected}; got {sorted(values)}")
    if not false_only(frame["approved_for_daily"]):
        fail(f"{label} approved_for_daily must remain false")


def expected_source_event_count() -> int:
    source = read_csv(CONTEXT_FILTER_DETAIL_CSV)
    rows = source[
        source["cohort_id"].astype(str).eq(PASS_COHORT_ID)
        & source["visual_context_filter_result"].astype(str).eq("pass")
        & ~source["visual_pre_signal_context"].astype(str).eq("bearish")
        & source["stop_rule_id"].astype(str).eq("signal_low_stop")
    ].copy()
    keys = rows[["stock_id", "signal_date", "retest_entry_date"]].drop_duplicates()
    return len(keys)


def main() -> int:
    comparison = read_csv(LATEST_COMPARISON_CSV)
    summary = read_csv(LATEST_SUMMARY_CSV)
    history_comparison = read_csv(HISTORY_COMPARISON_CSV)
    history_summary = read_csv(HISTORY_SUMMARY_CSV)
    if comparison.empty or summary.empty:
        fail("latest outputs must not be empty")
    if len(comparison) != len(history_comparison):
        fail("comparison latest/history row counts differ")
    if len(summary) != len(history_summary):
        fail("summary latest/history row counts differ")
    if not LATEST_MD.exists():
        fail(f"missing markdown output: {LATEST_MD}")

    require_columns(comparison, COMPARISON_COLUMNS, "comparison")
    require_columns(summary, SUMMARY_COLUMNS, "summary")
    forbidden = sorted((set(comparison.columns) | set(summary.columns)) & FORBIDDEN_PRODUCTION_FIELDS)
    if forbidden:
        fail(f"outputs must not emit production decision fields: {forbidden}")
    validate_constants(comparison, "comparison")
    validate_constants(summary, "summary")

    if set(summary["exit_rule_comparison_id"].astype(str)) != {INTRADAY_RULE_ID, CLOSE_NEUTRAL_RULE_ID}:
        fail(f"summary must contain exactly the two target comparison rows: {sorted(summary['exit_rule_comparison_id'].astype(str))}")
    selected = summary[summary["selected_for_next_research_iteration"].astype(str).str.lower().eq("true")]
    if len(selected) != 1:
        fail("summary must select exactly one next research iteration rule")
    if selected["exit_rule_comparison_id"].iloc[0] != SELECTED_EXIT_RULE_COMPARISON_ID:
        fail(f"selected rule must be {SELECTED_EXIT_RULE_COMPARISON_ID}")
    if set(selected["research_selection_reason"].astype(str)) != {RESEARCH_SELECTION_REASON}:
        fail("selected rule must preserve the explicit research selection reason")
    if set(comparison["event_family_id"].astype(str)) != {EVENT_FAMILY_ID}:
        fail("comparison event_family_id mismatch")
    if set(comparison["segment_id"].astype(str)) != {TARGET_SEGMENT_ID}:
        fail("comparison segment_id mismatch")
    if "bearish" in set(comparison["visual_pre_signal_context"].astype(str)):
        fail("comparison must not include bearish pre-signal context rows")
    if len(comparison) != expected_source_event_count():
        fail("comparison row count must match non-bearish source event count")

    transitions = set(comparison["outcome_transition"].astype(str))
    if not transitions:
        fail("outcome transitions must not be empty")
    if "win_to_neutral" not in transitions:
        fail("expected at least one win_to_neutral transition for the two rule comparison")
    if "loss_to_loss" not in transitions:
        fail("expected at least one loss_to_loss transition for downside review")

    numeric_columns = [
        "pure_win_rate_pct",
        "neutral_inclusive_success_rate_pct",
        "positive_return_rate_pct",
        "avg_return_pct",
        "median_return_pct",
        "avg_mfe_pct",
        "avg_mae_pct",
    ]
    for column in numeric_columns:
        if pd.to_numeric(summary[column], errors="coerce").isna().any():
            fail(f"summary column must be numeric: {column}")

    md_text = LATEST_MD.read_text(encoding="utf-8", errors="replace")
    required_text = [
        "Research Selection",
        SELECTED_EXIT_RULE_COMPARISON_ID,
        RESEARCH_SELECTION_REASON,
        "Rule Summary",
        "Outcome Transition Counts",
        "Rows To Review",
        "production impact: `none`",
        PRODUCTION_READINESS,
    ]
    for text in required_text:
        if text not in md_text:
            fail(f"markdown missing required text: {text}")

    print(
        "structured neckline non-bearish exit rule comparison validation passed "
        f"comparison_rows={len(comparison)} summary_rows={len(summary)}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
