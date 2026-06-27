from __future__ import annotations

from pathlib import Path

import pandas as pd


ROOT = Path(".")
RESEARCH_LATEST_DIR = ROOT / "output" / "latest" / "research_backtest"
RESEARCH_HISTORY_DIR = ROOT / "output" / "history" / "research"

SOURCE_DETAIL_CSV = RESEARCH_LATEST_DIR / "w_bottom_price_level_audit_detail_latest.csv"
LATEST_GRID_CSV = RESEARCH_LATEST_DIR / "w_bottom_price_level_filter_grid_latest.csv"
LATEST_GRID_MD = RESEARCH_LATEST_DIR / "w_bottom_price_level_filter_grid_latest.md"
HISTORY_GRID_CSV = RESEARCH_HISTORY_DIR / "w_bottom_price_level_filter_grid.csv"

MODEL_ID = "w_bottom_right_side"
CONFIRMATION_MODEL_ID = "neckline_volume_breakout_confirmation"
RESEARCH_ID = "w_bottom_price_level_filter_grid"
SOURCE_RESEARCH_ID = "w_bottom_price_level_audit"
RESEARCH_VARIANT_ID = "warning_research_variant_only"
OBSERVATION_TO_VOLUME = "observation_to_volume_confirmation"
WV_CATEGORY = "wv_multiple_turn_risk"
BASELINE_FILTER_ID = "baseline_no_price_level_filter"
PRICE_FILTER_ID = "price_position_252_le_40"
PRICE_POSITION_MAX_PCT = 40.0

EXPECTED_BASE_SCOPES = {
    "all_w_bottom_candidates",
    "observation_to_volume_confirmation",
    "observation_volume_exclude_wv",
    "core_mainstream_observation_volume_exclude_wv",
}

EXPECTED_SEGMENT_DIMENSIONS = {
    "overall",
    "signal_quarter",
    "effective_mainstream_label",
}

EXPECTED_FILTERS = {
    BASELINE_FILTER_ID,
    PRICE_FILTER_ID,
}

STABILITY_SIGNALS = {
    "baseline",
    "insufficient_sample",
    "directionally_improved",
    "improved_but_median_still_weak",
    "mixed_flat_to_slightly_better",
    "not_improved",
}

REQUIRED_COLUMNS = {
    "model_id",
    "confirmation_model_id",
    "research_id",
    "source_research_id",
    "research_variant_id",
    "advisory_status",
    "base_scope_id",
    "segment_dimension",
    "segment_value",
    "filter_id",
    "price_position_max_pct",
    "sample_size",
    "mature_sample_size",
    "win_count",
    "win_rate_pct",
    "avg_a_return_pct",
    "median_a_return_pct",
    "baseline_sample_size",
    "baseline_mature_sample_size",
    "baseline_win_rate_pct",
    "baseline_avg_a_return_pct",
    "baseline_median_a_return_pct",
    "delta_sample_size",
    "sample_retention_rate_pct",
    "delta_win_rate_pct",
    "delta_avg_a_return_pct",
    "delta_median_a_return_pct",
    "volume_confirmation_count",
    "tdcc_any_age7_count",
    "smooth_count",
    "sharp_v_count",
    "wv_multiple_turn_count",
    "slope_break_count",
    "bottom_quartile_count",
    "low_level_count",
    "mid_level_count",
    "high_level_count",
    "avg_price_position_252_pct",
    "median_price_position_252_pct",
    "stability_signal",
    "sample_warning",
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


def false_only(series: pd.Series) -> bool:
    return set(series.astype(str).str.lower().unique()) <= {"false", "0", ""}


def normalize_date(value: object) -> str:
    digits = "".join(ch for ch in str(value) if ch.isdigit())
    return digits[:8]


def prepare_source(source: pd.DataFrame) -> pd.DataFrame:
    source = source.copy()
    source["signal_date"] = source["signal_date"].map(normalize_date)
    source["signal_quarter"] = pd.to_datetime(source["signal_date"], format="%Y%m%d", errors="coerce").dt.to_period("Q").astype(str)
    source["signal_quarter"] = source["signal_quarter"].replace("NaT", "unknown_quarter")
    return source


def source_scope(source: pd.DataFrame, scope: str) -> pd.DataFrame:
    if scope == "all_w_bottom_candidates":
        return source.copy()
    if scope == "observation_to_volume_confirmation":
        return source[source["transition_status"].eq(OBSERVATION_TO_VOLUME)].copy()
    if scope == "observation_volume_exclude_wv":
        return source[source["transition_status"].eq(OBSERVATION_TO_VOLUME) & ~source["slope_curvature_category"].eq(WV_CATEGORY)].copy()
    if scope == "core_mainstream_observation_volume_exclude_wv":
        return source[
            source["transition_status"].eq(OBSERVATION_TO_VOLUME)
            & ~source["slope_curvature_category"].eq(WV_CATEGORY)
            & source["effective_mainstream_label"].eq("core_mainstream")
        ].copy()
    fail(f"unexpected scope: {scope}")


def source_segment(scope_df: pd.DataFrame, dimension: str, value: str) -> pd.DataFrame:
    if dimension == "overall":
        return scope_df.copy() if value == "all" else scope_df.iloc[0:0].copy()
    return scope_df[scope_df[dimension].astype(str).eq(value)].copy()


def numeric_columns() -> list[str]:
    return [
        "sample_size",
        "mature_sample_size",
        "win_count",
        "baseline_sample_size",
        "baseline_mature_sample_size",
        "delta_sample_size",
        "volume_confirmation_count",
        "tdcc_any_age7_count",
        "smooth_count",
        "sharp_v_count",
        "wv_multiple_turn_count",
        "slope_break_count",
        "bottom_quartile_count",
        "low_level_count",
        "mid_level_count",
        "high_level_count",
    ]


def validate_constants(grid: pd.DataFrame) -> None:
    constants = {
        "model_id": MODEL_ID,
        "confirmation_model_id": CONFIRMATION_MODEL_ID,
        "research_id": RESEARCH_ID,
        "source_research_id": SOURCE_RESEARCH_ID,
        "research_variant_id": RESEARCH_VARIANT_ID,
        "advisory_status": RESEARCH_VARIANT_ID,
        "production_readiness": "not_production_ready_research_only",
    }
    for column, expected in constants.items():
        values = set(grid[column].astype(str))
        if values != {expected}:
            fail(f"{column} must be {expected}; got {sorted(values)}")
    if not false_only(grid["approved_for_daily"]):
        fail("approved_for_daily must remain false")


def main() -> int:
    source = prepare_source(read_csv(SOURCE_DETAIL_CSV))
    latest = read_csv(LATEST_GRID_CSV)
    history = read_csv(HISTORY_GRID_CSV)

    if not LATEST_GRID_MD.exists():
        fail(f"missing required file: {LATEST_GRID_MD}")
    md_text = LATEST_GRID_MD.read_text(encoding="utf-8", errors="replace")
    if len(md_text.splitlines()) < 45:
        fail(f"{LATEST_GRID_MD} is suspiciously short")
    if "production impact: `none`" not in md_text:
        fail("markdown must explicitly state production impact is none")
    if "price_position_252_pct <= 40.0" not in md_text:
        fail("markdown must document the price-position filter")

    if latest.empty:
        fail(f"{LATEST_GRID_CSV} has no rows")
    if len(latest) != len(history):
        fail("latest/history grid row counts differ")
    missing = sorted(REQUIRED_COLUMNS - set(latest.columns))
    if missing:
        fail(f"{LATEST_GRID_CSV} missing columns: {missing}")
    missing_history = sorted(REQUIRED_COLUMNS - set(history.columns))
    if missing_history:
        fail(f"{HISTORY_GRID_CSV} missing columns: {missing_history}")
    forbidden = sorted((set(latest.columns) | set(history.columns)) & FORBIDDEN_PRODUCTION_FIELDS)
    if forbidden:
        fail(f"price-level filter grid must not emit production decision fields: {forbidden}")

    validate_constants(latest)
    validate_constants(history)

    invalid_scopes = sorted(set(latest["base_scope_id"].astype(str)) - EXPECTED_BASE_SCOPES)
    invalid_dimensions = sorted(set(latest["segment_dimension"].astype(str)) - EXPECTED_SEGMENT_DIMENSIONS)
    invalid_filters = sorted(set(latest["filter_id"].astype(str)) - EXPECTED_FILTERS)
    invalid_signals = sorted(set(latest["stability_signal"].astype(str)) - STABILITY_SIGNALS)
    if invalid_scopes:
        fail(f"unexpected base_scope_id values: {invalid_scopes}")
    if invalid_dimensions:
        fail(f"unexpected segment_dimension values: {invalid_dimensions}")
    if invalid_filters:
        fail(f"unexpected filter_id values: {invalid_filters}")
    if invalid_signals:
        fail(f"unexpected stability_signal values: {invalid_signals}")

    for column in numeric_columns():
        values = pd.to_numeric(latest[column], errors="coerce")
        if values.isna().any():
            fail(f"{column} must be numeric for every row")
    price_filter_rows = latest[latest["filter_id"].eq(PRICE_FILTER_ID)]
    if not pd.to_numeric(price_filter_rows["price_position_max_pct"], errors="coerce").eq(PRICE_POSITION_MAX_PCT).all():
        fail("price filter rows must set price_position_max_pct to 40.0")
    baseline_rows = latest[latest["filter_id"].eq(BASELINE_FILTER_ID)]
    if not baseline_rows["price_position_max_pct"].astype(str).eq("").all():
        fail("baseline rows must leave price_position_max_pct blank")

    group_cols = ["base_scope_id", "segment_dimension", "segment_value"]
    for _, group in latest.groupby(group_cols, dropna=False):
        filters = set(group["filter_id"].astype(str))
        if filters != EXPECTED_FILTERS:
            fail(f"each scope/segment group must have baseline and price filter rows; got {filters}")
        baseline = group[group["filter_id"].eq(BASELINE_FILTER_ID)].iloc[0]
        filtered = group[group["filter_id"].eq(PRICE_FILTER_ID)].iloc[0]
        if baseline["stability_signal"] != "baseline":
            fail("baseline row must have stability_signal=baseline")
        if int(filtered["sample_size"]) > int(baseline["sample_size"]):
            fail("price filter sample_size must not exceed baseline sample_size")
        if int(filtered["mid_level_count"]) != 0 or int(filtered["high_level_count"]) != 0:
            fail("price filter rows must not contain mid/high level rows")
        if int(filtered["bottom_quartile_count"]) + int(filtered["low_level_count"]) != int(filtered["sample_size"]):
            fail("price filter rows must equal bottom+low level counts")

    overall_all = latest[
        latest["base_scope_id"].eq("all_w_bottom_candidates")
        & latest["segment_dimension"].eq("overall")
        & latest["segment_value"].eq("all")
    ]
    if len(overall_all) != 2:
        fail("must have two overall all_w_bottom_candidates rows")
    source_all = len(source)
    baseline_sample = int(overall_all[overall_all["filter_id"].eq(BASELINE_FILTER_ID)].iloc[0]["sample_size"])
    filter_sample = int(overall_all[overall_all["filter_id"].eq(PRICE_FILTER_ID)].iloc[0]["sample_size"])
    expected_filter_sample = int(pd.to_numeric(source["price_position_252_pct"], errors="coerce").le(PRICE_POSITION_MAX_PCT).sum())
    if baseline_sample != source_all:
        fail(f"overall baseline sample must match source rows: {baseline_sample} != {source_all}")
    if filter_sample != expected_filter_sample:
        fail(f"overall price filter sample mismatch: {filter_sample} != {expected_filter_sample}")

    for scope in EXPECTED_BASE_SCOPES:
        scope_df = source_scope(source, scope)
        overall_group = latest[
            latest["base_scope_id"].eq(scope)
            & latest["segment_dimension"].eq("overall")
            & latest["segment_value"].eq("all")
        ]
        if len(overall_group) != 2:
            fail(f"missing overall rows for scope {scope}")
        baseline = overall_group[overall_group["filter_id"].eq(BASELINE_FILTER_ID)].iloc[0]
        filtered = overall_group[overall_group["filter_id"].eq(PRICE_FILTER_ID)].iloc[0]
        expected_filtered = int(pd.to_numeric(scope_df["price_position_252_pct"], errors="coerce").le(PRICE_POSITION_MAX_PCT).sum())
        if int(baseline["sample_size"]) != len(scope_df):
            fail(f"{scope} baseline sample mismatch")
        if int(filtered["sample_size"]) != expected_filtered:
            fail(f"{scope} price filter sample mismatch")

    print(
        "W-bottom price-level filter grid validation passed "
        f"rows={len(latest)} overall_source={source_all} overall_price_filter={filter_sample}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
