from __future__ import annotations

import argparse
import csv
import hashlib
import json
import os
import re
import shutil
import stat
import subprocess
import sys
import tempfile
import time
from contextlib import contextmanager
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Iterator, Sequence


ROOT = Path(__file__).resolve().parents[1]
CONTRACT_PATH = ROOT / "config" / "git_worktree_materialization_contract.csv"
SPARSE_TASK_CONSUMER_ID = "sparse_task_worktree"
LOCAL_VALIDATION_REPLAY_CONSUMER_ID = "local_daily_full_validation_replay"
APPROVED_SPARSE_DESTINATION_ROOT_WINDOWS = (
    r"F:\CodexStorage\task-worktrees\taiwan-stock-recommendation"
)
APPROVED_LOCAL_VALIDATION_REPLAY_ROOT_WINDOWS = (
    r"F:\CodexStorage\validation-replay-workspaces\taiwan-stock-recommendation"
)
APPROVED_SPARSE_DESTINATION_FILESYSTEM = "NTFS"
APPROVED_LOCAL_VALIDATION_REPLAY_FILESYSTEM = "NTFS"
DEFAULT_SPARSE_DESTINATION_POLICY = "approved_root_task_child"
DEFAULT_LOCAL_VALIDATION_REPLAY_DESTINATION_POLICY = "approved_root_task_or_run_child"
MINIMUM_APPROVED_ROOT_FREE_BYTES = 10 * 1024 * 1024 * 1024
MINIMUM_LOCAL_VALIDATION_REPLAY_FREE_BYTES = 20 * 1024 * 1024 * 1024
WINDOWS_FIXED_DRIVE_TYPE = 3
MAX_TASK_NAME_LENGTH = 80
DEFAULT_MAX_CHANGED_PATHS = 250
DEFAULT_MAX_MATERIALIZED_FILES = 2500
DEFAULT_INCLUDE_PATHS = (
    ".github",
    "AGENTS.md",
    "config",
    "docs/rules",
    "rules",
    "scripts",
    "tests",
)
PROTECTED_MATERIALIZATION_PREFIXES = (
    "chatgpt_side_outputs",
    "data/",
    "docs/history/",
    "docs/latest/",
    "output/",
    "published_reports/",
)


class GitWorktreeSafetyError(RuntimeError):
    pass


@dataclass(frozen=True)
class RefTransitionAudit:
    repo_root: str
    current_sha: str
    target_ref: str
    target_sha: str
    dirty_path_count: int
    changed_path_count: int
    protected_path_count: int
    protected_path_examples: tuple[str, ...]
    decision: str
    reason: str


@dataclass(frozen=True)
class SparseWorktreeResult:
    repo_root: str
    destination: str
    destination_mode: str
    task_name: str
    source_ref: str
    source_sha: str
    branch: str
    include_paths: tuple[str, ...]
    materialized_file_count: int
    checkout_workers: int
    status: str


def _run(
    args: Sequence[str],
    *,
    cwd: Path,
    text: bool = True,
) -> subprocess.CompletedProcess[str] | subprocess.CompletedProcess[bytes]:
    return subprocess.run(
        list(args),
        cwd=str(cwd),
        check=False,
        capture_output=True,
        text=text,
        encoding="utf-8" if text else None,
        errors="replace" if text else None,
    )


def _require(
    proc: subprocess.CompletedProcess[str] | subprocess.CompletedProcess[bytes],
    action: str,
) -> str:
    if proc.returncode != 0:
        stderr = proc.stderr.decode("utf-8", errors="replace") if isinstance(proc.stderr, bytes) else proc.stderr
        stdout = proc.stdout.decode("utf-8", errors="replace") if isinstance(proc.stdout, bytes) else proc.stdout
        detail = (stderr or stdout or f"{action} failed").strip()
        raise GitWorktreeSafetyError(f"{action} failed: {detail}")
    if isinstance(proc.stdout, bytes):
        return proc.stdout.decode("utf-8", errors="replace")
    return proc.stdout


def _git(repo_root: Path, *args: str, text: bool = True):
    return _run(["git", "-C", str(repo_root), *args], cwd=repo_root, text=text)


def _normalize_path(value: str) -> str:
    normalized = value.strip().replace("\\", "/")
    while normalized.startswith("./"):
        normalized = normalized[2:]
    return normalized


def _is_protected_path(path: str) -> bool:
    normalized = _normalize_path(path)
    return any(
        normalized == prefix.rstrip("/") or normalized.startswith(prefix)
        for prefix in PROTECTED_MATERIALIZATION_PREFIXES
    )


def _include_materializes_protected_path(path: str) -> bool:
    normalized = _normalize_path(path).rstrip("/")
    if normalized in {"", "."}:
        return True
    return any(
        normalized == protected
        or normalized.startswith(f"{protected}/")
        or protected.startswith(f"{normalized}/")
        for prefix in PROTECTED_MATERIALIZATION_PREFIXES
        if (protected := prefix.rstrip("/"))
    )


def _nul_paths(proc: subprocess.CompletedProcess[bytes], action: str) -> list[str]:
    _require(proc, action)
    assert isinstance(proc.stdout, bytes)
    return [part.decode("utf-8", errors="surrogateescape") for part in proc.stdout.split(b"\0") if part]


def audit_ref_transition(
    repo_root: Path,
    target_ref: str,
    *,
    max_changed_paths: int = DEFAULT_MAX_CHANGED_PATHS,
) -> RefTransitionAudit:
    repo_root = repo_root.resolve()
    current_sha = _require(_git(repo_root, "rev-parse", "HEAD"), "resolve current HEAD").strip()
    target_sha = _require(_git(repo_root, "rev-parse", "--verify", target_ref), f"resolve {target_ref}").strip()
    dirty_paths = _nul_paths(
        _git(repo_root, "status", "--porcelain=v1", "-z", text=False),
        "inspect worktree status",
    )

    if current_sha == target_sha:
        changed_paths: list[str] = []
    else:
        changed_paths = _nul_paths(
            _git(repo_root, "diff", "--name-only", "-z", current_sha, target_sha, text=False),
            "measure ref transition impact",
        )
    protected_paths = sorted(path for path in changed_paths if _is_protected_path(path))

    if dirty_paths:
        decision = "block_dirty_worktree"
        reason = "The fixed worktree is dirty; no ref transition is allowed."
    elif current_sha == target_sha:
        decision = "allow_no_content_change"
        reason = "HEAD already resolves to the target commit, so no tracked file materialization is needed."
    elif protected_paths:
        decision = "block_protected_path_materialization"
        reason = "The transition would rewrite protected high-churn data or output paths."
    elif len(changed_paths) > max_changed_paths:
        decision = "block_large_in_place_transition"
        reason = f"The transition changes {len(changed_paths)} paths, above the limit of {max_changed_paths}."
    else:
        decision = "require_explicit_user_approval"
        reason = "A small in-place transition still requires explicit user approval; a sparse task worktree is preferred."

    return RefTransitionAudit(
        repo_root=str(repo_root),
        current_sha=current_sha,
        target_ref=target_ref,
        target_sha=target_sha,
        dirty_path_count=len(dirty_paths),
        changed_path_count=len(changed_paths),
        protected_path_count=len(protected_paths),
        protected_path_examples=tuple(protected_paths[:20]),
        decision=decision,
        reason=reason,
    )


def _system_temp_root() -> Path:
    return Path(tempfile.gettempdir()).resolve()


def _path_is_within(path: Path, root: Path) -> bool:
    try:
        path.relative_to(root)
        return True
    except ValueError:
        return False


def _is_drive_root(path: Path) -> bool:
    raw = str(path)
    if len(raw) == 3 and raw[1] == ":" and raw[2] in {"/", "\\"}:
        return True
    absolute = Path(os.path.abspath(raw))
    return absolute.parent == absolute


def _absolute_without_resolving(path: Path) -> Path:
    return Path(os.path.abspath(str(path)))


def _is_reparse_point(path: Path) -> bool:
    try:
        metadata = path.lstat()
    except OSError:
        return False
    attributes = getattr(metadata, "st_file_attributes", 0)
    reparse_attribute = getattr(stat, "FILE_ATTRIBUTE_REPARSE_POINT", 0x400)
    return path.is_symlink() or bool(attributes & reparse_attribute)


def _require_no_reparse_points(path: Path) -> None:
    current = path
    while True:
        if _is_reparse_point(current):
            raise GitWorktreeSafetyError(
                f"worktree destination path contains a reparse point: {current}"
            )
        if current.parent == current:
            break
        current = current.parent


def _filesystem_type(path: Path) -> str:
    if os.name != "nt":
        raise GitWorktreeSafetyError("approved non-system-temp worktree roots are supported only on Windows")
    import ctypes
    from ctypes import wintypes

    volume_root = Path(path.anchor)
    if not volume_root.anchor:
        raise GitWorktreeSafetyError(f"approved worktree root has no Windows volume: {path}")
    filesystem_name = ctypes.create_unicode_buffer(261)
    kernel32 = ctypes.WinDLL("kernel32", use_last_error=True)
    get_volume_information = kernel32.GetVolumeInformationW
    get_volume_information.argtypes = (
        wintypes.LPCWSTR,
        wintypes.LPWSTR,
        wintypes.DWORD,
        ctypes.POINTER(wintypes.DWORD),
        ctypes.POINTER(wintypes.DWORD),
        ctypes.POINTER(wintypes.DWORD),
        wintypes.LPWSTR,
        wintypes.DWORD,
    )
    get_volume_information.restype = wintypes.BOOL
    if not get_volume_information(
        str(volume_root),
        None,
        0,
        None,
        None,
        None,
        filesystem_name,
        len(filesystem_name),
    ):
        error_code = ctypes.get_last_error()
        raise GitWorktreeSafetyError(
            f"cannot verify approved worktree root filesystem for {volume_root}: winerror={error_code}"
        )
    return filesystem_name.value.upper()


def _drive_type(path: Path) -> int:
    if os.name != "nt":
        raise GitWorktreeSafetyError(
            "approved local validation replay roots are supported only on Windows"
        )
    import ctypes
    from ctypes import wintypes

    volume_root = Path(path.anchor)
    if not volume_root.anchor:
        raise GitWorktreeSafetyError(
            f"approved local validation replay root has no Windows volume: {path}"
        )
    kernel32 = ctypes.WinDLL("kernel32", use_last_error=True)
    get_drive_type = kernel32.GetDriveTypeW
    get_drive_type.argtypes = (wintypes.LPCWSTR,)
    get_drive_type.restype = wintypes.UINT
    return int(get_drive_type(str(volume_root)))


def _common_git_dir(repo_root: Path) -> Path:
    raw = _require(_git(repo_root, "rev-parse", "--git-common-dir"), "resolve git common directory").strip()
    path = Path(raw)
    if not path.is_absolute():
        path = repo_root / path
    return path.resolve()


def _load_materialization_contract_rows() -> list[dict[str, str]]:
    if not CONTRACT_PATH.exists():
        raise GitWorktreeSafetyError(f"missing worktree materialization contract: {CONTRACT_PATH}")
    with CONTRACT_PATH.open("r", encoding="utf-8-sig", newline="") as handle:
        return [dict(row) for row in csv.DictReader(handle)]


def _load_materialization_contract(consumer_id: str) -> dict[str, str]:
    matching = [
        row
        for row in _load_materialization_contract_rows()
        if row.get("consumer_id", "").strip() == consumer_id
    ]
    if len(matching) != 1:
        raise GitWorktreeSafetyError(
            f"worktree consumer must have exactly one contract row: {consumer_id!r}"
        )
    return matching[0]


def _approved_sparse_destination_roots() -> tuple[Path, ...]:
    row = _load_materialization_contract(SPARSE_TASK_CONSUMER_ID)
    if row.get("materialization_mode", "").strip() != "sparse_task_only":
        raise GitWorktreeSafetyError("sparse task contract must use materialization_mode=sparse_task_only")
    if row.get("temp_root_policy", "").strip() != "system_temp_or_approved_root":
        raise GitWorktreeSafetyError(
            "sparse task contract must use temp_root_policy=system_temp_or_approved_root"
        )
    approved_root = row.get("approved_destination_root", "").strip()
    if approved_root.lower().rstrip("\\/") != APPROVED_SPARSE_DESTINATION_ROOT_WINDOWS.lower():
        raise GitWorktreeSafetyError(
            "sparse task contract approved_destination_root must be exactly "
            f"{APPROVED_SPARSE_DESTINATION_ROOT_WINDOWS}"
        )
    filesystem = row.get("approved_root_filesystem", "").strip().upper()
    if filesystem != APPROVED_SPARSE_DESTINATION_FILESYSTEM:
        raise GitWorktreeSafetyError(
            "sparse task contract approved_root_filesystem must be NTFS"
        )
    if row.get("default_destination_policy", "").strip() != DEFAULT_SPARSE_DESTINATION_POLICY:
        raise GitWorktreeSafetyError(
            "sparse task contract default_destination_policy must be approved_root_task_child"
        )
    try:
        minimum_free_bytes = int(row.get("minimum_free_bytes", "").strip())
    except ValueError as exc:
        raise GitWorktreeSafetyError(
            "sparse task contract minimum_free_bytes must be an integer"
        ) from exc
    if minimum_free_bytes != MINIMUM_APPROVED_ROOT_FREE_BYTES:
        raise GitWorktreeSafetyError(
            f"sparse task contract minimum_free_bytes must be {MINIMUM_APPROVED_ROOT_FREE_BYTES}"
        )
    return (Path(approved_root),)


def _require_full_local_validation_replay_contract(
    consumer_id: str,
) -> dict[str, str]:
    row = _load_materialization_contract(consumer_id)
    if consumer_id != LOCAL_VALIDATION_REPLAY_CONSUMER_ID:
        raise GitWorktreeSafetyError(
            f"consumer is not approved for local validation replay materialization: {consumer_id}"
        )
    expected = {
        "entrypoint": "scripts/run_local_daily_full_validation_replay.py",
        "materialization_mode": "full_local_validation_replay_only",
        "checkout_workers": "1",
        "max_concurrent": "1",
        "temp_root_policy": "approved_root_only",
        "approved_destination_root": APPROVED_LOCAL_VALIDATION_REPLAY_ROOT_WINDOWS,
        "approved_root_filesystem": APPROVED_LOCAL_VALIDATION_REPLAY_FILESYSTEM,
        "default_destination_policy": DEFAULT_LOCAL_VALIDATION_REPLAY_DESTINATION_POLICY,
        "minimum_free_bytes": str(MINIMUM_LOCAL_VALIDATION_REPLAY_FREE_BYTES),
    }
    for key, expected_value in expected.items():
        observed = row.get(key, "").strip()
        if key == "approved_destination_root":
            observed = observed.lower().rstrip("\\/")
            expected_value = expected_value.lower().rstrip("\\/")
        elif key == "approved_root_filesystem":
            observed = observed.upper()
            expected_value = expected_value.upper()
        if observed != expected_value:
            raise GitWorktreeSafetyError(
                f"local validation replay contract {key} mismatch: "
                f"expected={expected_value!r}, observed={observed!r}"
            )
    return row


def approved_local_validation_replay_root(repo_root: Path) -> Path:
    _require_full_local_validation_replay_contract(
        LOCAL_VALIDATION_REPLAY_CONSUMER_ID
    )
    approved_root = _absolute_without_resolving(
        Path(APPROVED_LOCAL_VALIDATION_REPLAY_ROOT_WINDOWS)
    )
    if _is_drive_root(approved_root):
        raise GitWorktreeSafetyError(
            f"approved local validation replay root must not be a drive root: {approved_root}"
        )
    _require_no_reparse_points(approved_root)
    _require_destination_outside_repository_roots(repo_root, approved_root)
    drive_type = _drive_type(approved_root)
    if drive_type != WINDOWS_FIXED_DRIVE_TYPE:
        raise GitWorktreeSafetyError(
            "approved local validation replay root must be on a fixed drive: "
            f"drive_type={drive_type}, root={approved_root}"
        )
    filesystem = _filesystem_type(approved_root)
    if filesystem != APPROVED_LOCAL_VALIDATION_REPLAY_FILESYSTEM:
        raise GitWorktreeSafetyError(
            "approved local validation replay root must be on NTFS: "
            f"found={filesystem or 'unknown'}, root={approved_root}"
        )
    capacity_path = approved_root
    while not capacity_path.exists() and capacity_path.parent != capacity_path:
        capacity_path = capacity_path.parent
    free_bytes = _available_free_bytes(capacity_path)
    if free_bytes < MINIMUM_LOCAL_VALIDATION_REPLAY_FREE_BYTES:
        raise GitWorktreeSafetyError(
            "approved local validation replay root has insufficient free space: "
            f"required={MINIMUM_LOCAL_VALIDATION_REPLAY_FREE_BYTES}, "
            f"available={free_bytes}, root={approved_root}"
        )
    try:
        approved_root.mkdir(parents=True, exist_ok=True)
    except OSError as exc:
        raise GitWorktreeSafetyError(
            f"cannot create approved local validation replay root {approved_root}: {exc}"
        ) from exc
    _require_no_reparse_points(approved_root)
    if not approved_root.is_dir():
        raise GitWorktreeSafetyError(
            f"approved local validation replay root is not a directory: {approved_root}"
        )
    return approved_root.resolve()


def _registered_worktree_paths(repo_root: Path) -> tuple[Path, ...]:
    output = _require(
        _git(repo_root, "worktree", "list", "--porcelain"),
        "list registered worktrees",
    )
    paths: list[Path] = []
    for line in output.splitlines():
        if line.startswith("worktree "):
            paths.append(Path(line.removeprefix("worktree ")).resolve())
    return tuple(paths)


def _require_destination_outside_repository_roots(repo_root: Path, destination: Path) -> None:
    repo_root = repo_root.resolve()
    try:
        relative = destination.relative_to(repo_root)
    except ValueError:
        relative = None
    if relative is not None:
        first_part = relative.parts[0].lower() if relative.parts else ""
        if first_part in {"data", "docs", "output", "published_reports"} or first_part.startswith(
            "chatgpt_side_outputs"
        ):
            raise GitWorktreeSafetyError(
                "worktree destination must not be inside a protected repository data/output/docs root: "
                f"{destination}"
            )

    common_git_dir = _common_git_dir(repo_root)
    protected_roots = (repo_root, common_git_dir, *_registered_worktree_paths(repo_root))
    for protected_root in protected_roots:
        if _path_is_within(destination, protected_root):
            raise GitWorktreeSafetyError(
                f"worktree destination must not be inside a repository, Git common, or registered worktree root: "
                f"{protected_root}"
            )


def _prepare_approved_sparse_root(repo_root: Path, approved_root: Path) -> Path:
    if _is_drive_root(approved_root):
        raise GitWorktreeSafetyError(
            f"approved worktree root must not be a drive root: {approved_root}"
        )
    approved_root = _absolute_without_resolving(approved_root)
    _require_no_reparse_points(approved_root)
    _require_destination_outside_repository_roots(repo_root, approved_root)
    filesystem = _filesystem_type(approved_root)
    if filesystem != APPROVED_SPARSE_DESTINATION_FILESYSTEM:
        raise GitWorktreeSafetyError(
            f"approved worktree root must be on NTFS, found {filesystem or 'unknown'}: {approved_root}"
        )
    try:
        approved_root.mkdir(parents=True, exist_ok=True)
    except OSError as exc:
        raise GitWorktreeSafetyError(
            f"cannot create approved worktree root {approved_root}: {exc}"
        ) from exc
    _require_no_reparse_points(approved_root)
    if not approved_root.is_dir():
        raise GitWorktreeSafetyError(
            f"approved worktree root is not a directory: {approved_root}"
        )
    free_bytes = _available_free_bytes(approved_root)
    if free_bytes < MINIMUM_APPROVED_ROOT_FREE_BYTES:
        raise GitWorktreeSafetyError(
            "approved worktree root has insufficient free space: "
            f"required={MINIMUM_APPROVED_ROOT_FREE_BYTES}, available={free_bytes}, root={approved_root}"
        )
    return approved_root.resolve()


def _available_free_bytes(path: Path) -> int:
    try:
        return int(shutil.disk_usage(path).free)
    except OSError as exc:
        raise GitWorktreeSafetyError(
            f"cannot verify approved worktree root free space for {path}: {exc}"
        ) from exc


def _sanitize_task_name(task_name: str, branch: str) -> str:
    raw = task_name.strip() or branch.strip()
    if not raw:
        raise GitWorktreeSafetyError(
            "omitting --destination requires --task-name or --branch for a traceable F-drive child"
        )
    if raw.lower().startswith("refs/heads/"):
        raw = raw[len("refs/heads/") :]
    if raw.lower().startswith("codex/"):
        raw = raw[len("codex/") :]
    normalized = raw.lower().replace("\\", "/")
    slug = re.sub(r"[^a-z0-9._-]+", "-", normalized)
    slug = re.sub(r"-+", "-", slug).strip(" ._-")
    if not slug:
        raise GitWorktreeSafetyError("task name is empty after sanitization")
    if len(slug) > MAX_TASK_NAME_LENGTH:
        digest = hashlib.sha256(normalized.encode("utf-8")).hexdigest()[:8]
        prefix = slug[: MAX_TASK_NAME_LENGTH - len(digest) - 1].rstrip(" ._-")
        slug = f"{prefix}-{digest}"
    reserved = {
        "aux",
        "con",
        "nul",
        "prn",
        *(f"com{index}" for index in range(1, 10)),
        *(f"lpt{index}" for index in range(1, 10)),
    }
    if slug in reserved or slug in {".", "..", ".git"}:
        raise GitWorktreeSafetyError(f"task name is reserved on Windows: {slug}")
    return slug


def _resolve_sparse_destination(
    repo_root: Path,
    destination: Path | None,
    *,
    approved_sparse_roots: Sequence[Path],
    task_name: str,
    branch: str,
) -> tuple[Path, str, str]:
    if destination is not None:
        if task_name.strip():
            raise GitWorktreeSafetyError(
                "--task-name cannot be combined with an explicit --destination"
            )
        return (
            _require_new_worktree_destination(
                repo_root,
                destination,
                approved_sparse_roots=approved_sparse_roots,
            ),
            "",
            "explicit",
        )
    if len(approved_sparse_roots) != 1:
        raise GitWorktreeSafetyError(
            "default sparse destination requires exactly one approved external root"
        )
    sanitized_task_name = _sanitize_task_name(task_name, branch)
    default_destination = approved_sparse_roots[0] / sanitized_task_name
    return (
        _require_new_worktree_destination(
            repo_root,
            default_destination,
            approved_sparse_roots=approved_sparse_roots,
        ),
        sanitized_task_name,
        "default_approved_root",
    )


def _require_new_worktree_destination(
    repo_root: Path,
    destination: Path,
    *,
    approved_sparse_roots: Sequence[Path] = (),
) -> Path:
    if _is_drive_root(destination):
        raise GitWorktreeSafetyError(
            f"worktree destination must not be a drive root: {destination}"
        )
    destination = _absolute_without_resolving(destination)
    _require_no_reparse_points(destination)
    temp_root = _system_temp_root()

    if destination == temp_root:
        raise GitWorktreeSafetyError("worktree destination must not be the system temp root itself")
    if _path_is_within(destination, temp_root):
        _require_destination_outside_repository_roots(repo_root, destination)
    else:
        matched_root: Path | None = None
        for configured_root in approved_sparse_roots:
            if _is_drive_root(configured_root):
                raise GitWorktreeSafetyError(
                    f"approved worktree root must not be a drive root: {configured_root}"
                )
            configured_root = _absolute_without_resolving(configured_root)
            if destination == configured_root:
                raise GitWorktreeSafetyError(
                    f"worktree destination must be a child of the approved root, not the root itself: "
                    f"{configured_root}"
                )
            if not _path_is_within(destination, configured_root):
                continue
            approved_root = _prepare_approved_sparse_root(repo_root, configured_root)
            if _path_is_within(destination, approved_root):
                matched_root = approved_root
                break
        if matched_root is None:
            allowed = ", ".join(str(root) for root in approved_sparse_roots) or "none"
            raise GitWorktreeSafetyError(
                f"worktree destination must stay under the system temp root {temp_root} or an approved sparse "
                f"root ({allowed}): {destination}"
            )
        _require_no_reparse_points(destination)
        _require_destination_outside_repository_roots(repo_root, destination)

    if destination.exists():
        raise GitWorktreeSafetyError(f"worktree destination already exists: {destination}")
    return destination.resolve(strict=False)


def _lock_path(repo_root: Path) -> Path:
    digest = hashlib.sha256(str(_common_git_dir(repo_root)).lower().encode("utf-8")).hexdigest()[:20]
    return _system_temp_root() / f"codex_git_materialization_{digest}.lock"


@contextmanager
def checkout_materialization_lock(repo_root: Path, *, timeout_seconds: float = 2.0) -> Iterator[Path]:
    lock_path = _lock_path(repo_root)
    lock_path.parent.mkdir(parents=True, exist_ok=True)
    handle = lock_path.open("a+b")
    handle.seek(0, os.SEEK_END)
    if handle.tell() == 0:
        handle.write(b"0")
        handle.flush()

    deadline = time.monotonic() + timeout_seconds
    acquired = False
    try:
        while not acquired:
            handle.seek(0)
            try:
                if os.name == "nt":
                    import msvcrt

                    msvcrt.locking(handle.fileno(), msvcrt.LK_NBLCK, 1)
                else:
                    import fcntl

                    fcntl.flock(handle.fileno(), fcntl.LOCK_EX | fcntl.LOCK_NB)
                acquired = True
            except OSError:
                if time.monotonic() >= deadline:
                    raise GitWorktreeSafetyError(
                        "another checkout materialization is already running for this repository; "
                        "the second checkout was blocked to preserve workstation responsiveness"
                    )
                time.sleep(0.1)
        yield lock_path
    finally:
        if acquired:
            handle.seek(0)
            if os.name == "nt":
                import msvcrt

                msvcrt.locking(handle.fileno(), msvcrt.LK_UNLCK, 1)
            else:
                import fcntl

                fcntl.flock(handle.fileno(), fcntl.LOCK_UN)
        handle.close()


def _cleanup_failed_worktree(repo_root: Path, destination: Path) -> None:
    registered = _git(repo_root, "worktree", "list", "--porcelain")
    if registered.returncode == 0 and str(destination).replace("\\", "/").lower() in str(registered.stdout).replace("\\", "/").lower():
        _git(repo_root, "worktree", "remove", "--force", str(destination))
        return
    if destination.exists():
        raise GitWorktreeSafetyError(
            f"failed worktree is not registered, so automatic deletion was refused: {destination}"
        )


def _materialized_file_count(worktree_root: Path) -> int:
    output = _require(
        _git(worktree_root, "ls-files", "-t", "-z", text=False),
        "count sparse worktree materialized files",
    )
    return sum(1 for item in output.split("\0") if item and not item.startswith("S "))


def _verify_clean_worktree(worktree_root: Path) -> str:
    status = _require(_git(worktree_root, "status", "--short", "--branch"), "verify new worktree status").strip()
    dirty = _require(_git(worktree_root, "status", "--porcelain=v1"), "verify new worktree cleanliness").strip()
    if dirty:
        raise GitWorktreeSafetyError(f"new worktree is unexpectedly dirty: {dirty[:1000]}")
    return status


def create_sparse_worktree(
    repo_root: Path,
    source_ref: str,
    destination: Path | None = None,
    *,
    include_paths: Sequence[str] = DEFAULT_INCLUDE_PATHS,
    branch: str = "",
    task_name: str = "",
    max_materialized_files: int = DEFAULT_MAX_MATERIALIZED_FILES,
) -> SparseWorktreeResult:
    repo_root = repo_root.resolve()
    roots = _approved_sparse_destination_roots()
    destination, resolved_task_name, destination_mode = _resolve_sparse_destination(
        repo_root,
        destination,
        approved_sparse_roots=roots,
        task_name=task_name,
        branch=branch,
    )
    includes = tuple(dict.fromkeys(_normalize_path(path) for path in include_paths if _normalize_path(path)))
    if not includes:
        raise GitWorktreeSafetyError("at least one sparse include path is required")
    protected_includes = sorted(
        path for path in includes if _include_materializes_protected_path(path)
    )
    if protected_includes:
        raise GitWorktreeSafetyError(
            f"sparse task worktree includes protected high-churn paths: {protected_includes}"
        )

    source_sha = _require(_git(repo_root, "rev-parse", "--verify", source_ref), f"resolve {source_ref}").strip()
    add_args = ["worktree", "add", "--no-checkout"]
    if branch:
        add_args.extend(["-b", branch])
    else:
        add_args.append("--detach")
    add_args.extend([str(destination), source_ref])

    with checkout_materialization_lock(repo_root):
        try:
            _require(_git(repo_root, *add_args), "register no-checkout sparse worktree")
            _require(_git(destination, "sparse-checkout", "init", "--cone"), "initialize sparse checkout")
            _require(
                _git(destination, "sparse-checkout", "set", "--", *includes),
                "set sparse checkout paths",
            )
            _require(
                _git(destination, "-c", "checkout.workers=1", "reset", "--hard", "HEAD"),
                "materialize sparse worktree with one checkout worker",
            )
            materialized_count = _materialized_file_count(destination)
            if materialized_count > max_materialized_files:
                raise GitWorktreeSafetyError(
                    f"sparse worktree materialized {materialized_count} files, above limit {max_materialized_files}"
                )
            status = _verify_clean_worktree(destination)
        except Exception:
            _cleanup_failed_worktree(repo_root, destination)
            raise

    return SparseWorktreeResult(
        repo_root=str(repo_root),
        destination=str(destination),
        destination_mode=destination_mode,
        task_name=resolved_task_name,
        source_ref=source_ref,
        source_sha=source_sha,
        branch=branch,
        include_paths=includes,
        materialized_file_count=materialized_count,
        checkout_workers=1,
        status=status,
    )


def _require_full_temp_materialization_contract(consumer_id: str) -> dict[str, str]:
    row = _load_materialization_contract(consumer_id)
    if row.get("materialization_mode", "").strip() != "full_temp_only":
        raise GitWorktreeSafetyError(f"consumer is not approved for full temp materialization: {consumer_id}")
    if row.get("checkout_workers", "").strip() != "1" or row.get("max_concurrent", "").strip() != "1":
        raise GitWorktreeSafetyError(
            f"consumer must use checkout_workers=1 and max_concurrent=1: {consumer_id}"
        )
    if row.get("temp_root_policy", "").strip() != "system_temp_only":
        raise GitWorktreeSafetyError(
            f"full temp consumer must stay system_temp_only: {consumer_id}"
        )
    if (
        row.get("approved_destination_root", "").strip()
        or row.get("approved_root_filesystem", "").strip()
        or row.get("default_destination_policy", "").strip()
        or row.get("minimum_free_bytes", "").strip()
    ):
        raise GitWorktreeSafetyError(
            f"full temp consumer must not define sparse destination settings: {consumer_id}"
        )
    return row


def create_registered_full_temp_worktree(
    repo_root: Path,
    source_ref: str,
    temp_root: Path,
    *,
    leaf_name: str,
    consumer_id: str,
) -> Path:
    _require_full_temp_materialization_contract(consumer_id)
    repo_root = repo_root.resolve()
    temp_root = temp_root.resolve(strict=False)
    destination = _require_new_worktree_destination(repo_root, temp_root / leaf_name)
    _require(_git(repo_root, "rev-parse", "--verify", source_ref), f"resolve {source_ref}")

    with checkout_materialization_lock(repo_root):
        try:
            _require(
                _git(repo_root, "worktree", "add", "--no-checkout", "--detach", str(destination), source_ref),
                "register no-checkout full temp worktree",
            )
            _require(
                _git(destination, "-c", "checkout.workers=1", "reset", "--hard", "HEAD"),
                "materialize registered full temp worktree with one checkout worker",
            )
            _verify_clean_worktree(destination)
        except Exception:
            _cleanup_failed_worktree(repo_root, destination)
            raise
    return destination


def create_registered_full_local_validation_replay_worktree(
    repo_root: Path,
    source_ref: str,
    destination: Path,
    *,
    consumer_id: str = LOCAL_VALIDATION_REPLAY_CONSUMER_ID,
) -> Path:
    _require_full_local_validation_replay_contract(consumer_id)
    repo_root = repo_root.resolve()
    approved_root = approved_local_validation_replay_root(repo_root)
    destination = _absolute_without_resolving(destination)
    if destination == approved_root or not _path_is_within(destination, approved_root):
        raise GitWorktreeSafetyError(
            "local validation replay full worktree must be a child of the exact "
            f"approved F root {approved_root}: {destination}"
        )
    _require_no_reparse_points(destination)
    _require_destination_outside_repository_roots(repo_root, destination)
    if destination.exists():
        raise GitWorktreeSafetyError(
            f"local validation replay worktree destination already exists: {destination}"
        )
    _require(
        _git(repo_root, "rev-parse", "--verify", source_ref),
        f"resolve {source_ref}",
    )
    with checkout_materialization_lock(repo_root):
        try:
            _require(
                _git(
                    repo_root,
                    "worktree",
                    "add",
                    "--no-checkout",
                    "--detach",
                    str(destination),
                    source_ref,
                ),
                "register no-checkout local validation replay worktree",
            )
            _require(
                _git(
                    destination,
                    "-c",
                    "checkout.workers=1",
                    "reset",
                    "--hard",
                    "HEAD",
                ),
                "materialize local validation replay worktree with one checkout worker",
            )
            _verify_clean_worktree(destination)
        except Exception:
            _cleanup_failed_worktree(repo_root, destination)
            raise
    return destination


def _build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Audit fixed-worktree ref transitions or create a guarded sparse task worktree."
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    audit = subparsers.add_parser("audit", help="Measure and classify an in-place ref transition without switching.")
    audit.add_argument("--repo-root", type=Path, default=Path.cwd())
    audit.add_argument("--target-ref", required=True)
    audit.add_argument("--max-changed-paths", type=int, default=DEFAULT_MAX_CHANGED_PATHS)

    create = subparsers.add_parser("create-sparse", help="Create a temp sparse worktree without full checkout.")
    create.add_argument("--repo-root", type=Path, default=Path.cwd())
    create.add_argument("--source-ref", default="origin/main")
    create.add_argument("--destination", type=Path)
    create.add_argument("--branch", default="")
    create.add_argument("--task-name", default="")
    create.add_argument("--include", action="append", dest="includes")
    create.add_argument("--max-materialized-files", type=int, default=DEFAULT_MAX_MATERIALIZED_FILES)
    return parser


def main() -> int:
    args = _build_parser().parse_args()
    try:
        if args.command == "audit":
            result = audit_ref_transition(
                args.repo_root,
                args.target_ref,
                max_changed_paths=args.max_changed_paths,
            )
            print(json.dumps(asdict(result), ensure_ascii=False, indent=2))
            return 0 if result.decision == "allow_no_content_change" else 2
        result = create_sparse_worktree(
            args.repo_root,
            args.source_ref,
            args.destination,
            include_paths=args.includes or DEFAULT_INCLUDE_PATHS,
            branch=args.branch,
            task_name=args.task_name,
            max_materialized_files=args.max_materialized_files,
        )
        print(json.dumps(asdict(result), ensure_ascii=False, indent=2))
        return 0
    except GitWorktreeSafetyError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
