from __future__ import annotations

from pathlib import Path

import pandas as pd


ROOT = Path(".")
RESEARCH_LATEST_DIR = ROOT / "output" / "latest" / "research_backtest"
RESEARCH_HISTORY_DIR = ROOT / "output" / "history" / "research"

SOURCE_CHART_REVIEW_CSV = RESEARCH_LATEST_DIR / "w_bottom_candidate_chart_review_latest.csv"
SLOPE_REVIEW_ROOT = RESEARCH_LATEST_DIR / "w_bottom_candidate_slope_curvature_review"
LATEST_AUDIT_CSV = RESEARCH_LATEST_DIR / "w_bottom_candidate_slope_curvature_audit_latest.csv"
LATEST_AUDIT_MD = RESEARCH_LATEST_DIR / "w_bottom_candidate_slope_curvature_audit_latest.md"
HISTORY_AUDIT_CSV = RESEARCH_HISTORY_DIR / "w_bottom_candidate_slope_curvature_audit.csv"

REQUIRED_COLUMNS = {
    "model_id",
    "research_id",
    "source_research_id",
    "source_candidate_set_id",
    "research_variant_id",
    "advisory_status",
    "stock_id",
    "signal_date",
    "outcome_category_id",
    "slope_curvature_category",
    "slope_category_folder",
    "source_chart_path",
    "slope_review_chart_path",
    "path_days",
    "full_path_significant_turn_count",
    "full_path_abrupt_slope_change_count",
    "full_path_direction_switch_count",
    "first_low_sharp_v_flag",
    "second_low_sharp_v_flag",
    "slope_issue_reasons",
    "manual_review_status",
    "approved_for_daily",
    "generated_at",
}

SLOPE_CATEGORY_FOLDERS = {
    "smooth_rounded_w_like": "01_smooth_rounded_w_like",
    "sharp_v_bottom_risk": "02_sharp_v_bottom_risk",
    "wv_multiple_turn_risk": "03_wv_multiple_turn_risk",
    "slope_break_discontinuous": "04_slope_break_discontinuous",
    "insufficient_price_path": "99_insufficient_price_path",
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


def main() -> int:
    source = read_csv(SOURCE_CHART_REVIEW_CSV)
    latest = read_csv(LATEST_AUDIT_CSV)
    history = read_csv(HISTORY_AUDIT_CSV)
    if not LATEST_AUDIT_MD.exists():
        fail(f"missing required file: {LATEST_AUDIT_MD}")
    if not SLOPE_REVIEW_ROOT.exists():
        fail(f"missing slope review root: {SLOPE_REVIEW_ROOT}")
    md_lines = LATEST_AUDIT_MD.read_text(encoding="utf-8", errors="replace").splitlines()
    if len(md_lines) < 30:
        fail(f"{LATEST_AUDIT_MD} is suspiciously short")
    if latest.empty:
        fail(f"{LATEST_AUDIT_CSV} has no rows")
    if len(latest) != len(history):
        fail("latest and history slope audit row counts differ")
    if len(latest) != len(source):
        fail(f"slope audit rows must equal chart review rows: latest={len(latest)} source={len(source)}")

    missing = sorted(REQUIRED_COLUMNS - set(latest.columns))
    if missing:
        fail(f"{LATEST_AUDIT_CSV} missing columns: {missing}")
    missing_history = sorted(REQUIRED_COLUMNS - set(history.columns))
    if missing_history:
        fail(f"{HISTORY_AUDIT_CSV} missing columns: {missing_history}")

    forbidden = sorted((set(latest.columns) | set(history.columns)) & FORBIDDEN_PRODUCTION_FIELDS)
    if forbidden:
        fail(f"W-bottom slope audit must not emit production decision fields: {forbidden}")

    if set(latest["model_id"].astype(str)) != {"w_bottom_right_side"}:
        fail("slope audit model_id must be w_bottom_right_side")
    if set(latest["research_id"].astype(str)) != {"w_bottom_candidate_slope_curvature_audit"}:
        fail("slope audit research_id must be w_bottom_candidate_slope_curvature_audit")
    if set(latest["source_research_id"].astype(str)) != {"w_bottom_candidate_chart_review"}:
        fail("slope audit source_research_id must be w_bottom_candidate_chart_review")
    if set(latest["research_variant_id"].astype(str)) != {"warning_research_variant_only"}:
        fail("slope audit must be marked warning_research_variant_only")
    if set(latest["advisory_status"].astype(str)) != {"warning_research_variant_only"}:
        fail("slope audit advisory_status must be warning_research_variant_only")
    if set(latest["manual_review_status"].astype(str)) != {"pending_user_shape_review"}:
        fail("slope audit manual_review_status must remain pending_user_shape_review")
    if not false_only(latest["approved_for_daily"]):
        fail("slope audit approved_for_daily must remain false")

    invalid_categories = sorted(set(latest["slope_curvature_category"].astype(str)) - set(SLOPE_CATEGORY_FOLDERS))
    if invalid_categories:
        fail(f"unexpected slope_curvature_category values: {invalid_categories}")
    for category, folder in SLOPE_CATEGORY_FOLDERS.items():
        folder_path = SLOPE_REVIEW_ROOT / folder
        if not folder_path.exists():
            fail(f"missing slope category folder: {folder_path}")
        row_count = int(latest["slope_category_folder"].astype(str).eq(folder).sum())
        png_count = len(list(folder_path.glob("*.png")))
        if row_count != png_count:
            fail(f"folder png count mismatch for {folder}: index={row_count} png={png_count}")

    for column in ["path_days", "full_path_significant_turn_count", "full_path_abrupt_slope_change_count", "full_path_direction_switch_count"]:
        values = pd.to_numeric(latest[column], errors="coerce")
        if values.isna().any() or (values < 0).any():
            fail(f"{column} must be non-negative numeric")
    for column in ["first_low_sharp_v_flag", "second_low_sharp_v_flag"]:
        if not boolish_only(latest[column]):
            fail(f"{column} must be boolean-like")

    for row_number, row in latest.iterrows():
        source_chart = Path(str(row.get("source_chart_path", "")))
        slope_chart = Path(str(row.get("slope_review_chart_path", "")))
        if not source_chart.exists():
            fail(f"missing source chart at row {row_number}: {source_chart}")
        if not slope_chart.exists():
            fail(f"missing slope review chart at row {row_number}: {slope_chart}")
        if slope_chart.suffix.lower() != ".png":
            fail(f"slope review chart must be .png at row {row_number}: {slope_chart}")
        if slope_chart.stat().st_size < 10_000:
            fail(f"slope review chart suspiciously small at row {row_number}: {slope_chart}")
        category = str(row.get("slope_curvature_category", ""))
        folder = str(row.get("slope_category_folder", ""))
        if SLOPE_CATEGORY_FOLDERS.get(category) != folder:
            fail(f"slope_category_folder mismatch at row {row_number}: {category} -> {folder}")

    print(
        "W-bottom candidate slope curvature audit validation passed "
        f"rows={len(latest)} slope_review_root={SLOPE_REVIEW_ROOT}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
