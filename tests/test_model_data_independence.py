from __future__ import annotations

import ast
import csv
import subprocess
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))

from model_data_independence import (  # noqa: E402
    BASELINE_MIGRATION_ROW_SHA256,
    BASELINE_DATA_MIGRATION_ROW_SHA256,
    DATA_SHARING_MIGRATION_COLUMNS,
    REVENUE_CROSS_MARKET_CONSUMER_FAMILIES,
    REVENUE_CROSS_MARKET_RESOLUTION_CANONICAL_COLUMNS,
    REVENUE_CROSS_MARKET_RESOLUTION_SHA_TOKEN,
    SEMANTIC_MIGRATION_COLUMNS,
    VALID_INDEPENDENT_VALIDATOR_ROLES,
    SourceSemanticGraph,
    _data_write_scopes_overlap,
    _production_imports,
    _active_repo_python_sources,
    _active_stock_models,
    _governed_business_import_contract,
    _python_source_module_map,
    _revenue_cross_market_resolution_registry_canonical_sha256,
    _validate_revenue_cross_market_resolution_contract_binding,
    _validate_current_migration_chain,
    _validate_independent_governed_imports,
    aggregate_semantic_sha256,
    data_contract_sha256,
    data_migration_row_sha256,
    migration_row_sha256,
    runtime_subgraph_sha256,
    semantic_record_sha256,
    strict_csv_rows,
    validate_data_sharing,
    validate_model_semantic_ownership,
    validate_validator_independence,
)
from validate_model_data_independence import (  # noqa: E402
    validate,
    validate_audit_artifact,
    validate_data_sharing_migration_append_only,
)
import build_model_data_independence_audit as audit_builder  # noqa: E402


ACTIVE_MODELS = {
    "hot_theme_pullback",
    "neckline_volume_breakout_confirmation",
    "price_pullback_23ema",
    "pullback_short_reclaim",
    "revenue_unreacted_range",
    "tdcc_short_term_continuation_d5_d10",
    "tdcc_stealth_accumulation",
    "volume_range_breakout_v2_high_position_volume_attack",
    "volume_range_breakout_v2_low_position_volume_attack",
    "volume_range_breakout_v2_mid_position_momentum_attack",
    "w_bottom_right_side",
}


def read_csv(path: str) -> list[dict[str, str]]:
    with (ROOT / path).open("r", encoding="utf-8-sig", newline="") as fh:
        return list(csv.DictReader(fh))


def _write_data_migrations(path: Path, rows: list[dict[str, str]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=DATA_SHARING_MIGRATION_COLUMNS)
        writer.writeheader()
        writer.writerows(rows)


def _migration_row(migration_id: str) -> dict[str, str]:
    return {
        column: (
            migration_id
            if column == "migration_id"
            else "validated_user_approved_migration"
            if column == "migration_status"
            else f"{migration_id}_{column}"
        )
        for column in DATA_SHARING_MIGRATION_COLUMNS
    }


def _commit_base_migrations(tmp_path: Path) -> tuple[Path, list[dict[str, str]]]:
    migration_path = tmp_path / "config" / "daily_model_data_sharing_migrations.csv"
    rows = [_migration_row("base_one"), _migration_row("base_two")]
    _write_data_migrations(migration_path, rows)
    subprocess.run(["git", "init", "-q"], cwd=tmp_path, check=True)
    subprocess.run(["git", "add", migration_path.relative_to(tmp_path).as_posix()], cwd=tmp_path, check=True)
    subprocess.run(
        [
            "git",
            "-c",
            "user.name=Codex Test",
            "-c",
            "user.email=codex-test@example.invalid",
            "commit",
            "-qm",
            "base migrations",
        ],
        cwd=tmp_path,
        check=True,
    )
    return migration_path, rows


def test_model_data_independence_validator_passes() -> None:
    assert validate(base_ref="") == []


def test_model_data_independence_audit_is_current_and_mirrored() -> None:
    assert validate_audit_artifact() == []


def test_model_data_independence_csv_writer_uses_lf_only(tmp_path: Path) -> None:
    path = tmp_path / "audit.csv"
    row = {column: column for column in audit_builder.OUTPUT_COLUMNS}

    audit_builder._write_csv(path, [row])

    raw = path.read_bytes()
    assert raw.startswith(b"\xef\xbb\xbf")
    assert raw.count(b"\n") == 2
    assert b"\r" not in raw


def test_retired_normalize_only_cli_is_rejected() -> None:
    with pytest.raises(SystemExit):
        audit_builder.main(["--normalize-existing-csv-line-endings-only"])


def test_data_sharing_migration_base_rows_allow_only_exact_prefix_append(
    tmp_path: Path,
) -> None:
    migration_path, rows = _commit_base_migrations(tmp_path)
    _write_data_migrations(migration_path, [*rows, _migration_row("appended_three")])

    assert validate_data_sharing_migration_append_only(
        "HEAD",
        migration_path=migration_path,
        repository_root=tmp_path,
    ) == []


@pytest.mark.parametrize("attack", ["rewrite", "reorder", "delete", "requote"])
def test_data_sharing_migration_base_prefix_rejects_hostile_history_changes(
    tmp_path: Path,
    attack: str,
) -> None:
    migration_path, rows = _commit_base_migrations(tmp_path)
    hostile = [dict(row) for row in rows]
    if attack == "rewrite":
        hostile[0]["migration_status"] = "silently_rewritten"
    elif attack == "reorder":
        hostile = [hostile[1], hostile[0]]
    elif attack == "delete":
        hostile = hostile[:-1]
    _write_data_migrations(migration_path, hostile)
    if attack == "requote":
        text = migration_path.read_text(encoding="utf-8")
        migration_path.write_text(
            text.replace("base_one,", '"base_one",', 1),
            encoding="utf-8",
        )

    errors = validate_data_sharing_migration_append_only(
        "HEAD",
        migration_path=migration_path,
        repository_root=tmp_path,
    )

    assert errors
    assert any("is append-only" in error for error in errors)


def test_every_active_model_has_exact_ast_semantic_ownership() -> None:
    errors, semantics = validate_model_semantic_ownership(base_ref="")
    assert errors == []
    assert set(semantics) == ACTIVE_MODELS
    assert all(model.semantic_sha256 and model.items for model in semantics.values())


def test_shared_business_semantics_are_disclosed_as_contained_not_technical() -> None:
    rows = read_csv("config/daily_model_shared_semantic_registry.csv")
    by_item = {row["semantic_item"]: row for row in rows}
    assert len(rows) == 88
    assert by_item["global:MODEL_SCORE_PROFILES"]["semantic_class"] == (
        "contained_legacy_cross_model_semantic"
    )
    for retired_single_consumer_item in (
        "function:bottom_volume_attack_like",
        "function:bottom_volume_attack_normal_volume",
        "function:in_recent_range",
    ):
        assert retired_single_consumer_item not in by_item
    old_monolith_rows = [
        row
        for row in rows
        if row["source_file"] == "scripts/build_daily_candidate_model_layer.py"
    ]
    assert all(
        "revenue_unreacted_range"
        not in row["consumer_models"].split(";")
        for row in old_monolith_rows
    )
    assert by_item["function:bottom_volume_attack_breakout_level"][
        "consumer_models"
    ] == (
        "tdcc_stealth_accumulation;"
        "volume_range_breakout_v2_high_position_volume_attack;"
        "volume_range_breakout_v2_low_position_volume_attack;"
        "volume_range_breakout_v2_mid_position_momentum_attack"
    )
    assert by_item["function:text"]["semantic_class"] == "shared_technical"
    assert by_item["function:append_volume_breakout_signals"]["consumer_models"] == (
        "volume_range_breakout_v2_high_position_volume_attack;"
        "volume_range_breakout_v2_low_position_volume_attack;"
        "volume_range_breakout_v2_mid_position_momentum_attack"
    )
    family_helper_migrations = {
        "function:append_volume_breakout_signals": (
            "volume_v2_global_official_candidate_scope_repair_20260809"
        ),
        "function:_volume_v2_formal_outcome_envelope": (
            "volume_v2_formal_outcome_numeric_canonicalization_20260810"
        ),
        "function:_volume_v2_formal_outcome_sha256": (
            "volume_v2_candidate_projection_lineage_20260731"
        ),
        "function:volume_v2_candidate_lookup": (
            "volume_v2_candidate_projection_lineage_20260731"
        ),
    }
    for family_helper, expected_migration in family_helper_migrations.items():
        assert by_item[family_helper]["semantic_class"] == (
            "contained_model_family_semantic"
        )
        assert by_item[family_helper]["last_migration_id"] == expected_migration
    watch_lineage_validator = by_item["function:validate_volume_v2_watch_advisory_lineage"]
    assert watch_lineage_validator["semantic_class"] == "contained_model_family_semantic"
    assert watch_lineage_validator["last_migration_id"] == (
        "volume_v2_advisory_asof_slice_lineage_20260727"
    )
    canonical_hash = by_item["function:volume_v2_canonical_text_sha256"]
    assert canonical_hash["semantic_class"] == "contained_model_family_semantic"
    assert canonical_hash["last_migration_id"] == (
        "volume_v2_advisory_asof_slice_lineage_20260727"
    )
    for dispatcher_guard in (
        "global:VOLUME_V2_CANDIDATE_SCORE_FIELDS",
        "global:VOLUME_V2_FORMAL_DISPATCH_FORBIDDEN_FIELDS",
        "global:VOLUME_V2_WATCH_NON_AUTHORITATIVE_COLLISION_FIELDS",
        "global:VOLUME_V2_WATCH_OVERLAY_FIELDS",
    ):
        assert by_item[dispatcher_guard]["semantic_class"] == (
            "contained_model_family_semantic"
        )
        assert by_item[dispatcher_guard]["last_migration_id"] == (
            "volume_v2_formal_lineage_hardening_20260718"
        )
    for model_family_source in (
        "global:VOLUME_BREAKOUT_TAXONOMY",
        "global:WARRANT_FLOW",
    ):
        assert by_item[model_family_source]["semantic_class"] == (
            "contained_model_family_semantic"
        )
        assert by_item[model_family_source]["consumer_models"] == (
            "volume_range_breakout_v2_high_position_volume_attack;"
            "volume_range_breakout_v2_low_position_volume_attack;"
            "volume_range_breakout_v2_mid_position_momentum_attack"
        )
    for no_longer_shared_item in (
        "function:candidate_lookup",
        "function:taxonomy_lookup",
        "function:taxonomy_or_source",
        "global:STOCK_THEME_TAXONOMY",
    ):
        assert no_longer_shared_item not in by_item


def test_revenue_v2_adapter_migrations_pin_activation_and_history_repair() -> None:
    ownership = {
        row["model_id"]: row
        for row in read_csv("config/daily_model_semantic_ownership.csv")
    }["revenue_unreacted_range"]
    migrations = read_csv("config/daily_model_semantic_migrations.csv")
    activation = next(
        row
        for row in migrations
        if row["migration_id"]
        == "revenue_v2_dedicated_adapter_activation_20260830"
    )
    history_repair = next(
        row
        for row in migrations
        if row["migration_id"]
        == "revenue_operation_history_filename_contract_repair_20260902"
    )

    assert ownership["production_source_file"] == (
        "scripts/build_daily_revenue_unreacted_range_operation_section.py"
    )
    assert ownership["execution_entry_functions"] == (
        "_selected_source_mid_falling;build_operation_section"
    )
    assert ownership["ownership_status"] == "model_owned_module"
    assert ownership["last_migration_id"] == history_repair["migration_id"]
    assert ownership["approval_reference"] == history_repair["user_approval_reference"]
    assert history_repair["changed_semantics"] == "model:revenue_unreacted_range"
    assert history_repair["previous_sha256s"] == activation["new_sha256s"].split(";")[0]
    assert history_repair["new_sha256s"] == semantic_record_sha256(
        "model:revenue_unreacted_range", ownership
    )
    assert history_repair["affected_models"] == "revenue_unreacted_range"
    assert history_repair["migration_status"] == "validated_user_approved_migration"
    assert "generic rN published snapshots" in history_repair["notes"]

    changed = activation["changed_semantics"].split(";")
    previous = activation["previous_sha256s"].split(";")
    current = activation["new_sha256s"].split(";")
    assert len(changed) == len(previous) == len(current) == 32
    assert changed[0] == "model:revenue_unreacted_range"
    old_monolith_items = changed[1:]
    assert len(old_monolith_items) == 31
    assert all(
        item.startswith(
            "item:scripts/build_daily_candidate_model_layer.py::"
        )
        for item in old_monolith_items
    )
    assert sum("::runtime_subgraph:" in item for item in old_monolith_items) == 4
    retired = {
        key
        for key, new_hash in zip(changed, current)
        if new_hash == "RETIRED"
    }
    assert retired == {
        "item:scripts/build_daily_candidate_model_layer.py::"
        "function:bottom_volume_attack_like",
        "item:scripts/build_daily_candidate_model_layer.py::"
        "function:bottom_volume_attack_normal_volume",
        "item:scripts/build_daily_candidate_model_layer.py::"
        "function:in_recent_range",
    }
    assert set(activation["affected_models"].split(";")) == ACTIVE_MODELS
    assert "only behavior change" in activation["notes"]
    assert "Every other model keeps the same AST" in activation["notes"]


def test_warrant_runtime_subgraphs_pin_recursive_hashes_consumers_and_migration() -> None:
    registry_rows = read_csv("config/daily_model_shared_semantic_registry.csv")
    runtime_rows = {
        row["semantic_item"]: row
        for row in registry_rows
        if row["semantic_item"].startswith("runtime_subgraph:")
    }
    expected_items = {
        "runtime_subgraph:run_warrant_formal_sync_only",
        "runtime_subgraph:synchronize_warrant_formal_frames",
        "runtime_subgraph:rebuild_warrant_formal_consumers",
        "runtime_subgraph:finalize_warrant_formal_consumer_parity",
    }
    assert set(runtime_rows) == expected_items
    source_path = ROOT / "scripts/build_daily_candidate_model_layer.py"
    graph = SourceSemanticGraph(
        "scripts/build_daily_candidate_model_layer.py",
        source_path.read_text(encoding="utf-8"),
    )
    expected_consumers = ";".join(
        sorted(ACTIVE_MODELS - {"revenue_unreacted_range"})
    )
    for item, row in runtime_rows.items():
        assert row["semantic_class"] == "registered_cross_model_runtime_semantic"
        assert row["consumer_models"] == expected_consumers
        assert row["canonical_ast_sha256"] == runtime_subgraph_sha256(graph, item)
        assert row["last_migration_id"] == (
            "revenue_v2_dedicated_adapter_activation_20260830"
        )

    migration = next(
        row
        for row in read_csv("config/daily_model_semantic_migrations.csv")
        if row["migration_id"]
        == "warrant_fixed_membership_runtime_semantics_20260720"
    )
    changed = migration["changed_semantics"].split(";")
    assert changed == [
        f"item:scripts/build_daily_candidate_model_layer.py::{item}"
        for item in (
            "runtime_subgraph:run_warrant_formal_sync_only",
            "runtime_subgraph:synchronize_warrant_formal_frames",
            "runtime_subgraph:rebuild_warrant_formal_consumers",
            "runtime_subgraph:finalize_warrant_formal_consumer_parity",
        )
    ]
    assert migration["previous_sha256s"].split(";") == ["NEW", "NEW", "NEW", "NEW"]
    assert migration["new_sha256s"].split(";") == [
        "7f14f7f8836872c113147bf95816806cf78f1266904990855cb719a854139ac8",
        "6b4e2f3d99eebe91d964298a5324ce3e577c93842452314cb07f34892a1a9f4d",
        "a4c28d82a2ecd4634c91b31099584ebb7b353dacb76d471e95f138c837249f04",
        "07751409ace85e0f5d99aea851a9dd1a325daf3ddf6015804b943cac80a7c103",
    ]
    assert migration["affected_models"] == ";".join(sorted(ACTIVE_MODELS))


def test_volume_v2_asof_slice_migration_pins_exact_current_records() -> None:
    migration_id = "volume_v2_advisory_asof_slice_lineage_20260727"
    approval = "user_approved_option_A_volume_watch_asof_lineage_20260727"
    ownership = {
        row["model_id"]: row
        for row in read_csv("config/daily_model_semantic_ownership.csv")
    }
    shared = {
        f"item:{row['source_file']}::{row['semantic_item']}": row
        for row in read_csv("config/daily_model_shared_semantic_registry.csv")
    }
    migration = next(
        row
        for row in read_csv("config/daily_model_semantic_migrations.csv")
        if row["migration_id"] == migration_id
    )
    changed = migration["changed_semantics"].split(";")
    assert changed == [
        "item:scripts/build_daily_candidate_model_layer.py::function:validate_volume_v2_watch_advisory_lineage",
        "item:scripts/build_daily_candidate_model_layer.py::function:volume_v2_canonical_text_sha256",
        "item:scripts/build_daily_candidate_model_layer.py::runtime_subgraph:run_warrant_formal_sync_only",
        "item:scripts/build_daily_candidate_model_layer.py::runtime_subgraph:synchronize_warrant_formal_frames",
        "model:volume_range_breakout_v2_high_position_volume_attack",
        "model:volume_range_breakout_v2_low_position_volume_attack",
        "model:volume_range_breakout_v2_mid_position_momentum_attack",
    ]
    assert migration["previous_sha256s"].split(";") == [
        "3003fe187bbc20fcfe665779a0d1c7c988a39fd0bed8315b60cf52b2a7c10480",
        "98ae16b8cd4329f0aeeb7ec1649439ad2920881dbf834cbcd600ab014e1cdf66",
        "7f14f7f8836872c113147bf95816806cf78f1266904990855cb719a854139ac8",
        "6b4e2f3d99eebe91d964298a5324ce3e577c93842452314cb07f34892a1a9f4d",
        "8931241b02aff58db5a59ee465b6c46608756aa1238aa1cb8b3c1e5dd0e8f2c8",
        "058e804846048b75e88274525c5265fe8357a4263605d9f7d71d5be2ed53c9af",
        "8f85c0a93255f5d58424d9adc947f7051a8b5c763ec5882dec36da689bbe96a5",
    ]
    current_rows = [
        shared[key] if key.startswith("item:") else ownership[key.removeprefix("model:")]
        for key in changed
    ]
    migration_new_sha256s = migration["new_sha256s"].split(";")
    assert migration_new_sha256s[:2] == [
        semantic_record_sha256(key, row)
        for key, row in zip(changed[:2], current_rows[:2])
    ]
    later_projection = next(
        row
        for row in read_csv("config/daily_model_semantic_migrations.csv")
        if row["migration_id"] == "volume_v2_candidate_projection_lineage_20260731"
    )
    later_previous_by_key = dict(
        zip(
            later_projection["changed_semantics"].split(";"),
            later_projection["previous_sha256s"].split(";"),
        )
    )
    assert migration_new_sha256s[2:] == [
        later_previous_by_key[key] for key in changed[2:]
    ]
    expected_consumers = ";".join(sorted(ACTIVE_MODELS))
    assert migration["affected_models"] == expected_consumers
    assert migration["user_approval_reference"] == approval
    assert migration["migration_status"] == "validated_user_approved_migration"
    for key, row in zip(changed[:2], current_rows[:2]):
        assert row["last_migration_id"] == migration_id
        assert row["approval_reference"] == approval


def test_volume_v2_candidate_projection_migration_chains_to_current_records() -> None:
    migration_id = "volume_v2_candidate_projection_lineage_20260731"
    approval = "user_delegated_daily_model_2451_duplicate_normalization_repair_20260731"
    ownership = {
        row["model_id"]: row
        for row in read_csv("config/daily_model_semantic_ownership.csv")
    }
    shared = {
        f"item:{row['source_file']}::{row['semantic_item']}": row
        for row in read_csv("config/daily_model_shared_semantic_registry.csv")
    }
    migration = next(
        row
        for row in read_csv("config/daily_model_semantic_migrations.csv")
        if row["migration_id"] == migration_id
    )
    changed = migration["changed_semantics"].split(";")
    assert changed == [
        "item:scripts/build_daily_candidate_model_layer.py::function:append_volume_breakout_signals",
        "item:scripts/build_daily_candidate_model_layer.py::function:_volume_v2_formal_outcome_envelope",
        "item:scripts/build_daily_candidate_model_layer.py::function:_volume_v2_formal_outcome_sha256",
        "item:scripts/build_daily_candidate_model_layer.py::function:volume_v2_candidate_lookup",
        "item:scripts/build_daily_candidate_model_layer.py::runtime_subgraph:run_warrant_formal_sync_only",
        "item:scripts/build_daily_candidate_model_layer.py::runtime_subgraph:synchronize_warrant_formal_frames",
        "model:volume_range_breakout_v2_high_position_volume_attack",
        "model:volume_range_breakout_v2_low_position_volume_attack",
        "model:volume_range_breakout_v2_mid_position_momentum_attack",
    ]
    assert migration["previous_sha256s"].split(";") == [
        "841c11be7321e4000b59ce95a0ca7cc1cd843c24be482bccc4a8c36098327f0a",
        "NEW",
        "NEW",
        "a22f68e77932175e9ca2b04ca3c60471a5a173a34fa90765b426e3ea1afe07ab",
        "14320bec05bbc2370eb9b1f03a3e240536a011e6460f09ef71d78303995c02b2",
        "e83a5815d063bdd5707128c492414e2012ec4bd1f5d39105cf5169cb9bd3c458",
        "46645d18da4feebe982590842427274a899c7046d8b37d57d80ba2b2b9fd42c5",
        "76776e3924e0d32ba83951c809608f080e2c4e1b54f90eec7e37dfe760e69117",
        "34a8a772898459af18305daee7310ead321aea9e992e1cc869505ed585a13ecc",
    ]
    old_new_by_key = dict(zip(changed, migration["new_sha256s"].split(";")))
    later_previous_by_key: dict[str, str] = {}
    for later_id in (
        "volume_v2_global_official_candidate_scope_repair_20260809",
        "volume_v2_formal_outcome_numeric_canonicalization_20260810",
    ):
        later = next(
            row
            for row in read_csv("config/daily_model_semantic_migrations.csv")
            if row["migration_id"] == later_id
        )
        for key, previous in zip(
            later["changed_semantics"].split(";"),
            later["previous_sha256s"].split(";"),
        ):
            later_previous_by_key.setdefault(key, previous)
    for key in changed:
        if key in later_previous_by_key:
            assert old_new_by_key[key] == later_previous_by_key[key]
            continue
        row = shared[key] if key.startswith("item:") else ownership[key.removeprefix("model:")]
        assert old_new_by_key[key] == semantic_record_sha256(key, row)
        assert row["last_migration_id"] == migration_id
        assert row["approval_reference"] == approval
    assert migration["affected_models"] == ";".join(sorted(ACTIVE_MODELS))
    assert migration["user_approval_reference"] == approval
    assert migration["migration_status"] == "validated_user_approved_migration"


def test_volume_v2_global_official_candidate_scope_migration_pins_current_records() -> None:
    migration_id = "volume_v2_global_official_candidate_scope_repair_20260809"
    approval = "user_delegated_validation_only_replay_2059_repair_20260809"
    ownership = {
        row["model_id"]: row
        for row in read_csv("config/daily_model_semantic_ownership.csv")
    }
    shared = {
        f"item:{row['source_file']}::{row['semantic_item']}": row
        for row in read_csv("config/daily_model_shared_semantic_registry.csv")
    }
    migration = next(
        row
        for row in read_csv("config/daily_model_semantic_migrations.csv")
        if row["migration_id"] == migration_id
    )
    changed = migration["changed_semantics"].split(";")
    assert changed == [
        "item:scripts/build_daily_candidate_model_layer.py::function:append_volume_breakout_signals",
        "item:scripts/build_daily_candidate_model_layer.py::runtime_subgraph:run_warrant_formal_sync_only",
        "item:scripts/build_daily_candidate_model_layer.py::runtime_subgraph:synchronize_warrant_formal_frames",
        "model:volume_range_breakout_v2_high_position_volume_attack",
        "model:volume_range_breakout_v2_low_position_volume_attack",
        "model:volume_range_breakout_v2_mid_position_momentum_attack",
    ]
    assert migration["previous_sha256s"].split(";") == [
        "cdb45b61aa6bfb8314ff7dd7314a802122a928493410c0153aab82c69a4817fc",
        "92ea9cd7e27699898eb93c662cac829a4f630e6cb2942b77ab65690a66eb1d28",
        "f4493b8be563267a35c3a88ce38b5d5b70f7c23c3a242a8051843fe2d66c35c2",
        "3e52846d512a084ad735d2671e707a5b869d2cc3e51fe59f7c94926beb5f9d5f",
        "f90afe066a203f71a1c45deea5476a758a32fa1d3e74918bd7cd7d7379c3a628",
        "d97f4c00df25456aad5a9368ebd2394bf59cb6bbdd3a0ece24a15cf069039295",
    ]
    current_rows = {
        key: shared[key] if key.startswith("item:") else ownership[key.removeprefix("model:")]
        for key in changed
    }
    successor = next(
        row
        for row in read_csv("config/daily_model_semantic_migrations.csv")
        if row["migration_id"]
        == "volume_v2_formal_outcome_numeric_canonicalization_20260810"
    )
    successor_previous = dict(
        zip(
            successor["changed_semantics"].split(";"),
            successor["previous_sha256s"].split(";"),
        )
    )
    revenue_successor = next(
        row
        for row in read_csv("config/daily_model_semantic_migrations.csv")
        if row["migration_id"]
        == "revenue_v2_dedicated_adapter_activation_20260830"
    )
    revenue_successor_previous = dict(
        zip(
            revenue_successor["changed_semantics"].split(";"),
            revenue_successor["previous_sha256s"].split(";"),
        )
    )
    for key, new_hash in zip(changed, migration["new_sha256s"].split(";")):
        if key in successor_previous:
            assert new_hash == successor_previous[key]
        else:
            assert new_hash == semantic_record_sha256(key, current_rows[key])
    assert migration["affected_models"] == ";".join(sorted(ACTIVE_MODELS))
    assert migration["user_approval_reference"] == approval
    assert migration["migration_status"] == "validated_user_approved_migration"
    for key, row in current_rows.items():
        expected_migration = (
            "revenue_v2_dedicated_adapter_activation_20260830"
            if key in revenue_successor_previous
            else "volume_v2_formal_outcome_numeric_canonicalization_20260810"
            if key in successor_previous
            else migration_id
        )
        assert row["last_migration_id"] == expected_migration


def test_volume_v2_formal_outcome_numeric_migration_pins_current_records() -> None:
    migration_id = "volume_v2_formal_outcome_numeric_canonicalization_20260810"
    approval = "user_delegated_volume_v2_formal_outcome_sha_repair_20260810"
    ownership = {
        row["model_id"]: row
        for row in read_csv("config/daily_model_semantic_ownership.csv")
    }
    shared = {
        f"item:{row['source_file']}::{row['semantic_item']}": row
        for row in read_csv("config/daily_model_shared_semantic_registry.csv")
    }
    migration = next(
        row
        for row in read_csv("config/daily_model_semantic_migrations.csv")
        if row["migration_id"] == migration_id
    )
    changed = migration["changed_semantics"].split(";")
    assert changed == [
        "item:scripts/build_daily_candidate_model_layer.py::function:_volume_v2_formal_outcome_envelope",
        "item:scripts/build_daily_candidate_model_layer.py::runtime_subgraph:run_warrant_formal_sync_only",
        "item:scripts/build_daily_candidate_model_layer.py::runtime_subgraph:synchronize_warrant_formal_frames",
        "model:volume_range_breakout_v2_high_position_volume_attack",
        "model:volume_range_breakout_v2_low_position_volume_attack",
        "model:volume_range_breakout_v2_mid_position_momentum_attack",
    ]
    assert migration["previous_sha256s"].split(";") == [
        "0c7e887aab10df7fe9b843205a2494da9a58bd5e019162cc8ce1218732616fbc",
        "7922c5ed9ac50ecf3eed579a2fa7d211e65c4b743d0be08f0e0a43e4deff48f2",
        "5e0ae45788de4e1ea555ddcc4c227a9fd127651ae906f7750253ad702923224c",
        "de8caba7a68cbf2cf1928548d7438625b96b3b18fd3a57bc4da1049e12fc8c05",
        "6a4c0763c9a109ac142f5e05311f7b9ba5d5f47afc18804af3c0e0d27c36613b",
        "23abb241fa9b4c80b350832796b1fdb02d0bfed8bee7a58213c518a54d3709e2",
    ]
    current_rows = [
        shared[key] if key.startswith("item:") else ownership[key.removeprefix("model:")]
        for key in changed
    ]
    revenue_successor = next(
        row
        for row in read_csv("config/daily_model_semantic_migrations.csv")
        if row["migration_id"]
        == "revenue_v2_dedicated_adapter_activation_20260830"
    )
    revenue_successor_previous = dict(
        zip(
            revenue_successor["changed_semantics"].split(";"),
            revenue_successor["previous_sha256s"].split(";"),
        )
    )
    for key, row, new_hash in zip(
        changed,
        current_rows,
        migration["new_sha256s"].split(";"),
    ):
        if key in revenue_successor_previous:
            assert new_hash == revenue_successor_previous[key]
        else:
            assert new_hash == semantic_record_sha256(key, row)
    assert migration["user_approval_reference"] == approval
    assert migration["migration_status"] == "validated_user_approved_migration"
    for key, row in zip(changed, current_rows):
        if key in revenue_successor_previous:
            assert row["last_migration_id"] == revenue_successor["migration_id"]
            assert row["approval_reference"] == revenue_successor[
                "user_approval_reference"
            ]
        else:
            assert row["last_migration_id"] == migration_id
            assert row["approval_reference"] == approval


def test_warrant_runtime_entrypoint_pins_lifecycle_sequence() -> None:
    source_path = ROOT / "scripts/build_daily_candidate_model_layer.py"
    graph = SourceSemanticGraph(
        "scripts/build_daily_candidate_model_layer.py",
        source_path.read_text(encoding="utf-8"),
    )
    entrypoint = graph.functions["run_warrant_formal_sync_only"]
    calls = sorted(
        (
            node.lineno,
            node.func.id,
        )
        for node in ast.walk(entrypoint)
        if isinstance(node, ast.Call) and isinstance(node.func, ast.Name)
    )
    lifecycle_calls = [
        name
        for _, name in calls
        if name
        in {
            "synchronize_warrant_formal_frames",
            "rebuild_warrant_formal_consumers",
            "finalize_warrant_formal_consumer_parity",
        }
    ]
    assert lifecycle_calls == [
        "synchronize_warrant_formal_frames",
        "rebuild_warrant_formal_consumers",
        "finalize_warrant_formal_consumer_parity",
    ]
    first_write_line = min(
        lineno for lineno, name in calls if name in {"write_csv", "write_md_table"}
    )
    finalize_line = next(
        lineno
        for lineno, name in calls
        if name == "finalize_warrant_formal_consumer_parity"
    )
    packet_line = next(lineno for lineno, name in calls if name == "write_packet")
    assert finalize_line < first_write_line < packet_line


def test_runtime_subgraph_hash_includes_indirect_repo_local_callback() -> None:
    before = SourceSemanticGraph(
        "runtime.py",
        "def helper():\n    return 1\n\ndef root():\n    callback = helper\n    return callback()\n",
    )
    after = SourceSemanticGraph(
        "runtime.py",
        "def helper():\n    return 2\n\ndef root():\n    callback = helper\n    return callback()\n",
    )
    item = "runtime_subgraph:root"
    assert runtime_subgraph_sha256(before, item) != runtime_subgraph_sha256(after, item)


def test_semantic_baseline_is_immutable_and_pins_all_initial_records() -> None:
    rows = read_csv("config/daily_model_semantic_migrations.csv")
    assert len(rows) >= 1
    baseline = rows[0]
    assert tuple(baseline) == SEMANTIC_MIGRATION_COLUMNS
    assert migration_row_sha256(baseline) == BASELINE_MIGRATION_ROW_SHA256
    assert len(baseline["changed_semantics"].split(";")) == 91
    assert set(baseline["previous_sha256s"].split(";")) == {"BASELINE"}
    tampered = dict(baseline)
    tampered["new_sha256s"] = tampered["new_sha256s"].replace("a", "b", 1)
    assert migration_row_sha256(tampered) != BASELINE_MIGRATION_ROW_SHA256


def test_ast_signature_changes_when_a_referenced_global_changes() -> None:
    before = SourceSemanticGraph("model.py", "LIMIT = 1\n\ndef gate():\n    return LIMIT > 0\n")
    after = SourceSemanticGraph("model.py", "LIMIT = 2\n\ndef gate():\n    return LIMIT > 0\n")
    before_hash = aggregate_semantic_sha256(before.semantic_items(["gate"]))
    after_hash = aggregate_semantic_sha256(after.semantic_items(["gate"]))
    assert before_hash != after_hash


def test_volume_v2_candidate_score_allowlist_ast_is_registry_pinned() -> None:
    source = (ROOT / "scripts/build_daily_candidate_model_layer.py").read_text(
        encoding="utf-8-sig"
    )
    tampered = source.replace(
        'VOLUME_V2_CANDIDATE_SCORE_FIELDS = (\n    "open",',
        'VOLUME_V2_CANDIDATE_SCORE_FIELDS = (\n    "future_candidate_score_semantic",\n    "open",',
        1,
    )
    current_items = SourceSemanticGraph(
        "scripts/build_daily_candidate_model_layer.py", source
    ).semantic_items(["append_volume_breakout_signals"])
    tampered_items = SourceSemanticGraph(
        "scripts/build_daily_candidate_model_layer.py", tampered
    ).semantic_items(["append_volume_breakout_signals"])
    registry = {
        row["semantic_item"]: row
        for row in read_csv("config/daily_model_shared_semantic_registry.csv")
    }

    assert current_items["global:VOLUME_V2_CANDIDATE_SCORE_FIELDS"] == registry[
        "global:VOLUME_V2_CANDIDATE_SCORE_FIELDS"
    ]["canonical_ast_sha256"]
    assert tampered_items["global:VOLUME_V2_CANDIDATE_SCORE_FIELDS"] != registry[
        "global:VOLUME_V2_CANDIDATE_SCORE_FIELDS"
    ]["canonical_ast_sha256"]


def test_strict_csv_rejects_silent_overflow_fields(tmp_path: Path) -> None:
    path = tmp_path / "malformed.csv"
    path.write_text("a,b\n1,2,unexpected\n", encoding="utf-8")
    errors: list[str] = []
    rows = strict_csv_rows(path, ("a", "b"), errors)
    assert rows == []
    assert any("field count 3 does not match header count 2" in error for error in errors)


def test_data_write_scope_overlap_ignores_non_matching_exact_path_with_shared_prefix() -> None:
    assert not _data_write_scopes_overlap(
        "output/latest/volume_breakout_*operation*_latest.csv",
        "output/latest/volume_breakout_watch_latest.csv",
    )


@pytest.mark.parametrize(
    "exact_path",
    [
        "output/latest/volume_breakout_formal_operation_backtest_latest.csv",
        "output/latest/volume_breakout_formal_operation_lifecycle_latest.csv",
        "output/latest/volume_breakout_confirmed_operation_rank_latest.csv",
        "output/latest/volume_breakout_pending_operation_queue_latest.csv",
    ],
)
def test_data_write_scope_overlap_rejects_exact_path_that_matches_glob(
    exact_path: str,
) -> None:
    assert _data_write_scopes_overlap(
        "output/latest/volume_breakout_*operation*_latest.csv",
        exact_path,
    )


def test_data_sharing_registry_uses_model_owned_research_entrypoints() -> None:
    errors, rows = validate_data_sharing(base_ref="")
    assert errors == []
    by_family = {row["data_family_id"]: row for row in rows}
    assert by_family["price_pullback_23ema_research_outputs"]["registered_producers"] == (
        "scripts/build_price_pullback_23ema_research.py"
    )
    assert by_family[
        "hot_theme_pullback_published_signal_research_outputs"
    ]["registered_producers"] == "scripts/build_hot_theme_pullback_research.py"
    assert by_family["pullback_short_reclaim_research_outputs"][
        "registered_producers"
    ] == "scripts/build_pullback_short_reclaim_research.py"
    assert by_family[
        "tdcc_stealth_accumulation_published_signal_research_outputs"
    ]["registered_producers"] == (
        "scripts/build_tdcc_stealth_accumulation_research.py"
    )
    assert by_family[
        "tdcc_short_term_continuation_d5_d10_research_outputs"
    ]["registered_producers"] == (
        "scripts/build_tdcc_short_term_continuation_d5_d10_research.py"
    )
    assert by_family["revenue_unreacted_range_feature_contrast_audit"]["registered_producers"] == (
        "scripts/build_revenue_unreacted_range_research.py"
    )
    assert by_family["revenue_unreacted_range_extreme_return_path_audit"]["registered_producers"] == (
        "scripts/build_revenue_unreacted_range_research.py"
    )
    assert by_family["revenue_unreacted_range_lag_strength_matrix"]["registered_producers"] == (
        "scripts/build_revenue_unreacted_range_research.py"
    )
    assert by_family["revenue_unreacted_range_source_first_condition_audit"][
        "registered_producers"
    ] == "scripts/build_revenue_unreacted_range_research.py"
    assert by_family["revenue_unreacted_range_forward_confirmation_feature_audit"][
        "registered_producers"
    ] == "scripts/build_revenue_unreacted_range_research.py"
    assert by_family["revenue_unreacted_range_rearmed_operation_grid"][
        "registered_producers"
    ] == "scripts/build_revenue_unreacted_range_research.py"
    assert by_family["revenue_unreacted_range_operation_lag_bucket_audit"][
        "registered_producers"
    ] == "scripts/build_revenue_unreacted_range_research.py"
    assert by_family["volume_range_breakout_v2_high_position_improvement_audit"][
        "registered_producers"
    ] == "scripts/build_volume_range_breakout_v2_research.py"
    assert by_family["financial_statement_point_in_time_history"]["registered_producers"] == (
        "scripts/build_financial_statement_pit.py"
    )
    assert by_family["financial_statement_point_in_time_history"]["ownership_mode"] == (
        "approved_shared_objective"
    )
    assert by_family["official_warrant_flow_current_snapshot"]["ownership_mode"] == (
        "latest_context_not_historical"
    )
    assert by_family["official_warrant_flow_current_snapshot"]["consumer_access_mode"] == (
        "current_projection_parity_and_pinned_committed_revision_lineage_audit_only"
    )
    background = {
        row["data_family_id"]: row
        for row in read_csv("config/daily_model_background_data_registry.csv")
    }
    assert "scripts/build_volume_attack_theme_layer.py" in background[
        "official_warrant_flow_current_snapshot"
    ]["consumer_surfaces"].split(";")


def test_hot_theme_pullback_research_outputs_are_model_owned_and_fail_closed() -> None:
    family = "hot_theme_pullback_published_signal_research_outputs"
    migration_id = "hot_theme_pullback_published_signal_research_outputs_20260902"
    approval = (
        "user_requested_four_model_artifact_registration_then_sequential_"
        "backtests_20260902"
    )
    expected_hash = (
        "eed0ec068c227c47c7cfa79372fc7d5c898025f0ea431b067cd70a1d8cfe1eac"
    )
    background = {
        row["data_family_id"]: row
        for row in read_csv("config/daily_model_background_data_registry.csv")
    }
    sharing = {
        row["data_family_id"]: row
        for row in read_csv("config/daily_model_data_sharing_registry.csv")
    }
    migrations = {
        row["migration_id"]: row
        for row in read_csv("config/daily_model_data_sharing_migrations.csv")
    }

    bg = background[family]
    assert bg["scope"] == "model_research_output"
    assert bg["owner_lane"] == "research_backtest"
    assert bg["producer"] == "scripts/build_hot_theme_pullback_research.py"
    assert bg["artifact_path"] == (
        "output/latest/research_backtest/"
        "hot_theme_pullback_published_signal_*_latest.csv"
    )
    assert bg["source_artifacts"].split(";") == [
        "output/history/daily_model_snapshots/"
        "daily_published_model_snapshot_manifest.csv",
        "output/history/daily_model_snapshots/"
        "daily_candidate_model_signals_for_report_*.csv",
        "data/stock_price_history/*.csv",
    ]
    assert bg["consumer_surfaces"] == "research_backtest"
    assert bg["consumer_models"] == "hot_theme_pullback"
    assert bg["validator"] == "scripts/validate_hot_theme_pullback_research.py"
    assert "as_published_signal_exact_membership" in bg["point_in_time_status"]
    assert "point-in-time hot-theme labels" in bg["forbidden_use"]
    assert "current-AST semantic binding" in bg["forbidden_use"]
    assert "promotion evidence" in bg["forbidden_use"]
    assert "events summary and anomaly payload files" in bg["notes"]
    assert "fourth emitted output artifact" in bg["notes"]

    row = sharing[family]
    assert row["ownership_mode"] == "model_owned_not_shared"
    assert row["owner_model_or_family"] == "hot_theme_pullback"
    assert row["registered_producers"] == bg["producer"]
    assert row["producer_write_scope"] == bg["artifact_path"]
    assert row["approved_consumer_models"] == "hot_theme_pullback"
    assert row["data_contract_sha256"] == expected_hash
    assert row["data_contract_sha256"] == data_contract_sha256(bg)
    assert row["last_migration_id"] == migration_id
    assert row["sharing_decision_reference"] == approval
    assert row["formal_evidence_policy"] == (
        "research_only_published_signal_replay_not_formal_or_promotion_evidence"
    )

    migration = migrations[migration_id]
    assert migration["changed_data_families"] == family
    assert migration["previous_contract_sha256s"] == "NEW"
    assert migration["new_contract_sha256s"] == expected_hash
    assert migration["affected_models"] == "hot_theme_pullback"
    assert migration["user_approval_reference"] == approval
    assert migration["migration_status"] == "validated_user_approved_migration"


def test_pullback_short_reclaim_research_outputs_are_model_owned_and_fail_closed() -> None:
    family = "pullback_short_reclaim_research_outputs"
    migration_id = "pullback_short_reclaim_research_outputs_registration_20260902"
    approval = (
        "user_requested_four_model_artifact_registration_then_sequential_"
        "backtests_20260902"
    )
    expected_hash = (
        "b5172cdd7e30e33a328a8d31bfe0069afca213b60b5b08516fb80a15a1354986"
    )
    background = {
        row["data_family_id"]: row
        for row in read_csv("config/daily_model_background_data_registry.csv")
    }
    sharing = {
        row["data_family_id"]: row
        for row in read_csv("config/daily_model_data_sharing_registry.csv")
    }
    migrations = {
        row["migration_id"]: row
        for row in read_csv("config/daily_model_data_sharing_migrations.csv")
    }

    bg = background[family]
    assert bg["scope"] == "model_research_output"
    assert bg["owner_lane"] == "research_backtest"
    assert bg["producer"] == "scripts/build_pullback_short_reclaim_research.py"
    assert bg["artifact_path"] == (
        "output/latest/research_backtest/"
        "pullback_short_reclaim_published_signal_replay_*_latest.csv"
    )
    assert bg["source_artifacts"].split(";") == [
        "output/history/daily_model_snapshots/"
        "daily_published_model_snapshot_manifest.csv",
        "output/history/daily_model_snapshots/"
        "daily_candidate_model_signals_for_report_*.csv",
        "data/stock_price_history/*.csv",
    ]
    assert bg["consumer_surfaces"] == "research_backtest"
    assert bg["consumer_models"] == "pullback_short_reclaim"
    assert bg["validator"] == "scripts/validate_pullback_short_reclaim_research.py"
    assert "latest_registered_revision_per_report_date" in bg["point_in_time_status"]
    assert "exactly one signal event per date and stock" in bg["allowed_use"]
    assert "self-contained immutable replay" in bg["forbidden_use"]
    assert "operation_contract_status is decision_required" in bg["forbidden_use"]
    assert "market-calendar proof is absent" in bg["forbidden_use"]
    assert "promotion evidence" in bg["forbidden_use"]
    assert "exactly three latest CSV artifacts" in bg["notes"]
    assert "snapshot_pipeline_commit_sha" in bg["notes"]
    assert "No model-owned manifest history or docs artifact" in bg["notes"]

    row = sharing[family]
    assert row["ownership_mode"] == "model_owned_not_shared"
    assert row["owner_model_or_family"] == "pullback_short_reclaim"
    assert row["registered_producers"] == bg["producer"]
    assert row["producer_write_scope"] == bg["artifact_path"]
    assert row["approved_consumer_models"] == "pullback_short_reclaim"
    assert row["data_contract_sha256"] == expected_hash
    assert row["data_contract_sha256"] == data_contract_sha256(bg)
    assert row["last_migration_id"] == migration_id
    assert row["sharing_decision_reference"] == approval
    assert row["formal_evidence_policy"] == (
        "research_only_published_signal_replay_not_formal_operation_or_"
        "promotion_evidence"
    )

    migration = migrations[migration_id]
    assert migration["changed_data_families"] == family
    assert migration["previous_contract_sha256s"] == "NEW"
    assert migration["new_contract_sha256s"] == expected_hash
    assert migration["affected_models"] == "pullback_short_reclaim"
    assert migration["user_approval_reference"] == approval
    assert migration["migration_status"] == "validated_user_approved_migration"


def test_tdcc_stealth_accumulation_research_outputs_are_model_owned_and_fail_closed() -> None:
    family = "tdcc_stealth_accumulation_published_signal_research_outputs"
    migration_id = (
        "tdcc_stealth_accumulation_published_signal_research_outputs_20260902"
    )
    approval = (
        "user_requested_four_model_artifact_registration_then_sequential_"
        "backtests_20260902"
    )
    expected_hash = (
        "771d2fa7b6065da58dca2cb3c9331a9a7e53f7e5331b54ff249258dccfee112b"
    )
    background = {
        row["data_family_id"]: row
        for row in read_csv("config/daily_model_background_data_registry.csv")
    }
    sharing = {
        row["data_family_id"]: row
        for row in read_csv("config/daily_model_data_sharing_registry.csv")
    }
    migrations = {
        row["migration_id"]: row
        for row in read_csv("config/daily_model_data_sharing_migrations.csv")
    }

    bg = background[family]
    assert bg["scope"] == "model_research_output"
    assert bg["owner_lane"] == "research_backtest"
    assert bg["producer"] == "scripts/build_tdcc_stealth_accumulation_research.py"
    assert bg["artifact_path"] == (
        "output/research/tdcc_stealth_accumulation/"
        "tdcc_stealth_accumulation_actual_recommendation_replay_*_v1.csv"
    )
    assert bg["source_artifacts"].split(";") == [
        "output/history/daily_model_snapshots/"
        "daily_published_model_snapshot_manifest.csv",
        "output/history/daily_model_snapshots/"
        "daily_candidate_model_signals_for_report_*.csv",
        "data/stock_price_history/*.csv",
    ]
    assert bg["consumer_surfaces"] == "research_backtest"
    assert bg["consumer_models"] == "tdcc_stealth_accumulation"
    assert bg["validator"] == "scripts/validate_tdcc_stealth_accumulation_research.py"
    assert "latest_valid_revision_per_report_date" in bg["point_in_time_status"]
    assert "identity_deduplicated" in bg["point_in_time_status"]
    assert "zero_sample_explicit" in bg["point_in_time_status"]
    assert "same-signal identity deduplication" in bg["allowed_use"]
    assert "header-only detail and three summary rows" in bg["allowed_use"]
    assert "production semantic SHA binding is unavailable" in bg["forbidden_use"]
    assert "do not infer or synthesize recommendation events" in bg["forbidden_use"]
    assert "mutable unpinned price inputs" in bg["forbidden_use"]
    assert "promotion evidence" in bg["forbidden_use"]
    assert "exactly two CSV files" in bg["notes"]
    assert "detail is header-only" in bg["notes"]
    assert "Formal-use trade-eligibility promotion-evidence" in bg["notes"]

    row = sharing[family]
    assert row["ownership_mode"] == "model_owned_not_shared"
    assert row["owner_model_or_family"] == "tdcc_stealth_accumulation"
    assert row["registered_producers"] == bg["producer"]
    assert row["producer_write_scope"] == bg["artifact_path"]
    assert row["consumer_access_mode"] == "owner_model_research_only"
    assert row["approved_consumer_models"] == "tdcc_stealth_accumulation"
    assert row["data_contract_sha256"] == expected_hash
    assert row["data_contract_sha256"] == data_contract_sha256(bg)
    assert row["last_migration_id"] == migration_id
    assert row["sharing_decision_reference"] == approval
    assert row["formal_evidence_policy"] == (
        "research_only_published_signal_replay_not_formal_or_promotion_evidence"
    )
    assert "No synthetic event win rate or operation row is permitted" in row["notes"]

    migration = migrations[migration_id]
    assert migration["changed_data_families"] == family
    assert migration["previous_contract_sha256s"] == "NEW"
    assert migration["new_contract_sha256s"] == expected_hash
    assert migration["affected_models"] == "tdcc_stealth_accumulation"
    assert migration["user_approval_reference"] == approval
    assert migration["migration_status"] == "validated_user_approved_migration"


def test_tdcc_stealth_pit_replay_availability_audit_is_model_owned_and_fail_closed() -> None:
    family = "tdcc_stealth_accumulation_pit_replay_availability_audit"
    migration_id = (
        "tdcc_stealth_accumulation_pit_replay_availability_audit_20260903"
    )
    approval = (
        "user_requested_tdcc_stealth_accumulation_pit_historical_replay_"
        "availability_audit_20260903"
    )
    expected_hash = (
        "b0dbfae2a9a675969f17b2cb6c963569bfb11222a1d8098615f9af81572879db"
    )
    background = {
        row["data_family_id"]: row
        for row in read_csv("config/daily_model_background_data_registry.csv")
    }
    sharing = {
        row["data_family_id"]: row
        for row in read_csv("config/daily_model_data_sharing_registry.csv")
    }
    migrations = {
        row["migration_id"]: row
        for row in read_csv("config/daily_model_data_sharing_migrations.csv")
    }

    bg = background[family]
    assert bg["scope"] == "model_research_output"
    assert bg["owner_lane"] == "research_backtest"
    assert bg["producer"] == (
        "scripts/audit_tdcc_stealth_accumulation_pit_replay_availability.py"
    )
    assert bg["artifact_path"] == (
        "output/research/tdcc_stealth_accumulation/"
        "tdcc_stealth_accumulation_pit_replay_availability_audit_v1.csv"
    )
    assert bg["source_artifacts"].split(";") == [
        "output/history/daily_model_snapshots/"
        "daily_published_model_snapshot_manifest.csv",
        "output/history/daily_model_snapshots/all_candidates_*.csv",
        "output/history/daily_model_snapshots/"
        "daily_candidate_model_signals_for_report_*.csv",
        "output/history/daily_candidate_models/"
        "daily_candidate_model_signal_log.csv",
        "output/history/tdcc/tdcc_holder_ratio_*.csv",
        "output/history/tdcc/tdcc_latest_ratio_raw_*.csv",
        "output/latest/tdcc_dataset_manifest_latest.json",
        "output/history/tdcc/tdcc_dataset_manifest_*.json",
        "output/history/tdcc_signals/tdcc_signal_snapshot.csv",
        "data/tdcc_stock_history_raw/*.csv",
        "data/tdcc_stock_history/*.csv",
        (
            "data/daily_price/"
            "[0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9].csv"
        ),
        "data/stock_price_history/*.csv",
        "config/stock_model_contract_registry.csv",
        "config/daily_model_semantic_ownership.csv",
        "config/daily_model_shared_semantic_registry.csv",
    ]
    assert bg["consumer_surfaces"] == "research_backtest"
    assert bg["consumer_models"] == "tdcc_stealth_accumulation"
    assert bg["validator"] == (
        "scripts/validate_tdcc_stealth_accumulation_pit_replay_availability.py"
    )
    assert bg["point_in_time_status"] == "coverage_backfill_audit_only"
    assert (
        "availability_state=partial_inputs_available_selector_replay_not_formally_available"
        in bg["notes"]
    )
    assert "separately approved historical selector replay" in bg["allowed_use"]
    assert "do not derive synthesize or publish replay events" in bg["forbidden_use"]
    assert (
        "do not use audit rows as a model-specific gate score recommendation or "
        "production rule"
        in bg["forbidden_use"]
    )
    assert "win rates returns or any other performance metric" in bg["forbidden_use"]
    assert "do not import or replay production selector logic" in bg["forbidden_use"]
    assert "promotion evidence" in bg["forbidden_use"]
    for token in (
        "phase_classifier_unresolved",
        "full_historical_selector_replay_unavailable",
        "model_semantic_sha_unavailable_from_snapshot_contract",
        "formal_operation_decision_required",
        "mutable_price_source_unpinned",
        "no_published_tdcc_stealth_signal_rows",
        "formal_use=False",
        "trade_eligible=False",
        "promotion_evidence_allowed=False",
        "promotion_status=blocked",
    ):
        assert token in bg["notes"]

    row = sharing[family]
    assert row["ownership_mode"] == "model_owned_not_shared"
    assert row["owner_model_or_family"] == family
    assert row["registered_producers"] == bg["producer"]
    assert row["producer_write_scope"] == bg["artifact_path"]
    assert row["consumer_access_mode"] == "owner_model_research_only"
    assert row["approved_consumer_models"] == "tdcc_stealth_accumulation"
    assert row["data_contract_sha256"] == expected_hash
    assert row["data_contract_sha256"] == data_contract_sha256(bg)
    assert row["last_migration_id"] == migration_id
    assert row["sharing_decision_reference"] == approval
    assert row["formal_evidence_policy"] == (
        "research_only_availability_audit_not_formal_performance_or_"
        "promotion_evidence"
    )
    assert "cannot contain replay events win rates returns" in row["notes"]

    migration = migrations[migration_id]
    assert migration["changed_data_families"] == family
    assert migration["previous_contract_sha256s"] == "NEW"
    assert migration["new_contract_sha256s"] == expected_hash
    assert migration["affected_models"] == "tdcc_stealth_accumulation"
    assert migration["user_approval_reference"] == approval
    assert migration["migration_status"] == "validated_user_approved_migration"


def test_tdcc_short_term_continuation_d5_d10_research_outputs_are_model_owned_and_fail_closed() -> None:
    family = "tdcc_short_term_continuation_d5_d10_research_outputs"
    migration_id = (
        "tdcc_short_term_continuation_d5_d10_research_output_registration_20260902"
    )
    approval = (
        "user_requested_four_model_artifact_registration_then_sequential_"
        "backtests_20260902"
    )
    expected_hash = (
        "76bfc0980fab217aa63b38988c8919b1fbec8a0b3927a229665897f2285d1caf"
    )
    background = {
        row["data_family_id"]: row
        for row in read_csv("config/daily_model_background_data_registry.csv")
    }
    sharing = {
        row["data_family_id"]: row
        for row in read_csv("config/daily_model_data_sharing_registry.csv")
    }
    migrations = {
        row["migration_id"]: row
        for row in read_csv("config/daily_model_data_sharing_migrations.csv")
    }

    bg = background[family]
    assert bg["scope"] == "model_research_output"
    assert bg["owner_lane"] == "research_backtest"
    assert bg["producer"] == (
        "scripts/build_tdcc_short_term_continuation_d5_d10_research.py"
    )
    assert bg["artifact_path"] == (
        "output/latest/research_backtest/"
        "tdcc_short_term_continuation_d5_d10_research_*"
    )
    assert bg["source_artifacts"].split(";") == [
        "output/history/tdcc_signals/tdcc_signal_snapshot.csv",
        "output/latest/tdcc_dataset_manifest_latest.json",
        "output/history/tdcc/tdcc_holder_ratio_*.csv",
        "data/stock_price_history/*.csv",
        "output/history/research/daily_published_snapshot_ranking_events.csv",
    ]
    assert bg["consumer_surfaces"] == "research_backtest"
    assert bg["consumer_models"] == "tdcc_short_term_continuation_d5_d10"
    assert bg["validator"] == (
        "scripts/validate_tdcc_short_term_continuation_d5_d10_research.py"
    )
    assert "no_event_time_immutable_signal_packet" in bg["point_in_time_status"]
    assert "price_adjustment_not_formally_verified" in bg["point_in_time_status"]
    assert "K/D derived from intraday high and low" in bg["allowed_use"]
    assert "research-only oscillator selector for frozen Rule B" in bg["allowed_use"]
    assert "next-trading-day-open entry" in bg["allowed_use"]
    assert "fixed D+5 or D+10 close exit" in bg["allowed_use"]
    assert "advisory MFE or MAE" in bg["allowed_use"]
    assert "do not treat current TDCC manifest binding as event-time PIT proof" in (
        bg["forbidden_use"]
    )
    assert (
        "do not use intraday high or low or K/D as formal entry exit stop "
        "profit-taking win failure or realized-return prices"
    ) in bg["forbidden_use"]
    assert "let K/D MFE or MAE alone support promotion" in bg["forbidden_use"]
    assert "corrected primary performance" in bg["forbidden_use"]
    assert "four-artifact family" in bg["notes"]
    assert "supplementary only and never a selector or primary metric source" in bg["notes"]
    assert "K/D oscillator used only by frozen research Rule B" in bg["notes"]
    assert "research replay returns use next-trading-day open" in bg["notes"]
    assert "formal_operation_contract_defined formal_use approved_for_daily" in bg["notes"]
    assert "promotion_blocked remains True" in bg["notes"]

    row = sharing[family]
    assert row["ownership_mode"] == "model_owned_not_shared"
    assert row["owner_model_or_family"] == (
        "tdcc_short_term_continuation_d5_d10"
    )
    assert row["registered_producers"] == bg["producer"]
    assert row["producer_write_scope"] == bg["artifact_path"]
    assert row["consumer_access_mode"] == "owner_model_research_only"
    assert row["approved_consumer_models"] == (
        "tdcc_short_term_continuation_d5_d10"
    )
    assert row["data_contract_sha256"] == expected_hash
    assert row["data_contract_sha256"] == data_contract_sha256(bg)
    assert row["last_migration_id"] == migration_id
    assert row["sharing_decision_reference"] == approval
    assert row["formal_evidence_policy"] == (
        "research_only_not_formal_operation_or_promotion_evidence"
    )
    assert "K/D oscillator used only by frozen research Rule B" in row["notes"]
    assert "MFE and MAE" in row["notes"]
    assert "cross-model uses remain fail-closed" in row["notes"]

    migration = migrations[migration_id]
    assert migration["changed_data_families"] == family
    assert migration["previous_contract_sha256s"] == "NEW"
    assert migration["new_contract_sha256s"] == expected_hash
    assert migration["affected_models"] == (
        "tdcc_short_term_continuation_d5_d10"
    )
    assert migration["user_approval_reference"] == approval
    assert migration["migration_status"] == "validated_user_approved_migration"


def test_volume_v2_watch_committed_lineage_audit_is_exactly_registered() -> None:
    approval = "user_authorized_volume_v2_advisory_lineage_refresh_1a_20260815"
    migration_id = "volume_v2_watch_committed_lineage_audit_20260815"
    v2_models = {
        "volume_range_breakout_v2_high_position_volume_attack",
        "volume_range_breakout_v2_low_position_volume_attack",
        "volume_range_breakout_v2_mid_position_momentum_attack",
    }
    background = {
        row["data_family_id"]: row
        for row in read_csv("config/daily_model_background_data_registry.csv")
    }
    sharing = {
        row["data_family_id"]: row
        for row in read_csv("config/daily_model_data_sharing_registry.csv")
    }
    migrations = {
        row["migration_id"]: row
        for row in read_csv("config/daily_model_data_sharing_migrations.csv")
    }

    watch_background = background["volume_v2_watch_committed_lineage_audit"]
    watch_sharing = sharing["volume_v2_watch_committed_lineage_audit"]
    assert watch_background["artifact_path"] == (
        "output/latest/volume_breakout_watch_latest.csv"
    )
    assert watch_background["producer"] == "scripts/build_volume_breakout_watch.py"
    assert set(watch_background["consumer_models"].split(";")) == v2_models
    assert "historical features" in watch_background["forbidden_use"]
    assert "taxonomy historical replay" in watch_background["forbidden_use"]
    assert watch_sharing["ownership_mode"] == "model_family_owned_not_shared"
    assert watch_sharing["data_contract_sha256"] == data_contract_sha256(
        watch_background
    )
    assert watch_sharing["last_migration_id"] == migration_id
    assert watch_sharing["sharing_decision_reference"] == approval

    legacy_background = background["volume_breakout_operation_research_outputs"]
    legacy_sharing = sharing["volume_breakout_operation_research_outputs"]
    assert legacy_background["artifact_path"] == (
        "output/latest/volume_breakout_*operation*_latest.csv"
    )
    assert legacy_sharing["data_contract_sha256"] == data_contract_sha256(
        legacy_background
    )
    assert legacy_sharing["last_migration_id"] == migration_id
    assert legacy_sharing["sharing_decision_reference"] == approval

    migration = migrations[migration_id]
    assert migration["changed_data_families"].split(";") == [
        "volume_breakout_operation_research_outputs",
        "volume_v2_watch_committed_lineage_audit",
    ]
    assert migration["previous_contract_sha256s"].split(";") == [
        "07a5a51735d24d0c78c9d412be9dbe5cdcebe8fd6c88e05f19f4d0d24d712f48",
        "NEW",
    ]
    assert migration["new_contract_sha256s"].split(";") == [
        legacy_sharing["data_contract_sha256"],
        watch_sharing["data_contract_sha256"],
    ]
    assert set(migration["affected_models"].split(";")) == {
        "volume_range_breakout",
        *v2_models,
    }
    assert migration["user_approval_reference"] == approval
    assert migration["migration_status"] == "validated_user_approved_migration"


def test_data_contract_baseline_is_immutable_and_covers_every_family() -> None:
    rows = read_csv("config/daily_model_data_sharing_migrations.csv")
    assert len(rows) == 35
    assert rows[-1]["migration_id"] == (
        "tdcc_stealth_accumulation_pit_replay_availability_audit_20260903"
    )
    baseline = rows[0]
    assert tuple(baseline) == DATA_SHARING_MIGRATION_COLUMNS
    assert data_migration_row_sha256(baseline) == BASELINE_DATA_MIGRATION_ROW_SHA256
    assert len(baseline["changed_data_families"].split(";")) == 25
    assert set(baseline["previous_contract_sha256s"].split(";")) == {"BASELINE"}

    anomaly_migration = rows[1]
    assert anomaly_migration["migration_id"] == "anomaly_candidate_primary_metrics_20260712"
    assert anomaly_migration["migration_status"] == "validated_user_approved_migration"
    assert len(anomaly_migration["changed_data_families"].split(";")) == 12
    assert anomaly_migration["previous_contract_sha256s"].split(";")[-2:] == ["NEW", "NEW"]
    assert set(anomaly_migration["affected_models"].split(";")) == {
        "all_models",
        "price_pullback_23ema",
        "revenue_unreacted_range",
    }
    assert anomaly_migration["user_approval_reference"] == (
        "user_approved_anomaly_root_cause_governance_20260712"
    )

    launch_timing_migration = rows[2]
    assert launch_timing_migration["migration_id"] == (
        "revenue_launch_timing_feature_audit_20260713"
    )
    assert launch_timing_migration["changed_data_families"] == (
        "revenue_unreacted_range_launch_timing_feature_audit"
    )
    assert launch_timing_migration["previous_contract_sha256s"] == "NEW"
    assert launch_timing_migration["new_contract_sha256s"] == (
        "9156f82c9831ba1d0f6b159463eb7571944b9c6fe24cabdf3a068c5ed40aae6e"
    )
    assert launch_timing_migration["affected_models"] == "revenue_unreacted_range"
    assert launch_timing_migration["user_approval_reference"] == (
        "user_requested_revenue_launch_timing_feature_audit_20260713"
    )
    assert launch_timing_migration["migration_status"] == (
        "validated_user_approved_migration"
    )

    source_first_migration = rows[3]
    assert source_first_migration["migration_id"] == (
        "revenue_source_first_known_success_coverage_20260713"
    )
    assert source_first_migration["changed_data_families"] == (
        "revenue_unreacted_range_source_first_condition_audit"
    )
    assert source_first_migration["previous_contract_sha256s"] == "NEW"
    assert source_first_migration["new_contract_sha256s"] == (
        "d0af612a7d09bca295f0b56e6b286ab16d69fd05e0330841ff8a94032742f99a"
    )
    assert source_first_migration["affected_models"] == "revenue_unreacted_range"
    assert source_first_migration["user_approval_reference"] == (
        "user_requested_known_success_coverage_and_condition_adjustment_20260713"
    )
    assert source_first_migration["migration_status"] == (
        "validated_user_approved_migration"
    )

    forward_confirmation_migration = rows[4]
    assert forward_confirmation_migration["migration_id"] == (
        "revenue_forward_confirmation_feature_audit_20260713"
    )
    assert forward_confirmation_migration["changed_data_families"] == (
        "revenue_unreacted_range_forward_confirmation_feature_audit"
    )
    assert forward_confirmation_migration["previous_contract_sha256s"] == "NEW"
    assert forward_confirmation_migration["new_contract_sha256s"] == (
        "995625483248e76a27316420e8de07491158a83f25c3fc443c4f76bb72490dd5"
    )
    assert forward_confirmation_migration["affected_models"] == "revenue_unreacted_range"
    assert forward_confirmation_migration["user_approval_reference"] == (
        "user_requested_forward_confirmation_feature_audit_20260713"
    )
    assert forward_confirmation_migration["migration_status"] == (
        "validated_user_approved_migration"
    )

    rearmed_operation_migration = rows[5]
    assert rearmed_operation_migration["migration_id"] == (
        "revenue_rearmed_operation_grid_20260713"
    )
    assert rearmed_operation_migration["changed_data_families"] == (
        "revenue_unreacted_range_rearmed_operation_grid"
    )
    assert rearmed_operation_migration["previous_contract_sha256s"] == "NEW"
    assert rearmed_operation_migration["new_contract_sha256s"] == (
        "1b3915bf2f82c119820a1ae7b545ed74c91dd83fc24c00a0f5f49481206b1189"
    )
    assert rearmed_operation_migration["affected_models"] == "revenue_unreacted_range"
    assert rearmed_operation_migration["user_approval_reference"] == (
        "user_adopted_rearmed_operation_grid_20260713"
    )
    assert rearmed_operation_migration["migration_status"] == (
        "validated_user_approved_migration"
    )

    price_comparability_migration = rows[6]
    assert price_comparability_migration["migration_id"] == (
        "revenue_price_comparability_2380_20260713"
    )
    assert price_comparability_migration["changed_data_families"] == (
        "revenue_unreacted_range_launch_timing_feature_audit"
    )
    assert price_comparability_migration["previous_contract_sha256s"] == (
        "9156f82c9831ba1d0f6b159463eb7571944b9c6fe24cabdf3a068c5ed40aae6e"
    )
    assert price_comparability_migration["new_contract_sha256s"] == (
        "7fae8b6102f7cac5715ef3845ee6345788bee7d57188c9eff5d754219a632145"
    )
    assert price_comparability_migration["affected_models"] == "revenue_unreacted_range"
    assert price_comparability_migration["user_approval_reference"] == (
        "user_adopted_rearmed_grid_and_required_bottom_level_2380_review_20260713"
    )
    assert price_comparability_migration["migration_status"] == (
        "validated_user_approved_migration"
    )

    operation_lag_migration = rows[7]
    assert operation_lag_migration["migration_id"] == (
        "revenue_operation_lag_bucket_audit_20260714"
    )
    assert operation_lag_migration["changed_data_families"] == (
        "revenue_unreacted_range_source_first_condition_audit;"
        "revenue_unreacted_range_operation_lag_bucket_audit"
    )
    assert operation_lag_migration["previous_contract_sha256s"] == (
        "d0af612a7d09bca295f0b56e6b286ab16d69fd05e0330841ff8a94032742f99a;NEW"
    )
    assert operation_lag_migration["new_contract_sha256s"] == (
        "ed1c90dfeba7846f6078c01a116967b2cc42e695d37471c6892402b9e7acb044;"
        "c204e9e4fe2dfd55da9331272f3084654e9323f025c10950a0cfe92e567af693"
    )
    assert operation_lag_migration["affected_models"] == "revenue_unreacted_range"
    assert operation_lag_migration["user_approval_reference"] == (
        "user_requested_revenue_operation_lag_bucket_audit_20260714"
    )
    assert operation_lag_migration["migration_status"] == (
        "validated_user_approved_migration"
    )

    financial_statement_migration = rows[8]
    assert financial_statement_migration["migration_id"] == (
        "financial_statement_pit_data_layer_20260716"
    )
    assert financial_statement_migration["previous_contract_sha256s"] == "NEW;NEW;NEW"
    assert financial_statement_migration["new_contract_sha256s"] == (
        "ddc0c0a54d0374f8622fb3dbe51a88ca1aa841d2955ca5f1432e81aec9e08f63;"
        "8cccd88ec43a1b8d51577e3776e866881c661e9811746da4e4a5c142af5529f0;"
        "35fc38ac95271dee3ad7aa3fa7671f52dfbdfd4ff26646e43f4bc62a4c2d8aae"
    )
    assert financial_statement_migration["affected_models"] == "all_models"
    assert financial_statement_migration["user_approval_reference"] == (
        "user_requested_financial_statement_pit_data_layer_20260716"
    )
    assert financial_statement_migration["migration_status"] == (
        "validated_user_approved_migration"
    )

    historical_source_audit_migration = rows[9]
    assert historical_source_audit_migration["migration_id"] == (
        "historical_financial_statement_pit_source_audit_20260716"
    )
    assert historical_source_audit_migration["changed_data_families"] == (
        "financial_statement_historical_pit_source_audit"
    )
    assert historical_source_audit_migration["previous_contract_sha256s"] == "NEW"
    assert historical_source_audit_migration["new_contract_sha256s"] == (
        "8da21eb04ed9fce3ffe4c8f1338e78db0736a5e1bee75b35d5eee11ad933f260"
    )
    assert historical_source_audit_migration["affected_models"] == "all_models"
    assert historical_source_audit_migration["user_approval_reference"] == (
        "user_requested_historical_financial_statement_pit_source_audit_20260716"
    )
    assert historical_source_audit_migration["migration_status"] == (
        "validated_user_approved_migration"
    )

    historical_source_retention_migration = rows[10]
    assert historical_source_retention_migration["migration_id"] == (
        "historical_financial_statement_pit_evidence_retention_20260716"
    )
    assert historical_source_retention_migration["changed_data_families"] == (
        "financial_statement_historical_pit_source_audit"
    )
    assert historical_source_retention_migration["previous_contract_sha256s"] == (
        "8da21eb04ed9fce3ffe4c8f1338e78db0736a5e1bee75b35d5eee11ad933f260"
    )
    assert historical_source_retention_migration["new_contract_sha256s"] == (
        "c24fb7342cfdf7e628e049d9d465f5d0b59373607d4448bab1ac9a2227e98d13"
    )
    assert historical_source_retention_migration["affected_models"] == "all_models"
    assert historical_source_retention_migration["user_approval_reference"] == (
        "user_requested_historical_financial_statement_pit_source_audit_continuation_20260716"
    )
    assert historical_source_retention_migration["migration_status"] == (
        "validated_user_approved_migration"
    )

    historical_source_acquisition_v3 = rows[11]
    assert historical_source_acquisition_v3["migration_id"] == (
        "historical_financial_statement_pit_official_acquisition_v3_20260717"
    )
    assert historical_source_acquisition_v3["changed_data_families"] == (
        "financial_statement_historical_pit_source_audit"
    )
    assert historical_source_acquisition_v3["previous_contract_sha256s"] == (
        "c24fb7342cfdf7e628e049d9d465f5d0b59373607d4448bab1ac9a2227e98d13"
    )
    assert historical_source_acquisition_v3["new_contract_sha256s"] == (
        "04170be9ddccd8b40ae0816ff11d3b8428c8568d80ab4e3385683d6d72d056c8"
    )
    assert historical_source_acquisition_v3["affected_models"] == "all_models"
    assert historical_source_acquisition_v3["user_approval_reference"] == (
        "user_requested_historical_financial_statement_official_source_acquisition_continuation_20260717"
    )
    assert historical_source_acquisition_v3["migration_status"] == (
        "validated_user_approved_migration"
    )

    position_shape_migration = rows[12]
    assert position_shape_migration["migration_id"] == (
        "revenue_position_shape_three_anchor_matrix_20260717"
    )
    assert position_shape_migration["changed_data_families"] == (
        "revenue_unreacted_range_position_shape_transition_matrix"
    )
    assert position_shape_migration["previous_contract_sha256s"] == "NEW"
    assert position_shape_migration["new_contract_sha256s"] == (
        "5c41b1f6314159a580ed1bb54811ba96e8c5193235367d4d8d512314077e37ac"
    )
    assert position_shape_migration["affected_models"] == "revenue_unreacted_range"
    assert position_shape_migration["user_approval_reference"] == (
        "user_requested_revenue_position_shape_three_anchor_matrix_20260717"
    )
    assert position_shape_migration["migration_status"] == (
        "validated_user_approved_migration"
    )

    warrant_negative_projection_migration = rows[13]
    assert warrant_negative_projection_migration["migration_id"] == (
        "warrant_flow_volume_negative_projection_guard_20260717"
    )
    assert warrant_negative_projection_migration["changed_data_families"] == (
        "official_warrant_flow_current_snapshot"
    )
    assert warrant_negative_projection_migration["previous_contract_sha256s"] == "NEW"
    assert warrant_negative_projection_migration["new_contract_sha256s"] == (
        "96dc1229637d51e0f026607e88de325033e972b458c0f2aba2de7b6124841f1b"
    )
    assert set(warrant_negative_projection_migration["affected_models"].split(";")) == {
        "volume_range_breakout_v2_high_position_volume_attack",
        "volume_range_breakout_v2_low_position_volume_attack",
        "volume_range_breakout_v2_mid_position_momentum_attack",
    }
    assert warrant_negative_projection_migration["user_approval_reference"] == (
        "user_requested_warrant_flow_formal_sync_completion_20260717"
    )
    assert warrant_negative_projection_migration["migration_status"] == (
        "validated_user_approved_migration"
    )

    historical_source_acquisition_v4 = rows[14]
    assert historical_source_acquisition_v4["migration_id"] == (
        "historical_financial_statement_pit_revision_guard_and_data_eshop_v4_20260717"
    )
    assert historical_source_acquisition_v4["changed_data_families"] == (
        "financial_statement_point_in_time_history;"
        "financial_statement_source_manifest;"
        "financial_statement_pit_coverage_audit;"
        "financial_statement_historical_pit_source_audit"
    )
    assert historical_source_acquisition_v4["previous_contract_sha256s"] == (
        "ddc0c0a54d0374f8622fb3dbe51a88ca1aa841d2955ca5f1432e81aec9e08f63;"
        "8cccd88ec43a1b8d51577e3776e866881c661e9811746da4e4a5c142af5529f0;"
        "35fc38ac95271dee3ad7aa3fa7671f52dfbdfd4ff26646e43f4bc62a4c2d8aae;"
        "04170be9ddccd8b40ae0816ff11d3b8428c8568d80ab4e3385683d6d72d056c8"
    )
    assert historical_source_acquisition_v4["new_contract_sha256s"] == (
        "3392f0a30f9612638a3950d3767211662728c2c55179d1490dff58d22e71e72b;"
        "4df321fd776c4a1fc4dca350ec2ae16538a101af3e3132328840a961c70f013a;"
        "a4357224e45bcab9e0c14b2bb8e5b83c231e426db21e1dbe97506c06859c931d;"
        "975dccb3546cea31bb05f28c3ccd5b5ecf1015898e84abff99b603c784e2bfcb"
    )
    assert historical_source_acquisition_v4["affected_models"] == "all_models"
    assert historical_source_acquisition_v4["user_approval_reference"] == (
        "user_requested_historical_financial_statement_official_source_continuation_20260717"
    )
    assert historical_source_acquisition_v4["migration_status"] == (
        "validated_user_approved_migration"
    )

    warrant_lineage_hardening = rows[15]
    assert warrant_lineage_hardening["migration_id"] == (
        "volume_v2_formal_lineage_hardening_20260718"
    )
    assert warrant_lineage_hardening["changed_data_families"] == (
        "official_warrant_flow_current_snapshot"
    )
    assert warrant_lineage_hardening["previous_contract_sha256s"] == (
        "96dc1229637d51e0f026607e88de325033e972b458c0f2aba2de7b6124841f1b"
    )
    assert warrant_lineage_hardening["new_contract_sha256s"] == (
        "75872e9619017808259ebb41f72655b795ce4154ba128260f4a239ccd5f8b691"
    )
    assert warrant_lineage_hardening["user_approval_reference"] == (
        "user_requested_formal_lineage_hardening_20260718"
    )
    assert warrant_lineage_hardening["migration_status"] == (
        "validated_user_approved_migration"
    )

    canonical_tdcc_consumer = rows[16]
    assert canonical_tdcc_consumer["migration_id"] == (
        "canonical_tdcc_full_history_consumer_20260719"
    )
    assert canonical_tdcc_consumer["changed_data_families"] == (
        "daily_model_signal_background_feature_panel"
    )
    assert canonical_tdcc_consumer["previous_contract_sha256s"] == (
        "3c405af56f0e056f542c7f47fab7d89db25242037b7d1de8bb5887f95eb82c27"
    )
    assert canonical_tdcc_consumer["new_contract_sha256s"] == (
        "ac32d241d118ab1121bffa97f0f3b4b821f0403fe4fbbf53d6624cd4f641cff9"
    )
    assert canonical_tdcc_consumer["migration_status"] == (
        "validated_user_approved_migration"
    )

    snapshot_revision_contract = rows[17]
    assert snapshot_revision_contract["migration_id"] == (
        "daily_snapshot_append_only_revision_contract_20260720"
    )
    assert snapshot_revision_contract["changed_data_families"] == (
        "daily_model_signal_snapshots;daily_all_candidates_snapshots;"
        "daily_model_snapshot_revision_manifest"
    )
    assert snapshot_revision_contract["previous_contract_sha256s"] == (
        "93adf9f60cdbd52b34ddf08d7294f5391af5895b9f80116c4a3259a0dcf308e9;"
        "6f5b7c13d4f6b4478f4ec843066690627c3034abc46cdc5a61e0238ca25226d7;NEW"
    )
    assert snapshot_revision_contract["new_contract_sha256s"] == (
        "78bceca0e4bb643a5d56f86971c488350b44618a3b4c30b30f4c05b0b011f9c7;"
        "43159083c5c2173a45d60a6bb3e7cb892df11073cafb4b55c1b3d8ddb4fde1d8;"
        "affa7abf285f61ed8ddca94f47068b81404940e010b595cb7f71405a84534cb5"
    )
    assert snapshot_revision_contract["user_approval_reference"] == (
        "user_selected_option_1_daily_snapshot_revision_lineage_20260720"
    )
    assert snapshot_revision_contract["migration_status"] == (
        "validated_user_approved_migration"
    )

    low_mid_falling_candidate = rows[19]
    assert low_mid_falling_candidate["migration_id"] == (
        "revenue_low_mid_falling_candidate_audit_20260720"
    )
    assert low_mid_falling_candidate["changed_data_families"] == (
        "revenue_unreacted_range_low_mid_falling_candidate_audit"
    )
    assert low_mid_falling_candidate["previous_contract_sha256s"] == "NEW"
    assert low_mid_falling_candidate["new_contract_sha256s"] == (
        "45ccdded177fa9425bf0d6f2f092f55662734026e7a3dd6a9353c2f9b785ceaa"
    )
    assert low_mid_falling_candidate["affected_models"] == (
        "revenue_unreacted_range"
    )
    assert low_mid_falling_candidate["user_approval_reference"] == (
        "user_requested_revenue_low_mid_falling_research_candidates_20260720"
    )
    assert low_mid_falling_candidate["migration_status"] == (
        "validated_user_approved_migration"
    )

    cross_market_lineage = rows[20]
    assert cross_market_lineage["migration_id"] == (
        "revenue_monthly_cross_market_lineage_resolution_20260720"
    )
    expected_cross_market_contracts = {
        "revenue_unreacted_range_revenue_condition_matrix": (
            "ed8750ab708a521c25dd7fa63ae57575888741f74f3fe1ec5c2915543b6f4cd0",
            "d00447260585f63c729ecd06d984408284393ac5c2de1a136cabe0d8e35f7346",
        ),
        "revenue_unreacted_range_operation_candidate_matrix": (
            "2916eeb6a8b13d73505068aafdea9f85b9d38595529af2866bff65036152419f",
            "fab505e8a651241996203a6aea2dd54de2ab4cd469fec1f6cdbf270967eea630",
        ),
        "revenue_unreacted_range_feature_contrast_audit": (
            "289aab7764939a9eab80a8427d870ce94e7350f87927bd33f1840df26dd897ce",
            "d56a182fb8798d8924aa1d99c3399abd37d8c3505469744dadc19a86349075b3",
        ),
        "revenue_unreacted_range_close_confirmation_timing_audit": (
            "c99b6fb2080896b4cbb432ad6d0e2468bdcd9148c638a469563e545a1c1c2ed4",
            "66c8e65e36e46deaf69a5827a11e638680044aaf1f578b8ab63f8dfc31e09acc",
        ),
        "revenue_unreacted_range_fixed_confirmation_feature_contrast_audit": (
            "cf59df65d092aa900528b0f11a5440a4917386ed77f4fcbae1bcf3850a4a285e",
            "300064197a3b83510f7f16e9f675a4da2ed4846f9184d49088e54e48a56e5576",
        ),
        "revenue_unreacted_range_extreme_return_path_audit": (
            "8b52d4659d3212236328ecb1b2decb582fb6a063bdc598bf98d4bfae79c55719",
            "9de8bfd31d9cea1395ac4ace08504f2353a8c6c3ec2ac53333244020143899e0",
        ),
        "revenue_unreacted_range_lag_strength_matrix": (
            "c42e820afc93e6f467de7103f70b19faae344dcb40e96048ab11318fe75a54df",
            "93a83bd64ba0f7b4a8595ba5683a9cb38e9e35011e3cd6f0bbc514068efa9766",
        ),
        "revenue_unreacted_range_launch_timing_feature_audit": (
            "7fae8b6102f7cac5715ef3845ee6345788bee7d57188c9eff5d754219a632145",
            "a3facf77c3ca4831cd2c9fe47246e84c601f96fcd326b0cf4f2bdacfef9df305",
        ),
        "revenue_unreacted_range_source_first_condition_audit": (
            "ed1c90dfeba7846f6078c01a116967b2cc42e695d37471c6892402b9e7acb044",
            "fca68c6a1eab47d9fca82720981f08afe496f473a9602efd641337adb95acd94",
        ),
        "revenue_unreacted_range_forward_confirmation_feature_audit": (
            "995625483248e76a27316420e8de07491158a83f25c3fc443c4f76bb72490dd5",
            "1a350c64189bdf6ead59dc0d2494f6d07df7f1f18f685de6c41220e8cac43d2c",
        ),
        "revenue_unreacted_range_rearmed_operation_grid": (
            "1b3915bf2f82c119820a1ae7b545ed74c91dd83fc24c00a0f5f49481206b1189",
            "de1c5ff2386087bd64775e4ba01f9fc953be23253828ccd064619b422ddb2449",
        ),
        "revenue_unreacted_range_operation_lag_bucket_audit": (
            "c204e9e4fe2dfd55da9331272f3084654e9323f025c10950a0cfe92e567af693",
            "8720f64feb216362755d9c3a4f503e9233d1ce5a06d04de1a3c1580c7a36863b",
        ),
        "revenue_unreacted_range_position_shape_transition_matrix": (
            "5c41b1f6314159a580ed1bb54811ba96e8c5193235367d4d8d512314077e37ac",
            "c5598b7f0a8c988667f8c635d609a86c4d7f339608c02f2a7a25c1167e278d65",
        ),
        "revenue_unreacted_range_low_mid_falling_candidate_audit": (
            "45ccdded177fa9425bf0d6f2f092f55662734026e7a3dd6a9353c2f9b785ceaa",
            "b92495db71a2fd4534e80ba1c77c5c2d1a1d50effd934e2e188c24804a8d4bd3",
        ),
    }
    assert cross_market_lineage["changed_data_families"].split(";") == list(
        expected_cross_market_contracts
    )
    assert cross_market_lineage["previous_contract_sha256s"].split(";") == [
        old_hash for old_hash, _new_hash in expected_cross_market_contracts.values()
    ]
    assert cross_market_lineage["new_contract_sha256s"].split(";") == [
        new_hash for _old_hash, new_hash in expected_cross_market_contracts.values()
    ]
    assert cross_market_lineage["affected_models"] == "revenue_unreacted_range"
    assert cross_market_lineage["user_approval_reference"] == (
        "user_requested_revenue_low_mid_falling_research_candidates_20260720"
    )
    assert cross_market_lineage["migration_status"] == (
        "validated_user_approved_migration"
    )
    cutoff_migration = next(
        row
        for row in rows
        if row["migration_id"] == "revenue_lag_launch_observation_cutoff_20260802"
    )
    expected_cutoff_contracts = {
        "revenue_unreacted_range_lag_strength_matrix": (
            "93a83bd64ba0f7b4a8595ba5683a9cb38e9e35011e3cd6f0bbc514068efa9766",
            "bb4229a1233d1f9a6e42bd545da7c235202bb4a43846b9066c37cfcf1b50e697",
        ),
        "revenue_unreacted_range_launch_timing_feature_audit": (
            "a3facf77c3ca4831cd2c9fe47246e84c601f96fcd326b0cf4f2bdacfef9df305",
            "929e84bc7611061948a3cefe5ba78961e9b06bcff6375d21eaa75340d7958e2f",
        ),
    }
    assert cutoff_migration["changed_data_families"].split(";") == list(
        expected_cutoff_contracts
    )
    assert cutoff_migration["previous_contract_sha256s"].split(";") == [
        old_hash for old_hash, _new_hash in expected_cutoff_contracts.values()
    ]
    assert cutoff_migration["new_contract_sha256s"].split(";") == [
        new_hash for _old_hash, new_hash in expected_cutoff_contracts.values()
    ]
    assert cutoff_migration["affected_models"] == "revenue_unreacted_range"
    assert cutoff_migration["user_approval_reference"] == (
        "user_authorized_research_only_observation_cutoff_20260802"
    )
    assert cutoff_migration["migration_status"] == (
        "validated_user_approved_migration"
    )
    sharing_by_family = {
        row["data_family_id"]: row
        for row in read_csv("config/daily_model_data_sharing_registry.csv")
    }
    background_by_family = {
        row["data_family_id"]: row
        for row in read_csv("config/daily_model_background_data_registry.csv")
    }
    snapshot_contracts = {
        "revenue_unreacted_range_forward_confirmation_feature_audit": (
            "ad1bbe3e1f76d8680857b7c40d588915582da39e398e39cefcefcbb77da4b637"
        ),
        "revenue_unreacted_range_rearmed_operation_grid": (
            "2d528012095f626e20b67f33ca7df5d357a245874ccbe148769e4a37bf6b611b"
        ),
        "revenue_unreacted_range_operation_lag_bucket_audit": (
            "3038067e652157e31c76a8a4b9254e1184fe1309de87b78ba94b44ed02595d06"
        ),
        "revenue_unreacted_range_low_mid_falling_candidate_audit": (
            "4aff77863a07ba5fe7c574731ea84ac778b85daffbbfe7123d38cccd4cc61432"
        ),
    }
    snapshot_migration_ids = {
        family: "revenue_source_snapshot_projection_20260731"
        for family in snapshot_contracts
    }
    snapshot_migration_ids[
        "revenue_unreacted_range_forward_confirmation_feature_audit"
    ] = "revenue_forward_confirmation_source_snapshot_projection_20260731"
    for family, (_old_hash, new_hash) in expected_cross_market_contracts.items():
        expected_current_hash = (
            snapshot_contracts[family]
            if family in snapshot_contracts
            else expected_cutoff_contracts[family][1]
            if family in expected_cutoff_contracts
            else new_hash
        )
        assert sharing_by_family[family]["data_contract_sha256"] == expected_current_hash
        assert sharing_by_family[family]["last_migration_id"] == (
            snapshot_migration_ids[family]
            if family in snapshot_contracts
            else cutoff_migration["migration_id"]
            if family in expected_cutoff_contracts
            else "revenue_monthly_cross_market_lineage_resolution_20260720"
        )
        assert sharing_by_family[family]["sharing_decision_reference"] == (
            "user_authorized_20260713_source_snapshot_projection_and_955_baseline_20260731"
            if family in snapshot_contracts
            else "user_authorized_research_only_observation_cutoff_20260802"
            if family in expected_cutoff_contracts
            else "user_requested_revenue_low_mid_falling_research_candidates_20260720"
        )
        background = background_by_family[family]
        assert (
            "config/revenue_unreacted_range_monthly_revenue_cross_market_resolution.csv"
            in background["source_artifacts"].split(";")
        )
        if family not in expected_cutoff_contracts:
            assert (
                "registered_exact_lineage_equal_payload_cross_market_mirror_"
                "earliest_availability_fail_closed"
                in background["point_in_time_status"]
            )
            assert (
                "registered exact-lineage equal-payload cross-market mirrors use the "
                "earliest official source-table availability"
                in background["allowed_use"]
            )
            assert (
                "unregistered same-market or conflicting-payload stock-period "
                "collisions fail closed"
                in background["forbidden_use"]
            )
            assert "Raw monthly history remains market-grained" in background["notes"]

    projection_manifest = (
        "output/latest/research_backtest/"
        "revenue_unreacted_range_source_snapshot_projection_manifest_latest.csv"
    )
    projection_detail = (
        "output/latest/research_backtest/"
        "revenue_unreacted_range_source_snapshot_projection_detail_latest.csv"
    )
    cutoff_background_contracts = {
        "revenue_unreacted_range_lag_strength_matrix": {
            "point_in_time_status": (
                "research_only_lag_strength_matrix_immutable_source_snapshot_"
                "cutoff_20260713_fail_closed"
            ),
            "sources": {
                "output/latest/research_backtest/"
                "revenue_unreacted_range_fixed_confirmation_feature_contrast_audit_"
                "detail_latest.csv",
                projection_manifest,
                projection_detail,
                "data/monthly_revenue_history/monthly_revenue_history.csv",
                "data/stock_price_history/*.csv",
                "config/revenue_unreacted_range_monthly_revenue_cross_market_resolution.csv",
            },
        },
        "revenue_unreacted_range_launch_timing_feature_audit": {
            "point_in_time_status": (
                "research_only_launch_timing_immutable_observation_cutoff_"
                "20260713_fail_closed"
            ),
            "sources": {
                "output/latest/research_backtest/"
                "revenue_unreacted_range_lag_strength_matrix_detail_latest.csv",
                projection_manifest,
                projection_detail,
                "data/stock_price_history/*.csv",
                "data/tdcc_stock_history",
                "data/market_index_history.csv",
                "data/monthly_revenue_history/monthly_revenue_history.csv",
                "config/revenue_unreacted_range_price_comparability_resolution.csv",
                "config/revenue_unreacted_range_monthly_revenue_cross_market_resolution.csv",
            },
        },
    }
    for family, contract in cutoff_background_contracts.items():
        _previous_hash, current_hash = expected_cutoff_contracts[family]
        sharing = sharing_by_family[family]
        assert sharing["data_contract_sha256"] == current_hash
        assert sharing["last_migration_id"] == cutoff_migration["migration_id"]
        assert sharing["sharing_decision_reference"] == cutoff_migration[
            "user_approval_reference"
        ]
        background = background_by_family[family]
        assert background["point_in_time_status"] == contract["point_in_time_status"]
        assert contract["sources"] <= set(background["source_artifacts"].split(";"))
        assert "20260713" in background["allowed_use"]
        assert "post-20260713" in background["forbidden_use"]
        assert background["consumer_models"] == "revenue_unreacted_range"

    snapshot_migration = next(
        row
        for row in rows
        if row["migration_id"] == "revenue_source_snapshot_projection_20260731"
    )
    assert snapshot_migration["migration_id"] == (
        "revenue_source_snapshot_projection_20260731"
    )
    assert snapshot_migration["changed_data_families"].split(";") == [
        "revenue_unreacted_range_source_snapshot_projection",
        "revenue_unreacted_range_rearmed_operation_grid",
        "revenue_unreacted_range_operation_lag_bucket_audit",
        "revenue_unreacted_range_low_mid_falling_candidate_audit",
    ]
    assert snapshot_migration["previous_contract_sha256s"].split(";")[0] == "NEW"
    assert snapshot_migration["new_contract_sha256s"].split(";") == [
        "d941b53613e393cc016e4f7b777787b0e9118e6e9d30aa4e00e5a04f959daa79",
        snapshot_contracts["revenue_unreacted_range_rearmed_operation_grid"],
        snapshot_contracts["revenue_unreacted_range_operation_lag_bucket_audit"],
        snapshot_contracts["revenue_unreacted_range_low_mid_falling_candidate_audit"],
    ]
    assert snapshot_migration["user_approval_reference"] == (
        "user_authorized_20260713_source_snapshot_projection_and_955_baseline_20260731"
    )
    projection = sharing_by_family[
        "revenue_unreacted_range_source_snapshot_projection"
    ]
    assert projection["data_contract_sha256"] == data_contract_sha256(
        background_by_family["revenue_unreacted_range_source_snapshot_projection"]
    )
    assert projection["ownership_mode"] == "model_owned_not_shared"
    projection_background = background_by_family[
        "revenue_unreacted_range_source_snapshot_projection"
    ]
    assert projection_background["validator"] == (
        "scripts/validate_revenue_unreacted_range_source_snapshot_projection.py"
    )
    assert "20260713" in projection_background["point_in_time_status"]

    v2_bootstrap_migration = next(
        row
        for row in rows
        if row["migration_id"]
        == "revenue_source_snapshot_projection_v2_bootstrap_20260822"
    )
    v2_bootstrap_families = [
        "revenue_unreacted_range_source_snapshot_projection_v1_archive",
        "revenue_unreacted_range_source_snapshot_projection_v2_candidate",
        "revenue_unreacted_range_source_snapshot_projection_v1_v2_diff",
    ]
    assert v2_bootstrap_migration["changed_data_families"].split(";") == (
        v2_bootstrap_families
    )
    assert v2_bootstrap_migration["previous_contract_sha256s"].split(";") == [
        "NEW",
        "NEW",
        "NEW",
    ]
    assert v2_bootstrap_migration["new_contract_sha256s"].split(";") == [
        data_contract_sha256(background_by_family[family])
        for family in v2_bootstrap_families
    ]
    assert v2_bootstrap_migration["user_approval_reference"] == (
        "user_authorized_revenue_source_snapshot_projection_v2_bootstrap_20260822"
    )
    assert v2_bootstrap_migration["migration_status"] == (
        "validated_user_approved_migration"
    )
    validation_commands = v2_bootstrap_migration["validation_commands"].split(";")
    diff_validator_index = validation_commands.index(
        "python scripts/"
        "validate_revenue_unreacted_range_source_snapshot_projection_v1_v2_diff.py "
        "--v1-manifest output/history/research/"
        "revenue_unreacted_range_source_snapshot_projection_manifest_v1_20260731.csv "
        "--v1-detail output/history/research/"
        "revenue_unreacted_range_source_snapshot_projection_detail_v1_20260731.csv "
        "--v2-manifest output/history/research/"
        "revenue_unreacted_range_source_snapshot_projection_manifest_v2_20260822.csv "
        "--v2-detail output/history/research/"
        "revenue_unreacted_range_source_snapshot_projection_detail_v2_20260822.csv "
        "--diff-summary output/history/research/"
        "revenue_unreacted_range_source_snapshot_projection_v1_20260731_to_v2_20260822_"
        "diff_summary.csv --diff-detail output/history/research/"
        "revenue_unreacted_range_source_snapshot_projection_v1_20260731_to_v2_20260822_"
        "diff_detail.csv"
    )
    assert validation_commands[diff_validator_index + 1 : diff_validator_index + 3] == [
        "python scripts/build_model_data_independence_audit.py",
        "python scripts/validate_model_data_independence.py",
    ]
    for family in v2_bootstrap_families:
        sharing = sharing_by_family[family]
        assert sharing["data_contract_sha256"] == data_contract_sha256(
            background_by_family[family]
        )
        assert sharing["last_migration_id"] == v2_bootstrap_migration[
            "migration_id"
        ]
        assert sharing["sharing_decision_reference"] == v2_bootstrap_migration[
            "user_approval_reference"
        ]
        assert sharing["ownership_mode"] == "model_owned_not_shared"
        assert sharing["approved_consumer_models"] == "revenue_unreacted_range"
    supersede_migration = next(
        row
        for row in rows
        if row["migration_id"]
        == "revenue_source_snapshot_projection_v2_supersede_and_chain_20260822"
    )
    supersede_families = [
        "revenue_unreacted_range_source_snapshot_projection",
        "revenue_unreacted_range_source_snapshot_projection_v2_supersede_evidence",
    ]
    assert supersede_migration["changed_data_families"].split(";") == (
        supersede_families
    )
    assert supersede_migration["previous_contract_sha256s"].split(";") == [
        "d941b53613e393cc016e4f7b777787b0e9118e6e9d30aa4e00e5a04f959daa79",
        "NEW",
    ]
    assert supersede_migration["new_contract_sha256s"].split(";") == [
        data_contract_sha256(background_by_family[family])
        for family in supersede_families
    ]
    assert supersede_migration["user_approval_reference"] == (
        "user_authorized_revenue_source_snapshot_projection_v2_"
        "supersede_and_chain_20260822"
    )
    supersede_commands = supersede_migration["validation_commands"].split(";")
    assert supersede_commands[0] == (
        "python scripts/build_revenue_unreacted_range_research.py "
        "--stage source_snapshot_projection_supersede_and_chain"
    )
    assert all("forward_holdout" not in command for command in supersede_commands)
    assert "promotion_preparation" not in supersede_migration["notes"]
    for family in supersede_families:
        sharing = sharing_by_family[family]
        assert sharing["data_contract_sha256"] == data_contract_sha256(
            background_by_family[family]
        )
        assert sharing["last_migration_id"] == supersede_migration["migration_id"]
        assert sharing["sharing_decision_reference"] == supersede_migration[
            "user_approval_reference"
        ]
        assert sharing["ownership_mode"] == "model_owned_not_shared"
        assert sharing["approved_consumer_models"] == "revenue_unreacted_range"
    assert projection["data_contract_sha256"] == (
        "bb4e654263668b750b73e2009a1fcdee5a334e9493603c849fd393b25a418bfe"
    )
    assert projection["last_migration_id"] == (
        "revenue_source_snapshot_projection_v2_supersede_and_chain_20260822"
    )

    forward_migration = next(
        row
        for row in rows
        if row["migration_id"]
        == "revenue_forward_confirmation_source_snapshot_projection_20260731"
    )
    assert forward_migration["changed_data_families"] == (
        "revenue_unreacted_range_forward_confirmation_feature_audit"
    )
    assert forward_migration["previous_contract_sha256s"] == (
        "1a350c64189bdf6ead59dc0d2494f6d07df7f1f18f685de6c41220e8cac43d2c"
    )
    assert forward_migration["new_contract_sha256s"] == snapshot_contracts[
        "revenue_unreacted_range_forward_confirmation_feature_audit"
    ]
    assert forward_migration["affected_models"] == "revenue_unreacted_range"
    assert forward_migration["user_approval_reference"] == (
        "user_authorized_20260713_source_snapshot_projection_and_955_baseline_20260731"
    )
    assert forward_migration["migration_status"] == (
        "validated_user_approved_migration"
    )
    forward = sharing_by_family[
        "revenue_unreacted_range_forward_confirmation_feature_audit"
    ]
    assert forward["last_migration_id"] == forward_migration["migration_id"]
    assert forward["data_contract_sha256"] == forward_migration[
        "new_contract_sha256s"
    ]
    forward_background = background_by_family[
        "revenue_unreacted_range_forward_confirmation_feature_audit"
    ]
    forward_sources = forward_background["source_artifacts"].split(";")
    assert (
        "output/latest/research_backtest/"
        "revenue_unreacted_range_source_snapshot_projection_manifest_latest.csv"
        in forward_sources
    )
    assert (
        "output/latest/research_backtest/"
        "revenue_unreacted_range_source_snapshot_projection_detail_latest.csv"
        in forward_sources
    )
    assert (
        "output/latest/research_backtest/"
        "revenue_unreacted_range_source_first_condition_audit_detail_latest.csv"
        not in forward_sources
    )
    assert "20260713" in forward_background["point_in_time_status"]
    assert "current source-first fallback" in forward_background["forbidden_use"]
    assert "current source-first fallback is forbidden" in forward_background["notes"]

    theme_warrant_revision_contract = rows[18]
    assert theme_warrant_revision_contract["migration_id"] == (
        "theme_warrant_lineage_revision_contract_20260801"
    )
    assert theme_warrant_revision_contract["changed_data_families"] == (
        "official_warrant_flow_current_snapshot"
    )
    assert theme_warrant_revision_contract["previous_contract_sha256s"] == (
        "75872e9619017808259ebb41f72655b795ce4154ba128260f4a239ccd5f8b691"
    )
    assert theme_warrant_revision_contract["new_contract_sha256s"] == (
        "a7bccc9ab66457283c1070606fc8ef763a07920642255aa79740ab93b3c69d19"
    )
    assert theme_warrant_revision_contract["migration_status"] == (
        "validated_user_approved_migration"
    )

    forward_holdout_migration = next(
        row
        for row in rows
        if row["migration_id"]
        == "revenue_low_mid_falling_forward_holdout_20260811"
    )
    assert forward_holdout_migration["migration_id"] == (
        "revenue_low_mid_falling_forward_holdout_20260811"
    )
    assert forward_holdout_migration["changed_data_families"] == (
        "revenue_unreacted_range_forward_holdout"
    )
    assert forward_holdout_migration["previous_contract_sha256s"] == "NEW"
    assert forward_holdout_migration["new_contract_sha256s"] == (
        "6798ba95d83ead7fdb616d9eff730efa51614f399af7f831780b2183992caae5"
    )
    assert forward_holdout_migration["affected_models"] == (
        "revenue_unreacted_range"
    )
    assert forward_holdout_migration["user_approval_reference"] == (
        "user_authorized_revenue_low_mid_falling_forward_holdout_20260811"
    )
    assert forward_holdout_migration["migration_status"] == (
        "validated_user_approved_migration"
    )

    replay_source_migration = next(
        row
        for row in rows
        if row["migration_id"]
        == "revenue_forward_holdout_replay_source_detail_20260812"
    )
    assert replay_source_migration["changed_data_families"] == (
        "revenue_unreacted_range_forward_holdout"
    )
    assert replay_source_migration["previous_contract_sha256s"] == (
        "6798ba95d83ead7fdb616d9eff730efa51614f399af7f831780b2183992caae5"
    )
    assert replay_source_migration["new_contract_sha256s"] == (
        "64a0b285a5065dd2d4484cca544d31f5b6e887f1bb9a4bf6e076582edd66b561"
    )
    assert replay_source_migration["affected_models"] == (
        "revenue_unreacted_range"
    )
    assert replay_source_migration["user_approval_reference"] == (
        "user_authorized_revenue_forward_holdout_replay_input_20260812"
    )
    assert replay_source_migration["migration_status"] == (
        "validated_user_approved_migration"
    )
    forward_holdout = sharing_by_family[
        "revenue_unreacted_range_forward_holdout"
    ]
    assert forward_holdout["last_migration_id"] == replay_source_migration[
        "migration_id"
    ]
    assert forward_holdout["data_contract_sha256"] == replay_source_migration[
        "new_contract_sha256s"
    ]


def test_forward_confirmation_artifact_lineage_uses_projection_not_current_source() -> None:
    rows = {
        row["artifact_path"]: row
        for row in read_csv("config/report_artifact_lineage.csv")
    }
    prefix = (
        "output/latest/research_backtest/"
        "revenue_unreacted_range_forward_confirmation_feature_audit"
    )
    direct_artifacts = {
        f"{prefix}_latest.csv",
        f"{prefix}_detail_latest.csv",
        f"{prefix}_event_detail_latest.csv",
        f"{prefix}_feature_contrast_latest.csv",
        f"{prefix}_operation_return_review_latest.csv",
    }
    projection_manifest = (
        "output/latest/research_backtest/"
        "revenue_unreacted_range_source_snapshot_projection_manifest_latest.csv"
    )
    projection_detail = (
        "output/latest/research_backtest/"
        "revenue_unreacted_range_source_snapshot_projection_detail_latest.csv"
    )
    mutable_source = (
        "output/latest/research_backtest/"
        "revenue_unreacted_range_source_first_condition_audit_detail_latest.csv"
    )
    for artifact_path in direct_artifacts:
        sources = rows[artifact_path]["source_artifacts"].split(";")
        assert projection_manifest in sources
        assert projection_detail in sources
        assert mutable_source not in sources


def test_forward_holdout_artifact_lineage_lists_only_actual_direct_inputs() -> None:
    rows = {
        row["artifact_path"]: row
        for row in read_csv("config/report_artifact_lineage.csv")
    }
    prefix = "output/latest/research_backtest/revenue_unreacted_range_forward_holdout_"
    projection_manifest = (
        "output/latest/research_backtest/"
        "revenue_unreacted_range_source_snapshot_projection_manifest_latest.csv"
    )
    unconsumed_sources = {
        "output/latest/research_backtest/"
        "revenue_unreacted_range_source_snapshot_projection_detail_latest.csv",
        "output/latest/research_backtest/"
        "revenue_unreacted_range_low_mid_falling_candidate_audit_latest.csv",
    }
    for artifact_name in ("manifest", "event_detail"):
        sources = rows[f"{prefix}{artifact_name}_latest.csv"][
            "source_artifacts"
        ].split(";")
        assert projection_manifest in sources
        assert unconsumed_sources.isdisjoint(sources)

    for artifact_name in (
        "manifest",
        "event_detail",
        "maturity_status",
        "comparison",
        "anomaly_sensitivity",
    ):
        history_path = (
            "output/history/research/"
            f"revenue_unreacted_range_forward_holdout_{artifact_name}.csv"
        )
        assert rows[history_path]["validator"] == (
            "scripts/validate_revenue_unreacted_range_forward_holdout.py"
        )


def test_data_contract_hash_detects_point_in_time_or_forbidden_use_drift() -> None:
    row = read_csv("config/daily_model_background_data_registry.csv")[0]
    original = data_contract_sha256(row)
    changed_pit = dict(row)
    changed_pit["point_in_time_status"] = "silently_changed"
    changed_forbidden = dict(row)
    changed_forbidden["forbidden_use"] = "silently_changed"
    assert data_contract_sha256(changed_pit) != original
    assert data_contract_sha256(changed_forbidden) != original


def test_revenue_cross_market_resolution_contract_requires_one_exact_sha_token() -> None:
    digest = "a" * 64
    rows = {
        family: {
            "notes": (
                "model-owned resolution contract; "
                f"{REVENUE_CROSS_MARKET_RESOLUTION_SHA_TOKEN}{digest}"
            )
        }
        for family in REVENUE_CROSS_MARKET_CONSUMER_FAMILIES
    }
    errors: list[str] = []
    _validate_revenue_cross_market_resolution_contract_binding(rows, digest, errors)
    assert errors == []

    drifted = {family: dict(row) for family, row in rows.items()}
    drifted[REVENUE_CROSS_MARKET_CONSUMER_FAMILIES[0]]["notes"] = (
        f"{REVENUE_CROSS_MARKET_RESOLUTION_SHA_TOKEN}{'b' * 64}"
    )
    errors = []
    _validate_revenue_cross_market_resolution_contract_binding(
        drifted, digest, errors
    )
    assert any("must pin exact" in error for error in errors)


def test_revenue_cross_market_research_artifact_lineage_is_complete() -> None:
    rows = read_csv("config/report_artifact_lineage.csv")
    artifact_paths = [row["artifact_path"] for row in rows]
    assert len(artifact_paths) == len(set(artifact_paths))

    expected_by_family = {
        "revenue_unreacted_range_launch_timing_feature_audit": {
            "output/latest/research_backtest/revenue_unreacted_range_launch_timing_feature_audit_latest.csv",
            "output/latest/research_backtest/revenue_unreacted_range_launch_timing_feature_audit_detail_latest.csv",
            "output/latest/research_backtest/revenue_unreacted_range_launch_timing_feature_audit_feature_contrast_latest.csv",
            "output/latest/research_backtest/revenue_unreacted_range_launch_timing_feature_audit_latest.md",
            "output/history/research/revenue_unreacted_range_launch_timing_feature_audit.csv",
            "output/history/research/revenue_unreacted_range_launch_timing_feature_audit_feature_contrast.csv",
        },
        "revenue_unreacted_range_source_first_condition_audit": {
            "output/latest/research_backtest/revenue_unreacted_range_source_first_condition_audit_latest.csv",
            "output/latest/research_backtest/revenue_unreacted_range_source_first_condition_audit_detail_latest.csv",
            "output/latest/research_backtest/revenue_unreacted_range_source_first_condition_audit_latest.md",
            "output/history/research/revenue_unreacted_range_source_first_condition_audit.csv",
        },
        "revenue_unreacted_range_source_snapshot_projection": {
            "output/latest/research_backtest/revenue_unreacted_range_source_snapshot_projection_manifest_latest.csv",
            "output/latest/research_backtest/revenue_unreacted_range_source_snapshot_projection_detail_latest.csv",
            "output/history/research/revenue_unreacted_range_source_snapshot_projection_manifest.csv",
            "output/history/research/revenue_unreacted_range_source_snapshot_projection_supersede_evidence_v2_20260822.csv",
            "docs/latest/revenue_unreacted_range_source_snapshot_projection_manifest_latest.csv",
        },
        "revenue_unreacted_range_forward_confirmation_feature_audit": {
            "output/latest/research_backtest/revenue_unreacted_range_forward_confirmation_feature_audit_latest.csv",
            "output/latest/research_backtest/revenue_unreacted_range_forward_confirmation_feature_audit_detail_latest.csv",
            "output/latest/research_backtest/revenue_unreacted_range_forward_confirmation_feature_audit_event_detail_latest.csv",
            "output/latest/research_backtest/revenue_unreacted_range_forward_confirmation_feature_audit_feature_contrast_latest.csv",
            "output/latest/research_backtest/revenue_unreacted_range_forward_confirmation_feature_audit_operation_return_review_latest.csv",
            "output/latest/research_backtest/revenue_unreacted_range_forward_confirmation_feature_audit_latest.md",
            "output/history/research/revenue_unreacted_range_forward_confirmation_feature_audit.csv",
            "output/history/research/revenue_unreacted_range_forward_confirmation_feature_audit_feature_contrast.csv",
            "output/history/research/revenue_unreacted_range_forward_confirmation_feature_audit_operation_return_review.csv",
        },
        "revenue_unreacted_range_rearmed_operation_grid": {
            "output/latest/research_backtest/revenue_unreacted_range_rearmed_operation_grid_latest.csv",
            "output/latest/research_backtest/revenue_unreacted_range_rearmed_operation_grid_detail_latest.csv",
            "output/latest/research_backtest/revenue_unreacted_range_rearmed_operation_grid_operation_return_review_latest.csv",
            "output/latest/research_backtest/revenue_unreacted_range_rearmed_operation_grid_latest.md",
            "output/history/research/revenue_unreacted_range_rearmed_operation_grid.csv",
            "output/history/research/revenue_unreacted_range_rearmed_operation_grid_operation_return_review.csv",
        },
        "revenue_unreacted_range_operation_lag_bucket_audit": {
            "output/latest/research_backtest/revenue_unreacted_range_operation_lag_bucket_audit_latest.csv",
            "output/latest/research_backtest/revenue_unreacted_range_operation_lag_bucket_audit_detail_latest.csv",
            "output/latest/research_backtest/revenue_unreacted_range_operation_lag_bucket_audit_latest.md",
            "output/history/research/revenue_unreacted_range_operation_lag_bucket_audit.csv",
        },
        "revenue_unreacted_range_position_shape_transition_matrix": {
            "output/latest/research_backtest/revenue_unreacted_range_position_shape_transition_matrix_latest.csv",
            "output/latest/research_backtest/revenue_unreacted_range_position_shape_transition_matrix_detail_latest.csv",
            "output/latest/research_backtest/revenue_unreacted_range_position_shape_transition_matrix_transition_latest.csv",
            "output/latest/research_backtest/revenue_unreacted_range_position_shape_transition_matrix_latest.md",
            "output/history/research/revenue_unreacted_range_position_shape_transition_matrix.csv",
            "output/history/research/revenue_unreacted_range_position_shape_transition_matrix_transition.csv",
        },
        "revenue_unreacted_range_low_mid_falling_candidate_audit": {
            "output/latest/research_backtest/revenue_unreacted_range_low_mid_falling_candidate_audit_latest.csv",
            "output/latest/research_backtest/revenue_unreacted_range_low_mid_falling_candidate_audit_detail_latest.csv",
            "output/latest/research_backtest/revenue_unreacted_range_low_mid_falling_candidate_audit_paired_confirmation_latest.csv",
            "output/latest/research_backtest/revenue_unreacted_range_low_mid_falling_candidate_audit_feature_contrast_latest.csv",
            "output/latest/research_backtest/revenue_unreacted_range_low_mid_falling_candidate_audit_latest.md",
            "output/history/research/revenue_unreacted_range_low_mid_falling_candidate_audit.csv",
            "output/history/research/revenue_unreacted_range_low_mid_falling_candidate_audit_detail.csv",
            "output/history/research/revenue_unreacted_range_low_mid_falling_candidate_audit_paired_confirmation.csv",
            "output/history/research/revenue_unreacted_range_low_mid_falling_candidate_audit_feature_contrast.csv",
        },
        "revenue_unreacted_range_forward_holdout": {
            "output/latest/research_backtest/revenue_unreacted_range_forward_holdout_manifest_latest.csv",
            "output/latest/research_backtest/revenue_unreacted_range_forward_holdout_event_detail_latest.csv",
            "output/latest/research_backtest/revenue_unreacted_range_forward_holdout_maturity_status_latest.csv",
            "output/latest/research_backtest/revenue_unreacted_range_forward_holdout_comparison_latest.csv",
            "output/latest/research_backtest/revenue_unreacted_range_forward_holdout_anomaly_sensitivity_latest.csv",
            "output/latest/research_backtest/revenue_unreacted_range_forward_holdout_replay_source_detail_latest.csv",
            "output/history/research/revenue_unreacted_range_forward_holdout_manifest.csv",
            "output/history/research/revenue_unreacted_range_forward_holdout_event_detail.csv",
            "output/history/research/revenue_unreacted_range_forward_holdout_maturity_status.csv",
            "output/history/research/revenue_unreacted_range_forward_holdout_comparison.csv",
            "output/history/research/revenue_unreacted_range_forward_holdout_anomaly_sensitivity.csv",
        },
    }
    row_by_path = {row["artifact_path"]: row for row in rows}
    for family, expected_paths in expected_by_family.items():
        actual_paths = {
            path for path in artifact_paths if Path(path).name.startswith(family)
        }
        assert actual_paths == expected_paths
        for path in expected_paths:
            row = row_by_path[path]
            if "_latest.csv" in path and "output/latest/" in path:
                assert (
                    "config/revenue_unreacted_range_monthly_revenue_cross_market_resolution.csv"
                    in row["source_artifacts"].split(";")
                )


def test_revenue_cross_market_resolution_canonical_sha_is_semantic_and_stable() -> None:
    row = {
        column: f"value-{column}"
        for column in REVENUE_CROSS_MARKET_RESOLUTION_CANONICAL_COLUMNS
    }
    row.update(
        {
            "model_id": "revenue_unreacted_range",
            "stock_id": "5236.0",
            "revenue_period": "2026-06",
            "earlier_market": "OTC",
            "earlier_source_market_name": "tpex",
            "earlier_source_table_date": "2026-07-15",
            "later_market": "LISTED",
            "later_source_market_name": "twse",
            "later_source_table_date": "2026-07-17",
            "official_market_transition_date": "2026-07-16",
            "canonical_source_table_date": "2026-07-15",
            "formal_model_use_allowed": "False",
            "notes": "not part of the canonical payload",
        }
    )
    normalized_equivalent = dict(row)
    normalized_equivalent.update(
        {
            "stock_id": "5236",
            "revenue_period": "202606",
            "earlier_market": "otc",
            "earlier_source_market_name": "TPEX",
            "earlier_source_table_date": "20260715",
            "later_market": "listed",
            "later_source_market_name": "TWSE",
            "later_source_table_date": "20260717",
            "official_market_transition_date": "20260716",
            "canonical_source_table_date": "20260715",
            "formal_model_use_allowed": "false",
            "notes": "changed but intentionally excluded",
        }
    )
    digest = _revenue_cross_market_resolution_registry_canonical_sha256([row])
    assert digest == _revenue_cross_market_resolution_registry_canonical_sha256(
        [normalized_equivalent]
    )

    changed_raw_binding = dict(row)
    changed_raw_binding["earlier_raw_row_canonical_sha256"] = "b" * 64
    assert digest != _revenue_cross_market_resolution_registry_canonical_sha256(
        [changed_raw_binding]
    )


def test_financial_statement_revision_guard_migrates_every_changed_shared_contract() -> None:
    rows = {
        row["data_family_id"]: row
        for row in read_csv("config/daily_model_data_sharing_registry.csv")
    }
    migration_id = (
        "historical_financial_statement_pit_revision_guard_and_data_eshop_v4_20260717"
    )
    expected_hashes = {
        "financial_statement_point_in_time_history": (
            "3392f0a30f9612638a3950d3767211662728c2c55179d1490dff58d22e71e72b"
        ),
        "financial_statement_source_manifest": (
            "4df321fd776c4a1fc4dca350ec2ae16538a101af3e3132328840a961c70f013a"
        ),
        "financial_statement_pit_coverage_audit": (
            "a4357224e45bcab9e0c14b2bb8e5b83c231e426db21e1dbe97506c06859c931d"
        ),
        "financial_statement_historical_pit_source_audit": (
            "975dccb3546cea31bb05f28c3ccd5b5ecf1015898e84abff99b603c784e2bfcb"
        ),
    }
    for family, expected_hash in expected_hashes.items():
        assert rows[family]["last_migration_id"] == migration_id
        assert rows[family]["data_contract_sha256"] == expected_hash
        assert rows[family]["sharing_decision_reference"] == (
            "user_requested_historical_financial_statement_official_source_continuation_20260717"
        )


def test_production_importing_audits_cannot_claim_independent_evidence() -> None:
    errors, rows = validate_validator_independence()
    assert errors == []
    importing = [row for row in rows if row["imported_production_symbols"]]
    assert importing
    assert all(row["independence_claim"] == "False" for row in importing)
    guard = next(
        row for row in rows if row["validator_path"] == "scripts/validate_model_data_independence.py"
    )
    assert guard["independence_claim"] == "True"
    revenue_guard = next(
        row
        for row in rows
        if row["validator_path"]
        == "scripts/validate_revenue_unreacted_range_financial_statement_fail_closed.py"
    )
    assert revenue_guard["independence_claim"] == "True"
    research_independent = {
        row["validator_path"]: row
        for row in rows
        if row["validator_path"]
        in {
            "scripts/validate_revenue_unreacted_range_monthly_revenue_cross_market_resolution.py",
            "scripts/validate_revenue_unreacted_range_low_mid_falling_candidate_audit.py",
            "scripts/validate_revenue_unreacted_range_promotion_preparation.py",
        }
    }
    assert set(research_independent) == {
        "scripts/validate_revenue_unreacted_range_monthly_revenue_cross_market_resolution.py",
        "scripts/validate_revenue_unreacted_range_low_mid_falling_candidate_audit.py",
        "scripts/validate_revenue_unreacted_range_promotion_preparation.py",
    }
    expected_sources = {
        "scripts/validate_revenue_unreacted_range_monthly_revenue_cross_market_resolution.py": (
            "scripts/revenue_unreacted_range_monthly_revenue_cross_market_resolution.py"
        ),
        "scripts/validate_revenue_unreacted_range_low_mid_falling_candidate_audit.py": (
            "scripts/revenue_unreacted_range_low_mid_falling_candidate_audit.py"
        ),
        "scripts/validate_revenue_unreacted_range_promotion_preparation.py": (
            "scripts/revenue_unreacted_range_low_mid_falling_candidate_audit.py"
        ),
    }
    for path, row in research_independent.items():
        assert row["independence_claim"] == "True"
        assert row["imported_production_symbols"] == ""
        assert row["production_source_file"] == expected_sources[path]
        assert "independent" in row["allowed_evidence_use"]
        assert "not_promotion_proof" in row["allowed_evidence_use"]
        sources, symbols = _production_imports(
            ROOT / path,
            {Path(expected_sources[path]).stem: expected_sources[path]},
        )
        assert sources == ()
        assert symbols == ()


def test_input_bound_independent_validator_role_is_closed_set_and_registered() -> None:
    assert VALID_INDEPENDENT_VALIDATOR_ROLES == {
        "independent_contract_ast_guard",
        "independent_contract_artifact_binding_validator",
        "independent_source_lineage_validator",
        "independent_research_replay_validator",
        "input_bound_in_process_independent_validator",
    }
    rows = {
        row["validator_path"]: row
        for row in read_csv("config/daily_model_validator_independence.csv")
    }
    forward = rows["scripts/validate_revenue_unreacted_range_forward_holdout.py"]
    assert forward["validator_role"] == (
        "input_bound_in_process_independent_validator"
    )
    assert forward["production_source_file"] == (
        "scripts/build_revenue_unreacted_range_research.py"
    )
    assert forward["imported_production_symbols"] == ""
    assert forward["independence_claim"] == "True"
    assert forward["allowed_evidence_use"] == (
        "independent_input_bound_research_validation_only_not_promotion_proof"
    )


def test_revenue_projection_v1_v2_diff_validator_is_independent_and_research_only() -> None:
    rows = {
        row["validator_path"]: row
        for row in read_csv("config/daily_model_validator_independence.csv")
    }
    path = (
        "scripts/"
        "validate_revenue_unreacted_range_source_snapshot_projection_v1_v2_diff.py"
    )
    source = (
        "scripts/revenue_unreacted_range_source_snapshot_projection_v1_v2_diff.py"
    )
    row = rows[path]
    assert row["validator_role"] == (
        "independent_contract_artifact_binding_validator"
    )
    assert row["production_source_file"] == source
    assert row["imported_production_symbols"] == ""
    assert row["independence_claim"] == "True"
    assert row["allowed_evidence_use"] == (
        "independent_research_projection_version_diff_evidence_only_"
        "not_promotion_proof"
    )
    sources, symbols = _production_imports(
        ROOT / path,
        {Path(source).stem: source},
    )
    assert sources == ()
    assert symbols == ()


def test_future_model_owned_module_import_is_detected(tmp_path: Path) -> None:
    validator = tmp_path / "validate_future_model.py"
    validator.write_text("from future_model import condition, score\n", encoding="utf-8")
    sources, symbols = _production_imports(
        validator, {"future_model": "scripts/models/future_model.py"}
    )
    assert sources == ("scripts/models/future_model.py",)
    assert symbols == ("condition", "score")


def test_independent_validator_declared_source_cannot_hide_other_repo_import(
    tmp_path: Path,
) -> None:
    validator = tmp_path / "validate_substitution.py"
    validator.write_text("from producer_b import business_rule\n", encoding="utf-8")
    declared_sources = {"scripts/producer_a.py"}
    errors: list[str] = []
    repo_modules = _python_source_module_map(
        {*declared_sources, "scripts/producer_b.py"},
        errors,
    )

    assert errors == []
    _validate_independent_governed_imports(
        "scripts/validate_substitution.py",
        validator,
        repo_modules,
        {"scripts/producer_b.py"},
        set(),
        {},
        errors,
    )

    assert errors == [
        "scripts/validate_substitution.py: independent validator imports governed "
        "producer business logic: scripts/producer_b.py; symbols=business_rule"
    ]
    assert "scripts/producer_b.py" not in declared_sources


def test_canonical_lineage_producer_is_in_current_governed_import_contract(
    tmp_path: Path,
) -> None:
    errors: list[str] = []
    validator_rows = read_csv("config/daily_model_validator_independence.csv")
    canonical_lineage_rows = read_csv(
        "config/daily_model_canonical_field_lineage_registry.csv"
    )
    canonical_producer = next(
        row["producer"]
        for row in canonical_lineage_rows
        if row["lineage_id"] == "score__all_candidates_current"
    )
    (
        repo_modules,
        governed_sources,
        technical_utility_sources,
        technical_symbols_by_source,
    ) = _governed_business_import_contract(
        validator_rows,
        _active_stock_models(errors),
        _active_repo_python_sources(errors),
        errors,
    )
    assert errors == []
    assert canonical_producer in governed_sources

    validator = tmp_path / "validate_canonical_lineage.py"
    validator.write_text(
        f"from {Path(canonical_producer).stem} import load_all_sources\n",
        encoding="utf-8",
    )
    _validate_independent_governed_imports(
        "scripts/validate_canonical_lineage.py",
        validator,
        repo_modules,
        governed_sources,
        technical_utility_sources,
        technical_symbols_by_source,
        errors,
    )
    assert errors == [
        "scripts/validate_canonical_lineage.py: independent validator imports governed "
        f"producer business logic: {canonical_producer}; symbols=load_all_sources"
    ]


def test_independent_validator_package_import_cannot_hide_governed_producer(
    tmp_path: Path,
) -> None:
    scripts = tmp_path / "scripts"
    scripts.mkdir()
    validator = scripts / "validate_substitution.py"
    validator.write_text(
        "from scripts import producer_b as hidden\n",
        encoding="utf-8",
    )
    producer = scripts / "producer_b.py"
    producer.write_text("def business_rule(): return True\n", encoding="utf-8")
    errors: list[str] = []
    repo_modules = _python_source_module_map(
        {"scripts/producer_b.py"},
        errors,
    )
    _validate_independent_governed_imports(
        "scripts/validate_substitution.py",
        validator,
        repo_modules,
        {"scripts/producer_b.py"},
        set(),
        {},
        errors,
        repo_root=tmp_path,
    )

    assert errors == [
        "scripts/validate_substitution.py: independent validator imports governed "
        "producer business logic: scripts/producer_b.py; symbols=*"
    ]


def test_independent_validator_relative_import_cannot_hide_governed_producer(
    tmp_path: Path,
) -> None:
    package = tmp_path / "scripts" / "fixture_package"
    package.mkdir(parents=True)
    validator = package / "validate_substitution.py"
    validator.write_text("from . import producer_b\n", encoding="utf-8")
    producer = package / "producer_b.py"
    producer.write_text("def business_rule(): return True\n", encoding="utf-8")
    errors: list[str] = []
    repo_modules = _python_source_module_map(
        {"scripts/fixture_package/producer_b.py"},
        errors,
    )
    _validate_independent_governed_imports(
        "scripts/fixture_package/validate_substitution.py",
        validator,
        repo_modules,
        {"scripts/fixture_package/producer_b.py"},
        set(),
        {},
        errors,
        repo_root=tmp_path,
    )

    assert errors == [
        "scripts/fixture_package/validate_substitution.py: independent validator "
        "imports governed producer business logic: "
        "scripts/fixture_package/producer_b.py; symbols=*"
    ]


def test_independent_validator_helper_cannot_hide_transitive_governed_import(
    tmp_path: Path,
) -> None:
    scripts = tmp_path / "scripts"
    scripts.mkdir()
    validator = scripts / "validate_with_helper.py"
    validator.write_text(
        "from validation_helper import validate_binding\n",
        encoding="utf-8",
    )
    helper = scripts / "validation_helper.py"
    helper.write_text(
        "from producer_b import business_rule\n"
        "def validate_binding(): return business_rule()\n",
        encoding="utf-8",
    )
    producer = scripts / "producer_b.py"
    producer.write_text("def business_rule(): return True\n", encoding="utf-8")
    errors: list[str] = []
    repo_modules = _python_source_module_map(
        {
            "scripts/producer_b.py",
            "scripts/validation_helper.py",
        },
        errors,
    )
    _validate_independent_governed_imports(
        "scripts/validate_with_helper.py",
        validator,
        repo_modules,
        {"scripts/producer_b.py"},
        set(),
        {},
        errors,
        repo_root=tmp_path,
    )

    assert errors == [
        "scripts/validate_with_helper.py: independent validator imports governed "
        "producer business logic: scripts/producer_b.py; symbols=business_rule"
    ]


def test_independent_validator_can_import_non_producer_validation_helper(
    tmp_path: Path,
) -> None:
    scripts = tmp_path / "scripts"
    scripts.mkdir()
    validator = scripts / "validate_with_helper.py"
    validator.write_text(
        "from validation_helper import validate_binding\n",
        encoding="utf-8",
    )
    (scripts / "validation_helper.py").write_text(
        "from validation_leaf import validate_leaf\n"
        "def validate_binding(): return validate_leaf()\n",
        encoding="utf-8",
    )
    (scripts / "validation_leaf.py").write_text(
        "def validate_leaf(): return True\n",
        encoding="utf-8",
    )
    errors: list[str] = []
    repo_modules = _python_source_module_map(
        {
            "scripts/producer.py",
            "scripts/validation_helper.py",
            "scripts/validation_leaf.py",
        },
        errors,
    )
    _validate_independent_governed_imports(
        "scripts/validate_with_helper.py",
        validator,
        repo_modules,
        {"scripts/producer.py"},
        set(),
        {},
        errors,
        repo_root=tmp_path,
    )

    assert errors == []


def test_independent_validator_technical_import_exceptions_are_narrow(
    tmp_path: Path,
) -> None:
    scripts = tmp_path / "scripts"
    scripts.mkdir()
    validator = scripts / "validate_technical.py"
    validator.write_text(
        "from synthetic_independence_technical_utility import read_csv\n"
        "from mixed_producer import num\n",
        encoding="utf-8",
    )
    (scripts / "synthetic_independence_technical_utility.py").write_text(
        "def read_csv(path): return path\n",
        encoding="utf-8",
    )
    (scripts / "mixed_producer.py").write_text(
        "def num(value): return value\n"
        "def business_rule(): return True\n",
        encoding="utf-8",
    )
    errors: list[str] = []
    repo_modules = _python_source_module_map(
        {
            "scripts/synthetic_independence_technical_utility.py",
            "scripts/mixed_producer.py",
        },
        errors,
    )
    _validate_independent_governed_imports(
        "scripts/validate_technical.py",
        validator,
        repo_modules,
        {"scripts/mixed_producer.py"},
        {"scripts/synthetic_independence_technical_utility.py"},
        {"scripts/mixed_producer.py": {"num"}},
        errors,
        repo_root=tmp_path,
    )
    assert errors == []

    validator.write_text(
        "from mixed_producer import business_rule\n",
        encoding="utf-8",
    )
    _validate_independent_governed_imports(
        "scripts/validate_technical.py",
        validator,
        repo_modules,
        {"scripts/mixed_producer.py"},
        {"scripts/synthetic_independence_technical_utility.py"},
        {"scripts/mixed_producer.py": {"num"}},
        errors,
        repo_root=tmp_path,
    )
    assert errors == [
        "scripts/validate_technical.py: independent validator imports governed "
        "producer business logic: scripts/mixed_producer.py; symbols=business_rule"
    ]


def test_new_model_cannot_reuse_contained_legacy_monolith_status() -> None:
    ownership = read_csv("config/daily_model_semantic_ownership.csv")
    shared = read_csv("config/daily_model_shared_semantic_registry.csv")
    migrations = read_csv("config/daily_model_semantic_migrations.csv")
    fake = dict(ownership[0])
    fake["model_id"] = "future_model"
    fake["ownership_status"] = "contained_legacy_monolith"
    errors: list[str] = []
    _validate_current_migration_chain([*ownership, fake], shared, migrations, errors)
    assert any("new formal model must use a model-owned module" in error for error in errors)
