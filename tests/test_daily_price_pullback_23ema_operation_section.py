from __future__ import annotations

from pathlib import Path
import sys

import pandas as pd


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import build_daily_price_pullback_23ema_operation_section as builder  # noqa: E402


def approval_frame() -> pd.DataFrame:
    return pd.DataFrame(
        [
            {
                "model_id": builder.MODEL_ID,
                "approved_for_daily": "True",
                "approval_status": "approved_for_daily_v1",
                "operation_module_id": builder.OPERATION_MODULE_ID,
                "approval_version": builder.APPROVAL_VERSION,
                "operation_directive_level": "approved_daily_operation_guidance",
                "buy_filter_id": builder.BUY_FILTER_ID,
                "approval_note_zh": "approved",
            }
        ]
    )


def signal_row(signal_date: str = "20260703") -> dict[str, str]:
    return {
        "model_id": builder.MODEL_ID,
        "model_name_zh": builder.MODEL_NAME_ZH,
        "signal_date": signal_date,
        "stock_id": "1234",
        "stock_name": "TestCo",
        "report_bucket": "mainstream",
        "report_line": "mainstream",
        "report_line_memberships": "mainstream",
        "price_pullback_operation_quality": "technical_strength",
        "price_pullback_reason_tags": "base_v1|technical_strength_rsi60_macd_positive",
        "price_pullback_risk_tags": "",
        "model_score": "70",
    }


def test_current_price_pullback_signal_becomes_confirmed_operation_rows() -> None:
    section, audit = builder.build_section(
        pd.DataFrame([signal_row("20260703")]),
        approval_frame(),
        "20260703",
        "2026-07-03 18:00:00 Asia/Taipei",
    )

    confirmed = section[
        section["row_type"].eq("data") & section["pdf_section"].eq("confirmed_operation")
    ]
    assert set(confirmed["pdf_view"]) == {"highlight", "full"}
    assert set(confirmed["row_action_status"]) == {"confirmed_buy_candidate"}
    assert set(confirmed["buy_rank_eligible"]) == {"True"}
    assert set(confirmed["operation_quality"]) == {"technical_strength"}
    assert set(confirmed["entry_rule_id"]) == {builder.ENTRY_RULE_ID}
    assert set(confirmed["exit_rule_id"]) == {builder.EXIT_RULE_ID}
    assert "active_operation" in set(section["pdf_section"])
    assert not audit.empty


def test_prior_price_pullback_signal_can_become_active_tracking_row(monkeypatch) -> None:
    price = pd.DataFrame(
        [
            {"date": "20260701", "open": 10.0, "high": 12.0, "low": 9.8, "close": 10.0},
            {"date": "20260702", "open": 10.0, "high": 11.8, "low": 9.7, "close": 10.1},
            {"date": "20260703", "open": 10.0, "high": 10.5, "low": 9.9, "close": 10.0},
            {"date": "20260706", "open": 10.1, "high": 10.6, "low": 9.9, "close": 10.2},
            {"date": "20260707", "open": 10.2, "high": 10.7, "low": 10.0, "close": 10.3},
            {"date": "20260708", "open": 10.3, "high": 10.8, "low": 10.1, "close": 10.4},
        ]
    )
    monkeypatch.setattr(builder, "price_for_stock", lambda _stock_id: price)
    monkeypatch.setattr(
        builder,
        "load_signal_history",
        lambda _signals, _report_date: pd.DataFrame([signal_row("20260703")]),
    )

    section, audit = builder.build_section(
        pd.DataFrame(columns=["model_id", "signal_date", "stock_id"]),
        approval_frame(),
        "20260708",
        "2026-07-08 18:00:00 Asia/Taipei",
    )

    active = section[section["row_type"].eq("data") & section["pdf_section"].eq("active_operation")]
    assert set(active["pdf_view"]) == {"highlight", "full"}
    assert set(active["row_action_status"]) == {"active_operation"}
    assert set(active["buy_rank_eligible"]) == {"False"}
    assert set(active["entry_date"]) == {"20260706"}
    assert "active_operation" in set(audit["audit_status"])


def test_daily_full_pipeline_runs_price_pullback_operation_adapter() -> None:
    workflow = (ROOT / ".github" / "workflows" / "daily_full_pipeline.yml").read_text(encoding="utf-8")
    assert "python scripts/build_daily_price_pullback_23ema_operation_section.py" in workflow
    assert "python scripts/validate_daily_price_pullback_23ema_operation_section.py" in workflow
