from __future__ import annotations

import sys
from pathlib import Path

import pandas as pd
from pypdf import PdfReader


ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))

from build_volume_breakout_operation_pdf_preview import (  # noqa: E402
    build_preview,
    positive_evidence,
    stop_basis,
)
import build_volume_breakout_operation_pdf_preview_pdf as pdf_builder  # noqa: E402


def test_stop_basis_uses_date_low_wording() -> None:
    assert stop_basis("20260613", "49") == "跌破 6/13 最低價 49.00"


def test_positive_evidence_requires_positive_median() -> None:
    good = pd.Series(
        {
            "evidence_sample_size": "12",
            "evidence_win_rate": "66.67",
            "evidence_median_return": "21.09",
            "ranking_research_score": "31.8",
        }
    )
    bad = good.copy()
    bad["evidence_median_return"] = "-1.0"

    assert positive_evidence(good)
    assert not positive_evidence(bad)


def test_preview_dedupes_pending_and_uses_chinese_labels() -> None:
    rank = pd.DataFrame(
        [
            {
                "operation_rank": "1",
                "stock_id": "2243",
                "stock_name": "TEST",
                "signal_date": "20260611",
                "confirmation_date": "20260612",
                "trigger_id": "next_day_continuation_confirmed",
                "stop_loss_level": "30.3",
                "tdcc_list_type": "weekly_increase",
                "tdcc_rank": "6",
                "classification_id": "limit_up_like_breakout",
                "attack_method": "general_breakout",
                "price_position_type": "high_position",
                "evidence_sample_size": "12",
                "evidence_win_rate": "66.67",
                "evidence_avg_return": "21.67",
                "evidence_median_return": "21.09",
                "evidence_confidence_status": "low",
                "ranking_research_score": "31.8",
            },
            {
                "operation_rank": "2",
                "stock_id": "2547",
                "stock_name": "WEAK",
                "signal_date": "20260611",
                "confirmation_date": "20260612",
                "trigger_id": "next_day_continuation_confirmed",
                "stop_loss_level": "10.85",
                "tdcc_list_type": "no_tdcc",
                "classification_id": "standard_breakout",
                "attack_method": "general_breakout",
                "price_position_type": "middle_position",
                "evidence_sample_size": "555",
                "evidence_win_rate": "43.6",
                "evidence_avg_return": "2.65",
                "evidence_median_return": "-1.88",
                "evidence_confidence_status": "medium",
                "ranking_research_score": "-1.3",
            },
        ]
    )
    pending = pd.DataFrame(
        [
            {
                "signal_date": "20260610",
                "signal_age_trading_days": "2",
                "stock_id": "1409",
                "stock_name": "AAA",
                "stop_loss_level": "18.2",
                "classification_id": "high_position_breakout",
                "attack_method": "volume_attack",
                "price_position_type": "high_position",
            },
            {
                "signal_date": "20260611",
                "signal_age_trading_days": "1",
                "stock_id": "1409",
                "stock_name": "AAA",
                "stop_loss_level": "19.2",
                "classification_id": "limit_up_like_breakout",
                "attack_method": "volume_attack",
                "price_position_type": "high_position",
            },
        ]
    )

    preview = build_preview(rank, pending)
    highlight_confirmed = preview[
        preview["pdf_view"].eq("highlight") & preview["pdf_section"].eq("confirmed_operation")
    ]
    full_pending = preview[
        preview["pdf_view"].eq("full") & preview["pdf_section"].eq("pending_confirmation")
    ]

    assert len(highlight_confirmed) == 1
    assert highlight_confirmed.iloc[0]["median_return_zh"] == "+21.09%"
    assert "最低價" in highlight_confirmed.iloc[0]["stop_basis_zh"]
    assert len(full_pending) == 1
    assert full_pending.iloc[0]["same_stock_pending_count"] == 2
    assert full_pending.iloc[0]["pending_age_zh"].startswith("D+1")


def test_pdf_preview_builder_writes_readable_pdf(tmp_path, monkeypatch) -> None:
    preview = pd.DataFrame(
        [
            {
                "pdf_view": "highlight",
                "pdf_section": "confirmed_operation",
                "display_order": "1",
                "stock_id": "2243",
                "stock_name": "宏旭-KY",
                "stock_display": "2243 宏旭-KY",
                "operation_status_zh": "已確認",
                "quality_status_zh": "正向證據",
                "trigger_zh": "隔日續強確認",
                "entry_basis_zh": "確認後下一交易日開盤",
                "stop_basis_zh": "跌破 6/11 最低價 30.30",
                "sample_size": "12",
                "win_rate_zh": "66.67%",
                "avg_return_zh": "+21.67%",
                "median_return_zh": "+21.09%",
                "confidence_zh": "低",
                "pdf_note_zh": "類漲停突破",
            },
            {
                "pdf_view": "highlight",
                "pdf_section": "pending_confirmation",
                "display_order": "1",
                "stock_id": "1409",
                "stock_name": "AAA",
                "stock_display": "1409 AAA",
                "operation_status_zh": "待確認",
                "pending_age_zh": "D+1，剩 9 個交易日",
                "pending_group_zh": "D+0-D+1 等隔日續強",
                "stop_basis_zh": "跌破 6/11 最低價 19.20",
                "same_stock_pending_count": "1",
                "pdf_note_zh": "高位階突破",
            },
        ]
    )
    # Include the full rows so each PDF section is exercised.
    full = preview.copy()
    full["pdf_view"] = "full"
    preview = pd.concat([preview, full], ignore_index=True)
    out_pdf = tmp_path / "preview.pdf"
    monkeypatch.setattr(pdf_builder, "PREVIEW_PDF", out_pdf)

    pdf_builder.build_pdf(preview)

    reader = PdfReader(str(out_pdf))
    text = "\n".join(page.extract_text() or "" for page in reader.pages)
    assert len(reader.pages) >= 1
    assert "放量攻擊" in text
    assert "中位數報酬" in text
    assert "最低價" in text
