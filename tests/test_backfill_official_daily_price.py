import copy
import io
import runpy
from datetime import datetime
from pathlib import Path
from unittest.mock import Mock

import pandas as pd
import pytest

import backfill_official_daily_price as backfill


FIELDS = [
    "代號", "名稱", "收盤 ", "漲跌", "開盤 ", "最高 ", "最低",
    "成交股數  ", " 成交金額(元)", " 成交筆數 ", "最後買價",
    "最後買量<br>(張數)", "最後賣價", "最後賣量<br>(張數)",
    "發行股數 ", "次日漲停價 ", "次日跌停價",
]


def quote(code="4123", name="Stock", close="21.25", volume="12,345"):
    return [
        code, name, close, "0.25", "20.5", "21.5", "20.25", volume,
        "262,345", "17", "21.20", "2", "21.25", "3", "100,000,000",
        "23.35", "19.15",
    ]


def payload(rows=None, date="20250919"):
    table_date = f"{int(date[:4]) - 1911}/{date[4:6]}/{date[6:]}"
    return {
        "date": date,
        "flagField": "張數",
        "stat": "ok",
        "tables": [{
            "title": "上櫃股票每日收盤行情(不含定價)",
            "date": table_date,
            "fields": FIELDS.copy(),
            "data": [quote()] if rows is None else rows,
        }],
    }


def test_import_has_no_directory_creation(monkeypatch):
    mkdir = Mock(side_effect=AssertionError("import must not create directories"))
    monkeypatch.setattr(Path, "mkdir", mkdir)
    runpy.run_path(backfill.__file__, run_name="backfill_import_test")
    mkdir.assert_not_called()


def test_parser_exact_units_schema_and_no_payload_mutation():
    source = payload()
    before = copy.deepcopy(source)
    actual = backfill.parse_tpex_daily_price(source, "20250919")
    expected = pd.DataFrame([{
        "date": "20250919", "ticker": "4123", "name": "Stock", "market": "otc",
        "open": 20.5, "high": 21.5, "low": 20.25, "close": 21.25,
        "volume": 12345.0, "turnover": 262345.0,
    }])
    pd.testing.assert_frame_equal(actual, expected)
    assert source == before


@pytest.mark.parametrize("layer", ["response", "table"])
@pytest.mark.parametrize("date", [None, "", "20250918", "114/09/18", "20250230", "invalid"])
def test_rejects_missing_wrong_invalid_or_conflicting_date(layer, date):
    source = payload()
    target = source if layer == "response" else source["tables"][0]
    if date is None:
        del target["date"]
    else:
        target["date"] = date
    with pytest.raises(ValueError):
        backfill.parse_tpex_daily_price(source, "20250919")


@pytest.mark.parametrize("date", ["20250919", "114/09/19", "2025/09/19"])
def test_accepts_equivalent_official_date_formats(date):
    source = payload()
    source["date"] = source["tables"][0]["date"] = date
    assert backfill.parse_tpex_daily_price(source, "20250919")["date"].tolist() == ["20250919"]


def test_rejects_stale_payload_even_when_both_source_dates_agree():
    with pytest.raises(ValueError, match="date mismatch"):
        backfill.parse_tpex_daily_price(payload(date="20250918"), "20250919")


@pytest.mark.parametrize("date", ["2025/09/19", "2025919", "20250230"])
def test_rejects_invalid_requested_date(date):
    with pytest.raises(ValueError):
        backfill.parse_tpex_daily_price(payload(), date)


def test_long_codes_are_excluded_before_common_stock_filter_without_truncation():
    codes = ["4123", "41230", "4123A", "994123", "AB4123", "12345", "00679B", "0012", "123", " 5678 "]
    actual = backfill.parse_tpex_daily_price(payload([quote(code) for code in codes]), "20250919")
    assert actual["ticker"].tolist() == ["4123", "5678"]


@pytest.mark.parametrize("code", ["4123", "4123A"])
@pytest.mark.parametrize("missing_close", [False, True])
def test_duplicate_raw_ids_rejected_before_filtering_or_dropna(code, missing_close):
    second = quote(code, name="Other", close="----" if missing_close else "99")
    with pytest.raises(ValueError, match="duplicate raw security code"):
        backfill.parse_tpex_daily_price(payload([quote(code), second]), "20250919")


def test_identical_duplicate_raw_rows_are_not_silently_deduplicated():
    with pytest.raises(ValueError, match="duplicate raw security code"):
        backfill.parse_tpex_daily_price(payload([quote(), quote()]), "20250919")


def test_no_trade_and_missing_prices_preserve_existing_close_volume_eligibility():
    no_trade = quote("1234", close="----", volume="0")
    no_trade[4:7] = ["----"] * 3
    partial = quote("2345", volume="0")
    partial[4:7] = ["----"] * 3
    rows = [no_trade, partial, quote("3456", volume="----"), quote("4567")]
    actual = backfill.parse_tpex_daily_price(payload(rows), "20250919")
    assert actual["ticker"].tolist() == ["2345", "4567"]
    assert actual.loc[0, ["open", "high", "low"]].isna().all()
    assert actual.loc[0, "volume"] == 0
    assert actual.loc[0, "close"] == 21.25


@pytest.mark.parametrize("defect", ["stat", "title", "duplicate_table", "missing_field", "duplicate_field"])
def test_rejects_unusable_or_ambiguous_official_table(defect):
    source = payload()
    table = source["tables"][0]
    if defect == "stat":
        source["stat"] = "error"
    elif defect == "title":
        table["title"] = "Other table"
    elif defect == "duplicate_table":
        source["tables"].append(copy.deepcopy(table))
    elif defect == "missing_field":
        table["fields"][8] = "Other amount"
    else:
        table["fields"][9] = "收盤"
    with pytest.raises(ValueError):
        backfill.parse_tpex_daily_price(source, "20250919")


def test_empty_official_table_is_not_fabricated():
    assert backfill.parse_tpex_daily_price(payload([]), "20250919").empty


def test_fetch_uses_date_bound_official_endpoint(monkeypatch):
    response = Mock()
    response.json.return_value = payload()
    get = Mock(return_value=response)
    monkeypatch.setattr(backfill.requests, "get", get)
    actual = backfill.fetch_tpex_daily_price("20250919")
    get.assert_called_once_with(
        "https://www.tpex.org.tw/www/zh-tw/afterTrading/otc",
        params={"date": "2025/09/19", "type": "EW", "response": "json"},
        headers={"User-Agent": "Mozilla/5.0"}, timeout=30,
    )
    response.raise_for_status.assert_called_once_with()
    pd.testing.assert_frame_equal(actual, backfill.parse_tpex_daily_price(payload(), "20250919"))


def test_fetch_does_not_hide_response_date_rejection(monkeypatch):
    response = Mock()
    response.json.return_value = payload(date="20250918")
    monkeypatch.setattr(backfill.requests, "get", Mock(return_value=response))
    with pytest.raises(ValueError, match="date mismatch"):
        backfill.fetch_tpex_daily_price("20250919")


def listed_frame(date="20250919", ticker="2330"):
    return pd.DataFrame([{
        "date": date, "ticker": ticker, "name": "Listed", "market": "listed",
        "open": 100.0, "high": 105.0, "low": 99.0, "close": 104.0,
        "volume": 1000.0, "turnover": 104000.0,
    }])


@pytest.mark.parametrize("collision", ["cross_market", "same_market"])
def test_combined_rejects_id_collisions_without_dropping_rows(monkeypatch, collision):
    twse = listed_frame(ticker="4123" if collision == "cross_market" else "2330")
    if collision == "same_market":
        twse = pd.concat([twse, twse], ignore_index=True)
    before = twse.copy(deep=True)
    monkeypatch.setattr(backfill, "fetch_twse_daily_price", lambda date: twse)
    monkeypatch.setattr(backfill, "fetch_tpex_daily_price", lambda date: backfill.parse_tpex_daily_price(payload(), date))
    monkeypatch.setattr(backfill.time, "sleep", lambda seconds: None)
    with pytest.raises(ValueError, match="Duplicate or cross-market daily identity"):
        backfill.fetch_combined_daily_price("20250919")
    pd.testing.assert_frame_equal(twse, before)


def test_twse_fetch_parser_and_combined_listed_rows_unchanged(monkeypatch):
    response = Mock(text=(
        'Report\n"證券代號","證券名稱","開盤價","最高價","最低價","收盤價","成交股數","成交金額"\n'
        '"2330","Listed","100","105","99","104","1,000","104,000"\n'
        '"2330A","Preferred","100","105","99","104","1,000","104,000"\n'
        '"0050","ETF","100","105","99","104","1,000","104,000"\n'
        '"2345","No trade","----","----","----","----","0","0"\n'
    ))
    get = Mock(return_value=response)
    monkeypatch.setattr(backfill.requests, "get", get)
    monkeypatch.setattr(backfill.time, "sleep", lambda seconds: None)
    monkeypatch.setattr(backfill, "fetch_tpex_daily_price", lambda date: backfill.parse_tpex_daily_price(payload(), date))
    twse, _, combined = backfill.fetch_combined_daily_price("20250919")
    get.assert_called_once_with(
        "https://www.twse.com.tw/exchangeReport/MI_INDEX",
        params={"response": "csv", "date": "20250919", "type": "ALLBUT0999"},
        headers={"User-Agent": "Mozilla/5.0"}, timeout=30,
    )
    assert response.encoding == "big5"
    pd.testing.assert_frame_equal(twse, listed_frame())
    pd.testing.assert_frame_equal(combined[combined["market"] == "listed"], twse)


def test_batch_comparison_excludes_only_date_and_listed_rows():
    otc = backfill.parse_tpex_daily_price(payload([quote(), quote("5678")]), "20250919")
    combined = pd.concat([listed_frame(), otc], ignore_index=True)
    previous = pd.read_csv(io.StringIO(combined.to_csv(index=False)), dtype={"date": str, "ticker": str}, float_precision="round_trip")
    previous["date"] = "20250918"
    previous.loc[previous["market"] == "listed", "close"] = 9999
    assert backfill._tpex_batch_signature(previous.iloc[::-1]) == backfill._tpex_batch_signature(otc)
    for field, value in [
        ("name", "Renamed"), ("ticker", "6789"), ("open", 20.6),
        ("high", 21.6), ("low", 20.3), ("close", 21.26),
        ("volume", 12346), ("turnover", 262346),
    ]:
        changed = otc.copy()
        changed.loc[0, field] = value
        assert backfill._tpex_batch_signature(changed) != backfill._tpex_batch_signature(otc)
    assert backfill._tpex_batch_signature(otc.iloc[:1]) != backfill._tpex_batch_signature(otc)


@pytest.fixture
def main_environment(monkeypatch, tmp_path):
    class FixedDatetime(datetime):
        @classmethod
        def now(cls):
            return cls(2025, 9, 26)

    monkeypatch.setattr(backfill, "datetime", FixedDatetime)
    monkeypatch.setattr(backfill, "DATA_DIR", tmp_path / "prices")
    monkeypatch.setattr(backfill, "OUTPUT_DIR", tmp_path / "reports")
    monkeypatch.setattr(backfill, "LOOKBACK_DAYS", 1)
    monkeypatch.setattr(backfill, "MIN_TWSE_ROWS", 1)
    monkeypatch.setattr(backfill, "MIN_TPEX_ROWS", 1)
    monkeypatch.setattr(backfill, "MIN_TOTAL_ROWS", 2)
    monkeypatch.setattr(backfill.time, "sleep", lambda seconds: None)
    monkeypatch.setattr(backfill, "fetch_twse_daily_price", lambda date: listed_frame(date))
    monkeypatch.setattr(backfill, "fetch_tpex_daily_price", lambda date: backfill.parse_tpex_daily_price(payload(date=date), date))
    return tmp_path


def test_main_rejects_exact_batch_repeated_anywhere_in_same_run(main_environment, monkeypatch):
    monkeypatch.setattr(backfill, "LOOKBACK_DAYS", 3)
    monkeypatch.setattr(backfill, "fetch_tpex_daily_price", lambda date: backfill.parse_tpex_daily_price(
        payload([quote(close="22" if date == "20250925" else "21.25")], date), date,
    ))
    backfill.main()
    assert sorted(path.name for path in backfill.DATA_DIR.iterdir()) == ["20250925.csv", "20250926.csv"]
    report = (backfill.OUTPUT_DIR / "official_price_backfill_latest.md").read_text(encoding="utf-8")
    assert "TPEx exact batch repeats 20250926 on 20250924" in report
    stats = pd.read_csv(backfill.OUTPUT_DIR / "official_price_backfill_row_stats.csv", dtype={"date": str})
    assert not stats.loc[stats["date"] == "20250924", "valid"].item()


@pytest.mark.parametrize("different_batch", [False, True])
def test_main_compares_previous_existing_day_and_preserves_it(main_environment, different_batch):
    backfill.DATA_DIR.mkdir()
    previous_otc = backfill.parse_tpex_daily_price(payload(date="20250919"), "20250919")
    if different_batch:
        previous_otc.loc[0, "turnover"] += 1
    previous = pd.concat([listed_frame("20250919"), previous_otc], ignore_index=True)
    previous_path = backfill.DATA_DIR / "20250919.csv"
    previous.to_csv(previous_path, index=False, encoding="utf-8-sig")
    original = previous_path.read_bytes()
    backfill.main()
    assert previous_path.read_bytes() == original
    assert (backfill.DATA_DIR / "20250926.csv").exists() == different_batch
    stats = pd.read_csv(backfill.OUTPUT_DIR / "official_price_backfill_row_stats.csv")
    assert bool(stats.loc[0, "valid"]) == different_batch
    if different_batch:
        saved = pd.read_csv(backfill.DATA_DIR / "20250926.csv", dtype={"date": str, "ticker": str})
        pd.testing.assert_frame_equal(saved[saved["market"] == "listed"], listed_frame("20250926"), check_dtype=False)
    else:
        report = (backfill.OUTPUT_DIR / "official_price_backfill_latest.md").read_text(encoding="utf-8")
        assert "TPEx exact batch repeats existing 20250919 on 20250926" in report


def test_main_rejected_response_never_writes_price_file(main_environment, monkeypatch):
    monkeypatch.setattr(backfill, "fetch_tpex_daily_price", lambda date: backfill.parse_tpex_daily_price(payload(), date))
    backfill.main()
    assert not list(backfill.DATA_DIR.iterdir())
