from __future__ import annotations

from pathlib import Path

from scripts import validate_repo_code_isolation_policy as validator


ROOT = Path(__file__).resolve().parents[1]


def test_repo_code_isolation_policy_validator_passes() -> None:
    assert validator.main() == 0


def test_daily_full_pipeline_runs_code_isolation_gates() -> None:
    workflow_text = (ROOT / ".github" / "workflows" / "daily_full_pipeline.yml").read_text(
        encoding="utf-8"
    )

    assert "python scripts/validate_repo_code_isolation_policy.py" in workflow_text
    assert "python scripts/validate_chatgpt_side_pdf_layout_independence.py" in workflow_text


def test_daily_boundary_validator_runs_code_isolation_policy() -> None:
    boundary_text = (ROOT / "scripts" / "validate_daily_production_boundaries.py").read_text(
        encoding="utf-8"
    )

    assert "validate_repo_code_isolation_policy.py" in boundary_text
