from __future__ import annotations

from pathlib import Path
from typing import Any

import pandas as pd


ROOT = Path(".")
RESEARCH_LATEST_DIR = ROOT / "output" / "latest" / "research_backtest"
RESEARCH_HISTORY_DIR = ROOT / "output" / "history" / "research"

LATEST_DETAIL_CSV = RESEARCH_LATEST_DIR / "w_bottom_early_entry_parameter_grid_detail_latest.csv"
LATEST_GRID_CSV = RESEARCH_LATEST_DIR / "w_bottom_early_entry_parameter_grid_latest.csv"
LATEST_MD = RESEARCH_LATEST_DIR / "w_bottom_early_entry_parameter_grid_latest.md"
HISTORY_DETAIL_CSV = RESEARCH_HISTORY_DIR / "w_bottom_early_entry_parameter_grid_detail.csv"
HISTORY_GRID_CSV = RESEARCH_HISTORY_DIR / "w_bottom_early_entry_parameter_grid.csv"

RESEARCH_ID = "w_bottom_early_entry_parameter_grid"
SOURCE_RESEARCH_ID = "w_bottom_split_entry_outcome_backtest"
RESEARCH_VARIANT_ID = "warning_research_variant_only"
PRODUCTION_READINESS = "not_production_ready_research_only"
SURFACE_ID = "w_bottom_right_low_early_entry"
BASELINE_CONDITION_ID = "all_early_entry_rows"

EXPECTED_EVENT_SETS = {"baseline_current_detector", "variant_nearest_micro_45d_event_replay"}
EXPECTED_OUTCOME_RULES = {
    "fixed_10d_close_positive_return",
    "fixed_20d_close_positive_return",
    "fixed_30d_close_positive_return",
    "fixed_40d_close_positive_return",
    "reach_neckline_close_before_right_low_stop_40d",
    "volume_breakout_close_before_right_low_stop_40d",
}
EXPECTED_CONDITION_IDS = {
    BASELINE_CONDITION_ID,
    "price_position_le_40",
    "price_position_le_30",
    "price_position_le_25",
    "core_mainstream_price_le40",
    "second_arc_volume_gte1_2",
    "second_red_ratio_gt_first",
    "core_mainstream_price_le40_volume_red",
    "core_mainstream_price_le40_gap_m5_p8_rebound_3_20",
    "core_mainstream_price_le40_below_neckline5",
}

REQUIRED_DETAIL_COLUMNS = [
    "model_id",
    "confirmation_model_id",
    "overlay_model_id",
    "research_id",
    "source_research_id",
    "research_variant_id",
    "parameter_set_id",
    "advisory_status",
    "surface_id",
    "event_set_id",
    "entry_rule_id",
    "outcome_rule_id",
    "stock_id",
    "source_signal_date",
    "left_peak_date",
    "left_low_date",
    "neckline_date",
    "right_low_date",
    "signal_close",
    "left_low_price",
    "right_low_price",
    "second_low_gap_pct",
    "signal_rebound_from_right_low_pct",
    "neckline_distance_pct",
    "second_arc_volume_ratio",
    "first_arc_red_ratio_pct",
    "second_arc_red_ratio_pct",
    "red_ratio_delta_pct",
    "entry_open_price",
    "exit_close_price",
    "return_pct",
    "mature",
    "success",
    "positive_return",
    "approved_for_daily",
    "production_readiness",
]

REQUIRED_GRID_COLUMNS = [
    "model_id",
    "confirmation_model_id",
    "overlay_model_id",
    "research_id",
    "source_research_id",
    "research_variant_id",
    "parameter_set_id",
    "advisory_status",
    "surface_id",
    "event_set_id",
    "entry_rule_id",
    "outcome_rule_id",
    "condition_set_id",
    "condition_set_description",
    "sample_size",
    "mature_sample_size",
    "success_count",
    "success_rate_pct",
    "positive_return_count",
    "positive_return_rate_pct",
    "avg_return_pct",
    "median_return_pct",
    "baseline_condition_set_id",
    "baseline_sample_size",
    "baseline_mature_sample_size",
    "delta_success_rate_pct_vs_all",
    "delta_avg_return_pct_vs_all",
    "sample_retention_rate_pct",
    "sample_warning",
    "research_interpretation",
    "approved_for_daily",
    "production_readiness",
]

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


def validate_schema(df: pd.DataFrame, required: list[str], name: str) -> None:
    missing = [column for column in required if column not in df.columns]
    if missing:
        fail(f"{name} missing columns: {missing}")


def false_only(series: pd.Series) -> bool:
    return set(series.astype(str).str.lower()).issubset({"false"})


def validate_constants(df: pd.DataFrame, name: str) -> None:
    expected = {
        "research_id": RESEARCH_ID,
        "source_research_id": SOURCE_RESEARCH_ID,
        "research_variant_id": RESEARCH_VARIANT_ID,
        "advisory_status": RESEARCH_VARIANT_ID,
        "surface_id": SURFACE_ID,
        "approved_for_daily": "false",
        "production_readiness": PRODUCTION_READINESS,
    }
    for column, expected_value in expected.items():
        if column not in df.columns:
            fail(f"{name} missing constant column: {column}")
        values = set(df[column].astype(str))
        if values != {expected_value}:
            fail(f"{name} unexpected values for {column}: {sorted(values)}")
    forbidden = sorted(set(df.columns) & FORBIDDEN_PRODUCTION_FIELDS)
    if forbidden:
        fail(f"{name} must not emit production decision fields: {forbidden}")
    if not false_only(df["approved_for_daily"]):
        fail(f"{name} approved_for_daily must remain false")


def validate_numeric(df: pd.DataFrame, columns: list[str], name: str) -> None:
    for column in columns:
        values = pd.to_numeric(df[column], errors="coerce")
        populated = df[column].astype(str).ne("")
        if values[populated].isna().any():
            fail(f"{name} column must be numeric when populated: {column}")


def validate_markdown(path: Path) -> None:
    if not path.exists():
        fail(f"missing markdown: {path}")
    text = path.read_text(encoding="utf-8")
    required = [
        "production impact: `none`",
        "entry uses next trading day's open; exit uses exit day's close",
        "surface: `w_bottom_right_low_early_entry` only",
        "approved_for_daily=false",
        "Strong-looking rows are promotion-review candidates only",
    ]
    for item in required:
        if item not in text:
            fail(f"markdown missing required text: {item}")


def main() -> int:
    latest_detail = read_csv(LATEST_DETAIL_CSV)
    history_detail = read_csv(HISTORY_DETAIL_CSV)
    latest_grid = read_csv(LATEST_GRID_CSV)
    history_grid = read_csv(HISTORY_GRID_CSV)
    validate_markdown(LATEST_MD)

    validate_schema(latest_detail, REQUIRED_DETAIL_COLUMNS, "latest detail")
    validate_schema(history_detail, REQUIRED_DETAIL_COLUMNS, "history detail")
    validate_schema(latest_grid, REQUIRED_GRID_COLUMNS, "latest grid")
    validate_schema(history_grid, REQUIRED_GRID_COLUMNS, "history grid")
    validate_constants(latest_detail, "latest detail")
    validate_constants(history_detail, "history detail")
    validate_constants(latest_grid, "latest grid")
    validate_constants(history_grid, "history grid")

    if len(latest_detail) != len(history_detail):
        fail("latest/history detail row counts differ")
    if len(latest_grid) != len(history_grid):
        fail("latest/history grid row counts differ")
    if len(latest_detail) < 5000:
        fail(f"detail row count unexpectedly small: {len(latest_detail)}")
    if len(latest_grid) < 300:
        fail(f"grid row count unexpectedly small: {len(latest_grid)}")

    if set(latest_detail["event_set_id"].astype(str)) != EXPECTED_EVENT_SETS:
        fail("detail event_set_id values mismatch")
    if set(latest_grid["event_set_id"].astype(str)) != EXPECTED_EVENT_SETS:
        fail("grid event_set_id values mismatch")
    if set(latest_detail["outcome_rule_id"].astype(str)) != EXPECTED_OUTCOME_RULES:
        fail("detail outcome_rule_id values mismatch")
    if set(latest_grid["outcome_rule_id"].astype(str)) != EXPECTED_OUTCOME_RULES:
        fail("grid outcome_rule_id values mismatch")
    condition_ids = set(latest_grid["condition_set_id"].astype(str))
    missing_conditions = sorted(EXPECTED_CONDITION_IDS - condition_ids)
    if missing_conditions:
        fail(f"grid missing expected condition ids: {missing_conditions}")

    for column in ["mature", "success", "positive_return"]:
        values = set(latest_detail[column].astype(str).str.lower())
        if not values.issubset({"true", "false"}):
            fail(f"detail {column} must be true/false")

    mature = latest_detail[latest_detail["mature"].astype(str).str.lower().eq("true")].copy()
    if mature.empty:
        fail("no mature detail rows")
    validate_numeric(
        mature,
        [
            "entry_open_price",
            "exit_close_price",
            "return_pct",
            "signal_close",
            "right_low_price",
            "second_low_gap_pct",
            "signal_rebound_from_right_low_pct",
            "neckline_distance_pct",
            "second_arc_volume_ratio",
            "red_ratio_delta_pct",
        ],
        "mature detail",
    )
    validate_numeric(
        latest_grid,
        [
            "sample_size",
            "mature_sample_size",
            "success_count",
            "positive_return_count",
            "baseline_sample_size",
            "baseline_mature_sample_size",
        ],
        "latest grid",
    )

    fixed = latest_detail[latest_detail["outcome_rule_id"].str.startswith("fixed_")]
    fixed_mature = fixed[fixed["mature"].astype(str).str.lower().eq("true")]
    mismatch = fixed_mature[
        fixed_mature["success"].astype(str).str.lower().ne(
            fixed_mature["positive_return"].astype(str).str.lower()
        )
    ]
    if not mismatch.empty:
        fail("fixed-horizon success must equal positive_return")

    print(
        "W-bottom early-entry parameter grid validation passed "
        f"detail_rows={len(latest_detail)} grid_rows={len(latest_grid)}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
