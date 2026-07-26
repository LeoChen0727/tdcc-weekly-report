from __future__ import annotations

import hashlib
import os
import sys
from pathlib import Path

import pandas as pd
import pytest

REPO_ROOT = Path(__file__).resolve().parents[1]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

SCRIPTS_DIR = REPO_ROOT / "scripts"
if str(SCRIPTS_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPTS_DIR))

from scripts import fetch_futures_options_indicators as fut

class _FakeResponse:
    def __init__(self, content: bytes):
        self.content = content
        self.status_code = 200

    def raise_for_status(self) -> None:
        return None


def _legacy_csv(payload_rows: list[dict[str, str]]) -> bytes:
    text = pd.DataFrame(payload_rows).to_csv(index=False)
    return text.encode("cp950")


def _requested_dates(start_date: str, end_date: str) -> list[str]:
    return [d.strftime("%Y%m%d") for d in pd.date_range(start_date, end_date, freq="B").to_list()]


def test_fetch_taifex_historical_filters_exact_dates_with_ms950(monkeypatch):
    requested_dates = _requested_dates("20260720", "20260724")
    payload = _legacy_csv([
        {"日期": date, "身份別": "外資", "多空未平倉口數淨額": "1"}
        for date in requested_dates
    ])
    def fake_post(*args, **kwargs):
        data = kwargs["data"]
        assert data["queryStartDate"] == "2026/07/20"
        assert data["queryEndDate"] == "2026/07/24"
        return _FakeResponse(payload)

    monkeypatch.setattr(fut, "requests", type("RequestsNamespace", (), {"post": fake_post})())
    df, provenance = fut.fetch_taifex_historical(
        "institutional_fo",
        "20260720",
        "20260724",
        require_exact_source_dates=True,
    )
    assert len(df) == len(requested_dates)
    assert provenance["encoding"] == "cp950"
    assert provenance["requested_dates"] == requested_dates
    assert provenance["observed_dates"] == requested_dates
    assert provenance["rows"] == len(requested_dates)
    assert provenance["raw_sha256"] == hashlib.sha256(payload).hexdigest()


def test_fetch_taifex_historical_fails_missing_or_mixed_dates(monkeypatch):
    requested_dates = _requested_dates("20260720", "20260724")
    missing_payload = _legacy_csv([
        {"日期": requested_dates[0], "身份別": "外資", "多空未平倉口數淨額": "1"},
    ])
    mixed_payload = _legacy_csv([
            {"日期": requested_dates[0], "身份別": "外資", "多空未平倉口數淨額": "1"},
            {"日期": requested_dates[1], "身份別": "外資", "多空未平倉口數淨額": "2"},
            {"日期": requested_dates[2], "身份別": "外資", "多空未平倉口數淨額": "3"},
            {"日期": requested_dates[3], "身份別": "外資", "多空未平倉口數淨額": "4"},
            {"日期": requested_dates[4], "身份別": "外資", "多空未平倉口數淨額": "5"},
            # include out-of-range date, should be rejected when require exact source dates
            {"日期": "20260725", "身份別": "外資", "多空未平倉口數淨額": "5"},
        ])

    def fake_post_missing(*args, **kwargs):
        _ = kwargs["data"]
        return _FakeResponse(missing_payload)

    monkeypatch.setattr(fut, "requests", type("RequestsNamespace", (), {"post": fake_post_missing})())
    with pytest.raises(RuntimeError, match="missing requested dates"):
        fut.fetch_taifex_historical("institutional_fo", "20260720", "20260724")

    def fake_post_mixed(*args, **kwargs):
        _ = kwargs["data"]
        return _FakeResponse(mixed_payload)

    monkeypatch.setattr(fut, "requests", type("RequestsNamespace", (), {"post": fake_post_mixed})())
    with pytest.raises(RuntimeError, match="out-of-range"):
        fut.fetch_taifex_historical("institutional_fo", "20260720", "20260724")


def test_filter_rows_for_target_date_is_exact():
    df = pd.DataFrame(
        [
            {"日期": "20260720", "值": "a"},
            {"日期": "20260721", "值": "b"},
            {"日期": "20260722", "值": "c"},
        ]
    )
    df["日期"] = df["日期"].astype(str)
    assert fut.filter_rows_for_target_date(df, "20260721", "institutional_fo").iloc[0]["值"] == "b"
    with pytest.raises(RuntimeError, match="requested target_date=20260730"):
        fut.filter_rows_for_target_date(df, "20260730", "institutional_fo")


def test_build_indicator_row_filters_by_target_date():
    institutional = pd.DataFrame(
        [
            {"日期": "20260720", "身份別": "外資", "期貨多空未平倉口數淨額": "1"},
            {"日期": "20260721", "身份別": "外資", "期貨多空未平倉口數淨額": "9"},
        ]
    )
    futures_contracts = pd.DataFrame(
        [
            {"日期": "20260720", "身份別": "外資", "商品名稱": "臺股期貨", "多空未平倉口數淨額": "100"},
            {"日期": "20260721", "身份別": "外資", "商品名稱": "臺股期貨", "多空未平倉口數淨額": "200"},
        ]
    )
    options_call_put = pd.DataFrame(
        [
            {"日期": "20260720", "商品名稱": "臺指選擇權", "買賣權別": "CALL", "身份別": "外資", "未平倉口數買賣淨額": "10"},
            {"日期": "20260721", "商品名稱": "臺指選擇權", "買賣權別": "CALL", "身份別": "外資", "未平倉口數買賣淨額": "20"},
        ]
    )
    put_call_ratio = pd.DataFrame([{"日期": "20260720", "賣權成交量": "10", "買權成交量": "10", "買賣權成交量比率%": "1", "賣權未平倉量": "10", "買權未平倉量": "10", "買賣權未平倉量比率%": "1", "買權未平倉量比率%": "1"}])
    vix = pd.DataFrame([{"date": "20260721", "taiwan_vix": 25.0, "vix_return_5d": 1.0, "vix_return_10d": 1.0, "vix_return_20d": 1.0}])
    row = fut.build_indicator_row(
        institutional,
        futures_contracts,
        options_call_put,
        put_call_ratio,
        vix,
        {},
        target_date="20260720",
    ).iloc[0]
    assert row["date"] == "20260720"
    assert row["foreign_futures_net_oi"] == 1.0
    assert row["taifex_institutional_date"] == "20260720"
    assert row["put_call_ratio_date"] == "20260720"


def test_detect_date_column_requires_known_headers_or_raises():
    with pytest.raises(RuntimeError, match="missing date column"):
        fut.detect_date_column(pd.DataFrame({"foo": ["1"], "bar": ["2"]}))

    with pytest.raises(RuntimeError, match="ambiguous date columns"):
        fut.detect_date_column(pd.DataFrame({"日期": ["20260720"], "交易日期": ["20260720"]}))

    assert fut.detect_date_column(pd.DataFrame({"日期": ["20260720"]})) == "日期"


def test_main_rejects_unpaired_target_window(monkeypatch):
    monkeypatch.setattr(sys, "argv", ["fetch_futures_options_indicators.py", "--start-date", "20260720"])
    with pytest.raises(RuntimeError, match="--start-date and --end-date must be provided together"):
        fut.main()


def test_main_rejects_end_without_start(monkeypatch):
    monkeypatch.setattr(sys, "argv", ["fetch_futures_options_indicators.py", "--end-date", "20260724"])
    with pytest.raises(RuntimeError, match="--start-date and --end-date must be provided together"):
        fut.main()


def test_main_rejects_invalid_start_end_raw_dates(monkeypatch):
    monkeypatch.setattr(
        sys,
        "argv",
        ["fetch_futures_options_indicators.py", "--start-date", "foo", "--end-date", "bar"],
    )
    with pytest.raises(RuntimeError, match="must be YYYYMMDD"):
        fut.main()


def test_main_rejects_impossible_raw_dates(monkeypatch):
    monkeypatch.setattr(
        sys,
        "argv",
        [
            "fetch_futures_options_indicators.py",
            "--start-date",
            "20261340",
            "--end-date",
            "20260230",
        ],
    )
    with pytest.raises(RuntimeError, match="must be YYYYMMDD"):
        fut.main()


def _configure_io_roots(monkeypatch: pytest.MonkeyPatch, tmp_path: Path) -> None:
    data_dir = tmp_path / "data"
    fo_dir = data_dir / "futures_options"
    raw_dir = fo_dir / "raw"
    latest_dir = tmp_path / "latest"
    monkeypatch.setattr(fut, "DATA_DIR", data_dir)
    monkeypatch.setattr(fut, "FO_DIR", fo_dir)
    monkeypatch.setattr(fut, "RAW_DIR", raw_dir)
    monkeypatch.setattr(fut, "LATEST_DIR", latest_dir)
    monkeypatch.setattr(
        fut,
        "HISTORY_FILES",
        {
            "institutional_fo": fo_dir / "taifex_institutional_fo_history.csv",
            "futures_contracts": fo_dir / "taifex_futures_contracts_history.csv",
            "options_call_put": fo_dir / "taifex_options_call_put_history.csv",
            "put_call_ratio": fo_dir / "put_call_ratio_history.csv",
            "taiwan_vix": fo_dir / "taiwan_vix_history.csv",
        },
    )
    monkeypatch.setattr(
        fut,
        "LATEST_FILES",
        {
            "institutional_fo": latest_dir / "futures_options_institutional_fo_latest.csv",
            "futures_contracts": latest_dir / "futures_options_contracts_latest.csv",
            "options_call_put": latest_dir / "futures_options_call_put_latest.csv",
            "put_call_ratio": latest_dir / "futures_options_put_call_ratio_latest.csv",
            "taiwan_vix": latest_dir / "taiwan_vix_latest.csv",
        },
    )
    monkeypatch.setattr(fut, "INDICATORS_CSV", latest_dir / "futures_options_indicators_latest.csv")
    monkeypatch.setattr(fut, "STATUS_JSON", latest_dir / "futures_options_source_status_latest.json")
    monkeypatch.setattr(fut, "STATUS_MD", latest_dir / "futures_options_source_status_latest.md")


def test_rows_have_unique_keys_detects_missing_and_duplicate_columns():
    with pytest.raises(RuntimeError, match="missing required key columns"):
        fut.rows_have_unique_keys(pd.DataFrame({"a": ["1"]}), ["a", "b"])
    df = pd.DataFrame({"a": ["1", "1"], "b": ["2", "2"]})
    assert fut.rows_have_unique_keys(df, ["a", "b"]) is False


def test_filter_vix_candidate_exact_dates_supports_superset_and_rejects_missing():
    vix = pd.DataFrame(
        [
            {"date": "20260718", "taiwan_vix": 20.0, "vix_return_5d": 0.0, "vix_return_10d": 0.0, "vix_return_20d": 0.0},
            {"date": "20260719", "taiwan_vix": 21.0, "vix_return_5d": 0.0, "vix_return_10d": 0.0, "vix_return_20d": 0.0},
            {"date": "20260720", "taiwan_vix": 22.0, "vix_return_5d": 0.0, "vix_return_10d": 0.0, "vix_return_20d": 0.0},
            {"date": "20260721", "taiwan_vix": 23.0, "vix_return_5d": 0.0, "vix_return_10d": 0.0, "vix_return_20d": 0.0},
            {"date": "20260722", "taiwan_vix": 24.0, "vix_return_5d": 0.0, "vix_return_10d": 0.0, "vix_return_20d": 0.0},
            {"date": "20260723", "taiwan_vix": 25.0, "vix_return_5d": 0.0, "vix_return_10d": 0.0, "vix_return_20d": 0.0},
            {"date": "20260724", "taiwan_vix": 26.0, "vix_return_5d": 0.0, "vix_return_10d": 0.0, "vix_return_20d": 0.0},
        ]
    )
    _, _, observed_dates = fut.filter_vix_candidate_exact_dates(vix, "20260720", "20260724")
    assert observed_dates == ["20260720", "20260721", "20260722", "20260723", "20260724"]

    missing_one = vix[vix["date"] != "20260723"].copy()
    with pytest.raises(RuntimeError, match="missing requested dates"):
        fut.filter_vix_candidate_exact_dates(
            missing_one,
            "20260720",
            "20260724",
            ["20260720", "20260721", "20260722", "20260723", "20260724"],
        )


def test_main_rejects_historical_vix_missing_target_without_fallback(monkeypatch, tmp_path):
    _configure_io_roots(monkeypatch, tmp_path)
    monkeypatch.setattr(fut, "rows_have_unique_keys", lambda *_: True)
    def fake_fetch_taifex_historical(name, start_date, end_date, require_exact_source_dates=True):
        return pd.DataFrame({"dummy": ["1"]}), {
            "source": name,
            "status": "ok",
            "fetched_at": "",
            "endpoint": "",
            "params": {},
            "encoding": "utf-8",
            "raw_sha256": "",
            "normalized_sha256": "",
            "requested_dates": fut.requested_trading_dates(start_date, end_date),
            "observed_dates": ["20260724"],
            "rows": 1,
        }
    monkeypatch.setattr(fut, "fetch_taifex_historical", fake_fetch_taifex_historical)
    monkeypatch.setattr(
        fut,
        "fetch_vix_history_with_provenance",
        lambda months=6: (
            pd.DataFrame(
                [{"date": "20260721", "taiwan_vix": 1.0, "vix_return_5d": 0.0, "vix_return_10d": 0.0, "vix_return_20d": 0.0}]
            ),
            {"source_files": [], "source_manifest_sha256": "a" * 64},
        ),
    )

    replaced: list[str] = []
    monkeypatch.setattr(
        fut,
        "commit_staged_paths",
        lambda staged_paths, rollback_root: replaced.extend(str(target) for _, target in staged_paths),
    )
    writes: list[str] = []
    monkeypatch.setattr(fut, "write_csv", lambda df, target: writes.append(str(target)))
    monkeypatch.setattr(fut, "append_update_csv", lambda *args, **kwargs: writes.append("append_update"))
    monkeypatch.setattr(fut, "write_status", lambda status, status_json=fut.STATUS_JSON, status_md=fut.STATUS_MD: writes.append("status"))

    monkeypatch.setattr(sys, "argv", ["fetch_futures_options_indicators.py", "--start-date", "20260720", "--end-date", "20260724"])
    with pytest.raises(RuntimeError, match="missing requested dates"):
        fut.main()
    assert writes == []
    assert replaced == []


def test_main_atomic_no_commit_when_stage_write_fails(monkeypatch, tmp_path):
    _configure_io_roots(monkeypatch, tmp_path)
    monkeypatch.setattr(fut, "rows_have_unique_keys", lambda *_: True)
    def fake_fetch_taifex_historical(name, start_date, end_date, require_exact_source_dates=True):
        return pd.DataFrame({"dummy": ["1"]}), {
            "source": name,
            "status": "ok",
            "fetched_at": "",
            "endpoint": "",
            "params": {},
            "encoding": "utf-8",
            "raw_sha256": "",
            "normalized_sha256": "",
            "requested_dates": fut.requested_trading_dates(start_date, end_date),
            "observed_dates": fut.requested_trading_dates(start_date, end_date),
            "rows": 1,
        }
    monkeypatch.setattr(fut, "fetch_taifex_historical", fake_fetch_taifex_historical)
    monkeypatch.setattr(
        fut,
        "fetch_vix_history_with_provenance",
        lambda months=6: (
            pd.DataFrame(
                [
                    {"date": "20260724", "taiwan_vix": 26.0, "vix_return_5d": 0.0, "vix_return_10d": 0.0, "vix_return_20d": 0.0},
                ]
            ),
            {"source_files": [], "source_manifest_sha256": "a" * 64},
        ),
    )
    monkeypatch.setattr(
        fut,
        "build_indicator_row",
        lambda institutional_fo, futures_contracts, options_call_put, put_call_ratio, vix, source_status, target_date="": pd.DataFrame(
            [
                {
                    "date": target_date or "20260724",
                    "source_status": "ready",
                    "taiwan_vix_date": "20260724",
                }
            ]
        ),
    )

    replaced: list[str] = []
    monkeypatch.setattr(fut.Path, "replace", lambda self, target: replaced.append(str(target)) or self)

    call_count = {"write_csv": 0}
    def fail_on_source_latest(df, target):
        call_count["write_csv"] += 1
        target_text = str(target)
        if "futures_options_contracts_latest.csv" in target_text:
            raise RuntimeError("inject write_csv failure")

    monkeypatch.setattr(fut, "write_csv", fail_on_source_latest)
    monkeypatch.setattr(fut, "append_update_csv", lambda *args, **kwargs: None)
    monkeypatch.setattr(fut, "write_status", lambda *args, **kwargs: None)

    monkeypatch.setattr(sys, "argv", ["fetch_futures_options_indicators.py", "--start-date", "20260724", "--end-date", "20260724"])
    with pytest.raises(RuntimeError, match="inject write_csv failure"):
        fut.main()
    assert replaced == []
    assert call_count["write_csv"] >= 1


def test_main_current_fallback_source_not_persisted(monkeypatch, tmp_path):
    _configure_io_roots(monkeypatch, tmp_path)
    monkeypatch.setattr(fut, "rows_have_unique_keys", lambda *_: True)

    def fake_fetch_open_data(data_name: str) -> pd.DataFrame:
        if data_name == "MarketDataOfMajorInstitutionalTradersDividedByFuturesAndOptionsBytheDate":
            raise RuntimeError("open-data failed")
        return pd.DataFrame({"dummy": ["1"]})

    monkeypatch.setattr(fut, "fetch_open_data", fake_fetch_open_data)
    monkeypatch.setattr(
        fut,
        "fetch_vix_history_with_provenance",
        lambda months=6: (
            pd.DataFrame(
                [
                    {"date": "20260724", "taiwan_vix": 26.0, "vix_return_5d": 0.0, "vix_return_10d": 0.0, "vix_return_20d": 0.0},
                ]
            ),
            {"source_files": [], "source_manifest_sha256": "a" * 64},
        ),
    )
    monkeypatch.setattr(
        fut,
        "build_indicator_row",
        lambda institutional_fo, futures_contracts, options_call_put, put_call_ratio, vix, source_status, target_date="": pd.DataFrame(
            [
                {
                    "date": "20260724",
                    "source_status": "partial",
                    "taiwan_vix_date": "20260724",
                }
            ]
        ),
    )

    replaced: list[str] = []
    monkeypatch.setattr(
        fut,
        "commit_staged_paths",
        lambda staged_paths, rollback_root: replaced.extend(str(target) for _, target in staged_paths),
    )
    monkeypatch.setattr(fut, "write_csv", lambda df, target: None)
    monkeypatch.setattr(fut, "append_update_csv", lambda *args, **kwargs: None)
    monkeypatch.setattr(fut, "write_status", lambda *args, **kwargs: None)
    monkeypatch.setattr(fut, "read_csv", lambda *args, **kwargs: pd.DataFrame({"dummy": ["1"]}))

    monkeypatch.setattr(sys, "argv", ["fetch_futures_options_indicators.py"])
    assert fut.main() == 0
    assert not any("institutional_fo" in target for target in replaced)
    assert any("futures_options_indicators_latest.csv" in target for target in replaced)


def test_build_indicator_row_target_date_bypasses_freshness_cap(monkeypatch):
    frames = {
        "institutional_fo": pd.DataFrame({"date": ["20260717", "20260724"], "col": [0.0, 1.0]}),
        "futures_contracts": pd.DataFrame({"date": ["20260724"], "col": [1.0]}),
        "options_call_put": pd.DataFrame({"date": ["20260724"], "col": [1.0]}),
        "put_call_ratio": pd.DataFrame({"日期": ["20260724"], "col": [1.0]}),
        "vix": pd.DataFrame({"date": ["20260724"], "taiwan_vix": [26.0], "vix_return_5d": [1.0], "vix_return_10d": [1.0], "vix_return_20d": [1.0]}),
    }
    monkeypatch.setattr(fut, "main_price_date_from_freshness", lambda: "20260717")
    row = fut.build_indicator_row(
        frames["institutional_fo"],
        frames["futures_contracts"],
        frames["options_call_put"],
        frames["put_call_ratio"],
        frames["vix"],
        {},
        target_date="20260724",
    ).iloc[0]
    assert row["date"] == "20260724"
    assert row["taiwan_vix_date"] == "20260724"


def test_commit_staged_paths_replaces_bytes_and_verifies_sha(tmp_path):
    staged_one = tmp_path / "stage" / "one.stage"
    staged_two = tmp_path / "stage" / "two.stage"
    target_one = tmp_path / "target" / "one.csv"
    target_two = tmp_path / "target" / "two.csv"
    staged_one.parent.mkdir(parents=True)
    target_one.parent.mkdir(parents=True)
    staged_one.write_bytes(b"new-one\n")
    staged_two.write_bytes(b"new-two\n")
    target_one.write_bytes(b"old-one\n")
    target_two.write_bytes(b"old-two\n")

    expected = {
        target_one: fut.file_sha256(staged_one),
        target_two: fut.file_sha256(staged_two),
    }
    fut.commit_staged_paths(
        [(staged_one, target_one), (staged_two, target_two)],
        tmp_path / "rollback",
    )

    assert target_one.read_bytes() == b"new-one\n"
    assert target_two.read_bytes() == b"new-two\n"
    assert fut.file_sha256(target_one) == expected[target_one]
    assert fut.file_sha256(target_two) == expected[target_two]


def test_commit_staged_paths_rolls_back_all_touched_targets(monkeypatch, tmp_path):
    staged_one = tmp_path / "stage" / "one.stage"
    staged_two = tmp_path / "stage" / "two.stage"
    target_one = tmp_path / "target" / "one.csv"
    target_two = tmp_path / "target" / "two.csv"
    staged_one.parent.mkdir(parents=True)
    target_one.parent.mkdir(parents=True)
    staged_one.write_bytes(b"new-one\n")
    staged_two.write_bytes(b"new-two\n")
    target_one.write_bytes(b"old-one\n")
    target_two.write_bytes(b"old-two\n")
    original_replace = Path.replace

    def fail_second_replace(self, target):
        if self.name == "two.stage":
            raise OSError("injected replace failure")
        return original_replace(self, target)

    monkeypatch.setattr(Path, "replace", fail_second_replace)
    with pytest.raises(OSError, match="injected replace failure"):
        fut.commit_staged_paths(
            [(staged_one, target_one), (staged_two, target_two)],
            tmp_path / "rollback",
        )

    assert target_one.read_bytes() == b"old-one\n"
    assert target_two.read_bytes() == b"old-two\n"


def test_fetch_vix_month_provenance_hashes_actual_payload(monkeypatch):
    payload = "2026/07/24\t18.5\n".encode("cp950")

    def fake_get(*args, **kwargs):
        return _FakeResponse(payload)

    monkeypatch.setattr(fut, "requests", type("RequestsNamespace", (), {"get": fake_get})())
    frame, provenance = fut.fetch_vix_month_with_provenance("202607")

    assert frame.iloc[0]["date"] == "20260724"
    assert provenance["raw_sha256"] == hashlib.sha256(payload).hexdigest()
    decoded = payload.decode(provenance["encoding"])
    assert provenance["normalized_sha256"] == hashlib.sha256(decoded.encode("utf-8")).hexdigest()


def test_vix_latest_context_keeps_chart_history_and_excludes_future_rows():
    dates = pd.date_range("2026-01-20", "2026-07-27", freq="B").strftime("%Y%m%d")
    history = pd.DataFrame(
        {
            "date": dates,
            "taiwan_vix": range(len(dates)),
            "vix_return_5d": range(len(dates)),
        }
    )
    latest = fut.vix_latest_context(history, "20260724")

    assert len(latest) > 100
    assert latest["date"].max() == "20260724"
    assert not (latest["date"] > "20260724").any()
    assert latest.iloc[-1]["vix_return_5d"] == history.loc[
        history["date"].eq("20260724"), "vix_return_5d"
    ].iloc[0]


def test_put_call_latest_context_keeps_chart_history_and_excludes_future_rows():
    dates = pd.date_range("2026-01-01", "2026-07-27", freq="B").strftime("%Y%m%d")
    history = pd.DataFrame({"日期": dates, "買賣權成交量比率%": range(len(dates))})
    latest = fut.dated_latest_context(
        history,
        "20260724",
        date_col="日期",
        max_rows=90,
    )

    assert len(latest) == 90
    assert latest["日期"].max() == "20260724"
    assert not (latest["日期"] > "20260724").any()
