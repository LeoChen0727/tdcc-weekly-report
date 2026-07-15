from __future__ import annotations

import csv
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import build_financial_statement_historical_pit_source_audit as builder  # noqa: E402
import validate_financial_statement_historical_pit_source_audit as validator  # noqa: E402


def test_committed_source_audit_is_fail_closed_and_valid() -> None:
    assert validator.validate() == []
    rows = validator.read_rows(validator.OUTPUT_CSV)
    assert {row["pit_eligible"] for row in rows} == {"False"}
    assert {row["formal_model_use_allowed"] for row in rows} == {"False"}


def test_pilot_covers_cross_year_market_scope_and_industry() -> None:
    rows = validator.read_rows(validator.PILOT_PATH)
    assert {row["period"] for row in rows} == {"2013Q1", "2025Q1"}
    for row in rows:
        assert "2330:ci:cr" in row["pilot_instances"]
        assert "5347:ci:cr" in row["pilot_instances"]
        assert "2881:fh:cr" in row["pilot_instances"]
        assert "2816:ins:ir" in row["pilot_instances"]
        assert row["member_time_min"][:4] != row["period"][:4]


def test_builder_preserves_mature_model_sentinel_hash(tmp_path: Path, monkeypatch) -> None:
    sentinel = tmp_path / "output/latest/daily_w_bottom_right_side_operation_section_latest.csv"
    sentinel.parent.mkdir(parents=True)
    sentinel.write_text("protected\n", encoding="utf-8")
    registry = tmp_path / "sentinels.csv"
    registry.write_text(
        "sentinel_id,artifact_glob,owner,sentinel_class,required,notes\n"
        "w_bottom,output/latest/daily_w_bottom_right_side_operation_section_latest.csv,w_bottom_right_side,formal_operation_adapter,True,test\n",
        encoding="utf-8",
    )
    monkeypatch.setattr(builder, "SOURCE_PATH", validator.SOURCE_PATH)
    monkeypatch.setattr(builder, "PILOT_PATH", validator.PILOT_PATH)
    before = sentinel.read_bytes()
    outputs = builder.build_and_write(tmp_path, registry)
    assert sentinel.read_bytes() == before
    assert all(path.is_file() for path in outputs.values())


def test_validator_rejects_pilot_that_claims_historical_pit(tmp_path: Path) -> None:
    for relative in (
        "config/daily_model_financial_statement_historical_pit_sources.csv",
        "config/daily_model_financial_statement_historical_pit_pilot.csv",
        "output/latest/research_backtest/financial_statement_historical_pit_source_audit_latest.csv",
        "output/latest/research_backtest/financial_statement_historical_pit_source_audit_latest.md",
        "docs/latest/financial_statement_historical_pit_source_audit_latest.csv",
        "docs/latest/financial_statement_historical_pit_source_audit_latest.md",
    ):
        src = ROOT / relative
        dst = tmp_path / relative
        dst.parent.mkdir(parents=True, exist_ok=True)
        dst.write_bytes(src.read_bytes())
    pilot_path = tmp_path / "config/daily_model_financial_statement_historical_pit_pilot.csv"
    rows = validator.read_rows(pilot_path)
    rows[0]["pit_eligible"] = "True"
    with pilot_path.open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)
    errors = validator.validate(tmp_path)
    assert any("pilot must remain fail closed" in error for error in errors)


def test_pr_workflow_builds_and_validates_source_audit() -> None:
    text = (ROOT / ".github/workflows/daily_model_maintenance_pr_validation.yml").read_text(
        encoding="utf-8"
    )
    assert "docs/latest/financial_statement_historical_pit_source_audit_latest.*" in text
    assert "python scripts/build_financial_statement_historical_pit_source_audit.py" in text
    assert "python scripts/validate_financial_statement_historical_pit_source_audit.py" in text
    assert "tests/test_financial_statement_historical_pit_source_audit.py" in text
