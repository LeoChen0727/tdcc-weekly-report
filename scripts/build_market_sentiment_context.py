from __future__ import annotations

import math
import re
import sys
from pathlib import Path
from typing import Any

import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent))

from tracking_utils import (  # noqa: E402
    DATA_DIR,
    DOCS_LATEST_DIR,
    HISTORY_DIR,
    LATEST_DIR,
    append_update_csv,
    main_price_date_from_freshness,
    normalize_date,
    now_text,
    read_csv,
    safe_str,
    to_number,
    write_csv,
)


FUTURES_OPTIONS_LATEST = LATEST_DIR / "futures_options_indicators_latest.csv"
MARKET_REGIME_LATEST = LATEST_DIR / "market_regime_latest.csv"
MARKET_RISK_DASHBOARD_MD = LATEST_DIR / "market_risk_dashboard_latest.md"
MARKET_TIMING_PACKET_MD = LATEST_DIR / "market_timing_chatgpt_packet_latest.md"
MARKET_INDEX_HISTORY = DATA_DIR / "market_index_history.csv"

TAIWAN_VIX_HISTORY = DATA_DIR / "futures_options" / "taiwan_vix_history.csv"
TAIFEX_FUTURES_CONTRACTS_HISTORY = DATA_DIR / "futures_options" / "taifex_futures_contracts_history.csv"
PUT_CALL_RATIO_HISTORY = DATA_DIR / "futures_options" / "put_call_ratio_history.csv"

MARKET_RISK_HISTORY_DIR = HISTORY_DIR / "market_risk"
MARKET_SENTIMENT_CONTEXT_CSV = LATEST_DIR / "market_sentiment_context_latest.csv"
MARKET_SENTIMENT_CONTEXT_MD = LATEST_DIR / "market_sentiment_context_latest.md"
MARKET_SENTIMENT_CONTEXT_HISTORY = MARKET_RISK_HISTORY_DIR / "market_sentiment_context_history.csv"
VIX_HISTORY_OUT = MARKET_RISK_HISTORY_DIR / "vix_history.csv"
RETAIL_MTX_HISTORY_OUT = MARKET_RISK_HISTORY_DIR / "retail_mtx_sentiment_history.csv"
FUTURES_OPTIONS_HISTORY_OUT = MARKET_RISK_HISTORY_DIR / "futures_options_indicators_history.csv"

DOCS_MARKET_SENTIMENT_CONTEXT_CSV = DOCS_LATEST_DIR / "market_sentiment_context_latest.csv"
DOCS_MARKET_SENTIMENT_CONTEXT_MD = DOCS_LATEST_DIR / "market_sentiment_context_latest.md"

CONTEXT_START = "<!-- MARKET_SENTIMENT_CONTEXT_START -->"
CONTEXT_END = "<!-- MARKET_SENTIMENT_CONTEXT_END -->"


REQUIRED_CONTEXT_COLUMNS = [
    "date",
    "taiwan_vix",
    "taiwan_vix_252d_high",
    "taiwan_vix_252d_low",
    "taiwan_vix_252d_percentile",
    "taiwan_vix_504d_high",
    "taiwan_vix_504d_low",
    "taiwan_vix_504d_percentile",
    "taiwan_vix_zscore_252d",
    "taiwan_vix_rank_label",
    "vix_context_label",
    "vix_return_5d",
    "vix_return_10d",
    "vix_return_20d",
    "retail_mtx_net_oi_proxy",
    "retail_mtx_proxy_method",
    "retail_mtx_proxy_252d_high",
    "retail_mtx_proxy_252d_low",
    "retail_mtx_proxy_252d_percentile",
    "retail_mtx_proxy_504d_high",
    "retail_mtx_proxy_504d_low",
    "retail_mtx_proxy_504d_percentile",
    "retail_mtx_proxy_zscore_252d",
    "retail_mtx_rank_label",
    "retail_mtx_context_label",
    "foreign_tx_futures_net_oi",
    "dealer_tx_futures_net_oi",
    "trust_tx_futures_net_oi",
    "foreign_futures_net_oi",
    "put_call_oi_ratio_pct",
    "foreign_txo_call_net_oi",
    "foreign_txo_put_net_oi",
    "foreign_txo_synthetic_net_oi",
    "twse_close",
    "tpex_close",
    "twse_distance_to_20d_high",
    "twse_distance_to_60d_high",
    "twse_distance_to_252d_high",
    "twse_distance_to_20d_low",
    "twse_distance_to_60d_low",
    "twse_distance_to_252d_low",
    "tpex_distance_to_20d_high",
    "tpex_distance_to_60d_high",
    "tpex_distance_to_252d_high",
    "tpex_distance_to_20d_low",
    "tpex_distance_to_60d_low",
    "tpex_distance_to_252d_low",
    "twse_above_ma20",
    "twse_above_ma60",
    "tpex_above_ma20",
    "tpex_above_ma60",
    "market_regime",
    "risk_level",
    "sample_status",
    "vix_index_interpretation",
    "retail_mtx_index_interpretation",
    "combined_sentiment_interpretation",
    "sentiment_warning_level",
    "data_quality_note",
]


def _num(value: Any) -> float | None:
    result = to_number(value)
    if math.isnan(result):
        return None
    return float(result)


def _round(value: Any, digits: int = 4) -> Any:
    result = _num(value)
    if result is None:
        return ""
    return round(result, digits)


def _bool(value: Any) -> bool:
    return safe_str(value).lower() in {"true", "1", "yes", "y"}


def _pct_rank(values: pd.Series, latest: float) -> float:
    clean = pd.to_numeric(values, errors="coerce").dropna()
    if clean.empty:
        return float("nan")
    return float((clean <= latest).sum() / len(clean) * 100)



def _window_stats(series: pd.Series, latest_value: Any) -> dict[str, Any]:
    clean = pd.to_numeric(series, errors="coerce").dropna()
    latest = _num(latest_value)
    if latest is None and not clean.empty:
        latest = float(clean.iloc[-1])

    count = int(len(clean))
    result: dict[str, Any] = {
        "count": count,
        "sample_status": "insufficient_history",
        "data_quality_note": "資料不足 / 僅能觀察：歷史樣本未達 60 筆，不能輸出分位結論。",
        "high_252d": "",
        "low_252d": "",
        "percentile_252d": "",
        "high_504d": "",
        "low_504d": "",
        "percentile_504d": "",
        "zscore_252d": "",
    }
    if latest is None or count < 60:
        return result

    window_252 = clean.tail(min(252, count))
    result["sample_status"] = "short_history" if count < 252 else "ready_252d"
    result["data_quality_note"] = (
        "short_history：可輸出短樣本分位，但未達 252 個交易日完整歷史。"
        if count < 252
        else "ready_252d"
    )
    result["high_252d"] = float(window_252.max())
    result["low_252d"] = float(window_252.min())
    result["percentile_252d"] = _pct_rank(window_252, latest)
    std = float(window_252.std(ddof=0))
    result["zscore_252d"] = (latest - float(window_252.mean())) / std if std else ""

    if count >= 504:
        window_504 = clean.tail(504)
        result["sample_status"] = "ready_504d"
        result["data_quality_note"] = "ready_504d"
        result["high_504d"] = float(window_504.max())
        result["low_504d"] = float(window_504.min())
        result["percentile_504d"] = _pct_rank(window_504, latest)
    return result

def _vix_labels(stats: dict[str, Any]) -> tuple[str, str]:
    pct = _num(stats.get("percentile_252d"))
    if pct is None:
        return "insufficient_history", "insufficient_history"
    if pct >= 90:
        return "top_decile", "extreme_fear_or_hedging"
    if pct >= 75:
        return "upper_quartile", "elevated_hedging"
    if pct <= 25:
        return "lower_quartile", "complacency_low_vol"
    return "middle_range", "normal_range"


def _retail_labels(stats: dict[str, Any]) -> tuple[str, str]:
    pct = _num(stats.get("percentile_252d"))
    if pct is None:
        return "insufficient_history", "insufficient_history"
    if pct >= 90:
        return "top_decile", "retail_extreme_long"
    if pct >= 75:
        return "upper_quartile", "retail_long_elevated"
    if pct <= 10:
        return "bottom_decile", "retail_extreme_short"
    if pct <= 25:
        return "lower_quartile", "retail_short_elevated"
    return "middle_range", "retail_normal_range"


def _is_bull(regime: str) -> bool:
    return regime in {"strong_bull", "mild_bull"}


def _near_high(row: dict[str, Any]) -> bool:
    keys = [
        "twse_distance_to_60d_high",
        "twse_distance_to_252d_high",
        "tpex_distance_to_60d_high",
        "tpex_distance_to_252d_high",
    ]
    return any((value := _num(row.get(key))) is not None and value >= -3 for key in keys)


def _near_low_or_off_high(row: dict[str, Any]) -> bool:
    low_keys = [
        "twse_distance_to_60d_low",
        "twse_distance_to_252d_low",
        "tpex_distance_to_60d_low",
        "tpex_distance_to_252d_low",
    ]
    high_keys = [
        "twse_distance_to_60d_high",
        "twse_distance_to_252d_high",
        "tpex_distance_to_60d_high",
        "tpex_distance_to_252d_high",
    ]
    near_low = any((value := _num(row.get(key))) is not None and value <= 5 for key in low_keys)
    off_high = any((value := _num(row.get(key))) is not None and value <= -8 for key in high_keys)
    return near_low or off_high


def _index_above_ma(row: dict[str, Any]) -> bool:
    return any(
        _bool(row.get(key))
        for key in ["twse_above_ma20", "twse_above_ma60", "tpex_above_ma20", "tpex_above_ma60"]
    )


def _vix_interpretation(row: dict[str, Any]) -> str:
    if row.get("vix_context_label") == "insufficient_history":
        return "insufficient_history_observe_only"
    pct = _num(row.get("taiwan_vix_252d_percentile"))
    regime = safe_str(row.get("market_regime"))
    if pct is None:
        return "insufficient_history_observe_only"
    if pct >= 75 and _is_bull(regime) and _index_above_ma(row) and _near_high(row):
        return "index_strong_but_hedging_elevated"
    if pct >= 75 and regime in {"correction", "high_risk"} and _near_low_or_off_high(row):
        return "possible_panic_contrarian_signal"
    if pct <= 25 and _is_bull(regime) and _near_high(row):
        return "low_vol_complacency_at_high"
    if row.get("vix_context_label") == "normal_range" and _is_bull(regime):
        return "trend_supported_no_extreme_vix"
    return "vix_context_neutral_observe"


def _retail_interpretation(row: dict[str, Any]) -> str:
    if row.get("retail_mtx_context_label") == "insufficient_history":
        return "insufficient_history_observe_only"
    pct = _num(row.get("retail_mtx_proxy_252d_percentile"))
    regime = safe_str(row.get("market_regime"))
    if pct is None:
        return "insufficient_history_observe_only"
    if pct >= 90 and _is_bull(regime) and _near_high(row) and _index_above_ma(row):
        return "retail_overlong_chase_risk"
    if pct >= 75 and _is_bull(regime) and _near_high(row):
        return "retail_long_elevated_but_trend_intact"
    if pct <= 10 and regime in {"correction", "high_risk"} and _near_low_or_off_high(row):
        return "retail_extreme_short_possible_rebound_watch"
    if row.get("retail_mtx_context_label") == "retail_normal_range":
        return "retail_positioning_normal"
    return "retail_positioning_observe"


def _combined_interpretation(row: dict[str, Any]) -> tuple[str, str]:
    vix_interp = safe_str(row.get("vix_index_interpretation"))
    retail_interp = safe_str(row.get("retail_mtx_index_interpretation"))
    regime = safe_str(row.get("market_regime"))
    vix_pct = _num(row.get("taiwan_vix_252d_percentile"))
    retail_pct = _num(row.get("retail_mtx_proxy_252d_percentile"))

    if "insufficient_history" in vix_interp or "insufficient_history" in retail_interp:
        return "insufficient_history_observe_only", "insufficient"
    if (
        vix_interp == "index_strong_but_hedging_elevated"
        and retail_interp in {"retail_overlong_chase_risk", "retail_long_elevated_but_trend_intact"}
    ):
        combined = "index_strong_but_sentiment_crowded_and_hedged"
    elif vix_interp == "possible_panic_contrarian_signal" or retail_interp == "retail_extreme_short_possible_rebound_watch":
        combined = "possible_contrarian_rebound_watch"
    elif vix_interp == "trend_supported_no_extreme_vix" and retail_interp == "retail_positioning_normal" and _is_bull(regime):
        combined = "trend_supported_sentiment_not_extreme"
    else:
        combined = "sentiment_mixed_observe"

    if (vix_pct is not None and vix_pct >= 90 and _near_high(row)) or (
        retail_pct is not None and retail_pct >= 90 and _near_high(row)
    ):
        level = "high"
    elif (vix_pct is not None and vix_pct >= 75) or (retail_pct is not None and retail_pct >= 75):
        level = "medium"
    else:
        level = "low"
    return combined, level



def _latest_row(df: pd.DataFrame, date_col: str = "date") -> pd.Series:
    if df.empty or date_col not in df.columns:
        return pd.Series(dtype=object)
    work = df.copy()
    work[date_col] = work[date_col].map(normalize_date)
    work = work[work[date_col].astype(str).str.len().eq(8)]
    if work.empty:
        return pd.Series(dtype=object)
    return work.sort_values(date_col).iloc[-1]


def _latest_row_at_or_before(df: pd.DataFrame, target_date: str, date_col: str = "date") -> pd.Series:
    if df.empty or date_col not in df.columns:
        return pd.Series(dtype=object)
    work = df.copy()
    work[date_col] = work[date_col].map(normalize_date)
    work = work[work[date_col].astype(str).str.len().eq(8)]
    if target_date:
        work = work[work[date_col] <= target_date]
    if work.empty:
        return pd.Series(dtype=object)
    return work.sort_values(date_col).iloc[-1]

def _load_vix_history(latest: pd.Series) -> pd.DataFrame:
    raw = read_csv(TAIWAN_VIX_HISTORY, dtype=str)
    if raw.empty:
        raw = pd.DataFrame(columns=["date", "taiwan_vix", "vix_return_5d", "vix_return_10d", "vix_return_20d"])
    for col in ["date", "taiwan_vix", "vix_return_5d", "vix_return_10d", "vix_return_20d"]:
        if col not in raw.columns:
            raw[col] = ""
    raw = raw[["date", "taiwan_vix", "vix_return_5d", "vix_return_10d", "vix_return_20d"]].copy()
    raw["date"] = raw["date"].map(normalize_date)

    latest_date = normalize_date(latest.get("date", ""))
    if latest_date:
        latest_row = {
            "date": latest_date,
            "taiwan_vix": latest.get("taiwan_vix", ""),
            "vix_return_5d": latest.get("vix_return_5d", ""),
            "vix_return_10d": latest.get("vix_return_10d", ""),
            "vix_return_20d": latest.get("vix_return_20d", ""),
        }
        raw = pd.concat([raw, pd.DataFrame([latest_row])], ignore_index=True, sort=False)

    raw = raw[raw["date"].astype(str).str.len().eq(8)]
    raw = raw.drop_duplicates(subset=["date"], keep="last").sort_values("date").reset_index(drop=True)
    write_csv(raw, VIX_HISTORY_OUT)
    return raw


def _load_put_call_history() -> pd.DataFrame:
    raw = read_csv(PUT_CALL_RATIO_HISTORY, dtype=str)
    if raw.empty or "日期" not in raw.columns:
        return pd.DataFrame(columns=["date", "put_call_oi_ratio_pct"])
    result = pd.DataFrame(
        {
            "date": raw["日期"].map(normalize_date),
            "put_volume": raw.get("賣權成交量", ""),
            "call_volume": raw.get("買權成交量", ""),
            "put_call_volume_ratio_pct": raw.get("買賣權成交量比率%", ""),
            "put_oi": raw.get("賣權未平倉量", ""),
            "call_oi": raw.get("買權未平倉量", ""),
            "put_call_oi_ratio_pct": raw.get("買賣權未平倉量比率%", ""),
        }
    )
    return result[result["date"].astype(str).str.len().eq(8)]


def _taifex_net_oi(df: pd.DataFrame, date: str, product: str | None, identity: str) -> Any:
    if df.empty:
        return ""
    work = df[df["date"].eq(date)]
    if product:
        work = work[work["商品名稱"].eq(product)]
    work = work[work["身份別"].eq(identity)]
    if work.empty:
        return ""
    values = pd.to_numeric(work["多空未平倉口數淨額"], errors="coerce").dropna()
    if values.empty:
        return ""
    return float(values.sum())


def _load_retail_mtx_history(latest: pd.Series) -> pd.DataFrame:
    raw = read_csv(TAIFEX_FUTURES_CONTRACTS_HISTORY, dtype=str)
    if raw.empty:
        result = pd.DataFrame(columns=["date", "foreign_mtx_futures_net_oi", "three_institution_mtx_net_oi", "retail_mtx_net_oi_proxy", "retail_mtx_proxy_method"])
        write_csv(result, RETAIL_MTX_HISTORY_OUT)
        return result

    required = ["日期", "商品名稱", "身份別", "多空未平倉口數淨額"]
    if any(col not in raw.columns for col in required):
        result = pd.DataFrame(columns=["date", "foreign_mtx_futures_net_oi", "three_institution_mtx_net_oi", "retail_mtx_net_oi_proxy", "retail_mtx_proxy_method"])
        write_csv(result, RETAIL_MTX_HISTORY_OUT)
        return result

    work = raw[required].copy()
    work["date"] = work["日期"].map(normalize_date)
    rows: list[dict[str, Any]] = []
    for date in sorted(x for x in work["date"].dropna().unique() if len(str(x)) == 8):
        foreign_mtx = _taifex_net_oi(work, date, "小型臺指期貨", "外資及陸資")
        dealer_mtx = _taifex_net_oi(work, date, "小型臺指期貨", "自營商")
        trust_mtx = _taifex_net_oi(work, date, "小型臺指期貨", "投信")
        three_values = [_num(foreign_mtx), _num(dealer_mtx), _num(trust_mtx)]
        three_sum = sum(v for v in three_values if v is not None)
        retail_proxy = -three_sum if any(v is not None for v in three_values) else ""
        rows.append(
            {
                "date": date,
                "foreign_mtx_futures_net_oi": foreign_mtx,
                "three_institution_mtx_net_oi": three_sum if any(v is not None for v in three_values) else "",
                "retail_mtx_net_oi_proxy": retail_proxy,
                "retail_mtx_proxy_method": "negative_sum_of_three_institution_mtx_net_oi",
            }
        )

    result = pd.DataFrame(rows)
    latest_date = normalize_date(latest.get("date", ""))
    if latest_date:
        latest_row = {
            "date": latest_date,
            "foreign_mtx_futures_net_oi": latest.get("foreign_mtx_futures_net_oi", ""),
            "three_institution_mtx_net_oi": latest.get("three_institution_mtx_net_oi", ""),
            "retail_mtx_net_oi_proxy": latest.get("retail_mtx_net_oi_proxy", ""),
            "retail_mtx_proxy_method": latest.get("retail_mtx_proxy_method", ""),
        }
        result = pd.concat([result, pd.DataFrame([latest_row])], ignore_index=True, sort=False)

    result = result.drop_duplicates(subset=["date"], keep="last").sort_values("date").reset_index(drop=True)
    write_csv(result, RETAIL_MTX_HISTORY_OUT)
    return result


def _load_futures_options_history(latest: pd.Series, vix_history: pd.DataFrame, retail_history: pd.DataFrame) -> pd.DataFrame:
    put_call = _load_put_call_history()
    base_dates = set(vix_history.get("date", pd.Series(dtype=str)).astype(str))
    base_dates.update(retail_history.get("date", pd.Series(dtype=str)).astype(str))
    base_dates.update(put_call.get("date", pd.Series(dtype=str)).astype(str))
    latest_date = normalize_date(latest.get("date", ""))
    if latest_date:
        base_dates.add(latest_date)

    rows: list[dict[str, Any]] = []
    for date in sorted(d for d in base_dates if len(str(d)) == 8):
        row: dict[str, Any] = {"date": date}
        retail_row = _latest_row(retail_history[retail_history["date"].eq(date)]) if not retail_history.empty else pd.Series(dtype=object)
        vix_row = _latest_row(vix_history[vix_history["date"].eq(date)]) if not vix_history.empty else pd.Series(dtype=object)
        pc_row = _latest_row(put_call[put_call["date"].eq(date)]) if not put_call.empty else pd.Series(dtype=object)
        if latest_date == date:
            source = latest
        else:
            source = pd.Series(dtype=object)

        for col in [
            "foreign_futures_net_oi",
            "foreign_tx_futures_net_oi",
            "dealer_tx_futures_net_oi",
            "trust_tx_futures_net_oi",
            "foreign_txo_call_net_oi",
            "foreign_txo_put_net_oi",
            "foreign_txo_synthetic_net_oi",
        ]:
            row[col] = source.get(col, "")

        row["foreign_mtx_futures_net_oi"] = source.get("foreign_mtx_futures_net_oi", retail_row.get("foreign_mtx_futures_net_oi", ""))
        row["three_institution_mtx_net_oi"] = source.get("three_institution_mtx_net_oi", retail_row.get("three_institution_mtx_net_oi", ""))
        row["retail_mtx_net_oi_proxy"] = source.get("retail_mtx_net_oi_proxy", retail_row.get("retail_mtx_net_oi_proxy", ""))
        row["retail_mtx_proxy_method"] = source.get("retail_mtx_proxy_method", retail_row.get("retail_mtx_proxy_method", ""))
        row["put_call_oi_ratio_pct"] = source.get("put_call_oi_ratio_pct", pc_row.get("put_call_oi_ratio_pct", ""))
        row["taiwan_vix"] = source.get("taiwan_vix", vix_row.get("taiwan_vix", ""))
        row["vix_return_5d"] = source.get("vix_return_5d", vix_row.get("vix_return_5d", ""))
        row["vix_return_10d"] = source.get("vix_return_10d", vix_row.get("vix_return_10d", ""))
        row["vix_return_20d"] = source.get("vix_return_20d", vix_row.get("vix_return_20d", ""))
        rows.append(row)

    result = pd.DataFrame(rows)
    write_csv(result, FUTURES_OPTIONS_HISTORY_OUT)
    return result


def _rolling_high_low(df: pd.DataFrame, date: str, index_code: str, window: int) -> tuple[Any, Any]:
    work = df[df["index_code"].eq(index_code)].copy()
    work["date"] = work["date"].map(normalize_date)
    work = work[work["date"].le(date)].sort_values("date").tail(window)
    if work.empty:
        return "", ""
    close = pd.to_numeric(work["close"], errors="coerce").dropna()
    if close.empty:
        return "", ""
    return float(close.max()), float(close.min())


def _distance_to_level(close: Any, level: Any) -> Any:
    close_num = _num(close)
    level_num = _num(level)
    if close_num is None or level_num is None or level_num == 0:
        return ""
    return (close_num / level_num - 1) * 100


def _index_context(date: str, market_regime_row: pd.Series) -> dict[str, Any]:
    raw = read_csv(MARKET_INDEX_HISTORY, dtype=str)
    result: dict[str, Any] = {}
    for prefix, code in [("twse", "TWSE"), ("tpex", "TPEX")]:
        latest = pd.Series(dtype=object)
        if not raw.empty:
            work = raw[raw.get("index_code", "").eq(code)].copy()
            if not work.empty:
                work["date"] = work["date"].map(normalize_date)
                work = work[work["date"].le(date)].sort_values("date")
                if not work.empty:
                    latest = work.iloc[-1]
        close = latest.get("close", market_regime_row.get(f"{prefix}_close", ""))
        result[f"{prefix}_close"] = _round(close, 4)
        result[f"{prefix}_above_ma20"] = safe_str(latest.get("above_ma20", market_regime_row.get(f"{prefix}_above_ma20", "")))
        result[f"{prefix}_above_ma60"] = safe_str(latest.get("above_ma60", market_regime_row.get(f"{prefix}_above_ma60", "")))
        for window in [20, 60, 252]:
            high, low = _rolling_high_low(raw, date, code, window)
            result[f"{prefix}_distance_to_{window}d_high"] = _round(_distance_to_level(close, high), 4)
            result[f"{prefix}_distance_to_{window}d_low"] = _round(_distance_to_level(close, low), 4)
    return result



def _context_row() -> tuple[dict[str, Any], pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    futures = read_csv(FUTURES_OPTIONS_LATEST, dtype=str)
    market_regime = read_csv(MARKET_REGIME_LATEST, dtype=str)
    target_date = normalize_date(main_price_date_from_freshness())
    latest_futures = _latest_row_at_or_before(futures, target_date)
    latest_regime = _latest_row_at_or_before(market_regime, target_date)
    date = target_date or normalize_date(latest_futures.get("date", "")) or normalize_date(latest_regime.get("date", ""))
    if not date:
        raise RuntimeError("Cannot build market sentiment context: main price date and futures/options date are missing.")
    if latest_futures.empty:
        raise RuntimeError(f"Cannot build market sentiment context: no futures/options row at or before main_price_date={date}.")
    if latest_regime.empty:
        raise RuntimeError(f"Cannot build market sentiment context: no market regime row at or before main_price_date={date}.")

    latest_futures = latest_futures.copy()
    latest_futures["date"] = date
    latest_regime = latest_regime.copy()
    latest_regime["date"] = date

    vix_history = _load_vix_history(latest_futures)
    retail_history = _load_retail_mtx_history(latest_futures)
    futures_history = _load_futures_options_history(latest_futures, vix_history, retail_history)

    vix_series = vix_history["taiwan_vix"] if "taiwan_vix" in vix_history.columns else pd.Series(dtype=float)
    retail_series = (
        retail_history["retail_mtx_net_oi_proxy"]
        if "retail_mtx_net_oi_proxy" in retail_history.columns
        else pd.Series(dtype=float)
    )
    vix_stats = _window_stats(vix_series, latest_futures.get("taiwan_vix", ""))
    retail_stats = _window_stats(retail_series, latest_futures.get("retail_mtx_net_oi_proxy", ""))
    vix_rank, vix_label = _vix_labels(vix_stats)
    retail_rank, retail_label = _retail_labels(retail_stats)

    row: dict[str, Any] = {
        "date": date,
        "taiwan_vix": _round(latest_futures.get("taiwan_vix", ""), 4),
        "taiwan_vix_252d_high": _round(vix_stats.get("high_252d"), 4),
        "taiwan_vix_252d_low": _round(vix_stats.get("low_252d"), 4),
        "taiwan_vix_252d_percentile": _round(vix_stats.get("percentile_252d"), 4),
        "taiwan_vix_504d_high": _round(vix_stats.get("high_504d"), 4),
        "taiwan_vix_504d_low": _round(vix_stats.get("low_504d"), 4),
        "taiwan_vix_504d_percentile": _round(vix_stats.get("percentile_504d"), 4),
        "taiwan_vix_zscore_252d": _round(vix_stats.get("zscore_252d"), 4),
        "taiwan_vix_rank_label": vix_rank,
        "vix_context_label": vix_label,
        "vix_return_5d": _round(latest_futures.get("vix_return_5d", ""), 4),
        "vix_return_10d": _round(latest_futures.get("vix_return_10d", ""), 4),
        "vix_return_20d": _round(latest_futures.get("vix_return_20d", ""), 4),
        "retail_mtx_net_oi_proxy": _round(latest_futures.get("retail_mtx_net_oi_proxy", ""), 4),
        "retail_mtx_proxy_method": safe_str(latest_futures.get("retail_mtx_proxy_method", "")),
        "retail_mtx_proxy_252d_high": _round(retail_stats.get("high_252d"), 4),
        "retail_mtx_proxy_252d_low": _round(retail_stats.get("low_252d"), 4),
        "retail_mtx_proxy_252d_percentile": _round(retail_stats.get("percentile_252d"), 4),
        "retail_mtx_proxy_504d_high": _round(retail_stats.get("high_504d"), 4),
        "retail_mtx_proxy_504d_low": _round(retail_stats.get("low_504d"), 4),
        "retail_mtx_proxy_504d_percentile": _round(retail_stats.get("percentile_504d"), 4),
        "retail_mtx_proxy_zscore_252d": _round(retail_stats.get("zscore_252d"), 4),
        "retail_mtx_rank_label": retail_rank,
        "retail_mtx_context_label": retail_label,
        "foreign_tx_futures_net_oi": _round(latest_futures.get("foreign_tx_futures_net_oi", ""), 4),
        "dealer_tx_futures_net_oi": _round(latest_futures.get("dealer_tx_futures_net_oi", ""), 4),
        "trust_tx_futures_net_oi": _round(latest_futures.get("trust_tx_futures_net_oi", ""), 4),
        "foreign_futures_net_oi": _round(latest_futures.get("foreign_futures_net_oi", ""), 4),
        "put_call_oi_ratio_pct": _round(latest_futures.get("put_call_oi_ratio_pct", ""), 4),
        "foreign_txo_call_net_oi": _round(latest_futures.get("foreign_txo_call_net_oi", ""), 4),
        "foreign_txo_put_net_oi": _round(latest_futures.get("foreign_txo_put_net_oi", ""), 4),
        "foreign_txo_synthetic_net_oi": _round(latest_futures.get("foreign_txo_synthetic_net_oi", ""), 4),
        "market_regime": safe_str(latest_regime.get("market_regime", "")),
        "risk_level": safe_str(latest_regime.get("risk_level", "")),
    }
    row.update(_index_context(date, latest_regime))

    row["vix_index_interpretation"] = _vix_interpretation(row)
    row["retail_mtx_index_interpretation"] = _retail_interpretation(row)
    combined, level = _combined_interpretation(row)
    row["combined_sentiment_interpretation"] = combined
    row["sentiment_warning_level"] = level

    statuses = {vix_stats["sample_status"], retail_stats["sample_status"]}
    if "insufficient_history" in statuses:
        row["sample_status"] = "insufficient_history"
        row["data_quality_note"] = "資料不足 / 僅能觀察：VIX 或散戶小台歷史樣本未達 60 筆，不能判斷是否達歷史極端。"
    elif "short_history" in statuses:
        row["sample_status"] = "short_history"
        row["data_quality_note"] = "short_history：可提供短樣本分位，但未達 252 日完整歷史。"
    else:
        row["sample_status"] = "ready"
        row["data_quality_note"] = "ready"

    for col in REQUIRED_CONTEXT_COLUMNS:
        row.setdefault(col, "")

    return row, vix_history, retail_history, futures_history

def _fmt(value: Any, suffix: str = "") -> str:
    num = _num(value)
    if num is None:
        return "-"
    if abs(num) >= 1000:
        text = f"{num:,.0f}"
    else:
        text = f"{num:.2f}".rstrip("0").rstrip(".")
    return f"{text}{suffix}"



def _markdown(row: dict[str, Any]) -> str:
    lines = [
        "# Market Sentiment Context",
        "",
        f"- generated_at: `{now_text()}`",
        f"- date: `{row.get('date')}`",
        f"- sample_status: `{row.get('sample_status')}`",
        f"- data_quality_note: {row.get('data_quality_note')}",
        "",
        "## VIX Historical Context",
        "",
        f"- Taiwan VIX latest: `{_fmt(row.get('taiwan_vix'))}`",
        f"- 252D high / low: `{_fmt(row.get('taiwan_vix_252d_high'))}` / `{_fmt(row.get('taiwan_vix_252d_low'))}`",
        f"- 252D percentile: `{_fmt(row.get('taiwan_vix_252d_percentile'), '%')}`",
        f"- 504D percentile: `{_fmt(row.get('taiwan_vix_504d_percentile'), '%')}`",
        f"- z-score 252D: `{_fmt(row.get('taiwan_vix_zscore_252d'))}`",
        f"- vix_return_5d / 10d / 20d: `{_fmt(row.get('vix_return_5d'), '%')}` / `{_fmt(row.get('vix_return_10d'), '%')}` / `{_fmt(row.get('vix_return_20d'), '%')}`",
        f"- vix_context_label: `{row.get('vix_context_label')}`",
        f"- vix_index_interpretation: `{row.get('vix_index_interpretation')}`",
        "",
        "VIX interpretation: VIX must be read with TWSE / TPEx position, market_regime, Put/Call, and foreign TX futures net OI. It is not a standalone buy/sell signal.",
        "",
        "## Retail MTX Historical Context",
        "",
        f"- retail_mtx_net_oi_proxy latest: `{_fmt(row.get('retail_mtx_net_oi_proxy'))}`",
        f"- proxy method: `{row.get('retail_mtx_proxy_method')}`",
        f"- 252D high / low: `{_fmt(row.get('retail_mtx_proxy_252d_high'))}` / `{_fmt(row.get('retail_mtx_proxy_252d_low'))}`",
        f"- 252D percentile: `{_fmt(row.get('retail_mtx_proxy_252d_percentile'), '%')}`",
        f"- 504D percentile: `{_fmt(row.get('retail_mtx_proxy_504d_percentile'), '%')}`",
        f"- retail_mtx_context_label: `{row.get('retail_mtx_context_label')}`",
        f"- retail_mtx_index_interpretation: `{row.get('retail_mtx_index_interpretation')}`",
        "",
        "Retail MTX interpretation: retail positioning is a contrarian sentiment proxy only. It must be confirmed by index price position and breadth.",
        "",
        "## Index Position Inputs",
        "",
        "| index | close | dist 20D high | dist 60D high | dist 252D high | above MA20 | above MA60 |",
        "| --- | ---: | ---: | ---: | ---: | --- | --- |",
        f"| TWSE | {_fmt(row.get('twse_close'))} | {_fmt(row.get('twse_distance_to_20d_high'), '%')} | {_fmt(row.get('twse_distance_to_60d_high'), '%')} | {_fmt(row.get('twse_distance_to_252d_high'), '%')} | {row.get('twse_above_ma20')} | {row.get('twse_above_ma60')} |",
        f"| TPEx | {_fmt(row.get('tpex_close'))} | {_fmt(row.get('tpex_distance_to_20d_high'), '%')} | {_fmt(row.get('tpex_distance_to_60d_high'), '%')} | {_fmt(row.get('tpex_distance_to_252d_high'), '%')} | {row.get('tpex_above_ma20')} | {row.get('tpex_above_ma60')} |",
        "",
        "## Combined Sentiment Interpretation",
        "",
        f"- combined_sentiment_interpretation: `{row.get('combined_sentiment_interpretation')}`",
        f"- sentiment_warning_level: `{row.get('sentiment_warning_level')}`",
        f"- foreign_tx_futures_net_oi: `{_fmt(row.get('foreign_tx_futures_net_oi'))}`",
        f"- foreign_futures_net_oi: `{_fmt(row.get('foreign_futures_net_oi'))}` (whole futures exposure background only, not TX direction)",
        f"- put_call_oi_ratio_pct: `{_fmt(row.get('put_call_oi_ratio_pct'), '%')}`",
        "",
    ]
    if row.get("sample_status") == "insufficient_history":
        lines.append("資料不足 / 僅能觀察：目前 VIX / 散戶小台缺少足夠歷史分位資料，不可作為反指標結論。")
        lines.append("")
    lines.extend(
        [
            "## Usage Boundary",
            "",
            "- VIX, Put/Call, and retail MTX proxy cannot be used as standalone trading signals.",
            "- foreign_tx_futures_net_oi is the TX futures direction anchor; foreign_futures_net_oi is only broad futures exposure background.",
            "- Use this context as market-risk background for daily reports and opening-prep analysis.",
        ]
    )
    return "\n".join(lines) + "\n"

def _update_marked_section(path: Path, section: str) -> None:
    existing = path.read_text(encoding="utf-8") if path.exists() else ""
    block = f"{CONTEXT_START}\n{section.rstrip()}\n{CONTEXT_END}"
    if CONTEXT_START in existing and CONTEXT_END in existing:
        pattern = re.compile(re.escape(CONTEXT_START) + r".*?" + re.escape(CONTEXT_END), flags=re.S)
        updated = pattern.sub(block, existing)
    else:
        updated = existing.rstrip() + "\n\n" + block + "\n"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(updated, encoding="utf-8")


def _dashboard_section(row: dict[str, Any]) -> str:
    return "\n".join(
        [
            "## VIX Historical Context",
            "",
            f"- Taiwan VIX latest: `{_fmt(row.get('taiwan_vix'))}`",
            f"- 252D high / low / percentile: `{_fmt(row.get('taiwan_vix_252d_high'))}` / `{_fmt(row.get('taiwan_vix_252d_low'))}` / `{_fmt(row.get('taiwan_vix_252d_percentile'), '%')}`",
            f"- 504D percentile: `{_fmt(row.get('taiwan_vix_504d_percentile'), '%')}`",
            f"- z-score: `{_fmt(row.get('taiwan_vix_zscore_252d'))}`",
            f"- vix_return_5d / 10d / 20d: `{_fmt(row.get('vix_return_5d'), '%')}` / `{_fmt(row.get('vix_return_10d'), '%')}` / `{_fmt(row.get('vix_return_20d'), '%')}`",
            f"- TWSE / TPEx position: TWSE dist 60D high `{_fmt(row.get('twse_distance_to_60d_high'), '%')}`, TPEx dist 60D high `{_fmt(row.get('tpex_distance_to_60d_high'), '%')}`",
            f"- vix_index_interpretation: `{row.get('vix_index_interpretation')}`",
            "",
            "## Retail MTX Historical Context",
            "",
            f"- retail_mtx_net_oi_proxy latest: `{_fmt(row.get('retail_mtx_net_oi_proxy'))}`",
            f"- proxy method: `{row.get('retail_mtx_proxy_method')}`",
            f"- 252D high / low / percentile: `{_fmt(row.get('retail_mtx_proxy_252d_high'))}` / `{_fmt(row.get('retail_mtx_proxy_252d_low'))}` / `{_fmt(row.get('retail_mtx_proxy_252d_percentile'), '%')}`",
            f"- 504D percentile: `{_fmt(row.get('retail_mtx_proxy_504d_percentile'), '%')}`",
            f"- retail_mtx_index_interpretation: `{row.get('retail_mtx_index_interpretation')}`",
            "",
            "## Combined Sentiment Interpretation",
            "",
            f"- combined_sentiment_interpretation: `{row.get('combined_sentiment_interpretation')}`",
            f"- sentiment_warning_level: `{row.get('sentiment_warning_level')}`",
            f"- data_quality_note: {row.get('data_quality_note')}",
            "",
            "Operation meaning: use sentiment context only with TWSE / TPEx technical position, market_regime, Put/Call, and foreign TX futures net OI. Do not use VIX or retail MTX as standalone buy/sell signals.",
        ]
    )


def _packet_section(row: dict[str, Any]) -> str:
    return "\n".join(
        [
            "## MARKET_SENTIMENT_CONTEXT",
            "",
            "market_sentiment_context:",
            "  taiwan_vix:",
            f"    latest: {row.get('taiwan_vix')}",
            f"    percentile_252d: {row.get('taiwan_vix_252d_percentile')}",
            f"    percentile_504d: {row.get('taiwan_vix_504d_percentile')}",
            f"    rank_label: {row.get('taiwan_vix_rank_label')}",
            f"    context_label: {row.get('vix_context_label')}",
            f"    index_interpretation: {row.get('vix_index_interpretation')}",
            "  retail_mtx:",
            f"    latest_proxy: {row.get('retail_mtx_net_oi_proxy')}",
            f"    proxy_method: {row.get('retail_mtx_proxy_method')}",
            f"    percentile_252d: {row.get('retail_mtx_proxy_252d_percentile')}",
            f"    percentile_504d: {row.get('retail_mtx_proxy_504d_percentile')}",
            f"    rank_label: {row.get('retail_mtx_rank_label')}",
            f"    context_label: {row.get('retail_mtx_context_label')}",
            f"    index_interpretation: {row.get('retail_mtx_index_interpretation')}",
            "  combined:",
            f"    combined_sentiment_interpretation: {row.get('combined_sentiment_interpretation')}",
            f"    sentiment_warning_level: {row.get('sentiment_warning_level')}",
            f"    sample_status: {row.get('sample_status')}",
            f"    data_quality_note: {row.get('data_quality_note')}",
            "",
            "ChatGPT-friendly summary:",
            f"- VIX context: {row.get('vix_context_label')} / {row.get('vix_index_interpretation')}",
            f"- Retail MTX context: {row.get('retail_mtx_context_label')} / {row.get('retail_mtx_index_interpretation')}",
            f"- Combined: {row.get('combined_sentiment_interpretation')} (warning={row.get('sentiment_warning_level')})",
            "- VIX / PutCall / retail MTX are auxiliary context only; cross-check market_regime and foreign_tx_futures_net_oi.",
        ]
    )


def build() -> pd.DataFrame:
    row, _, _, _ = _context_row()
    df = pd.DataFrame([{col: row.get(col, "") for col in REQUIRED_CONTEXT_COLUMNS}])
    write_csv(df, MARKET_SENTIMENT_CONTEXT_CSV)
    write_csv(df, DOCS_MARKET_SENTIMENT_CONTEXT_CSV)
    append_update_csv(df, MARKET_SENTIMENT_CONTEXT_HISTORY, key_cols=["date"], sort_cols=["date"])

    md = _markdown(row)
    MARKET_SENTIMENT_CONTEXT_MD.parent.mkdir(parents=True, exist_ok=True)
    MARKET_SENTIMENT_CONTEXT_MD.write_text(md, encoding="utf-8")
    DOCS_MARKET_SENTIMENT_CONTEXT_MD.parent.mkdir(parents=True, exist_ok=True)
    DOCS_MARKET_SENTIMENT_CONTEXT_MD.write_text(md, encoding="utf-8")

    _update_marked_section(MARKET_RISK_DASHBOARD_MD, _dashboard_section(row))
    _update_marked_section(MARKET_TIMING_PACKET_MD, _packet_section(row))

    print(f"Saved: {MARKET_SENTIMENT_CONTEXT_CSV}")
    print(f"Saved: {MARKET_SENTIMENT_CONTEXT_MD}")
    print(f"Updated: {MARKET_RISK_DASHBOARD_MD}")
    print(f"Updated: {MARKET_TIMING_PACKET_MD}")
    return df


def main() -> None:
    build()


if __name__ == "__main__":
    main()
