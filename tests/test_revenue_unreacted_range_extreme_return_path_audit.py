from __future__ import annotations

import sys
from pathlib import Path

import pandas as pd


ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))

from revenue_unreacted_range_extreme_return_path_audit import (  # noqa: E402
    _canonical_raw_price_row_sha256,
    build_extreme_return_path_audit,
)
from validate_revenue_unreacted_range_extreme_return_path_audit import validate  # noqa: E402


SOURCE = ROOT / (
    "output/latest/research_backtest/revenue_unreacted_range_fixed_"
    "confirmation_feature_contrast_audit_detail_latest.csv"
)


def test_extreme_return_path_audit_is_complete_and_reproducible() -> None:
    assert validate() == []


def test_threshold_rows_remain_unresolved_candidates_after_partial_price_path_checks() -> None:
    detail = pd.read_csv(SOURCE, dtype={"stock_id": str}, low_memory=False)
    audit = build_extreme_return_path_audit(detail)
    realized = pd.to_numeric(detail["realized_return_pct"], errors="coerce")
    expected = detail[
        detail["decision_basis"].astype(str).str.lower().isin({"true", "1", "yes"})
        & ~detail["sensitivity_basis"].astype(str).str.lower().isin({"true", "1", "yes"})
        & detail["feature_time_basis"].eq("signal_date_close")
        & realized.abs().ge(80.0)
    ].drop_duplicates("episode_key")
    assert len(audit) == len(expected)
    assert set(audit["episode_key"]) == set(expected["episode_key"])
    assert not audit["episode_key"].duplicated().any()
    assert audit["price_path_trading_rows"].eq(20).all()
    assert audit["market_limit_violation_count"].eq(0).all()
    assert audit["all_ohlc_raw_match"].all()
    assert not audit["impossible_return_flag"].any()
    assert set(audit["statistical_trigger_status"]) == {"anomaly_candidate"}
    assert set(audit["price_path_classification"]) == {
        "candidate_continuous_price_path_repo_source_matched"
    }
    assert set(audit["root_cause_verification_status"]) == {
        "partial_root_checks_incomplete"
    }
    assert set(audit["final_disposition"]) == {"unresolved_anomaly_candidate"}
    assert audit["root_cause_checks_missing"].ne("").all()
    assert set(audit["primary_metric_handling"]) == {
        "retain_observed_candidate_and_block_promotion_until_resolved"
    }


def test_raw_price_source_hash_uses_only_the_consumed_stock_ohlc_row() -> None:
    base = pd.Series({"open": 10, "high": 11.0, "low": 9.5, "close": 10.5, "volume": 100})
    unrelated_change = pd.Series(
        {
            "open": 10.0,
            "high": 11,
            "low": 9.5,
            "close": 10.50,
            "volume": 999999,
            "stock_name": "changed",
        }
    )
    price_change = pd.Series({"open": 10, "high": 11, "low": 9.5, "close": 10.6})

    base_hash = _canonical_raw_price_row_sha256("1234", "20260701", base)
    assert base_hash == _canonical_raw_price_row_sha256("1234", "20260701", unrelated_change)
    assert base_hash != _canonical_raw_price_row_sha256("1234", "20260701", price_change)
