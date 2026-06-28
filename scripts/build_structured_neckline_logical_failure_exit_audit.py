from __future__ import annotations

from datetime import datetime
from pathlib import Path
from typing import Any
from zoneinfo import ZoneInfo
import math

import pandas as pd

from build_structured_neckline_close_only_failure_control_audit import (
    BASE_CLOSE_ONLY_RULE_ID,
    FAILURE_CONTROL_SCOPE_ID,
    LATEST_DETAIL_CSV as CLOSE_ONLY_DETAIL_CSV,
    PARAMETER_SET_ID as CLOSE_ONLY_PARAMETER_SET_ID,
    RESEARCH_ID as CLOSE_ONLY_RESEARCH_ID,
    RESEARCH_VARIANT_ID,
    close_return,
    event_key,
    index_for_date,
    metric_text,
    normalize_date,
    read_csv,
    read_price_file,
    safe_float,
    safe_str,
)
from build_structured_neckline_context_filter_entry_exit_audit import (
    LATEST_EVENT_CSV as CONTEXT_EVENT_CSV,
    PARAMETER_SET_ID as CONTEXT_EVENT_PARAMETER_SET_ID,
    RESEARCH_ID as CONTEXT_EVENT_RESEARCH_ID,
)
from build_structured_neckline_retest_entry_exit_grid import EVENT_FAMILY_ID, PRODUCTION_READINESS
from build_structured_neckline_selected_exit_loss_diagnostics import load_stock_name_lookup


ROOT = Path(__file__).resolve().parents[1]
RESEARCH_LATEST_DIR = ROOT / "output" / "latest" / "research_backtest"
RESEARCH_HISTORY_DIR = ROOT / "output" / "history" / "research"

RESEARCH_ID = "structured_neckline_logical_failure_exit_audit"
PARAMETER_SET_ID = "structured_neckline_logical_failure_exit_audit_20260629"
FAILURE_EXIT_SCOPE_ID = "selected_close_based_logical_failure_exit"
BASELINE_RULE_ID = "close_only_no_logical_failure_exit"

LATEST_DETAIL_CSV = RESEARCH_LATEST_DIR / "structured_neckline_logical_failure_exit_audit_latest.csv"
LATEST_SUMMARY_CSV = RESEARCH_LATEST_DIR / "structured_neckline_logical_failure_exit_audit_summary_latest.csv"
LATEST_MD = RESEARCH_LATEST_DIR / "structured_neckline_logical_failure_exit_audit_latest.md"
HISTORY_DETAIL_CSV = RESEARCH_HISTORY_DIR / "structured_neckline_logical_failure_exit_audit.csv"
HISTORY_SUMMARY_CSV = RESEARCH_HISTORY_DIR / "structured_neckline_logical_failure_exit_audit_summary.csv"

FAILURE_EXIT_RULE_IDS = [
    BASELINE_RULE_ID,
    "neckline_close_lost_two_sessions",
    "retest_low_close_break",
    "signal_low_close_break",
    "close_below_5ma_two_sessions",
    "close_below_10ma_two_sessions",
]

DETAIL_COLUMNS = [
    "research_id",
    "source_close_only_research_id",
    "source_close_only_parameter_set_id",
    "source_context_research_id",
    "source_context_parameter_set_id",
    "research_variant_id",
    "parameter_set_id",
    "advisory_status",
    "failure_exit_scope_id",
    "source_failure_control_scope_id",
    "event_family_id",
    "segment_id",
    "stock_id",
    "stock_name",
    "signal_date",
    "retest_date",
    "retest_attack_date",
    "retest_entry_date",
    "visual_pre_signal_context",
    "failure_exit_rule_id",
    "reference_price",
    "signal_low",
    "retest_low",
    "entry_price",
    "exit_date",
    "exit_price",
    "holding_days",
    "return_pct",
    "max_close_return_pct",
    "min_close_return_pct",
    "outcome_result",
    "exit_reason",
    "baseline_outcome",
    "baseline_return_pct",
    "baseline_exit_date",
    "baseline_exit_reason",
    "outcome_transition_from_baseline",
    "approved_for_daily",
    "production_readiness",
    "generated_at",
]

SUMMARY_COLUMNS = [
    "research_id",
    "research_variant_id",
    "parameter_set_id",
    "advisory_status",
    "failure_exit_scope_id",
    "failure_exit_rule_id",
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
    "changed_from_baseline_count",
    "baseline_loss_to_non_loss_count",
    "baseline_non_loss_to_loss_count",
    "approved_for_daily",
    "production_readiness",
    "generated_at",
]


def now_text() -> str:
    return datetime.now(ZoneInfo("Asia/Taipei")).strftime("%Y-%m-%d %H:%M:%S Asia/Taipei")


def to_float(value: Any) -> float:
    try:
        return float(value)
    except (TypeError, ValueError):
        return math.nan


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


def read_source_events() -> pd.DataFrame:
    close_only = read_csv(CLOSE_ONLY_DETAIL_CSV)
    context = read_csv(CONTEXT_EVENT_CSV)
    required_close = {
        "research_id",
        "parameter_set_id",
        "research_variant_id",
        "advisory_status",
        "failure_control_scope_id",
        "event_family_id",
        "segment_id",
        "stock_id",
        "stock_name",
        "signal_date",
        "retest_date",
        "retest_attack_date",
        "retest_entry_date",
        "visual_pre_signal_context",
        "failure_control_rule_id",
        "entry_price",
        "exit_date",
        "exit_price",
        "return_pct",
        "outcome_result",
        "exit_reason",
        "approved_for_daily",
        "production_readiness",
    }
    required_context = {
        "research_id",
        "parameter_set_id",
        "research_variant_id",
        "advisory_status",
        "event_family_id",
        "segment_id",
        "stock_id",
        "signal_date",
        "retest_date",
        "retest_entry_date",
        "reference_price",
        "approved_for_daily",
        "production_readiness",
    }
    missing_close = sorted(required_close - set(close_only.columns))
    missing_context = sorted(required_context - set(context.columns))
    if missing_close:
        raise SystemExit(f"ERROR: close-only detail missing columns: {missing_close}")
    if missing_context:
        raise SystemExit(f"ERROR: context event output missing columns: {missing_context}")

    base = close_only[
        close_only["research_id"].astype(str).eq(CLOSE_ONLY_RESEARCH_ID)
        & close_only["parameter_set_id"].astype(str).eq(CLOSE_ONLY_PARAMETER_SET_ID)
        & close_only["research_variant_id"].astype(str).eq(RESEARCH_VARIANT_ID)
        & close_only["advisory_status"].astype(str).eq(RESEARCH_VARIANT_ID)
        & close_only["failure_control_scope_id"].astype(str).eq(FAILURE_CONTROL_SCOPE_ID)
        & close_only["failure_control_rule_id"].astype(str).eq(BASE_CLOSE_ONLY_RULE_ID)
        & close_only["production_readiness"].astype(str).eq(PRODUCTION_READINESS)
        & close_only["approved_for_daily"].astype(str).str.lower().eq("false")
    ].copy()
    if base.empty:
        raise SystemExit("ERROR: no close-only baseline rows found")
    base["_key"] = base.apply(event_key, axis=1)
    if base["_key"].duplicated().any():
        raise SystemExit("ERROR: duplicate close-only baseline event keys")

    context_rows = context[
        context["research_id"].astype(str).eq(CONTEXT_EVENT_RESEARCH_ID)
        & context["parameter_set_id"].astype(str).eq(CONTEXT_EVENT_PARAMETER_SET_ID)
        & context["research_variant_id"].astype(str).eq(RESEARCH_VARIANT_ID)
        & context["advisory_status"].astype(str).eq(RESEARCH_VARIANT_ID)
        & context["event_family_id"].astype(str).eq(EVENT_FAMILY_ID)
        & context["production_readiness"].astype(str).eq(PRODUCTION_READINESS)
        & context["approved_for_daily"].astype(str).str.lower().eq("false")
    ].copy()
    context_rows["_key"] = context_rows.apply(event_key, axis=1)
    context_lookup = context_rows.drop_duplicates("_key").set_index("_key")
    missing_keys = sorted(set(base["_key"]) - set(context_lookup.index))
    if missing_keys:
        raise SystemExit(f"ERROR: missing context rows for baseline events: {missing_keys[:5]}")

    enriched = base.join(context_lookup[["reference_price"]], on="_key", rsuffix="_context")
    enriched = enriched.sort_values(["signal_date", "stock_id", "retest_entry_date"]).reset_index(drop=True)
    if len(enriched) != 23:
        raise SystemExit(f"ERROR: expected 23 source events; got {len(enriched)}")
    return enriched


def price_low_on_date(price: pd.DataFrame, date_text: Any) -> float:
    idx = index_for_date(price, date_text)
    if idx is None:
        return math.nan
    return safe_float(price.iloc[idx].get("low"))


def add_moving_averages(price: pd.DataFrame) -> pd.DataFrame:
    frame = price.copy()
    closes = pd.to_numeric(frame.get("close"), errors="coerce")
    frame["ma5"] = closes.rolling(5, min_periods=5).mean()
    frame["ma10"] = closes.rolling(10, min_periods=10).mean()
    return frame


def failure_triggered(rule_id: str, window: pd.DataFrame, day_idx: int, reference: float, signal_low: float, retest_low: float) -> str | None:
    close = safe_float(window.iloc[day_idx].get("close"))
    if math.isnan(close):
        return None
    if rule_id == BASELINE_RULE_ID:
        return None
    if rule_id == "neckline_close_lost_two_sessions":
        if day_idx < 1 or math.isnan(reference):
            return None
        prior_close = safe_float(window.iloc[day_idx - 1].get("close"))
        if not math.isnan(prior_close) and prior_close < reference and close < reference:
            return "neckline_close_lost_two_sessions"
        return None
    if rule_id == "retest_low_close_break":
        if not math.isnan(retest_low) and close < retest_low:
            return "retest_low_close_break"
        return None
    if rule_id == "signal_low_close_break":
        if not math.isnan(signal_low) and close < signal_low:
            return "signal_low_close_break"
        return None
    if rule_id == "close_below_5ma_two_sessions":
        if day_idx < 1:
            return None
        ma = safe_float(window.iloc[day_idx].get("ma5"))
        prior_ma = safe_float(window.iloc[day_idx - 1].get("ma5"))
        prior_close = safe_float(window.iloc[day_idx - 1].get("close"))
        if not any(math.isnan(value) for value in [ma, prior_ma, prior_close]) and prior_close < prior_ma and close < ma:
            return "close_below_5ma_two_sessions"
        return None
    if rule_id == "close_below_10ma_two_sessions":
        if day_idx < 1:
            return None
        ma = safe_float(window.iloc[day_idx].get("ma10"))
        prior_ma = safe_float(window.iloc[day_idx - 1].get("ma10"))
        prior_close = safe_float(window.iloc[day_idx - 1].get("close"))
        if not any(math.isnan(value) for value in [ma, prior_ma, prior_close]) and prior_close < prior_ma and close < ma:
            return "close_below_10ma_two_sessions"
        return None
    raise ValueError(f"unknown failure exit rule: {rule_id}")


def simulate_rule(price: pd.DataFrame, entry_idx: int | None, rule_id: str, reference: float, signal_low: float, retest_low: float) -> dict[str, Any]:
    if entry_idx is None:
        return incomplete_trade("missing_retest_entry_price_row")
    planned_end_idx = entry_idx + 19
    if entry_idx >= len(price) or planned_end_idx >= len(price):
        return incomplete_trade("insufficient_forward_price_history")
    entry_price = safe_float(price.iloc[entry_idx].get("open"))
    if math.isnan(entry_price) or entry_price <= 0:
        return incomplete_trade("invalid_entry_open")
    price_with_ma = add_moving_averages(price)
    window = price_with_ma.iloc[entry_idx : planned_end_idx + 1].reset_index(drop=True)

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
        failure_reason = failure_triggered(rule_id, window, day_idx, reference, signal_low, retest_low)
        if failure_reason:
            return finish_trade(window, day_idx, entry_price, failure_reason, "loss")

    return finish_trade(window, len(window) - 1, entry_price, "fixed_20d_close_no_tp10_no_neutral", "loss")


def transition(baseline_outcome: str, outcome: str) -> str:
    return f"{baseline_outcome}_to_{outcome}" if baseline_outcome and outcome else "unknown"


def build_detail(generated_at: str) -> pd.DataFrame:
    source = read_source_events()
    stock_names = load_stock_name_lookup(list(source["stock_id"].astype(str)))
    price_cache: dict[str, pd.DataFrame] = {}
    rows: list[dict[str, str]] = []
    for _, item in source.iterrows():
        stock_id = safe_str(item.get("stock_id"))
        if stock_id not in price_cache:
            price_cache[stock_id] = read_price_file(stock_id)
        price = price_cache[stock_id]
        entry_idx = index_for_date(price, item.get("retest_entry_date")) if not price.empty else None
        reference = to_float(item.get("reference_price"))
        signal_low = price_low_on_date(price, item.get("signal_date")) if not price.empty else math.nan
        retest_low = price_low_on_date(price, item.get("retest_date")) if not price.empty else math.nan
        baseline_outcome = safe_str(item.get("outcome_result"))
        for rule_id in FAILURE_EXIT_RULE_IDS:
            trade = simulate_rule(price, entry_idx, rule_id, reference, signal_low, retest_low)
            outcome = safe_str(trade.get("outcome_result"))
            rows.append(
                {
                    "research_id": RESEARCH_ID,
                    "source_close_only_research_id": CLOSE_ONLY_RESEARCH_ID,
                    "source_close_only_parameter_set_id": CLOSE_ONLY_PARAMETER_SET_ID,
                    "source_context_research_id": CONTEXT_EVENT_RESEARCH_ID,
                    "source_context_parameter_set_id": CONTEXT_EVENT_PARAMETER_SET_ID,
                    "research_variant_id": RESEARCH_VARIANT_ID,
                    "parameter_set_id": PARAMETER_SET_ID,
                    "advisory_status": RESEARCH_VARIANT_ID,
                    "failure_exit_scope_id": FAILURE_EXIT_SCOPE_ID,
                    "source_failure_control_scope_id": FAILURE_CONTROL_SCOPE_ID,
                    "event_family_id": EVENT_FAMILY_ID,
                    "segment_id": safe_str(item.get("segment_id")),
                    "stock_id": stock_id,
                    "stock_name": stock_names.get(stock_id, safe_str(item.get("stock_name"))),
                    "signal_date": normalize_date(item.get("signal_date")),
                    "retest_date": normalize_date(item.get("retest_date")),
                    "retest_attack_date": normalize_date(item.get("retest_attack_date")),
                    "retest_entry_date": normalize_date(item.get("retest_entry_date")),
                    "visual_pre_signal_context": safe_str(item.get("visual_pre_signal_context")),
                    "failure_exit_rule_id": rule_id,
                    "reference_price": metric_text(reference),
                    "signal_low": metric_text(signal_low),
                    "retest_low": metric_text(retest_low),
                    "baseline_outcome": baseline_outcome,
                    "baseline_return_pct": metric_text(to_float(item.get("return_pct"))),
                    "baseline_exit_date": normalize_date(item.get("exit_date")),
                    "baseline_exit_reason": safe_str(item.get("exit_reason")),
                    "outcome_transition_from_baseline": transition(baseline_outcome, outcome),
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
        raise SystemExit("ERROR: no logical failure exit audit rows generated")
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
    baseline_outcomes = group["baseline_outcome"].astype(str)
    changed = baseline_outcomes.ne(outcomes)
    baseline_loss_to_non_loss = baseline_outcomes.eq("loss") & outcomes.isin(["win", "neutral"])
    baseline_non_loss_to_loss = baseline_outcomes.isin(["win", "neutral"]) & outcomes.eq("loss")
    return {
        "research_id": RESEARCH_ID,
        "research_variant_id": RESEARCH_VARIANT_ID,
        "parameter_set_id": PARAMETER_SET_ID,
        "advisory_status": RESEARCH_VARIANT_ID,
        "failure_exit_scope_id": FAILURE_EXIT_SCOPE_ID,
        "failure_exit_rule_id": safe_str(group["failure_exit_rule_id"].iloc[0]),
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
        "changed_from_baseline_count": str(int(changed.sum())),
        "baseline_loss_to_non_loss_count": str(int(baseline_loss_to_non_loss.sum())),
        "baseline_non_loss_to_loss_count": str(int(baseline_non_loss_to_loss.sum())),
        "approved_for_daily": "false",
        "production_readiness": PRODUCTION_READINESS,
        "generated_at": generated_at,
    }


def build_summary(detail: pd.DataFrame, generated_at: str) -> pd.DataFrame:
    rows = [summarize_group(group, generated_at) for _, group in detail.groupby("failure_exit_rule_id", sort=False)]
    return pd.DataFrame(rows, columns=SUMMARY_COLUMNS)


def write_outputs(detail: pd.DataFrame, summary: pd.DataFrame) -> None:
    RESEARCH_LATEST_DIR.mkdir(parents=True, exist_ok=True)
    RESEARCH_HISTORY_DIR.mkdir(parents=True, exist_ok=True)
    detail.to_csv(LATEST_DETAIL_CSV, index=False, encoding="utf-8-sig")
    detail.to_csv(HISTORY_DETAIL_CSV, index=False, encoding="utf-8-sig")
    summary.to_csv(LATEST_SUMMARY_CSV, index=False, encoding="utf-8-sig")
    summary.to_csv(HISTORY_SUMMARY_CSV, index=False, encoding="utf-8-sig")
    lines = [
        "# Structured Neckline Logical Failure Exit Audit",
        "",
        f"- research_id: `{RESEARCH_ID}`",
        f"- parameter_set_id: `{PARAMETER_SET_ID}`",
        f"- baseline_rule_id: `{BASELINE_RULE_ID}`",
        "- execution basis: buy next open; sell by close-based rules only",
        "- intraday high/low trigger is not used",
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
    loss_cols = [
        "stock_id",
        "stock_name",
        "signal_date",
        "retest_entry_date",
        "return_pct",
        "max_close_return_pct",
        "min_close_return_pct",
        "exit_reason",
        "outcome_transition_from_baseline",
    ]
    for rule_id, group in detail[detail["outcome_result"].eq("loss")].groupby("failure_exit_rule_id", sort=False):
        lines.extend([f"### {rule_id}", "", group[loss_cols].to_markdown(index=False), ""])
    lines.extend(
        [
            "## Boundary",
            "",
            "- This is research/backtest advisory-only evidence.",
            "- No production model condition, scoring, ranking, PDF logic, or baseline was changed.",
            "- Logical failure rows are candidate exit definitions only, not production filters.",
        ]
    )
    LATEST_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    generated_at = now_text()
    detail = build_detail(generated_at)
    summary = build_summary(detail, generated_at)
    write_outputs(detail, summary)
    print(
        "structured neckline logical failure exit audit built "
        f"detail_rows={len(detail)} summary_rows={len(summary)}"
    )
    print(f"latest_detail={LATEST_DETAIL_CSV.as_posix()}")
    print(f"latest_summary={LATEST_SUMMARY_CSV.as_posix()}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
