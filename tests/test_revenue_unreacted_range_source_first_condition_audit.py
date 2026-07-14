from __future__ import annotations

import sys
from pathlib import Path

import pandas as pd


ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))

from revenue_unreacted_range_source_first_condition_audit import (  # noqa: E402
    BASELINE_VARIANT_ID,
    DETAIL_CSV,
    LATEST_CSV,
    PRIMARY_VARIANT_ID,
)
from validate_revenue_unreacted_range_source_first_condition_audit import validate  # noqa: E402


def test_source_first_condition_audit_passes() -> None:
    assert validate() == []


def test_selected_condition_covers_both_known_successes_without_counting_overlap() -> None:
    detail = pd.read_csv(
        DETAIL_CSV,
        dtype={"stock_id": str, "launch_date": str},
        keep_default_na=False,
        low_memory=False,
    )
    selected = detail.loc[
        detail["condition_variant_id"].eq(PRIMARY_VARIANT_ID)
        & detail["episode_status"].eq("launch_within_active_horizon")
        & detail["stock_id"].isin(["4916", "1303"])
    ]
    assert set(selected["stock_id"]) == {"4916", "1303"}
    assert selected.loc[selected["stock_id"].eq("4916"), "launch_date"].tolist() == ["20260518"]
    assert selected.loc[selected["stock_id"].eq("1303"), "launch_date"].tolist() == ["20260527"]
    for stock_id, rows in detail.loc[
        detail["condition_variant_id"].eq(PRIMARY_VARIANT_ID)
    ].groupby("stock_id", sort=False):
        ordered = rows.sort_values("episode_start_sequence_index", kind="mergesort")
        starts = pd.to_numeric(ordered["episode_start_sequence_index"], errors="coerce")
        prior_ends = pd.to_numeric(ordered["episode_end_sequence_index"], errors="coerce").shift(1)
        assert not starts.le(prior_ends).fillna(False).any(), stock_id


def test_retrospective_launch_rate_is_not_misreported_as_first_breakout_win_rate() -> None:
    summary = pd.read_csv(LATEST_CSV, keep_default_na=False, low_memory=False)
    selected = summary.loc[summary["condition_variant_id"].eq(PRIMARY_VARIANT_ID)].iloc[0]
    baseline = summary.loc[summary["condition_variant_id"].eq(BASELINE_VARIANT_ID)].iloc[0]
    assert float(selected["retrospective_launch_rate_pct"]) > float(
        baseline["retrospective_launch_rate_pct"]
    )
    assert float(selected["retrospective_launch_rate_excluding_candidates_pct"]) > float(
        baseline["retrospective_launch_rate_excluding_candidates_pct"]
    )
    assert float(selected["first_breakout_strict_success_rate_pct"]) < float(
        selected["retrospective_launch_rate_pct"]
    )


def test_4916_keeps_the_confirmation_gap_visible() -> None:
    detail = pd.read_csv(
        DETAIL_CSV,
        dtype={"stock_id": str},
        keep_default_na=False,
        low_memory=False,
    )
    row = detail.loc[
        detail["condition_variant_id"].eq(PRIMARY_VARIANT_ID)
        & detail["stock_id"].eq("4916")
        & detail["episode_status"].eq("launch_within_active_horizon")
    ].iloc[0]
    assert row["first_breakout_outcome"] == "mature_failure"
    assert row["launch_date"] == "20260518"


def test_source_first_condition_preserves_aligned_qualifying_revenue_lineage() -> None:
    detail = pd.read_csv(
        DETAIL_CSV,
        dtype={"stock_id": str},
        keep_default_na=False,
        low_memory=False,
    )
    for row in detail.itertuples(index=False):
        periods = str(row.qualifying_revenue_periods).split("|")
        source_dates = str(row.qualifying_source_dates).split("|")
        trade_dates = str(row.qualifying_trade_dates).split("|")
        sequence_indices = str(row.qualifying_sequence_indices).split("|")
        assert len(periods) == len(source_dates) == len(trade_dates) == len(sequence_indices)
        assert len(periods) == int(row.qualifying_update_count)
        assert periods[0] == str(row.episode_start_revenue_period)
        assert source_dates[0] == str(row.episode_start_source_date)
        assert trade_dates[0] == str(row.episode_start_trade_date)
        assert periods[-1] == str(row.latest_qualifying_revenue_period)
        assert source_dates[-1] == str(row.latest_qualifying_source_date)
        assert trade_dates[-1] == str(row.latest_qualifying_trade_date)
