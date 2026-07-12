from __future__ import annotations

import sys
from pathlib import Path

import pandas as pd


ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))

from revenue_unreacted_range_lag_strength_matrix import DETAIL_CSV, LATEST_CSV  # noqa: E402
from validate_revenue_unreacted_range_lag_strength_matrix import validate  # noqa: E402


def test_revenue_lag_strength_matrix_passes() -> None:
    assert validate() == []


def test_revenue_lag_matrix_has_no_omission_overlap_or_hidden_small_sample_gate() -> None:
    detail = pd.read_csv(DETAIL_CSV, dtype={"stock_id": str}, keep_default_na=False, low_memory=False)
    summary = pd.read_csv(LATEST_CSV, keep_default_na=False, low_memory=False)
    assert len(detail) == 1530
    assert not detail["episode_key"].duplicated().any()
    assert detail["current_revenue_lag_bucket"].ne("").all()
    assert set(summary["sample_policy"]) == {"sample_count_disclosed_not_used_as_automatic_rejection"}
    assert summary["same_stock_overlap_pair_count"].eq(0).all()
    assert summary["same_stock_revenue_period_repeat_count"].eq(0).all()
