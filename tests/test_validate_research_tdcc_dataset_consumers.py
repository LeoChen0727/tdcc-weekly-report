from __future__ import annotations

import sys
from pathlib import Path

import pandas as pd


ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))

from research_tdcc_dataset_consumer import ResearchTdccDatasetContract
from validate_research_tdcc_dataset_consumers import (
    CONSUMER_PATHS,
    validate_consumer_sources,
    validate_csv_artifacts,
    validate_markdown_artifacts,
)


def contract(tmp_path: Path) -> ResearchTdccDatasetContract:
    return ResearchTdccDatasetContract(
        dataset_id="tdcc-fixture-full-history",
        dataset_hash="fixture",
        signal_date="20260717",
        required_dates=("20260703", "20260709", "20260717"),
        history_dates=("20260626", "20260703", "20260709", "20260717"),
        official_dates=("20260626", "20260703", "20260709", "20260717"),
        accepted_history_exceptions=frozenset(),
        snapshots=(),
        continuity_snapshots=(),
        manifest_path=tmp_path / "manifest.json",
    )


def test_registered_consumers_use_only_canonical_adapter() -> None:
    assert validate_consumer_sources() == []


def test_forbidden_secondary_history_source_fails(tmp_path: Path) -> None:
    for relative in CONSUMER_PATHS:
        path = tmp_path / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text("from research_tdcc_dataset_consumer import load_research_tdcc_dataset_contract\n", encoding="utf-8")
    target = tmp_path / CONSUMER_PATHS[0]
    target.write_text(target.read_text(encoding="utf-8") + 'Path("data/tdcc_stock_history")\n', encoding="utf-8")
    errors = validate_consumer_sources(tmp_path)
    assert any("forbidden source" in error for error in errors)


def test_artifact_dataset_id_must_match(tmp_path: Path) -> None:
    expected = contract(tmp_path)
    csv_path = tmp_path / "artifact.csv"
    md_path = tmp_path / "artifact.md"
    pd.DataFrame([{"source_tdcc_dataset_id": expected.dataset_id}]).to_csv(csv_path, index=False)
    md_path.write_text(f"source_tdcc_dataset_id: {expected.dataset_id}\n", encoding="utf-8")
    assert validate_csv_artifacts([csv_path], expected) == []
    assert validate_markdown_artifacts([md_path], expected) == []

    pd.DataFrame([{"source_tdcc_dataset_id": "stale"}]).to_csv(csv_path, index=False)
    assert "mismatch" in validate_csv_artifacts([csv_path], expected)[0]
