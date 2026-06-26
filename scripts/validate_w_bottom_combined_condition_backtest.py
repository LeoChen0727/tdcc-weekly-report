from __future__ import annotations

from pathlib import Path

import pandas as pd


ROOT = Path(".")
RESEARCH_LATEST_DIR = ROOT / "output" / "latest" / "research_backtest"
RESEARCH_HISTORY_DIR = ROOT / "output" / "history" / "research"

LATEST_DETAIL_CSV = RESEARCH_LATEST_DIR / "w_bottom_combined_condition_backtest_detail_latest.csv"
LATEST_GRID_CSV = RESEARCH_LATEST_DIR / "w_bottom_combined_condition_backtest_latest.csv"
LATEST_MD = RESEARCH_LATEST_DIR / "w_bottom_combined_condition_backtest_latest.md"
HISTORY_DETAIL_CSV = RESEARCH_HISTORY_DIR / "w_bottom_combined_condition_backtest_detail.csv"
HISTORY_GRID_CSV = RESEARCH_HISTORY_DIR / "w_bottom_combined_condition_backtest.csv"

MODEL_ID = "w_bottom_right_side"
CONFIRMATION_MODEL_ID = "neckline_volume_breakout_confirmation"
OVERLAY_MODEL_ID = "tdcc_weekly_ranking_formula"
RESEARCH_ID = "w_bottom_combined_condition_backtest"
SOURCE_RESEARCH_ID = "w_bottom_nearest_micro_anchor_event_replay"
RESEARCH_VARIANT_ID = "warning_research_variant_only"
PRODUCTION_READINESS = "not_production_ready_research_only"
BASELINE_EVENT_SET_ID = "baseline_current_detector"
VARIANT_EVENT_SET_ID = "variant_nearest_micro_45d_event_replay"
REVENUE_CATALYST_STATUS = "pending_historical_feature_join_not_evaluated"

EXPECTED_CONDITION_COUNT = 23
EXPECTED_GRID_ROWS = EXPECTED_CONDITION_COUNT * 2 * 2

DETAIL_REQUIRED_COLUMNS = {
    "model_id",
    "confirmation_model_id",
    "overlay_model_id",
    "research_id",
    "source_research_id",
    "research_variant_id",
    "advisory_status",
    "event_set_id",
    "comparison_status",
    "stock_id",
    "signal_date",
    "has_neckline_breakout",
    "a_mature",
    "a_return_pct",
    "c_mature",
    "c_return_pct",
    "tdcc_any_age7",
    "tdcc_any_age14",
    "price_position_252_pct",
    "price_level_bucket",
    "slope_curvature_category",
    "effective_mainstream_label",
    "has_hot_theme",
    "revenue_catalyst_feature_status",
    "approved_for_daily",
    "production_readiness",
}

GRID_REQUIRED_COLUMNS = {
    "model_id",
    "confirmation_model_id",
    "overlay_model_id",
    "research_id",
    "source_research_id",
    "research_variant_id",
    "advisory_status",
    "event_set_id",
    "entry_timing_id",
    "condition_set_id",
    "condition_set_description",
    "sample_size",
    "mature_sample_size",
    "win_count",
    "win_rate_pct",
    "avg_return_pct",
    "median_return_pct",
    "baseline_sample_size",
    "baseline_mature_sample_size",
    "delta_win_rate_pct_vs_baseline",
    "delta_avg_return_pct_vs_baseline",
    "breakout_signal_count",
    "post_confirmation_count",
    "tdcc_any_age7_count",
    "sample_warning",
    "research_interpretation",
    "revenue_catalyst_feature_status",
    "approved_for_daily",
    "production_readiness",
}

EXPECTED_EVENT_SETS = {
    BASELINE_EVENT_SET_ID,
    VARIANT_EVENT_SET_ID,
}

EXPECTED_ENTRY_TIMINGS = {
    "a_next_open_after_neckline_breakout",
    "c_post_confirmation",
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


def validate_constants(df: pd.DataFrame) -> None:
    expected = {
        "model_id": MODEL_ID,
        "confirmation_model_id": CONFIRMATION_MODEL_ID,
        "overlay_model_id": OVERLAY_MODEL_ID,
        "research_id": RESEARCH_ID,
        "source_research_id": SOURCE_RESEARCH_ID,
        "research_variant_id": RESEARCH_VARIANT_ID,
        "advisory_status": RESEARCH_VARIANT_ID,
        "production_readiness": PRODUCTION_READINESS,
        "revenue_catalyst_feature_status": REVENUE_CATALYST_STATUS,
    }
    for column, value in expected.items():
        values = set(df[column].astype(str))
        if values != {value}:
            fail(f"{column} must be {value}; got {sorted(values)}")
    if not false_only(df["approved_for_daily"]):
        fail("approved_for_daily must remain false")


def validate_numeric(df: pd.DataFrame, columns: list[str]) -> None:
    for column in columns:
        values = pd.to_numeric(df[column], errors="coerce")
        if values.isna().any():
            fail(f"{column} must be numeric for every row")


def main() -> int:
    latest_detail = read_csv(LATEST_DETAIL_CSV)
    history_detail = read_csv(HISTORY_DETAIL_CSV)
    latest_grid = read_csv(LATEST_GRID_CSV)
    history_grid = read_csv(HISTORY_GRID_CSV)

    if not LATEST_MD.exists():
        fail(f"missing required file: {LATEST_MD}")
    md = LATEST_MD.read_text(encoding="utf-8", errors="replace")
    for text in [
        "production impact: `none`",
        REVENUE_CATALYST_STATUS,
        "A higher win rate is not enough for promotion",
        "Taxonomy is used as a read-only segment label",
    ]:
        if text not in md:
            fail(f"markdown missing required text: {text}")

    for df, required, name in [
        (latest_detail, DETAIL_REQUIRED_COLUMNS, "latest detail"),
        (history_detail, DETAIL_REQUIRED_COLUMNS, "history detail"),
        (latest_grid, GRID_REQUIRED_COLUMNS, "latest grid"),
        (history_grid, GRID_REQUIRED_COLUMNS, "history grid"),
    ]:
        missing = sorted(required - set(df.columns))
        if missing:
            fail(f"{name} missing columns: {missing}")
        forbidden = sorted(set(df.columns) & FORBIDDEN_PRODUCTION_FIELDS)
        if forbidden:
            fail(f"{name} must not emit production decision fields: {forbidden}")
        validate_constants(df)

    if latest_detail.empty:
        fail("detail rows must not be empty")
    if len(history_detail) != len(latest_detail):
        fail("history detail row count mismatch")
    if len(latest_grid) != EXPECTED_GRID_ROWS:
        fail(f"grid row count must be {EXPECTED_GRID_ROWS}; got {len(latest_grid)}")
    if len(history_grid) != EXPECTED_GRID_ROWS:
        fail("history grid row count mismatch")

    if set(latest_detail["event_set_id"].astype(str)) != EXPECTED_EVENT_SETS:
        fail("detail event_set_id values mismatch")
    if set(latest_grid["event_set_id"].astype(str)) != EXPECTED_EVENT_SETS:
        fail("grid event_set_id values mismatch")
    if set(latest_grid["entry_timing_id"].astype(str)) != EXPECTED_ENTRY_TIMINGS:
        fail("grid entry_timing_id values mismatch")

    comparison_counts = latest_detail.groupby(["event_set_id", "comparison_status"]).size().to_dict()
    required_comparisons = {
        (BASELINE_EVENT_SET_ID, "common"),
        (BASELINE_EVENT_SET_ID, "baseline_only"),
        (VARIANT_EVENT_SET_ID, "common"),
        (VARIANT_EVENT_SET_ID, "variant_only"),
    }
    missing_comparisons = sorted(required_comparisons - set(comparison_counts))
    if missing_comparisons:
        fail(f"missing comparison count keys: {missing_comparisons}")

    validate_numeric(
        latest_grid,
        [
            "sample_size",
            "mature_sample_size",
            "win_count",
            "baseline_sample_size",
            "baseline_mature_sample_size",
            "breakout_signal_count",
            "post_confirmation_count",
            "tdcc_any_age7_count",
        ],
    )

    if latest_grid["condition_set_id"].nunique() != EXPECTED_CONDITION_COUNT:
        fail("unexpected condition_set_id count")
    if latest_grid[
        latest_grid["condition_set_id"].eq("has_neckline_breakout_tdcc_any_age7")
        & latest_grid["event_set_id"].eq(VARIANT_EVENT_SET_ID)
        & latest_grid["entry_timing_id"].eq("a_next_open_after_neckline_breakout")
    ].empty:
        fail("missing variant TDCC age<=7 row")

    print(
        "W-bottom combined condition backtest validation passed "
        f"detail_rows={len(latest_detail)} grid_rows={len(latest_grid)}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
