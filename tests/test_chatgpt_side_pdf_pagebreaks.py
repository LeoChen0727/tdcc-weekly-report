from __future__ import annotations

from pathlib import Path

import pandas as pd

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
    end = text.index("\ndef matches_line(", start)
    function_text = text[start:end]

    assert "append_page_break_once(story)" in function_text
    assert "story.append(PageBreak())" not in function_text


def test_volume_breakout_operation_rows_include_research_statistics_and_empty_active_section() -> None:
    operation = pd.DataFrame(
        [
            {
                "model_id": "volume_range_breakout",
                "pdf_view": "highlight",
                "pdf_section": "confirmed_operation",
                "display_order": "1",
                "stock_id": "2243",
                "stock_display": "2243 宏旭-KY",
                "operation_status_zh": "已確認",
                "trigger_zh": "隔日續強確認",
                "entry_basis_zh": "確認後下一交易日開盤",
                "entry_price_status_zh": "進場價待下一交易日開盤",
                "stop_basis_zh": "跌破 6/11 最低價 30.30",
                "exit_rule_zh": "先跌破停損基準出場，否則進場後第 10 個交易日收盤出場",
                "signal_date": "20260611",
                "confirmation_date": "20260612",
                "sample_size": "12",
                "win_rate_zh": "66.67%",
                "avg_return_zh": "+21.67%",
                "median_return_zh": "+21.09%",
                "confidence_zh": "低",
            }
        ]
    )

    confirmed = generator.volume_operation_section_rows(
        operation,
        "highlight",
        "confirmed_operation",
        {"2243"},
    )
    active = generator.volume_operation_section_rows(
        operation,
        "highlight",
        "active_operation",
        {"2243"},
    )

    assert confirmed[0] == ["狀態", "標的", "觸發 / 日期", "買進 / 停損 / 賣出", "歷史統計"]
    assert confirmed[1][1] == "2243 宏旭-KY"
    assert "中位數報酬 +21.09%" in confirmed[1][4]
    assert "勝率 66.67%" in confirmed[1][4]
    assert active[1][0] == "操作中"
    assert active[1][3] == "目前無操作中。"


def test_volume_breakout_operation_section_is_model_scoped() -> None:
    story: list[object] = []

    generator.append_volume_breakout_operation_research(
        story,
        {"volume_operation": pd.DataFrame()},
        "price_pullback_23ema",
        [pd.Series({"stock_id": "2243"})],
        full=False,
    )

    assert story == []
