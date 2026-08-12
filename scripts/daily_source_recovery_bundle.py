from __future__ import annotations

import argparse
import csv
import hashlib
import json
import os
import re
import shutil
import subprocess
import sys
import uuid
from datetime import datetime, timedelta, timezone
from pathlib import Path, PurePosixPath
from typing import Any, Callable


ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from scripts import daily_authority_release, market_session_calendar


BUNDLE_SCHEMA = "daily_source_recovery_bundle_v1"
STATE_SCHEMA = "daily_source_recovery_state_v1"
RESERVATION_SCHEMA = "daily_source_recovery_dispatch_reservation_v1"
WORKFLOW_PATH = ".github/workflows/daily_full_pipeline.yml"
SHA1_RE = re.compile(r"[0-9a-f]{40}")
SHA256_RE = re.compile(r"[0-9a-f]{64}")
DATE_RE = re.compile(r"20\d{6}")
RELEASE_RE = re.compile(r"[A-Za-z0-9][A-Za-z0-9._:-]{7,127}")

ALLOWED_TRANSITIONS = {
    "source_absent": {"repairing", "failed"},
    "repairing": {"bundle_ready", "failed"},
    "bundle_ready": {"bundle_committed", "failed"},
    "bundle_committed": {"resume_not_required", "resume_dispatched", "failed"},
    "resume_not_required": {"confirm_source_gate", "failed"},
    "resume_dispatched": {"resume_running", "failed"},
    "resume_running": {"resume_succeeded", "failed"},
    "resume_succeeded": {"confirm_source_gate", "failed"},
    "confirm_source_gate": set(),
    "failed": set(),
}


class DailySourceRecoveryError(RuntimeError):
    pass


def sha256_bytes(payload: bytes) -> str:
    return hashlib.sha256(payload).hexdigest()


def json_bytes(payload: dict[str, Any]) -> bytes:
    return (json.dumps(payload, ensure_ascii=False, indent=2, sort_keys=True) + "\n").encode("utf-8")


def normalized_date(value: object) -> str:
    text = re.sub(r"[^0-9]", "", str(value or ""))
    if not DATE_RE.fullmatch(text):
        raise DailySourceRecoveryError(f"invalid trading date: {value!r}")
    return text


def checked_release_id(value: object) -> str:
    text = str(value or "").strip()
    if not RELEASE_RE.fullmatch(text):
        raise DailySourceRecoveryError(f"invalid source recovery release id: {text!r}")
    return text


def checked_sha1(value: object, label: str) -> str:
    text = str(value or "").strip().lower()
    if not SHA1_RE.fullmatch(text):
        raise DailySourceRecoveryError(f"invalid {label}: {text!r}")
    return text


def checked_sha256(value: object, label: str) -> str:
    text = str(value or "").strip().lower()
    if not SHA256_RE.fullmatch(text):
        raise DailySourceRecoveryError(f"invalid {label}: {text!r}")
    return text


def checked_relative_path(value: object) -> str:
    text = str(value or "").replace("\\", "/").strip()
    path = PurePosixPath(text)
    if not text or path.is_absolute() or ".." in path.parts or "." in path.parts:
        raise DailySourceRecoveryError(f"unsafe source bundle path: {text!r}")
    return path.as_posix()


def required_source_paths(trading_date: str) -> tuple[str, ...]:
    date_text = normalized_date(trading_date)
    return (
        f"data/daily_price/{date_text}.csv",
        f"data/daily_price/daily_price_{date_text}.csv",
        "output/latest/official_daily_price_latest.csv",
        "data/market_calendar/exceptional_non_trading_days.csv",
    )


def bundle_root_path(trading_date: str, release_id: str) -> Path:
    return Path("output/history/daily_source_bundles") / normalized_date(trading_date) / checked_release_id(
        release_id
    )


def git_output(root: Path, *args: str) -> bytes:
    proc = subprocess.run(
        ["git", *args],
        cwd=root,
        check=False,
        capture_output=True,
    )
    if proc.returncode != 0:
        detail = (proc.stderr or proc.stdout).decode("utf-8", errors="replace").strip()
        raise DailySourceRecoveryError(f"git {' '.join(args)} failed: {detail}")
    return proc.stdout


def git_head(root: Path) -> str:
    return checked_sha1(git_output(root, "rev-parse", "HEAD").decode().strip(), "repository HEAD")


def git_blob(root: Path, commit_sha: str, relative_path: str) -> bytes:
    commit = checked_sha1(commit_sha, "source bundle commit SHA")
    path = checked_relative_path(relative_path)
    return git_output(root, "show", f"{commit}:{path}")


def git_mode(root: Path, commit_sha: str, relative_path: str) -> str:
    commit = checked_sha1(commit_sha, "source bundle commit SHA")
    path = checked_relative_path(relative_path)
    output = git_output(root, "ls-tree", commit, "--", path).decode("utf-8", errors="strict").strip()
    fields = output.split(None, 3)
    if len(fields) != 4 or fields[3] != path or fields[1] != "blob":
        raise DailySourceRecoveryError(f"missing or non-blob Git object for {path}")
    if fields[0] != "100644":
        raise DailySourceRecoveryError(f"unexpected Git mode for {path}: {fields[0]}")
    return fields[0]


def git_last_path_commit(root: Path, revision: str, relative_path: str) -> str:
    path = checked_relative_path(relative_path)
    commit = git_output(root, "log", "-1", "--format=%H", revision, "--", path).decode(
        "ascii"
    ).strip()
    return checked_sha1(commit, f"last-change commit for {path}")


def git_blob_oid(root: Path, revision: str, relative_path: str) -> str:
    path = checked_relative_path(relative_path)
    return checked_sha1(
        git_output(root, "rev-parse", f"{revision}:{path}").decode("ascii").strip(),
        f"Git blob object for {path}",
    )


def git_worktree_blob_oid(root: Path, relative_path: str) -> str:
    path = checked_relative_path(relative_path)
    return checked_sha1(
        git_output(root, "hash-object", "--path", path, path).decode("ascii").strip(),
        f"working-tree Git blob object for {path}",
    )


def _validate_price_csv(payload: bytes, trading_date: str, path: str) -> list[str]:
    try:
        text = payload.decode("utf-8-sig")
        rows = list(csv.DictReader(text.splitlines()))
    except Exception as exc:
        raise DailySourceRecoveryError(f"cannot parse daily price source {path}: {exc}") from exc
    if len(rows) < 1000:
        raise DailySourceRecoveryError(f"daily price source has too few rows: {path} rows={len(rows)}")
    dates = {str(row.get("date") or "").strip() for row in rows}
    if dates != {trading_date}:
        raise DailySourceRecoveryError(
            f"daily price source date mismatch: {path} expected={trading_date} observed={sorted(dates)}"
        )
    identities = sorted({str(row.get("source") or "").strip() for row in rows if row.get("source")})
    if not identities:
        raise DailySourceRecoveryError(f"daily price source identity is missing: {path}")
    return identities


def _validate_market_session(payload: dict[str, Any], trading_date: str) -> None:
    required = {
        "market_status": market_session_calendar.OPEN_CONFIRMED,
        "phase": "confirm",
        "market_session_date": trading_date,
        "expected_main_price_date": trading_date,
    }
    for field, expected in required.items():
        observed = str(payload.get(field) or "")
        if observed != expected:
            raise DailySourceRecoveryError(
                f"source bundle market-session mismatch: {field} expected={expected!r} observed={observed!r}"
            )


def new_state(
    *,
    trading_date: str,
    release_id: str,
    source_bundle_sha: str,
    source_base_sha: str,
    run_id: str,
    run_attempt: int,
    phase: str = "bundle_ready",
) -> dict[str, Any]:
    if phase not in ALLOWED_TRANSITIONS:
        raise DailySourceRecoveryError(f"invalid source recovery phase: {phase}")
    attempt = int(run_attempt)
    if attempt < 1:
        raise DailySourceRecoveryError("source workflow run_attempt must be positive")
    return {
        "schema_version": STATE_SCHEMA,
        "phase": phase,
        "trading_date": normalized_date(trading_date),
        "release_id": checked_release_id(release_id),
        "source_bundle_sha": checked_sha256(source_bundle_sha, "source bundle SHA-256"),
        "source_base_sha": checked_sha1(source_base_sha, "source base SHA"),
        "source_workflow_run_id": str(run_id),
        "source_workflow_run_attempt": attempt,
    }


def transition_state(state: dict[str, Any], next_phase: str, **updates: Any) -> dict[str, Any]:
    if state.get("schema_version") != STATE_SCHEMA:
        raise DailySourceRecoveryError("invalid source recovery state schema")
    current = str(state.get("phase") or "")
    if next_phase not in ALLOWED_TRANSITIONS.get(current, set()):
        raise DailySourceRecoveryError(f"forbidden source recovery transition: {current} -> {next_phase}")
    result = dict(state)
    result.update({key: value for key, value in updates.items() if value not in (None, "")})
    result["phase"] = next_phase
    if next_phase == "bundle_committed":
        result["source_bundle_commit_sha"] = checked_sha1(
            result.get("source_bundle_commit_sha"), "source bundle commit SHA"
        )
    if next_phase == "resume_dispatched":
        if result.get("resume_workflow_path") != WORKFLOW_PATH:
            raise DailySourceRecoveryError("resume workflow path must be the exact Daily Full workflow")
        checked_sha1(result.get("resume_expected_head_sha"), "resume expected head SHA")
        _parse_utc(result.get("resume_dispatch_started_at"), "resume dispatch time")
        int(result.get("resume_baseline_run_id") or 0)
        title = str(result.get("resume_expected_display_title") or "")
        if not re.fullmatch(r"Daily Full Pipeline \| recovery=[A-Za-z0-9._:-]{8,160}", title):
            raise DailySourceRecoveryError("resume expected display title is invalid")
        reservation_path = checked_relative_path(result.get("resume_reservation_path"))
        if reservation_path != dispatch_reservation_path(result["trading_date"]).as_posix():
            raise DailySourceRecoveryError("resume reservation path is not date-scoped")
        checked_sha256(result.get("resume_reservation_sha256"), "resume reservation SHA-256")
    if next_phase == "resume_not_required":
        release_id = checked_release_id(result.get("existing_authority_release_id"))
        if result.get("existing_authority_generation_id") != release_id:
            raise DailySourceRecoveryError("existing authority release/generation identity mismatch")
        checked_sha1(result.get("existing_authority_commit_sha"), "existing authority commit SHA")
    if next_phase == "resume_running":
        run_id = int(result.get("resume_workflow_run_id") or 0)
        baseline = int(result.get("resume_baseline_run_id") or 0)
        if run_id <= baseline:
            raise DailySourceRecoveryError("resume workflow run id must be newer than the baseline")
        if int(result.get("resume_workflow_run_attempt") or 0) != 1:
            raise DailySourceRecoveryError("resume workflow run_attempt must equal 1")
        if not str(result.get("resume_workflow_run_url") or "").startswith("https://github.com/"):
            raise DailySourceRecoveryError("resume workflow run URL is invalid")
    if next_phase == "resume_succeeded" and result.get("resume_conclusion") != "success":
        raise DailySourceRecoveryError("resume_succeeded requires conclusion=success")
    if next_phase == "failed" and not str(result.get("error") or ""):
        raise DailySourceRecoveryError("failed source recovery state requires an error")
    return result


def _parse_utc(value: object, label: str) -> datetime:
    text = str(value or "").strip()
    try:
        parsed = datetime.fromisoformat(text.replace("Z", "+00:00"))
    except ValueError as exc:
        raise DailySourceRecoveryError(f"invalid {label}: {text!r}") from exc
    if parsed.tzinfo is None:
        raise DailySourceRecoveryError(f"{label} must include a timezone")
    return parsed.astimezone(timezone.utc)


def select_correlated_run(
    runs: list[dict[str, Any]],
    *,
    baseline_run_id: int,
    dispatch_started_at: str,
    expected_head_sha: str,
    expected_display_title: str,
    window_seconds: int = 900,
) -> dict[str, Any] | None:
    head_sha = checked_sha1(expected_head_sha, "resume expected head SHA")
    started = _parse_utc(dispatch_started_at, "resume dispatch time")
    earliest = started - timedelta(seconds=15)
    latest = started + timedelta(seconds=window_seconds)
    matches: list[dict[str, Any]] = []
    for run in runs:
        try:
            run_id = int(run.get("databaseId") or 0)
            run_attempt = int(run.get("attempt") or 0)
            created_at = _parse_utc(run.get("createdAt"), "workflow run createdAt")
        except (TypeError, ValueError, DailySourceRecoveryError):
            continue
        if (
            run_id > int(baseline_run_id)
            and run_attempt == 1
            and run.get("event") == "workflow_dispatch"
            and run.get("workflowName") == "Daily Full Pipeline"
            and run.get("headSha") == head_sha
            and run.get("displayTitle") == expected_display_title
            and earliest <= created_at <= latest
        ):
            matches.append(run)
    if len(matches) > 1:
        raise DailySourceRecoveryError(
            "multiple Daily Full runs match one source recovery dispatch: "
            + ",".join(str(item.get("databaseId")) for item in matches)
        )
    return matches[0] if matches else None


def reject_existing_recovery_run(
    runs: list[dict[str, Any]], *, expected_display_title: str
) -> None:
    title = str(expected_display_title or "")
    if not re.fullmatch(r"Daily Full Pipeline \| recovery=daily-source-20\d{6}", title):
        raise DailySourceRecoveryError("stable recovery display title is invalid")
    matches = [
        run
        for run in runs
        if run.get("event") == "workflow_dispatch"
        and run.get("workflowName") == "Daily Full Pipeline"
        and run.get("displayTitle") == title
    ]
    if matches:
        raise DailySourceRecoveryError(
            "Daily Full recovery run already exists for this trading date: "
            + ",".join(str(item.get("databaseId") or "") for item in matches)
        )


def dispatch_reservation_path(trading_date: str) -> PurePosixPath:
    return PurePosixPath(
        "output/history/daily_source_recovery_reservations"
    ) / f"{normalized_date(trading_date)}.json"


def create_dispatch_reservation(
    root: Path,
    *,
    trading_date: str,
    source_commit_sha: str,
    manifest_path: str,
    manifest_sha256: str,
    source_bundle_sha: str,
    baseline_run_id: int,
    dispatch_started_at: str,
    expected_display_title: str,
) -> dict[str, Any]:
    root = root.resolve()
    date_text = normalized_date(trading_date)
    source_commit = checked_sha1(source_commit_sha, "source bundle commit SHA")
    manifest = verify_bundle_from_git(
        root,
        source_commit_sha=source_commit,
        manifest_path=manifest_path,
        manifest_sha256=manifest_sha256,
        source_bundle_sha=source_bundle_sha,
        trading_date=date_text,
    )
    baseline = int(baseline_run_id)
    if baseline < 0:
        raise DailySourceRecoveryError("dispatch reservation baseline run id cannot be negative")
    started = _parse_utc(dispatch_started_at, "dispatch reservation time")
    title = str(expected_display_title or "")
    expected_title = f"Daily Full Pipeline | recovery=daily-source-{date_text}"
    if title != expected_title:
        raise DailySourceRecoveryError(
            f"dispatch reservation title mismatch: expected={expected_title!r} observed={title!r}"
        )
    relative_path = dispatch_reservation_path(date_text)
    target = root / relative_path
    if target.exists():
        raise DailySourceRecoveryError(
            f"daily source recovery dispatch reservation already exists: {relative_path}"
        )
    payload = {
        "schema_version": RESERVATION_SCHEMA,
        "trading_date": date_text,
        "source_bundle_commit_sha": source_commit,
        "source_bundle_manifest_path": checked_relative_path(manifest_path),
        "source_bundle_manifest_sha256": checked_sha256(
            manifest_sha256, "source bundle manifest SHA-256"
        ),
        "source_bundle_sha": checked_sha256(source_bundle_sha, "source bundle SHA-256"),
        "source_bundle_release_id": checked_release_id(manifest["release_id"]),
        "reservation_base_sha": git_head(root),
        "resume_workflow_path": WORKFLOW_PATH,
        "resume_baseline_run_id": baseline,
        "resume_dispatch_started_at": started.isoformat().replace("+00:00", "Z"),
        "resume_expected_display_title": title,
    }
    payload_bytes = json_bytes(payload)
    _write_atomic(target, payload_bytes)
    return {
        "path": relative_path.as_posix(),
        "sha256": sha256_bytes(payload_bytes),
        "payload": payload,
    }


def verify_dispatch_reservation(
    root: Path,
    *,
    trading_date: str,
    reservation_path: str,
    reservation_sha256: str,
    expected_head_sha: str,
    source_commit_sha: str,
    manifest_path: str,
    manifest_sha256: str,
    source_bundle_sha: str,
    correlation_id: str,
) -> dict[str, Any]:
    root = root.resolve()
    date_text = normalized_date(trading_date)
    head_sha = checked_sha1(expected_head_sha, "recovery expected head SHA")
    if git_head(root) != head_sha:
        raise DailySourceRecoveryError("dispatch reservation checkout does not equal expected head")
    path = checked_relative_path(reservation_path)
    expected_path = dispatch_reservation_path(date_text).as_posix()
    if path != expected_path:
        raise DailySourceRecoveryError(
            f"dispatch reservation path mismatch: expected={expected_path} observed={path}"
        )
    expected_sha = checked_sha256(reservation_sha256, "dispatch reservation SHA-256")
    source_manifest = verify_bundle_from_git(
        root,
        source_commit_sha=source_commit_sha,
        manifest_path=manifest_path,
        manifest_sha256=manifest_sha256,
        source_bundle_sha=source_bundle_sha,
        trading_date=date_text,
    )
    payload_bytes = git_blob(root, head_sha, path)
    if sha256_bytes(payload_bytes) != expected_sha:
        raise DailySourceRecoveryError("dispatch reservation Git object SHA-256 mismatch")
    if git_mode(root, head_sha, path) != "100644":
        raise DailySourceRecoveryError("dispatch reservation Git mode must equal 100644")
    working_path = root / path
    if not working_path.is_file() or working_path.read_bytes() != payload_bytes:
        raise DailySourceRecoveryError("dispatch reservation working bytes differ from Git object")
    parent_sha = subprocess.check_output(
        ["git", "rev-parse", f"{head_sha}^"], cwd=root, text=True
    ).strip()
    changed_paths = subprocess.check_output(
        ["git", "diff-tree", "--no-commit-id", "--name-only", "-r", head_sha],
        cwd=root,
        text=True,
    ).splitlines()
    if changed_paths != [path]:
        raise DailySourceRecoveryError(
            f"dispatch reservation commit path set is not exact: {changed_paths}"
        )
    try:
        payload = json.loads(payload_bytes.decode("utf-8"))
    except Exception as exc:
        raise DailySourceRecoveryError(f"cannot parse dispatch reservation: {exc}") from exc
    expected_keys = {
        "schema_version",
        "trading_date",
        "source_bundle_commit_sha",
        "source_bundle_manifest_path",
        "source_bundle_manifest_sha256",
        "source_bundle_sha",
        "source_bundle_release_id",
        "reservation_base_sha",
        "resume_workflow_path",
        "resume_baseline_run_id",
        "resume_dispatch_started_at",
        "resume_expected_display_title",
    }
    if set(payload) != expected_keys:
        raise DailySourceRecoveryError("dispatch reservation field set is not exact")
    expected_correlation = f"daily-source-{date_text}"
    expected_title = f"Daily Full Pipeline | recovery={expected_correlation}"
    expected_values = {
        "schema_version": RESERVATION_SCHEMA,
        "trading_date": date_text,
        "source_bundle_commit_sha": checked_sha1(
            source_commit_sha, "source bundle commit SHA"
        ),
        "source_bundle_manifest_path": checked_relative_path(manifest_path),
        "source_bundle_manifest_sha256": checked_sha256(
            manifest_sha256, "source bundle manifest SHA-256"
        ),
        "source_bundle_sha": checked_sha256(source_bundle_sha, "source bundle SHA-256"),
        "source_bundle_release_id": checked_release_id(source_manifest["release_id"]),
        "reservation_base_sha": parent_sha,
        "resume_workflow_path": WORKFLOW_PATH,
        "resume_expected_display_title": expected_title,
    }
    for key, expected_value in expected_values.items():
        if payload.get(key) != expected_value:
            raise DailySourceRecoveryError(
                f"dispatch reservation identity mismatch for {key}: "
                f"expected={expected_value!r} observed={payload.get(key)!r}"
            )
    if correlation_id != expected_correlation:
        raise DailySourceRecoveryError("dispatch reservation correlation id is not date-scoped")
    if int(payload.get("resume_baseline_run_id") or -1) < 0:
        raise DailySourceRecoveryError("dispatch reservation baseline run id is invalid")
    _parse_utc(payload.get("resume_dispatch_started_at"), "dispatch reservation time")
    return payload


def existing_authority_completion(
    root: Path,
    trading_date: str,
    *,
    source_commit_sha: str,
    manifest_path: str,
    manifest_sha256: str,
    source_bundle_sha: str,
) -> dict[str, str] | None:
    root = root.resolve()
    date_text = normalized_date(trading_date)
    try:
        source_manifest = verify_bundle_from_git(
            root,
            source_commit_sha=source_commit_sha,
            manifest_path=manifest_path,
            manifest_sha256=manifest_sha256,
            source_bundle_sha=source_bundle_sha,
            trading_date=date_text,
        )
        source_commit = checked_sha1(source_commit_sha, "source bundle commit SHA")
        for entry in source_manifest["files"]:
            current_path = root / entry["path"]
            bundle_payload = git_blob(root, source_commit, entry["bundle_path"])
            if not current_path.is_file() or current_path.read_bytes() != bundle_payload:
                return None
        market_path = root / "output/latest/market_session_status_latest.json"
        bundle_market_payload = git_blob(
            root,
            source_commit,
            source_manifest["market_session"]["bundle_path"],
        )
        if not market_path.is_file():
            return None
        bundle_market = json.loads(bundle_market_payload.decode("utf-8"))
        manifest = daily_authority_release.validate_authority_release(root)
        authority_base_sha = checked_sha1(
            manifest.get("base_commit_sha"), "authority base commit SHA"
        )
        release_manifest_path = daily_authority_release.RELEASE_MANIFEST_PATH.as_posix()
        authority_release_sha = git_last_path_commit(
            root, source_commit, release_manifest_path
        )
        if subprocess.run(
            [
                "git",
                "merge-base",
                "--is-ancestor",
                authority_base_sha,
                authority_release_sha,
            ],
            cwd=root,
            check=False,
        ).returncode != 0:
            return None
        if subprocess.run(
            ["git", "merge-base", "--is-ancestor", authority_release_sha, source_commit],
            cwd=root,
            check=False,
        ).returncode != 0:
            return None
        for surface_path in (
            daily_authority_release.MARKET_SESSION_PATH,
            daily_authority_release.FRESHNESS_CSV_PATH,
            daily_authority_release.FRESHNESS_MD_PATH,
            daily_authority_release.RELEASE_MANIFEST_PATH,
        ):
            relative_surface = surface_path.as_posix()
            current_surface = root / surface_path
            if (
                not current_surface.is_file()
                or git_mode(root, authority_release_sha, relative_surface) != "100644"
                or git_blob_oid(root, authority_release_sha, relative_surface)
                != git_worktree_blob_oid(root, relative_surface)
            ):
                return None
        for entry in source_manifest["files"]:
            bundle_payload = git_blob(root, source_commit, entry["bundle_path"])
            authority_payload = git_blob(root, authority_release_sha, entry["path"])
            if git_mode(root, authority_release_sha, entry["path"]) != entry["mode"]:
                return None
            if (
                authority_payload != bundle_payload
                or sha256_bytes(authority_payload) != entry["sha256"]
            ):
                return None
        market = json.loads(
            market_path.read_text(encoding="utf-8-sig")
        )
        _, freshness = daily_authority_release.read_single_csv(
            root / "output/latest/data_freshness_latest.csv"
        )
    except Exception:
        return None
    required_market = {
        "market_status": market_session_calendar.OPEN_CONFIRMED,
        "phase": "confirm",
        "market_session_date": date_text,
        "expected_main_price_date": date_text,
    }
    if any(str(market.get(key) or "") != value for key, value in required_market.items()):
        return None
    decision_fields = (
        "market_status",
        "phase",
        "market_session_date",
        "expected_main_price_date",
        "should_run_daily_pipeline",
    )
    if any(market.get(key) != bundle_market.get(key) for key in decision_fields):
        return None
    if market.get("should_run_daily_pipeline") is not True:
        return None
    required_freshness = {
        "market_session_status": market_session_calendar.OPEN_CONFIRMED,
        "market_session_date": date_text,
        "expected_main_price_date": date_text,
        "main_price_date": date_text,
        "report_ready": "True",
        "warrant_ready": "True",
        "daily_pdf_ready": "True",
    }
    if any(str(freshness.get(key) or "") != value for key, value in required_freshness.items()):
        return None
    release_id = str(manifest.get("release_id") or "")
    generation_id = str(manifest.get("generation_id") or "")
    if not release_id or generation_id != release_id:
        return None
    return {
        "release_id": release_id,
        "generation_id": generation_id,
        "commit_sha": authority_release_sha,
    }


def _write_atomic(path: Path, payload: bytes) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    candidate = path.with_name(f".{path.name}.{uuid.uuid4().hex}.tmp")
    try:
        candidate.write_bytes(payload)
        os.replace(candidate, path)
    finally:
        candidate.unlink(missing_ok=True)


def _validate_manifest_shape(manifest: dict[str, Any], *, expected_date: str = "") -> None:
    if manifest.get("schema_version") != BUNDLE_SCHEMA:
        raise DailySourceRecoveryError("invalid source recovery bundle schema")
    trading_date = normalized_date(manifest.get("trading_date"))
    if expected_date and trading_date != normalized_date(expected_date):
        raise DailySourceRecoveryError(
            f"source bundle trading date mismatch: expected={expected_date} observed={trading_date}"
        )
    checked_release_id(manifest.get("release_id"))
    checked_sha1(manifest.get("source_base_sha"), "source base SHA")
    expected_paths = set(required_source_paths(trading_date))
    files = manifest.get("files")
    if (
        not isinstance(files, list)
        or len(files) != len(expected_paths)
        or not all(isinstance(entry, dict) for entry in files)
        or {entry.get("path") for entry in files} != expected_paths
    ):
        raise DailySourceRecoveryError("source bundle file allowlist mismatch")
    source_identities = manifest.get("source_identities")
    if (
        not isinstance(source_identities, list)
        or source_identities != sorted(set(source_identities))
        or not source_identities
        or any(not isinstance(item, str) or not item.strip() for item in source_identities)
    ):
        raise DailySourceRecoveryError("source bundle source identity set is invalid")
    expected_bundle_root = bundle_root_path(trading_date, manifest.get("release_id"))
    for index, entry in enumerate(files, start=1):
        path = checked_relative_path(entry.get("path"))
        bundle_path = checked_relative_path(entry.get("bundle_path"))
        expected_bundle_path = (
            expected_bundle_root / "files" / f"{index:02d}-{Path(path).name}"
        ).as_posix()
        if bundle_path != expected_bundle_path:
            raise DailySourceRecoveryError(
                f"source bundle payload path mismatch: expected={expected_bundle_path} observed={bundle_path}"
            )
        if entry.get("mode") != "100644":
            raise DailySourceRecoveryError(f"source bundle mode mismatch: {path}")
        if int(entry.get("bytes") or -1) < 1:
            raise DailySourceRecoveryError(f"source bundle byte count is invalid: {path}")
        checked_sha256(entry.get("sha256"), f"source bundle file SHA-256 for {path}")
    market = manifest.get("market_session")
    if not isinstance(market, dict):
        raise DailySourceRecoveryError("source bundle market-session evidence is missing")
    _validate_market_session(market.get("payload") or {}, trading_date)
    checked_sha256(market.get("sha256"), "market-session evidence SHA-256")
    identity = dict(manifest)
    observed_bundle_sha = checked_sha256(identity.pop("source_bundle_sha", ""), "source bundle SHA-256")
    expected_bundle_sha = sha256_bytes(json_bytes(identity))
    if observed_bundle_sha != expected_bundle_sha:
        raise DailySourceRecoveryError("source bundle identity SHA mismatch")


def build_bundle(
    root: Path,
    *,
    trading_date: str,
    release_id: str,
    source_base_sha: str,
    run_id: str,
    run_attempt: int,
    market_session: dict[str, Any] | None = None,
    fail_after_copy: int = 0,
    fail_after_official_publish: bool = False,
) -> dict[str, Any]:
    root = root.resolve()
    date_text = normalized_date(trading_date)
    release = checked_release_id(release_id)
    base_sha = checked_sha1(source_base_sha, "source base SHA")
    if git_head(root) != base_sha:
        raise DailySourceRecoveryError("source bundle base SHA must equal repository HEAD")
    root_rel = bundle_root_path(date_text, release)
    final_root = root / root_rel
    if final_root.exists():
        raise DailySourceRecoveryError(f"source bundle root collision: {root_rel.as_posix()}")
    preparing = final_root.parent / f".prepare-{uuid.uuid4().hex[:8]}"
    price_paths = required_source_paths(date_text)[:2]
    price_payloads: list[bytes] = []
    source_identities: set[str] = set()
    for relative_path in price_paths:
        source = root / relative_path
        if not source.is_file() or source.is_symlink():
            raise DailySourceRecoveryError(f"required immutable source file is missing or unsafe: {relative_path}")
        payload = source.read_bytes()
        source_identities.update(_validate_price_csv(payload, date_text, relative_path))
        price_payloads.append(payload)
    if len({sha256_bytes(item) for item in price_payloads}) != 1:
        raise DailySourceRecoveryError("daily price canonical and legacy row projections are not byte-identical")
    price_payload = price_payloads[0]
    official_latest = root / "output/latest/official_daily_price_latest.csv"
    if official_latest.exists() and (not official_latest.is_file() or official_latest.is_symlink()):
        raise DailySourceRecoveryError("official daily price latest path is not a safe regular file")
    previous_official_payload = official_latest.read_bytes() if official_latest.exists() else None
    official_published = False
    final_published = False
    entries: list[dict[str, Any]] = []
    try:
        _write_atomic(official_latest, price_payload)
        official_published = True
        if fail_after_official_publish:
            raise DailySourceRecoveryError("injected source bundle publish failure")
        market = market_session or market_session_calendar.refresh_market_session_status(
            root, phase="confirm", write_files=False
        )
        _validate_market_session(market, date_text)
        preparing.mkdir(parents=True, exist_ok=False)
        copied = 0
        for index, relative_path in enumerate(required_source_paths(date_text), start=1):
            source = root / relative_path
            if relative_path == "output/latest/official_daily_price_latest.csv":
                payload = price_payload
            else:
                if not source.is_file() or source.is_symlink():
                    raise DailySourceRecoveryError(
                        f"required immutable source file is missing or unsafe: {relative_path}"
                    )
                payload = source.read_bytes()
            bundle_path = root_rel / "files" / f"{index:02d}-{Path(relative_path).name}"
            destination = preparing / "files" / f"{index:02d}-{Path(relative_path).name}"
            destination.parent.mkdir(parents=True, exist_ok=True)
            destination.write_bytes(payload)
            entries.append(
                {
                    "path": relative_path,
                    "bundle_path": bundle_path.as_posix(),
                    "mode": "100644",
                    "bytes": len(payload),
                    "sha256": sha256_bytes(payload),
                }
            )
            copied += 1
            if fail_after_copy and copied >= fail_after_copy:
                raise DailySourceRecoveryError("injected source bundle copy failure")
        market_payload = json_bytes(market)
        (preparing / "market_session_status.json").write_bytes(market_payload)
        identity: dict[str, Any] = {
            "schema_version": BUNDLE_SCHEMA,
            "trading_date": date_text,
            "release_id": release,
            "source_base_sha": base_sha,
            "source_workflow_run_id": str(run_id),
            "source_workflow_run_attempt": int(run_attempt),
            "source_identities": sorted(source_identities),
            "files": entries,
            "market_session": {
                "bundle_path": (root_rel / "market_session_status.json").as_posix(),
                "mode": "100644",
                "bytes": len(market_payload),
                "sha256": sha256_bytes(market_payload),
                "payload": market,
            },
        }
        manifest = dict(identity)
        manifest["source_bundle_sha"] = sha256_bytes(json_bytes(identity))
        manifest_payload = json_bytes(manifest)
        (preparing / "manifest.json").write_bytes(manifest_payload)
        state = new_state(
            trading_date=date_text,
            release_id=release,
            source_bundle_sha=manifest["source_bundle_sha"],
            source_base_sha=base_sha,
            run_id=run_id,
            run_attempt=run_attempt,
        )
        (preparing / "state.json").write_bytes(json_bytes(state))
        final_root.parent.mkdir(parents=True, exist_ok=True)
        os.replace(preparing, final_root)
        final_published = True
        return {
            "manifest": manifest,
            "manifest_path": (root_rel / "manifest.json").as_posix(),
            "manifest_sha256": sha256_bytes(manifest_payload),
            "state_path": (root_rel / "state.json").as_posix(),
        }
    except Exception:
        if final_published and final_root.exists():
            shutil.rmtree(final_root)
        if official_published:
            if previous_official_payload is None:
                official_latest.unlink(missing_ok=True)
            else:
                _write_atomic(official_latest, previous_official_payload)
        raise
    finally:
        if preparing.exists():
            shutil.rmtree(preparing)


def verify_bundle_from_git(
    root: Path,
    *,
    source_commit_sha: str,
    manifest_path: str,
    manifest_sha256: str,
    source_bundle_sha: str,
    trading_date: str,
    materialize: bool = False,
    state_output: Path | None = None,
) -> dict[str, Any]:
    root = root.resolve()
    source_commit = checked_sha1(source_commit_sha, "source bundle commit SHA")
    current_head = git_head(root)
    if subprocess.run(
        ["git", "merge-base", "--is-ancestor", source_commit, current_head],
        cwd=root,
        check=False,
    ).returncode != 0:
        raise DailySourceRecoveryError("source bundle commit is not an ancestor of repository HEAD")
    path = checked_relative_path(manifest_path)
    expected_manifest_sha = checked_sha256(manifest_sha256, "source bundle manifest SHA-256")
    expected_bundle_sha = checked_sha256(source_bundle_sha, "source bundle SHA-256")
    manifest_payload = git_blob(root, source_commit, path)
    if sha256_bytes(manifest_payload) != expected_manifest_sha:
        raise DailySourceRecoveryError("source bundle manifest Git object SHA-256 mismatch")
    try:
        manifest = json.loads(manifest_payload.decode("utf-8"))
    except Exception as exc:
        raise DailySourceRecoveryError(f"cannot parse source bundle manifest: {exc}") from exc
    _validate_manifest_shape(manifest, expected_date=trading_date)
    if manifest.get("source_bundle_sha") != expected_bundle_sha:
        raise DailySourceRecoveryError("source bundle identity does not match dispatch input")
    expected_path = (bundle_root_path(manifest["trading_date"], manifest["release_id"]) / "manifest.json").as_posix()
    if path != expected_path:
        raise DailySourceRecoveryError(
            f"source bundle manifest path mismatch: expected={expected_path} observed={path}"
        )
    git_mode(root, source_commit, path)
    base_sha = checked_sha1(manifest.get("source_base_sha"), "source base SHA")
    if subprocess.run(
        ["git", "merge-base", "--is-ancestor", base_sha, source_commit], cwd=root, check=False
    ).returncode != 0:
        raise DailySourceRecoveryError("source bundle commit does not descend from its source base SHA")
    materializations: list[tuple[Path, bytes]] = []
    for entry in manifest["files"]:
        canonical_path = entry["path"]
        bundle_path = entry["bundle_path"]
        payload = git_blob(root, source_commit, bundle_path)
        if len(payload) != entry["bytes"] or sha256_bytes(payload) != entry["sha256"]:
            raise DailySourceRecoveryError(f"source bundle payload identity mismatch: {canonical_path}")
        git_mode(root, source_commit, bundle_path)
        canonical_payload = git_blob(root, source_commit, canonical_path)
        if canonical_payload != payload or git_mode(root, source_commit, canonical_path) != entry["mode"]:
            raise DailySourceRecoveryError(f"source bundle canonical Git object mismatch: {canonical_path}")
        if materialize:
            materializations.append((root / canonical_path, payload))
    market_entry = manifest["market_session"]
    market_payload = git_blob(root, source_commit, market_entry["bundle_path"])
    if len(market_payload) != market_entry["bytes"] or sha256_bytes(market_payload) != market_entry["sha256"]:
        raise DailySourceRecoveryError("source bundle market-session Git object mismatch")
    if market_payload != json_bytes(market_entry["payload"]):
        raise DailySourceRecoveryError("source bundle market-session payload identity mismatch")
    git_mode(root, source_commit, market_entry["bundle_path"])
    if materialize:
        market_target = root / "output/latest/market_session_status_latest.json"
        if market_target.exists():
            try:
                current_market = json.loads(market_target.read_text(encoding="utf-8-sig"))
            except Exception as exc:
                raise DailySourceRecoveryError(
                    f"cannot parse current market-session state before materialization: {exc}"
                ) from exc
            transition_errors = market_session_calendar.market_session_transition_errors(
                current_market,
                market_entry["payload"],
            )
            if transition_errors:
                raise DailySourceRecoveryError(
                    "source bundle market-session transition is not monotonic: "
                    + "; ".join(transition_errors)
                )
        materializations.append((market_target, market_payload))
    state_path = str(PurePosixPath(path).parent / "state.json")
    state_payload = git_blob(root, source_commit, state_path)
    state = json.loads(state_payload.decode("utf-8"))
    expected_state = new_state(
        trading_date=manifest["trading_date"],
        release_id=manifest["release_id"],
        source_bundle_sha=expected_bundle_sha,
        source_base_sha=manifest["source_base_sha"],
        run_id=manifest["source_workflow_run_id"],
        run_attempt=int(manifest["source_workflow_run_attempt"]),
    )
    if state != expected_state:
        raise DailySourceRecoveryError("source recovery state identity mismatch")
    git_mode(root, source_commit, state_path)
    if materialize:
        previous_payloads = [
            (target, target.exists(), target.read_bytes() if target.exists() else b"")
            for target, _ in materializations
        ]
        try:
            for target, payload in materializations:
                _write_atomic(target, payload)
        except Exception:
            for target, existed, previous_payload in reversed(previous_payloads):
                if existed:
                    _write_atomic(target, previous_payload)
                else:
                    target.unlink(missing_ok=True)
            raise
    if state_output:
        _write_atomic(state_output.resolve(), state_payload)
    return manifest


def write_github_output(path: str, values: dict[str, object]) -> None:
    if not path:
        return
    with Path(path).open("a", encoding="utf-8") as handle:
        for key, value in values.items():
            handle.write(f"{key}={value}\n")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Build and verify immutable current-day source recovery bundles.")
    sub = parser.add_subparsers(dest="command", required=True)
    build = sub.add_parser("build")
    build.add_argument("--repo-root", default=".")
    build.add_argument("--trading-date", required=True)
    build.add_argument("--release-id", required=True)
    build.add_argument("--source-base-sha", required=True)
    build.add_argument("--run-id", required=True)
    build.add_argument("--run-attempt", type=int, required=True)
    build.add_argument("--github-output", default="")
    verify = sub.add_parser("verify")
    verify.add_argument("--repo-root", default=".")
    verify.add_argument("--source-commit-sha", required=True)
    verify.add_argument("--manifest-path", required=True)
    verify.add_argument("--manifest-sha256", required=True)
    verify.add_argument("--source-bundle-sha", required=True)
    verify.add_argument("--trading-date", required=True)
    verify.add_argument("--materialize", action="store_true")
    verify.add_argument("--state-output", default="")
    reserve = sub.add_parser("reserve")
    reserve.add_argument("--repo-root", default=".")
    reserve.add_argument("--trading-date", required=True)
    reserve.add_argument("--source-commit-sha", required=True)
    reserve.add_argument("--manifest-path", required=True)
    reserve.add_argument("--manifest-sha256", required=True)
    reserve.add_argument("--source-bundle-sha", required=True)
    reserve.add_argument("--baseline-run-id", required=True)
    reserve.add_argument("--dispatch-started-at", required=True)
    reserve.add_argument("--expected-display-title", required=True)
    verify_reservation = sub.add_parser("verify-reservation")
    verify_reservation.add_argument("--repo-root", default=".")
    verify_reservation.add_argument("--trading-date", required=True)
    verify_reservation.add_argument("--reservation-path", required=True)
    verify_reservation.add_argument("--reservation-sha256", required=True)
    verify_reservation.add_argument("--expected-head-sha", required=True)
    verify_reservation.add_argument("--source-commit-sha", required=True)
    verify_reservation.add_argument("--manifest-path", required=True)
    verify_reservation.add_argument("--manifest-sha256", required=True)
    verify_reservation.add_argument("--source-bundle-sha", required=True)
    verify_reservation.add_argument("--correlation-id", required=True)
    authority = sub.add_parser("authority-status")
    authority.add_argument("--repo-root", default=".")
    authority.add_argument("--trading-date", required=True)
    authority.add_argument("--source-commit-sha", required=True)
    authority.add_argument("--manifest-path", required=True)
    authority.add_argument("--manifest-sha256", required=True)
    authority.add_argument("--source-bundle-sha", required=True)
    authority.add_argument("--output", required=True)
    transition = sub.add_parser("transition")
    transition.add_argument("--state", required=True)
    transition.add_argument("--to", required=True, choices=tuple(ALLOWED_TRANSITIONS))
    transition.add_argument("--output", required=True)
    transition.add_argument("--source-bundle-commit-sha", default="")
    transition.add_argument("--resume-workflow-path", default="")
    transition.add_argument("--resume-baseline-run-id", default="")
    transition.add_argument("--resume-dispatch-started-at", default="")
    transition.add_argument("--resume-expected-head-sha", default="")
    transition.add_argument("--resume-expected-display-title", default="")
    transition.add_argument("--resume-reservation-path", default="")
    transition.add_argument("--resume-reservation-sha256", default="")
    transition.add_argument("--resume-workflow-run-id", default="")
    transition.add_argument("--resume-workflow-run-url", default="")
    transition.add_argument("--resume-workflow-run-attempt", default="")
    transition.add_argument("--resume-conclusion", default="")
    transition.add_argument("--existing-authority-release-id", default="")
    transition.add_argument("--existing-authority-generation-id", default="")
    transition.add_argument("--existing-authority-commit-sha", default="")
    transition.add_argument("--error", default="")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    try:
        if args.command == "build":
            result = build_bundle(
                Path(args.repo_root),
                trading_date=args.trading_date,
                release_id=args.release_id,
                source_base_sha=args.source_base_sha,
                run_id=args.run_id,
                run_attempt=args.run_attempt,
            )
            write_github_output(
                args.github_output,
                {
                    "manifest_path": result["manifest_path"],
                    "manifest_sha256": result["manifest_sha256"],
                    "source_bundle_sha": result["manifest"]["source_bundle_sha"],
                    "state_path": result["state_path"],
                },
            )
        elif args.command == "verify":
            verify_bundle_from_git(
                Path(args.repo_root),
                source_commit_sha=args.source_commit_sha,
                manifest_path=args.manifest_path,
                manifest_sha256=args.manifest_sha256,
                source_bundle_sha=args.source_bundle_sha,
                trading_date=args.trading_date,
                materialize=args.materialize,
                state_output=Path(args.state_output) if args.state_output else None,
            )
        elif args.command == "reserve":
            create_dispatch_reservation(
                Path(args.repo_root),
                trading_date=args.trading_date,
                source_commit_sha=args.source_commit_sha,
                manifest_path=args.manifest_path,
                manifest_sha256=args.manifest_sha256,
                source_bundle_sha=args.source_bundle_sha,
                baseline_run_id=int(args.baseline_run_id),
                dispatch_started_at=args.dispatch_started_at,
                expected_display_title=args.expected_display_title,
            )
        elif args.command == "verify-reservation":
            verify_dispatch_reservation(
                Path(args.repo_root),
                trading_date=args.trading_date,
                reservation_path=args.reservation_path,
                reservation_sha256=args.reservation_sha256,
                expected_head_sha=args.expected_head_sha,
                source_commit_sha=args.source_commit_sha,
                manifest_path=args.manifest_path,
                manifest_sha256=args.manifest_sha256,
                source_bundle_sha=args.source_bundle_sha,
                correlation_id=args.correlation_id,
            )
        elif args.command == "authority-status":
            identity = existing_authority_completion(
                Path(args.repo_root),
                args.trading_date,
                source_commit_sha=args.source_commit_sha,
                manifest_path=args.manifest_path,
                manifest_sha256=args.manifest_sha256,
                source_bundle_sha=args.source_bundle_sha,
            )
            _write_atomic(
                Path(args.output).resolve(),
                json_bytes(
                    {
                        "resume_required": identity is None,
                        "existing_authority": identity or {},
                    }
                ),
            )
        else:
            state = json.loads(Path(args.state).read_text(encoding="utf-8"))
            updates = {
                key: value
                for key, value in {
                    "source_bundle_commit_sha": args.source_bundle_commit_sha,
                    "resume_workflow_path": args.resume_workflow_path,
                    "resume_baseline_run_id": args.resume_baseline_run_id,
                    "resume_dispatch_started_at": args.resume_dispatch_started_at,
                    "resume_expected_head_sha": args.resume_expected_head_sha,
                    "resume_expected_display_title": args.resume_expected_display_title,
                    "resume_reservation_path": args.resume_reservation_path,
                    "resume_reservation_sha256": args.resume_reservation_sha256,
                    "resume_workflow_run_id": args.resume_workflow_run_id,
                    "resume_workflow_run_url": args.resume_workflow_run_url,
                    "resume_workflow_run_attempt": args.resume_workflow_run_attempt,
                    "resume_conclusion": args.resume_conclusion,
                    "existing_authority_release_id": args.existing_authority_release_id,
                    "existing_authority_generation_id": args.existing_authority_generation_id,
                    "existing_authority_commit_sha": args.existing_authority_commit_sha,
                    "error": args.error,
                }.items()
                if value != ""
            }
            updated = transition_state(state, args.to, **updates)
            _write_atomic(Path(args.output).resolve(), json_bytes(updated))
    except Exception as exc:
        print(f"ERROR: daily source recovery bundle failed: {exc}", file=sys.stderr)
        return 1
    print(f"daily source recovery bundle {args.command} passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
