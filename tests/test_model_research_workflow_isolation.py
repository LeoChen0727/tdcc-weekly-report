from __future__ import annotations

from scripts import validate_model_research_workflow_isolation as validator


def _inputs() -> tuple[str, list[validator.WorkflowEntrypoint], dict[str, str]]:
    text = validator.WORKFLOW.read_text(encoding="utf-8")
    return text, validator.load_registry(), validator.load_model_owned_producers()


def test_model_research_workflow_isolation_validator_passes() -> None:
    assert validator.main() == 0


def test_research_publish_block_exits_zero_only_when_nothing_is_staged() -> None:
    text, rows, producers = _inputs()
    assert validator.PUBLISH_NO_CHANGE_GUARD in validator._normalized_shell_block(text)

    mutated = text.replace(
        "          if git diff --cached --quiet; then\n"
        '            echo "No changes to commit"\n'
        "            exit 0\n"
        "          fi\n",
        "",
        1,
    )
    errors = validator.validate_workflow_text(mutated, rows, producers)

    assert any("staged no-change exit guard" in error for error in errors)


def test_research_publish_block_rejects_swallowed_commit_failure() -> None:
    text, rows, producers = _inputs()
    mutated = text.replace(
        validator.PUBLISH_COMMIT,
        validator.PUBLISH_COMMIT + ' || echo "No changes to commit"',
        1,
    )

    errors = validator.validate_workflow_text(mutated, rows, producers)

    assert any("must not swallow" in error for error in errors)


def test_research_publish_block_rejects_disabled_fail_closed_shell() -> None:
    text, rows, producers = _inputs()
    mutated = text.replace(validator.PUBLISH_FAIL_CLOSED_SHELL, "set +e", 1)

    errors = validator.validate_workflow_text(mutated, rows, producers)

    assert any("missing fail-closed shell mode" in error for error in errors)
    assert any("must not mask shell failure" in error for error in errors)


def test_research_publish_block_rejects_continue_on_error() -> None:
    text, rows, producers = _inputs()
    mutated = text.replace(
        "        run: |\n          set -euo pipefail\n",
        "        continue-on-error: true\n        run: |\n          set -euo pipefail\n",
        1,
    )

    errors = validator.validate_workflow_text(mutated, rows, producers)

    assert any("must not mask shell failure" in error for error in errors)


def test_research_publish_block_rejects_retrying_rebase_push_helper() -> None:
    text, rows, producers = _inputs()
    mutated = text.replace(
        validator.PUBLISH_PUSH,
        'bash scripts/ci_push_with_retry.sh "$TARGET_BRANCH" 5',
        1,
    )

    errors = validator.validate_workflow_text(mutated, rows, producers)

    assert any("must not retry or rebase" in error for error in errors)
    assert any("exactly one direct research output push" in error for error in errors)


def test_research_publish_block_rejects_post_validation_branch_rewrite() -> None:
    text, rows, producers = _inputs()
    mutated = text.replace(
        validator.PUBLISH_COMMIT,
        'git pull --rebase origin "$TARGET_BRANCH"\n          ' + validator.PUBLISH_COMMIT,
        1,
    )

    errors = validator.validate_workflow_text(mutated, rows, producers)

    assert any("must not rewrite or resynchronize" in error for error in errors)


def test_research_workflow_rejects_separate_post_publish_rebase_step() -> None:
    text, rows, producers = _inputs()
    mutated = text + (
        "\n      - name: Retry publish after validation\n"
        "        run: |\n"
        '          git pull --rebase origin "$TARGET_BRANCH"\n'
    )

    errors = validator.validate_workflow_text(mutated, rows, producers)

    assert any("no post-validation branch rewrite" in error for error in errors)


def test_research_workflow_rejects_second_ff_only_sync_after_publish() -> None:
    text, rows, producers = _inputs()
    mutated = text + (
        "\n      - name: Advance target after validation\n"
        "        run: |\n"
        '          git pull --ff-only origin "$TARGET_BRANCH"\n'
    )

    errors = validator.validate_workflow_text(mutated, rows, producers)

    assert any("no post-validation branch rewrite" in error for error in errors)


def test_research_publish_block_rejects_muted_direct_push_failure() -> None:
    text, rows, producers = _inputs()
    mutated = text.replace(validator.PUBLISH_PUSH, validator.PUBLISH_PUSH + " || true", 1)

    errors = validator.validate_workflow_text(mutated, rows, producers)

    assert any("must be direct, non-force, and fail closed" in error for error in errors)


def test_research_workflow_rejects_duplicate_commit_push_block() -> None:
    text, rows, producers = _inputs()
    mutated = text + (
        "\n      - name: Duplicate publish block\n"
        "        run: |\n"
        f"          {validator.PUBLISH_COMMIT}\n"
        f"          {validator.PUBLISH_PUSH}\n"
    )

    errors = validator.validate_workflow_text(mutated, rows, producers)

    assert any("exactly one commit/push publish block" in error for error in errors)
    assert any("exactly one research output commit" in error for error in errors)
    assert any("exactly one direct research output push" in error for error in errors)


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
    projection_chain_validators = {
        "python scripts/validate_revenue_unreacted_range_lag_strength_matrix.py",
        "python scripts/validate_revenue_unreacted_range_launch_timing_feature_audit.py",
        "python scripts/validate_revenue_unreacted_range_forward_confirmation_feature_audit.py",
    }
    assert projection_chain_validators <= validator.REVENUE_PROJECTION_CHAIN_VALIDATOR_COMMANDS
    assert projection_chain_validators <= {line.strip() for line in text.splitlines()}
    assert validator.validate_workflow_text(text, rows, producers) == []


def test_revenue_forward_holdout_stage_is_nested_and_model_owned() -> None:
    text, rows, producers = _inputs()
    stage_input = validator.REVENUE_FORWARD_HOLDOUT_STAGE_INPUT

    assert validator.workflow_input_defaults(text)[stage_input] == "false"
    assert stage_input not in {row.workflow_input for row in rows}
    assert validator.REVENUE_FORWARD_HOLDOUT_BUILD_COMMAND in text
    for command in validator.REVENUE_FORWARD_HOLDOUT_STAGE_COMMANDS:
        assert command in text
    assert "python scripts/validate_revenue_unreacted_range_forward_holdout.py" not in text
    assert validator.validate_workflow_text(text, rows, producers) == []


def test_revenue_forward_holdout_stage_rejects_plain_boolean_true_default() -> None:
    text, rows, producers = _inputs()
    input_block = (
        "      run_revenue_unreacted_range_forward_holdout_only:\n"
        '        description: "Declare the model-owned revenue forward holdout input; disabled by default"\n'
        "        required: false\n"
        "        default: false\n"
        "        type: boolean"
    )
    assert input_block in text
    text = text.replace(input_block, input_block.replace("default: false", "default: true"), 1)

    errors = validator.validate_workflow_text(text, rows, producers)

    assert any("must default false" in error for error in errors)
    assert any("missing opt-in revenue stage input" in error for error in errors)


def test_revenue_forward_holdout_stage_rejects_unregistered_command() -> None:
    text, rows, producers = _inputs()
    stage_command = f"            {validator.REVENUE_FORWARD_HOLDOUT_BUILD_COMMAND}\n"
    text = text.replace(
        stage_command,
        stage_command + "            python scripts/unregistered_holdout_command.py\n",
        1,
    )

    errors = validator.validate_workflow_text(text, rows, producers)

    assert any("forward holdout stage mode must contain only" in error for error in errors)


def test_revenue_forward_holdout_commit_stage_rejects_broad_revenue_glob() -> None:
    text, rows, producers = _inputs()
    exact_command = (
        "              git add output/latest/research_backtest/"
        "revenue_unreacted_range_forward_holdout_* || true\n"
    )
    broad_command = (
        "              git add output/latest/research_backtest/"
        "revenue_unreacted_range_* || true\n"
    )
    assert exact_command in text
    text = text.replace(exact_command, broad_command, 1)

    errors = validator.validate_workflow_text(text, rows, producers)

    assert any(
        "forward holdout commit stage must contain only" in error
        for error in errors
    )


def test_revenue_forward_holdout_stage_rejects_independent_selection() -> None:
    text, rows, producers = _inputs()
    marker = "      MODEL_RESEARCH_SELECTED: ${{ "
    text = text.replace(
        marker,
        marker
        + "github.event.inputs."
        + validator.REVENUE_FORWARD_HOLDOUT_STAGE_INPUT
        + " == 'true' || ",
        1,
    )

    errors = validator.validate_workflow_text(text, rows, producers)

    assert any("instead of selecting research independently" in error for error in errors)


def test_revenue_forward_holdout_stage_requires_primary_and_exclusive_mode_guards() -> None:
    text, rows, producers = _inputs()
    primary_guard = (
        '          if [[ "${{ github.event.inputs.'
        + validator.REVENUE_FORWARD_HOLDOUT_STAGE_INPUT
        + ' }}" == "true" && "${{ github.event.inputs.'
        + validator.REVENUE_WORKFLOW_INPUT
        + ' }}" != "true" ]]; then\n'
    )
    exclusive_guard = (
        '          if [[ "${{ github.event.inputs.'
        + validator.REVENUE_FORWARD_HOLDOUT_STAGE_INPUT
        + ' }}" == "true" && "${{ github.event.inputs.'
        + validator.REVENUE_PROJECTION_CHAIN_STAGE_INPUT
        + ' }}" == "true" ]]; then\n'
    )
    assert primary_guard in text
    assert exclusive_guard in text

    without_primary = text.replace(primary_guard, "", 1)
    primary_errors = validator.validate_workflow_text(without_primary, rows, producers)
    assert any("unless the primary revenue" in error for error in primary_errors)

    without_exclusive = text.replace(exclusive_guard, "", 1)
    exclusive_errors = validator.validate_workflow_text(
        without_exclusive, rows, producers
    )
    assert any("mutually exclusive" in error for error in exclusive_errors)


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


def test_pr_validation_requires_each_registered_model_namespace() -> None:
    rows = validator.load_registry()
    text = validator.PR_VALIDATION_WORKFLOW.read_text(encoding="utf-8").replace(
        '      - "scripts/revenue_unreacted_range_*.py"\n',
        "",
        1,
    )

    errors = validator.validate_pr_workflow_text(text, rows)

    assert any("scripts/revenue_unreacted_range_*.py" in error for error in errors)
