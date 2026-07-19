from __future__ import annotations

import subprocess
from pathlib import Path

import pytest

import scripts.git_worktree_safety as worktree_safety
from scripts.git_worktree_safety import (
    GitWorktreeSafetyError,
    _cleanup_failed_worktree,
    audit_ref_transition,
    checkout_materialization_lock,
    create_registered_full_temp_worktree,
    create_sparse_worktree,
)
from scripts.validate_git_worktree_safety import validate as validate_git_worktree_safety


def run_git(repo: Path, *args: str) -> str:
    proc = subprocess.run(
        ["git", "-C", str(repo), *args],
        check=True,
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
    )
    return proc.stdout.strip()


def init_repo(tmp_path: Path) -> Path:
    repo = tmp_path / "repo"
    repo.mkdir()
    run_git(repo, "init")
    run_git(repo, "config", "user.email", "tests@example.com")
    run_git(repo, "config", "user.name", "Checkout Safety Tests")
    return repo


def commit_all(repo: Path, message: str) -> str:
    run_git(repo, "add", "-A")
    run_git(repo, "commit", "-m", message)
    return run_git(repo, "rev-parse", "HEAD")


def write(repo: Path, relative: str, value: str) -> None:
    path = repo / relative
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(value, encoding="utf-8")


def remove_worktree(repo: Path, worktree: Path) -> None:
    if worktree.exists():
        run_git(repo, "worktree", "remove", "--force", str(worktree))


def test_audit_allows_same_commit_without_materialization(tmp_path: Path) -> None:
    repo = init_repo(tmp_path)
    write(repo, "scripts/a.py", "print('a')\n")
    head = commit_all(repo, "base")

    result = audit_ref_transition(repo, head)

    assert result.decision == "allow_no_content_change"
    assert result.changed_path_count == 0
    assert result.protected_path_count == 0


def test_audit_blocks_protected_path_materialization(tmp_path: Path) -> None:
    repo = init_repo(tmp_path)
    write(repo, "scripts/a.py", "print('a')\n")
    base = commit_all(repo, "base")
    write(repo, "output/latest/packet.csv", "stock_id\n2330\n")
    target = commit_all(repo, "generated output")
    run_git(repo, "reset", "--hard", base)

    result = audit_ref_transition(repo, target)

    assert result.decision == "block_protected_path_materialization"
    assert result.protected_path_count == 1
    assert result.protected_path_examples == ("output/latest/packet.csv",)


def test_audit_blocks_large_code_only_transition(tmp_path: Path) -> None:
    repo = init_repo(tmp_path)
    write(repo, "scripts/base.py", "BASE = True\n")
    base = commit_all(repo, "base")
    for index in range(6):
        write(repo, f"scripts/change_{index}.py", f"VALUE = {index}\n")
    target = commit_all(repo, "many code files")
    run_git(repo, "reset", "--hard", base)

    result = audit_ref_transition(repo, target, max_changed_paths=5)

    assert result.decision == "block_large_in_place_transition"
    assert result.changed_path_count == 6


def test_sparse_worktree_materializes_only_allowlisted_paths(tmp_path: Path) -> None:
    repo = init_repo(tmp_path)
    write(repo, "AGENTS.md", "rules\n")
    write(repo, ".github/workflows/check.yml", "name: check\n")
    write(repo, "scripts/a.py", "print('a')\n")
    write(repo, "tests/test_a.py", "def test_a(): pass\n")
    write(repo, "config/a.csv", "a\n")
    write(repo, "rules/a.md", "rule\n")
    write(repo, "output/latest/packet.csv", "stock_id\n")
    write(repo, "data/stock_price_history/2330.csv", "date,close\n")
    target = commit_all(repo, "full tree")
    source_status = run_git(repo, "status", "--short", "--branch")
    destination = tmp_path / "sparse-worktree"

    result = create_sparse_worktree(
        repo,
        target,
        destination,
        include_paths=(".github", "AGENTS.md", "config", "rules", "scripts", "tests"),
        branch="codex/test-sparse-guard",
        max_materialized_files=20,
    )
    try:
        assert (destination / "AGENTS.md").exists()
        assert (destination / ".github" / "workflows" / "check.yml").exists()
        assert (destination / "scripts" / "a.py").exists()
        assert (destination / "tests" / "test_a.py").exists()
        assert (destination / "config" / "a.csv").exists()
        assert (destination / "rules" / "a.md").exists()
        assert not (destination / "output").exists()
        assert not (destination / "data").exists()
        assert result.materialized_file_count <= 20
        assert result.checkout_workers == 1
        assert run_git(destination, "status", "--porcelain=v1") == ""
        assert run_git(repo, "rev-parse", "HEAD") == target
        assert run_git(repo, "status", "--short", "--branch") == source_status
    finally:
        remove_worktree(repo, destination)


def test_sparse_worktree_rejects_protected_include(tmp_path: Path) -> None:
    repo = init_repo(tmp_path)
    write(repo, "scripts/a.py", "print('a')\n")
    target = commit_all(repo, "base")

    with pytest.raises(GitWorktreeSafetyError, match="protected high-churn paths"):
        create_sparse_worktree(
            repo,
            target,
            tmp_path / "blocked-worktree",
            include_paths=("scripts", "output/latest"),
        )


def test_sparse_worktree_rejects_existing_destination(tmp_path: Path) -> None:
    repo = init_repo(tmp_path)
    write(repo, "scripts/a.py", "print('a')\n")
    target = commit_all(repo, "base")
    destination = tmp_path / "existing"
    destination.mkdir()

    with pytest.raises(GitWorktreeSafetyError, match="already exists"):
        create_sparse_worktree(repo, target, destination, include_paths=("scripts",))


def test_sparse_worktree_allows_child_of_approved_ntfs_root(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    repo = init_repo(tmp_path)
    write(repo, "scripts/a.py", "print('a')\n")
    target = commit_all(repo, "base")
    system_temp = tmp_path / "isolated-system-temp"
    system_temp.mkdir()
    approved_root = tmp_path / "approved-f-root"
    destination = approved_root / "pilot"
    monkeypatch.setattr(worktree_safety, "_system_temp_root", lambda: system_temp)
    monkeypatch.setattr(worktree_safety, "_filesystem_type", lambda _path: "NTFS")
    monkeypatch.setattr(
        worktree_safety,
        "_approved_sparse_destination_roots",
        lambda: (approved_root,),
    )

    result = create_sparse_worktree(
        repo,
        target,
        destination,
        include_paths=("scripts",),
        branch="codex/test-approved-f-root",
    )
    try:
        assert approved_root.is_dir()
        assert (destination / "scripts" / "a.py").exists()
        assert result.destination == str(destination.resolve())
        assert run_git(destination, "status", "--porcelain=v1") == ""
    finally:
        remove_worktree(repo, destination)


def test_sparse_worktree_rejects_path_outside_approved_root(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    repo = init_repo(tmp_path)
    write(repo, "scripts/a.py", "print('a')\n")
    target = commit_all(repo, "base")
    system_temp = tmp_path / "isolated-system-temp"
    system_temp.mkdir()
    approved_root = tmp_path / "approved-f-root"
    destination = tmp_path / "other-f-path" / "pilot"
    monkeypatch.setattr(worktree_safety, "_system_temp_root", lambda: system_temp)
    monkeypatch.setattr(worktree_safety, "_filesystem_type", lambda _path: "NTFS")
    monkeypatch.setattr(
        worktree_safety,
        "_approved_sparse_destination_roots",
        lambda: (approved_root,),
    )

    with pytest.raises(GitWorktreeSafetyError, match="system temp root.*approved sparse root"):
        create_sparse_worktree(
            repo,
            target,
            destination,
            include_paths=("scripts",),
        )


@pytest.mark.parametrize("drive_root", [Path("C:\\"), Path("F:\\")])
def test_sparse_worktree_rejects_drive_roots(tmp_path: Path, drive_root: Path) -> None:
    repo = init_repo(tmp_path)
    write(repo, "scripts/a.py", "print('a')\n")
    target = commit_all(repo, "base")

    with pytest.raises(GitWorktreeSafetyError, match="must not be a drive root"):
        create_sparse_worktree(
            repo,
            target,
            drive_root,
            include_paths=("scripts",),
        )


def test_sparse_worktree_rejects_approved_root_itself(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    repo = init_repo(tmp_path)
    write(repo, "scripts/a.py", "print('a')\n")
    target = commit_all(repo, "base")
    system_temp = tmp_path / "isolated-system-temp"
    system_temp.mkdir()
    approved_root = tmp_path / "approved-f-root"
    monkeypatch.setattr(worktree_safety, "_system_temp_root", lambda: system_temp)
    monkeypatch.setattr(worktree_safety, "_filesystem_type", lambda _path: "NTFS")
    monkeypatch.setattr(
        worktree_safety,
        "_approved_sparse_destination_roots",
        lambda: (approved_root,),
    )

    with pytest.raises(GitWorktreeSafetyError, match="child of the approved root"):
        create_sparse_worktree(
            repo,
            target,
            approved_root,
            include_paths=("scripts",),
        )


def test_sparse_worktree_rejects_reparse_point(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    repo = init_repo(tmp_path)
    write(repo, "scripts/a.py", "print('a')\n")
    target = commit_all(repo, "base")
    system_temp = tmp_path / "isolated-system-temp"
    system_temp.mkdir()
    approved_root = tmp_path / "approved-f-root"
    destination = approved_root / "reparse-pilot"
    monkeypatch.setattr(worktree_safety, "_system_temp_root", lambda: system_temp)
    monkeypatch.setattr(
        worktree_safety,
        "_approved_sparse_destination_roots",
        lambda: (approved_root,),
    )
    monkeypatch.setattr(
        worktree_safety,
        "_is_reparse_point",
        lambda path: Path(path) == destination,
    )

    with pytest.raises(GitWorktreeSafetyError, match="contains a reparse point"):
        create_sparse_worktree(
            repo,
            target,
            destination,
            include_paths=("scripts",),
        )


def test_sparse_worktree_rejects_non_ntfs_approved_root(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    repo = init_repo(tmp_path)
    write(repo, "scripts/a.py", "print('a')\n")
    target = commit_all(repo, "base")
    system_temp = tmp_path / "isolated-system-temp"
    system_temp.mkdir()
    approved_root = tmp_path / "approved-f-root"
    monkeypatch.setattr(worktree_safety, "_system_temp_root", lambda: system_temp)
    monkeypatch.setattr(worktree_safety, "_filesystem_type", lambda _path: "FAT32")
    monkeypatch.setattr(
        worktree_safety,
        "_approved_sparse_destination_roots",
        lambda: (approved_root,),
    )

    with pytest.raises(GitWorktreeSafetyError, match="must be on NTFS"):
        create_sparse_worktree(
            repo,
            target,
            approved_root / "pilot",
            include_paths=("scripts",),
        )


def test_sparse_worktree_rejects_approved_root_inside_repository(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    repo = init_repo(tmp_path)
    write(repo, "scripts/a.py", "print('a')\n")
    target = commit_all(repo, "base")
    system_temp = tmp_path / "isolated-system-temp"
    system_temp.mkdir()
    approved_root = repo / "docs" / "task-worktrees"
    monkeypatch.setattr(worktree_safety, "_system_temp_root", lambda: system_temp)
    monkeypatch.setattr(
        worktree_safety,
        "_approved_sparse_destination_roots",
        lambda: (approved_root,),
    )

    with pytest.raises(GitWorktreeSafetyError, match="protected repository data/output/docs root"):
        create_sparse_worktree(
            repo,
            target,
            approved_root / "pilot",
            include_paths=("scripts",),
        )


def test_failed_cleanup_refuses_unregistered_directory(tmp_path: Path) -> None:
    repo = init_repo(tmp_path)
    write(repo, "scripts/a.py", "print('a')\n")
    commit_all(repo, "base")
    unregistered = tmp_path / "unregistered"
    unregistered.mkdir()
    marker = unregistered / "keep.txt"
    marker.write_text("keep\n", encoding="utf-8")

    with pytest.raises(GitWorktreeSafetyError, match="automatic deletion was refused"):
        _cleanup_failed_worktree(repo, unregistered)

    assert marker.read_text(encoding="utf-8") == "keep\n"


def test_checkout_lock_fails_closed_instead_of_waiting(tmp_path: Path) -> None:
    repo = init_repo(tmp_path)
    write(repo, "scripts/a.py", "print('a')\n")
    commit_all(repo, "base")

    with checkout_materialization_lock(repo):
        with pytest.raises(GitWorktreeSafetyError, match="already running"):
            with checkout_materialization_lock(repo, timeout_seconds=0.1):
                raise AssertionError("second lock must not be acquired")


def test_registered_full_temp_worktree_materializes_complete_tree(tmp_path: Path) -> None:
    repo = init_repo(tmp_path)
    write(repo, "scripts/a.py", "print('a')\n")
    write(repo, "output/latest/packet.csv", "stock_id\n")
    target = commit_all(repo, "full tree")
    temp_root = tmp_path / "full-worktrees"
    temp_root.mkdir()

    destination = create_registered_full_temp_worktree(
        repo,
        target,
        temp_root,
        leaf_name="origin_main_daily_report_source",
        consumer_id="chatgpt_daily_report_entrypoint",
    )
    try:
        assert (destination / "scripts" / "a.py").exists()
        assert (destination / "output" / "latest" / "packet.csv").exists()
        assert run_git(destination, "status", "--porcelain=v1") == ""
    finally:
        remove_worktree(repo, destination)


def test_registered_full_temp_worktree_stays_under_system_temp(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    repo = init_repo(tmp_path)
    write(repo, "scripts/a.py", "print('a')\n")
    target = commit_all(repo, "base")
    system_temp = tmp_path / "isolated-system-temp"
    system_temp.mkdir()
    external_root = tmp_path / "external-full-root"
    monkeypatch.setattr(worktree_safety, "_system_temp_root", lambda: system_temp)

    with pytest.raises(GitWorktreeSafetyError, match="must stay under the system temp root"):
        create_registered_full_temp_worktree(
            repo,
            target,
            external_root,
            leaf_name="source",
            consumer_id="chatgpt_daily_report_entrypoint",
        )


def test_unregistered_full_temp_consumer_is_rejected(tmp_path: Path) -> None:
    repo = init_repo(tmp_path)
    write(repo, "scripts/a.py", "print('a')\n")
    target = commit_all(repo, "base")

    with pytest.raises(GitWorktreeSafetyError, match="exactly one contract row"):
        create_registered_full_temp_worktree(
            repo,
            target,
            tmp_path / "full-worktrees",
            leaf_name="source",
            consumer_id="unregistered_consumer",
        )


def test_repository_worktree_safety_contract_is_self_consistent() -> None:
    assert validate_git_worktree_safety() == []
