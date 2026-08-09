#!/usr/bin/env python3
"""Run the date-locked, validation-only Daily Full historical replay."""

from __future__ import annotations

import argparse
import contextlib
import csv
import hashlib
import io
import json
import os
import re
import shutil
import stat
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Iterable, Sequence


ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

import scripts.daily_full_validation_replay_checkpoint as checkpoint  # noqa: E402
from scripts import replay_historical_structured_sources as historical_replay  # noqa: E402


REPLAY_DATE = "20260807"
OLD_FAILED_RUN_ID = "31174813266"
AUTHORIZED_CHECKPOINT_SOURCE_SHA = "4d715065f38389752aaeaa0c511280c47ccedc08"
AUTHORIZED_CHECKPOINT_RUN_ID = "31268964962"
AUTHORIZED_CHECKPOINT_ARTIFACT_ID = "9025240156"
AUTHORIZED_CHECKPOINT_ARTIFACT_DIGEST = (
    "sha256:492038fcf6c2a443ac2c77423624700d174a7d3522fc581673ef48b8314927fd"
)
AUTHORIZED_CHECKPOINT_MANIFEST_SHA256 = (
    "a8b7ac80d5342a72e0f1df823392025f26d18c4494aae32a7137e11f1aa1fd96"
)
AUTHORIZED_PRODUCER_FIX_COMMIT = "33568e1e3cc33530a4af65f4d50cda6fcf17b77d"
AUTHORIZED_PRODUCER_FIX_PATHS = (
    "config/daily_model_semantic_migrations.csv",
    "config/daily_model_semantic_ownership.csv",
    "config/daily_model_shared_semantic_registry.csv",
    "config/model_research_shared_utility_migrations.csv",
    "config/model_research_shared_utility_registry.csv",
    "scripts/build_daily_candidate_model_layer.py",
    "scripts/validate_daily_canonical_field_lineage.py",
    "scripts/validate_daily_warrant_formal_sync_scope.py",
    "tests/test_daily_candidate_model_layer.py",
    "tests/test_daily_canonical_field_lineage.py",
    "tests/test_daily_warrant_formal_sync_scope.py",
    "tests/test_model_data_independence.py",
)
AUTHORIZED_VALIDATOR_FIX_COMMIT = "898656c1167bbe5cc8b4a7e31e2b507cb144a657"
AUTHORIZED_VALIDATOR_FIX_PATHS = (
    "scripts/validate_daily_canonical_field_lineage.py",
    "tests/test_daily_canonical_field_lineage.py",
)
AUTHORIZED_FORMAL_LINEAGE_FIX_COMMIT = (
    "f677331954f8baef3aad17cfff1d0866df0db2bc"
)
AUTHORIZED_FORMAL_LINEAGE_FIX_PATHS = (
    "scripts/build_daily_volume_breakout_operation_section.py",
    "tests/test_daily_volume_breakout_operation_section.py",
)
AUTHORIZED_OPERATION_COMPLETENESS_FIX_COMMIT = (
    "954db8310d2bd5f0ab7d43655afaa45d09f7c5e3"
)
AUTHORIZED_OPERATION_COMPLETENESS_FIX_PATHS = (
    "scripts/validate_daily_volume_breakout_operation_section.py",
    "tests/test_daily_volume_breakout_operation_section.py",
)
AUTHORIZED_FORMAL_OPERATION_SHARED_PATH = (
    "tests/test_daily_volume_breakout_operation_section.py"
)
PIPELINE_WORKFLOW = Path(".github/workflows/daily_full_pipeline.yml")
HISTORICAL_REPLAY_SCRIPT = Path(
    "scripts/replay_historical_structured_sources.py"
)
HISTORICAL_REPLAY_VALIDATOR = Path(
    "scripts/validate_historical_structured_source_replay.py"
)
HISTORICAL_REPLAY_PLANNER = Path(
    "scripts/plan_historical_structured_source_replay.py"
)
PRE_STEP_NAMES = (
    "Build monthly revenue history",
    "Run daily stock monitor",
    "Validate daily candidate regression cases",
    "Build revenue breakout low response candidates",
    "Build data freshness status after stock monitor",
    "Fetch market abnormal status",
    "Inspect daily stock monitor output",
    "Build all candidates latest files",
    "Build stock-level warrant flow",
    "Merge warrant flow into candidates",
    "Apply revenue industry applicability rules",
    "Update catalyst data tables",
    "Record calendar source status before integrity gate",
    "Refresh data freshness before external-source integrity gate",
    "Validate refreshed external-source integrity",
    "Apply fundamental and event catalyst layer",
    "Update candidate repeat appearance tracking",
    "Build stock theme taxonomy",
    "Remove deprecated daily candidate decision artifacts",
    "Build daily theme leadership layer",
    "Build volume breakout watch",
)
POST_START_STEP = "Build volume attack theme layer"
POST_END_STEP = "Validate catalyst layer"
MUTABLE_POST_COMMANDS = frozenset(
    {"python scripts/fetch_futures_options_indicators.py"}
)
MODEL_SIGNAL_PATH = Path(
    "output/latest/daily_candidate_model_signals_for_report_latest.csv"
)
ALL_CANDIDATES_PATH = Path("output/latest/all_candidates_latest.csv")
WARRANT_FLOW_PATH = Path("output/latest/warrant_flow_latest.csv")
THEME_STOCK_PATH = Path(
    "output/latest/volume_attack_theme_stocks_latest.csv"
)
MODEL_SIGNAL_VALIDATION_PATH = Path(
    "output/latest/daily_candidate_model_layer_validation_latest.json"
)
THEME_VALIDATION_PATH = Path(
    "output/latest/volume_attack_theme_layer_validation_latest.json"
)
REGISTERED_PARITY_VALIDATOR_PATHS = (
    Path("scripts/validate_daily_candidate_model_layer.py"),
    Path("scripts/validate_volume_attack_theme_layer.py"),
    Path("scripts/validate_daily_warrant_formal_sync_scope.py"),
)
REGISTERED_PARITY_VALIDATOR_ARGUMENTS = {
    Path("scripts/validate_daily_candidate_model_layer.py"): (),
    Path("scripts/validate_volume_attack_theme_layer.py"): (),
    Path("scripts/validate_daily_warrant_formal_sync_scope.py"): (
        "--validate-source-date",
    ),
}
PARITY_EVIDENCE_PATHS = (
    MODEL_SIGNAL_PATH,
    ALL_CANDIDATES_PATH,
    WARRANT_FLOW_PATH,
    THEME_STOCK_PATH,
    MODEL_SIGNAL_VALIDATION_PATH,
    THEME_VALIDATION_PATH,
)
FRESHNESS_PATH = Path("output/latest/data_freshness_latest.csv")
AUTHORIZED_PUBLISH_BASELINE_DATE = "20260805"
PUBLISH_BASELINE_DIRNAME = "tdcc_daily_baseline"
PUBLISH_BASELINE_EVIDENCE_PATH = Path(
    "output/validation_replay/20260807/"
    "publish_freshness_baseline_evidence.json"
)
MARKET_SESSION_PATH = Path(
    "output/latest/market_session_status_latest.json"
)
README_PATH = Path("output/latest/READ_ME_FIRST_DAILY_REPORT.txt")
PACKET_PATH = Path(
    "output/latest/chatgpt_daily_report_packet_latest.txt"
)
VALIDATION_SOURCE_STATE_PATH = Path(
    "output/validation_replay/20260807/validation_source_state.json"
)
PARITY_EVIDENCE_PATH = Path(
    "output/validation_replay/20260807/"
    "producer_consumer_parity_evidence.json"
)
STEP_RESULTS_PATH = Path(
    "output/validation_replay/20260807/step_results.json"
)
DELETION_MANIFEST_PATH = Path(
    "output/validation_replay/20260807/deleted_paths.json"
)
SOURCE_REVISION_FILENAME = "source_revision_manifest.json"
PRICE_HISTORY_EXTENSION_MANIFEST = "price_history_extension_manifest.json"
PRICE_HISTORY_EXTENSION_ALLOWED_PREFIXES = (
    "data/stock_price_history/",
)
PRICE_HISTORY_EXTENSION_ALLOWED_FILES = frozenset(
    {
        f"data/daily_price/{REPLAY_DATE}.csv",
        f"data/daily_price/daily_price_{REPLAY_DATE}.csv",
        "output/latest/official_daily_price_latest.csv",
        "output/latest/official_price_fetch_latest.json",
        "output/latest/official_price_fetch_latest.md",
        "output/latest/stock_price_history_manifest.csv",
        "output/latest/stock_price_history_manifest.json",
        "output/latest/stock_price_history_manifest.md",
        "docs/latest/stock_price_history_manifest.csv",
        "docs/latest/stock_price_history_manifest.json",
        "docs/latest/stock_price_history_manifest.md",
    }
)
PRICE_HISTORY_EXTENSION_REQUIRED_FILES = PRICE_HISTORY_EXTENSION_ALLOWED_FILES
ALLOWED_CHECKPOINT_PREFIXES = ("data", "output", "docs")
class ValidationReplayError(RuntimeError):
    """A fail-closed validation replay contract violation."""


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def canonical_json_bytes(value: object) -> bytes:
    return (
        json.dumps(
            value,
            ensure_ascii=False,
            sort_keys=True,
            separators=(",", ":"),
        )
        + "\n"
    ).encode("utf-8")


def require_exact_date(value: str, label: str) -> str:
    if value != REPLAY_DATE:
        raise ValidationReplayError(
            f"{label} must equal {REPLAY_DATE}; observed={value}"
        )
    return value


def require_sha(value: str, label: str) -> str:
    normalized = str(value).strip().lower()
    if not re.fullmatch(r"[0-9a-f]{40}", normalized):
        raise ValidationReplayError(
            f"{label} must be an exact 40-character Git SHA"
        )
    return normalized


def run_command(
    command: Sequence[str],
    *,
    cwd: Path,
    env: dict[str, str],
    label: str,
) -> str:
    checkpoint.assert_validation_only_command(command)
    result = subprocess.run(
        [str(part) for part in command],
        cwd=cwd,
        env=env,
        text=True,
        encoding="utf-8",
        errors="replace",
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        check=False,
    )
    if result.stdout:
        print(result.stdout.rstrip())
    if result.returncode:
        raise ValidationReplayError(
            f"{label} failed with exit={result.returncode}"
        )
    return result.stdout


def run_bash_block(
    script: str,
    *,
    cwd: Path,
    env: dict[str, str],
    label: str,
) -> str:
    checkpoint.assert_validation_only_command(script)
    result = subprocess.run(
        ["bash", "--noprofile", "--norc", "-euo", "pipefail", "-c", script],
        cwd=cwd,
        env=env,
        text=True,
        encoding="utf-8",
        errors="replace",
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        check=False,
    )
    if result.stdout:
        print(result.stdout.rstrip())
    if result.returncode:
        raise ValidationReplayError(
            f"{label} failed with exit={result.returncode}"
        )
    return result.stdout


def apply_github_environment(env: dict[str, str]) -> None:
    path = Path(env["GITHUB_ENV"])
    if not path.is_file():
        return
    lines = path.read_text(encoding="utf-8").splitlines()
    index = 0
    while index < len(lines):
        line = lines[index]
        index += 1
        if not line:
            continue
        if "<<" in line:
            name, delimiter = line.split("<<", 1)
            name = name.strip()
            delimiter = delimiter.strip()
            values: list[str] = []
            while index < len(lines) and lines[index] != delimiter:
                values.append(lines[index])
                index += 1
            if index >= len(lines):
                raise ValidationReplayError(
                    f"unterminated GITHUB_ENV value for {name}"
                )
            index += 1
            env[name] = "\n".join(values)
            continue
        if "=" not in line:
            raise ValidationReplayError(
                f"invalid GITHUB_ENV line: {line!r}"
            )
        name, value = line.split("=", 1)
        if not name.strip():
            raise ValidationReplayError(
                "GITHUB_ENV variable name cannot be empty"
            )
        env[name.strip()] = value


def parse_workflow_run_steps(path: Path) -> list[tuple[str, str]]:
    lines = path.read_text(encoding="utf-8").splitlines()
    try:
        job_start = lines.index("  daily-full-pipeline:") + 1
    except ValueError as error:
        raise ValidationReplayError(
            "daily-full-pipeline job is missing"
        ) from error
    job_end = len(lines)
    for candidate in range(job_start, len(lines)):
        if re.match(r"^  [A-Za-z0-9_-]+:\s*$", lines[candidate]):
            job_end = candidate
            break
    lines = lines[job_start:job_end]
    steps: list[tuple[str, str]] = []
    index = 0
    while index < len(lines):
        match = re.match(r"^      - name:\s*(.+?)\s*$", lines[index])
        if not match:
            index += 1
            continue
        name = match.group(1).strip().strip('"').strip("'")
        cursor = index + 1
        run_index: int | None = None
        while cursor < len(lines):
            if re.match(r"^      - name:", lines[cursor]):
                break
            if re.match(r"^        run:\s*\|\s*$", lines[cursor]):
                run_index = cursor + 1
                break
            cursor += 1
        if run_index is None:
            index = cursor
            continue
        body: list[str] = []
        cursor = run_index
        while cursor < len(lines):
            line = lines[cursor]
            if line and len(line) - len(line.lstrip(" ")) < 10:
                break
            body.append(line[10:] if line else "")
            cursor += 1
        steps.append((name, "\n".join(body).rstrip() + "\n"))
        index = cursor
    return steps


def step_map(repo_root: Path) -> dict[str, str]:
    parsed = parse_workflow_run_steps(repo_root / PIPELINE_WORKFLOW)
    result: dict[str, str] = {}
    for name, script in parsed:
        if name in result:
            raise ValidationReplayError(
                f"workflow step name is not unique: {name}"
            )
        result[name] = script
    return result


def post_step_names(repo_root: Path) -> list[str]:
    names = [
        name
        for name, _script in parse_workflow_run_steps(
            repo_root / PIPELINE_WORKFLOW
        )
    ]
    try:
        start = names.index(POST_START_STEP)
        end = names.index(POST_END_STEP)
    except ValueError as error:
        raise ValidationReplayError(
            "production post-step replay boundaries are missing"
        ) from error
    if end < start:
        raise ValidationReplayError(
            "production post-step replay boundaries are reversed"
        )
    return names[start : end + 1]


def remove_mutable_post_commands(script: str) -> str:
    retained: list[str] = []
    removed: set[str] = set()
    for line in script.splitlines():
        stripped = line.strip().rstrip("\\").strip()
        if stripped in MUTABLE_POST_COMMANDS:
            removed.add(stripped)
            continue
        retained.append(line)
    unknown = removed - MUTABLE_POST_COMMANDS
    if unknown:
        raise ValidationReplayError(
            f"unknown mutable post commands: {sorted(unknown)}"
        )
    return "\n".join(retained).rstrip() + "\n"


def base_environment(
    *,
    repo_root: Path,
    runner_temp: Path,
    source_sha: str,
) -> dict[str, str]:
    env = os.environ.copy()
    env.update(
        {
            "PYTHONIOENCODING": "utf-8",
            "PYTHONDONTWRITEBYTECODE": "1",
            "EXPECTED_MAIN_PRICE_DATE": REPLAY_DATE,
            "HISTORICAL_REPLAY_MAIN_PRICE_DATE": REPLAY_DATE,
            "VALIDATION_REPLAY_MAIN_PRICE_DATE": REPLAY_DATE,
            "DAILY_FULL_VALIDATION_ONLY": "1",
            "DAILY_FULL_VALIDATION_SOURCE_SHA": source_sha,
            "RUNNER_TEMP": str(runner_temp),
            "GITHUB_ENV": str(runner_temp / "github_env"),
            "GITHUB_OUTPUT": str(runner_temp / "github_output"),
            "PYTHONPATH": str(repo_root),
        }
    )
    Path(env["GITHUB_ENV"]).touch()
    Path(env["GITHUB_OUTPUT"]).touch()
    return env


def require_main_source(repo_root: Path, source_sha: str) -> None:
    source_sha = require_sha(source_sha, "source_sha")
    head = subprocess.run(
        ["git", "rev-parse", "HEAD"],
        cwd=repo_root,
        check=True,
        capture_output=True,
        text=True,
    ).stdout.strip()
    if head != source_sha:
        raise ValidationReplayError(
            f"checkout HEAD/source SHA mismatch: head={head} "
            f"source={source_sha}"
        )
    status = subprocess.run(
        ["git", "status", "--porcelain"],
        cwd=repo_root,
        check=True,
        capture_output=True,
        text=True,
    ).stdout
    if status.strip():
        raise ValidationReplayError(
            "validation replay must start from a clean main checkout"
        )


def run_market_session_preflight(
    repo_root: Path, env: dict[str, str]
) -> dict[str, Any]:
    run_command(
        [
            sys.executable,
            "-B",
            "scripts/market_session_calendar.py",
            "--phase",
            "confirm",
            "--as-of",
            "2026-08-07T23:00:00+08:00",
            "--assessment-date",
            REPLAY_DATE,
        ],
        cwd=repo_root,
        env=env,
        label="date-locked historical market-session confirmation",
    )
    payload = json.loads(
        (repo_root / MARKET_SESSION_PATH).read_text(
            encoding="utf-8-sig"
        )
    )
    expected = str(payload.get("expected_main_price_date") or "")
    require_exact_date(expected, "market-session expected date")
    status = str(payload.get("market_status") or "")
    if status != "open_confirmed":
        raise ValidationReplayError(
            "historical replay market session must be open_confirmed; "
            f"observed={status}"
        )
    session_date = str(payload.get("market_session_date") or "")
    require_exact_date(session_date, "market-session date")
    env["MARKET_STATUS"] = status
    env["MARKET_SESSION_DATE"] = session_date
    return payload


def _is_price_history_extension_path(relative_path: str) -> bool:
    return relative_path in PRICE_HISTORY_EXTENSION_ALLOWED_FILES or bool(
        re.fullmatch(r"data/stock_price_history/[^/]+\.csv", relative_path)
    )


def _git_capture(
    repo_root: Path,
    *args: str,
    env: dict[str, str] | None = None,
    binary: bool = False,
) -> bytes | str:
    git_env = os.environ.copy()
    if env:
        git_env.update(env)
    git_env["GIT_OPTIONAL_LOCKS"] = "0"
    completed = subprocess.run(
        ["git", *args],
        cwd=repo_root,
        env=git_env,
        capture_output=True,
        text=not binary,
        encoding=None if binary else "utf-8",
        errors=None if binary else "replace",
        check=False,
    )
    if completed.returncode != 0:
        stderr = (
            completed.stderr.decode("utf-8", errors="replace")
            if binary
            else completed.stderr
        )
        raise ValidationReplayError(
            f"validation-only git command failed rc={completed.returncode}: "
            f"git {' '.join(args)}: {str(stderr).strip()}"
        )
    return completed.stdout


def real_index_identity(repo_root: Path) -> tuple[Path, str]:
    raw_path = str(
        _git_capture(
            repo_root,
            "rev-parse",
            "--path-format=absolute",
            "--git-path",
            "index",
        )
    ).strip()
    index_path = Path(raw_path)
    if not index_path.is_file():
        raise ValidationReplayError(f"real Git index is missing: {index_path}")
    return index_path, sha256_file(index_path)


def assert_real_index_unchanged(
    repo_root: Path,
    expected_path: Path,
    expected_sha256: str,
) -> None:
    observed_path, observed_sha256 = real_index_identity(repo_root)
    if observed_path != expected_path or observed_sha256 != expected_sha256:
        raise ValidationReplayError(
            "real Git index drifted during validation-only price extension: "
            f"path={observed_path} sha256={observed_sha256}"
        )


def assert_real_head_and_ref_unchanged(
    repo_root: Path, expected_source_sha: str
) -> None:
    observed_head = str(_git_capture(repo_root, "rev-parse", "HEAD")).strip()
    observed_ref = str(_git_capture(repo_root, "symbolic-ref", "HEAD")).strip()
    if observed_head != expected_source_sha or observed_ref != "refs/heads/main":
        raise ValidationReplayError(
            "real Git HEAD/ref drifted during validation-only price extension: "
            f"head={observed_head} ref={observed_ref}"
        )


def price_extension_status_entries(repo_root: Path) -> list[dict[str, str]]:
    raw = _git_capture(
        repo_root,
        "status",
        "--porcelain=v1",
        "-z",
        "--untracked-files=all",
        binary=True,
    )
    assert isinstance(raw, bytes)
    fields = raw.split(b"\0")
    entries: list[dict[str, str]] = []
    index = 0
    while index < len(fields) and fields[index]:
        field = fields[index]
        index += 1
        if len(field) < 4 or field[2:3] != b" ":
            raise ValidationReplayError(
                "price history extension has malformed git status evidence"
            )
        status = field[:2].decode("ascii", errors="strict")
        path = field[3:].decode("utf-8", errors="strict").replace("\\", "/")
        if "R" in status or "C" in status:
            if index < len(fields) and fields[index]:
                index += 1
            raise ValidationReplayError(
                f"price history extension forbids rename/copy status: {status} {path}"
            )
        if status not in {" M", "??"}:
            raise ValidationReplayError(
                f"price history extension forbids git status: {status} {path}"
            )
        if not _is_price_history_extension_path(path):
            raise ValidationReplayError(
                f"price history extension changed an unapproved path: {path}"
            )
        file_path = repo_root / path
        if not file_path.is_file() or file_path.is_symlink():
            raise ValidationReplayError(
                f"price history extension path is not a regular file: {path}"
            )
        if status == "??":
            mode = (
                "100755"
                if file_path.stat().st_mode & stat.S_IXUSR
                else "100644"
            )
        else:
            staged = str(
                _git_capture(repo_root, "ls-files", "--stage", "--", path)
            ).strip()
            match = re.fullmatch(r"(100644|100755) [0-9a-f]{40,64} 0\t.+", staged)
            if not match:
                raise ValidationReplayError(
                    f"price history extension cannot prove tracked mode: {path}"
                )
            mode = match.group(1)
        entries.append({"path": path, "status": status, "mode": mode})
    return sorted(entries, key=lambda row: row["path"])


def _validate_price_history_extension_status(status: dict[str, Any]) -> None:
    if (
        status.get("target_date") != REPLAY_DATE
        or status.get("saved_price_date") != REPLAY_DATE
        or status.get("is_target_date") is not True
        or status.get("future_rows_used") is not False
    ):
        raise ValidationReplayError(
            "authoritative price-history extension returned a wrong-date or "
            "future-row status"
        )
    responses = status.get("source_responses") or []
    if not responses or any(
        response.get("exact_date_match") is not True
        or response.get("observed_response_dates") != [REPLAY_DATE]
        for response in responses
    ):
        raise ValidationReplayError(
            "authoritative price-history extension lacks exact-date source evidence"
        )
    coverage = status.get("stock_history_coverage") or {}
    if int(coverage.get("missing_history_rows", -1)) != 0:
        raise ValidationReplayError(
            "authoritative price-history extension has incomplete stock-history coverage"
        )


def verify_price_history_extension_manifest(
    *,
    repo_root: Path,
    manifest_path: Path,
    expected_manifest_sha256: str,
    source_sha: str,
) -> dict[str, Any]:
    if not manifest_path.is_file():
        raise ValidationReplayError(
            f"price history extension manifest missing: {manifest_path}"
        )
    if sha256_file(manifest_path) != expected_manifest_sha256:
        raise ValidationReplayError("price history extension manifest SHA mismatch")
    payload = json.loads(manifest_path.read_text(encoding="utf-8"))
    if (
        payload.get("schema_version") != 1
        or payload.get("mode") != "validation_only_authoritative_price_history_extension"
        or payload.get("replay_date") != REPLAY_DATE
        or payload.get("source_sha") != source_sha
    ):
        raise ValidationReplayError(
            "price history extension manifest date/source contract mismatch"
        )
    _validate_price_history_extension_status(payload.get("source_status") or {})
    rows = payload.get("files") or []
    expected_paths = [str(row.get("path") or "") for row in rows]
    if (
        not expected_paths
        or len(expected_paths) != len(set(expected_paths))
        or expected_paths != sorted(expected_paths)
        or any(not _is_price_history_extension_path(path) for path in expected_paths)
    ):
        raise ValidationReplayError(
            "price history extension manifest path allowlist is invalid"
        )
    if not PRICE_HISTORY_EXTENSION_REQUIRED_FILES.issubset(expected_paths) or not any(
        path.startswith(PRICE_HISTORY_EXTENSION_ALLOWED_PREFIXES[0])
        for path in expected_paths
    ):
        raise ValidationReplayError(
            "price history extension manifest is missing required price/history files"
        )
    observed_entries = price_extension_status_entries(repo_root)
    observed_paths = [row["path"] for row in observed_entries]
    if observed_paths != expected_paths:
        raise ValidationReplayError(
            "price history extension manifest path set drift: "
            f"observed={observed_paths} expected={expected_paths}"
        )
    observed_by_path = {row["path"]: row for row in observed_entries}
    for row in rows:
        relative = str(row["path"])
        observed = observed_by_path[relative]
        if (
            row.get("status") != observed["status"]
            or row.get("mode") != observed["mode"]
        ):
            raise ValidationReplayError(
                f"price history extension status/mode mismatch: {relative}"
            )
        path = repo_root / relative
        if not path.is_file():
            raise ValidationReplayError(
                f"price history extension file missing: {relative}"
            )
        if path.stat().st_size != int(row.get("bytes", -1)):
            raise ValidationReplayError(
                f"price history extension byte mismatch: {relative}"
            )
        if sha256_file(path) != str(row.get("sha256") or ""):
            raise ValidationReplayError(
                f"price history extension hash mismatch: {relative}"
            )
    return payload


def extend_authoritative_price_history(
    *,
    repo_root: Path,
    runner_temp: Path,
    source_sha: str,
    initial_high_water_date: str,
) -> tuple[dict[str, Any], Path, str]:
    expected_previous = historical_replay.previous_trading_date(REPLAY_DATE)
    if initial_high_water_date != expected_previous:
        raise ValidationReplayError(
            "price history extension requires the immediately preceding trading "
            f"date; observed={initial_high_water_date} expected={expected_previous}"
        )
    real_index_path, real_index_sha256 = real_index_identity(repo_root)
    previous_cwd = Path.cwd()
    try:
        os.chdir(repo_root)
        status = historical_replay.replay_price_date(REPLAY_DATE)
        _validate_price_history_extension_status(status)
        tails = historical_replay.source_tail_matrix()
    finally:
        os.chdir(previous_cwd)
        assert_real_index_unchanged(
            repo_root, real_index_path, real_index_sha256
        )
    if (
        tails.get("daily_price") != REPLAY_DATE
        or (tails.get("stock_price_history") or {}).get("max_date") != REPLAY_DATE
    ):
        raise ValidationReplayError(
            "authoritative price-history extension did not reach exact replay date"
        )
    status_entries = price_extension_status_entries(repo_root)
    changed_paths = [row["path"] for row in status_entries]
    if not changed_paths:
        raise ValidationReplayError(
            "authoritative price-history extension produced no file evidence"
        )
    status_by_path = {row["path"]: row for row in status_entries}
    files = [
        {
            "path": relative,
            "status": status_by_path[relative]["status"],
            "mode": status_by_path[relative]["mode"],
            "bytes": (repo_root / relative).stat().st_size,
            "sha256": sha256_file(repo_root / relative),
        }
        for relative in changed_paths
    ]
    payload = {
        "schema_version": 1,
        "mode": "validation_only_authoritative_price_history_extension",
        "replay_date": REPLAY_DATE,
        "source_sha": source_sha,
        "initial_price_history_high_water_date": initial_high_water_date,
        "real_index_path": str(real_index_path),
        "real_index_sha256": real_index_sha256,
        "source_status": status,
        "files": files,
    }
    manifest_path = runner_temp / PRICE_HISTORY_EXTENSION_MANIFEST
    manifest_path.write_bytes(canonical_json_bytes(payload))
    manifest_sha256 = sha256_file(manifest_path)
    (runner_temp / f"{PRICE_HISTORY_EXTENSION_MANIFEST}.sha256").write_text(
        manifest_sha256 + "\n", encoding="ascii", newline="\n"
    )
    verify_price_history_extension_manifest(
        repo_root=repo_root,
        manifest_path=manifest_path,
        expected_manifest_sha256=manifest_sha256,
        source_sha=source_sha,
    )
    return payload, manifest_path, manifest_sha256


def assert_validation_only_git_baseline(
    *,
    repo_root: Path,
    producer_env: dict[str, str],
    source_sha: str,
    expected_paths: list[str],
) -> None:
    branch = run_command(
        ["git", "rev-parse", "--abbrev-ref", "HEAD"],
        cwd=repo_root,
        env=producer_env,
        label="verify validation-only synthetic branch",
    ).strip()
    if branch != "main":
        raise ValidationReplayError(
            f"validation-only synthetic branch drifted: {branch}"
        )
    observed_head = run_command(
        ["git", "rev-parse", "HEAD"],
        cwd=repo_root,
        env=producer_env,
        label="verify validation-only source HEAD",
    ).strip()
    if observed_head != source_sha:
        raise ValidationReplayError(
            "validation-only source HEAD drifted: "
            f"expected={source_sha} observed={observed_head}"
        )
    replace_ref = f"refs/replace/{source_sha}"
    replace_refs = sorted(
        line.strip()
        for line in run_command(
            ["git", "for-each-ref", "--format=%(refname)", "refs/replace/"],
            cwd=repo_root,
            env=producer_env,
            label="verify validation-only replacement ref set",
        ).splitlines()
        if line.strip()
    )
    if replace_refs != [replace_ref]:
        raise ValidationReplayError(
            "validation-only synthetic replace ref drifted: "
            f"expected={[replace_ref]} observed={replace_refs}"
        )
    baseline_commit = run_command(
        ["git", "rev-parse", replace_ref],
        cwd=repo_root,
        env=producer_env,
        label="resolve validation-only synthetic commit",
    ).strip()
    no_replace_env = producer_env.copy()
    no_replace_env["GIT_NO_REPLACE_OBJECTS"] = "1"
    source_parents = run_command(
        ["git", "rev-list", "--parents", "-n", "1", source_sha],
        cwd=repo_root,
        env=no_replace_env,
        label="resolve validation-only source parents",
    ).strip().split()[1:]
    baseline_parents = run_command(
        ["git", "rev-list", "--parents", "-n", "1", baseline_commit],
        cwd=repo_root,
        env=no_replace_env,
        label="verify validation-only synthetic parents",
    ).strip().split()[1:]
    if baseline_parents != source_parents:
        raise ValidationReplayError(
            "validation-only synthetic parent set drifted: "
            f"expected={source_parents} observed={baseline_parents}"
        )
    head_tree = run_command(
        ["git", "rev-parse", "HEAD^{tree}"],
        cwd=repo_root,
        env=producer_env,
        label="resolve validation-only synthetic tree",
    ).strip()
    index_tree = run_command(
        ["git", "write-tree"],
        cwd=repo_root,
        env=producer_env,
        label="verify validation-only index tree",
    ).strip()
    if index_tree != head_tree:
        raise ValidationReplayError(
            "validation-only synthetic index tree drifted: "
            f"head={head_tree} index={index_tree}"
        )
    staged_paths = sorted(
        line.strip().replace("\\", "/")
        for line in run_command(
            ["git", "diff", "--cached", "--name-only", source_sha],
            cwd=repo_root,
            env=no_replace_env,
            label="verify validation-only synthetic path set",
        ).splitlines()
        if line.strip()
    )
    if staged_paths != expected_paths:
        raise ValidationReplayError(
            "validation-only synthetic path set drifted: "
            f"expected={expected_paths} observed={staged_paths}"
        )
    run_command(
        ["git", "diff", "--cached", "--quiet"],
        cwd=repo_root,
        env=producer_env,
        label="verify validation-only staged baseline",
    )
    run_command(
        ["git", "diff", "--quiet"],
        cwd=repo_root,
        env=producer_env,
        label="verify validation-only working tree baseline",
    )
    status = run_command(
        ["git", "status", "--porcelain=v1", "--untracked-files=all"],
        cwd=repo_root,
        env=producer_env,
        label="verify validation-only alternate index",
    )
    if status.strip():
        raise ValidationReplayError(
            "validation-only alternate index did not preserve an exact clean baseline: "
            f"{status.strip()}"
        )


def remove_validation_only_git_dir(git_dir_path: Path) -> None:
    if not git_dir_path.exists():
        return
    if git_dir_path.is_symlink() or not git_dir_path.is_dir():
        raise ValidationReplayError(
            f"validation-only Git directory cleanup is unsafe: {git_dir_path}"
        )

    def remove_readonly_path(
        function: Any, path: str, _error: Any
    ) -> None:
        os.chmod(path, stat.S_IWRITE)
        function(path)

    shutil.rmtree(git_dir_path, onerror=remove_readonly_path)


def prepare_validation_only_git_index(
    *,
    repo_root: Path,
    runner_temp: Path,
    env: dict[str, str],
    manifest: dict[str, Any],
) -> tuple[dict[str, str], Path, Path, Path]:
    index_path = runner_temp / "price-history-extension.git-index"
    pathspec_path = runner_temp / "price-history-extension-paths.bin"
    git_dir_path = runner_temp / "price-history-extension.git-dir"
    if index_path.exists():
        index_path.unlink()
    paths = [str(row["path"]) for row in manifest["files"]]
    if paths != sorted(set(paths)):
        raise ValidationReplayError(
            "validation-only alternate index requires a sorted unique path set"
        )
    source_sha = str(manifest["source_sha"])
    real_index_path = Path(str(manifest["real_index_path"]))
    real_index_sha256 = str(manifest["real_index_sha256"])
    assert_real_index_unchanged(repo_root, real_index_path, real_index_sha256)
    assert_real_head_and_ref_unchanged(repo_root, source_sha)
    remove_validation_only_git_dir(git_dir_path)
    pathspec_path.write_bytes(b"\0".join(path.encode("utf-8") for path in paths) + b"\0")
    common_dir_text = run_command(
        ["git", "rev-parse", "--git-common-dir"],
        cwd=repo_root,
        env=env,
        label="resolve real Git object database",
    ).strip()
    common_dir = Path(common_dir_text)
    if not common_dir.is_absolute():
        common_dir = repo_root / common_dir
    real_objects_dir = (common_dir.resolve() / "objects")
    if not real_objects_dir.is_dir():
        raise ValidationReplayError(
            f"real Git object database is missing: {real_objects_dir}"
        )
    run_command(
        ["git", "init", "--bare", str(git_dir_path)],
        cwd=repo_root,
        env=env,
        label="initialize validation-only Git directory",
    )
    alternates_path = git_dir_path / "objects" / "info" / "alternates"
    alternates_path.parent.mkdir(parents=True, exist_ok=True)
    alternates_path.write_text(
        real_objects_dir.as_posix() + "\n", encoding="utf-8", newline="\n"
    )
    producer_env = env.copy()
    producer_env["GIT_DIR"] = str(git_dir_path)
    producer_env["GIT_WORK_TREE"] = str(repo_root)
    producer_env["GIT_INDEX_FILE"] = str(index_path)
    try:
        run_command(
            ["git", "config", "core.bare", "false"],
            cwd=repo_root,
            env=producer_env,
            label="enable validation-only Git work tree",
        )
        run_command(
            ["git", "config", "core.worktree", str(repo_root)],
            cwd=repo_root,
            env=producer_env,
            label="bind validation-only Git work tree",
        )
        run_command(
            ["git", "read-tree", source_sha],
            cwd=repo_root,
            env=producer_env,
            label="initialize validation-only price-extension index",
        )
        run_command(
            [
                "git",
                "add",
                "--all",
                f"--pathspec-from-file={pathspec_path}",
                "--pathspec-file-nul",
            ],
            cwd=repo_root,
            env=producer_env,
            label="stage verified price extension in alternate index",
        )
        staged_paths = sorted(
            line.strip().replace("\\", "/")
            for line in run_command(
                ["git", "diff", "--cached", "--name-only", source_sha],
                cwd=repo_root,
                env=producer_env,
                label="verify validation-only staged path set",
            ).splitlines()
            if line.strip()
        )
        if staged_paths != paths:
            raise ValidationReplayError(
                "validation-only alternate index staged path set drifted: "
                f"expected={paths} observed={staged_paths}"
            )
        baseline_tree = run_command(
            ["git", "write-tree"],
            cwd=repo_root,
            env=producer_env,
            label="write validation-only synthetic baseline tree",
        ).strip()
        commit_env = producer_env.copy()
        no_replace_env = producer_env.copy()
        no_replace_env["GIT_NO_REPLACE_OBJECTS"] = "1"
        source_commit = run_command(
            ["git", "rev-list", "--parents", "-n", "1", source_sha],
            cwd=repo_root,
            env=no_replace_env,
            label="resolve source parents for validation-only baseline",
        ).strip().split()
        if not source_commit or source_commit[0] != source_sha:
            raise ValidationReplayError(
                "validation-only source parent evidence drifted"
            )
        commit_env.update(
            {
                "GIT_AUTHOR_NAME": "Validation Replay",
                "GIT_AUTHOR_EMAIL": "validation-replay@example.invalid",
                "GIT_AUTHOR_DATE": "2026-08-07T23:59:59+08:00",
                "GIT_COMMITTER_NAME": "Validation Replay",
                "GIT_COMMITTER_EMAIL": "validation-replay@example.invalid",
                "GIT_COMMITTER_DATE": "2026-08-07T23:59:59+08:00",
            }
        )
        commit_command = ["git", "commit-tree", baseline_tree]
        for parent_sha in source_commit[1:]:
            commit_command.extend(["-p", parent_sha])
        commit_command.extend(
            ["-m", "Validation-only verified price-extension baseline"]
        )
        baseline_commit = run_command(
            commit_command,
            cwd=repo_root,
            env=commit_env,
            label="create validation-only synthetic baseline commit",
        ).strip()
        run_command(
            ["git", "update-ref", f"refs/replace/{source_sha}", baseline_commit],
            cwd=repo_root,
            env=producer_env,
            label="bind validation-only synthetic replacement",
        )
        run_command(
            ["git", "update-ref", "refs/heads/main", source_sha],
            cwd=repo_root,
            env=producer_env,
            label="bind validation-only synthetic main",
        )
        run_command(
            ["git", "symbolic-ref", "HEAD", "refs/heads/main"],
            cwd=repo_root,
            env=producer_env,
            label="select validation-only synthetic main",
        )
        assert_validation_only_git_baseline(
            repo_root=repo_root,
            producer_env=producer_env,
            source_sha=source_sha,
            expected_paths=paths,
        )
    except Exception:
        remove_validation_only_git_index(
            repo_root=repo_root,
            index_path=index_path,
            pathspec_path=pathspec_path,
            git_dir_path=git_dir_path,
            real_index_path=real_index_path,
            real_index_sha256=real_index_sha256,
            source_sha=source_sha,
        )
        raise
    assert_real_index_unchanged(repo_root, real_index_path, real_index_sha256)
    assert_real_head_and_ref_unchanged(repo_root, source_sha)
    return producer_env, index_path, pathspec_path, git_dir_path


def remove_validation_only_git_index(
    *,
    repo_root: Path,
    index_path: Path,
    pathspec_path: Path,
    git_dir_path: Path,
    real_index_path: Path,
    real_index_sha256: str,
    source_sha: str,
) -> None:
    for path in (Path(f"{index_path}.lock"), index_path, pathspec_path):
        path.unlink(missing_ok=True)
    expected_git_dir = index_path.parent / "price-history-extension.git-dir"
    if git_dir_path != expected_git_dir:
        raise ValidationReplayError(
            f"refusing to remove unexpected validation-only Git directory: {git_dir_path}"
        )
    remove_validation_only_git_dir(git_dir_path)
    assert_real_index_unchanged(repo_root, real_index_path, real_index_sha256)
    assert_real_head_and_ref_unchanged(repo_root, source_sha)


def run_authoritative_historical_revision(
    *,
    repo_root: Path,
    runner_temp: Path,
    env: dict[str, str],
    run_id: str,
    source_sha: str,
) -> tuple[dict[str, Any], Path]:
    plan_path = runner_temp / "historical_replay_plan_before_price_extension.json"
    run_command(
        [
            sys.executable,
            "-B",
            str(HISTORICAL_REPLAY_PLANNER),
            "--max-replay-dates",
            "5",
            "--output",
            str(plan_path),
        ],
        cwd=repo_root,
        env=env,
        label="historical source replay planner",
    )
    initial_plan = json.loads(plan_path.read_text(encoding="utf-8"))
    plan = initial_plan
    producer_env = env
    temporary_index_path: Path | None = None
    temporary_pathspec_path: Path | None = None
    temporary_git_dir_path: Path | None = None
    real_index_path: Path | None = None
    real_index_sha256 = ""
    extension: dict[str, Any] | None = None
    extension_evidence: dict[str, Any] | None = None
    if str(initial_plan.get("end_date") or "") != REPLAY_DATE:
        initial_high_water = str(
            initial_plan.get("price_history_high_water_date") or ""
        )
        initial_end = str(initial_plan.get("end_date") or "")
        if initial_end and initial_end != initial_high_water:
            raise ValidationReplayError(
                "historical source replay planner initial end/high-water mismatch"
            )
        extension, extension_manifest, extension_sha = (
            extend_authoritative_price_history(
                repo_root=repo_root,
                runner_temp=runner_temp,
                source_sha=source_sha,
                initial_high_water_date=initial_high_water,
            )
        )
        plan_path = runner_temp / "historical_replay_plan_after_price_extension.json"
        run_command(
            [
                sys.executable,
                "-B",
                str(HISTORICAL_REPLAY_PLANNER),
                "--max-replay-dates",
                "5",
                "--output",
                str(plan_path),
            ],
            cwd=repo_root,
            env=env,
            label="historical source replay planner after price extension",
        )
        plan = json.loads(plan_path.read_text(encoding="utf-8"))
        verify_price_history_extension_manifest(
            repo_root=repo_root,
            manifest_path=extension_manifest,
            expected_manifest_sha256=extension_sha,
            source_sha=source_sha,
        )
        extension_evidence = {
            "initial_plan": initial_plan,
            "manifest_path": str(extension_manifest),
            "manifest_sha256": extension_sha,
        }
    require_exact_date(
        str(plan.get("end_date") or ""),
        "historical source replay plan end_date",
    )
    trading_dates = [
        str(value) for value in plan.get("trading_dates", [])
    ]
    if (
        not trading_dates
        or trading_dates[-1] != REPLAY_DATE
        or any(value > REPLAY_DATE for value in trading_dates)
    ):
        raise ValidationReplayError(
            "historical source replay planner escaped the exact "
            f"date lock: {trading_dates}"
        )
    if extension is not None:
        (
            producer_env,
            temporary_index_path,
            temporary_pathspec_path,
            temporary_git_dir_path,
        ) = (
            prepare_validation_only_git_index(
                repo_root=repo_root,
                runner_temp=runner_temp,
                env=env,
                manifest=extension,
            )
        )
        real_index_path = Path(str(extension["real_index_path"]))
        real_index_sha256 = str(extension["real_index_sha256"])
    replay_id = f"validation-only-{run_id}-authoritative-r1"
    command = [
        sys.executable,
        "-B",
        str(HISTORICAL_REPLAY_SCRIPT),
        "--start-date",
        str(plan["start_date"]),
        "--end-date",
        REPLAY_DATE,
        "--price-history-high-water-date",
        str(plan.get("price_history_high_water_date") or ""),
        "--repair-market-index-base-date",
        str(plan.get("repair_market_index_base_date") or ""),
        "--replay-id",
        replay_id,
    ]
    try:
        run_command(
            command,
            cwd=repo_root,
            env=producer_env,
            label="authoritative historical source replay",
        )
    finally:
        if (
            temporary_index_path is not None
            and temporary_pathspec_path is not None
            and temporary_git_dir_path is not None
            and real_index_path is not None
        ):
            remove_validation_only_git_index(
                repo_root=repo_root,
                index_path=temporary_index_path,
                pathspec_path=temporary_pathspec_path,
                git_dir_path=temporary_git_dir_path,
                real_index_path=real_index_path,
                real_index_sha256=real_index_sha256,
                source_sha=source_sha,
            )
    validator = [
        sys.executable,
        "-B",
        str(HISTORICAL_REPLAY_VALIDATOR),
        "--start-date",
        str(plan["start_date"]),
        "--end-date",
        REPLAY_DATE,
        "--price-history-high-water-date",
        str(plan.get("price_history_high_water_date") or ""),
        "--repair-market-index-base-date",
        str(plan.get("repair_market_index_base_date") or ""),
        "--replay-id",
        replay_id,
        "--expected-pipeline-sha",
        source_sha,
    ]
    run_command(
        validator,
        cwd=repo_root,
        env=env,
        label="authoritative historical source replay validator",
    )
    manifest_path = (
        repo_root
        / "output/history/historical_source_replay"
        / replay_id
        / REPLAY_DATE
        / "structured_source_manifest.json"
    )
    if not manifest_path.is_file():
        raise ValidationReplayError(
            f"historical source manifest missing: {manifest_path}"
        )
    manifest = json.loads(
        manifest_path.read_text(encoding="utf-8")
    )
    if (
        manifest.get("report_date") != REPLAY_DATE
        or manifest.get("pipeline_commit_sha") != source_sha
        or manifest.get("as_published") is not False
    ):
        raise ValidationReplayError(
            "historical source manifest date/SHA/revision contract mismatch"
        )
    if extension_evidence is not None:
        plan = {**plan, "validation_only_price_history_extension": extension_evidence}
    return plan, manifest_path


def run_named_steps(
    *,
    repo_root: Path,
    env: dict[str, str],
    names: Iterable[str],
    post_mode: bool,
    results: list[dict[str, str]] | None = None,
) -> list[dict[str, str]]:
    commands = step_map(repo_root)
    step_results = results if results is not None else []
    for name in names:
        if name not in commands:
            raise ValidationReplayError(
                f"production workflow step is missing: {name}"
            )
        script = commands[name]
        if post_mode:
            script = remove_mutable_post_commands(script)
        started = datetime.now(timezone.utc).isoformat()
        try:
            run_bash_block(
                script,
                cwd=repo_root,
                env=env,
                label=f"production step replay: {name}",
            )
        except Exception as error:
            step_results.append(
                {
                    "step": name,
                    "status": "failure",
                    "started_at_utc": started,
                    "completed_at_utc": datetime.now(
                        timezone.utc
                    ).isoformat(),
                    "error": str(error),
                }
            )
            raise
        apply_github_environment(env)
        step_results.append(
            {
                "step": name,
                "status": "pass",
                "started_at_utc": started,
                "completed_at_utc": datetime.now(
                    timezone.utc
                ).isoformat(),
            }
        )
    return step_results


def read_csv_rows(path: Path) -> tuple[list[str], list[dict[str, str]]]:
    if not path.is_file():
        raise ValidationReplayError(f"required CSV missing: {path}")
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle)
        return list(reader.fieldnames or []), list(reader)


def require_csv_exact_date(
    path: Path,
    expected_date: str,
    candidate_fields: Sequence[str],
    label: str,
) -> None:
    columns, rows = read_csv_rows(path)
    field = next(
        (candidate for candidate in candidate_fields if candidate in columns),
        "",
    )
    if not field:
        raise ValidationReplayError(
            f"{label} has no date field from {list(candidate_fields)}"
        )
    observed = {
        str(row.get(field) or "").strip()
        for row in rows
        if str(row.get(field) or "").strip()
    }
    if not rows or observed != {expected_date}:
        raise ValidationReplayError(
            f"{label} is not exact date {expected_date}: "
            f"field={field} observed={sorted(observed)}"
        )


def run_registered_parity_validators(
    repo_root: Path,
    env: dict[str, str],
) -> dict[str, Any]:
    validators: list[dict[str, str]] = []
    for relative_path in REGISTERED_PARITY_VALIDATOR_PATHS:
        arguments = REGISTERED_PARITY_VALIDATOR_ARGUMENTS.get(relative_path)
        if arguments is None:
            raise ValidationReplayError(
                "registered replay parity validator mode is missing: "
                f"{relative_path.as_posix()}"
            )
        run_command(
            [
                sys.executable,
                "-B",
                relative_path.as_posix(),
                *arguments,
            ],
            cwd=repo_root,
            env=env,
            label=(
                "registered replay parity validator: "
                f"{relative_path.as_posix()}"
            ),
        )
        validators.append(
            {
                "path": relative_path.as_posix(),
                "status": "pass",
            }
        )

    artifacts: dict[str, dict[str, object]] = {}
    for relative_path in PARITY_EVIDENCE_PATHS:
        path = repo_root / relative_path
        if not path.is_file():
            raise ValidationReplayError(
                "registered replay parity validator evidence missing: "
                f"{relative_path.as_posix()}"
            )
        artifacts[relative_path.as_posix()] = {
            "bytes": path.stat().st_size,
            "sha256": sha256_file(path),
        }
    return {
        "validation_mode": "registered_fail_closed_validators",
        "validators": validators,
        "artifacts": artifacts,
    }


def source_row(
    structured_manifest: dict[str, Any],
    source_id: str,
) -> dict[str, Any]:
    for row in structured_manifest.get("sources", []):
        if row.get("source_id") == source_id:
            return row
    raise ValidationReplayError(
        f"structured source manifest missing source_id={source_id}"
    )


def first_existing(repo_root: Path, candidates: Sequence[Path]) -> Path:
    for relative in candidates:
        if (repo_root / relative).is_file():
            return relative
    raise ValidationReplayError(
        "required checkpoint source artifact is missing: "
        + ", ".join(path.as_posix() for path in candidates)
    )


def source_urls(row: dict[str, Any]) -> str:
    endpoints = row.get("endpoint", [])
    if isinstance(endpoints, str):
        endpoints = [endpoints]
    normalized = sorted(
        {str(value).strip() for value in endpoints if str(value).strip()}
    )
    if not normalized:
        raise ValidationReplayError(
            f"source row has no endpoint: {row.get('source_id')}"
        )
    return " | ".join(normalized)


def create_source_revision_manifest(
    *,
    repo_root: Path,
    output_path: Path,
    source_sha: str,
    revision_kind: str,
    structured_manifest_path: Path | None,
) -> tuple[dict[str, Any], list[str]]:
    if revision_kind == "authoritative_historical_revision":
        if structured_manifest_path is None:
            raise ValidationReplayError(
                "historical source revision requires structured manifest"
            )
        structured_relative = structured_manifest_path.relative_to(
            repo_root
        )
        structured = json.loads(
            structured_manifest_path.read_text(encoding="utf-8")
        )
        if structured.get("report_date") != REPLAY_DATE:
            raise ValidationReplayError(
                "structured source manifest report date mismatch"
            )
        price_row = source_row(structured, "official_daily_price")
        warrant_row = source_row(
            structured, "official_warrant_daily"
        )
        price_raw = first_existing(
            repo_root,
            (Path(f"data/daily_price/{REPLAY_DATE}.csv"),),
        )
        price_url = source_urls(price_row)
        warrant_url = source_urls(warrant_row)
    else:
        structured = {}
        price_raw = first_existing(
            repo_root,
            (
                Path("output/latest/official_price_fetch_latest.json"),
                Path("output/latest/official_price_fetch_latest.md"),
            ),
        )
        price_url = (
            "repo+producer://fetch_official_daily_price/"
            f"{price_raw.as_posix()}@{source_sha}"
        )
        warrant_url = (
            "repo+producer://fetch_official_warrant_daily/"
            f"{REPLAY_DATE}@{source_sha}"
        )

    market_session = MARKET_SESSION_PATH
    price_normalized = first_existing(
        repo_root,
        (
            Path(f"data/daily_price/daily_price_{REPLAY_DATE}.csv"),
            Path(f"data/daily_price/{REPLAY_DATE}.csv"),
        ),
    )
    candidate_inputs = ALL_CANDIDATES_PATH
    warrant_raw = Path("output/latest/warrant_daily_raw_latest.csv")
    warrant_normalized = WARRANT_FLOW_PATH
    trading_calendar = Path(
        "data/market_calendar/exceptional_non_trading_days.csv"
    )
    path_contract = {
        "market_session": market_session,
        "daily_price_raw": price_raw,
        "daily_price_normalized": price_normalized,
        "candidate_inputs": candidate_inputs,
        "warrant_raw": warrant_raw,
        "warrant_normalized": warrant_normalized,
        "trading_calendar": trading_calendar,
    }
    for category, relative in path_contract.items():
        if not (repo_root / relative).is_file():
            raise ValidationReplayError(
                f"{category} checkpoint artifact missing: {relative}"
            )
    require_csv_exact_date(
        repo_root / price_raw,
        REPLAY_DATE,
        ("date", "report_date", "signal_date"),
        "daily price raw",
    )
    require_csv_exact_date(
        repo_root / price_normalized,
        REPLAY_DATE,
        ("date", "report_date", "signal_date"),
        "daily price normalized",
    )
    require_csv_exact_date(
        repo_root / candidate_inputs,
        REPLAY_DATE,
        ("date", "report_date", "signal_date", "price_date"),
        "candidate inputs",
    )
    require_csv_exact_date(
        repo_root / warrant_raw,
        REPLAY_DATE,
        ("date", "report_date", "signal_date"),
        "warrant raw",
    )
    require_csv_exact_date(
        repo_root / warrant_normalized,
        REPLAY_DATE,
        ("date", "report_date", "signal_date"),
        "warrant normalized",
    )
    urls = {
        "market_session": (
            "repo+producer://market_session_calendar/"
            f"{REPLAY_DATE}@{source_sha}"
        ),
        "daily_price_raw": price_url,
        "daily_price_normalized": price_url,
        "candidate_inputs": (
            "repo+producer://build_all_candidates_latest/"
            f"{REPLAY_DATE}@{source_sha}"
        ),
        "warrant_raw": warrant_url,
        "warrant_normalized": warrant_url,
        "trading_calendar": (
            "repo+calendar://exceptional_non_trading_days"
            f"@{source_sha}"
        ),
    }
    sources = []
    for category, relative in path_contract.items():
        path = repo_root / relative
        sources.append(
            {
                "category": category,
                "identity": (
                    f"{category}:{REPLAY_DATE}:"
                    f"{sha256_file(path)}"
                ),
                "source_url": urls[category],
                "artifact_path": relative.as_posix(),
                "bytes": path.stat().st_size,
                "sha256": sha256_file(path),
            }
        )
    payload: dict[str, Any] = {
        "schema_version": 1,
        "replay_date": REPLAY_DATE,
        "revision_kind": revision_kind,
        "source_sha": source_sha,
        "generated_at_utc": datetime.now(timezone.utc).isoformat(),
        "byte_parity_with_run_31174813266": False,
        "supersedes_failed_run_as_new_revision": OLD_FAILED_RUN_ID,
        "sources": sources,
    }
    if structured_manifest_path is not None:
        payload["structured_source_manifest"] = {
            "path": structured_manifest_path.relative_to(
                repo_root
            ).as_posix(),
            "bytes": structured_manifest_path.stat().st_size,
            "sha256": sha256_file(structured_manifest_path),
        }
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_bytes(canonical_json_bytes(payload))
    return payload, sorted(
        {row["artifact_path"] for row in sources}
        | (
            {
                payload["structured_source_manifest"]["path"],
            }
            if "structured_source_manifest" in payload
            else set()
        )
    )


def checkpoint_paths(
    repo_root: Path, required_paths: Iterable[str]
) -> list[str]:
    changed = checkpoint.discover_changed_paths(
        repo_root, ALLOWED_CHECKPOINT_PREFIXES
    )
    paths = sorted(set(changed) | set(required_paths))
    if not paths:
        raise ValidationReplayError(
            "checkpoint path allowlist is empty"
        )
    return paths


def source_tree_file_identity(
    repo_root: Path, source_sha: str, relative: str
) -> dict[str, Any]:
    source_sha = require_sha(source_sha, "source_sha")
    normalized = Path(relative).as_posix()
    if (
        not normalized
        or Path(normalized).is_absolute()
        or ".." in Path(normalized).parts
        or normalized == DELETION_MANIFEST_PATH.as_posix()
        or not any(
            normalized == prefix or normalized.startswith(f"{prefix}/")
            for prefix in ALLOWED_CHECKPOINT_PREFIXES
        )
    ):
        raise ValidationReplayError(
            f"checkpoint deletion path is not allowed: {relative}"
        )
    result = subprocess.run(
        ["git", "ls-tree", "-z", source_sha, "--", normalized],
        cwd=repo_root,
        check=False,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    rows = [row for row in result.stdout.split(b"\0") if row]
    if result.returncode != 0 or len(rows) != 1 or b"\t" not in rows[0]:
        raise ValidationReplayError(
            f"checkpoint deletion source object is missing: {normalized}"
        )
    metadata_raw, observed_path_raw = rows[0].split(b"\t", 1)
    try:
        metadata = metadata_raw.decode("ascii")
        observed_path = observed_path_raw.decode("utf-8")
    except UnicodeDecodeError as error:
        raise ValidationReplayError(
            f"checkpoint deletion source path/mode mismatch: {normalized}"
        ) from error
    parts = metadata.split()
    if (
        observed_path != normalized
        or len(parts) != 3
        or parts[0] not in {"100644", "100755"}
        or parts[1] != "blob"
        or not re.fullmatch(r"[0-9a-f]{40,64}", parts[2])
    ):
        raise ValidationReplayError(
            f"checkpoint deletion source path/mode mismatch: {normalized}"
        )
    blob = subprocess.run(
        ["git", "cat-file", "blob", parts[2]],
        cwd=repo_root,
        check=False,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    if blob.returncode != 0:
        raise ValidationReplayError(
            f"checkpoint deletion source blob is unreadable: {normalized}"
        )
    return {
        "path": normalized,
        "mode": parts[0],
        "blob_sha": parts[2],
        "bytes": len(blob.stdout),
        "sha256": hashlib.sha256(blob.stdout).hexdigest(),
    }


def write_checkpoint_deletion_manifest(
    repo_root: Path, source_sha: str, deleted_paths: Iterable[str]
) -> Path:
    rows: list[dict[str, Any]] = []
    for relative in sorted(set(deleted_paths)):
        target = repo_root / Path(relative)
        if target.exists() or target.is_symlink():
            raise ValidationReplayError(
                f"checkpoint deletion path still exists: {relative}"
            )
        rows.append(source_tree_file_identity(repo_root, source_sha, relative))
    payload = {
        "schema_version": 1,
        "replay_date": REPLAY_DATE,
        "source_sha": source_sha,
        "deletions": rows,
    }
    path = repo_root / DELETION_MANIFEST_PATH
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(canonical_json_bytes(payload))
    return path


def checkpoint_deletion_baseline_matches(
    repo_root: Path,
    target: Path,
    relative: str,
    expected: dict[str, Any],
) -> bool:
    if not target.is_file() or target.is_symlink():
        return False
    content = target.read_bytes()
    if (
        len(content) == expected["bytes"]
        and hashlib.sha256(content).hexdigest() == expected["sha256"]
    ):
        return True
    canonical = subprocess.run(
        ["git", "hash-object", "--path", relative, "--stdin"],
        cwd=repo_root,
        check=False,
        input=content,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    observed = canonical.stdout.strip()
    if (
        canonical.returncode != 0
        or not re.fullmatch(rb"[0-9a-f]{40,64}", observed)
    ):
        raise ValidationReplayError(
            "checkpoint deletion Git canonicalization failed: "
            f"{relative}"
        )
    return observed.decode("ascii") == expected["blob_sha"]


def apply_checkpoint_deletions(
    repo_root: Path, source_sha: str
) -> list[str]:
    path = repo_root / DELETION_MANIFEST_PATH
    if not path.is_file() or path.is_symlink():
        raise ValidationReplayError(
            "checkpoint deletion manifest is missing or not a regular file"
        )
    raw = path.read_bytes()
    try:
        payload = json.loads(raw.decode("utf-8"))
    except (UnicodeDecodeError, json.JSONDecodeError) as error:
        raise ValidationReplayError(
            "checkpoint deletion manifest is not UTF-8 JSON"
        ) from error
    if raw != canonical_json_bytes(payload):
        raise ValidationReplayError(
            "checkpoint deletion manifest is not canonical"
        )
    if (
        set(payload) != {
            "schema_version",
            "replay_date",
            "source_sha",
            "deletions",
        }
        or payload.get("schema_version") != 1
        or payload.get("replay_date") != REPLAY_DATE
        or payload.get("source_sha") != source_sha
        or not isinstance(payload.get("deletions"), list)
    ):
        raise ValidationReplayError(
            "checkpoint deletion manifest identity mismatch"
        )
    deleted: list[str] = []
    seen: set[str] = set()
    for row in payload["deletions"]:
        if not isinstance(row, dict) or set(row) != {
            "path",
            "mode",
            "blob_sha",
            "bytes",
            "sha256",
        }:
            raise ValidationReplayError(
                "checkpoint deletion row is malformed"
            )
        relative = str(row.get("path") or "")
        if relative in seen:
            raise ValidationReplayError(
                f"checkpoint deletion path is duplicated: {relative}"
            )
        seen.add(relative)
        expected = source_tree_file_identity(repo_root, source_sha, relative)
        if row != expected:
            raise ValidationReplayError(
                f"checkpoint deletion source identity drift: {relative}"
            )
        target = repo_root / Path(relative)
        if not checkpoint_deletion_baseline_matches(
            repo_root, target, relative, expected
        ):
            raise ValidationReplayError(
                f"checkpoint deletion baseline content drift: {relative}"
            )
        target.unlink()
        if target.exists() or target.is_symlink():
            raise ValidationReplayError(
                f"checkpoint deletion did not remove path: {relative}"
            )
        deleted.append(relative)
    return deleted


def capture_checkpoint(
    *,
    repo_root: Path,
    bundle_dir: Path,
    runner_temp: Path,
    source_sha: str,
    run_id: str,
    structured_manifest_path: Path | None,
    revision_kind: str,
    checkpoint_kind: str,
    capture_context: str,
    producer_steps: Sequence[str],
    source_revision_manifest_path: Path | None = None,
) -> dict[str, Any]:
    if source_revision_manifest_path is None:
        source_revision_path = runner_temp / SOURCE_REVISION_FILENAME
        _revision, required = create_source_revision_manifest(
            repo_root=repo_root,
            output_path=source_revision_path,
            source_sha=source_sha,
            revision_kind=revision_kind,
            structured_manifest_path=structured_manifest_path,
        )
    else:
        source_revision_path = source_revision_manifest_path
        raw = source_revision_path.read_bytes()
        try:
            revision = json.loads(raw.decode("utf-8"))
        except (UnicodeDecodeError, json.JSONDecodeError) as error:
            raise ValidationReplayError(
                "replay source revision manifest is not UTF-8 JSON"
            ) from error
        if raw != canonical_json_bytes(revision):
            raise ValidationReplayError(
                "replay source revision manifest is not canonical"
            )
        if (
            revision.get("source_sha") != source_sha
            or revision.get("replay_source_sha") != source_sha
            or revision.get("replay_date") != REPLAY_DATE
            or revision.get("revision_kind") != revision_kind
        ):
            raise ValidationReplayError(
                "replay source revision manifest identity mismatch"
            )
        structured = revision.get("structured_source_manifest")
        if structured_manifest_path is None or not isinstance(
            structured, dict
        ):
            raise ValidationReplayError(
                "replay source revision manifest lacks structured identity"
            )
        structured_relative = structured_manifest_path.relative_to(
            repo_root
        ).as_posix()
        if (
            structured.get("path") != structured_relative
            or structured.get("bytes") != structured_manifest_path.stat().st_size
            or str(structured.get("sha256") or "").lower()
            != sha256_file(structured_manifest_path)
        ):
            raise ValidationReplayError(
                "replay source revision structured identity mismatch"
            )
        sources = revision.get("sources")
        if not isinstance(sources, list) or not sources:
            raise ValidationReplayError(
                "replay source revision source allowlist is missing"
            )
        required = []
        for row in sources:
            if not isinstance(row, dict):
                raise ValidationReplayError(
                    "replay source revision source row is malformed"
                )
            artifact_path = str(row.get("artifact_path") or "")
            if not artifact_path or ".." in Path(artifact_path).parts:
                raise ValidationReplayError(
                    "replay source revision artifact path is malformed"
                )
            artifact = repo_root / artifact_path
            if (
                not artifact.is_file()
                or row.get("bytes") != artifact.stat().st_size
                or str(row.get("sha256") or "").lower()
                != sha256_file(artifact)
            ):
                raise ValidationReplayError(
                    "replay source revision artifact identity mismatch: "
                    f"{artifact_path}"
                )
            required.append(artifact_path)
        required.append(structured_relative)
    paths = checkpoint_paths(repo_root, required)
    deleted_paths = [
        relative
        for relative in paths
        if not (repo_root / Path(relative)).is_file()
    ]
    if set(deleted_paths) & set(required):
        raise ValidationReplayError(
            "required source identity path cannot be deleted from checkpoint"
        )
    deletion_manifest = write_checkpoint_deletion_manifest(
        repo_root, source_sha, deleted_paths
    )
    deletion_relative = deletion_manifest.relative_to(repo_root).as_posix()
    paths = sorted(
        {relative for relative in paths if relative not in deleted_paths}
        | {deletion_relative}
    )
    return checkpoint.create_checkpoint(
        repo_root=repo_root,
        bundle_dir=bundle_dir,
        paths=paths,
        replay_date=REPLAY_DATE,
        source_sha=source_sha,
        producer_run_id=run_id,
        producer_head_sha=source_sha,
        source_identity_manifest=source_revision_path,
        checkpoint_kind=checkpoint_kind,
        producer_steps=producer_steps,
        locked_replay_date=REPLAY_DATE,
        capture_context=capture_context,
    )


def capture_canary(args: argparse.Namespace) -> int:
    repo_root = args.repo_root.resolve()
    runner_temp = args.runner_temp.resolve()
    runner_temp.mkdir(parents=True, exist_ok=True)
    source_sha = require_sha(args.source_sha, "source_sha")
    require_exact_date(args.replay_date, "replay_date")
    require_main_source(repo_root, source_sha)
    env = base_environment(
        repo_root=repo_root,
        runner_temp=runner_temp,
        source_sha=source_sha,
    )
    plan, structured_manifest = run_authoritative_historical_revision(
        repo_root=repo_root,
        runner_temp=runner_temp,
        env=env,
        run_id=args.run_id,
        source_sha=source_sha,
    )
    run_market_session_preflight(repo_root, env)
    steps = run_named_steps(
        repo_root=repo_root,
        env=env,
        names=PRE_STEP_NAMES,
        post_mode=False,
    )
    STEP_RESULTS_PATH_ABS = repo_root / STEP_RESULTS_PATH
    STEP_RESULTS_PATH_ABS.parent.mkdir(parents=True, exist_ok=True)
    STEP_RESULTS_PATH_ABS.write_bytes(
        canonical_json_bytes(
            {
                "schema_version": 1,
                "mode": "capture_canary",
                "replay_date": REPLAY_DATE,
                "source_sha": source_sha,
                "historical_plan": plan,
                "steps": steps,
            }
        )
    )
    manifest = capture_checkpoint(
        repo_root=repo_root,
        bundle_dir=args.bundle_dir.resolve(),
        runner_temp=runner_temp,
        source_sha=source_sha,
        run_id=args.run_id,
        structured_manifest_path=structured_manifest,
        revision_kind="authoritative_historical_revision",
        checkpoint_kind="pre_step41",
        capture_context="validation_canary",
        producer_steps=[row["step"] for row in steps],
    )
    print(
        json.dumps(
            {
                "status": "checkpoint_ready_for_controlled_failure",
                "files": len(manifest["files"]),
                "replay_date": REPLAY_DATE,
                "source_sha": source_sha,
            },
            sort_keys=True,
        )
    )
    return 0


def capture_production_checkpoint(args: argparse.Namespace) -> int:
    repo_root = args.repo_root.resolve()
    runner_temp = args.runner_temp.resolve()
    runner_temp.mkdir(parents=True, exist_ok=True)
    source_sha = require_sha(args.source_sha, "source_sha")
    head_sha = subprocess.run(
        ["git", "rev-parse", "HEAD"],
        cwd=repo_root,
        check=True,
        capture_output=True,
        text=True,
    ).stdout.strip()
    if head_sha != source_sha:
        raise ValidationReplayError(
            "production checkpoint HEAD/source SHA mismatch"
        )
    production_date = str(args.replay_date)
    if not re.fullmatch(r"20\d{6}", production_date):
        raise ValidationReplayError(
            "production checkpoint date must be YYYYMMDD"
        )
    market = json.loads(
        (repo_root / MARKET_SESSION_PATH).read_text(
            encoding="utf-8-sig"
        )
    )
    if (
        str(market.get("expected_main_price_date") or "")
        != production_date
    ):
        raise ValidationReplayError(
            "production checkpoint market-session date mismatch"
        )
    production_paths = {
        "market_session": MARKET_SESSION_PATH,
        "daily_price_raw": first_existing(
            repo_root,
            (
                Path(f"data/daily_price/{production_date}.csv"),
            ),
        ),
        "daily_price_normalized": first_existing(
            repo_root,
            (
                Path(
                    f"data/daily_price/daily_price_"
                    f"{production_date}.csv"
                ),
                Path(f"data/daily_price/{production_date}.csv"),
            ),
        ),
        "candidate_inputs": ALL_CANDIDATES_PATH,
        "warrant_raw": Path(
            "output/latest/warrant_daily_raw_latest.csv"
        ),
        "warrant_normalized": WARRANT_FLOW_PATH,
        "trading_calendar": Path(
            "data/market_calendar/"
            "exceptional_non_trading_days.csv"
        ),
    }
    sources = []
    for category, relative in production_paths.items():
        path = repo_root / relative
        if not path.is_file():
            raise ValidationReplayError(
                f"production checkpoint source missing: {relative}"
            )
        sources.append(
            {
                "category": category,
                "identity": (
                    f"{category}:{production_date}:"
                    f"{sha256_file(path)}"
                ),
                "source_url": (
                    f"repo+producer://daily-full-pipeline/{category}/"
                    f"{production_date}@{source_sha}"
                ),
                "artifact_path": relative.as_posix(),
                "bytes": path.stat().st_size,
                "sha256": sha256_file(path),
            }
        )
    for category in (
        "daily_price_raw",
        "daily_price_normalized",
        "candidate_inputs",
        "warrant_raw",
        "warrant_normalized",
    ):
        require_csv_exact_date(
            repo_root / production_paths[category],
            production_date,
            ("date", "report_date", "signal_date", "price_date"),
            f"production checkpoint {category}",
        )
    source_revision = {
        "schema_version": 1,
        "replay_date": production_date,
        "revision_kind": "live_production_capture",
        "source_sha": source_sha,
        "generated_at_utc": datetime.now(timezone.utc).isoformat(),
        "byte_parity_with_run_31174813266": False,
        "sources": sources,
    }
    source_revision_path = (
        runner_temp / SOURCE_REVISION_FILENAME
    )
    source_revision_path.write_bytes(
        canonical_json_bytes(source_revision)
    )
    required = [row["artifact_path"] for row in sources]
    paths = checkpoint_paths(repo_root, required)
    manifest = checkpoint.create_checkpoint(
        repo_root=repo_root,
        bundle_dir=args.bundle_dir.resolve(),
        paths=paths,
        replay_date=production_date,
        source_sha=source_sha,
        producer_run_id=args.run_id,
        producer_head_sha=source_sha,
        source_identity_manifest=source_revision_path,
        checkpoint_kind="pre_step41",
        producer_steps=["Build volume breakout watch"],
        locked_replay_date=None,
        capture_context="production_pre_step41",
    )
    print(
        json.dumps(
            {
                "status": "production_pre_step41_checkpoint_ready",
                "files": len(manifest["files"]),
            },
            sort_keys=True,
        )
    )
    return 0


def write_validation_only_pdf_source_readme(
    *,
    repo_root: Path,
    replay_source_sha: str,
    transition: dict[str, Any],
    validation_env: dict[str, str],
) -> Path:
    if validation_env.get("DAILY_FULL_VALIDATION_ONLY") != "1":
        raise ValidationReplayError(
            "validation-only PDF source README requires validation-only mode"
        )
    replay_source_sha = require_sha(
        replay_source_sha, "replay_source_sha"
    )
    checkpoint_source_sha = require_sha(
        str(transition.get("checkpoint_source_sha") or ""),
        "checkpoint_source_sha",
    )
    _columns, rows = read_csv_rows(repo_root / FRESHNESS_PATH)
    if len(rows) != 1:
        raise ValidationReplayError(
            "validation-only PDF source README requires one freshness row"
        )
    freshness = rows[0]
    for field in (
        "expected_main_price_date",
        "main_price_date",
        "stock_monitor_price_date",
        "all_candidates_date",
        "official_price_fetch_date",
        "warrant_flow_date",
    ):
        if freshness.get(field, "") != REPLAY_DATE:
            raise ValidationReplayError(
                "validation-only PDF source README freshness date mismatch: "
                f"{field}={freshness.get(field, '')!r}"
            )
    for field in ("report_ready", "warrant_ready", "daily_pdf_ready"):
        if str(freshness.get(field, "")).strip().lower() != "true":
            raise ValidationReplayError(
                "validation-only PDF source README readiness mismatch: "
                f"{field}={freshness.get(field, '')!r}"
            )
    market = json.loads(
        (repo_root / MARKET_SESSION_PATH).read_text(encoding="utf-8-sig")
    )
    if market.get("expected_main_price_date") != REPLAY_DATE:
        raise ValidationReplayError(
            "validation-only PDF source README market date mismatch"
        )
    if not (repo_root / PACKET_PATH).is_file():
        raise ValidationReplayError(
            f"PDF source-gate artifact missing: {PACKET_PATH}"
        )
    fields = {
        "validation_only": "true",
        "production_not_run": "true",
        "official_pdf_published": "false",
        "repo_artifacts_pushed": "false",
        "main_price_date": REPLAY_DATE,
        "expected_main_price_date": REPLAY_DATE,
        "market_session_date": str(
            market.get("market_session_date") or REPLAY_DATE
        ),
        "market_status": str(market.get("market_status") or ""),
        "report_ready": "True",
        "warrant_ready": "True",
        "daily_pdf_ready": "True",
        "warrant_source_status": str(
            freshness.get("warrant_source_status") or "ok"
        ),
        "warrant_pdf_visibility": str(
            freshness.get("warrant_pdf_visibility") or "visible"
        ),
        "warrant_source_status_note": (
            "validation-only authoritative historical replay"
        ),
        "checkpoint_source_sha": checkpoint_source_sha,
        "replay_source_sha": replay_source_sha,
        "source_commit_sha": replay_source_sha,
    }
    path = repo_root / README_PATH
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        "".join(f"{key}={value}\n" for key, value in fields.items()),
        encoding="utf-8",
        newline="\n",
    )
    return path


def read_key_value_file(path: Path) -> dict[str, str]:
    fields: dict[str, str] = {}
    for raw_line in path.read_text(
        encoding="utf-8-sig", errors="strict"
    ).splitlines():
        line = raw_line.strip()
        if not line or "=" not in line:
            continue
        key, value = line.split("=", 1)
        fields[key.strip()] = value.strip()
    return fields


def require_freshness_contract(
    repo_root: Path,
    source_sha: str,
    checkpoint_source_sha: str,
) -> dict[str, Any]:
    _columns, rows = read_csv_rows(repo_root / FRESHNESS_PATH)
    if len(rows) != 1:
        raise ValidationReplayError(
            "data freshness artifact must contain exactly one row"
        )
    row = rows[0]
    date_fields = (
        "expected_main_price_date",
        "main_price_date",
        "stock_monitor_price_date",
        "all_candidates_date",
        "official_price_fetch_date",
        "warrant_flow_date",
    )
    mismatches = {
        field: row.get(field, "")
        for field in date_fields
        if row.get(field, "") != REPLAY_DATE
    }
    if mismatches:
        raise ValidationReplayError(
            f"replay freshness date mismatch: {mismatches}"
        )
    for field in ("report_ready", "warrant_ready", "daily_pdf_ready"):
        if str(row.get(field, "")).strip().lower() != "true":
            raise ValidationReplayError(
                f"replay freshness {field} must be True"
            )
    market = json.loads(
        (repo_root / MARKET_SESSION_PATH).read_text(
            encoding="utf-8-sig"
        )
    )
    if market.get("expected_main_price_date") != REPLAY_DATE:
        raise ValidationReplayError(
            "market-session expected date drifted after replay"
        )
    for required in (README_PATH, PACKET_PATH):
        if not (repo_root / required).is_file():
            raise ValidationReplayError(
                f"PDF source-gate artifact missing: {required}"
            )
    readme_fields = read_key_value_file(repo_root / README_PATH)
    expected_readme_fields = {
        "validation_only": "true",
        "production_not_run": "true",
        "official_pdf_published": "false",
        "repo_artifacts_pushed": "false",
        "main_price_date": REPLAY_DATE,
        "expected_main_price_date": REPLAY_DATE,
        "report_ready": "True",
        "warrant_ready": "True",
        "daily_pdf_ready": "True",
        "checkpoint_source_sha": checkpoint_source_sha,
        "replay_source_sha": source_sha,
        "source_commit_sha": source_sha,
    }
    readme_mismatches = {
        key: readme_fields.get(key)
        for key, expected in expected_readme_fields.items()
        if readme_fields.get(key) != expected
    }
    if readme_mismatches:
        raise ValidationReplayError(
            "validation-only PDF source README identity mismatch: "
            f"{readme_mismatches}"
        )
    state = {
        "source": f"validation-checkpoint:{source_sha}",
        "source_ref": f"validation-checkpoint:{source_sha}",
        "source_commit_sha": source_sha,
        "freshness_path": str((repo_root / FRESHNESS_PATH).resolve()),
        "readme_path": str((repo_root / README_PATH).resolve()),
        "packet_path": str((repo_root / PACKET_PATH).resolve()),
        "market_session_status_path": str(
            (repo_root / MARKET_SESSION_PATH).resolve()
        ),
        "market_session_status": str(
            market.get("market_status") or ""
        ),
        "market_session_date": str(
            market.get("market_session_date") or ""
        ),
        "expected_main_price_date": REPLAY_DATE,
        "main_price_date": REPLAY_DATE,
        "report_ready": True,
        "warrant_ready": True,
        "warrant_daily_publish_allowed": True,
        "warrant_pdf_visibility": str(
            row.get("warrant_pdf_visibility") or "visible"
        ),
        "warrant_source_status": str(
            row.get("warrant_source_status") or "ok"
        ),
        "daily_pdf_ready": True,
        "allow_report_generation": True,
        "freshness_fields": row,
        "readme_fields": readme_fields,
        "packet_fields": {},
        "market_session_fields": market,
        "validation_replay_main_price_date": REPLAY_DATE,
        "market_session_validation_scope": "authoritative_historical_revision",
        "live_market_session_status": str(
            market.get("market_status") or ""
        ),
        "live_market_session_date": str(
            market.get("market_session_date") or ""
        ),
        "live_expected_main_price_date": REPLAY_DATE,
    }
    return state


def require_authorized_checkpoint_revision_transition(
    *,
    repo_root: Path,
    checkpoint_source_sha: str,
    replay_source_sha: str,
    checkpoint_run_id: str,
    checkpoint_artifact_id: str,
    checkpoint_artifact_digest: str,
) -> dict[str, Any]:
    checkpoint_source_sha = require_sha(
        checkpoint_source_sha, "checkpoint_source_sha"
    )
    replay_source_sha = require_sha(replay_source_sha, "replay_source_sha")
    if (
        not str(checkpoint_run_id).isdigit()
        or not str(checkpoint_artifact_id).isdigit()
        or not re.fullmatch(
            r"sha256:[0-9a-f]{64}", checkpoint_artifact_digest
        )
    ):
        raise ValidationReplayError(
            "checkpoint replay identity inputs are malformed"
        )
    if checkpoint_source_sha == replay_source_sha:
        return {
            "mode": "same_source",
            "checkpoint_source_sha": checkpoint_source_sha,
            "replay_source_sha": replay_source_sha,
            "checkpoint_run_id": str(checkpoint_run_id),
            "checkpoint_artifact_id": str(checkpoint_artifact_id),
            "checkpoint_artifact_digest": checkpoint_artifact_digest,
        }
    observed = (
        checkpoint_source_sha,
        str(checkpoint_run_id),
        str(checkpoint_artifact_id),
        checkpoint_artifact_digest,
    )
    expected = (
        AUTHORIZED_CHECKPOINT_SOURCE_SHA,
        AUTHORIZED_CHECKPOINT_RUN_ID,
        AUTHORIZED_CHECKPOINT_ARTIFACT_ID,
        AUTHORIZED_CHECKPOINT_ARTIFACT_DIGEST,
    )
    if observed != expected:
        raise ValidationReplayError(
            "checkpoint replay source transition is not preauthorized"
        )
    for ancestor, label in (
        (checkpoint_source_sha, "checkpoint source"),
        (AUTHORIZED_PRODUCER_FIX_COMMIT, "producer fix"),
        (AUTHORIZED_VALIDATOR_FIX_COMMIT, "validator fix"),
        (AUTHORIZED_FORMAL_LINEAGE_FIX_COMMIT, "formal lineage fix"),
        (
            AUTHORIZED_OPERATION_COMPLETENESS_FIX_COMMIT,
            "operation completeness fix",
        ),
    ):
        result = subprocess.run(
            ["git", "merge-base", "--is-ancestor", ancestor, replay_source_sha],
            cwd=repo_root,
            check=False,
        )
        if result.returncode != 0:
            raise ValidationReplayError(
                f"authorized {label} is not an ancestor of replay source"
            )
    transition_order = subprocess.run(
        [
            "git",
            "merge-base",
            "--is-ancestor",
            AUTHORIZED_PRODUCER_FIX_COMMIT,
            AUTHORIZED_VALIDATOR_FIX_COMMIT,
        ],
        cwd=repo_root,
        check=False,
    )
    if transition_order.returncode != 0:
        raise ValidationReplayError(
            "authorized validator fix does not descend from the producer fix"
        )
    formal_transition_order = subprocess.run(
        [
            "git",
            "merge-base",
            "--is-ancestor",
            AUTHORIZED_VALIDATOR_FIX_COMMIT,
            AUTHORIZED_FORMAL_LINEAGE_FIX_COMMIT,
        ],
        cwd=repo_root,
        check=False,
    )
    if formal_transition_order.returncode != 0:
        raise ValidationReplayError(
            "authorized formal lineage fix does not descend from the validator fix"
        )
    operation_transition_order = subprocess.run(
        [
            "git",
            "merge-base",
            "--is-ancestor",
            AUTHORIZED_FORMAL_LINEAGE_FIX_COMMIT,
            AUTHORIZED_OPERATION_COMPLETENESS_FIX_COMMIT,
        ],
        cwd=repo_root,
        check=False,
    )
    if operation_transition_order.returncode != 0:
        raise ValidationReplayError(
            "authorized operation completeness fix does not descend from "
            "the formal lineage fix"
        )
    validator_paths = set(AUTHORIZED_VALIDATOR_FIX_PATHS)
    producer_paths = set(AUTHORIZED_PRODUCER_FIX_PATHS)
    if not validator_paths or not validator_paths <= producer_paths:
        raise ValidationReplayError(
            "authorized validator fix paths are outside the producer contract"
        )
    stable_producer_paths = tuple(
        path
        for path in AUTHORIZED_PRODUCER_FIX_PATHS
        if path not in validator_paths
    )
    formal_paths = set(AUTHORIZED_FORMAL_LINEAGE_FIX_PATHS)
    operation_paths = set(AUTHORIZED_OPERATION_COMPLETENESS_FIX_PATHS)
    if formal_paths & operation_paths != {
        AUTHORIZED_FORMAL_OPERATION_SHARED_PATH
    }:
        raise ValidationReplayError(
            "authorized formal/operation fix path overlap is not exact"
        )
    stable_formal_paths = tuple(
        path
        for path in AUTHORIZED_FORMAL_LINEAGE_FIX_PATHS
        if path not in operation_paths
    )
    if not stable_formal_paths or not operation_paths:
        raise ValidationReplayError(
            "authorized formal/operation fix path contract is empty"
        )
    for base_sha, label, paths in (
        (
            AUTHORIZED_PRODUCER_FIX_COMMIT,
            "producer fix",
            stable_producer_paths,
        ),
        (
            AUTHORIZED_VALIDATOR_FIX_COMMIT,
            "validator fix",
            AUTHORIZED_VALIDATOR_FIX_PATHS,
        ),
        (
            AUTHORIZED_FORMAL_LINEAGE_FIX_COMMIT,
            "formal lineage fix",
            stable_formal_paths,
        ),
        (
            AUTHORIZED_OPERATION_COMPLETENESS_FIX_COMMIT,
            "operation completeness fix",
            AUTHORIZED_OPERATION_COMPLETENESS_FIX_PATHS,
        ),
    ):
        drift = subprocess.run(
            [
                "git",
                "diff",
                "--quiet",
                base_sha,
                replay_source_sha,
                "--",
                *paths,
            ],
            cwd=repo_root,
            check=False,
        )
        if drift.returncode != 0:
            raise ValidationReplayError(
                f"authorized {label} paths drifted after the pinned revision"
            )
    return {
        "mode": "authorized_code_revision_transition",
        "checkpoint_source_sha": checkpoint_source_sha,
        "replay_source_sha": replay_source_sha,
        "checkpoint_run_id": str(checkpoint_run_id),
        "checkpoint_artifact_id": str(checkpoint_artifact_id),
        "checkpoint_artifact_digest": checkpoint_artifact_digest,
        "checkpoint_manifest_sha256": (
            AUTHORIZED_CHECKPOINT_MANIFEST_SHA256
        ),
        "producer_fix_commit": AUTHORIZED_PRODUCER_FIX_COMMIT,
        "producer_fix_paths": list(AUTHORIZED_PRODUCER_FIX_PATHS),
        "validator_fix_commit": AUTHORIZED_VALIDATOR_FIX_COMMIT,
        "validator_fix_paths": list(AUTHORIZED_VALIDATOR_FIX_PATHS),
        "formal_lineage_fix_commit": AUTHORIZED_FORMAL_LINEAGE_FIX_COMMIT,
        "formal_lineage_fix_paths": list(
            AUTHORIZED_FORMAL_LINEAGE_FIX_PATHS
        ),
        "operation_completeness_fix_commit": (
            AUTHORIZED_OPERATION_COMPLETENESS_FIX_COMMIT
        ),
        "operation_completeness_fix_paths": list(
            AUTHORIZED_OPERATION_COMPLETENESS_FIX_PATHS
        ),
        "formal_operation_shared_path": (
            AUTHORIZED_FORMAL_OPERATION_SHARED_PATH
        ),
    }


def require_authorized_checkpoint_bundle_identity(bundle_dir: Path) -> None:
    manifest_path = bundle_dir / checkpoint.CHECKPOINT_MANIFEST
    sidecar_path = bundle_dir / checkpoint.CHECKPOINT_MANIFEST_SHA
    if not manifest_path.is_file() or not sidecar_path.is_file():
        raise ValidationReplayError(
            "authorized checkpoint manifest or sidecar is missing"
        )
    manifest_sha = sha256_file(manifest_path)
    sidecar_sha = sidecar_path.read_text(encoding="ascii").strip().lower()
    if (
        manifest_sha != AUTHORIZED_CHECKPOINT_MANIFEST_SHA256
        or sidecar_sha != AUTHORIZED_CHECKPOINT_MANIFEST_SHA256
    ):
        raise ValidationReplayError(
            "authorized checkpoint manifest/sidecar SHA mismatch"
        )


def checkpoint_manifest_file_mode(path: Path) -> int:
    return path.lstat().st_mode


def require_checkpoint_structured_source_manifest_identity(
    *,
    repo_root: Path,
    checkpoint_manifest: dict[str, Any],
    checkpoint_source_sha: str,
) -> Path:
    expected_suffix = f"/{REPLAY_DATE}/structured_source_manifest.json"
    entries = [
        row
        for row in checkpoint_manifest.get("files", [])
        if isinstance(row, dict)
        and str(row.get("path") or "").startswith(
            "output/history/historical_source_replay/"
        )
        and str(row.get("path") or "").endswith(expected_suffix)
    ]
    if len(entries) != 1:
        raise ValidationReplayError(
            "checkpoint structured source manifest has no unique allowlist entry"
        )
    entry = entries[0]
    relative = str(entry.get("path") or "")
    expected_bytes = entry.get("bytes")
    expected_sha = str(entry.get("sha256") or "").lower()
    if (
        ".." in Path(relative).parts
        or not isinstance(expected_bytes, int)
        or expected_bytes <= 0
        or not re.fullmatch(r"[0-9a-f]{64}", expected_sha)
    ):
        raise ValidationReplayError(
            "checkpoint structured source manifest path/date identity mismatch"
        )
    path = repo_root / relative
    if not path.exists() or path.is_symlink():
        raise ValidationReplayError(
            "restored checkpoint structured source manifest is missing"
        )
    mode = checkpoint_manifest_file_mode(path)
    if not stat.S_ISREG(mode) or stat.S_IMODE(mode) & 0o111:
        raise ValidationReplayError(
            "checkpoint structured source manifest mode mismatch: "
            f"observed={stat.filemode(mode)}"
        )
    raw = path.read_bytes()
    observed_sha = hashlib.sha256(raw).hexdigest()
    if len(raw) != expected_bytes or observed_sha != expected_sha:
        raise ValidationReplayError(
            "restored checkpoint structured source manifest bytes/SHA mismatch"
        )
    try:
        payload = json.loads(raw.decode("utf-8"))
    except (UnicodeDecodeError, json.JSONDecodeError) as error:
        raise ValidationReplayError(
            "restored checkpoint structured source manifest is not UTF-8 JSON"
        ) from error
    if payload.get("report_date") != REPLAY_DATE:
        raise ValidationReplayError(
            "checkpoint structured source manifest report date mismatch"
        )
    if payload.get("pipeline_commit_sha") != checkpoint_source_sha:
        raise ValidationReplayError(
            "checkpoint structured source manifest source SHA mismatch: "
            f"expected={checkpoint_source_sha} "
            f"observed={payload.get('pipeline_commit_sha')!r}"
        )
    return path


def require_checkpoint_source_revision_manifest_identity(
    *,
    bundle_dir: Path,
    repo_root: Path,
    checkpoint_manifest: dict[str, Any],
    checkpoint_source_sha: str,
    structured_source_manifest: Path | None,
) -> Path:
    metadata = checkpoint_manifest.get("source_revision_manifest")
    if not isinstance(metadata, dict) or set(metadata) != {
        "bytes",
        "path",
        "sha256",
    }:
        raise ValidationReplayError(
            "checkpoint source revision manifest metadata is malformed"
        )
    relative = str(metadata.get("path") or "")
    if relative != SOURCE_REVISION_FILENAME:
        raise ValidationReplayError(
            "checkpoint source revision manifest path/object mismatch: "
            f"expected={SOURCE_REVISION_FILENAME} observed={relative!r}"
        )
    expected_bytes = metadata.get("bytes")
    expected_sha = str(metadata.get("sha256") or "").lower()
    if (
        not isinstance(expected_bytes, int)
        or expected_bytes <= 0
        or not re.fullmatch(r"[0-9a-f]{64}", expected_sha)
    ):
        raise ValidationReplayError(
            "checkpoint source revision manifest bytes/SHA metadata is malformed"
        )
    source_path = bundle_dir / relative
    if not source_path.exists() or source_path.is_symlink():
        raise ValidationReplayError(
            "checkpoint source revision manifest is missing or not a regular file"
        )
    mode = checkpoint_manifest_file_mode(source_path)
    if not stat.S_ISREG(mode) or stat.S_IMODE(mode) & 0o111:
        raise ValidationReplayError(
            "checkpoint source revision manifest mode mismatch: "
            f"observed={stat.filemode(mode)}"
        )
    raw = source_path.read_bytes()
    raw_sha = hashlib.sha256(raw).hexdigest()
    if len(raw) != expected_bytes or raw_sha != expected_sha:
        raise ValidationReplayError(
            "checkpoint source revision manifest raw bytes/SHA mismatch: "
            f"expected_bytes={expected_bytes} observed_bytes={len(raw)} "
            f"expected_sha={expected_sha} observed_sha={raw_sha}"
        )
    try:
        payload = json.loads(raw.decode("utf-8"))
    except (UnicodeDecodeError, json.JSONDecodeError) as error:
        raise ValidationReplayError(
            "checkpoint source revision manifest is not canonical UTF-8 JSON"
        ) from error
    canonical = canonical_json_bytes(payload)
    canonical_sha = hashlib.sha256(canonical).hexdigest()
    if raw != canonical or canonical_sha != expected_sha:
        raise ValidationReplayError(
            "checkpoint source revision manifest raw/canonical SHA mismatch: "
            f"raw_sha={raw_sha} canonical_sha={canonical_sha} "
            f"expected_sha={expected_sha}"
        )
    if payload.get("schema_version") != 1:
        raise ValidationReplayError(
            "checkpoint source revision manifest schema mismatch"
        )
    if payload.get("revision_kind") != "authoritative_historical_revision":
        raise ValidationReplayError(
            "checkpoint source revision manifest revision kind mismatch"
        )
    if payload.get("replay_date") != REPLAY_DATE:
        raise ValidationReplayError(
            "checkpoint source revision manifest date mismatch: "
            f"expected={REPLAY_DATE} observed={payload.get('replay_date')!r}"
        )
    if payload.get("source_sha") != checkpoint_source_sha:
        raise ValidationReplayError(
            "checkpoint source revision manifest source SHA mismatch: "
            f"expected={checkpoint_source_sha} "
            f"observed={payload.get('source_sha')!r}"
        )
    structured = payload.get("structured_source_manifest")
    if not isinstance(structured, dict) or set(structured) != {
        "bytes",
        "path",
        "sha256",
    }:
        raise ValidationReplayError(
            "checkpoint structured source manifest identity is malformed"
        )
    structured_relative = str(structured.get("path") or "")
    structured_bytes = structured.get("bytes")
    structured_sha = str(structured.get("sha256") or "").lower()
    expected_suffix = f"/{REPLAY_DATE}/structured_source_manifest.json"
    if (
        not structured_relative.startswith(
            "output/history/historical_source_replay/"
        )
        or not structured_relative.endswith(expected_suffix)
        or ".." in Path(structured_relative).parts
        or not isinstance(structured_bytes, int)
        or structured_bytes <= 0
        or not re.fullmatch(r"[0-9a-f]{64}", structured_sha)
    ):
        raise ValidationReplayError(
            "checkpoint structured source manifest path/date identity mismatch"
        )
    observed_relative = structured_source_manifest.relative_to(
        repo_root
    ).as_posix()
    structured_raw = structured_source_manifest.read_bytes()
    if (
        observed_relative != structured_relative
        or len(structured_raw) != structured_bytes
        or hashlib.sha256(structured_raw).hexdigest() != structured_sha
    ):
        raise ValidationReplayError(
            "checkpoint structured source manifest identity/allowlist mismatch"
        )
    return source_path


def write_replay_source_revision_manifest(
    *,
    source_manifest_path: Path,
    output_path: Path,
    transition: dict[str, Any],
) -> Path:
    payload = json.loads(source_manifest_path.read_text(encoding="utf-8"))
    checkpoint_source_sha = str(transition["checkpoint_source_sha"])
    replay_source_sha = str(transition["replay_source_sha"])
    if payload.get("source_sha") != checkpoint_source_sha:
        raise ValidationReplayError(
            "checkpoint source revision manifest source SHA mismatch: "
            f"expected={checkpoint_source_sha} "
            f"observed={payload.get('source_sha')!r}"
        )
    payload["source_sha"] = replay_source_sha
    payload["checkpoint_source_sha"] = checkpoint_source_sha
    payload["replay_source_sha"] = replay_source_sha
    payload["revision_transition"] = {
        **transition,
        "checkpoint_source_manifest_sha256": sha256_file(
            source_manifest_path
        ),
    }
    output_path.write_bytes(canonical_json_bytes(payload))
    return output_path


def write_validation_source_state(
    repo_root: Path,
    replay_source_sha: str,
    transition: dict[str, Any],
) -> dict[str, Any]:
    state = require_freshness_contract(
        repo_root,
        replay_source_sha,
        str(transition["checkpoint_source_sha"]),
    )
    state["checkpoint_source_sha"] = transition["checkpoint_source_sha"]
    state["replay_source_sha"] = replay_source_sha
    files = {}
    for relative in (
        FRESHNESS_PATH,
        README_PATH,
        PACKET_PATH,
        MARKET_SESSION_PATH,
    ):
        path = repo_root / relative
        files[relative.as_posix()] = {
            "bytes": path.stat().st_size,
            "sha256": sha256_file(path),
        }
    payload = {
        "schema_version": 1,
        "replay_date": REPLAY_DATE,
        "source_sha": replay_source_sha,
        "checkpoint_source_sha": transition["checkpoint_source_sha"],
        "replay_source_sha": replay_source_sha,
        "revision_transition": transition,
        "source_state": state,
        "files": files,
        "safety": {
            "validation_only": True,
            "official_pdf_published": False,
            "repo_artifacts_pushed": False,
        },
    }
    path = repo_root / VALIDATION_SOURCE_STATE_PATH
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(canonical_json_bytes(payload))
    return payload


def materialize_publish_freshness_baseline(
    *,
    repo_root: Path,
    runner_temp: Path,
    checkpoint_source_sha: str,
    checkpoint_manifest: dict[str, Any],
) -> dict[str, Any]:
    relative = FRESHNESS_PATH.as_posix()
    entries = [
        row
        for row in checkpoint_manifest.get("files", [])
        if isinstance(row, dict) and row.get("path") == relative
    ]
    if len(entries) != 1:
        raise ValidationReplayError(
            "checkpoint has no unique publish freshness baseline entry"
        )
    baseline = entries[0].get("baseline")
    if not isinstance(baseline, dict) or baseline.get("exists") is not True:
        raise ValidationReplayError(
            "checkpoint publish freshness baseline is missing"
        )
    expected_bytes = baseline.get("bytes")
    expected_sha = str(baseline.get("sha256") or "").lower()
    if (
        not isinstance(expected_bytes, int)
        or expected_bytes <= 0
        or not re.fullmatch(r"[0-9a-f]{64}", expected_sha)
    ):
        raise ValidationReplayError(
            "checkpoint publish freshness baseline metadata is malformed"
        )
    result = subprocess.run(
        [
            "git",
            "show",
            f"{checkpoint_source_sha}:{relative}",
        ],
        cwd=repo_root,
        env={**os.environ, "GIT_NO_REPLACE_OBJECTS": "1"},
        check=False,
        capture_output=True,
    )
    baseline_bytes = result.stdout
    if result.returncode != 0:
        raise ValidationReplayError(
            "cannot materialize publish freshness baseline from "
            "checkpoint source Git object"
        )
    if (
        len(baseline_bytes) != expected_bytes
        or hashlib.sha256(baseline_bytes).hexdigest() != expected_sha
    ):
        raise ValidationReplayError(
            "checkpoint publish freshness baseline bytes/SHA mismatch"
        )
    current_path = repo_root / FRESHNESS_PATH
    if not current_path.is_file():
        raise ValidationReplayError(
            "restored current freshness artifact is missing"
        )
    current_bytes = current_path.read_bytes()
    current_sha = hashlib.sha256(current_bytes).hexdigest()
    if current_sha == expected_sha or current_bytes == baseline_bytes:
        raise ValidationReplayError(
            "current freshness artifact cannot substitute for baseline"
        )
    destination = (
        runner_temp / PUBLISH_BASELINE_DIRNAME / FRESHNESS_PATH.name
    )
    if destination.exists():
        raise ValidationReplayError(
            "publish freshness baseline destination already exists"
        )
    destination.parent.mkdir(parents=True, exist_ok=False)
    destination.write_bytes(baseline_bytes)
    columns, rows = read_csv_rows(destination)
    required_date_fields = (
        "market_session_date",
        "expected_main_price_date",
        "main_price_date",
    )
    if len(rows) != 1 or not set(required_date_fields) <= set(columns):
        raise ValidationReplayError(
            "publish freshness baseline row/date contract is malformed"
        )
    observed_dates = {
        str(rows[0].get(field) or "").strip()
        for field in required_date_fields
    }
    if observed_dates != {AUTHORIZED_PUBLISH_BASELINE_DATE}:
        raise ValidationReplayError(
            "publish freshness baseline date mismatch: "
            f"observed={sorted(observed_dates)}"
        )
    if (
        str(rows[0].get("report_ready") or "").strip().lower()
        != "false"
        or str(rows[0].get("daily_pdf_ready") or "").strip().lower()
        != "false"
    ):
        raise ValidationReplayError(
            "publish freshness baseline readiness contract mismatch"
        )
    if (
        destination.stat().st_size != expected_bytes
        or sha256_file(destination) != expected_sha
    ):
        raise ValidationReplayError(
            "materialized publish freshness baseline drifted"
        )
    evidence = {
        "schema_version": 1,
        "replay_date": REPLAY_DATE,
        "checkpoint_source_sha": checkpoint_source_sha,
        "baseline_source_path": relative,
        "baseline_date": AUTHORIZED_PUBLISH_BASELINE_DATE,
        "baseline_bytes": expected_bytes,
        "baseline_sha256": expected_sha,
        "current_bytes": len(current_bytes),
        "current_sha256": current_sha,
        "current_substitution_forbidden": True,
        "materialized_relative_path": (
            f"{PUBLISH_BASELINE_DIRNAME}/{FRESHNESS_PATH.name}"
        ),
    }
    evidence_path = repo_root / PUBLISH_BASELINE_EVIDENCE_PATH
    evidence_path.parent.mkdir(parents=True, exist_ok=True)
    evidence_path.write_bytes(canonical_json_bytes(evidence))
    return evidence


def capture_replay_failure_checkpoint(
    *,
    repo_root: Path,
    runner_temp: Path,
    bundle_dir: Path,
    source_sha: str,
    run_id: str,
    checkpoint_source_sha: str,
    structured_source_manifest: Path,
    replay_source_manifest: Path | None,
    failure_phase: str,
    steps: Sequence[dict[str, str]],
    error: Exception,
) -> dict[str, Any]:
    step_path = repo_root / STEP_RESULTS_PATH
    step_path.parent.mkdir(parents=True, exist_ok=True)
    step_path.write_bytes(
        canonical_json_bytes(
            {
                "schema_version": 1,
                "mode": "replay_failure",
                "replay_date": REPLAY_DATE,
                "source_sha": source_sha,
                "checkpoint_source_sha": checkpoint_source_sha,
                "failure_phase": failure_phase,
                "error": str(error),
                "steps": list(steps),
                "production_not_run": True,
                "official_pdf_published": False,
            }
        )
    )
    producer_steps = [
        f"{row.get('step', 'unknown')}:{row.get('status', 'unknown')}"
        for row in steps
    ] or [f"{failure_phase}:failure"]
    return capture_checkpoint(
        repo_root=repo_root,
        bundle_dir=bundle_dir,
        runner_temp=runner_temp,
        source_sha=source_sha,
        run_id=run_id,
        structured_manifest_path=structured_source_manifest,
        revision_kind="authoritative_historical_revision",
        checkpoint_kind="post_validation",
        capture_context="validation_replay",
        producer_steps=producer_steps,
        source_revision_manifest_path=replay_source_manifest,
    )


def write_minimal_replay_failure_upload_receipt(
    *,
    bundle_dir: Path,
    source_sha: str,
    checkpoint_source_sha: str,
    run_id: str,
    failure_phase: str,
    error: Exception,
    capture_error: Exception,
) -> Path:
    bundle_dir.mkdir(parents=True, exist_ok=True)
    payload = {
        "schema_version": 1,
        "mode": "replay_failure_minimal_receipt",
        "replay_date": REPLAY_DATE,
        "source_sha": source_sha,
        "checkpoint_source_sha": checkpoint_source_sha,
        "run_id": str(run_id),
        "failure_phase": failure_phase,
        "error": str(error),
        "full_checkpoint_capture_error": str(capture_error),
        "production_not_run": True,
        "official_pdf_published": False,
        "repo_artifacts_pushed": False,
    }
    path = bundle_dir / "replay_failure_evidence.json"
    if path.exists():
        raise ValidationReplayError(
            "minimal replay failure receipt destination already exists"
        )
    path.write_bytes(canonical_json_bytes(payload))
    sidecar = bundle_dir / "replay_failure_evidence.json.sha256"
    sidecar.write_text(sha256_file(path) + "\n", encoding="ascii")
    return path


def replay_from_checkpoint(args: argparse.Namespace) -> int:
    repo_root = args.repo_root.resolve()
    runner_temp = args.runner_temp.resolve()
    runner_temp.mkdir(parents=True, exist_ok=True)
    source_sha = require_sha(args.source_sha, "replay_source_sha")
    checkpoint_source_sha = require_sha(
        args.checkpoint_source_sha, "checkpoint_source_sha"
    )
    require_exact_date(args.replay_date, "replay_date")
    require_main_source(repo_root, source_sha)
    transition = require_authorized_checkpoint_revision_transition(
        repo_root=repo_root,
        checkpoint_source_sha=checkpoint_source_sha,
        replay_source_sha=source_sha,
        checkpoint_run_id=args.checkpoint_run_id,
        checkpoint_artifact_id=args.checkpoint_artifact_id,
        checkpoint_artifact_digest=args.checkpoint_artifact_digest,
    )
    bundle_dir = args.bundle_dir.resolve()
    if transition["mode"] == "authorized_code_revision_transition":
        require_authorized_checkpoint_bundle_identity(bundle_dir)
    checkpoint_manifest = checkpoint.restore_checkpoint(
        bundle_dir=bundle_dir,
        destination_root=repo_root,
        expected_source_sha=checkpoint_source_sha,
        expected_destination_source_sha=source_sha,
        expected_run_id=args.checkpoint_run_id,
        expected_kind="pre_step41",
        expected_capture_context="validation_canary",
    )
    steps: list[dict[str, str]] = []
    checkpoint_structured_manifest: Path | None = None
    replay_source_manifest: Path | None = None
    failure_phase = "verify checkpoint structured source manifest"
    try:
        checkpoint_structured_manifest = (
            require_checkpoint_structured_source_manifest_identity(
                repo_root=repo_root,
                checkpoint_manifest=checkpoint_manifest,
                checkpoint_source_sha=checkpoint_source_sha,
            )
        )
        failure_phase = "verify checkpoint source revision manifest"
        source_revision_manifest = (
            require_checkpoint_source_revision_manifest_identity(
                bundle_dir=bundle_dir,
                repo_root=repo_root,
                checkpoint_manifest=checkpoint_manifest,
                checkpoint_source_sha=checkpoint_source_sha,
                structured_source_manifest=checkpoint_structured_manifest,
            )
        )
        failure_phase = "write replay source revision manifest"
        replay_source_manifest = write_replay_source_revision_manifest(
            source_manifest_path=source_revision_manifest,
            output_path=runner_temp / "replay_source_revision_manifest.json",
            transition=transition,
        )
        failure_phase = "materialize publish freshness baseline"
        materialize_publish_freshness_baseline(
            repo_root=repo_root,
            runner_temp=runner_temp,
            checkpoint_source_sha=checkpoint_source_sha,
            checkpoint_manifest=checkpoint_manifest,
        )
        failure_phase = "prepare replay environment"
        env = base_environment(
            repo_root=repo_root,
            runner_temp=runner_temp,
            source_sha=source_sha,
        )
        market = json.loads(
            (repo_root / MARKET_SESSION_PATH).read_text(
                encoding="utf-8-sig"
            )
        )
        env["MARKET_STATUS"] = str(market.get("market_status") or "")
        env["MARKET_SESSION_DATE"] = str(
            market.get("market_session_date") or REPLAY_DATE
        )
        names = post_step_names(repo_root)
        failure_phase = "run post-step41 validation gates"
        run_named_steps(
            repo_root=repo_root,
            env=env,
            names=names,
            post_mode=True,
            results=steps,
        )
    except Exception as error:
        try:
            capture_replay_failure_checkpoint(
                repo_root=repo_root,
                runner_temp=runner_temp,
                bundle_dir=args.post_bundle_dir.resolve(),
                source_sha=source_sha,
                run_id=args.run_id,
                checkpoint_source_sha=checkpoint_source_sha,
                structured_source_manifest=checkpoint_structured_manifest,
                replay_source_manifest=replay_source_manifest,
                failure_phase=failure_phase,
                steps=steps,
                error=error,
            )
        except Exception as capture_error:
            try:
                write_minimal_replay_failure_upload_receipt(
                    bundle_dir=args.post_bundle_dir.resolve(),
                    source_sha=source_sha,
                    checkpoint_source_sha=checkpoint_source_sha,
                    run_id=args.run_id,
                    failure_phase=failure_phase,
                    error=error,
                    capture_error=capture_error,
                )
            except Exception as receipt_error:
                raise ValidationReplayError(
                    f"{error}; failure checkpoint capture failed: "
                    f"{capture_error}; minimal failure receipt failed: "
                    f"{receipt_error}"
                ) from error
            raise ValidationReplayError(
                f"{error}; failure checkpoint capture failed: "
                f"{capture_error}; minimal failure receipt written"
            ) from error
        raise
    assert checkpoint_structured_manifest is not None
    assert replay_source_manifest is not None
    failure_phase = "run registered replay parity validators"
    try:
        parity_evidence = run_registered_parity_validators(
            repo_root,
            env,
        )
        failure_phase = "materialize validation-only PDF source README"
        write_validation_only_pdf_source_readme(
            repo_root=repo_root,
            replay_source_sha=source_sha,
            transition=transition,
            validation_env=env,
        )
        failure_phase = "write validation replay source state"
        source_state = write_validation_source_state(
            repo_root, source_sha, transition
        )
        parity = {
            "schema_version": 1,
            "replay_date": REPLAY_DATE,
            "source_sha": source_sha,
            "checkpoint_source_sha": checkpoint_source_sha,
            "replay_source_sha": source_sha,
            "revision_transition": transition,
            "checkpoint_run_id": args.checkpoint_run_id,
            "original_failure_step": POST_START_STEP,
            "original_failure_stock_id": "2059",
            "registered_parity_validation": parity_evidence,
            "pdf_source_gate": {
                "status": "pass",
                "main_price_date": source_state["source_state"][
                    "main_price_date"
                ],
                "report_ready": True,
                "daily_pdf_ready": True,
            },
            "production_not_run": True,
            "official_pdf_published": False,
        }
        failure_phase = "write validation replay parity evidence"
        parity_path = repo_root / PARITY_EVIDENCE_PATH
        parity_path.parent.mkdir(parents=True, exist_ok=True)
        parity_path.write_bytes(canonical_json_bytes(parity))
        step_path = repo_root / STEP_RESULTS_PATH
        step_path.write_bytes(
            canonical_json_bytes(
                {
                    "schema_version": 1,
                    "mode": "replay",
                    "replay_date": REPLAY_DATE,
                    "source_sha": source_sha,
                    "checkpoint_source_sha": checkpoint_source_sha,
                    "replay_source_sha": source_sha,
                    "steps": steps,
                }
            )
        )
    except Exception as error:
        try:
            capture_replay_failure_checkpoint(
                repo_root=repo_root,
                runner_temp=runner_temp,
                bundle_dir=args.post_bundle_dir.resolve(),
                source_sha=source_sha,
                run_id=args.run_id,
                checkpoint_source_sha=checkpoint_source_sha,
                structured_source_manifest=checkpoint_structured_manifest,
                replay_source_manifest=replay_source_manifest,
                failure_phase=failure_phase,
                steps=steps,
                error=error,
            )
        except Exception as capture_error:
            try:
                write_minimal_replay_failure_upload_receipt(
                    bundle_dir=args.post_bundle_dir.resolve(),
                    source_sha=source_sha,
                    checkpoint_source_sha=checkpoint_source_sha,
                    run_id=args.run_id,
                    failure_phase=failure_phase,
                    error=error,
                    capture_error=capture_error,
                )
            except Exception as receipt_error:
                raise ValidationReplayError(
                    f"{error}; failure checkpoint capture failed: "
                    f"{capture_error}; minimal failure receipt failed: "
                    f"{receipt_error}"
                ) from error
            raise ValidationReplayError(
                f"{error}; failure checkpoint capture failed: "
                f"{capture_error}; minimal failure receipt written"
            ) from error
        raise
    manifest = capture_checkpoint(
        repo_root=repo_root,
        bundle_dir=args.post_bundle_dir.resolve(),
        runner_temp=runner_temp,
        source_sha=source_sha,
        run_id=args.run_id,
        structured_manifest_path=checkpoint_structured_manifest,
        revision_kind="authoritative_historical_revision",
        checkpoint_kind="post_validation",
        capture_context="validation_replay",
        producer_steps=[row["step"] for row in steps],
        source_revision_manifest_path=replay_source_manifest,
    )
    print(
        json.dumps(
            {
                "status": "post_step_validation_pass",
                "steps": len(steps),
                "files": len(manifest["files"]),
                "pdf_source_gate": "pass",
            },
            sort_keys=True,
        )
    )
    return 0


def verify_local_source_state(
    repo_root: Path, source_sha: str
) -> dict[str, Any]:
    path = repo_root / VALIDATION_SOURCE_STATE_PATH
    if not path.is_file():
        raise ValidationReplayError(
            "validation source-state manifest is missing"
        )
    payload = json.loads(path.read_text(encoding="utf-8"))
    checkpoint_source_sha = str(
        payload.get("checkpoint_source_sha") or source_sha
    )
    replay_source_sha = str(payload.get("replay_source_sha") or source_sha)
    transition = payload.get("revision_transition") or {}
    cross_revision_invalid = checkpoint_source_sha != source_sha and (
        replay_source_sha != source_sha
        or checkpoint_source_sha != AUTHORIZED_CHECKPOINT_SOURCE_SHA
        or transition.get("checkpoint_run_id")
        != AUTHORIZED_CHECKPOINT_RUN_ID
        or transition.get("checkpoint_artifact_id")
        != AUTHORIZED_CHECKPOINT_ARTIFACT_ID
        or transition.get("checkpoint_artifact_digest")
        != AUTHORIZED_CHECKPOINT_ARTIFACT_DIGEST
    )
    if (
        payload.get("replay_date") != REPLAY_DATE
        or payload.get("source_sha") != source_sha
        or replay_source_sha != source_sha
        or cross_revision_invalid
        or payload.get("safety")
        != {
            "validation_only": True,
            "official_pdf_published": False,
            "repo_artifacts_pushed": False,
        }
    ):
        raise ValidationReplayError(
            "validation source-state contract mismatch"
        )
    for relative, expected in payload.get("files", {}).items():
        target = repo_root / relative
        if (
            not target.is_file()
            or target.stat().st_size != expected.get("bytes")
            or sha256_file(target) != expected.get("sha256")
        ):
            raise ValidationReplayError(
                f"validation source-state file drift: {relative}"
            )
    return payload["source_state"]


def render_contact_sheets(
    pdf_paths: Sequence[Path], output_dir: Path
) -> Path:
    try:
        import fitz
        from PIL import Image, ImageDraw
    except ImportError as error:
        raise ValidationReplayError(
            f"PDF visual dependencies are unavailable: {error}"
        ) from error
    evidence_root = output_dir / "visual_evidence"
    pages_root = evidence_root / "pages"
    sheets_root = evidence_root / "contact_sheets"
    pages_root.mkdir(parents=True, exist_ok=True)
    sheets_root.mkdir(parents=True, exist_ok=True)
    pdf_entries: list[dict[str, Any]] = []
    for pdf_index, pdf_path in enumerate(pdf_paths, start=1):
        document = fitz.open(pdf_path)
        if document.page_count < 1:
            raise ValidationReplayError(
                f"PDF has no pages: {pdf_path}"
            )
        page_dir = pages_root / f"pdf_{pdf_index:02d}"
        page_dir.mkdir()
        page_entries = []
        thumbnails: list[tuple[int, Image.Image]] = []
        for page_index in range(document.page_count):
            page = document.load_page(page_index)
            text = page.get_text("text")
            if "\ufffd" in text:
                raise ValidationReplayError(
                    f"PDF page has replacement character: "
                    f"{pdf_path.name} page={page_index + 1}"
                )
            pixmap = page.get_pixmap(matrix=fitz.Matrix(1.25, 1.25))
            image_path = page_dir / f"page_{page_index + 1:04d}.png"
            pixmap.save(str(image_path))
            with Image.open(image_path) as source_image:
                image = source_image.convert("RGB")
                grayscale = image.convert("L")
                histogram = grayscale.histogram()
                nonwhite = sum(histogram[:248])
                ink_ratio = nonwhite / max(1, image.width * image.height)
                if len(text.strip()) < 5 and ink_ratio < 0.002:
                    raise ValidationReplayError(
                        f"blank PDF page detected: {pdf_path.name} "
                        f"page={page_index + 1}"
                    )
                thumb = image.copy()
                thumb.thumbnail((420, 594))
                thumbnails.append((page_index + 1, thumb))
            fonts = sorted(
                {
                    str(row[3] or row[2] or "")
                    for row in page.get_fonts(full=True)
                    if str(row[3] or row[2] or "").strip()
                }
            )
            if not fonts:
                raise ValidationReplayError(
                    f"PDF page has no embedded font evidence: "
                    f"{pdf_path.name} page={page_index + 1}"
                )
            page_entries.append(
                {
                    "page": page_index + 1,
                    "png_path": image_path.relative_to(
                        output_dir
                    ).as_posix(),
                    "png_bytes": image_path.stat().st_size,
                    "png_sha256": sha256_file(image_path),
                    "text_characters": len(text.strip()),
                    "ink_ratio": round(ink_ratio, 6),
                    "fonts": fonts,
                }
            )
        sheet_entries = []
        chunk_size = 16
        for chunk_index in range(
            0, len(thumbnails), chunk_size
        ):
            chunk = thumbnails[
                chunk_index : chunk_index + chunk_size
            ]
            cell_width, cell_height = 440, 630
            columns = 4
            rows = (len(chunk) + columns - 1) // columns
            sheet = Image.new(
                "RGB",
                (columns * cell_width, rows * cell_height),
                "white",
            )
            draw = ImageDraw.Draw(sheet)
            for local_index, (page_number, thumb) in enumerate(
                chunk
            ):
                column = local_index % columns
                row = local_index // columns
                x = column * cell_width
                y = row * cell_height
                draw.text(
                    (x + 8, y + 5),
                    f"PDF {pdf_index} page {page_number}",
                    fill="black",
                )
                sheet.paste(thumb, (x + 8, y + 28))
            sheet_path = (
                sheets_root
                / f"pdf_{pdf_index:02d}_sheet_"
                f"{chunk_index // chunk_size + 1:03d}.png"
            )
            sheet.save(sheet_path)
            sheet_entries.append(
                {
                    "path": sheet_path.relative_to(
                        output_dir
                    ).as_posix(),
                    "bytes": sheet_path.stat().st_size,
                    "sha256": sha256_file(sheet_path),
                    "first_page": chunk[0][0],
                    "last_page": chunk[-1][0],
                }
            )
        document.close()
        pdf_entries.append(
            {
                "pdf_index": pdf_index,
                "path": pdf_path.name,
                "bytes": pdf_path.stat().st_size,
                "sha256": sha256_file(pdf_path),
                "page_count": len(page_entries),
                "pages": page_entries,
                "contact_sheets": sheet_entries,
            }
        )
    manifest = {
        "schema_version": 1,
        "replay_date": REPLAY_DATE,
        "inspection_scope": (
            "all_pages_rasterized_complete_contact_sheets"
        ),
        "automated_checks": {
            "blank_pages": "pass",
            "replacement_characters": "pass",
            "font_presence": "pass",
        },
        "manual_contact_sheet_review": "pending_owner_download",
        "pdfs": pdf_entries,
    }
    manifest_path = evidence_root / "visual_manifest.json"
    manifest_path.write_bytes(canonical_json_bytes(manifest))
    return manifest_path


def render_pdfs(args: argparse.Namespace) -> int:
    repo_root = args.repo_root.resolve()
    source_sha = require_sha(args.source_sha, "source_sha")
    require_main_source(repo_root, source_sha)
    checkpoint.restore_checkpoint(
        bundle_dir=args.bundle_dir.resolve(),
        destination_root=repo_root,
        expected_source_sha=source_sha,
        expected_run_id=args.run_id,
        expected_kind="post_validation",
        expected_capture_context="validation_replay",
    )
    apply_checkpoint_deletions(repo_root, source_sha)
    source_state = verify_local_source_state(
        repo_root, source_sha
    )
    output_dir = args.output_dir.resolve()
    checkpoint.assert_isolated_output_path(
        output_dir, args.runner_temp.resolve()
    )
    output_dir.mkdir(parents=True)
    from scripts import generate_chatgpt_side_daily_reports as renderer
    from scripts import run_chatgpt_daily_report_entrypoint as entrypoint

    def validation_resolver(
        candidate_root: Path,
        source_ref: str = "",
        **_kwargs: object,
    ) -> dict[str, Any]:
        if candidate_root.resolve() != repo_root:
            raise ValidationReplayError(
                "renderer attempted a different source root"
            )
        if source_ref != source_state["source_ref"]:
            raise ValidationReplayError(
                "renderer attempted a different source identity"
            )
        return dict(source_state)

    renderer.resolve_daily_report_source_state = validation_resolver
    entrypoint.ensure_local_dfkai_font_for_pdf_rendering()
    old_argv = sys.argv[:]
    old_env = os.environ.copy()
    stdout = io.StringIO()
    try:
        os.environ.update(
            {
                "CHATGPT_DAILY_REPORT_ENTRYPOINT": "1",
                "CHATGPT_DAILY_REPO_ROOT": str(repo_root),
                "CHATGPT_DAILY_OUTPUT_DIR": str(output_dir),
                "CHATGPT_DAILY_SOURCE_REF": str(
                    source_state["source_ref"]
                ),
                "CHATGPT_DAILY_VALIDATION_REPLAY_MAIN_PRICE_DATE": REPLAY_DATE,
                "DAILY_FULL_VALIDATION_ONLY": "1",
            }
        )
        sys.argv = [
            str(repo_root / "scripts/generate_chatgpt_side_daily_reports.py"),
            "--repo-root",
            str(repo_root),
            "--output-dir",
            str(output_dir),
        ]
        with contextlib.redirect_stdout(stdout):
            renderer.main()
    finally:
        sys.argv = old_argv
        os.environ.clear()
        os.environ.update(old_env)
    rendered_stdout = stdout.getvalue()
    print(rendered_stdout.rstrip())
    pdf_paths = [
        Path(line.strip()).resolve()
        for line in rendered_stdout.splitlines()
        if line.strip().lower().endswith(".pdf")
    ]
    if len(pdf_paths) != 6 or any(
        path.parent != output_dir for path in pdf_paths
    ):
        raise ValidationReplayError(
            "renderer must emit exactly six isolated PDFs"
        )
    runtime_manifest_path = entrypoint.write_runtime_manifest(
        output_dir,
        source_state,
        source_state,
        pdf_paths,
        repo_root,
    )
    runtime_manifest = json.loads(
        runtime_manifest_path.read_text(encoding="utf-8")
    )
    runtime_manifest.update(
        {
            "official_entrypoint": (
                "validation_only:scripts/"
                "run_daily_full_validation_replay.py"
            ),
            "official_entrypoint_invoked": False,
            "execution_mode": (
                "validation_only_authoritative_historical_revision"
            ),
            "source_materialization": "verified_checkpoint_overlay",
            "validation_checkpoint_source_sha": source_state[
                "checkpoint_source_sha"
            ],
            "validation_replay_source_sha": source_sha,
            "production_not_run": True,
            "official_pdf_published": False,
            "repo_artifacts_pushed_by_replay": False,
        }
    )
    runtime_manifest_path.write_bytes(
        canonical_json_bytes(runtime_manifest)
    )
    env = base_environment(
        repo_root=repo_root,
        runner_temp=args.runner_temp.resolve(),
        source_sha=source_sha,
    )
    run_command(
        [
            sys.executable,
            "-B",
            "scripts/validate_daily_pdf_completion_hard_gate.py",
            "--require-output-dir",
            str(output_dir),
        ],
        cwd=repo_root,
        env=env,
        label="six-PDF completion hard gate",
    )
    visual_manifest = render_contact_sheets(
        pdf_paths, output_dir
    )
    evidence = {
        "schema_version": 1,
        "replay_date": REPLAY_DATE,
        "source_sha": source_sha,
        "checkpoint_source_sha": source_state["checkpoint_source_sha"],
        "replay_source_sha": source_sha,
        "pdf_count": 6,
        "pdf_source_gate": "pass",
        "pdf_completion_hard_gate": "pass",
        "visual_manifest": {
            "path": visual_manifest.relative_to(
                output_dir
            ).as_posix(),
            "bytes": visual_manifest.stat().st_size,
            "sha256": sha256_file(visual_manifest),
        },
        "production_not_run": True,
        "official_pdf_published": False,
        "repo_artifacts_pushed_by_replay": False,
    }
    (output_dir / "validation_runtime_evidence.json").write_bytes(
        canonical_json_bytes(evidence)
    )
    print(
        json.dumps(
            {
                "status": "six_isolated_pdfs_validated",
                "pdf_count": 6,
                "visual_manifest": str(visual_manifest),
            },
            sort_keys=True,
        )
    )
    return 0


def parser() -> argparse.ArgumentParser:
    result = argparse.ArgumentParser()
    subparsers = result.add_subparsers(
        dest="command", required=True
    )
    common = argparse.ArgumentParser(add_help=False)
    common.add_argument("--repo-root", type=Path, required=True)
    common.add_argument("--runner-temp", type=Path, required=True)
    common.add_argument("--replay-date", required=True)
    common.add_argument("--source-sha", required=True)
    common.add_argument("--run-id", required=True)

    capture = subparsers.add_parser(
        "capture-canary", parents=[common]
    )
    capture.add_argument("--bundle-dir", type=Path, required=True)

    production = subparsers.add_parser(
        "capture-production-checkpoint", parents=[common]
    )
    production.add_argument(
        "--bundle-dir", type=Path, required=True
    )

    replay = subparsers.add_parser(
        "replay", parents=[common]
    )
    replay.add_argument("--bundle-dir", type=Path, required=True)
    replay.add_argument("--checkpoint-run-id", required=True)
    replay.add_argument("--checkpoint-source-sha", required=True)
    replay.add_argument("--checkpoint-artifact-id", required=True)
    replay.add_argument("--checkpoint-artifact-digest", required=True)
    replay.add_argument(
        "--post-bundle-dir", type=Path, required=True
    )

    render = subparsers.add_parser(
        "render-pdfs", parents=[common]
    )
    render.add_argument("--bundle-dir", type=Path, required=True)
    render.add_argument("--output-dir", type=Path, required=True)
    return result


def main(argv: Sequence[str] | None = None) -> int:
    args = parser().parse_args(argv)
    if args.command == "capture-canary":
        return capture_canary(args)
    if args.command == "capture-production-checkpoint":
        return capture_production_checkpoint(args)
    if args.command == "replay":
        return replay_from_checkpoint(args)
    return render_pdfs(args)


if __name__ == "__main__":
    raise SystemExit(main())
