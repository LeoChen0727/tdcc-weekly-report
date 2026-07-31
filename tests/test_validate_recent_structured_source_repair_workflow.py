from __future__ import annotations

from scripts import validate_recent_structured_source_repair_workflow as validator


def _texts() -> tuple[str, str]:
    return (
        validator.RECENT_REPAIR_WORKFLOW.read_text(encoding="utf-8"),
        validator.HISTORICAL_REPLAY_WORKFLOW.read_text(encoding="utf-8"),
    )


def test_current_workflows_pass_data_only_catch_up_contract() -> None:
    recent_text, replay_text = _texts()

    assert validator.validate(recent_text, replay_text) == []
    assert recent_text.index("Commit repaired recent daily price gaps") < recent_text.index(
        "Checkout current main for structured catch-up planning"
    ) < recent_text.index("Plan bounded structured objective-source catch-up")


def test_direct_replay_or_model_work_is_rejected() -> None:
    recent_text, replay_text = _texts()
    replay_script = "replay_historical_structured" + "_sources.py"
    model_script = "build_daily_candidate_model" + "_layer.py"
    recent_text += (
        f"\nrun: python scripts/{replay_script}\n"
        f"run: python scripts/{model_script}\n"
    )

    errors = validator.validate(recent_text, replay_text)

    assert any("must not bypass" in error for error in errors)
    assert any("must remain data-only" in error for error in errors)


def test_missing_fresh_checkout_or_main_drift_gate_is_rejected() -> None:
    recent_text, replay_text = _texts()
    recent_text = recent_text.replace(
        "Checkout current main for structured catch-up planning",
        "Checkout stale source",
        1,
    ).replace(
        'if [ -z "$local_sha" ] || [ "$local_sha" != "$remote_main_sha" ]; then',
        'if [ -z "$local_sha" ] || [ "$local_sha" = "$remote_main_sha" ]; then',
        1,
    )

    errors = validator.validate(recent_text, replay_text)

    assert any("fresh-checkout" in error for error in errors)
    assert any("reject main drift" in error for error in errors)


def test_reusable_workflow_definition_and_post_plan_drift_gates_are_required() -> None:
    recent_text, replay_text = _texts()
    recent_text = recent_text.replace(
        '"$remote_replay_workflow_blob_sha" != "$CALLER_REPLAY_WORKFLOW_BLOB_SHA"',
        '"$remote_replay_workflow_blob_sha" = "$CALLER_REPLAY_WORKFLOW_BLOB_SHA"',
        1,
    ).replace(
        '"$remote_main_sha_after_plan" != "$local_sha"',
        '"$remote_main_sha_after_plan" = "$local_sha"',
        1,
    )

    errors = validator.validate(recent_text, replay_text)

    assert any("reusable workflow definition drift" in error for error in errors)
    assert any("no-op plan" in error for error in errors)


def test_reusable_replay_rejects_inherited_or_extra_secrets() -> None:
    recent_text, replay_text = _texts()
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
        errors = validator.validate(invalid, replay_text)
        assert any("must pass exactly the named" in error for error in errors)


def test_raw_repair_requires_immutable_base_push_mode() -> None:
    recent_text, replay_text = _texts()
    recent_text = recent_text.replace(
        'export CI_PUSH_EXPECTED_REMOTE_SHA="$REPAIR_BASE_SHA"',
        'export CI_PUSH_EXPECTED_REMOTE_SHA=""',
        1,
    )

    errors = validator.validate(recent_text, replay_text)

    assert any("immutable-base mode" in error for error in errors)


def test_structured_replay_limit_is_independent_from_raw_repair_limit() -> None:
    recent_text, replay_text = _texts()
    recent_text = recent_text.replace(
        "MAX_REPLAY_DATES: ${{ inputs.max_structured_replay_dates }}",
        "MAX_REPLAY_DATES: ${{ inputs.max_repair_dates }}",
        1,
    )

    errors = validator.validate(recent_text, replay_text)

    assert any("narrower raw repair limit" in error for error in errors)


def test_reusable_replay_entrypoint_and_secret_are_required() -> None:
    recent_text, replay_text = _texts()
    replay_text = replay_text.replace("workflow_call:", "disabled_workflow_call:", 1).replace(
        "PRODUCTION_ARTIFACT_WRITE_DEPLOY_KEY:",
        "MISSING_PRODUCTION_WRITER_SECRET:",
        1,
    )

    errors = validator.validate(recent_text, replay_text)

    assert any("reusable workflow entrypoint" in error for error in errors)
    assert any("production writer secret" in error for error in errors)
