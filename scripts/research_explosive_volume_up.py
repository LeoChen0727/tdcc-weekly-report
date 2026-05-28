from __future__ import annotations

from pathlib import Path
from typing import Any

import pandas as pd

from tracking_utils import (
    DOCS_LATEST_DIR,
    LATEST_DIR,
    STOCK_PRICE_HISTORY_DIR,
    fmt_pct,
    markdown_table,
    normalize_code,
    normalize_date,
    now_text,
    read_csv,
    safe_str,
    to_number,
    write_csv,
)


OUT_EVENTS = LATEST_DIR / "explosive_volume_up_events_latest.csv"
OUT_SUMMARY = LATEST_DIR / "explosive_volume_up_backtest_latest.csv"
OUT_MD = LATEST_DIR / "explosive_volume_up_backtest_latest.md"
HISTORY_EVENTS = Path("output/history/research/explosive_volume_up_events.csv")
HISTORY_SUMMARY = Path("output/history/research/explosive_volume_up_backtest.csv")

DOCS_EVENTS = DOCS_LATEST_DIR / OUT_EVENTS.name
DOCS_SUMMARY = DOCS_LATEST_DIR / OUT_SUMMARY.name
DOCS_MD = DOCS_LATEST_DIR / OUT_MD.name

VOLUME_RATIO_THRESHOLDS = [10, 8, 6, 5, 4, 3, 2]
MIN_SIGNAL_RETURNS = [0, 3, 5, 7]
HORIZONS = list(range(1, 21))
TARGETS = [5, 10, 20]


def load_price(path: Path) -> pd.DataFrame:
    df = read_csv(path, dtype=str)
    if df.empty:
        return df
    if "date" not in df.columns:
        return pd.DataFrame()
    for col in ["open", "high", "low", "close", "volume"]:
        if col not in df.columns:
            return pd.DataFrame()
        df[col] = pd.to_numeric(df[col], errors="coerce")
    df["date"] = df["date"].map(normalize_date)
    if "stock_id" not in df.columns:
        df["stock_id"] = normalize_code(path.stem)
    df["stock_id"] = df["stock_id"].map(normalize_code)
    if "stock_name" not in df.columns:
        df["stock_name"] = ""
    if "market" not in df.columns:
        df["market"] = ""
    df = df.dropna(subset=["open", "high", "low", "close", "volume"])
    df = df[df["date"].astype(str).str.len() == 8]
    return df.sort_values("date").reset_index(drop=True)


def build_stock_events(path: Path) -> pd.DataFrame:
    price = load_price(path)
    if len(price) < 45:
        return pd.DataFrame()

    price["prev_close"] = price["close"].shift(1)
    price["signal_return_1d_pct"] = (price["close"] / price["prev_close"] - 1) * 100
    price["intraday_return_pct"] = (price["close"] / price["open"] - 1) * 100
    price["prev20_volume_avg"] = price["volume"].shift(1).rolling(20, min_periods=10).mean()
    price["prev5_volume_avg"] = price["volume"].shift(1).rolling(5, min_periods=3).mean()
    price["volume_ratio_vs_prev20"] = price["volume"] / price["prev20_volume_avg"]
    price["volume_ratio_vs_prev5"] = price["volume"] / price["prev5_volume_avg"]
    price["prev_day_volume_ratio_vs_prev20"] = price["volume"].shift(1) / price["prev20_volume_avg"]
    price["next_open"] = price["open"].shift(-1)

    for horizon in HORIZONS:
        window_high = price["high"].shift(-1).rolling(horizon, min_periods=horizon).max().shift(-(horizon - 1))
        window_low = price["low"].shift(-1).rolling(horizon, min_periods=horizon).min().shift(-(horizon - 1))
        d_close = price["close"].shift(-horizon)
        price[f"mature_d{horizon}"] = price["next_open"].notna() & d_close.notna()
        price[f"next_open_to_d{horizon}_close_return_pct"] = (d_close / price["next_open"] - 1) * 100
        price[f"next_open_to_d{horizon}_max_high_return_pct"] = (window_high / price["next_open"] - 1) * 100
        price[f"next_open_to_d{horizon}_max_low_return_pct"] = (window_low / price["next_open"] - 1) * 100

    mask = (
        price["volume_ratio_vs_prev20"].ge(min(VOLUME_RATIO_THRESHOLDS))
        & price["signal_return_1d_pct"].ge(min(MIN_SIGNAL_RETURNS))
        & price["next_open"].notna()
    )
    out = price.loc[mask].copy()
    if out.empty:
        return pd.DataFrame()
    keep = [
        "date",
        "stock_id",
        "stock_name",
        "market",
        "open",
        "high",
        "low",
        "close",
        "volume",
        "prev20_volume_avg",
        "prev5_volume_avg",
        "volume_ratio_vs_prev20",
        "volume_ratio_vs_prev5",
        "prev_day_volume_ratio_vs_prev20",
        "signal_return_1d_pct",
        "intraday_return_pct",
        "next_open",
    ]
    for horizon in HORIZONS:
        keep += [
            f"mature_d{horizon}",
            f"next_open_to_d{horizon}_close_return_pct",
            f"next_open_to_d{horizon}_max_high_return_pct",
            f"next_open_to_d{horizon}_max_low_return_pct",
        ]
    return out[keep]


def summarize_rule(events: pd.DataFrame) -> pd.DataFrame:
    rows: list[dict[str, Any]] = []
    if events.empty:
        return pd.DataFrame()
    for volume_threshold in VOLUME_RATIO_THRESHOLDS:
        for min_return in MIN_SIGNAL_RETURNS:
            part = events[
                events["volume_ratio_vs_prev20"].ge(volume_threshold)
                & events["signal_return_1d_pct"].ge(min_return)
            ].copy()
            if part.empty:
                continue
            rule_name = f"volume_ratio_prev20_ge_{volume_threshold}x_signal_return_ge_{min_return}pct"
            unique_stock_days = part[["date", "stock_id"]].drop_duplicates().shape[0]
            unique_stocks = part["stock_id"].nunique()
            for horizon in HORIZONS:
                mature_col = f"mature_d{horizon}"
                close_col = f"next_open_to_d{horizon}_close_return_pct"
                high_col = f"next_open_to_d{horizon}_max_high_return_pct"
                low_col = f"next_open_to_d{horizon}_max_low_return_pct"
                matured = part[part[mature_col].astype(bool)].copy()
                row: dict[str, Any] = {
                    "rule_name": rule_name,
                    "volume_ratio_threshold": volume_threshold,
                    "min_signal_return_pct": min_return,
                    "horizon": f"D+{horizon}",
                    "selected_stock_days": unique_stock_days,
                    "selected_stocks": unique_stocks,
                    "mature_count": len(matured),
                    "sample_status": sample_status(len(matured)),
                }
                if matured.empty:
                    rows.append(row)
                    continue
                close_ret = pd.to_numeric(matured[close_col], errors="coerce")
                high_ret = pd.to_numeric(matured[high_col], errors="coerce")
                low_ret = pd.to_numeric(matured[low_col], errors="coerce")
                row.update(
                    {
                        "close_win_rate_pct": round(close_ret.gt(0).mean() * 100, 2),
                        "avg_close_return_pct": round(close_ret.mean(), 2),
                        "median_close_return_pct": round(close_ret.median(), 2),
                        "avg_mfe_pct": round(high_ret.mean(), 2),
                        "median_mfe_pct": round(high_ret.median(), 2),
                        "avg_mae_pct": round(low_ret.mean(), 2),
                        "median_mae_pct": round(low_ret.median(), 2),
                    }
                )
                for target in TARGETS:
                    row[f"hit_rate_high_ge_{target}pct"] = round(high_ret.ge(target).mean() * 100, 2)
                    row[f"close_hit_rate_ge_{target}pct"] = round(close_ret.ge(target).mean() * 100, 2)
                rows.append(row)
    return pd.DataFrame(rows).sort_values(
        ["volume_ratio_threshold", "min_signal_return_pct", "horizon"],
        ascending=[False, True, True],
    )


def sample_status(mature_count: int) -> str:
    if mature_count >= 100:
        return "ok"
    if mature_count >= 30:
        return "small_sample"
    if mature_count > 0:
        return "insufficient_sample"
    return "pending_or_no_mature"


def fmt_num(value: Any, digits: int = 2) -> str:
    num = to_number(value)
    if pd.isna(num):
        return "-"
    return f"{num:.{digits}f}"


def best_tables(summary: pd.DataFrame) -> tuple[pd.DataFrame, pd.DataFrame]:
    if summary.empty:
        return pd.DataFrame(), pd.DataFrame()
    d10 = summary[summary["horizon"].eq("D+10")].copy()
    d20 = summary[summary["horizon"].eq("D+20")].copy()
    rank_cols = ["hit_rate_high_ge_10pct", "close_win_rate_pct", "mature_count"]
    d10 = d10.sort_values(rank_cols, ascending=[False, False, False]).head(20)
    d20 = d20.sort_values(rank_cols, ascending=[False, False, False]).head(20)
    return d10, d20


def build_markdown(events: pd.DataFrame, summary: pd.DataFrame) -> str:
    lines: list[str] = []
    lines.append("# Explosive Volume Up Backtest")
    lines.append("")
    lines.append(f"- generated_at: `{now_text()}`")
    lines.append("- signal_definition: signal day volume / previous 20 trading day average volume >= threshold, and signal day close-to-close return >= minimum return.")
    lines.append("- entry_basis: next trading day open.")
    lines.append("- close_return: next open to D+N close.")
    lines.append("- high_hit_rate: next open to the highest high within D+N reaches target return.")
    lines.append("- purpose: research only; do not mix into daily candidate core ranking until sample and regime tests mature.")
    lines.append("")
    if events.empty or summary.empty:
        lines.append("_No mature events._")
        return "\n".join(lines) + "\n"

    lines.append("## Data Summary")
    lines.append("")
    lines.append(f"- total_event_rows: `{len(events)}`")
    lines.append(f"- unique_stock_days: `{events[['date', 'stock_id']].drop_duplicates().shape[0]}`")
    lines.append(f"- date_range: `{events['date'].min()}` to `{events['date'].max()}`")
    lines.append("")

    display_cols = [
        "rule_name",
        "horizon",
        "selected_stock_days",
        "mature_count",
        "close_win_rate_pct",
        "avg_close_return_pct",
        "median_close_return_pct",
        "hit_rate_high_ge_10pct",
        "hit_rate_high_ge_20pct",
        "avg_mfe_pct",
        "avg_mae_pct",
        "sample_status",
    ]

    for title, part in [("D+10 Highest +10% Hit Rate", best_tables(summary)[0]), ("D+20 Highest +10% Hit Rate", best_tables(summary)[1])]:
        lines.append(f"## {title}")
        lines.append("")
        lines.append(markdown_table(part, display_cols, limit=20))
        lines.append("")

    lines.append("## Threshold Matrix: D+10")
    lines.append("")
    d10 = summary[summary["horizon"].eq("D+10")].copy()
    lines.append(markdown_table(d10, display_cols, limit=80))
    lines.append("")

    lines.append("## Threshold Matrix: D+20")
    lines.append("")
    d20 = summary[summary["horizon"].eq("D+20")].copy()
    lines.append(markdown_table(d20, display_cols, limit=80))
    lines.append("")

    lines.append("## Interpretation")
    lines.append("")
    lines.append("- If a high volume-ratio threshold has very few mature samples, the hit rate is unstable even if it looks high.")
    lines.append("- If lowering the threshold increases sample size but hit rate falls toward 50%, volume alone is not discriminative enough.")
    lines.append("- This module should next be segmented by theme/mainstream status, TDCC phase, market regime, and technical position.")
    lines.append("")
    return "\n".join(lines) + "\n"


def compact_events(events: pd.DataFrame) -> pd.DataFrame:
    if events.empty:
        return events
    keep = [
        "date",
        "stock_id",
        "stock_name",
        "market",
        "open",
        "high",
        "low",
        "close",
        "volume",
        "prev20_volume_avg",
        "volume_ratio_vs_prev20",
        "volume_ratio_vs_prev5",
        "prev_day_volume_ratio_vs_prev20",
        "signal_return_1d_pct",
        "intraday_return_pct",
        "next_open",
    ]
    for horizon in [1, 5, 10, 20]:
        keep += [
            f"mature_d{horizon}",
            f"next_open_to_d{horizon}_close_return_pct",
            f"next_open_to_d{horizon}_max_high_return_pct",
            f"next_open_to_d{horizon}_max_low_return_pct",
        ]
    existing = [col for col in keep if col in events.columns]
    out = events[existing].copy()
    return out.sort_values(["date", "volume_ratio_vs_prev20"], ascending=[False, False]).reset_index(drop=True)


def mirror_to_docs(paths: list[Path]) -> None:
    for path in paths:
        target = DOCS_LATEST_DIR / path.name
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(path.read_bytes())


def main() -> int:
    rows: list[pd.DataFrame] = []
    for path in sorted(STOCK_PRICE_HISTORY_DIR.glob("*.csv")):
        events = build_stock_events(path)
        if not events.empty:
            rows.append(events)

    all_events = pd.concat(rows, ignore_index=True) if rows else pd.DataFrame()
    summary = summarize_rule(all_events)
    event_output = compact_events(all_events)

    write_csv(event_output, OUT_EVENTS)
    write_csv(summary, OUT_SUMMARY)
    write_csv(event_output, HISTORY_EVENTS)
    write_csv(summary, HISTORY_SUMMARY)
    OUT_MD.write_text(build_markdown(event_output, summary), encoding="utf-8", newline="\n")
    mirror_to_docs([OUT_EVENTS, OUT_SUMMARY, OUT_MD])

    print(f"Saved: {OUT_EVENTS} rows={len(event_output)}")
    print(f"Saved: {OUT_SUMMARY} rows={len(summary)}")
    print(f"Saved: {OUT_MD}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
