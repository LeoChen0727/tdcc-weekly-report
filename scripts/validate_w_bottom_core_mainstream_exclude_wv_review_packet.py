from __future__ import annotations

from pathlib import Path

import pandas as pd


ROOT = Path(".")
RESEARCH_LATEST_DIR = ROOT / "output" / "latest" / "research_backtest"
RESEARCH_HISTORY_DIR = ROOT / "output" / "history" / "research"

SOURCE_DETAIL_CSV = RESEARCH_LATEST_DIR / "w_bottom_path_quality_filter_audit_detail_latest.csv"
SOURCE_TAXONOMY_CSV = ROOT / "output" / "latest" / "stock_theme_taxonomy_latest.csv"
CHART_ROOT = RESEARCH_LATEST_DIR / "w_bottom_core_mainstream_exclude_wv_review"
LATEST_INDEX_CSV = RESEARCH_LATEST_DIR / "w_bottom_core_mainstream_exclude_wv_review_latest.csv"
LATEST_INDEX_MD = RESEARCH_LATEST_DIR / "w_bottom_core_mainstream_exclude_wv_review_latest.md"
HISTORY_INDEX_CSV = RESEARCH_HISTORY_DIR / "w_bottom_core_mainstream_exclude_wv_review.csv"

MODEL_ID = "w_bottom_right_side"
CONFIRMATION_MODEL_ID = "neckline_volume_breakout_confirmation"
RESEARCH_ID = "w_bottom_core_mainstream_exclude_wv_review"
SOURCE_RESEARCH_ID = "w_bottom_wv_filter_stability_grid"
RESEARCH_VARIANT_ID = "warning_research_variant_only"
TARGET_TRANSITION_STATUS = "observation_to_volume_confirmation"
TARGET_SEGMENT_DIMENSION = "effective_mainstream_label"
TARGET_SEGMENT_VALUE = "core_mainstream"
TARGET_FILTER_ID = "exclude_wv_multiple_turn"
EXCLUDED_PATH_CATEGORY = "wv_multiple_turn_risk"

REQUIRED_COLUMNS = {
    "model_id",
    "confirmation_model_id",
    "research_id",
    "source_research_id",
    "source_detail_research_id",
    "source_quality_research_id",
    "research_variant_id",
    "advisory_status",
    "segment_dimension",
    "segment_value",
    "filter_id",
    "transition_status",
    "stock_id",
    "signal_date",
    "slope_curvature_category",
    "left_peak_date",
    "left_low_date",
    "neckline_date",
    "right_low_date",
    "signal_distance_to_neckline_pct",
    "signal_rebound_from_right_low_pct",
    "second_arc_volume_ratio",
    "a_mature",
    "a_return_pct",
    "tdcc_any_age7",
    "effective_mainstream_label",
    "has_hot_theme",
    "structural_theme_bucket",
    "chart_path",
    "chart_path_absolute",
    "manual_review_status",
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
    print(f"ERROR: {message}")
    raise SystemExit(1)


def read_csv(path: Path) -> pd.DataFrame:
    if not path.exists():
        fail(f"missing required file: {path}")
    try:
        return pd.read_csv(path, dtype=str, keep_default_na=False)
    except Exception as exc:
        fail(f"{path} is not readable CSV: {exc}")


def normalize_code(value: object) -> str:
    text = "" if value is None else str(value).replace("\ufeff", "").strip()
    if text.endswith(".0"):
        text = text[:-2]
    return text.zfill(4) if text.isdigit() and len(text) < 4 else text


def normalize_date(value: object) -> str:
    digits = "".join(ch for ch in str(value) if ch.isdigit())
    return digits[:8]


def false_only(series: pd.Series) -> bool:
    return set(series.astype(str).str.lower().unique()) <= {"false", "0", ""}


def expected_selection() -> pd.DataFrame:
    detail = read_csv(SOURCE_DETAIL_CSV)
    taxonomy = read_csv(SOURCE_TAXONOMY_CSV)
    if "stock_id" not in detail.columns or "stock_id" not in taxonomy.columns:
        fail("source detail and taxonomy must both have stock_id")
    for column in ["transition_status", "slope_curvature_category"]:
        if column not in detail.columns:
            fail(f"path quality detail missing {column}")
    if TARGET_SEGMENT_DIMENSION not in taxonomy.columns:
        fail(f"taxonomy missing {TARGET_SEGMENT_DIMENSION}")
    detail = detail.copy()
    taxonomy = taxonomy.copy()
    detail["stock_id"] = detail["stock_id"].map(normalize_code)
    detail["signal_date"] = detail["signal_date"].map(normalize_date)
    taxonomy["stock_id"] = taxonomy["stock_id"].map(normalize_code)
    taxonomy = taxonomy[["stock_id", TARGET_SEGMENT_DIMENSION]].drop_duplicates("stock_id", keep="first")
    merged = detail.merge(taxonomy, on="stock_id", how="left")
    return merged[
        merged["transition_status"].eq(TARGET_TRANSITION_STATUS)
        & ~merged["slope_curvature_category"].eq(EXCLUDED_PATH_CATEGORY)
        & merged[TARGET_SEGMENT_DIMENSION].eq(TARGET_SEGMENT_VALUE)
    ].copy()


def main() -> int:
    latest = read_csv(LATEST_INDEX_CSV)
    history = read_csv(HISTORY_INDEX_CSV)
    expected = expected_selection()
    if not LATEST_INDEX_MD.exists():
        fail(f"missing required file: {LATEST_INDEX_MD}")
    if not CHART_ROOT.exists():
        fail(f"missing chart root: {CHART_ROOT}")
    md_text = LATEST_INDEX_MD.read_text(encoding="utf-8", errors="replace")
    if len(md_text.splitlines()) < 35:
        fail(f"{LATEST_INDEX_MD} is suspiciously short")
    if "production impact: `none`" not in md_text:
        fail("markdown must explicitly state production impact is none")
    if "not_production_ready_research_only" not in md_text:
        fail("markdown must preserve research-only production readiness")

    if latest.empty:
        fail(f"{LATEST_INDEX_CSV} has no rows")
    missing = sorted(REQUIRED_COLUMNS - set(latest.columns))
    if missing:
        fail(f"{LATEST_INDEX_CSV} missing columns: {missing}")
    missing_history = sorted(REQUIRED_COLUMNS - set(history.columns))
    if missing_history:
        fail(f"{HISTORY_INDEX_CSV} missing columns: {missing_history}")
    forbidden = sorted((set(latest.columns) | set(history.columns)) & FORBIDDEN_PRODUCTION_FIELDS)
    if forbidden:
        fail(f"review packet must not emit production decision fields: {forbidden}")
    if len(latest) != len(history):
        fail("latest and history review packet row counts differ")
    if len(latest) != len(expected):
        fail(f"review packet count mismatch: latest={len(latest)} expected={len(expected)}")

    constants = {
        "model_id": MODEL_ID,
        "confirmation_model_id": CONFIRMATION_MODEL_ID,
        "research_id": RESEARCH_ID,
        "source_research_id": SOURCE_RESEARCH_ID,
        "research_variant_id": RESEARCH_VARIANT_ID,
        "advisory_status": RESEARCH_VARIANT_ID,
        "segment_dimension": TARGET_SEGMENT_DIMENSION,
        "segment_value": TARGET_SEGMENT_VALUE,
        "filter_id": TARGET_FILTER_ID,
        "transition_status": TARGET_TRANSITION_STATUS,
        "manual_review_status": "pending_user_shape_review",
        "production_readiness": "not_production_ready_research_only",
    }
    for column, expected_value in constants.items():
        values = set(latest[column].astype(str))
        if values != {expected_value}:
            fail(f"{column} must be {expected_value}; got {sorted(values)}")
    if not false_only(latest["approved_for_daily"]):
        fail("approved_for_daily must remain false")
    if latest["slope_curvature_category"].astype(str).eq(EXCLUDED_PATH_CATEGORY).any():
        fail(f"review packet must exclude {EXCLUDED_PATH_CATEGORY}")
    if set(latest["effective_mainstream_label"].astype(str)) != {TARGET_SEGMENT_VALUE}:
        fail("review packet must contain only core_mainstream rows")

    key_columns = ["stock_id", "signal_date"]
    latest_keys = latest[key_columns].copy()
    expected_keys = expected[key_columns].copy()
    latest_keys["stock_id"] = latest_keys["stock_id"].map(normalize_code)
    expected_keys["stock_id"] = expected_keys["stock_id"].map(normalize_code)
    latest_keys["signal_date"] = latest_keys["signal_date"].map(normalize_date)
    expected_keys["signal_date"] = expected_keys["signal_date"].map(normalize_date)
    latest_key_set = set(map(tuple, latest_keys.to_records(index=False)))
    expected_key_set = set(map(tuple, expected_keys.to_records(index=False)))
    if latest_key_set != expected_key_set:
        fail("review packet keys do not match expected core-mainstream exclude-WV selection")

    png_paths = list(CHART_ROOT.glob("*.png"))
    if len(png_paths) != len(latest):
        fail(f"chart png count mismatch: png={len(png_paths)} rows={len(latest)}")
    for row_number, row in latest.iterrows():
        chart_path = Path(str(row.get("chart_path", "")))
        if not chart_path.exists():
            fail(f"missing chart image at row {row_number}: {chart_path}")
        if chart_path.suffix.lower() != ".png":
            fail(f"chart image must be .png at row {row_number}: {chart_path}")
        if chart_path.stat().st_size < 10_000:
            fail(f"chart image suspiciously small at row {row_number}: {chart_path}")

    mature = latest[latest["a_mature"].astype(str).str.lower().eq("true")].copy()
    returns = pd.to_numeric(mature["a_return_pct"], errors="coerce").dropna()
    print(
        "W-bottom core-mainstream exclude-WV review packet validation passed "
        f"rows={len(latest)} mature={len(returns)} "
        f"wins={int(returns.gt(0).sum())} charts={len(png_paths)}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
