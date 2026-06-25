from __future__ import annotations

from pathlib import Path

import pandas as pd


ROOT = Path(".")
RESEARCH_LATEST_DIR = ROOT / "output" / "latest" / "research_backtest"
RESEARCH_HISTORY_DIR = ROOT / "output" / "history" / "research"

SOURCE_DETAIL_CSV = RESEARCH_LATEST_DIR / "w_bottom_path_quality_filter_audit_detail_latest.csv"
LATEST_SUMMARY_CSV = RESEARCH_LATEST_DIR / "w_bottom_price_level_audit_latest.csv"
LATEST_DETAIL_CSV = RESEARCH_LATEST_DIR / "w_bottom_price_level_audit_detail_latest.csv"
LATEST_MD = RESEARCH_LATEST_DIR / "w_bottom_price_level_audit_latest.md"
HISTORY_SUMMARY_CSV = RESEARCH_HISTORY_DIR / "w_bottom_price_level_audit.csv"
HISTORY_DETAIL_CSV = RESEARCH_HISTORY_DIR / "w_bottom_price_level_audit_detail.csv"

MODEL_ID = "w_bottom_right_side"
CONFIRMATION_MODEL_ID = "neckline_volume_breakout_confirmation"
RESEARCH_ID = "w_bottom_price_level_audit"
SOURCE_RESEARCH_ID = "w_bottom_path_quality_filter_audit"
RESEARCH_VARIANT_ID = "warning_research_variant_only"
OBSERVATION_TO_VOLUME = "observation_to_volume_confirmation"
WV_CATEGORY = "wv_multiple_turn_risk"

REQUIRED_DETAIL_COLUMNS = {
    "model_id",
    "confirmation_model_id",
    "research_id",
    "source_research_id",
    "research_variant_id",
    "advisory_status",
    "stock_id",
    "signal_date",
    "transition_status",
    "slope_curvature_category",
    "a_mature",
    "a_return_pct",
    "tdcc_any_age7",
    "effective_mainstream_label",
    "lookback_days_requested",
    "min_price_history_days",
    "lookback_observed_days",
    "lookback_start_date",
    "lookback_end_date",
    "signal_close",
    "lookback_low_price",
    "lookback_high_price",
    "lookback_close_median",
    "lookback_close_mean",
    "price_position_252_pct",
    "below_252_median",
    "below_252_mean",
    "source_long_position_gate_passed",
    "price_level_bucket",
    "price_level_available",
    "core_mainstream_exclude_wv_review_candidate",
    "manual_review_status",
    "approved_for_daily",
    "production_readiness",
    "generated_at",
}

REQUIRED_SUMMARY_COLUMNS = {
    "model_id",
    "confirmation_model_id",
    "research_id",
    "source_research_id",
    "research_variant_id",
    "advisory_status",
    "summary_scope",
    "price_level_bucket",
    "sample_size",
    "price_level_available_count",
    "below_252_median_count",
    "source_long_position_gate_pass_count",
    "volume_confirmation_count",
    "volume_confirmation_rate_pct",
    "mature_sample_size",
    "win_count",
    "win_rate_pct",
    "avg_a_return_pct",
    "median_a_return_pct",
    "avg_price_position_252_pct",
    "median_price_position_252_pct",
    "approved_for_daily",
    "production_readiness",
    "generated_at",
}

EXPECTED_SCOPES = {
    "all_w_bottom_candidates",
    "observation_to_volume_confirmation",
    "observation_volume_exclude_wv",
    "core_mainstream_observation_volume_exclude_wv",
}

EXPECTED_BUCKETS = {
    "bottom_quartile_level",
    "low_level",
    "mid_level",
    "high_level",
    "price_history_insufficient",
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


def true_only(series: pd.Series) -> bool:
    return set(series.astype(str).str.lower().unique()) <= {"true", "1"}


def bool_series(series: pd.Series) -> pd.Series:
    return series.astype(str).str.lower().isin(["true", "1", "yes", "y"])


def numeric_series(df: pd.DataFrame, column: str) -> pd.Series:
    return pd.to_numeric(df[column], errors="coerce")


def validate_constants(df: pd.DataFrame, label: str) -> None:
    constants = {
        "model_id": MODEL_ID,
        "confirmation_model_id": CONFIRMATION_MODEL_ID,
        "research_id": RESEARCH_ID,
        "source_research_id": SOURCE_RESEARCH_ID,
        "research_variant_id": RESEARCH_VARIANT_ID,
        "advisory_status": RESEARCH_VARIANT_ID,
        "production_readiness": "not_production_ready_research_only",
    }
    for column, expected in constants.items():
        values = set(df[column].astype(str))
        if values != {expected}:
            fail(f"{label} {column} must be {expected}; got {sorted(values)}")
    if not false_only(df["approved_for_daily"]):
        fail(f"{label} approved_for_daily must remain false")


def main() -> int:
    source = read_csv(SOURCE_DETAIL_CSV)
    latest_detail = read_csv(LATEST_DETAIL_CSV)
    history_detail = read_csv(HISTORY_DETAIL_CSV)
    latest_summary = read_csv(LATEST_SUMMARY_CSV)
    history_summary = read_csv(HISTORY_SUMMARY_CSV)

    if not LATEST_MD.exists():
        fail(f"missing required file: {LATEST_MD}")
    md_text = LATEST_MD.read_text(encoding="utf-8", errors="replace")
    if len(md_text.splitlines()) < 45:
        fail(f"{LATEST_MD} is suspiciously short")
    if "production impact: `none`" not in md_text:
        fail("markdown must explicitly state production impact is none")
    if "signal close <= 252-day median close" not in md_text:
        fail("markdown must document the existing 252-day median gate")

    missing_detail = sorted(REQUIRED_DETAIL_COLUMNS - set(latest_detail.columns))
    missing_history_detail = sorted(REQUIRED_DETAIL_COLUMNS - set(history_detail.columns))
    missing_summary = sorted(REQUIRED_SUMMARY_COLUMNS - set(latest_summary.columns))
    missing_history_summary = sorted(REQUIRED_SUMMARY_COLUMNS - set(history_summary.columns))
    if missing_detail:
        fail(f"{LATEST_DETAIL_CSV} missing columns: {missing_detail}")
    if missing_history_detail:
        fail(f"{HISTORY_DETAIL_CSV} missing columns: {missing_history_detail}")
    if missing_summary:
        fail(f"{LATEST_SUMMARY_CSV} missing columns: {missing_summary}")
    if missing_history_summary:
        fail(f"{HISTORY_SUMMARY_CSV} missing columns: {missing_history_summary}")

    forbidden = sorted(
        (
            set(latest_detail.columns)
            | set(history_detail.columns)
            | set(latest_summary.columns)
            | set(history_summary.columns)
        )
        & FORBIDDEN_PRODUCTION_FIELDS
    )
    if forbidden:
        fail(f"price-level audit must not emit production decision fields: {forbidden}")

    if len(latest_detail) != len(source):
        fail(f"detail row count must match source detail: latest={len(latest_detail)} source={len(source)}")
    if len(history_detail) != len(latest_detail):
        fail("latest/history detail row counts differ")
    if len(history_summary) != len(latest_summary):
        fail("latest/history summary row counts differ")
    if latest_summary.empty:
        fail("summary has no rows")

    validate_constants(latest_detail, "latest detail")
    validate_constants(history_detail, "history detail")
    validate_constants(latest_summary, "latest summary")
    validate_constants(history_summary, "history summary")

    if not true_only(latest_detail["price_level_available"]):
        fail("all current W-bottom candidates should have enough price history for price-level audit")
    if not true_only(latest_detail["source_long_position_gate_passed"]):
        fail("source long-position median gate should pass for every source candidate")
    observed_days = numeric_series(latest_detail, "lookback_observed_days")
    min_days = numeric_series(latest_detail, "min_price_history_days")
    if observed_days.lt(min_days).any():
        fail("lookback_observed_days must be >= min_price_history_days for every detail row")
    positions = numeric_series(latest_detail, "price_position_252_pct")
    if positions.isna().any() or positions.lt(0).any() or positions.gt(100).any():
        fail("price_position_252_pct must be numeric between 0 and 100")
    low_prices = numeric_series(latest_detail, "lookback_low_price")
    high_prices = numeric_series(latest_detail, "lookback_high_price")
    signal_close = numeric_series(latest_detail, "signal_close")
    if low_prices.isna().any() or high_prices.isna().any() or signal_close.isna().any():
        fail("price-level numeric fields must not be blank")
    if high_prices.le(low_prices).any():
        fail("lookback_high_price must be greater than lookback_low_price")

    bucket_values = set(latest_detail["price_level_bucket"].astype(str))
    invalid_buckets = sorted(bucket_values - EXPECTED_BUCKETS)
    if invalid_buckets:
        fail(f"unexpected price_level_bucket values: {invalid_buckets}")
    scope_values = set(latest_summary["summary_scope"].astype(str))
    missing_scopes = sorted(EXPECTED_SCOPES - scope_values)
    if missing_scopes:
        fail(f"summary missing scopes: {missing_scopes}")

    all_row = latest_summary[
        latest_summary["summary_scope"].eq("all_w_bottom_candidates")
        & latest_summary["price_level_bucket"].eq("all")
    ]
    if len(all_row) != 1:
        fail("summary must contain exactly one all_w_bottom_candidates/all row")
    if int(all_row.iloc[0]["sample_size"]) != len(latest_detail):
        fail("all_w_bottom_candidates/all sample_size must match detail rows")

    expected_core = latest_detail[
        latest_detail["transition_status"].eq(OBSERVATION_TO_VOLUME)
        & ~latest_detail["slope_curvature_category"].eq(WV_CATEGORY)
        & latest_detail["effective_mainstream_label"].eq("core_mainstream")
    ]
    actual_core = latest_detail[bool_series(latest_detail["core_mainstream_exclude_wv_review_candidate"])]
    if len(expected_core) != len(actual_core):
        fail("core_mainstream_exclude_wv_review_candidate count mismatch")
    core_summary = latest_summary[
        latest_summary["summary_scope"].eq("core_mainstream_observation_volume_exclude_wv")
        & latest_summary["price_level_bucket"].eq("all")
    ]
    if len(core_summary) != 1:
        fail("summary must include core_mainstream_observation_volume_exclude_wv/all")
    if int(core_summary.iloc[0]["sample_size"]) != len(actual_core):
        fail("core-mainstream summary sample_size must match detail flag count")

    mature = latest_detail[bool_series(latest_detail["a_mature"])]
    returns = pd.to_numeric(mature["a_return_pct"], errors="coerce").dropna()
    print(
        "W-bottom price-level audit validation passed "
        f"detail_rows={len(latest_detail)} summary_rows={len(latest_summary)} "
        f"mature={len(returns)} buckets={sorted(bucket_values)}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
