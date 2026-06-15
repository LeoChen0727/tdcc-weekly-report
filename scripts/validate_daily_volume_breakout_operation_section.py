from __future__ import annotations

from pathlib import Path

import pandas as pd


ROOT = Path(__file__).resolve().parents[1]
LATEST_DIR = ROOT / "output" / "latest"
DOCS_LATEST_DIR = ROOT / "docs" / "latest"

SECTION_CSV = LATEST_DIR / "daily_volume_breakout_operation_section_latest.csv"
SECTION_MD = LATEST_DIR / "daily_volume_breakout_operation_section_latest.md"
DOCS_SECTION_CSV = DOCS_LATEST_DIR / SECTION_CSV.name
DOCS_SECTION_MD = DOCS_LATEST_DIR / SECTION_MD.name
PDF_GENERATOR = ROOT / "scripts" / "generate_chatgpt_side_daily_reports.py"
CONTRACT_MD = ROOT / "docs" / "specs" / "daily_volume_breakout_operation_section_contract.md"

MODEL_ID = "volume_range_breakout"
PDF_VIEWS = {"highlight", "full"}
PDF_SECTIONS = {"confirmed_operation", "pending_confirmation", "active_operation"}
ROW_TYPES = {"data", "empty_state"}
SOURCE_STATUSES = {"ready", "missing_or_empty_research_source"}

REQUIRED_COLUMNS = {
    "model_id",
    "pdf_view",
    "pdf_section",
    "pdf_section_zh",
    "row_type",
    "display_order",
    "stock_id",
    "stock_display",
    "operation_status_zh",
    "entry_basis_zh",
    "stop_basis_zh",
    "exit_rule_zh",
    "sample_size",
    "win_rate_zh",
    "median_return_zh",
    "daily_signal_date",
    "daily_volume_model_signal_count",
    "adapter_source",
    "adapter_source_status",
    "adapter_note_zh",
    "generated_at",
}

DISPLAY_COLUMNS = [
    "pdf_section_zh",
    "stock_display",
    "operation_status_zh",
    "quality_status_zh",
    "trigger_zh",
    "entry_basis_zh",
    "entry_price_status_zh",
    "stop_basis_zh",
    "exit_rule_zh",
    "pending_age_zh",
    "pending_group_zh",
    "pending_confirmation_zh",
    "tdcc_status_zh",
    "win_rate_zh",
    "avg_return_zh",
    "median_return_zh",
    "confidence_zh",
    "pdf_note_zh",
    "adapter_note_zh",
]

FORBIDDEN_DISPLAY_TOKENS = [
    "signal_low",
    "next_open",
    "pullback_5ma_confirmed",
    "pullback_10ma_confirmed",
    "next_day_continuation_confirmed",
]


def fail(message: str) -> None:
    print(f"ERROR: {message}")
    raise SystemExit(1)


def read_csv(path: Path) -> pd.DataFrame:
    try:
        return pd.read_csv(path, dtype=str, keep_default_na=False)
    except Exception as exc:
        fail(f"{path} is not readable CSV: {exc}")


def validate_file_presence() -> None:
    for path in [SECTION_CSV, SECTION_MD, DOCS_SECTION_CSV, DOCS_SECTION_MD, CONTRACT_MD]:
        if not path.exists():
            fail(f"missing required file: {path.relative_to(ROOT).as_posix()}")


def validate_shape(section: pd.DataFrame) -> None:
    if section.empty:
        fail(f"{SECTION_CSV.relative_to(ROOT).as_posix()} has no rows")
    missing = sorted(REQUIRED_COLUMNS - set(section.columns))
    if missing:
        fail(f"daily volume breakout operation section missing columns: {missing}")

    bad_models = sorted(set(section["model_id"].astype(str)) - {MODEL_ID})
    if bad_models:
        fail(f"daily volume breakout operation section must not include other models: {bad_models}")

    bad_views = sorted(set(section["pdf_view"].astype(str)) - PDF_VIEWS)
    if bad_views:
        fail(f"invalid pdf_view values: {bad_views}")

    bad_sections = sorted(set(section["pdf_section"].astype(str)) - PDF_SECTIONS)
    if bad_sections:
        fail(f"invalid pdf_section values: {bad_sections}")

    bad_row_types = sorted(set(section["row_type"].astype(str)) - ROW_TYPES)
    if bad_row_types:
        fail(f"invalid row_type values: {bad_row_types}")

    bad_status = sorted(set(section["adapter_source_status"].astype(str)) - SOURCE_STATUSES)
    if bad_status:
        fail(f"invalid adapter_source_status values: {bad_status}")

    for view in PDF_VIEWS:
        for section_id in PDF_SECTIONS:
            part = section[section["pdf_view"].eq(view) & section["pdf_section"].eq(section_id)]
            if part.empty:
                fail(f"missing {view}/{section_id} section row")

    active = section[section["pdf_section"].eq("active_operation")]
    if active.empty:
        fail("active_operation section is required even when empty")
    if set(active["row_type"].astype(str)) != {"empty_state"}:
        fail("active_operation must remain an explicit empty table until a holding-tracker source exists")
    if not active["adapter_note_zh"].astype(str).str.contains("操作中").any():
        fail("active_operation empty row must explain operation-in-progress status")


def validate_display_text(section: pd.DataFrame) -> None:
    display_text = "\n".join(
        section[col].astype(str).str.cat(sep="\n") for col in DISPLAY_COLUMNS if col in section.columns
    )
    for token in FORBIDDEN_DISPLAY_TOKENS:
        if token in display_text:
            fail(f"forbidden raw display token leaked: {token}")
    if "median" in display_text.lower():
        fail("display text must use Chinese wording for median return, not raw 'median'")
    if "目前無資料" not in display_text:
        fail("empty-state display text must be present for PDF empty tables")


def validate_pdf_generator_boundary() -> None:
    if not PDF_GENERATOR.exists():
        return
    source = PDF_GENERATOR.read_text(encoding="utf-8", errors="replace")
    forbidden = [
        "volume_breakout_operation_pdf_preview_latest.csv",
        "volume_breakout_confirmed_operation_rank_latest.csv",
        "volume_breakout_pending_operation_queue_latest.csv",
        "historical_pattern_operation_registry_latest.csv",
    ]
    for token in forbidden:
        if token in source:
            fail(f"PDF generator must not read research artifact directly: {token}")


def main() -> int:
    validate_file_presence()
    section = read_csv(SECTION_CSV)
    validate_shape(section)
    validate_display_text(section)
    validate_pdf_generator_boundary()
    print(
        "daily volume breakout operation section validation passed "
        f"rows={len(section)} "
        f"data_rows={(section['row_type'].astype(str) == 'data').sum()} "
        f"empty_rows={(section['row_type'].astype(str) == 'empty_state').sum()}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
