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
CONTACT_SHEET_MANIFEST_CSV = LATEST_DIR / "contact_sheet_manifest.csv"
WARRANT_FLOW_CSV = LATEST_DIR / "warrant_flow_latest.csv"
STOCK_MONITOR_MD = LATEST_DIR / "stock_monitor_latest.md"

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
    return str(value)


def safe_float(value, default=math.nan) -> float:
    try:
        if pd.isna(value):
            return default
        return float(value)
    except Exception:
        return default


def safe_int(value, default=0) -> int:
    try:
        if pd.isna(value):
            return default
        return int(float(value))
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


def read_text(path: Path) -> str:
    if not path.exists():
        return ""
    try:
        return path.read_text(encoding="utf-8")
    except Exception:
        try:
            return path.read_text(encoding="utf-8-sig")
        except Exception:
            return ""


def get_main_price_date() -> tuple[str, bool, dict]:
    freshness = read_csv(DATA_FRESHNESS_CSV)

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

    if not freshness.empty:
        row = freshness.iloc[0].to_dict()
        for key in meta.keys():
            if key in row:
                meta[key] = row[key]

        main_date = normalize_date(meta.get("main_price_date", ""))
        report_ready_raw = safe_str(meta.get("report_ready", "")).lower()
        report_ready = report_ready_raw in ["true", "1", "yes"]

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

    if "stock_id" not in df.columns:
        for col in ["ticker", "code", "股票代號"]:
            if col in df.columns:
                df = df.rename(columns={col: "stock_id"})
                break

    if "stock_name" not in df.columns:
        for col in ["name", "股票名稱", "證券名稱"]:
            if col in df.columns:
                df = df.rename(columns={col: "stock_name"})
                break

    for col in ["score", "rank", "warrant_flow_score"]:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors="coerce")

    if "category" not in df.columns:
        df["category"] = "unknown"

    if "category_cn" not in df.columns:
        df["category_cn"] = df["category"].map(lambda x: CATEGORY_CN.get(safe_str(x), safe_str(x)))

    if "note" not in df.columns:
        df["note"] = ""

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

    return df


def choose_chart_path(row: pd.Series, chart_manifest: pd.DataFrame) -> str:
    for col in ["chart_path", "chart_url"]:
        if col in row and safe_str(row[col]):
            value = safe_str(row[col])
            if value.startswith("http"):
                return value
            if Path(value).exists():
                return value

    if chart_manifest.empty:
        return ""

    stock_id = safe_str(row.get("stock_id", "")).zfill(4)
    category = safe_str(row.get("category", ""))

    part = chart_manifest.copy()

    if "stock_id" in part.columns:
        part = part[part["stock_id"].astype(str).str.zfill(4) == stock_id]

    if "category" in part.columns and category:
        same_cat = part[part["category"].astype(str) == category]
        if not same_cat.empty:
            part = same_cat

    if part.empty:
        return ""

    for col in ["chart_path", "path", "chart_url"]:
        if col in part.columns:
            value = safe_str(part.iloc[0].get(col, ""))
            if value:
                if value.startswith("http"):
                    return value
                if Path(value).exists():
                    return value
                return value

    return ""


def build_reason(row: pd.Series) -> str:
    parts = []

    for col in [
        "revaluation_priority",
        "tdcc_accumulation_signal",
        "tdcc_accumulation_note",
        "tdcc_judgement",
        "warrant_flow_signal",
        "warrant_flow_warning",
        "warrant_note",
        "note",
    ]:
        value = safe_str(row.get(col, ""))
        if value and value.lower() != "nan":
            parts.append(value)

    reason = "；".join(parts)
    reason = reason.replace("\n", " ").replace("|", "/")

    if len(reason) > 120:
        reason = reason[:120] + "..."

    return reason


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

    remaining_categories = [
        c for c in df["category"].dropna().astype(str).unique().tolist()
        if c not in used
    ]

    for category in remaining_categories:
        part = df[df["category"].astype(str) == category].copy()
        groups.append((category, sort_candidates(part)))

    return groups


def build_summary_markdown(
    candidates: pd.DataFrame,
    chart_manifest: pd.DataFrame,
    meta: dict,
    main_date: str,
    report_ready: bool,
) -> str:
    lines = []

    lines.append(f"# 每日全市場候選股監測報告 - 精華版")
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
    lines.append("| 分類 | 檔數 | 備註 |")
    lines.append("|---|---:|---|")

    for category, part in get_category_groups(candidates):
        cn = CATEGORY_CN.get(category, safe_str(part["category_cn"].iloc[0]) if "category_cn" in part.columns else category)
        lines.append(f"| {cn} | {len(part)} | 每類只列精華候選，完整清單請看完整版 |")

    lines.append("")

    lines.append("## 精華候選股")
    lines.append("")

    for category, part in get_category_groups(candidates):
        limit = SUMMARY_LIMIT_BY_CATEGORY.get(category, 5)
        show = part.head(limit).copy()

        if show.empty:
            continue

        cn = CATEGORY_CN.get(category, safe_str(show["category_cn"].iloc[0]) if "category_cn" in show.columns else category)

        lines.append(f"## {cn}")
        lines.append("")
        lines.append("| 股票 | 族群 | 分數 | 排名 | 優先級 | 權證 | 權證分 | 簡短原因 |")
        lines.append("|---|---|---:|---:|---|---|---:|---|")

        for _, row in show.iterrows():
            stock = f"{safe_str(row.get('stock_id', ''))} {safe_str(row.get('stock_name', ''))}"
            theme = safe_str(row.get("細分族群", "")) or safe_str(row.get("theme_note", "")) or safe_str(row.get("industry", ""))
            score = safe_str(row.get("score", ""))
            rank = safe_str(row.get("rank", ""))
            priority = safe_str(row.get("revaluation_priority", ""))
            warrant_signal = safe_str(row.get("warrant_flow_signal", ""))
            warrant_score = safe_str(row.get("warrant_flow_score", ""))
            reason = build_reason(row)

            lines.append(
                f"| {stock} | {theme} | {score} | {rank} | {priority} | {warrant_signal} | {warrant_score} | {reason} |"
            )

        lines.append("")

        for _, row in show.iterrows():
            chart_path = choose_chart_path(row, chart_manifest)

            if chart_path:
                stock = f"{safe_str(row.get('stock_id', ''))} {safe_str(row.get('stock_name', ''))}"
                lines.append(f"### {stock} 圖表")
                lines.append("")
                if chart_path.startswith("http"):
                    lines.append(f"- 圖表：{chart_path}")
                else:
                    lines.append(f"- 圖表：`{chart_path}`")
                lines.append(f"- 選入原因：{build_reason(row)}")
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
        "warrant_flow_warning",
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

                if col in ["note", "warrant_flow_warning"] and len(value) > 80:
                    value = value[:80] + "..."

                values.append(value)

            lines.append("| " + " | ".join(values) + " |")

        lines.append("")

    return "\n".join(lines)


def register_pdf_fonts() -> str:
    try:
        pdfmetrics.registerFont(UnicodeCIDFont("STSong-Light"))
        return "STSong-Light"
    except Exception:
        return "Helvetica"


def paragraph(text: str, style: ParagraphStyle) -> Paragraph:
    text = safe_str(text)
    text = (
        text.replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
        .replace("\n", "<br/>")
    )
    return Paragraph(text, style)


def create_pdf_styles(font_name: str) -> dict:
    styles = getSampleStyleSheet()

    title = ParagraphStyle(
        "CustomTitle",
        parent=styles["Title"],
        fontName=font_name,
        fontSize=20,
        leading=26,
        alignment=TA_CENTER,
        spaceAfter=16,
    )

    h1 = ParagraphStyle(
        "CustomH1",
        parent=styles["Heading1"],
        fontName=font_name,
        fontSize=15,
        leading=20,
        spaceBefore=14,
        spaceAfter=8,
    )

    h2 = ParagraphStyle(
        "CustomH2",
        parent=styles["Heading2"],
        fontName=font_name,
        fontSize=12,
        leading=16,
        spaceBefore=10,
        spaceAfter=6,
    )

    normal = ParagraphStyle(
        "CustomNormal",
        parent=styles["Normal"],
        fontName=font_name,
        fontSize=9,
        leading=13,
        spaceAfter=5,
    )

    small = ParagraphStyle(
        "CustomSmall",
        parent=styles["Normal"],
        fontName=font_name,
        fontSize=7,
        leading=10,
    )

    table_cell = ParagraphStyle(
        "TableCell",
        parent=styles["Normal"],
        fontName=font_name,
        fontSize=7,
        leading=9,
        alignment=TA_LEFT,
    )

    table_header = ParagraphStyle(
        "TableHeader",
        parent=styles["Normal"],
        fontName=font_name,
        fontSize=7,
        leading=9,
        alignment=TA_CENTER,
    )

    return {
        "title": title,
        "h1": h1,
        "h2": h2,
        "normal": normal,
        "small": small,
        "table_cell": table_cell,
        "table_header": table_header,
    }


def create_table(data: list[list[str]], styles: dict, col_widths=None) -> Table:
    wrapped = []

    for row_idx, row in enumerate(data):
        style = styles["table_header"] if row_idx == 0 else styles["table_cell"]
        wrapped.append([paragraph(str(cell), style) for cell in row])

    table = Table(wrapped, colWidths=col_widths, repeatRows=1)

    table.setStyle(
        TableStyle(
            [
                ("FONTNAME", (0, 0), (-1, -1), styles["table_cell"].fontName),
                ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#EAEAEA")),
                ("TEXTCOLOR", (0, 0), (-1, 0), colors.black),
                ("GRID", (0, 0), (-1, -1), 0.25, colors.HexColor("#BBBBBB")),
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, colors.HexColor("#FAFAFA")]),
                ("LEFTPADDING", (0, 0), (-1, -1), 3),
                ("RIGHTPADDING", (0, 0), (-1, -1), 3),
                ("TOPPADDING", (0, 0), (-1, -1), 3),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 3),
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
        max_width = 24 * cm
        max_height = 10 * cm

        ratio = min(max_width / img.imageWidth, max_height / img.imageHeight)
        img.drawWidth = img.imageWidth * ratio
        img.drawHeight = img.imageHeight * ratio

        story.append(img)
        story.append(Spacer(1, 0.25 * cm))
    except Exception as exc:
        story.append(paragraph(f"圖表載入失敗：{chart_path} / {exc}", styles["small"]))


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
        pagesize=landscape(A4),
        leftMargin=0.9 * cm,
        rightMargin=0.9 * cm,
        topMargin=0.9 * cm,
        bottomMargin=0.9 * cm,
    )

    story = []

    story.append(paragraph("每日全市場候選股監測報告 - 精華版", styles["title"]))
    story.append(paragraph(f"主資料日期：{main_date}", styles["normal"]))
    story.append(paragraph(f"產生時間：{now_taipei()} Asia/Taipei", styles["normal"]))
    story.append(paragraph(f"是否可產出正式每日報告：{report_ready}", styles["normal"]))
    story.append(paragraph(f"判斷說明：{safe_str(meta.get('report_ready_note', ''))}", styles["normal"]))
    story.append(paragraph(f"權證資料日期：{safe_str(meta.get('warrant_flow_date', ''))}", styles["normal"]))
    story.append(Spacer(1, 0.3 * cm))

    if candidates.empty:
        story.append(paragraph("目前沒有候選股資料。", styles["normal"]))
        doc.build(story)
        return

    summary_rows = [["分類", "檔數", "說明"]]

    for category, part in get_category_groups(candidates):
        cn = CATEGORY_CN.get(category, safe_str(part["category_cn"].iloc[0]) if "category_cn" in part.columns else category)
        summary_rows.append([cn, str(len(part)), "每類列精華候選，完整版列完整清單"])

    story.append(paragraph("今日分類摘要", styles["h1"]))
    story.append(create_table(summary_rows, styles, col_widths=[7 * cm, 2 * cm, 16 * cm]))
    story.append(Spacer(1, 0.5 * cm))

    for category, part in get_category_groups(candidates):
        show = part.head(SUMMARY_LIMIT_BY_CATEGORY.get(category, 5)).copy()

        if show.empty:
            continue

        cn = CATEGORY_CN.get(category, safe_str(show["category_cn"].iloc[0]) if "category_cn" in show.columns else category)

        story.append(paragraph(cn, styles["h1"]))

        rows = [["股票", "族群", "分數", "排名", "優先級", "權證", "權證分", "簡短原因"]]

        for _, row in show.iterrows():
            rows.append(
                [
                    f"{safe_str(row.get('stock_id', ''))} {safe_str(row.get('stock_name', ''))}",
                    safe_str(row.get("細分族群", "")) or safe_str(row.get("theme_note", "")) or safe_str(row.get("industry", "")),
                    safe_str(row.get("score", "")),
                    safe_str(row.get("rank", "")),
                    safe_str(row.get("revaluation_priority", "")),
                    safe_str(row.get("warrant_flow_signal", "")),
                    safe_str(row.get("warrant_flow_score", "")),
                    build_reason(row),
                ]
            )

        story.append(
            create_table(
                rows,
                styles,
                col_widths=[3.0 * cm, 3.3 * cm, 1.5 * cm, 1.5 * cm, 3.0 * cm, 4.0 * cm, 1.7 * cm, 9.0 * cm],
            )
        )
        story.append(Spacer(1, 0.3 * cm))

        charts_added = 0

        for _, row in show.iterrows():
            chart_path = choose_chart_path(row, chart_manifest)

            if chart_path and not chart_path.startswith("http") and Path(chart_path).exists():
                story.append(
                    paragraph(
                        f"{safe_str(row.get('stock_id', ''))} {safe_str(row.get('stock_name', ''))} - 圖表",
                        styles["h2"],
                    )
                )
                story.append(paragraph(f"選入原因：{build_reason(row)}", styles["small"]))
                add_chart_image(story, chart_path, styles)
                charts_added += 1

            if charts_added >= 3:
                break

        story.append(Spacer(1, 0.4 * cm))

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
        leftMargin=0.7 * cm,
        rightMargin=0.7 * cm,
        topMargin=0.7 * cm,
        bottomMargin=0.7 * cm,
    )

    story = []

    story.append(paragraph("完整候選股清單 - 完整版表格", styles["title"]))
    story.append(paragraph(f"主資料日期：{main_date}", styles["normal"]))
    story.append(paragraph(f"產生時間：{now_taipei()} Asia/Taipei", styles["normal"]))
    story.append(paragraph(f"是否可產出正式每日報告：{report_ready}", styles["normal"]))
    story.append(paragraph(f"權證資料日期：{safe_str(meta.get('warrant_flow_date', ''))}", styles["normal"]))
    story.append(Spacer(1, 0.3 * cm))

    if candidates.empty:
        story.append(paragraph("目前沒有候選股資料。", styles["normal"]))
        doc.build(story)
        return

    display_cols = [
        "date",
        "stock_id",
        "stock_name",
        "細分族群",
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

    col_labels = {
        "date": "日期",
        "stock_id": "代號",
        "stock_name": "名稱",
        "細分族群": "族群",
        "category_cn": "分類",
        "score": "分數",
        "rank": "排名",
        "revaluation_priority": "優先級",
        "tdcc_accumulation_signal": "TDCC趨勢",
        "tdcc_judgement": "TDCC",
        "warrant_flow_signal": "權證訊號",
        "warrant_flow_score": "權證分",
        "note": "簡短原因",
    }

    for idx, (category, part) in enumerate(get_category_groups(candidates)):
        if idx > 0:
            story.append(PageBreak())

        cn = CATEGORY_CN.get(category, safe_str(part["category_cn"].iloc[0]) if "category_cn" in part.columns else category)
        story.append(paragraph(f"{cn}（{len(part)} 檔）", styles["h1"]))

        rows = [[col_labels.get(col, col) for col in display_cols]]

        for _, row in part.iterrows():
            values = []
            for col in display_cols:
                value = safe_str(row.get(col, ""))
                value = value.replace("\n", " ").replace("|", "/")

                if col == "note" and len(value) > 70:
                    value = value[:70] + "..."

                if col in ["tdcc_accumulation_signal", "warrant_flow_signal"] and len(value) > 28:
                    value = value[:28] + "..."

                values.append(value)

            rows.append(values)

        widths_map = {
            "date": 2.0 * cm,
            "stock_id": 1.7 * cm,
            "stock_name": 2.1 * cm,
            "細分族群": 2.8 * cm,
            "category_cn": 3.0 * cm,
            "score": 1.2 * cm,
            "rank": 1.2 * cm,
            "revaluation_priority": 2.6 * cm,
            "tdcc_accumulation_signal": 2.8 * cm,
            "tdcc_judgement": 2.4 * cm,
            "warrant_flow_signal": 3.0 * cm,
            "warrant_flow_score": 1.3 * cm,
            "note": 5.8 * cm,
        }

        col_widths = [widths_map.get(col, 2.0 * cm) for col in display_cols]
        story.append(create_table(rows, styles, col_widths=col_widths))
        story.append(Spacer(1, 0.3 * cm))

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
    manifest = {
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

    return manifest


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
    candidates = load_candidates()
    chart_manifest = load_chart_manifest()

    if not main_date:
        main_date = datetime.now(ZoneInfo("Asia/Taipei")).strftime("%Y%m%d")

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
