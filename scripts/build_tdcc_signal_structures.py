from __future__ import annotations

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
    load_price_history,
    markdown_table,
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


def load_theme_map() -> dict[str, dict[str, str]]:
    df = read_csv(THEME_MAP, dtype=str)
    if df.empty:
        return {}
    df["code"] = df["code"].map(normalize_code)
    return {row["code"]: row.to_dict() for _, row in df.iterrows()}


def load_tdcc_snapshots() -> list[tuple[str, pd.DataFrame]]:
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
    out: list[tuple[str, pd.DataFrame]] = []
    for date, path in sorted(unique.items()):
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


def price_metrics(code: str, signal_date: str) -> dict[str, Any]:
    price = load_price_history(code)
    out: dict[str, Any] = {}
    if price.empty:
        return out
    part = price[price["date"] <= signal_date].copy()
    if part.empty:
        return out
    row = part.iloc[-1]
    close = to_number(row.get("close"))
    for days in [5, 10, 20, 60]:
        if len(part) > days:
            out[f"pre_{days}d_return" if days in [5, 10, 20] else "price_return_60d"] = (close / to_number(part.iloc[-days - 1].get("close")) - 1) * 100
            out[f"price_return_{days}d"] = (close / to_number(part.iloc[-days - 1].get("close")) - 1) * 100
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
    return out


def build_snapshot() -> tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    snapshots = load_tdcc_snapshots()
    if not snapshots:
        raise FileNotFoundError("Missing TDCC holder ratio snapshots")
    signal_date, latest = snapshots[-1]
    theme_map = load_theme_map()
    rows: list[dict[str, Any]] = []

    for _, row in latest.iterrows():
        code = normalize_code(row.get("code", ""))
        if not code:
            continue
        deltas = {th: latest_delta(tdcc_series(snapshots, code, th)) for th in THRESHOLDS}
        has = {th: (not math.isnan(deltas[th]) and deltas[th] > 0) for th in THRESHOLDS}
        if not any(has.values()):
            continue
        theme = theme_map.get(code, {})
        streaks = {th: streak_weeks(tdcc_series(snapshots, code, th)) for th in THRESHOLDS}
        all_streak = min(streaks.values()) if streaks else 0
        metrics = price_metrics(code, signal_date)
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
            "created_at": now_text(),
            "updated_at": now_text(),
        }
        for th in THRESHOLDS:
            ratio = ratio_to_high(tdcc_series(snapshots, code, th))
            item[f"tdcc_{th}_ratio_20w_high"] = ratio
            item[f"tdcc_{th}_near_20w_high"] = ratio >= 0.95 if not math.isnan(ratio) else ""
        item.update(metrics)
        item["is_price_not_reacted"] = to_number(item.get("price_return_20d")) <= 10
        item["is_quiet_accumulation"] = item["is_consecutive_2w"] and (item["has_800"] or item["has_1000"]) and item["is_price_not_reacted"]
        item["is_early_breakout"] = item.get("breakout_20d") and to_number(item.get("price_return_20d")) <= 15
        item["abm_score"] = ""
        item["abm_rank"] = ""
        item["setup_type"] = ""
        item["abm_reason"] = ""
        rows.append(item)

    snapshot = pd.DataFrame(rows)
    if snapshot.empty:
        return snapshot, pd.DataFrame(), pd.DataFrame()

    breadth = build_theme_breadth(snapshot)
    score_map = breadth.set_index("primary_theme")["breadth_score"].to_dict() if not breadth.empty else {}
    sync_map = breadth.set_index("primary_theme")["sync_status"].to_dict() if not breadth.empty else {}
    snapshot["theme_breadth_score"] = snapshot["primary_theme"].map(score_map).fillna(0)
    snapshot["theme_sync_status"] = snapshot["primary_theme"].map(sync_map).fillna("neutral")

    normalized = snapshot[
        [
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
            "pre_5d_return",
            "overheat_bucket",
            "price_confirm_bucket",
            "theme_breadth_score",
            "created_at",
            "updated_at",
        ]
    ].copy()
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
    signal_date = safe_str(snapshot["signal_date"].max())
    for theme, group in snapshot.groupby("primary_theme"):
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
                "representative_codes": reps,
                "created_at": now_text(),
                "updated_at": now_text(),
            }
        )
    return pd.DataFrame(rows).sort_values(["breadth_score", "total_signal_count"], ascending=[False, False]).reset_index(drop=True)


def main() -> int:
    TDCC_SIGNALS_DIR.mkdir(parents=True, exist_ok=True)
    snapshot, normalized, breadth = build_snapshot()
    if not snapshot.empty:
        snapshot = append_update_csv(snapshot, SNAPSHOT_CSV, ["signal_id"], ["signal_date", "code"])
        normalized = append_update_csv(normalized, NORMALIZED_LOG, ["signal_id"], ["signal_date", "code"])
        breadth = append_update_csv(breadth, THEME_BREADTH, ["signal_date", "primary_theme"], ["signal_date", "primary_theme"])
    else:
        write_csv(snapshot, SNAPSHOT_CSV)
        write_csv(normalized, NORMALIZED_LOG)
        write_csv(breadth, THEME_BREADTH)

    lines = [
        "# TDCC Normalized Signal Structures",
        "",
        f"- generated_at: `{now_text()}`",
        f"- snapshot_rows: `{len(snapshot)}`",
        f"- normalized_rows: `{len(normalized)}`",
        f"- theme_breadth_rows: `{len(breadth)}`",
        "",
        "## Latest Theme Breadth",
        "",
        markdown_table(breadth.tail(50).sort_values("breadth_score", ascending=False), ["signal_date", "primary_theme", "total_signal_count", "all_threshold_count", "consecutive_2w_count", "breadth_score", "sync_status", "theme_priority", "representative_codes"], 50),
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
