from __future__ import annotations

from datetime import datetime
from pathlib import Path
from typing import Any
from zoneinfo import ZoneInfo
import math
import sys

import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent))

from tracking_utils import load_price_history, normalize_code, position_on_or_before  # noqa: E402


ROOT = Path(".")
LATEST_DIR = ROOT / "output" / "latest"
RESEARCH_HISTORY_DIR = ROOT / "output" / "history" / "research"

DETAIL_CSV = RESEARCH_HISTORY_DIR / "historical_pattern_operation_events.csv"
OUT_SUMMARY_CSV = LATEST_DIR / "volume_breakout_pattern_classification_latest.csv"
OUT_SUMMARY_MD = LATEST_DIR / "volume_breakout_pattern_classification_latest.md"
HISTORY_SUMMARY_CSV = RESEARCH_HISTORY_DIR / "volume_breakout_pattern_classification.csv"
HISTORY_EVENTS_CSV = RESEARCH_HISTORY_DIR / "volume_breakout_pattern_classification_events.csv"
OUT_DIMENSION_CSV = LATEST_DIR / "volume_breakout_pattern_dimension_latest.csv"
OUT_DIMENSION_MD = LATEST_DIR / "volume_breakout_pattern_dimension_latest.md"
HISTORY_DIMENSION_CSV = RESEARCH_HISTORY_DIR / "volume_breakout_pattern_dimension.csv"

MODEL_ID = "volume_range_breakout"
PRICE_CACHE: dict[str, pd.DataFrame] = {}

ZH = {
    "locked_limit_up_breakout": "\u9396\u91cf\u6f32\u505c\u7a81\u7834",
    "limit_up_like_breakout": "\u985e\u6f32\u505c\u653e\u91cf\u7a81\u7834",
    "long_base_low_position": "\u9577\u76e4\u6574\u4f4e\u4f4d\u968e\u7a81\u7834",
    "low_position_breakout": "\u4f4e\u4f4d\u968e\u7a81\u7834",
    "high_position_breakout": "\u9ad8\u4f4d\u968e\u7a81\u7834",
    "wide_range_breakout": "\u5bec\u5340\u9593\u7a81\u7834",
    "standard_breakout": "\u4e00\u822c\u7a81\u7834",
    "long_consolidation": "\u9577\u76e4\u6574",
    "short_consolidation": "\u77ed\u76e4\u6574",
    "non_consolidation": "\u975e\u76e4\u6574",
    "unknown_consolidation": "\u76e4\u6574\u8cc7\u6599\u4e0d\u8db3",
    "low_position": "\u4f4e\u4f4d\u968e",
    "middle_position": "\u4e2d\u4f4d\u968e",
    "high_position": "\u9ad8\u4f4d\u968e",
    "unknown_position": "\u4f4d\u968e\u8cc7\u6599\u4e0d\u8db3",
    "locked_limit_up": "\u9396\u91cf\u6f32\u505c",
    "volume_attack": "\u653e\u91cf\u653b\u64ca",
    "general_breakout": "\u4e00\u822c\u7a81\u7834",
    "close_at_high": "\u6536\u6700\u9ad8",
    "upper_shadow": "\u7559\u4e0a\u5f71",
    "explosive_long_red": "\u7206\u91cf\u9577\u7d05",
    "false_breakout": "\u5047\u7a81\u7834",
    "standard_candle": "\u4e00\u822cK\u68d2",
    "next_day_continuation": "\u9694\u65e5\u7e8c\u5f37",
    "next_day_gap_fade": "\u9694\u65e5\u958b\u9ad8\u8d70\u4f4e",
    "pullback_5ma": "\u56de\u6e2c5MA",
    "pullback_10ma": "\u56de\u6e2c10MA",
    "break_signal_low": "\u8dcc\u7834\u8a0a\u865f\u4f4e\u9ede",
    "no_clear_follow_through": "\u5f8c\u7e8c\u4e0d\u660e\u78ba",
    "high_position_chase": "\u9ad8\u4f4d\u968e\u8ffd\u50f9",
    "volume_overheat": "\u91cf\u80fd\u904e\u71b1",
    "breakout_failure": "\u7a81\u7834\u5931\u6557",
    "stop_loss_easy_trigger": "\u505c\u640d\u5bb9\u6613\u88ab\u6253\u5230",
    "normal_risk": "\u4e00\u822c\u98a8\u96aa",
}

SUMMARY_COLUMNS = [
    "model_id",
    "classification_id",
    "classification_name_zh",
    "pattern_id",
    "event_count",
    "unique_stocks",
    "win_rate",
    "avg_return",
    "median_return",
    "max_drawdown",
    "avg_mfe",
    "avg_mae",
    "avg_holding_days",
    "profit_factor",
    "out_of_sample_size",
    "out_of_sample_win_rate",
    "out_of_sample_avg_return",
    "confidence_status",
    "out_of_sample_pass",
    "approved_for_daily",
    "risk_notes_zh",
    "generated_at",
    "data_start_date",
    "data_end_date",
]

DIMENSION_SUMMARY_COLUMNS = [
    "model_id",
    "dimension_type",
    "dimension_id",
    "dimension_name_zh",
    "pattern_id",
    "event_count",
    "unique_stocks",
    "win_rate",
    "avg_return",
    "median_return",
    "max_drawdown",
    "avg_mfe",
    "avg_mae",
    "avg_holding_days",
    "profit_factor",
    "out_of_sample_size",
    "out_of_sample_win_rate",
    "out_of_sample_avg_return",
    "confidence_status",
    "out_of_sample_pass",
    "approved_for_daily",
    "risk_notes_zh",
    "generated_at",
    "data_start_date",
    "data_end_date",
]

EVENT_COLUMNS = [
    "model_id",
    "event_date",
    "stock_id",
    "stock_name",
    "market",
    "market_regime",
    "classification_id",
    "classification_name_zh",
    "pattern_tags",
    "consolidation_type",
    "consolidation_name_zh",
    "price_position_type",
    "price_position_name_zh",
    "attack_method",
    "attack_method_name_zh",
    "candle_quality",
    "candle_quality_name_zh",
    "follow_through_type",
    "follow_through_name_zh",
    "follow_through_tags",
    "risk_type",
    "risk_name_zh",
    "risk_tags",
    "volume_ratio",
    "signal_return_1d_pct",
    "signal_open",
    "signal_high",
    "signal_low",
    "signal_close",
    "next_open",
    "next_high",
    "next_low",
    "next_close",
    "touch_5ma_10d",
    "touch_10ma_10d",
    "break_signal_low_5d",
    "range_width_20_pct",
    "range_width_40_pct",
    "range_width_60_pct",
    "low_position_60_pct",
    "limit_up_like",
    "out_of_sample",
]

DIMENSION_DEFINITIONS = [
    ("consolidation_type", "\u76e4\u6574\u578b\u614b"),
    ("price_position_type", "\u4f4d\u968e"),
    ("attack_method", "\u653b\u64ca\u65b9\u5f0f"),
    ("candle_quality", "K\u68d2\u54c1\u8cea"),
    ("follow_through_type", "\u5f8c\u7e8c\u8d70\u6cd5"),
    ("risk_type", "\u98a8\u96aa\u578b\u614b"),
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
    text = str(value).strip()
    if text.lower() in {"nan", "none", "nat", "<na>"}:
        return ""
    return text


def safe_float(value: Any, default: float = math.nan) -> float:
    text = safe_str(value).replace(",", "").replace("%", "")
    if text in {"", "-"}:
        return default
    try:
        return float(text)
    except Exception:
        return default


def bool_value(value: Any) -> bool:
    return safe_str(value).lower() in {"1", "1.0", "true", "yes", "y", "t"}


def write_csv(df: pd.DataFrame, path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(path, index=False, encoding="utf-8-sig", lineterminator="\n")


def pct_round(value: Any) -> float | str:
    num = safe_float(value)
    return round(num, 4) if not math.isnan(num) else ""


def cached_price_history(stock_id: Any) -> pd.DataFrame:
    code = normalize_code(stock_id)
    if not code:
        return pd.DataFrame()
    if code not in PRICE_CACHE:
        price = load_price_history(code)
        if not price.empty and "close" in price.columns:
            close = pd.to_numeric(price["close"], errors="coerce")
            if "ma5" not in price.columns or pd.to_numeric(price.get("ma5"), errors="coerce").isna().all():
                price["ma5"] = close.rolling(5, min_periods=5).mean()
            if "ma10" not in price.columns or pd.to_numeric(price.get("ma10"), errors="coerce").isna().all():
                price["ma10"] = close.rolling(10, min_periods=10).mean()
        PRICE_CACHE[code] = price
    return PRICE_CACHE[code]


def price_context(row: pd.Series) -> dict[str, Any]:
    price = cached_price_history(row.get("stock_id"))
    pos = position_on_or_before(price, safe_str(row.get("event_date")))
    empty = {
        "signal_open": "",
        "signal_high": "",
        "signal_low": "",
        "signal_close": "",
        "signal_ma5": "",
        "signal_ma10": "",
        "next_open": "",
        "next_high": "",
        "next_low": "",
        "next_close": "",
        "next_ma5": "",
        "next_ma10": "",
        "touch_5ma_10d": False,
        "touch_10ma_10d": False,
        "break_signal_low_5d": False,
        "close_below_prior20_next_day": False,
    }
    if pos is None:
        return empty
    signal = price.loc[pos]
    out = empty.copy()
    for source, target in [
        ("open", "signal_open"),
        ("high", "signal_high"),
        ("low", "signal_low"),
        ("close", "signal_close"),
        ("ma5", "signal_ma5"),
        ("ma10", "signal_ma10"),
    ]:
        out[target] = pct_round(signal.get(source))
    if pos + 1 < len(price):
        nxt = price.loc[pos + 1]
        for source, target in [
            ("open", "next_open"),
            ("high", "next_high"),
            ("low", "next_low"),
            ("close", "next_close"),
            ("ma5", "next_ma5"),
            ("ma10", "next_ma10"),
        ]:
            out[target] = pct_round(nxt.get(source))
        previous_20d_high = safe_float(row.get("previous_20d_high"))
        next_close = safe_float(out["next_close"])
        out["close_below_prior20_next_day"] = (
            not math.isnan(previous_20d_high)
            and not math.isnan(next_close)
            and next_close < previous_20d_high
        )
    window = price.iloc[pos + 1 : min(len(price), pos + 11)].copy()
    signal_low = safe_float(out["signal_low"])
    if not window.empty:
        low = pd.to_numeric(window.get("low", pd.Series(index=window.index, dtype=float)), errors="coerce")
        ma5 = pd.to_numeric(window.get("ma5", pd.Series(index=window.index, dtype=float)), errors="coerce")
        ma10 = pd.to_numeric(window.get("ma10", pd.Series(index=window.index, dtype=float)), errors="coerce")
        out["touch_5ma_10d"] = bool((low <= ma5).fillna(False).any())
        out["touch_10ma_10d"] = bool((low <= ma10).fillna(False).any())
        out["break_signal_low_5d"] = bool(
            not math.isnan(signal_low)
            and (low.head(5) <= signal_low).fillna(False).any()
        )
    return out


def consolidation_dimension(row: pd.Series) -> tuple[str, str]:
    width20 = safe_float(row.get("range_width_20_pct"))
    width40 = safe_float(row.get("range_width_40_pct"))
    width60 = safe_float(row.get("range_width_60_pct"))
    if not math.isnan(width60) and width60 <= 30:
        return "long_consolidation", ZH["long_consolidation"]
    if not math.isnan(width40) and width40 <= 25:
        return "long_consolidation", ZH["long_consolidation"]
    if not math.isnan(width20) and width20 <= 18:
        return "short_consolidation", ZH["short_consolidation"]
    if any(not math.isnan(value) for value in [width20, width40, width60]):
        return "non_consolidation", ZH["non_consolidation"]
    return "unknown_consolidation", ZH["unknown_consolidation"]


def price_position_dimension(row: pd.Series) -> tuple[str, str]:
    low_pos60 = safe_float(row.get("low_position_60_pct"))
    if math.isnan(low_pos60):
        return "unknown_position", ZH["unknown_position"]
    if low_pos60 <= 60:
        return "low_position", ZH["low_position"]
    if low_pos60 >= 80:
        return "high_position", ZH["high_position"]
    return "middle_position", ZH["middle_position"]


def attack_method_dimension(row: pd.Series) -> tuple[str, str]:
    volume_ratio = safe_float(row.get("volume_ratio"))
    limit_up_like = bool_value(row.get("limit_up_like"))
    if limit_up_like and not math.isnan(volume_ratio) and volume_ratio < 2:
        return "locked_limit_up", ZH["locked_limit_up"]
    if not math.isnan(volume_ratio) and volume_ratio >= 3:
        return "volume_attack", ZH["volume_attack"]
    return "general_breakout", ZH["general_breakout"]


def candle_quality_dimension(row: pd.Series) -> tuple[str, str]:
    open_price = safe_float(row.get("signal_open"))
    high = safe_float(row.get("signal_high"))
    low = safe_float(row.get("signal_low"))
    close = safe_float(row.get("signal_close"))
    volume_ratio = safe_float(row.get("volume_ratio"))
    signal_return = safe_float(row.get("signal_return_1d_pct"))
    prior20 = safe_float(row.get("previous_20d_high"))
    next_close = safe_float(row.get("next_close"))

    if not math.isnan(next_close) and not math.isnan(prior20) and next_close < prior20:
        return "false_breakout", ZH["false_breakout"]
    if not math.isnan(high) and not math.isnan(close) and high > 0 and abs(close - high) / high <= 0.003:
        return "close_at_high", ZH["close_at_high"]
    if (
        not math.isnan(open_price)
        and not math.isnan(close)
        and not math.isnan(signal_return)
        and not math.isnan(volume_ratio)
        and close > open_price
        and signal_return >= 5
        and volume_ratio >= 3
    ):
        return "explosive_long_red", ZH["explosive_long_red"]
    if not math.isnan(high) and not math.isnan(low) and high > low and not math.isnan(close):
        upper_shadow_ratio = (high - max(open_price if not math.isnan(open_price) else close, close)) / (high - low)
        if upper_shadow_ratio >= 0.35:
            return "upper_shadow", ZH["upper_shadow"]
    return "standard_candle", ZH["standard_candle"]


def follow_through_dimension(row: pd.Series) -> tuple[str, str, str]:
    close = safe_float(row.get("signal_close"))
    high = safe_float(row.get("signal_high"))
    low = safe_float(row.get("signal_low"))
    next_open = safe_float(row.get("next_open"))
    next_close = safe_float(row.get("next_close"))
    next_low = safe_float(row.get("next_low"))
    tags: list[str] = []

    next_day_continuation = (
        not math.isnan(close)
        and not math.isnan(next_close)
        and next_close > close
        and (math.isnan(high) or next_close >= high)
    )
    next_day_gap_fade = (
        not math.isnan(close)
        and not math.isnan(next_open)
        and not math.isnan(next_close)
        and next_open > close
        and next_close < next_open
    )
    pullback_5ma = bool(row.get("touch_5ma_10d"))
    pullback_10ma = bool(row.get("touch_10ma_10d"))
    break_signal_low = bool(row.get("break_signal_low_5d")) or (
        not math.isnan(low) and not math.isnan(next_low) and next_low < low
    )

    if next_day_continuation:
        tags.append("next_day_continuation")
    if next_day_gap_fade:
        tags.append("next_day_gap_fade")
    if pullback_5ma:
        tags.append("pullback_5ma")
    if pullback_10ma:
        tags.append("pullback_10ma")
    if break_signal_low:
        tags.append("break_signal_low")

    if break_signal_low:
        return "break_signal_low", ZH["break_signal_low"], "|".join(tags)
    if next_day_gap_fade:
        return "next_day_gap_fade", ZH["next_day_gap_fade"], "|".join(tags)
    if next_day_continuation:
        return "next_day_continuation", ZH["next_day_continuation"], "|".join(tags)
    if pullback_10ma:
        return "pullback_10ma", ZH["pullback_10ma"], "|".join(tags)
    if pullback_5ma:
        return "pullback_5ma", ZH["pullback_5ma"], "|".join(tags)
    return "no_clear_follow_through", ZH["no_clear_follow_through"], "|".join(tags)


def risk_dimension(row: pd.Series) -> tuple[str, str, str]:
    price_position, _ = price_position_dimension(row)
    volume_ratio = safe_float(row.get("volume_ratio"))
    signal_return = safe_float(row.get("signal_return_1d_pct"))
    follow = safe_str(row.get("follow_through_type"))
    close = safe_float(row.get("signal_close"))
    low = safe_float(row.get("signal_low"))
    tags: list[str] = []

    if price_position == "high_position" and not math.isnan(signal_return) and signal_return >= 5:
        tags.append("high_position_chase")
    if not math.isnan(volume_ratio) and volume_ratio >= 5:
        tags.append("volume_overheat")
    if follow == "break_signal_low" or bool(row.get("close_below_prior20_next_day")):
        tags.append("breakout_failure")
    if not math.isnan(close) and not math.isnan(low) and close > 0 and (close / low - 1.0) * 100 <= 3:
        tags.append("tight_signal_low_stop")
    if bool(row.get("break_signal_low_5d")):
        tags.append("stop_loss_easy_trigger")

    if "breakout_failure" in tags:
        return "breakout_failure", ZH["breakout_failure"], "|".join(tags)
    if "high_position_chase" in tags:
        return "high_position_chase", ZH["high_position_chase"], "|".join(tags)
    if "volume_overheat" in tags:
        return "volume_overheat", ZH["volume_overheat"], "|".join(tags)
    if "stop_loss_easy_trigger" in tags or "tight_signal_low_stop" in tags:
        return "stop_loss_easy_trigger", ZH["stop_loss_easy_trigger"], "|".join(tags)
    return "normal_risk", ZH["normal_risk"], "|".join(tags)


def classify_event(row: pd.Series) -> dict[str, str]:
    volume_ratio = safe_float(row.get("volume_ratio"))
    width40 = safe_float(row.get("range_width_40_pct"))
    low_pos60 = safe_float(row.get("low_position_60_pct"))
    limit_up_like = bool_value(row.get("limit_up_like"))
    consolidation_type, consolidation_name = consolidation_dimension(row)
    price_position_type, price_position_name = price_position_dimension(row)
    attack_method, attack_method_name = attack_method_dimension(row)
    candle_quality, candle_quality_name = candle_quality_dimension(row)
    follow_type, follow_name, follow_tags = follow_through_dimension(row)
    risk_row = row.copy()
    risk_row["follow_through_type"] = follow_type
    risk_type, risk_name, risk_tags = risk_dimension(risk_row)

    tags: list[str] = []
    if limit_up_like:
        tags.append("limit_up_like")
    if not math.isnan(volume_ratio):
        if volume_ratio < 2:
            tags.append("volume_ratio_lt_2")
        elif volume_ratio >= 3:
            tags.append("volume_ratio_ge_3")
        else:
            tags.append("volume_ratio_2_3")
    if not math.isnan(width40):
        tags.append("long_base" if width40 <= 25 else "wide_base")
    if not math.isnan(low_pos60):
        if low_pos60 <= 60:
            tags.append("low_position_60")
        elif low_pos60 >= 80:
            tags.append("high_position_60")
        else:
            tags.append("middle_position_60")
    tags.extend([consolidation_type, price_position_type, attack_method, candle_quality, follow_type, risk_type])

    if limit_up_like and not math.isnan(volume_ratio) and volume_ratio < 2:
        classification_id = "locked_limit_up_breakout"
    elif limit_up_like:
        classification_id = "limit_up_like_breakout"
    elif not math.isnan(width40) and not math.isnan(low_pos60) and width40 <= 25 and low_pos60 <= 60:
        classification_id = "long_base_low_position"
    elif not math.isnan(low_pos60) and low_pos60 <= 60:
        classification_id = "low_position_breakout"
    elif not math.isnan(low_pos60) and low_pos60 >= 80:
        classification_id = "high_position_breakout"
    elif not math.isnan(width40) and width40 > 25:
        classification_id = "wide_range_breakout"
    else:
        classification_id = "standard_breakout"

    return {
        "classification_id": classification_id,
        "classification_name_zh": ZH[classification_id],
        "pattern_tags": "|".join(dict.fromkeys(tags)),
        "consolidation_type": consolidation_type,
        "consolidation_name_zh": consolidation_name,
        "price_position_type": price_position_type,
        "price_position_name_zh": price_position_name,
        "attack_method": attack_method,
        "attack_method_name_zh": attack_method_name,
        "candle_quality": candle_quality,
        "candle_quality_name_zh": candle_quality_name,
        "follow_through_type": follow_type,
        "follow_through_name_zh": follow_name,
        "follow_through_tags": follow_tags,
        "risk_type": risk_type,
        "risk_name_zh": risk_name,
        "risk_tags": risk_tags,
    }


def unique_current_events(detail: pd.DataFrame) -> pd.DataFrame:
    current = detail[
        detail["model_id"].astype(str).eq(MODEL_ID)
        & detail["event_filter_id"].astype(str).eq("current_model_hit_all")
        & detail["model_hit_status"].astype(str).eq("current_model_hit")
    ].copy()
    if current.empty:
        return pd.DataFrame(columns=EVENT_COLUMNS)

    event_cols = [
        "model_id",
        "event_date",
        "stock_id",
        "stock_name",
        "market",
        "market_regime",
        "volume_ratio",
        "signal_return_1d_pct",
        "previous_20d_high",
        "range_width_20_pct",
        "range_width_40_pct",
        "range_width_60_pct",
        "low_position_60_pct",
        "limit_up_like",
        "out_of_sample",
    ]
    events = current[event_cols].drop_duplicates(["event_date", "stock_id"], keep="first").copy()
    price_features = events.apply(price_context, axis=1, result_type="expand")
    events = pd.concat([events, price_features], axis=1)
    classes = events.apply(classify_event, axis=1, result_type="expand")
    events = pd.concat([events, classes], axis=1)
    return events[EVENT_COLUMNS].sort_values(["event_date", "stock_id"]).reset_index(drop=True)


def profit_factor(returns: pd.Series) -> float | str:
    nums = pd.to_numeric(returns, errors="coerce").dropna()
    if nums.empty:
        return ""
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


def confidence_status(sample: int) -> str:
    if sample >= 500:
        return "high"
    if sample >= 100:
        return "medium"
    return "low"


def summary_row(
    group_key: str,
    group_name: str,
    pattern_id: str,
    part: pd.DataFrame,
    generated_at: str,
    data_start: str,
    data_end: str,
) -> dict[str, Any]:
    returns = pd.to_numeric(part["return_pct"], errors="coerce").dropna()
    mae = pd.to_numeric(part.get("mae_pct", pd.Series(dtype=float)), errors="coerce")
    mfe = pd.to_numeric(part.get("mfe_pct", pd.Series(dtype=float)), errors="coerce")
    holding = pd.to_numeric(part.get("holding_days", pd.Series(dtype=float)), errors="coerce")
    oos = part[part["out_of_sample"].map(bool_value)].copy()
    oos_returns = pd.to_numeric(oos["return_pct"], errors="coerce").dropna()
    sample = int(len(returns))
    oos_avg = round(float(oos_returns.mean()), 4) if not oos_returns.empty else ""
    oos_win = win_rate(oos_returns)
    oos_pass = bool(len(oos_returns) >= 30 and safe_float(oos_avg) > 0 and safe_float(oos_win) >= 50)
    return {
        "model_id": MODEL_ID,
        "group_key": safe_str(group_key),
        "group_name_zh": safe_str(group_name),
        "pattern_id": safe_str(pattern_id),
        "event_count": sample,
        "unique_stocks": int(part["stock_id"].nunique()),
        "win_rate": win_rate(returns),
        "avg_return": round(float(returns.mean()), 4) if not returns.empty else "",
        "median_return": round(float(returns.median()), 4) if not returns.empty else "",
        "max_drawdown": round(float(mae.min()), 4) if not mae.dropna().empty else "",
        "avg_mfe": round(float(mfe.mean()), 4) if not mfe.dropna().empty else "",
        "avg_mae": round(float(mae.mean()), 4) if not mae.dropna().empty else "",
        "avg_holding_days": round(float(holding.mean()), 2) if not holding.dropna().empty else "",
        "profit_factor": profit_factor(returns),
        "out_of_sample_size": int(len(oos_returns)),
        "out_of_sample_win_rate": oos_win,
        "out_of_sample_avg_return": oos_avg,
        "confidence_status": confidence_status(sample),
        "out_of_sample_pass": oos_pass,
        "approved_for_daily": False,
        "risk_notes_zh": "research classification only; approved_for_daily remains False",
        "generated_at": generated_at,
        "data_start_date": data_start,
        "data_end_date": data_end,
    }


def summarize(detail: pd.DataFrame, events: pd.DataFrame) -> pd.DataFrame:
    if detail.empty or events.empty:
        return pd.DataFrame(columns=SUMMARY_COLUMNS)

    current = detail[
        detail["model_id"].astype(str).eq(MODEL_ID)
        & detail["event_filter_id"].astype(str).eq("current_model_hit_all")
        & detail["model_hit_status"].astype(str).eq("current_model_hit")
    ].copy()
    joined = current.merge(
        events[["event_date", "stock_id", "classification_id", "classification_name_zh"]],
        on=["event_date", "stock_id"],
        how="inner",
    )
    generated_at = now_text()
    data_start = safe_str(events["event_date"].min())
    data_end = safe_str(events["event_date"].max())
    rows: list[dict[str, Any]] = []
    for (classification_id, pattern_id), part in joined.groupby(["classification_id", "pattern_id"], dropna=False):
        class_name = safe_str(part["classification_name_zh"].iloc[0])
        row = summary_row(safe_str(classification_id), class_name, safe_str(pattern_id), part, generated_at, data_start, data_end)
        row["classification_id"] = row.pop("group_key")
        row["classification_name_zh"] = row.pop("group_name_zh")
        rows.append(row)
    out = pd.DataFrame(rows)
    if out.empty:
        return pd.DataFrame(columns=SUMMARY_COLUMNS)
    out["_confidence_order"] = out["confidence_status"].map({"high": 0, "medium": 1, "low": 2}).fillna(9)
    out["_avg"] = pd.to_numeric(out["avg_return"], errors="coerce").fillna(-999)
    out = out.sort_values(["classification_id", "_confidence_order", "_avg", "event_count"], ascending=[True, True, False, False])
    return out.drop(columns=["_confidence_order", "_avg"])[SUMMARY_COLUMNS].reset_index(drop=True)


def summarize_dimensions(detail: pd.DataFrame, events: pd.DataFrame) -> pd.DataFrame:
    if detail.empty or events.empty:
        return pd.DataFrame(columns=DIMENSION_SUMMARY_COLUMNS)
    current = detail[
        detail["model_id"].astype(str).eq(MODEL_ID)
        & detail["event_filter_id"].astype(str).eq("current_model_hit_all")
        & detail["model_hit_status"].astype(str).eq("current_model_hit")
    ].copy()
    generated_at = now_text()
    data_start = safe_str(events["event_date"].min())
    data_end = safe_str(events["event_date"].max())
    rows: list[dict[str, Any]] = []
    for dimension_col, dimension_type_zh in DIMENSION_DEFINITIONS:
        name_col = f"{dimension_col.replace('_type', '')}_name_zh"
        if dimension_col == "attack_method":
            name_col = "attack_method_name_zh"
        if dimension_col == "candle_quality":
            name_col = "candle_quality_name_zh"
        joined = current.merge(
            events[["event_date", "stock_id", dimension_col, name_col]],
            on=["event_date", "stock_id"],
            how="inner",
        )
        for (dimension_id, pattern_id), part in joined.groupby([dimension_col, "pattern_id"], dropna=False):
            dimension_name = safe_str(part[name_col].iloc[0]) if name_col in part else safe_str(dimension_id)
            row = summary_row(safe_str(dimension_id), dimension_name, safe_str(pattern_id), part, generated_at, data_start, data_end)
            row["dimension_type"] = dimension_col
            row["dimension_type_zh"] = dimension_type_zh
            row["dimension_id"] = row.pop("group_key")
            row["dimension_name_zh"] = row.pop("group_name_zh")
            rows.append(row)
    out = pd.DataFrame(rows)
    if out.empty:
        return pd.DataFrame(columns=DIMENSION_SUMMARY_COLUMNS)
    out["_dimension_order"] = out["dimension_type"].map({name: idx for idx, (name, _) in enumerate(DIMENSION_DEFINITIONS)}).fillna(99)
    out["_confidence_order"] = out["confidence_status"].map({"high": 0, "medium": 1, "low": 2}).fillna(9)
    out["_avg"] = pd.to_numeric(out["avg_return"], errors="coerce").fillna(-999)
    out = out.sort_values(
        ["_dimension_order", "dimension_id", "_confidence_order", "_avg", "event_count"],
        ascending=[True, True, True, False, False],
    )
    return out.drop(columns=["_dimension_order", "_confidence_order", "_avg"], errors="ignore")[
        DIMENSION_SUMMARY_COLUMNS
    ].reset_index(drop=True)


def markdown_table(df: pd.DataFrame, cols: list[str], limit: int = 30) -> list[str]:
    if df.empty:
        return ["_No rows._"]
    lines = ["| " + " | ".join(cols) + " |", "| " + " | ".join(["---"] * len(cols)) + " |"]
    for _, row in df.head(limit).iterrows():
        vals = [safe_str(row.get(col)).replace("|", "/").replace("\n", " ")[:120] for col in cols]
        lines.append("| " + " | ".join(vals) + " |")
    return lines


def write_classification_markdown(summary: pd.DataFrame, events: pd.DataFrame) -> None:
    counts = (
        events.groupby(["classification_id", "classification_name_zh"], dropna=False)
        .size()
        .reset_index(name="event_count")
        .sort_values("event_count", ascending=False)
    )
    best = summary.copy()
    if not best.empty:
        best["_avg"] = pd.to_numeric(best["avg_return"], errors="coerce").fillna(-999)
        best = best.sort_values(["classification_id", "_avg", "event_count"], ascending=[True, False, False])
        best = best.groupby("classification_id", as_index=False).head(3).drop(columns=["_avg"])
    lines = [
        "# Volume Breakout Pattern Classification",
        "",
        f"- generated_at: `{now_text()}`",
        f"- model_id: `{MODEL_ID}`",
        f"- unique_event_rows: `{len(events)}`",
        f"- summary_rows: `{len(summary)}`",
        "- scope: current model hits only; research classification, not production promotion.",
        "- approved_for_daily: always `False` in this artifact.",
        "",
        "## Classification Counts",
        "",
        *markdown_table(counts, ["classification_id", "classification_name_zh", "event_count"], 30),
        "",
        "## Best Operation Patterns By Classification",
        "",
        *markdown_table(
            best,
            [
                "classification_id",
                "pattern_id",
                "event_count",
                "win_rate",
                "avg_return",
                "median_return",
                "out_of_sample_size",
                "out_of_sample_avg_return",
                "confidence_status",
                "out_of_sample_pass",
            ],
            80,
        ),
    ]
    OUT_SUMMARY_MD.parent.mkdir(parents=True, exist_ok=True)
    OUT_SUMMARY_MD.write_text("\n".join(lines) + "\n", encoding="utf-8", newline="\n")


def write_dimension_markdown(dimension_summary: pd.DataFrame, events: pd.DataFrame) -> None:
    counts_rows: list[pd.DataFrame] = []
    for dimension_col, dimension_type_zh in DIMENSION_DEFINITIONS:
        name_col = f"{dimension_col.replace('_type', '')}_name_zh"
        if dimension_col == "attack_method":
            name_col = "attack_method_name_zh"
        if dimension_col == "candle_quality":
            name_col = "candle_quality_name_zh"
        counts = (
            events.groupby([dimension_col, name_col], dropna=False)
            .size()
            .reset_index(name="event_count")
            .rename(columns={dimension_col: "dimension_id", name_col: "dimension_name_zh"})
        )
        counts["dimension_type"] = dimension_col
        counts["dimension_type_zh"] = dimension_type_zh
        counts_rows.append(counts)
    counts_all = pd.concat(counts_rows, ignore_index=True, sort=False) if counts_rows else pd.DataFrame()

    best = dimension_summary.copy()
    if not best.empty:
        best["_avg"] = pd.to_numeric(best["avg_return"], errors="coerce").fillna(-999)
        best = best.sort_values(["dimension_type", "dimension_id", "_avg", "event_count"], ascending=[True, True, False, False])
        best = best.groupby(["dimension_type", "dimension_id"], as_index=False).head(2).drop(columns=["_avg"])

    lines = [
        "# Volume Breakout Pattern Dimensions",
        "",
        f"- generated_at: `{now_text()}`",
        f"- model_id: `{MODEL_ID}`",
        f"- unique_event_rows: `{len(events)}`",
        "- dimensions: consolidation, price position, attack method, candle quality, follow-through, risk type.",
        "- scope: research only; all rows keep `approved_for_daily=False`.",
        "",
        "## Dimension Counts",
        "",
        *markdown_table(counts_all, ["dimension_type", "dimension_type_zh", "dimension_id", "dimension_name_zh", "event_count"], 80),
        "",
        "## Best Operation Patterns By Dimension",
        "",
        *markdown_table(
            best,
            [
                "dimension_type",
                "dimension_id",
                "dimension_name_zh",
                "pattern_id",
                "event_count",
                "win_rate",
                "avg_return",
                "median_return",
                "confidence_status",
                "out_of_sample_pass",
            ],
            120,
        ),
    ]
    OUT_DIMENSION_MD.parent.mkdir(parents=True, exist_ok=True)
    OUT_DIMENSION_MD.write_text("\n".join(lines) + "\n", encoding="utf-8", newline="\n")


def main() -> int:
    if not DETAIL_CSV.exists():
        raise FileNotFoundError(f"missing historical operation detail: {DETAIL_CSV}")
    detail = pd.read_csv(DETAIL_CSV, dtype=str, keep_default_na=False)
    events = unique_current_events(detail)
    summary = summarize(detail, events)
    dimension_summary = summarize_dimensions(detail, events)
    write_csv(events, HISTORY_EVENTS_CSV)
    write_csv(summary, OUT_SUMMARY_CSV)
    write_csv(summary, HISTORY_SUMMARY_CSV)
    write_csv(dimension_summary, OUT_DIMENSION_CSV)
    write_csv(dimension_summary, HISTORY_DIMENSION_CSV)
    write_classification_markdown(summary, events)
    write_dimension_markdown(dimension_summary, events)
    print(f"Saved: {OUT_SUMMARY_CSV} rows={len(summary)}")
    print(f"Saved: {OUT_DIMENSION_CSV} rows={len(dimension_summary)}")
    print(f"Saved: {HISTORY_EVENTS_CSV} rows={len(events)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
