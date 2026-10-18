from __future__ import annotations

from pathlib import Path
import csv
import io
import json

import pandas as pd
import pytest

import fetch_official_daily_price as fetcher


def test_detect_target_date_uses_market_session_override(monkeypatch) -> None:
    monkeypatch.setenv("OFFICIAL_PRICE_TARGET_DATE", "20260713")

    assert fetcher.detect_target_date() == "20260713"


def test_detect_target_date_rejects_invalid_override(monkeypatch) -> None:
    monkeypatch.setenv("OFFICIAL_PRICE_TARGET_DATE", "2026-07-13")

    with pytest.raises(ValueError, match="OFFICIAL_PRICE_TARGET_DATE"):
        fetcher.detect_target_date()


def _write_daily_price(path: Path, date_text: str, base_price: float, rows: int = 1400) -> None:
    records = []
    for index in range(rows):
        stock_id = f"{1000 + index}"
        records.append(
            {
                "date": date_text,
                "stock_id": stock_id,
                "stock_name": f"Stock{stock_id}",
                # Quality selection requires a complete two-market payload.
                "market": "TWSE" if index < 700 else "TPEx",
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
        '{"tables":[{"date":"115/06/09","fields":["代號","名稱","收盤","漲跌","開盤",'
        '"最高","最低","成交股數","成交金額(元)"],"data":[["006201","ETF","26.36","-0.09",'
        '"26.33","26.38","26.31","63,012,000","1,660,553,000"]]}]}'
    )
    log: list[str] = []

    df = fetcher.parse_tpex_json(text, "20260609", "TPEX_TEST", log)

    assert len(df) == 1
    row = df.iloc[0]
    assert row["stock_id"] == "006201"
    assert row["date"] == "20260609"
    assert float(row["volume"]) == 63012000.0
    assert row["source"] == "TPEX_TEST_SHARES_V1"


def _tpex_official_quote_payload() -> dict:
    # Saved official 2026-05-27 receipt, response SHA-256:
    # d20d9657e53d82ca0b78e238d0a2cbd33926f60f43f3d898f9ae90065fdb94f4
    return {
        "date": "20260527",
        "tables": [{
            "date": "20260527",
            "fields": [
                "代號", "名稱", "收盤", "漲跌", "開盤", "最高", "最低", "均價",
                "成交股數", "成交金額(元)", "成交筆數", "最後買價", "最後買量(張數)",
                "最後賣價", "最後賣量(張數)", "發行股數", "次日 參考價", "次日 漲停價", "次日 跌停價",
            ],
            "data": [[
                "5498", "凱崴", "68.80", "-1.50 ", "72.00", "72.20", "67.10", "69.19",
                "7,765,534", "537,313,966", "7,130", "68.50", "4", "68.80", "33",
                "193,548,545", "68.80", "75.60", "62.00",
            ]],
        }],
    }


@pytest.mark.parametrize("reorder", [False, True])
def test_tpex_json_uses_official_19_column_share_and_ntd_fields(reorder):
    payload = _tpex_official_quote_payload()
    table = payload["tables"][0]
    if reorder:
        order = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0, *range(10, 19)]
        table["fields"] = [table["fields"][index] for index in order]
        table["data"][0] = [table["data"][0][index] for index in order]
    frame = fetcher.parse_tpex_json(json.dumps(payload), "20260527", "TPEX_OLD_DAILY_JSON", [])
    assert list(frame.columns) == fetcher.FINAL_COLUMNS
    assert len(frame) == 1
    assert frame.iloc[0].to_dict() == {
        "date": "20260527", "stock_id": "5498", "stock_name": "凱崴", "market": "TPEx",
        "open": 72.0, "high": 72.2, "low": 67.1, "close": 68.8,
        "volume": 7765534, "trading_value": 537313966, "source": "TPEX_OLD_DAILY_JSON_SHARES_V1",
    }


@pytest.mark.parametrize("defect", [
    "fieldless", "missing_shares", "missing_identity", "duplicate", "ambiguous_alias", "unknown_volume",
    "unknown_amount_unit", "unknown_optional", "row_width", "fields_not_list",
])
def test_tpex_json_rejects_unbound_or_ambiguous_schema(defect):
    payload = _tpex_official_quote_payload()
    table = payload["tables"][0]
    if defect == "fieldless":
        del table["fields"]
    elif defect == "missing_shares":
        table["fields"].pop(8)
        table["data"][0].pop(8)
    elif defect == "missing_identity":
        table["fields"] = table["fields"][2:]
        table["data"][0] = table["data"][0][2:]
        # A malformed quote table must reject the entire mixed batch.
        payload["tables"].insert(0, _tpex_official_quote_payload()["tables"][0])
    elif defect == "duplicate":
        table["fields"][9] = table["fields"][8]
    elif defect == "ambiguous_alias":
        table["fields"].append("TradingShares")
        table["data"][0].append("7,765,534")
    elif defect == "unknown_volume":
        table["fields"][8] = "成交量"
    elif defect == "unknown_amount_unit":
        table["fields"][9] = "成交金額"
    elif defect == "unknown_optional":
        table["fields"].append("未審核欄位")
        table["data"][0].append("1")
    elif defect == "row_width":
        table["data"][0].pop()
    else:
        table["fields"] = "代號,成交股數"
    log: list[str] = []
    frame = fetcher.parse_tpex_json(json.dumps(payload), "20260527", "TPEX_OLD_DAILY_JSON", log)
    assert frame.empty
    assert any("rejected TPEx schema" in line for line in log)


def test_tpex_json_binds_each_table_to_its_own_fields_and_visits_once(monkeypatch):
    payload = _tpex_official_quote_payload()
    second = _tpex_official_quote_payload()["tables"][0]
    second["data"][0][0] = "6588"
    second["data"][0][1] = "東典光電"
    second["fields"].reverse()
    second["data"][0].reverse()
    payload["tables"].append(second)
    normalize = fetcher.normalize_row
    visited: list[str] = []

    def recording_normalize(**kwargs):
        visited.append(kwargs["stock_id"])
        return normalize(**kwargs)

    monkeypatch.setattr(fetcher, "normalize_row", recording_normalize)
    frame = fetcher.parse_tpex_json(json.dumps(payload), "20260527", "TPEX_OLD_DAILY_JSON", [])
    assert visited == ["5498", "6588"]
    assert frame["volume"].tolist() == [7765534, 7765534]


def test_tpex_json_keeps_quotes_when_response_also_has_non_security_summary():
    payload = _tpex_official_quote_payload()
    payload["tables"].append({"fields": ["項目", "數值"], "data": [["成交股票數", 1011]]})

    frame = fetcher.parse_tpex_json(json.dumps(payload), "20260527", "TPEX_OLD_DAILY_JSON", [])

    assert len(frame) == 1
    assert frame.iloc[0]["stock_id"] == "5498"
    assert frame.iloc[0]["volume"] == 7765534


@pytest.mark.parametrize("reorder", [False, True])
def test_tpex_csv_uses_header_with_quoted_numbers_and_preamble(reorder):
    table = _tpex_official_quote_payload()["tables"][0]
    if reorder:
        table["fields"].reverse()
        table["data"][0].reverse()
    text = io.StringIO()
    text.write("\ufeff資料日期:115/05/27\n上櫃股票每日收盤行情(不含定價)\n")
    writer = csv.writer(text, quoting=csv.QUOTE_ALL)
    writer.writerow(table["fields"] + [""])
    writer.writerow(table["data"][0] + [""])
    frame = fetcher.parse_tpex_csv(text.getvalue(), "20260527", "TPEX_OLD_DAILY_CSV", [])
    assert len(frame) == 1
    row = frame.iloc[0]
    assert row["volume"] == 7765534
    assert row["trading_value"] == 537313966
    assert row["source"] == "TPEX_OLD_DAILY_CSV_SHARES_V1"


@pytest.mark.parametrize("defect", ["fieldless", "duplicate", "missing_shares", "unknown_unit", "row_width"])
def test_tpex_csv_rejects_unbound_header_or_row(defect):
    table = _tpex_official_quote_payload()["tables"][0]
    if defect == "duplicate":
        table["fields"][9] = "成交股數"
    elif defect == "missing_shares":
        table["fields"].pop(8)
        table["data"][0].pop(8)
    elif defect == "unknown_unit":
        table["fields"][8] = "成交張數"
    elif defect == "row_width":
        table["data"][0].pop()
    text = io.StringIO()
    writer = csv.writer(text)
    if defect != "fieldless":
        writer.writerow(table["fields"])
    writer.writerow(table["data"][0])
    log: list[str] = []
    assert fetcher.parse_tpex_csv(text.getvalue(), "20260527", "TPEX_OLD_DAILY_CSV", log).empty
    assert any("rejected TPEx schema" in line for line in log)


def test_tpex_csv_rejects_partial_quote_batch_after_reordered_header():
    table = _tpex_official_quote_payload()["tables"][0]
    text = io.StringIO()
    writer = csv.writer(text)
    writer.writerow(list(reversed(table["fields"])))
    writer.writerow(list(reversed(table["data"][0])))
    # Identity is the last field after reordering; a short next row cannot be skipped.
    writer.writerow(list(reversed(table["data"][0]))[:-1])
    log: list[str] = []
    assert fetcher.parse_tpex_csv(text.getvalue(), "20260527", "TPEX_OLD_DAILY_CSV", log).empty
    assert any("row width" in line for line in log)


def test_tpex_csv_preserves_empty_optional_column_before_trailing_delimiter():
    table = _tpex_official_quote_payload()["tables"][0]
    table["data"][0][-1] = ""
    text = io.StringIO()
    writer = csv.writer(text)
    writer.writerow(table["fields"] + [""])
    writer.writerow(table["data"][0] + [""])

    frame = fetcher.parse_tpex_csv(text.getvalue(), "20260527", "TPEX_OLD_DAILY_CSV", [])

    assert len(frame) == 1
    assert frame.iloc[0]["volume"] == 7765534
    assert frame.iloc[0]["trading_value"] == 537313966


def _tpex_openapi_quote() -> dict:
    return {
        "SecuritiesCompanyCode": "5498", "CompanyName": "凱崴", "Close": "68.80",
        "Open": "72.00", "High": "72.20", "Low": "67.10",
        "TradingShares": "7,765,534", "TransactionAmount": "537,313,966",
    }


def test_tpex_dictionary_preserves_explicit_share_and_ntd_fields():
    quote = _tpex_openapi_quote()
    quote["TradingShares"] = 0
    frame = fetcher.parse_tpex_json(json.dumps([quote]), "20260527", "TPEX_OPENAPI_MAINBOARD_DAILY_CLOSE_QUOTES", [])
    assert len(frame) == 1
    assert frame.iloc[0]["volume"] == 0
    assert frame.iloc[0]["trading_value"] == 537313966
    assert frame.iloc[0]["source"] == "TPEX_OPENAPI_MAINBOARD_DAILY_CLOSE_QUOTES_SHARES_V1"


@pytest.mark.parametrize("key", ["Volume", "成交量", "成交張數"])
def test_tpex_dictionary_rejects_ambiguous_or_lot_volume(key):
    quote = _tpex_openapi_quote()
    quote[key] = quote.pop("TradingShares")
    log: list[str] = []
    assert fetcher.parse_tpex_json(json.dumps([quote]), "20260527", "TPEX_OPENAPI_MAINBOARD_DAILY_CLOSE_QUOTES", log).empty
    assert any("required dictionary field: volume" in line for line in log)


def test_tpex_dictionary_rejects_ambiguous_amount_unit():
    quote = _tpex_openapi_quote()
    quote["TradingValue"] = quote.pop("TransactionAmount")
    log: list[str] = []
    assert fetcher.parse_tpex_json(json.dumps([quote]), "20260527", "TPEX_OPENAPI_MAINBOARD_DAILY_CLOSE_QUOTES", log).empty
    assert any("required dictionary field: trading_value" in line for line in log)


def test_tpex_fetch_skips_latest_only_openapi_for_historical_target(monkeypatch):
    monkeypatch.setattr(fetcher, "now_taipei", lambda: fetcher.datetime(2026, 6, 18, tzinfo=fetcher.TAIPEI))

    requested: list[str] = []

    def fake_request_text(
        url: str,
        log: list[str],
        referer: str = "https://www.twse.com.tw/",
        **kwargs,
    ) -> str:
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


def test_twse_historical_json_requires_official_exact_response_date(monkeypatch):
    monkeypatch.setattr(fetcher, "REQUIRE_EXACT_HISTORICAL_RESPONSE_DATES", True)
    text = (
        '{"title":"115年07月17日 每日收盤行情","data9":'
        '[["2330","TSMC","1000","10","500000","500","510","495","505"]]}'
    )
    log: list[str] = []

    rejected = fetcher.parse_twse_mi_index_json(
        text,
        "20260720",
        "TWSE_RWD_JSON_MI_INDEX",
        log,
    )
    accepted = fetcher.parse_twse_mi_index_json(
        text,
        "20260717",
        "TWSE_RWD_JSON_MI_INDEX",
        log,
    )

    assert rejected.empty
    assert len(accepted) == 1
    assert accepted.iloc[0]["date"] == "20260717"
    assert accepted.iloc[0]["source"] == "TWSE_RWD_JSON_MI_INDEX"
    assert accepted.iloc[0]["volume"] == 1000
    assert accepted.iloc[0]["trading_value"] == 500000


def test_twse_historical_mode_skips_latest_only_openapi(monkeypatch):
    monkeypatch.setattr(fetcher, "REQUIRE_EXACT_HISTORICAL_RESPONSE_DATES", True)
    requested: list[str] = []

    def fake_request_text(url: str, log: list[str], **kwargs) -> str:
        requested.append(url)
        return ""

    monkeypatch.setattr(fetcher, "request_text", fake_request_text)
    fetcher.fetch_twse_batch("20260720", [])

    assert not any("openapi" in url for url in requested)


def test_official_response_date_extraction_reads_roc_title() -> None:
    text = '{"title":"115年07月20日 每日收盤行情","data9":[]}'
    assert fetcher.collect_official_response_dates_from_text(text) == ["20260720"]


def test_official_response_date_extraction_ignores_data_row_dates() -> None:
    text = (
        '{"title":"115年07月20日 每日收盤行情",'
        '"data9":[["2330","TSMC","2030/12/31","114年01月03日"]]}'
    )
    assert fetcher.collect_official_response_dates_from_text(text) == ["20260720"]


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



def _tpex_observed_20261005_payload() -> dict:
    # Official no1430 JSON saved by run 39114045701; raw response SHA-256:
    # 24413a4dde2bd6cf6cce54dc4902081b1d11b099ef57b49fdbd85de0bebb4f77
    return {
        "date": "20261005", "flagField": "張數", "stat": "ok",
        "tables": [{
            "title": "上櫃股票每日收盤行情(不含定價)", "date": "115/10/05",
            "fields": [
                "代號", "名稱", "收盤 ", "漲跌", "開盤 ", "最高 ", "最低",
                "成交股數  ", " 成交金額(元)", " 成交筆數 ", "最後買價",
                "最後買量<br>(張數)", "最後賣價", "最後賣量<br>(張數)",
                "發行股數 ", "次日漲停價 ", "次日跌停價",
            ],
            "data": [[
                "1240", "茂生農經", "53.90", "-0.10", "54.00", "54.20", "53.80",
                "61,000", "3,293,100", "28", "53.80", "10", "54.00", "5",
                "46,443,992", "59.20", "48.55",
            ]],
        }],
    }


def _decode_observed_tpex_payload(payload: dict, fmt: str, log: list[str]):
    if fmt == "json":
        return fetcher.parse_tpex_json(json.dumps(payload), "20261005", "TPEX_OBSERVED_JSON", log)
    text = io.StringIO()
    # Use an already accepted full-year preamble; ROC slash date parsing is separate.
    text.write(f"資料日期:{payload['date']}\n")
    writer = csv.writer(text, quoting=csv.QUOTE_ALL)
    table = payload["tables"][0]
    writer.writerow(table["fields"])
    writer.writerows(table["data"])
    return fetcher.parse_tpex_csv(text.getvalue(), "20261005", "TPEX_OBSERVED_CSV", log)


@pytest.mark.parametrize("fmt", ["json", "csv"])
@pytest.mark.parametrize("reorder", [False, True])
def test_tpex_observed_17_fields_preserve_quote_mapping_and_units(monkeypatch, fmt, reorder):
    monkeypatch.setattr(fetcher, "REQUIRE_EXACT_HISTORICAL_RESPONSE_DATES", True)
    payload = _tpex_observed_20261005_payload()
    table = payload["tables"][0]
    if reorder:
        table["fields"].reverse()
        table["data"][0].reverse()
    frame = _decode_observed_tpex_payload(payload, fmt, [])
    assert list(frame.columns) == fetcher.FINAL_COLUMNS
    assert len(frame) == 1
    assert frame.iloc[0].to_dict() == {
        "date": "20261005", "stock_id": "1240", "stock_name": "茂生農經", "market": "TPEx",
        "open": 54.0, "high": 54.2, "low": 53.8, "close": 53.9,
        "volume": 61000, "trading_value": 3293100,
        "source": f"TPEX_OBSERVED_{fmt.upper()}_SHARES_V1",
    }


@pytest.mark.parametrize("fmt", ["json", "csv"])
@pytest.mark.parametrize("defect", ["wrong_date", "unknown_field"])
def test_tpex_observed_schema_keeps_date_and_unknown_field_rejections(monkeypatch, fmt, defect):
    monkeypatch.setattr(fetcher, "REQUIRE_EXACT_HISTORICAL_RESPONSE_DATES", True)
    payload = _tpex_observed_20261005_payload()
    if defect == "wrong_date":
        payload["date"] = "20261016"
        payload["tables"][0]["date"] = "20261016"
    else:
        payload["tables"][0]["fields"].append("未批准額外欄位")
        payload["tables"][0]["data"][0].append("9999.95")
    log: list[str] = []
    assert _decode_observed_tpex_payload(payload, fmt, log).empty
    expected = "rejected response dates" if defect == "wrong_date" else "unknown fields/header"
    assert any(expected in line for line in log)
