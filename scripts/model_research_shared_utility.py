from __future__ import annotations

import csv
import hashlib
import subprocess
from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
UTILITY_REGISTRY = ROOT / "config/model_research_shared_utility_registry.csv"
MIGRATION_REGISTRY = ROOT / "config/model_research_shared_utility_migrations.csv"


@dataclass(frozen=True)
class SharedUtility:
    utility_path: str
    ownership_class: str
    semantic_scope: str
    consumer_models: tuple[str, ...]
    current_canonical_sha256: str
    change_policy: str
    required_validation_commands: tuple[str, ...]
    last_migration_id: str


@dataclass(frozen=True)
class SharedUtilityMigration:
    migration_id: str
    utility_path: str
    previous_canonical_sha256: str
    new_canonical_sha256: str
    affected_models: tuple[str, ...]
    validation_commands: tuple[str, ...]
    migration_status: str


def _items(value: str) -> tuple[str, ...]:
    return tuple(sorted(item.strip() for item in value.split(";") if item.strip()))


def canonical_text_sha256(path: Path) -> str:
    text = path.read_text(encoding="utf-8-sig")
    normalized = "\n".join(line.rstrip() for line in text.splitlines()).strip() + "\n"
    return hashlib.sha256(normalized.encode("utf-8")).hexdigest()


def load_shared_utilities(path: Path = UTILITY_REGISTRY) -> list[SharedUtility]:
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        rows = list(csv.DictReader(handle))
    required = {
        "utility_path",
        "ownership_class",
        "semantic_scope",
        "consumer_models",
        "current_canonical_sha256",
        "change_policy",
        "required_validation_commands",
        "last_migration_id",
    }
    if not rows or not required.issubset(rows[0]):
        raise RuntimeError("shared utility registry schema is incomplete")
    return [
        SharedUtility(
            utility_path=Path(row["utility_path"].strip()).as_posix(),
            ownership_class=row["ownership_class"].strip(),
            semantic_scope=row["semantic_scope"].strip(),
            consumer_models=_items(row["consumer_models"]),
            current_canonical_sha256=row["current_canonical_sha256"].strip().lower(),
            change_policy=row["change_policy"].strip(),
            required_validation_commands=_items(row["required_validation_commands"]),
            last_migration_id=row["last_migration_id"].strip(),
        )
        for row in rows
    ]


def load_shared_utility_migrations(path: Path = MIGRATION_REGISTRY) -> list[SharedUtilityMigration]:
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        rows = list(csv.DictReader(handle))
    required = {
        "migration_id",
        "utility_path",
        "previous_canonical_sha256",
        "new_canonical_sha256",
        "affected_models",
        "validation_commands",
        "migration_status",
    }
    if not rows or not required.issubset(rows[0]):
        raise RuntimeError("shared utility migration registry schema is incomplete")
    return [
        SharedUtilityMigration(
            migration_id=row["migration_id"].strip(),
            utility_path=Path(row["utility_path"].strip()).as_posix(),
            previous_canonical_sha256=row["previous_canonical_sha256"].strip().lower(),
            new_canonical_sha256=row["new_canonical_sha256"].strip().lower(),
            affected_models=_items(row["affected_models"]),
            validation_commands=_items(row["validation_commands"]),
            migration_status=row["migration_status"].strip(),
        )
        for row in rows
    ]


def changed_paths_against(base_ref: str, *, root: Path = ROOT) -> set[str]:
    result = subprocess.run(
        ["git", "diff", "--name-only", base_ref, "--"],
        cwd=root,
        check=True,
        capture_output=True,
        text=True,
        encoding="utf-8",
    )
    return {Path(line.strip()).as_posix() for line in result.stdout.splitlines() if line.strip()}


def validate_shared_utilities(*, root: Path = ROOT, base_ref: str | None = None) -> list[str]:
    errors: list[str] = []
    try:
        utilities = load_shared_utilities()
        migrations = load_shared_utility_migrations()
    except (OSError, RuntimeError) as exc:
        return [str(exc)]

    utility_paths = [item.utility_path for item in utilities]
    duplicates = sorted({path for path in utility_paths if utility_paths.count(path) > 1})
    if duplicates:
        errors.append(f"duplicate shared utility paths: {duplicates}")

    changed = changed_paths_against(base_ref, root=root) if base_ref else set()
    for utility in utilities:
        path = root / utility.utility_path
        if not path.is_file():
            errors.append(f"missing shared utility: {utility.utility_path}")
            continue
        actual_hash = canonical_text_sha256(path)
        if actual_hash != utility.current_canonical_sha256:
            errors.append(
                f"shared utility hash drift: path={utility.utility_path}; "
                f"expected={utility.current_canonical_sha256}; actual={actual_hash}"
            )
        if utility.change_policy != "cross_model_utility_migration_only":
            errors.append(f"shared utility change policy is not fail-closed: {utility.utility_path}")
        if len(utility.consumer_models) < 2:
            errors.append(f"shared utility must list every consumer model: {utility.utility_path}")
        if not utility.required_validation_commands:
            errors.append(f"shared utility missing consumer validators: {utility.utility_path}")

        matches = [
            migration
            for migration in migrations
            if migration.migration_id == utility.last_migration_id
            and migration.utility_path == utility.utility_path
        ]
        if len(matches) != 1:
            errors.append(f"shared utility must resolve to exactly one migration row: {utility.utility_path}")
            continue
        migration = matches[0]
        if migration.new_canonical_sha256 != utility.current_canonical_sha256:
            errors.append(f"shared utility migration hash mismatch: {utility.utility_path}")
        if migration.affected_models != utility.consumer_models:
            errors.append(f"shared utility migration consumer mismatch: {utility.utility_path}")
        if migration.validation_commands != utility.required_validation_commands:
            errors.append(f"shared utility migration validator mismatch: {utility.utility_path}")

        if utility.utility_path in changed and migration.migration_status != "validated_cross_model_migration":
            errors.append(
                f"changed shared utility lacks validated cross-model migration: {utility.utility_path}; "
                f"migration_status={migration.migration_status}"
            )
        if utility.utility_path in changed and not migration.previous_canonical_sha256:
            errors.append(f"changed shared utility migration lacks previous hash: {utility.utility_path}")
    return errors
