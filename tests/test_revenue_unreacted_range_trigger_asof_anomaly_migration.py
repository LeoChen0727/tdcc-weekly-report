from __future__ import annotations

import hashlib
import json
from pathlib import Path
import sys

import pandas as pd
import pytest


ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))

import revenue_unreacted_range_source_first_condition_audit as source_first  # noqa: E402
import revenue_unreacted_range_trigger_asof_anomaly_migration as migration  # noqa: E402
from revenue_unreacted_range_rearmed_operation_grid import (  # noqa: E402
    EPISODE_AGGREGATE_ANOMALY_POLICY_ID,
    TRIGGER_ASOF_ANOMALY_POLICY_ID,
    V2_ARTIFACT_VERSION,
    V3_ARTIFACT_VERSION,
    _source_anomaly,
    _source_anomaly_as_of_trigger,
    artifact_version_for_projection,
)
from revenue_unreacted_range_source_snapshot_projection import (  # noqa: E402
    V1_PROJECTION_VERSION,
    V2_PROJECTION_VERSION,
)
from revenue_unreacted_range_low_mid_falling_candidate_audit import (  # noqa: E402
    V3_ARTIFACT_VERSION as LOW_MID_V3_ARTIFACT_VERSION,
    _candidate_detail_row_sha256,
)
from revenue_unreacted_range_trigger_asof_anomaly_migration import (  # noqa: E402
    _write_append_only,
    canonical_table_semantic_sha256,
    validate_raw_provenance_hash_invariance,
)


SOURCE_FIRST_V3_DETAIL_COLUMN_SCHEMA_SHA256 = (
    "7f92001f3ddfdc57ac812808e6fce9dbbf76b1432dc9478abf07f2f8b8077391"
)


def test_source_first_v3_default_detail_schema_stays_immutable() -> None:
    payload = json.dumps(
        source_first.DETAIL_COLUMNS, separators=(",", ":")
    ).encode("utf-8")
    assert hashlib.sha256(payload).hexdigest() == (
        SOURCE_FIRST_V3_DETAIL_COLUMN_SCHEMA_SHA256
    )
    assert "qualifying_source_revenue_anomaly_candidate_flags" not in (
        source_first.DETAIL_COLUMNS
    )


def test_transient_event_enrichment_is_copy_on_write_and_parallel(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    source = pd.DataFrame(
        [
            {
                "episode_key": "absolute_or_two_month_yoy_ge15|6177|20250517|1",
                "qualifying_source_row_canonical_sha256s": f"{'a' * 64}|{'b' * 64}",
                "qualifying_source_dates": "20250517|20260117",
                "qualifying_trade_dates": "20250519|20260119",
                "qualifying_sequence_indices": "29|196",
                "qualifying_source_revenue_anomaly_candidate_flag": True,
            }
        ]
    )
    revenue = pd.DataFrame(
        [
            {
                "source_row_canonical_sha256": "a" * 64,
                "source_revenue_anomaly_candidate_flag": False,
            },
            {
                "source_row_canonical_sha256": "b" * 64,
                "source_revenue_anomaly_candidate_flag": True,
            },
        ]
    )
    monkeypatch.setattr(source_first, "load_revenue_history", lambda *_a, **_k: revenue)

    enriched = source_first.attach_qualifying_event_anomaly_flags(source)

    assert "qualifying_source_revenue_anomaly_candidate_flags" not in source.columns
    assert enriched.loc[0, "qualifying_source_revenue_anomaly_candidate_flags"] == (
        "False|True"
    )


def test_6177_future_anomaly_does_not_flow_backward_before_availability() -> None:
    episode = pd.Series(
        {
            "episode_key": "absolute_or_two_month_yoy_ge15|6177|20250517|1",
            "qualifying_source_revenue_anomaly_candidate_flag": True,
            "qualifying_trade_dates": "20250519|20251017|20260119",
            "qualifying_source_revenue_anomaly_candidate_flags": (
                "False|False|True"
            ),
            "unresolved_price_path_candidate_flag": False,
        }
    )

    assert _source_anomaly(episode) is True
    assert _source_anomaly_as_of_trigger(episode, "20251204") is False
    assert _source_anomaly_as_of_trigger(episode, "20260119") is True


def test_v3_version_requires_explicit_trigger_asof_policy_and_v2_projection() -> None:
    assert artifact_version_for_projection(V2_PROJECTION_VERSION) == V2_ARTIFACT_VERSION
    assert artifact_version_for_projection(
        V2_PROJECTION_VERSION,
        anomaly_attribution_policy_id=TRIGGER_ASOF_ANOMALY_POLICY_ID,
    ) == V3_ARTIFACT_VERSION
    assert artifact_version_for_projection(
        V1_PROJECTION_VERSION,
        anomaly_attribution_policy_id=EPISODE_AGGREGATE_ANOMALY_POLICY_ID,
    ) != V3_ARTIFACT_VERSION
    with pytest.raises(RuntimeError, match="requires the immutable v2"):
        artifact_version_for_projection(
            V1_PROJECTION_VERSION,
            anomaly_attribution_policy_id=TRIGGER_ASOF_ANOMALY_POLICY_ID,
        )


def test_append_only_writer_accepts_identical_replay_and_rejects_drift(
    tmp_path: Path,
) -> None:
    target = tmp_path / "v3.csv"
    _write_append_only(target, b"immutable-v3\n")
    _write_append_only(target, b"immutable-v3\n")
    with pytest.raises(RuntimeError, match="append-only v3 artifact"):
        _write_append_only(target, b"changed\n")
    assert target.read_bytes() == b"immutable-v3\n"


def test_v3_canonical_hashes_ignore_raw_only_provenance_mutation() -> None:
    before = {
        "generated_at": "2026-08-29 00:00:00 Asia/Taipei",
        "artifact_version": LOW_MID_V3_ARTIFACT_VERSION,
        "operation_key": "operation-1",
        "realized_return_pct": "5.274",
        "monthly_revenue_history_blob_sha256": "a" * 64,
    }
    after = {
        **before,
        "generated_at": "2026-08-29 00:01:00 Asia/Taipei",
        "monthly_revenue_history_blob_sha256": "b" * 64,
    }
    assert _candidate_detail_row_sha256(
        before, artifact_version=LOW_MID_V3_ARTIFACT_VERSION
    ) == _candidate_detail_row_sha256(
        after, artifact_version=LOW_MID_V3_ARTIFACT_VERSION
    )

    before_table = pd.DataFrame(
        [{**before, "raw_source_file": "raw-a.csv", "raw_source_sha256": "c" * 64}]
    )
    after_table = pd.DataFrame(
        [{**after, "raw_source_file": "raw-b.csv", "raw_source_sha256": "d" * 64}]
    )
    assert canonical_table_semantic_sha256(
        before_table
    ) == canonical_table_semantic_sha256(after_table)

    changed_business = after_table.copy()
    changed_business.loc[0, "realized_return_pct"] = "5.275"
    assert canonical_table_semantic_sha256(
        before_table
    ) != canonical_table_semantic_sha256(changed_business)


def test_full_v3_promotion_hash_envelope_provenance_invariance() -> None:
    validate_raw_provenance_hash_invariance()


def test_full_manifest_validator_treats_crlf_byte_drift_as_diagnostic(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    validation_path = tmp_path / "validation.csv"
    candidates_path = tmp_path / "candidates.csv"
    specs = {
        "validation_summary": migration.ArtifactSpec(
            "validation",
            "v3",
            validation_path,
        ),
        "candidate_rows": migration.ArtifactSpec(
            "candidates",
            "v3",
            candidates_path,
        ),
    }
    manifest_path = tmp_path / "manifest.csv"
    monkeypatch.setattr(migration, "ROOT", tmp_path)
    monkeypatch.setattr(migration, "ARTIFACT_SPECS", specs)
    monkeypatch.setattr(migration, "MANIFEST_PATH", manifest_path)

    frames = {
        "validation_summary": pd.DataFrame(
            [
                {
                    "selected_53_business_projection_unchanged": True,
                    "primary_metrics_unchanged": True,
                    "raw_only_mutation_canonical_hashes_unchanged": True,
                    "business_pit_mutation_canonical_hashes_changed": True,
                    "v1_v2_artifacts_written": False,
                }
            ]
        ),
        "candidate_rows": pd.DataFrame(
            [
                {
                    "stock_id": "6177" if index == 0 else str(7000 + index),
                    "entry_date": "20251208" if index == 0 else f"202501{index + 1:02d}",
                    "after_source_anomaly_candidate_flag": False,
                }
                for index in range(9)
            ]
        ),
    }
    manifest_rows = []
    for key, spec in specs.items():
        frame = frames[key]
        payload = migration._csv_bytes(frame)
        spec.path.write_bytes(payload)
        manifest_rows.append(
            {
                "artifact_key": key,
                "path": spec.path.relative_to(tmp_path).as_posix(),
                "row_count": len(frame),
                "byte_sha256": migration._sha256(payload),
                "canonical_semantic_sha256": canonical_table_semantic_sha256(frame),
            }
        )
    manifest_path.write_bytes(migration._csv_bytes(pd.DataFrame(manifest_rows)))

    candidates_path.write_bytes(
        candidates_path.read_bytes().replace(b"\n", b"\r\n")
    )
    assert migration.validate_committed_v3_chain() == []
