from __future__ import annotations

import sys
from pathlib import Path

import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import generate_daily_market_pdf as pdf  # noqa: E402
import validate_daily_market_report as market_validator  # noqa: E402


def test_mainstream_highlight_summary_splits_multi_stock_cell_into_rows() -> None:
    summary = pd.DataFrame(
        [
            {
                "report_line": "mainstream",
                "model_name_zh": "嚴格突破",
                "new_signal_stock_display": "8021 尖點\n突破成立\n觀察\n3022 威強電\n突破成立\n觀察\n2478 大毅\n突破成立\n觀察",
                "new_signal_model_score": "84",
                "new_signal_rank_label_zh": "新進榜 #1",
                "repeated_signal_stock_display": "今日無候選",
                "operation_reminder_zh": "觀察",
            }
        ]
    )

    rows = pdf.mainstream_highlight_summary_rows(summary)
    stock_cells = [row[3] for row in rows[1:]]

    assert stock_cells == ["8021 尖點", "3022 威強電", "2478 大毅"]
    assert all(str(cell).count(" ") <= 1 for cell in stock_cells)


def test_make_table_uses_full_grid_and_zebra_rows() -> None:
    table = pdf.make_table([["H1", "H2"], ["A", "B"], ["C", "D"]], pdf.styles(), [100, 100])

    assert any(cmd[:5] == ("GRID", (0, 0), (-1, -1), 0.35, pdf.colors.HexColor("#bfbfbf")) for cmd in table._linecmds)
    assert ("BACKGROUND", (0, 0), (-1, 0), pdf.colors.HexColor("#1D3557")) in table._bkgrndcmds
    assert ("ROWBACKGROUNDS", (0, 1), (-1, -1), [pdf.colors.white, pdf.colors.HexColor("#f4f7fa")]) in table._bkgrndcmds


def test_formal_pdf_text_sanitizes_report_line_raw_tokens() -> None:
    text = pdf.pdf_text("mainstream / non_mainstream / mainstream_overheated / non_mainstream_theme")

    assert "mainstream" not in text
    assert "non_mainstream" not in text
    assert "\u4e3b\u6d41" in text
    assert "\u975e\u4e3b\u6d41" in text


def test_model_summary_empty_line_fallback_does_not_emit_raw_report_line() -> None:
    summary = pd.DataFrame(
        [
            {
                "report_line": "non_mainstream",
                "model_name_zh": "\u653e\u91cf\u653b\u64ca\u6a21\u578b",
                "operation_reminder_zh": "\u4f9d\u6a21\u578b\u689d\u4ef6\u8207\u98a8\u96aa\u6b04\u4f4d\u89c0\u5bdf\u3002",
            }
        ]
    )

    mainstream_rows = pdf.mainstream_full_summary_rows(summary)

    assert "mainstream" not in mainstream_rows[1][5]
    assert "\u4e3b\u6d41" in mainstream_rows[1][5]


def test_raw_slug_validator_does_not_match_mainstream_inside_hyphenated_english() -> None:
    errors: list[str] = []

    market_validator.check_raw_slug_terms("full_table", "plain English non-mainstream phrase", errors)

    assert errors == []


def test_raw_slug_validator_still_catches_report_line_and_theme_raw_ids() -> None:
    errors: list[str] = []

    market_validator.check_raw_slug_terms("full_table", "mainstream \u7121\u6a21\u578b\u6458\u8981\u8cc7\u6599", errors)
    market_validator.check_raw_slug_terms("full_table", "theme value non_mainstream_theme leaked", errors)

    assert any("raw slug appears in formal PDF text: mainstream;" in error for error in errors)
    assert any("raw slug appears in formal PDF text: non_mainstream_theme;" in error for error in errors)
