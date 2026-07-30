from __future__ import annotations

import os
from pathlib import Path
import shutil
import subprocess

import pytest


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "ci_push_with_retry.sh"


def _run(
    args: list[str],
    *,
    cwd: Path,
    env: dict[str, str] | None = None,
    check: bool = True,
) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        args,
        cwd=cwd,
        env=env,
        check=check,
        text=True,
        capture_output=True,
    )


def _git(cwd: Path, *args: str) -> str:
    return _run(["git", *args], cwd=cwd).stdout.strip()


def _bash() -> str:
    discovered = shutil.which("bash")
    if discovered:
        return discovered
    windows_git_bash = Path("C:/Program Files/Git/bin/bash.exe")
    if windows_git_bash.exists():
        return str(windows_git_bash)
    pytest.skip("bash is unavailable")


def _commit(work: Path, name: str, content: str) -> str:
    (work / name).write_text(content, encoding="utf-8")
    _git(work, "add", name)
    _git(work, "commit", "-m", f"update {name}")
    return _git(work, "rev-parse", "HEAD")


def _repo_pair(tmp_path: Path) -> tuple[Path, Path, str]:
    remote = tmp_path / "remote.git"
    work = tmp_path / "work"
    _run(["git", "init", "--bare", str(remote)], cwd=tmp_path)
    _run(["git", "init", "-b", "main", str(work)], cwd=tmp_path)
    _git(work, "config", "user.name", "Codex Test")
    _git(work, "config", "user.email", "codex-test@example.invalid")
    base = _commit(work, "base.txt", "base\n")
    _git(work, "remote", "add", "origin", str(remote))
    _git(work, "push", "-u", "origin", "main")
    return remote, work, base


def _immutable_push(work: Path, expected_sha: str) -> subprocess.CompletedProcess[str]:
    env = os.environ.copy()
    env["CI_PUSH_EXPECTED_REMOTE_SHA"] = expected_sha
    return _run(
        [_bash(), SCRIPT.as_posix(), "main", "5"],
        cwd=work,
        env=env,
        check=False,
    )


def test_immutable_base_mode_pushes_exactly_one_descendant(tmp_path: Path) -> None:
    remote, work, base = _repo_pair(tmp_path)
    local_head = _commit(work, "new.txt", "new\n")

    result = _immutable_push(work, base)

    assert result.returncode == 0, result.stdout + result.stderr
    assert "Immutable-base push succeeded" in result.stdout
    assert "Push attempt" not in result.stdout
    assert _git(remote, "rev-parse", "refs/heads/main") == local_head
    assert _git(work, "rev-list", "--count", f"{base}..{local_head}") == "1"


def test_immutable_base_mode_rejects_remote_drift_without_rebase(tmp_path: Path) -> None:
    remote, work, base = _repo_pair(tmp_path)
    local_head = _commit(work, "local.txt", "local\n")
    peer = tmp_path / "peer"
    _run(["git", "clone", "--branch", "main", str(remote), str(peer)], cwd=tmp_path)
    _git(peer, "config", "user.name", "Codex Peer")
    _git(peer, "config", "user.email", "codex-peer@example.invalid")
    remote_head = _commit(peer, "remote.txt", "remote\n")
    _git(peer, "push", "origin", "main")

    result = _immutable_push(work, base)

    assert result.returncode != 0
    assert "refusing rebase or push" in result.stdout
    assert _git(work, "rev-parse", "HEAD") == local_head
    assert _git(remote, "rev-parse", "refs/heads/main") == remote_head


def test_immutable_base_mode_rejects_invalid_expected_sha(tmp_path: Path) -> None:
    remote, work, base = _repo_pair(tmp_path)
    _commit(work, "new.txt", "new\n")

    result = _immutable_push(work, "not-a-sha")

    assert result.returncode != 0
    assert "must be an exact 40-character Git SHA" in result.stdout
    assert _git(remote, "rev-parse", "refs/heads/main") == base


def test_immutable_base_mode_rejects_multiple_local_commits(tmp_path: Path) -> None:
    remote, work, base = _repo_pair(tmp_path)
    _commit(work, "first.txt", "first\n")
    local_head = _commit(work, "second.txt", "second\n")

    result = _immutable_push(work, base)

    assert result.returncode != 0
    assert "requires exactly one local commit; observed 2" in result.stdout
    assert _git(work, "rev-parse", "HEAD") == local_head
    assert _git(remote, "rev-parse", "refs/heads/main") == base
