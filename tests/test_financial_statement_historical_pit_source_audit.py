from __future__ import annotations

import csv
import hashlib
import re
import sys
import zipfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import build_financial_statement_historical_pit_source_audit as builder  # noqa: E402
import validate_financial_statement_historical_pit_source_audit as validator  # noqa: E402


def test_committed_source_audit_is_fail_closed_and_valid() -> None:
    assert validator.validate() == []
    rows = validator.read_rows(validator.OUTPUT_CSV)
    assert {row["audit_id"] for row in rows} == {
        "financial_statement_historical_pit_source_audit_v4"
    }
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


def test_source_registry_keeps_twse_openapi_current_snapshot_only() -> None:
    rows = validator.read_rows(validator.SOURCE_PATH)
    source = next(
        row
        for row in rows
        if row["source_id"] == "twse_openapi_financial_statement_current_snapshot"
    )
    assert source["official_url"].startswith("https://openapi.twse.com.tw/")
    assert source["status"] == "current_snapshot_only_not_historical_pit"
    assert "not company filed_at" in source["availability_semantics"]
    assert "no company revision id or version selector" in source["revision_semantics"]
    assert source["pit_eligible"] == "False"
    assert source["formal_model_use_allowed"] == "False"


def test_source_registry_keeps_data_eshop_candidates_specification_only() -> None:
    rows = {
        row["source_id"]: row for row in validator.read_rows(validator.SOURCE_PATH)
    }
    s21 = rows["twse_data_eshop_s21_ifrs_active_push"]
    l01 = rows["twse_data_eshop_l01_delivery_list"]
    application = rows["twse_data_eshop_application_process"]
    assert s21["official_url"].startswith("https://eshop.twse.com.tw/")
    assert l01["official_url"].startswith("https://eshop.twse.com.tw/")
    assert application["official_url"].endswith("/zh/mops/publicStep")
    assert "written specification" in s21["notes"]
    assert "written schema" in l01["notes"]
    assert (
        "does not publish whether L01 identifies company period statement scope or S21 payload"
        in l01["scope_semantics"]
    )
    assert "may be a delivery crosswalk only" in l01["notes"]
    assert application["status"] == "external_coordination_required"
    assert all(row["pit_eligible"] == "False" for row in (s21, l01, application))
    assert all(
        row["formal_model_use_allowed"] == "False"
        for row in (s21, l01, application)
    )


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


def test_evidence_registry_pins_two_2348_revisions_and_one_current_payload() -> None:
    rows = validator.read_rows(validator.EVIDENCE_PATH)
    revision_1 = next(row for row in rows if row["witness_id"] == "2026Q1_2348_cr_revision_1")
    revision_2 = next(row for row in rows if row["witness_id"] == "2026Q1_2348_cr_revision_2")
    current = next(
        row
        for row in rows
        if row["witness_id"] == "2026Q1_2348_cr_current_snapshot_after_two_revisions"
    )
    assert revision_1["revision_public_at"] == "2026-05-25T15:59:11+08:00"
    assert revision_2["revision_public_at"] == "2026-06-03T15:38:46+08:00"
    assert "SKEY=1" in revision_1["request_contracts"]
    assert "SKEY=2" in revision_2["request_contracts"]
    assert current["current_payload_sha256"] == (
        "b2e2852b47d751bfe352925c75882d016124ed6a5bff6fd4d6964b4741efd534"
    )
    assert "bulk=" in current["corroborating_sha256s"]
    assert all(row["pit_eligible"] == "False" for row in (revision_1, revision_2, current))
    assert all(
        row["formal_model_use_allowed"] == "False"
        for row in (revision_1, revision_2, current)
    )


def test_raw_archive_manifest_binds_all_source_payload_hashes() -> None:
    archives = validator.read_rows(validator.RAW_ARCHIVE_MANIFEST_PATH)
    pilots = validator.read_rows(validator.PILOT_PATH)
    evidence = validator.read_rows(validator.EVIDENCE_PATH)
    assert len(archives) == 39
    assert len({row["archive_id"] for row in archives}) == 39
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
    expected_hashes.update(
        {
            "6fea1b7ff3677d8fb21ec3c320e910eafe5ca872b418e9e93253f749efc58098",
            "9c7936c4bc31dfd954a6d2cb565f14358e52fef805886306fb7200fc772a20d9",
            "7c5cb39eeba722f7fe1dc211caea0655c734aedb28081d40aef02ac09e2c940f",
        }
    )
    assert archived_hashes == expected_hashes
    data_eshop_bindings = {
        "twse_data_eshop_s21_product_page": "twse_data_eshop_s21_ifrs_active_push",
        "twse_data_eshop_l01_product_page": "twse_data_eshop_l01_delivery_list",
        "twse_data_eshop_application_page": "twse_data_eshop_application_process",
    }
    for archive_id, source_id in data_eshop_bindings.items():
        matching = [
            row
            for row in archives
            if source_id in row["related_record_ids"].split(";")
        ]
        assert len(matching) == 1
        assert matching[0]["archive_id"] == archive_id
        assert matching[0]["related_record_ids"] == source_id


def test_validator_rejects_data_eshop_cross_source_raw_binding(tmp_path: Path) -> None:
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
    l01 = next(
        row
        for row in rows
        if row["archive_id"] == "twse_data_eshop_l01_product_page"
    )
    l01["related_record_ids"] += ";twse_data_eshop_s21_ifrs_active_push"
    with manifest_path.open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)
    errors = validator.validate(tmp_path)
    assert any(
        "Data E-Shop source must bind exactly one dedicated raw page" in error
        for error in errors
    )


def test_archive_lineage_binding_rejects_cross_witness_row_swap() -> None:
    archives = [
        dict(row) for row in validator.read_rows(validator.RAW_ARCHIVE_MANIFEST_PATH)
    ]
    pilots = validator.read_rows(validator.PILOT_PATH)
    evidence = validator.read_rows(validator.EVIDENCE_PATH)
    first = next(row for row in archives if row["archive_id"] == "t57_2330_2013Q1")
    second = next(row for row in archives if row["archive_id"] == "t57_5347_2013Q1")
    for field in (
        "raw_payload_sha256",
        "raw_archive_ref",
        "external_archive_relative_path",
        "raw_byte_count",
    ):
        first[field], second[field] = second[field], first[field]
    errors = validator.validate_archive_lineage_bindings(pilots, evidence, archives)
    assert any("2013Q1_2330_cr_upload" in error for error in errors)
    assert any("2013Q1_5347_cr_upload" in error for error in errors)


def test_archive_lineage_binding_rejects_same_witness_role_swap() -> None:
    archives = [
        dict(row) for row in validator.read_rows(validator.RAW_ARCHIVE_MANIFEST_PATH)
    ]
    pilots = validator.read_rows(validator.PILOT_PATH)
    evidence = validator.read_rows(validator.EVIDENCE_PATH)
    first = next(
        row for row in archives if row["archive_id"] == "t05_api_2348_2026Q1_revision1"
    )
    second = next(
        row for row in archives if row["archive_id"] == "t56_2348_2026Q1_skey1"
    )
    for field in (
        "raw_payload_sha256",
        "raw_archive_ref",
        "external_archive_relative_path",
        "raw_byte_count",
    ):
        first[field], second[field] = second[field], first[field]
    errors = validator.validate_archive_lineage_bindings(pilots, evidence, archives)
    assert any("t05_api_2348_2026Q1_revision1" in error for error in errors)
    assert any("t56_2348_2026Q1_skey1" in error for error in errors)


def test_correction_attachments_remain_selected_page_evidence() -> None:
    archives = {
        row["archive_id"]: row
        for row in validator.read_rows(validator.RAW_ARCHIVE_MANIFEST_PATH)
    }
    expected = {
        "t56_attachment_2816_2013Q1",
        "t56_attachment_4552_2025Q1",
        "t56_attachment_2348_2026Q1_skey1",
        "t56_attachment_2348_2026Q1_skey2",
    }
    assert expected <= set(archives)
    for archive_id in expected:
        row = archives[archive_id]
        assert row["payload_role"] == "financial_report_correction_attachment_selected_pages"
        assert row["availability_precision"] == (
            "correction_attachment_link_date_only_not_filed_at"
        )
        assert row["media_type"] == "application/pdf"
        assert row["pit_eligible"] == "False"
        assert row["formal_model_use_allowed"] == "False"


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


def test_external_archive_validation_opens_bulk_and_matches_direct_2348_member(
    tmp_path: Path,
) -> None:
    member_name = "tifrs-fr1-m1-ci-cr-2348-2026Q1.html"
    direct_payload = b"<html>immutable current 2348 payload</html>\n"
    direct_path = tmp_path / "direct.html"
    direct_path.write_bytes(direct_payload)
    bulk_path = tmp_path / "bulk.zip"
    with zipfile.ZipFile(bulk_path, "w", compression=zipfile.ZIP_DEFLATED) as archive:
        archive.writestr(member_name, direct_payload)

    rows = [
        {
            "archive_id": "bulk_xbrl_2026Q1",
            "external_archive_relative_path": bulk_path.name,
            "raw_byte_count": str(bulk_path.stat().st_size),
            "raw_payload_sha256": hashlib.sha256(bulk_path.read_bytes()).hexdigest(),
        },
        {
            "archive_id": "xbrl_2348_2026Q1_current",
            "external_archive_relative_path": direct_path.name,
            "raw_byte_count": str(len(direct_payload)),
            "raw_payload_sha256": hashlib.sha256(direct_payload).hexdigest(),
        },
    ]
    assert validator.validate_external_archive_files(rows, tmp_path) == []

    with zipfile.ZipFile(bulk_path, "w", compression=zipfile.ZIP_DEFLATED) as archive:
        archive.writestr(member_name, direct_payload)
        archive.writestr(f"duplicate/{member_name}", direct_payload)
    rows[0]["raw_byte_count"] = str(bulk_path.stat().st_size)
    rows[0]["raw_payload_sha256"] = hashlib.sha256(bulk_path.read_bytes()).hexdigest()
    errors = validator.validate_external_archive_files(rows, tmp_path)
    assert any("expected exactly one 2348 2026Q1 member" in error for error in errors)

    with zipfile.ZipFile(bulk_path, "w", compression=zipfile.ZIP_DEFLATED) as archive:
        archive.writestr(f"nested/{member_name}", direct_payload)
    rows[0]["raw_byte_count"] = str(bulk_path.stat().st_size)
    rows[0]["raw_payload_sha256"] = hashlib.sha256(bulk_path.read_bytes()).hexdigest()
    errors = validator.validate_external_archive_files(rows, tmp_path)
    assert any("expected exactly one 2348 2026Q1 member" in error for error in errors)


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


def test_validator_rejects_generated_audit_that_claims_formal_use(tmp_path: Path) -> None:
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
    for relative in (
        "output/latest/research_backtest/financial_statement_historical_pit_source_audit_latest.csv",
        "docs/latest/financial_statement_historical_pit_source_audit_latest.csv",
    ):
        path = tmp_path / relative
        rows = validator.read_rows(path)
        rows[0]["formal_model_use_allowed"] = "True"
        with path.open("w", encoding="utf-8-sig", newline="") as handle:
            writer = csv.DictWriter(handle, fieldnames=list(rows[0]))
            writer.writeheader()
            writer.writerows(rows)
    errors = validator.validate(tmp_path)
    assert any("generated source audit must remain fail closed" in error for error in errors)


def test_validator_rejects_generated_witness_and_archive_projection_drift(
    tmp_path: Path,
) -> None:
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
    for relative in (
        "output/latest/research_backtest/financial_statement_historical_pit_source_audit_latest.csv",
        "docs/latest/financial_statement_historical_pit_source_audit_latest.csv",
    ):
        path = tmp_path / relative
        rows = validator.read_rows(path)
        witness = next(
            row
            for row in rows
            if row["record_type"] == "evidence_witness"
            and row["record_id"] == "2026Q1_2348_cr_revision_1"
        )
        witness["revision_evidence"] += ";tampered=true"
        witness["blocker"] = "noncanonical_witness_blocker"
        archive = next(
            row
            for row in rows
            if row["record_type"] == "raw_archive"
            and row["record_id"] == "t05_api_2348_2026Q1_revision1"
        )
        archive["blocker"] = "noncanonical_archive_blocker"
        with path.open("w", encoding="utf-8-sig", newline="") as handle:
            writer = csv.DictWriter(handle, fieldnames=list(rows[0]))
            writer.writeheader()
            writer.writerows(rows)
    errors = validator.validate(tmp_path)
    assert any("generated witness projection drift" in error for error in errors)
    assert any("generated raw archive projection drift" in error for error in errors)


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
