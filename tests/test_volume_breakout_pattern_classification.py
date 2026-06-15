from __future__ import annotations

import sys
from pathlib import Path

import pandas as pd


ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))

from build_volume_breakout_pattern_classification import (  # noqa: E402
    attack_method_dimension,
    candle_quality_dimension,
    classify_event,
    consolidation_dimension,
    follow_through_dimension,
    price_position_dimension,
    risk_dimension,
    summarize,
)


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
    assert out["attack_method"] == "locked_limit_up"


def test_classify_limit_up_breakout_does_not_require_low_volume_ratio() -> None:
    row = pd.Series(
        {
            "volume_ratio": "3.2",
            "range_width_40_pct": "18",
            "low_position_60_pct": "55",
            "limit_up_like": "True",
        }
    )

    out = classify_event(row)

    assert out["classification_id"] == "locked_limit_up_breakout"
    assert "volume_ratio_ge_3" in out["pattern_tags"]
    assert out["attack_method"] == "locked_limit_up"


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
    assert out["consolidation_type"] == "long_consolidation"
    assert out["price_position_type"] == "low_position"


def test_price_position_dimension_has_low_middle_high_buckets() -> None:
    assert price_position_dimension(pd.Series({"low_position_60_pct": "45"}))[0] == "low_position"
    assert price_position_dimension(pd.Series({"low_position_60_pct": "70"}))[0] == "middle_position"
    assert price_position_dimension(pd.Series({"low_position_60_pct": "85"}))[0] == "high_position"


def test_pattern_dimensions_cover_requested_categories() -> None:
    assert consolidation_dimension(pd.Series({"range_width_40_pct": "20"}))[0] == "long_consolidation"
    assert consolidation_dimension(pd.Series({"range_width_20_pct": "15"}))[0] == "short_consolidation"
    assert consolidation_dimension(pd.Series({"range_width_20_pct": "35"}))[0] == "non_consolidation"

    assert attack_method_dimension(pd.Series({"limit_up_like": "True", "volume_ratio": "0.8"}))[0] == "locked_limit_up"
    assert attack_method_dimension(pd.Series({"limit_up_like": "True", "volume_ratio": "3.2"}))[0] == "locked_limit_up"
    assert attack_method_dimension(pd.Series({"limit_up_like": "False", "volume_ratio": "3.2"}))[0] == "volume_attack"
    assert attack_method_dimension(pd.Series({"limit_up_like": "False", "volume_ratio": "2.2"}))[0] == "general_breakout"


def test_candle_follow_and_risk_dimensions() -> None:
    candle = candle_quality_dimension(
        pd.Series(
            {
                "signal_open": "10",
                "signal_high": "11",
                "signal_low": "9.8",
                "signal_close": "11",
                "signal_return_1d_pct": "8",
                "volume_ratio": "3.5",
                "previous_20d_high": "10.5",
                "next_close": "11.2",
            }
        )
    )
    assert candle[0] == "close_at_high"

    follow = follow_through_dimension(
        pd.Series(
            {
                "signal_close": "11",
                "signal_high": "11",
                "signal_low": "9.8",
                "next_open": "11.2",
                "next_close": "10.8",
                "next_low": "10.6",
                "touch_5ma_10d": False,
                "touch_10ma_10d": False,
                "break_signal_low_5d": False,
            }
        )
    )
    assert follow[0] == "next_day_gap_fade"

    pullback_10ma = follow_through_dimension(
        pd.Series(
            {
                "signal_close": "11",
                "signal_high": "11.5",
                "signal_low": "10",
                "next_open": "10.8",
                "next_close": "10.9",
                "next_low": "10.2",
                "touch_5ma_10d": True,
                "touch_10ma_10d": True,
                "break_signal_low_5d": False,
            }
        )
    )
    assert pullback_10ma[0] == "pullback_10ma"
    assert "pullback_5ma" in pullback_10ma[2]
    assert "pullback_10ma" in pullback_10ma[2]

    risk = risk_dimension(
        pd.Series(
            {
                "low_position_60_pct": "90",
                "signal_return_1d_pct": "6",
                "volume_ratio": "2.5",
                "follow_through_type": "next_day_continuation",
                "signal_close": "11",
                "signal_low": "10",
                "break_signal_low_5d": False,
            }
        )
    )
    assert risk[0] == "high_position_chase"


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
