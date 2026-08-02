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


def test_pr_validation_requires_each_registered_model_namespace() -> None:
    rows = validator.load_registry()
    text = validator.PR_VALIDATION_WORKFLOW.read_text(encoding="utf-8").replace(
        '      - "scripts/revenue_unreacted_range_*.py"\n',
        "",
        1,
    )

    errors = validator.validate_pr_workflow_text(text, rows)

    assert any("scripts/revenue_unreacted_range_*.py" in error for error in errors)
