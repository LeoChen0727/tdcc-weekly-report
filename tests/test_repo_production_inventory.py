from __future__ import annotations

from pathlib import Path
import csv

from scripts import validate_repo_production_inventory as inventory


ROOT = Path(__file__).resolve().parents[1]


def test_repo_production_inventory_validator_passes() -> None:
    assert inventory.main() == 0


def test_inventory_manifest_exists_and_is_authoritative() -> None:
    manifest = ROOT / "config" / "repo_production_inventory.csv"
    docs = ROOT / "docs" / "repo_production_inventory.md"

    assert manifest.exists()
    assert docs.exists()
    assert "config/repo_production_inventory.csv" in docs.read_text(encoding="utf-8")
    assert "tests/**/*.py" in docs.read_text(encoding="utf-8")
    assert "executable_script" in docs.read_text(encoding="utf-8")


def test_inventory_covers_tests_and_non_python_executables() -> None:
    manifest = ROOT / "config" / "repo_production_inventory.csv"
    with manifest.open("r", encoding="utf-8-sig", newline="") as fh:
        rows = {row["path"]: row for row in csv.DictReader(fh)}

    assert rows["tests/conftest.py"]["kind"] == "test_python"
    assert rows["scripts/ci_push_with_retry.sh"]["kind"] == "executable_script"
    assert rows["docs/apps_script_workflow_trigger.gs"]["kind"] == "executable_script"


def test_all_lane_workflows_run_repo_inventory_gate() -> None:
    for workflow_path in inventory.REQUIRED_WORKFLOW_COMMANDS:
        workflow_text = (ROOT / workflow_path).read_text(encoding="utf-8")
        assert "python scripts/validate_repo_production_inventory.py" in workflow_text


def test_weekly_and_warrant_workflows_do_not_stage_source_files() -> None:
    for workflow_path in (
        ".github/workflows/tdcc_weekly.yml",
        ".github/workflows/tdcc_weekly_pr_validation.yml",
        ".github/workflows/tdcc_history_backfill.yml",
        ".github/workflows/warrant_flow.yml",
    ):
        workflow_text = (ROOT / workflow_path).read_text(encoding="utf-8")
        assert "git add scripts/" not in workflow_text
        assert "git add .github/workflows/" not in workflow_text


def test_tdcc_weekly_pr_validation_is_not_a_publish_workflow() -> None:
    workflow_text = (ROOT / ".github" / "workflows" / "tdcc_weekly_pr_validation.yml").read_text(
        encoding="utf-8"
    )

    assert "pull_request:" in workflow_text
    assert "workflow_dispatch:" not in workflow_text
    assert "contents: read" in workflow_text
    assert "contents: write" not in workflow_text
    assert "git commit" not in workflow_text
    assert "git push" not in workflow_text
    assert "actions/deploy-pages" not in workflow_text


def test_daily_workflow_runs_repo_inventory_before_daily_generation() -> None:
    workflow_text = (ROOT / ".github" / "workflows" / "daily_full_pipeline.yml").read_text(
        encoding="utf-8"
    )

    repo_inventory_at = workflow_text.index("python scripts/validate_repo_production_inventory.py")
    price_fetch_at = workflow_text.index("python fetch_official_daily_price.py")
    assert repo_inventory_at < price_fetch_at


def test_daily_boundary_validator_runs_repo_inventory_gate() -> None:
    boundary_text = (ROOT / "scripts" / "validate_daily_production_boundaries.py").read_text(
        encoding="utf-8"
    )

    assert "validate_repo_production_inventory.py" in boundary_text
