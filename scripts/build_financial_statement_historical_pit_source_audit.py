from __future__ import annotations

import csv
import fnmatch
import hashlib
import subprocess
from pathlib import Path

from model_research_artifact_guard import (
    compare_protected_sentinel_snapshots,
    load_protected_sentinels,
    protected_sentinel_aggregate_sha256,
)


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
AUDIT_ID = "financial_statement_historical_pit_source_audit_v2"

AUDIT_COLUMNS = [
    "audit_id",
    "record_type",
    "record_id",
    "period",
    "source_role",
    "official_url",
    "scope_evidence",
    "taxonomy_evidence",
    "availability_evidence",
    "revision_evidence",
    "raw_payload_sha256",
    "member_count",
    "pit_eligible",
    "formal_model_use_allowed",
    "audit_status",
    "blocker",
]


def read_rows(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        return list(csv.DictReader(handle))


def build_rows() -> list[dict[str, str]]:
    rows: list[dict[str, str]] = []
    for source in read_rows(SOURCE_PATH):
        rows.append(
            {
                "audit_id": AUDIT_ID,
                "record_type": "source_surface",
                "record_id": source["source_id"],
                "period": source["coverage_start"],
                "source_role": source["source_role"],
                "official_url": source["official_url"],
                "scope_evidence": source["scope_semantics"],
                "taxonomy_evidence": source["taxonomy_semantics"],
                "availability_evidence": source["availability_semantics"],
                "revision_evidence": source["revision_semantics"],
                "raw_payload_sha256": "",
                "member_count": "",
                "pit_eligible": source["pit_eligible"],
                "formal_model_use_allowed": source["formal_model_use_allowed"],
                "audit_status": source["status"],
                "blocker": source["blocker"],
            }
        )
    for pilot in read_rows(PILOT_PATH):
        rows.append(
            {
                "audit_id": AUDIT_ID,
                "record_type": "pilot_archive",
                "record_id": pilot["archive_file"],
                "period": pilot["period"],
                "source_role": "quarter_archive_pilot",
                "official_url": "https://mopsov.twse.com.tw/server-java/FileDownLoad",
                "scope_evidence": f"{pilot['scope_counts']};{pilot['market_scope_evidence']}",
                "taxonomy_evidence": pilot["taxonomy_evidence"],
                "availability_evidence": pilot["initial_filed_at_evidence"],
                "revision_evidence": pilot["revision_payload_evidence"],
                "raw_payload_sha256": pilot["raw_payload_sha256"],
                "member_count": pilot["member_count"],
                "pit_eligible": pilot["pit_eligible"],
                "formal_model_use_allowed": pilot["formal_model_use_allowed"],
                "audit_status": "pilot_payload_and_scope_verified_pit_blocked",
                "blocker": pilot["blocker"],
            }
        )
    for witness in read_rows(EVIDENCE_PATH):
        availability = (
            f"metric_initial_public_at={witness['metric_initial_public_at'] or 'none'};"
            f"document_visible_upload_at={witness['document_visible_upload_at'] or 'none'};"
            f"revision_public_at={witness['revision_public_at'] or 'none'}"
        )
        revision = (
            f"metric={witness['metric_name'] or 'none'};initial={witness['initial_value'] or 'none'};"
            f"revision={witness['revision_value'] or 'none'};"
            f"current_visible={witness['current_visible_value'] or 'none'};"
            f"visibility={witness['public_version_visibility']};"
            f"requests={witness['request_contracts']};"
            f"primary_response_sha256={witness['primary_response_sha256']};"
            f"corroborating_sha256s={witness['corroborating_sha256s'] or 'none'};"
            f"current_payload_sha256={witness['current_payload_sha256'] or 'none'};"
            f"captured_at={witness['captured_at']}"
        )
        rows.append(
            {
                "audit_id": AUDIT_ID,
                "record_type": "evidence_witness",
                "record_id": witness["witness_id"],
                "period": witness["period"],
                "source_role": witness["witness_type"],
                "official_url": witness["official_url"],
                "scope_evidence": (
                    f"company_id={witness['company_id']};market={witness['market']};"
                    f"scope={witness['report_scope']};filename={witness['canonical_filename']}"
                ),
                "taxonomy_evidence": f"industry_schema={witness['industry_schema']}",
                "availability_evidence": availability,
                "revision_evidence": revision,
                "raw_payload_sha256": (
                    witness["current_payload_sha256"] or witness["primary_response_sha256"]
                ),
                "member_count": "",
                "pit_eligible": witness["pit_eligible"],
                "formal_model_use_allowed": witness["formal_model_use_allowed"],
                "audit_status": witness["conclusion"],
                "blocker": "exact_xbrl_fact_availability_and_complete_revision_payload_lineage_unavailable",
            }
        )
    for archive in read_rows(RAW_ARCHIVE_MANIFEST_PATH):
        rows.append(
            {
                "audit_id": AUDIT_ID,
                "record_type": "raw_archive",
                "record_id": archive["archive_id"],
                "period": archive["period"],
                "source_role": archive["payload_role"],
                "official_url": archive["official_url"],
                "scope_evidence": (
                    f"related_record_ids={archive['related_record_ids']};"
                    f"external_archive_relative_path={archive['external_archive_relative_path']}"
                ),
                "taxonomy_evidence": f"source_id={archive['source_id']}",
                "availability_evidence": (
                    f"captured_at={archive['captured_at']};"
                    f"official_public_at={archive['official_public_at'] or 'none'};"
                    f"availability_precision={archive['availability_precision']};"
                    f"archive_root_id={archive['external_archive_root_id']};"
                    f"raw_archive_ref={archive['raw_archive_ref']};"
                    f"raw_byte_count={archive['raw_byte_count']}"
                ),
                "revision_evidence": (
                    f"request={archive['request_contract']};"
                    f"archive_status={archive['archive_status']};notes={archive['notes']}"
                ),
                "raw_payload_sha256": archive["raw_payload_sha256"],
                "member_count": "",
                "pit_eligible": archive["pit_eligible"],
                "formal_model_use_allowed": archive["formal_model_use_allowed"],
                "audit_status": archive["archive_status"],
                "blocker": (
                    "raw_retained_but_exact_xbrl_fact_availability_and_complete_revision_"
                    "payload_lineage_unavailable"
                ),
            }
        )
    return rows


def write_csv(path: Path, rows: list[dict[str, str]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=AUDIT_COLUMNS)
        writer.writeheader()
        writer.writerows(rows)


def markdown(rows: list[dict[str, str]]) -> str:
    source_rows = [row for row in rows if row["record_type"] == "source_surface"]
    pilot_rows = [row for row in rows if row["record_type"] == "pilot_archive"]
    witness_rows = [row for row in rows if row["record_type"] == "evidence_witness"]
    raw_archive_rows = [row for row in rows if row["record_type"] == "raw_archive"]
    lines = [
        "# Historical Financial Statement PIT Source Audit",
        "",
        f"- audit_id: `{AUDIT_ID}`",
        "- conclusion: `blocked_exact_xbrl_fact_availability_and_complete_revision_payload_lineage_unavailable`",
        "- target coverage: `2013Q1 onward`",
        "- current tracked price-history overlap: `2025-04-07 onward` (verified for the cross-market and cross-industry pilot stocks at source-audit time)",
        "- `pit_eligible=False`",
        "- `formal_model_use_allowed=False`",
        "",
        "The official MOPS bulk and single-company XBRL surfaces provide period payloads, report scope, industry taxonomy, and correction-event evidence. The historical material-information surface provides second-level public times for fields actually included in a matching announcement. The financial-report document index provides second-level PDF upload times. Neither timestamp can be assigned to omitted XBRL facts or to the one currently visible payload after a correction.",
        "The public document interface exposes one canonical filename per company-period-report type and a latest-correction indicator, but no selectable immutable before/after payload pair. TWSE's official correction guidance describes resubmitting corrected formatted data and deleting the uploaded electronic book before uploading its replacement; it does not specify a publicly retrievable immutable before/after archive. This proves that the public reproducible contract is insufficient; it does not claim that the official backend never retained prior files. ZIP member times are archive rebuild times, and `ReviewAuditDate` is not MOPS filing availability.",
        "The 2013Q1 archive is an earliest-IFRS source-contract probe, not current backtest evidence. The 2025Q1 archive is the first pilot quarter near the current tracked price-history window. Financial-statement source retention and research-price overlap are separate gates.",
        "",
        "## Official source surfaces",
        "",
        "| Source | Role | Coverage | Availability / revision contract | Result | Official URL |",
        "| --- | --- | --- | --- | --- | --- |",
    ]
    for row in source_rows:
        lines.append(
            f"| `{row['record_id']}` | {row['source_role']} | {row['period']} | "
            f"{row['availability_evidence']}; {row['revision_evidence']} | "
            f"`{row['audit_status']}` | {row['official_url']} |"
        )
    lines.extend(
        [
            "",
            "## Cross-period archive probes",
            "",
            "| Period | Archive SHA-256 | Members | Scope evidence | Taxonomy evidence | Result |",
            "| --- | --- | ---: | --- | --- | --- |",
        ]
    )
    for row in pilot_rows:
        lines.append(
            f"| {row['period']} | `{row['raw_payload_sha256']}` | {row['member_count']} | "
            f"{row['scope_evidence']} | {row['taxonomy_evidence']} | `{row['audit_status']}` |"
        )
    lines.extend(
        [
            "",
            "## Availability and revision evidence",
            "",
            "| Witness | Period | Company/scope | Role | Official times | Metric states | Public version visibility | Result |",
            "| --- | --- | --- | --- | --- | --- | --- | --- |",
        ]
    )
    for row in witness_rows:
        metric_states = ";".join(
            part
            for part in row["revision_evidence"].split(";")[:4]
            if not part.endswith("=none")
        ) or "none"
        visibility = next(
            (
                part.removeprefix("visibility=")
                for part in row["revision_evidence"].split(";")
                if part.startswith("visibility=")
            ),
            "missing",
        )
        lines.append(
            f"| `{row['record_id']}` | {row['period']} | {row['scope_evidence']} | "
            f"{row['source_role']} | {row['availability_evidence']} | {metric_states} | "
            f"{visibility} | `{row['audit_status']}` |"
        )
    lines.extend(
        [
            "",
            "## External raw evidence retention",
            "",
            "Raw payloads remain outside Git under the logical root "
            "`codex_data_archives_taiwan_stock_financial_statement_historical_pit_source_audit_v1`. "
            "Every committed locator is content-addressed and was verified against the full SHA-256.",
            "",
            "| Archive | Period | Role | SHA-256 | Bytes | Relative locator | Status |",
            "| --- | --- | --- | --- | ---: | --- | --- |",
        ]
    )
    for row in raw_archive_rows:
        availability_parts = {
            part.split("=", 1)[0]: part.split("=", 1)[1]
            for part in row["availability_evidence"].split(";")
            if "=" in part
        }
        relative_locator = row["scope_evidence"].split(
            "external_archive_relative_path=", 1
        )[1]
        lines.append(
            f"| `{row['record_id']}` | {row['period']} | {row['source_role']} | "
            f"`{row['raw_payload_sha256']}` | {availability_parts['raw_byte_count']} | "
            f"`{relative_locator}` | `{row['audit_status']}` |"
        )
    lines.extend(
        [
            "",
            "## Formal-use boundary",
            "",
            "Until an official reproducible source binds every company-period-scope fact state to its actual public availability and complete revision payload lineage, EPS, gross margin, operating margin, operating income, non-operating income, and net income must not enter `revenue_unreacted_range`, any production gate, score, ranking, PDF, packet, or promotion evidence.",
            "",
            "The next admissible implementation is a source adapter that can bind each company-period-scope revision and every exposed fact state to an immutable payload SHA-256 plus its official availability timestamp or date. A PDF upload time cannot be reused as XBRL revision time; a material-information time applies only to the metrics actually present in that announcement. Statutory deadlines, audit/review dates, ZIP timestamps, and first-observed local capture times are not substitutes.",
            "",
        ]
    )
    return "\n".join(lines)


def _sha256_bytes(payload: bytes) -> str:
    return hashlib.sha256(payload).hexdigest()


def _git_tracked_entries(root: Path) -> dict[str, str]:
    try:
        result = subprocess.run(
            ["git", "ls-tree", "-r", "HEAD"],
            cwd=root,
            check=True,
            capture_output=True,
            text=True,
            encoding="utf-8",
        )
    except (OSError, subprocess.CalledProcessError):
        return {}
    entries: dict[str, str] = {}
    for line in result.stdout.splitlines():
        metadata, path = line.split("\t", 1)
        _mode, _kind, blob_sha = metadata.split()
        entries[path] = blob_sha
    return entries


def _sentinel_snapshot(root: Path, sentinels: list) -> tuple[dict[str, str], list[str]]:
    tracked = _git_tracked_entries(root)
    snapshot: dict[str, str] = {}
    errors: list[str] = []
    for sentinel in sentinels:
        worktree_matches = {
            path.relative_to(root).as_posix()
            for path in root.glob(sentinel.artifact_glob)
            if path.is_file()
        }
        tracked_matches = {
            path for path in tracked if fnmatch.fnmatchcase(path, sentinel.artifact_glob)
        }
        matches = sorted(worktree_matches | tracked_matches)
        if sentinel.required and not matches:
            errors.append(
                f"required protected sentinel has no worktree or HEAD match: {sentinel.sentinel_id}"
            )
        for relative in matches:
            local = root / relative
            if local.is_file():
                digest = _sha256_bytes(local.read_bytes())
            else:
                digest = f"git_blob:{tracked[relative]}"
            if relative in snapshot:
                errors.append(f"protected sentinel path matched more than once: {relative}")
            snapshot[relative] = digest
    return snapshot, errors


def build_and_write(root: Path = ROOT, sentinel_registry_path: Path | None = None) -> dict[str, Path]:
    global OUTPUT_CSV, OUTPUT_MD, DOCS_CSV, DOCS_MD
    outputs = {
        "output_csv": root / "output/latest/research_backtest/financial_statement_historical_pit_source_audit_latest.csv",
        "output_md": root / "output/latest/research_backtest/financial_statement_historical_pit_source_audit_latest.md",
        "docs_csv": root / "docs/latest/financial_statement_historical_pit_source_audit_latest.csv",
        "docs_md": root / "docs/latest/financial_statement_historical_pit_source_audit_latest.md",
    }
    registry = sentinel_registry_path or ROOT / "config/model_research_protected_sentinels.csv"
    sentinels = load_protected_sentinels(registry)
    before, before_errors = _sentinel_snapshot(root, sentinels)
    if before_errors:
        raise RuntimeError("protected sentinel preflight failed: " + "; ".join(before_errors))
    before_sha = protected_sentinel_aggregate_sha256(before)
    rows = build_rows()
    write_csv(outputs["output_csv"], rows)
    write_csv(outputs["docs_csv"], rows)
    text = markdown(rows)
    for key in ("output_md", "docs_md"):
        outputs[key].parent.mkdir(parents=True, exist_ok=True)
        outputs[key].write_text(text, encoding="utf-8")
    after, after_errors = _sentinel_snapshot(root, sentinels)
    errors = [*after_errors, *compare_protected_sentinel_snapshots(before, after)]
    if errors:
        raise RuntimeError("protected mature-model sentinel drift: " + "; ".join(errors))
    after_sha = protected_sentinel_aggregate_sha256(after)
    print(f"protected_sentinel_before_sha256={before_sha}")
    print(f"protected_sentinel_after_sha256={after_sha}")
    print("historical_financial_statement_pit_source_audit=blocked")
    return outputs


if __name__ == "__main__":
    for name, path in build_and_write().items():
        print(f"{name}={path}")
