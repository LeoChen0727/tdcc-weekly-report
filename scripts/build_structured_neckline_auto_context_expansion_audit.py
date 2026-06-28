from __future__ import annotations

from datetime import datetime
from pathlib import Path
from typing import Any, Callable
from zoneinfo import ZoneInfo
import math

import pandas as pd

from build_structured_neckline_logical_failure_exit_audit import (
    BASELINE_RULE_ID,
    FAILURE_EXIT_SCOPE_ID as SOURCE_FAILURE_EXIT_SCOPE_ID,
    PARAMETER_SET_ID as SOURCE_FAILURE_EXIT_PARAMETER_SET_ID,
    RESEARCH_ID as SOURCE_FAILURE_EXIT_RESEARCH_ID,
    incomplete_trade,
    price_low_on_date,
    simulate_rule,
)
from build_structured_neckline_retest_entry_exit_grid import (
    EVENT_FAMILY_ID,
    LATEST_DETAIL_CSV as ENTRY_EXIT_DETAIL_CSV,
    OUTCOME_RULE_BY_EXIT,
    PARAMETER_SET_ID as ENTRY_EXIT_PARAMETER_SET_ID,
    PRODUCTION_READINESS,
    RESEARCH_ID as ENTRY_EXIT_RESEARCH_ID,
    RESEARCH_VARIANT_ID,
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

RESEARCH_ID = "structured_neckline_auto_context_expansion_audit"
PARAMETER_SET_ID = "structured_neckline_auto_context_expansion_audit_20260629"
AUTO_CONTEXT_SCOPE_ID = "auto_pre_signal_context_expansion"

SOURCE_SEGMENT_ID = "all_retest_entries"
TARGET_SEGMENT_ID = "low_position_le60_market_bull"
TARGET_STOP_RULE_ID = "signal_low_stop"
TARGET_EXIT_RULE_ID = "tp10_close_or_neutral_after_5pct_close_20d"
TARGET_OUTCOME_RULE_ID = OUTCOME_RULE_BY_EXIT[TARGET_EXIT_RULE_ID]
NECKLINE_FAILURE_RULE_ID = "neckline_close_lost_two_sessions"
FAILURE_EXIT_RULE_IDS = [BASELINE_RULE_ID, NECKLINE_FAILURE_RULE_ID]

LATEST_DETAIL_CSV = RESEARCH_LATEST_DIR / "structured_neckline_auto_context_expansion_audit_latest.csv"
LATEST_SUMMARY_CSV = RESEARCH_LATEST_DIR / "structured_neckline_auto_context_expansion_audit_summary_latest.csv"
LATEST_CONTEXT_CSV = RESEARCH_LATEST_DIR / "structured_neckline_auto_context_expansion_context_latest.csv"
LATEST_MD = RESEARCH_LATEST_DIR / "structured_neckline_auto_context_expansion_audit_latest.md"
HISTORY_DETAIL_CSV = RESEARCH_HISTORY_DIR / "structured_neckline_auto_context_expansion_audit.csv"
HISTORY_SUMMARY_CSV = RESEARCH_HISTORY_DIR / "structured_neckline_auto_context_expansion_audit_summary.csv"
HISTORY_CONTEXT_CSV = RESEARCH_HISTORY_DIR / "structured_neckline_auto_context_expansion_context.csv"

DETAIL_COLUMNS = [
    "research_id",
    "source_entry_exit_research_id",
    "source_entry_exit_parameter_set_id",
    "source_failure_exit_research_id",
    "source_failure_exit_parameter_set_id",
    "research_variant_id",
    "parameter_set_id",
    "advisory_status",
    "auto_context_scope_id",
    "source_failure_exit_scope_id",
    "event_family_id",
    "source_segment_id",
    "stock_id",
    "stock_name",
    "signal_date",
    "retest_date",
    "retest_attack_date",
    "retest_entry_date",
    "market_regime",
    "low_position_120_pct",
    "base_width_pct",
    "support_touch_count",
    "in_low_position_le60_market_bull",
    "auto_pre_signal_context",
    "auto_context_filter_result",
    "auto_context_start",
    "auto_context_end",
    "auto_context_sessions",
    "auto_context_return_pct",
    "auto_context_range_pct",
    "auto_context_slope_pct_per_20d",
    "auto_context_max_drawdown_pct",
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
    "approved_for_daily",
    "production_readiness",
    "generated_at",
]

SUMMARY_COLUMNS = [
    "research_id",
    "research_variant_id",
    "parameter_set_id",
    "advisory_status",
    "auto_context_scope_id",
    "analysis_scope_id",
    "failure_exit_rule_id",
    "sample_size",
    "unique_stock_count",
    "auto_bearish_count",
    "auto_non_bearish_count",
    "auto_unknown_count",
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
    "approved_for_daily",
    "production_readiness",
    "generated_at",
]

CONTEXT_COLUMNS = [
    "research_id",
    "research_variant_id",
    "parameter_set_id",
    "advisory_status",
    "auto_context_scope_id",
    "analysis_scope_id",
    "auto_pre_signal_context",
    "event_count",
    "win_count",
    "neutral_count",
    "loss_count",
    "pure_win_rate_pct",
    "neutral_inclusive_success_rate_pct",
    "avg_return_pct",
    "median_return_pct",
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
    return "|".join(
        [
            safe_str(row.get("stock_id")),
            normalize_date(row.get("signal_date")),
            normalize_date(row.get("retest_entry_date")),
        ]
    )


def load_source_events() -> pd.DataFrame:
    detail = read_csv(ENTRY_EXIT_DETAIL_CSV)
    required = {
        "research_id",
        "research_variant_id",
        "parameter_set_id",
        "advisory_status",
        "event_family_id",
        "segment_id",
        "stock_id",
        "stock_name",
        "signal_date",
        "retest_date",
        "retest_attack_date",
        "retest_entry_date",
        "reference_price",
        "stop_rule_id",
        "exit_rule_id",
        "outcome_rule_id",
        "market_regime",
        "low_position_120_pct",
        "base_width_pct",
        "support_touch_count",
        "approved_for_daily",
        "production_readiness",
    }
    missing = sorted(required - set(detail.columns))
    if missing:
        raise SystemExit(f"ERROR: entry/exit detail missing columns: {missing}")
    rows = detail[
        detail["research_id"].astype(str).eq(ENTRY_EXIT_RESEARCH_ID)
        & detail["parameter_set_id"].astype(str).eq(ENTRY_EXIT_PARAMETER_SET_ID)
        & detail["research_variant_id"].astype(str).eq(RESEARCH_VARIANT_ID)
        & detail["advisory_status"].astype(str).eq(RESEARCH_VARIANT_ID)
        & detail["event_family_id"].astype(str).eq(EVENT_FAMILY_ID)
        & detail["segment_id"].astype(str).eq(SOURCE_SEGMENT_ID)
        & detail["stop_rule_id"].astype(str).eq(TARGET_STOP_RULE_ID)
        & detail["exit_rule_id"].astype(str).eq(TARGET_EXIT_RULE_ID)
        & detail["outcome_rule_id"].astype(str).eq(TARGET_OUTCOME_RULE_ID)
        & detail["production_readiness"].astype(str).eq(PRODUCTION_READINESS)
        & detail["approved_for_daily"].astype(str).str.lower().eq("false")
    ].copy()
    if rows.empty:
        raise SystemExit("ERROR: no source retest-entry rows found")
    rows["_key"] = rows.apply(event_key, axis=1)
    duplicated = rows["_key"].duplicated(keep=False)
    if duplicated.any():
        duplicates = sorted(set(rows.loc[duplicated, "_key"].astype(str)))
        raise SystemExit(f"ERROR: duplicate source event keys: {duplicates[:5]}")
    rows["low_position_120_pct"] = pd.to_numeric(rows["low_position_120_pct"], errors="coerce")
    if len(rows) != 374:
        raise SystemExit(f"ERROR: expected 374 all retest-entry events; got {len(rows)}")
    return rows.sort_values(["signal_date", "stock_id", "retest_entry_date"]).reset_index(drop=True)


def pct_change(end_value: float, start_value: float) -> float:
    if math.isnan(start_value) or math.isnan(end_value) or start_value <= 0:
        return math.nan
    return (end_value / start_value - 1.0) * 100.0


def max_drawdown_pct(closes: list[float]) -> float:
    peak = -math.inf
    worst = 0.0
    for close in closes:
        if math.isnan(close):
            continue
        peak = max(peak, close)
        if peak > 0:
            worst = min(worst, (close / peak - 1.0) * 100.0)
    return worst if peak > 0 else math.nan


def slope_pct_per_20d(closes: list[float]) -> float:
    values = [value for value in closes if not math.isnan(value)]
    if len(values) < 10 or values[0] <= 0:
        return math.nan
    n = len(values)
    mean_x = (n - 1) / 2.0
    mean_y = sum(values) / n
    denom = sum((idx - mean_x) ** 2 for idx in range(n))
    if denom == 0:
        return math.nan
    slope = sum((idx - mean_x) * (value - mean_y) for idx, value in enumerate(values)) / denom
    return slope * 20.0 / values[0] * 100.0


def classify_context(return_pct: float, range_pct: float, slope20_pct: float, drawdown_pct: float) -> str:
    if any(math.isnan(value) for value in [return_pct, range_pct, slope20_pct, drawdown_pct]):
        return "unknown"
    if return_pct <= -12.0 or (slope20_pct <= -4.0 and drawdown_pct <= -18.0):
        return "bearish"
    if abs(return_pct) <= 8.0 and range_pct <= 35.0 and drawdown_pct >= -22.0:
        return "sideways_or_consolidation"
    if return_pct >= 8.0 and slope20_pct >= 1.25:
        return "slow_uptrend"
    return "volatile_mixed"


def context_filter_result(context: str) -> str:
    if context == "unknown":
        return "unknown"
    return "auto_bearish" if context == "bearish" else "auto_non_bearish"


def compute_context(price: pd.DataFrame, signal_date: Any) -> dict[str, str]:
    if price.empty or "date" not in price.columns:
        return {
            "auto_pre_signal_context": "unknown",
            "auto_context_filter_result": "unknown",
            "auto_context_start": "",
            "auto_context_end": "",
            "auto_context_sessions": "0",
            "auto_context_return_pct": "",
            "auto_context_range_pct": "",
            "auto_context_slope_pct_per_20d": "",
            "auto_context_max_drawdown_pct": "",
        }
    signal_idx = index_for_date(price, signal_date)
    if signal_idx is None or signal_idx <= 1:
        return {
            "auto_pre_signal_context": "unknown",
            "auto_context_filter_result": "unknown",
            "auto_context_start": "",
            "auto_context_end": "",
            "auto_context_sessions": "0",
            "auto_context_return_pct": "",
            "auto_context_range_pct": "",
            "auto_context_slope_pct_per_20d": "",
            "auto_context_max_drawdown_pct": "",
        }
    start_idx = max(0, signal_idx - 90)
    end_idx = signal_idx - 1
    window = price.iloc[start_idx : end_idx + 1].copy()
    if len(window) < 20:
        context = "unknown"
        return_pct = range_pct = slope20 = drawdown = math.nan
    else:
        closes = [safe_float(value) for value in window.get("close", [])]
        highs = pd.to_numeric(window.get("high", ""), errors="coerce").dropna()
        lows = pd.to_numeric(window.get("low", ""), errors="coerce").dropna()
        return_pct = pct_change(closes[-1], closes[0])
        range_pct = (float(highs.max()) / float(lows.min()) - 1.0) * 100.0 if len(highs) and len(lows) and float(lows.min()) > 0 else math.nan
        slope20 = slope_pct_per_20d(closes)
        drawdown = max_drawdown_pct(closes)
        context = classify_context(return_pct, range_pct, slope20, drawdown)
    return {
        "auto_pre_signal_context": context,
        "auto_context_filter_result": context_filter_result(context),
        "auto_context_start": normalize_date(price.iloc[start_idx].get("date")),
        "auto_context_end": normalize_date(price.iloc[end_idx].get("date")),
        "auto_context_sessions": str(len(window)),
        "auto_context_return_pct": metric_text(return_pct),
        "auto_context_range_pct": metric_text(range_pct),
        "auto_context_slope_pct_per_20d": metric_text(slope20),
        "auto_context_max_drawdown_pct": metric_text(drawdown),
    }


def in_target_segment(row: pd.Series) -> bool:
    low_position = to_float(row.get("low_position_120_pct"))
    market_regime = safe_str(row.get("market_regime"))
    return not math.isnan(low_position) and low_position <= 60.0 and market_regime in {"strong_bull", "mild_bull"}


def build_detail(generated_at: str) -> pd.DataFrame:
    source = load_source_events()
    stock_names = load_stock_name_lookup(list(source["stock_id"].astype(str)))
    price_cache: dict[str, pd.DataFrame] = {}
    rows: list[dict[str, str]] = []
    for _, item in source.iterrows():
        stock_id = safe_str(item.get("stock_id"))
        if stock_id not in price_cache:
            price_cache[stock_id] = read_price_file(stock_id)
        price = price_cache[stock_id]
        context = compute_context(price, item.get("signal_date")) if not price.empty else compute_context(pd.DataFrame(), item.get("signal_date"))
        entry_idx = index_for_date(price, item.get("retest_entry_date")) if not price.empty else None
        reference = to_float(item.get("reference_price"))
        signal_low = price_low_on_date(price, item.get("signal_date")) if not price.empty else math.nan
        retest_low = price_low_on_date(price, item.get("retest_date")) if not price.empty else math.nan
        target_segment = in_target_segment(item)
        for rule_id in FAILURE_EXIT_RULE_IDS:
            trade = simulate_rule(price, entry_idx, rule_id, reference, signal_low, retest_low) if not price.empty else incomplete_trade("missing_price_history")
            rows.append(
                {
                    "research_id": RESEARCH_ID,
                    "source_entry_exit_research_id": ENTRY_EXIT_RESEARCH_ID,
                    "source_entry_exit_parameter_set_id": ENTRY_EXIT_PARAMETER_SET_ID,
                    "source_failure_exit_research_id": SOURCE_FAILURE_EXIT_RESEARCH_ID,
                    "source_failure_exit_parameter_set_id": SOURCE_FAILURE_EXIT_PARAMETER_SET_ID,
                    "research_variant_id": RESEARCH_VARIANT_ID,
                    "parameter_set_id": PARAMETER_SET_ID,
                    "advisory_status": RESEARCH_VARIANT_ID,
                    "auto_context_scope_id": AUTO_CONTEXT_SCOPE_ID,
                    "source_failure_exit_scope_id": SOURCE_FAILURE_EXIT_SCOPE_ID,
                    "event_family_id": EVENT_FAMILY_ID,
                    "source_segment_id": SOURCE_SEGMENT_ID,
                    "stock_id": stock_id,
                    "stock_name": stock_names.get(stock_id, safe_str(item.get("stock_name"))),
                    "signal_date": normalize_date(item.get("signal_date")),
                    "retest_date": normalize_date(item.get("retest_date")),
                    "retest_attack_date": normalize_date(item.get("retest_attack_date")),
                    "retest_entry_date": normalize_date(item.get("retest_entry_date")),
                    "market_regime": safe_str(item.get("market_regime")),
                    "low_position_120_pct": metric_text(low_position) if not math.isnan((low_position := to_float(item.get("low_position_120_pct")))) else "",
                    "base_width_pct": metric_text(to_float(item.get("base_width_pct"))),
                    "support_touch_count": safe_str(item.get("support_touch_count")),
                    "in_low_position_le60_market_bull": "true" if target_segment else "false",
                    **context,
                    "failure_exit_rule_id": rule_id,
                    "reference_price": metric_text(reference),
                    "signal_low": metric_text(signal_low),
                    "retest_low": metric_text(retest_low),
                    "entry_price": metric_text(trade.get("entry_price")),
                    "exit_date": safe_str(trade.get("exit_date")),
                    "exit_price": metric_text(trade.get("exit_price")),
                    "holding_days": safe_str(trade.get("holding_days")),
                    "return_pct": metric_text(trade.get("return_pct")),
                    "max_close_return_pct": metric_text(trade.get("max_close_return_pct")),
                    "min_close_return_pct": metric_text(trade.get("min_close_return_pct")),
                    "outcome_result": safe_str(trade.get("outcome_result")),
                    "exit_reason": safe_str(trade.get("exit_reason")),
                    "approved_for_daily": "false",
                    "production_readiness": PRODUCTION_READINESS,
                    "generated_at": generated_at,
                }
            )
    detail = pd.DataFrame(rows, columns=DETAIL_COLUMNS)
    if detail.empty:
        raise SystemExit("ERROR: no auto context expansion detail rows generated")
    return detail


def pct(numerator: int, denominator: int) -> str:
    if denominator <= 0:
        return ""
    return metric_text(numerator / denominator * 100.0)


def summarize_rows(group: pd.DataFrame, analysis_scope_id: str, generated_at: str) -> dict[str, str]:
    outcomes = group["outcome_result"].astype(str)
    evaluated = outcomes.isin(["win", "neutral", "loss"])
    wins = int((outcomes == "win").sum())
    neutrals = int((outcomes == "neutral").sum())
    losses = int((outcomes == "loss").sum())
    win_loss = wins + losses
    returns = pd.to_numeric(group.loc[evaluated, "return_pct"], errors="coerce").dropna()
    max_close = pd.to_numeric(group.loc[evaluated, "max_close_return_pct"], errors="coerce").dropna()
    min_close = pd.to_numeric(group.loc[evaluated, "min_close_return_pct"], errors="coerce").dropna()
    filters = group["auto_context_filter_result"].astype(str)
    return {
        "research_id": RESEARCH_ID,
        "research_variant_id": RESEARCH_VARIANT_ID,
        "parameter_set_id": PARAMETER_SET_ID,
        "advisory_status": RESEARCH_VARIANT_ID,
        "auto_context_scope_id": AUTO_CONTEXT_SCOPE_ID,
        "analysis_scope_id": analysis_scope_id,
        "failure_exit_rule_id": safe_str(group["failure_exit_rule_id"].iloc[0]),
        "sample_size": str(len(group)),
        "unique_stock_count": str(group["stock_id"].nunique()),
        "auto_bearish_count": str(int(filters.eq("auto_bearish").sum())),
        "auto_non_bearish_count": str(int(filters.eq("auto_non_bearish").sum())),
        "auto_unknown_count": str(int(filters.eq("unknown").sum())),
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
        "approved_for_daily": "false",
        "production_readiness": PRODUCTION_READINESS,
        "generated_at": generated_at,
    }


def scope_definitions(frame: pd.DataFrame) -> list[tuple[str, Callable[[pd.DataFrame], pd.Series]]]:
    return [
        ("all_retest_entries", lambda d: pd.Series(True, index=d.index)),
        ("all_auto_non_bearish", lambda d: d["auto_context_filter_result"].eq("auto_non_bearish")),
        ("all_auto_bearish", lambda d: d["auto_context_filter_result"].eq("auto_bearish")),
        ("low_position_le60_market_bull", lambda d: d["in_low_position_le60_market_bull"].eq("true")),
        (
            "low_position_le60_market_bull_auto_non_bearish",
            lambda d: d["in_low_position_le60_market_bull"].eq("true") & d["auto_context_filter_result"].eq("auto_non_bearish"),
        ),
        (
            "low_position_le60_market_bull_auto_bearish",
            lambda d: d["in_low_position_le60_market_bull"].eq("true") & d["auto_context_filter_result"].eq("auto_bearish"),
        ),
    ]


def build_summary(detail: pd.DataFrame, generated_at: str) -> pd.DataFrame:
    rows: list[dict[str, str]] = []
    for scope_id, selector in scope_definitions(detail):
        scope = detail[selector(detail)].copy()
        if scope.empty:
            continue
        for _rule_id, group in scope.groupby("failure_exit_rule_id", sort=False):
            rows.append(summarize_rows(group, scope_id, generated_at))
    return pd.DataFrame(rows, columns=SUMMARY_COLUMNS)


def build_context_summary(detail: pd.DataFrame, generated_at: str) -> pd.DataFrame:
    baseline = detail[detail["failure_exit_rule_id"].eq(BASELINE_RULE_ID)].copy()
    rows: list[dict[str, str]] = []
    for scope_id, selector in scope_definitions(baseline):
        scope = baseline[selector(baseline)].copy()
        if scope.empty:
            continue
        for context, group in scope.groupby("auto_pre_signal_context", dropna=False):
            outcomes = group["outcome_result"].astype(str)
            wins = int((outcomes == "win").sum())
            neutrals = int((outcomes == "neutral").sum())
            losses = int((outcomes == "loss").sum())
            win_loss = wins + losses
            returns = pd.to_numeric(group["return_pct"], errors="coerce").dropna()
            rows.append(
                {
                    "research_id": RESEARCH_ID,
                    "research_variant_id": RESEARCH_VARIANT_ID,
                    "parameter_set_id": PARAMETER_SET_ID,
                    "advisory_status": RESEARCH_VARIANT_ID,
                    "auto_context_scope_id": AUTO_CONTEXT_SCOPE_ID,
                    "analysis_scope_id": scope_id,
                    "auto_pre_signal_context": safe_str(context),
                    "event_count": str(len(group)),
                    "win_count": str(wins),
                    "neutral_count": str(neutrals),
                    "loss_count": str(losses),
                    "pure_win_rate_pct": pct(wins, win_loss),
                    "neutral_inclusive_success_rate_pct": pct(wins + neutrals, len(group)),
                    "avg_return_pct": metric_text(float(returns.mean()) if len(returns) else math.nan),
                    "median_return_pct": metric_text(float(returns.median()) if len(returns) else math.nan),
                    "approved_for_daily": "false",
                    "production_readiness": PRODUCTION_READINESS,
                    "generated_at": generated_at,
                }
            )
    return pd.DataFrame(rows, columns=CONTEXT_COLUMNS)


def markdown_table(frame: pd.DataFrame, columns: list[str], limit: int = 50) -> str:
    if frame.empty:
        return "_No rows._"
    return frame.loc[:, columns].head(limit).to_markdown(index=False)


def write_outputs(detail: pd.DataFrame, summary: pd.DataFrame, context: pd.DataFrame) -> None:
    RESEARCH_LATEST_DIR.mkdir(parents=True, exist_ok=True)
    RESEARCH_HISTORY_DIR.mkdir(parents=True, exist_ok=True)
    detail.to_csv(LATEST_DETAIL_CSV, index=False, encoding="utf-8-sig")
    detail.to_csv(HISTORY_DETAIL_CSV, index=False, encoding="utf-8-sig")
    summary.to_csv(LATEST_SUMMARY_CSV, index=False, encoding="utf-8-sig")
    summary.to_csv(HISTORY_SUMMARY_CSV, index=False, encoding="utf-8-sig")
    context.to_csv(LATEST_CONTEXT_CSV, index=False, encoding="utf-8-sig")
    context.to_csv(HISTORY_CONTEXT_CSV, index=False, encoding="utf-8-sig")
    key_summary = summary[
        summary["analysis_scope_id"].isin(
            [
                "all_retest_entries",
                "all_auto_non_bearish",
                "low_position_le60_market_bull",
                "low_position_le60_market_bull_auto_non_bearish",
            ]
        )
    ].copy()
    lines = [
        "# Structured Neckline Auto Context Expansion Audit",
        "",
        f"- research_id: `{RESEARCH_ID}`",
        f"- parameter_set_id: `{PARAMETER_SET_ID}`",
        "- source_pool: `all_retest_entries` from structured neckline retest entry/exit grid",
        "- auto context window: 90 sessions before signal date through the trading day before signal date",
        "- failure rules compared: `close_only_no_logical_failure_exit` and `neckline_close_lost_two_sessions`",
        "- execution basis: buy next open; sell by close-based rules only",
        "- intraday high/low trigger is not used",
        "- production impact: `none`",
        f"- production_readiness: `{PRODUCTION_READINESS}`",
        "",
        "## Key Summary",
        "",
        markdown_table(
            key_summary,
            [
                "analysis_scope_id",
                "failure_exit_rule_id",
                "sample_size",
                "win_count",
                "neutral_count",
                "loss_count",
                "neutral_inclusive_success_rate_pct",
                "avg_return_pct",
                "median_return_pct",
            ],
            limit=20,
        ),
        "",
        "## Auto Context Distribution",
        "",
        markdown_table(
            context,
            [
                "analysis_scope_id",
                "auto_pre_signal_context",
                "event_count",
                "win_count",
                "neutral_count",
                "loss_count",
                "neutral_inclusive_success_rate_pct",
                "avg_return_pct",
            ],
            limit=40,
        ),
        "",
        "## Boundary",
        "",
        "- This is research/backtest advisory-only evidence.",
        "- No production model condition, scoring, ranking, PDF logic, or baseline was changed.",
        "- Auto context labels are candidate research labels only, not production filters.",
    ]
    LATEST_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    generated_at = now_text()
    detail = build_detail(generated_at)
    summary = build_summary(detail, generated_at)
    context = build_context_summary(detail, generated_at)
    write_outputs(detail, summary, context)
    print(
        "structured neckline auto context expansion audit built "
        f"detail_rows={len(detail)} summary_rows={len(summary)} context_rows={len(context)}"
    )
    print(f"latest_detail={LATEST_DETAIL_CSV.as_posix()}")
    print(f"latest_summary={LATEST_SUMMARY_CSV.as_posix()}")
    print(f"latest_context={LATEST_CONTEXT_CSV.as_posix()}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
