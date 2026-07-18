from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
WORKFLOW = ROOT / ".github" / "workflows" / "research_backtest_pipeline.yml"


def test_research_workflow_validates_canonical_contract_before_tdcc_jobs() -> None:
    text = WORKFLOW.read_text(encoding="utf-8")
    gate = text.index("Validate canonical TDCC research consumer contract")
    first_tdcc_job = text.index("Build TDCC overheated short-term edge")
    assert gate < first_tdcc_job
    assert "python scripts/validate_tdcc_dataset_manifest.py" in text[gate:first_tdcc_job]
    assert "python scripts/validate_research_tdcc_dataset_consumers.py" in text[gate:first_tdcc_job]


def test_research_workflow_validates_generated_tdcc_lineage() -> None:
    text = WORKFLOW.read_text(encoding="utf-8")
    assert text.count("python scripts/validate_research_tdcc_dataset_consumers.py") >= 3
    assert "--csv output/history/tdcc_signals/tdcc_signal_snapshot.csv" in text
    assert "--csv output/latest/weekly_surge_multifactor_filter_grid_latest.csv" in text
