from __future__ import annotations

from pathlib import Path
import sys

import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent))

from research_tdcc_dataset_consumer import load_research_tdcc_dataset_contract  # noqa: E402


ROOT = Path(".")
RESEARCH_LATEST_DIR = ROOT / "output" / "latest" / "research_backtest"
RESEARCH_HISTORY_DIR = ROOT / "output" / "history" / "research"

LATEST_SUMMARY_CSV = RESEARCH_LATEST_DIR / "w_bottom_tdcc_abc_backtest_latest.csv"
LATEST_SUMMARY_MD = RESEARCH_LATEST_DIR / "w_bottom_tdcc_abc_backtest_latest.md"
HISTORY_SUMMARY_CSV = RESEARCH_HISTORY_DIR / "w_bottom_tdcc_abc_backtest.csv"
HISTORY_EVENTS_CSV = RESEARCH_HISTORY_DIR / "w_bottom_tdcc_abc_events.csv"

REQUIRED_SUMMARY_COLUMNS = {
    "model_id",
    "confirmation_model_id",
    "overlay_model_id",
    "research_id",
    "research_variant_id",
    "parameter_set_id",
    "advisory_status",
    "sample_mode",
    "symmetry_ratio",
    "abc_stage",
    "tdcc_filter_id",
    "tdcc_age_days",
    "tdcc_rank_bucket",
    "sample_size",
    "mature_sample_size",
    "win_rate",
    "avg_return",
    "median_return",
    "confidence_status",
    "approved_for_daily",
    "risk_notes",
    "generated_at",
    "source_tdcc_dataset_id",
}

REQUIRED_EVENT_COLUMNS = {
    "model_id",
    "confirmation_model_id",
    "overlay_model_id",
    "research_id",
    "research_variant_id",
    "advisory_status",
    "sample_mode",
    "symmetry_ratio",
    "signal_date",
    "stock_id",
    "neckline_date",
    "right_low_date",
    "breakout_date",
    "late_breakout_not_w",
    "tdcc_match_detail_age7",
    "tdcc_match_detail_age14",
    "post_confirmation_trigger_id",
    "a_mature",
    "a_return_pct",
    "c_mature",
    "c_return_pct",
    "approved_for_daily",
    "generated_at",
    "source_tdcc_dataset_id",
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

EXPECTED_STAGES = {
    "A_w_neckline_breakout_next_open",
    "B_tdcc_filter_next_open",
    "C_tdcc_filter_post_confirmation_next_open",
}

EXPECTED_SAMPLE_MODES = {
    "raw_daily_signal",
    "dedup_approx_20_trading_days",
}


def fail(message: str) -> None:
    print(f"ERROR: {message}")
    raise SystemExit(1)


def check_file(path: Path) -> None:
    if not path.exists():
        fail(f"missing required file: {path}")
    if path.suffix.lower() == ".md":
        lines = path.read_text(encoding="utf-8", errors="replace").splitlines()
        if len(lines) < 20:
            fail(f"{path} is suspiciously short")


def read_csv(path: Path) -> pd.DataFrame:
    try:
        return pd.read_csv(path, dtype=str, keep_default_na=False)
    except Exception as exc:
        fail(f"{path} is not readable CSV: {exc}")


def false_only(series: pd.Series) -> bool:
    return set(series.astype(str).str.lower().unique()) <= {"false", "0", ""}


def validate_tdcc_details(events: pd.DataFrame, column: str, max_age: int) -> list[str]:
    errors: list[str] = []
    with_details = events[events[column].astype(str).str.strip().ne("")]
    for row_number, row in with_details.head(20000).iterrows():
        breakout_date = str(row.get("breakout_date", ""))
        if not breakout_date:
            errors.append(f"{column} has TDCC detail without breakout_date at row {row_number}")
            continue
        breakout_dt = pd.to_datetime(breakout_date, format="%Y%m%d", errors="coerce")
        if pd.isna(breakout_dt):
            errors.append(f"invalid breakout_date at row {row_number}: {breakout_date}")
            continue
        for detail in str(row.get(column, "")).split(";"):
            parts = detail.split(":")
            if len(parts) < 4:
                errors.append(f"malformed TDCC detail at row {row_number}: {detail}")
                continue
            age_part = next((part for part in parts if part.startswith("age")), "")
            date_part = next((part for part in parts if part.startswith("date")), "")
            if not age_part or not date_part:
                errors.append(f"TDCC detail missing age/date at row {row_number}: {detail}")
                continue
            try:
                age = int(age_part.replace("age", ""))
            except ValueError:
                errors.append(f"TDCC detail has non-numeric age at row {row_number}: {detail}")
                continue
            tdcc_date = date_part.replace("date", "")
            tdcc_dt = pd.to_datetime(tdcc_date, format="%Y%m%d", errors="coerce")
            if pd.isna(tdcc_dt):
                errors.append(f"TDCC detail has invalid date at row {row_number}: {detail}")
                continue
            if tdcc_dt > breakout_dt:
                errors.append(f"future TDCC leak at row {row_number}: {detail} > {breakout_date}")
            if age < 0 or age > max_age:
                errors.append(f"TDCC age outside max_age={max_age} at row {row_number}: {detail}")
    return errors


def main() -> int:
    for path in [LATEST_SUMMARY_CSV, LATEST_SUMMARY_MD, HISTORY_SUMMARY_CSV, HISTORY_EVENTS_CSV]:
        check_file(path)

    summary = read_csv(LATEST_SUMMARY_CSV)
    history_summary = read_csv(HISTORY_SUMMARY_CSV)
    events = read_csv(HISTORY_EVENTS_CSV)
    contract = load_research_tdcc_dataset_contract()
    if summary.empty:
        fail(f"{LATEST_SUMMARY_CSV} has no rows")
    if history_summary.empty:
        fail(f"{HISTORY_SUMMARY_CSV} has no rows")
    if events.empty:
        fail(f"{HISTORY_EVENTS_CSV} has no rows")

    for label, frame in [("summary", summary), ("history", history_summary), ("events", events)]:
        values = sorted({value for value in frame.get("source_tdcc_dataset_id", pd.Series(dtype=str)).astype(str) if value})
        if values != [contract.dataset_id]:
            fail(f"{label} source_tdcc_dataset_id mismatch: expected {contract.dataset_id}, got {values}")

    missing_summary = sorted(REQUIRED_SUMMARY_COLUMNS - set(summary.columns))
    if missing_summary:
        fail(f"{LATEST_SUMMARY_CSV} missing columns: {missing_summary}")
    missing_events = sorted(REQUIRED_EVENT_COLUMNS - set(events.columns))
    if missing_events:
        fail(f"{HISTORY_EVENTS_CSV} missing columns: {missing_events}")

    forbidden = sorted((set(summary.columns) | set(events.columns)) & FORBIDDEN_PRODUCTION_FIELDS)
    if forbidden:
        fail(f"W-bottom research output must not emit production decision fields: {forbidden}")

    if set(summary["model_id"].astype(str)) != {"w_bottom_right_side"}:
        fail("summary model_id must be w_bottom_right_side")
    if set(events["model_id"].astype(str)) != {"w_bottom_right_side"}:
        fail("events model_id must be w_bottom_right_side")
    if set(summary["research_variant_id"].astype(str)) != {"warning_research_variant_only"}:
        fail("summary must be marked warning_research_variant_only")
    if set(events["research_variant_id"].astype(str)) != {"warning_research_variant_only"}:
        fail("events must be marked warning_research_variant_only")
    if not false_only(summary["approved_for_daily"]):
        fail("summary approved_for_daily must remain false")
    if not false_only(events["approved_for_daily"]):
        fail("events approved_for_daily must remain false")

    missing_modes = sorted(EXPECTED_SAMPLE_MODES - set(summary["sample_mode"].astype(str)))
    if missing_modes:
        fail(f"summary missing sample modes: {missing_modes}")
    missing_stages = sorted(EXPECTED_STAGES - set(summary["abc_stage"].astype(str)))
    if missing_stages:
        fail(f"summary missing A/B/C stages: {missing_stages}")

    sample_size = pd.to_numeric(summary["sample_size"], errors="coerce")
    mature_size = pd.to_numeric(summary["mature_sample_size"], errors="coerce")
    if sample_size.isna().any() or (sample_size <= 0).any():
        fail("summary sample_size must be positive")
    if mature_size.isna().any() or (mature_size < 0).any():
        fail("summary mature_sample_size must be non-negative")

    symmetry = pd.to_numeric(events["symmetry_ratio"], errors="coerce")
    if symmetry.isna().any() or not set(symmetry.astype(float).unique()).issubset({1.5, 2.0}):
        fail("events symmetry_ratio must be 1.5 or 2.0")

    date_cols = ["signal_date", "neckline_date", "right_low_date"]
    for col in date_cols:
        parsed = pd.to_datetime(events[col], format="%Y%m%d", errors="coerce")
        if parsed.isna().any():
            fail(f"{col} must contain valid YYYYMMDD dates")

    tdcc_errors = validate_tdcc_details(events, "tdcc_match_detail_age7", 7)
    tdcc_errors += validate_tdcc_details(events, "tdcc_match_detail_age14", 14)
    if tdcc_errors:
        for error in tdcc_errors[:20]:
            print(f"ERROR: {error}")
        if len(tdcc_errors) > 20:
            print(f"ERROR: ... {len(tdcc_errors) - 20} additional TDCC validation errors")
        return 1

    print(
        "W-bottom TDCC A/B/C backtest validation passed "
        f"summary_rows={len(summary)} event_rows={len(events)}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
