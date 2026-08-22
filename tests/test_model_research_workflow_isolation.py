from __future__ import annotations

from dataclasses import replace

import pytest

from scripts import validate_model_research_workflow_isolation as validator


def _inputs() -> tuple[str, list[validator.WorkflowEntrypoint], dict[str, str]]:
    text = validator.WORKFLOW.read_text(encoding="utf-8")
    return text, validator.load_registry(), validator.load_model_owned_producers()


def _replace_last(text: str, old: str, new: str) -> str:
    head, separator, tail = text.rpartition(old)
    assert separator
    return head + new + tail


def test_model_research_workflow_isolation_validator_passes() -> None:
    assert validator.main() == 0


def test_consumed_revenue_migration_controls_remain_retired() -> None:
    text, rows, producers = _inputs()
    defaults = validator.workflow_input_defaults(text)

    assert set(validator.RETIRED_REVENUE_WORKFLOW_INPUTS).isdisjoint(defaults)
    assert validator.RETIRED_REVENUE_CONFIRMATION_TOKEN not in text
    assert validator.validate_workflow_text(text, rows, producers) == []


@pytest.mark.parametrize("retired_input", validator.RETIRED_REVENUE_WORKFLOW_INPUTS)
def test_research_workflow_rejects_reintroduced_consumed_input(
    retired_input: str,
) -> None:
    text, rows, producers = _inputs()
    mutated = text.replace(
        "    inputs:\n",
        "    inputs:\n"
        f"      {retired_input}:\n"
        "        description: \"Retired one-time migration control\"\n"
        "        required: false\n"
        "        default: \"false\"\n",
        1,
    )

    errors = validator.validate_workflow_text(mutated, rows, producers)

    assert any("must remain retired" in error for error in errors)


def test_research_workflow_rejects_reintroduced_consumed_confirmation_token() -> None:
    text, rows, producers = _inputs()
    mutated = text.replace(
        "          set -euo pipefail\n",
        "          set -euo pipefail\n"
        f"          echo {validator.RETIRED_REVENUE_CONFIRMATION_TOKEN}\n",
        1,
    )

    errors = validator.validate_workflow_text(mutated, rows, producers)

    assert any("confirmation token must remain retired" in error for error in errors)


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
    mutated = _replace_last(text, validator.PUBLISH_FAIL_CLOSED_SHELL, "set +e")

    errors = validator.validate_workflow_text(mutated, rows, producers)

    assert any("missing fail-closed shell mode" in error for error in errors)
    assert any("must not mask shell failure" in error for error in errors)


def test_research_publish_block_rejects_continue_on_error() -> None:
    text, rows, producers = _inputs()
    mutated = _replace_last(
        text,
        "        run: |\n          set -euo pipefail\n",
        "        continue-on-error: true\n        run: |\n          set -euo pipefail\n",
    )

    errors = validator.validate_workflow_text(mutated, rows, producers)

    assert any("must not mask shell failure" in error for error in errors)


@pytest.mark.parametrize("fallback", ("GITHUB_TOKEN", "github.token"))
def test_research_publish_block_rejects_github_token_fallback(fallback: str) -> None:
    text, rows, producers = _inputs()
    mutated = text.replace(
        validator.PUBLISH_COMMIT,
        f'echo "${{{fallback}}}"\n          ' + validator.PUBLISH_COMMIT,
        1,
    )

    errors = validator.validate_workflow_text(mutated, rows, producers)

    assert any("must not use a GITHUB_TOKEN fallback" in error for error in errors)


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


def test_ordinary_revenue_workflow_rejects_promotion_preparation_call() -> None:
    text, rows, producers = _inputs()
    full_build = f"            {validator.REVENUE_FULL_BUILD_COMMAND}\n"
    assert full_build in text
    mutated = text.replace(
        full_build,
        full_build
        + "            "
        + validator.FORBIDDEN_REVENUE_PROMOTION_PREPARATION_COMMAND
        + " --require-source-artifacts\n",
        1,
    )

    errors = validator.validate_workflow_text(mutated, rows, producers)

    assert any("must not invoke revenue promotion preparation" in error for error in errors)


def test_model_data_independence_audit_refresh_is_durable_and_exactly_staged() -> None:
    text, rows, producers = _inputs()
    lines = [line.strip() for line in text.splitlines()]

    assert lines.count(validator.MODEL_DATA_AUDIT_BUILD_COMMAND) == 1
    assert lines.count(validator.MODEL_DATA_AUDIT_VALIDATE_COMMAND) == 1
    assert lines.index(validator.MODEL_DATA_AUDIT_BUILD_COMMAND) < lines.index(
        validator.MODEL_DATA_AUDIT_VALIDATE_COMMAND
    )
    assert all(command in lines for command in validator.MODEL_DATA_AUDIT_STAGE_COMMANDS)
    assert validator.validate_workflow_text(text, rows, producers) == []


@pytest.mark.parametrize(
    "command",
    (
        validator.MODEL_DATA_AUDIT_BUILD_COMMAND,
        validator.MODEL_DATA_AUDIT_VALIDATE_COMMAND,
    ),
)
def test_model_data_independence_audit_rejects_missing_or_duplicate_command(
    command: str,
) -> None:
    text, rows, producers = _inputs()
    command_line = f"          {command}\n"
    assert command_line in text

    for mutated in (
        text.replace(command_line, "", 1),
        text.replace(command_line, command_line + command_line, 1),
    ):
        errors = validator.validate_workflow_text(mutated, rows, producers)
        assert any("must appear exactly once" in error for error in errors)


def test_model_data_independence_audit_rejects_validate_before_build() -> None:
    text, rows, producers = _inputs()
    ordered = (
        f"          {validator.MODEL_DATA_AUDIT_BUILD_COMMAND}\n"
        f"          {validator.MODEL_DATA_AUDIT_VALIDATE_COMMAND}\n"
    )
    reversed_order = (
        f"          {validator.MODEL_DATA_AUDIT_VALIDATE_COMMAND}\n"
        f"          {validator.MODEL_DATA_AUDIT_BUILD_COMMAND}\n"
    )
    assert ordered in text

    errors = validator.validate_workflow_text(
        text.replace(ordered, reversed_order, 1), rows, producers
    )

    assert any("must build before" in error for error in errors)


def test_model_data_independence_audit_rejects_non_model_post_run_condition() -> None:
    text, rows, producers = _inputs()
    assert validator.MODEL_DATA_AUDIT_POST_RUN_CONDITION in text
    mutated = text.replace(
        validator.MODEL_DATA_AUDIT_POST_RUN_CONDITION,
        "if: ${{ env.ANY_RESEARCH_SELECTED == 'true' }}",
        1,
    )

    errors = validator.validate_workflow_text(mutated, rows, producers)

    assert any("must require MODEL_RESEARCH_SELECTED" in error for error in errors)


@pytest.mark.parametrize(
    "rogue_command",
    (
        "git add -- docs/latest/rogue_model_audit.md",
        "echo bypass-exact4-stage",
    ),
)
def test_model_data_independence_audit_rejects_non_exact_stage_body(
    rogue_command: str,
) -> None:
    text, rows, producers = _inputs()
    exact = f"            {validator.MODEL_DATA_AUDIT_STAGE_COMMANDS[-1]}\n"
    assert exact in text
    mutated = text.replace(
        exact,
        exact + f"            {rogue_command}\n",
        1,
    )

    errors = validator.validate_workflow_text(mutated, rows, producers)

    assert any("must equal the exact four" in error for error in errors)


@pytest.mark.parametrize(
    "outside_command",
    (
        "git add -- docs/latest/model_data_independence_audit_rogue.md",
        validator.MODEL_DATA_AUDIT_STAGE_COMMANDS[0],
    ),
)
def test_model_data_independence_audit_rejects_stage_outside_model_guard(
    outside_command: str,
) -> None:
    text, rows, producers = _inputs()
    anchor = "          git status --short\n"
    assert anchor in text
    mutated = text.replace(
        anchor,
        f"          {outside_command}\n" + anchor,
        1,
    )

    errors = validator.validate_workflow_text(mutated, rows, producers)

    assert any("exactly the four guarded" in error for error in errors)


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
        '          if [[ "$REVENUE_FORWARD_HOLDOUT_ONLY" == "true" && '
        '"$REVENUE_RESEARCH_ENABLED" != "true" ]]; then\n'
    )
    exclusive_guard = (
        '          if [[ "$REVENUE_FORWARD_HOLDOUT_ONLY" == "true" && '
        '"$REVENUE_SOURCE_PROJECTION_CHAIN_ONLY" == "true" ]]; then\n'
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


@pytest.mark.parametrize("filter_key", ("paths", "paths-ignore"))
def test_pr_validation_requires_unfiltered_pull_request_scope(
    filter_key: str,
) -> None:
    rows = validator.load_registry()
    text = validator.PR_VALIDATION_WORKFLOW.read_text(encoding="utf-8")
    assert validator.validate_pr_workflow_text(text, rows) == []
    mutated = text.replace(
        "  pull_request:\n",
        f"  pull_request:\n    {filter_key}:\n      - scripts/**\n",
        1,
    )

    errors = validator.validate_pr_workflow_text(mutated, rows)

    assert any("must remain unfiltered" in error for error in errors)


def test_pr_validation_requires_cheap_scope_detector() -> None:
    rows = validator.load_registry()
    text = validator.PR_VALIDATION_WORKFLOW.read_text(encoding="utf-8").replace(
        "python scripts/detect_daily_model_pr_validation_scope.py",
        "echo scope-detector-disabled",
        1,
    )

    errors = validator.validate_pr_workflow_text(text, rows)

    assert any("missing scope contract" in error for error in errors)


def test_pr_validation_rejects_unrouted_registered_model_namespace() -> None:
    rows = validator.load_registry()
    rows.append(
        replace(
            rows[0],
            model_id="foo_bar",
            producer="scripts/foo_bar_research.py",
        )
    )
    text = validator.PR_VALIDATION_WORKFLOW.read_text(encoding="utf-8")

    errors = validator.validate_pr_workflow_text(text, rows)

    assert any("scripts/foo_bar_research.py" in error for error in errors)
