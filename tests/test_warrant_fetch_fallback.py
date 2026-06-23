from __future__ import annotations

import sys

import pandas as pd

from scripts import fetch_official_warrant_daily as warrant_fetch


def raw_snapshot(date: str = "20260611") -> pd.DataFrame:
    row = {col: "" for col in warrant_fetch.RAW_COLUMNS}
    row.update(
        {
            "date": date,
            "market": "TWSE",
            "source_name": "test",
            "source_url": "https://example.invalid",
            "warrant_id": "030001",
            "warrant_name": "TEST",
            "stock_id": "2330",
            "stock_name": "TSMC",
            "call_put": "call",
            "volume": "10",
            "turnover": "1000",
            "close": "1.23",
            "issuer": "TEST",
        }
    )
    return pd.DataFrame([row])


def patch_warrant_fetch_paths(tmp_path, monkeypatch):
    latest_dir = tmp_path / "output" / "latest"
    debug_dir = tmp_path / "output" / "debug"
    history_dir = tmp_path / "output" / "history" / "warrant_daily"
    price_dir = tmp_path / "data" / "daily_price"

    for path in (latest_dir, debug_dir, history_dir, price_dir):
        path.mkdir(parents=True, exist_ok=True)

    monkeypatch.setattr(warrant_fetch, "OUTPUT_DIR", latest_dir)
    monkeypatch.setattr(warrant_fetch, "DEBUG_DIR", debug_dir)
    monkeypatch.setattr(warrant_fetch, "HISTORY_DIR", history_dir)
    monkeypatch.setattr(warrant_fetch, "RAW_LATEST", latest_dir / "warrant_daily_raw_latest.csv")
    monkeypatch.setattr(warrant_fetch, "FETCH_STATUS_MD", latest_dir / "warrant_daily_fetch_latest.md")
    monkeypatch.setattr(warrant_fetch, "SOURCE_STATUS_JSON", latest_dir / "warrant_source_status_latest.json")
    monkeypatch.setattr(warrant_fetch, "SOURCE_STATUS_MD", latest_dir / "warrant_source_status_latest.md")
    monkeypatch.setattr(warrant_fetch, "DEBUG_MD", debug_dir / "warrant_fetch_debug_latest.md")
    monkeypatch.setattr(warrant_fetch, "DEBUG_CSV", debug_dir / "warrant_fetch_debug_latest.csv")
    monkeypatch.setattr(warrant_fetch, "PRICE_DIR", price_dir)
    return latest_dir, history_dir


def test_empty_live_fetch_preserves_existing_same_date_raw_snapshot(tmp_path, monkeypatch):
    latest_dir, history_dir = patch_warrant_fetch_paths(tmp_path, monkeypatch)
    raw_snapshot().to_csv(history_dir / "warrant_daily_20260611.csv", index=False, encoding="utf-8")

    def fake_fetch(requested_date, deadline=None):
        return (
            "20260611",
            pd.DataFrame(),
            pd.DataFrame(),
            pd.DataFrame(columns=warrant_fetch.RAW_COLUMNS),
            ["live fetch returned no usable rows"],
            [],
            "live fetch failed",
        )

    monkeypatch.setattr(warrant_fetch, "get_latest_price_date", lambda: "20260611")
    monkeypatch.setattr(warrant_fetch, "fetch_warrant_data_with_quote_fallback", fake_fetch)
    monkeypatch.setattr(sys, "argv", ["fetch_official_warrant_daily.py"])

    assert warrant_fetch.main() == 0

    latest_raw = pd.read_csv(latest_dir / "warrant_daily_raw_latest.csv", dtype=str)
    status = (latest_dir / "warrant_daily_fetch_latest.md").read_text(encoding="utf-8")

    assert len(latest_raw) == 1
    assert latest_raw.loc[0, "date"] == "20260611"
    assert latest_raw.loc[0, "stock_id"] == "2330"
    assert "preserved existing same-date raw snapshot" in status
    assert (latest_dir / "warrant_source_status_latest.json").exists()


def test_mapping_only_live_fetch_preserves_existing_same_date_raw_snapshot(tmp_path, monkeypatch):
    latest_dir, history_dir = patch_warrant_fetch_paths(tmp_path, monkeypatch)
    raw_snapshot().to_csv(history_dir / "warrant_daily_20260611.csv", index=False, encoding="utf-8")
    mapping_only = raw_snapshot()
    mapping_only[["volume", "turnover", "close"]] = ""

    def fake_fetch(requested_date, deadline=None):
        return (
            "20260611",
            mapping_only,
            pd.DataFrame(),
            mapping_only,
            ["live fetch returned mapping rows only"],
            [],
            "live fetch had no quotes",
        )

    monkeypatch.setattr(warrant_fetch, "get_latest_price_date", lambda: "20260611")
    monkeypatch.setattr(warrant_fetch, "fetch_warrant_data_with_quote_fallback", fake_fetch)
    monkeypatch.setattr(sys, "argv", ["fetch_official_warrant_daily.py"])

    assert warrant_fetch.main() == 0

    latest_raw = pd.read_csv(latest_dir / "warrant_daily_raw_latest.csv", dtype=str)
    assert latest_raw.loc[0, "turnover"] == "1000"


def test_require_current_usable_preserves_existing_same_date_raw_snapshot(tmp_path, monkeypatch):
    latest_dir, history_dir = patch_warrant_fetch_paths(tmp_path, monkeypatch)
    raw_snapshot("20260623").to_csv(history_dir / "warrant_daily_20260623.csv", index=False, encoding="utf-8")
    captured = {}

    def fake_fetch(requested_date, lookback_days=10, deadline=None):
        captured["lookback_days"] = lookback_days
        return (
            "20260623",
            pd.DataFrame(),
            pd.DataFrame(),
            pd.DataFrame(columns=warrant_fetch.RAW_COLUMNS),
            ["live fetch returned no usable rows"],
            [],
            "live fetch failed",
        )

    monkeypatch.setattr(warrant_fetch, "get_latest_price_date", lambda: "20260623")
    monkeypatch.setattr(warrant_fetch, "fetch_warrant_data_with_quote_fallback", fake_fetch)
    monkeypatch.setattr(sys, "argv", ["fetch_official_warrant_daily.py", "--require-current-usable"])

    assert warrant_fetch.main() == 0
    assert captured["lookback_days"] == 0

    latest_raw = pd.read_csv(latest_dir / "warrant_daily_raw_latest.csv", dtype=str)
    assert latest_raw.loc[0, "date"] == "20260623"
    assert latest_raw.loc[0, "turnover"] == "1000"


def test_require_current_usable_rejects_mapping_only_without_same_date_fallback(tmp_path, monkeypatch):
    latest_dir, _ = patch_warrant_fetch_paths(tmp_path, monkeypatch)
    mapping_only = raw_snapshot("20260623")
    mapping_only[["volume", "turnover", "close"]] = ""
    captured = {}

    def fake_fetch(requested_date, lookback_days=10, deadline=None):
        captured["lookback_days"] = lookback_days
        return (
            "20260623",
            mapping_only,
            pd.DataFrame(),
            mapping_only,
            ["live fetch returned mapping rows only"],
            [],
            "live fetch had no quotes",
        )

    monkeypatch.setattr(warrant_fetch, "get_latest_price_date", lambda: "20260623")
    monkeypatch.setattr(warrant_fetch, "fetch_warrant_data_with_quote_fallback", fake_fetch)
    monkeypatch.setattr(sys, "argv", ["fetch_official_warrant_daily.py", "--require-current-usable"])

    assert warrant_fetch.main() == 1
    assert captured["lookback_days"] == 0

    latest_raw = pd.read_csv(latest_dir / "warrant_daily_raw_latest.csv", dtype=str)
    status = (latest_dir / "warrant_daily_fetch_latest.md").read_text(encoding="utf-8")
    assert latest_raw.loc[0, "date"] == "20260623"
    assert "--require-current-usable requires same-date rows with usable quote values" in status


def test_require_current_usable_rejects_empty_without_same_date_fallback(tmp_path, monkeypatch):
    latest_dir, _ = patch_warrant_fetch_paths(tmp_path, monkeypatch)
    captured = {}

    def fake_fetch(requested_date, lookback_days=10, deadline=None):
        captured["lookback_days"] = lookback_days
        return (
            "20260623",
            pd.DataFrame(),
            pd.DataFrame(),
            pd.DataFrame(columns=warrant_fetch.RAW_COLUMNS),
            ["live fetch returned no usable rows"],
            [],
            "live fetch failed",
        )

    monkeypatch.setattr(warrant_fetch, "get_latest_price_date", lambda: "20260623")
    monkeypatch.setattr(warrant_fetch, "fetch_warrant_data_with_quote_fallback", fake_fetch)
    monkeypatch.setattr(sys, "argv", ["fetch_official_warrant_daily.py", "--require-current-usable"])

    assert warrant_fetch.main() == 1
    assert captured["lookback_days"] == 0

    latest_raw = pd.read_csv(latest_dir / "warrant_daily_raw_latest.csv", dtype=str)
    assert latest_raw.empty
