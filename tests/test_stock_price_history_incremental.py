from __future__ import annotations

from pathlib import Path

import pandas as pd

from scripts import build_stock_price_history as history


def patch_history_paths(tmp_path: Path, monkeypatch) -> tuple[Path, Path, Path, Path]:
    daily_dir = tmp_path / "data" / "daily_price"
    stock_dir = tmp_path / "data" / "stock_price_history"
    latest_dir = tmp_path / "output" / "latest"
    docs_latest_dir = tmp_path / "docs" / "latest"
    for path in (daily_dir, stock_dir, latest_dir, docs_latest_dir):
        path.mkdir(parents=True, exist_ok=True)

    monkeypatch.setattr(history, "DATA_DAILY_PRICE_DIR", daily_dir)
    monkeypatch.setattr(history, "STOCK_HISTORY_DIR", stock_dir)
    monkeypatch.setattr(history, "LATEST_DIR", latest_dir)
    monkeypatch.setattr(history, "DOCS_LATEST_DIR", docs_latest_dir)
    monkeypatch.setattr(history, "MANIFEST_CSV", latest_dir / "stock_price_history_manifest.csv")
    monkeypatch.setattr(history, "MANIFEST_JSON", latest_dir / "stock_price_history_manifest.json")
    monkeypatch.setattr(history, "MANIFEST_MD", latest_dir / "stock_price_history_manifest.md")
    monkeypatch.setattr(history, "DOCS_MANIFEST_CSV", docs_latest_dir / "stock_price_history_manifest.csv")
    monkeypatch.setattr(history, "DOCS_MANIFEST_JSON", docs_latest_dir / "stock_price_history_manifest.json")
    monkeypatch.setattr(history, "DOCS_MANIFEST_MD", docs_latest_dir / "stock_price_history_manifest.md")
    return daily_dir, stock_dir, latest_dir, docs_latest_dir


def write_daily_price(path: Path, date: str, close: float) -> None:
    pd.DataFrame(
        [
            {
                "date": date,
                "stock_id": "2330",
                "stock_name": "TSMC",
                "market": "TWSE",
                "open": close - 5,
                "high": close + 5,
                "low": close - 10,
                "close": close,
                "volume": 1000,
                "trading_value": 1000000,
                "source": "TEST",
            }
        ]
    ).to_csv(path, index=False, encoding="utf-8")


def write_existing_history(path: Path) -> None:
    pd.DataFrame(
        [
            {
                "date": "20260605",
                "stock_id": "2330",
                "stock_name": "TSMC",
                "market": "TWSE",
                "open": 1000,
                "high": 1010,
                "low": 990,
                "close": 1005,
                "volume": 1000,
                "trading_value": 1000000,
                "source": "TEST",
                "source_file": "data/daily_price/daily_price_20260605.csv",
            }
        ]
    ).to_csv(path, index=False, encoding="utf-8")


def write_manifest_claiming_newer_history(path: Path) -> None:
    pd.DataFrame(
        [
            {
                "stock_id": "2330",
                "stock_name": "TSMC",
                "market": "TWSE",
                "rows": 2,
                "start_date": "20260605",
                "end_date": "20260611",
                "latest_close": 1050,
                "latest_volume": 1000,
                "file_path": "data/stock_price_history/2330.csv",
                "raw_url": "https://example.invalid/2330.csv",
            }
        ]
    ).to_csv(path, index=False, encoding="utf-8")


def test_incremental_latest_updates_when_manifest_is_newer_than_actual_history(tmp_path, monkeypatch):
    daily_dir, stock_dir, latest_dir, _ = patch_history_paths(tmp_path, monkeypatch)
    write_daily_price(daily_dir / "daily_price_20260611.csv", "20260611", close=1050)
    write_existing_history(stock_dir / "2330.csv")
    write_manifest_claiming_newer_history(latest_dir / "stock_price_history_manifest.csv")

    manifest = history.build_history_files_incremental_latest()

    updated = pd.read_csv(stock_dir / "2330.csv", dtype=str)

    assert updated["date"].iloc[-1] == "20260611"
    assert manifest.loc[manifest["stock_id"].astype(str).eq("2330"), "end_date"].iloc[0] == "20260611"
