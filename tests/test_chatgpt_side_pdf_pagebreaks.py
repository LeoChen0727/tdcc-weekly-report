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


def _function_text(text: str, name: str, next_name: str) -> str:
    start = text.index(f"def {name}(")
    end = text.index(f"\ndef {next_name}(", start)
    return text[start:end]


def test_curated_pdfs_use_single_pagebreak_helper_before_model_sections() -> None:
    text = (ROOT / "scripts" / "generate_chatgpt_side_daily_reports.py").read_text(
        encoding="utf-8",
        errors="replace",
    )

    mainstream_text = _function_text(text, "build_mainstream_curated_pdf", "build_non_mainstream_curated_pdf")
    non_mainstream_text = _function_text(text, "build_non_mainstream_curated_pdf", "build_mainstream_full_candidate_pdf")

    assert "append_page_break_once(story)\n        story.append(Paragraph(model_name, H1))" in mainstream_text
    assert "build_mainstream_curated_operation_page(row, all_map, two_map, story, vol_map)" in mainstream_text
    assert "append_page_break_once(story)\n        story.append(Paragraph(model_name, H1))" in non_mainstream_text
    assert "build_non_mainstream_curated_operation_page(row, all_map, two_map, story, vol_map)" in non_mainstream_text


def test_group_rotation_end_sections_use_single_pagebreak_helper() -> None:
    text = (ROOT / "scripts" / "generate_chatgpt_side_daily_reports.py").read_text(
        encoding="utf-8",
        errors="replace",
    )
    names = [
        "append_mainstream_curated_group_rotation_end_section",
        "append_mainstream_full_group_rotation_end_section",
        "append_non_mainstream_curated_group_rotation_end_section",
        "append_non_mainstream_full_group_rotation_end_section",
    ]
    for index, name in enumerate(names):
        next_name = names[index + 1] if index + 1 < len(names) else "matches_line"
        function_text = _function_text(text, name, next_name)

        assert "append_page_break_once(story)" in function_text
        assert "story.append(PageBreak())" not in function_text
