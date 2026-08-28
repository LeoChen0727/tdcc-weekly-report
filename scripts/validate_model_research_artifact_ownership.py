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
READINESS_FORMAL_SYNC_PRODUCER = (
    "scripts/sync_revenue_unreacted_range_operation_readiness.py"
)
LEGACY_BROAD_READINESS_PRODUCER = "scripts/build_model_operation_readiness.py"
OUTPUT_LATEST_ARTIFACT_INVENTORY = (
    ROOT / "config/output_latest_artifact_inventory.csv"
)
EXPECTED_READINESS_OUTPUT_INVENTORY_PATHS = {
    "output/latest/model_operation_readiness_latest.csv",
    "output/latest/model_operation_readiness_latest.md",
}
MIGRATION_REGISTRY = ROOT / "config/model_research_artifact_ownership_migrations.csv"
MIGRATION_COLUMNS = (
    "migration_id",
    "effective_date",
    "registry_path",
    "record_keys",
    "previous_owner",
    "new_owner",
    "change_policy",
    "approval_reference",
    "status",
    "notes",
)
EXPECTED_READINESS_MIGRATIONS = (
    {
        "migration_id": "revenue_readiness_docs_ownership_registration_v1",
        "effective_date": "2026-08-28",
        "registry_path": "config/model_research_artifact_ownership.csv",
        "record_keys": "docs/latest/model_operation_readiness_latest.*",
        "previous_owner": "unregistered",
        "new_owner": "model_governance",
        "change_policy": "formal_sync_only",
        "approval_reference": "user_authorized_3A_3C_20260828",
        "status": "validated_user_approved_migration",
        "notes": (
            "Register the previously absent docs readiness mirror without rewriting "
            "the pre-existing model-governance output readiness ownership."
        ),
    },
    {
        "migration_id": "revenue_readiness_output_inventory_owner_v1",
        "effective_date": "2026-08-28",
        "registry_path": "config/output_latest_artifact_inventory.csv",
        "record_keys": (
            "output/latest/model_operation_readiness_latest.csv;"
            "output/latest/model_operation_readiness_latest.md"
        ),
        "previous_owner": "research_backtest",
        "new_owner": "model_governance",
        "change_policy": "formal_sync_only",
        "approval_reference": "user_authorized_3A_3C_20260828",
        "status": "validated_user_approved_migration",
        "notes": (
            "Correct the two output-latest inventory records to the already canonical "
            "model-governance readiness owner."
        ),
    },
    {
        "migration_id": "revenue_readiness_lifecycle_inventory_owner_v1",
        "effective_date": "2026-08-28",
        "registry_path": "config/repo_file_lifecycle_inventory.csv",
        "record_keys": (
            "scripts/build_model_operation_readiness.py;"
            "scripts/validate_model_operation_readiness.py"
        ),
        "previous_owner": "research_backtest",
        "new_owner": "model_governance",
        "change_policy": "formal_sync_only",
        "approval_reference": "user_authorized_3A_3C_20260828",
        "status": "validated_user_approved_migration",
        "notes": (
            "Route builder and validator lifecycle ownership to the formal readiness owner."
        ),
    },
    {
        "migration_id": "revenue_readiness_production_inventory_owner_v1",
        "effective_date": "2026-08-28",
        "registry_path": "config/repo_production_inventory.csv",
        "record_keys": (
            "scripts/build_model_operation_readiness.py;"
            "scripts/validate_model_operation_readiness.py"
        ),
        "previous_owner": "research_backtest",
        "new_owner": "model_governance",
        "change_policy": "formal_sync_only",
        "approval_reference": "user_authorized_3A_3C_20260828",
        "status": "validated_user_approved_migration",
        "notes": (
            "Route builder and validator production inventory ownership to the formal "
            "readiness owner."
        ),
    },
)
REGISTRY_FACT_SPECS = {
    "config/model_research_artifact_ownership.csv": (
        "artifact_glob",
        "owner_model_id",
    ),
    "config/output_latest_artifact_inventory.csv": ("path", "owner_lane"),
    "config/repo_file_lifecycle_inventory.csv": ("path", "owner"),
    "config/repo_production_inventory.csv": ("path", "owner"),
}
PREEXISTING_OUTPUT_OWNERSHIP_KEY = (
    "config/model_research_artifact_ownership.csv",
    "output/latest/model_operation_readiness_latest.*",
)
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


def _base_path_bytes(base_ref: str, relative_path: str) -> bytes | None:
    result = subprocess.run(
        [
            "git",
            "--no-replace-objects",
            "show",
            f"{base_ref}:{relative_path}",
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


def _base_migration_bytes(base_ref: str) -> bytes | None:
    return _base_path_bytes(
        base_ref,
        "config/model_research_artifact_ownership_migrations.csv",
    )


def _base_registry_bytes(base_ref: str, registry_path: str) -> bytes | None:
    return _base_path_bytes(base_ref, registry_path)


def _registry_owner_map(
    data: bytes,
    registry_path: str,
) -> tuple[dict[str, str], list[str]]:
    key_column, owner_column = REGISTRY_FACT_SPECS[registry_path]
    try:
        reader = csv.DictReader(io.StringIO(data.decode("utf-8-sig")))
        fieldnames = tuple(reader.fieldnames or ())
        if key_column not in fieldnames or owner_column not in fieldnames:
            return {}, [
                f"ownership fact registry {registry_path} must contain "
                f"{key_column!r} and {owner_column!r}"
            ]
        rows = list(reader)
    except (UnicodeDecodeError, csv.Error) as exc:
        return {}, [f"invalid ownership fact registry {registry_path}: {exc}"]
    owners: dict[str, str] = {}
    errors: list[str] = []
    for row_number, row in enumerate(rows, start=2):
        key = row.get(key_column, "").strip()
        owner = row.get(owner_column, "").strip()
        if not key or not owner:
            errors.append(
                f"ownership fact registry {registry_path} row {row_number} has blank "
                f"{key_column!r} or {owner_column!r}"
            )
            continue
        if key in owners:
            errors.append(
                f"ownership fact registry {registry_path} has duplicate key {key!r}"
            )
            continue
        owners[key] = owner
    return owners, errors


def _record_keys(row: dict[str, str]) -> tuple[list[str], list[str]]:
    raw_keys = row.get("record_keys", "")
    keys = [key.strip() for key in raw_keys.split(";")]
    errors: list[str] = []
    if any(not key for key in keys):
        errors.append(
            f"ownership migration {row.get('migration_id', '')!r} contains a blank record key"
        )
    duplicates = sorted({key for key in keys if key and keys.count(key) > 1})
    if duplicates:
        errors.append(
            f"ownership migration {row.get('migration_id', '')!r} contains duplicate "
            f"record keys: {duplicates}"
        )
    return [key for key in keys if key], errors


def _current_registry_bytes(registry_path: str) -> bytes:
    return (ROOT / registry_path).read_bytes()


def _validate_migration_facts(
    current_rows: list[dict[str, str]],
    *,
    base_ref: str | None,
    new_rows: list[dict[str, str]],
) -> list[str]:
    errors: list[str] = []
    current_maps: dict[str, dict[str, str]] = {}
    base_maps: dict[str, dict[str, str]] = {}
    claimed_keys: set[tuple[str, str]] = set()

    for row in current_rows:
        migration_id = row.get("migration_id", "")
        registry_path = row.get("registry_path", "")
        if registry_path not in REGISTRY_FACT_SPECS:
            errors.append(
                f"ownership migration {migration_id!r} has unsupported registry_path "
                f"{registry_path!r}"
            )
            continue
        keys, key_errors = _record_keys(row)
        errors.extend(key_errors)
        if row.get("previous_owner") == row.get("new_owner"):
            errors.append(
                f"ownership migration {migration_id!r} must change owner"
            )
        for key in keys:
            identity = (registry_path, key)
            if identity in claimed_keys:
                errors.append(
                    "ownership migration registry contains duplicate registry/key claim: "
                    f"{registry_path}:{key}"
                )
            claimed_keys.add(identity)
        if registry_path not in current_maps:
            try:
                owners, owner_errors = _registry_owner_map(
                    _current_registry_bytes(registry_path),
                    registry_path,
                )
                current_maps[registry_path] = owners
                errors.extend(owner_errors)
            except OSError as exc:
                errors.append(
                    f"cannot read current ownership fact registry {registry_path}: {exc}"
                )
                current_maps[registry_path] = {}
        current_owners = current_maps[registry_path]
        for key in keys:
            observed = current_owners.get(key, "unregistered")
            if observed != row.get("new_owner"):
                errors.append(
                    f"ownership migration {migration_id!r} current fact mismatch for "
                    f"{registry_path}:{key}: expected new_owner={row.get('new_owner')!r}; "
                    f"observed={observed!r}"
                )

    if PREEXISTING_OUTPUT_OWNERSHIP_KEY in claimed_keys:
        errors.append(
            "pre-existing output/latest readiness ownership must not be represented as "
            "an ownership migration"
        )

    if base_ref:
        for row in new_rows:
            migration_id = row.get("migration_id", "")
            registry_path = row.get("registry_path", "")
            if registry_path not in REGISTRY_FACT_SPECS:
                continue
            if registry_path not in base_maps:
                try:
                    base_bytes = _base_registry_bytes(base_ref, registry_path)
                    if base_bytes is None:
                        errors.append(
                            f"base ownership fact registry is missing at {base_ref}: "
                            f"{registry_path}"
                        )
                        base_maps[registry_path] = {}
                    else:
                        owners, owner_errors = _registry_owner_map(
                            base_bytes,
                            registry_path,
                        )
                        base_maps[registry_path] = owners
                        errors.extend(f"base {error}" for error in owner_errors)
                except RuntimeError as exc:
                    errors.append(
                        f"cannot read base ownership fact registry {registry_path}: {exc}"
                    )
                    base_maps[registry_path] = {}
            keys, _key_errors = _record_keys(row)
            for key in keys:
                observed = base_maps[registry_path].get(key, "unregistered")
                if observed != row.get("previous_owner"):
                    errors.append(
                        f"ownership migration {migration_id!r} base fact mismatch for "
                        f"{registry_path}:{key}: expected previous_owner="
                        f"{row.get('previous_owner')!r}; observed={observed!r}"
                    )

        registry_path, record_key = PREEXISTING_OUTPUT_OWNERSHIP_KEY
        if registry_path not in base_maps:
            try:
                base_bytes = _base_registry_bytes(base_ref, registry_path)
                if base_bytes is not None:
                    owners, owner_errors = _registry_owner_map(base_bytes, registry_path)
                    base_maps[registry_path] = owners
                    errors.extend(f"base {error}" for error in owner_errors)
            except RuntimeError as exc:
                errors.append(
                    f"cannot verify pre-existing readiness ownership at {base_ref}: {exc}"
                )
        observed_base_owner = base_maps.get(registry_path, {}).get(
            record_key,
            "unregistered",
        )
        if observed_base_owner != "model_governance":
            errors.append(
                "base model research ownership fact for output/latest readiness must be "
                f"'model_governance', got {observed_base_owner!r}"
            )
    return errors


def validate_ownership_migrations(base_ref: str | None = None) -> list[str]:
    try:
        current_bytes = MIGRATION_REGISTRY.read_bytes()
    except OSError as exc:
        return [f"missing model research ownership migration registry: {exc}"]
    current_rows, errors = _migration_rows(current_bytes)
    current_by_id = {row.get("migration_id", ""): row for row in current_rows}
    for expected in EXPECTED_READINESS_MIGRATIONS:
        if current_by_id.get(expected["migration_id"]) != expected:
            errors.append(
                "model research ownership migration registry must contain exact "
                f"user-approved migration {expected['migration_id']!r}"
            )
    base_rows: list[dict[str, str]] = []
    new_rows: list[dict[str, str]] = []
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
                else:
                    new_rows = current_rows[len(base_rows):]
            else:
                new_rows = current_rows
        except RuntimeError as exc:
            errors.append(f"cannot validate ownership migration append-only base: {exc}")
    errors.extend(
        _validate_migration_facts(
            current_rows,
            base_ref=base_ref,
            new_rows=new_rows,
        )
    )
    return errors


def validate_readiness_output_inventory_producer() -> list[str]:
    errors: list[str] = []
    if not OUTPUT_LATEST_ARTIFACT_INVENTORY.exists():
        return [
            "missing output latest artifact inventory for readiness producer closure: "
            f"{OUTPUT_LATEST_ARTIFACT_INVENTORY.relative_to(ROOT).as_posix()}"
        ]
    with OUTPUT_LATEST_ARTIFACT_INVENTORY.open(
        "r",
        encoding="utf-8-sig",
        newline="",
    ) as handle:
        reader = csv.DictReader(handle)
        required = {"path", "owner_lane", "producer"}
        if reader.fieldnames is None or not required.issubset(reader.fieldnames):
            return [
                "output latest artifact inventory schema is incomplete for readiness "
                "producer closure"
            ]
        all_rows = [
            {key: (value or "").strip() for key, value in row.items()}
            for row in reader
            if (row.get("path") or "").strip()
        ]

    rows = [
        row
        for row in all_rows
        if row["path"] in EXPECTED_READINESS_OUTPUT_INVENTORY_PATHS
    ]
    formal_sync_paths = [
        row["path"]
        for row in all_rows
        if row["producer"] == READINESS_FORMAL_SYNC_PRODUCER
    ]
    if set(formal_sync_paths) != EXPECTED_READINESS_OUTPUT_INVENTORY_PATHS or (
        len(formal_sync_paths) != len(EXPECTED_READINESS_OUTPUT_INVENTORY_PATHS)
    ):
        errors.append(
            "formal readiness producer output inventory must close exactly over "
            "the two registered output/latest mirrors: "
            f"actual={sorted(formal_sync_paths)}"
        )

    paths = [row["path"] for row in rows]
    duplicate_paths = sorted({path for path in paths if paths.count(path) > 1})
    if duplicate_paths:
        errors.append(
            "duplicate readiness output inventory paths: "
            f"{duplicate_paths}"
        )
    missing_paths = sorted(EXPECTED_READINESS_OUTPUT_INVENTORY_PATHS - set(paths))
    if missing_paths:
        errors.append(
            "missing readiness output inventory paths: "
            f"{missing_paths}"
        )
    for row in rows:
        if row["owner_lane"] != "model_governance":
            errors.append(
                f"{row['path']} readiness output owner must be model_governance"
            )
        if row["producer"] != READINESS_FORMAL_SYNC_PRODUCER:
            errors.append(
                f"{row['path']} readiness output producer must be "
                f"{READINESS_FORMAL_SYNC_PRODUCER}"
            )
    if any(row["producer"] == LEGACY_BROAD_READINESS_PRODUCER for row in rows):
        errors.append(
            "legacy broad readiness builder must not own output latest readiness mirrors"
        )
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

    readiness_producer_rules = {
        (
            rule.owner_model_id,
            rule.artifact_glob,
            rule.artifact_class,
            rule.change_policy,
            rule.formal_evidence_status,
        )
        for rule in rules
        if rule.producer == READINESS_FORMAL_SYNC_PRODUCER
    }
    expected_readiness_producer_rules = {
        (
            "model_governance",
            artifact_glob,
            artifact_class,
            "formal_sync_only",
            "formal_evidence_pinned",
        )
        for artifact_glob, artifact_class in EXPECTED_READINESS_RULES
    }
    if readiness_producer_rules != expected_readiness_producer_rules:
        errors.append(
            "formal readiness producer ownership must close exactly over the two "
            "registered output/latest and docs/latest formal-sync mirrors"
        )
    legacy_readiness_rules = [
        rule.artifact_glob
        for rule in rules
        if rule.producer == LEGACY_BROAD_READINESS_PRODUCER
        and (
            rule.artifact_glob
            in {
                artifact_glob
                for artifact_glob, _artifact_class in EXPECTED_READINESS_RULES
            }
            or rule.artifact_class in {"formal_readiness", "formal_readiness_mirror"}
        )
    ]
    if legacy_readiness_rules:
        errors.append(
            "legacy broad readiness builder must not own formal readiness mirrors: "
            f"{sorted(legacy_readiness_rules)}"
        )
    errors.extend(validate_readiness_output_inventory_producer())
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
