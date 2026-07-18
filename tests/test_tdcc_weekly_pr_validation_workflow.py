from __future__ import annotations

from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
WORKFLOW = ROOT / ".github" / "workflows" / "tdcc_weekly_pr_validation.yml"


def workflow_text() -> str:
    return WORKFLOW.read_text(encoding="utf-8")


def test_tdcc_pr_validation_is_read_only() -> None:
    text = workflow_text()
    assert "pull_request:" in text
    assert "contents: read" in text
    for forbidden in ("contents: write", "git add ", "git commit", "git push"):
        assert forbidden not in text


def test_tdcc_pr_validation_covers_continuity_contracts() -> None:
    text = workflow_text()
    required = (
        "python scripts/validate_apps_script_workflow_triggers.py",
        "python scripts/validate_repo_file_lifecycle_inventory.py",
        "python scripts/validate_repo_production_inventory.py",
        "python scripts/validate_repo_semantic_integrity.py",
        "python scripts/validate_daily_production_boundaries.py",
        "tests/test_tdcc_monthly_history_gap_repair.py",
        "tests/test_tdcc_dataset_contract.py",
        "tests/test_tdcc_weekly_data_readiness.py",
        "tests/test_tdcc_weekly_history_continuity.py",
        "tests/test_tdcc_weekly_pr_validation_workflow.py",
    )
    for command in required:
        assert command in text


def test_tdcc_pr_validation_watches_runtime_files() -> None:
    text = workflow_text()
    required_paths = (
        '".github/workflows/tdcc_weekly.yml"',
        '"docs/apps_script_workflow_trigger.gs"',
        '"scripts/build_tdcc_stock_history.py"',
        '"scripts/build_tdcc_dataset_manifest.py"',
        '"scripts/repair_tdcc_weekly_history_continuity.py"',
        '"scripts/tdcc_weekly_data_readiness.py"',
        '"scripts/tdcc_stock_history_utils.py"',
        '"scripts/tdcc_dataset_contract.py"',
        '"scripts/validate_tdcc_dataset_manifest.py"',
        '"tdcc_holder_ratio_top10.py"',
    )
    for path in required_paths:
        assert path in text
