from __future__ import annotations

from pathlib import Path

import pandas as pd


ROOT = Path(".")
RESEARCH_LATEST_DIR = ROOT / "output" / "latest" / "research_backtest"
RESEARCH_HISTORY_DIR = ROOT / "output" / "history" / "research"

LATEST_DETAIL_CSV = RESEARCH_LATEST_DIR / "w_bottom_split_entry_outcome_backtest_detail_latest.csv"
LATEST_SUMMARY_CSV = RESEARCH_LATEST_DIR / "w_bottom_split_entry_outcome_backtest_latest.csv"
LATEST_MD = RESEARCH_LATEST_DIR / "w_bottom_split_entry_outcome_backtest_latest.md"
HISTORY_DETAIL_CSV = RESEARCH_HISTORY_DIR / "w_bottom_split_entry_outcome_backtest_detail.csv"
HISTORY_SUMMARY_CSV = RESEARCH_HISTORY_DIR / "w_bottom_split_entry_outcome_backtest.csv"

MODEL_ID = "w_bottom_right_side"
CONFIRMATION_MODEL_ID = "neckline_volume_breakout_confirmation"
OVERLAY_MODEL_ID = "tdcc_weekly_ranking_formula"
RESEARCH_ID = "w_bottom_split_entry_outcome_backtest"
SOURCE_RESEARCH_ID = "w_bottom_combined_condition_backtest"
RESEARCH_VARIANT_ID = "warning_research_variant_only"
PRODUCTION_READINESS = "not_production_ready_research_only"

EXPECTED_SURFACES = {
    "w_bottom_neckline_volume_breakout_confirmation",
    "w_bottom_right_low_early_entry",
}

EXPECTED_EVENT_SETS = {
    "baseline_current_detector",
    "variant_nearest_micro_45d_event_replay",
}

REQUIRED_DETAIL_COLUMNS = {
    "model_id",
    "confirmation_model_id",
    "overlay_model_id",
    "research_id",
    "source_research_id",
    "research_variant_id",
    "advisory_status",
    "surface_id",
    "event_set_id",
    "entry_rule_id",
    "outcome_rule_id",
    "stock_id",
    "source_signal_date",
    "entry_signal_date",
    "entry_date",
    "entry_open_price",
    "exit_date",
    "exit_close_price",
    "exit_reason",
    "return_pct",
    "mature",
    "success",
    "positive_return",
    "approved_for_daily",
    "production_readiness",
}

REQUIRED_SUMMARY_COLUMNS = {
    "model_id",
    "confirmation_model_id",
    "overlay_model_id",
    "research_id",
    "source_research_id",
    "research_variant_id",
    "advisory_status",
    "surface_id",
    "event_set_id",
    "entry_rule_id",
    "outcome_rule_id",
    "condition_set_id",
    "sample_size",
    "mature_sample_size",
    "success_count",
    "success_rate_pct",
    "positive_return_count",
    "positive_return_rate_pct",
    "avg_return_pct",
    "median_return_pct",
    "approved_for_daily",
    "production_readiness",
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
    }
    for column, value in expected.items():
        values = set(df[column].astype(str))
        if values != {value}:
            fail(f"{column} must be {value}; got {sorted(values)}")
    if not false_only(df["approved_for_daily"]):
        fail("approved_for_daily must remain false")


def validate_schema(df: pd.DataFrame, required: set[str], name: str) -> None:
    missing = sorted(required - set(df.columns))
    if missing:
        fail(f"{name} missing columns: {missing}")
    forbidden = sorted(set(df.columns) & FORBIDDEN_PRODUCTION_FIELDS)
    if forbidden:
        fail(f"{name} must not emit production decision fields: {forbidden}")


def validate_numeric(df: pd.DataFrame, columns: list[str], name: str) -> None:
    for column in columns:
        values = pd.to_numeric(df[column], errors="coerce")
        if values.isna().any():
            fail(f"{name}.{column} must be numeric for every row")


def main() -> int:
    latest_detail = read_csv(LATEST_DETAIL_CSV)
    history_detail = read_csv(HISTORY_DETAIL_CSV)
    latest_summary = read_csv(LATEST_SUMMARY_CSV)
    history_summary = read_csv(HISTORY_SUMMARY_CSV)

    if not LATEST_MD.exists():
        fail(f"missing required file: {LATEST_MD}")
    md = LATEST_MD.read_text(encoding="utf-8", errors="replace")
    for text in [
        "production impact: `none`",
        "entry uses next trading day's open; exit uses exit day's close",
        "Early-entry success is separated from breakout-confirmation success",
    ]:
        if text not in md:
            fail(f"markdown missing required text: {text}")

    validate_schema(latest_detail, REQUIRED_DETAIL_COLUMNS, "latest detail")
    validate_schema(history_detail, REQUIRED_DETAIL_COLUMNS, "history detail")
    validate_schema(latest_summary, REQUIRED_SUMMARY_COLUMNS, "latest summary")
    validate_schema(history_summary, REQUIRED_SUMMARY_COLUMNS, "history summary")
    validate_constants(latest_detail)
    validate_constants(history_detail)
    validate_constants(latest_summary)
    validate_constants(history_summary)

    if len(latest_detail) != len(history_detail):
        fail("latest/history detail row counts differ")
    if len(latest_summary) != len(history_summary):
        fail("latest/history summary row counts differ")
    if len(latest_detail) < 5000:
        fail(f"detail row count unexpectedly small: {len(latest_detail)}")
    if len(latest_summary) < 200:
        fail(f"summary row count unexpectedly small: {len(latest_summary)}")

    if set(latest_detail["surface_id"].astype(str)) != EXPECTED_SURFACES:
        fail("detail surface_id values mismatch")
    if set(latest_summary["surface_id"].astype(str)) != EXPECTED_SURFACES:
        fail("summary surface_id values mismatch")
    if set(latest_detail["event_set_id"].astype(str)) != EXPECTED_EVENT_SETS:
        fail("detail event_set_id values mismatch")
    if set(latest_summary["event_set_id"].astype(str)) != EXPECTED_EVENT_SETS:
        fail("summary event_set_id values mismatch")

    bool_columns = ["mature", "success", "positive_return"]
    for column in bool_columns:
        values = set(latest_detail[column].astype(str).str.lower())
        if not values.issubset({"true", "false"}):
            fail(f"{column} must be true/false")

    mature = latest_detail[latest_detail["mature"].astype(str).str.lower().eq("true")].copy()
    if mature.empty:
        fail("no mature rows")
    numeric_mature = pd.to_numeric(mature["return_pct"], errors="coerce")
    if numeric_mature.isna().any():
        fail("mature return_pct must be numeric")

    validate_numeric(
        latest_summary,
        [
            "sample_size",
            "mature_sample_size",
            "success_count",
            "positive_return_count",
            "baseline_sample_size",
            "baseline_mature_sample_size",
            "tdcc_any_age7_count",
        ],
        "latest summary",
    )

    target_rules = latest_detail[latest_detail["outcome_rule_id"].str.contains("before_right_low_stop", regex=False)]
    if target_rules.empty:
        fail("missing early-entry target/stop outcome rows")
    fixed_rules = latest_detail[latest_detail["outcome_rule_id"].str.contains("fixed_", regex=False)]
    if fixed_rules.empty:
        fail("missing fixed-horizon outcome rows")
    fixed_mature = fixed_rules[fixed_rules["mature"].astype(str).str.lower().eq("true")]
    mismatch = fixed_mature[
        fixed_mature["success"].astype(str).str.lower().ne(
            fixed_mature["positive_return"].astype(str).str.lower()
        )
    ]
    if not mismatch.empty:
        fail("fixed-horizon success must equal positive_return")

    print(
        "W-bottom split entry outcome backtest validation passed "
        f"detail_rows={len(latest_detail)} summary_rows={len(latest_summary)}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
