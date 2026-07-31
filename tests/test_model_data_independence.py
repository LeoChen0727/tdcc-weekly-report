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
    SourceSemanticGraph,
    _production_imports,
    _revenue_cross_market_resolution_registry_canonical_sha256,
    _validate_revenue_cross_market_resolution_contract_binding,
    _validate_current_migration_chain,
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
    assert len(rows) == 89
    assert by_item["global:MODEL_SCORE_PROFILES"]["semantic_class"] == (
        "contained_legacy_cross_model_semantic"
    )
    assert by_item["function:bottom_volume_attack_like"]["consumer_models"] == (
        "revenue_unreacted_range;tdcc_stealth_accumulation"
    )
    assert by_item["function:text"]["semantic_class"] == "shared_technical"
    assert by_item["function:append_volume_breakout_signals"]["consumer_models"] == (
        "volume_range_breakout_v2_high_position_volume_attack;"
        "volume_range_breakout_v2_low_position_volume_attack;"
        "volume_range_breakout_v2_mid_position_momentum_attack"
    )
    for family_helper in (
        "function:append_volume_breakout_signals",
        "function:volume_v2_candidate_lookup",
    ):
        assert by_item[family_helper]["semantic_class"] == (
            "contained_model_family_semantic"
        )
        assert by_item[family_helper]["last_migration_id"] == (
            "volume_v2_formal_lineage_hardening_20260718"
        )
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
    expected_consumers = ";".join(sorted(ACTIVE_MODELS))
    for item, row in runtime_rows.items():
        assert row["semantic_class"] == "registered_cross_model_runtime_semantic"
        assert row["consumer_models"] == expected_consumers
        assert row["canonical_ast_sha256"] == runtime_subgraph_sha256(graph, item)
        expected_migration = (
            "volume_v2_advisory_asof_slice_lineage_20260727"
            if item
            in {
                "runtime_subgraph:run_warrant_formal_sync_only",
                "runtime_subgraph:synchronize_warrant_formal_frames",
            }
            else "warrant_fixed_membership_runtime_semantics_20260720"
        )
        assert row["last_migration_id"] == expected_migration

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
    assert migration["affected_models"] == expected_consumers


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
    assert migration["new_sha256s"].split(";") == [
        semantic_record_sha256(key, row)
        for key, row in zip(changed, current_rows)
    ]
    expected_consumers = ";".join(sorted(ACTIVE_MODELS))
    assert migration["affected_models"] == expected_consumers
    assert migration["user_approval_reference"] == approval
    assert migration["migration_status"] == "validated_user_approved_migration"
    for key, row in zip(changed, current_rows):
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


def test_data_sharing_registry_uses_model_owned_research_entrypoints() -> None:
    errors, rows = validate_data_sharing(base_ref="")
    assert errors == []
    by_family = {row["data_family_id"]: row for row in rows}
    assert by_family["price_pullback_23ema_research_outputs"]["registered_producers"] == (
        "scripts/build_price_pullback_23ema_research.py"
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
        "current_date_negative_or_exact_projection_parity_guard_only"
    )
    background = {
        row["data_family_id"]: row
        for row in read_csv("config/daily_model_background_data_registry.csv")
    }
    assert "scripts/build_volume_attack_theme_layer.py" in background[
        "official_warrant_flow_current_snapshot"
    ]["consumer_surfaces"].split(";")


def test_data_contract_baseline_is_immutable_and_covers_every_family() -> None:
    rows = read_csv("config/daily_model_data_sharing_migrations.csv")
    assert len(rows) == 22
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

    low_mid_falling_candidate = rows[18]
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

    cross_market_lineage = rows[19]
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
        expected_current_hash = snapshot_contracts.get(family, new_hash)
        assert sharing_by_family[family]["data_contract_sha256"] == expected_current_hash
        assert sharing_by_family[family]["last_migration_id"] == (
            snapshot_migration_ids[family]
            if family in snapshot_contracts
            else "revenue_monthly_cross_market_lineage_resolution_20260720"
        )
        assert sharing_by_family[family]["sharing_decision_reference"] == (
            "user_authorized_20260713_source_snapshot_projection_and_955_baseline_20260731"
            if family in snapshot_contracts
            else "user_requested_revenue_low_mid_falling_research_candidates_20260720"
        )
        background = background_by_family[family]
        assert (
            "config/revenue_unreacted_range_monthly_revenue_cross_market_resolution.csv"
            in background["source_artifacts"].split(";")
        )
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
    assert projection["data_contract_sha256"] == (
        "d941b53613e393cc016e4f7b777787b0e9118e6e9d30aa4e00e5a04f959daa79"
    )
    assert projection["ownership_mode"] == "model_owned_not_shared"
    projection_background = background_by_family[
        "revenue_unreacted_range_source_snapshot_projection"
    ]
    assert projection_background["validator"] == (
        "scripts/validate_revenue_unreacted_range_source_snapshot_projection.py"
    )
    assert "20260713" in projection_background["point_in_time_status"]

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
        }
    }
    assert set(research_independent) == {
        "scripts/validate_revenue_unreacted_range_monthly_revenue_cross_market_resolution.py",
        "scripts/validate_revenue_unreacted_range_low_mid_falling_candidate_audit.py",
    }
    expected_sources = {
        "scripts/validate_revenue_unreacted_range_monthly_revenue_cross_market_resolution.py": (
            "scripts/revenue_unreacted_range_monthly_revenue_cross_market_resolution.py"
        ),
        "scripts/validate_revenue_unreacted_range_low_mid_falling_candidate_audit.py": (
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


def test_future_model_owned_module_import_is_detected(tmp_path: Path) -> None:
    validator = tmp_path / "validate_future_model.py"
    validator.write_text("from future_model import condition, score\n", encoding="utf-8")
    sources, symbols = _production_imports(
        validator, {"future_model": "scripts/models/future_model.py"}
    )
    assert sources == ("scripts/models/future_model.py",)
    assert symbols == ("condition", "score")


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
