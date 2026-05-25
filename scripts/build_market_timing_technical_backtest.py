from __future__ import annotations

from pathlib import Path
import math
import sys
import warnings
from typing import Any

import pandas as pd
from pandas.errors import PerformanceWarning

warnings.simplefilter("ignore", PerformanceWarning)
warnings.simplefilter("ignore", FutureWarning)

sys.path.insert(0, str(Path(__file__).resolve().parent))

from tracking_utils import (  # noqa: E402
    LATEST_DIR,
    STOCK_PRICE_HISTORY_DIR,
    classify_market_regime,
    load_market_index_history,
    markdown_table,
    normalize_date,
    now_text,
    read_csv,
    safe_str,
    to_number,
    write_csv,
)


MARKET_TIMING_DIR = Path("output/history/market_timing")
FEATURE_PANEL = MARKET_TIMING_DIR / "market_technical_feature_panel.csv"
BREADTH_HISTORY = MARKET_TIMING_DIR / "market_breadth_history.csv"
EVENT_LOG = MARKET_TIMING_DIR / "market_technical_event_log.csv"

BACKTEST_CSV = LATEST_DIR / "market_timing_backtest_latest.csv"
BACKTEST_MD = LATEST_DIR / "market_timing_backtest_latest.md"
REGIME_CSV = LATEST_DIR / "market_timing_regime_effectiveness_latest.csv"
REGIME_MD = LATEST_DIR / "market_timing_regime_effectiveness_latest.md"
COMPOSITE_CSV = LATEST_DIR / "market_timing_composite_backtest_latest.csv"
COMPOSITE_MD = LATEST_DIR / "market_timing_composite_backtest_latest.md"
PACKET_MD = LATEST_DIR / "market_timing_chatgpt_packet_latest.md"

FUTURES_OPTIONS_CSV = LATEST_DIR / "futures_options_indicators_latest.csv"
MARKET_REGIME_CSV = LATEST_DIR / "market_regime_latest.csv"
DAILY_SIGNAL_LOG = Path("output/history/daily_candidates/daily_candidate_signal_log.csv")

HORIZONS = [1, 3, 5, 10, 20, 40, 60]
INDEX_LIST = ["TWSE", "TPEX"]


def pct(current: Any, base: Any) -> float:
    current_num = to_number(current)
    base_num = to_number(base)
    if math.isnan(current_num) or math.isnan(base_num) or base_num == 0:
        return math.nan
    return (current_num / base_num - 1) * 100


def bool_series(series: pd.Series) -> pd.Series:
    return series.fillna(False).astype(bool)


def rolling_percentile_last(series: pd.Series, window: int = 120) -> pd.Series:
    def rank_last(values: pd.Series) -> float:
        values = pd.Series(values).dropna()
        if values.empty:
            return math.nan
        return float((values <= values.iloc[-1]).mean() * 100)

    return series.rolling(window, min_periods=max(5, min(window, 20))).apply(rank_last, raw=False)


def rsi(close: pd.Series, period: int) -> pd.Series:
    delta = close.diff()
    gain = delta.clip(lower=0).rolling(period, min_periods=period).mean()
    loss = (-delta.clip(upper=0)).rolling(period, min_periods=period).mean()
    rs = gain / loss.replace(0, math.nan)
    result = 100 - (100 / (1 + rs))
    return result.fillna(50)


def add_adx(part: pd.DataFrame) -> pd.DataFrame:
    high = part["high"]
    low = part["low"]
    close = part["close"]
    up_move = high.diff()
    down_move = -low.diff()
    plus_dm = up_move.where((up_move > down_move) & (up_move > 0), 0)
    minus_dm = down_move.where((down_move > up_move) & (down_move > 0), 0)
    tr = pd.concat(
        [
            high - low,
            (high - close.shift(1)).abs(),
            (low - close.shift(1)).abs(),
        ],
        axis=1,
    ).max(axis=1)
    atr = tr.rolling(14, min_periods=14).mean().replace(0, math.nan)
    plus_di = 100 * plus_dm.rolling(14, min_periods=14).mean() / atr
    minus_di = 100 * minus_dm.rolling(14, min_periods=14).mean() / atr
    dx = ((plus_di - minus_di).abs() / (plus_di + minus_di).replace(0, math.nan)) * 100
    part["adx14"] = dx.rolling(14, min_periods=14).mean()
    part["plus_di14"] = plus_di
    part["minus_di14"] = minus_di
    part["adx_trend_plus_di_dominant"] = (part["adx14"] >= 20) & (part["plus_di14"] > part["minus_di14"])
    return part


def normalize_index_history() -> tuple[pd.DataFrame, list[str]]:
    df = load_market_index_history(update_if_missing=True)
    notes: list[str] = []
    if df.empty:
        return df, ["market_index_history_missing"]

    df = df.copy()
    rename = {"index_code": "index_id", "date": "trade_date"}
    df = df.rename(columns=rename)
    df["trade_date"] = df["trade_date"].map(normalize_date)
    df = df[df["trade_date"] != ""].copy()
    df["index_id"] = df["index_id"].astype(str).str.upper()
    df = df[df["index_id"].isin(INDEX_LIST)].copy()
    if df.empty:
        return df, ["market_index_history_no_twse_tpex"]

    for col in ["open", "high", "low"]:
        if col not in df.columns:
            df[col] = df["close"]
            notes.append(f"{col}_unavailable_filled_with_close")
    for col in ["volume", "turnover_value", "value"]:
        if col not in df.columns:
            df[col] = math.nan
    if "turnover_value" not in df.columns and "value" in df.columns:
        df["turnover_value"] = df["value"]
    for col in ["open", "high", "low", "close", "volume", "turnover_value"]:
        df[col] = pd.to_numeric(df[col], errors="coerce")

    frames: list[pd.DataFrame] = []
    for code, part in df.sort_values(["index_id", "trade_date"]).groupby("index_id", sort=False):
        part = part.copy().reset_index(drop=True)
        date_series = pd.to_datetime(part["trade_date"], format="%Y%m%d", errors="coerce")
        gaps = date_series.diff().dt.days.fillna(1)
        if (gaps > 14).any():
            last_gap_idx = int(gaps[gaps > 14].index.max())
            notes.append(f"{code}_history_had_large_gap_keep_latest_continuous_segment")
            part = part.iloc[last_gap_idx:].copy().reset_index(drop=True)
        close = part["close"]
        high = part["high"]
        low = part["low"]
        volume = part["volume"]

        part["index_name"] = part.get("index_name", part["index_id"])

        for window in [5, 10, 20, 60, 120, 240]:
            part[f"ma{window}"] = close.rolling(window, min_periods=1).mean()
            part[f"distance_ma{window}_pct"] = (close / part[f"ma{window}"] - 1) * 100
            part[f"ma{window}_slope_5d"] = part[f"ma{window}"].pct_change(5) * 100

        for span in [12, 23, 26, 50, 200]:
            part[f"ema{span}"] = close.ewm(span=span, adjust=False).mean()
            part[f"distance_ema{span}_pct"] = (close / part[f"ema{span}"] - 1) * 100
            part[f"ema{span}_slope_5d"] = part[f"ema{span}"].pct_change(5) * 100

        part["bullish_ma_alignment"] = (part["ma5"] > part["ma20"]) & (part["ma20"] > part["ma60"])
        part["bearish_ma_alignment"] = (part["ma5"] < part["ma20"]) & (part["ma20"] < part["ma60"])
        part["bullish_ema_alignment"] = (part["ema12"] > part["ema26"]) & (part["ema26"] > part["ema50"])
        part["bearish_ema_alignment"] = (part["ema12"] < part["ema26"]) & (part["ema26"] < part["ema50"])
        for ma in [20, 60]:
            part[f"price_above_ma{ma}"] = close >= part[f"ma{ma}"]
            part[f"price_below_ma{ma}"] = close < part[f"ma{ma}"]
        part["price_above_ema23"] = close >= part["ema23"]
        part["price_below_ema23"] = close < part["ema23"]
        ma_spread = (part[["ma5", "ma20", "ma60"]].max(axis=1) / part[["ma5", "ma20", "ma60"]].min(axis=1) - 1) * 100
        ema_spread = (part[["ema12", "ema26", "ema50"]].max(axis=1) / part[["ema12", "ema26", "ema50"]].min(axis=1) - 1) * 100
        part["ma_convergence"] = ma_spread <= ma_spread.rolling(60, min_periods=10).quantile(0.25)
        part["ma_expansion"] = ma_spread >= ma_spread.rolling(60, min_periods=10).quantile(0.75)
        part["ema_convergence"] = ema_spread <= ema_spread.rolling(60, min_periods=10).quantile(0.25)
        part["ema_expansion"] = ema_spread >= ema_spread.rolling(60, min_periods=10).quantile(0.75)

        cross_pairs = [(5, 20), (20, 60), (60, 120)]
        for fast, slow in cross_pairs:
            fast_col = part[f"ma{fast}"]
            slow_col = part[f"ma{slow}"]
            part[f"golden_cross_ma{fast}_ma{slow}"] = (fast_col >= slow_col) & (fast_col.shift(1) < slow_col.shift(1))
            part[f"death_cross_ma{fast}_ma{slow}"] = (fast_col < slow_col) & (fast_col.shift(1) >= slow_col.shift(1))
        part["golden_cross_ema12_ema26"] = (part["ema12"] >= part["ema26"]) & (part["ema12"].shift(1) < part["ema26"].shift(1))
        part["death_cross_ema12_ema26"] = (part["ema12"] < part["ema26"]) & (part["ema12"].shift(1) >= part["ema26"].shift(1))

        part["macd_dif"] = part["ema12"] - part["ema26"]
        part["macd_dea"] = part["macd_dif"].ewm(span=9, adjust=False).mean()
        part["macd_signal"] = part["macd_dea"]
        part["macd_hist"] = part["macd_dif"] - part["macd_dea"]
        part["macd_hist_change_1d"] = part["macd_hist"].diff(1)
        part["macd_hist_change_3d"] = part["macd_hist"].diff(3)
        part["macd_bull_cross"] = (part["macd_dif"] >= part["macd_dea"]) & (part["macd_dif"].shift(1) < part["macd_dea"].shift(1))
        part["macd_bear_cross"] = (part["macd_dif"] < part["macd_dea"]) & (part["macd_dif"].shift(1) >= part["macd_dea"].shift(1))
        part["macd_above_zero"] = part["macd_dif"] > 0
        part["macd_below_zero"] = part["macd_dif"] < 0
        part["macd_hist_turn_positive"] = (part["macd_hist"] > 0) & (part["macd_hist"].shift(1) <= 0)
        part["macd_hist_turn_negative"] = (part["macd_hist"] < 0) & (part["macd_hist"].shift(1) >= 0)
        part["macd_dif_low_cross_signal"] = part["macd_bull_cross"] & (part["macd_dif"] < 0)
        part["macd_bullish_divergence"] = False
        part["macd_bearish_divergence"] = False

        part["rsi6"] = rsi(close, 6)
        part["rsi14"] = rsi(close, 14)
        part["rsi14_overbought_70"] = part["rsi14"] >= 70
        part["rsi14_oversold_30"] = part["rsi14"] <= 30
        part["rsi14_rebound_from_oversold"] = (part["rsi14"] > 30) & (part["rsi14"].shift(1) <= 30)
        part["rsi14_fall_from_overbought"] = (part["rsi14"] < 70) & (part["rsi14"].shift(1) >= 70)
        part["rsi_bullish_divergence"] = False
        part["rsi_bearish_divergence"] = False
        for window in [5, 10, 20]:
            part[f"roc_{window}"] = close.pct_change(window) * 100
            part[f"momentum_{window}"] = close - close.shift(window)

        highest14 = high.rolling(14, min_periods=1).max()
        lowest14 = low.rolling(14, min_periods=1).min()
        part["williams_r14"] = -100 * (highest14 - close) / (highest14 - lowest14).replace(0, math.nan)
        part["williams_oversold"] = part["williams_r14"] <= -80
        part["williams_overbought"] = part["williams_r14"] >= -20
        part["williams_rebound"] = (part["williams_r14"] > -80) & (part["williams_r14"].shift(1) <= -80)
        tp = (high + low + close) / 3
        tp_ma = tp.rolling(20, min_periods=20).mean()
        mean_dev = (tp - tp_ma).abs().rolling(20, min_periods=20).mean()
        part["cci20"] = (tp - tp_ma) / (0.015 * mean_dev.replace(0, math.nan))
        part["cci_over_100"] = part["cci20"] >= 100
        part["cci_below_minus_100"] = part["cci20"] <= -100
        part["cci_rebound_from_low"] = (part["cci20"] > -100) & (part["cci20"].shift(1) <= -100)
        part["cci_fall_from_high"] = (part["cci20"] < 100) & (part["cci20"].shift(1) >= 100)

        low9 = low.rolling(9, min_periods=1).min()
        high9 = high.rolling(9, min_periods=1).max()
        part["rsv9"] = ((close - low9) / (high9 - low9).replace(0, math.nan) * 100).fillna(50)
        part["k_value"] = part["rsv9"].ewm(alpha=1 / 3, adjust=False).mean()
        part["d_value"] = part["k_value"].ewm(alpha=1 / 3, adjust=False).mean()
        part["j_value"] = 3 * part["k_value"] - 2 * part["d_value"]
        part["kd_bull_cross"] = (part["k_value"] >= part["d_value"]) & (part["k_value"].shift(1) < part["d_value"].shift(1))
        part["kd_bear_cross"] = (part["k_value"] < part["d_value"]) & (part["k_value"].shift(1) >= part["d_value"].shift(1))
        part["kd_overbought"] = (part["k_value"] >= 80) & (part["d_value"] >= 80)
        part["kd_oversold"] = (part["k_value"] <= 20) & (part["d_value"] <= 20)
        part["kd_low_golden_cross"] = part["kd_bull_cross"] & (part["k_value"] <= 30)
        part["kd_high_death_cross"] = part["kd_bear_cross"] & (part["k_value"] >= 70)
        part["kd_value_rising_3d"] = part["k_value"] > part["k_value"].shift(3)
        part["kd_value_falling_3d"] = part["k_value"] < part["k_value"].shift(3)
        part["kd_bullish_divergence"] = False
        part["kd_bearish_divergence"] = False
        part["kd_overbought_persistence_days"] = consecutive_flag_count(part["kd_overbought"])
        part["kd_oversold_persistence_days"] = consecutive_flag_count(part["kd_oversold"])

        part["bb_mid_20"] = close.rolling(20, min_periods=1).mean()
        bb_std = close.rolling(20, min_periods=2).std()
        part["bb_upper_20"] = part["bb_mid_20"] + 2 * bb_std
        part["bb_lower_20"] = part["bb_mid_20"] - 2 * bb_std
        part["bb_width_20"] = (part["bb_upper_20"] - part["bb_lower_20"]) / part["bb_mid_20"].replace(0, math.nan) * 100
        part["bb_width_percentile_120d"] = rolling_percentile_last(part["bb_width_20"], 120)
        part["close_above_bb_upper"] = close > part["bb_upper_20"]
        part["close_below_bb_lower"] = close < part["bb_lower_20"]
        part["close_reenter_from_lower"] = (close >= part["bb_lower_20"]) & (close.shift(1) < part["bb_lower_20"].shift(1))
        part["close_reenter_from_upper"] = (close <= part["bb_upper_20"]) & (close.shift(1) > part["bb_upper_20"].shift(1))
        part["bollinger_squeeze"] = part["bb_width_percentile_120d"] <= 20
        part["bollinger_expansion"] = part["bb_width_percentile_120d"] >= 80
        part["bollinger_squeeze_breakout"] = part["close_above_bb_upper"] & bool_series(part["bollinger_squeeze"].shift(1).rolling(5, min_periods=1).max())
        part["bollinger_upper_breakout_with_volume"] = part["bollinger_squeeze_breakout"] & (part["volume_ratio_20d"] >= 1.2 if "volume_ratio_20d" in part else False)
        part["bollinger_upper_breakout_long_upper_shadow"] = part["close_above_bb_upper"] & (upper_shadow_ratio(part) >= 0.4)
        part["bollinger_lower_breakdown_panic"] = part["close_below_bb_lower"] & (part["rsi14"] <= 30)

        tr = pd.concat([(high - low), (high - close.shift(1)).abs(), (low - close.shift(1)).abs()], axis=1).max(axis=1)
        part["atr14"] = tr.rolling(14, min_periods=14).mean()
        part["atr14_pct"] = part["atr14"] / close.replace(0, math.nan) * 100
        part["atr_percentile_120d"] = rolling_percentile_last(part["atr14_pct"], 120)
        part["keltner_mid"] = part["ema23"]
        part["keltner_upper"] = part["keltner_mid"] + 2 * part["atr14"]
        part["keltner_lower"] = part["keltner_mid"] - 2 * part["atr14"]
        part["close_above_keltner_upper"] = close > part["keltner_upper"]
        part["close_below_keltner_lower"] = close < part["keltner_lower"]
        for window in [20, 60]:
            part[f"donchian_high_{window}"] = high.rolling(window, min_periods=1).max()
            part[f"donchian_low_{window}"] = low.rolling(window, min_periods=1).min()
            part[f"donchian_breakout_{window}d"] = close >= part[f"donchian_high_{window}"].shift(1)
            part[f"donchian_breakdown_{window}d"] = close <= part[f"donchian_low_{window}"].shift(1)
        for window in [10, 20, 60]:
            part[f"volatility_{window}d"] = close.pct_change().rolling(window, min_periods=window).std() * math.sqrt(252) * 100
        part["volatility_percentile_120d"] = rolling_percentile_last(part["volatility_20d"], 120)
        part["high_low_range_pct"] = (high - low) / close.replace(0, math.nan) * 100
        part["volatility_expansion_after_squeeze"] = part["bollinger_squeeze"].shift(1).fillna(False) & part["bollinger_expansion"]
        part["volatility_reversal_after_expansion"] = part["bollinger_expansion"].shift(1).fillna(False) & (part["bb_width_percentile_120d"] < 80)

        part["volume_ma5"] = volume.rolling(5, min_periods=1).mean()
        part["volume_ma20"] = volume.rolling(20, min_periods=1).mean()
        part["volume_ratio_5d"] = volume / part["volume_ma5"].replace(0, math.nan)
        part["volume_ratio_20d"] = volume / part["volume_ma20"].replace(0, math.nan)
        part["bollinger_upper_breakout_with_volume"] = part["bollinger_squeeze_breakout"] & (part["volume_ratio_20d"] >= 1.2)
        part["volume_expansion"] = part["volume_ratio_20d"] >= 1.2
        part["volume_contraction"] = part["volume_ratio_20d"] <= 0.8
        ret1 = close.pct_change() * 100
        part["price_up_volume_up"] = (ret1 > 0) & (part["volume_ratio_20d"] > 1)
        part["price_up_volume_down"] = (ret1 > 0) & (part["volume_ratio_20d"] < 1)
        part["price_down_volume_up"] = (ret1 < 0) & (part["volume_ratio_20d"] > 1)
        part["price_down_volume_down"] = (ret1 < 0) & (part["volume_ratio_20d"] < 1)
        part["high_volume_breakout"] = part["donchian_breakout_20d"] & (part["volume_ratio_20d"] >= 1.2)
        part["high_volume_down_day"] = (ret1 < -1) & (part["volume_ratio_20d"] >= 1.5)
        part["high_volume_long_black"] = (close < part["open"]) & (part["volume_ratio_20d"] >= 1.5) & (ret1 < -1)
        part["volume_price_bullish"] = part["price_up_volume_up"] | part["high_volume_breakout"]
        part["volume_price_bearish"] = part["price_down_volume_up"] | part["high_volume_long_black"]
        part["index_new_high_volume_divergence"] = part["donchian_breakout_60d"] & (part["volume_ratio_20d"] < 0.9)
        part["obv"] = (volume.fillna(0) * ret1.apply(lambda x: 1 if x > 0 else (-1 if x < 0 else 0))).cumsum()
        part["obv_ma20"] = part["obv"].rolling(20, min_periods=1).mean()
        part["obv_above_ma20"] = part["obv"] >= part["obv_ma20"]
        part["obv_slope_5d"] = part["obv"].diff(5)
        part["obv_price_divergence_bullish"] = False
        part["obv_price_divergence_bearish"] = False
        raw_money_flow = tp * volume
        positive_flow = raw_money_flow.where(tp > tp.shift(1), 0).rolling(14, min_periods=14).sum()
        negative_flow = raw_money_flow.where(tp < tp.shift(1), 0).rolling(14, min_periods=14).sum()
        mfi_ratio = positive_flow / negative_flow.replace(0, math.nan)
        part["mfi14"] = 100 - (100 / (1 + mfi_ratio))
        part["mfi_overbought"] = part["mfi14"] >= 80
        part["mfi_oversold"] = part["mfi14"] <= 20
        part["mfi_rebound"] = (part["mfi14"] > 20) & (part["mfi14"].shift(1) <= 20)
        part["vwap_daily"] = math.nan
        part["close_above_vwap"] = False
        part["close_below_vwap"] = False
        clv = ((close - low) - (high - close)) / (high - low).replace(0, math.nan)
        part["ad_line"] = (clv.fillna(0) * volume.fillna(0)).cumsum()
        part["ad_line_slope_5d"] = part["ad_line"].diff(5)
        part["ad_line_bullish_divergence"] = False
        part["ad_line_bearish_divergence"] = False
        mfv = clv.fillna(0) * volume.fillna(0)
        part["cmf20"] = mfv.rolling(20, min_periods=20).sum() / volume.rolling(20, min_periods=20).sum().replace(0, math.nan)
        part["cmf_positive"] = part["cmf20"] > 0
        part["cmf_negative"] = part["cmf20"] < 0
        part["cmf_turn_positive"] = (part["cmf20"] > 0) & (part["cmf20"].shift(1) <= 0)
        part["cmf_turn_negative"] = (part["cmf20"] < 0) & (part["cmf20"].shift(1) >= 0)

        part["above_ma20"] = part["price_above_ma20"]
        part["above_ma60"] = part["price_above_ma60"]
        part["above_ma120"] = close >= part["ma120"]
        part["overextended_from_ma20"] = part["distance_ma20_pct"] > 8
        part["overextended_from_ma60"] = part["distance_ma60_pct"] > 15
        part["long_upper_shadow_flag"] = upper_shadow_ratio(part) >= 0.4
        part["long_lower_shadow_flag"] = lower_shadow_ratio(part) >= 0.4
        part["gap_up_flag"] = part["open"] > close.shift(1) * 1.01
        part["gap_down_flag"] = part["open"] < close.shift(1) * 0.99
        part["break_ma20_flag"] = (close < part["ma20"]) & (close.shift(1) >= part["ma20"].shift(1))
        part["break_ma60_flag"] = (close < part["ma60"]) & (close.shift(1) >= part["ma60"].shift(1))
        part["new_20d_high_flag"] = part["donchian_breakout_20d"]
        part["new_60d_high_flag"] = part["donchian_breakout_60d"]

        part = add_adx(part)
        part["long_lower_shadow"] = part["long_lower_shadow_flag"]
        frames.append(part)

    result = pd.concat(frames, ignore_index=True, sort=False)
    return result.sort_values(["index_id", "trade_date"]).reset_index(drop=True), sorted(set(notes))


def consecutive_flag_count(flag: pd.Series) -> pd.Series:
    counts: list[int] = []
    current = 0
    for value in flag.fillna(False).astype(bool):
        current = current + 1 if value else 0
        counts.append(current)
    return pd.Series(counts, index=flag.index)


def upper_shadow_ratio(df: pd.DataFrame) -> pd.Series:
    rng = (df["high"] - df["low"]).replace(0, math.nan)
    body_top = df[["open", "close"]].max(axis=1)
    return (df["high"] - body_top) / rng


def lower_shadow_ratio(df: pd.DataFrame) -> pd.Series:
    rng = (df["high"] - df["low"]).replace(0, math.nan)
    body_bottom = df[["open", "close"]].min(axis=1)
    return (body_bottom - df["low"]) / rng


def build_market_breadth_history() -> pd.DataFrame:
    rows: list[pd.DataFrame] = []
    for path in STOCK_PRICE_HISTORY_DIR.glob("*.csv"):
        df = read_csv(path, dtype=str)
        if df.empty or "date" not in df.columns or "close" not in df.columns:
            continue
        keep = df.copy()
        keep["date"] = keep["date"].map(normalize_date)
        keep = keep[keep["date"] != ""].copy()
        if keep.empty:
            continue
        for col in ["close", "ma20", "ma60", "ma120", "volume", "return_1d", "return_20d", "high_20", "high_60", "high_120", "low_20", "low_60"]:
            keep[col] = pd.to_numeric(keep[col], errors="coerce") if col in keep.columns else math.nan
        keep["stock_id"] = path.stem
        rows.append(
            keep[
                [
                    "date",
                    "stock_id",
                    "close",
                    "ma20",
                    "ma60",
                    "ma120",
                    "volume",
                    "return_1d",
                    "return_20d",
                    "high_20",
                    "high_60",
                    "high_120",
                    "low_20",
                    "low_60",
                ]
            ]
        )
    if not rows:
        return pd.DataFrame()

    panel = pd.concat(rows, ignore_index=True, sort=False)
    panel["advancing"] = panel["return_1d"] > 0
    panel["declining"] = panel["return_1d"] < 0
    panel["above_ma20"] = panel["close"] >= panel["ma20"]
    panel["above_ma60"] = panel["close"] >= panel["ma60"]
    panel["above_ma120"] = panel["close"] >= panel["ma120"]
    panel["above_ma240"] = False
    panel["new_20d_high"] = panel["close"] >= panel["high_20"]
    panel["new_60d_high"] = panel["close"] >= panel["high_60"]
    panel["new_120d_high"] = panel["close"] >= panel["high_120"]
    panel["new_20d_low"] = panel["close"] <= panel["low_20"]
    panel["new_60d_low"] = panel["close"] <= panel["low_60"]
    panel["new_120d_low"] = False
    panel["limit_up"] = panel["return_1d"] >= 9.5
    panel["limit_down"] = panel["return_1d"] <= -9.5
    panel["strong_stock"] = panel["return_20d"] >= 10
    panel["weak_stock"] = panel["return_20d"] <= -10

    grouped = panel.groupby("date")
    out = pd.DataFrame(
        {
            "date": grouped.size().index,
            "total_stocks": grouped.size().values,
            "advancing_stocks": grouped["advancing"].sum().values,
            "declining_stocks": grouped["declining"].sum().values,
            "advance_volume": grouped.apply(lambda g: g.loc[g["advancing"], "volume"].sum()).values,
            "decline_volume": grouped.apply(lambda g: g.loc[g["declining"], "volume"].sum()).values,
            "new_20d_high_count": grouped["new_20d_high"].sum().values,
            "new_60d_high_count": grouped["new_60d_high"].sum().values,
            "new_120d_high_count": grouped["new_120d_high"].sum().values,
            "new_20d_low_count": grouped["new_20d_low"].sum().values,
            "new_60d_low_count": grouped["new_60d_low"].sum().values,
            "new_120d_low_count": grouped["new_120d_low"].sum().values,
            "stocks_above_ma20_count": grouped["above_ma20"].sum().values,
            "stocks_above_ma60_count": grouped["above_ma60"].sum().values,
            "stocks_above_ma120_count": grouped["above_ma120"].sum().values,
            "stocks_above_ma240_count": grouped["above_ma240"].sum().values,
            "limit_up_count": grouped["limit_up"].sum().values,
            "limit_down_count": grouped["limit_down"].sum().values,
            "strong_stock_count": grouped["strong_stock"].sum().values,
            "weak_stock_count": grouped["weak_stock"].sum().values,
        }
    )
    out["advance_decline_ratio"] = out["advancing_stocks"] / out["declining_stocks"].replace(0, math.nan)
    out["advance_decline_volume_ratio"] = out["advance_volume"] / out["decline_volume"].replace(0, math.nan)
    out["new_high_new_low_ratio"] = out["new_20d_high_count"] / out["new_20d_low_count"].replace(0, math.nan)
    for window in [20, 60, 120, 240]:
        out[f"pct_stocks_above_ma{window}"] = out[f"stocks_above_ma{window}_count"] / out["total_stocks"].replace(0, math.nan) * 100
    out["strong_stock_ratio"] = out["strong_stock_count"] / out["total_stocks"].replace(0, math.nan) * 100
    out["weak_stock_ratio"] = out["weak_stock_count"] / out["total_stocks"].replace(0, math.nan) * 100

    signal_log = read_csv(DAILY_SIGNAL_LOG, dtype=str)
    if not signal_log.empty and "signal_date" in signal_log.columns:
        signal_log["signal_date"] = signal_log["signal_date"].map(normalize_date)
        candidate_counts = signal_log.groupby("signal_date").agg(
            candidate_count=("stock_id", "nunique"),
            strict_breakout_count=("category", lambda s: (s.astype(str) == "breakout").sum()),
            range_rebound_count=("category", lambda s: (s.astype(str) == "range_rebound").sum()),
            revenue_low_response_count=("category", lambda s: (s.astype(str) == "revenue_breakout_low_response").sum()),
            pattern_watch_count=("category", lambda s: (s.astype(str) == "pattern").sum()),
        ).reset_index().rename(columns={"signal_date": "date"})
        out = out.merge(candidate_counts, on="date", how="left")
    for col in ["candidate_count", "strict_breakout_count", "range_rebound_count", "revenue_low_response_count", "pattern_watch_count"]:
        if col not in out.columns:
            out[col] = 0
        out[col] = out[col].fillna(0)

    out["strong_sector_count"] = math.nan
    out["weak_sector_count"] = math.nan
    out["electronics_relative_strength"] = math.nan
    out["finance_relative_strength"] = math.nan
    out["non_fin_electronics_relative_strength"] = math.nan
    out["twse_vs_tpex_relative_strength"] = math.nan
    out["large_cap_vs_small_cap_relative_strength"] = math.nan
    out = out.sort_values("date").reset_index(drop=True)
    out["breadth_expansion"] = out["pct_stocks_above_ma20"] > out["pct_stocks_above_ma20"].shift(5)
    out["breadth_deterioration"] = out["pct_stocks_above_ma20"] < out["pct_stocks_above_ma20"].shift(5)
    out["narrow_leadership"] = (out["new_20d_high_count"] > out["new_20d_high_count"].rolling(20, min_periods=1).median()) & (out["pct_stocks_above_ma20"] < out["pct_stocks_above_ma20"].shift(5))
    out["broad_participation"] = (out["pct_stocks_above_ma20"] >= 60) & (out["advance_decline_ratio"] > 1)
    return out


def merge_breadth(feature: pd.DataFrame, breadth: pd.DataFrame) -> pd.DataFrame:
    if breadth.empty:
        for col in [
            "advancing_stocks",
            "declining_stocks",
            "advance_decline_ratio",
            "advance_volume",
            "decline_volume",
            "advance_decline_volume_ratio",
            "new_20d_high_count",
            "new_60d_high_count",
            "new_120d_high_count",
            "new_20d_low_count",
            "new_60d_low_count",
            "new_120d_low_count",
            "new_high_new_low_ratio",
            "pct_stocks_above_ma20",
            "pct_stocks_above_ma60",
            "pct_stocks_above_ma120",
            "pct_stocks_above_ma240",
            "strong_stock_ratio",
            "weak_stock_ratio",
            "limit_up_count",
            "limit_down_count",
            "strong_sector_count",
            "weak_sector_count",
            "candidate_count",
            "strict_breakout_count",
            "range_rebound_count",
            "revenue_low_response_count",
            "pattern_watch_count",
        ]:
            feature[col] = math.nan
        return feature

    merged = feature.merge(breadth.rename(columns={"date": "trade_date"}), on="trade_date", how="left")
    merged = merged.sort_values(["index_id", "trade_date"]).reset_index(drop=True)
    merged["index_up_breadth_down"] = (merged.groupby("index_id")["close"].pct_change() > 0) & (merged["advance_decline_ratio"] < 1)
    merged["market_new_high_breadth_divergence"] = merged["new_60d_high_flag"] & (merged["pct_stocks_above_ma20"] < merged["pct_stocks_above_ma20"].shift(5))
    merged["index_new_high_but_ma20_breadth_down"] = merged["new_60d_high_flag"] & (merged["pct_stocks_above_ma20"] < merged["pct_stocks_above_ma20"].shift(5))
    return merged


def add_regime_and_risk(feature: pd.DataFrame) -> pd.DataFrame:
    frames: list[pd.DataFrame] = []
    for _, part in feature.sort_values(["index_id", "trade_date"]).groupby("index_id", sort=False):
        part = part.copy()
        part["return_5d"] = part["close"].pct_change(5) * 100
        part["return_10d"] = part["close"].pct_change(10) * 100
        part["return_20d"] = part["close"].pct_change(20) * 100
        part["return_60d"] = part["close"].pct_change(60) * 100
        part["market_regime"] = part.apply(classify_market_regime, axis=1)
        part["risk_level"] = part.apply(row_risk_level, axis=1)
        frames.append(part)
    return pd.concat(frames, ignore_index=True, sort=False)


def row_risk_level(row: pd.Series) -> str:
    if bool(row.get("price_below_ma60")) and to_number(row.get("return_20d")) < 0:
        return "high_risk"
    risk_points = 0
    if bool(row.get("overextended_from_ma20")):
        risk_points += 1
    if bool(row.get("rsi14_overbought_70")):
        risk_points += 1
    if bool(row.get("kd_overbought")):
        risk_points += 1
    if bool(row.get("index_new_high_but_ma20_breadth_down")):
        risk_points += 2
    if bool(row.get("high_volume_long_black")):
        risk_points += 2
    if risk_points >= 4:
        return "high_risk"
    if risk_points >= 2:
        return "elevated_risk"
    if risk_points <= 0 and bool(row.get("price_above_ma20")):
        return "low_risk"
    return "normal_risk"


def add_market_context_events(feature: pd.DataFrame) -> pd.DataFrame:
    indicators = read_csv(FUTURES_OPTIONS_CSV, dtype=str)
    if indicators.empty:
        feature["put_call_ratio_extreme_high"] = False
        feature["foreign_tx_extreme_short"] = False
        feature["vix_spike"] = False
        return feature
    indicators = indicators.copy()
    indicators["date"] = indicators["date"].map(normalize_date)
    for col in ["put_call_oi_ratio_pct", "foreign_tx_futures_net_oi", "taiwan_vix"]:
        indicators[col] = pd.to_numeric(indicators[col], errors="coerce") if col in indicators.columns else math.nan
    cols = [c for c in ["date", "put_call_oi_ratio_pct", "foreign_tx_futures_net_oi", "taiwan_vix"] if c in indicators.columns]
    context = indicators[cols].drop_duplicates("date", keep="last")
    feature = feature.merge(context.rename(columns={"date": "trade_date"}), on="trade_date", how="left")
    feature["put_call_ratio_extreme_high"] = feature["put_call_oi_ratio_pct"] >= 160
    feature["foreign_tx_extreme_short"] = feature["foreign_tx_futures_net_oi"] <= -40000
    feature["vix_spike"] = feature["taiwan_vix"] >= 35
    return feature


def event_conditions(row: pd.Series) -> list[tuple[str, str, Any]]:
    events: list[tuple[str, str, Any]] = []
    mapping = [
        ("reclaim_ma20_after_breakdown", "trend_ma", row.get("price_above_ma20") and row.get("_prev_price_below_ma20")),
        ("ma20_slope_up_price_above_ma20_ma60", "trend_ma", to_number(row.get("ma20_slope_5d")) > 0 and row.get("price_above_ma20") and row.get("price_above_ma60")),
        ("golden_cross_ma20_ma60", "trend_ma", row.get("golden_cross_ma20_ma60")),
        ("macd_hist_turn_positive", "momentum", row.get("macd_hist_turn_positive")),
        ("macd_dif_low_cross_signal", "momentum", row.get("macd_dif_low_cross_signal")),
        ("kd_low_golden_cross", "kd_stochastic", row.get("kd_low_golden_cross")),
        ("kd_high_death_cross", "kd_stochastic", row.get("kd_high_death_cross")),
        ("rsi14_overbought_70", "momentum", row.get("rsi14_overbought_70")),
        ("rsi14_oversold_30", "momentum", row.get("rsi14_oversold_30")),
        ("bollinger_squeeze_breakout_with_volume", "volatility_channel", row.get("bollinger_squeeze_breakout_with_volume")),
        ("bb_upper_breakout_long_upper_shadow", "volatility_channel", row.get("bollinger_upper_breakout_long_upper_shadow")),
        ("adx_trend_plus_di_dominant", "trend_ma", row.get("adx_trend_plus_di_dominant")),
        ("high_volume_long_black_break_ma20_ema23", "volume_flow", row.get("high_volume_long_black") and row.get("price_below_ma20") and row.get("price_below_ema23")),
        ("index_new_high_but_ma20_breadth_down", "market_breadth", row.get("index_new_high_but_ma20_breadth_down")),
        ("high_put_call_ratio_index_holds_ma20", "futures_options", row.get("put_call_ratio_extreme_high") and row.get("price_above_ma20")),
        ("foreign_tx_extreme_short_technical_weak", "futures_options", row.get("foreign_tx_extreme_short") and row.get("price_below_ma20")),
    ]
    for name, group, flag in mapping:
        try:
            active = bool(flag)
        except Exception:
            active = False
        if active:
            events.append((name, group, True))

    composite = composite_signal_for_row(row)
    if composite:
        events.append((composite, "composite_signal", True))
    return events


def composite_signal_for_row(row: pd.Series) -> str:
    close = to_number(row.get("close"))
    ma20 = to_number(row.get("ma20"))
    near_ma20 = not math.isnan(close) and not math.isnan(ma20) and abs(close / ma20 - 1) * 100 <= 2.5
    if row.get("price_above_ma20") and to_number(row.get("ma20_slope_5d")) > 0 and to_number(row.get("macd_hist")) > 0 and row.get("kd_value_rising_3d") and to_number(row.get("volume_ratio_20d")) >= 1:
        return "composite_bull_confirmation"
    if to_number(row.get("distance_ma20_pct")) > 8 and row.get("rsi14_overbought_70") and row.get("kd_overbought") and row.get("close_above_bb_upper") and to_number(row.get("volume_ratio_20d")) > 1.5:
        return "composite_overheat_risk"
    if near_ma20 and row.get("rsi14_rebound_from_oversold") and row.get("kd_low_golden_cross") and row.get("long_lower_shadow") and row.get("volume_contraction"):
        return "composite_pullback_bottoming"
    if row.get("price_below_ma20") and to_number(row.get("ma20_slope_5d")) < 0 and row.get("macd_hist_turn_negative") and row.get("kd_bear_cross") and row.get("high_volume_down_day"):
        return "composite_weakening_risk"
    if row.get("vix_spike") and row.get("put_call_ratio_extreme_high") and row.get("rsi14_oversold_30") and row.get("close_reenter_from_lower") and row.get("long_lower_shadow"):
        return "composite_panic_rebound"
    if row.get("donchian_breakout_20d") and to_number(row.get("distance_ma20_pct")) > 6 and to_number(row.get("rsi14")) > 65 and to_number(row.get("volume_ratio_20d")) > 1.8:
        return "composite_breakout_chasing_risk"
    return ""


def build_event_log(feature: pd.DataFrame) -> pd.DataFrame:
    events: list[dict[str, Any]] = []
    for _, part in feature.sort_values(["index_id", "trade_date"]).groupby("index_id", sort=False):
        part = part.copy().reset_index(drop=True)
        part["_prev_price_below_ma20"] = part["price_below_ma20"].shift(1).fillna(False)
        for idx, row in part.iterrows():
            for event_name, event_group, event_value in event_conditions(row):
                event = {
                    "event_date": row.get("trade_date"),
                    "index_id": row.get("index_id"),
                    "index_name": row.get("index_name"),
                    "event_name": event_name,
                    "event_group": event_group,
                    "event_value": event_value,
                    "close_on_event": row.get("close"),
                    "market_regime": row.get("market_regime"),
                    "risk_level": row.get("risk_level"),
                }
                event.update(forward_metrics(part, idx))
                events.append(event)
    if not events:
        return pd.DataFrame()
    return pd.DataFrame(events).sort_values(["event_date", "index_id", "event_name"]).reset_index(drop=True)


def forward_metrics(part: pd.DataFrame, idx: int) -> dict[str, Any]:
    base = to_number(part.loc[idx, "close"])
    out: dict[str, Any] = {}
    for horizon in HORIZONS:
        mature = idx + horizon < len(part) and not math.isnan(base) and base != 0
        out[f"mature_d{horizon}"] = bool(mature)
        for prefix in ["future_ret", "future_max_ret", "future_min_ret", "mfe", "mae", "max_drawdown"]:
            out[f"{prefix}_d{horizon}"] = math.nan
        out[f"time_to_peak_d{horizon}"] = math.nan
        out[f"time_to_trough_d{horizon}"] = math.nan
        if not mature:
            continue
        window = part.iloc[idx + 1 : idx + horizon + 1].copy()
        close_h = to_number(part.loc[idx + horizon, "close"])
        high_col = "high" if "high" in window.columns else "close"
        low_col = "low" if "low" in window.columns else "close"
        max_high = pd.to_numeric(window[high_col], errors="coerce").max()
        min_low = pd.to_numeric(window[low_col], errors="coerce").min()
        out[f"future_ret_d{horizon}"] = pct(close_h, base)
        out[f"future_max_ret_d{horizon}"] = pct(max_high, base)
        out[f"future_min_ret_d{horizon}"] = pct(min_low, base)
        out[f"mfe_d{horizon}"] = out[f"future_max_ret_d{horizon}"]
        out[f"mae_d{horizon}"] = out[f"future_min_ret_d{horizon}"]
        out[f"max_drawdown_d{horizon}"] = min(out[f"future_min_ret_d{horizon}"], 0)
        if not window.empty:
            out[f"time_to_peak_d{horizon}"] = int(pd.to_numeric(window[high_col], errors="coerce").reset_index(drop=True).idxmax() + 1)
            out[f"time_to_trough_d{horizon}"] = int(pd.to_numeric(window[low_col], errors="coerce").reset_index(drop=True).idxmin() + 1)
    return out


def summarize_events(events: pd.DataFrame) -> pd.DataFrame:
    if events.empty:
        return pd.DataFrame()
    rows: list[dict[str, Any]] = []
    group_cols = ["event_name", "index_id"]
    for (event_name, index_id), group in events.groupby(group_cols, dropna=False):
        row: dict[str, Any] = {
            "event_name": event_name,
            "index_id": index_id,
            "index_name": safe_str(group["index_name"].iloc[0]) if "index_name" in group.columns else "",
            "event_group": safe_str(group["event_group"].iloc[0]),
            "sample_count": len(group),
        }
        statuses: list[str] = []
        best_horizon = ""
        best_value = -10**9
        worst_horizon = ""
        worst_value = 10**9
        for horizon in HORIZONS:
            mature = group[group[f"mature_d{horizon}"].astype(bool)]
            row[f"mature_d{horizon}_count"] = len(mature)
            if mature.empty:
                for prefix in ["avg_ret", "median_ret", "win_rate", "relative_win_rate", "avg_mfe", "avg_mae", "avg_max_drawdown", "avg_time_to_peak", "avg_time_to_trough", "baseline_ret", "lift_vs_baseline"]:
                    row[f"{prefix}_d{horizon}"] = math.nan
                statuses.append(f"D+{horizon}:pending_only")
                continue
            ret = pd.to_numeric(mature[f"future_ret_d{horizon}"], errors="coerce")
            mfe = pd.to_numeric(mature[f"mfe_d{horizon}"], errors="coerce")
            mae = pd.to_numeric(mature[f"mae_d{horizon}"], errors="coerce")
            draw = pd.to_numeric(mature[f"max_drawdown_d{horizon}"], errors="coerce")
            row[f"avg_ret_d{horizon}"] = ret.mean()
            row[f"median_ret_d{horizon}"] = ret.median()
            row[f"win_rate_d{horizon}"] = (ret > 0).mean() * 100
            baseline_source = events[events["index_id"] == index_id] if "index_id" in events.columns else events
            baseline = event_baseline_return(baseline_source, horizon)
            row[f"baseline_ret_d{horizon}"] = baseline
            row[f"lift_vs_baseline_d{horizon}"] = ret.mean() - baseline if not math.isnan(baseline) else math.nan
            row[f"relative_win_rate_d{horizon}"] = (ret > baseline).mean() * 100 if not math.isnan(baseline) else math.nan
            row[f"avg_mfe_d{horizon}"] = mfe.mean()
            row[f"avg_mae_d{horizon}"] = mae.mean()
            row[f"avg_max_drawdown_d{horizon}"] = draw.mean()
            row[f"avg_time_to_peak_d{horizon}"] = pd.to_numeric(mature[f"time_to_peak_d{horizon}"], errors="coerce").mean()
            row[f"avg_time_to_trough_d{horizon}"] = pd.to_numeric(mature[f"time_to_trough_d{horizon}"], errors="coerce").mean()
            threshold = 20 if horizon in [40, 60] else 30
            statuses.append(f"D+{horizon}:{'ok' if len(mature) >= threshold else 'insufficient_sample'}")
            if ret.mean() > best_value:
                best_value = float(ret.mean())
                best_horizon = f"D+{horizon}"
            if ret.mean() < worst_value:
                worst_value = float(ret.mean())
                worst_horizon = f"D+{horizon}"
        row["best_horizon"] = best_horizon
        row["worst_horizon"] = worst_horizon
        row["sample_status"] = ";".join(statuses)
        rows.append(row)
    return pd.DataFrame(rows).sort_values(["event_group", "event_name", "index_id"]).reset_index(drop=True)


def event_baseline_return(events: pd.DataFrame, horizon: int) -> float:
    col = f"future_ret_d{horizon}"
    mature_col = f"mature_d{horizon}"
    if col not in events.columns:
        return math.nan
    mature = events[events[mature_col].astype(bool)]
    if mature.empty:
        return math.nan
    return pd.to_numeric(mature[col], errors="coerce").mean()


def summarize_by_regime(events: pd.DataFrame) -> pd.DataFrame:
    if events.empty:
        return pd.DataFrame()
    rows: list[dict[str, Any]] = []
    for (event_name, index_id, regime), group in events.groupby(["event_name", "index_id", "market_regime"], dropna=False):
        row = {"event_name": event_name, "index_id": index_id, "market_regime": regime, "sample_count": len(group)}
        for horizon in HORIZONS:
            mature = group[group[f"mature_d{horizon}"].astype(bool)]
            ret = pd.to_numeric(mature[f"future_ret_d{horizon}"], errors="coerce") if not mature.empty else pd.Series(dtype=float)
            row[f"mature_d{horizon}_count"] = len(mature)
            row[f"avg_ret_d{horizon}"] = ret.mean() if not ret.empty else math.nan
            row[f"win_rate_d{horizon}"] = (ret > 0).mean() * 100 if not ret.empty else math.nan
        row["sample_status"] = "ok" if row.get("mature_d10_count", 0) >= 30 else ("pending_only" if row.get("mature_d10_count", 0) == 0 else "insufficient_sample")
        rows.append(row)
    return pd.DataFrame(rows).sort_values(["event_name", "index_id", "market_regime"]).reset_index(drop=True)


def summarize_composites(events: pd.DataFrame) -> pd.DataFrame:
    if events.empty:
        return pd.DataFrame()
    composites = events[events["event_group"] == "composite_signal"].copy()
    if composites.empty:
        return pd.DataFrame()
    return summarize_events(composites)


def current_state_summary(feature: pd.DataFrame) -> pd.DataFrame:
    if feature.empty:
        return pd.DataFrame()
    latest = feature.sort_values(["index_id", "trade_date"]).groupby("index_id", as_index=False).tail(1).copy()
    rows = []
    for _, row in latest.iterrows():
        trend = "多頭" if row.get("price_above_ma20") and row.get("price_above_ma60") else ("轉弱" if row.get("price_below_ma20") else "盤整")
        momentum = "增強" if to_number(row.get("macd_hist_change_3d")) > 0 and row.get("kd_value_rising_3d") else ("鈍化" if row.get("rsi14_overbought_70") else "中性")
        volatility = "壓縮" if row.get("bollinger_squeeze") else ("放大" if row.get("bollinger_expansion") else "正常")
        volume_flow = "健康" if row.get("volume_price_bullish") else ("出貨疑慮" if row.get("volume_price_bearish") else "中性")
        breadth = "擴散" if row.get("breadth_expansion") else ("惡化" if row.get("breadth_deterioration") else "中性")
        rows.append(
            {
                "index_id": row.get("index_id"),
                "trade_date": row.get("trade_date"),
                "close": row.get("close"),
                "ret_5d": row.get("return_5d"),
                "ret_20d": row.get("return_20d"),
                "market_regime": row.get("market_regime"),
                "risk_level": row.get("risk_level"),
                "trend_summary": trend,
                "momentum_summary": momentum,
                "kd_summary": "低檔轉強" if row.get("kd_low_golden_cross") else ("高檔轉弱" if row.get("kd_high_death_cross") else "中性"),
                "volatility_summary": volatility,
                "volume_flow_summary": volume_flow,
                "breadth_summary": breadth,
                "futures_options_summary": "期權資料已整合" if "put_call_oi_ratio_pct" in row.index else "期權資料不足",
            }
        )
    return pd.DataFrame(rows)


def write_backtest_md(summary: pd.DataFrame, path: Path, title: str, intro: list[str]) -> None:
    lines = [f"# {title}", "", *intro, ""]
    if summary.empty:
        lines.append("目前沒有可用回測資料。")
    else:
        cols = [
            "event_name",
            "index_id",
            "event_group",
            "sample_count",
            "mature_d5_count",
            "avg_ret_d5",
            "win_rate_d5",
            "avg_mfe_d5",
            "avg_mae_d5",
            "mature_d10_count",
            "avg_ret_d10",
            "win_rate_d10",
            "mature_d20_count",
            "avg_ret_d20",
            "win_rate_d20",
            "best_horizon",
            "sample_status",
        ]
        lines.append(markdown_table(format_for_md(summary), cols, limit=80))
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def format_for_md(df: pd.DataFrame) -> pd.DataFrame:
    out = df.copy()
    for col in out.columns:
        if any(token in col for token in ["avg_", "median_", "win_rate", "lift_", "ret_", "mfe", "mae", "drawdown", "time_to"]):
            out[col] = pd.to_numeric(out[col], errors="coerce").map(lambda x: "" if pd.isna(x) else f"{x:.2f}")
    return out


def write_regime_md(summary: pd.DataFrame) -> None:
    lines = [
        "# Market Timing Regime Effectiveness",
        "",
        "- 所有統計只使用 mature_dN=True 的事件樣本。",
        "- 同一技術訊號需分 market_regime 解讀，避免把多頭有效訊號誤套到修正盤。",
        "",
    ]
    if summary.empty:
        lines.append("目前沒有可用 regime 分層資料。")
    else:
        cols = ["event_name", "index_id", "market_regime", "sample_count", "mature_d5_count", "avg_ret_d5", "win_rate_d5", "mature_d10_count", "avg_ret_d10", "win_rate_d10", "sample_status"]
        lines.append(markdown_table(format_for_md(summary), cols, limit=100))
    REGIME_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")


def write_packet(feature: pd.DataFrame, events: pd.DataFrame, backtest: pd.DataFrame, composite: pd.DataFrame, regime: pd.DataFrame, data_notes: list[str]) -> None:
    current = current_state_summary(feature)
    latest_events = events.sort_values("event_date").tail(80) if not events.empty else pd.DataFrame()
    recent_cutoff = ""
    if not latest_events.empty:
        recent_dates = sorted(latest_events["event_date"].dropna().unique())
        if recent_dates:
            recent_cutoff = recent_dates[-5] if len(recent_dates) >= 5 else recent_dates[0]
            latest_events = latest_events[latest_events["event_date"] >= recent_cutoff]

    mature_counts = {}
    for horizon in HORIZONS:
        mature_counts[f"mature_d{horizon}_count"] = int(events[f"mature_d{horizon}"].astype(bool).sum()) if not events.empty and f"mature_d{horizon}" in events.columns else 0

    lines = [
        "# MARKET TIMING CHATGPT PACKET",
        "",
        "## Metadata",
        f"- generated_at: {now_text()}",
        f"- main_price_date: {feature['trade_date'].max() if not feature.empty else ''}",
        f"- index_list: {', '.join(sorted(feature['index_id'].dropna().unique())) if not feature.empty else ''}",
        f"- data_range: {feature['trade_date'].min() if not feature.empty else ''} ~ {feature['trade_date'].max() if not feature.empty else ''}",
        f"- source_files: data/market_index_history.csv, {BREADTH_HISTORY.as_posix()}, {EVENT_LOG.as_posix()}",
        "- tuning_status: not_ready",
        "",
        "## Current Market Technical State",
        markdown_table(format_for_md(current), ["index_id", "trade_date", "close", "ret_5d", "ret_20d", "market_regime", "risk_level", "trend_summary", "momentum_summary", "kd_summary", "volatility_summary", "volume_flow_summary", "breadth_summary", "futures_options_summary"], limit=10),
        "",
        "## Six-Layer Technical Summary",
    ]

    for layer, desc in [
        ("趨勢 / 均線", "MA/EMA、均線距離、斜率、交叉與排列。"),
        ("動能指標", "MACD、RSI、ROC、Williams、CCI。"),
        ("KD / 隨機指標", "KD 低檔轉強、高檔轉弱、超買超賣與鈍化。"),
        ("波動 / 通道", "Bollinger、ATR、Keltner、Donchian。"),
        ("價量 / 資金", "量比、OBV、MFI、A/D、CMF。"),
        ("市場廣度 / 內部結構", "上漲下跌家數、站上均線比例、創高創低與候選數。"),
    ]:
        lines.extend([f"### {layer}", f"- current_state: {desc}", "- backtest_status: 使用下方 Event Backtest Summary，樣本不足時不得作定論。", ""])

    lines.extend(
        [
            "## Active Technical Events",
            markdown_table(latest_events, ["event_date", "index_id", "event_name", "event_group", "close_on_event", "market_regime", "risk_level"], limit=60),
            "",
            "## Event Backtest Summary",
            markdown_table(format_for_md(backtest), ["event_name", "index_id", "sample_count", "mature_d5_count", "avg_ret_d5", "win_rate_d5", "mature_d10_count", "avg_ret_d10", "win_rate_d10", "mature_d20_count", "avg_ret_d20", "win_rate_d20", "best_horizon", "sample_status"], limit=50),
            "",
            "## Composite Signal Backtest Summary",
            markdown_table(format_for_md(composite), ["event_name", "index_id", "sample_count", "mature_d5_count", "avg_ret_d5", "win_rate_d5", "mature_d10_count", "avg_ret_d10", "win_rate_d10", "best_horizon", "sample_status"], limit=30),
            "",
            "## Regime Sensitivity",
            markdown_table(format_for_md(regime), ["event_name", "index_id", "market_regime", "sample_count", "mature_d5_count", "avg_ret_d5", "win_rate_d5", "mature_d10_count", "avg_ret_d10", "sample_status"], limit=60),
            "",
            "## Time Effect Summary",
            "- D+1 / D+3: 適合檢查短線轉折、假突破、KD 高低檔交叉。",
            "- D+5 / D+10: 適合檢查 MACD 翻正、站回 MA20、期權極端後回歸。",
            "- D+20 / D+40 / D+60: 適合檢查均線黃金交叉與中期趨勢事件。",
            "- 樣本不足時只能標示待回測假設，目前只作為觀察，不作為模型加權依據。",
            "",
            "## Data Quality Notes",
            f"- missing_fields: {', '.join(sorted(set(data_notes))) if data_notes else 'none'}",
            f"- pending_events: {sum(1 for _, row in events.iterrows() if not bool(row.get('mature_d20'))) if not events.empty else 0}",
            f"- benchmark_available: TWSE/TPEX index history available={not feature.empty}",
            f"- regime_available: {'market_regime' in feature.columns if not feature.empty else False}",
            f"- breadth_available: {BREADTH_HISTORY.exists()}",
            f"- mature_counts: {mature_counts}",
            "",
            "## Model Tuning Recommendation",
            "- tuning_status = not_ready",
            "- allowed_changes = reporting_only",
            "- forbidden_changes = core_weight_change",
            "- reason = market timing event samples still need mature D+10 / D+20 accumulation before formal weighting.",
            "",
        ]
    )
    PACKET_MD.write_text("\n".join(lines), encoding="utf-8")


def main() -> int:
    MARKET_TIMING_DIR.mkdir(parents=True, exist_ok=True)
    feature, notes = normalize_index_history()
    if feature.empty:
        write_csv(pd.DataFrame(), FEATURE_PANEL)
        write_csv(pd.DataFrame(), EVENT_LOG)
        PACKET_MD.write_text("# MARKET TIMING CHATGPT PACKET\n\nmarket_index_history_missing\n", encoding="utf-8")
        return 0

    breadth = build_market_breadth_history()
    write_csv(breadth, BREADTH_HISTORY)
    feature = merge_breadth(feature, breadth)
    feature = add_regime_and_risk(feature)
    feature = add_market_context_events(feature)
    write_csv(feature, FEATURE_PANEL)

    events = build_event_log(feature)
    write_csv(events, EVENT_LOG)

    backtest = summarize_events(events)
    regime = summarize_by_regime(events)
    composite = summarize_composites(events)
    write_csv(backtest, BACKTEST_CSV)
    write_csv(regime, REGIME_CSV)
    write_csv(composite, COMPOSITE_CSV)

    write_backtest_md(
        backtest,
        BACKTEST_MD,
        "Market Timing Technical Event Backtest",
        [
            "- This report tracks market technical events with D+1/D+3/D+5/D+10/D+20/D+40/D+60 outcomes.",
            "- Features use only information available on event_date. Future data is used only for performance labels.",
            "- pending is not success or failure; sample_status must be checked before drawing conclusions.",
        ],
    )
    write_backtest_md(
        composite,
        COMPOSITE_MD,
        "Market Timing Composite Signal Backtest",
        [
            "- Composite signals combine trend, momentum, volatility, volume, breadth, and derivatives context.",
            "- Current stage is reporting/backtesting only; no core model weights are changed here.",
        ],
    )
    write_regime_md(regime)
    write_packet(feature, events, backtest, composite, regime, notes)

    print(f"Saved: {FEATURE_PANEL} rows={len(feature)}")
    print(f"Saved: {BREADTH_HISTORY} rows={len(breadth)}")
    print(f"Saved: {EVENT_LOG} rows={len(events)}")
    print(f"Saved: {BACKTEST_MD}")
    print(f"Saved: {PACKET_MD}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
