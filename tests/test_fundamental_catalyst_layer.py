from __future__ import annotations

import sys
from pathlib import Path

import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import apply_fundamental_catalyst_layer as layer  # noqa: E402


def test_degraded_calendar_context_has_no_model_effect() -> None:
    calendar = pd.Series(
        {
            "event_type": "ex_dividend",
            "event_name": "ex dividend",
            "event_date": "20260622",
            "days_to_event": "3",
            "proximity_bucket": "within_3d",
            "event_status": "source_stale_cached",
            "catalyst_tags": "dividend_calendar;calendar_source_stale;calendar_source_degraded",
            "source": "TWSE ex-right/ex-dividend calendar",
            "expected_impact": "calendar_event_stale_reminder_only",
            "notes": "source_status=stale_ok; model_effect_allowed=False; pdf_effect_allowed=False",
        }
    )

    info = layer.calendar_flags(calendar)

    assert info["event_calendar_tags"] == "calendar_source_degraded"
    assert info["event_proximity_score"] == "0"
    assert info["calendar_effect_allowed"] == "False"
    assert "model_effect_allowed=False" in info["summary"]
    assert "pdf_effect_allowed=False" in info["summary"]


def test_degraded_calendar_tag_is_not_promoted_to_catalyst_tags() -> None:
    row = pd.Series(
        {
            "stock_id": "2330",
            "category": "",
            "tdcc_accumulation_signal": "",
            "already_priced_in": "False",
        }
    )
    calendar = pd.Series(
        {
            "event_type": "ex_dividend",
            "event_name": "ex dividend",
            "event_date": "20260622",
            "days_to_event": "3",
            "proximity_bucket": "within_3d",
            "event_status": "source_degraded_blocked",
            "catalyst_tags": "dividend_calendar;calendar_source_degraded",
            "source": "TWSE ex-right/ex-dividend calendar",
            "expected_impact": "calendar_event_degraded_blocked_no_effect",
            "notes": "source_status=degraded_blocked_effect; model_effect_allowed=False; pdf_effect_allowed=False",
        }
    )

    result = layer.derive_row(row, fin=None, event=None, theme=None, calendar=calendar)

    assert result["event_calendar_tags"] == "calendar_source_degraded"
    assert result["event_proximity_score"] == "0"
    assert result["catalyst_tags"] == ""
