from __future__ import annotations

from pathlib import Path

from pypdf import PdfReader

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


def test_highlight_specs_keep_program_side_layout_order() -> None:
    specs = [
        generator.pd.Series({"model_id": generator.VOLUME_BREAKOUT_MODEL_ID}),
        generator.pd.Series({"model_id": "price_pullback_23ema"}),
        generator.pd.Series({"model_id": "tdcc_short_term_continuation_d5_d10"}),
    ]

    ordered = generator.highlight_specs_in_layout_order(specs)

    assert [row["model_id"] for row in ordered] == [
        generator.VOLUME_BREAKOUT_MODEL_ID,
        "price_pullback_23ema",
        "tdcc_short_term_continuation_d5_d10",
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

    assert 'DAILY_HIGHLIGHT_LAYOUT_CONTRACT = "legacy_volume_first"' in text
    assert 'DAILY_HIGHLIGHT_MODEL_ORDER_POLICY = "program_side_order"' in text
    assert "curated_specs_with_volume_last" not in text
    assert "append_page_break_once(story)\n        append_stock_model_title(story, model_name, level=1)" in mainstream_text
    assert "highlight_specs_in_layout_order(mainstream_curated_core_model_specs(inputs))" in mainstream_text
    assert "should_render_highlight_model_description(model_id)" in mainstream_text
    assert "build_mainstream_curated_operation_page(row, all_map, two_map, story, vol_map)" in mainstream_text
    assert "append_stock_model_description_lines(story, desc)" in mainstream_text
    assert "story.append(para(desc, BODY_SMALL))" not in mainstream_text
    assert "append_page_break_once(story)\n        append_stock_model_title(story, model_name, level=1)" in non_mainstream_text
    assert "highlight_specs_in_layout_order(non_mainstream_curated_core_model_specs(inputs))" in non_mainstream_text
    assert "should_render_highlight_model_description(model_id)" in non_mainstream_text
    assert "build_non_mainstream_curated_operation_page(row, all_map, two_map, story, vol_map)" in non_mainstream_text
    assert "append_stock_model_description_lines(story, desc)" in non_mainstream_text
    assert "story.append(para(desc, BODY_SMALL))" not in non_mainstream_text


def test_daily_stock_model_titles_use_dedicated_blue_style_helper() -> None:
    text = (ROOT / "scripts" / "generate_chatgpt_side_daily_reports.py").read_text(
        encoding="utf-8",
        errors="replace",
    )

    assert "PDF_MODEL_TITLE_BLUE" in text
    assert "MODEL_H1 = ParagraphStyle(" in text
    assert "MODEL_H2 = ParagraphStyle(" in text
    assert "append_stock_model_title(story, model_name, level=1)" in text
    assert "append_stock_model_title(story, model_name, level=2)" in text
    assert "story.append(Paragraph(model_name, H1))" not in text
    assert "story.append(Paragraph(model_name, H2))" not in text


def test_operation_section_labels_use_keep_with_table_helper() -> None:
    text = (ROOT / "scripts" / "generate_chatgpt_side_daily_reports.py").read_text(
        encoding="utf-8",
        errors="replace",
    )
    cases = [
        ("render_w_bottom_operation_section", "render_price_pullback_operation_section"),
        ("render_price_pullback_operation_section", "render_volume_range_breakout_operation_section"),
        ("render_volume_range_breakout_operation_section", "render_model_operation_section_if_applicable"),
    ]

    assert "def append_section_label_with_table(" in text
    assert "keepWithNext = 1" in text
    for name, next_name in cases:
        function_text = _function_text(text, name, next_name)

        assert "append_section_label_with_table(" in function_text
        assert "story.append(Paragraph(OPERATION_CONFIRMED_BUY_TABLE_TITLE, H2))" not in function_text
        assert "story.append(Paragraph(OPERATION_ACTIVE_TABLE_TITLE, H2))" not in function_text
        assert 'story.append(Paragraph("已確認但未通過買入排名門檻", H2))' not in function_text
        assert 'story.append(Paragraph("待確認", H2))' not in function_text


def test_append_section_label_with_table_marks_label_and_preface_keep_with_next() -> None:
    story: list[object] = []
    table = generator.build_table([["TABLE_HEADER"], ["FIRST_ROW"]], [40 * generator.mm], 12.0)
    preface = generator.para("PREFACE", generator.BODY_SMALL)

    generator.append_section_label_with_table(story, "ACTIVE_SECTION", table, preface)

    assert len(story) == 3
    assert story[0].getPlainText() == "ACTIVE_SECTION"
    assert getattr(story[0], "keepWithNext") == 1
    assert story[1].getPlainText() == "PREFACE"
    assert getattr(story[1], "keepWithNext") == 1
    assert story[2] is table


def test_section_label_moves_with_table_when_page_tail_is_too_short(tmp_path: Path) -> None:
    pdf_path = tmp_path / "section_label_keep_with_table.pdf"
    story: list[object] = [generator.Spacer(1, 42 * generator.mm)]
    table = generator.build_table([["TABLE_HEADER"], ["FIRST_ROW"]], [45 * generator.mm], 12.0)
    generator.append_section_label_with_table(story, "ACTIVE_SECTION", table)
    doc = generator.SimpleDocTemplate(
        str(pdf_path),
        pagesize=(70 * generator.mm, 70 * generator.mm),
        leftMargin=6 * generator.mm,
        rightMargin=6 * generator.mm,
        topMargin=6 * generator.mm,
        bottomMargin=6 * generator.mm,
    )

    doc.build(story)

    page_texts = [page.extract_text() or "" for page in PdfReader(str(pdf_path)).pages]
    assert len(page_texts) >= 2
    assert "ACTIVE_SECTION" not in page_texts[0]
    assert "ACTIVE_SECTION" in page_texts[1]
    assert "TABLE_HEADER" in page_texts[1]
    assert "FIRST_ROW" in page_texts[1]


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
