from __future__ import annotations

from scripts import validate_recent_structured_source_repair_workflow as validator


def _texts() -> tuple[str, str, str]:
    return (
        validator.RECENT_REPAIR_WORKFLOW.read_text(encoding="utf-8"),
        validator.HISTORICAL_REPLAY_WORKFLOW.read_text(encoding="utf-8"),
        validator.DAILY_FULL_WORKFLOW.read_text(encoding="utf-8"),
    )


def test_current_workflows_pass_data_only_catch_up_contract() -> None:
    recent_text, replay_text, daily_full_text = _texts()

    assert validator.validate(recent_text, replay_text, daily_full_text) == []
    assert recent_text.index("Commit repaired recent daily price gaps") < recent_text.index(
        "Checkout current main for structured catch-up planning"
    ) < recent_text.index("Plan bounded structured objective-source catch-up")


def test_direct_replay_or_model_work_is_rejected() -> None:
    recent_text, replay_text, daily_full_text = _texts()
    replay_script = "replay_historical_structured" + "_sources.py"
    model_script = "build_daily_candidate_model" + "_layer.py"
    recent_text += (
        f"\nrun: python scripts/{replay_script}\n"
        f"run: python scripts/{model_script}\n"
    )

    errors = validator.validate(recent_text, replay_text, daily_full_text)

    assert any("must not bypass" in error for error in errors)
    assert any("must remain data-only" in error for error in errors)


def test_missing_fresh_checkout_or_main_drift_gate_is_rejected() -> None:
    recent_text, replay_text, daily_full_text = _texts()
    recent_text = recent_text.replace(
        "Checkout current main for structured catch-up planning",
        "Checkout stale source",
        1,
    ).replace(
        'if [ -z "$local_sha" ] || [ "$local_sha" != "$remote_main_sha" ]; then',
        'if [ -z "$local_sha" ] || [ "$local_sha" = "$remote_main_sha" ]; then',
        1,
    )

    errors = validator.validate(recent_text, replay_text, daily_full_text)

    assert any("fresh-checkout" in error for error in errors)
    assert any("reject main drift" in error for error in errors)


def test_reusable_workflow_definition_and_post_plan_drift_gates_are_required() -> None:
    recent_text, replay_text, daily_full_text = _texts()
    recent_text = recent_text.replace(
        '"$remote_replay_workflow_blob_sha" != "$CALLER_REPLAY_WORKFLOW_BLOB_SHA"',
        '"$remote_replay_workflow_blob_sha" = "$CALLER_REPLAY_WORKFLOW_BLOB_SHA"',
        1,
    ).replace(
        '"$remote_main_sha_after_plan" != "$local_sha"',
        '"$remote_main_sha_after_plan" = "$local_sha"',
        1,
    )

    errors = validator.validate(recent_text, replay_text, daily_full_text)

    assert any("reusable workflow definition drift" in error for error in errors)
    assert any("no-op plan" in error for error in errors)


def test_reusable_replay_rejects_inherited_or_extra_secrets() -> None:
    recent_text, replay_text, daily_full_text = _texts()
    named_mapping = (
        "    secrets:\n"
        "      PRODUCTION_ARTIFACT_WRITE_DEPLOY_KEY: "
        "${{ secrets.PRODUCTION_ARTIFACT_WRITE_DEPLOY_KEY }}"
    )
    for replacement in (
        "    secrets: inherit",
        named_mapping + "\n      OTHER_SECRET: ${{ secrets.OTHER_SECRET }}",
    ):
        invalid = recent_text.replace(named_mapping, replacement, 1)
        errors = validator.validate(invalid, replay_text, daily_full_text)
        assert any("must pass exactly the named" in error for error in errors)


def test_raw_repair_requires_immutable_base_push_mode() -> None:
    recent_text, replay_text, daily_full_text = _texts()
    recent_text = recent_text.replace(
        'git push origin HEAD:main',
        'bash scripts/ci_push_with_retry.sh main 5',
        1,
    )

    errors = validator.validate(recent_text, replay_text, daily_full_text)

    assert any("rebase or retry" in error for error in errors)


def test_structured_replay_limit_is_independent_from_raw_repair_limit() -> None:
    recent_text, replay_text, daily_full_text = _texts()
    recent_text = recent_text.replace(
        "MAX_REPLAY_DATES: ${{ inputs.max_structured_replay_dates }}",
        "MAX_REPLAY_DATES: ${{ inputs.max_repair_dates }}",
        1,
    )

    errors = validator.validate(recent_text, replay_text, daily_full_text)

    assert any("narrower raw repair limit" in error for error in errors)


def test_reusable_replay_entrypoint_and_secret_are_required() -> None:
    recent_text, replay_text, daily_full_text = _texts()
    replay_text = replay_text.replace("workflow_call:", "disabled_workflow_call:", 1).replace(
        "PRODUCTION_ARTIFACT_WRITE_DEPLOY_KEY:",
        "MISSING_PRODUCTION_WRITER_SECRET:",
        1,
    )

    errors = validator.validate(recent_text, replay_text, daily_full_text)

    assert any("reusable workflow entrypoint" in error for error in errors)
    assert any("production writer secret" in error for error in errors)


def test_resume_identity_polling_and_current_day_contract_fail_closed() -> None:
    recent_text, replay_text, daily_full_text = _texts()
    invalid_recent = recent_text.replace(
        "for completion_poll in $(seq 1 240)",
        "while true",
        1,
    ).replace(
        "gh workflow run daily_full_pipeline.yml",
        "gh workflow run other.yml",
        1,
    )
    invalid_daily = daily_full_text.replace(
        "recovery source bundle inputs must be all-or-none",
        "recovery inputs optional",
        1,
    ).replace(
        "recovery dispatch requires github.run_attempt=1",
        "recovery rerun attempts are allowed",
        1,
    ).replace(
        "if: github.run_attempt == 1 && needs.market-session-preflight.outputs.should_run_daily_pipeline == 'true'",
        "if: needs.market-session-preflight.outputs.should_run_daily_pipeline == 'true'",
        1,
    )

    errors = validator.validate(invalid_recent, replay_text, invalid_daily)

    assert any("completion polling must be bounded" in error for error in errors)
    assert any("dispatch Daily Full exactly once" in error for error in errors)
    assert any("unapproved workflow dispatch" in error for error in errors)
    assert any("reject partial recovery identities" in error for error in errors)
    assert any("reject rerun attempts" in error for error in errors)
    assert any("independently reject rerun attempts" in error for error in errors)


def test_resume_requires_completed_authority_shortcut_and_durable_date_reservation() -> None:
    recent_text, replay_text, daily_full_text = _texts()
    invalid_recent = recent_text.replace("authority-status", "authority-check-disabled").replace(
        'correlation_id="daily-source-${SOURCE_TRADING_DATE}"',
        'correlation_id="daily-source-${GITHUB_RUN_ID}"',
        1,
    ).replace("reject_existing_recovery_run", "accept_existing_recovery_run")

    errors = validator.validate(invalid_recent, replay_text, daily_full_text)

    assert any("completed authority" in error for error in errors)
    assert any("per trading date" in error for error in errors)
    assert any("before POST" in error for error in errors)


def test_completed_authority_shortcut_requires_zero_raw_and_structured_changes() -> None:
    recent_text, replay_text, daily_full_text = _texts()
    invalid_recent = recent_text.replace(
        'if [ "$REPAIR_ACTION_COUNT" = 0 ] && [ "$STRUCTURED_REPLAY_REQUIRED" != true ]; then',
        "if true; then",
        1,
        ).replace(
            '--source-bundle-sha "$SOURCE_BUNDLE_SHA"',
            '--source-bundle-sha "$UNBOUND_BUNDLE_SHA"',
        )

    errors = validator.validate(invalid_recent, replay_text, daily_full_text)

    assert any("true zero-change" in error for error in errors)
    assert any("exact immutable bundle identity" in error for error in errors)


def test_daily_full_recovery_is_bound_to_event_sha_and_actual_production_job() -> None:
    recent_text, replay_text, daily_full_text = _texts()
    invalid_daily = daily_full_text.replace(
        "recovery event SHA mismatch",
        "recovery event SHA accepted",
        1,
    ).replace(
        "      - name: Materialize immutable recovery source bundle for production",
        "      - name: Disabled immutable recovery source bundle for production",
        1,
    )

    errors = validator.validate(recent_text, replay_text, invalid_daily)

    assert any("ref-resolution drift" in error for error in errors)
    assert any("production job must materialize" in error for error in errors)


def test_daily_full_recovery_requires_exact_durable_reservation_inputs() -> None:
    recent_text, replay_text, daily_full_text = _texts()
    invalid_recent = recent_text.replace(
        '-f recovery_reservation_sha256="$reservation_sha256"',
        '-f recovery_reservation_sha256=""',
        1,
    )
    invalid_daily = daily_full_text.replace(
        "python -B scripts/daily_source_recovery_bundle.py verify-reservation",
        "python -B scripts/daily_source_recovery_bundle.py skip-reservation",
        1,
    )

    errors = validator.validate(invalid_recent, replay_text, invalid_daily)

    assert any("durable reservation SHA" in error for error in errors)
    assert any("canonical reservation verifier" in error for error in errors)


def test_daily_full_materializes_before_identity_and_validators() -> None:
    recent_text, replay_text, daily_full_text = _texts()
    materialize = "      - name: Materialize immutable recovery source bundle for production"
    download = "      - name: Download market-session preflight evidence"
    invalid_daily = daily_full_text.replace(materialize, "__MATERIALIZE__", 1)
    invalid_daily = invalid_daily.replace(download, materialize, 1).replace(
        "__MATERIALIZE__", download, 1
    )

    errors = validator.validate(recent_text, replay_text, invalid_daily)

    assert any("before artifact identity" in error for error in errors)


def test_recovery_daily_full_uses_a_non_deadlocking_correlation_scoped_group() -> None:
    recent_text, replay_text, daily_full_text = _texts()
    invalid_daily = daily_full_text.replace(
        "group: ${{ inputs.recovery_correlation_id != '' && format('daily-full-recovery-{0}', inputs.recovery_correlation_id) || format('daily-full-pipeline-{0}', github.ref) }}",
        "group: daily-full-pipeline-${{ github.ref }}",
        1,
    )

    errors = validator.validate(recent_text, replay_text, invalid_daily)

    assert any("deadlocking" in error for error in errors)


def test_repair_holds_normal_production_lock_for_entire_recovery_chain() -> None:
    recent_text, replay_text, daily_full_text = _texts()
    invalid_recent = recent_text.replace(
        "  repair-recent-daily-price-gaps:\n    runs-on: ubuntu-latest",
        "  repair-recent-daily-price-gaps:\n    runs-on: ubuntu-latest\n"
        "    concurrency:\n      group: daily-full-pipeline-${{ github.ref }}",
        1,
    )

    errors = validator.validate(invalid_recent, replay_text, daily_full_text)

    assert any("entire workflow" in error for error in errors)


def test_resume_prerequisite_and_dispatch_uncertainty_persist_terminal_state() -> None:
    recent_text, replay_text, daily_full_text = _texts()
    invalid_recent = recent_text.replace("fail_recovery() {", "log_failure() {", 1).replace(
        'fail_recovery "Daily Full dispatch command failed or is uncertain"',
        'echo "dispatch failed"',
        1,
    )

    errors = validator.validate(invalid_recent, replay_text, daily_full_text)

    assert any("persist a terminal state" in error for error in errors)
    assert any("every dispatch/API/correlation uncertainty" in error for error in errors)


def test_mutable_fetch_cannot_run_for_recovery_bundle() -> None:
    recent_text, replay_text, daily_full_text = _texts()
    invalid_daily = daily_full_text.replace(
        "if: env.RECOVERY_SOURCE_BUNDLE_COMMIT_SHA == ''",
        "if: always()",
        1,
    )

    errors = validator.validate(recent_text, replay_text, invalid_daily)

    assert any("skip exactly the fetch" in error for error in errors)


def test_each_mutable_source_step_is_individually_recovery_gated() -> None:
    recent_text, replay_text, daily_full_text = _texts()
    invalid_daily = daily_full_text.replace(
        "      - name: Fetch latest official daily price\n"
        "        if: env.RECOVERY_SOURCE_BUNDLE_COMMIT_SHA == ''",
        "      - name: Fetch latest official daily price\n        if: always()",
        1,
    ).replace(
        "      - name: Install dependencies\n        run: |",
        "      - name: Install dependencies\n"
        "        if: env.RECOVERY_SOURCE_BUNDLE_COMMIT_SHA == ''\n        run: |",
        1,
    )

    errors = validator.validate(recent_text, replay_text, invalid_daily)

    assert any("Fetch latest official daily price" in error for error in errors)
