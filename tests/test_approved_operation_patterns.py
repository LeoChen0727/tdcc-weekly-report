from __future__ import annotations

import sys
from pathlib import Path

import pandas as pd


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from build_approved_operation_patterns import build_approval, positive_rank_rows  # noqa: E402


def test_positive_rank_rows_use_strict_evidence_gate() -> None:
    rank = pd.DataFrame(
        [
            {
                "evidence_sample_size": "10",
                "evidence_win_rate": "50",
                "evidence_median_return": "0.1",
                "evidence_out_of_sample_pass": "True",
                "ranking_research_score": "0.1",
            },
            {
                "evidence_sample_size": "9",
                "evidence_win_rate": "80",
                "evidence_median_return": "10",
                "evidence_out_of_sample_pass": "True",
                "ranking_research_score": "10",
            },
            {
                "evidence_sample_size": "50",
                "evidence_win_rate": "70",
                "evidence_median_return": "-1",
                "evidence_out_of_sample_pass": "True",
                "ranking_research_score": "10",
            },
        ]
    )

    out = positive_rank_rows(rank)

    assert len(out) == 1


def test_build_approval_creates_versioned_daily_guidance() -> None:
    summary = pd.DataFrame(
        [
            {
                "confluence_scope": "operation_trigger",
                "confluence_id": "all_confirmed_volume_breakout",
                "sample_size": "50",
                "win_rate": "62",
                "median_return": "4.8",
                "ranking_research_score": "20.7",
                "confidence_status": "medium",
                "out_of_sample_pass": "True",
                "data_start_date": "20250507",
                "data_end_date": "20260602",
                "out_of_sample_start_date": "20260130",
            }
        ]
    )
    rank = pd.DataFrame(
        [
            {
                "evidence_sample_size": "44",
                "evidence_win_rate": "63.64",
                "evidence_median_return": "5.62",
                "evidence_out_of_sample_pass": "True",
                "ranking_research_score": "22.8",
                "approved_for_daily": "False",
            }
        ]
    )

    approval = build_approval(summary, rank, generated_at="2026-06-15 00:00:00 Asia/Taipei")
    row = approval[approval["model_id"].eq("volume_range_breakout")].iloc[0]

    assert row["model_id"] == "volume_range_breakout"
    assert row["approved_for_daily"] == "True"
    assert row["operation_directive_level"] == "approved_daily_operation_guidance"
    assert row["entry_rule_id"] == "confirmation_next_open"
    assert row["stop_loss_rule_id"] == "signal_low_stop"
    assert row["exit_rule_id"] == "signal_low_stop_or_fixed_10d_close"
    assert row["evidence_positive_rank_rows"] == 1

    w_bottom = approval[approval["model_id"].eq("w_bottom_right_side")].iloc[0]
    assert w_bottom["operation_module_id"] == "w_bottom_early_entry_operation_v1"
    assert w_bottom["approval_version"] == "w_bottom_early_entry_operation_v1_20260629"
    assert w_bottom["approved_for_daily"] == "True"
    assert w_bottom["operation_directive_level"] == "approved_daily_operation_guidance"
    assert w_bottom["entry_rule_id"] == "right_low_signal_next_open"
    assert w_bottom["stop_loss_rule_id"] == "no_fixed_stop_loss_d40_evaluation"
    assert w_bottom["exit_rule_id"] == "take_profit_10pct_or_neutral_5pct_d40_close"
    assert w_bottom["buy_filter_id"] == "smooth_core_mainstream_right_rebound_5_20_bull"
    assert w_bottom["best_evidence_sample_size"] == "20"
    assert w_bottom["best_evidence_win_rate"] == "65.0000"
    assert w_bottom["w_bottom_neutral_inclusive_success_rate_pct"] == "77.4194"

    neckline = approval[approval["model_id"].eq("neckline_volume_breakout_confirmation")].iloc[0]
    assert neckline["operation_module_id"] == "neckline_strict_45_signal_90_score_v1"
    assert neckline["approval_version"] == "neckline_strict_45_signal_90_score_v1_20260629"
    assert neckline["approved_for_daily"] == "True"
    assert neckline["operation_directive_level"] == "approved_daily_operation_guidance"
    assert neckline["entry_rule_id"] == "close_ge_1pct_within_3_sessions_next_open"
    assert neckline["stop_loss_rule_id"] == "no_fixed_stop_loss_20d_operation_rule"
    assert neckline["exit_rule_id"] == "tp10_close_win_5pct_pullback_neutral_else_20d_close_loss"
    assert neckline["buy_filter_id"] == "broad_45_non_bearish_with_90_warning"
    assert neckline["best_evidence_sample_size"] == "51"
    assert neckline["best_evidence_win_rate"] == "63.8889"
    assert neckline["neckline_neutral_inclusive_success_rate_pct"] == "74.5098"
    assert neckline["neckline_filter90_auto_bearish_confirmed_count"] == "19"
