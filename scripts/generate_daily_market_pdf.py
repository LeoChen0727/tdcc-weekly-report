from __future__ import annotations

from datetime import datetime
import importlib.util
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
    Image as PdfImage,
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
VOLUME_BREAKOUT_WATCH_CSV = LATEST_DIR / "volume_breakout_watch_latest.csv"
VOLUME_ATTACK_THEME_STOCKS_CSV = LATEST_DIR / "volume_attack_theme_stocks_latest.csv"
THEME_LEADERSHIP_CSV = LATEST_DIR / "daily_theme_leadership_latest.csv"
TWO_LINE_VIEW_CSV = LATEST_DIR / "daily_candidate_two_line_view_latest.csv"
TDCC_OVERHEATED_EDGE_CSV = LATEST_DIR / "tdcc_overheated_short_term_edge_latest.csv"
TDCC_OVERHEATED_EDGE_CANDIDATES_CSV = LATEST_DIR / "tdcc_overheated_short_term_edge_candidates_latest.csv"
WEEKLY_SURGE_STRICT_SEARCH_CSV = LATEST_DIR / "weekly_surge_strict_parameter_search_latest.csv"
WEEKLY_SURGE_STRICT_CANDIDATES_CSV = LATEST_DIR / "weekly_surge_strict_parameter_candidates_latest.csv"
NON_REVENUE_MOMENTUM_CSV = LATEST_DIR / "non_revenue_momentum_watch_latest.csv"
MARKET_ABNORMAL_STATUS_CSV = LATEST_DIR / "market_abnormal_status_latest.csv"
MODEL_REPORT_SIGNALS_CSV = LATEST_DIR / "daily_candidate_model_signals_for_report_latest.csv"
MODEL_SUMMARY_FOR_REPORT_CSV = LATEST_DIR / "daily_candidate_model_summary_for_report_latest.csv"
TECHNICAL_SNAPSHOT_CSV = LATEST_DIR / "individual_stock_technical_snapshot_latest.csv"
PDF_KLINE_CHART_STATUS_CSV = LATEST_DIR / "pdf_kline_chart_status_latest.csv"
PDF_KLINE_DIR = LATEST_DIR / "charts" / "pdf_kline"
_ARTIFACTS_MODULE: Any | None = None

CURATED_PDF = LATEST_DIR / "daily_market_curated_report_latest.pdf"
FULL_TABLE_PDF = LATEST_DIR / "daily_market_full_table_report_latest.pdf"
MAINSTREAM_CURATED_PDF = LATEST_DIR / "mainstream_daily_recommendation_highlight_latest.pdf"
MAINSTREAM_FULL_PDF = LATEST_DIR / "mainstream_full_candidate_list_latest.pdf"
NON_MAINSTREAM_CURATED_PDF = LATEST_DIR / "non_mainstream_daily_recommendation_highlight_latest.pdf"
NON_MAINSTREAM_FULL_PDF = LATEST_DIR / "non_mainstream_full_candidate_list_latest.pdf"
DOCS_CURATED_PDF = DOCS_LATEST_DIR / CURATED_PDF.name
DOCS_FULL_TABLE_PDF = DOCS_LATEST_DIR / FULL_TABLE_PDF.name
DOCS_MAINSTREAM_CURATED_PDF = DOCS_LATEST_DIR / MAINSTREAM_CURATED_PDF.name
DOCS_MAINSTREAM_FULL_PDF = DOCS_LATEST_DIR / MAINSTREAM_FULL_PDF.name
DOCS_NON_MAINSTREAM_CURATED_PDF = DOCS_LATEST_DIR / NON_MAINSTREAM_CURATED_PDF.name
DOCS_NON_MAINSTREAM_FULL_PDF = DOCS_LATEST_DIR / NON_MAINSTREAM_FULL_PDF.name
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

PDF_TOKEN_ZH = {
    "true_breakout": "嚴格突破",
    "range_rebound": "區間轉強",
    "near_resistance": "接近壓力",
    "abnormal_volume_up": "異常放量上漲",
    "revenue_breakout_low_response": "營收爆發股價尚未反應",
    "revenue_pullback": "營收成長股價回檔",
    "pullback_rebound": "回檔後短線轉強",
    "pattern": "型態觀察",
    "short_term_specialty": "短線專項",
    "volume_breakout": "帶量突破",
    "range_breakout_volume": "帶量突破盤整區間",
    "range_breakout_watch": "接近盤整上緣觀察",
    "ma_reclaim_volume_attack": "帶量站回均線",
    "near_high_volume_watch": "接近前高帶量觀察",
    "strict_high_breakout": "帶量突破波段高點",
    "failed_range_breakout_risk": "盤整區間假突破風險",
    "mainstream": "主流",
    "non_mainstream": "非主流",
    "mainstream_leader": "主流領先族群",
    "mainstream_follow_through": "主流延伸族群",
    "emerging_theme": "新興族群",
    "single_name_signal": "單一個股訊號",
    "weak_theme": "弱族群",
    "mainstream_overheated": "主流過熱",
    "core_mainstream_supported": "核心主流支撐",
    "core_mainstream_theme": "核心主流題材",
    "non_mainstream_theme": "非主流題材",
    "non_mainstream": "非主流",
    "mainstream": "主流",
    "short_term_specialty": "短線專項",
    "range_rebound": "區間轉強",
    "revenue_pullback": "營收成長回檔",
    "revenue_breakout_low_response": "營收爆發股價尚未反應",
    "pullback_rebound": "回檔後短線轉強",
    "true_breakout": "嚴格突破",
    "pattern": "型態觀察",
    "neckline_challenge": "頸線挑戰",
    "neckline_breakout": "頸線突破",
    "platform_breakout": "平台突破",
    "right_side_attack": "右側攻擊",
    "right_side_volume_attack": "右側放量攻擊",
    "range_breakout_volume": "帶量突破盤整區間",
    "range_breakout_watch": "接近盤整上緣觀察",
    "ma_reclaim_volume_attack": "帶量站回均線",
    "near_high_volume_watch": "近高帶量觀察",
    "strict_high_breakout": "帶量突破波段高點",
    "failed_range_breakout_risk": "盤整假突破風險",
    "confirmed_volume_theme": "已確認放量族群",
    "early_mainstream_candidate": "早期主流候選",
    "watch_volume_theme": "放量觀察族群",
    "single_stock_volume_attack": "單股放量攻擊",
    "failed_volume_theme": "放量失敗族群",
    "overheated_volume_theme": "放量過熱族群",
    "strong_accumulation": "大戶強累積",
    "mild_accumulation": "大戶溫和增加",
    "neutral": "中性",
    "distribution_warning": "大戶轉弱警示",
    "call_strong_inflow": "認購強流入",
    "call_inflow": "認購流入",
    "call_put_bullish": "權證偏多",
    "put_inflow": "認售流入",
    "put_strong_inflow": "認售強流入",
    "no_signal": "無明確權證訊號",
    "neckline": "頸線",
    "breakout": "突破",
    "hot_theme_tag": "熱門族群標籤",
    "hot theme tag": "熱門族群標籤",
    "core_mainstream_overheated": "核心主流過熱",
    "non_mainstream_overheated": "非主流過熱",
    "non_mainstream_single_name": "非主流單一個股",
    "non_mainstream_flow_active": "非主流資金流動",
    "continued_2_3d": "連續 2-3 日",
    "continued_many_days": "連續多日",
    "continued_overheated": "連續上榜但過熱",
    "stale_signal": "訊號鈍化",
    "repeated_but_no_breakout": "反覆上榜未突破",
    "first_seen": "首次上榜",
    "A_priority_watch": "A 優先追蹤",
    "B_confirm_needed": "B 等確認",
    "C_watch_only": "C 僅觀察",
    "D_risk_downgrade": "D 風險降級",
    "two_line_overlap": "雙線交集",
    "mainstream_leader_stock": "主流領漲股",
    "mainstream_follow_through_stock": "主流延伸股",
    "emerging_theme_watch": "新興族群觀察",
    "individual_revenue_low_response_watch": "營收低反應觀察",
    "individual_fundamental_catalyst_watch": "基本面催化觀察",
    "individual_tdcc_latent_watch": "TDCC 潛伏觀察",
    "non_mainstream_flow_watch": "非主流資金觀察",
    "individual_single_name_signal": "單一個股訊號",
    "individual_pattern_watch": "型態觀察",
    "individual_quality_watch": "個股條件觀察",
    "individual_watch": "個股觀察",
    "risk": "風險",
}


def display_zh(value: Any, fallback: str = "") -> str:
    text = safe_str(value)
    if not text:
        return fallback
    clean_map = {
        "true_breakout": "嚴格突破",
        "range_rebound": "區間轉強",
        "near_resistance": "接近壓力",
        "abnormal_volume_up": "異常放量上漲",
        "revenue_breakout_low_response": "營收爆發但股價尚未反應",
        "revenue_pullback": "營收成長股價回檔",
        "pullback_rebound": "回檔後短線轉強",
        "pattern": "型態觀察",
        "short_term_specialty": "短線專項",
        "hot_theme_pullback": "熱門族群回檔",
        "volume_breakout": "帶量突破",
        "range_breakout_volume": "帶量突破盤整區間",
        "range_breakout_watch": "接近盤整上緣觀察",
        "ma_reclaim_volume_attack": "帶量站回均線",
        "near_high_volume_watch": "接近前高放量觀察",
        "strict_high_breakout": "帶量突破波段高點",
        "failed_range_breakout_risk": "盤整區間假突破風險",
        "mainstream": "主流",
        "non_mainstream": "非主流",
        "mainstream_leader": "主流領先族群",
        "mainstream_follow_through": "主流延伸族群",
        "emerging_theme": "新興族群",
        "single_name_signal": "單一個股訊號",
        "weak_theme": "弱族群",
        "mainstream_overheated": "主流過熱",
        "strong_accumulation": "大戶強累積",
        "mild_accumulation": "大戶溫和增加",
        "neutral": "中性",
        "distribution_warning": "大戶轉弱警示",
        "call_strong_inflow": "認購強流入",
        "call_inflow": "認購流入",
        "call_put_bullish": "權證偏多",
        "put_inflow": "認售流入",
        "put_strong_inflow": "認售強流入",
        "no_signal": "無明確訊號",
        "neckline": "頸線",
        "breakout": "突破",
        "hot_theme_tag": "熱門族群標籤",
        "hot theme tag": "熱門族群標籤",
        "new_model_signal": "新進榜",
        "repeated_same_model_signal": "重複進榜",
    }
    out = text
    for src in sorted(clean_map, key=len, reverse=True):
        out = out.replace(src, clean_map[src])
    return out or fallback

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


def read_csv_safe(path: Path, **kwargs: Any) -> pd.DataFrame:
    if not path.exists():
        return pd.DataFrame()
    try:
        return pd.read_csv(path, **kwargs)
    except Exception:
        return pd.DataFrame()


def clean_text(text: Any, limit: int | None = None) -> str:
    result = safe_str(text)
    result = result.replace("\n", " ").replace("\r", " ").replace("|", "/")
    result = re.sub(r"\s+", " ", result).strip()
    for old in sorted(FORBIDDEN_WORD_REPLACEMENTS, key=len, reverse=True):
        result = result.replace(old, FORBIDDEN_WORD_REPLACEMENTS[old])
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
    return pdf_text(text).replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


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
    for col in ["score", "rank", "decision_score", "volume_ratio", "return_20d", "return_60d", "return_120d"]:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors="coerce")
    df["category_key"] = df.apply(category_key, axis=1)
    df["group_name"] = df.apply(group_name, axis=1)
    df["priority_label"] = df.apply(priority_label, axis=1)
    df["sort_score"] = df.apply(sort_score, axis=1)
    return df


def load_pdf_kline_chart_map() -> dict[tuple[str, str], Path]:
    """Return K-line chart paths keyed by (stock_id, category), with stock fallback."""
    if not PDF_KLINE_CHART_STATUS_CSV.exists():
        return {}
    try:
        df = pd.read_csv(PDF_KLINE_CHART_STATUS_CSV, dtype=str, keep_default_na=False)
    except Exception:
        return {}
    chart_map: dict[tuple[str, str], Path] = {}
    for _, row in df.iterrows():
        stock_id = safe_str(row.get("stock_id", ""))
        if not stock_id:
            continue
        image_path = Path(safe_str(row.get("image_path", "")))
        if not image_path.exists():
            continue
        category = safe_str(row.get("category", ""))
        if category:
            chart_map[(stock_id, category)] = image_path
        chart_map.setdefault((stock_id, ""), image_path)
    if PDF_KLINE_DIR.exists():
        for image_path in sorted(PDF_KLINE_DIR.glob("*.png")):
            stock_id = image_path.name.split("_", 1)[0]
            if stock_id:
                chart_map.setdefault((stock_id, ""), image_path)
    return chart_map


def chart_path_for_row(row: pd.Series, chart_map: dict[tuple[str, str], Path]) -> Path | None:
    stock_id = safe_str(row.get("stock_id", ""))
    if not stock_id:
        return None
    category = safe_str(row.get("category_key", "")) or safe_str(row.get("category", ""))
    return chart_map.get((stock_id, category)) or chart_map.get((stock_id, ""))


def load_artifacts_module() -> Any | None:
    global _ARTIFACTS_MODULE
    if _ARTIFACTS_MODULE is not None:
        return _ARTIFACTS_MODULE
    artifact_path = Path(__file__).resolve().parents[1] / "build_daily_market_report_artifacts.py"
    if not artifact_path.exists():
        return None
    spec = importlib.util.spec_from_file_location("daily_market_report_artifacts", artifact_path)
    if spec is None or spec.loader is None:
        return None
    artifacts = importlib.util.module_from_spec(spec)
    try:
        spec.loader.exec_module(artifacts)
    except Exception:
        return None
    _ARTIFACTS_MODULE = artifacts
    return artifacts


def redraw_pdf_kline_chart_for_row(row: pd.Series) -> Path | None:
    """Create a K-line chart for curated PDF rows not covered by the artifact chart status."""
    artifacts = load_artifacts_module()
    if artifacts is None:
        return None

    chart_row = row.copy()
    category = safe_str(chart_row.get("category", "")) or safe_str(chart_row.get("category_key", ""))
    if category:
        chart_row["category"] = category
    try:
        price_df, source, _warning = artifacts.select_price_history_for_row(chart_row)
        if price_df.empty:
            return None
        chart_path = artifacts.draw_pdf_kline_chart(chart_row, price_df, source)
    except Exception:
        return None
    return chart_path if chart_path.exists() else None


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


def tdcc_signal_raw(row: pd.Series) -> str:
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


def tdcc_signal(row: pd.Series) -> str:
    return display_zh(tdcc_signal_raw(row))


def warrant_signal_raw(row: pd.Series, warrant_flow_date: str) -> str:
    if not warrant_flow_date:
        return ""
    value = safe_str(row.get("warrant_flow_signal", ""))
    if value:
        return value
    note = clean_text(row.get("warrant_note", ""))
    if note:
        return note
    return "no_signal"


def warrant_signal(row: pd.Series, warrant_flow_date: str) -> str:
    raw = warrant_signal_raw(row, warrant_flow_date)
    if not raw:
        return "權證資料不足 / 今日不作為主要判斷"
    return display_zh(raw)


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
    decision_label = clean_text(row.get("decision_priority_label", ""))
    if decision_label:
        return decision_label
    tdcc = tdcc_signal_raw(row)
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
    decision_priority = clean_text(row.get("decision_priority", ""))
    decision_score = safe_float(row.get("decision_score"), math.nan)
    if decision_priority:
        priority_bonus = {
            "A_priority_watch": 1000,
            "B_confirm_needed": 700,
            "C_watch_only": 350,
            "D_risk_downgrade": 0,
        }.get(decision_priority, 250)
        if math.isnan(decision_score):
            decision_score = 0
        return priority_bonus + decision_score

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
    }.get(tdcc_signal_raw(row), 0)
    score = safe_float(row.get("score"), 0)
    rank = safe_float(row.get("rank"), 9999)
    rank_bonus = max(0, 100 - rank) if not math.isnan(rank) else 0
    volume_bonus = min(safe_float(row.get("volume_ratio"), 0) * 10, 60)
    return priority_bonus + tdcc_bonus + score + rank_bonus + volume_bonus


DECISION_PRIORITY_ORDER = {
    "A_priority_watch": 1,
    "B_confirm_needed": 2,
    "C_watch_only": 3,
    "D_risk_downgrade": 4,
}


WARNING_FLAG_COLUMNS = [
    "why_downgraded",
    "downgrade_flags",
    "risk_tags",
]


WARNING_BOOLEAN_COLUMNS = [
    "must_not_overstate",
    "revenue_good_eps_unconfirmed_flag",
    "continued_overheated",
    "false_breakout_risk",
]


WARNING_TOKENS = [
    "repeated_but_no_breakout",
    "stale_signal",
    "stale_no_warrant_no_breakout",
    "needs_eps_confirmation",
    "revenue_good_eps_unconfirmed",
    "revenue_eps_unconfirmed_no_attack",
    "revenue_no_warrant_stale_no_breakout",
    "tdcc_distribution_warning",
    "distribution_warning",
    "continued_overheated",
    "overheated",
    "false_breakout_risk",
    "must_not_overstate",
]


def decision_priority_order(row: pd.Series) -> int:
    return DECISION_PRIORITY_ORDER.get(clean_text(row.get("decision_priority", "")), 9)


def has_decision_warning(row: pd.Series) -> bool:
    theme_status = clean_text(row.get("theme_final_status", "")).lower()
    theme_mainstream_status = clean_text(row.get("theme_mainstream_status", "")).lower()
    risky_theme_statuses = {
        "mainstream_overheated",
        "weak_theme",
        "failed_volume_theme",
        "overheated_volume_theme",
    }
    if theme_status in risky_theme_statuses or theme_mainstream_status in risky_theme_statuses:
        return True
    for col in WARNING_BOOLEAN_COLUMNS:
        if is_truthy(row.get(col, "")):
            return True
    joined = "|".join(clean_text(row.get(col, ""), 300).lower() for col in WARNING_FLAG_COLUMNS)
    if any(token.lower() in joined for token in WARNING_TOKENS):
        return True
    repeat_label = clean_text(row.get("repeat_appear_label", "")).lower()
    if repeat_label in {"stale_signal", "repeated_but_no_breakout", "continued_overheated"}:
        return True
    if tdcc_signal_raw(row) == "distribution_warning":
        return True
    if overheated(row):
        return True
    return False


def front_priority_eligible(row: pd.Series) -> bool:
    if clean_text(row.get("decision_priority", "")) != "A_priority_watch":
        return False
    if has_decision_warning(row):
        return False
    line_group = clean_text(row.get("candidate_line_group", ""))
    if line_group == "risk":
        return False
    return True


def decision_sort(part: pd.DataFrame) -> pd.DataFrame:
    if part.empty:
        return part
    work = part.copy()
    work["_decision_order"] = work.apply(decision_priority_order, axis=1)
    work["_has_warning"] = work.apply(has_decision_warning, axis=1).astype(int)
    work["_decision_score"] = pd.to_numeric(work.get("decision_score", ""), errors="coerce").fillna(0)
    return work.sort_values(
        ["_decision_order", "_has_warning", "_decision_score", "sort_score"],
        ascending=[True, True, False, False],
    ).drop(columns=["_decision_order", "_has_warning", "_decision_score"], errors="ignore")


def score_rank_text(row: pd.Series) -> str:
    parts: list[str] = []
    decision_score = num_text(row.get("decision_score"), 1)
    score = num_text(row.get("score"), 1)
    rank = num_text(row.get("rank"), 0)
    priority = clean_text(row.get("revaluation_priority", ""))
    if decision_score:
        parts.append(f"decision {decision_score}")
    if score:
        parts.append(f"score {score}")
    if rank:
        parts.append(f"rank {rank}")
    if priority:
        parts.append(priority)
    return " / ".join(parts) if parts else "無分數"


REPEAT_LABEL_TEXT = {
    "first_seen": "首次上榜",
    "continued_2_3d": "連續 2-3 日",
    "continued_many_days": "連續多日",
    "repeated_but_no_breakout": "反覆上榜未突破",
    "continued_overheated": "連續上榜但過熱",
    "stale_signal": "訊號鈍化",
}


def repeat_display(row: pd.Series) -> str:
    label = safe_str(row.get("repeat_appear_label", ""))
    any_days = safe_int(row.get("consecutive_appear_days_any_category", ""))
    if label == "continued_2_3d" and any_days:
        return f"連續 {any_days} 日"
    if label == "continued_many_days" and any_days:
        return f"連續 {any_days} 日"
    if label:
        return REPEAT_LABEL_TEXT.get(label, label)
    return "資料不足"


def repeat_full_text(row: pd.Series) -> str:
    display = repeat_display(row)
    count5 = safe_str(row.get("appear_count_5d", ""))
    count10 = safe_str(row.get("appear_count_10d", ""))
    note = clean_text(row.get("repeat_appear_note", ""), 50)
    parts = [display]
    if count5:
        parts.append(f"5日{count5}")
    if count10:
        parts.append(f"10日{count10}")
    if note:
        parts.append(note)
    return " / ".join(parts)


def stock_text(row: pd.Series) -> str:
    return f"{safe_str(row.get('stock_id', ''))} {clean_text(row.get('stock_name', ''))}".strip()


def reason_text(row: pd.Series) -> str:
    human_reason = clean_text(row.get("why_selected_human_zh", ""), 130)
    if human_reason:
        return display_zh(human_reason)
    decision_reason = clean_text(row.get("why_selected", ""), 130)
    if decision_reason:
        return display_zh(decision_reason)
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
    tdcc = tdcc_signal_raw(row)
    if tdcc in {"strong_accumulation", "mild_accumulation"}:
        parts.append(f"TDCC {display_zh(tdcc)}")
    return display_zh(clean_text("；".join(parts), 130))


def risk_text(row: pd.Series, warrant_flow_date: str) -> str:
    decision_risk = clean_text(row.get("why_downgraded", ""), 120)
    if decision_risk:
        return display_zh(decision_risk)
    risks: list[str] = []
    tdcc = tdcc_signal_raw(row)
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
    return display_zh(clean_text("；".join(risks), 120))


def warning_confirmation_text(row: pd.Series, limit: int = 120) -> str:
    risk = clean_text(row.get("why_downgraded", ""), limit)
    flags = clean_text(row.get("downgrade_flags", ""), limit)
    confirm = clean_text(row.get("next_confirmation", ""), limit)
    parts: list[str] = []
    if risk:
        parts.append(f"風險提醒：{display_zh(risk)}")
    elif flags:
        parts.append(f"風險標籤：{display_zh(flags)}")
    if confirm:
        parts.append(f"下一確認：{display_zh(confirm)}")
    if not parts and has_decision_warning(row):
        parts.append("風險提醒：決策層有風險標籤，不可過度放大為最高優先。")
    return display_zh(clean_text(" / ".join(parts), limit))


def confirm_text(row: pd.Series) -> str:
    decision_confirmation = clean_text(row.get("next_confirmation", ""), 130)
    if decision_confirmation:
        return decision_confirmation
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
    calendar_tags = clean_text(row.get("event_calendar_tags", ""), 60)
    nearest_event = clean_text(row.get("nearest_event_date", ""), 16)
    nearest_event_type = clean_text(row.get("nearest_event_type", ""), 40)
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
    if calendar_tags:
        parts.append(calendar_tags)
    if nearest_event:
        parts.append(f"calendar {nearest_event_type or 'event'} {nearest_event}")
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
    proximity_score = pd.to_numeric(part.get("event_proximity_score", ""), errors="coerce").fillna(0)
    mask = (
        part["_catalyst_score_sort"].gt(0)
        | proximity_score.gt(0)
        | part.get("similar_to_shihsinko_flag", pd.Series("", index=part.index)).astype(str).eq("True")
        | part.get("revenue_good_eps_unconfirmed_flag", pd.Series("", index=part.index)).astype(str).eq("True")
        | part.get("already_reacted_to_catalyst", pd.Series("", index=part.index)).astype(str).eq("True")
    )
    part["_catalyst_score_sort"] = part["_catalyst_score_sort"] + proximity_score
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
        if is_truthy(row.get("already_reacted_to_catalyst", "")) or tdcc_signal_raw(row) == "distribution_warning":
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


def load_theme_leadership() -> pd.DataFrame:
    if not THEME_LEADERSHIP_CSV.exists():
        return pd.DataFrame()
    try:
        return pd.read_csv(THEME_LEADERSHIP_CSV, dtype=str, keep_default_na=False)
    except Exception:
        return pd.DataFrame()


def load_two_line_view() -> pd.DataFrame:
    if not TWO_LINE_VIEW_CSV.exists():
        return pd.DataFrame()
    try:
        return pd.read_csv(TWO_LINE_VIEW_CSV, dtype=str, keep_default_na=False)
    except Exception:
        return pd.DataFrame()


def theme_leadership_rows(theme_df: pd.DataFrame, limit: int = 12) -> list[list[Any]]:
    rows = [[
        "theme",
        "status",
        "structure",
        "count",
        "breakout",
        "volume",
        "near high",
        "TDCC",
        "warrant",
        "overheat",
        "leader",
        "score",
        "interpretation",
    ]]
    if theme_df.empty:
        rows.append(["n/a", "missing", "", "", "", "", "", "", "", "", "", "", "daily_theme_leadership_latest.csv missing"])
        return rows
    view = theme_df.copy()
    for col in ["theme_strength_score", "theme_breadth_score", "theme_risk_score"]:
        if col in view.columns:
            view[col] = pd.to_numeric(view[col], errors="coerce").fillna(0)
    view = view.sort_values(["theme_strength_score", "theme_breadth_score", "theme_risk_score"], ascending=[False, False, True]).head(limit)
    for _, row in view.iterrows():
        status_raw = clean_text(row.get("theme_final_status", ""), 28)
        status = status_raw
        if status == "mainstream_leader":
            note = "主流領漲；優先看兩條線交集股"
        elif status == "mainstream_follow_through":
            note = "主流延伸；適合找補漲與轉強確認"
        elif status == "emerging_theme":
            note = "新興擴散；等第二/第三檔確認"
        elif status == "single_name_signal":
            note = "單一個股訊號；放個股條件線"
        elif status == "mainstream_overheated":
            note = "主流但過熱；避免追高"
        else:
            note = "弱族群或零散訊號"
        rows.append(
            [
                clean_text(row.get("theme_name", ""), 18),
                status,
                clean_text(row.get("theme_structural_status", ""), 18),
                safe_str(row.get("theme_candidate_count", "")),
                safe_str(row.get("theme_true_breakout_count", "")),
                safe_str(row.get("theme_volume_breakout_count", "")),
                safe_str(row.get("theme_near_high_count", "")),
                f"{safe_str(row.get('theme_tdcc_strong_count', ''))}/{safe_str(row.get('theme_tdcc_mild_count', ''))}",
                safe_str(row.get("theme_warrant_bullish_count", "")),
                safe_str(row.get("theme_overheated_count", "")),
                f"{safe_str(row.get('theme_leader_stock_id', ''))} {clean_text(row.get('theme_leader_stock_name', ''), 10)}",
                safe_str(row.get("theme_strength_score", "")),
                note,
            ]
        )
    return rows


def two_line_rows(two_line: pd.DataFrame, groups: set[str], limit: int = 12) -> list[list[Any]]:
    rows = [["股票", "分類", "族群", "結構", "報告線", "優先級", "分數", "TDCC", "權證", "連續", "備註"]]
    if two_line.empty:
        rows.append(["無資料", "", "", "", "", "", "", "", "", "", "雙線候選表缺失"])
        return rows
    part = two_line[two_line["candidate_line_group"].isin(groups)].copy()
    if part.empty:
        rows.append(["無資料", "", "", "", "", "", "", "", "", "", "本區無符合資料"])
        return rows
    part["_priority_order"] = part["decision_priority"].map(DECISION_PRIORITY_ORDER).fillna(9)
    part["_has_warning"] = part.apply(has_decision_warning, axis=1).astype(int)
    part["_score"] = pd.to_numeric(part.get("decision_score", ""), errors="coerce").fillna(0)
    part = part.sort_values(["_priority_order", "_has_warning", "_score"], ascending=[True, True, False]).head(limit)
    for _, row in part.iterrows():
        note = warning_confirmation_text(row, 85) or clean_text(row.get("theme_leadership_note", ""), 85)
        rows.append(
            [
                f"{safe_str(row.get('stock_id', ''))} {clean_text(row.get('stock_name', ''), 10)}",
                clean_text(display_zh(row.get("category", "")), 18),
                f"{clean_text(display_zh(row.get('theme_name', '')), 14)} / {clean_text(display_zh(row.get('theme_final_status', '')), 24)}",
                clean_text(display_zh(row.get("theme_structural_status", "")), 20),
                clean_text(display_zh(row.get("candidate_line", "")), 20),
                clean_text(display_zh(row.get("decision_priority", "")), 20),
                safe_str(row.get("decision_score", "")),
                clean_text(display_zh(row.get("tdcc_status", "")), 20),
                clean_text(display_zh(row.get("warrant_flow_signal", "")), 18),
                clean_text(display_zh(row.get("repeat_appear_label", "")), 18),
                clean_text(display_zh(row.get("theme_mainstream_label", "")), 32) or note,
            ]
        )
    return rows


def append_theme_leadership_sections(
    story: list[Any],
    style_map: dict[str, ParagraphStyle],
    compact: bool = True,
) -> None:
    theme_df = load_theme_leadership()
    two_line = load_two_line_view()
    story.append(para("主流族群矩陣 / 兩條線分流", style_map["h1"]))
    story.append(
        para(
            "主流資金線與個股條件線並存，報告固定分線呈現。雙重確認股代表同時有族群支持與個股條件；潛伏觀察股仍可追蹤，但不能放在主流資金線前段。",
            style_map["normal"],
        )
    )
    theme_limit = 8 if compact else 18
    story.append(para("今日主流族群矩陣", style_map["h2"]))
    story.append(
        make_table(
            theme_leadership_rows(theme_df, limit=theme_limit),
            style_map,
            [1.4 * cm, 1.7 * cm, 1.8 * cm, 0.6 * cm, 0.7 * cm, 0.7 * cm, 0.7 * cm, 0.7 * cm, 0.6 * cm, 0.6 * cm, 1.6 * cm, 0.7 * cm, 3.8 * cm],
            header_bg="#375623",
        )
    )
    story.append(Spacer(1, 0.25 * cm))
    story.append(para("雙重確認優先股", style_map["h2"]))
    story.append(
        make_table(
            two_line_rows(two_line, {"two_line_overlap"}, limit=8 if compact else 20),
            style_map,
            [1.5 * cm, 1.4 * cm, 2.1 * cm, 1.6 * cm, 1.7 * cm, 1.3 * cm, 0.6 * cm, 1.1 * cm, 1.0 * cm, 1.0 * cm, 2.9 * cm],
            header_bg="#1F4E79",
        )
    )
    story.append(Spacer(1, 0.25 * cm))
    story.append(para("主流資金股", style_map["h2"]))
    story.append(
        make_table(
            two_line_rows(two_line, {"mainstream_leader_stock", "mainstream_follow_through_stock", "emerging_theme_watch"}, limit=10 if compact else 30),
            style_map,
            [1.5 * cm, 1.4 * cm, 2.1 * cm, 1.6 * cm, 1.7 * cm, 1.3 * cm, 0.6 * cm, 1.1 * cm, 1.0 * cm, 1.0 * cm, 2.9 * cm],
            header_bg="#2F5597",
        )
    )
    story.append(Spacer(1, 0.25 * cm))
    story.append(para("個股條件股 / 潛伏觀察股", style_map["h2"]))
    story.append(
        make_table(
            two_line_rows(
                two_line,
                {
                    "individual_revenue_low_response_watch",
                    "individual_fundamental_catalyst_watch",
                    "individual_tdcc_latent_watch",
                    "non_mainstream_flow_watch",
                    "individual_single_name_signal",
                    "individual_pattern_watch",
                    "individual_quality_watch",
                    "individual_watch",
                },
                limit=10 if compact else 35,
            ),
            style_map,
            [1.5 * cm, 1.4 * cm, 2.1 * cm, 1.6 * cm, 1.7 * cm, 1.3 * cm, 0.6 * cm, 1.1 * cm, 1.0 * cm, 1.0 * cm, 2.9 * cm],
            header_bg="#7F6000",
        )
    )
    story.append(Spacer(1, 0.25 * cm))
    story.append(para("降級 / 鈍化 / 風險清單", style_map["h2"]))
    story.append(
        make_table(
            two_line_rows(two_line, {"risk"}, limit=8 if compact else 25),
            style_map,
            [1.5 * cm, 1.4 * cm, 2.1 * cm, 1.6 * cm, 1.7 * cm, 1.3 * cm, 0.6 * cm, 1.1 * cm, 1.0 * cm, 1.0 * cm, 2.9 * cm],
            header_bg="#7F1D1D",
        )
    )
    story.append(Spacer(1, 0.35 * cm))


def load_tdcc_overheated_edge_stats() -> pd.DataFrame:
    if not TDCC_OVERHEATED_EDGE_CSV.exists():
        return pd.DataFrame()
    try:
        return pd.read_csv(TDCC_OVERHEATED_EDGE_CSV, dtype=str, keep_default_na=False)
    except Exception:
        return pd.DataFrame()


def load_tdcc_overheated_edge_candidates() -> pd.DataFrame:
    if not TDCC_OVERHEATED_EDGE_CANDIDATES_CSV.exists():
        return pd.DataFrame()
    try:
        return pd.read_csv(TDCC_OVERHEATED_EDGE_CANDIDATES_CSV, dtype=str, keep_default_na=False)
    except Exception:
        return pd.DataFrame()


def tdcc_edge_stats_rows(stats: pd.DataFrame, horizon: str) -> list[list[Any]]:
    rows = [[
        "rule",
        "mature",
        "win C-C",
        "avg C-C",
        "median C-C",
        "avg rel",
        "win next-open",
        "avg next-open rel",
        "status",
    ]]
    if stats.empty:
        rows.append(["n/a", "", "", "", "", "", "", "", "tdcc_overheated_short_term_edge_latest.csv missing"])
        return rows
    if "horizon" not in stats.columns:
        rows.append(["n/a", "", "", "", "", "", "", "", f"{horizon} horizon column missing"])
        return rows
    part = stats[stats["horizon"].astype(str).eq(horizon)].copy()
    if part.empty:
        rows.append(["n/a", "", "", "", "", "", "", "", f"{horizon} rows missing"])
        return rows
    for _, row in part.iterrows():
        rows.append(
            [
                clean_text(row.get("rule_name_zh", row.get("rule_name", "")), 42),
                safe_str(row.get("mature_count", "")),
                pct_text(row.get("win_rate_close_to_close_pct", "")),
                pct_text(row.get("avg_return_close_to_close_pct", "")),
                pct_text(row.get("median_return_close_to_close_pct", "")),
                pct_text(row.get("avg_relative_return_vs_benchmark_pct", "")),
                pct_text(row.get("win_rate_next_open_to_close_pct", "")),
                pct_text(row.get("avg_next_open_relative_return_vs_benchmark_pct", "")),
                clean_text(row.get("sample_status", ""), 20),
            ]
        )
    return rows


def tdcc_edge_candidate_rows(candidates: pd.DataFrame, limit: int = 12) -> list[list[Any]]:
    rows = [[
        "stock",
        "theme",
        "rule",
        "1w",
        "2w",
        "D+5 win/rel",
        "D+10 win/rel",
        "note",
    ]]
    if candidates.empty:
        rows.append(["n/a", "", "", "", "", "", "", "No current stocks matched this TDCC overheated specialty."])
        return rows
    view = candidates.copy()
    for col in ["d10_win_rate_pct", "d5_win_rate_pct", "price_ret_2w"]:
        if col in view.columns:
            view[col] = pd.to_numeric(view[col], errors="coerce").fillna(0)
    view = view.sort_values(["d10_win_rate_pct", "d5_win_rate_pct", "price_ret_2w"], ascending=[False, False, False]).head(limit)
    for _, row in view.iterrows():
        rows.append(
            [
                f"{safe_str(row.get('stock_id', ''))} {clean_text(row.get('stock_name', ''), 10)}",
                clean_text(row.get("theme", ""), 14),
                clean_text(row.get("rule_name_zh", row.get("rule_id", "")), 34),
                pct_text(row.get("price_ret_1w", "")),
                pct_text(row.get("price_ret_2w", "")),
                f"{pct_text(row.get('d5_win_rate_pct', ''))}/{pct_text(row.get('d5_avg_relative_return_pct', ''))}",
                f"{pct_text(row.get('d10_win_rate_pct', ''))}/{pct_text(row.get('d10_avg_relative_return_pct', ''))}",
                "reporting-only; more regimes needed",
            ]
        )
    return rows


def append_tdcc_overheated_edge_section(
    story: list[Any],
    style_map: dict[str, ParagraphStyle],
    compact: bool = True,
) -> None:
    stats = load_tdcc_overheated_edge_stats()
    candidates = load_tdcc_overheated_edge_candidates()
    story.append(para("TDCC 過熱短線勝率專項（D+5 / D+10）", style_map["h1"]))
    story.append(
        para(
            "此段是獨立 reporting-only 專項，不混入六大分類核心排序，也不調整 TDCC/ABM 核心權重。勝率以 mature_dN=True 後，訊號日收盤到 D+N 收盤報酬 > 0 計算；next-open 欄位另以隔日開盤到 D+N 收盤計算。",
            style_map["normal"],
        )
    )
    story.append(para("目前符合專項條件個股", style_map["h2"]))
    story.append(
        make_table(
            tdcc_edge_candidate_rows(candidates, limit=8 if compact else 20),
            style_map,
            [1.8 * cm, 1.6 * cm, 4.1 * cm, 0.8 * cm, 0.8 * cm, 1.4 * cm, 1.5 * cm, 3.2 * cm],
            header_bg="#984807",
        )
    )
    story.append(Spacer(1, 0.22 * cm))
    story.append(para("D+5 回測表", style_map["h2"]))
    story.append(
        make_table(
            tdcc_edge_stats_rows(stats, "D+5"),
            style_map,
            [4.3 * cm, 0.9 * cm, 1.1 * cm, 1.0 * cm, 1.1 * cm, 1.0 * cm, 1.3 * cm, 1.5 * cm, 1.5 * cm],
            header_bg="#7030A0",
        )
    )
    story.append(Spacer(1, 0.22 * cm))
    story.append(para("D+10 回測表", style_map["h2"]))
    story.append(
        make_table(
            tdcc_edge_stats_rows(stats, "D+10"),
            style_map,
            [4.3 * cm, 0.9 * cm, 1.1 * cm, 1.0 * cm, 1.1 * cm, 1.0 * cm, 1.3 * cm, 1.5 * cm, 1.5 * cm],
            header_bg="#5B9BD5",
        )
    )
    story.append(Spacer(1, 0.35 * cm))


def load_weekly_surge_strict_search() -> pd.DataFrame:
    if not WEEKLY_SURGE_STRICT_SEARCH_CSV.exists():
        return pd.DataFrame()
    try:
        return pd.read_csv(WEEKLY_SURGE_STRICT_SEARCH_CSV, dtype=str, keep_default_na=False)
    except Exception:
        return pd.DataFrame()


def load_weekly_surge_strict_candidates() -> pd.DataFrame:
    if not WEEKLY_SURGE_STRICT_CANDIDATES_CSV.exists():
        return pd.DataFrame()
    try:
        return pd.read_csv(WEEKLY_SURGE_STRICT_CANDIDATES_CSV, dtype=str, keep_default_na=False)
    except Exception:
        return pd.DataFrame()


def weekly_surge_strict_stats_rows(stats: pd.DataFrame, horizon: str, limit: int = 10) -> list[list[Any]]:
    rows = [[
        "rule",
        "samples",
        "close win",
        "avg close ret",
        "avg loss",
        "worst close",
        "median low",
        "worst low",
        "+10% touch",
        "status",
    ]]
    if stats.empty:
        rows.append(["n/a", "", "", "", "", "", "next-open +10% touch research missing"])
        return rows
    part = stats[stats.get("target_window", pd.Series(dtype=str)).astype(str).eq(horizon)].copy()
    if part.empty:
        rows.append(["n/a", "", "", "", "", "", f"{horizon} rows missing"])
        return rows
    for col in [
        "selected_stock_days",
        "hit_rate_pct",
        "win_rate_next_open_to_close_pct",
        "avg_next_open_to_close_return_pct",
        "median_next_open_to_high_return_pct",
        "avg_loss_next_open_to_close_return_pct",
        "worst_loss_next_open_to_close_return_pct",
        "median_next_open_to_low_return_pct",
        "worst_next_open_to_low_return_pct",
        "avg_signal_close_to_next_open_gap_pct",
        "coverage_of_all_hits_pct",
    ]:
        part[col] = pd.to_numeric(part.get(col), errors="coerce")
    part = part[part["selected_stock_days"] >= 100]
    part = part.sort_values(["hit_rate_pct", "selected_stock_days"], ascending=[False, False]).head(limit)
    if part.empty:
        rows.append(["n/a", "", "", "", "", "", "no rule has selected_stock_days >= 100"])
        return rows
    for _, row in part.iterrows():
        rows.append(
            [
                clean_text(row.get("rule_name", ""), 52),
                safe_str(row.get("selected_stock_days", "")),
                pct_text(row.get("win_rate_next_open_to_close_pct", "")),
                pct_text(row.get("avg_next_open_to_close_return_pct", "")),
                pct_text(row.get("avg_loss_next_open_to_close_return_pct", "")),
                pct_text(row.get("worst_loss_next_open_to_close_return_pct", "")),
                pct_text(row.get("median_next_open_to_low_return_pct", "")),
                pct_text(row.get("worst_next_open_to_low_return_pct", "")),
                pct_text(row.get("hit_rate_pct", "")),
                clean_text(row.get("sample_status", ""), 20),
            ]
        )
    return rows


def weekly_surge_horizon_summary_rows(stats: pd.DataFrame) -> list[list[Any]]:
    rows = [["horizon", "selected", "close win", "avg close", "median close", "median low", "+10% touch", "best rule"]]
    if stats.empty:
        rows.append(["n/a", "", "", "", "", "next-open +10% touch research missing"])
        return rows
    for day in range(1, 11):
        horizon = f"D+{day}"
        part = stats[stats.get("target_window", pd.Series(dtype=str)).astype(str).eq(horizon)].copy()
        if part.empty:
            rows.append([horizon, "", "", "", "", "rows missing"])
            continue
        for col in [
            "selected_stock_days",
            "hit_rate_pct",
            "median_next_open_to_high_return_pct",
            "win_rate_next_open_to_close_pct",
            "avg_next_open_to_close_return_pct",
            "median_next_open_to_close_return_pct",
            "median_next_open_to_low_return_pct",
            "avg_signal_close_to_next_open_gap_pct",
        ]:
            part[col] = pd.to_numeric(part.get(col), errors="coerce")
        part = part[part["selected_stock_days"] >= 100].sort_values(
            ["win_rate_next_open_to_close_pct", "avg_next_open_to_close_return_pct", "selected_stock_days"],
            ascending=[False, False, False],
        )
        if part.empty:
            rows.append([horizon, "", "", "", "", "no rule has selected_stock_days >= 100"])
            continue
        row = part.iloc[0]
        rows.append(
            [
                horizon,
                safe_str(row.get("selected_stock_days", "")),
                pct_text(row.get("win_rate_next_open_to_close_pct", "")),
                pct_text(row.get("avg_next_open_to_close_return_pct", "")),
                pct_text(row.get("median_next_open_to_close_return_pct", "")),
                pct_text(row.get("median_next_open_to_low_return_pct", "")),
                pct_text(row.get("hit_rate_pct", "")),
                clean_text(row.get("rule_name", ""), 52),
            ]
        )
    return rows


def weekly_surge_strict_candidate_rows(candidates: pd.DataFrame, limit: int = 15) -> list[list[Any]]:
    rows = [[
        "stock",
        "priority",
        "vol5x",
        "10d ret",
        "abnormal",
        "D+5 hit",
        "D+10 hit",
        "rule / execution risk",
    ]]
    if candidates.empty:
        rows.append(["n/a", "", "", "", "", "", "", "No current next-open +10% touch candidates."])
        return rows
    view = candidates.copy()
    for col in ["best_d10_hit_rate_pct", "best_d5_hit_rate_pct", "start_5d_avg_volume_ratio_vs_prev20"]:
        if col in view.columns:
            view[col] = pd.to_numeric(view[col], errors="coerce").fillna(0)
    view = view.sort_values(["research_priority", "best_d10_hit_rate_pct", "best_d5_hit_rate_pct"], ascending=[True, False, False]).head(limit)
    for _, row in view.iterrows():
        rows.append(
            [
                f"{safe_str(row.get('stock_id', ''))} {clean_text(row.get('stock_name', ''), 10)}",
                clean_text(row.get("research_priority", ""), 24),
                num_text(row.get("start_5d_avg_volume_ratio_vs_prev20", ""), 2),
                pct_text(row.get("return_10d_pct", "")),
                clean_text(row.get("market_abnormal_status", "normal"), 20),
                pct_text(row.get("best_d5_hit_rate_pct", "")),
                pct_text(row.get("best_d10_hit_rate_pct", "")),
                clean_text("; ".join(x for x in [safe_str(row.get("best_d10_rule", "")), safe_str(row.get("execution_risk_note", ""))] if x), 72),
            ]
        )
    return rows


def append_weekly_surge_strict_section(
    story: list[Any],
    style_map: dict[str, ParagraphStyle],
    compact: bool = True,
) -> None:
    stats = load_weekly_surge_strict_search()
    candidates = load_weekly_surge_strict_candidates()
    story.append(para("Next-Open +10% Touch Specialty (D+1-D+10)", style_map["h1"]))
    story.append(
        para(
            "Research-only section. This is not a weekly candlestick signal. Entry basis is next trading day open after the signal-day close. A hit means the high from next open to D+N reaches +10%; it is a touch-rate, not D+N close-to-close win rate. Close-return and intraperiod low columns are shown separately to avoid overstating this signal. This table uses no latest theme label and must not be mixed into the core six-category ranking.",
            style_map["normal"],
        )
    )
    story.append(
        para(
            "Execution-risk note: disposition / attention / periodic-trading flags come from official TWSE/TPEx abnormal-status feeds. Historical backtest rows are not retroactively filtered until enough daily snapshots or verified historical sources are available.",
            style_map["small"],
        )
    )
    story.append(para("Current Strict Research Candidates", style_map["h2"]))
    story.append(
        make_table(
            weekly_surge_strict_candidate_rows(candidates, limit=8 if compact else 25),
            style_map,
            [2.1 * cm, 2.4 * cm, 0.9 * cm, 1.0 * cm, 0.9 * cm, 1.0 * cm, 1.1 * cm, 5.2 * cm],
            header_bg="#1F4E79",
        )
    )
    story.append(Spacer(1, 0.22 * cm))
    story.append(para("D+1 to D+10 Horizon Summary", style_map["h2"]))
    story.append(
        make_table(
            weekly_surge_horizon_summary_rows(stats),
            style_map,
            [0.9 * cm, 0.9 * cm, 1.0 * cm, 1.1 * cm, 1.1 * cm, 1.1 * cm, 1.0 * cm, 6.3 * cm],
            header_bg="#7030A0",
        )
    )
    story.append(Spacer(1, 0.22 * cm))
    story.append(para("D+5 Close-Exit / High-Touch Detail", style_map["h2"]))
    story.append(
        make_table(
            weekly_surge_strict_stats_rows(stats, "D+5", limit=6 if compact else 12),
            style_map,
            [3.5 * cm, 0.75 * cm, 0.9 * cm, 0.9 * cm, 0.9 * cm, 0.9 * cm, 0.9 * cm, 0.9 * cm, 0.9 * cm, 1.2 * cm],
            header_bg="#375623",
        )
    )
    story.append(Spacer(1, 0.22 * cm))
    story.append(para("D+10 Close-Exit / High-Touch Detail", style_map["h2"]))
    story.append(
        make_table(
            weekly_surge_strict_stats_rows(stats, "D+10", limit=6 if compact else 12),
            style_map,
            [3.5 * cm, 0.75 * cm, 0.9 * cm, 0.9 * cm, 0.9 * cm, 0.9 * cm, 0.9 * cm, 0.9 * cm, 0.9 * cm, 1.2 * cm],
            header_bg="#5B9BD5",
        )
    )
    story.append(Spacer(1, 0.35 * cm))


def load_non_revenue_momentum() -> pd.DataFrame:
    if not NON_REVENUE_MOMENTUM_CSV.exists():
        return pd.DataFrame()
    try:
        return pd.read_csv(NON_REVENUE_MOMENTUM_CSV, dtype=str, keep_default_na=False)
    except Exception:
        return pd.DataFrame()


def non_revenue_momentum_rows(df: pd.DataFrame, limit: int = 12) -> list[list[Any]]:
    rows = [[
        "stock",
        "type",
        "theme",
        "revenue",
        "theme status",
        "volume",
        "TDCC/warrant",
        "next confirmation",
    ]]
    if df.empty:
        rows.append(["n/a", "", "", "", "", "", "", "non_revenue_momentum_watch_latest.csv missing or empty"])
        return rows
    view = df.copy()
    for col in ["non_revenue_momentum_type", "decision_score"]:
        if col not in view.columns:
            view[col] = ""
    order = {
        "A_fund_flow_confirmed_revenue_unconfirmed": 1,
        "B_turnaround_theme_watch": 2,
        "C_hot_money_watch": 3,
        "D_overheated_or_failed_risk": 4,
    }
    view["_order"] = view["non_revenue_momentum_type"].map(order).fillna(99)
    view["_score"] = pd.to_numeric(view["decision_score"], errors="coerce").fillna(-999)
    view = view.sort_values(["_order", "_score"], ascending=[True, False]).head(limit)
    for _, row in view.iterrows():
        rows.append(
            [
                f"{safe_str(row.get('stock_id', ''))} {clean_text(row.get('stock_name', ''), 10)}",
                clean_text(display_zh(row.get("non_revenue_momentum_type", "")), 28),
                clean_text(display_zh(row.get("theme_name", "")), 14),
                clean_text(display_zh(row.get("revenue_confirmation_status", "")), 22),
                clean_text(display_zh(safe_str(row.get("theme_final_status", "")) or safe_str(row.get("theme_volume_attack_status", ""))), 24),
                f"{clean_text(display_zh(row.get('volume_breakout_type', '')), 24)} / {num_text(row.get('volume_ratio', ''), 1)}x",
                f"{clean_text(display_zh(row.get('tdcc_status', '')), 18)} / {clean_text(display_zh(row.get('warrant_flow_signal', '')), 18)}",
                clean_text(display_zh(row.get("next_confirmation", "")), 68),
            ]
        )
    return rows


def append_non_revenue_momentum_section(
    story: list[Any],
    style_map: dict[str, ParagraphStyle],
    compact: bool = True,
) -> None:
    df = load_non_revenue_momentum()
    story.append(para("非營收驅動強勢股 / 題材資金先行", style_map["h1"]))
    story.append(
        para(
            "This is a standalone specialty overlay for stocks where price, theme, volume, TDCC, or warrant flow moves before revenue/EPS confirmation. It is not a seventh core category and must not change core model weights.",
            style_map["normal"],
        )
    )
    story.append(
        make_table(
            non_revenue_momentum_rows(df, limit=8 if compact else 30),
            style_map,
            [1.8 * cm, 3.0 * cm, 1.5 * cm, 2.0 * cm, 2.1 * cm, 2.1 * cm, 2.0 * cm, 4.4 * cm],
            header_bg="#7F6000",
        )
    )
    story.append(Spacer(1, 0.35 * cm))


def downgrade_reason(row: pd.Series) -> str:
    decision_risk = clean_text(row.get("why_downgraded", ""), 110)
    if decision_risk:
        return decision_risk
    flags = clean_text(row.get("downgrade_flags", ""), 80)
    if flags:
        return flags
    items: list[str] = []
    if tdcc_signal_raw(row) == "distribution_warning":
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
        part = decision_sort(part)
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


def selected_by_category(df: pd.DataFrame, limit_default: int = 5) -> dict[str, pd.DataFrame]:
    """Select category rows by decision layer first; score only sorts inside the layer."""
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
                (part["decision_priority"].isin(["A_priority_watch", "B_confirm_needed"]))
                & (~part.apply(has_decision_warning, axis=1))
                & (part.apply(tdcc_signal, axis=1).isin(["strong_accumulation", "mild_accumulation"]))
            ].copy()
            if preferred.empty:
                preferred = part[part["decision_priority"] != "D_risk_downgrade"].copy()
            part = preferred if not preferred.empty else part
        else:
            usable = part[part["decision_priority"] != "D_risk_downgrade"].copy()
            if not usable.empty:
                part = usable
        result[cat] = decision_sort(part).head(limits.get(cat, limit_default)).copy()
    return result


def top_watchlist(selected: dict[str, pd.DataFrame]) -> pd.DataFrame:
    """Front priority list must not promote B/C or warning-capped rows by raw score."""
    pieces = []
    for cat in CATEGORY_ORDER:
        part = selected.get(cat, pd.DataFrame()).copy()
        if part.empty:
            continue
        part = part[part.apply(front_priority_eligible, axis=1)].copy()
        if not part.empty:
            pieces.append(part.head(2))
    if not pieces:
        return pd.DataFrame()
    out = pd.concat(pieces, ignore_index=True)
    return decision_sort(out).head(10)


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


def stock_card(
    row: pd.Series,
    style_map: dict[str, ParagraphStyle],
    warrant_flow_date: str,
    chart_map: dict[tuple[str, str], Path] | None = None,
) -> KeepTogether:
    title = f"{stock_text(row)}｜{CATEGORY_LABEL.get(safe_str(row.get('category_key')), '')}"
    rows = [
        [title, f"{row['priority_label']}｜{score_rank_text(row)}"],
        ["入選理由", reason_text(row)],
        ["TDCC / 權證", f"{tdcc_signal(row)} / {warrant_signal(row, warrant_flow_date)}"],
        ["連續上榜", repeat_full_text(row)],
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
    parts: list[Any] = [table]
    chart_path = chart_path_for_row(row, chart_map or {})
    if chart_path is None:
        chart_path = redraw_pdf_kline_chart_for_row(row)
    if chart_path is not None:
        parts.extend(
            [
                Spacer(1, 0.12 * cm),
                PdfImage(str(chart_path), width=16.6 * cm, height=8.2 * cm),
                Spacer(1, 0.22 * cm),
            ]
        )
    else:
        parts.append(Spacer(1, 0.22 * cm))
    return KeepTogether(parts)


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
    chart_map = load_pdf_kline_chart_map()

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
    append_theme_leadership_sections(story, style_map, compact=True)
    append_tdcc_overheated_edge_section(story, style_map, compact=True)
    append_weekly_surge_strict_section(story, style_map, compact=True)
    append_non_revenue_momentum_section(story, style_map, compact=True)

    story.append(PageBreak())

    story.append(para("今日優先追蹤", style_map["h1"]))
    if watch.empty:
        story.append(para("今日沒有達到優先追蹤條件的標的。", style_map["normal"]))
    else:
        rows = [["分類", "股票", "優先級", "連續上榜", "分數 / 排名 / priority", "為什麼先看", "風險與確認"]]
        for _, row in watch.iterrows():
            rows.append(
                [
                    CATEGORY_SHORT.get(safe_str(row.get("category_key")), ""),
                    stock_text(row),
                    row["priority_label"],
                    repeat_display(row),
                    score_rank_text(row),
                    reason_text(row),
                    f"{risk_text(row, warrant_flow_date)}；{confirm_text(row)}",
                ]
            )
        story.append(
            make_table(
                rows,
                style_map,
                [2.0 * cm, 2.4 * cm, 2.1 * cm, 2.1 * cm, 2.7 * cm, 3.7 * cm, 4.2 * cm],
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
            story.append(stock_card(row, style_map, warrant_flow_date, chart_map))

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
        tdcc_support = int(part.apply(tdcc_signal_raw, axis=1).isin(["strong_accumulation", "mild_accumulation"]).sum())
        tdcc_weak = int((part.apply(tdcc_signal_raw, axis=1) == "distribution_warning").sum())
        if warrant_flow_date:
            warrant_support = int(part.apply(lambda row: warrant_signal_raw(row, warrant_flow_date) in BULLISH_WARRANT_SIGNALS, axis=1).sum())
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
    rows = [["股票代號", "股票名稱", "分數 / 排名 / priority", "連續上榜", "近5日上榜", "近10日上榜", "多分類共振", "細分族群", "TDCC 判斷", "權證判斷", "催化層", "精簡理由", "降級原因"]]
    for _, row in part.iterrows():
        rows.append(
            [
                safe_str(row.get("stock_id", "")),
                clean_text(row.get("stock_name", ""), 18),
                score_rank_text(row),
                repeat_display(row),
                safe_str(row.get("appear_count_5d", "")),
                safe_str(row.get("appear_count_10d", "")),
                clean_text(display_zh(row.get("multi_category_flags", "")), 24),
                clean_text(display_zh(row.get("group_name", "")), 24),
                tdcc_signal(row),
                warrant_signal(row, warrant_flow_date),
                display_zh(catalyst_brief(row)),
                display_zh(reason_text(row)),
                display_zh(downgrade_reason(row)),
            ]
        )
    return rows


def load_volume_breakout_watch() -> pd.DataFrame:
    source = VOLUME_ATTACK_THEME_STOCKS_CSV if VOLUME_ATTACK_THEME_STOCKS_CSV.exists() else VOLUME_BREAKOUT_WATCH_CSV
    if not source.exists():
        return pd.DataFrame()
    try:
        df = pd.read_csv(source, dtype=str, keep_default_na=False)
    except Exception:
        return pd.DataFrame()
    if df.empty:
        return df
    if "volume_breakout_rank" in df.columns:
        df["_rank"] = pd.to_numeric(df["volume_breakout_rank"], errors="coerce")
        df = df.sort_values("_rank").drop(columns=["_rank"])
    return df


def volume_breakout_table_rows(part: pd.DataFrame) -> list[list[Any]]:
    rows = [[
        "代號",
        "股票",
        "族群",
        "族群狀態",
        "放量族群狀態",
        "放量型態",
        "優先級",
        "分流分類",
        "TDCC",
        "量比",
        "5日",
        "20日",
        "下一確認",
    ]]
    for _, row in part.iterrows():
        rows.append(
            [
                safe_str(row.get("stock_id", "")),
                clean_text(row.get("stock_name", ""), 14),
                clean_text(display_zh(row.get("theme_name", row.get("theme_group", ""))), 14),
                clean_text(display_zh(row.get("theme_final_status", "")), 22),
                clean_text(display_zh(row.get("theme_volume_attack_status", "")), 24),
                clean_text(display_zh(row.get("volume_breakout_type", "")), 28),
                clean_text(display_zh(row.get("volume_breakout_priority", "")), 24),
                clean_text(display_zh(row.get("category", row.get("original_category", ""))), 18),
                clean_text(display_zh(row.get("tdcc_status", "")), 22),
                num_text(row.get("volume_ratio", ""), 2),
                pct_text(row.get("return_5d", "")),
                pct_text(row.get("return_20d", "")),
                clean_text(display_zh(row.get("next_volume_breakout_confirmation", "")), 48),
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
    append_theme_leadership_sections(story, style_map, compact=False)
    append_tdcc_overheated_edge_section(story, style_map, compact=False)
    append_weekly_surge_strict_section(story, style_map, compact=False)
    append_non_revenue_momentum_section(story, style_map, compact=False)

    volume_watch = load_volume_breakout_watch()
    story.append(Spacer(1, 0.25 * cm))
    story.append(para("帶量突破 / 放量攻擊觀察", style_map["h2"]))
    story.append(
        para(
            "本節列出價格與量能衍生的帶量突破、平台突破、頸線挑戰、區間突破與右側放量攻擊，並搭配 TDCC、連續上榜與過熱風險標籤分層。",
            style_map["normal"],
        )
    )
    if volume_watch.empty:
        story.append(para("本次資料日未產生帶量突破觀察列。", style_map["normal"]))
    else:
        for start in range(0, min(len(volume_watch), 60), 18):
            chunk = volume_watch.iloc[start : start + 18]
            story.append(
                make_table(
                    volume_breakout_table_rows(chunk),
                    style_map,
                    [0.8 * cm, 1.1 * cm, 1.4 * cm, 2.0 * cm, 2.4 * cm, 2.4 * cm, 1.9 * cm, 1.6 * cm, 1.5 * cm, 0.9 * cm, 0.8 * cm, 0.8 * cm, 4.4 * cm],
                )
            )
            story.append(Spacer(1, 0.2 * cm))

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
                    [
                        1.1 * cm,
                        1.4 * cm,
                        2.1 * cm,
                        1.5 * cm,
                        1.1 * cm,
                        1.1 * cm,
                        2.1 * cm,
                        1.8 * cm,
                        1.8 * cm,
                        1.8 * cm,
                        2.8 * cm,
                        4.0 * cm,
                        2.3 * cm,
                    ],
                )
            )
            story.append(Spacer(1, 0.25 * cm))
    doc.build(story)


def load_model_report_signals() -> pd.DataFrame:
    df = read_csv_safe(MODEL_REPORT_SIGNALS_CSV, dtype=str, keep_default_na=False)
    if df.empty:
        return df
    for col in ["report_line", "model_id", "stock_id", "model_name_zh", "display_rank", "model_score"]:
        if col not in df.columns:
            df[col] = ""
    df["_rank_num"] = pd.to_numeric(df["display_rank"], errors="coerce").fillna(999999)
    df["_score_num"] = pd.to_numeric(df["model_score"], errors="coerce").fillna(-999999)
    df = df.sort_values(["report_line", "model_id", "stock_id", "_rank_num", "_score_num"], ascending=[True, True, True, True, False])
    df = df.drop_duplicates(["report_line", "model_id", "stock_id"], keep="first")
    df = df.sort_values(["report_line", "model_name_zh", "_rank_num", "_score_num"], ascending=[True, True, True, False])
    return df.drop(columns=["_rank_num", "_score_num"], errors="ignore").reset_index(drop=True)


def load_technical_snapshot() -> dict[str, pd.Series]:
    df = read_csv_safe(TECHNICAL_SNAPSHOT_CSV, dtype={"stock_id": str}, keep_default_na=False)
    if df.empty or "stock_id" not in df.columns:
        return {}
    return {safe_str(row.get("stock_id")): row for _, row in df.iterrows()}


def display_text(*values: Any, fallback: str = "") -> str:
    for value in values:
        text = safe_str(value).strip()
        if not text:
            continue
        if "欄位尚未完成" in text or text in {"nan", "None"}:
            continue
        return display_zh(text)
    return fallback


def best_rows_by_model(df: pd.DataFrame, limit: int | None = None) -> pd.DataFrame:
    if df.empty:
        return df
    work = df.copy()
    work["_rank_num"] = pd.to_numeric(work.get("display_rank", ""), errors="coerce").fillna(999999)
    work["_score_num"] = pd.to_numeric(work.get("model_score", ""), errors="coerce").fillna(-999999)
    work = work.sort_values(["model_name_zh", "_rank_num", "_score_num"], ascending=[True, True, False])
    if limit is None:
        out = work
    else:
        out = work.groupby("model_name_zh", dropna=False, group_keys=False).head(limit)
    return out.drop(columns=["_rank_num", "_score_num"], errors="ignore")


def repeat_section_status(value: Any) -> str:
    return "repeated" if safe_str(value) == "repeated_same_model_signal" else "new"


def section_rank_fields(section: str) -> tuple[str, str, str]:
    if section == "repeated":
        return "model_rank_repeated_signal", "display_rank_repeated_signal", "連續上榜排名"
    return "model_rank_new_signal", "display_rank_new_signal", "新進榜排名"


def section_rows_by_model(df: pd.DataFrame, section: str, limit: int | None = None) -> pd.DataFrame:
    if df.empty:
        return df
    rank_col, display_col, section_label = section_rank_fields(section)
    work = df.copy()
    status_series = work.get("same_model_repeat_status", pd.Series("", index=work.index)).astype(str)
    if section == "repeated":
        work = work[status_series.eq("repeated_same_model_signal")]
    else:
        work = work[~status_series.eq("repeated_same_model_signal")]
    if work.empty:
        return work

    rank_values = work[rank_col] if rank_col in work.columns else pd.Series("", index=work.index)
    display_values = work[display_col] if display_col in work.columns else pd.Series("", index=work.index)
    fallback_rank_values = work["display_rank"] if "display_rank" in work.columns else pd.Series("", index=work.index)
    score_values = work["model_score"] if "model_score" in work.columns else pd.Series("", index=work.index)

    work["_section_rank_num"] = pd.to_numeric(rank_values, errors="coerce")
    work["_fallback_rank_num"] = pd.to_numeric(fallback_rank_values, errors="coerce")
    work["_rank_num"] = work["_section_rank_num"].fillna(work["_fallback_rank_num"]).fillna(999999)
    work["_score_num"] = pd.to_numeric(score_values, errors="coerce").fillna(-999999)
    work["pdf_section_status_zh"] = section_label
    fallback_display = fallback_rank_values.astype(str).replace({"nan": ""})
    work["pdf_section_rank"] = display_values.astype(str).replace({"nan": ""})
    work.loc[work["pdf_section_rank"].str.strip().eq(""), "pdf_section_rank"] = fallback_display
    work = work.sort_values(["model_name_zh", "_rank_num", "_score_num"], ascending=[True, True, False])
    if limit is not None:
        work = work.groupby("model_name_zh", dropna=False, group_keys=False).head(limit)
    return work.drop(columns=["_section_rank_num", "_fallback_rank_num", "_rank_num", "_score_num"], errors="ignore")


def sectioned_model_rows(df: pd.DataFrame, limit: int | None = None) -> list[tuple[str, str, pd.DataFrame]]:
    if df.empty:
        return []
    ordered = best_rows_by_model(df, None)
    result: list[tuple[str, str, pd.DataFrame]] = []
    seen_models: set[str] = set()
    for model_name in ordered.get("model_name_zh", pd.Series(dtype=str)).astype(str).tolist():
        if model_name in seen_models:
            continue
        seen_models.add(model_name)
        model_df = df[df.get("model_name_zh", "").astype(str).eq(model_name)].copy()
        for section in ["new", "repeated"]:
            section_df = section_rows_by_model(model_df, section, limit)
            if section_df.empty:
                continue
            _, _, section_label = section_rank_fields(section)
            result.append((model_name, section_label, section_df))
    return result


def pdf_text(value: Any, limit: int | None = None, fallback: str = "") -> str:
    return clean_text(display_zh(value, fallback=fallback), limit)


def first_page_best_rows(df: pd.DataFrame) -> pd.DataFrame:
    if df.empty:
        return df
    rows: list[pd.Series] = []
    ordered = best_rows_by_model(df, None)
    seen_models: set[str] = set()
    for model_name in ordered.get("model_name_zh", pd.Series(dtype=str)).astype(str).tolist():
        if model_name in seen_models:
            continue
        seen_models.add(model_name)
        model_df = df[df.get("model_name_zh", "").astype(str).eq(model_name)].copy()
        chosen = section_rows_by_model(model_df, "new", 1)
        if chosen.empty:
            chosen = section_rows_by_model(model_df, "repeated", 1)
        if not chosen.empty:
            rows.append(chosen.iloc[0])
    return pd.DataFrame(rows) if rows else df.head(0)


def section_rank_text(row: pd.Series) -> str:
    rank_text = display_text(row.get("pdf_section_rank"), row.get("display_rank"), fallback="")
    section_text = display_text(row.get("pdf_section_status_zh"), row.get("same_model_repeat_status_zh"), fallback="")
    if not rank_text:
        return section_text
    if section_text and not rank_text.startswith(section_text):
        normalized_rank = rank_text.replace("連續 / 重複進榜", "").strip()
        if section_text == "連續 / 重複進榜":
            return normalized_rank or rank_text
        if section_text == "新進榜":
            return normalized_rank or rank_text
    return rank_text


def first_page_rows(df: pd.DataFrame) -> list[list[Any]]:
    rows = [["模型", "第一名標的", "分數 / 榜別排名", "入選原因", "風險 / 操作提醒"]]
    if df.empty:
        rows.append(["資料不足", "無", "", "報告用模型訊號表尚未產生", "資料不足 / 僅能觀察"])
        return rows
    first = first_page_best_rows(df)
    for _, row in first.iterrows():
        rank_text = section_rank_text(row)
        rows.append(
            [
                clean_text(row.get("model_name_zh", "欄位尚未完成"), 22),
                f"{safe_str(row.get('stock_id'))} {safe_str(row.get('stock_name'))}",
                clean_text(f"{safe_str(row.get('model_score'))} / {rank_text}", 22),
                clean_text(display_text(row.get("why_selected_human_zh", ""), row.get("why_selected_zh", ""), fallback="依模型主條件入選"), 70),
                clean_text(display_text(row.get("operation_reminder_zh", ""), row.get("risk_tags_zh", ""), row.get("next_confirmation_zh", ""), row.get("recommended_usage_zh", ""), fallback="依支撐、壓力與量價管理"), 70),
            ]
        )
    return rows


def model_signal_card(
    row: pd.Series,
    style_map: dict[str, ParagraphStyle],
    tech_map: dict[str, pd.Series],
    chart_map: dict[tuple[str, str], Path],
    include_chart: bool,
) -> KeepTogether:
    stock_id = safe_str(row.get("stock_id"))
    tech = tech_map.get(stock_id, pd.Series(dtype=object))
    title = f"{stock_id} {safe_str(row.get('stock_name'))} / {safe_str(row.get('model_name_zh'))}"
    current_position = display_text(tech.get("price_position_summary_zh"), fallback="使用現有價格資料判斷位置。")
    technical = display_text(tech.get("technical_summary_zh"), fallback="使用現有技術 snapshot 判斷動能。")
    sr = display_text(tech.get("support_resistance_summary_zh"), fallback="依近期高低點與23EMA控管支撐壓力。")
    buy = display_text(tech.get("buy_condition_text_zh"), row.get("operation_reminder_zh"), row.get("recommended_usage_zh"), fallback="依模型主條件與支撐壓力執行。")
    take_profit = display_text(tech.get("take_profit_text_zh"), fallback="接近壓力且量價失敗時分批停利。")
    exit_text = display_text(tech.get("exit_condition_text_zh"), fallback="跌破支撐且站不回時退出或降風險。")
    risk = display_text(row.get("risk_tags_zh"), row.get("tdcc_risk_text_zh"), fallback="依量價、TDCC與風險標籤管理。")
    tdcc = display_text(row.get("tdcc_big_holder_summary_zh"), row.get("tdcc_status_zh"), fallback="TDCC資料不足，僅能輔助觀察。")
    rows = [
        ["操作結論", display_text(row.get("operation_reminder_zh"), row.get("recommended_usage_zh"), fallback="模型條件成立，依下列支撐壓力與風控管理。")],
        ["目前位置", current_position],
        ["技術狀態", technical],
        ["支撐 / 壓力", sr],
        ["買進條件", buy],
        ["停利 / 退出", f"{take_profit}；{exit_text}"],
        ["主要風險", risk],
        ["TDCC / 權證 / 營收補充", f"{tdcc}；{display_text(row.get('warrant_flow_signal_zh'), fallback='權證無明確訊號')}；來源：{display_text(row.get('source_hit_labels_zh'), fallback='使用模型來源欄位')}"],
    ]
    table_rows = [[para(title, style_map["curated_cell"]), para(f"分數 {safe_str(row.get('model_score'))} / {section_rank_text(row)}", style_map["curated_cell"])]]
    table_rows.extend([[para(k, style_map["label"]), para(v, style_map["curated_cell"])] for k, v in rows])
    table = Table(table_rows, colWidths=[4.0 * cm, 12.8 * cm])
    table.setStyle(
        TableStyle(
            [
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
    parts: list[Any] = [table]
    if include_chart:
        chart_row = row.copy()
        chart_row["category"] = safe_str(row.get("original_category")) or safe_str(row.get("source_hit_labels"))
        chart_path = chart_map.get((stock_id, "")) or redraw_pdf_kline_chart_for_row(chart_row)
        if chart_path is not None and chart_path.exists():
            parts.extend([Spacer(1, 0.12 * cm), PdfImage(str(chart_path), width=16.6 * cm, height=8.2 * cm)])
    parts.append(Spacer(1, 0.22 * cm))
    return KeepTogether(parts)


def model_detail_rows(df: pd.DataFrame) -> list[list[Any]]:
    rows = [["模型", "榜別", "排名", "股票", "分數", "入選原因", "風險 / 操作提醒"]]
    if df.empty:
        rows.append(["資料不足", "", "", "", "", "報告用模型訊號表尚未產生", "資料不足 / 僅能觀察"])
        return rows
    for _, row in df.iterrows():
        rows.append(
            [
                clean_text(row.get("model_name_zh", ""), 18),
                clean_text(display_text(row.get("pdf_section_status_zh"), row.get("same_model_repeat_status_zh"), fallback=""), 10),
                clean_text(display_text(row.get("pdf_section_rank"), row.get("display_rank"), fallback=""), 8),
                f"{safe_str(row.get('stock_id'))} {safe_str(row.get('stock_name'))}",
                clean_text(row.get("model_score", ""), 8),
                clean_text(display_text(row.get("why_selected_human_zh", ""), row.get("why_selected_zh", ""), fallback="依模型主條件入選"), 65),
                clean_text(display_text(row.get("operation_reminder_zh", ""), row.get("risk_tags_zh", ""), row.get("next_confirmation_zh", ""), row.get("recommended_usage_zh", ""), fallback="依支撐壓力管理"), 65),
            ]
        )
    return rows


def append_group_rotation_section(story: list[Any], style_map: dict[str, ParagraphStyle]) -> None:
    rotation = read_csv_safe(LATEST_DIR / "daily_candidate_group_rotation_latest.csv", dtype=str, keep_default_na=False)
    if rotation.empty:
        return
    story.append(PageBreak())
    story.append(para("族群資金輪動觀察", style_map["h1"]))
    story.append(para("此段用於預判資金流向，不是個股買進模型。條件為同族群超過三分之一股票量比達 3 倍以上。", style_map["normal"]))
    rows = [["族群", "股票數", "3倍量檔數", "擴散比例", "龍頭 / 老二 / 老三", "解讀"]]
    for _, row in rotation.head(20).iterrows():
        rows.append(
            [
                clean_text(row.get("theme", ""), 18),
                clean_text(row.get("stock_count", ""), 8),
                clean_text(row.get("volume_expansion_3x_count", ""), 8),
                clean_text(row.get("volume_expansion_ratio", ""), 8),
                " / ".join([safe_str(row.get("leader_1")), safe_str(row.get("leader_2")), safe_str(row.get("leader_3"))]).strip(" /"),
                clean_text(row.get("interpretation_zh", "") or row.get("interpretation", "") or "觀察資金是否由龍頭擴散", 70),
            ]
        )
    story.append(make_table(rows, style_map, [2.5 * cm, 1.6 * cm, 1.8 * cm, 1.8 * cm, 4.1 * cm, 6.0 * cm]))


def append_theme_event_watch_section(story: list[Any], style_map: dict[str, ParagraphStyle], compact: bool) -> None:
    events = read_csv_safe(LATEST_DIR / "theme_event_watch_latest.csv", dtype=str, keep_default_na=False)
    story.append(PageBreak())
    story.append(para("近期事件預警 / 主題催化觀察", style_map["h1"]))
    story.append(
        para(
            "用途：提示近期展覽、法說、政策或產業事件與候選股/族群的交集。這是事件標籤與追蹤提醒，不取代模型入選條件。",
            style_map["normal"],
        )
    )
    if events.empty:
        story.append(para("目前沒有可用的近期事件資料；事件層暫不影響今日候選股解讀。", style_map["normal"]))
        return

    for col in ["days_to_event", "importance", "candidate_intersection_count", "matched_stock_count"]:
        if col in events.columns:
            events[col + "_num"] = pd.to_numeric(events[col], errors="coerce")
    sort_cols = [c for c in ["days_to_event_num", "importance_num", "candidate_intersection_count_num"] if c in events.columns]
    if sort_cols:
        ascending = [True if c == "days_to_event_num" else False for c in sort_cols]
        events = events.sort_values(sort_cols, ascending=ascending)
    limit = 10 if compact else 40
    rows = [["事件", "日期", "族群", "候選交集", "代表候選", "解讀"]]
    for _, row in events.head(limit).iterrows():
        event_range = safe_str(row.get("event_date", ""))
        end_date = safe_str(row.get("event_end_date", ""))
        if end_date and end_date != event_range:
            event_range = f"{event_range}-{end_date}"
        candidates = display_text(
            row.get("top_candidate_summary_zh"),
            row.get("candidate_intersection_stock_names"),
            fallback="目前無候選股交集",
        )
        rows.append(
            [
                clean_text(display_text(row.get("event_name"), fallback="事件未命名"), 26),
                clean_text(event_range, 18),
                clean_text(display_text(row.get("theme_tag"), fallback="族群未標示"), 18),
                clean_text(display_text(row.get("candidate_intersection_count"), fallback="0"), 8),
                clean_text(candidates, 42),
                clean_text(display_text(row.get("interpretation_zh"), row.get("theme_event_watch_status"), fallback="事件資料僅供觀察"), 58),
            ]
        )
    story.append(make_table(rows, style_map, [3.1 * cm, 2.0 * cm, 2.2 * cm, 1.5 * cm, 4.2 * cm, 5.2 * cm]))


def build_model_line_pdf(report_line: str, full: bool, main_date: str, path: Path) -> None:
    style_map = styles()
    signals = load_model_report_signals()
    model_summary = _load_model_summary_for_report()
    tech_map = load_technical_snapshot()
    chart_map = load_pdf_kline_chart_map()
    part = signals[signals.get("report_line", "").astype(str).eq(report_line)].copy() if not signals.empty else signals
    title_prefix = "主流股" if report_line == "mainstream" else "非主流股"
    title = f"{title_prefix}{'完整候選清單' if full else '每日推薦精華'}"
    doc = SimpleDocTemplate(
        str(path),
        pagesize=A4,
        leftMargin=1.5 * cm,
        rightMargin=1.5 * cm,
        topMargin=1.2 * cm,
        bottomMargin=1.2 * cm,
    )
    story: list[Any] = []
    story.append(para(f"{main_date} {title}", style_map["title"]))
    story.append(para("資料來源：報告用模型訊號表；不同模型不混成單一排名。", style_map["subtitle"]))
    story.append(para("各模型第一名摘要", style_map["h1"]))
    story.append(make_table(first_page_rows(part), style_map, [3.1 * cm, 3.1 * cm, 2.2 * cm, 5.0 * cm, 5.0 * cm]))
    story.append(PageBreak())
    if full:
        story.append(para("完整模型候選清單", style_map["h1"]))
        for model_name, section_label, group in sectioned_model_rows(part, None):
            story.append(para(safe_str(model_name) or "模型欄位尚未完成", style_map["h2"]))
            story.append(para(section_label, style_map["normal"]))
            story.append(make_table(model_detail_rows(group), style_map, [2.3 * cm, 1.4 * cm, 1.2 * cm, 2.4 * cm, 1.2 * cm, 4.8 * cm, 5.2 * cm]))
            story.append(Spacer(1, 0.3 * cm))
    else:
        story.append(para("各模型代表股操作卡", style_map["h1"]))
        for model_name, section_label, group in sectioned_model_rows(part, 5):
            story.append(para(safe_str(model_name) or "模型欄位尚未完成", style_map["h2"]))
            story.append(para(section_label, style_map["normal"]))
            for _, row in group.iterrows():
                story.append(model_signal_card(row, style_map, tech_map, chart_map, include_chart=True))
    append_theme_event_watch_section(story, style_map, compact=not full)
    append_group_rotation_section(story, style_map)
    doc.build(story)


def _rank_for_display(row: pd.Series) -> str:
    rank = display_text(row.get("pdf_section_rank"), row.get("display_rank"), fallback="")
    status = display_text(row.get("pdf_section_status_zh"), row.get("same_model_repeat_status_zh"), fallback="")
    if rank:
        return rank
    return status


def _first_page_rows_clean(df: pd.DataFrame) -> list[list[Any]]:
    rows = [["模型", "第一名標的", "分數 / 排名", "入選優點", "風險 / 操作提醒"]]
    if df.empty:
        rows.append(["資料不足", "-", "", "報告用模型訊號表未產出", "資料不足 / 僅能觀察"])
        return rows
    first = first_page_best_rows(df)
    for _, row in first.iterrows():
        rows.append(
            [
                clean_text(display_text(row.get("model_name_zh"), fallback="模型名稱未完成"), 22),
                f"{safe_str(row.get('stock_id'))} {safe_str(row.get('stock_name'))}",
                clean_text(f"{safe_str(row.get('model_score'))} / {_rank_for_display(row)}", 22),
                clean_text(display_text(row.get("why_selected_human_zh"), row.get("why_selected_zh"), fallback="欄位尚未完成 / 暫用現有資料"), 68),
                clean_text(display_text(row.get("operation_reminder_zh"), row.get("risk_tags_zh"), row.get("next_confirmation_zh"), row.get("recommended_usage_zh"), fallback="依支撐壓力與模型條件管理。"), 68),
            ]
        )
    return rows


def _model_detail_rows_clean(df: pd.DataFrame) -> list[list[Any]]:
    rows = [["模型", "榜別", "排名", "標的", "分數", "入選優點", "風險 / 操作提醒"]]
    if df.empty:
        rows.append(["資料不足", "", "", "-", "", "報告用模型訊號表未產出", "資料不足 / 僅能觀察"])
        return rows
    for _, row in df.iterrows():
        rows.append(
            [
                clean_text(display_text(row.get("model_name_zh"), fallback="模型名稱未完成"), 18),
                clean_text(display_text(row.get("pdf_section_status_zh"), row.get("same_model_repeat_status_zh"), fallback=""), 10),
                clean_text(display_text(row.get("pdf_section_rank"), row.get("display_rank"), fallback=""), 12),
                f"{safe_str(row.get('stock_id'))} {safe_str(row.get('stock_name'))}",
                clean_text(row.get("model_score", ""), 8),
                clean_text(display_text(row.get("why_selected_human_zh"), row.get("why_selected_zh"), fallback="欄位尚未完成 / 暫用現有資料"), 64),
                clean_text(display_text(row.get("operation_reminder_zh"), row.get("risk_tags_zh"), row.get("next_confirmation_zh"), row.get("recommended_usage_zh"), fallback="依支撐壓力與模型條件管理。"), 64),
            ]
        )
    return rows


def _model_signal_card_clean(
    row: pd.Series,
    style_map: dict[str, ParagraphStyle],
    tech_map: dict[str, pd.Series],
    chart_map: dict[tuple[str, str], Path],
    include_chart: bool,
) -> KeepTogether:
    stock_id = safe_str(row.get("stock_id"))
    stock_name = safe_str(row.get("stock_name"))
    tech = tech_map.get(stock_id, pd.Series(dtype=object))
    title = f"{stock_id} {stock_name} / {display_text(row.get('model_name_zh'), fallback='模型名稱未完成')}"
    rows = [
        ["操作結論", display_text(row.get("operation_reminder_zh"), row.get("recommended_usage_zh"), fallback="依模型條件入選；後續以支撐壓力與量價管理。")],
        ["目前位置", display_text(tech.get("price_position_summary_zh"), fallback="技術 snapshot 尚未完成 / 暫用現有資料")],
        ["技術狀態", display_text(tech.get("technical_summary_zh"), fallback="技術 snapshot 尚未完成 / 暫用現有資料")],
        ["支撐 / 壓力", display_text(tech.get("support_resistance_summary_zh"), fallback="支撐壓力欄位尚未完成 / 暫用現有資料")],
        ["買進條件", display_text(tech.get("buy_condition_text_zh"), row.get("operation_reminder_zh"), fallback="依模型主條件成立後，以隔日開盤與支撐壓力控管。")],
        ["停利 / 退出", f"{display_text(tech.get('take_profit_text_zh'), fallback='接近前高或量價失敗時分批停利。')}；{display_text(tech.get('exit_condition_text_zh'), fallback='跌破關鍵支撐且無法收回時退出。')}"],
        ["主要風險", display_text(row.get("risk_tags_zh"), row.get("tdcc_risk_text_zh"), fallback="風險欄位尚未完成 / 暫用現有資料")],
        ["TDCC / 權證 / 來源", f"{display_text(row.get('tdcc_big_holder_summary_zh'), row.get('tdcc_status_zh'), fallback='TDCC 欄位尚未完成')}；{display_text(row.get('warrant_flow_signal_zh'), fallback='權證欄位尚未完成')}；{display_text(row.get('source_hit_labels_zh'), fallback='來源欄位尚未完成')}"],
    ]
    table_rows = [[para(title, style_map["curated_cell"]), para(f"分數 {safe_str(row.get('model_score'))} / {_rank_for_display(row)}", style_map["curated_cell"])]]
    table_rows.extend([[para(k, style_map["label"]), para(v, style_map["curated_cell"])] for k, v in rows])
    table = Table(table_rows, colWidths=[4.0 * cm, 12.8 * cm])
    table.setStyle(
        TableStyle(
            [
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
    parts: list[Any] = [table]
    if include_chart:
        chart_row = row.copy()
        chart_row["category"] = safe_str(row.get("original_category")) or safe_str(row.get("source_hit_labels"))
        chart_path = chart_map.get((stock_id, "")) or redraw_pdf_kline_chart_for_row(chart_row)
        if chart_path is not None and chart_path.exists():
            parts.extend([Spacer(1, 0.12 * cm), PdfImage(str(chart_path), width=16.6 * cm, height=8.2 * cm)])
    parts.append(Spacer(1, 0.22 * cm))
    return KeepTogether(parts)


def _append_theme_event_watch_section_clean(story: list[Any], style_map: dict[str, ParagraphStyle], compact: bool) -> None:
    events = read_csv_safe(LATEST_DIR / "theme_event_watch_latest.csv", dtype=str, keep_default_na=False)
    story.append(PageBreak())
    story.append(para("近期事件預警 / 主題催化觀察", style_map["h1"]))
    if events.empty:
        story.append(para("目前沒有可用的事件預警資料。", style_map["normal"]))
        return
    rows = [["事件", "日期", "族群", "交集數", "相關標的", "解讀"]]
    limit = 8 if compact else 30
    for _, row in events.head(limit).iterrows():
        start_date = display_text(row.get("event_start_date"), row.get("start_date"), fallback="")
        end_date = display_text(row.get("event_end_date"), row.get("end_date"), fallback="")
        event_range = start_date if not end_date or end_date == start_date else f"{start_date}-{end_date}"
        rows.append(
            [
                clean_text(display_text(row.get("event_name"), fallback="事件名稱未完成"), 24),
                clean_text(event_range, 18),
                clean_text(display_text(row.get("theme_tag"), fallback="族群標籤未完成"), 18),
                clean_text(display_text(row.get("candidate_intersection_count"), fallback="0"), 8),
                clean_text(display_text(row.get("top_candidate_summary_zh"), row.get("candidate_intersection_stock_names"), fallback="-"), 42),
                clean_text(display_text(row.get("interpretation_zh"), row.get("theme_event_watch_status"), fallback="事件資料僅供觀察。"), 58),
            ]
        )
    story.append(make_table(rows, style_map, [3.1 * cm, 2.0 * cm, 2.2 * cm, 1.5 * cm, 4.2 * cm, 5.2 * cm]))


def _append_group_rotation_section_clean(story: list[Any], style_map: dict[str, ParagraphStyle]) -> None:
    rotation = read_csv_safe(LATEST_DIR / "daily_candidate_group_rotation_latest.csv", dtype=str, keep_default_na=False)
    if rotation.empty:
        return
    story.append(PageBreak())
    story.append(para("族群資金輪動觀察", style_map["h1"]))
    story.append(para("此區不是個股買進模型，用於觀察族群出量是否由龍頭擴散到老二、老三。", style_map["normal"]))
    rows = [["族群", "檔數", "3倍量檔數", "出量比例", "龍頭 / 老二 / 老三", "解讀"]]
    for _, row in rotation.head(20).iterrows():
        rows.append(
            [
                clean_text(display_text(row.get("theme"), fallback="族群未完成"), 18),
                clean_text(row.get("stock_count", ""), 8),
                clean_text(row.get("volume_expansion_3x_count", ""), 8),
                clean_text(row.get("volume_expansion_ratio", ""), 8),
                clean_text(" / ".join([safe_str(row.get("leader_1")), safe_str(row.get("leader_2")), safe_str(row.get("leader_3"))]).strip(" /"), 36),
                clean_text(display_text(row.get("interpretation_zh"), row.get("interpretation"), fallback="觀察資金是否持續擴散。"), 60),
            ]
        )
    story.append(make_table(rows, style_map, [2.5 * cm, 1.6 * cm, 1.8 * cm, 1.8 * cm, 4.1 * cm, 6.0 * cm]))


def build_model_line_pdf(report_line: str, full: bool, main_date: str, path: Path) -> None:
    style_map = styles()
    signals = load_model_report_signals()
    tech_map = load_technical_snapshot()
    chart_map = load_pdf_kline_chart_map()
    part = signals[signals.get("report_line", "").astype(str).eq(report_line)].copy() if not signals.empty else signals
    title_prefix = "主流股" if report_line == "mainstream" else "非主流股"
    title = f"{title_prefix}{'完整候選清單' if full else '每日推薦精華'}"
    doc = SimpleDocTemplate(
        str(path),
        pagesize=A4,
        leftMargin=1.5 * cm,
        rightMargin=1.5 * cm,
        topMargin=1.2 * cm,
        bottomMargin=1.2 * cm,
    )
    story: list[Any] = []
    story.append(para(f"{main_date} {title}", style_map["title"]))
    story.append(para("資料來源：報告用模型訊號表；各模型獨立呈現，不混成單一總排名。", style_map["subtitle"]))
    story.append(para("各模型第一名摘要", style_map["h1"]))
    story.append(make_table(_first_page_rows_clean(part), style_map, [3.1 * cm, 3.1 * cm, 2.2 * cm, 5.0 * cm, 5.0 * cm]))
    story.append(PageBreak())
    if full:
        story.append(para("完整模型候選清單", style_map["h1"]))
        for model_name, section_label, group in sectioned_model_rows(part, None):
            story.append(para(display_text(model_name, fallback="模型名稱未完成"), style_map["h2"]))
            story.append(para(section_label, style_map["normal"]))
            story.append(make_table(_model_detail_rows_clean(group), style_map, [2.3 * cm, 1.4 * cm, 1.2 * cm, 2.4 * cm, 1.2 * cm, 4.8 * cm, 5.2 * cm]))
            story.append(Spacer(1, 0.3 * cm))
    else:
        story.append(para("各模型代表股解析", style_map["h1"]))
        for model_name, section_label, group in sectioned_model_rows(part, 5):
            story.append(para(display_text(model_name, fallback="模型名稱未完成"), style_map["h2"]))
            story.append(para(section_label, style_map["normal"]))
            for _, row in group.iterrows():
                story.append(_model_signal_card_clean(row, style_map, tech_map, chart_map, include_chart=True))
    _append_theme_event_watch_section_clean(story, style_map, compact=not full)
    _append_group_rotation_section_clean(story, style_map)
    doc.build(story)


def _rank_for_display_final(row: pd.Series) -> str:
    rank = display_text(row.get("pdf_section_rank"), fallback="")
    if not rank:
        rank = display_text(row.get("display_rank"), fallback="")
    status = display_text(row.get("pdf_section_status_zh"), row.get("same_model_repeat_status_zh"), fallback="")
    if status and rank and not rank.startswith(status):
        return f"{status} {rank}"
    return rank or status or "-"


def _display_final(*values: Any, fallback: str = "欄位尚未完成 / 暫用現有資料", limit: int | None = None) -> str:
    text = display_text(*values, fallback=fallback)
    text = clean_text(text, limit)
    if not text or "甈" in text or "鞈" in text or "銝" in text or "摰" in text:
        return fallback
    return text


def _first_page_rows_final(df: pd.DataFrame) -> list[list[Any]]:
    rows = [["模型", "第一名標的", "分數 / 排名", "入選優點", "風險 / 操作提醒"]]
    if df.empty:
        rows.append(["資料不足", "-", "-", "報告用模型訊號表無資料", "資料不足 / 僅能觀察"])
        return rows
    first = first_page_best_rows(df)
    for _, row in first.iterrows():
        rows.append(
            [
                _display_final(row.get("model_name_zh"), fallback="模型名稱未完成", limit=24),
                f"{safe_str(row.get('stock_id'))} {safe_str(row.get('stock_name'))}",
                clean_text(f"{safe_str(row.get('model_score'))} / {_rank_for_display_final(row)}", 24),
                _display_final(row.get("why_selected_human_zh"), row.get("why_selected_zh"), fallback="符合模型主要條件；詳細計分請看 score_components_zh。", limit=72),
                _display_final(row.get("operation_reminder_zh"), row.get("risk_tags_zh"), row.get("next_confirmation_zh"), row.get("recommended_usage_zh"), fallback="依模型條件入選；買進後依支撐、量價與 TDCC 變化管理。", limit=72),
            ]
        )
    return rows


def _model_detail_rows_final(df: pd.DataFrame) -> list[list[Any]]:
    rows = [["模型", "榜別", "排名", "標的", "分數", "入選優點", "風險 / 操作提醒"]]
    if df.empty:
        rows.append(["資料不足", "", "", "-", "", "報告用模型訊號表無資料", "資料不足 / 僅能觀察"])
        return rows
    for _, row in df.iterrows():
        rows.append(
            [
                _display_final(row.get("model_name_zh"), fallback="模型名稱未完成", limit=18),
                _display_final(row.get("pdf_section_status_zh"), row.get("same_model_repeat_status_zh"), fallback="", limit=10),
                clean_text(_rank_for_display_final(row), 14),
                f"{safe_str(row.get('stock_id'))} {safe_str(row.get('stock_name'))}",
                clean_text(row.get("model_score", ""), 8),
                _display_final(row.get("why_selected_human_zh"), row.get("why_selected_zh"), fallback="符合模型主要條件；詳細計分請看 score_components_zh。", limit=66),
                _display_final(row.get("operation_reminder_zh"), row.get("risk_tags_zh"), row.get("next_confirmation_zh"), row.get("recommended_usage_zh"), fallback="依模型條件入選；買進後依支撐、量價與 TDCC 變化管理。", limit=66),
            ]
        )
    return rows


def _model_signal_card_final(
    row: pd.Series,
    style_map: dict[str, ParagraphStyle],
    tech_map: dict[str, pd.Series],
    chart_map: dict[tuple[str, str], Path],
    include_chart: bool,
) -> KeepTogether:
    stock_id = safe_str(row.get("stock_id"))
    stock_name = safe_str(row.get("stock_name"))
    tech = tech_map.get(stock_id, pd.Series(dtype=object))
    title = f"{stock_id} {stock_name} / {_display_final(row.get('model_name_zh'), fallback='模型名稱未完成')}"
    table_rows = [
        [
            para(title, style_map["curated_cell"]),
            para(f"分數 {safe_str(row.get('model_score'))} / {_rank_for_display_final(row)}", style_map["curated_cell"]),
        ],
        [para("操作提醒", style_map["label"]), para(_display_final(row.get("operation_reminder_zh"), row.get("recommended_usage_zh"), fallback="依模型條件入選；買進後依支撐、量價與 TDCC 變化管理。"), style_map["curated_cell"])],
        [para("目前位置", style_map["label"]), para(_display_final(tech.get("price_position_summary_zh"), fallback="技術 snapshot 尚未完成 / 暫用 K 線圖判讀。"), style_map["curated_cell"])],
        [para("技術狀態", style_map["label"]), para(_display_final(tech.get("technical_summary_zh"), fallback="技術 snapshot 尚未完成 / 暫用 K 線圖判讀。"), style_map["curated_cell"])],
        [para("支撐 / 壓力", style_map["label"]), para(_display_final(tech.get("support_resistance_summary_zh"), fallback="支撐壓力欄位尚未完成 / 暫用 23EMA、前高與近期低點管理。"), style_map["curated_cell"])],
        [para("入選優點", style_map["label"]), para(_display_final(row.get("why_selected_human_zh"), row.get("why_selected_zh"), fallback="符合模型主要條件；詳細計分請看 score_components_zh。"), style_map["curated_cell"])],
        [para("買進條件", style_map["label"]), para(_display_final(tech.get("buy_condition_text_zh"), row.get("operation_reminder_zh"), fallback="依模型條件入選；實際進場以隔日開盤、支撐與量價確認管理。"), style_map["curated_cell"])],
        [para("停利 / 退出", style_map["label"]), para(f"{_display_final(tech.get('take_profit_text_zh'), fallback='接近前高、爆量不漲或量價背離時分批停利。')}；{_display_final(tech.get('exit_condition_text_zh'), fallback='跌破 23EMA、近期低點或出現放量長黑時降低部位或退出。')}", style_map["curated_cell"])],
        [para("主要風險", style_map["label"]), para(_display_final(row.get("risk_tags_zh"), row.get("tdcc_risk_text_zh"), row.get("downgrade_flags_zh"), fallback="風險欄位尚未完成 / 需觀察量價、TDCC 與事件後續。"), style_map["curated_cell"])],
        [para("TDCC / 權證 / 來源", style_map["label"]), para(f"{_display_final(row.get('tdcc_big_holder_summary_zh'), row.get('tdcc_status_zh'), fallback='TDCC 摘要尚未完成')}；{_display_final(row.get('warrant_flow_signal_zh'), fallback='權證訊號尚未完成')}；{_display_final(row.get('source_hit_labels_zh'), fallback='來源分類尚未完成')}", style_map["curated_cell"])],
    ]
    table = Table(table_rows, colWidths=[4.0 * cm, 12.8 * cm])
    table.setStyle(
        TableStyle(
            [
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
    parts: list[Any] = [table]
    if include_chart:
        chart_row = row.copy()
        chart_row["category"] = safe_str(row.get("original_category")) or safe_str(row.get("source_hit_labels"))
        chart_path = chart_map.get((stock_id, "")) or redraw_pdf_kline_chart_for_row(chart_row)
        if chart_path is not None and chart_path.exists():
            parts.extend([Spacer(1, 0.12 * cm), PdfImage(str(chart_path), width=16.6 * cm, height=8.2 * cm)])
    parts.append(Spacer(1, 0.22 * cm))
    return KeepTogether(parts)


def _append_theme_event_watch_section_final(story: list[Any], style_map: dict[str, ParagraphStyle], compact: bool) -> None:
    events = read_csv_safe(LATEST_DIR / "theme_event_watch_latest.csv", dtype=str, keep_default_na=False)
    story.append(PageBreak())
    story.append(para("近期事件預警 / 主題催化觀察", style_map["h1"]))
    if events.empty:
        story.append(para("目前沒有可用事件預警資料。若事件資料未進入 theme_event_watch_latest.csv，PDF 不自行補事件。", style_map["normal"]))
        return
    rows = [["事件", "日期", "族群", "交集數", "相關候選", "解讀"]]
    limit = 8 if compact else 30
    for _, row in events.head(limit).iterrows():
        start_date = _display_final(row.get("event_start_date"), row.get("start_date"), fallback="")
        end_date = _display_final(row.get("event_end_date"), row.get("end_date"), fallback="")
        event_range = start_date if not end_date or end_date == start_date else f"{start_date}-{end_date}"
        rows.append(
            [
                _display_final(row.get("event_name"), fallback="事件名稱未完成", limit=24),
                clean_text(event_range, 18),
                _display_final(row.get("theme_tag"), fallback="族群標籤未完成", limit=18),
                _display_final(row.get("candidate_intersection_count"), fallback="0", limit=8),
                _display_final(row.get("top_candidate_summary_zh"), row.get("candidate_intersection_stock_names"), fallback="-", limit=42),
                _display_final(row.get("interpretation_zh"), row.get("theme_event_watch_status"), fallback="事件資料已建立，需觀察族群量價與候選股交集。", limit=58),
            ]
        )
    story.append(make_table(rows, style_map, [3.1 * cm, 2.0 * cm, 2.2 * cm, 1.5 * cm, 4.2 * cm, 5.2 * cm]))


def _append_group_rotation_section_final(story: list[Any], style_map: dict[str, ParagraphStyle]) -> None:
    rotation = read_csv_safe(LATEST_DIR / "daily_candidate_group_rotation_latest.csv", dtype=str, keep_default_na=False)
    if rotation.empty:
        return
    story.append(PageBreak())
    story.append(para("族群資金輪動觀察", style_map["h1"]))
    story.append(para("這不是個股買進模型。用途是觀察同族群是否出現資金擴散，判斷資金是否從龍頭擴散到第二、第三順位。", style_map["normal"]))
    rows = [["族群", "股票數", "3倍量家數", "出量比例", "龍頭 / 老二 / 老三", "解讀"]]
    for _, row in rotation.head(20).iterrows():
        rows.append(
            [
                _display_final(row.get("theme"), fallback="族群未完成", limit=18),
                clean_text(row.get("stock_count", ""), 8),
                clean_text(row.get("volume_expansion_3x_count", ""), 8),
                clean_text(row.get("volume_expansion_ratio", ""), 8),
                clean_text(" / ".join([safe_str(row.get("leader_1")), safe_str(row.get("leader_2")), safe_str(row.get("leader_3"))]).strip(" /"), 36),
                _display_final(row.get("interpretation_zh"), row.get("interpretation"), fallback="資金擴散狀態待觀察。", limit=60),
            ]
        )
    story.append(make_table(rows, style_map, [2.5 * cm, 1.6 * cm, 1.8 * cm, 1.8 * cm, 4.1 * cm, 6.0 * cm]))


def build_model_line_pdf(report_line: str, full: bool, main_date: str, path: Path) -> None:
    style_map = styles()
    signals = load_model_report_signals()
    tech_map = load_technical_snapshot()
    chart_map = load_pdf_kline_chart_map()
    part = signals[signals.get("report_line", "").astype(str).eq(report_line)].copy() if not signals.empty else signals
    title_prefix = "主流股" if report_line == "mainstream" else "非主流股"
    title_suffix = "完整候選清單" if full else "每日推薦精華"
    doc = SimpleDocTemplate(
        str(path),
        pagesize=A4,
        leftMargin=1.5 * cm,
        rightMargin=1.5 * cm,
        topMargin=1.2 * cm,
        bottomMargin=1.2 * cm,
    )
    story: list[Any] = []
    story.append(para(f"{main_date} {title_prefix}{title_suffix}", style_map["title"]))
    story.append(para("資料來源：報告用模型訊號表；同一模型同一股票已去重，並依新進榜 / 重複進榜分段呈現。", style_map["subtitle"]))
    story.append(para("各模型第一名摘要", style_map["h1"]))
    story.append(make_table(_first_page_rows_final(part), style_map, [3.1 * cm, 3.1 * cm, 2.2 * cm, 5.0 * cm, 5.0 * cm]))
    story.append(PageBreak())
    if full:
        story.append(para("完整模型名單", style_map["h1"]))
        for model_name, section_label, group in sectioned_model_rows(part, None):
            story.append(para(_display_final(model_name, fallback="模型名稱未完成"), style_map["h2"]))
            story.append(para(_display_final(section_label, fallback="榜別未完成"), style_map["h2"]))
            story.append(make_table(_model_detail_rows_final(group), style_map, [2.3 * cm, 1.4 * cm, 1.2 * cm, 2.4 * cm, 1.2 * cm, 4.8 * cm, 5.2 * cm]))
            story.append(Spacer(1, 0.3 * cm))
    else:
        story.append(para("各模型代表股", style_map["h1"]))
        for model_name, section_label, group in sectioned_model_rows(part, 5):
            story.append(para(_display_final(model_name, fallback="模型名稱未完成"), style_map["h2"]))
            story.append(para(_display_final(section_label, fallback="榜別未完成"), style_map["h2"]))
            for _, row in group.iterrows():
                story.append(_model_signal_card_final(row, style_map, tech_map, chart_map, include_chart=True))
    _append_theme_event_watch_section_final(story, style_map, compact=not full)
    _append_group_rotation_section_final(story, style_map)
    doc.build(story)


PDF_DISPLAY_TOKEN_ZH_CLEAN = {
    "range_rebound": "區間內轉強",
    "revenue_pullback": "營收成長股價回檔",
    "revenue_breakout_low_response": "營收爆發但股價尚未反應",
    "pullback_rebound": "回檔後短線轉強",
    "short_term_specialty": "短線專項",
    "tdcc_short_term_edge": "TDCC短線延續",
    "hot_theme_pullback": "熱門族群回檔",
    "price_pullback_23ema": "股價回檔",
    "tdcc_stealth_accumulation": "TDCC潛伏吸籌",
    "tdcc_short_term_continuation_d5_d10": "TDCC短線延續 D+5/D+10",
    "volume_range_breakout": "帶量突破",
    "w_bottom_right_side": "W底右側",
    "platform_strengthening": "平台整理轉強",
    "near_high_neckline_challenge": "接近前高/頸線挑戰",
    "new_model_signal": "新進榜",
    "repeated_same_model_signal": "連續/累計進榜",
    "mainstream": "主流",
    "non_mainstream": "非主流",
    "strong_accumulation": "大戶強累積",
    "mild_accumulation": "大戶溫和增加",
    "distribution_warning": "大戶轉弱警示",
    "neutral": "中性",
    "call_strong_inflow": "認購明確偏多",
    "call_inflow": "認購偏多",
    "call_put_bullish": "權證偏多",
    "mixed_flow": "權證多空混合",
    "no_signal": "無明確訊號",
    "insufficient_data": "資料不足",
    "neckline": "頸線",
    "breakout": "突破",
    "hot_theme_tag": "熱門族群標籤",
    "hot theme tag": "熱門族群標籤",
}


def _pdf_human_text(*values: Any, fallback: str = "資料不足 / 暫用現有資料", limit: int | None = None) -> str:
    text = ""
    for value in values:
        candidate = safe_str(value).strip()
        if not candidate or candidate.lower() in {"nan", "none", "null"}:
            continue
        text = candidate
        break
    if not text:
        text = fallback
    for raw, zh in PDF_DISPLAY_TOKEN_ZH_CLEAN.items():
        text = re.sub(rf"(?<![A-Za-z0-9_]){re.escape(raw)}(?![A-Za-z0-9_])", zh, text)
    if re.fullmatch(r"[A-Za-z0-9_./ -]+", text or "") and "_" in text:
        text = fallback
    return clean_text(text, limit)


def _model_score_text(value: Any) -> str:
    text = safe_str(value).strip()
    if not text:
        return "-"
    try:
        num = float(text)
        return f"{num:.1f}".rstrip("0").rstrip(".")
    except Exception:
        return clean_text(text, 10)


def _repeat_key(row: pd.Series) -> str:
    status = safe_str(row.get("same_model_repeat_status"))
    return "repeated" if status == "repeated_same_model_signal" else "new"


def _repeat_label(section: str) -> str:
    return "連續/累計進榜" if section == "repeated" else "新進榜"


def _rank_for_section(row: pd.Series, section: str) -> str:
    if section == "repeated":
        rank = safe_str(row.get("display_rank_repeated_signal")) or safe_str(row.get("model_rank_repeated_signal"))
    else:
        rank = safe_str(row.get("display_rank_new_signal")) or safe_str(row.get("model_rank_new_signal"))
    if not rank:
        rank = safe_str(row.get("display_rank")) or safe_str(row.get("model_rank"))
    try:
        if re.fullmatch(r"\d+(\.0+)?", rank):
            rank = str(int(float(rank)))
    except Exception:
        pass
    prefix = "連續榜#" if section == "repeated" else "新進榜#"
    if rank and not rank.startswith(prefix) and not rank.startswith(_repeat_label(section)):
        rank = f"{prefix}{rank}"
    return rank or "-"


def _rank_sort_number(row: pd.Series, section: str) -> float:
    if section == "repeated":
        fields = ["model_rank_repeated_signal", "display_rank_repeated_signal", "display_rank", "model_rank"]
    else:
        fields = ["model_rank_new_signal", "display_rank_new_signal", "display_rank", "model_rank"]
    for field in fields:
        text = safe_str(row.get(field))
        match = re.search(r"\d+", text)
        if match:
            return float(match.group(0))
    return 999999.0


def _score_sort_number(row: pd.Series) -> float:
    try:
        return float(safe_str(row.get("model_score")))
    except Exception:
        return -999999.0


def _model_names_in_report_order(df: pd.DataFrame) -> list[str]:
    if df.empty or "model_name_zh" not in df.columns:
        return []
    work = df.copy()
    work["_rank"] = work.apply(lambda row: min(_rank_sort_number(row, "new"), _rank_sort_number(row, "repeated")), axis=1)
    work["_score"] = work.apply(_score_sort_number, axis=1)
    work = work.sort_values(["_rank", "_score"], ascending=[True, False])
    names: list[str] = []
    seen: set[str] = set()
    for name in work["model_name_zh"].astype(str).tolist():
        name = _pdf_human_text(name, fallback="模型名稱未完成")
        if name in seen:
            continue
        seen.add(name)
        names.append(name)
    return names


def _rows_for_model_section(df: pd.DataFrame, model_name: str, section: str, limit: int | None) -> pd.DataFrame:
    if df.empty:
        return df
    work = df[df["model_name_zh"].astype(str).map(lambda x: _pdf_human_text(x, fallback="模型名稱未完成") == model_name)].copy()
    if work.empty:
        return work
    if section == "repeated":
        work = work[work.apply(_repeat_key, axis=1).eq("repeated")]
    else:
        work = work[work.apply(_repeat_key, axis=1).eq("new")]
    if work.empty:
        return work
    work["_rank"] = work.apply(lambda row: _rank_sort_number(row, section), axis=1)
    work["_score"] = work.apply(_score_sort_number, axis=1)
    work = work.sort_values(["_rank", "_score"], ascending=[True, False])
    if limit is not None:
        work = work.head(limit)
    return work.drop(columns=["_rank", "_score"], errors="ignore")


def _summary_rows_for_section(df: pd.DataFrame, section: str) -> list[list[Any]]:
    rows = [["模型", "第一名標的", "分數", "榜別排名", "入選優點", "風險 / 操作提醒"]]
    if df.empty:
        rows.append(["資料不足", "-", "-", "-", "報告用欄位無資料", "資料不足 / 僅能觀察"])
        return rows
    for model_name in _model_names_in_report_order(df):
        picked = _rows_for_model_section(df, model_name, section, 1)
        if picked.empty:
            continue
        row = picked.iloc[0]
        rows.append(
            [
                _pdf_human_text(model_name, fallback="模型名稱未完成", limit=16),
                f"{safe_str(row.get('stock_id'))} {safe_str(row.get('stock_name'))}",
                _model_score_text(row.get("model_score")),
                _rank_for_section(row, section),
                _pdf_human_text(row.get("why_selected_human_zh"), row.get("why_selected_zh"), fallback="模型條件成立，細節請見個股頁。", limit=48),
                _pdf_human_text(row.get("operation_reminder_zh"), row.get("risk_tags_zh"), row.get("next_confirmation_zh"), row.get("recommended_usage_zh"), fallback="依支撐、壓力與量價失敗條件管理。", limit=48),
            ]
        )
    if len(rows) == 1:
        rows.append(["本段無資料", "-", "-", "-", f"今日沒有{_repeat_label(section)}資料", ""])
    return rows


def _load_model_summary_for_report() -> pd.DataFrame:
    df = read_csv_safe(MODEL_SUMMARY_FOR_REPORT_CSV, dtype=str, keep_default_na=False)
    if df.empty:
        return df
    if "model_registry_order" in df.columns:
        df["_order"] = pd.to_numeric(df["model_registry_order"], errors="coerce").fillna(9999)
        df = df.sort_values(["report_line", "_order", "model_name_zh"], kind="stable")
    return df


def _summary_stock_text(row: pd.Series, prefix: str) -> str:
    display = _pdf_human_text(row.get(f"{prefix}_signal_stock_display"), row.get(f"{prefix}_stock_display"), fallback="")
    if display and display != "資料不足 / 暫用現有資料":
        return display
    stock_id = safe_str(row.get(f"{prefix}_stock_id"))
    stock_name = safe_str(row.get(f"{prefix}_stock_name"))
    if stock_id or stock_name:
        return f"{stock_id} {stock_name}".strip()
    return "今日無候選"


def _summary_score_text(row: pd.Series, prefix: str) -> str:
    return _pdf_human_text(row.get(f"{prefix}_signal_model_score"), row.get(f"{prefix}_model_score"), fallback="-", limit=10)


def _summary_rank_text(row: pd.Series, prefix: str) -> str:
    if prefix == "new":
        return _pdf_human_text(row.get("new_signal_rank_label_zh"), row.get("new_rank_label"), fallback="-", limit=18)
    return _pdf_human_text(row.get("repeated_signal_rank_label_zh"), row.get("repeated_rank_label"), fallback="-", limit=18)


def _fixed_model_summary_rows(summary: pd.DataFrame, report_line: str) -> list[list[Any]]:
    rows = [[
        "模型",
        "新進榜第一名",
        "新進分數",
        "新進排名",
        "連續/累計第一名",
        "連續分數",
        "連續排名",
        "重點提醒",
    ]]
    if summary.empty:
        rows.append(["資料不足", "今日無候選", "-", "-", "今日無候選", "-", "-", "daily_candidate_model_summary_for_report_latest.csv 無資料。"])
        return rows
    part = summary[summary.get("report_line", "").astype(str).eq(report_line)].copy()
    if part.empty:
        rows.append(["資料不足", "今日無候選", "-", "-", "今日無候選", "-", "-", f"{report_line} 無模型摘要資料。"])
        return rows
    for _, row in part.iterrows():
        rows.append([
            _pdf_human_text(row.get("model_name_zh"), fallback="模型名稱尚未完成", limit=24),
            _summary_stock_text(row, "new"),
            _summary_score_text(row, "new"),
            _summary_rank_text(row, "new"),
            _summary_stock_text(row, "repeated"),
            _summary_score_text(row, "repeated"),
            _summary_rank_text(row, "repeated"),
            _pdf_human_text(row.get("operation_reminder_zh"), fallback="依程式端模型條件與風險欄位管理。", limit=58),
        ])
    return rows


def _detail_table_rows_for_section(df: pd.DataFrame, section: str) -> list[list[Any]]:
    rows = [["排名", "標的", "分數", "入選優點", "風險 / 操作提醒"]]
    if df.empty:
        rows.append(["-", "-", "-", "本段無資料", ""])
        return rows
    for _, row in df.iterrows():
        rows.append(
            [
                _rank_for_section(row, section),
                f"{safe_str(row.get('stock_id'))} {safe_str(row.get('stock_name'))}",
                _model_score_text(row.get("model_score")),
                _pdf_human_text(row.get("why_selected_human_zh"), row.get("why_selected_zh"), fallback="模型條件成立，細節請見個股頁。", limit=62),
                _pdf_human_text(row.get("operation_reminder_zh"), row.get("risk_tags_zh"), row.get("next_confirmation_zh"), row.get("recommended_usage_zh"), fallback="依支撐、壓力與量價失敗條件管理。", limit=62),
            ]
        )
    return rows


def _model_signal_card_readable(
    row: pd.Series,
    section: str,
    style_map: dict[str, ParagraphStyle],
    tech_map: dict[str, pd.Series],
    chart_map: dict[tuple[str, str], Path],
    include_chart: bool,
) -> KeepTogether:
    stock_id = safe_str(row.get("stock_id"))
    stock_name = safe_str(row.get("stock_name"))
    model_name = _pdf_human_text(row.get("model_name_zh"), fallback="模型名稱未完成")
    tech = tech_map.get(stock_id, pd.Series(dtype=object))
    title = f"{stock_id} {stock_name} / {model_name}"
    table_rows = [
        [para(title, style_map["curated_cell"]), para(f"{_repeat_label(section)} / {_rank_for_section(row, section)} / 分數 {_model_score_text(row.get('model_score'))}", style_map["curated_cell"])],
        [para("操作結論", style_map["label"]), para(_pdf_human_text(row.get("operation_reminder_zh"), row.get("recommended_usage_zh"), fallback="模型條件成立；後續依支撐、壓力、量價失敗與TDCC變化管理。"), style_map["curated_cell"])],
        [para("目前位置", style_map["label"]), para(_pdf_human_text(tech.get("price_position_summary_zh"), fallback="技術位置摘要尚未完成，請搭配K線與支撐壓力檢查。"), style_map["curated_cell"])],
        [para("技術狀態", style_map["label"]), para(_pdf_human_text(tech.get("technical_summary_zh"), fallback="技術指標摘要尚未完成，暫用K線圖判讀。"), style_map["curated_cell"])],
        [para("支撐 / 壓力", style_map["label"]), para(_pdf_human_text(tech.get("support_resistance_summary_zh"), fallback="支撐壓力摘要尚未完成，請以23EMA、平台與近期高低點管理。"), style_map["curated_cell"])],
        [para("入選優點", style_map["label"]), para(_pdf_human_text(row.get("why_selected_human_zh"), row.get("why_selected_zh"), fallback="模型條件成立。"), style_map["curated_cell"])],
        [para("買進條件", style_map["label"]), para(_pdf_human_text(tech.get("buy_condition_text_zh"), row.get("operation_reminder_zh"), fallback="依模型入選條件與隔日開盤後量價確認執行。"), style_map["curated_cell"])],
        [para("停利 / 退出", style_map["label"]), para(f"{_pdf_human_text(tech.get('take_profit_text_zh'), fallback='接近壓力或量價背離時分批停利。')} / {_pdf_human_text(tech.get('exit_condition_text_zh'), fallback='跌破關鍵支撐、23EMA或出現量價失敗時退出。')}", style_map["curated_cell"])],
        [para("主要風險", style_map["label"]), para(_pdf_human_text(row.get("risk_tags_zh"), row.get("tdcc_risk_text_zh"), row.get("downgrade_flags_zh"), fallback="風險標籤尚未完成，仍需檢查TDCC、權證、量價與市場背景。"), style_map["curated_cell"])],
        [para("TDCC / 權證 / 來源", style_map["label"]), para(f"{_pdf_human_text(row.get('tdcc_big_holder_summary_zh'), row.get('tdcc_status_zh'), fallback='TDCC摘要尚未完成')} / {_pdf_human_text(row.get('warrant_flow_signal_zh'), fallback='權證摘要尚未完成')} / {_pdf_human_text(row.get('source_hit_labels_zh'), fallback='來源標籤尚未完成')}", style_map["curated_cell"])],
    ]
    table = Table(table_rows, colWidths=[4.0 * cm, 12.8 * cm])
    table.setStyle(
        TableStyle(
            [
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
    parts: list[Any] = [table]
    if include_chart:
        chart_row = row.copy()
        chart_row["category"] = safe_str(row.get("original_category")) or safe_str(row.get("source_hit_labels"))
        chart_path = chart_map.get((stock_id, "")) or redraw_pdf_kline_chart_for_row(chart_row)
        if chart_path is not None and chart_path.exists():
            parts.extend([Spacer(1, 0.12 * cm), PdfImage(str(chart_path), width=16.6 * cm, height=8.2 * cm)])
    parts.append(Spacer(1, 0.22 * cm))
    return KeepTogether(parts)


def _append_theme_event_watch_section_readable(story: list[Any], style_map: dict[str, ParagraphStyle], compact: bool) -> None:
    events = read_csv_safe(LATEST_DIR / "theme_event_watch_latest.csv", dtype=str, keep_default_na=False)
    story.append(PageBreak())
    story.append(para("近期事件預警 / 主題催化觀察", style_map["h1"]))
    if events.empty:
        story.append(para("目前沒有可用的事件預警資料。若有展覽、法說、重大公告或主題催化，應進入 theme_event_watch_latest.csv 後再呈現。", style_map["normal"]))
        return
    rows = [["事件", "日期", "族群", "交集數", "相關候選", "解讀"]]
    limit = 8 if compact else 30
    for _, row in events.head(limit).iterrows():
        start_date = _pdf_human_text(row.get("event_start_date"), row.get("start_date"), fallback="")
        end_date = _pdf_human_text(row.get("event_end_date"), row.get("end_date"), fallback="")
        event_range = start_date if not end_date or end_date == start_date else f"{start_date}-{end_date}"
        rows.append(
            [
                _pdf_human_text(row.get("event_name"), fallback="事件名稱未完成", limit=24),
                clean_text(event_range, 18),
                _pdf_human_text(row.get("theme_tag"), fallback="族群標籤未完成", limit=18),
                _pdf_human_text(row.get("candidate_intersection_count"), fallback="0", limit=8),
                _pdf_human_text(row.get("top_candidate_summary_zh"), row.get("candidate_intersection_stock_names"), fallback="-", limit=42),
                _pdf_human_text(row.get("interpretation_zh"), row.get("theme_event_watch_status"), fallback="事件資料已建立，需觀察候選股與族群資金是否提前反應。", limit=58),
            ]
        )
    story.append(make_table(rows, style_map, [3.1 * cm, 2.0 * cm, 2.2 * cm, 1.5 * cm, 4.2 * cm, 5.2 * cm]))


def _append_group_rotation_section_readable(story: list[Any], style_map: dict[str, ParagraphStyle]) -> None:
    rotation = read_csv_safe(LATEST_DIR / "daily_candidate_group_rotation_latest.csv", dtype=str, keep_default_na=False)
    if rotation.empty:
        return
    story.append(PageBreak())
    story.append(para("族群資金輪動觀察", style_map["h1"]))
    story.append(para("這一段用來觀察同族群是否出現量能擴散，不是直接買進名單。", style_map["normal"]))
    rows = [["族群", "股票數", "3倍量檔數", "擴散比例", "龍頭 / 老二 / 老三", "解讀"]]
    for _, row in rotation.head(20).iterrows():
        rows.append(
            [
                _pdf_human_text(row.get("theme"), fallback="族群名稱未完成", limit=18),
                clean_text(row.get("stock_count", ""), 8),
                clean_text(row.get("volume_expansion_3x_count", ""), 8),
                clean_text(row.get("volume_expansion_ratio", ""), 8),
                clean_text(" / ".join([safe_str(row.get("leader_1")), safe_str(row.get("leader_2")), safe_str(row.get("leader_3"))]).strip(" /"), 36),
                _pdf_human_text(row.get("interpretation_zh"), row.get("interpretation"), fallback="資金擴散狀態待觀察。", limit=60),
            ]
        )
    story.append(make_table(rows, style_map, [2.5 * cm, 1.6 * cm, 1.8 * cm, 1.8 * cm, 4.1 * cm, 6.0 * cm]))


def build_model_line_pdf(report_line: str, full: bool, main_date: str, path: Path) -> None:
    style_map = styles()
    signals = load_model_report_signals()
    tech_map = load_technical_snapshot()
    chart_map = load_pdf_kline_chart_map()
    part = signals[signals.get("report_line", "").astype(str).eq(report_line)].copy() if not signals.empty else signals
    title_prefix = "主流股" if report_line == "mainstream" else "非主流股"
    title_suffix = "完整候選清單" if full else "每日推薦精華"
    doc = SimpleDocTemplate(
        str(path),
        pagesize=A4,
        leftMargin=1.5 * cm,
        rightMargin=1.5 * cm,
        topMargin=1.2 * cm,
        bottomMargin=1.2 * cm,
    )
    story: list[Any] = []
    story.append(para(f"{main_date} {title_prefix}{title_suffix}", style_map["title"]))
    story.append(para("資料來源：報告用模型訊號表；同一模型內分成新進榜與連續/累計進榜，並各自使用程式端排名。", style_map["subtitle"]))

    story.append(para("各模型新進榜第一名摘要", style_map["h1"]))
    story.append(make_table(_summary_rows_for_section(part, "new"), style_map, [2.8 * cm, 2.8 * cm, 1.4 * cm, 2.0 * cm, 5.2 * cm, 5.0 * cm]))
    story.append(Spacer(1, 0.25 * cm))
    story.append(para("各模型連續/累計進榜第一名摘要", style_map["h1"]))
    story.append(make_table(_summary_rows_for_section(part, "repeated"), style_map, [2.8 * cm, 2.8 * cm, 1.4 * cm, 2.0 * cm, 5.2 * cm, 5.0 * cm]))
    story.append(PageBreak())

    if full:
        story.append(para("完整模型名單", style_map["h1"]))
        limit = None
    else:
        story.append(para("各模型代表股分析", style_map["h1"]))
        limit = 5

    for model_name in _model_names_in_report_order(part):
        story.append(para(model_name, style_map["h2"]))
        for section in ["new", "repeated"]:
            group = _rows_for_model_section(part, model_name, section, limit)
            if group.empty:
                continue
            story.append(para(_repeat_label(section), style_map["h2"]))
            story.append(make_table(_detail_table_rows_for_section(group, section), style_map, [2.0 * cm, 2.6 * cm, 1.4 * cm, 6.0 * cm, 6.0 * cm]))
            if not full:
                story.append(Spacer(1, 0.18 * cm))
                for _, row in group.iterrows():
                    story.append(_model_signal_card_readable(row, section, style_map, tech_map, chart_map, include_chart=True))
            story.append(Spacer(1, 0.25 * cm))

    _append_theme_event_watch_section_readable(story, style_map, compact=not full)
    _append_group_rotation_section_readable(story, style_map)
    doc.build(story)


# Final PDF-facing renderer override.
# Keep this block immediately before copy_outputs(), so main() uses this clean
# implementation even if older experimental helpers above are still present.
PDF_DISPLAY_TOKEN_ZH_FINAL = {
    "range_rebound": "\u5340\u9593\u5167\u8f49\u5f37",
    "revenue_pullback": "\u71df\u6536\u6210\u9577\u80a1\u50f9\u56de\u6a94",
    "revenue_breakout_low_response": "\u71df\u6536\u7206\u767c\u4f46\u80a1\u50f9\u5c1a\u672a\u53cd\u61c9",
    "pullback_rebound": "\u56de\u6a94\u5f8c\u77ed\u7dda\u8f49\u5f37",
    "short_term_specialty": "\u77ed\u7dda\u5c08\u9805",
    "tdcc_short_term_edge": "TDCC\u77ed\u7dda\u5ef6\u7e8c",
    "hot_theme_pullback": "\u71b1\u9580\u65cf\u7fa4\u56de\u6a94",
    "price_pullback_23ema": "\u80a1\u50f9\u56de\u6a94",
    "tdcc_stealth_accumulation": "TDCC\u6f5b\u4f0f\u5438\u7c4c",
    "tdcc_short_term_continuation_d5_d10": "TDCC\u77ed\u7dda\u5ef6\u7e8c D+5/D+10",
    "volume_range_breakout": "\u5e36\u91cf\u7a81\u7834",
    "w_bottom_right_side": "W\u5e95\u53f3\u5074",
    "platform_strengthening": "\u5e73\u53f0\u6574\u7406\u8f49\u5f37",
    "near_high_neckline_challenge": "\u63a5\u8fd1\u524d\u9ad8/\u9838\u7dda\u6311\u6230",
    "new_model_signal": "\u65b0\u9032\u699c",
    "repeated_same_model_signal": "\u9023\u7e8c/\u7d2f\u8a08\u9032\u699c",
    "mainstream": "\u4e3b\u6d41",
    "non_mainstream": "\u975e\u4e3b\u6d41",
    "strong_accumulation": "\u5927\u6236\u5f37\u7d2f\u7a4d",
    "mild_accumulation": "\u5927\u6236\u6eab\u548c\u589e\u52a0",
    "distribution_warning": "\u5927\u6236\u8f49\u5f31\u8b66\u793a",
    "neutral": "\u4e2d\u6027",
    "call_strong_inflow": "\u8a8d\u8cfc\u660e\u78ba\u504f\u591a",
    "call_inflow": "\u8a8d\u8cfc\u504f\u591a",
    "call_put_bullish": "\u6b0a\u8b49\u504f\u591a",
    "mixed_flow": "\u6b0a\u8b49\u591a\u7a7a\u6df7\u5408",
    "no_signal": "\u7121\u660e\u78ba\u8a0a\u865f",
    "insufficient_data": "\u8cc7\u6599\u4e0d\u8db3",
    "neckline": "\u9838\u7dda",
    "breakout": "\u7a81\u7834",
    "hot_theme_tag": "\u71b1\u9580\u65cf\u7fa4\u6a19\u7c64",
    "hot theme tag": "\u71b1\u9580\u65cf\u7fa4\u6a19\u7c64",
}


def _pdf_human_text(*values: Any, fallback: str = "\u8cc7\u6599\u4e0d\u8db3 / \u66ab\u7528\u73fe\u6709\u8cc7\u6599", limit: int | None = None) -> str:
    text = ""
    for value in values:
        candidate = safe_str(value).strip()
        if candidate and candidate.lower() not in {"nan", "none", "null"}:
            text = candidate
            break
    if not text:
        text = fallback
    for raw, zh in PDF_DISPLAY_TOKEN_ZH_FINAL.items():
        text = re.sub(rf"(?<![A-Za-z0-9_]){re.escape(raw)}(?![A-Za-z0-9_])", zh, text)
    if re.fullmatch(r"[A-Za-z0-9_./ -]+", text or "") and "_" in text:
        text = fallback
    return clean_text(text, limit)


def _repeat_label(section: str) -> str:
    return "\u9023\u7e8c/\u7d2f\u8a08\u9032\u699c" if section == "repeated" else "\u65b0\u9032\u699c"


def _rank_for_section(row: pd.Series, section: str) -> str:
    fields = (
        ["display_rank_repeated_signal", "model_rank_repeated_signal", "display_rank", "model_rank"]
        if section == "repeated"
        else ["display_rank_new_signal", "model_rank_new_signal", "display_rank", "model_rank"]
    )
    rank = ""
    for field in fields:
        rank = safe_str(row.get(field)).strip()
        if rank:
            break
    if re.fullmatch(r"\d+(\.0+)?", rank or ""):
        rank = str(int(float(rank)))
    prefix = "\u9023\u7e8c\u699c#" if section == "repeated" else "\u65b0\u9032\u699c#"
    if rank and not rank.startswith(prefix):
        rank = f"{prefix}{rank}"
    return rank or "-"


def _rank_sort_number(row: pd.Series, section: str) -> float:
    fields = (
        ["model_rank_repeated_signal", "display_rank_repeated_signal", "display_rank", "model_rank"]
        if section == "repeated"
        else ["model_rank_new_signal", "display_rank_new_signal", "display_rank", "model_rank"]
    )
    for field in fields:
        text = safe_str(row.get(field))
        match = re.search(r"\d+", text)
        if match:
            return float(match.group(0))
    return 999999.0


def _score_sort_number(row: pd.Series) -> float:
    try:
        return float(safe_str(row.get("model_score")))
    except Exception:
        return -999999.0


def _model_score_text(value: Any) -> str:
    text = safe_str(value).strip()
    if not text:
        return "-"
    try:
        num = float(text)
        return f"{num:.1f}".rstrip("0").rstrip(".")
    except Exception:
        return clean_text(text, 10)


def _model_names_in_report_order(df: pd.DataFrame) -> list[str]:
    if df.empty or "model_name_zh" not in df.columns:
        return []
    work = df.copy()
    work["_rank"] = work.apply(lambda row: min(_rank_sort_number(row, "new"), _rank_sort_number(row, "repeated")), axis=1)
    work["_score"] = work.apply(_score_sort_number, axis=1)
    work = work.sort_values(["_rank", "_score"], ascending=[True, False])
    names: list[str] = []
    seen: set[str] = set()
    for name in work["model_name_zh"].astype(str).tolist():
        clean_name = _pdf_human_text(name, fallback="\u6a21\u578b\u540d\u7a31\u5c1a\u672a\u5b8c\u6210")
        if clean_name in seen:
            continue
        seen.add(clean_name)
        names.append(clean_name)
    return names


def _rows_for_model_section(df: pd.DataFrame, model_name: str, section: str, limit: int | None) -> pd.DataFrame:
    if df.empty:
        return df
    work = df[df["model_name_zh"].astype(str).map(lambda x: _pdf_human_text(x, fallback="\u6a21\u578b\u540d\u7a31\u5c1a\u672a\u5b8c\u6210")) == model_name].copy()
    work = work[work.apply(_repeat_key, axis=1).eq("repeated" if section == "repeated" else "new")]
    if work.empty:
        return work
    work["_rank"] = work.apply(lambda row: _rank_sort_number(row, section), axis=1)
    work["_score"] = work.apply(_score_sort_number, axis=1)
    work = work.sort_values(["_rank", "_score"], ascending=[True, False])
    if limit is not None:
        work = work.head(limit)
    return work.drop(columns=["_rank", "_score"], errors="ignore")


def _summary_rows_for_section(df: pd.DataFrame, section: str) -> list[list[Any]]:
    rows = [["\u6a21\u578b", "\u7b2c\u4e00\u540d\u6a19\u7684", "\u5206\u6578", "\u6392\u540d", "\u5165\u9078\u539f\u56e0", "\u98a8\u96aa/\u64cd\u4f5c\u63d0\u9192"]]
    if df.empty:
        rows.append(["\u8cc7\u6599\u4e0d\u8db3", "-", "-", "-", "\u5831\u544a\u7528\u6b04\u4f4d\u7121\u8cc7\u6599", "\u8cc7\u6599\u4e0d\u8db3 / \u50c5\u80fd\u89c0\u5bdf"])
        return rows
    for model_name in _model_names_in_report_order(df):
        picked = _rows_for_model_section(df, model_name, section, 1)
        if picked.empty:
            continue
        row = picked.iloc[0]
        rows.append(
            [
                _pdf_human_text(model_name, fallback="\u6a21\u578b\u540d\u7a31\u5c1a\u672a\u5b8c\u6210", limit=16),
                f"{safe_str(row.get('stock_id'))} {safe_str(row.get('stock_name'))}",
                _model_score_text(row.get("model_score")),
                _rank_for_section(row, section),
                _pdf_human_text(row.get("why_selected_human_zh"), row.get("why_selected_zh"), fallback="\u7b26\u5408\u6a21\u578b\u4e3b\u689d\u4ef6\uff0c\u7d30\u9805\u8acb\u770b\u5f8c\u7e8c\u500b\u80a1\u9801\u3002", limit=48),
                _pdf_human_text(row.get("operation_reminder_zh"), row.get("risk_tags_zh"), row.get("next_confirmation_zh"), row.get("recommended_usage_zh"), fallback="\u4f9d\u6a21\u578b\u689d\u4ef6\u7ba1\u7406\uff1b\u8dcc\u7834\u95dc\u9375\u652f\u6490\u6216\u91cf\u50f9\u5931\u6557\u9700\u964d\u4f4e\u90e8\u4f4d\u3002", limit=48),
            ]
        )
    if len(rows) == 1:
        rows.append(["\u672c\u6bb5\u7121\u6a19\u7684", "-", "-", "-", f"\u672c\u5831\u544a\u7dda\u6c92\u6709{_repeat_label(section)}\u8cc7\u6599", ""])
    return rows


def _detail_table_rows_for_section(df: pd.DataFrame, section: str) -> list[list[Any]]:
    rows = [["\u6392\u540d", "\u6a19\u7684", "\u5206\u6578", "\u5165\u9078\u539f\u56e0", "\u98a8\u96aa/\u64cd\u4f5c\u63d0\u9192"]]
    if df.empty:
        rows.append(["-", "-", "-", "\u672c\u6bb5\u7121\u6a19\u7684", ""])
        return rows
    for _, row in df.iterrows():
        rows.append(
            [
                _rank_for_section(row, section),
                f"{safe_str(row.get('stock_id'))} {safe_str(row.get('stock_name'))}",
                _model_score_text(row.get("model_score")),
                _pdf_human_text(row.get("why_selected_human_zh"), row.get("why_selected_zh"), fallback="\u7b26\u5408\u6a21\u578b\u4e3b\u689d\u4ef6\u3002", limit=62),
                _pdf_human_text(row.get("operation_reminder_zh"), row.get("risk_tags_zh"), row.get("next_confirmation_zh"), row.get("recommended_usage_zh"), fallback="\u4f9d\u95dc\u9375\u652f\u6490\u8207\u91cf\u50f9\u8b8a\u5316\u7ba1\u7406\u3002", limit=62),
            ]
        )
    return rows


def _model_signal_card_readable(
    row: pd.Series,
    section: str,
    style_map: dict[str, ParagraphStyle],
    tech_map: dict[str, pd.Series],
    chart_map: dict[tuple[str, str], Path],
    include_chart: bool,
) -> KeepTogether:
    stock_id = safe_str(row.get("stock_id"))
    stock_name = safe_str(row.get("stock_name"))
    model_name = _pdf_human_text(row.get("model_name_zh"), fallback="\u6a21\u578b\u540d\u7a31\u5c1a\u672a\u5b8c\u6210")
    tech = tech_map.get(stock_id, pd.Series(dtype=object))
    title = f"{stock_id} {stock_name} / {model_name}"
    take_profit_text = _pdf_human_text(
        tech.get("take_profit_text_zh"),
        fallback="\u63a5\u8fd1\u58d3\u529b\u6216\u91cf\u50f9\u5931\u6557\u6642\u5206\u6279\u505c\u5229\u3002",
    )
    exit_text = _pdf_human_text(
        tech.get("exit_condition_text_zh"),
        fallback="\u8dcc\u7834\u8fd1\u671f\u652f\u6490\u621623EMA\u7121\u6cd5\u6536\u56de\u6642\u9000\u51fa\u3002",
    )
    tdcc_text = _pdf_human_text(
        row.get("tdcc_big_holder_summary_zh"),
        row.get("tdcc_status_zh"),
        fallback="TDCC\u6458\u8981\u5c1a\u672a\u5b8c\u6210",
    )
    warrant_text = _pdf_human_text(
        row.get("warrant_flow_signal_zh"),
        fallback="\u6b0a\u8b49\u6458\u8981\u5c1a\u672a\u5b8c\u6210",
    )
    source_text = _pdf_human_text(
        row.get("source_hit_labels_zh"),
        fallback="\u4f86\u6e90\u6a19\u7c64\u5c1a\u672a\u5b8c\u6210",
    )
    table_rows = [
        [para(title, style_map["curated_cell"]), para(f"{_repeat_label(section)} / {_rank_for_section(row, section)} / \u5206\u6578 {_model_score_text(row.get('model_score'))}", style_map["curated_cell"])],
        [para("\u64cd\u4f5c\u7d50\u8ad6", style_map["label"]), para(_pdf_human_text(row.get("operation_reminder_zh"), row.get("recommended_usage_zh"), fallback="\u7b26\u5408\u6a21\u578b\u689d\u4ef6\uff0c\u4ee5\u95dc\u9375\u652f\u6490\u3001\u91cf\u50f9\u8207TDCC\u8b8a\u5316\u7ba1\u7406\u3002"), style_map["curated_cell"])],
        [para("\u76ee\u524d\u4f4d\u7f6e", style_map["label"]), para(_pdf_human_text(tech.get("price_position_summary_zh"), fallback="\u4f4d\u7f6e\u6458\u8981\u6b04\u4f4d\u5c1a\u672a\u5b8c\u6210\uff0c\u8acb\u4ee5K\u7dda\u5716\u8207\u652f\u6490\u58d3\u529b\u5c0d\u7167\u3002"), style_map["curated_cell"])],
        [para("\u6280\u8853\u72c0\u614b", style_map["label"]), para(_pdf_human_text(tech.get("technical_summary_zh"), fallback="\u6280\u8853\u6458\u8981\u6b04\u4f4d\u5c1a\u672a\u5b8c\u6210\uff0c\u66ab\u7528K\u7dda\u8207\u91cf\u50f9\u5224\u8b80\u3002"), style_map["curated_cell"])],
        [para("\u652f\u6490/\u58d3\u529b", style_map["label"]), para(_pdf_human_text(tech.get("support_resistance_summary_zh"), fallback="\u652f\u6490\u58d3\u529b\u7531\u5716\u9762\u6a19\u793a\uff0c\u512a\u5148\u770b23EMA\u3001\u5e73\u53f0\u8207\u524d\u9ad8\u58d3\u529b\u3002"), style_map["curated_cell"])],
        [para("\u5165\u9078\u539f\u56e0", style_map["label"]), para(_pdf_human_text(row.get("why_selected_human_zh"), row.get("why_selected_zh"), fallback="\u7b26\u5408\u6a21\u578b\u4e3b\u689d\u4ef6\u3002"), style_map["curated_cell"])],
        [para("\u8cb7\u9032\u689d\u4ef6", style_map["label"]), para(_pdf_human_text(tech.get("buy_condition_text_zh"), row.get("operation_reminder_zh"), fallback="\u7b26\u5408\u6a21\u578b\u689d\u4ef6\u5f8c\uff0c\u4ee5\u4e0d\u8dcc\u7834\u95dc\u9375\u652f\u6490\u8207\u91cf\u50f9\u7e8c\u5f37\u7ba1\u7406\u3002"), style_map["curated_cell"])],
        [para("\u505c\u5229/\u9000\u51fa", style_map["label"]), para(f"{take_profit_text} / {exit_text}", style_map["curated_cell"])],
        [para("\u4e3b\u8981\u98a8\u96aa", style_map["label"]), para(_pdf_human_text(row.get("risk_tags_zh"), row.get("tdcc_risk_text_zh"), row.get("downgrade_flags_zh"), fallback="\u98a8\u96aa\u6a19\u7c64\u5c1a\u672a\u5b8c\u6210\uff0c\u4ee5\u91cf\u50f9\u3001TDCC\u8207\u652f\u6490\u5931\u5b88\u7ba1\u7406\u3002"), style_map["curated_cell"])],
        [para("TDCC / \u6b0a\u8b49 / \u4f86\u6e90", style_map["label"]), para(f"{tdcc_text} / {warrant_text} / {source_text}", style_map["curated_cell"])],
    ]
    table = Table(table_rows, colWidths=[4.0 * cm, 12.8 * cm])
    table.setStyle(TableStyle([("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#EAF2F8")), ("GRID", (0, 0), (-1, -1), 0.25, colors.HexColor("#CFD8E3")), ("VALIGN", (0, 0), (-1, -1), "TOP"), ("LEFTPADDING", (0, 0), (-1, -1), 6), ("RIGHTPADDING", (0, 0), (-1, -1), 6), ("TOPPADDING", (0, 0), (-1, -1), 5), ("BOTTOMPADDING", (0, 0), (-1, -1), 5)]))
    parts: list[Any] = [table]
    if include_chart:
        chart_row = row.copy()
        chart_row["category"] = safe_str(row.get("original_category")) or safe_str(row.get("source_hit_labels"))
        chart_path = chart_map.get((stock_id, "")) or redraw_pdf_kline_chart_for_row(chart_row)
        if chart_path is not None and chart_path.exists():
            parts.extend([Spacer(1, 0.12 * cm), PdfImage(str(chart_path), width=16.6 * cm, height=8.2 * cm)])
    parts.append(Spacer(1, 0.22 * cm))
    return KeepTogether(parts)


def _append_theme_event_watch_section_readable(story: list[Any], style_map: dict[str, ParagraphStyle], compact: bool) -> None:
    events = read_csv_safe(LATEST_DIR / "theme_event_watch_latest.csv", dtype=str, keep_default_na=False)
    story.append(PageBreak())
    story.append(para("\u8fd1\u671f\u4e8b\u4ef6\u9810\u8b66 / \u4e3b\u984c\u50ac\u5316\u89c0\u5bdf", style_map["h1"]))
    if events.empty:
        story.append(para("\u76ee\u524d\u7121\u53ef\u986f\u793a\u7684\u4e8b\u4ef6\u9810\u8b66\u8cc7\u6599\uff1b\u82e5\u6709\u65b0\u4e8b\u4ef6\uff0c\u8acb\u88dc\u5165 theme_event_watch_latest.csv \u6216\u4e8b\u4ef6\u884c\u4e8b\u66c6\u3002", style_map["normal"]))
        return
    rows = [["\u4e8b\u4ef6", "\u65e5\u671f", "\u65cf\u7fa4", "\u4ea4\u96c6\u6578", "\u76f8\u95dc\u6a19\u7684", "\u89e3\u8b80"]]
    limit = 8 if compact else 30
    for _, row in events.head(limit).iterrows():
        start_date = _pdf_human_text(row.get("event_start_date"), row.get("start_date"), fallback="")
        end_date = _pdf_human_text(row.get("event_end_date"), row.get("end_date"), fallback="")
        event_range = start_date if not end_date or end_date == start_date else f"{start_date}-{end_date}"
        rows.append([
            _pdf_human_text(row.get("event_name"), fallback="\u4e8b\u4ef6\u540d\u7a31\u5c1a\u672a\u5b8c\u6210", limit=24),
            clean_text(event_range, 18),
            _pdf_human_text(row.get("theme_tag"), fallback="\u65cf\u7fa4\u6a19\u7c64\u5c1a\u672a\u5b8c\u6210", limit=18),
            _pdf_human_text(row.get("candidate_intersection_count"), fallback="0", limit=8),
            _pdf_human_text(row.get("top_candidate_summary_zh"), row.get("candidate_intersection_stock_names"), fallback="-", limit=42),
            _pdf_human_text(row.get("interpretation_zh"), row.get("theme_event_watch_status"), fallback="\u4e8b\u4ef6\u8cc7\u6599\u5df2\u5217\u5165\u89c0\u5bdf\uff0c\u9700\u5c0d\u7167\u65cf\u7fa4\u8cc7\u91d1\u662f\u5426\u64f4\u6563\u3002", limit=58),
        ])
    story.append(make_table(rows, style_map, [3.1 * cm, 2.0 * cm, 2.2 * cm, 1.5 * cm, 4.2 * cm, 5.2 * cm]))


def _append_group_rotation_section_readable(story: list[Any], style_map: dict[str, ParagraphStyle]) -> None:
    rotation = read_csv_safe(LATEST_DIR / "daily_candidate_group_rotation_latest.csv", dtype=str, keep_default_na=False)
    if rotation.empty:
        return
    story.append(PageBreak())
    story.append(para("\u65cf\u7fa4\u8cc7\u91d1\u8f2a\u52d5\u89c0\u5bdf", style_map["h1"]))
    story.append(para("\u672c\u7bc0\u53ea\u5224\u8b80\u65cf\u7fa4\u51fa\u91cf\u64f4\u6563\uff0c\u4e0d\u76f4\u63a5\u7576\u500b\u80a1\u8cb7\u9032\u7406\u7531\u3002", style_map["normal"]))
    rows = [["\u65cf\u7fa4", "\u6a94\u6578", "3\u500d\u91cf\u6a94\u6578", "\u64f4\u6563\u6bd4\u4f8b", "\u9f8d\u982d/\u8001\u4e8c/\u8001\u4e09", "\u89e3\u8b80"]]
    for _, row in rotation.head(20).iterrows():
        rows.append([
            _pdf_human_text(row.get("theme"), fallback="\u65cf\u7fa4\u5c1a\u672a\u5b8c\u6210", limit=18),
            clean_text(row.get("stock_count", ""), 8),
            clean_text(row.get("volume_expansion_3x_count", ""), 8),
            clean_text(row.get("volume_expansion_ratio", ""), 8),
            clean_text(" / ".join([safe_str(row.get("leader_1")), safe_str(row.get("leader_2")), safe_str(row.get("leader_3"))]).strip(" /"), 36),
            _pdf_human_text(row.get("interpretation_zh"), row.get("interpretation"), fallback="\u8cc7\u91d1\u64f4\u6563\u72c0\u614b\u5c1a\u672a\u5b8c\u6210\u3002", limit=60),
        ])
    story.append(make_table(rows, style_map, [2.5 * cm, 1.6 * cm, 1.8 * cm, 1.8 * cm, 4.1 * cm, 6.0 * cm]))


def build_model_line_pdf(report_line: str, full: bool, main_date: str, path: Path) -> None:
    style_map = styles()
    signals = load_model_report_signals()
    model_summary = _load_model_summary_for_report()
    tech_map = load_technical_snapshot()
    chart_map = load_pdf_kline_chart_map()
    part = signals[signals.get("report_line", "").astype(str).eq(report_line)].copy() if not signals.empty else signals
    title_prefix = "\u4e3b\u6d41\u80a1" if report_line == "mainstream" else "\u975e\u4e3b\u6d41\u80a1"
    title_suffix = "\u5b8c\u6574\u5019\u9078\u6e05\u55ae" if full else "\u6bcf\u65e5\u63a8\u85a6\u7cbe\u83ef"
    doc = SimpleDocTemplate(str(path), pagesize=A4, leftMargin=1.5 * cm, rightMargin=1.5 * cm, topMargin=1.2 * cm, bottomMargin=1.2 * cm)
    story: list[Any] = []
    story.append(para(f"{main_date} {title_prefix}{title_suffix}", style_map["title"]))
    story.append(para("資料來源：報告用模型訊號表；同一模型內分成新進榜與連續/累計進榜，並各自使用程式端排名。", style_map["subtitle"]))
    story.append(para("各模型新進榜 / 連續榜固定摘要", style_map["h1"]))
    story.append(make_table(_fixed_model_summary_rows(model_summary, report_line), style_map, [2.5 * cm, 2.2 * cm, 1.25 * cm, 1.45 * cm, 2.2 * cm, 1.25 * cm, 1.45 * cm, 5.2 * cm]))
    story.append(PageBreak())
    limit = None if full else 5
    story.append(para("\u5b8c\u6574\u6a21\u578b\u6e05\u55ae" if full else "\u5404\u6a21\u578b\u4ee3\u8868\u80a1\u5206\u6790", style_map["h1"]))
    for model_name in _model_names_in_report_order(part):
        story.append(para(model_name, style_map["h2"]))
        for section in ["new", "repeated"]:
            group = _rows_for_model_section(part, model_name, section, limit)
            if group.empty:
                continue
            story.append(para(_repeat_label(section), style_map["h2"]))
            story.append(make_table(_detail_table_rows_for_section(group, section), style_map, [2.0 * cm, 2.6 * cm, 1.4 * cm, 6.0 * cm, 6.0 * cm]))
            if not full:
                story.append(Spacer(1, 0.18 * cm))
                for _, row in group.iterrows():
                    story.append(_model_signal_card_readable(row, section, style_map, tech_map, chart_map, include_chart=True))
            story.append(Spacer(1, 0.25 * cm))
    _append_theme_event_watch_section_readable(story, style_map, compact=not full)
    _append_group_rotation_section_readable(story, style_map)
    doc.build(story)


def copy_outputs(main_date: str) -> dict[str, str]:
    DOCS_LATEST_DIR.mkdir(parents=True, exist_ok=True)
    HISTORY_REPORT_DIR.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(CURATED_PDF, DOCS_CURATED_PDF)
    shutil.copyfile(FULL_TABLE_PDF, DOCS_FULL_TABLE_PDF)
    model_pdf_pairs = [
        (MAINSTREAM_CURATED_PDF, DOCS_MAINSTREAM_CURATED_PDF, f"{main_date}_mainstream_daily_recommendation_highlight.pdf", "history_mainstream_curated_pdf"),
        (MAINSTREAM_FULL_PDF, DOCS_MAINSTREAM_FULL_PDF, f"{main_date}_mainstream_full_candidate_list.pdf", "history_mainstream_full_pdf"),
        (NON_MAINSTREAM_CURATED_PDF, DOCS_NON_MAINSTREAM_CURATED_PDF, f"{main_date}_non_mainstream_daily_recommendation_highlight.pdf", "history_non_mainstream_curated_pdf"),
        (NON_MAINSTREAM_FULL_PDF, DOCS_NON_MAINSTREAM_FULL_PDF, f"{main_date}_non_mainstream_full_candidate_list.pdf", "history_non_mainstream_full_pdf"),
    ]
    history_curated = HISTORY_REPORT_DIR / f"{main_date}_daily_market_curated_report.pdf"
    history_full = HISTORY_REPORT_DIR / f"{main_date}_daily_market_full_table_report.pdf"
    shutil.copyfile(CURATED_PDF, history_curated)
    shutil.copyfile(FULL_TABLE_PDF, history_full)
    result = {
        "history_curated_pdf": history_curated.as_posix(),
        "history_full_table_pdf": history_full.as_posix(),
    }
    for src, docs_dst, history_name, key in model_pdf_pairs:
        if not src.exists():
            continue
        shutil.copyfile(src, docs_dst)
        history_path = HISTORY_REPORT_DIR / history_name
        shutil.copyfile(src, history_path)
        result[key] = history_path.as_posix()
    return result


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
        "model_line_pdfs": {
            "mainstream_curated": {
                "status": "generated" if MAINSTREAM_CURATED_PDF.exists() else "missing",
                "file_path": MAINSTREAM_CURATED_PDF.as_posix(),
                "docs_path": DOCS_MAINSTREAM_CURATED_PDF.as_posix(),
                "pages_url": pages_url(DOCS_MAINSTREAM_CURATED_PDF),
                "raw_url": raw_url(MAINSTREAM_CURATED_PDF),
                "history_path": history_paths.get("history_mainstream_curated_pdf", ""),
            },
            "mainstream_full": {
                "status": "generated" if MAINSTREAM_FULL_PDF.exists() else "missing",
                "file_path": MAINSTREAM_FULL_PDF.as_posix(),
                "docs_path": DOCS_MAINSTREAM_FULL_PDF.as_posix(),
                "pages_url": pages_url(DOCS_MAINSTREAM_FULL_PDF),
                "raw_url": raw_url(MAINSTREAM_FULL_PDF),
                "history_path": history_paths.get("history_mainstream_full_pdf", ""),
            },
            "non_mainstream_curated": {
                "status": "generated" if NON_MAINSTREAM_CURATED_PDF.exists() else "missing",
                "file_path": NON_MAINSTREAM_CURATED_PDF.as_posix(),
                "docs_path": DOCS_NON_MAINSTREAM_CURATED_PDF.as_posix(),
                "pages_url": pages_url(DOCS_NON_MAINSTREAM_CURATED_PDF),
                "raw_url": raw_url(NON_MAINSTREAM_CURATED_PDF),
                "history_path": history_paths.get("history_non_mainstream_curated_pdf", ""),
            },
            "non_mainstream_full": {
                "status": "generated" if NON_MAINSTREAM_FULL_PDF.exists() else "missing",
                "file_path": NON_MAINSTREAM_FULL_PDF.as_posix(),
                "docs_path": DOCS_NON_MAINSTREAM_FULL_PDF.as_posix(),
                "pages_url": pages_url(DOCS_NON_MAINSTREAM_FULL_PDF),
                "raw_url": raw_url(NON_MAINSTREAM_FULL_PDF),
                "history_path": history_paths.get("history_non_mainstream_full_pdf", ""),
            },
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
        "## Model-Line PDFs",
        f"- mainstream_curated_pages_url: {manifest['model_line_pdfs']['mainstream_curated']['pages_url']}",
        f"- mainstream_full_pages_url: {manifest['model_line_pdfs']['mainstream_full']['pages_url']}",
        f"- non_mainstream_curated_pages_url: {manifest['model_line_pdfs']['non_mainstream_curated']['pages_url']}",
        f"- non_mainstream_full_pages_url: {manifest['model_line_pdfs']['non_mainstream_full']['pages_url']}",
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
    build_model_line_pdf("mainstream", False, main_date, MAINSTREAM_CURATED_PDF)
    build_model_line_pdf("mainstream", True, main_date, MAINSTREAM_FULL_PDF)
    build_model_line_pdf("non_mainstream", False, main_date, NON_MAINSTREAM_CURATED_PDF)
    build_model_line_pdf("non_mainstream", True, main_date, NON_MAINSTREAM_FULL_PDF)
    history_paths = copy_outputs(main_date)
    write_manifest(main_date, freshness, history_paths)

    print(f"Saved: {CURATED_PDF}")
    print(f"Saved: {DOCS_CURATED_PDF}")
    print(f"Saved: {FULL_TABLE_PDF}")
    print(f"Saved: {DOCS_FULL_TABLE_PDF}")
    print(f"Saved: {MAINSTREAM_CURATED_PDF}")
    print(f"Saved: {MAINSTREAM_FULL_PDF}")
    print(f"Saved: {NON_MAINSTREAM_CURATED_PDF}")
    print(f"Saved: {NON_MAINSTREAM_FULL_PDF}")
    print(f"Saved: {MANIFEST_JSON}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
