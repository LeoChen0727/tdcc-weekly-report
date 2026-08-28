from __future__ import annotations

import subprocess
from pathlib import Path

import pytest

from scripts import detect_tdcc_weekly_pr_scope as scope


def git(repo: Path, *args: str) -> str:
    result = subprocess.run(
        ["git", *args],
        cwd=repo,
        check=True,
        text=True,
        encoding="utf-8",
        stdout=subprocess.PIPE,
    )
    return result.stdout.strip()


def commit_all(repo: Path, message: str) -> str:
    git(repo, "add", "--all")
    git(repo, "commit", "-m", message)
    return git(repo, "rev-parse", "HEAD")


def initialize_git_repo(repo: Path) -> None:
    git(repo, "init", "--quiet")
    git(repo, "config", "user.name", "Scope Test")
    git(repo, "config", "user.email", "scope-test@example.invalid")


@pytest.mark.parametrize(
    "path",
    (
        ".github/workflows/tdcc_weekly.yml",
        ".github/workflows/tdcc_weekly_pr_validation.yml",
        "scripts/detect_tdcc_weekly_pr_scope.py",
        "scripts/build_tdcc_dataset_manifest.py",
        "tests/test_tdcc_dataset_contract.py",
        "output/history/tdcc/20260828/manifest.json",
    ),
)
def test_direct_tdcc_path_is_affected(path: str) -> None:
    assert scope.is_tdcc_affected_path(path)


@pytest.mark.parametrize(
    "path",
    (
        "scripts/revenue_unreacted_range_research.py",
        "tests/test_revenue_unreacted_range_forward_holdout_v2.py",
        "config/revenue_unreacted_range_promotion_preparation_registry.csv",
    ),
)
def test_direct_revenue_path_is_not_affected(path: str) -> None:
    assert not scope.is_tdcc_affected_path(path)


def test_real_rename_is_reported_as_deleted_and_added_paths(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    initialize_git_repo(tmp_path)
    old_path = tmp_path / "scripts" / "build_tdcc_dataset_manifest.py"
    old_path.parent.mkdir(parents=True)
    old_path.write_text("old\n", encoding="utf-8")
    base_sha = commit_all(tmp_path, "base")
    new_path = tmp_path / "docs" / "renamed_manifest.py"
    new_path.parent.mkdir(parents=True)
    git(
        tmp_path,
        "mv",
        "scripts/build_tdcc_dataset_manifest.py",
        "docs/renamed_manifest.py",
    )
    head_sha = commit_all(tmp_path, "rename")
    monkeypatch.setattr(scope, "ROOT", tmp_path)

    assert scope.validate_commit_range(base_sha, head_sha) == (base_sha, head_sha)
    changed = scope.changed_paths_from_git(base_sha, head_sha)
    assert changed == [
        "docs/renamed_manifest.py",
        "scripts/build_tdcc_dataset_manifest.py",
    ]
    assert scope.matched_tdcc_affected_paths(
        changed,
        base_sha=base_sha,
        head_sha=head_sha,
    ) == ["scripts/build_tdcc_dataset_manifest.py"]


def test_commit_range_rejects_non_commit_and_non_ancestor_base(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    initialize_git_repo(tmp_path)
    tracked = tmp_path / "tracked.txt"
    tracked.write_text("base\n", encoding="utf-8")
    root_sha = commit_all(tmp_path, "root")
    tracked.write_text("head\n", encoding="utf-8")
    head_sha = commit_all(tmp_path, "head")
    git(tmp_path, "checkout", "--quiet", root_sha)
    tracked.write_text("side\n", encoding="utf-8")
    side_sha = commit_all(tmp_path, "side")
    tree_sha = git(tmp_path, "rev-parse", f"{head_sha}^{{tree}}")
    monkeypatch.setattr(scope, "ROOT", tmp_path)

    with pytest.raises(scope.RegistryScopeError, match="commit object"):
        scope.validate_commit_range(tree_sha, head_sha)
    with pytest.raises(scope.RegistryScopeError, match="must be an ancestor"):
        scope.validate_commit_range(side_sha, head_sha)


@pytest.mark.parametrize("path", sorted(scope.SHARED_REGISTRY_KEY_FIELDS))
def test_shared_registry_revenue_only_row_change_is_not_tdcc_affected(
    path: str,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    key_field = scope.SHARED_REGISTRY_KEY_FIELDS[path]
    base = (
        f"{key_field},owner,producer,source_artifacts,purpose\n"
        "output/revenue.csv,research_backtest,scripts/revenue.py,"
        "data/tdcc_stock_history,revenue old\n"
    )
    head = base.replace("revenue old", "revenue new")
    monkeypatch.setattr(
        scope,
        "_read_git_text",
        lambda revision, _path: base if revision == "base" else head,
    )

    assert not scope.is_tdcc_affected_changed_path(
        path,
        base_sha="base",
        head_sha="head",
    )


@pytest.mark.parametrize("path", sorted(scope.SHARED_REGISTRY_KEY_FIELDS))
def test_shared_registry_tdcc_owned_row_change_is_affected(
    path: str,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    key_field = scope.SHARED_REGISTRY_KEY_FIELDS[path]
    base = (
        f"{key_field},owner,producer,purpose\n"
        "scripts/revenue.py,research_backtest,scripts/revenue.py,same\n"
    )
    head = base + (
        "scripts/build_tdcc_dataset_manifest.py,tdcc_weekly,"
        "scripts/build_tdcc_dataset_manifest.py,manifest\n"
    )
    monkeypatch.setattr(
        scope,
        "_read_git_text",
        lambda revision, _path: base if revision == "base" else head,
    )

    assert scope.is_tdcc_affected_changed_path(
        path,
        base_sha="base",
        head_sha="head",
    )


def test_shared_registry_relation_to_tdcc_workflow_is_affected(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    path = "config/repo_production_inventory.csv"
    base = "path,owner,allowed_workflows\nscripts/shared.py,repo_infrastructure,\n"
    head = (
        "path,owner,allowed_workflows\n"
        "scripts/shared.py,repo_infrastructure,.github/workflows/tdcc_weekly.yml\n"
    )
    monkeypatch.setattr(
        scope,
        "_read_git_text",
        lambda revision, _path: base if revision == "base" else head,
    )

    assert scope.is_tdcc_affected_changed_path(
        path,
        base_sha="base",
        head_sha="head",
    )


def test_shared_registry_ambiguous_state_fails_closed(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.setattr(
        scope,
        "_read_git_text",
        lambda *_args: (_ for _ in ()).throw(
            scope.RegistryScopeError("missing blob")
        ),
    )

    assert scope.is_tdcc_affected_changed_path(
        "config/report_artifact_lineage.csv",
        base_sha="base",
        head_sha="head",
    )


def test_github_output_uses_individual_compatible_keys(tmp_path: Path) -> None:
    output = tmp_path / "github-output.txt"
    scope.write_github_output(output, ["scripts/build_tdcc_dataset_manifest.py"])

    assert output.read_text(encoding="utf-8").splitlines() == [
        "affected=true",
        "matched_count=1",
    ]
