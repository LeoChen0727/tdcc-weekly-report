from __future__ import annotations

import sys
from pathlib import Path

import pandas as pd


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from build_approved_operation_patterns import build_approval  # noqa: E402


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

    approval = build_approval(generated_at="2026-06-15 00:00:00 Asia/Taipei")
    assert approval[approval["model_id"].eq("volume_range_breakout")].empty

    low = approval[approval["model_id"].eq("volume_range_breakout_v2_low_position_volume_attack")].iloc[0]
    assert low["operation_module_id"] == "volume_range_breakout_v2_low_position_operation_v1"
    assert low["approved_for_daily"] == "True"
    assert low["operation_directive_level"] == "approved_daily_operation_guidance"
    assert low["entry_rule_id"] == "confirmation_next_open"
    assert low["stop_loss_rule_id"] == "sustained_close_below_lower_ma20_ema23_4pct_4d"
    assert low["exit_rule_id"] == "ema23_close_stop_or_fixed_15d_close"
    assert low["best_evidence_sample_size"] == "26"
    assert low["best_evidence_win_rate"] == "80.7692"
    assert low["volume_v2_loss_rate_pct"] == "19.2308"

    mid = approval[approval["model_id"].eq("volume_range_breakout_v2_mid_position_momentum_attack")].iloc[0]
    assert mid["operation_module_id"] == "volume_range_breakout_v2_mid_position_operation_v1"
    assert mid["approved_for_daily"] == "True"
    assert mid["entry_rule_id"] == "confirmation_next_open"
    assert mid["stop_loss_rule_id"] == "sustained_close_below_lower_ma20_ema23_4pct_4d"
    assert mid["exit_rule_id"] == "ema23_close_stop_or_fixed_15d_close"
    assert mid["best_evidence_sample_size"] == "25"
    assert mid["best_evidence_win_rate"] == "80.0000"
    assert mid["volume_v2_loss_rate_pct"] == "20.0000"

    high = approval[approval["model_id"].eq("volume_range_breakout_v2_high_position_volume_attack")].iloc[0]
    assert high["operation_module_id"] == "volume_range_breakout_v2_high_position_operation_v1"
    assert high["approval_version"] == "volume_range_breakout_v2_high_position_operation_20260710"
    assert high["approved_for_daily"] == "True"
    assert high["entry_rule_id"] == "confirmation_next_open"
    assert high["stop_loss_rule_id"] == "sustained_close_below_lower_ma20_ema23_4pct_4d"
    assert high["exit_rule_id"] == "ema23_close_stop_or_fixed_15d_close"
    assert high["buy_filter_id"] == "pos120_high_nonconsolidation_or_wide_ma60_gt_ma120_next_day_continuation_d15_stop"
    assert high["source_research_id"] == "volume_range_breakout_v2_high_position_improvement_audit"
    assert high["evidence_source_kind"] == "volume_range_breakout_v2_high_position_improvement_audit"
    assert high["best_evidence_sample_size"] == "231"
    assert high["best_evidence_win_rate"] == "62.3377"
    assert high["volume_v2_loss_rate_pct"] == "37.6623"

    w_bottom = approval[approval["model_id"].eq("w_bottom_right_side")].iloc[0]
    assert w_bottom["operation_module_id"] == "w_bottom_early_entry_operation_v2"
    assert w_bottom["approval_version"] == "w_bottom_early_entry_operation_v2_20260629"
    assert w_bottom["approved_for_daily"] == "True"
    assert w_bottom["operation_directive_level"] == "approved_daily_operation_guidance"
    assert w_bottom["entry_rule_id"] == "right_low_signal_next_open"
    assert w_bottom["stop_loss_rule_id"] == "w_structure_low_close_stop"
    assert w_bottom["exit_rule_id"] == "d20_gain10_else_d40_close"
    assert w_bottom["buy_filter_id"] == "smooth_core_mainstream_right_rebound_5_20_bull"
    assert w_bottom["best_evidence_sample_size"] == "31"
    assert w_bottom["best_evidence_win_rate"] == "58.0645"
    assert w_bottom["w_bottom_positive_return_rate_pct"] == "58.0645"
    assert w_bottom["w_bottom_avg_return_pct"] == "11.2532"
    assert w_bottom["w_bottom_min_return_pct"] == "-12.7202"

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

    revenue = approval[approval["model_id"].eq("revenue_unreacted_range")].iloc[0]
    assert revenue["operation_module_id"] == (
        "revenue_unreacted_range_source_mid_falling_v2_operation_v2"
    )
    assert revenue["approval_status"] == (
        "provisional_backtest_supported_oos_unconfirmed"
    )
    assert revenue["approved_for_daily"] == "True"
    assert revenue["entry_rule_id"] == "d2_analysis_open"
    assert revenue["stop_loss_rule_id"] == "none_no_stop_reference"
    assert revenue["exit_rule_id"] == "d30_analysis_close_offset29"
    assert revenue["min_sample_size"] == "0"
    assert revenue["min_win_rate"] == "0.0"
    assert revenue["require_out_of_sample_pass"] == "False"
    assert revenue["best_evidence_sample_size"] == "53"
    assert revenue["best_evidence_win_rate"] == "77.3585"
    assert revenue["best_evidence_median_return"] == "9.4077"
    assert revenue["best_evidence_out_of_sample_pass"] == "unconfirmed"
    assert revenue["revenue_forward_holdout_status"] == (
        "post_launch_monitoring_non_hard_no_tuning"
    )
