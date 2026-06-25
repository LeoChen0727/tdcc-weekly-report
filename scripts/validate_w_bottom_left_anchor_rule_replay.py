from __future__ import annotations

from pathlib import Path

import pandas as pd


ROOT = Path(".")
RESEARCH_LATEST_DIR = ROOT / "output" / "latest" / "research_backtest"
RESEARCH_HISTORY_DIR = ROOT / "output" / "history" / "research"

SOURCE_RULE_DETAIL_CSV = RESEARCH_LATEST_DIR / "w_bottom_left_anchor_rule_grid_detail_latest.csv"
LATEST_DETAIL_CSV = RESEARCH_LATEST_DIR / "w_bottom_left_anchor_rule_replay_detail_latest.csv"
LATEST_SUMMARY_CSV = RESEARCH_LATEST_DIR / "w_bottom_left_anchor_rule_replay_latest.csv"
LATEST_MD = RESEARCH_LATEST_DIR / "w_bottom_left_anchor_rule_replay_latest.md"
HISTORY_DETAIL_CSV = RESEARCH_HISTORY_DIR / "w_bottom_left_anchor_rule_replay_detail.csv"
HISTORY_SUMMARY_CSV = RESEARCH_HISTORY_DIR / "w_bottom_left_anchor_rule_replay.csv"

MODEL_ID = "w_bottom_right_side"
CONFIRMATION_MODEL_ID = "neckline_volume_breakout_confirmation"
RESEARCH_ID = "w_bottom_left_anchor_rule_replay"
SOURCE_RESEARCH_ID = "w_bottom_left_anchor_rule_grid"
RESEARCH_VARIANT_ID = "warning_research_variant_only"
BASELINE_RULE_ID = "current_detector_left_peak"
MICRO45_RULE_ID = "nearest_micro_pressure_45d_min15_before_left_low"
MICRO90_RULE_ID = "nearest_micro_pressure_90d_min15_before_left_low"
HIGH90_RULE_ID = "highest_high_90d_before_left_low"

EXPECTED_RULE_IDS = {
    BASELINE_RULE_ID,
    "highest_high_45d_before_left_low",
    HIGH90_RULE_ID,
    MICRO45_RULE_ID,
    MICRO90_RULE_ID,
}

REQUIRED_DETAIL_COLUMNS = {
    "model_id",
    "confirmation_model_id",
    "research_id",
    "source_research_id",
    "research_variant_id",
    "parameter_set_id",
    "advisory_status",
    "rule_id",
    "rule_window_days",
    "selector_method",
    "source_audit_scope",
    "case_review_tag",
    "manual_case_id",
    "stock_id",
    "stock_name",
    "signal_date",
    "source_pattern_family",
    "baseline_current_left_peak_date",
    "candidate_left_peak_date",
    "candidate_days_before_left_low",
    "candidate_drop_to_left_low_pct",
    "candidate_left_descent_wrong_direction_rate_pct",
    "candidate_matches_human_left_peak",
    "candidate_selection_status",
    "candidate_selection_reason",
    "outcome_available",
    "sym1_5_quality_bucket",
    "sym1_5_w_shape_completed",
    "sym1_5_neckline_volume_breakout",
    "sym1_5_breakout_date",
    "primary_review_flag",
    "transition_status",
    "slope_curvature_category",
    "price_level_bucket",
    "effective_mainstream_label",
    "a_mature",
    "a_return_pct",
    "c_mature",
    "c_return_pct",
    "tdcc_any_age7",
    "selected_for_rule_replay",
    "manual_review_status",
    "approved_for_daily",
    "production_readiness",
    "generated_at",
}

REQUIRED_SUMMARY_COLUMNS = {
    "model_id",
    "confirmation_model_id",
    "research_id",
    "research_variant_id",
    "parameter_set_id",
    "advisory_status",
    "rule_id",
    "rule_window_days",
    "selector_method",
    "rule_source_rows",
    "selected_rows",
    "selected_rate_pct",
    "outcome_available_rows",
    "manual_positive_rows",
    "shape_completed_count",
    "shape_completed_rate_pct",
    "volume_breakout_count",
    "volume_breakout_rate_pct",
    "observation_to_volume_confirmation_count",
    "mature_sample_size",
    "win_count",
    "win_rate_pct",
    "avg_a_return_pct",
    "median_a_return_pct",
    "tdcc_any_age7_count",
    "baseline_outcome_available_rows",
    "baseline_volume_breakout_rate_pct",
    "baseline_mature_sample_size",
    "baseline_win_rate_pct",
    "baseline_avg_a_return_pct",
    "delta_selected_rows_vs_baseline",
    "delta_volume_breakout_rate_pct",
    "delta_win_rate_pct",
    "delta_avg_a_return_pct",
    "sample_warning",
    "production_readiness",
    "generated_at",
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
    print(f"ERROR: {message}")
    raise SystemExit(1)


def read_csv(path: Path) -> pd.DataFrame:
    if not path.exists():
        fail(f"missing required file: {path}")
    try:
        return pd.read_csv(path, dtype=str, keep_default_na=False)
    except Exception as exc:
        fail(f"{path} is not readable CSV: {exc}")


def normalize_code(value: object) -> str:
    text = str(value).replace("\ufeff", "").strip()
    if text.endswith(".0"):
        text = text[:-2]
    return text.zfill(4) if text.isdigit() and len(text) < 4 else text


def to_number(value: object) -> float:
    text = str(value).replace(",", "").replace("%", "").strip()
    if not text:
        return float("nan")
    try:
        return float(text)
    except ValueError:
        return float("nan")


def false_only(series: pd.Series) -> bool:
    return set(series.astype(str).str.lower().unique()) <= {"false", "0", ""}


def assert_close(actual: object, expected: float, label: str, tolerance: float = 0.0002) -> None:
    actual_number = to_number(actual)
    if pd.isna(actual_number) or abs(actual_number - expected) > tolerance:
        fail(f"{label} must be {expected}; got {actual}")


def validate_constants(df: pd.DataFrame, require_source: bool = False, require_approved: bool = False) -> None:
    expected = {
        "model_id": MODEL_ID,
        "confirmation_model_id": CONFIRMATION_MODEL_ID,
        "research_id": RESEARCH_ID,
        "research_variant_id": RESEARCH_VARIANT_ID,
        "advisory_status": RESEARCH_VARIANT_ID,
        "production_readiness": "not_production_ready_research_only",
    }
    for column, value in expected.items():
        values = set(df[column].astype(str))
        if values != {value}:
            fail(f"{column} must be {value}; got {sorted(values)}")
    if require_source:
        values = set(df["source_research_id"].astype(str))
        if values != {SOURCE_RESEARCH_ID}:
            fail(f"source_research_id must be {SOURCE_RESEARCH_ID}; got {sorted(values)}")
    if require_approved and not false_only(df["approved_for_daily"]):
        fail("approved_for_daily must remain false")


def validate_detail(detail: pd.DataFrame) -> None:
    validate_constants(detail, require_source=True, require_approved=True)
    source_rule = read_csv(SOURCE_RULE_DETAIL_CSV)
    if len(detail) != len(source_rule):
        fail(f"detail row count must match rule-grid detail rows {len(source_rule)}; got {len(detail)}")
    if set(detail["rule_id"].astype(str)) != EXPECTED_RULE_IDS:
        fail(f"unexpected rule ids: {sorted(set(detail['rule_id'].astype(str)))}")
    if detail["stock_id"].map(normalize_code).eq("4916").any():
        fail("4916 higher-right-low case must not appear in standard-W replay detail")
    if not set(detail["selected_for_rule_replay"].astype(str).str.lower()).issubset({"true", "false"}):
        fail("selected_for_rule_replay must be true/false")
    if not set(detail["outcome_available"].astype(str).str.lower()).issubset({"true", "false"}):
        fail("outcome_available must be true/false")

    row_8069_micro = detail[
        detail["stock_id"].map(normalize_code).eq("8069")
        & detail["rule_id"].eq(MICRO45_RULE_ID)
    ]
    if len(row_8069_micro) != 1:
        fail("expected one 8069 nearest micro 45 replay row")
    r8069 = row_8069_micro.iloc[0]
    if r8069["candidate_left_peak_date"] != "20260311":
        fail("8069 nearest micro 45 replay must preserve 20260311 candidate anchor")
    if r8069["candidate_matches_human_left_peak"].lower() != "true":
        fail("8069 nearest micro 45 replay must match the human anchor")
    if r8069["outcome_available"].lower() != "false":
        fail("8069 manual positive replay row must not be counted in production-like outcome metrics")

    row_6415_high90 = detail[
        detail["stock_id"].map(normalize_code).eq("6415")
        & detail["signal_date"].eq("20260115")
        & detail["rule_id"].eq(HIGH90_RULE_ID)
    ]
    if len(row_6415_high90) != 1:
        fail("expected one 6415 high90 replay row")
    r6415 = row_6415_high90.iloc[0]
    if r6415["candidate_left_peak_date"] != "20250718":
        fail("6415 high90 replay must preserve 20250718 candidate anchor")
    if r6415["outcome_available"].lower() != "true":
        fail("6415 high90 replay should have outcome metrics")


def validate_summary(summary: pd.DataFrame, detail: pd.DataFrame) -> None:
    validate_constants(summary)
    if set(summary["rule_id"].astype(str)) != EXPECTED_RULE_IDS:
        fail(f"summary rule ids mismatch: {sorted(set(summary['rule_id'].astype(str)))}")
    if len(summary) != len(EXPECTED_RULE_IDS):
        fail(f"summary must have one row per rule; got {len(summary)}")
    for _, row in summary.iterrows():
        rule_id = row["rule_id"]
        detail_rule = detail[detail["rule_id"].eq(rule_id)]
        selected_detail = detail_rule[detail_rule["selected_for_rule_replay"].eq("true")]
        outcome_detail = selected_detail[selected_detail["outcome_available"].eq("true")]
        if int(to_number(row["rule_source_rows"])) != len(detail_rule):
            fail(f"{rule_id} rule_source_rows does not match detail")
        if int(to_number(row["selected_rows"])) != len(selected_detail):
            fail(f"{rule_id} selected_rows does not match detail")
        if int(to_number(row["outcome_available_rows"])) != len(outcome_detail):
            fail(f"{rule_id} outcome_available_rows does not match detail")

    baseline = summary[summary["rule_id"].eq(BASELINE_RULE_ID)].iloc[0]
    if int(to_number(baseline["outcome_available_rows"])) != 470:
        fail("baseline outcome_available_rows must remain 470")
    if int(to_number(baseline["mature_sample_size"])) != 52:
        fail("baseline mature_sample_size must remain 52")
    assert_close(baseline["volume_breakout_rate_pct"], 11.9149, "baseline volume_breakout_rate_pct")
    assert_close(baseline["win_rate_pct"], 30.7692, "baseline win_rate_pct")
    assert_close(baseline["avg_a_return_pct"], 0.1621, "baseline avg_a_return_pct")

    micro45 = summary[summary["rule_id"].eq(MICRO45_RULE_ID)].iloc[0]
    if int(to_number(micro45["selected_rows"])) != 309:
        fail("nearest micro 45 selected_rows must remain 309")
    if int(to_number(micro45["outcome_available_rows"])) != 308:
        fail("nearest micro 45 outcome_available_rows must remain 308")
    if int(to_number(micro45["mature_sample_size"])) != 37:
        fail("nearest micro 45 mature_sample_size must remain 37")
    if to_number(micro45["delta_win_rate_pct"]) <= 0:
        fail("nearest micro 45 must remain directionally better than baseline win rate")
    if to_number(micro45["delta_avg_a_return_pct"]) <= 0:
        fail("nearest micro 45 must remain directionally better than baseline average return")
    if to_number(micro45["delta_volume_breakout_rate_pct"]) <= 0:
        fail("nearest micro 45 must remain directionally better than baseline volume breakout rate")

    micro90 = summary[summary["rule_id"].eq(MICRO90_RULE_ID)].iloc[0]
    if to_number(micro90["delta_avg_a_return_pct"]) < 0:
        fail("nearest micro 90 should not be worse than baseline average return in this replay")


def main() -> int:
    detail = read_csv(LATEST_DETAIL_CSV)
    detail_history = read_csv(HISTORY_DETAIL_CSV)
    summary = read_csv(LATEST_SUMMARY_CSV)
    summary_history = read_csv(HISTORY_SUMMARY_CSV)
    if not LATEST_MD.exists():
        fail(f"missing required markdown file: {LATEST_MD}")

    missing_detail = sorted(REQUIRED_DETAIL_COLUMNS - set(detail.columns))
    missing_detail_history = sorted(REQUIRED_DETAIL_COLUMNS - set(detail_history.columns))
    missing_summary = sorted(REQUIRED_SUMMARY_COLUMNS - set(summary.columns))
    missing_summary_history = sorted(REQUIRED_SUMMARY_COLUMNS - set(summary_history.columns))
    if missing_detail:
        fail(f"{LATEST_DETAIL_CSV} missing columns: {missing_detail}")
    if missing_detail_history:
        fail(f"{HISTORY_DETAIL_CSV} missing columns: {missing_detail_history}")
    if missing_summary:
        fail(f"{LATEST_SUMMARY_CSV} missing columns: {missing_summary}")
    if missing_summary_history:
        fail(f"{HISTORY_SUMMARY_CSV} missing columns: {missing_summary_history}")
    forbidden = sorted(
        (set(detail.columns) | set(detail_history.columns) | set(summary.columns) | set(summary_history.columns))
        & FORBIDDEN_PRODUCTION_FIELDS
    )
    if forbidden:
        fail(f"left-anchor replay must not emit production fields: {forbidden}")
    if len(detail) != len(detail_history):
        fail("latest/history detail row counts differ")
    if len(summary) != len(summary_history):
        fail("latest/history summary row counts differ")

    validate_detail(detail)
    validate_summary(summary, detail)

    md = LATEST_MD.read_text(encoding="utf-8", errors="replace")
    required_text = [
        "production impact: `none`",
        "candidate filters/quality segments",
        "nearest_micro_pressure",
        "8069",
        "6415",
        "A better human anchor match is not enough for promotion",
    ]
    for text in required_text:
        if text not in md:
            fail(f"markdown missing required text: {text}")

    print(f"W-bottom left-anchor rule replay validation passed detail_rows={len(detail)} summary_rows={len(summary)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
