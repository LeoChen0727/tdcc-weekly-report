from __future__ import annotations

import csv
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
REGISTRY_CSV = ROOT / "config" / "stock_model_contract_registry.csv"
CONDITION_SPEC_CSV = ROOT / "config" / "daily_model_condition_spec.csv"

REQUIRED_COLUMNS = [
    "model_id",
    "model_name",
    "contract_version",
    "owner_lane",
    "production_source_file",
    "condition_function",
    "score_function",
    "score_profile_id",
    "input_columns",
    "output_columns",
    "pdf_visibility",
    "approved_for_daily_pdf",
    "approved_for_tdcc_weekly_pdf",
    "approved_for_individual_pdf",
    "research_baseline_required",
    "promotion_required",
    "effective_from",
    "deprecated_after",
    "change_reason",
]

APPROVAL_COLUMNS = [
    "approved_for_daily_pdf",
    "approved_for_tdcc_weekly_pdf",
    "approved_for_individual_pdf",
]

SPEC_ALIGNMENT_COLUMNS = [
    "condition_function",
    "score_function",
    "score_profile_id",
]

BOOL_VALUES = {"true", "false"}
CONTRACT_VERSION_RE = re.compile(r"^v[0-9]+$")
DATE_OR_STATUS_RE = re.compile(r"^[0-9]{4}-[0-9]{2}-[0-9]{2}$")


def rel(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def load_csv_rows(path: Path) -> tuple[list[dict[str, str]], list[str], list[str]]:
    if not path.exists():
        return [], [], [f"missing CSV: {rel(path)}"]
    with path.open("r", encoding="utf-8-sig", newline="") as fh:
        reader = csv.DictReader(fh)
        fieldnames = list(reader.fieldnames or [])
        rows = [{key: str(value or "").strip() for key, value in row.items()} for row in reader]
    if not fieldnames:
        return rows, fieldnames, [f"empty CSV header: {rel(path)}"]
    return rows, fieldnames, []


def split_semicolon(value: str) -> list[str]:
    return [part.strip() for part in str(value or "").split(";") if part.strip()]


def validate_schema(fieldnames: list[str]) -> list[str]:
    missing = [col for col in REQUIRED_COLUMNS if col not in fieldnames]
    if missing:
        return [f"stock model contract registry missing columns: {missing}"]
    return []


def validate_rows(rows: list[dict[str, str]]) -> list[str]:
    errors: list[str] = []
    if not rows:
        return ["stock model contract registry is empty"]

    seen: set[str] = set()
    for line_no, row in enumerate(rows, start=2):
        model_id = row.get("model_id", "").strip()
        if not model_id:
            errors.append(f"registry row {line_no} has empty model_id")
            continue
        if model_id in seen:
            errors.append(f"duplicate model_id in contract registry: {model_id}")
        seen.add(model_id)

        for col in REQUIRED_COLUMNS:
            if not row.get(col, "").strip():
                errors.append(f"{model_id} has empty required field: {col}")

        version = row.get("contract_version", "")
        if version and not CONTRACT_VERSION_RE.match(version):
            errors.append(f"{model_id} has invalid contract_version: {version}")

        for col in APPROVAL_COLUMNS:
            value = row.get(col, "")
            if value not in BOOL_VALUES:
                errors.append(f"{model_id} {col} must be true/false, got {value!r}")

        effective_from = row.get("effective_from", "")
        if effective_from and effective_from != "pending_review" and not DATE_OR_STATUS_RE.match(effective_from):
            errors.append(f"{model_id} effective_from must be YYYY-MM-DD or pending_review, got {effective_from!r}")

        deprecated_after = row.get("deprecated_after", "")
        if deprecated_after and deprecated_after not in {"none", "pending_review"} and not DATE_OR_STATUS_RE.match(deprecated_after):
            errors.append(f"{model_id} deprecated_after must be YYYY-MM-DD, none, or pending_review, got {deprecated_after!r}")

        for source in split_semicolon(row.get("production_source_file", "")):
            if source == "pending_review":
                continue
            if not (ROOT / source).exists():
                errors.append(f"{model_id} production_source_file does not exist: {source}")

    return errors


def validate_condition_spec_alignment(rows: list[dict[str, str]]) -> list[str]:
    errors: list[str] = []
    spec_rows, spec_fields, spec_errors = load_csv_rows(CONDITION_SPEC_CSV)
    errors.extend(spec_errors)
    if errors:
        return errors

    required_spec = {"model_id", "condition_function", "score_function", "score_profile_id"}
    missing_spec_cols = sorted(required_spec - set(spec_fields))
    if missing_spec_cols:
        return [f"daily model condition spec missing columns: {missing_spec_cols}"]

    contracts = {row["model_id"]: row for row in rows if row.get("model_id")}
    for spec in spec_rows:
        model_id = spec.get("model_id", "")
        if not model_id:
            errors.append("daily model condition spec has empty model_id")
            continue
        contract = contracts.get(model_id)
        if contract is None:
            errors.append(f"contract registry missing production model from daily_model_condition_spec.csv: {model_id}")
            continue
        for col in SPEC_ALIGNMENT_COLUMNS:
            if contract.get(col, "") != spec.get(col, ""):
                errors.append(
                    f"{model_id} contract {col}={contract.get(col, '')!r} "
                    f"does not match daily_model_condition_spec.csv {spec.get(col, '')!r}"
                )

    return errors


def pending_review_models(rows: list[dict[str, str]]) -> dict[str, list[str]]:
    pending: dict[str, list[str]] = {}
    for row in rows:
        fields = [col for col, value in row.items() if str(value).strip() == "pending_review"]
        if fields:
            pending[row.get("model_id", "")] = fields
    return pending


def validate() -> list[str]:
    rows, fieldnames, errors = load_csv_rows(REGISTRY_CSV)
    errors.extend(validate_schema(fieldnames))
    if errors:
        return errors
    errors.extend(validate_rows(rows))
    errors.extend(validate_condition_spec_alignment(rows))
    return errors


def main() -> int:
    rows, _, _ = load_csv_rows(REGISTRY_CSV)
    errors = validate()
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1

    tdcc_models = sorted(
        row["model_id"]
        for row in rows
        if row.get("approved_for_tdcc_weekly_pdf") == "true"
    )
    pending = pending_review_models(rows)
    print("stock model contract registry validation passed")
    print(f"registry={rel(REGISTRY_CSV)}")
    print(f"validated_models={len(rows)}")
    print(f"tdcc_weekly_pdf_models={tdcc_models}")
    print(f"pending_review_models={sorted(pending)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
