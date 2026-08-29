from __future__ import annotations

import argparse
import csv
import io
import re
import subprocess
from dataclasses import dataclass
from pathlib import Path


MODEL_ID = "revenue_unreacted_range"
CONTRACT_VERSION = "revenue_readiness_sync_3c_v2_20260829"
ALLOWED_PATHS = {
    "output/latest/model_operation_readiness_latest.csv",
    "output/latest/model_operation_readiness_latest.md",
    "docs/latest/model_operation_readiness_latest.csv",
    "docs/latest/model_operation_readiness_latest.md",
}
CSV_PATH = "output/latest/model_operation_readiness_latest.csv"
DOCS_CSV_PATH = "docs/latest/model_operation_readiness_latest.csv"
MD_PATH = "output/latest/model_operation_readiness_latest.md"
DOCS_MD_PATH = "docs/latest/model_operation_readiness_latest.md"

PERMISSION_FALSE_FIELDS = {
    "formal_model_use_allowed",
    "approved_for_daily",
    "presentation_allowed",
    "production_allowed",
}
REVENUE_ONLY_PERMISSION_FIELDS = {
    "formal_model_use_allowed",
    "production_allowed",
}
EXPECTED_FIELDS = {
    "parity_status": "research_matrix_complete",
    "blocker": "forward_holdout_v2_mature=0/20",
    "operation_module_status": "disabled_adapter_preparation_validated",
    "daily_adapter_status": "disabled_no_runtime_artifact",
    "approval_status": "not_started",
    "operation_module_id": (
        "revenue_unreacted_range_source_mid_falling_v2_operation_v1"
    ),
    "approval_version": "",
    "operation_directive_level": "no_operation_directive",
    "pdf_integration_status": "not_started",
    "packet_integration_status": "not_started",
    "registry_current_model_pattern_count": "0",
    "daily_adapter_row_count": "0",
    "daily_adapter_data_row_count": "0",
    "daily_adapter_sections": "",
}
EXPECTED_STATUS_NOTE_TOKENS = (
    "九筆 anomaly disposition 與 disabled formal adapter preparation 均已完成",
    "八筆 verified_real_extreme 保留於 Primary",
    "6177",
    "data error 已完成固定規則修復重跑",
    "目前 promotion blocker 僅為 forward holdout v2 成熟度 0/20",
)


def _base_authorization_already_consumed(row: dict[str, str]) -> bool:
    return (
        all(
            row.get(field, "") == expected
            for field, expected in EXPECTED_FIELDS.items()
        )
        and all(
            row.get(field, "") == "False" for field in PERMISSION_FALSE_FIELDS
        )
        and all(
            token in row.get("status_note_zh", "")
            for token in EXPECTED_STATUS_NOTE_TOKENS
        )
    )


MARKDOWN_COMPARE_FIELDS = (
    "model_id",
    "parity_status",
    "operation_module_status",
    "daily_adapter_status",
    "formal_model_use_allowed",
    "approved_for_daily",
    "approval_status",
    "operation_module_id",
    "approval_version",
    "presentation_allowed",
    "production_allowed",
    "operation_directive_level",
    "pdf_integration_status",
    "packet_integration_status",
    "blocker",
    "status_note_zh",
)


@dataclass(frozen=True)
class StatusEntry:
    index_status: str
    worktree_status: str
    path: str


def _git(repo: Path, *args: str) -> bytes:
    completed = subprocess.run(
        ["git", "--no-replace-objects", *args],
        cwd=repo,
        check=False,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    if completed.returncode:
        detail = completed.stderr.decode("utf-8", errors="replace").strip()
        raise RuntimeError(detail or f"git {' '.join(args)} failed")
    return completed.stdout


def _parse_csv(data: bytes) -> tuple[tuple[str, ...], list[dict[str, str]]]:
    text = data.decode("utf-8-sig")
    reader = csv.DictReader(io.StringIO(text))
    fieldnames = tuple(reader.fieldnames or ())
    if not fieldnames:
        raise ValueError("missing CSV header")
    if any(not field.strip() for field in fieldnames):
        raise ValueError("blank CSV header")
    if len(fieldnames) != len(set(fieldnames)):
        raise ValueError("duplicate CSV header")
    rows = list(reader)
    if not rows:
        raise ValueError("readiness CSV has no data rows")
    if any(None in row for row in rows):
        raise ValueError("row has more values than the CSV header")
    if any(value is None for row in rows for value in row.values()):
        raise ValueError("row has fewer values than the CSV header")
    return fieldnames, rows


def _rows_by_model(rows: list[dict[str, str]]) -> dict[str, dict[str, str]]:
    indexed: dict[str, dict[str, str]] = {}
    for row in rows:
        model_id = row.get("model_id", "").strip()
        if not model_id:
            raise ValueError("readiness contains a blank model_id")
        if model_id in indexed:
            raise ValueError(f"readiness contains duplicate model_id {model_id!r}")
        indexed[model_id] = row
    return indexed


def _normalized_non_revenue(
    rows_by_model: dict[str, dict[str, str]],
) -> dict[str, dict[str, str]]:
    return {
        model_id: {
            field: ("" if field == "generated_at" else value)
            for field, value in row.items()
        }
        for model_id, row in rows_by_model.items()
        if model_id != MODEL_ID
    }


def _validate_csv_semantics(base_csv: bytes, current_csv: bytes) -> list[str]:
    errors: list[str] = []
    try:
        base_fields, base_rows = _parse_csv(base_csv)
        current_fields, current_rows = _parse_csv(current_csv)
        if current_fields != base_fields:
            errors.append("readiness CSV schema or column order changed from base_sha")
        missing_fields = sorted(set(EXPECTED_FIELDS) - set(current_fields))
        if missing_fields:
            errors.append(f"readiness CSV is missing required fields: {missing_fields}")
        base_by_model = _rows_by_model(base_rows)
        current_by_model = _rows_by_model(current_rows)
    except (UnicodeDecodeError, csv.Error, ValueError) as exc:
        return [f"malformed readiness CSV: {exc}"]

    if set(current_by_model) != set(base_by_model):
        errors.append("readiness model_id set changed from base_sha")
    if _normalized_non_revenue(current_by_model) != _normalized_non_revenue(
        base_by_model
    ):
        errors.append("non-revenue readiness rows drifted beyond generated_at")

    base_revenue = base_by_model.get(MODEL_ID)
    revenue = current_by_model.get(MODEL_ID)
    if revenue is None:
        return errors + [f"readiness must contain exactly one {MODEL_ID} row"]
    if base_revenue is None:
        errors.append(f"base_sha readiness has no {MODEL_ID} row")
    else:
        if _base_authorization_already_consumed(base_revenue):
            errors.append(
                f"{CONTRACT_VERSION} authorization is already consumed by "
                "the base_sha readiness mirrors"
            )
        if revenue.get("model_name_zh", "") != base_revenue.get("model_name_zh", ""):
            errors.append(f"{MODEL_ID} model_name_zh changed from base_sha")

    for field, expected in EXPECTED_FIELDS.items():
        if revenue.get(field, "") != expected:
            errors.append(
                f"{MODEL_ID} {field} must be {expected!r}, "
                f"got {revenue.get(field, '')!r}"
            )
    for field in sorted(PERMISSION_FALSE_FIELDS):
        if revenue.get(field, "") != "False":
            errors.append(f"{MODEL_ID} {field} must remain False")
    for model_id, row in current_by_model.items():
        if model_id == MODEL_ID:
            continue
        for field in sorted(REVENUE_ONLY_PERMISSION_FIELDS):
            if row.get(field, "") != "":
                errors.append(
                    f"{model_id} {field} is revenue-only; non-revenue rows "
                    "must remain neutral blank"
                )

    status_note = revenue.get("status_note_zh", "")
    for token in EXPECTED_STATUS_NOTE_TOKENS:
        if token not in status_note:
            errors.append(f"{MODEL_ID} status_note_zh is missing {token!r}")
    return errors


def _markdown_status_rows(data: bytes) -> tuple[list[str], list[dict[str, str]]]:
    lines = data.decode("utf-8-sig").splitlines()
    try:
        heading = next(
            index
            for index, line in enumerate(lines)
            if line.strip() == "## Status Table"
        )
    except StopIteration as exc:
        raise ValueError("readiness Markdown is missing the Status Table") from exc
    table_lines = [
        line for line in lines[heading + 1 :] if line.strip().startswith("|")
    ]
    if len(table_lines) < 3:
        raise ValueError("readiness Markdown Status Table is incomplete")

    def cells(line: str) -> list[str]:
        return [cell.strip() for cell in line.strip().strip("|").split("|")]

    header = cells(table_lines[0])
    if not header or len(header) != len(set(header)):
        raise ValueError("readiness Markdown Status Table header is invalid")
    rows: list[dict[str, str]] = []
    for line in table_lines[2:]:
        values = cells(line)
        if len(values) != len(header):
            raise ValueError("readiness Markdown Status Table row width drifted")
        rows.append(dict(zip(header, values)))
    return header, rows


def _validate_markdown_semantics(markdown: bytes, current_csv: bytes) -> list[str]:
    errors: list[str] = []
    try:
        header, markdown_rows = _markdown_status_rows(markdown)
        _, csv_rows = _parse_csv(current_csv)
        markdown_by_model = _rows_by_model(markdown_rows)
        csv_by_model = _rows_by_model(csv_rows)
    except (UnicodeDecodeError, csv.Error, ValueError) as exc:
        return [f"malformed readiness Markdown: {exc}"]

    missing = sorted(set(MARKDOWN_COMPARE_FIELDS) - set(header))
    if missing:
        errors.append(f"readiness Markdown Status Table is missing fields: {missing}")
    if set(markdown_by_model) != set(csv_by_model):
        errors.append("readiness Markdown and CSV model_id sets differ")
    revenue_markdown = markdown_by_model.get(MODEL_ID)
    revenue_csv = csv_by_model.get(MODEL_ID)
    if revenue_markdown is None or revenue_csv is None:
        return errors + [f"readiness Markdown or CSV has no {MODEL_ID} row"]
    for field in MARKDOWN_COMPARE_FIELDS:
        if field in header and revenue_markdown.get(field, "") != revenue_csv.get(
            field, ""
        ):
            errors.append(f"readiness Markdown {MODEL_ID} {field} disagrees with CSV")
    for field in sorted(PERMISSION_FALSE_FIELDS):
        if revenue_markdown.get(field, "") != "False":
            errors.append(f"readiness Markdown {MODEL_ID} {field} must remain False")
    return errors


def _status_entries(repo: Path) -> list[StatusEntry]:
    raw = _git(
        repo,
        "status",
        "--porcelain=v1",
        "-z",
        "--untracked-files=all",
        "--",
        ".",
    )
    records = raw.decode("utf-8", errors="strict").split("\0")
    entries: list[StatusEntry] = []
    index = 0
    while index < len(records):
        record = records[index]
        index += 1
        if not record:
            continue
        if len(record) < 4 or record[2] != " ":
            raise RuntimeError(f"malformed git status record: {record!r}")
        index_status, worktree_status = record[0], record[1]
        path = record[3:]
        if index_status in {"R", "C"} or worktree_status in {"R", "C"}:
            if index >= len(records) or not records[index]:
                raise RuntimeError("malformed rename/copy status record")
            source = records[index]
            raise RuntimeError(
                f"readiness sync forbids rename/copy status: {source!r} -> {path!r}"
            )
        entries.append(StatusEntry(index_status, worktree_status, path))
    return entries


def _validate_regular_artifacts(repo: Path, revision: str | None) -> list[str]:
    errors: list[str] = []
    for logical_path in sorted(ALLOWED_PATHS):
        path = repo / logical_path
        if path.is_symlink() or not path.is_file():
            errors.append(f"readiness mirror must be a regular file: {logical_path}")
            continue
        if revision is None:
            record = _git(repo, "ls-files", "--stage", "--", logical_path).decode()
            fields = record.strip().split()
            valid = (
                len(fields) >= 4
                and fields[0] == "100644"
                and fields[2] == "0"
            )
        else:
            record = _git(repo, "ls-tree", revision, "--", logical_path).decode()
            fields = record.strip().split()
            valid = (
                len(fields) >= 4
                and fields[0] == "100644"
                and fields[1] == "blob"
            )
        if not valid:
            errors.append(
                f"readiness mirror must be a tracked 100644 blob: {logical_path}"
            )
    return errors


def _validate_phase(repo: Path, base_sha: str, phase: str) -> list[str]:
    errors: list[str] = []
    head = _git(repo, "rev-parse", "HEAD").decode().strip()
    entries = _status_entries(repo)
    status_paths = {entry.path for entry in entries}

    if phase in {"working-tree", "staged"} and head != base_sha:
        errors.append(f"{phase} sync HEAD must equal base_sha")

    if phase == "working-tree":
        if any(
            (entry.index_status, entry.worktree_status) != (" ", "M")
            for entry in entries
        ):
            errors.append(
                "working-tree sync must contain only unstaged tracked modifications"
            )
        changed = status_paths
        errors.extend(_validate_regular_artifacts(repo, None))
    elif phase == "staged":
        if any(
            (entry.index_status, entry.worktree_status) != ("M", " ")
            for entry in entries
        ):
            errors.append(
                "staged sync must contain only staged tracked modifications and no "
                "unstaged or untracked changes"
            )
        changed = set(
            _git(
                repo,
                "diff",
                "--cached",
                "--no-renames",
                "--name-only",
                "--",
                ".",
            )
            .decode()
            .splitlines()
        )
        if status_paths != changed:
            errors.append("staged sync git status and index diff paths differ")
        errors.extend(_validate_regular_artifacts(repo, None))
    else:
        parent = _git(repo, "rev-parse", "HEAD^").decode().strip()
        commit_count = (
            _git(repo, "rev-list", "--count", f"{base_sha}..HEAD")
            .decode()
            .strip()
        )
        if parent != base_sha or commit_count != "1":
            errors.append("committed sync must be exactly one direct child of base_sha")
        if entries:
            errors.append("committed sync worktree and index must be clean")
        changed = set(
            _git(
                repo,
                "diff",
                "--no-renames",
                "--name-only",
                f"{base_sha}..HEAD",
                "--",
                ".",
            )
            .decode()
            .splitlines()
        )
        errors.extend(_validate_regular_artifacts(repo, "HEAD"))

    if changed != ALLOWED_PATHS:
        errors.append(
            "readiness formal sync must change exactly the four readiness mirrors: "
            f"missing={sorted(ALLOWED_PATHS - changed)}; "
            f"unexpected={sorted(changed - ALLOWED_PATHS)}"
        )
    return errors


def validate(repo: Path, base_sha: str, phase: str) -> list[str]:
    if phase not in {"working-tree", "staged", "committed"}:
        return ["phase must be working-tree, staged, or committed"]
    if re.fullmatch(r"[0-9a-f]{40}", base_sha) is None:
        return ["base_sha must be an exact lowercase SHA"]
    errors: list[str] = []
    try:
        _git(repo, "cat-file", "-e", f"{base_sha}^{{commit}}")
        errors.extend(_validate_phase(repo, base_sha, phase))
        current_csv = (repo / CSV_PATH).read_bytes()
        current_markdown = (repo / MD_PATH).read_bytes()
        if current_csv != (repo / DOCS_CSV_PATH).read_bytes():
            errors.append("output/docs readiness CSV mirrors differ")
        if current_markdown != (repo / DOCS_MD_PATH).read_bytes():
            errors.append("output/docs readiness Markdown mirrors differ")
        base_csv = _git(repo, "show", f"{base_sha}:{CSV_PATH}")
        errors.extend(_validate_csv_semantics(base_csv, current_csv))
        errors.extend(_validate_markdown_semantics(current_markdown, current_csv))
    except (OSError, RuntimeError, UnicodeDecodeError) as exc:
        errors.append(f"fail-closed readiness sync validation error: {exc}")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo-root", type=Path, default=Path("."))
    parser.add_argument("--base-sha", required=True)
    parser.add_argument(
        "--phase",
        choices=("working-tree", "staged", "committed"),
        required=True,
    )
    args = parser.parse_args()
    errors = validate(args.repo_root.resolve(), args.base_sha, args.phase)
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1
    print(
        "Revenue unreacted range readiness formal sync validation passed: "
        f"{CONTRACT_VERSION}."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
