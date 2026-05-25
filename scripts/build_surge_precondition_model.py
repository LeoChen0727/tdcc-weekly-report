from __future__ import annotations

import math
from pathlib import Path
from typing import Any

import pandas as pd

from tracking_utils import (
    LATEST_DIR,
    STOCK_PRICE_HISTORY_DIR,
    normalize_code,
    normalize_date,
    now_text,
    raw_url,
    read_csv,
    safe_str,
    to_number,
    write_csv,
)


HISTORY_DIR = Path("output/history/surge_model")

FEATURE_PANEL_CSV = HISTORY_DIR / "daily_stock_feature_panel.csv"
LABELS_CSV = HISTORY_DIR / "surge_event_labels.csv"
EVENT_STUDY_CSV = HISTORY_DIR / "pre_surge_event_study.csv"
CONTROL_SAMPLE_CSV = HISTORY_DIR / "non_surge_control_sample.csv"

FEATURE_IMPORTANCE_CSV = LATEST_DIR / "surge_model_feature_importance_latest.csv"
FEATURE_IMPORTANCE_MD = LATEST_DIR / "surge_model_feature_importance_latest.md"
SCORE_CSV = LATEST_DIR / "surge_model_score_latest.csv"
SCORE_MD = LATEST_DIR / "surge_model_score_latest.md"
CANDIDATES_CSV = LATEST_DIR / "surge_precondition_candidates_latest.csv"
CANDIDATES_MD = LATEST_DIR / "surge_precondition_candidates_latest.md"
BACKTEST_CSV = LATEST_DIR / "surge_model_backtest_latest.csv"
BACKTEST_MD = LATEST_DIR / "surge_model_backtest_latest.md"
PACKET_MD = LATEST_DIR / "surge_model_chatgpt_packet_latest.md"

MARKET_INDEX_CSV = Path("data/market_index_history.csv")
STOCK_THEME_MAP_CSV = Path("config/stock_theme_map.csv")
DAILY_CANDIDATE_LOG_CSV = Path("output/history/daily_candidates/daily_candidate_signal_log.csv")
ALL_CANDIDATES_CSV = LATEST_DIR / "all_candidates_latest.csv"
CANDIDATE_REPEAT_CSV = LATEST_DIR / "candidate_repeat_appearance_latest.csv"
TDCC_SNAPSHOT_CSV = Path("output/history/tdcc_signals/tdcc_signal_snapshot.csv")
ABM_TOP_CSV = LATEST_DIR / "tdcc_pre_move_abm_top_latest.csv"
WARRANT_FLOW_CSV = LATEST_DIR / "warrant_flow_by_stock_latest.csv"
WARRANT_SECTOR_HEAT_CSV = LATEST_DIR / "warrant_sector_heat_latest.csv"
MARKET_REGIME_CSV = LATEST_DIR / "market_regime_latest.csv"

MAX_HISTORY_ROWS_PER_STOCK = 180
FEATURE_PANEL_EXPORT_DAYS = 20
LABEL_EXPORT_DAYS = 60
EVENT_STUDY_EXPORT_ROWS = 20_000
SURGE_EVENT_LOOKBACKS = [1, 2, 3, 5, 10]
TOP_PACKET_ROWS = 30


def pct_change(current: pd.Series, base: pd.Series) -> pd.Series:
    return (current / base - 1) * 100


def numeric(df: pd.DataFrame, column: str, default: float = math.nan) -> pd.Series:
    if column not in df.columns:
        return pd.Series(default, index=df.index, dtype="float64")
    return pd.to_numeric(df[column].astype(str).str.replace(",", "", regex=False), errors="coerce")


def as_bool_series(df: pd.DataFrame, column: str) -> pd.Series:
    if column not in df.columns:
        return pd.Series(False, index=df.index)
    return df[column].astype(str).str.lower().isin({"true", "1", "yes", "y"})


def fmt(value: Any, digits: int = 2) -> str:
    num = to_number(value)
    if math.isnan(num):
        return ""
    return f"{num:.{digits}f}"


def markdown_table(df: pd.DataFrame, max_rows: int = 30) -> str:
    if df.empty:
        return "_No rows._"
    view = df.head(max_rows).fillna("")
    cols = list(view.columns)
    lines = [
        "| " + " | ".join(cols) + " |",
        "| " + " | ".join(["---"] * len(cols)) + " |",
    ]
    for _, row in view.iterrows():
        lines.append("| " + " | ".join(str(row.get(col, "")).replace("\n", " ") for col in cols) + " |")
    return "\n".join(lines)


def load_market_index() -> pd.DataFrame:
    df = read_csv(MARKET_INDEX_CSV, dtype=str, keep_default_na=False)
    if df.empty:
        return pd.DataFrame()
    df["date"] = df["date"].map(normalize_date)
    df["index_code"] = df["index_code"].astype(str).str.upper()
    for col in ["close", "return_5d", "return_10d", "return_20d", "return_60d", "ma20", "ma60"]:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors="coerce")
    return df.dropna(subset=["date"]).sort_values(["index_code", "date"]).reset_index(drop=True)


def market_return_map(market_index: pd.DataFrame, index_code: str, horizon: int) -> dict[str, float]:
    if market_index.empty:
        return {}
    subset = market_index[market_index["index_code"].eq(index_code)].copy()
    col = f"return_{horizon}d"
    if col not in subset.columns:
        return {}
    return subset.set_index("date")[col].to_dict()


def market_close_map(market_index: pd.DataFrame, index_code: str) -> dict[str, float]:
    if market_index.empty or "close" not in market_index.columns:
        return {}
    subset = market_index[market_index["index_code"].eq(index_code)].copy()
    return subset.set_index("date")["close"].to_dict()


def add_future_labels(df: pd.DataFrame) -> pd.DataFrame:
    out = df.copy()
    close = out["close"]
    high = out["high"]
    low = out["low"]
    n = len(out)

    for horizon in [5, 10, 20]:
        future_close = close.shift(-horizon)
        future_high = high.shift(-1).iloc[::-1].rolling(horizon, min_periods=horizon).max().iloc[::-1]
        future_low = low.shift(-1).iloc[::-1].rolling(horizon, min_periods=horizon).min().iloc[::-1]
        days_to_high: list[Any] = []
        high_values = high.to_numpy()

        for i in range(n):
            if i + horizon >= n:
                days_to_high.append("")
                continue
            window = high_values[i + 1 : i + horizon + 1]
            if len(window) < horizon or pd.isna(window).all():
                days_to_high.append("")
            else:
                days_to_high.append(int(pd.Series(window).idxmax()) + 1)

        out[f"future_close_d{horizon}"] = future_close
        out[f"future_high_d{horizon}"] = future_high
        out[f"future_low_d{horizon}"] = future_low
        out[f"future_ret_{horizon}d_close"] = pct_change(pd.Series(future_close, index=out.index), close)
        out[f"future_max_ret_{horizon}d"] = pct_change(pd.Series(future_high, index=out.index), close)
        out[f"future_min_ret_{horizon}d"] = pct_change(pd.Series(future_low, index=out.index), close)
        out[f"max_drawdown_d{horizon}"] = out[f"future_min_ret_{horizon}d"]
        out[f"days_to_high_d{horizon}"] = days_to_high
        out[f"mature_{horizon}d"] = future_close.notna() & future_high.notna() & future_low.notna()

    out["surge_5d"] = out["future_max_ret_5d"] >= 20
    out["surge_10d"] = out["future_max_ret_10d"] >= 25
    out["surge_20d"] = out["future_max_ret_20d"] >= 35
    return out


def build_stock_features(path: Path, market_index: pd.DataFrame) -> pd.DataFrame:
    raw = read_csv(path, dtype=str, keep_default_na=False)
    if raw.empty or "date" not in raw.columns:
        return pd.DataFrame()

    stock_id = normalize_code(path.stem)
    raw["date"] = raw["date"].map(normalize_date)
    raw["stock_id"] = raw.get("stock_id", stock_id)
    raw["stock_id"] = raw["stock_id"].map(normalize_code)
    raw.loc[raw["stock_id"].eq(""), "stock_id"] = stock_id
    if "stock_name" not in raw.columns:
        raw["stock_name"] = ""
    if "market" not in raw.columns:
        raw["market"] = ""

    for col in ["open", "high", "low", "close", "volume", "trading_value"]:
        if col not in raw.columns:
            raw[col] = math.nan
        raw[col] = pd.to_numeric(raw[col].astype(str).str.replace(",", "", regex=False), errors="coerce")

    df = raw.dropna(subset=["date", "close"]).sort_values("date").drop_duplicates("date", keep="last")
    if len(df) < 25:
        return pd.DataFrame()
    df = df.tail(MAX_HISTORY_ROWS_PER_STOCK).reset_index(drop=True)

    out = pd.DataFrame()
    out["trade_date"] = df["date"]
    out["stock_id"] = df["stock_id"]
    out["stock_name"] = df["stock_name"]
    out["market_type"] = df["market"]
    out["theme"] = ""
    out["close"] = df["close"]
    out["open"] = df["open"]
    out["high"] = df["high"]
    out["low"] = df["low"]
    out["volume"] = df["volume"]
    out["turnover_value"] = df["trading_value"]

    close = df["close"]
    high = df["high"]
    low = df["low"]
    open_ = df["open"]
    volume = df["volume"]

    for horizon in [1, 3, 5, 10, 20, 60]:
        out[f"price_ret_{horizon}d"] = pct_change(close, close.shift(horizon))

    for window in [5, 10, 20, 60, 120]:
        ma_col = f"ma{window}"
        if ma_col in df.columns:
            ma = pd.to_numeric(df[ma_col], errors="coerce")
            ma = ma.where(ma.notna(), close.rolling(window, min_periods=max(3, min(window, 20))).mean())
        else:
            ma = close.rolling(window, min_periods=max(3, min(window, 20))).mean()
        out[ma_col] = ma
        out[f"distance_{ma_col}_pct"] = pct_change(close, ma)
        if window in [5, 10, 20, 60]:
            out[f"{ma_col}_slope"] = pct_change(ma, ma.shift(5))

    for window in [5, 10, 20]:
        vol_ma = volume.rolling(window, min_periods=max(3, window // 2)).mean()
        out[f"volume_ratio_{window}d"] = volume / vol_ma

    prev_close = close.shift(1)
    true_range = pd.concat(
        [
            (high - low).abs(),
            (high - prev_close).abs(),
            (low - prev_close).abs(),
        ],
        axis=1,
    ).max(axis=1)
    out["atr_14"] = true_range.rolling(14, min_periods=5).mean()
    out["volatility_20d"] = close.pct_change().rolling(20, min_periods=10).std() * 100

    for window in [20, 60]:
        roll_high = high.rolling(window, min_periods=max(5, min(window, 20))).max()
        roll_low = low.rolling(window, min_periods=max(5, min(window, 20))).min()
        out[f"close_position_{window}d"] = (close - roll_low) / (roll_high - roll_low).replace(0, math.nan) * 100
        out[f"distance_{window}d_high"] = pct_change(close, roll_high)
        out[f"breakout_{window}d_high"] = close > high.shift(1).rolling(window, min_periods=max(5, min(window, 20))).max()

    out["pullback_to_ma20"] = out["distance_ma20_pct"].between(-3, 3)
    out["pullback_to_ma60"] = out["distance_ma60_pct"].between(-3, 3)

    range_10 = (high.rolling(10, min_periods=5).max() / low.rolling(10, min_periods=5).min() - 1) * 100
    range_20 = (high.rolling(20, min_periods=10).max() / low.rolling(20, min_periods=10).min() - 1) * 100
    out["narrow_range_10d"] = range_10 <= 10
    out["narrow_range_20d"] = range_20 <= 15
    out["consolidation_days"] = (range_20 <= 18).rolling(20, min_periods=1).sum()

    candle_range = (high - low).replace(0, math.nan)
    out["upper_shadow_ratio"] = (high - pd.concat([open_, close], axis=1).max(axis=1)) / candle_range * 100
    out["lower_shadow_ratio"] = (pd.concat([open_, close], axis=1).min(axis=1) - low) / candle_range * 100
    out["high_volume_upper_shadow"] = (out["upper_shadow_ratio"] >= 40) & (out["volume_ratio_5d"] >= 1.5)
    out["high_volume_breakout"] = out["breakout_20d_high"] & (out["volume_ratio_5d"] >= 1.5)
    prev_20d_high = high.shift(1).rolling(20, min_periods=10).max()
    out["failed_breakout"] = (high > prev_20d_high) & (close < prev_20d_high)
    out["gap_up_failed"] = (open_ > prev_close * 1.02) & (close < open_)

    twse_maps = {h: market_return_map(market_index, "TWSE", h) for h in [5, 10, 20]}
    tpex_maps = {h: market_return_map(market_index, "TPEX", h) for h in [5, 10, 20]}
    for horizon in [5, 10, 20]:
        twse_ret = out["trade_date"].map(twse_maps[horizon])
        tpex_ret = out["trade_date"].map(tpex_maps[horizon])
        out[f"relative_ret_{horizon}d_vs_twse"] = out[f"price_ret_{horizon}d"] - twse_ret
        out[f"relative_ret_{horizon}d_vs_tpex"] = out[f"price_ret_{horizon}d"] - tpex_ret

    labeled = add_future_labels(pd.concat([out, df[["close", "high", "low"]]], axis=1).loc[:, ~pd.concat([out, df[["close", "high", "low"]]], axis=1).columns.duplicated()])
    return labeled


def normalize_stock_columns(df: pd.DataFrame) -> pd.DataFrame:
    out = df.copy()
    rename = {
        "date": "trade_date",
        "signal_date": "trade_date",
        "code": "stock_id",
        "ticker": "stock_id",
        "name": "stock_name",
        "category_cn": "daily_candidate_category",
        "category": "daily_candidate_category",
        "細分族群": "theme",
        "primary_theme": "theme",
    }
    for src, dst in rename.items():
        if src in out.columns and dst not in out.columns:
            out[dst] = out[src]
    if "stock_id" in out.columns:
        out["stock_id"] = out["stock_id"].map(normalize_code)
    if "trade_date" in out.columns:
        out["trade_date"] = out["trade_date"].map(normalize_date)
    return out


def merge_exact_enrichment(panel: pd.DataFrame, source: pd.DataFrame, columns: list[str], prefix: str = "") -> pd.DataFrame:
    if source.empty or not {"trade_date", "stock_id"}.issubset(source.columns):
        return panel
    source = source.dropna(subset=["trade_date", "stock_id"]).copy()
    source = source[source["trade_date"].ne("") & source["stock_id"].ne("")]
    keep = ["trade_date", "stock_id"] + [col for col in columns if col in source.columns]
    if len(keep) <= 2:
        return panel
    source = source[keep].drop_duplicates(["trade_date", "stock_id"], keep="last")
    rename_map: dict[str, str] = {}
    for col in keep:
        if col in {"trade_date", "stock_id"}:
            continue
        rename_map[col] = f"{prefix}{col}" if prefix else f"{col}__new"
    source = source.rename(columns=rename_map)
    merged = panel.merge(source, how="left", on=["trade_date", "stock_id"])
    for original, incoming in rename_map.items():
        if original not in merged.columns:
            merged[original] = merged[incoming]
        else:
            current = merged[original].astype(str)
            empty = merged[original].isna() | current.isin(["", "nan", "None", "<NA>"])
            merged.loc[empty, original] = merged.loc[empty, incoming]
        merged = merged.drop(columns=[incoming])
    return merged


def merge_asof_by_stock(panel: pd.DataFrame, source: pd.DataFrame, source_date_col: str, columns: list[str], max_days: int = 10) -> pd.DataFrame:
    if source.empty or source_date_col not in source.columns:
        return panel
    src = source.copy()
    if "code" in src.columns and "stock_id" not in src.columns:
        src["stock_id"] = src["code"]
    src["stock_id"] = src["stock_id"].map(normalize_code)
    src[source_date_col] = src[source_date_col].map(normalize_date)
    src = src[src["stock_id"].ne("") & src[source_date_col].ne("")]
    keep = ["stock_id", source_date_col] + [col for col in columns if col in src.columns]
    if len(keep) <= 2:
        return panel
    src = src[keep].drop_duplicates(["stock_id", source_date_col], keep="last")
    src["_source_dt"] = pd.to_datetime(src[source_date_col], format="%Y%m%d", errors="coerce")

    base = panel.copy()
    base["_trade_dt"] = pd.to_datetime(base["trade_date"], format="%Y%m%d", errors="coerce")
    base = base.sort_values(["_trade_dt", "stock_id"]).reset_index(drop=True)
    right_payload = src.sort_values(["_source_dt", "stock_id"]).reset_index(drop=True)
    rename_map = {
        col: f"{col}__tdcc"
        for col in right_payload.columns
        if col not in {"stock_id", source_date_col, "_source_dt"}
    }
    right_payload = right_payload.rename(columns=rename_map)
    out = pd.merge_asof(
        base,
        right_payload,
        left_on="_trade_dt",
        right_on="_source_dt",
        by="stock_id",
        direction="backward",
        tolerance=pd.Timedelta(days=max_days),
    )
    for original, incoming in rename_map.items():
        if original not in out.columns:
            out[original] = out[incoming]
        else:
            current = out[original].astype(str)
            empty = out[original].isna() | current.isin(["", "nan", "None", "<NA>"])
            out.loc[empty, original] = out.loc[empty, incoming]
        out = out.drop(columns=[incoming])
    return out.drop(columns=[c for c in ["_trade_dt", "_source_dt"] if c in out.columns])


def enrich_panel(panel: pd.DataFrame) -> pd.DataFrame:
    out = panel.copy()

    theme_map = read_csv(STOCK_THEME_MAP_CSV, dtype=str, keep_default_na=False)
    if not theme_map.empty:
        theme_map["stock_id"] = theme_map.get("code", "").map(normalize_code)
        theme_cols = ["stock_id", "primary_theme", "secondary_theme", "industry", "concept_tags"]
        theme_map = theme_map[[col for col in theme_cols if col in theme_map.columns]].drop_duplicates("stock_id")
        out = out.merge(theme_map, how="left", on="stock_id")
        out["theme"] = out["theme"].where(out["theme"].astype(str).ne(""), out.get("primary_theme", ""))

    candidates = normalize_stock_columns(read_csv(DAILY_CANDIDATE_LOG_CSV, dtype=str, keep_default_na=False))
    candidate_cols = [
        "daily_candidate_category", "score", "rank", "priority", "sector", "sub_theme",
        "tdcc_status", "warrant_status", "close_at_signal",
    ]
    out = merge_exact_enrichment(out, candidates, candidate_cols)

    latest_candidates = normalize_stock_columns(read_csv(ALL_CANDIDATES_CSV, dtype=str, keep_default_na=False))
    latest_cols = [
        "daily_candidate_category", "score", "rank", "theme", "industry",
        "tdcc_judgement", "tdcc_accumulation_signal", "warrant_flow_signal",
        "warrant_flow_score", "revenue_yoy_pct", "latest_revenue_yoy",
        "cumulative_revenue_yoy", "revenue_low_price_response", "revenue_pullback",
        "revenue_breakout_low_response", "is_construction_recognition",
        "recognition_type", "revenue_signal_type", "theme_strength_score",
        "catalyst_strength_score", "catalyst_tags", "event_catalyst_tags",
        "fundamental_catalyst_tags", "similar_to_shihsinko_flag",
        "catalyst_summary", "price_reaction_level", "low_reaction_after_catalyst",
        "already_reacted_to_catalyst", "catalyst_overheated",
    ]
    out = merge_exact_enrichment(out, latest_candidates, latest_cols)

    repeat = normalize_stock_columns(read_csv(CANDIDATE_REPEAT_CSV, dtype=str, keep_default_na=False))
    repeat_cols = [
        "consecutive_appear_days_any_category", "appear_count_5d", "appear_count_10d",
        "appear_count_20d", "repeat_appear_label",
    ]
    out = merge_exact_enrichment(out, repeat, repeat_cols)

    tdcc = read_csv(TDCC_SNAPSHOT_CSV, dtype=str, keep_default_na=False)
    tdcc_cols = [
        "primary_theme", "tdcc_available", "tdcc_consecutive_up_weeks", "all_thresholds_up",
        "high_thresholds_up", "four_thresholds_sync_up", "tdcc_1w_change_400",
        "tdcc_1w_change_600", "tdcc_1w_change_800", "tdcc_1w_change_1000",
        "tdcc_2w_change_400", "tdcc_2w_change_800", "tdcc_2w_change_1000",
        "tdcc_3w_change_400", "tdcc_3w_change_800", "tdcc_3w_change_1000",
        "retail_ratio_change_1w", "total_shareholders_change_1w", "tdcc_price_phase",
        "setup_type", "abm_score", "abm_rank", "theme_breadth_score",
        "theme_mainstream_status", "theme_heat_level", "theme_momentum_score",
        "theme_tdcc_breadth_score", "theme_price_breadth_score", "theme_warrant_heat_score",
        "theme_relative_strength",
    ]
    out = merge_asof_by_stock(out, tdcc, "signal_date", tdcc_cols, max_days=10)

    abm = read_csv(ABM_TOP_CSV, dtype=str, keep_default_na=False)
    if not abm.empty:
        abm["stock_id"] = abm["stock_id"].map(normalize_code)
        abm["trade_date"] = out["trade_date"].max()
        abm_cols = [
            "abm_score", "abm_rank", "setup_type", "tdcc_price_phase",
            "theme_mainstream_status", "theme_heat_level", "theme_breadth_score",
        ]
        out = merge_exact_enrichment(out, abm, abm_cols)

    warrant = normalize_stock_columns(read_csv(WARRANT_FLOW_CSV, dtype=str, keep_default_na=False))
    warrant_cols = [
        "warrant_flow_signal", "warrant_flow_score", "call_turnover", "put_turnover",
        "call_put_turnover_ratio", "low_float_call_spike_count",
    ]
    out = merge_exact_enrichment(out, warrant, warrant_cols)

    market_regime = read_csv(MARKET_REGIME_CSV, dtype=str, keep_default_na=False)
    if not market_regime.empty:
        market_regime["trade_date"] = market_regime["date"].map(normalize_date)
        regime_cols = [
            "trade_date", "market_regime", "risk_level", "twse_return_5d",
            "twse_return_20d", "tpex_return_5d", "tpex_return_20d",
            "foreign_tx_futures_net_oi", "put_call_oi_ratio_pct", "taiwan_vix",
        ]
        market_regime = market_regime[[col for col in regime_cols if col in market_regime.columns]].drop_duplicates("trade_date")
        out = out.merge(market_regime, how="left", on="trade_date")

    defaults = {
        "tdcc_available": out.get("tdcc_consecutive_up_weeks", "").astype(str).ne(""),
        "warrant_available": out.get("warrant_flow_signal", "").astype(str).ne(""),
        "revenue_available": out.get("revenue_yoy_pct", out.get("latest_revenue_yoy", "")).astype(str).ne(""),
        "catalyst_available": out.get("catalyst_tags", "").astype(str).ne(""),
    }
    for col, values in defaults.items():
        if col not in out.columns:
            out[col] = values

    out["theme"] = out["theme"].fillna("").astype(str)
    if "primary_theme" in out.columns:
        out["theme"] = out["theme"].where(out["theme"].ne(""), out["primary_theme"].fillna(""))
    out["theme"] = out["theme"].where(out["theme"].ne(""), "other")
    return out


def finalize_columns(panel: pd.DataFrame) -> pd.DataFrame:
    out = panel.copy()
    column_defaults: dict[str, Any] = {
        "warrant_available": False,
        "call_inflow": False,
        "call_strong_inflow": False,
        "put_inflow": False,
        "call_put_bullish": False,
        "warrant_overheat": False,
        "low_float_call_spike": False,
        "warrant_flow_score": "",
        "warrant_sector_heat_score": "",
        "revenue_yoy": out.get("revenue_yoy_pct", out.get("latest_revenue_yoy", "")),
        "revenue_mom": "",
        "revenue_yoy_accel": "",
        "revenue_mom_accel": "",
        "revenue_growth_rank": "",
        "revenue_low_price_response": False,
        "revenue_pullback": False,
        "revenue_breakout_low_response": False,
        "revenue_type": out.get("revenue_signal_type", ""),
        "construction_recognition_flag": out.get("is_construction_recognition", ""),
        "shipment_type_flag": "",
        "catalyst_count_7d": "",
        "catalyst_count_30d": "",
        "catalyst_type": out.get("event_catalyst_tags", ""),
        "catalyst_confirmed": "",
        "catalyst_needs_review": "",
        "event_date_nearby": out.get("nearest_event_date", ""),
        "earnings_call_nearby": "",
        "shareholder_meeting_nearby": "",
        "product_news_flag": "",
        "policy_news_flag": "",
        "order_news_flag": "",
        "legal_risk_news_flag": "",
        "same_theme_breakout_count": "",
        "same_theme_tdcc_accumulation_count": "",
        "same_theme_warrant_hot_count": "",
        "foreign_tx_net_oi": out.get("foreign_tx_futures_net_oi", ""),
        "txo_put_call_ratio": out.get("put_call_oi_ratio_pct", ""),
        "taiwan_vix": out.get("taiwan_vix", ""),
        "continuous_days_on_list": out.get("consecutive_appear_days_any_category", ""),
        "overheat_flag": False,
        "watch_only_flag": "",
    }
    for col, default in column_defaults.items():
        if col not in out.columns:
            out[col] = default

    signal = out.get("warrant_flow_signal", pd.Series("", index=out.index)).astype(str)
    out["call_inflow"] = signal.str.contains("call_inflow|call_put_bullish", case=False, na=False)
    out["call_strong_inflow"] = signal.str.contains("call_strong", case=False, na=False)
    out["put_inflow"] = signal.str.contains("put_inflow|bearish", case=False, na=False)
    out["call_put_bullish"] = signal.str.contains("call_put_bullish", case=False, na=False)
    warrant_warning = out["warrant_flow_warning"] if "warrant_flow_warning" in out.columns else pd.Series("", index=out.index)
    out["warrant_overheat"] = warrant_warning.astype(str).str.contains("overheat|過熱", case=False, na=False)
    out["low_float_call_spike"] = numeric(out, "low_float_call_spike_count", 0).fillna(0) > 0

    out["overheat_flag"] = (
        numeric(out, "price_ret_20d", 0).fillna(0) > 25
    ) | (
        numeric(out, "distance_ma20_pct", 0).fillna(0) > 15
    ) | out["high_volume_upper_shadow"].fillna(False)
    out["failed_breakout_flag"] = out["failed_breakout"]

    desired = [
        "trade_date", "stock_id", "stock_name", "market_type", "theme", "close", "volume", "turnover_value",
        "price_ret_1d", "price_ret_3d", "price_ret_5d", "price_ret_10d", "price_ret_20d",
        "relative_ret_5d_vs_twse", "relative_ret_10d_vs_twse", "relative_ret_20d_vs_twse",
        "relative_ret_5d_vs_tpex", "relative_ret_10d_vs_tpex", "relative_ret_20d_vs_tpex",
        "distance_ma5_pct", "distance_ma10_pct", "distance_ma20_pct", "distance_ma60_pct",
        "ma5_slope", "ma10_slope", "ma20_slope", "ma60_slope", "volume_ratio_5d",
        "volume_ratio_10d", "volume_ratio_20d", "volatility_20d", "atr_14",
        "close_position_20d", "close_position_60d", "distance_20d_high", "distance_60d_high",
        "breakout_20d_high", "breakout_60d_high", "pullback_to_ma20", "pullback_to_ma60",
        "consolidation_days", "narrow_range_10d", "narrow_range_20d", "upper_shadow_ratio",
        "lower_shadow_ratio", "high_volume_upper_shadow", "high_volume_breakout",
        "failed_breakout", "gap_up_failed", "tdcc_available", "tdcc_consecutive_up_weeks",
        "all_thresholds_up", "high_thresholds_up", "four_thresholds_sync_up",
        "tdcc_1w_change_400", "tdcc_1w_change_600", "tdcc_1w_change_800", "tdcc_1w_change_1000",
        "tdcc_2w_change_400", "tdcc_2w_change_800", "tdcc_2w_change_1000",
        "tdcc_3w_change_400", "tdcc_3w_change_800", "tdcc_3w_change_1000",
        "retail_ratio_change_1w", "total_shareholders_change_1w", "tdcc_price_phase",
        "setup_type", "abm_score", "abm_rank", "warrant_available", "call_inflow",
        "call_strong_inflow", "put_inflow", "call_put_bullish", "warrant_overheat",
        "low_float_call_spike", "warrant_flow_score", "warrant_sector_heat_score",
        "revenue_available", "revenue_yoy", "revenue_mom", "revenue_yoy_accel",
        "revenue_mom_accel", "revenue_growth_rank", "revenue_low_price_response",
        "revenue_pullback", "revenue_breakout_low_response", "revenue_type",
        "construction_recognition_flag", "shipment_type_flag", "catalyst_available",
        "catalyst_count_7d", "catalyst_count_30d", "catalyst_type", "catalyst_confirmed",
        "catalyst_needs_review", "event_date_nearby", "earnings_call_nearby",
        "shareholder_meeting_nearby", "product_news_flag", "policy_news_flag",
        "order_news_flag", "legal_risk_news_flag", "theme_breadth_score",
        "theme_mainstream_status", "theme_heat_level", "theme_momentum_score",
        "theme_tdcc_breadth_score", "theme_price_breadth_score", "theme_warrant_heat_score",
        "theme_relative_strength", "same_theme_breakout_count",
        "same_theme_tdcc_accumulation_count", "same_theme_warrant_hot_count",
        "market_regime", "risk_level", "twse_return_5d", "twse_return_20d",
        "tpex_return_5d", "tpex_return_20d", "foreign_tx_net_oi", "txo_put_call_ratio",
        "taiwan_vix", "daily_candidate_category", "score", "rank", "continuous_days_on_list",
        "failed_breakout_flag", "overheat_flag", "watch_only_flag",
        "future_close_d5", "future_close_d10", "future_close_d20",
        "future_high_d5", "future_high_d10", "future_high_d20",
        "future_ret_5d_close", "future_ret_10d_close", "future_ret_20d_close",
        "future_max_ret_5d", "future_max_ret_10d", "future_max_ret_20d",
        "future_min_ret_5d", "future_min_ret_10d", "future_min_ret_20d",
        "max_drawdown_d5", "max_drawdown_d10", "max_drawdown_d20",
        "days_to_high_d5", "days_to_high_d10", "days_to_high_d20",
        "surge_5d", "surge_10d", "surge_20d", "mature_5d", "mature_10d", "mature_20d",
    ]
    for col in desired:
        if col not in out.columns:
            out[col] = ""
    return out[desired]


def score_rows(panel: pd.DataFrame) -> pd.DataFrame:
    out = panel.copy()
    score = pd.Series(0.0, index=out.index)

    phase = out.get("tdcc_price_phase", "").astype(str)
    setup = out.get("setup_type", "").astype(str)
    theme_status = out.get("theme_mainstream_status", "").astype(str)
    market_regime = out.get("market_regime", "").astype(str)
    warrant_signal = out.get("warrant_flow_signal", "").astype(str) if "warrant_flow_signal" in out.columns else pd.Series("", index=out.index)

    score += phase.eq("tdcc_leading_price").astype(int) * 20
    score += (numeric(out, "tdcc_consecutive_up_weeks", 0).fillna(0) >= 2).astype(int) * 10
    score += as_bool_series(out, "high_thresholds_up").astype(int) * 10
    score += setup.eq("quiet_accumulation").astype(int) * 15
    score -= phase.eq("overheated_after_tdcc").astype(int) * 20
    score -= phase.eq("tdcc_price_divergence").astype(int) * 25

    score += (numeric(out, "consolidation_days", 0).fillna(0) >= 10).astype(int) * 10
    score += as_bool_series(out, "narrow_range_20d").astype(int) * 10
    score += numeric(out, "distance_ma20_pct", math.nan).between(-3, 6).astype(int) * 10
    score += numeric(out, "volume_ratio_20d", math.nan).between(1.0, 1.8).astype(int) * 8
    score += as_bool_series(out, "breakout_20d_high").astype(int) * 8
    score -= as_bool_series(out, "high_volume_upper_shadow").astype(int) * 10
    score -= as_bool_series(out, "failed_breakout").astype(int) * 15
    score -= (numeric(out, "price_ret_20d", 0).fillna(0) > 25).astype(int) * 20

    score += theme_status.eq("emerging_theme").astype(int) * 15
    score += theme_status.eq("mainstream_follow_through").astype(int) * 10
    score -= theme_status.eq("single_name_signal").astype(int) * 10
    score -= theme_status.eq("weak_theme").astype(int) * 15
    score += (numeric(out, "theme_breadth_score", 0).fillna(0) >= 8).astype(int) * 10

    score += (numeric(out, "revenue_yoy", 0).fillna(0) > 20).astype(int) * 8
    score += (numeric(out, "revenue_yoy_accel", 0).fillna(0) > 0).astype(int) * 8
    score += as_bool_series(out, "revenue_low_price_response").astype(int) * 12
    score += out.get("catalyst_confirmed", pd.Series("", index=out.index)).astype(str).str.lower().isin({"true", "1", "yes"}).astype(int) * 10
    score -= as_bool_series(out, "construction_recognition_flag").astype(int) * 5

    score += warrant_signal.str.contains("call_inflow", case=False, na=False).astype(int) * 5
    score += warrant_signal.str.contains("call_strong", case=False, na=False).astype(int) * 8
    score -= as_bool_series(out, "warrant_overheat").astype(int) * 10
    score -= warrant_signal.str.contains("put_inflow", case=False, na=False).astype(int) * 10

    score += market_regime.eq("strong_bull").astype(int) * 5
    score += market_regime.eq("mild_bull").astype(int) * 3
    score -= market_regime.eq("correction").astype(int) * 10
    score -= out.get("risk_level", pd.Series("", index=out.index)).astype(str).eq("high_risk").astype(int) * 8

    out["surge_precondition_score"] = score.clip(lower=0).round(2)
    too_hot = (numeric(out, "price_ret_20d", 0).fillna(0) > 25) | as_bool_series(out, "overheat_flag")
    insufficient = out["close"].isna() | out["trade_date"].astype(str).eq("")
    out["surge_watch_label"] = "D_weak_or_insufficient"
    out.loc[out["surge_precondition_score"].ge(60), "surge_watch_label"] = "B_confirm_needed"
    out.loc[out["surge_precondition_score"].ge(75), "surge_watch_label"] = "A_surge_watch"
    out.loc[too_hot, "surge_watch_label"] = "C_too_hot"
    out.loc[insufficient, "surge_watch_label"] = "D_weak_or_insufficient"
    out["risk_flags"] = ""
    out.loc[too_hot, "risk_flags"] = "too_hot_or_overextended"
    out.loc[as_bool_series(out, "failed_breakout"), "risk_flags"] = out["risk_flags"].where(out["risk_flags"].eq(""), out["risk_flags"] + ";") + "failed_breakout"
    out.loc[phase.eq("tdcc_price_divergence"), "risk_flags"] = out["risk_flags"].where(out["risk_flags"].eq(""), out["risk_flags"] + ";") + "tdcc_price_divergence"

    reasons: list[str] = []
    for _, row in out.iterrows():
        bits = []
        if safe_str(row.get("tdcc_price_phase")) == "tdcc_leading_price":
            bits.append("TDCC領先股價")
        if safe_str(row.get("setup_type")) == "quiet_accumulation":
            bits.append("quiet_accumulation")
        if to_number(row.get("distance_ma20_pct")) >= -3 and to_number(row.get("distance_ma20_pct")) <= 6:
            bits.append("靠近MA20")
        if to_number(row.get("volume_ratio_20d")) >= 1.0 and to_number(row.get("volume_ratio_20d")) <= 1.8:
            bits.append("量能溫和")
        if safe_str(row.get("theme_mainstream_status")) in {"emerging_theme", "mainstream_follow_through"}:
            bits.append("族群擴散")
        if safe_str(row.get("risk_flags")):
            bits.append("風險:" + safe_str(row.get("risk_flags")))
        reasons.append("；".join(bits[:5]))
    out["reason_summary"] = reasons
    return out


def build_labels(panel: pd.DataFrame) -> pd.DataFrame:
    cols = [
        "trade_date", "stock_id", "stock_name", "close",
        "future_close_d5", "future_close_d10", "future_close_d20",
        "future_high_d5", "future_high_d10", "future_high_d20",
        "future_ret_5d_close", "future_ret_10d_close", "future_ret_20d_close",
        "future_max_ret_5d", "future_max_ret_10d", "future_max_ret_20d",
        "future_min_ret_5d", "future_min_ret_10d", "future_min_ret_20d",
        "max_drawdown_d5", "max_drawdown_d10", "max_drawdown_d20",
        "days_to_high_d5", "days_to_high_d10", "days_to_high_d20",
        "surge_5d", "surge_10d", "surge_20d", "mature_5d", "mature_10d", "mature_20d",
    ]
    labels = panel[[col for col in cols if col in panel.columns]].copy()
    labels = labels.rename(columns={"trade_date": "trade_date"})
    return labels


def build_event_study(panel: pd.DataFrame) -> pd.DataFrame:
    mature_surge = panel[
        ((as_bool_series(panel, "surge_5d") & as_bool_series(panel, "mature_5d"))
         | (as_bool_series(panel, "surge_10d") & as_bool_series(panel, "mature_10d")))
    ].copy()
    if mature_surge.empty:
        return pd.DataFrame()

    records: list[dict[str, Any]] = []
    panel_by_stock = {sid: g.sort_values("trade_date").reset_index(drop=True) for sid, g in panel.groupby("stock_id")}
    for _, event in mature_surge.iterrows():
        stock_id = safe_str(event.get("stock_id"))
        group = panel_by_stock.get(stock_id)
        if group is None or group.empty:
            continue
        matches = group.index[group["trade_date"].astype(str).eq(safe_str(event.get("trade_date")))].tolist()
        if not matches:
            continue
        idx = matches[0]
        surge_type = "surge_10d" if bool(event.get("surge_10d")) else "surge_5d"
        for lookback in SURGE_EVENT_LOOKBACKS:
            pre_idx = idx - lookback
            if pre_idx < 0:
                continue
            row = group.iloc[pre_idx].to_dict()
            row.update(
                {
                    "surge_date": event.get("trade_date"),
                    "pre_date": row.get("trade_date"),
                    "surge_type": surge_type,
                    "days_before_surge_signal": lookback,
                    "event_future_max_ret_5d": event.get("future_max_ret_5d"),
                    "event_future_max_ret_10d": event.get("future_max_ret_10d"),
                    "event_future_max_ret_20d": event.get("future_max_ret_20d"),
                    "days_to_surge_high": event.get("days_to_high_d10") or event.get("days_to_high_d5"),
                }
            )
            records.append(row)
    return pd.DataFrame(records)


def build_control_sample(panel: pd.DataFrame, event_study: pd.DataFrame) -> pd.DataFrame:
    if event_study.empty:
        return pd.DataFrame()
    controls: list[pd.DataFrame] = []
    mature = panel[as_bool_series(panel, "mature_10d")].copy()
    mature = mature[~as_bool_series(mature, "surge_5d") & ~as_bool_series(mature, "surge_10d") & ~as_bool_series(mature, "surge_20d")]
    if mature.empty:
        return pd.DataFrame()

    for _, event in event_study[["pre_date", "theme", "market_type"]].drop_duplicates().iterrows():
        same_day = mature[mature["trade_date"].astype(str).eq(safe_str(event.get("pre_date")))]
        if same_day.empty:
            continue
        same_theme = same_day[same_day["theme"].astype(str).eq(safe_str(event.get("theme")))]
        pool = same_theme if len(same_theme) >= 5 else same_day[same_day["market_type"].astype(str).eq(safe_str(event.get("market_type")))]
        if pool.empty:
            pool = same_day
        controls.append(pool.sort_values(["theme", "stock_id"]).head(10).assign(control_for_pre_date=event.get("pre_date")))
    if not controls:
        return pd.DataFrame()
    return pd.concat(controls, ignore_index=True).drop_duplicates(["trade_date", "stock_id"], keep="first")


def condition_masks(df: pd.DataFrame) -> dict[str, pd.Series]:
    phase = df.get("tdcc_price_phase", pd.Series("", index=df.index)).astype(str)
    setup = df.get("setup_type", pd.Series("", index=df.index)).astype(str)
    theme_status = df.get("theme_mainstream_status", pd.Series("", index=df.index)).astype(str)
    warrant_signal = df.get("warrant_flow_signal", pd.Series("", index=df.index)).astype(str)
    return {
        "tdcc_leading_price + quiet_accumulation": phase.eq("tdcc_leading_price") & setup.eq("quiet_accumulation"),
        "tdcc_consecutive_up_weeks >= 2 + price_ret_20d <= 8": (numeric(df, "tdcc_consecutive_up_weeks", 0) >= 2) & (numeric(df, "price_ret_20d", 999) <= 8),
        "volume_ratio_20d between 1.0 and 1.8": numeric(df, "volume_ratio_20d", math.nan).between(1.0, 1.8),
        "distance_ma20_pct between -3 and +6": numeric(df, "distance_ma20_pct", math.nan).between(-3, 6),
        "theme_mainstream_status = emerging_theme": theme_status.eq("emerging_theme"),
        "revenue_yoy > 20 + revenue_low_price_response": (numeric(df, "revenue_yoy", 0) > 20) & as_bool_series(df, "revenue_low_price_response"),
        "warrant_call_inflow + TDCC high_thresholds_up": warrant_signal.str.contains("call", case=False, na=False) & as_bool_series(df, "high_thresholds_up"),
        "consolidation_days >= 10 + narrow_range_20d": (numeric(df, "consolidation_days", 0) >= 10) & as_bool_series(df, "narrow_range_20d"),
        "relative_ret_20d_vs_twse > 0": numeric(df, "relative_ret_20d_vs_twse", math.nan) > 0,
        "low volatility compression + volume expansion": as_bool_series(df, "narrow_range_20d") & numeric(df, "volume_ratio_20d", math.nan).between(1.0, 1.8),
    }


def build_feature_importance(panel: pd.DataFrame, control: pd.DataFrame) -> pd.DataFrame:
    mature = panel[as_bool_series(panel, "mature_10d")].copy()
    if mature.empty:
        return pd.DataFrame()
    mature["surge_target"] = as_bool_series(mature, "surge_5d") | as_bool_series(mature, "surge_10d")
    baseline = float(mature["surge_target"].mean()) if len(mature) else 0.0
    total_surge = int(mature["surge_target"].sum())

    records: list[dict[str, Any]] = []
    for name, mask in condition_masks(mature).items():
        subset = mature[mask.fillna(False)]
        sample_count = len(subset)
        surge_count = int(subset["surge_target"].sum()) if sample_count else 0
        surge_rate = surge_count / sample_count if sample_count else math.nan
        records.append(
            {
                "condition_name": name,
                "sample_count": sample_count,
                "surge_count": surge_count,
                "surge_rate": surge_rate,
                "baseline_surge_rate": baseline,
                "lift_vs_baseline": (surge_rate / baseline) if sample_count and baseline > 0 else math.nan,
                "avg_future_max_ret_5d": subset["future_max_ret_5d"].mean() if sample_count else math.nan,
                "avg_future_max_ret_10d": subset["future_max_ret_10d"].mean() if sample_count else math.nan,
                "avg_mae_before_surge": subset["future_min_ret_10d"].mean() if sample_count else math.nan,
                "false_positive_rate": 1 - surge_rate if sample_count else math.nan,
                "precision": surge_rate,
                "recall": surge_count / total_surge if total_surge else math.nan,
                "control_sample_count": len(control) if not control.empty else 0,
                "sample_status": "ok" if sample_count >= 30 else "insufficient_sample",
            }
        )
    return pd.DataFrame(records).sort_values(["lift_vs_baseline", "sample_count"], ascending=[False, False])


def build_backtest(scored: pd.DataFrame) -> pd.DataFrame:
    mature = scored[as_bool_series(scored, "mature_10d")].copy()
    if mature.empty:
        return pd.DataFrame()
    baseline_5 = as_bool_series(mature, "surge_5d").mean()
    baseline_10 = as_bool_series(mature, "surge_10d").mean()
    baseline_20 = as_bool_series(mature, "surge_20d").mean()
    records: list[dict[str, Any]] = []

    for top_n in [10, 20, 50, 100]:
        daily_rows = []
        for _, group in mature.groupby("trade_date"):
            daily_rows.append(group.sort_values("surge_precondition_score", ascending=False).head(top_n))
        subset = pd.concat(daily_rows, ignore_index=True) if daily_rows else pd.DataFrame()
        records.append(backtest_record(f"top_{top_n}", subset, baseline_5, baseline_10, baseline_20))

    bins = [
        ("score_ge_80", mature[mature["surge_precondition_score"] >= 80]),
        ("score_70_80", mature[(mature["surge_precondition_score"] >= 70) & (mature["surge_precondition_score"] < 80)]),
        ("score_60_70", mature[(mature["surge_precondition_score"] >= 60) & (mature["surge_precondition_score"] < 70)]),
        ("score_50_60", mature[(mature["surge_precondition_score"] >= 50) & (mature["surge_precondition_score"] < 60)]),
        ("score_lt_50", mature[mature["surge_precondition_score"] < 50]),
    ]
    for name, subset in bins:
        records.append(backtest_record(name, subset, baseline_5, baseline_10, baseline_20))

    for label, subset in mature.groupby("surge_watch_label"):
        records.append(backtest_record(f"label_{label}", subset, baseline_5, baseline_10, baseline_20))

    for regime, subset in mature.groupby("market_regime", dropna=False):
        records.append(backtest_record(f"market_{safe_str(regime) or 'unknown'}", subset, baseline_5, baseline_10, baseline_20))

    for theme_status, subset in mature.groupby("theme_mainstream_status", dropna=False):
        records.append(backtest_record(f"theme_{safe_str(theme_status) or 'unknown'}", subset, baseline_5, baseline_10, baseline_20))

    return pd.DataFrame(records)


def feature_export_frame(scored: pd.DataFrame) -> pd.DataFrame:
    label_prefixes = (
        "future_",
        "surge_5d",
        "surge_10d",
        "surge_20d",
        "mature_",
        "max_drawdown_d",
        "days_to_high_d",
    )
    feature_cols = [col for col in scored.columns if not col.startswith(label_prefixes)]
    dates = sorted(scored["trade_date"].dropna().astype(str).unique().tolist())
    keep_dates = set(dates[-FEATURE_PANEL_EXPORT_DAYS:]) if dates else set()
    return scored[scored["trade_date"].astype(str).isin(keep_dates)][feature_cols].copy()


def label_export_frame(labels: pd.DataFrame) -> pd.DataFrame:
    if labels.empty or "trade_date" not in labels.columns:
        return labels
    dates = sorted(labels["trade_date"].dropna().astype(str).unique().tolist())
    keep_dates = set(dates[-LABEL_EXPORT_DAYS:]) if dates else set()
    return labels[labels["trade_date"].astype(str).isin(keep_dates)].copy()


def event_study_export_frame(event_study: pd.DataFrame) -> pd.DataFrame:
    keep = [
        "surge_date", "pre_date", "stock_id", "stock_name", "theme", "market_type",
        "surge_type", "days_before_surge_signal", "event_future_max_ret_5d",
        "event_future_max_ret_10d", "event_future_max_ret_20d", "days_to_surge_high",
        "close", "volume", "price_ret_5d", "price_ret_10d", "price_ret_20d",
        "relative_ret_20d_vs_twse", "relative_ret_20d_vs_tpex", "distance_ma20_pct",
        "distance_ma60_pct", "volume_ratio_20d", "volatility_20d", "atr_14",
        "close_position_20d", "distance_20d_high", "breakout_20d_high",
        "consolidation_days", "narrow_range_20d", "high_volume_upper_shadow",
        "failed_breakout", "tdcc_consecutive_up_weeks", "all_thresholds_up",
        "high_thresholds_up", "tdcc_price_phase", "setup_type", "abm_score",
        "warrant_flow_score", "revenue_yoy", "revenue_low_price_response",
        "catalyst_available", "theme_breadth_score", "theme_mainstream_status",
        "market_regime", "risk_level", "surge_precondition_score",
        "surge_watch_label", "risk_flags", "reason_summary",
    ]
    out = event_study[[col for col in keep if col in event_study.columns]].copy()
    if "pre_date" in out.columns:
        out = out.sort_values(["pre_date", "stock_id"]).tail(EVENT_STUDY_EXPORT_ROWS)
    return out


def backtest_record(segment: str, subset: pd.DataFrame, baseline_5: float, baseline_10: float, baseline_20: float) -> dict[str, Any]:
    count = len(subset)
    if count == 0:
        return {"segment": segment, "sample_count": 0, "sample_status": "insufficient_sample"}
    rate_5 = as_bool_series(subset, "surge_5d").mean()
    rate_10 = as_bool_series(subset, "surge_10d").mean()
    rate_20 = as_bool_series(subset, "surge_20d").mean()
    return {
        "segment": segment,
        "sample_count": count,
        "surge_5d_rate": rate_5,
        "surge_10d_rate": rate_10,
        "surge_20d_rate": rate_20,
        "baseline_surge_5d_rate": baseline_5,
        "baseline_surge_10d_rate": baseline_10,
        "baseline_surge_20d_rate": baseline_20,
        "lift_5d": rate_5 / baseline_5 if baseline_5 else math.nan,
        "lift_10d": rate_10 / baseline_10 if baseline_10 else math.nan,
        "lift_20d": rate_20 / baseline_20 if baseline_20 else math.nan,
        "avg_future_max_ret_5d": subset["future_max_ret_5d"].mean(),
        "avg_future_max_ret_10d": subset["future_max_ret_10d"].mean(),
        "avg_future_max_ret_20d": subset["future_max_ret_20d"].mean(),
        "avg_max_drawdown_10d": subset["max_drawdown_d10"].mean(),
        "avg_max_drawdown_20d": subset["max_drawdown_d20"].mean(),
        "sample_status": "ok" if count >= 30 else "insufficient_sample",
    }


def write_latest_reports(
    panel: pd.DataFrame,
    labels: pd.DataFrame,
    event_study: pd.DataFrame,
    controls: pd.DataFrame,
    importance: pd.DataFrame,
    scored: pd.DataFrame,
    backtest: pd.DataFrame,
) -> None:
    latest_date = panel["trade_date"].max() if not panel.empty else ""
    latest = scored[scored["trade_date"].eq(latest_date)].copy()
    latest = latest.sort_values(["surge_precondition_score", "stock_id"], ascending=[False, True])

    candidate_cols = [
        "trade_date", "stock_id", "stock_name", "theme", "surge_precondition_score",
        "surge_watch_label", "tdcc_price_phase", "setup_type", "abm_score",
        "tdcc_consecutive_up_weeks", "price_ret_20d", "distance_ma20_pct",
        "volume_ratio_20d", "theme_mainstream_status", "revenue_yoy",
        "warrant_flow_score", "catalyst_summary", "market_regime", "risk_flags",
        "reason_summary",
    ]
    candidates = latest[[col for col in candidate_cols if col in latest.columns]].head(100)
    write_csv(candidates, CANDIDATES_CSV)
    CANDIDATES_MD.write_text(
        "\n".join(
            [
                "# Surge Precondition Candidates Latest",
                "",
                f"generated_at: {now_text()}",
                f"trade_date: {latest_date}",
                "",
                "這不是買進建議，是暴漲前條件研究與候選追蹤。",
                "",
                markdown_table(candidates.head(30)),
                "",
            ]
        ),
        encoding="utf-8",
    )

    score_cols = [
        "trade_date", "stock_id", "stock_name", "theme", "surge_precondition_score",
        "surge_watch_label", "reason_summary", "risk_flags",
    ]
    score_latest = latest[[col for col in score_cols if col in latest.columns]].head(300)
    write_csv(score_latest, SCORE_CSV)
    SCORE_MD.write_text(
        "\n".join(
            [
                "# Surge Model Score Latest",
                "",
                f"generated_at: {now_text()}",
                f"trade_date: {latest_date}",
                "",
                "初版為 rule-based score，等待 mature samples 足夠後才可調整權重。",
                "",
                markdown_table(score_latest.head(50)),
                "",
            ]
        ),
        encoding="utf-8",
    )

    write_csv(importance, FEATURE_IMPORTANCE_CSV)
    FEATURE_IMPORTANCE_MD.write_text(
        "\n".join(
            [
                "# Surge Model Feature Importance Latest",
                "",
                f"generated_at: {now_text()}",
                "",
                "使用可解釋條件統計，比較 mature surge samples 與非暴漲對照母體。樣本不足時不得下正式結論。",
                "",
                markdown_table(importance.head(30)),
                "",
            ]
        ),
        encoding="utf-8",
    )

    write_csv(backtest, BACKTEST_CSV)
    BACKTEST_MD.write_text(
        "\n".join(
            [
                "# Surge Model Backtest Latest",
                "",
                f"generated_at: {now_text()}",
                "",
                "所有回測僅使用 mature_dN=True 的樣本；pending 不視為成功或失敗。",
                "",
                markdown_table(backtest.head(60)),
                "",
            ]
        ),
        encoding="utf-8",
    )

    mature_5 = int(as_bool_series(labels, "mature_5d").sum()) if not labels.empty else 0
    mature_10 = int(as_bool_series(labels, "mature_10d").sum()) if not labels.empty else 0
    mature_20 = int(as_bool_series(labels, "mature_20d").sum()) if not labels.empty else 0
    baseline_5 = as_bool_series(labels[as_bool_series(labels, "mature_5d")], "surge_5d").mean() if mature_5 else 0
    baseline_10 = as_bool_series(labels[as_bool_series(labels, "mature_10d")], "surge_10d").mean() if mature_10 else 0
    baseline_20 = as_bool_series(labels[as_bool_series(labels, "mature_20d")], "surge_20d").mean() if mature_20 else 0

    packet_lines = [
        "# SURGE MODEL CHATGPT PACKET",
        "",
        "## Metadata",
        f"- generated_at: {now_text()}",
        f"- main_price_date: {latest_date}",
        "- surge_definition: surge_5d=future 5d high >= 20%; surge_10d=future 10d high >= 25%; surge_20d=future 20d high >= 35%",
        f"- feature_panel_rows: {len(panel)}",
        f"- mature_5d_count: {mature_5}",
        f"- mature_10d_count: {mature_10}",
        f"- mature_20d_count: {mature_20}",
        f"- baseline_surge_rate_5d: {baseline_5:.4f}",
        f"- baseline_surge_rate_10d: {baseline_10:.4f}",
        f"- baseline_surge_rate_20d: {baseline_20:.4f}",
        "",
        "## Data Availability",
        f"- feature_panel: {FEATURE_PANEL_CSV.exists()}",
        f"- labels: {LABELS_CSV.exists()}",
        f"- pre_surge_event_study: {EVENT_STUDY_CSV.exists()}",
        f"- non_surge_control_sample: {CONTROL_SAMPLE_CSV.exists()}",
        f"- tdcc_snapshot: {TDCC_SNAPSHOT_CSV.exists()}",
        f"- warrant_flow_by_stock: {WARRANT_FLOW_CSV.exists()}",
        f"- market_index_history: {MARKET_INDEX_CSV.exists()}",
        "",
        "## Top Surge Precondition Candidates",
        markdown_table(candidates.head(TOP_PACKET_ROWS)),
        "",
        "## Feature Importance Summary",
        markdown_table(importance.head(20)),
        "",
        "## Backtest Summary",
        markdown_table(backtest.head(40)),
        "",
        "## Risk Summary",
        "- C_too_hot / failed_breakout / high_volume_upper_shadow 不可解讀為暴漲前低位候選。",
        "- 未來資料只用於 label，不可用來產生當日 feature。",
        "- pending 不可視為成功或失敗。",
        "- 樣本不足時標示 insufficient_sample，不做正式調參。",
        "",
        "## Model Tuning Status",
        "tuning_status = not_ready",
        "reason = insufficient mature samples for stable feature/weight tuning",
        "allowed_changes = reporting_priority_only",
        "forbidden_changes = core_weight_change",
        "",
        "## Raw URLs",
        f"- surge_precondition_candidates_md_raw_url: {raw_url(CANDIDATES_MD)}",
        f"- surge_precondition_candidates_csv_raw_url: {raw_url(CANDIDATES_CSV)}",
        f"- surge_model_backtest_md_raw_url: {raw_url(BACKTEST_MD)}",
        f"- surge_model_backtest_csv_raw_url: {raw_url(BACKTEST_CSV)}",
        f"- surge_model_feature_importance_md_raw_url: {raw_url(FEATURE_IMPORTANCE_MD)}",
        f"- surge_model_feature_importance_csv_raw_url: {raw_url(FEATURE_IMPORTANCE_CSV)}",
        "",
    ]
    PACKET_MD.write_text("\n".join(packet_lines), encoding="utf-8")


def main() -> int:
    HISTORY_DIR.mkdir(parents=True, exist_ok=True)
    LATEST_DIR.mkdir(parents=True, exist_ok=True)

    market_index = load_market_index()
    frames: list[pd.DataFrame] = []
    paths = sorted(STOCK_PRICE_HISTORY_DIR.glob("*.csv"))
    for idx, path in enumerate(paths, start=1):
        frame = build_stock_features(path, market_index)
        if not frame.empty:
            frames.append(frame)
        if idx % 250 == 0:
            print(f"processed price histories: {idx}/{len(paths)}")

    if not frames:
        raise RuntimeError("No stock price history available for surge model")

    panel = pd.concat(frames, ignore_index=True, sort=False)
    panel = enrich_panel(panel)
    panel = finalize_columns(panel)
    scored = score_rows(panel)
    labels = build_labels(scored)
    event_study = build_event_study(scored)
    controls = build_control_sample(scored, event_study)
    importance = build_feature_importance(scored, controls)
    backtest = build_backtest(scored)

    feature_export = feature_export_frame(scored)
    labels_export = label_export_frame(labels)
    event_study_export = event_study_export_frame(event_study)
    control_export = event_study_export_frame(controls)

    write_csv(feature_export, FEATURE_PANEL_CSV)
    write_csv(labels_export, LABELS_CSV)
    write_csv(event_study_export, EVENT_STUDY_CSV)
    write_csv(control_export, CONTROL_SAMPLE_CSV)
    write_latest_reports(scored, labels, event_study, controls, importance, scored, backtest)

    print(f"Saved: {FEATURE_PANEL_CSV} rows={len(feature_export)}")
    print(f"Saved: {LABELS_CSV} rows={len(labels_export)}")
    print(f"Saved: {EVENT_STUDY_CSV} rows={len(event_study_export)}")
    print(f"Saved: {CONTROL_SAMPLE_CSV} rows={len(control_export)}")
    print(f"Saved: {PACKET_MD}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
