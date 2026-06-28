from __future__ import annotations

from datetime import datetime
from pathlib import Path
from typing import Any
from zoneinfo import ZoneInfo
import math

import pandas as pd

from build_structured_neckline_strict_45_90_review_packet import (
    FORBIDDEN_PRODUCTION_FIELDS,
    LATEST_INDEX_CSV as SOURCE_PACKET_CSV,
    PARAMETER_SET_ID as SOURCE_PACKET_PARAMETER_SET_ID,
    PRODUCTION_READINESS,
    RESEARCH_ID as SOURCE_PACKET_RESEARCH_ID,
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

RESEARCH_ID = "structured_neckline_strict_45_90_follow_through_audit"
PARAMETER_SET_ID = "structured_neckline_strict_45_90_follow_through_audit_20260629"
FOLLOW_THROUGH_SCOPE_ID = "post_entry_close_follow_through_diagnostic_grid"

LATEST_EVENT_CSV = RESEARCH_LATEST_DIR / "structured_neckline_strict_45_90_follow_through_latest.csv"
LATEST_SUMMARY_CSV = RESEARCH_LATEST_DIR / "structured_neckline_strict_45_90_follow_through_summary_latest.csv"
LATEST_MD = RESEARCH_LATEST_DIR / "structured_neckline_strict_45_90_follow_through_latest.md"
HISTORY_EVENT_CSV = RESEARCH_HISTORY_DIR / "structured_neckline_strict_45_90_follow_through.csv"
HISTORY_SUMMARY_CSV = RESEARCH_HISTORY_DIR / "structured_neckline_strict_45_90_follow_through_summary.csv"

WINDOW_SESSIONS = [1, 2, 3, 5]
FOLLOW_THROUGH_THRESHOLDS = [1.0, 2.0, 3.0, 5.0]

EVENT_COLUMNS = [
    "research_id",
    "source_research_id",
    "source_parameter_set_id",
    "research_variant_id",
    "parameter_set_id",
    "advisory_status",
    "follow_through_scope_id",
    "risk_penalty_rule_id",
    "segment_id",
    "stock_id",
    "stock_name",
    "signal_date",
    "retest_entry_date",
    "entry_price",
    "exit_date",
    "return_pct",
    "max_close_return_pct",
    "min_close_return_pct",
    "outcome_result",
    "follow_through_data_status",
    "follow_through_unavailable_reason",
    "close_return_1_session_pct",
    "close_return_2_session_pct",
    "close_return_3_session_pct",
    "close_return_5_session_pct",
    "max_close_return_1_session_pct",
    "max_close_return_2_session_pct",
    "max_close_return_3_session_pct",
    "max_close_return_5_session_pct",
    "min_close_return_1_session_pct",
    "min_close_return_2_session_pct",
    "min_close_return_3_session_pct",
    "min_close_return_5_session_pct",
    "first_close_ge_1pct_session",
    "first_close_ge_1pct_date",
    "first_close_ge_2pct_session",
    "first_close_ge_2pct_date",
    "first_close_ge_3pct_session",
    "first_close_ge_3pct_date",
    "first_close_ge_5pct_session",
    "first_close_ge_5pct_date",
    "weak_follow_through_5d_lt5pct",
    "weak_follow_through_3d_lt3pct",
    "early_adverse_3d_le_minus5pct",
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
    "follow_through_scope_id",
    "rule_id",
    "rule_type",
    "max_window_sessions",
    "min_follow_through_pct",
    "accepted_count",
    "rejected_count",
    "unavailable_count",
    "accepted_win_count",
    "accepted_neutral_count",
    "accepted_loss_count",
    "rejected_win_count",
    "rejected_neutral_count",
    "rejected_loss_count",
    "accepted_pure_win_rate_pct",
    "accepted_neutral_inclusive_success_rate_pct",
    "accepted_avg_return_pct",
    "rejected_avg_return_pct",
    "loss_rejection_rate_pct",
    "success_or_neutral_rejection_rate_pct",
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


def source_packet() -> pd.DataFrame:
    packet = read_csv(SOURCE_PACKET_CSV)
    required = {
        "research_id",
        "parameter_set_id",
        "research_variant_id",
        "advisory_status",
        "risk_penalty_rule_id",
        "segment_id",
        "stock_id",
        "stock_name",
        "signal_date",
        "retest_entry_date",
        "entry_price",
        "exit_date",
        "return_pct",
        "max_close_return_pct",
        "min_close_return_pct",
        "outcome_result",
        "approved_for_daily",
        "production_readiness",
    }
    missing = sorted(required - set(packet.columns))
    if missing:
        raise SystemExit(f"ERROR: source packet missing columns: {missing}")
    forbidden = sorted(set(packet.columns) & FORBIDDEN_PRODUCTION_FIELDS)
    if forbidden:
        raise SystemExit(f"ERROR: source packet contains forbidden production fields: {forbidden}")
    packet = packet[
        packet["research_id"].astype(str).eq(SOURCE_PACKET_RESEARCH_ID)
        & packet["parameter_set_id"].astype(str).eq(SOURCE_PACKET_PARAMETER_SET_ID)
        & packet["risk_penalty_rule_id"].astype(str).eq(TARGET_RISK_RULE_ID)
        & packet["segment_id"].astype(str).eq(TARGET_SEGMENT_ID)
    ].copy()
    if len(packet) != 48:
        raise SystemExit(f"ERROR: expected 48 strict 45/90 packet rows; got {len(packet)}")
    packet["stock_id"] = packet["stock_id"].map(normalize_code)
    return packet.sort_values(["outcome_result", "signal_date", "stock_id"]).reset_index(drop=True)


def price_window_after_entry(row: pd.Series, max_sessions: int) -> tuple[pd.DataFrame, str]:
    stock_id = normalize_code(row.get("stock_id"))
    price = read_price(stock_id)
    if price.empty:
        return pd.DataFrame(), "missing_price_history_file"
    entry_date = normalize_date(row.get("retest_entry_date"))
    matches = price.index[price["date"].astype(str).eq(entry_date)].tolist()
    if not matches:
        return pd.DataFrame(), "entry_date_missing_from_stock_price_history"
    start = int(matches[0])
    end = min(len(price), start + max_sessions)
    window = price.iloc[start:end].copy().reset_index(drop=True)
    if len(window) < max_sessions:
        return pd.DataFrame(), "insufficient_post_entry_price_window"
    return window, ""


def return_from_entry(close_value: Any, entry_price: float) -> float:
    close_price = to_float(close_value)
    if math.isnan(close_price) or math.isnan(entry_price) or entry_price <= 0:
        return math.nan
    return (close_price / entry_price - 1.0) * 100.0


def window_returns(row: pd.Series) -> dict[str, Any]:
    entry_price = to_float(row.get("entry_price"))
    window, unavailable_reason = price_window_after_entry(row, max(WINDOW_SESSIONS))
    if unavailable_reason:
        out: dict[str, Any] = {
            "follow_through_data_status": "unavailable",
            "follow_through_unavailable_reason": unavailable_reason,
        }
        for sessions in WINDOW_SESSIONS:
            out[f"close_return_{sessions}_session_pct"] = math.nan
            out[f"max_close_return_{sessions}_session_pct"] = math.nan
            out[f"min_close_return_{sessions}_session_pct"] = math.nan
        for threshold in FOLLOW_THROUGH_THRESHOLDS:
            key = str(threshold).replace(".", "p").rstrip("0").rstrip("p")
            out[f"first_close_ge_{key}pct_session"] = ""
            out[f"first_close_ge_{key}pct_date"] = ""
        out["weak_follow_through_5d_lt5pct"] = "unknown"
        out["weak_follow_through_3d_lt3pct"] = "unknown"
        out["early_adverse_3d_le_minus5pct"] = "unknown"
        return out
    close_returns = [return_from_entry(value, entry_price) for value in window["close"].tolist()]
    out = {
        "follow_through_data_status": "available",
        "follow_through_unavailable_reason": "",
    }
    for sessions in WINDOW_SESSIONS:
        values = close_returns[:sessions]
        out[f"close_return_{sessions}_session_pct"] = values[-1] if values else math.nan
        out[f"max_close_return_{sessions}_session_pct"] = max(values) if values else math.nan
        out[f"min_close_return_{sessions}_session_pct"] = min(values) if values else math.nan
    for threshold in FOLLOW_THROUGH_THRESHOLDS:
        hit_session = ""
        hit_date = ""
        for idx, value in enumerate(close_returns, start=1):
            if value >= threshold:
                hit_session = str(idx)
                hit_date = safe_str(window.iloc[idx - 1].get("date"))
                break
        key = str(threshold).replace(".", "p").rstrip("0").rstrip("p")
        out[f"first_close_ge_{key}pct_session"] = hit_session
        out[f"first_close_ge_{key}pct_date"] = hit_date
    out["weak_follow_through_5d_lt5pct"] = "true" if out["max_close_return_5_session_pct"] < 5.0 else "false"
    out["weak_follow_through_3d_lt3pct"] = "true" if out["max_close_return_3_session_pct"] < 3.0 else "false"
    out["early_adverse_3d_le_minus5pct"] = "true" if out["min_close_return_3_session_pct"] <= -5.0 else "false"
    return out


def build_events(generated_at: str) -> pd.DataFrame:
    source = source_packet()
    rows: list[dict[str, str]] = []
    for _, item in source.iterrows():
        metrics = window_returns(item)
        rows.append(
            {
                "research_id": RESEARCH_ID,
                "source_research_id": SOURCE_PACKET_RESEARCH_ID,
                "source_parameter_set_id": SOURCE_PACKET_PARAMETER_SET_ID,
                "research_variant_id": RESEARCH_VARIANT_ID,
                "parameter_set_id": PARAMETER_SET_ID,
                "advisory_status": RESEARCH_VARIANT_ID,
                "follow_through_scope_id": FOLLOW_THROUGH_SCOPE_ID,
                "risk_penalty_rule_id": TARGET_RISK_RULE_ID,
                "segment_id": TARGET_SEGMENT_ID,
                "stock_id": normalize_code(item.get("stock_id")),
                "stock_name": safe_str(item.get("stock_name")),
                "signal_date": normalize_date(item.get("signal_date")),
                "retest_entry_date": normalize_date(item.get("retest_entry_date")),
                "entry_price": format_float(item.get("entry_price")),
                "exit_date": normalize_date(item.get("exit_date")),
                "return_pct": format_float(item.get("return_pct")),
                "max_close_return_pct": format_float(item.get("max_close_return_pct")),
                "min_close_return_pct": format_float(item.get("min_close_return_pct")),
                "outcome_result": safe_str(item.get("outcome_result")),
                "follow_through_data_status": safe_str(metrics["follow_through_data_status"]),
                "follow_through_unavailable_reason": safe_str(metrics["follow_through_unavailable_reason"]),
                "close_return_1_session_pct": metric_text(metrics["close_return_1_session_pct"]),
                "close_return_2_session_pct": metric_text(metrics["close_return_2_session_pct"]),
                "close_return_3_session_pct": metric_text(metrics["close_return_3_session_pct"]),
                "close_return_5_session_pct": metric_text(metrics["close_return_5_session_pct"]),
                "max_close_return_1_session_pct": metric_text(metrics["max_close_return_1_session_pct"]),
                "max_close_return_2_session_pct": metric_text(metrics["max_close_return_2_session_pct"]),
                "max_close_return_3_session_pct": metric_text(metrics["max_close_return_3_session_pct"]),
                "max_close_return_5_session_pct": metric_text(metrics["max_close_return_5_session_pct"]),
                "min_close_return_1_session_pct": metric_text(metrics["min_close_return_1_session_pct"]),
                "min_close_return_2_session_pct": metric_text(metrics["min_close_return_2_session_pct"]),
                "min_close_return_3_session_pct": metric_text(metrics["min_close_return_3_session_pct"]),
                "min_close_return_5_session_pct": metric_text(metrics["min_close_return_5_session_pct"]),
                "first_close_ge_1pct_session": safe_str(metrics["first_close_ge_1pct_session"]),
                "first_close_ge_1pct_date": safe_str(metrics["first_close_ge_1pct_date"]),
                "first_close_ge_2pct_session": safe_str(metrics["first_close_ge_2pct_session"]),
                "first_close_ge_2pct_date": safe_str(metrics["first_close_ge_2pct_date"]),
                "first_close_ge_3pct_session": safe_str(metrics["first_close_ge_3pct_session"]),
                "first_close_ge_3pct_date": safe_str(metrics["first_close_ge_3pct_date"]),
                "first_close_ge_5pct_session": safe_str(metrics["first_close_ge_5pct_session"]),
                "first_close_ge_5pct_date": safe_str(metrics["first_close_ge_5pct_date"]),
                "weak_follow_through_5d_lt5pct": safe_str(metrics["weak_follow_through_5d_lt5pct"]),
                "weak_follow_through_3d_lt3pct": safe_str(metrics["weak_follow_through_3d_lt3pct"]),
                "early_adverse_3d_le_minus5pct": safe_str(metrics["early_adverse_3d_le_minus5pct"]),
                "diagnostic_note": "future_known_post_entry_diagnostic_not_original_entry_filter",
                "approved_for_daily": "false",
                "production_readiness": PRODUCTION_READINESS,
                "generated_at": generated_at,
            }
        )
    events = pd.DataFrame(rows)
    for column in EVENT_COLUMNS:
        if column not in events.columns:
            events[column] = ""
    forbidden = sorted(set(events.columns) & FORBIDDEN_PRODUCTION_FIELDS)
    if forbidden:
        raise SystemExit(f"ERROR: output contains forbidden production fields: {forbidden}")
    return events[EVENT_COLUMNS]


def summary_row(events: pd.DataFrame, sessions: int, threshold: float, generated_at: str) -> dict[str, str]:
    rule_id = f"max_close_ge_{str(threshold).replace('.', 'p').rstrip('0').rstrip('p')}pct_within_{sessions}_sessions"
    metric_column = f"max_close_return_{sessions}_session_pct"
    values = pd.to_numeric(events[metric_column], errors="coerce")
    available = values.notna()
    accepted = events[available & values.ge(threshold)].copy()
    rejected = events[available & ~values.ge(threshold)].copy()
    unavailable = events[~available].copy()
    accepted_outcome = accepted["outcome_result"].astype(str)
    rejected_outcome = rejected["outcome_result"].astype(str)
    accepted_win = int(accepted_outcome.eq("win").sum())
    accepted_neutral = int(accepted_outcome.eq("neutral").sum())
    accepted_loss = int(accepted_outcome.eq("loss").sum())
    rejected_win = int(rejected_outcome.eq("win").sum())
    rejected_neutral = int(rejected_outcome.eq("neutral").sum())
    rejected_loss = int(rejected_outcome.eq("loss").sum())
    accepted_mature = accepted_win + accepted_loss
    accepted_evaluated = accepted_win + accepted_neutral + accepted_loss
    evaluable_events = events[available].copy()
    total_loss = int(evaluable_events["outcome_result"].eq("loss").sum())
    total_success_or_neutral = int(evaluable_events["outcome_result"].isin(["win", "neutral"]).sum())
    accepted_return = pd.to_numeric(accepted["return_pct"], errors="coerce")
    rejected_return = pd.to_numeric(rejected["return_pct"], errors="coerce")
    return {
        "research_id": RESEARCH_ID,
        "research_variant_id": RESEARCH_VARIANT_ID,
        "parameter_set_id": PARAMETER_SET_ID,
        "advisory_status": RESEARCH_VARIANT_ID,
        "follow_through_scope_id": FOLLOW_THROUGH_SCOPE_ID,
        "rule_id": rule_id,
        "rule_type": "diagnostic_future_known_filter_not_original_entry_rule",
        "max_window_sessions": str(sessions),
        "min_follow_through_pct": metric_text(threshold),
        "accepted_count": str(len(accepted)),
        "rejected_count": str(len(rejected)),
        "unavailable_count": str(len(unavailable)),
        "accepted_win_count": str(accepted_win),
        "accepted_neutral_count": str(accepted_neutral),
        "accepted_loss_count": str(accepted_loss),
        "rejected_win_count": str(rejected_win),
        "rejected_neutral_count": str(rejected_neutral),
        "rejected_loss_count": str(rejected_loss),
        "accepted_pure_win_rate_pct": pct_text(accepted_win, accepted_mature),
        "accepted_neutral_inclusive_success_rate_pct": pct_text(accepted_win + accepted_neutral, accepted_evaluated),
        "accepted_avg_return_pct": metric_text(float(accepted_return.mean())) if accepted_return.notna().any() else "",
        "rejected_avg_return_pct": metric_text(float(rejected_return.mean())) if rejected_return.notna().any() else "",
        "loss_rejection_rate_pct": pct_text(rejected_loss, total_loss),
        "success_or_neutral_rejection_rate_pct": pct_text(rejected_win + rejected_neutral, total_success_or_neutral),
        "interpretation": "use_as_confirmation_entry_hypothesis_or_risk_label_only",
        "approved_for_daily": "false",
        "production_readiness": PRODUCTION_READINESS,
        "generated_at": generated_at,
    }


def build_summary(events: pd.DataFrame, generated_at: str) -> pd.DataFrame:
    rows = [
        summary_row(events, sessions=sessions, threshold=threshold, generated_at=generated_at)
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


def write_markdown(events: pd.DataFrame, summary: pd.DataFrame, generated_at: str) -> None:
    top = summary.copy()
    top["_accepted_loss"] = pd.to_numeric(top["accepted_loss_count"], errors="coerce")
    top["_accepted_success"] = pd.to_numeric(top["accepted_neutral_inclusive_success_rate_pct"], errors="coerce")
    top = top.sort_values(["_accepted_loss", "_accepted_success", "accepted_count"], ascending=[True, False, False]).drop(columns=["_accepted_loss", "_accepted_success"])
    review = events[
        [
            "outcome_result",
            "stock_id",
            "stock_name",
            "retest_entry_date",
            "entry_price",
            "follow_through_data_status",
            "return_pct",
            "max_close_return_1_session_pct",
            "max_close_return_2_session_pct",
            "max_close_return_3_session_pct",
            "max_close_return_5_session_pct",
            "first_close_ge_3pct_session",
            "first_close_ge_5pct_session",
            "weak_follow_through_5d_lt5pct",
            "early_adverse_3d_le_minus5pct",
        ]
    ].copy()
    review["_outcome_order"] = review["outcome_result"].map({"win": 1, "neutral": 2, "loss": 3}).fillna(9)
    review["_return"] = pd.to_numeric(review["return_pct"], errors="coerce")
    review = review.sort_values(["_outcome_order", "_return"], ascending=[True, False]).drop(columns=["_outcome_order", "_return"])
    lines = [
        "# Structured Neckline Strict 45/90 Follow-Through Audit",
        "",
        f"- generated_at: `{generated_at}`",
        f"- research_id: `{RESEARCH_ID}`",
        f"- source_research_id: `{SOURCE_PACKET_RESEARCH_ID}`",
        f"- source_parameter_set_id: `{SOURCE_PACKET_PARAMETER_SET_ID}`",
        f"- follow_through_scope_id: `{FOLLOW_THROUGH_SCOPE_ID}`",
        f"- sample: `{len(events)}`",
        f"- data_available: `{int(events['follow_through_data_status'].eq('available').sum())}`",
        f"- data_unavailable: `{int(events['follow_through_data_status'].eq('unavailable').sum())}`",
        f"- advisory_status: `{RESEARCH_VARIANT_ID}`",
        f"- production_readiness: `{PRODUCTION_READINESS}`",
        "- production impact: `none`; this audit does not update production model conditions, scoring, ranking, PDF logic, or baseline.",
        "",
        "## Boundary",
        "",
        "The follow-through values are known only after the original entry date. Therefore these rows must not be used as original-entry filters. They are research-only diagnostics for a possible later confirmation-entry model or a risk label. Rows without enough price-history coverage stay in the event index as `follow_through_data_status=unavailable` and are excluded from rule-rate denominators.",
        "",
        "## Rule Grid",
        "",
        *markdown_table(
            top,
            [
                "rule_id",
                "accepted_count",
                "accepted_win_count",
                "accepted_neutral_count",
                "accepted_loss_count",
                "unavailable_count",
                "accepted_neutral_inclusive_success_rate_pct",
                "accepted_avg_return_pct",
                "loss_rejection_rate_pct",
                "success_or_neutral_rejection_rate_pct",
                "interpretation",
            ],
            limit=40,
        ),
        "",
        "## Event Features",
        "",
        *markdown_table(review, list(review.columns), limit=80),
        "",
        "## Reading Notes",
        "",
        "- `within_1_session` means the entry-date close after buying at the entry-date open.",
        "- These diagnostics can support a future `confirmation_next_open` backtest, but are not themselves a production rule.",
        "- `weak_follow_through_5d_lt5pct` is the direct test of whether a row failed to reach +5% close return within the first five sessions.",
    ]
    LATEST_MD.parent.mkdir(parents=True, exist_ok=True)
    LATEST_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    generated_at = now_text()
    events = build_events(generated_at)
    summary = build_summary(events, generated_at)
    write_csv(events, LATEST_EVENT_CSV)
    write_csv(summary, LATEST_SUMMARY_CSV)
    write_csv(events, HISTORY_EVENT_CSV)
    write_csv(summary, HISTORY_SUMMARY_CSV)
    write_markdown(events, summary, generated_at)
    print(f"Saved: {LATEST_EVENT_CSV} rows={len(events)}")
    print(f"Saved: {LATEST_SUMMARY_CSV} rows={len(summary)}")
    print(f"Saved: {LATEST_MD}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
