from __future__ import annotations

import argparse
import csv
import io
import json
import subprocess
from pathlib import Path
from typing import Callable, Iterable, Mapping


ROOT = Path(__file__).resolve().parents[1]

SHARED_REGISTRY_KEY_FIELDS = {
    "config/repo_file_lifecycle_inventory.csv": "path",
    "config/repo_production_inventory.csv": "path",
    "config/report_artifact_lineage.csv": "artifact_path",
    "config/runtime_file_lineage_contract.csv": "script_path",
}

TDCC_AFFECTED_EXACT_PATHS = frozenset(
    {
        ".github/workflows/tdcc_weekly.yml",
        ".github/workflows/tdcc_weekly_pr_validation.yml",
        ".github/workflows/tdcc_history_backfill.yml",
        ".github/workflows/test_tdcc_trend.yml",
        ".github/workflows/repair_tdcc_monthly_history_gaps.yml",
        "config/repo_file_lifecycle_inventory.csv",
        "config/repo_production_inventory.csv",
        "config/report_artifact_lineage.csv",
        "config/runtime_file_lineage_contract.csv",
        "docs/APPS_SCRIPT_WORKFLOW_TRIGGER.md",
        "docs/apps_script_workflow_trigger.gs",
        "scripts/detect_tdcc_weekly_pr_scope.py",
        "scripts/validate_apps_script_workflow_triggers.py",
        "scripts/validate_daily_production_boundaries.py",
        "scripts/validate_repo_file_lifecycle_inventory.py",
        "scripts/validate_repo_production_inventory.py",
        "scripts/validate_repo_semantic_integrity.py",
        "tdcc_holder_ratio_top10.py",
        "tests/test_detect_tdcc_weekly_pr_scope.py",
        "tests/test_tdcc_weekly_pr_validation_workflow.py",
    }
)

TDCC_AFFECTED_PATH_PREFIXES = (
    ".github/workflows/repair_tdcc_",
    ".github/workflows/tdcc_",
    "data/tdcc_stock_history",
    "docs/tdcc_",
    "docs/latest/tdcc_",
    "output/history/tdcc/",
    "output/latest/tdcc_",
    "scripts/backfill_tdcc_",
    "scripts/build_tdcc_",
    "scripts/repair_tdcc_",
    "scripts/tdcc_",
    "scripts/validate_tdcc_",
    "tests/test_tdcc_",
    "tdcc_",
)

TDCC_REGISTRY_OWNERS = frozenset({"tdcc_weekly"})
TDCC_REGISTRY_RELATION_FIELDS = frozenset(
    {
        "path",
        "artifact_path",
        "script_path",
        "owner",
        "producer",
        "validator",
        "publisher",
        "allowed_workflows",
        "called_by_workflow",
        "imported_by",
        "tested_by",
        "documented_by",
        "writes_artifact",
        "purpose",
        "keep_reason",
    }
)
TDCC_REGISTRY_MARKERS = (
    "tdcc_weekly",
    "tdcc-weekly",
    "/tdcc_",
    "tdcc_",
    "tdcc/",
)


def normalize_path(value: str) -> str:
    path = value.strip().replace("\\", "/")
    while path.startswith("./"):
        path = path[2:]
    return path


def is_tdcc_affected_path(value: str) -> bool:
    path = normalize_path(value)
    return path in TDCC_AFFECTED_EXACT_PATHS or path.startswith(
        TDCC_AFFECTED_PATH_PREFIXES
    )


def is_tdcc_registry_row(row: Mapping[str, str]) -> bool:
    if row.get("owner", "").strip().lower() in TDCC_REGISTRY_OWNERS:
        return True
    return any(
        marker in value.lower()
        for field, value in row.items()
        if field in TDCC_REGISTRY_RELATION_FIELDS
        for marker in TDCC_REGISTRY_MARKERS
    )


class RegistryScopeError(RuntimeError):
    pass


def _read_git_text(revision: str, path: str) -> str:
    result = subprocess.run(
        ["git", "--no-replace-objects", "show", f"{revision}:{path}"],
        cwd=ROOT,
        check=False,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    if result.returncode != 0:
        stderr = result.stderr.decode("utf-8", errors="replace").strip()
        raise RegistryScopeError(
            f"cannot read shared registry {path!r} at {revision!r}: {stderr}"
        )
    try:
        return result.stdout.decode("utf-8-sig", errors="strict")
    except UnicodeDecodeError as exc:
        raise RegistryScopeError(
            f"shared registry must be valid UTF-8: {path!r} at {revision!r}: {exc}"
        ) from exc


def _parse_registry(
    source: str,
    *,
    path: str,
    key_field: str,
    revision: str,
) -> tuple[tuple[str, ...], dict[str, dict[str, str]]]:
    try:
        reader = csv.DictReader(io.StringIO(source, newline=""), strict=True)
        fieldnames = tuple(reader.fieldnames or ())
        if key_field not in fieldnames or len(fieldnames) != len(set(fieldnames)):
            raise RegistryScopeError(
                f"shared registry schema is invalid for {path!r} at {revision!r}"
            )
        rows: dict[str, dict[str, str]] = {}
        for row_number, row in enumerate(reader, start=2):
            if None in row or any(value is None for value in row.values()):
                raise RegistryScopeError(
                    f"shared registry row is malformed: {path}:{row_number} "
                    f"at {revision!r}"
                )
            normalized = {name: value for name, value in row.items()}
            key = normalized[key_field].strip()
            if not key or key in rows:
                raise RegistryScopeError(
                    f"shared registry key is empty or duplicated: {path}:{row_number} "
                    f"at {revision!r}"
                )
            rows[key] = normalized
    except csv.Error as exc:
        raise RegistryScopeError(
            f"cannot parse shared registry {path!r} at {revision!r}: {exc}"
        ) from exc
    return fieldnames, rows


def registry_change_affects(
    path: str,
    *,
    base_revision: str,
    head_revision: str,
    row_is_relevant: Callable[[Mapping[str, str]], bool],
) -> bool:
    key_field = SHARED_REGISTRY_KEY_FIELDS[path]
    try:
        base_fields, base_rows = _parse_registry(
            _read_git_text(base_revision, path),
            path=path,
            key_field=key_field,
            revision=base_revision,
        )
        head_fields, head_rows = _parse_registry(
            _read_git_text(head_revision, path),
            path=path,
            key_field=key_field,
            revision=head_revision,
        )
        if base_fields != head_fields:
            raise RegistryScopeError(f"shared registry schema changed: {path!r}")
    except RegistryScopeError:
        return True
    return any(
        row_is_relevant(row)
        for key in set(base_rows) | set(head_rows)
        if base_rows.get(key) != head_rows.get(key)
        for row in (base_rows.get(key), head_rows.get(key))
        if row is not None
    )


def is_tdcc_affected_changed_path(
    value: str,
    *,
    base_sha: str | None = None,
    head_sha: str | None = None,
) -> bool:
    path = normalize_path(value)
    if not is_tdcc_affected_path(path):
        return False
    if path not in SHARED_REGISTRY_KEY_FIELDS:
        return True
    if not base_sha or not head_sha:
        return True
    return registry_change_affects(
        path,
        base_revision=base_sha,
        head_revision=head_sha,
        row_is_relevant=is_tdcc_registry_row,
    )


def matched_tdcc_affected_paths(
    paths: Iterable[str],
    *,
    base_sha: str | None = None,
    head_sha: str | None = None,
) -> list[str]:
    return sorted(
        {
            normalize_path(path)
            for path in paths
            if is_tdcc_affected_changed_path(
                path,
                base_sha=base_sha,
                head_sha=head_sha,
            )
        }
    )


def changed_paths_from_git(base_sha: str, head_sha: str) -> list[str]:
    result = subprocess.run(
        [
            "git",
            "--no-replace-objects",
            "diff",
            "--name-only",
            "--diff-filter=ACMRD",
            f"{base_sha}...{head_sha}",
            "--",
        ],
        cwd=ROOT,
        check=True,
        text=True,
        encoding="utf-8",
        errors="replace",
        stdout=subprocess.PIPE,
    )
    return [normalize_path(line) for line in result.stdout.splitlines() if line.strip()]


def write_github_output(path: Path, matched: list[str]) -> None:
    with path.open("a", encoding="utf-8", newline="\n") as handle:
        handle.write(f"affected={'true' if matched else 'false'}\n")
        handle.write(f"matched_count={len(matched)}\n")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Detect whether a pull request affects TDCC weekly contracts."
    )
    parser.add_argument("--base-sha", required=True)
    parser.add_argument("--head-sha", required=True)
    parser.add_argument("--github-output", type=Path)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    changed = changed_paths_from_git(args.base_sha, args.head_sha)
    matched = matched_tdcc_affected_paths(
        changed,
        base_sha=args.base_sha,
        head_sha=args.head_sha,
    )
    payload = {
        "affected": bool(matched),
        "changed_count": len(changed),
        "matched_count": len(matched),
        "matched_paths": matched,
    }
    print(json.dumps(payload, ensure_ascii=True, sort_keys=True))
    if args.github_output:
        write_github_output(args.github_output, matched)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
