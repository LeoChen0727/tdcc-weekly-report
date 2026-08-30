from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DAILY_WORKFLOW = ROOT / ".github" / "workflows" / "daily_full_pipeline.yml"
MONITORING_WORKFLOW_RELATIVE = (
    ".github/workflows/revenue_unreacted_range_post_launch_monitoring.yml"
)
MONITORING_WORKFLOW = ROOT / MONITORING_WORKFLOW_RELATIVE


def _block(text: str, start: str, end: str) -> str:
    start_index = text.index(start)
    end_index = text.index(end, start_index)
    return text[start_index:end_index]


def test_daily_full_revenue_adapter_is_fail_closed_on_four_readiness_flags() -> None:
    text = DAILY_WORKFLOW.read_text(encoding="utf-8")
    resolver = _block(
        text,
        "- name: Resolve revenue v2 formal operation readiness",
        "- name: Build revenue v2 formal operation adapter",
    )
    builder = _block(
        text,
        "- name: Build revenue v2 formal operation adapter",
        "- name: Record disabled revenue v2 formal operation skip",
    )
    disabled = _block(
        text,
        "- name: Record disabled revenue v2 formal operation skip",
        "- name: Publish and validate volume v2 audit-source snapshots",
    )

    assert 'Path("output/latest/model_operation_readiness_latest.csv")' in resolver
    assert 'row.get("model_id", "").strip() == "revenue_unreacted_range"' in resolver
    for field in (
        "formal_model_use_allowed",
        "approved_for_daily",
        "presentation_allowed",
        "production_allowed",
    ):
        assert f'"{field}"' in resolver
    assert 'row.get(field, "").strip() == "True"' in resolver
    assert "len(matching_rows) == 1" in resolver
    assert (
        '== "revenue_unreacted_range_source_mid_falling_v2_operation_v2"'
        in resolver
    )
    assert '== "pdf_integrated_daily_adapter"' in resolver
    for section in (
        "active_operation",
        "confirmed_operation",
        "confirmed_unranked_operation",
        "pending_confirmation",
    ):
        assert f'"{section}"' in resolver
    assert "len(observed_section_tokens) == len(expected_sections)" in resolver
    assert "observed_sections == expected_sections" in resolver
    assert "if: steps.revenue-v2-readiness.outputs.enabled == 'true'" in builder
    assert (
        "python scripts/build_daily_revenue_unreacted_range_operation_section.py"
        in builder
    )
    assert '--report-date "$EXPECTED_MAIN_PRICE_DATE"' in builder
    assert (
        "python scripts/validate_daily_revenue_unreacted_range_operation_section.py"
        in builder
    )
    assert "no runtime artifact was produced" in disabled
    assert "build_daily_revenue_unreacted_range_operation_section.py" not in disabled


def test_daily_full_revenue_artifact_copy_snapshot_and_stage_are_conditional() -> None:
    text = DAILY_WORKFLOW.read_text(encoding="utf-8")
    publish = _block(
        text,
        "- name: Publish and validate post-audit daily model snapshots",
        "- name: Validate catalyst layer",
    )
    pages = _block(
        text,
        "- name: Prepare GitHub Pages packet and rules files",
        "- name: Prepare daily authority release before immutable snapshot finalization",
    )
    staging = _block(
        text,
        "- name: Stage immutable published snapshot revisions",
        "- name: Validate immutable published snapshot revisions",
    )
    commit = _block(
        text,
        "- name: Commit report artifacts, packets, and rules first",
        "- name: Wait briefly for GitHub Pages and raw propagation",
    )

    assert "$REVENUE_UNREACTED_RANGE_V2_SNAPSHOT_ARGS" in publish
    assert "$REVENUE_UNREACTED_RANGE_V2_SNAPSHOT_ARGS" in staging
    assert (
        "--artifact-id revenue_unreacted_range_operation_section" in text
    )
    assert "if enabled and snapshot_registered" in text
    assert "if enabled and not snapshot_registered" in text
    assert "published snapshot artifact id is not registered" in text
    for suffix in ("csv", "md"):
        artifact = (
            "daily_revenue_unreacted_range_operation_section_latest."
            f"{suffix}"
        )
        assert artifact in pages
        assert artifact in commit
    assert 'if [ "$REVENUE_UNREACTED_RANGE_V2_ENABLED" = "true" ]' in pages
    assert 'if [ "$REVENUE_UNREACTED_RANGE_V2_ENABLED" = "true" ]' in commit
    assert (
        "output/history/daily_model_snapshots/"
        "daily_revenue_unreacted_range_operation_section_*.csv"
        in commit
    )


def test_post_launch_monitoring_dispatches_only_frozen_revenue_v2_inputs() -> None:
    text = MONITORING_WORKFLOW.read_text(encoding="utf-8")

    assert 'cron: "30 13 * * 1-5"' in text
    assert "workflow_dispatch:" in text
    assert "contents: read" in text
    assert "actions: write" in text
    assert "ref: main" in text
    assert 'Path("output/latest/model_operation_readiness_latest.csv")' in text
    for field in (
        "formal_model_use_allowed",
        "approved_for_daily",
        "presentation_allowed",
        "production_allowed",
    ):
        assert f'"{field}"' in text
    assert "len(rows) == 1" in text
    assert (
        '== "revenue_unreacted_range_source_mid_falling_v2_operation_v2"' in text
    )
    assert '== "pdf_integrated_daily_adapter"' in text
    for section in (
        "active_operation",
        "confirmed_operation",
        "confirmed_unranked_operation",
        "pending_confirmation",
    ):
        assert f'"{section}"' in text
    assert "len(observed_section_tokens) == len(expected_sections)" in text
    assert "observed_sections == expected_sections" in text
    assert "gh workflow run research_backtest_pipeline.yml" in text
    assert "--ref main" in text
    assert "-f run_revenue_unreacted_range_research=true" in text
    assert (
        "-f run_revenue_unreacted_range_forward_holdout_v2_only=true" in text
    )
    assert text.count("gh workflow run") == 1
    assert "git commit" not in text
    assert "git push" not in text
    assert "run_shared_model_research_data_refresh=true" not in text
    assert "apps_script" not in text.lower()
    assert "triggerdaily" not in text.lower()
