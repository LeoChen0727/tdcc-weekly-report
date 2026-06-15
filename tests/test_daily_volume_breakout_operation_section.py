from __future__ import annotations

import sys
from pathlib import Path

import pandas as pd


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import build_daily_volume_breakout_operation_section as builder  # noqa: E402


def approval_stub() -> dict[str, str]:
    return {
        "approval_source": "approved_operation_patterns_latest.csv",
        "approved_for_daily": "True",
        "approval_status": "approved_for_daily_v1",
        "operation_module_id": "volume_breakout_confirmed_operation_v1",
        "approval_version": "volume_breakout_operation_v1_20260615",
        "operation_directive_level": "approved_daily_operation_guidance",
        "buy_filter_id": "positive_evidence_oos_rank_v1",
        "approval_note_zh": "approved for test",
    }


def test_daily_volume_breakout_operation_section_adds_active_empty_rows() -> None:
    source = pd.DataFrame(
        [
            {
                "model_id": "volume_range_breakout",
                "pdf_view": "highlight",
                "pdf_section": "confirmed_operation",
                "display_order": "1",
                "stock_id": "1234",
                "stock_name": "TEST",
                "stock_display": "1234 TEST",
                "operation_status_zh": "已確認操作",
                "trigger_zh": "隔日續強確認",
                "entry_basis_zh": "確認後下一交易日開盤",
                "stop_basis_zh": "跌破 6/12 最低價 10.00",
                "exit_rule_zh": "先跌破停損基準出場，否則進場後第 10 個交易日收盤出場",
                "sample_size": "20",
                "win_rate_zh": "55.00%",
                "median_return_zh": "+2.00%",
            }
        ]
    )

    out = builder.normalize_source_rows(
        source,
        "ready",
        "20260612",
        3,
        approval_stub(),
        "2026-06-15 12:00:00 Asia/Taipei",
    )

    assert set(out["model_id"]) == {"volume_range_breakout"}
    assert set(out["pdf_view"]) == {"highlight", "full"}
    assert set(out["pdf_section"]) == {"confirmed_operation", "pending_confirmation", "active_operation"}
    assert set(out["approved_for_daily"]) == {"True"}
    assert set(out["approval_status"]) == {"approved_for_daily_v1"}
    assert set(out["operation_directive_level"]) == {"approved_daily_operation_guidance"}
    active = out[out["pdf_section"].eq("active_operation")]
    assert len(active) == 2
    assert set(active["row_type"]) == {"empty_state"}
    assert active["stock_display"].eq("目前無資料").all()


def test_daily_volume_breakout_operation_section_ignores_other_models() -> None:
    source = pd.DataFrame(
        [
            {
                "model_id": "price_pullback_23ema",
                "pdf_view": "highlight",
                "pdf_section": "confirmed_operation",
                "display_order": "1",
                "stock_id": "9999",
            }
        ]
    )

    out = builder.normalize_source_rows(
        source,
        "ready",
        "20260612",
        0,
        approval_stub(),
        "2026-06-15 12:00:00 Asia/Taipei",
    )

    assert set(out["model_id"]) == {"volume_range_breakout"}
    assert set(out["row_type"]) == {"empty_state"}
    assert len(out) == 6


def test_confirmed_operation_keeps_positive_evidence_only() -> None:
    source = pd.DataFrame(
        [
            {
                "model_id": "volume_range_breakout",
                "pdf_view": "full",
                "pdf_section": "confirmed_operation",
                "display_order": "1",
                "stock_id": "1111",
                "quality_status_zh": "正向證據",
                "sample_size": "12",
                "win_rate_zh": "66.67%",
                "median_return_zh": "+21.09%",
                "research_score": "31.8",
            },
            {
                "model_id": "volume_range_breakout",
                "pdf_view": "full",
                "pdf_section": "confirmed_operation",
                "display_order": "2",
                "stock_id": "2222",
                "quality_status_zh": "證據偏弱",
                "sample_size": "20",
                "win_rate_zh": "55.00%",
                "median_return_zh": "+2.00%",
                "research_score": "9.9",
            },
        ]
    )

    out = builder.normalize_source_rows(
        source,
        "ready",
        "20260612",
        2,
        approval_stub(),
        "2026-06-15 12:00:00 Asia/Taipei",
    )

    confirmed = out[
        out["pdf_section"].eq("confirmed_operation") & out["row_type"].eq("data")
    ].copy()
    assert confirmed["stock_id"].tolist() == ["1111"]
    assert confirmed["quality_status_zh"].tolist() == ["正向證據"]


def test_daily_pipeline_runs_volume_breakout_operation_adapter() -> None:
    workflow = (ROOT / ".github" / "workflows" / "daily_full_pipeline.yml").read_text(encoding="utf-8")

    assert "python scripts/build_daily_volume_breakout_operation_section.py" in workflow
    assert "python scripts/validate_daily_volume_breakout_operation_section.py" in workflow


def test_daily_pdf_generator_does_not_read_research_operation_artifacts_directly() -> None:
    generator = ROOT / "scripts" / "generate_chatgpt_side_daily_reports.py"
    if not generator.exists():
        return
    source = generator.read_text(encoding="utf-8", errors="replace")

    assert "volume_breakout_operation_pdf_preview_latest.csv" not in source
    assert "volume_breakout_confirmed_operation_rank_latest.csv" not in source
    assert "volume_breakout_pending_operation_queue_latest.csv" not in source
    assert "approved_operation_patterns_latest.csv" not in source
