from __future__ import annotations

import sys
from pathlib import Path

import pandas as pd
import pytest


ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))

import revenue_unreacted_range_lag_strength_matrix as lag_strength  # noqa: E402
from revenue_unreacted_range_lag_strength_matrix import (  # noqa: E402
    ALL_LINEAGE_COLUMNS,
    DETAIL_CSV,
    LATEST_CSV,
    SOURCE_DATE_COLUMNS,
    SOURCE_SNAPSHOT_CUTOFF_DATE,
    _fixed_source_lineage,
    _source_episodes,
    canonical_fixed_source_slice_sha256,
)
from revenue_unreacted_range_monthly_revenue_cross_market_resolution import (  # noqa: E402
    monthly_revenue_history_blob_sha256,
)
from validate_revenue_unreacted_range_lag_strength_matrix import (  # noqa: E402
    _expected_artifact_version,
    _runtime_lineage_errors,
    validate,
)
from revenue_unreacted_range_source_snapshot_projection import (  # noqa: E402
    V1_PROJECTION_VERSION,
    V2_PROJECTION_VERSION,
)


def _source_episode_row() -> dict[str, object]:
    return {
        "research_artifact_id": "fixed_confirmation_feature_contrast_audit",
        "artifact_version": "fixed_confirmation_v1",
        "episode_key": "9999:202605:20260620",
        "stock_id": "9999",
        "source_monthly_revenue_period": "202605",
        "source_monthly_revenue_source_table_date": "20260617",
        "signal_date": "20260620",
        "confirmation_date": "20260623",
        "entry_date": "20260624",
        "exit_date": "20260710",
        "realized_return_pct": "8.25",
        "full_monthly_revenue_latest_yoy_pct": "35.0",
        "full_monthly_revenue_cumulative_yoy_pct": "25.0",
        "full_monthly_revenue_prev1_latest_yoy_pct": "30.0",
        "full_monthly_revenue_prev2_latest_yoy_pct": "20.0",
        "full_monthly_revenue_prev3_latest_yoy_pct": "10.0",
        "full_monthly_revenue_latest_yoy_delta_1m_pct_points": "5.0",
        "decision_basis": True,
        "sensitivity_basis": False,
        "feature_time_basis": "signal_date_close",
        "source_revenue_or_price_anomaly_candidate_flag": False,
    }


def test_revenue_lag_strength_matrix_passes() -> None:
    assert validate() == []


def test_lag_artifact_version_is_projection_bound_and_unknown_fails_closed() -> None:
    assert lag_strength.artifact_version_for_projection(V1_PROJECTION_VERSION) == (
        lag_strength.V1_ARTIFACT_VERSION
    )
    assert lag_strength.artifact_version_for_projection(V2_PROJECTION_VERSION) == (
        lag_strength.V2_ARTIFACT_VERSION
    )
    assert _expected_artifact_version(V1_PROJECTION_VERSION) == (
        lag_strength.V1_ARTIFACT_VERSION
    )
    assert _expected_artifact_version(V2_PROJECTION_VERSION) == (
        lag_strength.V2_ARTIFACT_VERSION
    )
    with pytest.raises(RuntimeError, match="unsupported canonical source projection"):
        lag_strength.artifact_version_for_projection("source_snapshot_projection_v3")


def test_lag_runtime_lineage_validator_rejects_each_mutated_field() -> None:
    expected = {column: f"expected-{index}" for index, column in enumerate(ALL_LINEAGE_COLUMNS)}
    frame = pd.DataFrame([expected])
    for column in ALL_LINEAGE_COLUMNS:
        mutated = frame.copy()
        mutated.loc[0, column] = f"mutated-{column}"
        assert _runtime_lineage_errors(
            mutated,
            label="synthetic",
            expected=expected,
        ) == [f"lag strength matrix synthetic runtime lineage drift: {column}"]


def test_lag_projection_lineage_uses_cutoff_manifest_not_mutable_latest(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    baseline_history, baseline_lineage = lag_strength._monthly_revenue_runtime_context()
    mutable_latest = pd.read_csv(
        lag_strength.MONTHLY_REVENUE_HISTORY,
        dtype=str,
        keep_default_na=False,
        low_memory=False,
    )
    future_rows = mutable_latest.iloc[[0, 0]].copy()
    future_rows["source_table_date"] = "20260714"
    mutated_latest = tmp_path / "monthly_revenue_history_latest.csv"
    pd.concat([mutable_latest, future_rows], ignore_index=True).to_csv(
        mutated_latest,
        index=False,
    )
    monkeypatch.setattr(lag_strength, "MONTHLY_REVENUE_HISTORY", mutated_latest)

    cutoff_history, cutoff_lineage = lag_strength._monthly_revenue_runtime_context()
    manifest = lag_strength.load_source_snapshot_projection_manifest(
        lag_strength.SOURCE_SNAPSHOT_MANIFEST_CSV
    ).iloc[0]

    pd.testing.assert_frame_equal(baseline_history, cutoff_history, check_dtype=False)
    assert cutoff_lineage == baseline_lineage
    assert cutoff_lineage["monthly_revenue_history_blob_sha256"] == str(
        manifest["monthly_revenue_history_blob_sha256"]
    ).lower()
    assert cutoff_lineage["monthly_revenue_canonical_table_sha256"] == str(
        manifest["cutoff_revenue_subset_semantic_sha256"]
    ).lower()
    assert cutoff_lineage["source_projection_cutoff_date"] == SOURCE_SNAPSHOT_CUTOFF_DATE
    assert monthly_revenue_history_blob_sha256(mutated_latest) != cutoff_lineage[
        "monthly_revenue_history_blob_sha256"
    ]


def test_lag_price_dates_ignore_post_cutoff_rows_and_duplicates(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    pd.DataFrame(
        {"date": ["20260710", "20260713", "20260714", "20260714"]}
    ).to_csv(tmp_path / "9999.csv", index=False)
    monkeypatch.setattr(lag_strength, "PRICE_HISTORY_DIR", tmp_path)

    dates = lag_strength._load_price_dates("9999", {})

    assert dates.tolist() == ["20260710", "20260713"]


def test_lag_price_dates_fail_on_pre_cutoff_duplicate(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    pd.DataFrame(
        {"date": ["20260710", "20260710", "20260714"]}
    ).to_csv(tmp_path / "9999.csv", index=False)
    monkeypatch.setattr(lag_strength, "PRICE_HISTORY_DIR", tmp_path)

    with pytest.raises(RuntimeError, match="repeats trading dates within cutoff"):
        lag_strength._load_price_dates("9999", {})


def test_complete_post_cutoff_source_episode_is_ignored_without_output_drift(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    baseline_row = _source_episode_row()
    post_cutoff_row = {
        **baseline_row,
        "episode_key": "9999:202606:20260715",
        "source_monthly_revenue_period": "202606",
        "source_monthly_revenue_source_table_date": "20260714",
        "signal_date": "20260715",
        "confirmation_date": "20260716",
        "entry_date": "20260717",
        "exit_date": "20260814",
    }

    baseline = _source_episodes(pd.DataFrame([baseline_row]))
    with_post_cutoff = _source_episodes(
        pd.DataFrame([baseline_row, post_cutoff_row])
    )

    pd.testing.assert_frame_equal(with_post_cutoff, baseline)
    assert canonical_fixed_source_slice_sha256(with_post_cutoff) == (
        canonical_fixed_source_slice_sha256(baseline)
    )
    assert _fixed_source_lineage(with_post_cutoff) == _fixed_source_lineage(baseline)

    monthly_history = pd.DataFrame(
        [
            {
                "stock_id": "9999",
                "revenue_period": "202605",
                "source_table_date": "20260617",
                "latest_revenue_yoy_pct": "35.0",
                "cumulative_revenue_yoy_pct": "25.0",
            }
        ]
    )
    runtime_lineage = {
        column: f"synthetic-{index}"
        for index, column in enumerate(ALL_LINEAGE_COLUMNS)
        if column not in lag_strength.FIXED_SOURCE_LINEAGE_COLUMNS
    }
    runtime_lineage["source_projection_version"] = V1_PROJECTION_VERSION
    monkeypatch.setattr(
        lag_strength,
        "_monthly_revenue_runtime_context",
        lambda *_args, **_kwargs: (monthly_history, runtime_lineage),
    )
    monkeypatch.setattr(
        lag_strength,
        "_trading_day_lag",
        lambda _stock_id, _start_date, _end_date, _cache: 1,
    )
    monkeypatch.setattr(lag_strength, "_now_text", lambda: "2026-08-02 12:00:00 Asia/Taipei")

    baseline_summary, baseline_detail = lag_strength.build_lag_strength_matrix(
        pd.DataFrame([baseline_row])
    )
    candidate_summary, candidate_detail = lag_strength.build_lag_strength_matrix(
        pd.DataFrame([baseline_row, post_cutoff_row])
    )

    pd.testing.assert_frame_equal(candidate_summary, baseline_summary)
    pd.testing.assert_frame_equal(candidate_detail, baseline_detail)


@pytest.mark.parametrize("date_column", SOURCE_DATE_COLUMNS)
def test_lag_pre_cutoff_source_date_malformed_fails_closed(date_column: str) -> None:
    row = _source_episode_row()
    row[date_column] = "2026071"

    with pytest.raises(RuntimeError, match=f"contains invalid {date_column}"):
        _source_episodes(pd.DataFrame([row]))


def test_lag_pre_cutoff_duplicate_episode_fails_closed() -> None:
    row = _source_episode_row()

    with pytest.raises(RuntimeError, match="contains duplicate episodes"):
        _source_episodes(pd.DataFrame([row, row]))


def test_fixed_source_semantic_hash_changes_on_source_mutation() -> None:
    episodes = _source_episodes(pd.DataFrame([_source_episode_row()]))
    baseline_hash = canonical_fixed_source_slice_sha256(episodes)
    baseline_lineage = _fixed_source_lineage(episodes)
    generated_at_only = episodes.assign(generated_at="2026-08-02 00:00:00 Asia/Taipei")
    mutated = episodes.copy()
    mutated.loc[0, "realized_return_pct"] = "9.25"

    assert canonical_fixed_source_slice_sha256(generated_at_only) == baseline_hash
    assert canonical_fixed_source_slice_sha256(mutated) != baseline_hash
    assert _fixed_source_lineage(mutated)[
        "source_fixed_confirmation_cutoff_semantic_sha256"
    ] != baseline_lineage["source_fixed_confirmation_cutoff_semantic_sha256"]


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
