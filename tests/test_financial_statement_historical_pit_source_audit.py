from __future__ import annotations

import csv
import hashlib
import re
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


def test_source_registry_includes_official_correction_replacement_guidance() -> None:
    rows = validator.read_rows(validator.SOURCE_PATH)
    guidance = next(
        row
        for row in rows
        if row["source_id"] == "twse_financial_report_correction_guidance"
    )
    assert guidance["official_url"].startswith("https://www.twse.com.tw/")
    assert "deleted before a new electronic book is uploaded" in guidance["revision_semantics"]
    assert guidance["raw_archive_policy"] == "external_content_addressed_archive_required"
    assert guidance["pit_eligible"] == "False"
    assert guidance["formal_model_use_allowed"] == "False"


def test_evidence_registry_pins_upload_times_and_revision_leakage() -> None:
    rows = validator.read_rows(validator.EVIDENCE_PATH)
    uploads = [row for row in rows if row["witness_type"] == "visible_pdf_upload"]
    assert len(uploads) == 8
    assert {(row["period"], row["company_id"]) for row in uploads} == {
        (period, stock)
        for period in ("2013Q1", "2025Q1")
        for stock in ("2330", "5347", "2881", "2816")
    }
    leakage = next(row for row in rows if row["witness_id"] == "2025Q1_4552_cr_revision_leakage")
    assert leakage["metric_name"] == "basic_eps"
    assert (leakage["initial_value"], leakage["revision_value"], leakage["current_visible_value"]) == (
        "0.63",
        "0.65",
        "0.65",
    )
    assert leakage["document_visible_upload_at"] < leakage["revision_public_at"]
    assert leakage["pit_eligible"] == "False"
    assert leakage["formal_model_use_allowed"] == "False"


def test_raw_archive_manifest_binds_all_source_payload_hashes() -> None:
    archives = validator.read_rows(validator.RAW_ARCHIVE_MANIFEST_PATH)
    pilots = validator.read_rows(validator.PILOT_PATH)
    evidence = validator.read_rows(validator.EVIDENCE_PATH)
    assert len(archives) == 20
    assert len({row["archive_id"] for row in archives}) == 20
    archived_hashes = {row["raw_payload_sha256"] for row in archives}
    for row in archives:
        assert row["raw_archive_ref"] == f"sha256://{row['raw_payload_sha256']}"
        assert row["raw_payload_sha256"][:16] in row["external_archive_relative_path"]
        assert row["archive_status"] == "external_content_addressed_archive_verified"
        assert row["pit_eligible"] == "False"
        assert row["formal_model_use_allowed"] == "False"
    expected_hashes = {row["raw_payload_sha256"] for row in pilots}
    for row in evidence:
        expected_hashes.add(row["primary_response_sha256"])
        expected_hashes.update(
            re.findall(r"=([0-9a-f]{64})(?:;|$)", row["corroborating_sha256s"])
        )
        if row["current_payload_sha256"]:
            expected_hashes.add(row["current_payload_sha256"])
    expected_hashes.add(
        "7c5502cbcd4eab7f391c40e24a5375b1b8f9a4cea8e3aa345c674623d595cd1e"
    )
    assert archived_hashes == expected_hashes


def test_external_archive_validation_recomputes_bytes_and_sha(tmp_path: Path) -> None:
    payload = b"immutable raw evidence\n"
    raw_path = tmp_path / "evidence.bin"
    raw_path.write_bytes(payload)
    row = {
        "archive_id": "synthetic",
        "external_archive_relative_path": raw_path.name,
        "raw_byte_count": str(len(payload)),
        "raw_payload_sha256": hashlib.sha256(payload).hexdigest(),
    }
    assert validator.validate_external_archive_files([row], tmp_path) == []
    raw_path.write_bytes(payload + b"tampered")
    errors = validator.validate_external_archive_files([row], tmp_path)
    assert any("external raw byte count drift" in error for error in errors)
    assert any("external raw SHA-256 drift" in error for error in errors)


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
    monkeypatch.setattr(builder, "EVIDENCE_PATH", validator.EVIDENCE_PATH)
    monkeypatch.setattr(
        builder, "RAW_ARCHIVE_MANIFEST_PATH", validator.RAW_ARCHIVE_MANIFEST_PATH
    )
    before = sentinel.read_bytes()
    outputs = builder.build_and_write(tmp_path, registry)
    assert sentinel.read_bytes() == before
    assert all(path.is_file() for path in outputs.values())
    assert all(b"\r\n" not in path.read_bytes() for path in outputs.values())


def test_validator_rejects_pilot_that_claims_historical_pit(tmp_path: Path) -> None:
    for relative in (
        "config/daily_model_financial_statement_historical_pit_sources.csv",
        "config/daily_model_financial_statement_historical_pit_pilot.csv",
        "config/daily_model_financial_statement_historical_pit_evidence.csv",
        "config/daily_model_financial_statement_historical_pit_raw_archive_manifest.csv",
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


def test_validator_rejects_revision_leakage_state_drift(tmp_path: Path) -> None:
    for relative in (
        "config/daily_model_financial_statement_historical_pit_sources.csv",
        "config/daily_model_financial_statement_historical_pit_pilot.csv",
        "config/daily_model_financial_statement_historical_pit_evidence.csv",
        "config/daily_model_financial_statement_historical_pit_raw_archive_manifest.csv",
        "output/latest/research_backtest/financial_statement_historical_pit_source_audit_latest.csv",
        "output/latest/research_backtest/financial_statement_historical_pit_source_audit_latest.md",
        "docs/latest/financial_statement_historical_pit_source_audit_latest.csv",
        "docs/latest/financial_statement_historical_pit_source_audit_latest.md",
    ):
        src = ROOT / relative
        dst = tmp_path / relative
        dst.parent.mkdir(parents=True, exist_ok=True)
        dst.write_bytes(src.read_bytes())
    evidence_path = tmp_path / "config/daily_model_financial_statement_historical_pit_evidence.csv"
    rows = validator.read_rows(evidence_path)
    leakage = next(row for row in rows if row["witness_id"] == "2025Q1_4552_cr_revision_leakage")
    leakage["current_visible_value"] = "0.63"
    with evidence_path.open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)
    errors = validator.validate(tmp_path)
    assert any("EPS states must remain" in error for error in errors)


def test_validator_rejects_missing_historical_revision_witness(tmp_path: Path) -> None:
    for relative in (
        "config/daily_model_financial_statement_historical_pit_sources.csv",
        "config/daily_model_financial_statement_historical_pit_pilot.csv",
        "config/daily_model_financial_statement_historical_pit_evidence.csv",
        "config/daily_model_financial_statement_historical_pit_raw_archive_manifest.csv",
        "output/latest/research_backtest/financial_statement_historical_pit_source_audit_latest.csv",
        "output/latest/research_backtest/financial_statement_historical_pit_source_audit_latest.md",
        "docs/latest/financial_statement_historical_pit_source_audit_latest.csv",
        "docs/latest/financial_statement_historical_pit_source_audit_latest.md",
    ):
        src = ROOT / relative
        dst = tmp_path / relative
        dst.parent.mkdir(parents=True, exist_ok=True)
        dst.write_bytes(src.read_bytes())
    evidence_path = tmp_path / "config/daily_model_financial_statement_historical_pit_evidence.csv"
    rows = [
        row
        for row in validator.read_rows(evidence_path)
        if row["witness_id"] != "2013Q1_2816_ir_revision"
    ]
    with evidence_path.open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)
    errors = validator.validate(tmp_path)
    assert any("missing 2816 2013Q1 revision witness" in error for error in errors)


def test_validator_rejects_raw_archive_byte_count_drift(tmp_path: Path) -> None:
    for relative in (
        "config/daily_model_financial_statement_historical_pit_sources.csv",
        "config/daily_model_financial_statement_historical_pit_pilot.csv",
        "config/daily_model_financial_statement_historical_pit_evidence.csv",
        "config/daily_model_financial_statement_historical_pit_raw_archive_manifest.csv",
        "output/latest/research_backtest/financial_statement_historical_pit_source_audit_latest.csv",
        "output/latest/research_backtest/financial_statement_historical_pit_source_audit_latest.md",
        "docs/latest/financial_statement_historical_pit_source_audit_latest.csv",
        "docs/latest/financial_statement_historical_pit_source_audit_latest.md",
    ):
        src = ROOT / relative
        dst = tmp_path / relative
        dst.parent.mkdir(parents=True, exist_ok=True)
        dst.write_bytes(src.read_bytes())
    manifest_path = (
        tmp_path
        / "config/daily_model_financial_statement_historical_pit_raw_archive_manifest.csv"
    )
    rows = validator.read_rows(manifest_path)
    row = next(item for item in rows if item["archive_id"] == "t56_2816_2013Q1_correction")
    row["raw_byte_count"] = "6638"
    with manifest_path.open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)
    errors = validator.validate(tmp_path)
    assert any("generated raw archive byte count drift" in error for error in errors)


def test_pr_workflow_builds_and_validates_source_audit() -> None:
    text = (ROOT / ".github/workflows/daily_model_maintenance_pr_validation.yml").read_text(
        encoding="utf-8"
    )
    assert "docs/latest/financial_statement_historical_pit_source_audit_latest.*" in text
    assert "python scripts/build_financial_statement_historical_pit_source_audit.py" in text
    assert "python scripts/validate_financial_statement_historical_pit_source_audit.py" in text
    assert "git diff --exit-code --" in text
    assert "tests/test_financial_statement_historical_pit_source_audit.py" in text
