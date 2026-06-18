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


def test_tpex_json_rejects_response_date_that_does_not_match_target():
    text = (
        '{"date":"20260618","tables":[{"data":[["006201","ETF","50.25","","49.25",'
        '"50.25","48.96","50","2512"]]}]}'
    )
    log: list[str] = []

    df = fetcher.parse_tpex_json(text, "20260608", "TPEX_TEST", log)

    assert df.empty
    assert any("rejected response dates ['20260618']" in item for item in log)


def test_tpex_csv_rejects_response_date_that_does_not_match_target():
    text = '資料日期:115/06/18\n006201,ETF,50.25,,49.25,50.25,48.96,50,2512\n'
    log: list[str] = []

    df = fetcher.parse_tpex_csv(text, "20260608", "TPEX_TEST", log)

    assert df.empty
    assert any("rejected response date 20260618" in item for item in log)


def test_tpex_json_accepts_nested_table_response_date_that_matches_target():
    text = (
        '{"tables":[{"date":"115/06/09","data":[["006201","ETF","26.36","-0.09",'
        '"26.33","26.38","26.31","63,012,000","1,660,553,000"]]}]}'
    )
    log: list[str] = []

    df = fetcher.parse_tpex_json(text, "20260609", "TPEX_TEST", log)

    assert len(df) == 1
    row = df.iloc[0]
    assert row["stock_id"] == "006201"
    assert row["date"] == "20260609"
    assert float(row["volume"]) == 63012000.0


def test_tpex_fetch_skips_latest_only_openapi_for_historical_target(monkeypatch):
    monkeypatch.setattr(fetcher, "now_taipei", lambda: fetcher.datetime(2026, 6, 18, tzinfo=fetcher.TAIPEI))

    requested: list[str] = []

    def fake_request_text(url: str, log: list[str], referer: str = "https://www.twse.com.tw/") -> str:
        requested.append(url)
        if "openapi" in url:
            return '{"data":[["006201","ETF","50.25","","49.25","50.25","48.96","50","2512"]]}'
        return ""

    monkeypatch.setattr(fetcher, "request_text", fake_request_text)

    log: list[str] = []
    df = fetcher.fetch_tpex_batch("20260608", log)

    assert df.empty
    assert not any("openapi" in url for url in requested)
    assert any("latest-only" in item for item in log)


def test_apply_canonical_stock_names_overrides_corrupted_endpoint_name(tmp_path, monkeypatch):
    snapshot = tmp_path / "company_industry_snapshot_latest.csv"
    pd.DataFrame(
        [
            {
                "stock_id": "2243",
                "stock_name": "宏旭-KY",
                "industry": "汽車工業",
                "market": "TWSE",
            }
        ]
    ).to_csv(snapshot, index=False, encoding="utf-8-sig")
    monkeypatch.setattr(fetcher, "CANONICAL_STOCK_NAME_SOURCES", [snapshot])

    source = pd.DataFrame(
        [
            {
                "date": "20260610",
                "stock_id": "2243",
                "stock_name": "ЇЛІА-KY",
                "market": "TWSE",
                "open": 28.0,
                "high": 31.2,
                "low": 28.0,
                "close": 30.8,
                "volume": 2128874,
                "trading_value": 64777690,
                "source": "TWSE_RWD_JSON_MI_INDEX",
            }
        ]
    )
    log: list[str] = []

    out = fetcher.apply_canonical_stock_names(source, log)

    assert out.iloc[0]["stock_name"] == "宏旭-KY"
    assert any("Applied canonical stock names" in item for item in log)
