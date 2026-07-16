from __future__ import annotations

import argparse
import csv
import hashlib
import re
import zipfile
from datetime import datetime
from pathlib import Path, PurePosixPath


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

EXPECTED_ARCHIVE_SHA256_BY_ID = {
    "bulk_xbrl_2013Q1": "f6974e00aec749a3486d7944871fbe299129bdfe4107f1f4453699272b266f16",
    "bulk_xbrl_2025Q1": "975c3439879d92bb336476f0691cc0547108b19603d06940439963c5fba1cb11",
    "t57_2330_2013Q1": "8521042ec753b3d2395f6afdf5c38e0e135734c031c27db67c8022c16fab33d9",
    "t57_5347_2013Q1": "4cd786421ee144e80e5e274fc7e895dd57b119f21b21d138c7d2306682690622",
    "t57_2881_2013Q1": "e3c4b9abe341f0391a1f41afc1fbe9b853970c30875fea49a0fb9e395c0d84af",
    "t57_2816_2013Q1": "83fc61b4a444c132ba9e4c5ea7c7af4d1cbadcff97905bc63a1c9a9bdd2e2b74",
    "t05_2816_2013Q1_correction": "cdeda2e1ae85b03409a2025f58d23c06d27b5e5647e5e0cacf9bf90a793035b1",
    "t56_2816_2013Q1_correction": "eb101c71b11be2e79fccba32c22843f5b4f224bed9e9ea86ffe08f3c96af0f23",
    "t57_pdf_2816_2013Q1": "df3bd64b27dfc2bf53a75f1560a152aed7361d2ba8ee9605715ed81709470e0b",
    "t57_2330_2025Q1": "cfe39d9ba137ca012caf74ebddfdb30aba1f00b7d34e9141941a8649036f3878",
    "t57_5347_2025Q1": "dcd2cc6710219df67a31c34f34c91938423e17a18c31f09baa6a0bfcaa0d23cf",
    "t57_2881_2025Q1": "4e17588aff0088db3a3ea6546b6f4d4001b61310aad4fc354ec9994ea6d18e7e",
    "t57_2816_2025Q1": "71ef7f2d5c6e637943e4936467b4101556738850bc96469ceb90a3bd9c15221a",
    "t05_4552_2025Q1_initial": "21aab3bf2402bd1ebf4dfdaf6eb3f7aa2b6ddb19e42e5baa635aa41ba45ed16a",
    "t05_4552_2025Q1_correction": "beed0b027b4b677f63d2c61ee713032d85adcfca0e5c70ede7bd2cca62fc07c7",
    "t56_4552_2025Q1_correction": "ec66623bbe9d3ed2975317743339acaa5a26dc1ce72976193195244a565832b0",
    "t57_4552_2025Q1": "34d6b6a44dab3dc1f2b1beb27ffef5b4243c70cd62c22a9ebc404d9a2eaff91e",
    "t57_pdf_4552_2025Q1": "99a7320d1c22d35c0b88166655f6912b6da26f53869ca1f0276afaa42cd20fd4",
    "xbrl_4552_2025Q1_current": "8d23008d8565964acf1c784102411a5e7217d86849ed239001740448c611f277",
    "twse_correction_guidance": "7c5502cbcd4eab7f391c40e24a5375b1b8f9a4cea8e3aa345c674623d595cd1e",
    "t56_attachment_2816_2013Q1": "899a2483f1d50277e5f4967aa45bd971b7cf373de57d672b62f9a6af467348be",
    "t56_attachment_4552_2025Q1": "24382f38ae0fb50a6894d82495b519b69ce0174c6e5ce783f83223a70b89e325",
    "twse_openapi_swagger": "2c2cecccb7a220ac9e263228a7659aa49b1ada5aea397650e601ad3dfcc48043",
    "twse_openapi_L_ci_2026Q1": "31c1e47fd73e5c3597638d0f596e900bee09b41bc96c54c6eea6a2b95f0eef52",
    "t05_api_2348_2026Q1_may": "0dbb39dd202f85c5ac07297e74b4abcdd6f0898870538622e77afe5f7c50b94e",
    "t05_api_2348_2026Q1_june": "908fd10b49709f985bbd287de9ef605a38a2fb93b8243183d653c0f415ca150f",
    "t05_api_2348_2026Q1_revision1": "1df555073fa7fcd00322e4c7c9d727708a7785346d0554b3b4b7b3f289db0f02",
    "t05_api_2348_2026Q1_revision2": "c0890a8ce48fe442c7b9a5d730e922512e5fc7443c318eb372a6ea57536ddcd7",
    "t163_api_2348_2026Q1_current": "dacb680b6ef561f7e54d77a526d29d6033935d0573864ad5bf1961e5c9c13fb7",
    "t57_2348_2026Q1": "3104c04f8010c23025ada1a1a7ec52aa7bf6ef3f2e78d3d4eb6422eb1f0cb270",
    "t56_2348_2026Q1_skey1": "b7409343461930b00d4ce1084e3eb398c66ea25fcd74cce2b079c9c96b0b0d47",
    "t56_2348_2026Q1_skey2": "8bca6f829d136a5455697c47a85449ff8cff2db527c1cd86b4dfce708029974c",
    "t56_attachment_2348_2026Q1_skey1": "a1ab34ca2649193ebde5c717657fd0d471ef299525fe089a283ca9c9737822ca",
    "t56_attachment_2348_2026Q1_skey2": "0ffcb2b64dd452aea6d3a20119a2e03a45ad76fbb38e9ba1fc1de9fd5548067e",
    "xbrl_2348_2026Q1_current": "b2e2852b47d751bfe352925c75882d016124ed6a5bff6fd4d6964b4741efd534",
    "bulk_xbrl_2026Q1": "6d1423056561dfcff07b7f720c0f1d4416fce3f0b11bcd47c254ed88557d0e10",
}


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

    raw_by_id = {row["archive_id"]: row for row in raw_archives}
    bulk = raw_by_id.get("bulk_xbrl_2026Q1")
    direct = raw_by_id.get("xbrl_2348_2026Q1_current")
    if bulk is not None and direct is not None:
        bulk_path = external_archive_root / bulk["external_archive_relative_path"]
        direct_path = external_archive_root / direct["external_archive_relative_path"]
        if bulk_path.is_file() and direct_path.is_file():
            expected_member_name = "tifrs-fr1-m1-ci-cr-2348-2026Q1.html"
            try:
                with zipfile.ZipFile(bulk_path) as archive:
                    matching = [
                        info
                        for info in archive.infolist()
                        if PurePosixPath(info.filename).name == expected_member_name
                    ]
                    if len(matching) != 1 or matching[0].filename != expected_member_name:
                        errors.append(
                            "bulk_xbrl_2026Q1: expected exactly one 2348 2026Q1 member"
                        )
                    else:
                        member_bytes = archive.read(matching[0])
                        member_sha256 = hashlib.sha256(member_bytes).hexdigest()
                        if len(member_bytes) != int(direct["raw_byte_count"]):
                            errors.append(
                                "bulk_xbrl_2026Q1: 2348 member byte count differs from direct payload"
                            )
                        if member_sha256 != direct["raw_payload_sha256"]:
                            errors.append(
                                "bulk_xbrl_2026Q1: 2348 member SHA-256 differs from direct payload"
                            )
                        if member_bytes != direct_path.read_bytes():
                            errors.append(
                                "bulk_xbrl_2026Q1: 2348 member bytes differ from direct payload"
                            )
            except (OSError, ValueError, zipfile.BadZipFile) as exc:
                errors.append(f"bulk_xbrl_2026Q1: cannot verify 2348 member: {exc}")
    return errors


def _evidence_lineage_hashes(row: dict[str, str]) -> set[str]:
    hashes = {row["primary_response_sha256"]}
    hashes.update(re.findall(r"=([0-9a-f]{64})(?:;|$)", row["corroborating_sha256s"]))
    if row["current_payload_sha256"]:
        hashes.add(row["current_payload_sha256"])
    return hashes


def validate_archive_lineage_bindings(
    pilots: list[dict[str, str]],
    evidence: list[dict[str, str]],
    raw_archives: list[dict[str, str]],
) -> list[str]:
    errors: list[str] = []
    lineage_rows: dict[str, list[dict[str, str]]] = {}
    for archive in raw_archives:
        expected_sha256 = EXPECTED_ARCHIVE_SHA256_BY_ID.get(archive["archive_id"])
        if expected_sha256 is None:
            errors.append(f"{archive['archive_id']}: archive id has no pinned SHA-256 lineage")
        elif archive["raw_payload_sha256"] != expected_sha256:
            errors.append(f"{archive['archive_id']}: archive id to SHA-256 lineage drift")
        for related_id in archive["related_record_ids"].split(";"):
            lineage_rows.setdefault(related_id, []).append(archive)

    for pilot in pilots:
        record_id = pilot["archive_file"]
        related = lineage_rows.get(record_id, [])
        actual_hashes = {row["raw_payload_sha256"] for row in related}
        expected_hashes = {pilot["raw_payload_sha256"]}
        if actual_hashes != expected_hashes or len(related) != 1:
            errors.append(f"{record_id}: pilot archive payload lineage does not match manifest row")
            continue
        archive = related[0]
        if (
            archive["raw_byte_count"] != pilot["archive_bytes"]
            or archive["captured_at"] != pilot["captured_at"]
            or archive["period"] != pilot["period"]
        ):
            errors.append(f"{record_id}: pilot archive metadata lineage does not match manifest row")

    for witness in evidence:
        witness_id = witness["witness_id"]
        related = lineage_rows.get(witness_id, [])
        actual_hashes = {row["raw_payload_sha256"] for row in related}
        expected_hashes = _evidence_lineage_hashes(witness)
        if actual_hashes != expected_hashes or len(related) != len(expected_hashes):
            errors.append(f"{witness_id}: evidence payload lineage does not match manifest rows")
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
        "twse_openapi_financial_statement_current_snapshot",
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
            (
                "https://mopsov.twse.com.tw/",
                "https://mops.twse.com.tw/",
                "https://www.twse.com.tw/",
                "https://openapi.twse.com.tw/",
            )
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
        if not row["public_version_visibility"].startswith(
            (
                "one_current_canonical_filename",
                "one_current_bulk_member",
                "one_current_dataset_snapshot",
            )
        ):
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
    required_archive_ids = set(EXPECTED_ARCHIVE_SHA256_BY_ID)
    if set(raw_by_id) != required_archive_ids:
        errors.append("historical PIT raw archive manifest must retain all 36 source payloads")
    expected_payload_hashes = {row["raw_payload_sha256"] for row in pilots}
    for row in evidence:
        expected_payload_hashes.update(_evidence_lineage_hashes(row))
    guidance_sha = "7c5502cbcd4eab7f391c40e24a5375b1b8f9a4cea8e3aa345c674623d595cd1e"
    expected_payload_hashes.add(guidance_sha)
    manifest_payload_hashes = {row["raw_payload_sha256"] for row in raw_archives}
    if manifest_payload_hashes != expected_payload_hashes:
        errors.append("raw archive SHA set must equal pilot evidence and guidance payload lineage")
    errors.extend(validate_archive_lineage_bindings(pilots, evidence, raw_archives))
    guidance_rows = [
        row
        for row in raw_archives
        if "twse_financial_report_correction_guidance"
        in row["related_record_ids"].split(";")
    ]
    if (
        len(guidance_rows) != 1
        or guidance_rows[0]["archive_id"] != "twse_correction_guidance"
        or guidance_rows[0]["raw_payload_sha256"] != guidance_sha
    ):
        errors.append("official correction guidance payload lineage does not match manifest row")
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
                "https://mops.twse.com.tw/",
                "https://doc.twse.com.tw/",
                "https://www.twse.com.tw/",
                "https://openapi.twse.com.tw/",
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

    expected_correction_attachments = {
        "t56_attachment_2816_2013Q1": (
            "899a2483f1d50277e5f4967aa45bd971b7cf373de57d672b62f9a6af467348be",
            "300050",
            "Eleven nonconsecutive selected report pages",
        ),
        "t56_attachment_4552_2025Q1": (
            "24382f38ae0fb50a6894d82495b519b69ce0174c6e5ce783f83223a70b89e325",
            "734170",
            "Two selected corrected report pages",
        ),
        "t56_attachment_2348_2026Q1_skey1": (
            "a1ab34ca2649193ebde5c717657fd0d471ef299525fe089a283ca9c9737822ca",
            "537872",
            "One replacement page numbered 42",
        ),
        "t56_attachment_2348_2026Q1_skey2": (
            "0ffcb2b64dd452aea6d3a20119a2e03a45ad76fbb38e9ba1fc1de9fd5548067e",
            "79988",
            "Two replacement pages numbered 42 and 45",
        ),
    }
    for archive_id, (digest, byte_count, note_token) in expected_correction_attachments.items():
        row = raw_by_id.get(archive_id)
        if row is None:
            errors.append(f"{archive_id}: missing correction attachment archive")
            continue
        if (
            row["raw_payload_sha256"] != digest
            or row["raw_byte_count"] != byte_count
            or row["media_type"] != "application/pdf"
        ):
            errors.append(f"{archive_id}: pinned correction attachment contract drift")
        if (
            row["payload_role"] != "financial_report_correction_attachment_selected_pages"
            or row["availability_precision"] != "correction_attachment_link_date_only_not_filed_at"
            or note_token not in row["notes"]
        ):
            errors.append(f"{archive_id}: correction attachment must remain selected-page evidence only")

    openapi_source = next(
        (
            row
            for row in sources
            if row["source_id"] == "twse_openapi_financial_statement_current_snapshot"
        ),
        None,
    )
    if openapi_source is None:
        errors.append("missing TWSE OpenAPI current-snapshot source contract")
    elif (
        openapi_source["status"] != "current_snapshot_only_not_historical_pit"
        or "not company filed_at" not in openapi_source["availability_semantics"]
        or "no company revision id or version selector" not in openapi_source["revision_semantics"]
    ):
        errors.append("TWSE OpenAPI source must remain current-snapshot-only")

    openapi_witness = witness_by_id.get("2026Q1_twse_openapi_L_ci_snapshot")
    if openapi_witness is None:
        errors.append("missing TWSE OpenAPI current-snapshot witness")
    else:
        if (
            openapi_witness["primary_response_sha256"]
            != "31c1e47fd73e5c3597638d0f596e900bee09b41bc96c54c6eea6a2b95f0eef52"
            or openapi_witness["corroborating_sha256s"]
            != "swagger=2c2cecccb7a220ac9e263228a7659aa49b1ada5aea397650e601ad3dfcc48043"
        ):
            errors.append("TWSE OpenAPI payload and Swagger hashes drift")
        if (
            openapi_witness["company_id"],
            openapi_witness["industry_schema"],
            openapi_witness["report_scope"],
        ) != ("all_listed", "ci", "cr_current_snapshot"):
            errors.append("TWSE OpenAPI witness scope drift")
        if openapi_witness["conclusion"] != (
            "dataset_output_date_is_not_company_fact_availability_or_revision_lineage"
        ):
            errors.append("TWSE OpenAPI witness must remain fail closed")

    expected_2348_revisions = {
        "2026Q1_2348_cr_revision_1": (
            "2026-05-25T15:59:11+08:00",
            "1df555073fa7fcd00322e4c7c9d727708a7785346d0554b3b4b7b3f289db0f02",
            "t05_list=0dbb39dd202f85c5ac07297e74b4abcdd6f0898870538622e77afe5f7c50b94e;"
            "t56=b7409343461930b00d4ce1084e3eb398c66ea25fcd74cce2b079c9c96b0b0d47;"
            "t56_attachment=a1ab34ca2649193ebde5c717657fd0d471ef299525fe089a283ca9c9737822ca",
            "SKEY=1",
        ),
        "2026Q1_2348_cr_revision_2": (
            "2026-06-03T15:38:46+08:00",
            "c0890a8ce48fe442c7b9a5d730e922512e5fc7443c318eb372a6ea57536ddcd7",
            "t05_list=908fd10b49709f985bbd287de9ef605a38a2fb93b8243183d653c0f415ca150f;"
            "t56=8bca6f829d136a5455697c47a85449ff8cff2db527c1cd86b4dfce708029974c;"
            "t56_attachment=0ffcb2b64dd452aea6d3a20119a2e03a45ad76fbb38e9ba1fc1de9fd5548067e",
            "SKEY=2",
        ),
    }
    for witness_id, (revision_time, primary_sha, corroborating, skey) in expected_2348_revisions.items():
        row = witness_by_id.get(witness_id)
        if row is None:
            errors.append(f"missing 2348 revision witness: {witness_id}")
            continue
        if (
            row["company_id"],
            row["market"],
            row["industry_schema"],
            row["report_scope"],
        ) != ("2348", "sii", "ci", "cr"):
            errors.append(f"{witness_id}: market scope or schema drift")
        if (
            row["document_visible_upload_at"] != "2026-05-15T16:02:11+08:00"
            or row["revision_public_at"] != revision_time
            or row["primary_response_sha256"] != primary_sha
            or row["corroborating_sha256s"] != corroborating
        ):
            errors.append(f"{witness_id}: pinned revision time or payload lineage drift")
        if skey not in row["request_contracts"] or "t05_detail:POST JSON" not in row["request_contracts"]:
            errors.append(f"{witness_id}: reproducible t05 and t56 requests are required")

    current_2348 = witness_by_id.get(
        "2026Q1_2348_cr_current_snapshot_after_two_revisions"
    )
    if current_2348 is None:
        errors.append("missing 2348 post-revision current-snapshot witness")
    else:
        if current_2348["primary_response_sha256"] != (
            "dacb680b6ef561f7e54d77a526d29d6033935d0573864ad5bf1961e5c9c13fb7"
        ):
            errors.append("2348 current t163 response hash drift")
        if current_2348["corroborating_sha256s"] != (
            "t57=3104c04f8010c23025ada1a1a7ec52aa7bf6ef3f2e78d3d4eb6422eb1f0cb270;"
            "bulk=6d1423056561dfcff07b7f720c0f1d4416fce3f0b11bcd47c254ed88557d0e10"
        ):
            errors.append("2348 current t57 or bulk lineage hash drift")
        if current_2348["current_payload_sha256"] != (
            "b2e2852b47d751bfe352925c75882d016124ed6a5bff6fd4d6964b4741efd534"
        ):
            errors.append("2348 direct current XBRL hash drift")
        if current_2348["conclusion"] != (
            "bulk_and_direct_are_identical_current_snapshot_bytes_after_two_revisions_not_version_history"
        ):
            errors.append("2348 bulk/direct witness must remain current-snapshot-only")

    bulk_2348 = raw_by_id.get("bulk_xbrl_2026Q1")
    direct_2348 = raw_by_id.get("xbrl_2348_2026Q1_current")
    if bulk_2348 is not None and direct_2348 is not None:
        if (
            direct_2348["raw_payload_sha256"]
            != "b2e2852b47d751bfe352925c75882d016124ed6a5bff6fd4d6964b4741efd534"
            or direct_2348["raw_byte_count"] != "686961"
            or "exactly one 2348 member" not in bulk_2348["notes"]
            or "SHA match the direct current payload" not in bulk_2348["notes"]
        ):
            errors.append("2348 bulk/direct single-current-payload evidence drift")

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
            "pdf=df3bd64b27dfc2bf53a75f1560a152aed7361d2ba8ee9605715ed81709470e0b;"
            "t56_attachment=899a2483f1d50277e5f4967aa45bd971b7cf373de57d672b62f9a6af467348be"
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
            "pdf=99a7320d1c22d35c0b88166655f6912b6da26f53869ca1f0276afaa42cd20fd4;"
            "t56_attachment=24382f38ae0fb50a6894d82495b519b69ce0174c6e5ce783f83223a70b89e325"
        )
        if leakage["corroborating_sha256s"] != expected_corroborating:
            errors.append("4552 revision-leakage corroborating lineage SHA-256 drift")
        corroborating = re.findall(r"=([0-9a-f]{64})(?:;|$)", leakage["corroborating_sha256s"])
        if len(corroborating) != 5:
            errors.append(
                "4552 revision-leakage witness requires t05 revision t56 t57 PDF and correction-attachment hashes"
            )
    expected_records = len(sources) + len(pilots) + len(evidence) + len(raw_archives)
    if len(audit) != expected_records:
        errors.append("generated source audit row count mismatch")
    if {row["audit_id"] for row in audit} != {"financial_statement_historical_pit_source_audit_v3"}:
        errors.append("generated source audit must use the v3 acquisition and revision contract")
    for row in audit:
        record_label = f"{row['record_type']}:{row['record_id']}"
        if row["pit_eligible"] != "False" or row["formal_model_use_allowed"] != "False":
            errors.append(f"{record_label}: generated source audit must remain fail closed")
        if not row["blocker"]:
            errors.append(f"{record_label}: generated source audit blocker is required")
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
    for source in sources:
        generated = audit_by_type["source_surface"].get(source["source_id"])
        if generated is None:
            continue
        expected = {
            "period": source["coverage_start"],
            "source_role": source["source_role"],
            "official_url": source["official_url"],
            "scope_evidence": source["scope_semantics"],
            "taxonomy_evidence": source["taxonomy_semantics"],
            "availability_evidence": source["availability_semantics"],
            "revision_evidence": source["revision_semantics"],
            "raw_payload_sha256": "",
            "member_count": "",
            "audit_status": source["status"],
            "blocker": source["blocker"],
        }
        if any(generated[key] != value for key, value in expected.items()):
            errors.append(f"{source['source_id']}: generated source-surface projection drift")
    for pilot in pilots:
        generated = audit_by_type["pilot_archive"].get(pilot["archive_file"])
        if generated is None:
            continue
        expected = {
            "period": pilot["period"],
            "source_role": "quarter_archive_pilot",
            "official_url": "https://mopsov.twse.com.tw/server-java/FileDownLoad",
            "scope_evidence": f"{pilot['scope_counts']};{pilot['market_scope_evidence']}",
            "taxonomy_evidence": pilot["taxonomy_evidence"],
            "availability_evidence": pilot["initial_filed_at_evidence"],
            "revision_evidence": pilot["revision_payload_evidence"],
            "raw_payload_sha256": pilot["raw_payload_sha256"],
            "member_count": pilot["member_count"],
            "audit_status": "pilot_payload_and_scope_verified_pit_blocked",
            "blocker": pilot["blocker"],
        }
        if any(generated[key] != value for key, value in expected.items()):
            errors.append(f"{pilot['archive_file']}: generated pilot projection drift")
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
        expected_availability = (
            f"metric_initial_public_at={witness['metric_initial_public_at'] or 'none'};"
            f"document_visible_upload_at={witness['document_visible_upload_at'] or 'none'};"
            f"revision_public_at={witness['revision_public_at'] or 'none'}"
        )
        expected_scope = (
            f"company_id={witness['company_id']};market={witness['market']};"
            f"scope={witness['report_scope']};filename={witness['canonical_filename']}"
        )
        expected_revision = (
            f"metric={witness['metric_name'] or 'none'};"
            f"initial={witness['initial_value'] or 'none'};"
            f"revision={witness['revision_value'] or 'none'};"
            f"current_visible={witness['current_visible_value'] or 'none'};"
            f"visibility={witness['public_version_visibility']};"
            f"requests={witness['request_contracts']};"
            f"primary_response_sha256={witness['primary_response_sha256']};"
            f"corroborating_sha256s={witness['corroborating_sha256s'] or 'none'};"
            f"current_payload_sha256={witness['current_payload_sha256'] or 'none'};"
            f"captured_at={witness['captured_at']}"
        )
        if (
            generated["period"] != witness["period"]
            or generated["source_role"] != witness["witness_type"]
            or generated["official_url"] != witness["official_url"]
            or generated["scope_evidence"] != expected_scope
            or generated["taxonomy_evidence"] != f"industry_schema={witness['industry_schema']}"
            or generated["availability_evidence"] != expected_availability
            or generated["revision_evidence"] != expected_revision
            or generated["member_count"] != ""
            or generated["audit_status"] != witness["conclusion"]
            or generated["blocker"]
            != "exact_xbrl_fact_availability_and_complete_revision_payload_lineage_unavailable"
        ):
            errors.append(f"{witness_id}: generated witness projection drift")
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
        expected_scope = (
            f"related_record_ids={archive['related_record_ids']};"
            f"external_archive_relative_path={archive['external_archive_relative_path']}"
        )
        expected_availability = (
            f"captured_at={archive['captured_at']};"
            f"official_public_at={archive['official_public_at'] or 'none'};"
            f"availability_precision={archive['availability_precision']};"
            f"archive_root_id={archive['external_archive_root_id']};"
            f"raw_archive_ref={archive['raw_archive_ref']};"
            f"raw_byte_count={archive['raw_byte_count']}"
        )
        expected_revision = (
            f"request={archive['request_contract']};"
            f"archive_status={archive['archive_status']};notes={archive['notes']}"
        )
        if (
            generated["period"] != archive["period"]
            or generated["source_role"] != archive["payload_role"]
            or generated["official_url"] != archive["official_url"]
            or generated["scope_evidence"] != expected_scope
            or generated["taxonomy_evidence"] != f"source_id={archive['source_id']}"
            or generated["availability_evidence"] != expected_availability
            or generated["revision_evidence"] != expected_revision
            or generated["member_count"] != ""
            or generated["audit_status"] != archive["archive_status"]
            or generated["blocker"]
            != (
                "raw_retained_but_exact_xbrl_fact_availability_and_complete_revision_"
                "payload_lineage_unavailable"
            )
        ):
            errors.append(f"{archive_id}: generated raw archive projection drift")
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
        "document_visible_upload_at",
        "revision_public_at",
        "selected corrected or replacement pages",
        "company_period_date_text",
        "matched_not_officially_keyed",
        "exactly one 2348 member",
        "686961 bytes",
        "TWSE OpenAPI",
        "1043 rows",
        "出表日期=1150716",
        "no company filed_at, revision id, or version selector",
        "t56_attachment_2816_2013Q1",
        "t56_attachment_4552_2025Q1",
        "t56_attachment_2348_2026Q1_skey1",
        "t56_attachment_2348_2026Q1_skey2",
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
