from __future__ import annotations

import sys
from pathlib import Path

import pandas as pd


ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))

from build_volume_breakout_tdcc_confluence_backtest import (  # noqa: E402
    attach_tdcc_asof,
    normalize_inputs,
    scope_summary,
)


def test_attach_tdcc_asof_uses_only_prior_weekly_signal() -> None:
    ops = pd.DataFrame(
        [
            {
                "model_id": "volume_range_breakout",
                "overlay_model_id": "",
                "research_id": "",
                "event_date": "20260610",
                "stock_id": "1234",
                "stock_name": "TEST",
                "market": "listed",
                "market_regime": "mild_bull",
                "event_filter_id": "current_model_hit_all",
                "model_hit_status": "current_model_hit",
                "pattern_id": "pullback_10ma_hold_10d",
                "entry_date": "20260611",
                "entry_price": "100",
                "exit_date": "20260624",
                "exit_price": "110",
                "exit_reason": "fixed_10d_close",
                "holding_days": "10",
                "return_pct": "10",
                "mfe_pct": "12",
                "mae_pct": "-2",
                "out_of_sample": "True",
            }
        ]
    )
    tdcc = pd.DataFrame(
        [
            {
                "model_id": "tdcc_weekly_ranking_formula",
                "signal_date": "20260605",
                "stock_id": "1234",
                "tdcc_list_type": "weekly_increase",
                "tdcc_rank": "8",
                "tdcc_ranking_score": "20",
            },
            {
                "model_id": "tdcc_weekly_ranking_formula",
                "signal_date": "20260612",
                "stock_id": "1234",
                "tdcc_list_type": "weekly_increase",
                "tdcc_rank": "1",
                "tdcc_ranking_score": "99",
            },
        ]
    )

    events = attach_tdcc_asof(ops, tdcc)

    assert len(events) == 1
    assert events.iloc[0]["tdcc_signal_date"] == "20260605"
    assert int(events.iloc[0]["tdcc_signal_age_days"]) == 5
    assert events.iloc[0]["tdcc_rank"] == "8"


def test_attach_tdcc_asof_rejects_stale_signal() -> None:
    ops = pd.DataFrame(
        [
            {
                "model_id": "volume_range_breakout",
                "event_date": "20260620",
                "stock_id": "1234",
                "event_filter_id": "current_model_hit_all",
                "model_hit_status": "current_model_hit",
                "pattern_id": "signal_close_hold_5d",
                "return_pct": "3",
            }
        ]
    )
    tdcc = pd.DataFrame(
        [
            {
                "model_id": "tdcc_weekly_ranking_formula",
                "signal_date": "20260605",
                "stock_id": "1234",
                "tdcc_list_type": "weekly_increase",
                "tdcc_rank": "8",
            }
        ]
    )

    events = attach_tdcc_asof(ops, tdcc)

    assert events.empty


def test_normalize_inputs_keeps_only_current_volume_breakout_hits() -> None:
    ops = pd.DataFrame(
        [
            {
                "model_id": "volume_range_breakout",
                "event_date": "20260610",
                "stock_id": "1234",
                "event_filter_id": "current_model_hit_all",
                "model_hit_status": "current_model_hit",
            },
            {
                "model_id": "volume_range_breakout",
                "event_date": "20260610",
                "stock_id": "5678",
                "event_filter_id": "non_current_research_control",
                "model_hit_status": "research_relaxed_not_current_model",
            },
        ]
    )
    classification = pd.DataFrame([{"event_date": "20260610", "stock_id": "1234"}])
    tdcc = pd.DataFrame(
        [
            {
                "model_id": "tdcc_weekly_ranking_formula",
                "signal_date": "20260605",
                "stock_id": "1234",
            }
        ]
    )

    norm_ops, _, _ = normalize_inputs(ops, classification, tdcc)

    assert list(norm_ops["stock_id"]) == ["1234"]
    assert set(norm_ops["model_hit_status"]) == {"current_model_hit"}


def test_scope_summary_keeps_research_not_daily_approval() -> None:
    events = pd.DataFrame(
        [
            {
                "model_id": "volume_range_breakout",
                "overlay_model_id": "tdcc_weekly_ranking_formula",
                "research_id": "volume_breakout_tdcc_confluence",
                "event_date": "20260610",
                "tdcc_signal_date": "20260605",
                "tdcc_signal_age_days": "5",
                "stock_id": "1234",
                "pattern_id": "signal_close_hold_5d",
                "return_pct": "5",
                "mfe_pct": "8",
                "mae_pct": "-1",
                "holding_days": "5",
                "out_of_sample": "True",
                "classification_id": "locked_limit_up_breakout",
                "classification_name_zh": "locked",
                "attack_method": "locked_limit_up",
                "attack_method_name_zh": "locked",
                "price_position_type": "high_position",
                "price_position_name_zh": "high",
                "follow_through_type": "next_day_continuation",
                "follow_through_name_zh": "strong",
                "risk_type": "high_position_chase",
                "risk_name_zh": "risk",
                "candle_quality": "close_at_high",
                "candle_quality_name_zh": "close high",
                "consolidation_type": "non_consolidation",
                "consolidation_name_zh": "non",
                "tdcc_list_type": "weekly_increase",
                "tdcc_rank": "8",
                "tdcc_ranking_score": "20",
            }
        ]
    )

    summary = scope_summary(events, "now", "20260610", "20260610")

    assert not summary.empty
    assert set(summary["approved_for_daily"].astype(str).str.lower()) == {"false"}
    assert "tdcc_rank_only" in set(summary["confluence_scope"])
    assert "tdcc_attack_follow" in set(summary["confluence_scope"])
