from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo
from concurrent.futures import ThreadPoolExecutor
import math
import os
from typing import Any, Callable

import pandas as pd

from build_volume_breakout_watch import (
    PRICE_HISTORY_DIR,
    add_price_metrics,
    detect_volume_breakout,
    locked_limit_up_breakout_mask,
    normalize_date,
    normalize_stock_id,
    normalize_volume_ma20_lots,
    safe_bool,
    safe_float,
    safe_str,
)


ROOT = Path(".")
LATEST_DIR = ROOT / "output" / "latest"
RESEARCH_HISTORY_DIR = ROOT / "output" / "history" / "research"
MARKET_INDEX_HISTORY = ROOT / "data" / "market_index_history.csv"

REGISTRY_CSV = LATEST_DIR / "historical_pattern_operation_registry_latest.csv"
REGISTRY_MD = LATEST_DIR / "historical_pattern_operation_registry_latest.md"
DETAIL_HISTORY_CSV = RESEARCH_HISTORY_DIR / "historical_pattern_operation_events.csv"
REGISTRY_HISTORY_CSV = RESEARCH_HISTORY_DIR / "historical_pattern_operation_registry.csv"

MODEL_ID = "volume_range_breakout"
MODEL_NAME_ZH = "底部放量攻擊模型"
RAW_PREFIX = "https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main"


REGISTRY_COLUMNS = [
    "model_id",
    "model_name_zh",
    "event_filter_id",
    "event_filter_zh",
    "model_hit_status",
    "pattern_id",
    "pattern_name_zh",
    "entry_rule_zh",
    "stop_loss_rule_zh",
    "hold_rule_zh",
    "exit_rule_zh",
    "sample_size",
    "unique_stocks",
    "win_rate",
    "avg_return",
    "median_return",
    "max_drawdown",
    "avg_holding_days",
    "profit_factor",
    "in_sample_size",
    "in_sample_win_rate",
    "in_sample_avg_return",
    "out_of_sample_size",
    "out_of_sample_win_rate",
    "out_of_sample_avg_return",
    "best_for_market_regime",
    "risk_notes_zh",
    "confidence_status",
    "approved_for_daily",
    "out_of_sample_pass",
    "generated_at",
    "data_start_date",
    "data_end_date",
    "out_of_sample_start_date",
]

DETAIL_COLUMNS = [
    "model_id",
    "event_filter_id",
    "model_hit_status",
    "pattern_id",
    "event_date",
    "stock_id",
    "stock_name",
    "market",
    "market_regime",
    "entry_date",
    "entry_price",
    "exit_date",
    "exit_price",
    "exit_reason",
    "holding_days",
    "return_pct",
    "mfe_pct",
    "mae_pct",
    "out_of_sample",
    "volume_ratio",
    "signal_return_1d_pct",
    "signal_low",
    "signal_high",
    "previous_20d_high",
    "range_width_20_pct",
    "range_width_40_pct",
    "range_width_60_pct",
    "low_position_60_pct",
    "limit_up_like",
]


@dataclass(frozen=True)
class EventFilter:
    event_filter_id: str
    event_filter_zh: str
    model_hit_status: str
    predicate: Callable[[pd.Series], bool]
    risk_note_zh: str


@dataclass(frozen=True)
class PatternSpec:
    pattern_id: str
    pattern_name_zh: str
    entry_rule_zh: str
    stop_loss_rule_zh: str
    hold_rule_zh: str
    exit_rule_zh: str
    entry_kind: str
    max_holding_days: int
    stop_kind: str = "none"
    take_profit_pct: float | None = None
    trigger_window_days: int = 1


def now_text() -> str:
    return datetime.now(ZoneInfo("Asia/Taipei")).strftime("%Y-%m-%d %H:%M:%S Asia/Taipei")


def raw_url(path: Path) -> str:
    return f"{RAW_PREFIX}/{path.as_posix()}"


def write_csv(df: pd.DataFrame, path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(path, index=False, encoding="utf-8", lineterminator="\n")


def read_csv(path: Path) -> pd.DataFrame:
    if not path.exists():
        return pd.DataFrame()
    try:
        return pd.read_csv(path, dtype=str, keep_default_na=False)
    except Exception:
        return pd.DataFrame()


def pct(value: Any) -> float:
    num = safe_float(value)
    return num if not math.isnan(num) else math.nan


def pct_round(value: Any, digits: int = 4) -> float | str:
    num = safe_float(value)
    if math.isnan(num):
        return ""
    return round(num, digits)


def is_equity_stock_id(stock_id: Any) -> bool:
    text = normalize_stock_id(stock_id)
    return text.isdigit() and len(text) == 4 and not text.startswith("00")


def bool_value(value: Any) -> bool:
    if isinstance(value, bool):
        return value
    return safe_bool(value)


def classify_market_regime(row: pd.Series) -> str:
    if row.empty:
        return "unknown"
    above_ma20 = bool_value(row.get("above_ma20"))
    above_ma60 = bool_value(row.get("above_ma60"))
    ret20 = safe_float(row.get("return_20d"))
    if above_ma20 and above_ma60 and not math.isnan(ret20) and ret20 >= 3:
        return "strong_bull"
    if above_ma20 and above_ma60:
        return "mild_bull"
    if not above_ma20 and not math.isnan(ret20) and ret20 <= -3:
        return "correction"
    return "range_or_mixed"


def load_market_regime_map() -> dict[str, str]:
    df = read_csv(MARKET_INDEX_HISTORY)
    if df.empty or "date" not in df.columns:
        return {}
    if "index_code" in df.columns:
        twse = df[df["index_code"].map(safe_str).eq("TWSE")].copy()
        if not twse.empty:
            df = twse
    df["date"] = df["date"].map(normalize_date)
    df = df[df["date"] != ""].sort_values("date")
    return {safe_str(row.get("date")): classify_market_regime(row) for _, row in df.iterrows()}


def numeric_series(df: pd.DataFrame, col: str) -> pd.Series:
    if col not in df.columns:
        return pd.Series([math.nan] * len(df), index=df.index, dtype="float64")
    return pd.to_numeric(df[col], errors="coerce")


def add_research_features(df: pd.DataFrame) -> pd.DataFrame:
    out = add_price_metrics(df)
    high = numeric_series(out, "high")
    low = numeric_series(out, "low")
    close = numeric_series(out, "close")
    volume_ratio = numeric_series(out, "volume_ratio")
    prev_close = numeric_series(out, "previous_close_calc")

    out["previous_40d_high_calc"] = high.shift(1).rolling(40, min_periods=40).max()
    out["previous_40d_low_calc"] = low.shift(1).rolling(40, min_periods=40).min()
    for window in [20, 40, 60]:
        hi = numeric_series(out, f"previous_{window}d_high_calc")
        lo = numeric_series(out, f"previous_{window}d_low_calc")
        out[f"range_width_{window}_pct"] = (hi - lo) / lo.replace(0, pd.NA) * 100.0

    prev60_hi = numeric_series(out, "previous_60d_high_calc")
    prev60_lo = numeric_series(out, "previous_60d_low_calc")
    out["low_position_60_pct"] = (close - prev60_lo) / (prev60_hi - prev60_lo).replace(0, pd.NA) * 100.0
    out["signal_return_1d_pct"] = (close / prev_close - 1.0) * 100.0
    one_price_or_close_high = (high == low) | (out["close_position_in_range"] >= 0.9)
    out["limit_up_like"] = (
        (out["signal_return_1d_pct"] >= 9.0)
        & one_price_or_close_high
        & (close >= numeric_series(out, "previous_20d_high_calc") * 1.02)
    )
    out["volume_ratio_bucket"] = pd.cut(
        volume_ratio,
        bins=[-math.inf, 1.0, 1.5, 2.0, 3.0, math.inf],
        labels=["lt_1", "1_1p5", "1p5_2", "2_3", "ge_3"],
    ).astype(str)
    return out


def current_model_hit(row: pd.Series) -> bool:
    return detect_volume_breakout(row) is not None


def long_base_low_position(row: pd.Series) -> bool:
    width40 = safe_float(row.get("range_width_40_pct"))
    low_pos60 = safe_float(row.get("low_position_60_pct"))
    return (
        current_model_hit(row)
        and not math.isnan(width40)
        and not math.isnan(low_pos60)
        and width40 <= 25
        and low_pos60 <= 60
    )


def simple_or_high_position(row: pd.Series) -> bool:
    return current_model_hit(row) and not long_base_low_position(row)


def limit_up_current_hit(row: pd.Series) -> bool:
    return current_model_hit(row) and bool_value(row.get("limit_up_like"))


EVENT_FILTERS = [
    EventFilter(
        "current_model_hit_all",
        "現行放量攻擊模型全部命中",
        "current_model_hit",
        lambda row: current_model_hit(row),
        "正式模型命中樣本，可作為 operation pattern 的基準宇宙。",
    ),
    EventFilter(
        "long_base_low_position",
        "長盤整加低位階突破",
        "current_model_hit",
        long_base_low_position,
        "檢驗長盤整、60日相對低位階是否優於單純突破。",
    ),
    EventFilter(
        "simple_or_high_position_breakout",
        "非長盤整低位階的一般突破",
        "current_model_hit",
        simple_or_high_position,
        "作為長盤整低位階突破的對照組。",
    ),
    EventFilter(
        "limit_up_like_current_hit",
        "漲停或接近漲停且符合現行模型",
        "current_model_hit",
        limit_up_current_hit,
        "檢驗漲停後第1/2/3天追價與停損風險。",
    ),
]


PATTERN_SPECS = [
    PatternSpec(
        "signal_close_hold_5d",
        "當日收盤買固定5日",
        "訊號日收盤價買進。",
        "無固定停損；僅統計歷史持有表現。",
        "固定持有至 D+5 收盤。",
        "D+5 收盤出場。",
        "signal_close",
        5,
    ),
    PatternSpec(
        "next_open_hold_5d",
        "隔日開盤買固定5日",
        "訊號隔日開盤買進。",
        "無固定停損；僅統計歷史持有表現。",
        "固定持有5個交易日。",
        "第5個持有交易日收盤出場。",
        "next_open",
        5,
    ),
    PatternSpec(
        "next_open_hold_10d",
        "隔日開盤買固定10日",
        "訊號隔日開盤買進。",
        "無固定停損；僅統計歷史持有表現。",
        "固定持有10個交易日。",
        "第10個持有交易日收盤出場。",
        "next_open",
        10,
    ),
    PatternSpec(
        "next_open_hold_20d",
        "隔日開盤買固定20日",
        "訊號隔日開盤買進。",
        "無固定停損；僅統計歷史持有表現。",
        "固定持有20個交易日。",
        "第20個持有交易日收盤出場。",
        "next_open",
        20,
    ),
    PatternSpec(
        "next_day_break_signal_high_hold_10d",
        "隔日突破訊號高點買",
        "隔日盤中突破訊號K高點才買進；若隔日開盤已跳空越過高點，以開盤價估算。",
        "無固定停損；僅統計觸發後表現。",
        "觸發後固定持有10個交易日。",
        "第10個持有交易日收盤出場。",
        "next_break_signal_high",
        10,
        trigger_window_days=1,
    ),
    PatternSpec(
        "pullback_5ma_hold_10d",
        "回測5MA買固定10日",
        "訊號後5個交易日內第一次回測5MA買進。",
        "無固定停損；僅統計回測買點表現。",
        "買進後固定持有10個交易日。",
        "第10個持有交易日收盤出場。",
        "pullback_ma5",
        10,
        trigger_window_days=5,
    ),
    PatternSpec(
        "pullback_10ma_hold_10d",
        "回測10MA買固定10日",
        "訊號後7個交易日內第一次回測10MA買進。",
        "無固定停損；僅統計回測買點表現。",
        "買進後固定持有10個交易日。",
        "第10個持有交易日收盤出場。",
        "pullback_ma10",
        10,
        trigger_window_days=7,
    ),
    PatternSpec(
        "next_open_signal_low_stop_10d",
        "隔日開盤買跌破訊號K低點停損",
        "訊號隔日開盤買進。",
        "跌破訊號K低點停損；若跳空跌破，以開盤價估算。",
        "最多持有10個交易日。",
        "觸及停損或第10個持有交易日收盤出場。",
        "next_open",
        10,
        stop_kind="signal_low",
    ),
    PatternSpec(
        "next_open_5pct_stop_10d",
        "隔日開盤買固定5%停損",
        "訊號隔日開盤買進。",
        "自進場價下跌5%停損；若跳空跌破，以開盤價估算。",
        "最多持有10個交易日。",
        "觸及停損或第10個持有交易日收盤出場。",
        "next_open",
        10,
        stop_kind="fixed_5_pct",
    ),
    PatternSpec(
        "next_open_5ma_trailing_20d",
        "隔日開盤買沿5MA續抱",
        "訊號隔日開盤買進。",
        "收盤跌破5MA出場。",
        "最多持有20個交易日，未跌破則續抱至上限。",
        "跌破5MA收盤或第20個持有交易日收盤出場。",
        "next_open",
        20,
        stop_kind="ma5_close",
    ),
    PatternSpec(
        "next_open_10ma_trailing_20d",
        "隔日開盤買沿10MA續抱",
        "訊號隔日開盤買進。",
        "收盤跌破10MA出場。",
        "最多持有20個交易日，未跌破則續抱至上限。",
        "跌破10MA收盤或第20個持有交易日收盤出場。",
        "next_open",
        20,
        stop_kind="ma10_close",
    ),
    PatternSpec(
        "next_open_large_black_exit_10d",
        "隔日開盤買大量黑K出場",
        "訊號隔日開盤買進。",
        "出現大量黑K時以當日收盤出場。",
        "最多持有10個交易日。",
        "大量黑K收盤或第10個持有交易日收盤出場。",
        "next_open",
        10,
        stop_kind="large_black_candle",
    ),
    PatternSpec(
        "next_open_tp5_signal_low_stop_10d",
        "隔日開盤買5%停利訊號低點停損",
        "訊號隔日開盤買進。",
        "跌破訊號K低點停損。",
        "最多持有10個交易日。",
        "盤中觸及5%停利、觸及停損，或第10個持有交易日收盤出場。",
        "next_open",
        10,
        stop_kind="signal_low",
        take_profit_pct=5.0,
    ),
    PatternSpec(
        "next_open_tp10_signal_low_stop_20d",
        "隔日開盤買10%停利訊號低點停損",
        "訊號隔日開盤買進。",
        "跌破訊號K低點停損。",
        "最多持有20個交易日。",
        "盤中觸及10%停利、觸及停損，或第20個持有交易日收盤出場。",
        "next_open",
        20,
        stop_kind="signal_low",
        take_profit_pct=10.0,
    ),
    PatternSpec(
        "chase_day1_signal_low_stop_5d",
        "漲停後第1天追價",
        "訊號後第1個交易日開盤追價。",
        "跌破訊號K低點停損。",
        "最多持有5個交易日。",
        "觸及停損或第5個持有交易日收盤出場。",
        "chase_day1",
        5,
        stop_kind="signal_low",
    ),
    PatternSpec(
        "chase_day2_signal_low_stop_5d",
        "漲停後第2天追價",
        "訊號後第2個交易日開盤追價。",
        "跌破訊號K低點停損。",
        "最多持有5個交易日。",
        "觸及停損或第5個持有交易日收盤出場。",
        "chase_day2",
        5,
        stop_kind="signal_low",
    ),
    PatternSpec(
        "chase_day3_signal_low_stop_5d",
        "漲停後第3天追價",
        "訊號後第3個交易日開盤追價。",
        "跌破訊號K低點停損。",
        "最多持有5個交易日。",
        "觸及停損或第5個持有交易日收盤出場。",
        "chase_day3",
        5,
        stop_kind="signal_low",
    ),
]


def entry_for_pattern(df: pd.DataFrame, signal_idx: int, spec: PatternSpec) -> tuple[int, float] | None:
    signal = df.iloc[signal_idx]
    signal_high = safe_float(signal.get("high"))
    if spec.entry_kind == "signal_close":
        price = safe_float(signal.get("close"))
        if math.isnan(price) or price <= 0:
            return None
        return signal_idx, price

    if spec.entry_kind == "next_open":
        entry_idx = signal_idx + 1
        if entry_idx >= len(df):
            return None
        price = safe_float(df.iloc[entry_idx].get("open"))
        return (entry_idx, price) if not math.isnan(price) and price > 0 else None

    if spec.entry_kind.startswith("chase_day"):
        day = int(spec.entry_kind.replace("chase_day", ""))
        entry_idx = signal_idx + day
        if entry_idx >= len(df):
            return None
        price = safe_float(df.iloc[entry_idx].get("open"))
        return (entry_idx, price) if not math.isnan(price) and price > 0 else None

    if spec.entry_kind == "next_break_signal_high":
        if math.isnan(signal_high) or signal_high <= 0:
            return None
        for entry_idx in range(signal_idx + 1, min(len(df), signal_idx + 1 + spec.trigger_window_days)):
            row = df.iloc[entry_idx]
            high = safe_float(row.get("high"))
            open_ = safe_float(row.get("open"))
            if math.isnan(high) or high < signal_high:
                continue
            price = open_ if not math.isnan(open_) and open_ > signal_high else signal_high
            return entry_idx, price
        return None

    if spec.entry_kind in {"pullback_ma5", "pullback_ma10"}:
        ma_col = "ma5" if spec.entry_kind == "pullback_ma5" else "ma10"
        for entry_idx in range(signal_idx + 1, min(len(df), signal_idx + 1 + spec.trigger_window_days)):
            row = df.iloc[entry_idx]
            ma = safe_float(row.get(ma_col))
            low = safe_float(row.get("low"))
            open_ = safe_float(row.get("open"))
            if any(math.isnan(v) for v in [ma, low, open_]) or ma <= 0:
                continue
            if low <= ma:
                price = open_ if open_ <= ma else ma
                return entry_idx, price
        return None

    raise ValueError(f"unknown entry_kind: {spec.entry_kind}")


def stop_price_for_day(row: pd.Series, stop_level: float) -> float:
    open_ = safe_float(row.get("open"))
    if not math.isnan(open_) and open_ < stop_level:
        return open_
    return stop_level


def large_black_candle(row: pd.Series) -> bool:
    open_ = safe_float(row.get("open"))
    close = safe_float(row.get("close"))
    prev_close = safe_float(row.get("previous_close_calc"))
    vol_ratio = safe_float(row.get("volume_ratio"))
    if any(math.isnan(v) for v in [open_, close, prev_close, vol_ratio]) or prev_close <= 0:
        return False
    day_ret = (close / prev_close - 1.0) * 100.0
    return close < open_ and day_ret <= -3.0 and vol_ratio >= 1.5


def simulate_trade(df: pd.DataFrame, signal_idx: int, spec: PatternSpec) -> dict[str, Any] | None:
    entry = entry_for_pattern(df, signal_idx, spec)
    if entry is None:
        return None
    entry_idx, entry_price = entry
    if entry_idx >= len(df) or math.isnan(entry_price) or entry_price <= 0:
        return None

    signal_row = df.iloc[signal_idx]
    signal_low = safe_float(signal_row.get("low"))
    signal_high = safe_float(signal_row.get("high"))

    if spec.entry_kind == "signal_close":
        planned_exit_idx = signal_idx + spec.max_holding_days
        stop_start_idx = signal_idx + 1
    else:
        planned_exit_idx = entry_idx + spec.max_holding_days - 1
        stop_start_idx = entry_idx
    if planned_exit_idx >= len(df):
        return None

    exit_idx = planned_exit_idx
    exit_reason = f"fixed_{spec.max_holding_days}d_close"
    exit_price = safe_float(df.iloc[planned_exit_idx].get("close"))
    if math.isnan(exit_price) or exit_price <= 0:
        return None

    for day_idx in range(stop_start_idx, planned_exit_idx + 1):
        day = df.iloc[day_idx]
        low = safe_float(day.get("low"))
        high = safe_float(day.get("high"))
        close = safe_float(day.get("close"))

        if spec.stop_kind == "signal_low" and not math.isnan(signal_low) and not math.isnan(low) and low <= signal_low:
            exit_idx = day_idx
            exit_price = stop_price_for_day(day, signal_low)
            exit_reason = "stop_signal_low"
            break
        if spec.stop_kind == "fixed_5_pct" and not math.isnan(low) and low <= entry_price * 0.95:
            exit_idx = day_idx
            exit_price = stop_price_for_day(day, entry_price * 0.95)
            exit_reason = "stop_fixed_5pct"
            break
        if spec.stop_kind == "ma5_close":
            ma = safe_float(day.get("ma5"))
            if not math.isnan(ma) and not math.isnan(close) and close < ma:
                exit_idx = day_idx
                exit_price = close
                exit_reason = "exit_close_below_ma5"
                break
        if spec.stop_kind == "ma10_close":
            ma = safe_float(day.get("ma10"))
            if not math.isnan(ma) and not math.isnan(close) and close < ma:
                exit_idx = day_idx
                exit_price = close
                exit_reason = "exit_close_below_ma10"
                break
        if spec.stop_kind == "large_black_candle" and large_black_candle(day):
            exit_idx = day_idx
            exit_price = close
            exit_reason = "exit_large_black_candle"
            break
        if spec.take_profit_pct is not None and not math.isnan(high) and high >= entry_price * (1 + spec.take_profit_pct / 100.0):
            exit_idx = day_idx
            exit_price = entry_price * (1 + spec.take_profit_pct / 100.0)
            exit_reason = f"take_profit_{spec.take_profit_pct:g}pct"
            break

    holding_window = df.iloc[entry_idx : exit_idx + 1]
    max_high = pd.to_numeric(holding_window["high"], errors="coerce").max()
    min_low = pd.to_numeric(holding_window["low"], errors="coerce").min()
    return_pct = (exit_price / entry_price - 1.0) * 100.0
    mfe_pct = (max_high / entry_price - 1.0) * 100.0 if not math.isnan(max_high) else math.nan
    mae_pct = (min_low / entry_price - 1.0) * 100.0 if not math.isnan(min_low) else math.nan

    return {
        "entry_date": normalize_date(df.iloc[entry_idx].get("date")),
        "entry_price": round(entry_price, 4),
        "exit_date": normalize_date(df.iloc[exit_idx].get("date")),
        "exit_price": round(exit_price, 4),
        "exit_reason": exit_reason,
        "holding_days": exit_idx - entry_idx + 1 if spec.entry_kind != "signal_close" else exit_idx - signal_idx,
        "return_pct": round(return_pct, 4),
        "mfe_pct": round(mfe_pct, 4) if not math.isnan(mfe_pct) else "",
        "mae_pct": round(mae_pct, 4) if not math.isnan(mae_pct) else "",
        "signal_low": round(signal_low, 4) if not math.isnan(signal_low) else "",
        "signal_high": round(signal_high, 4) if not math.isnan(signal_high) else "",
    }


def base_event_payload(row: pd.Series, market_regimes: dict[str, str]) -> dict[str, Any]:
    event_date = normalize_date(row.get("date"))
    return {
        "model_id": MODEL_ID,
        "event_date": event_date,
        "stock_id": normalize_stock_id(row.get("stock_id")),
        "stock_name": safe_str(row.get("stock_name")),
        "market": safe_str(row.get("market")),
        "market_regime": market_regimes.get(event_date, "unknown"),
        "volume_ratio": pct_round(row.get("volume_ratio")),
        "signal_return_1d_pct": pct_round(row.get("signal_return_1d_pct")),
        "previous_20d_high": pct_round(row.get("previous_20d_high_calc")),
        "range_width_20_pct": pct_round(row.get("range_width_20_pct")),
        "range_width_40_pct": pct_round(row.get("range_width_40_pct")),
        "range_width_60_pct": pct_round(row.get("range_width_60_pct")),
        "low_position_60_pct": pct_round(row.get("low_position_60_pct")),
        "limit_up_like": bool_value(row.get("limit_up_like")),
    }


def build_detail_events() -> pd.DataFrame:
    market_regimes = load_market_regime_map()
    paths = sorted(PRICE_HISTORY_DIR.glob("*.csv"))
    workers = min(12, max(2, os.cpu_count() or 4))
    detail_rows: list[dict[str, Any]] = []
    worker_args = [(path, market_regimes) for path in paths]
    with ThreadPoolExecutor(max_workers=workers) as executor:
        for part in executor.map(lambda args: process_price_history_path(*args), worker_args):
            detail_rows.extend(part)
    detail = pd.DataFrame(detail_rows)
    if detail.empty:
        return pd.DataFrame(columns=DETAIL_COLUMNS)
    detail = detail.sort_values(["event_date", "stock_id", "event_filter_id", "pattern_id"]).reset_index(drop=True)
    split_date = out_of_sample_start_date(detail)
    detail["out_of_sample"] = detail["event_date"].map(lambda value: bool(split_date and safe_str(value) >= split_date))
    return detail[DETAIL_COLUMNS]


def formal_model_hit_mask(price: pd.DataFrame) -> pd.Series:
    close = numeric_series(price, "close")
    open_ = numeric_series(price, "open")
    prev_close = numeric_series(price, "previous_close_calc")
    prev20 = numeric_series(price, "previous_20d_high_calc")
    volume_ratio = numeric_series(price, "volume_ratio")
    volume_ma20 = numeric_series(price, "volume_ma20")
    volume_ma20_lots = volume_ma20.where(volume_ma20 < 100000, volume_ma20 / 1000.0)
    bullish = (close > open_) | ((close == open_) & (close > prev_close))
    normal_volume_attack = (
        (close >= prev20 * 1.02)
        & (volume_ratio >= 2.0)
        & (volume_ma20_lots >= 1000)
        & bullish
    ).fillna(False)
    base_mask = (normal_volume_attack | locked_limit_up_breakout_mask(price)).fillna(False)
    if not base_mask.any():
        return base_mask
    validated = pd.Series(False, index=price.index)
    for idx in base_mask[base_mask].index:
        validated.loc[idx] = detect_volume_breakout(price.loc[idx]) is not None
    return validated


def event_filter_masks(price: pd.DataFrame) -> dict[str, pd.Series]:
    model_mask = formal_model_hit_mask(price)
    width40 = numeric_series(price, "range_width_40_pct")
    low_pos60 = numeric_series(price, "low_position_60_pct")
    long_low = (model_mask & (width40 <= 25) & (low_pos60 <= 60)).fillna(False)
    return {
        "current_model_hit_all": model_mask,
        "long_base_low_position": long_low,
        "simple_or_high_position_breakout": (model_mask & ~long_low).fillna(False),
        "limit_up_like_current_hit": (model_mask & price["limit_up_like"].fillna(False)).fillna(False),
    }


def process_price_history_path(path: Path, market_regimes: dict[str, str]) -> list[dict[str, Any]]:
    detail_rows: list[dict[str, Any]] = []
    df = read_csv(path)
    if df.empty or len(df) < 90:
        return detail_rows
    if not {"date", "stock_id", "stock_name", "open", "high", "low", "close", "volume"}.issubset(df.columns):
        return detail_rows
    first_id = normalize_stock_id(df.iloc[0].get("stock_id"))
    if not is_equity_stock_id(first_id):
        return detail_rows
    price = add_research_features(df)
    if price.empty:
        return detail_rows

    masks = event_filter_masks(price)
    filter_map = {item.event_filter_id: item for item in EVENT_FILTERS}
    candidate_indices = sorted({int(idx) for mask in masks.values() for idx in mask[mask].index})
    for idx in candidate_indices:
        row = price.iloc[idx]
        base_payload = base_event_payload(row, market_regimes)
        matched_filters = [filter_map[filter_id] for filter_id, mask in masks.items() if bool(mask.iloc[idx])]
        simulated_trades: list[tuple[PatternSpec, dict[str, Any]]] = []
        for spec in PATTERN_SPECS:
            trade = simulate_trade(price, idx, spec)
            if trade is not None:
                simulated_trades.append((spec, trade))
        for event_filter in matched_filters:
            for spec, trade in simulated_trades:
                detail_rows.append(
                    {
                        **base_payload,
                        "event_filter_id": event_filter.event_filter_id,
                        "model_hit_status": event_filter.model_hit_status,
                        "pattern_id": spec.pattern_id,
                        **trade,
                    }
                )
    return detail_rows


def out_of_sample_start_date(detail: pd.DataFrame) -> str:
    dates = sorted({safe_str(value) for value in detail.get("event_date", []) if safe_str(value)})
    if len(dates) < 5:
        return ""
    return dates[int(len(dates) * 0.7)]


def profit_factor(returns: pd.Series) -> float | str:
    nums = pd.to_numeric(returns, errors="coerce").dropna()
    gains = nums[nums > 0].sum()
    losses = nums[nums < 0].sum()
    if losses == 0:
        return round(float("inf"), 4) if gains > 0 else ""
    return round(float(gains / abs(losses)), 4)


def win_rate(returns: pd.Series) -> float | str:
    nums = pd.to_numeric(returns, errors="coerce").dropna()
    if nums.empty:
        return ""
    return round(float((nums > 0).mean() * 100.0), 2)


def avg_return(returns: pd.Series) -> float | str:
    nums = pd.to_numeric(returns, errors="coerce").dropna()
    if nums.empty:
        return ""
    return round(float(nums.mean()), 4)


def confidence_status(sample_size: int, oos_size: int, avg_ret: float, pf: float, oos_pass: bool) -> str:
    if sample_size >= 300 and oos_size >= 80 and oos_pass and avg_ret >= 1.5 and pf >= 1.2:
        return "high"
    if sample_size >= 100 and oos_size >= 30 and avg_ret > 0 and pf >= 1.05:
        return "medium"
    return "low"


def out_of_sample_pass(part: pd.DataFrame) -> bool:
    oos = part[part["out_of_sample"].map(bool_value)]
    if len(part) < 100 or len(oos) < 30:
        return False
    all_avg = safe_float(avg_return(part["return_pct"]))
    oos_avg = safe_float(avg_return(oos["return_pct"]))
    oos_win = safe_float(win_rate(oos["return_pct"]))
    return not any(math.isnan(v) for v in [all_avg, oos_avg, oos_win]) and all_avg > 0 and oos_avg > 0 and oos_win >= 45


def best_regime(part: pd.DataFrame) -> str:
    rows: list[tuple[str, int, float]] = []
    for regime, regime_part in part.groupby("market_regime", dropna=False):
        if len(regime_part) < 30:
            continue
        avg_ret = safe_float(avg_return(regime_part["return_pct"]))
        if not math.isnan(avg_ret):
            rows.append((safe_str(regime), len(regime_part), avg_ret))
    if not rows:
        return "sample_not_enough_by_regime"
    rows.sort(key=lambda item: (item[2], item[1]), reverse=True)
    return rows[0][0] or "unknown"


def summarize_registry(detail: pd.DataFrame) -> pd.DataFrame:
    generated_at = now_text()
    if detail.empty:
        return pd.DataFrame(columns=REGISTRY_COLUMNS)

    filter_map = {item.event_filter_id: item for item in EVENT_FILTERS}
    pattern_map = {item.pattern_id: item for item in PATTERN_SPECS}
    data_start = min(detail["event_date"])
    data_end = max(detail["event_date"])
    split_date = out_of_sample_start_date(detail)

    rows: list[dict[str, Any]] = []
    for (event_filter_id, pattern_id), part in detail.groupby(["event_filter_id", "pattern_id"], dropna=False):
        event_filter = filter_map[safe_str(event_filter_id)]
        spec = pattern_map[safe_str(pattern_id)]
        returns = pd.to_numeric(part["return_pct"], errors="coerce")
        mae = pd.to_numeric(part["mae_pct"], errors="coerce")
        holding = pd.to_numeric(part["holding_days"], errors="coerce")
        oos = part[part["out_of_sample"].map(bool_value)]
        ins = part[~part["out_of_sample"].map(bool_value)]
        oos_pass = out_of_sample_pass(part)
        pf_value = profit_factor(returns)
        avg_ret_value = safe_float(avg_return(returns))
        pf_num = safe_float(pf_value)
        if math.isinf(pf_num):
            pf_num = 999.0
        rows.append(
            {
                "model_id": MODEL_ID,
                "model_name_zh": MODEL_NAME_ZH,
                "event_filter_id": event_filter.event_filter_id,
                "event_filter_zh": event_filter.event_filter_zh,
                "model_hit_status": event_filter.model_hit_status,
                "pattern_id": spec.pattern_id,
                "pattern_name_zh": spec.pattern_name_zh,
                "entry_rule_zh": spec.entry_rule_zh,
                "stop_loss_rule_zh": spec.stop_loss_rule_zh,
                "hold_rule_zh": spec.hold_rule_zh,
                "exit_rule_zh": spec.exit_rule_zh,
                "sample_size": len(part),
                "unique_stocks": part["stock_id"].nunique(),
                "win_rate": win_rate(returns),
                "avg_return": avg_return(returns),
                "median_return": round(float(returns.median()), 4) if not returns.dropna().empty else "",
                "max_drawdown": round(float(mae.min()), 4) if not mae.dropna().empty else "",
                "avg_holding_days": round(float(holding.mean()), 2) if not holding.dropna().empty else "",
                "profit_factor": pf_value,
                "in_sample_size": len(ins),
                "in_sample_win_rate": win_rate(ins["return_pct"]),
                "in_sample_avg_return": avg_return(ins["return_pct"]),
                "out_of_sample_size": len(oos),
                "out_of_sample_win_rate": win_rate(oos["return_pct"]),
                "out_of_sample_avg_return": avg_return(oos["return_pct"]),
                "best_for_market_regime": best_regime(part),
                "risk_notes_zh": (
                    event_filter.risk_note_zh
                    + " 同日同時觸及停利與停損時，採保守順序先檢查停損。"
                ),
                "confidence_status": confidence_status(len(part), len(oos), avg_ret_value, pf_num, oos_pass),
                "approved_for_daily": False,
                "out_of_sample_pass": oos_pass,
                "generated_at": generated_at,
                "data_start_date": data_start,
                "data_end_date": data_end,
                "out_of_sample_start_date": split_date,
            }
        )
    out = pd.DataFrame(rows)
    if out.empty:
        return pd.DataFrame(columns=REGISTRY_COLUMNS)
    out["_confidence_order"] = out["confidence_status"].map({"high": 0, "medium": 1, "low": 2}).fillna(9)
    out["_avg_return_sort"] = pd.to_numeric(out["avg_return"], errors="coerce").fillna(-999)
    out = out.sort_values(
        ["model_hit_status", "event_filter_id", "_confidence_order", "_avg_return_sort", "sample_size"],
        ascending=[True, True, True, False, False],
    ).drop(columns=["_confidence_order", "_avg_return_sort"])
    return out[REGISTRY_COLUMNS]


def table_lines(df: pd.DataFrame, columns: list[str], limit: int = 30) -> list[str]:
    if df.empty:
        return ["_No rows._"]
    cols = [col for col in columns if col in df.columns]
    lines = ["| " + " | ".join(cols) + " |", "| " + " | ".join(["---"] * len(cols)) + " |"]
    for _, row in df.head(limit).iterrows():
        vals = [safe_str(row.get(col)).replace("|", "/").replace("\n", " ")[:160] for col in cols]
        lines.append("| " + " | ".join(vals) + " |")
    return lines


def write_registry_md(registry: pd.DataFrame, detail: pd.DataFrame) -> None:
    current = registry[registry["model_hit_status"].eq("current_model_hit")].copy() if not registry.empty else registry
    relaxed = registry[registry["model_hit_status"].ne("current_model_hit")].copy() if not registry.empty else registry
    lines = [
        "# Historical Pattern Operation Registry",
        "",
        f"- generated_at: `{now_text()}`",
        f"- model_id: `{MODEL_ID}`",
        f"- detail_rows: `{len(detail)}`",
        f"- registry_rows: `{len(registry)}`",
        f"- registry_csv_raw_url: {raw_url(REGISTRY_CSV)}",
        f"- detail_csv_raw_url: {raw_url(DETAIL_HISTORY_CSV)}",
        "",
        "## Scope",
        "",
        "- This is research/backtest output only.",
        "- It does not write production config, daily candidate files, or PDF operation text.",
        "- `approved_for_daily` remains `False` until a separate promotion PR explicitly approves a pattern.",
        "- Current model hit groups include locked-limit breakouts without volume-ratio or 20D average-volume gates; non-current research comparisons must not reintroduce the removed volume gate.",
        "",
        "## Current Model Hit Patterns",
        "",
        *table_lines(
            current,
            [
                "event_filter_id",
                "pattern_id",
                "sample_size",
                "win_rate",
                "avg_return",
                "median_return",
                "max_drawdown",
                "avg_holding_days",
                "profit_factor",
                "out_of_sample_size",
                "out_of_sample_win_rate",
                "out_of_sample_avg_return",
                "confidence_status",
                "out_of_sample_pass",
                "approved_for_daily",
            ],
            limit=120,
        ),
        "",
        "## Research-Only Relaxed Comparison",
        "",
        *table_lines(
            relaxed,
            [
                "event_filter_id",
                "pattern_id",
                "sample_size",
                "win_rate",
                "avg_return",
                "median_return",
                "max_drawdown",
                "out_of_sample_size",
                "out_of_sample_avg_return",
                "confidence_status",
                "out_of_sample_pass",
                "approved_for_daily",
            ],
            limit=80,
        ),
        "",
        "## Promotion Gate",
        "",
        "- Minimum gate for future daily adoption: enough `sample_size`, `out_of_sample_pass=True`, `confidence_status` not `low`, explicit pattern rules, and separate human/code approval.",
        "- This artifact intentionally separates entry, stop, hold, and exit rules from the daily stock-selection model.",
        "",
    ]
    REGISTRY_MD.write_text("\n".join(lines) + "\n", encoding="utf-8", newline="\n")


def main() -> int:
    LATEST_DIR.mkdir(parents=True, exist_ok=True)
    RESEARCH_HISTORY_DIR.mkdir(parents=True, exist_ok=True)

    detail = build_detail_events()
    registry = summarize_registry(detail)

    write_csv(detail, DETAIL_HISTORY_CSV)
    write_csv(registry, REGISTRY_CSV)
    write_csv(registry, REGISTRY_HISTORY_CSV)
    write_registry_md(registry, detail)

    print(f"Saved: {REGISTRY_CSV} rows={len(registry)}")
    print(f"Saved: {REGISTRY_MD}")
    print(f"Saved: {DETAIL_HISTORY_CSV} rows={len(detail)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
