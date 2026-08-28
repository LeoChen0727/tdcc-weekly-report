from __future__ import annotations

from contextlib import contextmanager
import csv
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
    MIGRATION_COLUMNS,
    validate,
    validate_ownership_migrations,
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


def test_model_research_artifact_ownership_registry_passes() -> None:
    assert validate() == []


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
        and rule.producer
        == "scripts/sync_revenue_unreacted_range_operation_readiness.py"
        and rule.change_policy == "formal_sync_only"
        and rule.formal_evidence_status == "formal_evidence_pinned"
    }
    assert readiness_rules == EXPECTED_READINESS_RULES
    assert validate_ownership_migrations() == []


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
