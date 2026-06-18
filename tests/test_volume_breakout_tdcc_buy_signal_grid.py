from __future__ import annotations

import sys
from pathlib import Path

import pandas as pd


ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))

from build_volume_breakout_tdcc_buy_signal_grid import (  # noqa: E402
    SIGNAL_UNIVERSE_ID,
    attach_tdcc_asof,
    expand_detail,
    rank_buckets_for_row,
    summarize_grid,
    tdcc_feature_groups,
)


def event_row(**overrides: object) -> dict[str, object]:
    row: dict[str, object] = {
        "model_id": "volume_range_breakout",
        "event_filter_id": "current_model_hit_all",
        "model_hit_status": "current_model_hit",
        "pattern_id": "signal_close_hold_5d",
        "event_date": "20260610",
        "stock_id": "1234",
        "stock_name": "TEST",
        "market": "listed",
        "market_regime": "range_or_mixed",
        "entry_date": "20260611",
        "entry_price": "100",
        "exit_date": "20260618",
        "exit_price": "105",
        "exit_reason": "fixed_5d_close",
        "holding_days": "5",
        "return_pct": "5",
        "mfe_pct": "9",
        "mae_pct": "-2",
        "out_of_sample": "True",
        "volume_ratio": "1.5",
        "signal_return_1d_pct": "9.8",
        "signal_low": "90",
        "signal_high": "100",
        "previous_20d_high": "92",
        "range_width_40_pct": "18",
        "low_position_60_pct": "25",
        "limit_up_like": "True",
        "source_signal_universe_id": SIGNAL_UNIVERSE_ID,
    }
    row.update(overrides)
    return row


def test_rank_bucket_expansion_is_cumulative() -> None:
    assert rank_buckets_for_row({"tdcc_list_type": "no_tdcc"}) == [("all", "全體")]
    assert [key for key, _ in rank_buckets_for_row({"tdcc_list_type": "weekly_increase", "tdcc_rank": "8"})] == [
        "top_10",
        "top_20",
        "top_50",
    ]
    assert [key for key, _ in rank_buckets_for_row({"tdcc_list_type": "weekly_increase", "tdcc_rank": "15"})] == [
        "top_20",
        "top_50",
    ]
    assert [key for key, _ in rank_buckets_for_row({"tdcc_list_type": "weekly_increase", "tdcc_rank": "40"})] == ["top_50"]


def test_attach_tdcc_asof_uses_only_prior_signal_and_keeps_baseline() -> None:
    detail = pd.DataFrame([event_row()])
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

    events = attach_tdcc_asof(detail, tdcc)

    assert set(events["tdcc_list_type"]) == {"no_tdcc", "weekly_increase"}
    matched = events[events["tdcc_list_type"].eq("weekly_increase")].iloc[0]
    assert matched["tdcc_signal_date"] == "20260605"
    assert int(matched["tdcc_signal_age_days"]) == 5
    assert matched["tdcc_rank"] == "8"


def test_tdcc_feature_groups_adds_confluence_dimensions() -> None:
    row = pd.Series(
        event_row(
            tdcc_list_type="weekly_increase",
            tdcc_rank="8",
            tdcc_signal_date="20260605",
            tdcc_signal_age_days="5",
        )
    )

    groups = tdcc_feature_groups(row)
    keys = {(item["rank_bucket"], item["tdcc_feature_scope"]) for item in groups}

    assert ("top_10", "tdcc_only") in keys
    assert ("top_20", "tdcc_price_position") in keys
    assert ("top_50", "tdcc_attack_method") in keys
    assert ("top_10", "tdcc_attack_position") in keys


def test_summarize_grid_keeps_research_only_candidate_status() -> None:
    rows = []
    for idx in range(120):
        rows.append(
            event_row(
                event_date=f"2025{(idx % 12) + 1:02d}{(idx % 20) + 1:02d}",
                stock_id=f"{1000 + idx}",
                return_pct="4" if idx % 3 else "-1",
                out_of_sample="True" if idx >= 80 else "False",
                tdcc_list_type="weekly_increase",
                tdcc_rank="8",
                tdcc_signal_date="20250101",
                tdcc_signal_age_days="5",
                tdcc_ranking_score="20",
            )
        )
    expanded = expand_detail(pd.DataFrame(rows))
    grid = summarize_grid(expanded)

    assert not grid.empty
    row = grid[grid["tdcc_feature_scope"].eq("tdcc_only")].iloc[0]
    assert row["approved_for_daily"] == "False"
    assert row["approved_for_daily_candidate"] == "True"
    assert row["candidate_status"] == "promotion_candidate"
    assert row["tdcc_list_type"] == "weekly_increase"
