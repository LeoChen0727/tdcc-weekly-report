from __future__ import annotations

from pathlib import Path
from datetime import datetime
from zoneinfo import ZoneInfo
import json
import math
import re
import shutil
from urllib.parse import quote

import pandas as pd

from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT, TA_CENTER
from reportlab.lib.pagesizes import A4, landscape
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import cm
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle,
    PageBreak,
    Image,
)
from reportlab.pdfbase.cidfonts import UnicodeCIDFont
from reportlab.pdfbase import pdfmetrics


LATEST_DIR = Path("output/latest")
HISTORY_REPORT_DIR = Path("output/history/reports")

DATA_FRESHNESS_CSV = LATEST_DIR / "data_freshness_latest.csv"
DATA_FRESHNESS_MD = LATEST_DIR / "data_freshness_latest.md"
ALL_CANDIDATES_CSV = LATEST_DIR / "all_candidates_latest.csv"
CHART_MANIFEST_CSV = LATEST_DIR / "chart_manifest.csv"

LATEST_SUMMARY_MD = LATEST_DIR / "每日全市場候選股監測報告_精華版.md"
LATEST_SUMMARY_PDF = LATEST_DIR / "每日全市場候選股監測報告_精華版.pdf"
LATEST_FULL_MD = LATEST_DIR / "完整候選股清單_完整版.md"
LATEST_FULL_PDF = LATEST_DIR / "完整候選股清單_完整版表格.pdf"

MANIFEST_JSON = LATEST_DIR / "report_manifest_latest.json"
MANIFEST_MD = LATEST_DIR / "report_manifest_latest.md"

GITHUB_RAW_PREFIX = "https://raw.githubusercontent.com/LeoChen0727/tdcc-weekly-report/main/"

CATEGORY_ORDER = [
    "true_breakout",
    "range_rebound",
    "near_resistance",
    "abnormal_volume_up",
    "revenue_breakout_low_response",
    "revenue_pullback",
    "pullback_rebound",
    "pattern",
]

CATEGORY_CN = {
    "true_breakout": "嚴格突破",
    "range_rebound": "區間內轉強 / 挑戰前高觀察",
    "near_resistance": "區間內轉強 / 挑戰前高觀察",
    "abnormal_volume_up": "區間內轉強 / 挑戰前高觀察",
    "revenue_breakout_low_response": "營收爆發低反應股",
    "revenue_pullback": "營收成長股價回檔",
    "pullback_rebound": "回檔後短線轉強",
    "pattern": "型態觀察",
}

SUMMARY_LIMIT_BY_CATEGORY = {
    "true_breakout": 5,
    "range_rebound": 5,
    "near_resistance": 5,
    "abnormal_volume_up": 5,
    "revenue_breakout_low_response": 5,
    "revenue_pullback": 5,
    "pullback_rebound": 5,
    "pattern": 5,
}

FULL_PDF_ROWS_PER_PAGE = 18

FULL_PDF_COLUMN_CONFIG = {
    "true_breakout": {
        "headers": ["股票", "族群", "分數", "排名", "突破型態", "量能", "TDCC", "權證", "簡短原因"],
        "widths": [3.0, 3.1, 1.4, 1.4, 2.6, 2.0, 3.0, 4.0, 7.2],
    },
    "range_rebound": {
        "headers": ["股票", "族群", "分數", "排名", "轉強型態", "距前高", "TDCC", "權證", "簡短原因"],
        "widths": [3.0, 3.1, 1.4, 1.4, 2.6, 2.0, 3.0, 4.0, 7.2],
    },
    "near_resistance": {
        "headers": ["股票", "族群", "分數", "排名", "轉強型態", "距前高", "TDCC", "權證", "簡短原因"],
        "widths": [3.0, 3.1, 1.4, 1.4, 2.6, 2.0, 3.0, 4.0, 7.2],
    },
    "abnormal_volume_up": {
        "headers": ["股票", "族群", "分數", "排名", "轉強型態", "量能", "TDCC", "權證", "簡短原因"],
        "widths": [3.0, 3.1, 1.4, 1.4, 2.6, 2.0, 3.0, 4.0, 7.2],
    },
    "revenue_breakout_low_response": {
        "headers": ["股票", "族群", "分數", "排名", "優先級", "營收YoY", "TDCC趨勢", "權證", "簡短原因"],
        "widths": [3.0, 3.1, 1.4, 1.4, 2.8, 2.4, 3.2, 4.0, 6.8],
    },
    "revenue_pullback": {
        "headers": ["股票", "族群", "分數", "排名", "營收YoY", "距均線", "TDCC", "權證", "簡短原因"],
        "widths": [3.0, 3.1, 1.4, 1.4, 2.4, 2.2, 3.0, 4.0, 7.0],
    },
    "pullback_rebound": {
        "headers": ["股票", "族群", "分數", "排名", "轉強訊號", "距均線", "TDCC", "權證", "簡短原因"],
        "widths": [3.0, 3.1, 1.4, 1.4, 2.8, 2.2, 3.0, 4.0, 6.6],
    },
    "pattern": {
        "headers": ["股票", "族群", "分數", "排名", "型態訊號", "型態狀態", "TDCC", "權證", "簡短原因"],
        "widths": [3.0, 3.1, 1.4, 1.4, 2.8, 2.4, 3.0, 4.0, 6.4],
    },
    "default": {
        "headers": ["股票", "族群", "分數", "排名", "分類", "TDCC", "權證", "簡短原因"],
        "widths": [3.0, 3.2, 1.4, 1.4, 3.0, 3.0, 4.0, 8.0],
    },
}


def now_taipei() -> str:
    return datetime.now(ZoneInfo("Asia/Taipei")).strftime("%Y-%m-%d %H:%M:%S")


def safe_str(value) -> str:
    if value is None:
        return ""
    try:
        if pd.isna(value):
            return ""
    except Exception:
        pass
    text = str(value)
    if text.lower() in ["nan", "none", "<na>"]:
        return ""
    return text.strip()


def safe_float(value, default=math.nan) -> float:
    try:
        if pd.isna(value):
            return default
        return float(value)
    except Exception:
        return default


def normalize_date(value) -> str:
    text = safe_str(value)
    digits = re.sub(r"[^0-9]", "", text)
    if len(digits) >= 8:
        return digits[:8]
    return ""


def raw_url_for_path(path: str | Path) -> str:
    path_text = safe_str(path).replace("\\", "/").lstrip("/")
    return GITHUB_RAW_PREFIX + quote(path_text, safe="/")


def read_csv(path: Path) -> pd.DataFrame:
    if not path.exists():
        return pd.DataFrame()
    try:
        return pd.read_csv(path, dtype=str)
    except Exception as exc:
        print(f"Failed to read {path}: {exc}")
        return pd.DataFrame()


def get_main_price_date() -> tuple[str, bool, dict]:
    meta = {
        "generated_at": now_taipei(),
        "main_price_date": "",
        "report_ready": False,
        "stock_monitor_price_date": "",
        "all_candidates_date": "",
        "official_price_fetch_date": "",
        "warrant_flow_date": "",
        "report_ready_note": "",
    }

    freshness = read_csv(DATA_FRESHNESS_CSV)

    if not freshness.empty:
        row = freshness.iloc[0].to_dict()

        for key in meta:
            if key in row:
                meta[key] = row[key]

        main_date = normalize_date(meta.get("main_price_date", ""))
        report_ready = safe_str(meta.get("report_ready", "")).lower() in ["true", "1", "yes"]

        meta["main_price_date"] = main_date
        meta["report_ready"] = report_ready

        return main_date, report_ready, meta

    candidates = read_csv(ALL_CANDIDATES_CSV)

    if not candidates.empty and "date" in candidates.columns:
        dates = candidates["date"].map(normalize_date)
        dates = dates[dates.astype(str).str.len() == 8]

        if not dates.empty:
            main_date = str(dates.max())
            meta["main_price_date"] = main_date
            meta["all_candidates_date"] = main_date
            meta["report_ready"] = True
            meta["report_ready_note"] = "data_freshness_latest.csv 不存在，改用 all_candidates_latest.csv date 最大值"
            return main_date, True, meta

    meta["report_ready_note"] = "無法判斷主資料日期"
    return "", False, meta


def load_candidates() -> pd.DataFrame:
    df = read_csv(ALL_CANDIDATES_CSV)

    if df.empty:
        return df

    rename_map = {}

    if "stock_id" not in df.columns:
        for col in ["ticker", "code", "股票代號"]:
            if col in df.columns:
                rename_map[col] = "stock_id"
                break

    if "stock_name" not in df.columns:
        for col in ["name", "股票名稱", "證券名稱"]:
            if col in df.columns:
                rename_map[col] = "stock_name"
                break

    if rename_map:
        df = df.rename(columns=rename_map)

    if "stock_id" not in df.columns:
        df["stock_id"] = ""

    if "stock_name" not in df.columns:
        df["stock_name"] = ""

    if "category" not in df.columns:
        df["category"] = "unknown"

    if "category_cn" not in df.columns:
        df["category_cn"] = df["category"].map(lambda x: CATEGORY_CN.get(safe_str(x), safe_str(x)))

    if "note" not in df.columns:
        df["note"] = ""

    if "細分族群" not in df.columns:
        df["細分族群"] = ""

    for col in ["score", "rank", "warrant_flow_score"]:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors="coerce")

    df["stock_id"] = df["stock_id"].astype(str).str.zfill(4)

    return df


def load_chart_manifest() -> pd.DataFrame:
    df = read_csv(CHART_MANIFEST_CSV)

    if df.empty:
        return df

    if "stock_id" not in df.columns:
        for col in ["ticker", "code", "股票代號"]:
            if col in df.columns:
                df = df.rename(columns={col: "stock_id"})
                break

    if "stock_id" in df.columns:
        df["stock_id"] = df["stock_id"].astype(str).str.zfill(4)

    return df


def choose_chart_path(row: pd.Series, chart_manifest: pd.DataFrame) -> str:
    for col in ["chart_path", "chart_url"]:
        value = safe_str(row.get(col, ""))
        if value:
            if value.startswith("http"):
                return value
            if Path(value).exists():
                return value

    if chart_manifest.empty or "stock_id" not in chart_manifest.columns:
        return ""

    stock_id = safe_str(row.get("stock_id", "")).zfill(4)
    category = safe_str(row.get("category", ""))

    part = chart_manifest[chart_manifest["stock_id"].astype(str).str.zfill(4) == stock_id].copy()

    if part.empty:
        return ""

    if "category" in part.columns and category:
        same_category = part[part["category"].astype(str) == category]
        if not same_category.empty:
            part = same_category

    for col in ["chart_path", "path", "chart_url"]:
        if col in part.columns:
            value = safe_str(part.iloc[0].get(col, ""))
            if value:
                return value

    return ""


def clean_reason(text: str, limit: int = 80) -> str:
    text = safe_str(text)
    text = text.replace("\n", " ").replace("|", "/")
    text = re.sub(r"\s+", " ", text)
    if len(text) > limit:
        return text[:limit] + "..."
    return text


def build_reason(row: pd.Series, limit: int = 90) -> str:
    parts = []

    priority = safe_str(row.get("revaluation_priority", ""))
    if priority:
        parts.append(priority)

    for col in [
        "tdcc_accumulation_note",
        "tdcc_judgement",
        "warrant_flow_signal",
        "warrant_flow_warning",
        "warrant_note",
        "note",
    ]:
        value = safe_str(row.get(col, ""))
        if value:
            parts.append(value)

    if not parts:
        for col in [
            "revenue_acceleration_note",
            "pattern_signal",
            "breakout_type",
            "category_cn",
        ]:
            value = safe_str(row.get(col, ""))
            if value:
                parts.append(value)

    reason = "；".join(parts)
    reason = reason.replace("\n", " ").replace("|", "/")
    reason = re.sub(r"\s+", " ", reason)

    if len(reason) > limit:
        reason = reason[:limit] + "..."

    return reason


def tdcc_short(row: pd.Series) -> str:
    for col in ["tdcc_accumulation_signal", "tdcc_judgement", "tdcc_accumulation_note"]:
        value = safe_str(row.get(col, ""))
        if value:
            return clean_reason(value, 28)
    return ""


def warrant_short(row: pd.Series) -> str:
    signal = safe_str(row.get("warrant_flow_signal", ""))
    score = safe_str(row.get("warrant_flow_score", ""))

    if signal and score:
        return f"{signal} / {score}"

    return signal or score


def theme_short(row: pd.Series) -> str:
    return (
        safe_str(row.get("細分族群", ""))
        or safe_str(row.get("theme_note", ""))
        or safe_str(row.get("industry", ""))
        or ""
    )


def breakout_type_short(row: pd.Series) -> str:
    value = safe_str(row.get("breakout_type", ""))
    if value:
        return clean_reason(value, 22)

    value = safe_str(row.get("category", ""))
    return clean_reason(value, 22)


def volume_short(row: pd.Series) -> str:
    volume_ratio = safe_str(row.get("volume_ratio", ""))
    volume_ratio_20 = safe_str(row.get("volume_ratio_20", ""))

    if volume_ratio:
        return f"{volume_ratio}x"

    if volume_ratio_20:
        return f"{volume_ratio_20}x"

    return ""


def distance_high_short(row: pd.Series) -> str:
    for col in [
        "distance_to_previous_high_pct",
        "distance_to_previous_60d_high_pct",
        "distance_to_high_60_pct",
    ]:
        value = safe_str(row.get(col, ""))
        if value:
            return f"{value}%"
    return ""


def revenue_yoy_short(row: pd.Series) -> str:
    latest = safe_str(row.get("latest_revenue_yoy", ""))
    cumulative = safe_str(row.get("cumulative_revenue_yoy", ""))

    if latest and cumulative:
        return f"單月{latest}% / 累計{cumulative}%"

    if latest:
        return f"單月{latest}%"

    if cumulative:
        return f"累計{cumulative}%"

    return ""


def ma_distance_short(row: pd.Series) -> str:
    d20 = safe_str(row.get("distance_to_ma20_pct", ""))
    d60 = safe_str(row.get("distance_to_ma60_pct", ""))
    d23 = safe_str(row.get("distance_to_ema23_pct", ""))

    parts = []

    if d20:
        parts.append(f"20MA {d20}%")
    if d23:
        parts.append(f"23EMA {d23}%")
    if d60:
        parts.append(f"60MA {d60}%")

    return " / ".join(parts[:2])


def pattern_signal_short(row: pd.Series) -> str:
    for col in [
        "pattern_signal",
        "action_trigger",
        "breakout_type",
        "category_cn",
    ]:
        value = safe_str(row.get(col, ""))
        if value:
            return clean_reason(value, 24)
    return ""


def pattern_state_short(row: pd.Series) -> str:
    for col in [
        "pattern_state",
        "price_data_warning",
        "risk_note",
    ]:
        value = safe_str(row.get(col, ""))
        if value:
            return clean_reason(value, 24)
    return ""


def category_pdf_row(category: str, row: pd.Series) -> list[str]:
    stock = f"{safe_str(row.get('stock_id', ''))} {safe_str(row.get('stock_name', ''))}"
    theme = clean_reason(theme_short(row), 22)
    score = safe_str(row.get("score", ""))
    rank = safe_str(row.get("rank", ""))
    tdcc = tdcc_short(row)
    warrant = clean_reason(warrant_short(row), 26)
    reason = build_reason(row, 70)

    if category == "true_breakout":
        return [
            stock,
            theme,
            score,
            rank,
            breakout_type_short(row),
            volume_short(row),
            tdcc,
            warrant,
            reason,
        ]

    if category in ["range_rebound", "near_resistance"]:
        return [
            stock,
            theme,
            score,
            rank,
            breakout_type_short(row),
            distance_high_short(row),
            tdcc,
            warrant,
            reason,
        ]

    if category == "abnormal_volume_up":
        return [
            stock,
            theme,
            score,
            rank,
            breakout_type_short(row),
            volume_short(row),
            tdcc,
            warrant,
            reason,
        ]

    if category == "revenue_breakout_low_response":
        return [
            stock,
            theme,
            score,
            rank,
            clean_reason(safe_str(row.get("revaluation_priority", "")), 18),
            revenue_yoy_short(row),
            tdcc,
            warrant,
            reason,
        ]

    if category == "revenue_pullback":
        return [
            stock,
            theme,
            score,
            rank,
            revenue_yoy_short(row),
            ma_distance_short(row),
            tdcc,
            warrant,
            reason,
        ]

    if category == "pullback_rebound":
        return [
            stock,
            theme,
            score,
            rank,
            pattern_signal_short(row),
            ma_distance_short(row),
            tdcc,
            warrant,
            reason,
        ]

    if category == "pattern":
        return [
            stock,
            theme,
            score,
            rank,
            pattern_signal_short(row),
            pattern_state_short(row),
            tdcc,
            warrant,
            reason,
        ]

    return [
        stock,
        theme,
        score,
        rank,
        clean_reason(safe_str(row.get("category_cn", "")), 24),
        tdcc,
        warrant,
        reason,
    ]


def sort_candidates(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    if "score" not in df.columns:
        df["score"] = pd.NA

    if "rank" not in df.columns:
        df["rank"] = pd.NA

    if "warrant_flow_score" not in df.columns:
        df["warrant_flow_score"] = 0

    df["_score_sort"] = pd.to_numeric(df["score"], errors="coerce").fillna(-999999)
    df["_rank_sort"] = pd.to_numeric(df["rank"], errors="coerce").fillna(999999)
    df["_warrant_sort"] = pd.to_numeric(df["warrant_flow_score"], errors="coerce").fillna(0)

    df = df.sort_values(
        ["_score_sort", "_warrant_sort", "_rank_sort"],
        ascending=[False, False, True],
    )

    return df.drop(columns=["_score_sort", "_rank_sort", "_warrant_sort"], errors="ignore")


def get_category_groups(df: pd.DataFrame) -> list[tuple[str, pd.DataFrame]]:
    groups = []
    used = set()

    for category in CATEGORY_ORDER:
        part = df[df["category"].astype(str) == category].copy()

        if not part.empty:
            groups.append((category, sort_candidates(part)))
            used.add(category)

    remaining = [
        c for c in df["category"].dropna().astype(str).unique().tolist()
        if c not in used
    ]

    for category in remaining:
        part = df[df["category"].astype(str) == category].copy()
        if not part.empty:
            groups.append((category, sort_candidates(part)))

    return groups


def register_pdf_fonts() -> str:
    try:
        pdfmetrics.registerFont(UnicodeCIDFont("STSong-Light"))
        return "STSong-Light"
    except Exception:
        return "Helvetica"


def escape_pdf_text(text: str) -> str:
    text = safe_str(text)
    text = (
        text.replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
    )
    return text


def p(text: str, style: ParagraphStyle) -> Paragraph:
    return Paragraph(escape_pdf_text(text), style)


def create_pdf_styles(font_name: str) -> dict:
    styles = getSampleStyleSheet()

    return {
        "title": ParagraphStyle(
            "title",
            parent=styles["Title"],
            fontName=font_name,
            fontSize=20,
            leading=26,
            alignment=TA_CENTER,
            spaceAfter=16,
        ),
        "h1": ParagraphStyle(
            "h1",
            parent=styles["Heading1"],
            fontName=font_name,
            fontSize=15,
            leading=20,
            spaceBefore=12,
            spaceAfter=8,
        ),
        "h2": ParagraphStyle(
            "h2",
            parent=styles["Heading2"],
            fontName=font_name,
            fontSize=12,
            leading=16,
            spaceBefore=8,
            spaceAfter=5,
        ),
        "normal": ParagraphStyle(
            "normal",
            parent=styles["Normal"],
            fontName=font_name,
            fontSize=10,
            leading=15,
            spaceAfter=5,
        ),
        "small": ParagraphStyle(
            "small",
            parent=styles["Normal"],
            fontName=font_name,
            fontSize=8.5,
            leading=12,
            spaceAfter=4,
        ),
        "table_header": ParagraphStyle(
            "table_header",
            parent=styles["Normal"],
            fontName=font_name,
            fontSize=8.5,
            leading=11,
            alignment=TA_CENTER,
        ),
        "table_cell": ParagraphStyle(
            "table_cell",
            parent=styles["Normal"],
            fontName=font_name,
            fontSize=8.2,
            leading=11,
            alignment=TA_LEFT,
        ),
        "card_title": ParagraphStyle(
            "card_title",
            parent=styles["Heading3"],
            fontName=font_name,
            fontSize=11.5,
            leading=15,
            spaceBefore=5,
            spaceAfter=3,
        ),
        "card_body": ParagraphStyle(
            "card_body",
            parent=styles["Normal"],
            fontName=font_name,
            fontSize=9.2,
            leading=13,
            spaceAfter=3,
        ),
    }


def create_table(data: list[list[str]], styles: dict, col_widths=None) -> Table:
    wrapped = []

    for row_idx, row in enumerate(data):
        style = styles["table_header"] if row_idx == 0 else styles["table_cell"]
        wrapped.append([p(safe_str(cell), style) for cell in row])

    table = Table(wrapped, colWidths=col_widths, repeatRows=1)

    table.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#EAEAEA")),
                ("GRID", (0, 0), (-1, -1), 0.25, colors.HexColor("#BBBBBB")),
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, colors.HexColor("#FAFAFA")]),
                ("LEFTPADDING", (0, 0), (-1, -1), 4),
                ("RIGHTPADDING", (0, 0), (-1, -1), 4),
                ("TOPPADDING", (0, 0), (-1, -1), 4),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
            ]
        )
    )

    return table


def add_chart_image(story: list, chart_path: str, styles: dict) -> None:
    if not chart_path or chart_path.startswith("http"):
        return

    path = Path(chart_path)

    if not path.exists():
        return

    try:
        img = Image(str(path))
        max_width = 22.5 * cm
        max_height = 8.8 * cm
        ratio = min(max_width / img.imageWidth, max_height / img.imageHeight)

        img.drawWidth = img.imageWidth * ratio
        img.drawHeight = img.imageHeight * ratio

        story.append(img)
        story.append(Spacer(1, 0.25 * cm))
    except Exception as exc:
        story.append(p(f"圖表載入失敗：{chart_path} / {exc}", styles["small"]))


def build_summary_markdown(
    candidates: pd.DataFrame,
    chart_manifest: pd.DataFrame,
    meta: dict,
    main_date: str,
    report_ready: bool,
) -> str:
    lines = []
    lines.append("# 每日全市場候選股監測報告 - 精華版")
    lines.append("")
    lines.append(f"- 主資料日期：`{main_date}`")
    lines.append(f"- 產生時間：`{now_taipei()} Asia/Taipei`")
    lines.append(f"- 是否可產出正式每日報告：`{report_ready}`")
    lines.append(f"- 判斷說明：{safe_str(meta.get('report_ready_note', ''))}")
    lines.append(f"- 權證資料日期：`{safe_str(meta.get('warrant_flow_date', ''))}`")
    lines.append("")

    if candidates.empty:
        lines.append("目前沒有候選股資料。")
        return "\n".join(lines)

    lines.append("## 今日分類摘要")
    lines.append("")
    lines.append("| 分類 | 檔數 |")
    lines.append("|---|---:|")

    for category, part in get_category_groups(candidates):
        cn = CATEGORY_CN.get(category, safe_str(part["category_cn"].iloc[0]) if "category_cn" in part.columns else category)
        lines.append(f"| {cn} | {len(part)} |")

    lines.append("")
    lines.append("## 精華候選股")
    lines.append("")

    for category, part in get_category_groups(candidates):
        show = part.head(SUMMARY_LIMIT_BY_CATEGORY.get(category, 5)).copy()

        if show.empty:
            continue

        cn = CATEGORY_CN.get(category, safe_str(show["category_cn"].iloc[0]) if "category_cn" in show.columns else category)

        lines.append(f"## {cn}")
        lines.append("")

        for _, row in show.iterrows():
            stock = f"{safe_str(row.get('stock_id', ''))} {safe_str(row.get('stock_name', ''))}"
            lines.append(f"### {stock}")
            lines.append(f"- 族群：{theme_short(row)}")
            lines.append(f"- 分數 / 排名：{safe_str(row.get('score', ''))} / {safe_str(row.get('rank', ''))}")
            lines.append(f"- 優先級：{safe_str(row.get('revaluation_priority', ''))}")
            lines.append(f"- TDCC：{tdcc_short(row)}")
            lines.append(f"- 權證：{warrant_short(row)}")
            lines.append(f"- 簡短原因：{build_reason(row, 180)}")

            chart_path = choose_chart_path(row, chart_manifest)
            if chart_path:
                lines.append(f"- 圖表：{chart_path if chart_path.startswith('http') else '`' + chart_path + '`'}")

            lines.append("")

    return "\n".join(lines)


def build_full_markdown(
    candidates: pd.DataFrame,
    meta: dict,
    main_date: str,
    report_ready: bool,
) -> str:
    lines = []
    lines.append("# 完整候選股清單 - 完整版")
    lines.append("")
    lines.append(f"- 主資料日期：`{main_date}`")
    lines.append(f"- 產生時間：`{now_taipei()} Asia/Taipei`")
    lines.append(f"- 是否可產出正式每日報告：`{report_ready}`")
    lines.append(f"- 權證資料日期：`{safe_str(meta.get('warrant_flow_date', ''))}`")
    lines.append("")

    if candidates.empty:
        lines.append("目前沒有候選股資料。")
        return "\n".join(lines)

    display_cols = [
        "date",
        "stock_id",
        "stock_name",
        "細分族群",
        "industry",
        "category_cn",
        "score",
        "rank",
        "revaluation_priority",
        "tdcc_accumulation_signal",
        "tdcc_judgement",
        "warrant_flow_signal",
        "warrant_flow_score",
        "note",
    ]

    display_cols = [col for col in display_cols if col in candidates.columns]

    for category, part in get_category_groups(candidates):
        cn = CATEGORY_CN.get(category, safe_str(part["category_cn"].iloc[0]) if "category_cn" in part.columns else category)

        lines.append(f"## {cn}")
        lines.append("")
        lines.append(f"- 檔數：`{len(part)}`")
        lines.append("")
        lines.append("| " + " | ".join(display_cols) + " |")
        lines.append("| " + " | ".join(["---"] * len(display_cols)) + " |")

        for _, row in part.iterrows():
            values = []
            for col in display_cols:
                value = safe_str(row.get(col, ""))
                value = value.replace("\n", " ").replace("|", "/")
                if col == "note" and len(value) > 120:
                    value = value[:120] + "..."
                values.append(value)
            lines.append("| " + " | ".join(values) + " |")

        lines.append("")

    return "\n".join(lines)


def build_summary_pdf(
    path: Path,
    candidates: pd.DataFrame,
    chart_manifest: pd.DataFrame,
    meta: dict,
    main_date: str,
    report_ready: bool,
) -> None:
    font_name = register_pdf_fonts()
    styles = create_pdf_styles(font_name)

    doc = SimpleDocTemplate(
        str(path),
        pagesize=A4,
        leftMargin=1.5 * cm,
        rightMargin=1.5 * cm,
        topMargin=1.2 * cm,
        bottomMargin=1.2 * cm,
    )

    story = []
    story.append(p("每日全市場候選股監測報告 - 精華版", styles["title"]))
    story.append(p(f"主資料日期：{main_date}", styles["normal"]))
    story.append(p(f"產生時間：{now_taipei()} Asia/Taipei", styles["normal"]))
    story.append(p(f"是否可產出正式每日報告：{report_ready}", styles["normal"]))
    story.append(p(f"判斷說明：{safe_str(meta.get('report_ready_note', ''))}", styles["normal"]))
    story.append(p(f"權證資料日期：{safe_str(meta.get('warrant_flow_date', ''))}", styles["normal"]))
    story.append(Spacer(1, 0.3 * cm))

    if candidates.empty:
        story.append(p("目前沒有候選股資料。", styles["normal"]))
        doc.build(story)
        return

    summary_rows = [["分類", "檔數"]]

    for category, part in get_category_groups(candidates):
        cn = CATEGORY_CN.get(category, safe_str(part["category_cn"].iloc[0]) if "category_cn" in part.columns else category)
        summary_rows.append([cn, str(len(part))])

    story.append(p("今日分類摘要", styles["h1"]))
    story.append(create_table(summary_rows, styles, col_widths=[12 * cm, 3 * cm]))
    story.append(Spacer(1, 0.4 * cm))

    first_category = True

    for category, part in get_category_groups(candidates):
        show = part.head(SUMMARY_LIMIT_BY_CATEGORY.get(category, 5)).copy()

        if show.empty:
            continue

        if not first_category:
            story.append(PageBreak())
        first_category = False

        cn = CATEGORY_CN.get(category, safe_str(show["category_cn"].iloc[0]) if "category_cn" in show.columns else category)
        story.append(p(cn, styles["h1"]))

        chart_count = 0

        for _, row in show.iterrows():
            stock = f"{safe_str(row.get('stock_id', ''))} {safe_str(row.get('stock_name', ''))}"

            story.append(p(stock, styles["card_title"]))
            story.append(p(f"族群：{theme_short(row)}", styles["card_body"]))
            story.append(p(f"分數 / 排名：{safe_str(row.get('score', ''))} / {safe_str(row.get('rank', ''))}", styles["card_body"]))
            story.append(p(f"優先級：{safe_str(row.get('revaluation_priority', ''))}", styles["card_body"]))
            story.append(p(f"TDCC：{tdcc_short(row)}", styles["card_body"]))
            story.append(p(f"權證：{warrant_short(row)}", styles["card_body"]))
            story.append(p(f"簡短原因：{build_reason(row, 150)}", styles["card_body"]))

            chart_path = choose_chart_path(row, chart_manifest)

            if chart_count < 2 and chart_path and not chart_path.startswith("http") and Path(chart_path).exists():
                add_chart_image(story, chart_path, styles)
                chart_count += 1

            story.append(Spacer(1, 0.2 * cm))

    doc.build(story)


def build_full_pdf(
    path: Path,
    candidates: pd.DataFrame,
    meta: dict,
    main_date: str,
    report_ready: bool,
) -> None:
    font_name = register_pdf_fonts()
    styles = create_pdf_styles(font_name)

    doc = SimpleDocTemplate(
        str(path),
        pagesize=landscape(A4),
        leftMargin=0.9 * cm,
        rightMargin=0.9 * cm,
        topMargin=0.8 * cm,
        bottomMargin=0.8 * cm,
    )

    story = []
    story.append(p("完整候選股清單 - 完整版表格", styles["title"]))
    story.append(p(f"主資料日期：{main_date}", styles["normal"]))
    story.append(p(f"產生時間：{now_taipei()} Asia/Taipei", styles["normal"]))
    story.append(p(f"是否可產出正式每日報告：{report_ready}", styles["normal"]))
    story.append(p(f"權證資料日期：{safe_str(meta.get('warrant_flow_date', ''))}", styles["normal"]))
    story.append(Spacer(1, 0.3 * cm))

    if candidates.empty:
        story.append(p("目前沒有候選股資料。", styles["normal"]))
        doc.build(story)
        return

    for category_index, (category, part) in enumerate(get_category_groups(candidates)):
        cn = CATEGORY_CN.get(
            category,
            safe_str(part["category_cn"].iloc[0]) if "category_cn" in part.columns else category,
        )

        config = FULL_PDF_COLUMN_CONFIG.get(category, FULL_PDF_COLUMN_CONFIG["default"])
        headers = config["headers"]
        col_widths = [w * cm for w in config["widths"]]

        chunks = [
            part.iloc[i:i + FULL_PDF_ROWS_PER_PAGE].copy()
            for i in range(0, len(part), FULL_PDF_ROWS_PER_PAGE)
        ]

        for chunk_index, chunk in enumerate(chunks):
            if category_index > 0 or chunk_index > 0:
                story.append(PageBreak())

            story.append(p(f"{cn}（{len(part)} 檔）", styles["h1"]))

            if len(chunks) > 1:
                story.append(p(f"第 {chunk_index + 1} / {len(chunks)} 頁", styles["small"]))

            rows = [headers]

            for _, row in chunk.iterrows():
                rows.append(category_pdf_row(category, row))

            table = create_table(
                rows,
                styles,
                col_widths=col_widths,
            )

            story.append(table)

    doc.build(story)


def build_manifest(
    main_date: str,
    report_ready: bool,
    meta: dict,
    history_summary_md: Path,
    history_summary_pdf: Path,
    history_full_md: Path,
    history_full_pdf: Path,
) -> dict:
    return {
        "generated_at": now_taipei() + " Asia/Taipei",
        "main_price_date": main_date,
        "report_ready": bool(report_ready),
        "report_ready_note": safe_str(meta.get("report_ready_note", "")),
        "latest_summary_md": str(LATEST_SUMMARY_MD),
        "latest_summary_pdf": str(LATEST_SUMMARY_PDF),
        "latest_full_md": str(LATEST_FULL_MD),
        "latest_full_pdf": str(LATEST_FULL_PDF),
        "history_summary_md": str(history_summary_md),
        "history_summary_pdf": str(history_summary_pdf),
        "history_full_md": str(history_full_md),
        "history_full_pdf": str(history_full_pdf),
        "summary_md_raw_url": raw_url_for_path(history_summary_md),
        "summary_pdf_raw_url": raw_url_for_path(history_summary_pdf),
        "full_md_raw_url": raw_url_for_path(history_full_md),
        "full_pdf_raw_url": raw_url_for_path(history_full_pdf),
        "data_freshness_raw_url": raw_url_for_path(DATA_FRESHNESS_MD),
        "all_candidates_raw_url": raw_url_for_path(ALL_CANDIDATES_CSV),
    }


def write_manifest_files(manifest: dict) -> None:
    MANIFEST_JSON.write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )

    lines = []
    lines.append("# 每日報告 Manifest")
    lines.append("")
    lines.append(f"- 產生時間：`{manifest.get('generated_at', '')}`")
    lines.append(f"- 主資料日期：`{manifest.get('main_price_date', '')}`")
    lines.append(f"- 是否可產出正式每日報告：`{manifest.get('report_ready', '')}`")
    lines.append(f"- 判斷說明：{manifest.get('report_ready_note', '')}")
    lines.append("")
    lines.append("## 建議讀取順序")
    lines.append("")
    lines.append("1. 優先讀日期版精華 MD。")
    lines.append("2. 若 MD 讀取失敗，再讀日期版精華 PDF。")
    lines.append("3. 若日期版讀取失敗，再讀 latest 版。")
    lines.append("4. 若全部失敗，才回報讀取工具失敗。")
    lines.append("")
    lines.append("## 檔案")
    lines.append("")
    lines.append(f"- 日期版精華 MD：`{manifest.get('history_summary_md', '')}`")
    lines.append(f"- 日期版精華 PDF：`{manifest.get('history_summary_pdf', '')}`")
    lines.append(f"- 日期版完整版 MD：`{manifest.get('history_full_md', '')}`")
    lines.append(f"- 日期版完整版 PDF：`{manifest.get('history_full_pdf', '')}`")
    lines.append(f"- latest 精華 MD：`{manifest.get('latest_summary_md', '')}`")
    lines.append(f"- latest 精華 PDF：`{manifest.get('latest_summary_pdf', '')}`")
    lines.append(f"- latest 完整版 MD：`{manifest.get('latest_full_md', '')}`")
    lines.append(f"- latest 完整版 PDF：`{manifest.get('latest_full_pdf', '')}`")
    lines.append("")
    lines.append("## Raw URLs")
    lines.append("")
    lines.append(f"- summary_md_raw_url: {manifest.get('summary_md_raw_url', '')}")
    lines.append(f"- summary_pdf_raw_url: {manifest.get('summary_pdf_raw_url', '')}")
    lines.append(f"- full_md_raw_url: {manifest.get('full_md_raw_url', '')}")
    lines.append(f"- full_pdf_raw_url: {manifest.get('full_pdf_raw_url', '')}")
    lines.append("")

    MANIFEST_MD.write_text("\n".join(lines), encoding="utf-8")


def main() -> int:
    LATEST_DIR.mkdir(parents=True, exist_ok=True)
    HISTORY_REPORT_DIR.mkdir(parents=True, exist_ok=True)

    main_date, report_ready, meta = get_main_price_date()

    if not main_date:
        main_date = datetime.now(ZoneInfo("Asia/Taipei")).strftime("%Y%m%d")

    candidates = load_candidates()
    chart_manifest = load_chart_manifest()

    summary_md = build_summary_markdown(
        candidates=candidates,
        chart_manifest=chart_manifest,
        meta=meta,
        main_date=main_date,
        report_ready=report_ready,
    )

    full_md = build_full_markdown(
        candidates=candidates,
        meta=meta,
        main_date=main_date,
        report_ready=report_ready,
    )

    LATEST_SUMMARY_MD.write_text(summary_md, encoding="utf-8")
    LATEST_FULL_MD.write_text(full_md, encoding="utf-8")

    build_summary_pdf(
        path=LATEST_SUMMARY_PDF,
        candidates=candidates,
        chart_manifest=chart_manifest,
        meta=meta,
        main_date=main_date,
        report_ready=report_ready,
    )

    build_full_pdf(
        path=LATEST_FULL_PDF,
        candidates=candidates,
        meta=meta,
        main_date=main_date,
        report_ready=report_ready,
    )

    history_summary_md = HISTORY_REPORT_DIR / f"{main_date}_每日全市場候選股監測報告_精華版.md"
    history_summary_pdf = HISTORY_REPORT_DIR / f"{main_date}_每日全市場候選股監測報告_精華版.pdf"
    history_full_md = HISTORY_REPORT_DIR / f"{main_date}_完整候選股清單_完整版.md"
    history_full_pdf = HISTORY_REPORT_DIR / f"{main_date}_完整候選股清單_完整版表格.pdf"

    shutil.copyfile(LATEST_SUMMARY_MD, history_summary_md)
    shutil.copyfile(LATEST_SUMMARY_PDF, history_summary_pdf)
    shutil.copyfile(LATEST_FULL_MD, history_full_md)
    shutil.copyfile(LATEST_FULL_PDF, history_full_pdf)

    manifest = build_manifest(
        main_date=main_date,
        report_ready=report_ready,
        meta=meta,
        history_summary_md=history_summary_md,
        history_summary_pdf=history_summary_pdf,
        history_full_md=history_full_md,
        history_full_pdf=history_full_pdf,
    )

    write_manifest_files(manifest)

    print(f"Saved: {LATEST_SUMMARY_MD}")
    print(f"Saved: {LATEST_SUMMARY_PDF}")
    print(f"Saved: {LATEST_FULL_MD}")
    print(f"Saved: {LATEST_FULL_PDF}")
    print(f"Saved: {MANIFEST_JSON}")
    print(f"Saved: {MANIFEST_MD}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
