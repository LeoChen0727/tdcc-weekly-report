from __future__ import annotations

import math
import re
import sys
from functools import lru_cache
from pathlib import Path
from typing import Any

import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent))

from tracking_utils import DOCS_LATEST_DIR, LATEST_DIR, markdown_table, normalize_code, normalize_date, now_text, write_csv  # noqa: E402
from research_tdcc_dataset_consumer import (  # noqa: E402
    build_canonical_tdcc_history,
    load_research_tdcc_dataset_contract,
)


ROOT = Path(__file__).resolve().parents[1]
SIGNAL_SNAPSHOT_DIR = ROOT / "output" / "history" / "daily_model_snapshots"
LATEST_SIGNAL_CSV = LATEST_DIR / "daily_candidate_model_signals_for_report_latest.csv"
PRICE_HISTORY_DIR = ROOT / "data" / "stock_price_history"
MARKET_INDEX_HISTORY_CSV = ROOT / "data" / "market_index_history.csv"
RESEARCH_LATEST_DIR = LATEST_DIR / "research_backtest"
MONTHLY_REVENUE_PIT_PANEL_CSV = RESEARCH_LATEST_DIR / "monthly_revenue_point_in_time_panel_latest.csv"
THEME_STATUS_HISTORY_CSVS = (
    LATEST_DIR / "daily_theme_status_history_latest.csv",
    ROOT / "output" / "history" / "daily_signals" / "daily_theme_status_history.csv",
    ROOT / "output" / "history" / "daily_candidates" / "daily_theme_status_history.csv",
)

PANEL_CSV = RESEARCH_LATEST_DIR / "daily_model_signal_background_feature_panel_latest.csv"
PANEL_MD = RESEARCH_LATEST_DIR / "daily_model_signal_background_feature_panel_latest.md"
CATALOG_CSV = RESEARCH_LATEST_DIR / "daily_model_background_feature_catalog_latest.csv"
CATALOG_MD = RESEARCH_LATEST_DIR / "daily_model_background_feature_catalog_latest.md"

DOCS_PANEL_CSV = DOCS_LATEST_DIR / PANEL_CSV.name
DOCS_PANEL_MD = DOCS_LATEST_DIR / PANEL_MD.name
DOCS_CATALOG_CSV = DOCS_LATEST_DIR / CATALOG_CSV.name
DOCS_CATALOG_MD = DOCS_LATEST_DIR / CATALOG_MD.name

PANEL_ID = "daily_model_signal_background_features_v1"

FORBIDDEN_MODEL_SEMANTIC_COLUMN_PATTERNS = (
    "price_pullback",
    "neckline",
    "w_bottom",
    "volume_range_breakout",
    "buy_filter",
    "entry_rule",
    "exit_rule",
    "stop_rule",
    "win_definition",
    "failure_definition",
    "approved_for_daily",
    "model_score",
    "score_component",
    "risk_tag",
    "gate",
    "recommend",
)


def rel_to_root(path: Path) -> str:
    resolved = path if path.is_absolute() else ROOT / path
    try:
        return resolved.relative_to(ROOT).as_posix()
    except ValueError:
        return path.as_posix()


def blank_if_nan(value: Any, digits: int = 4) -> str | float | int | bool:
    if value is None:
        return ""
    if isinstance(value, bool):
        return value
    try:
        if pd.isna(value):
            return ""
    except TypeError:
        pass
    if isinstance(value, float):
        if math.isnan(value) or math.isinf(value):
            return ""
        return round(value, digits)
    return value


def to_float(value: Any) -> float:
    try:
        out = float(value)
    except (TypeError, ValueError):
        return math.nan
    return out if math.isfinite(out) else math.nan


def pct_change(end_value: float, start_value: float) -> float:
    if math.isnan(end_value) or math.isnan(start_value) or start_value <= 0:
        return math.nan
    return (end_value / start_value - 1.0) * 100.0


def max_drawdown_pct(values: list[float]) -> float:
    peak = -math.inf
    worst = 0.0
    for value in values:
        if math.isnan(value):
            continue
        peak = max(peak, value)
        if peak > 0:
            worst = min(worst, (value / peak - 1.0) * 100.0)
    return worst if peak > 0 else math.nan


def slope_pct_per_20d(values: list[float]) -> float:
    clean = [value for value in values if not math.isnan(value)]
    if len(clean) < 10 or clean[0] <= 0:
        return math.nan
    n = len(clean)
    mean_x = (n - 1) / 2.0
    mean_y = sum(clean) / n
    denom = sum((idx - mean_x) ** 2 for idx in range(n))
    if denom == 0:
        return math.nan
    slope = sum((idx - mean_x) * (value - mean_y) for idx, value in enumerate(clean)) / denom
    return slope * 20.0 / clean[0] * 100.0


def window_stats(prior: pd.DataFrame, current_close: float, window: int) -> dict[str, Any]:
    window_df = prior.tail(window).copy()
    prefix = f"pre{window}"
    if window_df.empty:
        return {
            f"{prefix}_sessions": 0,
            f"{prefix}_return_pct": "",
            f"{prefix}_range_high": "",
            f"{prefix}_range_low": "",
            f"{prefix}_range_width_pct": "",
            f"{prefix}_close_position_pct": "",
            f"{prefix}_distance_to_high_pct": "",
            f"{prefix}_drawdown_pct": "",
            f"{prefix}_slope20_pct": "",
        }

    highs = pd.to_numeric(window_df["high"], errors="coerce").dropna()
    lows = pd.to_numeric(window_df["low"], errors="coerce").dropna()
    closes = pd.to_numeric(window_df["close"], errors="coerce").dropna().tolist()
    high = float(highs.max()) if len(highs) else math.nan
    low = float(lows.min()) if len(lows) else math.nan
    width = pct_change(high, low)
    position = ((current_close - low) / (high - low) * 100.0) if not any(math.isnan(v) for v in [current_close, high, low]) and high != low else math.nan
    return {
        f"{prefix}_sessions": len(window_df),
        f"{prefix}_return_pct": blank_if_nan(pct_change(closes[-1], closes[0]) if len(closes) >= 2 else math.nan),
        f"{prefix}_range_high": blank_if_nan(high),
        f"{prefix}_range_low": blank_if_nan(low),
        f"{prefix}_range_width_pct": blank_if_nan(width),
        f"{prefix}_close_position_pct": blank_if_nan(position),
        f"{prefix}_distance_to_high_pct": blank_if_nan(pct_change(current_close, high)),
        f"{prefix}_drawdown_pct": blank_if_nan(max_drawdown_pct(closes)),
        f"{prefix}_slope20_pct": blank_if_nan(slope_pct_per_20d(closes)),
    }


def read_csv_safely(path: Path, **kwargs: Any) -> pd.DataFrame:
    try:
        return pd.read_csv(path, **kwargs)
    except (OSError, ValueError, pd.errors.ParserError):
        return pd.DataFrame()


def normalize_stock_id(value: Any) -> str:
    return normalize_code(value)


def signal_snapshot_date(path: Path) -> str:
    match = re.search(r"_(\d{8})\.csv$", path.name)
    return match.group(1) if match else "latest"


def load_signal_universe(
    snapshot_dir: Path = SIGNAL_SNAPSHOT_DIR,
    latest_signal_csv: Path = LATEST_SIGNAL_CSV,
) -> pd.DataFrame:
    frames: list[pd.DataFrame] = []
    for path in sorted(snapshot_dir.glob("daily_candidate_model_signals_for_report_*.csv")):
        df = read_csv_safely(path, dtype=str, keep_default_na=False)
        if df.empty:
            continue
        df = df.copy()
        df["source_snapshot_date"] = signal_snapshot_date(path)
        df["source_snapshot_file"] = rel_to_root(path)
        frames.append(df)

    if latest_signal_csv.exists():
        latest = read_csv_safely(latest_signal_csv, dtype=str, keep_default_na=False)
        if not latest.empty:
            latest = latest.copy()
            latest["source_snapshot_date"] = "latest"
            latest["source_snapshot_file"] = rel_to_root(latest_signal_csv)
            frames.append(latest)

    if not frames:
        return pd.DataFrame()

    raw = pd.concat(frames, ignore_index=True).fillna("")
    raw["stock_id"] = raw.get("stock_id", "").map(normalize_stock_id)
    raw["signal_date"] = raw.apply(lambda row: normalize_date(row.get("signal_date") or row.get("as_of_date") or row.get("date")), axis=1)
    raw["stock_name"] = raw.get("stock_name", "")
    raw["model_id"] = raw.get("model_id", "")
    raw = raw[(raw["stock_id"] != "") & (raw["signal_date"] != "")]
    if raw.empty:
        return pd.DataFrame()

    grouped = (
        raw.groupby(["stock_id", "signal_date"], dropna=False)
        .agg(
            stock_name=("stock_name", lambda s: next((str(v) for v in s if str(v).strip()), "")),
            source_model_ids=("model_id", lambda s: ";".join(sorted({str(v).strip() for v in s if str(v).strip()}))),
            source_snapshot_dates=("source_snapshot_date", lambda s: ";".join(sorted({str(v).strip() for v in s if str(v).strip()}))),
            source_snapshot_files=("source_snapshot_file", lambda s: ";".join(sorted({str(v).strip() for v in s if str(v).strip()}))),
            source_signal_rows=("stock_id", "size"),
        )
        .reset_index()
    )
    return grouped.sort_values(["signal_date", "stock_id"]).reset_index(drop=True)


@lru_cache(maxsize=4096)
def load_price_history(stock_id: str, price_dir_text: str = str(PRICE_HISTORY_DIR)) -> pd.DataFrame:
    path = Path(price_dir_text) / f"{normalize_stock_id(stock_id)}.csv"
    df = read_csv_safely(path, dtype={"stock_id": str}, keep_default_na=False)
    required = {"date", "open", "high", "low", "close", "volume"}
    if df.empty or not required.issubset(df.columns):
        return pd.DataFrame()
    out = df.copy()
    out["date"] = out["date"].map(normalize_date)
    for col in ["open", "high", "low", "close", "volume"]:
        out[col] = pd.to_numeric(out[col], errors="coerce")
    out = out.dropna(subset=["date", "open", "high", "low", "close"]).sort_values("date")
    return out.reset_index(drop=True)


@lru_cache(maxsize=1)
def load_canonical_tdcc_history() -> pd.DataFrame:
    return build_canonical_tdcc_history(load_research_tdcc_dataset_contract())


@lru_cache(maxsize=4096)
def load_tdcc_history(stock_id: str) -> pd.DataFrame:
    df = load_canonical_tdcc_history()
    if df.empty or "as_of_date" not in df.columns:
        return pd.DataFrame()
    out = df[df["stock_id"].astype(str).eq(normalize_stock_id(stock_id))].copy()
    if out.empty:
        return out
    out["tdcc_as_of_date"] = out["as_of_date"].map(normalize_date)
    for col in [
        "tdcc_consecutive_up_weeks",
        "over_400_ratio",
        "over_400_change_1w",
        "over_400_change_2w",
        "over_400_change_3w",
        "over_600_ratio",
        "over_600_change_1w",
        "over_800_ratio",
        "over_800_change_1w",
        "over_1000_ratio",
        "over_1000_change_1w",
        "over_1000_change_2w",
        "over_1000_change_3w",
    ]:
        if col in out.columns:
            out[col] = pd.to_numeric(out[col], errors="coerce")
    return out[out["tdcc_as_of_date"] != ""].sort_values("tdcc_as_of_date").reset_index(drop=True)


@lru_cache(maxsize=1)
def load_market_index_history(path_text: str = str(MARKET_INDEX_HISTORY_CSV)) -> pd.DataFrame:
    df = read_csv_safely(Path(path_text), dtype=str, keep_default_na=False)
    if df.empty or not {"date", "index_code"}.issubset(df.columns):
        return pd.DataFrame()
    out = df.copy()
    out["date"] = out["date"].map(normalize_date)
    out["index_code"] = out["index_code"].astype(str).str.upper()
    for col in ["close", "return_5d", "return_10d", "return_20d", "return_60d", "ma20", "ma60"]:
        if col in out.columns:
            out[col] = pd.to_numeric(out[col], errors="coerce")
    return out[out["date"] != ""].sort_values(["index_code", "date"]).reset_index(drop=True)


def _bool_value(value: Any) -> bool | str:
    text = str(value).strip().lower()
    if text in {"true", "1", "yes"}:
        return True
    if text in {"false", "0", "no"}:
        return False
    return ""


def load_theme_status_history(paths: tuple[Path, ...] = THEME_STATUS_HISTORY_CSVS) -> pd.DataFrame:
    frames: list[pd.DataFrame] = []
    for order, path in enumerate(paths):
        df = read_csv_safely(path, dtype=str, keep_default_na=False)
        if df.empty or not {"stock_id", "signal_date"}.issubset(df.columns):
            continue
        frame = df.copy()
        frame["theme_context_source_artifact"] = rel_to_root(path)
        frame["theme_context_source_order"] = order
        frames.append(frame)
    if not frames:
        return pd.DataFrame()

    out = pd.concat(frames, ignore_index=True).fillna("")
    out["stock_id"] = out["stock_id"].map(normalize_stock_id)
    out["signal_date"] = out["signal_date"].map(normalize_date)
    out = out[(out["stock_id"] != "") & (out["signal_date"] != "")]
    for col in ["presentation_priority", "volume_ratio", "return_20d"]:
        if col in out.columns:
            out[col] = pd.to_numeric(out[col], errors="coerce")
    for col in [
        "two_line_overlap_flag",
        "is_volume_attack_selected",
        "is_volume_attack_watch",
        "is_volume_attack_failed",
    ]:
        if col in out.columns:
            out[col] = out[col].map(_bool_value)
    return (
        out.sort_values(["stock_id", "signal_date", "theme_context_source_order"])
        .drop_duplicates(["stock_id", "signal_date"], keep="last")
        .reset_index(drop=True)
    )


@lru_cache(maxsize=1)
def load_monthly_revenue_pit_panel(path_text: str = str(MONTHLY_REVENUE_PIT_PANEL_CSV)) -> pd.DataFrame:
    df = read_csv_safely(Path(path_text), dtype=str, keep_default_na=False)
    required = {"stock_id", "observed_as_of_date", "research_join_allowed"}
    if df.empty or not required.issubset(df.columns):
        return pd.DataFrame()
    out = df.copy()
    out["stock_id"] = out["stock_id"].map(normalize_stock_id)
    out["observed_as_of_date"] = out["observed_as_of_date"].map(normalize_date)
    for col in ["latest_revenue_yoy_pct", "cumulative_revenue_yoy_pct"]:
        if col in out.columns:
            out[col] = pd.to_numeric(out[col], errors="coerce")
    return out[out["stock_id"].ne("") & out["observed_as_of_date"].ne("")].sort_values(
        ["stock_id", "observed_as_of_date", "revenue_period"]
    )


def asof_market_features(signal_date: str, market_df: pd.DataFrame | None = None) -> dict[str, Any]:
    market = load_market_index_history() if market_df is None else market_df
    features: dict[str, Any] = {
        "market_index_as_of_date": "",
        "twse_close": "",
        "twse_return_5d_pct": "",
        "twse_return_20d_pct": "",
        "twse_above_ma20": "",
        "twse_above_ma60": "",
        "tpex_close": "",
        "tpex_return_5d_pct": "",
        "tpex_return_20d_pct": "",
        "tpex_above_ma20": "",
        "tpex_above_ma60": "",
    }
    if market.empty:
        return features

    asof_dates: list[str] = []
    for code, prefix in [("TWSE", "twse"), ("TPEX", "tpex")]:
        part = market[market["index_code"].eq(code)]
        part = part[part["date"].astype(str) <= signal_date]
        if part.empty:
            continue
        row = part.iloc[-1]
        asof_dates.append(str(row.get("date", "")))
        features[f"{prefix}_close"] = blank_if_nan(to_float(row.get("close")))
        features[f"{prefix}_return_5d_pct"] = blank_if_nan(to_float(row.get("return_5d")))
        features[f"{prefix}_return_20d_pct"] = blank_if_nan(to_float(row.get("return_20d")))
        for ma_col in ["above_ma20", "above_ma60"]:
            value = str(row.get(ma_col, "")).strip().lower()
            features[f"{prefix}_{ma_col}"] = value in {"true", "1", "yes"}
    features["market_index_as_of_date"] = max(asof_dates) if asof_dates else ""
    return features


def revenue_background_features(
    stock_id: str,
    signal_date: str,
    revenue_panel: pd.DataFrame | None = None,
) -> dict[str, Any]:
    panel = load_monthly_revenue_pit_panel() if revenue_panel is None else revenue_panel
    features: dict[str, Any] = {
        "monthly_revenue_context_as_of_date": "",
        "monthly_revenue_rows_as_of": 0,
        "monthly_revenue_future_rows_ignored": 0,
        "monthly_revenue_data_status": "missing_monthly_revenue_pit_panel",
        "monthly_revenue_period": "",
        "monthly_revenue_latest_yoy_pct": "",
        "monthly_revenue_cumulative_yoy_pct": "",
        "monthly_revenue_positive_flag": "",
        "monthly_revenue_strong_flag": "",
        "monthly_revenue_good_eps_unconfirmed_flag": "",
        "monthly_revenue_numerical_anomaly_flag": "",
        "monthly_revenue_source_artifact": "",
        "monthly_revenue_formal_model_use_allowed": False,
    }
    if panel is None or panel.empty:
        return features

    stock_rows = panel[panel["stock_id"].astype(str).eq(normalize_stock_id(stock_id))].copy()
    if stock_rows.empty:
        features["monthly_revenue_data_status"] = "no_revenue_on_or_before_signal"
        return features

    stock_rows["observed_as_of_date"] = stock_rows["observed_as_of_date"].map(normalize_date)
    features["monthly_revenue_future_rows_ignored"] = int(
        (stock_rows["observed_as_of_date"].astype(str) > signal_date).sum()
    )
    asof = stock_rows[
        stock_rows["observed_as_of_date"].astype(str).le(signal_date)
        & stock_rows["research_join_allowed"].astype(str).eq("True")
    ].copy()
    if asof.empty:
        features["monthly_revenue_data_status"] = "no_revenue_on_or_before_signal"
        return features

    row = asof.sort_values(["observed_as_of_date", "revenue_period"]).iloc[-1]
    asof_date = str(row.get("observed_as_of_date", ""))
    features.update(
        {
            "monthly_revenue_context_as_of_date": asof_date,
            "monthly_revenue_rows_as_of": len(asof),
            "monthly_revenue_data_status": "ready_exact_signal_date"
            if asof_date == signal_date
            else "ready_previous_snapshot_date",
            "monthly_revenue_period": row.get("revenue_period", ""),
            "monthly_revenue_latest_yoy_pct": blank_if_nan(to_float(row.get("latest_revenue_yoy_pct"))),
            "monthly_revenue_cumulative_yoy_pct": blank_if_nan(to_float(row.get("cumulative_revenue_yoy_pct"))),
            "monthly_revenue_positive_flag": _bool_value(row.get("revenue_positive_flag", "")),
            "monthly_revenue_strong_flag": _bool_value(row.get("revenue_strong_flag", "")),
            "monthly_revenue_good_eps_unconfirmed_flag": _bool_value(
                row.get("revenue_good_eps_unconfirmed_flag", "")
            ),
            "monthly_revenue_numerical_anomaly_flag": _bool_value(row.get("revenue_numerical_anomaly_flag", "")),
            "monthly_revenue_source_artifact": row.get("source_snapshot_files", ""),
            "monthly_revenue_formal_model_use_allowed": _bool_value(
                row.get("allowed_for_formal_historical_model_use", "")
            )
            is True,
        }
    )
    return features


def technical_features(price: pd.DataFrame) -> dict[str, Any]:
    close = pd.to_numeric(price["close"], errors="coerce")
    high = pd.to_numeric(price["high"], errors="coerce")
    low = pd.to_numeric(price["low"], errors="coerce")
    volume = pd.to_numeric(price["volume"], errors="coerce").fillna(0.0)
    groups = pd.Series(["x"] * len(price), index=price.index)

    ma20 = close.rolling(20, min_periods=20).mean()
    ma60 = close.rolling(60, min_periods=60).mean()
    ema12 = close.ewm(span=12, adjust=False, min_periods=12).mean()
    ema23 = close.ewm(span=23, adjust=False, min_periods=23).mean()
    ema26 = close.ewm(span=26, adjust=False, min_periods=26).mean()
    macd_dif = ema12 - ema26
    macd_dea = macd_dif.ewm(span=9, adjust=False, min_periods=9).mean()
    macd_hist = macd_dif - macd_dea

    delta = close.diff()
    gain = delta.clip(lower=0)
    loss = -delta.clip(upper=0)
    avg_gain = gain.rolling(14, min_periods=14).mean()
    avg_loss = loss.rolling(14, min_periods=14).mean()
    rs = avg_gain / avg_loss.replace(0, pd.NA)
    rsi14 = 100 - (100 / (1 + rs))
    rsi14 = rsi14.mask((avg_loss == 0) & (avg_gain > 0), 100.0)
    rsi14 = rsi14.mask((avg_loss == 0) & (avg_gain == 0), 50.0)

    low9 = low.rolling(9, min_periods=9).min()
    high9 = high.rolling(9, min_periods=9).max()
    rsv9 = (close - low9) / (high9 - low9).replace(0, pd.NA) * 100.0
    k_value = rsv9.ewm(alpha=1 / 3, adjust=False, min_periods=3).mean()
    d_value = k_value.ewm(alpha=1 / 3, adjust=False, min_periods=3).mean()

    obv_direction = (close - close.shift(1)).apply(lambda value: 1.0 if value > 0 else (-1.0 if value < 0 else 0.0)).fillna(0.0)
    obv = (obv_direction * volume).cumsum()
    obv_ma20 = obv.rolling(20, min_periods=10).mean()
    obv_slope_5d = obv - obv.shift(5)

    bb_std = close.rolling(20, min_periods=20).std()
    bb_width_pct = (4 * bb_std / ma20) * 100.0
    bb_width_pct_rank_120d = bb_width_pct.rolling(120, min_periods=60).rank(pct=True)

    idx = price.index[-1]
    current_close = to_float(close.iloc[-1])
    current_ema23 = to_float(ema23.iloc[-1])
    current_ma20 = to_float(ma20.iloc[-1])
    current_ma60 = to_float(ma60.iloc[-1])

    # Keep group variable referenced so static analysis does not mistake this
    # function for a per-model transformation; all calculations are stock-local.
    _ = groups

    return {
        "ma20": blank_if_nan(current_ma20),
        "ma60": blank_if_nan(current_ma60),
        "ema23": blank_if_nan(current_ema23),
        "distance_to_ma20_pct": blank_if_nan(pct_change(current_close, current_ma20)),
        "distance_to_ma60_pct": blank_if_nan(pct_change(current_close, current_ma60)),
        "distance_to_ema23_pct": blank_if_nan(pct_change(current_close, current_ema23)),
        "ema23_slope_5d_pct": blank_if_nan(pct_change(current_ema23, to_float(ema23.shift(5).iloc[-1]))),
        "macd_dif": blank_if_nan(to_float(macd_dif.loc[idx])),
        "macd_dea": blank_if_nan(to_float(macd_dea.loc[idx])),
        "macd_hist": blank_if_nan(to_float(macd_hist.loc[idx])),
        "rsi14": blank_if_nan(to_float(rsi14.loc[idx])),
        "kd_k_value": blank_if_nan(to_float(k_value.loc[idx])),
        "kd_d_value": blank_if_nan(to_float(d_value.loc[idx])),
        "kd_k_minus_d": blank_if_nan(to_float(k_value.loc[idx]) - to_float(d_value.loc[idx])),
        "obv": blank_if_nan(to_float(obv.loc[idx])),
        "obv_ma20": blank_if_nan(to_float(obv_ma20.loc[idx])),
        "obv_slope_5d": blank_if_nan(to_float(obv_slope_5d.loc[idx])),
        "bb_width_pct": blank_if_nan(to_float(bb_width_pct.loc[idx])),
        "bb_width_pct_rank_120d": blank_if_nan(to_float(bb_width_pct_rank_120d.loc[idx])),
    }


def price_background_features(stock_id: str, signal_date: str, price_dir: Path = PRICE_HISTORY_DIR) -> dict[str, Any]:
    full = load_price_history(stock_id, str(price_dir))
    base = {
        "feature_as_of_date": "",
        "price_history_max_date": str(full["date"].max()) if not full.empty and "date" in full.columns else "",
        "price_history_rows_as_of": 0,
        "future_price_rows_ignored": 0,
        "point_in_time_status": "missing_price_history",
        "open": "",
        "high": "",
        "low": "",
        "close": "",
        "volume": "",
    }
    if full.empty:
        return base

    asof = full[full["date"].astype(str) <= signal_date].copy()
    base["future_price_rows_ignored"] = int((full["date"].astype(str) > signal_date).sum())
    if asof.empty:
        base["point_in_time_status"] = "no_price_on_or_before_signal"
        return base

    asof = asof.sort_values("date").reset_index(drop=True)
    current = asof.iloc[-1]
    prior = asof.iloc[:-1].copy()
    current_close = to_float(current.get("close"))
    previous_close = to_float(prior.iloc[-1].get("close")) if not prior.empty else math.nan
    volume_ma20_prev = pd.to_numeric(prior["volume"], errors="coerce").tail(20).mean() if len(prior) >= 20 else math.nan
    candle_range = to_float(current.get("high")) - to_float(current.get("low"))
    candle_range = candle_range if candle_range > 0 else math.nan

    base.update(
        {
            "feature_as_of_date": str(current.get("date", "")),
            "price_history_rows_as_of": len(asof),
            "point_in_time_status": "exact_signal_date" if str(current.get("date", "")) == signal_date else "used_previous_trading_day",
            "open": blank_if_nan(to_float(current.get("open"))),
            "high": blank_if_nan(to_float(current.get("high"))),
            "low": blank_if_nan(to_float(current.get("low"))),
            "close": blank_if_nan(current_close),
            "volume": blank_if_nan(to_float(current.get("volume")), digits=2),
            "signal_return_1d_pct": blank_if_nan(pct_change(current_close, previous_close)),
            "volume_ratio_prev20": blank_if_nan(to_float(current.get("volume")) / volume_ma20_prev if volume_ma20_prev and not math.isnan(volume_ma20_prev) else math.nan),
            "close_above_open": to_float(current.get("close")) > to_float(current.get("open")),
            "body_ratio": blank_if_nan(abs(to_float(current.get("close")) - to_float(current.get("open"))) / candle_range if not math.isnan(candle_range) else math.nan),
            "upper_shadow_ratio": blank_if_nan((to_float(current.get("high")) - max(to_float(current.get("close")), to_float(current.get("open")))) / candle_range if not math.isnan(candle_range) else math.nan),
            "close_location": blank_if_nan((to_float(current.get("close")) - to_float(current.get("low"))) / candle_range if not math.isnan(candle_range) else math.nan),
        }
    )

    close_series = pd.to_numeric(asof["close"], errors="coerce")
    for window in [20, 45, 90]:
        if len(close_series) > window:
            base[f"close_return_{window}d_pct"] = blank_if_nan(pct_change(float(close_series.iloc[-1]), float(close_series.iloc[-1 - window])))
        else:
            base[f"close_return_{window}d_pct"] = ""
        base.update(window_stats(prior, current_close, window))

    base.update(technical_features(asof))
    return base


def tdcc_background_features(
    stock_id: str,
    signal_date: str,
    tdcc_history: pd.DataFrame | None = None,
    source_tdcc_dataset_id: str | None = None,
) -> dict[str, Any]:
    if tdcc_history is None:
        contract = load_research_tdcc_dataset_contract()
        source_tdcc_dataset_id = contract.dataset_id
        full = load_tdcc_history(stock_id)
    else:
        full = tdcc_history.copy()
        if "tdcc_as_of_date" not in full.columns and "as_of_date" in full.columns:
            full["tdcc_as_of_date"] = full["as_of_date"].map(normalize_date)
    features: dict[str, Any] = {
        "source_tdcc_dataset_id": source_tdcc_dataset_id or "",
        "tdcc_as_of_date": "",
        "tdcc_rows_as_of": 0,
        "tdcc_future_rows_ignored": 0,
        "tdcc_data_status": "missing_tdcc_history",
        "tdcc_continuity_status": "",
        "tdcc_missing_official_dates": "",
        "tdcc_consecutive_up_weeks": "",
        "tdcc_over_400_ratio": "",
        "tdcc_over_400_change_1w": "",
        "tdcc_over_400_change_3w": "",
        "tdcc_over_600_ratio": "",
        "tdcc_over_600_change_1w": "",
        "tdcc_over_800_ratio": "",
        "tdcc_over_800_change_1w": "",
        "tdcc_over_1000_ratio": "",
        "tdcc_over_1000_change_1w": "",
        "tdcc_over_1000_change_3w": "",
    }
    if full.empty:
        return features
    features["tdcc_future_rows_ignored"] = int((full["tdcc_as_of_date"].astype(str) > signal_date).sum())
    asof = full[full["tdcc_as_of_date"].astype(str) <= signal_date].copy()
    if asof.empty:
        features["tdcc_data_status"] = "no_tdcc_on_or_before_signal"
        return features
    row = asof.iloc[-1]
    features["tdcc_as_of_date"] = str(row.get("tdcc_as_of_date", ""))
    features["tdcc_rows_as_of"] = len(asof)
    features["tdcc_data_status"] = "ready"
    features["tdcc_continuity_status"] = str(row.get("tdcc_continuity_status", ""))
    features["tdcc_missing_official_dates"] = str(row.get("tdcc_missing_official_dates", ""))
    mapping = {
        "tdcc_consecutive_up_weeks": "tdcc_consecutive_up_weeks",
        "tdcc_over_400_ratio": "over_400_ratio",
        "tdcc_over_400_change_1w": "over_400_change_1w",
        "tdcc_over_400_change_3w": "over_400_change_3w",
        "tdcc_over_600_ratio": "over_600_ratio",
        "tdcc_over_600_change_1w": "over_600_change_1w",
        "tdcc_over_800_ratio": "over_800_ratio",
        "tdcc_over_800_change_1w": "over_800_change_1w",
        "tdcc_over_1000_ratio": "over_1000_ratio",
        "tdcc_over_1000_change_1w": "over_1000_change_1w",
        "tdcc_over_1000_change_3w": "over_1000_change_3w",
    }
    for out_col, source_col in mapping.items():
        features[out_col] = blank_if_nan(to_float(row.get(source_col)))
    return features


def theme_background_features(stock_id: str, signal_date: str, theme_history: pd.DataFrame | None = None) -> dict[str, Any]:
    history = load_theme_status_history() if theme_history is None else theme_history
    features: dict[str, Any] = {
        "theme_context_as_of_date": "",
        "theme_context_rows_as_of": 0,
        "theme_context_future_rows_ignored": 0,
        "theme_context_data_status": "missing_theme_status_history",
        "theme_context_name": "",
        "theme_context_final_status": "",
        "theme_context_status_group": "",
        "theme_context_source_type": "",
        "theme_context_line_group": "",
        "theme_context_line": "",
        "theme_context_two_line_overlap": "",
        "theme_context_priority": "",
        "theme_context_tdcc_status": "",
        "theme_context_warrant_flow_signal": "",
        "theme_context_volume_ratio": "",
        "theme_context_return_20d_pct": "",
        "theme_context_repeat_label": "",
        "theme_context_volume_breakout_type": "",
        "theme_context_volume_bucket": "",
        "theme_context_volume_attack_status": "",
        "theme_context_volume_attack_selected": "",
        "theme_context_volume_attack_watch": "",
        "theme_context_volume_attack_failed": "",
        "theme_context_source_artifact": "",
    }
    if history is None or history.empty:
        return features

    stock_rows = history[history["stock_id"].astype(str).eq(normalize_stock_id(stock_id))].copy()
    if stock_rows.empty:
        features["theme_context_data_status"] = "no_theme_on_or_before_signal"
        return features

    features["theme_context_future_rows_ignored"] = int((stock_rows["signal_date"].astype(str) > signal_date).sum())
    asof = stock_rows[stock_rows["signal_date"].astype(str) <= signal_date].copy()
    if asof.empty:
        features["theme_context_data_status"] = "no_theme_on_or_before_signal"
        return features

    row = asof.iloc[-1]
    asof_date = str(row.get("signal_date", ""))
    features.update(
        {
            "theme_context_as_of_date": asof_date,
            "theme_context_rows_as_of": len(asof),
            "theme_context_data_status": "ready_exact_signal_date"
            if asof_date == signal_date
            else "ready_previous_signal_date",
            "theme_context_name": row.get("theme_name", ""),
            "theme_context_final_status": row.get("theme_final_status", ""),
            "theme_context_status_group": row.get("theme_status_group", ""),
            "theme_context_source_type": row.get("candidate_source_type", ""),
            "theme_context_line_group": row.get("candidate_line_group", ""),
            "theme_context_line": row.get("candidate_line", ""),
            "theme_context_two_line_overlap": _bool_value(row.get("two_line_overlap_flag", "")),
            "theme_context_priority": blank_if_nan(to_float(row.get("presentation_priority"))),
            "theme_context_tdcc_status": row.get("tdcc_status", ""),
            "theme_context_warrant_flow_signal": row.get("warrant_flow_signal", ""),
            "theme_context_volume_ratio": blank_if_nan(to_float(row.get("volume_ratio"))),
            "theme_context_return_20d_pct": blank_if_nan(to_float(row.get("return_20d"))),
            "theme_context_repeat_label": row.get("repeat_appear_label", ""),
            "theme_context_volume_breakout_type": row.get("volume_breakout_type", ""),
            "theme_context_volume_bucket": row.get("volume_attack_bucket", ""),
            "theme_context_volume_attack_status": row.get("theme_volume_attack_status", ""),
            "theme_context_volume_attack_selected": _bool_value(row.get("is_volume_attack_selected", "")),
            "theme_context_volume_attack_watch": _bool_value(row.get("is_volume_attack_watch", "")),
            "theme_context_volume_attack_failed": _bool_value(row.get("is_volume_attack_failed", "")),
            "theme_context_source_artifact": row.get("theme_context_source_artifact", ""),
        }
    )
    return features


def build_feature_panel(signals: pd.DataFrame | None = None) -> pd.DataFrame:
    signal_rows = load_signal_universe() if signals is None else signals.copy()
    if signal_rows.empty:
        return pd.DataFrame()

    generated_at = now_text()
    rows: list[dict[str, Any]] = []
    market_cache: dict[str, dict[str, Any]] = {}
    theme_history = load_theme_status_history()
    revenue_panel = load_monthly_revenue_pit_panel()
    tdcc_contract = load_research_tdcc_dataset_contract()
    tdcc_history = load_canonical_tdcc_history()
    for _, signal in signal_rows.iterrows():
        stock_id = normalize_stock_id(signal.get("stock_id"))
        signal_date = normalize_date(signal.get("signal_date"))
        market_cache.setdefault(signal_date, asof_market_features(signal_date))
        row = {
            "generated_at": generated_at,
            "feature_panel_id": PANEL_ID,
            "feature_scope": "shared_objective_point_in_time",
            "stock_id": stock_id,
            "stock_name": signal.get("stock_name", ""),
            "signal_date": signal_date,
            "source_model_ids": signal.get("source_model_ids", ""),
            "source_snapshot_dates": signal.get("source_snapshot_dates", ""),
            "source_snapshot_files": signal.get("source_snapshot_files", ""),
            "source_signal_rows": signal.get("source_signal_rows", ""),
        }
        row.update(price_background_features(stock_id, signal_date))
        stock_tdcc_history = tdcc_history[
            tdcc_history["stock_id"].astype(str).eq(stock_id)
        ].copy()
        row.update(
            tdcc_background_features(
                stock_id,
                signal_date,
                tdcc_history=stock_tdcc_history,
                source_tdcc_dataset_id=tdcc_contract.dataset_id,
            )
        )
        row.update(revenue_background_features(stock_id, signal_date, revenue_panel))
        row.update(theme_background_features(stock_id, signal_date, theme_history))
        row.update(market_cache[signal_date])
        rows.append({key: blank_if_nan(value) for key, value in row.items()})

    return pd.DataFrame(rows).sort_values(["signal_date", "stock_id"]).reset_index(drop=True)


def feature_catalog(panel: pd.DataFrame) -> pd.DataFrame:
    metadata = {
        "generated_at",
        "feature_panel_id",
        "feature_scope",
        "stock_id",
        "stock_name",
        "signal_date",
        "source_model_ids",
        "source_tdcc_dataset_id",
        "source_snapshot_dates",
        "source_snapshot_files",
        "source_signal_rows",
    }
    families = {
        "pre": "price_context",
        "close_return": "price_context",
        "distance": "price_context",
        "ema23": "technical_price",
        "ma20": "technical_price",
        "ma60": "technical_price",
        "macd": "technical_indicator",
        "rsi": "technical_indicator",
        "kd": "technical_indicator",
        "obv": "technical_indicator",
        "bb": "technical_indicator",
        "tdcc": "holder_flow",
        "monthly_revenue": "revenue",
        "theme_context": "theme_status_history",
        "twse": "market_index",
        "tpex": "market_index",
        "market_index": "market_index",
    }
    rows: list[dict[str, Any]] = []
    for column in panel.columns:
        if column in metadata:
            family = "metadata"
        else:
            family = next((value for prefix, value in families.items() if column.startswith(prefix)), "price_ohlcv")
        rows.append(
            {
                "generated_at": now_text(),
                "feature_column": column,
                "feature_family": family,
                "feature_scope": "metadata" if family == "metadata" else "shared_objective_point_in_time",
                "allowed_use": "research_background_only_not_a_model_gate_or_score",
                "model_specific_owner": "",
                "point_in_time_rule": "use rows available on or before signal_date",
            }
        )

    rows.extend(
        [
            {
                "generated_at": now_text(),
                "feature_column": "monthly_revenue_point_in_time_panel",
                "feature_family": "revenue",
                "feature_scope": "shared_objective_point_in_time",
                "allowed_use": "research_background_only_coverage_limited_not_a_required_model_gate",
                "model_specific_owner": "",
                "point_in_time_rule": "use observed_as_of_date on or before signal_date; reported release date is not complete",
            },
            {
                "generated_at": now_text(),
                "feature_column": "price_pullback_23ema_operation_filter",
                "feature_family": "model_specific_interpretation",
                "feature_scope": "model_specific_not_in_shared_panel",
                "allowed_use": "price_pullback_23ema_only_after_explicit_research_and_promotion",
                "model_specific_owner": "price_pullback_23ema",
                "point_in_time_rule": "must consume shared objective columns without rewriting shared semantics",
            },
            {
                "generated_at": now_text(),
                "feature_column": "neckline_45d_non_bearish_filter",
                "feature_family": "model_specific_interpretation",
                "feature_scope": "model_specific_not_in_shared_panel",
                "allowed_use": "neckline_volume_breakout_confirmation_only",
                "model_specific_owner": "neckline_volume_breakout_confirmation",
                "point_in_time_rule": "must not be reused as a price_pullback_23ema gate",
            },
        ]
    )
    return pd.DataFrame(rows)


def validate_no_model_semantic_columns(columns: list[str]) -> None:
    offenders = [
        column
        for column in columns
        for pattern in FORBIDDEN_MODEL_SEMANTIC_COLUMN_PATTERNS
        if pattern in column.lower()
    ]
    if offenders:
        raise RuntimeError(f"shared background feature panel contains model-semantic columns: {sorted(set(offenders))}")


def write_markdown(panel: pd.DataFrame, catalog: pd.DataFrame) -> None:
    status_counts = (
        panel.groupby("point_in_time_status", dropna=False)
        .size()
        .reset_index(name="rows")
        .sort_values(["point_in_time_status"])
        if not panel.empty and "point_in_time_status" in panel.columns
        else pd.DataFrame(columns=["point_in_time_status", "rows"])
    )
    tdcc_counts = (
        panel.groupby("tdcc_data_status", dropna=False)
        .size()
        .reset_index(name="rows")
        .sort_values(["tdcc_data_status"])
        if not panel.empty and "tdcc_data_status" in panel.columns
        else pd.DataFrame(columns=["tdcc_data_status", "rows"])
    )
    theme_counts = (
        panel.groupby("theme_context_data_status", dropna=False)
        .size()
        .reset_index(name="rows")
        .sort_values(["theme_context_data_status"])
        if not panel.empty and "theme_context_data_status" in panel.columns
        else pd.DataFrame(columns=["theme_context_data_status", "rows"])
    )
    family_counts = (
        catalog.groupby(["feature_scope", "feature_family"], dropna=False)
        .size()
        .reset_index(name="columns")
        .sort_values(["feature_scope", "feature_family"])
        if not catalog.empty
        else pd.DataFrame(columns=["feature_scope", "feature_family", "columns"])
    )
    lines = [
        "# Daily Model Signal Background Feature Panel",
        "",
        f"- generated_at: `{now_text()}`",
        f"- feature_panel_id: `{PANEL_ID}`",
        f"- source_tdcc_dataset_id: `{panel['source_tdcc_dataset_id'].iloc[0] if not panel.empty else ''}`",
        "- owner: `research_backtest`",
        "- scope: shared objective point-in-time background features for model research discussion.",
        "- non_goal: not a production gate, not a score, not a recommendation, not a model-specific filter.",
        "- model_specific_boundary: price_pullback_23ema, neckline, W-bottom, and volume-breakout interpretations must stay outside this shared panel.",
        "- revenue_status: coverage-limited monthly revenue PIT context is joined from daily snapshot-observed rows; it remains research-only and cannot be a formal gate.",
        "",
        "## Coverage",
        "",
        markdown_table(status_counts, ["point_in_time_status", "rows"]) if not status_counts.empty else "No price coverage rows.",
        "",
        markdown_table(tdcc_counts, ["tdcc_data_status", "rows"]) if not tdcc_counts.empty else "No TDCC coverage rows.",
        "",
        markdown_table(theme_counts, ["theme_context_data_status", "rows"])
        if not theme_counts.empty
        else "No theme context coverage rows.",
        "",
        "## Feature Families",
        "",
        markdown_table(family_counts, ["feature_scope", "feature_family", "columns"]) if not family_counts.empty else "No catalog rows.",
        "",
        "## Sample",
        "",
        markdown_table(
            panel,
            [
                "stock_id",
                "signal_date",
                "source_model_ids",
                "source_tdcc_dataset_id",
                "feature_as_of_date",
                "point_in_time_status",
                "close",
                "distance_to_ema23_pct",
                "pre45_return_pct",
                "pre45_range_width_pct",
                "pre45_drawdown_pct",
                "macd_hist",
                "rsi14",
                "tdcc_as_of_date",
                "tdcc_over_400_change_1w",
                "monthly_revenue_context_as_of_date",
                "monthly_revenue_data_status",
                "monthly_revenue_latest_yoy_pct",
                "monthly_revenue_strong_flag",
                "theme_context_as_of_date",
                "theme_context_status_group",
                "theme_context_volume_attack_status",
                "twse_return_20d_pct",
            ],
            limit=30,
        )
        if not panel.empty
        else "No panel rows.",
    ]
    PANEL_MD.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8", newline="\n")
    DOCS_PANEL_MD.write_text(PANEL_MD.read_text(encoding="utf-8"), encoding="utf-8", newline="\n")

    catalog_lines = [
        "# Daily Model Background Feature Catalog",
        "",
        f"- generated_at: `{now_text()}`",
        "- scope: documents which columns are shared objective background data and which ideas are explicitly model-specific.",
        "- rule: shared objective data can be reused; model-specific interpretations require separate research evidence and promotion.",
        "",
        markdown_table(
            catalog,
            [
                "feature_column",
                "feature_family",
                "feature_scope",
                "allowed_use",
                "model_specific_owner",
                "point_in_time_rule",
            ],
            limit=120,
        ),
    ]
    CATALOG_MD.write_text("\n".join(catalog_lines).rstrip() + "\n", encoding="utf-8", newline="\n")
    DOCS_CATALOG_MD.write_text(CATALOG_MD.read_text(encoding="utf-8"), encoding="utf-8", newline="\n")


def main() -> int:
    RESEARCH_LATEST_DIR.mkdir(parents=True, exist_ok=True)
    DOCS_LATEST_DIR.mkdir(parents=True, exist_ok=True)
    panel = build_feature_panel()
    if panel.empty:
        raise RuntimeError("No daily model signal rows available for background feature panel")
    validate_no_model_semantic_columns(panel.columns.tolist())
    catalog = feature_catalog(panel)

    write_csv(panel, PANEL_CSV)
    write_csv(panel, DOCS_PANEL_CSV)
    write_csv(catalog, CATALOG_CSV)
    write_csv(catalog, DOCS_CATALOG_CSV)
    write_markdown(panel, catalog)

    print(f"Saved {PANEL_CSV} rows={len(panel)}")
    print(f"Saved {CATALOG_CSV} rows={len(catalog)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
