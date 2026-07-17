from __future__ import annotations

import csv
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))

from model_data_independence import (  # noqa: E402
    BASELINE_MIGRATION_ROW_SHA256,
    BASELINE_DATA_MIGRATION_ROW_SHA256,
    DATA_SHARING_MIGRATION_COLUMNS,
    SEMANTIC_MIGRATION_COLUMNS,
    SourceSemanticGraph,
    _production_imports,
    _validate_current_migration_chain,
    aggregate_semantic_sha256,
    data_contract_sha256,
    data_migration_row_sha256,
    migration_row_sha256,
    strict_csv_rows,
    validate_data_sharing,
    validate_model_semantic_ownership,
    validate_validator_independence,
)
from validate_model_data_independence import validate, validate_audit_artifact  # noqa: E402


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


def test_model_data_independence_validator_passes() -> None:
    assert validate(base_ref="") == []


def test_model_data_independence_audit_is_current_and_mirrored() -> None:
    assert validate_audit_artifact() == []


def test_every_active_model_has_exact_ast_semantic_ownership() -> None:
    errors, semantics = validate_model_semantic_ownership(base_ref="")
    assert errors == []
    assert set(semantics) == ACTIVE_MODELS
    assert all(model.semantic_sha256 and model.items for model in semantics.values())


def test_shared_business_semantics_are_disclosed_as_contained_not_technical() -> None:
    rows = read_csv("config/daily_model_shared_semantic_registry.csv")
    by_item = {row["semantic_item"]: row for row in rows}
    assert len(rows) == 79
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
        "function:taxonomy_lookup",
        "function:taxonomy_or_source",
        "global:STOCK_THEME_TAXONOMY",
    ):
        assert no_longer_shared_item not in by_item


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
        "current_date_negative_projection_guard_only"
    )


def test_data_contract_baseline_is_immutable_and_covers_every_family() -> None:
    rows = read_csv("config/daily_model_data_sharing_migrations.csv")
    assert len(rows) == 15
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


def test_data_contract_hash_detects_point_in_time_or_forbidden_use_drift() -> None:
    row = read_csv("config/daily_model_background_data_registry.csv")[0]
    original = data_contract_sha256(row)
    changed_pit = dict(row)
    changed_pit["point_in_time_status"] = "silently_changed"
    changed_forbidden = dict(row)
    changed_forbidden["forbidden_use"] = "silently_changed"
    assert data_contract_sha256(changed_pit) != original
    assert data_contract_sha256(changed_forbidden) != original


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
