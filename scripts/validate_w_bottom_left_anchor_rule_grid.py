from __future__ import annotations

from pathlib import Path

import pandas as pd


ROOT = Path(".")
RESEARCH_LATEST_DIR = ROOT / "output" / "latest" / "research_backtest"
RESEARCH_HISTORY_DIR = ROOT / "output" / "history" / "research"

SOURCE_ANCHOR_DETAIL_CSV = RESEARCH_LATEST_DIR / "w_bottom_left_anchor_pattern_family_audit_detail_latest.csv"
LATEST_DETAIL_CSV = RESEARCH_LATEST_DIR / "w_bottom_left_anchor_rule_grid_detail_latest.csv"
LATEST_SUMMARY_CSV = RESEARCH_LATEST_DIR / "w_bottom_left_anchor_rule_grid_latest.csv"
LATEST_MD = RESEARCH_LATEST_DIR / "w_bottom_left_anchor_rule_grid_latest.md"
HISTORY_DETAIL_CSV = RESEARCH_HISTORY_DIR / "w_bottom_left_anchor_rule_grid_detail.csv"
HISTORY_SUMMARY_CSV = RESEARCH_HISTORY_DIR / "w_bottom_left_anchor_rule_grid.csv"

MODEL_ID = "w_bottom_right_side"
CONFIRMATION_MODEL_ID = "neckline_volume_breakout_confirmation"
RESEARCH_ID = "w_bottom_left_anchor_rule_grid"
SOURCE_RESEARCH_ID = "w_bottom_left_anchor_pattern_family_audit"
RESEARCH_VARIANT_ID = "warning_research_variant_only"
STANDARD_W_FAMILY = "standard_double_bottom_w"

EXPECTED_RULE_IDS = {
    "current_detector_left_peak",
    "highest_high_45d_before_left_low",
    "highest_high_90d_before_left_low",
    "nearest_micro_pressure_45d_min15_before_left_low",
    "nearest_micro_pressure_90d_min15_before_left_low",
}

REQUIRED_DETAIL_COLUMNS = {
    "model_id",
    "confirmation_model_id",
    "research_id",
    "source_research_id",
    "research_variant_id",
    "parameter_set_id",
    "advisory_status",
    "source_audit_scope",
    "case_review_tag",
    "manual_case_id",
    "stock_id",
    "stock_name",
    "signal_date",
    "source_pattern_family",
    "rule_id",
    "rule_window_days",
    "selector_method",
    "baseline_current_left_peak_date",
    "human_left_peak_date",
    "left_low_date",
    "neckline_date",
    "right_low_date",
    "candidate_left_peak_date",
    "candidate_left_peak_price",
    "candidate_days_before_left_low",
    "candidate_drop_to_left_low_pct",
    "candidate_left_descent_wrong_direction_rate_pct",
    "candidate_anchor_delta_vs_current_days",
    "candidate_anchor_delta_vs_human_days",
    "candidate_matches_current_left_peak",
    "candidate_matches_human_left_peak",
    "candidate_anchor_changed_from_current",
    "candidate_inside_current_45d_window",
    "candidate_selection_status",
    "candidate_selection_reason",
    "transition_status",
    "slope_curvature_category",
    "price_level_bucket",
    "anchor_issue_type",
    "recommended_next_research_action",
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
    "row_count",
    "selected_count",
    "selection_rate_pct",
    "anchor_changed_count",
    "anchor_changed_rate_pct",
    "human_match_count",
    "human_match_rate_pct",
    "avg_candidate_days_before_left_low",
    "median_candidate_days_before_left_low",
    "avg_drop_to_left_low_pct",
    "median_drop_to_left_low_pct",
    "avg_left_descent_wrong_direction_rate_pct",
    "median_left_descent_wrong_direction_rate_pct",
    "inside_current_45d_window_count",
    "manual_positive_rows",
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


def validate_constants(df: pd.DataFrame, require_approved: bool = False) -> None:
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
    if "source_research_id" in df.columns:
        values = set(df["source_research_id"].astype(str))
        if values != {SOURCE_RESEARCH_ID}:
            fail(f"source_research_id must be {SOURCE_RESEARCH_ID}; got {sorted(values)}")
    if require_approved and not false_only(df["approved_for_daily"]):
        fail("approved_for_daily must remain false")


def validate_detail(detail: pd.DataFrame) -> None:
    validate_constants(detail, require_approved=True)
    source = read_csv(SOURCE_ANCHOR_DETAIL_CSV)
    source["stock_id"] = source["stock_id"].map(normalize_code)
    standard_rows = source[source["computed_pattern_family"].eq(STANDARD_W_FAMILY)].copy()
    expected_rows = len(standard_rows) * len(EXPECTED_RULE_IDS)
    if len(detail) != expected_rows:
        fail(f"detail row count must be {expected_rows}; got {len(detail)}")
    if set(detail["rule_id"].astype(str)) != EXPECTED_RULE_IDS:
        fail(f"unexpected rule ids: {sorted(set(detail['rule_id'].astype(str)))}")
    counts = detail.groupby("rule_id")["stock_id"].count().to_dict()
    for rule_id, count in counts.items():
        if count != len(standard_rows):
            fail(f"{rule_id} must have {len(standard_rows)} rows; got {count}")
    if detail["source_pattern_family"].ne(STANDARD_W_FAMILY).any():
        fail("rule grid must only include standard_double_bottom_w source rows")
    if detail["stock_id"].map(normalize_code).eq("4916").any():
        fail("4916 higher-right-low manual case must not be included in the standard-W rule grid")

    row_8069_micro = detail[
        detail["stock_id"].map(normalize_code).eq("8069")
        & detail["rule_id"].eq("nearest_micro_pressure_45d_min15_before_left_low")
    ]
    if len(row_8069_micro) != 1:
        fail("expected one 8069 nearest_micro_pressure_45d row")
    r8069 = row_8069_micro.iloc[0]
    if r8069["candidate_left_peak_date"] != "20260311":
        fail("8069 nearest micro pressure rule must select 20260311")
    if r8069["candidate_matches_human_left_peak"].lower() != "true":
        fail("8069 nearest micro pressure rule must match the human 20260312 anchor within tolerance")
    if abs(to_number(r8069["candidate_anchor_delta_vs_human_days"])) > 2:
        fail("8069 nearest micro pressure rule must stay within +/-2 trading days of the human anchor")

    row_8069_current = detail[
        detail["stock_id"].map(normalize_code).eq("8069")
        & detail["rule_id"].eq("current_detector_left_peak")
    ].iloc[0]
    if row_8069_current["candidate_left_peak_date"] != "20260211":
        fail("8069 current detector rule must preserve 20260211")
    if row_8069_current["candidate_matches_human_left_peak"].lower() != "false":
        fail("8069 current detector rule must not match the human anchor")

    row_6415_high90 = detail[
        detail["stock_id"].map(normalize_code).eq("6415")
        & detail["signal_date"].eq("20260115")
        & detail["rule_id"].eq("highest_high_90d_before_left_low")
    ]
    if len(row_6415_high90) != 1:
        fail("expected one 6415 highest_high_90d row")
    r6415 = row_6415_high90.iloc[0]
    if r6415["candidate_left_peak_date"] != "20250718":
        fail("6415 highest_high_90d must preserve the 20250718 earlier high comparison")
    if to_number(r6415["candidate_days_before_left_low"]) < 80:
        fail("6415 highest_high_90d should expose an early structural high around 81 trading days before the low")


def validate_summary(summary: pd.DataFrame, detail: pd.DataFrame) -> None:
    validate_constants(summary)
    if set(summary["rule_id"].astype(str)) != EXPECTED_RULE_IDS:
        fail(f"summary rule ids mismatch: {sorted(set(summary['rule_id'].astype(str)))}")
    if len(summary) != len(EXPECTED_RULE_IDS):
        fail(f"summary must have one row per rule; got {len(summary)}")
    detail_counts = detail.groupby("rule_id").size().to_dict()
    for _, row in summary.iterrows():
        rule_id = row["rule_id"]
        if int(to_number(row["row_count"])) != detail_counts[rule_id]:
            fail(f"{rule_id} summary row_count does not match detail")
    micro45 = summary[summary["rule_id"].eq("nearest_micro_pressure_45d_min15_before_left_low")].iloc[0]
    if int(to_number(micro45["human_match_count"])) != 1:
        fail("nearest_micro_pressure_45d must have exactly one human-match row")
    high90 = summary[summary["rule_id"].eq("highest_high_90d_before_left_low")].iloc[0]
    high45 = summary[summary["rule_id"].eq("highest_high_45d_before_left_low")].iloc[0]
    if to_number(high90["anchor_changed_count"]) <= to_number(high45["anchor_changed_count"]):
        fail("highest_high_90d should change more anchors than highest_high_45d")


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
        fail(f"left-anchor rule grid must not emit production fields: {forbidden}")
    if len(detail) != len(detail_history):
        fail("latest/history detail row counts differ")
    if len(summary) != len(summary_history):
        fail("latest/history summary row counts differ")

    validate_detail(detail)
    validate_summary(summary, detail)

    md = LATEST_MD.read_text(encoding="utf-8", errors="replace")
    required_text = [
        "production impact: `none`",
        "research-only comparison",
        "nearest_micro_pressure",
        "highest_high_90d",
        "8069",
        "6415",
        "15.0",
    ]
    for text in required_text:
        if text not in md:
            fail(f"markdown missing required text: {text}")

    print(f"W-bottom left-anchor rule grid validation passed detail_rows={len(detail)} summary_rows={len(summary)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
