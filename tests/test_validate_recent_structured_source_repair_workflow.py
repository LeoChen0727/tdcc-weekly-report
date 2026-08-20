from __future__ import annotations

from scripts import repair_recent_daily_price_gaps as repair
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


def test_repair_contract_is_not_locked_to_unrelated_workflow_bytes() -> None:
    recent_text, replay_text, daily_full_text = _texts()

    assert validator.validate(
        recent_text + "\n# unrelated workflow comment\n",
        replay_text,
        daily_full_text,
    ) == []


def test_reusable_replay_concurrency_and_result_gate_are_minimal_and_fail_closed() -> None:
    recent_text, replay_text, daily_full_text = _texts()

    assert "caller_concurrency_identity" not in recent_text
    assert "caller_concurrency_identity" not in replay_text
    assert validator.validate(recent_text, replay_text, daily_full_text) == []

    self_colliding = replay_text.replace(
        "group: historical-structured-source-replay-${{ github.ref }}",
        "group: daily-full-pipeline-${{ github.ref }}",
        1,
    )
    errors = validator.validate(recent_text, self_colliding, daily_full_text)
    assert any("self-collide" in error for error in errors)

    permissive_required = recent_text.replace(
        'if [ "$STRUCTURED_REPLAY_RESULT" != success ]; then',
        'if [ "$STRUCTURED_REPLAY_RESULT" != failure ]; then',
        1,
    )
    errors = validator.validate(permissive_required, replay_text, daily_full_text)
    assert any("must succeed before resume" in error for error in errors)

    caller_ceremony = recent_text.replace(
        "      expected_main_sha:",
        "      caller_concurrency_identity: fixed\n      expected_main_sha:",
        1,
    )
    errors = validator.validate(caller_ceremony, replay_text, daily_full_text)
    assert any("identity ceremony" in error for error in errors)


def test_repair_trading_date_boundary_includes_current_day_by_default() -> None:
    assert repair.latest_trading_date_on_or_before("20260820", set()) == "20260820"
    assert (
        repair.latest_trading_date_on_or_before(
            "20260820",
            set(),
            include_as_of_date=False,
        )
        == "20260819"
    )


def test_repair_continuity_must_bind_target_date_and_precede_commit() -> None:
    recent_text, replay_text, daily_full_text = _texts()
    exact_continuity = (
        'python scripts/validate_daily_price_history_continuity.py '
        '--main-price-date "$REPAIR_TARGET_DATE"'
    )
    missing_date = recent_text.replace(
        exact_continuity,
        "python scripts/validate_daily_price_history_continuity.py",
        1,
    )
    errors = validator.validate(missing_date, replay_text, daily_full_text)
    assert any("bind the exact REPAIR_TARGET_DATE" in error for error in errors)

    moved_after_commit = recent_text.replace(exact_continuity, "echo deferred-continuity", 1).replace(
        'git commit -m "Persist ${REPAIR_TARGET_DATE} daily source recovery bundle"',
        'git commit -m "Persist ${REPAIR_TARGET_DATE} daily source recovery bundle"\n'
        f"            {exact_continuity}",
        1,
    )
    errors = validator.validate(moved_after_commit, replay_text, daily_full_text)
    assert any("before commit/push" in error for error in errors)


def test_repair_safety_validators_must_be_direct_shell_commands() -> None:
    recent_text, replay_text, daily_full_text = _texts()
    exact_continuity = (
        'python scripts/validate_daily_price_history_continuity.py '
        '--main-price-date "$REPAIR_TARGET_DATE"'
    )
    staged_validator = (
        "python scripts/validate_recent_daily_price_repair_staged_paths.py \\"
    )
    for carrier in (
        f"echo '{exact_continuity}'",
        f"printf '%s\\n' '{exact_continuity}'",
        f"cat <<'EOF'\n          {exact_continuity}\n          EOF",
        f'result="$({exact_continuity})"',
    ):
        invalid = recent_text.replace(exact_continuity, carrier, 1)
        errors = validator.validate(invalid, replay_text, daily_full_text)
        assert any("one direct command" in error for error in errors)

    for carrier in (
        f"echo {staged_validator}",
        f"printf '%s\\n' '{staged_validator}'",
        f"cat <<'EOF'\n              {staged_validator}\n              EOF",
        f'result="$({staged_validator})"',
    ):
        invalid = recent_text.replace(staged_validator, carrier, 1)
        errors = validator.validate(invalid, replay_text, daily_full_text)
        assert any("staged-path validator" in error for error in errors)


def test_repair_safety_gates_reject_dead_shell_control_flow() -> None:
    recent_text, replay_text, daily_full_text = _texts()
    continuity = (
        'python scripts/validate_daily_price_history_continuity.py '
        '--main-price-date "$REPAIR_TARGET_DATE"'
    )
    staged_validator = (
        "python scripts/validate_recent_daily_price_repair_staged_paths.py \\"
    )
    history_stage = "git add data/stock_price_history/"
    mutations = (
        recent_text.replace(
            continuity,
            f"if false; then\n          {continuity}\n          fi",
            1,
        ),
        recent_text.replace(
            staged_validator,
            f"if false; then\n          {staged_validator}",
            1,
        ).replace(
            '--source-bundle-sha "${{ steps.source_bundle.outputs.source_bundle_sha }}"',
            '--source-bundle-sha "${{ steps.source_bundle.outputs.source_bundle_sha }}"\n          fi',
            1,
        ),
        recent_text.replace(
            history_stage,
            f"if false; then\n          {history_stage}\n          fi",
            1,
        ),
        recent_text.replace(continuity, f"false && {continuity}", 1),
        recent_text.replace(
            history_stage,
            f"case never in always) {history_stage} ;; esac",
            1,
        ),
    )
    for invalid in mutations:
        errors = validator.validate(invalid, replay_text, daily_full_text)
        assert any(
            marker in error
            for error in errors
            for marker in (
                "one direct command",
                "staged-path validator",
                "exact unconditional staging step",
            )
        )


def test_repair_safety_steps_reject_skip_metadata_and_permissive_persist() -> None:
    recent_text, replay_text, daily_full_text = _texts()
    staged_step = "      - name: Validate exact staged current-day source recovery bundle\n"
    for metadata in (
        "        if: ${{ false }}\n",
        "        continue-on-error: true\n",
        "        shell: pwsh\n",
    ):
        invalid = recent_text.replace(staged_step, staged_step + metadata, 1)
        errors = validator.validate(invalid, replay_text, daily_full_text)
        assert any("staged-path validator" in error for error in errors)

    permissive_commit = recent_text.replace(
        'git commit -m "Persist ${REPAIR_TARGET_DATE} daily source recovery bundle"',
        'git commit -m "Persist ${REPAIR_TARGET_DATE} daily source recovery bundle" || true',
        1,
    )
    errors = validator.validate(permissive_commit, replay_text, daily_full_text)
    assert any("fail-closed commit/push step" in error for error in errors)


def test_repair_rejects_duplicate_or_interposed_critical_steps() -> None:
    recent_text, replay_text, daily_full_text = _texts()
    staged_step = validator._step_block(
        validator._job_block(recent_text, "repair-recent-daily-price-gaps"),
        "Validate exact staged current-day source recovery bundle",
    )
    duplicate = recent_text.replace(staged_step, staged_step + staged_step, 1)
    errors = validator.validate(duplicate, replay_text, daily_full_text)
    assert any("must exist exactly once" in error for error in errors)

    staged_marker = "      - name: Validate exact staged current-day source recovery bundle\n"
    malicious_step = (
        "      - name: Premature remote mutation\n"
        "        run: |\n"
        '          git commit -m "premature"\n'
        "          git push origin HEAD:main\n\n"
    )
    interposed = recent_text.replace(
        staged_marker, malicious_step + staged_marker, 1
    )
    errors = validator.validate(interposed, replay_text, daily_full_text)
    assert any("exact adjacent" in error for error in errors)
    assert any("globally unique" in error for error in errors)


def test_repair_rejects_unnamed_interposed_git_write_step() -> None:
    recent_text, replay_text, daily_full_text = _texts()
    staged_marker = "      - name: Validate exact staged current-day source recovery bundle\n"
    unnamed_write = (
        "      - run: |\n"
        '          git commit -m "premature unnamed"\n'
        "          git push origin HEAD:main\n\n"
    )
    invalid = recent_text.replace(
        staged_marker, unnamed_write + staged_marker, 1
    )
    errors = validator.validate(invalid, replay_text, daily_full_text)
    assert any("every step" in error for error in errors)
    assert any("exact adjacent" in error for error in errors)
    assert any("globally unique" in error for error in errors)


def test_repair_rejects_safety_metadata_after_run_block() -> None:
    recent_text, replay_text, daily_full_text = _texts()
    job_block = validator._job_block(recent_text, "repair-recent-daily-price-gaps")
    step_name = "Validate exact staged current-day source recovery bundle"
    staged_block = validator._step_block(job_block, step_name)
    assert staged_block
    for metadata in (
        "        if: ${{ false }}",
        "        continue-on-error: true",
        "        shell: pwsh",
    ):
        invalid_block = staged_block.rstrip() + f"\n{metadata}\n"
        invalid = recent_text.replace(staged_block, invalid_block, 1)
        errors = validator.validate(invalid, replay_text, daily_full_text)
        assert any("staged-path validator" in error for error in errors)


def test_repair_rejects_job_level_bypass_metadata() -> None:
    recent_text, replay_text, daily_full_text = _texts()
    job_marker = "  repair-recent-daily-price-gaps:\n"
    for metadata in (
        "    if: ${{ false }}\n",
        "    continue-on-error: true\n",
        '    "if": ${{ false }}\n',
        "    'continue-on-error': true\n",
    ):
        invalid = recent_text.replace(job_marker, job_marker + metadata, 1)
        errors = validator.validate(invalid, replay_text, daily_full_text)
        assert any(
            "job must be unconditional" in error
            or "canonical unquoted YAML" in error
            for error in errors
        )


def test_repair_rejects_git_write_in_any_other_job() -> None:
    recent_text, replay_text, daily_full_text = _texts()
    rogue_job = (
        "\n  rogue-write:\n"
        "    runs-on: ubuntu-latest\n"
        "    steps:\n"
        "      - name: Unauthorized repository write\n"
        "        run: |\n"
        '          git commit -m "cross-job write"\n'
        "          git push origin HEAD:main\n"
    )
    errors = validator.validate(
        recent_text + rogue_job, replay_text, daily_full_text
    )
    assert any("globally unique" in error for error in errors)


def test_repair_rejects_multiline_git_write_in_any_other_job() -> None:
    recent_text, replay_text, daily_full_text = _texts()
    rogue_job = (
        "\n  rogue-multiline-write:\n"
        "    runs-on: ubuntu-latest\n"
        "    steps:\n"
        "      - name: Unauthorized multiline repository write\n"
        "        run: |\n"
        "          git \\\n"
        '            commit -m "cross-job write"\n'
        "          git \\\n"
        "            push origin HEAD:main\n"
    )
    errors = validator.validate(
        recent_text + rogue_job, replay_text, daily_full_text
    )
    assert any("globally unique" in error for error in errors)


def test_required_history_staging_failure_cannot_be_swallowed() -> None:
    recent_text, replay_text, daily_full_text = _texts()
    safe_stage = "git add data/stock_price_history/"
    assert safe_stage in {line.strip() for line in recent_text.splitlines()}
    assert f"{safe_stage} || true" not in recent_text

    permissive = recent_text.replace(safe_stage, f"{safe_stage} || true", 1)
    errors = validator.validate(permissive, replay_text, daily_full_text)
    assert any("must not swallow" in error for error in errors)

    missing = recent_text.replace(safe_stage, "echo skip-history-stage", 1)
    errors = validator.validate(missing, replay_text, daily_full_text)
    assert any("fail closed while staging" in error for error in errors)


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
    assert daily_full_text.count("github.run_attempt == 1") == 1
    assert daily_full_text.count("recovery dispatch requires github.run_attempt=1") == 1
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
