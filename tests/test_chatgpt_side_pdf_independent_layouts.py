from __future__ import annotations

from pathlib import Path

from scripts import validate_chatgpt_side_pdf_layout_independence as validator


ROOT = Path(__file__).resolve().parents[1]
GENERATOR = ROOT / "scripts" / "generate_chatgpt_side_daily_reports.py"
INVENTORY = ROOT / "docs" / "daily_pdf_template_independence_inventory.md"


def _source() -> str:
    return GENERATOR.read_text(encoding="utf-8", errors="replace")


def _function_text(text: str, name: str) -> str:
    start = text.index(f"def {name}(")
    next_def = text.find("\ndef ", start + 1)
    end = len(text) if next_def == -1 else next_def
    return text[start:end]


def test_pdf_layout_independence_validator_passes() -> None:
    assert validator.main() == 0


def test_chatgpt_side_pdf_builders_are_explicit_independent_entrypoints() -> None:
    text = _source()
    main_text = _function_text(text, "main")

    for name in validator.PDF_BUILDERS:
        assert f"def {name}(" in text
        assert f"{name}(" in main_text

    assert "build_curated_pdf_for_line" not in text
    assert "build_full_candidate_pdf_for_line" not in text
    assert "line_titles(" not in text
    assert "LINE_TITLE_MAP" not in text


def test_stock_pdf_layout_builders_do_not_share_line_dispatch() -> None:
    text = _source()

    for name in validator.STOCK_PDF_BUILDERS:
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

    for name in validator.REPORT_SPECIFIC_LAYOUT_COMPONENTS:
        assert f"def {name}(" in text

    for forbidden in validator.FORBIDDEN_SHARED_LAYOUT_ENTRIES:
        assert forbidden not in text


def test_daily_pdf_template_independence_inventory_marks_fixed_path_retired() -> None:
    text = INVENTORY.read_text(encoding="utf-8", errors="replace")

    for marker in validator.REQUIRED_INVENTORY_MARKERS:
        assert marker in text
    assert "scripts/generate_daily_market_pdf.py::" not in text
