from __future__ import annotations

from pathlib import Path
from typing import Any
import json
import math
import shutil

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd

from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import cm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.cidfonts import UnicodeCIDFont
from reportlab.platypus import Image, PageBreak, Paragraph, SimpleDocTemplate, Spacer, Table, TableStyle

from tracking_utils import (
    DOCS_LATEST_DIR,
    LATEST_DIR,
    classify_market_regime,
    fmt_pct,
    load_market_index_history,
    now_text,
    read_csv,
    safe_str,
    to_number,
    write_csv,
)


INDICATORS_CSV = LATEST_DIR / "futures_options_indicators_latest.csv"
SOURCE_STATUS_JSON = LATEST_DIR / "futures_options_source_status_latest.json"
FUTURES_CONTRACTS_HISTORY = Path("data/futures_options/taifex_futures_contracts_history.csv")
PUT_CALL_RATIO_HISTORY = Path("data/futures_options/put_call_ratio_history.csv")
TAIWAN_VIX_HISTORY = Path("data/futures_options/taiwan_vix_history.csv")
MARKET_REGIME_CSV = LATEST_DIR / "market_regime_latest.csv"
REPORT_MD = LATEST_DIR / "market_risk_dashboard_latest.md"
REPORT_PDF = LATEST_DIR / "market_risk_dashboard_latest.pdf"
DOCS_REPORT_PDF = DOCS_LATEST_DIR / REPORT_PDF.name
MANIFEST_JSON = LATEST_DIR / "market_risk_dashboard_manifest_latest.json"
CHART_DIR = LATEST_DIR / "charts/market_regime"
MARKET_INDEX_CHART = CHART_DIR / "market_index_technical_6m.png"
RISK_INDICATOR_CHART = CHART_DIR / "risk_indicators_6m.png"
FOREIGN_FUTURES_CHART = CHART_DIR / "foreign_futures_net_oi_6m.png"
RETAIL_MTX_PROXY_CHART = CHART_DIR / "retail_mtx_proxy_6m.png"


def latest_index_rows() -> pd.DataFrame:
    df = load_market_index_history(update_if_missing=True)
    if df.empty:
        return pd.DataFrame()
    return df.sort_values(["index_code", "date"]).groupby("index_code", as_index=False).tail(1)


def row_for_index(rows: pd.DataFrame, code: str) -> pd.Series | None:
    part = rows[rows["index_code"].astype(str) == code]
    if part.empty:
        return None
    return part.iloc[-1]


def clean_num(value: Any, digits: int = 0) -> str:
    num = to_number(value)
    if math.isnan(num):
        return "-"
    if digits == 0:
        return f"{num:,.0f}"
    return f"{num:,.{digits}f}"


def clean_signed(value: Any, digits: int = 0) -> str:
    num = to_number(value)
    if math.isnan(num):
        return "-"
    if digits == 0:
        return f"{num:+,.0f}"
    return f"{num:+,.{digits}f}"


def classify_vix(vix: float) -> str:
    if math.isnan(vix):
        return "unknown"
    if vix >= 35:
        return "panic_high"
    if vix >= 28:
        return "risk_elevated"
    if vix >= 22:
        return "watch"
    return "calm"


def classify_pc_ratio(pc_oi: float) -> str:
    if math.isnan(pc_oi):
        return "unknown"
    if pc_oi >= 180:
        return "heavy_put_hedge"
    if pc_oi >= 145:
        return "put_hedge_elevated"
    if pc_oi <= 85:
        return "call_crowded_or_low_hedge"
    return "neutral"


def classify_foreign_futures(net_oi: float) -> str:
    if math.isnan(net_oi):
        return "unknown"
    if net_oi >= 20000:
        return "foreign_net_long"
    if net_oi <= -40000:
        return "foreign_heavy_net_short"
    if net_oi <= -15000:
        return "foreign_net_short"
    return "neutral"


def classify_retail_mtx_proxy(net_oi: float) -> str:
    if math.isnan(net_oi):
        return "unknown"
    if net_oi >= 20000:
        return "retail_net_long_crowded"
    if net_oi >= 10000:
        return "retail_net_long_watch"
    if net_oi <= -20000:
        return "retail_net_short_extreme"
    if net_oi <= -10000:
        return "retail_net_short_watch"
    return "neutral"


def risk_score(index_rows: pd.DataFrame, indicators: pd.Series) -> tuple[int, str, list[str]]:
    score = 0
    reasons: list[str] = []

    for code, label in [("TWSE", "TWSE"), ("TPEX", "TPEx")]:
        row = row_for_index(index_rows, code)
        regime = classify_market_regime(row)
        if regime == "high_risk":
            score += 3
            reasons.append(f"{label} below MA60 and 20d return negative")
        elif regime == "correction":
            score += 2
            reasons.append(f"{label} correction")
        elif regime == "range_bound":
            score += 1
            reasons.append(f"{label} range bound")
        elif regime == "strong_bull":
            score -= 1
            reasons.append(f"{label} strong bull")

    vix = to_number(indicators.get("taiwan_vix", ""))
    if not math.isnan(vix):
        if vix >= 35:
            score += 3
            reasons.append("Taiwan VIX panic-high")
        elif vix >= 28:
            score += 2
            reasons.append("Taiwan VIX elevated")
        elif vix <= 18:
            score -= 1
            reasons.append("Taiwan VIX calm")

    pc_oi = to_number(indicators.get("put_call_oi_ratio_pct", ""))
    if not math.isnan(pc_oi):
        if pc_oi >= 180:
            score += 2
            reasons.append("TXO put/call OI hedge high")
        elif pc_oi >= 145:
            score += 1
            reasons.append("TXO put/call OI hedge elevated")

    foreign_net = to_number(indicators.get("foreign_tx_futures_net_oi", ""))
    if not math.isnan(foreign_net):
        if foreign_net <= -40000:
            score += 2
            reasons.append("Foreign TX futures heavy net short")
        elif foreign_net <= -15000:
            score += 1
            reasons.append("Foreign TX futures net short")
        elif foreign_net >= 20000:
            score -= 1
            reasons.append("Foreign TX futures net long")

    retail_mtx = to_number(indicators.get("retail_mtx_net_oi_proxy", ""))
    if not math.isnan(retail_mtx):
        if retail_mtx >= 20000:
            score += 2
            reasons.append("Retail MTX proxy net long crowded")
        elif retail_mtx >= 10000:
            score += 1
            reasons.append("Retail MTX proxy net long watch")
        elif retail_mtx <= -20000:
            score -= 1
            reasons.append("Retail MTX proxy net short extreme")

    if score >= 6:
        return score, "very_high_risk", reasons
    if score >= 4:
        return score, "high_risk", reasons
    if score >= 2:
        return score, "elevated_risk", reasons
    if score <= -1:
        return score, "risk_on", reasons
    return score, "neutral", reasons


def combined_market_regime(index_rows: pd.DataFrame) -> str:
    twse = classify_market_regime(row_for_index(index_rows, "TWSE"))
    tpex = classify_market_regime(row_for_index(index_rows, "TPEX"))
    if "high_risk" in {twse, tpex}:
        return "high_risk"
    if "correction" in {twse, tpex}:
        return "correction"
    if twse == "strong_bull" and tpex == "strong_bull":
        return "strong_bull"
    if twse in {"strong_bull", "mild_bull"} and tpex in {"strong_bull", "mild_bull"}:
        return "mild_bull"
    return "range_bound"


def build_regime_row(index_rows: pd.DataFrame, indicators: pd.Series) -> pd.DataFrame:
    twse = row_for_index(index_rows, "TWSE")
    tpex = row_for_index(index_rows, "TPEX")
    score, risk_level, reasons = risk_score(index_rows, indicators)
    date_candidates = [
        safe_str(twse.get("date", "")) if twse is not None else "",
        safe_str(tpex.get("date", "")) if tpex is not None else "",
        safe_str(indicators.get("date", "")),
    ]
    date = max([d for d in date_candidates if d] or [""])
    row = {
        "date": date,
        "generated_at": now_text(),
        "market_regime": combined_market_regime(index_rows),
        "risk_level": risk_level,
        "risk_score": score,
        "risk_reasons": "; ".join(reasons),
        "twse_close": twse.get("close", "") if twse is not None else "",
        "twse_return_5d": twse.get("return_5d", "") if twse is not None else "",
        "twse_return_20d": twse.get("return_20d", "") if twse is not None else "",
        "twse_above_ma20": twse.get("above_ma20", "") if twse is not None else "",
        "twse_above_ma60": twse.get("above_ma60", "") if twse is not None else "",
        "tpex_close": tpex.get("close", "") if tpex is not None else "",
        "tpex_return_5d": tpex.get("return_5d", "") if tpex is not None else "",
        "tpex_return_20d": tpex.get("return_20d", "") if tpex is not None else "",
        "tpex_above_ma20": tpex.get("above_ma20", "") if tpex is not None else "",
        "tpex_above_ma60": tpex.get("above_ma60", "") if tpex is not None else "",
        "taiwan_vix": indicators.get("taiwan_vix", ""),
        "vix_state": classify_vix(to_number(indicators.get("taiwan_vix", ""))),
        "put_call_oi_ratio_pct": indicators.get("put_call_oi_ratio_pct", ""),
        "put_call_state": classify_pc_ratio(to_number(indicators.get("put_call_oi_ratio_pct", ""))),
        "foreign_tx_futures_net_oi": indicators.get("foreign_tx_futures_net_oi", ""),
        "foreign_futures_state": classify_foreign_futures(to_number(indicators.get("foreign_tx_futures_net_oi", ""))),
        "retail_mtx_net_oi_proxy": indicators.get("retail_mtx_net_oi_proxy", ""),
        "retail_mtx_state": classify_retail_mtx_proxy(to_number(indicators.get("retail_mtx_net_oi_proxy", ""))),
        "retail_mtx_proxy_method": indicators.get("retail_mtx_proxy_method", ""),
        "source_status": indicators.get("source_status", "missing"),
    }
    return pd.DataFrame([row])


def parse_yyyymmdd(series: pd.Series) -> pd.Series:
    return pd.to_datetime(series.astype(str).str.replace(r"[^0-9]", "", regex=True), format="%Y%m%d", errors="coerce")


def last_six_months(df: pd.DataFrame, date_col: str = "date") -> pd.DataFrame:
    if df.empty or date_col not in df.columns:
        return pd.DataFrame()
    out = df.copy()
    out["_dt"] = parse_yyyymmdd(out[date_col])
    out = out.dropna(subset=["_dt"]).sort_values("_dt")
    if out.empty:
        return pd.DataFrame()
    cutoff = out["_dt"].max() - pd.DateOffset(months=6)
    six_month = out[out["_dt"] >= cutoff].copy()
    if six_month.empty:
        six_month = out.tail(126).copy()
    return six_month


def to_numeric_col(df: pd.DataFrame, col: str) -> pd.Series:
    if col not in df.columns:
        return pd.Series([math.nan] * len(df), index=df.index)
    return pd.to_numeric(df[col].astype(str).str.replace(",", "", regex=False), errors="coerce")


def placeholder_chart(path: Path, title: str, message: str) -> Path:
    path.parent.mkdir(parents=True, exist_ok=True)
    fig, ax = plt.subplots(figsize=(10, 4.8))
    ax.axis("off")
    ax.text(0.5, 0.62, title, ha="center", va="center", fontsize=16, fontweight="bold", transform=ax.transAxes)
    ax.text(0.5, 0.43, message, ha="center", va="center", fontsize=11, color="#555555", transform=ax.transAxes)
    fig.savefig(path, dpi=150, bbox_inches="tight")
    plt.close(fig)
    return path


def make_market_index_chart(index_history: pd.DataFrame, path: Path) -> Path:
    data = last_six_months(index_history, "date")
    if data.empty:
        return placeholder_chart(path, "Six-Month Market Index Technical Chart", "No market index history available.")

    path.parent.mkdir(parents=True, exist_ok=True)
    fig, axes = plt.subplots(2, 1, figsize=(11, 7.2), sharex=True)
    for ax, code, label in [(axes[0], "TWSE", "TWSE / TAIEX"), (axes[1], "TPEX", "TPEx / OTC")]:
        part = data[data["index_code"].astype(str) == code].copy()
        if part.empty:
            ax.text(0.5, 0.5, f"{label}: no data", ha="center", va="center", transform=ax.transAxes)
            ax.set_axis_off()
            continue
        for col in ["close", "ma20", "ma60"]:
            part[col] = to_numeric_col(part, col)
        ax.plot(part["_dt"], part["close"], color="#1f77b4", linewidth=1.7, label="Close")
        ax.plot(part["_dt"], part["ma20"], color="#ff7f0e", linewidth=1.1, label="MA20")
        ax.plot(part["_dt"], part["ma60"], color="#2ca02c", linewidth=1.1, label="MA60")
        high_60 = part["close"].tail(min(60, len(part))).max()
        low_60 = part["close"].tail(min(60, len(part))).min()
        if not math.isnan(high_60):
            ax.axhline(high_60, color="#d62728", linestyle="--", linewidth=0.8, alpha=0.7, label="60D high")
        if not math.isnan(low_60):
            ax.axhline(low_60, color="#9467bd", linestyle=":", linewidth=0.8, alpha=0.7, label="60D low")
        latest = part.iloc[-1]
        regime = classify_market_regime(latest)
        ax.set_title(f"{label} technical trend - {regime}", fontsize=11, fontweight="bold")
        ax.grid(True, alpha=0.25)
        ax.legend(loc="upper left", fontsize=8, ncol=4)
    fig.suptitle("Six-Month Market Index Technical View", fontsize=14, fontweight="bold")
    fig.autofmt_xdate()
    fig.tight_layout(rect=[0, 0, 1, 0.96])
    fig.savefig(path, dpi=150, bbox_inches="tight")
    plt.close(fig)
    return path


def make_risk_indicator_chart(path: Path) -> Path:
    pc = read_csv(PUT_CALL_RATIO_HISTORY, dtype=str)
    vix = read_csv(TAIWAN_VIX_HISTORY, dtype=str)
    pc = last_six_months(pc.rename(columns={"日期": "date"}), "date") if not pc.empty else pd.DataFrame()
    vix = last_six_months(vix, "date") if not vix.empty else pd.DataFrame()
    if pc.empty and vix.empty:
        return placeholder_chart(path, "Six-Month Risk Indicator Chart", "No Put/Call or Taiwan VIX history available.")

    path.parent.mkdir(parents=True, exist_ok=True)
    fig, axes = plt.subplots(2, 1, figsize=(11, 7.0), sharex=False)
    if not vix.empty:
        vix["taiwan_vix"] = to_numeric_col(vix, "taiwan_vix")
        axes[0].plot(vix["_dt"], vix["taiwan_vix"], color="#d62728", linewidth=1.6, label="Taiwan VIX")
        axes[0].axhline(28, color="#ff7f0e", linestyle="--", linewidth=0.9, label="watch 28")
        axes[0].axhline(35, color="#d62728", linestyle=":", linewidth=0.9, label="panic 35")
        axes[0].set_title(f"Taiwan VIX ({len(vix)} observations)", fontsize=11, fontweight="bold")
        axes[0].legend(loc="upper left", fontsize=8)
        axes[0].grid(True, alpha=0.25)
    else:
        axes[0].text(0.5, 0.5, "Taiwan VIX: no data", ha="center", va="center", transform=axes[0].transAxes)
        axes[0].set_axis_off()

    if not pc.empty:
        col = "買賣權未平倉量比率%"
        pc[col] = to_numeric_col(pc, col)
        axes[1].plot(pc["_dt"], pc[col], color="#1f77b4", linewidth=1.6, label="TXO P/C OI ratio")
        axes[1].axhline(145, color="#ff7f0e", linestyle="--", linewidth=0.9, label="hedge elevated 145")
        axes[1].axhline(180, color="#d62728", linestyle=":", linewidth=0.9, label="heavy hedge 180")
        axes[1].set_title(f"TXO Put/Call Open Interest Ratio ({len(pc)} observations)", fontsize=11, fontweight="bold")
        axes[1].legend(loc="upper left", fontsize=8)
        axes[1].grid(True, alpha=0.25)
    else:
        axes[1].text(0.5, 0.5, "Put/Call ratio: no data", ha="center", va="center", transform=axes[1].transAxes)
        axes[1].set_axis_off()
    fig.suptitle("Six-Month Options / Fear Indicators", fontsize=14, fontweight="bold")
    fig.autofmt_xdate()
    fig.tight_layout(rect=[0, 0, 1, 0.96])
    fig.savefig(path, dpi=150, bbox_inches="tight")
    plt.close(fig)
    return path


def make_foreign_futures_chart(path: Path) -> Path:
    futures = read_csv(FUTURES_CONTRACTS_HISTORY, dtype=str)
    if futures.empty:
        return placeholder_chart(path, "Six-Month Foreign Futures Positioning", "No futures contract history available.")
    required = {"日期", "商品名稱", "身份別", "多空未平倉口數淨額"}
    if not required.issubset(set(futures.columns)):
        return placeholder_chart(path, "Six-Month Foreign Futures Positioning", "Futures contract history columns are incomplete.")
    futures = futures[
        futures["商品名稱"].astype(str).str.contains("臺股期貨|台股期貨", regex=True, na=False)
        & futures["身份別"].astype(str).str.contains("外資", na=False)
    ].copy()
    if futures.empty:
        return placeholder_chart(path, "Six-Month Foreign Futures Positioning", "No foreign TX futures rows available.")
    futures["net_oi"] = to_numeric_col(futures, "多空未平倉口數淨額")
    futures = futures.groupby("日期", as_index=False)["net_oi"].sum().rename(columns={"日期": "date"})
    futures = last_six_months(futures, "date")

    path.parent.mkdir(parents=True, exist_ok=True)
    if len(futures) < 2:
        msg = f"Only {len(futures)} usable observation. Workflow will extend this chart as daily data accumulates."
        return placeholder_chart(path, "Six-Month Foreign TX Futures Net OI", msg)

    fig, ax = plt.subplots(figsize=(11, 4.8))
    colors_bar = ["#d62728" if x < 0 else "#2ca02c" for x in futures["net_oi"]]
    ax.bar(futures["_dt"], futures["net_oi"], color=colors_bar, alpha=0.75, width=1.8)
    ax.axhline(0, color="#333333", linewidth=0.8)
    ax.axhline(-40000, color="#d62728", linestyle="--", linewidth=0.9, label="heavy net short")
    ax.axhline(20000, color="#2ca02c", linestyle="--", linewidth=0.9, label="net long watch")
    ax.set_title("Six-Month Foreign TX Futures Net Open Interest", fontsize=13, fontweight="bold")
    ax.grid(True, axis="y", alpha=0.25)
    ax.legend(loc="upper left", fontsize=8)
    fig.autofmt_xdate()
    fig.tight_layout()
    fig.savefig(path, dpi=150, bbox_inches="tight")
    plt.close(fig)
    return path


def retail_mtx_proxy_history() -> pd.DataFrame:
    futures = read_csv(FUTURES_CONTRACTS_HISTORY, dtype=str)
    required = {"日期", "商品名稱", "身份別", "多空未平倉口數淨額"}
    if futures.empty or not required.issubset(set(futures.columns)):
        return pd.DataFrame()
    work = futures[
        futures["商品名稱"].astype(str).str.contains("小型臺指期貨", na=False)
        & futures["身份別"].astype(str).str.contains("自營商|投信|外資", regex=True, na=False)
    ].copy()
    if work.empty:
        return pd.DataFrame()
    work["institution_net_oi"] = to_numeric_col(work, "多空未平倉口數淨額")
    grouped = work.groupby("日期", as_index=False)["institution_net_oi"].sum().rename(columns={"日期": "date"})
    grouped["retail_mtx_net_oi_proxy"] = grouped["institution_net_oi"] * -1
    return last_six_months(grouped, "date")


def make_retail_mtx_proxy_chart(path: Path) -> Path:
    data = retail_mtx_proxy_history()
    if data.empty:
        return placeholder_chart(path, "Six-Month Retail MTX Proxy Positioning", "No mini-TAIEX futures institutional history available.")

    latest_value = data["retail_mtx_net_oi_proxy"].iloc[-1]
    path.parent.mkdir(parents=True, exist_ok=True)
    if len(data) < 2:
        msg = (
            f"Only {len(data)} usable observation. Latest proxy value: {clean_signed(latest_value)}. "
            "Workflow will extend this chart as daily data accumulates."
        )
        return placeholder_chart(path, "Six-Month Retail MTX Net OI Proxy", msg)

    fig, ax = plt.subplots(figsize=(11, 4.8))
    colors_bar = ["#d62728" if x > 0 else "#2ca02c" for x in data["retail_mtx_net_oi_proxy"]]
    ax.bar(data["_dt"], data["retail_mtx_net_oi_proxy"], color=colors_bar, alpha=0.75, width=1.8)
    ax.axhline(0, color="#333333", linewidth=0.8)
    ax.axhline(20000, color="#d62728", linestyle="--", linewidth=0.9, label="retail net long crowded")
    ax.axhline(-20000, color="#2ca02c", linestyle="--", linewidth=0.9, label="retail net short extreme")
    ax.set_title("Six-Month Retail Mini-TAIEX Futures Net OI Proxy", fontsize=13, fontweight="bold")
    ax.grid(True, axis="y", alpha=0.25)
    ax.legend(loc="upper left", fontsize=8)
    fig.autofmt_xdate()
    fig.tight_layout()
    fig.savefig(path, dpi=150, bbox_inches="tight")
    plt.close(fig)
    return path


def build_chart_outputs(index_history: pd.DataFrame) -> list[Path]:
    CHART_DIR.mkdir(parents=True, exist_ok=True)
    return [
        make_market_index_chart(index_history, MARKET_INDEX_CHART),
        make_risk_indicator_chart(RISK_INDICATOR_CHART),
        make_foreign_futures_chart(FOREIGN_FUTURES_CHART),
        make_retail_mtx_proxy_chart(RETAIL_MTX_PROXY_CHART),
    ]


def technical_pattern_notes(index_history: pd.DataFrame) -> list[str]:
    notes: list[str] = []
    data = last_six_months(index_history, "date")
    if data.empty:
        return ["- Market index history is unavailable; technical pattern notes cannot be generated."]
    for code, label in [("TWSE", "TWSE / TAIEX"), ("TPEX", "TPEx / OTC")]:
        part = data[data["index_code"].astype(str) == code].copy()
        if part.empty:
            notes.append(f"- {label}: no six-month data.")
            continue
        part["close"] = to_numeric_col(part, "close")
        close = part["close"].iloc[-1]
        six_month_high = part["close"].max()
        six_month_low = part["close"].min()
        distance_high = (close / six_month_high - 1) * 100 if six_month_high else math.nan
        regime = classify_market_regime(part.iloc[-1])
        ma20 = safe_str(part.iloc[-1].get("above_ma20", ""))
        ma60 = safe_str(part.iloc[-1].get("above_ma60", ""))
        notes.append(
            "- "
            + f"{label}: {regime}; close {clean_num(close, 2)}; "
            + f"6M range {clean_num(six_month_low, 2)}-{clean_num(six_month_high, 2)}; "
            + f"distance from 6M high {clean_signed(distance_high, 2)}%; "
            + f"above MA20={ma20}, above MA60={ma60}."
        )
    return notes


def markdown_table(rows: list[list[str]]) -> str:
    if not rows:
        return ""
    header = rows[0]
    lines = ["| " + " | ".join(header) + " |", "| " + " | ".join(["---"] * len(header)) + " |"]
    for row in rows[1:]:
        lines.append("| " + " | ".join(safe_str(x).replace("|", "/") for x in row) + " |")
    return "\n".join(lines)


def build_markdown(
    index_rows: pd.DataFrame,
    indicators: pd.Series,
    regime: pd.Series,
    status: dict[str, Any],
    index_history: pd.DataFrame,
    chart_paths: list[Path],
) -> str:
    twse = row_for_index(index_rows, "TWSE")
    tpex = row_for_index(index_rows, "TPEX")
    index_table = [["index", "close", "5d", "20d", "MA20", "MA60", "regime"]]
    for code, row in [("TWSE", twse), ("TPEx", tpex)]:
        index_table.append(
            [
                code,
                clean_num(row.get("close", ""), 2) if row is not None else "-",
                fmt_pct(row.get("return_5d", "")) if row is not None else "-",
                fmt_pct(row.get("return_20d", "")) if row is not None else "-",
                safe_str(row.get("above_ma20", "")) if row is not None else "-",
                safe_str(row.get("above_ma60", "")) if row is not None else "-",
                classify_market_regime(row),
            ]
        )

    inst_table = [
        ["indicator", "value", "state"],
        ["Foreign TX futures net OI", clean_signed(indicators.get("foreign_tx_futures_net_oi", "")), safe_str(regime.get("foreign_futures_state", ""))],
        ["Dealer TX futures net OI", clean_signed(indicators.get("dealer_tx_futures_net_oi", "")), ""],
        ["Trust TX futures net OI", clean_signed(indicators.get("trust_tx_futures_net_oi", "")), ""],
        ["Retail MTX net OI proxy", clean_signed(indicators.get("retail_mtx_net_oi_proxy", "")), safe_str(regime.get("retail_mtx_state", ""))],
        ["Foreign TXO call net OI", clean_signed(indicators.get("foreign_txo_call_net_oi", "")), ""],
        ["Foreign TXO put net OI", clean_signed(indicators.get("foreign_txo_put_net_oi", "")), ""],
        ["TXO put/call OI ratio", clean_num(indicators.get("put_call_oi_ratio_pct", ""), 2) + "%", safe_str(regime.get("put_call_state", ""))],
        ["Taiwan VIX", clean_num(indicators.get("taiwan_vix", ""), 2), safe_str(regime.get("vix_state", ""))],
    ]

    lines = [
        "# Market Risk Dashboard",
        "",
        f"- generated_at: `{now_text()}`",
        f"- data_date: `{safe_str(regime.get('date', ''))}`",
        f"- market_regime: `{safe_str(regime.get('market_regime', ''))}`",
        f"- risk_level: `{safe_str(regime.get('risk_level', ''))}`",
        f"- risk_score: `{safe_str(regime.get('risk_score', ''))}`",
        f"- futures_options_source_status: `{safe_str(indicators.get('source_status', 'missing'))}`",
        "",
        "## Data Status",
        "",
        "This report uses official market index data already stored in the repo plus TAIFEX open data for futures, options, put/call ratio, and Taiwan VIX. It is a market-background dashboard, not a trading instruction.",
        "",
        "| source | status | rows | latest_date |",
        "| --- | --- | ---: | --- |",
    ]
    for name, info in status.get("sources", {}).items():
        lines.append(f"| {name} | {info.get('status', '')} | {info.get('rows', 0)} | {info.get('latest_date', '')} |")

    lines.extend(
        [
            "",
            "## Market Index Regime",
            "",
            markdown_table(index_table),
            "",
            "## Futures / Options Positioning",
            "",
            markdown_table(inst_table),
            "",
            "## Six-Month Technical Charts",
            "",
            "The PDF version of this dashboard must include six-month charts for index trend, fear/option indicators, foreign futures positioning, and retail mini-TAIEX futures proxy positioning. If a source has insufficient history, the PDF still includes a placeholder chart and states the limitation.",
            "",
        ]
    )
    for path in chart_paths:
        lines.append(f"- chart: `{path.as_posix()}`")
    lines.extend(
        [
            "",
            "## Technical / Pattern Notes",
            "",
        ]
    )
    lines.extend(technical_pattern_notes(index_history))
    retail_proxy = to_number(indicators.get("retail_mtx_net_oi_proxy", ""))
    retail_state = safe_str(regime.get("retail_mtx_state", "unknown"))
    lines.extend(
        [
            "",
            "## Retail Mini-TAIEX Futures Proxy",
            "",
            "- This is a contrarian sentiment proxy, calculated as the negative of the three-institution net open interest in mini-TAIEX futures.",
            f"- latest_proxy_value: `{clean_signed(retail_proxy)}`",
            f"- state: `{retail_state}`",
            "- Positive proxy values mean non-three-institution accounts are net long MTX; crowded net-long readings are treated as a caution signal, not a standalone short signal.",
            "- Negative proxy values mean non-three-institution accounts are net short MTX; extreme net-short readings may support contrarian risk-on interpretation, but still need index confirmation.",
        ]
    )
    lines.extend(
        [
            "",
            "## Risk Notes",
            "",
        ]
    )
    reasons = [x.strip() for x in safe_str(regime.get("risk_reasons", "")).split(";") if x.strip()]
    if reasons:
        for reason in reasons:
            lines.append(f"- {reason}")
    else:
        lines.append("- No major risk note generated.")
    lines.extend(
        [
            "",
            "## Usage Boundary",
            "",
            "- Use this dashboard as market background for Taiwan index futures and portfolio exposure review.",
            "- Do not treat a single futures/options indicator as a buy or sell signal.",
            "- Keep this report separate from the daily all-market candidate-stock report; that report may cite market regime only as background.",
        ]
    )
    return "\n".join(lines) + "\n"


def register_font() -> str:
    try:
        pdfmetrics.registerFont(UnicodeCIDFont("STSong-Light"))
        return "STSong-Light"
    except Exception:
        return "Helvetica"


def build_pdf(markdown_text: str, output_path: Path, chart_paths: list[Path]) -> None:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    font_name = register_font()
    styles = getSampleStyleSheet()
    styles.add(ParagraphStyle(name="TitleTW", parent=styles["Title"], fontName=font_name, fontSize=20, leading=24))
    styles.add(ParagraphStyle(name="HeadingTW", parent=styles["Heading2"], fontName=font_name, fontSize=13, leading=17, spaceBefore=10))
    styles.add(ParagraphStyle(name="BodyTW", parent=styles["BodyText"], fontName=font_name, fontSize=9.5, leading=13, alignment=TA_LEFT))
    doc = SimpleDocTemplate(str(output_path), pagesize=A4, rightMargin=1.2 * cm, leftMargin=1.2 * cm, topMargin=1.1 * cm, bottomMargin=1.1 * cm)
    story: list[Any] = []
    for line in markdown_text.splitlines():
        if line.startswith("# "):
            story.append(Paragraph(line[2:], styles["TitleTW"]))
            story.append(Spacer(1, 8))
        elif line.startswith("## "):
            story.append(Paragraph(line[3:], styles["HeadingTW"]))
        elif line.startswith("| "):
            continue
        elif line.strip() == "":
            story.append(Spacer(1, 4))
        else:
            text = line
            if text.startswith("- "):
                text = "• " + text[2:]
            story.append(Paragraph(text, styles["BodyTW"]))
    story.append(PageBreak())
    story.append(Paragraph("Six-Month Technical Charts", styles["TitleTW"]))
    story.append(Spacer(1, 8))
    for idx, chart_path in enumerate(chart_paths, start=1):
        if not chart_path.exists():
            continue
        story.append(Paragraph(f"Chart {idx}: {chart_path.name}", styles["HeadingTW"]))
        if chart_path.name in {FOREIGN_FUTURES_CHART.name, RETAIL_MTX_PROXY_CHART.name}:
            story.append(Image(str(chart_path), width=17.5 * cm, height=7.6 * cm))
        else:
            story.append(Image(str(chart_path), width=17.5 * cm, height=11.3 * cm))
        story.append(Spacer(1, 8))
    doc.build(story)


def main() -> int:
    index_history = load_market_index_history(update_if_missing=True)
    if index_history.empty:
        index_rows = pd.DataFrame()
    else:
        index_rows = index_history.sort_values(["index_code", "date"]).groupby("index_code", as_index=False).tail(1)
    indicators_df = read_csv(INDICATORS_CSV, dtype=str)
    if indicators_df.empty:
        raise FileNotFoundError(f"Missing or empty {INDICATORS_CSV}. Run scripts/fetch_futures_options_indicators.py first.")
    indicators = indicators_df.iloc[-1]
    source_status = json.loads(SOURCE_STATUS_JSON.read_text(encoding="utf-8")) if SOURCE_STATUS_JSON.exists() else {}
    regime_df = build_regime_row(index_rows, indicators)
    write_csv(regime_df, MARKET_REGIME_CSV)

    chart_paths = build_chart_outputs(index_history)
    md = build_markdown(index_rows, indicators, regime_df.iloc[0], source_status, index_history, chart_paths)
    REPORT_MD.write_text(md, encoding="utf-8")
    build_pdf(md, REPORT_PDF, chart_paths)
    DOCS_LATEST_DIR.mkdir(parents=True, exist_ok=True)
    shutil.copy2(REPORT_PDF, DOCS_REPORT_PDF)

    manifest = {
        "generated_at": now_text(),
        "market_regime_csv": MARKET_REGIME_CSV.as_posix(),
        "report_md": REPORT_MD.as_posix(),
        "report_pdf": REPORT_PDF.as_posix(),
        "docs_report_pdf": DOCS_REPORT_PDF.as_posix(),
        "chart_lookback": "six_months",
        "chart_paths": [path.as_posix() for path in chart_paths],
        "source_status": safe_str(indicators.get("source_status", "missing")),
    }
    MANIFEST_JSON.write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Saved: {MARKET_REGIME_CSV}")
    print(f"Saved: {REPORT_MD}")
    print(f"Saved: {REPORT_PDF}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
