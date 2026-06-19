from __future__ import annotations

import argparse
import csv
import hashlib
import json
import re
import subprocess
from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PROTECTED_PATHS = ROOT / "config" / "workspace_cleanup_protected_paths.csv"
OUTPUT_SCHEMA = ROOT / "config" / "workspace_output_lifecycle_schema.csv"
GITIGNORE = ROOT / ".gitignore"
ENTRYPOINT = ROOT / "scripts" / "run_chatgpt_daily_report_entrypoint.py"
DAILY_WORKFLOW = ROOT / ".github" / "workflows" / "daily_full_pipeline.yml"

REQUIRED_PROTECTED_COLUMNS = {
    "path",
    "match_type",
    "path_required",
    "scope",
    "owner",
    "protected_reason",
    "hard_block",
    "review_required",
}

REQUIRED_OUTPUT_SCHEMA_COLUMNS = {
    "path",
    "type",
    "owner",
    "producer",
    "purpose",
    "source_ref",
    "reproducible",
    "official",
    "evidence_level",
    "action",
    "expires_at",
    "delete_risk",
    "protected_reason",
    "main_price_date",
    "report_ready",
    "warrant_ready",
    "daily_pdf_ready",
}

PROTECTED_MANIFEST_PREFIXES = ("output/latest/", "config/", ".github/workflows/")
FORBIDDEN_APPLY_PATTERNS = (
    "apply_workspace_cleanup.py",
    "apply_workspace_cleanup",
)


@dataclass(frozen=True)
class ProtectedRow:
    path: str
    match_type: str
    path_required: bool


def contains_wildcard(value: str) -> bool:
    return any(char in value for char in "*?[]")


def read_csv(path: Path) -> tuple[list[str], list[dict[str, str]]]:
    with path.open("r", encoding="utf-8-sig", newline="") as fh:
        reader = csv.DictReader(fh)
        return list(reader.fieldnames or []), [{key: str(value or "") for key, value in row.items()} for row in reader]


def load_protected_rows(errors: list[str]) -> list[ProtectedRow]:
    rows: list[ProtectedRow] = []
    if not PROTECTED_PATHS.exists():
        errors.append("missing config/workspace_cleanup_protected_paths.csv")
        return rows
    fieldnames, raw_rows = read_csv(PROTECTED_PATHS)
    missing = REQUIRED_PROTECTED_COLUMNS.difference(fieldnames)
    if missing:
        errors.append(f"protected paths missing columns: {sorted(missing)}")
        return rows
    for line_no, row in enumerate(raw_rows, start=2):
        path = row.get("path", "").strip().replace("\\", "/")
        match_type = row.get("match_type", "").strip()
        if not path:
            errors.append(f"protected path row {line_no} has empty path")
            continue
        if contains_wildcard(path):
            errors.append(f"protected path row {line_no} uses wildcard: {path}")
        if ".." in Path(path).parts:
            errors.append(f"protected path row {line_no} uses parent traversal: {path}")
        if match_type not in {"exact", "prefix"}:
            errors.append(f"protected path row {line_no} has invalid match_type: {match_type}")
        path_required = row.get("path_required", "").strip().lower() == "true"
        if path_required and not (ROOT / path).exists():
            errors.append(f"required protected path missing: {path}")
        rows.append(ProtectedRow(path=path, match_type=match_type, path_required=path_required))
    return rows


def path_matches_protected(rel_path: str, rows: list[ProtectedRow]) -> tuple[bool, str]:
    normalized = rel_path.replace("\\", "/").lower().rstrip("/")
    for row in rows:
        protected = row.path.lower().rstrip("/")
        if row.match_type == "exact" and normalized == protected:
            return True, row.path
        if row.match_type == "prefix" and (normalized == protected or normalized.startswith(protected.rstrip("/") + "/")):
            return True, row.path
    return False, ""


def validate_output_schema(errors: list[str]) -> None:
    if not OUTPUT_SCHEMA.exists():
        errors.append("missing config/workspace_output_lifecycle_schema.csv")
        return
    fieldnames, _ = read_csv(OUTPUT_SCHEMA)
    missing = REQUIRED_OUTPUT_SCHEMA_COLUMNS.difference(fieldnames)
    if missing:
        errors.append(f"output lifecycle schema missing columns: {sorted(missing)}")


def validate_gitignore(errors: list[str]) -> None:
    text = GITIGNORE.read_text(encoding="utf-8", errors="replace") if GITIGNORE.exists() else ""
    for required in ("_workspace_quarantine/", "workspace_cleanup_reports/"):
        if required not in text:
            errors.append(f".gitignore missing {required}")


def validate_no_apply_hooks(errors: list[str]) -> None:
    for path in (ENTRYPOINT, DAILY_WORKFLOW):
        text = path.read_text(encoding="utf-8", errors="replace") if path.exists() else ""
        for pattern in FORBIDDEN_APPLY_PATTERNS:
            if pattern in text:
                errors.append(f"{path.relative_to(ROOT).as_posix()} must not call cleanup apply tooling: {pattern}")


def git_ls_files() -> set[str]:
    result = subprocess.run(
        ["git", "ls-files"],
        cwd=ROOT,
        check=True,
        text=True,
        encoding="utf-8",
        errors="replace",
        stdout=subprocess.PIPE,
    )
    return {line.strip().replace("\\", "/") for line in result.stdout.splitlines() if line.strip()}


def canonical_manifest_hash(manifest: dict[str, object]) -> str:
    copy = json.loads(json.dumps(manifest, ensure_ascii=False))
    copy["manifest_hash"] = ""
    payload = json.dumps(copy, sort_keys=True, ensure_ascii=False, separators=(",", ":")).encode("utf-8")
    return hashlib.sha256(payload).hexdigest()


def resolve_manifest_pointer(path: Path) -> tuple[Path, dict[str, object]]:
    pointer = json.loads(path.read_text(encoding="utf-8"))
    manifest_path = ROOT / str(pointer.get("manifest_path", ""))
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    if pointer.get("report_id") != manifest.get("report_id"):
        raise ValueError("latest_manifest pointer report_id does not match manifest")
    if pointer.get("manifest_hash") != manifest.get("manifest_hash"):
        raise ValueError("latest_manifest pointer hash does not match manifest")
    if canonical_manifest_hash(manifest) != manifest.get("manifest_hash"):
        raise ValueError("manifest hash does not match canonical payload")
    return manifest_path, manifest


def status_new_entries(before: str, after: str) -> set[str]:
    before_lines = {line for line in before.splitlines() if line.strip()}
    after_lines = {line for line in after.splitlines() if line.strip()}
    return after_lines - before_lines


def status_only_allows_history_summary(before: str, after: str, history_summary: str) -> bool:
    added = status_new_entries(before, after)
    if not added:
        return True
    if not history_summary:
        return False
    normalized = history_summary.replace("\\", "/")
    return all(line[3:].replace("\\", "/") == normalized for line in added if len(line) > 3)


def validate_manifest(manifest_arg: Path, protected_rows: list[ProtectedRow], errors: list[str]) -> None:
    try:
        manifest_path, manifest = resolve_manifest_pointer(manifest_arg)
    except Exception as exc:
        errors.append(f"manifest pointer cannot be resolved: {exc}")
        return
    if not manifest_path.exists():
        errors.append(f"manifest path does not exist: {manifest_path}")
        return
    if manifest_path.name != "manifest.json":
        errors.append(f"manifest pointer must resolve to manifest.json: {manifest_path}")
    tracked = git_ls_files()
    rows = manifest.get("rows", [])
    if not isinstance(rows, list):
        errors.append("manifest rows must be a list")
        return
    for row in rows:
        rel_path = str(row.get("path", "")).strip().replace("\\", "/")
        if not rel_path:
            errors.append("manifest row has empty path")
            continue
        if contains_wildcard(rel_path):
            errors.append(f"manifest row uses wildcard: {rel_path}")
        if ".." in Path(rel_path).parts:
            errors.append(f"manifest row uses parent traversal: {rel_path}")
        resolved = (ROOT / rel_path).resolve(strict=False)
        root_resolved = ROOT.resolve(strict=False)
        if root_resolved not in (resolved, *resolved.parents):
            errors.append(f"manifest row escapes repo root: {rel_path}")
        protected, protected_match = path_matches_protected(rel_path, protected_rows)
        if protected:
            errors.append(f"manifest row includes protected path {rel_path} via {protected_match}")
        for prefix in PROTECTED_MANIFEST_PREFIXES:
            if rel_path == prefix.rstrip("/") or rel_path.startswith(prefix):
                errors.append(f"manifest row includes protected prefix: {rel_path}")
        if rel_path in tracked:
            errors.append(f"manifest row includes tracked file: {rel_path}")
        if row.get("planned_action") == "delete" and int(row.get("file_count", 1) or 1) != 0:
            errors.append(f"manifest delete row is not empty: {rel_path}")
        if str(row.get("layout_baseline_keep", "")).lower() == "true" and row.get("planned_action") != "keep":
            errors.append(f"layout baseline row must be kept: {rel_path}")

    before = str(manifest.get("git_status_porcelain_before_planner", ""))
    after = str(manifest.get("git_status_porcelain_after_planner", ""))
    history_summary = str(manifest.get("history_summary_path", ""))
    if not status_only_allows_history_summary(before, after, history_summary):
        errors.append("planner added tracked status entries outside the allowed history summary")


def validate(manifest: Path | None = None) -> list[str]:
    errors: list[str] = []
    protected_rows = load_protected_rows(errors)
    validate_output_schema(errors)
    validate_gitignore(errors)
    validate_no_apply_hooks(errors)
    if manifest is not None:
        validate_manifest(manifest, protected_rows, errors)
    return errors


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Validate workspace cleanup policy and manifests.")
    parser.add_argument("--manifest", default="")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    errors = validate(Path(args.manifest) if args.manifest else None)
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1
    print("workspace cleanup policy validation passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
