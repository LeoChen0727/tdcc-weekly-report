from __future__ import annotations

import argparse
import csv
import json
import subprocess
import sys
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
)


DEFAULT_SOURCE_REF = "origin/main"
FRESHNESS_PATH = "output/latest/data_freshness_latest.csv"
README_PATH = "output/latest/READ_ME_FIRST_DAILY_REPORT.txt"

DATE_FIELDS_REQUIRED_TO_MATCH_MAIN = (
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

STATE_FIELDS_REQUIRED_TO_MATCH_LOCAL = (
    "main_price_date",
    "report_ready",
    "warrant_flow_date",
    "warrant_ready",
    "daily_pdf_ready",
)


class DailyReportSourceError(RuntimeError):
    def __init__(self, errors: list[str]):
        super().__init__("daily_report_source_not_ready: " + " | ".join(errors))
        self.errors = errors


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
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
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

    for field in ("report_ready", "warrant_ready", "daily_pdf_ready"):
        if not is_true(row.get(field, "")):
            errors.append(f"{source_label}: {field} must be True, got {row.get(field, '')!r}")

    return errors


def validate_readme_matches_freshness(
    readme_fields: dict[str, str],
    freshness_row: dict[str, str],
    source_label: str,
) -> list[str]:
    errors: list[str] = []
    for field in README_FIELDS_REQUIRED_TO_MATCH_FRESHNESS:
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


def validate_local_matches_origin(
    repo_root: Path,
    origin_freshness: dict[str, str],
    origin_readme: dict[str, str],
) -> list[str]:
    errors: list[str] = []
    local_freshness_path = repo_root / FRESHNESS_PATH
    local_readme_path = repo_root / README_PATH

    if not local_freshness_path.exists():
        return [f"local {FRESHNESS_PATH} is missing; cannot mirror {DEFAULT_SOURCE_REF}"]
    if not local_readme_path.exists():
        return [f"local {README_PATH} is missing; cannot mirror {DEFAULT_SOURCE_REF}"]

    try:
        local_freshness = parse_freshness_text(
            local_freshness_path.read_text(encoding="utf-8", errors="replace"),
            f"local {FRESHNESS_PATH}",
        )
    except Exception as exc:
        return [f"local {FRESHNESS_PATH} is unreadable: {exc}"]

    local_readme = parse_key_value_text(local_readme_path.read_text(encoding="utf-8", errors="replace"))

    for field in STATE_FIELDS_REQUIRED_TO_MATCH_LOCAL:
        origin_value = origin_freshness.get(field, origin_readme.get(field, ""))
        local_value = local_freshness.get(field, local_readme.get(field, ""))
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
) -> dict[str, Any]:
    repo_root = repo_root.expanduser().resolve()
    forbid_helper_source(repo_root)

    clean_errors = require_clean_git_checkout(repo_root, allow_dirty=allow_dirty) if require_git_clean else []
    if clean_errors:
        raise DailyReportSourceError(clean_errors)

    if fetch:
        fetch_source_ref(repo_root, source_ref)

    source_commit = git_rev_parse(repo_root, source_ref)
    freshness_text = git_show_text(repo_root, source_ref, FRESHNESS_PATH)
    readme_text = git_show_text(repo_root, source_ref, README_PATH)

    freshness_row = parse_freshness_text(freshness_text, f"{source_ref}:{FRESHNESS_PATH}")
    readme_fields = parse_key_value_text(readme_text)

    errors: list[str] = []
    errors.extend(validate_freshness_row(freshness_row, f"{source_ref}:{FRESHNESS_PATH}"))
    errors.extend(validate_readme_matches_freshness(readme_fields, freshness_row, f"{source_ref}:{README_PATH}"))
    if require_local_match:
        errors.extend(validate_local_matches_origin(repo_root, freshness_row, readme_fields))

    if errors:
        raise DailyReportSourceError(errors)

    main_price_date = normalize_date(freshness_row.get("main_price_date", ""))
    return {
        "source": source_ref,
        "source_ref": source_ref,
        "source_commit_sha": source_commit,
        "freshness_path": f"{source_ref}:{FRESHNESS_PATH}",
        "readme_path": f"{source_ref}:{README_PATH}",
        "main_price_date": main_price_date,
        "report_ready": is_true(freshness_row.get("report_ready", "")),
        "warrant_ready": is_true(freshness_row.get("warrant_ready", "")),
        "daily_pdf_ready": is_true(freshness_row.get("daily_pdf_ready", "")),
        "allow_report_generation": True,
        "freshness_fields": freshness_row,
        "readme_fields": readme_fields,
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
