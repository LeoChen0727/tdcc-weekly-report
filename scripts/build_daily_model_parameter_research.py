from __future__ import annotations

import math
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Callable

import numpy as np
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent))

from research_weekly_20pct_surge_volume import build_stock_day_frame  # noqa: E402
from research_weekly_surge_technical_grid import add_technical_features  # noqa: E402
from research_weekly_surge_theme_segments import attach_theme_labels  # noqa: E402
from build_daily_candidate_model_layer import build_parameter_table, build_specs, cond_pullback  # noqa: E402
from build_approved_operation_patterns import (  # noqa: E402
    NECKLINE_APPROVAL_METRICS,
    NECKLINE_OPERATION_MODULE_ID,
    W_BOTTOM_APPROVAL_METRICS,
    W_BOTTOM_OPERATION_MODULE_ID,
)
from tracking_utils import (  # noqa: E402
    DOCS_LATEST_DIR,
    LATEST_DIR,
    RESEARCH_LATEST_DIR,
    markdown_table,
    normalize_code,
    normalize_date,
    now_text,
    safe_str,
    write_csv,
)


HISTORY_DIR = Path("output/history/research")
DAILY_SNAPSHOT_DIR = Path("output/history/daily_model_snapshots")
OUT_CSV = LATEST_DIR / "daily_model_parameter_research_latest.csv"
OUT_MD = LATEST_DIR / "daily_model_parameter_research_latest.md"
OUT_DETAIL_CSV = LATEST_DIR / "daily_model_parameter_research_horizon_detail_latest.csv"
OUT_DETAIL_MD = LATEST_DIR / "daily_model_parameter_research_horizon_detail_latest.md"
OUT_PARITY_CSV = RESEARCH_LATEST_DIR / "daily_model_research_parity_latest.csv"
OUT_PARITY_MD = RESEARCH_LATEST_DIR / "daily_model_research_parity_latest.md"
HISTORY_CSV = HISTORY_DIR / "daily_model_parameter_research.csv"
DOCS_CSV = DOCS_LATEST_DIR / OUT_CSV.name
DOCS_MD = DOCS_LATEST_DIR / OUT_MD.name
DOCS_DETAIL_CSV = DOCS_LATEST_DIR / OUT_DETAIL_CSV.name
DOCS_DETAIL_MD = DOCS_LATEST_DIR / OUT_DETAIL_MD.name
DOCS_PARITY_CSV = DOCS_LATEST_DIR / OUT_PARITY_CSV.name
DOCS_PARITY_MD = DOCS_LATEST_DIR / OUT_PARITY_MD.name
PRICE_PULLBACK_OPERATION_CSV = RESEARCH_LATEST_DIR / "price_pullback_23ema_operation_research_latest.csv"
PRICE_PULLBACK_OPERATION_MD = RESEARCH_LATEST_DIR / "price_pullback_23ema_operation_research_latest.md"
PRICE_PULLBACK_OPERATION_HISTORY_CSV = HISTORY_DIR / "price_pullback_23ema_operation_research.csv"
DOCS_PRICE_PULLBACK_OPERATION_CSV = DOCS_LATEST_DIR / PRICE_PULLBACK_OPERATION_CSV.name
DOCS_PRICE_PULLBACK_OPERATION_MD = DOCS_LATEST_DIR / PRICE_PULLBACK_OPERATION_MD.name
PRICE_PULLBACK_TIME_COST_CSV = RESEARCH_LATEST_DIR / "price_pullback_23ema_time_cost_backtest_latest.csv"
PRICE_PULLBACK_TIME_COST_MD = RESEARCH_LATEST_DIR / "price_pullback_23ema_time_cost_backtest_latest.md"
PRICE_PULLBACK_TIME_COST_HISTORY_CSV = HISTORY_DIR / "price_pullback_23ema_time_cost_backtest.csv"
DOCS_PRICE_PULLBACK_TIME_COST_CSV = DOCS_LATEST_DIR / PRICE_PULLBACK_TIME_COST_CSV.name
DOCS_PRICE_PULLBACK_TIME_COST_MD = DOCS_LATEST_DIR / PRICE_PULLBACK_TIME_COST_MD.name
PRICE_PULLBACK_OPERATION_MODULE_CSV = RESEARCH_LATEST_DIR / "price_pullback_23ema_operation_module_research_latest.csv"
PRICE_PULLBACK_OPERATION_MODULE_MD = RESEARCH_LATEST_DIR / "price_pullback_23ema_operation_module_research_latest.md"
PRICE_PULLBACK_OPERATION_MODULE_HISTORY_CSV = HISTORY_DIR / "price_pullback_23ema_operation_module_research.csv"
DOCS_PRICE_PULLBACK_OPERATION_MODULE_CSV = DOCS_LATEST_DIR / PRICE_PULLBACK_OPERATION_MODULE_CSV.name
DOCS_PRICE_PULLBACK_OPERATION_MODULE_MD = DOCS_LATEST_DIR / PRICE_PULLBACK_OPERATION_MODULE_MD.name
PRICE_PULLBACK_FEATURE_CONFIRMATION_CSV = (
    RESEARCH_LATEST_DIR / "price_pullback_23ema_feature_confirmation_research_latest.csv"
)
PRICE_PULLBACK_FEATURE_CONFIRMATION_MD = (
    RESEARCH_LATEST_DIR / "price_pullback_23ema_feature_confirmation_research_latest.md"
)
PRICE_PULLBACK_FEATURE_CONFIRMATION_HISTORY_CSV = HISTORY_DIR / "price_pullback_23ema_feature_confirmation_research.csv"
DOCS_PRICE_PULLBACK_FEATURE_CONFIRMATION_CSV = DOCS_LATEST_DIR / PRICE_PULLBACK_FEATURE_CONFIRMATION_CSV.name
DOCS_PRICE_PULLBACK_FEATURE_CONFIRMATION_MD = DOCS_LATEST_DIR / PRICE_PULLBACK_FEATURE_CONFIRMATION_MD.name
PRICE_PULLBACK_DAILY_ROW_PARITY_CSV = (
    RESEARCH_LATEST_DIR / "price_pullback_23ema_daily_row_parity_latest.csv"
)
PRICE_PULLBACK_DAILY_ROW_PARITY_MD = (
    RESEARCH_LATEST_DIR / "price_pullback_23ema_daily_row_parity_latest.md"
)
PRICE_PULLBACK_DAILY_ROW_PARITY_HISTORY_CSV = HISTORY_DIR / "price_pullback_23ema_daily_row_parity.csv"
DOCS_PRICE_PULLBACK_DAILY_ROW_PARITY_CSV = DOCS_LATEST_DIR / PRICE_PULLBACK_DAILY_ROW_PARITY_CSV.name
DOCS_PRICE_PULLBACK_DAILY_ROW_PARITY_MD = DOCS_LATEST_DIR / PRICE_PULLBACK_DAILY_ROW_PARITY_MD.name
PRICE_PULLBACK_DECISION_AUDIT_CSV = (
    RESEARCH_LATEST_DIR / "price_pullback_23ema_model_decision_audit_latest.csv"
)
PRICE_PULLBACK_DECISION_AUDIT_MD = RESEARCH_LATEST_DIR / "price_pullback_23ema_model_decision_audit_latest.md"
PRICE_PULLBACK_DECISION_AUDIT_HISTORY_CSV = HISTORY_DIR / "price_pullback_23ema_model_decision_audit.csv"
DOCS_PRICE_PULLBACK_DECISION_AUDIT_CSV = DOCS_LATEST_DIR / PRICE_PULLBACK_DECISION_AUDIT_CSV.name
DOCS_PRICE_PULLBACK_DECISION_AUDIT_MD = DOCS_LATEST_DIR / PRICE_PULLBACK_DECISION_AUDIT_MD.name

HORIZONS = list(range(1, 11)) + [20]
TIME_COST_HORIZON_DAYS = 20
TIME_COST_TARGET_PCT = 5.0
TIME_COST_STOP_PCT = -5.0
MIN_OK_SAMPLE = 100
MIN_REVIEW_SAMPLE = 30
PRICE_PULLBACK_CANDIDATE_REPLAY_REQUIRED_COLUMNS = {
    "stock_id",
    "candidate_source_type",
    "candidate_line",
    "candidate_line_group",
    "source_row_index",
    "close",
    "ema23",
    "ma20",
    "distance_to_ema23_pct",
    "gap_ema23_pct",
    "platform_low",
    "short_platform_low",
    "previous_20d_low",
    "low_20",
    "ma5_turning_up_flag",
    "ma10_turning_up_flag",
}


@dataclass(frozen=True)
class RuleSpec:
    model_id: str
    model_name_zh: str
    parameter_set_id: str
    parameter_summary: str
    pdf_visibility: str
    condition: Callable[[pd.DataFrame], pd.Series]
    notes: str
    parameter_role: str = "parameter_variant"
    production_parity_status: str = "variant_not_baseline"
    parity_blocker: str = ""
    variant_of: str = ""


def pct(num: float) -> str:
    if math.isnan(num):
        return "-"
    return f"{num:.2f}%"


def sample_status(n: int) -> str:
    if n >= MIN_OK_SAMPLE:
        return "ok_first_pass"
    if n >= MIN_REVIEW_SAMPLE:
        return "small_sample_review_only"
    return "insufficient_sample"


def bool_series(df: pd.DataFrame, value: bool = False) -> pd.Series:
    return pd.Series(value, index=df.index)


def between(series: pd.Series, low: float, high: float) -> pd.Series:
    return (series >= low) & (series <= high)


def trueish(series: pd.Series) -> pd.Series:
    if series.dtype == bool:
        return series.fillna(False)
    return series.astype(str).str.lower().isin(["true", "1", "yes"])


def numeric_column(df: pd.DataFrame, name: str) -> pd.Series:
    if name not in df.columns:
        return pd.Series(math.nan, index=df.index)
    return pd.to_numeric(df[name], errors="coerce")


def trueish_column(df: pd.DataFrame, name: str) -> pd.Series:
    if name not in df.columns:
        return bool_series(df)
    return trueish(df[name])


def add_price_structure_features(df: pd.DataFrame) -> pd.DataFrame:
    out = df.sort_values(["stock_id", "date"]).copy()
    groups = out.groupby("stock_id", group_keys=False)

    if "ma5" not in out.columns:
        out["ma5"] = groups["close"].transform(lambda s: s.rolling(5, min_periods=3).mean())
    if "ma10" not in out.columns:
        out["ma10"] = groups["close"].transform(lambda s: s.rolling(10, min_periods=5).mean())
    out["ma5_turning_up_flag"] = out["ma5"] > groups["ma5"].shift(1)
    out["ma10_turning_up_flag"] = out["ma10"] > groups["ma10"].shift(1)
    out["ema23_prev5"] = groups["ema23"].shift(5)
    out["ema23_slope_5d_pct"] = (out["ema23"] / out["ema23_prev5"] - 1.0) * 100.0
    out["ema23_slope_pct"] = out["ema23_slope_5d_pct"]
    out["previous_close"] = groups["close"].shift(1)
    out["signal_return_1d_pct"] = (out["close"] / out["previous_close"] - 1.0) * 100.0
    out["return_45d_pct"] = groups["close"].pct_change(45) * 100.0
    out["close_above_open"] = out["close"] > out["open"]
    out["bullish_attack_candle"] = (out["close"] > out["open"]) | (
        out["close"].eq(out["open"]) & (out["close"] > out["previous_close"])
    )
    candle_range = (out["high"] - out["low"]).replace(0, pd.NA)
    out["body_ratio"] = (out["close"] - out["open"]).abs() / candle_range
    out["upper_shadow_ratio"] = (out["high"] - out[["close", "open"]].max(axis=1)) / candle_range
    out["close_location"] = (out["close"] - out["low"]) / candle_range
    out["solid_red_candle"] = (
        (out["close"] > out["open"])
        & (out["body_ratio"] >= 0.25)
        & (out["upper_shadow_ratio"] <= 0.35)
        & (out["close_location"] >= 0.65)
    )

    # build_stock_day_frame already calculates this with a per-stock previous
    # 20-day denominator. Keep the alias local to this research script so the
    # parameter rules read consistently.
    out["volume_ratio_prev20"] = out["start_day_volume_ratio_vs_prev20"]
    volume_ma20 = (
        groups["volume"]
        .shift(1)
        .rolling(20, min_periods=10)
        .mean()
        .reset_index(level=0, drop=True)
    )
    # Some sources store raw shares, others store lots. Normalize only clearly
    # share-denominated values so the liquidity rule remains stable.
    out["volume_ma20_lots"] = volume_ma20.where(volume_ma20 < 100000, volume_ma20 / 1000.0)
    obv_direction = np.sign(out["close"] - out["previous_close"]).fillna(0.0)
    obv_flow = obv_direction * pd.to_numeric(out["volume"], errors="coerce").fillna(0.0)
    out["obv"] = obv_flow.groupby(out["stock_id"]).cumsum()
    obv_groups = out.groupby("stock_id", group_keys=False)
    out["obv_ma20"] = obv_groups["obv"].transform(lambda s: s.rolling(20, min_periods=10).mean())
    out["obv_above_ma20"] = out["obv"] > out["obv_ma20"]
    out["obv_slope_5d"] = out["obv"] - obv_groups["obv"].shift(5)

    for window in [10, 20, 23, 30, 45, 60]:
        high = groups["high"].shift(1).rolling(window, min_periods=max(5, min(window, 20))).max().reset_index(level=0, drop=True)
        low = groups["low"].shift(1).rolling(window, min_periods=max(5, min(window, 20))).min().reset_index(level=0, drop=True)
        out[f"range_high_{window}d_prev"] = high
        out[f"range_low_{window}d_prev"] = low
        out[f"range_width_{window}d_pct"] = (high / low - 1.0) * 100.0
        out[f"range_breakout_{window}d_pct"] = (out["close"] / high - 1.0) * 100.0
        out[f"distance_to_range_high_{window}d_pct"] = (out["close"] / high - 1.0) * 100.0

    range_45d = (out["range_high_45d_prev"] - out["range_low_45d_prev"]).replace(0, pd.NA)
    out["close_position_45d_pct"] = (out["close"] - out["range_low_45d_prev"]) / range_45d * 100.0

    for window in [20, 30, 60]:
        high = out[f"range_high_{window}d_prev"]
        low = out[f"range_low_{window}d_prev"]
        out[f"prior_extension_ema23_{window}d_pct"] = (high / out["ema23"] - 1.0) * 100.0
        out[f"prior_runup_{window}d_pct"] = (high / low - 1.0) * 100.0
        out[f"pullback_from_high_{window}d_pct"] = (out["close"] / high - 1.0) * 100.0

    out["distance_to_ema23_pct"] = out["distance_ema23_pct"]
    out["distance_23ema_pct"] = out["distance_ema23_pct"]
    out["gap_ema23_pct"] = out["distance_ema23_pct"]
    out["platform_high"] = out["range_high_20d_prev"]
    out["platform_low"] = out["range_low_20d_prev"]
    out["short_platform_high"] = out["range_high_10d_prev"]
    out["short_platform_low"] = out["range_low_10d_prev"]
    out["previous_20d_low"] = out["range_low_20d_prev"]
    out["low_20"] = out["range_low_20d_prev"]
    support_zone = (
        (out["previous_20d_low"] > 0)
        & (out["close"] >= out["previous_20d_low"] * 0.98)
        & (out["close"] <= out["previous_20d_low"] * 1.08)
    )
    out["pullback_entry_zone_flag"] = between(out["distance_ema23_pct"], -2.5, 5.0) | support_zone

    future_return_cols: dict[str, pd.Series] = {}
    for day in range(1, TIME_COST_HORIZON_DAYS + 1):
        future_close = groups["close"].shift(-day)
        future_high = groups["high"].shift(-day)
        future_low = groups["low"].shift(-day)
        future_return_cols[f"next_open_to_d{day}_day_close_return_pct"] = (
            future_close / out["next_open"] - 1.0
        ) * 100.0
        future_return_cols[f"next_open_to_d{day}_day_high_return_pct"] = (future_high / out["next_open"] - 1.0) * 100.0
        future_return_cols[f"next_open_to_d{day}_day_low_return_pct"] = (future_low / out["next_open"] - 1.0) * 100.0
        future_return_cols[f"future_d{day}_ma20"] = groups["ma20"].shift(-day)
        future_return_cols[f"future_d{day}_ema23"] = groups["ema23"].shift(-day)
    out = pd.concat([out, pd.DataFrame(future_return_cols, index=out.index)], axis=1)

    range_pct = (out["high"] - out["low"]) / out["previous_close"].replace(0, pd.NA) * 100.0
    out["locked_limit_up_breakout"] = (
        (out["range_breakout_20d_pct"] >= 2.0)
        & (out["signal_return_1d_pct"] >= 9.0)
        & (out["close"] >= out["high"] * 0.995)
        & (out["open"] >= out["close"] * 0.995)
        & ((out["high"] == out["low"]) | (range_pct <= 1.0))
    )

    # A simple W-bottom proxy for research: the latest 35 trading days contain two
    # similar lows and the second low is higher, while price is back in the upper half.
    low_35 = groups["low"].shift(1).rolling(35, min_periods=25).min().reset_index(level=0, drop=True)
    low_18 = groups["low"].shift(1).rolling(18, min_periods=12).min().reset_index(level=0, drop=True)
    high_35 = groups["high"].shift(1).rolling(35, min_periods=25).max().reset_index(level=0, drop=True)
    out["w_bottom_proxy"] = (
        (low_18 >= low_35 * 0.98)
        & (low_18 <= low_35 * 1.12)
        & (out["close"] >= (low_35 + high_35) / 2)
        & (out["ema23_slope_5d_pct"] > 0)
    )
    return out


def attach_tdcc_features(df: pd.DataFrame) -> pd.DataFrame:
    rows: list[pd.DataFrame] = []
    tdcc_dir = Path("data/tdcc_stock_history")
    for path in sorted(tdcc_dir.glob("*.csv")):
        try:
            t = pd.read_csv(path, dtype={"stock_id": str}, keep_default_na=False)
        except Exception:
            continue
        if t.empty or "as_of_date" not in t.columns or "stock_id" not in t.columns:
            continue
        t = t.copy()
        t["stock_id"] = t["stock_id"].astype(str).str.extract(r"(\d+)")[0].str.zfill(4)
        t["tdcc_as_of_date"] = t["as_of_date"].astype(str).str.replace(r"\D", "", regex=True).str[:8]
        keep = [
            "stock_id",
            "tdcc_as_of_date",
            "tdcc_consecutive_up_weeks",
            "all_thresholds_up",
            "high_thresholds_up",
            "four_thresholds_sync_up",
            "over_400_change_1w",
            "over_800_change_1w",
            "over_1000_change_1w",
        ]
        for col in keep:
            if col not in t.columns:
                t[col] = ""
        rows.append(t[keep])
    if not rows:
        out = df.copy()
        out["tdcc_history_available"] = False
        return out

    tdcc = pd.concat(rows, ignore_index=True)
    tdcc["tdcc_date_dt"] = pd.to_datetime(tdcc["tdcc_as_of_date"], format="%Y%m%d", errors="coerce")
    for col in ["tdcc_consecutive_up_weeks", "over_400_change_1w", "over_800_change_1w", "over_1000_change_1w"]:
        tdcc[col] = pd.to_numeric(tdcc[col], errors="coerce")
    for col in ["all_thresholds_up", "high_thresholds_up", "four_thresholds_sync_up"]:
        tdcc[col] = tdcc[col].astype(str).str.lower().isin(["true", "1", "yes"])

    left = df.copy()
    left["price_date_dt"] = pd.to_datetime(left["date"].astype(str), format="%Y%m%d", errors="coerce")
    merged_parts: list[pd.DataFrame] = []
    for stock_id, price_part in left.groupby("stock_id", sort=False):
        tdcc_part = tdcc[tdcc["stock_id"].eq(stock_id)].sort_values("tdcc_date_dt")
        if tdcc_part.empty:
            p = price_part.copy()
            p["tdcc_history_available"] = False
            merged_parts.append(p)
            continue
        merged = pd.merge_asof(
            price_part.sort_values("price_date_dt"),
            tdcc_part.drop(columns=["stock_id"]).sort_values("tdcc_date_dt"),
            left_on="price_date_dt",
            right_on="tdcc_date_dt",
            direction="backward",
        )
        merged["tdcc_history_available"] = merged["tdcc_as_of_date"].notna()
        merged_parts.append(merged)
    out = pd.concat(merged_parts, ignore_index=True)
    return out


def build_research_frame() -> pd.DataFrame:
    df = build_stock_day_frame()
    if df.empty:
        return df
    df = add_technical_features(df)
    df = add_price_structure_features(df)
    df = attach_theme_labels(df)
    df = attach_tdcc_features(df)
    return df


def support_retest_mask(d: pd.DataFrame, low_col: str = "range_low_20d_prev") -> pd.Series:
    return (
        (d[low_col] > 0)
        & (d["close"] >= d[low_col] * 0.98)
        & (d["close"] <= d[low_col] * 1.08)
    )


def price_pullback_near_ema23_or_support(d: pd.DataFrame) -> pd.Series:
    distance = numeric_column(d, "distance_ema23_pct")
    near_ema23 = between(distance, -2.5, 5.0)
    support_cols = ["platform_low", "short_platform_low", "previous_20d_low", "low_20", "range_low_20d_prev"]
    support = bool_series(d)
    close = numeric_column(d, "close")
    for col in support_cols:
        low = numeric_column(d, col)
        support = support | ((low > 0) & (close >= low * 0.98) & (close <= low * 1.08))
    return (near_ema23 | support).fillna(False)


def price_pullback_ema23_slope_proxy_up(d: pd.DataFrame) -> pd.Series:
    close = numeric_column(d, "close")
    ema23 = numeric_column(d, "ema23")
    ma20 = numeric_column(d, "ma20")
    slope = numeric_column(d, "ema23_slope_pct")
    if slope.isna().all():
        slope = numeric_column(d, "ema23_slope_5d_pct")
    return (
        trueish_column(d, "ma5_turning_up_flag")
        | trueish_column(d, "ma10_turning_up_flag")
        | (slope > 0)
        | ((close > 0) & (ema23 > 0) & (close >= ema23))
        | ((ema23 > 0) & (ma20 > 0) & (ema23 >= ma20 * 0.98))
    ).fillna(False)


def current_volume_range_breakout_baseline(d: pd.DataFrame) -> pd.Series:
    normal_volume = (
        (d["volume_ratio_prev20"] >= 2.0)
        & (d["range_breakout_20d_pct"] >= 2.0)
        & (d["volume_ma20_lots"] >= 1000)
        & d["bullish_attack_candle"]
    )
    return normal_volume | d["locked_limit_up_breakout"]


def current_price_pullback_baseline_proxy(d: pd.DataFrame) -> pd.Series:
    return price_pullback_near_ema23_or_support(d) & price_pullback_ema23_slope_proxy_up(d)


def price_pullback_red_k_entry_filter(d: pd.DataFrame, volume_min: float, solid: bool = False) -> pd.Series:
    candle_col = "solid_red_candle" if solid else "bullish_attack_candle"
    return (numeric_column(d, "volume_ratio_prev20") >= volume_min) & trueish_column(d, candle_col)


def price_pullback_prior_extension_filter(
    d: pd.DataFrame,
    window: int,
    min_extension_pct: float,
    min_runup_pct: float,
    min_pullback_from_high_pct: float,
) -> pd.Series:
    return (
        (numeric_column(d, f"prior_extension_ema23_{window}d_pct") >= min_extension_pct)
        & (numeric_column(d, f"prior_runup_{window}d_pct") >= min_runup_pct)
        & (numeric_column(d, f"pullback_from_high_{window}d_pct") <= -min_pullback_from_high_pct)
    ).fillna(False)


def price_pullback_45d_bullish_pullback_filter(d: pd.DataFrame) -> pd.Series:
    return (
        (numeric_column(d, "return_45d_pct") >= 8.0)
        & (numeric_column(d, "range_width_45d_pct") >= 18.0)
        & between(numeric_column(d, "close_position_45d_pct"), 35.0, 80.0)
    ).fillna(False)


def price_pullback_return20_balanced_filter(d: pd.DataFrame) -> pd.Series:
    return between(numeric_column(d, "return_20d_pct"), 0.0, 25.0).fillna(False)


def price_pullback_tdcc_high_thresholds_up_filter(d: pd.DataFrame) -> pd.Series:
    return (trueish_column(d, "tdcc_history_available") & trueish_column(d, "high_thresholds_up")).fillna(False)


def price_pullback_tdcc_consecutive_up_ge1_filter(d: pd.DataFrame) -> pd.Series:
    return (
        trueish_column(d, "tdcc_history_available")
        & (numeric_column(d, "tdcc_consecutive_up_weeks") >= 1.0)
    ).fillna(False)


def price_pullback_macd_kd_confirm_filter(d: pd.DataFrame) -> pd.Series:
    return (trueish_column(d, "macd_hist_gt0") & trueish_column(d, "kd_bullish_not_overheated")).fillna(False)


def price_pullback_obv_above_ma20_filter(d: pd.DataFrame) -> pd.Series:
    return trueish_column(d, "obv_above_ma20").fillna(False)


def price_pullback_volume_red_k_entry(d: pd.DataFrame, volume_min: float, solid: bool = False) -> pd.Series:
    return current_price_pullback_baseline_proxy(d) & price_pullback_red_k_entry_filter(d, volume_min, solid)


def current_hot_theme_pullback_baseline_proxy(d: pd.DataFrame) -> pd.Series:
    return (
        d["strict_theme_status_group"].isin({"mainstream_supported", "mainstream_overheated"})
        & (between(d["distance_ema23_pct"], -2.5, 5.0) | support_retest_mask(d))
    )


def active_price_attack_proxy(d: pd.DataFrame) -> pd.Series:
    return (
        current_volume_range_breakout_baseline(d)
        | (d["volume_ratio_prev20"] >= 2.5)
        | (d["return_5d_pct"] >= 8)
        | (d["return_20d_pct"] >= 20)
    ).fillna(False)


def current_revenue_unreacted_baseline_proxy(d: pd.DataFrame) -> pd.Series:
    # Historical revenue feature panels are not yet complete in this research
    # frame, so this can only mirror the production price-range and not-started
    # parts. The parity artifact must keep this row marked as proxy-only.
    return (
        (d["close"] >= d["range_low_23d_prev"] * 0.95)
        & (d["close"] <= d["range_high_23d_prev"] * 1.05)
        & (~active_price_attack_proxy(d))
    )


def current_w_bottom_baseline_proxy(d: pd.DataFrame) -> pd.Series:
    return d["w_bottom_proxy"] & (d["range_breakout_20d_pct"] < 2.0)


def current_w_bottom_approved_operation_baseline(d: pd.DataFrame) -> pd.Series:
    """Anchor W-bottom parity to the approved operation artifact.

    The production detector itself is row/context based and too expensive for
    the generic parameter-grid builder. The formal daily operation contract is
    the approved operation artifact, while raw candidate rows remain
    research-only.
    """
    return current_w_bottom_baseline_proxy(d)


def current_neckline_volume_breakout_baseline_proxy(d: pd.DataFrame) -> pd.Series:
    return (
        d["w_bottom_proxy"]
        & (
            ((d["range_breakout_20d_pct"] >= 0.0) & (d["volume_ratio_prev20"] >= 2.0) & d["bullish_attack_candle"])
            | d["locked_limit_up_breakout"]
        )
    )


def current_neckline_approved_operation_baseline(d: pd.DataFrame) -> pd.Series:
    """Anchor neckline parity to the approved operation v1 artifact.

    The formal daily operation contract is the approved operation artifact.
    Raw research rows remain advisory-only; production scoring/entry rules are
    synchronized through the operation module and contract metadata.
    """
    return current_neckline_volume_breakout_baseline_proxy(d)


def current_near_high_baseline_proxy(d: pd.DataFrame) -> pd.Series:
    return (
        between(d["near_60d_high_pct"], -5.0, 0.0)
        & (d["volume_ratio_prev20"] >= 1.2)
        & (d["ema23_slope_5d_pct"] > 0)
        & (d["range_breakout_20d_pct"] < 2.0)
    )


def current_platform_strengthening_baseline_proxy(d: pd.DataFrame) -> pd.Series:
    return (
        (d["range_width_20d_pct"] <= 18)
        & between(d["distance_to_range_high_20d_pct"], -5.0, 1.5)
        & (d["volume_ratio_prev20"] >= 1.2)
        & d["solid_red_candle"]
        & (d["range_breakout_20d_pct"] < 2.0)
    )


def current_pullback_short_reclaim_baseline_proxy(d: pd.DataFrame) -> pd.Series:
    return (
        (d["return_20d_pct"] >= 5)
        & (between(d["distance_ema23_pct"], -1.0, 6.0) | (d["close_above_ma20"] & (d["ema23_slope_5d_pct"] > 0)))
        & (d["ema23_slope_5d_pct"] > 0)
    )


def current_tdcc_stealth_baseline_proxy(d: pd.DataFrame) -> pd.Series:
    return (
        trueish(d["tdcc_history_available"])
        & (
            (d["tdcc_consecutive_up_weeks"] >= 1)
            | trueish(d["all_thresholds_up"])
            | trueish(d["high_thresholds_up"])
        )
        & (d["volume_ratio_prev20"] < 2.5)
        & (d["return_5d_pct"] < 8)
        & (d["return_20d_pct"] < 20)
        & (d["close"] >= d["range_low_23d_prev"] * 0.90)
        & (d["close"] <= d["range_high_23d_prev"] * 1.10)
        & (~current_volume_range_breakout_baseline(d))
    )


def current_tdcc_short_term_continuation_baseline_proxy(d: pd.DataFrame) -> pd.Series:
    return (
        trueish(d["tdcc_history_available"])
        & (
            trueish(d["all_thresholds_up"])
            | trueish(d["high_thresholds_up"])
            | trueish(d["four_thresholds_sync_up"])
        )
        & between(d["return_5d_pct"], 10, 30)
        & (trueish(d["macd_hist_gt0"]) | trueish(d["kd_bullish_not_overheated"]))
    )


def production_baseline_specs() -> list[RuleSpec]:
    return [
        RuleSpec(
            "volume_range_breakout",
            "放量攻擊模型",
            "production_current",
            "production baseline: normal prior-20d breakout OR locked-limit-up breakout bypass",
            "pdf_core_model",
            current_volume_range_breakout_baseline,
            "Matches current production logic available in historical price fields, including locked-limit-up bypass without a volume-ratio gate.",
            "production_baseline",
            "production_parity",
            "",
            "production_current",
        ),
        RuleSpec(
            "price_pullback_23ema",
            "股價回檔模型",
            "production_current_proxy",
            "production baseline proxy replay: near 23EMA/support + MA/EMA trend proxy up",
            "pdf_core_model",
            current_price_pullback_baseline_proxy,
            "Research replays production pullback support/EMA and MA/EMA trend proxy fields from point-in-time price history; operation rules remain advisory.",
            "production_baseline",
            "production_proxy",
            "as-published daily candidate row parity and a validated operation module are still pending",
            "production_current",
        ),
        RuleSpec(
            "hot_theme_pullback",
            "熱門族群回檔模型",
            "production_current_proxy",
            "production baseline proxy: no-lookahead mainstream theme + pullback near 23EMA/support",
            "pdf_core_model",
            current_hot_theme_pullback_baseline_proxy,
            "Production uses current model-layer hot theme labels; research uses strict historical no-lookahead theme state.",
            "production_baseline",
            "production_proxy",
            "daily hot-theme labels are not fully backfilled as point-in-time model-layer fields",
            "production_current",
        ),
        RuleSpec(
            "revenue_unreacted_range",
            "營收爆發但股價尚未反應模型",
            "production_current_proxy",
            "production baseline proxy: price still in 23d range and attack not started; revenue panel missing",
            "pdf_core_model",
            current_revenue_unreacted_baseline_proxy,
            "Revenue YoY/cumulative YoY history is not complete in this research frame, so this row is not production-parity.",
            "production_baseline",
            "proxy_only",
            "historical revenue panel is incomplete; strong_revenue gate cannot be replayed point-in-time",
            "production_current",
        ),
        RuleSpec(
            "w_bottom_right_side",
            "W底右側模型",
            W_BOTTOM_OPERATION_MODULE_ID,
            "approved operation baseline: right-low early entry, W-structure-low stop, D+20 gain10 else D+40 close exit",
            "pdf_core_model",
            current_w_bottom_approved_operation_baseline,
            (
                f"{W_BOTTOM_OPERATION_MODULE_ID} is the formal daily baseline through "
                "approved_operation_patterns_latest.csv; raw research candidate rows remain advisory-only."
            ),
            "production_baseline",
            "production_parity",
            "",
            "production_current",
        ),
        RuleSpec(
            "neckline_volume_breakout_confirmation",
            "W底頸線帶量突破確認模型",
            NECKLINE_OPERATION_MODULE_ID,
            "approved operation baseline: W-bottom neckline signal, 45d non-bearish context, 90d score-only context, next-open entry and 20d operation-rule outcome",
            "pdf_core_model",
            current_neckline_approved_operation_baseline,
            (
                "W-bottom neckline volume breakout operation v1 is the formal daily baseline through "
                "approved_operation_patterns_latest.csv; other neckline subtypes remain outside this model."
            ),
            "production_baseline",
            "production_parity",
            "",
            "production_current",
        ),
        RuleSpec(
            "pullback_short_reclaim",
            "回檔後短線轉強模型",
            "production_current_proxy",
            "production baseline proxy: 20d return >= 5%, pullback/reclaim proxy, EMA23 up",
            "pdf_core_model",
            current_pullback_short_reclaim_baseline_proxy,
            "Production uses pullback/right-side/reclaim flags; research approximates with EMA and MA20 reclaim context.",
            "production_baseline",
            "production_proxy",
            "pullback_entry_zone/right_side/ma20_reclaim setup flags are not fully backfilled",
            "production_current",
        ),
        RuleSpec(
            "tdcc_stealth_accumulation",
            "TDCC潛伏吸籌模型",
            "production_current_proxy",
            "production baseline proxy: TDCC positive, attack not started, low volume/return, still in range",
            "pdf_core_model",
            current_tdcc_stealth_baseline_proxy,
            "Production uses TDCC phase when available; research uses weekly TDCC history and range constraints.",
            "production_baseline",
            "production_proxy",
            "tdcc_price_phase is not fully available historically for every signal date",
            "production_current",
        ),
        RuleSpec(
            "tdcc_short_term_continuation_d5_d10",
            "TDCC短線延續模型 D+5/D+10",
            "production_current_proxy",
            "production baseline proxy: TDCC sync/high thresholds + 5d momentum + MACD/KD",
            "pdf_core_model",
            current_tdcc_short_term_continuation_baseline_proxy,
            "This mirrors the daily specialty short-term continuation surface enough to serve as baseline before deeper grid variants.",
            "production_baseline",
            "production_proxy",
            "daily specialty packet fields are not a single core build_specs condition and must be replayed from historical TDCC/technical proxies",
            "production_current",
        ),
    ]


def rule_specs() -> list[RuleSpec]:
    specs: list[RuleSpec] = production_baseline_specs()

    for breakout_pct in [1.0, 2.0, 3.0]:
        for vol in [2.0, 3.0, 5.0]:
            for min_lots in [500, 1000, 2000]:
                specs.append(
                    RuleSpec(
                        "volume_range_breakout",
                        "放量攻擊模型",
                        f"prior20x{1 + breakout_pct / 100:.2f}_vol{vol:g}_minvol{min_lots}",
                        f"收盤突破前20日高點 {breakout_pct:g}% + 量比 >= {vol:g} + 20日均量 >= {min_lots}張 + 實體紅K",
                        "pdf_core_model",
                        lambda d, breakout_pct=breakout_pct, vol=vol, min_lots=min_lots: (
                            (d["volume_ratio_prev20"] >= vol)
                            & (d["range_breakout_20d_pct"] >= breakout_pct)
                            & (d["volume_ma20_lots"] >= min_lots)
                            & d["bullish_attack_candle"]
                        ),
                        "主條件是前20日高點突破、量能放大、流動性與實體紅K。漲幅、過熱、均線與60日高點不作為此模型否決條件。",
                    )
                )
    specs.append(
        RuleSpec(
            "volume_range_breakout",
            "放量攻擊模型",
            "locked_limit_up_breakout_no_volume_gate",
            "鎖量漲停突破前20日高點 2% + 漲幅 >= 9% + 一價或極窄區間；不要求量比或20日均量",
            "pdf_core_model",
            lambda d: d["locked_limit_up_breakout"],
            "這是現行放量攻擊模型的鎖量漲停旁路；不是全面降低一般突破的量比門檻。",
        )
    )

    for low, high in [(-1.5, 3.0), (-2.5, 5.0), (-4.0, 7.0)]:
        for vol_max in [1.0, 1.2, 1.5]:
            specs.append(
                RuleSpec(
                    "price_pullback_23ema",
                    "股價回檔模型",
                    f"ema{low:g}_{high:g}_volmax{vol_max:g}",
                    f"距 23EMA {low:g}% 至 {high:g}% + 23EMA 向上 + 量比 <= {vol_max:g}",
                    "research_only_not_pdf_core",
                    lambda d, low=low, high=high, vol_max=vol_max: (
                        between(d["distance_ema23_pct"], low, high)
                        & (d["ema23_slope_5d_pct"] > 0)
                        & (d["volume_ratio_prev20"] <= vol_max)
                    ),
                    "回檔模型不要求突破；主軸是結構支撐與量縮回檔。",
                )
            )
    for filter_id, volume_min, solid, label in [
        ("volume_red_k_vol1.2", 1.2, False, "帶量紅K"),
        ("solid_volume_red_k_vol1.2", 1.2, True, "實體帶量紅K"),
        ("solid_volume_red_k_vol1.5", 1.5, True, "實體強量紅K"),
    ]:
        specs.append(
            RuleSpec(
                "price_pullback_23ema",
                "股價回檔模型",
                filter_id,
                f"production proxy replay + {label} + 量比 >= {volume_min:g}",
                "research_only_not_pdf_core",
                lambda d, volume_min=volume_min, solid=solid: price_pullback_volume_red_k_entry(
                    d,
                    volume_min,
                    solid,
                ),
                "研究買點濾網：回檔到23EMA/支撐後，用帶量紅K確認買盤承接；不要求突破，也不可寫回 production baseline。",
            )
        )

    hot_theme_groups = {
        "strict_mainstream_any": {"mainstream_supported", "mainstream_overheated"},
        "strict_mainstream_supported": {"mainstream_supported"},
        "strict_mainstream_overheated": {"mainstream_overheated"},
    }
    for group_id, groups in hot_theme_groups.items():
        for low, high, support_high in [(-2.5, 5.0, 8.0), (-4.0, 7.0, 10.0)]:
            specs.append(
                RuleSpec(
                    "hot_theme_pullback",
                    "熱門族群回檔模型",
                    f"{group_id}_ema{low:g}_{high:g}_support{support_high:g}",
                    f"歷史熱門/主流族群狀態 {group_id} + 距 23EMA {low:g}% 至 {high:g}% 或接近20日支撐 {support_high:g}% 內",
                    "pdf_core_model",
                    lambda d, groups=groups, low=low, high=high, support_high=support_high: (
                        d["strict_theme_status_group"].isin(groups)
                        & (
                            between(d["distance_ema23_pct"], low, high)
                            | (
                                (d["range_low_20d_prev"] > 0)
                                & (d["close"] >= d["range_low_20d_prev"] * 0.98)
                                & (d["close"] <= d["range_low_20d_prev"] * (1 + support_high / 100))
                            )
                        )
                    ),
                    "使用 strict no-lookahead 歷史族群狀態近似每日熱門族群標籤；營收不作為必要條件。",
                )
            )

    for tolerance in [5, 10]:
        specs.append(
            RuleSpec(
                "revenue_unreacted_range",
                "營收爆發但股價尚未反應模型",
                f"range23_tol{tolerance}",
                f"股價位於 23 日區間上下 {tolerance}% 內；營收確認由每日模型層欄位提供",
                "pdf_core_model",
                lambda d, tolerance=tolerance: (
                    (d["close"] >= d["range_low_23d_prev"] * (1 - tolerance / 100))
                    & (d["close"] <= d["range_high_23d_prev"] * (1 + tolerance / 100))
                    & (d["range_width_23d_pct"] <= 20)
                ),
                "歷史營收 feature panel 尚未完整，這裡先用價格未反應區間作第一版近似條件。",
            )
        )

    for vol in [1.0, 1.2, 1.5]:
        specs.append(
            RuleSpec(
                "w_bottom_right_side",
                "W底右側模型",
                f"wproxy_vol{vol:g}",
                f"W底近似條件 + 右側結構墊高 + 量比 >= {vol:g}",
                "pdf_core_model",
                lambda d, vol=vol: d["w_bottom_proxy"] & (d["volume_ratio_prev20"] >= vol),
                "W底右側研究近似條件；正式升級仍需要圖形品質確認。",
            )
        )

    for dist in [3, 5]:
        for vol in [1.2, 1.5]:
            specs.append(
                RuleSpec(
                    "near_high_neckline_challenge",
                    "接近前高 / 頸線挑戰模型",
                    f"near{dist}_vol{vol:g}",
                    f"距 60 日高點下方 {dist}% 內 + 量比 >= {vol:g} + 23EMA 向上",
                    "research_only_not_pdf_core",
                    lambda d, dist=dist, vol=vol: (
                        between(d["near_60d_high_pct"], -dist, 0)
                        & (d["volume_ratio_prev20"] >= vol)
                        & (d["ema23_slope_5d_pct"] > 0)
                    ),
                    "用來提前 1 到 5 個交易日觀察突破前壓力挑戰；不是嚴格突破模型。",
                )
            )

    for window in [20, 30]:
        for near in [3, 5]:
            for vol in [1.2, 1.5]:
                specs.append(
                    RuleSpec(
                        "platform_strengthening",
                        "平台整理轉強模型",
                        f"w{window}_near{near}_vol{vol:g}",
                        f"{window}日區間寬度 <= 18% + 距區間上緣 {near}% 內 + 量比 >= {vol:g} + 實體紅K",
                        "research_only_not_pdf_core",
                        lambda d, window=window, near=near, vol=vol: (
                            (d[f"range_width_{window}d_pct"] <= 18)
                            & between(d[f"distance_to_range_high_{window}d_pct"], -near, 1.5)
                            & (d["volume_ratio_prev20"] >= vol)
                            & d["solid_red_candle"]
                        ),
                        "平台模型尋找波動收斂後、接近上緣時量能回升的型態。",
                    )
                )

    for vol in [1.0, 1.2, 1.5]:
        specs.append(
            RuleSpec(
                "pullback_short_reclaim",
                "回檔後短線轉強模型",
                f"prior20up_reclaim_vol{vol:g}",
                f"前 20 日漲幅 >= 10% + 距 23EMA -1% 至 6% + MACD 柱狀體 > 0 + 量比 >= {vol:g}",
                "pdf_core_model",
                lambda d, vol=vol: (
                    (d["return_20d_pct"] >= 10)
                    & between(d["distance_ema23_pct"], -1, 6)
                    & trueish(d["macd_hist_gt0"])
                    & (d["volume_ratio_prev20"] >= vol)
                ),
                "尋找前段上漲後回檔未破結構、並重新恢復短線動能的股票。",
            )
        )

    for consecutive in [1, 2, 3]:
        specs.append(
            RuleSpec(
                "tdcc_stealth_accumulation",
                "TDCC潛伏吸籌模型",
                f"tdcc_up{consecutive}_range10",
                f"TDCC 連續增加週數 >= {consecutive} + 股價位於 23 日區間上下 10% 內 + 20 日漲幅 <= 20%",
                "pdf_core_model",
                lambda d, consecutive=consecutive: (
                    trueish(d["tdcc_history_available"])
                    & (d["tdcc_consecutive_up_weeks"] >= consecutive)
                    & (d["close"] >= d["range_low_23d_prev"] * 0.90)
                    & (d["close"] <= d["range_high_23d_prev"] * 1.10)
                    & (d["return_20d_pct"] <= 20)
                ),
                "目前使用本地 TDCC 歷史資料；完整歷史 phase panel 可用後再升級 phase 篩選。",
            )
        )

    specs.extend(
        [
            RuleSpec(
                "tdcc_short_term_continuation_d5_d10",
                "TDCC短線延續模型 D+5/D+10",
                "all_thresholds_up_ret5_10_30_macd",
                "四級距同步增加 + 5日漲幅 10% 至 30% + MACD 柱狀體 > 0",
                "pdf_core_model",
                lambda d: (
                    trueish(d["tdcc_history_available"])
                    & trueish(d["all_thresholds_up"])
                    & between(d["return_5d_pct"], 10, 30)
                    & trueish(d["macd_hist_gt0"])
                ),
                "短線延續專項，不是低位吸籌模型。",
            ),
            RuleSpec(
                "tdcc_short_term_continuation_d5_d10",
                "TDCC短線延續模型 D+5/D+10",
                "high_thresholds_ret5_10_30_ret10_20_50_kd",
                "高級距增加 + 5日漲幅 10% 至 30% + 10日漲幅 20% 至 50% + KD 多方但未過熱",
                "pdf_core_model",
                lambda d: (
                    trueish(d["tdcc_history_available"])
                    & trueish(d["high_thresholds_up"])
                    & between(d["return_5d_pct"], 10, 30)
                    & between(d["return_10d_pct"], 20, 50)
                    & trueish(d["kd_bullish_not_overheated"])
                ),
                "短線延續研究；報酬統計使用訊號日隔天開盤到 D+1 至 D+10。",
            ),
            RuleSpec(
                "short_term_surge_d5_d10",
                "短線急漲 D+5/D+10 研究",
                "ret5_10_30_vol5_ge1_5_macd",
                "5日漲幅 10% 至 30% + 5日平均量比 >= 1.5 + MACD 柱狀體 > 0",
                "research_only_not_pdf_core",
                lambda d: (
                    between(d["return_5d_pct"], 10, 30)
                    & (d["start_5d_avg_volume_ratio_vs_prev20"] >= 1.5)
                    & trueish(d["macd_hist_gt0"])
                ),
                "動能研究名單；進場假設必須使用訊號日後下一交易日開盤。",
            ),
        ]
    )

    for vol in [3.0, 5.0, 10.0]:
        specs.append(
            RuleSpec(
                "explosive_volume_red_candle",
                "爆天量紅K研究",
                f"vol{vol:g}_solid_red",
                f"量比 >= {vol:g} + 實體紅K + 上影線小 + 收盤接近日高",
                "research_only_not_pdf_core",
                lambda d, vol=vol: (d["volume_ratio_prev20"] >= vol) & d["solid_red_candle"],
                "研究用模型，參數驗證成熟前不納入核心 PDF 推薦模型。",
            )
        )

    return specs

def summarize_rule(df: pd.DataFrame, spec: RuleSpec) -> tuple[dict[str, object], list[dict[str, object]]]:
    mask = spec.condition(df).fillna(False)
    picked = df[mask].copy()
    n = len(picked)
    unique_stocks = picked["stock_id"].nunique() if n else 0
    detail_rows: list[dict[str, object]] = []
    best_horizon = ""
    best_avg = -math.inf
    best_win = 0.0
    for h in HORIZONS:
        close_col = f"next_open_to_d{h}_close_return_pct"
        high_col = f"next_open_to_d{h}_high_return_pct"
        if close_col not in picked.columns:
            continue
        valid = picked.dropna(subset=[close_col])
        mature = len(valid)
        win = float((valid[close_col] > 0).mean() * 100.0) if mature else math.nan
        avg = float(valid[close_col].mean()) if mature else math.nan
        med = float(valid[close_col].median()) if mature else math.nan
        high_avg = float(valid[high_col].mean()) if mature and high_col in valid.columns else math.nan
        high_win_5 = float((valid[high_col] >= 5).mean() * 100.0) if mature and high_col in valid.columns else math.nan
        if mature and not math.isnan(avg) and avg > best_avg and h <= 10:
            best_avg = avg
            best_horizon = f"D+{h}"
            best_win = win
        detail_rows.append(
            {
                "model_id": spec.model_id,
                "model_name_zh": spec.model_name_zh,
                "parameter_set_id": spec.parameter_set_id,
                "horizon": f"D+{h}",
                "entry_basis": "signal_date_next_open",
                "exit_close_basis": f"D+{h}_close",
                "exit_high_basis": f"D+{h}_intraday_high",
                "mature_count": mature,
                "close_win_rate_pct": round(win, 2) if not math.isnan(win) else "",
                "avg_close_return_pct": round(avg, 2) if not math.isnan(avg) else "",
                "median_close_return_pct": round(med, 2) if not math.isnan(med) else "",
                "avg_high_return_pct": round(high_avg, 2) if not math.isnan(high_avg) else "",
                "high_5pct_hit_rate_pct": round(high_win_5, 2) if not math.isnan(high_win_5) else "",
            }
        )

    summary = {
        "generated_at": now_text(),
        "model_id": spec.model_id,
        "model_name_zh": spec.model_name_zh,
        "parameter_set_id": spec.parameter_set_id,
        "parameter_summary": spec.parameter_summary,
        "parameter_role": spec.parameter_role,
        "production_parity_status": spec.production_parity_status,
        "parity_blocker": spec.parity_blocker,
        "variant_of": spec.variant_of,
        "pdf_visibility": spec.pdf_visibility,
        "entry_basis": "signal_date_next_open",
        "selected_stock_days": n,
        "selected_unique_stocks": unique_stocks,
        "best_close_horizon_d1_d10": best_horizon,
        "best_close_win_rate_pct": round(best_win, 2) if best_horizon else "",
        "best_avg_close_return_pct": round(best_avg, 2) if best_horizon else "",
        "sample_status": sample_status(n),
        "apply_status": "candidate_parameter_review" if n >= MIN_REVIEW_SAMPLE else "do_not_apply_insufficient_sample",
        "notes": spec.notes,
    }
    for h in [1, 2, 3, 5, 10, 20]:
        row = next((r for r in detail_rows if r["horizon"] == f"D+{h}"), None)
        summary[f"d{h}_mature_count"] = row["mature_count"] if row else 0
        summary[f"d{h}_close_win_rate_pct"] = row["close_win_rate_pct"] if row else ""
        summary[f"d{h}_avg_close_return_pct"] = row["avg_close_return_pct"] if row else ""
        summary[f"d{h}_avg_high_return_pct"] = row["avg_high_return_pct"] if row else ""
    return summary, detail_rows


def current_production_core_models() -> pd.DataFrame:
    current = build_parameter_table(build_specs()).copy()
    current = current[current["pdf_visibility"].eq("pdf_core_model")].copy()
    return current.drop_duplicates("model_id", keep="first").reset_index(drop=True)


def build_model_parity(summary: pd.DataFrame) -> pd.DataFrame:
    production = current_production_core_models()
    baseline = summary[summary["parameter_role"].eq("production_baseline")].copy()
    rows: list[dict[str, object]] = []
    for _, prod in production.iterrows():
        model_id = str(prod.get("model_id", ""))
        base_rows = baseline[baseline["model_id"].eq(model_id)].copy()
        variant_rows = summary[
            summary["model_id"].eq(model_id) & ~summary["parameter_role"].eq("production_baseline")
        ].copy()
        if base_rows.empty:
            status = "missing_production_baseline"
            baseline_ids = ""
            blockers = "research rule_specs() has no production_baseline row for this production core model"
            selected_days = ""
            unique_stocks = ""
        else:
            statuses = sorted(set(base_rows["production_parity_status"].astype(str)))
            if statuses == ["production_parity"]:
                status = "production_parity"
            elif "proxy_only" in statuses:
                status = "proxy_only"
            else:
                status = "production_proxy"
            baseline_ids = ",".join(base_rows["parameter_set_id"].astype(str))
            blockers = "; ".join(
                sorted(
                    {
                        str(value).strip()
                        for value in base_rows["parity_blocker"].fillna("")
                        if str(value).strip()
                    }
                )
            )
            if model_id == "w_bottom_right_side" and status == "production_parity":
                selected_days = int(W_BOTTOM_APPROVAL_METRICS["sample_size"])
                unique_stocks = int(W_BOTTOM_APPROVAL_METRICS["unique_stock_count"])
            elif model_id == "neckline_volume_breakout_confirmation" and status == "production_parity":
                selected_days = int(NECKLINE_APPROVAL_METRICS["tradable_entry_count"])
                unique_stocks = int(NECKLINE_APPROVAL_METRICS["unique_stock_count"])
            else:
                selected_days = int(pd.to_numeric(base_rows["selected_stock_days"], errors="coerce").fillna(0).sum())
                unique_stocks = int(pd.to_numeric(base_rows["selected_unique_stocks"], errors="coerce").fillna(0).max())
        rows.append(
            {
                "generated_at": now_text(),
                "model_id": model_id,
                "model_name_zh": prod.get("model_name_zh", ""),
                "production_pdf_visibility": prod.get("pdf_visibility", ""),
                "production_parameter_status": prod.get("parameter_status", ""),
                "production_main_conditions": prod.get("main_conditions", ""),
                "research_baseline_status": status,
                "research_baseline_parameter_set_id": baseline_ids,
                "research_variant_count": len(variant_rows),
                "baseline_selected_stock_days": selected_days,
                "baseline_selected_unique_stocks": unique_stocks,
                "parity_blocker": blockers,
                "completion_rule": (
                    "usable_as_exact_baseline"
                    if status == "production_parity"
                    else "usable_for_relative_research_only_until_blocker_resolved"
                ),
            }
        )
    return pd.DataFrame(rows)


PRICE_PULLBACK_OPERATION_CANDIDATES = [
    {
        "operation_candidate_id": "d10_close_target5_loss3",
        "holding_window_days": 10,
        "target_basis": "D+10_close",
        "target_return_pct": 5.0,
        "stop_basis": "D+10_close",
        "stop_return_pct": -3.0,
        "entry_rule": "signal_date_next_open after price_pullback_23ema production proxy replay",
        "exit_rule": "research close-only target at D+10; no intraday path ordering",
    },
    {
        "operation_candidate_id": "d20_close_target5_loss3",
        "holding_window_days": 20,
        "target_basis": "D+20_close",
        "target_return_pct": 5.0,
        "stop_basis": "D+20_close",
        "stop_return_pct": -3.0,
        "entry_rule": "signal_date_next_open after price_pullback_23ema production proxy replay",
        "exit_rule": "research close-only target at D+20; no intraday path ordering",
    },
    {
        "operation_candidate_id": "d20_high_target5_low_stop5_order_unresolved",
        "holding_window_days": 20,
        "target_basis": "max_D+20_intraday_high",
        "target_return_pct": 5.0,
        "stop_basis": "min_D+20_intraday_low",
        "stop_return_pct": -5.0,
        "entry_rule": "signal_date_next_open after price_pullback_23ema production proxy replay",
        "exit_rule": "research high/low target-stop study; same-window hit order is unresolved",
    },
    {
        "operation_candidate_id": "d20_high_target8_low_stop5_order_unresolved",
        "holding_window_days": 20,
        "target_basis": "max_D+20_intraday_high",
        "target_return_pct": 8.0,
        "stop_basis": "min_D+20_intraday_low",
        "stop_return_pct": -5.0,
        "entry_rule": "signal_date_next_open after price_pullback_23ema production proxy replay",
        "exit_rule": "research high/low target-stop study; same-window hit order is unresolved",
    },
]


PRICE_PULLBACK_ENTRY_FILTERS = [
    {
        "entry_filter_id": "baseline_replay",
        "entry_signal_rule": "no extra candle/volume confirmation beyond production proxy replay",
        "condition": lambda d: bool_series(d, True),
    },
    {
        "entry_filter_id": "volume_red_k_vol1.2",
        "entry_signal_rule": "bullish red K with volume_ratio_prev20 >= 1.2",
        "condition": lambda d: price_pullback_red_k_entry_filter(d, 1.2, solid=False),
    },
    {
        "entry_filter_id": "solid_volume_red_k_vol1.2",
        "entry_signal_rule": "solid red K with volume_ratio_prev20 >= 1.2",
        "condition": lambda d: price_pullback_red_k_entry_filter(d, 1.2, solid=True),
    },
    {
        "entry_filter_id": "solid_volume_red_k_vol1.5",
        "entry_signal_rule": "solid red K with volume_ratio_prev20 >= 1.5",
        "condition": lambda d: price_pullback_red_k_entry_filter(d, 1.5, solid=True),
    },
    {
        "entry_filter_id": "prior_ext20_ema10_runup20_pullback5",
        "entry_signal_rule": "prior 20d high was >=10% above 23EMA, prior 20d range runup >=20%, and signal close is at least 5% below that high",
        "condition": lambda d: price_pullback_prior_extension_filter(d, 20, 10.0, 20.0, 5.0),
    },
    {
        "entry_filter_id": "prior_ext30_ema12_runup25_pullback8",
        "entry_signal_rule": "prior 30d high was >=12% above 23EMA, prior 30d range runup >=25%, and signal close is at least 8% below that high",
        "condition": lambda d: price_pullback_prior_extension_filter(d, 30, 12.0, 25.0, 8.0),
    },
    {
        "entry_filter_id": "prior_ext60_ema15_runup35_pullback10",
        "entry_signal_rule": "prior 60d high was >=15% above 23EMA, prior 60d range runup >=35%, and signal close is at least 10% below that high",
        "condition": lambda d: price_pullback_prior_extension_filter(d, 60, 15.0, 35.0, 10.0),
    },
]


PRICE_PULLBACK_PRIOR_HIGH_STOP_GRID = [
    {
        "stop_reference_id": "ma20",
        "candidate_label": "monthline",
        "stop_reference_name": "current 20MA/monthline",
    },
    {
        "stop_reference_id": "ema23",
        "candidate_label": "ema23",
        "stop_reference_name": "current 23EMA",
    },
    {
        "stop_reference_id": "lower_ma20_ema23",
        "candidate_label": "lower_ma20_ema23",
        "stop_reference_name": "lower of current 20MA and 23EMA",
    },
]
PRICE_PULLBACK_PRIOR_HIGH_TARGET_WINDOWS = [20, 30, 60]
PRICE_PULLBACK_PRIOR_HIGH_STOP_PCTS = [1.0, 2.0, 3.0, 4.0]
PRICE_PULLBACK_PRIOR_HIGH_STOP_CONSECUTIVE_DAYS = [2, 3, 4]


def _price_pullback_prior_high_stop_candidates() -> list[dict[str, object]]:
    candidates: list[dict[str, object]] = []
    for target_window in PRICE_PULLBACK_PRIOR_HIGH_TARGET_WINDOWS:
        for ref in PRICE_PULLBACK_PRIOR_HIGH_STOP_GRID:
            for stop_pct in PRICE_PULLBACK_PRIOR_HIGH_STOP_PCTS:
                for consecutive_days in PRICE_PULLBACK_PRIOR_HIGH_STOP_CONSECUTIVE_DAYS:
                    pct_label = f"{stop_pct:g}"
                    candidates.append(
                        {
                            "operation_module_candidate_id": (
                                f"next_open_prev{target_window}_high_breakout_"
                                f"{ref['candidate_label']}_stop{pct_label}pct_{consecutive_days}d_d20_close_exit"
                            ),
                            "target_rule_id": "prior_high_breakout",
                            "target_lookback_days": target_window,
                            "target_return_pct": "",
                            "stop_rule_id": "sustained_close_below_reference_pct",
                            "stop_reference_id": ref["stop_reference_id"],
                            "stop_reference_name": ref["stop_reference_name"],
                            "stop_buffer_pct": stop_pct,
                            "stop_consecutive_days": consecutive_days,
                            "stop_return_pct": "",
                            "holding_window_days": 20,
                            "entry_rule_id": "signal_date_next_open",
                            "buy_point_rule": (
                                "Buy next open only when the price_pullback_23ema signal and the entry filter both hold on signal date."
                            ),
                            "stop_rule": (
                                f"Failure stop when close stays at least {pct_label}% below "
                                f"the {ref['stop_reference_name']} for {consecutive_days} consecutive trading days."
                            ),
                            "exit_rule": (
                                f"If no previous {target_window}-day high breakout or sustained reference stop appears by D+20, "
                                "exit at D+20 close."
                            ),
                        }
                    )
    return candidates


PRICE_PULLBACK_OPERATION_MODULE_CANDIDATES = [
    {
        "operation_module_candidate_id": "next_open_tp5_intraday_stop5_d20_close_exit",
        "target_rule_id": "intraday_return_pct",
        "target_return_pct": 5.0,
        "stop_rule_id": "intraday_low_stop5",
        "stop_return_pct": -5.0,
        "holding_window_days": 20,
        "entry_rule_id": "signal_date_next_open",
        "buy_point_rule": "Buy next open only when the price_pullback_23ema signal and the entry filter both hold on signal date.",
        "stop_rule": "Failure stop when intraday low first reaches -5% from next-open entry.",
        "exit_rule": "If no target or stop appears by D+20, exit at D+20 close.",
    },
    {
        "operation_module_candidate_id": "next_open_tp5_structure_stop_d20_close_exit",
        "target_rule_id": "intraday_return_pct",
        "target_return_pct": 5.0,
        "stop_rule_id": "close_below_23ema_or_support_2pct",
        "stop_return_pct": "",
        "holding_window_days": 20,
        "entry_rule_id": "signal_date_next_open",
        "buy_point_rule": "Buy next open only when the price_pullback_23ema signal and the entry filter both hold on signal date.",
        "stop_rule": "Failure stop when a close first falls below the higher of signal-day 23EMA/support references by 2%.",
        "exit_rule": "If no target or structure stop appears by D+20, exit at D+20 close.",
    },
    {
        "operation_module_candidate_id": "next_open_tp8_intraday_stop5_d20_close_exit",
        "target_rule_id": "intraday_return_pct",
        "target_return_pct": 8.0,
        "stop_rule_id": "intraday_low_stop5",
        "stop_return_pct": -5.0,
        "holding_window_days": 20,
        "entry_rule_id": "signal_date_next_open",
        "buy_point_rule": "Buy next open only when the price_pullback_23ema signal and the entry filter both hold on signal date.",
        "stop_rule": "Failure stop when intraday low first reaches -5% from next-open entry.",
        "exit_rule": "If no target or stop appears by D+20, exit at D+20 close.",
    },
    {
        "operation_module_candidate_id": "next_open_tp8_structure_stop_d20_close_exit",
        "target_rule_id": "intraday_return_pct",
        "target_return_pct": 8.0,
        "stop_rule_id": "close_below_23ema_or_support_2pct",
        "stop_return_pct": "",
        "holding_window_days": 20,
        "entry_rule_id": "signal_date_next_open",
        "buy_point_rule": "Buy next open only when the price_pullback_23ema signal and the entry filter both hold on signal date.",
        "stop_rule": "Failure stop when a close first falls below the higher of signal-day 23EMA/support references by 2%.",
        "exit_rule": "If no target or structure stop appears by D+20, exit at D+20 close.",
    },
    *_price_pullback_prior_high_stop_candidates(),
]


PRICE_PULLBACK_FEATURE_CONFIRMATION_OPERATION_ID = (
    "next_open_prev20_high_breakout_lower_ma20_ema23_stop4pct_4d_d20_close_exit"
)

PRICE_PULLBACK_FEATURE_CONFIRMATION_FILTERS = [
    {
        "feature_filter_id": "baseline_replay",
        "feature_family": "baseline",
        "feature_rule": "no extra feature confirmation beyond production proxy replay",
        "feature_test_status": "tested_point_in_time",
        "data_status": "available_point_in_time_research_frame",
        "condition": lambda d: bool_series(d, True),
    },
    {
        "feature_filter_id": "prior_ext20_ema10_runup20_pullback5",
        "feature_family": "prior_extension",
        "feature_rule": "prior 20d high was >=10% above 23EMA, prior 20d range runup >=20%, signal close at least 5% below that high",
        "feature_test_status": "tested_point_in_time",
        "data_status": "available_point_in_time_research_frame",
        "condition": lambda d: price_pullback_prior_extension_filter(d, 20, 10.0, 20.0, 5.0),
    },
    {
        "feature_filter_id": "macd_hist_gt0",
        "feature_family": "technical",
        "feature_rule": "MACD histogram above zero on signal date",
        "feature_test_status": "tested_point_in_time",
        "data_status": "available_point_in_time_research_frame",
        "condition": lambda d: trueish_column(d, "macd_hist_gt0"),
    },
    {
        "feature_filter_id": "kd_bullish_not_overheated",
        "feature_family": "technical",
        "feature_rule": "KD bullish but not overheated on signal date",
        "feature_test_status": "tested_point_in_time",
        "data_status": "available_point_in_time_research_frame",
        "condition": lambda d: trueish_column(d, "kd_bullish_not_overheated"),
    },
    {
        "feature_filter_id": "macd_kd_confirm",
        "feature_family": "technical",
        "feature_rule": "MACD histogram above zero and KD bullish-not-overheated both hold",
        "feature_test_status": "tested_point_in_time",
        "data_status": "available_point_in_time_research_frame",
        "condition": price_pullback_macd_kd_confirm_filter,
    },
    {
        "feature_filter_id": "rsi14_40_70",
        "feature_family": "technical",
        "feature_rule": "RSI14 between 40 and 70 on signal date",
        "feature_test_status": "tested_point_in_time",
        "data_status": "available_point_in_time_research_frame",
        "condition": lambda d: between(numeric_column(d, "rsi14"), 40.0, 70.0).fillna(False),
    },
    {
        "feature_filter_id": "bb_width_not_extreme",
        "feature_family": "technical",
        "feature_rule": "Bollinger bandwidth percentile is not extreme",
        "feature_test_status": "tested_point_in_time",
        "data_status": "available_point_in_time_research_frame",
        "condition": lambda d: trueish_column(d, "bb_width_not_extreme"),
    },
    {
        "feature_filter_id": "obv_above_ma20",
        "feature_family": "technical_volume",
        "feature_rule": "OBV above OBV MA20 on signal date",
        "feature_test_status": "tested_point_in_time",
        "data_status": "computed_from_point_in_time_price_volume",
        "condition": price_pullback_obv_above_ma20_filter,
    },
    {
        "feature_filter_id": "tdcc_history_available",
        "feature_family": "chip",
        "feature_rule": "TDCC history is available for point-in-time join",
        "feature_test_status": "tested_point_in_time",
        "data_status": "available_point_in_time_research_frame",
        "condition": lambda d: trueish_column(d, "tdcc_history_available"),
    },
    {
        "feature_filter_id": "tdcc_consecutive_up_weeks_ge1",
        "feature_family": "chip",
        "feature_rule": "TDCC consecutive up weeks >= 1",
        "feature_test_status": "tested_point_in_time",
        "data_status": "available_point_in_time_research_frame",
        "condition": lambda d: trueish_column(d, "tdcc_history_available")
        & (numeric_column(d, "tdcc_consecutive_up_weeks") >= 1.0),
    },
    {
        "feature_filter_id": "tdcc_high_thresholds_up",
        "feature_family": "chip",
        "feature_rule": "large-holder TDCC high thresholds increased",
        "feature_test_status": "tested_point_in_time",
        "data_status": "available_point_in_time_research_frame",
        "condition": price_pullback_tdcc_high_thresholds_up_filter,
    },
    {
        "feature_filter_id": "tdcc_all_thresholds_up",
        "feature_family": "chip",
        "feature_rule": "all TDCC holder thresholds increased together",
        "feature_test_status": "tested_point_in_time",
        "data_status": "available_point_in_time_research_frame",
        "condition": lambda d: trueish_column(d, "tdcc_history_available") & trueish_column(d, "all_thresholds_up"),
    },
    {
        "feature_filter_id": "return20_0_25",
        "feature_family": "risk_control",
        "feature_rule": "20d return is between 0% and 25% to avoid deeply weak or excessively extended names",
        "feature_test_status": "tested_point_in_time",
        "data_status": "available_point_in_time_research_frame",
        "condition": price_pullback_return20_balanced_filter,
    },
    {
        "feature_filter_id": "pattern45_bull_pullback",
        "feature_family": "price_structure",
        "feature_rule": "45d return >=8%, 45d range width >=18%, and signal close sits in the 35%-80% zone of the prior 45d range",
        "feature_test_status": "tested_point_in_time",
        "data_status": "computed_from_point_in_time_price_history",
        "condition": price_pullback_45d_bullish_pullback_filter,
    },
    {
        "feature_filter_id": "tdcc_high_thresholds_up_return20_0_25",
        "feature_family": "combo_chip_risk_control",
        "feature_rule": "large-holder TDCC high thresholds increased and 20d return is between 0% and 25%",
        "feature_test_status": "tested_point_in_time",
        "data_status": "available_point_in_time_research_frame",
        "condition": lambda d: price_pullback_tdcc_high_thresholds_up_filter(d)
        & price_pullback_return20_balanced_filter(d),
    },
    {
        "feature_filter_id": "tdcc_consecutive_up_ge1_return20_0_25",
        "feature_family": "combo_chip_risk_control",
        "feature_rule": "TDCC consecutive up weeks >=1 and 20d return is between 0% and 25%",
        "feature_test_status": "tested_point_in_time",
        "data_status": "available_point_in_time_research_frame",
        "condition": lambda d: price_pullback_tdcc_consecutive_up_ge1_filter(d)
        & price_pullback_return20_balanced_filter(d),
    },
    {
        "feature_filter_id": "tdcc_high_thresholds_up_obv_above_ma20",
        "feature_family": "combo_chip_technical_volume",
        "feature_rule": "large-holder TDCC high thresholds increased and OBV above OBV MA20",
        "feature_test_status": "tested_point_in_time",
        "data_status": "available_point_in_time_research_frame",
        "condition": lambda d: price_pullback_tdcc_high_thresholds_up_filter(d)
        & price_pullback_obv_above_ma20_filter(d),
    },
    {
        "feature_filter_id": "tdcc_high_thresholds_up_macd_kd_confirm",
        "feature_family": "combo_chip_technical",
        "feature_rule": "large-holder TDCC high thresholds increased plus MACD/KD confirmation",
        "feature_test_status": "tested_point_in_time",
        "data_status": "available_point_in_time_research_frame",
        "condition": lambda d: price_pullback_tdcc_high_thresholds_up_filter(d)
        & price_pullback_macd_kd_confirm_filter(d),
    },
    {
        "feature_filter_id": "tdcc_high_thresholds_up_return20_0_25_obv_above_ma20",
        "feature_family": "combo_chip_risk_control_technical_volume",
        "feature_rule": "large-holder TDCC high thresholds increased, 20d return is between 0% and 25%, and OBV above OBV MA20",
        "feature_test_status": "tested_point_in_time",
        "data_status": "available_point_in_time_research_frame",
        "condition": lambda d: price_pullback_tdcc_high_thresholds_up_filter(d)
        & price_pullback_return20_balanced_filter(d)
        & price_pullback_obv_above_ma20_filter(d),
    },
    {
        "feature_filter_id": "revenue_positive_or_strong",
        "feature_family": "revenue",
        "feature_rule": "candidate revenue should be positive/strong as gate or add-score candidate",
        "feature_test_status": "blocked_data_panel_incomplete",
        "data_status": "historical revenue panel is not complete enough for point-in-time replay in this research frame",
        "condition": None,
    },
    {
        "feature_filter_id": "market_background_regime",
        "feature_family": "market_background",
        "feature_rule": "market regime/risk background filter requires dated market feature join by signal date and market/index mapping",
        "feature_test_status": "deferred_join_required",
        "data_status": "market feature panel exists, but this artifact does not yet join it into stock-day rows",
        "condition": None,
    },
]


def _rate(count: int, total: int) -> float | str:
    if total <= 0:
        return ""
    return round(count / total * 100.0, 2)


def build_price_pullback_operation_research(df: pd.DataFrame) -> pd.DataFrame:
    base_mask = current_price_pullback_baseline_proxy(df).fillna(False)
    rows: list[dict[str, object]] = []
    generated_at = now_text()
    for entry_filter in PRICE_PULLBACK_ENTRY_FILTERS:
        filter_mask = entry_filter["condition"](df).fillna(False)
        picked = df[base_mask & filter_mask].copy()
        for candidate in PRICE_PULLBACK_OPERATION_CANDIDATES:
            h = int(candidate["holding_window_days"])
            close_col = f"next_open_to_d{h}_close_return_pct"
            high_col = f"next_open_to_d{h}_high_return_pct"
            low_col = f"next_open_to_d{h}_low_return_pct"
            required = [close_col]
            if str(candidate["target_basis"]).startswith("max_"):
                required.extend([high_col, low_col])
            valid = (
                picked.dropna(subset=required).copy()
                if all(col in picked.columns for col in required)
                else picked.iloc[0:0].copy()
            )
            mature = len(valid)

            target = float(candidate["target_return_pct"])
            stop = float(candidate["stop_return_pct"])
            if mature and str(candidate["target_basis"]).startswith("max_"):
                target_hit = valid[high_col] >= target
                stop_hit = valid[low_col] <= stop
                ambiguous = target_hit & stop_hit
                win = target_hit & ~stop_hit
                loss = stop_hit & ~target_hit
                neutral = ~(win | loss | ambiguous)
                avg_high = float(valid[high_col].mean())
                high5_hit = float((valid[high_col] >= 5.0).mean() * 100.0)
            elif mature:
                win = valid[close_col] >= target
                loss = valid[close_col] <= stop
                ambiguous = bool_series(valid)
                neutral = ~(win | loss)
                avg_high = math.nan
                high5_hit = math.nan
            else:
                win = loss = neutral = ambiguous = bool_series(valid)
                avg_high = math.nan
                high5_hit = math.nan

            win_count = int(win.sum()) if mature else 0
            loss_count = int(loss.sum()) if mature else 0
            neutral_count = int(neutral.sum()) if mature else 0
            ambiguous_count = int(ambiguous.sum()) if mature else 0
            avg_close = float(valid[close_col].mean()) if mature else math.nan
            median_close = float(valid[close_col].median()) if mature else math.nan
            rows.append(
                {
                    "generated_at": generated_at,
                    "model_id": "price_pullback_23ema",
                    "model_name_zh": "股價回檔模型",
                    "research_baseline_parameter_set_id": "production_current_proxy",
                    "research_baseline_status": "production_proxy",
                    "entry_filter_id": entry_filter["entry_filter_id"],
                    "entry_signal_rule": entry_filter["entry_signal_rule"],
                    "operation_candidate_id": candidate["operation_candidate_id"],
                    "advisory_status": "not_production_ready_research_only",
                    "approved_for_daily": False,
                    "entry_rule": f"{candidate['entry_rule']} + {entry_filter['entry_signal_rule']}",
                    "target_rule": f"{candidate['target_basis']} >= {target:g}%",
                    "stop_rule": f"{candidate['stop_basis']} <= {stop:g}%",
                    "exit_rule": candidate["exit_rule"],
                    "outcome_rule": "win/neutral/loss research labels only; not a validated trading module",
                    "holding_window_days": h,
                    "selected_stock_days": len(picked),
                    "selected_unique_stocks": picked["stock_id"].nunique() if not picked.empty else 0,
                    "mature_count": mature,
                    "win_count": win_count,
                    "neutral_count": neutral_count,
                    "loss_count": loss_count,
                    "ambiguous_order_count": ambiguous_count,
                    "win_rate_pct": _rate(win_count, mature),
                    "neutral_rate_pct": _rate(neutral_count, mature),
                    "loss_rate_pct": _rate(loss_count, mature),
                    "ambiguous_order_rate_pct": _rate(ambiguous_count, mature),
                    "avg_close_return_pct": round(avg_close, 2) if not math.isnan(avg_close) else "",
                    "median_close_return_pct": round(median_close, 2) if not math.isnan(median_close) else "",
                    "avg_high_return_pct": round(avg_high, 2) if not math.isnan(avg_high) else "",
                    "high_5pct_hit_rate_pct": round(high5_hit, 2) if not math.isnan(high5_hit) else "",
                    "path_order_limitation": (
                        "high/low target-stop studies cannot determine whether target or stop happened first inside the holding window"
                        if str(candidate["target_basis"]).startswith("max_")
                        else "close-only study does not model intraday stop execution"
                    ),
                    "promotion_blocker": "requires exact daily candidate row parity plus validated buy/sell/stop operation module",
                }
            )
    return pd.DataFrame(rows)


def write_price_pullback_operation_research(operation: pd.DataFrame) -> None:
    write_csv(operation, PRICE_PULLBACK_OPERATION_CSV)
    write_csv(operation, PRICE_PULLBACK_OPERATION_HISTORY_CSV)
    write_csv(operation, DOCS_PRICE_PULLBACK_OPERATION_CSV)
    lines = [
        "# Price Pullback 23EMA Operation Research",
        "",
        f"- generated_at: `{now_text()}`",
        "- model_id: `price_pullback_23ema`",
        "- status: `not_production_ready_research_only`",
        "- entry_basis: `signal_date_next_open` after production proxy replay",
        "- scope: advisory operation candidates only; this does not approve daily production use",
        "- blocker: exact daily candidate row parity and validated buy/sell/stop module are still required before promotion",
        "",
        markdown_table(
            operation,
            [
                "entry_filter_id",
                "operation_candidate_id",
                "selected_stock_days",
                "mature_count",
                "win_rate_pct",
                "neutral_rate_pct",
                "loss_rate_pct",
                "ambiguous_order_rate_pct",
                "avg_close_return_pct",
                "avg_high_return_pct",
                "high_5pct_hit_rate_pct",
                "promotion_blocker",
            ],
            limit=50,
        ),
    ]
    PRICE_PULLBACK_OPERATION_MD.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8", newline="\n")
    DOCS_PRICE_PULLBACK_OPERATION_MD.write_text(
        PRICE_PULLBACK_OPERATION_MD.read_text(encoding="utf-8"),
        encoding="utf-8",
        newline="\n",
    )


def _first_hit_day(hits: pd.DataFrame) -> pd.Series:
    arr = hits.fillna(False).to_numpy(dtype=bool)
    if arr.size == 0:
        return pd.Series(dtype=float, index=hits.index)
    any_hit = arr.any(axis=1)
    first_idx = arr.argmax(axis=1) + 1
    return pd.Series(np.where(any_hit, first_idx, math.nan), index=hits.index, dtype=float)


def _first_consecutive_hit_day(hits: pd.DataFrame, consecutive_days: int) -> pd.Series:
    if consecutive_days <= 1:
        return _first_hit_day(hits)
    arr = hits.fillna(False).to_numpy(dtype=bool)
    if arr.size == 0:
        return pd.Series(dtype=float, index=hits.index)
    result = np.full(arr.shape[0], math.nan)
    for row_idx, row in enumerate(arr):
        streak = 0
        for day_idx, hit in enumerate(row, start=1):
            streak = streak + 1 if hit else 0
            if streak >= consecutive_days:
                result[row_idx] = day_idx
                break
    return pd.Series(result, index=hits.index, dtype=float)


def _mean_or_blank(series: pd.Series) -> float | str:
    clean = pd.to_numeric(series, errors="coerce").dropna()
    if clean.empty:
        return ""
    return round(float(clean.mean()), 2)


def build_price_pullback_time_cost_backtest(df: pd.DataFrame) -> pd.DataFrame:
    base_mask = current_price_pullback_baseline_proxy(df).fillna(False)
    high_cols = [f"next_open_to_d{day}_day_high_return_pct" for day in range(1, TIME_COST_HORIZON_DAYS + 1)]
    low_cols = [f"next_open_to_d{day}_day_low_return_pct" for day in range(1, TIME_COST_HORIZON_DAYS + 1)]
    rows: list[dict[str, object]] = []
    generated_at = now_text()
    for entry_filter in PRICE_PULLBACK_ENTRY_FILTERS:
        filter_mask = entry_filter["condition"](df).fillna(False)
        picked = df[base_mask & filter_mask].copy()
        valid = (
            picked.dropna(subset=high_cols + low_cols).copy()
            if all(col in picked.columns for col in high_cols + low_cols)
            else picked.iloc[0:0].copy()
        )
        mature = len(valid)
        if mature:
            target_day = _first_hit_day(valid[high_cols] >= TIME_COST_TARGET_PCT)
            stop_day = _first_hit_day(valid[low_cols] <= TIME_COST_STOP_PCT)
            target_before_stop = target_day.notna() & (stop_day.isna() | (target_day < stop_day))
            stop_before_target = stop_day.notna() & (target_day.isna() | (stop_day < target_day))
            same_day = target_day.notna() & stop_day.notna() & target_day.eq(stop_day)
            no_decision = target_day.isna() & stop_day.isna()
            first_decision_day = pd.Series(TIME_COST_HORIZON_DAYS, index=valid.index, dtype=float)
            first_decision_day = first_decision_day.mask(target_before_stop, target_day)
            first_decision_day = first_decision_day.mask(stop_before_target, stop_day)
            first_decision_day = first_decision_day.mask(same_day, target_day)
        else:
            target_day = stop_day = first_decision_day = pd.Series(dtype=float, index=valid.index)
            target_before_stop = stop_before_target = same_day = no_decision = bool_series(valid)

        target_before_count = int(target_before_stop.sum()) if mature else 0
        stop_before_count = int(stop_before_target.sum()) if mature else 0
        same_day_count = int(same_day.sum()) if mature else 0
        no_decision_count = int(no_decision.sum()) if mature else 0
        rows.append(
            {
                "generated_at": generated_at,
                "model_id": "price_pullback_23ema",
                "model_name_zh": "股價回檔模型",
                "research_baseline_parameter_set_id": "production_current_proxy",
                "research_baseline_status": "production_proxy",
                "entry_filter_id": entry_filter["entry_filter_id"],
                "entry_signal_rule": entry_filter["entry_signal_rule"],
                "advisory_status": "not_production_ready_research_only",
                "approved_for_daily": False,
                "entry_basis": "signal_date_next_open",
                "target_rule": f"first intraday high >= +{TIME_COST_TARGET_PCT:g}% through D+{TIME_COST_HORIZON_DAYS}",
                "stop_rule": f"first intraday low <= {TIME_COST_STOP_PCT:g}% through D+{TIME_COST_HORIZON_DAYS}",
                "same_day_rule": "if target and stop both hit on the same daily candle, order is unresolved",
                "selected_stock_days": len(picked),
                "selected_unique_stocks": picked["stock_id"].nunique() if not picked.empty else 0,
                "mature_count": mature,
                "target_before_stop_count": target_before_count,
                "stop_before_target_count": stop_before_count,
                "same_day_target_stop_count": same_day_count,
                "no_decision_after_20d_count": no_decision_count,
                "target_before_stop_rate_pct": _rate(target_before_count, mature),
                "stop_before_target_rate_pct": _rate(stop_before_count, mature),
                "same_day_target_stop_rate_pct": _rate(same_day_count, mature),
                "no_decision_after_20d_rate_pct": _rate(no_decision_count, mature),
                "avg_days_to_target_5pct": _mean_or_blank(target_day),
                "avg_days_to_stop_5pct": _mean_or_blank(stop_day),
                "avg_holding_days_if_win": _mean_or_blank(target_day[target_before_stop]) if mature else "",
                "avg_holding_days_if_loss": _mean_or_blank(stop_day[stop_before_target]) if mature else "",
                "avg_first_decision_or_20d_days": _mean_or_blank(first_decision_day),
                "time_cost_interpretation": "lower no_decision and lower avg_first_decision_or_20d_days imply lower capital time cost",
                "promotion_blocker": "requires exact daily candidate row parity plus validated buy/sell/stop operation module",
            }
        )
    return pd.DataFrame(rows)


def write_price_pullback_time_cost_backtest(time_cost: pd.DataFrame) -> None:
    write_csv(time_cost, PRICE_PULLBACK_TIME_COST_CSV)
    write_csv(time_cost, PRICE_PULLBACK_TIME_COST_HISTORY_CSV)
    write_csv(time_cost, DOCS_PRICE_PULLBACK_TIME_COST_CSV)
    lines = [
        "# Price Pullback 23EMA Time Cost Backtest",
        "",
        f"- generated_at: `{now_text()}`",
        "- model_id: `price_pullback_23ema`",
        "- status: `not_production_ready_research_only`",
        "- entry_basis: `signal_date_next_open`",
        f"- target_rule: first intraday high >= `+{TIME_COST_TARGET_PCT:g}%` through `D+{TIME_COST_HORIZON_DAYS}`",
        f"- stop_rule: first intraday low <= `{TIME_COST_STOP_PCT:g}%` through `D+{TIME_COST_HORIZON_DAYS}`",
        "- same_day_rule: if daily high and low hit target/stop on the same day, order is unresolved",
        "- scope: advisory time-cost research only; this does not approve daily production use",
        "",
        markdown_table(
            time_cost,
            [
                "entry_filter_id",
                "selected_stock_days",
                "mature_count",
                "target_before_stop_rate_pct",
                "stop_before_target_rate_pct",
                "same_day_target_stop_rate_pct",
                "no_decision_after_20d_rate_pct",
                "avg_holding_days_if_win",
                "avg_holding_days_if_loss",
                "avg_first_decision_or_20d_days",
            ],
            limit=50,
        ),
    ]
    PRICE_PULLBACK_TIME_COST_MD.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8", newline="\n")
    DOCS_PRICE_PULLBACK_TIME_COST_MD.write_text(
        PRICE_PULLBACK_TIME_COST_MD.read_text(encoding="utf-8"),
        encoding="utf-8",
        newline="\n",
    )


def _structure_stop_return_pct(df: pd.DataFrame) -> pd.Series:
    refs = pd.DataFrame(
        {
            "ema23": numeric_column(df, "ema23"),
            "platform_low": numeric_column(df, "platform_low"),
            "short_platform_low": numeric_column(df, "short_platform_low"),
            "previous_20d_low": numeric_column(df, "previous_20d_low"),
            "range_low_20d_prev": numeric_column(df, "range_low_20d_prev"),
        },
        index=df.index,
    )
    refs = refs.where(refs > 0)
    stop_price = refs.max(axis=1, skipna=True) * 0.98
    entry_price = numeric_column(df, "next_open")
    return (stop_price / entry_price.replace(0, pd.NA) - 1.0) * 100.0


def _future_reference_frame(valid: pd.DataFrame, h: int, reference_id: str, output_cols: list[str]) -> pd.DataFrame:
    ma20_cols = [f"future_d{day}_ma20" for day in range(1, h + 1)]
    ema23_cols = [f"future_d{day}_ema23" for day in range(1, h + 1)]
    if reference_id == "ma20":
        refs = valid[ma20_cols].apply(pd.to_numeric, errors="coerce")
    elif reference_id == "ema23":
        refs = valid[ema23_cols].apply(pd.to_numeric, errors="coerce")
    elif reference_id == "lower_ma20_ema23":
        ma20_refs = valid[ma20_cols].apply(pd.to_numeric, errors="coerce")
        ema23_refs = valid[ema23_cols].apply(pd.to_numeric, errors="coerce")
        ma20_refs.columns = output_cols
        ema23_refs.columns = output_cols
        return ma20_refs.combine(ema23_refs, np.minimum)
    else:
        raise ValueError(f"Unsupported stop_reference_id: {reference_id}")
    refs.columns = output_cols
    return refs


def _value_at_day(values: pd.DataFrame, day: pd.Series) -> pd.Series:
    result = pd.Series(math.nan, index=values.index, dtype=float)
    clean_day = pd.to_numeric(day, errors="coerce")
    mask = clean_day.notna()
    if not mask.any():
        return result
    arr = values.to_numpy(dtype=float)
    row_positions = np.flatnonzero(mask.to_numpy())
    col_positions = clean_day[mask].astype(int).to_numpy() - 1
    valid_col = (col_positions >= 0) & (col_positions < arr.shape[1])
    result.iloc[row_positions[valid_col]] = arr[row_positions[valid_col], col_positions[valid_col]]
    return result


def _blank_operation_outcome() -> dict[str, object]:
    return {
        "mature_count": 0,
        "win_count": 0,
        "neutral_count": 0,
        "failure_count": 0,
        "same_day_unresolved_count": 0,
        "win_rate_pct": "",
        "neutral_rate_pct": "",
        "failure_rate_pct": "",
        "same_day_unresolved_rate_pct": "",
        "avg_d20_close_return_pct": "",
        "median_d20_close_return_pct": "",
        "avg_realized_return_pct": "",
        "avg_win_realized_return_pct": "",
        "avg_failure_realized_return_pct": "",
        "avg_neutral_realized_return_pct": "",
        "avg_realized_or_d20_days": "",
        "avg_days_to_win": "",
        "avg_days_to_failure": "",
    }


def _operation_required_columns(candidate: dict[str, object]) -> list[str]:
    h = int(candidate["holding_window_days"])
    required = [f"next_open_to_d{day}_day_high_return_pct" for day in range(1, h + 1)]
    required.extend(f"next_open_to_d{day}_day_low_return_pct" for day in range(1, h + 1))
    required.extend(f"next_open_to_d{day}_day_close_return_pct" for day in range(1, h + 1))
    required.append(f"next_open_to_d{h}_close_return_pct")
    if candidate.get("target_rule_id") in {"prev20_high_breakout", "prior_high_breakout"}:
        target_lookback_days = int(candidate.get("target_lookback_days", 20))
        required.extend(["next_open", f"range_high_{target_lookback_days}d_prev"])
    if candidate["stop_rule_id"] == "close_below_23ema_or_support_2pct":
        required.extend(["next_open", "ema23"])
    if candidate["stop_rule_id"] in {"sustained_close_below_ma20_pct", "sustained_close_below_reference_pct"}:
        required.append("next_open")
        reference_id = str(candidate.get("stop_reference_id", "ma20"))
        if reference_id in {"ma20", "lower_ma20_ema23"}:
            required.extend(f"future_d{day}_ma20" for day in range(1, h + 1))
        if reference_id in {"ema23", "lower_ma20_ema23"}:
            required.extend(f"future_d{day}_ema23" for day in range(1, h + 1))
    return required


def _operation_outcome_counts(
    valid: pd.DataFrame,
    candidate: dict[str, object],
) -> dict[str, object]:
    h = int(candidate["holding_window_days"])
    high_cols = [f"next_open_to_d{day}_day_high_return_pct" for day in range(1, h + 1)]
    low_cols = [f"next_open_to_d{day}_day_low_return_pct" for day in range(1, h + 1)]
    close_cols = [f"next_open_to_d{day}_day_close_return_pct" for day in range(1, h + 1)]
    final_close_col = f"next_open_to_d{h}_close_return_pct"

    target_return_at_hit: pd.Series
    if candidate.get("target_rule_id") in {"prev20_high_breakout", "prior_high_breakout"}:
        entry_price = numeric_column(valid, "next_open")
        target_lookback_days = int(candidate.get("target_lookback_days", 20))
        target_price = numeric_column(valid, f"range_high_{target_lookback_days}d_prev")
        target_pct_series = (target_price / entry_price.replace(0, pd.NA) - 1.0) * 100.0
        target_day = _first_hit_day(valid[high_cols].ge(target_pct_series, axis=0))
        target_return_at_hit = target_pct_series
    else:
        target_pct = float(candidate["target_return_pct"])
        target_day = _first_hit_day(valid[high_cols] >= target_pct)
        target_return_at_hit = pd.Series(target_pct, index=valid.index, dtype=float)

    if candidate["stop_rule_id"] == "intraday_low_stop5":
        stop_pct = float(candidate["stop_return_pct"])
        stop_day = _first_hit_day(valid[low_cols] <= stop_pct)
        stop_return_at_hit = pd.Series(stop_pct, index=valid.index, dtype=float)
    elif candidate["stop_rule_id"] == "close_below_23ema_or_support_2pct":
        stop_pct_series = _structure_stop_return_pct(valid)
        stop_day = _first_hit_day(valid[close_cols].le(stop_pct_series, axis=0))
        stop_return_at_hit = _value_at_day(valid[close_cols].apply(pd.to_numeric, errors="coerce"), stop_day)
    elif candidate["stop_rule_id"] in {"sustained_close_below_ma20_pct", "sustained_close_below_reference_pct"}:
        entry_price = numeric_column(valid, "next_open")
        stop_pct = float(candidate.get("stop_buffer_pct", candidate.get("monthline_stop_pct", 0.0)))
        consecutive_days = int(candidate.get("stop_consecutive_days", candidate.get("monthline_stop_consecutive_days", 1)))
        reference_id = str(candidate.get("stop_reference_id", "ma20"))
        close_returns = valid[close_cols].apply(pd.to_numeric, errors="coerce")
        refs = _future_reference_frame(valid, h, reference_id, close_cols)
        stop_threshold = (refs.mul(1.0 - stop_pct / 100.0).div(entry_price, axis=0) - 1.0) * 100.0
        stop_hits = close_returns.le(stop_threshold)
        stop_day = _first_consecutive_hit_day(stop_hits, consecutive_days)
        stop_return_at_hit = _value_at_day(close_returns, stop_day)
    else:
        raise ValueError(f"Unsupported stop_rule_id: {candidate['stop_rule_id']}")

    target_before_stop = target_day.notna() & (stop_day.isna() | (target_day < stop_day))
    stop_before_target = stop_day.notna() & (target_day.isna() | (stop_day < target_day))
    same_day_unresolved = target_day.notna() & stop_day.notna() & target_day.eq(stop_day)
    no_trigger = target_day.isna() & stop_day.isna()
    final_close_return = pd.to_numeric(valid[final_close_col], errors="coerce")
    neutral = no_trigger & final_close_return.ge(0)
    late_failure = no_trigger & final_close_return.lt(0)
    failure = stop_before_target | late_failure

    realized_days = pd.Series(h, index=valid.index, dtype=float)
    realized_days = realized_days.mask(target_before_stop, target_day)
    realized_days = realized_days.mask(stop_before_target, stop_day)
    realized_days = realized_days.mask(same_day_unresolved, target_day)

    realized_return = pd.Series(math.nan, index=valid.index, dtype=float)
    realized_return = realized_return.mask(target_before_stop, target_return_at_hit)
    realized_return = realized_return.mask(stop_before_target, stop_return_at_hit)
    realized_return = realized_return.mask(no_trigger, final_close_return)

    win_count = int(target_before_stop.sum())
    neutral_count = int(neutral.sum())
    failure_count = int(failure.sum())
    same_day_count = int(same_day_unresolved.sum())
    mature = len(valid)
    return {
        "mature_count": mature,
        "win_count": win_count,
        "neutral_count": neutral_count,
        "failure_count": failure_count,
        "same_day_unresolved_count": same_day_count,
        "win_rate_pct": _rate(win_count, mature),
        "neutral_rate_pct": _rate(neutral_count, mature),
        "failure_rate_pct": _rate(failure_count, mature),
        "same_day_unresolved_rate_pct": _rate(same_day_count, mature),
        "avg_d20_close_return_pct": round(float(final_close_return.mean()), 2) if mature else "",
        "median_d20_close_return_pct": round(float(final_close_return.median()), 2) if mature else "",
        "avg_realized_return_pct": _mean_or_blank(realized_return),
        "avg_win_realized_return_pct": _mean_or_blank(realized_return[target_before_stop]) if mature else "",
        "avg_failure_realized_return_pct": _mean_or_blank(realized_return[failure]) if mature else "",
        "avg_neutral_realized_return_pct": _mean_or_blank(realized_return[neutral]) if mature else "",
        "avg_realized_or_d20_days": _mean_or_blank(realized_days),
        "avg_days_to_win": _mean_or_blank(target_day[target_before_stop]) if mature else "",
        "avg_days_to_failure": _mean_or_blank(realized_days[failure]) if mature else "",
    }


def build_price_pullback_operation_module_research(df: pd.DataFrame) -> pd.DataFrame:
    base_mask = current_price_pullback_baseline_proxy(df).fillna(False)
    rows: list[dict[str, object]] = []
    generated_at = now_text()
    for entry_filter in PRICE_PULLBACK_ENTRY_FILTERS:
        filter_mask = entry_filter["condition"](df).fillna(False)
        picked = df[base_mask & filter_mask].copy()
        for candidate in PRICE_PULLBACK_OPERATION_MODULE_CANDIDATES:
            h = int(candidate["holding_window_days"])
            required = [f"next_open_to_d{day}_day_high_return_pct" for day in range(1, h + 1)]
            required.extend(f"next_open_to_d{day}_day_low_return_pct" for day in range(1, h + 1))
            required.extend(f"next_open_to_d{day}_day_close_return_pct" for day in range(1, h + 1))
            required.append(f"next_open_to_d{h}_close_return_pct")
            if candidate.get("target_rule_id") in {"prev20_high_breakout", "prior_high_breakout"}:
                target_lookback_days = int(candidate.get("target_lookback_days", 20))
                required.extend(["next_open", f"range_high_{target_lookback_days}d_prev"])
            if candidate["stop_rule_id"] == "close_below_23ema_or_support_2pct":
                required.extend(["next_open", "ema23"])
            if candidate["stop_rule_id"] in {"sustained_close_below_ma20_pct", "sustained_close_below_reference_pct"}:
                required.append("next_open")
                reference_id = str(candidate.get("stop_reference_id", "ma20"))
                if reference_id in {"ma20", "lower_ma20_ema23"}:
                    required.extend(f"future_d{day}_ma20" for day in range(1, h + 1))
                if reference_id in {"ema23", "lower_ma20_ema23"}:
                    required.extend(f"future_d{day}_ema23" for day in range(1, h + 1))
            valid = (
                picked.dropna(subset=required).copy()
                if all(col in picked.columns for col in required)
                else picked.iloc[0:0].copy()
            )
            outcome = _operation_outcome_counts(valid, candidate) if not valid.empty else {
                "mature_count": 0,
                "win_count": 0,
                "neutral_count": 0,
                "failure_count": 0,
                "same_day_unresolved_count": 0,
                "win_rate_pct": "",
                "neutral_rate_pct": "",
                "failure_rate_pct": "",
                "same_day_unresolved_rate_pct": "",
                "avg_d20_close_return_pct": "",
                "median_d20_close_return_pct": "",
                "avg_realized_return_pct": "",
                "avg_win_realized_return_pct": "",
                "avg_failure_realized_return_pct": "",
                "avg_neutral_realized_return_pct": "",
                "avg_realized_or_d20_days": "",
                "avg_days_to_win": "",
                "avg_days_to_failure": "",
            }
            target_lookback_days = candidate.get("target_lookback_days", "")
            rows.append(
                {
                    "generated_at": generated_at,
                    "model_id": "price_pullback_23ema",
                    "model_name_zh": "股價回檔模型",
                    "research_baseline_parameter_set_id": "production_current_proxy",
                    "research_baseline_status": "production_proxy",
                    "operation_module_candidate_id": candidate["operation_module_candidate_id"],
                    "entry_filter_id": entry_filter["entry_filter_id"],
                    "entry_signal_rule": entry_filter["entry_signal_rule"],
                    "entry_rule_id": candidate["entry_rule_id"],
                    "buy_point_rule": f"{candidate['buy_point_rule']} Entry filter: {entry_filter['entry_signal_rule']}",
                    "target_rule": (
                        f"Win if first intraday high breaks above signal-day previous {target_lookback_days}-day high before stop through D+{h}."
                        if candidate.get("target_rule_id") in {"prev20_high_breakout", "prior_high_breakout"}
                        else f"Win if first intraday high reaches +{float(candidate['target_return_pct']):g}% before stop through D+{h}."
                    ),
                    "target_lookback_days": target_lookback_days,
                    "stop_rule_id": candidate["stop_rule_id"],
                    "stop_reference_id": candidate.get("stop_reference_id", ""),
                    "stop_reference_name": candidate.get("stop_reference_name", ""),
                    "stop_buffer_pct": candidate.get("stop_buffer_pct", ""),
                    "stop_consecutive_days": candidate.get("stop_consecutive_days", ""),
                    "stop_rule": candidate["stop_rule"],
                    "exit_rule": candidate["exit_rule"],
                    "win_definition": "target hit before stop",
                    "neutral_definition": "no target/stop by D+20 and D+20 close return >= 0%",
                    "failure_definition": "stop hit before target, or no target/stop by D+20 and D+20 close return < 0%",
                    "same_day_rule": "if target and stop are first seen on the same daily candle, classify as same_day_unresolved",
                    "holding_window_days": h,
                    "selected_stock_days": len(picked),
                    "selected_unique_stocks": picked["stock_id"].nunique() if not picked.empty else 0,
                    "advisory_status": "not_production_ready_research_only",
                    "approved_for_daily": False,
                    "promotion_readiness": "blocked_exact_daily_row_parity_and_operation_approval_required",
                    "promotion_blocker": "requires exact daily candidate row parity plus explicit promotion/sync PR before production use",
                    **outcome,
                }
            )
    return pd.DataFrame(rows)


def write_price_pullback_operation_module_research(module: pd.DataFrame) -> None:
    write_csv(module, PRICE_PULLBACK_OPERATION_MODULE_CSV)
    write_csv(module, PRICE_PULLBACK_OPERATION_MODULE_HISTORY_CSV)
    write_csv(module, DOCS_PRICE_PULLBACK_OPERATION_MODULE_CSV)
    lines = [
        "# Price Pullback 23EMA Operation Module Research",
        "",
        f"- generated_at: `{now_text()}`",
        "- model_id: `price_pullback_23ema`",
        "- status: `not_production_ready_research_only`",
        "- scope: advisory operation module candidates only; this does not approve daily production use",
        "- entry_basis: `signal_date_next_open`",
        "- win_definition: target hit before stop",
        "- neutral_definition: no target/stop by D+20 and D+20 close return >= 0%",
        "- failure_definition: stop hit before target, or no target/stop by D+20 and D+20 close return < 0%",
        "- same_day_rule: if target and stop are first seen on the same daily candle, classify as `same_day_unresolved`",
        "- blocker: exact daily candidate row parity and explicit promotion/sync PR are still required before production use",
        "",
        markdown_table(
            module,
            [
                "entry_filter_id",
                "operation_module_candidate_id",
                "target_lookback_days",
                "stop_reference_id",
                "stop_buffer_pct",
                "stop_consecutive_days",
                "selected_stock_days",
                "mature_count",
                "win_rate_pct",
                "neutral_rate_pct",
                "failure_rate_pct",
                "same_day_unresolved_rate_pct",
                "avg_realized_return_pct",
                "avg_win_realized_return_pct",
                "avg_failure_realized_return_pct",
                "avg_d20_close_return_pct",
                "avg_realized_or_d20_days",
                "promotion_readiness",
            ],
            limit=80,
        ),
    ]
    PRICE_PULLBACK_OPERATION_MODULE_MD.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8", newline="\n")
    DOCS_PRICE_PULLBACK_OPERATION_MODULE_MD.write_text(
        PRICE_PULLBACK_OPERATION_MODULE_MD.read_text(encoding="utf-8"),
        encoding="utf-8",
        newline="\n",
    )


def _price_pullback_feature_confirmation_operation_candidate() -> dict[str, object]:
    for candidate in PRICE_PULLBACK_OPERATION_MODULE_CANDIDATES:
        if candidate["operation_module_candidate_id"] == PRICE_PULLBACK_FEATURE_CONFIRMATION_OPERATION_ID:
            return candidate
    raise RuntimeError(f"Missing price_pullback feature confirmation operation: {PRICE_PULLBACK_FEATURE_CONFIRMATION_OPERATION_ID}")


def _add_feature_confirmation_deltas(result: pd.DataFrame) -> pd.DataFrame:
    if result.empty or "feature_filter_id" not in result.columns:
        return result
    out = result.copy()
    delta_map = {
        "win_rate_pct": "delta_vs_baseline_win_rate_pct",
        "failure_rate_pct": "delta_vs_baseline_failure_rate_pct",
        "avg_realized_return_pct": "delta_vs_baseline_avg_realized_return_pct",
        "avg_realized_or_d20_days": "delta_vs_baseline_avg_realized_or_d20_days",
    }
    for col in [*delta_map.values(), "selected_share_of_baseline_pct", "mature_share_of_baseline_pct"]:
        out[col] = np.nan

    baseline = out[out["feature_filter_id"].eq("baseline_replay")]
    if baseline.empty:
        return out
    baseline_row = baseline.iloc[0]
    baseline_values = {metric: pd.to_numeric(pd.Series([baseline_row.get(metric, "")]), errors="coerce").iloc[0] for metric in delta_map}
    baseline_selected = pd.to_numeric(pd.Series([baseline_row.get("selected_stock_days", "")]), errors="coerce").iloc[0]
    baseline_mature = pd.to_numeric(pd.Series([baseline_row.get("mature_count", "")]), errors="coerce").iloc[0]

    tested = out["feature_test_status"].eq("tested_point_in_time")
    for idx, row in out[tested].iterrows():
        selected = pd.to_numeric(pd.Series([row.get("selected_stock_days", "")]), errors="coerce").iloc[0]
        mature = pd.to_numeric(pd.Series([row.get("mature_count", "")]), errors="coerce").iloc[0]
        if pd.notna(selected) and pd.notna(baseline_selected) and baseline_selected > 0:
            out.at[idx, "selected_share_of_baseline_pct"] = round(float(selected / baseline_selected * 100.0), 2)
        if pd.notna(mature) and pd.notna(baseline_mature) and baseline_mature > 0:
            out.at[idx, "mature_share_of_baseline_pct"] = round(float(mature / baseline_mature * 100.0), 2)
        for metric, delta_col in delta_map.items():
            value = pd.to_numeric(pd.Series([row.get(metric, "")]), errors="coerce").iloc[0]
            baseline_value = baseline_values[metric]
            if pd.notna(value) and pd.notna(baseline_value):
                out.at[idx, delta_col] = round(float(value - baseline_value), 2)
    return out


def build_price_pullback_feature_confirmation_research(df: pd.DataFrame) -> pd.DataFrame:
    base_mask = current_price_pullback_baseline_proxy(df).fillna(False)
    candidate = _price_pullback_feature_confirmation_operation_candidate()
    required = _operation_required_columns(candidate)
    h = int(candidate["holding_window_days"])
    rows: list[dict[str, object]] = []
    generated_at = now_text()
    for feature_filter in PRICE_PULLBACK_FEATURE_CONFIRMATION_FILTERS:
        status = str(feature_filter["feature_test_status"])
        condition = feature_filter.get("condition")
        if status == "tested_point_in_time" and condition is not None:
            filter_mask = condition(df).fillna(False)
            picked = df[base_mask & filter_mask].copy()
            valid = (
                picked.dropna(subset=required).copy()
                if all(col in picked.columns for col in required)
                else picked.iloc[0:0].copy()
            )
            outcome = _operation_outcome_counts(valid, candidate) if not valid.empty else _blank_operation_outcome()
            selected_stock_days: int | str = len(picked)
            selected_unique_stocks: int | str = picked["stock_id"].nunique() if not picked.empty else 0
        else:
            picked = df.iloc[0:0].copy()
            outcome = _blank_operation_outcome()
            selected_stock_days = ""
            selected_unique_stocks = ""

        target_lookback_days = candidate.get("target_lookback_days", "")
        rows.append(
            {
                "generated_at": generated_at,
                "model_id": "price_pullback_23ema",
                "model_name_zh": "股價回檔模型",
                "research_artifact_id": "price_pullback_23ema_feature_confirmation_research",
                "research_baseline_parameter_set_id": "production_current_proxy",
                "research_baseline_status": "production_proxy",
                "fixed_operation_module_candidate_id": PRICE_PULLBACK_FEATURE_CONFIRMATION_OPERATION_ID,
                "feature_filter_id": feature_filter["feature_filter_id"],
                "feature_family": feature_filter["feature_family"],
                "feature_rule": feature_filter["feature_rule"],
                "feature_test_status": status,
                "data_status": feature_filter["data_status"],
                "entry_rule_id": candidate["entry_rule_id"],
                "buy_point_rule": candidate["buy_point_rule"],
                "target_rule": (
                    f"Win if first intraday high breaks above signal-day previous {target_lookback_days}-day high before stop through D+{h}."
                ),
                "target_lookback_days": target_lookback_days,
                "stop_rule_id": candidate["stop_rule_id"],
                "stop_reference_id": candidate.get("stop_reference_id", ""),
                "stop_reference_name": candidate.get("stop_reference_name", ""),
                "stop_buffer_pct": candidate.get("stop_buffer_pct", ""),
                "stop_consecutive_days": candidate.get("stop_consecutive_days", ""),
                "stop_rule": candidate["stop_rule"],
                "exit_rule": candidate["exit_rule"],
                "win_definition": "target hit before stop",
                "neutral_definition": "no target/stop by D+20 and D+20 close return >= 0%",
                "failure_definition": "stop hit before target, or no target/stop by D+20 and D+20 close return < 0%",
                "same_day_rule": "if target and stop are first seen on the same daily candle, classify as same_day_unresolved",
                "holding_window_days": h,
                "selected_stock_days": selected_stock_days,
                "selected_unique_stocks": selected_unique_stocks,
                "advisory_status": "not_production_ready_research_only",
                "approved_for_daily": False,
                "promotion_readiness": "blocked_exact_daily_row_parity_and_operation_approval_required",
                "promotion_blocker": "requires exact daily candidate row parity plus explicit promotion/sync PR before production use",
                **outcome,
            }
        )
    return _add_feature_confirmation_deltas(pd.DataFrame(rows))


def write_price_pullback_feature_confirmation_research(feature_confirmation: pd.DataFrame) -> None:
    write_csv(feature_confirmation, PRICE_PULLBACK_FEATURE_CONFIRMATION_CSV)
    write_csv(feature_confirmation, PRICE_PULLBACK_FEATURE_CONFIRMATION_HISTORY_CSV)
    write_csv(feature_confirmation, DOCS_PRICE_PULLBACK_FEATURE_CONFIRMATION_CSV)
    lines = [
        "# Price Pullback 23EMA Feature Confirmation Research",
        "",
        f"- generated_at: `{now_text()}`",
        "- model_id: `price_pullback_23ema`",
        "- status: `not_production_ready_research_only`",
        "- scope: advisory feature confirmation only; this does not approve daily production use",
        f"- fixed_operation_module_candidate_id: `{PRICE_PULLBACK_FEATURE_CONFIRMATION_OPERATION_ID}`",
        "- entry_basis: `signal_date_next_open` after production proxy replay plus the feature filter under test",
        "- target: previous 20-day high breakout before stop through D+20",
        "- stop: close stays at least 4% below lower of MA20 and EMA23 for 4 consecutive trading days",
        "- blocked rows: revenue and market background are documented as data/join gaps, not scored as backtest results",
        "- blocker: exact daily candidate row parity and explicit promotion/sync PR are still required before production use",
        "",
        markdown_table(
            feature_confirmation,
            [
                "feature_filter_id",
                "feature_family",
                "feature_test_status",
                "data_status",
                "selected_stock_days",
                "selected_share_of_baseline_pct",
                "mature_count",
                "mature_share_of_baseline_pct",
                "win_rate_pct",
                "delta_vs_baseline_win_rate_pct",
                "neutral_rate_pct",
                "failure_rate_pct",
                "delta_vs_baseline_failure_rate_pct",
                "same_day_unresolved_rate_pct",
                "avg_realized_return_pct",
                "delta_vs_baseline_avg_realized_return_pct",
                "avg_realized_or_d20_days",
                "delta_vs_baseline_avg_realized_or_d20_days",
                "promotion_readiness",
            ],
            limit=80,
        ),
    ]
    PRICE_PULLBACK_FEATURE_CONFIRMATION_MD.write_text(
        "\n".join(lines).rstrip() + "\n",
        encoding="utf-8",
        newline="\n",
    )
    DOCS_PRICE_PULLBACK_FEATURE_CONFIRMATION_MD.write_text(
        PRICE_PULLBACK_FEATURE_CONFIRMATION_MD.read_text(encoding="utf-8"),
        encoding="utf-8",
        newline="\n",
    )


def _numeric_or_nan(value: object) -> float:
    parsed = pd.to_numeric(pd.Series([value]), errors="coerce").iloc[0]
    return float(parsed) if pd.notna(parsed) else math.nan


def _delta_or_blank(value: object, baseline: object) -> float | str:
    parsed = _numeric_or_nan(value)
    base = _numeric_or_nan(baseline)
    if math.isnan(parsed) or math.isnan(base):
        return ""
    return round(parsed - base, 2)


def _share_pct_or_blank(value: object, baseline: object) -> float | str:
    parsed = _numeric_or_nan(value)
    base = _numeric_or_nan(baseline)
    if math.isnan(parsed) or math.isnan(base) or base <= 0:
        return ""
    return round(parsed / base * 100.0, 2)


def _price_pullback_parity_discussion_status(row_parity: pd.DataFrame) -> dict[str, object]:
    if row_parity.empty or "parity_status" not in row_parity.columns:
        return {
            "daily_row_parity_status_summary": "missing_price_pullback_row_parity_audit",
            "daily_row_parity_exact_pass_count": 0,
            "daily_row_parity_blocked_count": 0,
            "daily_row_parity_blocker_summary": "price_pullback daily row parity artifact is missing",
        }
    counts = row_parity["parity_status"].map(safe_str).value_counts()
    blocked = row_parity[~row_parity["parity_status"].map(safe_str).eq("exact_daily_row_parity_pass")]
    blocker_values = (
        blocked["parity_blocker"].map(safe_str).replace("", pd.NA).dropna().unique().tolist()
        if "parity_blocker" in blocked.columns
        else []
    )
    return {
        "daily_row_parity_status_summary": ";".join(f"{status}:{int(count)}" for status, count in counts.items()),
        "daily_row_parity_exact_pass_count": int(counts.get("exact_daily_row_parity_pass", 0)),
        "daily_row_parity_blocked_count": int(len(blocked)),
        "daily_row_parity_blocker_summary": "; ".join(blocker_values[:3]),
    }


def _price_pullback_decision_status(row: dict[str, object]) -> tuple[str, str]:
    item_id = safe_str(row.get("decision_item_id", ""))
    test_status = safe_str(row.get("test_status", ""))
    feature_family = safe_str(row.get("feature_family", ""))
    mature = _numeric_or_nan(row.get("mature_count", ""))
    win_delta = _numeric_or_nan(row.get("delta_vs_baseline_win_rate_pct", ""))
    failure_delta = _numeric_or_nan(row.get("delta_vs_baseline_failure_rate_pct", ""))
    avg_delta = _numeric_or_nan(row.get("delta_vs_baseline_avg_realized_return_pct", ""))

    if item_id == "baseline:production_replay_operation_anchor":
        return (
            "baseline_anchor",
            "作為比較基準；不是正式買賣模組，仍需 promotion PR 才能升格。",
        )
    if test_status != "tested_point_in_time":
        if feature_family == "revenue":
            return (
                "blocked_data_gap_required_before_gate",
                "營收可以當必要條件或加分討論，但目前缺 point-in-time 歷史營收 panel，不能先寫進 production。",
            )
        if feature_family == "market_background":
            return (
                "blocked_market_join_required",
                "大盤背景方向合理，但需要把 market regime 依 signal_date 接到個股 research frame 後才能評估。",
            )
        return ("blocked_data_gap", "資料或 join 尚未完成，不能視為已回測條件。")
    if math.isnan(mature) or mature < MIN_REVIEW_SAMPLE:
        return ("insufficient_sample_review_only", "樣本不足，只能列為觀察，不能當必要條件。")
    if not math.isnan(win_delta) and not math.isnan(failure_delta):
        if win_delta >= 5.0 and failure_delta <= -3.0:
            if not math.isnan(avg_delta) and avg_delta < 0:
                return (
                    "score_bonus_candidate_winrate_tradeoff",
                    "勝率與失敗率改善，但平均實現報酬低於 baseline；較適合討論加分，不適合直接當硬 gate。",
                )
            return (
                "score_bonus_candidate",
                "相對 baseline 改善勝率與失敗率，可優先討論作為加分或 ranking 權重。",
            )
        if win_delta <= -3.0 and failure_delta >= 3.0:
            return (
                "reject_as_required_gate",
                "相對 baseline 勝率下降且失敗率上升，不適合升成必要條件。",
            )
        if not math.isnan(avg_delta) and avg_delta > 0 and (win_delta < 0 or failure_delta > 0):
            return (
                "return_up_but_riskier_not_gate",
                "平均報酬提高但勝率或失敗率變差，若保留只能當高波動加分候選，不適合硬篩。",
            )
        if win_delta > 0 or failure_delta < 0:
            return (
                "mixed_discussion_candidate",
                "有部分指標優於 baseline，但改善不夠完整，適合進入討論而非直接升格。",
            )
    if not math.isnan(avg_delta) and avg_delta > 0:
        return (
            "return_only_discussion_candidate",
            "平均報酬高於 baseline，但勝率/失敗率沒有同步改善，需人工判斷是否符合模型目標。",
        )
    return ("no_observed_improvement", "目前沒有相對 baseline 的明確優勢。")


def _price_pullback_decision_row_from_metrics(
    *,
    generated_at: str,
    source_artifact_id: str,
    decision_axis: str,
    decision_item_id: str,
    feature_family: str,
    condition_role: str,
    rule_text: str,
    test_status: str,
    data_status: str,
    row: pd.Series,
    baseline: pd.Series,
    parity: dict[str, object],
) -> dict[str, object]:
    out: dict[str, object] = {
        "generated_at": generated_at,
        "model_id": "price_pullback_23ema",
        "model_name_zh": "股價回檔模型",
        "research_artifact_id": "price_pullback_23ema_model_decision_audit",
        "source_artifact_id": source_artifact_id,
        "decision_axis": decision_axis,
        "decision_item_id": decision_item_id,
        "feature_family": feature_family,
        "condition_role": condition_role,
        "condition_rule": rule_text,
        "test_status": test_status,
        "data_status": data_status,
        "fixed_operation_module_candidate_id": PRICE_PULLBACK_FEATURE_CONFIRMATION_OPERATION_ID,
        "buy_point_rule": safe_str(row.get("buy_point_rule", baseline.get("buy_point_rule", ""))),
        "target_rule": safe_str(row.get("target_rule", baseline.get("target_rule", ""))),
        "stop_rule": safe_str(row.get("stop_rule", baseline.get("stop_rule", ""))),
        "exit_rule": safe_str(row.get("exit_rule", baseline.get("exit_rule", ""))),
        "win_definition": safe_str(row.get("win_definition", baseline.get("win_definition", ""))),
        "neutral_definition": safe_str(row.get("neutral_definition", baseline.get("neutral_definition", ""))),
        "failure_definition": safe_str(row.get("failure_definition", baseline.get("failure_definition", ""))),
        "selected_stock_days": row.get("selected_stock_days", ""),
        "selected_unique_stocks": row.get("selected_unique_stocks", ""),
        "mature_count": row.get("mature_count", ""),
        "selected_share_of_baseline_pct": _share_pct_or_blank(
            row.get("selected_stock_days", ""),
            baseline.get("selected_stock_days", ""),
        ),
        "mature_share_of_baseline_pct": _share_pct_or_blank(
            row.get("mature_count", ""),
            baseline.get("mature_count", ""),
        ),
        "win_rate_pct": row.get("win_rate_pct", ""),
        "neutral_rate_pct": row.get("neutral_rate_pct", ""),
        "failure_rate_pct": row.get("failure_rate_pct", ""),
        "same_day_unresolved_rate_pct": row.get("same_day_unresolved_rate_pct", ""),
        "avg_realized_return_pct": row.get("avg_realized_return_pct", ""),
        "avg_d20_close_return_pct": row.get("avg_d20_close_return_pct", ""),
        "avg_realized_or_d20_days": row.get("avg_realized_or_d20_days", ""),
        "delta_vs_baseline_win_rate_pct": _delta_or_blank(row.get("win_rate_pct", ""), baseline.get("win_rate_pct", "")),
        "delta_vs_baseline_failure_rate_pct": _delta_or_blank(
            row.get("failure_rate_pct", ""), baseline.get("failure_rate_pct", "")
        ),
        "delta_vs_baseline_avg_realized_return_pct": _delta_or_blank(
            row.get("avg_realized_return_pct", ""), baseline.get("avg_realized_return_pct", "")
        ),
        "delta_vs_baseline_avg_realized_or_d20_days": _delta_or_blank(
            row.get("avg_realized_or_d20_days", ""), baseline.get("avg_realized_or_d20_days", "")
        ),
        "advisory_status": "not_production_ready_research_only",
        "approved_for_daily": False,
        "production_change": "none",
        "promotion_blocker": "requires explicit model promotion PR with exact research parity, contract update, validators, and post-merge validation",
        **parity,
    }
    if decision_item_id == "baseline:production_replay_operation_anchor":
        out["selected_share_of_baseline_pct"] = 100.0
        out["mature_share_of_baseline_pct"] = 100.0
        for col in [
            "delta_vs_baseline_win_rate_pct",
            "delta_vs_baseline_failure_rate_pct",
            "delta_vs_baseline_avg_realized_return_pct",
            "delta_vs_baseline_avg_realized_or_d20_days",
        ]:
            out[col] = 0.0
    status, conclusion = _price_pullback_decision_status(out)
    out["decision_status"] = status
    out["plain_conclusion_zh"] = conclusion
    return out


def build_price_pullback_model_decision_audit(
    operation_module: pd.DataFrame,
    feature_confirmation: pd.DataFrame,
    row_parity: pd.DataFrame,
) -> pd.DataFrame:
    generated = now_text()
    columns = [
        "generated_at",
        "model_id",
        "model_name_zh",
        "research_artifact_id",
        "source_artifact_id",
        "decision_axis",
        "decision_item_id",
        "feature_family",
        "condition_role",
        "condition_rule",
        "test_status",
        "data_status",
        "fixed_operation_module_candidate_id",
        "buy_point_rule",
        "target_rule",
        "stop_rule",
        "exit_rule",
        "win_definition",
        "neutral_definition",
        "failure_definition",
        "selected_stock_days",
        "selected_unique_stocks",
        "mature_count",
        "selected_share_of_baseline_pct",
        "mature_share_of_baseline_pct",
        "win_rate_pct",
        "neutral_rate_pct",
        "failure_rate_pct",
        "same_day_unresolved_rate_pct",
        "avg_realized_return_pct",
        "avg_d20_close_return_pct",
        "avg_realized_or_d20_days",
        "delta_vs_baseline_win_rate_pct",
        "delta_vs_baseline_failure_rate_pct",
        "delta_vs_baseline_avg_realized_return_pct",
        "delta_vs_baseline_avg_realized_or_d20_days",
        "decision_status",
        "plain_conclusion_zh",
        "advisory_status",
        "approved_for_daily",
        "production_change",
        "daily_row_parity_status_summary",
        "daily_row_parity_exact_pass_count",
        "daily_row_parity_blocked_count",
        "daily_row_parity_blocker_summary",
        "promotion_blocker",
    ]
    if operation_module.empty:
        return pd.DataFrame(columns=columns)

    op = operation_module[
        operation_module["operation_module_candidate_id"].astype(str).eq(PRICE_PULLBACK_FEATURE_CONFIRMATION_OPERATION_ID)
    ].copy()
    if op.empty:
        return pd.DataFrame(columns=columns)
    baseline_rows = op[op["entry_filter_id"].astype(str).eq("baseline_replay")]
    if baseline_rows.empty:
        return pd.DataFrame(columns=columns)
    baseline = baseline_rows.iloc[0]
    parity = _price_pullback_parity_discussion_status(row_parity)

    rows: list[dict[str, object]] = [
        _price_pullback_decision_row_from_metrics(
            generated_at=generated,
            source_artifact_id="price_pullback_23ema_operation_module_research",
            decision_axis="baseline_operation",
            decision_item_id="baseline:production_replay_operation_anchor",
            feature_family="baseline",
            condition_role="comparison_anchor",
            rule_text="current production proxy replay; no extra entry or feature filter",
            test_status="tested_point_in_time",
            data_status="available_point_in_time_research_frame",
            row=baseline,
            baseline=baseline,
            parity=parity,
        )
    ]

    for _, entry_row in op[~op["entry_filter_id"].astype(str).eq("baseline_replay")].iterrows():
        rows.append(
            _price_pullback_decision_row_from_metrics(
                generated_at=generated,
                source_artifact_id="price_pullback_23ema_operation_module_research",
                decision_axis="entry_filter",
                decision_item_id=f"entry_filter:{safe_str(entry_row.get('entry_filter_id', ''))}",
                feature_family="entry_filter",
                condition_role="possible_buy_gate_or_score_bonus",
                rule_text=safe_str(entry_row.get("entry_signal_rule", "")),
                test_status="tested_point_in_time",
                data_status="available_point_in_time_research_frame",
                row=entry_row,
                baseline=baseline,
                parity=parity,
            )
        )

    if not feature_confirmation.empty:
        features = feature_confirmation[
            ~feature_confirmation["feature_filter_id"].astype(str).eq("baseline_replay")
        ].copy()
        for _, feature_row in features.iterrows():
            status = safe_str(feature_row.get("feature_test_status", ""))
            rows.append(
                _price_pullback_decision_row_from_metrics(
                    generated_at=generated,
                    source_artifact_id="price_pullback_23ema_feature_confirmation_research",
                    decision_axis="feature_filter",
                    decision_item_id=f"feature_filter:{safe_str(feature_row.get('feature_filter_id', ''))}",
                    feature_family=safe_str(feature_row.get("feature_family", "")),
                    condition_role="possible_required_gate_or_score_bonus",
                    rule_text=safe_str(feature_row.get("feature_rule", "")),
                    test_status=status,
                    data_status=safe_str(feature_row.get("data_status", "")),
                    row=feature_row,
                    baseline=baseline,
                    parity=parity,
                )
            )

    return pd.DataFrame(rows, columns=columns)


def write_price_pullback_model_decision_audit(decision: pd.DataFrame) -> None:
    write_csv(decision, PRICE_PULLBACK_DECISION_AUDIT_CSV)
    write_csv(decision, PRICE_PULLBACK_DECISION_AUDIT_HISTORY_CSV)
    write_csv(decision, DOCS_PRICE_PULLBACK_DECISION_AUDIT_CSV)
    status_counts = (
        decision["decision_status"].value_counts().reset_index()
        if not decision.empty and "decision_status" in decision.columns
        else pd.DataFrame(columns=["decision_status", "count"])
    )
    if not status_counts.empty:
        status_counts.columns = ["decision_status", "count"]
    lines = [
        "# Price Pullback 23EMA Model Decision Audit",
        "",
        f"- generated_at: `{now_text()}`",
        "- model_id: `price_pullback_23ema`",
        "- status: `discussion_ready_research_only`; this does not change production condition, scoring, ranking, or contract registry",
        f"- fixed_operation_module_candidate_id: `{PRICE_PULLBACK_FEATURE_CONFIRMATION_OPERATION_ID}`",
        "- buy_point: current production proxy signal plus the tested entry/feature filter on signal date; buy next open only after both hold",
        "- sell_point: first intraday breakout above signal-day previous 20-day high before stop through D+20",
        "- stop: close stays at least 4% below the lower of 20MA and 23EMA for 4 consecutive trading days",
        "- model_decision_use: compare baseline, volume red K, prior extension, chip, technical, 45d structure, revenue gap, and market-background gap in one table",
        "- rule: rows marked `reject_as_required_gate` must not become production gates without new evidence; blocked rows require data joins before scoring",
        "",
        "## Decision Status Counts",
        "",
        markdown_table(status_counts, status_counts.columns.tolist()) if not status_counts.empty else "No decision rows.",
        "",
        "## Decision Rows",
        "",
        markdown_table(
            decision,
            [
                "decision_axis",
                "decision_item_id",
                "feature_family",
                "selected_share_of_baseline_pct",
                "mature_count",
                "win_rate_pct",
                "delta_vs_baseline_win_rate_pct",
                "failure_rate_pct",
                "delta_vs_baseline_failure_rate_pct",
                "avg_realized_return_pct",
                "delta_vs_baseline_avg_realized_return_pct",
                "avg_realized_or_d20_days",
                "decision_status",
                "plain_conclusion_zh",
            ],
            limit=120,
        ),
    ]
    PRICE_PULLBACK_DECISION_AUDIT_MD.write_text(
        "\n".join(lines).rstrip() + "\n",
        encoding="utf-8",
        newline="\n",
    )
    DOCS_PRICE_PULLBACK_DECISION_AUDIT_MD.write_text(
        PRICE_PULLBACK_DECISION_AUDIT_MD.read_text(encoding="utf-8"),
        encoding="utf-8",
        newline="\n",
    )


def _stock_id_sample(values: set[str], limit: int = 12) -> str:
    return ";".join(sorted(values)[:limit])


def _snapshot_date_from_path(path: Path) -> str:
    return normalize_date(path.stem.rsplit("_", 1)[-1])


def _value_counts_summary(series: pd.Series, limit: int = 8) -> str:
    if series.empty:
        return ""
    cleaned = series.map(lambda value: safe_str(value).strip() or "(blank)")
    counts = cleaned.value_counts()
    return ";".join(f"{key}:{int(count)}" for key, count in counts.head(limit).items())


def _all_candidates_snapshot_path(snapshot_dir: Path, report_date: str) -> Path:
    return snapshot_dir / f"all_candidates_{report_date}.csv"


def _price_pullback_candidate_universe_replay(
    snapshot_dir: Path,
    report_date: str,
) -> dict[str, object]:
    path = _all_candidates_snapshot_path(snapshot_dir, report_date)
    if not path.exists():
        return {
            "comparison_basis": "full_research_frame_proxy",
            "comparison_stock_ids": None,
            "candidate_universe_replay_status": "missing_historical_all_candidates_source_row_snapshot",
            "candidate_universe_snapshot_path": "",
            "candidate_universe_source_row_count": "",
            "candidate_universe_condition_stock_count": "",
            "candidate_universe_missing_required_columns": "",
            "replay_error": "",
        }

    try:
        candidates = pd.read_csv(path, dtype=str, keep_default_na=False).fillna("")
    except Exception as exc:
        return {
            "comparison_basis": "production_all_candidates_source_row_replay",
            "comparison_stock_ids": set(),
            "candidate_universe_replay_status": "blocked_unreadable_all_candidates_source_row_snapshot",
            "candidate_universe_snapshot_path": path.as_posix(),
            "candidate_universe_source_row_count": "",
            "candidate_universe_condition_stock_count": "",
            "candidate_universe_missing_required_columns": "",
            "replay_error": str(exc),
        }

    missing = sorted(PRICE_PULLBACK_CANDIDATE_REPLAY_REQUIRED_COLUMNS - set(candidates.columns))
    if missing:
        return {
            "comparison_basis": "production_all_candidates_source_row_replay",
            "comparison_stock_ids": set(),
            "candidate_universe_replay_status": "blocked_invalid_all_candidates_source_row_schema",
            "candidate_universe_snapshot_path": path.as_posix(),
            "candidate_universe_source_row_count": len(candidates),
            "candidate_universe_condition_stock_count": "",
            "candidate_universe_missing_required_columns": ";".join(missing),
            "replay_error": "",
        }

    mask = candidates.apply(cond_pullback, axis=1).fillna(False)
    matched = candidates.loc[mask].copy()
    stock_ids = {normalize_code(value) for value in matched["stock_id"].tolist()}
    stock_ids.discard("")
    return {
        "comparison_basis": "production_all_candidates_source_row_replay",
        "comparison_stock_ids": stock_ids,
        "candidate_universe_replay_status": "candidate_universe_replay_available",
        "candidate_universe_snapshot_path": path.as_posix(),
        "candidate_universe_source_row_count": len(candidates),
        "candidate_universe_condition_stock_count": len(stock_ids),
        "candidate_universe_missing_required_columns": "",
        "replay_error": "",
    }


def _price_pullback_gap_driver(
    *,
    has_research_date: bool,
    comparison_basis: str,
    published_unique: int,
    published_not_proxy_count: int,
    proxy_not_published_count: int,
) -> str:
    if not has_research_date:
        return "missing_research_frame_date"
    if published_not_proxy_count == 0 and proxy_not_published_count == 0:
        return "none_exact"
    if comparison_basis == "production_all_candidates_source_row_replay":
        if published_not_proxy_count and proxy_not_published_count:
            return "production_candidate_universe_bidirectional_row_gap"
        if published_not_proxy_count:
            return "published_rows_not_reproduced_by_production_candidate_universe_replay"
        return "production_candidate_universe_rows_not_in_published_snapshot"
    if proxy_not_published_count > max(published_unique, published_not_proxy_count):
        return "research_full_universe_proxy_exceeds_daily_candidate_publication_scope"
    if published_not_proxy_count and proxy_not_published_count:
        return "bidirectional_proxy_and_publication_gap"
    if published_not_proxy_count:
        return "published_rows_not_reproduced_by_research_proxy"
    return "research_proxy_rows_not_in_published_snapshot"


def _published_not_proxy_interpretation(count: int, comparison_basis: str) -> str:
    if count <= 0:
        return ""
    if comparison_basis == "production_all_candidates_source_row_replay":
        return (
            "published rows do not satisfy the production all_candidates cond_pullback replay; "
            "inspect dated source-row schema, merge keys, and condition drift before promotion"
        )
    return (
        "published rows do not satisfy the current research proxy; inspect feature parity, "
        "dated source columns, and snapshot lifecycle before promotion"
    )


def _proxy_not_published_interpretation(count: int, comparison_basis: str) -> str:
    if count <= 0:
        return ""
    if comparison_basis == "production_all_candidates_source_row_replay":
        return (
            "production all_candidates cond_pullback replay found stocks not on the published report surface; "
            "inspect report publication scope, duplicate merge, and dated snapshot alignment"
        )
    return (
        "research proxy runs on the full stock-day frame, while daily production starts from "
        "all_candidates/source-row eligibility and then writes the published report surface"
    )


def build_price_pullback_daily_row_parity_audit(
    df: pd.DataFrame,
    snapshot_dir: Path = DAILY_SNAPSHOT_DIR,
    generated_at: str | None = None,
) -> pd.DataFrame:
    generated = generated_at or now_text()
    columns = [
        "generated_at",
        "model_id",
        "snapshot_report_date",
        "research_frame_has_date",
        "outcome_research_frame_has_date",
        "source_row_research_frame_has_date",
        "research_frame_date_basis",
        "published_row_count",
        "published_unique_stock_count",
        "published_duplicate_stock_count",
        "research_proxy_unique_stock_count",
        "overlap_stock_count",
        "published_not_in_proxy_rows",
        "proxy_not_published_rows",
        "published_proxy_coverage_pct",
        "proxy_publish_precision_pct",
        "published_not_in_proxy_sample",
        "proxy_not_published_sample",
        "parity_scope",
        "published_surface",
        "research_proxy_scope",
        "comparison_basis",
        "candidate_universe_snapshot_path",
        "candidate_universe_source_row_count",
        "candidate_universe_condition_stock_count",
        "candidate_universe_missing_required_columns",
        "published_selection_semantics_values",
        "published_source_category_counts",
        "published_report_bucket_counts",
        "candidate_universe_replay_status",
        "parity_gap_driver",
        "published_not_in_proxy_interpretation",
        "proxy_not_published_interpretation",
        "next_required_replay_artifact",
        "parity_status",
        "parity_blocker",
    ]
    if df.empty:
        return pd.DataFrame(columns=columns)

    research = df.copy()
    research["_row_parity_date"] = research["date"].map(normalize_date)
    research["_row_parity_stock_id"] = research["stock_id"].map(normalize_code)
    outcome_research_dates = set(research["_row_parity_date"].astype(str))
    proxy_mask = current_price_pullback_baseline_proxy(research).fillna(False)
    proxy_rows = research.loc[
        proxy_mask
        & research["_row_parity_date"].astype(str).ne("")
        & research["_row_parity_stock_id"].astype(str).ne(""),
        ["_row_parity_date", "_row_parity_stock_id"],
    ].drop_duplicates()
    proxy_by_date = {
        date: set(part["_row_parity_stock_id"].astype(str))
        for date, part in proxy_rows.groupby("_row_parity_date")
    }

    rows: list[dict[str, object]] = []
    for snapshot_path in sorted(snapshot_dir.glob("daily_candidate_model_signals_for_report_*.csv")):
        report_date = _snapshot_date_from_path(snapshot_path)
        if not report_date:
            continue
        try:
            snapshot = pd.read_csv(snapshot_path, dtype=str, keep_default_na=False)
        except Exception as exc:
            rows.append(
                {
                    "generated_at": generated,
                    "model_id": "price_pullback_23ema",
                    "snapshot_report_date": report_date,
                    "research_frame_has_date": "False",
                    "outcome_research_frame_has_date": "False",
                    "source_row_research_frame_has_date": "False",
                    "research_frame_date_basis": "missing_research_frame_date",
                    "published_row_count": 0,
                    "published_unique_stock_count": 0,
                    "published_duplicate_stock_count": 0,
                    "research_proxy_unique_stock_count": 0,
                    "overlap_stock_count": 0,
                    "published_not_in_proxy_rows": 0,
                    "proxy_not_published_rows": 0,
                    "published_proxy_coverage_pct": "",
                    "proxy_publish_precision_pct": "",
                    "published_not_in_proxy_sample": "",
                    "proxy_not_published_sample": "",
                    "parity_scope": "signal_date_stock_id",
                    "published_surface": "daily_candidate_model_signals_for_report",
                    "research_proxy_scope": "full_stock_day_frame_current_price_pullback_baseline_proxy_without_daily_candidate_universe_replay",
                    "comparison_basis": "unavailable_published_snapshot",
                    "candidate_universe_snapshot_path": "",
                    "candidate_universe_source_row_count": "",
                    "candidate_universe_condition_stock_count": "",
                    "candidate_universe_missing_required_columns": "",
                    "published_selection_semantics_values": "",
                    "published_source_category_counts": "",
                    "published_report_bucket_counts": "",
                    "candidate_universe_replay_status": "blocked_unreadable_snapshot",
                    "parity_gap_driver": "unreadable_snapshot",
                    "published_not_in_proxy_interpretation": "",
                    "proxy_not_published_interpretation": "",
                    "next_required_replay_artifact": "readable published snapshot before candidate-universe replay can be assessed",
                    "parity_status": "blocked_unreadable_snapshot",
                    "parity_blocker": f"failed to read published daily snapshot: {exc}",
                }
            )
            continue

        if not {"model_id", "stock_id"}.issubset(snapshot.columns):
            rows.append(
                {
                    "generated_at": generated,
                    "model_id": "price_pullback_23ema",
                    "snapshot_report_date": report_date,
                    "research_frame_has_date": "False",
                    "outcome_research_frame_has_date": "False",
                    "source_row_research_frame_has_date": "False",
                    "research_frame_date_basis": "missing_research_frame_date",
                    "published_row_count": 0,
                    "published_unique_stock_count": 0,
                    "published_duplicate_stock_count": 0,
                    "research_proxy_unique_stock_count": 0,
                    "overlap_stock_count": 0,
                    "published_not_in_proxy_rows": 0,
                    "proxy_not_published_rows": 0,
                    "published_proxy_coverage_pct": "",
                    "proxy_publish_precision_pct": "",
                    "published_not_in_proxy_sample": "",
                    "proxy_not_published_sample": "",
                    "parity_scope": "signal_date_stock_id",
                    "published_surface": "daily_candidate_model_signals_for_report",
                    "research_proxy_scope": "full_stock_day_frame_current_price_pullback_baseline_proxy_without_daily_candidate_universe_replay",
                    "comparison_basis": "unavailable_published_snapshot",
                    "candidate_universe_snapshot_path": "",
                    "candidate_universe_source_row_count": "",
                    "candidate_universe_condition_stock_count": "",
                    "candidate_universe_missing_required_columns": "",
                    "published_selection_semantics_values": "",
                    "published_source_category_counts": "",
                    "published_report_bucket_counts": "",
                    "candidate_universe_replay_status": "blocked_invalid_snapshot_schema",
                    "parity_gap_driver": "invalid_snapshot_schema",
                    "published_not_in_proxy_interpretation": "",
                    "proxy_not_published_interpretation": "",
                    "next_required_replay_artifact": "valid published snapshot with model_id and stock_id",
                    "parity_status": "blocked_invalid_snapshot_schema",
                    "parity_blocker": "published daily snapshot missing model_id or stock_id",
                }
            )
            continue

        published = snapshot[snapshot["model_id"].astype(str).eq("price_pullback_23ema")].copy()
        published_stock_ids = [normalize_code(value) for value in published["stock_id"].tolist()]
        published_stock_ids = [stock_id for stock_id in published_stock_ids if stock_id]
        published_set = set(published_stock_ids)
        candidate_replay = _price_pullback_candidate_universe_replay(snapshot_dir, report_date)
        comparison_basis = safe_str(candidate_replay.get("comparison_basis", "")) or "full_research_frame_proxy"
        candidate_replay_set = candidate_replay.get("comparison_stock_ids")
        source_row_research_has_date = (
            comparison_basis == "production_all_candidates_source_row_replay"
            and isinstance(candidate_replay_set, set)
            and not safe_str(candidate_replay.get("replay_error", ""))
        )
        if isinstance(candidate_replay_set, set):
            proxy_set = candidate_replay_set
        else:
            proxy_set = proxy_by_date.get(report_date, set())
        overlap = published_set & proxy_set
        published_not_proxy = published_set - proxy_set
        proxy_not_published = proxy_set - published_set
        published_unique = len(published_set)
        proxy_unique = len(proxy_set)
        outcome_research_has_date = report_date in outcome_research_dates
        has_research_date = outcome_research_has_date or source_row_research_has_date
        date_basis_parts: list[str] = []
        if outcome_research_has_date:
            date_basis_parts.append("outcome_research_frame")
        if source_row_research_has_date:
            date_basis_parts.append("production_all_candidates_source_row_replay")
        research_frame_date_basis = ";".join(date_basis_parts) if date_basis_parts else "missing_research_frame_date"
        published_not_proxy_count = len(published_not_proxy)
        proxy_not_published_count = len(proxy_not_published)
        gap_driver = _price_pullback_gap_driver(
            has_research_date=has_research_date,
            comparison_basis=comparison_basis,
            published_unique=published_unique,
            published_not_proxy_count=published_not_proxy_count,
            proxy_not_published_count=proxy_not_published_count,
        )
        candidate_replay_status = safe_str(candidate_replay.get("candidate_universe_replay_status", ""))
        if comparison_basis == "production_all_candidates_source_row_replay" and candidate_replay_status == "candidate_universe_replay_available":
            candidate_replay_status = (
                "candidate_universe_replay_exact_match"
                if not published_not_proxy and not proxy_not_published
                else "candidate_universe_replay_row_gap"
            )

        if not has_research_date:
            parity_status = "blocked_missing_research_frame_date"
            parity_blocker = "research frame does not include this published snapshot date"
        elif published_not_proxy or proxy_not_published:
            parity_status = "blocked_not_exact_daily_row_parity"
            parity_blocker = (
                "research proxy does not exactly reproduce as-published daily price_pullback_23ema rows; "
                "daily candidate-universe/source-row eligibility and report publication scope must be replayed before promotion"
            )
        else:
            parity_status = "exact_daily_row_parity_pass"
            parity_blocker = ""

        rows.append(
            {
                "generated_at": generated,
                "model_id": "price_pullback_23ema",
                "snapshot_report_date": report_date,
                "research_frame_has_date": "True" if has_research_date else "False",
                "outcome_research_frame_has_date": "True" if outcome_research_has_date else "False",
                "source_row_research_frame_has_date": "True" if source_row_research_has_date else "False",
                "research_frame_date_basis": research_frame_date_basis,
                "published_row_count": len(published),
                "published_unique_stock_count": published_unique,
                "published_duplicate_stock_count": len(published_stock_ids) - published_unique,
                "research_proxy_unique_stock_count": proxy_unique,
                "overlap_stock_count": len(overlap),
                "published_not_in_proxy_rows": published_not_proxy_count,
                "proxy_not_published_rows": proxy_not_published_count,
                "published_proxy_coverage_pct": (
                    round(len(overlap) / published_unique * 100.0, 2) if published_unique else ""
                ),
                "proxy_publish_precision_pct": round(len(overlap) / proxy_unique * 100.0, 2) if proxy_unique else "",
                "published_not_in_proxy_sample": _stock_id_sample(published_not_proxy),
                "proxy_not_published_sample": _stock_id_sample(proxy_not_published),
                "parity_scope": "signal_date_stock_id",
                "published_surface": "daily_candidate_model_signals_for_report",
                "research_proxy_scope": (
                    "production_all_candidates_source_row_cond_pullback_replay"
                    if comparison_basis == "production_all_candidates_source_row_replay"
                    else "full_stock_day_frame_current_price_pullback_baseline_proxy_without_daily_candidate_universe_replay"
                ),
                "comparison_basis": comparison_basis,
                "candidate_universe_snapshot_path": candidate_replay.get("candidate_universe_snapshot_path", ""),
                "candidate_universe_source_row_count": candidate_replay.get("candidate_universe_source_row_count", ""),
                "candidate_universe_condition_stock_count": candidate_replay.get(
                    "candidate_universe_condition_stock_count", ""
                ),
                "candidate_universe_missing_required_columns": candidate_replay.get(
                    "candidate_universe_missing_required_columns", ""
                ),
                "published_selection_semantics_values": _value_counts_summary(
                    published["selection_semantics"] if "selection_semantics" in published.columns else pd.Series(dtype=str)
                ),
                "published_source_category_counts": _value_counts_summary(
                    published["original_category"] if "original_category" in published.columns else pd.Series(dtype=str)
                ),
                "published_report_bucket_counts": _value_counts_summary(
                    published["report_bucket"] if "report_bucket" in published.columns else pd.Series(dtype=str)
                ),
                "candidate_universe_replay_status": candidate_replay_status,
                "parity_gap_driver": gap_driver,
                "published_not_in_proxy_interpretation": _published_not_proxy_interpretation(
                    published_not_proxy_count, comparison_basis
                ),
                "proxy_not_published_interpretation": _proxy_not_published_interpretation(
                    proxy_not_published_count, comparison_basis
                ),
                "next_required_replay_artifact": (
                    "historical all_candidates/source-row snapshot with candidate_source_type, "
                    "candidate_line, report eligibility, source_row_index, and the exact model input columns"
                ),
                "parity_status": parity_status,
                "parity_blocker": parity_blocker,
            }
        )
    return pd.DataFrame(rows, columns=columns)


def write_price_pullback_daily_row_parity_audit(row_parity: pd.DataFrame) -> None:
    write_csv(row_parity, PRICE_PULLBACK_DAILY_ROW_PARITY_CSV)
    write_csv(row_parity, PRICE_PULLBACK_DAILY_ROW_PARITY_HISTORY_CSV)
    write_csv(row_parity, DOCS_PRICE_PULLBACK_DAILY_ROW_PARITY_CSV)
    counts = (
        row_parity["parity_status"].value_counts().reset_index()
        if not row_parity.empty and "parity_status" in row_parity.columns
        else pd.DataFrame(columns=["parity_status", "count"])
    )
    if not counts.empty:
        counts.columns = ["parity_status", "count"]
    lines = [
        "# Price Pullback 23EMA Daily Row Parity Audit",
        "",
        f"- generated_at: `{now_text()}`",
        "- model_id: `price_pullback_23ema`",
        "- scope: compare as-published daily snapshot rows to the research production proxy at `signal_date + stock_id` level",
        "- rule: any missing or extra stock row keeps the model blocked from daily operation promotion",
        "- gap interpretation: the research proxy currently runs on the full stock-day frame; exact parity still needs dated daily candidate-universe/source-row replay before promotion",
        "- date rule: `outcome_research_frame_has_date` tracks mature next-open/D+N outcome rows; `source_row_research_frame_has_date` tracks dated all_candidates/source-row replay for as-of daily row parity.",
        "- note: this audit does not change production selection, scoring, ranking, or PDF output",
        "",
        "## Status Summary",
        "",
        markdown_table(counts, counts.columns.tolist()) if not counts.empty else "No parity rows.",
        "",
        "## Snapshot Detail",
        "",
        markdown_table(
            row_parity,
            [
                "snapshot_report_date",
                "research_frame_has_date",
                "outcome_research_frame_has_date",
                "source_row_research_frame_has_date",
                "research_frame_date_basis",
                "published_unique_stock_count",
                "research_proxy_unique_stock_count",
                "overlap_stock_count",
                "published_not_in_proxy_rows",
                "proxy_not_published_rows",
                "published_proxy_coverage_pct",
                "proxy_publish_precision_pct",
                "parity_gap_driver",
                "comparison_basis",
                "candidate_universe_condition_stock_count",
                "candidate_universe_replay_status",
                "parity_status",
                "parity_blocker",
            ],
            limit=120,
        ),
    ]
    PRICE_PULLBACK_DAILY_ROW_PARITY_MD.write_text(
        "\n".join(lines).rstrip() + "\n",
        encoding="utf-8",
        newline="\n",
    )
    DOCS_PRICE_PULLBACK_DAILY_ROW_PARITY_MD.write_text(
        PRICE_PULLBACK_DAILY_ROW_PARITY_MD.read_text(encoding="utf-8"),
        encoding="utf-8",
        newline="\n",
    )


def write_model_parity(parity: pd.DataFrame) -> None:
    write_csv(parity, OUT_PARITY_CSV)
    write_csv(parity, DOCS_PARITY_CSV)
    counts = (
        parity["research_baseline_status"].value_counts().reset_index()
        if not parity.empty
        else pd.DataFrame(columns=["research_baseline_status", "count"])
    )
    if not counts.empty:
        counts.columns = ["research_baseline_status", "count"]
    lines = [
        "# Daily Model Research Baseline Parity",
        "",
        f"- generated_at: `{now_text()}`",
        "- purpose: verify that every daily production core model has a research production-baseline row before parameter variants are compared",
        "- production_parity: historical research fields can replay the production baseline directly",
        "- production_proxy / proxy_only: baseline exists, but one or more production fields are not fully available point-in-time in the research frame",
        "- rule: variants must compare against the production_baseline row of the same model_id; proxy rows cannot be promoted without resolving blockers",
        "",
        "## Status Summary",
        "",
        markdown_table(counts, counts.columns.tolist()) if not counts.empty else "No parity rows.",
        "",
        "## Model Parity Detail",
        "",
        markdown_table(
            parity,
            [
                "model_id",
                "research_baseline_status",
                "research_baseline_parameter_set_id",
                "research_variant_count",
                "baseline_selected_stock_days",
                "baseline_selected_unique_stocks",
                "parity_blocker",
                "completion_rule",
            ],
            limit=80,
        ),
    ]
    OUT_PARITY_MD.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8", newline="\n")
    DOCS_PARITY_MD.write_text(OUT_PARITY_MD.read_text(encoding="utf-8"), encoding="utf-8", newline="\n")


def write_markdown(summary: pd.DataFrame, detail: pd.DataFrame, coverage: dict[str, object]) -> None:
    summary_sorted = summary.sort_values(
        ["model_id", "sample_status", "best_avg_close_return_pct"],
        ascending=[True, True, False],
    ).reset_index(drop=True)
    review = summary_sorted[summary_sorted["selected_stock_days"] >= MIN_REVIEW_SAMPLE].copy()
    top = review.sort_values(["best_avg_close_return_pct", "selected_stock_days"], ascending=[False, False]).head(30)
    lines = [
        "# Daily Model Parameter Research",
        "",
        f"- generated_at: `{now_text()}`",
        f"- price_history_files: `{coverage.get('price_history_files')}`",
        f"- max_price_rows: `{coverage.get('max_price_rows')}`",
        f"- data_range: `{coverage.get('date_min')}` ~ `{coverage.get('date_max')}`",
        "- entry_basis: `signal_date_next_open`",
        "- close_return_definition: `(D+n close / next trading day open - 1)`",
        "- high_return_definition: `(max intraday high through D+n / next trading day open - 1)`",
        "",
        "## Data Quality",
        "",
        "- This is first-pass parameter research using the current repo price history.",
        "- If sample_status is `small_sample_review_only` or `insufficient_sample`, do not treat the parameter as a final model weight.",
        "- Revenue historical panel is not complete in price history, so the revenue-unreacted research row only validates the price-range component.",
        "",
        "## Top Parameter Sets By Avg Close Return",
        "",
        markdown_table(
            top,
            [
                "model_id",
                "parameter_set_id",
                "parameter_role",
                "production_parity_status",
                "selected_stock_days",
                "selected_unique_stocks",
                "best_close_horizon_d1_d10",
                "best_close_win_rate_pct",
                "best_avg_close_return_pct",
                "sample_status",
                "parameter_summary",
            ],
            limit=30,
        ),
        "",
        "## All Model Parameter Summary",
        "",
        markdown_table(
            summary_sorted,
            [
                "model_id",
                "parameter_set_id",
                "parameter_role",
                "production_parity_status",
                "selected_stock_days",
                "d1_close_win_rate_pct",
                "d3_close_win_rate_pct",
                "d5_close_win_rate_pct",
                "d10_close_win_rate_pct",
                "d5_avg_close_return_pct",
                "d10_avg_close_return_pct",
                "sample_status",
                "parameter_summary",
            ],
            limit=200,
        ),
    ]
    OUT_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")
    DOCS_LATEST_DIR.mkdir(parents=True, exist_ok=True)
    DOCS_MD.write_text(OUT_MD.read_text(encoding="utf-8"), encoding="utf-8")

    focus = detail[detail["horizon"].isin(["D+1", "D+2", "D+3", "D+4", "D+5", "D+6", "D+7", "D+8", "D+9", "D+10"])].copy()
    lines2 = [
        "# Daily Model Parameter Research - Horizon Detail",
        "",
        f"- generated_at: `{now_text()}`",
        "- entry_basis: `signal_date_next_open`",
        "",
        markdown_table(
            focus,
            [
                "model_id",
                "parameter_set_id",
                "horizon",
                "mature_count",
                "close_win_rate_pct",
                "avg_close_return_pct",
                "median_close_return_pct",
                "avg_high_return_pct",
                "high_5pct_hit_rate_pct",
            ],
            limit=300,
        ),
    ]
    OUT_DETAIL_MD.write_text("\n".join(lines2) + "\n", encoding="utf-8")
    DOCS_DETAIL_MD.write_text(OUT_DETAIL_MD.read_text(encoding="utf-8"), encoding="utf-8")


def coverage_stats() -> dict[str, object]:
    rows = []
    for path in Path("data/stock_price_history").glob("*.csv"):
        try:
            df = pd.read_csv(path, usecols=["date"])
        except Exception:
            continue
        if df.empty:
            continue
        rows.append((len(df), str(df["date"].min()), str(df["date"].max())))
    if not rows:
        return {"price_history_files": 0, "max_price_rows": 0, "date_min": "", "date_max": ""}
    return {
        "price_history_files": len(rows),
        "max_price_rows": max(r[0] for r in rows),
        "date_min": min(r[1] for r in rows),
        "date_max": max(r[2] for r in rows),
    }


def main() -> int:
    df = build_research_frame()
    if df.empty:
        raise RuntimeError("No price history available for model parameter research")

    summaries: list[dict[str, object]] = []
    details: list[dict[str, object]] = []
    for spec in rule_specs():
        summary, detail_rows = summarize_rule(df, spec)
        summaries.append(summary)
        details.extend(detail_rows)

    summary_df = pd.DataFrame(summaries)
    detail_df = pd.DataFrame(details)
    coverage = coverage_stats()
    parity_df = build_model_parity(summary_df)
    price_pullback_operation_df = build_price_pullback_operation_research(df)
    price_pullback_time_cost_df = build_price_pullback_time_cost_backtest(df)
    price_pullback_operation_module_df = build_price_pullback_operation_module_research(df)
    price_pullback_feature_confirmation_df = build_price_pullback_feature_confirmation_research(df)
    price_pullback_daily_row_parity_df = build_price_pullback_daily_row_parity_audit(df)
    price_pullback_decision_audit_df = build_price_pullback_model_decision_audit(
        price_pullback_operation_module_df,
        price_pullback_feature_confirmation_df,
        price_pullback_daily_row_parity_df,
    )

    write_csv(summary_df, OUT_CSV)
    write_csv(detail_df, OUT_DETAIL_CSV)
    HISTORY_DIR.mkdir(parents=True, exist_ok=True)
    write_csv(summary_df, HISTORY_CSV)
    DOCS_LATEST_DIR.mkdir(parents=True, exist_ok=True)
    write_csv(summary_df, DOCS_CSV)
    write_csv(detail_df, DOCS_DETAIL_CSV)
    write_markdown(summary_df, detail_df, coverage)
    write_model_parity(parity_df)
    write_price_pullback_operation_research(price_pullback_operation_df)
    write_price_pullback_time_cost_backtest(price_pullback_time_cost_df)
    write_price_pullback_operation_module_research(price_pullback_operation_module_df)
    write_price_pullback_feature_confirmation_research(price_pullback_feature_confirmation_df)
    write_price_pullback_daily_row_parity_audit(price_pullback_daily_row_parity_df)
    write_price_pullback_model_decision_audit(price_pullback_decision_audit_df)

    print(f"Saved {OUT_CSV} rows={len(summary_df)}")
    print(f"Saved {OUT_DETAIL_CSV} rows={len(detail_df)}")
    print(f"Saved {OUT_PARITY_CSV} rows={len(parity_df)}")
    print(f"Saved {PRICE_PULLBACK_OPERATION_CSV} rows={len(price_pullback_operation_df)}")
    print(f"Saved {PRICE_PULLBACK_TIME_COST_CSV} rows={len(price_pullback_time_cost_df)}")
    print(f"Saved {PRICE_PULLBACK_OPERATION_MODULE_CSV} rows={len(price_pullback_operation_module_df)}")
    print(f"Saved {PRICE_PULLBACK_FEATURE_CONFIRMATION_CSV} rows={len(price_pullback_feature_confirmation_df)}")
    print(f"Saved {PRICE_PULLBACK_DAILY_ROW_PARITY_CSV} rows={len(price_pullback_daily_row_parity_df)}")
    print(f"Saved {PRICE_PULLBACK_DECISION_AUDIT_CSV} rows={len(price_pullback_decision_audit_df)}")
    print(f"Saved {OUT_MD}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

