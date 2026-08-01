from __future__ import annotations

import re
import subprocess
from pathlib import Path

from scripts import validate_daily_production_boundaries as boundaries
from scripts.update_daily_published_model_snapshots import ARTIFACTS_BY_ID


ROOT = Path(__file__).resolve().parents[1]
WORKFLOW = ROOT / ".github" / "workflows" / "daily_model_maintenance_pr_validation.yml"
DAILY_WORKFLOW = ROOT / ".github" / "workflows" / "daily_full_pipeline.yml"
WARRANT_WORKFLOW = ROOT / ".github" / "workflows" / "warrant_flow.yml"
PDF_REPLAY_WORKFLOW = ROOT / ".github" / "workflows" / "daily_pdf_replay_pr_validation.yml"


def test_every_formal_snapshot_workflow_pins_an_explicit_revision_reason() -> None:
    expected_callers = {
        "daily_full_pipeline.yml": (
            "daily_full_volume_v2_audit_sources",
            "daily_full_post_audit_artifacts",
        ),
        "weekly_theme_review.yml": ("weekly_theme_formal_sync",),
        "warrant_flow.yml": ("warrant_formal_sync",),
    }
    workflow_dir = ROOT / ".github" / "workflows"
    publisher = "python scripts/update_daily_published_model_snapshots.py"
    actual_callers = {
        path.name
        for path in workflow_dir.glob("*.yml")
        if publisher in path.read_text(encoding="utf-8")
    }

    assert actual_callers == set(expected_callers)
    for filename, revision_reasons in expected_callers.items():
        text = (workflow_dir / filename).read_text(encoding="utf-8")
        assert text.count(publisher) == len(revision_reasons)
        for revision_reason in revision_reasons:
            assert text.count(f"--revision-reason {revision_reason}") == 1


def test_every_formal_snapshot_workflow_uses_registered_artifact_ids() -> None:
    workflow_dir = ROOT / ".github" / "workflows"
    publisher = "python scripts/update_daily_published_model_snapshots.py"
    for path in workflow_dir.glob("*.yml"):
        text = path.read_text(encoding="utf-8")
        if publisher not in text:
            continue
        observed = set(re.findall(r"--artifact-id ([A-Za-z0-9_]+)", text))
        assert observed
        assert observed <= set(ARTIFACTS_BY_ID), path.name


def test_daily_full_stages_only_exact_manifest_snapshot_revisions() -> None:
    text = DAILY_WORKFLOW.read_text(encoding="utf-8")
    commit_block = text[
        text.index("- name: Commit report artifacts, packets, and rules first") :
        text.index("- name: Wait briefly for GitHub Pages and raw propagation")
    ]
    assert 're.sub(r"[^0-9]", ""' in commit_block
    assert 'if [[ ! "$snapshot_report_date" =~ ^[0-9]{8}$ ]]; then' in commit_block
    assert "git add output/history/daily_model_snapshots/ || true" not in commit_block

    artifact_ids = (
        "data_freshness",
        "model_signals_for_report",
        "all_candidates_source_rows",
        "model_summary_for_report",
        "model_registry",
        "model_parameters",
        "volume_breakout_operation_section",
        "volume_breakout_operation_evidence_audit",
        "w_bottom_right_side_operation_section",
        "neckline_volume_breakout_confirmation_operation_section",
    )
    assert commit_block.count(
        "python scripts/stage_daily_published_snapshot_revisions.py"
    ) == 1
    for artifact_id in artifact_ids:
        assert commit_block.count(f"--artifact-id {artifact_id}") == 1
    assert 'daily_model_snapshots/data_freshness_${snapshot_report_date}"*.csv' not in commit_block


def run_git(repo: Path, *args: str) -> str:
    proc = subprocess.run(
        ["git", *args],
        cwd=repo,
        check=True,
        capture_output=True,
        text=True,
    )
    return proc.stdout.strip()


def test_daily_model_maintenance_pr_workflow_exists_for_model_pdf_paths() -> None:
    text = WORKFLOW.read_text(encoding="utf-8")

    assert "pull_request:" in text
    assert "fetch-depth: 0" in text
    assert "scripts/generate_chatgpt_side_daily_reports.py" in text
    assert "scripts/run_chatgpt_daily_report_entrypoint.py" in text
    assert "scripts/update_daily_published_model_snapshots.py" in text
    assert "config/daily_pdf_rendered_model_regression_contract.csv" in text
    assert "config/daily_pdf_semantic_golden_cases.csv" in text
    assert "tests/test_chatgpt_daily_report_new_conversation_replay.py" in text
    assert "tests/test_chatgpt_daily_report_entrypoint.py" in text
    assert "docs/specs/daily_mature_model_row_level_metric_contract.md" in text
    assert "scripts/build_mature_model_row_level_metric_contract_audit.py" in text
    assert "scripts/validate_mature_model_row_level_metric_contract_audit.py" in text
    assert "tests/test_mature_model_row_level_metric_contract_audit.py" in text


def test_production_snapshot_updates_are_followed_by_dynamic_lineage_parity() -> None:
    for workflow_path in (DAILY_WORKFLOW, WARRANT_WORKFLOW):
        text = workflow_path.read_text(encoding="utf-8")
        snapshot_update_index = text.index(
            "python scripts/update_daily_published_model_snapshots.py"
        )
        snapshot_validation_index = text.index(
            "python scripts/validate_daily_published_model_snapshots.py",
            snapshot_update_index,
        )
        canonical_validation_index = text.index(
            "python scripts/validate_daily_canonical_field_lineage.py",
            snapshot_validation_index,
        )
        history_validation_index = text.index(
            "python scripts/validate_volume_v2_warrant_lineage_history_audit.py",
            canonical_validation_index,
        )

        assert (
            snapshot_update_index
            < snapshot_validation_index
            < canonical_validation_index
            < history_validation_index
        )

    pr_workflow = WORKFLOW.read_text(encoding="utf-8")
    assert "python scripts/update_daily_published_model_snapshots.py" not in pr_workflow
    assert "Validate production lineage parity ordering contract" in pr_workflow
    assert (
        "-k production_snapshot_updates_are_followed_by_dynamic_lineage_parity"
        in pr_workflow
    )


def test_pdf_replay_pr_workflow_is_renderer_contract_only_and_manually_dispatchable() -> None:
    text = PDF_REPLAY_WORKFLOW.read_text(encoding="utf-8")
    observed_paths = boundaries.workflow_pull_request_paths(text)

    assert "pull_request:" in text
    assert "workflow_dispatch:" in text
    assert observed_paths == boundaries.DAILY_PDF_REPLAY_AUTOMATIC_PATHS
    assert not (
        observed_paths & boundaries.MODEL_OUTPUT_PATHS_FORBIDDEN_FROM_DFKAI_REPLAY
    )
    for source_gate_path in (
        "config/git_worktree_materialization_contract.csv",
        "scripts/git_worktree_safety.py",
        "scripts/market_session_calendar.py",
        "scripts/resolve_daily_report_source_state.py",
        "scripts/run_chatgpt_daily_report_entrypoint.py",
        "scripts/validate_chatgpt_daily_report_new_conversation_replay.py",
        "scripts/validate_daily_publish_freshness_gate.py",
    ):
        assert source_gate_path not in observed_paths


def test_daily_production_boundary_rejects_model_output_dfkai_auto_trigger() -> None:
    text = PDF_REPLAY_WORKFLOW.read_text(encoding="utf-8")
    marker = '      - "scripts/validate_chatgpt_side_pdf_contract.py"\n'
    assert marker in text
    mutated = text.replace(
        marker,
        marker + '      - "output/latest/model_operation_readiness_latest.csv"\n',
        1,
    )

    errors = boundaries.validate_pdf_replay_automatic_paths(mutated)

    assert any("model_operation_readiness_latest.csv" in error for error in errors)
    assert any("no-font model validation" in error for error in errors)


def test_daily_model_pr_workflow_does_not_install_dfkai_or_render_pdfs() -> None:
    text = WORKFLOW.read_text(encoding="utf-8")

    assert "daily-pdf-dfkai-replay:" not in text
    assert "Install and validate DFKai-SB" not in text
    assert "Replay ChatGPT-side daily PDF new conversation" not in text


def test_daily_model_maintenance_pr_workflow_triggers_on_independence_guard_changes() -> None:
    text = WORKFLOW.read_text(encoding="utf-8")

    required_paths = (
        "config/daily_model_*.csv",
        "data/financial_statement_history/*.csv",
        "config/runtime_file_lineage_contract.csv",
        "scripts/build_model_data_independence_audit.py",
        "scripts/model_data_independence.py",
        "scripts/validate_model_data_independence.py",
        "scripts/validate_model_surface_registry.py",
        "scripts/validate_repo_code_isolation_policy.py",
        "tests/test_model_data_independence.py",
        "tests/test_model_surface_registry.py",
        "tests/test_repo_code_isolation_policy.py",
        "docs/latest/model_data_independence_audit_latest.*",
        "output/latest/model_data_independence_audit_latest.*",
        "output/latest/research_backtest/financial_statement_pit_coverage_latest.*",
        "scripts/build_financial_statement_pit.py",
        "scripts/build_volume_breakout_watch.py",
        "scripts/build_volume_attack_theme_layer.py",
        "scripts/validate_financial_statement_pit.py",
        "scripts/validate_volume_breakout_watch.py",
        "scripts/validate_volume_attack_theme_layer.py",
        "scripts/validate_daily_canonical_field_lineage.py",
        "scripts/build_volume_v2_warrant_lineage_history_audit.py",
        "scripts/build_daily_published_snapshot_ranking_backtest.py",
        "scripts/backfill_historical_all_candidates_snapshots_from_git_history.py",
        "scripts/stage_daily_published_snapshot_revisions.py",
        "scripts/validate_volume_v2_warrant_lineage_history_audit.py",
        "tests/test_financial_statement_pit.py",
        "tests/test_volume_breakout_watch.py",
        "tests/test_daily_canonical_field_lineage.py",
        "tests/test_daily_model_maintenance_pr_validation_workflow.py",
        "tests/test_volume_v2_warrant_lineage_history_audit.py",
        "tests/test_daily_published_snapshot_ranking_backtest.py",
        "tests/test_backfill_historical_all_candidates_snapshots.py",
        "tests/test_stage_daily_published_snapshot_revisions.py",
    )
    for path in required_paths:
        assert path in text


def test_daily_model_maintenance_pr_workflow_pins_append_only_validation_base() -> None:
    text = WORKFLOW.read_text(encoding="utf-8")

    assert "fetch-depth: 0" in text
    assert "BASE_SHA: ${{ github.event.pull_request.base.sha || 'origin/main' }}" in text
    assert 'if [ "$BASE_SHA" = "origin/main" ]; then' in text
    assert "git fetch --no-tags origin main:refs/remotes/origin/main" in text
    assert 'git cat-file -e "${BASE_SHA}^{commit}"' in text
    assert (
        'python scripts/validate_model_data_independence.py --base-ref "$BASE_SHA"'
        in text
    )
    assert (
        'python scripts/validate_model_research_shared_utilities.py '
        '--base-ref "$BASE_SHA"'
        in text
    )
    assert (
        'python scripts/validate_daily_canonical_field_lineage.py '
        '--base-ref "$BASE_SHA"'
        in text
    )
    assert "python scripts/validate_model_data_independence.py\n" not in text
    assert "python scripts/validate_model_research_shared_utilities.py\n" not in text
    assert "python scripts/validate_daily_canonical_field_lineage.py\n" not in text


def test_daily_model_maintenance_pr_workflow_runs_contract_validators() -> None:
    text = WORKFLOW.read_text(encoding="utf-8")

    required_commands = (
        "python scripts/validate_repo_production_inventory.py",
        "python scripts/validate_stock_model_contract_registry.py",
        "python scripts/validate_daily_pdf_contract_consumers.py",
        "python scripts/validate_daily_pdf_role_manifest_contract.py",
        "python scripts/validate_daily_pdf_completion_hard_gate.py",
        "python scripts/validate_daily_production_boundaries.py",
        'python scripts/validate_daily_published_model_snapshots_pr_safe.py --base-ref "$BASE_SHA"',
        'python scripts/validate_repo_advanced_integrity_pr_safe.py --base-ref "$BASE_SHA"',
        "python scripts/validate_daily_model_background_data_registry.py",
        "python scripts/validate_model_data_independence.py",
        'python scripts/validate_model_research_shared_utilities.py --base-ref "$BASE_SHA"',
        "python scripts/validate_volume_breakout_watch.py --latest-only",
        "python scripts/validate_volume_attack_theme_layer.py",
        "python scripts/validate_daily_canonical_field_lineage.py",
        "python scripts/build_volume_v2_warrant_lineage_history_audit.py",
        "python scripts/validate_volume_v2_warrant_lineage_history_audit.py",
        "python scripts/validate_financial_statement_pit.py",
        "python scripts/validate_revenue_unreacted_range_source_first_condition_audit.py",
        "python scripts/validate_revenue_unreacted_range_forward_confirmation_feature_audit.py",
        "python scripts/validate_revenue_unreacted_range_rearmed_operation_grid.py",
        "python scripts/validate_revenue_unreacted_range_operation_lag_bucket_audit.py",
        "python scripts/build_mature_model_row_level_metric_contract_audit.py",
        "python scripts/validate_mature_model_row_level_metric_contract_audit.py",
        "python scripts/validate_research_against_stock_model_contract.py",
        "python scripts/validate_daily_model_research_parity.py",
        "python scripts/validate_repo_hidden_coupling_audit.py",
        "python scripts/validate_repo_code_isolation_policy.py",
        "python scripts/validate_chatgpt_side_pdf_layout_independence.py",
    )
    for command in required_commands:
        assert command in text


def test_daily_model_maintenance_pr_workflow_runs_focused_pdf_operation_tests() -> None:
    text = WORKFLOW.read_text(encoding="utf-8")

    required_tests = (
        "tests/test_chatgpt_daily_report_new_conversation_replay.py",
        "tests/test_chatgpt_daily_report_entrypoint.py",
        "tests/test_daily_report_source_resolver.py",
        "tests/test_daily_pdf_contract_consumers.py",
        "tests/test_daily_pdf_completion_hard_gate.py",
        "tests/test_daily_published_model_snapshots.py",
        "tests/test_repo_advanced_integrity_pr_safe.py",
        "tests/test_backfill_historical_all_candidates_snapshots.py",
        "tests/test_daily_published_snapshot_ranking_backtest.py",
        "tests/test_stage_daily_published_snapshot_revisions.py",
        "tests/test_daily_operation_adapter_protected_fields.py",
        "tests/test_daily_volume_breakout_operation_section.py",
        "tests/test_daily_w_bottom_operation_sections.py",
        "tests/test_daily_price_pullback_23ema_operation_section.py",
        "tests/test_mature_model_row_level_metric_contract_audit.py",
        "tests/test_daily_report_model_summary.py",
        "tests/test_daily_production_boundaries.py",
        "tests/test_model_data_independence.py",
        "tests/test_volume_breakout_watch.py",
        "tests/test_daily_canonical_field_lineage.py",
        "tests/test_daily_model_maintenance_pr_validation_workflow.py",
        "tests/test_volume_v2_warrant_lineage_history_audit.py",
        "tests/test_financial_statement_pit.py",
        "tests/test_revenue_unreacted_range_source_first_condition_audit.py",
        "tests/test_revenue_unreacted_range_forward_confirmation_feature_audit.py",
        "tests/test_revenue_unreacted_range_rearmed_operation_grid.py",
        "tests/test_revenue_unreacted_range_operation_lag_bucket_audit.py",
        "tests/test_repo_hidden_coupling_audit.py",
        "tests/test_stock_model_contract_registry.py",
    )
    for path in required_tests:
        assert path in text


def test_daily_model_pr_focused_suite_replaces_only_strict_runtime_integrity_test() -> None:
    text = WORKFLOW.read_text(encoding="utf-8")
    focused = text.split("- name: Run focused regression tests", 1)[1]
    strict_node = (
        "tests/test_repo_advanced_integrity.py::"
        "test_repo_advanced_integrity_validator_passes"
    )

    assert "tests/test_repo_advanced_integrity.py" in focused
    assert f"--deselect {strict_node}" in focused
    assert focused.count("--deselect") == 1
    assert "--ignore=tests/test_repo_advanced_integrity.py" not in focused
    assert "-k " not in focused


def test_pdf_impact_pr_workflow_runs_actual_pdf_replay_and_uploads_evidence() -> None:
    text = PDF_REPLAY_WORKFLOW.read_text(encoding="utf-8")
    replay_job = boundaries.workflow_job_block(text, "daily-pdf-dfkai-replay")

    assert "Replay ChatGPT-side daily PDF new conversation" in text
    assert "python scripts/validate_chatgpt_daily_report_new_conversation_replay.py" in text
    assert "timeout-minutes: 20" in text
    assert "timeout 20m python scripts/validate_chatgpt_daily_report_new_conversation_replay.py" in text
    assert "PDF replay source_ref=$source_ref" in text
    assert "PDF replay output_dir=chatgpt_side_outputs_pr_validation" in text
    assert "--source-ref \"$source_ref\"" in text
    assert "--output-dir chatgpt_side_outputs_pr_validation" in text
    assert "--require-output-dir chatgpt_side_outputs_pr_validation" in text
    assert "PDF_REPLAY_SOURCE_SHA: ${{ github.event.pull_request.head.sha || github.sha }}" in replay_job
    assert 'checkout_sha="$(git rev-parse HEAD)"' in replay_job
    assert 'if [ "$checkout_sha" != "$GITHUB_SHA" ]; then' in replay_job
    assert 'source_sha="$PDF_REPLAY_SOURCE_SHA"' in replay_job
    assert 'git fetch --no-tags --depth=1 origin "$source_sha"' in replay_job
    assert 'fetched_source_sha="$(git rev-parse FETCH_HEAD)"' in replay_job
    assert 'if [ "$fetched_source_sha" != "$source_sha" ]; then' in replay_job
    assert 'pinned_remote="pinned-replay"' in replay_job
    assert 'pinned_branch="workflow-${GITHUB_RUN_ID}-${GITHUB_RUN_ATTEMPT}"' in replay_job
    assert 'git branch --force "$pinned_branch" "$source_sha"' in replay_job
    assert 'git remote add "$pinned_remote" "$PWD"' in replay_job
    assert 'git fetch "$pinned_remote" "$pinned_branch"' in replay_job
    assert 'source_ref="$pinned_remote/$pinned_branch"' in replay_job
    assert 'resolved_source_sha="$(git rev-parse "$source_ref")"' in replay_job
    assert 'if [ "$resolved_source_sha" != "$source_sha" ]; then' in replay_job
    assert "PDF replay workflow_checkout_sha=$GITHUB_SHA" in replay_job
    assert "PDF replay source_sha=$source_sha" in replay_job
    assert "GITHUB_HEAD_REF" not in replay_job
    assert "GITHUB_REF_NAME" not in replay_job
    assert 'source_ref="origin/' not in replay_job
    assert "Upload PR daily PDF replay evidence" in text
    assert "actions/upload-artifact@v4" in text
    assert "daily-pdf-replay-pr-validation" in text
    assert "chatgpt_side_outputs_pr_validation/*.pdf" in text
    assert "chatgpt_side_outputs_pr_validation/chatgpt_daily_report_runtime_manifest.json" in text
    assert "chatgpt_side_outputs_pr_validation/chatgpt_daily_pdf_semantic_manifest.csv" in text
    assert "if-no-files-found: error" in text


def test_pdf_replay_local_remote_ref_stays_pinned_when_checked_out_branch_advances(
    tmp_path: Path,
) -> None:
    repo = tmp_path / "repo"
    repo.mkdir()
    run_git(repo, "init", "--initial-branch=main")
    run_git(repo, "config", "user.email", "workflow-test@example.invalid")
    run_git(repo, "config", "user.name", "Workflow Test")
    marker = repo / "marker.txt"
    marker.write_text("pinned\n", encoding="utf-8")
    run_git(repo, "add", "marker.txt")
    run_git(repo, "commit", "-m", "pinned source")

    source_sha = run_git(repo, "rev-parse", "HEAD")
    pinned_remote = "pinned-replay"
    pinned_branch = "workflow-123-1"
    run_git(repo, "branch", "--force", pinned_branch, source_sha)
    run_git(repo, "remote", "add", pinned_remote, str(repo))
    run_git(repo, "fetch", pinned_remote, pinned_branch)
    source_ref = f"{pinned_remote}/{pinned_branch}"
    assert run_git(repo, "rev-parse", source_ref) == source_sha

    marker.write_text("moving main\n", encoding="utf-8")
    run_git(repo, "add", "marker.txt")
    run_git(repo, "commit", "-m", "advance main")
    assert run_git(repo, "rev-parse", "HEAD") != source_sha
    run_git(repo, "fetch", pinned_remote, pinned_branch)
    assert run_git(repo, "rev-parse", source_ref) == source_sha


def test_daily_production_boundary_accepts_immutable_pr_pdf_replay_source_pin() -> None:
    text = PDF_REPLAY_WORKFLOW.read_text(encoding="utf-8")
    assert boundaries.validate_pr_pdf_replay_source_pin(text) == []


def test_daily_production_boundary_rejects_moving_pr_pdf_replay_source_ref() -> None:
    invalid = """
jobs:
  daily-pdf-dfkai-replay:
    steps:
      - name: Replay ChatGPT-side daily PDF new conversation
        run: |
          source_ref="origin/${GITHUB_HEAD_REF}"
          git fetch origin "${source_ref#origin/}"
          python scripts/validate_chatgpt_daily_report_new_conversation_replay.py --source-ref "$source_ref"
"""
    errors = boundaries.validate_pr_pdf_replay_source_pin(invalid)
    assert any("moving pull-request branch ref" in error for error in errors)
    assert any("moving origin ref" in error for error in errors)
    assert any("immutable PR head SHA" in error for error in errors)


def test_daily_pdf_replay_jobs_require_windows_dfkai_runtime() -> None:
    daily_text = DAILY_WORKFLOW.read_text(encoding="utf-8")
    pr_text = PDF_REPLAY_WORKFLOW.read_text(encoding="utf-8")

    assert boundaries.validate_dfkai_pdf_replay_job(
        daily_text,
        workflow_label="daily_full_pipeline",
        needs_job="[market-session-preflight, record-market-closure, daily-full-pipeline]",
        output_dir="chatgpt_side_outputs_new_conversation_replay",
        upload_step="Upload main daily PDF replay evidence",
    ) == []
    assert boundaries.validate_dfkai_pdf_replay_job(
        pr_text,
        workflow_label="daily_pdf_replay_pr_validation",
        needs_job="daily-pdf-replay-contract-validation",
        output_dir="chatgpt_side_outputs_pr_validation",
        upload_step="Upload PR daily PDF replay evidence",
    ) == []
    assert boundaries.workflow_step_block(
        daily_text,
        "Install and validate DFKai-SB",
    ) == boundaries.workflow_step_block(
        pr_text,
        "Install and validate DFKai-SB",
    )
    assert "Replay ChatGPT-side daily PDF" not in boundaries.workflow_job_block(
        daily_text,
        "daily-full-pipeline",
    )
    assert "Replay ChatGPT-side daily PDF" not in boundaries.workflow_job_block(
        pr_text,
        "daily-model-maintenance-pr-validation",
    )


def test_dfkai_replay_job_validator_rejects_generic_or_ubuntu_job() -> None:
    invalid = """
jobs:
  daily-pdf-dfkai-replay:
    needs: upstream
    runs-on: ubuntu-latest
    steps:
      - name: Replay ChatGPT-side daily PDF new conversation
        run: python scripts/validate_chatgpt_daily_report_new_conversation_replay.py
"""

    errors = boundaries.validate_dfkai_pdf_replay_job(
        invalid,
        workflow_label="fixture",
        needs_job="upstream",
        output_dir="expected-output",
        upload_step="Upload evidence",
    )

    assert any("windows-2025" in error for error in errors)
    assert any("Language.Fonts.Hant" in error for error in errors)
    assert any("Windows Update" in error for error in errors)
    assert any("DISM" in error for error in errors)
    assert any("long-path" in error for error in errors)
    assert any("temporary" in error for error in errors)
    assert any("kaiu.ttf" in error for error in errors)
    assert any("DFKai-SB" in error for error in errors)


def test_dfkai_replay_job_validator_requires_post_validation_dism_recovery() -> None:
    text = PDF_REPLAY_WORKFLOW.read_text(encoding="utf-8")
    recovery_block = """          if ($dismExitCode -ne 0) {
            Write-Warning "DISM returned exit code $dismExitCode, but canonical DFKai-SB passed final file, identity, and glyph validation"
          }
"""
    env_line = (
        '          "CHATGPT_DAILY_DFKAI_FONT_PATH=$fontPath" | '
        "Out-File -FilePath $env:GITHUB_ENV -Append -Encoding utf8\n"
    )
    assert recovery_block in text
    assert env_line in text

    reordered = text.replace(recovery_block, "", 1).replace(
        env_line,
        recovery_block + env_line,
        1,
    )
    errors = boundaries.validate_dfkai_pdf_replay_job(
        reordered,
        workflow_label="fixture",
        needs_job="daily-pdf-replay-contract-validation",
        output_dir="chatgpt_side_outputs_pr_validation",
        upload_step="Upload PR daily PDF replay evidence",
    )

    assert any("final-state validation order" in error for error in errors)


def test_dfkai_replay_job_validator_rejects_immediate_dism_exit_failure() -> None:
    text = PDF_REPLAY_WORKFLOW.read_text(encoding="utf-8")
    capture = "              $dismExitCode = $LASTEXITCODE\n"
    assert capture in text
    immediate_failure = (
        capture
        + '              throw "DFKai-SB capability installation failed with DISM exit code $LASTEXITCODE"\n'
    )
    mutated = text.replace(capture, immediate_failure, 1)

    errors = boundaries.validate_dfkai_pdf_replay_job(
        mutated,
        workflow_label="fixture",
        needs_job="daily-pdf-replay-contract-validation",
        output_dir="chatgpt_side_outputs_pr_validation",
        upload_step="Upload PR daily PDF replay evidence",
    )

    assert any("before rejecting a DISM exit code" in error for error in errors)


def test_dfkai_replay_job_validator_rejects_missing_font_warning_only() -> None:
    text = PDF_REPLAY_WORKFLOW.read_text(encoding="utf-8")
    fail_closed = (
        'throw "Required DFKai-SB font file is missing after capability install: '
        '$fontPath (DISM exit code $dismExitCode)"'
    )
    assert fail_closed in text
    mutated = text.replace(fail_closed, fail_closed.replace("throw", "Write-Warning"), 1)

    errors = boundaries.validate_dfkai_pdf_replay_job(
        mutated,
        workflow_label="fixture",
        needs_job="daily-pdf-replay-contract-validation",
        output_dir="chatgpt_side_outputs_pr_validation",
        upload_step="Upload PR daily PDF replay evidence",
    )

    assert any("canonical font file remains missing" in error for error in errors)


def test_dfkai_replay_job_validator_rejects_font_validation_warning_only() -> None:
    text = PDF_REPLAY_WORKFLOW.read_text(encoding="utf-8")
    fail_closed = (
        'throw "DFKai-SB final font validation failed with exit code '
        '$fontValidationExitCode (DISM exit code $dismExitCode)"'
    )
    assert fail_closed in text
    mutated = text.replace(fail_closed, fail_closed.replace("throw", "Write-Warning"), 1)

    errors = boundaries.validate_dfkai_pdf_replay_job(
        mutated,
        workflow_label="fixture",
        needs_job="daily-pdf-replay-contract-validation",
        output_dir="chatgpt_side_outputs_pr_validation",
        upload_step="Upload PR daily PDF replay evidence",
    )

    assert any("font identity or glyph validation fails" in error for error in errors)


def test_dfkai_replay_job_validator_rejects_disabled_font_identity_assertion() -> None:
    text = PDF_REPLAY_WORKFLOW.read_text(encoding="utf-8")
    assert "assert names & accepted" in text
    mutated = text.replace("assert names & accepted", "print(names & accepted)", 1)

    errors = boundaries.validate_dfkai_pdf_replay_job(
        mutated,
        workflow_label="fixture",
        needs_job="daily-pdf-replay-contract-validation",
        output_dir="chatgpt_side_outputs_pr_validation",
        upload_step="Upload PR daily PDF replay evidence",
    )

    assert any("unexpected font identity" in error for error in errors)


def test_dfkai_replay_job_validator_rejects_disabled_glyph_assertion() -> None:
    text = PDF_REPLAY_WORKFLOW.read_text(encoding="utf-8")
    assert "assert not missing" in text
    mutated = text.replace("assert not missing", "print(missing)", 1)

    errors = boundaries.validate_dfkai_pdf_replay_job(
        mutated,
        workflow_label="fixture",
        needs_job="daily-pdf-replay-contract-validation",
        output_dir="chatgpt_side_outputs_pr_validation",
        upload_step="Upload PR daily PDF replay evidence",
    )

    assert any("canary glyphs are missing" in error for error in errors)
