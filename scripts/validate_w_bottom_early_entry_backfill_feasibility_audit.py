from __future__ import annotations

from pathlib import Path

import pandas as pd


ROOT = Path(".")
RESEARCH_LATEST_DIR = ROOT / "output" / "latest" / "research_backtest"
RESEARCH_HISTORY_DIR = ROOT / "output" / "history" / "research"

LATEST_CSV = RESEARCH_LATEST_DIR / "w_bottom_early_entry_backfill_feasibility_audit_latest.csv"
LATEST_MD = RESEARCH_LATEST_DIR / "w_bottom_early_entry_backfill_feasibility_audit_latest.md"
HISTORY_CSV = RESEARCH_HISTORY_DIR / "w_bottom_early_entry_backfill_feasibility_audit.csv"

RESEARCH_ID = "w_bottom_early_entry_backfill_feasibility_audit"
SOURCE_RESEARCH_ID = "w_bottom_early_entry_data_coverage_audit"
RESEARCH_VARIANT_ID = "warning_research_variant_only"
PRODUCTION_READINESS = "not_production_ready_research_only"
OWNER = "research_backtest_data_governance"

REQUIRED_COLUMNS = {
    "research_id",
    "source_research_id",
    "research_variant_id",
    "advisory_status",
    "surface_id",
    "audit_section",
    "audit_item_id",
    "source_artifact",
    "status",
    "finding",
    "daily_price_file_count",
    "daily_price_unique_dates",
    "daily_price_rows",
    "daily_price_min_date",
    "daily_price_max_date",
    "price_history_file_count",
    "price_history_rows",
    "price_history_min_date",
    "price_history_max_date",
    "price_history_files_ge_180",
    "earliest_180th_observed_date",
    "repo_existing_data_can_extend_to_earlier_2025",
    "max_signal_start_with_existing_data",
    "required_external_source",
    "required_action",
    "required_followup_owner",
    "forbidden_actions",
    "production_impact",
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
    raise SystemExit(f"ERROR: {message}")


def read_csv(path: Path) -> pd.DataFrame:
    if not path.exists():
        fail(f"missing required file: {path}")
    return pd.read_csv(path, dtype=str, keep_default_na=False)


def validate_frame(df: pd.DataFrame, name: str) -> None:
    missing = sorted(REQUIRED_COLUMNS - set(df.columns))
    if missing:
        fail(f"{name} missing columns: {missing}")
    forbidden = sorted(set(df.columns) & FORBIDDEN_PRODUCTION_FIELDS)
    if forbidden:
        fail(f"{name} must not emit production decision fields: {forbidden}")

    expected = {
        "research_id": RESEARCH_ID,
        "source_research_id": SOURCE_RESEARCH_ID,
        "research_variant_id": RESEARCH_VARIANT_ID,
        "advisory_status": RESEARCH_VARIANT_ID,
        "repo_existing_data_can_extend_to_earlier_2025": "true",
        "required_followup_owner": OWNER,
        "production_impact": "none",
        "approved_for_daily": "false",
        "production_readiness": PRODUCTION_READINESS,
    }
    for column, expected_value in expected.items():
        values = set(df[column].astype(str))
        if values != {expected_value}:
            fail(f"{name} unexpected {column}: {sorted(values)}")

    numeric_columns = [
        "daily_price_file_count",
        "daily_price_unique_dates",
        "daily_price_rows",
        "price_history_file_count",
        "price_history_rows",
        "price_history_files_ge_180",
    ]
    for column in numeric_columns:
        values = pd.to_numeric(df[column], errors="coerce")
        if values.isna().any():
            fail(f"{name} column must be numeric: {column}")


def validate_markdown() -> None:
    if not LATEST_MD.exists():
        fail(f"missing markdown: {LATEST_MD}")
    text = LATEST_MD.read_text(encoding="utf-8")
    required = [
        "production impact: `none`",
        "does not modify production conditions, scoring, ranking, PDFs, baselines, daily_full_pipeline, or GitHub Actions triggers",
        "can extend with repo-existing data: `true`",
        "completed_approved_official_price_backfill",
        "TWSE MI_INDEX",
        "TPEx",
        OWNER,
    ]
    for item in required:
        if item not in text:
            fail(f"markdown missing required text: {item}")


def main() -> int:
    latest = read_csv(LATEST_CSV)
    history = read_csv(HISTORY_CSV)
    validate_markdown()
    for df, name in [(latest, "latest"), (history, "history")]:
        validate_frame(df, name)
        if len(df) < 8:
            fail(f"{name} row count unexpectedly small: {len(df)}")
        required_sections = {
            "current_repo_data_window",
            "supporting_artifact_inventory",
            "backfill_feasibility_conclusion",
        }
        missing_sections = sorted(required_sections - set(df["audit_section"]))
        if missing_sections:
            fail(f"{name} missing sections: {missing_sections}")
        conclusion = df[df["audit_section"].eq("backfill_feasibility_conclusion")]
        if len(conclusion) != 1:
            fail(f"{name} expected exactly one conclusion row")
        row = conclusion.iloc[0]
        if row["status"] != "completed_approved_official_price_backfill":
            fail(f"{name} unexpected conclusion status: {row['status']}")
        if row["daily_price_min_date"] >= "20250407":
            fail(f"{name} expected daily price min date before 20250407, got {row['daily_price_min_date']}")
        if row["earliest_180th_observed_date"] >= "20260105":
            fail(
                f"{name} expected earliest 180th observed date before 20260105, "
                f"got {row['earliest_180th_observed_date']}"
            )
        source = row["required_external_source"]
        if "TWSE" not in source or "TPEx" not in source:
            fail(f"{name} missing required external price source names: {source}")

    if len(latest) != len(history):
        fail("latest/history row counts differ")
    print(f"W-bottom early-entry backfill feasibility audit validation passed rows={len(latest)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
