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
RECOVERY_RETRY_REPAIR_PREFIXES = (
    ".github/workflows/",
    "scripts/",
    "tests/",
)
RECOVERY_RUN_PAGE_SIZE = 100
RECOVERY_RUN_MAX_PAGES = 10
RECOVERY_DISPATCH_WINDOW_SECONDS = 900

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
        "output/latest/official_price_fetch_latest.json",
        "output/latest/official_price_fetch_latest.md",
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
    expected_head_text = str(expected_head_sha or "").strip()
    head_sha = (
        checked_sha1(expected_head_text, "resume expected head SHA")
        if expected_head_text
        else ""
    )
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
            and (not head_sha or run.get("headSha") == head_sha)
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


def _run_value(run: dict[str, Any], *names: str) -> Any:
    for name in names:
        if name in run:
            return run[name]
    return None


def checked_run_id(value: object, label: str) -> int:
    text = str(value or "").strip()
    if not text.isdigit() or int(text) <= 0:
        raise DailySourceRecoveryError(f"invalid {label}: {value!r}")
    return int(text)


def _workflow_run_identity(run: dict[str, Any]) -> tuple[object, ...]:
    return (
        checked_run_id(_run_value(run, "databaseId", "id"), "observed recovery run id"),
        int(_run_value(run, "attempt", "run_attempt") or 0),
        str(_run_value(run, "event") or ""),
        str(_run_value(run, "workflowName") or ""),
        str(_run_value(run, "name") or ""),
        str(_run_value(run, "path") or ""),
        str(_run_value(run, "headBranch", "head_branch") or ""),
        checked_sha1(_run_value(run, "headSha", "head_sha"), "observed recovery head SHA"),
        str(_run_value(run, "displayTitle", "display_title") or ""),
        _parse_utc(
            _run_value(run, "createdAt", "created_at"), "workflow run created_at"
        ).isoformat(),
    )


def collect_paginated_workflow_runs(
    fetch_page: Callable[[int, int], list[dict[str, Any]]],
    *,
    page_size: int = RECOVERY_RUN_PAGE_SIZE,
    max_pages: int = RECOVERY_RUN_MAX_PAGES,
) -> list[dict[str, Any]]:
    if page_size <= 0 or max_pages <= 0:
        raise DailySourceRecoveryError("workflow run pagination bounds must be positive")
    collected: list[dict[str, Any]] = []
    seen_ids: set[int] = set()
    for page in range(1, max_pages + 1):
        rows = fetch_page(page, page_size)
        if not isinstance(rows, list) or not all(isinstance(row, dict) for row in rows):
            raise DailySourceRecoveryError("workflow run API page must be a JSON list of objects")
        if len(rows) > page_size:
            raise DailySourceRecoveryError("workflow run API page exceeds the requested page size")
        for row in rows:
            run_id = checked_run_id(
                _run_value(row, "databaseId", "id"), "observed recovery run id"
            )
            if run_id in seen_ids:
                raise DailySourceRecoveryError(
                    f"workflow run pagination returned duplicate run id: {run_id}"
                )
            seen_ids.add(run_id)
            collected.append(row)
        if len(rows) < page_size:
            return collected
    raise DailySourceRecoveryError(
        f"workflow run collection exceeded the bounded {max_pages}-page limit"
    )


def collect_stable_paginated_workflow_runs(
    fetch_page: Callable[[int, int], list[dict[str, Any]]],
) -> list[dict[str, Any]]:
    first = collect_paginated_workflow_runs(fetch_page)
    second = collect_paginated_workflow_runs(fetch_page)
    if [_workflow_run_identity(run) for run in first] != [
        _workflow_run_identity(run) for run in second
    ]:
        raise DailySourceRecoveryError(
            "workflow run pagination changed between bounded collection passes"
        )
    return second


def fetch_stable_workflow_dispatch_runs(repository: str) -> list[dict[str, Any]]:
    repo = str(repository or "").strip()
    if re.fullmatch(r"[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+", repo) is None:
        raise DailySourceRecoveryError(f"invalid GitHub repository identity: {repo!r}")

    def fetch_page(page: int, page_size: int) -> list[dict[str, Any]]:
        url = (
            f"/repos/{repo}/actions/workflows/daily_full_pipeline.yml/runs"
            f"?event=workflow_dispatch&per_page={page_size}&page={page}"
        )
        try:
            proc = subprocess.run(
                ["gh", "api", url],
                check=False,
                capture_output=True,
                timeout=30,
            )
        except subprocess.TimeoutExpired as exc:
            raise DailySourceRecoveryError(
                f"GitHub workflow run page {page} timed out"
            ) from exc
        if proc.returncode != 0:
            detail = (proc.stderr or proc.stdout).decode("utf-8", errors="replace").strip()
            raise DailySourceRecoveryError(
                f"GitHub workflow run page {page} failed: {detail}"
            )
        try:
            payload = json.loads(proc.stdout.decode("utf-8", errors="strict"))
        except (UnicodeDecodeError, json.JSONDecodeError) as exc:
            raise DailySourceRecoveryError(
                f"GitHub workflow run page {page} is not valid UTF-8 JSON"
            ) from exc
        rows = payload.get("workflow_runs") if isinstance(payload, dict) else None
        if not isinstance(rows, list):
            raise DailySourceRecoveryError(
                f"GitHub workflow run page {page} has no workflow_runs list"
            )
        return rows

    return collect_stable_paginated_workflow_runs(fetch_page)


def _matches_daily_full_run_identity(
    run: dict[str, Any], *, expected_title: str
) -> bool:
    if _run_value(run, "event") != "workflow_dispatch":
        return False
    if _run_value(run, "path") != WORKFLOW_PATH:
        return False
    if _run_value(run, "headBranch", "head_branch") != "main":
        return False
    if _run_value(run, "displayTitle", "display_title") != expected_title:
        return False
    legacy_name = str(_run_value(run, "workflowName") or "").strip()
    rest_name = _run_value(run, "name")
    if legacy_name:
        if legacy_name != "Daily Full Pipeline":
            return False
        return rest_name is None or str(rest_name) == expected_title
    return str(rest_name or "") == expected_title


def _immutable_recovery_protected_paths(
    *,
    reservation_path: str,
    manifest_path: str,
    source_manifest: dict[str, Any],
) -> set[str]:
    manifest_relative = PurePosixPath(checked_relative_path(manifest_path))
    market_session = source_manifest.get("market_session")
    if not isinstance(market_session, dict):
        raise DailySourceRecoveryError("source bundle market_session contract is missing")
    market_bundle_path = checked_relative_path(market_session.get("bundle_path"))
    return {
        checked_relative_path(reservation_path),
        manifest_relative.as_posix(),
        (manifest_relative.parent / "state.json").as_posix(),
        market_bundle_path,
        *(
            checked_relative_path(entry["path"])
            for entry in source_manifest["files"]
        ),
        *(
            checked_relative_path(entry["bundle_path"])
            for entry in source_manifest["files"]
        ),
    }


def verify_failed_recovery_retry_runs(
    root: Path,
    runs: list[dict[str, Any]],
    *,
    reservation_commit_sha: str,
    reservation_payload: dict[str, Any],
    trading_date: str,
    retry_of_run_id: object,
    current_run_id: object,
    current_head_sha: str,
) -> dict[str, dict[str, Any]]:
    root = root.resolve()
    date_text = normalized_date(trading_date)
    reservation_commit = checked_sha1(
        reservation_commit_sha, "recovery reservation commit SHA"
    )
    prior_id = checked_run_id(retry_of_run_id, "failed recovery run id")
    current_id = checked_run_id(current_run_id, "current recovery run id")
    if prior_id == current_id:
        raise DailySourceRecoveryError("failed and current recovery run ids must differ")
    head_sha = checked_sha1(current_head_sha, "current recovery head SHA")
    expected_title = f"Daily Full Pipeline | recovery=daily-source-{date_text}"
    if reservation_payload.get("trading_date") != date_text:
        raise DailySourceRecoveryError("retry reservation trading date mismatch")
    if reservation_payload.get("resume_expected_display_title") != expected_title:
        raise DailySourceRecoveryError("retry reservation display title mismatch")
    try:
        baseline_run_id = int(reservation_payload.get("resume_baseline_run_id"))
    except (TypeError, ValueError) as exc:
        raise DailySourceRecoveryError("retry reservation baseline run id is invalid") from exc
    if baseline_run_id < 0:
        raise DailySourceRecoveryError("retry reservation baseline run id is invalid")
    if prior_id <= baseline_run_id or current_id <= baseline_run_id:
        raise DailySourceRecoveryError(
            "failed and current recovery run ids must be newer than the reservation baseline"
        )
    dispatch_started = _parse_utc(
        reservation_payload.get("resume_dispatch_started_at"),
        "retry reservation dispatch time",
    )
    anchor_earliest = dispatch_started - timedelta(seconds=15)
    anchor_latest = dispatch_started + timedelta(seconds=RECOVERY_DISPATCH_WINDOW_SECONDS)
    source_manifest = verify_bundle_from_git(
        root,
        source_commit_sha=str(reservation_payload.get("source_bundle_commit_sha") or ""),
        manifest_path=str(reservation_payload.get("source_bundle_manifest_path") or ""),
        manifest_sha256=str(
            reservation_payload.get("source_bundle_manifest_sha256") or ""
        ),
        source_bundle_sha=str(reservation_payload.get("source_bundle_sha") or ""),
        trading_date=date_text,
    )
    protected_paths = _immutable_recovery_protected_paths(
        reservation_path=dispatch_reservation_path(date_text).as_posix(),
        manifest_path=str(
            reservation_payload.get("source_bundle_manifest_path") or ""
        ),
        source_manifest=source_manifest,
    )
    matches = [
        run
        for run in runs
        if _matches_daily_full_run_identity(run, expected_title=expected_title)
    ]
    by_id: dict[int, dict[str, Any]] = {}
    for run in matches:
        run_id = checked_run_id(
            _run_value(run, "databaseId", "id"), "observed recovery run id"
        )
        if run_id in by_id:
            raise DailySourceRecoveryError(
                f"failed-recovery retry title set contains duplicate run id: {run_id}"
            )
        by_id[run_id] = run
    if current_id not in by_id or prior_id not in by_id:
        raise DailySourceRecoveryError(
            "failed-recovery retry title set must contain the designated prior failure "
            f"and current attempt: observed={sorted(by_id)}"
        )
    current = by_id[current_id]
    if (
        int(_run_value(current, "attempt", "run_attempt") or 0) != 1
        or _run_value(current, "status") not in {"queued", "in_progress"}
        or str(_run_value(current, "conclusion") or "") != ""
        or _run_value(current, "headSha", "head_sha") != head_sha
    ):
        raise DailySourceRecoveryError(
            "current retry run must be the unique attempt=1 run at the current head"
        )
    current_created = _parse_utc(
        _run_value(current, "createdAt", "created_at"), "current retry created_at"
    )
    historical_candidates: list[tuple[datetime, int, str, dict[str, Any]]] = []
    for run_id, run in by_id.items():
        if run_id == current_id:
            continue
        if run_id <= baseline_run_id:
            continue
        if (
            run_id >= current_id
            or int(_run_value(run, "attempt", "run_attempt") or 0) != 1
            or _run_value(run, "status") != "completed"
            or _run_value(run, "conclusion") != "failure"
        ):
            raise DailySourceRecoveryError(
                "every historical recovery run must be a newer-than-baseline "
                "completed failure with run_attempt=1"
            )
        created_at = _parse_utc(
            _run_value(run, "createdAt", "created_at"), "historical retry created_at"
        )
        if (created_at, run_id) >= (current_created, current_id):
            raise DailySourceRecoveryError(
                "historical recovery run must predate the current retry"
            )
        run_head = checked_sha1(
            _run_value(run, "headSha", "head_sha"), "historical recovery head SHA"
        )
        historical_candidates.append((created_at, run_id, run_head, run))
    if not historical_candidates:
        raise DailySourceRecoveryError(
            "failed-recovery history must contain an initial completed failure"
        )
    anchor_created, anchor_id, anchor_head, anchor = min(
        historical_candidates, key=lambda item: (item[0], item[1])
    )
    if not anchor_earliest <= anchor_created <= anchor_latest:
        raise DailySourceRecoveryError(
            "the earliest post-baseline recovery failure must be inside the original "
            "reservation dispatch window"
        )
    verify_nonoverlapping_dispatch_descendant(
        root,
        reservation_commit_sha=reservation_commit,
        current_head_sha=anchor_head,
        protected_paths=protected_paths,
    )
    ordered_historical = sorted(
        historical_candidates, key=lambda item: (item[0], item[1])
    )
    historical: list[tuple[datetime, int, dict[str, Any]]] = [
        (anchor_created, anchor_id, anchor)
    ]
    previous_head = anchor_head
    for created_at, run_id, run_head, run in ordered_historical[1:]:
        verify_bounded_retry_descendant(
            root,
            failed_head_sha=previous_head,
            retry_head_sha=run_head,
            protected_paths=protected_paths,
        )
        historical.append((created_at, run_id, run))
        previous_head = run_head
    _latest_created, latest_id, prior = historical[-1]
    if latest_id != prior_id:
        raise DailySourceRecoveryError(
            "retry_of_run_id must identify the latest related completed failure: "
            f"expected={latest_id} observed={prior_id}"
        )
    verify_bounded_retry_descendant(
        root,
        failed_head_sha=previous_head,
        retry_head_sha=head_sha,
        protected_paths=protected_paths,
    )
    return {"anchor": anchor, "prior": prior, "current": current}


def _git_raw_diff_entries(
    root: Path,
    *,
    base_sha: str,
    head_sha: str,
    label: str,
) -> list[tuple[str, str, str, str]]:
    raw = git_output(
        root,
        "diff",
        "--raw",
        "--no-abbrev",
        "--no-renames",
        base_sha,
        head_sha,
        "--",
    ).decode("utf-8", errors="strict")
    entries: list[tuple[str, str, str, str]] = []
    paths: set[str] = set()
    for line in raw.splitlines():
        try:
            metadata, raw_path = line.split("\t", 1)
        except ValueError as exc:
            raise DailySourceRecoveryError(
                f"malformed {label} diff record: {line!r}"
            ) from exc
        fields = metadata.removeprefix(":").split()
        if len(fields) != 5:
            raise DailySourceRecoveryError(
                f"malformed {label} diff metadata: {metadata!r}"
            )
        old_mode, new_mode, _old_oid, _new_oid, status = fields
        path = checked_relative_path(raw_path)
        if path in paths:
            raise DailySourceRecoveryError(f"{label} changed path is duplicated: {path}")
        paths.add(path)
        entries.append((path, status, old_mode, new_mode))
    return entries


def verify_bounded_retry_descendant(
    root: Path,
    *,
    failed_head_sha: str,
    retry_head_sha: str,
    protected_paths: set[str],
) -> list[str]:
    root = root.resolve()
    failed_head = checked_sha1(failed_head_sha, "failed recovery head SHA")
    retry_head = checked_sha1(retry_head_sha, "recovery retry head SHA")
    if failed_head == retry_head:
        raise DailySourceRecoveryError(
            "failed-recovery retry requires a strict descendant of the failed head"
        )
    try:
        git_output(root, "merge-base", "--is-ancestor", failed_head, retry_head)
    except DailySourceRecoveryError as exc:
        raise DailySourceRecoveryError(
            "failed-recovery retry head is not a descendant of the failed head"
        ) from exc
    protected = {checked_relative_path(path) for path in protected_paths}
    paths: list[str] = []
    repair_paths: list[str] = []
    for path, status, old_mode, new_mode in _git_raw_diff_entries(
        root,
        base_sha=failed_head,
        head_sha=retry_head,
        label="failed-recovery retry",
    ):
        if status not in {"A", "M"}:
            raise DailySourceRecoveryError(
                f"failed-recovery retry cannot {status} path: {path}"
            )
        if status == "A":
            valid_mode = old_mode == "000000" and new_mode == "100644"
        else:
            valid_mode = old_mode == new_mode == "100644"
        if not valid_mode:
            raise DailySourceRecoveryError(
                "failed-recovery retry path mode/type drift is forbidden: "
                f"path={path} old_mode={old_mode} new_mode={new_mode}"
            )
        if path in protected:
            raise DailySourceRecoveryError(
                f"failed-recovery retry changed immutable protected path: {path}"
            )
        paths.append(path)
        if path.startswith(RECOVERY_RETRY_REPAIR_PREFIXES):
            repair_paths.append(path)
    if not repair_paths:
        raise DailySourceRecoveryError(
            "failed-recovery retry descendant has no repair path under "
            ".github/workflows/, scripts/, or tests/"
        )
    return paths


def verify_nonoverlapping_dispatch_descendant(
    root: Path,
    *,
    reservation_commit_sha: str,
    current_head_sha: str,
    protected_paths: set[str],
) -> list[str]:
    reservation_commit = checked_sha1(
        reservation_commit_sha, "recovery reservation commit SHA"
    )
    current_head = checked_sha1(current_head_sha, "recovery current head SHA")
    if reservation_commit == current_head:
        return []
    git_output(root, "merge-base", "--is-ancestor", reservation_commit, current_head)
    changed_paths = [
        path
        for path, _status, _old_mode, _new_mode in _git_raw_diff_entries(
            root,
            base_sha=reservation_commit,
            head_sha=current_head,
            label="recovery dispatch descendant",
        )
    ]
    overlap = sorted(set(changed_paths) & protected_paths)
    if overlap:
        raise DailySourceRecoveryError(
            "recovery dispatch descendant changed reserved source paths: "
            + ",".join(overlap)
        )
    return changed_paths


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
    reservation_commit_sha: str = "",
    retry_of_run_id: str = "",
) -> dict[str, Any]:
    root = root.resolve()
    date_text = normalized_date(trading_date)
    head_sha = checked_sha1(expected_head_sha, "recovery expected head SHA")
    if git_head(root) != head_sha:
        raise DailySourceRecoveryError("dispatch reservation checkout does not equal expected head")
    reservation_commit_text = str(reservation_commit_sha or "").strip()
    retry_run_text = str(retry_of_run_id or "").strip()
    if retry_run_text and not reservation_commit_text:
        raise DailySourceRecoveryError(
            "failed recovery run id requires a recovery reservation commit"
        )
    if reservation_commit_text:
        reservation_commit = checked_sha1(
            reservation_commit_text, "recovery reservation commit SHA"
        )
    else:
        reservation_commit = head_sha
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
    source_commit = checked_sha1(source_commit_sha, "source bundle commit SHA")
    git_output(root, "merge-base", "--is-ancestor", source_commit, head_sha)
    protected_paths = _immutable_recovery_protected_paths(
        reservation_path=path,
        manifest_path=manifest_path,
        source_manifest=source_manifest,
    )
    if retry_run_text:
        checked_run_id(retry_run_text, "failed recovery run id")
    verify_nonoverlapping_dispatch_descendant(
        root,
        reservation_commit_sha=reservation_commit,
        current_head_sha=head_sha,
        protected_paths=protected_paths,
    )
    payload_bytes = git_blob(root, reservation_commit, path)
    if sha256_bytes(payload_bytes) != expected_sha:
        raise DailySourceRecoveryError("dispatch reservation Git object SHA-256 mismatch")
    if git_mode(root, reservation_commit, path) != "100644":
        raise DailySourceRecoveryError("dispatch reservation Git mode must equal 100644")
    if git_blob(root, head_sha, path) != payload_bytes or git_mode(root, head_sha, path) != "100644":
        raise DailySourceRecoveryError(
            "current HEAD reservation bytes or mode differ from reservation commit"
        )
    working_path = root / path
    if not working_path.is_file() or working_path.read_bytes() != payload_bytes:
        raise DailySourceRecoveryError("dispatch reservation working bytes differ from Git object")
    parent_sha = subprocess.check_output(
        ["git", "rev-parse", f"{reservation_commit}^"], cwd=root, text=True
    ).strip()
    changed_paths = subprocess.check_output(
        ["git", "diff-tree", "--no-commit-id", "--name-only", "-r", reservation_commit],
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
    if retry_run_text:
        expected_prefix = f"manual-resume-{date_text}-"
        if not str(correlation_id).startswith(expected_prefix) or re.fullmatch(
            r"[A-Za-z0-9._-]{16,128}", str(correlation_id)
        ) is None:
            raise DailySourceRecoveryError(
                "failed-recovery retry correlation id is invalid"
            )
    elif correlation_id != expected_correlation:
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
    confirmation = manifest.get("official_price_confirmation")
    if not isinstance(confirmation, dict):
        raise DailySourceRecoveryError("source bundle official-price confirmation is missing")
    entries_by_path = {str(entry.get("path") or ""): entry for entry in files}
    expected_confirmation_paths = {
        "path": f"data/daily_price/daily_price_{trading_date}.csv",
        "fetch_status_path": "output/latest/official_price_fetch_latest.json",
        "fetch_markdown_path": "output/latest/official_price_fetch_latest.md",
    }
    for field, expected_path in expected_confirmation_paths.items():
        if confirmation.get(field) != expected_path:
            raise DailySourceRecoveryError(
                f"source bundle official-price confirmation {field} mismatch"
            )
    identity_fields = {
        "path": ("price_bytes", "price_sha256"),
        "fetch_status_path": ("fetch_status_bytes", "fetch_status_sha256"),
        "fetch_markdown_path": ("fetch_markdown_bytes", "fetch_markdown_sha256"),
    }
    for path_field, (bytes_field, sha_field) in identity_fields.items():
        entry = entries_by_path[confirmation[path_field]]
        if (
            int(confirmation.get(bytes_field) or -1) != int(entry.get("bytes") or -1)
            or confirmation.get(sha_field) != entry.get("sha256")
        ):
            raise DailySourceRecoveryError(
                f"source bundle official-price confirmation identity mismatch: {confirmation[path_field]}"
            )
    if (
        int(confirmation.get("twse_rows") or 0) <= 0
        or int(confirmation.get("tpex_rows") or 0) <= 0
        or int(confirmation.get("total_rows") or 0)
        != int(confirmation.get("twse_rows") or 0) + int(confirmation.get("tpex_rows") or 0)
    ):
        raise DailySourceRecoveryError("source bundle official-price row confirmation is invalid")
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
    if not official_latest.is_file() or official_latest.is_symlink():
        raise DailySourceRecoveryError("official daily price latest path is not a safe regular file")
    if official_latest.read_bytes() != price_payload:
        raise DailySourceRecoveryError(
            "official daily price latest does not match the date-bound repair projection"
        )
    confirmed, confirmation, confirmation_reason = (
        market_session_calendar.read_official_price_confirmation(root, date_text)
    )
    if not confirmed:
        raise DailySourceRecoveryError(
            f"official price confirmation is not date-bound: {confirmation_reason}"
        )
    final_published = False
    entries: list[dict[str, Any]] = []
    try:
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
            "official_price_confirmation": confirmation,
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
    verify_reservation.add_argument("--reservation-commit-sha", default="")
    verify_reservation.add_argument("--retry-of-run-id", default="")
    collect_retry_runs = sub.add_parser("collect-retry-runs")
    collect_retry_runs.add_argument("--repository", required=True)
    collect_retry_runs.add_argument("--output", required=True)
    retry_runs = sub.add_parser("verify-retry-runs")
    retry_runs.add_argument("--repo-root", default=".")
    retry_runs.add_argument("--runs-json", required=True)
    retry_runs.add_argument("--reservation-commit-sha", required=True)
    retry_runs.add_argument("--reservation-path", required=True)
    retry_runs.add_argument("--trading-date", required=True)
    retry_runs.add_argument("--retry-of-run-id", required=True)
    retry_runs.add_argument("--current-run-id", required=True)
    retry_runs.add_argument("--current-head-sha", required=True)
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
                reservation_commit_sha=args.reservation_commit_sha,
                retry_of_run_id=args.retry_of_run_id,
            )
        elif args.command == "collect-retry-runs":
            runs = fetch_stable_workflow_dispatch_runs(args.repository)
            _write_atomic(
                Path(args.output).resolve(),
                (json.dumps(runs, ensure_ascii=False, indent=2) + "\n").encode("utf-8"),
            )
        elif args.command == "verify-retry-runs":
            runs = json.loads(Path(args.runs_json).read_text(encoding="utf-8"))
            if not isinstance(runs, list) or not all(isinstance(run, dict) for run in runs):
                raise DailySourceRecoveryError("retry run evidence must be a JSON list of objects")
            root = Path(args.repo_root).resolve()
            reservation_commit = checked_sha1(
                args.reservation_commit_sha, "recovery reservation commit SHA"
            )
            reservation_path = checked_relative_path(args.reservation_path)
            try:
                reservation_payload = json.loads(
                    git_blob(root, reservation_commit, reservation_path).decode(
                        "utf-8", errors="strict"
                    )
                )
            except (UnicodeDecodeError, json.JSONDecodeError) as exc:
                raise DailySourceRecoveryError(
                    "retry reservation Git object is not valid UTF-8 JSON"
                ) from exc
            if not isinstance(reservation_payload, dict):
                raise DailySourceRecoveryError("retry reservation payload must be a JSON object")
            verify_failed_recovery_retry_runs(
                root,
                runs,
                reservation_commit_sha=reservation_commit,
                reservation_payload=reservation_payload,
                trading_date=args.trading_date,
                retry_of_run_id=args.retry_of_run_id,
                current_run_id=args.current_run_id,
                current_head_sha=args.current_head_sha,
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
