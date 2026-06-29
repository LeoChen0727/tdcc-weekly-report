from __future__ import annotations

from datetime import datetime
from pathlib import Path
from typing import Any
from zoneinfo import ZoneInfo
import math

import pandas as pd

from build_structured_neckline_strict_45_90_confirmation_entry_audit import (
    EXIT_RULE_ID,
    FORBIDDEN_PRODUCTION_FIELDS,
    MAX_HOLDING_SESSIONS,
    RESEARCH_VARIANT_ID,
    format_float,
    metric_text,
    normalize_code,
    normalize_date,
    read_price,
    safe_str,
    simulate_confirmation_trade,
    to_float,
)


ROOT = Path(__file__).resolve().parents[1]
RESEARCH_LATEST_DIR = ROOT / "output" / "latest" / "research_backtest"
RESEARCH_HISTORY_DIR = ROOT / "output" / "history" / "research"

SOURCE_RISK_CSV = RESEARCH_LATEST_DIR / "structured_neckline_dual_window_risk_penalty_audit_latest.csv"

MODEL_ID = "neckline_volume_breakout_confirmation"
RESEARCH_ID = "neckline_strict_45_signal_90_score_operation_candidate"
PARAMETER_SET_ID = "neckline_strict_45_signal_90_score_operation_candidate_20260629"
SOURCE_RESEARCH_ID = "structured_neckline_dual_window_risk_penalty_audit"
SOURCE_PARAMETER_SET_ID = "structured_neckline_dual_window_risk_penalty_audit_20260629"
SOURCE_RISK_RULE_ID = "broad_45_non_bearish_with_90_warning"
SEGMENT_ID = "low_position_le60_market_bull"
OPERATION_CANDIDATE_ID = "neckline_strict_45_signal_90_score_v1"
CONFIRMATION_RULE_ID = "close_ge_1pct_within_3_sessions_next_open"
ENTRY_RULE_ID = CONFIRMATION_RULE_ID
ENTRY_RULE_TEXT = (
    "After a 45-day non-bearish neckline candidate, wait until close return from the "
    "original retest entry is at least +1% within 3 sessions, then buy next open."
)
EXIT_RULE_TEXT = (
    "Win when close return reaches +10%; neutral when close return first reaches +5% "
    "then closes back at or below +5% before +10%; otherwise sell at the 20th close."
)
OUTCOME_DEFINITION_VERSION = "tp10_close_win_5pct_pullback_neutral_else_20d_loss_v1"
WIN_DEFINITION = "close return reaches +10% before the 20-session limit"
NEUTRAL_DEFINITION = "close return reaches +5% first, then closes back at or below +5% before +10%"
LOSS_DEFINITION = "no +10% close win and no neutral trigger before the 20th close, even if the final return is positive"
PDF_METRIC_LABEL = "operation-rule win rate and neutral-inclusive success rate"
PDF_SUBTITLE_NOTE = (
    "PDF subtitle must label this as operation-rule evidence: win=+10% close hit; "
    "neutral=+5% close reached then pulled back to +5%; loss=otherwise 20th close."
)
SIGNAL_WINDOW_ROLE = "45d_auto_non_bearish_required_entry_signal"
SCORE_WINDOW_ROLE = "90d_context_score_adjustment_only_not_entry_exclusion"
PRODUCTION_READINESS = "not_production_ready_research_only"

LATEST_DETAIL_CSV = RESEARCH_LATEST_DIR / "neckline_strict_45_signal_90_score_operation_candidate_detail_latest.csv"
LATEST_SUMMARY_CSV = RESEARCH_LATEST_DIR / "neckline_strict_45_signal_90_score_operation_candidate_latest.csv"
LATEST_MD = RESEARCH_LATEST_DIR / "neckline_strict_45_signal_90_score_operation_candidate_latest.md"
HISTORY_DETAIL_CSV = RESEARCH_HISTORY_DIR / "neckline_strict_45_signal_90_score_operation_candidate_detail.csv"
HISTORY_SUMMARY_CSV = RESEARCH_HISTORY_DIR / "neckline_strict_45_signal_90_score_operation_candidate.csv"

DETAIL_COLUMNS = [
    "model_id",
    "operation_candidate_id",
    "research_id",
    "source_research_id",
    "source_parameter_set_id",
    "research_variant_id",
    "parameter_set_id",
    "advisory_status",
    "source_risk_rule_id",
    "segment_id",
    "entry_rule_id",
    "exit_rule_id",
    "signal_window_role",
    "score_window_role",
    "stock_id",
    "stock_name",
    "signal_date",
    "original_retest_entry_date",
    "original_entry_price",
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
    "context_45",
    "filter_45",
    "return_45",
    "slope20_45",
    "drawdown_45",
    "context_90",
    "filter_90",
    "return_90",
    "slope20_90",
    "drawdown_90",
    "score_adjustment_points",
    "score_adjustment_flags",
    "score_adjustment_label",
    "market_regime",
    "low_position_120_pct",
    "base_width_pct",
    "support_touch_count",
    "diagnostic_note",
    "approved_for_daily",
    "production_readiness",
    "generated_at",
]

SUMMARY_COLUMNS = [
    "model_id",
    "operation_candidate_id",
    "research_id",
    "source_research_id",
    "source_parameter_set_id",
    "research_variant_id",
    "parameter_set_id",
    "advisory_status",
    "source_risk_rule_id",
    "segment_id",
    "entry_rule_id",
    "entry_rule",
    "exit_rule_id",
    "exit_rule",
    "outcome_definition_version",
    "win_definition",
    "neutral_definition",
    "loss_definition",
    "pdf_metric_label",
    "pdf_subtitle_note",
    "signal_window_role",
    "score_window_role",
    "source_candidate_count",
    "confirmation_candidate_count",
    "tradable_entry_count",
    "incomplete_count",
    "filter90_auto_bearish_source_count",
    "filter90_auto_bearish_confirmed_count",
    "score_adjustment_avg_points",
    "win_count",
    "neutral_count",
    "loss_count",
    "pure_win_rate_pct",
    "neutral_inclusive_success_rate_pct",
    "avg_return_pct",
    "median_return_pct",
    "avg_max_close_return_pct",
    "avg_min_close_return_pct",
    "candidate_status",
    "promotion_boundary",
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


def write_csv(frame: pd.DataFrame, path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    frame.to_csv(path, index=False, encoding="utf-8-sig")


def pct_text(numerator: int | float, denominator: int | float) -> str:
    if denominator == 0:
        return ""
    return f"{float(numerator) / float(denominator) * 100.0:.4f}"


def source_rows() -> pd.DataFrame:
    source = read_csv(SOURCE_RISK_CSV)
    required = {
        "research_id",
        "parameter_set_id",
        "risk_penalty_rule_id",
        "risk_penalty_candidate_accept",
        "risk_penalty_points",
        "risk_penalty_flags",
        "stock_id",
        "stock_name",
        "signal_date",
        "retest_entry_date",
        "entry_price",
        "market_regime",
        "low_position_120_pct",
        "base_width_pct",
        "support_touch_count",
        "in_low_position_le60_market_bull",
        "context_45",
        "filter_45",
        "return_45",
        "slope20_45",
        "drawdown_45",
        "context_90",
        "filter_90",
        "return_90",
        "slope20_90",
        "drawdown_90",
        "approved_for_daily",
        "production_readiness",
    }
    missing = sorted(required - set(source.columns))
    if missing:
        raise SystemExit(f"ERROR: source risk audit missing columns: {missing}")
    forbidden = sorted(set(source.columns) & FORBIDDEN_PRODUCTION_FIELDS)
    if forbidden:
        raise SystemExit(f"ERROR: source risk audit contains forbidden production fields: {forbidden}")
    rows = source[
        source["research_id"].astype(str).eq(SOURCE_RESEARCH_ID)
        & source["parameter_set_id"].astype(str).eq(SOURCE_PARAMETER_SET_ID)
        & source["risk_penalty_rule_id"].astype(str).eq(SOURCE_RISK_RULE_ID)
        & source["risk_penalty_candidate_accept"].astype(str).str.lower().eq("true")
        & source["in_low_position_le60_market_bull"].astype(str).str.lower().eq("true")
        & source["filter_45"].astype(str).eq("auto_non_bearish")
    ].copy()
    if rows.empty:
        raise SystemExit("ERROR: no broad 45-day signal rows found")
    rows["stock_id"] = rows["stock_id"].map(normalize_code)
    return rows.sort_values(["signal_date", "stock_id", "retest_entry_date"]).reset_index(drop=True)


def return_from_entry(close_value: Any, entry_price: float) -> float:
    close_price = to_float(close_value)
    if math.isnan(close_price) or math.isnan(entry_price) or entry_price <= 0:
        return math.nan
    return (close_price / entry_price - 1.0) * 100.0


def confirmation_hit(row: pd.Series) -> dict[str, str]:
    stock_id = normalize_code(row.get("stock_id"))
    price = read_price(stock_id)
    if price.empty:
        return {"tradability_status": "missing_price_history_file"}
    entry_date = normalize_date(row.get("retest_entry_date"))
    matches = price.index[price["date"].astype(str).eq(entry_date)].tolist()
    if not matches:
        return {"tradability_status": "original_retest_entry_date_missing"}
    entry_idx = int(matches[0])
    entry_price = to_float(row.get("entry_price"))
    if math.isnan(entry_price) or entry_price <= 0:
        return {"tradability_status": "invalid_original_entry_price"}
    window = price.iloc[entry_idx : min(len(price), entry_idx + 3)].copy().reset_index(drop=True)
    if len(window) < 3:
        return {"tradability_status": "insufficient_confirmation_window"}
    for idx, item in window.iterrows():
        close_return = return_from_entry(item.get("close"), entry_price)
        if not math.isnan(close_return) and close_return >= 1.0:
            return {
                "tradability_status": "confirmation_signal_found",
                "confirmation_signal_date": safe_str(item.get("date")),
                "confirmation_signal_session": str(int(idx) + 1),
            }
    return {"tradability_status": "no_confirmation_close_ge_1pct_within_3_sessions"}


def score_adjustment_label(row: pd.Series) -> str:
    points = to_float(row.get("risk_penalty_points"))
    filter_90 = safe_str(row.get("filter_90"))
    if filter_90 == "auto_bearish":
        if not math.isnan(points) and points >= 4:
            return "heavy_90d_risk_penalty"
        return "moderate_90d_risk_penalty"
    if filter_90 == "auto_non_bearish":
        if not math.isnan(points) and points <= 1:
            return "clean_or_repair_credit"
        return "non_bearish_with_risk_tags"
    return "unknown_90d_context_score_only"


def build_detail(generated_at: str) -> pd.DataFrame:
    rows: list[dict[str, str]] = []
    for _, source in source_rows().iterrows():
        hit = confirmation_hit(source)
        if hit["tradability_status"] != "confirmation_signal_found":
            continue
        trade = simulate_confirmation_trade(source, hit["confirmation_signal_date"])
        rows.append(
            {
                "model_id": MODEL_ID,
                "operation_candidate_id": OPERATION_CANDIDATE_ID,
                "research_id": RESEARCH_ID,
                "source_research_id": SOURCE_RESEARCH_ID,
                "source_parameter_set_id": SOURCE_PARAMETER_SET_ID,
                "research_variant_id": RESEARCH_VARIANT_ID,
                "parameter_set_id": PARAMETER_SET_ID,
                "advisory_status": RESEARCH_VARIANT_ID,
                "source_risk_rule_id": SOURCE_RISK_RULE_ID,
                "segment_id": SEGMENT_ID,
                "entry_rule_id": ENTRY_RULE_ID,
                "exit_rule_id": EXIT_RULE_ID,
                "signal_window_role": SIGNAL_WINDOW_ROLE,
                "score_window_role": SCORE_WINDOW_ROLE,
                "stock_id": normalize_code(source.get("stock_id")),
                "stock_name": safe_str(source.get("stock_name")),
                "signal_date": normalize_date(source.get("signal_date")),
                "original_retest_entry_date": normalize_date(source.get("retest_entry_date")),
                "original_entry_price": format_float(source.get("entry_price")),
                "confirmation_signal_date": safe_str(hit.get("confirmation_signal_date")),
                "confirmation_signal_session": safe_str(hit.get("confirmation_signal_session")),
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
                "context_45": safe_str(source.get("context_45")),
                "filter_45": safe_str(source.get("filter_45")),
                "return_45": format_float(source.get("return_45")),
                "slope20_45": format_float(source.get("slope20_45")),
                "drawdown_45": format_float(source.get("drawdown_45")),
                "context_90": safe_str(source.get("context_90")),
                "filter_90": safe_str(source.get("filter_90")),
                "return_90": format_float(source.get("return_90")),
                "slope20_90": format_float(source.get("slope20_90")),
                "drawdown_90": format_float(source.get("drawdown_90")),
                "score_adjustment_points": safe_str(source.get("risk_penalty_points")),
                "score_adjustment_flags": safe_str(source.get("risk_penalty_flags")),
                "score_adjustment_label": score_adjustment_label(source),
                "market_regime": safe_str(source.get("market_regime")),
                "low_position_120_pct": format_float(source.get("low_position_120_pct")),
                "base_width_pct": format_float(source.get("base_width_pct")),
                "support_touch_count": safe_str(source.get("support_touch_count")),
                "diagnostic_note": "research_only_45_signal_90_score_adjustment_candidate",
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
        raise SystemExit(f"ERROR: operation candidate detail contains forbidden production fields: {forbidden}")
    return detail[DETAIL_COLUMNS]


def build_summary(detail: pd.DataFrame, generated_at: str) -> pd.DataFrame:
    source = source_rows()
    tradable = detail[detail["tradability_status"].astype(str).eq("tradable")].copy()
    outcomes = tradable["outcome_result"].astype(str)
    win = int(outcomes.eq("win").sum())
    neutral = int(outcomes.eq("neutral").sum())
    loss = int(outcomes.eq("loss").sum())
    mature = win + loss
    evaluated = win + neutral + loss
    returns = pd.to_numeric(tradable["return_pct"], errors="coerce")
    max_returns = pd.to_numeric(tradable["max_close_return_pct"], errors="coerce")
    min_returns = pd.to_numeric(tradable["min_close_return_pct"], errors="coerce")
    points = pd.to_numeric(tradable["score_adjustment_points"], errors="coerce")
    row = {
        "model_id": MODEL_ID,
        "operation_candidate_id": OPERATION_CANDIDATE_ID,
        "research_id": RESEARCH_ID,
        "source_research_id": SOURCE_RESEARCH_ID,
        "source_parameter_set_id": SOURCE_PARAMETER_SET_ID,
        "research_variant_id": RESEARCH_VARIANT_ID,
        "parameter_set_id": PARAMETER_SET_ID,
        "advisory_status": RESEARCH_VARIANT_ID,
        "source_risk_rule_id": SOURCE_RISK_RULE_ID,
        "segment_id": SEGMENT_ID,
        "entry_rule_id": ENTRY_RULE_ID,
        "entry_rule": ENTRY_RULE_TEXT,
        "exit_rule_id": EXIT_RULE_ID,
        "exit_rule": EXIT_RULE_TEXT,
        "outcome_definition_version": OUTCOME_DEFINITION_VERSION,
        "win_definition": WIN_DEFINITION,
        "neutral_definition": NEUTRAL_DEFINITION,
        "loss_definition": LOSS_DEFINITION,
        "pdf_metric_label": PDF_METRIC_LABEL,
        "pdf_subtitle_note": PDF_SUBTITLE_NOTE,
        "signal_window_role": SIGNAL_WINDOW_ROLE,
        "score_window_role": SCORE_WINDOW_ROLE,
        "source_candidate_count": str(len(source)),
        "confirmation_candidate_count": str(len(detail)),
        "tradable_entry_count": str(len(tradable)),
        "incomplete_count": str(len(detail) - len(tradable)),
        "filter90_auto_bearish_source_count": str(int(source["filter_90"].astype(str).eq("auto_bearish").sum())),
        "filter90_auto_bearish_confirmed_count": str(int(detail["filter_90"].astype(str).eq("auto_bearish").sum())),
        "score_adjustment_avg_points": metric_text(float(points.mean())) if points.notna().any() else "",
        "win_count": str(win),
        "neutral_count": str(neutral),
        "loss_count": str(loss),
        "pure_win_rate_pct": pct_text(win, mature),
        "neutral_inclusive_success_rate_pct": pct_text(win + neutral, evaluated),
        "avg_return_pct": metric_text(float(returns.mean())) if returns.notna().any() else "",
        "median_return_pct": metric_text(float(returns.median())) if returns.notna().any() else "",
        "avg_max_close_return_pct": metric_text(float(max_returns.mean())) if max_returns.notna().any() else "",
        "avg_min_close_return_pct": metric_text(float(min_returns.mean())) if min_returns.notna().any() else "",
        "candidate_status": "promotion_candidate_requires_daily_model_change_pr",
        "promotion_boundary": (
            "research advisory only; does not update production model logic, ranking, scoring, "
            "daily PDF approval, or production baseline"
        ),
        "approved_for_daily": "false",
        "production_readiness": PRODUCTION_READINESS,
        "generated_at": generated_at,
    }
    summary = pd.DataFrame([row])
    return summary[SUMMARY_COLUMNS]


def markdown_table(frame: pd.DataFrame, columns: list[str], limit: int = 80) -> list[str]:
    if frame.empty:
        return ["_No rows._"]
    lines = ["| " + " | ".join(columns) + " |", "| " + " | ".join(["---"] * len(columns)) + " |"]
    for _, row in frame.loc[:, columns].head(limit).iterrows():
        lines.append("| " + " | ".join(safe_str(row.get(column)) for column in columns) + " |")
    return lines


def write_markdown(detail: pd.DataFrame, summary: pd.DataFrame, generated_at: str) -> None:
    row = summary.iloc[0]
    lines = [
        "# Neckline Strict 45 Signal 90 Score Operation Candidate",
        "",
        f"- generated_at: `{generated_at}`",
        f"- model_id: `{MODEL_ID}`",
        f"- operation_candidate_id: `{OPERATION_CANDIDATE_ID}`",
        f"- research_id: `{RESEARCH_ID}`",
        f"- source_research_id: `{SOURCE_RESEARCH_ID}`",
        f"- source_risk_rule_id: `{SOURCE_RISK_RULE_ID}`",
        f"- segment_id: `{SEGMENT_ID}`",
        f"- entry_rule_id: `{ENTRY_RULE_ID}`",
        f"- exit_rule_id: `{EXIT_RULE_ID}`",
        f"- outcome_definition_version: `{OUTCOME_DEFINITION_VERSION}`",
        f"- advisory_status: `{RESEARCH_VARIANT_ID}`",
        f"- production_readiness: `{PRODUCTION_READINESS}`",
        "- approved_for_daily: `false`",
        "- production impact: `none`; this candidate does not update production model conditions, scoring, ranking, PDF logic, daily_full_pipeline, or production baseline.",
        "",
        "## Candidate Semantics",
        "",
        "- 45-day context is the entry-signal gate: `filter_45` must be `auto_non_bearish`.",
        "- 90-day context is score adjustment only, not an entry exclusion; `filter_90=auto_bearish` rows remain eligible with penalty labels.",
        "- Entry uses the next open after the confirmation close, so it is tradable and does not use same-day close as a buy price.",
        "- This is research-only evidence. Promotion requires a separate daily_model_maintenance PR before removing or replacing production models.",
        "",
        "## Summary",
        "",
        *markdown_table(
            summary,
            [
                "source_candidate_count",
                "confirmation_candidate_count",
                "tradable_entry_count",
                "win_count",
                "neutral_count",
                "loss_count",
                "pure_win_rate_pct",
                "neutral_inclusive_success_rate_pct",
                "avg_return_pct",
                "median_return_pct",
                "filter90_auto_bearish_confirmed_count",
            ],
            limit=5,
        ),
        "",
        "## Selected Rule",
        "",
        f"- entry_rule: `{row['entry_rule']}`",
        f"- exit_rule: `{row['exit_rule']}`",
        f"- signal_window_role: `{SIGNAL_WINDOW_ROLE}`",
        f"- score_window_role: `{SCORE_WINDOW_ROLE}`",
        "",
        "## Outcome And PDF Metric Definitions",
        "",
        f"- pdf_metric_label: `{PDF_METRIC_LABEL}`",
        f"- win_definition: `{WIN_DEFINITION}`",
        f"- neutral_definition: `{NEUTRAL_DEFINITION}`",
        f"- loss_definition: `{LOSS_DEFINITION}`",
        f"- pdf_subtitle_note: `{PDF_SUBTITLE_NOTE}`",
        "",
        "## Detail Preview",
        "",
        *markdown_table(
            detail.sort_values(["outcome_result", "return_pct"], ascending=[True, False]),
            [
                "outcome_result",
                "stock_id",
                "stock_name",
                "signal_date",
                "confirmation_signal_date",
                "confirmation_entry_date",
                "return_pct",
                "context_45",
                "context_90",
                "filter_90",
                "score_adjustment_points",
                "score_adjustment_label",
            ],
            limit=40,
        ),
    ]
    LATEST_MD.parent.mkdir(parents=True, exist_ok=True)
    LATEST_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")


def build(generated_at: str) -> tuple[pd.DataFrame, pd.DataFrame]:
    detail = build_detail(generated_at)
    summary = build_summary(detail, generated_at)
    return detail, summary


def main() -> int:
    generated_at = now_text()
    detail, summary = build(generated_at)
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
