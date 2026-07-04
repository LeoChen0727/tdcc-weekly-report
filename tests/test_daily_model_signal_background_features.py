from __future__ import annotations

from pathlib import Path

import pandas as pd

import sys

ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))

from build_daily_model_signal_background_features import (  # noqa: E402
    build_feature_panel,
    feature_catalog,
    load_theme_status_history,
    load_monthly_revenue_pit_panel,
    load_price_history,
    load_tdcc_history,
    price_background_features,
    revenue_background_features,
    theme_background_features,
    tdcc_background_features,
)
from validate_daily_model_signal_background_features import validate_catalog, validate_panel  # noqa: E402


def write_price(path: Path, stock_id: str, start: int = 1, days: int = 130) -> None:
    rows = []
    for i in range(days):
        day = start + i
        close = 100.0 + i
        rows.append(
            {
                "date": f"202601{day:02d}" if day <= 31 else f"202602{day - 31:02d}" if day <= 59 else f"202603{day - 59:02d}" if day <= 90 else f"202604{day - 90:02d}",
                "stock_id": stock_id,
                "stock_name": "Test",
                "market": "listed",
                "open": close - 0.5,
                "high": close + 1.0,
                "low": close - 1.0,
                "close": close,
                "volume": 1000.0 + i * 10,
            }
        )
    pd.DataFrame(rows).to_csv(path, index=False)


def test_price_background_features_are_point_in_time(tmp_path: Path) -> None:
    price_dir = tmp_path / "prices"
    price_dir.mkdir()
    write_price(price_dir / "2330.csv", "2330", days=95)
    load_price_history.cache_clear()

    features = price_background_features("2330", "20260320", price_dir=price_dir)

    assert features["feature_as_of_date"] == "20260320"
    assert features["price_history_max_date"] > "20260320"
    assert features["future_price_rows_ignored"] > 0
    assert features["point_in_time_status"] == "exact_signal_date"
    assert features["pre45_sessions"] == 45
    assert features["pre45_return_pct"] != ""
    assert features["pre45_range_width_pct"] != ""
    assert features["macd_hist"] != ""
    assert features["rsi14"] != ""


def test_tdcc_background_features_use_asof_rows_only(tmp_path: Path) -> None:
    tdcc_dir = tmp_path / "tdcc"
    tdcc_dir.mkdir()
    pd.DataFrame(
        [
            {
                "as_of_date": "20260313",
                "stock_id": "2330",
                "tdcc_consecutive_up_weeks": 1,
                "over_400_ratio": 40.0,
                "over_400_change_1w": 0.2,
                "over_1000_ratio": 30.0,
                "over_1000_change_1w": 0.1,
                "over_1000_change_3w": 0.3,
            },
            {
                "as_of_date": "20260327",
                "stock_id": "2330",
                "tdcc_consecutive_up_weeks": 2,
                "over_400_ratio": 50.0,
                "over_400_change_1w": 5.0,
                "over_1000_ratio": 35.0,
                "over_1000_change_1w": 4.0,
                "over_1000_change_3w": 6.0,
            },
        ]
    ).to_csv(tdcc_dir / "2330.csv", index=False)
    load_tdcc_history.cache_clear()

    features = tdcc_background_features("2330", "20260320", tdcc_dir=tdcc_dir)

    assert features["tdcc_as_of_date"] == "20260313"
    assert features["tdcc_future_rows_ignored"] == 1
    assert features["tdcc_over_400_change_1w"] == 0.2
    assert features["tdcc_over_1000_change_1w"] == 0.1


def test_theme_background_features_use_signal_date_asof_history(tmp_path: Path) -> None:
    theme_path = tmp_path / "daily_theme_status_history.csv"
    pd.DataFrame(
        [
            {
                "signal_date": "20260313",
                "stock_id": "2330",
                "theme_name": "AI",
                "theme_final_status": "mainstream_follow_through",
                "theme_status_group": "mainstream_supported",
                "candidate_source_type": "mainstream_theme_candidate",
                "candidate_line_group": "breakout_attack_stock",
                "candidate_line": "帶量突破",
                "two_line_overlap_flag": "true",
                "presentation_priority": "2",
                "tdcc_status": "up",
                "warrant_flow_signal": "neutral",
                "volume_ratio": "1.8",
                "return_20d": "12.5",
                "repeat_appear_label": "first_seen",
                "volume_breakout_type": "confirmed",
                "volume_attack_bucket": "selected",
                "theme_volume_attack_status": "selected",
                "is_volume_attack_selected": "true",
                "is_volume_attack_watch": "false",
                "is_volume_attack_failed": "false",
            },
            {
                "signal_date": "20260327",
                "stock_id": "2330",
                "theme_name": "AI",
                "theme_final_status": "mainstream_overheated",
                "theme_status_group": "mainstream_overheated",
                "candidate_source_type": "risk_downgraded_candidate",
                "candidate_line_group": "risk",
                "candidate_line": "風險",
                "two_line_overlap_flag": "false",
                "presentation_priority": "9",
                "tdcc_status": "down",
                "warrant_flow_signal": "negative",
                "volume_ratio": "3.5",
                "return_20d": "42.0",
                "repeat_appear_label": "continued_overheated",
                "volume_breakout_type": "overheated",
                "volume_attack_bucket": "failed",
                "theme_volume_attack_status": "failed",
                "is_volume_attack_selected": "false",
                "is_volume_attack_watch": "false",
                "is_volume_attack_failed": "true",
            },
        ]
    ).to_csv(theme_path, index=False)

    history = load_theme_status_history((theme_path,))
    features = theme_background_features("2330", "20260320", history)

    assert features["theme_context_as_of_date"] == "20260313"
    assert features["theme_context_future_rows_ignored"] == 1
    assert features["theme_context_data_status"] == "ready_previous_signal_date"
    assert features["theme_context_status_group"] == "mainstream_supported"
    assert features["theme_context_volume_ratio"] == 1.8
    assert features["theme_context_volume_attack_selected"] is True
    assert str(theme_path.name) in features["theme_context_source_artifact"]


def test_revenue_background_features_use_snapshot_observed_asof_rows(tmp_path: Path) -> None:
    panel_path = tmp_path / "monthly_revenue_point_in_time_panel_latest.csv"
    pd.DataFrame(
        [
            {
                "stock_id": "2330",
                "observed_as_of_date": "20260313",
                "revenue_period": "202602",
                "latest_revenue_yoy_pct": "10.5",
                "cumulative_revenue_yoy_pct": "8.0",
                "revenue_positive_flag": "True",
                "revenue_strong_flag": "False",
                "revenue_good_eps_unconfirmed_flag": "False",
                "revenue_numerical_anomaly_flag": "False",
                "research_join_allowed": "True",
                "allowed_for_formal_historical_model_use": "False",
                "source_snapshot_files": "output/history/daily_model_snapshots/all_candidates_20260313.csv",
            },
            {
                "stock_id": "2330",
                "observed_as_of_date": "20260327",
                "revenue_period": "202603",
                "latest_revenue_yoy_pct": "99.0",
                "cumulative_revenue_yoy_pct": "88.0",
                "revenue_positive_flag": "True",
                "revenue_strong_flag": "True",
                "revenue_good_eps_unconfirmed_flag": "True",
                "revenue_numerical_anomaly_flag": "False",
                "research_join_allowed": "True",
                "allowed_for_formal_historical_model_use": "False",
                "source_snapshot_files": "future.csv",
            },
        ]
    ).to_csv(panel_path, index=False)
    load_monthly_revenue_pit_panel.cache_clear()
    panel = load_monthly_revenue_pit_panel(str(panel_path))

    features = revenue_background_features("2330", "20260320", panel)

    assert features["monthly_revenue_context_as_of_date"] == "20260313"
    assert features["monthly_revenue_future_rows_ignored"] == 1
    assert features["monthly_revenue_data_status"] == "ready_previous_snapshot_date"
    assert features["monthly_revenue_latest_yoy_pct"] == 10.5
    assert features["monthly_revenue_positive_flag"] is True
    assert features["monthly_revenue_formal_model_use_allowed"] is False


def test_background_feature_panel_stays_shared_objective(tmp_path: Path) -> None:
    price_dir = tmp_path / "prices"
    tdcc_dir = tmp_path / "tdcc"
    price_dir.mkdir()
    tdcc_dir.mkdir()
    write_price(price_dir / "2330.csv", "2330", days=95)
    pd.DataFrame(
        [
            {
                "as_of_date": "20260313",
                "stock_id": "2330",
                "tdcc_consecutive_up_weeks": 1,
                "over_400_ratio": 40.0,
                "over_400_change_1w": 0.2,
                "over_1000_ratio": 30.0,
                "over_1000_change_1w": 0.1,
                "over_1000_change_3w": 0.3,
            }
        ]
    ).to_csv(tdcc_dir / "2330.csv", index=False)
    load_price_history.cache_clear()
    load_tdcc_history.cache_clear()

    signals = pd.DataFrame(
        [
            {
                "stock_id": "2330",
                "stock_name": "Test",
                "signal_date": "20260320",
                "source_model_ids": "price_pullback_23ema;neckline_volume_breakout_confirmation",
                "source_snapshot_dates": "20260320",
                "source_snapshot_files": "synthetic.csv",
                "source_signal_rows": 2,
            }
        ]
    )

    # Patch only the low-level path constants by calling the underlying feature
    # functions through a small local frame; this keeps the panel schema under
    # validator coverage without touching production model rules.
    row = {
        "generated_at": "test",
        "feature_panel_id": "daily_model_signal_background_features_v1",
        "feature_scope": "shared_objective_point_in_time",
        "stock_id": "2330",
        "stock_name": "Test",
        "signal_date": "20260320",
        "source_model_ids": signals.iloc[0]["source_model_ids"],
        "source_snapshot_dates": "20260320",
        "source_snapshot_files": "synthetic.csv",
        "source_signal_rows": 2,
    }
    row.update(price_background_features("2330", "20260320", price_dir=price_dir))
    row.update(tdcc_background_features("2330", "20260320", tdcc_dir=tdcc_dir))
    row.update(
        {
            "monthly_revenue_context_as_of_date": "20260313",
            "monthly_revenue_rows_as_of": 1,
            "monthly_revenue_future_rows_ignored": 0,
            "monthly_revenue_data_status": "ready_previous_snapshot_date",
            "monthly_revenue_period": "202602",
            "monthly_revenue_latest_yoy_pct": 10.5,
            "monthly_revenue_cumulative_yoy_pct": 8.0,
            "monthly_revenue_positive_flag": True,
            "monthly_revenue_strong_flag": False,
            "monthly_revenue_good_eps_unconfirmed_flag": False,
            "monthly_revenue_numerical_anomaly_flag": False,
            "monthly_revenue_source_artifact": "output/history/daily_model_snapshots/all_candidates_20260313.csv",
            "monthly_revenue_formal_model_use_allowed": False,
            "theme_context_as_of_date": "20260313",
            "theme_context_rows_as_of": 1,
            "theme_context_future_rows_ignored": 0,
            "theme_context_data_status": "ready_previous_signal_date",
            "theme_context_name": "AI",
            "theme_context_final_status": "mainstream_follow_through",
            "theme_context_status_group": "mainstream_supported",
            "theme_context_source_type": "mainstream_theme_candidate",
            "theme_context_line_group": "breakout_attack_stock",
            "theme_context_line": "帶量突破",
            "theme_context_two_line_overlap": True,
            "theme_context_priority": 2,
            "theme_context_tdcc_status": "up",
            "theme_context_warrant_flow_signal": "neutral",
            "theme_context_volume_ratio": 1.8,
            "theme_context_return_20d_pct": 12.5,
            "theme_context_repeat_label": "first_seen",
            "theme_context_volume_breakout_type": "confirmed",
            "theme_context_volume_bucket": "selected",
            "theme_context_volume_attack_status": "selected",
            "theme_context_volume_attack_selected": True,
            "theme_context_volume_attack_watch": False,
            "theme_context_volume_attack_failed": False,
            "theme_context_source_artifact": "output/history/daily_signals/daily_theme_status_history.csv",
        }
    )
    row.update(
        {
            "market_index_as_of_date": "20260320",
            "twse_close": 10000,
            "twse_return_5d_pct": 1.0,
            "twse_return_20d_pct": 2.0,
            "twse_above_ma20": True,
            "twse_above_ma60": True,
            "tpex_close": 500,
            "tpex_return_5d_pct": 1.0,
            "tpex_return_20d_pct": 2.0,
            "tpex_above_ma20": True,
            "tpex_above_ma60": True,
        }
    )
    panel = pd.DataFrame([row])
    catalog = feature_catalog(panel)

    assert validate_panel(panel.astype(str)) == []
    assert validate_catalog(panel.astype(str), catalog.astype(str)) == []
    assert not any("price_pullback" in col for col in panel.columns)
    assert not any("neckline" in col for col in panel.columns)
    assert "price_pullback_23ema_operation_filter" in set(catalog["feature_column"])
    assert "neckline_45d_non_bearish_filter" in set(catalog["feature_column"])
    revenue_catalog = catalog[catalog["feature_column"].eq("monthly_revenue_point_in_time_panel")].iloc[0]
    assert revenue_catalog["feature_scope"] == "shared_objective_point_in_time"
    theme_catalog = catalog[catalog["feature_column"].eq("theme_context_status_group")].iloc[0]
    assert theme_catalog["feature_family"] == "theme_status_history"
    assert theme_catalog["allowed_use"] == "research_background_only_not_a_model_gate_or_score"


def test_build_feature_panel_accepts_empty_signal_override() -> None:
    assert build_feature_panel(pd.DataFrame()).empty
