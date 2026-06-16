from __future__ import annotations

from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
GENERATOR = ROOT / "scripts" / "generate_chatgpt_side_daily_reports.py"
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

FORBIDDEN_CHATGPT_SIDE_BUILDER_CALLS = [
    "for spec in core_model_specs(",
    "= model_signal_rows(inputs,",
]

REQUIRED_INVENTORY_MARKERS = [
    "PDF Template Scope",
    "ChatGPT-side mainstream curated",
    "ChatGPT-side mainstream full",
    "ChatGPT-side non-mainstream curated",
    "ChatGPT-side non-mainstream full",
    "ChatGPT-side warrant auxiliary",
    "ChatGPT-side market risk/background",
    "Retired Fixed Daily Market PDF Path",
    "Generic stock-PDF dispatchers",
    "TDCC weekly PDF writers",
    "Signal performance PDF writers",
    "volume_range_breakout",
    "New-listed and consecutive/repeated-listed",
]


def read_text(path: Path) -> str:
    if not path.exists():
        raise FileNotFoundError(path)
    return path.read_text(encoding="utf-8", errors="replace")


def function_text(text: str, name: str) -> str:
    start = text.index(f"def {name}(")
    next_def = text.find("\ndef ", start + 1)
    end = len(text) if next_def == -1 else next_def
    return text[start:end]


def validate() -> list[str]:
    errors: list[str] = []
    text = read_text(GENERATOR)
    other_texts = {
        path: read_text(path)
        for path in OTHER_PDF_TEMPLATE_ENTRYPOINTS
    }

    if not INVENTORY.exists():
        errors.append("missing daily PDF template independence inventory")
    else:
        inventory_text = read_text(INVENTORY)
        for marker in REQUIRED_INVENTORY_MARKERS:
            if marker not in inventory_text:
                errors.append(f"inventory missing required boundary marker: {marker}")
        if "scripts/generate_daily_market_pdf.py::" in inventory_text:
            errors.append("inventory must not list retired fixed daily market PDF builders as active template scope")

    for name in PDF_BUILDERS:
        if f"def {name}(" not in text:
            errors.append(f"missing explicit ChatGPT-side PDF builder: {name}")

    for name in REPORT_SPECIFIC_LAYOUT_COMPONENTS:
        if f"def {name}(" not in text:
            errors.append(f"missing report-specific layout component: {name}")

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
            errors.append(f"main() does not call explicit ChatGPT-side PDF builder: {name}")

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

    for path, entrypoints in OTHER_PDF_TEMPLATE_ENTRYPOINTS.items():
        text_for_path = other_texts[path]
        for name in entrypoints:
            if f"def {name}(" not in text_for_path:
                errors.append(f"missing PDF template entrypoint {path.name}::{name}")

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
