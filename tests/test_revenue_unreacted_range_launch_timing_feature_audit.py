from __future__ import annotations

import sys
from pathlib import Path

import pandas as pd


ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))

from revenue_unreacted_range_launch_timing_feature_audit import (  # noqa: E402
    DETAIL_CSV,
    FEATURE_CSV,
    FULL_OBSERVATION_NON_OVERLAP_DAYS,
    LATEST_CSV,
    PRIMARY_ANALYSIS_BASIS,
    PRIMARY_OUTCOME_ID,
    PRIMARY_TRIGGER_ID,
    SENSITIVITY_ANALYSIS_BASIS,
    _path_rows,
    _prepare_daily_rows,
    _source_cohort,
)
from validate_revenue_unreacted_range_launch_timing_feature_audit import validate  # noqa: E402


def test_revenue_launch_timing_feature_audit_passes() -> None:
    assert validate() == []


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
