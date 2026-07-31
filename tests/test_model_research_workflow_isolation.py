from __future__ import annotations

from scripts import validate_model_research_workflow_isolation as validator


def _inputs() -> tuple[str, list[validator.WorkflowEntrypoint], dict[str, str]]:
    text = validator.WORKFLOW.read_text(encoding="utf-8")
    return text, validator.load_registry(), validator.load_model_owned_producers()


def test_model_research_workflow_isolation_validator_passes() -> None:
    assert validator.main() == 0


def test_revenue_step_rejects_another_model_producer() -> None:
    text, rows, producers = _inputs()
    text = text.replace(
        "          python scripts/build_revenue_unreacted_range_research.py",
        "          python scripts/build_revenue_unreacted_range_research.py\n"
        "          python scripts/build_price_pullback_23ema_research.py",
        1,
    )

    errors = validator.validate_workflow_text(text, rows, producers)

    assert any("mixes producers" in error for error in errors)


def test_revenue_cross_market_lineage_preflight_runs_before_expensive_build() -> None:
    text, _rows, _producers = _inputs()
    preflight = (
        "          python scripts/"
        "validate_revenue_unreacted_range_monthly_revenue_cross_market_resolution.py"
    )
    build = "          python scripts/build_revenue_unreacted_range_research.py"

    assert preflight in text
    assert text.index(preflight) < text.index(build)


def test_revenue_projection_chain_stage_is_not_a_second_producer_entrypoint() -> None:
    text, rows, producers = _inputs()
    stage_input = validator.REVENUE_PROJECTION_CHAIN_STAGE_INPUT

    assert validator.workflow_input_defaults(text)[stage_input] == "false"
    assert stage_input not in {row.workflow_input for row in rows}
    assert validator.REVENUE_PROJECTION_CHAIN_BUILD_COMMAND in text
    assert validator.validate_workflow_text(text, rows, producers) == []


def test_revenue_projection_chain_stage_rejects_unregistered_command() -> None:
    text, rows, producers = _inputs()
    stage_command = (
        f"            {validator.REVENUE_PROJECTION_CHAIN_BUILD_COMMAND}\n"
    )
    text = text.replace(
        stage_command,
        stage_command
        + "            python scripts/unregistered_projection_chain_command.py\n",
        1,
    )

    errors = validator.validate_workflow_text(text, rows, producers)

    assert any("stage mode must contain only" in error for error in errors)


def test_revenue_projection_chain_stage_rejects_independent_selection() -> None:
    text, rows, producers = _inputs()
    marker = "      MODEL_RESEARCH_SELECTED: ${{ "
    text = text.replace(
        marker,
        marker
        + "github.event.inputs."
        + validator.REVENUE_PROJECTION_CHAIN_STAGE_INPUT
        + " == 'true' || ",
        1,
    )

    errors = validator.validate_workflow_text(text, rows, producers)

    assert any("instead of selecting research independently" in error for error in errors)


def test_research_workflow_rejects_broad_history_stage() -> None:
    text, rows, producers = _inputs()
    text = text.replace(
        "          git status --short",
        "          git add output/history/research/ || true\n          git status --short",
        1,
    )

    errors = validator.validate_workflow_text(text, rows, producers)

    assert any("forbidden broad/formal stage path" in error for error in errors)


def test_revenue_step_rejects_embedded_shared_data_refresh() -> None:
    text, rows, producers = _inputs()
    text = text.replace(
        "          python scripts/build_revenue_unreacted_range_research.py",
        "          python scripts/build_revenue_unreacted_range_research.py\n"
        "          python scripts/build_monthly_revenue_point_in_time_panel.py",
        1,
    )

    errors = validator.validate_workflow_text(text, rows, producers)

    assert any("contains shared data refresh" in error for error in errors)


def test_research_workflow_rejects_default_true_model_input() -> None:
    text, rows, producers = _inputs()
    text = text.replace(
        '      run_revenue_unreacted_range_research:\n'
        '        description: "Run model-owned revenue lag and strength research only"\n'
        "        required: false\n"
        '        default: "false"',
        '      run_revenue_unreacted_range_research:\n'
        '        description: "Run model-owned revenue lag and strength research only"\n'
        "        required: false\n"
        '        default: "true"',
        1,
    )

    errors = validator.validate_workflow_text(text, rows, producers)

    assert any("must default false" in error for error in errors)


def test_research_workflow_rejects_missing_post_run_full_background_validation() -> None:
    text, rows, producers = _inputs()
    marker = "      - name: Validate post-run model research contracts"
    marker_index = text.index(marker)
    command = "          python scripts/validate_daily_model_background_data_registry.py\n"
    command_index = text.index(command, marker_index)
    text = text[:command_index] + text[command_index + len(command) :]

    errors = validator.validate_workflow_text(text, rows, producers)

    assert any("full background artifact validation" in error for error in errors)


def test_research_workflow_rejects_wrong_post_run_full_validation_condition() -> None:
    text, rows, producers = _inputs()
    marker = "      - name: Validate post-run model research contracts"
    marker_index = text.index(marker)
    condition = "        if: ${{ env.MODEL_RESEARCH_SELECTED == 'true' }}"
    condition_index = text.index(condition, marker_index)
    text = (
        text[:condition_index]
        + "        if: ${{ env.MODEL_RESEARCH_SELECTED != 'true' }}"
        + text[condition_index + len(condition) :]
    )

    errors = validator.validate_workflow_text(text, rows, producers)

    assert any("post-run full background artifact validation" in error for error in errors)


def test_research_workflow_rejects_post_validation_rebase_retry() -> None:
    text, rows, producers = _inputs()
    text = text.replace(
        'git push origin "HEAD:$TARGET_BRANCH"',
        'bash scripts/ci_push_with_retry.sh "$TARGET_BRANCH" 5',
    )

    errors = validator.validate_workflow_text(text, rows, producers)

    assert any("post-validation rebase retry is forbidden" in error for error in errors)


def test_research_workflow_rejects_swallowed_commit_failure() -> None:
    text, rows, producers = _inputs()
    text = text.replace(
        'git commit -m "Update research backtest outputs"',
        'git commit -m "Update research backtest outputs" || echo "No changes to commit"',
    )

    errors = validator.validate_workflow_text(text, rows, producers)

    assert any("must not swallow commit failures" in error for error in errors)


def test_pr_validation_requires_each_registered_model_namespace() -> None:
    rows = validator.load_registry()
    text = validator.PR_VALIDATION_WORKFLOW.read_text(encoding="utf-8").replace(
        '      - "scripts/revenue_unreacted_range_*.py"\n',
        "",
        1,
    )

    errors = validator.validate_pr_workflow_text(text, rows)

    assert any("scripts/revenue_unreacted_range_*.py" in error for error in errors)
