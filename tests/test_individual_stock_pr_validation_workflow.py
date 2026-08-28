from __future__ import annotations

import subprocess
from pathlib import Path

import pytest

from scripts import detect_individual_stock_pr_scope as scope
from scripts import validate_repo_production_inventory as inventory


ROOT = Path(__file__).resolve().parents[1]
WORKFLOW = ROOT / ".github" / "workflows" / "individual_stock_pr_validation.yml"

PR_404_PATHS = (
    "config/repo_file_lifecycle_inventory.csv",
    "config/repo_production_inventory.csv",
    "docs/individual_stock_tdcc_freshness_contract.md",
    "scripts/build_individual_stock_chatgpt_packets.py",
    "scripts/validate_individual_stock_outputs.py",
    "tests/test_individual_stock_outputs.py",
)

PRODUCTION_ARTIFACT_WRITER_WORKFLOWS = (
    ".github/workflows/current_holdings_pattern.yml",
    ".github/workflows/daily_full_pipeline.yml",
    ".github/workflows/individual_stock_data_refresh.yml",
    ".github/workflows/individual_stock_report.yml",
    ".github/workflows/repair_daily_price_range.yml",
    ".github/workflows/repair_one_daily_price.yml",
    ".github/workflows/repair_recent_daily_price_gaps.yml",
    ".github/workflows/repair_tdcc_monthly_history_gaps.yml",
    ".github/workflows/research_backtest_pipeline.yml",
    ".github/workflows/tdcc_history_backfill.yml",
    ".github/workflows/tdcc_weekly.yml",
    ".github/workflows/volume_v2_advisory_lineage_refresh.yml",
    ".github/workflows/warrant_flow.yml",
)

def workflow_text() -> str:
    return WORKFLOW.read_text(encoding="utf-8")


def pull_request_nested_lines(text: str) -> list[str]:
    lines = text.splitlines()
    start = lines.index("  pull_request:")
    nested: list[str] = []
    for line in lines[start + 1 :]:
        if line and not line.startswith("    "):
            break
        nested.append(line)
    return nested


def test_workflow_creates_the_same_check_for_every_pull_request() -> None:
    text = workflow_text()

    assert "  pull_request:" in text
    assert all(line.strip() != "paths:" for line in pull_request_nested_lines(text))
    assert "  individual-stock-pr-validation:" in text
    assert f"    name: {inventory.PR_SAFE_REGULAR_JOB_NAME_EXPRESSION}" in text
    assert inventory.PR_SAFE_REQUIRED_CHECK_CONTEXT != inventory.PR_SAFE_TARGET_SKIP_CHECK_NAME
    assert inventory.PR_SAFE_REQUIRED_CHECK_CONTEXT in inventory.PR_SAFE_REGULAR_JOB_NAME_EXPRESSION
    assert inventory.PR_SAFE_TARGET_SKIP_CHECK_NAME in inventory.PR_SAFE_REGULAR_JOB_NAME_EXPRESSION
    regular_job = inventory.workflow_job_blocks(text)["individual-stock-pr-validation"]
    assert "    timeout-minutes: 30" in regular_job
    assert "workflow_dispatch:" not in text


def test_pr_404_file_set_is_fully_affected() -> None:
    assert scope.matched_affected_paths(PR_404_PATHS) == sorted(PR_404_PATHS)


def test_normalize_path_preserves_dot_github_exact_match() -> None:
    workflow_path = ".github/workflows/individual_stock_data_refresh.yml"

    assert scope.normalize_path(f"./{workflow_path}") == workflow_path
    assert scope.is_affected_path(workflow_path)


def test_scope_covers_gate_inventories_and_probe_contract_docs() -> None:
    affected = (
        ".github/workflows/individual_stock_data_refresh.yml",
        ".github/workflows/individual_stock_pr_validation.yml",
        "config/repo_file_lifecycle_inventory.csv",
        "config/repo_production_inventory.csv",
        "config/report_artifact_lineage.csv",
        "config/runtime_file_lineage_contract.csv",
        "docs/individual_stock_lifecycle_probe.md",
        "output/history/individual_stock_reports/2330/report.pdf",
        "scripts/detect_individual_stock_pr_scope.py",
        "scripts/individual_tdcc_dataset_consumer.py",
        "scripts/validate_individual_pdf_contract_consumers.py",
        "tests/test_individual_pdf_contract_consumers.py",
        "tests/test_individual_tdcc_dataset_consumer.py",
        "tests/test_individual_stock_pr_validation_workflow.py",
    )
    unrelated = (
        "config/revenue_unreacted_range_promotion_preparation_registry.csv",
        "docs/unrelated_note.md",
        "scripts/" + "build_daily_" + "candidate_model_layer.py",
        "scripts/revenue_unreacted_range_fastpass_probe.py",
        "tests/test_daily_candidate_model_layer.py",
    )

    assert all(scope.is_affected_path(path) for path in affected)
    assert not any(scope.is_affected_path(path) for path in unrelated)


@pytest.mark.parametrize("path", sorted(scope.SHARED_REGISTRY_KEY_FIELDS))
def test_shared_registry_revenue_only_row_change_is_not_individual_affected(
    path: str,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    key_field = scope.SHARED_REGISTRY_KEY_FIELDS[path]
    base = f"{key_field},owner,purpose\nscripts/revenue.py,research_backtest,old\n"
    head = f"{key_field},owner,purpose\nscripts/revenue.py,research_backtest,new\n"
    monkeypatch.setattr(
        scope,
        "_read_git_text",
        lambda revision, _path: base if revision == "base" else head,
    )

    assert not scope.is_affected_changed_path(
        path,
        base_sha="base",
        head_sha="head",
    )


@pytest.mark.parametrize("path", sorted(scope.SHARED_REGISTRY_KEY_FIELDS))
def test_shared_registry_individual_row_change_is_affected(
    path: str,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    key_field = scope.SHARED_REGISTRY_KEY_FIELDS[path]
    base = f"{key_field},owner,purpose\nscripts/revenue.py,research_backtest,same\n"
    head = (
        base
        + "scripts/build_individual_stock_packet.py,individual_stock,packet\n"
    )
    monkeypatch.setattr(
        scope,
        "_read_git_text",
        lambda revision, _path: base if revision == "base" else head,
    )

    assert scope.is_affected_changed_path(
        path,
        base_sha="base",
        head_sha="head",
    )


def test_shared_registry_unreadable_state_fails_closed(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.setattr(
        scope,
        "_read_git_text",
        lambda *_args: (_ for _ in ()).throw(
            scope.RegistryScopeError("missing blob")
        ),
    )

    assert scope.is_affected_changed_path(
        "config/repo_production_inventory.csv",
        base_sha="base",
        head_sha="head",
    )


def test_shared_registry_duplicate_key_fails_closed(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    base = "path,owner,purpose\nscripts/revenue.py,research_backtest,revenue\n"
    head = base + "scripts/revenue.py,research_backtest,duplicate\n"
    monkeypatch.setattr(
        scope,
        "_read_git_text",
        lambda revision, _path: base if revision == "base" else head,
    )

    assert scope.is_affected_changed_path(
        "config/repo_production_inventory.csv",
        base_sha="base",
        head_sha="head",
    )


def test_scope_covers_every_registered_production_artifact_writer() -> None:
    assert all(
        scope.is_affected_path(path)
        for path in PRODUCTION_ARTIFACT_WRITER_WORKFLOWS
    )


def test_volume_v2_advisory_lineage_refresh_writer_is_affected() -> None:
    workflow_path = ".github/workflows/volume_v2_advisory_lineage_refresh.yml"

    assert workflow_path in scope.AFFECTED_EXACT_PATHS
    assert scope.matched_affected_paths([workflow_path]) == [workflow_path]


def test_individual_stock_history_root_is_affected() -> None:
    assert scope.is_affected_path(
        "output/history/individual_stock_reports/2330/20260717.json"
    )


def test_individual_tdcc_dataset_consumer_is_affected() -> None:
    assert scope.is_affected_path("scripts/individual_tdcc_dataset_consumer.py")
    assert scope.is_affected_path("tests/test_individual_tdcc_dataset_consumer.py")


def test_workflow_contains_required_affected_validation_commands() -> None:
    text = workflow_text()
    assert "tests/test_individual_tdcc_dataset_consumer.py" in text
    commands = (
        "git diff --check",
        "python -m pip install --disable-pip-version-check pandas requests",
        "python scripts/validate_repo_file_lifecycle_inventory.py",
        "python scripts/validate_repo_production_inventory.py",
        "python scripts/validate_individual_pdf_contract_consumers.py",
        "python -m pytest tests/test_repo_production_inventory.py -q",
        "python -m pytest tests/test_individual_stock_outputs.py -q",
        "python -m pytest tests/test_individual_stock_pr_validation_workflow.py -q",
    )

    for command in commands:
        assert command in text
    assert text.count("if: steps.scope.outputs.affected == 'true'") == 5


def test_pull_request_static_validation_step_is_exact_and_affected_only() -> None:
    text = workflow_text()

    assert inventory.validate_regular_pr_static_validation_step(text) == []
    regular_job = inventory.workflow_job_blocks(text)["individual-stock-pr-validation"]
    steps = inventory.workflow_step_blocks(regular_job)
    names = [inventory.workflow_step_name(step) for step in steps]
    assert names.count(inventory.PR_STATIC_DEPENDENCY_STEP_NAME) == 1
    assert names.count(inventory.PR_STATIC_VALIDATION_STEP_NAME) == 1
    assert names.index(inventory.PR_STATIC_DEPENDENCY_STEP_NAME) < names.index(
        inventory.PR_STATIC_VALIDATION_STEP_NAME
    )
    for step_name in (
        inventory.PR_STATIC_DEPENDENCY_STEP_NAME,
        "Validate workflow and scope contract",
        inventory.PR_STATIC_VALIDATION_STEP_NAME,
    ):
        step = next(
            step
            for step in steps
            if inventory.workflow_step_name(step) == step_name
        )
        assert (
            inventory.workflow_step_condition(step)
            == inventory.PR_STATIC_AFFECTED_CONDITION
        )


@pytest.mark.parametrize(
    "step_name",
    (
        inventory.PR_STATIC_DEPENDENCY_STEP_NAME,
        inventory.PR_STATIC_WORKFLOW_CONTRACT_STEP_NAME,
        inventory.PR_STATIC_VALIDATION_STEP_NAME,
    ),
)
def test_pull_request_static_validation_rejects_legacy_unconditional_step(
    step_name: str,
) -> None:
    text = workflow_text()
    affected_header = (
        f"      - name: {step_name}\n"
        f"        if: {inventory.PR_STATIC_AFFECTED_CONDITION}\n"
    )
    unconditional_header = f"      - name: {step_name}\n"
    assert text.count(affected_header) == 1

    mutated = text.replace(affected_header, unconditional_header, 1)

    assert inventory.validate_regular_pr_static_validation_step(mutated)


@pytest.mark.parametrize("command", inventory.PR_STATIC_VALIDATION_COMMANDS)
def test_pull_request_static_validation_rejects_each_missing_command(command: str) -> None:
    text = workflow_text()
    exact_line = f"          {command}\n"
    assert text.count(exact_line) == 1

    mutated = text.replace(exact_line, "", 1)

    assert inventory.validate_regular_pr_static_validation_step(mutated)


@pytest.mark.parametrize(
    "mutation",
    ("condition", "continue_on_error", "dead_branch", "duplicate"),
)
def test_pull_request_static_validation_rejects_inert_or_non_failing_carriers(
    mutation: str,
) -> None:
    text = workflow_text()
    name_line = f"      - name: {inventory.PR_STATIC_VALIDATION_STEP_NAME}\n"
    assert text.count(name_line) == 1
    if mutation == "condition":
        affected_header = (
            name_line
            + f"        if: {inventory.PR_STATIC_AFFECTED_CONDITION}\n"
        )
        assert text.count(affected_header) == 1
        mutated = text.replace(
            affected_header,
            name_line + "        if: false\n",
            1,
        )
    elif mutation == "continue_on_error":
        mutated = text.replace(
            name_line,
            name_line + "        continue-on-error: true\n",
            1,
        )
    elif mutation == "dead_branch":
        first = f"          {inventory.PR_STATIC_VALIDATION_COMMANDS[0]}\n"
        last = f"          {inventory.PR_STATIC_VALIDATION_COMMANDS[-1]}\n"
        mutated = text.replace(first, "          if false; then\n" + first, 1)
        mutated = mutated.replace(last, last + "          fi\n", 1)
    else:
        regular_job = inventory.workflow_job_blocks(text)["individual-stock-pr-validation"]
        static_step = next(
            step
            for step in inventory.workflow_step_blocks(regular_job)
            if inventory.workflow_step_name(step) == inventory.PR_STATIC_VALIDATION_STEP_NAME
        )
        mutated = text.replace(static_step, static_step + static_step, 1)

    assert inventory.validate_regular_pr_static_validation_step(mutated)

def test_pull_request_target_is_base_only_read_only_and_unfiltered() -> None:
    text = WORKFLOW.read_text(encoding="utf-8")
    jobs = inventory.workflow_job_blocks(text)
    guard = jobs[inventory.PR_SAFE_GUARD_JOB_ID]

    assert inventory.validate_pr_safe_base_guard_workflow_text(text) == []
    target_header = text.index("  pull_request_target:")
    permissions_header = text.index("\npermissions:", target_header)
    target_block = text[target_header:permissions_header]
    assert "paths:" not in target_block
    assert "paths-ignore:" not in target_block
    assert "permissions:\n  contents: read" in text
    assert "permissions:\n      contents: read" in guard
    assert "ref: ${{ github.event.pull_request.base.sha }}" in guard
    assert "ref: ${{ github.event.pull_request.head.sha }}" not in guard
    assert "git checkout " not in guard
    assert "git switch " not in guard
    assert "git show " not in guard
    assert "actions/upload-artifact@" not in guard
    assert "continue-on-error:" not in guard
    assert "secrets." not in guard
    assert "self-hosted" not in guard


def test_trust_root_guard_structure_rejects_security_drift() -> None:
    text = WORKFLOW.read_text(encoding="utf-8")
    assert inventory.validate_pr_safe_base_guard_workflow_text(text) == []

    mutations = (
        text.replace(
            "  pull_request_target:\n    types:",
            "  pull_request_target:\n    paths:\n      - scripts/**\n    types:",
            1,
        ),
        text.replace("      contents: read", "      contents: write", 1),
        text.replace(
            "      github.event.pull_request.base.repo.full_name == github.repository\n"
            "    runs-on: ubuntu-latest",
            "      github.event.pull_request.base.repo.full_name == github.repository\n"
            "    runs-on: self-hosted",
            1,
        ),
        text.replace(
            "          ref: ${{ github.event.pull_request.base.sha }}",
            "          ref: ${{ github.event.pull_request.head.sha }}",
            1,
        ),
        text.replace(
            '          test "$(git rev-parse "$LOCAL_HEAD_REF")" = "$HEAD_SHA"',
            '          git checkout "$LOCAL_HEAD_REF"',
            1,
        ),
        text.replace(
            "      - name: Validate trust-root self-change from base code",
            "      - name: Validate trust-root self-change from base code\n"
            "        continue-on-error: true",
            1,
        ),
        text.replace(
            '            --maintainer-approved "$MAINTAINER_APPROVED"',
            "            --maintainer-approved true",
            1,
        ),
        text.replace(
            "          HEAD_REPOSITORY: ${{ github.event.pull_request.head.repo.full_name }}",
            "          HEAD_REPOSITORY: ${{ secrets.UNTRUSTED }}",
            1,
        ),
    )
    for mutated in mutations:
        assert mutated != text
        assert inventory.validate_pr_safe_base_guard_workflow_text(mutated)


def test_regular_pull_request_job_remains_required_with_affected_only_static_steps() -> None:
    text = WORKFLOW.read_text(encoding="utf-8")
    jobs = inventory.workflow_job_blocks(text)
    regular = jobs["individual-stock-pr-validation"]

    assert inventory.validate_regular_pr_static_validation_step(text) == []
    assert "if: github.event_name == 'pull_request'" in regular
    assert inventory.PR_STATIC_VALIDATION_STEP_NAME in regular
    assert regular.count(
        f"if: {inventory.PR_STATIC_AFFECTED_CONDITION}"
    ) == 5
    for command in inventory.PR_STATIC_VALIDATION_COMMANDS:
        assert command in regular
