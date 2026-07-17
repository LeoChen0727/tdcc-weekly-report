from __future__ import annotations

from pathlib import Path

import pytest

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


def test_event_and_weekly_workflows_publish_pages_and_use_full_validation() -> None:
    for workflow in [
        ROOT / ".github" / "workflows" / "event_catalyst_update.yml",
        ROOT / ".github" / "workflows" / "weekly_theme_review.yml",
    ]:
        text = workflow.read_text(encoding="utf-8")
        assert "actions: write" in text
        assert "actions/checkout@v6.0.3" in text
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
        assert "python scripts/validate_daily_published_model_snapshots.py" in text
        assert "python scripts/validate_daily_staged_paths.py" in text
        assert 'capture_mature_sentinels "$mature_sentinel_before"' in text
        assert 'capture_mature_sentinels "$mature_sentinel_after"' in text
        assert 'cmp --silent "$mature_sentinel_before" "$mature_sentinel_after"' in text
        assert "mature_model_sentinel_before_sha256=" in text
        assert "mature_model_sentinel_after_sha256=" in text
        assert "mature_model_sentinel_artifact_count=" in text
        assert "git add output/history/daily_candidate_models/" in text
        assert "git add output/history/daily_model_snapshots/" in text
        assert "git add docs/latest/" in text
        assert "gh workflow run pages.yml --ref main" in text
        assert "timeout-minutes: 40" in text
        assert "pages_deploy_attempts=3" in text
        assert "for poll_attempt in {1..44}" in text
        assert "GitHub Pages deploy did not succeed after" in text
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
        snapshot_validate_index = text.index("python scripts/validate_daily_published_model_snapshots.py")
        pages_sync_index = text.index("python scripts/sync_catalyst_pages_artifacts.py")
        indicator_guide_index = text.index("python scripts/build_chatgpt_indicator_usage_guide.py")
        sentinel_after_index = text.index('capture_mature_sentinels "$mature_sentinel_after"')
        staged_validate_index = text.index("python scripts/validate_daily_staged_paths.py")
        commit_index = text.index("git commit -m")
        assert (
            sentinel_before_index
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
