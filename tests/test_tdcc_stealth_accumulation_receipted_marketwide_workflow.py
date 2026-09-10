from dataclasses import replace
from pathlib import Path

import pytest

from scripts import detect_daily_model_pr_validation_scope as scope
from scripts import validate_apps_script_workflow_triggers as apps
from scripts import validate_model_research_workflow_isolation as workflow
from scripts import validate_repo_production_inventory as inventory


ROOT = Path(__file__).resolve().parents[1]
PATH = workflow.RECEIPTED_REPLAY_WORKFLOW_PATH
MODEL = workflow.RECEIPTED_REPLAY_MODEL_ID


def workflow_errors(text):
    return workflow.validate_workflow_text(
        text, workflow.load_registry(), workflow.load_model_owned_producers(),
        workflow_path=PATH,
    )


def test_receipted_workflow_exact_contract():
    text = (ROOT / PATH).read_text(encoding="utf-8")
    assert workflow_errors(text) == []
    assert workflow.workflow_input_defaults(text) == {workflow.RECEIPTED_REPLAY_INPUT: "false"}
    assert len(workflow.RECEIPTED_REPLAY_ARTIFACTS) == 9
    assert tuple(line.strip() for line in text.splitlines() if line.strip().startswith("git add")) == workflow.RECEIPTED_REPLAY_STAGE_COMMANDS
    assert "schedule:" not in text
    assert "fetch-depth: 0" in text
    assert workflow.RECEIPTED_REPLAY_SOURCE_REF == "40cee0405390a9ccaf3a1ad0778aa1e680ab8252"


@pytest.mark.parametrize("command", workflow.RECEIPTED_REPLAY_STAGE_COMMANDS)
def test_receipted_workflow_rejects_each_missing_artifact(command):
    text = (ROOT / PATH).read_text(encoding="utf-8")
    assert workflow_errors(text.replace(command, "echo missing-artifact", 1))


@pytest.mark.parametrize("old,new", [
    ("default: false", "default: true"),
    ("contents: write", "contents: read"),
    ("fetch-depth: 0", "fetch-depth: 1"),
    (workflow.RECEIPTED_REPLAY_FETCH_COMMAND, "git fetch --no-tags origin main"),
    (workflow.RECEIPTED_REPLAY_PRODUCER_COMMAND, workflow.RECEIPTED_REPLAY_PRODUCER_COMMAND + " || true"),
    (workflow.RECEIPTED_REPLAY_VALIDATOR_COMMAND, "echo no-validator"),
    (workflow.RECEIPTED_REPLAY_STAGE_COMMANDS[0], "git add output/research/tdcc_stealth_accumulation/"),
    (workflow.RECEIPTED_REPLAY_STAGE_COMMANDS[0], "git add output/latest/model_operation_readiness_latest.csv"),
    (workflow.RECEIPTED_REPLAY_VALIDATOR_COMMAND, workflow.MODEL_DATA_AUDIT_BUILD_COMMAND + "\n          " + workflow.RECEIPTED_REPLAY_VALIDATOR_COMMAND),
    ("on:\n  workflow_dispatch:", "on:\n  schedule:\n    - cron: '0 1 * * *'\n  workflow_dispatch:"),
    ("No research selected; no repository checkout or artifact writes.", "No research selected"),
])
def test_receipted_workflow_fail_closed_mutations(old, new):
    text = (ROOT / PATH).read_text(encoding="utf-8")
    assert old in text
    assert workflow_errors(text.replace(old, new, 1))


def test_receipted_registry_cannot_move_or_enable_formal_sync():
    rows = workflow.load_registry()
    index = next(i for i, row in enumerate(rows) if row.model_id == MODEL)
    for replacement in (
        replace(rows[index], workflow_path=workflow.LEGACY_WORKFLOW_PATH),
        replace(rows[index], latest_stage_glob="output/research/*"),
    ):
        changed = rows.copy()
        changed[index] = replacement
        assert workflow.validate_registry_contract(changed, workflow.load_model_owned_producers())
    assert not rows[index].default_enabled
    assert not rows[index].formal_sync_allowed


def test_receipted_scope_is_research_only_for_exact_paths():
    paths = (
        PATH, f"scripts/build_{MODEL}.py", f"scripts/validate_{MODEL}.py",
        f"tests/test_{MODEL}.py", f"tests/test_{MODEL}_scope_probe.py",
        "tests/test_tdcc_stealth_accumulation_receipted_marketwide_workflow.py",
        f"config/{MODEL}_v1.json",
        "config/tdcc_stealth_accumulation_receipted_marketwide_availability_v1.json",
        *workflow.RECEIPTED_REPLAY_ARTIFACTS,
    )
    for path in paths:
        assert set(scope.domains_for_path(path)) == {scope.RESEARCH_SAFETY_LITE, scope.SHARED_MODEL_RESEARCH}


def test_receipted_inventory_invocations_are_exact_and_no_other_writer(monkeypatch):
    errors = []
    rows = inventory.load_inventory(errors)
    assert errors == []
    expected = {command.split()[1] for command in (*workflow.STATIC_VALIDATOR_COMMANDS, workflow.RECEIPTED_REPLAY_PRODUCER_COMMAND, workflow.RECEIPTED_REPLAY_VALIDATOR_COMMAND, *workflow.READ_ONLY_POST_RUN_COMMANDS)}
    assert inventory.WORKFLOW_EXACT_INVOCATION_ALLOWLIST[PATH] == expected
    assert inventory.WORKFLOW_ALLOWED_OWNERS[PATH] == set()
    assert rows[PATH].allowed_stage_patterns == workflow.RECEIPTED_REPLAY_STAGE_COMMANDS
    inventory.validate_workflow_invocations(rows, {PATH}, errors)
    assert errors == []
    monkeypatch.setattr(inventory, "workflow_invocations", lambda _: {workflow.MODEL_DATA_AUDIT_BUILD_COMMAND.split()[1]})
    inventory.validate_workflow_invocations(rows, {PATH}, errors)
    assert errors


def test_receipted_dispatch_is_workflow_only():
    registry = apps.load_research_dispatch_registry()
    row = registry[workflow.RECEIPTED_REPLAY_INPUT]
    assert row["workflow_path"] == PATH
    assert row["activation_mode"] == "workflow_only"
    assert apps.research_input_workflow_path(workflow.RECEIPTED_REPLAY_INPUT) == PATH
    bad = {name: dict(value) for name, value in registry.items()}
    bad[workflow.RECEIPTED_REPLAY_INPUT]["activation_mode"] = "required"
    errors = []
    apps.validate_research_dispatch_contract(
        errors, workflow_path=PATH, workflow_input_names={workflow.RECEIPTED_REPLAY_INPUT},
        workflow_input_defaults={workflow.RECEIPTED_REPLAY_INPUT: "false"},
        workflow_input_types={workflow.RECEIPTED_REPLAY_INPUT: "boolean"},
        apps_inputs=set(), guarded_inputs=set(), registry=bad,
    )
    assert errors


def test_receipted_ci_validates_without_running_producer():
    text = workflow.PR_VALIDATION_WORKFLOW.read_text(encoding="utf-8")
    assert workflow.validate_pr_workflow_text(text, workflow.load_registry()) == []
    assert workflow.RECEIPTED_REPLAY_VALIDATOR_COMMAND in text
    assert workflow.RECEIPTED_REPLAY_PRODUCER_COMMAND not in text
    assert f"tests/test_{MODEL}.py" in text
    assert "tests/test_tdcc_stealth_accumulation_receipted_marketwide_workflow.py" in text
    assert "git diff --exit-code -- " + workflow.RECEIPTED_REPLAY_STAGE_GLOB in text


@pytest.mark.parametrize("mutation", ("missing_validator", "missing_tests", "missing_drift_check", "execute_producer"))
def test_receipted_ci_rejects_missing_checks_or_producer_execution(mutation):
    text = workflow.PR_VALIDATION_WORKFLOW.read_text(encoding="utf-8")
    if mutation == "missing_validator":
        text = text.replace(workflow.RECEIPTED_REPLAY_VALIDATOR_COMMAND, "echo skipped")
    elif mutation == "missing_tests":
        text = text.replace("tests/test_tdcc_stealth_accumulation_receipted_marketwide_workflow.py", "")
    elif mutation == "missing_drift_check":
        text = text.replace("git diff --exit-code -- " + workflow.RECEIPTED_REPLAY_STAGE_GLOB, "echo skipped")
    else:
        text += "\n          " + workflow.RECEIPTED_REPLAY_PRODUCER_COMMAND + "\n"
    assert workflow.validate_pr_workflow_text(text, workflow.load_registry())


@pytest.mark.parametrize("path", (workflow.LEGACY_WORKFLOW_PATH, workflow.PRICE_PIT_WORKFLOW_PATH, workflow.OPERATION_REPLAY_WORKFLOW_PATH))
def test_receipted_fetch_allowance_does_not_expand_other_workflows(path):
    text = (ROOT / path).read_text(encoding="utf-8")
    sync = 'git pull --ff-only origin "$TARGET_BRANCH"'
    assert sync in text
    changed = text.replace(sync, sync + "\n          " + workflow.RECEIPTED_REPLAY_FETCH_COMMAND)
    assert workflow.validate_workflow_text(changed, workflow.load_registry(), workflow.load_model_owned_producers(), workflow_path=path)
