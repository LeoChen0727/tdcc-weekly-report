from __future__ import annotations

import csv
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ARCHIVER = ROOT / "scripts" / "archive_daily_official_report_bundles.py"
VALIDATOR = ROOT / "scripts" / "validate_daily_official_report_archive_contract.py"
CONTRACT = ROOT / "config" / "daily_official_report_archive_contract.json"
DOC = ROOT / "docs" / "daily_official_report_archive.md"
WORKSPACE_POLICY = ROOT / "docs" / "workspace_cleanup_policy.md"
PRODUCTION_INVENTORY = ROOT / "config" / "repo_production_inventory.csv"
LIFECYCLE_INVENTORY = ROOT / "config" / "repo_file_lifecycle_inventory.csv"
RUNTIME_LINEAGE = ROOT / "config" / "runtime_file_lineage_contract.csv"
REPORT_LINEAGE = ROOT / "config" / "report_artifact_lineage.csv"
TEST_PATH = "tests/test_daily_official_report_archive.py"


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        return [dict(row) for row in csv.DictReader(handle)]


def rows_by_path(path: Path, key: str = "path") -> dict[str, dict[str, str]]:
    return {str(row.get(key, "")): row for row in read_csv(path)}


def validate() -> list[str]:
    errors: list[str] = []
    required_paths = (
        ARCHIVER,
        VALIDATOR,
        CONTRACT,
        DOC,
        WORKSPACE_POLICY,
        PRODUCTION_INVENTORY,
        LIFECYCLE_INVENTORY,
        RUNTIME_LINEAGE,
        REPORT_LINEAGE,
        ROOT / TEST_PATH,
    )
    for path in required_paths:
        if not path.exists():
            errors.append(f"missing daily official archive contract path: {path.relative_to(ROOT).as_posix()}")
    if errors:
        return errors

    contract = json.loads(CONTRACT.read_text(encoding="utf-8"))
    expected = {
        "report_family": "daily",
        "source_root_name": "chatgpt_side_outputs_official",
        "report_manifest_path": "output/latest/report_manifest_latest.json",
        "freshness_csv_path": "output/latest/data_freshness_latest.csv",
        "runtime_manifest_name": "chatgpt_daily_report_runtime_manifest.json",
        "required_destination_filesystem": "NTFS",
        "current_authority": "origin_main_report_manifest_and_data_freshness",
        "baseline_authority": "immediate_predecessor_dated_bundle_runtime_manifest",
        "copy_only": True,
        "source_mutation_forbidden": True,
        "automation_allowed": False,
        "execution_report_required": True,
    }
    for field, expected_value in expected.items():
        if contract.get(field) != expected_value:
            errors.append(f"archive contract {field} must equal {expected_value!r}")
    if set(contract.get("allowed_extensions", [])) != {".pdf", ".png", ".csv", ".json"}:
        errors.append("archive contract allowed_extensions must be exactly PDF/PNG/CSV/JSON")

    archiver_text = ARCHIVER.read_text(encoding="utf-8")
    for marker in (
        "load_authority_state",
        "validate_retained_bundle",
        "preflight_destinations",
        "copy_candidate_atomic",
        "source_fingerprint_unchanged",
        "already_present_same_sha",
        "execution_manifest",
        "source_files_deleted\": 0",
        "--expected-destination-volume",
        "--include-date",
        "--copy",
    ):
        if marker not in archiver_text:
            errors.append(f"archive command missing contract marker: {marker}")
    for forbidden in (
        "F:\\CodexStorage",
        "shutil.move(",
        "os.remove(",
        "os.replace(",
        ".rmdir(",
        "--delete",
        "--move",
    ):
        if forbidden in archiver_text:
            errors.append(f"archive command contains forbidden source/destructive marker: {forbidden}")

    workflow_mentions: list[str] = []
    for workflow in sorted((ROOT / ".github" / "workflows").glob("*.y*ml")):
        if ARCHIVER.name in workflow.read_text(encoding="utf-8", errors="replace"):
            workflow_mentions.append(workflow.relative_to(ROOT).as_posix())
    if workflow_mentions:
        errors.append(f"archive command must not be wired into automation: {workflow_mentions}")

    production_rows = rows_by_path(PRODUCTION_INVENTORY)
    expected_production = {
        ARCHIVER.relative_to(ROOT).as_posix(): ("python", "daily_production"),
        VALIDATOR.relative_to(ROOT).as_posix(): ("python", "daily_production"),
        TEST_PATH: ("test_python", "daily_production"),
    }
    for path, (kind, owner) in expected_production.items():
        row = production_rows.get(path)
        if row is None:
            errors.append(f"repo production inventory missing archive path: {path}")
        elif row.get("kind") != kind or row.get("owner") != owner or row.get("status") != "active":
            errors.append(f"repo production inventory has incorrect archive ownership: {path}")

    lifecycle_rows = rows_by_path(LIFECYCLE_INVENTORY)
    expected_lifecycle = {
        ARCHIVER.relative_to(ROOT).as_posix(): "python",
        VALIDATOR.relative_to(ROOT).as_posix(): "python",
        TEST_PATH: "test_python",
        DOC.relative_to(ROOT).as_posix(): "guidance_doc",
    }
    for path, expected_type in expected_lifecycle.items():
        row = lifecycle_rows.get(path)
        if row is None:
            errors.append(f"repo lifecycle inventory missing archive path: {path}")
        elif row.get("type") != expected_type or row.get("owner") != "daily_production":
            errors.append(f"repo lifecycle inventory has incorrect archive ownership: {path}")
    archiver_lifecycle = lifecycle_rows.get(ARCHIVER.relative_to(ROOT).as_posix(), {})
    if TEST_PATH not in str(archiver_lifecycle.get("tested_by", "")):
        errors.append("archive command lifecycle row must reference its behavioral tests")
    if DOC.relative_to(ROOT).as_posix() not in str(archiver_lifecycle.get("documented_by", "")):
        errors.append("archive command lifecycle row must reference its contract document")

    runtime_rows = rows_by_path(RUNTIME_LINEAGE, key="script_path")
    runtime_row = runtime_rows.get(ARCHIVER.relative_to(ROOT).as_posix())
    if runtime_row is None:
        errors.append("runtime file lineage is missing the daily official archive command")
    else:
        required_reads = str(runtime_row.get("required_read_artifacts", ""))
        for marker in (
            "config/daily_official_report_archive_contract.json",
            "output/latest/report_manifest_latest.json",
            "output/latest/data_freshness_latest.csv",
        ):
            if marker not in required_reads:
                errors.append(f"runtime lineage missing archive read artifact: {marker}")
        allowed_reads = str(runtime_row.get("allowed_read_prefixes", ""))
        if "chatgpt_side_outputs_official" not in allowed_reads:
            errors.append("runtime lineage must allow the dated official bundle family")
        if "F:\\" in json.dumps(runtime_row):
            errors.append("runtime lineage must not hard-code an F-drive dependency")

    report_rows = rows_by_path(REPORT_LINEAGE, key="artifact_path")
    archive_artifact = "external/report-archive/taiwan-stock-recommendation/daily/YYYYMMDD/**"
    report_row = report_rows.get(archive_artifact)
    if report_row is None:
        errors.append("report artifact lineage is missing the external daily archive family")
    elif report_row.get("producer") != ARCHIVER.relative_to(ROOT).as_posix():
        errors.append("external daily archive lineage has the wrong producer")
    for evidence_artifact in (
        "external/archive-execution/daily_official_report_archive_*.csv",
        "external/archive-execution/daily_official_report_archive_*.json",
    ):
        evidence_row = report_rows.get(evidence_artifact)
        if evidence_row is None:
            errors.append(f"report artifact lineage is missing archive evidence: {evidence_artifact}")
        elif evidence_row.get("producer") != ARCHIVER.relative_to(ROOT).as_posix():
            errors.append(f"archive evidence lineage has the wrong producer: {evidence_artifact}")

    doc_text = DOC.read_text(encoding="utf-8")
    for marker in (
        "origin/main",
        "current",
        "baseline",
        "--expected-destination-volume F:",
        "--copy",
        "不得刪除、搬移、改名或改寫",
        "workflow_automation_maintenance",
    ):
        if marker not in doc_text:
            errors.append(f"archive documentation missing marker: {marker}")
    if "archive_daily_official_report_bundles.py" not in WORKSPACE_POLICY.read_text(encoding="utf-8"):
        errors.append("workspace cleanup policy must document the external archive command boundary")
    return errors


def main() -> int:
    errors = validate()
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1
    print("daily official report archive contract validation passed")
    print("archive_mode=copy_only_non_destructive")
    print("automation_allowed=false")
    print("destination_root=runtime_argument_only")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
