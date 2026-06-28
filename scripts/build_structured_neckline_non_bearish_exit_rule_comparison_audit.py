from __future__ import annotations

from datetime import datetime
from pathlib import Path
from typing import Any
from zoneinfo import ZoneInfo
import math

import pandas as pd

from build_structured_neckline_context_filter_entry_exit_audit import (
    EVENT_FAMILY_ID,
    LATEST_DETAIL_CSV as CONTEXT_FILTER_DETAIL_CSV,
    PARAMETER_SET_ID as CONTEXT_FILTER_PARAMETER_SET_ID,
    PASS_COHORT_ID,
    PRODUCTION_READINESS,
    RESEARCH_ID as CONTEXT_FILTER_RESEARCH_ID,
    RESEARCH_VARIANT_ID,
    TARGET_SEGMENT_ID,
    metric_text,
    safe_str,
)
from build_structured_neckline_retest_review_packet import (
    FORBIDDEN_PRODUCTION_FIELDS,
    RESEARCH_HISTORY_DIR,
    RESEARCH_LATEST_DIR,
)


RESEARCH_ID = "structured_neckline_non_bearish_exit_rule_comparison_audit"
PARAMETER_SET_ID = "structured_neckline_non_bearish_exit_rule_comparison_audit_20260629"
COMPARISON_SCOPE_ID = "visual_context_non_bearish_signal_low_stop"
STOP_RULE_ID = "signal_low_stop"

INTRADAY_RULE_ID = "tp10_intraday_touch"
INTRADAY_EXIT_RULE_ID = "tp10_intraday_or_fixed_20d_close"
INTRADAY_OUTCOME_RULE_ID = "tp10_intraday_required_else_loss"

CLOSE_NEUTRAL_RULE_ID = "tp10_close_with_5pct_pullback_neutral"
CLOSE_NEUTRAL_EXIT_RULE_ID = "tp10_close_or_neutral_after_5pct_close_20d"
CLOSE_NEUTRAL_OUTCOME_RULE_ID = "tp10_close_win_5pct_pullback_neutral"

LATEST_COMPARISON_CSV = RESEARCH_LATEST_DIR / "structured_neckline_non_bearish_exit_rule_comparison_latest.csv"
LATEST_SUMMARY_CSV = RESEARCH_LATEST_DIR / "structured_neckline_non_bearish_exit_rule_comparison_summary_latest.csv"
LATEST_MD = RESEARCH_LATEST_DIR / "structured_neckline_non_bearish_exit_rule_comparison_latest.md"
HISTORY_COMPARISON_CSV = RESEARCH_HISTORY_DIR / "structured_neckline_non_bearish_exit_rule_comparison.csv"
HISTORY_SUMMARY_CSV = RESEARCH_HISTORY_DIR / "structured_neckline_non_bearish_exit_rule_comparison_summary.csv"

EVENT_KEY_COLUMNS = ["stock_id", "signal_date", "retest_entry_date"]

COMPARISON_COLUMNS = [
    "research_id",
    "source_research_id",
    "source_parameter_set_id",
    "research_variant_id",
    "parameter_set_id",
    "advisory_status",
    "comparison_scope_id",
    "event_family_id",
    "segment_id",
    "stock_id",
    "stock_name",
    "signal_date",
    "retest_date",
    "retest_attack_date",
    "retest_entry_date",
    "visual_pre_signal_context",
    "entry_price",
    "intraday_outcome",
    "intraday_exit_date",
    "intraday_exit_reason",
    "intraday_return_pct",
    "intraday_mfe_pct",
    "intraday_mae_pct",
    "close_neutral_outcome",
    "close_neutral_exit_date",
    "close_neutral_exit_reason",
    "close_neutral_return_pct",
    "close_neutral_mfe_pct",
    "close_neutral_mae_pct",
    "outcome_transition",
    "interpretation_bucket",
    "approved_for_daily",
    "production_readiness",
    "generated_at",
]

SUMMARY_COLUMNS = [
    "research_id",
    "research_variant_id",
    "parameter_set_id",
    "advisory_status",
    "comparison_scope_id",
    "exit_rule_comparison_id",
    "exit_rule_id",
    "outcome_rule_id",
    "sample_size",
    "unique_stock_count",
    "win_count",
    "neutral_count",
    "loss_count",
    "pure_win_rate_pct",
    "neutral_inclusive_success_rate_pct",
    "positive_return_rate_pct",
    "avg_return_pct",
    "median_return_pct",
    "avg_mfe_pct",
    "avg_mae_pct",
    "approved_for_daily",
    "production_readiness",
    "generated_at",
]


def now_text() -> str:
    return datetime.now(ZoneInfo("Asia/Taipei")).strftime("%Y-%m-%d %H:%M:%S Asia/Taipei")


def read_csv(path: Path) -> pd.DataFrame:
    if not path.exists():
        raise SystemExit(f"ERROR: missing required input: {path}")
    return pd.read_csv(path, dtype=str, keep_default_na=False)


def to_float(value: Any) -> float:
    try:
        return float(value)
    except (TypeError, ValueError):
        return math.nan


def event_key(row: pd.Series) -> str:
    return "|".join(str(row.get(column, "")) for column in EVENT_KEY_COLUMNS)


def load_target_rows() -> pd.DataFrame:
    source = read_csv(CONTEXT_FILTER_DETAIL_CSV)
    required = {
        "research_id",
        "parameter_set_id",
        "research_variant_id",
        "advisory_status",
        "cohort_id",
        "event_family_id",
        "segment_id",
        "stock_id",
        "stock_name",
        "signal_date",
        "retest_date",
        "retest_attack_date",
        "retest_entry_date",
        "visual_pre_signal_context",
        "visual_context_filter_result",
        "stop_rule_id",
        "exit_rule_id",
        "outcome_rule_id",
        "entry_price",
        "exit_date",
        "exit_price",
        "exit_reason",
        "holding_days",
        "return_pct",
        "mfe_pct",
        "mae_pct",
        "outcome_result",
        "positive_return_result",
        "approved_for_daily",
        "production_readiness",
    }
    missing = sorted(required - set(source.columns))
    if missing:
        raise SystemExit(f"ERROR: context filter detail missing columns: {missing}")
    forbidden = sorted(set(source.columns) & FORBIDDEN_PRODUCTION_FIELDS)
    if forbidden:
        raise SystemExit(f"ERROR: context filter detail contains production fields: {forbidden}")
    rows = source[
        source["research_id"].astype(str).eq(CONTEXT_FILTER_RESEARCH_ID)
        & source["parameter_set_id"].astype(str).eq(CONTEXT_FILTER_PARAMETER_SET_ID)
        & source["research_variant_id"].astype(str).eq(RESEARCH_VARIANT_ID)
        & source["advisory_status"].astype(str).eq(RESEARCH_VARIANT_ID)
        & source["cohort_id"].astype(str).eq(PASS_COHORT_ID)
        & source["visual_context_filter_result"].astype(str).eq("pass")
        & ~source["visual_pre_signal_context"].astype(str).eq("bearish")
        & source["stop_rule_id"].astype(str).eq(STOP_RULE_ID)
    ].copy()
    if rows.empty:
        raise SystemExit("ERROR: no non-bearish signal-low-stop detail rows found")
    return rows


def select_rule(rows: pd.DataFrame, exit_rule_id: str, outcome_rule_id: str) -> pd.DataFrame:
    rule_rows = rows[
        rows["exit_rule_id"].astype(str).eq(exit_rule_id)
        & rows["outcome_rule_id"].astype(str).eq(outcome_rule_id)
    ].copy()
    if rule_rows.empty:
        raise SystemExit(f"ERROR: missing comparison rule rows: {exit_rule_id} / {outcome_rule_id}")
    rule_rows["_key"] = rule_rows.apply(event_key, axis=1)
    duplicated = rule_rows["_key"].duplicated(keep=False)
    if duplicated.any():
        duplicate_keys = sorted(set(rule_rows.loc[duplicated, "_key"].astype(str)))
        raise SystemExit(f"ERROR: duplicate event keys for rule {exit_rule_id}: {duplicate_keys[:5]}")
    return rule_rows


def interpretation_bucket(intraday_outcome: str, close_neutral_outcome: str) -> str:
    if intraday_outcome == "win" and close_neutral_outcome == "win":
        return "both_rules_win"
    if intraday_outcome == "win" and close_neutral_outcome == "neutral":
        return "intraday_touch_win_close_rule_neutral"
    if intraday_outcome == "win" and close_neutral_outcome == "loss":
        return "intraday_touch_win_close_rule_loss"
    if intraday_outcome == "loss" and close_neutral_outcome == "neutral":
        return "intraday_loss_close_rule_neutral"
    if intraday_outcome == "loss" and close_neutral_outcome == "win":
        return "intraday_loss_close_rule_win"
    if intraday_outcome == "loss" and close_neutral_outcome == "loss":
        return "both_rules_loss"
    return "mixed_or_unexpected"


def build_comparison(rows: pd.DataFrame, generated_at: str) -> pd.DataFrame:
    intraday = select_rule(rows, INTRADAY_EXIT_RULE_ID, INTRADAY_OUTCOME_RULE_ID).set_index("_key")
    close_neutral = select_rule(rows, CLOSE_NEUTRAL_EXIT_RULE_ID, CLOSE_NEUTRAL_OUTCOME_RULE_ID).set_index("_key")
    if set(intraday.index) != set(close_neutral.index):
        raise SystemExit("ERROR: comparison rule event keys do not match")
    comparison_rows: list[dict[str, str]] = []
    for key in sorted(intraday.index):
        left = intraday.loc[key]
        right = close_neutral.loc[key]
        transition = f"{safe_str(left.get('outcome_result'))}_to_{safe_str(right.get('outcome_result'))}"
        bucket = interpretation_bucket(safe_str(left.get("outcome_result")), safe_str(right.get("outcome_result")))
        comparison_rows.append(
            {
                "research_id": RESEARCH_ID,
                "source_research_id": CONTEXT_FILTER_RESEARCH_ID,
                "source_parameter_set_id": CONTEXT_FILTER_PARAMETER_SET_ID,
                "research_variant_id": RESEARCH_VARIANT_ID,
                "parameter_set_id": PARAMETER_SET_ID,
                "advisory_status": RESEARCH_VARIANT_ID,
                "comparison_scope_id": COMPARISON_SCOPE_ID,
                "event_family_id": EVENT_FAMILY_ID,
                "segment_id": TARGET_SEGMENT_ID,
                "stock_id": safe_str(left.get("stock_id")),
                "stock_name": safe_str(left.get("stock_name")),
                "signal_date": safe_str(left.get("signal_date")),
                "retest_date": safe_str(left.get("retest_date")),
                "retest_attack_date": safe_str(left.get("retest_attack_date")),
                "retest_entry_date": safe_str(left.get("retest_entry_date")),
                "visual_pre_signal_context": safe_str(left.get("visual_pre_signal_context")),
                "entry_price": safe_str(left.get("entry_price")),
                "intraday_outcome": safe_str(left.get("outcome_result")),
                "intraday_exit_date": safe_str(left.get("exit_date")),
                "intraday_exit_reason": safe_str(left.get("exit_reason")),
                "intraday_return_pct": metric_text(to_float(left.get("return_pct"))),
                "intraday_mfe_pct": metric_text(to_float(left.get("mfe_pct"))),
                "intraday_mae_pct": metric_text(to_float(left.get("mae_pct"))),
                "close_neutral_outcome": safe_str(right.get("outcome_result")),
                "close_neutral_exit_date": safe_str(right.get("exit_date")),
                "close_neutral_exit_reason": safe_str(right.get("exit_reason")),
                "close_neutral_return_pct": metric_text(to_float(right.get("return_pct"))),
                "close_neutral_mfe_pct": metric_text(to_float(right.get("mfe_pct"))),
                "close_neutral_mae_pct": metric_text(to_float(right.get("mae_pct"))),
                "outcome_transition": transition,
                "interpretation_bucket": bucket,
                "approved_for_daily": "false",
                "production_readiness": PRODUCTION_READINESS,
                "generated_at": generated_at,
            }
        )
    comparison = pd.DataFrame(comparison_rows)
    for column in COMPARISON_COLUMNS:
        if column not in comparison.columns:
            comparison[column] = ""
    return comparison[COMPARISON_COLUMNS]


def summary_for(rule_rows: pd.DataFrame, comparison_id: str, exit_rule_id: str, outcome_rule_id: str, generated_at: str) -> dict[str, str]:
    outcome = rule_rows["outcome_result"].astype(str)
    wins = int(outcome.eq("win").sum())
    neutral = int(outcome.eq("neutral").sum())
    losses = int(outcome.eq("loss").sum())
    evaluated = wins + neutral + losses
    mature = wins + losses
    returns = pd.to_numeric(rule_rows["return_pct"], errors="coerce").dropna()
    mfe = pd.to_numeric(rule_rows["mfe_pct"], errors="coerce").dropna()
    mae = pd.to_numeric(rule_rows["mae_pct"], errors="coerce").dropna()
    positives = rule_rows["positive_return_result"].astype(str).eq("positive")
    return {
        "research_id": RESEARCH_ID,
        "research_variant_id": RESEARCH_VARIANT_ID,
        "parameter_set_id": PARAMETER_SET_ID,
        "advisory_status": RESEARCH_VARIANT_ID,
        "comparison_scope_id": COMPARISON_SCOPE_ID,
        "exit_rule_comparison_id": comparison_id,
        "exit_rule_id": exit_rule_id,
        "outcome_rule_id": outcome_rule_id,
        "sample_size": str(len(rule_rows)),
        "unique_stock_count": str(int(rule_rows["stock_id"].nunique())),
        "win_count": str(wins),
        "neutral_count": str(neutral),
        "loss_count": str(losses),
        "pure_win_rate_pct": metric_text(wins / mature * 100.0 if mature else math.nan),
        "neutral_inclusive_success_rate_pct": metric_text((wins + neutral) / evaluated * 100.0 if evaluated else math.nan),
        "positive_return_rate_pct": metric_text(float(positives.mean()) * 100.0 if len(positives) else math.nan),
        "avg_return_pct": metric_text(float(returns.mean()) if len(returns) else math.nan),
        "median_return_pct": metric_text(float(returns.median()) if len(returns) else math.nan),
        "avg_mfe_pct": metric_text(float(mfe.mean()) if len(mfe) else math.nan),
        "avg_mae_pct": metric_text(float(mae.mean()) if len(mae) else math.nan),
        "approved_for_daily": "false",
        "production_readiness": PRODUCTION_READINESS,
        "generated_at": generated_at,
    }


def build_summary(rows: pd.DataFrame, generated_at: str) -> pd.DataFrame:
    intraday = select_rule(rows, INTRADAY_EXIT_RULE_ID, INTRADAY_OUTCOME_RULE_ID)
    close_neutral = select_rule(rows, CLOSE_NEUTRAL_EXIT_RULE_ID, CLOSE_NEUTRAL_OUTCOME_RULE_ID)
    summary = pd.DataFrame(
        [
            summary_for(intraday, INTRADAY_RULE_ID, INTRADAY_EXIT_RULE_ID, INTRADAY_OUTCOME_RULE_ID, generated_at),
            summary_for(close_neutral, CLOSE_NEUTRAL_RULE_ID, CLOSE_NEUTRAL_EXIT_RULE_ID, CLOSE_NEUTRAL_OUTCOME_RULE_ID, generated_at),
        ]
    )
    for column in SUMMARY_COLUMNS:
        if column not in summary.columns:
            summary[column] = ""
    return summary[SUMMARY_COLUMNS]


def markdown_table(df: pd.DataFrame, columns: list[str], limit: int = 80) -> list[str]:
    if df.empty:
        return ["_No rows._"]
    lines = ["| " + " | ".join(columns) + " |", "| " + " | ".join(["---"] * len(columns)) + " |"]
    for _, row in df.loc[:, columns].head(limit).iterrows():
        lines.append("| " + " | ".join(safe_str(row.get(column)) for column in columns) + " |")
    return lines


def write_csv(df: pd.DataFrame, path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(path, index=False, encoding="utf-8-sig")


def write_markdown(comparison: pd.DataFrame, summary: pd.DataFrame, generated_at: str) -> None:
    transitions = (
        comparison.groupby(["outcome_transition", "interpretation_bucket"], dropna=False)
        .agg(events=("stock_id", "size"), unique_stocks=("stock_id", "nunique"))
        .reset_index()
        .sort_values(["events", "outcome_transition"], ascending=[False, True])
    )
    review_rows = comparison[
        comparison["interpretation_bucket"].isin(
            [
                "intraday_touch_win_close_rule_neutral",
                "intraday_touch_win_close_rule_loss",
                "both_rules_loss",
            ]
        )
    ].copy()
    review_rows["_sort"] = review_rows["interpretation_bucket"].map(
        {
            "intraday_touch_win_close_rule_loss": 0,
            "intraday_touch_win_close_rule_neutral": 1,
            "both_rules_loss": 2,
        }
    )
    review_rows = review_rows.sort_values(["_sort", "signal_date", "stock_id"]).drop(columns=["_sort"])
    lines = [
        "# Structured Neckline Non-Bearish Exit Rule Comparison",
        "",
        f"- generated_at: `{generated_at}`",
        f"- research_id: `{RESEARCH_ID}`",
        f"- source_research_id: `{CONTEXT_FILTER_RESEARCH_ID}`",
        f"- comparison_scope_id: `{COMPARISON_SCOPE_ID}`",
        f"- sample_size: `{len(comparison)}`",
        f"- stop_rule_id: `{STOP_RULE_ID}`",
        f"- advisory_status: `{RESEARCH_VARIANT_ID}`",
        f"- production_readiness: `{PRODUCTION_READINESS}`",
        "- production impact: `none`; this audit does not update production model conditions, scoring, ranking, PDF logic, or baseline.",
        "",
        "## Why This Exists",
        "",
        "- The previous audit supported excluding bearish pre-signal context first.",
        "- This audit compares only the remaining non-bearish events.",
        "- It compares two sell/outcome definitions on the same entry event set.",
        "- Pure win rate and neutral-inclusive success rate remain separate metrics.",
        "",
        "## Rule Summary",
        "",
        *markdown_table(
            summary,
            [
                "exit_rule_comparison_id",
                "sample_size",
                "win_count",
                "neutral_count",
                "loss_count",
                "pure_win_rate_pct",
                "neutral_inclusive_success_rate_pct",
                "positive_return_rate_pct",
                "avg_return_pct",
                "median_return_pct",
                "avg_mae_pct",
            ],
        ),
        "",
        "## Outcome Transition Counts",
        "",
        *markdown_table(transitions, list(transitions.columns), limit=40),
        "",
        "## Rows To Review",
        "",
        "- `intraday_touch_win_close_rule_loss`: the stock touched +10% intraday, but the close-based rule did not produce a win or neutral.",
        "- `intraday_touch_win_close_rule_neutral`: the stock touched +10% intraday, but the close-based rule treats the trade as an escape/neutral.",
        "- `both_rules_loss`: both candidate sell definitions fail; these are the highest-priority chart review rows.",
        "",
        *markdown_table(
            review_rows,
            [
                "stock_id",
                "stock_name",
                "signal_date",
                "retest_entry_date",
                "visual_pre_signal_context",
                "entry_price",
                "intraday_outcome",
                "intraday_return_pct",
                "close_neutral_outcome",
                "close_neutral_return_pct",
                "outcome_transition",
                "interpretation_bucket",
            ],
            limit=80,
        ),
        "",
        "## Boundary Notes",
        "",
        "- This is research/backtest advisory-only output.",
        "- All rows remain `approved_for_daily=false`, `warning_research_variant_only`, and `not_production_ready_research_only`.",
        "- No production model condition, scoring, ranking, PDF logic, or baseline was changed.",
    ]
    LATEST_MD.parent.mkdir(parents=True, exist_ok=True)
    LATEST_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    generated_at = now_text()
    rows = load_target_rows()
    comparison = build_comparison(rows, generated_at)
    summary = build_summary(rows, generated_at)
    write_csv(comparison, LATEST_COMPARISON_CSV)
    write_csv(summary, LATEST_SUMMARY_CSV)
    write_csv(comparison, HISTORY_COMPARISON_CSV)
    write_csv(summary, HISTORY_SUMMARY_CSV)
    write_markdown(comparison, summary, generated_at)
    print(f"Saved: {LATEST_COMPARISON_CSV} rows={len(comparison)}")
    print(f"Saved: {LATEST_SUMMARY_CSV} rows={len(summary)}")
    print(f"Saved: {LATEST_MD}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
