from __future__ import annotations

from pathlib import Path

import pandas as pd


ROOT = Path(".")
RESEARCH_LATEST_DIR = ROOT / "output" / "latest" / "research_backtest"
RESEARCH_HISTORY_DIR = ROOT / "output" / "history" / "research"

LATEST_CSV = RESEARCH_LATEST_DIR / "w_bottom_early_entry_data_coverage_audit_latest.csv"
LATEST_MD = RESEARCH_LATEST_DIR / "w_bottom_early_entry_data_coverage_audit_latest.md"
HISTORY_CSV = RESEARCH_HISTORY_DIR / "w_bottom_early_entry_data_coverage_audit.csv"

RESEARCH_ID = "w_bottom_early_entry_data_coverage_audit"
SOURCE_RESEARCH_ID = "w_bottom_early_entry_parameter_grid"
RESEARCH_VARIANT_ID = "warning_research_variant_only"
PRODUCTION_READINESS = "not_production_ready_research_only"
SURFACE_ID = "w_bottom_right_low_early_entry"
STRICT_SEGMENT_ID = "smooth_right_rebound_5_20"

REQUIRED_COLUMNS = {
    "model_id",
    "confirmation_model_id",
    "overlay_model_id",
    "research_id",
    "source_research_id",
    "research_variant_id",
    "advisory_status",
    "surface_id",
    "audit_section",
    "audit_item_id",
    "source_artifact",
    "event_set_id",
    "outcome_rule_id",
    "segment_id",
    "period_id",
    "row_count",
    "stock_count",
    "unique_signal_count",
    "min_date",
    "max_date",
    "month_count",
    "sample_size",
    "evaluated_sample_size",
    "mature_sample_size",
    "win_count",
    "neutral_count",
    "loss_count",
    "incomplete_count",
    "mature_signal_month_count",
    "months_with_mature_ge5",
    "months_with_mature_ge10",
    "price_files_with_dates",
    "price_rows",
    "price_global_min_date",
    "price_global_max_date",
    "files_with_180_days",
    "earliest_180th_observed_date",
    "signal_window_status",
    "maturity_status",
    "promotion_readiness",
    "blocker_reason",
    "required_followup_owner",
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
    raise SystemExit(f"ERROR: {message}")


def read_csv(path: Path) -> pd.DataFrame:
    if not path.exists():
        fail(f"missing required file: {path}")
    return pd.read_csv(path, dtype=str, keep_default_na=False)


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
        values = set(df[column].astype(str))
        if values != {expected_value}:
            fail(f"{name} unexpected {column}: {sorted(values)}")


def validate_numeric(df: pd.DataFrame, columns: list[str], name: str) -> None:
    for column in columns:
        populated = df[column].astype(str).ne("")
        values = pd.to_numeric(df[column], errors="coerce")
        if values[populated].isna().any():
            fail(f"{name} column must be numeric when populated: {column}")


def validate_markdown() -> None:
    if not LATEST_MD.exists():
        fail(f"missing markdown: {LATEST_MD}")
    text = LATEST_MD.read_text(encoding="utf-8")
    required = [
        "production impact: `none`",
        "does not modify production conditions, scoring, ranking, PDFs, baselines, or daily_full_pipeline",
        "approved_for_daily=false",
        "blocked_data_window_too_short",
        "research_backtest_data_governance",
    ]
    for item in required:
        if item not in text:
            fail(f"markdown missing required text: {item}")


def main() -> int:
    latest = read_csv(LATEST_CSV)
    history = read_csv(HISTORY_CSV)
    validate_markdown()

    for df, name in [(latest, "latest"), (history, "history")]:
        missing = sorted(REQUIRED_COLUMNS - set(df.columns))
        if missing:
            fail(f"{name} missing columns: {missing}")
        forbidden = sorted(set(df.columns) & FORBIDDEN_PRODUCTION_FIELDS)
        if forbidden:
            fail(f"{name} must not emit production decision fields: {forbidden}")
        validate_constants(df, name)
        validate_numeric(
            df,
            [
                "row_count",
                "stock_count",
                "unique_signal_count",
                "month_count",
                "sample_size",
                "evaluated_sample_size",
                "mature_sample_size",
                "win_count",
                "neutral_count",
                "loss_count",
                "incomplete_count",
                "mature_signal_month_count",
                "months_with_mature_ge5",
                "months_with_mature_ge10",
                "price_files_with_dates",
                "price_rows",
                "files_with_180_days",
            ],
            name,
        )

    if len(latest) != len(history):
        fail("latest/history row counts differ")
    if len(latest) < 15:
        fail(f"row count unexpectedly small: {len(latest)}")

    required_sections = {
        "price_history_coverage",
        "w_bottom_signal_source_window",
        "outcome_month_maturity",
        "outcome_maturity_summary",
        "promotion_readiness_conclusion",
    }
    missing_sections = sorted(required_sections - set(latest["audit_section"]))
    if missing_sections:
        fail(f"missing audit sections: {missing_sections}")

    conclusion = latest[latest["audit_section"].eq("promotion_readiness_conclusion")]
    if len(conclusion) != 1:
        fail("expected exactly one promotion readiness conclusion row")
    conclusion_row = conclusion.iloc[0]
    if conclusion_row["promotion_readiness"] != "blocked_data_window_too_short":
        fail(f"unexpected promotion readiness: {conclusion_row['promotion_readiness']}")
    if conclusion_row["required_followup_owner"] != "research_backtest_data_governance":
        fail(f"unexpected follow-up owner: {conclusion_row['required_followup_owner']}")
    if int(conclusion_row["mature_signal_month_count"]) >= 6:
        fail("current audit expected fewer than six mature signal months; review promotion gate before passing")

    source_windows = latest[latest["audit_section"].eq("w_bottom_signal_source_window")]
    if source_windows["min_date"].min() < "20260101":
        fail("this audit currently documents the short 2026-only W signal window; rerun and update conclusions after backfill")
    if source_windows["month_count"].astype(int).max() < 6:
        fail("expected current source windows to cover at least six signal months")

    strict_months = latest[
        latest["audit_section"].eq("outcome_month_maturity")
        & latest["segment_id"].eq(STRICT_SEGMENT_ID)
    ]
    if strict_months["period_id"].nunique() < 6:
        fail("strict segment monthly maturity should cover the current six signal months")
    if not strict_months["maturity_status"].isin(["partially_mature", "future_window_incomplete"]).all():
        fail("unexpected strict monthly maturity status")

    print(f"W-bottom early-entry data coverage audit validation passed rows={len(latest)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
