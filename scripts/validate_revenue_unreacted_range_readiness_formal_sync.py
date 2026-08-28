from __future__ import annotations

import argparse
import csv
import io
import re
import subprocess
from dataclasses import dataclass
from pathlib import Path


MODEL_ID = "revenue_unreacted_range"
CONTRACT_VERSION = "revenue_readiness_sync_3a_v1_20260828"
EXPECTED_PROMOTION_DECISION_ID = (
    "revenue_unreacted_range_source_mid_falling_promotion_preparation_v3_20260828"
)
EXPECTED_HOLDOUT_ARTIFACT_VERSION = "forward_holdout_v2_20260828"
EXPECTED_ANOMALY_COUNT = 9
EXPECTED_HOLDOUT_MATURE = 0
EXPECTED_HOLDOUT_MINIMUM = 20
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
READINESS_FALSE_FIELDS = {"approved_for_daily", "presentation_allowed"}
CANONICAL_FALSE_FIELDS = {
    "formal_model_use_allowed",
    "approved_for_daily",
    "presentation_allowed",
    "production_change",
}
EXPECTED_FIELDS = {
    "parity_status": "research_matrix_complete",
    "operation_module_status": "research_matrix_complete_formal_adapter_not_started",
    "daily_adapter_status": "not_started",
    "approval_status": "not_started",
    "operation_module_id": "",
    "approval_version": "",
    "operation_directive_level": "no_operation_directive",
    "pdf_integration_status": "not_started",
    "packet_integration_status": "not_started",
}
EXPECTED_BLOCKER = (
    "anomaly_disposition_blockers=9; unresolved_anomalies=9; "
    "forward_holdout_v2_mature=0/20; formal_adapter=not_started"
)


@dataclass(frozen=True)
class StatusEntry:
    index_status: str
    worktree_status: str
    path: str


def _git(repo: Path, *args: str) -> bytes:
    result = subprocess.run(
        ["git", "--no-replace-objects", *args],
        cwd=repo,
        check=False,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    if result.returncode:
        raise RuntimeError(result.stderr.decode("utf-8", errors="replace").strip())
    return result.stdout


def _rows(data: bytes) -> list[dict[str, str]]:
    text = data.decode("utf-8-sig")
    reader = csv.DictReader(io.StringIO(text))
    fieldnames = reader.fieldnames
    if not fieldnames:
        raise ValueError("missing CSV header")
    if any(not field.strip() for field in fieldnames):
        raise ValueError("blank CSV header")
    if len(fieldnames) != len(set(fieldnames)):
        raise ValueError("duplicate CSV header")
    rows = list(reader)
    if any(None in row for row in rows):
        raise ValueError("row has more values than the CSV header")
    return rows


def _normalized_non_revenue(rows: list[dict[str, str]]) -> dict[str, dict[str, str]]:
    normalized: dict[str, dict[str, str]] = {}
    for row in rows:
        model_id = row.get("model_id", "").strip()
        if not model_id:
            raise ValueError("readiness contains a blank model_id")
        if model_id == MODEL_ID:
            continue
        if model_id in normalized:
            raise ValueError(f"duplicate non-revenue model_id: {model_id}")
        normalized[model_id] = {
            key: ("" if key == "generated_at" else value)
            for key, value in row.items()
        }
    return normalized


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
            index += 1
            raise RuntimeError(
                f"readiness sync forbids rename/copy status: {source!r} -> {path!r}"
            )
        entries.append(StatusEntry(index_status, worktree_status, path))
    return entries


def validate_semantics(base_csv: bytes, current_csv: bytes) -> list[str]:
    errors: list[str] = []
    try:
        base_rows = _rows(base_csv)
        current_rows = _rows(current_csv)
        if _normalized_non_revenue(base_rows) != _normalized_non_revenue(current_rows):
            errors.append("non-revenue readiness rows drifted beyond generated_at")
    except (UnicodeDecodeError, csv.Error, ValueError) as exc:
        return [f"malformed readiness CSV: {exc}"]

    revenue = [row for row in current_rows if row.get("model_id", "").strip() == MODEL_ID]
    if len(revenue) != 1:
        return errors + [f"current readiness must contain exactly one {MODEL_ID} row"]
    row = revenue[0]
    for field in sorted(READINESS_FALSE_FIELDS):
        if row.get(field) != "False":
            errors.append(f"{MODEL_ID} {field} must remain False")
    for field, expected in EXPECTED_FIELDS.items():
        if row.get(field, "") != expected:
            errors.append(f"{MODEL_ID} {field} must be {expected!r}")
    if row.get("blocker", "") != EXPECTED_BLOCKER:
        errors.append(
            f"{MODEL_ID} blocker must equal the exact {CONTRACT_VERSION} blocker"
        )
    for optional_false_field in (
        "formal_model_use_allowed",
        "production_allowed",
        "production_change",
    ):
        if optional_false_field in row and row.get(optional_false_field) != "False":
            errors.append(f"{MODEL_ID} {optional_false_field} must remain False")
    return errors


def _canonical_model_rows(path: Path) -> tuple[list[dict[str, str]], list[str]]:
    try:
        rows = _rows(path.read_bytes())
    except (OSError, UnicodeDecodeError, csv.Error, ValueError) as exc:
        return [], [f"invalid canonical disabled source {path}: {exc}"]
    model_rows = [row for row in rows if row.get("model_id", "").strip() == MODEL_ID]
    if not model_rows:
        return [], [f"canonical disabled source has no {MODEL_ID} row: {path}"]
    return model_rows, []


def validate_canonical_disabled_sources(repo: Path) -> list[str]:
    errors: list[str] = []
    promotion_path = (
        repo / "config/revenue_unreacted_range_promotion_preparation_registry.csv"
    )
    holdout_path = (
        repo
        / "output/latest/research_backtest/"
        "revenue_unreacted_range_forward_holdout_v2_manifest_latest.csv"
    )
    promotion_rows, source_errors = _canonical_model_rows(promotion_path)
    errors.extend(source_errors)
    holdout_rows, source_errors = _canonical_model_rows(holdout_path)
    errors.extend(source_errors)
    if errors:
        return errors

    promotion_ids = [row.get("decision_id", "").strip() for row in promotion_rows]
    if any(not value for value in promotion_ids):
        errors.append("canonical promotion registry contains a blank decision_id")
    if len(promotion_ids) != len(set(promotion_ids)):
        errors.append("canonical promotion registry contains duplicate decision_id values")
    promotion = promotion_rows[-1]
    if promotion.get("decision_id") != EXPECTED_PROMOTION_DECISION_ID:
        errors.append(
            "canonical promotion decision must match the versioned one-shot sync contract"
        )
    if promotion.get("combined_exclusion_candidate_count") != str(EXPECTED_ANOMALY_COUNT):
        errors.append(
            f"canonical promotion anomaly count must remain {EXPECTED_ANOMALY_COUNT}"
        )
    if (
        promotion.get("forward_holdout_first_interpretation_min_mature")
        != str(EXPECTED_HOLDOUT_MINIMUM)
    ):
        errors.append(
            f"canonical promotion holdout minimum must remain {EXPECTED_HOLDOUT_MINIMUM}"
        )

    holdout_keys = [
        (
            row.get("artifact_version", "").strip(),
            row.get("capture_id", "").strip(),
            row.get("artifact_row_key", "").strip(),
        )
        for row in holdout_rows
    ]
    if any(not all(key) for key in holdout_keys):
        errors.append("canonical holdout source contains a blank versioned identity")
    if len(holdout_keys) != len(set(holdout_keys)):
        errors.append("canonical holdout source contains duplicate versioned identities")
    holdout = holdout_rows[-1]
    if holdout.get("artifact_version") != EXPECTED_HOLDOUT_ARTIFACT_VERSION:
        errors.append(
            "canonical holdout artifact_version must match the versioned one-shot sync contract"
        )
    if holdout.get("primary_mature_count") != str(EXPECTED_HOLDOUT_MATURE):
        errors.append(
            f"canonical forward holdout mature count must remain {EXPECTED_HOLDOUT_MATURE}"
        )

    for path, row in ((promotion_path, promotion), (holdout_path, holdout)):
        for field in sorted(CANONICAL_FALSE_FIELDS):
            if row.get(field) != "False":
                errors.append(f"canonical source {path} {field} must remain False")

    anomaly_path = (
        repo
        / "config/revenue_unreacted_range_anomaly_disposition_registry_v2_20260828.csv"
    )
    anomaly_rows, anomaly_errors = _canonical_model_rows(anomaly_path)
    errors.extend(anomaly_errors)
    if anomaly_errors:
        return errors
    operation_keys = [row.get("operation_key", "").strip() for row in anomaly_rows]
    if any(not key for key in operation_keys):
        errors.append("canonical anomaly evidence contains a blank operation_key")
    duplicate_keys = sorted(
        {key for key in operation_keys if key and operation_keys.count(key) > 1}
    )
    if duplicate_keys:
        errors.append(
            f"canonical anomaly evidence contains duplicate operation_key values: {duplicate_keys}"
        )
    unresolved = sum(
        row.get("final_disposition") == "unresolved_anomaly_candidate"
        for row in anomaly_rows
    )
    if len(anomaly_rows) != EXPECTED_ANOMALY_COUNT or unresolved != EXPECTED_ANOMALY_COUNT:
        errors.append(
            "canonical anomaly evidence must remain exact "
            f"{EXPECTED_ANOMALY_COUNT} distinct unresolved rows, "
            f"got rows={len(anomaly_rows)} unique={len(set(operation_keys))} "
            f"unresolved={unresolved}"
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
        if any(entry.index_status != " " for entry in entries):
            errors.append("working-tree sync must not contain staged changes")
        changed = status_paths
    elif phase == "staged":
        if any(
            entry.index_status not in {"A", "M"}
            or entry.worktree_status != " "
            for entry in entries
        ):
            errors.append(
                "staged sync must contain only staged additions/modifications and no "
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
    else:
        parent = _git(repo, "rev-parse", "HEAD^").decode().strip()
        commit_count = _git(repo, "rev-list", "--count", f"{base_sha}..HEAD").decode().strip()
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

    if changed != ALLOWED_PATHS:
        missing = sorted(ALLOWED_PATHS - changed)
        unexpected = sorted(changed - ALLOWED_PATHS)
        errors.append(
            "readiness formal sync must change exactly the four readiness mirrors: "
            f"missing={missing}; unexpected={unexpected}"
        )
    return errors


def validate(repo: Path, base_sha: str, phase: str) -> list[str]:
    if not re.fullmatch(r"[0-9a-f]{40}", base_sha):
        return ["base_sha must be an exact lowercase SHA"]
    errors: list[str] = []
    try:
        _git(repo, "cat-file", "-e", f"{base_sha}^{{commit}}")
        errors.extend(_validate_phase(repo, base_sha, phase))
        current_csv = (repo / CSV_PATH).read_bytes()
        if current_csv != (repo / DOCS_CSV_PATH).read_bytes():
            errors.append("output/docs readiness CSV copies differ")
        if (repo / MD_PATH).read_bytes() != (repo / DOCS_MD_PATH).read_bytes():
            errors.append("output/docs readiness Markdown copies differ")
        base_csv = _git(repo, "show", f"{base_sha}:{CSV_PATH}")
        errors.extend(validate_semantics(base_csv, current_csv))
        errors.extend(validate_canonical_disabled_sources(repo))
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
