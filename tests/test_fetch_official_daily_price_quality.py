from __future__ import annotations

from pathlib import Path

import pandas as pd

import fetch_official_daily_price as fetcher


def _write_daily_price(path: Path, date_text: str, base_price: float, rows: int = 350) -> None:
    records = []
    for index in range(rows):
        stock_id = f"{1000 + index}"
        records.append(
            {
                "date": date_text,
                "stock_id": stock_id,
                "stock_name": f"Stock{stock_id}",
                "market": "TWSE",
                "open": base_price + index / 1000,
                "high": base_price + 1 + index / 1000,
                "low": base_price - 1 + index / 1000,
                "close": base_price + 0.5 + index / 1000,
                "volume": 1_000_000 + index,
                "trading_value": 10_000_000 + index,
                "source": "TEST",
            }
        )
    pd.DataFrame(records).to_csv(path, index=False)


def test_latest_existing_daily_file_skips_stale_duplicate_candidate(tmp_path, monkeypatch):
    monkeypatch.setattr(fetcher, "DATA_DIR", tmp_path)

    _write_daily_price(tmp_path / "daily_price_20260602.csv", "20260602", 10)
    _write_daily_price(tmp_path / "daily_price_20260603.csv", "20260603", 20)
    _write_daily_price(tmp_path / "daily_price_20260604.csv", "20260604", 10)

    log: list[str] = []
    selected = fetcher.get_latest_existing_daily_file(before_date="20260605", log=log)

    assert selected is not None
    assert selected.name == "daily_price_20260603.csv"
    assert any("rejected daily_price_20260604.csv" in item for item in log)


def test_latest_existing_daily_file_prefers_canonical_daily_price_name(tmp_path, monkeypatch):
    monkeypatch.setattr(fetcher, "DATA_DIR", tmp_path)

    _write_daily_price(tmp_path / "20260604.csv", "20260604", 10)
    _write_daily_price(tmp_path / "daily_price_20260604.csv", "20260604", 11)

    selected = fetcher.get_latest_existing_daily_file(before_date="20260605")

    assert selected is not None
    assert selected.name == "daily_price_20260604.csv"
