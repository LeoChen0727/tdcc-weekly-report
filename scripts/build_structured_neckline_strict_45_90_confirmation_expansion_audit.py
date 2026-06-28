from __future__ import annotations

from datetime import datetime
from pathlib import Path
from typing import Any, Callable
from zoneinfo import ZoneInfo
import math

import pandas as pd

from build_structured_neckline_dual_window_risk_penalty_audit import (
    LATEST_DETAIL_CSV as SOURCE_RISK_DETAIL_CSV,
    PARAMETER_SET_ID as SOURCE_RISK_PARAMETER_SET_ID,
    RESEARCH_ID as SOURCE_RISK_RESEARCH_ID,
)
from build_structured_neckline_strict_45_90_confirmation_entry_audit import (
    EXIT_RULE_ID,
    MAX_HOLDING_SESSIONS,
    simulate_confirmation_trade,
)
from build_structured_neckline_strict_45_90_follow_through_audit import (
    FOLLOW_THROUGH_THRESHOLDS,
    WINDOW_SESSIONS,
)
from build_structured_neckline_strict_45_90_review_packet import (
    FORBIDDEN_PRODUCTION_FIELDS,
    PRODUCTION_READINESS,
    RESEARCH_VARIANT_ID,
    TARGET_RISK_RULE_ID,
    metric_text,
    normalize_code,
    normalize_date,
    read_price,
    safe_str,
)


ROOT = Path(__file__).resolve().parents[1]
RESEARCH_LATEST_DIR = ROOT / "output" / "latest" / "research_backtest"
RESEARCH_HISTORY_DIR = ROOT / "output" / "history" / "research"

RESEARCH_ID = "structured_neckline_strict_45_90_confirmation_expansion_audit"
PARAMETER_SET_ID = "structured_neckline_strict_45_90_confirmation_expansion_audit_20260629"
CONFIRMATION_SCOPE_ID = "strict_45_90_all_sample_confirmation_next_open_expansion"

LATEST_EVENT_CSV = RESEARCH_LATEST_DIR / "structured_neckline_strict_45_90_confirmation_expansion_events_latest.csv"
LATEST_DETAIL_CSV = RESEARCH_LATEST_DIR / "structured_neckline_strict_45_90_confirmation_expansion_detail_latest.csv"
LATEST_SUMMARY_CSV = RESEARCH_LATEST_DIR / "structured_neckline_strict_45_90_confirmation_expansion_summary_latest.csv"
LATEST_MD = RESEARCH_LATEST_DIR / "structured_neckline_strict_45_90_confirmation_expansion_latest.md"
HISTORY_EVENT_CSV = RESEARCH_HISTORY_DIR / "structured_neckline_strict_45_90_confirmation_expansion_events.csv"
HISTORY_DETAIL_CSV = RESEARCH_HISTORY_DIR / "structured_neckline_strict_45_90_confirmation_expansion_detail.csv"
HISTORY_SUMMARY_CSV = RESEARCH_HISTORY_DIR / "structured_neckline_strict_45_90_confirmation_expansion_summary.csv"

EVENT_COLUMNS = [
    "research_id",
    "source_research_id",
    "source_parameter_set_id",
    "research_variant_id",
    "parameter_set_id",
    "advisory_status",
    "confirmation_scope_id",
    "risk_penalty_rule_id",
    "source_event_key",
    "event_family_id",
    "source_segment_id",
    "stock_id",
    "stock_name",
    "signal_date",
    "retest_date",
    "retest_attack_date",
    "retest_entry_date",
    "entry_price",
    "original_exit_date",
    "original_return_pct",
    "original_max_close_return_pct",
    "original_min_close_return_pct",
    "original_outcome_result",
    "market_regime",
    "low_position_120_pct",
    "base_width_pct",
    "support_touch_count",
    "in_low_position_le60_market_bull",
    "follow_through_data_status",
    "follow_through_unavailable_reason",
    "max_close_return_1_session_pct",
    "max_close_return_2_session_pct",
    "max_close_return_3_session_pct",
    "max_close_return_5_session_pct",
    "first_close_ge_1pct_session",
    "first_close_ge_1pct_date",
    "first_close_ge_2pct_session",
    "first_close_ge_2pct_date",
    "first_close_ge_3pct_session",
    "first_close_ge_3pct_date",
    "first_close_ge_5pct_session",
    "first_close_ge_5pct_date",
    "analysis_scope_ids",
    "approved_for_daily",
    "production_readiness",
    "generated_at",
]

DETAIL_COLUMNS = [
    "research_id",
    "source_research_id",
    "source_parameter_set_id",
    "research_variant_id",
    "parameter_set_id",
    "advisory_status",
    "confirmation_scope_id",
    "risk_penalty_rule_id",
    "source_event_key",
    "confirmation_rule_id",
    "max_window_sessions",
    "min_follow_through_pct",
    "stock_id",
    "stock_name",
    "signal_date",
    "original_retest_entry_date",
    "original_entry_price",
    "original_outcome_result",
    "original_return_pct",
    "market_regime",
    "in_low_position_le60_market_bull",
    "confirmation_signal_date",
    "confirmation_signal_session",
    "confirmation_entry_date",
    "confirmation_entry_price",
    "exit_date",
    "exit_price",
    "holding_sessions",
    "return_pct",
    "max_close_return_pct",
    "min_close_return_pct",
    "outcome_result",
    "exit_reason",
    "tradability_status",
    "analysis_scope_ids",
    "approved_for_daily",
    "production_readiness",
    "generated_at",
]

SUMMARY_COLUMNS = [
    "research_id",
    "research_variant_id",
    "parameter_set_id",
    "advisory_status",
    "confirmation_scope_id",
    "analysis_scope_id",
    "confirmation_rule_id",
    "max_window_sessions",
    "min_follow_through_pct",
    "scope_event_count",
    "data_available_count",
    "source_accepted_count",
    "tradable_entry_count",
    "incomplete_count",
    "win_count",
    "neutral_count",
    "loss_count",
    "pure_win_rate_pct",
    "neutral_inclusive_success_rate_pct",
    "avg_return_pct",
    "median_return_pct",
    "avg_max_close_return_pct",
    "avg_min_close_return_pct",
    "sample_status",
    "interpretation",
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
        text = safe_str(value)
        if not text:
            return math.nan
        return float(text)
    except (TypeError, ValueError):
        return math.nan


def format_float(value: Any) -> str:
    return metric_text(to_float(value))


def pct_text(numerator: int | float, denominator: int | float) -> str:
    if denominator == 0:
        return ""
    return f"{float(numerator) / float(denominator) * 100.0:.4f}"


def threshold_key(threshold: float) -> str:
    return str(threshold).replace(".", "p").rstrip("0").rstrip("p")


def confirmation_rule_id(sessions: int, threshold: float) -> str:
    return f"close_ge_{threshold_key(threshold)}pct_within_{sessions}_sessions_next_open"


def source_rows() -> pd.DataFrame:
    source = read_csv(SOURCE_RISK_DETAIL_CSV)
    required = {
        "research_id",
        "parameter_set_id",
        "research_variant_id",
        "advisory_status",
        "risk_penalty_rule_id",
        "risk_penalty_candidate_accept",
        "source_event_key",
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
        "entry_price",
        "exit_date",
        "return_pct",
        "max_close_return_pct",
        "min_close_return_pct",
        "outcome_result",
        "approved_for_daily",
        "production_readiness",
    }
    missing = sorted(required - set(source.columns))
    if missing:
        raise SystemExit(f"ERROR: source risk detail missing columns: {missing}")
    forbidden = sorted(set(source.columns) & FORBIDDEN_PRODUCTION_FIELDS)
    if forbidden:
        raise SystemExit(f"ERROR: source risk detail contains forbidden production fields: {forbidden}")
    rows = source[
        source["research_id"].astype(str).eq(SOURCE_RISK_RESEARCH_ID)
        & source["parameter_set_id"].astype(str).eq(SOURCE_RISK_PARAMETER_SET_ID)
        & source["risk_penalty_rule_id"].astype(str).eq(TARGET_RISK_RULE_ID)
        & source["risk_penalty_candidate_accept"].astype(str).str.lower().eq("true")
    ].copy()
    if len(rows) != 313:
        raise SystemExit(f"ERROR: expected 313 strict 45/90 accepted rows; got {len(rows)}")
    rows["stock_id"] = rows["stock_id"].map(normalize_code)
    if rows["source_event_key"].duplicated().any():
        duplicated = rows.loc[rows["source_event_key"].duplicated(), "source_event_key"].head(5).tolist()
        raise SystemExit(f"ERROR: duplicate source_event_key rows: {duplicated}")
    return rows.sort_values(["signal_date", "stock_id"]).reset_index(drop=True)


def price_index_for_date(price: pd.DataFrame, date: Any) -> int | None:
    date_text = normalize_date(date)
    matches = price.index[price["date"].astype(str).eq(date_text)].tolist()
    return int(matches[0]) if matches else None


def return_from_entry(close_value: Any, entry_price: float) -> float:
    close_price = to_float(close_value)
    if math.isnan(close_price) or math.isnan(entry_price) or entry_price <= 0:
        return math.nan
    return (close_price / entry_price - 1.0) * 100.0


def follow_through_metrics(row: pd.Series) -> dict[str, Any]:
    stock_id = normalize_code(row.get("stock_id"))
    price = read_price(stock_id)
    if price.empty:
        return unavailable_metrics("missing_price_history_file")
    entry_idx = price_index_for_date(price, row.get("retest_entry_date"))
    if entry_idx is None:
        return unavailable_metrics("entry_date_missing_from_stock_price_history")
    end_idx = min(len(price), entry_idx + max(WINDOW_SESSIONS))
    window = price.iloc[entry_idx:end_idx].copy().reset_index(drop=True)
    if len(window) < max(WINDOW_SESSIONS):
        return unavailable_metrics("insufficient_post_entry_price_window")
    entry_price = to_float(row.get("entry_price"))
    returns = [return_from_entry(value, entry_price) for value in window["close"].tolist()]
    metrics: dict[str, Any] = {
        "follow_through_data_status": "available",
        "follow_through_unavailable_reason": "",
    }
    for sessions in WINDOW_SESSIONS:
        values = returns[:sessions]
        metrics[f"max_close_return_{sessions}_session_pct"] = max(values) if values else math.nan
    for threshold in FOLLOW_THROUGH_THRESHOLDS:
        hit_session = ""
        hit_date = ""
        for idx, value in enumerate(returns, start=1):
            if value >= threshold:
                hit_session = str(idx)
                hit_date = safe_str(window.iloc[idx - 1].get("date"))
                break
        key = threshold_key(threshold)
        metrics[f"first_close_ge_{key}pct_session"] = hit_session
        metrics[f"first_close_ge_{key}pct_date"] = hit_date
    return metrics


def unavailable_metrics(reason: str) -> dict[str, Any]:
    metrics: dict[str, Any] = {
        "follow_through_data_status": "unavailable",
        "follow_through_unavailable_reason": reason,
    }
    for sessions in WINDOW_SESSIONS:
        metrics[f"max_close_return_{sessions}_session_pct"] = math.nan
    for threshold in FOLLOW_THROUGH_THRESHOLDS:
        key = threshold_key(threshold)
        metrics[f"first_close_ge_{key}pct_session"] = ""
        metrics[f"first_close_ge_{key}pct_date"] = ""
    return metrics


def scope_ids_for(row: pd.Series) -> list[str]:
    scopes = ["all_strict_45_90"]
    market_regime = safe_str(row.get("market_regime")) or "unknown"
    scopes.append(f"market_regime_{market_regime}")
    if safe_str(row.get("in_low_position_le60_market_bull")).lower() == "true":
        scopes.append("low_position_le60_market_bull")
    else:
        scopes.append("non_low_position_le60_market_bull")
    low_position = to_float(row.get("low_position_120_pct"))
    if not math.isnan(low_position) and low_position <= 60.0:
        scopes.append("low_position_le60_any_market")
    else:
        scopes.append("low_position_gt60_or_unknown")
    return scopes


def build_events(generated_at: str) -> pd.DataFrame:
    rows: list[dict[str, str]] = []
    for _, item in source_rows().iterrows():
        metrics = follow_through_metrics(item)
        row = {
            "research_id": RESEARCH_ID,
            "source_research_id": SOURCE_RISK_RESEARCH_ID,
            "source_parameter_set_id": SOURCE_RISK_PARAMETER_SET_ID,
            "research_variant_id": RESEARCH_VARIANT_ID,
            "parameter_set_id": PARAMETER_SET_ID,
            "advisory_status": RESEARCH_VARIANT_ID,
            "confirmation_scope_id": CONFIRMATION_SCOPE_ID,
            "risk_penalty_rule_id": TARGET_RISK_RULE_ID,
            "source_event_key": safe_str(item.get("source_event_key")),
            "event_family_id": safe_str(item.get("event_family_id")),
            "source_segment_id": safe_str(item.get("source_segment_id")),
            "stock_id": normalize_code(item.get("stock_id")),
            "stock_name": safe_str(item.get("stock_name")),
            "signal_date": normalize_date(item.get("signal_date")),
            "retest_date": normalize_date(item.get("retest_date")),
            "retest_attack_date": normalize_date(item.get("retest_attack_date")),
            "retest_entry_date": normalize_date(item.get("retest_entry_date")),
            "entry_price": format_float(item.get("entry_price")),
            "original_exit_date": normalize_date(item.get("exit_date")),
            "original_return_pct": format_float(item.get("return_pct")),
            "original_max_close_return_pct": format_float(item.get("max_close_return_pct")),
            "original_min_close_return_pct": format_float(item.get("min_close_return_pct")),
            "original_outcome_result": safe_str(item.get("outcome_result")),
            "market_regime": safe_str(item.get("market_regime")),
            "low_position_120_pct": format_float(item.get("low_position_120_pct")),
            "base_width_pct": format_float(item.get("base_width_pct")),
            "support_touch_count": safe_str(item.get("support_touch_count")),
            "in_low_position_le60_market_bull": safe_str(item.get("in_low_position_le60_market_bull")).lower(),
            "follow_through_data_status": safe_str(metrics.get("follow_through_data_status")),
            "follow_through_unavailable_reason": safe_str(metrics.get("follow_through_unavailable_reason")),
            "analysis_scope_ids": ";".join(scope_ids_for(item)),
            "approved_for_daily": "false",
            "production_readiness": PRODUCTION_READINESS,
            "generated_at": generated_at,
        }
        for sessions in WINDOW_SESSIONS:
            row[f"max_close_return_{sessions}_session_pct"] = metric_text(metrics[f"max_close_return_{sessions}_session_pct"])
        for threshold in FOLLOW_THROUGH_THRESHOLDS:
            key = threshold_key(threshold)
            row[f"first_close_ge_{key}pct_session"] = safe_str(metrics[f"first_close_ge_{key}pct_session"])
            row[f"first_close_ge_{key}pct_date"] = safe_str(metrics[f"first_close_ge_{key}pct_date"])
        rows.append(row)
    events = pd.DataFrame(rows)
    for column in EVENT_COLUMNS:
        if column not in events.columns:
            events[column] = ""
    forbidden = sorted(set(events.columns) & FORBIDDEN_PRODUCTION_FIELDS)
    if forbidden:
        raise SystemExit(f"ERROR: expansion events contain forbidden production fields: {forbidden}")
    return events[EVENT_COLUMNS]


def event_scope_set(row: pd.Series) -> set[str]:
    return {item for item in safe_str(row.get("analysis_scope_ids")).split(";") if item}


def build_detail(events: pd.DataFrame, generated_at: str) -> pd.DataFrame:
    rows: list[dict[str, str]] = []
    for _, item in events.iterrows():
        for sessions in WINDOW_SESSIONS:
            max_value = to_float(item.get(f"max_close_return_{sessions}_session_pct"))
            if math.isnan(max_value):
                continue
            for threshold in FOLLOW_THROUGH_THRESHOLDS:
                if max_value < threshold:
                    continue
                key = threshold_key(threshold)
                hit_session = safe_str(item.get(f"first_close_ge_{key}pct_session"))
                if not hit_session or int(float(hit_session)) > sessions:
                    continue
                confirmation_signal_date = normalize_date(item.get(f"first_close_ge_{key}pct_date"))
                trade = simulate_confirmation_trade(item, confirmation_signal_date)
                rows.append(
                    {
                        "research_id": RESEARCH_ID,
                        "source_research_id": SOURCE_RISK_RESEARCH_ID,
                        "source_parameter_set_id": SOURCE_RISK_PARAMETER_SET_ID,
                        "research_variant_id": RESEARCH_VARIANT_ID,
                        "parameter_set_id": PARAMETER_SET_ID,
                        "advisory_status": RESEARCH_VARIANT_ID,
                        "confirmation_scope_id": CONFIRMATION_SCOPE_ID,
                        "risk_penalty_rule_id": TARGET_RISK_RULE_ID,
                        "source_event_key": safe_str(item.get("source_event_key")),
                        "confirmation_rule_id": confirmation_rule_id(sessions, threshold),
                        "max_window_sessions": str(sessions),
                        "min_follow_through_pct": metric_text(threshold),
                        "stock_id": normalize_code(item.get("stock_id")),
                        "stock_name": safe_str(item.get("stock_name")),
                        "signal_date": normalize_date(item.get("signal_date")),
                        "original_retest_entry_date": normalize_date(item.get("retest_entry_date")),
                        "original_entry_price": format_float(item.get("entry_price")),
                        "original_outcome_result": safe_str(item.get("original_outcome_result")),
                        "original_return_pct": format_float(item.get("original_return_pct")),
                        "market_regime": safe_str(item.get("market_regime")),
                        "in_low_position_le60_market_bull": safe_str(item.get("in_low_position_le60_market_bull")).lower(),
                        "confirmation_signal_date": confirmation_signal_date,
                        "confirmation_signal_session": hit_session,
                        "confirmation_entry_date": safe_str(trade.get("confirmation_entry_date")),
                        "confirmation_entry_price": safe_str(trade.get("confirmation_entry_price")),
                        "exit_date": safe_str(trade.get("exit_date")),
                        "exit_price": safe_str(trade.get("exit_price")),
                        "holding_sessions": safe_str(trade.get("holding_sessions")),
                        "return_pct": safe_str(trade.get("return_pct")),
                        "max_close_return_pct": safe_str(trade.get("max_close_return_pct")),
                        "min_close_return_pct": safe_str(trade.get("min_close_return_pct")),
                        "outcome_result": safe_str(trade.get("outcome_result")),
                        "exit_reason": safe_str(trade.get("exit_reason")),
                        "tradability_status": safe_str(trade.get("tradability_status")),
                        "analysis_scope_ids": safe_str(item.get("analysis_scope_ids")),
                        "approved_for_daily": "false",
                        "production_readiness": PRODUCTION_READINESS,
                        "generated_at": generated_at,
                    }
                )
    detail = pd.DataFrame(rows)
    for column in DETAIL_COLUMNS:
        if column not in detail.columns:
            detail[column] = ""
    forbidden = sorted(set(detail.columns) & FORBIDDEN_PRODUCTION_FIELDS)
    if forbidden:
        raise SystemExit(f"ERROR: expansion detail contains forbidden production fields: {forbidden}")
    return detail[DETAIL_COLUMNS]


def analysis_scopes(events: pd.DataFrame) -> list[str]:
    scopes = sorted({scope for _, row in events.iterrows() for scope in event_scope_set(row)})
    preferred = [
        "all_strict_45_90",
        "low_position_le60_market_bull",
        "non_low_position_le60_market_bull",
        "low_position_le60_any_market",
        "low_position_gt60_or_unknown",
        "market_regime_strong_bull",
        "market_regime_mild_bull",
        "market_regime_range_or_mixed",
        "market_regime_correction",
    ]
    return [scope for scope in preferred if scope in scopes] + [scope for scope in scopes if scope not in preferred]


def has_scope(frame: pd.DataFrame, scope_id: str) -> pd.Series:
    return frame["analysis_scope_ids"].astype(str).str.split(";").apply(lambda parts: scope_id in parts)


def summary_row(events: pd.DataFrame, detail: pd.DataFrame, scope_id: str, sessions: int, threshold: float, generated_at: str) -> dict[str, str]:
    rid = confirmation_rule_id(sessions, threshold)
    scoped_events = events[has_scope(events, scope_id)].copy()
    available_events = scoped_events[scoped_events["follow_through_data_status"].astype(str).eq("available")]
    event_values = pd.to_numeric(scoped_events[f"max_close_return_{sessions}_session_pct"], errors="coerce")
    source_accepted_count = int(event_values.ge(threshold).sum())
    scoped_detail = detail[detail["confirmation_rule_id"].astype(str).eq(rid) & has_scope(detail, scope_id)].copy()
    tradable = scoped_detail[scoped_detail["tradability_status"].astype(str).eq("tradable")].copy()
    outcomes = tradable["outcome_result"].astype(str)
    win = int(outcomes.eq("win").sum())
    neutral = int(outcomes.eq("neutral").sum())
    loss = int(outcomes.eq("loss").sum())
    mature = win + loss
    evaluated = win + neutral + loss
    returns = pd.to_numeric(tradable["return_pct"], errors="coerce")
    max_returns = pd.to_numeric(tradable["max_close_return_pct"], errors="coerce")
    min_returns = pd.to_numeric(tradable["min_close_return_pct"], errors="coerce")
    if len(tradable) >= 60:
        sample_status = "reviewable_broader_sample"
    elif len(tradable) >= 30:
        sample_status = "reviewable_small_sample"
    elif len(tradable) > 0:
        sample_status = "thin_sample"
    else:
        sample_status = "no_tradable_rows"
    return {
        "research_id": RESEARCH_ID,
        "research_variant_id": RESEARCH_VARIANT_ID,
        "parameter_set_id": PARAMETER_SET_ID,
        "advisory_status": RESEARCH_VARIANT_ID,
        "confirmation_scope_id": CONFIRMATION_SCOPE_ID,
        "analysis_scope_id": scope_id,
        "confirmation_rule_id": rid,
        "max_window_sessions": str(sessions),
        "min_follow_through_pct": metric_text(threshold),
        "scope_event_count": str(len(scoped_events)),
        "data_available_count": str(len(available_events)),
        "source_accepted_count": str(source_accepted_count),
        "tradable_entry_count": str(len(tradable)),
        "incomplete_count": str(len(scoped_detail) - len(tradable)),
        "win_count": str(win),
        "neutral_count": str(neutral),
        "loss_count": str(loss),
        "pure_win_rate_pct": pct_text(win, mature),
        "neutral_inclusive_success_rate_pct": pct_text(win + neutral, evaluated),
        "avg_return_pct": metric_text(float(returns.mean())) if returns.notna().any() else "",
        "median_return_pct": metric_text(float(returns.median())) if returns.notna().any() else "",
        "avg_max_close_return_pct": metric_text(float(max_returns.mean())) if max_returns.notna().any() else "",
        "avg_min_close_return_pct": metric_text(float(min_returns.mean())) if min_returns.notna().any() else "",
        "sample_status": sample_status,
        "interpretation": "confirmation_next_open_expansion_research_only_not_production_ready",
        "approved_for_daily": "false",
        "production_readiness": PRODUCTION_READINESS,
        "generated_at": generated_at,
    }


def build_summary(events: pd.DataFrame, detail: pd.DataFrame, generated_at: str) -> pd.DataFrame:
    rows = [
        summary_row(events, detail, scope_id, sessions, threshold, generated_at)
        for scope_id in analysis_scopes(events)
        for sessions in WINDOW_SESSIONS
        for threshold in FOLLOW_THROUGH_THRESHOLDS
    ]
    summary = pd.DataFrame(rows)
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


def write_markdown(events: pd.DataFrame, detail: pd.DataFrame, summary: pd.DataFrame, generated_at: str) -> None:
    top = summary[summary["analysis_scope_id"].isin(["all_strict_45_90", "low_position_le60_market_bull", "non_low_position_le60_market_bull"])].copy()
    top["_sample"] = pd.to_numeric(top["tradable_entry_count"], errors="coerce")
    top["_success"] = pd.to_numeric(top["neutral_inclusive_success_rate_pct"], errors="coerce")
    top = top.sort_values(["analysis_scope_id", "_success", "_sample"], ascending=[True, False, False]).drop(columns=["_sample", "_success"])
    lines = [
        "# Structured Neckline Strict 45/90 Confirmation Expansion Audit",
        "",
        f"- generated_at: `{generated_at}`",
        f"- research_id: `{RESEARCH_ID}`",
        f"- source_research_id: `{SOURCE_RISK_RESEARCH_ID}`",
        f"- source_parameter_set_id: `{SOURCE_RISK_PARAMETER_SET_ID}`",
        f"- confirmation_scope_id: `{CONFIRMATION_SCOPE_ID}`",
        f"- source_events: `{len(events)}`",
        f"- detail_rows: `{len(detail)}`",
        f"- exit_rule_id: `{EXIT_RULE_ID}`",
        f"- max_holding_sessions: `{MAX_HOLDING_SESSIONS}`",
        f"- advisory_status: `{RESEARCH_VARIANT_ID}`",
        f"- production_readiness: `{PRODUCTION_READINESS}`",
        "- production impact: `none`; this audit does not update production model conditions, scoring, ranking, PDF logic, or baseline.",
        "",
        "## Boundary",
        "",
        "This expands the strict 45/90 confirmation-next-open hypothesis from the 48-row low-position bull subset to all strict 45/90 accepted events. It remains research-only and is not a production promotion.",
        "",
        "## Key Scope Summary",
        "",
        *markdown_table(
            top,
            [
                "analysis_scope_id",
                "confirmation_rule_id",
                "scope_event_count",
                "tradable_entry_count",
                "win_count",
                "neutral_count",
                "loss_count",
                "neutral_inclusive_success_rate_pct",
                "avg_return_pct",
                "sample_status",
            ],
            limit=60,
        ),
    ]
    LATEST_MD.parent.mkdir(parents=True, exist_ok=True)
    LATEST_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    generated_at = now_text()
    events = build_events(generated_at)
    detail = build_detail(events, generated_at)
    summary = build_summary(events, detail, generated_at)
    write_csv(events, LATEST_EVENT_CSV)
    write_csv(detail, LATEST_DETAIL_CSV)
    write_csv(summary, LATEST_SUMMARY_CSV)
    write_csv(events, HISTORY_EVENT_CSV)
    write_csv(detail, HISTORY_DETAIL_CSV)
    write_csv(summary, HISTORY_SUMMARY_CSV)
    write_markdown(events, detail, summary, generated_at)
    print(f"Saved: {LATEST_EVENT_CSV} rows={len(events)}")
    print(f"Saved: {LATEST_DETAIL_CSV} rows={len(detail)}")
    print(f"Saved: {LATEST_SUMMARY_CSV} rows={len(summary)}")
    print(f"Saved: {LATEST_MD}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
