from __future__ import annotations

import argparse
import csv
import io
import subprocess
from datetime import date
from pathlib import Path

from model_research_artifact_guard import (
    DEFAULT_REGISTRY,
    DEFAULT_SENTINEL_REGISTRY,
    ROOT,
    load_ownership_rules,
    load_protected_sentinels,
    protected_sentinel_snapshot,
)


REQUIRED_MODEL_PRODUCERS = {
    "revenue_unreacted_range": "scripts/build_revenue_unreacted_range_research.py",
    "price_pullback_23ema": "scripts/build_price_pullback_23ema_research.py",
    "volume_range_breakout_v2": "scripts/build_volume_range_breakout_v2_research.py",
}
REQUIRED_PROTECTED_CLASSES = {
    "formal_operation_adapter",
    "production_snapshot",
    "formal_readiness",
    "formal_approval",
    "cross_model_aggregate",
}
MIGRATION_REGISTRY = ROOT / "config/model_research_artifact_ownership_migrations.csv"
MIGRATION_COLUMNS = (
    "migration_id",
    "effective_date",
    "artifact_glob",
    "previous_owner",
    "new_owner",
    "change_policy",
    "approval_reference",
    "status",
    "notes",
)
EXPECTED_READINESS_MIGRATION = {
    "migration_id": "revenue_readiness_formal_sync_owner_closure_v1",
    "effective_date": "2026-08-28",
    "artifact_glob": (
        "output/latest/model_operation_readiness_latest.*;"
        "docs/latest/model_operation_readiness_latest.*"
    ),
    "previous_owner": "research_backtest;unregistered_docs_mirror",
    "new_owner": "model_governance",
    "change_policy": "formal_sync_only",
    "approval_reference": "user_authorized_3A_3C_20260828",
    "status": "validated_user_approved_migration",
    "notes": (
        "Research workflows remain forbidden; only trusted-main content-addressed "
        "formal sync may prepare and publish these four mirrors."
    ),
}
EXPECTED_READINESS_RULES = {
    (
        "output/latest/model_operation_readiness_latest.*",
        "formal_readiness",
    ),
    (
        "docs/latest/model_operation_readiness_latest.*",
        "formal_readiness_mirror",
    ),
}


def _migration_rows(data: bytes) -> tuple[list[dict[str, str]], list[str]]:
    errors: list[str] = []
    try:
        reader = csv.DictReader(io.StringIO(data.decode("utf-8-sig")))
        if tuple(reader.fieldnames or ()) != MIGRATION_COLUMNS:
            return [], [
                "model research ownership migration schema must be exact: "
                f"expected={list(MIGRATION_COLUMNS)!r}; actual={reader.fieldnames!r}"
            ]
        rows = list(reader)
    except (UnicodeDecodeError, csv.Error) as exc:
        return [], [f"invalid model research ownership migration CSV: {exc}"]
    for row_number, row in enumerate(rows, start=2):
        blank_fields = [field for field in MIGRATION_COLUMNS if not row.get(field, "").strip()]
        if blank_fields:
            errors.append(
                f"model research ownership migration row {row_number} has blank fields: "
                f"{blank_fields}"
            )
        try:
            date.fromisoformat(row.get("effective_date", ""))
        except ValueError:
            errors.append(
                f"model research ownership migration row {row_number} has invalid effective_date"
            )
    ids = [row.get("migration_id", "").strip() for row in rows]
    duplicates = sorted({migration_id for migration_id in ids if ids.count(migration_id) > 1})
    if duplicates:
        errors.append(f"duplicate model research ownership migration_id values: {duplicates}")
    return rows, errors


def _base_migration_bytes(base_ref: str) -> bytes | None:
    result = subprocess.run(
        [
            "git",
            "--no-replace-objects",
            "show",
            f"{base_ref}:config/model_research_artifact_ownership_migrations.csv",
        ],
        cwd=ROOT,
        check=False,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    if result.returncode == 0:
        return result.stdout
    error = result.stderr.decode("utf-8", errors="replace")
    if "exists on disk, but not in" in error or "does not exist in" in error:
        return None
    raise RuntimeError(error.strip())


def validate_ownership_migrations(base_ref: str | None = None) -> list[str]:
    try:
        current_bytes = MIGRATION_REGISTRY.read_bytes()
    except OSError as exc:
        return [f"missing model research ownership migration registry: {exc}"]
    current_rows, errors = _migration_rows(current_bytes)
    expected_rows = [
        row for row in current_rows
        if row.get("migration_id") == EXPECTED_READINESS_MIGRATION["migration_id"]
    ]
    if expected_rows != [EXPECTED_READINESS_MIGRATION]:
        errors.append(
            "model research ownership migration registry must contain the exact "
            "user-approved readiness owner closure"
        )
    if base_ref:
        try:
            base_bytes = _base_migration_bytes(base_ref)
            if base_bytes is not None:
                base_rows, base_errors = _migration_rows(base_bytes)
                errors.extend(f"base {error}" for error in base_errors)
                if current_rows[: len(base_rows)] != base_rows:
                    errors.append(
                        "model research ownership migrations must be append-only relative "
                        f"to {base_ref}"
                    )
        except RuntimeError as exc:
            errors.append(f"cannot validate ownership migration append-only base: {exc}")
    return errors


def validate(base_ref: str | None = None) -> list[str]:
    errors: list[str] = []
    try:
        rules = load_ownership_rules(DEFAULT_REGISTRY)
    except RuntimeError as exc:
        return [str(exc)]

    patterns = [rule.artifact_glob for rule in rules]
    duplicates = sorted({pattern for pattern in patterns if patterns.count(pattern) > 1})
    if duplicates:
        errors.append(f"duplicate artifact ownership globs: {duplicates}")

    model_owned_model_ids = sorted(
        {rule.owner_model_id for rule in rules if rule.change_policy == "model_owned_write"}
    )
    missing_required_models = sorted(set(REQUIRED_MODEL_PRODUCERS) - set(model_owned_model_ids))
    if missing_required_models:
        errors.append(f"missing required model-owned producers: {missing_required_models}")

    for model_id in model_owned_model_ids:
        rows = [rule for rule in rules if rule.owner_model_id == model_id and rule.change_policy == "model_owned_write"]
        if not rows:
            errors.append(f"{model_id} missing model_owned_write rows")
            continue
        producers = {row.producer for row in rows}
        if len(producers) != 1:
            errors.append(f"{model_id} must have exactly one model-owned producer: {sorted(producers)}")
            continue
        producer = next(iter(producers))
        expected_producer = REQUIRED_MODEL_PRODUCERS.get(model_id)
        if expected_producer and producer != expected_producer:
            errors.append(f"{model_id} producer must be {expected_producer}")
        path = ROOT / producer
        if not path.exists():
            errors.append(f"missing model-owned producer: {producer}")
            continue
        text = path.read_text(encoding="utf-8")
        if "model_owned_artifact_guard" not in text:
            errors.append(f"{producer} must invoke model_owned_artifact_guard")

    protected = {rule.artifact_class for rule in rules if rule.change_policy != "model_owned_write"}
    missing_protected = sorted(REQUIRED_PROTECTED_CLASSES - protected)
    if missing_protected:
        errors.append(f"missing protected artifact classes: {missing_protected}")

    readiness_rules = {
        (rule.artifact_glob, rule.artifact_class)
        for rule in rules
        if rule.owner_model_id == "model_governance"
        and rule.producer == "scripts/build_model_operation_readiness.py"
        and rule.change_policy == "formal_sync_only"
        and rule.formal_evidence_status == "formal_evidence_pinned"
    }
    if readiness_rules != EXPECTED_READINESS_RULES:
        errors.append(
            "model operation readiness ownership must close exactly over output/latest "
            "and docs/latest formal-sync mirrors"
        )
    errors.extend(validate_ownership_migrations(base_ref))

    legacy_rows = [rule for rule in rules if rule.producer == "scripts/build_daily_model_parameter_research.py"]
    if not legacy_rows or {row.change_policy for row in legacy_rows} != {"cross_model_migration_only"}:
        errors.append("legacy cross-model parameter research outputs must be cross_model_migration_only")

    try:
        sentinels = load_protected_sentinels()
        _snapshot, sentinel_errors = protected_sentinel_snapshot(ROOT, sentinels)
        errors.extend(sentinel_errors)
    except RuntimeError as exc:
        errors.append(str(exc))
        sentinels = []
    required_sentinel_classes = {
        "formal_contract",
        "formal_evidence",
        "formal_operation_adapter",
        "formal_readiness",
        "production_snapshot",
    }
    actual_sentinel_classes = {sentinel.sentinel_class for sentinel in sentinels}
    missing_sentinel_classes = sorted(required_sentinel_classes - actual_sentinel_classes)
    if missing_sentinel_classes:
        errors.append(f"missing protected sentinel classes: {missing_sentinel_classes}")

    return errors


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--base-ref")
    args = parser.parse_args()
    errors = validate(args.base_ref)
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1
    print(f"model research artifact ownership validation passed: {DEFAULT_REGISTRY.relative_to(ROOT)}")
    print(f"protected sentinel registry passed: {DEFAULT_SENTINEL_REGISTRY.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
