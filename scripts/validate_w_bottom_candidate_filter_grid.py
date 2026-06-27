from __future__ import annotations

from pathlib import Path

import pandas as pd


ROOT = Path(".")
RESEARCH_LATEST_DIR = ROOT / "output" / "latest" / "research_backtest"
RESEARCH_HISTORY_DIR = ROOT / "output" / "history" / "research"

SOURCE_AUDIT_CSV = RESEARCH_LATEST_DIR / "w_bottom_candidate_quality_audit_latest.csv"
LATEST_GRID_CSV = RESEARCH_LATEST_DIR / "w_bottom_candidate_filter_grid_latest.csv"
LATEST_GRID_MD = RESEARCH_LATEST_DIR / "w_bottom_candidate_filter_grid_latest.md"
HISTORY_GRID_CSV = RESEARCH_HISTORY_DIR / "w_bottom_candidate_filter_grid.csv"

REQUIRED_COLUMNS = {
    "model_id",
    "research_id",
    "source_research_id",
    "research_variant_id",
    "advisory_status",
    "candidate_set_id",
    "candidate_set_family",
    "neckline_gap_min_pct",
    "neckline_gap_max_pct",
    "right_rebound_min_pct",
    "right_rebound_max_pct",
    "second_arc_volume_ratio_min",
    "sample_size",
    "unique_stocks",
    "w_shape_completed_rate",
    "neckline_volume_breakout_rate",
    "right_low_failed_rate",
    "too_near_neckline_rate",
    "review_score",
    "sample_status",
    "interpretation",
    "approved_for_daily",
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

EXPECTED_FAMILIES = {
    "baseline",
    "single_gap_filter",
    "single_rebound_filter",
    "single_volume_filter",
    "combined_grid",
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


def numeric_between(df: pd.DataFrame, column: str, min_value: float, max_value: float) -> None:
    values = pd.to_numeric(df[column], errors="coerce")
    if values.isna().any():
        fail(f"{column} must be numeric")
    if ((values < min_value) | (values > max_value)).any():
        fail(f"{column} must be between {min_value} and {max_value}")


def main() -> int:
    latest = read_csv(LATEST_GRID_CSV)
    history = read_csv(HISTORY_GRID_CSV)
    source = read_csv(SOURCE_AUDIT_CSV)
    if not LATEST_GRID_MD.exists():
        fail(f"missing required file: {LATEST_GRID_MD}")
    md_lines = LATEST_GRID_MD.read_text(encoding="utf-8", errors="replace").splitlines()
    if len(md_lines) < 30:
        fail(f"{LATEST_GRID_MD} is suspiciously short")
    if latest.empty:
        fail(f"{LATEST_GRID_CSV} has no rows")
    if history.empty:
        fail(f"{HISTORY_GRID_CSV} has no rows")
    if len(latest) != len(history):
        fail("latest and history grid row counts differ")

    missing = sorted(REQUIRED_COLUMNS - set(latest.columns))
    if missing:
        fail(f"{LATEST_GRID_CSV} missing columns: {missing}")
    missing_history = sorted(REQUIRED_COLUMNS - set(history.columns))
    if missing_history:
        fail(f"{HISTORY_GRID_CSV} missing columns: {missing_history}")

    forbidden = sorted((set(latest.columns) | set(history.columns)) & FORBIDDEN_PRODUCTION_FIELDS)
    if forbidden:
        fail(f"W-bottom filter grid must not emit production decision fields: {forbidden}")

    if set(latest["model_id"].astype(str)) != {"w_bottom_right_side"}:
        fail("grid model_id must be w_bottom_right_side")
    if set(latest["research_id"].astype(str)) != {"w_bottom_candidate_filter_grid"}:
        fail("grid research_id must be w_bottom_candidate_filter_grid")
    if set(latest["source_research_id"].astype(str)) != {"w_bottom_candidate_quality_audit"}:
        fail("grid source_research_id must be w_bottom_candidate_quality_audit")
    if set(latest["research_variant_id"].astype(str)) != {"warning_research_variant_only"}:
        fail("grid must be marked warning_research_variant_only")
    if set(latest["advisory_status"].astype(str)) != {"warning_research_variant_only"}:
        fail("grid advisory_status must be warning_research_variant_only")
    if not false_only(latest["approved_for_daily"]):
        fail("grid approved_for_daily must remain false")

    if latest["candidate_set_id"].duplicated().any():
        fail("candidate_set_id values must be unique")
    missing_family = sorted(EXPECTED_FAMILIES - set(latest["candidate_set_family"].astype(str)))
    if missing_family:
        fail(f"grid missing candidate_set_family values: {missing_family}")
    if "baseline_current_audit_all" not in set(latest["candidate_set_id"].astype(str)):
        fail("grid must include baseline_current_audit_all")

    sample_size = pd.to_numeric(latest["sample_size"], errors="coerce")
    if sample_size.isna().any() or (sample_size < 0).any():
        fail("sample_size must be non-negative numeric")
    baseline = latest[latest["candidate_set_id"].eq("baseline_current_audit_all")]
    if len(baseline) != 1:
        fail("grid must contain exactly one baseline row")
    if int(float(baseline.iloc[0]["sample_size"])) != len(source):
        fail("baseline sample_size must equal source audit row count")

    for column in [
        "w_shape_completed_rate",
        "neckline_volume_breakout_rate",
        "right_low_failed_rate",
        "too_near_neckline_rate",
    ]:
        numeric_between(latest, column, 0.0, 100.0)

    print(
        "W-bottom candidate filter grid validation passed "
        f"rows={len(latest)} baseline_sample_size={int(float(baseline.iloc[0]['sample_size']))}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
