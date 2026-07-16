from __future__ import annotations

import argparse
import csv
import hashlib
import re
from datetime import datetime
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SOURCE_PATH = ROOT / "config/daily_model_financial_statement_historical_pit_sources.csv"
PILOT_PATH = ROOT / "config/daily_model_financial_statement_historical_pit_pilot.csv"
EVIDENCE_PATH = ROOT / "config/daily_model_financial_statement_historical_pit_evidence.csv"
RAW_ARCHIVE_MANIFEST_PATH = (
    ROOT / "config/daily_model_financial_statement_historical_pit_raw_archive_manifest.csv"
)
OUTPUT_CSV = ROOT / "output/latest/research_backtest/financial_statement_historical_pit_source_audit_latest.csv"
OUTPUT_MD = ROOT / "output/latest/research_backtest/financial_statement_historical_pit_source_audit_latest.md"
DOCS_CSV = ROOT / "docs/latest/financial_statement_historical_pit_source_audit_latest.csv"
DOCS_MD = ROOT / "docs/latest/financial_statement_historical_pit_source_audit_latest.md"


def read_rows(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))


def _sha256_path(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def validate_external_archive_files(
    raw_archives: list[dict[str, str]], external_archive_root: Path
) -> list[str]:
    errors: list[str] = []
    for row in raw_archives:
        archive_id = row["archive_id"]
        raw_path = external_archive_root / row["external_archive_relative_path"]
        if not raw_path.is_file():
            errors.append(f"{archive_id}: external raw payload is missing: {raw_path}")
            continue
        try:
            expected_bytes = int(row["raw_byte_count"])
        except ValueError:
            errors.append(f"{archive_id}: external manifest raw byte count is invalid")
            expected_bytes = -1
        if raw_path.stat().st_size != expected_bytes:
            errors.append(f"{archive_id}: external raw byte count drift")
        if _sha256_path(raw_path) != row["raw_payload_sha256"]:
            errors.append(f"{archive_id}: external raw SHA-256 drift")
    return errors


def validate(root: Path = ROOT, external_archive_root: Path | None = None) -> list[str]:
    errors: list[str] = []
    sources = read_rows(root / SOURCE_PATH.relative_to(ROOT))
    pilots = read_rows(root / PILOT_PATH.relative_to(ROOT))
    evidence = read_rows(root / EVIDENCE_PATH.relative_to(ROOT))
    raw_archives = read_rows(root / RAW_ARCHIVE_MANIFEST_PATH.relative_to(ROOT))
    audit = read_rows(root / OUTPUT_CSV.relative_to(ROOT))
    required_sources = {
        "mops_xbrl_bulk_index",
        "mops_xbrl_bulk_download",
        "mops_xbrl_single_company",
        "mops_financial_report_announcement",
        "mops_financial_report_correction",
        "mops_historical_material_information",
        "mops_financial_report_document_index",
        "twse_financial_report_correction_guidance",
        "mops_taxonomy_download",
    }
    if {row["source_id"] for row in sources} != required_sources:
        errors.append("historical PIT source surface registry is incomplete")
    if len({row["source_id"] for row in sources}) != len(sources):
        errors.append("historical PIT source surface ids must be unique")
    for row in sources:
        if row["pit_eligible"] != "False" or row["formal_model_use_allowed"] != "False":
            errors.append(f"{row['source_id']}: unproven source cannot authorize historical PIT or formal use")
        if row["raw_archive_policy"] != "external_content_addressed_archive_required":
            errors.append(f"{row['source_id']}: official source evidence must be archived externally")
        if not row["official_url"].startswith(
            ("https://mopsov.twse.com.tw/", "https://www.twse.com.tw/")
        ):
            errors.append(f"{row['source_id']}: source must be an official MOPS or TWSE URL")
        if not row["blocker"]:
            errors.append(f"{row['source_id']}: blocker is required")
    if {row["period"] for row in pilots} != {"2013Q1", "2025Q1"}:
        errors.append("pilot must cover 2013Q1 and a modern quarter")
    if len({row["period"] for row in pilots}) != len(pilots):
        errors.append("historical PIT pilot periods must be unique")
    for row in pilots:
        label = row["period"]
        if not re.fullmatch(r"[0-9a-f]{64}", row["raw_payload_sha256"]):
            errors.append(f"{label}: raw archive SHA-256 is invalid")
        if int(row["member_count"]) <= 0 or int(row["archive_bytes"]) <= 0:
            errors.append(f"{label}: archive evidence is empty")
        for schema in ("ci=", "basi=", "bd=", "fh=", "ins=", "mim="):
            if schema not in row["schema_counts"]:
                errors.append(f"{label}: missing schema pilot {schema}")
        if "cr=" not in row["scope_counts"] or "ir=" not in row["scope_counts"]:
            errors.append(f"{label}: consolidated and individual scope coverage is required")
        for stock in ("2330:ci:cr", "5347:ci:cr", "2881:fh:cr", "2816:ins:ir"):
            if stock not in row["pilot_instances"]:
                errors.append(f"{label}: missing cross-market or cross-industry pilot {stock}")
        if row["pit_eligible"] != "False" or row["formal_model_use_allowed"] != "False":
            errors.append(f"{label}: pilot must remain fail closed")
    required_visible_uploads = {
        ("2013Q1", "2330"): ("2013-05-15T14:26:07+08:00", "ci", "cr", "201301_2330_AI1.pdf", "8521042ec753b3d2395f6afdf5c38e0e135734c031c27db67c8022c16fab33d9"),
        ("2013Q1", "5347"): ("2013-05-06T14:04:13+08:00", "ci", "cr", "201301_5347_AI1.pdf", "4cd786421ee144e80e5e274fc7e895dd57b119f21b21d138c7d2306682690622"),
        ("2013Q1", "2881"): ("2013-05-30T09:46:03+08:00", "fh", "cr", "201301_2881_AI1.pdf", "e3c4b9abe341f0391a1f41afc1fbe9b853970c30875fea49a0fb9e395c0d84af"),
        ("2013Q1", "2816"): ("2013-04-30T14:58:52+08:00", "ins", "ir", "201301_2816_AI2.pdf", "83fc61b4a444c132ba9e4c5ea7c7af4d1cbadcff97905bc63a1c9a9bdd2e2b74"),
        ("2025Q1", "2330"): ("2025-05-15T13:40:15+08:00", "ci", "cr", "202501_2330_AI1.pdf", "cfe39d9ba137ca012caf74ebddfdb30aba1f00b7d34e9141941a8649036f3878"),
        ("2025Q1", "5347"): ("2025-05-06T13:48:16+08:00", "ci", "cr", "202501_5347_AI1.pdf", "dcd2cc6710219df67a31c34f34c91938423e17a18c31f09baa6a0bfcaa0d23cf"),
        ("2025Q1", "2881"): ("2025-05-29T16:03:54+08:00", "fh", "cr", "202501_2881_AI1.pdf", "4e17588aff0088db3a3ea6546b6f4d4001b61310aad4fc354ec9994ea6d18e7e"),
        ("2025Q1", "2816"): ("2025-05-12T12:22:03+08:00", "ins", "ir", "202501_2816_AI2.pdf", "71ef7f2d5c6e637943e4936467b4101556738850bc96469ceb90a3bd9c15221a"),
    }
    witness_by_id = {row["witness_id"]: row for row in evidence}
    if len(witness_by_id) != len(evidence):
        errors.append("historical PIT evidence witness ids must be unique")
    upload_rows = {
        (row["period"], row["company_id"]): row
        for row in evidence
        if row["witness_type"] == "visible_pdf_upload"
    }
    if set(upload_rows) != set(required_visible_uploads):
        errors.append("t57 upload witnesses must cover both periods and all four market-industry-scope probes")
    for key, expected in required_visible_uploads.items():
        row = upload_rows.get(key)
        if row is None:
            continue
        upload_at, schema, scope, filename, response_sha = expected
        if (
            row["document_visible_upload_at"],
            row["industry_schema"],
            row["report_scope"],
            row["canonical_filename"],
        ) != expected[:4]:
            errors.append(f"{row['witness_id']}: t57 upload witness contract drift")
        if row["market"] != ("otc" if row["company_id"] == "5347" else "sii"):
            errors.append(f"{row['witness_id']}: market witness drift")
        if not re.fullmatch(r"[0-9a-f]{64}", row["primary_response_sha256"]):
            errors.append(f"{row['witness_id']}: response SHA-256 is invalid")
        if row["primary_response_sha256"] != response_sha:
            errors.append(f"{row['witness_id']}: pinned t57 response SHA-256 drift")
        if "t57sb01" not in row["official_url"] or "co_id=" not in row["request_contracts"]:
            errors.append(f"{row['witness_id']}: reproducible t57 request contract is required")
    for row in evidence:
        witness_id = row["witness_id"]
        if row["pit_eligible"] != "False" or row["formal_model_use_allowed"] != "False":
            errors.append(f"{witness_id}: evidence witness must remain fail closed")
        if not row["public_version_visibility"].startswith("one_current_canonical_filename"):
            errors.append(f"{witness_id}: public version visibility must remain explicit")
        try:
            datetime.fromisoformat(row["captured_at"])
        except ValueError:
            errors.append(f"{witness_id}: captured_at must be an ISO-8601 timestamp")
    required_archive_columns = {
        "archive_id",
        "related_record_ids",
        "period",
        "payload_role",
        "source_id",
        "official_url",
        "request_contract",
        "captured_at",
        "official_public_at",
        "availability_precision",
        "external_archive_root_id",
        "external_archive_relative_path",
        "raw_archive_ref",
        "raw_payload_sha256",
        "raw_byte_count",
        "media_type",
        "archive_status",
        "pit_eligible",
        "formal_model_use_allowed",
        "notes",
    }
    if not raw_archives or set(raw_archives[0]) != required_archive_columns:
        errors.append("historical PIT raw archive manifest schema is invalid")
    raw_by_id = {row["archive_id"]: row for row in raw_archives}
    if len(raw_by_id) != len(raw_archives):
        errors.append("historical PIT raw archive ids must be unique")
    required_archive_ids = {
        "bulk_xbrl_2013Q1",
        "bulk_xbrl_2025Q1",
        "t57_2330_2013Q1",
        "t57_5347_2013Q1",
        "t57_2881_2013Q1",
        "t57_2816_2013Q1",
        "t05_2816_2013Q1_correction",
        "t56_2816_2013Q1_correction",
        "t57_pdf_2816_2013Q1",
        "t57_2330_2025Q1",
        "t57_5347_2025Q1",
        "t57_2881_2025Q1",
        "t57_2816_2025Q1",
        "t05_4552_2025Q1_initial",
        "t05_4552_2025Q1_correction",
        "t56_4552_2025Q1_correction",
        "t57_4552_2025Q1",
        "t57_pdf_4552_2025Q1",
        "xbrl_4552_2025Q1_current",
        "twse_correction_guidance",
    }
    if set(raw_by_id) != required_archive_ids:
        errors.append("historical PIT raw archive manifest must retain all 20 source payloads")
    expected_payload_hashes = {row["raw_payload_sha256"] for row in pilots}
    for row in evidence:
        expected_payload_hashes.add(row["primary_response_sha256"])
        expected_payload_hashes.update(
            re.findall(r"=([0-9a-f]{64})(?:;|$)", row["corroborating_sha256s"])
        )
        if row["current_payload_sha256"]:
            expected_payload_hashes.add(row["current_payload_sha256"])
    guidance_sha = "7c5502cbcd4eab7f391c40e24a5375b1b8f9a4cea8e3aa345c674623d595cd1e"
    expected_payload_hashes.add(guidance_sha)
    manifest_payload_hashes = {row["raw_payload_sha256"] for row in raw_archives}
    if manifest_payload_hashes != expected_payload_hashes:
        errors.append("raw archive SHA set must equal pilot evidence and guidance payload lineage")
    source_ids = {row["source_id"] for row in sources}
    related_ids = (
        {row["archive_file"] for row in pilots}
        | {row["witness_id"] for row in evidence}
        | source_ids
    )
    archive_relative_paths: set[str] = set()
    for row in raw_archives:
        archive_id = row["archive_id"]
        digest = row["raw_payload_sha256"]
        relative = row["external_archive_relative_path"]
        if row["source_id"] not in source_ids:
            errors.append(f"{archive_id}: raw archive source_id is not registered")
        if not row["official_url"].startswith(
            (
                "https://mopsov.twse.com.tw/",
                "https://doc.twse.com.tw/",
                "https://www.twse.com.tw/",
            )
        ):
            errors.append(f"{archive_id}: raw archive must reference an official URL")
        for related in row["related_record_ids"].split(";"):
            if related not in related_ids:
                errors.append(f"{archive_id}: raw archive related record is not registered: {related}")
        if not re.fullmatch(r"[0-9a-f]{64}", digest):
            errors.append(f"{archive_id}: raw archive SHA-256 is invalid")
        if row["raw_archive_ref"] != f"sha256://{digest}":
            errors.append(f"{archive_id}: raw archive ref must bind the full SHA-256")
        if row["external_archive_root_id"] != (
            "codex_data_archives_taiwan_stock_financial_statement_historical_pit_"
            "source_audit_v1"
        ):
            errors.append(f"{archive_id}: external archive root id drift")
        if Path(relative).name != relative or digest[:16] not in relative:
            errors.append(f"{archive_id}: external archive relative locator is invalid")
        if relative in archive_relative_paths:
            errors.append(f"{archive_id}: external archive relative locator is duplicated")
        archive_relative_paths.add(relative)
        try:
            if int(row["raw_byte_count"]) <= 0:
                raise ValueError
        except ValueError:
            errors.append(f"{archive_id}: raw byte count must be positive")
        try:
            datetime.fromisoformat(row["captured_at"])
        except ValueError:
            errors.append(f"{archive_id}: captured_at must be ISO-8601")
        if row["archive_status"] != "external_content_addressed_archive_verified":
            errors.append(f"{archive_id}: archive status must remain verified")
        if row["pit_eligible"] != "False" or row["formal_model_use_allowed"] != "False":
            errors.append(f"{archive_id}: retained raw evidence cannot authorize formal use")
    if external_archive_root is not None:
        errors.extend(validate_external_archive_files(raw_archives, external_archive_root))
    historical_revision = witness_by_id.get("2013Q1_2816_ir_revision")
    if historical_revision is None:
        errors.append("missing 2816 2013Q1 revision witness")
    else:
        expected_historical_times = (
            "2013-04-30T14:58:52+08:00",
            "2013-05-16T18:53:38+08:00",
        )
        if (
            historical_revision["document_visible_upload_at"],
            historical_revision["revision_public_at"],
        ) != expected_historical_times:
            errors.append("2013Q1_2816_ir_revision: official timestamp pin drift")
        upload_witness = upload_rows.get(("2013Q1", "2816"))
        if upload_witness and historical_revision["document_visible_upload_at"] != upload_witness["document_visible_upload_at"]:
            errors.append("2013Q1_2816_ir_revision: upload time disagrees with t57 witness")
        if historical_revision["primary_response_sha256"] != "cdeda2e1ae85b03409a2025f58d23c06d27b5e5647e5e0cacf9bf90a793035b1":
            errors.append("2013Q1_2816_ir_revision: pinned t05 response SHA-256 drift")
        if historical_revision["current_payload_sha256"] != "df3bd64b27dfc2bf53a75f1560a152aed7361d2ba8ee9605715ed81709470e0b":
            errors.append("2013Q1_2816_ir_revision: pinned current PDF SHA-256 drift")
        expected_corroborating = (
            "t57=83fc61b4a444c132ba9e4c5ea7c7af4d1cbadcff97905bc63a1c9a9bdd2e2b74;"
            "t56=eb101c71b11be2e79fccba32c22843f5b4f224bed9e9ea86ffe08f3c96af0f23;"
            "pdf=df3bd64b27dfc2bf53a75f1560a152aed7361d2ba8ee9605715ed81709470e0b"
        )
        if historical_revision["corroborating_sha256s"] != expected_corroborating:
            errors.append("2013Q1_2816_ir_revision: corroborating lineage SHA-256 drift")
        try:
            if not (
                datetime.fromisoformat(historical_revision["document_visible_upload_at"])
                < datetime.fromisoformat(historical_revision["revision_public_at"])
            ):
                errors.append(
                    "2013Q1_2816_ir_revision: visible document upload must precede correction"
                )
        except ValueError:
            errors.append("2013Q1_2816_ir_revision: invalid official timestamp")
        for required in ("spoke_date=20130516", "spoke_time=185338", "seq_no=1", "YEAR_SEASON=201301"):
            if required not in historical_revision["request_contracts"]:
                errors.append(f"2013Q1_2816_ir_revision: missing replay key {required}")
    leakage = witness_by_id.get("2025Q1_4552_cr_revision_leakage")
    if leakage is None:
        errors.append("missing 4552 2025Q1 revision-leakage witness")
    else:
        expected_leakage_times = (
            "2025-05-13T13:59:37+08:00",
            "2025-05-13T15:22:01+08:00",
            "2025-05-16T15:06:12+08:00",
        )
        if (
            leakage["metric_initial_public_at"],
            leakage["document_visible_upload_at"],
            leakage["revision_public_at"],
        ) != expected_leakage_times:
            errors.append("4552 revision-leakage official timestamp pin drift")
        if (leakage["metric_name"], leakage["initial_value"], leakage["revision_value"], leakage["current_visible_value"]) != ("basic_eps", "0.63", "0.65", "0.65"):
            errors.append("4552 revision-leakage EPS states must remain 0.63 -> 0.65 -> 0.65")
        try:
            if not (
                datetime.fromisoformat(leakage["metric_initial_public_at"])
                < datetime.fromisoformat(leakage["document_visible_upload_at"])
                < datetime.fromisoformat(leakage["revision_public_at"])
            ):
                errors.append("4552 revision-leakage official timestamp ordering is invalid")
        except ValueError:
            errors.append("4552 revision-leakage witness has an invalid official timestamp")
        if leakage["canonical_filename"] != "202501_4552_AI1.pdf":
            errors.append("4552 revision-leakage canonical filename drift")
        for required in (
            "spoke_date=20250513",
            "spoke_time=135937",
            "seq_no=2",
            "spoke_date=20250516",
            "spoke_time=150612",
            "seq_no=1",
            "YEAR_SEASON=202501",
            "report_id=C",
        ):
            if required not in leakage["request_contracts"]:
                errors.append(f"4552 revision-leakage witness missing replay key {required}")
        for field in ("primary_response_sha256", "current_payload_sha256"):
            if not re.fullmatch(r"[0-9a-f]{64}", leakage[field]):
                errors.append(f"4552 revision-leakage {field} is invalid")
        if leakage["primary_response_sha256"] != "21aab3bf2402bd1ebf4dfdaf6eb3f7aa2b6ddb19e42e5baa635aa41ba45ed16a":
            errors.append("4552 revision-leakage initial t05 SHA-256 drift")
        if leakage["current_payload_sha256"] != "8d23008d8565964acf1c784102411a5e7217d86849ed239001740448c611f277":
            errors.append("4552 revision-leakage current XBRL SHA-256 drift")
        expected_corroborating = (
            "t05_revision=beed0b027b4b677f63d2c61ee713032d85adcfca0e5c70ede7bd2cca62fc07c7;"
            "t56=ec66623bbe9d3ed2975317743339acaa5a26dc1ce72976193195244a565832b0;"
            "t57=34d6b6a44dab3dc1f2b1beb27ffef5b4243c70cd62c22a9ebc404d9a2eaff91e;"
            "pdf=99a7320d1c22d35c0b88166655f6912b6da26f53869ca1f0276afaa42cd20fd4"
        )
        if leakage["corroborating_sha256s"] != expected_corroborating:
            errors.append("4552 revision-leakage corroborating lineage SHA-256 drift")
        corroborating = re.findall(r"=([0-9a-f]{64})(?:;|$)", leakage["corroborating_sha256s"])
        if len(corroborating) != 4:
            errors.append("4552 revision-leakage witness requires t05 revision t56 t57 and PDF hashes")
    expected_records = len(sources) + len(pilots) + len(evidence) + len(raw_archives)
    if len(audit) != expected_records:
        errors.append("generated source audit row count mismatch")
    if {row["audit_id"] for row in audit} != {"financial_statement_historical_pit_source_audit_v2"}:
        errors.append("generated source audit must use the v2 availability and revision contract")
    audit_by_type = {
        record_type: {row["record_id"]: row for row in audit if row["record_type"] == record_type}
        for record_type in (
            "source_surface",
            "pilot_archive",
            "evidence_witness",
            "raw_archive",
        )
    }
    if set(audit_by_type["source_surface"]) != {row["source_id"] for row in sources}:
        errors.append("generated source-surface audit rows drift from the source registry")
    if set(audit_by_type["pilot_archive"]) != {row["archive_file"] for row in pilots}:
        errors.append("generated pilot audit rows drift from the pilot registry")
    if set(audit_by_type["evidence_witness"]) != set(witness_by_id):
        errors.append("generated evidence rows drift from the witness registry")
    if set(audit_by_type["raw_archive"]) != set(raw_by_id):
        errors.append("generated raw archive rows drift from the archive manifest")
    for witness_id, witness in witness_by_id.items():
        generated = audit_by_type["evidence_witness"].get(witness_id)
        if generated is None:
            continue
        expected_sha = witness["current_payload_sha256"] or witness["primary_response_sha256"]
        if generated["raw_payload_sha256"] != expected_sha:
            errors.append(f"{witness_id}: generated witness SHA drift")
        for required in (witness["request_contracts"], witness["primary_response_sha256"], witness["captured_at"]):
            if required not in generated["revision_evidence"]:
                errors.append(f"{witness_id}: generated witness lineage is incomplete")
    for archive_id, archive in raw_by_id.items():
        generated = audit_by_type["raw_archive"].get(archive_id)
        if generated is None:
            continue
        if generated["raw_payload_sha256"] != archive["raw_payload_sha256"]:
            errors.append(f"{archive_id}: generated raw archive SHA drift")
        for required in (
            archive["raw_archive_ref"],
            archive["external_archive_relative_path"],
            archive["archive_status"],
        ):
            if required not in (
                generated["availability_evidence"]
                + generated["revision_evidence"]
                + generated["scope_evidence"]
            ):
                errors.append(f"{archive_id}: generated raw archive locator is incomplete")
        generated_availability = {
            part.split("=", 1)[0]: part.split("=", 1)[1]
            for part in generated["availability_evidence"].split(";")
            if "=" in part
        }
        if generated_availability.get("raw_byte_count") != archive["raw_byte_count"]:
            errors.append(f"{archive_id}: generated raw archive byte count drift")
    for relative in (OUTPUT_CSV, OUTPUT_MD, DOCS_CSV, DOCS_MD):
        if not (root / relative.relative_to(ROOT)).is_file():
            errors.append(f"missing generated source audit artifact: {relative.relative_to(ROOT).as_posix()}")
    if (root / OUTPUT_CSV.relative_to(ROOT)).read_bytes() != (root / DOCS_CSV.relative_to(ROOT)).read_bytes():
        errors.append("source audit CSV docs mirror drift")
    if (root / OUTPUT_MD.relative_to(ROOT)).read_bytes() != (root / DOCS_MD.relative_to(ROOT)).read_bytes():
        errors.append("source audit Markdown docs mirror drift")
    md = (root / DOCS_MD.relative_to(ROOT)).read_text(encoding="utf-8")
    for required in (
        "pit_eligible=False",
        "formal_model_use_allowed=False",
        "ReviewAuditDate",
        "revenue_unreacted_range",
        "actual public availability",
        "2025-04-07 onward",
        "2013Q1 archive is an earliest-IFRS source-contract probe",
        "initial=0.63;revision=0.65;current_visible=0.65",
        "one canonical filename",
        "public reproducible contract is insufficient",
        "current_visible_xbrl_value_cannot_be_assigned_to_initial_public_time",
        "twse_financial_report_correction_guidance",
        "deleting the uploaded electronic book before uploading its replacement",
        "external_content_addressed_archive_verified",
        "codex_data_archives_taiwan_stock_financial_statement_historical_pit_source_audit_v1",
        guidance_sha,
    ):
        if required not in md:
            errors.append(f"source audit Markdown missing fail-closed evidence: {required}")
    return errors


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--external-archive-root", type=Path)
    args = parser.parse_args()
    errors = validate(external_archive_root=args.external_archive_root)
    if errors:
        raise SystemExit("\n".join(f"- {error}" for error in errors))
    print("financial statement historical PIT source audit passed: pit_eligible=False formal_model_use_allowed=False")


if __name__ == "__main__":
    main()
