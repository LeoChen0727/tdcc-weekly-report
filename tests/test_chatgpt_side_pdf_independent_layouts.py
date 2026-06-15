from __future__ import annotations

from pathlib import Path

from scripts import validate_chatgpt_side_pdf_layout_independence as validator


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

PRODUCTION_RENDERERS = {
    "build_mainstream_daily_recommendation_highlight_pdf": "mainstream_highlight",
    "build_mainstream_full_candidate_list_pdf": "mainstream_full",
    "build_non_mainstream_daily_recommendation_highlight_pdf": "non_mainstream_highlight",
    "build_non_mainstream_full_candidate_list_pdf": "non_mainstream_full",
}

FORMAL_PDF_PATHS = {
    "output/latest/mainstream_daily_recommendation_highlight_latest.pdf",
    "output/latest/mainstream_full_candidate_list_latest.pdf",
    "output/latest/non_mainstream_daily_recommendation_highlight_latest.pdf",
    "output/latest/non_mainstream_full_candidate_list_latest.pdf",
    "output/latest/warrant_market_report_latest.pdf",
    "output/latest/market_risk_dashboard_latest.pdf",
}

PRODUCTION_DAILY_PDF_ENTRYPOINTS = [
    "build_curated_pdf",
    "build_full_table_pdf",
    *PRODUCTION_RENDERERS.keys(),
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

FORBIDDEN_PRODUCTION_SHARED_RENDERERS = [
    "def _model_names_in_report_order(",
    "def _rows_for_model_section(",
    "def _summary_rows_for_section(",
    "def _fixed_model_summary_rows(",
    "def _detail_table_rows_for_section(",
    "def _model_signal_card_readable(",
    "def _append_theme_event_watch_section_readable(",
    "def _append_group_rotation_section_readable(",
]


def _source() -> str:
    return GENERATOR.read_text(encoding="utf-8", errors="replace")


def _production_source() -> str:
    return PRODUCTION_GENERATOR.read_text(encoding="utf-8", errors="replace")


def _file_source(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace")


def _function_text(text: str, name: str) -> str:
    start = text.index(f"def {name}(")
    next_def = text.find("\ndef ", start + 1)
    end = len(text) if next_def == -1 else next_def
    return text[start:end]


def test_chatgpt_side_pdf_builders_are_explicit_independent_entrypoints() -> None:
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


def test_daily_pdf_template_independence_inventory_covers_template_scope_and_formal_contract_subset() -> None:
    text = INVENTORY.read_text(encoding="utf-8", errors="replace")

    for path in FORMAL_PDF_PATHS:
        assert path in text
    assert "PDF Template Scope" in text
    assert "write_tdcc_weekly_highlight_pdf" in text
    assert "write_tdcc_weekly_full_pdf" in text
    assert "write_weekly_signal_performance_pdf_from_markdown" in text
    assert "write_monthly_signal_performance_pdf_from_markdown" in text
    assert "volume_range_breakout" in text
    assert "Generic stock-PDF dispatchers" in text
    assert "TDCC weekly PDF writers" in text
    assert "Signal performance PDF writers" in text
    assert "New-listed and consecutive/repeated-listed" in text


def test_production_stock_pdf_builders_use_report_specific_namespaces() -> None:
    text = _production_source()

    assert "def build_model_line_pdf(" not in text
    for forbidden in FORBIDDEN_PRODUCTION_SHARED_RENDERERS:
        assert forbidden not in text
    for entrypoint in PRODUCTION_DAILY_PDF_ENTRYPOINTS:
        assert f"def {entrypoint}(" in text

    for name, namespace in PRODUCTION_RENDERERS.items():
        body = _function_text(text, name)
        assert f"{namespace}_" in body
        assert "build_model_line_pdf(" not in body
        assert "for model_name in _model_names_in_report_order(" not in body
        assert "group = _rows_for_model_section(" not in body
        assert "make_table(_detail_table_rows_for_section(" not in body
        assert "story.append(_model_signal_card_readable(" not in body
        assert "_append_theme_event_watch_section_readable(story," not in body
        assert "_append_group_rotation_section_readable(story," not in body


def test_other_pdf_template_entrypoints_are_explicit() -> None:
    for path, entrypoints in OTHER_PDF_TEMPLATE_ENTRYPOINTS.items():
        text = _file_source(path)
        for entrypoint in entrypoints:
            assert f"def {entrypoint}(" in text


def test_tdcc_and_signal_performance_pdfs_do_not_share_generic_template_writers() -> None:
    tdcc_text = _file_source(TDCC_WEEKLY_GENERATOR)
    signal_text = _file_source(SIGNAL_PERFORMANCE_GENERATOR)

    assert "def write_pdf(" not in tdcc_text
    assert "def write_pdf_v2(" not in tdcc_text
    assert "write_pdf_v2(" not in tdcc_text
    assert "def write_pdf_from_markdown(" not in signal_text
    assert "write_pdf_from_markdown(" not in signal_text


def test_chatgpt_side_builders_do_not_call_shared_model_loop_directly() -> None:
    text = _source()

    for name in STOCK_PDF_BUILDERS:
        body = _function_text(text, name)
        assert "for spec in core_model_specs(" not in body
        assert "= model_signal_rows(inputs," not in body


def test_volume_breakout_uses_operation_section_not_general_model_table() -> None:
    text = _source()

    for name in STOCK_PDF_BUILDERS:
        body = _function_text(text, name)
        if "VOLUME_BREAKOUT_MODEL_ID" not in body:
            continue
        volume_branch = body[body.index("if model_id == VOLUME_BREAKOUT_MODEL_ID:") :]
        branch_end = volume_branch.find("story.append(build_")
        checked = volume_branch if branch_end == -1 else volume_branch[:branch_end]
        assert "render_volume_range_breakout_operation_section" in checked
        assert "continue" in checked


def test_standard_model_tables_are_split_into_new_and_repeated_sections() -> None:
    text = _source()

    for name in REPORT_SPECIFIC_TABLE_BUILDERS:
        body = _function_text(text, name)
        signature_block = "\n".join(body.splitlines()[:8])
        assert "-> list" in signature_block
        assert "CondPageBreak(MODEL_SUBSECTION_MIN_ROOM)" in body
        assert "新上榜" in body
        assert "重複上榜" in body
        assert '"#c00000"' in body
        assert '"#1f4e79"' in body
        assert "return build_table(" not in body

    for name in STOCK_PDF_BUILDERS:
        body = _function_text(text, name)
        for table_builder in REPORT_SPECIFIC_TABLE_BUILDERS:
            if f"{table_builder}(" in body:
                assert f"story.extend({table_builder}(" in body


def test_non_mainstream_curated_pdf_matches_mainstream_model_first_layout() -> None:
    text = _source()
    body = _function_text(text, "build_non_mainstream_curated_pdf")

    assert "non_mainstream_curated_recommendation_rows(" not in body
    assert "non_mainstream_curated_front_observation_rows(" not in body
    assert "模型重點" not in body
    assert "觀察清單" not in body
    assert "started_model_sections = False" in body
    assert "if started_model_sections:" in body
    assert "append_page_break_once(story)" in body
    assert "story.append(Paragraph(model_name, H1))" in body


def test_full_candidate_model_headings_have_page_bottom_guard() -> None:
    text = _source()

    for name in ["build_mainstream_full_candidate_pdf", "build_non_mainstream_full_candidate_pdf"]:
        body = _function_text(text, name)
        assert "story.append(CondPageBreak(MODEL_SECTION_MIN_ROOM))\n    story.append(Paragraph(f\"{line_label}完整候選\", H1))" in body
        assert "story.append(CondPageBreak(MODEL_SECTION_MIN_ROOM))\n        story.append(Paragraph(model_name, H2))" in body
        assert "story.append(CondPageBreak(MODEL_SUBSECTION_MIN_ROOM))\n            story.append(Paragraph(zh_line_group(group), H2))" in body
