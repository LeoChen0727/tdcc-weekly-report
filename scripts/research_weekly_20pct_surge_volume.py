from __future__ import annotations

from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo

import pandas as pd


PRICE_DIR = Path("data/stock_price_history")
LATEST_DIR = Path("output/latest")
HISTORY_DIR = Path("output/history/research")

EVENTS_CSV = LATEST_DIR / "weekly_20pct_surge_volume_events_latest.csv"
SUMMARY_CSV = LATEST_DIR / "weekly_20pct_surge_volume_hit_rate_latest.csv"
SUMMARY_MD = LATEST_DIR / "weekly_20pct_surge_volume_hit_rate_latest.md"
TARGET_COMPARISON_CSV = LATEST_DIR / "weekly_10pct_vs_20pct_surge_volume_comparison_latest.csv"
TARGET_COMPARISON_MD = LATEST_DIR / "weekly_10pct_vs_20pct_surge_volume_comparison_latest.md"
HISTORY_EVENTS_CSV = HISTORY_DIR / "weekly_20pct_surge_volume_events.csv"

FORWARD_DAYS = 5
SURGE_THRESHOLD_PCT = 20.0
VOL_AVG_DAYS = 20

THRESHOLDS = [0.5, 0.8, 1.0, 1.2, 1.5, 2.0, 3.0, 5.0]
BINS = [0, 0.5, 0.8, 1.0, 1.2, 1.5, 2.0, 3.0, 5.0, float("inf")]
BIN_LABELS = ["<0.5x", "0.5-0.8x", "0.8-1.0x", "1.0-1.2x", "1.2-1.5x", "1.5-2.0x", "2.0-3.0x", "3.0-5.0x", ">=5.0x"]


def now_text() -> str:
    return datetime.now(ZoneInfo("Asia/Taipei")).strftime("%Y-%m-%d %H:%M:%S Asia/Taipei")


def normalize_stock_id(value: object) -> str:
    text = str(value).strip()
    if text.endswith(".0"):
        text = text[:-2]
    return text.zfill(4) if text.isdigit() and len(text) < 4 else text


def read_price(path: Path) -> pd.DataFrame:
    try:
        df = pd.read_csv(path, dtype={"stock_id": str}, keep_default_na=False)
    except Exception:
        return pd.DataFrame()
    required = {"date", "stock_id", "stock_name", "open", "high", "low", "close", "volume"}
    if not required.issubset(df.columns):
        return pd.DataFrame()
    df = df.copy()
    df["stock_id"] = df["stock_id"].map(normalize_stock_id)
    df["date"] = df["date"].astype(str).str.replace(r"\D", "", regex=True).str[:8]
    for col in ["open", "high", "low", "close", "volume"]:
        df[col] = pd.to_numeric(df[col], errors="coerce")
    df = df.dropna(subset=["date", "high", "low", "close", "volume"])
    df = df[(df["date"] != "") & (df["low"] > 0) & (df["high"] > 0) & (df["volume"] > 0)]
    return df.sort_values("date").reset_index(drop=True)


def build_stock_day_frame() -> pd.DataFrame:
    frames: list[pd.DataFrame] = []
    for path in sorted(PRICE_DIR.glob("*.csv")):
        df = read_price(path)
        if len(df) < VOL_AVG_DAYS + FORWARD_DAYS + 1:
            continue
        df["volume_ma20_prev"] = df["volume"].shift(1).rolling(VOL_AVG_DAYS, min_periods=VOL_AVG_DAYS).mean()
        df["start_day_volume_ratio_vs_prev20"] = df["volume"] / df["volume_ma20_prev"]
        df["prev_day_volume_ratio_vs_prev20"] = df["volume"].shift(1) / df["volume"].shift(2).rolling(VOL_AVG_DAYS, min_periods=VOL_AVG_DAYS).mean()

        # Future high over the start day and the next 5 trading days.
        future_high = pd.concat([df["high"].shift(-i) for i in range(FORWARD_DAYS + 1)], axis=1).max(axis=1)
        future_high_offset = pd.concat([df["high"].shift(-i) for i in range(FORWARD_DAYS + 1)], axis=1).idxmax(axis=1)
        # idxmax returns the column label from concat, which is duplicated/opaque. Recompute with numpy-like loop.
        offsets: list[int | None] = []
        highs = df["high"].to_list()
        for idx in range(len(df)):
            window = highs[idx : idx + FORWARD_DAYS + 1]
            if not window:
                offsets.append(None)
                continue
            max_val = max(window)
            offsets.append(window.index(max_val))

        df["future_5d_high"] = future_high
        df["future_5d_high_day_offset"] = offsets
        df["future_5d_high_from_start_low_pct"] = (df["future_5d_high"] / df["low"] - 1.0) * 100.0
        df["weekly_20pct_surge_hit"] = df["future_5d_high_from_start_low_pct"] >= SURGE_THRESHOLD_PCT
        df["weekly_10pct_surge_hit"] = df["future_5d_high_from_start_low_pct"] >= 10.0
        df["signal_day_close_return_pct"] = (df["close"] / df["open"] - 1.0) * 100.0
        df["signal_day_high_from_low_pct"] = (df["high"] / df["low"] - 1.0) * 100.0
        df = df.dropna(subset=["start_day_volume_ratio_vs_prev20", "prev_day_volume_ratio_vs_prev20", "future_5d_high_from_start_low_pct"])
        if not df.empty:
            frames.append(df)
    if not frames:
        return pd.DataFrame()
    return pd.concat(frames, ignore_index=True)


def summarize_thresholds(df: pd.DataFrame, metric: str, label: str) -> pd.DataFrame:
    rows = []
    total_hits = int(df["weekly_20pct_surge_hit"].sum())
    total_days = len(df)
    for threshold in THRESHOLDS:
        picked = df[df[metric] >= threshold]
        hit = picked[picked["weekly_20pct_surge_hit"]]
        rows.append(
            {
                "summary_type": "threshold_ge",
                "filter_metric": label,
                "filter_rule": f"{metric}>={threshold:g}",
                "threshold": threshold,
                "selected_stock_days": len(picked),
                "hit_stock_days": len(hit),
                "hit_rate_pct": round(len(hit) / len(picked) * 100, 2) if len(picked) else 0,
                "selected_unique_stocks": picked["stock_id"].nunique(),
                "hit_unique_stocks": hit["stock_id"].nunique(),
                "coverage_of_all_hits_pct": round(len(hit) / total_hits * 100, 2) if total_hits else 0,
                "base_hit_rate_pct": round(total_hits / total_days * 100, 2) if total_days else 0,
            }
        )
    return pd.DataFrame(rows)


def summarize_thresholds_for_target(df: pd.DataFrame, metric: str, label: str, hit_col: str, target_pct: float) -> pd.DataFrame:
    rows = []
    total_hits = int(df[hit_col].sum())
    total_days = len(df)
    for threshold in THRESHOLDS:
        picked = df[df[metric] >= threshold]
        hit = picked[picked[hit_col]]
        rows.append(
            {
                "target_return_pct": target_pct,
                "filter_metric": label,
                "filter_rule": f"{metric}>={threshold:g}",
                "threshold": threshold,
                "selected_stock_days": len(picked),
                "hit_stock_days": len(hit),
                "hit_rate_pct": round(len(hit) / len(picked) * 100, 2) if len(picked) else 0,
                "selected_unique_stocks": picked["stock_id"].nunique(),
                "hit_unique_stocks": hit["stock_id"].nunique(),
                "coverage_of_all_hits_pct": round(len(hit) / total_hits * 100, 2) if total_hits else 0,
                "base_hit_rate_pct": round(total_hits / total_days * 100, 2) if total_days else 0,
                "total_hit_stock_days": total_hits,
            }
        )
    return pd.DataFrame(rows)


def summarize_bins(df: pd.DataFrame, metric: str, label: str) -> pd.DataFrame:
    temp = df.copy()
    temp["_bin"] = pd.cut(temp[metric], bins=BINS, labels=BIN_LABELS, right=False)
    rows = []
    for bin_label, picked in temp.groupby("_bin", observed=False):
        if picked.empty:
            continue
        hit = picked[picked["weekly_20pct_surge_hit"]]
        rows.append(
            {
                "summary_type": "bin",
                "filter_metric": label,
                "filter_rule": f"{metric} in {bin_label}",
                "threshold": str(bin_label),
                "selected_stock_days": len(picked),
                "hit_stock_days": len(hit),
                "hit_rate_pct": round(len(hit) / len(picked) * 100, 2),
                "selected_unique_stocks": picked["stock_id"].nunique(),
                "hit_unique_stocks": hit["stock_id"].nunique(),
                "coverage_of_all_hits_pct": "",
                "base_hit_rate_pct": "",
            }
        )
    return pd.DataFrame(rows)


def build_markdown(df: pd.DataFrame, summary: pd.DataFrame, events: pd.DataFrame) -> str:
    lines: list[str] = []
    lines.append("# Weekly 20pct Surge Volume Research")
    lines.append("")
    lines.append(f"- generated_at: {now_text()}")
    lines.append(f"- definition: start date is any stock trading day; hit if max high from D0 through D+{FORWARD_DAYS} divided by D0 low is >= {SURGE_THRESHOLD_PCT:.0f}%.")
    lines.append(f"- volume baseline: previous {VOL_AVG_DAYS} completed trading days, excluding the measured day.")
    lines.append("- counting: stock-day level; one stock can appear on multiple start dates.")
    lines.append("")
    lines.append("## Overall")
    lines.append("")
    total = len(df)
    hits = int(df["weekly_20pct_surge_hit"].sum()) if not df.empty else 0
    lines.append(f"- stock_day_count: {total}")
    lines.append(f"- hit_stock_day_count: {hits}")
    lines.append(f"- base_hit_rate: {hits / total * 100:.2f}%" if total else "- base_hit_rate: 0.00%")
    lines.append(f"- hit_unique_stocks: {events['stock_id'].nunique() if not events.empty else 0}")
    lines.append("")

    for metric_label in ["start_day_volume_ratio", "previous_day_volume_ratio"]:
        part = summary[(summary["filter_metric"] == metric_label) & (summary["summary_type"] == "threshold_ge")]
        lines.append(f"## Threshold Hit Rate - {metric_label}")
        lines.append("")
        lines.append(part.to_markdown(index=False))
        lines.append("")

    for metric_label in ["start_day_volume_ratio", "previous_day_volume_ratio"]:
        part = summary[(summary["filter_metric"] == metric_label) & (summary["summary_type"] == "bin")]
        lines.append(f"## Bin Hit Rate - {metric_label}")
        lines.append("")
        lines.append(part.to_markdown(index=False))
        lines.append("")

    top_events = events.sort_values("future_5d_high_from_start_low_pct", ascending=False).head(50)
    keep_cols = [
        "date",
        "stock_id",
        "stock_name",
        "low",
        "future_5d_high",
        "future_5d_high_from_start_low_pct",
        "future_5d_high_day_offset",
        "start_day_volume_ratio_vs_prev20",
        "prev_day_volume_ratio_vs_prev20",
    ]
    lines.append("## Top Hit Events")
    lines.append("")
    lines.append(top_events[keep_cols].to_markdown(index=False) if not top_events.empty else "_No hit events._")
    lines.append("")
    return "\n".join(lines)


def build_target_comparison_markdown(df: pd.DataFrame, comparison: pd.DataFrame) -> str:
    lines: list[str] = []
    lines.append("# Weekly Surge Volume Target Comparison")
    lines.append("")
    lines.append(f"- generated_at: {now_text()}")
    lines.append(f"- definition: start date is any stock trading day; future return uses max high from D0 through D+{FORWARD_DAYS} divided by D0 low.")
    lines.append(f"- volume baseline: previous {VOL_AVG_DAYS} completed trading days, excluding the measured day.")
    lines.append("- purpose: compare the same volume filters under 20% and 10% weekly high-from-low targets.")
    lines.append("- counting: stock-day level; one stock can appear on multiple start dates.")
    lines.append("")
    total = len(df)
    hit_20 = int(df["weekly_20pct_surge_hit"].sum())
    hit_10 = int(df["weekly_10pct_surge_hit"].sum())
    lines.append("## Overall")
    lines.append("")
    lines.append(f"- stock_day_count: {total}")
    lines.append(f"- weekly_20pct_hit_stock_days: {hit_20}")
    lines.append(f"- weekly_20pct_base_hit_rate: {hit_20 / total * 100:.2f}%" if total else "- weekly_20pct_base_hit_rate: 0.00%")
    lines.append(f"- weekly_10pct_hit_stock_days: {hit_10}")
    lines.append(f"- weekly_10pct_base_hit_rate: {hit_10 / total * 100:.2f}%" if total else "- weekly_10pct_base_hit_rate: 0.00%")
    lines.append("")

    keep_cols = [
        "target_return_pct",
        "threshold",
        "selected_stock_days",
        "hit_stock_days",
        "hit_rate_pct",
        "coverage_of_all_hits_pct",
        "base_hit_rate_pct",
    ]
    for metric_label in ["start_day_volume_ratio", "previous_day_volume_ratio"]:
        part = comparison[comparison["filter_metric"] == metric_label]
        lines.append(f"## Target Comparison - {metric_label}")
        lines.append("")
        lines.append(part[keep_cols].to_markdown(index=False))
        lines.append("")
    return "\n".join(lines)


def main() -> int:
    LATEST_DIR.mkdir(parents=True, exist_ok=True)
    HISTORY_DIR.mkdir(parents=True, exist_ok=True)
    df = build_stock_day_frame()
    if df.empty:
        raise RuntimeError("no stock day frame built")

    events = df[df["weekly_20pct_surge_hit"]].copy()
    event_cols = [
        "date",
        "stock_id",
        "stock_name",
        "market",
        "open",
        "high",
        "low",
        "close",
        "volume",
        "volume_ma20_prev",
        "start_day_volume_ratio_vs_prev20",
        "prev_day_volume_ratio_vs_prev20",
        "future_5d_high",
        "future_5d_high_day_offset",
        "future_5d_high_from_start_low_pct",
        "signal_day_close_return_pct",
        "signal_day_high_from_low_pct",
    ]
    events[event_cols].to_csv(EVENTS_CSV, index=False, encoding="utf-8", lineterminator="\n")
    events[event_cols].to_csv(HISTORY_EVENTS_CSV, index=False, encoding="utf-8", lineterminator="\n")

    summary = pd.concat(
        [
            summarize_thresholds(df, "start_day_volume_ratio_vs_prev20", "start_day_volume_ratio"),
            summarize_thresholds(df, "prev_day_volume_ratio_vs_prev20", "previous_day_volume_ratio"),
            summarize_bins(df, "start_day_volume_ratio_vs_prev20", "start_day_volume_ratio"),
            summarize_bins(df, "prev_day_volume_ratio_vs_prev20", "previous_day_volume_ratio"),
        ],
        ignore_index=True,
    )
    summary.to_csv(SUMMARY_CSV, index=False, encoding="utf-8", lineterminator="\n")
    SUMMARY_MD.write_text(build_markdown(df, summary, events[event_cols]), encoding="utf-8")

    target_comparison = pd.concat(
        [
            summarize_thresholds_for_target(df, "start_day_volume_ratio_vs_prev20", "start_day_volume_ratio", "weekly_20pct_surge_hit", 20.0),
            summarize_thresholds_for_target(df, "prev_day_volume_ratio_vs_prev20", "previous_day_volume_ratio", "weekly_20pct_surge_hit", 20.0),
            summarize_thresholds_for_target(df, "start_day_volume_ratio_vs_prev20", "start_day_volume_ratio", "weekly_10pct_surge_hit", 10.0),
            summarize_thresholds_for_target(df, "prev_day_volume_ratio_vs_prev20", "previous_day_volume_ratio", "weekly_10pct_surge_hit", 10.0),
        ],
        ignore_index=True,
    )
    target_comparison.to_csv(TARGET_COMPARISON_CSV, index=False, encoding="utf-8", lineterminator="\n")
    TARGET_COMPARISON_MD.write_text(build_target_comparison_markdown(df, target_comparison), encoding="utf-8")

    print(f"Saved: {EVENTS_CSV} rows={len(events)}")
    print(f"Saved: {SUMMARY_CSV} rows={len(summary)}")
    print(f"Saved: {SUMMARY_MD}")
    print(f"Saved: {TARGET_COMPARISON_CSV} rows={len(target_comparison)}")
    print(f"Saved: {TARGET_COMPARISON_MD}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
