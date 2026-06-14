from __future__ import annotations

import sys
from pathlib import Path

import pandas as pd


ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))

from build_volume_breakout_pattern_classification import classify_event, summarize  # noqa: E402


def test_classify_locked_limit_up_breakout() -> None:
    row = pd.Series(
        {
            "volume_ratio": "0.504",
            "range_width_40_pct": "18",
            "low_position_60_pct": "55",
            "limit_up_like": "True",
        }
    )

    out = classify_event(row)

    assert out["classification_id"] == "locked_limit_up_breakout"
    assert "volume_ratio_lt_2" in out["pattern_tags"]


def test_classify_long_base_low_position_before_generic_low_position() -> None:
    row = pd.Series(
        {
            "volume_ratio": "2.5",
            "range_width_40_pct": "20",
            "low_position_60_pct": "45",
            "limit_up_like": "False",
        }
    )

    out = classify_event(row)

    assert out["classification_id"] == "long_base_low_position"


def test_classification_summary_never_approves_daily() -> None:
    detail = pd.DataFrame(
        [
            {
                "model_id": "volume_range_breakout",
                "event_filter_id": "current_model_hit_all",
                "model_hit_status": "current_model_hit",
                "pattern_id": "pullback_10ma_hold_10d",
                "event_date": "20260101",
                "stock_id": "1234",
                "stock_name": "TEST",
                "market": "TWSE",
                "market_regime": "mild_bull",
                "return_pct": "3",
                "mfe_pct": "5",
                "mae_pct": "-1",
                "holding_days": "10",
                "out_of_sample": "False",
            }
        ]
    )
    events = pd.DataFrame(
        [
            {
                "model_id": "volume_range_breakout",
                "event_date": "20260101",
                "stock_id": "1234",
                "classification_id": "long_base_low_position",
                "classification_name_zh": "長盤整低位階突破",
            }
        ]
    )

    out = summarize(detail, events)

    assert not bool(out.iloc[0]["approved_for_daily"])
    assert out.iloc[0]["classification_id"] == "long_base_low_position"
