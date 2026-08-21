from __future__ import annotations

import subprocess
from pathlib import Path

import pytest

from scripts import detect_daily_model_pr_validation_scope as scope


ROOT = Path(__file__).resolve().parents[1]
WORKFLOW = ROOT / ".github" / "workflows" / "daily_model_maintenance_pr_validation.yml"


def run_git(repo: Path, *args: str) -> str:
    result = subprocess.run(
        ["git", "--no-replace-objects", *args],
        cwd=repo,
        check=True,
        capture_output=True,
        text=True,
    )
    return result.stdout.strip()


def init_repo(
    tmp_path: Path,
    changed_rel: str = ".github/workflows/daily_full_pipeline.yml",
) -> tuple[Path, str, str, str]:
    repo = tmp_path / "repo"
    repo.mkdir()
    run_git(repo, "init", "--initial-branch=main")
    run_git(repo, "config", "user.email", "scope-test@example.invalid")
    run_git(repo, "config", "user.name", "Scope Test")
    marker = repo / "README.md"
    marker.write_text("base\n", encoding="utf-8")
    run_git(repo, "add", "README.md")
    run_git(repo, "commit", "-m", "base")
    base_sha = run_git(repo, "rev-parse", "HEAD")
    run_git(repo, "switch", "-c", "feature")
    changed = repo / changed_rel
    changed.parent.mkdir(parents=True, exist_ok=True)
    changed.write_text("feature\n", encoding="utf-8")
    run_git(repo, "add", changed_rel)
    run_git(repo, "commit", "-m", "head")
    head_sha = run_git(repo, "rev-parse", "HEAD")
    run_git(repo, "switch", "main")
    run_git(repo, "merge", "--no-ff", "feature", "-m", "synthetic merge")
    return repo, base_sha, head_sha, run_git(repo, "rev-parse", "HEAD")


def test_workflow_runs_the_cheap_scope_for_every_pull_request() -> None:
    text = WORKFLOW.read_text(encoding="utf-8")
    event_block = text[text.index("on:") : text.index("permissions:")]

    assert "  pull_request:\n" in event_block
    assert "  workflow_dispatch:\n" in event_block
    assert "paths:" not in event_block
    assert "paths-ignore:" not in event_block


def test_every_current_tracked_owned_path_has_a_declared_domain() -> None:
    result = subprocess.run(
        ["git", "--no-replace-objects", "ls-files", "-z"],
        cwd=ROOT,
        check=True,
        capture_output=True,
    )
    tracked = [
        field.decode("utf-8", errors="surrogateescape")
        for field in result.stdout.split(b"\0")
        if field
    ]
    watched = [
        path
        for path in tracked
        if scope.is_watched_path(path) or scope.is_model_like_path(path)
    ]

    assert watched
    for path in watched:
        assert scope.REPO_CURRENT_CONTRACTS in scope.domains_for_path(path), path


@pytest.mark.parametrize(
    ("path", "expected"),
    (
        (
            ".github/workflows/daily_full_pipeline.yml",
            {scope.REPO_CURRENT_CONTRACTS},
        ),
        (
            ".github/workflows/daily_pdf_replay_pr_validation.yml",
            {scope.REPO_CURRENT_CONTRACTS},
        ),
        (
            "scripts/model_data_independence.py",
            {scope.REPO_CURRENT_CONTRACTS, scope.SHARED_MODEL_RESEARCH},
        ),
        (
            "scripts/build_volume_v2_warrant_lineage_history_audit.py",
            {scope.REPO_CURRENT_CONTRACTS, scope.VOLUME_V2_RESEARCH},
        ),
        (
            "scripts/validate_revenue_unreacted_range_source_snapshot_projection.py",
            {scope.REPO_CURRENT_CONTRACTS, scope.REVENUE_RESEARCH},
        ),
        (
            "scripts/build_financial_statement_historical_pit_source_audit.py",
            {
                scope.REPO_CURRENT_CONTRACTS,
                scope.REVENUE_RESEARCH,
                scope.FINANCIAL_STATEMENT_RESEARCH,
            },
        ),
        (
            ".github/workflows/research_backtest_pipeline.yml",
            set(scope.DOMAINS),
        ),
        (
            "scripts/build_daily_candidate_model_layer.py",
            {
                scope.REPO_CURRENT_CONTRACTS,
                scope.SHARED_MODEL_RESEARCH,
                scope.VOLUME_V2_RESEARCH,
                scope.REVENUE_RESEARCH,
            },
        ),
        (
            "config/stock_model_contract_registry.csv",
            {
                scope.REPO_CURRENT_CONTRACTS,
                scope.SHARED_MODEL_RESEARCH,
                scope.VOLUME_V2_RESEARCH,
                scope.REVENUE_RESEARCH,
            },
        ),
        (
            "config/formal_model_evidence_pins.csv",
            {
                scope.REPO_CURRENT_CONTRACTS,
                scope.SHARED_MODEL_RESEARCH,
                scope.VOLUME_V2_RESEARCH,
                scope.REVENUE_RESEARCH,
            },
        ),
        (
            "data/monthly_revenue_history/monthly_revenue_history.csv",
            {scope.REPO_CURRENT_CONTRACTS, scope.REVENUE_RESEARCH},
        ),
        (
            "docs/latest/revenue_unreacted_range_scope_probe.csv",
            {scope.REPO_CURRENT_CONTRACTS, scope.REVENUE_RESEARCH},
        ),
        (
            "docs/latest/volume_v2_scope_probe.csv",
            {scope.REPO_CURRENT_CONTRACTS, scope.VOLUME_V2_RESEARCH},
        ),
        (
            "output/history/daily_model_snapshots/scope_probe.csv",
            {
                scope.REPO_CURRENT_CONTRACTS,
                scope.SHARED_MODEL_RESEARCH,
                scope.VOLUME_V2_RESEARCH,
            },
        ),
    ),
)
def test_paths_select_only_their_declared_domains(
    path: str, expected: set[str]
) -> None:
    assert set(scope.domains_for_path(path)) == expected


def test_unrelated_path_is_ignored() -> None:
    assert scope.domains_for_path("docs/unrelated_release_note.md") == frozenset()


@pytest.mark.parametrize(
    "path",
    (
        "scripts/daily_alpha_signal_engine.py",
        "output/latest/daily_alpha_signal_latest.csv",
    ),
)
def test_unknown_model_like_path_fails_closed(path: str) -> None:
    with pytest.raises(scope.ScopeDetectionError, match="no declared validation domain"):
        scope.domains_for_path(path)


@pytest.mark.parametrize(
    "path",
    (
        "config/apps_script_research_dispatch_inputs.csv",
        "scripts/build_non_revenue_momentum_watch.py",
        "scripts/research_tdcc_dataset_consumer.py",
        "tests/test_research_tdcc_dataset_consumer.py",
    ),
)
def test_known_other_lane_paths_are_fast_pass_unrelated(path: str) -> None:
    assert not scope.is_watched_path(path)
    assert not scope.is_model_like_path(path)
    assert scope.domains_for_path(path) == frozenset()


def test_workflow_dispatch_selects_all_domains_without_reading_git(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.setattr(
        scope,
        "changed_paths_from_git",
        lambda *_args: pytest.fail("workflow_dispatch must not read a PR diff"),
    )

    result = scope.detect_scope(event_name="workflow_dispatch")

    assert result.changed_paths == ()
    assert result.watched_paths == ()
    assert result.selected_domains == scope.DOMAINS


def test_pull_request_requires_all_three_commit_objects() -> None:
    with pytest.raises(scope.ScopeDetectionError, match="base, head, and synthetic merge"):
        scope.detect_scope(event_name="pull_request", base_sha="abc")


def test_unsupported_event_fails_closed() -> None:
    with pytest.raises(scope.ScopeDetectionError, match="unsupported event"):
        scope.detect_scope(event_name="push")


def test_unrelated_nonempty_diff_fast_passes_with_no_domains(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.setattr(
        scope, "changed_paths_from_git", lambda *_args: ["README.md"]
    )

    result = scope.detect_scope(
        event_name="pull_request",
        base_sha="base",
        head_sha="head",
        merge_sha="merge",
    )

    assert result.changed_paths == ("README.md",)
    assert result.watched_paths == ()
    assert result.selected_domains == ()


def test_empty_effective_diff_fails_closed(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr(scope, "changed_paths_from_git", lambda *_args: [])

    with pytest.raises(scope.ScopeDetectionError, match="effective tree diff is empty"):
        scope.detect_scope(
            event_name="pull_request",
            base_sha="base",
            head_sha="head",
            merge_sha="merge",
        )


def test_pull_request_combines_relevant_domains_only(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.setattr(
        scope,
        "changed_paths_from_git",
        lambda *_args: [
            "README.md",
            ".github/workflows/daily_full_pipeline.yml",
            "scripts/validate_revenue_unreacted_range_source_snapshot_projection.py",
        ],
    )

    result = scope.detect_scope(
        event_name="pull_request",
        base_sha="base",
        head_sha="head",
        merge_sha="merge",
    )

    assert result.watched_paths == (
        ".github/workflows/daily_full_pipeline.yml",
        "scripts/validate_revenue_unreacted_range_source_snapshot_projection.py",
    )
    assert result.selected_domains == (
        scope.REPO_CURRENT_CONTRACTS,
        scope.REVENUE_RESEARCH,
    )


def test_name_status_parser_is_nul_safe_and_preserves_unusual_names() -> None:
    payload = (
        b"M\0.github/workflows/daily_full_pipeline.yml\0"
        b"A\0scripts/model file\nwith newline.py\0"
        b"D\0tests/trailing-space.py \0"
    )

    assert scope.parse_name_status_z(payload) == [
        ".github/workflows/daily_full_pipeline.yml",
        "scripts/model file\nwith newline.py",
        "tests/trailing-space.py ",
    ]


@pytest.mark.parametrize(
    "payload",
    (
        b"M\0missing-path-field",
        b"R100\0old.py\0new.py\0",
        b"M\0\0",
    ),
)
def test_name_status_parser_rejects_malformed_or_renamed_records(
    payload: bytes,
) -> None:
    with pytest.raises(scope.ScopeDetectionError):
        scope.parse_name_status_z(payload)


def test_git_diff_is_nul_delimited_no_renames_and_disables_replace_objects(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    calls: list[list[str]] = []

    def fake_run(args: list[str], **_kwargs: object) -> subprocess.CompletedProcess[bytes]:
        calls.append(args)
        if "diff" in args:
            return subprocess.CompletedProcess(
                args, 0, b"M\0.github/workflows/daily_full_pipeline.yml\0", b""
            )
        if "rev-list" in args:
            return subprocess.CompletedProcess(
                args, 0, b"merge base head\n", b""
            )
        return subprocess.CompletedProcess(args, 0, b"", b"")

    monkeypatch.setattr(scope.subprocess, "run", fake_run)

    assert scope.changed_paths_from_git("base", "head", "merge") == [
        ".github/workflows/daily_full_pipeline.yml"
    ]
    assert len(calls) == 5
    for args in calls:
        assert args[:2] == ["git", "--no-replace-objects"]
    diff_args = calls[-1]
    assert "--name-status" in diff_args
    assert "--no-renames" in diff_args
    assert "-z" in diff_args
    assert "base..merge" in diff_args


def test_missing_commit_object_fails_before_diff(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    calls: list[list[str]] = []

    def fake_run(args: list[str], **_kwargs: object) -> subprocess.CompletedProcess[bytes]:
        calls.append(args)
        return subprocess.CompletedProcess(args, 1, b"", b"missing")

    monkeypatch.setattr(scope.subprocess, "run", fake_run)

    with pytest.raises(scope.ScopeDetectionError, match="not an available commit"):
        scope.changed_paths_from_git("missing-base", "head", "merge")
    assert len(calls) == 1
    assert "cat-file" in calls[0]


def test_diff_failure_is_not_treated_as_an_empty_scope(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    def fake_run(args: list[str], **_kwargs: object) -> subprocess.CompletedProcess[bytes]:
        if "rev-list" in args:
            return subprocess.CompletedProcess(
                args, 0, b"merge base head\n", b""
            )
        if "diff" not in args:
            return subprocess.CompletedProcess(args, 0, b"", b"")
        return subprocess.CompletedProcess(args, 128, b"", b"diff exploded")

    monkeypatch.setattr(scope.subprocess, "run", fake_run)

    with pytest.raises(scope.ScopeDetectionError, match="git diff failed"):
        scope.changed_paths_from_git("base", "head", "merge")


def test_rev_list_failure_is_not_treated_as_a_scope_result(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    def fake_run(args: list[str], **_kwargs: object) -> subprocess.CompletedProcess[bytes]:
        if "rev-list" in args:
            return subprocess.CompletedProcess(args, 128, b"", b"cannot inspect")
        return subprocess.CompletedProcess(args, 0, b"", b"")

    monkeypatch.setattr(scope.subprocess, "run", fake_run)

    with pytest.raises(scope.ScopeDetectionError, match="cannot inspect"):
        scope.changed_paths_from_git("base", "head", "merge")


@pytest.mark.parametrize(
    ("parents", "message"),
    (
        (b"merge base\n", "two-parent"),
        (b"merge wrong-base head\n", "base parent mismatch"),
        (b"merge base wrong-head\n", "head parent mismatch"),
        (b"wrong-merge base head\n", "merge SHA mismatch"),
    ),
)
def test_synthetic_merge_identity_mismatch_fails_closed(
    parents: bytes,
    message: str,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    def fake_run(args: list[str], **_kwargs: object) -> subprocess.CompletedProcess[bytes]:
        if "rev-list" in args:
            return subprocess.CompletedProcess(args, 0, parents, b"")
        return subprocess.CompletedProcess(args, 0, b"", b"")

    monkeypatch.setattr(scope.subprocess, "run", fake_run)

    with pytest.raises(scope.ScopeDetectionError, match=message):
        scope.changed_paths_from_git("base", "head", "merge")


def test_real_git_diff_detects_the_routine_workflow_as_core_only(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    repo, base_sha, head_sha, merge_sha = init_repo(tmp_path)
    monkeypatch.setattr(scope, "ROOT", repo)

    result = scope.detect_scope(
        event_name="pull_request",
        base_sha=base_sha,
        head_sha=head_sha,
        merge_sha=merge_sha,
    )

    assert result.watched_paths == (
        ".github/workflows/daily_full_pipeline.yml",
    )
    assert result.selected_domains == (scope.REPO_CURRENT_CONTRACTS,)


@pytest.mark.parametrize(
    ("path", "expected"),
    (
        (
            "data/monthly_revenue_history/monthly_revenue_history.csv",
            {scope.REPO_CURRENT_CONTRACTS, scope.REVENUE_RESEARCH},
        ),
        (
            "docs/latest/revenue_unreacted_range_scope_probe.csv",
            {scope.REPO_CURRENT_CONTRACTS, scope.REVENUE_RESEARCH},
        ),
        (
            "docs/latest/volume_v2_scope_probe.csv",
            {scope.REPO_CURRENT_CONTRACTS, scope.VOLUME_V2_RESEARCH},
        ),
        (
            "output/history/daily_model_snapshots/scope_probe.csv",
            {
                scope.REPO_CURRENT_CONTRACTS,
                scope.SHARED_MODEL_RESEARCH,
                scope.VOLUME_V2_RESEARCH,
            },
        ),
    ),
)
def test_real_git_diff_routes_owned_data_docs_and_output(
    path: str,
    expected: set[str],
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    repo, base_sha, head_sha, merge_sha = init_repo(tmp_path, path)
    monkeypatch.setattr(scope, "ROOT", repo)

    result = scope.detect_scope(
        event_name="pull_request",
        base_sha=base_sha,
        head_sha=head_sha,
        merge_sha=merge_sha,
    )

    assert result.watched_paths == (path,)
    assert set(result.selected_domains) == expected


def test_real_git_rename_selects_both_old_and_new_path_domains(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    repo = tmp_path / "rename-repo"
    repo.mkdir()
    run_git(repo, "init", "--initial-branch=main")
    run_git(repo, "config", "user.email", "scope-test@example.invalid")
    run_git(repo, "config", "user.name", "Scope Test")
    old_path = repo / "scripts" / "build_volume_v2_warrant_lineage_history_audit.py"
    old_path.parent.mkdir(parents=True)
    old_path.write_text("old\n", encoding="utf-8")
    run_git(repo, "add", old_path.relative_to(repo).as_posix())
    run_git(repo, "commit", "-m", "base")
    base_sha = run_git(repo, "rev-parse", "HEAD")
    run_git(repo, "switch", "-c", "feature")
    new_rel = "scripts/validate_revenue_unreacted_range_new_projection.py"
    run_git(repo, "mv", old_path.relative_to(repo).as_posix(), new_rel)
    run_git(repo, "commit", "-m", "rename across domains")
    head_sha = run_git(repo, "rev-parse", "HEAD")
    run_git(repo, "switch", "main")
    run_git(repo, "merge", "--no-ff", "feature", "-m", "synthetic merge")
    merge_sha = run_git(repo, "rev-parse", "HEAD")
    monkeypatch.setattr(scope, "ROOT", repo)

    result = scope.detect_scope(
        event_name="pull_request",
        base_sha=base_sha,
        head_sha=head_sha,
        merge_sha=merge_sha,
    )

    assert result.watched_paths == (
        "scripts/build_volume_v2_warrant_lineage_history_audit.py",
        new_rel,
    )
    assert result.selected_domains == (
        scope.REPO_CURRENT_CONTRACTS,
        scope.VOLUME_V2_RESEARCH,
        scope.REVENUE_RESEARCH,
    )


def test_real_git_deletion_keeps_the_deleted_paths_domains(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    repo = tmp_path / "delete-repo"
    repo.mkdir()
    run_git(repo, "init", "--initial-branch=main")
    run_git(repo, "config", "user.email", "scope-test@example.invalid")
    run_git(repo, "config", "user.name", "Scope Test")
    deleted_rel = "scripts/build_financial_statement_historical_pit_source_audit.py"
    deleted = repo / deleted_rel
    deleted.parent.mkdir(parents=True)
    deleted.write_text("delete me\n", encoding="utf-8")
    run_git(repo, "add", deleted_rel)
    run_git(repo, "commit", "-m", "base")
    base_sha = run_git(repo, "rev-parse", "HEAD")
    run_git(repo, "switch", "-c", "feature")
    run_git(repo, "rm", deleted_rel)
    run_git(repo, "commit", "-m", "delete financial path")
    head_sha = run_git(repo, "rev-parse", "HEAD")
    run_git(repo, "switch", "main")
    run_git(repo, "merge", "--no-ff", "feature", "-m", "synthetic merge")
    merge_sha = run_git(repo, "rev-parse", "HEAD")
    monkeypatch.setattr(scope, "ROOT", repo)

    result = scope.detect_scope(
        event_name="pull_request",
        base_sha=base_sha,
        head_sha=head_sha,
        merge_sha=merge_sha,
    )

    assert result.watched_paths == (deleted_rel,)
    assert result.selected_domains == (
        scope.REPO_CURRENT_CONTRACTS,
        scope.REVENUE_RESEARCH,
        scope.FINANCIAL_STATEMENT_RESEARCH,
    )


def test_base_to_synthetic_merge_diff_excludes_base_only_advances(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    repo = tmp_path / "advanced-base-repo"
    repo.mkdir()
    run_git(repo, "init", "--initial-branch=main")
    run_git(repo, "config", "user.email", "scope-test@example.invalid")
    run_git(repo, "config", "user.name", "Scope Test")
    marker = repo / "README.md"
    marker.write_text("common\n", encoding="utf-8")
    run_git(repo, "add", "README.md")
    run_git(repo, "commit", "-m", "common")
    run_git(repo, "switch", "-c", "feature")
    feature_path = repo / ".github" / "workflows" / "daily_full_pipeline.yml"
    feature_path.parent.mkdir(parents=True)
    feature_path.write_text("name: feature\n", encoding="utf-8")
    run_git(repo, "add", feature_path.relative_to(repo).as_posix())
    run_git(repo, "commit", "-m", "feature")
    head_sha = run_git(repo, "rev-parse", "HEAD")
    run_git(repo, "switch", "main")
    base_only_rel = "scripts/build_volume_v2_warrant_lineage_history_audit.py"
    base_only = repo / base_only_rel
    base_only.parent.mkdir(parents=True)
    base_only.write_text("base advance\n", encoding="utf-8")
    run_git(repo, "add", base_only_rel)
    run_git(repo, "commit", "-m", "advance base")
    base_sha = run_git(repo, "rev-parse", "HEAD")
    run_git(repo, "merge", "--no-ff", "feature", "-m", "synthetic merge")
    merge_sha = run_git(repo, "rev-parse", "HEAD")
    monkeypatch.setattr(scope, "ROOT", repo)

    result = scope.detect_scope(
        event_name="pull_request",
        base_sha=base_sha,
        head_sha=head_sha,
        merge_sha=merge_sha,
    )

    assert result.watched_paths == (
        ".github/workflows/daily_full_pipeline.yml",
    )
    assert base_only_rel not in result.changed_paths
    assert result.selected_domains == (scope.REPO_CURRENT_CONTRACTS,)


def test_github_output_records_each_domain_and_counts(tmp_path: Path) -> None:
    output = tmp_path / "github-output.txt"
    result = scope.ScopeResult(
        changed_paths=("README.md", "scripts/model_data_independence.py"),
        watched_paths=("scripts/model_data_independence.py",),
        selected_domains=(
            scope.REPO_CURRENT_CONTRACTS,
            scope.SHARED_MODEL_RESEARCH,
        ),
    )

    scope.write_github_output(output, result)

    assert output.read_text(encoding="utf-8").splitlines() == [
        "repo_current_contracts=true",
        "shared_model_research=true",
        "volume_v2_research=false",
        "revenue_research=false",
        "financial_statement_research=false",
        "changed_count=2",
        "watched_count=1",
    ]
