from __future__ import annotations

import sys
from pathlib import Path

import pandas as pd


ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))

from revenue_unreacted_range_extreme_return_path_audit import build_extreme_return_path_audit  # noqa: E402
from validate_revenue_unreacted_range_extreme_return_path_audit import validate  # noqa: E402


SOURCE = ROOT / (
    "output/latest/research_backtest/revenue_unreacted_range_fixed_"
    "confirmation_feature_contrast_audit_detail_latest.csv"
)


def test_extreme_return_path_audit_is_complete_and_reproducible() -> None:
    assert validate() == []


def test_extreme_return_rows_are_real_paths_not_duplicate_or_impossible_jumps() -> None:
    detail = pd.read_csv(SOURCE, dtype={"stock_id": str}, low_memory=False)
    audit = build_extreme_return_path_audit(detail)
    assert len(audit) == 14
    assert not audit["episode_key"].duplicated().any()
    assert audit["price_path_trading_rows"].eq(20).all()
    assert audit["market_limit_violation_count"].eq(0).all()
    assert audit["all_ohlc_raw_match"].all()
    assert not audit["impossible_return_flag"].any()
    assert set(audit["price_path_classification"]) == {"plausible_extreme_continuous_gain"}
