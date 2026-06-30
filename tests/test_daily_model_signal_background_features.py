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
    load_price_history,
    load_tdcc_history,
    price_background_features,
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


def test_build_feature_panel_accepts_empty_signal_override() -> None:
    assert build_feature_panel(pd.DataFrame()).empty
