from __future__ import annotations

import sys
from pathlib import Path

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
from validate_model_research_artifact_ownership import validate  # noqa: E402
import model_research_artifact_guard as guard_module  # noqa: E402


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


def test_revenue_producer_accepts_only_revenue_artifacts() -> None:
    rules = load_ownership_rules()
    errors = validate_changed_paths(
        "revenue_unreacted_range",
        REVENUE_PRODUCER,
        [
            "output/latest/research_backtest/revenue_unreacted_range_feature_contrast_audit_latest.csv",
            "output/history/research/revenue_unreacted_range_feature_contrast_audit.csv",
            "docs/latest/revenue_unreacted_range_feature_contrast_audit_latest.md",
        ],
        rules,
    )
    assert errors == []


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
