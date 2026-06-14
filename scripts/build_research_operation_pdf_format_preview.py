from __future__ import annotations

from pathlib import Path
import sys
from typing import Any

import pandas as pd
from reportlab.lib.pagesizes import A4, landscape
from reportlab.lib.units import cm
from reportlab.platypus import PageBreak, Paragraph, SimpleDocTemplate, Spacer

sys.path.insert(0, str(Path(__file__).resolve().parent))

from build_volume_breakout_operation_pdf_preview import MARKDOWN_HEADERS, now_text  # noqa: E402
from build_volume_breakout_operation_pdf_preview_pdf import add_table, style_map  # noqa: E402
from tracking_utils import LATEST_DIR, safe_str  # noqa: E402


ROOT = Path(".")
MODEL_REGISTRY_CSV = LATEST_DIR / "daily_report_model_registry_latest.csv"
MODEL_PARAMS_CSV = LATEST_DIR / "daily_candidate_model_parameters_latest.csv"
VOLUME_PREVIEW_CSV = LATEST_DIR / "volume_breakout_operation_pdf_preview_latest.csv"
FORMAT_PREVIEW_PDF = LATEST_DIR / "research_operation_pdf_format_preview_latest.pdf"

PDF_MODEL_VISIBILITY = {"pdf_core_model", "pdf_specialty_section"}

CONFIRMED_COLUMNS = [
    "display_order",
    "stock_display",
    "operation_status_zh",
    "trigger_zh",
    "entry_basis_zh",
    "stop_basis_zh",
    "sample_size",
    "win_rate_zh",
    "median_return_zh",
    "pdf_note_zh",
]
ACTIVE_COLUMNS = [
    "display_order",
    "stock_display",
    "operation_status_zh",
    "entry_basis_zh",
    "stop_basis_zh",
    "holding_age_zh",
    "planned_exit_zh",
    "pdf_note_zh",
]
PENDING_COLUMNS = [
    "display_order",
    "stock_display",
    "operation_status_zh",
    "pending_age_zh",
    "pending_group_zh",
    "stop_basis_zh",
    "same_stock_pending_count",
    "pdf_note_zh",
]


def read_csv(path: Path) -> pd.DataFrame:
    if not path.exists():
        return pd.DataFrame()
    try:
        return pd.read_csv(path, dtype=str, keep_default_na=False)
    except Exception:
        return pd.DataFrame()


def pdf_models() -> pd.DataFrame:
    registry = read_csv(MODEL_REGISTRY_CSV)
    params = read_csv(MODEL_PARAMS_CSV)
    if registry.empty:
        return pd.DataFrame(columns=["model_id", "model_name_zh", "model_registry_order", "pdf_visibility"])
    if not params.empty and {"model_id", "pdf_visibility"}.issubset(params.columns):
        registry = registry.merge(
            params[["model_id", "pdf_visibility", "recommended_usage", "recommended_sample_status"]],
            on="model_id",
            how="left",
        )
    else:
        registry["pdf_visibility"] = ""
        registry["recommended_usage"] = ""
        registry["recommended_sample_status"] = ""
    active = registry[registry.get("model_registry_active", "").astype(str).str.lower().eq("true")].copy()
    active = active[active["pdf_visibility"].astype(str).isin(PDF_MODEL_VISIBILITY)].copy()
    active["_order"] = pd.to_numeric(active.get("model_registry_order"), errors="coerce").fillna(999)
    return active.sort_values(["_order", "model_id"]).drop(columns=["_order"])


def volume_section(preview: pd.DataFrame, section: str) -> pd.DataFrame:
    if preview.empty:
        return pd.DataFrame()
    return preview[
        preview.get("pdf_view", "").astype(str).eq("highlight")
        & preview.get("pdf_section", "").astype(str).eq(section)
    ].copy()


def empty_table_note(model_name: str, state_name: str) -> str:
    return f"{model_name} 目前沒有{state_name}資料；若此模型尚未接入 historical operation research，先固定顯示空表格。"


def model_summary_rows(models: pd.DataFrame, volume_preview: pd.DataFrame) -> pd.DataFrame:
    rows: list[dict[str, Any]] = []
    volume_confirmed = len(volume_section(volume_preview, "confirmed_operation"))
    volume_pending = len(volume_section(volume_preview, "pending_confirmation"))
    for idx, (_, row) in enumerate(models.iterrows(), start=1):
        model_id = safe_str(row.get("model_id"))
        if model_id == "volume_range_breakout":
            research_status = f"已接入：已確認 {volume_confirmed}，操作中 0，待確認 {volume_pending}"
        else:
            research_status = "尚未接入操作回測；保留固定表格"
        rows.append(
            {
                "display_order": idx,
                "model_id": model_id,
                "model_name_zh": safe_str(row.get("model_name_zh")),
                "pdf_visibility": safe_str(row.get("pdf_visibility")),
                "recommended_usage": safe_str(row.get("recommended_usage")),
                "research_status_zh": research_status,
            }
        )
    return pd.DataFrame(rows)


def build_pdf() -> None:
    models = pdf_models()
    volume_preview = read_csv(VOLUME_PREVIEW_CSV)
    styles = style_map()
    doc = SimpleDocTemplate(
        str(FORMAT_PREVIEW_PDF),
        pagesize=landscape(A4),
        leftMargin=0.8 * cm,
        rightMargin=0.8 * cm,
        topMargin=0.9 * cm,
        bottomMargin=0.8 * cm,
        title="全模型操作表格格式 Preview",
        author="tdcc-weekly-report research backtest",
    )
    story: list[Any] = [
        Paragraph("全模型操作表格格式 Preview", styles["title"]),
        Paragraph(
            (
                f"產生時間：{now_text()}。這份 PDF 是格式預演，不是正式 daily production PDF。"
                "目的：先固定所有模型的操作表格版面，避免正式接入時才改欄位。"
            ),
            styles["note"],
        ),
        Paragraph("每個模型都固定顯示：已確認可進場、操作中、待確認。沒有資料也必須有空表格。", styles["note"]),
    ]

    summary = model_summary_rows(models, volume_preview)
    add_table(
        story,
        "模型覆蓋狀態",
        summary,
        ["display_order", "model_name_zh", "pdf_visibility", "recommended_usage", "research_status_zh"],
        [1.0, 5.0, 3.0, 3.0, 12.0],
        styles,
        "目前沒有可顯示的 PDF core model。",
    )
    story.append(PageBreak())

    volume_confirmed = volume_section(volume_preview, "confirmed_operation")
    volume_pending = volume_section(volume_preview, "pending_confirmation")
    active_empty = pd.DataFrame()

    for model_idx, (_, model) in enumerate(models.iterrows(), start=1):
        model_id = safe_str(model.get("model_id"))
        model_name = safe_str(model.get("model_name_zh")) or model_id
        if model_idx > 1:
            story.append(PageBreak())
        story.append(Paragraph(f"{model_idx}. {model_name}", styles["title"]))
        story.append(
            Paragraph(
                f"model_id：{model_id}。本頁固定測試三個操作狀態表格；正式接入時只能讀 research artifact，不在 PDF 端重算。",
                styles["note"],
            )
        )
        confirmed = volume_confirmed if model_id == "volume_range_breakout" else pd.DataFrame()
        pending = volume_pending if model_id == "volume_range_breakout" else pd.DataFrame()
        no_research_suffix = "" if model_id == "volume_range_breakout" else "此模型尚未接入操作回測，"

        add_table(
            story,
            "已確認可進場",
            confirmed,
            CONFIRMED_COLUMNS,
            [1.0, 3.0, 1.7, 2.5, 3.2, 3.7, 1.4, 1.6, 2.0, 6.0],
            styles,
            f"{no_research_suffix}{empty_table_note(model_name, '已確認可進場')}",
        )
        add_table(
            story,
            "操作中",
            active_empty,
            ACTIVE_COLUMNS,
            [1.0, 3.2, 1.8, 3.4, 4.0, 2.4, 4.2, 8.0],
            styles,
            f"{no_research_suffix}{empty_table_note(model_name, '操作中')}",
        )
        add_table(
            story,
            "待確認",
            pending,
            PENDING_COLUMNS,
            [1.0, 3.2, 1.8, 3.2, 4.0, 4.0, 1.8, 8.0],
            styles,
            f"{no_research_suffix}{empty_table_note(model_name, '待確認')}",
        )
        story.append(Spacer(1, 0.1 * cm))

    FORMAT_PREVIEW_PDF.parent.mkdir(parents=True, exist_ok=True)
    doc.build(story)


def main() -> int:
    build_pdf()
    print(f"Saved: {FORMAT_PREVIEW_PDF}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
