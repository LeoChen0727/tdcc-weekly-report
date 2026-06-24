from __future__ import annotations

from pathlib import Path

import pandas as pd


ROOT = Path(".")
RESEARCH_LATEST_DIR = ROOT / "output" / "latest" / "research_backtest"
RESEARCH_HISTORY_DIR = ROOT / "output" / "history" / "research"

SOURCE_EVENTS_CSV = RESEARCH_HISTORY_DIR / "w_bottom_tdcc_abc_events.csv"
LATEST_AUDIT_CSV = RESEARCH_LATEST_DIR / "w_bottom_candidate_quality_audit_latest.csv"
LATEST_AUDIT_MD = RESEARCH_LATEST_DIR / "w_bottom_candidate_quality_audit_latest.md"
HISTORY_AUDIT_CSV = RESEARCH_HISTORY_DIR / "w_bottom_candidate_quality_audit.csv"

REQUIRED_COLUMNS = {
    "model_id",
    "confirmation_model_id",
    "research_id",
    "source_research_id",
    "research_variant_id",
    "advisory_status",
    "sample_mode",
    "stock_id",
    "stock_name",
    "signal_date",
    "left_peak_date",
    "left_low_date",
    "neckline_date",
    "right_low_date",
    "neckline_price",
    "right_low_value",
    "signal_distance_to_neckline_pct",
    "signal_rebound_from_right_low_pct",
    "signal_near_neckline_zone",
    "first_rebound_days",
    "right_rebound_days_at_signal",
    "second_arc_volume_ratio",
    "sym1_5_w_shape_completed",
    "sym1_5_neckline_volume_breakout",
    "sym1_5_quality_bucket",
    "sym2_0_w_shape_completed",
    "sym2_0_neckline_volume_breakout",
    "sym2_0_quality_bucket",
    "primary_review_flag",
    "approved_for_daily",
    "generated_at",
}

QUALITY_BUCKETS = {
    "neckline_volume_breakout",
    "already_near_neckline_at_signal",
    "completed_without_volume_breakout",
    "right_low_broken_before_completion",
    "future_window_incomplete",
    "late_volume_breakout_not_w",
    "late_neckline_completion_not_w",
    "right_low_broken_after_deadline",
    "no_completion_within_symmetry",
    "price_history_missing",
    "price_date_missing",
    "invalid_price_inputs",
}

REVIEW_FLAGS = {
    "passed_volume_breakout_confirmation",
    "candidate_selected_too_near_neckline",
    "shape_completed_but_volume_missing",
    "right_low_failed",
    "completion_too_late_for_w",
    "did_not_complete_w",
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


def false_only(series: pd.Series) -> bool:
    return set(series.astype(str).str.lower().unique()) <= {"false", "0", ""}


def boolish_only(series: pd.Series) -> bool:
    return set(series.astype(str).str.lower().unique()) <= {"true", "false", "1", "0", ""}


def validate_dates(df: pd.DataFrame, columns: list[str]) -> None:
    for column in columns:
        parsed = pd.to_datetime(df[column], format="%Y%m%d", errors="coerce")
        if parsed.isna().any():
            fail(f"{column} must contain valid YYYYMMDD dates")


def main() -> int:
    latest = read_csv(LATEST_AUDIT_CSV)
    history = read_csv(HISTORY_AUDIT_CSV)
    source = read_csv(SOURCE_EVENTS_CSV)
    if not LATEST_AUDIT_MD.exists():
        fail(f"missing required file: {LATEST_AUDIT_MD}")
    md_lines = LATEST_AUDIT_MD.read_text(encoding="utf-8", errors="replace").splitlines()
    if len(md_lines) < 30:
        fail(f"{LATEST_AUDIT_MD} is suspiciously short")
    if latest.empty:
        fail(f"{LATEST_AUDIT_CSV} has no rows")
    if history.empty:
        fail(f"{HISTORY_AUDIT_CSV} has no rows")
    if len(latest) != len(history):
        fail("latest and history audit row counts differ")

    missing = sorted(REQUIRED_COLUMNS - set(latest.columns))
    if missing:
        fail(f"{LATEST_AUDIT_CSV} missing columns: {missing}")
    missing_history = sorted(REQUIRED_COLUMNS - set(history.columns))
    if missing_history:
        fail(f"{HISTORY_AUDIT_CSV} missing columns: {missing_history}")

    forbidden = sorted((set(latest.columns) | set(history.columns)) & FORBIDDEN_PRODUCTION_FIELDS)
    if forbidden:
        fail(f"W-bottom quality audit must not emit production decision fields: {forbidden}")

    dedup_source = source[
        source["symmetry_ratio"].astype(str).eq("1.5")
        & source["dedup_20d_eligible"].astype(str).str.lower().isin(["true", "1"])
    ]
    if len(latest) != len(dedup_source):
        fail(f"audit rows must equal dedup strict source events: audit={len(latest)} source={len(dedup_source)}")

    if set(latest["model_id"].astype(str)) != {"w_bottom_right_side"}:
        fail("audit model_id must be w_bottom_right_side")
    if set(latest["confirmation_model_id"].astype(str)) != {"neckline_volume_breakout_confirmation"}:
        fail("audit confirmation_model_id must be neckline_volume_breakout_confirmation")
    if set(latest["research_id"].astype(str)) != {"w_bottom_candidate_quality_audit"}:
        fail("audit research_id must be w_bottom_candidate_quality_audit")
    if set(latest["source_research_id"].astype(str)) != {"w_bottom_tdcc_abc_backtest"}:
        fail("audit source_research_id must be w_bottom_tdcc_abc_backtest")
    if set(latest["research_variant_id"].astype(str)) != {"warning_research_variant_only"}:
        fail("audit must be marked warning_research_variant_only")
    if set(latest["advisory_status"].astype(str)) != {"warning_research_variant_only"}:
        fail("audit advisory_status must be warning_research_variant_only")
    if not false_only(latest["approved_for_daily"]):
        fail("audit approved_for_daily must remain false")

    date_cols = ["signal_date", "left_peak_date", "left_low_date", "neckline_date", "right_low_date"]
    validate_dates(latest, date_cols)
    for column in [
        "signal_near_neckline_zone",
        "signal_above_neckline",
        "sym1_5_w_shape_completed",
        "sym1_5_neckline_volume_breakout",
        "sym2_0_w_shape_completed",
        "sym2_0_neckline_volume_breakout",
    ]:
        if not boolish_only(latest[column]):
            fail(f"{column} must be boolean-like")

    invalid_buckets = sorted((set(latest["sym1_5_quality_bucket"]) | set(latest["sym2_0_quality_bucket"])) - QUALITY_BUCKETS)
    if invalid_buckets:
        fail(f"unexpected quality buckets: {invalid_buckets}")
    invalid_flags = sorted(set(latest["primary_review_flag"]) - REVIEW_FLAGS)
    if invalid_flags:
        fail(f"unexpected primary_review_flag values: {invalid_flags}")

    strict_completed = latest["sym1_5_w_shape_completed"].astype(str).str.lower().isin(["true", "1"])
    missing_completion_date = latest[strict_completed & latest["sym1_5_completion_date"].astype(str).eq("")]
    if not missing_completion_date.empty:
        fail("strict completed rows must have sym1_5_completion_date")
    strict_breakout = latest["sym1_5_neckline_volume_breakout"].astype(str).str.lower().isin(["true", "1"])
    missing_breakout_date = latest[strict_breakout & latest["sym1_5_breakout_date"].astype(str).eq("")]
    if not missing_breakout_date.empty:
        fail("strict volume-breakout rows must have sym1_5_breakout_date")

    print(
        "W-bottom candidate quality audit validation passed "
        f"rows={len(latest)} strict_breakouts={int(strict_breakout.sum())}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
