from __future__ import annotations

import csv
from pathlib import Path

from scripts import trace_runtime_file_lineage
from scripts import validate_repo_advanced_integrity as validator


ROOT = Path(__file__).resolve().parents[1]


def test_repo_advanced_integrity_validator_passes() -> None:
    assert validator.main() == 0


def test_advanced_integrity_gate_is_hooked_into_daily_pipeline() -> None:
    workflow = (ROOT / ".github" / "workflows" / "daily_full_pipeline.yml").read_text(
        encoding="utf-8"
    )
    boundary = (ROOT / "scripts" / "validate_daily_production_boundaries.py").read_text(
        encoding="utf-8"
    )

    assert "python scripts/validate_repo_advanced_integrity.py" in workflow
    assert "validate_repo_advanced_integrity.py" in boundary


def test_advanced_integrity_contracts_exist() -> None:
    for path in validator.REQUIRED_CONFIGS:
        assert path.exists(), path


def test_pdf_golden_contract_has_six_formal_chatgpt_side_reports() -> None:
    with validator.PDF_GOLDEN_CONTRACT.open("r", encoding="utf-8-sig", newline="") as fh:
        rows = {row["report_id"]: row for row in csv.DictReader(fh)}

    assert set(rows) == {
        "mainstream_daily_recommendation_highlight",
        "mainstream_full_candidate_list",
        "non_mainstream_daily_recommendation_highlight",
        "non_mainstream_full_candidate_list",
        "warrant_market_auxiliary",
        "market_risk_background",
    }


def test_runtime_file_lineage_tracer_records_read_and_write(tmp_path: Path) -> None:
    data = tmp_path / "sample.txt"
    tracer = trace_runtime_file_lineage.FileAccessTracer(repo_root=tmp_path)

    with tracer:
        data.write_text("ok", encoding="utf-8")
        assert data.read_text(encoding="utf-8") == "ok"

    events = {(event.operation, event.normalized_path) for event in tracer.iter_unique_events()}
    assert ("Path.write_text:write", "sample.txt") in events
    assert ("Path.read_text:read", "sample.txt") in events


def test_model_condition_spec_covers_registry_models() -> None:
    spec_rows = validator.read_csv_rows(validator.MODEL_CONDITION_SPEC)
    registry_rows = validator.read_csv_rows(validator.MODEL_REGISTRY_CSV)

    spec_models = {row["model_id"] for row in spec_rows}
    registry_models = {
        row["model_id"]
        for row in registry_rows
        if row.get("model_registry_active", "") == "True"
    }
    assert registry_models <= spec_models
