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
    assert len(rows) == 80
    assert by_item["global:MODEL_SCORE_PROFILES"]["semantic_class"] == (
        "contained_legacy_cross_model_semantic"
    )
    assert by_item["function:bottom_volume_attack_like"]["consumer_models"] == (
        "revenue_unreacted_range;tdcc_stealth_accumulation"
    )
    assert by_item["function:text"]["semantic_class"] == "shared_technical"


def test_semantic_baseline_is_immutable_and_pins_all_initial_records() -> None:
    rows = read_csv("config/daily_model_semantic_migrations.csv")
    assert len(rows) == 1
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
    assert by_family["volume_range_breakout_v2_high_position_improvement_audit"][
        "registered_producers"
    ] == "scripts/build_volume_range_breakout_v2_research.py"


def test_data_contract_baseline_is_immutable_and_covers_every_family() -> None:
    rows = read_csv("config/daily_model_data_sharing_migrations.csv")
    assert len(rows) == 1
    baseline = rows[0]
    assert tuple(baseline) == DATA_SHARING_MIGRATION_COLUMNS
    assert data_migration_row_sha256(baseline) == BASELINE_DATA_MIGRATION_ROW_SHA256
    assert len(baseline["changed_data_families"].split(";")) == 25
    assert set(baseline["previous_contract_sha256s"].split(";")) == {"BASELINE"}


def test_data_contract_hash_detects_point_in_time_or_forbidden_use_drift() -> None:
    row = read_csv("config/daily_model_background_data_registry.csv")[0]
    original = data_contract_sha256(row)
    changed_pit = dict(row)
    changed_pit["point_in_time_status"] = "silently_changed"
    changed_forbidden = dict(row)
    changed_forbidden["forbidden_use"] = "silently_changed"
    assert data_contract_sha256(changed_pit) != original
    assert data_contract_sha256(changed_forbidden) != original


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
