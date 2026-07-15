from __future__ import annotations

import argparse
import csv
import hashlib
import json
import os
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
DEFAULT_MAX_CHANGED_PATHS = 250
DEFAULT_MAX_MATERIALIZED_FILES = 2500
DEFAULT_INCLUDE_PATHS = (".github", "AGENTS.md", "config", "docs", "rules", "scripts", "tests")
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


def _require_new_temp_destination(destination: Path) -> Path:
    destination = destination.resolve(strict=False)
    temp_root = _system_temp_root()
    try:
        destination.relative_to(temp_root)
    except ValueError as exc:
        raise GitWorktreeSafetyError(
            f"worktree destination must stay under the system temp root {temp_root}: {destination}"
        ) from exc
    if destination == temp_root:
        raise GitWorktreeSafetyError("worktree destination must not be the system temp root itself")
    if destination.exists():
        raise GitWorktreeSafetyError(f"worktree destination already exists: {destination}")
    return destination


def _common_git_dir(repo_root: Path) -> Path:
    raw = _require(_git(repo_root, "rev-parse", "--git-common-dir"), "resolve git common directory").strip()
    path = Path(raw)
    if not path.is_absolute():
        path = repo_root / path
    return path.resolve()


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
    destination: Path,
    *,
    include_paths: Sequence[str] = DEFAULT_INCLUDE_PATHS,
    branch: str = "",
    max_materialized_files: int = DEFAULT_MAX_MATERIALIZED_FILES,
) -> SparseWorktreeResult:
    repo_root = repo_root.resolve()
    destination = _require_new_temp_destination(destination)
    includes = tuple(dict.fromkeys(_normalize_path(path) for path in include_paths if _normalize_path(path)))
    if not includes:
        raise GitWorktreeSafetyError("at least one sparse include path is required")
    protected_includes = sorted(path for path in includes if _is_protected_path(path))
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
        source_ref=source_ref,
        source_sha=source_sha,
        branch=branch,
        include_paths=includes,
        materialized_file_count=materialized_count,
        checkout_workers=1,
        status=status,
    )


def _load_materialization_contract(consumer_id: str) -> dict[str, str]:
    if not CONTRACT_PATH.exists():
        raise GitWorktreeSafetyError(f"missing worktree materialization contract: {CONTRACT_PATH}")
    with CONTRACT_PATH.open("r", encoding="utf-8-sig", newline="") as handle:
        rows = [dict(row) for row in csv.DictReader(handle)]
    matching = [row for row in rows if row.get("consumer_id", "").strip() == consumer_id]
    if len(matching) != 1:
        raise GitWorktreeSafetyError(
            f"full worktree consumer must have exactly one contract row: {consumer_id!r}"
        )
    row = matching[0]
    if row.get("materialization_mode", "").strip() != "full_temp_only":
        raise GitWorktreeSafetyError(f"consumer is not approved for full temp materialization: {consumer_id}")
    if row.get("checkout_workers", "").strip() != "1" or row.get("max_concurrent", "").strip() != "1":
        raise GitWorktreeSafetyError(
            f"consumer must use checkout_workers=1 and max_concurrent=1: {consumer_id}"
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
    _load_materialization_contract(consumer_id)
    repo_root = repo_root.resolve()
    temp_root = temp_root.resolve(strict=False)
    destination = _require_new_temp_destination(temp_root / leaf_name)
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
    create.add_argument("--destination", type=Path, required=True)
    create.add_argument("--branch", default="")
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
            max_materialized_files=args.max_materialized_files,
        )
        print(json.dumps(asdict(result), ensure_ascii=False, indent=2))
        return 0
    except GitWorktreeSafetyError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
