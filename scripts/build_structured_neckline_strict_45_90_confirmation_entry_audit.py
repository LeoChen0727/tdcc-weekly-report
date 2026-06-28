from __future__ import annotations

from datetime import datetime
from pathlib import Path
from typing import Any
from zoneinfo import ZoneInfo
import math

import pandas as pd

from build_structured_neckline_strict_45_90_follow_through_audit import (
    FOLLOW_THROUGH_SCOPE_ID as SOURCE_FOLLOW_THROUGH_SCOPE_ID,
    FOLLOW_THROUGH_THRESHOLDS,
    LATEST_EVENT_CSV as SOURCE_EVENT_CSV,
    PARAMETER_SET_ID as SOURCE_PARAMETER_SET_ID,
    RESEARCH_ID as SOURCE_RESEARCH_ID,
    WINDOW_SESSIONS,
)
from build_structured_neckline_strict_45_90_review_packet import (
    FORBIDDEN_PRODUCTION_FIELDS,
    PRODUCTION_READINESS,
    RESEARCH_VARIANT_ID,
    TARGET_RISK_RULE_ID,
    TARGET_SEGMENT_ID,
    metric_text,
    normalize_code,
    normalize_date,
    read_price,
    safe_str,
)


ROOT = Path(__file__).resolve().parents[1]
RESEARCH_LATEST_DIR = ROOT / "output" / "latest" / "research_backtest"
RESEARCH_HISTORY_DIR = ROOT / "output" / "history" / "research"

RESEARCH_ID = "structured_neckline_strict_45_90_confirmation_entry_audit"
PARAMETER_SET_ID = "structured_neckline_strict_45_90_confirmation_entry_audit_20260629"
CONFIRMATION_SCOPE_ID = "follow_through_close_confirmation_next_open_grid"
EXIT_RULE_ID = "tp10_close_win_5pct_pullback_neutral_else_20d_close_loss"
MAX_HOLDING_SESSIONS = 20

LATEST_DETAIL_CSV = RESEARCH_LATEST_DIR / "structured_neckline_strict_45_90_confirmation_entry_detail_latest.csv"
LATEST_SUMMARY_CSV = RESEARCH_LATEST_DIR / "structured_neckline_strict_45_90_confirmation_entry_summary_latest.csv"
LATEST_MD = RESEARCH_LATEST_DIR / "structured_neckline_strict_45_90_confirmation_entry_latest.md"
HISTORY_DETAIL_CSV = RESEARCH_HISTORY_DIR / "structured_neckline_strict_45_90_confirmation_entry_detail.csv"
HISTORY_SUMMARY_CSV = RESEARCH_HISTORY_DIR / "structured_neckline_strict_45_90_confirmation_entry_summary.csv"

DETAIL_COLUMNS = [
    "research_id",
    "source_research_id",
    "source_parameter_set_id",
    "research_variant_id",
    "parameter_set_id",
    "advisory_status",
    "confirmation_scope_id",
    "source_follow_through_scope_id",
    "risk_penalty_rule_id",
    "segment_id",
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
    "diagnostic_note",
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
    "confirmation_rule_id",
    "max_window_sessions",
    "min_follow_through_pct",
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


def rule_id(sessions: int, threshold: float) -> str:
    return f"close_ge_{threshold_key(threshold)}pct_within_{sessions}_sessions_next_open"


def source_events() -> pd.DataFrame:
    events = read_csv(SOURCE_EVENT_CSV)
    required = {
        "research_id",
        "parameter_set_id",
        "follow_through_scope_id",
        "risk_penalty_rule_id",
        "segment_id",
        "stock_id",
        "stock_name",
        "signal_date",
        "retest_entry_date",
        "entry_price",
        "return_pct",
        "outcome_result",
        "follow_through_data_status",
    }
    for sessions in WINDOW_SESSIONS:
        required.add(f"max_close_return_{sessions}_session_pct")
    for threshold in FOLLOW_THROUGH_THRESHOLDS:
        key = threshold_key(threshold)
        required.add(f"first_close_ge_{key}pct_session")
        required.add(f"first_close_ge_{key}pct_date")
    missing = sorted(required - set(events.columns))
    if missing:
        raise SystemExit(f"ERROR: follow-through source missing columns: {missing}")
    forbidden = sorted(set(events.columns) & FORBIDDEN_PRODUCTION_FIELDS)
    if forbidden:
        raise SystemExit(f"ERROR: follow-through source contains forbidden production fields: {forbidden}")
    events = events[
        events["research_id"].astype(str).eq(SOURCE_RESEARCH_ID)
        & events["parameter_set_id"].astype(str).eq(SOURCE_PARAMETER_SET_ID)
        & events["follow_through_scope_id"].astype(str).eq(SOURCE_FOLLOW_THROUGH_SCOPE_ID)
        & events["risk_penalty_rule_id"].astype(str).eq(TARGET_RISK_RULE_ID)
        & events["segment_id"].astype(str).eq(TARGET_SEGMENT_ID)
    ].copy()
    if len(events) != 48:
        raise SystemExit(f"ERROR: expected 48 follow-through source rows; got {len(events)}")
    events["stock_id"] = events["stock_id"].map(normalize_code)
    return events


def price_index_for_date(price: pd.DataFrame, date: Any) -> int | None:
    date_text = normalize_date(date)
    matches = price.index[price["date"].astype(str).eq(date_text)].tolist()
    return int(matches[0]) if matches else None


def return_from_entry(close_value: Any, entry_price: float) -> float:
    close_price = to_float(close_value)
    if math.isnan(close_price) or math.isnan(entry_price) or entry_price <= 0:
        return math.nan
    return (close_price / entry_price - 1.0) * 100.0


def simulate_confirmation_trade(row: pd.Series, confirmation_signal_date: str) -> dict[str, str]:
    stock_id = normalize_code(row.get("stock_id"))
    price = read_price(stock_id)
    if price.empty:
        return {"tradability_status": "missing_price_history_file"}
    signal_idx = price_index_for_date(price, confirmation_signal_date)
    if signal_idx is None:
        return {"tradability_status": "confirmation_signal_date_missing"}
    entry_idx = signal_idx + 1
    if entry_idx >= len(price):
        return {"tradability_status": "missing_next_open_after_confirmation"}
    end_idx = min(len(price), entry_idx + MAX_HOLDING_SESSIONS)
    window = price.iloc[entry_idx:end_idx].copy().reset_index(drop=True)
    if len(window) < MAX_HOLDING_SESSIONS:
        return {"tradability_status": "insufficient_exit_window"}
    entry_price = to_float(window.iloc[0].get("open"))
    if math.isnan(entry_price) or entry_price <= 0:
        return {"tradability_status": "invalid_confirmation_entry_price"}
    close_returns = [return_from_entry(value, entry_price) for value in window["close"].tolist()]
    hit5 = False
    exit_idx = len(window) - 1
    outcome = "loss"
    exit_reason = "fixed_20d_close_without_tp10_or_neutral"
    for idx, value in enumerate(close_returns):
        if value >= 10.0:
            exit_idx = idx
            outcome = "win"
            exit_reason = "close_tp10_hit"
            break
        if value >= 5.0:
            hit5 = True
        elif hit5 and value <= 5.0:
            exit_idx = idx
            outcome = "neutral"
            exit_reason = "pulled_back_to_5pct_after_plus5_without_tp10"
            break
    exit_row = window.iloc[exit_idx]
    exit_price = to_float(exit_row.get("close"))
    return {
        "tradability_status": "tradable",
        "confirmation_entry_date": safe_str(window.iloc[0].get("date")),
        "confirmation_entry_price": metric_text(entry_price),
        "exit_date": safe_str(exit_row.get("date")),
        "exit_price": metric_text(exit_price),
        "holding_sessions": str(exit_idx + 1),
        "return_pct": metric_text(close_returns[exit_idx]),
        "max_close_return_pct": metric_text(max(close_returns[: exit_idx + 1])),
        "min_close_return_pct": metric_text(min(close_returns[: exit_idx + 1])),
        "outcome_result": outcome,
        "exit_reason": exit_reason,
    }


def build_detail(generated_at: str) -> pd.DataFrame:
    events = source_events()
    rows: list[dict[str, str]] = []
    for sessions in WINDOW_SESSIONS:
        for threshold in FOLLOW_THROUGH_THRESHOLDS:
            key = threshold_key(threshold)
            max_column = f"max_close_return_{sessions}_session_pct"
            hit_session_column = f"first_close_ge_{key}pct_session"
            hit_date_column = f"first_close_ge_{key}pct_date"
            for _, item in events.iterrows():
                max_value = to_float(item.get(max_column))
                hit_session = safe_str(item.get(hit_session_column))
                if math.isnan(max_value) or max_value < threshold or not hit_session or int(float(hit_session)) > sessions:
                    continue
                confirmation_signal_date = normalize_date(item.get(hit_date_column))
                trade = simulate_confirmation_trade(item, confirmation_signal_date)
                base = {
                    "research_id": RESEARCH_ID,
                    "source_research_id": SOURCE_RESEARCH_ID,
                    "source_parameter_set_id": SOURCE_PARAMETER_SET_ID,
                    "research_variant_id": RESEARCH_VARIANT_ID,
                    "parameter_set_id": PARAMETER_SET_ID,
                    "advisory_status": RESEARCH_VARIANT_ID,
                    "confirmation_scope_id": CONFIRMATION_SCOPE_ID,
                    "source_follow_through_scope_id": SOURCE_FOLLOW_THROUGH_SCOPE_ID,
                    "risk_penalty_rule_id": TARGET_RISK_RULE_ID,
                    "segment_id": TARGET_SEGMENT_ID,
                    "confirmation_rule_id": rule_id(sessions, threshold),
                    "max_window_sessions": str(sessions),
                    "min_follow_through_pct": metric_text(threshold),
                    "stock_id": normalize_code(item.get("stock_id")),
                    "stock_name": safe_str(item.get("stock_name")),
                    "signal_date": normalize_date(item.get("signal_date")),
                    "original_retest_entry_date": normalize_date(item.get("retest_entry_date")),
                    "original_entry_price": format_float(item.get("entry_price")),
                    "original_outcome_result": safe_str(item.get("outcome_result")),
                    "original_return_pct": format_float(item.get("return_pct")),
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
                    "diagnostic_note": "tradable_confirmation_next_open_research_only",
                    "approved_for_daily": "false",
                    "production_readiness": PRODUCTION_READINESS,
                    "generated_at": generated_at,
                }
                rows.append(base)
    detail = pd.DataFrame(rows)
    for column in DETAIL_COLUMNS:
        if column not in detail.columns:
            detail[column] = ""
    forbidden = sorted(set(detail.columns) & FORBIDDEN_PRODUCTION_FIELDS)
    if forbidden:
        raise SystemExit(f"ERROR: confirmation detail contains forbidden production fields: {forbidden}")
    return detail[DETAIL_COLUMNS]


def source_accepted_count(events: pd.DataFrame, sessions: int, threshold: float) -> int:
    values = pd.to_numeric(events[f"max_close_return_{sessions}_session_pct"], errors="coerce")
    return int(values.ge(threshold).sum())


def summary_row(detail: pd.DataFrame, events: pd.DataFrame, sessions: int, threshold: float, generated_at: str) -> dict[str, str]:
    rid = rule_id(sessions, threshold)
    group = detail[detail["confirmation_rule_id"].astype(str).eq(rid)].copy()
    tradable = group[group["tradability_status"].astype(str).eq("tradable")].copy()
    outcomes = tradable["outcome_result"].astype(str)
    win = int(outcomes.eq("win").sum())
    neutral = int(outcomes.eq("neutral").sum())
    loss = int(outcomes.eq("loss").sum())
    mature = win + loss
    evaluated = win + neutral + loss
    returns = pd.to_numeric(tradable["return_pct"], errors="coerce")
    max_returns = pd.to_numeric(tradable["max_close_return_pct"], errors="coerce")
    min_returns = pd.to_numeric(tradable["min_close_return_pct"], errors="coerce")
    return {
        "research_id": RESEARCH_ID,
        "research_variant_id": RESEARCH_VARIANT_ID,
        "parameter_set_id": PARAMETER_SET_ID,
        "advisory_status": RESEARCH_VARIANT_ID,
        "confirmation_scope_id": CONFIRMATION_SCOPE_ID,
        "confirmation_rule_id": rid,
        "max_window_sessions": str(sessions),
        "min_follow_through_pct": metric_text(threshold),
        "source_accepted_count": str(source_accepted_count(events, sessions, threshold)),
        "tradable_entry_count": str(len(tradable)),
        "incomplete_count": str(len(group) - len(tradable)),
        "win_count": str(win),
        "neutral_count": str(neutral),
        "loss_count": str(loss),
        "pure_win_rate_pct": pct_text(win, mature),
        "neutral_inclusive_success_rate_pct": pct_text(win + neutral, evaluated),
        "avg_return_pct": metric_text(float(returns.mean())) if returns.notna().any() else "",
        "median_return_pct": metric_text(float(returns.median())) if returns.notna().any() else "",
        "avg_max_close_return_pct": metric_text(float(max_returns.mean())) if max_returns.notna().any() else "",
        "avg_min_close_return_pct": metric_text(float(min_returns.mean())) if min_returns.notna().any() else "",
        "interpretation": "confirmation_next_open_research_only_not_production_ready",
        "approved_for_daily": "false",
        "production_readiness": PRODUCTION_READINESS,
        "generated_at": generated_at,
    }


def build_summary(detail: pd.DataFrame, generated_at: str) -> pd.DataFrame:
    events = source_events()
    rows = [
        summary_row(detail, events, sessions=sessions, threshold=threshold, generated_at=generated_at)
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


def write_markdown(detail: pd.DataFrame, summary: pd.DataFrame, generated_at: str) -> None:
    top = summary.copy()
    top["_success"] = pd.to_numeric(top["neutral_inclusive_success_rate_pct"], errors="coerce")
    top["_sample"] = pd.to_numeric(top["tradable_entry_count"], errors="coerce")
    top = top.sort_values(["_success", "_sample"], ascending=[False, False]).drop(columns=["_success", "_sample"])
    lines = [
        "# Structured Neckline Strict 45/90 Confirmation Entry Audit",
        "",
        f"- generated_at: `{generated_at}`",
        f"- research_id: `{RESEARCH_ID}`",
        f"- source_research_id: `{SOURCE_RESEARCH_ID}`",
        f"- source_parameter_set_id: `{SOURCE_PARAMETER_SET_ID}`",
        f"- confirmation_scope_id: `{CONFIRMATION_SCOPE_ID}`",
        f"- exit_rule_id: `{EXIT_RULE_ID}`",
        f"- max_holding_sessions: `{MAX_HOLDING_SESSIONS}`",
        f"- detail_rows: `{len(detail)}`",
        f"- advisory_status: `{RESEARCH_VARIANT_ID}`",
        f"- production_readiness: `{PRODUCTION_READINESS}`",
        "- production impact: `none`; this audit does not update production model conditions, scoring, ranking, PDF logic, or baseline.",
        "",
        "## Boundary",
        "",
        "This is a tradable follow-through hypothesis because entry is the next open after the confirmation close is already known. It is still research-only and not a production promotion.",
        "",
        "## Summary",
        "",
        *markdown_table(
            top,
            [
                "confirmation_rule_id",
                "source_accepted_count",
                "tradable_entry_count",
                "win_count",
                "neutral_count",
                "loss_count",
                "neutral_inclusive_success_rate_pct",
                "avg_return_pct",
                "interpretation",
            ],
            limit=40,
        ),
    ]
    LATEST_MD.parent.mkdir(parents=True, exist_ok=True)
    LATEST_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    generated_at = now_text()
    detail = build_detail(generated_at)
    summary = build_summary(detail, generated_at)
    write_csv(detail, LATEST_DETAIL_CSV)
    write_csv(summary, LATEST_SUMMARY_CSV)
    write_csv(detail, HISTORY_DETAIL_CSV)
    write_csv(summary, HISTORY_SUMMARY_CSV)
    write_markdown(detail, summary, generated_at)
    print(f"Saved: {LATEST_DETAIL_CSV} rows={len(detail)}")
    print(f"Saved: {LATEST_SUMMARY_CSV} rows={len(summary)}")
    print(f"Saved: {LATEST_MD}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
