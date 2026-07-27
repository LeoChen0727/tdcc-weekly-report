from __future__ import annotations

from pathlib import Path

import pandas as pd
import pytest

from scripts import replay_historical_structured_sources as replay


def test_target_slice_hash_is_stable_when_later_rows_are_appended(tmp_path: Path) -> None:
    path = tmp_path / "history.csv"
    pd.DataFrame(
        [
            {"date": "20260720", "stock_id": "2330", "close": "100"},
            {"date": "20260721", "stock_id": "2330", "close": "101"},
        ]
    ).to_csv(path, index=False)

    before = replay.build_component_evidence(
        "stock",
        [(path, ["date", "stock_id"], {})],
        "20260720",
    )
    frame = pd.read_csv(path, dtype=str)
    frame.loc[len(frame)] = {"date": "20260724", "stock_id": "2330", "close": "104"}
    frame.to_csv(path, index=False)
    after = replay.build_component_evidence(
        "stock",
        [(path, ["date", "stock_id"], {})],
        "20260720",
    )

    assert before["slice_manifest_sha256"] == after["slice_manifest_sha256"]
    assert before["future_row_count"] == 1
    assert after["future_row_count"] == 2
    assert after["future_rows_excluded_from_slice"] is True


def test_immutable_manifest_rejects_nonidentical_collision(tmp_path: Path) -> None:
    path = tmp_path / "manifest.json"
    replay.write_json_immutable(path, {"replay_id": "run-1", "status": "pass"})
    replay.write_json_immutable(path, {"replay_id": "run-1", "status": "pass"})

    with pytest.raises(RuntimeError, match="immutable replay manifest collision"):
        replay.write_json_immutable(path, {"replay_id": "run-1", "status": "changed"})


def test_tpex_base_repair_routes_only_tpex(monkeypatch) -> None:
    commands: list[list[str]] = []
    monkeypatch.setattr(replay, "run_checked", lambda command, **kwargs: commands.append(command))
    monkeypatch.setattr(replay, "validate_exact_market_date", lambda date, codes: None)
    monkeypatch.setattr(
        replay,
        "read_json",
        lambda path: {
            "requested_date": "20260717",
            "requested_index_codes": ["TPEX"],
            "observed_dates": {"TPEX": "20260717"},
            "fallback_used": False,
            "future_rows_used": False,
        },
    )

    replay.run_market_date("20260717", {"TPEX"})

    assert len(commands) == 1
    assert commands[0][-2:] == ["--target-index-code", "TPEX"]
    assert "TWSE" not in commands[0]


def test_replay_id_is_path_safe() -> None:
    assert replay.parse_replay_id("github-run-123-1") == "github-run-123-1"
    with pytest.raises(RuntimeError, match="--replay-id"):
        replay.parse_replay_id("../escape")


def test_replay_window_excludes_weekend_dates_20260718_and_20260719() -> None:
    assert replay.expected_trading_dates("20260718", "20260724") == [
        "20260720",
        "20260721",
        "20260722",
        "20260723",
        "20260724",
    ]


def test_taifex_manifest_keeps_failed_attempt_evidence_and_accepts_only_exact_success(monkeypatch) -> None:
    failed = {
        "attempt": 1,
        "status": "failed",
        "endpoint": "https://www.taifex.com.tw/cht/3/pcRatioDown",
        "params": {"queryStartDate": "2026/07/20", "queryEndDate": "2026/07/20"},
        "http_status": 200,
        "raw_bytes": 92,
        "raw_sha256": "a" * 64,
        "normalized_sha256": "b" * 64,
        "encoding": "cp950",
        "requested_dates": ["20260720"],
        "observed_dates": [],
        "rows": 0,
        "parse_metadata": {},
        "error": "RuntimeError: header only",
        "fetched_at": "2026-07-27 00:00:00 Asia/Taipei",
    }
    accepted = {
        **failed,
        "attempt": 2,
        "status": "ok",
        "raw_bytes": 143,
        "raw_sha256": "c" * 64,
        "normalized_sha256": "d" * 64,
        "observed_dates": ["20260720"],
        "rows": 1,
        "parse_metadata": {"trimmed_trailing_empty_fields": 1},
        "error": "",
    }
    status = {
        "fallback_used": False,
        "future_rows_used": False,
        "sources": {
            "put_call_ratio": {
                "observed_dates": ["20260720"],
                "provenance": {"attempts": [failed, accepted]},
            }
        },
    }
    monkeypatch.setattr(
        replay,
        "build_source_output_evidence",
        lambda *args, **kwargs: {
            "pk_unique": True,
            "row_count": 1,
            "output_sha256": "e" * 64,
        },
    )

    row = replay.manifest_source_row(
        "taifex_futures_options_vix",
        "20260720",
        status,
        "20260717",
        "20260720",
        observed_dates=["20260720"],
    )

    assert row["source_attempt_count"] == 2
    assert [item["status"] for item in row["source_response_attempts"]] == ["failed", "ok"]
    assert row["source_response_attempts"][0]["raw_sha256"] == "a" * 64
    assert row["source_response_attempts"][1]["parse_metadata"] == {
        "trimmed_trailing_empty_fields": 1
    }
    assert row["accepted_source_response_count"] == 1
    assert row["accepted_source_responses"][0]["raw_sha256"] == "c" * 64


def test_warrant_manifest_keeps_attempts_but_accepts_all_three_logical_groups(monkeypatch) -> None:
    def response(source_name, logical_group, *, accepted, sha):
        return {
            "attempt": 1,
            "source_name": source_name,
            "family": "mapping" if logical_group == "mapping" else "quote",
            "logical_group": logical_group,
            "endpoint": "https://example.invalid/" + source_name,
            "params": {"date": "20260720"},
            "status": "accepted" if accepted else "failed",
            "status_code": 200,
            "raw_bytes": 10,
            "raw_sha256": sha,
            "normalized_sha256": sha,
            "encoding": "utf-8",
            "expected_response_date": "20260720",
            "observed_response_dates": ["20260720"],
            "exact_date_match": True,
            "parsed_table_count": 1,
            "parsed_table_rows": 1,
            "accepted_rows": 1 if accepted else 0,
            "accepted": accepted,
            "error": "" if accepted else "parser produced no usable rows",
            "fetched_at": "2026-07-27 00:00:00 Asia/Taipei",
            "elapsed_seconds": 0.1,
        }

    status = {
        "fallback_used": False,
        "future_rows_used": False,
        "source_responses": [
            response("TWSE_MI_INDEX_0999_JSON", "quote-0999", accepted=False, sha="a" * 64),
            response("TWSE_MI_INDEX_0999_JSON", "quote-0999", accepted=True, sha="b" * 64),
            response("TWSE_MI_INDEX_0999P_JSON", "quote-0999P", accepted=True, sha="c" * 64),
            response("TWSE_WARRANT_STOCK_JSON", "mapping", accepted=True, sha="d" * 64),
        ],
    }
    monkeypatch.setattr(
        replay,
        "build_source_output_evidence",
        lambda *args, **kwargs: {
            "pk_unique": True,
            "row_count": 1,
            "output_sha256": "e" * 64,
        },
    )

    row = replay.manifest_source_row(
        "official_warrant_daily",
        "20260720",
        status,
        "20260717",
        "20260720",
        observed_dates=["20260720"],
    )

    assert row["source_attempt_count"] == 4
    assert len(row["source_response_attempts"]) == 4
    assert row["source_response_attempts"][0]["accepted"] is False
    assert row["source_response_attempts"][0]["logical_group"] == "quote-0999"
    assert row["accepted_source_response_count"] == 3
    assert {item["logical_group"] for item in row["accepted_source_responses"]} == {
        "mapping",
        "quote-0999",
        "quote-0999P",
    }
    assert all(item["accepted"] is True for item in row["accepted_source_responses"])
