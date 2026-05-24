from __future__ import annotations

from pathlib import Path
from typing import Any
import json
import math
import shutil

import pandas as pd

from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import cm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.cidfonts import UnicodeCIDFont
from reportlab.platypus import Paragraph, SimpleDocTemplate, Spacer, Table, TableStyle

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
MARKET_REGIME_CSV = LATEST_DIR / "market_regime_latest.csv"
REPORT_MD = LATEST_DIR / "market_risk_dashboard_latest.md"
REPORT_PDF = LATEST_DIR / "market_risk_dashboard_latest.pdf"
DOCS_REPORT_PDF = DOCS_LATEST_DIR / REPORT_PDF.name
MANIFEST_JSON = LATEST_DIR / "market_risk_dashboard_manifest_latest.json"


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
        "source_status": indicators.get("source_status", "missing"),
    }
    return pd.DataFrame([row])


def markdown_table(rows: list[list[str]]) -> str:
    if not rows:
        return ""
    header = rows[0]
    lines = ["| " + " | ".join(header) + " |", "| " + " | ".join(["---"] * len(header)) + " |"]
    for row in rows[1:]:
        lines.append("| " + " | ".join(safe_str(x).replace("|", "/") for x in row) + " |")
    return "\n".join(lines)


def build_markdown(index_rows: pd.DataFrame, indicators: pd.Series, regime: pd.Series, status: dict[str, Any]) -> str:
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


def build_pdf(markdown_text: str, output_path: Path) -> None:
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
    doc.build(story)


def main() -> int:
    index_rows = latest_index_rows()
    indicators_df = read_csv(INDICATORS_CSV, dtype=str)
    if indicators_df.empty:
        raise FileNotFoundError(f"Missing or empty {INDICATORS_CSV}. Run scripts/fetch_futures_options_indicators.py first.")
    indicators = indicators_df.iloc[-1]
    source_status = json.loads(SOURCE_STATUS_JSON.read_text(encoding="utf-8")) if SOURCE_STATUS_JSON.exists() else {}
    regime_df = build_regime_row(index_rows, indicators)
    write_csv(regime_df, MARKET_REGIME_CSV)

    md = build_markdown(index_rows, indicators, regime_df.iloc[0], source_status)
    REPORT_MD.write_text(md, encoding="utf-8")
    build_pdf(md, REPORT_PDF)
    DOCS_LATEST_DIR.mkdir(parents=True, exist_ok=True)
    shutil.copy2(REPORT_PDF, DOCS_REPORT_PDF)

    manifest = {
        "generated_at": now_text(),
        "market_regime_csv": MARKET_REGIME_CSV.as_posix(),
        "report_md": REPORT_MD.as_posix(),
        "report_pdf": REPORT_PDF.as_posix(),
        "docs_report_pdf": DOCS_REPORT_PDF.as_posix(),
        "source_status": safe_str(indicators.get("source_status", "missing")),
    }
    MANIFEST_JSON.write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Saved: {MARKET_REGIME_CSV}")
    print(f"Saved: {REPORT_MD}")
    print(f"Saved: {REPORT_PDF}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
