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
    row = approval.iloc[0]

    assert row["model_id"] == "volume_range_breakout"
    assert row["approved_for_daily"] == "True"
    assert row["operation_directive_level"] == "approved_daily_operation_guidance"
    assert row["entry_rule_id"] == "confirmation_next_open"
    assert row["stop_loss_rule_id"] == "signal_low_stop"
    assert row["exit_rule_id"] == "signal_low_stop_or_fixed_10d_close"
    assert row["evidence_positive_rank_rows"] == 1
