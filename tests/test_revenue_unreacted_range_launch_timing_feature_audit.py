from __future__ import annotations

import sys
from pathlib import Path

import pandas as pd
import pytest


ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))

from revenue_unreacted_range_launch_timing_feature_audit import (  # noqa: E402
    ALL_LINEAGE_COLUMNS,
    DETAIL_CSV,
    FEATURE_CSV,
    FULL_OBSERVATION_NON_OVERLAP_DAYS,
    LAG_INHERITED_LINEAGE_COLUMNS,
    LATEST_CSV,
    PRIMARY_ANALYSIS_BASIS,
    PRIMARY_OUTCOME_ID,
    PRIMARY_TRIGGER_ID,
    SOURCE_LAG_DETAIL_LINEAGE_COLUMNS,
    SOURCE_SNAPSHOT_CUTOFF_DATE,
    SENSITIVITY_ANALYSIS_BASIS,
    EXPECTED_SOURCE_ARTIFACT_ID,
    EXPECTED_SOURCE_ARTIFACT_VERSION,
    _assert_source_detail_lineage,
    _path_rows,
    _prepare_daily_rows,
    _source_cohort,
    build_launch_timing_feature_audit,
)
from validate_revenue_unreacted_range_launch_timing_feature_audit import validate  # noqa: E402
import validate_revenue_unreacted_range_launch_timing_feature_audit as launch_validator  # noqa: E402
import revenue_unreacted_range_launch_timing_feature_audit as launch_audit  # noqa: E402
from revenue_unreacted_range_source_snapshot_projection import (  # noqa: E402
    V1_PROJECTION_VERSION,
    V2_PROJECTION_VERSION,
)


VALID_SOURCE_LINEAGE = {
    column: (
        SOURCE_SNAPSHOT_CUTOFF_DATE
        if column == "source_projection_cutoff_date"
        else "1"
        if column.endswith("_row_count")
        else f"{(index + 1) % 16:x}" * 64
        if column.endswith("sha256")
        else f"lineage_{index}"
    )
    for index, column in enumerate(LAG_INHERITED_LINEAGE_COLUMNS)
}
VALID_SOURCE_LINEAGE["source_projection_version"] = V1_PROJECTION_VERSION


def test_launch_artifact_and_source_versions_are_projection_bound() -> None:
    assert launch_audit.artifact_version_for_projection(V1_PROJECTION_VERSION) == (
        launch_audit.V1_ARTIFACT_VERSION
    )
    assert launch_audit.artifact_version_for_projection(V2_PROJECTION_VERSION) == (
        launch_audit.V2_ARTIFACT_VERSION
    )
    source = _source_lineage_frame()
    source.loc[:, "source_projection_version"] = V2_PROJECTION_VERSION
    source.loc[:, "artifact_version"] = (
        launch_audit.SOURCE_ARTIFACT_VERSION_BY_PROJECTION[V2_PROJECTION_VERSION]
    )
    lineage = _assert_source_detail_lineage(source)
    assert lineage["source_projection_version"] == V2_PROJECTION_VERSION
    with pytest.raises(RuntimeError, match="unsupported canonical source projection"):
        launch_audit.artifact_version_for_projection("unknown")


def _synthetic_prepared() -> pd.DataFrame:
    dates = pd.bdate_range(end=SOURCE_SNAPSHOT_CUTOFF_DATE, periods=180).strftime(
        "%Y%m%d"
    )
    row_count = len(dates)
    closes = [100.0] * 25 + [110.0] + [133.0] * (row_count - 26)
    return pd.DataFrame(
        {
            "stock_id": ["1111"] * row_count,
            "stock_name": ["synthetic"] * row_count,
            "_revenue_signal_date": dates,
            "close": closes,
            "ma20": [100.0] * row_count,
            "ma60": [100.0] * row_count,
            "ema23": [100.0] * row_count,
            "return_5d_pct": [0.0] * row_count,
            "return_20d_pct": [0.0] * row_count,
            "volume_ratio_prev20": [1.0] * row_count,
            "macd_hist": [0.0] * row_count,
            "rsi14": [50.0] * row_count,
            "k_value": [50.0] * row_count,
            "d_value": [50.0] * row_count,
            "bb_width_pct": [10.0] * row_count,
            "ema23_slope_5d_pct": [0.0] * row_count,
            "distance_to_ema23_pct": [0.0] * row_count,
            "obv_slope_5d": [0.0] * row_count,
            "range_width_20d_pct": [10.0] * row_count,
            "range_width_60d_pct": [20.0] * row_count,
            "close_position_120d_pct": [50.0] * row_count,
            "tdcc_history_available": [False] * row_count,
            "tdcc_consecutive_up_weeks": [0.0] * row_count,
            "high_thresholds_up": [False] * row_count,
            "all_thresholds_up": [False] * row_count,
            "four_thresholds_sync_up": [False] * row_count,
            "full_monthly_revenue_context_ready": [True] * row_count,
            "full_monthly_revenue_latest_yoy_pct": [30.0] * row_count,
            "full_monthly_revenue_cumulative_yoy_pct": [30.0] * row_count,
            "full_monthly_revenue_latest_yoy_delta_1m_pct_points": [0.0]
            * row_count,
            "bullish_attack_candle": [False] * row_count,
            "solid_red_candle": [False] * row_count,
            "signal_market_regime": ["bull"] * row_count,
            "obv_above_ma20": [False] * row_count,
        }
    )


def _future_prepared_row(prepared: pd.DataFrame) -> pd.DataFrame:
    future = prepared.iloc[[-1]].copy()
    future.loc[:, "_revenue_signal_date"] = "20260714"
    future.loc[:, "close"] = 999.0
    return future


def _source_lineage_frame(prepared: pd.DataFrame | None = None) -> pd.DataFrame:
    dates = (
        _synthetic_prepared()["_revenue_signal_date"].astype(str).tolist()
        if prepared is None
        else prepared["_revenue_signal_date"].astype(str).tolist()
    )
    return pd.DataFrame(
        [
            {
                "artifact_id": EXPECTED_SOURCE_ARTIFACT_ID,
                "artifact_version": EXPECTED_SOURCE_ARTIFACT_VERSION,
                **VALID_SOURCE_LINEAGE,
                "episode_key": "1111|synthetic",
                "stock_id": "1111",
                "stock_name": "synthetic",
                "source_monthly_revenue_period": "202510",
                "source_monthly_revenue_source_table_date": dates[0],
                "signal_date": dates[8],
                "confirmation_date": dates[9],
                "entry_date": dates[10],
                "exit_date": dates[30],
                "strict_30_20_streak_months": 3,
                "source_to_signal_trading_days": 8,
                "current_revenue_lag_bucket": "lag_d8_14",
                "flag_strict30_20_consecutive_ge3": True,
                "source_revenue_or_price_anomaly_candidate_flag": False,
                "abs_ge80_anomaly_candidate_flag": False,
            }
        ]
    )


def _assert_semantic_frame_equal(left: pd.DataFrame, right: pd.DataFrame) -> None:
    pd.testing.assert_frame_equal(
        left.drop(columns="generated_at").reset_index(drop=True),
        right.drop(columns="generated_at").reset_index(drop=True),
        check_dtype=False,
    )


def test_revenue_launch_timing_feature_audit_passes() -> None:
    assert validate() == []


@pytest.mark.parametrize(
    ("column", "value", "message"),
    (
        ("artifact_id", "wrong_lag_artifact", "artifact id drift"),
        ("artifact_version", "stale_lag_v3", "artifact version drift"),
    ),
)
def test_launch_source_lineage_rejects_mutated_or_stale_artifact(
    column: str,
    value: str,
    message: str,
) -> None:
    source = _source_lineage_frame()
    source.loc[0, column] = value

    with pytest.raises(RuntimeError, match=message):
        _assert_source_detail_lineage(source)
    assert any(message in error for error in launch_validator._source_lineage_errors(source))


@pytest.mark.parametrize(
    "column",
    tuple(
        column
        for column in LAG_INHERITED_LINEAGE_COLUMNS
        if column != "source_projection_cutoff_date"
    ),
)
def test_launch_source_lineage_rejects_nonconstant_inherited_lineage(
    column: str,
) -> None:
    source = pd.concat([_source_lineage_frame(), _source_lineage_frame()], ignore_index=True)
    source.loc[1, column] = "not-a-sha"

    with pytest.raises(RuntimeError, match="not constant"):
        _assert_source_detail_lineage(source)
    assert any(
        "not constant" in error
        for error in launch_validator._source_lineage_errors(source)
    )


@pytest.mark.parametrize("column", LAG_INHERITED_LINEAGE_COLUMNS)
def test_launch_validator_rejects_stale_constant_inherited_lineage(column: str) -> None:
    source = _source_lineage_frame()
    expected = dict(VALID_SOURCE_LINEAGE)
    expected[column] = (
        "d" * 64
        if column.endswith("sha256")
        else "20260712"
        if column == "source_projection_cutoff_date"
        else "mutated_lineage"
    )

    errors = launch_validator._source_lineage_errors(
        source,
        expected_runtime_lineage=expected,
    )
    assert errors == [f"launch timing source current input lineage drift: {column}"]


def test_launch_source_projection_cutoff_mutation_fails_closed() -> None:
    source = _source_lineage_frame()
    source.loc[0, "source_projection_cutoff_date"] = "20260714"

    with pytest.raises(RuntimeError, match="source projection cutoff drift"):
        _assert_source_detail_lineage(source)


@pytest.mark.parametrize(
    "column",
    (
        "source_monthly_revenue_source_table_date",
        "signal_date",
        "confirmation_date",
        "entry_date",
        "exit_date",
    ),
)
def test_launch_source_lineage_rejects_invalid_cutoff_dates(column: str) -> None:
    source = _source_lineage_frame()
    source.loc[0, column] = "invalid"

    with pytest.raises(RuntimeError, match=f"{column} contains invalid dates"):
        _assert_source_detail_lineage(source)


def test_post_cutoff_prepared_row_does_not_change_daily_or_build_outputs() -> None:
    prepared = _synthetic_prepared()
    extended = pd.concat(
        [prepared, _future_prepared_row(prepared)],
        ignore_index=True,
    )
    source = _source_lineage_frame(prepared)

    baseline_daily, baseline_by_stock = _prepare_daily_rows(prepared)
    extended_daily, extended_by_stock = _prepare_daily_rows(extended)
    pd.testing.assert_frame_equal(baseline_daily, extended_daily)
    assert set(baseline_by_stock) == set(extended_by_stock)
    for stock_id in baseline_by_stock:
        pd.testing.assert_frame_equal(
            baseline_by_stock[stock_id],
            extended_by_stock[stock_id],
        )

    baseline_outputs = build_launch_timing_feature_audit(prepared, source)
    extended_outputs = build_launch_timing_feature_audit(extended, source)
    for baseline, candidate in zip(baseline_outputs, extended_outputs):
        _assert_semantic_frame_equal(baseline, candidate)


def test_pre_cutoff_duplicate_fails_and_post_cutoff_duplicates_are_ignored() -> None:
    prepared = _synthetic_prepared()
    pre_cutoff_duplicate = prepared.iloc[[10]].copy()
    with pytest.raises(RuntimeError, match="duplicate stock dates"):
        _prepare_daily_rows(
            pd.concat([prepared, pre_cutoff_duplicate], ignore_index=True)
        )

    future = _future_prepared_row(prepared)
    candidate = pd.concat([prepared, future, future], ignore_index=True)
    baseline_daily, _baseline_by_stock = _prepare_daily_rows(prepared)
    candidate_daily, _candidate_by_stock = _prepare_daily_rows(candidate)
    pd.testing.assert_frame_equal(baseline_daily, candidate_daily)


def test_post_cutoff_price_resolution_is_not_applied(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    resolution_path = tmp_path / "future_price_resolution.csv"
    pd.DataFrame(
        [
            {
                "resolution_id": "1111_future_resolution",
                "model_id": "revenue_unreacted_range",
                "stock_id": "1111",
                "event_type": "capital_reduction",
                "pre_event_last_trade_date": "20260710",
                "suspension_start_date": "20260711",
                "suspension_end_date": "20260713",
                "resume_date": "20260714",
                "exchange_ratio": "0.5",
                "pre_event_close": "10",
                "resume_reference_price": "20",
                "authority": "TWSE",
                "authority_source_url": "https://www.twse.com.tw/future-test",
                "root_cause_status": "verified_non_comparable_raw_price_scale",
                "adjustment_basis": "official_exchange_ratio",
                "approved_scope": (
                    "revenue_unreacted_range_model_owned_research_only"
                ),
            }
        ]
    ).to_csv(resolution_path, index=False)
    monkeypatch.setattr(
        launch_audit,
        "PRICE_COMPARABILITY_RESOLUTION_CSV",
        resolution_path,
    )

    _daily, grouped = _prepare_daily_rows(_synthetic_prepared())
    stock = grouped["1111"]
    assert stock["analysis_price_adjustment_factor"].eq(1.0).all()
    assert stock["analysis_close"].equals(stock["raw_close"])
    assert stock["price_comparability_resolution_ids_on_resume_date"].eq("").all()


def test_source_lag_row_count_and_sha_bind_every_build_output() -> None:
    prepared = _synthetic_prepared()
    source = _source_lineage_frame(prepared)
    expected = _assert_source_detail_lineage(source)
    outputs = build_launch_timing_feature_audit(prepared, source)

    assert set(SOURCE_LAG_DETAIL_LINEAGE_COLUMNS) <= set(ALL_LINEAGE_COLUMNS)
    for frame in outputs:
        for column in SOURCE_LAG_DETAIL_LINEAGE_COLUMNS:
            assert set(frame[column].astype(str)) == {str(expected[column])}

    second = source.copy()
    second.loc[0, "episode_key"] = "2222|synthetic"
    second.loc[0, "stock_id"] = "2222"
    mutated_source = pd.concat([source, second], ignore_index=True)
    mutated = _assert_source_detail_lineage(mutated_source)
    assert mutated["source_lag_detail_row_count"] == 2
    assert (
        mutated["source_lag_detail_semantic_sha256"]
        != expected["source_lag_detail_semantic_sha256"]
    )
    for frame in outputs:
        assert set(frame["source_lag_detail_row_count"].astype(str)) != {
            str(mutated["source_lag_detail_row_count"])
        }
        assert set(frame["source_lag_detail_semantic_sha256"].astype(str)) != {
            str(mutated["source_lag_detail_semantic_sha256"])
        }


def test_user_no_fallback_definition_is_stricter_than_month_end_and_retain10() -> None:
    closes = [100.0] + [105.0, 108.0, 112.0, 116.0, 121.0, 112.0] + [121.0] * 14
    stock = pd.DataFrame(
        {
            "feature_date": [f"202501{day:02d}" for day in range(1, 22)],
            "close": closes,
            "close_breakout_prev20": [False] * 21,
            "close_breakout_prev40": [False] * 21,
            "close_breakout_prev60": [False] * 21,
        }
    )
    row = _path_rows(stock, 0, 0).iloc[0]
    assert bool(row["d20_close_ge20"])
    assert bool(row["hit20_by15_retain10_to_d20"])
    assert not bool(row[PRIMARY_OUTCOME_ID])


def test_primary_source_retains_candidates_and_sensitivity_is_explicitly_smaller() -> None:
    source = pd.DataFrame(
        [
            {
                "episode_key": "a",
                "stock_id": "0001",
                "stock_name": "A",
                "source_monthly_revenue_period": "202501",
                "source_monthly_revenue_source_table_date": "20250217",
                "signal_date": "20250228",
                "strict_30_20_streak_months": 3,
                "source_to_signal_trading_days": 8,
                "current_revenue_lag_bucket": "lag_d8_14",
                "flag_strict30_20_consecutive_ge3": True,
                "source_revenue_or_price_anomaly_candidate_flag": False,
                "abs_ge80_anomaly_candidate_flag": False,
            },
            {
                "episode_key": "b",
                "stock_id": "0002",
                "stock_name": "B",
                "source_monthly_revenue_period": "202501",
                "source_monthly_revenue_source_table_date": "20250217",
                "signal_date": "20250228",
                "strict_30_20_streak_months": 4,
                "source_to_signal_trading_days": 8,
                "current_revenue_lag_bucket": "lag_d8_14",
                "flag_strict30_20_consecutive_ge3": True,
                "source_revenue_or_price_anomaly_candidate_flag": True,
                "abs_ge80_anomaly_candidate_flag": False,
            },
        ]
    )
    assert len(_source_cohort(source, PRIMARY_ANALYSIS_BASIS)) == 2
    assert len(_source_cohort(source, SENSITIVITY_ANALYSIS_BASIS)) == 1


def test_current_artifact_has_no_same_stock_full_observation_overlap() -> None:
    detail = pd.read_csv(DETAIL_CSV, dtype={"stock_id": str}, keep_default_na=False, low_memory=False)
    canonical = detail.loc[
        detail["trigger_id"].eq(PRIMARY_TRIGGER_ID)
        & detail["outcome_definition_id"].eq(PRIMARY_OUTCOME_ID)
        & detail["observation_selection_status"].eq("accepted")
    ]
    for (_basis, _stock_id), rows in canonical.groupby(["analysis_basis", "stock_id"], sort=False):
        positions = pd.to_numeric(rows["source_stock_sequence_index"], errors="coerce").dropna().sort_values()
        assert not positions.diff().dropna().le(FULL_OBSERVATION_NON_OVERLAP_DAYS).any()


def test_current_artifact_observation_dates_do_not_exceed_source_snapshot_cutoff() -> None:
    detail = pd.read_csv(
        DETAIL_CSV,
        dtype={"stock_id": str},
        keep_default_na=False,
        low_memory=False,
    )
    assert set(detail["observation_cutoff_date"].astype(str)) == {
        SOURCE_SNAPSHOT_CUTOFF_DATE
    }
    accepted_last_trade_dates = detail.loc[
        detail["observation_selection_status"].eq("accepted"),
        "observation_last_trade_date",
    ].astype(str)
    assert accepted_last_trade_dates.ne("").all()
    assert accepted_last_trade_dates.le(SOURCE_SNAPSHOT_CUTOFF_DATE).all()
    for column in (
        "source_monthly_revenue_source_table_date",
        "source_trade_date",
        "signal_date",
        "first_trigger_date",
        "launch_date",
    ):
        values = detail[column].astype(str)
        assert values.loc[values.ne("")].le(SOURCE_SNAPSHOT_CUTOFF_DATE).all()


def test_current_artifact_keeps_right_censor_and_feature_failure_comparison_visible() -> None:
    summary = pd.read_csv(LATEST_CSV, keep_default_na=False, low_memory=False)
    feature = pd.read_csv(FEATURE_CSV, keep_default_na=False, low_memory=False)
    assert pd.to_numeric(summary["right_censored_count"], errors="coerce").gt(0).any()
    assert set(feature["feature_time_basis"]) == {
        "source_signal_date",
        "retrospective_breakout_anchor",
        "pre_breakout_week_change",
    }
    assert pd.to_numeric(feature["launch_group_count"], errors="coerce").gt(0).all()
    assert pd.to_numeric(feature["no_launch_group_count"], errors="coerce").gt(0).all()
    binary = feature.loc[feature["feature_kind"].eq("binary")]
    hit_count = pd.to_numeric(binary["feature_hit_sample_count"], errors="coerce")
    hit_rate = pd.to_numeric(binary["launch_rate_when_feature_hit_pct"], errors="coerce")
    assert hit_count.notna().all()
    assert hit_rate.loc[hit_count.gt(0)].notna().all()


def test_3593_capital_reduction_uses_comparable_price_scale() -> None:
    prepared = pd.DataFrame(
        {
            "stock_id": ["3593"] * 62,
            "stock_name": ["力銘"] * 62,
            "_revenue_signal_date": [f"2025{month:02d}{day:02d}" for month, day in (
                [(9, day) for day in range(1, 31)]
                + [(10, day) for day in range(1, 32)]
                + [(12, 22)]
            )],
            "close": [8.1] * 61 + [12.3],
            "ma20": [8.1] * 62,
            "ma60": [8.1] * 62,
            "ema23": [8.1] * 62,
            "return_5d_pct": [0.0] * 62,
            "return_20d_pct": [0.0] * 62,
            "volume_ratio_prev20": [1.0] * 62,
            "macd_hist": [0.0] * 62,
            "rsi14": [50.0] * 62,
            "k_value": [50.0] * 62,
            "d_value": [50.0] * 62,
            "bb_width_pct": [10.0] * 62,
            "ema23_slope_5d_pct": [0.0] * 62,
            "distance_to_ema23_pct": [0.0] * 62,
            "obv_slope_5d": [0.0] * 62,
            "range_width_20d_pct": [10.0] * 62,
            "range_width_60d_pct": [20.0] * 62,
            "close_position_120d_pct": [50.0] * 62,
            "tdcc_history_available": [False] * 62,
            "tdcc_consecutive_up_weeks": [0.0] * 62,
            "high_thresholds_up": [False] * 62,
            "all_thresholds_up": [False] * 62,
            "four_thresholds_sync_up": [False] * 62,
            "full_monthly_revenue_context_ready": [True] * 62,
            "full_monthly_revenue_latest_yoy_pct": [30.0] * 62,
            "full_monthly_revenue_cumulative_yoy_pct": [30.0] * 62,
            "full_monthly_revenue_latest_yoy_delta_1m_pct_points": [0.0] * 62,
            "bullish_attack_candle": [False] * 62,
            "solid_red_candle": [False] * 62,
            "signal_market_regime": ["bull"] * 62,
            "obv_above_ma20": [False] * 62,
        }
    )
    _daily, grouped = _prepare_daily_rows(prepared)
    stock = grouped["3593"]
    before = stock.loc[stock["feature_date"].eq("20251031")].iloc[0]
    resumed = stock.loc[stock["feature_date"].eq("20251222")].iloc[0]
    assert before["raw_close"] == 8.1
    assert before["close"] == 8.1
    assert before["analysis_close"] == 13.5
    assert resumed["raw_close"] == 12.3
    assert resumed["close"] == 12.3
    assert resumed["analysis_close"] == 12.3
    assert not bool(resumed["close_breakout_prev20"])
