from __future__ import annotations

from pathlib import Path

from scripts import generate_chatgpt_side_daily_reports as generator


ROOT = Path(__file__).resolve().parents[1]


def test_append_page_break_once_does_not_duplicate_consecutive_breaks() -> None:
    story: list[object] = []

    generator.append_page_break_once(story)
    generator.append_page_break_once(story)

    assert len(story) == 1
    assert isinstance(story[-1], generator.PageBreak)

    story.append(object())
    generator.append_page_break_once(story)

    assert len(story) == 3
    assert isinstance(story[-1], generator.PageBreak)


def test_curated_pdf_uses_single_pagebreak_helper_before_model_sections() -> None:
    text = (ROOT / "scripts" / "generate_chatgpt_side_daily_reports.py").read_text(
        encoding="utf-8",
        errors="replace",
    )
    start = text.index("def build_curated_pdf_for_line(")
    end = text.index("\ndef build_full_candidate_pdf_for_line(", start)
    function_text = text[start:end]

    assert "append_page_break_once(story)\n        story.append(Paragraph(model_name, H1))" in function_text
    assert "build_operation_page(row, all_map, two_map, story, vol_map)" in function_text


def test_group_rotation_end_section_uses_single_pagebreak_helper() -> None:
    text = (ROOT / "scripts" / "generate_chatgpt_side_daily_reports.py").read_text(
        encoding="utf-8",
        errors="replace",
    )
    start = text.index("def append_group_rotation_end_section(")
    end = text.index("\ndef operation_overview_rows(", start)
    function_text = text[start:end]

    assert "append_page_break_once(story)" in function_text
    assert "story.append(PageBreak())" not in function_text
