from __future__ import annotations

from pathlib import Path

import pandas as pd


ROOT = Path(".")
RESEARCH_LATEST_DIR = ROOT / "output" / "latest" / "research_backtest"
RESEARCH_HISTORY_DIR = ROOT / "output" / "history" / "research"

SOURCE_DETAIL_CSV = RESEARCH_LATEST_DIR / "w_bottom_path_quality_filter_audit_detail_latest.csv"
LATEST_GRID_CSV = RESEARCH_LATEST_DIR / "w_bottom_wv_filter_stability_grid_latest.csv"
LATEST_GRID_MD = RESEARCH_LATEST_DIR / "w_bottom_wv_filter_stability_grid_latest.md"
HISTORY_GRID_CSV = RESEARCH_HISTORY_DIR / "w_bottom_wv_filter_stability_grid.csv"

REQUIRED_COLUMNS = {
    "model_id",
    "confirmation_model_id",
    "research_id",
    "source_research_id",
    "research_variant_id",
    "advisory_status",
    "filter_id",
    "filter_description",
    "segment_dimension",
    "segment_value",
    "segment_source",
    "has_taxonomy",
    "baseline_filter_id",
    "sample_size",
    "mature_sample_size",
    "win_count",
    "win_rate",
    "avg_a_return_pct",
    "median_a_return_pct",
    "baseline_sample_size",
    "baseline_mature_sample_size",
    "baseline_win_rate",
    "baseline_avg_a_return_pct",
    "delta_sample_size",
    "sample_retention_rate",
    "delta_win_rate_pct",
    "delta_avg_a_return_pct",
    "stability_signal",
    "sample_warning",
    "approved_for_daily",
    "production_readiness",
    "generated_at",
}

EXPECTED_FILTERS = {
    "observation_to_volume_confirmation",
    "exclude_wv_multiple_turn",
    "exclude_slope_break",
    "exclude_wv_or_slope_break",
    "exclude_sharp_v",
    "smooth_only",
}

EXPECTED_SEGMENT_DIMENSIONS = {
    "overall",
    "signal_month",
    "signal_quarter",
    "signal_half",
    "effective_mainstream_label",
    "has_hot_theme",
    "structural_theme_bucket",
}

STABILITY_SIGNALS = {
    "baseline",
    "insufficient_sample",
    "directionally_improved",
    "improved_but_median_still_weak",
    "mixed_flat_to_slightly_better",
    "not_improved",
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
    return set(series.astype(str).str.lower().unique()) <= {"true", "false", "1", "0"}


def main() -> int:
    source = read_csv(SOURCE_DETAIL_CSV)
    latest = read_csv(LATEST_GRID_CSV)
    history = read_csv(HISTORY_GRID_CSV)
    if not LATEST_GRID_MD.exists():
        fail(f"missing required file: {LATEST_GRID_MD}")
    md_lines = LATEST_GRID_MD.read_text(encoding="utf-8", errors="replace").splitlines()
    if len(md_lines) < 40:
        fail(f"{LATEST_GRID_MD} is suspiciously short")
    if latest.empty:
        fail(f"{LATEST_GRID_CSV} has no rows")
    if len(latest) != len(history):
        fail("latest and history stability grid row counts differ")

    missing = sorted(REQUIRED_COLUMNS - set(latest.columns))
    if missing:
        fail(f"{LATEST_GRID_CSV} missing columns: {missing}")
    missing_history = sorted(REQUIRED_COLUMNS - set(history.columns))
    if missing_history:
        fail(f"{HISTORY_GRID_CSV} missing columns: {missing_history}")

    forbidden = sorted((set(latest.columns) | set(history.columns)) & FORBIDDEN_PRODUCTION_FIELDS)
    if forbidden:
        fail(f"W-bottom WV/WVV stability grid must not emit production decision fields: {forbidden}")

    if set(latest["model_id"].astype(str)) != {"w_bottom_right_side"}:
        fail("grid model_id must be w_bottom_right_side")
    if set(latest["confirmation_model_id"].astype(str)) != {"neckline_volume_breakout_confirmation"}:
        fail("grid confirmation_model_id must be neckline_volume_breakout_confirmation")
    if set(latest["research_id"].astype(str)) != {"w_bottom_wv_filter_stability_grid"}:
        fail("grid research_id must be w_bottom_wv_filter_stability_grid")
    if set(latest["source_research_id"].astype(str)) != {"w_bottom_path_quality_filter_audit"}:
        fail("grid source_research_id must be w_bottom_path_quality_filter_audit")
    if set(latest["research_variant_id"].astype(str)) != {"warning_research_variant_only"}:
        fail("grid research_variant_id must be warning_research_variant_only")
    if set(latest["advisory_status"].astype(str)) != {"warning_research_variant_only"}:
        fail("grid advisory_status must be warning_research_variant_only")
    if set(latest["production_readiness"].astype(str)) != {"not_production_ready_research_only"}:
        fail("grid production_readiness must remain not_production_ready_research_only")
    if not false_only(latest["approved_for_daily"]):
        fail("grid approved_for_daily must remain false")
    if not boolish_only(latest["has_taxonomy"]):
        fail("has_taxonomy must be boolean-like")

    filters = set(latest["filter_id"].astype(str))
    if not EXPECTED_FILTERS <= filters:
        fail(f"missing expected filters: {sorted(EXPECTED_FILTERS - filters)}")
    dimensions = set(latest["segment_dimension"].astype(str))
    if not EXPECTED_SEGMENT_DIMENSIONS <= dimensions:
        fail(f"missing expected segment dimensions: {sorted(EXPECTED_SEGMENT_DIMENSIONS - dimensions)}")
    invalid_signals = sorted(set(latest["stability_signal"].astype(str)) - STABILITY_SIGNALS)
    if invalid_signals:
        fail(f"unexpected stability_signal values: {invalid_signals}")

    numeric_columns = [
        "sample_size",
        "mature_sample_size",
        "win_count",
        "baseline_sample_size",
        "baseline_mature_sample_size",
        "delta_sample_size",
        "smooth_count",
        "sharp_v_count",
        "wv_multiple_turn_count",
        "slope_break_count",
        "tdcc_any_age7_count",
    ]
    for column in numeric_columns:
        values = pd.to_numeric(latest[column], errors="coerce")
        if values.isna().any():
            fail(f"{column} must be numeric for every row")

    overall = latest[latest["segment_dimension"].eq("overall")]
    if set(overall["filter_id"].astype(str)) != EXPECTED_FILTERS:
        fail("overall rows must contain exactly the expected filter set")
    baseline = overall[overall["filter_id"].eq("observation_to_volume_confirmation")]
    exclude_wv = overall[overall["filter_id"].eq("exclude_wv_multiple_turn")]
    if baseline.empty or exclude_wv.empty:
        fail("overall baseline and exclude_wv_multiple_turn rows are required")
    baseline_sample = int(pd.to_numeric(baseline.iloc[0]["sample_size"], errors="coerce"))
    exclude_sample = int(pd.to_numeric(exclude_wv.iloc[0]["sample_size"], errors="coerce"))
    source_baseline = source[source["transition_status"].astype(str).eq("observation_to_volume_confirmation")]
    if baseline_sample != len(source_baseline):
        fail(f"overall baseline sample_size must match source baseline rows: {baseline_sample} != {len(source_baseline)}")
    if exclude_sample >= baseline_sample:
        fail("exclude_wv_multiple_turn must reduce sample size versus baseline")

    print(
        "W-bottom WV/WVV filter stability grid validation passed "
        f"rows={len(latest)} overall_baseline_sample={baseline_sample} "
        f"overall_exclude_wv_sample={exclude_sample}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
