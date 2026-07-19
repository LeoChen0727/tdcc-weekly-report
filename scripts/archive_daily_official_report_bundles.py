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
VALID_EXECUTION_MODES = frozenset({"validate_only", "copy", "move_after_verify"})


class ArchiveError(RuntimeError):
    pass


class VerifiedTransferError(ArchiveError):
    def __init__(
        self,
        message: str,
        *,
        files: tuple[FileEvidence, ...],
        removed_count: int,
    ) -> None:
        super().__init__(message)
        self.files = files
        self.removed_count = removed_count


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
    archive_index_relative_path: str
    default_mode: str
    copy_mode_source_mutation_forbidden: bool
    verified_transfer_enabled: bool
    pre_delete_manifest_required: bool


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
    artifact_type: str = ""
    protected_path_result: str = "pending"
    preflight_destination_status: str = "pending"
    destination_parity: str = "pending"
    delete_ready: bool = False
    copy_action: str = "pending"
    destination_sha256: str = ""
    source_sha256_after: str = ""
    source_deletion_status: str = "not_requested"
    status: str = "pending"
    error: str = ""


@dataclass(frozen=True)
class ArchivePlan:
    authority: AuthorityState
    current_date: str
    baseline_date: str
    eligible_dates: tuple[str, ...]
    selected_dates: tuple[str, ...]
    empty_selected_dates: tuple[str, ...]
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
    execution_id: str
    pre_delete_manifest_path: Path | None
    pre_delete_manifest_sha256: str
    archive_index_path: Path | None
    archive_index_sha256: str
    source_files_deleted: int


StorageProbe = Callable[[Path], StorageInfo]
CopyFunction = Callable[[FileEvidence], tuple[str, str]]
DeleteFunction = Callable[[Path], None]
PreDeleteHook = Callable[[Path], None]


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
    if payload.get("contract_version") != 2:
        raise ArchiveError("archive contract_version must be 2")
    if payload.get("default_mode") != "validate_only":
        raise ArchiveError("archive contract default_mode must be validate_only")
    if payload.get("copy_mode_source_mutation_forbidden") is not True:
        raise ArchiveError("archive contract must forbid source mutation in copy mode")
    if payload.get("verified_transfer_enabled") is not True:
        raise ArchiveError("archive contract must explicitly enable verified transfer")
    if payload.get("verified_transfer_mode") != "move_after_verify":
        raise ArchiveError("archive contract verified_transfer_mode must be move_after_verify")
    if payload.get("source_removal_scope") != "manifest_exact_older_bundle_files_only":
        raise ArchiveError("archive contract source_removal_scope is not sufficiently bounded")
    if payload.get("pre_delete_manifest_required") is not True:
        raise ArchiveError("archive contract must require a pre-delete manifest")
    if payload.get("archive_index_required") is not True:
        raise ArchiveError("archive contract must require an authoritative archive index")
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
        archive_index_relative_path=str(payload["archive_index_relative_path"]),
        default_mode=str(payload["default_mode"]),
        copy_mode_source_mutation_forbidden=bool(
            payload["copy_mode_source_mutation_forbidden"]
        ),
        verified_transfer_enabled=bool(payload["verified_transfer_enabled"]),
        pre_delete_manifest_required=bool(payload["pre_delete_manifest_required"]),
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
                    artifact_type=suffix.lstrip("."),
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
    dates_with_files = {item.report_date for item in all_files}
    empty_selected_dates = tuple(
        date for date in selected_dates if date not in dates_with_files
    )
    selected_files = tuple(
        replace(
            item,
            retention_reason=(
                f"older_than_contract_baseline:{baseline_date};"
                f"current_authority:{current_date};report_family:{contract.report_family}"
            ),
            protected_path_result=(
                f"eligible_older_bundle;not_current:{current_date};"
                f"not_baseline:{baseline_date}"
            ),
        )
        for item in all_files
        if item.report_date in selected_set
    )
    if not selected_files and not empty_selected_dates:
        raise ArchiveError("archive selection contains no eligible artifacts")
    fingerprint, file_count, total_bytes = source_tree_fingerprint(all_files)
    return ArchivePlan(
        authority=authority,
        current_date=current_date,
        baseline_date=baseline_date,
        eligible_dates=eligible_dates,
        selected_dates=selected_dates,
        empty_selected_dates=empty_selected_dates,
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


def preflight_destinations(
    files: Iterable[FileEvidence], destination_root: Path
) -> tuple[FileEvidence, ...]:
    destination_keys: set[str] = set()
    prepared: list[FileEvidence] = []
    for item in files:
        resolved_destination = item.destination_path.resolve(strict=False)
        if not is_under(resolved_destination, destination_root):
            raise ArchiveError(
                f"archive destination escaped its authorized root: {item.destination_path}"
            )
        current = item.destination_path.parent
        while current.exists() and current.resolve() != destination_root.resolve():
            if is_reparse_point(current):
                raise ArchiveError(f"archive destination parent is a reparse point: {current}")
            current = current.parent
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
                    destination_parity="sha256_match",
                    delete_ready=True,
                )
            )
        else:
            prepared.append(
                replace(
                    item,
                    preflight_destination_status="destination_absent",
                    destination_parity="destination_absent",
                    delete_ready=False,
                )
            )
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


def canonical_json_sha256(payload: object) -> str:
    encoded = json.dumps(
        payload,
        ensure_ascii=False,
        sort_keys=True,
        separators=(",", ":"),
    ).encode("utf-8")
    return hashlib.sha256(encoded).hexdigest()


def archive_index_path(destination_root: Path, contract: ArchiveContract) -> Path:
    relative = Path(contract.archive_index_relative_path)
    if relative.is_absolute() or ".." in relative.parts:
        raise ArchiveError("archive index path must be a safe relative path")
    path = destination_root / relative
    if not is_under(path, destination_root):
        raise ArchiveError("archive index path escaped the destination root")
    return path


def load_archive_index(path: Path, contract: ArchiveContract) -> dict[str, object]:
    if not path.exists():
        return {
            "schema_version": 1,
            "report_family": contract.report_family,
            "entries": [],
        }
    if not path.is_file() or is_reparse_point(path):
        raise ArchiveError(f"archive index is not a regular file: {path}")
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:
        raise ArchiveError(f"archive index is invalid: {path}: {exc}") from exc
    digest = str(payload.pop("archive_index_sha256", ""))
    if not SHA256_RE.fullmatch(digest) or canonical_json_sha256(payload) != digest:
        raise ArchiveError(f"archive index digest validation failed: {path}")
    if payload.get("schema_version") != 1 or payload.get("report_family") != contract.report_family:
        raise ArchiveError(f"archive index contract mismatch: {path}")
    if not isinstance(payload.get("entries"), list):
        raise ArchiveError(f"archive index entries must be a list: {path}")
    return payload


def write_archive_index_atomic(
    destination_root: Path,
    contract: ArchiveContract,
    files: tuple[FileEvidence, ...],
    execution_id: str,
    archived_at_utc: str,
) -> tuple[Path, str]:
    index_path = archive_index_path(destination_root, contract)
    ensure_destination_parent(index_path, destination_root)
    lock_path = index_path.with_name(f".{index_path.name}.lock")
    try:
        lock_fd = os.open(lock_path, os.O_CREAT | os.O_EXCL | os.O_WRONLY)
    except FileExistsError as exc:
        raise ArchiveError(f"archive index writer lock already exists: {lock_path}") from exc
    os.close(lock_fd)
    temporary = index_path.with_name(f".{index_path.name}.tmp-{uuid.uuid4().hex}")
    try:
        payload = load_archive_index(index_path, contract)
        existing: dict[tuple[str, str], dict[str, object]] = {}
        for raw_entry in payload["entries"]:
            if not isinstance(raw_entry, dict):
                raise ArchiveError(f"archive index contains a non-object entry: {index_path}")
            key = (str(raw_entry.get("report_date", "")), str(raw_entry.get("relative_path", "")))
            if key in existing:
                raise ArchiveError(f"archive index contains a duplicate entry: {key}")
            canonical_path = Path(str(raw_entry.get("canonical_archive_path", "")))
            if not canonical_path.is_absolute() or not is_under(canonical_path, destination_root):
                raise ArchiveError(f"archive index contains an invalid canonical path: {canonical_path}")
            existing[key] = dict(raw_entry)

        for item in files:
            if item.destination_parity != "sha256_match":
                raise ArchiveError(
                    f"archive index cannot record an unverified destination: {item.destination_path}"
                )
            canonical_path = item.destination_path.resolve(strict=True)
            if not is_under(canonical_path, destination_root):
                raise ArchiveError(f"archive index destination escaped its root: {canonical_path}")
            destination_size, destination_sha = hash_file_stable(canonical_path)
            if (destination_size, destination_sha) != (item.size_bytes, item.sha256):
                raise ArchiveError(
                    f"archive index destination failed live SHA-256 parity: {canonical_path}"
                )
            key = (item.report_date, item.relative_path.replace(os.sep, "/"))
            prior = existing.get(key)
            if prior is not None:
                immutable_values = {
                    "artifact_type": item.artifact_type,
                    "canonical_archive_path": str(canonical_path),
                    "bytes": item.size_bytes,
                    "sha256": item.sha256,
                }
                for field, expected in immutable_values.items():
                    if prior.get(field) != expected:
                        raise ArchiveError(
                            f"archive index collision for {key}: {field} differs"
                        )
            source_removed = item.source_deletion_status == "removed"
            existing[key] = {
                "report_date": item.report_date,
                "artifact_type": item.artifact_type,
                "relative_path": key[1],
                "canonical_archive_path": str(canonical_path),
                "bytes": item.size_bytes,
                "sha256": item.sha256,
                "source_removed": source_removed,
                "execution_id": execution_id,
                "archived_at": str(
                    prior.get("archived_at", archived_at_utc) if prior else archived_at_utc
                ),
            }

        body: dict[str, object] = {
            "schema_version": 1,
            "report_family": contract.report_family,
            "entries": [existing[key] for key in sorted(existing)],
        }
        digest = canonical_json_sha256(body)
        output = {**body, "archive_index_sha256": digest}
        with temporary.open("x", encoding="utf-8", newline="\n") as handle:
            json.dump(output, handle, ensure_ascii=False, indent=2, sort_keys=True)
            handle.write("\n")
            handle.flush()
            os.fsync(handle.fileno())
        os.replace(temporary, index_path)
        verified = load_archive_index(index_path, contract)
        if canonical_json_sha256(verified) != digest:
            raise ArchiveError(f"archive index post-write verification failed: {index_path}")
        return index_path, digest
    finally:
        if temporary.exists():
            temporary.unlink()
        if lock_path.exists():
            lock_path.unlink()


def pre_delete_manifest_row(
    item: FileEvidence,
    *,
    execution_id: str,
    plan: ArchivePlan,
) -> dict[str, object]:
    return {
        "execution_id": execution_id,
        "source_path": str(item.source_path.resolve(strict=True)),
        "destination_path": str(item.destination_path.resolve(strict=True)),
        "relative_path": item.relative_path.replace(os.sep, "/"),
        "report_date": item.report_date,
        "artifact_type": item.artifact_type,
        "bytes": item.size_bytes,
        "sha256": item.sha256,
        "retention_authority": item.retention_reason,
        "authority_ref": plan.authority.authority_ref,
        "authority_sha": plan.authority.authority_sha,
        "current_date": plan.current_date,
        "baseline_date": plan.baseline_date,
        "protected_path_result": item.protected_path_result,
        "destination_parity": item.destination_parity,
    }


def write_pre_delete_manifest(
    report_dir: Path,
    execution_id: str,
    plan: ArchivePlan,
    files: tuple[FileEvidence, ...],
) -> tuple[Path, str]:
    rows = [
        pre_delete_manifest_row(item, execution_id=execution_id, plan=plan)
        for item in sorted(files, key=lambda value: value.relative_path.casefold())
    ]
    body: dict[str, object] = {
        "schema_version": 1,
        "manifest_type": "daily_official_report_pre_delete_manifest",
        "immutable": True,
        "execution_id": execution_id,
        "report_family": "daily",
        "authority_ref": plan.authority.authority_ref,
        "authority_sha": plan.authority.authority_sha,
        "current_date": plan.current_date,
        "baseline_date": plan.baseline_date,
        "selected_dates": list(plan.selected_dates),
        "rows": rows,
    }
    digest = canonical_json_sha256(body)
    output = {
        **body,
        "manifest_digest_algorithm": "sha256_canonical_json",
        "manifest_digest": digest,
    }
    path = report_dir / (
        f"daily_official_report_pre_delete_{execution_id}_{digest[:16]}.json"
    )
    with path.open("x", encoding="utf-8", newline="\n") as handle:
        json.dump(output, handle, ensure_ascii=False, indent=2, sort_keys=True)
        handle.write("\n")
        handle.flush()
        os.fsync(handle.fileno())
    return path, digest


def load_verified_pre_delete_manifest(path: Path, expected_digest: str) -> dict[str, object]:
    if not path.is_file() or is_reparse_point(path):
        raise ArchiveError(f"pre-delete manifest is not a regular file: {path}")
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:
        raise ArchiveError(f"pre-delete manifest is invalid: {path}: {exc}") from exc
    digest = str(payload.pop("manifest_digest", ""))
    algorithm = payload.pop("manifest_digest_algorithm", "")
    if algorithm != "sha256_canonical_json" or digest != expected_digest:
        raise ArchiveError(f"pre-delete manifest declared digest mismatch: {path}")
    if canonical_json_sha256(payload) != expected_digest:
        raise ArchiveError(f"pre-delete manifest content digest mismatch: {path}")
    return payload


def validate_live_retention_boundary(
    *,
    repo_root: Path,
    source_root: Path,
    authority_ref: str,
    contract: ArchiveContract,
    plan: ArchivePlan,
    injected_authority: AuthorityState | None,
) -> None:
    authority = injected_authority or load_authority_state(repo_root, authority_ref, contract)
    if authority.authority_sha != plan.authority.authority_sha or authority.current_date != plan.current_date:
        raise ArchiveError("retention authority changed after archive planning")
    date_dirs = {
        child.name: child
        for child in source_root.iterdir()
        if child.is_dir() and DATE_RE.fullmatch(child.name)
    }
    dates = sorted(date_dirs)
    if len(dates) < 2 or dates[-1] != plan.current_date or dates[-2] != plan.baseline_date:
        raise ArchiveError("live current/baseline source boundary changed before deletion")
    validate_retained_bundle(
        date_dirs[plan.current_date],
        plan.current_date,
        contract,
        contract.required_current_pdf_count,
    )
    validate_retained_bundle(
        date_dirs[plan.baseline_date],
        plan.baseline_date,
        contract,
        contract.required_baseline_pdf_count,
    )


def validate_bundle_before_deletion(
    *,
    source_root: Path,
    destination_root: Path,
    report_date: str,
    files: tuple[FileEvidence, ...],
    plan: ArchivePlan,
    manifest_payload: dict[str, object],
) -> None:
    if report_date >= plan.baseline_date or report_date in {plan.current_date, plan.baseline_date}:
        raise ArchiveError(f"protected report date cannot be removed: {report_date}")
    bundle_dir = source_root / report_date
    if not bundle_dir.is_dir() or is_reparse_point(bundle_dir):
        raise ArchiveError(f"source bundle is missing or reparse-backed: {bundle_dir}")
    if bundle_dir.parent.resolve() != source_root.resolve():
        raise ArchiveError(f"source bundle is not a direct child of the source root: {bundle_dir}")
    ensure_no_reparse_descendants(bundle_dir)
    actual_paths = {
        str(path.resolve())
        for path in bundle_dir.rglob("*")
        if path.is_file()
    }
    expected_paths = {str(item.source_path.resolve(strict=True)) for item in files}
    if actual_paths != expected_paths:
        missing = sorted(expected_paths.difference(actual_paths))
        unlisted = sorted(actual_paths.difference(expected_paths))
        raise ArchiveError(
            f"source bundle differs from the pre-delete manifest: missing={missing} unlisted={unlisted}"
        )
    manifest_rows = manifest_payload.get("rows")
    if not isinstance(manifest_rows, list):
        raise ArchiveError("pre-delete manifest rows are invalid")
    manifest_by_source = {
        str(row.get("source_path", "")): row
        for row in manifest_rows
        if isinstance(row, dict) and row.get("report_date") == report_date
    }
    if set(manifest_by_source) != expected_paths:
        raise ArchiveError(f"pre-delete manifest does not exactly cover bundle {report_date}")
    for item in files:
        row = manifest_by_source[str(item.source_path.resolve(strict=True))]
        expected = pre_delete_manifest_row(
            item,
            execution_id=str(manifest_payload.get("execution_id", "")),
            plan=plan,
        )
        if row != expected:
            raise ArchiveError(f"pre-delete manifest row mismatch: {item.source_path}")
        source_size, source_sha = hash_file_stable(item.source_path)
        destination_size, destination_sha = hash_file_stable(item.destination_path)
        if (source_size, source_sha) != (item.size_bytes, item.sha256):
            raise ArchiveError(f"source changed after copy verification: {item.source_path}")
        if (destination_size, destination_sha) != (item.size_bytes, item.sha256):
            raise ArchiveError(f"destination parity changed before deletion: {item.destination_path}")
        if not is_under(item.destination_path.resolve(), destination_root):
            raise ArchiveError(f"destination escaped its authorized root: {item.destination_path}")


def validate_source_immediately_before_deletion(
    item: FileEvidence,
    *,
    source_root: Path,
    destination_root: Path,
    plan: ArchivePlan,
) -> None:
    if item.report_date >= plan.baseline_date or item.report_date in {
        plan.current_date,
        plan.baseline_date,
    }:
        raise ArchiveError(f"source is no longer older than the protected baseline: {item.source_path}")
    if not item.source_path.is_absolute() or is_reparse_point(item.source_path):
        raise ArchiveError(f"source deletion path is not an absolute regular file: {item.source_path}")
    resolved_source = item.source_path.resolve(strict=True)
    if not is_under(resolved_source, source_root):
        raise ArchiveError(f"source deletion path escaped its authorized root: {resolved_source}")
    relative = resolved_source.relative_to(source_root.resolve())
    if len(relative.parts) < 2 or relative.parts[0] != item.report_date:
        raise ArchiveError(f"source deletion path is outside its dated bundle: {resolved_source}")
    resolved_destination = item.destination_path.resolve(strict=True)
    if not is_under(resolved_destination, destination_root):
        raise ArchiveError(f"destination parity path escaped its authorized root: {resolved_destination}")
    source_size, source_sha = hash_file_stable(resolved_source)
    destination_size, destination_sha = hash_file_stable(resolved_destination)
    if (source_size, source_sha) != (item.size_bytes, item.sha256):
        raise ArchiveError(f"source bytes or SHA changed immediately before deletion: {resolved_source}")
    if (destination_size, destination_sha) != (item.size_bytes, item.sha256):
        raise ArchiveError(f"destination parity failed immediately before deletion: {resolved_destination}")


def validate_empty_bundle_archive_index(
    report_date: str,
    destination_root: Path,
    contract: ArchiveContract,
) -> None:
    index = load_archive_index(archive_index_path(destination_root, contract), contract)
    entries = [
        entry
        for entry in index["entries"]
        if isinstance(entry, dict) and entry.get("report_date") == report_date
    ]
    if not entries:
        raise ArchiveError(
            f"empty source bundle has no prior verified-transfer index evidence: {report_date}"
        )
    for entry in entries:
        if entry.get("source_removed") is not True:
            raise ArchiveError(
                f"empty source bundle index is not fully source_removed: {report_date}"
            )
        destination = Path(str(entry.get("canonical_archive_path", "")))
        if not destination.is_absolute() or not is_under(destination, destination_root):
            raise ArchiveError(f"empty bundle index path escaped destination root: {destination}")
        size_bytes, sha256 = hash_file_stable(destination)
        if size_bytes != int(entry.get("bytes", -1)) or sha256 != entry.get("sha256"):
            raise ArchiveError(f"empty bundle destination parity failed: {destination}")


def delete_source_file_exact(path: Path) -> None:
    path.unlink()


def remove_empty_bundle_directory(bundle_dir: Path, source_root: Path) -> None:
    if bundle_dir.parent.resolve() != source_root.resolve() or not DATE_RE.fullmatch(bundle_dir.name):
        raise ArchiveError(f"refusing to remove an unauthorized bundle directory: {bundle_dir}")
    if is_reparse_point(bundle_dir):
        raise ArchiveError(f"refusing to remove a reparse-backed bundle directory: {bundle_dir}")
    descendants = sorted(
        (path for path in bundle_dir.rglob("*") if path.is_dir()),
        key=lambda path: len(path.relative_to(bundle_dir).parts),
        reverse=True,
    )
    for directory in descendants:
        if is_reparse_point(directory) or not is_under(directory, bundle_dir):
            raise ArchiveError(f"refusing to remove an unsafe bundle subdirectory: {directory}")
        if any(directory.iterdir()):
            raise ArchiveError(f"refusing to remove non-empty bundle subdirectory: {directory}")
        directory.rmdir()
    if any(bundle_dir.iterdir()):
        raise ArchiveError(f"refusing to remove non-empty bundle directory: {bundle_dir}")
    bundle_dir.rmdir()


def delete_verified_bundles(
    *,
    repo_root: Path,
    source_root: Path,
    destination_root: Path,
    authority_ref: str,
    contract: ArchiveContract,
    plan: ArchivePlan,
    files: tuple[FileEvidence, ...],
    pre_delete_manifest_path: Path,
    pre_delete_manifest_sha256: str,
    injected_authority: AuthorityState | None,
    delete_function: DeleteFunction,
) -> tuple[tuple[FileEvidence, ...], int]:
    updated = list(files)
    removed_count = 0
    try:
        for report_date in plan.selected_dates:
            validate_live_retention_boundary(
                repo_root=repo_root,
                source_root=source_root,
                authority_ref=authority_ref,
                contract=contract,
                plan=plan,
                injected_authority=injected_authority,
            )
            payload = load_verified_pre_delete_manifest(
                pre_delete_manifest_path, pre_delete_manifest_sha256
            )
            positions = [
                index for index, item in enumerate(updated) if item.report_date == report_date
            ]
            bundle_files = tuple(updated[index] for index in positions)
            validate_bundle_before_deletion(
                source_root=source_root,
                destination_root=destination_root,
                report_date=report_date,
                files=bundle_files,
                plan=plan,
                manifest_payload=payload,
            )
            if not bundle_files:
                validate_empty_bundle_archive_index(
                    report_date,
                    destination_root,
                    contract,
                )
            for position in positions:
                item = updated[position]
                load_verified_pre_delete_manifest(
                    pre_delete_manifest_path, pre_delete_manifest_sha256
                )
                validate_source_immediately_before_deletion(
                    item,
                    source_root=source_root,
                    destination_root=destination_root,
                    plan=plan,
                )
                try:
                    delete_function(item.source_path)
                except Exception as exc:
                    updated[position] = replace(
                        item,
                        source_deletion_status="delete_failed",
                        status="partial_source_cleanup" if removed_count else "delete_blocked",
                        error=str(exc),
                    )
                    raise
                removed_count += 1
                updated[position] = replace(
                    item,
                    source_deletion_status="removed",
                    status="verified_transfer_complete",
                )
            remove_empty_bundle_directory(source_root / report_date, source_root)
        return tuple(updated), removed_count
    except Exception as exc:
        raise VerifiedTransferError(
            str(exc), files=tuple(updated), removed_count=removed_count
        ) from exc


def execution_row(item: FileEvidence, execution_id: str) -> dict[str, object]:
    return {
        "execution_id": execution_id,
        "relative_path": item.relative_path,
        "artifact_type": item.artifact_type,
        "bytes": item.size_bytes,
        "sha256": item.sha256,
        "source_path": str(item.source_path),
        "destination_path": str(item.destination_path),
        "canonical_archive_path": str(item.destination_path),
        "report_date": item.report_date,
        "retention_reason": item.retention_reason,
        "protected_path_result": item.protected_path_result,
        "preflight_destination_status": item.preflight_destination_status,
        "destination_parity": item.destination_parity,
        "delete_ready": item.delete_ready,
        "copy_action": item.copy_action,
        "destination_sha256": item.destination_sha256,
        "source_sha256_after": item.source_sha256_after,
        "status": item.status,
        "error": item.error,
        "source_deletion_status": item.source_deletion_status,
        "source_move_status": "not_used_exact_delete_only",
    }


def write_execution_evidence(
    report_dir: Path,
    execution_id: str,
    completion_state: str,
    error: str,
    files: tuple[FileEvidence, ...],
    summary: dict[str, object],
) -> tuple[Path, Path]:
    stamp = datetime.now(UTC).strftime("%Y%m%dT%H%M%S%fZ")
    base = f"daily_official_report_archive_{stamp}_{execution_id}"
    manifest_path = report_dir / f"{base}.csv"
    report_path = report_dir / f"{base}.json"
    fieldnames = list(execution_row(files[0], execution_id).keys()) if files else [
        "execution_id",
        "relative_path",
        "artifact_type",
        "bytes",
        "sha256",
        "source_path",
        "destination_path",
        "canonical_archive_path",
        "report_date",
        "retention_reason",
        "protected_path_result",
        "preflight_destination_status",
        "destination_parity",
        "delete_ready",
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
        writer.writerows(execution_row(item, execution_id) for item in files)
    manifest_sha256 = hash_file_stable(manifest_path)[1]
    payload = {
        **summary,
        "execution_id": execution_id,
        "completion_state": completion_state,
        "error": error,
        "execution_manifest_path": str(manifest_path),
        "execution_manifest_sha256": manifest_sha256,
        "execution_report_path": str(report_path),
        "source_files_deleted": int(summary.get("source_files_deleted", 0)),
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
    move_after_verify: bool = False,
    include_dates: Iterable[str] = (),
    storage_probe: StorageProbe = windows_storage_probe,
    authority_state: AuthorityState | None = None,
    copy_function: CopyFunction | None = None,
    delete_function: DeleteFunction | None = None,
    pre_delete_hook: PreDeleteHook | None = None,
) -> ArchiveResult:
    repo_root = repo_root.resolve()
    execution_mode = (
        "move_after_verify" if move_after_verify else "copy" if apply_copy else "validate_only"
    )
    if execution_mode not in VALID_EXECUTION_MODES:
        raise ArchiveError(f"unsupported archive execution mode: {execution_mode}")
    if move_after_verify and not contract.verified_transfer_enabled:
        raise ArchiveError("verified-transfer mode is disabled by contract")
    execution_id = uuid.uuid4().hex
    archived_at_utc = datetime.now(UTC).isoformat()
    completion_state = {
        "validate_only": "validation_failed",
        "copy": "copy_failed",
        "move_after_verify": "verified_transfer_failed",
    }[execution_mode]
    error = ""
    files: tuple[FileEvidence, ...] = ()
    plan: ArchivePlan | None = None
    fingerprint_after = ""
    file_count_after = 0
    total_bytes_after = 0
    storage: StorageInfo | None = None
    source_files_deleted = 0
    pre_delete_manifest_path: Path | None = None
    pre_delete_manifest_sha256 = ""
    index_path: Path | None = None
    index_sha256 = ""
    source_recheck_matches_expected = False
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
        files = preflight_destinations(plan.selected_files, destination_root)
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
        if execution_mode == "validate_only":
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
                            destination_parity="sha256_match",
                            delete_ready=True,
                            source_sha256_after=source_sha_after,
                            source_deletion_status=(
                                "pending" if execution_mode == "move_after_verify" else "not_requested"
                            ),
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
            index_path, index_sha256 = write_archive_index_atomic(
                destination_root,
                contract,
                files,
                execution_id,
                archived_at_utc,
            )
            if execution_mode == "copy":
                completion_state = "copy_complete"
            else:
                pre_delete_manifest_path, pre_delete_manifest_sha256 = write_pre_delete_manifest(
                    report_dir,
                    execution_id,
                    plan,
                    files,
                )
                if pre_delete_hook is not None:
                    pre_delete_hook(pre_delete_manifest_path)
                files, source_files_deleted = delete_verified_bundles(
                    repo_root=repo_root,
                    source_root=source_root,
                    destination_root=destination_root,
                    authority_ref=authority_ref,
                    contract=contract,
                    plan=plan,
                    files=files,
                    pre_delete_manifest_path=pre_delete_manifest_path,
                    pre_delete_manifest_sha256=pre_delete_manifest_sha256,
                    injected_authority=authority_state,
                    delete_function=delete_function or delete_source_file_exact,
                )
                index_path, index_sha256 = write_archive_index_atomic(
                    destination_root,
                    contract,
                    files,
                    execution_id,
                    archived_at_utc,
                )
                completion_state = "verified_transfer_complete"

        _, after_files = scan_source_tree(source_root, destination_root, contract)
        fingerprint_after, file_count_after, total_bytes_after = source_tree_fingerprint(after_files)
        removed_paths = {
            str(item.source_path.resolve(strict=False)).casefold()
            for item in files
            if item.source_deletion_status == "removed"
        }
        expected_after = tuple(
            item
            for item in plan.all_source_files
            if str(item.source_path.resolve(strict=False)).casefold() not in removed_paths
        )
        expected_fingerprint, expected_count, expected_bytes = source_tree_fingerprint(expected_after)
        source_recheck_matches_expected = (
            fingerprint_after == expected_fingerprint
            and file_count_after == expected_count
            and total_bytes_after == expected_bytes
        )
        if not source_recheck_matches_expected:
            raise ArchiveError("source tree changed outside the exact authorized archive operation")
    except VerifiedTransferError as exc:
        files = exc.files
        source_files_deleted = exc.removed_count
        error = str(exc)
        completion_state = (
            "partial_source_cleanup" if source_files_deleted else "verified_transfer_failed"
        )
        if index_path is not None:
            try:
                index_path, index_sha256 = write_archive_index_atomic(
                    destination_root,
                    contract,
                    files,
                    execution_id,
                    archived_at_utc,
                )
            except Exception as index_exc:
                error = f"{error} | archive index update failed: {index_exc}"
    except Exception as exc:
        error = str(exc)
        completion_state = {
            "validate_only": "validation_failed",
            "copy": "copy_failed",
            "move_after_verify": "verified_transfer_failed",
        }[execution_mode]

    if plan is not None and not fingerprint_after:
        try:
            _, after_files = scan_source_tree(source_root, destination_root, contract)
            fingerprint_after, file_count_after, total_bytes_after = source_tree_fingerprint(after_files)
            removed_paths = {
                str(item.source_path.resolve(strict=False)).casefold()
                for item in files
                if item.source_deletion_status == "removed"
            }
            expected_after = tuple(
                item
                for item in plan.all_source_files
                if str(item.source_path.resolve(strict=False)).casefold() not in removed_paths
            )
            expected_fingerprint, expected_count, expected_bytes = source_tree_fingerprint(
                expected_after
            )
            source_recheck_matches_expected = (
                fingerprint_after == expected_fingerprint
                and file_count_after == expected_count
                and total_bytes_after == expected_bytes
            )
            if not source_recheck_matches_expected:
                error = (
                    f"{error} | source recheck differs from exact authorized deletion set"
                ).strip(" |")
        except Exception as fingerprint_exc:
            error = f"{error} | source recheck failed: {fingerprint_exc}".strip(" |")

    summary = {
        "execution_mode": execution_mode,
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
        "empty_selected_dates": list(plan.empty_selected_dates) if plan else [],
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
        "transfer_ready_files": sum(
            item.delete_ready and item.destination_parity == "sha256_match" for item in files
        ),
        "transfer_ready_dates": sorted(
            {
                report_date
                for report_date in (plan.selected_dates if plan else ())
                if all(
                    item.delete_ready and item.destination_parity == "sha256_match"
                    for item in files
                    if item.report_date == report_date
                )
            }
        ),
        "pre_delete_manifest_path": str(pre_delete_manifest_path or ""),
        "pre_delete_manifest_sha256": pre_delete_manifest_sha256,
        "archive_index_path": str(index_path or ""),
        "archive_index_sha256": index_sha256,
        "source_files_deleted": source_files_deleted,
        "source_fingerprint_before": plan.source_fingerprint if plan else "",
        "source_fingerprint_after": fingerprint_after,
        "source_fingerprint_unchanged": bool(
            plan is not None and fingerprint_after == plan.source_fingerprint
        ),
        "source_recheck_matches_exact_authorized_state": source_recheck_matches_expected,
        "source_file_count_before": plan.source_file_count if plan else 0,
        "source_file_count_after": file_count_after,
        "source_total_bytes_before": plan.source_total_bytes if plan else 0,
        "source_total_bytes_after": total_bytes_after,
    }
    try:
        report_dir = require_absolute_directory(report_dir_input, label="execution report directory")
        manifest_path, report_path = write_execution_evidence(
            report_dir,
            execution_id,
            completion_state,
            error,
            files,
            summary,
        )
    except Exception as report_exc:
        raise ArchiveError(
            f"archive execution could not write mandatory evidence: {report_exc}; original_error={error}"
        ) from report_exc

    success = completion_state in {
        "validation_passed",
        "copy_complete",
        "verified_transfer_complete",
    } and not error
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
        execution_id=execution_id,
        pre_delete_manifest_path=pre_delete_manifest_path,
        pre_delete_manifest_sha256=pre_delete_manifest_sha256,
        archive_index_path=index_path,
        archive_index_sha256=index_sha256,
        source_files_deleted=source_files_deleted,
    )


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Validate, copy, or verified-transfer eligible older official daily report bundles."
        )
    )
    parser.add_argument("--source-root", default=str(ROOT / "chatgpt_side_outputs_official"))
    parser.add_argument("--destination-root", required=True)
    parser.add_argument("--execution-report-dir", required=True)
    parser.add_argument("--expected-destination-volume", required=True)
    parser.add_argument("--repo-root", default=str(ROOT))
    parser.add_argument("--authority-ref", default="origin/main")
    parser.add_argument("--contract", default=str(DEFAULT_CONTRACT))
    parser.add_argument("--include-date", action="append", default=[])
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument("--copy", action="store_true", help="copy and verify without deleting sources")
    mode.add_argument(
        "--move-after-verify",
        action="store_true",
        help="copy, verify the complete bundle, write immutable evidence, then delete exact sources",
    )
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
            move_after_verify=bool(args.move_after_verify),
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
    print(f"pre_delete_manifest={result.pre_delete_manifest_path or ''}")
    print(f"archive_index={result.archive_index_path or ''}")
    if result.error:
        print(f"ERROR: {result.error}", file=sys.stderr)
    return 0 if result.success else 1


if __name__ == "__main__":
    raise SystemExit(main())
