from __future__ import annotations

from pathlib import Path

import pandas as pd


ROOT = Path(".")
RESEARCH_LATEST_DIR = ROOT / "output" / "latest" / "research_backtest"
RESEARCH_HISTORY_DIR = ROOT / "output" / "history" / "research"

LATEST_DETAIL_CSV = RESEARCH_LATEST_DIR / "w_bottom_early_entry_stop_loss_audit_detail_latest.csv"
LATEST_SUMMARY_CSV = RESEARCH_LATEST_DIR / "w_bottom_early_entry_stop_loss_audit_latest.csv"
LATEST_MD = RESEARCH_LATEST_DIR / "w_bottom_early_entry_stop_loss_audit_latest.md"
HISTORY_DETAIL_CSV = RESEARCH_HISTORY_DIR / "w_bottom_early_entry_stop_loss_audit_detail.csv"
HISTORY_SUMMARY_CSV = RESEARCH_HISTORY_DIR / "w_bottom_early_entry_stop_loss_audit.csv"

RESEARCH_ID = "w_bottom_early_entry_stop_loss_audit"
SOURCE_RESEARCH_ID = "w_bottom_market_regime_gated_review"
RESEARCH_VARIANT_ID = "warning_research_variant_only"
PRODUCTION_READINESS = "research_only_pending_promotion_decision"
SURFACE_ID = "w_bottom_right_low_early_entry"
EVENT_SET_ID = "variant_nearest_micro_45d_event_replay"
ENTRY_RULE_ID = "right_low_signal_next_open"
SOURCE_OUTCOME_RULE_ID = "tp10_or_neutral_after_5pct_close_40d"
SELECTED_SEGMENT_ID = "smooth_core_mainstream_right_rebound_5_20_bull"

EXPECTED_STOP_RULES = {
    "no_fixed_stop_d40_v1",
    "right_low_close_stop_d40",
    "w_structure_low_close_stop_d40",
    "w_structure_low_stop_d20_gain10_else_d40",
    "w_structure_low_close_stop_1pct_buffer_d40",
}

REQUIRED_DETAIL_COLUMNS = {
    "model_id",
    "research_id",
    "source_research_id",
    "research_variant_id",
    "advisory_status",
    "production_readiness",
    "approved_for_daily",
    "surface_id",
    "event_set_id",
    "entry_rule_id",
    "source_outcome_rule_id",
    "stop_rule_id",
    "segment_id",
    "stock_id",
    "entry_signal_date",
    "entry_date",
    "entry_open_price",
    "left_low_price",
    "right_low_price",
    "w_structure_low_stop_level",
    "stop_hit",
    "exit_date",
    "exit_close_price",
    "exit_reason",
    "return_pct",
    "mature",
    "success",
    "positive_return",
    "neutral_outcome",
    "outcome_result",
}

REQUIRED_SUMMARY_COLUMNS = {
    "model_id",
    "research_id",
    "source_research_id",
    "research_variant_id",
    "advisory_status",
    "production_readiness",
    "approved_for_daily",
    "surface_id",
    "event_set_id",
    "entry_rule_id",
    "source_outcome_rule_id",
    "segment_id",
    "stop_rule_id",
    "sample_size",
    "evaluated_sample_size",
    "mature_sample_size",
    "win_count",
    "neutral_count",
    "loss_count",
    "incomplete_count",
    "stop_hit_count",
    "pure_win_rate_pct",
    "neutral_inclusive_success_rate_pct",
    "avg_return_pct",
    "median_return_pct",
    "min_return_pct",
    "delta_pure_win_rate_pct",
    "delta_avg_return_pct",
    "min_return_improvement_pct",
    "recommendation_status",
}

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
    raise SystemExit(f"ERROR: {message}")


def read_csv(path: Path) -> pd.DataFrame:
    if not path.exists():
        fail(f"missing required file: {path}")
    return pd.read_csv(path, dtype=str, keep_default_na=False)


def validate_schema(df: pd.DataFrame, required: set[str], name: str) -> None:
    missing = sorted(required - set(df.columns))
    if missing:
        fail(f"{name} missing columns: {missing}")
    forbidden = sorted(set(df.columns) & FORBIDDEN_PRODUCTION_FIELDS)
    if forbidden:
        fail(f"{name} must not emit production decision fields: {forbidden}")


def validate_constants(df: pd.DataFrame, name: str) -> None:
    expected = {
        "research_id": RESEARCH_ID,
        "source_research_id": SOURCE_RESEARCH_ID,
        "research_variant_id": RESEARCH_VARIANT_ID,
        "advisory_status": RESEARCH_VARIANT_ID,
        "production_readiness": PRODUCTION_READINESS,
        "approved_for_daily": "false",
        "surface_id": SURFACE_ID,
        "event_set_id": EVENT_SET_ID,
        "entry_rule_id": ENTRY_RULE_ID,
        "source_outcome_rule_id": SOURCE_OUTCOME_RULE_ID,
    }
    for column, expected_value in expected.items():
        values = set(df[column].astype(str))
        if values != {expected_value}:
            fail(f"{name} unexpected values for {column}: {sorted(values)}")


def numeric_value(row: pd.Series, column: str) -> float:
    return float(pd.to_numeric(pd.Series([row[column]]), errors="coerce").iloc[0])


def validate_selected_tradeoff(summary: pd.DataFrame) -> None:
    selected = summary[summary["segment_id"].eq(SELECTED_SEGMENT_ID)].copy()
    if set(selected["stop_rule_id"]) != EXPECTED_STOP_RULES:
        fail("selected segment missing expected stop-rule comparison rows")
    baseline = selected[selected["stop_rule_id"].eq("no_fixed_stop_d40_v1")]
    structure = selected[selected["stop_rule_id"].eq("w_structure_low_close_stop_d40")]
    hybrid = selected[selected["stop_rule_id"].eq("w_structure_low_stop_d20_gain10_else_d40")]
    if len(baseline) != 1 or len(structure) != 1 or len(hybrid) != 1:
        fail("selected segment must contain one baseline, one structure-low stop, and one hybrid D+20/D+40 row")
    b = baseline.iloc[0]
    s = structure.iloc[0]
    h = hybrid.iloc[0]
    if numeric_value(s, "avg_return_pct") <= numeric_value(b, "avg_return_pct"):
        fail("structure-low stop must improve selected-segment average return versus baseline")
    if numeric_value(s, "min_return_pct") <= numeric_value(b, "min_return_pct"):
        fail("structure-low stop must improve selected-segment worst return versus baseline")
    if numeric_value(s, "pure_win_rate_pct") >= numeric_value(b, "pure_win_rate_pct"):
        fail("structure-low stop tradeoff must explicitly show lower pure win rate than baseline")
    if str(s["recommendation_status"]) != "risk_repair_candidate_tradeoff_review":
        fail("structure-low stop recommendation_status must require tradeoff review")
    if numeric_value(h, "avg_return_pct") <= numeric_value(s, "avg_return_pct"):
        fail("hybrid D+20/D+40 row must improve average return versus structure-low stop with +10%/+5% rule")
    if numeric_value(h, "min_return_pct") <= numeric_value(b, "min_return_pct"):
        fail("hybrid D+20/D+40 row must improve selected-segment worst return versus baseline")
    if str(h["recommendation_status"]) != "preferred_v2_candidate_tradeoff_review":
        fail("hybrid D+20/D+40 recommendation_status must require explicit v2 review")


def validate_markdown() -> None:
    if not LATEST_MD.exists():
        fail(f"missing markdown: {LATEST_MD}")
    text = LATEST_MD.read_text(encoding="utf-8")
    required = [
        "production impact: `none`",
        "w_structure_low_close_stop_d40",
        "w_structure_low_stop_d20_gain10_else_d40",
        "pure win",
        "left-tail risk",
        "must not be promoted silently as production v2",
    ]
    for item in required:
        if item not in text:
            fail(f"markdown missing required text: {item}")


def main() -> int:
    detail = read_csv(LATEST_DETAIL_CSV)
    history_detail = read_csv(HISTORY_DETAIL_CSV)
    summary = read_csv(LATEST_SUMMARY_CSV)
    history_summary = read_csv(HISTORY_SUMMARY_CSV)

    validate_schema(detail, REQUIRED_DETAIL_COLUMNS, "latest detail")
    validate_schema(history_detail, REQUIRED_DETAIL_COLUMNS, "history detail")
    validate_schema(summary, REQUIRED_SUMMARY_COLUMNS, "latest summary")
    validate_schema(history_summary, REQUIRED_SUMMARY_COLUMNS, "history summary")
    validate_constants(detail, "latest detail")
    validate_constants(history_detail, "history detail")
    validate_constants(summary, "latest summary")
    validate_constants(history_summary, "history summary")

    if len(detail) != len(history_detail):
        fail("latest/history detail row counts differ")
    if len(summary) != len(history_summary):
        fail("latest/history summary row counts differ")
    if len(detail) < 1000:
        fail(f"detail row count unexpectedly small: {len(detail)}")
    if len(summary) != 25:
        fail(f"summary row count should be 25, got {len(summary)}")
    if set(detail["stop_rule_id"]) != EXPECTED_STOP_RULES:
        fail("detail stop_rule_id values mismatch")
    if set(summary["stop_rule_id"]) != EXPECTED_STOP_RULES:
        fail("summary stop_rule_id values mismatch")
    if not set(detail["outcome_result"]).issubset({"win", "neutral", "loss", "incomplete"}):
        fail("detail outcome_result has unexpected values")
    for column in ["mature", "success", "positive_return", "neutral_outcome", "stop_hit"]:
        if not set(detail[column].astype(str)).issubset({"true", "false"}):
            fail(f"detail {column} must be true/false")

    validate_selected_tradeoff(summary)
    validate_markdown()

    selected = summary[
        summary["segment_id"].eq(SELECTED_SEGMENT_ID)
        & summary["stop_rule_id"].eq("w_structure_low_stop_d20_gain10_else_d40")
    ].iloc[0]
    print("w_bottom_early_entry_stop_loss_audit validation passed")
    print(f"detail_rows={len(detail)} summary_rows={len(summary)}")
    print(
        "selected_hybrid_rule="
        f"pure_win={selected['pure_win_rate_pct']} "
        f"inclusive_success={selected['neutral_inclusive_success_rate_pct']} "
        f"avg_return={selected['avg_return_pct']} "
        f"min_return={selected['min_return_pct']}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
