from __future__ import annotations

import argparse
import csv
import ctypes
import hashlib
import json
import os
import re
import shutil
import stat
import subprocess
import sys
import uuid
from dataclasses import dataclass, replace
from datetime import UTC, datetime
from pathlib import Path
from typing import Callable, Iterable


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_CONTRACT = ROOT / "config" / "daily_official_report_archive_contract.json"
DATE_RE = re.compile(r"^20\d{6}$")
SHA256_RE = re.compile(r"^[0-9a-f]{64}$")
SOURCE_MUTATION_FORBIDDEN = True


class ArchiveError(RuntimeError):
    pass


@dataclass(frozen=True)
class ArchiveContract:
    report_family: str
    source_root_name: str
    report_manifest_path: str
    freshness_csv_path: str
    runtime_manifest_name: str
    required_current_pdf_count: int
    required_baseline_pdf_count: int
    allowed_extensions: frozenset[str]
    required_destination_filesystem: str
    free_space_margin_bytes: int


@dataclass(frozen=True)
class AuthorityState:
    current_date: str
    authority_ref: str
    authority_sha: str
    report_manifest_path: str
    freshness_csv_path: str


@dataclass(frozen=True)
class StorageInfo:
    volume: str
    filesystem: str
    free_bytes: int


@dataclass(frozen=True)
class FileEvidence:
    report_date: str
    relative_path: str
    source_path: Path
    destination_path: Path
    size_bytes: int
    sha256: str
    retention_reason: str
    preflight_destination_status: str = "pending"
    copy_action: str = "pending"
    destination_sha256: str = ""
    source_sha256_after: str = ""
    status: str = "pending"
    error: str = ""


@dataclass(frozen=True)
class ArchivePlan:
    authority: AuthorityState
    current_date: str
    baseline_date: str
    eligible_dates: tuple[str, ...]
    selected_dates: tuple[str, ...]
    all_source_files: tuple[FileEvidence, ...]
    selected_files: tuple[FileEvidence, ...]
    source_fingerprint: str
    source_file_count: int
    source_total_bytes: int


@dataclass(frozen=True)
class ArchiveResult:
    success: bool
    completion_state: str
    error: str
    manifest_path: Path
    report_path: Path
    selected_files: tuple[FileEvidence, ...]
    current_date: str
    baseline_date: str
    authority_sha: str
    source_fingerprint_before: str
    source_fingerprint_after: str
    source_file_count_before: int
    source_file_count_after: int
    source_total_bytes_before: int
    source_total_bytes_after: int


StorageProbe = Callable[[Path], StorageInfo]
CopyFunction = Callable[[FileEvidence], tuple[str, str]]


def parse_bool(value: object) -> bool:
    return str(value).strip().lower() in {"1", "true", "yes"}


def normalize_date(value: object, *, label: str) -> str:
    text = re.sub(r"[^0-9]", "", str(value or ""))
    if not DATE_RE.fullmatch(text):
        raise ArchiveError(f"{label} must be an 8-digit report date, got {value!r}")
    return text


def load_contract(path: Path = DEFAULT_CONTRACT) -> ArchiveContract:
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:
        raise ArchiveError(f"cannot read archive contract {path}: {exc}") from exc
    if payload.get("contract_version") != 1:
        raise ArchiveError("archive contract_version must be 1")
    if payload.get("copy_only") is not True or payload.get("source_mutation_forbidden") is not True:
        raise ArchiveError("archive contract must be copy-only and forbid source mutation")
    if payload.get("automation_allowed") is not False:
        raise ArchiveError("archive contract must keep automation disabled")
    if payload.get("execution_report_required") is not True:
        raise ArchiveError("archive contract must require an execution report")
    extensions = frozenset(str(value).lower() for value in payload.get("allowed_extensions", []))
    if extensions != frozenset({".pdf", ".png", ".csv", ".json"}):
        raise ArchiveError("archive contract allowed_extensions must be exactly PDF/PNG/CSV/JSON")
    return ArchiveContract(
        report_family=str(payload["report_family"]),
        source_root_name=str(payload["source_root_name"]),
        report_manifest_path=str(payload["report_manifest_path"]),
        freshness_csv_path=str(payload["freshness_csv_path"]),
        runtime_manifest_name=str(payload["runtime_manifest_name"]),
        required_current_pdf_count=int(payload["required_current_pdf_count"]),
        required_baseline_pdf_count=int(payload["required_baseline_pdf_count"]),
        allowed_extensions=extensions,
        required_destination_filesystem=str(payload["required_destination_filesystem"]),
        free_space_margin_bytes=int(payload["free_space_margin_bytes"]),
    )


def require_absolute_directory(path: Path, *, label: str) -> Path:
    if not path.is_absolute():
        raise ArchiveError(f"{label} must be an absolute path: {path}")
    if not path.exists() or not path.is_dir():
        raise ArchiveError(f"{label} must be an existing directory: {path}")
    if is_reparse_point(path):
        raise ArchiveError(f"{label} must not be a symlink, junction, or reparse point: {path}")
    return path.resolve()


def is_under(path: Path, root: Path) -> bool:
    try:
        path.resolve().relative_to(root.resolve())
        return True
    except ValueError:
        return False


def is_reparse_point(path: Path) -> bool:
    try:
        info = path.lstat()
    except OSError as exc:
        raise ArchiveError(f"cannot inspect path attributes: {path}: {exc}") from exc
    attributes = int(getattr(info, "st_file_attributes", 0))
    marker = int(getattr(stat, "FILE_ATTRIBUTE_REPARSE_POINT", 0x400))
    return path.is_symlink() or bool(attributes & marker)


def ensure_no_reparse_descendants(root: Path) -> None:
    for current, directories, files in os.walk(root, followlinks=False):
        current_path = Path(current)
        for name in [*directories, *files]:
            path = current_path / name
            if is_reparse_point(path):
                raise ArchiveError(f"source contains a symlink, junction, or reparse point: {path}")


def hash_file_stable(path: Path) -> tuple[int, str]:
    if not path.is_file() or is_reparse_point(path):
        raise ArchiveError(f"source artifact is not a regular file: {path}")
    before = path.stat()
    digest = hashlib.sha256()
    try:
        with path.open("rb") as handle:
            for chunk in iter(lambda: handle.read(1024 * 1024), b""):
                digest.update(chunk)
    except OSError as exc:
        raise ArchiveError(f"cannot read source artifact: {path}: {exc}") from exc
    after = path.stat()
    if (before.st_size, before.st_mtime_ns) != (after.st_size, after.st_mtime_ns):
        raise ArchiveError(f"source artifact changed while hashing: {path}")
    return int(after.st_size), digest.hexdigest()


def run_git(repo_root: Path, args: list[str]) -> str:
    result = subprocess.run(
        ["git", *args],
        cwd=repo_root,
        check=False,
        text=True,
        encoding="utf-8-sig",
        errors="replace",
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    if result.returncode != 0:
        raise ArchiveError(f"git {' '.join(args)} failed: {result.stderr.strip()}")
    return result.stdout


def git_show_text(repo_root: Path, authority_ref: str, relative_path: str) -> str:
    normalized = relative_path.replace("\\", "/").lstrip("/")
    return run_git(repo_root, ["show", f"{authority_ref}:{normalized}"])


def load_authority_state(
    repo_root: Path,
    authority_ref: str,
    contract: ArchiveContract,
) -> AuthorityState:
    repo_root = require_absolute_directory(repo_root, label="repo root")
    authority_sha = run_git(repo_root, ["rev-parse", authority_ref]).strip()
    if not re.fullmatch(r"[0-9a-f]{40}", authority_sha):
        raise ArchiveError(f"authority ref did not resolve to a commit SHA: {authority_ref}")
    try:
        report_manifest = json.loads(
            git_show_text(repo_root, authority_sha, contract.report_manifest_path)
        )
    except Exception as exc:
        raise ArchiveError(f"cannot load authoritative report manifest: {exc}") from exc
    if report_manifest.get("report_ready") is not True:
        raise ArchiveError("authoritative report manifest is not report_ready")
    if report_manifest.get("history_path_contract") != "canonical_daily_market_history_only":
        raise ArchiveError("authoritative report manifest has an unexpected history_path_contract")
    current_date = normalize_date(report_manifest.get("main_price_date"), label="manifest main_price_date")

    try:
        freshness_rows = list(
            csv.DictReader(git_show_text(repo_root, authority_sha, contract.freshness_csv_path).splitlines())
        )
    except Exception as exc:
        raise ArchiveError(f"cannot load authoritative freshness CSV: {exc}") from exc
    if len(freshness_rows) != 1:
        raise ArchiveError("authoritative freshness CSV must contain exactly one data row")
    freshness = freshness_rows[0]
    freshness_date = normalize_date(freshness.get("main_price_date"), label="freshness main_price_date")
    if freshness_date != current_date:
        raise ArchiveError(
            f"report manifest and freshness current dates differ: {current_date} != {freshness_date}"
        )
    for field in ("report_ready", "warrant_ready", "daily_pdf_ready"):
        if not parse_bool(freshness.get(field)):
            raise ArchiveError(f"authoritative freshness {field} must be true")

    return AuthorityState(
        current_date=current_date,
        authority_ref=authority_ref,
        authority_sha=authority_sha,
        report_manifest_path=contract.report_manifest_path,
        freshness_csv_path=contract.freshness_csv_path,
    )


def validate_retained_bundle(
    bundle_dir: Path,
    report_date: str,
    contract: ArchiveContract,
    required_pdf_count: int,
) -> None:
    runtime_path = bundle_dir / contract.runtime_manifest_name
    if not runtime_path.is_file() or is_reparse_point(runtime_path):
        raise ArchiveError(f"retained bundle runtime manifest is missing: {runtime_path}")
    try:
        runtime = json.loads(runtime_path.read_text(encoding="utf-8"))
    except Exception as exc:
        raise ArchiveError(f"retained bundle runtime manifest is invalid: {runtime_path}: {exc}") from exc
    required_values = {
        "manifest_type": "chatgpt_daily_report_runtime_manifest",
        "main_price_date": report_date,
        "expected_main_price_date": report_date,
        "source_ref": "origin/main",
        "official_entrypoint": "scripts/run_chatgpt_daily_report_entrypoint.py",
    }
    for field, expected in required_values.items():
        if str(runtime.get(field, "")) != expected:
            raise ArchiveError(
                f"retained bundle runtime manifest {field} must equal {expected}: {runtime_path}"
            )
    for field in ("report_ready", "warrant_ready", "daily_pdf_ready"):
        if runtime.get(field) is not True:
            raise ArchiveError(f"retained bundle runtime manifest {field} must be true: {runtime_path}")
    if int(runtime.get("pdf_count", -1)) != required_pdf_count:
        raise ArchiveError(
            f"retained bundle runtime manifest pdf_count must be {required_pdf_count}: {runtime_path}"
        )
    actual_pdf_count = sum(1 for path in bundle_dir.rglob("*.pdf") if path.is_file())
    if actual_pdf_count != required_pdf_count:
        raise ArchiveError(
            f"retained bundle actual PDF count must be {required_pdf_count}, got {actual_pdf_count}: {bundle_dir}"
        )


def source_tree_fingerprint(files: Iterable[FileEvidence]) -> tuple[str, int, int]:
    rows = sorted(files, key=lambda item: item.relative_path.casefold())
    payload = "\n".join(
        f"{item.relative_path.replace(os.sep, '/')}\t{item.size_bytes}\t{item.sha256}" for item in rows
    ).encode("utf-8")
    return hashlib.sha256(payload).hexdigest(), len(rows), sum(item.size_bytes for item in rows)


def scan_source_tree(
    source_root: Path,
    destination_root: Path,
    contract: ArchiveContract,
) -> tuple[dict[str, Path], tuple[FileEvidence, ...]]:
    ensure_no_reparse_descendants(source_root)
    date_dirs: dict[str, Path] = {}
    unexpected: list[str] = []
    for child in source_root.iterdir():
        if child.is_dir() and DATE_RE.fullmatch(child.name):
            date_dirs[child.name] = child
        else:
            unexpected.append(child.name)
    if unexpected:
        raise ArchiveError(f"official report source root contains unexpected entries: {sorted(unexpected)}")
    if len(date_dirs) < 2:
        raise ArchiveError("official report source root must contain at least current and baseline bundles")

    evidence: list[FileEvidence] = []
    for report_date, bundle_dir in sorted(date_dirs.items()):
        bundle_files = sorted(path for path in bundle_dir.rglob("*") if path.is_file())
        if not bundle_files:
            raise ArchiveError(f"dated report bundle is empty: {bundle_dir}")
        for source_path in bundle_files:
            suffix = source_path.suffix.lower()
            if suffix not in contract.allowed_extensions:
                raise ArchiveError(f"unsupported artifact type in dated bundle: {source_path}")
            relative = source_path.relative_to(source_root)
            if relative.parts[0] != report_date:
                raise ArchiveError(f"dated artifact escaped its report bundle: {source_path}")
            size_bytes, sha256 = hash_file_stable(source_path)
            destination_path = destination_root / contract.report_family / relative
            evidence.append(
                FileEvidence(
                    report_date=report_date,
                    relative_path=str(relative),
                    source_path=source_path,
                    destination_path=destination_path,
                    size_bytes=size_bytes,
                    sha256=sha256,
                    retention_reason="pending_retention_classification",
                )
            )
    return date_dirs, tuple(evidence)


def build_archive_plan(
    source_root: Path,
    destination_root: Path,
    contract: ArchiveContract,
    authority: AuthorityState,
    include_dates: Iterable[str] = (),
) -> ArchivePlan:
    date_dirs, all_files = scan_source_tree(source_root, destination_root, contract)
    dates = sorted(date_dirs)
    current_date = authority.current_date
    if dates[-1] != current_date:
        raise ArchiveError(
            f"authoritative current date must equal newest source bundle: {current_date} != {dates[-1]}"
        )
    baseline_date = dates[-2]
    validate_retained_bundle(
        date_dirs[current_date],
        current_date,
        contract,
        contract.required_current_pdf_count,
    )
    validate_retained_bundle(
        date_dirs[baseline_date],
        baseline_date,
        contract,
        contract.required_baseline_pdf_count,
    )
    eligible_dates = tuple(date for date in dates if date < baseline_date)
    requested = tuple(sorted({normalize_date(value, label="include date") for value in include_dates}))
    if requested:
        invalid = sorted(set(requested).difference(eligible_dates))
        if invalid:
            raise ArchiveError(
                f"requested dates are not older than the retained baseline {baseline_date}: {invalid}"
            )
        selected_dates = requested
    else:
        selected_dates = eligible_dates
    selected_set = set(selected_dates)
    selected_files = tuple(
        replace(
            item,
            retention_reason=(
                f"older_than_contract_baseline:{baseline_date};"
                f"current_authority:{current_date};report_family:{contract.report_family}"
            ),
        )
        for item in all_files
        if item.report_date in selected_set
    )
    if not selected_files:
        raise ArchiveError("archive selection contains no eligible artifacts")
    fingerprint, file_count, total_bytes = source_tree_fingerprint(all_files)
    return ArchivePlan(
        authority=authority,
        current_date=current_date,
        baseline_date=baseline_date,
        eligible_dates=eligible_dates,
        selected_dates=selected_dates,
        all_source_files=all_files,
        selected_files=selected_files,
        source_fingerprint=fingerprint,
        source_file_count=file_count,
        source_total_bytes=total_bytes,
    )


def windows_storage_probe(path: Path) -> StorageInfo:
    if os.name != "nt":
        raise ArchiveError("NTFS destination validation requires Windows")
    existing = path
    while not existing.exists() and existing.parent != existing:
        existing = existing.parent
    if not existing.exists():
        raise ArchiveError(f"cannot locate an existing destination ancestor: {path}")
    volume_buffer = ctypes.create_unicode_buffer(1024)
    if not ctypes.windll.kernel32.GetVolumePathNameW(str(existing), volume_buffer, len(volume_buffer)):
        raise ArchiveError(f"cannot resolve destination volume: {path}")
    filesystem_buffer = ctypes.create_unicode_buffer(256)
    if not ctypes.windll.kernel32.GetVolumeInformationW(
        volume_buffer.value,
        None,
        0,
        None,
        None,
        None,
        filesystem_buffer,
        len(filesystem_buffer),
    ):
        raise ArchiveError(f"cannot read destination filesystem: {path}")
    free_bytes = int(shutil.disk_usage(existing).free)
    return StorageInfo(
        volume=Path(volume_buffer.value).drive.upper(),
        filesystem=filesystem_buffer.value,
        free_bytes=free_bytes,
    )


def validate_roots_and_storage(
    source_root: Path,
    destination_root: Path,
    report_dir: Path,
    expected_destination_volume: str,
    contract: ArchiveContract,
    selected_bytes: int,
    storage_probe: StorageProbe,
) -> StorageInfo:
    if source_root.name != contract.source_root_name:
        raise ArchiveError(
            f"source root name must be {contract.source_root_name}, got {source_root.name}"
        )
    if is_under(destination_root, source_root) or is_under(source_root, destination_root):
        raise ArchiveError("destination root and source root must be disjoint")
    if is_under(report_dir, source_root) or is_under(report_dir, destination_root):
        raise ArchiveError("execution report directory must be outside source and destination roots")
    storage = storage_probe(destination_root)
    expected_volume = expected_destination_volume.rstrip("\\/").upper()
    if not expected_volume:
        raise ArchiveError("expected destination volume is required")
    if storage.volume.rstrip("\\/").upper() != expected_volume:
        raise ArchiveError(
            f"destination volume mismatch: expected {expected_volume}, got {storage.volume}"
        )
    if storage.filesystem.upper() != contract.required_destination_filesystem.upper():
        raise ArchiveError(
            f"destination filesystem must be {contract.required_destination_filesystem}, "
            f"got {storage.filesystem}"
        )
    required_free = selected_bytes + contract.free_space_margin_bytes
    if storage.free_bytes < required_free:
        raise ArchiveError(
            f"destination free space is insufficient: required={required_free} available={storage.free_bytes}"
        )
    return storage


def preflight_destinations(files: Iterable[FileEvidence]) -> tuple[FileEvidence, ...]:
    destination_keys: set[str] = set()
    prepared: list[FileEvidence] = []
    for item in files:
        key = str(item.destination_path.resolve(strict=False)).casefold()
        if key in destination_keys:
            raise ArchiveError(f"duplicate archive destination: {item.destination_path}")
        destination_keys.add(key)
        if item.destination_path.exists():
            if not item.destination_path.is_file() or is_reparse_point(item.destination_path):
                raise ArchiveError(f"archive destination is not a regular file: {item.destination_path}")
            size_bytes, destination_sha = hash_file_stable(item.destination_path)
            if size_bytes != item.size_bytes or destination_sha != item.sha256:
                raise ArchiveError(
                    f"archive destination collision has different content: {item.destination_path}"
                )
            prepared.append(
                replace(
                    item,
                    preflight_destination_status="destination_same_sha",
                    destination_sha256=destination_sha,
                )
            )
        else:
            prepared.append(replace(item, preflight_destination_status="destination_absent"))
    return tuple(prepared)


def ensure_destination_parent(destination: Path, destination_root: Path) -> None:
    destination.parent.mkdir(parents=True, exist_ok=True)
    current = destination.parent
    root = destination_root.resolve()
    while True:
        if is_reparse_point(current):
            raise ArchiveError(f"archive destination parent is a reparse point: {current}")
        if current.resolve() == root:
            break
        if not is_under(current, root):
            raise ArchiveError(f"archive destination escaped its authorized root: {destination}")
        current = current.parent


def copy_candidate_atomic(item: FileEvidence, destination_root: Path) -> tuple[str, str]:
    current_size, current_sha = hash_file_stable(item.source_path)
    if current_size != item.size_bytes or current_sha != item.sha256:
        raise ArchiveError(f"source changed immediately before copy: {item.source_path}")
    if item.destination_path.exists():
        size_bytes, destination_sha = hash_file_stable(item.destination_path)
        if size_bytes != item.size_bytes or destination_sha != item.sha256:
            raise ArchiveError(f"destination collision appeared during copy: {item.destination_path}")
        return "already_present_same_sha", destination_sha

    ensure_destination_parent(item.destination_path, destination_root)
    temporary = item.destination_path.with_name(
        f".{item.destination_path.name}.archive-tmp-{uuid.uuid4().hex}"
    )
    try:
        shutil.copy2(item.source_path, temporary)
        temp_size, temp_sha = hash_file_stable(temporary)
        if temp_size != item.size_bytes or temp_sha != item.sha256:
            raise ArchiveError(f"temporary archive copy failed SHA-256 parity: {temporary}")
        try:
            os.link(temporary, item.destination_path)
        except FileExistsError:
            size_bytes, destination_sha = hash_file_stable(item.destination_path)
            if size_bytes != item.size_bytes or destination_sha != item.sha256:
                raise ArchiveError(f"destination collision appeared during commit: {item.destination_path}")
            return "already_present_same_sha", destination_sha
        destination_size, destination_sha = hash_file_stable(item.destination_path)
        if destination_size != item.size_bytes or destination_sha != item.sha256:
            raise ArchiveError(f"committed archive copy failed SHA-256 parity: {item.destination_path}")
        return "copied_new", destination_sha
    finally:
        if temporary.exists():
            temporary.unlink()


def execution_row(item: FileEvidence) -> dict[str, object]:
    return {
        "relative_path": item.relative_path,
        "bytes": item.size_bytes,
        "sha256": item.sha256,
        "source_path": str(item.source_path),
        "destination_path": str(item.destination_path),
        "report_date": item.report_date,
        "retention_reason": item.retention_reason,
        "preflight_destination_status": item.preflight_destination_status,
        "copy_action": item.copy_action,
        "destination_sha256": item.destination_sha256,
        "source_sha256_after": item.source_sha256_after,
        "status": item.status,
        "error": item.error,
        "source_deletion_status": "not_authorized",
        "source_move_status": "not_authorized",
    }


def write_execution_evidence(
    report_dir: Path,
    completion_state: str,
    error: str,
    files: tuple[FileEvidence, ...],
    summary: dict[str, object],
) -> tuple[Path, Path]:
    stamp = datetime.now(UTC).strftime("%Y%m%dT%H%M%S%fZ")
    nonce = uuid.uuid4().hex[:8]
    base = f"daily_official_report_archive_{stamp}_{nonce}"
    manifest_path = report_dir / f"{base}.csv"
    report_path = report_dir / f"{base}.json"
    fieldnames = list(execution_row(files[0]).keys()) if files else [
        "relative_path",
        "bytes",
        "sha256",
        "source_path",
        "destination_path",
        "report_date",
        "retention_reason",
        "preflight_destination_status",
        "copy_action",
        "destination_sha256",
        "source_sha256_after",
        "status",
        "error",
        "source_deletion_status",
        "source_move_status",
    ]
    with manifest_path.open("x", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(execution_row(item) for item in files)
    manifest_sha256 = hash_file_stable(manifest_path)[1]
    payload = {
        **summary,
        "completion_state": completion_state,
        "error": error,
        "execution_manifest_path": str(manifest_path),
        "execution_manifest_sha256": manifest_sha256,
        "execution_report_path": str(report_path),
        "source_files_deleted": 0,
        "source_files_moved": 0,
        "source_files_renamed": 0,
        "source_files_rewritten": 0,
        "generated_at_utc": datetime.now(UTC).isoformat(),
    }
    report_path.write_text(
        json.dumps(payload, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    return manifest_path, report_path


def execute_archive(
    *,
    repo_root: Path,
    source_root: Path,
    destination_root: Path,
    report_dir: Path,
    expected_destination_volume: str,
    authority_ref: str,
    contract: ArchiveContract,
    apply_copy: bool,
    include_dates: Iterable[str] = (),
    storage_probe: StorageProbe = windows_storage_probe,
    authority_state: AuthorityState | None = None,
    copy_function: CopyFunction | None = None,
) -> ArchiveResult:
    repo_root = repo_root.resolve()
    completion_state = "copy_failed" if apply_copy else "validation_failed"
    error = ""
    files: tuple[FileEvidence, ...] = ()
    plan: ArchivePlan | None = None
    fingerprint_after = ""
    file_count_after = 0
    total_bytes_after = 0
    storage: StorageInfo | None = None
    source_root_input = source_root
    destination_root_input = destination_root
    report_dir_input = report_dir
    try:
        source_root = require_absolute_directory(source_root, label="source root")
        destination_root = require_absolute_directory(destination_root, label="destination root")
        report_dir = require_absolute_directory(report_dir, label="execution report directory")
        authority = authority_state or load_authority_state(repo_root, authority_ref, contract)
        plan = build_archive_plan(
            source_root,
            destination_root,
            contract,
            authority,
            include_dates=include_dates,
        )
        files = plan.selected_files
        files = preflight_destinations(plan.selected_files)
        copy_required_bytes = sum(
            item.size_bytes
            for item in files
            if item.preflight_destination_status == "destination_absent"
        )
        storage = validate_roots_and_storage(
            source_root,
            destination_root,
            report_dir,
            expected_destination_volume,
            contract,
            copy_required_bytes,
            storage_probe,
        )
        if not apply_copy:
            files = tuple(
                replace(
                    item,
                    copy_action="validated_not_copied",
                    source_sha256_after=item.sha256,
                    status="validated",
                )
                for item in files
            )
            completion_state = "validation_passed"
        else:
            copied: list[FileEvidence] = []
            copier = copy_function or (
                lambda item: copy_candidate_atomic(item, destination_root)
            )
            for index, item in enumerate(files):
                try:
                    action, destination_sha = copier(item)
                    source_size_after, source_sha_after = hash_file_stable(item.source_path)
                    if source_size_after != item.size_bytes or source_sha_after != item.sha256:
                        raise ArchiveError(f"source changed during copy: {item.source_path}")
                    copied.append(
                        replace(
                            item,
                            copy_action=action,
                            destination_sha256=destination_sha,
                            source_sha256_after=source_sha_after,
                            status="verified",
                        )
                    )
                except Exception as exc:
                    copied.append(
                        replace(
                            item,
                            copy_action="copy_failed",
                            status="failed",
                            error=str(exc),
                        )
                    )
                    copied.extend(files[index + 1 :])
                    files = tuple(copied)
                    raise
            files = tuple(copied)
            completion_state = "copy_complete"

        _, after_files = scan_source_tree(source_root, destination_root, contract)
        fingerprint_after, file_count_after, total_bytes_after = source_tree_fingerprint(after_files)
        if (
            fingerprint_after != plan.source_fingerprint
            or file_count_after != plan.source_file_count
            or total_bytes_after != plan.source_total_bytes
        ):
            raise ArchiveError("source tree changed during non-destructive archive execution")
    except Exception as exc:
        error = str(exc)
        completion_state = "copy_failed" if apply_copy else "validation_failed"
        if plan is not None and not fingerprint_after:
            try:
                _, after_files = scan_source_tree(source_root, destination_root, contract)
                fingerprint_after, file_count_after, total_bytes_after = source_tree_fingerprint(after_files)
            except Exception as fingerprint_exc:
                error = f"{error} | source recheck failed: {fingerprint_exc}"

    summary = {
        "execution_mode": "copy" if apply_copy else "validate_only",
        "repo_root": str(repo_root),
        "source_root": str(source_root_input),
        "destination_root": str(destination_root_input),
        "report_family": contract.report_family,
        "expected_destination_volume": expected_destination_volume,
        "destination_volume": storage.volume if storage else "",
        "destination_filesystem": storage.filesystem if storage else "",
        "destination_free_bytes": storage.free_bytes if storage else 0,
        "authority_ref": plan.authority.authority_ref if plan else authority_ref,
        "authority_sha": plan.authority.authority_sha if plan else "",
        "current_date": plan.current_date if plan else "",
        "baseline_date": plan.baseline_date if plan else "",
        "eligible_dates": list(plan.eligible_dates) if plan else [],
        "selected_dates": list(plan.selected_dates) if plan else [],
        "selected_files": len(files),
        "selected_bytes": sum(item.size_bytes for item in files),
        "copy_required_bytes": sum(
            item.size_bytes
            for item in files
            if item.preflight_destination_status == "destination_absent"
        ),
        "copied_new_files": sum(item.copy_action == "copied_new" for item in files),
        "already_present_same_sha_files": sum(
            item.copy_action == "already_present_same_sha" for item in files
        ),
        "verified_destination_files": sum(item.status == "verified" for item in files),
        "source_fingerprint_before": plan.source_fingerprint if plan else "",
        "source_fingerprint_after": fingerprint_after,
        "source_fingerprint_unchanged": bool(
            plan is not None and fingerprint_after == plan.source_fingerprint
        ),
        "source_file_count_before": plan.source_file_count if plan else 0,
        "source_file_count_after": file_count_after,
        "source_total_bytes_before": plan.source_total_bytes if plan else 0,
        "source_total_bytes_after": total_bytes_after,
    }
    try:
        report_dir = require_absolute_directory(report_dir_input, label="execution report directory")
        manifest_path, report_path = write_execution_evidence(
            report_dir,
            completion_state,
            error,
            files,
            summary,
        )
    except Exception as report_exc:
        raise ArchiveError(
            f"archive execution could not write mandatory evidence: {report_exc}; original_error={error}"
        ) from report_exc

    success = completion_state in {"validation_passed", "copy_complete"} and not error
    return ArchiveResult(
        success=success,
        completion_state=completion_state,
        error=error,
        manifest_path=manifest_path,
        report_path=report_path,
        selected_files=files,
        current_date=plan.current_date if plan else "",
        baseline_date=plan.baseline_date if plan else "",
        authority_sha=plan.authority.authority_sha if plan else "",
        source_fingerprint_before=plan.source_fingerprint if plan else "",
        source_fingerprint_after=fingerprint_after,
        source_file_count_before=plan.source_file_count if plan else 0,
        source_file_count_after=file_count_after,
        source_total_bytes_before=plan.source_total_bytes if plan else 0,
        source_total_bytes_after=total_bytes_after,
    )


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Copy eligible older official daily report bundles to a verified external archive."
    )
    parser.add_argument("--source-root", default=str(ROOT / "chatgpt_side_outputs_official"))
    parser.add_argument("--destination-root", required=True)
    parser.add_argument("--execution-report-dir", required=True)
    parser.add_argument("--expected-destination-volume", required=True)
    parser.add_argument("--repo-root", default=str(ROOT))
    parser.add_argument("--authority-ref", default="origin/main")
    parser.add_argument("--contract", default=str(DEFAULT_CONTRACT))
    parser.add_argument("--include-date", action="append", default=[])
    parser.add_argument("--copy", action="store_true", help="perform copy-only archive actions")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    try:
        contract = load_contract(Path(args.contract))
        result = execute_archive(
            repo_root=Path(args.repo_root),
            source_root=Path(args.source_root),
            destination_root=Path(args.destination_root),
            report_dir=Path(args.execution_report_dir),
            expected_destination_volume=args.expected_destination_volume,
            authority_ref=args.authority_ref,
            contract=contract,
            apply_copy=bool(args.copy),
            include_dates=args.include_date,
        )
    except Exception as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1
    print(f"completion_state={result.completion_state}")
    print(f"current_date={result.current_date}")
    print(f"baseline_date={result.baseline_date}")
    print(f"authority_sha={result.authority_sha}")
    print(f"execution_manifest={result.manifest_path}")
    print(f"execution_report={result.report_path}")
    if result.error:
        print(f"ERROR: {result.error}", file=sys.stderr)
    return 0 if result.success else 1


if __name__ == "__main__":
    raise SystemExit(main())
