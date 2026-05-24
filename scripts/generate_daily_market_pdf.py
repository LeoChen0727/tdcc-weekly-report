from __future__ import annotations

from datetime import datetime
from pathlib import Path
from typing import Any
from zoneinfo import ZoneInfo
import json
import math
import re
import shutil

import pandas as pd

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.lib.pagesizes import A4, landscape
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import cm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.cidfonts import UnicodeCIDFont
from reportlab.platypus import (
    KeepTogether,
    PageBreak,
    Paragraph,
    SimpleDocTemplate,
    Spacer,
    Table,
    TableStyle,
)


OWNER_REPO = "LeoChen0727/tdcc-weekly-report"
RAW_PREFIX = f"https://raw.githubusercontent.com/{OWNER_REPO}/main"
PAGES_PREFIX = "https://LeoChen0727.github.io/tdcc-weekly-report"

LATEST_DIR = Path("output/latest")
DOCS_LATEST_DIR = Path("docs/latest")
HISTORY_REPORT_DIR = Path("output/history/reports")

ALL_CANDIDATES_CSV = LATEST_DIR / "all_candidates_latest.csv"
DATA_FRESHNESS_CSV = LATEST_DIR / "data_freshness_latest.csv"
MARKET_REGIME_CSV = LATEST_DIR / "market_regime_latest.csv"
WARRANT_FLOW_BY_STOCK_CSV = LATEST_DIR / "warrant_flow_by_stock_latest.csv"

CURATED_PDF = LATEST_DIR / "daily_market_curated_report_latest.pdf"
FULL_TABLE_PDF = LATEST_DIR / "daily_market_full_table_report_latest.pdf"
DOCS_CURATED_PDF = DOCS_LATEST_DIR / CURATED_PDF.name
DOCS_FULL_TABLE_PDF = DOCS_LATEST_DIR / FULL_TABLE_PDF.name
MANIFEST_JSON = LATEST_DIR / "daily_market_pdf_report_manifest_latest.json"
MANIFEST_MD = LATEST_DIR / "daily_market_pdf_report_manifest_latest.md"

CATEGORY_ORDER = [
    "true_breakout",
    "range_rebound",
    "revenue_breakout_low_response",
    "revenue_pullback",
    "pullback_rebound",
    "pattern",
]

EXCLUDED_FINAL_REPORT_CATEGORIES = {"chip_flow_positive_streak"}

CATEGORY_LABEL = {
    "true_breakout": "嚴格突破",
    "range_rebound": "區間內轉強 / 挑戰前高觀察",
    "near_resistance": "區間內轉強 / 挑戰前高觀察",
    "abnormal_volume_up": "區間內轉強 / 挑戰前高觀察",
    "revenue_breakout_low_response": "營收爆發低反應股",
    "revenue_pullback": "營收成長股價回檔",
    "pullback_rebound": "回檔後短線轉強",
    "pattern": "型態觀察",
}

CATEGORY_SHORT = {
    "true_breakout": "嚴格突破",
    "range_rebound": "區間轉強",
    "revenue_breakout_low_response": "營收低反應",
    "revenue_pullback": "營收回檔",
    "pullback_rebound": "短線轉強",
    "pattern": "型態觀察",
}

MATRIX_COLUMNS = {
    "true_breakout": "嚴格突破",
    "range_rebound": "區間轉強",
    "revenue_breakout_low_response": "營收低反應",
    "revenue_pullback": "營收回檔",
    "pullback_rebound": "短線轉強",
    "pattern": "型態觀察",
}

BULLISH_WARRANT_SIGNALS = {
    "call_strong_inflow",
    "call_inflow",
    "call_put_bullish",
    "low_float_call_spike",
}

FORBIDDEN_WORD_REPLACEMENTS = {
    "持股": "候選名單",
    "成本": "價格區",
    "損益": "表現",
    "融資": "槓桿",
    "個人部位": "市場候選",
    "我的持股": "市場候選",
    "張": "單位",
}


def now_taipei() -> datetime:
    return datetime.now(ZoneInfo("Asia/Taipei"))


def now_text() -> str:
    return now_taipei().strftime("%Y-%m-%d %H:%M:%S Asia/Taipei")


def safe_str(value: Any) -> str:
    if value is None:
        return ""
    try:
        if pd.isna(value):
            return ""
    except Exception:
        pass
    text = str(value).strip()
    if text.lower() in {"nan", "none", "nat"}:
        return ""
    return text


def safe_float(value: Any, default: float = math.nan) -> float:
    text = safe_str(value).replace(",", "")
    if not text:
        return default
    try:
        return float(text)
    except Exception:
        return default


def safe_int(value: Any, default: int = 0) -> int:
    num = safe_float(value)
    if math.isnan(num):
        return default
    return int(num)


def clean_text(text: Any, limit: int | None = None) -> str:
    result = safe_str(text)
    result = result.replace("\n", " ").replace("\r", " ").replace("|", "/")
    result = re.sub(r"\s+", " ", result).strip()
    for old, new in FORBIDDEN_WORD_REPLACEMENTS.items():
        result = result.replace(old, new)
    if limit and len(result) > limit:
        result = result[: max(0, limit - 1)] + "…"
    return result


def pct_text(value: Any, suffix: str = "%") -> str:
    num = safe_float(value)
    if math.isnan(num):
        return ""
    return f"{num:.1f}{suffix}"


def num_text(value: Any, digits: int = 1) -> str:
    num = safe_float(value)
    if math.isnan(num):
        return ""
    return f"{num:.{digits}f}"


def raw_url(path: Path) -> str:
    return f"{RAW_PREFIX}/{path.as_posix()}"


def pages_url(path: Path) -> str:
    if path.as_posix().startswith("docs/"):
        rel = path.relative_to("docs").as_posix()
    elif path.as_posix().startswith("output/latest/"):
        rel = path.relative_to("output").as_posix()
    else:
        rel = path.as_posix()
    return f"{PAGES_PREFIX}/{rel}"


def register_font() -> str:
    try:
        pdfmetrics.registerFont(UnicodeCIDFont("STSong-Light"))
        return "STSong-Light"
    except Exception:
        return "Helvetica"


def escape_html(text: Any) -> str:
    return clean_text(text).replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def para(text: Any, style: ParagraphStyle) -> Paragraph:
    return Paragraph(escape_html(text), style)


def styles() -> dict[str, ParagraphStyle]:
    font = register_font()
    base = getSampleStyleSheet()
    return {
        "title": ParagraphStyle(
            "title",
            parent=base["Title"],
            fontName=font,
            fontSize=22,
            leading=30,
            alignment=TA_CENTER,
            textColor=colors.HexColor("#1D3557"),
            spaceAfter=12,
        ),
        "subtitle": ParagraphStyle(
            "subtitle",
            parent=base["Normal"],
            fontName=font,
            fontSize=12,
            leading=18,
            alignment=TA_CENTER,
            textColor=colors.HexColor("#44546A"),
            spaceAfter=8,
        ),
        "h1": ParagraphStyle(
            "h1",
            parent=base["Heading1"],
            fontName=font,
            fontSize=16,
            leading=22,
            textColor=colors.HexColor("#1D3557"),
            spaceBefore=10,
            spaceAfter=8,
        ),
        "h2": ParagraphStyle(
            "h2",
            parent=base["Heading2"],
            fontName=font,
            fontSize=13,
            leading=18,
            textColor=colors.HexColor("#2F5597"),
            spaceBefore=8,
            spaceAfter=5,
        ),
        "normal": ParagraphStyle(
            "normal",
            parent=base["Normal"],
            fontName=font,
            fontSize=10.2,
            leading=15,
            spaceAfter=5,
        ),
        "small": ParagraphStyle(
            "small",
            parent=base["Normal"],
            fontName=font,
            fontSize=8.0,
            leading=11,
            spaceAfter=3,
        ),
        "tiny": ParagraphStyle(
            "tiny",
            parent=base["Normal"],
            fontName=font,
            fontSize=7.0,
            leading=9,
        ),
        "table_header": ParagraphStyle(
            "table_header",
            parent=base["Normal"],
            fontName=font,
            fontSize=7.6,
            leading=9.5,
            alignment=TA_CENTER,
            textColor=colors.white,
        ),
        "table_cell": ParagraphStyle(
            "table_cell",
            parent=base["Normal"],
            fontName=font,
            fontSize=7.0,
            leading=9,
            alignment=TA_LEFT,
        ),
        "curated_cell": ParagraphStyle(
            "curated_cell",
            parent=base["Normal"],
            fontName=font,
            fontSize=9.0,
            leading=12.5,
            alignment=TA_LEFT,
        ),
        "label": ParagraphStyle(
            "label",
            parent=base["Normal"],
            fontName=font,
            fontSize=8.7,
            leading=11,
            textColor=colors.HexColor("#44546A"),
        ),
    }


def load_freshness() -> dict[str, Any]:
    if not DATA_FRESHNESS_CSV.exists():
        return {}
    try:
        df = pd.read_csv(DATA_FRESHNESS_CSV, dtype=str)
        if not df.empty:
            return df.iloc[0].fillna("").to_dict()
    except Exception:
        return {}
    return {}


def load_candidates() -> pd.DataFrame:
    if not ALL_CANDIDATES_CSV.exists():
        raise FileNotFoundError(f"Missing {ALL_CANDIDATES_CSV}")
    df = pd.read_csv(ALL_CANDIDATES_CSV, dtype=str, keep_default_na=False)
    if "category" in df.columns:
        df = df[~df["category"].astype(str).isin(EXCLUDED_FINAL_REPORT_CATEGORIES)].copy()
    for col in ["score", "rank", "volume_ratio", "return_20d", "return_60d", "return_120d"]:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors="coerce")
    df["category_key"] = df.apply(category_key, axis=1)
    df["group_name"] = df.apply(group_name, axis=1)
    df["priority_label"] = df.apply(priority_label, axis=1)
    df["sort_score"] = df.apply(sort_score, axis=1)
    return df


def load_first_csv_row(path: Path) -> dict[str, Any]:
    if not path.exists():
        return {}
    try:
        df = pd.read_csv(path, dtype=str, keep_default_na=False)
    except Exception:
        return {}
    if df.empty:
        return {}
    return df.iloc[0].fillna("").to_dict()


def signed_pct_text(value: Any) -> str:
    num = safe_float(value)
    if math.isnan(num):
        return "n/a"
    return f"{num:+.2f}%"


def compact_number(value: Any, digits: int = 0) -> str:
    num = safe_float(value)
    if math.isnan(num):
        return "n/a"
    return f"{num:,.{digits}f}"


def bool_marker(value: Any) -> str:
    text = safe_str(value).lower()
    if text in {"true", "1", "yes", "y"}:
        return "yes"
    if text in {"false", "0", "no", "n"}:
        return "no"
    return safe_str(value) or "n/a"


def market_context_rows() -> list[list[Any]]:
    row = load_first_csv_row(MARKET_REGIME_CSV)
    if not row:
        return [["Item", "Status"], ["Market background", "market_regime_latest.csv is not available"]]

    twse = (
        f"close {compact_number(row.get('twse_close'), 2)}; "
        f"5d {signed_pct_text(row.get('twse_return_5d'))}; "
        f"20d {signed_pct_text(row.get('twse_return_20d'))}; "
        f"MA20 {bool_marker(row.get('twse_above_ma20'))}; "
        f"MA60 {bool_marker(row.get('twse_above_ma60'))}"
    )
    tpex = (
        f"close {compact_number(row.get('tpex_close'), 2)}; "
        f"5d {signed_pct_text(row.get('tpex_return_5d'))}; "
        f"20d {signed_pct_text(row.get('tpex_return_20d'))}; "
        f"MA20 {bool_marker(row.get('tpex_above_ma20'))}; "
        f"MA60 {bool_marker(row.get('tpex_above_ma60'))}"
    )
    futures_options = (
        f"Foreign TX futures net OI {compact_number(row.get('foreign_tx_futures_net_oi'))}; "
        f"TXO P/C OI {compact_number(row.get('put_call_oi_ratio_pct'), 2)}%; "
        f"Taiwan VIX {compact_number(row.get('taiwan_vix'), 2)}"
    )

    return [
        ["Item", "Status"],
        ["Market regime", f"{safe_str(row.get('market_regime')) or 'n/a'} / {safe_str(row.get('risk_level')) or 'n/a'} / risk_score {safe_str(row.get('risk_score')) or 'n/a'}"],
        ["TWSE", twse],
        ["TPEx", tpex],
        ["Futures/options", futures_options],
        ["Risk notes", clean_text(row.get("risk_reasons", ""), 140) or "n/a"],
    ]


def warrant_context_rows(freshness: dict[str, Any]) -> list[list[Any]]:
    if not WARRANT_FLOW_BY_STOCK_CSV.exists():
        return [["Item", "Status"], ["Warrant market", "warrant_flow_by_stock_latest.csv is not available"]]
    try:
        df = pd.read_csv(WARRANT_FLOW_BY_STOCK_CSV, dtype=str, keep_default_na=False)
    except Exception:
        return [["Item", "Status"], ["Warrant market", "failed to read warrant_flow_by_stock_latest.csv"]]
    if df.empty:
        return [["Item", "Status"], ["Warrant market", "no stock-level warrant rows"]]

    numeric_cols = [
        "call_turnover",
        "put_turnover",
        "call_warrant_count",
        "put_warrant_count",
        "total_warrant_volume",
    ]
    for col in numeric_cols:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors="coerce").fillna(0)

    date = safe_str(df.iloc[0].get("date", "")) or safe_str(freshness.get("warrant_flow_date", ""))
    call_turnover = float(df["call_turnover"].sum()) if "call_turnover" in df.columns else 0.0
    put_turnover = float(df["put_turnover"].sum()) if "put_turnover" in df.columns else 0.0
    call_count = int(df["call_warrant_count"].sum()) if "call_warrant_count" in df.columns else 0
    put_count = int(df["put_warrant_count"].sum()) if "put_warrant_count" in df.columns else 0
    candidate_overlap = 0
    if "candidate_category" in df.columns:
        candidate_overlap = int(df["candidate_category"].astype(str).str.strip().ne("").sum())
    turnover_ready = call_turnover > 0 or put_turnover > 0

    top_col = "call_turnover" if turnover_ready and "call_turnover" in df.columns else "call_warrant_count"
    top_names = []
    if top_col in df.columns:
        top_names = (
            df.sort_values(top_col, ascending=False)
            .head(5)
            .apply(lambda row: f"{safe_str(row.get('stock_id'))} {clean_text(row.get('stock_name'), 12)}", axis=1)
            .tolist()
        )

    readiness_note = (
        "turnover data ready"
        if turnover_ready
        else "turnover amount is zero or missing; use warrant counts and candidate overlap only"
    )
    return [
        ["Item", "Status"],
        ["Warrant date", date or "n/a"],
        ["Market breadth", f"stock-level rows {len(df)}; candidate overlap {candidate_overlap}"],
        ["Call/put scale", f"call warrants {call_count:,}; put warrants {put_count:,}; call turnover {call_turnover:,.0f}; put turnover {put_turnover:,.0f}"],
        ["Top call-side names", ", ".join(top_names) if top_names else "n/a"],
        ["Readiness", readiness_note],
    ]


def append_context_sections(
    story: list[Any],
    style_map: dict[str, ParagraphStyle],
    freshness: dict[str, Any],
    widths: list[float],
) -> None:
    story.append(para("Market Background and Warrant Summary", style_map["h1"]))
    story.append(
        para(
            "This section is context only. Candidate categories, scores, and ranks remain category-specific; warrant and futures/options data are auxiliary signals.",
            style_map["normal"],
        )
    )
    story.append(para("Market regime / futures-options", style_map["h2"]))
    story.append(make_table(market_context_rows(), style_map, widths, header_bg="#2F5597"))
    story.append(Spacer(1, 0.25 * cm))
    story.append(para("Warrant market summary", style_map["h2"]))
    story.append(make_table(warrant_context_rows(freshness), style_map, widths, header_bg="#7F6000"))
    story.append(Spacer(1, 0.35 * cm))


def category_key(row: pd.Series) -> str:
    cat = safe_str(row.get("category", ""))
    if cat in {"range_rebound", "near_resistance", "abnormal_volume_up"}:
        return "range_rebound"
    if cat in CATEGORY_LABEL:
        return cat
    label = safe_str(row.get("category_cn", ""))
    for key, text in CATEGORY_LABEL.items():
        if label == text:
            return "range_rebound" if key in {"near_resistance", "abnormal_volume_up"} else key
    return cat or "other"


def group_name(row: pd.Series) -> str:
    for col in ["細分族群", "industry", "theme_group", "market"]:
        value = clean_text(row.get(col, ""))
        if value:
            return value
    return "其他"


def tdcc_signal(row: pd.Series) -> str:
    for col in ["tdcc_accumulation_signal", "tdcc_judgement", "tdcc_judge"]:
        value = safe_str(row.get(col, ""))
        if value in {"strong_accumulation", "mild_accumulation", "neutral", "distribution_warning"}:
            return value
        if "同步累積" in value or "強" in value:
            return "strong_accumulation"
        if "溫和" in value or "增加" in value:
            return "mild_accumulation"
        if "轉弱" in value or "減少" in value:
            return "distribution_warning"
    note = safe_str(row.get("tdcc_accumulation_note", ""))
    if "同步累積" in note:
        return "strong_accumulation"
    if "溫和" in note or "增加" in note:
        return "mild_accumulation"
    if "轉弱" in note or "減少" in note:
        return "distribution_warning"
    return "neutral"


def warrant_signal(row: pd.Series, warrant_flow_date: str) -> str:
    if not warrant_flow_date:
        return "權證資料不足 / 今日不作為主要判斷"
    value = safe_str(row.get("warrant_flow_signal", ""))
    if value:
        return value
    note = clean_text(row.get("warrant_note", ""))
    if note:
        return note
    return "no_signal"


def is_truthy(value: Any) -> bool:
    text = safe_str(value).lower()
    return text in {"true", "1", "yes", "y"}


def overheated(row: pd.Series) -> bool:
    return any(
        safe_float(row.get(col)) >= threshold
        for col, threshold in [
            ("return_20d", 35),
            ("return_20d_pct", 35),
            ("return_60d", 55),
            ("return_60d_pct", 55),
            ("return_120d", 90),
            ("return_120d_pct", 90),
        ]
    )


def priority_label(row: pd.Series) -> str:
    tdcc = tdcc_signal(row)
    rev = clean_text(row.get("revaluation_priority", ""))
    if tdcc == "distribution_warning" or rev.startswith("D_") or is_truthy(row.get("already_priced_in", "")) or overheated(row):
        return "暫避降級"
    if rev.startswith("A_") and tdcc in {"strong_accumulation", "mild_accumulation"}:
        return "最優先追蹤"
    if row.get("category_key") == "true_breakout" and tdcc in {"strong_accumulation", "mild_accumulation"}:
        return "最優先追蹤"
    if rev.startswith("B_") or tdcc in {"strong_accumulation", "mild_accumulation"}:
        return "可等確認"
    return "僅觀察"


def sort_score(row: pd.Series) -> float:
    priority_bonus = {
        "最優先追蹤": 1000,
        "可等確認": 700,
        "僅觀察": 350,
        "暫避降級": 0,
    }.get(safe_str(row.get("priority_label", "")), 0)
    tdcc_bonus = {
        "strong_accumulation": 180,
        "mild_accumulation": 120,
        "neutral": 30,
        "distribution_warning": -250,
    }.get(tdcc_signal(row), 0)
    score = safe_float(row.get("score"), 0)
    rank = safe_float(row.get("rank"), 9999)
    rank_bonus = max(0, 100 - rank) if not math.isnan(rank) else 0
    volume_bonus = min(safe_float(row.get("volume_ratio"), 0) * 10, 60)
    return priority_bonus + tdcc_bonus + score + rank_bonus + volume_bonus


def score_rank_text(row: pd.Series) -> str:
    parts: list[str] = []
    score = num_text(row.get("score"), 1)
    rank = num_text(row.get("rank"), 0)
    priority = clean_text(row.get("revaluation_priority", ""))
    if score:
        parts.append(f"score {score}")
    if rank:
        parts.append(f"rank {rank}")
    if priority:
        parts.append(priority)
    return " / ".join(parts) if parts else "無分數"


def stock_text(row: pd.Series) -> str:
    return f"{safe_str(row.get('stock_id', ''))} {clean_text(row.get('stock_name', ''))}".strip()


def reason_text(row: pd.Series) -> str:
    cat = safe_str(row.get("category_key", ""))
    parts: list[str] = []
    if cat == "revenue_breakout_low_response":
        latest = pct_text(row.get("latest_revenue_yoy") or row.get("revenue_yoy_pct"))
        cum = pct_text(row.get("cumulative_revenue_yoy") or row.get("cumulative_yoy_pct"))
        if latest:
            parts.append(f"單月營收 YoY {latest}")
        if cum:
            parts.append(f"累計營收 YoY {cum}")
        parts.append("股價反應仍偏低，適合等確認")
    elif cat == "revenue_pullback":
        latest = pct_text(row.get("latest_revenue_yoy") or row.get("revenue_yoy_pct"))
        if latest:
            parts.append(f"營收 YoY {latest}")
        parts.append("價格回到支撐區附近")
    elif cat == "range_rebound":
        dist = pct_text(row.get("distance_to_previous_60d_high_pct"))
        if dist:
            parts.append(f"距前高 {dist}")
        vr = num_text(row.get("volume_ratio"), 2)
        if vr:
            parts.append(f"量比 {vr}x")
        parts.append("區間內轉強，仍需突破確認")
    elif cat == "pullback_rebound":
        vr = num_text(row.get("volume_ratio"), 2)
        if vr:
            parts.append(f"量比 {vr}x")
        parts.append("回檔後出現短線轉強")
    elif cat == "true_breakout":
        vr = num_text(row.get("volume_ratio"), 2)
        if vr:
            parts.append(f"量比 {vr}x")
        parts.append("價量突破訊號")
    elif cat == "pattern":
        pattern = clean_text(row.get("pattern") or row.get("pattern_stage"), 28)
        parts.append(pattern or "型態進入觀察區")
    tdcc = tdcc_signal(row)
    if tdcc in {"strong_accumulation", "mild_accumulation"}:
        parts.append(f"TDCC {tdcc}")
    return clean_text("；".join(parts), 130)


def risk_text(row: pd.Series, warrant_flow_date: str) -> str:
    risks: list[str] = []
    tdcc = tdcc_signal(row)
    if tdcc == "distribution_warning":
        risks.append("TDCC 轉弱，訊號可靠度下降")
    if is_truthy(row.get("already_priced_in", "")):
        risks.append("漲幅可能已提前反應")
    if overheated(row):
        risks.append("短中期漲幅偏高")
    warning = clean_text(row.get("warrant_flow_warning", "") or row.get("revenue_warning", ""), 40)
    if warning:
        risks.append(warning)
    if not warrant_flow_date:
        risks.append("權證資料不足")
    if not risks:
        risks.append("需等量能與價格續強確認")
    return clean_text("；".join(risks), 120)


def confirm_text(row: pd.Series) -> str:
    cat = safe_str(row.get("category_key", ""))
    if cat == "true_breakout":
        return "突破價上方換手，成交量維持且不跌回平台。"
    if cat == "range_rebound":
        return "收盤續守 20MA/23EMA，量能不失速，再觀察前高壓力。"
    if cat == "revenue_breakout_low_response":
        return "營收強勢延續，股價站穩均線或平台且未快速過熱。"
    if cat == "revenue_pullback":
        return "回檔守支撐後量能回升，避免跌破關鍵均線。"
    if cat == "pullback_rebound":
        return "轉強後不跌破轉折低點，量能延續。"
    if cat == "pattern":
        return "型態頸線或平台突破，或回測不破。"
    return "隔日價量確認。"


def catalyst_brief(row: pd.Series) -> str:
    catalyst_tags = clean_text(row.get("catalyst_tags", ""), 70)
    tags = clean_text(row.get("fundamental_catalyst_tags", ""), 70)
    event_tags = clean_text(row.get("event_catalyst_tags", ""), 60)
    score = clean_text(row.get("catalyst_strength_score", "")) or clean_text(row.get("fundamental_catalyst_score", ""))
    theme_score = clean_text(row.get("theme_strength_score", ""))
    reaction_level = clean_text(row.get("price_reaction_level", ""))
    quality = clean_text(row.get("catalyst_quality", ""))
    low_reaction = is_truthy(row.get("low_reaction_after_catalyst", ""))
    already = is_truthy(row.get("already_reacted_to_catalyst", "")) or is_truthy(row.get("catalyst_overheated", ""))
    similar = is_truthy(row.get("similar_to_shihsinko_flag", ""))
    revenue_unconfirmed = is_truthy(row.get("revenue_good_eps_unconfirmed_flag", ""))
    summary = clean_text(row.get("catalyst_summary", ""), 110)

    parts: list[str] = []
    if score:
        parts.append(f"score {score}")
    if theme_score:
        parts.append(f"theme {theme_score}/5")
    if catalyst_tags:
        parts.append(catalyst_tags)
    if tags:
        parts.append(tags)
    if event_tags:
        parts.append(event_tags)
    if reaction_level:
        parts.append(f"reaction {reaction_level}")
    if similar:
        parts.append("類事欣科型")
    elif revenue_unconfirmed:
        parts.append("營收好但 EPS 尚未確認")
    if low_reaction:
        parts.append("利多尚未完全反應")
    if already:
        parts.append("利多已反應/過熱降級")
    if quality:
        parts.append(quality)
    if summary:
        parts.append(summary)
    return clean_text(" / ".join(parts), 180) if parts else "無明確財報/事件催化資料"


def catalyst_rows(df: pd.DataFrame) -> list[list[Any]]:
    if df.empty or "fundamental_catalyst_score" not in df.columns:
        return [["Stock", "Original category", "Catalyst layer", "TDCC / action"], ["n/a", "n/a", "No catalyst layer columns available", "keep original category"]]

    part = df.copy()
    part["_catalyst_score_sort"] = pd.to_numeric(part.get("catalyst_strength_score", part.get("fundamental_catalyst_score", "")), errors="coerce").fillna(0)
    mask = (
        part["_catalyst_score_sort"].gt(0)
        | part.get("similar_to_shihsinko_flag", pd.Series("", index=part.index)).astype(str).eq("True")
        | part.get("revenue_good_eps_unconfirmed_flag", pd.Series("", index=part.index)).astype(str).eq("True")
        | part.get("already_reacted_to_catalyst", pd.Series("", index=part.index)).astype(str).eq("True")
    )
    part = part[mask].sort_values("_catalyst_score_sort", ascending=False).head(12)

    rows: list[list[Any]] = [["Stock", "Original category", "Catalyst layer", "TDCC / action"]]
    if part.empty:
        rows.append(["n/a", "n/a", "No confirmed EPS/event catalyst today", "Do not upgrade without source data"])
        return rows

    for _, row in part.iterrows():
        action = "觀察"
        if is_truthy(row.get("similar_to_shihsinko_flag", "")):
            action = "可升級觀察"
        elif is_truthy(row.get("revenue_good_eps_unconfirmed_flag", "")):
            action = "等 EPS 確認"
        if is_truthy(row.get("already_reacted_to_catalyst", "")) or tdcc_signal(row) == "distribution_warning":
            action = "降級/僅觀察"
        rows.append(
            [
                stock_text(row),
                CATEGORY_LABEL.get(safe_str(row.get("category_key", "")), safe_str(row.get("category_cn", ""))),
                catalyst_brief(row),
                f"{tdcc_signal(row)} / {action}",
            ]
        )
    return rows


def append_catalyst_section(story: list[Any], style_map: dict[str, ParagraphStyle], df: pd.DataFrame) -> None:
    story.append(para("財報 / 事件催化觀察", style_map["h1"]))
    story.append(
        para(
            "此段是跨分類催化層，不新增第七大分類；EPS、毛利率、重大事件與題材來源不足時，只標示待確認，不把營收好直接升級為類事欣科型。",
            style_map["normal"],
        )
    )
    story.append(
        make_table(
            catalyst_rows(df),
            style_map,
            [3.1 * cm, 3.1 * cm, 7.2 * cm, 3.6 * cm],
            header_bg="#7030A0",
        )
    )
    story.append(Spacer(1, 0.35 * cm))


def downgrade_reason(row: pd.Series) -> str:
    items: list[str] = []
    if tdcc_signal(row) == "distribution_warning":
        items.append("TDCC 轉弱")
    if is_truthy(row.get("already_priced_in", "")):
        items.append("漲幅已反應")
    if overheated(row):
        items.append("漲幅偏熱")
    warning = clean_text(row.get("warrant_flow_warning", ""), 28)
    if warning:
        items.append(warning)
    return clean_text("；".join(items))


def category_groups(df: pd.DataFrame) -> list[tuple[str, pd.DataFrame]]:
    groups: list[tuple[str, pd.DataFrame]] = []
    for cat in CATEGORY_ORDER:
        part = df[df["category_key"] == cat].copy()
        part = part.sort_values(["sort_score"], ascending=False)
        groups.append((cat, part))
    return groups


def selected_by_category(df: pd.DataFrame, limit_default: int = 5) -> dict[str, pd.DataFrame]:
    limits = {
        "true_breakout": 6,
        "range_rebound": 5,
        "revenue_breakout_low_response": 6,
        "revenue_pullback": 5,
        "pullback_rebound": 5,
        "pattern": 5,
    }
    result: dict[str, pd.DataFrame] = {}
    for cat, part in category_groups(df):
        if part.empty:
            result[cat] = part
            continue
        if cat == "revenue_breakout_low_response":
            preferred = part[
                (part["priority_label"].isin(["最優先追蹤", "可等確認"]))
                & (part.apply(tdcc_signal, axis=1).isin(["strong_accumulation", "mild_accumulation"]))
            ].copy()
            if preferred.empty:
                preferred = part[part["priority_label"] != "暫避降級"].copy()
            part = preferred if not preferred.empty else part
        else:
            usable = part[part["priority_label"] != "暫避降級"].copy()
            if not usable.empty:
                part = usable
        result[cat] = part.head(limits.get(cat, limit_default)).copy()
    return result


def top_watchlist(selected: dict[str, pd.DataFrame]) -> pd.DataFrame:
    pieces = []
    for cat in CATEGORY_ORDER:
        part = selected.get(cat, pd.DataFrame()).copy()
        if part.empty:
            continue
        part = part[part["priority_label"].isin(["最優先追蹤", "可等確認"])].copy()
        if not part.empty:
            pieces.append(part.head(2))
    if not pieces:
        return pd.DataFrame()
    out = pd.concat(pieces, ignore_index=True)
    return out.sort_values("sort_score", ascending=False).head(10)


def market_conclusion(df: pd.DataFrame) -> str:
    counts = df["category_key"].value_counts().to_dict()
    group_counts = df["group_name"].value_counts().head(3)
    top_groups = "、".join(group_counts.index.tolist()) if not group_counts.empty else "分散族群"
    main_cat = max(counts, key=counts.get) if counts else ""
    main_cat_text = CATEGORY_LABEL.get(main_cat, "分散訊號")
    return clean_text(
        f"今日候選集中在 {top_groups}，主要訊號為 {main_cat_text}；優先看有 TDCC 支持、未過熱且明日價量能確認的標的。",
        120,
    )


def make_table(rows: list[list[Any]], style_map: dict[str, ParagraphStyle], widths: list[float], header_bg: str = "#1D3557") -> Table:
    wrapped: list[list[Paragraph]] = []
    for row_idx, row in enumerate(rows):
        style = style_map["table_header"] if row_idx == 0 else style_map["table_cell"]
        wrapped.append([para(cell, style) for cell in row])
    table = Table(wrapped, colWidths=widths, repeatRows=1)
    table.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor(header_bg)),
                ("GRID", (0, 0), (-1, -1), 0.25, colors.HexColor("#D7DDE8")),
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, colors.HexColor("#F7F9FC")]),
                ("LEFTPADDING", (0, 0), (-1, -1), 4),
                ("RIGHTPADDING", (0, 0), (-1, -1), 4),
                ("TOPPADDING", (0, 0), (-1, -1), 4),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
            ]
        )
    )
    return table


def stock_card(row: pd.Series, style_map: dict[str, ParagraphStyle], warrant_flow_date: str) -> KeepTogether:
    title = f"{stock_text(row)}｜{CATEGORY_LABEL.get(safe_str(row.get('category_key')), '')}"
    rows = [
        [title, f"{row['priority_label']}｜{score_rank_text(row)}"],
        ["入選理由", reason_text(row)],
        ["TDCC / 權證", f"{tdcc_signal(row)} / {warrant_signal(row, warrant_flow_date)}"],
        ["財報 / 事件催化", catalyst_brief(row)],
        ["主要風險", risk_text(row, warrant_flow_date)],
        ["明日確認條件", confirm_text(row)],
    ]
    wrapped = []
    for idx, item in enumerate(rows):
        if idx == 0:
            wrapped.append([para(item[0], style_map["curated_cell"]), para(item[1], style_map["curated_cell"])])
        else:
            wrapped.append([para(item[0], style_map["label"]), para(item[1], style_map["curated_cell"])])
    table = Table(wrapped, colWidths=[4.0 * cm, 12.8 * cm])
    table.setStyle(
        TableStyle(
            [
                ("SPAN", (0, 0), (0, 0)),
                ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#EAF2F8")),
                ("GRID", (0, 0), (-1, -1), 0.25, colors.HexColor("#CFD8E3")),
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("LEFTPADDING", (0, 0), (-1, -1), 6),
                ("RIGHTPADDING", (0, 0), (-1, -1), 6),
                ("TOPPADDING", (0, 0), (-1, -1), 5),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
            ]
        )
    )
    return KeepTogether([table, Spacer(1, 0.22 * cm)])


def build_curated_pdf(df: pd.DataFrame, freshness: dict[str, Any], main_date: str, path: Path) -> None:
    style_map = styles()
    path.parent.mkdir(parents=True, exist_ok=True)
    doc = SimpleDocTemplate(
        str(path),
        pagesize=A4,
        leftMargin=1.7 * cm,
        rightMargin=1.7 * cm,
        topMargin=1.4 * cm,
        bottomMargin=1.4 * cm,
    )
    story: list[Any] = []
    report_ready = safe_str(freshness.get("report_ready", ""))
    warrant_flow_date = safe_str(freshness.get("warrant_flow_date", ""))
    conclusion = market_conclusion(df)
    selected = selected_by_category(df)
    watch = top_watchlist(selected)

    story.append(Spacer(1, 1.0 * cm))
    story.append(para("每日全市場候選股監測報告", style_map["title"]))
    story.append(para("精華版 PDF", style_map["subtitle"]))
    story.append(Spacer(1, 0.5 * cm))
    story.append(para(f"主資料日期：{main_date}", style_map["normal"]))
    story.append(para(f"資料狀態：report_ready={report_ready}", style_map["normal"]))
    story.append(para(f"今日市場結論：{conclusion}", style_map["h2"]))
    story.append(Spacer(1, 0.5 * cm))
    story.append(para("本報告由 Daily Full Pipeline 固定格式產生，精華版只放精選標的，完整清單請看完整版表格 PDF。", style_map["normal"]))
    append_context_sections(story, style_map, freshness, [4.2 * cm, 12.8 * cm])
    append_catalyst_section(story, style_map, df)
    story.append(PageBreak())

    story.append(para("今日優先追蹤", style_map["h1"]))
    if watch.empty:
        story.append(para("今日沒有達到優先追蹤條件的標的。", style_map["normal"]))
    else:
        rows = [["分類", "股票", "優先級", "分數 / 排名 / priority", "為什麼先看", "風險與確認"]]
        for _, row in watch.iterrows():
            rows.append(
                [
                    CATEGORY_SHORT.get(safe_str(row.get("category_key")), ""),
                    stock_text(row),
                    row["priority_label"],
                    score_rank_text(row),
                    reason_text(row),
                    f"{risk_text(row, warrant_flow_date)}；{confirm_text(row)}",
                ]
            )
        story.append(
            make_table(
                rows,
                style_map,
                [2.3 * cm, 2.5 * cm, 2.3 * cm, 3.0 * cm, 4.2 * cm, 4.7 * cm],
            )
        )

    story.append(Spacer(1, 0.4 * cm))
    story.append(para("風險提醒", style_map["h1"]))
    story.append(para("權證只作為輔助資金熱度，不能單獨構成追蹤理由；若 TDCC 為 distribution_warning，優先度必須下修。", style_map["normal"]))
    if not warrant_flow_date:
        story.append(para("權證資料不足 / 今日不作為主要判斷。", style_map["normal"]))
    story.append(para("區間轉強與型態觀察都需要隔日價量確認；營收低反應股也要避開已過熱或已反應的標的。", style_map["normal"]))

    story.append(para("明日觀察", style_map["h1"]))
    story.append(para("先看優先追蹤清單是否站穩均線或平台，再看族群是否延續擴散；若量能退潮或 TDCC 轉弱，降低追蹤優先度。", style_map["normal"]))
    story.append(PageBreak())

    story.append(para("分類解讀", style_map["h1"]))
    for cat in CATEGORY_ORDER:
        label = CATEGORY_LABEL[cat]
        story.append(para(label, style_map["h2"]))
        part = selected.get(cat, pd.DataFrame())
        if part.empty:
            story.append(para("本分類今日沒有符合精華版條件的標的。", style_map["normal"]))
            continue
        for _, row in part.iterrows():
            story.append(stock_card(row, style_map, warrant_flow_date))

    doc.build(story)


def sector_matrix(df: pd.DataFrame, warrant_flow_date: str) -> pd.DataFrame:
    rows: list[dict[str, Any]] = []
    for group, part in df.groupby("group_name"):
        record: dict[str, Any] = {"細分族群": group, "總檔數": len(part)}
        resonance = 0
        for cat, label in MATRIX_COLUMNS.items():
            count = int((part["category_key"] == cat).sum())
            record[label] = count
            if count:
                resonance += 1
        tdcc_support = int(part.apply(tdcc_signal, axis=1).isin(["strong_accumulation", "mild_accumulation"]).sum())
        tdcc_weak = int((part.apply(tdcc_signal, axis=1) == "distribution_warning").sum())
        if warrant_flow_date:
            warrant_support = int(part.apply(lambda row: warrant_signal(row, warrant_flow_date) in BULLISH_WARRANT_SIGNALS, axis=1).sum())
        else:
            warrant_support = 0
        has_breakout_mix = record["嚴格突破"] > 0 and record["區間轉強"] > 0
        has_revenue_tdcc = record["營收低反應"] > 0 and tdcc_support > 0
        if tdcc_weak > tdcc_support and (warrant_support > 0 or record["型態觀察"] >= max(1, len(part) // 2)):
            grade = "D"
        elif resonance >= 3 or has_breakout_mix or has_revenue_tdcc:
            grade = "A"
        elif resonance >= 2 or tdcc_support >= 2:
            grade = "B"
        else:
            grade = "C"
        reps = part.sort_values("sort_score", ascending=False).head(3).apply(stock_text, axis=1).tolist()
        record["TDCC支持度"] = f"{tdcc_support}/{len(part)}"
        record["權證支持度"] = f"{warrant_support}/{len(part)}" if warrant_flow_date else "資料不足"
        record["族群等級"] = grade
        record["代表股票"] = "、".join(reps)
        record["族群結論"] = sector_conclusion(grade, resonance, tdcc_support, warrant_support, tdcc_weak)
        record["_sort"] = grade_sort(grade) * 10000 - resonance * 1000 - tdcc_support * 100 - len(part)
        rows.append(record)
    out = pd.DataFrame(rows)
    if out.empty:
        return out
    return out.sort_values(["_sort", "總檔數"]).drop(columns=["_sort"])


def grade_sort(grade: str) -> int:
    return {"A": 0, "B": 1, "C": 2, "D": 3}.get(grade, 9)


def sector_conclusion(grade: str, resonance: int, tdcc_support: int, warrant_support: int, tdcc_weak: int) -> str:
    if grade == "A":
        return "多分類共振，優先觀察延續性。"
    if grade == "B":
        return "有擴散跡象，需等價量確認。"
    if grade == "D":
        return "熱度與支撐不一致，偏保守。"
    if tdcc_support:
        return "零星個股有 TDCC 支持。"
    if warrant_support and tdcc_weak:
        return "權證熱度不可單獨採信。"
    return "零星訊號，先列觀察。"


def full_table_rows(part: pd.DataFrame, warrant_flow_date: str) -> list[list[Any]]:
    rows = [["股票代號", "股票名稱", "分數 / 排名 / priority", "細分族群", "TDCC 判斷", "權證判斷", "催化層", "精簡理由", "降級原因"]]
    for _, row in part.iterrows():
        rows.append(
            [
                safe_str(row.get("stock_id", "")),
                clean_text(row.get("stock_name", ""), 18),
                score_rank_text(row),
                clean_text(row.get("group_name", ""), 24),
                tdcc_signal(row),
                warrant_signal(row, warrant_flow_date),
                catalyst_brief(row),
                reason_text(row),
                downgrade_reason(row),
            ]
        )
    return rows


def build_full_table_pdf(df: pd.DataFrame, freshness: dict[str, Any], main_date: str, path: Path) -> None:
    style_map = styles()
    path.parent.mkdir(parents=True, exist_ok=True)
    doc = SimpleDocTemplate(
        str(path),
        pagesize=landscape(A4),
        leftMargin=0.9 * cm,
        rightMargin=0.9 * cm,
        topMargin=0.8 * cm,
        bottomMargin=0.8 * cm,
    )
    warrant_flow_date = safe_str(freshness.get("warrant_flow_date", ""))
    story: list[Any] = []
    story.append(para("每日全市場候選股監測報告 - 完整版表格 PDF", style_map["title"]))
    story.append(para(f"主資料日期：{main_date}｜report_ready={safe_str(freshness.get('report_ready', ''))}", style_map["subtitle"]))
    story.append(para("族群性分析 / 今日族群輪動", style_map["h1"]))
    story.append(para("族群排序依多分類共振、嚴格突破與區間轉強、營收低反應搭配 TDCC 支持度綜合判斷。", style_map["normal"]))
    append_context_sections(story, style_map, freshness, [5.0 * cm, 21.5 * cm])

    matrix = sector_matrix(df, warrant_flow_date)
    story.append(para("族群矩陣", style_map["h2"]))
    if matrix.empty:
        story.append(para("今日沒有可用族群資料。", style_map["normal"]))
    else:
        matrix_rows = [[col for col in matrix.columns]]
        for _, row in matrix.head(35).iterrows():
            matrix_rows.append([row.get(col, "") for col in matrix.columns])
        story.append(
            make_table(
                matrix_rows,
                style_map,
                [2.7 * cm, 1.3 * cm, 1.2 * cm, 1.2 * cm, 1.4 * cm, 1.3 * cm, 1.3 * cm, 1.3 * cm, 1.6 * cm, 1.6 * cm, 1.1 * cm, 4.0 * cm, 4.2 * cm],
            )
        )

    story.append(PageBreak())
    story.append(para("各分類清單", style_map["h1"]))
    for cat, part in category_groups(df):
        label = CATEGORY_LABEL[cat]
        story.append(para(label, style_map["h2"]))
        if part.empty:
            story.append(para("本分類今日無資料。", style_map["normal"]))
            continue
        chunk_size = 22
        for start in range(0, len(part), chunk_size):
            chunk = part.iloc[start : start + chunk_size]
            story.append(
                make_table(
                    full_table_rows(chunk, warrant_flow_date),
                    style_map,
                    [1.4 * cm, 1.6 * cm, 2.6 * cm, 2.0 * cm, 2.3 * cm, 2.3 * cm, 3.6 * cm, 5.2 * cm, 3.0 * cm],
                )
            )
            story.append(Spacer(1, 0.25 * cm))
    doc.build(story)


def copy_outputs(main_date: str) -> dict[str, str]:
    DOCS_LATEST_DIR.mkdir(parents=True, exist_ok=True)
    HISTORY_REPORT_DIR.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(CURATED_PDF, DOCS_CURATED_PDF)
    shutil.copyfile(FULL_TABLE_PDF, DOCS_FULL_TABLE_PDF)
    history_curated = HISTORY_REPORT_DIR / f"{main_date}_daily_market_curated_report.pdf"
    history_full = HISTORY_REPORT_DIR / f"{main_date}_daily_market_full_table_report.pdf"
    shutil.copyfile(CURATED_PDF, history_curated)
    shutil.copyfile(FULL_TABLE_PDF, history_full)
    return {
        "history_curated_pdf": history_curated.as_posix(),
        "history_full_table_pdf": history_full.as_posix(),
    }


def write_manifest(main_date: str, freshness: dict[str, Any], history_paths: dict[str, str]) -> None:
    manifest = {
        "generated_at": now_text(),
        "main_price_date": main_date,
        "report_ready": safe_str(freshness.get("report_ready", "")),
        "curated_pdf": {
            "status": "generated" if CURATED_PDF.exists() else "missing",
            "file_path": CURATED_PDF.as_posix(),
            "docs_path": DOCS_CURATED_PDF.as_posix(),
            "pages_url": pages_url(DOCS_CURATED_PDF),
            "raw_url": raw_url(CURATED_PDF),
            "history_path": history_paths.get("history_curated_pdf", ""),
        },
        "full_table_pdf": {
            "status": "generated" if FULL_TABLE_PDF.exists() else "missing",
            "file_path": FULL_TABLE_PDF.as_posix(),
            "docs_path": DOCS_FULL_TABLE_PDF.as_posix(),
            "pages_url": pages_url(DOCS_FULL_TABLE_PDF),
            "raw_url": raw_url(FULL_TABLE_PDF),
            "history_path": history_paths.get("history_full_table_pdf", ""),
        },
    }
    MANIFEST_JSON.write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8")
    lines = [
        "# Daily Market Fixed PDF Manifest",
        "",
        f"- generated_at: `{manifest['generated_at']}`",
        f"- main_price_date: `{main_date}`",
        f"- report_ready: `{manifest['report_ready']}`",
        "",
        "## Curated PDF",
        f"- pages_url: {manifest['curated_pdf']['pages_url']}",
        f"- raw_url: {manifest['curated_pdf']['raw_url']}",
        f"- file_path: `{manifest['curated_pdf']['file_path']}`",
        "",
        "## Full Table PDF",
        f"- pages_url: {manifest['full_table_pdf']['pages_url']}",
        f"- raw_url: {manifest['full_table_pdf']['raw_url']}",
        f"- file_path: `{manifest['full_table_pdf']['file_path']}`",
        "",
    ]
    MANIFEST_MD.write_text("\n".join(lines), encoding="utf-8")


def main() -> int:
    LATEST_DIR.mkdir(parents=True, exist_ok=True)
    freshness = load_freshness()
    df = load_candidates()
    main_date = safe_str(freshness.get("main_price_date")) or safe_str(df["date"].max())
    if not main_date:
        main_date = now_taipei().strftime("%Y%m%d")

    build_curated_pdf(df, freshness, main_date, CURATED_PDF)
    build_full_table_pdf(df, freshness, main_date, FULL_TABLE_PDF)
    history_paths = copy_outputs(main_date)
    write_manifest(main_date, freshness, history_paths)

    print(f"Saved: {CURATED_PDF}")
    print(f"Saved: {DOCS_CURATED_PDF}")
    print(f"Saved: {FULL_TABLE_PDF}")
    print(f"Saved: {DOCS_FULL_TABLE_PDF}")
    print(f"Saved: {MANIFEST_JSON}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
