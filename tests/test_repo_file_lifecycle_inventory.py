from __future__ import annotations

import csv
from pathlib import Path

from scripts import validate_repo_file_lifecycle_inventory as validator


ROOT = Path(__file__).resolve().parents[1]


def test_repo_file_lifecycle_inventory_validator_passes() -> None:
    assert validator.main() == 0


def test_lifecycle_inventory_covers_existing_production_inventory() -> None:
    lifecycle_path = ROOT / "config" / "repo_file_lifecycle_inventory.csv"
    production_path = ROOT / "config" / "repo_production_inventory.csv"

    with lifecycle_path.open("r", encoding="utf-8-sig", newline="") as fh:
        lifecycle = {row["path"]: row for row in csv.DictReader(fh)}
    with production_path.open("r", encoding="utf-8-sig", newline="") as fh:
        production = {row["path"]: row for row in csv.DictReader(fh)}

    assert set(production) <= set(lifecycle)
    assert lifecycle["scripts/validate_repo_file_lifecycle_inventory.py"]["status"] == "active"
    assert lifecycle["scripts/build_chip_flow_positive_streak.py"]["status"] == "delete_candidate"


def test_active_guidance_does_not_point_to_retired_daily_pdf_artifacts() -> None:
    for path, row in validator.load_lifecycle_inventory([]).items():
        if row.type not in {"guidance_doc", "generated_guidance"} or row.status == "historical_artifact":
            continue
        text = (ROOT / path).read_text(encoding="utf-8-sig", errors="replace")
        assert "daily_market_curated_report_latest.pdf" not in text
        assert "daily_market_full_table_report_latest.pdf" not in text


def test_lifecycle_gate_is_hooked_into_daily_pipeline() -> None:
    workflow = (ROOT / ".github" / "workflows" / "daily_full_pipeline.yml").read_text(
        encoding="utf-8"
    )
    boundary = (ROOT / "scripts" / "validate_daily_production_boundaries.py").read_text(
        encoding="utf-8"
    )

    assert "python scripts/validate_repo_file_lifecycle_inventory.py" in workflow
    assert "validate_repo_file_lifecycle_inventory.py" in boundary
