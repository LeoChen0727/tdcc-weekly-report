from __future__ import annotations

from pathlib import Path
import sys

import pandas as pd


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import build_daily_w_bottom_operation_sections as builder  # noqa: E402
import validate_daily_w_bottom_operation_sections as validator  # noqa: E402


def approval_frame() -> pd.DataFrame:
    return pd.DataFrame(
        [
            {
                "model_id": "w_bottom_right_side",
                "approved_for_daily": "True",
                "approval_status": "approved_for_daily_v2",
                "operation_module_id": "w_bottom_early_entry_operation_v2",
                "approval_version": "w_bottom_early_entry_operation_v2_20260629",
                "operation_directive_level": "approved_daily_operation_guidance",
                "buy_filter_id": "smooth_core_mainstream_right_rebound_5_20_bull",
                "best_evidence_sample_size": "31",
                "best_evidence_win_rate": "58.0645",
                "best_evidence_avg_return": "11.2532",
                "best_evidence_median_return": "6.2374",
                "approval_note_zh": "approved",
            },
            {
                "model_id": "neckline_volume_breakout_confirmation",
                "approved_for_daily": "True",
                "approval_status": "approved_for_daily_v1",
                "operation_module_id": "neckline_strict_45_signal_90_score_v1",
                "approval_version": "neckline_strict_45_signal_90_score_v1_20260629",
                "operation_directive_level": "approved_daily_operation_guidance",
                "buy_filter_id": "broad_45_non_bearish_with_90_warning",
                "best_evidence_sample_size": "51",
                "best_evidence_win_rate": "63.8889",
                "best_evidence_avg_return": "4.3784",
                "best_evidence_median_return": "4.4597",
                "approval_note_zh": "approved",
            },
        ]
    )


def signal_row(model_id: str, signal_date: str = "20260630") -> dict[str, str]:
    return {
        "model_id": model_id,
        "model_name_zh": "W bottom model",
        "signal_date": signal_date,
        "stock_id": "1234",
        "stock_name": "TestCo",
        "report_bucket": "mainstream",
        "report_line": "mainstream",
        "report_line_memberships": "mainstream",
        "display_rank": "1",
        "model_score": "70",
        "next_confirmation_zh": "follow approved rule",
    }


def test_current_signal_becomes_confirmed_buy_rows() -> None:
    section, audit = builder.build_model_section(
        pd.DataFrame([signal_row("w_bottom_right_side")]),
        approval_frame(),
        builder.MODEL_CONFIGS["w_bottom_right_side"],
        "20260630",
        "2026-06-30 12:00:00 Asia/Taipei",
    )

    confirmed = section[
        section["row_type"].eq("data") & section["pdf_section"].eq("confirmed_operation")
    ]
    assert set(confirmed["pdf_view"]) == {"highlight", "full"}
    assert set(confirmed["row_action_status"]) == {"confirmed_buy_candidate"}
    assert set(confirmed["buy_rank_eligible"]) == {"True"}
    assert set(confirmed["row_metric_status"]) == {"unavailable_no_approved_add_score_metric"}
    assert set(confirmed["row_metric_id"]) == {""}
    assert set(confirmed["row_metric_win_rate_zh"]) == {""}
    assert set(confirmed["entry_rule_id"]) == {"right_low_signal_next_open"}
    assert set(confirmed["exit_rule_id"]) == {"d20_gain10_else_d40_close"}
    assert "active_operation" in set(section["pdf_section"])
    assert not audit.empty


def test_prior_signal_can_become_active_tracking_row(monkeypatch) -> None:
    price = pd.DataFrame(
        [
            {"date": "20260624", "open": 10.0, "high": 10.5, "low": 9.8, "close": 10.2},
            {"date": "20260625", "open": 10.3, "high": 10.8, "low": 10.1, "close": 10.5},
            {"date": "20260626", "open": 10.6, "high": 11.0, "low": 10.4, "close": 10.8},
            {"date": "20260629", "open": 10.9, "high": 11.2, "low": 10.7, "close": 11.0},
            {"date": "20260630", "open": 11.1, "high": 11.5, "low": 10.9, "close": 11.2},
        ]
    )
    monkeypatch.setattr(builder, "price_for_stock", lambda _stock_id: price)
    monkeypatch.setattr(
        builder,
        "build_structure_context",
        lambda _row, _price: {
            "left_low_date": "20260624",
            "right_low_date": "20260625",
            "w_structure_low_price": 9.8,
            "neckline_price": 12.0,
            "neckline_distance_pct": -6.67,
        },
    )
    monkeypatch.setattr(
        builder,
        "load_signal_history",
        lambda _signals, _config, _report_date: pd.DataFrame([signal_row("w_bottom_right_side", "20260624")]),
    )

    section, audit = builder.build_model_section(
        pd.DataFrame(columns=["model_id", "signal_date", "stock_id"]),
        approval_frame(),
        builder.MODEL_CONFIGS["w_bottom_right_side"],
        "20260630",
        "2026-06-30 12:00:00 Asia/Taipei",
    )

    active = section[section["row_type"].eq("data") & section["pdf_section"].eq("active_operation")]
    assert set(active["pdf_view"]) == {"highlight", "full"}
    assert set(active["row_action_status"]) == {"active_tracking"}
    assert set(active["buy_rank_eligible"]) == {"False"}
    assert set(active["entry_date"]) == {"20260625"}
    assert all(token in active.iloc[0]["exit_rule_zh"] for token in ("D+20", "+10%", "D+40"))
    assert "candidate_evaluated" in set(audit["audit_status"])


def test_validator_rejects_active_w_bottom_rows_without_exit_rule_tokens() -> None:
    active = pd.DataFrame(
        [
            {
                "pdf_view": "highlight",
                "report_line": "mainstream",
                "stock_id": "1234",
                "exit_rule_zh": "若 D+20 收盤報酬達 +10% 則 D+20 收盤出場。",
            }
        ]
    )

    errors = validator.validate_active_exit_rule_tokens(
        active,
        "daily_w_bottom_right_side_operation_section_latest.csv",
        "w_bottom_right_side",
    )

    assert any("missing tokens ['D+40']" in error for error in errors)

    active.loc[0, "exit_rule_zh"] = "若 D+20 收盤報酬達 +10% 則 D+20 收盤出場；否則持有到 D+40 收盤。"

    assert (
        validator.validate_active_exit_rule_tokens(
            active,
            "daily_w_bottom_right_side_operation_section_latest.csv",
            "w_bottom_right_side",
        )
        == []
    )


def test_current_w_bottom_signal_is_suppressed_when_same_stock_is_already_active(monkeypatch) -> None:
    price = pd.DataFrame(
        [
            {"date": "20260624", "open": 10.0, "high": 10.5, "low": 9.8, "close": 10.2},
            {"date": "20260625", "open": 10.3, "high": 10.8, "low": 10.1, "close": 10.5},
            {"date": "20260626", "open": 10.6, "high": 11.0, "low": 10.4, "close": 10.8},
            {"date": "20260629", "open": 10.9, "high": 11.2, "low": 10.7, "close": 11.0},
            {"date": "20260630", "open": 11.1, "high": 11.5, "low": 10.9, "close": 11.2},
        ]
    )
    monkeypatch.setattr(builder, "price_for_stock", lambda _stock_id: price)
    monkeypatch.setattr(
        builder,
        "build_structure_context",
        lambda _row, _price: {
            "left_low_date": "20260624",
            "right_low_date": "20260625",
            "w_structure_low_price": 9.8,
            "neckline_price": 12.0,
            "neckline_distance_pct": -6.67,
        },
    )
    monkeypatch.setattr(
        builder,
        "load_signal_history",
        lambda _signals, _config, _report_date: pd.DataFrame([signal_row("w_bottom_right_side", "20260624")]),
    )

    section, audit = builder.build_model_section(
        pd.DataFrame([signal_row("w_bottom_right_side", "20260630")]),
        approval_frame(),
        builder.MODEL_CONFIGS["w_bottom_right_side"],
        "20260630",
        "2026-06-30 12:00:00 Asia/Taipei",
    )

    confirmed = section[section["row_type"].eq("data") & section["pdf_section"].eq("confirmed_operation")]
    active = section[section["row_type"].eq("data") & section["pdf_section"].eq("active_operation")]
    assert confirmed.empty
    assert set(active["signal_date"]) == {"20260624"}
    assert set(active["stock_id"]) == {"1234"}
    suppressed = audit[audit["audit_status"].eq("lifecycle_suppressed")]
    assert suppressed[["stock_id", "signal_date", "reason"]].to_dict("records") == [
        {
            "stock_id": "1234",
            "signal_date": "20260630",
            "reason": "same_stock_already_active_operation",
        }
    ]
    assert set(suppressed["included_in_daily_adapter"]) == {"False"}


def test_daily_full_pipeline_runs_w_bottom_operation_adapter() -> None:
    workflow = (ROOT / ".github" / "workflows" / "daily_full_pipeline.yml").read_text(encoding="utf-8")
    assert "python scripts/build_daily_w_bottom_operation_sections.py" in workflow
    assert "python scripts/validate_daily_w_bottom_operation_sections.py" in workflow
    assert "git add docs/latest/daily_w_bottom_right_side_operation_*_latest.*" in workflow
    assert "git add docs/latest/daily_neckline_volume_breakout_confirmation_operation_*_latest.*" in workflow
