from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from scripts.validate_daily_publish_freshness_gate import (  # noqa: E402
    is_true,
    normalize_date,
    read_one_row,
    require_current_ready,
    warrant_grace_allows_publish,
)


DEFAULT_FRESHNESS = Path("output/latest/data_freshness_latest.csv")
DEFAULT_README = Path("output/latest/READ_ME_FIRST_DAILY_REPORT.txt")

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

README_FIELDS_OPTIONAL_TO_MATCH_FRESHNESS = (
    "warrant_daily_publish_allowed",
    "warrant_pdf_visibility",
)


def parse_key_value_file(path: Path) -> dict[str, str]:
    fields: dict[str, str] = {}
    for raw_line in path.read_text(encoding="utf-8", errors="replace").splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        fields[key.strip()] = value.strip()
    return fields


def run_git(repo_root: Path, *args: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        ["git", "-C", str(repo_root), *args],
        check=False,
        capture_output=True,
        text=True,
    )


def current_git_head(repo_root: Path) -> tuple[str | None, str | None]:
    proc = run_git(repo_root, "rev-parse", "HEAD")
    if proc.returncode != 0:
        return None, (proc.stderr or proc.stdout or "git rev-parse HEAD failed").strip()
    return proc.stdout.strip(), None


def require_clean_git_checkout(repo_root: Path, allow_dirty: bool) -> list[str]:
    errors: list[str] = []

    head, head_error = current_git_head(repo_root)
    if head_error:
        return [f"not a git checkout or HEAD is unreadable: {head_error}"]
    if not head:
        return ["git HEAD is empty"]

    status = run_git(repo_root, "status", "--porcelain")
    if status.returncode != 0:
        errors.append((status.stderr or status.stdout or "git status failed").strip())
        return errors

    dirty_lines = [line for line in status.stdout.splitlines() if line.strip()]
    if dirty_lines and not allow_dirty:
        sample = "; ".join(dirty_lines[:8])
        if len(dirty_lines) > 8:
            sample += f"; ... ({len(dirty_lines)} total)"
        errors.append(
            "local checkout is dirty; use a clean clone/worktree/archive before official PDF generation "
            f"or rerun with --allow-dirty for diagnostics only: {sample}"
        )

    return errors


def validate_freshness_row(row: dict[str, str], expected_date: str | None) -> list[str]:
    errors = require_current_ready(row)

    main_date = normalize_date(row.get("main_price_date", ""))
    if expected_date and main_date != expected_date:
        errors.append(f"main_price_date={main_date or '<missing>'} does not match expected date {expected_date}")

    for field in DATE_FIELDS_REQUIRED_TO_MATCH_MAIN:
        value = normalize_date(row.get(field, ""))
        if not value:
            errors.append(f"{field} is missing")
        elif main_date and value != main_date:
            errors.append(f"{field}={value} does not match main_price_date={main_date}")

    return errors


def validate_readme_matches_freshness(readme_fields: dict[str, str], freshness_row: dict[str, str]) -> list[str]:
    errors: list[str] = []

    fields = list(README_FIELDS_REQUIRED_TO_MATCH_FRESHNESS)
    fields.extend(field for field in README_FIELDS_OPTIONAL_TO_MATCH_FRESHNESS if str(freshness_row.get(field, "")).strip())
    for field in fields:
        readme_value = readme_fields.get(field, "")
        freshness_value = freshness_row.get(field, "")
        if field.endswith("_date"):
            if normalize_date(readme_value) != normalize_date(freshness_value):
                errors.append(
                    f"README {field}={readme_value or '<missing>'} does not match freshness "
                    f"{field}={freshness_value or '<missing>'}"
                )
        elif str(readme_value).strip() != str(freshness_value).strip():
            errors.append(
                f"README {field}={readme_value or '<missing>'} does not match freshness "
                f"{field}={freshness_value or '<missing>'}"
            )

    return errors


def validate_daily_report_source_preflight(
    repo_root: Path,
    freshness_path: Path,
    readme_path: Path,
    expected_date: str | None = None,
    require_git_clean: bool = True,
    allow_dirty: bool = False,
) -> tuple[list[str], list[str]]:
    errors: list[str] = []
    info: list[str] = []

    repo_root = repo_root.resolve()
    freshness_path = (repo_root / freshness_path).resolve() if not freshness_path.is_absolute() else freshness_path.resolve()
    readme_path = (repo_root / readme_path).resolve() if not readme_path.is_absolute() else readme_path.resolve()
    expected_date = normalize_date(expected_date) if expected_date else None

    if not freshness_path.exists():
        return [f"freshness file is missing: {freshness_path}"], info

    try:
        freshness_row = read_one_row(freshness_path)
    except Exception as exc:
        return [f"freshness file is unreadable: {exc}"], info

    errors.extend(validate_freshness_row(freshness_row, expected_date))

    readme_fields: dict[str, str] = {}
    if readme_path.exists():
        readme_fields = parse_key_value_file(readme_path)
        errors.extend(validate_readme_matches_freshness(readme_fields, freshness_row))
    else:
        errors.append(f"README file is missing: {readme_path}")

    head: str | None = None
    if require_git_clean:
        errors.extend(require_clean_git_checkout(repo_root, allow_dirty=allow_dirty))
        head, head_error = current_git_head(repo_root)
        if head_error:
            head = None

    readme_commit = readme_fields.get("commit_sha", "").strip()
    if readme_commit and head and readme_commit != head:
        info.append(
            "README commit_sha differs from checkout HEAD; allowed because README commit_sha is an "
            f"artifact source hint (readme_commit_sha={readme_commit}, head={head})."
        )

    return errors, info


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Validate that a daily report generation source is current, ready, and not a dirty/stale "
            "local checkout before producing ChatGPT-side PDFs."
        )
    )
    parser.add_argument("--repo-root", type=Path, default=Path("."))
    parser.add_argument("--freshness", type=Path, default=DEFAULT_FRESHNESS)
    parser.add_argument("--readme", type=Path, default=DEFAULT_README)
    parser.add_argument("--expected-date", default=None, help="Expected main_price_date in YYYYMMDD form.")
    parser.add_argument(
        "--allow-dirty",
        action="store_true",
        help="Allow a dirty checkout. Use only for diagnostics, not official report generation.",
    )
    parser.add_argument(
        "--skip-git-clean-check",
        action="store_true",
        help="Skip git clean checks for a trusted GitHub archive/non-git source.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()

    errors, info = validate_daily_report_source_preflight(
        repo_root=args.repo_root,
        freshness_path=args.freshness,
        readme_path=args.readme,
        expected_date=args.expected_date,
        require_git_clean=not args.skip_git_clean_check,
        allow_dirty=args.allow_dirty,
    )

    for line in info:
        print(f"INFO: {line}")

    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1

    row = read_one_row((args.repo_root / args.freshness).resolve() if not args.freshness.is_absolute() else args.freshness)
    print(
        "daily report source preflight passed: "
        f"main_price_date={normalize_date(row.get('main_price_date', ''))} "
        f"report_ready={is_true(row.get('report_ready', ''))} "
        f"warrant_ready={is_true(row.get('warrant_ready', ''))} "
        f"daily_pdf_ready={is_true(row.get('daily_pdf_ready', ''))} "
        f"git_clean={not args.skip_git_clean_check and not args.allow_dirty}"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
