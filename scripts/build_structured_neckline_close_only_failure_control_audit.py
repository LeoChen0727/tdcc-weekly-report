from __future__ import annotations

from datetime import datetime
from pathlib import Path
from typing import Any
from zoneinfo import ZoneInfo
import math

import pandas as pd

from build_structured_neckline_non_bearish_exit_rule_comparison_audit import (
    CLOSE_NEUTRAL_RULE_ID,
    COMPARISON_SCOPE_ID,
    LATEST_COMPARISON_CSV,
    PARAMETER_SET_ID as COMPARISON_PARAMETER_SET_ID,
    RESEARCH_ID as COMPARISON_RESEARCH_ID,
    RESEARCH_SELECTION_REASON,
    RESEARCH_VARIANT_ID,
    SELECTED_EXIT_RULE_COMPARISON_ID,
)
from build_structured_neckline_retest_entry_exit_grid import (
    EVENT_FAMILY_ID,
    PRODUCTION_READINESS,
    index_for_date,
    metric_text,
    normalize_date,
    read_price_file,
    safe_float,
    safe_str,
)
from build_structured_neckline_selected_exit_loss_diagnostics import load_stock_name_lookup


ROOT = Path(__file__).resolve().parents[1]
RESEARCH_LATEST_DIR = ROOT / "output" / "latest" / "research_backtest"
RESEARCH_HISTORY_DIR = ROOT / "output" / "history" / "research"

RESEARCH_ID = "structured_neckline_close_only_failure_control_audit"
PARAMETER_SET_ID = "structured_neckline_close_only_failure_control_audit_20260629"
FAILURE_CONTROL_SCOPE_ID = "selected_close_based_exit_close_only_failure_control"

LATEST_DETAIL_CSV = RESEARCH_LATEST_DIR / "structured_neckline_close_only_failure_control_audit_latest.csv"
LATEST_SUMMARY_CSV = RESEARCH_LATEST_DIR / "structured_neckline_close_only_failure_control_audit_summary_latest.csv"
LATEST_MD = RESEARCH_LATEST_DIR / "structured_neckline_close_only_failure_control_audit_latest.md"
HISTORY_DETAIL_CSV = RESEARCH_HISTORY_DIR / "structured_neckline_close_only_failure_control_audit.csv"
HISTORY_SUMMARY_CSV = RESEARCH_HISTORY_DIR / "structured_neckline_close_only_failure_control_audit_summary.csv"

BASE_CLOSE_ONLY_RULE_ID = "close_only_no_negative_stop"
FAILURE_CONTROL_RULES: list[tuple[str, float | None]] = [
    (BASE_CLOSE_ONLY_RULE_ID, None),
    ("close_only_loss_stop_minus5pct", -5.0),
    ("close_only_loss_stop_minus8pct", -8.0),
    ("close_only_loss_stop_minus10pct", -10.0),
]

EVENT_KEY_COLUMNS = ["stock_id", "signal_date", "retest_entry_date"]

DETAIL_COLUMNS = [
    "research_id",
    "source_comparison_research_id",
    "source_comparison_parameter_set_id",
    "research_variant_id",
    "parameter_set_id",
    "advisory_status",
    "failure_control_scope_id",
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
    "selected_exit_rule_comparison_id",
    "research_selection_reason",
    "failure_control_rule_id",
    "close_negative_stop_threshold_pct",
    "entry_price",
    "exit_date",
    "exit_price",
    "holding_days",
    "return_pct",
    "max_close_return_pct",
    "min_close_return_pct",
    "outcome_result",
    "exit_reason",
    "source_selected_outcome",
    "source_selected_return_pct",
    "source_selected_exit_date",
    "source_selected_exit_reason",
    "outcome_transition_from_source",
    "approved_for_daily",
    "production_readiness",
    "generated_at",
]

SUMMARY_COLUMNS = [
    "research_id",
    "research_variant_id",
    "parameter_set_id",
    "advisory_status",
    "failure_control_scope_id",
    "selected_exit_rule_comparison_id",
    "failure_control_rule_id",
    "close_negative_stop_threshold_pct",
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
    "avg_max_close_return_pct",
    "median_max_close_return_pct",
    "avg_min_close_return_pct",
    "median_min_close_return_pct",
    "changed_from_source_count",
    "source_loss_to_non_loss_count",
    "source_non_loss_to_loss_count",
    "approved_for_daily",
    "production_readiness",
    "generated_at",
]


def now_text() -> str:
    return datetime.now(ZoneInfo("Asia/Taipei")).strftime("%Y-%m-%d %H:%M:%S Asia/Taipei")


def read_csv(path: Path) -> pd.DataFrame:
    if not path.exists():
        raise SystemExit(f"ERROR: missing required input: {path}")
    return pd.read_csv(path, dtype=str, keep_default_na=False, encoding="utf-8-sig")


def to_float(value: Any) -> float:
    try:
        return float(value)
    except (TypeError, ValueError):
        return math.nan


def event_key(row: pd.Series) -> str:
    return "|".join(str(row.get(column, "")) for column in EVENT_KEY_COLUMNS)


def load_selected_events() -> pd.DataFrame:
    source = read_csv(LATEST_COMPARISON_CSV)
    required = {
        "research_id",
        "parameter_set_id",
        "research_variant_id",
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
        "close_neutral_outcome",
        "close_neutral_exit_date",
        "close_neutral_exit_reason",
        "close_neutral_return_pct",
        "production_readiness",
        "approved_for_daily",
    }
    missing = sorted(required - set(source.columns))
    if missing:
        raise SystemExit(f"ERROR: comparison output missing columns: {missing}")
    rows = source[
        source["research_id"].astype(str).eq(COMPARISON_RESEARCH_ID)
        & source["parameter_set_id"].astype(str).eq(COMPARISON_PARAMETER_SET_ID)
        & source["research_variant_id"].astype(str).eq(RESEARCH_VARIANT_ID)
        & source["advisory_status"].astype(str).eq(RESEARCH_VARIANT_ID)
        & source["comparison_scope_id"].astype(str).eq(COMPARISON_SCOPE_ID)
        & source["event_family_id"].astype(str).eq(EVENT_FAMILY_ID)
        & source["production_readiness"].astype(str).eq(PRODUCTION_READINESS)
        & source["approved_for_daily"].astype(str).str.lower().eq("false")
        & ~source["visual_pre_signal_context"].astype(str).eq("bearish")
    ].copy()
    if rows.empty:
        raise SystemExit("ERROR: selected comparison output has no non-bearish rows")
    rows["_key"] = rows.apply(event_key, axis=1)
    if rows["_key"].duplicated().any():
        duplicate_keys = sorted(set(rows.loc[rows["_key"].duplicated(keep=False), "_key"].astype(str)))
        raise SystemExit(f"ERROR: duplicate selected comparison event keys: {duplicate_keys[:5]}")
    return rows.sort_values(["signal_date", "stock_id", "retest_entry_date"]).reset_index(drop=True)


def close_return(close_price: float, entry_price: float) -> float:
    if entry_price <= 0 or math.isnan(close_price):
        return math.nan
    return (close_price / entry_price - 1.0) * 100.0


def incomplete_trade(reason: str) -> dict[str, Any]:
    return {
        "entry_price": math.nan,
        "exit_date": "",
        "exit_price": math.nan,
        "holding_days": "",
        "return_pct": math.nan,
        "max_close_return_pct": math.nan,
        "min_close_return_pct": math.nan,
        "outcome_result": "incomplete",
        "exit_reason": reason,
    }


def finish_trade(
    window: pd.DataFrame,
    exit_idx: int,
    entry_price: float,
    exit_reason: str,
    outcome_result: str,
) -> dict[str, Any]:
    exit_close = safe_float(window.iloc[exit_idx].get("close"))
    if math.isnan(exit_close) or exit_close <= 0:
        return incomplete_trade("invalid_exit_close")
    close_returns = [
        close_return(safe_float(day.get("close")), entry_price)
        for _, day in window.iloc[: exit_idx + 1].iterrows()
    ]
    clean_returns = [value for value in close_returns if not math.isnan(value)]
    return {
        "entry_price": entry_price,
        "exit_date": normalize_date(window.iloc[exit_idx].get("date")),
        "exit_price": exit_close,
        "holding_days": str(exit_idx + 1),
        "return_pct": close_return(exit_close, entry_price),
        "max_close_return_pct": max(clean_returns) if clean_returns else math.nan,
        "min_close_return_pct": min(clean_returns) if clean_returns else math.nan,
        "outcome_result": outcome_result,
        "exit_reason": exit_reason,
    }


def simulate_close_only_rule(
    price: pd.DataFrame,
    entry_idx: int | None,
    failure_threshold_pct: float | None,
) -> dict[str, Any]:
    if entry_idx is None:
        return incomplete_trade("missing_retest_entry_price_row")
    planned_end_idx = entry_idx + 19
    if entry_idx >= len(price) or planned_end_idx >= len(price):
        return incomplete_trade("insufficient_forward_price_history")
    entry_price = safe_float(price.iloc[entry_idx].get("open"))
    if math.isnan(entry_price) or entry_price <= 0:
        return incomplete_trade("invalid_entry_open")
    window = price.iloc[entry_idx : planned_end_idx + 1].reset_index(drop=True)

    reached_five_close = False
    for day_idx, day in window.iterrows():
        close_pct = close_return(safe_float(day.get("close")), entry_price)
        if math.isnan(close_pct):
            continue
        if close_pct >= 10.0:
            return finish_trade(window, day_idx, entry_price, "tp10_close", "win")
        if reached_five_close and close_pct <= 5.0:
            return finish_trade(window, day_idx, entry_price, "neutral_after_5pct_pullback_close", "neutral")
        if close_pct >= 5.0:
            reached_five_close = True
        if failure_threshold_pct is not None and close_pct <= failure_threshold_pct:
            return finish_trade(window, day_idx, entry_price, "close_negative_stop", "loss")

    return finish_trade(window, len(window) - 1, entry_price, "fixed_20d_close_no_tp10_no_neutral", "loss")


def transition(source_outcome: str, outcome: str) -> str:
    return f"{source_outcome}_to_{outcome}" if source_outcome and outcome else "unknown"


def build_detail(generated_at: str) -> pd.DataFrame:
    source = load_selected_events()
    stock_names = load_stock_name_lookup(list(source["stock_id"].astype(str)))
    price_cache: dict[str, pd.DataFrame] = {}
    rows: list[dict[str, str]] = []
    for _, item in source.iterrows():
        stock_id = safe_str(item.get("stock_id"))
        if stock_id not in price_cache:
            price_cache[stock_id] = read_price_file(stock_id)
        price = price_cache[stock_id]
        entry_idx = index_for_date(price, item.get("retest_entry_date")) if not price.empty else None
        source_outcome = safe_str(item.get("close_neutral_outcome"))
        for rule_id, threshold in FAILURE_CONTROL_RULES:
            trade = simulate_close_only_rule(price, entry_idx, threshold)
            outcome = safe_str(trade.get("outcome_result"))
            rows.append(
                {
                    "research_id": RESEARCH_ID,
                    "source_comparison_research_id": COMPARISON_RESEARCH_ID,
                    "source_comparison_parameter_set_id": COMPARISON_PARAMETER_SET_ID,
                    "research_variant_id": RESEARCH_VARIANT_ID,
                    "parameter_set_id": PARAMETER_SET_ID,
                    "advisory_status": RESEARCH_VARIANT_ID,
                    "failure_control_scope_id": FAILURE_CONTROL_SCOPE_ID,
                    "comparison_scope_id": COMPARISON_SCOPE_ID,
                    "event_family_id": EVENT_FAMILY_ID,
                    "segment_id": safe_str(item.get("segment_id")),
                    "stock_id": stock_id,
                    "stock_name": stock_names.get(stock_id, safe_str(item.get("stock_name"))),
                    "signal_date": normalize_date(item.get("signal_date")),
                    "retest_date": normalize_date(item.get("retest_date")),
                    "retest_attack_date": normalize_date(item.get("retest_attack_date")),
                    "retest_entry_date": normalize_date(item.get("retest_entry_date")),
                    "visual_pre_signal_context": safe_str(item.get("visual_pre_signal_context")),
                    "selected_exit_rule_comparison_id": SELECTED_EXIT_RULE_COMPARISON_ID,
                    "research_selection_reason": RESEARCH_SELECTION_REASON,
                    "failure_control_rule_id": rule_id,
                    "close_negative_stop_threshold_pct": "" if threshold is None else metric_text(threshold),
                    "source_selected_outcome": source_outcome,
                    "source_selected_return_pct": metric_text(to_float(item.get("close_neutral_return_pct"))),
                    "source_selected_exit_date": normalize_date(item.get("close_neutral_exit_date")),
                    "source_selected_exit_reason": safe_str(item.get("close_neutral_exit_reason")),
                    "outcome_transition_from_source": transition(source_outcome, outcome),
                    "approved_for_daily": "false",
                    "production_readiness": PRODUCTION_READINESS,
                    "generated_at": generated_at,
                    "entry_price": metric_text(trade.get("entry_price")),
                    "exit_date": safe_str(trade.get("exit_date")),
                    "exit_price": metric_text(trade.get("exit_price")),
                    "holding_days": safe_str(trade.get("holding_days")),
                    "return_pct": metric_text(trade.get("return_pct")),
                    "max_close_return_pct": metric_text(trade.get("max_close_return_pct")),
                    "min_close_return_pct": metric_text(trade.get("min_close_return_pct")),
                    "outcome_result": outcome,
                    "exit_reason": safe_str(trade.get("exit_reason")),
                }
            )
    detail = pd.DataFrame(rows, columns=DETAIL_COLUMNS)
    if detail.empty:
        raise SystemExit("ERROR: no close-only failure-control detail rows generated")
    return detail


def pct(numerator: int, denominator: int) -> str:
    if denominator <= 0:
        return ""
    return metric_text(numerator / denominator * 100.0)


def summarize_group(group: pd.DataFrame, generated_at: str) -> dict[str, str]:
    outcomes = group["outcome_result"].astype(str)
    evaluated = outcomes.isin(["win", "neutral", "loss"])
    wins = int((outcomes == "win").sum())
    neutrals = int((outcomes == "neutral").sum())
    losses = int((outcomes == "loss").sum())
    win_loss = wins + losses
    returns = pd.to_numeric(group.loc[evaluated, "return_pct"], errors="coerce").dropna()
    max_close = pd.to_numeric(group.loc[evaluated, "max_close_return_pct"], errors="coerce").dropna()
    min_close = pd.to_numeric(group.loc[evaluated, "min_close_return_pct"], errors="coerce").dropna()
    source_outcomes = group["source_selected_outcome"].astype(str)
    changed = source_outcomes.ne(outcomes)
    source_loss_to_non_loss = source_outcomes.eq("loss") & outcomes.isin(["win", "neutral"])
    source_non_loss_to_loss = source_outcomes.isin(["win", "neutral"]) & outcomes.eq("loss")
    return {
        "research_id": RESEARCH_ID,
        "research_variant_id": RESEARCH_VARIANT_ID,
        "parameter_set_id": PARAMETER_SET_ID,
        "advisory_status": RESEARCH_VARIANT_ID,
        "failure_control_scope_id": FAILURE_CONTROL_SCOPE_ID,
        "selected_exit_rule_comparison_id": SELECTED_EXIT_RULE_COMPARISON_ID,
        "failure_control_rule_id": safe_str(group["failure_control_rule_id"].iloc[0]),
        "close_negative_stop_threshold_pct": safe_str(group["close_negative_stop_threshold_pct"].iloc[0]),
        "sample_size": str(len(group)),
        "unique_stock_count": str(group["stock_id"].nunique()),
        "win_count": str(wins),
        "neutral_count": str(neutrals),
        "loss_count": str(losses),
        "pure_win_rate_pct": pct(wins, win_loss),
        "neutral_inclusive_success_rate_pct": pct(wins + neutrals, int(evaluated.sum())),
        "positive_return_rate_pct": pct(int((returns > 0).sum()), len(returns)),
        "avg_return_pct": metric_text(float(returns.mean()) if len(returns) else math.nan),
        "median_return_pct": metric_text(float(returns.median()) if len(returns) else math.nan),
        "avg_max_close_return_pct": metric_text(float(max_close.mean()) if len(max_close) else math.nan),
        "median_max_close_return_pct": metric_text(float(max_close.median()) if len(max_close) else math.nan),
        "avg_min_close_return_pct": metric_text(float(min_close.mean()) if len(min_close) else math.nan),
        "median_min_close_return_pct": metric_text(float(min_close.median()) if len(min_close) else math.nan),
        "changed_from_source_count": str(int(changed.sum())),
        "source_loss_to_non_loss_count": str(int(source_loss_to_non_loss.sum())),
        "source_non_loss_to_loss_count": str(int(source_non_loss_to_loss.sum())),
        "approved_for_daily": "false",
        "production_readiness": PRODUCTION_READINESS,
        "generated_at": generated_at,
    }


def build_summary(detail: pd.DataFrame, generated_at: str) -> pd.DataFrame:
    rows = [summarize_group(group, generated_at) for _, group in detail.groupby("failure_control_rule_id", sort=False)]
    return pd.DataFrame(rows, columns=SUMMARY_COLUMNS)


def write_outputs(detail: pd.DataFrame, summary: pd.DataFrame) -> None:
    RESEARCH_LATEST_DIR.mkdir(parents=True, exist_ok=True)
    RESEARCH_HISTORY_DIR.mkdir(parents=True, exist_ok=True)
    detail.to_csv(LATEST_DETAIL_CSV, index=False, encoding="utf-8-sig")
    detail.to_csv(HISTORY_DETAIL_CSV, index=False, encoding="utf-8-sig")
    summary.to_csv(LATEST_SUMMARY_CSV, index=False, encoding="utf-8-sig")
    summary.to_csv(HISTORY_SUMMARY_CSV, index=False, encoding="utf-8-sig")
    lines = [
        "# Structured Neckline Close-Only Failure Control Audit",
        "",
        f"- research_id: `{RESEARCH_ID}`",
        f"- parameter_set_id: `{PARAMETER_SET_ID}`",
        f"- selected_exit_rule_comparison_id: `{SELECTED_EXIT_RULE_COMPARISON_ID}`",
        f"- selected rule source: `{CLOSE_NEUTRAL_RULE_ID}`",
        "- execution basis: buy next open; sell by close-based rules only",
        "- intraday +10% touch is not used",
        "- production impact: `none`",
        f"- production_readiness: `{PRODUCTION_READINESS}`",
        "",
        "## Summary",
        "",
        summary.to_markdown(index=False),
        "",
        "## Loss Rows By Rule",
        "",
    ]
    for rule_id, group in detail[detail["outcome_result"].eq("loss")].groupby("failure_control_rule_id", sort=False):
        cols = [
            "stock_id",
            "stock_name",
            "signal_date",
            "retest_entry_date",
            "return_pct",
            "max_close_return_pct",
            "min_close_return_pct",
            "exit_reason",
            "outcome_transition_from_source",
        ]
        lines.extend([f"### {rule_id}", "", group[cols].to_markdown(index=False), ""])
    lines.extend(
        [
            "## Boundary",
            "",
            "- This is research/backtest advisory-only evidence.",
            "- No production model condition, scoring, ranking, PDF logic, or baseline was changed.",
            "- Failure-control rows are candidate exit definitions only, not production filters.",
        ]
    )
    LATEST_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    generated_at = now_text()
    detail = build_detail(generated_at)
    summary = build_summary(detail, generated_at)
    write_outputs(detail, summary)
    print(
        "structured neckline close-only failure control audit built "
        f"detail_rows={len(detail)} summary_rows={len(summary)}"
    )
    print(f"latest_detail={LATEST_DETAIL_CSV.as_posix()}")
    print(f"latest_summary={LATEST_SUMMARY_CSV.as_posix()}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
