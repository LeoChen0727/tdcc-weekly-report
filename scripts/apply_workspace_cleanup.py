from __future__ import annotations

import argparse
import csv
import json
import os
import shutil
import subprocess
import sys
from dataclasses import dataclass
from datetime import UTC, datetime, timedelta
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from scripts import plan_workspace_cleanup as planner
from scripts import validate_workspace_cleanup_policy as policy


DEFAULT_MANIFEST = ROOT / "workspace_cleanup_reports" / "latest_manifest.json"
DEFAULT_QUARANTINE_ROOT = ROOT / "_workspace_quarantine"
DEFAULT_REPORT_ROOT = ROOT / "workspace_cleanup_reports"
QUARANTINE_MANIFEST_COLUMNS = [
    "original_path",
    "quarantine_path",
    "reason",
    "moved_at",
    "expires_at",
    "owner",
    "recovery_hint",
    "final_action",
]


class ApplyError(RuntimeError):
    pass


@dataclass(frozen=True)
class LoadedManifest:
    path: Path
    data: dict[str, Any]
    pointer_path: Path | None


def run_git(args: list[str]) -> str:
    result = subprocess.run(
        ["git", *args],
        cwd=ROOT,
        check=True,
        text=True,
        encoding="utf-8",
        errors="replace",
        stdout=subprocess.PIPE,
    )
    return result.stdout


def git_head() -> str:
    return run_git(["rev-parse", "HEAD"]).strip()


def git_status() -> str:
    return run_git(["status", "--porcelain=v1"])


def git_tracked_files() -> set[str]:
    return {line.strip().replace("\\", "/") for line in run_git(["ls-files"]).splitlines() if line.strip()}


def under_root(path: Path) -> bool:
    resolved = path.resolve(strict=False)
    root = ROOT.resolve(strict=False)
    return root in (resolved, *resolved.parents)


def repo_path(path_text: str) -> Path:
    text = path_text.strip().replace("\\", "/")
    if not text:
        raise ApplyError("empty path")
    if any(char in text for char in "*?[]"):
        raise ApplyError(f"wildcard paths are not allowed: {text}")
    if ".." in Path(text).parts:
        raise ApplyError(f"parent traversal is not allowed: {text}")
    path = ROOT / text
    if not under_root(path):
        raise ApplyError(f"path escapes repo root: {text}")
    return path


def manifest_hash(manifest: dict[str, Any]) -> str:
    return policy.canonical_manifest_hash(manifest)


def read_json(path: Path) -> dict[str, Any]:
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:
        raise ApplyError(f"cannot read JSON {path}: {exc}") from exc
    if not isinstance(data, dict):
        raise ApplyError(f"JSON root must be an object: {path}")
    return data


def load_manifest(path: Path) -> LoadedManifest:
    manifest_arg = path if path.is_absolute() else ROOT / path
    if not under_root(manifest_arg):
        raise ApplyError(f"manifest path escapes repo root: {manifest_arg}")
    payload = read_json(manifest_arg)

    if "manifest_path" in payload and "rows" not in payload:
        manifest_path = repo_path(str(payload.get("manifest_path", "")))
        manifest = read_json(manifest_path)
        if payload.get("report_id") != manifest.get("report_id"):
            raise ApplyError("latest_manifest pointer report_id does not match manifest")
        if payload.get("manifest_hash") != manifest.get("manifest_hash"):
            raise ApplyError("latest_manifest pointer hash does not match manifest")
        if manifest_hash(manifest) != manifest.get("manifest_hash"):
            raise ApplyError("manifest hash does not match canonical payload")
        return LoadedManifest(path=manifest_path, data=manifest, pointer_path=manifest_arg)

    if "rows" not in payload:
        raise ApplyError("manifest must be a full planner manifest or a latest_manifest pointer")
    if manifest_hash(payload) != payload.get("manifest_hash"):
        raise ApplyError("manifest hash does not match canonical payload")
    return LoadedManifest(path=manifest_arg, data=payload, pointer_path=None)


def generated_at_utc(manifest: dict[str, Any]) -> datetime:
    raw = str(manifest.get("generated_at_utc", "") or manifest.get("generated_at", ""))
    if not raw:
        raise ApplyError("manifest missing generated_at_utc")
    value = datetime.fromisoformat(raw.replace("Z", "+00:00"))
    if value.tzinfo is None:
        value = value.replace(tzinfo=UTC)
    return value.astimezone(UTC)


def validate_manifest_context(manifest: dict[str, Any], max_age_hours: int) -> None:
    if str(manifest.get("git_head", "")) != git_head():
        raise ApplyError("current git HEAD does not match planner manifest git_head")
    after_status = str(manifest.get("git_status_porcelain_after_planner", ""))
    current_status = git_status()
    if current_status != after_status:
        raise ApplyError("current git status does not match planner after-status; rerun planner from this worktree")
    age_limit = timedelta(hours=max_age_hours)
    if datetime.now(UTC) - generated_at_utc(manifest) > age_limit:
        raise ApplyError(f"manifest is older than {max_age_hours} hours; rerun planner")


def tracked_match(rel_path: str, tracked: set[str]) -> bool:
    normalized = rel_path.replace("\\", "/").rstrip("/")
    return normalized in tracked or any(item.startswith(normalized + "/") for item in tracked)


def validate_row_static(row: dict[str, Any], protected_rows: list[policy.ProtectedRow], tracked: set[str]) -> None:
    rel_path = str(row.get("path", "")).strip().replace("\\", "/")
    path = repo_path(rel_path)
    protected, protected_match = policy.path_matches_protected(rel_path, protected_rows)
    if protected:
        raise ApplyError(f"manifest row includes protected path {rel_path} via {protected_match}")
    if tracked_match(rel_path, tracked):
        raise ApplyError(f"manifest row includes tracked path: {rel_path}")
    if str(row.get("layout_baseline_keep", "")).lower() == "true" and row.get("planned_action") != "keep":
        raise ApplyError(f"layout baseline row must be kept: {rel_path}")
    action = str(row.get("planned_action", ""))
    if action in {"quarantine", "delete"} and not path.exists():
        raise ApplyError(f"action path no longer exists: {rel_path}")


def live_fingerprint_hash(path: Path) -> str:
    if planner.is_reparse_point(path):
        raise ApplyError(f"action path is a reparse point: {path.relative_to(ROOT).as_posix()}")
    details, permission_denied, reparse_points = planner.scan_path(path)
    if permission_denied:
        raise ApplyError(f"permission denied under action path: {permission_denied}")
    if reparse_points:
        raise ApplyError(f"reparse point under action path: {reparse_points}")
    return planner.fingerprint_hash(details)


def validate_action_fingerprint(row: dict[str, Any]) -> None:
    action = str(row.get("planned_action", ""))
    if action not in {"quarantine", "delete"}:
        return
    path = repo_path(str(row.get("path", "")))
    expected = str(row.get("path_fingerprint_hash", ""))
    current = live_fingerprint_hash(path)
    if not expected or expected != current:
        raise ApplyError(f"path fingerprint changed since dry-run: {row.get('path', '')}")


def assert_live_empty_directory(path: Path, rel_path: str) -> None:
    if not path.exists():
        raise ApplyError(f"delete target no longer exists: {rel_path}")
    if not path.is_dir():
        raise ApplyError(f"delete target is not a directory: {rel_path}")
    if planner.is_reparse_point(path):
        raise ApplyError(f"delete target is a reparse point: {rel_path}")
    try:
        with os.scandir(path) as entries:
            if any(True for _ in entries):
                raise ApplyError(f"delete target is not empty: {rel_path}")
    except PermissionError as exc:
        raise ApplyError(f"delete target permission denied: {rel_path}: {exc}") from exc


def quarantine_target(root: Path, report_id: str, rel_path: str) -> Path:
    target = root / report_id / rel_path.replace("/", "__")
    if not under_root(target):
        raise ApplyError(f"quarantine target escapes repo root: {target}")
    if target.exists():
        raise ApplyError(f"quarantine target already exists: {target.relative_to(ROOT).as_posix()}")
    return target


def append_quarantine_manifest(root: Path, rows: list[dict[str, str]]) -> None:
    if not rows:
        return
    root.mkdir(parents=True, exist_ok=True)
    manifest_path = root / "QUARANTINE_MANIFEST.csv"
    exists = manifest_path.exists()
    with manifest_path.open("a", encoding="utf-8", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=QUARANTINE_MANIFEST_COLUMNS)
        if not exists:
            writer.writeheader()
        for row in rows:
            writer.writerow(row)


def action_rows(manifest: dict[str, Any]) -> list[dict[str, Any]]:
    rows = manifest.get("rows", [])
    if not isinstance(rows, list):
        raise ApplyError("manifest rows must be a list")
    return [row for row in rows if isinstance(row, dict) and row.get("planned_action") in {"quarantine", "delete"}]


def validate_manifest_actions(
    manifest: dict[str, Any],
    allow_delete: bool,
    max_age_hours: int,
) -> list[dict[str, Any]]:
    validate_manifest_context(manifest, max_age_hours)
    protected_rows = policy.load_protected_rows([])
    tracked = git_tracked_files()
    actions = action_rows(manifest)
    for row in manifest.get("rows", []):
        if isinstance(row, dict):
            validate_row_static(row, protected_rows, tracked)
    for row in actions:
        action = str(row.get("planned_action", ""))
        rel_path = str(row.get("path", "")).strip().replace("\\", "/")
        if action == "delete" and not allow_delete:
            raise ApplyError(f"delete row requires --allow-delete: {rel_path}")
        if action == "delete" and int(row.get("file_count", 1) or 1) != 0:
            raise ApplyError(f"delete row is not empty in manifest: {rel_path}")
        validate_action_fingerprint(row)
    return actions


def write_apply_report(report_root: Path, manifest: dict[str, Any], payload: dict[str, Any]) -> Path:
    report_id = str(manifest.get("report_id", "unknown"))
    report_dir = report_root / report_id
    report_dir.mkdir(parents=True, exist_ok=True)
    report_path = report_dir / ("apply_report.json" if payload.get("applied") else "apply_validate_report.json")
    report_path.write_text(json.dumps(payload, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return report_path


def apply_actions(
    manifest: dict[str, Any],
    actions: list[dict[str, Any]],
    quarantine_root: Path,
    allow_delete: bool,
    owner: str,
    expires_days: int,
) -> list[dict[str, str]]:
    moved_rows: list[dict[str, str]] = []
    report_id = str(manifest.get("report_id", "unknown"))
    moved_at = datetime.now(UTC).isoformat()
    expires_at = (datetime.now(UTC) + timedelta(days=expires_days)).date().isoformat()
    for row in actions:
        action = str(row.get("planned_action", ""))
        rel_path = str(row.get("path", "")).strip().replace("\\", "/")
        source = repo_path(rel_path)
        if action == "delete":
            if not allow_delete:
                raise ApplyError(f"delete row requires --allow-delete: {rel_path}")
            assert_live_empty_directory(source, rel_path)
            source.rmdir()
            continue
        if action == "quarantine":
            target = quarantine_target(quarantine_root, report_id, rel_path)
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.move(str(source), str(target))
            moved_rows.append(
                {
                    "original_path": rel_path,
                    "quarantine_path": target.relative_to(ROOT).as_posix(),
                    "reason": str(row.get("evidence_reason", "")),
                    "moved_at": moved_at,
                    "expires_at": expires_at,
                    "owner": owner,
                    "recovery_hint": "manual-only: inspect this row and move the quarantine path back only after confirming it is needed",
                    "final_action": "review_before_delete",
                }
            )
    append_quarantine_manifest(quarantine_root, moved_rows)
    return moved_rows


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Validate or apply a workspace cleanup planner manifest.")
    parser.add_argument("--manifest", default=str(DEFAULT_MANIFEST.relative_to(ROOT)))
    parser.add_argument("--apply", action="store_true", help="perform quarantine/delete actions")
    parser.add_argument("--allow-delete", action="store_true", help="allow permanent deletion of live-empty directories")
    parser.add_argument("--quarantine-root", default=str(DEFAULT_QUARANTINE_ROOT.relative_to(ROOT)))
    parser.add_argument("--report-root", default=str(DEFAULT_REPORT_ROOT.relative_to(ROOT)))
    parser.add_argument("--max-age-hours", type=int, default=24)
    parser.add_argument("--expires-days", type=int, default=14)
    parser.add_argument("--owner", default="codex_workspace_cleanup")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    try:
        loaded = load_manifest(Path(args.manifest))
        actions = validate_manifest_actions(
            loaded.data,
            allow_delete=args.allow_delete,
            max_age_hours=args.max_age_hours,
        )
        before_status = git_status()
        applied_actions: list[dict[str, str]] = []
        if args.apply:
            quarantine_root = repo_path(args.quarantine_root)
            applied_actions = apply_actions(
                loaded.data,
                actions,
                quarantine_root=quarantine_root,
                allow_delete=args.allow_delete,
                owner=args.owner,
                expires_days=args.expires_days,
            )
            after_status = git_status()
            if after_status != before_status:
                raise ApplyError("cleanup apply changed tracked git status; inspect before continuing")
        else:
            after_status = before_status

        report_path = write_apply_report(
            repo_path(args.report_root),
            loaded.data,
            {
                "applied": bool(args.apply),
                "manifest_path": loaded.path.relative_to(ROOT).as_posix(),
                "pointer_path": loaded.pointer_path.relative_to(ROOT).as_posix() if loaded.pointer_path else "",
                "manifest_hash": loaded.data.get("manifest_hash", ""),
                "report_id": loaded.data.get("report_id", ""),
                "action_count": len(actions),
                "actions": [
                    {
                        "path": row.get("path", ""),
                        "planned_action": row.get("planned_action", ""),
                        "classification": row.get("classification", ""),
                    }
                    for row in actions
                ],
                "applied_quarantine_rows": applied_actions,
                "git_status_before_apply": before_status,
                "git_status_after_apply": after_status,
                "generated_at_utc": datetime.now(UTC).isoformat(),
            },
        )
        mode = "applied" if args.apply else "validated"
        print(f"workspace cleanup manifest {mode}; actions={len(actions)} report={report_path.relative_to(ROOT).as_posix()}")
        return 0
    except ApplyError as exc:
        print(f"workspace cleanup apply failed: {exc}")
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
