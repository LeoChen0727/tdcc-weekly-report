from __future__ import annotations

from datetime import datetime
from pathlib import Path
from typing import Any, Callable
from zoneinfo import ZoneInfo
import math

import pandas as pd

import build_w_bottom_tdcc_abc_backtest as w_bottom
from build_w_bottom_path_quality_filter_audit import build_path_metrics


ROOT = Path(".")
RESEARCH_LATEST_DIR = ROOT / "output" / "latest" / "research_backtest"
RESEARCH_HISTORY_DIR = ROOT / "output" / "history" / "research"

BASELINE_EVENTS_CSV = RESEARCH_HISTORY_DIR / "w_bottom_tdcc_abc_events.csv"
VARIANT_EVENTS_CSV = RESEARCH_LATEST_DIR / "w_bottom_nearest_micro_anchor_event_replay_events_latest.csv"
TAXONOMY_CSV = ROOT / "output" / "latest" / "stock_theme_taxonomy_latest.csv"

LATEST_DETAIL_CSV = RESEARCH_LATEST_DIR / "w_bottom_combined_condition_backtest_detail_latest.csv"
LATEST_GRID_CSV = RESEARCH_LATEST_DIR / "w_bottom_combined_condition_backtest_latest.csv"
LATEST_MD = RESEARCH_LATEST_DIR / "w_bottom_combined_condition_backtest_latest.md"
HISTORY_DETAIL_CSV = RESEARCH_HISTORY_DIR / "w_bottom_combined_condition_backtest_detail.csv"
HISTORY_GRID_CSV = RESEARCH_HISTORY_DIR / "w_bottom_combined_condition_backtest.csv"

MODEL_ID = "w_bottom_right_side"
CONFIRMATION_MODEL_ID = "neckline_volume_breakout_confirmation"
OVERLAY_MODEL_ID = "tdcc_weekly_ranking_formula"
RESEARCH_ID = "w_bottom_combined_condition_backtest"
SOURCE_RESEARCH_ID = "w_bottom_nearest_micro_anchor_event_replay"
RESEARCH_VARIANT_ID = "warning_research_variant_only"
PARAMETER_SET_ID = "w_bottom_combined_condition_backtest_20260626"
PRODUCTION_READINESS = "not_production_ready_research_only"
PRIMARY_SYMMETRY_RATIO = 1.5
BASELINE_EVENT_SET_ID = "baseline_current_detector"
VARIANT_EVENT_SET_ID = "variant_nearest_micro_45d_event_replay"
REVENUE_CATALYST_STATUS = "pending_historical_feature_join_not_evaluated"

FORBIDDEN_PRODUCTION_FIELDS = {
    "trade_decision",
    "action_rating",
    "entry_style",
    "position_sizing",
    "decision_score",
    "daily_candidate_decision",
    "buy_signal",
}

DETAIL_COLUMNS = [
    "model_id",
    "confirmation_model_id",
    "overlay_model_id",
    "research_id",
    "source_research_id",
    "research_variant_id",
    "parameter_set_id",
    "advisory_status",
    "event_set_id",
    "comparison_status",
    "sample_mode",
    "symmetry_ratio",
    "stock_id",
    "stock_name",
    "signal_date",
    "left_peak_date",
    "left_low_date",
    "neckline_date",
    "right_low_date",
    "breakout_date",
    "post_confirmation_trigger_id",
    "post_confirmation_date",
    "signal_close",
    "neckline_price",
    "second_arc_volume_ratio",
    "has_neckline_breakout",
    "late_breakout_not_w",
    "has_post_confirmation",
    "a_mature",
    "a_return_pct",
    "c_mature",
    "c_return_pct",
    "tdcc_any_age7",
    "tdcc_any_age14",
    "tdcc_top50_age7",
    "tdcc_top20_age7",
    "tdcc_weekly_top20_age7",
    "tdcc_consecutive_top20_age7",
    "lookback_observed_days",
    "price_position_252_pct",
    "below_252_median",
    "below_252_mean",
    "price_level_bucket",
    "slope_curvature_category",
    "slope_issue_reasons",
    "effective_mainstream_label",
    "has_hot_theme",
    "structural_theme_bucket",
    "primary_theme",
    "taxonomy_source",
    "taxonomy_confidence",
    "revenue_catalyst_feature_status",
    "manual_review_status",
    "approved_for_daily",
    "production_readiness",
    "generated_at",
]

GRID_COLUMNS = [
    "model_id",
    "confirmation_model_id",
    "overlay_model_id",
    "research_id",
    "source_research_id",
    "research_variant_id",
    "parameter_set_id",
    "advisory_status",
    "event_set_id",
    "entry_timing_id",
    "condition_set_id",
    "condition_set_description",
    "sample_size",
    "mature_sample_size",
    "win_count",
    "win_rate_pct",
    "avg_return_pct",
    "median_return_pct",
    "baseline_sample_size",
    "baseline_mature_sample_size",
    "baseline_win_rate_pct",
    "baseline_avg_return_pct",
    "baseline_median_return_pct",
    "delta_sample_size_vs_baseline",
    "delta_mature_sample_size_vs_baseline",
    "sample_retention_rate_pct",
    "delta_win_rate_pct_vs_baseline",
    "delta_avg_return_pct_vs_baseline",
    "delta_median_return_pct_vs_baseline",
    "breakout_signal_count",
    "post_confirmation_count",
    "tdcc_any_age7_count",
    "tdcc_any_age14_count",
    "core_mainstream_count",
    "hot_theme_count",
    "bottom_quartile_count",
    "low_level_count",
    "mid_level_count",
    "high_level_count",
    "wv_multiple_turn_count",
    "sharp_v_count",
    "slope_break_count",
    "smooth_count",
    "avg_price_position_252_pct",
    "median_price_position_252_pct",
    "sample_warning",
    "research_interpretation",
    "revenue_catalyst_feature_status",
    "approved_for_daily",
    "production_readiness",
    "generated_at",
]


def now_text() -> str:
    return datetime.now(ZoneInfo("Asia/Taipei")).strftime("%Y-%m-%d %H:%M:%S Asia/Taipei")


def safe_str(value: Any) -> str:
    return w_bottom.safe_str(value)


def safe_float(value: Any) -> float:
    return w_bottom.safe_float(value)


def normalize_code(value: Any) -> str:
    return w_bottom.normalize_code(value)


def normalize_date(value: Any) -> str:
    return w_bottom.normalize_date(value)


def bool_value(value: Any) -> bool:
    return safe_str(value).lower() in {"true", "1", "yes", "y"}


def bool_text(value: bool) -> str:
    return "true" if value else "false"


def metric_text(value: float, digits: int = 4) -> str:
    if math.isnan(value) or math.isinf(value):
        return ""
    return f"{value:.{digits}f}"


def read_csv(path: Path) -> pd.DataFrame:
    if not path.exists():
        raise SystemExit(f"ERROR: missing required input: {path}")
    return pd.read_csv(path, dtype=str, keep_default_na=False)


def write_csv(df: pd.DataFrame, path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(path, index=False, encoding="utf-8-sig")


def comparable_events(events: pd.DataFrame, event_set_id: str) -> pd.DataFrame:
    required = {
        "stock_id",
        "stock_name",
        "signal_date",
        "symmetry_ratio",
        "dedup_20d_eligible",
        "left_peak_date",
        "left_low_date",
        "neckline_date",
        "right_low_date",
        "breakout_date",
        "a_mature",
        "a_return_pct",
        "c_mature",
        "c_return_pct",
        "tdcc_any_age7",
        "tdcc_any_age14",
        "post_confirmation_trigger_id",
    }
    missing = sorted(required - set(events.columns))
    if missing:
        raise SystemExit(f"ERROR: {event_set_id} events missing columns: {missing}")
    sample = events[
        events["symmetry_ratio"].astype(float).eq(PRIMARY_SYMMETRY_RATIO)
        & events["dedup_20d_eligible"].map(bool_value)
    ].copy()
    sample["stock_id"] = sample["stock_id"].map(normalize_code)
    sample["signal_date"] = sample["signal_date"].map(normalize_date)
    sample["event_set_id"] = event_set_id
    sample["sample_mode"] = "dedup_approx_20_trading_days"
    return sample.sort_values(["stock_id", "signal_date"]).drop_duplicates(["stock_id", "signal_date"], keep="first")


def event_key_map(events: pd.DataFrame) -> set[tuple[str, str]]:
    return set(zip(events["stock_id"].map(normalize_code), events["signal_date"].map(normalize_date)))


def load_taxonomy() -> dict[str, dict[str, str]]:
    if not TAXONOMY_CSV.exists():
        return {}
    taxonomy = read_csv(TAXONOMY_CSV)
    result: dict[str, dict[str, str]] = {}
    for _, row in taxonomy.iterrows():
        stock_id = normalize_code(row.get("stock_id"))
        if not stock_id:
            continue
        result[stock_id] = {
            "effective_mainstream_label": safe_str(row.get("effective_mainstream_label")) or "taxonomy_missing",
            "has_hot_theme": bool_text(bool_value(row.get("has_hot_theme"))),
            "structural_theme_bucket": safe_str(row.get("structural_theme_bucket")) or "taxonomy_missing",
            "primary_theme": safe_str(row.get("primary_theme")),
            "taxonomy_source": safe_str(row.get("taxonomy_source")) or "stock_theme_taxonomy_latest",
            "taxonomy_confidence": safe_str(row.get("confidence")) or safe_str(row.get("taxonomy_confidence")) or "pending_review",
        }
    return result


def price_level_for(stock_id: str, signal_date: str) -> dict[str, Any]:
    path = w_bottom.PRICE_DIR / f"{normalize_code(stock_id)}.csv"
    if not path.exists():
        return price_level_missing()
    price = pd.read_csv(path, dtype=str, keep_default_na=False)
    if "date" not in price.columns or "close" not in price.columns:
        return price_level_missing()
    price = price.copy()
    price["date"] = price["date"].map(normalize_date)
    price["close_numeric"] = pd.to_numeric(price["close"], errors="coerce")
    history = price[price["date"].le(signal_date) & price["close_numeric"].notna()].sort_values("date").tail(252)
    if history.empty:
        return price_level_missing()
    closes = history["close_numeric"].astype(float)
    close = float(closes.iloc[-1])
    low = float(closes.min())
    high = float(closes.max())
    median = float(closes.median())
    mean = float(closes.mean())
    position = (close - low) / (high - low) * 100.0 if high > low else math.nan
    if math.isnan(position):
        bucket = "price_history_insufficient"
    elif position <= 25.0:
        bucket = "bottom_quartile_level"
    elif position <= 50.0:
        bucket = "low_level"
    elif position <= 75.0:
        bucket = "mid_level"
    else:
        bucket = "high_level"
    return {
        "lookback_observed_days": len(history),
        "price_position_252_pct": metric_text(position),
        "below_252_median": bool_text(close <= median),
        "below_252_mean": bool_text(close <= mean),
        "price_level_bucket": bucket,
    }


def price_level_missing() -> dict[str, Any]:
    return {
        "lookback_observed_days": 0,
        "price_position_252_pct": "",
        "below_252_median": "false",
        "below_252_mean": "false",
        "price_level_bucket": "price_history_insufficient",
    }


def build_detail(generated_at: str) -> pd.DataFrame:
    baseline = comparable_events(read_csv(BASELINE_EVENTS_CSV), BASELINE_EVENT_SET_ID)
    variant = comparable_events(read_csv(VARIANT_EVENTS_CSV), VARIANT_EVENT_SET_ID)
    baseline_keys = event_key_map(baseline)
    variant_keys = event_key_map(variant)
    taxonomy = load_taxonomy()
    rows: list[dict[str, Any]] = []

    for _, event in pd.concat([baseline, variant], ignore_index=True).iterrows():
        stock_id = normalize_code(event.get("stock_id"))
        signal_date = normalize_date(event.get("signal_date"))
        key = (stock_id, signal_date)
        if key in baseline_keys and key in variant_keys:
            comparison_status = "common"
        elif event.get("event_set_id") == VARIANT_EVENT_SET_ID:
            comparison_status = "variant_only"
        else:
            comparison_status = "baseline_only"

        price_level = price_level_for(stock_id, signal_date)
        path_metrics = build_path_metrics(event)
        taxonomy_row = taxonomy.get(
            stock_id,
            {
                "effective_mainstream_label": "taxonomy_missing",
                "has_hot_theme": "false",
                "structural_theme_bucket": "taxonomy_missing",
                "primary_theme": "",
                "taxonomy_source": "stock_theme_taxonomy_latest_missing",
                "taxonomy_confidence": "pending_review",
            },
        )
        row = {
            "model_id": MODEL_ID,
            "confirmation_model_id": CONFIRMATION_MODEL_ID,
            "overlay_model_id": OVERLAY_MODEL_ID,
            "research_id": RESEARCH_ID,
            "source_research_id": SOURCE_RESEARCH_ID,
            "research_variant_id": RESEARCH_VARIANT_ID,
            "parameter_set_id": PARAMETER_SET_ID,
            "advisory_status": RESEARCH_VARIANT_ID,
            "event_set_id": safe_str(event.get("event_set_id")),
            "comparison_status": comparison_status,
            "sample_mode": safe_str(event.get("sample_mode")),
            "symmetry_ratio": PRIMARY_SYMMETRY_RATIO,
            "stock_id": stock_id,
            "stock_name": safe_str(event.get("stock_name")),
            "signal_date": signal_date,
            "left_peak_date": normalize_date(event.get("left_peak_date")),
            "left_low_date": normalize_date(event.get("left_low_date")),
            "neckline_date": normalize_date(event.get("neckline_date")),
            "right_low_date": normalize_date(event.get("right_low_date")),
            "breakout_date": normalize_date(event.get("breakout_date")),
            "post_confirmation_trigger_id": safe_str(event.get("post_confirmation_trigger_id")),
            "post_confirmation_date": normalize_date(event.get("post_confirmation_date")),
            "signal_close": safe_str(event.get("signal_close")),
            "neckline_price": safe_str(event.get("neckline_price")),
            "second_arc_volume_ratio": safe_str(event.get("second_arc_volume_ratio")),
            "has_neckline_breakout": bool_text(normalize_date(event.get("breakout_date")) != ""),
            "late_breakout_not_w": bool_text(bool_value(event.get("late_breakout_not_w"))),
            "has_post_confirmation": bool_text(safe_str(event.get("post_confirmation_trigger_id")) != ""),
            "a_mature": bool_text(bool_value(event.get("a_mature"))),
            "a_return_pct": safe_str(event.get("a_return_pct")),
            "c_mature": bool_text(bool_value(event.get("c_mature"))),
            "c_return_pct": safe_str(event.get("c_return_pct")),
            "tdcc_any_age7": bool_text(bool_value(event.get("tdcc_any_age7"))),
            "tdcc_any_age14": bool_text(bool_value(event.get("tdcc_any_age14"))),
            "tdcc_top50_age7": bool_text(bool_value(event.get("tdcc_top50_age7"))),
            "tdcc_top20_age7": bool_text(bool_value(event.get("tdcc_top20_age7"))),
            "tdcc_weekly_top20_age7": bool_text(bool_value(event.get("tdcc_weekly_top20_age7"))),
            "tdcc_consecutive_top20_age7": bool_text(bool_value(event.get("tdcc_consecutive_top20_age7"))),
            "slope_curvature_category": safe_str(path_metrics.get("slope_curvature_category")),
            "slope_issue_reasons": safe_str(path_metrics.get("slope_issue_reasons")),
            "revenue_catalyst_feature_status": REVENUE_CATALYST_STATUS,
            "manual_review_status": "pending_user_model_review",
            "approved_for_daily": "false",
            "production_readiness": PRODUCTION_READINESS,
            "generated_at": generated_at,
        }
        row.update(price_level)
        row.update(taxonomy_row)
        rows.append(row)

    detail = pd.DataFrame(rows)
    for column in DETAIL_COLUMNS:
        if column not in detail.columns:
            detail[column] = ""
    forbidden = sorted(set(detail.columns) & FORBIDDEN_PRODUCTION_FIELDS)
    if forbidden:
        raise SystemExit(f"ERROR: forbidden production columns in combined detail: {forbidden}")
    return detail[DETAIL_COLUMNS]


def condition_specs() -> list[tuple[str, str, Callable[[pd.DataFrame], pd.Series]]]:
    return [
        ("all_dedup_signals", "All deduplicated W-bottom event signals.", lambda df: pd.Series(True, index=df.index)),
        ("price_position_le_40", "Signal close is in the lower 40% of the 252-day low/high range.", lambda df: num(df["price_position_252_pct"]).le(40.0)),
        ("bottom_quartile_level", "Signal close is in the bottom quartile of the 252-day low/high range.", lambda df: df["price_level_bucket"].eq("bottom_quartile_level")),
        ("bottom_or_low_level", "Signal close is bottom-quartile or low-level.", lambda df: df["price_level_bucket"].isin(["bottom_quartile_level", "low_level"])),
        ("core_mainstream", "Taxonomy segment is core_mainstream.", lambda df: df["effective_mainstream_label"].eq("core_mainstream")),
        ("non_mainstream", "Taxonomy segment is non_mainstream.", lambda df: df["effective_mainstream_label"].eq("non_mainstream")),
        ("hot_theme", "Current taxonomy marks the stock as hot-theme.", lambda df: df["has_hot_theme"].map(bool_value)),
        ("core_mainstream_price_le_40", "Core-mainstream plus price_position_252_pct <= 40.", lambda df: df["effective_mainstream_label"].eq("core_mainstream") & num(df["price_position_252_pct"]).le(40.0)),
        ("hot_theme_price_le_40", "Hot-theme plus price_position_252_pct <= 40.", lambda df: df["has_hot_theme"].map(bool_value) & num(df["price_position_252_pct"]).le(40.0)),
        ("exclude_wv_multiple_turn", "Exclude WV/WVV multiple-turn path category.", lambda df: ~df["slope_curvature_category"].eq("wv_multiple_turn_risk")),
        ("price_le40_exclude_wv", "price_position_252_pct <= 40 and exclude WV/WVV.", lambda df: num(df["price_position_252_pct"]).le(40.0) & ~df["slope_curvature_category"].eq("wv_multiple_turn_risk")),
        ("core_mainstream_price_le40_exclude_wv", "Core-mainstream, price_position_252_pct <= 40, exclude WV/WVV.", lambda df: df["effective_mainstream_label"].eq("core_mainstream") & num(df["price_position_252_pct"]).le(40.0) & ~df["slope_curvature_category"].eq("wv_multiple_turn_risk")),
        ("has_neckline_breakout", "Only rows with later neckline breakout.", lambda df: df["has_neckline_breakout"].map(bool_value)),
        ("has_neckline_breakout_price_le40", "Neckline breakout plus price_position_252_pct <= 40.", lambda df: df["has_neckline_breakout"].map(bool_value) & num(df["price_position_252_pct"]).le(40.0)),
        ("has_neckline_breakout_bottom_or_low", "Neckline breakout plus bottom-or-low level.", lambda df: df["has_neckline_breakout"].map(bool_value) & df["price_level_bucket"].isin(["bottom_quartile_level", "low_level"])),
        ("has_neckline_breakout_core_mainstream", "Neckline breakout plus core-mainstream.", lambda df: df["has_neckline_breakout"].map(bool_value) & df["effective_mainstream_label"].eq("core_mainstream")),
        ("has_neckline_breakout_core_mainstream_price_le40", "Neckline breakout, core-mainstream, price_position_252_pct <= 40.", lambda df: df["has_neckline_breakout"].map(bool_value) & df["effective_mainstream_label"].eq("core_mainstream") & num(df["price_position_252_pct"]).le(40.0)),
        ("has_neckline_breakout_price_le40_exclude_wv", "Neckline breakout, price_position_252_pct <= 40, exclude WV/WVV.", lambda df: df["has_neckline_breakout"].map(bool_value) & num(df["price_position_252_pct"]).le(40.0) & ~df["slope_curvature_category"].eq("wv_multiple_turn_risk")),
        ("has_post_confirmation", "Only rows with post-confirmation trigger.", lambda df: df["has_post_confirmation"].map(bool_value)),
        ("has_post_confirmation_price_le40", "Post-confirmation trigger plus price_position_252_pct <= 40.", lambda df: df["has_post_confirmation"].map(bool_value) & num(df["price_position_252_pct"]).le(40.0)),
        ("has_neckline_breakout_tdcc_any_age7", "Neckline breakout plus TDCC age<=7 match.", lambda df: df["has_neckline_breakout"].map(bool_value) & df["tdcc_any_age7"].map(bool_value)),
        ("has_neckline_breakout_tdcc_any_age14", "Neckline breakout plus TDCC age<=14 match.", lambda df: df["has_neckline_breakout"].map(bool_value) & df["tdcc_any_age14"].map(bool_value)),
        ("has_neckline_breakout_core_mainstream_price_le40_tdcc_any_age7", "Neckline breakout, core-mainstream, price_position_252_pct <= 40, TDCC age<=7.", lambda df: df["has_neckline_breakout"].map(bool_value) & df["effective_mainstream_label"].eq("core_mainstream") & num(df["price_position_252_pct"]).le(40.0) & df["tdcc_any_age7"].map(bool_value)),
    ]


def num(series: pd.Series) -> pd.Series:
    return pd.to_numeric(series, errors="coerce")


def metrics(sample: pd.DataFrame, entry_timing_id: str) -> dict[str, Any]:
    mature_col = "a_mature" if entry_timing_id == "a_next_open_after_neckline_breakout" else "c_mature"
    return_col = "a_return_pct" if entry_timing_id == "a_next_open_after_neckline_breakout" else "c_return_pct"
    mature = sample[sample[mature_col].map(bool_value)].copy() if not sample.empty else pd.DataFrame()
    returns = pd.to_numeric(mature[return_col], errors="coerce").dropna() if not mature.empty else pd.Series(dtype=float)
    positions = num(sample["price_position_252_pct"]).dropna() if not sample.empty else pd.Series(dtype=float)
    category_counts = sample["slope_curvature_category"].value_counts().to_dict() if not sample.empty else {}
    level_counts = sample["price_level_bucket"].value_counts().to_dict() if not sample.empty else {}
    sample_size = int(len(sample))
    mature_size = int(len(returns))
    wins = int(returns.gt(0).sum()) if mature_size else 0
    return {
        "sample_size": sample_size,
        "mature_sample_size": mature_size,
        "win_count": wins,
        "win_rate_pct_num": wins / mature_size * 100.0 if mature_size else math.nan,
        "avg_return_pct_num": float(returns.mean()) if mature_size else math.nan,
        "median_return_pct_num": float(returns.median()) if mature_size else math.nan,
        "breakout_signal_count": int(sample["has_neckline_breakout"].map(bool_value).sum()) if sample_size else 0,
        "post_confirmation_count": int(sample["has_post_confirmation"].map(bool_value).sum()) if sample_size else 0,
        "tdcc_any_age7_count": int(sample["tdcc_any_age7"].map(bool_value).sum()) if sample_size else 0,
        "tdcc_any_age14_count": int(sample["tdcc_any_age14"].map(bool_value).sum()) if sample_size else 0,
        "core_mainstream_count": int(sample["effective_mainstream_label"].eq("core_mainstream").sum()) if sample_size else 0,
        "hot_theme_count": int(sample["has_hot_theme"].map(bool_value).sum()) if sample_size else 0,
        "bottom_quartile_count": int(level_counts.get("bottom_quartile_level", 0)),
        "low_level_count": int(level_counts.get("low_level", 0)),
        "mid_level_count": int(level_counts.get("mid_level", 0)),
        "high_level_count": int(level_counts.get("high_level", 0)),
        "wv_multiple_turn_count": int(category_counts.get("wv_multiple_turn_risk", 0)),
        "sharp_v_count": int(category_counts.get("sharp_v_bottom_risk", 0)),
        "slope_break_count": int(category_counts.get("slope_break_discontinuous", 0)),
        "smooth_count": int(category_counts.get("smooth_rounded_w_like", 0)),
        "avg_price_position_252_pct_num": float(positions.mean()) if len(positions) else math.nan,
        "median_price_position_252_pct_num": float(positions.median()) if len(positions) else math.nan,
    }


def sample_warning(mature_sample_size: int) -> str:
    if mature_sample_size < 5:
        return "tiny_mature_sample_research_only"
    if mature_sample_size < 15:
        return "low_mature_sample_research_only"
    if mature_sample_size < 30:
        return "directional_only_below_promotion_review_size"
    return "medium_mature_sample_research_only"


def interpretation(row_metrics: dict[str, Any], baseline_metrics: dict[str, Any], event_set_id: str) -> str:
    if row_metrics["mature_sample_size"] < 5:
        return "too_small_for_directional_read"
    if event_set_id == BASELINE_EVENT_SET_ID:
        return "baseline_reference"
    win_delta = row_metrics["win_rate_pct_num"] - baseline_metrics["win_rate_pct_num"]
    avg_delta = row_metrics["avg_return_pct_num"] - baseline_metrics["avg_return_pct_num"]
    if math.isnan(win_delta) or math.isnan(avg_delta):
        return "insufficient_baseline_comparison"
    if win_delta > 0 and avg_delta > 0:
        return "directionally_better_than_baseline_same_condition"
    if win_delta > 0 or avg_delta > 0:
        return "mixed_vs_baseline_same_condition"
    return "not_better_than_baseline_same_condition"


def grid_row(
    *,
    event_set_id: str,
    entry_timing_id: str,
    condition_set_id: str,
    condition_set_description: str,
    row_metrics: dict[str, Any],
    baseline_metrics: dict[str, Any],
    generated_at: str,
) -> dict[str, Any]:
    baseline_sample = baseline_metrics["sample_size"]
    row_sample = row_metrics["sample_size"]
    win_delta = row_metrics["win_rate_pct_num"] - baseline_metrics["win_rate_pct_num"]
    avg_delta = row_metrics["avg_return_pct_num"] - baseline_metrics["avg_return_pct_num"]
    median_delta = row_metrics["median_return_pct_num"] - baseline_metrics["median_return_pct_num"]
    return {
        "model_id": MODEL_ID,
        "confirmation_model_id": CONFIRMATION_MODEL_ID,
        "overlay_model_id": OVERLAY_MODEL_ID,
        "research_id": RESEARCH_ID,
        "source_research_id": SOURCE_RESEARCH_ID,
        "research_variant_id": RESEARCH_VARIANT_ID,
        "parameter_set_id": PARAMETER_SET_ID,
        "advisory_status": RESEARCH_VARIANT_ID,
        "event_set_id": event_set_id,
        "entry_timing_id": entry_timing_id,
        "condition_set_id": condition_set_id,
        "condition_set_description": condition_set_description,
        "sample_size": row_metrics["sample_size"],
        "mature_sample_size": row_metrics["mature_sample_size"],
        "win_count": row_metrics["win_count"],
        "win_rate_pct": metric_text(row_metrics["win_rate_pct_num"]),
        "avg_return_pct": metric_text(row_metrics["avg_return_pct_num"]),
        "median_return_pct": metric_text(row_metrics["median_return_pct_num"]),
        "baseline_sample_size": baseline_metrics["sample_size"],
        "baseline_mature_sample_size": baseline_metrics["mature_sample_size"],
        "baseline_win_rate_pct": metric_text(baseline_metrics["win_rate_pct_num"]),
        "baseline_avg_return_pct": metric_text(baseline_metrics["avg_return_pct_num"]),
        "baseline_median_return_pct": metric_text(baseline_metrics["median_return_pct_num"]),
        "delta_sample_size_vs_baseline": row_metrics["sample_size"] - baseline_metrics["sample_size"],
        "delta_mature_sample_size_vs_baseline": row_metrics["mature_sample_size"] - baseline_metrics["mature_sample_size"],
        "sample_retention_rate_pct": metric_text(row_sample / baseline_sample * 100.0 if baseline_sample else math.nan),
        "delta_win_rate_pct_vs_baseline": metric_text(win_delta),
        "delta_avg_return_pct_vs_baseline": metric_text(avg_delta),
        "delta_median_return_pct_vs_baseline": metric_text(median_delta),
        "breakout_signal_count": row_metrics["breakout_signal_count"],
        "post_confirmation_count": row_metrics["post_confirmation_count"],
        "tdcc_any_age7_count": row_metrics["tdcc_any_age7_count"],
        "tdcc_any_age14_count": row_metrics["tdcc_any_age14_count"],
        "core_mainstream_count": row_metrics["core_mainstream_count"],
        "hot_theme_count": row_metrics["hot_theme_count"],
        "bottom_quartile_count": row_metrics["bottom_quartile_count"],
        "low_level_count": row_metrics["low_level_count"],
        "mid_level_count": row_metrics["mid_level_count"],
        "high_level_count": row_metrics["high_level_count"],
        "wv_multiple_turn_count": row_metrics["wv_multiple_turn_count"],
        "sharp_v_count": row_metrics["sharp_v_count"],
        "slope_break_count": row_metrics["slope_break_count"],
        "smooth_count": row_metrics["smooth_count"],
        "avg_price_position_252_pct": metric_text(row_metrics["avg_price_position_252_pct_num"]),
        "median_price_position_252_pct": metric_text(row_metrics["median_price_position_252_pct_num"]),
        "sample_warning": sample_warning(row_metrics["mature_sample_size"]),
        "research_interpretation": interpretation(row_metrics, baseline_metrics, event_set_id),
        "revenue_catalyst_feature_status": REVENUE_CATALYST_STATUS,
        "approved_for_daily": "false",
        "production_readiness": PRODUCTION_READINESS,
        "generated_at": generated_at,
    }


def build_grid(detail: pd.DataFrame, generated_at: str) -> pd.DataFrame:
    rows: list[dict[str, Any]] = []
    for entry_timing_id in ["a_next_open_after_neckline_breakout", "c_post_confirmation"]:
        for condition_id, description, condition in condition_specs():
            baseline_sample = detail[detail["event_set_id"].eq(BASELINE_EVENT_SET_ID)].copy()
            baseline_subset = baseline_sample[condition(baseline_sample)].copy()
            baseline_metrics = metrics(baseline_subset, entry_timing_id)
            for event_set_id in [BASELINE_EVENT_SET_ID, VARIANT_EVENT_SET_ID]:
                sample = detail[detail["event_set_id"].eq(event_set_id)].copy()
                subset = sample[condition(sample)].copy()
                rows.append(
                    grid_row(
                        event_set_id=event_set_id,
                        entry_timing_id=entry_timing_id,
                        condition_set_id=condition_id,
                        condition_set_description=description,
                        row_metrics=metrics(subset, entry_timing_id),
                        baseline_metrics=baseline_metrics,
                        generated_at=generated_at,
                    )
                )
    grid = pd.DataFrame(rows, columns=GRID_COLUMNS)
    forbidden = sorted(set(grid.columns) & FORBIDDEN_PRODUCTION_FIELDS)
    if forbidden:
        raise SystemExit(f"ERROR: forbidden production columns in combined grid: {forbidden}")
    return grid


def markdown_table(df: pd.DataFrame, columns: list[str], limit: int = 20) -> list[str]:
    if df.empty:
        return ["_No rows._"]
    rows = ["| " + " | ".join(columns) + " |", "| " + " | ".join(["---"] * len(columns)) + " |"]
    for _, row in df.head(limit).iterrows():
        rows.append("| " + " | ".join(safe_str(row.get(column)) for column in columns) + " |")
    return rows


def write_markdown(grid: pd.DataFrame, detail: pd.DataFrame, generated_at: str) -> None:
    variant_a = grid[
        grid["event_set_id"].eq(VARIANT_EVENT_SET_ID)
        & grid["entry_timing_id"].eq("a_next_open_after_neckline_breakout")
        & pd.to_numeric(grid["mature_sample_size"], errors="coerce").ge(5)
    ].copy()
    variant_a["win_rate_sort"] = pd.to_numeric(variant_a["win_rate_pct"], errors="coerce")
    variant_a["avg_return_sort"] = pd.to_numeric(variant_a["avg_return_pct"], errors="coerce")
    variant_a["mature_sort"] = pd.to_numeric(variant_a["mature_sample_size"], errors="coerce")
    top_variant_a = variant_a.sort_values(["win_rate_sort", "avg_return_sort", "mature_sort"], ascending=[False, False, False])

    event_set_counts = (
        detail.groupby(["event_set_id", "comparison_status"], dropna=False)
        .size()
        .reset_index(name="count")
        .sort_values(["event_set_id", "comparison_status"])
    )
    level_counts = (
        detail.groupby(["event_set_id", "price_level_bucket"], dropna=False)
        .size()
        .reset_index(name="count")
        .sort_values(["event_set_id", "price_level_bucket"])
    )

    lines = [
        "# W-Bottom Combined Condition Backtest",
        "",
        f"- generated_at: `{generated_at}`",
        f"- source_research_id: `{SOURCE_RESEARCH_ID}`",
        f"- baseline_event_set: `{BASELINE_EVENT_SET_ID}`",
        f"- variant_event_set: `{VARIANT_EVENT_SET_ID}`",
        "- production impact: `none`",
        f"- revenue/catalyst feature status: `{REVENUE_CATALYST_STATUS}`",
        "- note: revenue/catalyst current daily artifacts are not joined because they are not historical signal-date features in this research packet.",
        "",
        "## Event Set Counts",
        "",
        *markdown_table(event_set_counts, ["event_set_id", "comparison_status", "count"], limit=20),
        "",
        "## Price-Level Counts",
        "",
        *markdown_table(level_counts, ["event_set_id", "price_level_bucket", "count"], limit=20),
        "",
        "## Top Variant A-Path Condition Rows",
        "",
        *markdown_table(
            top_variant_a,
            [
                "condition_set_id",
                "sample_size",
                "mature_sample_size",
                "win_rate_pct",
                "avg_return_pct",
                "median_return_pct",
                "delta_win_rate_pct_vs_baseline",
                "delta_avg_return_pct_vs_baseline",
                "sample_warning",
                "research_interpretation",
            ],
            limit=25,
        ),
        "",
        "## Guardrails",
        "",
        "- This is a research/backtest grid, not a production model change.",
        "- All rows remain `approved_for_daily=false` and `warning_research_variant_only`.",
        "- A higher win rate is not enough for promotion without sample size, average return, median return, and stability review.",
        "- TDCC rows are very small in this sample and should be treated as directional only.",
        "- Taxonomy is used as a read-only segment label, not as historical proof of theme state at the signal date.",
    ]
    LATEST_MD.parent.mkdir(parents=True, exist_ok=True)
    LATEST_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    generated_at = now_text()
    detail = build_detail(generated_at)
    grid = build_grid(detail, generated_at)
    if len(detail) != 842:
        raise SystemExit(f"ERROR: expected 842 combined detail rows, got {len(detail)}")
    if len(grid) != len(condition_specs()) * 2 * 2:
        raise SystemExit(f"ERROR: unexpected grid row count: {len(grid)}")
    write_csv(detail, LATEST_DETAIL_CSV)
    write_csv(detail, HISTORY_DETAIL_CSV)
    write_csv(grid, LATEST_GRID_CSV)
    write_csv(grid, HISTORY_GRID_CSV)
    write_markdown(grid, detail, generated_at)
    print(f"Saved: {LATEST_DETAIL_CSV} rows={len(detail)}")
    print(f"Saved: {LATEST_GRID_CSV} rows={len(grid)}")
    print(f"Saved: {LATEST_MD}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
