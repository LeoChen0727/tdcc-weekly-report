from __future__ import annotations

from pathlib import Path

import pandas as pd


ROOT = Path(".")
RESEARCH_LATEST_DIR = ROOT / "output" / "latest" / "research_backtest"
RESEARCH_HISTORY_DIR = ROOT / "output" / "history" / "research"

LATEST_CSV = RESEARCH_LATEST_DIR / "w_bottom_manual_positive_missed_case_audit_latest.csv"
LATEST_MD = RESEARCH_LATEST_DIR / "w_bottom_manual_positive_missed_case_audit_latest.md"
HISTORY_CSV = RESEARCH_HISTORY_DIR / "w_bottom_manual_positive_missed_case_audit.csv"
CHART_ROOT = RESEARCH_LATEST_DIR / "w_bottom_manual_positive_missed_case_audit"

MODEL_ID = "w_bottom_right_side"
CONFIRMATION_MODEL_ID = "neckline_volume_breakout_confirmation"
RESEARCH_ID = "w_bottom_manual_positive_missed_case_audit"
SOURCE_RESEARCH_ID = "manual_user_positive_examples"
RESEARCH_VARIANT_ID = "warning_research_variant_only"

EXPECTED_STOCK_IDS = {"4916", "8069"}
EXPECTED_BLOCKERS = {
    "4916": "second_low_gap_above_standard_w_max",
    "8069": "insufficient_long_position_history",
}
EXPECTED_PATTERN_TYPES = {
    "4916": "higher_right_low_w_base",
    "8069": "standard_w_missed_by_history_gate",
}

REQUIRED_COLUMNS = {
    "model_id",
    "confirmation_model_id",
    "research_id",
    "source_research_id",
    "research_variant_id",
    "parameter_set_id",
    "advisory_status",
    "manual_case_id",
    "stock_id",
    "stock_name",
    "user_interval_start",
    "user_interval_end",
    "manual_pattern_type",
    "manual_left_peak_date",
    "manual_left_peak_price",
    "manual_left_low_date",
    "manual_left_low_price",
    "manual_neckline_date",
    "manual_neckline_price",
    "manual_right_low_date",
    "manual_right_low_price",
    "manual_observation_date",
    "manual_observation_close",
    "manual_breakout_date",
    "manual_breakout_close",
    "manual_breakout_volume_ratio",
    "first_high_volume_follow_through_date",
    "first_high_volume_follow_through_close",
    "first_high_volume_follow_through_volume_ratio",
    "second_low_gap_pct",
    "observation_to_neckline_pct",
    "observation_rebound_from_right_low_pct",
    "breakout_to_neckline_pct",
    "manual_first_arc_avg_volume",
    "manual_second_arc_avg_volume",
    "manual_second_arc_volume_ratio",
    "manual_first_arc_red_candle_ratio_pct",
    "manual_second_arc_red_candle_ratio_pct",
    "manual_second_minus_first_red_candle_ratio_pct",
    "valid_close_count_at_observation",
    "long_position_min_days",
    "observation_price_position_vs_median_pct",
    "current_quality_candidate_rows",
    "current_path_quality_candidate_rows",
    "current_price_level_candidate_rows",
    "missed_current_outputs",
    "current_detection_status",
    "current_detection_context",
    "relaxed_history_probe_date",
    "relaxed_history_detection_status",
    "relaxed_history_detection_context",
    "primary_blocker",
    "secondary_blocker",
    "current_gate_notes",
    "manual_read",
    "chart_path",
    "chart_path_absolute",
    "manual_review_status",
    "approved_for_daily",
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


def validate_constants(data: pd.DataFrame) -> None:
    expected = {
        "model_id": MODEL_ID,
        "confirmation_model_id": CONFIRMATION_MODEL_ID,
        "research_id": RESEARCH_ID,
        "source_research_id": SOURCE_RESEARCH_ID,
        "research_variant_id": RESEARCH_VARIANT_ID,
        "advisory_status": RESEARCH_VARIANT_ID,
        "manual_review_status": "pending_user_model_review",
        "production_readiness": "not_production_ready_research_only",
    }
    for column, value in expected.items():
        values = set(data[column].astype(str))
        if values != {value}:
            fail(f"{column} must be {value}; got {sorted(values)}")
    if not false_only(data["approved_for_daily"]):
        fail("approved_for_daily must remain false")


def validate_case_rows(data: pd.DataFrame) -> None:
    stock_ids = set(data["stock_id"].map(normalize_code))
    if stock_ids != EXPECTED_STOCK_IDS:
        fail(f"stock_id set must be {sorted(EXPECTED_STOCK_IDS)}; got {sorted(stock_ids)}")
    if len(data) != 2:
        fail(f"manual positive audit must contain exactly 2 rows; got {len(data)}")

    for _, row in data.iterrows():
        stock_id = normalize_code(row["stock_id"])
        if row["primary_blocker"] != EXPECTED_BLOCKERS[stock_id]:
            fail(f"{stock_id} primary_blocker must be {EXPECTED_BLOCKERS[stock_id]}; got {row['primary_blocker']}")
        if row["manual_pattern_type"] != EXPECTED_PATTERN_TYPES[stock_id]:
            fail(f"{stock_id} manual_pattern_type must be {EXPECTED_PATTERN_TYPES[stock_id]}; got {row['manual_pattern_type']}")
        if row["missed_current_outputs"].lower() != "true":
            fail(f"{stock_id} must remain marked missed_current_outputs=true")
        if row["current_detection_status"] != "missed_by_current_standard_w_detection":
            fail(f"{stock_id} current detection should be missed; got {row['current_detection_status']}")
        chart = Path(row["chart_path"])
        if not chart.exists():
            fail(f"{stock_id} chart does not exist: {chart}")
        if chart.stat().st_size < 10_000:
            fail(f"{stock_id} chart is suspiciously small: {chart}")
        for column in [
            "manual_left_peak_price",
            "manual_left_low_price",
            "manual_neckline_price",
            "manual_right_low_price",
            "manual_observation_close",
            "manual_first_arc_avg_volume",
            "manual_second_arc_avg_volume",
            "manual_second_arc_volume_ratio",
        ]:
            if pd.isna(to_number(row[column])):
                fail(f"{stock_id} numeric column is blank or invalid: {column}")

    row_4916 = data[data["stock_id"].map(normalize_code).eq("4916")].iloc[0]
    if to_number(row_4916["second_low_gap_pct"]) <= 6.0:
        fail("4916 must prove the right low is above the current standard-W second-low max")

    row_8069 = data[data["stock_id"].map(normalize_code).eq("8069")].iloc[0]
    if to_number(row_8069["valid_close_count_at_observation"]) >= to_number(row_8069["long_position_min_days"]):
        fail("8069 must prove the current long-position history gate is the blocker")
    if row_8069["relaxed_history_detection_status"] != "detected_if_history_gate_bypassed":
        fail("8069 should be detectable on the relaxed probe date when the history gate is bypassed")


def main() -> int:
    latest = read_csv(LATEST_CSV)
    history = read_csv(HISTORY_CSV)
    if not LATEST_MD.exists():
        fail(f"missing required file: {LATEST_MD}")
    if not CHART_ROOT.exists():
        fail(f"missing chart root: {CHART_ROOT}")

    missing = sorted(REQUIRED_COLUMNS - set(latest.columns))
    missing_history = sorted(REQUIRED_COLUMNS - set(history.columns))
    if missing:
        fail(f"{LATEST_CSV} missing columns: {missing}")
    if missing_history:
        fail(f"{HISTORY_CSV} missing columns: {missing_history}")
    forbidden = sorted((set(latest.columns) | set(history.columns)) & FORBIDDEN_PRODUCTION_FIELDS)
    if forbidden:
        fail(f"manual positive missed-case audit must not emit production fields: {forbidden}")
    if len(latest) != len(history):
        fail("latest/history row counts differ")

    validate_constants(latest)
    validate_constants(history)
    validate_case_rows(latest)

    md = LATEST_MD.read_text(encoding="utf-8", errors="replace")
    required_text = [
        "production impact: `none`",
        "manual positive examples are research evidence only",
        "4916",
        "8069",
        "higher-right-low",
        "180-valid-close",
    ]
    for text in required_text:
        if text not in md:
            fail(f"markdown missing required text: {text}")

    print(f"OK: validated {LATEST_CSV} rows={len(latest)}")
    print(f"OK: validated charts under {CHART_ROOT}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
