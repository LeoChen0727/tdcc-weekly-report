from __future__ import annotations

import argparse
import csv
import json
import re
import subprocess
import sys
from datetime import datetime
from io import StringIO
from pathlib import Path
from typing import Any

REPO_ROOT = Path(__file__).resolve().parents[1]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from scripts.validate_daily_publish_freshness_gate import (  # noqa: E402
    is_true,
    normalize_date,
    require_current_ready,
    warrant_grace_allows_publish,
)


DEFAULT_SOURCE_REF = "origin/main"
FRESHNESS_PATH = "output/latest/data_freshness_latest.csv"
README_PATH = "output/latest/READ_ME_FIRST_DAILY_REPORT.txt"
PACKET_PATH = "output/latest/chatgpt_daily_report_packet_latest.txt"
MARKET_SESSION_STATUS_PATH = "output/latest/market_session_status_latest.json"

DATE_FIELDS_REQUIRED_TO_MATCH_MAIN = (
    "market_session_date",
    "expected_main_price_date",
    "actual_stock_price_history_date",
    "stock_monitor_price_date",
    "all_candidates_date",
    "official_price_fetch_date",
    "warrant_flow_date",
    "raw_stock_monitor_price_date",
    "raw_all_candidates_date",
    "raw_official_price_fetch_date",
    "raw_warrant_flow_date",
)

README_FIELDS_REQUIRED_TO_MATCH_FRESHNESS = (
    "main_price_date",
    "report_ready",
    "warrant_flow_date",
    "warrant_ready",
    "daily_pdf_ready",
)

README_FIELDS_OPTIONAL_TO_MATCH_FRESHNESS = (
    "warrant_daily_publish_allowed",
    "warrant_pdf_visibility",
)

PACKET_FIELDS_REQUIRED_TO_MATCH_FRESHNESS = {
    "main_price_date": "main_price_date",
    "report_ready": "report_ready",
    "all_candidates_date": "all_candidates_date",
    "official_price_fetch_date": "official_price_fetch_date",
    "stock_monitor_date": "stock_monitor_price_date",
    "warrant_flow_date": "warrant_flow_date",
    "warrant_ready": "warrant_ready",
    "daily_pdf_ready": "daily_pdf_ready",
}

PACKET_FIELDS_OPTIONAL_TO_MATCH_FRESHNESS = {
    "warrant_daily_publish_allowed": "warrant_daily_publish_allowed",
    "warrant_pdf_visibility": "warrant_pdf_visibility",
}

PACKET_REQUIRED_MARKERS = (
    "CHATGPT DAILY REPORT PACKET",
    "CHATGPT_DELIVERY_CONTRACT",
    "official_chatgpt_side_pdf_entrypoint:",
)

STATE_FIELDS_REQUIRED_TO_MATCH_LOCAL = (
    "market_session_status",
    "market_session_date",
    "expected_main_price_date",
    "main_price_date",
    "report_ready",
    "warrant_flow_date",
    "warrant_ready",
    "daily_pdf_ready",
)

STATE_FIELDS_OPTIONAL_TO_MATCH_LOCAL = (
    "warrant_daily_publish_allowed",
    "warrant_pdf_visibility",
)


class DailyReportSourceError(RuntimeError):
    def __init__(self, errors: list[str]):
        super().__init__("daily_report_source_not_ready: " + " | ".join(errors))
        self.errors = errors


def normalize_validation_replay_main_price_date(value: object) -> str:
    text = str(value or "").strip()
    if not text:
        return ""
    if not re.fullmatch(r"\d{8}", text):
        raise DailyReportSourceError(
            [
                "validation replay date must use exact YYYYMMDD format: "
                f"validation_replay_main_price_date={text!r}"
            ]
        )
    try:
        datetime.strptime(text, "%Y%m%d")
    except ValueError as exc:
        raise DailyReportSourceError(
            [
                "validation replay date is not a valid calendar date: "
                f"validation_replay_main_price_date={text!r}"
            ]
        ) from exc
    return text


def run_git(repo_root: Path, *args: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        ["git", "-C", str(repo_root), *args],
        check=False,
        capture_output=True,
        encoding="utf-8",
        errors="replace",
        text=True,
    )


def require_git_success(proc: subprocess.CompletedProcess[str], action: str) -> str:
    if proc.returncode != 0:
        detail = (proc.stderr or proc.stdout or f"{action} failed").strip()
        raise DailyReportSourceError([f"{action} failed: {detail}"])
    return proc.stdout


def fetch_source_ref(repo_root: Path, source_ref: str) -> None:
    pieces = source_ref.split("/", 1)
    if len(pieces) != 2 or not pieces[0] or not pieces[1]:
        raise DailyReportSourceError(
            [f"source_ref must be a remote tracking ref like origin/main, got {source_ref!r}"]
        )
    remote, branch = pieces
    proc = run_git(repo_root, "fetch", remote, branch)
    require_git_success(proc, f"git fetch {remote} {branch}")


def git_show_text(repo_root: Path, source_ref: str, repo_path: str) -> str:
    proc = run_git(repo_root, "show", f"{source_ref}:{repo_path}")
    return require_git_success(proc, f"git show {source_ref}:{repo_path}")


def git_rev_parse(repo_root: Path, ref: str) -> str:
    proc = run_git(repo_root, "rev-parse", ref)
    return require_git_success(proc, f"git rev-parse {ref}").strip()


def forbid_helper_source(repo_root: Path) -> None:
    parts = {part.lower() for part in repo_root.resolve().parts}
    if "onedrive" in parts:
        raise DailyReportSourceError(
            [
                "official daily report source must not be a OneDrive/helper checkout; "
                f"use the fixed Documents/Codex worktree instead: {repo_root}"
            ]
        )


def require_clean_git_checkout(repo_root: Path, allow_dirty: bool) -> list[str]:
    head = run_git(repo_root, "rev-parse", "HEAD")
    if head.returncode != 0:
        return [f"not a git checkout or HEAD is unreadable: {(head.stderr or head.stdout).strip()}"]

    status = run_git(repo_root, "status", "--porcelain")
    if status.returncode != 0:
        return [(status.stderr or status.stdout or "git status failed").strip()]

    dirty_lines = [line for line in status.stdout.splitlines() if line.strip()]
    if dirty_lines and not allow_dirty:
        sample = "; ".join(dirty_lines[:8])
        if len(dirty_lines) > 8:
            sample += f"; ... ({len(dirty_lines)} total)"
        return [
            "local checkout is dirty; official ChatGPT-side daily PDF generation requires a clean "
            f"worktree before the run starts: {sample}"
        ]
    return []


def parse_key_value_text(text: str) -> dict[str, str]:
    fields: dict[str, str] = {}
    for raw_line in text.splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#") or line.startswith("|"):
            continue
        if "=" in line:
            key, value = line.split("=", 1)
        elif ":" in line and re.match(r"^-?\s*[A-Za-z0-9_ -]+:\s*", line):
            key, value = line.lstrip("- ").split(":", 1)
        else:
            continue
        fields[key.strip().lstrip("\ufeff")] = value.strip()
    return fields


def parse_freshness_text(text: str, source_label: str) -> dict[str, str]:
    rows = list(csv.DictReader(StringIO(text)))
    if len(rows) != 1:
        raise DailyReportSourceError([f"{source_label} must contain exactly one row, got {len(rows)}"])
    return {str(key).lstrip("\ufeff"): str(value or "") for key, value in rows[0].items()}


def validate_freshness_row(row: dict[str, str], source_label: str) -> list[str]:
    errors = [f"{source_label}: {error}" for error in require_current_ready(row)]

    main_date = normalize_date(row.get("main_price_date", ""))
    for field in DATE_FIELDS_REQUIRED_TO_MATCH_MAIN:
        value = normalize_date(row.get(field, ""))
        if not value:
            errors.append(f"{source_label}: {field} is missing")
        elif main_date and value != main_date:
            errors.append(f"{source_label}: {field}={value} does not match main_price_date={main_date}")

    if not is_true(row.get("report_ready", "")):
        errors.append(f"{source_label}: report_ready must be True, got {row.get('report_ready', '')!r}")
    if not is_true(row.get("warrant_ready", "")) and not warrant_grace_allows_publish(row):
        errors.append(
            f"{source_label}: warrant_ready must be True or bounded warrant_unavailable grace must hide "
            f"warrant effects, got {row.get('warrant_ready', '')!r}"
        )
    if not is_true(row.get("daily_pdf_ready", "")):
        errors.append(f"{source_label}: daily_pdf_ready must be True, got {row.get('daily_pdf_ready', '')!r}")

    return errors


def validate_market_session_status(
    status: dict[str, Any],
    freshness_row: dict[str, str],
    source_label: str,
    validation_replay_main_price_date: str = "",
) -> list[str]:
    errors: list[str] = []
    market_status = str(status.get("market_status") or "").strip()
    phase = str(status.get("phase") or "").strip()
    session_date = normalize_date(status.get("market_session_date", ""))
    expected_date = normalize_date(status.get("expected_main_price_date", ""))
    main_date = normalize_date(freshness_row.get("main_price_date", ""))
    replay_date = normalize_date(validation_replay_main_price_date)
    closed_validation_replay = bool(replay_date) and market_status == "closed_scheduled"

    if replay_date and main_date != replay_date:
        errors.append(
            f"{source_label}: validation_replay_main_price_date={replay_date} "
            f"does not match main_price_date={main_date or '<missing>'}"
        )

    if closed_validation_replay:
        if phase != "preflight":
            errors.append(
                f"{source_label}: closed-market validation replay phase must be preflight, "
                f"got {phase or '<missing>'}"
            )
        if expected_date != replay_date:
            errors.append(
                f"{source_label}: closed-market expected_main_price_date="
                f"{expected_date or '<missing>'} does not match "
                f"validation_replay_main_price_date={replay_date}"
            )
        if not session_date:
            errors.append(f"{source_label}: market_session_date is missing")
        elif session_date < replay_date:
            errors.append(
                f"{source_label}: closed-market market_session_date={session_date} "
                f"precedes validation_replay_main_price_date={replay_date}"
            )
        if status.get("should_run_daily_pipeline") is not False:
            errors.append(
                f"{source_label}: closed-market validation replay requires "
                "should_run_daily_pipeline=false"
            )
        if not str(status.get("reason_code") or "").strip():
            errors.append(
                f"{source_label}: closed-market validation replay reason_code is missing"
            )
        return errors

    if market_status != "open_confirmed":
        errors.append(
            f"{source_label}: market_status must be open_confirmed, got {market_status or '<missing>'}"
        )
    if phase != "confirm":
        errors.append(f"{source_label}: phase must be confirm, got {phase or '<missing>'}")
    if not expected_date:
        errors.append(f"{source_label}: expected_main_price_date is missing")
    elif main_date and expected_date != main_date:
        errors.append(
            f"{source_label}: expected_main_price_date={expected_date} "
            f"does not match main_price_date={main_date}"
        )
    if not session_date:
        errors.append(f"{source_label}: market_session_date is missing")
    elif expected_date and session_date != expected_date:
        errors.append(
            f"{source_label}: market_session_date={session_date} "
            f"does not match expected_main_price_date={expected_date}"
        )
    if status.get("should_run_daily_pipeline") is not True:
        errors.append(f"{source_label}: should_run_daily_pipeline must be true")
    return errors


def validate_local_market_session_matches_origin(
    repo_root: Path,
    origin_status: dict[str, Any],
) -> list[str]:
    path = repo_root / MARKET_SESSION_STATUS_PATH
    if not path.exists():
        return [f"local {MARKET_SESSION_STATUS_PATH} is missing; cannot mirror {DEFAULT_SOURCE_REF}"]
    try:
        local_status = json.loads(path.read_text(encoding="utf-8-sig"))
    except Exception as exc:
        return [f"local {MARKET_SESSION_STATUS_PATH} is unreadable: {exc}"]
    errors: list[str] = []
    for field in (
        "phase",
        "market_status",
        "market_session_date",
        "expected_main_price_date",
        "reason_code",
        "should_run_daily_pipeline",
    ):
        if local_status.get(field) != origin_status.get(field):
            errors.append(
                f"local market session {field}={local_status.get(field)!r} does not match "
                f"{DEFAULT_SOURCE_REF} {field}={origin_status.get(field)!r}"
            )
    return errors


def validate_readme_matches_freshness(
    readme_fields: dict[str, str],
    freshness_row: dict[str, str],
    source_label: str,
) -> list[str]:
    errors: list[str] = []
    fields = list(README_FIELDS_REQUIRED_TO_MATCH_FRESHNESS)
    fields.extend(field for field in README_FIELDS_OPTIONAL_TO_MATCH_FRESHNESS if str(freshness_row.get(field, "")).strip())
    for field in fields:
        readme_value = readme_fields.get(field, "")
        freshness_value = freshness_row.get(field, "")
        if field.endswith("_date"):
            if normalize_date(readme_value) != normalize_date(freshness_value):
                errors.append(
                    f"{source_label}: README {field}={readme_value or '<missing>'} does not match "
                    f"freshness {field}={freshness_value or '<missing>'}"
                )
        elif str(readme_value).strip() != str(freshness_value).strip():
            errors.append(
                f"{source_label}: README {field}={readme_value or '<missing>'} does not match "
                f"freshness {field}={freshness_value or '<missing>'}"
            )
    return errors


def validate_packet_matches_freshness(
    packet_text: str,
    packet_fields: dict[str, str],
    freshness_row: dict[str, str],
    source_label: str,
) -> list[str]:
    errors: list[str] = []
    for marker in PACKET_REQUIRED_MARKERS:
        if marker not in packet_text:
            errors.append(f"{source_label}: packet missing required marker {marker!r}")

    field_map = dict(PACKET_FIELDS_REQUIRED_TO_MATCH_FRESHNESS)
    field_map.update(
        {
            packet_field: freshness_field
            for packet_field, freshness_field in PACKET_FIELDS_OPTIONAL_TO_MATCH_FRESHNESS.items()
            if str(freshness_row.get(freshness_field, "")).strip()
        }
    )
    for packet_field, freshness_field in field_map.items():
        packet_value = packet_fields.get(packet_field, "")
        freshness_value = freshness_row.get(freshness_field, "")
        if packet_field.endswith("_date") or freshness_field.endswith("_date"):
            if normalize_date(packet_value) != normalize_date(freshness_value):
                errors.append(
                    f"{source_label}: packet {packet_field}={packet_value or '<missing>'} does not match "
                    f"freshness {freshness_field}={freshness_value or '<missing>'}"
                )
        elif str(packet_value).strip() != str(freshness_value).strip():
            errors.append(
                f"{source_label}: packet {packet_field}={packet_value or '<missing>'} does not match "
                f"freshness {freshness_field}={freshness_value or '<missing>'}"
            )
    return errors


def validate_local_matches_origin(
    repo_root: Path,
    origin_freshness: dict[str, str],
    origin_readme: dict[str, str],
    origin_packet: dict[str, str],
) -> list[str]:
    errors: list[str] = []
    local_freshness_path = repo_root / FRESHNESS_PATH
    local_readme_path = repo_root / README_PATH
    local_packet_path = repo_root / PACKET_PATH

    if not local_freshness_path.exists():
        return [f"local {FRESHNESS_PATH} is missing; cannot mirror {DEFAULT_SOURCE_REF}"]
    if not local_readme_path.exists():
        return [f"local {README_PATH} is missing; cannot mirror {DEFAULT_SOURCE_REF}"]
    if not local_packet_path.exists():
        return [f"local {PACKET_PATH} is missing; cannot mirror {DEFAULT_SOURCE_REF}"]

    try:
        local_freshness = parse_freshness_text(
            local_freshness_path.read_text(encoding="utf-8", errors="replace"),
            f"local {FRESHNESS_PATH}",
        )
    except Exception as exc:
        return [f"local {FRESHNESS_PATH} is unreadable: {exc}"]

    local_readme = parse_key_value_text(local_readme_path.read_text(encoding="utf-8", errors="replace"))
    local_packet = parse_key_value_text(local_packet_path.read_text(encoding="utf-8", errors="replace"))

    fields = list(STATE_FIELDS_REQUIRED_TO_MATCH_LOCAL)
    fields.extend(
        field
        for field in STATE_FIELDS_OPTIONAL_TO_MATCH_LOCAL
        if str(origin_freshness.get(field, origin_readme.get(field, origin_packet.get(field, "")))).strip()
    )
    for field in fields:
        origin_value = origin_freshness.get(field, origin_readme.get(field, origin_packet.get(field, "")))
        local_value = local_freshness.get(field, local_readme.get(field, local_packet.get(field, "")))
        if field.endswith("_date"):
            if normalize_date(local_value) != normalize_date(origin_value):
                errors.append(
                    f"local {field}={local_value or '<missing>'} does not match "
                    f"{DEFAULT_SOURCE_REF} {field}={origin_value or '<missing>'}"
                )
        elif str(local_value).strip() != str(origin_value).strip():
            errors.append(
                f"local {field}={local_value or '<missing>'} does not match "
                f"{DEFAULT_SOURCE_REF} {field}={origin_value or '<missing>'}"
            )

    return errors


def resolve_daily_report_source_state(
    repo_root: Path,
    source_ref: str = DEFAULT_SOURCE_REF,
    fetch: bool = True,
    require_git_clean: bool = True,
    allow_dirty: bool = False,
    require_local_match: bool = True,
    validation_replay_main_price_date: str = "",
) -> dict[str, Any]:
    repo_root = repo_root.expanduser().resolve()
    forbid_helper_source(repo_root)
    validation_replay_date = normalize_validation_replay_main_price_date(
        validation_replay_main_price_date
    )

    clean_errors = require_clean_git_checkout(repo_root, allow_dirty=allow_dirty) if require_git_clean else []
    if clean_errors:
        raise DailyReportSourceError(clean_errors)

    if fetch:
        fetch_source_ref(repo_root, source_ref)

    source_commit = git_rev_parse(repo_root, source_ref)
    freshness_text = git_show_text(repo_root, source_ref, FRESHNESS_PATH)
    readme_text = git_show_text(repo_root, source_ref, README_PATH)
    packet_text = git_show_text(repo_root, source_ref, PACKET_PATH)
    market_session_text = git_show_text(repo_root, source_ref, MARKET_SESSION_STATUS_PATH)

    freshness_row = parse_freshness_text(freshness_text, f"{source_ref}:{FRESHNESS_PATH}")
    readme_fields = parse_key_value_text(readme_text)
    packet_fields = parse_key_value_text(packet_text)
    try:
        market_session_status = json.loads(market_session_text)
    except Exception as exc:
        raise DailyReportSourceError(
            [f"{source_ref}:{MARKET_SESSION_STATUS_PATH} is unreadable: {exc}"]
        ) from exc
    if not isinstance(market_session_status, dict):
        raise DailyReportSourceError(
            [f"{source_ref}:{MARKET_SESSION_STATUS_PATH} must contain a JSON object"]
        )

    errors: list[str] = []
    errors.extend(validate_freshness_row(freshness_row, f"{source_ref}:{FRESHNESS_PATH}"))
    errors.extend(validate_readme_matches_freshness(readme_fields, freshness_row, f"{source_ref}:{README_PATH}"))
    errors.extend(validate_packet_matches_freshness(packet_text, packet_fields, freshness_row, f"{source_ref}:{PACKET_PATH}"))
    errors.extend(
        validate_market_session_status(
            market_session_status,
            freshness_row,
            f"{source_ref}:{MARKET_SESSION_STATUS_PATH}",
            validation_replay_date,
        )
    )
    if require_local_match:
        errors.extend(validate_local_matches_origin(repo_root, freshness_row, readme_fields, packet_fields))
        errors.extend(validate_local_market_session_matches_origin(repo_root, market_session_status))

    if errors:
        raise DailyReportSourceError(errors)

    main_price_date = normalize_date(freshness_row.get("main_price_date", ""))
    warrant_ready = is_true(freshness_row.get("warrant_ready", ""))
    warrant_daily_publish_allowed = is_true(freshness_row.get("warrant_daily_publish_allowed", "")) or warrant_ready
    warrant_pdf_visibility = freshness_row.get("warrant_pdf_visibility", "").strip()
    if not warrant_pdf_visibility and warrant_ready:
        warrant_pdf_visibility = "visible"
    warrant_source_status = freshness_row.get("warrant_source_status", "").strip()
    if not warrant_source_status and warrant_ready:
        warrant_source_status = "ok"
    return {
        "source": source_ref,
        "source_ref": source_ref,
        "source_commit_sha": source_commit,
        "freshness_path": f"{source_ref}:{FRESHNESS_PATH}",
        "readme_path": f"{source_ref}:{README_PATH}",
        "packet_path": f"{source_ref}:{PACKET_PATH}",
        "market_session_status_path": f"{source_ref}:{MARKET_SESSION_STATUS_PATH}",
        "market_session_status": str(market_session_status.get("market_status") or ""),
        "market_session_date": normalize_date(market_session_status.get("market_session_date", "")),
        "expected_main_price_date": normalize_date(
            market_session_status.get("expected_main_price_date", "")
        ),
        "main_price_date": main_price_date,
        "report_ready": is_true(freshness_row.get("report_ready", "")),
        "warrant_ready": warrant_ready,
        "warrant_daily_publish_allowed": warrant_daily_publish_allowed,
        "warrant_pdf_visibility": warrant_pdf_visibility,
        "warrant_source_status": warrant_source_status,
        "daily_pdf_ready": is_true(freshness_row.get("daily_pdf_ready", "")),
        "allow_report_generation": True,
        "freshness_fields": freshness_row,
        "readme_fields": readme_fields,
        "packet_fields": packet_fields,
        "market_session_fields": market_session_status,
        "validation_replay_main_price_date": validation_replay_date,
    }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Resolve the only allowed official daily ChatGPT-side report source from origin/main. "
            "This gate uses git fetch + git show, not wall-clock dates, OneDrive helpers, raw URLs, or Pages."
        )
    )
    parser.add_argument("--repo-root", type=Path, default=Path("."))
    parser.add_argument("--source-ref", default=DEFAULT_SOURCE_REF)
    parser.add_argument("--no-fetch", action="store_true", help="Skip git fetch; tests and offline diagnostics only.")
    parser.add_argument(
        "--allow-dirty",
        action="store_true",
        help="Allow a dirty local checkout for diagnostics only. Official PDF generation must not use this.",
    )
    parser.add_argument(
        "--skip-local-match",
        action="store_true",
        help="Do not require local output/latest files to match origin/main. Diagnostics only.",
    )
    parser.add_argument("--json", action="store_true", help="Print the full resolved state as JSON.")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    try:
        state = resolve_daily_report_source_state(
            repo_root=args.repo_root,
            source_ref=args.source_ref,
            fetch=not args.no_fetch,
            require_git_clean=True,
            allow_dirty=args.allow_dirty,
            require_local_match=not args.skip_local_match,
        )
    except DailyReportSourceError as exc:
        for error in exc.errors:
            print(f"ERROR: {error}")
        return 1

    if args.json:
        print(json.dumps(state, ensure_ascii=True, indent=2, sort_keys=True))
    else:
        print(
            "daily report source resolver passed: "
            f"source_ref={state['source_ref']} "
            f"source_commit_sha={state['source_commit_sha']} "
            f"main_price_date={state['main_price_date']} "
            f"report_ready={state['report_ready']} "
            f"warrant_ready={state['warrant_ready']} "
            f"daily_pdf_ready={state['daily_pdf_ready']}"
        )
    return 0


if __name__ == "__main__":
    sys.exit(main())
