from __future__ import annotations

import sys
from dataclasses import replace
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))

import model_research_shared_utility as shared  # noqa: E402


def test_shared_utility_registry_passes() -> None:
    assert shared.validate_shared_utilities() == []


def test_every_shared_utility_lists_multiple_consumers_and_validators() -> None:
    for utility in shared.load_shared_utilities():
        assert len(utility.consumer_models) >= 2
        assert utility.required_validation_commands
        assert utility.change_policy == "cross_model_utility_migration_only"


def test_changed_utility_requires_nonbaseline_migration(monkeypatch) -> None:
    utilities = shared.load_shared_utilities()
    migrations = shared.load_shared_utility_migrations()
    target = next(item for item in utilities if item.last_migration_id.startswith("baseline_"))
    monkeypatch.setattr(shared, "load_shared_utilities", lambda: utilities)
    monkeypatch.setattr(shared, "load_shared_utility_migrations", lambda: migrations)
    monkeypatch.setattr(shared, "changed_paths_against", lambda _base_ref, root=ROOT: {target.utility_path})
    errors = shared.validate_shared_utilities(base_ref="origin/main")
    assert any("lacks validated cross-model migration" in error for error in errors)


def test_validated_migration_requires_previous_hash(monkeypatch) -> None:
    utilities = shared.load_shared_utilities()
    migrations = shared.load_shared_utility_migrations()
    target = next(item for item in utilities if item.last_migration_id.startswith("baseline_"))
    patched = [
        replace(item, migration_status="validated_cross_model_migration")
        if item.migration_id == target.last_migration_id and item.utility_path == target.utility_path
        else item
        for item in migrations
    ]
    monkeypatch.setattr(shared, "load_shared_utilities", lambda: utilities)
    monkeypatch.setattr(shared, "load_shared_utility_migrations", lambda: patched)
    monkeypatch.setattr(shared, "changed_paths_against", lambda _base_ref, root=ROOT: {target.utility_path})
    errors = shared.validate_shared_utilities(base_ref="origin/main")
    assert any("lacks previous hash" in error for error in errors)
