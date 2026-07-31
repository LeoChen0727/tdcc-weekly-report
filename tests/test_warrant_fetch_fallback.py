from __future__ import annotations

import hashlib
import json
from pathlib import Path
import sys

import pandas as pd
import pytest

from scripts import fetch_official_warrant_daily as warrant_fetch


class FakeResponse:
    def __init__(self, payload: str, status_code: int = 200):
        self.text = payload
        self.content = payload.encode("utf-8")
        self.status_code = status_code
        self.encoding = "utf-8"
        self.apparent_encoding = "utf-8"


def accepted_response(
    source_name: str,
    logical_group: str,
    *,
    date: str = "20260720",
    sha: str = "a" * 64,
) -> dict:
    family = "mapping" if logical_group == "mapping" else "quote"
    return {
        "endpoint": "https://example.invalid/" + source_name,
        "source_name": source_name,
        "family": family,
        "logical_group": logical_group,
        "attempt": 1,
        "params": {"date": date},
        "status_code": 200,
        "fetched_at": "2026-07-27 01:00:00 Asia/Taipei",
        "elapsed_seconds": 0.1,
        "raw_bytes": 100,
        "raw_sha256": sha,
        "normalized_sha256": sha,
        "encoding": "utf-8",
        "observed_response_dates": [date],
        "expected_response_date": date,
        "exact_date_match": True,
        "parsed_table_count": 1,
        "parsed_table_rows": 1,
        "accepted_rows": 1,
        "accepted": True,
        "status": "accepted",
        "error": "",
    }


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


def test_historical_replay_requires_strict_flag_bundle(monkeypatch):
    monkeypatch.setattr(
        sys,
        "argv",
        ["fetch_official_warrant_daily.py", "--date", "20260720", "--historical-replay"],
    )
    with pytest.raises(RuntimeError, match="requires --require-live-fetch"):
        warrant_fetch.main()


def test_historical_replay_date_must_be_calendar_valid(monkeypatch):
    monkeypatch.setattr(
        sys,
        "argv",
        [
            "fetch_official_warrant_daily.py",
            "--date",
            "20260230",
            "--historical-replay",
            "--require-live-fetch",
            "--require-current-usable",
        ],
    )
    with pytest.raises(RuntimeError, match="calendar-valid YYYYMMDD"):
        warrant_fetch.main()


def test_historical_replay_provenance_requires_valid_response_hashes(monkeypatch):
    response = accepted_response("TWSE_MI_INDEX_0999_JSON", "quote-0999")
    response["raw_sha256"] = "bad"
    monkeypatch.setattr(warrant_fetch, "fetch_response_provenance", lambda: [response])
    with pytest.raises(RuntimeError, match="valid raw_sha256"):
        warrant_fetch.attach_replay_provenance(
            {"status": "ok"},
            historical_replay=True,
            requested_date="20260720",
            data_date="20260720",
            fallback_used=False,
        )


def test_historical_replay_rejects_response_date_mismatch(monkeypatch):
    monkeypatch.setattr(
        warrant_fetch,
        "fetch_response_provenance",
        lambda: [
            accepted_response("TWSE_MI_INDEX_0999_JSON", "quote-0999"),
            accepted_response("TWSE_MI_INDEX_0999P_JSON", "quote-0999P"),
            accepted_response("TWSE_WARRANT_STOCK_JSON", "mapping"),
        ],
    )
    with pytest.raises(RuntimeError, match="response date mismatch"):
        warrant_fetch.attach_replay_provenance(
            {"status": "ok"},
            historical_replay=True,
            requested_date="20260720",
            data_date="20260717",
            fallback_used=False,
        )


def test_historical_replay_never_uses_existing_raw_fallback(tmp_path, monkeypatch):
    latest_dir, history_dir = patch_warrant_fetch_paths(tmp_path, monkeypatch)
    history_path = history_dir / "warrant_daily_20260720.csv"
    latest_path = latest_dir / "warrant_daily_raw_latest.csv"
    raw_snapshot("20260720").to_csv(history_path, index=False, encoding="utf-8")
    latest_path.write_bytes(b"existing-latest")
    before_history = history_path.read_bytes()
    before_latest = latest_path.read_bytes()

    def fake_fetch(
        requested_date,
        lookback_days=10,
        deadline=None,
        require_exact_response_date=False,
    ):
        return (
            requested_date,
            pd.DataFrame(),
            pd.DataFrame(),
            pd.DataFrame(columns=warrant_fetch.RAW_COLUMNS),
            ["live fetch empty"],
            [],
            "live fetch failed",
        )

    monkeypatch.setattr(warrant_fetch, "fetch_warrant_data_with_quote_fallback", fake_fetch)
    monkeypatch.setattr(
        warrant_fetch,
        "fetch_response_provenance",
        lambda: [
            accepted_response("TWSE_MI_INDEX_0999_JSON", "quote-0999"),
            accepted_response("TWSE_MI_INDEX_0999P_JSON", "quote-0999P"),
            accepted_response("TWSE_WARRANT_STOCK_JSON", "mapping"),
        ],
    )
    monkeypatch.setattr(
        sys,
        "argv",
        [
            "fetch_official_warrant_daily.py",
            "--date",
            "20260720",
            "--historical-replay",
            "--require-live-fetch",
            "--require-current-usable",
        ],
    )

    with pytest.raises(RuntimeError, match="mapping output is empty"):
        warrant_fetch.main()
    assert history_path.read_bytes() == before_history
    assert latest_path.read_bytes() == before_latest
    assert not (latest_dir / "warrant_daily_fetch_latest.md").exists()
    assert not (latest_dir / "warrant_source_status_latest.json").exists()


def patch_strict_family_parsers(monkeypatch):
    def fake_read_tables(text):
        return [pd.DataFrame([{"marker": json.loads(text)["marker"]}])]

    def fake_mapping_parser(table, market, source_name, source_url):
        return pd.DataFrame(
            [
                {
                    "warrant_id": "030001",
                    "stock_id": "2330",
                    "stock_name": "TSMC",
                    "call_put_raw": "call",
                    "call_put": "call",
                    "issuer": "TEST",
                },
                {
                    "warrant_id": "03001P",
                    "stock_id": "2317",
                    "stock_name": "HON HAI",
                    "call_put_raw": "put",
                    "call_put": "put",
                    "issuer": "TEST",
                },
            ]
        )

    def fake_quote_parser(table, source_name, source_url):
        marker = table.loc[0, "marker"]
        warrant_id = "03001P" if marker == "quote-0999P" else "030001"
        return pd.DataFrame(
            [
                {
                    "market": "TWSE",
                    "source_name": source_name,
                    "source_url": source_url,
                    "warrant_id": warrant_id,
                    "warrant_name": marker,
                    "volume": 10,
                    "turnover": 1000,
                    "close": 1.0,
                }
            ]
        )

    monkeypatch.setattr(warrant_fetch, "read_tables_from_text", fake_read_tables)
    monkeypatch.setattr(warrant_fetch, "standardize_warrant_mapping_table", fake_mapping_parser)
    monkeypatch.setattr(warrant_fetch, "standardize_twse_mi_index_quotes_v2", fake_quote_parser)
    monkeypatch.setattr(warrant_fetch.time, "sleep", lambda *_: None)


def response_payload(logical_group: str, date_title: str = "115年07月20日") -> str:
    return json.dumps(
        {"title": date_title, "marker": logical_group},
        ensure_ascii=False,
    )


def group_from_url(url: str) -> str:
    if "warrantStock" in url:
        return "mapping"
    if "type=0999P" in url:
        return "quote-0999P"
    return "quote-0999"


def historical_argv() -> list[str]:
    return [
        "fetch_official_warrant_daily.py",
        "--date",
        "20260720",
        "--historical-replay",
        "--require-live-fetch",
        "--require-current-usable",
    ]


def seed_output_sentinels(latest_dir, history_dir) -> dict:
    paths = [
        latest_dir / "warrant_daily_raw_latest.csv",
        latest_dir / "warrant_daily_fetch_latest.md",
        latest_dir / "warrant_source_status_latest.json",
        latest_dir / "warrant_source_status_latest.md",
        warrant_fetch.DEBUG_MD,
        warrant_fetch.DEBUG_CSV,
        history_dir / "warrant_daily_20260720.csv",
    ]
    snapshots = {}
    for index, path in enumerate(paths):
        path.parent.mkdir(parents=True, exist_ok=True)
        payload = f"sentinel-{index}".encode("utf-8")
        path.write_bytes(payload)
        snapshots[path] = payload
    return snapshots


def valid_historical_result():
    mapping = pd.DataFrame(
        [
            {
                "warrant_id": "030001",
                "stock_id": "2330",
                "stock_name": "TSMC",
                "call_put_raw": "call",
                "call_put": "call",
                "issuer": "TEST",
            },
            {
                "warrant_id": "03001P",
                "stock_id": "2317",
                "stock_name": "HON HAI",
                "call_put_raw": "put",
                "call_put": "put",
                "issuer": "TEST",
            },
        ]
    )
    quotes = pd.DataFrame(
        [
            {
                "market": "TWSE",
                "source_name": "TWSE_MI_INDEX_0999_JSON",
                "source_url": "https://example.invalid/0999",
                "warrant_id": "030001",
                "warrant_name": "CALL",
                "volume": 10,
                "turnover": 1000,
                "close": 1.0,
            },
            {
                "market": "TWSE",
                "source_name": "TWSE_MI_INDEX_0999P_JSON",
                "source_url": "https://example.invalid/0999P",
                "warrant_id": "03001P",
                "warrant_name": "PUT",
                "volume": 20,
                "turnover": 2000,
                "close": 2.0,
            },
        ]
    )
    out = warrant_fetch.merge_mapping_and_quotes(mapping, quotes, "20260720")
    return mapping, quotes, out


def patch_valid_historical_result(monkeypatch):
    mapping, quotes, out = valid_historical_result()
    monkeypatch.setattr(
        warrant_fetch,
        "fetch_warrant_data_with_quote_fallback",
        lambda *args, **kwargs: (
            "20260720",
            mapping,
            quotes,
            out,
            [],
            [
                {
                    "source_name": "test",
                    "market": "TWSE",
                    "table_index": 0,
                    "rows": len(out),
                    "parsed_as": "test",
                    "columns": "warrant_id",
                }
            ],
            "",
        ),
    )
    monkeypatch.setattr(
        warrant_fetch,
        "fetch_response_provenance",
        lambda: [
            accepted_response("TWSE_WARRANT_STOCK_JSON", "mapping"),
            accepted_response("TWSE_MI_INDEX_0999_JSON", "quote-0999"),
            accepted_response("TWSE_MI_INDEX_0999P_JSON", "quote-0999P"),
        ],
    )
    monkeypatch.setattr(sys, "argv", historical_argv())


def test_historical_replay_retries_each_required_group_and_skips_csv_after_json_success(
    tmp_path,
    monkeypatch,
):
    latest_dir, history_dir = patch_warrant_fetch_paths(tmp_path, monkeypatch)
    patch_strict_family_parsers(monkeypatch)
    calls = []
    counts = {"mapping": 0, "quote-0999": 0, "quote-0999P": 0}

    def fake_get(url, **kwargs):
        group = group_from_url(url)
        counts[group] += 1
        calls.append((url, kwargs["timeout"]))
        if counts[group] == 1:
            raise warrant_fetch.requests.Timeout(f"transient {group}")
        return FakeResponse(response_payload(group))

    monkeypatch.setattr(warrant_fetch.requests, "get", fake_get)
    monkeypatch.setattr(sys, "argv", historical_argv())

    assert warrant_fetch.main() == 0
    assert counts == {"mapping": 2, "quote-0999": 2, "quote-0999P": 2}
    assert all("response=csv" not in url for url, _ in calls)
    assert all(timeout == warrant_fetch.HISTORICAL_REPLAY_REQUEST_TIMEOUT_SECONDS for _, timeout in calls)

    raw = pd.read_csv(latest_dir / "warrant_daily_raw_latest.csv", dtype=str)
    assert set(raw["warrant_id"]) == {"030001", "03001P"}
    assert set(raw["date"]) == {"20260720"}
    assert (history_dir / "warrant_daily_20260720.csv").exists()

    status = json.loads(
        (latest_dir / "warrant_source_status_latest.json").read_text(encoding="utf-8")
    )
    attempts = status["source_responses"]
    assert len(attempts) == 6
    for group in counts:
        group_attempts = [row for row in attempts if row["logical_group"] == group]
        assert [row["status"] for row in group_attempts] == ["failed", "accepted"]
        assert group_attempts[0]["status_code"] == 0
        assert group_attempts[0]["raw_sha256"] == ""
        assert "Timeout" in group_attempts[0]["error"]
        assert group_attempts[1]["status_code"] == 200
        assert group_attempts[1]["observed_response_dates"] == ["20260720"]
        assert group_attempts[1]["raw_sha256"] == hashlib.sha256(
            response_payload(group).encode("utf-8")
        ).hexdigest()


@pytest.mark.parametrize(
    "failed_stage",
    ["raw", "history", "debug", "fetch_status", "source_status"],
)
def test_historical_stage_failure_preserves_every_existing_output(
    failed_stage,
    tmp_path,
    monkeypatch,
):
    latest_dir, history_dir = patch_warrant_fetch_paths(tmp_path, monkeypatch)
    snapshots = seed_output_sentinels(latest_dir, history_dir)
    patch_valid_historical_result(monkeypatch)

    if failed_stage in {"raw", "history"}:
        original_to_csv = pd.DataFrame.to_csv
        failed_name = (
            "warrant_daily_raw_latest.csv"
            if failed_stage == "raw"
            else "warrant_daily_20260720.csv"
        )

        def fail_selected_csv(self, path_or_buf=None, *args, **kwargs):
            path = Path(path_or_buf) if isinstance(path_or_buf, (str, Path)) else None
            if path is not None and path.name == failed_name and path.parent.name.startswith(
                ".historical-warrant-replay-"
            ):
                raise OSError(f"injected {failed_stage} staging failure")
            return original_to_csv(self, path_or_buf, *args, **kwargs)

        monkeypatch.setattr(pd.DataFrame, "to_csv", fail_selected_csv)
    else:
        function_name = {
            "debug": "write_debug",
            "fetch_status": "write_status",
            "source_status": "write_source_status",
        }[failed_stage]

        def fail_writer(*args, **kwargs):
            raise OSError(f"injected {failed_stage} staging failure")

        monkeypatch.setattr(warrant_fetch, function_name, fail_writer)

    with pytest.raises(OSError, match=f"injected {failed_stage}"):
        warrant_fetch.main()

    assert all(path.read_bytes() == payload for path, payload in snapshots.items())
    assert not list(latest_dir.glob(".historical-warrant-replay-*"))


@pytest.mark.parametrize("failed_replace", range(1, 8))
def test_historical_transaction_rolls_back_each_publish_replace(
    failed_replace,
    tmp_path,
    monkeypatch,
):
    latest_dir, history_dir = patch_warrant_fetch_paths(tmp_path, monkeypatch)
    snapshots = seed_output_sentinels(latest_dir, history_dir)
    patch_valid_historical_result(monkeypatch)
    original_replace = Path.replace
    replace_count = 0

    def fail_selected_replace(self, target):
        nonlocal replace_count
        replace_count += 1
        if replace_count == failed_replace:
            raise OSError(f"injected replace {failed_replace}")
        return original_replace(self, target)

    monkeypatch.setattr(Path, "replace", fail_selected_replace)

    with pytest.raises(OSError, match=f"injected replace {failed_replace}"):
        warrant_fetch.main()

    assert replace_count == failed_replace
    assert all(path.read_bytes() == payload for path, payload in snapshots.items())
    assert not list(latest_dir.glob(".historical-warrant-replay-*"))


@pytest.mark.parametrize("failed_group", ["mapping", "quote-0999", "quote-0999P"])
def test_historical_replay_group_exhaustion_preserves_all_existing_outputs(
    failed_group,
    tmp_path,
    monkeypatch,
):
    latest_dir, history_dir = patch_warrant_fetch_paths(tmp_path, monkeypatch)
    snapshots = seed_output_sentinels(latest_dir, history_dir)
    patch_strict_family_parsers(monkeypatch)
    calls = []

    def fake_get(url, **kwargs):
        group = group_from_url(url)
        calls.append(url)
        if group == failed_group:
            raise warrant_fetch.requests.Timeout(f"exhausted {group}")
        return FakeResponse(response_payload(group))

    monkeypatch.setattr(warrant_fetch.requests, "get", fake_get)
    monkeypatch.setattr(sys, "argv", historical_argv())

    match = "family=mapping" if failed_group == "mapping" else f"subfamily={failed_group.removeprefix('quote-')}"
    with pytest.raises(RuntimeError, match=match) as exc_info:
        warrant_fetch.main()

    evidence = str(exc_info.value)
    assert f'"logical_group": "{failed_group}"' in evidence
    assert '"status": "failed"' in evidence
    assert '"status_code": 0' in evidence
    assert '"raw_sha256": ""' in evidence
    assert "Timeout" in evidence
    failed_calls = [url for url in calls if group_from_url(url) == failed_group]
    assert len(failed_calls) == 2 * warrant_fetch.HISTORICAL_REPLAY_MAX_ATTEMPTS
    assert all("date=20260720" in url for url in calls)
    assert all(path.read_bytes() == payload for path, payload in snapshots.items())


def test_expired_deadline_before_quote_records_structured_group_exhaustion(monkeypatch):
    network_calls = []
    monkeypatch.setattr(
        warrant_fetch.requests,
        "get",
        lambda *args, **kwargs: network_calls.append((args, kwargs)),
    )
    monkeypatch.setattr(warrant_fetch.time, "sleep", lambda *_: None)
    warrant_fetch.reset_fetch_response_provenance()

    with pytest.raises(RuntimeError, match="family=quote subfamily=0999") as exc_info:
        warrant_fetch.fetch_warrant_data_with_quote_fallback(
            "20260720",
            lookback_days=0,
            deadline=warrant_fetch.time.monotonic() - 1,
            require_exact_response_date=True,
        )

    attempts = warrant_fetch.fetch_response_provenance()
    assert network_calls == []
    assert len(attempts) == 2 * warrant_fetch.HISTORICAL_REPLAY_MAX_ATTEMPTS
    assert {row["logical_group"] for row in attempts} == {"quote-0999"}
    assert all(row["status"] == "failed" for row in attempts)
    assert all("deadline_exceeded before_request" in row["error"] for row in attempts)
    assert '"status_code": 0' in str(exc_info.value)


def test_expired_deadline_between_quote_and_mapping_records_mapping_exhaustion(monkeypatch):
    _, quotes, _ = valid_historical_result()
    network_calls = []
    monkeypatch.setattr(
        warrant_fetch,
        "fetch_twse_mi_index_quotes",
        lambda *args, **kwargs: (quotes, ["quote accepted"], []),
    )
    monkeypatch.setattr(
        warrant_fetch.requests,
        "get",
        lambda *args, **kwargs: network_calls.append((args, kwargs)),
    )
    monkeypatch.setattr(warrant_fetch.time, "sleep", lambda *_: None)
    warrant_fetch.reset_fetch_response_provenance()

    with pytest.raises(RuntimeError, match="family=mapping"):
        warrant_fetch.fetch_warrant_data_with_quote_fallback(
            "20260720",
            lookback_days=0,
            deadline=warrant_fetch.time.monotonic() - 1,
            require_exact_response_date=True,
        )

    attempts = warrant_fetch.fetch_response_provenance()
    assert network_calls == []
    assert len(attempts) == 2 * warrant_fetch.HISTORICAL_REPLAY_MAX_ATTEMPTS
    assert {row["logical_group"] for row in attempts} == {"mapping"}
    assert all("deadline_exceeded before_request" in row["error"] for row in attempts)


def test_retry_sleep_is_clamped_to_deadline(monkeypatch):
    sleeps = []
    monkeypatch.setattr(warrant_fetch.time, "monotonic", lambda: 100.0)
    monkeypatch.setattr(warrant_fetch.time, "sleep", lambda delay: sleeps.append(delay))

    actual = warrant_fetch.sleep_with_deadline(5.0, 101.0)

    assert actual == 1.0
    assert sleeps == [1.0]


def test_request_timeout_never_exceeds_subsecond_deadline(monkeypatch):
    monkeypatch.setattr(warrant_fetch.time, "monotonic", lambda: 100.0)

    assert warrant_fetch.request_timeout(100.125, 30.0) == pytest.approx(0.125)
    with pytest.raises(RuntimeError, match="deadline exhausted"):
        warrant_fetch.request_timeout(100.0, 30.0)


def test_historical_replay_rejects_one_quote_type_only(monkeypatch):
    monkeypatch.setattr(
        warrant_fetch,
        "fetch_response_provenance",
        lambda: [
            accepted_response("TWSE_WARRANT_STOCK_JSON", "mapping"),
            accepted_response("TWSE_MI_INDEX_0999_JSON", "quote-0999"),
        ],
    )
    with pytest.raises(RuntimeError, match="quote types 0999 and 0999P"):
        warrant_fetch.attach_replay_provenance(
            {"status": "ok"},
            historical_replay=True,
            requested_date="20260720",
            data_date="20260720",
            fallback_used=False,
        )


def test_historical_replay_merge_pk_failure_preserves_existing_outputs(tmp_path, monkeypatch):
    latest_dir, history_dir = patch_warrant_fetch_paths(tmp_path, monkeypatch)
    snapshots = seed_output_sentinels(latest_dir, history_dir)
    mapping = pd.DataFrame([{"warrant_id": "030001"}])
    quotes = pd.DataFrame(
        [
            {
                "market": "TWSE",
                "warrant_id": "030001",
                "volume": 10,
                "turnover": 1000,
                "close": 1.0,
            }
        ]
    )
    out = raw_snapshot("20260720")
    out = pd.concat([out, out], ignore_index=True)

    monkeypatch.setattr(
        warrant_fetch,
        "fetch_warrant_data_with_quote_fallback",
        lambda *args, **kwargs: (
            "20260720",
            mapping,
            quotes,
            out,
            [],
            [],
            "",
        ),
    )
    monkeypatch.setattr(sys, "argv", historical_argv())

    with pytest.raises(RuntimeError, match="primary key is not unique"):
        warrant_fetch.main()
    assert all(path.read_bytes() == payload for path, payload in snapshots.items())


def test_historical_output_rejects_any_blank_or_non_exact_date_row():
    mapping, quotes, out = valid_historical_result()
    out.loc[out.index[-1], "date"] = ""

    with pytest.raises(RuntimeError, match="non-exact date rows"):
        warrant_fetch.validate_historical_replay_output(
            requested_date="20260720",
            data_date="20260720",
            mapping=mapping,
            quotes=quotes,
            out=out,
        )


def test_historical_output_rejects_same_quote_id_added_under_another_market():
    mapping, quotes, out = valid_historical_result()
    mapping = mapping.iloc[[0]].copy()
    quotes = quotes.iloc[[0]].copy()
    out = out.iloc[[0]].copy()
    duplicate_market = out.copy()
    duplicate_market["market"] = "TPEX"
    out = pd.concat([out, duplicate_market], ignore_index=True)

    with pytest.raises(RuntimeError, match="lost or added quote rows"):
        warrant_fetch.validate_historical_replay_output(
            requested_date="20260720",
            data_date="20260720",
            mapping=mapping,
            quotes=quotes,
            out=out,
        )


@pytest.mark.parametrize(
    ("status_code", "title", "expected_error"),
    [
        (503, "115年07月20日", "HTTP status 503"),
        (200, "115年07月21日", "response_date_mismatch"),
        (200, "115年07月20日", "empty_or_unparsed"),
    ],
)
def test_fetch_source_records_http_date_and_empty_failure_evidence(
    status_code,
    title,
    expected_error,
    monkeypatch,
):
    payload = response_payload("quote-0999", title)
    monkeypatch.setattr(warrant_fetch.requests, "get", lambda *args, **kwargs: FakeResponse(payload, status_code))
    monkeypatch.setattr(warrant_fetch, "read_tables_from_text", lambda *_: [])
    warrant_fetch.reset_fetch_response_provenance()

    frames, _, attempt = warrant_fetch.fetch_source(
        "https://example.invalid?date=20260720",
        "TWSE_MI_INDEX_0999_JSON",
        expected_response_date="20260720",
        family="quote",
        logical_group="quote-0999",
        attempt_number=1,
        params={"date": "20260720"},
    )

    assert frames == []
    assert attempt["status"] == "failed"
    assert attempt["status_code"] == status_code
    assert expected_error in attempt["error"]
    assert attempt["raw_bytes"] == len(payload.encode("utf-8"))
    assert attempt["raw_sha256"] == hashlib.sha256(payload.encode("utf-8")).hexdigest()
    assert attempt["normalized_sha256"] == attempt["raw_sha256"]


def test_extract_official_response_date_from_roc_json_title() -> None:
    payload = '{"title":"115年07月20日 上市權證每日成交資訊","data":[]}'
    assert warrant_fetch.extract_official_response_dates(payload) == ["20260720"]


def test_response_date_extractor_ignores_dates_inside_data_rows() -> None:
    payload = (
        '{"title":"上市認購(售)權證每日收盤行情資訊彙總表 115年07月20日",'
        '"data":[["030001","114年01月03日","2030/12/31"]]}'
    )
    assert warrant_fetch.extract_official_response_dates(payload) == ["20260720"]
