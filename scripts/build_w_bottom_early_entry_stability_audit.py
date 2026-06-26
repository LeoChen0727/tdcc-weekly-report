from __future__ import annotations

from datetime import datetime
from pathlib import Path
from typing import Any, Callable
from zoneinfo import ZoneInfo
import math

import pandas as pd


ROOT = Path(".")
RESEARCH_LATEST_DIR = ROOT / "output" / "latest" / "research_backtest"
RESEARCH_HISTORY_DIR = ROOT / "output" / "history" / "research"

SOURCE_DETAIL_CSV = RESEARCH_LATEST_DIR / "w_bottom_early_entry_parameter_grid_detail_latest.csv"
MARKET_INDEX_HISTORY_CSV = ROOT / "data" / "market_index_history.csv"
LATEST_CSV = RESEARCH_LATEST_DIR / "w_bottom_early_entry_stability_audit_latest.csv"
LATEST_MD = RESEARCH_LATEST_DIR / "w_bottom_early_entry_stability_audit_latest.md"
HISTORY_CSV = RESEARCH_HISTORY_DIR / "w_bottom_early_entry_stability_audit.csv"

MODEL_ID = "w_bottom_right_side"
CONFIRMATION_MODEL_ID = "neckline_volume_breakout_confirmation"
OVERLAY_MODEL_ID = "tdcc_weekly_ranking_formula"
RESEARCH_ID = "w_bottom_early_entry_stability_audit"
SOURCE_RESEARCH_ID = "w_bottom_early_entry_parameter_grid"
RESEARCH_VARIANT_ID = "warning_research_variant_only"
PRODUCTION_READINESS = "not_production_ready_research_only"
SURFACE_ID = "w_bottom_right_low_early_entry"
EVENT_SET_ID = "variant_nearest_micro_45d_event_replay"
BASELINE_SEGMENT_ID = "all_rows"
TARGET_OUTCOME_RULES = [
    "take_profit_10pct_close_40d",
    "tp10_or_neutral_after_5pct_close_40d",
]
STRICT_SEGMENTS = [
    "smooth_right_rebound_5_20",
    "smooth_price_le40_right_rebound_5_20",
    "smooth_core_mainstream_right_rebound_5_20",
    "smooth_core_mainstream_price_le40_right_rebound_5_20",
    "smooth_right_rebound_5_20_red_ratio_gt_first",
    "smooth_right_rebound_5_20_near_neckline",
    "price_le30_rebound_3_20_volume_red",
    "price_le30_rebound_5_20_volume_red",
    "price_le30_rebound_3_20_volume_red_below_neckline5",
    "bottom_or_low_rebound_3_20_volume_red_exclude_wv",
    "core_mainstream_price_le30_rebound_3_20_volume_red",
    "core_or_hot_price_le30_rebound_3_20_volume_red",
    "smooth_price_le30_rebound_3_20_volume_red",
    "smooth_price_le30_rebound_5_20_volume_red",
    "smooth_right_rebound_5_20_strong_bull",
    "smooth_right_rebound_5_20_bull",
    "smooth_right_rebound_5_20_not_correction",
    "smooth_core_mainstream_right_rebound_5_20_strong_bull",
    "smooth_core_mainstream_right_rebound_5_20_bull",
    "core_mainstream_price_le30_rebound_3_20_volume_red_bull",
    "core_mainstream_price_le30_rebound_3_20_volume_red_not_correction",
    "bottom_or_low_rebound_3_20_volume_red_exclude_wv_strong_bull",
]

FORBIDDEN_PRODUCTION_FIELDS = {
    "trade_decision",
    "action_rating",
    "entry_style",
    "position_sizing",
    "decision_score",
    "daily_candidate_decision",
    "buy_signal",
}

OUTPUT_COLUMNS = [
    "model_id",
    "confirmation_model_id",
    "overlay_model_id",
    "research_id",
    "source_research_id",
    "research_variant_id",
    "advisory_status",
    "surface_id",
    "event_set_id",
    "outcome_rule_id",
    "segment_id",
    "segment_description",
    "row_type",
    "period_type",
    "period_id",
    "period_start_date",
    "period_end_date",
    "period_count",
    "periods_with_evaluated_ge5",
    "periods_with_mature_ge5",
    "periods_with_mature_ge10",
    "sample_size",
    "evaluated_sample_size",
    "mature_sample_size",
    "win_count",
    "neutral_count",
    "loss_count",
    "incomplete_count",
    "win_rate_excl_neutral_pct",
    "neutral_rate_evaluated_pct",
    "incomplete_rate_pct",
    "avg_return_pct",
    "median_return_pct",
    "min_period_win_rate_pct",
    "max_period_win_rate_pct",
    "win_rate_range_pct",
    "min_period_win_rate_mature_ge5_pct",
    "max_period_win_rate_mature_ge5_pct",
    "win_rate_range_mature_ge5_pct",
    "min_period_win_rate_mature_ge10_pct",
    "max_period_win_rate_mature_ge10_pct",
    "win_rate_range_mature_ge10_pct",
    "stability_status",
    "mature_period_stability_status",
    "next_review_status",
    "sample_warning",
    "research_interpretation",
    "approved_for_daily",
    "production_readiness",
    "generated_at",
]


def now_text() -> str:
    return datetime.now(ZoneInfo("Asia/Taipei")).strftime("%Y-%m-%d %H:%M:%S Asia/Taipei")


def safe_str(value: Any) -> str:
    if value is None:
        return ""
    try:
        if pd.isna(value):
            return ""
    except Exception:
        pass
    text = str(value).replace("\ufeff", "").strip()
    if text.lower() in {"nan", "none", "nat", "<na>"}:
        return ""
    return text


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


def normalize_date(value: Any) -> str:
    text = safe_str(value)
    if text.endswith(".0"):
        text = text[:-2]
    digits = "".join(ch for ch in text if ch.isdigit())
    return digits[:8]


def num(series: pd.Series) -> pd.Series:
    return pd.to_numeric(series, errors="coerce")


def bool_value(value: Any) -> bool:
    return safe_str(value).lower() in {"true", "1", "yes", "y"}


def classify_index_regime(row: pd.Series) -> str:
    if row.empty:
        return "unknown"
    above_ma20 = bool_value(row.get("above_ma20"))
    above_ma60 = bool_value(row.get("above_ma60"))
    ret20 = pd.to_numeric(pd.Series([row.get("return_20d")]), errors="coerce").iloc[0]
    if above_ma20 and above_ma60 and not math.isnan(ret20) and ret20 >= 3.0:
        return "strong_bull"
    if above_ma20 and above_ma60:
        return "mild_bull"
    if not above_ma20 and not math.isnan(ret20) and ret20 <= -3.0:
        return "correction"
    return "range_or_mixed"


def combine_index_regimes(twse_regime: str, tpex_regime: str) -> str:
    regimes = {twse_regime, tpex_regime}
    if "correction" in regimes:
        return "correction"
    if regimes == {"strong_bull"}:
        return "strong_bull"
    if regimes <= {"strong_bull", "mild_bull"}:
        return "mild_bull"
    if regimes == {"unknown"}:
        return "unknown"
    return "range_or_mixed"


def load_market_regime_map() -> dict[str, str]:
    if not MARKET_INDEX_HISTORY_CSV.exists():
        return {}
    df = read_csv(MARKET_INDEX_HISTORY_CSV)
    required = {"date", "index_code", "above_ma20", "above_ma60", "return_20d"}
    if df.empty or not required.issubset(df.columns):
        return {}
    df = df.copy()
    df["date"] = df["date"].map(normalize_date)
    df["index_code"] = df["index_code"].map(safe_str)
    regimes: dict[str, str] = {}
    for date, group in df[df["date"].ne("")].groupby("date", dropna=False):
        twse_part = group[group["index_code"].eq("TWSE")]
        tpex_part = group[group["index_code"].eq("TPEX")]
        twse_regime = classify_index_regime(twse_part.iloc[-1]) if not twse_part.empty else "unknown"
        tpex_regime = classify_index_regime(tpex_part.iloc[-1]) if not tpex_part.empty else "unknown"
        regimes[safe_str(date)] = combine_index_regimes(twse_regime, tpex_regime)
    return regimes


def metric_series(sample: pd.DataFrame, column: str) -> pd.Series:
    if sample.empty or column not in sample.columns:
        return pd.Series(dtype=float)
    return pd.to_numeric(sample[column], errors="coerce").dropna()


def month_id(date_text: str) -> str:
    date_text = normalize_date(date_text)
    return f"{date_text[:4]}-{date_text[4:6]}" if len(date_text) >= 6 else ""


def quarter_id(date_text: str) -> str:
    date_text = normalize_date(date_text)
    if len(date_text) < 6:
        return ""
    month = int(date_text[4:6])
    quarter = (month - 1) // 3 + 1
    return f"{date_text[:4]}Q{quarter}"


def segment_specs() -> list[tuple[str, str, Callable[[pd.DataFrame], pd.Series]]]:
    price_le30 = lambda df: num(df["price_position_252_pct"]).le(30.0)
    rebound_3_20 = lambda df: num(df["signal_rebound_from_right_low_pct"]).between(3.0, 20.0, inclusive="both")
    rebound_5_20 = lambda df: num(df["signal_rebound_from_right_low_pct"]).between(5.0, 20.0, inclusive="both")
    volume_red = lambda df: num(df["second_arc_volume_ratio"]).ge(1.2) & num(df["red_ratio_delta_pct"]).gt(0.0)
    smooth = lambda df: df["slope_curvature_category"].eq("smooth_rounded_w_like")
    exclude_wv = lambda df: ~df["slope_curvature_category"].eq("wv_multiple_turn_risk")
    bottom_or_low = lambda df: df["price_level_bucket"].isin(["bottom_quartile_level", "low_level"])
    core_mainstream = lambda df: df["effective_mainstream_label"].eq("core_mainstream")
    core_or_hot = lambda df: df["effective_mainstream_label"].eq("core_mainstream") | df["has_hot_theme"].astype(str).str.lower().eq("true")
    below_neckline5 = lambda df: num(df["neckline_distance_pct"]).le(-5.0)
    strong_bull = lambda df: df["signal_market_regime"].eq("strong_bull")
    bull = lambda df: df["signal_market_regime"].isin(["strong_bull", "mild_bull"])
    not_correction = lambda df: df["signal_market_regime"].isin(["strong_bull", "mild_bull", "range_or_mixed"])
    return [
        (BASELINE_SEGMENT_ID, "All variant right-low early-entry rows.", lambda df: pd.Series(True, index=df.index)),
        ("smooth_right_rebound_5_20", "Smooth rounded W-like path and signal rebound 5% to 20%.", lambda df: df["slope_curvature_category"].eq("smooth_rounded_w_like") & num(df["signal_rebound_from_right_low_pct"]).between(5.0, 20.0, inclusive="both")),
        ("smooth_price_le40_right_rebound_5_20", "Smooth rounded W-like path, price_position_252_pct <= 40, and signal rebound 5% to 20%.", lambda df: df["slope_curvature_category"].eq("smooth_rounded_w_like") & num(df["price_position_252_pct"]).le(40.0) & num(df["signal_rebound_from_right_low_pct"]).between(5.0, 20.0, inclusive="both")),
        ("smooth_core_mainstream_right_rebound_5_20", "Smooth rounded W-like path, core_mainstream, and signal rebound 5% to 20%.", lambda df: df["slope_curvature_category"].eq("smooth_rounded_w_like") & df["effective_mainstream_label"].eq("core_mainstream") & num(df["signal_rebound_from_right_low_pct"]).between(5.0, 20.0, inclusive="both")),
        ("smooth_core_mainstream_price_le40_right_rebound_5_20", "Smooth rounded W-like path, core_mainstream, price_position_252_pct <= 40, and signal rebound 5% to 20%.", lambda df: df["slope_curvature_category"].eq("smooth_rounded_w_like") & df["effective_mainstream_label"].eq("core_mainstream") & num(df["price_position_252_pct"]).le(40.0) & num(df["signal_rebound_from_right_low_pct"]).between(5.0, 20.0, inclusive="both")),
        ("smooth_right_rebound_5_20_red_ratio_gt_first", "Smooth rounded W-like path, signal rebound 5% to 20%, and second arc red ratio > first arc.", lambda df: df["slope_curvature_category"].eq("smooth_rounded_w_like") & num(df["signal_rebound_from_right_low_pct"]).between(5.0, 20.0, inclusive="both") & num(df["red_ratio_delta_pct"]).gt(0.0)),
        ("smooth_right_rebound_5_20_near_neckline", "Smooth rounded W-like path, signal rebound 5% to 20%, and signal is within 5% below neckline.", lambda df: df["slope_curvature_category"].eq("smooth_rounded_w_like") & num(df["signal_rebound_from_right_low_pct"]).between(5.0, 20.0, inclusive="both") & num(df["neckline_distance_pct"]).between(-5.0, 0.0, inclusive="both")),
        ("price_le30_rebound_3_20_volume_red", "price_position_252_pct <= 30, signal rebound 3% to 20%, second arc volume >= 1.2x first arc, and second arc red ratio > first arc.", lambda df: price_le30(df) & rebound_3_20(df) & volume_red(df)),
        ("price_le30_rebound_5_20_volume_red", "price_position_252_pct <= 30, signal rebound 5% to 20%, second arc volume >= 1.2x first arc, and second arc red ratio > first arc.", lambda df: price_le30(df) & rebound_5_20(df) & volume_red(df)),
        ("price_le30_rebound_3_20_volume_red_below_neckline5", "price_position_252_pct <= 30, signal rebound 3% to 20%, second arc volume/red improvement, and signal remains at least 5% below neckline.", lambda df: price_le30(df) & rebound_3_20(df) & volume_red(df) & below_neckline5(df)),
        ("bottom_or_low_rebound_3_20_volume_red_exclude_wv", "Bottom/low price level, signal rebound 3% to 20%, second arc volume/red improvement, and excludes WV/WVV multiple-turn paths.", lambda df: bottom_or_low(df) & rebound_3_20(df) & volume_red(df) & exclude_wv(df)),
        ("core_mainstream_price_le30_rebound_3_20_volume_red", "core_mainstream, price_position_252_pct <= 30, signal rebound 3% to 20%, and second arc volume/red improvement.", lambda df: core_mainstream(df) & price_le30(df) & rebound_3_20(df) & volume_red(df)),
        ("core_or_hot_price_le30_rebound_3_20_volume_red", "core_mainstream or hot theme, price_position_252_pct <= 30, signal rebound 3% to 20%, and second arc volume/red improvement.", lambda df: core_or_hot(df) & price_le30(df) & rebound_3_20(df) & volume_red(df)),
        ("smooth_price_le30_rebound_3_20_volume_red", "Smooth rounded W-like path, price_position_252_pct <= 30, signal rebound 3% to 20%, and second arc volume/red improvement.", lambda df: smooth(df) & price_le30(df) & rebound_3_20(df) & volume_red(df)),
        ("smooth_price_le30_rebound_5_20_volume_red", "Smooth rounded W-like path, price_position_252_pct <= 30, signal rebound 5% to 20%, and second arc volume/red improvement.", lambda df: smooth(df) & price_le30(df) & rebound_5_20(df) & volume_red(df)),
        ("smooth_right_rebound_5_20_strong_bull", "Smooth rounded W-like path, signal rebound 5% to 20%, and signal date market regime is strong_bull.", lambda df: smooth(df) & rebound_5_20(df) & strong_bull(df)),
        ("smooth_right_rebound_5_20_bull", "Smooth rounded W-like path, signal rebound 5% to 20%, and signal date market regime is strong_bull or mild_bull.", lambda df: smooth(df) & rebound_5_20(df) & bull(df)),
        ("smooth_right_rebound_5_20_not_correction", "Smooth rounded W-like path, signal rebound 5% to 20%, and signal date market regime is known non-correction.", lambda df: smooth(df) & rebound_5_20(df) & not_correction(df)),
        ("smooth_core_mainstream_right_rebound_5_20_strong_bull", "Smooth rounded W-like path, core_mainstream, signal rebound 5% to 20%, and signal date market regime is strong_bull.", lambda df: smooth(df) & core_mainstream(df) & rebound_5_20(df) & strong_bull(df)),
        ("smooth_core_mainstream_right_rebound_5_20_bull", "Smooth rounded W-like path, core_mainstream, signal rebound 5% to 20%, and signal date market regime is strong_bull or mild_bull.", lambda df: smooth(df) & core_mainstream(df) & rebound_5_20(df) & bull(df)),
        ("core_mainstream_price_le30_rebound_3_20_volume_red_bull", "core_mainstream, price_position_252_pct <= 30, signal rebound 3% to 20%, second arc volume/red improvement, and signal date market regime is strong_bull or mild_bull.", lambda df: core_mainstream(df) & price_le30(df) & rebound_3_20(df) & volume_red(df) & bull(df)),
        ("core_mainstream_price_le30_rebound_3_20_volume_red_not_correction", "core_mainstream, price_position_252_pct <= 30, signal rebound 3% to 20%, second arc volume/red improvement, and signal date market regime is known non-correction.", lambda df: core_mainstream(df) & price_le30(df) & rebound_3_20(df) & volume_red(df) & not_correction(df)),
        ("bottom_or_low_rebound_3_20_volume_red_exclude_wv_strong_bull", "Bottom/low price level, signal rebound 3% to 20%, second arc volume/red improvement, excludes WV/WVV, and signal date market regime is strong_bull.", lambda df: bottom_or_low(df) & rebound_3_20(df) & volume_red(df) & exclude_wv(df) & strong_bull(df)),
    ]


def metrics(sample: pd.DataFrame) -> dict[str, Any]:
    sample_size = int(len(sample))
    win_count = int(sample["outcome_result"].eq("win").sum()) if sample_size else 0
    neutral_count = int(sample["outcome_result"].eq("neutral").sum()) if sample_size else 0
    loss_count = int(sample["outcome_result"].eq("loss").sum()) if sample_size else 0
    incomplete_count = int(sample["outcome_result"].eq("incomplete").sum()) if sample_size else 0
    mature_size = win_count + loss_count
    evaluated_size = win_count + neutral_count + loss_count
    evaluated = sample[sample["outcome_result"].isin(["win", "neutral", "loss"])].copy()
    returns = metric_series(evaluated, "return_pct")
    return {
        "sample_size": sample_size,
        "evaluated_sample_size": evaluated_size,
        "mature_sample_size": mature_size,
        "win_count": win_count,
        "neutral_count": neutral_count,
        "loss_count": loss_count,
        "incomplete_count": incomplete_count,
        "win_rate_num": win_count / mature_size * 100.0 if mature_size else math.nan,
        "neutral_rate_num": neutral_count / evaluated_size * 100.0 if evaluated_size else math.nan,
        "incomplete_rate_num": incomplete_count / sample_size * 100.0 if sample_size else math.nan,
        "avg_return_num": float(returns.mean()) if len(returns) else math.nan,
        "median_return_num": float(returns.median()) if len(returns) else math.nan,
    }


def sample_warning(metrics_row: dict[str, Any]) -> str:
    if metrics_row["evaluated_sample_size"] == 0:
        return "no_evaluated_sample_research_only"
    if metrics_row["mature_sample_size"] < 5:
        return "tiny_mature_sample_research_only"
    if metrics_row["mature_sample_size"] < 15:
        return "low_mature_sample_research_only"
    if metrics_row["mature_sample_size"] < 30:
        return "directional_only_below_promotion_review_size"
    return "medium_mature_sample_research_only"


def period_interpretation(metrics_row: dict[str, Any]) -> str:
    if metrics_row["sample_size"] == 0:
        return "empty_period"
    if metrics_row["incomplete_rate_num"] >= 50.0:
        return "future_window_incomplete"
    if metrics_row["mature_sample_size"] < 5:
        return "too_small_for_period_decision"
    if metrics_row["win_rate_num"] >= 55.0:
        return "directionally_positive_period"
    return "not_directionally_positive_period"


def summary_interpretation(period_rows: pd.DataFrame) -> str:
    if period_rows.empty:
        return "no_period_rows"
    mature_ge10 = int(pd.to_numeric(period_rows["mature_sample_size"], errors="coerce").ge(10).sum())
    mature_ge5 = int(pd.to_numeric(period_rows["mature_sample_size"], errors="coerce").ge(5).sum())
    win_range = pd.to_numeric(period_rows["win_rate_excl_neutral_pct"], errors="coerce").dropna()
    if mature_ge10 < 3:
        return "insufficient_period_coverage_for_promotion"
    if mature_ge5 < 4:
        return "insufficient_monthly_repetition"
    if not win_range.empty and float(win_range.max() - win_range.min()) > 25.0:
        return "unstable_period_win_rate"
    return "directionally_stable_research_only"


def row_float(row: dict[str, Any], column: str) -> float:
    try:
        value = float(safe_str(row.get(column)))
    except ValueError:
        return math.nan
    return value if not math.isnan(value) else math.nan


def row_int(row: dict[str, Any], column: str) -> int:
    try:
        return int(float(safe_str(row.get(column))))
    except ValueError:
        return 0


def mature_period_stability_status(row: dict[str, Any]) -> str:
    periods_ge10 = row_int(row, "periods_with_mature_ge10")
    periods_ge5 = row_int(row, "periods_with_mature_ge5")
    if periods_ge10 >= 6:
        win_range = row_float(row, "win_rate_range_mature_ge10_pct")
        min_win = row_float(row, "min_period_win_rate_mature_ge10_pct")
        if not math.isnan(win_range) and win_range <= 25.0 and not math.isnan(min_win) and min_win >= 40.0:
            return "mature_ge10_stability_candidate_research_only"
        return "mature_ge10_unstable_or_weak_research_only"
    if periods_ge5 >= 8:
        win_range = row_float(row, "win_rate_range_mature_ge5_pct")
        min_win = row_float(row, "min_period_win_rate_mature_ge5_pct")
        if not math.isnan(win_range) and win_range <= 25.0 and not math.isnan(min_win) and min_win >= 40.0:
            return "mature_ge5_stability_candidate_research_only"
        return "mature_ge5_unstable_or_weak_research_only"
    return "insufficient_mature_periods_research_only"


def next_review_status(row: dict[str, Any]) -> str:
    mature_sample = row_int(row, "mature_sample_size")
    win_rate = row_float(row, "win_rate_excl_neutral_pct")
    avg_return = row_float(row, "avg_return_pct")
    stability = safe_str(row.get("mature_period_stability_status"))
    if "stability_candidate" in stability and mature_sample >= 60 and win_rate >= 50.0 and avg_return > 0:
        return "candidate_for_next_research_filter_review"
    if mature_sample >= 60 and win_rate >= 50.0 and avg_return > 0:
        return "promising_but_period_stability_blocked"
    if "insufficient_mature_periods" in stability:
        return "blocked_by_insufficient_monthly_repetition"
    return "blocked_by_unstable_or_weak_monthly_result"


def base_row(
    *,
    outcome_rule_id: str,
    segment_id: str,
    segment_description: str,
    row_type: str,
    period_type: str,
    period_id: str,
    period_start_date: str,
    period_end_date: str,
    metrics_row: dict[str, Any],
    generated_at: str,
) -> dict[str, Any]:
    return {
        "model_id": MODEL_ID,
        "confirmation_model_id": CONFIRMATION_MODEL_ID,
        "overlay_model_id": OVERLAY_MODEL_ID,
        "research_id": RESEARCH_ID,
        "source_research_id": SOURCE_RESEARCH_ID,
        "research_variant_id": RESEARCH_VARIANT_ID,
        "advisory_status": RESEARCH_VARIANT_ID,
        "surface_id": SURFACE_ID,
        "event_set_id": EVENT_SET_ID,
        "outcome_rule_id": outcome_rule_id,
        "segment_id": segment_id,
        "segment_description": segment_description,
        "row_type": row_type,
        "period_type": period_type,
        "period_id": period_id,
        "period_start_date": period_start_date,
        "period_end_date": period_end_date,
        "period_count": "",
        "periods_with_evaluated_ge5": "",
        "periods_with_mature_ge5": "",
        "periods_with_mature_ge10": "",
        "sample_size": metrics_row["sample_size"],
        "evaluated_sample_size": metrics_row["evaluated_sample_size"],
        "mature_sample_size": metrics_row["mature_sample_size"],
        "win_count": metrics_row["win_count"],
        "neutral_count": metrics_row["neutral_count"],
        "loss_count": metrics_row["loss_count"],
        "incomplete_count": metrics_row["incomplete_count"],
        "win_rate_excl_neutral_pct": metric_text(metrics_row["win_rate_num"]),
        "neutral_rate_evaluated_pct": metric_text(metrics_row["neutral_rate_num"]),
        "incomplete_rate_pct": metric_text(metrics_row["incomplete_rate_num"]),
        "avg_return_pct": metric_text(metrics_row["avg_return_num"]),
        "median_return_pct": metric_text(metrics_row["median_return_num"]),
        "min_period_win_rate_pct": "",
        "max_period_win_rate_pct": "",
        "win_rate_range_pct": "",
        "min_period_win_rate_mature_ge5_pct": "",
        "max_period_win_rate_mature_ge5_pct": "",
        "win_rate_range_mature_ge5_pct": "",
        "min_period_win_rate_mature_ge10_pct": "",
        "max_period_win_rate_mature_ge10_pct": "",
        "win_rate_range_mature_ge10_pct": "",
        "stability_status": "",
        "mature_period_stability_status": "",
        "next_review_status": "",
        "sample_warning": sample_warning(metrics_row),
        "research_interpretation": period_interpretation(metrics_row),
        "approved_for_daily": "false",
        "production_readiness": PRODUCTION_READINESS,
        "generated_at": generated_at,
    }


def period_rows_for_group(
    *,
    group: pd.DataFrame,
    outcome_rule_id: str,
    segment_id: str,
    segment_description: str,
    period_type: str,
    period_column: str,
    generated_at: str,
) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for period_id, period_group in group.groupby(period_column, dropna=False):
        period_id = safe_str(period_id)
        if not period_id:
            continue
        dates = period_group["source_signal_date"].map(normalize_date)
        metrics_row = metrics(period_group)
        rows.append(
            base_row(
                outcome_rule_id=outcome_rule_id,
                segment_id=segment_id,
                segment_description=segment_description,
                row_type="period",
                period_type=period_type,
                period_id=period_id,
                period_start_date=str(dates.min()),
                period_end_date=str(dates.max()),
                metrics_row=metrics_row,
                generated_at=generated_at,
            )
        )
    return rows


def summary_row(
    *,
    all_rows: list[dict[str, Any]],
    outcome_rule_id: str,
    segment_id: str,
    segment_description: str,
    generated_at: str,
) -> dict[str, Any]:
    period_df = pd.DataFrame([row for row in all_rows if row["row_type"] == "period" and row["period_type"] == "month"])
    win_rate_values = pd.to_numeric(period_df["win_rate_excl_neutral_pct"], errors="coerce") if not period_df.empty else pd.Series(dtype=float)
    mature_values = pd.to_numeric(period_df["mature_sample_size"], errors="coerce") if not period_df.empty else pd.Series(dtype=float)
    win_rates = win_rate_values.dropna()
    win_rates_ge5 = win_rate_values[mature_values.ge(5)].dropna() if not period_df.empty else pd.Series(dtype=float)
    win_rates_ge10 = win_rate_values[mature_values.ge(10)].dropna() if not period_df.empty else pd.Series(dtype=float)
    aggregate_metrics = {
        "sample_size": int(pd.to_numeric(period_df["sample_size"], errors="coerce").sum()) if not period_df.empty else 0,
        "evaluated_sample_size": int(pd.to_numeric(period_df["evaluated_sample_size"], errors="coerce").sum()) if not period_df.empty else 0,
        "mature_sample_size": int(pd.to_numeric(period_df["mature_sample_size"], errors="coerce").sum()) if not period_df.empty else 0,
        "win_count": int(pd.to_numeric(period_df["win_count"], errors="coerce").sum()) if not period_df.empty else 0,
        "neutral_count": int(pd.to_numeric(period_df["neutral_count"], errors="coerce").sum()) if not period_df.empty else 0,
        "loss_count": int(pd.to_numeric(period_df["loss_count"], errors="coerce").sum()) if not period_df.empty else 0,
        "incomplete_count": int(pd.to_numeric(period_df["incomplete_count"], errors="coerce").sum()) if not period_df.empty else 0,
        "win_rate_num": math.nan,
        "neutral_rate_num": math.nan,
        "incomplete_rate_num": math.nan,
        "avg_return_num": math.nan,
        "median_return_num": math.nan,
    }
    mature = aggregate_metrics["win_count"] + aggregate_metrics["loss_count"]
    evaluated = aggregate_metrics["win_count"] + aggregate_metrics["neutral_count"] + aggregate_metrics["loss_count"]
    sample_size = aggregate_metrics["sample_size"]
    aggregate_metrics["win_rate_num"] = aggregate_metrics["win_count"] / mature * 100.0 if mature else math.nan
    aggregate_metrics["neutral_rate_num"] = aggregate_metrics["neutral_count"] / evaluated * 100.0 if evaluated else math.nan
    aggregate_metrics["incomplete_rate_num"] = aggregate_metrics["incomplete_count"] / sample_size * 100.0 if sample_size else math.nan
    if not period_df.empty:
        avg_returns = pd.to_numeric(period_df["avg_return_pct"], errors="coerce")
        avg_weights = pd.to_numeric(period_df["evaluated_sample_size"], errors="coerce")
        weighted = avg_returns.notna() & avg_weights.gt(0)
        if weighted.any():
            aggregate_metrics["avg_return_num"] = float((avg_returns[weighted] * avg_weights[weighted]).sum() / avg_weights[weighted].sum())
    row = base_row(
        outcome_rule_id=outcome_rule_id,
        segment_id=segment_id,
        segment_description=segment_description,
        row_type="summary",
        period_type="month",
        period_id="monthly_rollup",
        period_start_date=str(period_df["period_start_date"].min()) if not period_df.empty else "",
        period_end_date=str(period_df["period_end_date"].max()) if not period_df.empty else "",
        metrics_row=aggregate_metrics,
        generated_at=generated_at,
    )
    row["period_count"] = str(len(period_df))
    row["periods_with_evaluated_ge5"] = str(int(pd.to_numeric(period_df["evaluated_sample_size"], errors="coerce").ge(5).sum())) if not period_df.empty else "0"
    row["periods_with_mature_ge5"] = str(int(pd.to_numeric(period_df["mature_sample_size"], errors="coerce").ge(5).sum())) if not period_df.empty else "0"
    row["periods_with_mature_ge10"] = str(int(pd.to_numeric(period_df["mature_sample_size"], errors="coerce").ge(10).sum())) if not period_df.empty else "0"
    row["min_period_win_rate_pct"] = metric_text(float(win_rates.min())) if not win_rates.empty else ""
    row["max_period_win_rate_pct"] = metric_text(float(win_rates.max())) if not win_rates.empty else ""
    row["win_rate_range_pct"] = metric_text(float(win_rates.max() - win_rates.min())) if not win_rates.empty else ""
    row["min_period_win_rate_mature_ge5_pct"] = metric_text(float(win_rates_ge5.min())) if not win_rates_ge5.empty else ""
    row["max_period_win_rate_mature_ge5_pct"] = metric_text(float(win_rates_ge5.max())) if not win_rates_ge5.empty else ""
    row["win_rate_range_mature_ge5_pct"] = metric_text(float(win_rates_ge5.max() - win_rates_ge5.min())) if not win_rates_ge5.empty else ""
    row["min_period_win_rate_mature_ge10_pct"] = metric_text(float(win_rates_ge10.min())) if not win_rates_ge10.empty else ""
    row["max_period_win_rate_mature_ge10_pct"] = metric_text(float(win_rates_ge10.max())) if not win_rates_ge10.empty else ""
    row["win_rate_range_mature_ge10_pct"] = metric_text(float(win_rates_ge10.max() - win_rates_ge10.min())) if not win_rates_ge10.empty else ""
    row["stability_status"] = summary_interpretation(period_df)
    row["mature_period_stability_status"] = mature_period_stability_status(row)
    row["next_review_status"] = next_review_status(row)
    row["research_interpretation"] = row["stability_status"]
    return row


def build_audit(generated_at: str) -> pd.DataFrame:
    source = read_csv(SOURCE_DETAIL_CSV)
    required = {
        "event_set_id",
        "outcome_rule_id",
        "source_signal_date",
        "outcome_result",
        "return_pct",
        "signal_rebound_from_right_low_pct",
        "slope_curvature_category",
        "effective_mainstream_label",
        "has_hot_theme",
        "price_level_bucket",
        "second_arc_volume_ratio",
        "price_position_252_pct",
        "second_low_gap_pct",
        "red_ratio_delta_pct",
        "neckline_distance_pct",
        "approved_for_daily",
        "production_readiness",
    }
    missing = sorted(required - set(source.columns))
    if missing:
        raise SystemExit(f"ERROR: source detail missing columns: {missing}")

    detail = source[
        source["event_set_id"].eq(EVENT_SET_ID)
        & source["outcome_rule_id"].isin(TARGET_OUTCOME_RULES)
    ].copy()
    detail["source_signal_date"] = detail["source_signal_date"].map(normalize_date)
    detail["signal_month"] = detail["source_signal_date"].map(month_id)
    detail["signal_quarter"] = detail["source_signal_date"].map(quarter_id)
    market_regimes = load_market_regime_map()
    detail["signal_market_regime"] = detail["source_signal_date"].map(lambda date: market_regimes.get(date, "unknown"))

    rows: list[dict[str, Any]] = []
    for outcome_rule_id, outcome_group in detail.groupby("outcome_rule_id", dropna=False):
        outcome_rule_id = safe_str(outcome_rule_id)
        for segment_id, description, condition in segment_specs():
            segment = outcome_group[condition(outcome_group).fillna(False)].copy()
            segment_rows: list[dict[str, Any]] = []
            if not segment.empty:
                all_dates = segment["source_signal_date"].map(normalize_date)
                segment_rows.append(
                    base_row(
                        outcome_rule_id=outcome_rule_id,
                        segment_id=segment_id,
                        segment_description=description,
                        row_type="period",
                        period_type="all",
                        period_id="all_available_period",
                        period_start_date=str(all_dates.min()),
                        period_end_date=str(all_dates.max()),
                        metrics_row=metrics(segment),
                        generated_at=generated_at,
                    )
                )
                segment_rows.extend(
                    period_rows_for_group(
                        group=segment,
                        outcome_rule_id=outcome_rule_id,
                        segment_id=segment_id,
                        segment_description=description,
                        period_type="quarter",
                        period_column="signal_quarter",
                        generated_at=generated_at,
                    )
                )
                segment_rows.extend(
                    period_rows_for_group(
                        group=segment,
                        outcome_rule_id=outcome_rule_id,
                        segment_id=segment_id,
                        segment_description=description,
                        period_type="month",
                        period_column="signal_month",
                        generated_at=generated_at,
                    )
                )
                segment_rows.extend(
                    period_rows_for_group(
                        group=segment,
                        outcome_rule_id=outcome_rule_id,
                        segment_id=segment_id,
                        segment_description=description,
                        period_type="market_regime",
                        period_column="signal_market_regime",
                        generated_at=generated_at,
                    )
                )
            segment_rows.append(
                summary_row(
                    all_rows=segment_rows,
                    outcome_rule_id=outcome_rule_id,
                    segment_id=segment_id,
                    segment_description=description,
                    generated_at=generated_at,
                )
            )
            rows.extend(segment_rows)

    output = pd.DataFrame(rows)
    for column in OUTPUT_COLUMNS:
        if column not in output.columns:
            output[column] = ""
    forbidden = sorted(set(output.columns) & FORBIDDEN_PRODUCTION_FIELDS)
    if forbidden:
        raise SystemExit(f"ERROR: forbidden production columns in stability audit: {forbidden}")
    return output[OUTPUT_COLUMNS]


def markdown_table(rows: pd.DataFrame, columns: list[str], limit: int) -> list[str]:
    if rows.empty:
        return ["_No rows._"]
    clipped = rows.head(limit)
    lines = [
        "| " + " | ".join(columns) + " |",
        "| " + " | ".join(["---"] * len(columns)) + " |",
    ]
    for _, row in clipped.iterrows():
        lines.append("| " + " | ".join(safe_str(row.get(column)) for column in columns) + " |")
    return lines


def write_markdown(audit: pd.DataFrame, generated_at: str) -> None:
    neutral_summary = audit[
        audit["outcome_rule_id"].eq("tp10_or_neutral_after_5pct_close_40d")
        & audit["row_type"].eq("summary")
        & audit["segment_id"].isin(STRICT_SEGMENTS)
    ].copy()
    neutral_summary["segment_order"] = neutral_summary["segment_id"].map(
        {segment_id: idx for idx, segment_id in enumerate(STRICT_SEGMENTS)}
    )
    neutral_summary = neutral_summary.sort_values("segment_order")
    neutral_month = audit[
        audit["outcome_rule_id"].eq("tp10_or_neutral_after_5pct_close_40d")
        & audit["row_type"].eq("period")
        & audit["period_type"].eq("month")
        & audit["segment_id"].eq("smooth_right_rebound_5_20")
    ].copy()
    neutral_regime = audit[
        audit["outcome_rule_id"].eq("tp10_or_neutral_after_5pct_close_40d")
        & audit["row_type"].eq("period")
        & audit["period_type"].eq("market_regime")
        & audit["segment_id"].isin(STRICT_SEGMENTS)
    ].copy()
    neutral_regime["segment_order"] = neutral_regime["segment_id"].map(
        {segment_id: idx for idx, segment_id in enumerate(STRICT_SEGMENTS)}
    )
    neutral_regime = neutral_regime.sort_values(["segment_order", "period_id"])
    populated_periods = sorted(
        period for period in neutral_month["period_id"].astype(str).unique() if period
    )
    signal_window = (
        f"{populated_periods[0]} to {populated_periods[-1]}"
        if populated_periods
        else "pending_review"
    )

    lines = [
        "# W-Bottom Early-Entry Stability Audit",
        "",
        f"- generated_at: `{generated_at}`",
        f"- source_research_id: `{SOURCE_RESEARCH_ID}`",
        "- production impact: `none`",
        "- surface: `w_bottom_right_low_early_entry` only.",
        "- scope: variant nearest-micro event replay, split by signal month and quarter.",
        f"- limitation: current backfilled signal window is `{signal_window}`; this remains a short-window stability check, not long-term evidence.",
        "",
        "## Strict Segment Monthly Rollup",
        "",
        *markdown_table(
            neutral_summary,
            [
                "segment_id",
                "period_count",
                "periods_with_mature_ge5",
                "periods_with_mature_ge10",
                "sample_size",
                "mature_sample_size",
                "win_count",
                "neutral_count",
                "loss_count",
                "win_rate_excl_neutral_pct",
                "neutral_rate_evaluated_pct",
                "min_period_win_rate_pct",
                "max_period_win_rate_pct",
                "win_rate_range_mature_ge5_pct",
                "win_rate_range_mature_ge10_pct",
                "stability_status",
                "mature_period_stability_status",
                "next_review_status",
            ],
            20,
        ),
        "",
        "## smooth_right_rebound_5_20 Monthly Detail",
        "",
        *markdown_table(
            neutral_month,
            [
                "period_id",
                "sample_size",
                "evaluated_sample_size",
                "mature_sample_size",
                "win_count",
                "neutral_count",
                "loss_count",
                "incomplete_count",
                "win_rate_excl_neutral_pct",
                "neutral_rate_evaluated_pct",
                "research_interpretation",
            ],
            20,
        ),
        "",
        "## Market Regime Rollup",
        "",
        *markdown_table(
            neutral_regime,
            [
                "segment_id",
                "period_id",
                "sample_size",
                "evaluated_sample_size",
                "mature_sample_size",
                "win_count",
                "neutral_count",
                "loss_count",
                "win_rate_excl_neutral_pct",
                "neutral_rate_evaluated_pct",
                "research_interpretation",
            ],
            80,
        ),
        "",
        "## Guardrails",
        "",
        "- This is research/backtest advisory-only work.",
        "- Rows remain `approved_for_daily=false` and `warning_research_variant_only`.",
        "- This audit does not modify production conditions, scoring, ranking, PDFs, baselines, or daily_full_pipeline.",
        "- Stability failures block promotion; they do not imply production drift.",
    ]
    LATEST_MD.parent.mkdir(parents=True, exist_ok=True)
    LATEST_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    generated_at = now_text()
    audit = build_audit(generated_at)
    if audit.empty:
        raise SystemExit("ERROR: W-bottom early-entry stability audit generated no rows")
    write_csv(audit, LATEST_CSV)
    write_csv(audit, HISTORY_CSV)
    write_markdown(audit, generated_at)
    print(f"Saved: {LATEST_CSV} rows={len(audit)}")
    print(f"Saved: {LATEST_MD}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
