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
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Iterable, Sequence


ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

import scripts.daily_full_validation_replay_checkpoint as checkpoint  # noqa: E402


REPLAY_DATE = "20260807"
OLD_FAILED_RUN_ID = "31174813266"
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
REQUIRED_MODEL_SIGNAL_COLUMNS = (
    "base_model_score",
    "operation_score",
    "tdcc_score",
    "pattern_score",
    "risk_penalty",
    "final_rank_score",
    "rank_reason_zh",
)
ALL_CANDIDATES_PATH = Path("output/latest/all_candidates_latest.csv")
WARRANT_FLOW_PATH = Path("output/latest/warrant_flow_latest.csv")
THEME_STOCK_PATH = Path(
    "output/latest/volume_attack_theme_stocks_latest.csv"
)
FRESHNESS_PATH = Path("output/latest/data_freshness_latest.csv")
MARKET_SESSION_PATH = Path(
    "output/latest/market_session_status_latest.json"
)
README_PATH = Path("output/latest/READ_ME_FIRST_DAILY_REPORT.txt")
PACKET_PATH = Path(
    "output/latest/chatgpt_daily_report_packet_latest.md"
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
SOURCE_REVISION_FILENAME = "source_revision_manifest.json"
ALLOWED_CHECKPOINT_PREFIXES = ("data", "output", "docs")
REGRESSION_STOCK_IDS = ("7711", "2059")


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


def run_authoritative_historical_revision(
    *,
    repo_root: Path,
    runner_temp: Path,
    env: dict[str, str],
    run_id: str,
    source_sha: str,
) -> tuple[dict[str, Any], Path]:
    plan_path = runner_temp / "historical_replay_plan.json"
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
    plan = json.loads(plan_path.read_text(encoding="utf-8"))
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
    run_command(
        command,
        cwd=repo_root,
        env=env,
        label="authoritative historical source replay",
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
    return plan, manifest_path


def run_named_steps(
    *,
    repo_root: Path,
    env: dict[str, str],
    names: Iterable[str],
    post_mode: bool,
) -> list[dict[str, str]]:
    commands = step_map(repo_root)
    results: list[dict[str, str]] = []
    for name in names:
        if name not in commands:
            raise ValidationReplayError(
                f"production workflow step is missing: {name}"
            )
        script = commands[name]
        if post_mode:
            script = remove_mutable_post_commands(script)
        started = datetime.now(timezone.utc).isoformat()
        run_bash_block(
            script,
            cwd=repo_root,
            env=env,
            label=f"production step replay: {name}",
        )
        apply_github_environment(env)
        results.append(
            {
                "step": name,
                "status": "pass",
                "started_at_utc": started,
                "completed_at_utc": datetime.now(
                    timezone.utc
                ).isoformat(),
            }
        )
        if name == POST_START_STEP:
            validate_candidate_scoped_warrant_projection(repo_root)
        if name == "Build daily candidate model layer":
            validate_model_signal_schema(repo_root)
    return results


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


def validate_model_signal_schema(repo_root: Path) -> dict[str, Any]:
    columns, rows = read_csv_rows(repo_root / MODEL_SIGNAL_PATH)
    missing = [
        field
        for field in REQUIRED_MODEL_SIGNAL_COLUMNS
        if field not in columns
    ]
    if missing:
        raise ValidationReplayError(
            f"daily model signal schema missing columns: {missing}"
        )
    return {
        "path": MODEL_SIGNAL_PATH.as_posix(),
        "sha256": sha256_file(repo_root / MODEL_SIGNAL_PATH),
        "rows": len(rows),
        "required_columns": list(REQUIRED_MODEL_SIGNAL_COLUMNS),
    }


def stock_ids(rows: Iterable[dict[str, str]]) -> set[str]:
    return {
        str(row.get("stock_id") or "").strip()
        for row in rows
        if str(row.get("stock_id") or "").strip()
    }


def validate_candidate_scoped_warrant_projection(
    repo_root: Path,
) -> dict[str, Any]:
    _candidate_columns, candidate_rows = read_csv_rows(
        repo_root / ALL_CANDIDATES_PATH
    )
    _warrant_columns, warrant_rows = read_csv_rows(
        repo_root / WARRANT_FLOW_PATH
    )
    _theme_columns, theme_rows = read_csv_rows(
        repo_root / THEME_STOCK_PATH
    )
    candidate_ids = stock_ids(candidate_rows)
    warrant_by_id = {
        str(row.get("stock_id") or "").strip(): row
        for row in warrant_rows
        if str(row.get("stock_id") or "").strip()
    }
    projected_ids = {
        stock_id
        for stock_id in stock_ids(theme_rows)
        if stock_id in warrant_by_id
        and str(
            warrant_by_id[stock_id].get("warrant_flow_signal") or ""
        ).strip()
    }
    leaked = sorted(projected_ids - candidate_ids)
    if leaked:
        raise ValidationReplayError(
            "official warrant projection escaped canonical "
            f"all_candidates: {leaked[:20]}"
        )
    regressions = {
        stock_id: {
            "in_all_candidates": stock_id in candidate_ids,
            "in_official_warrant": stock_id in warrant_by_id,
            "in_theme_output": stock_id in stock_ids(theme_rows),
            "projection_contract_pass": (
                stock_id not in projected_ids
                or stock_id in candidate_ids
            ),
        }
        for stock_id in REGRESSION_STOCK_IDS
    }
    missing_regression_sources = [
        stock_id
        for stock_id in REGRESSION_STOCK_IDS
        if stock_id not in warrant_by_id
    ]
    if missing_regression_sources:
        raise ValidationReplayError(
            "authoritative 20260807 warrant revision does not contain "
            f"required regression stock ids: {missing_regression_sources}"
        )
    if not all(
        row["projection_contract_pass"]
        for row in regressions.values()
    ):
        raise ValidationReplayError(
            "7711/2059 warrant projection regression failed"
        )
    return {
        "all_candidates_sha256": sha256_file(
            repo_root / ALL_CANDIDATES_PATH
        ),
        "official_warrant_sha256": sha256_file(
            repo_root / WARRANT_FLOW_PATH
        ),
        "theme_stock_sha256": sha256_file(
            repo_root / THEME_STOCK_PATH
        ),
        "candidate_count": len(candidate_ids),
        "projected_count": len(projected_ids),
        "leaked_ids": leaked,
        "regressions": regressions,
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
) -> dict[str, Any]:
    source_revision_path = runner_temp / SOURCE_REVISION_FILENAME
    _revision, required = create_source_revision_manifest(
        repo_root=repo_root,
        output_path=source_revision_path,
        source_sha=source_sha,
        revision_kind=revision_kind,
        structured_manifest_path=structured_manifest_path,
    )
    paths = checkpoint_paths(repo_root, required)
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


def require_freshness_contract(
    repo_root: Path, source_sha: str
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
        "readme_fields": {},
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


def write_validation_source_state(
    repo_root: Path, source_sha: str
) -> dict[str, Any]:
    state = require_freshness_contract(repo_root, source_sha)
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
        "source_sha": source_sha,
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


def replay_from_checkpoint(args: argparse.Namespace) -> int:
    repo_root = args.repo_root.resolve()
    runner_temp = args.runner_temp.resolve()
    runner_temp.mkdir(parents=True, exist_ok=True)
    source_sha = require_sha(args.source_sha, "source_sha")
    require_exact_date(args.replay_date, "replay_date")
    require_main_source(repo_root, source_sha)
    checkpoint.restore_checkpoint(
        bundle_dir=args.bundle_dir.resolve(),
        destination_root=repo_root,
        expected_source_sha=source_sha,
        expected_run_id=args.checkpoint_run_id,
        expected_kind="pre_step41",
        expected_capture_context="validation_canary",
    )
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
    env["MARKET_STATUS"] = str(
        market.get("market_status") or ""
    )
    env["MARKET_SESSION_DATE"] = str(
        market.get("market_session_date") or REPLAY_DATE
    )
    names = post_step_names(repo_root)
    steps = run_named_steps(
        repo_root=repo_root,
        env=env,
        names=names,
        post_mode=True,
    )
    model_evidence = validate_model_signal_schema(repo_root)
    warrant_evidence = validate_candidate_scoped_warrant_projection(
        repo_root
    )
    source_state = write_validation_source_state(
        repo_root, source_sha
    )
    parity = {
        "schema_version": 1,
        "replay_date": REPLAY_DATE,
        "source_sha": source_sha,
        "checkpoint_run_id": args.checkpoint_run_id,
        "original_failure_step": POST_START_STEP,
        "original_failure_stock_id": "2059",
        "model_signal_schema": model_evidence,
        "candidate_scoped_warrant_projection": warrant_evidence,
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
                "steps": steps,
            }
        )
    )
    structured_paths = sorted(
        repo_root.glob(
            "output/history/historical_source_replay/*/"
            f"{REPLAY_DATE}/structured_source_manifest.json"
        ),
        key=lambda path: path.stat().st_mtime_ns,
    )
    if not structured_paths:
        raise ValidationReplayError(
            "restored historical source manifest is missing"
        )
    manifest = capture_checkpoint(
        repo_root=repo_root,
        bundle_dir=args.post_bundle_dir.resolve(),
        runner_temp=runner_temp,
        source_sha=source_sha,
        run_id=args.run_id,
        structured_manifest_path=structured_paths[-1],
        revision_kind="authoritative_historical_revision",
        checkpoint_kind="post_validation",
        capture_context="validation_replay",
        producer_steps=[row["step"] for row in steps],
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
    if (
        payload.get("replay_date") != REPLAY_DATE
        or payload.get("source_sha") != source_sha
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
            "validation_checkpoint_source_sha": source_sha,
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
