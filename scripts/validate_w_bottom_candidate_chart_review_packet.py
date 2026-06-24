from __future__ import annotations

from pathlib import Path

import pandas as pd


ROOT = Path(".")
RESEARCH_LATEST_DIR = ROOT / "output" / "latest" / "research_backtest"
RESEARCH_HISTORY_DIR = ROOT / "output" / "history" / "research"

SOURCE_AUDIT_CSV = RESEARCH_LATEST_DIR / "w_bottom_candidate_quality_audit_latest.csv"
CHART_ROOT = RESEARCH_LATEST_DIR / "w_bottom_candidate_chart_review"
LATEST_INDEX_CSV = RESEARCH_LATEST_DIR / "w_bottom_candidate_chart_review_latest.csv"
LATEST_INDEX_MD = RESEARCH_LATEST_DIR / "w_bottom_candidate_chart_review_latest.md"
HISTORY_INDEX_CSV = RESEARCH_HISTORY_DIR / "w_bottom_candidate_chart_review.csv"

SOURCE_CANDIDATE_SET_ID = "grid_gap_2_20_rebound_7_12_vol_1_2"

NECKLINE_GAP_MIN_PCT = 2.0
NECKLINE_GAP_MAX_PCT = 20.0
RIGHT_REBOUND_MIN_PCT = 7.0
RIGHT_REBOUND_MAX_PCT = 12.0
SECOND_ARC_VOLUME_RATIO_MIN = 1.2

REQUIRED_COLUMNS = {
    "model_id",
    "research_id",
    "source_research_id",
    "source_candidate_set_id",
    "research_variant_id",
    "advisory_status",
    "stock_id",
    "signal_date",
    "category_id",
    "category_folder",
    "chart_path",
    "chart_path_absolute",
    "left_peak_date",
    "left_low_date",
    "neckline_date",
    "right_low_date",
    "signal_distance_to_neckline_pct",
    "signal_rebound_from_right_low_pct",
    "second_arc_volume_ratio",
    "sym1_5_quality_bucket",
    "primary_review_flag",
    "manual_review_status",
    "approved_for_daily",
    "generated_at",
}

CATEGORY_FOLDERS = {
    "passed_volume_breakout_confirmation": "01_passed_volume_breakout_confirmation",
    "shape_completed_but_volume_missing": "02_shape_completed_but_volume_missing",
    "candidate_selected_too_near_neckline": "03_candidate_selected_too_near_neckline",
    "right_low_failed": "04_right_low_failed",
    "completion_too_late_for_w": "05_completion_too_late_for_w",
    "did_not_complete_w": "06_did_not_complete_w",
    "other": "99_other",
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


def expected_candidate_count(source: pd.DataFrame) -> int:
    distance = pd.to_numeric(source["signal_distance_to_neckline_pct"], errors="coerce")
    rebound = pd.to_numeric(source["signal_rebound_from_right_low_pct"], errors="coerce")
    volume_ratio = pd.to_numeric(source["second_arc_volume_ratio"], errors="coerce")
    mask = (
        distance.le(-NECKLINE_GAP_MIN_PCT)
        & distance.ge(-NECKLINE_GAP_MAX_PCT)
        & rebound.ge(RIGHT_REBOUND_MIN_PCT)
        & rebound.le(RIGHT_REBOUND_MAX_PCT)
        & volume_ratio.ge(SECOND_ARC_VOLUME_RATIO_MIN)
    )
    return int(mask.sum())


def main() -> int:
    source = read_csv(SOURCE_AUDIT_CSV)
    latest = read_csv(LATEST_INDEX_CSV)
    history = read_csv(HISTORY_INDEX_CSV)
    if not LATEST_INDEX_MD.exists():
        fail(f"missing required file: {LATEST_INDEX_MD}")
    if not CHART_ROOT.exists():
        fail(f"missing chart root: {CHART_ROOT}")
    md_lines = LATEST_INDEX_MD.read_text(encoding="utf-8", errors="replace").splitlines()
    if len(md_lines) < 30:
        fail(f"{LATEST_INDEX_MD} is suspiciously short")
    if latest.empty:
        fail(f"{LATEST_INDEX_CSV} has no rows")
    if len(latest) != len(history):
        fail("latest and history chart review index row counts differ")

    missing = sorted(REQUIRED_COLUMNS - set(latest.columns))
    if missing:
        fail(f"{LATEST_INDEX_CSV} missing columns: {missing}")
    missing_history = sorted(REQUIRED_COLUMNS - set(history.columns))
    if missing_history:
        fail(f"{HISTORY_INDEX_CSV} missing columns: {missing_history}")

    forbidden = sorted((set(latest.columns) | set(history.columns)) & FORBIDDEN_PRODUCTION_FIELDS)
    if forbidden:
        fail(f"W-bottom chart review packet must not emit production decision fields: {forbidden}")

    expected_count = expected_candidate_count(source)
    if len(latest) != expected_count:
        fail(f"chart index rows must match selected filter count: index={len(latest)} expected={expected_count}")
    if set(latest["model_id"].astype(str)) != {"w_bottom_right_side"}:
        fail("chart review model_id must be w_bottom_right_side")
    if set(latest["research_id"].astype(str)) != {"w_bottom_candidate_chart_review"}:
        fail("chart review research_id must be w_bottom_candidate_chart_review")
    if set(latest["source_research_id"].astype(str)) != {"w_bottom_candidate_quality_audit"}:
        fail("chart review source_research_id must be w_bottom_candidate_quality_audit")
    if set(latest["source_candidate_set_id"].astype(str)) != {SOURCE_CANDIDATE_SET_ID}:
        fail("chart review source_candidate_set_id mismatch")
    if set(latest["research_variant_id"].astype(str)) != {"warning_research_variant_only"}:
        fail("chart review must be marked warning_research_variant_only")
    if set(latest["advisory_status"].astype(str)) != {"warning_research_variant_only"}:
        fail("chart review advisory_status must be warning_research_variant_only")
    if set(latest["manual_review_status"].astype(str)) != {"pending_user_shape_review"}:
        fail("chart review manual_review_status must remain pending_user_shape_review")
    if not false_only(latest["approved_for_daily"]):
        fail("chart review approved_for_daily must remain false")

    invalid_categories = sorted(set(latest["category_id"].astype(str)) - set(CATEGORY_FOLDERS))
    if invalid_categories:
        fail(f"unexpected category_id values: {invalid_categories}")
    for category, folder in CATEGORY_FOLDERS.items():
        folder_path = CHART_ROOT / folder
        if not folder_path.exists():
            fail(f"missing category folder: {folder_path}")
        row_count = int(latest["category_folder"].astype(str).eq(folder).sum())
        png_count = len(list(folder_path.glob("*.png")))
        if row_count != png_count:
            fail(f"folder png count mismatch for {folder}: index={row_count} png={png_count}")

    for row_number, row in latest.iterrows():
        chart_path = Path(str(row.get("chart_path", "")))
        if not chart_path.exists():
            fail(f"missing chart image at row {row_number}: {chart_path}")
        if chart_path.suffix.lower() != ".png":
            fail(f"chart image must be .png at row {row_number}: {chart_path}")
        if chart_path.stat().st_size < 10_000:
            fail(f"chart image suspiciously small at row {row_number}: {chart_path}")
        category = str(row.get("category_id", ""))
        folder = str(row.get("category_folder", ""))
        if CATEGORY_FOLDERS.get(category) != folder:
            fail(f"category_folder mismatch at row {row_number}: {category} -> {folder}")

    print(
        "W-bottom candidate chart review packet validation passed "
        f"charts={len(latest)} chart_root={CHART_ROOT}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
