from __future__ import annotations

import pandas as pd

from scripts import build_warrant_market_report as warrant_report


def patch_warrant_report_paths(tmp_path, monkeypatch):
    data_daily_dir = tmp_path / "data" / "warrant_daily"
    data_flow_dir = tmp_path / "data" / "warrant_flow_by_stock"
    latest_dir = tmp_path / "output" / "latest"

    for path in (data_daily_dir, data_flow_dir, latest_dir):
        path.mkdir(parents=True, exist_ok=True)

    monkeypatch.setattr(warrant_report, "DATA_WARRANT_DAILY", data_daily_dir)
    monkeypatch.setattr(warrant_report, "DATA_WARRANT_FLOW", data_flow_dir)
    monkeypatch.setattr(warrant_report, "RAW_LATEST", latest_dir / "warrant_daily_raw_latest.csv")
    monkeypatch.setattr(warrant_report, "FLOW_LATEST", latest_dir / "warrant_flow_latest.csv")
    monkeypatch.setattr(warrant_report, "ALL_CANDIDATES", latest_dir / "all_candidates_latest.csv")
    monkeypatch.setattr(warrant_report, "REPORT_MD", latest_dir / "warrant_market_report_latest.md")
    monkeypatch.setattr(warrant_report, "REPORT_PDF", latest_dir / "warrant_market_report_latest.pdf")
    monkeypatch.setattr(warrant_report, "FLOW_BY_STOCK_LATEST", latest_dir / "warrant_flow_by_stock_latest.csv")
    monkeypatch.setattr(warrant_report, "SECTOR_HEAT_LATEST", latest_dir / "warrant_sector_heat_latest.csv")
    monkeypatch.setattr(warrant_report, "PERFORMANCE_MD", latest_dir / "warrant_signal_performance_latest.md")
    return data_daily_dir, data_flow_dir, latest_dir


def test_stock_flow_fallback_prefers_existing_same_date_stock_rows(tmp_path, monkeypatch):
    _, data_flow_dir, _ = patch_warrant_report_paths(tmp_path, monkeypatch)
    pd.DataFrame(
        [
            {
                "date": "20260611",
                "stock_id": "2330",
                "stock_name": "TSMC",
                "call_turnover": "1000",
                "put_turnover": "100",
            }
        ]
    ).to_csv(data_flow_dir / "20260611.csv", index=False, encoding="utf-8")

    path, fallback = warrant_report.find_existing_stock_flow_fallback("20260611")

    assert path == data_flow_dir / "20260611.csv"
    assert len(fallback) == 1
    assert fallback.loc[0, "stock_id"] == "2330"


def test_stock_flow_fallback_rejects_observe_only_rows(tmp_path, monkeypatch):
    _, _, latest_dir = patch_warrant_report_paths(tmp_path, monkeypatch)
    pd.DataFrame(
        [
            {
                "date": "20260611",
                "stock_id": "",
                "data_quality_note": "observe-only",
            }
        ]
    ).to_csv(latest_dir / "warrant_flow_by_stock_latest.csv", index=False, encoding="utf-8")

    path, fallback = warrant_report.find_existing_stock_flow_fallback("20260611")

    assert path is None
    assert fallback.empty


def test_market_report_preserves_current_stock_flow_when_raw_latest_is_stale(tmp_path, monkeypatch):
    data_daily_dir, data_flow_dir, latest_dir = patch_warrant_report_paths(tmp_path, monkeypatch)
    monkeypatch.setattr(warrant_report, "latest_price_date", lambda: "20260612")
    monkeypatch.setattr(warrant_report, "write_pdf", lambda *_args, **_kwargs: None)

    pd.DataFrame(
        [
            {
                "date": "20260608",
                "stock_id": "2330",
                "stock_name": "TSMC",
                "warrant_id": "2330C1",
                "call_put": "call",
                "turnover": "999",
                "volume": "100",
            }
        ]
    ).to_csv(latest_dir / "warrant_daily_raw_latest.csv", index=False, encoding="utf-8")

    pd.DataFrame(
        [
            {
                "date": "20260612",
                "stock_id": "2330",
                "stock_name": "TSMC",
                "call_turnover": "1000",
                "put_turnover": "100",
                "call_volume": "10",
                "put_volume": "1",
                "warrant_flow_signal": "call_inflow",
            }
        ]
    ).to_csv(latest_dir / "warrant_flow_latest.csv", index=False, encoding="utf-8")

    assert warrant_report.main() == 0

    latest = pd.read_csv(latest_dir / "warrant_flow_by_stock_latest.csv", dtype=str)
    archived_flow = pd.read_csv(data_flow_dir / "20260612.csv", dtype=str)

    assert set(latest["date"]) == {"20260612"}
    assert set(archived_flow["date"]) == {"20260612"}
    assert latest.loc[0, "stock_id"] == "2330"
    assert not (data_flow_dir / "20260608.csv").exists()
    assert (data_daily_dir / "20260608.csv").exists()
    assert not (data_daily_dir / "20260612.csv").exists()


def test_market_report_falls_back_to_current_by_stock_when_raw_and_flow_are_stale(tmp_path, monkeypatch):
    _, data_flow_dir, latest_dir = patch_warrant_report_paths(tmp_path, monkeypatch)
    monkeypatch.setattr(warrant_report, "latest_price_date", lambda: "20260612")
    monkeypatch.setattr(warrant_report, "write_pdf", lambda *_args, **_kwargs: None)

    pd.DataFrame(
        [
            {
                "date": "20260608",
                "stock_id": "2330",
                "stock_name": "TSMC",
                "warrant_id": "2330C1",
                "call_put": "call",
                "turnover": "999",
                "volume": "100",
            }
        ]
    ).to_csv(latest_dir / "warrant_daily_raw_latest.csv", index=False, encoding="utf-8")

    pd.DataFrame(
        [
            {
                "date": "20260608",
                "stock_id": "2330",
                "stock_name": "TSMC",
                "call_turnover": "999",
                "put_turnover": "99",
                "warrant_flow_signal": "call_inflow",
            }
        ]
    ).to_csv(latest_dir / "warrant_flow_latest.csv", index=False, encoding="utf-8")

    pd.DataFrame(
        [
            {
                "date": "20260612",
                "stock_id": "2454",
                "stock_name": "MediaTek",
                "call_turnover": "2000",
                "put_turnover": "200",
                "warrant_flow_signal": "call_strong_inflow",
            }
        ]
    ).to_csv(latest_dir / "warrant_flow_by_stock_latest.csv", index=False, encoding="utf-8")

    assert warrant_report.main() == 0

    latest = pd.read_csv(latest_dir / "warrant_flow_by_stock_latest.csv", dtype=str)

    assert set(latest["date"]) == {"20260612"}
    assert latest.loc[0, "stock_id"] == "2454"
    assert (data_flow_dir / "20260612.csv").exists()
    assert not (data_flow_dir / "20260608.csv").exists()
