from __future__ import annotations

from pathlib import Path

import pytest
import yaml

from scripts.sync_catalyst_pages_artifacts import CATALYST_PAGES_ARTIFACTS, sync_artifacts


ROOT = Path(__file__).resolve().parents[1]


def test_sync_catalyst_pages_artifacts_copies_required_files(tmp_path: Path) -> None:
    latest = tmp_path / "output" / "latest"
    docs_latest = tmp_path / "docs" / "latest"
    latest.mkdir(parents=True)

    for name in CATALYST_PAGES_ARTIFACTS:
        (latest / name).write_text(f"{name}\n", encoding="utf-8")

    copied = sync_artifacts(latest, docs_latest)

    assert len(copied) == len(CATALYST_PAGES_ARTIFACTS)
    for name in CATALYST_PAGES_ARTIFACTS:
        assert (docs_latest / name).read_text(encoding="utf-8") == f"{name}\n"


def test_sync_catalyst_pages_artifacts_fails_on_missing_source(tmp_path: Path) -> None:
    latest = tmp_path / "output" / "latest"
    docs_latest = tmp_path / "docs" / "latest"
    latest.mkdir(parents=True)

    with pytest.raises(FileNotFoundError, match="missing catalyst Pages artifact"):
        sync_artifacts(latest, docs_latest, ["catalyst_summary_latest.md"])


def test_event_workflow_is_source_only_and_prepares_protected_artifact_pr() -> None:
    workflow = ROOT / ".github" / "workflows" / "event_catalyst_update.yml"
    text = workflow.read_text(encoding="utf-8")
    parsed_workflow = yaml.safe_load(text)

    assert parsed_workflow["jobs"]
    assert "workflow_dispatch:" in text
    assert "schedule:" not in text
    assert "contents: read" in text
    assert "actions: write" not in text
    assert "Require production artifact write deploy key" in text
    assert (
        "PRODUCTION_ARTIFACT_WRITE_DEPLOY_KEY: "
        "${{ secrets.PRODUCTION_ARTIFACT_WRITE_DEPLOY_KEY }}"
    ) in text
    assert 'if [ -z "${PRODUCTION_ARTIFACT_WRITE_DEPLOY_KEY}" ]; then' in text
    assert "actions/checkout@v6.0.3" in text
    assert "ssh-key: ${{ secrets.PRODUCTION_ARTIFACT_WRITE_DEPLOY_KEY }}" in text
    assert "persist-credentials: true" in text
    assert "group: daily-full-pipeline-${{ github.ref }}" in text
    assert "cancel-in-progress: false" in text
    assert "ref: main" in text
    assert "Enforce main-only mutation" in text
    assert 'if [[ "${GITHUB_REF}" != "refs/heads/main" ]]; then' in text
    assert 'test "$(git branch --show-current)" = "main"' in text
    assert "actions/setup-python@v6.2.0" in text
    assert "tabulate lxml html5lib beautifulsoup4" in text

    required_commands = (
        "python scripts/update_event_catalyst_data.py",
        "python scripts/update_event_calendar_data.py",
        "python scripts/validate_event_catalyst_overlay_contract.py",
        "python scripts/validate_event_calendar_data.py",
        "python scripts/validate_catalyst_layer.py --schema-only",
        "python scripts/validate_daily_production_boundaries.py",
        "python scripts/build_event_catalyst_historical_recovery_manifest.py",
        "python scripts/validate_event_catalyst_historical_recovery_manifest.py",
        "python scripts/validate_event_catalyst_source_refresh_scope.py",
    )
    for command in required_commands:
        assert command in text

    forbidden_commands = (
        "python scripts/validate_data_freshness_latest.py",
        "python scripts/apply_fundamental_catalyst_layer.py",
        "python scripts/update_catalyst_performance.py",
        "python scripts/build_daily_candidate_model_layer.py",
        "python scripts/validate_daily_candidate_model_layer.py",
        "python scripts/build_daily_report_model_summary.py",
        "python scripts/audit_daily_candidate_model_selection_correctness.py",
        "python scripts/audit_daily_candidate_pipeline_integrity.py",
        "python scripts/build_theme_event_watch.py",
        "python scripts/update_daily_published_model_snapshots.py",
        "python scripts/validate_daily_published_model_snapshots.py",
        "python scripts/stage_daily_published_snapshot_revisions.py",
        "python scripts/validate_daily_event_catalyst_formal_sync_scope.py",
        "python scripts/validate_daily_staged_paths.py",
        "python scripts/sync_catalyst_pages_artifacts.py",
        "python scripts/build_chatgpt_indicator_usage_guide.py",
    )
    for command in forbidden_commands:
        assert command not in text

    for forbidden_path in (
        "output/latest/all_candidates_latest",
        "output/latest/daily_candidate",
        "output/history/daily_candidate_models",
        "output/history/daily_model_snapshots",
        "docs/latest/daily_candidate",
    ):
        assert forbidden_path not in text

    required_artifacts = (
        "upcoming_catalyst_calendar_latest.csv",
        "upcoming_macro_event_calendar_latest.csv",
        "calendar_data_source_status_latest.json",
        "catalyst_data_source_status_latest.json",
        "catalyst_needs_review_latest.csv",
        "event_calendar_validation_latest.json",
        "catalyst_layer_validation_latest.json",
        "event_catalyst_historical_recovery_latest.json",
    )
    for artifact in required_artifacts:
        assert artifact in text

    prepare_index = text.index("python scripts/update_event_catalyst_data.py")
    calendar_index = text.index("python scripts/update_event_calendar_data.py")
    source_validate_index = text.index("python scripts/validate_event_calendar_data.py")
    recovery_index = text.index(
        "python scripts/build_event_catalyst_historical_recovery_manifest.py"
    )
    staged_gate_index = text.index(
        "python scripts/validate_event_catalyst_source_refresh_scope.py"
    )
    commit_index = text.index('git commit -m "Update event catalyst source tables"')
    assert (
        prepare_index
        < calendar_index
        < source_validate_index
        < recovery_index
        < staged_gate_index
        < commit_index
    )

    assert "git add output/history/event_catalyst_recovery/ || true" in text
    assert "git add docs/latest/ || true" not in text
    assert "artifact_commit_created=false" in text
    assert "artifact_commit_created=true" in text
    assert 'if [ "$artifact_commit_created" = "true" ]; then' in text
    assert "if git diff --cached --quiet; then" in text
    assert 'echo "BUILD_BASE_SHA=$build_base_sha" >> "$GITHUB_ENV"' in text
    assert 'if [ "$current_origin_main" != "$BUILD_BASE_SHA" ]; then' in text
    assert "git push origin HEAD:main" not in text
    assert (
        'artifact_branch="codex/event-catalyst-artifacts-'
        '${GITHUB_RUN_ID}-${GITHUB_RUN_ATTEMPT}"'
    ) in text
    assert 'git push origin "HEAD:refs/heads/$artifact_branch"' in text
    assert "Event/catalyst artifact PR required" in text
    assert "An external operator must open the artifact PR" in text
    assert "gh pr create" not in text
    assert "git pull --rebase origin main" not in text
    assert "gh workflow run pages.yml --ref main" not in text
    assert "Dispatch and wait for catalyst Pages deploy" not in text

    preflight_index = text.index("Require production artifact write deploy key")
    checkout_index = text.index("- name: Checkout")
    branch_push_index = text.index(
        'git push origin "HEAD:refs/heads/$artifact_branch"'
    )
    assert preflight_index < checkout_index < prepare_index < branch_push_index


def test_weekly_workflow_publishes_pages_and_uses_full_validation() -> None:
    workflows = {
        ROOT / ".github" / "workflows" / "weekly_theme_review.yml": (
            "weekly_theme_formal_sync"
        ),
    }
    for workflow, revision_reason in workflows.items():
        text = workflow.read_text(encoding="utf-8")
        parsed_workflow = yaml.safe_load(text)
        assert parsed_workflow["jobs"]
        assert "actions: write" in text
        assert "actions/checkout@v6.0.3" in text
        assert "group: daily-full-pipeline-${{ github.ref }}" in text
        assert "cancel-in-progress: false" in text
        assert "ref: main" in text
        assert "Enforce main-only mutation" in text
        assert 'if [[ "${GITHUB_REF}" != "refs/heads/main" ]]; then' in text
        assert 'test "$(git branch --show-current)" = "main"' in text
        assert "actions/setup-python@v6.2.0" in text
        assert "tabulate lxml html5lib beautifulsoup4" in text
        assert "python scripts/build_theme_event_watch.py" in text
        assert "python scripts/sync_catalyst_pages_artifacts.py" in text
        assert "python scripts/build_daily_candidate_model_layer.py" in text
        assert "python scripts/validate_daily_candidate_model_layer.py" in text
        assert "python scripts/validate_revenue_unreacted_range_financial_statement_fail_closed.py" in text
        assert "python scripts/build_daily_report_model_summary.py" in text
        assert "python scripts/audit_daily_candidate_model_selection_correctness.py" in text
        assert "python scripts/audit_daily_candidate_pipeline_integrity.py" in text
        assert "python scripts/update_daily_published_model_snapshots.py" in text
        assert f"--revision-reason {revision_reason}" in text
        assert "python scripts/validate_daily_published_model_snapshots.py" in text
        assert "python scripts/validate_daily_staged_paths.py" in text
        assert "python scripts/validate_daily_event_catalyst_formal_sync_scope.py" in text
        assert "python scripts/validate_daily_event_catalyst_formal_sync_scope.py --validate-staged" in text
        assert '--write-snapshot "$formal_sync_scope_before"' in text
        assert '--compare-snapshot "$formal_sync_scope_before"' in text
        assert 'capture_mature_sentinels "$mature_sentinel_before"' in text
        assert 'capture_mature_sentinels "$mature_sentinel_after"' in text
        assert 'cmp --silent "$mature_sentinel_before" "$mature_sentinel_after"' in text
        assert 'row["snapshot_revision"] = row.get("snapshot_revision") or "r1"' in text
        assert '"legacy_v1_manifest" if row["snapshot_revision"] == "r1"' in text
        assert ":{row.get('snapshot_revision', '')}" in text
        assert "mature_model_sentinel_before_sha256=" in text
        assert "mature_model_sentinel_after_sha256=" in text
        assert "mature_model_sentinel_artifact_count=" in text
        assert "git add output/history/daily_candidate_models/daily_candidate_model_signal_log.csv" in text
        assert "git add output/history/daily_candidate_models/ || true" not in text
        assert "git add output/history/daily_model_snapshots/ || true" not in text
        assert "git add docs/latest/ || true" not in text
        commit_block = text[
            text.index("- name: Commit") :
            text.index("- name: Dispatch and wait for catalyst Pages deploy")
        ]
        assert commit_block.count(
            "python scripts/stage_daily_published_snapshot_revisions.py"
        ) == 1
        for artifact_id in (
            "data_freshness",
            "model_signals_for_report",
            "all_candidates_source_rows",
            "model_summary_for_report",
        ):
            assert commit_block.count(f"--artifact-id {artifact_id}") == 1
        assert 'daily_model_snapshots/data_freshness_${snapshot_report_date}"*.csv' not in commit_block
        for artifact_id in (
            "data_freshness",
            "model_signals_for_report",
            "all_candidates_source_rows",
            "model_summary_for_report",
        ):
            assert f"--artifact-id {artifact_id}" in text
        assert "if git diff --cached --quiet; then" in text
        assert "bash scripts/ci_push_with_retry.sh main 5" not in text
        assert 'echo "BUILD_BASE_SHA=$build_base_sha" >> "$GITHUB_ENV"' in text
        assert 'if [ "$current_origin_main" != "$BUILD_BASE_SHA" ]; then' in text
        assert "git push origin HEAD:main" in text
        assert 'echo "ARTIFACT_COMMIT_CREATED=false" >> "$GITHUB_ENV"' in text
        assert 'echo "ARTIFACT_COMMIT_CREATED=true" >> "$GITHUB_ENV"' in text
        assert "GITHUB_REF_NAME" not in text
        assert "git pull --rebase origin main" not in text
        assert "\n          git push\n" not in text
        assert 'git commit -m "' in text
        assert 'git commit -m "Update' in text
        assert '|| echo "No changes to commit"' not in text
        assert "gh workflow run pages.yml --ref main" in text
        assert "timeout-minutes: 40" in text
        assert "pages_deploy_attempts=3" not in text
        assert "for poll_attempt in {1..150}" in text
        assert 'target_sha="$PUSHED_ARTIFACT_SHA"' in text
        assert '--commit "$target_sha"' in text
        assert 'pages_head_sha" != "$target_sha"' in text
        assert "Timed out waiting for exact-sha GitHub Pages deploy" in text
        assert "validate_event_calendar_data.py --schema-only" not in text
        assert "validate_catalyst_layer.py --schema-only" not in text
        for forbidden in [
            "build_daily_" + "volume_breakout_operation_section.py",
            "build_daily_" + "w_bottom_operation_sections.py",
            "build_daily_" + "price_pullback_23ema_operation_section.py",
            "build_mature_model_" + "row_level_metric_contract_audit.py",
            "git add output/latest/daily_volume_breakout_operation_",
            "git add output/latest/daily_w_bottom_right_side_operation_",
            "git add output/latest/daily_neckline_volume_breakout_confirmation_operation_",
            "git add output/latest/daily_price_pullback_23ema_operation_",
            "git add output/latest/mature_model_row_level_metric_",
        ]:
            assert forbidden not in text

        main_guard_index = text.index("Enforce main-only mutation")
        snapshot_baseline_index = text.index(
            "python scripts/validate_daily_published_model_snapshots.py"
        )
        sentinel_before_index = text.index('capture_mature_sentinels "$mature_sentinel_before"')
        catalyst_index = text.index("python scripts/apply_fundamental_catalyst_layer.py")
        catalyst_performance_index = text.index("python scripts/update_catalyst_performance.py")
        event_calendar_validate_index = text.index("python scripts/validate_event_calendar_data.py")
        catalyst_validate_index = text.index("python scripts/validate_catalyst_layer.py")
        model_build_index = text.index("python scripts/build_daily_candidate_model_layer.py")
        model_validate_index = text.index("python scripts/validate_daily_candidate_model_layer.py")
        revenue_fail_closed_index = text.index(
            "python scripts/validate_revenue_unreacted_range_financial_statement_fail_closed.py"
        )
        model_summary_index = text.index("python scripts/build_daily_report_model_summary.py")
        selection_audit_index = text.index(
            "python scripts/audit_daily_candidate_model_selection_correctness.py"
        )
        integrity_audit_index = text.index(
            "python scripts/audit_daily_candidate_pipeline_integrity.py"
        )
        theme_watch_index = text.index("python scripts/build_theme_event_watch.py")
        snapshot_update_index = text.index("python scripts/update_daily_published_model_snapshots.py")
        snapshot_validate_index = text.index(
            "python scripts/validate_daily_published_model_snapshots.py",
            snapshot_update_index,
        )
        pages_sync_index = text.index("python scripts/sync_catalyst_pages_artifacts.py")
        indicator_guide_index = text.index("python scripts/build_chatgpt_indicator_usage_guide.py")
        sentinel_after_index = text.index('capture_mature_sentinels "$mature_sentinel_after"')
        staged_validate_index = text.index("python scripts/validate_daily_staged_paths.py")
        commit_index = text.index("git commit -m")
        assert (
            main_guard_index
            < snapshot_baseline_index
            < sentinel_before_index
            < catalyst_index
            < catalyst_performance_index
            < event_calendar_validate_index
            < catalyst_validate_index
            < model_build_index
            < model_validate_index
            < revenue_fail_closed_index
            < model_summary_index
            < selection_audit_index
            < integrity_audit_index
            < theme_watch_index
            < snapshot_update_index
            < snapshot_validate_index
            < pages_sync_index
            < indicator_guide_index
            < sentinel_after_index
            < staged_validate_index
            < commit_index
        )

        for artifact in [
            "daily_candidate_model_parameters_latest.csv",
            "daily_candidate_model_signals_latest.csv",
            "daily_candidate_model_signals_for_report_latest.csv",
            "daily_candidate_frontpage_unique_latest.csv",
            "daily_candidate_same_model_repeat_latest.csv",
            "daily_candidate_model_layer_packet_latest.md",
            "daily_candidate_model_layer_validation_latest.json",
            "daily_candidate_model_selection_audit_latest.json",
            "daily_candidate_pipeline_integrity_audit_latest.json",
            "daily_candidate_group_rotation_latest.csv",
            "daily_report_model_registry_latest.csv",
            "daily_candidate_model_summary_for_report_latest.csv",
        ]:
            assert artifact in text

        for protected_pattern in [
            "output/latest/approved_operation_patterns_latest.*",
            "output/latest/model_operation_readiness_latest.*",
            "output/latest/daily_volume_breakout_operation_*_latest.*",
            "output/latest/daily_w_bottom_right_side_operation_*_latest.*",
            "output/latest/daily_neckline_volume_breakout_confirmation_operation_*_latest.*",
            "output/latest/daily_price_pullback_23ema_operation_*_latest.*",
            "output/latest/mature_model_row_level_metric_*_latest.*",
        ]:
            assert protected_pattern in text


def test_pages_deploy_timeout_stays_within_action_limit() -> None:
    text = (ROOT / ".github" / "workflows" / "pages.yml").read_text(
        encoding="utf-8"
    )
    assert "uses: actions/deploy-pages@v5.0.0" in text
    assert "timeout: \"1800000\"" not in text


def test_daily_workflow_syncs_catalyst_pages_artifacts() -> None:
    text = (ROOT / ".github" / "workflows" / "daily_full_pipeline.yml").read_text(
        encoding="utf-8"
    )
    assert "python scripts/sync_catalyst_pages_artifacts.py" in text
    assert "Dispatch and wait for GitHub Pages deploy" in text
    assert "timeout-minutes: 40" in text
    assert "pages_deploy_attempts=3" in text
    assert "for poll_attempt in {1..44}" in text
    assert "GitHub Pages deploy did not succeed after" in text
