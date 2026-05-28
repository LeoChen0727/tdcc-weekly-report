from __future__ import annotations

from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo

import pandas as pd

from research_weekly_20pct_surge_volume import build_stock_day_frame
from research_weekly_surge_technical_grid import add_technical_features
from research_weekly_surge_theme_segments import attach_theme_labels


LATEST_DIR = Path("output/latest")
HISTORY_DIR = Path("output/history/research")
TDCC_HISTORY_DIR = Path("output/history/tdcc")
MARKET_HISTORY = Path("data/market_index_history.csv")

OUT_CSV = LATEST_DIR / "weekly_surge_multifactor_filter_grid_latest.csv"
OUT_MD = LATEST_DIR / "weekly_surge_multifactor_filter_grid_latest.md"
HISTORY_CSV = HISTORY_DIR / "weekly_surge_multifactor_filter_grid.csv"

WINDOWS = [5, 10, 20]
TARGET_PCT = 10.0
MIN_SELECTED = 100


def now_text() -> str:
    return datetime.now(ZoneInfo("Asia/Taipei")).strftime("%Y-%m-%d %H:%M:%S Asia/Taipei")


def write_csv(df: pd.DataFrame, path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(path, index=False, encoding="utf-8", lineterminator="\n")


def normalize_stock_id(value: object) -> str:
    text = str(value).strip()
    if text.endswith(".0"):
        text = text[:-2]
    return text.zfill(4) if text.isdigit() and len(text) < 4 else text


def normalize_date(value: object) -> str:
    return str(value).strip().replace("-", "").replace("/", "")[:8]


def load_tdcc_context() -> pd.DataFrame:
    frames: list[pd.DataFrame] = []
    for path in sorted(TDCC_HISTORY_DIR.glob("tdcc_holder_ratio_*.csv")):
        try:
            df = pd.read_csv(path, dtype=str, keep_default_na=False)
        except Exception:
            continue
        required = {"date", "code", "over_400_pct", "over_600_pct", "over_800_pct", "over_1000_pct"}
        if not required.issubset(df.columns):
            continue
        df = df.copy()
        df["stock_id"] = df["code"].map(normalize_stock_id)
        df["tdcc_date"] = df["date"].map(normalize_date)
        for col in ["over_400_pct", "over_600_pct", "over_800_pct", "over_1000_pct"]:
            df[col] = pd.to_numeric(df[col], errors="coerce")
        frames.append(df[["stock_id", "tdcc_date", "over_400_pct", "over_600_pct", "over_800_pct", "over_1000_pct"]])
    if not frames:
        return pd.DataFrame()

    tdcc = pd.concat(frames, ignore_index=True)
    tdcc = tdcc.dropna(subset=["over_400_pct", "over_800_pct", "over_1000_pct"])
    tdcc = tdcc.sort_values(["stock_id", "tdcc_date"]).drop_duplicates(["stock_id", "tdcc_date"], keep="last")
    group = tdcc.groupby("stock_id", group_keys=False)
    for level in ["400", "600", "800", "1000"]:
        col = f"over_{level}_pct"
        tdcc[f"over_{level}_change_1w"] = group[col].diff()

    tdcc["tdcc_all_thresholds_up"] = (
        (tdcc["over_400_change_1w"] > 0)
        & (tdcc["over_600_change_1w"] > 0)
        & (tdcc["over_800_change_1w"] > 0)
        & (tdcc["over_1000_change_1w"] > 0)
    )
    tdcc["tdcc_high_thresholds_up"] = (tdcc["over_800_change_1w"] > 0) & (tdcc["over_1000_change_1w"] > 0)
    tdcc["tdcc_any_high_level_up"] = (tdcc["over_800_change_1w"] > 0) | (tdcc["over_1000_change_1w"] > 0)
    tdcc["tdcc_high_change_sum"] = tdcc["over_800_change_1w"].fillna(0) + tdcc["over_1000_change_1w"].fillna(0)
    tdcc["tdcc_available"] = True

    streaks: list[int] = []
    for _, part in tdcc.groupby("stock_id", sort=False):
        current = 0
        for flag in part["tdcc_high_thresholds_up"].fillna(False).tolist():
            current = current + 1 if flag else 0
            streaks.append(current)
    tdcc["tdcc_high_up_streak"] = streaks
    return tdcc


def attach_tdcc_context(df: pd.DataFrame) -> pd.DataFrame:
    tdcc = load_tdcc_context()
    out = df.copy()
    out["stock_id"] = out["stock_id"].map(normalize_stock_id)
    out["date_dt"] = pd.to_datetime(out["date"].map(normalize_date), format="%Y%m%d", errors="coerce")
    if tdcc.empty:
        out["tdcc_available"] = False
        return out

    tdcc = tdcc.copy()
    tdcc["tdcc_date_dt"] = pd.to_datetime(tdcc["tdcc_date"], format="%Y%m%d", errors="coerce")
    pieces: list[pd.DataFrame] = []
    for stock_id, part in out.groupby("stock_id", sort=False):
        tpart = tdcc[tdcc["stock_id"] == stock_id].sort_values("tdcc_date_dt")
        if tpart.empty:
            temp = part.copy()
            temp["tdcc_available"] = False
            pieces.append(temp)
            continue
        merged = pd.merge_asof(
            part.sort_values("date_dt"),
            tpart.sort_values("tdcc_date_dt"),
            left_on="date_dt",
            right_on="tdcc_date_dt",
            by="stock_id",
            direction="backward",
        )
        pieces.append(merged)
    result = pd.concat(pieces, ignore_index=True)
    result["tdcc_available"] = result["tdcc_available"].map(lambda value: bool(value) if pd.notna(value) else False)
    for col in ["tdcc_all_thresholds_up", "tdcc_high_thresholds_up", "tdcc_any_high_level_up"]:
        if col not in result.columns:
            result[col] = False
        result[col] = result[col].map(lambda value: bool(value) if pd.notna(value) else False)
    result["tdcc_high_up_streak"] = pd.to_numeric(result.get("tdcc_high_up_streak", 0), errors="coerce").fillna(0)
    result["tdcc_high_change_sum"] = pd.to_numeric(result.get("tdcc_high_change_sum", 0), errors="coerce").fillna(0)
    return result


def load_market_context() -> pd.DataFrame:
    if not MARKET_HISTORY.exists():
        return pd.DataFrame()
    market = pd.read_csv(MARKET_HISTORY, dtype=str, keep_default_na=False)
    if market.empty:
        return market
    market["date"] = market["date"].map(normalize_date)
    market["index_code"] = market["index_code"].astype(str).str.upper().replace({"TPEX": "TPEX", "TPEX ": "TPEX"})
    for col in ["close", "return_5d", "return_20d", "ma20", "ma60"]:
        market[col] = pd.to_numeric(market.get(col), errors="coerce")
    market["above_ma20_bool"] = market.get("above_ma20", "").astype(str).str.lower().isin(["true", "1", "yes"])
    market["above_ma60_bool"] = market.get("above_ma60", "").astype(str).str.lower().isin(["true", "1", "yes"])
    market["derived_market_regime"] = "range_or_unclear"
    strong = market["above_ma20_bool"] & market["above_ma60_bool"] & (market["return_20d"] > 5)
    mild = market["above_ma20_bool"] & market["above_ma60_bool"] & (market["return_20d"] > 0)
    weak = (~market["above_ma20_bool"]) & (~market["above_ma60_bool"])
    market.loc[strong, "derived_market_regime"] = "strong_bull"
    market.loc[mild & ~strong, "derived_market_regime"] = "mild_bull"
    market.loc[weak, "derived_market_regime"] = "weak_or_correction"
    return market[["date", "index_code", "derived_market_regime", "return_5d", "return_20d", "above_ma20_bool", "above_ma60_bool"]]


def attach_market_context(df: pd.DataFrame) -> pd.DataFrame:
    market = load_market_context()
    out = df.copy()
    out["market_norm"] = out["market"].astype(str).str.upper().replace({"TPEX": "TPEX", "TPEX ": "TPEX"})
    out["date"] = out["date"].map(normalize_date)
    if market.empty:
        out["derived_market_regime"] = "missing_market_history"
        return out
    return out.merge(
        market,
        how="left",
        left_on=["date", "market_norm"],
        right_on=["date", "index_code"],
    )


def between(series: pd.Series, low: float, high: float) -> pd.Series:
    return (series >= low) & (series <= high)


def build_rules(df: pd.DataFrame) -> list[tuple[str, pd.Series, str, str]]:
    vol2 = df["start_5d_avg_volume_ratio_vs_prev20"] >= 2
    vol3 = df["start_5d_avg_volume_ratio_vs_prev20"] >= 3
    mainstream_overheated = df["latest_theme_status_group"] == "mainstream_overheated"
    mainstream_supported = df["latest_theme_status_group"] == "mainstream_supported"
    non_mainstream = df["latest_theme_status_group"] == "non_mainstream"
    market_bull = df["derived_market_regime"].isin(["strong_bull", "mild_bull"])
    market_strong = df["derived_market_regime"].eq("strong_bull")
    tdcc_available = df["tdcc_available"].fillna(False)
    tdcc_high_up = df["tdcc_high_thresholds_up"].fillna(False)
    tdcc_all_up = df["tdcc_all_thresholds_up"].fillna(False)
    tdcc_high_streak1 = df["tdcc_high_up_streak"] >= 1
    tdcc_high_streak2 = df["tdcc_high_up_streak"] >= 2
    tdcc_high_sum_pos = df["tdcc_high_change_sum"] > 0
    macd_pos = df["macd_hist_gt0"].fillna(False)
    kd_good = df["kd_bullish_not_overheated"].fillna(False)
    bb_ok = df["bb_width_not_extreme"].fillna(False)
    rsi_ok = between(df["rsi14"], 50, 75)
    ret2w = between(df["return_10d_pct"], 20, 50)
    ret1w = between(df["return_5d_pct"], 10, 30)

    candidates: list[tuple[str, pd.Series, str, str]] = [
        ("all_stock__vol2__market_bull", vol2 & market_bull, "market_volume", "strict_market"),
        ("all_stock__vol2__market_strong_bull", vol2 & market_strong, "market_volume", "strict_market"),
        ("all_stock__vol2__tdcc_high_up", vol2 & tdcc_available & tdcc_high_up, "tdcc_volume", "strict_tdcc"),
        ("all_stock__vol2__tdcc_all_up", vol2 & tdcc_available & tdcc_all_up, "tdcc_volume", "strict_tdcc"),
        ("all_stock__vol2__tdcc_high_streak2", vol2 & tdcc_available & tdcc_high_streak2, "tdcc_volume", "strict_tdcc"),
        ("mainstream_supported__vol2__market_bull", mainstream_supported & vol2 & market_bull, "theme_market_volume", "latest_theme_plus_strict_market"),
        ("mainstream_overheated__vol2__market_bull", mainstream_overheated & vol2 & market_bull, "theme_market_volume", "latest_theme_plus_strict_market"),
        ("mainstream_overheated__vol3__market_bull", mainstream_overheated & vol3 & market_bull, "theme_market_volume", "latest_theme_plus_strict_market"),
        ("mainstream_overheated__vol2__tdcc_high_up", mainstream_overheated & vol2 & tdcc_available & tdcc_high_up, "theme_tdcc_volume", "latest_theme_plus_strict_tdcc"),
        ("mainstream_overheated__vol2__tdcc_all_up", mainstream_overheated & vol2 & tdcc_available & tdcc_all_up, "theme_tdcc_volume", "latest_theme_plus_strict_tdcc"),
        ("mainstream_overheated__vol2__tdcc_high_sum_pos", mainstream_overheated & vol2 & tdcc_available & tdcc_high_sum_pos, "theme_tdcc_volume", "latest_theme_plus_strict_tdcc"),
        ("mainstream_overheated__vol2__tdcc_streak1", mainstream_overheated & vol2 & tdcc_available & tdcc_high_streak1, "theme_tdcc_volume", "latest_theme_plus_strict_tdcc"),
        ("mainstream_overheated__vol2__market_bull__tdcc_high_up", mainstream_overheated & vol2 & market_bull & tdcc_available & tdcc_high_up, "theme_market_tdcc_volume", "latest_theme_plus_strict_market_tdcc"),
        ("mainstream_overheated__vol2__market_bull__tdcc_all_up", mainstream_overheated & vol2 & market_bull & tdcc_available & tdcc_all_up, "theme_market_tdcc_volume", "latest_theme_plus_strict_market_tdcc"),
        ("mainstream_overheated__vol2__market_bull__bb_ok", mainstream_overheated & vol2 & market_bull & bb_ok, "theme_market_technical", "latest_theme_plus_strict_market"),
        ("mainstream_overheated__vol2__market_bull__kd_good", mainstream_overheated & vol2 & market_bull & kd_good, "theme_market_technical", "latest_theme_plus_strict_market"),
        ("mainstream_overheated__vol2__market_bull__rsi50_75", mainstream_overheated & vol2 & market_bull & rsi_ok, "theme_market_technical", "latest_theme_plus_strict_market"),
        ("mainstream_overheated__vol2__market_bull__macd", mainstream_overheated & vol2 & market_bull & macd_pos, "theme_market_technical", "latest_theme_plus_strict_market"),
        ("mainstream_overheated__vol2__ret2w20_50__tdcc_high_up", mainstream_overheated & vol2 & ret2w & tdcc_available & tdcc_high_up, "theme_tdcc_momentum", "latest_theme_plus_strict_tdcc"),
        ("mainstream_overheated__vol2__ret1w10_30_ret2w20_50__tdcc_high_up", mainstream_overheated & vol2 & ret1w & ret2w & tdcc_available & tdcc_high_up, "theme_tdcc_momentum", "latest_theme_plus_strict_tdcc"),
        ("non_mainstream__vol2__tdcc_high_up", non_mainstream & vol2 & tdcc_available & tdcc_high_up, "non_mainstream_tdcc", "latest_theme_plus_strict_tdcc"),
    ]
    return [(name, mask.fillna(False), family, source) for name, mask, family, source in candidates]


def summarize_rule(df: pd.DataFrame, rule_name: str, family: str, source_type: str, mask: pd.Series, window: int) -> dict[str, object]:
    picked = df[mask]
    hit_col = f"next_open_to_d{window}_high_10pct_hit"
    ret_col = f"next_open_to_d{window}_high_return_pct"
    hits = picked[picked[hit_col]]
    total_hits = int(df[hit_col].sum())
    return {
        "rule_name": rule_name,
        "rule_family": family,
        "source_type": source_type,
        "target_window": f"D+{window}",
        "entry_basis": "D+1_open",
        "target_return_pct": TARGET_PCT,
        "selected_stock_days": len(picked),
        "hit_stock_days": len(hits),
        "hit_rate_pct": round(len(hits) / len(picked) * 100, 2) if len(picked) else 0,
        "coverage_of_all_hits_pct": round(len(hits) / total_hits * 100, 2) if total_hits else 0,
        "selected_unique_stocks": picked["stock_id"].nunique(),
        "hit_unique_stocks": hits["stock_id"].nunique(),
        "median_next_open_to_high_return_pct": round(picked[ret_col].median(), 2) if len(picked) else 0,
        "avg_next_open_to_high_return_pct": round(picked[ret_col].mean(), 2) if len(picked) else 0,
        "avg_signal_close_to_next_open_gap_pct": round(picked["signal_close_to_next_open_gap_pct"].mean(), 2) if len(picked) else 0,
        "tdcc_available_rate_pct": round(picked["tdcc_available"].mean() * 100, 2) if len(picked) and "tdcc_available" in picked else 0,
        "top_market_regime_counts": top_counts(picked, "derived_market_regime"),
        "top_theme_status_counts": top_counts(picked, "latest_theme_status_group"),
        "sample_status": sample_status(source_type, len(picked)),
    }


def sample_status(source_type: str, selected_count: int) -> str:
    if selected_count < MIN_SELECTED:
        return "insufficient_sample"
    if "latest_theme" in source_type:
        return "provisional_latest_theme_label"
    return "ok_initial_sample"


def top_counts(df: pd.DataFrame, col: str, limit: int = 4) -> str:
    if df.empty or col not in df.columns:
        return ""
    counts = df[col].fillna("").astype(str).replace({"": "blank"}).value_counts().head(limit)
    return "; ".join(f"{k}={v}" for k, v in counts.items())


def build_summary(df: pd.DataFrame) -> pd.DataFrame:
    rows: list[dict[str, object]] = []
    for rule_name, mask, family, source_type in build_rules(df):
        for window in WINDOWS:
            rows.append(summarize_rule(df, rule_name, family, source_type, mask, window))
    out = pd.DataFrame(rows)
    return out.sort_values(["target_window", "hit_rate_pct", "selected_stock_days"], ascending=[True, False, False]).reset_index(drop=True)


def df_to_md(df: pd.DataFrame, limit: int = 30) -> str:
    if df.empty:
        return "_No rows._"
    return df.head(limit).to_markdown(index=False)


def build_markdown(summary: pd.DataFrame, df: pd.DataFrame) -> str:
    lines: list[str] = []
    lines.append("# Weekly Surge Multifactor Filter Grid")
    lines.append("")
    lines.append(f"- generated_at: `{now_text()}`")
    lines.append("- entry_basis: D+1 open.")
    lines.append("- target: D+1 open to D+5 / D+10 / D+20 max high >= 10%.")
    lines.append("- strict parts: market regime is derived from historical index data; TDCC uses latest available weekly holder ratio as of each stock date.")
    lines.append("- caveat: rules containing latest theme labels are still exploratory and can contain look-ahead bias until daily theme history accumulates.")
    lines.append("- use: parameter discovery only; do not change core model weights from this table.")
    lines.append("")
    total = len(df)
    lines.append("## Overall Base Hit Rates")
    lines.append("")
    lines.append("| Window | Hit Count | Base Hit Rate |")
    lines.append("|---|---:|---:|")
    for window in WINDOWS:
        hit_col = f"next_open_to_d{window}_high_10pct_hit"
        hits = int(df[hit_col].sum())
        lines.append(f"| D+{window} | {hits} | {hits / total * 100:.2f}% |")
    lines.append("")
    lines.append("## Data Availability")
    lines.append("")
    lines.append(f"- stock_day_count: `{len(df)}`")
    lines.append(f"- tdcc_available_stock_days: `{int(df['tdcc_available'].sum())}`")
    lines.append(f"- tdcc_available_rate: `{df['tdcc_available'].mean() * 100:.2f}%`")
    lines.append(f"- market_regime_counts: `{top_counts(df, 'derived_market_regime', limit=8)}`")
    lines.append("")

    keep = [
        "rule_family",
        "rule_name",
        "source_type",
        "selected_stock_days",
        "hit_rate_pct",
        "median_next_open_to_high_return_pct",
        "avg_signal_close_to_next_open_gap_pct",
        "tdcc_available_rate_pct",
        "sample_status",
    ]
    for window in ["D+5", "D+10", "D+20"]:
        part = summary[(summary["target_window"] == window) & (summary["selected_stock_days"] >= MIN_SELECTED)]
        lines.append(f"## Best {window} Rules")
        lines.append("")
        lines.append(df_to_md(part[keep], limit=30))
        lines.append("")
        small = summary[
            (summary["target_window"] == window)
            & (summary["selected_stock_days"] >= 30)
            & (summary["selected_stock_days"] < MIN_SELECTED)
        ]
        lines.append(f"## Small-Sample High-Hit {window} Watchlist")
        lines.append("")
        lines.append("- These rows are useful for hypothesis discovery only. They are not mature enough for ranking weights.")
        lines.append("")
        lines.append(df_to_md(small[keep], limit=12))
        lines.append("")
    return "\n".join(lines) + "\n"


def main() -> int:
    LATEST_DIR.mkdir(parents=True, exist_ok=True)
    HISTORY_DIR.mkdir(parents=True, exist_ok=True)
    df = build_stock_day_frame()
    if df.empty:
        raise RuntimeError("no stock day frame built")
    df = attach_theme_labels(df)
    df = add_technical_features(df)
    df = attach_tdcc_context(df)
    df = attach_market_context(df)
    summary = build_summary(df)
    write_csv(summary, OUT_CSV)
    write_csv(summary, HISTORY_CSV)
    OUT_MD.write_text(build_markdown(summary, df), encoding="utf-8", newline="\n")
    print(f"Saved: {OUT_CSV} rows={len(summary)}")
    print(f"Saved: {OUT_MD}")
    print(f"Saved: {HISTORY_CSV} rows={len(summary)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
