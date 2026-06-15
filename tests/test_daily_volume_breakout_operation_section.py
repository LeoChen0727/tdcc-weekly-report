from __future__ import annotations

import sys
from pathlib import Path

import pandas as pd


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import build_daily_volume_breakout_operation_section as builder  # noqa: E402
import generate_chatgpt_side_daily_reports as pdf_generator  # noqa: E402


def approval_stub() -> dict[str, str]:
    return {
        "approval_source": "approved_operation_patterns_latest.csv",
        "approved_for_daily": "True",
        "operation_module_approved_for_daily": "True",
        "approval_status": "approved_for_daily_v1",
        "operation_module_id": "volume_breakout_confirmed_operation_v1",
        "approval_version": "volume_breakout_operation_v1_20260615",
        "operation_directive_level": "approved_daily_operation_guidance",
        "row_action_status": "",
        "buy_rank_eligible": "False",
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
                "operation_asof_date": "20260612",
                "display_order": "1",
                "stock_id": "1234",
                "stock_name": "TEST",
                "stock_display": "1234 TEST",
                "operation_status_zh": "已確認操作",
                "quality_status_zh": "正向證據",
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
    assert set(out["operation_module_approved_for_daily"]) == {"True"}
    assert set(out["approval_status"]) == {"approved_for_daily_v1"}
    assert set(out["operation_directive_level"]) == {"approved_daily_operation_guidance"}
    confirmed = out[out["pdf_section"].eq("confirmed_operation") & out["row_type"].eq("data")]
    assert confirmed["row_action_status"].tolist() == ["confirmed_buy_candidate"]
    assert confirmed["buy_rank_eligible"].tolist() == ["True"]
    active = out[out["pdf_section"].eq("active_operation")]
    assert len(active) == 2
    assert set(active["row_type"]) == {"empty_state"}
    assert active["stock_display"].eq("目前無資料").all()
    assert active["buy_rank_eligible"].eq("False").all()
    assert active["row_action_status"].eq("empty_state").all()


def test_pending_confirmation_rows_are_not_buy_rank_eligible() -> None:
    source = pd.DataFrame(
        [
            {
                "model_id": "volume_range_breakout",
                "pdf_view": "highlight",
                "pdf_section": "pending_confirmation",
                "operation_asof_date": "20260612",
                "display_order": "1",
                "stock_id": "1234",
                "stock_name": "TEST",
                "stock_display": "1234 TEST",
                "operation_status_zh": "待確認",
                "entry_basis_zh": "尚未確認，不列進場價",
                "stop_basis_zh": "跌破 6/12 最低價 10.00",
                "exit_rule_zh": "尚未成立；確認後才啟動進場與出場規則",
            }
        ]
    )

    out = builder.normalize_source_rows(
        source,
        "ready",
        "20260612",
        1,
        approval_stub(),
        "2026-06-15 12:00:00 Asia/Taipei",
    )

    pending = out[out["pdf_section"].eq("pending_confirmation") & out["row_type"].eq("data")]
    assert len(pending) == 1
    row = pending.iloc[0]
    assert row["approved_for_daily"] == "True"
    assert row["operation_module_approved_for_daily"] == "True"
    assert row["row_action_status"] == "pending_confirmation"
    assert row["buy_rank_eligible"] == "False"


def test_daily_signal_context_uses_report_date_as_authority() -> None:
    signals = pd.DataFrame(
        [
            {"model_id": "volume_range_breakout", "signal_date": "20260612", "stock_id": "1111"},
            {"model_id": "volume_range_breakout", "signal_date": "20260615", "stock_id": "2222"},
            {"model_id": "volume_range_breakout", "signal_date": "20260615", "stock_id": "3333"},
        ]
    )

    signal_date, count = builder.daily_signal_context(signals, "20260615")

    assert signal_date == "20260615"
    assert count == 2


def test_daily_signal_context_does_not_promote_stale_model_signal_date() -> None:
    signals = pd.DataFrame(
        [
            {"model_id": "volume_range_breakout", "signal_date": "20260612", "stock_id": "1111"},
        ]
    )

    signal_date, count = builder.daily_signal_context(signals, "20260615")

    assert signal_date == "20260615"
    assert count == 0


def test_daily_volume_breakout_operation_section_ignores_other_models() -> None:
    source = pd.DataFrame(
        [
            {
                "model_id": "price_pullback_23ema",
                "pdf_view": "highlight",
                "pdf_section": "confirmed_operation",
                "operation_asof_date": "20260612",
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
                "operation_asof_date": "20260612",
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
                "operation_asof_date": "20260612",
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
    assert confirmed["row_action_status"].tolist() == ["confirmed_buy_candidate"]
    assert confirmed["buy_rank_eligible"].tolist() == ["True"]


def test_stale_operation_source_renders_empty_rows_only() -> None:
    source = pd.DataFrame(
        [
            {
                "model_id": "volume_range_breakout",
                "pdf_view": "highlight",
                "pdf_section": "pending_confirmation",
                "operation_asof_date": "20260612",
                "display_order": "1",
                "stock_id": "1438",
                "stock_name": "三地開發",
                "stock_display": "1438 三地開發",
                "operation_status_zh": "待確認",
                "entry_basis_zh": "尚未確認，不列進場價",
                "stop_basis_zh": "跌破 6/11 最低價 22.90",
                "exit_rule_zh": "尚未成立；確認後才啟動進場與出場規則",
            }
        ]
    )

    out = builder.normalize_source_rows(
        source,
        "ready",
        "20260615",
        19,
        approval_stub(),
        "2026-06-16 12:00:00 Asia/Taipei",
    )

    assert set(out["row_type"]) == {"empty_state"}
    assert set(out["adapter_source_status"]) == {"stale_research_source"}
    assert set(out["operation_source_date_status"]) == {"stale_research_source"}
    assert out["stock_id"].eq("").all()
    assert out["adapter_note_zh"].str.contains("20260612").all()
    assert out["adapter_note_zh"].str.contains("20260615").all()


def test_pdf_volume_operation_uses_taxonomy_for_report_line_fallback() -> None:
    rows = pd.DataFrame(
        [
            {
                "model_id": "volume_range_breakout",
                "pdf_view": "highlight",
                "pdf_section": "pending_confirmation",
                "row_type": "data",
                "display_order": "1",
                "stock_id": "1438",
                "stock_display": "1438 三地開發",
                "row_action_status": "pending_confirmation",
                "buy_rank_eligible": "False",
            },
            {
                "model_id": "volume_range_breakout",
                "pdf_view": "highlight",
                "pdf_section": "active_operation",
                "row_type": "empty_state",
                "display_order": "0",
                "stock_id": "",
                "stock_display": "目前無資料",
                "row_action_status": "empty_state",
                "buy_rank_eligible": "False",
            },
        ]
    )
    inputs = {
        "stock_theme_taxonomy": pd.DataFrame(
            [
                {
                    "stock_id": "1438",
                    "stock_name": "三地開發",
                    "industry": "建材營造",
                    "report_line_memberships": "non_mainstream",
                    "mainstream_report_eligible": "False",
                    "non_mainstream_report_eligible": "True",
                }
            ]
        )
    }

    mainstream = pdf_generator.filter_volume_operation_rows_for_line(rows, inputs, "mainstream")
    non_mainstream = pdf_generator.filter_volume_operation_rows_for_line(rows, inputs, "non_mainstream")

    assert "1438" not in set(mainstream["stock_id"].astype(str))
    assert "1438" in set(non_mainstream["stock_id"].astype(str))
    assert mainstream[mainstream["row_type"].eq("empty_state")]["stock_display"].tolist() == ["目前無資料"]


def test_pdf_volume_operation_does_not_guess_missing_taxonomy() -> None:
    rows = pd.DataFrame(
        [
            {
                "model_id": "volume_range_breakout",
                "pdf_view": "highlight",
                "pdf_section": "pending_confirmation",
                "row_type": "data",
                "display_order": "1",
                "stock_id": "9999",
                "stock_display": "9999 未分類",
                "row_action_status": "pending_confirmation",
                "buy_rank_eligible": "False",
            }
        ]
    )

    mainstream = pdf_generator.filter_volume_operation_rows_for_line(rows, {}, "mainstream")
    non_mainstream = pdf_generator.filter_volume_operation_rows_for_line(rows, {}, "non_mainstream")

    assert mainstream.empty
    assert non_mainstream.empty


def test_daily_pipeline_runs_volume_breakout_operation_adapter() -> None:
    workflow = (ROOT / ".github" / "workflows" / "daily_full_pipeline.yml").read_text(encoding="utf-8")

    assert "python scripts/build_daily_volume_breakout_operation_section.py" in workflow
    assert "python scripts/validate_daily_volume_breakout_operation_section.py" in workflow


def test_daily_pdf_generator_does_not_read_research_operation_artifacts_directly() -> None:
    generator = ROOT / "scripts" / "generate_chatgpt_side_daily_reports.py"
    if not generator.exists():
        return
    source = generator.read_text(encoding="utf-8", errors="replace")

    assert "daily_volume_breakout_operation_section_latest.csv" in source
    assert "render_volume_range_breakout_operation_section" in source
    assert "volume_breakout_operation_pdf_preview_latest.csv" not in source
    assert "volume_breakout_confirmed_operation_rank_latest.csv" not in source
    assert "volume_breakout_pending_operation_queue_latest.csv" not in source
    assert "approved_operation_patterns_latest.csv" not in source


def test_daily_packet_builder_uses_daily_adapter_not_research_operation_artifacts() -> None:
    packet_builder = ROOT / "build_chatgpt_daily_report_packet.py"
    source = packet_builder.read_text(encoding="utf-8", errors="replace")

    assert "daily_volume_breakout_operation_section_latest.csv" in source
    assert "build_volume_operation_packet_lines" in source
    assert "volume_breakout_operation_pdf_preview_latest.csv" not in source
    assert "volume_breakout_confirmed_operation_rank_latest.csv" not in source
    assert "volume_breakout_pending_operation_queue_latest.csv" not in source
    assert "historical_pattern_operation_registry_latest.csv" not in source
    assert "approved_operation_patterns_latest.csv" not in source


def test_pdf_operation_renderer_uses_row_level_buy_eligibility(monkeypatch) -> None:
    captured_tables: list[list[list[str]]] = []

    def capture_table(rows, widths, font_size=7.2, header_bg=None):
        captured_tables.append(rows)
        return rows

    monkeypatch.setattr(pdf_generator, "build_table", capture_table)
    rows = pd.DataFrame(
        [
            {
                "model_id": "volume_range_breakout",
                "pdf_view": "highlight",
                "pdf_section": "confirmed_operation",
                "operation_asof_date": "20260612",
                "row_type": "data",
                "display_order": "1",
                "stock_id": "1111",
                "stock_display": "1111 測試A",
                "trigger_zh": "隔日續強確認",
                "entry_basis_zh": "確認後下一交易日開盤",
                "entry_price_status_zh": "進場價待下一交易日開盤",
                "stop_basis_zh": "跌破 6/11 最低價 10.00",
                "exit_rule_zh": "第 10 個交易日收盤出場",
                "sample_size": "12",
                "win_rate_zh": "66.67%",
                "avg_return_zh": "+21.67%",
                "median_return_zh": "+21.09%",
                "confidence_zh": "低",
                "operation_status_zh": "已確認",
                "row_action_status": "confirmed_buy_candidate",
                "buy_rank_eligible": "True",
            },
            {
                "model_id": "volume_range_breakout",
                "pdf_view": "highlight",
                "pdf_section": "pending_confirmation",
                "operation_asof_date": "20260612",
                "row_type": "data",
                "display_order": "1",
                "stock_id": "2222",
                "stock_display": "2222 測試B",
                "pending_age_zh": "D+1，剩 9 個交易日",
                "pending_group_zh": "D+0-D+1 等隔日續強",
                "pending_confirmation_zh": "等待隔日續強 / 回測 5MA / 回測 10MA",
                "entry_basis_zh": "尚未確認，不列進場價",
                "stop_basis_zh": "跌破 6/11 最低價 20.00",
                "operation_status_zh": "待確認",
                "row_action_status": "pending_confirmation",
                "buy_rank_eligible": "False",
            },
            {
                "model_id": "volume_range_breakout",
                "pdf_view": "highlight",
                "pdf_section": "active_operation",
                "operation_asof_date": "20260612",
                "row_type": "empty_state",
                "display_order": "0",
                "stock_id": "",
                "stock_display": "目前無資料",
                "operation_status_zh": "操作中",
                "adapter_note_zh": "目前無操作中追蹤列。",
                "row_action_status": "empty_state",
                "buy_rank_eligible": "False",
            },
        ]
    )

    story: list = []
    pdf_generator.render_volume_range_breakout_operation_section(
        story,
        {"volume_operation": rows},
        "highlight",
    )

    assert len(captured_tables) == 3
    confirmed, pending, active = captured_tables
    assert confirmed[0] == [
        "排名",
        "股票",
        "確認方式",
        "買入方式",
        "進場價狀態",
        "停損價",
        "出場規則",
        "樣本數",
        "勝率",
        "平均報酬",
        "中位數報酬",
        "信心",
    ]
    assert confirmed[1][1] == "1111 測試A"
    assert "2222 測試B" not in " ".join(str(cell) for row in confirmed for cell in row)
    assert pending[0] == ["股票", "等待天數", "等待分組", "待確認條件", "進場價狀態", "停損基準", "狀態"]
    assert pending[1][0] == "2222 測試B"
    assert pending[1][4] == "尚未確認，不列進場價"
    assert active[0] == ["狀態", "股票 / 說明", "備註"]
    assert active[1][0] == "操作中"

    visible = "\n".join(str(cell) for table in captured_tables for row in table for cell in row)
    assert "buy_rank_eligible" not in visible
    assert "row_action_status" not in visible
    assert "confirmed_buy_candidate" not in visible
