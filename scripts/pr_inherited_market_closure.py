"""Read-only PR evidence for an unchanged, authoritative emergency closure.

This module never declares a source ready. Callers must still compare the exact
runtime failures and enforce their own protected-change boundary.
"""
from __future__ import annotations

import csv
import hashlib
import io
import json
import os
import re
import subprocess
from datetime import datetime, timedelta
from pathlib import Path
from typing import Any

MARKET_PATH = "output/latest/market_session_status_latest.json"
FRESHNESS_PATH = "output/latest/data_freshness_latest.csv"
FRESHNESS_MD_PATH = "output/latest/data_freshness_latest.md"
MANIFEST_PATH = "output/latest/daily_authority_release_latest.json"
EXCEPTIONAL_PATH = "data/market_calendar/exceptional_non_trading_days.csv"
SCHEDULED_PATH = "config/twse_non_trading_days.csv"
INHERITED_SOURCE_PATHS = (
    MARKET_PATH, FRESHNESS_PATH, FRESHNESS_MD_PATH, MANIFEST_PATH,
    EXCEPTIONAL_PATH, SCHEDULED_PATH, "scripts/daily_authority_release.py",
    "scripts/market_session_calendar.py", "build_data_freshness_latest.py",
    "config/external_data_source_contract.csv", ".github/workflows/daily_full_pipeline.yml",
    "scripts/validate_daily_publish_freshness_gate.py",
    "scripts/validate_repo_advanced_integrity.py",
)
DGPA_URL = "https://www.dgpa.gov.tw/typh/daily/nds.html"
ANNUAL_URL = "https://openapi.twse.com.tw/v1/holidaySchedule/holidaySchedule"
RULE_URL = "https://www.twse.com.tw/zh/about/suspended_faq.html"
REASON_CODE = "taipei_full_day_or_morning_work_suspension"


class ClosureEvidenceError(ValueError):
    pass


def _require(condition: bool, message: str) -> None:
    if not condition:
        raise ClosureEvidenceError(message)


def _git(root: Path, *arguments: str) -> bytes:
    environment = os.environ.copy()
    environment.update(GIT_NO_LAZY_FETCH="1", GIT_NO_REPLACE_OBJECTS="1", GIT_OPTIONAL_LOCKS="0")
    result = subprocess.run(
        ["git", "--no-replace-objects", "-C", str(root), *arguments],
        stdout=subprocess.PIPE, stderr=subprocess.PIPE, env=environment, check=False,
    )
    if result.returncode:
        detail = result.stderr.decode("utf-8", errors="replace").strip()
        raise ClosureEvidenceError(f"local Git {arguments[0]} failed: {detail}")
    return result.stdout


def _commit(root: Path, revision: str) -> str:
    _require(bool(revision) and not revision.startswith("-"), "invalid Git revision")
    resolved = _git(root, "rev-parse", "--verify", "--end-of-options", f"{revision}^{{commit}}").decode().strip()
    _require(bool(re.fullmatch(r"[0-9a-f]{40}", resolved)), "Git revision must resolve to a full SHA-1 commit")
    return resolved


def _blob(root: Path, revision: str, path: str) -> tuple[str, bytes]:
    entry = _git(root, "ls-tree", "-z", revision, "--", path)
    _require(entry.count(b"\0") == 1, f"missing or ambiguous Git blob: {revision}:{path}")
    metadata, actual_path = entry[:-1].split(b"\t", 1)
    mode, kind, oid = metadata.decode("ascii").split(" ")
    _require(mode == "100644" and kind == "blob", f"authority dependency must be a 100644 blob: {path}")
    _require(actual_path.decode("utf-8") == path, f"Git blob path mismatch: {path}")
    return oid, _git(root, "cat-file", "blob", oid)


def _tree_entries(root: Path, revision: str) -> dict[str, str]:
    entries = _git(root, "ls-tree", "-z", revision, "--", *INHERITED_SOURCE_PATHS)
    result: dict[str, str] = {}
    for entry in entries.split(b"\0"):
        if not entry:
            continue
        metadata, path_bytes = entry.split(b"\t", 1)
        mode, kind, oid = metadata.decode("ascii").split(" ")
        path = path_bytes.decode("utf-8")
        _require(mode == "100644" and kind == "blob", f"authority dependency must be a 100644 blob: {path}")
        _require(path not in result, f"ambiguous Git blob: {path}")
        result[path] = oid
    _require(set(result) == set(INHERITED_SOURCE_PATHS), f"missing Git source dependencies: {sorted(set(INHERITED_SOURCE_PATHS) - set(result))}")
    return result


def _checkout_matches(root: Path, path: str, oid: str, payload: bytes, *, index_entries: set[bytes], sparse_entries: set[bytes]) -> None:
    expected = f"100644 {oid} 0\t{path}\0".encode()
    _require(expected[:-1] in index_entries, f"index differs from inherited HEAD blob: {path}")
    local = root / path
    _require(not local.is_symlink(), f"symlink checkout is forbidden: {path}")
    if not local.exists():
        _require(f"S {path}".encode() in sparse_entries, f"missing checkout dependency: {path}")
        return
    _require(local.is_file(), f"checkout dependency is not a regular file: {path}")
    _require(
        local.read_bytes().replace(b"\r\n", b"\n") == payload.replace(b"\r\n", b"\n"),
        f"checkout dependency differs beyond LF/CRLF: {path}",
    )


def _pairs(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for key, value in pairs:
        _require(key not in result, f"duplicate JSON key: {key}")
        result[key] = value
    return result


def _json(payload: bytes, label: str) -> dict[str, Any]:
    parsed = json.loads(payload.decode("utf-8-sig"), object_pairs_hook=_pairs)
    _require(isinstance(parsed, dict), f"{label} must be a JSON object")
    return parsed


def _csv(payload: bytes, label: str) -> list[dict[str, str]]:
    reader = csv.DictReader(io.StringIO(payload.decode("utf-8-sig")), strict=True)
    fields = reader.fieldnames or []
    _require(bool(fields) and len(fields) == len(set(fields)), f"invalid or duplicate CSV header: {label}")
    rows = list(reader)
    _require(all(None not in row and all(value is not None for value in row.values()) for row in rows), f"malformed CSV rows: {label}")
    return rows


def _date(value: Any, label: str) -> str:
    _require(isinstance(value, str) and bool(re.fullmatch(r"20\d{6}", value)), f"invalid date: {label}")
    datetime.strptime(value, "%Y%m%d")
    return value


def _timestamp(value: Any, label: str) -> datetime:
    _require(isinstance(value, str) and bool(value), f"missing timestamp: {label}")
    parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
    _require(parsed.tzinfo is not None and parsed.utcoffset() is not None, f"timestamp requires timezone: {label}")
    return parsed


def _sha(value: Any, label: str) -> str:
    _require(isinstance(value, str) and bool(re.fullmatch(r"[0-9a-f]{64}", value)), f"invalid SHA-256: {label}")
    return value


def is_inherited_market_closure_candidate(freshness_path: Path) -> bool:
    """Only select a branch; full authorization is always the validator's job."""
    try:
        rows = _csv(freshness_path.read_bytes(), FRESHNESS_PATH)
        return len(rows) == 1 and rows[0].get("market_session_status") == "closed_emergency"
    except (OSError, ValueError, UnicodeError, csv.Error):
        return False


def _closure_semantics(payloads: dict[str, bytes], previous: dict[str, Any]) -> None:
    market = _json(payloads[MARKET_PATH], MARKET_PATH)
    manifest = _json(payloads[MANIFEST_PATH], MANIFEST_PATH)
    rows = _csv(payloads[FRESHNESS_PATH], FRESHNESS_PATH)
    _require(len(rows) == 1, "freshness must contain exactly one row")
    freshness = rows[0]
    session = _date(market.get("market_session_date"), "market_session_date")
    expected_date = _date(market.get("expected_main_price_date"), "expected_main_price_date")
    generated = _timestamp(market.get("generated_at"), "market.generated_at")
    _require(generated.utcoffset() == timedelta(hours=8) and generated.strftime("%Y%m%d") == session, "closure generation must belong to its Taipei session date")
    _require(type(market.get("schema_version")) is int and market["schema_version"] == 1, "invalid market schema")
    _require(market.get("market_status") == "closed_emergency", "market must remain closed_emergency")
    _require(market.get("assessment_date") == session, "assessment date differs from session")
    _require(market.get("phase") in {"preflight", "confirm"}, "invalid closure phase")
    _require(market.get("should_run_daily_pipeline") is False, "closed market must keep should_run_daily_pipeline false")
    _require(market.get("reason_code") == REASON_CODE, "invalid emergency closure reason_code")
    _require(market.get("price_confirmation") == {}, "closed market must not contain price confirmation")
    release = manifest.get("release_id")
    _require(isinstance(release, str) and bool(re.fullmatch(rf"daily-authority-{session}-[1-9]\d*-[1-9]\d*", release)), "invalid authority release identity")
    _require(manifest.get("schema_version") == "daily_authority_release_v1", "invalid authority manifest schema")
    _require(manifest.get("producer") == "daily_full_pipeline", "invalid authority producer")
    baseline = manifest.get("base_commit_sha")
    _require(isinstance(baseline, str) and bool(re.fullmatch(r"[0-9a-f]{40}", baseline)), "invalid authority baseline SHA")
    _require(manifest.get("transition_baseline") == {"kind": "git_object", "commit_sha": baseline, "path": MARKET_PATH}, "invalid authority transition baseline")
    for field in ("generation_id",):
        _require(manifest.get(field) == release, f"authority {field} differs from release")
    for field in ("authority_release_id", "authority_generation_id"):
        _require(market.get(field) == release and freshness.get(field) == release, f"authority identity mismatch: {field}")
    for obj in (market, freshness):
        _require(obj.get("authority_base_commit_sha") == baseline, "authority base commit mismatch")
        _require(obj.get("authority_producer") == "daily_full_pipeline", "authority producer mismatch")
    for field in ("market_session_date", "expected_main_price_date", "market_status", "reason_code", "generated_at"):
        _require(manifest.get(field) == market.get(field), f"manifest semantic mismatch: {field}")
    for csv_field, json_field in {"market_session_status": "market_status", "market_session_date": "market_session_date", "expected_main_price_date": "expected_main_price_date", "market_session_reason_code": "reason_code", "market_session_generated_at": "generated_at"}.items():
        _require(freshness.get(csv_field) == market.get(json_field), f"freshness market mismatch: {csv_field}")
    report_note = "market session is not open_confirmed: market_session_status=closed_emergency"
    for field, value in {"report_ready": "False", "daily_pdf_ready": "False", "report_ready_note": report_note, "daily_pdf_ready_note": f"core daily data not ready: {report_note}", "main_price_date_source": "validated_stock_history", "historical_replay_main_price_date": "", "expected_price_history_high_water_date": ""}.items():
        _require(freshness.get(field) == value, f"closure freshness mismatch: {field}")
    main_date = _date(freshness.get("main_price_date"), "main_price_date")
    _require(main_date <= expected_date < session, "closure source dates must remain main <= expected < session")
    for field in ("actual_stock_price_history_date", "stock_monitor_price_date", "all_candidates_date", "official_price_fetch_date", "raw_stock_monitor_price_date", "raw_all_candidates_date", "raw_official_price_fetch_date"):
        _require(freshness.get(field) == main_date, f"closure source date mismatch: {field}")
    surfaces = manifest.get("surfaces")
    _require(isinstance(surfaces, dict) and set(surfaces) == {MARKET_PATH, FRESHNESS_PATH, FRESHNESS_MD_PATH}, "invalid authority manifest surface set")
    for path, digest in surfaces.items():
        _sha(digest, path)
        _require(hashlib.sha256(payloads[path]).hexdigest() == digest, f"authority surface SHA mismatch: {path}")

    scheduled = _csv(payloads[SCHEDULED_PATH], SCHEDULED_PATH)
    exceptional = _csv(payloads[EXCEPTIONAL_PATH], EXCEPTIONAL_PATH)
    scheduled_dates = [_date(row.get("date"), "scheduled calendar") for row in scheduled]
    exceptional_dates = [_date(row.get("date"), "exceptional calendar") for row in exceptional]
    _require(len(set(scheduled_dates)) == len(scheduled_dates) and len(set(exceptional_dates)) == len(exceptional_dates), "duplicate calendar dates")
    _require(market.get("scheduled_non_trading_days") == sorted(scheduled_dates), "scheduled calendar identity mismatch")
    _require(market.get("exceptional_non_trading_days") == sorted(exceptional_dates), "exceptional calendar identity mismatch")
    closure_rows = [row for row in exceptional if row["date"] == session]
    _require(len(closure_rows) == 1, "emergency closure needs one exceptional-calendar row")
    notice = market.get("emergency_notice")
    _require(isinstance(notice, dict), "missing emergency notice")
    _require(notice.get("date") == session and notice.get("scope") in {"full_day", "morning"}, "invalid emergency notice date/scope")
    _require(bool(notice.get("summary")) and notice.get("summary") == market.get("reason"), "emergency notice reason mismatch")
    _require(notice.get("source_url") == DGPA_URL and bool(notice.get("source_record_id")), "invalid emergency notice source identity")
    notice_time = _timestamp(notice.get("source_updated_at"), "notice.source_updated_at")
    _require(notice_time <= generated, "emergency notice is newer than closure publication")
    closure = closure_rows[0]
    for field, value in {"market_status": "closed_emergency", "market": "TWSE_TPEx", "government_area": "Taipei City", "closure_scope": notice["scope"], "source_url": DGPA_URL, "source_record_id": notice["source_record_id"], "source_updated_at": notice["source_updated_at"], "twse_rule_url": RULE_URL}.items():
        _require(closure.get(field) == value, f"exceptional calendar mismatch: {field}")
    first = _timestamp(closure.get("first_observed_at"), "closure.first_observed_at")
    last = _timestamp(closure.get("last_observed_at"), "closure.last_observed_at")
    _require(notice_time <= first <= last <= generated, "invalid emergency calendar observation chronology")
    sources = market.get("official_sources")
    _require(isinstance(sources, dict), "missing official source evidence")
    for name, url in (("dgpa_emergency_closure", DGPA_URL), ("twse_annual_calendar", ANNUAL_URL)):
        source = sources.get(name)
        _require(isinstance(source, dict), f"missing official source: {name}")
        _require(source.get("status") == "ok" and source.get("url") == url and source.get("source") == name, f"invalid official source status/identity: {name}")
        _sha(source.get("sha256"), f"{name}.sha256")
        for field in ("byte_len", "attempt_count"):
            _require(type(source.get(field)) is int and source[field] > 0, f"invalid official source {field}: {name}")
        _require(_timestamp(source.get("queried_at"), f"{name}.queried_at") == generated, f"official source query time mismatch: {name}")
    dgpa = sources["dgpa_emergency_closure"]
    _require(dgpa.get("conflict_dates") == [] and dgpa.get("latest_taipei_notice_dates") == [session], "ambiguous emergency source dates")
    _require(type(dgpa.get("taipei_notice_count")) is int and dgpa["taipei_notice_count"] > 0, "missing Taipei closure notice")
    annual = sources["twse_annual_calendar"]
    _require(isinstance(annual.get("covered_years"), list) and int(session[:4]) in annual["covered_years"], "annual calendar does not cover closure year")
    _require(sources.get("twse_emergency_rule") == {"status": "reference", "url": RULE_URL}, "invalid emergency rule identity")
    day = datetime.strptime(session, "%Y%m%d") - timedelta(days=1)
    closed = set(scheduled_dates) | set(exceptional_dates)
    while day.weekday() >= 5 or day.strftime("%Y%m%d") in closed:
        day -= timedelta(days=1)
    _require(expected_date == day.strftime("%Y%m%d"), "closure expected date differs from prior trading date")

    previous_date = _date(previous.get("market_session_date"), "previous market_session_date")
    _require(previous_date <= session, "market session date moves backward")
    _require(_timestamp(previous.get("generated_at"), "previous.generated_at") <= generated, "market generation moves backward")
    if previous_date == session:
        _require(previous.get("expected_main_price_date") == expected_date, "same-session expected date changed")
        if previous.get("market_status") in {"open_confirmed", "closed_scheduled", "closed_emergency"}:
            _require(previous.get("market_status") == "closed_emergency" and previous.get("phase") == market["phase"], "terminal market session changed")
        ranks = {"preflight": 0, "confirm": 1}
        _require(ranks.get(previous.get("phase"), -1) <= ranks[market["phase"]], "market phase moves backward")


def validate_inherited_market_closure(base_ref: str, *, repository_root: Path) -> list[str]:
    """Validate inherited closure evidence; never set or waive runtime readiness."""
    root = repository_root.resolve()
    try:
        base = _commit(root, base_ref)
        head = _commit(root, "HEAD")
        _git(root, "merge-base", "--is-ancestor", base, head)
        base_entries = _tree_entries(root, base)
        head_entries = _tree_entries(root, head)
        index_entries = set(_git(root, "ls-files", "--stage", "-z", "--", *INHERITED_SOURCE_PATHS).split(b"\0"))
        sparse_entries = set(_git(root, "ls-files", "-v", "-z", "--", *INHERITED_SOURCE_PATHS).split(b"\0"))
        payloads: dict[str, bytes] = {}
        for path in INHERITED_SOURCE_PATHS:
            head_oid = head_entries[path]
            _require(base_entries[path] == head_oid, f"inherited source dependency changed from base: {path}")
            payload = _git(root, "cat-file", "blob", head_oid)
            _checkout_matches(root, path, head_oid, payload, index_entries=index_entries, sparse_entries=sparse_entries)
            payloads[path] = payload
        manifest = _json(payloads[MANIFEST_PATH], MANIFEST_PATH)
        baseline = manifest.get("base_commit_sha")
        _require(isinstance(baseline, str) and bool(re.fullmatch(r"[0-9a-f]{40}", baseline)), "invalid authority baseline SHA")
        _git(root, "merge-base", "--is-ancestor", baseline, base)
        _, previous_payload = _blob(root, baseline, MARKET_PATH)
        _closure_semantics(payloads, _json(previous_payload, "authority transition preimage"))
    except (ClosureEvidenceError, OSError, ValueError, UnicodeError, csv.Error, TypeError, KeyError, OverflowError) as exc:
        return [f"inherited emergency closure evidence invalid: {exc}"]
    return []
