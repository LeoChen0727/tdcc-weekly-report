from __future__ import annotations

import json
import os
from pathlib import Path
import shutil
import subprocess

import pytest

from scripts import validate_recent_structured_source_repair_workflow as validator


def _texts() -> tuple[str, str, str]:
    return (
        validator.RECENT_REPAIR_WORKFLOW.read_text(encoding="utf-8"),
        validator.HISTORICAL_REPLAY_WORKFLOW.read_text(encoding="utf-8"),
        validator.DAILY_FULL_WORKFLOW.read_text(encoding="utf-8"),
    )


def test_current_workflows_pass_data_only_catch_up_contract() -> None:
    recent_text, replay_text, daily_full_text = _texts()

    assert (
        validator._canonical_text_sha256(recent_text)
        == validator.RECENT_REPAIR_WORKFLOW_CANONICAL_SHA256
    )
    assert validator.validate(recent_text, replay_text, daily_full_text) == []


def test_repair_rejects_any_unreviewed_workflow_byte_mutation() -> None:
    recent_text, replay_text, daily_full_text = _texts()
    mutations = (
        recent_text.replace(
            "jobs:\n",
            "defaults:\n  run:\n    shell: bash {0} || true\njobs:\n",
            1,
        ),
        recent_text.replace(
            "  repair-recent-daily-price-gaps:\n",
            "  repair-recent-daily-price-gaps:\n"
            "    defaults:\n"
            "      run:\n"
            "        shell: bash {0} || true\n",
            1,
        ),
        recent_text
        + "\n  rogue-variable-write:\n"
        "    runs-on: ubuntu-latest\n"
        "    steps:\n"
        "      - name: Unauthorized variable repository write\n"
        "        run: |\n"
        "          G=git\n"
        '          "$G" commit -m "cross-job write"\n'
        '          "$G" push origin HEAD:main\n',
        recent_text
        + "\n  rogue-ifs-write:\n"
        "    runs-on: ubuntu-latest\n"
        "    steps:\n"
        "      - name: Unauthorized IFS repository write\n"
        "        run: |\n"
        '          git${IFS}commit -m "cross-job write"\n'
        "          git${IFS}push origin HEAD:main\n",
    )
    for invalid in mutations:
        errors = validator.validate(invalid, replay_text, daily_full_text)
        assert any("canonical SHA-256 mismatch" in error for error in errors)
    assert recent_text.index("Commit repaired recent daily price gaps") < recent_text.index(
        "Checkout current main for structured catch-up planning"
    ) < recent_text.index("Plan bounded structured objective-source catch-up")
    assert "output/latest/official_price_fetch_latest.json" in recent_text
    assert "output/latest/official_price_fetch_latest.md" in recent_text
    assert "publish_current_day_repair_confirmation" in (
        (validator.ROOT / "scripts/repair_recent_daily_price_gaps.py").read_text(
            encoding="utf-8"
        )
    )
    exact_continuity = (
        'python scripts/validate_daily_price_history_continuity.py '
        '--main-price-date "$REPAIR_TARGET_DATE"'
    )
    assert exact_continuity in recent_text
    for identity_arg in (
        '--target-date "$REPAIR_TARGET_DATE"',
        '--source-base-sha "$REPAIR_BASE_SHA"',
        '--manifest-path "${{ steps.source_bundle.outputs.manifest_path }}"',
        '--manifest-sha256 "${{ steps.source_bundle.outputs.manifest_sha256 }}"',
        '--source-bundle-sha "${{ steps.source_bundle.outputs.source_bundle_sha }}"',
    ):
        assert identity_arg in recent_text
    assert recent_text.index("Summarize recent repair result") < recent_text.index(
        exact_continuity
    ) < recent_text.index("Build immutable current-day source recovery bundle") < recent_text.index(
        "python scripts/validate_recent_daily_price_repair_staged_paths.py"
    ) < recent_text.index('git commit -m "Persist ${REPAIR_TARGET_DATE} daily source recovery bundle"')


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
        assert any(
            "must pass exactly the named" in error
            or "structured workflow YAML contract invalid" in error
            for error in errors
        )


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

    assert any(
        "reusable workflow entrypoint" in error
        or "structured workflow YAML contract invalid" in error
        for error in errors
    )
    assert any("production writer secret" in error for error in errors)


def _production_bash() -> str | None:
    direct = shutil.which("bash")
    if direct is not None:
        return direct
    git = shutil.which("git")
    if git is None:
        return None
    git_root = Path(git).resolve().parent.parent
    for candidate in (git_root / "bin" / "bash.exe", git_root / "usr" / "bin" / "bash.exe"):
        if candidate.is_file():
            return str(candidate)
    return None


def test_complete_resume_shell_is_syntax_valid_without_command_line_truncation() -> None:
    bash = _production_bash()
    assert bash is not None, "bash is required to parse the production resume contract"
    recent_text, _, _ = _texts()
    root = validator._yaml_document_mapping(recent_text, "recent repair workflow")
    jobs = validator._yaml_unique_mapping(root.get("jobs"), "recent repair jobs")
    resume_job = validator._yaml_unique_mapping(
        jobs.get("resume-daily-full-from-source-bundle"), "resume job"
    )
    steps = dict(validator._yaml_named_steps(resume_job, "resume job"))
    resume_run = validator._yaml_scalar(
        steps["Verify bundle and dispatch exactly one Daily Full resume"].get("run"),
        "resume run",
    )

    completed = subprocess.run(
        [bash, "-n"],
        input=resume_run,
        cwd=validator.ROOT,
        text=True,
        capture_output=True,
        check=False,
    )

    assert completed.returncode == 0, completed.stderr


PRODUCTION_COMMAND_STUBS = r'''git() {
  case "$1 $2" in
    "fetch origin") [ "${FAIL_GIT_FETCH-}" != 1 ] ;;
    "rev-parse origin/main")
      [ "${FAIL_ORIGIN_REV_PARSE-}" != 1 ] || return 35
      printf '%s\n' aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
      ;;
    "rev-parse HEAD")
      [ "${FAIL_HEAD_REV_PARSE-}" != 1 ] || return 36
      printf '%s\n' aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
      ;;
    "merge-base --is-ancestor")
      [ "${FAIL_MERGE_BASE_COMMAND-}" != 1 ] || return 128
      [ "${FAIL_MERGE_BASE_NON_ANCESTOR-}" != 1 ] || return 1
      return 0
      ;;
    *) printf 'unexpected git invocation: %s\n' "$*" >&2; return 97 ;;
  esac
}
python() {
  python_args=("$@")
  mode=""
  state_output=""
  output=""
  transition_to=""
  error=""
  last=""
  while [ "$#" -gt 0 ]; do
    last="$1"
    case "$1" in
      verify|transition|authority-status) mode="$1" ;;
      --state-output) shift; state_output="$1" ;;
      --output) shift; output="$1" ;;
      --to) shift; transition_to="$1" ;;
      --error) shift; error="$1" ;;
    esac
    shift
  done
  case "$mode" in
    "")
      if [ "${FAILURE_SCHEMA-}" = daily_source_recovery_terminal_failure.v1 ]; then
        [ "${FAIL_TERMINAL_FALLBACK_WRITE-}" != 1 ] || return 37
      fi
      if [ -n "${FAILURE_SCHEMA-}" ]; then
        printf '{"schema_version":"%s","status":"failed","phase":"%s","error":"%s","persistence_error":"%s"}\n' "$FAILURE_SCHEMA" "$FAILURE_PHASE" "$FAILURE_ERROR" "$FAILURE_PERSISTENCE_ERROR" > "$last"
      else
        command python "${python_args[@]}"
      fi
      ;;
    verify)
      [ "${FAIL_VERIFY-}" != 1 ] || return 32
      printf '%s\n' '{"status":"verified"}' > "$state_output"
      ;;
    transition)
      if [ "$transition_to" = bundle_committed ] && [ "${FAIL_BUNDLE_TRANSITION-}" = 1 ]; then
        return 33
      fi
      if [ "$transition_to" = failed ]; then
        [ "${FAIL_FAILED_TRANSITION-}" != 1 ] || return 38
        printf '{"status":"failed","error":"%s"}\n' "$error" > "$output"
      elif [ "$transition_to" = resume_not_required ] && [ "${FAIL_RESUME_NOT_REQUIRED_TRANSITION-}" = 1 ]; then
        return 40
      else
        printf '{"status":"%s"}\n' "$transition_to" > "$output"
      fi
      ;;
    authority-status)
      [ "${FAIL_AUTHORITY_STATUS-}" != 1 ] || return 41
      if [ "${FAIL_AUTHORITY_JSON_MALFORMED-}" = 1 ]; then
        printf '%s\n' '{malformed' > "$output"
      elif [ "${FAIL_AUTHORITY_DECISION_INVALID-}" = 1 ]; then
        printf '%s\n' '{"resume_required":"false","existing_authority":{}}' > "$output"
      else
        printf '%s\n' '{"resume_required":false,"existing_authority":{"release_id":"release","generation_id":"generation","commit_sha":"aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"}}' > "$output"
      fi
      ;;
    *) printf 'unexpected python invocation\n' >&2; return 98 ;;
  esac
}
mv() {
  if [ "${FAIL_STATE_MOVE-}" = 1 ]; then
    return 34
  fi
  if [ "${FAIL_FAILED_STATE_MOVE-}" = 1 ] && [ -f "$1" ] && grep -q '"status":"failed"' "$1"; then
    return 39
  fi
  if [ "${FAIL_RESUME_NOT_REQUIRED_STATE_MOVE-}" = 1 ] && [ -f "$1" ] && grep -q '"status":"resume_not_required"' "$1"; then
    return 42
  fi
  command mv "$@"
}
'''


def test_reusable_replay_call_concurrency_cannot_self_collide_with_caller() -> None:
    recent_text, replay_text, daily_full_text = _texts()
    replacements = (
        "group: daily-full-pipeline-${{ github.ref }}\n  # "
        + validator.REUSABLE_REPLAY_CONCURRENCY_GROUP,
        validator.REUSABLE_REPLAY_CONCURRENCY_GROUP
        + "\n  group: daily-full-pipeline-${{ github.ref }}",
        validator.REUSABLE_REPLAY_CONCURRENCY_GROUP
        + '\n  "group": daily-full-pipeline-${{ github.ref }}',
        validator.REUSABLE_REPLAY_CONCURRENCY_GROUP
        + "\n  group : daily-full-pipeline-${{ github.ref }}",
        validator.REUSABLE_REPLAY_CONCURRENCY_GROUP
        + '\n"concurrency":\n  "group": daily-full-pipeline-${{ github.ref }}',
        validator.REUSABLE_REPLAY_CONCURRENCY_GROUP
        + '\n  "gr\\u006fup": daily-full-pipeline-${{ github.ref }}',
        validator.REUSABLE_REPLAY_CONCURRENCY_GROUP
        + '\n  "\\x67roup": daily-full-pipeline-${{ github.ref }}',
        validator.REUSABLE_REPLAY_CONCURRENCY_GROUP
        + "\n  ? group\n  : daily-full-pipeline-${{ github.ref }}",
        validator.REUSABLE_REPLAY_CONCURRENCY_GROUP
        + "\n  !!str group: daily-full-pipeline-${{ github.ref }}",
        validator.REUSABLE_REPLAY_CONCURRENCY_GROUP
        + '\nconcurrency: {group: "manual-bypass-${{ github.run_id }}", cancel-in-progress: false}',
        validator.REUSABLE_REPLAY_CONCURRENCY_GROUP
        + '\n"concu\\u0072rency": {group: "manual-bypass-${{ github.run_id }}"}',
        validator.REUSABLE_REPLAY_CONCURRENCY_GROUP
        + "\n!!str concurrency: {group: manual-bypass-${{ github.run_id }}}",
    )

    for replacement in replacements:
        invalid_replay = replay_text.replace(
            validator.REUSABLE_REPLAY_CONCURRENCY_GROUP,
            replacement,
            1,
        )
        errors = validator.validate(recent_text, invalid_replay, daily_full_text)
        assert any(
            "run-scoped group" in error
            or "structured workflow YAML contract invalid" in error
            for error in errors
        )


def test_reusable_concurrency_identity_is_required_from_caller_and_forbidden_on_dispatch() -> None:
    recent_text, replay_text, daily_full_text = _texts()
    invalid_recent = recent_text.replace(
        "      caller_concurrency_identity: ${{ format('{0}-{1}', github.run_id, github.run_attempt) }}\n",
        "",
        1,
    )
    dispatch_keys = (
        "caller_concurrency_identity:",
        '"caller_concurrency_identity":',
        "caller_concurrency_identity :",
    )

    caller_errors = validator.validate(invalid_recent, replay_text, daily_full_text)
    assert any("pass its exact run-id and attempt" in error for error in caller_errors)
    for dispatch_key in dispatch_keys:
        invalid_dispatch = replay_text.replace(
            "  workflow_dispatch:\n    inputs:\n",
            "  workflow_dispatch:\n    inputs:\n"
            f"      {dispatch_key}\n"
            "        required: false\n"
            "        default: ''\n"
            "        type: string\n",
            1,
        )
        dispatch_errors = validator.validate(
            recent_text, invalid_dispatch, daily_full_text
        )
        assert any("must not expose" in error for error in dispatch_errors)


def test_reusable_concurrency_identity_rejects_node_equivalent_dispatch_keys() -> None:
    recent_text, replay_text, daily_full_text = _texts()
    entries = (
        '      "caller_concurrency_\\u0069dentity":\n'
        "        required: false\n"
        "        type: string\n",
        "      ? caller_concurrency_identity\n"
        "      :\n"
        "        required: false\n"
        "        type: string\n",
        "      !!str caller_concurrency_identity:\n"
        "        required: false\n"
        "        type: string\n",
    )
    for entry in entries:
        invalid = replay_text.replace(
            "  workflow_dispatch:\n    inputs:\n",
            "  workflow_dispatch:\n    inputs:\n" + entry,
            1,
        )
        errors = validator.validate(recent_text, invalid, daily_full_text)
        assert any("must not expose" in error for error in errors)


def test_reusable_concurrency_identity_active_mapping_and_runtime_check_are_required() -> None:
    recent_text, replay_text, daily_full_text = _texts()
    expected_mapping = (
        "      caller_concurrency_identity: ${{ format('{0}-{1}', github.run_id, github.run_attempt) }}"
    )
    spoofed_recent = recent_text.replace(
        expected_mapping,
        "      caller_concurrency_identity: fixed-spoof\n      # "
        + expected_mapping.strip(),
        1,
    )
    disabled_runtime_check = replay_text.replace(
        "        if: inputs.caller_concurrency_identity != ''",
        "        if: false # inputs.caller_concurrency_identity != ''",
        1,
    )

    mapping_errors = validator.validate(
        spoofed_recent, replay_text, daily_full_text
    )
    runtime_errors = validator.validate(
        recent_text, disabled_runtime_check, daily_full_text
    )

    assert any("active with mapping" in error for error in mapping_errors)
    assert any("matches the actual GitHub run-id and attempt" in error for error in runtime_errors)


def test_reusable_caller_workflow_identity_is_bound_to_the_only_authorized_caller() -> None:
    recent_text, replay_text, daily_full_text = _texts()
    variants = (
        replay_text.replace(
            "CALLER_WORKFLOW_REF: ${{ github.workflow_ref }}",
            "CALLER_WORKFLOW_REF: fixed-spoof",
            1,
        ),
        replay_text.replace(
            "LeoChen0727/tdcc-weekly-report/.github/workflows/repair_recent_daily_price_gaps.yml@refs/heads/main",
            "LeoChen0727/tdcc-weekly-report/.github/workflows/rogue.yml@refs/heads/main",
            1,
        ),
    )

    for invalid in variants:
        errors = validator.validate(recent_text, invalid, daily_full_text)
        assert any("actual GitHub run-id and attempt" in error for error in errors)


def test_structured_workflow_parser_rejects_nested_duplicates_and_wrong_scalar_tags() -> None:
    recent_text, replay_text, daily_full_text = _texts()
    variants = (
        replay_text.replace(
            "        required: true\n        type: string",
            '        required: true\n        "required": false\n        type: string',
            1,
        ),
        replay_text.replace("        required: true", '        required: "true"', 1),
        replay_text.replace(
            "  cancel-in-progress: false",
            "  cancel-in-progress: !!str false",
            1,
        ),
    )

    for invalid in variants:
        errors = validator.validate(recent_text, invalid, daily_full_text)
        assert any(
            "structured workflow YAML contract invalid" in error
            or "typed contract" in error
            for error in errors
        )


def test_required_structured_replay_must_materialize_and_succeed() -> None:
    recent_text, replay_text, daily_full_text = _texts()
    invalid_required = recent_text.replace(
        'if [ "$STRUCTURED_REPLAY_RESULT" != success ]; then',
        'if [ "$STRUCTURED_REPLAY_RESULT" != failure ]; then',
        1,
    )
    invalid_noop = recent_text.replace(
        'if [ "$STRUCTURED_REPLAY_RESULT" != skipped ]; then',
        'if [ "$STRUCTURED_REPLAY_RESULT" = failure ]; then',
        1,
    )

    required_errors = validator.validate(
        invalid_required, replay_text, daily_full_text
    )
    noop_errors = validator.validate(invalid_noop, replay_text, daily_full_text)

    assert any("must materialize and succeed" in error for error in required_errors)
    assert any("no-op structured replay plan" in error for error in noop_errors)


def test_structured_replay_required_is_a_strict_true_false_closed_set() -> None:
    recent_text, replay_text, daily_full_text = _texts()
    missing_default = recent_text.replace(
        "            *)\n"
        '              printf \'%s\\n\' "Invalid structured objective-source replay requirement: ${STRUCTURED_REPLAY_REQUIRED-}" > "$gate_error_path"\n'
        "              ;;\n",
        "",
        1,
    )
    permissive_false = recent_text.replace(
        "            false)",
        "            false|*)",
        1,
    )

    missing_errors = validator.validate(
        missing_default, replay_text, daily_full_text
    )
    permissive_errors = validator.validate(
        permissive_false, replay_text, daily_full_text
    )

    assert any("missing, blank, or malformed values" in error for error in missing_errors)
    assert any("missing, blank, or malformed values" in error for error in permissive_errors)


def test_structured_replay_gate_failures_persist_terminal_state_artifact(
    tmp_path: Path,
) -> None:
    bash = _production_bash()
    assert bash is not None, "bash is required to execute the production gate contract"
    recent_text, _, _ = _texts()
    root = validator._yaml_document_mapping(recent_text, "recent repair workflow")
    jobs = validator._yaml_unique_mapping(root.get("jobs"), "recent repair jobs")
    resume_job = validator._yaml_unique_mapping(
        jobs.get("resume-daily-full-from-source-bundle"), "resume job"
    )
    steps = dict(validator._yaml_named_steps(resume_job, "resume job"))
    gate_run = validator._yaml_scalar(
        steps[validator.REPLAY_RESULT_GATE_STEP_NAME].get("run"), "gate run"
    )
    resume_run = validator._yaml_scalar(
        steps["Verify bundle and dispatch exactly one Daily Full resume"].get("run"),
        "resume run",
    )
    command_stubs = PRODUCTION_COMMAND_STUBS
    cases = (
        ("true", "failure", "Required structured objective-source replay"),
        ("false", "failure", "Unexpected structured objective-source replay result"),
        ("", "skipped", "Invalid structured objective-source replay requirement"),
    )
    for index, (required, result, expected_error) in enumerate(cases):
        runner_temp = tmp_path / str(index)
        runner_temp.mkdir()
        env = {
            **os.environ,
            "RUNNER_TEMP": str(runner_temp),
            "STRUCTURED_REPLAY_REQUIRED": required,
            "STRUCTURED_REPLAY_RESULT": result,
            "STRUCTURED_PLAN_RESULT": "success",
            "SOURCE_BUNDLE_COMMIT_SHA": "b" * 40,
            "SOURCE_BUNDLE_MANIFEST_PATH": "manifest.json",
            "SOURCE_BUNDLE_MANIFEST_SHA256": "c" * 64,
            "SOURCE_BUNDLE_SHA": "d" * 64,
            "SOURCE_TRADING_DATE": "20260814",
            "REPAIR_ACTION_COUNT": "1",
        }
        completed = subprocess.run(
            [bash, "-s"],
            input=command_stubs + gate_run + "\n" + resume_run,
            cwd=validator.ROOT,
            env=env,
            text=True,
            capture_output=True,
            check=False,
        )
        state_path = runner_temp / "daily-source-recovery-state.json"
        assert completed.returncode != 0
        assert state_path.is_file() and state_path.stat().st_size > 0
        state = json.loads(state_path.read_text(encoding="utf-8"))
        assert state["status"] == "failed"
        assert expected_error in state["error"]


def test_resume_prestate_failures_always_leave_truthful_uploadable_evidence(
    tmp_path: Path,
) -> None:
    bash = _production_bash()
    assert bash is not None, "bash is required to execute the production resume contract"
    recent_text, _, _ = _texts()
    root = validator._yaml_document_mapping(recent_text, "recent repair workflow")
    jobs = validator._yaml_unique_mapping(root.get("jobs"), "recent repair jobs")
    resume_job = validator._yaml_unique_mapping(
        jobs.get("resume-daily-full-from-source-bundle"), "resume job"
    )
    steps = dict(validator._yaml_named_steps(resume_job, "resume job"))
    resume_run = validator._yaml_scalar(
        steps["Verify bundle and dispatch exactly one Daily Full resume"].get("run"),
        "resume run",
    )
    command_stubs = PRODUCTION_COMMAND_STUBS
    cases = (
        ("FAIL_GIT_FETCH", "Unable to fetch current main"),
        ("FAIL_ORIGIN_REV_PARSE", "Unable to resolve current main"),
        ("FAIL_HEAD_REV_PARSE", "Unable to resolve resume checkout HEAD"),
        ("FAIL_MERGE_BASE_NON_ANCESTOR", "not an ancestor of current main"),
        ("FAIL_MERGE_BASE_COMMAND", "Unable to verify source bundle ancestry"),
        ("FAIL_VERIFY", "Immutable source recovery bundle verification failed"),
        ("FAIL_BUNDLE_TRANSITION", "Unable to persist bundle-committed"),
        ("FAIL_STATE_MOVE", "Unable to activate bundle-committed"),
    )
    for index, (failure_flag, expected_error) in enumerate(cases):
        runner_temp = tmp_path / str(index)
        runner_temp.mkdir()
        env = {
            **os.environ,
            "RUNNER_TEMP": str(runner_temp),
            "STRUCTURED_REPLAY_REQUIRED": "false",
            "STRUCTURED_REPLAY_RESULT": "skipped",
            "STRUCTURED_PLAN_RESULT": "success",
            "SOURCE_BUNDLE_COMMIT_SHA": "b" * 40,
            "SOURCE_BUNDLE_MANIFEST_PATH": "manifest.json",
            "SOURCE_BUNDLE_MANIFEST_SHA256": "c" * 64,
            "SOURCE_BUNDLE_SHA": "d" * 64,
            "SOURCE_TRADING_DATE": "20260814",
            "REPAIR_ACTION_COUNT": "1",
            "GITHUB_RUN_ID": "123",
            "GITHUB_RUN_ATTEMPT": "1",
            failure_flag: "1",
        }
        completed = subprocess.run(
            [bash, "-s"],
            input=command_stubs + "\n" + resume_run,
            cwd=validator.ROOT,
            env=env,
            text=True,
            capture_output=True,
            check=False,
        )
        state_path = runner_temp / "daily-source-recovery-state.json"
        assert completed.returncode != 0
        assert state_path.is_file() and state_path.stat().st_size > 0
        state = json.loads(state_path.read_text(encoding="utf-8"))
        assert state["schema_version"] == validator.PRE_STATE_FAILURE_SCHEMA
        assert state["status"] == "failed"
        assert state["phase"] == "resume_preflight"
        assert expected_error in state["error"]


@pytest.mark.parametrize(
    ("failure_flags", "expected_error"),
    [
        ({"FAIL_FAILED_TRANSITION": "1"}, "Required structured objective-source replay"),
        ({"FAIL_FAILED_STATE_MOVE": "1"}, "Required structured objective-source replay"),
        (
            {"FAIL_FAILED_TRANSITION": "1", "FAIL_TERMINAL_FALLBACK_WRITE": "1"},
            "Terminal source-recovery state writer failed",
        ),
    ],
)
def test_terminal_failure_persistence_never_leaves_bundle_committed_state(
    tmp_path: Path,
    failure_flags: dict[str, str],
    expected_error: str,
) -> None:
    bash = _production_bash()
    assert bash is not None, "bash is required to execute the production resume contract"
    recent_text, _, _ = _texts()
    root = validator._yaml_document_mapping(recent_text, "recent repair workflow")
    jobs = validator._yaml_unique_mapping(root.get("jobs"), "recent repair jobs")
    resume_job = validator._yaml_unique_mapping(
        jobs.get("resume-daily-full-from-source-bundle"), "resume job"
    )
    steps = dict(validator._yaml_named_steps(resume_job, "resume job"))
    gate_run = validator._yaml_scalar(
        steps[validator.REPLAY_RESULT_GATE_STEP_NAME].get("run"), "gate run"
    )
    resume_run = validator._yaml_scalar(
        steps["Verify bundle and dispatch exactly one Daily Full resume"].get("run"),
        "resume run",
    )
    runner_temp = tmp_path / "terminal"
    runner_temp.mkdir()
    env = {
        **os.environ,
        "RUNNER_TEMP": str(runner_temp),
        "STRUCTURED_REPLAY_REQUIRED": "true",
        "STRUCTURED_REPLAY_RESULT": "failure",
        "STRUCTURED_PLAN_RESULT": "success",
        "SOURCE_BUNDLE_COMMIT_SHA": "b" * 40,
        "SOURCE_BUNDLE_MANIFEST_PATH": "manifest.json",
        "SOURCE_BUNDLE_MANIFEST_SHA256": "c" * 64,
        "SOURCE_BUNDLE_SHA": "d" * 64,
        "SOURCE_TRADING_DATE": "20260814",
        "REPAIR_ACTION_COUNT": "1",
        "GITHUB_RUN_ID": "123",
        "GITHUB_RUN_ATTEMPT": "1",
        **failure_flags,
    }
    completed = subprocess.run(
        [bash, "-s"],
        input=PRODUCTION_COMMAND_STUBS + gate_run + "\n" + resume_run,
        cwd=validator.ROOT,
        env=env,
        text=True,
        capture_output=True,
        check=False,
    )

    state_path = runner_temp / "daily-source-recovery-state.json"
    assert completed.returncode != 0
    assert state_path.is_file() and state_path.stat().st_size > 0
    state = json.loads(state_path.read_text(encoding="utf-8"))
    assert state["schema_version"] == validator.TERMINAL_FAILURE_SCHEMA
    assert state["status"] == "failed"
    assert state["phase"] == "resume_terminal_failure"
    assert state["status"] != "bundle_committed"
    assert expected_error in state["error"]


@pytest.mark.parametrize(
    "failure_flag",
    (
        "FAIL_AUTHORITY_STATUS",
        "FAIL_AUTHORITY_JSON_MALFORMED",
        "FAIL_AUTHORITY_DECISION_INVALID",
        "FAIL_RESUME_NOT_REQUIRED_TRANSITION",
        "FAIL_RESUME_NOT_REQUIRED_STATE_MOVE",
    ),
)
def test_post_bundle_command_failures_are_finalized_as_truthful_terminal_evidence(
    tmp_path: Path,
    failure_flag: str,
) -> None:
    bash = _production_bash()
    assert bash is not None, "bash is required to execute the production resume contract"
    recent_text, _, _ = _texts()
    root = validator._yaml_document_mapping(recent_text, "recent repair workflow")
    jobs = validator._yaml_unique_mapping(root.get("jobs"), "recent repair jobs")
    resume_job = validator._yaml_unique_mapping(
        jobs.get("resume-daily-full-from-source-bundle"), "resume job"
    )
    steps = dict(validator._yaml_named_steps(resume_job, "resume job"))
    resume_run = validator._yaml_scalar(
        steps["Verify bundle and dispatch exactly one Daily Full resume"].get("run"),
        "resume run",
    )
    finalizer_run = validator._yaml_scalar(
        steps[validator.TERMINAL_FINALIZER_STEP_NAME].get("run"),
        "terminal finalizer run",
    )
    runner_temp = tmp_path / failure_flag.lower()
    runner_temp.mkdir()
    env = {
        **os.environ,
        "RUNNER_TEMP": str(runner_temp),
        "STRUCTURED_REPLAY_REQUIRED": "false",
        "STRUCTURED_REPLAY_RESULT": "skipped",
        "STRUCTURED_PLAN_RESULT": "success",
        "SOURCE_BUNDLE_COMMIT_SHA": "b" * 40,
        "SOURCE_BUNDLE_MANIFEST_PATH": "manifest.json",
        "SOURCE_BUNDLE_MANIFEST_SHA256": "c" * 64,
        "SOURCE_BUNDLE_SHA": "d" * 64,
        "SOURCE_TRADING_DATE": "20260814",
        "REPAIR_ACTION_COUNT": "0",
        "GITHUB_RUN_ID": "123",
        "GITHUB_RUN_ATTEMPT": "1",
        failure_flag: "1",
    }
    failed = subprocess.run(
        [bash, "-s"],
        input=PRODUCTION_COMMAND_STUBS + "\n" + resume_run,
        cwd=validator.ROOT,
        env=env,
        text=True,
        capture_output=True,
        check=False,
    )
    assert failed.returncode != 0

    finalized = subprocess.run(
        [bash, "-s"],
        input=finalizer_run,
        cwd=validator.ROOT,
        env={**env, "RESUME_JOB_STATUS": "failure"},
        text=True,
        capture_output=True,
        check=False,
    )
    assert finalized.returncode == 0, finalized.stderr
    state_path = runner_temp / "daily-source-recovery-state.json"
    state = json.loads(state_path.read_text(encoding="utf-8"))
    assert state["schema_version"] == validator.TERMINAL_FAILURE_SCHEMA
    assert state["status"] == "failed"
    assert state["phase"] == "resume_terminal_finalizer"
    assert state["status"] != "bundle_committed"


def test_terminal_finalizer_overwrites_stale_or_malformed_state_before_upload(
    tmp_path: Path,
) -> None:
    bash = _production_bash()
    assert bash is not None, "bash is required to execute the production terminal finalizer"
    recent_text, _, _ = _texts()
    root = validator._yaml_document_mapping(recent_text, "recent repair workflow")
    jobs = validator._yaml_unique_mapping(root.get("jobs"), "recent repair jobs")
    resume_job = validator._yaml_unique_mapping(
        jobs.get("resume-daily-full-from-source-bundle"), "resume job"
    )
    steps = dict(validator._yaml_named_steps(resume_job, "resume job"))
    finalizer_run = validator._yaml_scalar(
        steps[validator.TERMINAL_FINALIZER_STEP_NAME].get("run"),
        "terminal finalizer run",
    )
    upload_step = steps["Upload source recovery resume state"]
    assert validator._yaml_scalar(upload_step.get("if"), "upload if") == (
        "always() && steps.finalize_source_recovery_state.outcome == 'success'"
    )

    for index, initial in enumerate(
        ('{"status":"bundle_committed"}\n', "{malformed\n", "")
    ):
        runner_temp = tmp_path / str(index)
        runner_temp.mkdir()
        state_path = runner_temp / "daily-source-recovery-state.json"
        state_path.write_text(initial, encoding="utf-8")
        env = {
            **os.environ,
            "RUNNER_TEMP": str(runner_temp),
            "RESUME_JOB_STATUS": "failure",
            "SOURCE_BUNDLE_COMMIT_SHA": "b" * 40,
            "SOURCE_BUNDLE_MANIFEST_PATH": "manifest.json",
            "SOURCE_BUNDLE_MANIFEST_SHA256": "c" * 64,
            "SOURCE_BUNDLE_SHA": "d" * 64,
            "SOURCE_TRADING_DATE": "20260814",
            "GITHUB_RUN_ID": "123",
            "GITHUB_RUN_ATTEMPT": "1",
        }
        completed = subprocess.run(
            [bash, "-s"],
            input=finalizer_run,
            cwd=validator.ROOT,
            env=env,
            text=True,
            capture_output=True,
            check=False,
        )
        assert completed.returncode == 0, completed.stderr
        state = json.loads(state_path.read_text(encoding="utf-8"))
        assert state["status"] == "failed"
        assert state["phase"] == "resume_terminal_finalizer"
        assert state_path.stat().st_size > 0


def test_historical_replay_critical_steps_reject_bypass_metadata() -> None:
    recent_text, replay_text, daily_full_text = _texts()
    variants = []
    for index, step_name in enumerate(validator.HISTORICAL_REPLAY_CRITICAL_STEP_KEYS):
        marker = f"      - name: {step_name}\n"
        metadata = "        continue-on-error: true\n" if index % 2 == 0 else "        if: ${{ false }}\n"
        variants.append(replay_text.replace(marker, marker + metadata, 1))
        start = replay_text.index(marker)
        end = replay_text.find("\n      - name: ", start + len(marker))
        block = replay_text[start:] if end < 0 else replay_text[start:end]
        variants.append(
            replay_text.replace(block, block.replace("        shell: bash", "        shell: true {0}", 1), 1)
        )
        variants.append(
            replay_text.replace(
                block,
                block.replace("        run: |\n", "        run: |\n          if false; then\n          fi\n", 1),
                1,
            )
        )

    for invalid in variants:
        assert invalid != replay_text
        errors = validator.validate(recent_text, invalid, daily_full_text)
        assert any("critical step" in error for error in errors)


def test_historical_replay_runtime_job_rejects_job_level_bypass_metadata() -> None:
    recent_text, replay_text, daily_full_text = _texts()
    marker = "  replay-historical-structured-sources:\n"
    variants = (
        "    if: ${{ false }}\n",
        '    "if": ${{ true }}\n',
        "    continue-on-error: true\n",
        "    'continue-on-error': ${{ true }}\n",
    )

    for metadata in variants:
        invalid = replay_text.replace(marker, marker + metadata, 1)
        errors = validator.validate(recent_text, invalid, daily_full_text)
        assert any("runtime job must use the exact unconditional" in error for error in errors)


def test_terminal_finalizer_rejects_inert_run_wrapping() -> None:
    recent_text, replay_text, daily_full_text = _texts()
    marker = f"      - name: {validator.TERMINAL_FINALIZER_STEP_NAME}\n"
    start = recent_text.index(marker)
    end = recent_text.index("\n      - name: Upload source recovery resume state", start)
    block = recent_text[start:end]
    invalid = recent_text.replace(
        block,
        block.replace("        run: |\n", "        run: |\n          if false; then\n          fi\n", 1),
        1,
    )

    errors = validator.validate(invalid, replay_text, daily_full_text)

    assert any("terminal failure evidence" in error for error in errors)


def test_structured_replay_gate_cannot_drop_terminal_failure_persistence() -> None:
    recent_text, replay_text, daily_full_text = _texts()
    invalid = recent_text.replace(
        validator.REPLAY_GATE_FAILURE_PERSISTENCE_BLOCK.replace("\n", "\n          ").rstrip(),
        'gate_error_path="$RUNNER_TEMP/structured-replay-gate-error.txt"',
        1,
    )

    assert invalid != recent_text
    errors = validator.validate(invalid, replay_text, daily_full_text)
    assert any("terminal failure evidence" in error for error in errors)


def test_structured_replay_closed_set_gate_must_be_reachable_and_before_shortcuts() -> None:
    recent_text, replay_text, daily_full_text = _texts()
    start = recent_text.index("      - name: Validate structured replay completion contract")
    end = recent_text.index(
        "      - name: Verify bundle and dispatch exactly one Daily Full resume",
        start,
    )
    gate_step = recent_text[start:end]
    variants = (
        recent_text.replace(gate_step, gate_step.replace("          set -euo pipefail", "          if false; then"), 1),
        recent_text.replace(gate_step, gate_step.replace("          set -euo pipefail", "          builtin exit 0"), 1),
        recent_text.replace(gate_step, gate_step.replace("          set -euo pipefail", "          command false"), 1),
        recent_text.replace(gate_step, gate_step.replace("          set -euo pipefail", "          : <<123"), 1),
        recent_text[:start] + recent_text[end:],
        recent_text[:start] + recent_text[end:] + gate_step,
    )

    for invalid in variants:
        errors = validator.validate(invalid, replay_text, daily_full_text)
        assert any(
            "structured replay result gate" in error
            or "structured workflow YAML contract invalid" in error
            for error in errors
        )


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


def test_repair_top_level_global_concurrency_is_structurally_fixed() -> None:
    recent_text, replay_text, daily_full_text = _texts()
    expected = (
        "concurrency:\n"
        "  group: daily-full-pipeline-${{ github.ref }}\n"
        "  cancel-in-progress: false\n"
    )
    variants = (
        recent_text.replace(expected, "", 1),
        recent_text.replace(
            expected,
            "concurrency:\n"
            "  group: manual-bypass-${{ github.run_id }}\n"
            "  cancel-in-progress: false\n"
            "# group: daily-full-pipeline-${{ github.ref }}\n",
            1,
        ),
        recent_text.replace(
            "  group: daily-full-pipeline-${{ github.ref }}\n",
            "  group: daily-full-pipeline-${{ github.ref }}\n"
            '  "gr\\u006fup": manual-bypass-${{ github.run_id }}\n',
            1,
        ),
        recent_text.replace(
            "  cancel-in-progress: false\n",
            "  cancel-in-progress: !!str false\n",
            1,
        ),
    )

    for invalid in variants:
        assert invalid != recent_text
        errors = validator.validate(invalid, replay_text, daily_full_text)
        assert any(
            "top-level global production concurrency" in error
            or "structured workflow YAML contract invalid" in error
            for error in errors
        )


def test_structured_replay_gate_rejects_shell_or_environment_overrides() -> None:
    recent_text, replay_text, daily_full_text = _texts()
    variants = (
        recent_text.replace(
            "        shell: /bin/bash --noprofile --norc -e -o pipefail {0}\n",
            "        shell: bash\n",
            1,
        ),
        recent_text.replace("          BASH_ENV: /dev/null\n", "          BASH_ENV: /tmp/attacker\n", 1),
        recent_text.replace(
            "permissions:\n",
            "defaults:\n  run:\n    shell: bash\n\npermissions:\n",
            1,
        ),
        recent_text.replace(
            "      - name: Verify bundle and dispatch exactly one Daily Full resume\n",
            "      - name: Rewrite structured replay decision\n"
            "        run: |\n"
            "          echo \"STRUCTURED_REPLAY_REQUIRED=false\" >> \"$GITHUB_ENV\"\n"
            "          echo \"STRUCTURED_REPLAY_RESULT=skipped\" >> \"$GITHUB_ENV\"\n\n"
            "      - name: Verify bundle and dispatch exactly one Daily Full resume\n",
            1,
        ),
        recent_text.replace(
            "          STRUCTURED_REPLAY_REQUIRED: ${{ needs.plan-structured-objective-source-catch-up.outputs.should_replay }}\n",
            "          STRUCTURED_REPLAY_REQUIRED: false\n",
            1,
        ),
        recent_text.replace(
            "          STRUCTURED_PLAN_RESULT: ${{ needs.plan-structured-objective-source-catch-up.result }}\n",
            "          STRUCTURED_PLAN_RESULT: success\n",
            1,
        ),
    )

    for invalid in variants:
        errors = validator.validate(invalid, replay_text, daily_full_text)
        assert errors


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
