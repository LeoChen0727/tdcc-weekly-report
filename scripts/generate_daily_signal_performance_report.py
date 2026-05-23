from __future__ import annotations

from datetime import datetime, timedelta
import math
import sys
from pathlib import Path
from typing import Any

import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent))

from tracking_utils import (  # noqa: E402
    DAILY_SIGNALS_DIR,
    HORIZONS,
    LATEST_DIR,
    fmt_pct,
    load_market_index_history,
    markdown_table,
    now_text,
    safe_str,
    to_number,
    write_csv,
)


PERFORMANCE_CSV = DAILY_SIGNALS_DIR / "daily_candidate_signal_performance.csv"
SUMMARY_CSV = LATEST_DIR / "daily_signal_performance_summary_latest.csv"
SUMMARY_MD = LATEST_DIR / "daily_signal_performance_summary_latest.md"
WEEKLY_MD = LATEST_DIR / "daily_signal_performance_weekly_latest.md"
WEEKLY_PDF = LATEST_DIR / "daily_signal_performance_weekly_latest.pdf"
MONTHLY_MD = LATEST_DIR / "daily_signal_performance_monthly_latest.md"
MONTHLY_PDF = LATEST_DIR / "daily_signal_performance_monthly_latest.pdf"


def num_series(df: pd.DataFrame, col: str) -> pd.Series:
    if col not in df.columns:
        return pd.Series(dtype=float)
    return pd.to_numeric(df[col], errors="coerce")


def win_rate(series: pd.Series) -> float:
    clean = pd.to_numeric(series, errors="coerce").dropna()
    if clean.empty:
        return math.nan
    return float((clean > 0).mean() * 100)


def hit_rate(series: pd.Series, threshold: float) -> float:
    clean = pd.to_numeric(series, errors="coerce").dropna()
    if clean.empty:
        return math.nan
    return float((clean >= threshold).mean() * 100)


def outperformance_rate(series: pd.Series) -> float:
    return win_rate(series)


def stats_by(df: pd.DataFrame, group_cols: list[str], label: str) -> pd.DataFrame:
    if df.empty or any(col not in df.columns for col in group_cols):
        return pd.DataFrame()
    rows: list[dict[str, Any]] = []
    for keys, group in df.groupby(group_cols, dropna=False):
        if not isinstance(keys, tuple):
            keys = (keys,)
        row = {"dimension": label, "signal_count": len(group)}
        for col, key in zip(group_cols, keys):
            row[col] = key
        for h in HORIZONS:
            ret = num_series(group, f"return_d{h}")
            rel = num_series(group, f"relative_return_vs_benchmark_d{h}")
            mfe = num_series(group, f"mfe_d{h}")
            mae = num_series(group, f"mae_d{h}")
            row[f"avg_return_d{h}"] = ret.mean()
            row[f"win_rate_d{h}"] = win_rate(ret)
            row[f"avg_relative_return_vs_benchmark_d{h}"] = rel.mean()
            row[f"benchmark_outperform_rate_d{h}"] = outperformance_rate(rel)
            row[f"avg_mfe_d{h}"] = mfe.mean()
            row[f"avg_mae_d{h}"] = mae.mean()
        row["hit_5pct_rate_d10"] = hit_rate(num_series(group, "mfe_d10"), 5)
        rows.append(row)
    out = pd.DataFrame(rows)
    if "avg_relative_return_vs_benchmark_d10" in out.columns:
        out = out.sort_values(["dimension", "avg_relative_return_vs_benchmark_d10"], ascending=[True, False])
    return out.reset_index(drop=True)


def build_summary(perf: pd.DataFrame) -> pd.DataFrame:
    frames = [
        stats_by(perf, ["category"], "category"),
        stats_by(perf, ["tdcc_status"], "tdcc_status"),
        stats_by(perf, ["warrant_status"], "warrant_status"),
        stats_by(perf, ["sector", "sub_theme"], "theme"),
        stats_by(perf, ["revenue_signal_type"], "revenue_signal_type"),
        stats_by(perf, ["market_regime"], "market_regime"),
        stats_by(perf, ["category", "market_regime"], "category_by_market_regime"),
    ]
    frames = [df for df in frames if not df.empty]
    return pd.concat(frames, ignore_index=True, sort=False) if frames else pd.DataFrame()


def latest_market_summary() -> str:
    idx = load_market_index_history(update_if_missing=False)
    if idx.empty:
        return "目前沒有大盤/櫃買 benchmark 歷史資料。"
    rows = []
    for code in ["TWSE", "TPEX"]:
        part = idx[idx["index_code"] == code].sort_values("date")
        if part.empty:
            continue
        row = part.iloc[-1]
        rows.append(
            f"- {code}: close={row.get('close', '')}, 5d={fmt_pct(row.get('return_5d'))}, "
            f"10d={fmt_pct(row.get('return_10d'))}, 20d={fmt_pct(row.get('return_20d'))}, "
            f"above_ma20={row.get('above_ma20', '')}, above_ma60={row.get('above_ma60', '')}"
        )
    return "\n".join(rows) if rows else "目前沒有可用 benchmark 資料。"


def format_stats_table(summary: pd.DataFrame, dimension: str, columns: list[str], limit: int = 30) -> str:
    table = summary[summary["dimension"] == dimension].copy() if not summary.empty and "dimension" in summary.columns else pd.DataFrame()
    if table.empty:
        return "目前沒有可用統計。"
    return markdown_table(table, columns, limit=limit)


def build_md(title: str, perf: pd.DataFrame, summary: pd.DataFrame, period_note: str) -> str:
    latest_dates = sorted([safe_str(x) for x in perf.get("signal_date", pd.Series(dtype=str)).dropna().unique() if safe_str(x)])
    latest_date = latest_dates[-1] if latest_dates else ""
    lines = [
        f"# {title}",
        "",
        f"- generated_at: `{now_text()}`",
        f"- latest_signal_date: `{latest_date}`",
        f"- signal_count: `{len(perf)}`",
        f"- period: {period_note}",
        "",
        "## 市場背景摘要",
        "",
        latest_market_summary(),
        "",
        "## 絕對報酬 vs 相對報酬：分類",
        "",
        format_stats_table(
            summary,
            "category",
            [
                "category",
                "signal_count",
                "avg_return_d5",
                "avg_return_d10",
                "avg_relative_return_vs_benchmark_d5",
                "avg_relative_return_vs_benchmark_d10",
                "win_rate_d10",
                "benchmark_outperform_rate_d10",
                "avg_mfe_d10",
                "avg_mae_d10",
            ],
        ),
        "",
        "## TDCC 分層效果",
        "",
        format_stats_table(
            summary,
            "tdcc_status",
            ["tdcc_status", "signal_count", "avg_return_d5", "avg_return_d10", "avg_relative_return_vs_benchmark_d10", "win_rate_d10", "avg_mfe_d10", "avg_mae_d10"],
        ),
        "",
        "## 權證分層效果",
        "",
        format_stats_table(
            summary,
            "warrant_status",
            ["warrant_status", "signal_count", "avg_return_d5", "avg_return_d10", "avg_relative_return_vs_benchmark_d10", "win_rate_d10"],
        ),
        "",
        "## 族群表現",
        "",
        format_stats_table(
            summary,
            "theme",
            ["sector", "sub_theme", "signal_count", "avg_return_d5", "avg_return_d10", "avg_relative_return_vs_benchmark_d10", "win_rate_d10"],
            limit=50,
        ),
        "",
        "## 營收類型比較",
        "",
        format_stats_table(
            summary,
            "revenue_signal_type",
            ["revenue_signal_type", "signal_count", "avg_return_d10", "avg_relative_return_vs_benchmark_d10", "win_rate_d10", "benchmark_outperform_rate_d10"],
        ),
        "",
        "## 不同市場背景下的分類表現",
        "",
        format_stats_table(
            summary,
            "category_by_market_regime",
            ["category", "market_regime", "signal_count", "avg_return_d10", "avg_relative_return_vs_benchmark_d10", "benchmark_outperform_rate_d10"],
            limit=80,
        ),
        "",
        "## 判讀規則",
        "",
        "- 不只看個股絕對報酬，必須同時看是否跑贏 benchmark。",
        "- 大盤大漲時，個股小漲但落後 benchmark，應視為相對弱勢。",
        "- 大盤下跌時，個股小跌但明顯跑贏 benchmark，可標示為相對抗跌。",
        "- MFE 高但收盤報酬低，代表訊號可能有效但需要後續出場規則。",
        "- 最新未成熟批次不視為正面或負面，等 D+N 交易日成熟後再納入判斷。",
        "",
    ]
    return "\n".join(lines)


def write_pdf_from_markdown(md_path: Path, pdf_path: Path) -> None:
    try:
        from reportlab.lib.pagesizes import A4
        from reportlab.pdfbase import pdfmetrics
        from reportlab.pdfbase.cidfonts import UnicodeCIDFont
        from reportlab.pdfgen import canvas
    except Exception as exc:
        print(f"WARNING: reportlab unavailable, skip PDF {pdf_path}: {exc}")
        return

    pdf_path.parent.mkdir(parents=True, exist_ok=True)
    pdfmetrics.registerFont(UnicodeCIDFont("STSong-Light"))
    c = canvas.Canvas(str(pdf_path), pagesize=A4)
    width, height = A4
    x = 42
    y = height - 42
    font = "STSong-Light"
    c.setFont(font, 11)

    for raw_line in md_path.read_text(encoding="utf-8", errors="replace").splitlines():
        line = raw_line.replace("`", "")
        if line.startswith("# "):
            c.setFont(font, 18)
            step = 25
            text = line[2:]
        elif line.startswith("## "):
            c.setFont(font, 14)
            step = 21
            text = line[3:]
        else:
            c.setFont(font, 9)
            step = 14
            text = line

        chunks = [text[i : i + 90] for i in range(0, len(text), 90)] or [""]
        for chunk in chunks:
            if y < 48:
                c.showPage()
                c.setFont(font, 9)
                y = height - 42
            c.drawString(x, y, chunk)
            y -= step
            step = 14
    c.save()


def subset_by_days(perf: pd.DataFrame, days: int) -> pd.DataFrame:
    if perf.empty or "signal_date" not in perf.columns:
        return perf
    dates = pd.to_datetime(perf["signal_date"], format="%Y%m%d", errors="coerce")
    if dates.dropna().empty:
        return perf
    cutoff = dates.max() - timedelta(days=days)
    return perf[dates >= cutoff].copy()


def subset_month(perf: pd.DataFrame) -> pd.DataFrame:
    if perf.empty or "signal_date" not in perf.columns:
        return perf
    dates = pd.to_datetime(perf["signal_date"], format="%Y%m%d", errors="coerce")
    if dates.dropna().empty:
        return perf
    latest = dates.max()
    return perf[(dates.dt.year == latest.year) & (dates.dt.month == latest.month)].copy()


def main() -> int:
    if not PERFORMANCE_CSV.exists():
        raise FileNotFoundError(f"Missing {PERFORMANCE_CSV}")
    perf = pd.read_csv(PERFORMANCE_CSV, dtype=str, keep_default_na=False)
    if perf.empty:
        raise RuntimeError("daily_candidate_signal_performance.csv is empty")

    summary = build_summary(perf)
    write_csv(summary, SUMMARY_CSV)

    SUMMARY_MD.write_text(build_md("每日候選股訊號績效摘要", perf, summary, "all available signals"), encoding="utf-8")

    weekly_perf = subset_by_days(perf, 14)
    weekly_summary = build_summary(weekly_perf)
    WEEKLY_MD.write_text(build_md("每日候選股訊號績效週報", weekly_perf, weekly_summary, "latest 14 calendar days"), encoding="utf-8")
    write_pdf_from_markdown(WEEKLY_MD, WEEKLY_PDF)

    monthly_perf = subset_month(perf)
    monthly_summary = build_summary(monthly_perf)
    MONTHLY_MD.write_text(build_md("每日候選股模型績效月報", monthly_perf, monthly_summary, "latest signal month"), encoding="utf-8")
    write_pdf_from_markdown(MONTHLY_MD, MONTHLY_PDF)

    print(f"Saved: {SUMMARY_CSV}")
    print(f"Saved: {SUMMARY_MD}")
    print(f"Saved: {WEEKLY_MD}")
    print(f"Saved: {WEEKLY_PDF}")
    print(f"Saved: {MONTHLY_MD}")
    print(f"Saved: {MONTHLY_PDF}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
