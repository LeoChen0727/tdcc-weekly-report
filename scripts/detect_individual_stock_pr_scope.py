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

AFFECTED_EXACT_PATHS = frozenset(
    {
        ".github/workflows/current_holdings_pattern.yml",
        ".github/workflows/daily_full_pipeline.yml",
        ".github/workflows/individual_stock_data_refresh.yml",
        ".github/workflows/individual_stock_pr_validation.yml",
        ".github/workflows/individual_stock_report.yml",
        ".github/workflows/repair_daily_price_range.yml",
        ".github/workflows/repair_one_daily_price.yml",
        ".github/workflows/repair_recent_daily_price_gaps.yml",
        ".github/workflows/repair_tdcc_monthly_history_gaps.yml",
        ".github/workflows/research_backtest_pipeline.yml",
        ".github/workflows/tdcc_history_backfill.yml",
        ".github/workflows/tdcc_weekly.yml",
        ".github/workflows/volume_v2_advisory_lineage_refresh.yml",
        ".github/workflows/warrant_flow.yml",
        "config/repo_file_lifecycle_inventory.csv",
        "config/repo_production_inventory.csv",
        "config/report_artifact_lineage.csv",
        "config/runtime_file_lineage_contract.csv",
        "docs/APPS_SCRIPT_WORKFLOW_TRIGGER.md",
        "scripts/detect_individual_stock_pr_scope.py",
        "scripts/individual_tdcc_dataset_consumer.py",
        "scripts/validate_individual_pdf_contract_consumers.py",
        "scripts/validate_repo_file_lifecycle_inventory.py",
        "scripts/validate_repo_production_inventory.py",
        "tests/test_individual_pdf_contract_consumers.py",
        "tests/test_individual_tdcc_dataset_consumer.py",
        "tests/test_individual_stock_pr_validation_workflow.py",
        "tests/test_repo_file_lifecycle_inventory.py",
        "tests/test_repo_production_inventory.py",
    }
)

INDIVIDUAL_REGISTRY_OWNERS = frozenset({"individual_stock"})
INDIVIDUAL_REGISTRY_MARKERS = (
    "individual_stock",
    "individual-stock",
    "individual_tdcc",
    "individual_stock_reports",
)

AFFECTED_PATH_PREFIXES = (
    "config/individual_stock_",
    "docs/individual_stock_",
    "docs/latest/individual_stock_reports/",
    "output/history/individual_stock_reports/",
    "output/latest/individual_stock_reports/",
    "scripts/build_individual_stock_",
    "scripts/generate_individual_stock_",
    "scripts/validate_individual_stock_",
    "tests/test_individual_stock_",
)


def normalize_path(value: str) -> str:
    path = value.strip().replace("\\", "/")
    while path.startswith("./"):
        path = path[2:]
    return path


def is_affected_path(value: str) -> bool:
    path = normalize_path(value)
    return path in AFFECTED_EXACT_PATHS or path.startswith(AFFECTED_PATH_PREFIXES)


def is_individual_registry_row(row: Mapping[str, str]) -> bool:
    if row.get("owner", "").strip().lower() in INDIVIDUAL_REGISTRY_OWNERS:
        return True
    return any(
        marker in value.lower()
        for value in row.values()
        for marker in INDIVIDUAL_REGISTRY_MARKERS
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


def is_affected_changed_path(
    value: str,
    *,
    base_sha: str | None = None,
    head_sha: str | None = None,
) -> bool:
    path = normalize_path(value)
    if not is_affected_path(path):
        return False
    if path not in SHARED_REGISTRY_KEY_FIELDS:
        return True
    if not base_sha or not head_sha:
        # Path-only callers cannot prove that a shared registry edit is unrelated.
        return True
    return registry_change_affects(
        path,
        base_revision=base_sha,
        head_revision=head_sha,
        row_is_relevant=is_individual_registry_row,
    )


def matched_affected_paths(
    paths: Iterable[str],
    *,
    base_sha: str | None = None,
    head_sha: str | None = None,
) -> list[str]:
    return sorted(
        {
            normalize_path(path)
            for path in paths
            if is_affected_changed_path(
                path,
                base_sha=base_sha,
                head_sha=head_sha,
            )
        }
    )


def _run_git(args: list[str]) -> subprocess.CompletedProcess[bytes]:
    return subprocess.run(
        ["git", "--no-replace-objects", *args],
        cwd=ROOT,
        check=False,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )


def _resolve_commit_object(value: str, label: str) -> str:
    object_type = _run_git(["cat-file", "-t", value])
    if object_type.returncode != 0 or object_type.stdout.strip() != b"commit":
        stderr = object_type.stderr.decode("utf-8", errors="replace").strip()
        raise RegistryScopeError(
            f"{label} must identify a commit object: {value!r}: {stderr}"
        )
    resolved = _run_git(["rev-parse", "--verify", f"{value}^{{commit}}"])
    if resolved.returncode != 0:
        stderr = resolved.stderr.decode("utf-8", errors="replace").strip()
        raise RegistryScopeError(f"cannot resolve {label}: {value!r}: {stderr}")
    return resolved.stdout.decode("ascii", errors="strict").strip()


def validate_commit_range(base_sha: str, head_sha: str) -> tuple[str, str]:
    resolved_base = _resolve_commit_object(base_sha, "base SHA")
    resolved_head = _resolve_commit_object(head_sha, "head SHA")
    merge_base = _run_git(["merge-base", resolved_base, resolved_head])
    if merge_base.returncode != 0:
        stderr = merge_base.stderr.decode("utf-8", errors="replace").strip()
        raise RegistryScopeError(f"cannot compute base/head merge-base: {stderr}")
    actual_merge_base = merge_base.stdout.decode("ascii", errors="strict").strip()
    if actual_merge_base != resolved_base:
        raise RegistryScopeError(
            "base SHA must be an ancestor of head SHA: "
            f"base={resolved_base!r}, merge_base={actual_merge_base!r}"
        )
    return resolved_base, resolved_head


def parse_name_status_z(payload: bytes) -> list[str]:
    if payload and not payload.endswith(b"\0"):
        raise RegistryScopeError("malformed NUL-delimited git name-status output")
    fields = payload.split(b"\0")
    if fields and fields[-1] == b"":
        fields.pop()
    if len(fields) % 2:
        raise RegistryScopeError("malformed NUL-delimited git name-status output")

    paths: list[str] = []
    for index in range(0, len(fields), 2):
        status = fields[index].decode("ascii", errors="strict")
        if status not in {"A", "B", "D", "M", "T", "U", "X"}:
            raise RegistryScopeError(
                f"unexpected git status with rename detection disabled: {status!r}"
            )
        path = fields[index + 1].decode("utf-8", errors="surrogateescape")
        if not path:
            raise RegistryScopeError("git diff returned an empty changed path")
        paths.append(normalize_path(path))
    return sorted(set(paths))


def changed_paths_from_git(base_sha: str, head_sha: str) -> list[str]:
    result = subprocess.run(
        [
            "git",
            "--no-replace-objects",
            "diff",
            "--no-renames",
            "--name-status",
            "-z",
            f"{base_sha}...{head_sha}",
            "--",
        ],
        cwd=ROOT,
        check=False,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    if result.returncode != 0:
        stderr = result.stderr.decode("utf-8", errors="replace").strip()
        raise RegistryScopeError(f"git diff failed: {stderr}")
    return parse_name_status_z(result.stdout)


def write_github_output(path: Path, matched: list[str]) -> None:
    with path.open("a", encoding="utf-8", newline="\n") as handle:
        handle.write(f"affected={'true' if matched else 'false'}\n")
        handle.write(f"matched_count={len(matched)}\n")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Detect whether a pull request affects individual-stock contracts or "
            "production artifact-writer authentication."
        )
    )
    parser.add_argument("--base-sha", required=True)
    parser.add_argument("--head-sha", required=True)
    parser.add_argument("--github-output", type=Path)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    base_sha, head_sha = validate_commit_range(args.base_sha, args.head_sha)
    changed = changed_paths_from_git(base_sha, head_sha)
    matched = matched_affected_paths(
        changed,
        base_sha=base_sha,
        head_sha=head_sha,
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
