from __future__ import annotations

import csv
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SOURCE_PATH = ROOT / "config/daily_model_financial_statement_historical_pit_sources.csv"
PILOT_PATH = ROOT / "config/daily_model_financial_statement_historical_pit_pilot.csv"
OUTPUT_CSV = ROOT / "output/latest/research_backtest/financial_statement_historical_pit_source_audit_latest.csv"
OUTPUT_MD = ROOT / "output/latest/research_backtest/financial_statement_historical_pit_source_audit_latest.md"
DOCS_CSV = ROOT / "docs/latest/financial_statement_historical_pit_source_audit_latest.csv"
DOCS_MD = ROOT / "docs/latest/financial_statement_historical_pit_source_audit_latest.md"


def read_rows(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))


def validate(root: Path = ROOT) -> list[str]:
    errors: list[str] = []
    sources = read_rows(root / SOURCE_PATH.relative_to(ROOT))
    pilots = read_rows(root / PILOT_PATH.relative_to(ROOT))
    audit = read_rows(root / OUTPUT_CSV.relative_to(ROOT))
    required_sources = {
        "mops_xbrl_bulk_index",
        "mops_xbrl_bulk_download",
        "mops_xbrl_single_company",
        "mops_financial_report_announcement",
        "mops_financial_report_correction",
        "mops_taxonomy_download",
    }
    if {row["source_id"] for row in sources} != required_sources:
        errors.append("historical PIT source surface registry is incomplete")
    for row in sources:
        if row["pit_eligible"] != "False" or row["formal_model_use_allowed"] != "False":
            errors.append(f"{row['source_id']}: unproven source cannot authorize historical PIT or formal use")
        if not row["official_url"].startswith("https://mopsov.twse.com.tw/"):
            errors.append(f"{row['source_id']}: source must be an official MOPS URL")
        if not row["blocker"]:
            errors.append(f"{row['source_id']}: blocker is required")
    if {row["period"] for row in pilots} != {"2013Q1", "2025Q1"}:
        errors.append("pilot must cover 2013Q1 and a modern quarter")
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
    expected_records = len(sources) + len(pilots)
    if len(audit) != expected_records:
        errors.append("generated source audit row count mismatch")
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
        "exact initial filing availability",
        "2025-04-07 onward",
        "2013Q1 archive is an earliest-IFRS source-contract probe",
    ):
        if required not in md:
            errors.append(f"source audit Markdown missing fail-closed evidence: {required}")
    return errors


def main() -> None:
    errors = validate()
    if errors:
        raise SystemExit("\n".join(f"- {error}" for error in errors))
    print("financial statement historical PIT source audit passed: pit_eligible=False formal_model_use_allowed=False")


if __name__ == "__main__":
    main()
