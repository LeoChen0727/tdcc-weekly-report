from __future__ import annotations

import sys
from pathlib import Path

import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import generate_daily_market_pdf as pdf  # noqa: E402


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
