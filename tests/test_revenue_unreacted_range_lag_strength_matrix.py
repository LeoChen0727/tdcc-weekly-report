from __future__ import annotations

import sys
from pathlib import Path

import pandas as pd


ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))

from revenue_unreacted_range_lag_strength_matrix import (  # noqa: E402
    DETAIL_CSV,
    LATEST_CSV,
    MONTHLY_REVENUE_RUNTIME_LINEAGE_COLUMNS,
)
from validate_revenue_unreacted_range_lag_strength_matrix import (  # noqa: E402
    _runtime_lineage_errors,
    validate,
)


def test_revenue_lag_strength_matrix_passes() -> None:
    assert validate() == []


def test_lag_runtime_lineage_validator_rejects_each_mutated_sha() -> None:
    expected = {
        column: character * 64
        for column, character in zip(
            MONTHLY_REVENUE_RUNTIME_LINEAGE_COLUMNS,
            ("a", "b", "c"),
        )
    }
    frame = pd.DataFrame([expected])
    for column in MONTHLY_REVENUE_RUNTIME_LINEAGE_COLUMNS:
        mutated = frame.copy()
        mutated.loc[0, column] = "d" * 64
        assert _runtime_lineage_errors(
            mutated,
            label="synthetic",
            expected=expected,
        ) == [f"lag strength matrix synthetic runtime lineage drift: {column}"]


def test_revenue_lag_matrix_has_no_omission_overlap_or_hidden_small_sample_gate() -> None:
    detail = pd.read_csv(DETAIL_CSV, dtype={"stock_id": str}, keep_default_na=False, low_memory=False)
    summary = pd.read_csv(LATEST_CSV, keep_default_na=False, low_memory=False)
    assert not detail["episode_key"].duplicated().any()
    assert detail["current_revenue_lag_bucket"].ne("").all()
    candidate_flags = detail["abs_ge80_anomaly_candidate_flag"].astype(str).str.lower().isin(
        {"true", "1", "yes"}
    )
    source_candidate_flags = detail[
        "source_revenue_or_price_anomaly_candidate_flag"
    ].astype(str).str.lower().isin({"true", "1", "yes"})
    baseline = summary[summary["condition_test_id"].eq("all_confirmed_non_overlap")].iloc[0]
    assert int(baseline["accepted_trade_count"]) == len(detail)
    assert int(baseline["abs_ge80_anomaly_candidate_count"]) == int(candidate_flags.sum())
    assert int(baseline["source_anomaly_candidate_count"]) == int(source_candidate_flags.sum())
    assert set(summary["promotion_readiness"]) == {
        "blocked_pending_root_cause_anomaly_candidate_review"
    }
    assert set(summary["sample_policy"]) == {"sample_count_disclosed_not_used_as_automatic_rejection"}
    assert summary["same_stock_overlap_pair_count"].eq(0).all()
    assert summary["same_stock_revenue_period_repeat_count"].eq(0).all()
