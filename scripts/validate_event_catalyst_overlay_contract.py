from __future__ import annotations

import csv
import re
from datetime import datetime
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CONTRACT = ROOT / "config" / "event_catalyst_overlay_contract.csv"

REQUIRED_COLUMNS = [
    "overlay_id",
    "source_layer",
    "source_file",
    "field_name",
    "allowed_effect",
    "allowed_consumers",
    "degraded_behavior",
    "score_allowed",
    "ranking_allowed",
    "reason_text_allowed",
    "disclosure_only",
    "requires_backtest",
    "requires_human_review",
    "approved_for_daily_pdf",
    "approved_for_tdcc_weekly_pdf",
    "approved_for_individual_pdf",
    "effective_from",
    "deprecated_after",
    "change_reason",
]

ALLOWED_EFFECTS = {
    "disclosure_only",
    "reason_text_only",
    "risk_flag",
    "score_overlay",
    "ranking_modifier",
}

ALLOWED_CONSUMERS = {
    "daily_pdf",
    "tdcc_weekly_pdf",
    "individual_pdf",
    "packet",
    "validator",
}

BOOLEAN_COLUMNS = [
    "score_allowed",
    "ranking_allowed",
    "reason_text_allowed",
    "disclosure_only",
    "requires_backtest",
    "requires_human_review",
    "approved_for_daily_pdf",
    "approved_for_tdcc_weekly_pdf",
    "approved_for_individual_pdf",
]

OVERLAY_ID_RE = re.compile(r"^[a-z0-9_]+$")


def read_contract() -> tuple[list[str], list[dict[str, str]]]:
    if not CONTRACT.exists():
        return [], []
    with CONTRACT.open("r", encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle)
        rows = [{key: (value or "").strip() for key, value in row.items()} for row in reader]
        return list(reader.fieldnames or []), rows


def csv_columns(path: Path) -> set[str]:
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        reader = csv.reader(handle)
        try:
            return {column.strip() for column in next(reader)}
        except StopIteration:
            return set()


def parse_bool(row: dict[str, str], column: str, issues: list[str]) -> bool:
    value = row.get(column, "").strip().lower()
    if value not in {"true", "false"}:
        issues.append(f"{row.get('overlay_id', '<missing>')} has invalid boolean {column}={row.get(column, '')!r}")
        return False
    return value == "true"


def valid_date(value: str) -> bool:
    if not value:
        return True
    try:
        datetime.strptime(value, "%Y-%m-%d")
    except ValueError:
        return False
    return True


def validate() -> list[str]:
    issues: list[str] = []
    header, rows = read_contract()
    if not header:
        return [f"missing or empty contract: {CONTRACT.relative_to(ROOT).as_posix()}"]
    if header != REQUIRED_COLUMNS:
        issues.append(
            "contract header must match required columns exactly: "
            + ",".join(REQUIRED_COLUMNS)
        )
    if not rows:
        issues.append("contract has no rows")
        return issues

    seen_ids: set[str] = set()
    source_column_cache: dict[Path, set[str]] = {}

    for index, row in enumerate(rows, start=2):
        overlay_id = row.get("overlay_id", "")
        if not overlay_id:
            issues.append(f"row {index} missing overlay_id")
        elif not OVERLAY_ID_RE.match(overlay_id):
            issues.append(f"{overlay_id} must use lowercase snake_case overlay_id")
        elif overlay_id in seen_ids:
            issues.append(f"duplicate overlay_id: {overlay_id}")
        seen_ids.add(overlay_id)

        for column in ["source_layer", "source_file", "field_name", "allowed_consumers", "degraded_behavior", "effective_from", "change_reason"]:
            if not row.get(column, ""):
                issues.append(f"{overlay_id or f'row {index}'} missing required value: {column}")

        effect = row.get("allowed_effect", "")
        if effect not in ALLOWED_EFFECTS:
            issues.append(f"{overlay_id} has invalid allowed_effect={effect!r}")
        if effect != "disclosure_only":
            issues.append(f"{overlay_id} is not phase-one disclosure_only: allowed_effect={effect!r}")

        bools = {column: parse_bool(row, column, issues) for column in BOOLEAN_COLUMNS}
        if bools["score_allowed"]:
            issues.append(f"{overlay_id} violates phase-one contract: score_allowed must be false")
        if bools["ranking_allowed"]:
            issues.append(f"{overlay_id} violates phase-one contract: ranking_allowed must be false")
        if bools["reason_text_allowed"]:
            issues.append(f"{overlay_id} violates phase-one contract: reason_text_allowed must be false")
        if not bools["disclosure_only"]:
            issues.append(f"{overlay_id} violates phase-one contract: disclosure_only must be true")

        if effect in {"score_overlay", "ranking_modifier"} and not bools["requires_backtest"]:
            issues.append(f"{overlay_id} score/ranking effects require backtest evidence")
        if bools["score_allowed"] and not bools["requires_backtest"]:
            issues.append(f"{overlay_id} score_allowed requires backtest evidence")
        if bools["ranking_allowed"] and not bools["requires_backtest"]:
            issues.append(f"{overlay_id} ranking_allowed requires backtest evidence")

        degraded = row.get("degraded_behavior", "").lower()
        for marker in ["no_score", "no_rank", "no_reason"]:
            if marker not in degraded:
                issues.append(f"{overlay_id} degraded_behavior must include {marker}")
        if "degraded" in row.get("source_layer", "").lower() and (bools["score_allowed"] or bools["ranking_allowed"]):
            issues.append(f"{overlay_id} degraded source cannot allow score or ranking")

        consumers = [item.strip() for item in row.get("allowed_consumers", "").split(";") if item.strip()]
        if not consumers:
            issues.append(f"{overlay_id} has no allowed_consumers")
        unknown_consumers = sorted(set(consumers) - ALLOWED_CONSUMERS)
        if unknown_consumers:
            issues.append(f"{overlay_id} has unknown allowed_consumers: {unknown_consumers}")

        source_file = row.get("source_file", "")
        source_path = Path(source_file)
        if source_path.is_absolute():
            issues.append(f"{overlay_id} source_file must be repo-relative")
        if ".." in source_path.parts:
            issues.append(f"{overlay_id} source_file must not traverse outside the repo")
        if "onedrive" in source_file.lower() or "2026-06-11" in source_file:
            issues.append(f"{overlay_id} source_file must not use legacy/helper paths")

        full_source_path = ROOT / source_file
        if not full_source_path.exists():
            issues.append(f"{overlay_id} source_file does not exist: {source_file}")
        elif full_source_path.suffix.lower() == ".csv":
            columns = source_column_cache.setdefault(full_source_path, csv_columns(full_source_path))
            field_name = row.get("field_name", "")
            if field_name and field_name not in columns:
                issues.append(f"{overlay_id} field_name {field_name!r} not found in {source_file}")

        effective_from = row.get("effective_from", "")
        deprecated_after = row.get("deprecated_after", "")
        if not valid_date(effective_from):
            issues.append(f"{overlay_id} effective_from must use YYYY-MM-DD")
        if not valid_date(deprecated_after):
            issues.append(f"{overlay_id} deprecated_after must be blank or YYYY-MM-DD")
        if effective_from and deprecated_after and valid_date(effective_from) and valid_date(deprecated_after):
            if deprecated_after <= effective_from:
                issues.append(f"{overlay_id} deprecated_after must be after effective_from")

        pdf_approved = (
            bools["approved_for_daily_pdf"]
            or bools["approved_for_tdcc_weekly_pdf"]
            or bools["approved_for_individual_pdf"]
        )
        if pdf_approved and not bools["disclosure_only"]:
            issues.append(f"{overlay_id} PDF approvals require disclosure_only in phase one")
        if pdf_approved and (bools["score_allowed"] or bools["ranking_allowed"] or bools["reason_text_allowed"]):
            issues.append(f"{overlay_id} PDF approvals cannot carry score/ranking/reason effects in phase one")

    return issues


def disclosure_only_fields(rows: list[dict[str, str]]) -> list[str]:
    fields = []
    for row in rows:
        if row.get("disclosure_only", "").strip().lower() == "true":
            fields.append(f"{row.get('source_file', '')}:{row.get('field_name', '')}")
    return sorted(set(fields))


def main() -> int:
    _, rows = read_contract()
    issues = validate()
    if issues:
        for issue in issues:
            print(f"ERROR: {issue}")
        return 1
    fields = disclosure_only_fields(rows)
    print("event catalyst overlay contract validation passed")
    print(f"validated_contract={CONTRACT.relative_to(ROOT).as_posix()}")
    print(f"validated_rows={len(rows)}")
    print("phase_one_disclosure_only_fields=" + ";".join(fields))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
