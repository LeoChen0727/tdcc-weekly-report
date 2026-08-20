from __future__ import annotations

import csv
from pathlib import Path

from scripts import validate_repo_semantic_integrity as validator


ROOT = Path(__file__).resolve().parents[1]


def test_repo_semantic_integrity_validator_passes() -> None:
    assert validator.main() == 0


def test_semantic_integrity_gate_is_hooked_into_pr_static_workflow() -> None:
    workflow = (ROOT / ".github" / "workflows" / "individual_stock_pr_validation.yml").read_text(
        encoding="utf-8"
    )

    assert "python scripts/validate_repo_semantic_integrity.py" in workflow


def test_report_artifact_lineage_manifest_has_required_artifacts() -> None:
    lineage = ROOT / "config" / "report_artifact_lineage.csv"
    with lineage.open("r", encoding="utf-8-sig", newline="") as fh:
        rows = {row["artifact_path"]: row for row in csv.DictReader(fh)}

    for artifact in {
        "output/latest/READ_ME_FIRST_DAILY_REPORT.txt",
        "output/latest/chatgpt_daily_report_packet_latest.txt",
        "output/latest/daily_volume_breakout_operation_section_latest.csv",
        "output/latest/daily_candidate_model_signals_for_report_latest.csv",
        "output/latest/stock_theme_taxonomy_latest.csv",
    }:
        assert artifact in rows
        assert rows[artifact]["producer"]
        assert rows[artifact]["source_artifacts"]
        assert rows[artifact]["validator"]


def test_chip_flow_orphan_builder_was_removed() -> None:
    inventory = ROOT / "config" / "repo_production_inventory.csv"
    with inventory.open("r", encoding="utf-8-sig", newline="") as fh:
        rows = {row["path"]: row for row in csv.DictReader(fh)}

    assert "scripts/build_chip_flow_positive_streak.py" not in rows


def test_manual_diagnostic_script_is_not_reported_as_orphan() -> None:
    path = "scripts/build_revenue_unreacted_range_research.py"
    row = validator.InventoryRow(
        path=path,
        kind="python",
        owner="research_backtest",
        status="manual_diagnostic",
        purpose="model-owned revenue research producer pending workflow wiring",
    )

    assert validator.validate_orphan_code({path: row}) == []
