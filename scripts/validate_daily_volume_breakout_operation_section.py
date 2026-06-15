from __future__ import annotations

from pathlib import Path

import pandas as pd


ROOT = Path(__file__).resolve().parents[1]
LATEST_DIR = ROOT / "output" / "latest"
DOCS_LATEST_DIR = ROOT / "docs" / "latest"

SECTION_CSV = LATEST_DIR / "daily_volume_breakout_operation_section_latest.csv"
SECTION_MD = LATEST_DIR / "daily_volume_breakout_operation_section_latest.md"
TAXONOMY_CSV = LATEST_DIR / "stock_theme_taxonomy_latest.csv"
DOCS_SECTION_CSV = DOCS_LATEST_DIR / SECTION_CSV.name
DOCS_SECTION_MD = DOCS_LATEST_DIR / SECTION_MD.name
PDF_GENERATOR = ROOT / "scripts" / "generate_chatgpt_side_daily_reports.py"
PACKET_BUILDER = ROOT / "build_chatgpt_daily_report_packet.py"
CONTRACT_MD = ROOT / "docs" / "specs" / "daily_volume_breakout_operation_section_contract.md"

MODEL_ID = "volume_range_breakout"
PDF_VIEWS = {"highlight", "full"}
PDF_SECTIONS = {"confirmed_operation", "pending_confirmation", "active_operation"}
ROW_TYPES = {"data", "empty_state"}
SOURCE_STATUSES = {"ready", "missing_or_empty_research_source", "stale_research_source"}

REQUIRED_COLUMNS = {
    "model_id",
    "pdf_view",
    "pdf_section",
    "pdf_section_zh",
    "row_type",
    "operation_asof_date",
    "operation_source_date_status",
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
    "approval_source",
    "approved_for_daily",
    "operation_module_approved_for_daily",
    "approval_status",
    "operation_module_id",
    "approval_version",
    "operation_directive_level",
    "row_action_status",
    "buy_rank_eligible",
    "buy_filter_id",
    "approval_note_zh",
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
    "approved_for_daily",
    "operation_module_approved_for_daily",
    "approval_status",
    "approval_version",
    "operation_directive_level",
    "row_action_status",
    "buy_rank_eligible",
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


def stock_id_text(value: object) -> str:
    text = str(value).strip().replace(".0", "")
    return text.zfill(4) if text.isdigit() else text


def split_memberships(value: object) -> set[str]:
    tokens = str(value).replace(";", "|").replace(",", "|").split("|")
    return {token.strip() for token in tokens if token.strip()}


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
    bad_date_status = sorted(set(section["operation_source_date_status"].astype(str)) - SOURCE_STATUSES)
    if bad_date_status:
        fail(f"invalid operation_source_date_status values: {bad_date_status}")

    if set(section["approved_for_daily"].astype(str)) != {"True"}:
        fail("daily volume breakout operation section must be approved_for_daily=True")
    if set(section["operation_module_approved_for_daily"].astype(str)) != {"True"}:
        fail("daily volume breakout operation section must carry operation_module_approved_for_daily=True")
    if set(section["approval_status"].astype(str)) != {"approved_for_daily_v1"}:
        fail("daily volume breakout operation section must carry approval_status=approved_for_daily_v1")
    if set(section["operation_directive_level"].astype(str)) != {"approved_daily_operation_guidance"}:
        fail("daily volume breakout operation section must carry approved daily operation guidance")
    if section["operation_module_id"].astype(str).str.strip().eq("").any():
        fail("daily volume breakout operation section must carry operation_module_id")
    if section["approval_version"].astype(str).str.strip().eq("").any():
        fail("daily volume breakout operation section must carry approval_version")

    confirmed_data = section[
        section["pdf_section"].eq("confirmed_operation") & section["row_type"].eq("data")
    ].copy()
    data_rows = section[section["row_type"].eq("data")].copy()
    if not data_rows.empty:
        bad_dates = data_rows[
            data_rows["operation_asof_date"].astype(str).ne(data_rows["daily_signal_date"].astype(str))
        ]
        if not bad_dates.empty:
            fail("operation data rows must have operation_asof_date equal to daily_signal_date")
        bad_data_status = data_rows[data_rows["adapter_source_status"].astype(str).ne("ready")]
        if not bad_data_status.empty:
            fail("operation data rows are allowed only when adapter_source_status=ready")
    stale_rows = section[section["adapter_source_status"].astype(str).eq("stale_research_source")]
    if not stale_rows.empty and stale_rows["row_type"].astype(str).ne("empty_state").any():
        fail("stale operation research source must render only empty_state rows")
    if not data_rows.empty:
        taxonomy = read_csv(TAXONOMY_CSV)
        if taxonomy.empty or "stock_id" not in taxonomy.columns:
            fail("stock_theme_taxonomy_latest.csv is required to validate operation row report routing")
        taxonomy_ids = {stock_id_text(value) for value in taxonomy["stock_id"].tolist() if stock_id_text(value)}
        missing_taxonomy = sorted(
            set(data_rows["stock_id"].map(stock_id_text).tolist()) - taxonomy_ids
        )
        if missing_taxonomy:
            fail(f"operation data rows missing stock taxonomy/basic industry source: {missing_taxonomy}")
        if "report_line_memberships" not in taxonomy.columns:
            fail("stock taxonomy must include report_line_memberships")
        taxonomy_membership = {
            stock_id_text(row.get("stock_id")): split_memberships(row.get("report_line_memberships"))
            for _, row in taxonomy.iterrows()
        }
        unrouted = sorted(
            {
                stock_id
                for stock_id in data_rows["stock_id"].map(stock_id_text).tolist()
                if not taxonomy_membership.get(stock_id)
                or bool(taxonomy_membership.get(stock_id, set()) - {"mainstream", "non_mainstream"})
            }
        )
        if unrouted:
            fail(f"operation data rows have invalid stock taxonomy report routing: {unrouted}")
    if not confirmed_data.empty:
        bad_quality = sorted(set(confirmed_data["quality_status_zh"].astype(str)) - {"正向證據"})
        if bad_quality:
            fail(f"confirmed operation rows must be positive evidence only: {bad_quality}")
        if set(confirmed_data["row_action_status"].astype(str)) != {"confirmed_buy_candidate"}:
            fail("confirmed operation data rows must carry row_action_status=confirmed_buy_candidate")
        if set(confirmed_data["buy_rank_eligible"].astype(str)) != {"True"}:
            fail("confirmed operation data rows must be buy_rank_eligible=True")

    buy_eligible = section[section["buy_rank_eligible"].astype(str).eq("True")]
    bad_buy = buy_eligible[
        ~(
            buy_eligible["pdf_section"].eq("confirmed_operation")
            & buy_eligible["row_type"].eq("data")
            & buy_eligible["row_action_status"].eq("confirmed_buy_candidate")
        )
    ]
    if not bad_buy.empty:
        fail("buy_rank_eligible=True is allowed only on confirmed_operation data rows")

    pending = section[section["pdf_section"].eq("pending_confirmation") & section["row_type"].eq("data")]
    bad_pending = pending[
        pending["buy_rank_eligible"].astype(str).ne("False")
        | pending["row_action_status"].astype(str).ne("pending_confirmation")
    ]
    if not bad_pending.empty:
        fail("pending_confirmation rows must stay buy_rank_eligible=False with row_action_status=pending_confirmation")

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
    if active["buy_rank_eligible"].astype(str).ne("False").any():
        fail("active_operation empty rows must not be buy_rank_eligible")
    if set(active["row_action_status"].astype(str)) != {"empty_state"}:
        fail("active_operation empty rows must carry row_action_status=empty_state")
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
    if "daily_volume_breakout_operation_section_latest.csv" not in source:
        fail("PDF generator must read the daily volume breakout operation adapter artifact")
    if "render_volume_range_breakout_operation_section" not in source:
        fail("PDF generator must expose an independent volume breakout operation renderer")
    forbidden = [
        "volume_breakout_operation_pdf_preview_latest.csv",
        "volume_breakout_confirmed_operation_rank_latest.csv",
        "volume_breakout_pending_operation_queue_latest.csv",
        "historical_pattern_operation_registry_latest.csv",
        "approved_operation_patterns_latest.csv",
    ]
    for token in forbidden:
        if token in source:
            fail(f"PDF generator must not read research artifact directly: {token}")


def validate_packet_builder_boundary() -> None:
    if not PACKET_BUILDER.exists():
        return
    source = PACKET_BUILDER.read_text(encoding="utf-8", errors="replace")
    if "daily_volume_breakout_operation_section_latest.csv" not in source:
        fail("packet builder must read the daily volume breakout operation adapter artifact")
    if "build_volume_operation_packet_lines" not in source:
        fail("packet builder must render the volume breakout operation adapter section")
    forbidden = [
        "volume_breakout_operation_pdf_preview_latest.csv",
        "volume_breakout_confirmed_operation_rank_latest.csv",
        "volume_breakout_pending_operation_queue_latest.csv",
        "historical_pattern_operation_registry_latest.csv",
        "approved_operation_patterns_latest.csv",
    ]
    for token in forbidden:
        if token in source:
            fail(f"packet builder must not read research artifact directly: {token}")


def main() -> int:
    validate_file_presence()
    section = read_csv(SECTION_CSV)
    validate_shape(section)
    validate_display_text(section)
    validate_pdf_generator_boundary()
    validate_packet_builder_boundary()
    print(
        "daily volume breakout operation section validation passed "
        f"rows={len(section)} "
        f"data_rows={(section['row_type'].astype(str) == 'data').sum()} "
        f"empty_rows={(section['row_type'].astype(str) == 'empty_state').sum()}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
