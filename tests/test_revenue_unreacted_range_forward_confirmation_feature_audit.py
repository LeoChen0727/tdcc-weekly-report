from __future__ import annotations

import sys
from pathlib import Path

import numpy as np
import pandas as pd
import pytest


ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))

from revenue_unreacted_range_forward_confirmation_feature_audit import (  # noqa: E402
    V1_ARTIFACT_VERSION,
    V2_ARTIFACT_VERSION,
    artifact_version_for_projection,
    PRIMARY_ANALYSIS_BASIS,
    EXPECTED_SOURCE_ARTIFACT_ID,
    EXPECTED_SOURCE_ARTIFACT_VERSION,
    SOURCE_PROJECTION_CUTOFF_DATE,
    SOURCE_PROJECTION_SUMMARY_COLUMNS,
    _normalize_source_detail,
    build_forward_confirmation_feature_audit,
    build_operation_return_review,
)
from revenue_unreacted_range_source_snapshot_projection import (  # noqa: E402
    ARTIFACT_ID as SOURCE_PROJECTION_ARTIFACT_ID,
    ARTIFACT_VERSION as SOURCE_PROJECTION_ARTIFACT_VERSION,
    MANIFEST_COLUMNS as SOURCE_PROJECTION_MANIFEST_COLUMNS,
    MODEL_ID as SOURCE_PROJECTION_MODEL_ID,
    PROJECTION_ID as SOURCE_PROJECTION_ID,
    PROJECTION_POLICY_ID as SOURCE_PROJECTION_POLICY_ID,
    PROJECTION_VERSION as SOURCE_PROJECTION_VERSION,
    canonical_projected_source_detail_semantic_sha256,
    V1_PROJECTION_VERSION,
    V2_PROJECTION_VERSION,
)
from validate_revenue_unreacted_range_forward_confirmation_feature_audit import (  # noqa: E402
    validate,
)
import validate_revenue_unreacted_range_forward_confirmation_feature_audit as forward_validator  # noqa: E402


MONTHLY_REVENUE_BLOB_SHA = "a" * 64
MONTHLY_REVENUE_TABLE_SHA = "b" * 64
CROSS_MARKET_REGISTRY_SHA = "c" * 64


def test_forward_artifact_version_is_projection_bound() -> None:
    assert artifact_version_for_projection(V1_PROJECTION_VERSION) == V1_ARTIFACT_VERSION
    assert artifact_version_for_projection(V2_PROJECTION_VERSION) == V2_ARTIFACT_VERSION
    with pytest.raises(RuntimeError, match="unsupported canonical source projection"):
        artifact_version_for_projection("unknown")


def _stock_frame(stock_id: str, *, false_index: int | None, launch_index: int) -> pd.DataFrame:
    dates = pd.bdate_range("2025-01-02", periods=100).strftime("%Y%m%d")
    close = np.full(100, 10.0)
    cross = np.zeros(100, dtype=bool)
    if false_index is not None:
        close[false_index] = 10.5
        close[false_index + 1] = 10.4
        cross[false_index] = True
    close[launch_index] = 11.0
    close[launch_index + 1] = 11.3
    close[launch_index + 5 :] = 13.3
    cross[launch_index] = True
    frame = pd.DataFrame(
        {
            "stock_id": stock_id,
            "date": dates,
            "open": close,
            "high": close,
            "low": close,
            "close": close,
            "analysis_open": close + 0.1,
            "analysis_close": close,
            "previous_20d_highest_close": 10.0,
            "close_breakout_prev20": close > 10.0,
            "cross_breakout_prev20": cross,
            "cross_breakout_prev40": cross,
            "cross_breakout_prev60": cross,
            "close_breakout_prev40": cross,
            "close_breakout_prev60": cross,
            "volume_ratio_prev20": 2.0,
            "ma20": 9.5,
            "ma60": 10.0,
            "ma120": 9.0,
            "ema23": 9.5,
            "obv_slope_5d": 1.0,
            "obv_above_ma20": True,
            "k_value": 60.0,
            "d_value": 50.0,
            "kdj_j_value": 80.0,
            "macd_hist": 1.0,
            "rsi14": 60.0,
            "return_5d_pct": 3.0,
            "return_20d_pct": 10.0,
            "range_width_23d_pct": 10.0,
            "range_width_60d_pct": 20.0,
            "close_position_120d_pct": 60.0,
            "signal_body_pct": 2.0,
            "close_location_pct": 75.0,
            "solid_red_candle": True,
            "tdcc_history_available": True,
            "high_thresholds_up": True,
            "tdcc_consecutive_up_weeks": 2,
            "signal_market_regime": "mild_bull",
            "full_monthly_revenue_context_ready": True,
            "full_monthly_revenue_source_table_date": dates[20],
            "latest_qualifying_revenue_source_date_asof": dates[20],
            "full_monthly_revenue_period": "202412",
            "full_monthly_revenue_latest_yoy_pct": 30.0,
            "full_monthly_revenue_cumulative_yoy_pct": 20.0,
            "full_monthly_revenue_prev1_latest_yoy_pct": 20.0,
            "full_monthly_revenue_latest_yoy_delta_1m_pct_points": 5.0,
            "ema23_slope_5d_pct": 1.0,
            "distance_to_ema23_pct": 5.0,
        }
    )
    return frame


def _source_row(stock: pd.DataFrame, stock_id: str, *, start: int, end: int, first: int, launch: int) -> dict[str, object]:
    return {
        "artifact_id": EXPECTED_SOURCE_ARTIFACT_ID,
        "artifact_version": EXPECTED_SOURCE_ARTIFACT_VERSION,
        "condition_variant_id": "absolute_or_two_month_yoy_ge15",
        "episode_key": f"episode-{stock_id}",
        "stock_id": stock_id,
        "stock_name": stock_id,
        "episode_start_trade_date": stock.at[start, "date"],
        "episode_start_source_date": stock.at[start, "date"],
        "latest_qualifying_source_date": stock.at[start, "date"],
        "qualifying_source_dates": stock.at[start, "date"],
        "latest_qualifying_trade_date": stock.at[start, "date"],
        "qualifying_trade_dates": stock.at[start, "date"],
        "episode_end_date": stock.at[end, "date"],
        "episode_status": "launch_within_active_horizon",
        "first_breakout_date": stock.at[first, "date"],
        "first_breakout_outcome": "mature_failure" if first != launch else "strict_success",
        "launch_date": stock.at[launch, "date"],
        "qualifying_source_revenue_anomaly_candidate_flag": False,
        "unresolved_price_path_candidate_flag": False,
        "same_stock_non_overlap_applied": True,
        "monthly_revenue_history_blob_sha256": MONTHLY_REVENUE_BLOB_SHA,
        "monthly_revenue_canonical_table_sha256": MONTHLY_REVENUE_TABLE_SHA,
        "cross_market_resolution_registry_canonical_sha256": CROSS_MARKET_REGISTRY_SHA,
    }


def _source_projection_manifest(source: pd.DataFrame) -> pd.DataFrame:
    projected_sha = canonical_projected_source_detail_semantic_sha256(source)
    row = {column: "" for column in SOURCE_PROJECTION_MANIFEST_COLUMNS}
    row.update(
        {
            "generated_at": "2026-07-31 00:00:00 Asia/Taipei",
            "model_id": SOURCE_PROJECTION_MODEL_ID,
            "artifact_id": SOURCE_PROJECTION_ARTIFACT_ID,
            "artifact_version": SOURCE_PROJECTION_ARTIFACT_VERSION,
            "projection_id": SOURCE_PROJECTION_ID,
            "projection_version": SOURCE_PROJECTION_VERSION,
            "projection_policy_id": SOURCE_PROJECTION_POLICY_ID,
            "cutoff_date": SOURCE_PROJECTION_CUTOFF_DATE,
            "full_source_artifact_id": EXPECTED_SOURCE_ARTIFACT_ID,
            "full_source_artifact_version": EXPECTED_SOURCE_ARTIFACT_VERSION,
            "full_source_episode_row_count": len(source),
            "full_source_episode_semantic_sha256": projected_sha,
            "monthly_revenue_history_blob_sha256": MONTHLY_REVENUE_BLOB_SHA,
            "monthly_revenue_canonical_table_sha256": MONTHLY_REVENUE_TABLE_SHA,
            "cross_market_resolution_registry_canonical_sha256": CROSS_MARKET_REGISTRY_SHA,
            "cutoff_revenue_subset_row_count": 1,
            "cutoff_revenue_subset_semantic_sha256": MONTHLY_REVENUE_TABLE_SHA,
            "cutoff_price_input_stock_count": source["stock_id"].nunique(),
            "cutoff_price_input_row_count": len(source),
            "cutoff_price_input_file_semantic_sha256s": "d" * 64,
            "cutoff_price_input_semantic_sha256": "d" * 64,
            "applied_monthly_resolution_count": 0,
            "applied_monthly_resolution_ids": "none",
            "applied_monthly_resolution_semantic_sha256": "e" * 64,
            "applied_price_resolution_count": 0,
            "applied_price_resolution_ids": "none",
            "applied_price_resolution_semantic_sha256": "f" * 64,
            "projected_episode_row_count": len(source),
            "projected_episode_semantic_sha256": projected_sha,
            "projected_max_source_date": max(
                source["latest_qualifying_source_date"].astype(str)
            ),
            "projected_max_trade_date": max(
                source["latest_qualifying_trade_date"].astype(str)
            ),
            "projected_max_episode_end_date": max(source["episode_end_date"].astype(str)),
            "research_only": "true",
            "formal_model_use_allowed": "false",
            "approved_for_daily": "false",
            "production_change": "false",
            "promotion_evidence_allowed": "false",
            "ranking_consumption_allowed": "false",
            "pdf_consumption_allowed": "false",
        }
    )
    return pd.DataFrame([row], columns=list(SOURCE_PROJECTION_MANIFEST_COLUMNS))


@pytest.mark.parametrize(
    ("column", "value", "message"),
    (
        ("artifact_id", "wrong_source_artifact", "artifact id drift"),
        ("artifact_version", "source_first_condition_v2_20260714", "artifact version drift"),
    ),
)
def test_forward_source_normalization_rejects_mutated_or_stale_artifact(
    column: str,
    value: str,
    message: str,
) -> None:
    stock = _stock_frame("4916", false_index=25, launch_index=50)
    source = pd.DataFrame(
        [_source_row(stock, "4916", start=20, end=50, first=25, launch=50)]
    )
    source.loc[0, column] = value

    with pytest.raises(RuntimeError, match=message):
        _normalize_source_detail(source)
    assert any(message in error for error in forward_validator._source_lineage_errors(source))


def _audit_frames() -> tuple[
    pd.DataFrame,
    pd.DataFrame,
    pd.DataFrame,
    pd.DataFrame,
    pd.DataFrame,
    dict[str, pd.DataFrame],
]:
    stock_4916 = _stock_frame("4916", false_index=25, launch_index=50)
    stock_1303 = _stock_frame("1303", false_index=None, launch_index=30)
    source = pd.DataFrame(
        [
            _source_row(stock_4916, "4916", start=20, end=50, first=25, launch=50),
            _source_row(stock_1303, "1303", start=20, end=30, first=30, launch=30),
        ]
    )
    daily = {"4916": stock_4916, "1303": stock_1303}
    return (
        *build_forward_confirmation_feature_audit(
            source_detail=source,
            daily_by_stock=daily,
            source_projection_manifest=_source_projection_manifest(source),
        ),
        daily,
    )


def test_first_match_policy_keeps_4916_false_breakout_in_baseline() -> None:
    summary, detail, events, _, _, _ = _audit_frames()
    row = detail.loc[
        detail["stock_id"].eq("4916")
        & detail["rule_id"].eq("first_close_cross_prev20")
    ].iloc[0]
    assert row["trigger_date"] == events.loc[
        events["stock_id"].eq("4916")
        & events["contrast_group"].eq("first_mature_failure_event"),
        "trigger_date",
    ].iloc[0]
    assert row["outcome_status"] == "mature_failure"
    assert summary.loc[
        summary["analysis_basis"].eq(PRIMARY_ANALYSIS_BASIS)
        & summary["rule_id"].eq("first_close_cross_prev20"),
        "strict_success_count",
    ].iloc[0] == 1


def test_summary_carries_all_eight_source_projection_lineage_fields() -> None:
    summary, _, _, _, _, _ = _audit_frames()

    observed = tuple(
        column for column in summary.columns if column.startswith("source_projection_")
    )
    assert observed == SOURCE_PROJECTION_SUMMARY_COLUMNS
    for column in SOURCE_PROJECTION_SUMMARY_COLUMNS:
        assert summary[column].nunique(dropna=False) == 1
    assert set(summary["source_projection_artifact_id"]) == {
        SOURCE_PROJECTION_ARTIFACT_ID
    }
    assert set(summary["source_projection_cutoff_date"]) == {
        SOURCE_PROJECTION_CUTOFF_DATE
    }
    assert set(summary["source_projection_episode_row_count"]) == {2}
    assert summary["source_projection_detail_semantic_sha256"].str.fullmatch(
        r"[0-9a-f]{64}"
    ).all()


def test_source_level_reference_preserves_old_first_breakout_parity() -> None:
    _, detail, _, _, _, daily = _audit_frames()
    row = detail.loc[
        detail["stock_id"].eq("4916")
        & detail["rule_id"].eq("source_first_close_above_prev20_reference")
    ].iloc[0]
    assert row["trigger_date"] == daily["4916"].at[25, "date"]
    assert row["outcome_status"] == "mature_failure"
    assert row["rule_trigger_mode"] == "level"


@pytest.mark.parametrize(
    ("mutation", "expected_message"),
    (
        ("missing", "baseline reference is missing source episode keys"),
        ("extra", "baseline reference has extra episode keys"),
        ("duplicate", "baseline reference has duplicate episode keys"),
    ),
)
def test_source_reference_membership_mutations_fail_closed_without_key_error(
    mutation: str,
    expected_message: str,
) -> None:
    source = pd.DataFrame(
        [
            {
                "episode_key": "episode-a",
                "first_breakout_date": "20250110",
                "first_breakout_outcome": "strict_success",
            },
            {
                "episode_key": "episode-b",
                "first_breakout_date": "20250120",
                "first_breakout_outcome": "mature_failure",
            },
        ]
    )
    reference = pd.DataFrame(
        [
            {
                "episode_key": "episode-a",
                "rule_id": "source_first_close_above_prev20_reference",
                "trigger_date": "20250110",
                "outcome_status": "strict_success",
            },
            {
                "episode_key": "episode-b",
                "rule_id": "source_first_close_above_prev20_reference",
                "trigger_date": "20250120",
                "outcome_status": "mature_failure",
            },
        ]
    )
    if mutation == "missing":
        reference = reference.loc[reference["episode_key"].ne("episode-b")].copy()
    elif mutation == "extra":
        reference = pd.concat(
            [
                reference,
                pd.DataFrame(
                    [
                        {
                            "episode_key": "episode-extra",
                            "rule_id": "source_first_close_above_prev20_reference",
                            "trigger_date": "20250130",
                            "outcome_status": "strict_success",
                        }
                    ]
                ),
            ],
            ignore_index=True,
        )
    else:
        reference = pd.concat([reference, reference.iloc[[0]]], ignore_index=True)

    errors = forward_validator._source_reference_errors(source, reference)

    assert any(expected_message in error for error in errors)


def test_explicit_source_detail_requires_projection_manifest() -> None:
    stock = _stock_frame("4916", false_index=25, launch_index=50)
    source = pd.DataFrame(
        [_source_row(stock, "4916", start=20, end=50, first=25, launch=50)]
    )

    with pytest.raises(
        ValueError,
        match="source_projection_manifest is required with explicit source_detail",
    ):
        build_forward_confirmation_feature_audit(
            source_detail=source,
            daily_by_stock={"4916": stock},
        )


def test_explicit_daily_frame_cannot_extend_projection_cutoff() -> None:
    stock = _stock_frame("4916", false_index=25, launch_index=50)
    source = pd.DataFrame(
        [_source_row(stock, "4916", start=20, end=50, first=25, launch=50)]
    )
    stock.loc[stock.index[-1], "date"] = "20260714"

    with pytest.raises(
        RuntimeError,
        match="daily frame exceeds source projection cutoff",
    ):
        build_forward_confirmation_feature_audit(
            source_detail=source,
            daily_by_stock={"4916": stock},
            source_projection_manifest=_source_projection_manifest(source),
        )


def test_direct_source_detail_filters_non_primary_variants_before_expansion() -> None:
    stock = _stock_frame("4916", false_index=25, launch_index=50)
    primary = _source_row(stock, "4916", start=20, end=50, first=25, launch=50)
    alternate = dict(primary)
    alternate["condition_variant_id"] = "absolute_or_two_month_yoy_ge20"
    source = pd.DataFrame([primary, alternate])

    summary, detail, events, _, _ = build_forward_confirmation_feature_audit(
        source_detail=source,
        daily_by_stock={"4916": stock},
        source_projection_manifest=_source_projection_manifest(source),
    )

    assert set(detail["episode_key"]) == {"episode-4916"}
    assert set(events["episode_key"]) == {"episode-4916"}
    assert set(summary["source_episode_count"]) == {1}


def test_current_post_cutoff_episode_cannot_change_projected_forward_outputs() -> None:
    stock_4916 = _stock_frame("4916", false_index=25, launch_index=50)
    stock_1303 = _stock_frame("1303", false_index=None, launch_index=30)
    projected_source = pd.DataFrame(
        [
            _source_row(stock_4916, "4916", start=20, end=50, first=25, launch=50),
            _source_row(stock_1303, "1303", start=20, end=30, first=30, launch=30),
        ]
    )
    projected_daily = {"4916": stock_4916, "1303": stock_1303}
    manifest = _source_projection_manifest(projected_source)
    expected = build_forward_confirmation_feature_audit(
        source_detail=projected_source,
        daily_by_stock=projected_daily,
        source_projection_manifest=manifest,
    )

    post_cutoff_stock = _stock_frame("9999", false_index=None, launch_index=30)
    post_cutoff = _source_row(
        post_cutoff_stock,
        "9999",
        start=20,
        end=30,
        first=30,
        launch=30,
    )
    for column in (
        "episode_start_source_date",
        "latest_qualifying_source_date",
        "qualifying_source_dates",
        "episode_start_trade_date",
        "latest_qualifying_trade_date",
        "qualifying_trade_dates",
        "first_breakout_date",
        "launch_date",
    ):
        post_cutoff[column] = "20260714"
    post_cutoff["episode_end_date"] = "20260715"
    current_source = pd.concat(
        [projected_source, pd.DataFrame([post_cutoff])],
        ignore_index=True,
    )

    with pytest.raises(RuntimeError, match="source snapshot projection binding failed"):
        build_forward_confirmation_feature_audit(
            source_detail=current_source,
            daily_by_stock={**projected_daily, "9999": post_cutoff_stock},
            source_projection_manifest=manifest,
        )

    observed = build_forward_confirmation_feature_audit(
        source_detail=projected_source,
        daily_by_stock={**projected_daily, "9999": post_cutoff_stock},
        source_projection_manifest=manifest,
    )
    for expected_frame, observed_frame in zip(expected, observed, strict=True):
        pd.testing.assert_frame_equal(
            expected_frame.drop(columns=["generated_at"], errors="ignore"),
            observed_frame.drop(columns=["generated_at"], errors="ignore"),
        )


def test_next_day_close_rule_rejects_false_breakout_and_selects_later_launch() -> None:
    _, detail, events, _, _, daily = _audit_frames()
    row = detail.loc[
        detail["stock_id"].eq("4916")
        & detail["rule_id"].eq("prev20_next_close_continuation")
    ].iloc[0]
    launch_event = events.loc[
        events["stock_id"].eq("4916")
        & events["contrast_group"].eq("strict_success_launch_event")
    ].iloc[0]
    stock = daily["4916"]
    launch_index = int(stock.index[stock["date"].eq(launch_event["trigger_date"])][0])
    assert row["trigger_date"] == launch_event["trigger_date"]
    assert row["outcome_status"] == "strict_success"
    assert row["confirmation_date"] == stock.at[launch_index + 1, "date"]
    assert row["entry_date"] == stock.at[launch_index + 2, "date"]
    assert float(row["entry_open"]) == float(stock.at[launch_index + 2, "analysis_open"])


def test_next_day_confirmation_uses_same_boundary_policy_for_all_labels() -> None:
    _, detail, _, _, _, daily = _audit_frames()
    row = detail.loc[
        detail["stock_id"].eq("1303")
        & detail["rule_id"].eq("prev20_next_close_continuation")
    ].iloc[0]
    stock = daily["1303"]
    trigger_index = int(stock.index[stock["date"].eq(row["trigger_date"])][0])
    assert row["trigger_date"] == stock.at[30, "date"]
    assert row["confirmation_date"] == stock.at[trigger_index + 1, "date"]
    assert row["selection_status"] == "confirmed_first_rule_match"


def test_rule_detail_is_nonduplicated_and_event_features_are_normalized() -> None:
    _, detail, events, feature, return_review, _ = _audit_frames()
    assert not detail.duplicated(["episode_key", "rule_id"]).any()
    assert not events.duplicated(["episode_key", "contrast_group"]).any()
    assert len(events.loc[events["stock_id"].eq("4916")]) == 2
    assert len(events.loc[events["stock_id"].eq("1303")]) == 1
    assert "volume_ratio_prev20" not in detail.columns
    assert "volume_ratio_prev20" in events.columns
    assert set(feature["row_type"]) == {"binary_feature", "numeric_feature"}
    assert return_review.empty


def test_large_operation_return_is_replayed_and_retained_as_review_candidate() -> None:
    dates = pd.bdate_range("2025-01-02", periods=22).strftime("%Y%m%d")
    close = np.geomspace(10.0, 19.0, num=len(dates))
    entry_index = 1
    exit_index = len(dates) - 1
    fixed_return = (close[exit_index] / close[entry_index] - 1.0) * 100.0
    daily = pd.DataFrame(
        {
            "date": dates,
            "open": close,
            "close": close,
            "analysis_open": close,
            "analysis_close": close,
            "price_resolution_ids_on_date": "",
        }
    )
    detail = pd.DataFrame(
        [
            {
                "generated_at": "2026-07-13T00:00:00+08:00",
                "stock_id": "9999",
                "stock_name": "覆核樣本",
                "rule_id": "first_close_cross_prev20",
                "entry_date": dates[entry_index],
                "entry_open": close[entry_index],
                "fixed_exit_date": dates[exit_index],
                "fixed_exit_close": close[exit_index],
                "fixed_d20_return_pct": fixed_return,
                "operation_return_review_candidate_flag": True,
            }
        ]
    )

    review = build_operation_return_review(detail, {"9999": daily})

    assert len(review) == 1
    row = review.iloc[0]
    assert abs(float(row["replayed_fixed_d20_return_pct"]) - fixed_return) <= 0.0001
    assert float(row["max_abs_raw_close_return_1d_pct"]) < 20.0
    assert row["bottom_level_price_path_result"] == "no_single_day_scale_break_observed"
    assert bool(row["included_in_primary_metrics"])
    assert bool(row["excluded_in_review_candidate_sensitivity"])
    assert row["review_disposition"] == (
        "unresolved_review_candidate_retained_in_primary_not_classified_as_anomaly"
    )


def test_generated_forward_confirmation_artifact_passes() -> None:
    assert validate() == []
