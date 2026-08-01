from __future__ import annotations

import subprocess
import sys
from pathlib import Path

import pandas as pd
import pytest


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import validate_daily_published_model_snapshots as strict_snapshots  # noqa: E402
import validate_daily_published_model_snapshots_pr_safe as pr_safe  # noqa: E402


def run_git(repo: Path, *args: str) -> str:
    proc = subprocess.run(
        ["git", *args],
        cwd=repo,
        check=True,
        capture_output=True,
        text=True,
    )
    return proc.stdout.strip()


def write_historical_replay_freshness(
    repo: Path,
    *,
    report_ready_note: str = pr_safe.HISTORICAL_REPLAY_REPORT_READY_NOTE,
) -> None:
    path = repo / pr_safe.FRESHNESS_RELATIVE_PATH
    path.parent.mkdir(parents=True, exist_ok=True)
    pd.DataFrame(
        [
            {
                "main_price_date": "20260731",
                "main_price_date_source": "historical_replay_override",
                "historical_replay_main_price_date": "20260731",
                "expected_price_history_high_water_date": "20260731",
                "actual_stock_price_history_date": "20260731",
                "report_ready": "False",
                "report_ready_note": report_ready_note,
                "warrant_ready": "True",
                "daily_pdf_ready": "False",
                "daily_pdf_ready_note": pr_safe.HISTORICAL_REPLAY_DAILY_PDF_READY_NOTE,
            }
        ]
    ).to_csv(path, index=False, encoding="utf-8", lineterminator="\n")


def initialized_pr_repo(
    tmp_path: Path,
    *,
    report_ready_note: str = pr_safe.HISTORICAL_REPLAY_REPORT_READY_NOTE,
) -> tuple[Path, str]:
    repo = tmp_path / "repo"
    repo.mkdir()
    run_git(repo, "init", "--initial-branch=main")
    run_git(repo, "config", "user.email", "pr-safe-test@example.invalid")
    run_git(repo, "config", "user.name", "PR Safe Test")
    write_historical_replay_freshness(
        repo,
        report_ready_note=report_ready_note,
    )
    (repo / "scripts").mkdir(exist_ok=True)
    (repo / "scripts" / "pr_464_unrelated_model_change.py").write_text(
        "BASE = 1\n",
        encoding="utf-8",
    )
    manifest = (
        repo
        / "output"
        / "history"
        / "daily_model_snapshots"
        / "daily_published_model_snapshot_manifest.csv"
    )
    manifest.parent.mkdir(parents=True, exist_ok=True)
    manifest.write_text("base manifest sentinel\n", encoding="utf-8")
    run_git(repo, "add", ".")
    run_git(repo, "commit", "-m", "legal historical replay base")
    return repo, run_git(repo, "rev-parse", "HEAD")


def commit_unrelated_pr_change(repo: Path) -> None:
    path = repo / "scripts" / "pr_464_unrelated_model_change.py"
    path.write_text("BASE = 1\nNORMALIZE_DUPLICATES = True\n", encoding="utf-8")
    run_git(repo, "add", path.relative_to(repo).as_posix())
    run_git(repo, "commit", "-m", "PR 464 unrelated model normalization")


def test_pr_464_inherited_historical_replay_not_ready_is_pr_safe_but_strict_fails(
    tmp_path: Path,
) -> None:
    repo, base_sha = initialized_pr_repo(tmp_path)
    commit_unrelated_pr_change(repo)
    latest_dir = repo / "output" / "latest"

    strict_errors = strict_snapshots.validate_current_report_snapshots(
        latest_dir=latest_dir,
        snapshot_dir=repo / "output" / "history" / "daily_model_snapshots",
        manifest_path=(
            repo
            / "output"
            / "history"
            / "daily_model_snapshots"
            / "daily_published_model_snapshot_manifest.csv"
        ),
    )
    assert strict_errors == [pr_safe.EXPECTED_STRICT_NOT_READY_ERROR]
    assert pr_safe.validate_pr_safe_snapshot_contract(
        base_sha,
        repository_root=repo,
        latest_dir=latest_dir,
    ) == []


def test_sensitive_snapshot_change_still_requires_full_strict_validation(
    tmp_path: Path,
) -> None:
    repo, base_sha = initialized_pr_repo(tmp_path)
    manifest = (
        repo
        / "output"
        / "history"
        / "daily_model_snapshots"
        / "daily_published_model_snapshot_manifest.csv"
    )
    manifest.write_text("changed manifest sentinel\n", encoding="utf-8")
    run_git(repo, "add", manifest.relative_to(repo).as_posix())
    run_git(repo, "commit", "-m", "change snapshot manifest")

    errors = pr_safe.validate_pr_safe_snapshot_contract(
        base_sha,
        repository_root=repo,
        latest_dir=repo / "output" / "latest",
    )

    assert any("full runtime" in error for error in errors)
    assert any(
        "output/history/daily_model_snapshots/" in error
        for error in errors
    )
    assert pr_safe.EXPECTED_STRICT_NOT_READY_ERROR in errors


def test_arbitrary_not_ready_state_is_not_accepted_as_historical_replay(
    tmp_path: Path,
) -> None:
    repo, base_sha = initialized_pr_repo(
        tmp_path,
        report_ready_note="unrelated stale artifact",
    )
    commit_unrelated_pr_change(repo)

    errors = pr_safe.validate_pr_safe_snapshot_contract(
        base_sha,
        repository_root=repo,
        latest_dir=repo / "output" / "latest",
    )

    assert any("report_ready_note mismatch" in error for error in errors)


def test_historical_replay_marker_requires_raw_exact_yyyymmdd(tmp_path: Path) -> None:
    repo, _ = initialized_pr_repo(tmp_path)
    freshness_path = repo / pr_safe.FRESHNESS_RELATIVE_PATH
    freshness = pd.read_csv(freshness_path, dtype=str).fillna("")
    freshness.loc[0, "main_price_date"] = "2026-07-31"
    freshness.to_csv(
        freshness_path,
        index=False,
        encoding="utf-8",
        lineterminator="\n",
    )

    errors = pr_safe.validate_historical_replay_not_ready_marker(freshness_path)

    assert any("main_price_date must be YYYYMMDD" in error for error in errors)


def test_unrelated_pr_does_not_hide_other_strict_snapshot_failures(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    repo, base_sha = initialized_pr_repo(tmp_path)
    commit_unrelated_pr_change(repo)
    monkeypatch.setattr(
        pr_safe,
        "validate_current_report_snapshots",
        lambda **_: ["manifest has duplicate snapshot revision rows"],
    )

    errors = pr_safe.validate_pr_safe_snapshot_contract(
        base_sha,
        repository_root=repo,
        latest_dir=repo / "output" / "latest",
    )

    assert any("may inherit only" in error for error in errors)
    assert "manifest has duplicate snapshot revision rows" in errors


def test_uncommitted_freshness_drift_cannot_be_inherited_from_base(
    tmp_path: Path,
) -> None:
    repo, base_sha = initialized_pr_repo(tmp_path)
    commit_unrelated_pr_change(repo)
    write_historical_replay_freshness(
        repo,
        report_ready_note=pr_safe.HISTORICAL_REPLAY_REPORT_READY_NOTE,
    )
    freshness_path = repo / pr_safe.FRESHNESS_RELATIVE_PATH
    freshness_path.write_bytes(freshness_path.read_bytes() + b"\n")

    errors = pr_safe.validate_pr_safe_snapshot_contract(
        base_sha,
        repository_root=repo,
        latest_dir=repo / "output" / "latest",
    )

    assert any("differs from base_ref" in error for error in errors)


@pytest.mark.parametrize(
    "path",
    [
        "output/latest/data_freshness_latest.csv",
        "output/history/daily_model_snapshots/daily_published_model_snapshot_manifest.csv",
        "scripts/validate_daily_published_model_snapshots.py",
        ".github/workflows/historical_structured_source_replay.yml",
        ".github/workflows/daily_full_pipeline.yml",
    ],
)
def test_snapshot_publication_surfaces_always_require_strict_validation(
    path: str,
) -> None:
    assert pr_safe.requires_strict_runtime_validation(path)


def test_model_implementation_change_is_not_a_snapshot_publication_surface() -> None:
    assert not pr_safe.requires_strict_runtime_validation(
        "scripts/pr_464_unrelated_model_change.py"
    )


def test_snapshot_updater_path_requires_strict_runtime_validation() -> None:
    updater_path = "/".join(
        ("scripts", "update_daily_" + "published_model_snapshots.py")
    )
    assert pr_safe.requires_strict_runtime_validation(updater_path)


def test_initial_control_plane_bootstrap_is_one_time_and_future_changes_are_strict(
    tmp_path: Path,
) -> None:
    repo, _ = initialized_pr_repo(tmp_path)
    workflow = repo / pr_safe.PR_VALIDATION_WORKFLOW_PATH
    boundary = repo / pr_safe.PR_BOUNDARY_VALIDATOR_PATH
    workflow.parent.mkdir(parents=True, exist_ok=True)
    workflow.write_text(pr_safe.STRICT_SNAPSHOT_COMMAND + "\n", encoding="utf-8")
    boundary.write_text(
        repr(pr_safe.STRICT_SNAPSHOT_COMMAND) + "\n",
        encoding="utf-8",
    )
    run_git(repo, "add", ".")
    run_git(repo, "commit", "-m", "old unconditional PR snapshot gate")
    bootstrap_base = run_git(repo, "rev-parse", "HEAD")

    helper = repo / pr_safe.PR_SAFE_HELPER_PATH
    helper.write_text("PR_SAFE_HELPER = True\n", encoding="utf-8")
    workflow.write_text(pr_safe.PR_SAFE_SNAPSHOT_COMMAND + "\n", encoding="utf-8")
    boundary.write_text(
        repr(pr_safe.PR_SAFE_SNAPSHOT_COMMAND) + "\n",
        encoding="utf-8",
    )
    run_git(repo, "add", ".")
    run_git(repo, "commit", "-m", "install bounded PR-safe snapshot gate")

    assert pr_safe.validate_pr_safe_snapshot_contract(
        bootstrap_base,
        repository_root=repo,
        latest_dir=repo / "output" / "latest",
    ) == []

    future_base = run_git(repo, "rev-parse", "HEAD")
    helper.write_text("PR_SAFE_HELPER = 'changed'\n", encoding="utf-8")
    run_git(repo, "add", helper.relative_to(repo).as_posix())
    run_git(repo, "commit", "-m", "change PR-safe gate after bootstrap")
    future_errors = pr_safe.validate_pr_safe_snapshot_contract(
        future_base,
        repository_root=repo,
        latest_dir=repo / "output" / "latest",
    )
    assert any("full runtime" in error for error in future_errors)
    assert any(pr_safe.PR_SAFE_HELPER_PATH in error for error in future_errors)


def test_bootstrap_fails_closed_when_base_tree_cannot_be_read(tmp_path: Path) -> None:
    assert not pr_safe.is_initial_pr_safe_gate_bootstrap(
        "missing-base-ref",
        set(pr_safe.PR_SAFE_BOOTSTRAP_SURFACES),
        repository_root=tmp_path,
    )


def test_control_plane_self_update_requires_exact_base_and_workflow_bytes(
    tmp_path: Path,
    monkeypatch,
) -> None:
    repo, _ = initialized_pr_repo(tmp_path)
    helper = repo / pr_safe.PR_SAFE_HELPER_PATH
    workflow = repo / pr_safe.PR_VALIDATION_WORKFLOW_PATH
    helper.parent.mkdir(parents=True, exist_ok=True)
    workflow.parent.mkdir(parents=True, exist_ok=True)
    base_helper = b"snapshot PR-safe helper before controlled migration\n"
    base_workflow = b"".join(
        (
            b"jobs:\n",
            b"  validation:\n",
            b"    env:\n",
            b"      BASE_SHA: ${{ github.event.pull_request.base.sha || 'origin/main' }}\n",
            b"      - \"scripts/validate_repo_advanced_integrity.py\"\n",
            b"      - \"tests/test_repo_advanced_integrity.py\"\n",
            (f"          {pr_safe.PR_SAFE_SNAPSHOT_COMMAND}\n").encode("utf-8"),
            b"            tests/test_repo_advanced_integrity.py \\\n",
            b"            tests/test_stock_model_contract_registry.py\n",
        )
    )
    helper.write_bytes(base_helper)
    workflow.write_bytes(base_workflow)
    run_git(repo, "add", ".")
    run_git(repo, "commit", "-m", "base PR-safe control plane")
    base_ref = run_git(repo, "rev-parse", "HEAD")

    current_helper = (
        f"CONTROL_PLANE_MIGRATION_ID = {pr_safe.CONTROL_PLANE_MIGRATION_ID!r}\n"
    ).encode("utf-8")
    helper.write_bytes(current_helper)
    expected_workflow = pr_safe.expected_control_plane_workflow(
        base_workflow,
        current_helper_sha256=pr_safe.sha256_bytes(current_helper),
    )
    assert expected_workflow is not None
    workflow.write_bytes(expected_workflow)
    monkeypatch.setattr(
        pr_safe,
        "CONTROL_PLANE_MIGRATION_BASE_HELPER_SHA256",
        pr_safe.sha256_bytes(base_helper),
    )

    assert pr_safe.is_control_plane_self_update_migration(
        base_ref,
        set(pr_safe.CONTROL_PLANE_MIGRATION_SURFACES),
        repository_root=repo,
    )

    workflow.write_bytes(expected_workflow + b"unexpected broad workflow change\n")
    assert not pr_safe.is_control_plane_self_update_migration(
        base_ref,
        set(pr_safe.CONTROL_PLANE_MIGRATION_SURFACES),
        repository_root=repo,
    )
    assert not pr_safe.is_control_plane_self_update_migration(
        base_ref,
        {
            *pr_safe.CONTROL_PLANE_MIGRATION_SURFACES,
            pr_safe.PR_BOUNDARY_VALIDATOR_PATH,
        },
        repository_root=repo,
    )


def test_pr_workflow_uses_pr_safe_gate_while_publish_workflows_remain_strict() -> None:
    pr_workflow = (
        ROOT / ".github" / "workflows" / "daily_model_maintenance_pr_validation.yml"
    ).read_text(encoding="utf-8")
    assert (
        'python scripts/validate_daily_published_model_snapshots_pr_safe.py --base-ref "$BASE_SHA"'
        in pr_workflow
    )
    assert "python scripts/validate_daily_published_model_snapshots.py" not in pr_workflow
    assert "tests/test_daily_published_model_snapshots_pr_safe.py" in pr_workflow

    strict_command = "python scripts/validate_daily_published_model_snapshots.py"
    for workflow_name in (
        "daily_full_pipeline.yml",
        "warrant_flow.yml",
        "weekly_theme_review.yml",
    ):
        workflow = (ROOT / ".github" / "workflows" / workflow_name).read_text(
            encoding="utf-8"
        )
        assert strict_command in workflow, workflow_name
