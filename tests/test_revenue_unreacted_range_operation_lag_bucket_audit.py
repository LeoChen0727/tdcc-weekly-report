from __future__ import annotations

import sys
from pathlib import Path

import pandas as pd


ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))

from revenue_unreacted_range_operation_lag_bucket_audit import (  # noqa: E402
    ADOPTED_GRID_ID,
    DETAIL_CSV,
    LATEST_CSV,
    PRIMARY_ANALYSIS_BASIS,
    SENSITIVITY_ANALYSIS_BASIS,
    SOURCE_OPERATION_DETAIL_CSV,
)
from validate_revenue_unreacted_range_operation_lag_bucket_audit import (  # noqa: E402
    validate,
)


def test_operation_lag_bucket_audit_passes() -> None:
    assert validate() == []


def test_operation_lag_bucket_uses_asof_latest_revenue_without_future_backfill() -> None:
    detail = pd.read_csv(
        DETAIL_CSV,
        dtype={
            "stock_id": str,
            "trigger_date": str,
            "asof_latest_qualifying_trade_date": str,
            "final_episode_latest_qualifying_trade_date": str,
        },
        keep_default_na=False,
        low_memory=False,
    )
    assert detail["final_episode_latest_after_trigger_flag"].astype(str).eq("True").any()
    assert detail["asof_latest_qualifying_trade_date"].le(detail["trigger_date"]).all()
    future = detail.loc[
        pd.to_numeric(detail["future_qualifying_update_ignored_count"], errors="coerce").gt(0)
    ]
    assert not future.empty
    assert future["asof_latest_qualifying_trade_date"].lt(
        future["final_episode_latest_qualifying_trade_date"]
    ).all()
    assert detail["latest_source_lag_bucket"].astype(str).ne("").all()
    assert detail["first_source_lag_bucket"].astype(str).ne("").all()


def test_operation_lag_bucket_exactly_covers_the_adopted_mature_grid() -> None:
    detail = pd.read_csv(
        DETAIL_CSV,
        dtype={"stock_id": str, "entry_date": str, "exit_date": str},
        keep_default_na=False,
        low_memory=False,
    )
    source = pd.read_csv(
        SOURCE_OPERATION_DETAIL_CSV,
        dtype={"stock_id": str, "entry_date": str, "exit_date": str},
        keep_default_na=False,
        low_memory=False,
    )
    source = source.loc[
        source["grid_id"].eq(ADOPTED_GRID_ID)
        & source["return_valid"].astype(str).eq("True")
    ]
    detail_keys = set(zip(detail["episode_key"], detail["stock_id"], detail["entry_date"]))
    source_keys = set(zip(source["episode_key"], source["stock_id"], source["entry_date"]))
    assert detail_keys == source_keys
    for _stock_id, stock in detail.groupby("stock_id", sort=False):
        ordered = stock.sort_values("entry_date", kind="mergesort")
        entries = ordered["entry_date"].iloc[1:].reset_index(drop=True)
        prior_exits = ordered["exit_date"].iloc[:-1].reset_index(drop=True)
        assert not entries.le(prior_exits).any()


def test_operation_lag_bucket_partitions_conserve_primary_and_sensitivity_rows() -> None:
    summary = pd.read_csv(LATEST_CSV, keep_default_na=False, low_memory=False)
    for analysis_basis in (PRIMARY_ANALYSIS_BASIS, SENSITIVITY_ANALYSIS_BASIS):
        for lag_basis in (
            "latest_qualifying_source_asof_trigger",
            "episode_first_qualifying_source",
            "latest_qualifying_source_watch_horizon_comparison",
        ):
            rows = summary.loc[
                summary["analysis_basis"].eq(analysis_basis)
                & summary["lag_basis_id"].eq(lag_basis)
            ]
            overall = int(rows.loc[rows["lag_bucket_id"].eq("all"), "operation_count"].iloc[0])
            bucket_total = int(
                pd.to_numeric(
                    rows.loc[~rows["lag_bucket_id"].eq("all"), "operation_count"],
                    errors="raise",
                ).sum()
            )
            assert bucket_total == overall
