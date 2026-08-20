from __future__ import annotations

import csv
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
AUDIT_CSV = ROOT / "config" / "repo_hidden_coupling_audit.csv"
AUDIT_DOC = ROOT / "docs" / "repo_hidden_coupling_audit.md"
PR_WORKFLOW = ROOT / ".github" / "workflows" / "individual_stock_pr_validation.yml"

REQUIRED_COLUMNS = {
    "issue_id",
    "category",
    "risk_level",
    "status",
    "evidence_paths",
    "current_guardrail",
    "open_gap",
    "owner_lane",
    "next_pr_priority",
    "next_action",
    "notes",
}

REQUIRED_CATEGORIES = {
    "filename_substring_title_token_matching",
    "fallback_inference",
    "pdf_side_lifecycle_invention",
    "model_condition_scoring_ranking_shared_coupling",
    "validators_not_workflow_called",
    "artifact_lineage_owner_gaps",
    "legacy_artifact_code_cleanup",
}

VALID_RISK_LEVELS = {"low", "medium", "high", "critical"}
VALID_PRIORITIES = {"P1", "P2", "P3"}
OPEN_STATUS_TOKENS = ("open", "partial")
WORKFLOW_COMMAND = "python scripts/validate_repo_hidden_coupling_audit.py"


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8-sig", errors="replace")


def load_rows(errors: list[str]) -> list[dict[str, str]]:
    if not AUDIT_CSV.exists():
        errors.append(f"missing audit csv: {AUDIT_CSV.relative_to(ROOT).as_posix()}")
        return []
    with AUDIT_CSV.open("r", encoding="utf-8-sig", newline="") as fh:
        reader = csv.DictReader(fh)
        if not reader.fieldnames:
            errors.append("audit csv has no header")
            return []
        missing = REQUIRED_COLUMNS.difference(reader.fieldnames)
        if missing:
            errors.append(f"audit csv missing columns: {sorted(missing)}")
            return []
        return [{key: str(value or "").strip() for key, value in row.items()} for row in reader]


def validate_rows(rows: list[dict[str, str]], errors: list[str]) -> None:
    seen_ids: set[str] = set()
    categories: set[str] = set()
    critical_or_high = 0
    for line_no, row in enumerate(rows, start=2):
        issue_id = row["issue_id"]
        category = row["category"]
        risk = row["risk_level"]
        status = row["status"]

        if not issue_id.startswith("HC-"):
            errors.append(f"row {line_no} issue_id must start with HC-: {issue_id}")
        if issue_id in seen_ids:
            errors.append(f"duplicate issue_id: {issue_id}")
        seen_ids.add(issue_id)

        if category not in REQUIRED_CATEGORIES:
            errors.append(f"{issue_id} has unsupported category: {category}")
        categories.add(category)

        if risk not in VALID_RISK_LEVELS:
            errors.append(f"{issue_id} has unsupported risk_level: {risk}")
        if risk in {"high", "critical"}:
            critical_or_high += 1

        if row["next_pr_priority"] not in VALID_PRIORITIES:
            errors.append(f"{issue_id} has unsupported next_pr_priority: {row['next_pr_priority']}")

        required_non_empty = (
            "status",
            "evidence_paths",
            "current_guardrail",
            "open_gap",
            "owner_lane",
            "next_action",
            "notes",
        )
        for column in required_non_empty:
            if not row[column]:
                errors.append(f"{issue_id} has empty {column}")

        if any(token in status for token in OPEN_STATUS_TOKENS) and row["next_action"].lower() in {"none", "n/a"}:
            errors.append(f"{issue_id} is open/partial but has no actionable next_action")

        evidence_paths = [part.strip() for part in row["evidence_paths"].split(";") if part.strip()]
        if len(evidence_paths) < 2:
            errors.append(f"{issue_id} must cite at least two evidence paths or scopes")

    missing_categories = REQUIRED_CATEGORIES.difference(categories)
    if missing_categories:
        errors.append(f"audit csv missing required categories: {sorted(missing_categories)}")
    if critical_or_high < 4:
        errors.append("audit csv must classify at least four high/critical repo risks")


def validate_doc(rows: list[dict[str, str]], errors: list[str]) -> None:
    if not AUDIT_DOC.exists():
        errors.append(f"missing audit doc: {AUDIT_DOC.relative_to(ROOT).as_posix()}")
        return
    text = read_text(AUDIT_DOC)
    for required in (
        "Repo Hidden Coupling Audit",
        "Plain-Language Conclusion",
        "Audit Matrix",
        "Follow-Up PR Order",
        "No row in this audit authorizes",
    ):
        if required not in text:
            errors.append(f"audit doc missing required section/text: {required}")
    for row in rows:
        if row["issue_id"] not in text:
            errors.append(f"audit doc does not mention {row['issue_id']}")
        if row["category"] not in text:
            errors.append(f"audit doc does not mention category {row['category']}")


def validate_workflows(errors: list[str]) -> None:
    text = read_text(PR_WORKFLOW)
    if WORKFLOW_COMMAND not in text:
        errors.append(f"{PR_WORKFLOW.relative_to(ROOT).as_posix()} must run {WORKFLOW_COMMAND}")


def validate() -> list[str]:
    errors: list[str] = []
    rows = load_rows(errors)
    if rows:
        validate_rows(rows, errors)
        validate_doc(rows, errors)
    validate_workflows(errors)
    return errors


def main() -> int:
    errors = validate()
    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1
    print("repo hidden coupling audit validation passed")
    print(f"validated_audit={AUDIT_CSV.relative_to(ROOT).as_posix()}")
    print(f"validated_categories={';'.join(sorted(REQUIRED_CATEGORIES))}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
