from __future__ import annotations

from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
GENERATOR = ROOT / "scripts" / "generate_chatgpt_side_daily_reports.py"

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


def function_text(text: str, name: str) -> str:
    start = text.index(f"def {name}(")
    next_def = text.find("\ndef ", start + 1)
    end = len(text) if next_def == -1 else next_def
    return text[start:end]


def style_text(text: str, name: str, next_name: str) -> str:
    start = text.index(f"{name} = ParagraphStyle(")
    end = text.index(f"{next_name} = ParagraphStyle(", start + 1)
    return text[start:end]


def validate() -> list[str]:
    errors: list[str] = []
    text = GENERATOR.read_text(encoding="utf-8", errors="replace")

    for name in PDF_BUILDERS:
        if f"def {name}(" not in text:
            errors.append(f"missing explicit PDF builder: {name}")

    for name in REPORT_SPECIFIC_LAYOUT_COMPONENTS:
        if f"def {name}(" not in text:
            errors.append(f"missing report-specific layout component: {name}")

    for forbidden in FORBIDDEN_SHARED_LAYOUT_ENTRIES:
        if forbidden in text:
            errors.append(f"forbidden shared PDF layout entry remains: {forbidden}")

    try:
        h1_text = style_text(text, "H1", "H2")
        h2_text = style_text(text, "H2", "OP_LABEL")
    except ValueError:
        errors.append("missing H1/H2 group heading styles")
        h1_text = ""
        h2_text = ""
    for name, body, expected_size in [("H1", h1_text, "fontSize=18"), ("H2", h2_text, "fontSize=15")]:
        if "fontName=FONT_BOLD" not in body:
            errors.append(f"{name} group heading style must use bold font")
        if expected_size not in body:
            errors.append(f"{name} group heading style must keep the approved larger font size")
        if 'textColor=colors.HexColor("#c00000")' not in body:
            errors.append(f"{name} group heading style must stay red")

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
