from __future__ import annotations

import csv
import json
import os
import subprocess
from pathlib import Path

import pytest

from scripts import daily_authority_release as authority
from scripts import market_session_calendar as market_session
from scripts import validate_recent_daily_price_repair_staged_paths as repair_staged_paths


BASE_SHA = "a" * 40


def _market(*, status: str = "open_confirmed", phase: str = "confirm") -> dict[str, object]:
    return {
        "schema_version": 1,
        "generated_at": "2026-08-11T19:47:14+08:00",
        "phase": phase,
        "assessment_date": "20260811",
        "market_session_date": "20260811",
        "market_status": status,
        "expected_main_price_date": "20260811",
        "should_run_daily_pipeline": True,
        "reason_code": (
            "twse_tpex_target_date_confirmed"
            if status == "open_confirmed"
            else "awaiting_official_price_confirmation"
        ),
        "reason": "test",
        "official_sources": {},
        "scheduled_non_trading_days": [],
        "exceptional_non_trading_days": [],
        "price_confirmation": {},
    }


def _write_surfaces(root: Path, market: dict[str, object]) -> None:
    latest = root / "output" / "latest"
    latest.mkdir(parents=True, exist_ok=True)
    (latest / "market_session_status_latest.json").write_text(
        json.dumps(market),
        encoding="utf-8",
    )
    with (latest / "data_freshness_latest.csv").open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=[
                "market_session_status",
                "market_session_date",
                "expected_main_price_date",
                "market_session_reason_code",
                "market_session_generated_at",
                "main_price_date",
                "report_ready",
                "daily_pdf_ready",
            ],
        )
        writer.writeheader()
        writer.writerow(
            {
                "market_session_status": market["market_status"],
                "market_session_date": market["market_session_date"],
                "expected_main_price_date": market["expected_main_price_date"],
                "market_session_reason_code": market["reason_code"],
                "market_session_generated_at": market["generated_at"],
                "main_price_date": "20260811",
                "report_ready": "True",
                "daily_pdf_ready": "True",
            }
        )
    (latest / "data_freshness_latest.md").write_text("# Data Freshness\n", encoding="utf-8")


def test_confirmed_state_cannot_downgrade_to_same_day_preflight() -> None:
    previous = _market()
    candidate = _market(status="unknown", phase="preflight")

    errors = market_session.market_session_transition_errors(previous, candidate)

    assert any("terminal market session state cannot transition" in error for error in errors)
    assert any("phase cannot move backward" in error for error in errors)


def test_recent_repair_staged_paths_forbid_authoritative_market_surface() -> None:
    assert not repair_staged_paths._is_allowed(
        "output/latest/market_session_status_latest.json"
    )
    errors = repair_staged_paths.validate_entries(
        [("M", ("output/latest/market_session_status_latest.json",))]
    )
    assert errors == [
        "recent daily-price repair staged path is not allowed: "
        "output/latest/market_session_status_latest.json"
    ]


def test_runtime_contract_registers_every_authority_publisher_write_surface() -> None:
    contract_path = authority.ROOT / "config" / "runtime_file_lineage_contract.csv"
    with contract_path.open("r", encoding="utf-8-sig", newline="") as handle:
        rows = list(csv.DictReader(handle))
    row = next(item for item in rows if item["script_path"] == "scripts/daily_authority_release.py")

    assert set(row["required_read_artifacts"].split(";")) == {
        path.as_posix()
        for path in (
            authority.MARKET_SESSION_PATH,
            authority.FRESHNESS_CSV_PATH,
            authority.FRESHNESS_MD_PATH,
        )
    }
    assert set(row["required_write_prefixes"].split(";")) == {
        path.as_posix() for path in authority.AUTHORITY_PATHS
    }


def test_market_session_writer_rejects_downgrade_without_replacing_bytes(tmp_path: Path) -> None:
    _write_surfaces(tmp_path, _market())
    path = tmp_path / authority.MARKET_SESSION_PATH
    before = path.read_bytes()

    with pytest.raises(market_session.MarketSessionError, match="terminal market session state"):
        market_session.write_market_session_status(
            tmp_path,
            _market(status="unknown", phase="preflight"),
        )

    assert path.read_bytes() == before


def test_market_session_rejects_same_day_generated_at_regression() -> None:
    previous = _market()
    candidate = _market()
    candidate["generated_at"] = "2026-08-11T19:46:14+08:00"

    errors = market_session.market_session_transition_errors(previous, candidate)

    assert any("generated_at cannot move backward" in error for error in errors)


def test_market_session_rejects_new_date_with_older_generated_at() -> None:
    previous = _market()
    candidate = _market()
    candidate["market_session_date"] = "20260812"
    candidate["expected_main_price_date"] = "20260812"
    candidate["generated_at"] = "2026-08-11T19:46:14+08:00"

    errors = market_session.market_session_transition_errors(previous, candidate)

    assert any("generated_at cannot move backward" in error for error in errors)


def test_authority_release_publishes_all_surfaces_with_one_identity(tmp_path: Path) -> None:
    previous = _market(status="unknown", phase="preflight")
    _write_surfaces(tmp_path, _market())

    manifest = authority.publish_authority_release(
        tmp_path,
        release_id="daily-authority-20260811-test-1",
        producer="daily_full_pipeline",
        base_commit_sha=BASE_SHA,
        previous_market=previous,
    )

    validated = authority.validate_authority_release(
        tmp_path,
        expected_release_id="daily-authority-20260811-test-1",
    )
    assert validated == manifest
    market = authority.read_json(tmp_path / authority.MARKET_SESSION_PATH)
    _, freshness = authority.read_single_csv(tmp_path / authority.FRESHNESS_CSV_PATH)
    assert market["authority_release_id"] == freshness["authority_release_id"]
    assert market["authority_release_id"] == manifest["release_id"]
    assert set(manifest["surfaces"]) == {
        authority.MARKET_SESSION_PATH.as_posix(),
        authority.FRESHNESS_CSV_PATH.as_posix(),
        authority.FRESHNESS_MD_PATH.as_posix(),
    }


def test_authority_release_rejects_cross_surface_mismatch(tmp_path: Path) -> None:
    _write_surfaces(tmp_path, _market())
    csv_path = tmp_path / authority.FRESHNESS_CSV_PATH
    text = csv_path.read_text(encoding="utf-8-sig").replace("open_confirmed", "unknown")
    csv_path.write_text(text, encoding="utf-8-sig")

    with pytest.raises(authority.DailyAuthorityReleaseError, match="surface mismatch"):
        authority.publish_authority_release(
            tmp_path,
            release_id="daily-authority-20260811-test-2",
            producer="daily_full_pipeline",
            base_commit_sha=BASE_SHA,
            previous_market=_market(status="unknown", phase="preflight"),
        )


def test_authority_release_rolls_back_every_surface_after_partial_replace(tmp_path: Path) -> None:
    _write_surfaces(tmp_path, _market())
    paths = (
        authority.MARKET_SESSION_PATH,
        authority.FRESHNESS_CSV_PATH,
        authority.FRESHNESS_MD_PATH,
    )
    before = {path: (tmp_path / path).read_bytes() for path in paths}

    with pytest.raises(authority.DailyAuthorityReleaseError, match="injected partial"):
        authority.publish_authority_release(
            tmp_path,
            release_id="daily-authority-20260811-test-3",
            producer="daily_full_pipeline",
            base_commit_sha=BASE_SHA,
            previous_market=_market(status="unknown", phase="preflight"),
            fail_after_replace=2,
        )

    assert {(path): (tmp_path / path).read_bytes() for path in paths} == before
    assert not (tmp_path / authority.RELEASE_MANIFEST_PATH).exists()


def test_authority_release_recovers_after_uncaught_hard_crash_boundary(tmp_path: Path) -> None:
    _write_surfaces(tmp_path, _market())
    paths = (
        authority.MARKET_SESSION_PATH,
        authority.FRESHNESS_CSV_PATH,
        authority.FRESHNESS_MD_PATH,
    )
    before = {path: (tmp_path / path).read_bytes() for path in paths}
    replace_count = 0

    def crash_after_second_replace(source: Path, target: Path) -> None:
        nonlocal replace_count
        os.replace(source, target)
        replace_count += 1
        if replace_count == 2:
            raise KeyboardInterrupt("simulated process termination")

    with pytest.raises(KeyboardInterrupt, match="simulated process termination"):
        authority.publish_authority_release(
            tmp_path,
            release_id="daily-authority-20260811-crash-test",
            producer="daily_full_pipeline",
            base_commit_sha=BASE_SHA,
            previous_market=_market(status="unknown", phase="preflight"),
            replace=crash_after_second_replace,
        )

    assert (tmp_path / authority.TRANSACTION_DIR_PATH).is_dir()
    assert authority.recover_interrupted_authority_release(tmp_path) is True
    assert {path: (tmp_path / path).read_bytes() for path in paths} == before
    assert not (tmp_path / authority.RELEASE_MANIFEST_PATH).exists()


def test_authority_transaction_fsyncs_preparation_directory_before_activation(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    _write_surfaces(tmp_path, _market())
    synced: list[Path] = []
    monkeypatch.setattr(authority, "_fsync_directory", lambda path: synced.append(Path(path)))

    authority.publish_authority_release(
        tmp_path,
        release_id="daily-authority-20260811-durable-test",
        producer="daily_full_pipeline",
        base_commit_sha=BASE_SHA,
        previous_market=_market(status="unknown", phase="preflight"),
    )

    preparation_index = next(
        index for index, path in enumerate(synced) if ".preparing." in path.name
    )
    transaction_parent_index = next(
        index
        for index, path in enumerate(synced)
        if index > preparation_index and path == tmp_path / "output" / "latest"
    )
    assert preparation_index < transaction_parent_index


def test_authority_release_discards_inactive_preparation_without_surface_drift(tmp_path: Path) -> None:
    _write_surfaces(tmp_path, _market())
    before = {
        path: (tmp_path / path).read_bytes()
        for path in (
            authority.MARKET_SESSION_PATH,
            authority.FRESHNESS_CSV_PATH,
            authority.FRESHNESS_MD_PATH,
        )
    }
    preparing = tmp_path / authority.TRANSACTION_DIR_PATH
    preparing = preparing.with_name(f"{preparing.name}.preparing.abandoned")
    preparing.mkdir()
    (preparing / "candidate-0.bin").write_bytes(b"incomplete")

    assert authority.recover_interrupted_authority_release(tmp_path) is False
    assert not preparing.exists()
    assert {
        path: (tmp_path / path).read_bytes()
        for path in (
            authority.MARKET_SESSION_PATH,
            authority.FRESHNESS_CSV_PATH,
            authority.FRESHNESS_MD_PATH,
        )
    } == before


def test_authority_release_rejects_manifest_semantic_drift(tmp_path: Path) -> None:
    _write_surfaces(tmp_path, _market())
    authority.publish_authority_release(
        tmp_path,
        release_id="daily-authority-20260811-semantic-test",
        producer="daily_full_pipeline",
        base_commit_sha=BASE_SHA,
        previous_market=_market(status="unknown", phase="preflight"),
    )
    manifest_path = tmp_path / authority.RELEASE_MANIFEST_PATH
    manifest = authority.read_json(manifest_path)
    manifest["market_status"] = "unknown"
    manifest_path.write_bytes(authority.json_bytes(manifest))

    with pytest.raises(authority.DailyAuthorityReleaseError, match="manifest semantic mismatch"):
        authority.validate_authority_release(tmp_path)


def test_authority_release_rejects_unregistered_publisher(tmp_path: Path) -> None:
    _write_surfaces(tmp_path, _market())

    with pytest.raises(authority.DailyAuthorityReleaseError, match="producer must be daily_full_pipeline"):
        authority.publish_authority_release(
            tmp_path,
            release_id="daily-authority-20260811-publisher-test",
            producer="repair_recent_daily_price_gaps",
            base_commit_sha=BASE_SHA,
            previous_market=_market(status="unknown", phase="preflight"),
        )


def test_authority_release_rejects_unknown_manifest_schema(tmp_path: Path) -> None:
    _write_surfaces(tmp_path, _market())
    authority.publish_authority_release(
        tmp_path,
        release_id="daily-authority-20260811-schema-test",
        producer="daily_full_pipeline",
        base_commit_sha=BASE_SHA,
        previous_market=_market(status="unknown", phase="preflight"),
    )
    manifest_path = tmp_path / authority.RELEASE_MANIFEST_PATH
    manifest = authority.read_json(manifest_path)
    manifest["schema_version"] = "daily_authority_release_v999"
    manifest_path.write_bytes(authority.json_bytes(manifest))

    with pytest.raises(authority.DailyAuthorityReleaseError, match="schema version"):
        authority.validate_authority_release(tmp_path)


def test_staged_authority_release_rejects_manifest_base_other_than_head(tmp_path: Path) -> None:
    subprocess.run(["git", "init"], cwd=tmp_path, check=True, capture_output=True)
    subprocess.run(["git", "config", "user.name", "test"], cwd=tmp_path, check=True)
    subprocess.run(["git", "config", "user.email", "test@example.invalid"], cwd=tmp_path, check=True)
    _write_surfaces(tmp_path, _market())
    subprocess.run(["git", "add", "output/latest"], cwd=tmp_path, check=True)
    subprocess.run(["git", "commit", "-m", "baseline"], cwd=tmp_path, check=True, capture_output=True)
    authority.publish_authority_release(
        tmp_path,
        release_id="daily-authority-20260811-staged-head-test",
        producer="daily_full_pipeline",
        base_commit_sha=BASE_SHA,
        previous_market=_market(status="unknown", phase="preflight"),
    )
    subprocess.run(["git", "add", "output/latest"], cwd=tmp_path, check=True)

    with pytest.raises(authority.DailyAuthorityReleaseError, match="base SHA must equal current HEAD"):
        authority.validate_staged_authority_release(
            tmp_path,
            expected_release_id="daily-authority-20260811-staged-head-test",
        )


def test_staged_authority_release_rechecks_transition_against_head(tmp_path: Path) -> None:
    subprocess.run(["git", "init"], cwd=tmp_path, check=True, capture_output=True)
    subprocess.run(["git", "config", "user.name", "test"], cwd=tmp_path, check=True)
    subprocess.run(["git", "config", "user.email", "test@example.invalid"], cwd=tmp_path, check=True)
    _write_surfaces(tmp_path, _market())
    subprocess.run(["git", "add", "output/latest"], cwd=tmp_path, check=True)
    subprocess.run(["git", "commit", "-m", "confirmed baseline"], cwd=tmp_path, check=True, capture_output=True)
    head = authority.git_head_sha(tmp_path)
    _write_surfaces(tmp_path, _market(status="unknown", phase="preflight"))
    authority.publish_authority_release(
        tmp_path,
        release_id="daily-authority-20260811-staged-transition-test",
        producer="daily_full_pipeline",
        base_commit_sha=head,
        previous_market=_market(status="unknown", phase="preflight"),
    )
    subprocess.run(["git", "add", "output/latest"], cwd=tmp_path, check=True)

    with pytest.raises(authority.DailyAuthorityReleaseError, match="forbidden market-session transition"):
        authority.validate_staged_authority_release(
            tmp_path,
            expected_release_id="daily-authority-20260811-staged-transition-test",
        )
