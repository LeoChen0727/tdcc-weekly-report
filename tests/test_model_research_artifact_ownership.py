from __future__ import annotations

from contextlib import contextmanager
import csv
from dataclasses import replace
import io
import sys
from pathlib import Path
from types import SimpleNamespace

import pytest


ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))

from model_research_artifact_guard import (  # noqa: E402
    compare_protected_sentinel_snapshots,
    load_ownership_rules,
    load_protected_sentinels,
    protected_sentinel_snapshot,
    protected_sentinel_aggregate_sha256,
    validate_changed_paths,
)
from validate_model_research_artifact_ownership import (  # noqa: E402
    EXPECTED_READINESS_MIGRATIONS,
    EXPECTED_READINESS_RULES,
    LEGACY_BROAD_READINESS_PRODUCER,
    MIGRATION_COLUMNS,
    READINESS_FORMAL_SYNC_PRODUCER,
    REQUIRED_MODEL_PRODUCERS,
    validate,
    validate_ownership_migrations,
    validate_readiness_output_inventory_producer,
)
import model_research_artifact_guard as guard_module  # noqa: E402
import validate_model_research_artifact_ownership as ownership_validator  # noqa: E402


REVENUE_PRODUCER = "scripts/build_revenue_unreacted_" + "range_research.py"
LEGACY_CROSS_MODEL_PRODUCER = "scripts/build_daily_model_" + "parameter_research.py"
VOLUME_V2_PRODUCER = "build_volume_range_breakout_" + "v2_research.py"
FORBIDDEN_VOLUME_V2_BUILDERS = (
    "build_approved_operation_" + "patterns.py",
    "build_model_operation_" + "readiness.py",
    "build_volume_breakout_confirmed_" + "operation_backtest.py",
    "build_daily_w_bottom_" + "operation_sections.py",
)
FOUR_MODEL_IDS = (
    "hot_theme_pullback",
    "pullback_short_reclaim",
    "tdcc_stealth_accumulation",
    "tdcc_short_term_continuation_d5_d10",
)
FOUR_MODEL_PRODUCERS = {
    "hot_theme_pullback": "scripts/build_hot_theme_pullback_research.py",
    "pullback_short_reclaim": "scripts/build_pullback_short_reclaim_research.py",
    "tdcc_stealth_accumulation": (
        "scripts/build_tdcc_stealth_accumulation_research.py"
    ),
    "tdcc_short_term_continuation_d5_d10": (
        "scripts/build_tdcc_short_term_continuation_d5_d10_research.py"
    ),
}
FOUR_MODEL_OWNERSHIP_CLASSES = {
    "hot_theme_pullback": {
        (
            "output/latest/research_backtest/hot_theme_pullback_*",
            "model_research_output",
        ),
        (
            "output/history/research/hot_theme_pullback_*",
            "model_research_history",
        ),
        ("docs/latest/hot_theme_pullback_*", "model_research_docs"),
    },
    "pullback_short_reclaim": {
        (
            "output/latest/research_backtest/pullback_short_reclaim_*",
            "model_research_output",
        ),
    },
    "tdcc_stealth_accumulation": {
        (
            "output/research/tdcc_stealth_accumulation/"
            "tdcc_stealth_accumulation_actual_recommendation_replay_*_v1.csv",
            "model_research_output",
        ),
    },
    "tdcc_short_term_continuation_d5_d10": {
        (
            "output/latest/research_backtest/"
            "tdcc_short_term_continuation_d5_d10_research_*",
            "model_research_output",
        ),
    },
}
FOUR_MODEL_MIGRATION_RECORD_KEYS = {
    "hot_theme_pullback": (
        "output/latest/research_backtest/hot_theme_pullback_*;"
        "output/history/research/hot_theme_pullback_*;"
        "docs/latest/hot_theme_pullback_*"
    ),
    "pullback_short_reclaim": (
        "output/latest/research_backtest/pullback_short_reclaim_*"
    ),
    "tdcc_stealth_accumulation": (
        "output/research/tdcc_stealth_accumulation/"
        "tdcc_stealth_accumulation_actual_recommendation_replay_*_v1.csv"
    ),
    "tdcc_short_term_continuation_d5_d10": (
        "output/latest/research_backtest/"
        "tdcc_short_term_continuation_d5_d10_research_*"
    ),
}
FOUR_MODEL_MIGRATION_NOTES = {
    "hot_theme_pullback": (
        "Register the model-owned hot_theme_pullback latest history and docs "
        "research-only artifact families before workflow execution."
    ),
    "pullback_short_reclaim": (
        "Register the model-owned pullback_short_reclaim latest research-only "
        "artifact family before workflow execution."
    ),
    "tdcc_stealth_accumulation": (
        "Register the model-owned tdcc_stealth_accumulation v1 research-only "
        "artifact family before workflow execution."
    ),
    "tdcc_short_term_continuation_d5_d10": (
        "Register the model-owned tdcc_short_term_continuation_d5_d10 latest "
        "research-only artifact family before workflow execution."
    ),
}
EXPECTED_FOUR_MODEL_MIGRATIONS = tuple(
    {
        "migration_id": f"{model_id}_research_artifact_registration_v1",
        "effective_date": "2026-09-02",
        "registry_path": "config/model_research_artifact_ownership.csv",
        "record_keys": FOUR_MODEL_MIGRATION_RECORD_KEYS[model_id],
        "previous_owner": "unregistered",
        "new_owner": model_id,
        "change_policy": "model_owned_write",
        "approval_reference": (
            "user_authorized_four_model_artifact_workflow_registration_20260902"
        ),
        "status": "validated_user_approved_migration",
        "notes": FOUR_MODEL_MIGRATION_NOTES[model_id],
    }
    for model_id in FOUR_MODEL_IDS
)

TDCC_STEALTH_PIT_AUDIT_OWNER = (
    "tdcc_stealth_accumulation_pit_replay_availability_audit"
)
TDCC_STEALTH_PIT_AUDIT_PRODUCER = (
    "scripts/audit_tdcc_stealth_accumulation_pit_replay_availability.py"
)
TDCC_STEALTH_PIT_AUDIT_ARTIFACT = (
    "output/research/tdcc_stealth_accumulation/"
    "tdcc_stealth_accumulation_pit_replay_availability_audit_v1.csv"
)
TDCC_STEALTH_PIT_AUDIT_MIGRATION_ID = (
    "tdcc_stealth_accumulation_pit_replay_availability_audit_registration_v1"
)
TDCC_STEALTH_PIT_AUDIT_APPROVAL = (
    "user_requested_tdcc_stealth_accumulation_pit_historical_replay_"
    "availability_audit_20260903"
)


def test_model_research_artifact_ownership_registry_passes() -> None:
    assert validate() == []


def test_four_model_research_ownership_is_exact_and_research_only() -> None:
    rules = load_ownership_rules()
    assert {
        model_id: REQUIRED_MODEL_PRODUCERS[model_id]
        for model_id in FOUR_MODEL_IDS
    } == FOUR_MODEL_PRODUCERS

    for model_id in FOUR_MODEL_IDS:
        observed = {
            (
                rule.producer,
                rule.artifact_glob,
                rule.artifact_class,
                rule.change_policy,
                rule.formal_evidence_status,
            )
            for rule in rules
            if rule.owner_model_id == model_id
            and rule.change_policy == "model_owned_write"
        }
        expected = {
            (
                FOUR_MODEL_PRODUCERS[model_id],
                artifact_glob,
                artifact_class,
                "model_owned_write",
                "research_only",
            )
            for artifact_glob, artifact_class in FOUR_MODEL_OWNERSHIP_CLASSES[
                model_id
            ]
        }
        assert observed == expected


def test_four_model_ownership_migrations_are_exact() -> None:
    with (
        ROOT / "config/model_research_artifact_ownership_migrations.csv"
    ).open(encoding="utf-8-sig", newline="") as handle:
        rows = list(csv.DictReader(handle))
    current_by_id = {row["migration_id"]: row for row in rows}

    assert tuple(
        current_by_id[expected["migration_id"]]
        for expected in EXPECTED_FOUR_MODEL_MIGRATIONS
    ) == EXPECTED_FOUR_MODEL_MIGRATIONS


def test_tdcc_stealth_pit_replay_availability_audit_has_independent_owner() -> None:
    rules = load_ownership_rules()
    observed = [
        rule
        for rule in rules
        if rule.artifact_glob == TDCC_STEALTH_PIT_AUDIT_ARTIFACT
    ]

    assert len(observed) == 1
    rule = observed[0]
    assert rule.owner_model_id == TDCC_STEALTH_PIT_AUDIT_OWNER
    assert rule.producer == TDCC_STEALTH_PIT_AUDIT_PRODUCER
    assert rule.artifact_class == "model_research_output"
    assert rule.change_policy == "model_owned_write"
    assert rule.formal_evidence_status == "research_only"

    assert validate_changed_paths(
        TDCC_STEALTH_PIT_AUDIT_OWNER,
        TDCC_STEALTH_PIT_AUDIT_PRODUCER,
        [TDCC_STEALTH_PIT_AUDIT_ARTIFACT],
        rules,
    ) == []
    assert validate_changed_paths(
        "tdcc_stealth_accumulation",
        TDCC_STEALTH_PIT_AUDIT_PRODUCER,
        [TDCC_STEALTH_PIT_AUDIT_ARTIFACT],
        rules,
    )

    with (ROOT / "config/report_artifact_lineage.csv").open(
        encoding="utf-8-sig", newline=""
    ) as handle:
        lineage_rows = {
            row["artifact_path"]: row for row in csv.DictReader(handle)
        }
    with (ROOT / "config/daily_model_background_data_registry.csv").open(
        encoding="utf-8-sig", newline=""
    ) as handle:
        background = {
            row["data_family_id"]: row for row in csv.DictReader(handle)
        }
    lineage = lineage_rows[TDCC_STEALTH_PIT_AUDIT_ARTIFACT]
    assert lineage["artifact_kind"] == "research_model_pit_replay_availability_audit"
    assert lineage["owner"] == "research_backtest"
    assert lineage["producer"] == TDCC_STEALTH_PIT_AUDIT_PRODUCER
    assert lineage["validator"] == (
        "scripts/validate_tdcc_stealth_accumulation_pit_replay_availability.py"
    )
    assert lineage["source_artifacts"] == background[
        TDCC_STEALTH_PIT_AUDIT_OWNER
    ]["source_artifacts"]
    assert lineage["publisher"] == "manual_daily_model_maintenance_pr"
    assert lineage["public_surface"] == "output/research/tdcc_stealth_accumulation"


def test_tdcc_stealth_pit_replay_availability_audit_migration_is_exact() -> None:
    with (
        ROOT / "config/model_research_artifact_ownership_migrations.csv"
    ).open(encoding="utf-8-sig", newline="") as handle:
        rows = {row["migration_id"]: row for row in csv.DictReader(handle)}

    migration = rows[TDCC_STEALTH_PIT_AUDIT_MIGRATION_ID]
    assert migration == {
        "migration_id": TDCC_STEALTH_PIT_AUDIT_MIGRATION_ID,
        "effective_date": "2026-09-03",
        "registry_path": "config/model_research_artifact_ownership.csv",
        "record_keys": TDCC_STEALTH_PIT_AUDIT_ARTIFACT,
        "previous_owner": "unregistered",
        "new_owner": TDCC_STEALTH_PIT_AUDIT_OWNER,
        "change_policy": "model_owned_write",
        "approval_reference": TDCC_STEALTH_PIT_AUDIT_APPROVAL,
        "status": "validated_user_approved_migration",
        "notes": (
            "Register the TDCC stealth accumulation model-specific PIT replay "
            "availability audit artifact as research-only evidence that cannot "
            "contain replay events performance metrics formal evidence or "
            "promotion evidence."
        ),
    }


@pytest.mark.parametrize("model_id", FOUR_MODEL_IDS)
def test_four_model_artifact_guard_accepts_only_exact_owner_and_producer(
    model_id: str,
) -> None:
    rules = load_ownership_rules()
    producer = FOUR_MODEL_PRODUCERS[model_id]
    artifact_glob = sorted(FOUR_MODEL_OWNERSHIP_CLASSES[model_id])[0][0]
    sample_path = artifact_glob.replace("*", "ownership_probe.csv")

    assert validate_changed_paths(model_id, producer, [sample_path], rules) == []
    wrong_producer_errors = validate_changed_paths(
        model_id,
        LEGACY_CROSS_MODEL_PRODUCER,
        [sample_path],
        rules,
    )
    assert wrong_producer_errors and "wrong producer" in wrong_producer_errors[0]
    cross_model_errors = validate_changed_paths(
        "revenue_unreacted_range",
        producer,
        [sample_path],
        rules,
    )
    assert cross_model_errors and "cross-model artifact change" in cross_model_errors[0]


def test_four_model_required_producer_rows_fail_closed_when_removed(
    monkeypatch,
) -> None:
    rules = [
        rule
        for rule in load_ownership_rules()
        if rule.owner_model_id not in FOUR_MODEL_IDS
    ]
    monkeypatch.setattr(
        ownership_validator,
        "load_ownership_rules",
        lambda _registry: rules,
    )

    errors = validate()

    assert (
        f"missing required model-owned producers: {sorted(FOUR_MODEL_IDS)}"
        in errors
    )


def _write_ownership_migrations(path: Path, rows: list[dict[str, str]]) -> None:
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=MIGRATION_COLUMNS,
            lineterminator="\n",
        )
        writer.writeheader()
        writer.writerows(rows)


def test_readiness_owner_closure_and_exact_migration_are_canonical() -> None:
    rules = load_ownership_rules()
    readiness_rules = {
        (rule.artifact_glob, rule.artifact_class)
        for rule in rules
        if rule.owner_model_id == "model_governance"
        and rule.producer == READINESS_FORMAL_SYNC_PRODUCER
        and rule.change_policy == "formal_sync_only"
        and rule.formal_evidence_status == "formal_evidence_pinned"
    }
    assert readiness_rules == EXPECTED_READINESS_RULES
    assert not any(
        rule.producer == LEGACY_BROAD_READINESS_PRODUCER
        and rule.artifact_class in {"formal_readiness", "formal_readiness_mirror"}
        for rule in rules
    )
    assert validate_readiness_output_inventory_producer() == []
    assert validate_ownership_migrations() == []


def test_readiness_exact_child_dependencies_and_writer_lineage_are_registered() -> None:
    producer = "scripts/sync_revenue_unreacted_range_operation_readiness.py"
    with (ROOT / "config/repo_file_lifecycle_inventory.csv").open(
        encoding="utf-8", newline=""
    ) as handle:
        lifecycle_rows = list(csv.DictReader(handle))
    lifecycle = next(row for row in lifecycle_rows if row["path"] == producer)
    for token in (
        "revenue_unreacted_range_forward_holdout_v2",
        "validate_revenue_unreacted_range_forward_holdout_v2",
        "without importing research-owner raw-truth code",
        "independent raw monthly truth remains with research-owner CI",
        "trusted same-model in-memory child",
        "post-child repository cleanliness",
    ):
        assert token in lifecycle["keep_reason"]
    expected_outputs = {
        "output/latest/model_operation_readiness_latest.csv",
        "output/latest/model_operation_readiness_latest.md",
        "docs/latest/model_operation_readiness_latest.csv",
        "docs/latest/model_operation_readiness_latest.md",
    }
    assert set(lifecycle["writes_artifact"].split(";")) == expected_outputs
    assert "config/revenue_unreacted_range_promotion_preparation_registry.csv" in set(
        lifecycle["reads_artifact"].split(";")
    )
    with (ROOT / "config/report_artifact_lineage.csv").open(
        encoding="utf-8", newline=""
    ) as handle:
        lineage_rows = [
            row
            for row in csv.DictReader(handle)
            if row["producer"] == producer
        ]
    assert {row["artifact_path"] for row in lineage_rows} == expected_outputs
    assert all(
        row["validator"]
        == (
            "scripts/validate_model_operation_readiness.py;"
            "scripts/validate_revenue_unreacted_range_readiness_formal_sync.py"
        )
        for row in lineage_rows
    )

    with (ROOT / "config/repo_production_inventory.csv").open(
        encoding="utf-8", newline=""
    ) as handle:
        production_rows = list(csv.DictReader(handle))
    production = next(row for row in production_rows if row["path"] == producer)
    assert "trusted same-model in-memory replay" in production["purpose"]
    assert "post-child repository-cleanliness hard gate" in production["purpose"]
    assert production["allowed_stage_patterns"] == ""

    with (ROOT / "config/model_research_artifact_ownership.csv").open(
        encoding="utf-8", newline=""
    ) as handle:
        ownership_rows = [
            row
            for row in csv.DictReader(handle)
            if row["producer"] == producer
        ]
    assert len(ownership_rows) == 2
    ownership_notes = " ".join(row["notes"] for row in ownership_rows)
    assert "trusted same-model in-memory producer" in ownership_notes
    assert "replay-child called APIs do not include artifact writers" in ownership_notes
    assert "writes only the exact four readiness mirrors" in ownership_notes

    spec = (
        ROOT / "docs/specs/revenue_unreacted_range_readiness_formal_sync_v1.md"
    ).read_text(encoding="utf-8")
    for token in (
        "temporary clean detached worktree",
        "validate_v1_exact17_freeze",
        "build all five v2 frames",
        "reviewed same-model in-memory producer",
        "`-I -B`",
        "post-child clean Git status",
        "do not import research-owner code",
        "validate_revenue_unreacted_range_forward_holdout_v2.py",
        "Raw monthly",
        "provenance diagnostic",
        "four readiness mirrors",
    ):
        assert token in spec


def test_readiness_owner_closure_rejects_legacy_broad_builder(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    rules = load_ownership_rules()
    mutated = [
        replace(rule, producer=LEGACY_BROAD_READINESS_PRODUCER)
        if rule.producer == READINESS_FORMAL_SYNC_PRODUCER
        else rule
        for rule in rules
    ]
    monkeypatch.setattr(
        ownership_validator,
        "load_ownership_rules",
        lambda _path: mutated,
    )

    errors = validate()

    assert any("legacy broad readiness builder" in error for error in errors)


def test_readiness_owner_closure_rejects_additional_formal_sync_rule(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    rules = load_ownership_rules()
    template = next(
        rule for rule in rules if rule.producer == READINESS_FORMAL_SYNC_PRODUCER
    )
    mutated = [
        *rules,
        replace(
            template,
            owner_model_id="shadow_owner",
            artifact_glob="output/latest/model_operation_readiness_shadow_latest.*",
            artifact_class="shadow_readiness",
        ),
    ]
    monkeypatch.setattr(
        ownership_validator,
        "load_ownership_rules",
        lambda _path: mutated,
    )

    errors = validate()

    assert any(
        "formal readiness producer ownership must close exactly" in error
        for error in errors
    )


def test_output_readiness_inventory_rejects_legacy_broad_builder(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    inventory_path = tmp_path / "output_latest_artifact_inventory.csv"
    with inventory_path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=("path", "owner_lane", "producer"),
            lineterminator="\n",
        )
        writer.writeheader()
        for suffix in ("csv", "md"):
            writer.writerow(
                {
                    "path": (
                        "output/latest/model_operation_readiness_latest."
                        f"{suffix}"
                    ),
                    "owner_lane": "model_governance",
                    "producer": LEGACY_BROAD_READINESS_PRODUCER,
                }
            )
    monkeypatch.setattr(
        ownership_validator,
        "OUTPUT_LATEST_ARTIFACT_INVENTORY",
        inventory_path,
    )

    errors = validate_readiness_output_inventory_producer()

    assert any("readiness output producer must be" in error for error in errors)
    assert any("legacy broad readiness builder" in error for error in errors)


def test_output_readiness_inventory_rejects_additional_formal_sync_path(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    inventory_path = tmp_path / "output_latest_artifact_inventory.csv"
    with inventory_path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=("path", "owner_lane", "producer"),
            lineterminator="\n",
        )
        writer.writeheader()
        for suffix in ("csv", "md"):
            writer.writerow(
                {
                    "path": (
                        "output/latest/model_operation_readiness_latest."
                        f"{suffix}"
                    ),
                    "owner_lane": "model_governance",
                    "producer": READINESS_FORMAL_SYNC_PRODUCER,
                }
            )
        writer.writerow(
            {
                "path": "output/latest/model_operation_readiness_shadow_latest.csv",
                "owner_lane": "shadow_owner",
                "producer": READINESS_FORMAL_SYNC_PRODUCER,
            }
        )
    monkeypatch.setattr(
        ownership_validator,
        "OUTPUT_LATEST_ARTIFACT_INVENTORY",
        inventory_path,
    )

    errors = validate_readiness_output_inventory_producer()

    assert any(
        "formal readiness producer output inventory must close exactly" in error
        for error in errors
    )


@pytest.mark.parametrize(
    ("mutation", "message"),
    (
        ("blank", "blank fields"),
        ("duplicate", "duplicate model research ownership migration_id"),
        ("invalid_date", "invalid effective_date"),
        ("wrong_approval", "exact user-approved migration"),
    ),
)
def test_ownership_migration_rejects_blank_duplicate_date_and_approval_mutations(
    tmp_path: Path,
    monkeypatch,
    mutation: str,
    message: str,
) -> None:
    rows = [dict(row) for row in EXPECTED_READINESS_MIGRATIONS]
    if mutation == "blank":
        rows[0]["approval_reference"] = ""
    elif mutation == "duplicate":
        rows.append(dict(rows[0]))
    elif mutation == "invalid_date":
        rows[0]["effective_date"] = "2026-99-99"
    elif mutation == "wrong_approval":
        rows[0]["approval_reference"] = "self_authorized"
    path = tmp_path / "migrations.csv"
    _write_ownership_migrations(path, rows)
    monkeypatch.setattr(ownership_validator, "MIGRATION_REGISTRY", path)
    assert any(message in error for error in validate_ownership_migrations())


def test_ownership_migration_append_only_base_rejects_rewrite(
    tmp_path: Path,
    monkeypatch,
) -> None:
    current = dict(EXPECTED_READINESS_MIGRATIONS[0])
    path = tmp_path / "migrations.csv"
    _write_ownership_migrations(path, [current])
    base = dict(current)
    base["notes"] = "immutable prior value"
    base_path = tmp_path / "base.csv"
    _write_ownership_migrations(base_path, [base])
    monkeypatch.setattr(ownership_validator, "MIGRATION_REGISTRY", path)
    monkeypatch.setattr(
        ownership_validator,
        "_base_migration_bytes",
        lambda _base_ref: base_path.read_bytes(),
    )
    assert any(
        "append-only" in error
        for error in validate_ownership_migrations("base-ref")
    )


def _fact_registry_bytes(
    registry_path: str,
    owners: dict[str, str],
) -> bytes:
    key_column, owner_column = ownership_validator.REGISTRY_FACT_SPECS[registry_path]
    stream = io.StringIO()
    writer = csv.DictWriter(
        stream,
        fieldnames=[key_column, owner_column],
        lineterminator="\n",
    )
    writer.writeheader()
    for key, owner in owners.items():
        writer.writerow({key_column: key, owner_column: owner})
    return stream.getvalue().encode()


def _canonical_migration_fact_maps() -> tuple[
    dict[str, bytes],
    dict[str, bytes],
]:
    model_registry = "config/model_research_artifact_ownership.csv"
    output_inventory = "config/output_latest_artifact_inventory.csv"
    lifecycle_inventory = "config/repo_file_lifecycle_inventory.csv"
    production_inventory = "config/repo_production_inventory.csv"
    output_glob = "output/latest/model_operation_readiness_latest.*"
    docs_glob = "docs/latest/model_operation_readiness_latest.*"
    readiness_paths = {
        "output/latest/model_operation_readiness_latest.csv",
        "output/latest/model_operation_readiness_latest.md",
    }
    scripts = {
        "scripts/build_model_operation_readiness.py",
        "scripts/validate_model_operation_readiness.py",
    }
    base = {
        model_registry: _fact_registry_bytes(
            model_registry,
            {output_glob: "model_governance"},
        ),
        output_inventory: _fact_registry_bytes(
            output_inventory,
            {path: "research_backtest" for path in sorted(readiness_paths)},
        ),
        lifecycle_inventory: _fact_registry_bytes(
            lifecycle_inventory,
            {path: "research_backtest" for path in sorted(scripts)},
        ),
        production_inventory: _fact_registry_bytes(
            production_inventory,
            {path: "research_backtest" for path in sorted(scripts)},
        ),
    }
    current = {
        model_registry: _fact_registry_bytes(
            model_registry,
            {
                output_glob: "model_governance",
                docs_glob: "model_governance",
            },
        ),
        output_inventory: _fact_registry_bytes(
            output_inventory,
            {path: "model_governance" for path in sorted(readiness_paths)},
        ),
        lifecycle_inventory: _fact_registry_bytes(
            lifecycle_inventory,
            {path: "model_governance" for path in sorted(scripts)},
        ),
        production_inventory: _fact_registry_bytes(
            production_inventory,
            {path: "model_governance" for path in sorted(scripts)},
        ),
    }
    return base, current


def _patch_migration_facts(
    monkeypatch,
    base: dict[str, bytes],
    current: dict[str, bytes],
) -> None:
    monkeypatch.setattr(
        ownership_validator,
        "_base_migration_bytes",
        lambda _base_ref: None,
    )
    monkeypatch.setattr(
        ownership_validator,
        "_base_registry_bytes",
        lambda _base_ref, registry_path: base[registry_path],
    )
    monkeypatch.setattr(
        ownership_validator,
        "_current_registry_bytes",
        lambda registry_path: current[registry_path],
    )


def test_ownership_migrations_reconcile_each_registry_with_base_facts(
    tmp_path: Path,
    monkeypatch,
) -> None:
    path = tmp_path / "migrations.csv"
    _write_ownership_migrations(
        path,
        [dict(row) for row in EXPECTED_READINESS_MIGRATIONS],
    )
    base, current = _canonical_migration_fact_maps()
    monkeypatch.setattr(ownership_validator, "MIGRATION_REGISTRY", path)
    _patch_migration_facts(monkeypatch, base, current)

    assert validate_ownership_migrations("base-ref") == []


def test_ownership_migrations_reject_false_previous_or_current_owner_facts(
    tmp_path: Path,
    monkeypatch,
) -> None:
    path = tmp_path / "migrations.csv"
    _write_ownership_migrations(
        path,
        [dict(row) for row in EXPECTED_READINESS_MIGRATIONS],
    )
    base, current = _canonical_migration_fact_maps()
    output_inventory = "config/output_latest_artifact_inventory.csv"
    base[output_inventory] = _fact_registry_bytes(
        output_inventory,
        {
            "output/latest/model_operation_readiness_latest.csv": "model_governance",
            "output/latest/model_operation_readiness_latest.md": "research_backtest",
        },
    )
    lifecycle_inventory = "config/repo_file_lifecycle_inventory.csv"
    current[lifecycle_inventory] = _fact_registry_bytes(
        lifecycle_inventory,
        {
            "scripts/build_model_operation_readiness.py": "research_backtest",
            "scripts/validate_model_operation_readiness.py": "model_governance",
        },
    )
    monkeypatch.setattr(ownership_validator, "MIGRATION_REGISTRY", path)
    _patch_migration_facts(monkeypatch, base, current)

    errors = validate_ownership_migrations("base-ref")
    assert any("base fact mismatch" in error for error in errors)
    assert any("current fact mismatch" in error for error in errors)


def test_ownership_migrations_preserve_preexisting_output_readiness_owner(
    tmp_path: Path,
    monkeypatch,
) -> None:
    rows = [dict(row) for row in EXPECTED_READINESS_MIGRATIONS]
    rows[0]["record_keys"] = "output/latest/model_operation_readiness_latest.*"
    rows[0]["previous_owner"] = "research_backtest"
    path = tmp_path / "migrations.csv"
    _write_ownership_migrations(path, rows)
    base, current = _canonical_migration_fact_maps()
    monkeypatch.setattr(ownership_validator, "MIGRATION_REGISTRY", path)
    _patch_migration_facts(monkeypatch, base, current)

    errors = validate_ownership_migrations("base-ref")
    assert any(
        "pre-existing output/latest readiness ownership must not be represented"
        in error
        for error in errors
    )
    assert any("base fact mismatch" in error for error in errors)


def test_revenue_producer_accepts_only_revenue_artifacts() -> None:
    rules = load_ownership_rules()
    errors = validate_changed_paths(
        "revenue_unreacted_range",
        REVENUE_PRODUCER,
        [
            "output/latest/research_backtest/revenue_unreacted_range_feature_contrast_audit_latest.csv",
            "output/latest/research_backtest/revenue_unreacted_range_source_snapshot_projection_manifest_latest.csv",
            "output/latest/research_backtest/revenue_unreacted_range_source_snapshot_projection_detail_latest.csv",
            "output/latest/research_backtest/revenue_unreacted_range_position_shape_transition_matrix_latest.csv",
            "output/latest/research_backtest/revenue_unreacted_range_position_shape_transition_matrix_detail_latest.csv",
            "output/latest/research_backtest/revenue_unreacted_range_position_shape_transition_matrix_transition_latest.csv",
            "output/latest/research_backtest/revenue_unreacted_range_low_mid_falling_candidate_audit_latest.csv",
            "output/latest/research_backtest/revenue_unreacted_range_low_mid_falling_candidate_audit_detail_latest.csv",
            "output/latest/research_backtest/revenue_unreacted_range_low_mid_falling_candidate_audit_paired_confirmation_latest.csv",
            "output/latest/research_backtest/revenue_unreacted_range_low_mid_falling_candidate_audit_feature_contrast_latest.csv",
            "output/latest/research_backtest/revenue_unreacted_range_low_mid_falling_candidate_audit_latest.md",
            "output/latest/research_backtest/revenue_unreacted_range_forward_holdout_manifest_latest.csv",
            "output/latest/research_backtest/revenue_unreacted_range_forward_holdout_replay_source_detail_latest.csv",
            "output/history/research/revenue_unreacted_range_feature_contrast_audit.csv",
            "output/history/research/revenue_unreacted_range_source_snapshot_projection_manifest.csv",
            "output/history/research/revenue_unreacted_range_position_shape_transition_matrix.csv",
            "output/history/research/revenue_unreacted_range_position_shape_transition_matrix_transition.csv",
            "output/history/research/revenue_unreacted_range_low_mid_falling_candidate_audit.csv",
            "output/history/research/revenue_unreacted_range_low_mid_falling_candidate_audit_detail.csv",
            "output/history/research/revenue_unreacted_range_low_mid_falling_candidate_audit_paired_confirmation.csv",
            "output/history/research/revenue_unreacted_range_low_mid_falling_candidate_audit_feature_contrast.csv",
            "output/history/research/revenue_unreacted_range_forward_holdout_manifest.csv",
            "docs/latest/revenue_unreacted_range_feature_contrast_audit_latest.md",
            "docs/latest/revenue_unreacted_range_source_snapshot_projection_manifest_latest.csv",
            "docs/latest/revenue_unreacted_range_position_shape_transition_matrix_latest.csv",
            "docs/latest/revenue_unreacted_range_position_shape_transition_matrix_transition_latest.csv",
            "docs/latest/revenue_unreacted_range_position_shape_transition_matrix_latest.md",
            "docs/latest/revenue_unreacted_range_low_mid_falling_candidate_audit_latest.csv",
            "docs/latest/revenue_unreacted_range_low_mid_falling_candidate_audit_detail_latest.csv",
            "docs/latest/revenue_unreacted_range_low_mid_falling_candidate_audit_paired_confirmation_latest.csv",
            "docs/latest/revenue_unreacted_range_low_mid_falling_candidate_audit_feature_contrast_latest.csv",
            "docs/latest/revenue_unreacted_range_low_mid_falling_candidate_audit_latest.md",
            "docs/latest/revenue_unreacted_range_forward_holdout_manifest_latest.csv",
            "docs/latest/revenue_unreacted_range_forward_holdout_replay_source_detail_latest.csv",
        ],
        rules,
    )
    assert errors == []


def test_forward_holdout_stage_accepts_exact_seventeen_artifacts_only() -> None:
    from build_revenue_unreacted_range_research import (  # noqa: PLC0415
        FORWARD_HOLDOUT_ALLOWED_ARTIFACT_PATHS,
        validate_forward_holdout_stage_changed_paths,
    )

    assert len(FORWARD_HOLDOUT_ALLOWED_ARTIFACT_PATHS) == 17
    assert len(set(FORWARD_HOLDOUT_ALLOWED_ARTIFACT_PATHS)) == 17
    assert {
        "output/latest/research_backtest/"
        "revenue_unreacted_range_forward_holdout_replay_source_detail_latest.csv",
        "docs/latest/"
        "revenue_unreacted_range_forward_holdout_replay_source_detail_latest.csv",
    }.issubset(FORWARD_HOLDOUT_ALLOWED_ARTIFACT_PATHS)
    assert validate_forward_holdout_stage_changed_paths(
        list(FORWARD_HOLDOUT_ALLOWED_ARTIFACT_PATHS)
    ) == []

    eighteenth = (
        "output/latest/research_backtest/"
        "revenue_unreacted_range_forward_holdout_unregistered_surface_latest.csv"
    )
    assert validate_forward_holdout_stage_changed_paths(
        [*FORWARD_HOLDOUT_ALLOWED_ARTIFACT_PATHS, eighteenth]
    ) == [
        "forward holdout stage artifact allowlist violation: " + eighteenth
    ]


def test_forward_holdout_stage_rejects_other_same_model_research_artifact() -> None:
    from build_revenue_unreacted_range_research import (  # noqa: PLC0415
        validate_forward_holdout_stage_changed_paths,
    )

    errors = validate_forward_holdout_stage_changed_paths(
        [
            "output/latest/research_backtest/"
            "revenue_unreacted_range_low_mid_falling_candidate_audit_latest.csv"
        ]
    )

    assert errors == [
        "forward holdout stage artifact allowlist violation: "
        "output/latest/research_backtest/"
        "revenue_unreacted_range_low_mid_falling_candidate_audit_latest.csv"
    ]


@pytest.mark.parametrize(
    ("stage", "expected_stage_guard"),
    (
        ("forward_holdout", True),
        ("launch_timing_feature_audit", False),
    ),
)
def test_revenue_wrapper_runs_local_stage_guard_only_for_forward_holdout(
    monkeypatch,
    stage: str,
    expected_stage_guard: bool,
) -> None:
    import build_revenue_unreacted_range_research as revenue_builder  # noqa: PLC0415

    owner_guard_calls: list[str] = []
    stage_guard_calls: list[str] = []
    builder_calls: list[str] = []

    @contextmanager
    def fake_owner_guard(_model_id, _producer):
        owner_guard_calls.append("owner")
        yield

    @contextmanager
    def fake_stage_guard():
        stage_guard_calls.append("forward_holdout")
        yield

    monkeypatch.setattr(
        revenue_builder, "model_owned_artifact_guard", fake_owner_guard
    )
    monkeypatch.setattr(
        revenue_builder,
        "forward_holdout_stage_artifact_guard",
        fake_stage_guard,
    )
    monkeypatch.setattr(
        revenue_builder,
        "parse_args",
        lambda: SimpleNamespace(stage=stage),
    )
    monkeypatch.setattr(
        revenue_builder,
        "build_and_write_forward_holdout",
        lambda: builder_calls.append("forward_holdout"),
    )
    monkeypatch.setattr(
        revenue_builder,
        "build_and_write_launch_timing_feature_audit",
        lambda: builder_calls.append("launch_timing_feature_audit"),
    )

    assert revenue_builder.main() == 0
    assert owner_guard_calls == ["owner"]
    assert stage_guard_calls == (["forward_holdout"] if expected_stage_guard else [])
    assert builder_calls == [stage]


def test_stage_allowlist_is_opt_in_and_does_not_change_model_owner_validation() -> None:
    rules = load_ownership_rules()
    existing_revenue_artifact = (
        "output/latest/research_backtest/"
        "revenue_unreacted_range_feature_contrast_audit_latest.csv"
    )

    assert validate_changed_paths(
        "revenue_unreacted_range",
        REVENUE_PRODUCER,
        [existing_revenue_artifact],
        rules,
    ) == []


def test_forward_holdout_local_stage_guard_rejects_other_same_model_artifact(
    tmp_path, monkeypatch
) -> None:
    import build_revenue_unreacted_range_research as revenue_builder  # noqa: PLC0415

    changed_path = (
        "output/latest/research_backtest/"
        "revenue_unreacted_range_low_mid_falling_candidate_audit_latest.csv"
    )
    monkeypatch.setattr(revenue_builder, "_dirty_snapshot", lambda _root: {})
    monkeypatch.setattr(
        revenue_builder,
        "changed_during_run",
        lambda _root, _before: [changed_path],
    )

    with pytest.raises(
        RuntimeError, match="forward holdout stage artifact allowlist violation"
    ):
        with revenue_builder.forward_holdout_stage_artifact_guard(root=tmp_path):
            pass


def test_revenue_producer_fails_on_other_model_or_snapshot_changes() -> None:
    rules = load_ownership_rules()
    errors = validate_changed_paths(
        "revenue_unreacted_range",
        REVENUE_PRODUCER,
        [
            "output/latest/research_backtest/price_pullback_23ema_promotion_matrix_latest.csv",
            "output/latest/daily_w_bottom_right_side_operation_section_latest.csv",
            "output/history/daily_model_snapshots/all_candidates_20260709.csv",
        ],
        rules,
    )
    assert len(errors) == 3
    assert all("cross-model artifact change" in error for error in errors)


def test_wrong_producer_cannot_write_model_owned_artifact() -> None:
    rules = load_ownership_rules()
    errors = validate_changed_paths(
        "price_pullback_23ema",
        LEGACY_CROSS_MODEL_PRODUCER,
        ["output/latest/research_backtest/price_pullback_23ema_promotion_matrix_latest.csv"],
        rules,
    )
    assert errors and "wrong producer" in errors[0]


def test_volume_v2_entrypoint_excludes_formal_and_legacy_builders() -> None:
    text = (SCRIPTS / VOLUME_V2_PRODUCER).read_text(encoding="utf-8")
    for forbidden_builder in FORBIDDEN_VOLUME_V2_BUILDERS:
        assert forbidden_builder not in text


def test_protected_mature_model_sentinel_snapshot_is_complete() -> None:
    sentinels = load_protected_sentinels()
    snapshot, errors = protected_sentinel_snapshot(ROOT, sentinels)
    assert errors == []
    assert "config/stock_model_contract_registry.csv" in snapshot
    assert "output/latest/approved_operation_patterns_latest.csv" in snapshot
    assert "output/latest/daily_price_pullback_23ema_operation_section_latest.csv" in snapshot
    assert any(path.startswith("output/history/daily_model_snapshots/") for path in snapshot)


def test_protected_sentinel_detects_hash_drift() -> None:
    errors = compare_protected_sentinel_snapshots(
        {"output/latest/daily_w_bottom_right_side_operation_section_latest.csv": "before"},
        {"output/latest/daily_w_bottom_right_side_operation_section_latest.csv": "after"},
    )
    assert errors == [
        "protected sentinel hash drift during model research: "
        "output/latest/daily_w_bottom_right_side_operation_section_latest.csv"
    ]


def test_protected_sentinel_aggregate_hash_is_order_independent_and_drift_sensitive() -> None:
    before = {"b.csv": "hash-b", "a.csv": "hash-a"}
    same = {"a.csv": "hash-a", "b.csv": "hash-b"}
    after = {"a.csv": "hash-a", "b.csv": "hash-c"}

    assert protected_sentinel_aggregate_sha256(before) == protected_sentinel_aggregate_sha256(same)
    assert protected_sentinel_aggregate_sha256(before) != protected_sentinel_aggregate_sha256(after)


def test_model_owned_guard_fails_when_protected_artifact_changes(tmp_path, monkeypatch) -> None:
    protected = tmp_path / "output/latest/formal_adapter.csv"
    protected.parent.mkdir(parents=True)
    protected.write_text("before\n", encoding="utf-8")
    ownership = tmp_path / "ownership.csv"
    ownership.write_text(
        "owner_model_id,producer,artifact_glob,artifact_class,change_policy,formal_evidence_status,notes\n"
        "revenue_unreacted_range,scripts/build_revenue_unreacted_range_research.py,"
        "output/latest/research_backtest/revenue_unreacted_range_*,model_research_output,"
        "model_owned_write,research_only,test\n",
        encoding="utf-8",
    )
    sentinels = tmp_path / "sentinels.csv"
    sentinels.write_text(
        "sentinel_id,artifact_glob,owner,sentinel_class,required,notes\n"
        "formal_adapter,output/latest/formal_adapter.csv,mature_model,formal_operation_adapter,True,test\n",
        encoding="utf-8",
    )
    monkeypatch.setattr(guard_module, "_dirty_snapshot", lambda _root: {})
    monkeypatch.setattr(guard_module, "changed_during_run", lambda _root, _before: [])
    with pytest.raises(RuntimeError, match="protected sentinel hash drift"):
        with guard_module.model_owned_artifact_guard(
            "revenue_unreacted_range",
            "scripts/build_revenue_unreacted_range_research.py",
            root=tmp_path,
            registry_path=ownership,
            sentinel_registry_path=sentinels,
        ):
            protected.write_text("after\n", encoding="utf-8")
