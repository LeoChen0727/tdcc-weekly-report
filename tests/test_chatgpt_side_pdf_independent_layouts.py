from __future__ import annotations

from pathlib import Path

from scripts import validate_chatgpt_side_pdf_layout_independence as validator


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

REPORT_SPECIFIC_TABLE_BUILDERS = [
    "build_mainstream_curated_model_table",
    "build_mainstream_full_model_table",
    "build_non_mainstream_curated_model_table",
    "build_non_mainstream_full_model_table",
]

REPORT_SPECIFIC_GROUP_APPENDERS = [
    "append_mainstream_curated_group_rotation_end_section",
    "append_mainstream_full_group_rotation_end_section",
    "append_non_mainstream_curated_group_rotation_end_section",
    "append_non_mainstream_full_group_rotation_end_section",
]


def _source() -> str:
    return GENERATOR.read_text(encoding="utf-8", errors="replace")


def _function_text(text: str, name: str) -> str:
    start = text.index(f"def {name}(")
    next_def = text.find("\ndef ", start + 1)
    end = len(text) if next_def == -1 else next_def
    return text[start:end]


def test_six_chatgpt_side_pdf_builders_are_explicit_independent_entrypoints() -> None:
    text = _source()
    main_text = _function_text(text, "main")

    for name in PDF_BUILDERS:
        assert f"def {name}(" in text
        assert f"{name}(" in main_text

    assert "build_curated_pdf_for_line" not in text
    assert "build_full_candidate_pdf_for_line" not in text
    assert "line_titles(" not in text
    assert "LINE_TITLE_MAP" not in text


def test_pdf_layout_independence_validator_passes() -> None:
    assert validator.main() == 0


def test_stock_pdf_layout_builders_do_not_share_line_dispatch() -> None:
    text = _source()

    for name in STOCK_PDF_BUILDERS:
        function_text = _function_text(text, name)
        signature = function_text.splitlines()[0]

        assert "line:" not in signature
        assert "line_titles(" not in function_text
        assert 'if line == "mainstream"' not in function_text
        assert 'if line != "mainstream"' not in function_text
        assert "MAIN_REPORT_MAINSTREAM_LIMIT if line" not in function_text
        assert "FULL_REPORT_MAINSTREAM_LIMIT if line" not in function_text


def test_candidate_pdf_layout_components_are_report_specific() -> None:
    text = _source()

    for name in REPORT_SPECIFIC_TABLE_BUILDERS:
        assert f"def {name}(" in text
    for name in REPORT_SPECIFIC_GROUP_APPENDERS:
        assert f"def {name}(" in text

    assert "def model_split_table(" not in text
    assert "def model_recommendation_rows_for_line(" not in text
    assert "def model_front_observation_rows_for_line(" not in text
    assert "def append_group_rotation_end_section(" not in text
    assert "def build_operation_page(" not in text
    assert "def operation_representatives(" not in text
