from __future__ import annotations

import subprocess
from pathlib import Path

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
        "docs/unrelated_note.md",
        "scripts/" + "build_daily_" + "candidate_model_layer.py",
        "tests/test_daily_candidate_model_layer.py",
    )

    assert all(scope.is_affected_path(path) for path in affected)
    assert not any(scope.is_affected_path(path) for path in unrelated)


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
    assert text.count("if: steps.scope.outputs.affected == 'true'") >= 2


def test_workflow_cannot_commit_push_or_deploy_artifacts() -> None:
    text = workflow_text().lower()
    forbidden = (
        "contents: write",
        "pages: write",
        "deployments: write",
        "git add ",
        "git commit",
        "git push",
        "ci_push_with_retry",
        "actions/upload-pages-artifact",
        "actions/deploy-pages",
        "repository_dispatch",
        "workflow_run:",
        "gh workflow run",
    )

    assert "contents: read" in text
    for snippet in forbidden:
        assert snippet not in text
    assert text.count(
        "actions/checkout@d23441a48e516b6c34aea4fa41551a30e30af803"
    ) == 2
    assert text.count(
        "actions/setup-python@ece7cb06caefa5fff74198d8649806c4678c61a1"
    ) == 1
    assert text.count(
        "actions/upload-artifact@ea165f8d65b6e75b540449e92b4886f43607fa02"
    ) == 1
    assert "actions/checkout@v6" not in text
    assert "actions/setup-python@v6" not in text
    assert "actions/upload-artifact@v4" not in text
    assert "name: upload audit-only evidence" in text
    assert "pr-safe-control-plane-audit-${{ github.run_id }}-${{ github.run_attempt }}" in text
    assert "${{ runner.temp }}/pr-safe-control-plane-audit-manifest.json" in text
    assert "${{ runner.temp }}/pr-safe-control-plane-audit-manifest.json.sha256" in text


def test_privileged_workflow_structure_is_closed_against_spoofing() -> None:
    text = workflow_text()

    assert inventory.validate_pr_safe_base_guard_workflow_text(text) == []
    assert inventory.workflow_action_uses(text) == (
        inventory.PR_SAFE_EXPECTED_ACTION_USES,
        [],
    )
    assert inventory.workflow_exact_mapping(
        text,
        "permissions",
        section_indent=0,
        entry_indent=2,
    ) == (inventory.PR_SAFE_READ_ONLY_PERMISSIONS, [])
    audit_job = inventory.workflow_job_blocks(text)["pr-safe-base-audit-runner"]
    assert inventory.workflow_exact_mapping(
        audit_job,
        "permissions",
        section_indent=4,
        entry_indent=6,
    ) == (inventory.PR_SAFE_READ_ONLY_PERMISSIONS, [])

    mutations = (
        text.replace(
            inventory.PR_SAFE_REGULAR_JOB_NAME_EXPRESSION,
            inventory.PR_SAFE_REQUIRED_CHECK_CONTEXT,
            1,
        ),
        text.replace("    timeout-minutes: 30\n", "", 1),
        text.replace(
            "permissions:\n  contents: read",
            "permissions:\n  contents: read\n  id-token: write",
            1,
        ),
        text.replace(
            "    permissions:\n      contents: read",
            "    permissions:\n      contents: read\n      pull-requests: write",
            1,
        ),
        text.replace(
            "      - name: Upload audit-only evidence",
            "      - name: Unexpected fifth action\n"
            "        uses: actions/cache@0000000000000000000000000000000000000000\n\n"
            "      - name: Upload audit-only evidence",
            1,
        ),
        text.replace(
            inventory.PR_SAFE_SETUP_PYTHON_ACTION,
            "actions/setup-python@v6",
            1,
        ),
        text.replace(
            f"        uses: {inventory.PR_SAFE_SETUP_PYTHON_ACTION}\n",
            "",
            1,
        ),
        text.replace(
            f"        uses: {inventory.PR_SAFE_SETUP_PYTHON_ACTION}\n",
            f"        uses: {inventory.PR_SAFE_SETUP_PYTHON_ACTION}\n"
            f"        uses: {inventory.PR_SAFE_SETUP_PYTHON_ACTION}\n",
            1,
        ),
        text.replace(
            "permissions:\n  contents: read",
            "permissions:\n  contents: read\npermissions:\n  contents: read",
            1,
        ),
        text.replace(
            "    permissions:\n      contents: read",
            "    permissions:\n      contents: write",
            1,
        ),
        text.replace(
            "    permissions:\n      contents: read\n\n    steps:",
            "    permissions:\n      contents: read\n"
            "    permissions:\n      contents: read\n\n    steps:",
            1,
        ),
        text.replace(
            "    permissions:\n      contents: read",
            "    permissions:\n      contents: read\n      contents: read",
            1,
        ),
        text.replace(
            "    name: pr-safe-base-audit-runner",
            "    # name: pr-safe-base-audit-runner\n"
            "    name: individual-stock-pr-validation",
            1,
        ),
        text.replace(
            "      github.event.pull_request.base.repo.full_name == github.repository\n"
            "    runs-on: ubuntu-latest",
            "      github.event.pull_request.base.repo.full_name == github.repository\n"
            "    runs-on: self-hosted",
            1,
        ),
        text.replace(
            "    timeout-minutes: 10",
            "    timeout-minutes: 10\n    timeout-minutes: 999",
            1,
        ),
        text.replace(
            "    if: >-\n"
            "      github.event_name == 'pull_request_target' &&\n"
            "      github.event.pull_request.base.ref == 'main' &&\n"
            "      github.event.pull_request.base.repo.full_name == github.repository",
            "    if: always()",
            1,
        ),
    )
    for mutated in mutations:
        assert mutated != text
        assert inventory.validate_pr_safe_base_guard_workflow_text(mutated)


def test_scope_output_is_stable(tmp_path: Path) -> None:
    output = tmp_path / "github-output.txt"
    matched = scope.matched_affected_paths(
        ["docs/unrelated_note.md", "docs/individual_stock_lifecycle_probe.md"]
    )

    scope.write_github_output(output, matched)

    assert output.read_text(encoding="utf-8") == "affected=true\nmatched_count=1\n"


def test_deleted_individual_stock_path_remains_in_git_scope(monkeypatch) -> None:
    deleted_path = "docs/individual_stock_tdcc_freshness_contract.md"

    def fake_run(command, **kwargs):
        assert "--diff-filter=ACMRD" in command
        assert command[-1] == "--"
        return subprocess.CompletedProcess(command, 0, stdout=f"{deleted_path}\n")

    monkeypatch.setattr(scope.subprocess, "run", fake_run)

    changed = scope.changed_paths_from_git("base", "head")

    assert changed == [deleted_path]
    assert scope.matched_affected_paths(changed) == [deleted_path]
