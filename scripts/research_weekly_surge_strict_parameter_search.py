from __future__ import annotations

from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo

import pandas as pd

from research_weekly_20pct_surge_volume import build_stock_day_frame
from research_weekly_surge_multifactor_grid import attach_market_context, attach_tdcc_context, write_csv
from research_weekly_surge_technical_grid import add_technical_features


LATEST_DIR = Path("output/latest")
HISTORY_DIR = Path("output/history/research")

OUT_CSV = LATEST_DIR / "weekly_surge_strict_parameter_search_latest.csv"
OUT_MD = LATEST_DIR / "weekly_surge_strict_parameter_search_latest.md"
HISTORY_CSV = HISTORY_DIR / "weekly_surge_strict_parameter_search.csv"

WINDOWS = list(range(1, 11)) + [20]
TARGET_PCT = 10.0
MIN_SELECTED = 100


def now_text() -> str:
    return datetime.now(ZoneInfo("Asia/Taipei")).strftime("%Y-%m-%d %H:%M:%S Asia/Taipei")


def between(series: pd.Series, low: float, high: float) -> pd.Series:
    return (series >= low) & (series <= high)


def build_parameter_masks(df: pd.DataFrame) -> dict[str, pd.Series]:
    masks: dict[str, pd.Series] = {
        "vol5_avg_ge_1_5": df["start_5d_avg_volume_ratio_vs_prev20"] >= 1.5,
        "vol5_avg_ge_2": df["start_5d_avg_volume_ratio_vs_prev20"] >= 2,
        "vol5_avg_ge_3": df["start_5d_avg_volume_ratio_vs_prev20"] >= 3,
        "day_vol_ge_1_5": df["start_day_volume_ratio_vs_prev20"] >= 1.5,
        "day_vol_ge_2": df["start_day_volume_ratio_vs_prev20"] >= 2,
        "market_bull": df["derived_market_regime"].isin(["strong_bull", "mild_bull"]),
        "market_strong_bull": df["derived_market_regime"].eq("strong_bull"),
        "tdcc_high_up": df["tdcc_high_thresholds_up"].fillna(False),
        "tdcc_all_up": df["tdcc_all_thresholds_up"].fillna(False),
        "tdcc_high_streak2": df["tdcc_high_up_streak"] >= 2,
        "tdcc_high_change_pos": df["tdcc_high_change_sum"] > 0,
        "macd_hist_pos": df["macd_hist_gt0"].fillna(False),
        "kd_bullish_not_overheated": df["kd_bullish_not_overheated"].fillna(False),
        "bb_width_not_extreme": df["bb_width_not_extreme"].fillna(False),
        "rsi_50_75": between(df["rsi14"], 50, 75),
        "rsi_55_80": between(df["rsi14"], 55, 80),
        "close_above_ema23": df["close_above_ema23"].fillna(False),
        "close_above_ma20": df["close_above_ma20"].fillna(False),
        "distance_ema23_0_20": between(df["distance_ema23_pct"], 0, 20),
        "return_5d_5_20": between(df["return_5d_pct"], 5, 20),
        "return_5d_10_30": between(df["return_5d_pct"], 10, 30),
        "return_10d_10_40": between(df["return_10d_pct"], 10, 40),
        "return_10d_20_50": between(df["return_10d_pct"], 20, 50),
        "return_20d_10_60": between(df["return_20d_pct"], 10, 60),
        "return_20d_under_50": df["return_20d_pct"] <= 50,
        "near_60d_high_5pct": df["near_60d_high_pct"] >= -5,
        "near_60d_high_10pct": df["near_60d_high_pct"] >= -10,
    }
    return {name: mask.fillna(False) for name, mask in masks.items()}


def parameter_family(name: str) -> str:
    if name.startswith("vol") or name.startswith("day_vol"):
        return "volume"
    if name.startswith("tdcc"):
        return "tdcc"
    if name.startswith("market"):
        return "market"
    if name.startswith("return") or name.startswith("near"):
        return "price_position"
    return "technical"


def build_combinations(masks: dict[str, pd.Series]) -> list[tuple[str, pd.Series, str]]:
    volume_groups = [
        [],
        ["vol5_avg_ge_1_5"],
        ["vol5_avg_ge_2"],
        ["vol5_avg_ge_3"],
        ["day_vol_ge_2"],
    ]
    market_groups = [[], ["market_bull"], ["market_strong_bull"]]
    tdcc_groups = [[], ["tdcc_high_up"], ["tdcc_all_up"], ["tdcc_high_streak2"]]
    technical_groups = [
        [],
        ["macd_hist_pos"],
        ["kd_bullish_not_overheated"],
        ["bb_width_not_extreme"],
        ["rsi_50_75"],
        ["close_above_ema23"],
        ["macd_hist_pos", "kd_bullish_not_overheated"],
        ["kd_bullish_not_overheated", "bb_width_not_extreme"],
    ]
    price_groups = [
        [],
        ["return_5d_5_20"],
        ["return_5d_10_30"],
        ["return_10d_10_40"],
        ["return_10d_20_50"],
        ["return_20d_10_60"],
        ["near_60d_high_10pct"],
        ["near_60d_high_5pct"],
    ]
    combos: list[tuple[str, pd.Series, str]] = []

    for volume in volume_groups:
        for market in market_groups:
            for tdcc in tdcc_groups:
                for technical in technical_groups:
                    for price in price_groups:
                        names = volume + market + tdcc + technical + price
                        if not names:
                            continue
                        if not any(name.startswith("vol") or name.startswith("day_vol") for name in names):
                            # The current project is specifically testing attack volume as the base condition.
                            continue
                        if len(names) > 5:
                            continue
                        families = {parameter_family(name) for name in names}
                        mask = pd.Series(True, index=next(iter(masks.values())).index)
                        for name in names:
                            mask = mask & masks[name]
                        combos.append((" + ".join(names), mask, "+".join(sorted(families))))
    return combos


def summarize_picked(
    df: pd.DataFrame,
    picked: pd.DataFrame,
    rule_name: str,
    rule_family: str,
    window: int,
    total_hits: int,
) -> dict[str, object]:
    hit_col = f"next_open_to_d{window}_high_10pct_hit"
    ret_col = f"next_open_to_d{window}_high_return_pct"
    close_win_col = f"next_open_to_d{window}_close_win"
    close_ret_col = f"next_open_to_d{window}_close_return_pct"
    hits = picked[picked[hit_col]]
    close_wins = picked[picked[close_win_col]] if close_win_col in picked.columns else picked.iloc[0:0]
    sample = "ok_initial_sample" if len(picked) >= MIN_SELECTED else "insufficient_sample"
    return {
        "rule_name": rule_name,
        "rule_family": rule_family,
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
        "win_rate_next_open_to_close_pct": round(len(close_wins) / len(picked) * 100, 2) if len(picked) else 0,
        "avg_next_open_to_close_return_pct": round(picked[close_ret_col].mean(), 2) if len(picked) and close_ret_col in picked.columns else 0,
        "median_next_open_to_close_return_pct": round(picked[close_ret_col].median(), 2) if len(picked) and close_ret_col in picked.columns else 0,
        "avg_signal_close_to_next_open_gap_pct": round(picked["signal_close_to_next_open_gap_pct"].mean(), 2) if len(picked) else 0,
        "tdcc_available_rate_pct": round(picked["tdcc_available"].mean() * 100, 2) if len(picked) else 0,
        "top_market_regime_counts": top_counts(picked, "derived_market_regime"),
        "sample_status": sample,
    }


def summarize(df: pd.DataFrame, rule_name: str, rule_family: str, mask: pd.Series, window: int) -> dict[str, object]:
    hit_col = f"next_open_to_d{window}_high_10pct_hit"
    return summarize_picked(df, df[mask], rule_name, rule_family, window, int(df[hit_col].sum()))


def top_counts(df: pd.DataFrame, col: str, limit: int = 4) -> str:
    if df.empty or col not in df.columns:
        return ""
    counts = df[col].fillna("").astype(str).replace({"": "blank"}).value_counts().head(limit)
    return "; ".join(f"{k}={v}" for k, v in counts.items())


def df_to_md(df: pd.DataFrame, limit: int = 30) -> str:
    if df.empty:
        return "_No rows._"
    return df.head(limit).to_markdown(index=False)


def window_labels() -> list[str]:
    return [f"D+{window}" for window in WINDOWS]


def build_markdown(summary: pd.DataFrame, df: pd.DataFrame) -> str:
    lines: list[str] = []
    lines.append("# Next-Open +10pct Touch Strict Parameter Search")
    lines.append("")
    lines.append(f"- generated_at: `{now_text()}`")
    lines.append("- legacy_file_prefix: `weekly_surge` is kept only for backward compatibility.")
    lines.append("- display_name_zh: `隔日開盤買進後 D+1 至 D+10、D+20 盤中觸及 +10% 研究`.")
    lines.append("- not_weekly_candle: `True`.")
    lines.append("- entry_basis: D+1 open, because the signal is only known after the signal-day close.")
    lines.append("- target: D+1 open to D+1 / ... / D+10 / D+20 max high >= 10%.")
    lines.append("- win_rate_definition: selected stock-days whose post-entry intraperiod high touches +10%; this is not D+N close-to-close win rate.")
    lines.append("- close_exit_definition: D+1 open entry to D+N close exit; close-exit win rate uses return > 0.")
    lines.append("- strictness: no latest theme labels are used. Features are price/volume/technical, TDCC as-of data, and market regime derived from historical index data.")
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
        "coverage_of_all_hits_pct",
        "median_next_open_to_high_return_pct",
        "win_rate_next_open_to_close_pct",
        "avg_next_open_to_close_return_pct",
        "median_next_open_to_close_return_pct",
        "avg_signal_close_to_next_open_gap_pct",
        "tdcc_available_rate_pct",
        "sample_status",
    ]
    for window in window_labels():
        lines.append(f"## Best {window} Rules - Large Enough")
        lines.append("")
        part = summary[(summary["target_window"] == window) & (summary["selected_stock_days"] >= MIN_SELECTED)]
        lines.append(df_to_md(part[keep], limit=30))
        lines.append("")
        lines.append(f"## Best {window} Rules - Small Sample Watch")
        lines.append("")
        small = summary[
            (summary["target_window"] == window)
            & (summary["selected_stock_days"] >= 30)
            & (summary["selected_stock_days"] < MIN_SELECTED)
        ]
        lines.append(df_to_md(small[keep], limit=15))
        lines.append("")
    return "\n".join(lines) + "\n"


def main() -> int:
    df = build_stock_day_frame()
    if df.empty:
        raise RuntimeError("no stock day frame built")
    df = add_technical_features(df)
    df = attach_tdcc_context(df)
    df = attach_market_context(df)
    masks = build_parameter_masks(df)
    rows: list[dict[str, object]] = []
    total_hits_by_window = {
        window: int(df[f"next_open_to_d{window}_high_10pct_hit"].sum())
        for window in WINDOWS
    }
    for rule_name, mask, family in build_combinations(masks):
        selected = int(mask.sum())
        if selected < 30:
            continue
        picked = df[mask]
        for window in WINDOWS:
            rows.append(summarize_picked(df, picked, rule_name, family, window, total_hits_by_window[window]))
    summary = pd.DataFrame(rows)
    if not summary.empty:
        summary = summary.sort_values(
            ["target_window", "sample_status", "hit_rate_pct", "selected_stock_days"],
            ascending=[True, True, False, False],
        ).reset_index(drop=True)
    write_csv(summary, OUT_CSV)
    write_csv(summary, HISTORY_CSV)
    OUT_MD.write_text(build_markdown(summary, df), encoding="utf-8", newline="\n")
    print(f"Saved: {OUT_CSV} rows={len(summary)}")
    print(f"Saved: {OUT_MD}")
    print(f"Saved: {HISTORY_CSV} rows={len(summary)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
