from __future__ import annotations

import sys
from pathlib import Path

import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import tracking_utils as tracking  # noqa: E402
import update_market_index_history as market_update  # noqa: E402
from tracking_utils import recent_market_index_fetch_months  # noqa: E402


def test_recent_market_index_fetch_months_backfills_when_history_is_empty() -> None:
    assert recent_market_index_fetch_months("20260605", pd.DataFrame(), months=4) == [
        "20260301",
        "20260401",
        "20260501",
        "20260601",
    ]


def test_recent_market_index_fetch_months_refreshes_only_recent_months_when_current() -> None:
    old = pd.DataFrame(
        [
            {"date": "20260605", "index_code": "TWSE", "ohlc_available": True},
            {"date": "20260605", "index_code": "TPEX", "ohlc_available": True},
        ]
    )

    assert recent_market_index_fetch_months("20260605", old, months=4) == [
        "20260501",
        "20260601",
    ]


def test_recent_market_index_fetch_months_includes_missing_forward_months() -> None:
    old = pd.DataFrame(
        [
            {"date": "20260430", "index_code": "TWSE", "ohlc_available": True},
            {"date": "20260430", "index_code": "TPEX", "ohlc_available": True},
        ]
    )

    assert recent_market_index_fetch_months("20260605", old, months=4) == [
        "20260401",
        "20260501",
        "20260601",
    ]


def test_recent_market_index_fetch_months_backfills_if_required_index_missing() -> None:
    old = pd.DataFrame(
        [
            {"date": "20260605", "index_code": "TWSE", "ohlc_available": True},
        ]
    )

    assert recent_market_index_fetch_months("20260605", old, months=4) == [
        "20260301",
        "20260401",
        "20260501",
        "20260601",
    ]


def test_target_market_index_replay_preserves_future_rows_and_latest_mirror(monkeypatch, tmp_path):
    data_dir = tmp_path / "data"
    latest_dir = tmp_path / "latest"
    data_dir.mkdir()
    latest_dir.mkdir()
    market_path = data_dir / "market_index_history.csv"
    ohlc_path = data_dir / "market_index_ohlc_history.csv"
    dates = pd.date_range("2026-04-01", "2026-07-17", freq="B").strftime("%Y%m%d").tolist()
    rows = []
    for code, base in (("TWSE", 20000.0), ("TPEX", 300.0)):
        for offset, date in enumerate(dates):
            close = base + offset
            rows.append(
                {
                    "date": date,
                    "index_code": code,
                    "index_name": code,
                    "open": close - 1,
                    "high": close + 1,
                    "low": close - 2,
                    "close": close,
                    "volume": 100,
                    "turnover_value": 1000,
                    "transactions": 10,
                    "return_5d": "old",
                    "return_10d": "old",
                    "return_20d": "old",
                    "return_60d": "old",
                    "ma20": "old",
                    "ma60": "old",
                    "above_ma20": "old",
                    "above_ma60": "old",
                    "ohlc_available": True,
                    "volume_available": True,
                }
            )
        rows.append(
            {
                "date": "20260724",
                "index_code": code,
                "index_name": code,
                "open": "future-open",
                "high": "future-high",
                "low": "future-low",
                "close": "99999",
                "volume": "future-volume",
                "turnover_value": "future-turnover",
                "transactions": "future-transactions",
                "return_5d": "future-r5",
                "return_10d": "future-r10",
                "return_20d": "future-r20",
                "return_60d": "future-r60",
                "ma20": "future-ma20",
                "ma60": "future-ma60",
                "above_ma20": "future-above20",
                "above_ma60": "future-above60",
                "ohlc_available": "future-ohlc",
                "volume_available": "future-volume-available",
            }
        )
    old_market = pd.DataFrame(rows)
    old_market.to_csv(market_path, index=False)
    old_market[
        [
            "date", "index_code", "index_name", "open", "high", "low", "close",
            "volume", "turnover_value", "transactions", "ohlc_available", "volume_available",
        ]
    ].to_csv(ohlc_path, index=False)
    existing_latest = old_market[old_market["date"].eq("20260724")].copy()
    existing_latest.to_csv(latest_dir / "market_benchmark_latest.csv", index=False)

    monkeypatch.setattr(tracking, "DATA_DIR", data_dir)
    monkeypatch.setattr(tracking, "LATEST_DIR", latest_dir)
    monkeypatch.setattr(tracking, "MARKET_INDEX_PATH", market_path)
    monkeypatch.setattr(tracking, "MARKET_INDEX_OHLC_PATH", ohlc_path)
    monkeypatch.setattr(
        tracking,
        "fetch_twse_index_ohlc_month",
        lambda month: pd.DataFrame(
            [{"date": "20260720", "index_code": "TWSE", "index_name": "TAIEX", "open": 21000, "high": 21100, "low": 20900, "close": 21050, "ohlc_source": "twse"}]
        ),
    )
    monkeypatch.setattr(
        tracking,
        "fetch_tpex_index_ohlc_month",
        lambda month: pd.DataFrame(
            [{"date": "20260720", "index_code": "TPEX", "index_name": "TPEx", "open": 310, "high": 312, "low": 309, "close": 311, "ohlc_source": "tpex"}]
        ),
    )
    monkeypatch.setattr(
        tracking,
        "fetch_twse_index_turnover_month",
        lambda month: pd.DataFrame(
            [{"date": "20260720", "index_code": "TWSE", "volume": 200, "turnover_value": 2000, "transactions": 20, "turnover_source": "twse"}]
        ),
    )
    monkeypatch.setattr(
        tracking,
        "fetch_tpex_index_turnover_latest",
        lambda: (_ for _ in ()).throw(AssertionError("latest TPEx turnover must not be used")),
    )

    result = tracking.update_market_index_history(target_date="20260720")
    target_rows = result[result["date"].astype(str).eq("20260720")]
    assert set(target_rows["index_code"]) == {"TWSE", "TPEX"}
    assert target_rows["return_5d"].notna().all()
    assert result.attrs["target_calculation_context_max_date_by_index"] == {
        "TWSE": "20260720",
        "TPEX": "20260720",
    }
    after_future = result[result["date"].astype(str).eq("20260724")].set_index("index_code")
    before_future = old_market[old_market["date"].eq("20260724")].set_index("index_code")
    for col in [
        "open", "high", "low", "close", "volume", "turnover_value", "transactions",
        "return_5d", "return_10d", "return_20d", "return_60d", "ma20", "ma60",
        "above_ma20", "above_ma60", "ohlc_available", "volume_available",
    ]:
        assert after_future[col].astype(str).to_dict() == before_future[col].astype(str).to_dict()
    pd.testing.assert_frame_equal(
        pd.read_csv(latest_dir / "market_benchmark_latest.csv", dtype=str),
        existing_latest.astype(str).reset_index(drop=True),
        check_dtype=False,
    )


def test_tpex_only_base_repair_preserves_twse_rows_exactly(monkeypatch, tmp_path):
    data_dir = tmp_path / "data"
    latest_dir = tmp_path / "latest"
    data_dir.mkdir()
    latest_dir.mkdir()
    market_path = data_dir / "market_index_history.csv"
    ohlc_path = data_dir / "market_index_ohlc_history.csv"
    rows = []
    for code, base in (("TWSE", 20000), ("TPEX", 300)):
        for offset, date in enumerate(pd.date_range("2026-04-01", "2026-07-17", freq="B").strftime("%Y%m%d")):
            close = base + offset
            rows.append(
                {
                    "date": date,
                    "index_code": code,
                    "index_name": code,
                    "open": close - 1,
                    "high": close + 1,
                    "low": close - 2,
                    "close": close,
                    "volume": 100,
                    "turnover_value": 1000,
                    "transactions": 10,
                    "return_5d": "preserve",
                    "return_10d": "preserve",
                    "return_20d": "preserve",
                    "return_60d": "preserve",
                    "ma20": "preserve",
                    "ma60": "preserve",
                    "above_ma20": "preserve",
                    "above_ma60": "preserve",
                    "ohlc_available": True,
                    "volume_available": True,
                }
            )
    old_market = pd.DataFrame(rows)
    old_market.to_csv(market_path, index=False)
    old_market[
        [
            "date", "index_code", "index_name", "open", "high", "low", "close",
            "volume", "turnover_value", "transactions", "ohlc_available", "volume_available",
        ]
    ].to_csv(ohlc_path, index=False)
    before_twse = old_market[old_market["index_code"].eq("TWSE")].reset_index(drop=True)
    before_ohlc_twse = pd.read_csv(ohlc_path, dtype=str)
    before_ohlc_twse = before_ohlc_twse[before_ohlc_twse["index_code"].eq("TWSE")].reset_index(drop=True)

    monkeypatch.setattr(tracking, "DATA_DIR", data_dir)
    monkeypatch.setattr(tracking, "LATEST_DIR", latest_dir)
    monkeypatch.setattr(tracking, "MARKET_INDEX_PATH", market_path)
    monkeypatch.setattr(tracking, "MARKET_INDEX_OHLC_PATH", ohlc_path)
    monkeypatch.setattr(
        tracking,
        "fetch_twse_index_ohlc_month",
        lambda month: (_ for _ in ()).throw(AssertionError("TWSE must not be fetched")),
    )
    monkeypatch.setattr(
        tracking,
        "fetch_twse_index_turnover_month",
        lambda month: (_ for _ in ()).throw(AssertionError("TWSE turnover must not be fetched")),
    )
    monkeypatch.setattr(
        tracking,
        "fetch_tpex_index_ohlc_month",
        lambda month: pd.DataFrame(
            [{
                "date": "20260717", "index_code": "TPEX", "index_name": "TPEx",
                "open": 310, "high": 312, "low": 309, "close": 311, "ohlc_source": "tpex",
            }]
        ),
    )
    monkeypatch.setattr(
        tracking,
        "fetch_tpex_index_turnover_latest",
        lambda: (_ for _ in ()).throw(AssertionError("latest TPEx turnover must not be used")),
    )

    result = tracking.update_market_index_history(
        target_date="20260717",
        target_index_codes={"TPEX"},
    )

    assert result.attrs["target_calculation_context_max_date_by_index"] == {
        "TPEX": "20260717"
    }

    after_twse = result[result["index_code"].eq("TWSE")].reset_index(drop=True)
    pd.testing.assert_frame_equal(after_twse.astype(str), before_twse.astype(str), check_dtype=False)
    after_ohlc_twse = pd.read_csv(ohlc_path, dtype=str)
    after_ohlc_twse = after_ohlc_twse[after_ohlc_twse["index_code"].eq("TWSE")].reset_index(drop=True)
    pd.testing.assert_frame_equal(after_ohlc_twse, before_ohlc_twse, check_dtype=False)


def test_market_update_target_date_is_calendar_valid() -> None:
    try:
        market_update.parse_target_date("20260230")
    except RuntimeError as exc:
        assert "calendar-valid YYYYMMDD" in str(exc)
    else:
        raise AssertionError("invalid calendar date must fail")
