from __future__ import annotations

from dataclasses import replace
import os
import re
import shutil
import subprocess

import pytest

from scripts import validate_model_research_workflow_isolation as validator


FOUR_MODEL_ENTRYPOINT_CONTRACT = {
    "hot_theme_pullback": (
        "run_hot_theme_pullback_research",
        "scripts/build_hot_theme_pullback_research.py",
        "scripts/validate_hot_theme_pullback_research.py",
    ),
    "pullback_short_reclaim": (
        "run_pullback_short_reclaim_research",
        "scripts/build_pullback_short_reclaim_research.py",
        "scripts/validate_pullback_short_reclaim_research.py",
    ),
    "tdcc_stealth_accumulation": (
        "run_tdcc_stealth_accumulation_research",
        "scripts/build_tdcc_stealth_accumulation_research.py",
        "scripts/validate_tdcc_stealth_accumulation_research.py",
    ),
    "tdcc_short_term_continuation_d5_d10": (
        "run_tdcc_short_term_continuation_d5_d10_research",
        "scripts/build_tdcc_short_term_continuation_d5_d10_research.py",
        "scripts/validate_tdcc_short_term_continuation_d5_d10_research.py",
    ),
}
FOUR_MODEL_STAGE_ALLOWLISTS = {
    "output/latest/research_backtest/hot_theme_pullback_*",
    "output/history/research/hot_theme_pullback_*",
    "docs/latest/hot_theme_pullback_*",
    "output/latest/research_backtest/pullback_short_reclaim_*",
    (
        "output/research/tdcc_stealth_accumulation/"
        "tdcc_stealth_accumulation_actual_recommendation_replay_*_v1.csv"
    ),
    "output/latest/research_backtest/tdcc_short_term_continuation_d5_d10_research_*",
}
TDCC_STEALTH_PIT_AUDIT_ENTRYPOINT = (
    "run_tdcc_stealth_accumulation_pit_replay_availability_audit",
    "scripts/audit_tdcc_stealth_accumulation_pit_replay_availability.py",
    "scripts/validate_tdcc_stealth_accumulation_pit_replay_availability.py",
    "output/research/tdcc_stealth_accumulation/"
    "tdcc_stealth_accumulation_pit_replay_availability_audit_v1.csv",
)
TDCC_STEALTH_HISTORICAL_REPLAY_ENTRYPOINT = (
    "run_tdcc_stealth_accumulation_historical_selector_replay",
    "scripts/build_tdcc_stealth_accumulation_historical_replay.py",
    "scripts/validate_tdcc_stealth_accumulation_historical_replay.py",
    "output/research/tdcc_stealth_accumulation/"
    "tdcc_stealth_accumulation_historical_selector_replay_*_v1.csv",
    "output/research/tdcc_stealth_accumulation/"
    "tdcc_stealth_accumulation_historical_selector_replay_report_v1.md",
)
TDCC_STEALTH_FIELD_CONTRACT_REPLAY_ENTRYPOINT = (
    "run_tdcc_stealth_accumulation_field_contract_replay",
    "scripts/build_tdcc_stealth_accumulation_field_contract_replay.py",
    "scripts/validate_tdcc_stealth_accumulation_field_contract_replay.py",
    "output/research/tdcc_stealth_accumulation/"
    "tdcc_stealth_accumulation_historical_selector_field_contract_replay_*_v2.csv",
    "output/research/tdcc_stealth_accumulation/"
    "tdcc_stealth_accumulation_historical_selector_field_contract_replay_report_v2.md",
)
TDCC_STEALTH_FIELD_CONTRACT_SOURCE_REF = (
    "7ef37a966280201a5ee236856306fdb513de7092"
)


def _inputs(
    workflow_path: str = validator.LEGACY_WORKFLOW_PATH,
) -> tuple[str, list[validator.WorkflowEntrypoint], dict[str, str]]:
    text = (validator.ROOT / workflow_path).read_text(encoding="utf-8")
    return text, validator.load_registry(), validator.load_model_owned_producers()


def _replace_last(text: str, old: str, new: str) -> str:
    head, separator, tail = text.rpartition(old)
    assert separator
    return head + new + tail


def test_model_research_workflow_isolation_validator_passes() -> None:
    assert validator.main() == 0


def test_four_model_entrypoints_are_independent_opt_in_workflow_contracts() -> None:
    text, rows, _producers = _inputs()
    rows_by_model = {row.model_id: row for row in rows}
    registered_stage_globs: set[str] = set()

    for model_id, (workflow_input, producer, validator_script) in (
        FOUR_MODEL_ENTRYPOINT_CONTRACT.items()
    ):
        row = rows_by_model[model_id]
        assert row.workflow_input == workflow_input
        assert row.producer == producer
        assert row.default_enabled is False
        assert row.formal_sync_allowed is False
        assert (
            validator.MODEL_PR_VALIDATION_DOMAINS[model_id]
            == validator.pr_scope.SHARED_MODEL_RESEARCH
        )

        stage_globs = {
            value
            for value in (
                row.latest_stage_glob,
                row.history_stage_glob,
                row.docs_stage_glob,
            )
            if value
        }
        assert stage_globs
        registered_stage_globs.update(stage_globs)

        producer_command = f"python {producer}"
        producer_blocks = [
            block
            for block in validator.workflow_step_blocks(text)
            if producer_command in block
        ]
        assert len(producer_blocks) == 1
        assert f"github.event.inputs.{workflow_input} == 'true'" in producer_blocks[0]
        assert f"python {validator_script}" in producer_blocks[0]

    assert registered_stage_globs == FOUR_MODEL_STAGE_ALLOWLISTS

    tdcc_selected_line = next(
        line for line in text.splitlines() if "TDCC_RESEARCH_SELECTED:" in line
    )
    assert (
        "github.event.inputs.run_tdcc_short_term_continuation_d5_d10_research "
        "== 'true'"
    ) in tdcc_selected_line
    assert "run_tdcc_stealth_accumulation_research" not in tdcc_selected_line


def test_model_entrypoint_allows_blank_optional_stage_slots() -> None:
    text, rows, producers = _inputs()
    row = next(row for row in rows if row.model_id == "pullback_short_reclaim")

    assert row.latest_stage_glob
    assert row.history_stage_glob == ""
    assert row.docs_stage_glob == ""
    assert validator.validate_workflow_text(text, rows, producers) == []


def test_tdcc_stealth_pit_availability_audit_has_independent_opt_in_entrypoint() -> None:
    text, rows, producers = _inputs()
    workflow_input, producer, validator_script, artifact = (
        TDCC_STEALTH_PIT_AUDIT_ENTRYPOINT
    )
    row = next(
        row
        for row in rows
        if row.model_id
        == "tdcc_stealth_accumulation_pit_replay_availability_audit"
    )

    assert row.workflow_input == workflow_input
    assert row.producer == producer
    assert row.latest_stage_glob == artifact
    assert row.history_stage_glob == ""
    assert row.docs_stage_glob == ""
    assert row.default_enabled is False
    assert row.formal_sync_allowed is False
    assert validator.MODEL_PR_VALIDATION_DOMAINS[row.model_id] == (
        validator.pr_scope.SHARED_MODEL_RESEARCH
    )

    producer_command = f"python {producer}"
    blocks = [
        block
        for block in validator.workflow_step_blocks(text)
        if producer_command in block
    ]
    assert len(blocks) == 1
    assert f"github.event.inputs.{workflow_input} == 'true'" in blocks[0]
    assert f"python {validator_script}" in blocks[0]
    assert (
        f'if [[ "${{{{ github.event.inputs.{workflow_input} }}}}" == "true" ]]; then\n'
        f"            git add {artifact} || true\n"
        "          fi"
    ) in text
    assert validator.validate_workflow_text(text, rows, producers) == []


def test_tdcc_stealth_historical_replay_has_independent_opt_in_entrypoint() -> None:
    text, rows, producers = _inputs()
    workflow_input, producer, validator_script, csv_glob, report_path = (
        TDCC_STEALTH_HISTORICAL_REPLAY_ENTRYPOINT
    )
    row = next(
        row for row in rows
        if row.model_id == "tdcc_stealth_accumulation_historical_selector_replay"
    )
    assert row.workflow_input == workflow_input
    assert row.producer == producer
    assert row.latest_stage_glob == csv_glob
    assert row.history_stage_glob == ""
    assert row.docs_stage_glob == report_path
    assert row.default_enabled is False
    assert row.formal_sync_allowed is False
    assert validator.MODEL_PR_VALIDATION_DOMAINS[row.model_id] == validator.pr_scope.SHARED_MODEL_RESEARCH
    block = next(block for block in validator.workflow_step_blocks(text) if f"python {producer}" in block)
    assert f"github.event.inputs.{workflow_input} == 'true'" in block
    assert f"python {validator_script}" in block
    assert f"git add {csv_glob} || true" in text
    assert f"git add {report_path} || true" in text
    assert validator.validate_workflow_text(text, rows, producers) == []


def test_tdcc_stealth_field_contract_replay_has_independent_opt_in_entrypoint() -> None:
    text, rows, producers = _inputs()
    workflow_input, producer, validator_script, csv_glob, report_path = (
        TDCC_STEALTH_FIELD_CONTRACT_REPLAY_ENTRYPOINT
    )
    row = next(
        row
        for row in rows
        if row.model_id == "tdcc_stealth_accumulation_field_contract_replay"
    )
    assert row.workflow_input == workflow_input
    assert row.producer == producer
    assert row.latest_stage_glob == csv_glob
    assert row.history_stage_glob == ""
    assert row.docs_stage_glob == report_path
    assert row.default_enabled is False
    assert row.formal_sync_allowed is False
    assert validator.MODEL_PR_VALIDATION_DOMAINS[row.model_id] == (
        validator.pr_scope.SHARED_MODEL_RESEARCH
    )
    block = next(
        block
        for block in validator.workflow_step_blocks(text)
        if f"python {producer}" in block
    )
    assert f"github.event.inputs.{workflow_input} == 'true'" in block
    fetch_command = (
        "git fetch --no-tags --depth=1 origin "
        f"{TDCC_STEALTH_FIELD_CONTRACT_SOURCE_REF}"
    )
    producer_command = (
        f"python {producer} --source-ref {TDCC_STEALTH_FIELD_CONTRACT_SOURCE_REF}"
    )
    validator_command = (
        f"python {validator_script} --source-ref "
        f"{TDCC_STEALTH_FIELD_CONTRACT_SOURCE_REF}"
    )
    assert fetch_command in block
    assert (
        producer_command in block
    )
    assert validator_command in block
    assert (
        block.index(fetch_command)
        < block.index(producer_command)
        < block.index(validator_command)
    )
    assert f"git add {csv_glob} || true" in text
    assert f"git add {report_path} || true" in text
    assert validator.validate_workflow_text(text, rows, producers) == []


def test_tdcc_stealth_field_contract_replay_rejects_missing_source_fetch() -> None:
    text, rows, producers = _inputs()
    mutated = text.replace(
        validator.TDCC_STEALTH_FIELD_CONTRACT_REPLAY_FETCH_COMMAND + "\n",
        "",
        1,
    )

    errors = validator.validate_workflow_text(mutated, rows, producers)

    assert any(
        "must fetch its immutable source exactly once" in error for error in errors
    )


def test_model_entrypoint_rejects_all_blank_stage_slots() -> None:
    text, rows, producers = _inputs()
    index = next(
        index
        for index, row in enumerate(rows)
        if row.model_id == "pullback_short_reclaim"
    )
    rows[index] = replace(rows[index], latest_stage_glob="")

    errors = validator.validate_workflow_text(text, rows, producers)

    assert any(
        "requires at least one non-empty stage allowlist" in error
        and "pullback_short_reclaim" in error
        for error in errors
    )


def test_four_model_stage_allowlist_rejects_wrong_input_guard() -> None:
    text, rows, producers = _inputs()
    mutated = text.replace(
        'if [[ "${{ github.event.inputs.run_pullback_short_reclaim_research }}" == "true" ]]; then\n'
        "            git add output/latest/research_backtest/pullback_short_reclaim_* || true",
        'if [[ "${{ github.event.inputs.run_hot_theme_pullback_research }}" == "true" ]]; then\n'
        "            git add output/latest/research_backtest/pullback_short_reclaim_* || true",
        1,
    )

    errors = validator.validate_workflow_text(mutated, rows, producers)

    assert any(
        "stage allowlist must be exact" in error
        and "pullback_short_reclaim" in error
        for error in errors
    )


@pytest.mark.parametrize(
    "model_id",
    tuple(FOUR_MODEL_ENTRYPOINT_CONTRACT),
)
def test_research_workflow_rejects_missing_model_owned_validator(
    model_id: str,
) -> None:
    text, rows, producers = _inputs()
    validator_script = FOUR_MODEL_ENTRYPOINT_CONTRACT[model_id][2]
    mutated = text.replace(
        f"          python {validator_script}\n",
        f"          echo skipped-{model_id}-validator\n",
        1,
    )

    errors = validator.validate_workflow_text(mutated, rows, producers)

    assert any(
        "model-owned validator must appear exactly once" in error
        and validator_script in error
        for error in errors
    )


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
        "              git add -- output/latest/research_backtest/"
        "revenue_unreacted_range_forward_holdout_manifest_latest.csv\n"
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
    text = _mutate_input(text, validator.REVENUE_WORKFLOW_INPUT, "default", "true")

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


def test_price_pit_audit_uses_exact_bounded_optin_sources() -> None:
    text, rows, producers = _inputs(validator.PRICE_PIT_WORKFLOW_PATH)
    assert validator.validate_workflow_text(text, rows, producers, workflow_path=validator.PRICE_PIT_WORKFLOW_PATH) == []
    selected = [r for r in rows if r.model_id == validator.TDCC_STEALTH_PRICE_PIT_AUDIT_MODEL_ID]
    assert len(selected) == 1
    assert selected[0].workflow_input == "run_tdcc_stealth_accumulation_price_pit_audit"
    assert len(validator.TDCC_STEALTH_PRICE_PIT_AUDIT_SOURCE_REFS) == 17
    assert text.count(validator.TDCC_STEALTH_PRICE_PIT_AUDIT_FETCH_COMMAND) == 1


@pytest.mark.parametrize("replacement", ("", "git fetch --no-tags --depth=1 origin main"))
def test_price_pit_audit_rejects_missing_or_nonexact_source_fetch(replacement) -> None:
    text, rows, producers = _inputs(validator.PRICE_PIT_WORKFLOW_PATH)
    text = text.replace(validator.TDCC_STEALTH_PRICE_PIT_AUDIT_FETCH_COMMAND, replacement, 1)
    errors = validator.validate_workflow_text(text, rows, producers, workflow_path=validator.PRICE_PIT_WORKFLOW_PATH)
    assert any("price/PIT audit must fetch its exact immutable sources" in e for e in errors)


def test_price_pit_audit_rejects_source_fetch_after_validator() -> None:
    text, rows, producers = _inputs(validator.PRICE_PIT_WORKFLOW_PATH)
    command = validator.TDCC_STEALTH_PRICE_PIT_AUDIT_FETCH_COMMAND
    text = text.replace("          " + command + "\n", "", 1)
    validation = "          python scripts/validate_tdcc_stealth_accumulation_price_pit.py"
    text = text.replace(validation, validation + "\n          " + command, 1)
    errors = validator.validate_workflow_text(text, rows, producers, workflow_path=validator.PRICE_PIT_WORKFLOW_PATH)
    assert any("price/PIT audit must fetch before" in e for e in errors)


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


@pytest.mark.parametrize(
    "bad_domains",
    (
        frozenset({validator.pr_scope.REVENUE_RESEARCH}),
        frozenset(
            {
                validator.pr_scope.RESEARCH_SAFETY_LITE,
                validator.pr_scope.REVENUE_RESEARCH,
                validator.pr_scope.REPO_CURRENT_CONTRACTS,
            }
        ),
        frozenset(
            {
                validator.pr_scope.RESEARCH_SAFETY_LITE,
                validator.pr_scope.REVENUE_RESEARCH,
                validator.pr_scope.SHARED_MODEL_RESEARCH,
            }
        ),
    ),
)
def test_pr_validation_requires_exact_revenue_safety_and_model_domain(
    bad_domains: frozenset[str],
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    rows = validator.load_registry()
    text = validator.PR_VALIDATION_WORKFLOW.read_text(encoding="utf-8")
    original = validator.pr_scope.domains_for_path

    def domains_for_path(path: str) -> frozenset[str]:
        if "revenue_unreacted_range" in path:
            return bad_domains
        return original(path)

    monkeypatch.setattr(validator.pr_scope, "domains_for_path", domains_for_path)

    errors = validator.validate_pr_workflow_text(text, rows)

    assert any(
        "must route to exactly research safety and its model domain" in error
        and "revenue_unreacted_range" in error
        for error in errors
    )


def _mutate_input(text: str, name: str, field: str, value: str | None) -> str:
    start = text.index(f"      {name}:\n")
    end_match = re.search(r"(?m)^(?:      [A-Za-z0-9_]+:|permissions:)", text[start + 1:])
    assert end_match is not None
    end = start + 1 + end_match.start()
    block = text[start:end]
    replacement = "" if value is None else f"        {field}: {value}\n"
    changed, count = re.subn(rf"(?m)^        {field}:.*\n", replacement, block, count=1)
    assert count == 1
    return text[:start] + changed + text[end:]


def _workflow_texts() -> dict[str, str]:
    return {
        path: (validator.ROOT / path).read_text(encoding="utf-8")
        for path in validator.WORKFLOW_WRITER_JOBS
    }


def _errors(text: str, workflow_path: str) -> list[str]:
    return validator.validate_workflow_text(
        text, validator.load_registry(), validator.load_model_owned_producers(),
        workflow_path=workflow_path,
    )


def test_two_workflows_cover_aggregate_ownership_and_preserve_old_25_inputs() -> None:
    texts = _workflow_texts()
    rows = validator.load_registry()
    assert validator.validate_workflow_texts(
        texts, rows, validator.load_model_owned_producers()
    ) == []
    assert len(validator.workflow_input_defaults(texts[validator.LEGACY_WORKFLOW_PATH])) == 25
    legacy_inputs = validator._dispatch_inputs(texts[validator.LEGACY_WORKFLOW_PATH])
    legacy_string_inputs = set(legacy_inputs) - validator.LEGACY_BOOLEAN_INPUTS
    assert len(legacy_string_inputs) == 16
    assert all(
        (validator._scalar(legacy_inputs[name], "type") or "string") == "string"
        for name in legacy_string_inputs
    )
    assert set(validator.workflow_input_defaults(texts[validator.PRICE_PIT_WORKFLOW_PATH])) == {
        validator.PRICE_PIT_INPUT
    }
    assert len([row for row in rows if row.workflow_path == validator.PRICE_PIT_WORKFLOW_PATH]) == 1


def test_aggregate_registry_cannot_move_price_back_or_drop_an_owned_model() -> None:
    rows = validator.load_registry()
    owned = validator.load_model_owned_producers()
    price_index = next(i for i, row in enumerate(rows) if row.workflow_input == validator.PRICE_PIT_INPUT)
    moved = list(rows)
    moved[price_index] = replace(moved[price_index], workflow_path=validator.LEGACY_WORKFLOW_PATH)
    assert any("wrong workflow" in error for error in validator.validate_registry_contract(moved, owned))
    assert any("cover every model_owned_write" in error for error in validator.validate_registry_contract(rows[:-1], owned))


def test_aggregate_validator_rejects_missing_workflow() -> None:
    texts = _workflow_texts()
    del texts[validator.PRICE_PIT_WORKFLOW_PATH]
    assert any("missing research workflow" in error for error in validator.validate_workflow_texts(
        texts, validator.load_registry(), validator.load_model_owned_producers()
    ))


@pytest.mark.parametrize("workflow_path", tuple(validator.WORKFLOW_WRITER_JOBS))
def test_dispatch_rejects_missing_boolean_type_default_or_true(workflow_path: str) -> None:
    text, rows, _ = _inputs(workflow_path)
    assert _errors(text, workflow_path) == []
    row = next(
        row for row in rows
        if row.workflow_path == workflow_path
        and (
            workflow_path == validator.PRICE_PIT_WORKFLOW_PATH
            or row.workflow_input in validator.LEGACY_BOOLEAN_INPUTS
        )
    )
    for field, value in (
        ("type", None), ("type", "string"), ("default", None),
        ("default", "true"), ("required", "true"),
    ):
        assert _errors(_mutate_input(text, row.workflow_input, field, value), workflow_path)


def test_dispatch_limit_counts_all_inputs_including_unregistered_controls() -> None:
    text, _, _ = _inputs()
    extra = (
        "      unexpected_26th_input:\n"
        "        description: Extra\n"
        "        required: false\n"
        "        default: false\n"
        "        type: boolean\n"
    )
    errors = _errors(text.replace("permissions: {}", extra + "\npermissions: {}", 1), validator.LEGACY_WORKFLOW_PATH)
    assert any("25 input limit" in error for error in errors)


@pytest.mark.parametrize("workflow_path", tuple(validator.WORKFLOW_WRITER_JOBS))
def test_duplicate_mapping_keys_fail_closed(workflow_path: str) -> None:
    text, _, _ = _inputs(workflow_path)
    mutated = text.replace("        type: boolean\n", "        type: boolean\n        type: string\n", 1)
    assert any("duplicate workflow mapping key" in error for error in _errors(mutated, workflow_path))


@pytest.mark.parametrize("workflow_path", tuple(validator.WORKFLOW_WRITER_JOBS))
def test_writer_and_noop_gates_are_exact_complements(workflow_path: str) -> None:
    text, _, _ = _inputs(workflow_path)
    names = validator.workflow_input_defaults(text)
    selected = validator.workflow_selection_condition(names)
    negated = validator.workflow_selection_condition(names, negate=True)
    assert f"    if: {selected}" in text
    assert f"    if: {negated}" in text
    for before, after in (
        (f"    if: {selected}", "    if: false"),
        (f"    if: {negated}", f"    if: {selected}"),
        (f"    if: {selected}", "    if: ${{ env.ANY_RESEARCH_SELECTED == 'true' }}"),
    ):
        assert _errors(text.replace(before, after, 1), workflow_path)


@pytest.mark.parametrize("stage_input", (
    validator.REVENUE_FORWARD_HOLDOUT_STAGE_INPUT,
    validator.REVENUE_FORWARD_HOLDOUT_V2_STAGE_INPUT,
    validator.REVENUE_PROJECTION_CHAIN_STAGE_INPUT,
))
def test_legacy_writer_gate_cannot_drop_dependent_only_revenue_inputs(stage_input: str) -> None:
    text, _, _ = _inputs()
    names = validator.workflow_input_defaults(text)
    expected = validator.workflow_selection_condition(names)
    reduced = validator.workflow_selection_condition(name for name in names if name != stage_input)
    mutated = text.replace(f"    if: {expected}", f"    if: {reduced}", 1)
    assert any("OR of every dispatch input" in error for error in _errors(mutated, validator.LEGACY_WORKFLOW_PATH))


@pytest.mark.parametrize("workflow_path", tuple(validator.WORKFLOW_WRITER_JOBS))
@pytest.mark.parametrize("mutation", (
    "checkout", "python", "secret", "extra_key", "extra_step", "write_permissions",
    "duplicate_if", "extra_run_line",
))
def test_noop_cannot_acquire_execution_or_credentials(workflow_path: str, mutation: str) -> None:
    text, _, _ = _inputs(workflow_path)
    if mutation == "checkout":
        mutated = text.replace("        shell: bash\n        run: printf", "        uses: actions/checkout@v6\n        shell: bash\n        run: printf", 1)
    elif mutation == "python":
        mutated = text.replace(validator.NO_OP_RUN, "python scripts/build_model_data_independence_audit.py", 1)
    elif mutation == "secret":
        mutated = text.replace("  no-op:\n", "  no-op:\n    env:\n      KEY: ${{ secrets.PRODUCTION_ARTIFACT_WRITE_DEPLOY_KEY }}\n", 1)
    elif mutation == "extra_key":
        mutated = text.replace("  no-op:\n", "  no-op:\n    environment: production\n", 1)
    elif mutation == "extra_step":
        mutated = text.replace("      - name: No research selected\n", "      - name: Extra\n        run: printf extra\n      - name: No research selected\n", 1)
    elif mutation == "write_permissions":
        mutated = text.replace("    permissions: {}", "    permissions:\n      contents: write", 1)
    elif mutation == "duplicate_if":
        mutated = text.replace("  no-op:\n", "  no-op:\n    if: true\n", 1)
    else:
        mutated = text.replace(validator.NO_OP_RUN, "|\n          " + validator.NO_OP_RUN + "\n          printf extra", 1)
    assert mutated != text
    assert _errors(mutated, workflow_path)


@pytest.mark.parametrize("workflow_path", tuple(validator.WORKFLOW_WRITER_JOBS))
def test_top_and_writer_permissions_cannot_be_widened_or_removed(workflow_path: str) -> None:
    text, _, _ = _inputs(workflow_path)
    for before, after in (
        ("permissions: {}", "permissions:\n  contents: write"),
        ("      contents: write", "      contents: read"),
    ):
        assert _errors(text.replace(before, after, 1), workflow_path)


@pytest.mark.parametrize("row", validator.load_registry(), ids=lambda row: row.model_id)
@pytest.mark.parametrize("mutation", ("missing", "duplicate", "disabled", "masked"))
def test_each_registered_producer_is_guarded_once_in_its_own_workflow(
    row: validator.WorkflowEntrypoint, mutation: str,
) -> None:
    text, _, _ = _inputs(row.workflow_path)
    command = f"python {row.producer}"
    if mutation == "missing":
        mutated = text.replace(command, "echo removed-producer")
    elif mutation == "duplicate":
        mutated = text.replace(command, command + "\n          " + command, 1)
    elif mutation == "masked":
        mutated = text.replace(command, command + " || true", 1)
    else:
        before = "        if: " + validator.workflow_selection_condition([row.workflow_input])
        assert before in text
        mutated = text.replace(before, "        if: false", 1)
    assert _errors(mutated, row.workflow_path)


def test_price_workflow_rejects_other_models_and_global_audit_writes() -> None:
    path = validator.PRICE_PIT_WORKFLOW_PATH
    text, _, _ = _inputs(path)
    marker = "          python scripts/audit_tdcc_stealth_accumulation_price_pit.py\n"
    for command in (
        "python scripts/build_hot_theme_pullback_research.py",
        validator.MODEL_DATA_AUDIT_BUILD_COMMAND,
        *validator.MODEL_DATA_AUDIT_STAGE_COMMANDS,
    ):
        mutated = text.replace(marker, marker + f"          {command}\n", 1)
        assert _errors(mutated, path)


@pytest.mark.parametrize("workflow_path", tuple(validator.WORKFLOW_WRITER_JOBS))
@pytest.mark.parametrize("command", validator.STATIC_VALIDATOR_COMMANDS + validator.READ_ONLY_POST_RUN_COMMANDS)
def test_required_validation_cannot_be_removed_or_masked(workflow_path: str, command: str) -> None:
    text, _, _ = _inputs(workflow_path)
    line = f"          {command}\n"
    assert line in text
    for replacement in ("", f"          {command} || true\n"):
        assert _errors(_replace_last(text, line, replacement), workflow_path)


@pytest.mark.parametrize("workflow_path", tuple(validator.WORKFLOW_WRITER_JOBS))
def test_static_and_postrun_steps_cannot_be_disabled(workflow_path: str) -> None:
    text, _, _ = _inputs(workflow_path)
    static_name = (
        "Validate model research prerequisites" if workflow_path == validator.PRICE_PIT_WORKFLOW_PATH
        else "Validate Apps Script workflow triggers"
    )
    marker = f"      - name: {static_name}\n"
    assert marker in text
    assert _errors(text.replace(marker, marker + "        if: false\n", 1), workflow_path)
    marker = "      - name: Validate post-run model research contracts\n"
    before = marker + "        if: ${{ env.MODEL_RESEARCH_SELECTED == 'true' }}"
    assert before in text
    assert _errors(text.replace(before, marker + "        if: false", 1), workflow_path)


@pytest.mark.parametrize("replacement", (
    "git add output/research/tdcc_stealth_accumulation/*",
    f"git add {validator.PRICE_PIT_STAGE_GLOB} || true",
    "git add output/latest/",
    "",
))
def test_price_stage_is_exact_model_only_and_fail_closed(replacement: str) -> None:
    path = validator.PRICE_PIT_WORKFLOW_PATH
    text, _, _ = _inputs(path)
    assert _errors(text.replace(f"git add {validator.PRICE_PIT_STAGE_GLOB}", replacement, 1), path)


def test_price_registry_cannot_expand_allowlist_even_if_workflow_matches() -> None:
    path = validator.PRICE_PIT_WORKFLOW_PATH
    text, rows, owned = _inputs(path)
    index = next(i for i, row in enumerate(rows) if row.workflow_path == path)
    broad = "output/research/tdcc_stealth_accumulation/*"
    rows[index] = replace(rows[index], latest_stage_glob=broad)
    text = text.replace(validator.PRICE_PIT_STAGE_GLOB, broad)
    assert any("exact input and model family allowlist" in error for error in
               validator.validate_workflow_text(text, rows, owned, workflow_path=path))


def test_price_background_full_validation_is_postrun_only() -> None:
    text, _, _ = _inputs(validator.PRICE_PIT_WORKFLOW_PATH)
    lines = [line.strip() for line in text.splitlines()]
    assert lines.count(validator.BACKGROUND_REGISTRY_FULL_COMMAND) == 1
    assert validator.MODEL_DATA_AUDIT_BUILD_COMMAND not in lines
    assert not any("model_data_independence_audit" in line for line in lines if line.startswith("git add"))
    assert _errors(text, validator.PRICE_PIT_WORKFLOW_PATH) == []


def _dispatch_condition_value(condition: str, inputs: dict[str, str]) -> bool:
    assert condition.startswith("${{ ") and condition.endswith(" }}")
    expression = condition[4:-3].strip()
    negated = expression.startswith("!(") and expression.endswith(")")
    if negated:
        expression = expression[2:-1]
    values = []
    for term in expression.split(" || "):
        match = re.fullmatch(r"github\.event\.inputs\.([A-Za-z0-9_]+) == 'true'", term)
        assert match is not None
        values.append(inputs[match.group(1)] == "true")
    selected = any(values)
    return not selected if negated else selected


@pytest.mark.parametrize("dependent_input,environment_name", (
    (None, None),
    (validator.REVENUE_PROJECTION_CHAIN_STAGE_INPUT, "REVENUE_SOURCE_PROJECTION_CHAIN_ONLY"),
    (validator.REVENUE_FORWARD_HOLDOUT_STAGE_INPUT, "REVENUE_FORWARD_HOLDOUT_ONLY"),
    (validator.REVENUE_FORWARD_HOLDOUT_V2_STAGE_INPUT, "REVENUE_FORWARD_HOLDOUT_V2_ONLY"),
))
def test_only_all_false_is_noop_and_dependent_only_inputs_exit_one(
    dependent_input: str | None, environment_name: str | None,
) -> None:
    text, _, _ = _inputs()
    assert _errors(text, validator.LEGACY_WORKFLOW_PATH) == []
    root = validator._workflow_fields(text, 0)
    jobs = validator._children(root["jobs"], 2)
    writer = validator._children(jobs["research-backtest-pipeline"], 4)
    noop = validator._children(jobs["no-op"], 4)
    inputs = dict.fromkeys(validator.workflow_input_defaults(text), "false")
    if dependent_input:
        inputs[dependent_input] = "true"
    assert _dispatch_condition_value(validator._scalar(writer, "if"), inputs) is bool(dependent_input)
    assert _dispatch_condition_value(validator._scalar(noop, "if"), inputs) is (dependent_input is None)

    static = next(
        step for step in validator._workflow_steps(writer["steps"])
        if validator._scalar(step, "name") == "Validate Apps Script workflow triggers"
    )
    lines = validator._run_lines(static)
    guards = lines[:lines.index(validator.STATIC_VALIDATOR_COMMANDS[0])]
    assert guards[0] == "set -euo pipefail"
    assert all(
        line in {"set -euo pipefail", "exit 1", "fi"}
        or line.startswith(('if [[ "$REVENUE_', 'echo "::error::Revenue '))
        for line in guards
    )
    git_bash = os.path.join(os.environ.get("ProgramFiles", r"C:\Program Files"), "Git", "bin", "bash.exe")
    bash = git_bash if os.name == "nt" and os.path.isfile(git_bash) else shutil.which("bash")
    assert bash, "A real Bash executable is required for revenue guard regression"
    env = os.environ.copy()
    for key in ("BASH_ENV", "ENV"):
        env.pop(key, None)
    env.update(dict.fromkeys((
        "REVENUE_SOURCE_PROJECTION_CHAIN_ONLY", "REVENUE_FORWARD_HOLDOUT_ONLY",
        "REVENUE_FORWARD_HOLDOUT_V2_ONLY", "REVENUE_RESEARCH_ENABLED",
    ), "false"))
    if environment_name:
        env[environment_name] = "true"
    result = subprocess.run(
        [bash, "--noprofile", "--norc", "-c", "\n".join(guards) + "\nprintf 'RESEARCH_GUARDS_PASSED\\n'\n"],
        env=env, capture_output=True, text=True, timeout=10, check=False,
    )
    assert result.returncode == (1 if dependent_input else 0), result.stdout + result.stderr
    if dependent_input:
        assert "::error::Revenue " in result.stdout
        assert "requires run_revenue_unreacted_range_research=true." in result.stdout
        assert "RESEARCH_GUARDS_PASSED" not in result.stdout
    else:
        assert result.stdout.strip() == "RESEARCH_GUARDS_PASSED"


@pytest.mark.parametrize("mutation", ("remove", "exit_zero"))
def test_projection_chain_primary_guard_cannot_be_removed_or_succeed(mutation: str) -> None:
    text, _, _ = _inputs()
    condition = (
        '          if [[ "$REVENUE_SOURCE_PROJECTION_CHAIN_ONLY" == "true" && '
        '"$REVENUE_RESEARCH_ENABLED" != "true" ]]; then\n'
    )
    start = text.index(condition)
    end = text.index("          fi\n", start) + len("          fi\n")
    guard = text[start:end]
    assert "exit 1" in guard
    replacement = "" if mutation == "remove" else guard.replace("exit 1", "exit 0", 1)
    errors = _errors(text[:start] + replacement + text[end:], validator.LEGACY_WORKFLOW_PATH)
    assert any("projection chain stage must fail closed" in error for error in errors)
