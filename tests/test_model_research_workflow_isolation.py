from __future__ import annotations

import subprocess
from dataclasses import replace

import pytest

from scripts import validate_apps_script_workflow_triggers as apps_validator
from scripts import validate_model_research_workflow_isolation as validator


def _inputs() -> tuple[str, list[validator.WorkflowEntrypoint], dict[str, str]]:
    text = validator.WORKFLOW.read_text(encoding="utf-8")
    return text, validator.load_registry(), validator.load_model_owned_producers()


def _replace_in_named_step(
    text: str,
    step_name: str,
    exact: str,
    replacement: str,
) -> str:
    marker = f"      - name: {step_name}\n"
    start = text.index(marker)
    end = text.find("\n      - name: ", start + len(marker))
    if end < 0:
        end = len(text)
    block = text[start:end]
    assert exact in block
    return text[:start] + block.replace(exact, replacement, 1) + text[end:]


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

    assert any(
        "commit commands must be exact supersede, candidate repair, rebaseline, then generic commits"
        in error
        for error in errors
    )


def test_research_publish_block_rejects_disabled_fail_closed_shell() -> None:
    text, rows, producers = _inputs()
    marker = (
        "      - name: Commit research and backtest outputs\n"
        f"        if: {validator.PUBLISH_STEP_IF}\n"
        "        env:\n"
    )
    publish_index = text.index(marker)
    shell_index = text.index(
        f"          {validator.PUBLISH_FAIL_CLOSED_SHELL}\n",
        publish_index,
    )
    mutated = (
        text[:shell_index]
        + "          set +e\n"
        + text[shell_index + len(f"          {validator.PUBLISH_FAIL_CLOSED_SHELL}\n") :]
    )

    errors = validator.validate_workflow_text(mutated, rows, producers)

    assert any("missing fail-closed shell mode" in error for error in errors)
    assert any("must not mask shell failure" in error for error in errors)


def test_research_publish_block_rejects_continue_on_error() -> None:
    text, rows, producers = _inputs()
    marker = (
        "      - name: Commit research and backtest outputs\n"
        f"        if: {validator.PUBLISH_STEP_IF}\n"
    )
    assert marker in text
    mutated = text.replace(
        marker,
        marker + "        continue-on-error: true\n",
        1,
    )

    errors = validator.validate_workflow_text(mutated, rows, producers)

    assert any(
        "research publish step must not define continue-on-error" in error
        for error in errors
    )


def test_revenue_build_step_rejects_dynamic_continue_on_error() -> None:
    text, rows, producers = _inputs()
    marker = (
        "      - name: Build model-owned revenue lag and strength research\n"
        f"        if: {validator.REVENUE_BUILD_STEP_IF}\n"
    )
    assert marker in text
    mutated = text.replace(
        marker,
        marker + "        continue-on-error: ${{ github.event.inputs.allow_failure }}\n",
        1,
    )

    errors = validator.validate_workflow_text(mutated, rows, producers)

    assert any(
        "revenue build step must not define continue-on-error" in error
        for error in errors
    )


def test_revenue_build_step_rejects_shell_without_errexit() -> None:
    text, rows, producers = _inputs()
    marker = (
        "      - name: Build model-owned revenue lag and strength research\n"
        f"        if: {validator.REVENUE_BUILD_STEP_IF}\n"
    )
    assert marker in text
    mutated = text.replace(marker, marker + "        shell: bash {0}\n", 1)

    errors = validator.validate_workflow_text(mutated, rows, producers)

    assert any("revenue build step must not override" in error for error in errors)


def test_research_job_rejects_defaults_shell_without_errexit() -> None:
    text, rows, producers = _inputs()
    marker = "    runs-on: ubuntu-latest\n"
    assert marker in text
    mutated = text.replace(
        marker,
        marker + "    defaults:\n      run:\n        shell: bash {0}\n",
        1,
    )

    errors = validator.validate_workflow_text(mutated, rows, producers)

    assert any("must not override defaults.run.shell" in error for error in errors)


def test_research_job_exact_keys_reject_defaults_working_directory() -> None:
    text, rows, producers = _inputs()
    marker = "    runs-on: ubuntu-latest\n"
    mutated = text.replace(
        marker,
        marker
        + "    defaults:\n"
        + "      run:\n"
        + "        working-directory: scripts\n",
        1,
    )

    errors = validator.validate_workflow_text(mutated, rows, producers)

    assert any("job semantic keys must remain exact" in error for error in errors)


@pytest.mark.parametrize(
    "second_job_key",
    (
        "unprotected-research-bypass",
        '"unprotected-research-byp\\u0061ss"',
    ),
)
def test_semantic_jobs_mapping_rejects_second_job(second_job_key: str) -> None:
    text, rows, producers = _inputs()
    second_job = (
        f"\n  {second_job_key}:\n"
        "    runs-on: ubuntu-latest\n"
        "    steps:\n"
        "      - name: Bypass protected research job\n"
        "        run: python scripts/build_revenue_unreacted_range_research.py\n"
    )
    mutated = text.rstrip() + second_job

    errors = validator.validate_workflow_text(mutated, rows, producers)

    assert any("jobs must contain exactly the single protected research job" in error for error in errors)


@pytest.mark.parametrize(
    "continue_value",
    ("true", "${{ github.event.inputs.allow_failure }}"),
)
def test_research_job_rejects_true_or_dynamic_continue_on_error(
    continue_value: str,
) -> None:
    text, rows, producers = _inputs()
    marker = "    runs-on: ubuntu-latest\n"
    assert marker in text
    mutated = text.replace(
        marker,
        marker + f"    continue-on-error: {continue_value}\n",
        1,
    )

    errors = validator.validate_workflow_text(mutated, rows, producers)

    assert any(
        "research workflow job must not define continue-on-error" in error
        for error in errors
    )


def test_research_workflow_rejects_top_level_defaults_shell_without_errexit() -> None:
    text, rows, producers = _inputs()
    marker = "name: Research Backtest Pipeline\n"
    assert marker in text
    mutated = text.replace(
        marker,
        marker + "defaults:\n  run:\n    shell: bash {0}\n",
        1,
    )

    errors = validator.validate_workflow_text(mutated, rows, producers)

    assert any("must not override defaults.run.shell" in error for error in errors)


@pytest.mark.parametrize(
    ("marker", "label"),
    (
        (
            "      - name: Validate Apps Script workflow triggers\n",
            "research preflight",
        ),
        (
            "      - name: Validate post-run model research contracts\n"
            "        if: ${{ env.MODEL_RESEARCH_SELECTED == 'true' }}\n",
            "post-run research validation",
        ),
    ),
)
def test_research_validation_steps_reject_masking_metadata(
    marker: str,
    label: str,
) -> None:
    text, rows, producers = _inputs()
    assert marker in text
    dynamic = text.replace(
        marker,
        marker + "        continue-on-error: ${{ github.event.inputs.allow_failure }}\n",
        1,
    )
    dynamic_errors = validator.validate_workflow_text(dynamic, rows, producers)
    assert any(
        f"{label} step must not define continue-on-error" in error
        for error in dynamic_errors
    )

    shell = text.replace(marker, marker + "        shell: bash {0}\n", 1)
    shell_errors = validator.validate_workflow_text(shell, rows, producers)
    assert any(f"{label} step must not override" in error for error in shell_errors)


def test_research_preflight_rejects_disabling_condition() -> None:
    text, rows, producers = _inputs()
    marker = "      - name: Validate Apps Script workflow triggers\n"
    assert marker in text
    mutated = text.replace(marker, marker + "        if: false\n", 1)

    errors = validator.validate_workflow_text(mutated, rows, producers)

    assert any("research preflight step must retain its exact" in error for error in errors)


def test_research_publish_step_rejects_dynamic_continue_or_shell_override() -> None:
    text, rows, producers = _inputs()
    marker = (
        "      - name: Commit research and backtest outputs\n"
        f"        if: {validator.PUBLISH_STEP_IF}\n"
    )
    assert marker in text
    dynamic = text.replace(
        marker,
        marker + "        continue-on-error: ${{ github.event.inputs.allow_failure }}\n",
        1,
    )
    dynamic_errors = validator.validate_workflow_text(dynamic, rows, producers)
    assert any(
        "research publish step must not define continue-on-error" in error
        for error in dynamic_errors
    )

    shell = text.replace(marker, marker + "        shell: bash {0}\n", 1)
    shell_errors = validator.validate_workflow_text(shell, rows, producers)
    assert any(
        "research publish step must not override" in error for error in shell_errors
    )


@pytest.mark.parametrize("job_if_key", ("if", "'if'", '"if"'))
def test_research_job_rejects_quoted_or_unquoted_disabling_if(job_if_key: str) -> None:
    text, rows, producers = _inputs()
    marker = "    runs-on: ubuntu-latest\n"
    assert marker in text
    mutated = text.replace(marker, marker + f"    {job_if_key}: false\n", 1)

    errors = validator.validate_workflow_text(mutated, rows, producers)

    assert any("workflow job must not define if metadata" in error for error in errors)


@pytest.mark.parametrize("job_shell_key", ("shell", "'shell'", '"shell"'))
def test_research_job_rejects_quoted_or_unquoted_shell_override(
    job_shell_key: str,
) -> None:
    text, rows, producers = _inputs()
    marker = "    runs-on: ubuntu-latest\n"
    mutated = text.replace(marker, marker + f"    {job_shell_key}: bash {{0}}\n", 1)

    errors = validator.validate_workflow_text(mutated, rows, producers)

    assert any("workflow job must not define shell metadata" in error for error in errors)


@pytest.mark.parametrize(
    "continue_line",
    (
        "continue-on-error: true\n",
        "'continue-on-error': ${{ github.event.inputs.allow_failure }}\n",
        '"continue-on-error": "false"\n',
    ),
)
def test_research_workflow_rejects_top_level_continue_masking(
    continue_line: str,
) -> None:
    text, rows, producers = _inputs()
    marker = "name: Research Backtest Pipeline\n"
    mutated = text.replace(marker, marker + continue_line, 1)

    errors = validator.validate_workflow_text(mutated, rows, producers)

    assert any("top-level continue-on-error" in error for error in errors)


@pytest.mark.parametrize(
    "defaults_line",
    (
        'defaults: {run: {shell: "bash {0}"}}\n',
        "'defaults': {run: {shell: \"bash {0}\"}}\n",
    ),
)
def test_research_workflow_rejects_inline_top_level_defaults_shell(
    defaults_line: str,
) -> None:
    text, rows, producers = _inputs()
    marker = "name: Research Backtest Pipeline\n"
    mutated = text.replace(marker, marker + defaults_line, 1)

    errors = validator.validate_workflow_text(mutated, rows, producers)

    assert any("must not override defaults.run.shell" in error for error in errors)


@pytest.mark.parametrize(
    "defaults_block",
    (
        "defaults:\n  run:\n    working-directory: scripts\n",
        '"d\\u0065faults": {run: {working-directory: scripts}}\n',
        "? defaults\n: {run: {working-directory: scripts}}\n",
        "defaults: {run: {working-directory: .}, future-runtime-key: enabled}\n",
    ),
)
def test_semantic_workflow_rejects_any_root_defaults(
    defaults_block: str,
) -> None:
    text, rows, producers = _inputs()
    marker = "name: Research Backtest Pipeline\n"
    mutated = text.replace(marker, marker + defaults_block, 1)

    errors = validator.validate_workflow_text(mutated, rows, producers)

    assert any("must not define workflow-level defaults" in error for error in errors)


def test_research_preflight_rejects_quoted_disabling_condition() -> None:
    text, rows, producers = _inputs()
    marker = "      - name: Validate Apps Script workflow triggers\n"
    mutated = text.replace(marker, marker + "        'if': false\n", 1)

    errors = validator.validate_workflow_text(mutated, rows, producers)

    assert any("research preflight step must retain its exact" in error for error in errors)


def test_research_preflight_rejects_rebaseline_env_remapping() -> None:
    text, rows, producers = _inputs()
    exact = (
        "          REVENUE_RESEARCH_ENABLED: "
        "${{ github.event.inputs.run_revenue_unreacted_range_research }}\n"
    )
    assert exact in text
    mutated = text.replace(exact, "          REVENUE_RESEARCH_ENABLED: false\n", 1)

    errors = validator.validate_workflow_text(mutated, rows, producers)

    assert any("preflight step must retain its exact env" in error for error in errors)


def test_revenue_rebaseline_step_rejects_quoted_shell_override() -> None:
    text, rows, producers = _inputs()
    step_name, _command = validator.REVENUE_PROJECTION_REBASELINE_COMMAND_STEPS[0]
    marker = (
        f"      - name: {step_name}\n"
        f"        if: {validator.REVENUE_PROJECTION_REBASELINE_STEP_IF}\n"
    )
    assert marker in text
    mutated = text.replace(marker, marker + "        'shell': bash {0}\n", 1)

    errors = validator.validate_workflow_text(mutated, rows, producers)

    assert any(f"{step_name} step must not override" in error for error in errors)


def test_research_workflow_rejects_top_level_disabling_if() -> None:
    text, rows, producers = _inputs()
    marker = "name: Research Backtest Pipeline\n"
    mutated = text.replace(marker, marker + "if: false\n", 1)

    errors = validator.validate_workflow_text(mutated, rows, producers)

    assert any("must not define top-level if metadata" in error for error in errors)


def test_sync_install_and_preflight_are_exact_and_consecutive() -> None:
    text, rows, producers = _inputs()
    exact_sync = (
        f"      - name: {validator.SYNC_TARGET_BRANCH_STEP_NAME}\n"
        "        run: |\n"
        f"          {validator.SYNC_TARGET_BRANCH_COMMAND}\n\n"
    )
    exact_install = (
        f"      - name: {validator.PY_YAML_INSTALL_STEP_NAME}\n"
        "        run: |\n"
        f"          {validator.PY_YAML_INSTALL_COMMAND}\n\n"
    )
    preflight_marker = f"      - name: {validator.RESEARCH_PREFLIGHT_STEP_NAME}\n"
    assert exact_sync + exact_install + preflight_marker in text

    version_drift = text.replace("PyYAML==6.0.2", "PyYAML==6.0.1", 1)
    version_errors = validator.validate_workflow_text(version_drift, rows, producers)
    assert any("exact single-command parser bootstrap" in error for error in version_errors)

    for following_step in (
        validator.PY_YAML_INSTALL_STEP_NAME,
        validator.RESEARCH_PREFLIGHT_STEP_NAME,
    ):
        following_marker = f"      - name: {following_step}\n"
        interposed = text.replace(
            following_marker,
            "      - name: Interpose in synchronization bootstrap chain\n"
            "        run: |\n"
            "          echo unexpected\n\n"
            + following_marker,
            1,
        )
        interposed_errors = validator.validate_workflow_text(interposed, rows, producers)
        assert any(
            "must be consecutive in exact order" in error
            for error in interposed_errors
        )


@pytest.mark.parametrize(
    "masking_metadata",
    (
        "        if: false\n",
        "        shell: bash {0}\n",
        "        continue-on-error: true\n",
    ),
)
def test_sync_step_rejects_masking_semantic_metadata(masking_metadata: str) -> None:
    text, rows, producers = _inputs()
    marker = f"      - name: {validator.SYNC_TARGET_BRANCH_STEP_NAME}\n"
    mutated = text.replace(marker, marker + masking_metadata, 1)

    errors = validator.validate_workflow_text(mutated, rows, producers)

    assert any(
        "target branch synchronization step semantic metadata keys drifted" in error
        for error in errors
    )


def test_sync_step_semantic_name_is_exact() -> None:
    text, rows, producers = _inputs()
    marker = f"      - name: {validator.SYNC_TARGET_BRANCH_STEP_NAME}\n"
    mutated = text.replace(
        marker,
        "      - name: Synchronize target branch with failure masking\n",
        1,
    )

    errors = validator.validate_workflow_text(mutated, rows, producers)

    assert any(
        "target branch synchronization step must appear exactly once" in error
        for error in errors
    )


@pytest.mark.parametrize(
    ("root_env_enabled", "sync_mask_enabled"),
    (
        (True, False),
        (False, True),
        (True, True),
    ),
)
def test_workflow_env_and_sync_shell_masking_halves_fail_closed(
    root_env_enabled: bool,
    sync_mask_enabled: bool,
) -> None:
    text, rows, producers = _inputs()
    mutated = text
    if root_env_enabled:
        root_marker = "name: Research Backtest Pipeline\n"
        mutated = mutated.replace(
            root_marker,
            root_marker + "env:\n  BASH_ENV: /tmp/research-mask.sh\n",
            1,
        )
    if sync_mask_enabled:
        sync_command = f"          {validator.SYNC_TARGET_BRANCH_COMMAND}\n"
        shell_mask = (
            "          printf '%s\\n' "
            "'python() { command python \"$@\" || true; }' > \"$BASH_ENV\"\n"
        )
        mutated = mutated.replace(sync_command, sync_command + shell_mask, 1)

    errors = validator.validate_workflow_text(mutated, rows, producers)

    if root_env_enabled:
        assert any("must not define workflow-level env" in error for error in errors)
    if sync_mask_enabled:
        assert any(
            "target branch synchronization must retain its exact single-command" in error
            for error in errors
        )


@pytest.mark.parametrize(
    "root_env_block",
    (
        (
            "env:\n"
            "  BASH_ENV: >-\n"
            "    $(printf '%s\\n' 'python() { command python \"$@\" || true; }' "
            "> /tmp/research-mask.sh;\n"
            "    printf /tmp/research-mask.sh)\n"
        ),
        '"e\\u006ev": {SAFE_VALUE: enabled}\n',
    ),
)
def test_semantic_workflow_mapping_rejects_any_root_env(
    root_env_block: str,
) -> None:
    text, rows, producers = _inputs()
    marker = "name: Research Backtest Pipeline\n"
    mutated = text.replace(marker, marker + root_env_block, 1)

    errors = validator.validate_workflow_text(mutated, rows, producers)

    assert any("must not define workflow-level env" in error for error in errors)


@pytest.mark.parametrize("forbidden_env", ("BASH_ENV", "ENV"))
def test_job_env_digest_and_shell_startup_key_guard_reject_injection(
    forbidden_env: str,
) -> None:
    text, rows, producers = _inputs()
    marker = "    env:\n      TARGET_BRANCH: ${{ github.ref_name }}\n"
    assert marker in text
    mutated = text.replace(
        marker,
        marker + f"      {forbidden_env}: /tmp/research-mask.sh\n",
        1,
    )

    errors = validator.validate_workflow_text(mutated, rows, producers)

    assert any("job env must not define shell startup injection keys" in error for error in errors)
    assert any("research workflow job env drift" in error for error in errors)


def test_job_container_cannot_inject_shell_startup_environment() -> None:
    text, rows, producers = _inputs()
    marker = "    runs-on: ubuntu-latest\n"
    container = (
        "    container:\n"
        "      image: attacker/research-mask:latest\n"
        "      env:\n"
        "        BASH_ENV: /tmp/research-mask.sh\n"
    )
    mutated = text.replace(marker, marker + container, 1)

    errors = validator.validate_workflow_text(mutated, rows, producers)

    assert any("job semantic keys must remain exact" in error for error in errors)


@pytest.mark.parametrize("forbidden_env", ("BASH_ENV", "ENV"))
def test_step_env_rejects_shell_startup_injection_keys(forbidden_env: str) -> None:
    text, rows, producers = _inputs()
    step_name = "Require production artifact write deploy key"
    marker = (
        f"      - name: {step_name}\n"
        "        shell: bash\n"
        "        env:\n"
    )
    assert marker in text
    mutated = text.replace(
        marker,
        marker + f"          {forbidden_env}: /tmp/research-mask.sh\n",
        1,
    )

    errors = validator.validate_workflow_text(mutated, rows, producers)

    assert any(
        "step env must not define shell startup injection keys" in error
        and step_name in error
        for error in errors
    )


@pytest.mark.parametrize(
    ("step_name", "anchor", "channel"),
    (
        (
            validator.DEPLOY_KEY_STEP_NAME,
            "fi",
            "GITHUB_ENV",
        ),
        (
            validator.INSTALL_DEPENDENCIES_STEP_NAME,
            "pip install pandas requests tabulate matplotlib pillow openpyxl lxml "
            "html5lib beautifulsoup4 reportlab pypdf",
            "GITHUB_PATH",
        ),
    ),
)
def test_bootstrap_run_rejects_cross_step_state_channel_writes(
    step_name: str,
    anchor: str,
    channel: str,
) -> None:
    text, rows, producers = _inputs()
    mutated = _replace_in_named_step(
        text,
        step_name,
        anchor,
        anchor + f'\n          printf injected >> "${channel}"',
    )

    errors = validator.validate_workflow_text(mutated, rows, producers)

    assert any(
        "must not write or reference cross-step shell state channels" in error
        and step_name in error
        and channel in error
        for error in errors
    )
    assert any(
        "bootstrap step must retain its exact semantic metadata and body" in error
        and step_name in error
        for error in errors
    )


def test_decoded_run_scalar_rejects_escaped_cross_step_state_channel() -> None:
    text, rows, producers = _inputs()
    step_name = "Build MSCI Taiwan rebalance event backtest"
    escaped_run = (
        '        run: "printf injected >> \\"$GITHUB\\u005fPATH\\""'
    )
    marker = f"      - name: {step_name}\n"
    start = text.index(marker)
    end = text.find("\n      - name: ", start + len(marker))
    block = text[start : len(text) if end < 0 else end]
    run_start = block.index("        run:")
    mutated = text[:start] + block[:run_start] + escaped_run + (
        "" if end < 0 else text[end:]
    )

    errors = validator.validate_workflow_text(mutated, rows, producers)

    assert any(
        "must not write or reference cross-step shell state channels" in error
        and step_name in error
        and "GITHUB_PATH" in error
        for error in errors
    )


@pytest.mark.parametrize(
    ("step_name", "anchor", "obfuscated_writer"),
    (
        (
            validator.DEPLOY_KEY_STEP_NAME,
            "fi",
            'channel=GITHUB_E; channel="${channel}NV"; printf injected >> "${!channel}"',
        ),
        (
            validator.INSTALL_DEPENDENCIES_STEP_NAME,
            "pip install pandas requests tabulate matplotlib pillow openpyxl lxml "
            "html5lib beautifulsoup4 reportlab pypdf",
            'channel=GITHUB_; channel="${channel}PATH"; printf injected >> "${!channel}"',
        ),
    ),
)
def test_bootstrap_exact_mapping_rejects_obfuscated_state_writer(
    step_name: str,
    anchor: str,
    obfuscated_writer: str,
) -> None:
    text, rows, producers = _inputs()
    assert not any(
        channel in obfuscated_writer
        for channel in validator.FORBIDDEN_CROSS_STEP_STATE_CHANNELS
    )
    mutated = _replace_in_named_step(
        text,
        step_name,
        anchor,
        anchor + "\n          " + obfuscated_writer,
    )

    errors = validator.validate_workflow_text(mutated, rows, producers)

    assert any(
        "bootstrap step must retain its exact semantic metadata and body" in error
        and step_name in error
        for error in errors
    )


@pytest.mark.parametrize(
    ("step_name", "exact_uses", "replacement_uses"),
    (
        (
            validator.CHECKOUT_STEP_NAME,
            "actions/checkout@v6",
            "attacker/checkout-and-write-env@v1",
        ),
        (
            validator.SETUP_PYTHON_STEP_NAME,
            "actions/setup-python@v6",
            "attacker/setup-python-and-write-path@v1",
        ),
    ),
)
def test_rebaseline_active_action_uses_are_exact_locked(
    step_name: str,
    exact_uses: str,
    replacement_uses: str,
) -> None:
    text, rows, producers = _inputs()
    mutated = _replace_in_named_step(
        text,
        step_name,
        f"uses: {exact_uses}",
        f"uses: {replacement_uses}",
    )

    errors = validator.validate_workflow_text(mutated, rows, producers)

    assert any(
        "bootstrap step must retain its exact semantic metadata and body" in error
        and step_name in error
        for error in errors
    )
    assert any("step control plane drift" in error for error in errors)


@pytest.mark.parametrize(
    ("step_name", "exact_with", "replacement_with"),
    (
        (
            validator.CHECKOUT_STEP_NAME,
            "persist-credentials: true",
            "persist-credentials: false",
        ),
        (
            validator.SETUP_PYTHON_STEP_NAME,
            'python-version: "3.11"',
            'python-version: "3.12"',
        ),
    ),
)
def test_rebaseline_active_action_with_metadata_is_exact_locked(
    step_name: str,
    exact_with: str,
    replacement_with: str,
) -> None:
    text, rows, producers = _inputs()
    mutated = _replace_in_named_step(
        text,
        step_name,
        exact_with,
        replacement_with,
    )

    errors = validator.validate_workflow_text(mutated, rows, producers)

    assert any(
        "bootstrap step must retain its exact semantic metadata and body" in error
        and step_name in error
        for error in errors
    )


def test_rebaseline_bootstrap_dependency_order_is_exact() -> None:
    text, rows, producers = _inputs()
    dependency_marker = f"      - name: {validator.INSTALL_DEPENDENCIES_STEP_NAME}\n"
    mutated = text.replace(
        dependency_marker,
        "      - name: Interposed bootstrap state writer\n"
        "        run: echo unexpected\n\n"
        + dependency_marker,
        1,
    )

    errors = validator.validate_workflow_text(mutated, rows, producers)

    assert any("bootstrap steps must occupy the exact leading order" in error for error in errors)
    assert any("step control plane drift" in error for error in errors)


def test_skipped_step_cannot_be_reactivated_during_rebaseline() -> None:
    text, rows, producers = _inputs()
    step_name = "Build market timing technical backtest"
    exact_if = "${{ github.event.inputs.run_market_timing == 'true' }}"
    mutated = _replace_in_named_step(
        text,
        step_name,
        f"if: {exact_if}",
        "if: ${{ always() }}",
    )

    errors = validator.validate_workflow_text(mutated, rows, producers)

    assert any("step control plane drift" in error for error in errors)


def test_semantic_yaml_rejects_escaped_duplicate_critical_step_key() -> None:
    text, rows, producers = _inputs()
    step_name, _command = validator.REVENUE_PROJECTION_REBASELINE_COMMAND_STEPS[0]
    marker = (
        f"      - name: {step_name}\n"
        f"        if: {validator.REVENUE_PROJECTION_REBASELINE_STEP_IF}\n"
    )
    assert marker in text
    mutated = text.replace(marker, marker + '        "i\\u0066": false\n', 1)

    errors = validator.validate_workflow_text(mutated, rows, producers)

    assert any(
        "YAML semantic parse failed" in error and "duplicate semantic key" in error
        for error in errors
    )


def test_semantic_yaml_rejects_explicit_critical_step_shell_key() -> None:
    text, rows, producers = _inputs()
    step_name, _command = validator.REVENUE_PROJECTION_REBASELINE_COMMAND_STEPS[0]
    marker = (
        f"      - name: {step_name}\n"
        f"        if: {validator.REVENUE_PROJECTION_REBASELINE_STEP_IF}\n"
    )
    assert marker in text
    mutated = text.replace(marker, marker + "        ? shell\n        : bash {0}\n", 1)

    errors = validator.validate_workflow_text(mutated, rows, producers)

    assert any(f"{step_name} step must not override" in error for error in errors)


@pytest.mark.parametrize(
    "job_if_metadata",
    (
        '    "i\\u0066": false\n',
        "    ? if\n    : false\n",
    ),
)
def test_semantic_yaml_rejects_escaped_or_explicit_job_if(
    job_if_metadata: str,
) -> None:
    text, rows, producers = _inputs()
    marker = "    runs-on: ubuntu-latest\n"
    mutated = text.replace(marker, marker + job_if_metadata, 1)

    errors = validator.validate_workflow_text(mutated, rows, producers)

    assert any("workflow job must not define if metadata" in error for error in errors)


def test_semantic_yaml_rejects_escaped_inline_workflow_defaults_shell() -> None:
    text, rows, producers = _inputs()
    marker = "name: Research Backtest Pipeline\n"
    escaped_defaults = '"d\\u0065faults": {run: {shell: "bash {0}"}}\n'
    mutated = text.replace(marker, marker + escaped_defaults, 1)

    errors = validator.validate_workflow_text(mutated, rows, producers)

    assert any("must not override defaults.run.shell" in error for error in errors)


def test_semantic_yaml_rejects_explicit_preflight_if_key() -> None:
    text, rows, producers = _inputs()
    marker = f"      - name: {validator.RESEARCH_PREFLIGHT_STEP_NAME}\n"
    mutated = text.replace(marker, marker + "        ? if\n        : false\n", 1)

    errors = validator.validate_workflow_text(mutated, rows, producers)

    assert any("research preflight step must not define an if" in error for error in errors)


@pytest.mark.parametrize(
    ("exact", "replacement"),
    (
        ("jobs:\n", "jobs: &research_jobs\n"),
        (
            "name: Research Backtest Pipeline\n",
            "name: Research Backtest Pipeline\nresearch_jobs_copy: *research_jobs\n",
        ),
        (
            "name: Research Backtest Pipeline\n",
            "name: !!str Research Backtest Pipeline\n",
        ),
    ),
)
def test_semantic_yaml_rejects_anchor_alias_or_explicit_tag(
    exact: str,
    replacement: str,
) -> None:
    text, rows, producers = _inputs()
    mutated = text.replace(exact, replacement, 1)

    errors = validator.validate_workflow_text(mutated, rows, producers)

    assert any("anchors, aliases, and explicit tags are forbidden" in error for error in errors)


@pytest.mark.parametrize(
    ("exact", "replacement"),
    (
        (
            "name: Research Backtest Pipeline\n",
            "name: Research Backtest Pipeline\nname: Duplicate\n",
        ),
        ("jobs:\n", "jobs: [\n"),
    ),
)
def test_semantic_yaml_fails_closed_on_duplicate_or_malformed_root(
    exact: str,
    replacement: str,
) -> None:
    text, rows, producers = _inputs()
    mutated = text.replace(exact, replacement, 1)

    errors = validator.validate_workflow_text(mutated, rows, producers)

    assert any("YAML semantic parse failed" in error for error in errors)


def test_research_job_env_exact_lock_rejects_selector_masking() -> None:
    text, rows, producers = _inputs()
    model_selected_line = next(
        line for line in text.splitlines() if "MODEL_RESEARCH_SELECTED:" in line
    )
    assert model_selected_line.endswith(" }}")
    masked_line = model_selected_line[:-3] + " && false }}"
    mutated = text.replace(model_selected_line, masked_line, 1)

    errors = validator.validate_workflow_text(mutated, rows, producers)

    assert any("research workflow job env drift" in error for error in errors)


@pytest.mark.parametrize(
    "name_key",
    (
        '      - "n\\u0061me": ',
        "      - ? name\n        : ",
    ),
)
def test_semantic_step_run_lock_rejects_escaped_or_explicit_name_masking(
    name_key: str,
) -> None:
    text, rows, producers = _inputs()
    marker = f"      - name: {validator.POST_RUN_STEP_NAME}\n"
    mutated = text.replace(
        marker,
        name_key + validator.POST_RUN_STEP_NAME + "\n",
        1,
    )
    first_validator = (
        "          python scripts/validate_daily_model_background_data_registry.py\n"
    )
    sentinel = f"          printf 'pass\\n' > \"{validator.POST_RUN_SENTINEL}\"\n"
    assert first_validator in mutated
    assert sentinel in mutated
    mutated = mutated.replace(
        first_validator,
        "          if false; then\n" + first_validator,
        1,
    ).replace(sentinel, "          fi\n" + sentinel, 1)

    errors = validator.validate_workflow_text(mutated, rows, producers)

    assert any("post-run research validation run body" in error for error in errors)


def test_revenue_build_and_publish_steps_retain_exact_conditions() -> None:
    text, rows, producers = _inputs()
    mutations = (
        (
            "      - name: Build model-owned revenue lag and strength research\n"
            f"        if: {validator.REVENUE_BUILD_STEP_IF}\n",
            "      - name: Build model-owned revenue lag and strength research\n"
            "        if: ${{ always() }}\n",
            "revenue build step must retain its exact",
        ),
        (
            "      - name: Commit research and backtest outputs\n"
            f"        if: {validator.PUBLISH_STEP_IF}\n",
            "      - name: Commit research and backtest outputs\n"
            "        if: ${{ always() }}\n",
            "research publish step must retain its exact",
        ),
    )
    for exact_marker, replacement_marker, expected_error in mutations:
        assert exact_marker in text
        mutated = text.replace(exact_marker, replacement_marker, 1)
        errors = validator.validate_workflow_text(mutated, rows, producers)
        assert any(expected_error in error for error in errors)


def test_research_publish_block_rejects_retrying_rebase_push_helper() -> None:
    text, rows, producers = _inputs()
    mutated = text.replace(
        validator.PUBLISH_PUSH,
        'bash scripts/ci_push_with_retry.sh "$TARGET_BRANCH" 5',
        1,
    )

    errors = validator.validate_workflow_text(mutated, rows, producers)

    assert any("must not retry or rebase" in error for error in errors)
    assert any("exactly four direct fail-closed pushes" in error for error in errors)


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

    assert any("exactly four direct fail-closed pushes" in error for error in errors)


def test_research_workflow_rejects_duplicate_commit_push_block() -> None:
    text, rows, producers = _inputs()
    mutated = text + (
        "\n      - name: Duplicate publish block\n"
        "        run: |\n"
        f"          {validator.PUBLISH_COMMIT}\n"
        f"          {validator.PUBLISH_PUSH}\n"
    )

    errors = validator.validate_workflow_text(mutated, rows, producers)

    assert any(
        "exactly one generic, one supersede, one candidate repair, and one rebaseline"
        in error
        for error in errors
    )
    assert any("commit commands must be exact" in error for error in errors)
    assert any("exactly four direct fail-closed pushes" in error for error in errors)


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
        "python scripts/validate_revenue_unreacted_range_promotion_preparation.py --require-source-artifacts",
    }
    assert projection_chain_validators <= validator.REVENUE_PROJECTION_CHAIN_VALIDATOR_COMMANDS
    assert projection_chain_validators <= {line.strip() for line in text.splitlines()}
    assert validator.validate_workflow_text(text, rows, producers) == []


def test_revenue_projection_rebaseline_stage_is_workflow_only_and_false_default() -> None:
    text, rows, producers = _inputs()
    stage_input = validator.REVENUE_PROJECTION_REBASELINE_STAGE_INPUT

    assert validator.workflow_input_defaults(text)[stage_input] == "false"
    assert validator.workflow_input_types(text)[stage_input] == "boolean"
    assert stage_input not in {row.workflow_input for row in rows}
    any_selected_line = next(
        line for line in text.splitlines() if "ANY_RESEARCH_SELECTED:" in line
    )
    model_selected_line = next(
        line for line in text.splitlines() if "MODEL_RESEARCH_SELECTED:" in line
    )
    assert stage_input not in any_selected_line
    assert stage_input not in model_selected_line
    assert validator.validate_workflow_text(text, rows, producers) == []


def test_revenue_projection_candidate_repair_is_workflow_only_and_false_default() -> None:
    text, rows, producers = _inputs()
    stage_input = validator.REVENUE_PROJECTION_CANDIDATE_REPAIR_STAGE_INPUT

    assert validator.workflow_input_defaults(text)[stage_input] == "false"
    assert validator.workflow_input_types(text)[stage_input] == "boolean"
    assert stage_input not in {row.workflow_input for row in rows}
    any_selected_line = next(
        line for line in text.splitlines() if "ANY_RESEARCH_SELECTED:" in line
    )
    model_selected_line = next(
        line for line in text.splitlines() if "MODEL_RESEARCH_SELECTED:" in line
    )
    assert stage_input not in any_selected_line
    assert stage_input not in model_selected_line
    dispatch_row = apps_validator.load_research_dispatch_registry()[stage_input]
    assert dispatch_row["activation_mode"] == "workflow_only"
    assert dispatch_row["producer"] == "scripts/build_model_data_independence_audit.py"
    assert validator.validate_workflow_text(text, rows, producers) == []


def test_revenue_projection_candidate_repair_runs_only_exact_authorized_python() -> None:
    text, rows, producers = _inputs()
    mapping, yaml_errors = validator._semantic_workflow_mapping(text)
    assert yaml_errors == []
    assert mapping is not None
    steps = mapping["jobs"][validator.RESEARCH_JOB_NAME]["steps"]
    repair_steps = [
        step
        for step in steps
        if step.get("if") == validator.REVENUE_PROJECTION_CANDIDATE_REPAIR_STEP_IF
    ]
    assert [step["name"] for step in repair_steps] == [
        *(
            name
            for name, _command in validator.REVENUE_PROJECTION_CANDIDATE_REPAIR_COMMAND_STEPS
        ),
        validator.REVENUE_PROJECTION_CANDIDATE_REPAIR_CLOSURE_STEP_NAME,
        validator.REVENUE_PROJECTION_CANDIDATE_REPAIR_STAGE_STEP_NAME,
        validator.REVENUE_PROJECTION_CANDIDATE_REPAIR_COMMIT_STEP_NAME,
    ]
    python_lines = tuple(
        line.strip()
        for step in repair_steps
        for line in step["run"].splitlines()
        if line.strip().startswith("python ")
    )
    assert python_lines == (
        validator.REVENUE_PROJECTION_CANDIDATE_REPAIR_COMMAND,
        *validator.REVENUE_PROJECTION_CANDIDATE_REPAIR_VALIDATOR_COMMANDS,
    )
    assert validator.validate_workflow_text(text, rows, producers) == []


def test_revenue_projection_candidate_repair_skips_normal_build_and_publish() -> None:
    text, rows, producers = _inputs()
    candidate_condition = (
        "github.event.inputs."
        f"{validator.REVENUE_PROJECTION_CANDIDATE_REPAIR_STAGE_INPUT} != 'true'"
    )
    assert candidate_condition in validator.REVENUE_BUILD_STEP_IF
    assert candidate_condition in validator.PUBLISH_STEP_IF

    for step_name, expected_if in (
        (validator.REVENUE_BUILD_STEP_NAME, validator.REVENUE_BUILD_STEP_IF),
        (validator.PUBLISH_STEP_NAME, validator.PUBLISH_STEP_IF),
    ):
        block = validator._named_step_blocks(validator.workflow_step_blocks(text), step_name)
        assert len(block) == 1
        assert f"        if: {expected_if}" in block[0]
    assert validator.validate_workflow_text(text, rows, producers) == []


@pytest.mark.parametrize(
    ("step_name", "metadata"),
    (
        (
            "Normalize revenue projection candidate audit CSV line endings",
            "        continue-on-error: true\n",
        ),
        (
            validator.REVENUE_PROJECTION_CANDIDATE_REPAIR_STAGE_STEP_NAME,
            "        shell: bash {0}\n",
        ),
        (
            validator.REVENUE_PROJECTION_CANDIDATE_REPAIR_COMMIT_STEP_NAME,
            "        if: ${{ false }}\n",
        ),
    ),
)
def test_revenue_projection_candidate_repair_rejects_masking_metadata(
    step_name: str,
    metadata: str,
) -> None:
    text, rows, producers = _inputs()
    marker = f"      - name: {step_name}\n"
    mutated = text.replace(marker, marker + metadata, 1)

    errors = validator.validate_workflow_text(mutated, rows, producers)

    assert errors
    assert any(
        "metadata keys drifted" in error
        or "step control plane drift" in error
        or "fail-closed if condition" in error
        or "duplicate semantic key" in error
        for error in errors
    )


def test_revenue_projection_candidate_repair_guards_and_tail_order_are_exact() -> None:
    text, rows, producers = _inputs()
    guards = (
        (
            'if [[ "$REVENUE_SOURCE_PROJECTION_CANDIDATE_REPAIR_ONLY" == "true" && '
            '"$REVENUE_RESEARCH_ENABLED" != "true" ]]; then',
            "primary revenue workflow input",
        ),
        (
            'if [[ "$REVENUE_SOURCE_PROJECTION_CANDIDATE_REPAIR_ONLY" == "true" && '
            '( "$REVENUE_FORWARD_HOLDOUT_ONLY" == "true" || '
            '"$REVENUE_SOURCE_PROJECTION_CHAIN_ONLY" == "true" || '
            '"$REVENUE_SOURCE_PROJECTION_REBASELINE_ONLY" == "true" || '
            '"$REVENUE_SOURCE_PROJECTION_SUPERSEDE_ONLY" == "true" ) ]]; then',
            "mutually exclusive",
        ),
        (
            'if [[ "$REVENUE_SOURCE_PROJECTION_CANDIDATE_REPAIR_ONLY" == "true" && '
            '"$REVENUE_REBASELINE_OTHER_RESEARCH_SELECTED" == "true" ]]; then',
            "every other research input",
        ),
        (
            'if [[ "$REVENUE_SOURCE_PROJECTION_CANDIDATE_REPAIR_ONLY" == "true" && '
            '( "$REVENUE_REBASELINE_REF_TYPE" != "branch" || '
            '"$TARGET_BRANCH" == "main" ) ]]; then',
            "non-main branch ref",
        ),
        (
            validator.REVENUE_PROJECTION_CANDIDATE_REPAIR_RUN_ATTEMPT_GUARD,
            "workflow retry attempts",
        ),
        (
            validator.REVENUE_PROJECTION_CANDIDATE_REPAIR_DISPATCH_HEAD_GUARD,
            "dispatch SHA",
        ),
        (
            validator.REVENUE_PROJECTION_CANDIDATE_REPAIR_CODE_PARENT_GUARD,
            "single authorized code commit",
        ),
    )
    for guard, expected_error in guards:
        assert guard in text
        errors = validator.validate_workflow_text(text.replace(guard, "", 1), rows, producers)
        assert any(expected_error in error for error in errors)

    mapping, yaml_errors = validator._semantic_workflow_mapping(text)
    assert yaml_errors == []
    assert mapping is not None
    names = [
        step["name"]
        for step in mapping["jobs"][validator.RESEARCH_JOB_NAME]["steps"]
    ]
    tail = (
        validator.POST_RUN_STEP_NAME,
        validator.REVENUE_PROJECTION_SUPERSEDE_CLOSURE_STEP_NAME,
        validator.REVENUE_PROJECTION_SUPERSEDE_STAGE_STEP_NAME,
        validator.REVENUE_PROJECTION_SUPERSEDE_COMMIT_STEP_NAME,
        validator.REVENUE_PROJECTION_CANDIDATE_REPAIR_CLOSURE_STEP_NAME,
        validator.REVENUE_PROJECTION_CANDIDATE_REPAIR_STAGE_STEP_NAME,
        validator.REVENUE_PROJECTION_CANDIDATE_REPAIR_COMMIT_STEP_NAME,
        validator.REVENUE_PROJECTION_REBASELINE_CLOSURE_STEP_NAME,
        validator.REVENUE_PROJECTION_REBASELINE_STAGE_STEP_NAME,
        validator.REVENUE_PROJECTION_REBASELINE_COMMIT_STEP_NAME,
        validator.PUBLISH_STEP_NAME,
    )
    start = names.index(tail[0])
    assert tuple(names[start : start + len(tail)]) == tail


def test_revenue_projection_candidate_repair_requires_two_commit_checkout() -> None:
    text, rows, producers = _inputs()
    exact = f"          fetch-depth: {validator.CHECKOUT_FETCH_DEPTH}\n"
    assert exact in text

    for replacement in ("          fetch-depth: 1\n", ""):
        errors = validator.validate_workflow_text(
            text.replace(exact, replacement, 1), rows, producers
        )
        assert any("checkout must retain fetch-depth 2" in error for error in errors)


@pytest.mark.parametrize(
    ("exact", "replacement"),
    (
        (
            "              config/daily_model_data_sharing_registry.csv\n",
            "",
        ),
        (
            "              config/daily_model_data_sharing_registry.csv\n",
            "              config/daily_model_data_sharing_registry.csv\n"
            "              scripts/unauthorized_supersede_writer.py\n",
        ),
        (
            "              config/daily_model_data_sharing_registry.csv\n",
            "              config/renamed_data_sharing_registry.csv\n",
        ),
    ),
)
def test_revenue_projection_supersede_code_path_exact44_rejects_path_drift(
    exact: str,
    replacement: str,
) -> None:
    text, rows, producers = _inputs()
    mutated = _replace_in_named_step(
        text,
        validator.RESEARCH_PREFLIGHT_STEP_NAME,
        exact,
        replacement,
    )

    errors = validator.validate_workflow_text(mutated, rows, producers)

    assert any("exact44 literal code paths" in error for error in errors)


@pytest.mark.parametrize(
    "exact",
    (
        "git --no-replace-objects diff --name-only --no-renames",
        "git --no-replace-objects diff --name-status --no-renames",
        "$'M\\t'\"${REVENUE_SUPERSEDE_CODE_PATHS[$index]}\"",
    ),
)
def test_revenue_projection_supersede_code_commit_identity_guards_are_required(
    exact: str,
) -> None:
    text, rows, producers = _inputs()
    mutated = _replace_in_named_step(
        text,
        validator.RESEARCH_PREFLIGHT_STEP_NAME,
        exact,
        exact.replace("--no-renames", "--find-renames").replace("$'M\\t'", "$'D\\t'"),
    )

    errors = validator.validate_workflow_text(mutated, rows, producers)

    assert any("code-commit identity closure is incomplete" in error for error in errors)


def test_revenue_projection_supersede_unshallows_trusted_candidate_ancestry() -> None:
    text, rows, producers = _inputs()
    exact = (
        'git --no-replace-objects fetch --no-tags --unshallow origin '
        '"$TARGET_BRANCH"'
    )
    mutated = _replace_in_named_step(
        text,
        validator.REVENUE_PROJECTION_SUPERSEDE_CLOSURE_STEP_NAME,
        exact,
        "true",
    )

    errors = validator.validate_workflow_text(mutated, rows, producers)

    assert any("exact75 closure is incomplete" in error for error in errors)


def test_revenue_projection_supersede_unshallow_restores_trusted_ancestry(
    tmp_path,
) -> None:
    source = tmp_path / "source"
    clone = tmp_path / "shallow"
    subprocess.run(
        ["git", "init", "-b", "main", str(source)],
        check=True,
        capture_output=True,
        text=True,
    )
    subprocess.run(
        ["git", "-C", str(source), "config", "user.name", "test"],
        check=True,
    )
    subprocess.run(
        ["git", "-C", str(source), "config", "user.email", "test@example.invalid"],
        check=True,
    )
    marker = source / "marker.txt"
    trusted = ""
    for index in range(5):
        marker.write_text(f"{index}\n", encoding="utf-8")
        subprocess.run(["git", "-C", str(source), "add", "--", "marker.txt"], check=True)
        subprocess.run(
            ["git", "-C", str(source), "commit", "-m", f"commit {index}"],
            check=True,
            capture_output=True,
            text=True,
        )
        if index == 0:
            trusted = subprocess.check_output(
                ["git", "-C", str(source), "rev-parse", "HEAD"],
                text=True,
            ).strip()

    subprocess.run(
        [
            "git",
            "clone",
            "--depth=2",
            "--branch",
            "main",
            source.as_uri(),
            str(clone),
        ],
        check=True,
        capture_output=True,
        text=True,
    )
    assert subprocess.check_output(
        ["git", "-C", str(clone), "rev-parse", "--is-shallow-repository"],
        text=True,
    ).strip() == "true"
    assert subprocess.run(
        ["git", "-C", str(clone), "cat-file", "-e", f"{trusted}^{{commit}}"],
        capture_output=True,
        text=True,
    ).returncode != 0

    subprocess.run(
        [
            "git",
            "--no-replace-objects",
            "-C",
            str(clone),
            "fetch",
            "--no-tags",
            "--unshallow",
            "origin",
            "main",
        ],
        check=True,
        capture_output=True,
        text=True,
    )

    assert subprocess.check_output(
        ["git", "-C", str(clone), "rev-parse", "--is-shallow-repository"],
        text=True,
    ).strip() == "false"
    assert subprocess.check_output(
        ["git", "-C", str(clone), "rev-parse", f"{trusted}^{{commit}}"],
        text=True,
    ).strip() == trusted
    assert subprocess.run(
        [
            "git",
            "--no-replace-objects",
            "-C",
            str(clone),
            "merge-base",
            "--is-ancestor",
            trusted,
            "HEAD",
        ],
        check=False,
    ).returncode == 0


@pytest.mark.parametrize(
    ("exact", "replacement", "expected_error"),
    (
        (
            validator.REVENUE_PROJECTION_CANDIDATE_REPAIR_RUN_ATTEMPT_GUARD,
            validator.REVENUE_PROJECTION_CANDIDATE_REPAIR_RUN_ATTEMPT_GUARD.replace(
                '"$GITHUB_RUN_ATTEMPT"', '"2"'
            ),
            "workflow retry attempts",
        ),
        (
            validator.REVENUE_PROJECTION_CANDIDATE_REPAIR_DISPATCH_HEAD_GUARD,
            validator.REVENUE_PROJECTION_CANDIDATE_REPAIR_DISPATCH_HEAD_GUARD.replace(
                '"$GITHUB_SHA"', '"0000000000000000000000000000000000000000"'
            ),
            "dispatch SHA",
        ),
        (
            validator.REVENUE_PROJECTION_CANDIDATE_REPAIR_CODE_PARENT_GUARD,
            validator.REVENUE_PROJECTION_CANDIDATE_REPAIR_CODE_PARENT_GUARD.replace(
                validator.REVENUE_PROJECTION_CANDIDATE_REPAIR_BASE_COMMIT,
                "0000000000000000000000000000000000000000",
            ),
            "single authorized code commit",
        ),
    ),
)
def test_revenue_projection_candidate_repair_rejects_retry_or_head_identity_drift(
    exact: str,
    replacement: str,
    expected_error: str,
) -> None:
    text, rows, producers = _inputs()
    mutated = _replace_in_named_step(
        text,
        validator.RESEARCH_PREFLIGHT_STEP_NAME,
        exact,
        replacement,
    )

    errors = validator.validate_workflow_text(mutated, rows, producers)

    assert any(expected_error in error for error in errors)


def test_revenue_projection_candidate_repair_locks_exact2_and_exact15_identity() -> None:
    text, rows, producers = _inputs()
    blocks = validator.workflow_step_blocks(text)
    closure = validator._step_run_body(
        validator._named_step_blocks(
            blocks,
            validator.REVENUE_PROJECTION_CANDIDATE_REPAIR_CLOSURE_STEP_NAME,
        )[0]
    )
    stage = validator._step_run_body(
        validator._named_step_blocks(
            blocks,
            validator.REVENUE_PROJECTION_CANDIDATE_REPAIR_STAGE_STEP_NAME,
        )[0]
    )
    commit = validator._step_run_body(
        validator._named_step_blocks(
            blocks,
            validator.REVENUE_PROJECTION_CANDIDATE_REPAIR_COMMIT_STEP_NAME,
        )[0]
    )
    assert closure is not None and stage is not None and commit is not None
    assert validator._shell_array_values(
        closure, "REVENUE_CANDIDATE_REPAIR_PATHS"
    ) == validator.REVENUE_PROJECTION_CANDIDATE_REPAIR_PATHS
    assert validator._shell_array_values(
        closure, "REVENUE_CANDIDATE_REPAIR_UNCHANGED_PATHS"
    ) == validator.REVENUE_PROJECTION_CANDIDATE_REPAIR_UNCHANGED_PATHS
    assert validator._shell_array_values(
        commit, "REVENUE_CANDIDATE_REPAIR_UNCHANGED_PATHS"
    ) == validator.REVENUE_PROJECTION_CANDIDATE_REPAIR_UNCHANGED_PATHS
    for body in (closure, stage, commit):
        assert validator.REVENUE_PROJECTION_CANDIDATE_REPAIR_EXPECTED_BYTES in body
        assert validator.REVENUE_PROJECTION_CANDIDATE_REPAIR_EXPECTED_SHA256 in body
    assert validator.REVENUE_PROJECTION_CANDIDATE_REPAIR_BASE_COMMIT in closure
    assert 'git merge-base --is-ancestor "$REVENUE_CANDIDATE_REPAIR_BASE_COMMIT" HEAD' in closure
    assert validator.REVENUE_PROJECTION_CANDIDATE_REPAIR_LITERAL_GIT_ADD in stage
    assert 'git add -- "${REVENUE_CANDIDATE_REPAIR_PATHS[@]}"' not in stage
    rebaseline_stage = validator._step_run_body(
        validator._named_step_blocks(
            blocks,
            validator.REVENUE_PROJECTION_REBASELINE_STAGE_STEP_NAME,
        )[0]
    )
    assert rebaseline_stage is not None
    assert validator.REVENUE_PROJECTION_REBASELINE_LITERAL_GIT_ADD in rebaseline_stage
    assert 'git add -- "${REVENUE_REBASELINE_ALLOWED_PATHS[@]}"' not in rebaseline_stage
    assert validator.validate_workflow_text(text, rows, producers) == []


@pytest.mark.parametrize(
    "token",
    (
        validator.REVENUE_PROJECTION_CANDIDATE_REPAIR_EXPECTED_BYTES,
        validator.REVENUE_PROJECTION_CANDIDATE_REPAIR_EXPECTED_SHA256,
        validator.REVENUE_PROJECTION_CANDIDATE_REPAIR_BASE_COMMIT,
        validator.REVENUE_PROJECTION_CANDIDATE_REPAIR_UNCHANGED_PATHS[0],
    ),
)
def test_revenue_projection_candidate_repair_rejects_identity_contract_drift(
    token: str,
) -> None:
    text, rows, producers = _inputs()
    closure_name = validator.REVENUE_PROJECTION_CANDIDATE_REPAIR_CLOSURE_STEP_NAME
    mutated = _replace_in_named_step(text, closure_name, token, token + ".drift")

    errors = validator.validate_workflow_text(mutated, rows, producers)

    assert any(
        "candidate repair" in error and (
            "run body drifted" in error
            or "closure is incomplete" in error
            or "preserve the other exact15" in error
        )
        for error in errors
    )


@pytest.mark.parametrize(
    ("step_name", "exact", "replacement"),
    (
        (
            validator.REVENUE_PROJECTION_CANDIDATE_REPAIR_STAGE_STEP_NAME,
            validator.REVENUE_PROJECTION_CANDIDATE_REPAIR_LITERAL_GIT_ADD,
            'git add -- "${REVENUE_CANDIDATE_REPAIR_PATHS[@]}"',
        ),
        (
            validator.REVENUE_PROJECTION_REBASELINE_STAGE_STEP_NAME,
            validator.REVENUE_PROJECTION_REBASELINE_LITERAL_GIT_ADD,
            'git add -- "${REVENUE_REBASELINE_ALLOWED_PATHS[@]}"',
        ),
    ),
)
def test_revenue_projection_protected_staging_rejects_variable_pathspec(
    step_name: str,
    exact: str,
    replacement: str,
) -> None:
    text, rows, producers = _inputs()
    raw_exact = "          " + exact.replace("\n", "\n          ")
    raw_replacement = "          " + replacement.replace("\n", "\n          ")
    mutated = _replace_in_named_step(
        text,
        step_name,
        raw_exact,
        raw_replacement,
    )

    errors = validator.validate_workflow_text(mutated, rows, producers)

    assert any("array-expanded git add" in error for error in errors)


@pytest.mark.parametrize(
    ("step_name", "old_condition", "new_condition"),
    (
        (
            validator.REVENUE_BUILD_STEP_NAME,
            validator.REVENUE_BUILD_STEP_IF,
            validator.REVENUE_BUILD_STEP_IF.replace(
                " && github.event.inputs."
                "run_revenue_unreacted_range_source_snapshot_projection_candidate_repair_only "
                "!= 'true'",
                "",
            ),
        ),
        (
            validator.PUBLISH_STEP_NAME,
            validator.PUBLISH_STEP_IF,
            validator.PUBLISH_STEP_IF.replace(
                " && github.event.inputs."
                "run_revenue_unreacted_range_source_snapshot_projection_candidate_repair_only "
                "!= 'true'",
                "",
            ),
        ),
    ),
)
def test_revenue_projection_candidate_repair_cannot_activate_normal_paths(
    step_name: str,
    old_condition: str,
    new_condition: str,
) -> None:
    text, rows, producers = _inputs()
    assert new_condition != old_condition
    mutated = _replace_in_named_step(text, step_name, old_condition, new_condition)

    errors = validator.validate_workflow_text(mutated, rows, producers)

    assert any("fail-closed if condition" in error for error in errors)


def test_revenue_projection_rebaseline_stage_rejects_wrong_type() -> None:
    text, rows, producers = _inputs()
    block = (
        "      run_revenue_unreacted_range_source_snapshot_projection_rebaseline_only:\n"
        '        description: "Build only the branch-scoped immutable v1 archive and v2 source snapshot projection candidate"\n'
        "        required: false\n"
        "        default: false\n"
        "        type: boolean"
    )
    assert block in text
    mutated = text.replace(block, block.replace("type: boolean", "type: string"), 1)

    errors = validator.validate_workflow_text(mutated, rows, producers)

    assert any("must use workflow_dispatch type boolean" in error for error in errors)


def test_revenue_projection_rebaseline_stage_rejects_extra_command() -> None:
    text, rows, producers = _inputs()
    command = f"          {validator.REVENUE_PROJECTION_REBASELINE_BUILD_COMMAND}\n"
    assert command in text
    mutated = text.replace(
        command,
        command + "          python scripts/unregistered_rebaseline_command.py\n",
        1,
    )

    errors = validator.validate_workflow_text(mutated, rows, producers)

    assert any(
        "unconditional single-command fail-closed step" in error
        for error in errors
    )


def test_revenue_projection_rebaseline_stage_requires_audit_build_then_validation() -> None:
    text, rows, producers = _inputs()
    build_command, validate_command = (
        validator.REVENUE_PROJECTION_REBASELINE_AUDIT_COMMANDS
    )
    step_contracts = validator.REVENUE_PROJECTION_REBASELINE_COMMAND_STEPS[-2:]
    for step_name, expected_command in step_contracts:
        exact = (
            f"      - name: {step_name}\n"
            f"        if: {validator.REVENUE_PROJECTION_REBASELINE_STEP_IF}\n"
            "        run: |\n"
            f"          {expected_command}\n"
        )
        assert exact in text
        mutated = text.replace(f"          {expected_command}\n", "", 1)
        errors = validator.validate_workflow_text(mutated, rows, producers)
        assert any(
            f"{step_name} must be an unconditional single-command" in error
            for error in errors
        )

    mutated = text.replace(f"          {build_command}\n", "          __AUDIT_SWAP__\n", 1)
    mutated = mutated.replace(
        f"          {validate_command}\n",
        f"          {build_command}\n",
        1,
    ).replace("          __AUDIT_SWAP__\n", f"          {validate_command}\n", 1)
    errors = validator.validate_workflow_text(mutated, rows, producers)
    assert any(
        "unconditional single-command fail-closed step" in error
        for error in errors
    )


def test_revenue_projection_rebaseline_rejects_set_plus_e_before_validator() -> None:
    text, rows, producers = _inputs()
    step_name, command = validator.REVENUE_PROJECTION_REBASELINE_COMMAND_STEPS[1]
    exact = (
        f"      - name: {step_name}\n"
        f"        if: {validator.REVENUE_PROJECTION_REBASELINE_STEP_IF}\n"
        "        run: |\n"
        f"          {command}\n"
    )
    assert exact in text
    mutated = text.replace(
        exact,
        exact.replace("        run: |\n", "        run: |\n          set +e\n"),
        1,
    )

    errors = validator.validate_workflow_text(mutated, rows, producers)

    assert any(
        f"{step_name} must be an unconditional single-command" in error
        for error in errors
    )


def test_revenue_projection_rebaseline_rejects_control_wrapped_commands() -> None:
    text, rows, producers = _inputs()
    mutated = text
    for _step_name, command in validator.REVENUE_PROJECTION_REBASELINE_COMMAND_STEPS:
        exact = f"          {command}\n"
        assert exact in mutated
        mutated = mutated.replace(
            exact,
            "          if false; then\n"
            f"            {command}\n"
            "          fi\n",
            1,
        )

    errors = validator.validate_workflow_text(mutated, rows, producers)

    assert sum(
        "unconditional single-command fail-closed step" in error for error in errors
    ) == len(validator.REVENUE_PROJECTION_REBASELINE_COMMAND_STEPS)


def test_revenue_rebaseline_preflight_rejects_control_wrapper() -> None:
    text, rows, producers = _inputs()
    guard = (
        '          if [[ "$REVENUE_SOURCE_PROJECTION_REBASELINE_ONLY" == "true" && '
        '"$REVENUE_RESEARCH_ENABLED" != "true" ]]; then\n'
    )
    validator_command = "          python scripts/validate_apps_script_workflow_triggers.py\n"
    assert guard in text
    assert validator_command in text
    mutated = text.replace(guard, "          if false; then\n" + guard, 1).replace(
        validator_command,
        "          fi\n" + validator_command,
        1,
    )

    errors = validator.validate_workflow_text(mutated, rows, producers)

    assert any("preflight run body must retain its exact" in error for error in errors)


def test_revenue_projection_rebaseline_stage_rejects_independent_selection() -> None:
    text, rows, producers = _inputs()
    marker = "      MODEL_RESEARCH_SELECTED: ${{ "
    mutated = text.replace(
        marker,
        marker
        + "github.event.inputs."
        + validator.REVENUE_PROJECTION_REBASELINE_STAGE_INPUT
        + " == 'true' || ",
        1,
    )

    errors = validator.validate_workflow_text(mutated, rows, producers)

    assert any("instead of selecting research independently" in error for error in errors)


def test_revenue_projection_rebaseline_stage_requires_all_dispatch_guards() -> None:
    text, rows, producers = _inputs()
    guards = {
        "primary revenue": (
            '          if [[ "$REVENUE_SOURCE_PROJECTION_REBASELINE_ONLY" == "true" && '
            '"$REVENUE_RESEARCH_ENABLED" != "true" ]]; then\n'
        ),
        "mutually exclusive": (
            '          if [[ "$REVENUE_SOURCE_PROJECTION_REBASELINE_ONLY" == "true" && '
            '( "$REVENUE_FORWARD_HOLDOUT_ONLY" == "true" || '
            '"$REVENUE_SOURCE_PROJECTION_CHAIN_ONLY" == "true" || '
            '"$REVENUE_SOURCE_PROJECTION_CANDIDATE_REPAIR_ONLY" == "true" || '
            '"$REVENUE_SOURCE_PROJECTION_SUPERSEDE_ONLY" == "true" ) ]]; then\n'
        ),
        "every other research input": (
            '          if [[ "$REVENUE_SOURCE_PROJECTION_REBASELINE_ONLY" == "true" && '
            '"$REVENUE_REBASELINE_OTHER_RESEARCH_SELECTED" == "true" ]]; then\n'
        ),
        "non-main branch": (
            '          if [[ "$REVENUE_SOURCE_PROJECTION_REBASELINE_ONLY" == "true" && '
            '( "$REVENUE_REBASELINE_REF_TYPE" != "branch" || '
            '"$TARGET_BRANCH" == "main" ) ]]; then\n'
        ),
    }
    for expected_error, guard in guards.items():
        assert guard in text
        mutated = text.replace(guard, "", 1)
        errors = validator.validate_workflow_text(mutated, rows, producers)
        assert any(expected_error in error for error in errors)


def test_revenue_projection_rebaseline_stage_rejects_companion_input_drift() -> None:
    text, rows, producers = _inputs()
    input_name = validator.REVENUE_PROJECTION_REBASELINE_FORBIDDEN_COMPANION_INPUTS[0]
    token = f"github.event.inputs.{input_name} == 'true' || "
    companion_line = next(
        line
        for line in text.splitlines()
        if "REVENUE_REBASELINE_OTHER_RESEARCH_SELECTED:" in line
    )
    assert token in companion_line
    mutated = text.replace(companion_line, companion_line.replace(token, "", 1), 1)

    errors = validator.validate_workflow_text(mutated, rows, producers)

    assert any("companion-input guard drift" in error for error in errors)


def test_revenue_projection_rebaseline_stage_guards_exact_artifact_sets() -> None:
    text, rows, producers = _inputs()
    assert len(validator.REVENUE_PROJECTION_REBASELINE_ALLOWED_PATHS) == 17
    candidate_path = validator.REVENUE_PROJECTION_REBASELINE_ALLOWED_PATHS[0]
    replacement_path = candidate_path + ".unauthorized"
    closure_index = text.index(
        f"      - name: {validator.REVENUE_PROJECTION_REBASELINE_CLOSURE_STEP_NAME}\n"
    )
    path_index = text.index(candidate_path, closure_index)
    mutated = text[:path_index] + replacement_path + text[path_index + len(candidate_path) :]

    errors = validator.validate_workflow_text(mutated, rows, producers)

    assert any("exact seventeen changed or untracked artifact paths" in error for error in errors)


def test_revenue_projection_rebaseline_guards_all_four_independence_audit_mirrors() -> None:
    text, rows, producers = _inputs()
    audit_paths = (
        "output/latest/model_data_independence_audit_latest.csv",
        "output/latest/model_data_independence_audit_latest.md",
        "docs/latest/model_data_independence_audit_latest.csv",
        "docs/latest/model_data_independence_audit_latest.md",
    )
    assert validator.REVENUE_PROJECTION_REBASELINE_ALLOWED_PATHS[-4:] == audit_paths
    path = audit_paths[0]
    expected_count = dict(
        zip(
            validator.REVENUE_PROJECTION_REBASELINE_ALLOWED_PATHS,
            validator.REVENUE_PROJECTION_REBASELINE_EXPECTED_PATH_OCCURRENCES,
            strict=True,
        )
    )
    for audit_path in audit_paths:
        assert text.count(audit_path) == expected_count[audit_path]

    build_mutation = _replace_in_named_step(
        text,
        validator.REVENUE_PROJECTION_REBASELINE_CLOSURE_STEP_NAME,
        path,
        path + ".unauthorized",
    )
    build_errors = validator.validate_workflow_text(build_mutation, rows, producers)
    assert any(
        "exact seventeen changed or untracked artifact paths" in error
        for error in build_errors
    )

    stage_mutation = _replace_in_named_step(
        text,
        validator.REVENUE_PROJECTION_REBASELINE_STAGE_STEP_NAME,
        path,
        path + ".unauthorized",
    )
    stage_errors = validator.validate_workflow_text(stage_mutation, rows, producers)
    assert any(
        "only its exact seventeen artifact paths" in error
        for error in stage_errors
    )

    commit_mutation = _replace_in_named_step(
        text,
        validator.REVENUE_PROJECTION_REBASELINE_COMMIT_STEP_NAME,
        path,
        path + ".unauthorized",
    )
    commit_errors = validator.validate_workflow_text(commit_mutation, rows, producers)
    assert any(
        "dedicated commit must contain only its exact seventeen artifact paths" in error
        for error in commit_errors
    )


def test_revenue_projection_rebaseline_stage_requires_worktree_side_effect_guard() -> None:
    text, rows, producers = _inputs()
    status_command = "git status --porcelain=v1 --untracked-files=all"
    assert status_command in text
    mutated = text.replace(status_command, "git status --short", 1)

    errors = validator.validate_workflow_text(mutated, rows, producers)

    assert any("git status --porcelain=v1 --untracked-files=all" in error for error in errors)


def test_revenue_projection_rebaseline_commit_requires_pre_stage_worktree_guard() -> None:
    text, rows, producers = _inputs()
    status_command = "git status --porcelain=v1 --untracked-files=all"
    stage_marker = (
        f"      - name: {validator.REVENUE_PROJECTION_REBASELINE_STAGE_STEP_NAME}\n"
    )
    commit_marker = (
        f"      - name: {validator.REVENUE_PROJECTION_REBASELINE_COMMIT_STEP_NAME}\n"
    )
    stage_index = text.index(stage_marker)
    commit_index = text.index(commit_marker)
    status_index = text.index(status_command, stage_index, commit_index)
    mutated = text[:status_index] + "git status --short" + text[
        status_index + len(status_command) :
    ]

    errors = validator.validate_workflow_text(mutated, rows, producers)

    assert any(
        "staging step lacks fail-closed working/index identity closure" in error
        and status_command in error
        for error in errors
    )


def test_revenue_projection_rebaseline_stage_requires_v1_bytes_and_sha_guard() -> None:
    text, rows, producers = _inputs()
    sha_guard = validator.REVENUE_PROJECTION_REBASELINE_V1_IDENTITIES[0][2]
    assert sha_guard in text
    mutated = text.replace(sha_guard, "0" * 64, 1)

    errors = validator.validate_workflow_text(mutated, rows, producers)

    assert any("immutable v1 precheck run body drifted" in error for error in errors)


def test_revenue_projection_rebaseline_commit_rejects_wildcard_or_failure_masking() -> None:
    text, rows, producers = _inputs()
    exact = "          " + validator.REVENUE_PROJECTION_REBASELINE_LITERAL_GIT_ADD.replace(
        "\n", "\n          "
    )
    mutated = _replace_in_named_step(
        text,
        validator.REVENUE_PROJECTION_REBASELINE_STAGE_STEP_NAME,
        exact,
        "          git add output/history/research/revenue_unreacted_range_* || true",
    )

    errors = validator.validate_workflow_text(mutated, rows, producers)

    assert any("working/index identity closure" in error for error in errors)


def test_revenue_rebaseline_rejects_corruption_after_final_validator() -> None:
    text, rows, producers = _inputs()
    step_name, command = validator.REVENUE_PROJECTION_REBASELINE_COMMAND_STEPS[-1]
    exact = (
        f"      - name: {step_name}\n"
        f"        if: {validator.REVENUE_PROJECTION_REBASELINE_STEP_IF}\n"
        "        run: |\n"
        f"          {command}\n"
    )
    corrupt_path = validator.REVENUE_PROJECTION_REBASELINE_ALLOWED_PATHS[3]
    assert exact in text
    mutated = text.replace(
        exact,
        exact + f"          printf corrupt >> {corrupt_path}\n",
        1,
    )

    errors = validator.validate_workflow_text(mutated, rows, producers)

    assert any("unconditional single-command fail-closed step" in error for error in errors)
    assert any("exact17 path occurrence drift" in error for error in errors)


def test_post_run_validation_rejects_artifact_and_identity_forgery() -> None:
    text, rows, producers = _inputs()
    sentinel = f"printf 'pass\\n' > \"{validator.POST_RUN_SENTINEL}\""
    corrupt_path = validator.REVENUE_PROJECTION_REBASELINE_ALLOWED_PATHS[3]
    forged_identity = validator.REVENUE_PROJECTION_REBASELINE_IDENTITY_FILE
    forged_commands = (
        f"printf corrupt >> {corrupt_path}\n"
        f"          printf 'forged\\t0\\t0\\n' > \"{forged_identity}\"\n"
        "          "
        + sentinel
    )
    mutated = _replace_in_named_step(
        text,
        validator.POST_RUN_STEP_NAME,
        sentinel,
        forged_commands,
    )

    errors = validator.validate_workflow_text(mutated, rows, producers)

    assert any("post-run research validation run body" in error for error in errors)


def test_post_run_sentinel_write_and_closure_check_are_both_required() -> None:
    text, rows, producers = _inputs()
    sentinel_write = f"printf 'pass\\n' > \"{validator.POST_RUN_SENTINEL}\""
    without_write = _replace_in_named_step(
        text,
        validator.POST_RUN_STEP_NAME,
        sentinel_write,
        "",
    )
    write_errors = validator.validate_workflow_text(without_write, rows, producers)
    assert any("post-run research validation run body" in error for error in write_errors)
    assert any("sentinel must be written once and consumed once" in error for error in write_errors)

    sentinel_check = f'test "$(cat "{validator.POST_RUN_SENTINEL}")" = "pass"'
    without_check = _replace_in_named_step(
        text,
        validator.REVENUE_PROJECTION_REBASELINE_CLOSURE_STEP_NAME,
        sentinel_check,
        "true",
    )
    check_errors = validator.validate_workflow_text(without_check, rows, producers)
    assert any("exact17 validated identity closure run body drifted" in error for error in check_errors)
    assert any("sentinel must be written once and consumed once" in error for error in check_errors)


@pytest.mark.parametrize(
    "following_step",
    (
        validator.REVENUE_PROJECTION_REBASELINE_CLOSURE_STEP_NAME,
        validator.REVENUE_PROJECTION_REBASELINE_STAGE_STEP_NAME,
        validator.REVENUE_PROJECTION_REBASELINE_COMMIT_STEP_NAME,
    ),
)
def test_revenue_rebaseline_final_chain_rejects_any_interposed_step(
    following_step: str,
) -> None:
    text, rows, producers = _inputs()
    marker = f"      - name: {following_step}\n"
    interposed = (
        "      - name: Interposed writable rebaseline step\n"
        "        run: |\n"
        "          echo unauthorized\n\n"
    )
    mutated = text.replace(marker, interposed + marker, 1)

    errors = validator.validate_workflow_text(mutated, rows, producers)

    assert any(
        "post-run validators, supersede exact75 closure chain, repair exact2 closure chain, rebaseline exact17"
        in error
        and "consecutive in exact order" in error
        for error in errors
    )


def test_generic_publish_must_skip_rebaseline_mode() -> None:
    text, rows, producers = _inputs()
    unsafe_if = "${{ env.ANY_RESEARCH_SELECTED == 'true' }}"
    assert validator.PUBLISH_STEP_IF in text
    mutated = text.replace(validator.PUBLISH_STEP_IF, unsafe_if, 1)

    errors = validator.validate_workflow_text(mutated, rows, producers)

    assert any("research publish step must retain its exact fail-closed if" in error for error in errors)


def test_revenue_rebaseline_pre_commit_head_is_captured_in_dedicated_step() -> None:
    text, _rows, _producers = _inputs()
    commit_marker = (
        f"      - name: {validator.REVENUE_PROJECTION_REBASELINE_COMMIT_STEP_NAME}\n"
    )
    generic_marker = f"      - name: {validator.PUBLISH_STEP_NAME}\n"
    stage_marker = f"      - name: {validator.REVENUE_PROJECTION_REBASELINE_STAGE_STEP_NAME}\n"
    commit_start = text.index(commit_marker)
    commit_end = text.index(generic_marker, commit_start)
    stage_start = text.index(stage_marker)
    dedicated_body = text[commit_start:commit_end]
    stage_body = text[stage_start:commit_start]
    pre_head = 'REVENUE_REBASELINE_PRE_COMMIT_HEAD="$(git rev-parse HEAD)"'
    assert pre_head in dedicated_body
    assert pre_head not in stage_body
    assert dedicated_body.index(pre_head) < dedicated_body.index(
        validator.REVENUE_REBASELINE_COMMIT
    )


@pytest.mark.parametrize(
    ("exact", "replacement"),
    (
        ("if ! git diff --quiet; then", "if ! true; then"),
        ("git ls-files --others --exclude-standard", "printf ''"),
        (
            'REVENUE_REBASELINE_PRE_COMMIT_HEAD="$(git rev-parse HEAD)"',
            'REVENUE_REBASELINE_PRE_COMMIT_HEAD="forged"',
        ),
        (
            'staged_sha256="$(git show ":$path" | sha256sum | cut -d \' \' -f1)"',
            'staged_sha256="$validated_sha256"',
        ),
        (
            'REVENUE_REBASELINE_POST_COMMIT_HEAD="$(git rev-parse HEAD)"',
            'REVENUE_REBASELINE_POST_COMMIT_HEAD="$REVENUE_REBASELINE_PRE_COMMIT_HEAD"',
        ),
        (
            'git rev-parse "$REVENUE_REBASELINE_POST_COMMIT_HEAD^"',
            'printf %s "$REVENUE_REBASELINE_PRE_COMMIT_HEAD"',
        ),
        ("git diff --name-only --no-renames", "git diff --name-only"),
        (
            'committed_bytes="$(git cat-file -s "$REVENUE_REBASELINE_POST_COMMIT_HEAD:$path")"',
            'committed_bytes="$validated_bytes"',
        ),
        (
            'committed_sha256="$(git show "$REVENUE_REBASELINE_POST_COMMIT_HEAD:$path" | sha256sum | cut -d \' \' -f1)"',
            'committed_sha256="$validated_sha256"',
        ),
        (
            'if [[ -n "$(git status --porcelain=v1 --untracked-files=all)" ]]; then',
            "if false; then",
        ),
    ),
)
def test_revenue_rebaseline_dedicated_commit_rejects_removed_identity_guard(
    exact: str,
    replacement: str,
) -> None:
    text, rows, producers = _inputs()
    mutated = _replace_in_named_step(
        text,
        validator.REVENUE_PROJECTION_REBASELINE_COMMIT_STEP_NAME,
        exact,
        replacement,
    )

    errors = validator.validate_workflow_text(mutated, rows, producers)

    assert any("dedicated commit run body drifted" in error for error in errors)


def test_revenue_rebaseline_dedicated_commit_rejects_dynamic_corrupt_and_stage() -> None:
    text, rows, producers = _inputs()
    corrupt_path = validator.REVENUE_PROJECTION_REBASELINE_ALLOWED_PATHS[3]
    mutation = (
        f"printf corrupt >> {corrupt_path}\n"
        f"          git add -- {corrupt_path}\n"
        "          "
        + validator.REVENUE_REBASELINE_COMMIT
    )
    mutated = _replace_in_named_step(
        text,
        validator.REVENUE_PROJECTION_REBASELINE_COMMIT_STEP_NAME,
        validator.REVENUE_REBASELINE_COMMIT,
        mutation,
    )

    errors = validator.validate_workflow_text(mutated, rows, producers)

    assert any("dedicated commit run body drifted" in error for error in errors)
    assert any("must not modify or stage after index identity validation" in error for error in errors)


@pytest.mark.parametrize(
    ("exact", "replacement", "expected_error"),
    (
        (
            validator.REVENUE_REBASELINE_COMMIT,
            validator.REVENUE_REBASELINE_COMMIT + " || true",
            "commit commands must be exact",
        ),
        (
            validator.REVENUE_REBASELINE_COMMIT,
            'git commit -am "Update revenue projection v2 rebaseline candidate artifacts"',
            "commit commands must be exact",
        ),
        (
            validator.PUBLISH_PUSH,
            'git push --force origin "HEAD:$TARGET_BRANCH"',
            "exactly four direct fail-closed pushes",
        ),
        (
            validator.PUBLISH_PUSH,
            validator.PUBLISH_PUSH + "\n          echo writable-after-push",
            "dedicated direct push must be the final command",
        ),
    ),
)
def test_revenue_rebaseline_dedicated_publish_rejects_masking_or_post_push_work(
    exact: str,
    replacement: str,
    expected_error: str,
) -> None:
    text, rows, producers = _inputs()
    mutated = _replace_in_named_step(
        text,
        validator.REVENUE_PROJECTION_REBASELINE_COMMIT_STEP_NAME,
        exact,
        replacement,
    )

    errors = validator.validate_workflow_text(mutated, rows, producers)

    assert any("dedicated commit run body drifted" in error for error in errors)
    assert any(expected_error in error for error in errors)


def test_revenue_rebaseline_identity_closure_must_follow_validators_contiguously() -> None:
    text, rows, producers = _inputs()
    closure_marker = (
        f"      - name: {validator.REVENUE_PROJECTION_REBASELINE_CLOSURE_STEP_NAME}\n"
    )
    assert closure_marker in text
    unauthorized_step = (
        "      - name: Corrupt validated revenue candidate\n"
        f"        if: {validator.REVENUE_PROJECTION_REBASELINE_STEP_IF}\n"
        "        run: |\n"
        "          printf corrupt >> output/history/research/"
        "revenue_unreacted_range_source_snapshot_projection_manifest_v2_20260822.csv\n\n"
    )
    mutated = text.replace(closure_marker, unauthorized_step + closure_marker, 1)

    errors = validator.validate_workflow_text(mutated, rows, producers)

    assert any(
        "post-run validators, supersede exact75 closure chain, repair exact2 closure chain, rebaseline exact17"
        in error
        and "consecutive in exact order" in error
        for error in errors
    )


@pytest.mark.parametrize(
    "identity_line",
    (
        '            working_sha256="$(sha256sum "$path" | cut -d \' \' -f1)"\n',
        '            staged_bytes="$(git cat-file -s ":$path")"\n',
        '            staged_sha256="$(git show ":$path" | sha256sum | cut -d \' \' -f1)"\n',
    ),
)
def test_revenue_rebaseline_stage_requires_working_and_index_identity(
    identity_line: str,
) -> None:
    text, rows, producers = _inputs()
    exact = identity_line
    assert exact in text
    mutated = _replace_in_named_step(
        text,
        validator.REVENUE_PROJECTION_REBASELINE_STAGE_STEP_NAME,
        exact,
        "",
    )

    errors = validator.validate_workflow_text(mutated, rows, producers)

    assert any("working/index identity" in error for error in errors)


def test_revenue_rebaseline_stage_must_immediately_precede_commit() -> None:
    text, rows, producers = _inputs()
    commit_marker = (
        f"      - name: {validator.REVENUE_PROJECTION_REBASELINE_COMMIT_STEP_NAME}\n"
    )
    assert commit_marker in text
    mutated = text.replace(
        commit_marker,
        "      - name: Interpose after validated staging\n"
        "        run: |\n"
        "          echo unexpected\n\n"
        + commit_marker,
        1,
    )

    errors = validator.validate_workflow_text(mutated, rows, producers)

    assert any(
        "post-run validators, supersede exact75 closure chain, repair exact2 closure chain, rebaseline exact17"
        in error
        and "consecutive in exact order" in error
        for error in errors
    )


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
