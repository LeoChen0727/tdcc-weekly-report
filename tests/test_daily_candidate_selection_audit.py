from __future__ import annotations

import sys
from pathlib import Path

import pandas as pd


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import audit_daily_candidate_model_selection_correctness as audit  # noqa: E402


def v2_signal_row(model_id: str) -> pd.Series:
    return pd.Series(
        {
            "stock_id": "1234",
            "model_id": model_id,
            "main_condition_met": "True",
            "signal_date": "20260709",
        }
    )


def v2_watch_row() -> pd.Series:
    return pd.Series(
        {
            "stock_id": "1234",
            "signal_date": "20260709",
            "volume_breakout_type": "bottom_volume_attack",
            "selection_status": "selected",
        }
    )


def test_volume_v2_audit_accepts_matching_membership(monkeypatch) -> None:
    monkeypatch.setattr(
        audit,
        "volume_v2_model_memberships",
        lambda row, stock_id, signal_date: ([audit.VOLUME_BREAKOUT_V2_LOW_MODEL_ID], {}),
    )

    errors, warnings = audit.audit_selected_row(
        v2_signal_row(audit.VOLUME_BREAKOUT_V2_LOW_MODEL_ID),
        None,
        {"1234": v2_watch_row()},
        set(),
        volume_watch_fresh=True,
        tdcc_edge_fresh=True,
    )

    assert errors == []
    assert warnings == []


def test_volume_v2_audit_rejects_mismatched_membership(monkeypatch) -> None:
    monkeypatch.setattr(
        audit,
        "volume_v2_model_memberships",
        lambda row, stock_id, signal_date: ([audit.VOLUME_BREAKOUT_V2_LOW_MODEL_ID], {}),
    )

    errors, _warnings = audit.audit_selected_row(
        v2_signal_row(audit.VOLUME_BREAKOUT_V2_MID_MODEL_ID),
        None,
        {"1234": v2_watch_row()},
        set(),
        volume_watch_fresh=True,
        tdcc_edge_fresh=True,
    )

    assert any("source row v2 membership" in error for error in errors)
