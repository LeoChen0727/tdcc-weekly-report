from __future__ import annotations

import subprocess
from pathlib import Path

import pytest

import scripts.git_worktree_safety as worktree_safety
import scripts.run_local_daily_full_validation_replay as local_replay
from scripts.git_worktree_safety import (
    GitWorktreeSafetyError,
    _cleanup_failed_worktree,
    audit_ref_transition,
    checkout_materialization_lock,
    create_registered_full_temp_worktree,
    create_registered_full_local_validation_replay_worktree,
    create_sparse_worktree,
)
from scripts.validate_git_worktree_safety import validate as validate_git_worktree_safety


@pytest.fixture(autouse=True)
def _approved_root_has_test_capacity(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr(
        worktree_safety,
        "_available_free_bytes",
        lambda _path: worktree_safety.MINIMUM_APPROVED_ROOT_FREE_BYTES,
    )


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
        assert result.destination_mode == "explicit"
        assert result.task_name == ""
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


def test_sparse_worktree_rejects_ancestor_include_of_protected_subtree(tmp_path: Path) -> None:
    repo = init_repo(tmp_path)
    write(repo, "docs/rules/safe.md", "safe\n")
    write(repo, "docs/history/protected.md", "protected\n")
    target = commit_all(repo, "base")

    with pytest.raises(GitWorktreeSafetyError, match="protected high-churn paths"):
        create_sparse_worktree(
            repo,
            target,
            tmp_path / "blocked-ancestor-worktree",
            include_paths=("docs",),
        )


def test_default_sparse_includes_do_not_cover_protected_subtrees() -> None:
    assert "docs/rules" in worktree_safety.DEFAULT_INCLUDE_PATHS
    assert "docs" not in worktree_safety.DEFAULT_INCLUDE_PATHS
    assert all(
        not worktree_safety._include_materializes_protected_path(path)
        for path in worktree_safety.DEFAULT_INCLUDE_PATHS
    )


@pytest.mark.parametrize("include_path", [".", "/"])
def test_sparse_worktree_rejects_whole_tree_include(
    tmp_path: Path,
    include_path: str,
) -> None:
    repo = init_repo(tmp_path)
    write(repo, "scripts/a.py", "print('a')\n")
    target = commit_all(repo, "base")

    with pytest.raises(GitWorktreeSafetyError, match="protected high-churn paths"):
        create_sparse_worktree(
            repo,
            target,
            tmp_path / f"blocked-whole-tree-{include_path.replace('/', 'slash')}",
            include_paths=(include_path,),
        )


def test_sparse_worktree_rejects_existing_destination(tmp_path: Path) -> None:
    repo = init_repo(tmp_path)
    write(repo, "scripts/a.py", "print('a')\n")
    target = commit_all(repo, "base")
    destination = tmp_path / "existing"
    destination.mkdir()

    with pytest.raises(GitWorktreeSafetyError, match="already exists"):
        create_sparse_worktree(repo, target, destination, include_paths=("scripts",))


def test_sparse_worktree_defaults_to_sanitized_approved_root_child(
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

    result = create_sparse_worktree(
        repo,
        target,
        include_paths=("scripts",),
        branch="codex/test-default-child",
        task_name="My Task__Pilot",
    )
    destination = approved_root / "my-task__pilot"
    try:
        assert result.destination == str(destination.resolve())
        assert result.destination_mode == "default_approved_root"
        assert result.task_name == "my-task__pilot"
        assert (destination / "scripts" / "a.py").exists()
        registry = run_git(repo, "worktree", "list", "--porcelain").replace("\\", "/").lower()
        assert str(system_temp).replace("\\", "/").lower() not in registry
    finally:
        remove_worktree(repo, destination)


def test_sparse_worktree_default_requires_traceable_task_identity(
    tmp_path: Path,
) -> None:
    repo = init_repo(tmp_path)
    write(repo, "scripts/a.py", "print('a')\n")
    target = commit_all(repo, "base")

    with pytest.raises(GitWorktreeSafetyError, match="requires --task-name or --branch"):
        create_sparse_worktree(repo, target, include_paths=("scripts",))


def test_branch_derived_task_name_is_deterministic_and_sanitized() -> None:
    assert worktree_safety._sanitize_task_name("", "codex/F Default Pilot") == "f-default-pilot"
    long_name = "Task " + ("x" * 100)
    first = worktree_safety._sanitize_task_name(long_name, "")
    second = worktree_safety._sanitize_task_name(long_name, "")
    assert first == second
    assert len(first) == worktree_safety.MAX_TASK_NAME_LENGTH


def test_sparse_worktree_default_rejects_existing_task_child(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    repo = init_repo(tmp_path)
    write(repo, "scripts/a.py", "print('a')\n")
    target = commit_all(repo, "base")
    system_temp = tmp_path / "isolated-system-temp"
    system_temp.mkdir()
    approved_root = tmp_path / "approved-f-root"
    destination = approved_root / "collision"
    destination.mkdir(parents=True)
    monkeypatch.setattr(worktree_safety, "_system_temp_root", lambda: system_temp)
    monkeypatch.setattr(worktree_safety, "_filesystem_type", lambda _path: "NTFS")
    monkeypatch.setattr(
        worktree_safety,
        "_approved_sparse_destination_roots",
        lambda: (approved_root,),
    )

    with pytest.raises(GitWorktreeSafetyError, match="already exists"):
        create_sparse_worktree(
            repo,
            target,
            include_paths=("scripts",),
            task_name="collision",
        )


def test_sparse_worktree_default_rejects_reparse_task_child(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    repo = init_repo(tmp_path)
    write(repo, "scripts/a.py", "print('a')\n")
    target = commit_all(repo, "base")
    system_temp = tmp_path / "isolated-system-temp"
    system_temp.mkdir()
    approved_root = tmp_path / "approved-f-root"
    destination = approved_root / "reparse-default"
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
            include_paths=("scripts",),
            task_name="reparse-default",
        )


def test_sparse_worktree_default_does_not_fallback_when_f_root_is_unavailable(
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
    monkeypatch.setattr(
        worktree_safety,
        "_approved_sparse_destination_roots",
        lambda: (approved_root,),
    )
    monkeypatch.setattr(
        worktree_safety,
        "_filesystem_type",
        lambda _path: (_ for _ in ()).throw(GitWorktreeSafetyError("F root unavailable")),
    )

    with pytest.raises(GitWorktreeSafetyError, match="F root unavailable"):
        create_sparse_worktree(
            repo,
            target,
            include_paths=("scripts",),
            task_name="no-fallback",
        )

    assert not approved_root.exists()
    registry = run_git(repo, "worktree", "list", "--porcelain").replace("\\", "/").lower()
    assert str(system_temp).replace("\\", "/").lower() not in registry


def test_sparse_worktree_default_rejects_insufficient_f_root_space(
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
    monkeypatch.setattr(
        worktree_safety,
        "_available_free_bytes",
        lambda _path: worktree_safety.MINIMUM_APPROVED_ROOT_FREE_BYTES - 1,
    )

    with pytest.raises(GitWorktreeSafetyError, match="insufficient free space"):
        create_sparse_worktree(
            repo,
            target,
            include_paths=("scripts",),
            task_name="low-space",
        )

    assert not (approved_root / "low-space").exists()
    registry = run_git(repo, "worktree", "list", "--porcelain").replace("\\", "/").lower()
    assert str(system_temp).replace("\\", "/").lower() not in registry


def test_sparse_worktree_default_rejects_approved_root_inside_repository(
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
            include_paths=("scripts",),
            task_name="protected-root",
        )


def test_sparse_worktree_rejects_task_name_with_explicit_destination(
    tmp_path: Path,
) -> None:
    repo = init_repo(tmp_path)
    write(repo, "scripts/a.py", "print('a')\n")
    target = commit_all(repo, "base")

    with pytest.raises(GitWorktreeSafetyError, match="cannot be combined"):
        create_sparse_worktree(
            repo,
            target,
            tmp_path / "explicit",
            include_paths=("scripts",),
            task_name="ambiguous",
        )


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


def local_replay_contract_row(root: Path) -> dict[str, str]:
    return {
        "consumer_id": "local_daily_full_validation_replay",
        "entrypoint": "scripts/run_local_daily_full_validation_replay.py",
        "materialization_mode": "full_local_validation_replay_only",
        "checkout_workers": "1",
        "max_concurrent": "1",
        "temp_root_policy": "approved_root_only",
        "approved_destination_root": str(root),
        "approved_root_filesystem": "NTFS",
        "default_destination_policy": "approved_root_task_or_run_child",
        "minimum_free_bytes": str(
            worktree_safety.MINIMUM_LOCAL_VALIDATION_REPLAY_FREE_BYTES
        ),
        "purpose": "test",
    }


def configure_local_replay_root(
    monkeypatch: pytest.MonkeyPatch,
    root: Path,
) -> None:
    monkeypatch.setattr(
        worktree_safety,
        "APPROVED_LOCAL_VALIDATION_REPLAY_ROOT_WINDOWS",
        str(root),
    )
    monkeypatch.setattr(
        worktree_safety,
        "_load_materialization_contract",
        lambda _consumer: local_replay_contract_row(root),
    )
    monkeypatch.setattr(worktree_safety, "_filesystem_type", lambda _path: "NTFS")
    monkeypatch.setattr(
        worktree_safety,
        "_drive_type",
        lambda _path: worktree_safety.WINDOWS_FIXED_DRIVE_TYPE,
    )
    monkeypatch.setattr(
        worktree_safety,
        "_available_free_bytes",
        lambda _path: worktree_safety.MINIMUM_LOCAL_VALIDATION_REPLAY_FREE_BYTES,
    )


def test_registered_full_local_validation_replay_materializes_complete_tree(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    repo = init_repo(tmp_path)
    write(repo, "scripts/a.py", "print('a')\n")
    write(repo, "output/latest/packet.csv", "stock_id\n")
    target = commit_all(repo, "full tree")
    approved = tmp_path / "f-root"
    configure_local_replay_root(monkeypatch, approved)
    destination = approved / "run-123" / "full-source"
    destination.parent.mkdir(parents=True)
    materialized = create_registered_full_local_validation_replay_worktree(
        repo, target, destination
    )
    try:
        assert (materialized / "scripts/a.py").exists()
        assert (materialized / "output/latest/packet.csv").exists()
        assert run_git(materialized, "status", "--porcelain=v1") == ""
        assert materialized.is_relative_to(approved)
    finally:
        remove_worktree(repo, materialized)


def test_local_replay_pilot_routes_all_large_roots_to_f_without_c_temp(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    repo = init_repo(tmp_path)
    write(repo, "scripts/a.py", "print('a')\n")
    source_sha = commit_all(repo, "source")
    approved = tmp_path / "f-root"
    system_temp = tmp_path / "c-temp"
    system_temp.mkdir()
    configure_local_replay_root(monkeypatch, approved)
    monkeypatch.setattr(
        local_replay,
        "_system_temp_root_for_audit",
        lambda: system_temp,
    )

    def materialize(
        source_repo: Path,
        source_ref: str,
        destination: Path,
        **_kwargs: object,
    ) -> Path:
        run_git(
            source_repo,
            "worktree",
            "add",
            "--detach",
            str(destination),
            source_ref,
        )
        return destination

    monkeypatch.setattr(
        worktree_safety,
        "create_registered_full_local_validation_replay_worktree",
        materialize,
    )
    args = type(
        "Args",
        (),
        {
            "repo_root": repo,
            "source_ref": source_sha,
            "workspace_id": "run-123",
        },
    )()
    assert local_replay.run_pilot(args) == 0
    paths = local_replay.plan_workspace(repo, "run-123")
    payload = local_replay.verify_pilot_manifest(paths)
    assert set(payload["categories"]) == {
        "full_source",
        "synthetic_git_index_objects_metadata",
        "runner_local_temp",
        "pdf_test_render",
        "pdf_text_extract",
        "manifest_evidence",
    }
    for block in payload["categories"].values():
        assert Path(block["root"]).is_relative_to(approved)
        assert block["files"]
    assert payload["source_sha"] == source_sha
    assert payload["source_tree_sha"] == payload["synthetic_tree_sha"]
    assert payload["forbidden_system_temp_replay_paths_after"] == []
    assert list(system_temp.iterdir()) == []
    remove_worktree(repo, paths.source_root)


@pytest.mark.parametrize(
    ("filesystem", "drive_type", "free_bytes", "message"),
    [
        ("NTFS", 2, 40 * 1024**3, "fixed drive"),
        ("exFAT", 3, 40 * 1024**3, "must be on NTFS"),
        ("NTFS", 3, 1, "insufficient free space"),
    ],
)
def test_local_replay_rejects_unavailable_nonfixed_non_ntfs_and_low_space(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    filesystem: str,
    drive_type: int,
    free_bytes: int,
    message: str,
) -> None:
    repo = init_repo(tmp_path)
    approved = tmp_path / "f-root"
    configure_local_replay_root(monkeypatch, approved)
    monkeypatch.setattr(worktree_safety, "_filesystem_type", lambda _path: filesystem)
    monkeypatch.setattr(worktree_safety, "_drive_type", lambda _path: drive_type)
    monkeypatch.setattr(
        worktree_safety, "_available_free_bytes", lambda _path: free_bytes
    )
    with pytest.raises(GitWorktreeSafetyError, match=message):
        worktree_safety.approved_local_validation_replay_root(repo)
    assert not approved.exists()


def test_local_replay_unavailable_f_root_never_falls_back_to_c_temp(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    repo = init_repo(tmp_path)
    approved = tmp_path / "unavailable-f-root"
    system_temp = tmp_path / "c-temp"
    system_temp.mkdir()
    configure_local_replay_root(monkeypatch, approved)
    monkeypatch.setattr(
        worktree_safety,
        "_filesystem_type",
        lambda _path: (_ for _ in ()).throw(
            GitWorktreeSafetyError("F volume unavailable")
        ),
    )
    monkeypatch.setattr(
        local_replay,
        "_system_temp_root_for_audit",
        lambda: system_temp,
    )
    with pytest.raises(GitWorktreeSafetyError, match="F volume unavailable"):
        local_replay.plan_workspace(repo, "run-unavailable")
    assert list(system_temp.iterdir()) == []
    assert not approved.exists()


def test_local_replay_rejects_collision_reparse_and_path_traversal(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    repo = init_repo(tmp_path)
    approved = tmp_path / "f-root"
    configure_local_replay_root(monkeypatch, approved)
    approved.mkdir()
    collision = approved / "run-collision"
    collision.mkdir()
    with pytest.raises(
        local_replay.LocalValidationReplayWorkspaceError,
        match="collision",
    ):
        local_replay.create_workspace(
            repo, source_ref="HEAD", workspace_id="run-collision"
        )
    with pytest.raises(
        local_replay.LocalValidationReplayWorkspaceError,
        match="without traversal",
    ):
        local_replay.plan_workspace(repo, "../escape")
    monkeypatch.setattr(
        worktree_safety,
        "_is_reparse_point",
        lambda path: path == approved,
    )
    with pytest.raises(GitWorktreeSafetyError, match="reparse point"):
        worktree_safety.approved_local_validation_replay_root(repo)

    internal = tmp_path / "internal"
    internal.mkdir()
    probe = internal / "probe.txt"
    probe.write_text("probe\n", encoding="utf-8")
    monkeypatch.setattr(
        local_replay,
        "_is_reparse_path",
        lambda path: path == probe,
    )
    with pytest.raises(
        local_replay.LocalValidationReplayWorkspaceError,
        match="reparse path",
    ):
        local_replay._manifest_entries(internal)


def test_local_replay_manifest_rejects_bytes_or_sha_drift(
    tmp_path: Path,
) -> None:
    root = tmp_path / "workspace"
    evidence = root / "evidence"
    evidence.mkdir(parents=True)
    paths = local_replay.LocalReplayWorkspacePaths(
        workspace_root=root,
        source_root=root / "full-source",
        runner_temp_root=root / "runner-temp",
        synthetic_git_root=root / "runner-temp/synthetic.git",
        synthetic_index_path=root / "runner-temp/index",
        synthetic_pathspec_path=root / "runner-temp/paths",
        render_root=root / "pdf-render",
        extract_root=root / "pdf-render/visual_evidence",
        evidence_root=evidence,
        checkpoint_input_root=evidence / "checkpoint-input",
        post_checkpoint_root=evidence / "post",
        manifest_path=evidence / local_replay.WORKSPACE_MANIFEST,
        manifest_sha_path=evidence / local_replay.WORKSPACE_MANIFEST_SHA,
    )
    paths.source_root.mkdir(parents=True)
    source_probe = paths.source_root / "source-probe.txt"
    source_probe.write_text("full_source\n", encoding="utf-8")
    paths.runner_temp_root.mkdir(parents=True)
    (paths.runner_temp_root / "synthetic-probe.txt").write_text(
        "synthetic_git_index_objects_metadata\n", encoding="utf-8"
    )
    (paths.runner_temp_root / "routing-pilot-runner-temp.txt").write_text(
        "runner_local_temp\n", encoding="utf-8"
    )
    paths.render_root.mkdir(parents=True)
    (paths.render_root / "render-probe.txt").write_text(
        "pdf_test_render\n", encoding="utf-8"
    )
    paths.extract_root.mkdir(parents=True)
    (paths.extract_root / "extract-probe.txt").write_text(
        "pdf_text_extract\n", encoding="utf-8"
    )
    (paths.evidence_root / "evidence-probe.txt").write_text(
        "manifest_evidence\n", encoding="utf-8"
    )
    payload = {
        "status": "pilot_verified",
        "workspace_root": str(root),
        "source_tree_sha": "same-tree",
        "synthetic_tree_sha": "same-tree",
        "production_not_run": True,
        "official_pdf_published": False,
        "repo_artifacts_pushed_by_replay": False,
        "c_temp_fallback_used": False,
        "forbidden_system_temp_replay_paths_after": [],
        "categories": local_replay._pilot_categories(paths),
    }
    local_replay._write_manifest(paths, payload)
    source_probe.write_text("tampered\n", encoding="utf-8")
    with pytest.raises(
        local_replay.LocalValidationReplayWorkspaceError,
        match="bytes/SHA",
    ):
        local_replay.verify_pilot_manifest(paths)


def test_local_replay_commands_bind_every_runner_path_to_workspace(
    tmp_path: Path,
) -> None:
    root = Path(r"F:\CodexStorage\validation-replay-workspaces\taiwan-stock-recommendation\run-456")
    paths = local_replay.LocalReplayWorkspacePaths(
        workspace_root=root,
        source_root=root / "full-source",
        runner_temp_root=root / "runner-temp",
        synthetic_git_root=root / "runner-temp/price-history-extension.git-dir",
        synthetic_index_path=root / "runner-temp/price-history-extension.git-index",
        synthetic_pathspec_path=root / "runner-temp/price-history-extension-paths.bin",
        render_root=root / "pdf-render",
        extract_root=root / "pdf-render/visual_evidence",
        evidence_root=root / "evidence",
        checkpoint_input_root=root / "evidence/checkpoint-input",
        post_checkpoint_root=root / "evidence/post-validation-checkpoint",
        manifest_path=root / f"evidence/{local_replay.WORKSPACE_MANIFEST}",
        manifest_sha_path=root / f"evidence/{local_replay.WORKSPACE_MANIFEST_SHA}",
    )
    replay = local_replay.build_replay_command(
        paths,
        source_sha="a" * 40,
        run_id="local-1",
        checkpoint_run_id="31268964962",
        checkpoint_source_sha="b" * 40,
        checkpoint_artifact_id="9025240156",
        checkpoint_artifact_digest="sha256:" + "c" * 64,
    )
    render = local_replay.build_render_command(
        paths, source_sha="a" * 40, run_id="local-1"
    )
    for required in (
        paths.source_root,
        paths.runner_temp_root,
        paths.checkpoint_input_root,
        paths.post_checkpoint_root,
    ):
        assert str(required) in replay
    for required in (
        paths.source_root,
        paths.runner_temp_root,
        paths.post_checkpoint_root,
        paths.render_root,
    ):
        assert str(required) in render
    assert paths.extract_root == paths.render_root / "visual_evidence"
    c_temp = Path(r"C:\Users\p4693\AppData\Local\Temp")
    assert all(
        not Path(value).is_relative_to(c_temp)
        for value in paths.canonical_strings().values()
    )
    original_temp_audit = local_replay._system_temp_root_for_audit
    local_replay._system_temp_root_for_audit = lambda: c_temp
    try:
        with pytest.raises(
            local_replay.LocalValidationReplayWorkspaceError,
            match="must not be materialized",
        ):
            local_replay._require_checkpoint_bundle_outside_system_temp(
                c_temp / "checkpoint"
            )
    finally:
        local_replay._system_temp_root_for_audit = original_temp_audit
