from __future__ import annotations

from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
GENERATOR = ROOT / "scripts" / "generate_chatgpt_side_daily_reports.py"
PRODUCTION_GENERATOR = ROOT / "scripts" / "generate_daily_market_pdf.py"
TDCC_WEEKLY_GENERATOR = ROOT / "scripts" / "build_tdcc_weekly_candidate_reports.py"
SIGNAL_PERFORMANCE_GENERATOR = ROOT / "scripts" / "generate_daily_signal_performance_report.py"
INDIVIDUAL_STOCK_GENERATOR = ROOT / "scripts" / "generate_individual_stock_report.py"
WARRANT_GENERATOR = ROOT / "scripts" / "build_warrant_market_report.py"
MARKET_RISK_GENERATOR = ROOT / "scripts" / "build_market_regime_dashboard.py"
INVENTORY = ROOT / "docs" / "daily_pdf_template_independence_inventory.md"

PDF_BUILDERS = [
    "build_mainstream_curated_pdf",
    "build_mainstream_full_candidate_pdf",
    "build_non_mainstream_curated_pdf",
    "build_non_mainstream_full_candidate_pdf",
    "build_warrant_market_auxiliary_pdf",
    "build_market_risk_background_pdf",
]

STOCK_PDF_BUILDERS = PDF_BUILDERS[:4]

PRODUCTION_STOCK_PDF_BUILDERS = {
    "build_mainstream_daily_recommendation_highlight_pdf": "mainstream_highlight",
    "build_mainstream_full_candidate_list_pdf": "mainstream_full",
    "build_non_mainstream_daily_recommendation_highlight_pdf": "non_mainstream_highlight",
    "build_non_mainstream_full_candidate_list_pdf": "non_mainstream_full",
}

PRODUCTION_DAILY_PDF_ENTRYPOINTS = [
    "build_curated_pdf",
    "build_full_table_pdf",
    *PRODUCTION_STOCK_PDF_BUILDERS.keys(),
]

OTHER_PDF_TEMPLATE_ENTRYPOINTS = {
    TDCC_WEEKLY_GENERATOR: [
        "write_tdcc_weekly_highlight_pdf",
        "write_tdcc_weekly_full_pdf",
    ],
    SIGNAL_PERFORMANCE_GENERATOR: [
        "write_weekly_signal_performance_pdf_from_markdown",
        "write_monthly_signal_performance_pdf_from_markdown",
    ],
    INDIVIDUAL_STOCK_GENERATOR: ["build_pdf"],
    WARRANT_GENERATOR: ["write_pdf"],
    MARKET_RISK_GENERATOR: ["build_pdf"],
}

REPORT_SPECIFIC_LAYOUT_COMPONENTS = [
    "build_mainstream_curated_model_table",
    "build_mainstream_full_model_table",
    "build_non_mainstream_curated_model_table",
    "build_non_mainstream_full_model_table",
    "append_mainstream_curated_group_rotation_end_section",
    "append_mainstream_full_group_rotation_end_section",
    "append_non_mainstream_curated_group_rotation_end_section",
    "append_non_mainstream_full_group_rotation_end_section",
    "build_mainstream_curated_operation_page",
    "build_non_mainstream_curated_operation_page",
]

REPORT_SPECIFIC_MODEL_TABLE_BUILDERS = [
    "build_mainstream_curated_model_table",
    "build_mainstream_full_model_table",
    "build_non_mainstream_curated_model_table",
    "build_non_mainstream_full_model_table",
]

FORBIDDEN_SHARED_LAYOUT_ENTRIES = [
    "def build_curated_pdf_for_line(",
    "def build_full_candidate_pdf_for_line(",
    "def model_split_table(",
    "def model_recommendation_rows_for_line(",
    "def model_front_observation_rows_for_line(",
    "def append_group_rotation_end_section(",
    "def build_operation_page(",
    "def operation_representatives(",
    "line_titles(",
    "LINE_TITLE_MAP",
]

FORBIDDEN_PRODUCTION_SHARED_LAYOUT_CALLS = [
    "build_model_line_pdf(",
    "for model_name in _model_names_in_report_order(",
    "group = _rows_for_model_section(",
    "make_table(_detail_table_rows_for_section(",
    "story.append(_model_signal_card_readable(",
    "_append_theme_event_watch_section_readable(story,",
    "_append_group_rotation_section_readable(story,",
]

FORBIDDEN_PRODUCTION_SHARED_RENDERER_ENTRIES = [
    "def _model_names_in_report_order(",
    "def _rows_for_model_section(",
    "def _summary_rows_for_section(",
    "def _fixed_model_summary_rows(",
    "def _detail_table_rows_for_section(",
    "def _model_signal_card_readable(",
    "def _append_theme_event_watch_section_readable(",
    "def _append_group_rotation_section_readable(",
]

FORBIDDEN_CHATGPT_SIDE_BUILDER_CALLS = [
    "for spec in core_model_specs(",
    "= model_signal_rows(inputs,",
]

FORBIDDEN_OTHER_SHARED_TEMPLATE_ENTRIES = {
    TDCC_WEEKLY_GENERATOR: [
        "def write_pdf(",
        "def write_pdf_v2(",
        "write_pdf_v2(",
    ],
    SIGNAL_PERFORMANCE_GENERATOR: [
        "def write_pdf_from_markdown(",
        "write_pdf_from_markdown(",
    ],
}

FORMAL_PDF_PATHS = [
    "output/latest/mainstream_daily_recommendation_highlight_latest.pdf",
    "output/latest/mainstream_full_candidate_list_latest.pdf",
    "output/latest/non_mainstream_daily_recommendation_highlight_latest.pdf",
    "output/latest/non_mainstream_full_candidate_list_latest.pdf",
    "output/latest/warrant_market_report_latest.pdf",
    "output/latest/market_risk_dashboard_latest.pdf",
]


def function_text(text: str, name: str) -> str:
    start = text.index(f"def {name}(")
    next_def = text.find("\ndef ", start + 1)
    end = len(text) if next_def == -1 else next_def
    return text[start:end]


def validate() -> list[str]:
    errors: list[str] = []
    text = GENERATOR.read_text(encoding="utf-8", errors="replace")
    production_text = PRODUCTION_GENERATOR.read_text(encoding="utf-8", errors="replace")
    other_texts = {
        path: path.read_text(encoding="utf-8", errors="replace")
        for path in OTHER_PDF_TEMPLATE_ENTRYPOINTS
    }

    if not INVENTORY.exists():
        errors.append("missing daily PDF template independence inventory")
    else:
        inventory_text = INVENTORY.read_text(encoding="utf-8", errors="replace")
        for pdf_path in FORMAL_PDF_PATHS:
            if pdf_path not in inventory_text:
                errors.append(f"inventory missing formal PDF path: {pdf_path}")
        for marker in [
            "PDF Template Scope",
            "Generic stock-PDF dispatchers",
            "TDCC weekly PDF writers",
            "Signal performance PDF writers",
            "volume_range_breakout",
            "New-listed and consecutive/repeated-listed",
        ]:
            if marker not in inventory_text:
                errors.append(f"inventory missing required boundary marker: {marker}")

    for name in PDF_BUILDERS:
        if f"def {name}(" not in text:
            errors.append(f"missing explicit PDF builder: {name}")

    for name in REPORT_SPECIFIC_LAYOUT_COMPONENTS:
        if f"def {name}(" not in text:
            errors.append(f"missing report-specific layout component: {name}")

    for name in REPORT_SPECIFIC_MODEL_TABLE_BUILDERS:
        try:
            body = function_text(text, name)
        except ValueError:
            continue
        signature_block = "\n".join(body.splitlines()[:8])
        if "-> list" not in signature_block:
            errors.append(f"{name} must return split section flowables, not one shared table")
        for marker in ["新上榜", "重複上榜"]:
            if marker not in body:
                errors.append(f"{name} missing split listing section marker: {marker}")
        for color in ['"#c00000"', '"#1f4e79"']:
            if color not in body:
                errors.append(f"{name} missing distinct listing section color: {color}")
        if "return build_table(" in body:
            errors.append(f"{name} still returns a single model table")

    for forbidden in FORBIDDEN_SHARED_LAYOUT_ENTRIES:
        if forbidden in text:
            errors.append(f"forbidden shared PDF layout entry remains: {forbidden}")

    try:
        main_text = function_text(text, "main")
    except ValueError:
        errors.append("missing main()")
        main_text = ""
    for name in PDF_BUILDERS:
        if f"{name}(" not in main_text:
            errors.append(f"main() does not call explicit PDF builder: {name}")

    for name in STOCK_PDF_BUILDERS:
        try:
            body = function_text(text, name)
        except ValueError:
            continue
        signature = body.splitlines()[0]
        if "line:" in signature:
            errors.append(f"{name} still accepts a line parameter")
        for forbidden in [
            'if line == "mainstream"',
            'if line != "mainstream"',
            "MAIN_REPORT_MAINSTREAM_LIMIT if line",
            "FULL_REPORT_MAINSTREAM_LIMIT if line",
            "line_titles(",
        ]:
            if forbidden in body:
                errors.append(f"{name} still contains line-dispatch layout logic: {forbidden}")

        for forbidden in FORBIDDEN_CHATGPT_SIDE_BUILDER_CALLS:
            if forbidden in body:
                errors.append(f"{name} still calls shared ChatGPT-side model loop: {forbidden}")

    for name, namespace in PRODUCTION_STOCK_PDF_BUILDERS.items():
        if f"def {name}(" not in production_text:
            errors.append(f"missing production PDF builder: {name}")
            continue
        body = function_text(production_text, name)
        for forbidden in FORBIDDEN_PRODUCTION_SHARED_LAYOUT_CALLS:
            if forbidden in body:
                errors.append(f"{name} still calls shared production layout path: {forbidden}")
        if f"{namespace}_" not in body:
            errors.append(f"{name} does not call its report-specific renderer namespace: {namespace}_")

    if "def build_model_line_pdf(" in production_text:
        errors.append("production generator still contains generic build_model_line_pdf dispatcher")

    for name in PRODUCTION_DAILY_PDF_ENTRYPOINTS:
        if f"def {name}(" not in production_text:
            errors.append(f"missing daily production PDF template entrypoint: {name}")

    for forbidden in FORBIDDEN_PRODUCTION_SHARED_RENDERER_ENTRIES:
        if forbidden in production_text:
            errors.append(f"production generator still contains shared high-level renderer: {forbidden}")

    for path, entrypoints in OTHER_PDF_TEMPLATE_ENTRYPOINTS.items():
        text_for_path = other_texts[path]
        for name in entrypoints:
            if f"def {name}(" not in text_for_path:
                errors.append(f"missing PDF template entrypoint {path.name}::{name}")

    for path, forbidden_entries in FORBIDDEN_OTHER_SHARED_TEMPLATE_ENTRIES.items():
        text_for_path = other_texts[path]
        for forbidden in forbidden_entries:
            if forbidden in text_for_path:
                errors.append(f"forbidden shared PDF template entry remains in {path.name}: {forbidden}")

    return errors


def main() -> int:
    errors = validate()
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1
    print("chatgpt-side PDF layout independence validation passed")
    for name in PDF_BUILDERS:
        print(f"validated_builder={name}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

