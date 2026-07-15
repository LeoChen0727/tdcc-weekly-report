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
OUTPUT_CSV = ROOT / "output/latest/research_backtest/financial_statement_historical_pit_source_audit_latest.csv"
OUTPUT_MD = ROOT / "output/latest/research_backtest/financial_statement_historical_pit_source_audit_latest.md"
DOCS_CSV = ROOT / "docs/latest/financial_statement_historical_pit_source_audit_latest.csv"
DOCS_MD = ROOT / "docs/latest/financial_statement_historical_pit_source_audit_latest.md"

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
                "audit_id": "financial_statement_historical_pit_source_audit_v1",
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
                "audit_id": "financial_statement_historical_pit_source_audit_v1",
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
    return rows


def write_csv(path: Path, rows: list[dict[str, str]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=AUDIT_COLUMNS)
        writer.writeheader()
        writer.writerows(rows)


def markdown(rows: list[dict[str, str]]) -> str:
    pilot_rows = [row for row in rows if row["record_type"] == "pilot_archive"]
    lines = [
        "# Historical Financial Statement PIT Source Audit",
        "",
        "- audit_id: `financial_statement_historical_pit_source_audit_v1`",
        "- conclusion: `blocked_exact_initial_filed_at_and_complete_revision_payload_history_unavailable`",
        "- target coverage: `2013Q1 onward`",
        "- current tracked price-history overlap: `2025-04-07 onward` (verified for the cross-market and cross-industry pilot stocks at source-audit time)",
        "- `pit_eligible=False`",
        "- `formal_model_use_allowed=False`",
        "",
        "The official MOPS bulk and single-company XBRL surfaces provide period payloads, report scope, industry taxonomy, and correction-event evidence. They do not provide a reproducible initial company filing timestamp plus every before/after revision payload. ZIP member times are archive rebuild times, and `ReviewAuditDate` is not MOPS filing availability.",
        "The 2013Q1 archive is an earliest-IFRS source-contract probe, not current backtest evidence. The 2025Q1 archive is the first pilot quarter near the current tracked price-history window. Financial-statement source retention and research-price overlap are separate gates.",
        "",
        "| Period | Archive SHA-256 | Members | Scope evidence | Taxonomy evidence | Result |",
        "| --- | --- | ---: | --- | --- | --- |",
    ]
    for row in pilot_rows:
        lines.append(
            f"| {row['period']} | `{row['raw_payload_sha256']}` | {row['member_count']} | "
            f"{row['scope_evidence']} | {row['taxonomy_evidence']} | `{row['audit_status']}` |"
        )
    lines.extend(
        [
            "",
            "## Formal-use boundary",
            "",
            "Until an official reproducible source supplies exact initial filing availability and complete revision payload lineage, EPS, gross margin, operating margin, operating income, non-operating income, and net income must not enter `revenue_unreacted_range`, any production gate, score, ranking, PDF, packet, or promotion evidence.",
            "",
            "The next admissible implementation is a source adapter that can bind each company-period-scope revision to an immutable payload SHA-256 and an official availability timestamp or date. Statutory deadlines, audit/review dates, ZIP timestamps, and first-observed local capture times are not substitutes.",
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
