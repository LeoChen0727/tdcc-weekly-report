from __future__ import annotations

import csv
import hashlib
import io
import json
import os
import subprocess
from pathlib import Path

import pytest

from scripts import pr_inherited_market_closure as closure


def _json(value: object) -> bytes:
    return (json.dumps(value, sort_keys=True, ensure_ascii=False, indent=2) + "\n").encode()


def _csv(rows: list[dict[str, str]]) -> bytes:
    stream = io.StringIO(newline="")
    writer = csv.DictWriter(stream, fieldnames=list(rows[0]), lineterminator="\n")
    writer.writeheader()
    writer.writerows(rows)
    return stream.getvalue().encode()


def _git(root: Path, *arguments: str) -> str:
    environment = os.environ.copy()
    environment.update(GIT_NO_LAZY_FETCH="1", GIT_NO_REPLACE_OBJECTS="1")
    return subprocess.check_output(["git", "--no-replace-objects", "-C", str(root), *arguments], env=environment).decode().strip()


def _write(root: Path, path: str, payload: bytes) -> None:
    destination = root / path
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_bytes(payload)


def _seal(root: Path) -> None:
    manifest = json.loads((root / closure.MANIFEST_PATH).read_bytes())
    manifest["surfaces"] = {
        path: hashlib.sha256((root / path).read_bytes()).hexdigest()
        for path in (closure.MARKET_PATH, closure.FRESHNESS_PATH, closure.FRESHNESS_MD_PATH)
    }
    _write(root, closure.MANIFEST_PATH, _json(manifest))


def _commit(root: Path) -> str:
    _git(root, "add", ".")
    _git(root, "commit", "--quiet", "--allow-empty", "-m", "fixture")
    return _git(root, "rev-parse", "HEAD")


@pytest.fixture
def repo(tmp_path: Path) -> tuple[Path, str]:
    root = tmp_path / "repository"
    root.mkdir()
    _git(root, "init", "--quiet")
    _git(root, "config", "user.name", "fixture")
    _git(root, "config", "user.email", "fixture@example.invalid")
    _git(root, "config", "core.autocrlf", "false")
    previous = {"market_session_date": "20261021", "expected_main_price_date": "20261021", "generated_at": "2026-10-21T20:00:00+08:00", "market_status": "open_confirmed", "phase": "confirm"}
    for path in closure.INHERITED_SOURCE_PATHS:
        _write(root, path, b"unchanged fixture dependency\n")
    _write(root, closure.MARKET_PATH, _json(previous))
    baseline = _commit(root)
    generated = "2026-10-23T19:56:51+08:00"
    updated = "2026-10-23T19:47:03+08:00"
    release = "daily-authority-20261023-39949390425-1"
    market = {
        "schema_version": 1, "assessment_date": "20261023", "market_session_date": "20261023",
        "expected_main_price_date": "20261022", "generated_at": generated,
        "market_status": "closed_emergency", "phase": "preflight", "price_confirmation": {},
        "should_run_daily_pipeline": False, "reason_code": closure.REASON_CODE, "reason": "臺北市全日停止上班",
        "authority_release_id": release, "authority_generation_id": release,
        "authority_base_commit_sha": baseline, "authority_producer": "daily_full_pipeline",
        "scheduled_non_trading_days": ["20261026"], "exceptional_non_trading_days": ["20261023"],
        "emergency_notice": {"date": "20261023", "scope": "full_day", "summary": "臺北市全日停止上班", "source_url": closure.DGPA_URL, "source_record_id": "dgpa-record-1", "source_updated_at": updated},
        "official_sources": {
            "dgpa_emergency_closure": {"source": "dgpa_emergency_closure", "url": closure.DGPA_URL, "status": "ok", "sha256": "a" * 64, "byte_len": 123, "attempt_count": 1, "queried_at": generated, "conflict_dates": [], "latest_taipei_notice_dates": ["20261023"], "taipei_notice_count": 1},
            "twse_annual_calendar": {"source": "twse_annual_calendar", "url": closure.ANNUAL_URL, "status": "ok", "sha256": "b" * 64, "byte_len": 123, "attempt_count": 1, "queried_at": generated, "covered_years": [2026]},
            "twse_emergency_rule": {"status": "reference", "url": closure.RULE_URL},
        },
    }
    note = "market session is not open_confirmed: market_session_status=closed_emergency"
    fresh = {"market_session_status": "closed_emergency", "market_session_date": "20261023", "expected_main_price_date": "20261022", "market_session_reason_code": closure.REASON_CODE, "market_session_generated_at": generated, "main_price_date": "20261021", "main_price_date_source": "validated_stock_history", "report_ready": "False", "daily_pdf_ready": "False", "report_ready_note": note, "daily_pdf_ready_note": f"core daily data not ready: {note}", "historical_replay_main_price_date": "", "expected_price_history_high_water_date": "", "authority_release_id": release, "authority_generation_id": release, "authority_base_commit_sha": baseline, "authority_producer": "daily_full_pipeline"}
    for field in ("actual_stock_price_history_date", "stock_monitor_price_date", "all_candidates_date", "official_price_fetch_date", "raw_stock_monitor_price_date", "raw_all_candidates_date", "raw_official_price_fetch_date"):
        fresh[field] = "20261021"
    manifest = {"schema_version": "daily_authority_release_v1", "release_id": release, "generation_id": release, "producer": "daily_full_pipeline", "base_commit_sha": baseline, "transition_baseline": {"kind": "git_object", "commit_sha": baseline, "path": closure.MARKET_PATH}}
    for field in ("market_session_date", "expected_main_price_date", "generated_at", "market_status", "reason_code"):
        manifest[field] = market[field]
    _write(root, closure.MARKET_PATH, _json(market))
    _write(root, closure.FRESHNESS_PATH, _csv([fresh]))
    _write(root, closure.FRESHNESS_MD_PATH, b"# Closed emergency, no new report\n")
    _write(root, closure.MANIFEST_PATH, _json(manifest))
    _write(root, closure.SCHEDULED_PATH, _csv([{"date": "20261026", "market": "TWSE_TPEx", "reason": "holiday", "source_url": closure.ANNUAL_URL}]))
    _write(root, closure.EXCEPTIONAL_PATH, _csv([{"date": "20261023", "market_status": "closed_emergency", "market": "TWSE_TPEx", "government_area": "Taipei City", "closure_scope": "full_day", "source_url": closure.DGPA_URL, "source_record_id": "dgpa-record-1", "source_updated_at": updated, "twse_rule_url": closure.RULE_URL, "first_observed_at": generated, "last_observed_at": generated}]))
    _seal(root)
    return root, _commit(root)


def _validate(repo: tuple[Path, str]) -> list[str]:
    root, base = repo
    return closure.validate_inherited_market_closure(base, repository_root=root)


def test_valid_inherited_closure_preserves_false_readiness(repo: tuple[Path, str]) -> None:
    root, _ = repo
    before = {path: (root / path).read_bytes() for path in closure.INHERITED_SOURCE_PATHS}
    assert _validate(repo) == []
    assert closure.is_inherited_market_closure_candidate(root / closure.FRESHNESS_PATH)
    assert {path: (root / path).read_bytes() for path in before} == before


def test_checkout_crlf_only_is_allowed(repo: tuple[Path, str]) -> None:
    root, _ = repo
    for path in closure.INHERITED_SOURCE_PATHS:
        file = root / path
        file.write_bytes(file.read_bytes().replace(b"\n", b"\r\n"))
    assert _validate(repo) == []


def test_sparse_unmaterialized_paths_require_exact_skip_worktree_index(repo: tuple[Path, str]) -> None:
    root, _ = repo
    for path in (closure.MARKET_PATH, closure.FRESHNESS_PATH, closure.EXCEPTIONAL_PATH):
        _git(root, "update-index", "--skip-worktree", "--", path)
        (root / path).unlink()
    assert _validate(repo) == []


@pytest.mark.parametrize("path", closure.INHERITED_SOURCE_PATHS)
def test_every_source_dependency_change_is_rejected(repo: tuple[Path, str], path: str) -> None:
    root, _ = repo
    (root / path).write_bytes(b"changed\n")
    _commit(root)
    assert any("changed from base" in error for error in _validate(repo))


@pytest.mark.parametrize("change", ["unstaged", "staged", "missing", "mode", "deleted_in_head"])
def test_local_or_tree_dependency_drift_fails(repo: tuple[Path, str], change: str) -> None:
    root, _ = repo
    path = "scripts/market_session_calendar.py"
    if change in {"missing", "deleted_in_head"}:
        (root / path).unlink()
        if change == "deleted_in_head":
            _commit(root)
    elif change == "mode":
        _git(root, "update-index", "--chmod=+x", "--", path)
        _git(root, "commit", "--quiet", "-m", "mode")
    else:
        (root / path).write_bytes(b"changed locally\n")
        if change == "staged":
            _git(root, "add", path)
    assert _validate(repo)


def _mutate_json(root: Path, path: str, keys: tuple[str, ...], value: object) -> None:
    document = json.loads((root / path).read_bytes())
    target = document
    for key in keys[:-1]:
        target = target[key]
    target[keys[-1]] = value
    _write(root, path, _json(document))


@pytest.mark.parametrize(("path", "keys", "value", "message"), [
    (closure.MARKET_PATH, ("schema_version",), True, "market schema"),
    (closure.MARKET_PATH, ("market_status",), "unknown", "closed_emergency"),
    (closure.MARKET_PATH, ("should_run_daily_pipeline",), True, "should_run_daily_pipeline"),
    (closure.MARKET_PATH, ("price_confirmation",), {"status": "ok"}, "price confirmation"),
    (closure.MARKET_PATH, ("assessment_date",), "20261022", "assessment"),
    (closure.MARKET_PATH, ("phase",), "invented", "phase"),
    (closure.MARKET_PATH, ("reason_code",), "official_source_unavailable", "reason_code"),
    (closure.MARKET_PATH, ("authority_release_id",), "forged", "identity mismatch"),
    (closure.MARKET_PATH, ("authority_base_commit_sha",), "c" * 40, "base commit mismatch"),
    (closure.MARKET_PATH, ("official_sources", "dgpa_emergency_closure", "status"), "unavailable", "source status"),
    (closure.MARKET_PATH, ("official_sources", "dgpa_emergency_closure", "sha256"), "bad", "SHA-256"),
    (closure.MARKET_PATH, ("official_sources", "dgpa_emergency_closure", "byte_len"), True, "byte_len"),
    (closure.MARKET_PATH, ("official_sources", "dgpa_emergency_closure", "conflict_dates"), ["20261023"], "ambiguous"),
    (closure.MARKET_PATH, ("official_sources", "twse_annual_calendar", "covered_years"), [2025], "cover closure year"),
    (closure.MARKET_PATH, ("official_sources", "twse_emergency_rule", "url"), "https://invalid.example", "rule identity"),
    (closure.MARKET_PATH, ("emergency_notice", "scope"), "afternoon", "notice date/scope"),
    (closure.MARKET_PATH, ("emergency_notice", "source_record_id"), "forged", "calendar mismatch"),
    (closure.MARKET_PATH, ("scheduled_non_trading_days",), [], "scheduled calendar"),
    (closure.MARKET_PATH, ("exceptional_non_trading_days",), [], "exceptional calendar"),
    (closure.MANIFEST_PATH, ("schema_version",), "unknown", "manifest schema"),
    (closure.MANIFEST_PATH, ("producer",), "other", "producer"),
    (closure.MANIFEST_PATH, ("generation_id",), "other", "generation_id"),
    (closure.MANIFEST_PATH, ("transition_baseline", "path"), "other.json", "transition baseline"),
    (closure.MANIFEST_PATH, ("market_session_date",), "20261022", "semantic mismatch"),
])
def test_inherited_but_invalid_authority_semantics_fail_closed(repo: tuple[Path, str], path: str, keys: tuple[str, ...], value: object, message: str) -> None:
    root, _ = repo
    _mutate_json(root, path, keys, value)
    _seal(root)
    invalid_base = _commit(root)
    errors = closure.validate_inherited_market_closure(invalid_base, repository_root=root)
    assert errors and message in errors[0]


@pytest.mark.parametrize(("field", "value"), [
    ("report_ready", "True"), ("daily_pdf_ready", "True"),
    ("report_ready", "false"), ("daily_pdf_ready_note", "fake"),
    ("main_price_date_source", "historical_replay_override"),
    ("historical_replay_main_price_date", "20261021"),
    ("official_price_fetch_date", "20261022"),
    ("authority_generation_id", "other"),
])
def test_invalid_inherited_freshness_is_rejected(repo: tuple[Path, str], field: str, value: str) -> None:
    root, _ = repo
    rows = list(csv.DictReader(io.StringIO((root / closure.FRESHNESS_PATH).read_text())))
    rows[0][field] = value
    _write(root, closure.FRESHNESS_PATH, _csv(rows))
    _seal(root)
    bad_base = _commit(root)
    assert closure.validate_inherited_market_closure(bad_base, repository_root=root)


@pytest.mark.parametrize("kind", ["array", "invalid_json", "duplicate_json_key", "two_freshness_rows", "duplicate_csv_header", "extra_csv_column", "surface_sha", "surface_set", "calendar_duplicate", "missing_closure_calendar", "invalid_date", "naive_timestamp", "missing_baseline"])
def test_bad_shapes_hashes_and_preimage_fail_closed(repo: tuple[Path, str], kind: str) -> None:
    root, _ = repo
    if kind == "array":
        _write(root, closure.MARKET_PATH, b"[]")
    elif kind == "invalid_json":
        _write(root, closure.MARKET_PATH, b"{")
    elif kind == "duplicate_json_key":
        _write(root, closure.MARKET_PATH, b'{"schema_version":1,"schema_version":1}')
    elif kind == "two_freshness_rows":
        rows = list(csv.DictReader(io.StringIO((root / closure.FRESHNESS_PATH).read_text())))
        _write(root, closure.FRESHNESS_PATH, _csv(rows * 2))
    elif kind == "duplicate_csv_header":
        _write(root, closure.FRESHNESS_PATH, b"a,a\n1,2\n")
    elif kind == "extra_csv_column":
        _write(root, closure.FRESHNESS_PATH, b"a,b\n1,2,3\n")
    elif kind in {"surface_sha", "surface_set"}:
        _mutate_json(root, closure.MANIFEST_PATH, ("surfaces",), {} if kind == "surface_set" else {path: "0" * 64 for path in (closure.MARKET_PATH, closure.FRESHNESS_PATH, closure.FRESHNESS_MD_PATH)})
    elif kind in {"calendar_duplicate", "missing_closure_calendar"}:
        rows = list(csv.DictReader(io.StringIO((root / closure.EXCEPTIONAL_PATH).read_text())))
        _write(root, closure.EXCEPTIONAL_PATH, _csv(rows * 2) if kind == "calendar_duplicate" else b"date\n20261022\n")
    elif kind == "invalid_date":
        _mutate_json(root, closure.MARKET_PATH, ("market_session_date",), "20260230")
    elif kind == "naive_timestamp":
        _mutate_json(root, closure.MARKET_PATH, ("generated_at",), "2026-10-23T19:56:51")
    elif kind == "missing_baseline":
        _mutate_json(root, closure.MANIFEST_PATH, ("base_commit_sha",), "f" * 40)
    if kind not in {"surface_sha", "surface_set"}:
        _seal(root)
    bad_base = _commit(root)
    assert closure.validate_inherited_market_closure(bad_base, repository_root=root)


def test_candidate_is_only_a_selector_and_missing_or_other_states_are_false(tmp_path: Path) -> None:
    path = tmp_path / "freshness.csv"
    assert not closure.is_inherited_market_closure_candidate(path)
    for value in (b"[]", b"a,a\n1,2\n", b"market_session_status\nhistorical_replay_override\n", b"market_session_status\nunknown\n"):
        path.write_bytes(value)
        assert not closure.is_inherited_market_closure_candidate(path)


def test_git_calls_disable_replacements_and_lazy_fetch(repo: tuple[Path, str], monkeypatch: pytest.MonkeyPatch) -> None:
    original = subprocess.run
    calls: list[list[str]] = []

    def recording(arguments: list[str], **kwargs: object) -> subprocess.CompletedProcess[bytes]:
        assert arguments[:2] == ["git", "--no-replace-objects"]
        environment = kwargs["env"]
        assert isinstance(environment, dict)
        assert environment["GIT_NO_LAZY_FETCH"] == "1"
        assert environment["GIT_NO_REPLACE_OBJECTS"] == "1"
        calls.append(arguments)
        return original(arguments, **kwargs)

    monkeypatch.setattr(closure.subprocess, "run", recording)
    assert _validate(repo) == []
    assert calls
    assert all("fetch" not in command and "checkout" not in command for command in calls)


def test_invalid_revision_returns_explicit_error(repo: tuple[Path, str]) -> None:
    root, _ = repo
    assert "invalid Git revision" in closure.validate_inherited_market_closure("--help", repository_root=root)[0]
    assert "local Git rev-parse failed" in closure.validate_inherited_market_closure("missing", repository_root=root)[0]


@pytest.mark.parametrize(("previous", "message"), [
    ({"market_session_date": "20261024", "generated_at": "2026-10-21T20:00:00+08:00"}, "session date moves backward"),
    ({"market_session_date": "20261021", "generated_at": "2026-10-24T20:00:00+08:00"}, "generation moves backward"),
    ({"market_session_date": "20261023", "expected_main_price_date": "20261021", "generated_at": "2026-10-23T18:00:00+08:00", "phase": "preflight", "market_status": "unknown"}, "expected date changed"),
    ({"market_session_date": "20261023", "expected_main_price_date": "20261022", "generated_at": "2026-10-23T18:00:00+08:00", "phase": "preflight", "market_status": "open_confirmed"}, "terminal market session changed"),
    ({"market_session_date": "20261023", "expected_main_price_date": "20261022", "generated_at": "2026-10-23T18:00:00+08:00", "phase": "confirm", "market_status": "unknown"}, "phase moves backward"),
])
def test_transition_preimage_cannot_regress(repo: tuple[Path, str], previous: dict[str, str], message: str) -> None:
    root, _ = repo
    payloads = {path: (root / path).read_bytes() for path in closure.INHERITED_SOURCE_PATHS}
    with pytest.raises(closure.ClosureEvidenceError, match=message):
        closure._closure_semantics(payloads, previous)


def test_checkout_symlink_is_rejected(repo: tuple[Path, str], monkeypatch: pytest.MonkeyPatch) -> None:
    root, _ = repo
    original = Path.is_symlink
    monkeypatch.setattr(Path, "is_symlink", lambda path: path == root / closure.FRESHNESS_PATH or original(path))
    assert "symlink checkout is forbidden" in _validate(repo)[0]
