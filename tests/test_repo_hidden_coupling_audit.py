from __future__ import annotations

import csv
from pathlib import Path

from scripts import validate_repo_hidden_coupling_audit as validator


ROOT = Path(__file__).resolve().parents[1]


def test_repo_hidden_coupling_audit_validator_passes() -> None:
    assert validator.main() == 0


def test_hidden_coupling_audit_has_required_categories_and_actions() -> None:
    with (ROOT / "config" / "repo_hidden_coupling_audit.csv").open(
        "r", encoding="utf-8-sig", newline=""
    ) as fh:
        rows = list(csv.DictReader(fh))

    categories = {row["category"] for row in rows}
    assert validator.REQUIRED_CATEGORIES <= categories
    assert {row["issue_id"] for row in rows} == {f"HC-{index:03d}" for index in range(1, 7)}
    assert all(row["next_action"].strip() for row in rows)
    assert all(row["owner_lane"].strip() for row in rows)


def test_hidden_coupling_audit_is_hooked_into_workflows() -> None:
    command = "python scripts/validate_repo_hidden_coupling_audit.py"
    daily = (ROOT / ".github" / "workflows" / "daily_full_pipeline.yml").read_text(
        encoding="utf-8"
    )
    pr = (
        ROOT / ".github" / "workflows" / "daily_model_maintenance_pr_validation.yml"
    ).read_text(encoding="utf-8")

    assert command in daily
    assert command in pr
