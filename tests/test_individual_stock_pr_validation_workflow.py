from __future__ import annotations

import subprocess
from pathlib import Path

from scripts import detect_individual_stock_pr_scope as scope


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
    assert "    name: individual-stock-pr-validation" in text
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
        "scripts/validate_individual_pdf_contract_consumers.py",
        "tests/test_individual_pdf_contract_consumers.py",
        "tests/test_individual_stock_pr_validation_workflow.py",
    )
    unrelated = (
        "docs/unrelated_note.md",
        "scripts/" + "build_daily_" + "candidate_model_layer.py",
        "tests/test_daily_candidate_model_layer.py",
    )

    assert all(scope.is_affected_path(path) for path in affected)
    assert not any(scope.is_affected_path(path) for path in unrelated)


def test_individual_stock_history_root_is_affected() -> None:
    assert scope.is_affected_path(
        "output/history/individual_stock_reports/2330/20260717.json"
    )


def test_workflow_contains_required_affected_validation_commands() -> None:
    text = workflow_text()
    commands = (
        "git diff --check",
        "python scripts/validate_repo_file_lifecycle_inventory.py",
        "python scripts/validate_repo_production_inventory.py",
        "python scripts/validate_individual_pdf_contract_consumers.py",
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
        "actions/upload-artifact",
        "actions/upload-pages-artifact",
        "actions/deploy-pages",
        "repository_dispatch",
        "workflow_run:",
        "gh workflow run",
    )

    assert "contents: read" in text
    for snippet in forbidden:
        assert snippet not in text


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
