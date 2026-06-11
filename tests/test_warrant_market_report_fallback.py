from __future__ import annotations

import pandas as pd

from scripts import build_warrant_market_report as warrant_report


def patch_warrant_report_paths(tmp_path, monkeypatch):
    data_flow_dir = tmp_path / "data" / "warrant_flow_by_stock"
    latest_dir = tmp_path / "output" / "latest"

    for path in (data_flow_dir, latest_dir):
        path.mkdir(parents=True, exist_ok=True)

    monkeypatch.setattr(warrant_report, "DATA_WARRANT_FLOW", data_flow_dir)
    monkeypatch.setattr(warrant_report, "FLOW_BY_STOCK_LATEST", latest_dir / "warrant_flow_by_stock_latest.csv")
    return data_flow_dir, latest_dir


def test_stock_flow_fallback_prefers_existing_same_date_stock_rows(tmp_path, monkeypatch):
    data_flow_dir, _ = patch_warrant_report_paths(tmp_path, monkeypatch)
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
    _, latest_dir = patch_warrant_report_paths(tmp_path, monkeypatch)
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
