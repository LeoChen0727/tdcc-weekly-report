from __future__ import annotations

from pathlib import Path
import sys
from typing import Any

import pandas as pd
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.lib.pagesizes import A4, landscape
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import cm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.cidfonts import UnicodeCIDFont
from reportlab.platypus import LongTable, PageBreak, Paragraph, SimpleDocTemplate, Spacer, TableStyle

sys.path.insert(0, str(Path(__file__).resolve().parent))

from build_volume_breakout_operation_pdf_preview import MARKDOWN_HEADERS, now_text  # noqa: E402
from tracking_utils import LATEST_DIR, safe_str  # noqa: E402


PREVIEW_CSV = LATEST_DIR / "volume_breakout_operation_pdf_preview_latest.csv"
PREVIEW_PDF = LATEST_DIR / "volume_breakout_operation_pdf_preview_latest.pdf"

FONT_NAME = "STSong-Light"


def read_preview() -> pd.DataFrame:
    if not PREVIEW_CSV.exists():
        raise FileNotFoundError(f"missing preview CSV: {PREVIEW_CSV}")
    return pd.read_csv(PREVIEW_CSV, dtype=str, keep_default_na=False)


def style_map() -> dict[str, ParagraphStyle]:
    pdfmetrics.registerFont(UnicodeCIDFont(FONT_NAME))
    return {
        "title": ParagraphStyle(
            "title",
            fontName=FONT_NAME,
            fontSize=18,
            leading=23,
            alignment=TA_LEFT,
            textColor=colors.HexColor("#16324f"),
            spaceAfter=8,
        ),
        "section": ParagraphStyle(
            "section",
            fontName=FONT_NAME,
            fontSize=12,
            leading=16,
            alignment=TA_LEFT,
            textColor=colors.HexColor("#1d3557"),
            spaceBefore=10,
            spaceAfter=5,
        ),
        "note": ParagraphStyle(
            "note",
            fontName=FONT_NAME,
            fontSize=8,
            leading=11,
            alignment=TA_LEFT,
            textColor=colors.HexColor("#3f4752"),
            spaceAfter=6,
        ),
        "header": ParagraphStyle(
            "header",
            fontName=FONT_NAME,
            fontSize=7,
            leading=9,
            alignment=TA_CENTER,
            textColor=colors.white,
        ),
        "cell": ParagraphStyle(
            "cell",
            fontName=FONT_NAME,
            fontSize=7,
            leading=9,
            alignment=TA_LEFT,
            textColor=colors.HexColor("#111827"),
        ),
        "cell_center": ParagraphStyle(
            "cell_center",
            fontName=FONT_NAME,
            fontSize=7,
            leading=9,
            alignment=TA_CENTER,
            textColor=colors.HexColor("#111827"),
        ),
    }


def paragraph(value: Any, style: ParagraphStyle) -> Paragraph:
    text = safe_str(value).replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    return Paragraph(text, style)


def table_rows(df: pd.DataFrame, columns: list[str], styles: dict[str, ParagraphStyle]) -> list[list[Paragraph]]:
    rows: list[list[Paragraph]] = [[paragraph(MARKDOWN_HEADERS.get(col, col), styles["header"]) for col in columns]]
    center_cols = {
        "display_order",
        "operation_status_zh",
        "sample_size",
        "win_rate_zh",
        "avg_return_zh",
        "median_return_zh",
        "confidence_zh",
        "same_stock_pending_count",
        "research_score",
    }
    for _, row in df.iterrows():
        rows.append(
            [
                paragraph(row.get(col, ""), styles["cell_center" if col in center_cols else "cell"])
                for col in columns
            ]
        )
    return rows


def add_table(
    story: list[Any],
    title: str,
    df: pd.DataFrame,
    columns: list[str],
    widths_cm: list[float],
    styles: dict[str, ParagraphStyle],
    empty_text: str,
) -> None:
    story.append(Paragraph(title, styles["section"]))
    if df.empty:
        story.append(Paragraph(empty_text, styles["note"]))
        story.append(Spacer(1, 0.2 * cm))
        return
    table = LongTable(
        table_rows(df, columns, styles),
        colWidths=[width * cm for width in widths_cm],
        repeatRows=1,
        hAlign="LEFT",
    )
    table.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#1d3557")),
                ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
                ("FONTNAME", (0, 0), (-1, -1), FONT_NAME),
                ("GRID", (0, 0), (-1, -1), 0.3, colors.HexColor("#cbd5e1")),
                ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, colors.HexColor("#f8fafc")]),
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("LEFTPADDING", (0, 0), (-1, -1), 3),
                ("RIGHTPADDING", (0, 0), (-1, -1), 3),
                ("TOPPADDING", (0, 0), (-1, -1), 3),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 3),
            ]
        )
    )
    story.append(table)
    story.append(Spacer(1, 0.25 * cm))


def filtered(preview: pd.DataFrame, pdf_view: str, pdf_section: str) -> pd.DataFrame:
    return preview[
        preview.get("pdf_view", "").astype(str).eq(pdf_view)
        & preview.get("pdf_section", "").astype(str).eq(pdf_section)
    ].copy()


def build_pdf(preview: pd.DataFrame) -> None:
    styles = style_map()
    highlight_confirmed = filtered(preview, "highlight", "confirmed_operation")
    highlight_pending = filtered(preview, "highlight", "pending_confirmation")
    full_confirmed = filtered(preview, "full", "confirmed_operation")
    full_pending = filtered(preview, "full", "pending_confirmation")

    doc = SimpleDocTemplate(
        str(PREVIEW_PDF),
        pagesize=landscape(A4),
        leftMargin=0.8 * cm,
        rightMargin=0.8 * cm,
        topMargin=0.9 * cm,
        bottomMargin=0.8 * cm,
        title="放量攻擊操作 PDF Preview",
        author="tdcc-weekly-report research backtest",
    )

    story: list[Any] = [
        Paragraph("放量攻擊操作 PDF Preview", styles["title"]),
        Paragraph(
            (
                f"產生時間：{now_text()}。這份 PDF 是 research/backtest preview，"
                "尚未接入 daily production PDF；表格文字直接來自 preview CSV。"
            ),
            styles["note"],
        ),
        Paragraph(
            "進場基準：已確認後下一交易日開盤。停損基準固定顯示為日期最低價，例如：跌破 6/13 最低價 49.00。",
            styles["note"],
        ),
    ]

    add_table(
        story,
        "精華版 已確認操作排名",
        highlight_confirmed,
        [
            "display_order",
            "stock_display",
            "operation_status_zh",
            "trigger_zh",
            "entry_basis_zh",
            "stop_basis_zh",
            "sample_size",
            "win_rate_zh",
            "avg_return_zh",
            "median_return_zh",
            "confidence_zh",
        ],
        [1.0, 2.8, 1.5, 2.5, 3.0, 3.5, 1.4, 1.6, 1.8, 2.0, 1.2],
        styles,
        "沒有符合精華版條件的已確認操作。",
    )
    add_table(
        story,
        "精華版 待確認",
        highlight_pending,
        [
            "display_order",
            "stock_display",
            "operation_status_zh",
            "pending_age_zh",
            "pending_group_zh",
            "stop_basis_zh",
            "same_stock_pending_count",
            "pdf_note_zh",
        ],
        [1.0, 3.0, 1.7, 3.1, 4.0, 4.0, 1.8, 7.0],
        styles,
        "目前沒有待確認股票。",
    )

    story.append(PageBreak())
    story.append(Paragraph("完整版", styles["title"]))
    story.append(
        Paragraph(
            "完整版列出所有 confirmed rows，以及依股票去重後的 pending rows；holding 表需等 daily production 有持有追蹤狀態後才接入。",
            styles["note"],
        )
    )
    add_table(
        story,
        "完整版 已確認操作排名",
        full_confirmed,
        [
            "display_order",
            "stock_display",
            "quality_status_zh",
            "trigger_zh",
            "stop_basis_zh",
            "sample_size",
            "win_rate_zh",
            "median_return_zh",
            "research_score",
        ],
        [1.0, 3.0, 2.0, 2.6, 4.0, 1.5, 1.8, 2.1, 2.0],
        styles,
        "目前沒有已確認操作。",
    )
    add_table(
        story,
        "完整版 待確認",
        full_pending,
        [
            "display_order",
            "stock_display",
            "pending_age_zh",
            "pending_group_zh",
            "stop_basis_zh",
            "same_stock_pending_count",
            "pdf_note_zh",
        ],
        [1.0, 3.2, 3.2, 4.2, 4.0, 1.8, 9.0],
        styles,
        "目前沒有待確認股票。",
    )

    PREVIEW_PDF.parent.mkdir(parents=True, exist_ok=True)
    doc.build(story)


def main() -> int:
    preview = read_preview()
    build_pdf(preview)
    print(f"Saved: {PREVIEW_PDF}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
