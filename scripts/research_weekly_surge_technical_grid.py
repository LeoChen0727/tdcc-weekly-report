from __future__ import annotations

from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo

import pandas as pd

from research_weekly_20pct_surge_volume import build_stock_day_frame
from research_weekly_surge_theme_segments import attach_theme_labels


LATEST_DIR = Path("output/latest")
HISTORY_DIR = Path("output/history/research")

OUT_CSV = LATEST_DIR / "weekly_surge_technical_filter_grid_latest.csv"
OUT_MD = LATEST_DIR / "weekly_surge_technical_filter_grid_latest.md"
HISTORY_CSV = HISTORY_DIR / "weekly_surge_technical_filter_grid.csv"

WINDOWS = list(range(1, 11)) + [20]
TARGET_PCT = 10.0
MIN_SELECTED = 100


def now_text() -> str:
    return datetime.now(ZoneInfo("Asia/Taipei")).strftime("%Y-%m-%d %H:%M:%S Asia/Taipei")


def write_csv(df: pd.DataFrame, path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(path, index=False, encoding="utf-8", lineterminator="\n")


def add_technical_features(df: pd.DataFrame) -> pd.DataFrame:
    out = df.sort_values(["stock_id", "date"]).copy()
    numeric_cols = ["open", "high", "low", "close", "volume"]
    for col in numeric_cols:
        if col in out.columns:
            out[col] = pd.to_numeric(out[col], errors="coerce")
    groups = out.groupby("stock_id", group_keys=False)
    out["return_5d_pct"] = groups["close"].pct_change(5) * 100
    out["return_10d_pct"] = groups["close"].pct_change(10) * 100
    out["return_20d_pct"] = groups["close"].pct_change(20) * 100
    out["return_60d_pct"] = groups["close"].pct_change(60) * 100
    out["ma20"] = groups["close"].transform(lambda s: s.rolling(20, min_periods=20).mean())
    out["ma60"] = groups["close"].transform(lambda s: s.rolling(60, min_periods=60).mean())
    out["ema12"] = groups["close"].transform(lambda s: s.ewm(span=12, adjust=False, min_periods=12).mean())
    out["ema23"] = groups["close"].transform(lambda s: s.ewm(span=23, adjust=False, min_periods=23).mean())
    out["ema26"] = groups["close"].transform(lambda s: s.ewm(span=26, adjust=False, min_periods=26).mean())
    out["macd_dif"] = out["ema12"] - out["ema26"]
    out["macd_dea"] = out.groupby("stock_id", group_keys=False)["macd_dif"].transform(
        lambda s: s.ewm(span=9, adjust=False, min_periods=9).mean()
    )
    out["macd_hist"] = out["macd_dif"] - out["macd_dea"]
    out["macd_hist_gt0"] = out["macd_hist"] > 0
    out["distance_ema23_pct"] = (out["close"] / out["ema23"] - 1) * 100
    out["distance_ma20_pct"] = (out["close"] / out["ma20"] - 1) * 100
    out["close_above_ema23"] = out["close"] > out["ema23"]
    out["close_above_ma20"] = out["close"] > out["ma20"]

    delta = groups["close"].diff()
    gain = delta.clip(lower=0)
    loss = -delta.clip(upper=0)
    avg_gain = gain.groupby(out["stock_id"], group_keys=False).transform(lambda s: s.rolling(14, min_periods=14).mean())
    avg_loss = loss.groupby(out["stock_id"], group_keys=False).transform(lambda s: s.rolling(14, min_periods=14).mean())
    rs = avg_gain / avg_loss.replace(0, pd.NA)
    out["rsi14"] = 100 - (100 / (1 + rs))

    low9 = groups["low"].transform(lambda s: s.rolling(9, min_periods=9).min())
    high9 = groups["high"].transform(lambda s: s.rolling(9, min_periods=9).max())
    out["rsv9"] = pd.to_numeric((out["close"] - low9) / (high9 - low9).replace(0, pd.NA) * 100, errors="coerce")
    out["k_value"] = out.groupby("stock_id", group_keys=False)["rsv9"].transform(
        lambda s: pd.to_numeric(s, errors="coerce").ewm(alpha=1 / 3, adjust=False, min_periods=3).mean()
    )
    out["d_value"] = out.groupby("stock_id", group_keys=False)["k_value"].transform(
        lambda s: pd.to_numeric(s, errors="coerce").ewm(alpha=1 / 3, adjust=False, min_periods=3).mean()
    )
    out["kd_bullish_not_overheated"] = (out["k_value"] > out["d_value"]) & (out["k_value"] < 80)
    out["kd_overheated"] = out["k_value"] >= 80

    bb_mid = out["ma20"]
    bb_std = groups["close"].transform(lambda s: s.rolling(20, min_periods=20).std())
    out["bb_width_pct"] = (4 * bb_std / bb_mid) * 100
    out["bb_width_pct_rank_120d"] = out.groupby("stock_id", group_keys=False)["bb_width_pct"].transform(
        lambda s: s.rolling(120, min_periods=60).rank(pct=True)
    )
    out["bb_width_not_extreme"] = out["bb_width_pct_rank_120d"] <= 0.8
    out["near_60d_high_pct"] = (
        out["close"] / groups["high"].transform(lambda s: s.shift(1).rolling(60, min_periods=30).max()) - 1
    ) * 100
    return out


def between(series: pd.Series, low: float, high: float) -> pd.Series:
    return (series >= low) & (series <= high)


def ge(series: pd.Series, value: float) -> pd.Series:
    return series >= value


def build_rules(df: pd.DataFrame) -> list[tuple[str, pd.Series, str]]:
    base = pd.Series(True, index=df.index)
    mainstream_overheated = df["latest_theme_status_group"] == "mainstream_overheated"
    mainstream_supported = df["latest_theme_status_group"] == "mainstream_supported"
    non_mainstream = df["latest_theme_status_group"] == "non_mainstream"
    vol2 = ge(df["start_5d_avg_volume_ratio_vs_prev20"], 2.0)
    vol3 = ge(df["start_5d_avg_volume_ratio_vs_prev20"], 3.0)
    day_vol2 = ge(df["start_day_volume_ratio_vs_prev20"], 2.0)
    prev_vol2 = ge(df["prev_5d_avg_volume_ratio_vs_prev20"], 2.0)
    ret1w_10_30 = between(df["return_5d_pct"], 10, 30)
    ret2w_20_50 = between(df["return_10d_pct"], 20, 50)
    ret20_20_80 = between(df["return_20d_pct"], 20, 80)
    ret20_under50 = df["return_20d_pct"] <= 50
    macd_pos = df["macd_hist_gt0"].fillna(False)
    kd_good = df["kd_bullish_not_overheated"].fillna(False)
    bb_ok = df["bb_width_not_extreme"].fillna(False)
    ema_ok = df["close_above_ema23"].fillna(False) & between(df["distance_ema23_pct"], 0, 25)
    rsi_mid_hot = between(df["rsi14"], 50, 75)

    candidates: list[tuple[str, pd.Series, str]] = [
        ("all_stock__start5d_vol_ge2", vol2, "volume_only"),
        ("all_stock__start5d_vol_ge3", vol3, "volume_only"),
        ("mainstream_supported__start5d_vol_ge2", mainstream_supported & vol2, "theme_volume"),
        ("mainstream_overheated__start5d_vol_ge2", mainstream_overheated & vol2, "theme_volume"),
        ("mainstream_overheated__start5d_vol_ge3", mainstream_overheated & vol3, "theme_volume"),
        ("mainstream_overheated__prev5d_vol_ge2", mainstream_overheated & prev_vol2, "theme_volume"),
        ("mainstream_overheated__day_vol_ge2", mainstream_overheated & day_vol2, "theme_volume"),
        ("non_mainstream__start5d_vol_ge2", non_mainstream & vol2, "theme_volume"),
        ("mainstream_overheated__vol2_macd_pos", mainstream_overheated & vol2 & macd_pos, "theme_volume_technical"),
        ("mainstream_overheated__vol2_kd_good", mainstream_overheated & vol2 & kd_good, "theme_volume_technical"),
        ("mainstream_overheated__vol2_bb_not_extreme", mainstream_overheated & vol2 & bb_ok, "theme_volume_technical"),
        ("mainstream_overheated__vol2_ema23_ok", mainstream_overheated & vol2 & ema_ok, "theme_volume_technical"),
        ("mainstream_overheated__vol2_rsi50_75", mainstream_overheated & vol2 & rsi_mid_hot, "theme_volume_technical"),
        ("mainstream_overheated__vol2_macd_kd", mainstream_overheated & vol2 & macd_pos & kd_good, "theme_volume_technical"),
        ("mainstream_overheated__vol2_macd_bb", mainstream_overheated & vol2 & macd_pos & bb_ok, "theme_volume_technical"),
        ("mainstream_overheated__vol2_kd_bb", mainstream_overheated & vol2 & kd_good & bb_ok, "theme_volume_technical"),
        ("mainstream_overheated__vol2_ret1w10_30", mainstream_overheated & vol2 & ret1w_10_30, "theme_volume_momentum"),
        ("mainstream_overheated__vol2_ret2w20_50", mainstream_overheated & vol2 & ret2w_20_50, "theme_volume_momentum"),
        ("mainstream_overheated__vol2_ret20_20_80", mainstream_overheated & vol2 & ret20_20_80, "theme_volume_momentum"),
        ("mainstream_overheated__vol2_ret20_under50_macd", mainstream_overheated & vol2 & ret20_under50 & macd_pos, "theme_volume_momentum"),
        ("mainstream_overheated__vol2_ret2w20_50_macd", mainstream_overheated & vol2 & ret2w_20_50 & macd_pos, "theme_volume_momentum"),
        ("mainstream_overheated__vol2_ret2w20_50_kd", mainstream_overheated & vol2 & ret2w_20_50 & kd_good, "theme_volume_momentum"),
        ("mainstream_overheated__vol2_ret2w20_50_bb", mainstream_overheated & vol2 & ret2w_20_50 & bb_ok, "theme_volume_momentum"),
        ("mainstream_overheated__vol2_ret1w10_30_ret2w20_50", mainstream_overheated & vol2 & ret1w_10_30 & ret2w_20_50, "theme_volume_momentum"),
        ("mainstream_overheated__vol2_ret1w10_30_ret2w20_50_macd", mainstream_overheated & vol2 & ret1w_10_30 & ret2w_20_50 & macd_pos, "theme_volume_momentum"),
        ("mainstream_overheated__vol2_ret1w10_30_ret2w20_50_kd", mainstream_overheated & vol2 & ret1w_10_30 & ret2w_20_50 & kd_good, "theme_volume_momentum"),
        ("mainstream_overheated__vol2_ret1w10_30_ret2w20_50_bb", mainstream_overheated & vol2 & ret1w_10_30 & ret2w_20_50 & bb_ok, "theme_volume_momentum"),
    ]
    return [(name, mask.fillna(False) if hasattr(mask, "fillna") else mask, family) for name, mask, family in candidates]


def summarize_rule(df: pd.DataFrame, rule_name: str, family: str, mask: pd.Series, window: int) -> dict[str, object]:
    picked = df[mask]
    hit_col = f"next_open_to_d{window}_high_10pct_hit"
    ret_col = f"next_open_to_d{window}_high_return_pct"
    hits = picked[picked[hit_col]]
    total_hits = int(df[hit_col].sum())
    return {
        "label_type": "provisional_latest_stock_label",
        "rule_family": family,
        "rule_name": rule_name,
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
        "median_signal_close_to_next_open_gap_pct": round(picked["signal_close_to_next_open_gap_pct"].median(), 2) if len(picked) else 0,
        "avg_return_5d_pct": round(picked["return_5d_pct"].mean(), 2) if len(picked) else 0,
        "avg_return_10d_pct": round(picked["return_10d_pct"].mean(), 2) if len(picked) else 0,
        "avg_return_20d_pct": round(picked["return_20d_pct"].mean(), 2) if len(picked) else 0,
        "sample_status": "provisional_latest_label_only" if len(picked) >= MIN_SELECTED else "insufficient_sample",
    }


def build_summary(df: pd.DataFrame) -> pd.DataFrame:
    rows: list[dict[str, object]] = []
    for rule_name, mask, family in build_rules(df):
        for window in WINDOWS:
            rows.append(summarize_rule(df, rule_name, family, mask, window))
    out = pd.DataFrame(rows)
    return out.sort_values(["target_window", "hit_rate_pct", "selected_stock_days"], ascending=[True, False, False]).reset_index(drop=True)


def df_to_md(df: pd.DataFrame, limit: int = 30) -> str:
    if df.empty:
        return "_No rows._"
    return df.head(limit).to_markdown(index=False)


def build_markdown(summary: pd.DataFrame, df: pd.DataFrame) -> str:
    lines: list[str] = []
    lines.append("# Next-Open +10pct Technical Filter Grid")
    lines.append("")
    lines.append(f"- generated_at: `{now_text()}`")
    lines.append("- entry_basis: D+1 open.")
    lines.append("- target: D+1 open to D+1 / ... / D+10 / D+20 max high >= 10%.")
    lines.append("- label caveat: this version uses latest stock-level theme labels for exploration only, so mainstream/non-mainstream fields can contain look-ahead bias.")
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

    keep = [
        "rule_family",
        "rule_name",
        "selected_stock_days",
        "hit_rate_pct",
        "median_next_open_to_high_return_pct",
        "avg_signal_close_to_next_open_gap_pct",
        "coverage_of_all_hits_pct",
        "sample_status",
    ]
    for window in [f"D+{value}" for value in WINDOWS]:
        part = summary[(summary["target_window"] == window) & (summary["selected_stock_days"] >= MIN_SELECTED)]
        lines.append(f"## Best {window} Rules")
        lines.append("")
        lines.append(df_to_md(part[keep], limit=30))
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
