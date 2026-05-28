from __future__ import annotations

import argparse
import math
import sys
from pathlib import Path
from typing import Any

import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent))

from tracking_utils import (  # noqa: E402
    HISTORY_DIR,
    LATEST_DIR,
    TDCC_SIGNALS_DIR,
    append_update_csv,
    classify_market_regime,
    load_market_index_history,
    load_price_history,
    markdown_table,
    market_row_on_or_before,
    normalize_code,
    normalize_date,
    now_text,
    read_csv,
    safe_str,
    to_number,
    write_csv,
)


LATEST_TDCC = LATEST_DIR / "tdcc_holder_ratio_latest.csv"
THEME_MAP = Path("config/stock_theme_map.csv")
SNAPSHOT_CSV = TDCC_SIGNALS_DIR / "tdcc_signal_snapshot.csv"
NORMALIZED_LOG = TDCC_SIGNALS_DIR / "tdcc_normalized_signal_log.csv"
THEME_BREADTH = TDCC_SIGNALS_DIR / "theme_breadth_history.csv"
OUTPUT_MD = LATEST_DIR / "tdcc_signal_structures_latest.md"
THRESHOLDS = [400, 600, 800, 1000]
PRICE_HISTORY_CACHE: dict[str, pd.DataFrame] = {}


def load_theme_map() -> dict[str, dict[str, str]]:
    df = read_csv(THEME_MAP, dtype=str)
    if df.empty:
        return {}
    df["code"] = df["code"].map(normalize_code)
    return {row["code"]: row.to_dict() for _, row in df.iterrows()}


def load_tdcc_snapshots(max_dates: int | None = 26) -> list[tuple[str, pd.DataFrame]]:
    paths = sorted((HISTORY_DIR / "tdcc").glob("tdcc_holder_ratio_*.csv"))
    if LATEST_TDCC.exists():
        paths.append(LATEST_TDCC)
    unique: dict[str, Path] = {}
    for path in paths:
        df = read_csv(path, dtype=str)
        if df.empty or "date" not in df.columns or "code" not in df.columns:
            continue
        date = normalize_date(df["date"].dropna().astype(str).max())
        if date:
            unique[date] = path
    dated_paths = sorted(unique.items())
    if max_dates and max_dates > 0:
        dated_paths = dated_paths[-max_dates:]
    out: list[tuple[str, pd.DataFrame]] = []
    for date, path in dated_paths:
        df = read_csv(path, dtype=str)
        df["date"] = df["date"].map(normalize_date)
        df["code"] = df["code"].map(normalize_code)
        for th in THRESHOLDS:
            col = f"over_{th}_pct"
            if col in df.columns:
                df[col] = pd.to_numeric(df[col], errors="coerce")
        out.append((date, df))
    return out


def tdcc_series(snapshots: list[tuple[str, pd.DataFrame]], code: str, threshold: int) -> list[tuple[str, float]]:
    out: list[tuple[str, float]] = []
    col = f"over_{threshold}_pct"
    for date, df in snapshots:
        row = df[df["code"] == code]
        if not row.empty and col in row.columns:
            out.append((date, to_number(row.iloc[0].get(col))))
    return out


def streak_weeks(series: list[tuple[str, float]]) -> int:
    if len(series) < 2:
        return 0
    streak = 0
    for i in range(len(series) - 1, 0, -1):
        cur = series[i][1]
        prev = series[i - 1][1]
        if not math.isnan(cur) and not math.isnan(prev) and cur > prev:
            streak += 1
        else:
            break
    return streak


def latest_delta(series: list[tuple[str, float]]) -> float:
    if len(series) < 2:
        return math.nan
    cur = series[-1][1]
    prev = series[-2][1]
    if math.isnan(cur) or math.isnan(prev):
        return math.nan
    return cur - prev


def ratio_to_high(series: list[tuple[str, float]]) -> float:
    values = [value for _, value in series if not math.isnan(value)]
    if not values:
        return math.nan
    high = max(values)
    if high == 0:
        return math.nan
    return values[-1] / high


def tdcc_change(series: list[tuple[str, float]], weeks: int) -> float:
    if len(series) <= weeks:
        return math.nan
    cur = series[-1][1]
    prev = series[-weeks - 1][1]
    if math.isnan(cur) or math.isnan(prev):
        return math.nan
    return cur - prev


def infer_benchmark_from_price_row(row: pd.Series) -> str:
    market = safe_str(row.get("market", "")).upper()
    if "TPEX" in market or "OTC" in market:
        return "TPEX"
    return "TWSE"


def index_return_before(index_history: pd.DataFrame, index_code: str, signal_date: str, days: int) -> float:
    if index_history.empty:
        return math.nan
    part = index_history[
        (index_history["index_code"].astype(str) == index_code)
        & (index_history["date"].astype(str) <= signal_date)
    ].copy()
    part = part.sort_values("date").reset_index(drop=True)
    if len(part) <= days:
        return math.nan
    close = to_number(part.iloc[-1].get("close"))
    base = to_number(part.iloc[-days - 1].get("close"))
    if math.isnan(close) or math.isnan(base) or base == 0:
        return math.nan
    return (close / base - 1) * 100


def volume_window_ratio(part: pd.DataFrame, days: int, baseline_days: int = 20) -> float:
    if "volume" not in part.columns or len(part) < days + 1:
        return math.nan
    recent = pd.to_numeric(part["volume"].tail(days), errors="coerce").mean()
    baseline = pd.to_numeric(part["volume"].tail(baseline_days), errors="coerce").mean()
    if math.isnan(recent) or math.isnan(baseline) or baseline == 0:
        return math.nan
    return recent / baseline


def classify_tdcc_price_phase(metrics: dict[str, Any]) -> str:
    tdcc_weeks = int(to_number(metrics.get("tdcc_consecutive_up_weeks"), 0) or 0)
    price_1w = to_number(metrics.get("price_ret_1w"))
    price_2w = to_number(metrics.get("price_ret_2w"))
    price_4w = to_number(metrics.get("price_ret_4w"))
    relative_2w = to_number(metrics.get("relative_ret_2w"))
    relative_4w = to_number(metrics.get("relative_ret_4w"))
    volume_1w = to_number(metrics.get("volume_ratio_1w"))
    volume_2w = to_number(metrics.get("volume_ratio_2w"))
    dist_ma20 = to_number(metrics.get("distance_from_ma20"))
    dist_ma60 = to_number(metrics.get("distance_from_ma60"))

    if math.isnan(price_2w) or math.isnan(relative_2w) or math.isnan(volume_2w):
        return "insufficient_price_context"
    if (not math.isnan(price_1w) and price_1w > 25) or price_2w >= 30 or (not math.isnan(dist_ma20) and dist_ma20 >= 20):
        return "overheated_after_tdcc"
    if price_2w >= 20 or relative_2w >= 10 or (not math.isnan(dist_ma20) and dist_ma20 >= 15):
        return "price_leading_tdcc"
    if tdcc_weeks >= 2 and price_2w < 0 and relative_2w < 0:
        return "tdcc_price_divergence"
    if tdcc_weeks >= 2 and (not math.isnan(price_4w) and price_4w <= -10) and (not math.isnan(relative_4w) and relative_4w <= -8) and (not math.isnan(dist_ma60) and dist_ma60 < 0):
        return "failed_after_tdcc"
    if tdcc_weeks >= 2 and price_2w <= 8 and relative_2w <= 3 and volume_2w < 1.5:
        return "tdcc_leading_price"
    if tdcc_weeks >= 2 and price_2w > 8 and relative_2w > 3 and volume_2w >= 1.2:
        return "tdcc_price_confirmed"
    return "insufficient_price_context"


def price_metrics(code: str, signal_date: str, index_history: pd.DataFrame | None = None) -> dict[str, Any]:
    code = normalize_code(code)
    if code not in PRICE_HISTORY_CACHE:
        PRICE_HISTORY_CACHE[code] = load_price_history(code)
    price = PRICE_HISTORY_CACHE[code]
    out: dict[str, Any] = {}
    if price.empty:
        return out
    part = price[price["date"] <= signal_date].copy()
    if part.empty:
        return out
    row = part.iloc[-1]
    close = to_number(row.get("close"))
    index_history = index_history if index_history is not None else pd.DataFrame()
    benchmark = infer_benchmark_from_price_row(row)
    out["benchmark_index"] = benchmark
    market_row = market_row_on_or_before(index_history, benchmark, signal_date)
    out["market_regime"] = classify_market_regime(market_row)
    for days in [5, 10, 20, 60]:
        if len(part) > days:
            out[f"pre_{days}d_return" if days in [5, 10, 20] else "price_return_60d"] = (close / to_number(part.iloc[-days - 1].get("close")) - 1) * 100
            out[f"price_return_{days}d"] = (close / to_number(part.iloc[-days - 1].get("close")) - 1) * 100
    for weeks, days in [(1, 5), (2, 10), (3, 15), (4, 20)]:
        if len(part) > days:
            stock_ret = (close / to_number(part.iloc[-days - 1].get("close")) - 1) * 100
            out[f"price_ret_{weeks}w"] = stock_ret
            bench_ret = index_return_before(index_history, benchmark, signal_date, days)
            out[f"relative_ret_{weeks}w"] = "" if math.isnan(bench_ret) else stock_ret - bench_ret
        else:
            out[f"price_ret_{weeks}w"] = ""
            out[f"relative_ret_{weeks}w"] = ""
    out["volume_ratio_1w"] = volume_window_ratio(part, 5)
    out["volume_ratio_2w"] = volume_window_ratio(part, 10)
    for ma in [5, 10, 20, 60]:
        col = f"ma{ma}"
        ma_value = to_number(row.get(col))
        out[f"above_ma{ma}"] = "" if math.isnan(ma_value) else close >= ma_value
        out[f"distance_ma{ma}_pct"] = "" if math.isnan(ma_value) else (close / ma_value - 1) * 100
    if len(part) >= 25 and "ma20" in part.columns:
        out["ma20_slope"] = to_number(part.iloc[-1].get("ma20")) - to_number(part.iloc[-6].get("ma20"))
    if len(part) >= 65 and "ma60" in part.columns:
        out["ma60_slope"] = to_number(part.iloc[-1].get("ma60")) - to_number(part.iloc[-6].get("ma60"))
    for days in [20, 60, 120]:
        window = part.tail(days)
        if not window.empty:
            high = to_number(window["high"].max())
            low = to_number(window["low"].min())
            out[f"distance_{days}d_high_pct"] = (close / high - 1) * 100 if high else math.nan
            out[f"price_range_{days}d_pct"] = (high / low - 1) * 100 if low else math.nan
    if len(part) >= 20:
        last20 = part.tail(20)
        ma = last20["close"].mean()
        std = last20["close"].std()
        out["bollinger_bandwidth_20d"] = ((ma + 2 * std) - (ma - 2 * std)) / ma * 100 if ma else math.nan
        out["volume_ratio_20d"] = to_number(row.get("volume")) / last20["volume"].mean() if last20["volume"].mean() else math.nan
    if len(part) >= 14:
        recent = part.tail(14).copy()
        tr = recent["high"] - recent["low"]
        out["atr_pct_14d"] = tr.mean() / close * 100 if close else math.nan
    out["volume_ratio_5d"] = to_number(row.get("volume_ratio"))
    out["turnover_ratio"] = out.get("volume_ratio_20d", "")
    out["is_compression"] = to_number(out.get("price_range_20d_pct")) <= 15
    out["is_volume_healthy"] = 0.8 <= to_number(out.get("volume_ratio_20d")) <= 2.5
    out["is_volume_explosive"] = to_number(out.get("volume_ratio_5d")) > 3
    out["breakout_20d"] = to_number(out.get("distance_20d_high_pct")) >= -1
    out["overheat_bucket"] = "overheated" if to_number(out.get("price_return_20d")) > 30 or to_number(out.get("distance_ma20_pct")) > 20 else "normal"
    out["price_confirm_bucket"] = "confirmed" if bool(out.get("above_ma20")) and to_number(out.get("distance_ma20_pct")) <= 12 else "weak"
    out["distance_from_20d_high"] = out.get("distance_20d_high_pct", "")
    out["distance_from_60d_high"] = out.get("distance_60d_high_pct", "")
    out["distance_from_ma20"] = out.get("distance_ma20_pct", "")
    out["distance_from_ma60"] = out.get("distance_ma60_pct", "")
    return out


def build_snapshot_rows_for_date(
    snapshots: list[tuple[str, pd.DataFrame]],
    snapshot_idx: int,
    theme_map: dict[str, dict[str, str]],
    index_history: pd.DataFrame,
) -> list[dict[str, Any]]:
    signal_date, current_snapshot = snapshots[snapshot_idx]
    available_snapshots = snapshots[: snapshot_idx + 1]
    rows: list[dict[str, Any]] = []

    for _, row in current_snapshot.iterrows():
        code = normalize_code(row.get("code", ""))
        if not code:
            continue
        series_by_threshold = {th: tdcc_series(available_snapshots, code, th) for th in THRESHOLDS}
        deltas = {th: latest_delta(series_by_threshold[th]) for th in THRESHOLDS}
        has = {th: (not math.isnan(deltas[th]) and deltas[th] > 0) for th in THRESHOLDS}
        if not any(has.values()):
            continue
        theme = theme_map.get(code, {})
        streaks = {th: streak_weeks(series_by_threshold[th]) for th in THRESHOLDS}
        all_streak = min(streaks.values()) if streaks else 0
        tdcc_consecutive_up = max(streaks.values()) if streaks else 0
        metrics = price_metrics(code, signal_date, index_history)
        primary = safe_str(theme.get("primary_theme", "")) or "other"
        item: dict[str, Any] = {
            "signal_id": f"{signal_date}_{code}_normalized",
            "signal_date": signal_date,
            "code": code,
            "name": safe_str(row.get("name", "")) or safe_str(theme.get("name", "")),
            "primary_theme": primary,
            "secondary_theme": safe_str(theme.get("secondary_theme", "")),
            "signal_family": "tdcc_normalized_accumulation",
            "threshold_count": sum(1 for value in has.values() if value),
            "has_400": has[400],
            "has_600": has[600],
            "has_800": has[800],
            "has_1000": has[1000],
            "is_all_thresholds": all(has.values()),
            "is_consecutive_2w": all_streak >= 2,
            "is_consecutive_3w": all_streak >= 3,
            "weekly_change_400": deltas[400],
            "weekly_change_600": deltas[600],
            "weekly_change_800": deltas[800],
            "weekly_change_1000": deltas[1000],
            "rank_400": "",
            "rank_600": "",
            "rank_800": "",
            "rank_1000": "",
            "tdcc_400_streak_weeks": streaks[400],
            "tdcc_600_streak_weeks": streaks[600],
            "tdcc_800_streak_weeks": streaks[800],
            "tdcc_1000_streak_weeks": streaks[1000],
            "all_threshold_streak_weeks": all_streak,
            "tdcc_1w_change_400": tdcc_change(series_by_threshold[400], 1),
            "tdcc_1w_change_600": tdcc_change(series_by_threshold[600], 1),
            "tdcc_1w_change_800": tdcc_change(series_by_threshold[800], 1),
            "tdcc_1w_change_1000": tdcc_change(series_by_threshold[1000], 1),
            "tdcc_2w_change_400": tdcc_change(series_by_threshold[400], 2),
            "tdcc_2w_change_600": tdcc_change(series_by_threshold[600], 2),
            "tdcc_2w_change_800": tdcc_change(series_by_threshold[800], 2),
            "tdcc_2w_change_1000": tdcc_change(series_by_threshold[1000], 2),
            "tdcc_3w_change_400": tdcc_change(series_by_threshold[400], 3),
            "tdcc_3w_change_600": tdcc_change(series_by_threshold[600], 3),
            "tdcc_3w_change_800": tdcc_change(series_by_threshold[800], 3),
            "tdcc_3w_change_1000": tdcc_change(series_by_threshold[1000], 3),
            "tdcc_consecutive_up_weeks": tdcc_consecutive_up,
            "all_thresholds_up": all(has.values()),
            "high_thresholds_up": has[800] and has[1000],
            "created_at": now_text(),
            "updated_at": now_text(),
        }
        for th in THRESHOLDS:
            ratio = ratio_to_high(series_by_threshold[th])
            item[f"tdcc_{th}_ratio_20w_high"] = ratio
            item[f"tdcc_{th}_near_20w_high"] = ratio >= 0.95 if not math.isnan(ratio) else ""
        item.update(metrics)
        item["tdcc_price_phase"] = classify_tdcc_price_phase(item)
        item["is_price_not_reacted"] = to_number(item.get("price_return_20d")) <= 10
        item["is_quiet_accumulation"] = item["is_consecutive_2w"] and (item["has_800"] or item["has_1000"]) and item["is_price_not_reacted"]
        item["is_early_breakout"] = item.get("breakout_20d") and to_number(item.get("price_return_20d")) <= 15
        item["abm_score"] = ""
        item["abm_rank"] = ""
        item["setup_type"] = ""
        item["abm_reason"] = ""
        rows.append(item)

    return rows


def build_snapshot(max_dates: int | None = 26) -> tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    snapshots = load_tdcc_snapshots(max_dates=max_dates)
    if not snapshots:
        raise FileNotFoundError("Missing TDCC holder ratio snapshots")
    theme_map = load_theme_map()
    index_history = load_market_index_history(update_if_missing=True)
    rows: list[dict[str, Any]] = []

    for snapshot_idx in range(1, len(snapshots)):
        rows.extend(build_snapshot_rows_for_date(snapshots, snapshot_idx, theme_map, index_history))

    snapshot = pd.DataFrame(rows)
    if snapshot.empty:
        return snapshot, pd.DataFrame(), pd.DataFrame()

    breadth = build_theme_breadth(snapshot)
    if not breadth.empty:
        merge_cols = ["signal_date", "primary_theme", "breadth_score", "sync_status", "theme_breadth_level"]
        snapshot = snapshot.merge(
            breadth[[col for col in merge_cols if col in breadth.columns]],
            on=["signal_date", "primary_theme"],
            how="left",
            suffixes=("", "_breadth"),
        )
    if "theme_breadth_score" not in snapshot.columns and "breadth_score" in snapshot.columns:
        snapshot["theme_breadth_score"] = snapshot["breadth_score"]
    if "theme_sync_status" not in snapshot.columns and "sync_status" in snapshot.columns:
        snapshot["theme_sync_status"] = snapshot["sync_status"]
    snapshot["theme_breadth_score"] = pd.to_numeric(snapshot.get("theme_breadth_score", 0), errors="coerce").fillna(0)
    snapshot["theme_sync_status"] = snapshot.get("theme_sync_status", "neutral").fillna("neutral")
    snapshot["theme_breadth_level"] = snapshot.get("theme_breadth_level", "Neutral").fillna("Neutral")

    normalized_columns = [
            "signal_id",
            "signal_date",
            "code",
            "name",
            "primary_theme",
            "signal_family",
            "threshold_count",
            "has_400",
            "has_600",
            "has_800",
            "has_1000",
            "is_all_thresholds",
            "is_consecutive_2w",
            "is_consecutive_3w",
            "tdcc_consecutive_up_weeks",
            "all_thresholds_up",
            "high_thresholds_up",
            "tdcc_1w_change_400",
            "tdcc_1w_change_600",
            "tdcc_1w_change_800",
            "tdcc_1w_change_1000",
            "tdcc_2w_change_400",
            "tdcc_2w_change_600",
            "tdcc_2w_change_800",
            "tdcc_2w_change_1000",
            "tdcc_3w_change_400",
            "tdcc_3w_change_600",
            "tdcc_3w_change_800",
            "tdcc_3w_change_1000",
            "pre_5d_return",
            "price_ret_1w",
            "price_ret_2w",
            "price_ret_3w",
            "price_ret_4w",
            "relative_ret_1w",
            "relative_ret_2w",
            "relative_ret_3w",
            "relative_ret_4w",
            "volume_ratio_1w",
            "volume_ratio_2w",
            "distance_from_20d_high",
            "distance_from_60d_high",
            "distance_from_ma20",
            "distance_from_ma60",
            "tdcc_price_phase",
            "benchmark_index",
            "market_regime",
            "overheat_bucket",
            "price_confirm_bucket",
            "theme_breadth_score",
            "theme_breadth_level",
            "theme_sync_status",
            "created_at",
            "updated_at",
    ]
    for col in normalized_columns:
        if col not in snapshot.columns:
            snapshot[col] = ""
    normalized = snapshot[normalized_columns].copy()
    normalized["priority_group"] = normalized.apply(priority_group, axis=1)
    return snapshot, normalized, breadth


def priority_group(row: pd.Series) -> str:
    pre5 = to_number(row.get("pre_5d_return"))
    breadth = to_number(row.get("theme_breadth_score"))
    if safe_str(row.get("price_confirm_bucket")) == "weak":
        return "Avoid/low priority"
    if (str(row.get("is_all_thresholds")).lower() == "true" or str(row.get("is_consecutive_2w")).lower() == "true") and breadth >= 3 and (math.isnan(pre5) or pre5 <= 25):
        return "A"
    if not math.isnan(pre5) and pre5 > 30:
        return "C"
    if to_number(row.get("threshold_count")) >= 2:
        return "B"
    return "C"


def build_theme_breadth(snapshot: pd.DataFrame) -> pd.DataFrame:
    rows: list[dict[str, Any]] = []
    for (signal_date, theme), group in snapshot.groupby(["signal_date", "primary_theme"], dropna=False):
        signal_date = safe_str(signal_date)
        theme = safe_str(theme) or "other"
        total = len(group)
        all_count = int(group["is_all_thresholds"].astype(str).str.lower().eq("true").sum())
        c2 = int(group["is_consecutive_2w"].astype(str).str.lower().eq("true").sum())
        c3 = int(group["is_consecutive_3w"].astype(str).str.lower().eq("true").sum())
        high_count = int(((group["has_800"].astype(str).str.lower() == "true") | (group["has_1000"].astype(str).str.lower() == "true")).sum())
        score = min(10, total + all_count * 2 + c2 * 2 + c3 * 3 + high_count)
        if total >= 5 and high_count >= 3:
            sync = "synchronized_accumulation"
            priority = "A"
        elif total <= 2 and high_count <= 1:
            sync = "single_name_concentration"
            priority = "C"
        elif score >= 5:
            sync = "mixed_divergence"
            priority = "B"
        else:
            sync = "neutral"
            priority = "Neutral"
        reps = ",".join(group.sort_values(["threshold_count", "code"], ascending=[False, True])["code"].head(8).astype(str))
        rows.append(
            {
                "signal_date": signal_date,
                "primary_theme": theme,
                "total_signal_count": total,
                "increase_400_count": int(group["has_400"].astype(str).str.lower().eq("true").sum()),
                "increase_600_count": int(group["has_600"].astype(str).str.lower().eq("true").sum()),
                "increase_800_count": int(group["has_800"].astype(str).str.lower().eq("true").sum()),
                "increase_1000_count": int(group["has_1000"].astype(str).str.lower().eq("true").sum()),
                "all_threshold_count": all_count,
                "consecutive_2w_count": c2,
                "consecutive_3w_count": c3,
                "top20_count": "",
                "decrease_400_count": "",
                "decrease_600_count": "",
                "decrease_800_count": "",
                "decrease_1000_count": "",
                "breadth_score": score,
                "sync_status": sync,
                "theme_priority": priority,
                "theme_breadth_level": priority if priority in {"A", "B", "C"} else "Neutral",
                "representative_codes": reps,
                "created_at": now_text(),
                "updated_at": now_text(),
            }
        )
    return pd.DataFrame(rows).sort_values(["breadth_score", "total_signal_count"], ascending=[False, False]).reset_index(drop=True)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Build normalized TDCC signal structures.")
    parser.add_argument(
        "--max-dates",
        type=int,
        default=26,
        help="Maximum latest TDCC weekly snapshots to process. Use 0 with --full-history for all dates.",
    )
    parser.add_argument(
        "--full-history",
        action="store_true",
        help="Process all available TDCC snapshots. Use only in backfill/research jobs.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    max_dates = None if args.full_history or args.max_dates <= 0 else args.max_dates
    TDCC_SIGNALS_DIR.mkdir(parents=True, exist_ok=True)
    snapshot, normalized, breadth = build_snapshot(max_dates=max_dates)
    if not snapshot.empty:
        snapshot = append_update_csv(snapshot, SNAPSHOT_CSV, ["signal_id"], ["signal_date", "code"])
        normalized = append_update_csv(normalized, NORMALIZED_LOG, ["signal_id"], ["signal_date", "code"])
        breadth = append_update_csv(breadth, THEME_BREADTH, ["signal_date", "primary_theme"], ["signal_date", "primary_theme"])
    else:
        write_csv(snapshot, SNAPSHOT_CSV)
        write_csv(normalized, NORMALIZED_LOG)
        write_csv(breadth, THEME_BREADTH)

    phase_dist = pd.DataFrame()
    if not snapshot.empty and "tdcc_price_phase" in snapshot.columns:
        latest_date = safe_str(snapshot["signal_date"].max())
        latest_snapshot = snapshot[snapshot["signal_date"].astype(str) == latest_date].copy()
        phase_dist = (
            latest_snapshot.groupby(["tdcc_consecutive_up_weeks", "tdcc_price_phase"], dropna=False)
            .size()
            .reset_index(name="signal_count")
            .sort_values(["tdcc_consecutive_up_weeks", "signal_count"], ascending=[False, False])
        )

    lines = [
        "# TDCC Normalized Signal Structures",
        "",
        f"- generated_at: `{now_text()}`",
        f"- processed_snapshot_window: `{'full_history' if max_dates is None else f'latest_{max_dates}_dates'}`",
        f"- snapshot_rows: `{len(snapshot)}`",
        f"- normalized_rows: `{len(normalized)}`",
        f"- theme_breadth_rows: `{len(breadth)}`",
        "",
        "## Latest Theme Breadth",
        "",
        markdown_table(
            breadth.assign(_breadth_score=pd.to_numeric(breadth.get("breadth_score", 0), errors="coerce").fillna(0))
            .tail(50)
            .sort_values("_breadth_score", ascending=False)
            .drop(columns=["_breadth_score"], errors="ignore"),
            ["signal_date", "primary_theme", "total_signal_count", "all_threshold_count", "consecutive_2w_count", "breadth_score", "sync_status", "theme_priority", "theme_breadth_level", "representative_codes"],
            50,
        ),
        "",
        "## TDCC Price Phase Distribution",
        "",
        markdown_table(phase_dist, ["tdcc_consecutive_up_weeks", "tdcc_price_phase", "signal_count"], 80),
        "",
    ]
    OUTPUT_MD.write_text("\n".join(lines), encoding="utf-8")
    print(f"Saved: {SNAPSHOT_CSV}")
    print(f"Saved: {NORMALIZED_LOG}")
    print(f"Saved: {THEME_BREADTH}")
    print(f"Saved: {OUTPUT_MD}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
