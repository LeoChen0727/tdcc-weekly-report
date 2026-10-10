"""Fail-closed tests for the reclaim matched-feature research contract."""
from __future__ import annotations

import ast
import copy
from contextlib import nullcontext
from pathlib import Path
import sys

import pandas as pd
import pytest


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import build_pullback_short_reclaim_matched_feature_research as producer
import validate_pullback_short_reclaim_matched_feature_research as validator


@pytest.fixture(scope="module")
def source_payloads():
    return validator.load_sources(ROOT)


@pytest.fixture(scope="module")
def matched_bundle(source_payloads):
    """Build the new artifacts only in memory; never call producer.main/write_bundle."""
    def reader(root, commit, path, expected_sha256):
        assert commit == validator.SOURCE_COMMIT
        keys = [key for key, spec in validator.SOURCE_ARTIFACTS.items() if spec["path"] == path]
        assert len(keys) == 1
        payload = source_payloads[keys[0]]
        assert validator._sha(payload) == expected_sha256
        return payload

    with pytest.MonkeyPatch.context() as patch:
        patch.setattr(producer, "read_git_blob", reader)
        return producer.build_bundle(ROOT)


@pytest.fixture(scope="module")
def independent_references(source_payloads):
    canonical, source_manifest = validator.verify_sources(source_payloads)
    metrics = validator.expected_metrics(canonical)
    features = validator.expected_features(canonical)
    audit = validator.expected_audit(canonical)
    manifest = validator.expected_manifest(source_manifest, canonical, metrics, features, audit)
    return canonical, metrics, features, audit, manifest


def test_matched_bundle_independently_validates(source_payloads, matched_bundle):
    assert validator.validate_bundle(ROOT, *matched_bundle, sources=source_payloads) == {
        "source_rows": 3020,
        "unique_signal_events": 2992,
        "source_duplicate_groups": 28,
        "union_review_candidate_events": 8,
        "metrics_rows": 15,
        "feature_rows": 1776,
        "audit_rows": 98,
        "first_publication_pit_proven": False,
        "formal_use_allowed": False,
    }


def test_exact_schema_and_column_order(matched_bundle):
    metrics, features, audit = matched_bundle[:3]
    assert len(validator.METRICS_COLUMNS) == 38
    assert len(validator.FEATURES_COLUMNS) == 34
    assert len(validator.AUDIT_COLUMNS) == 57
    assert tuple(metrics.columns) == validator.METRICS_COLUMNS
    assert tuple(features.columns) == validator.FEATURES_COLUMNS
    assert tuple(audit.columns) == validator.AUDIT_COLUMNS
    assert validator.METRICS_COLUMNS[6] == "aggregation_basis"
    assert validator.METRICS_COLUMNS[5] == "return_cost_basis"
    assert validator.METRICS_COLUMNS[32] == "first_publication_pit_status"
    assert validator.FEATURES_COLUMNS[24:29] == (
        "positive_difference_count",
        "zero_difference_count",
        "negative_difference_count",
        "positive_difference_rate_pct",
        "negative_difference_rate_pct",
    )
    index = validator.AUDIT_COLUMNS.index("candidate_exclusion_sensitivity_delta_pct")
    assert validator.AUDIT_COLUMNS[index + 1] == "review_candidate_disposition"


def test_frozen_source_hash_and_manifest_tamper_rejected(source_payloads):
    changed = dict(source_payloads)
    changed["detail"] += b"\n"
    with pytest.raises(ValueError, match="immutable source SHA"):
        validator.verify_sources(changed)
    changed = dict(source_payloads)
    changed["manifest"] += b"\n"
    with pytest.raises(ValueError, match="immutable source SHA"):
        validator.verify_sources(changed)


def test_shallow_checkout_filesystem_fallback_is_content_sha_only(tmp_path, source_payloads):
    for key, spec in validator.SOURCE_ARTIFACTS.items():
        target = tmp_path / spec["path"]
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(source_payloads[key])
    loaded = validator.load_sources(tmp_path)
    assert {key: validator._sha(value) for key, value in loaded.items()} == {
        key: spec["raw_sha256"] for key, spec in validator.SOURCE_ARTIFACTS.items()
    }
    validator.verify_sources(loaded)
    detail_path = tmp_path / validator.SOURCE_ARTIFACTS["detail"]["path"]
    detail_path.write_bytes(source_payloads["detail"] + b"\n")
    with pytest.raises(ValueError, match="filesystem fallback source raw SHA"):
        validator.load_sources(tmp_path)


def test_exact_eight_event_union_and_dispositions(source_payloads, independent_references):
    canonical = independent_references[0]
    union_ids = validator._review_candidate_ids(canonical)
    assert len(union_ids) == 8
    for horizon in validator.HORIZONS:
        prefix = f"d{horizon}"
        candidate = canonical[prefix + "_comparison_anomaly_candidate"].eq("True")
        assert set(canonical.loc[candidate, prefix + "_comparison_anomaly_disposition"]) == {
            "unresolved_anomaly_candidate"
        }
        assert set(canonical.loc[~candidate, prefix + "_comparison_anomaly_disposition"]) == {
            "not_flagged_by_this_review"
        }

    detail = validator._csv(source_payloads["detail"])
    event_id = sorted(union_ids)[0]
    row_index = detail.index[
        detail["primary_metric_included"].eq("True") & detail["signal_event_id"].eq(event_id)
    ][0]
    for horizon in validator.HORIZONS:
        detail.at[row_index, f"d{horizon}_comparison_anomaly_candidate"] = "False"
        detail.at[row_index, f"d{horizon}_comparison_anomaly_disposition"] = "not_flagged_by_this_review"
    with pytest.raises(ValueError, match="candidate disposition|union must remain exactly 8"):
        validator._validate_source_frame(detail)


def test_source_candidate_disposition_change_rejected(source_payloads):
    detail = validator._csv(source_payloads["detail"])
    mask = detail["primary_metric_included"].eq("True") & detail[
        "d5_comparison_anomaly_candidate"
    ].eq("True")
    detail.at[detail.index[mask][0], "d5_comparison_anomaly_disposition"] = "verified_real_extreme"
    with pytest.raises(ValueError, match="candidate disposition"):
        validator._validate_source_frame(detail)


@pytest.mark.parametrize(
    "field,value",
    [
        ("signal_count", 0),
        ("average_return_pct", "999"),
        ("return_cost_basis", "after_costs"),
        ("union_review_candidate_event_count", 7),
        ("first_publication_pit_status", "proven"),
        ("formal_use_allowed", "True"),
    ],
)
def test_metric_tamper_rejected(matched_bundle, independent_references, field, value):
    changed = matched_bundle[0].copy(deep=True)
    changed.at[0, field] = value
    with pytest.raises(ValueError, match="metrics independent recomputation"):
        validator._verify_table(changed, independent_references[1], "metrics")


@pytest.mark.parametrize(
    "field,value",
    [
        ("q1", "999"),
        ("paired_status", "invented"),
        ("positive_difference_count", 999),
        ("negative_difference_rate_pct", "100"),
        ("feature_scale_note", "comparable_threshold"),
        ("promotion_evidence_allowed", "True"),
    ],
)
def test_feature_tamper_rejected(matched_bundle, independent_references, field, value):
    changed = matched_bundle[1].copy(deep=True)
    changed.at[0, field] = value
    with pytest.raises(ValueError, match="features independent recomputation"):
        validator._verify_table(changed, independent_references[2], "features")


@pytest.mark.parametrize(
    "field,value",
    [
        ("source_row_count", 2992),
        ("source_duplicate_extra_row_count", 0),
        ("overlap_not_assessed_event_count", 0),
        ("boundary_touch_pair_count", 999),
        ("review_candidate_average_point_contribution_pct", "0"),
        ("review_candidate_disposition", "verified_real_extreme"),
        ("overlap_interpretation", "actual_position_conflict"),
        ("formal_use_allowed", "True"),
    ],
)
def test_audit_tamper_rejected(matched_bundle, independent_references, field, value):
    audit = matched_bundle[2].copy(deep=True)
    eligible = audit.index[audit[field].ne("")]
    index = eligible[0] if len(eligible) else audit.index[0]
    audit.at[index, field] = value
    with pytest.raises(ValueError, match="audit independent recomputation"):
        validator._verify_table(audit, independent_references[3], "audit")


def test_row_order_and_exhaustiveness_are_contractual(matched_bundle, independent_references):
    for actual, expected, label in zip(
        matched_bundle[:3], independent_references[1:4], ("metrics", "features", "audit")
    ):
        with pytest.raises(ValueError, match="exhaustive row population"):
            validator._verify_table(actual.iloc[:-1], expected, label)
        reversed_rows = actual.iloc[::-1].reset_index(drop=True)
        with pytest.raises(ValueError, match="independent recomputation"):
            validator._verify_table(reversed_rows, expected, label)


def test_missing_paired_side_keeps_difference_blank():
    high_only = pd.DataFrame({"feature_price_pullback_rsi14": [60, 55]})
    row, delta = validator._date_contrast_row(
        high_only,
        pd.Series([12.0, 5.0]),
        period="202607",
        signal_date="20260703",
        horizon=5,
        feature_id="rsi14",
    )
    assert delta is None
    assert row["paired_status"] == "missing_loss_values"
    assert row["high_minus_loss_median"] == ""
    assert row["positive_difference_rate_pct"] == ""
    assert row["negative_difference_rate_pct"] == ""

    loss_only = pd.DataFrame({"feature_price_pullback_rsi14": [40, 45]})
    row, delta = validator._date_contrast_row(
        loss_only,
        pd.Series([-1.0, 2.0]),
        period="202607",
        signal_date="20260703",
        horizon=5,
        feature_id="rsi14",
    )
    assert delta is None
    assert row["paired_status"] == "missing_high_values"
    assert row["high_minus_loss_median"] == ""


def test_audit_identity_overlap_and_union_contract(matched_bundle, independent_references):
    canonical, _, _, expected, _ = independent_references
    audit = matched_bundle[2]
    identity = audit[audit["audit_type"].eq("source_identity_summary")].iloc[0]
    assert identity["source_row_count"] == 3020
    assert identity["canonical_signal_event_count"] == 2992
    assert identity["source_duplicate_group_count"] == 28
    assert identity["source_duplicate_extra_row_count"] == 28
    assert identity["canonical_same_stock_signal_date_group_count"] == 0
    assert identity["canonical_same_stock_signal_date_cross_report_line_group_count"] == 0
    duplicates = audit[audit["audit_type"].eq("source_duplicate_identity")]
    assert len(duplicates) == 28
    assert duplicates["signal_event_id"].nunique() == 28

    overlap = audit[audit["audit_type"].eq("period_stock_interval_overlap")]
    assert set(overlap["overlap_interval_basis"]) == {
        "mature_parseable_entry_to_fixed_horizon_exit_closed_interval"
    }
    assert set(overlap["overlap_interpretation"]) == {
        "conservative_inclusive_date_intersection_not_actual_position_conflict"
    }
    assert (pd.to_numeric(overlap["overlap_eligible_event_count"]) == pd.to_numeric(overlap["mature_count"])).all()
    assert (pd.to_numeric(overlap["overlap_not_assessed_event_count"]) ==
            pd.to_numeric(overlap["signal_count"]) - pd.to_numeric(overlap["mature_count"])).all()

    events = audit[audit["audit_type"].eq("review_candidate_event")]
    assert len(events) == 24 and events["signal_event_id"].nunique() == 8
    by_id = canonical.set_index("signal_event_id")
    for _, event in events.iterrows():
        horizon = int(event["horizon"])
        source = by_id.loc[event["signal_event_id"]]
        candidate = source[f"d{horizon}_comparison_anomaly_candidate"] == "True"
        expected_disposition = (
            "unresolved_anomaly_candidate"
            if candidate
            else "union_candidate_triggered_at_another_horizon"
        )
        assert event["review_candidate_disposition"] == expected_disposition
    validator._verify_table(audit, expected, "audit")


@pytest.mark.parametrize(
    "table_index,field",
    [
        (0, "primary_retains_unresolved_candidates"),
        (0, "sensitivity_is_corrected_primary"),
        (0, "first_publication_pit_proven"),
        (0, "total_return_complete"),
        (0, "trade_eligible"),
        (1, "first_publication_pit_proven"),
        (2, "promotion_evidence_allowed"),
    ],
)
def test_boundary_flags_fail_closed(matched_bundle, independent_references, table_index, field):
    changed = matched_bundle[table_index].copy(deep=True)
    expected = independent_references[table_index + 1]
    changed.at[0, field] = "False" if changed.at[0, field] == "True" else "True"
    with pytest.raises(ValueError, match="independent recomputation"):
        validator._verify_table(changed, expected, ("metrics", "features", "audit")[table_index])


@pytest.mark.parametrize(
    "key,value",
    [
        ("source_commit", "0" * 40),
        ("union_review_candidate_event_count", 7),
        ("first_publication_pit_proven", True),
        ("first_publication_pit_status", "proven"),
        ("non_overlapping_trades_proven", True),
        ("formal_use_allowed", True),
    ],
)
def test_manifest_tamper_rejected(source_payloads, matched_bundle, monkeypatch, key, value):
    manifest = copy.deepcopy(matched_bundle[3])
    manifest[key] = value
    monkeypatch.setattr(validator, "expected_metrics", lambda canonical: matched_bundle[0])
    monkeypatch.setattr(validator, "expected_features", lambda canonical: matched_bundle[1])
    monkeypatch.setattr(validator, "expected_audit", lambda canonical: matched_bundle[2])
    with pytest.raises(ValueError, match="manifest immutable"):
        validator.validate_bundle(ROOT, *matched_bundle[:3], manifest, sources=source_payloads)


def test_validator_has_no_producer_or_business_semantic_import():
    tree = ast.parse(Path(validator.__file__).read_text(encoding="utf-8"))
    imports = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            imports.extend(alias.name for alias in node.names)
        elif isinstance(node, ast.ImportFrom):
            imports.append(node.module or "")
        elif isinstance(node, ast.Call) and isinstance(node.func, ast.Name):
            assert node.func.id not in {"eval", "exec", "__import__"}
    assert all(
        not module.startswith(
            ("build_", "scripts", "model_", "price_pullback", "daily_model", "tracking_utils")
        )
        for module in imports
    )


def test_actual_published_artifacts_validate_when_present():
    present = [(ROOT / path).is_file() for path in validator.OUTPUTS.values()]
    assert len(set(present)) == 1, "partial published matched-feature bundle must fail closed"
    if present[0]:
        result = validator.validate(ROOT)
        assert result["unique_signal_events"] == 2992
        assert result["union_review_candidate_events"] == 8


def test_model_owned_guard_rejects_unregistered_outputs(tmp_path, monkeypatch):
    monkeypatch.setattr(producer, "load_ownership_rules", lambda path: ["synthetic-rule"])

    def reject(owner_id, producer_path, output_paths, rules):
        assert owner_id == producer.OWNER_ID
        assert producer_path == producer.PRODUCER
        assert output_paths == list(producer.OUTPUTS.values())
        assert rules == ["synthetic-rule"]
        return ["synthetic-unregistered-output"]

    monkeypatch.setattr(producer, "validate_changed_paths", reject)
    with pytest.raises(RuntimeError, match="unregistered matched-feature outputs"):
        with producer.model_owned_artifact_guard(tmp_path):
            pytest.fail("ownership rejection must occur before entering the write guard")


def test_model_owned_guard_rejects_foreign_model_write(tmp_path, monkeypatch):
    monkeypatch.setattr(producer, "load_ownership_rules", lambda path: [])
    monkeypatch.setattr(producer, "validate_changed_paths", lambda *args: [])
    monkeypatch.setattr(producer, "_dirty_snapshot", lambda root: {"before": "stable"})
    monkeypatch.setattr(
        producer,
        "changed_during_run",
        lambda root, before: ["output/research/another_model/foreign.csv"],
    )
    monkeypatch.setattr(producer, "protected_snapshot", lambda root: {"protected": "stable"})
    monkeypatch.setattr(
        producer,
        "_git",
        lambda root, *args: b"stable-index" if args[0] == "ls-files" else b"stable-head",
    )
    with pytest.raises(RuntimeError, match="changed protected/out-of-scope paths"):
        with producer.model_owned_artifact_guard(tmp_path):
            pass


@pytest.mark.parametrize("drift", ["protected", "index", "head"])
def test_model_owned_guard_rejects_protected_index_or_head_drift(
    tmp_path, monkeypatch, drift
):
    monkeypatch.setattr(producer, "load_ownership_rules", lambda path: [])
    monkeypatch.setattr(producer, "validate_changed_paths", lambda *args: [])
    monkeypatch.setattr(producer, "_dirty_snapshot", lambda root: {"before": "stable"})
    monkeypatch.setattr(producer, "changed_during_run", lambda root, before: [])

    protected_calls = 0

    def protected_snapshot(root):
        nonlocal protected_calls
        protected_calls += 1
        if drift == "protected" and protected_calls == 2:
            return {"protected": "after"}
        return {"protected": "before"}

    git_calls = {"ls-files": 0, "rev-parse": 0}

    def git(root, *args):
        command = args[0]
        git_calls[command] += 1
        if drift == "index" and command == "ls-files" and git_calls[command] == 2:
            return b"index-after"
        if drift == "head" and command == "rev-parse" and git_calls[command] == 2:
            return b"head-after"
        return b"index-before" if command == "ls-files" else b"head-before"

    monkeypatch.setattr(producer, "protected_snapshot", protected_snapshot)
    monkeypatch.setattr(producer, "_git", git)
    with pytest.raises(RuntimeError, match="changed protected/out-of-scope paths"):
        with producer.model_owned_artifact_guard(tmp_path):
            pass


def _synthetic_write_bundle():
    metrics = pd.DataFrame([{"synthetic": "metrics"}])
    features = pd.DataFrame([{"synthetic": "features"}])
    audit = pd.DataFrame([{"synthetic": "audit"}])
    csv_payloads = {
        producer.OUTPUTS["metrics"]: producer.csv_bytes(metrics),
        producer.OUTPUTS["features"]: producer.csv_bytes(features),
        producer.OUTPUTS["audit"]: producer.csv_bytes(audit),
    }
    manifest = {
        "output_sha256": {
            path: producer.sha256(payload) for path, payload in csv_payloads.items()
        }
    }
    payloads = {
        **csv_payloads,
        producer.OUTPUTS["manifest"]: producer.canonical_json(manifest) + b"\n",
    }
    return (metrics, features, audit, manifest), payloads


def test_write_bundle_different_existing_bytes_fails_without_overwrite(tmp_path, monkeypatch):
    bundle, payloads = _synthetic_write_bundle()
    monkeypatch.setattr(producer, "model_owned_artifact_guard", lambda root: nullcontext())
    conflicting = tmp_path / producer.OUTPUTS["audit"]
    conflicting.parent.mkdir(parents=True)
    conflicting.write_bytes(b"pre-existing-different-bytes\n")

    with pytest.raises(RuntimeError, match="immutable matched-feature output already differs"):
        producer.write_bundle(bundle, tmp_path)

    assert conflicting.read_bytes() == b"pre-existing-different-bytes\n"
    for relative in payloads:
        if relative != producer.OUTPUTS["audit"]:
            assert not (tmp_path / relative).exists()


def test_write_bundle_same_existing_bytes_are_not_rewritten(tmp_path, monkeypatch):
    bundle, payloads = _synthetic_write_bundle()
    monkeypatch.setattr(producer, "model_owned_artifact_guard", lambda root: nullcontext())
    targets = set()
    for relative, payload in payloads.items():
        target = tmp_path / relative
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(payload)
        targets.add(target.resolve())

    original_open = Path.open

    def reject_target_writes(path, mode="r", *args, **kwargs):
        if path.resolve() in targets and any(flag in mode for flag in "wax+"):
            raise AssertionError("same-byte immutable artifact must not be opened for writing")
        return original_open(path, mode, *args, **kwargs)

    monkeypatch.setattr(Path, "open", reject_target_writes)
    producer.write_bundle(bundle, tmp_path)
    assert {relative: (tmp_path / relative).read_bytes() for relative in payloads} == payloads
