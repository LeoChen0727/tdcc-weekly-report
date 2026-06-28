from __future__ import annotations

from pathlib import Path

import pandas as pd

from build_structured_neckline_auto_context_expansion_audit import (
    AUTO_CONTEXT_SCOPE_ID,
    CONTEXT_COLUMNS,
    DETAIL_COLUMNS,
    FAILURE_EXIT_RULE_IDS,
    HISTORY_CONTEXT_CSV,
    HISTORY_DETAIL_CSV,
    HISTORY_SUMMARY_CSV,
    LATEST_CONTEXT_CSV,
    LATEST_DETAIL_CSV,
    LATEST_MD,
    LATEST_SUMMARY_CSV,
    PARAMETER_SET_ID,
    PRODUCTION_READINESS,
    RESEARCH_ID,
    RESEARCH_VARIANT_ID,
    SUMMARY_COLUMNS,
    TARGET_SEGMENT_ID,
)


FORBIDDEN_PRODUCTION_FIELDS = {
    "trade_decision",
    "action_rating",
    "entry_style",
    "position_sizing",
    "decision_score",
    "daily_candidate_decision",
    "buy_signal",
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
        "auto_context_scope_id": AUTO_CONTEXT_SCOPE_ID,
        "production_readiness": PRODUCTION_READINESS,
    }
    for column, expected in constants.items():
        values = set(frame[column].astype(str))
        if values != {expected}:
            fail(f"{label} {column} must be {expected}; got {sorted(values)}")
    if not false_only(frame["approved_for_daily"]):
        fail(f"{label} approved_for_daily must remain false")


def main() -> int:
    detail = read_csv(LATEST_DETAIL_CSV)
    summary = read_csv(LATEST_SUMMARY_CSV)
    context = read_csv(LATEST_CONTEXT_CSV)
    history_detail = read_csv(HISTORY_DETAIL_CSV)
    history_summary = read_csv(HISTORY_SUMMARY_CSV)
    history_context = read_csv(HISTORY_CONTEXT_CSV)
    if detail.empty or summary.empty or context.empty:
        fail("latest outputs must not be empty")
    if len(detail) != len(history_detail):
        fail("detail latest/history row counts differ")
    if len(summary) != len(history_summary):
        fail("summary latest/history row counts differ")
    if len(context) != len(history_context):
        fail("context latest/history row counts differ")
    if not LATEST_MD.exists():
        fail(f"missing markdown output: {LATEST_MD}")

    require_columns(detail, DETAIL_COLUMNS, "detail")
    require_columns(summary, SUMMARY_COLUMNS, "summary")
    require_columns(context, CONTEXT_COLUMNS, "context")
    forbidden = sorted((set(detail.columns) | set(summary.columns) | set(context.columns)) & FORBIDDEN_PRODUCTION_FIELDS)
    if forbidden:
        fail(f"outputs must not emit production decision fields: {forbidden}")
    validate_constants(detail, "detail")
    validate_constants(summary, "summary")
    validate_constants(context, "context")

    expected_detail_rows = 374 * len(FAILURE_EXIT_RULE_IDS)
    if len(detail) != expected_detail_rows:
        fail(f"expected {expected_detail_rows} detail rows; got {len(detail)}")
    if set(detail["failure_exit_rule_id"].astype(str)) != set(FAILURE_EXIT_RULE_IDS):
        fail(f"detail failure_exit_rule_id mismatch: {sorted(set(detail['failure_exit_rule_id'].astype(str)))}")

    event_counts = detail.groupby("failure_exit_rule_id").size().to_dict()
    for rule_id in FAILURE_EXIT_RULE_IDS:
        if int(event_counts.get(rule_id, 0)) != 374:
            fail(f"{rule_id} must have 374 events; got {event_counts.get(rule_id, 0)}")

    target = detail[detail["in_low_position_le60_market_bull"].astype(str).eq("true")]
    target_event_count = target[["stock_id", "signal_date", "retest_entry_date"]].drop_duplicates().shape[0]
    if target_event_count != 95:
        fail(f"expected {TARGET_SEGMENT_ID} to have 95 events; got {target_event_count}")

    valid_contexts = {"bearish", "sideways_or_consolidation", "slow_uptrend", "volatile_mixed", "unknown"}
    contexts = set(detail["auto_pre_signal_context"].astype(str))
    if not contexts <= valid_contexts:
        fail(f"unexpected auto contexts: {sorted(contexts)}")
    if "bearish" not in contexts or "sideways_or_consolidation" not in contexts:
        fail(f"auto context expansion must include bearish and sideways/consolidation contexts; got {sorted(contexts)}")

    names = detail["stock_name"].astype(str)
    bad_names = detail[names.str.contains("\ufffd", regex=False) | names.str.contains("嚙", regex=False)]
    if not bad_names.empty:
        fail(f"stock_name contains replacement/mojibake characters for ids: {sorted(bad_names['stock_id'].astype(str).unique())}")

    required_scopes = {
        "all_retest_entries",
        "all_auto_non_bearish",
        "all_auto_bearish",
        "low_position_le60_market_bull",
        "low_position_le60_market_bull_auto_non_bearish",
        "low_position_le60_market_bull_auto_bearish",
    }
    scopes = set(summary["analysis_scope_id"].astype(str))
    missing_scopes = sorted(required_scopes - scopes)
    if missing_scopes:
        fail(f"summary missing required scopes: {missing_scopes}")

    for scope_id, expected_sample in {
        "all_retest_entries": 374,
        "low_position_le60_market_bull": 95,
    }.items():
        rows = summary[summary["analysis_scope_id"].astype(str).eq(scope_id)]
        if set(rows["failure_exit_rule_id"].astype(str)) != set(FAILURE_EXIT_RULE_IDS):
            fail(f"{scope_id} must include both failure rules")
        sizes = set(pd.to_numeric(rows["sample_size"], errors="coerce").dropna().astype(int))
        if sizes != {expected_sample}:
            fail(f"{scope_id} sample size must be {expected_sample}; got {sorted(sizes)}")

    auto_non_bearish = summary[
        summary["analysis_scope_id"].astype(str).eq("low_position_le60_market_bull_auto_non_bearish")
    ]
    if auto_non_bearish.empty:
        fail("missing low-position bull auto non-bearish scope")
    if pd.to_numeric(auto_non_bearish["sample_size"], errors="coerce").min() <= 23:
        fail("auto non-bearish low-position bull sample must expand beyond the 23-row manual shortlist")

    numeric_columns = [
        "sample_size",
        "unique_stock_count",
        "auto_bearish_count",
        "auto_non_bearish_count",
        "auto_unknown_count",
        "win_count",
        "neutral_count",
        "loss_count",
        "avg_return_pct",
        "median_return_pct",
        "avg_max_close_return_pct",
        "median_max_close_return_pct",
        "avg_min_close_return_pct",
        "median_min_close_return_pct",
    ]
    for column in numeric_columns:
        if pd.to_numeric(summary[column], errors="coerce").isna().any():
            fail(f"summary column must be numeric: {column}")

    md_text = LATEST_MD.read_text(encoding="utf-8", errors="replace")
    required_text = [
        "Auto Context Expansion Audit",
        "auto context window: 90 sessions",
        "intraday high/low trigger is not used",
        "production impact: `none`",
        "No production model condition, scoring, ranking, PDF logic, or baseline was changed.",
        PRODUCTION_READINESS,
    ]
    for text in required_text:
        if text not in md_text:
            fail(f"markdown missing required text: {text}")

    print(
        "structured neckline auto context expansion audit validation passed "
        f"detail_rows={len(detail)} summary_rows={len(summary)} context_rows={len(context)}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
