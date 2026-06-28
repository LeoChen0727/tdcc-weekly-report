from __future__ import annotations

from pathlib import Path

import pandas as pd

from build_structured_neckline_selected_exit_loss_diagnostics import (
    DIAGNOSTIC_SCOPE_ID,
    EVENT_COLUMNS,
    FLAG_COLUMNS,
    HISTORY_EVENT_CSV,
    HISTORY_FLAG_CSV,
    HISTORY_SUMMARY_CSV,
    LATEST_EVENT_CSV,
    LATEST_FLAG_CSV,
    LATEST_MD,
    LATEST_SUMMARY_CSV,
    PARAMETER_SET_ID,
    PRODUCTION_READINESS,
    RESEARCH_ID,
    RESEARCH_VARIANT_ID,
    SELECTED_EXIT_RULE_COMPARISON_ID,
    SUMMARY_COLUMNS,
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
        "diagnostic_scope_id": DIAGNOSTIC_SCOPE_ID,
        "selected_exit_rule_comparison_id": SELECTED_EXIT_RULE_COMPARISON_ID,
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
    summary = read_csv(LATEST_SUMMARY_CSV)
    flags = read_csv(LATEST_FLAG_CSV)
    history_events = read_csv(HISTORY_EVENT_CSV)
    history_summary = read_csv(HISTORY_SUMMARY_CSV)
    history_flags = read_csv(HISTORY_FLAG_CSV)
    if events.empty or summary.empty or flags.empty:
        fail("latest outputs must not be empty")
    if len(events) != len(history_events):
        fail("event latest/history row counts differ")
    if len(summary) != len(history_summary):
        fail("summary latest/history row counts differ")
    if len(flags) != len(history_flags):
        fail("flag latest/history row counts differ")
    if not LATEST_MD.exists():
        fail(f"missing markdown output: {LATEST_MD}")

    require_columns(events, EVENT_COLUMNS, "events")
    require_columns(summary, SUMMARY_COLUMNS, "summary")
    require_columns(flags, FLAG_COLUMNS, "flags")
    forbidden = sorted((set(events.columns) | set(summary.columns) | set(flags.columns)) & FORBIDDEN_PRODUCTION_FIELDS)
    if forbidden:
        fail(f"outputs must not emit production decision fields: {forbidden}")
    validate_constants(events, "events")
    validate_constants(summary, "summary")
    validate_constants(flags, "flags")

    if len(events) != 23:
        fail(f"expected 23 selected-rule diagnostic events; got {len(events)}")
    bad_names = events[events["stock_name"].astype(str).str.contains("�", regex=False)]
    if not bad_names.empty:
        fail(f"stock_name contains replacement characters for ids: {sorted(bad_names['stock_id'].astype(str).unique())}")
    if "bearish" in set(events["visual_pre_signal_context"].astype(str)):
        fail("events must not include bearish pre-signal context rows")
    outcome_counts = events["selected_outcome"].value_counts().to_dict()
    if outcome_counts.get("loss") != 5:
        fail(f"expected five selected-rule losses; got {outcome_counts}")
    if outcome_counts.get("win") != 8 or outcome_counts.get("neutral") != 10:
        fail(f"expected selected-rule win/neutral counts 8/10; got {outcome_counts}")

    expected_cohorts = {
        "selected_rule_loss",
        "selected_rule_success_or_neutral",
        "selected_rule_win",
        "selected_rule_neutral",
    }
    if set(summary["diagnostic_cohort"].astype(str)) != expected_cohorts:
        fail(f"summary cohort mismatch: {sorted(set(summary['diagnostic_cohort'].astype(str)))}")
    loss_flags = flags[pd.to_numeric(flags["loss_event_count"], errors="coerce").fillna(0).gt(0)]
    if loss_flags.empty:
        fail("flags must include at least one loss diagnostic flag")
    if "large_adverse_move_mae_below_minus10pct" not in set(flags["diagnostic_flag"].astype(str)):
        fail("expected large adverse move diagnostic flag")

    numeric_columns = [
        "avg_selected_return_pct",
        "median_selected_return_pct",
        "avg_selected_mfe_pct",
        "median_selected_mfe_pct",
        "avg_selected_mae_pct",
        "median_selected_mae_pct",
        "median_visual_pre_signal_return_pct",
        "median_visual_pre_signal_range_pct",
        "median_base_width_pct",
        "median_low_position_120_pct",
    ]
    for column in numeric_columns:
        if pd.to_numeric(summary[column], errors="coerce").isna().any():
            fail(f"summary column must be numeric: {column}")

    md_text = LATEST_MD.read_text(encoding="utf-8", errors="replace")
    required_text = [
        "Cohort Summary",
        "Loss Rows",
        "Loss Flag Counts",
        "candidate failure features only",
        "production impact: `none`",
        PRODUCTION_READINESS,
    ]
    for text in required_text:
        if text not in md_text:
            fail(f"markdown missing required text: {text}")

    print(
        "structured neckline selected exit loss diagnostics validation passed "
        f"events={len(events)} summary_rows={len(summary)} flags={len(flags)}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
