from __future__ import annotations

from pathlib import Path

import pandas as pd


ROOT = Path(".")
LATEST_DIR = ROOT / "output" / "latest"
FORMAT_PREVIEW_PDF = LATEST_DIR / "research_operation_pdf_format_preview_latest.pdf"
MODEL_REGISTRY_CSV = LATEST_DIR / "daily_report_model_registry_latest.csv"
MODEL_PARAMS_CSV = LATEST_DIR / "daily_candidate_model_parameters_latest.csv"
FORMAT_SPEC_MD = ROOT / "docs" / "specs" / "research_operation_pdf_format_spec.md"


def fail(message: str) -> None:
    print(f"ERROR: {message}")
    raise SystemExit(1)


def read_pdf_text(path: Path) -> tuple[int, str]:
    try:
        from pypdf import PdfReader
    except Exception as exc:
        fail(f"pypdf unavailable while validating {path}: {exc}")
    try:
        reader = PdfReader(str(path))
        text = "\n".join(page.extract_text() or "" for page in reader.pages)
        return len(reader.pages), text
    except Exception as exc:
        fail(f"{path} is not readable PDF: {exc}")


def expected_pdf_model_count() -> int:
    registry = pd.read_csv(MODEL_REGISTRY_CSV, dtype=str, keep_default_na=False)
    params = pd.read_csv(MODEL_PARAMS_CSV, dtype=str, keep_default_na=False)
    merged = registry.merge(params[["model_id", "pdf_visibility"]], on="model_id", how="left")
    active = merged[merged["model_registry_active"].astype(str).str.lower().eq("true")]
    return int(active["pdf_visibility"].astype(str).isin({"pdf_core_model", "pdf_specialty_section"}).sum())


def main() -> int:
    if not FORMAT_PREVIEW_PDF.exists():
        fail(f"missing required PDF: {FORMAT_PREVIEW_PDF}")
    if not FORMAT_SPEC_MD.exists():
        fail(f"missing required spec: {FORMAT_SPEC_MD}")
    if FORMAT_PREVIEW_PDF.stat().st_size < 10000:
        fail(f"format preview PDF too small: {FORMAT_PREVIEW_PDF}")
    pages, text = read_pdf_text(FORMAT_PREVIEW_PDF)
    model_count = expected_pdf_model_count()
    if pages < max(2, model_count):
        fail(f"format preview PDF pages too small: pages={pages} model_count={model_count}")
    for token in [
        "全模型操作表格格式 Preview",
        "模型覆蓋狀態",
        "已確認可進場",
        "操作中",
        "待確認",
        "沒有資料也必須有空表格",
        "尚未接入操作回測",
        "放量攻擊模型",
        "TDCC短線延續模型",
    ]:
        if token not in text:
            fail(f"format preview PDF missing required text: {token}")
    print(
        "research operation PDF format preview validation passed "
        f"pages={pages} pdf_core_models={model_count}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
