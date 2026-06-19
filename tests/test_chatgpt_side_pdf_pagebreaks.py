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


def test_curated_specs_with_volume_last_keeps_daily_highlights_first() -> None:
    specs = [
        generator.pd.Series({"model_id": generator.VOLUME_BREAKOUT_MODEL_ID}),
        generator.pd.Series({"model_id": "price_pullback_23ema"}),
        generator.pd.Series({"model_id": "tdcc_short_term_continuation_d5_d10"}),
    ]

    ordered = generator.curated_specs_with_volume_last(specs)

    assert [row["model_id"] for row in ordered] == [
        "price_pullback_23ema",
        "tdcc_short_term_continuation_d5_d10",
        generator.VOLUME_BREAKOUT_MODEL_ID,
    ]


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
    assert "story.append(para(desc, BODY_SMALL))" not in mainstream_text
    assert "append_page_break_once(story)\n        story.append(Paragraph(model_name, H1))" in non_mainstream_text
    assert "build_non_mainstream_curated_operation_page(row, all_map, two_map, story, vol_map)" in non_mainstream_text
    assert "story.append(para(desc, BODY_SMALL))" not in non_mainstream_text


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


def test_curated_operation_pages_keep_stock_table_and_chart_together() -> None:
    text = (ROOT / "scripts" / "generate_chatgpt_side_daily_reports.py").read_text(
        encoding="utf-8",
        errors="replace",
    )
    cases = [
        ("build_mainstream_curated_operation_page", "build_non_mainstream_curated_operation_page"),
        ("build_non_mainstream_curated_operation_page", "build_mainstream_curated_pdf"),
    ]

    for name, next_name in cases:
        function_text = _function_text(text, name, next_name)

        assert "story.append(\n        KeepTogether(" in function_text
        assert 'Paragraph(f"{sid} {name}｜{model_display(row)}", H2)' in function_text
        assert "op_table," in function_text
        assert "Spacer(1, 4)," in function_text
        assert "chart_table," in function_text
        assert "story.append(op_table)" not in function_text
        assert "story.append(chart_table)" not in function_text
