from __future__ import annotations

from pathlib import Path

import pandas as pd


ROOT = Path(".")
RESEARCH_LATEST_DIR = ROOT / "output" / "latest" / "research_backtest"
RESEARCH_HISTORY_DIR = ROOT / "output" / "history" / "research"

SOURCE_QUALITY_CSV = RESEARCH_LATEST_DIR / "w_bottom_candidate_quality_audit_latest.csv"
SOURCE_MANUAL_POSITIVE_CSV = RESEARCH_LATEST_DIR / "w_bottom_manual_positive_missed_case_audit_latest.csv"

LATEST_DETAIL_CSV = RESEARCH_LATEST_DIR / "w_bottom_left_anchor_pattern_family_audit_detail_latest.csv"
LATEST_SUMMARY_CSV = RESEARCH_LATEST_DIR / "w_bottom_left_anchor_pattern_family_audit_latest.csv"
LATEST_MD = RESEARCH_LATEST_DIR / "w_bottom_left_anchor_pattern_family_audit_latest.md"
HISTORY_DETAIL_CSV = RESEARCH_HISTORY_DIR / "w_bottom_left_anchor_pattern_family_audit_detail.csv"
HISTORY_SUMMARY_CSV = RESEARCH_HISTORY_DIR / "w_bottom_left_anchor_pattern_family_audit.csv"

MODEL_ID = "w_bottom_right_side"
CONFIRMATION_MODEL_ID = "neckline_volume_breakout_confirmation"
RESEARCH_ID = "w_bottom_left_anchor_pattern_family_audit"
RESEARCH_VARIANT_ID = "warning_research_variant_only"

REQUIRED_DETAIL_COLUMNS = {
    "model_id",
    "confirmation_model_id",
    "research_id",
    "source_research_id",
    "research_variant_id",
    "parameter_set_id",
    "advisory_status",
    "audit_scope",
    "case_review_tag",
    "manual_case_id",
    "stock_id",
    "stock_name",
    "signal_date",
    "user_interval_start",
    "user_interval_end",
    "transition_status",
    "slope_curvature_category",
    "price_level_bucket",
    "effective_mainstream_label",
    "human_pattern_type",
    "computed_pattern_family",
    "human_left_peak_date",
    "human_left_low_date",
    "human_neckline_date",
    "human_right_low_date",
    "auto_left_peak_date",
    "auto_left_peak_price",
    "auto_left_low_date",
    "auto_left_low_price",
    "auto_neckline_date",
    "auto_neckline_price",
    "auto_right_low_date",
    "auto_right_low_price",
    "second_low_gap_pct",
    "first_drop_pct",
    "neckline_depth_from_left_low_pct",
    "neckline_depth_from_right_low_pct",
    "auto_left_peak_days_before_left_low",
    "auto_selected_at_search_window_edge",
    "highest_pre_left_low_90_date",
    "highest_pre_left_low_90_price",
    "highest_pre_left_low_90_days_before_low",
    "highest_pre_left_low_90_diff_vs_auto_peak_pct",
    "higher_pre_left_low_90_outside_current_window",
    "human_auto_left_peak_delta_trading_days",
    "human_auto_left_low_delta_trading_days",
    "human_auto_neckline_delta_trading_days",
    "human_auto_right_low_delta_trading_days",
    "anchor_issue_type",
    "anchor_issue_reason",
    "recommended_next_research_action",
    "chart_path",
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
    "summary_dimension",
    "summary_value",
    "row_count",
    "current_candidate_count",
    "manual_positive_count",
    "anchor_issue_count",
    "anchor_issue_rate_pct",
    "standard_double_bottom_w_count",
    "higher_right_low_base_w_count",
    "search_window_edge_count",
    "higher_alt_peak_count",
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

EXPECTED_PATTERN_FAMILIES = {
    "standard_double_bottom_w",
    "higher_right_low_base_w",
}

EXPECTED_ANCHOR_ISSUES = {
    "no_anchor_issue_detected",
    "auto_left_peak_near_search_window_edge",
    "higher_pre_left_low_peak_outside_45d_window",
    "human_auto_left_peak_mismatch",
    "manual_positive_no_current_auto_anchor",
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


def validate_constants(df: pd.DataFrame) -> None:
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


def validate_detail(detail: pd.DataFrame) -> None:
    validate_constants(detail)
    if not false_only(detail["approved_for_daily"]):
        fail("approved_for_daily must remain false")
    unexpected_families = sorted(set(detail["computed_pattern_family"].astype(str)) - EXPECTED_PATTERN_FAMILIES)
    if unexpected_families:
        fail(f"unexpected pattern families: {unexpected_families}")
    unexpected_issues = sorted(set(detail["anchor_issue_type"].astype(str)) - EXPECTED_ANCHOR_ISSUES)
    if unexpected_issues:
        fail(f"unexpected anchor issue types: {unexpected_issues}")

    source_quality = read_csv(SOURCE_QUALITY_CSV)
    source_manual = read_csv(SOURCE_MANUAL_POSITIVE_CSV)
    expected_rows = len(source_quality) + len(source_manual)
    if len(detail) != expected_rows:
        fail(f"detail rows must equal quality+manual rows {expected_rows}; got {len(detail)}")
    current_count = int(detail["audit_scope"].eq("current_model_candidate").sum())
    manual_count = int(detail["audit_scope"].eq("manual_positive_missed_case").sum())
    if current_count != len(source_quality):
        fail(f"current_model_candidate count mismatch: expected {len(source_quality)} got {current_count}")
    if manual_count != len(source_manual):
        fail(f"manual_positive_missed_case count mismatch: expected {len(source_manual)} got {manual_count}")

    row_4916 = detail[detail["stock_id"].map(normalize_code).eq("4916")]
    row_8069 = detail[detail["stock_id"].map(normalize_code).eq("8069")]
    row_6415 = detail[
        detail["stock_id"].map(normalize_code).eq("6415")
        & detail["signal_date"].astype(str).eq("20260115")
    ]
    if len(row_4916) != 1 or len(row_8069) != 1 or len(row_6415) != 1:
        fail("expected exactly one key row each for 4916, 8069, and 6415/20260115")

    r4916 = row_4916.iloc[0]
    if r4916["computed_pattern_family"] != "higher_right_low_base_w":
        fail("4916 must be classified as higher_right_low_base_w")
    if r4916["anchor_issue_type"] != "manual_positive_no_current_auto_anchor":
        fail("4916 must remain a manual positive with no current auto anchor")
    if r4916["recommended_next_research_action"] != "split_higher_right_low_base_from_standard_w":
        fail("4916 must recommend splitting higher-right-low base from standard W")
    if to_number(r4916["second_low_gap_pct"]) <= 6.0:
        fail("4916 second_low_gap_pct must remain above the current standard-W max")

    r8069 = row_8069.iloc[0]
    if r8069["computed_pattern_family"] != "standard_double_bottom_w":
        fail("8069 must be classified as standard_double_bottom_w")
    if r8069["anchor_issue_type"] != "human_auto_left_peak_mismatch":
        fail("8069 must preserve human/auto left-peak mismatch")
    if r8069["human_left_peak_date"] != "20260312" or r8069["auto_left_peak_date"] != "20260211":
        fail("8069 must preserve human 20260312 vs auto 20260211 left-peak comparison")

    r6415 = row_6415.iloc[0]
    if r6415["case_review_tag"] != "user_question_auto_anchor_only":
        fail("6415/20260115 must remain tagged as user_question_auto_anchor_only")
    if r6415["anchor_issue_type"] != "higher_pre_left_low_peak_outside_45d_window":
        fail("6415/20260115 must remain flagged for a higher pre-low peak outside the 45-day window")
    if r6415["highest_pre_left_low_90_date"] != "20250718":
        fail("6415/20260115 must preserve the 20250718 earlier high comparison")
    if to_number(r6415["highest_pre_left_low_90_diff_vs_auto_peak_pct"]) < 20.0:
        fail("6415/20260115 earlier high comparison must remain at least 20% above the auto left peak")


def validate_summary(summary: pd.DataFrame, detail: pd.DataFrame) -> None:
    validate_constants(summary)
    if summary.empty:
        fail("summary must not be empty")
    overall = summary[
        summary["summary_dimension"].eq("overall")
        & summary["summary_value"].eq("all")
    ]
    if len(overall) != 1:
        fail("summary must contain exactly one overall/all row")
    row = overall.iloc[0]
    if int(to_number(row["row_count"])) != len(detail):
        fail("overall summary row_count does not match detail")
    issue_count = int((~detail["anchor_issue_type"].eq("no_anchor_issue_detected")).sum())
    if int(to_number(row["anchor_issue_count"])) != issue_count:
        fail("overall summary anchor_issue_count does not match detail")
    if int(to_number(row["higher_right_low_base_w_count"])) != 1:
        fail("overall summary must have exactly one higher_right_low_base_w row")


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
        fail(f"left-anchor audit must not emit production fields: {forbidden}")
    if len(detail) != len(detail_history):
        fail("latest/history detail row counts differ")
    if len(summary) != len(summary_history):
        fail("latest/history summary row counts differ")

    validate_detail(detail)
    validate_summary(summary, detail)

    md = LATEST_MD.read_text(encoding="utf-8", errors="replace")
    required_text = [
        "production impact: `none`",
        "left_peak_start_selection",
        "standard_double_bottom_w",
        "higher_right_low_base_w",
        "4916",
        "8069",
        "6415",
        "20.0",
    ]
    for text in required_text:
        if text not in md:
            fail(f"markdown missing required text: {text}")

    print(
        "W-bottom left-anchor/pattern-family audit validation passed "
        f"detail_rows={len(detail)} summary_rows={len(summary)}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
