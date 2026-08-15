from __future__ import annotations

import re
from pathlib import Path
import sys

import pytest


ROOT = Path(__file__).resolve().parents[1]
WORKFLOW = ROOT / ".github" / "workflows" / "volume_v2_advisory_lineage_refresh.yml"
RUNNER = ROOT / "scripts" / "run_volume_v2_advisory_lineage_refresh.py"
SCRIPTS = ROOT / "scripts"
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))

import run_volume_v2_advisory_lineage_refresh as runner  # noqa: E402


FINAL_ARTIFACT_PATHS = {
    "output/latest/volume_breakout_watch_latest.csv",
    "output/latest/volume_attack_theme_layer_latest.md",
    "output/latest/volume_attack_theme_stocks_latest.csv",
    "output/latest/volume_attack_theme_stocks_latest.md",
    "docs/latest/volume_attack_theme_layer_latest.md",
    "docs/latest/volume_attack_theme_stocks_latest.csv",
    "docs/latest/volume_attack_theme_stocks_latest.md",
}


def test_workflow_is_manual_main_only_and_exactly_bounded() -> None:
    text = WORKFLOW.read_text(encoding="utf-8-sig")
    assert "workflow_dispatch:" in text
    for forbidden_trigger in ("pull_request:", "push:", "schedule:"):
        assert forbidden_trigger not in text
    assert "expected_base_sha:" in text
    assert "confirmation:" in text
    assert "refresh_volume_v2_advisory_lineage" in text
    assert 'GITHUB_REF" != "refs/heads/main' in text
    assert 'git branch --show-current)" != "main' in text
    assert 'git ls-remote origin refs/heads/main' in text
    assert "cancel-in-progress: false" in text
    assert "group: daily-full-pipeline-${{ github.ref }}" in text

    assert "python -B scripts/run_volume_v2_advisory_lineage_refresh.py" in text
    assert "python -B scripts/validate_volume_v2_advisory_lineage_refresh.py" in text
    assert "python -B scripts/validate_volume_breakout_watch.py --latest-only" in text
    assert "python -B scripts/validate_volume_attack_theme_layer.py" in text
    assert "python -B scripts/validate_daily_canonical_field_lineage.py" in text
    assert "python -B scripts/validate_daily_warrant_formal_sync_scope.py" in text
    assert '--write-snapshot "$warrant_scope_snapshot"' in text
    assert '--compare-snapshot "$WARRANT_SCOPE_SNAPSHOT"' in text
    assert not re.search(
        r"^\s*python -B scripts/validate_daily_warrant_formal_sync_scope\.py\s*$",
        text,
        flags=re.MULTILINE,
    )

    stage_block = text.split("- name: Stage exact seven-artifact refresh", 1)[1].split(
        "- name: Create one bounded local artifact commit", 1
    )[0]
    observed_paths = set(re.findall(r"(?:output|docs)/latest/[A-Za-z0-9_./-]+", stage_block))
    assert observed_paths == FINAL_ARTIFACT_PATHS
    assert text.count("git commit -m") == 1
    assert text.count("git push origin HEAD:refs/heads/main") == 1
    assert 'git rev-parse HEAD^' in text
    assert 'git rev-list --count "$REFRESH_BASE_SHA..HEAD"' in text
    assert '"$refresh_parent_sha" != "$REFRESH_BASE_SHA"' in text
    assert '"$refresh_commit_count" != "1"' in text
    assert 'git status --porcelain=v1' in text
    commit_position = text.index('git commit -m "Refresh Volume V2 advisory lineage"')
    theme_validator_position = text.index(
        "python -B scripts/validate_volume_attack_theme_layer.py"
    )
    push_position = text.index("git push origin HEAD:refs/heads/main")
    warrant_snapshot_position = text.index('--write-snapshot "$warrant_scope_snapshot"')
    runner_position = text.index("python -B scripts/run_volume_v2_advisory_lineage_refresh.py")
    warrant_compare_position = text.index(
        '--compare-snapshot "$WARRANT_SCOPE_SNAPSHOT"'
    )
    assert warrant_snapshot_position < runner_position < commit_position
    assert commit_position < warrant_compare_position < push_position
    assert commit_position < theme_validator_position < push_position
    committed_block = text.split("- name: Validate committed refresh before publication", 1)[
        1
    ].split("- name: Push one validated bounded artifact commit", 1)[0]
    assert "Legacy theme validation reports were not byte-identical" in committed_block
    assert committed_block.index("python -B scripts/validate_volume_attack_theme_layer.py") < committed_block.index(
        "Legacy theme validation reports were not byte-identical"
    ) < committed_block.index("--phase committed")
    assert "Validate committed refresh before publication" in text
    assert "--phase committed" in text
    assert "REFRESH_COMMIT_SHA=$refresh_commit_sha" in text
    assert '--base-ref "$REFRESH_BASE_SHA"' in committed_block
    assert '--trusted-ref "$REFRESH_COMMIT_SHA"' in committed_block
    committed_guard_position = committed_block.index("--phase committed")
    canonical_lineage_position = committed_block.index(
        "python -B scripts/validate_daily_canonical_field_lineage.py"
    )
    assert committed_guard_position < canonical_lineage_position
    assert "|| true" not in committed_block
    for forbidden in (
        "git add -A",
        "git add --all",
        "git rebase",
        "git push --force",
        "daily_full_pipeline.yml",
        "generate_chatgpt_side_daily_reports.py",
        "run_chatgpt_daily_report_entrypoint.py",
        "Apps Script",
        "build_daily_candidate_model_layer.py",
    ):
        assert forbidden not in text


def test_runner_uses_only_existing_watch_theme_builders_and_restores_metadata() -> None:
    text = RUNNER.read_text(encoding="utf-8-sig")
    assert '"scripts/build_volume_breakout_watch.py", "--latest-only"' in text
    assert '"scripts/build_volume_attack_theme_layer.py"' in text
    assert '"scripts/validate_volume_breakout_watch.py", "--latest-only"' in text
    assert '"scripts/validate_volume_attack_theme_layer.py"' not in text
    assert '"--phase",\n                "post-build"' in text
    assert '"--phase",\n            "final"' in text
    assert "METADATA_ONLY_PATHS" in text
    assert '"git",\n            "restore"' in text
    assert 'f"--source={base_sha}"' in text
    assert 'OFFICIAL_REPOSITORY = "LeoChen0727/tdcc-weekly-report"' in text
    assert "workflow_ref != expected_workflow_ref" in text
    for forbidden in (
        "build_daily_candidate_model_layer.py",
        "daily_full_pipeline.yml",
        "generate_chatgpt_side_daily_reports.py",
        "git add",
        "git commit",
        "git push",
    ):
        assert forbidden not in text


def test_runner_requires_exact_official_repository_and_workflow_ref(
    monkeypatch: pytest.MonkeyPatch, tmp_path: Path
) -> None:
    base_sha = "a" * 40
    environment = {
        "GITHUB_ACTIONS": "true",
        "GITHUB_EVENT_NAME": "workflow_dispatch",
        "GITHUB_REF_NAME": "main",
        "GITHUB_REPOSITORY": runner.OFFICIAL_REPOSITORY,
        "GITHUB_SHA": base_sha,
        "GITHUB_WORKFLOW_REF": (
            f"{runner.OFFICIAL_REPOSITORY}/{runner.OFFICIAL_WORKFLOW_PATH}"
            "@refs/heads/main"
        ),
        "VOLUME_V2_ADVISORY_REFRESH_CONFIRMATION": runner.CONFIRMATION_TOKEN,
    }
    for name, value in environment.items():
        monkeypatch.setenv(name, value)

    def fake_git(_root: Path, *args: str) -> str:
        if args == ("rev-parse", "HEAD"):
            return f"{base_sha}\n"
        if args == ("branch", "--show-current"):
            return "main\n"
        if args == ("status", "--porcelain=v1"):
            return ""
        raise AssertionError(f"unexpected git call: {args!r}")

    monkeypatch.setattr(runner, "_git", fake_git)
    runner.validate_official_context(base_sha=base_sha, root=tmp_path)

    monkeypatch.setenv(
        "GITHUB_WORKFLOW_REF",
        f"evil/repo/{runner.OFFICIAL_WORKFLOW_PATH}@refs/heads/main",
    )
    with pytest.raises(runner.VolumeV2AdvisoryRefreshError, match="workflow ref"):
        runner.validate_official_context(base_sha=base_sha, root=tmp_path)
