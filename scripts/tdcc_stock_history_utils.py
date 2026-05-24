from __future__ import annotations

import math
import sys
from pathlib import Path
from typing import Any

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent))

from tracking_utils import (
    DATA_DIR,
    HISTORY_DIR,
    LATEST_DIR,
    TDCC_SIGNALS_DIR,
    classify_market_regime,
    load_market_index_history,
    load_price_history,
    market_return_after,
    market_row_on_or_before,
    normalize_code,
    normalize_date,
    read_csv,
    safe_str,
    to_number,
    write_csv,
)


TDCC_STOCK_HISTORY_DIR = DATA_DIR / "tdcc_stock_history"
TDCC_RAW_HISTORY_DIR = HISTORY_DIR / "tdcc"
TDCC_LATEST = LATEST_DIR / "tdcc_holder_ratio_latest.csv"
THEME_MAP = Path("config/stock_theme_map.csv")
THEME_BREADTH_HISTORY = TDCC_SIGNALS_DIR / "theme_breadth_history.csv"
SNAPSHOT_CSV = TDCC_SIGNALS_DIR / "tdcc_signal_snapshot.csv"
NORMALIZED_LOG = TDCC_SIGNALS_DIR / "tdcc_normalized_signal_log.csv"
ABM_HISTORY = TDCC_SIGNALS_DIR / "tdcc_pre_move_accumulation_history.csv"
THRESHOLDS = [400, 600, 800, 1000]


def pct_return(current: Any, base: Any) -> float:
    current_num = to_number(current)
    base_num = to_number(base)
    if math.isnan(current_num) or math.isnan(base_num) or base_num == 0:
        return math.nan
    return (current_num / base_num - 1) * 100


def safe_bool(value: Any) -> bool:
    return safe_str(value).lower() in {"true", "1", "yes"}


def infer_benchmark_index(market: Any) -> str:
    text = safe_str(market).upper()
    if "TPEX" in text or "OTC" in text:
        return "TPEX"
    if "TWSE" in text:
        return "TWSE"
    return "unknown"


def read_theme_map() -> dict[str, dict[str, str]]:
    df = read_csv(THEME_MAP, dtype=str)
    if df.empty:
        return {}
    df["code"] = df["code"].map(normalize_code)
    return {safe_str(row["code"]): row.to_dict() for _, row in df.iterrows()}


def read_theme_breadth_map() -> dict[tuple[str, str], str]:
    df = read_csv(THEME_BREADTH_HISTORY, dtype=str)
    if df.empty:
        return {}
    result: dict[tuple[str, str], str] = {}
    for _, row in df.iterrows():
        date = normalize_date(row.get("signal_date", ""))
        theme = safe_str(row.get("primary_theme", ""))
        level = safe_str(row.get("theme_breadth_level", "")) or safe_str(row.get("theme_priority", ""))
        if date and theme:
            result[(date, theme)] = level or "Neutral"
    return result


def load_tdcc_raw_snapshots() -> list[tuple[str, pd.DataFrame]]:
    paths = sorted(TDCC_RAW_HISTORY_DIR.glob("tdcc_holder_ratio_*.csv"))
    if TDCC_LATEST.exists():
        paths.append(TDCC_LATEST)
    unique: dict[str, Path] = {}
    for path in paths:
        df = read_csv(path, dtype=str)
        if df.empty or "date" not in df.columns or "code" not in df.columns:
            continue
        date = normalize_date(df["date"].dropna().astype(str).max())
        if date:
            unique[date] = path
    snapshots: list[tuple[str, pd.DataFrame]] = []
    for date, path in sorted(unique.items()):
        df = read_csv(path, dtype=str)
        if df.empty:
            continue
        df["date"] = df["date"].map(normalize_date)
        df["code"] = df["code"].map(normalize_code)
        if "name" not in df.columns:
            df["name"] = ""
        for threshold in THRESHOLDS:
            col = f"over_{threshold}_pct"
            if col not in df.columns:
                df[col] = math.nan
            df[col] = pd.to_numeric(df[col], errors="coerce")
        snapshots.append((date, df))
    return snapshots


def threshold_change(rows: pd.DataFrame, ratio_col: str, current_idx: int, weeks: int) -> float:
    if current_idx - weeks < 0:
        return math.nan
    current = to_number(rows.iloc[current_idx].get(ratio_col))
    previous = to_number(rows.iloc[current_idx - weeks].get(ratio_col))
    if math.isnan(current) or math.isnan(previous):
        return math.nan
    return current - previous


def consecutive_up_weeks(rows: pd.DataFrame, ratio_cols: list[str], current_idx: int) -> int:
    streak = 0
    for idx in range(current_idx, 0, -1):
        improved = False
        for col in ratio_cols:
            cur = to_number(rows.iloc[idx].get(col))
            prev = to_number(rows.iloc[idx - 1].get(col))
            if not math.isnan(cur) and not math.isnan(prev) and cur > prev:
                improved = True
                break
        if improved:
            streak += 1
        else:
            break
    return streak


def all_thresholds_up(rows: pd.DataFrame, current_idx: int) -> bool:
    return all(threshold_change(rows, f"over_{threshold}_ratio", current_idx, 1) > 0 for threshold in THRESHOLDS)


def high_thresholds_up(rows: pd.DataFrame, current_idx: int) -> bool:
    return (
        threshold_change(rows, "over_800_ratio", current_idx, 1) > 0
        or threshold_change(rows, "over_1000_ratio", current_idx, 1) > 0
    )


def build_tdcc_stock_history_frame() -> pd.DataFrame:
    snapshots = load_tdcc_raw_snapshots()
    if not snapshots:
        return pd.DataFrame()
    theme_map = read_theme_map()
    breadth_map = read_theme_breadth_map()
    frames: list[pd.DataFrame] = []
    for date, df in snapshots:
        part = pd.DataFrame()
        part["as_of_date"] = df["date"].map(normalize_date).where(df["date"].map(normalize_date).ne(""), date)
        part["stock_id"] = df["code"].map(normalize_code)
        part["stock_name"] = df["name"].astype(str)
        for threshold in THRESHOLDS:
            part[f"over_{threshold}_ratio"] = pd.to_numeric(df[f"over_{threshold}_pct"], errors="coerce")
        part["retail_ratio"] = math.nan
        part["total_shareholders"] = math.nan
        frames.append(part)
    if not frames:
        return pd.DataFrame()
    base = pd.concat(frames, ignore_index=True, sort=False)
    base = base[base["stock_id"].astype(str).str.len() > 0].copy()
    base = base.drop_duplicates(["as_of_date", "stock_id"], keep="last")
    base = base.sort_values(["stock_id", "as_of_date"]).reset_index(drop=True)

    rows: list[dict[str, Any]] = []
    ratio_cols = [f"over_{threshold}_ratio" for threshold in THRESHOLDS]
    for stock_id, group in base.groupby("stock_id", sort=True):
        group = group.sort_values("as_of_date").reset_index(drop=True)
        theme = theme_map.get(stock_id, {})
        primary_theme = safe_str(theme.get("primary_theme", "")) or safe_str(theme.get("theme", "")) or ""
        for idx, source in group.iterrows():
            as_of_date = safe_str(source.get("as_of_date", ""))
            item: dict[str, Any] = {
                "as_of_date": as_of_date,
                "stock_id": stock_id,
                "stock_name": safe_str(source.get("stock_name", "")) or safe_str(theme.get("name", "")),
                "theme": primary_theme,
                "retail_ratio": source.get("retail_ratio", math.nan),
                "retail_ratio_change_1w": math.nan,
                "total_shareholders": source.get("total_shareholders", math.nan),
                "total_shareholders_change_1w": math.nan,
                "tdcc_consecutive_up_weeks": consecutive_up_weeks(group, ratio_cols, idx),
                "all_thresholds_up": all_thresholds_up(group, idx),
                "high_thresholds_up": high_thresholds_up(group, idx),
                "four_thresholds_sync_up": all_thresholds_up(group, idx),
                "theme_breadth_level": breadth_map.get((as_of_date, primary_theme), "Neutral"),
            }
            for threshold in THRESHOLDS:
                ratio_col = f"over_{threshold}_ratio"
                item[ratio_col] = source.get(ratio_col, math.nan)
                item[f"over_{threshold}_change_1w"] = threshold_change(group, ratio_col, idx, 1)
                item[f"over_{threshold}_change_2w"] = threshold_change(group, ratio_col, idx, 2)
                item[f"over_{threshold}_change_3w"] = threshold_change(group, ratio_col, idx, 3)
            rows.append(item)
    out = pd.DataFrame(rows)
    return out.sort_values(["stock_id", "as_of_date"]).reset_index(drop=True)


def write_tdcc_stock_history_files(limit_stock_ids: set[str] | None = None) -> pd.DataFrame:
    TDCC_STOCK_HISTORY_DIR.mkdir(parents=True, exist_ok=True)
    all_history = build_tdcc_stock_history_frame()
    if all_history.empty:
        return all_history
    manifest_rows: list[dict[str, Any]] = []
    for stock_id, group in all_history.groupby("stock_id", sort=True):
        if limit_stock_ids and stock_id not in limit_stock_ids:
            continue
        group = group.sort_values("as_of_date").drop_duplicates(["as_of_date", "stock_id"], keep="last").reset_index(drop=True)
        path = TDCC_STOCK_HISTORY_DIR / f"{stock_id}.csv"
        write_csv(group, path)
        latest = group.iloc[-1]
        manifest_rows.append(
            {
                "stock_id": stock_id,
                "stock_name": latest.get("stock_name", ""),
                "theme": latest.get("theme", ""),
                "rows": len(group),
                "start_date": group["as_of_date"].iloc[0],
                "end_date": group["as_of_date"].iloc[-1],
                "file_path": path.as_posix(),
            }
        )
    manifest = pd.DataFrame(manifest_rows).sort_values("stock_id").reset_index(drop=True)
    write_csv(manifest, LATEST_DIR / "tdcc_stock_history_manifest.csv")
    return manifest


def normalize_tdcc_history_columns(df: pd.DataFrame, stock_id: str) -> pd.DataFrame:
    if df.empty:
        return df
    result = df.copy()
    if "stock_id" not in result.columns and "code" in result.columns:
        result["stock_id"] = result["code"]
    if "as_of_date" not in result.columns and "signal_date" in result.columns:
        result["as_of_date"] = result["signal_date"]
    if "stock_name" not in result.columns and "name" in result.columns:
        result["stock_name"] = result["name"]
    if "theme" not in result.columns and "primary_theme" in result.columns:
        result["theme"] = result["primary_theme"]
    result["stock_id"] = result["stock_id"].map(normalize_code)
    result["as_of_date"] = result["as_of_date"].map(normalize_date)
    result = result[result["stock_id"].eq(normalize_code(stock_id)) & result["as_of_date"].ne("")]

    rename_map = {
        "tdcc_1w_change_400": "over_400_change_1w",
        "tdcc_1w_change_600": "over_600_change_1w",
        "tdcc_1w_change_800": "over_800_change_1w",
        "tdcc_1w_change_1000": "over_1000_change_1w",
        "tdcc_2w_change_400": "over_400_change_2w",
        "tdcc_2w_change_600": "over_600_change_2w",
        "tdcc_2w_change_800": "over_800_change_2w",
        "tdcc_2w_change_1000": "over_1000_change_2w",
        "tdcc_3w_change_400": "over_400_change_3w",
        "tdcc_3w_change_600": "over_600_change_3w",
        "tdcc_3w_change_800": "over_800_change_3w",
        "tdcc_3w_change_1000": "over_1000_change_3w",
    }
    for old, new in rename_map.items():
        if old in result.columns and new not in result.columns:
            result[new] = result[old]
    for threshold in THRESHOLDS:
        ratio_col = f"over_{threshold}_ratio"
        alt_col = f"tdcc_{threshold}_ratio_20w_high"
        if ratio_col not in result.columns:
            result[ratio_col] = math.nan
        if result[ratio_col].isna().all() and alt_col in result.columns:
            result[ratio_col] = result[alt_col]
        for weeks in [1, 2, 3]:
            col = f"over_{threshold}_change_{weeks}w"
            if col not in result.columns:
                result[col] = math.nan
    for col in [
        "retail_ratio",
        "retail_ratio_change_1w",
        "total_shareholders",
        "total_shareholders_change_1w",
        "tdcc_consecutive_up_weeks",
        "all_thresholds_up",
        "high_thresholds_up",
        "four_thresholds_sync_up",
        "theme_breadth_level",
    ]:
        if col not in result.columns:
            result[col] = "" if col.endswith("_up") or col == "theme_breadth_level" else math.nan
    return result.sort_values("as_of_date").drop_duplicates(["as_of_date", "stock_id"], keep="last").reset_index(drop=True)


def load_stock_tdcc_history(stock_id: Any) -> tuple[pd.DataFrame, dict[str, Any]]:
    stock_id = normalize_code(stock_id)
    status = {
        "source": "",
        "tdcc_history_weeks": 0,
        "latest_tdcc_date": "",
        "insufficient_tdcc_history": True,
        "warnings": [],
    }
    if not stock_id:
        status["warnings"].append("missing_stock_id")
        return pd.DataFrame(), status

    path = TDCC_STOCK_HISTORY_DIR / f"{stock_id}.csv"
    if path.exists():
        df = normalize_tdcc_history_columns(read_csv(path, dtype=str), stock_id)
        status["source"] = path.as_posix()
    else:
        frames: list[pd.DataFrame] = []
        for fallback in [SNAPSHOT_CSV, NORMALIZED_LOG, ABM_HISTORY]:
            fallback_df = normalize_tdcc_history_columns(read_csv(fallback, dtype=str), stock_id)
            if not fallback_df.empty:
                frames.append(fallback_df)
        df = pd.concat(frames, ignore_index=True, sort=False) if frames else pd.DataFrame()
        if not df.empty:
            df = normalize_tdcc_history_columns(df, stock_id)
        status["source"] = "fallback_tdcc_signal_tables" if not df.empty else ""
    if df.empty:
        status["warnings"].append("insufficient_tdcc_history")
        return df, status
    status["tdcc_history_weeks"] = int(len(df))
    status["latest_tdcc_date"] = safe_str(df["as_of_date"].max())
    status["insufficient_tdcc_history"] = len(df) < 4
    if len(df) < 4:
        status["warnings"].append("tdcc_history_less_than_4_weeks")
    return df, status


def price_position_on_or_before(price: pd.DataFrame, date: str) -> int | None:
    if price.empty or "date" not in price.columns:
        return None
    date = normalize_date(date)
    candidates = price[price["date"] <= date]
    if candidates.empty:
        return None
    return int(candidates.index[-1])


def return_before(price: pd.DataFrame, pos: int, days: int) -> float:
    if pos is None or pos - days < 0:
        return math.nan
    return pct_return(price.loc[pos, "close"], price.loc[pos - days, "close"])


def index_return_before(index_history: pd.DataFrame, index_code: str, date: str, days: int) -> float:
    if index_history.empty or index_code == "unknown":
        return math.nan
    part = index_history[(index_history["index_code"] == index_code) & (index_history["date"] <= normalize_date(date))]
    part = part.sort_values("date").reset_index(drop=True)
    if len(part) <= days:
        return math.nan
    return pct_return(part.iloc[-1].get("close"), part.iloc[-days - 1].get("close"))


def volume_window_ratio(price: pd.DataFrame, pos: int, days: int, baseline_days: int = 20) -> float:
    if pos is None or "volume" not in price.columns:
        return math.nan
    start_recent = max(0, pos - days + 1)
    start_base = max(0, pos - baseline_days + 1)
    recent = pd.to_numeric(price.iloc[start_recent : pos + 1]["volume"], errors="coerce").mean()
    base = pd.to_numeric(price.iloc[start_base : pos + 1]["volume"], errors="coerce").mean()
    if math.isnan(recent) or math.isnan(base) or base == 0:
        return math.nan
    return recent / base


def close_distance(row: pd.Series, close_col: str, target_col: str) -> float:
    return pct_return(row.get(close_col), row.get(target_col))


def classify_tdcc_price_phase(row: pd.Series | dict[str, Any]) -> str:
    get = row.get if isinstance(row, dict) else row.get
    weeks = to_number(get("tdcc_consecutive_up_weeks"))
    high_up = safe_bool(get("high_thresholds_up")) or safe_bool(get("four_thresholds_sync_up"))
    four_up = safe_bool(get("four_thresholds_sync_up"))
    price_2w = to_number(get("price_ret_2w"))
    relative_2w = to_number(get("relative_ret_2w"))
    volume_2w = to_number(get("volume_ratio_2w"))
    dist_ma20 = to_number(get("distance_from_ma20"))

    if math.isnan(weeks) or math.isnan(price_2w) or math.isnan(volume_2w):
        return "insufficient_tdcc_history"
    relative_ok_low = math.isnan(relative_2w) or relative_2w <= 3
    relative_ok_confirm = math.isnan(relative_2w) or relative_2w > 3
    relative_negative = math.isnan(relative_2w) or relative_2w < 0
    if weeks >= 2 and price_2w >= 20 and volume_2w >= 1.8 and not math.isnan(dist_ma20) and dist_ma20 >= 15:
        return "overheated_after_tdcc"
    if price_2w >= 20 or (not math.isnan(relative_2w) and relative_2w >= 10) or (not math.isnan(dist_ma20) and dist_ma20 >= 15):
        return "price_leading_tdcc"
    if weeks >= 2 and price_2w < 0 and relative_negative:
        return "tdcc_price_divergence"
    if weeks >= 2 and (high_up or four_up) and price_2w <= 8 and relative_ok_low and volume_2w < 1.5:
        return "tdcc_leading_price"
    if weeks >= 2 and price_2w > 8 and relative_ok_confirm and volume_2w >= 1.2:
        return "tdcc_price_confirmed"
    return "neutral_or_unclear"


def build_stock_tdcc_price_panel(stock_id: Any) -> tuple[pd.DataFrame, dict[str, Any]]:
    stock_id = normalize_code(stock_id)
    tdcc, status = load_stock_tdcc_history(stock_id)
    price = load_price_history(stock_id)
    index_history = load_market_index_history(update_if_missing=False)
    status["price_history_available"] = not price.empty
    status["price_aligned"] = False
    status["benchmark_available"] = not index_history.empty
    if tdcc.empty or price.empty:
        if price.empty:
            status["warnings"].append("missing_price_history")
        return pd.DataFrame(), status

    rows: list[dict[str, Any]] = []
    for _, tdcc_row in tdcc.iterrows():
        as_of_date = normalize_date(tdcc_row.get("as_of_date", ""))
        pos = price_position_on_or_before(price, as_of_date)
        item = tdcc_row.to_dict()
        item["price_date"] = ""
        item["close"] = math.nan
        if pos is None:
            item["tdcc_price_phase"] = "insufficient_tdcc_history"
            rows.append(item)
            continue
        price_row = price.loc[pos]
        item["price_date"] = safe_str(price_row.get("date", ""))
        item["close"] = to_number(price_row.get("close"))
        benchmark = infer_benchmark_index(price_row.get("market", ""))
        item["benchmark_index"] = benchmark
        item["market_regime"] = classify_market_regime(market_row_on_or_before(index_history, benchmark, as_of_date))
        for weeks, days in [(1, 5), (2, 10), (3, 15), (4, 20), (8, 40)]:
            stock_ret = return_before(price, pos, days)
            item[f"price_ret_{weeks}w"] = stock_ret
            if weeks in {1, 2, 4}:
                bench_ret = index_return_before(index_history, benchmark, as_of_date, days)
                item[f"relative_ret_{weeks}w"] = math.nan if math.isnan(bench_ret) or math.isnan(stock_ret) else stock_ret - bench_ret
        item["volume_ratio_1w"] = volume_window_ratio(price, pos, 5)
        item["volume_ratio_2w"] = volume_window_ratio(price, pos, 10)
        item["distance_from_ma20"] = to_number(price_row.get("distance_to_ma20_pct", close_distance(price_row, "close", "ma20")))
        item["distance_from_ma60"] = to_number(price_row.get("distance_to_ma60_pct", close_distance(price_row, "close", "ma60")))
        item["distance_from_20d_high"] = to_number(price_row.get("distance_to_high_20_pct", close_distance(price_row, "close", "high_20")))
        item["distance_from_60d_high"] = to_number(price_row.get("distance_to_high_60_pct", close_distance(price_row, "close", "high_60")))
        item["breakout_status"] = "breakout_or_near_high" if to_number(item.get("distance_from_20d_high")) >= -1 else "below_recent_high"
        item["overheated_status"] = (
            "overheated"
            if to_number(item.get("price_ret_2w")) >= 20
            or to_number(item.get("distance_from_ma20")) >= 15
            or to_number(item.get("volume_ratio_2w")) >= 1.8
            else "not_overheated"
        )
        item["tdcc_price_phase"] = classify_tdcc_price_phase(item)
        rows.append(item)
    panel = pd.DataFrame(rows).sort_values("as_of_date").reset_index(drop=True)
    status["price_aligned"] = panel["price_date"].astype(str).str.len().gt(0).any()
    status["latest_tdcc_price_phase"] = safe_str(panel.iloc[-1].get("tdcc_price_phase", "")) if not panel.empty else ""
    return panel, status


def forward_stats(price: pd.DataFrame, index_history: pd.DataFrame, pos: int, benchmark: str, horizon: int) -> dict[str, Any]:
    close0 = to_number(price.loc[pos, "close"])
    available = len(price) - pos - 1
    row: dict[str, Any] = {f"mature_d{horizon}": available >= horizon}
    if available < horizon or math.isnan(close0) or close0 == 0:
        row[f"ret_d{horizon}"] = math.nan
        row[f"relative_ret_d{horizon}"] = math.nan
        return row
    close_h = to_number(price.loc[pos + horizon, "close"])
    ret = pct_return(close_h, close0)
    _, bench_ret = market_return_after(index_history, benchmark, price.loc[pos, "date"], horizon)
    row[f"ret_d{horizon}"] = ret
    row[f"relative_ret_d{horizon}"] = math.nan if math.isnan(ret) or math.isnan(bench_ret) else ret - bench_ret
    return row


def backtest_stock_tdcc_phase(stock_id: Any, phase: str | None = None) -> pd.DataFrame:
    stock_id = normalize_code(stock_id)
    panel, _status = build_stock_tdcc_price_panel(stock_id)
    price = load_price_history(stock_id)
    index_history = load_market_index_history(update_if_missing=False)
    if panel.empty or price.empty:
        return pd.DataFrame(
            [
                {
                    "stock_id": stock_id,
                    "phase": phase or "all",
                    "sample_count": 0,
                    "sample_status": "insufficient_sample",
                }
            ]
        )
    if phase:
        panel = panel[panel["tdcc_price_phase"].astype(str).eq(phase)].copy()
    rows: list[dict[str, Any]] = []
    for _, item in panel.iterrows():
        pos = price_position_on_or_before(price, safe_str(item.get("as_of_date", "")))
        if pos is None:
            continue
        benchmark = safe_str(item.get("benchmark_index", "")) or infer_benchmark_index(price.loc[pos].get("market", ""))
        result = {"phase": safe_str(item.get("tdcc_price_phase", "")), "as_of_date": item.get("as_of_date", "")}
        for horizon in [5, 10, 20]:
            result.update(forward_stats(price, index_history, pos, benchmark, horizon))
        close0 = to_number(price.loc[pos, "close"])
        for horizon in [10, 20]:
            window = price.iloc[pos + 1 : min(len(price), pos + horizon + 1)]
            result[f"mfe_d{horizon}"] = pct_return(window["high"].max(), close0) if not window.empty and "high" in window.columns else math.nan
            result[f"mae_d{horizon}"] = pct_return(window["low"].min(), close0) if not window.empty and "low" in window.columns else math.nan
        rows.append(result)
    samples = pd.DataFrame(rows)
    target_phase = phase or (safe_str(panel.iloc[-1].get("tdcc_price_phase", "")) if not panel.empty else "all")
    def mature_rows(horizon: int) -> pd.DataFrame:
        if samples.empty or f"mature_d{horizon}" not in samples.columns:
            return pd.DataFrame()
        return samples[samples[f"mature_d{horizon}"].astype(str).str.lower().isin(["true", "1", "yes"])].copy()

    mature5 = mature_rows(5)
    mature10 = mature_rows(10)
    mature20 = mature_rows(20)
    sample_count = len(mature10)
    summary = {
        "stock_id": stock_id,
        "phase": target_phase,
        "sample_count": sample_count,
        "avg_ret_d5": pd.to_numeric(mature5.get("ret_d5", pd.Series(dtype=float)), errors="coerce").mean(),
        "avg_ret_d10": pd.to_numeric(mature10.get("ret_d10", pd.Series(dtype=float)), errors="coerce").mean(),
        "avg_ret_d20": pd.to_numeric(mature20.get("ret_d20", pd.Series(dtype=float)), errors="coerce").mean(),
        "median_ret_d10": pd.to_numeric(mature10.get("ret_d10", pd.Series(dtype=float)), errors="coerce").median(),
        "win_rate_d10": (pd.to_numeric(mature10.get("ret_d10", pd.Series(dtype=float)), errors="coerce") > 0).mean() * 100 if sample_count else math.nan,
        "avg_relative_ret_d10": pd.to_numeric(mature10.get("relative_ret_d10", pd.Series(dtype=float)), errors="coerce").mean(),
        "avg_mfe_d10": pd.to_numeric(mature10.get("mfe_d10", pd.Series(dtype=float)), errors="coerce").mean(),
        "avg_mae_d10": pd.to_numeric(mature10.get("mae_d10", pd.Series(dtype=float)), errors="coerce").mean(),
        "sample_status": "ok" if sample_count >= 3 else "insufficient_sample",
    }
    return pd.DataFrame([summary])


def tdcc_support_label(latest: pd.Series | dict[str, Any] | None, status: dict[str, Any]) -> str:
    if latest is None or status.get("insufficient_tdcc_history"):
        return "資料不足"
    weeks = to_number(latest.get("tdcc_consecutive_up_weeks"))
    if weeks >= 3 and (safe_bool(latest.get("high_thresholds_up")) or safe_bool(latest.get("four_thresholds_sync_up"))):
        return "強"
    if weeks >= 2:
        return "中"
    return "弱"


def price_reaction_label(phase: str) -> str:
    return {
        "tdcc_leading_price": "未反應",
        "tdcc_price_confirmed": "初步確認",
        "price_leading_tdcc": "已過熱",
        "overheated_after_tdcc": "已過熱",
        "tdcc_price_divergence": "背離失效",
        "failed_after_tdcc": "背離失效",
        "insufficient_tdcc_history": "資料不足",
    }.get(phase, "資料不足" if phase == "" else "未明確")


def tdcc_history_analysis(stock_id: Any) -> dict[str, Any]:
    panel, status = build_stock_tdcc_price_panel(stock_id)
    latest = panel.iloc[-1] if not panel.empty else None
    phase = safe_str(latest.get("tdcc_price_phase", "")) if latest is not None else "insufficient_tdcc_history"
    backtest = backtest_stock_tdcc_phase(stock_id, phase if phase else None)
    support = tdcc_support_label(latest, status)
    reaction = price_reaction_label(phase)
    accumulation = "是" if phase == "tdcc_leading_price" else ("樣本不足" if status.get("insufficient_tdcc_history") else "否")
    factor = "是" if phase in {"tdcc_leading_price", "tdcc_price_confirmed"} else ("只能觀察" if phase in {"neutral_or_unclear", "tdcc_price_divergence"} else "否")
    risks: list[str] = []
    if phase in {"price_leading_tdcc", "overheated_after_tdcc"}:
        risks.append("股價已反應")
    if phase in {"tdcc_price_divergence", "failed_after_tdcc"}:
        risks.append("TDCC 背離")
    if status.get("insufficient_tdcc_history"):
        risks.append("資料不足")
    if latest is not None and safe_str(latest.get("theme_breadth_level", "")) in {"C", "Weakening", "Neutral"}:
        risks.append("族群不支持")
    if latest is not None and to_number(latest.get("relative_ret_2w")) < -3:
        risks.append("benchmark 落後")
    return {
        "panel": panel,
        "status": status,
        "latest": latest,
        "phase": phase,
        "backtest": backtest,
        "tdcc_support": support,
        "price_reaction_stage": reaction,
        "is_quiet_accumulation": accumulation,
        "is_positive_factor": factor,
        "main_risks": risks or ["資料不足" if status.get("insufficient_tdcc_history") else "無明顯 TDCC 專屬風險"],
    }


def plot_tdcc_history_chart(stock_id: Any, stock_name: str, panel: pd.DataFrame, path: Path) -> bool:
    path.parent.mkdir(parents=True, exist_ok=True)
    if panel.empty or len(panel) < 4 or "close" not in panel.columns:
        return False
    data = panel.tail(12).copy()
    data["x"] = range(len(data))
    fig, ax_price = plt.subplots(figsize=(10, 5.8), dpi=150)
    ax_tdcc = ax_price.twinx()
    ax_price.plot(data["x"], pd.to_numeric(data["close"], errors="coerce"), color="#1f77b4", linewidth=2, label="Close")
    for col, color, label in [
        ("over_400_ratio", "#ff7f0e", ">400"),
        ("over_800_ratio", "#2ca02c", ">800"),
        ("over_1000_ratio", "#d62728", ">1000"),
    ]:
        if col in data.columns and pd.to_numeric(data[col], errors="coerce").notna().any():
            ax_tdcc.plot(data["x"], pd.to_numeric(data[col], errors="coerce"), color=color, linewidth=1.4, marker="o", label=label)
    for _, row in data.iterrows():
        if to_number(row.get("tdcc_consecutive_up_weeks")) >= 2:
            ax_price.axvspan(row["x"] - 0.35, row["x"] + 0.35, color="#f4c542", alpha=0.18)
    latest_phase = safe_str(data.iloc[-1].get("tdcc_price_phase", ""))
    ax_price.set_title(f"{normalize_code(stock_id)} TDCC History - latest phase: {latest_phase}", fontsize=11, weight="bold")
    ax_price.set_ylabel("Close")
    ax_tdcc.set_ylabel("TDCC holder ratio")
    ax_price.grid(True, alpha=0.25)
    tick_positions = list(data["x"])
    ax_price.set_xticks(tick_positions)
    ax_price.set_xticklabels([safe_str(x) for x in data["as_of_date"]], rotation=35, ha="right")
    lines1, labels1 = ax_price.get_legend_handles_labels()
    lines2, labels2 = ax_tdcc.get_legend_handles_labels()
    ax_price.legend(lines1 + lines2, labels1 + labels2, loc="upper left", fontsize=8)
    fig.tight_layout()
    fig.savefig(path, bbox_inches="tight")
    plt.close(fig)
    return True
