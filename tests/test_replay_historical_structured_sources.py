from __future__ import annotations

import json
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


def test_optional_high_water_date_keeps_empty_legacy_mode_and_validates_nonempty() -> None:
    assert replay.parse_optional_date("", "--price-history-high-water-date") == ""
    assert (
        replay.parse_optional_date("20260728", "--price-history-high-water-date")
        == "20260728"
    )
    with pytest.raises(RuntimeError, match="calendar-valid"):
        replay.parse_optional_date("20260230", "--price-history-high-water-date")


def test_daily_price_high_water_requires_identical_canonical_and_legacy_pair(
    tmp_path: Path,
    monkeypatch,
) -> None:
    monkeypatch.chdir(tmp_path)
    price_dir = tmp_path / "data" / "daily_price"
    price_dir.mkdir(parents=True)
    frame = pd.DataFrame(
        [
            {"date": "20260728", "stock_id": "2330", "close": "100"},
            {"date": "20260728", "stock_id": "2317", "close": "90"},
        ]
    )
    frame.to_csv(price_dir / "daily_price_20260728.csv", index=False)
    frame.iloc[::-1].to_csv(price_dir / "20260728.csv", index=False)

    hashes = replay.validate_daily_price_canonical_legacy_pair("20260728")

    assert len(hashes) == 2
    assert len(set(hashes.values())) == 1


def test_daily_price_high_water_rejects_missing_or_different_legacy_pair(
    tmp_path: Path,
    monkeypatch,
) -> None:
    monkeypatch.chdir(tmp_path)
    price_dir = tmp_path / "data" / "daily_price"
    price_dir.mkdir(parents=True)
    frame = pd.DataFrame(
        [{"date": "20260728", "stock_id": "2330", "close": "100"}]
    )
    frame.to_csv(price_dir / "daily_price_20260728.csv", index=False)

    with pytest.raises(RuntimeError, match="pair is missing"):
        replay.validate_daily_price_canonical_legacy_pair("20260728")

    changed = frame.copy()
    changed["close"] = "101"
    changed.to_csv(price_dir / "20260728.csv", index=False)
    with pytest.raises(RuntimeError, match="content mismatch"):
        replay.validate_daily_price_canonical_legacy_pair("20260728")


def _prepare_stock_history_coverage_case(
    tmp_path: Path,
    monkeypatch,
    manifest_end_date: str,
) -> None:
    monkeypatch.chdir(tmp_path)
    history_dir = tmp_path / "data" / "stock_price_history"
    history_dir.mkdir(parents=True)
    pd.DataFrame(
        [
            {"date": "20260720", "stock_id": "2330"},
            {"date": "20260724", "stock_id": "2330"},
        ]
    ).to_csv(history_dir / "2330.csv", index=False)
    manifest = tmp_path / "stock_price_history_manifest.csv"
    pd.DataFrame([{"stock_id": "2330", "end_date": manifest_end_date}]).to_csv(
        manifest,
        index=False,
    )
    monkeypatch.setattr(replay, "STOCK_HISTORY_MANIFEST", manifest)
    monkeypatch.setattr(replay, "supported_daily_stock_ids", lambda target_date: ["2330"])


def test_preserved_target_coverage_accepts_manifest_end_between_target_and_high_water(
    tmp_path: Path,
    monkeypatch,
) -> None:
    _prepare_stock_history_coverage_case(tmp_path, monkeypatch, "20260724")

    result = replay.validate_stock_history_date_coverage(
        "20260720",
        manifest_end_date="20260728",
    )

    assert result["supported_stock_count"] == 1
    assert result["manifest_end_date_lower_bound"] == "20260720"
    assert result["manifest_end_date_upper_bound"] == "20260728"


@pytest.mark.parametrize("manifest_end_date", ["20260717", "20260729"])
def test_preserved_target_coverage_rejects_manifest_end_outside_target_high_water_bounds(
    tmp_path: Path,
    monkeypatch,
    manifest_end_date: str,
) -> None:
    _prepare_stock_history_coverage_case(tmp_path, monkeypatch, manifest_end_date)

    with pytest.raises(RuntimeError, match="outside target/high-water bounds"):
        replay.validate_stock_history_date_coverage(
            "20260720",
            manifest_end_date="20260728",
        )


def test_preserve_price_replay_refetches_but_skips_raw_and_history_writers(monkeypatch) -> None:
    frame = pd.DataFrame(
        [
            {
                "date": "20260720",
                "stock_id": "2330",
                "source": "TWSE",
            }
        ]
    )
    monkeypatch.setattr(replay.price_fetcher, "MAX_WORKERS", 8)
    monkeypatch.setattr(replay.price_fetcher, "reset_fetch_response_provenance", lambda: None)
    monkeypatch.setattr(
        replay.price_fetcher,
        "fetch_response_provenance",
        lambda: [
            {
                "source_name": "TWSE",
                "exact_date_match": True,
                "observed_response_dates": ["20260720"],
            }
        ],
    )
    monkeypatch.setattr(
        replay.price_repair,
        "fetch_with_retry",
        lambda *args, **kwargs: (frame, {"full_market_ok": True}, []),
    )
    monkeypatch.setattr(
        replay.price_repair,
        "write_daily_price_files",
        lambda *args, **kwargs: pytest.fail("preserve mode wrote raw daily prices"),
    )
    monkeypatch.setattr(
        replay,
        "run_checked",
        lambda *args, **kwargs: pytest.fail("preserve mode rebuilt stock histories"),
    )
    monkeypatch.setattr(
        replay,
        "validate_preserved_price_target_slices",
        lambda *args, **kwargs: {"mode": "preserve_existing_price_history"},
    )
    monkeypatch.setattr(
        replay,
        "write_price_status",
        lambda *args, **kwargs: {"future_rows_used": False},
    )
    monkeypatch.setattr(
        replay,
        "validate_stock_history_date_coverage",
        lambda *args, **kwargs: {"supported_stock_count": 1},
    )

    result = replay.replay_price_date("20260720", "20260728")

    assert result["stock_history_coverage"] == {"supported_stock_count": 1}


def _baseline_matrix(
    structured_date: str,
    price_history_high_water_date: str,
    *,
    tpex_date: str | None = None,
) -> dict:
    market_tail = {
        "TWSE": structured_date,
        "TPEX": tpex_date or structured_date,
    }
    return {
        "daily_price": price_history_high_water_date,
        "stock_price_history": {"max_date": price_history_high_water_date},
        "market_index": market_tail.copy(),
        "market_index_ohlc": market_tail.copy(),
        "taifex": {
            "institutional_fo": structured_date,
            "futures_contracts": structured_date,
            "options_call_put": structured_date,
            "put_call_ratio": structured_date,
            "taiwan_vix": structured_date,
        },
        "warrant_daily": structured_date,
        "warrant_flow": structured_date,
    }


def _operational_taifex_base_matrix(
    structured_date: str,
    previous_structured_date: str,
    price_history_high_water_date: str,
) -> dict:
    matrix = _baseline_matrix(structured_date, price_history_high_water_date)
    for source_id in replay.TAIFEX_DATED_RAW_SOURCE_IDS:
        matrix["taifex"][source_id] = previous_structured_date
    return matrix


def test_contiguous_replay_baseline_accepts_aligned_structured_tail(
    monkeypatch,
) -> None:
    monkeypatch.setattr(
        replay,
        "validate_daily_price_canonical_legacy_pair",
        lambda *_: None,
    )
    monkeypatch.setattr(
        replay,
        "validate_stock_history_date_coverage",
        lambda *_, **__: {},
    )

    replay.validate_exact_baseline(
        _baseline_matrix("20260724", "20260729"),
        "20260724",
        "20260729",
    )


def test_taifex_base_repair_accepts_only_explicit_operational_baseline(
    monkeypatch,
) -> None:
    monkeypatch.setattr(
        replay,
        "validate_daily_price_canonical_legacy_pair",
        lambda *_: None,
    )
    monkeypatch.setattr(
        replay,
        "validate_stock_history_date_coverage",
        lambda *_, **__: {},
    )
    matrix = _operational_taifex_base_matrix(
        "20260728",
        "20260727",
        "20260730",
    )

    replay.validate_exact_baseline(
        matrix,
        "20260728",
        "20260730",
        repair_taifex_base_date="20260728",
    )

    with pytest.raises(RuntimeError, match="expected all 20260728"):
        replay.validate_exact_baseline(
            matrix,
            "20260728",
            "20260730",
        )


@pytest.mark.parametrize(
    ("mutation", "expected"),
    [
        ("dated_d2", "expected source-specific base"),
        ("dated_mixed", "expected source-specific base"),
        ("vix_d1", "expected source-specific base"),
        ("missing_source", "source set mismatch"),
    ],
)
def test_taifex_base_repair_baseline_mutations_fail_closed(
    mutation: str,
    expected: str,
) -> None:
    matrix = _operational_taifex_base_matrix(
        "20260728",
        "20260727",
        "20260730",
    )
    if mutation == "dated_d2":
        for source_id in replay.TAIFEX_DATED_RAW_SOURCE_IDS:
            matrix["taifex"][source_id] = "20260724"
    elif mutation == "dated_mixed":
        matrix["taifex"][replay.TAIFEX_DATED_RAW_SOURCE_IDS[0]] = "20260728"
    elif mutation == "vix_d1":
        matrix["taifex"]["taiwan_vix"] = "20260727"
    else:
        del matrix["taifex"]["taiwan_vix"]

    errors = replay.baseline_matrix_errors(
        matrix,
        "20260728",
        "20260730",
        repair_taifex_base_date="20260728",
    )

    assert any(expected in error for error in errors)


def test_taifex_base_repair_rejects_missing_high_water_and_conflicting_repairs() -> None:
    matrix = _operational_taifex_base_matrix(
        "20260728",
        "20260727",
        "20260728",
    )

    missing_high_water = replay.baseline_matrix_errors(
        matrix,
        "20260728",
        repair_taifex_base_date="20260728",
    )
    conflicting = replay.baseline_matrix_errors(
        matrix,
        "20260728",
        "20260728",
        "20260728",
        "20260728",
    )

    assert any("requires price_history_high_water_date" in error for error in missing_high_water)
    assert any("mutually exclusive" in error for error in conflicting)
    assert any("later than required_base_date" in error for error in conflicting)


def test_contiguous_replay_baseline_rejects_structured_tail_drift(monkeypatch) -> None:
    monkeypatch.setattr(
        replay,
        "validate_daily_price_canonical_legacy_pair",
        lambda *_: None,
    )
    monkeypatch.setattr(
        replay,
        "validate_stock_history_date_coverage",
        lambda *_, **__: {},
    )
    matrix = _baseline_matrix("20260724", "20260729")
    matrix["warrant_flow"] = "20260723"

    with pytest.raises(RuntimeError, match="warrant_flow=20260723"):
        replay.validate_exact_baseline(
            matrix,
            "20260724",
            "20260729",
        )


def test_tpex_base_repair_baseline_remains_supported(monkeypatch) -> None:
    monkeypatch.setattr(
        replay,
        "validate_daily_price_canonical_legacy_pair",
        lambda *_: None,
    )
    monkeypatch.setattr(
        replay,
        "validate_stock_history_date_coverage",
        lambda *_, **__: {},
    )

    replay.validate_exact_baseline(
        _baseline_matrix("20260717", "20260729", tpex_date="20260716"),
        "20260717",
        "20260729",
        "20260717",
    )


def test_tpex_base_repair_date_must_match_derived_baseline(monkeypatch) -> None:
    monkeypatch.setattr(
        replay,
        "validate_daily_price_canonical_legacy_pair",
        lambda *_: None,
    )
    monkeypatch.setattr(
        replay,
        "validate_stock_history_date_coverage",
        lambda *_, **__: {},
    )

    with pytest.raises(RuntimeError, match="base_repair_date=20260717 expected=20260724"):
        replay.validate_exact_baseline(
            _baseline_matrix("20260724", "20260729"),
            "20260724",
            "20260729",
            "20260717",
        )


def test_price_history_high_water_allows_end_date_equality() -> None:
    replay.validate_price_history_high_water_date("20260729", "20260729")

    with pytest.raises(RuntimeError, match="same as or later"):
        replay.validate_price_history_high_water_date("20260729", "20260728")


def test_taifex_base_repair_window_requires_prev_high_water_end() -> None:
    replay.validate_taifex_base_repair_window(
        "20260729",
        "20260730",
        "20260728",
        "20260728",
    )

    with pytest.raises(RuntimeError, match="must end at the trading date before"):
        replay.validate_taifex_base_repair_window(
            "20260730",
            "20260730",
            "20260728",
            "20260728",
        )
    with pytest.raises(RuntimeError, match="must equal the replay required base"):
        replay.validate_taifex_base_repair_window(
            "20260729",
            "20260730",
            "20260727",
            "20260728",
        )


def test_recorded_baseline_validation_does_not_read_live_post_replay_history(
    monkeypatch,
) -> None:
    monkeypatch.setattr(
        replay,
        "validate_stock_history_date_coverage",
        lambda *_, **__: pytest.fail("recorded baseline validation read live history"),
    )

    assert replay.baseline_matrix_errors(
        _baseline_matrix("20260724", "20260724"),
        "20260724",
    ) == []


def test_mixed_tail_contract_keeps_price_history_high_water_and_other_sources_at_day() -> None:
    matrix = {
        "daily_price": "20260728",
        "stock_price_history": {"max_date": "20260728"},
        "market_index": {"TWSE": "20260724", "TPEX": "20260724"},
        "market_index_ohlc": {"TWSE": "20260724", "TPEX": "20260724"},
        "taifex": {"a": "20260724", "b": "20260724"},
        "warrant_daily": "20260724",
        "warrant_flow": "20260724",
    }

    replay.validate_replay_day_tail_matrix(matrix, "20260724", "20260728")

    matrix["warrant_flow"] = "20260723"
    with pytest.raises(RuntimeError, match="day tail mismatch"):
        replay.validate_replay_day_tail_matrix(matrix, "20260724", "20260728")


def _valid_manifest_source_row(source_id: str, target_date: str) -> dict:
    return {
        "source_id": source_id,
        "requested_dates": [target_date],
        "observed_dates": [target_date],
        "pk_unique": True,
        "fallback_used": False,
        "future_rows_used": False,
        "raw_sha256": "a" * 64,
        "normalized_sha256": "b" * 64,
        "output_sha256": "c" * 64,
    }


def test_taifex_base_repair_evidence_binds_preserved_tails_and_vix_slice(
    monkeypatch,
) -> None:
    before = _operational_taifex_base_matrix(
        "20260728",
        "20260727",
        "20260730",
    )
    after = _baseline_matrix("20260728", "20260730")
    protected = {"daily_price": {"aggregate_sha256": "d" * 64}}
    monkeypatch.setattr(
        replay,
        "manifest_source_row",
        lambda source_id, target_date, *args, **kwargs: _valid_manifest_source_row(
            source_id,
            target_date,
        ),
    )
    monkeypatch.setattr(replay, "git_output", lambda *args: "e" * 40)

    evidence = replay.build_taifex_base_repair_evidence(
        "github-run-123-1",
        "20260728",
        before,
        after,
        {"sources": {}},
        price_history_high_water_date="20260730",
        vix_base_slice_sha256_before="f" * 64,
        vix_base_slice_sha256_after="f" * 64,
        protected_price_history_fingerprints_before=protected,
        protected_price_history_fingerprints_after=protected,
    )

    assert evidence["report_date"] == "20260728"
    assert evidence["before_tail_matrix"] == before
    assert evidence["after_tail_matrix"] == after
    assert evidence["sources"] == [
        _valid_manifest_source_row("taifex_futures_options_vix", "20260728")
    ]


def test_taifex_base_repair_evidence_rejects_non_taifex_or_vix_drift() -> None:
    before = _operational_taifex_base_matrix(
        "20260728",
        "20260727",
        "20260730",
    )
    after = _baseline_matrix("20260728", "20260730")
    after["warrant_flow"] = "20260729"

    with pytest.raises(RuntimeError, match="non-TAIFEX source tail"):
        replay.build_taifex_base_repair_evidence(
            "github-run-123-1",
            "20260728",
            before,
            after,
            {"sources": {}},
            price_history_high_water_date="20260730",
            vix_base_slice_sha256_before="f" * 64,
            vix_base_slice_sha256_after="f" * 64,
            protected_price_history_fingerprints_before={},
            protected_price_history_fingerprints_after={},
        )

    after["warrant_flow"] = "20260728"
    with pytest.raises(RuntimeError, match="VIX base-date slice"):
        replay.build_taifex_base_repair_evidence(
            "github-run-123-1",
            "20260728",
            before,
            after,
            {"sources": {}},
            price_history_high_water_date="20260730",
            vix_base_slice_sha256_before="f" * 64,
            vix_base_slice_sha256_after="0" * 64,
            protected_price_history_fingerprints_before={},
            protected_price_history_fingerprints_after={},
        )


def test_day_manifest_embeds_taifex_base_repair_evidence(
    tmp_path: Path,
    monkeypatch,
) -> None:
    monkeypatch.setattr(replay, "REPLAY_HISTORY", tmp_path)
    monkeypatch.setattr(replay, "git_output", lambda *args: "e" * 40)
    monkeypatch.setattr(
        replay,
        "manifest_source_row",
        lambda source_id, target_date, *args, **kwargs: _valid_manifest_source_row(
            source_id,
            target_date,
        ),
    )
    embedded = {"schema_version": "historical_structured_source_taifex_base_repair_v1"}

    path = replay.write_day_manifest(
        "github-run-123-1",
        "20260729",
        {},
        {},
        {},
        {},
        {},
        {},
        "20260730",
        {},
        embedded,
    )

    assert json.loads(path.read_text(encoding="utf-8"))[
        "taifex_base_repair_evidence"
    ] == embedded


def test_protected_price_history_fingerprint_drift_fails_closed() -> None:
    before = {"daily_price": {"path_count": 2, "aggregate_sha256": "a" * 64}}
    replay.require_protected_price_history_fingerprints_unchanged(before, before.copy())

    after = {"daily_price": {"path_count": 2, "aggregate_sha256": "b" * 64}}
    with pytest.raises(RuntimeError, match="changed a protected"):
        replay.require_protected_price_history_fingerprints_unchanged(before, after)


def test_refresh_freshness_wires_replay_only_flags_and_keeps_legacy_command_clean(
    tmp_path: Path,
    monkeypatch,
) -> None:
    freshness_csv = tmp_path / "data_freshness_latest.csv"
    pd.DataFrame(
        [
            {
                "main_price_date": "20260724",
                "report_ready": "false",
                "daily_pdf_ready": "false",
            }
        ]
    ).to_csv(freshness_csv, index=False)
    monkeypatch.setattr(replay, "FRESHNESS_CSV", freshness_csv)
    commands: list[list[str]] = []
    monkeypatch.setattr(
        replay,
        "run_checked",
        lambda command, **kwargs: commands.append(command),
    )

    replay.refresh_truthful_freshness("20260724", "20260728")
    replay.refresh_truthful_freshness("20260724", "")

    freshness_builder = "build_data_" + "freshness_latest.py"
    assert commands[0] == [
        replay.sys.executable,
        freshness_builder,
        "--historical-replay-main-price-date",
        "20260724",
        "--expected-price-history-high-water-date",
        "20260728",
    ]
    assert commands[1] == [replay.sys.executable, freshness_builder]


def test_replay_continuity_lookback_covers_long_window_without_narrowing_default() -> None:
    assert replay.replay_continuity_lookback_days("20260718", "20260724") == (
        replay.continuity.DEFAULT_LOOKBACK_DAYS
    )
    assert replay.replay_continuity_lookback_days("20260601", "20260724") == 53


def test_taifex_dated_raw_must_match_committed_history_target_slice(
    tmp_path: Path,
    monkeypatch,
) -> None:
    monkeypatch.chdir(tmp_path)
    history_path = Path("data/futures_options/taifex_institutional_fo_history.csv")
    raw_path = Path("data/futures_options/raw/institutional_fo_20260724.csv")
    history_path.parent.mkdir(parents=True)
    raw_path.parent.mkdir(parents=True)
    frame = pd.DataFrame(
        [{"date": "20260724", "kind": "dealer", "value": "10"}]
    )
    frame.to_csv(history_path, index=False)
    frame.iloc[::-1].to_csv(raw_path, index=False)
    monkeypatch.setattr(
        replay,
        "TAIFEX_HISTORY_SPECS",
        {
            "institutional_fo": (history_path, ["date", "kind"]),
            "taiwan_vix": (
                Path("data/futures_options/taiwan_vix_history.csv"),
                ["date"],
            ),
        },
    )
    monkeypatch.setattr(
        replay,
        "TAIFEX_DATED_RAW_SOURCE_IDS",
        ("institutional_fo",),
    )

    parity = replay.validate_taifex_raw_history_parity("20260724")
    assert parity["institutional_fo"]["raw_path"] == raw_path.as_posix()
    assert parity["institutional_fo"]["row_count"] == 1

    changed = frame.copy()
    changed.loc[0, "value"] = "11"
    changed.to_csv(raw_path, index=False)
    with pytest.raises(RuntimeError, match="dated raw/history target-slice mismatch"):
        replay.validate_taifex_raw_history_parity("20260724")


def test_taifex_dated_raw_accepts_history_superset_with_equal_shared_rows(
    tmp_path: Path,
    monkeypatch,
) -> None:
    monkeypatch.chdir(tmp_path)
    target_date = "20260819"
    history_path = Path("data/futures_options/taifex_futures_contracts_history.csv")
    raw_path = Path(f"data/futures_options/raw/futures_contracts_{target_date}.csv")
    history_path.parent.mkdir(parents=True)
    raw_path.parent.mkdir(parents=True)
    shared = pd.DataFrame(
        [
            {
                "日期": target_date,
                "商品名稱": f"臺股期貨{i:02d}",
                "身份別": "自營商",
                "未平倉餘額_多方_口數": str(1000 + i),
            }
            for i in range(66)
        ]
    )
    history_only = pd.DataFrame(
        [
            {
                "日期": target_date,
                "商品名稱": "臺灣中型100期貨",
                "身份別": identity,
                "未平倉餘額_多方_口數": str(2000 + i),
            }
            for i, identity in enumerate(("自營商", "投信", "外資"))
        ]
    )
    shared.to_csv(raw_path, index=False)
    pd.concat([shared, history_only], ignore_index=True).to_csv(history_path, index=False)
    monkeypatch.setattr(
        replay,
        "TAIFEX_HISTORY_SPECS",
        {
            "futures_contracts": (
                history_path,
                ["日期", "商品名稱", "身份別"],
            )
        },
    )
    monkeypatch.setattr(replay, "TAIFEX_DATED_RAW_SOURCE_IDS", ("futures_contracts",))

    parity = replay.validate_taifex_raw_history_parity(target_date)

    evidence = parity["futures_contracts"]
    assert evidence["raw_row_count"] == 66
    assert evidence["history_row_count"] == 69
    assert evidence["shared_row_count"] == 66
    assert evidence["shared_slice_sha256"] == evidence["raw_slice_sha256"]
    assert evidence["history_slice_sha256"] != evidence["raw_slice_sha256"]
    assert evidence["history_only_row_count"] == 3
    assert evidence["history_only_pk_sha256"]
    assert evidence["parity_contract"] == (
        "raw_subset_of_history_with_equal_shared_values"
    )


def test_taifex_dated_raw_rejects_shared_key_value_conflict_in_history_superset(
    tmp_path: Path,
    monkeypatch,
) -> None:
    monkeypatch.chdir(tmp_path)
    target_date = "20260819"
    history_path = Path("data/futures_options/taifex_futures_contracts_history.csv")
    raw_path = Path(f"data/futures_options/raw/futures_contracts_{target_date}.csv")
    history_path.parent.mkdir(parents=True)
    raw_path.parent.mkdir(parents=True)
    raw = pd.DataFrame(
        [
            {
                "日期": target_date,
                "商品名稱": "臺股期貨",
                "身份別": "自營商",
                "未平倉餘額_多方_口數": "1000",
            }
        ]
    )
    history = pd.concat(
        [
            raw.assign(未平倉餘額_多方_口數="1001"),
            pd.DataFrame(
                [
                    {
                        "日期": target_date,
                        "商品名稱": "臺灣中型100期貨",
                        "身份別": "投信",
                        "未平倉餘額_多方_口數": "2000",
                    }
                ]
            ),
        ],
        ignore_index=True,
    )
    raw.to_csv(raw_path, index=False)
    history.to_csv(history_path, index=False)
    monkeypatch.setattr(
        replay,
        "TAIFEX_HISTORY_SPECS",
        {
            "futures_contracts": (
                history_path,
                ["日期", "商品名稱", "身份別"],
            )
        },
    )
    monkeypatch.setattr(replay, "TAIFEX_DATED_RAW_SOURCE_IDS", ("futures_contracts",))

    with pytest.raises(RuntimeError, match="reason=shared_value_conflict"):
        replay.validate_taifex_raw_history_parity(target_date)
