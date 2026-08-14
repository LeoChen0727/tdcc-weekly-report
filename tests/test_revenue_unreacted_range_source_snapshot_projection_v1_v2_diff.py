from __future__ import annotations

from pathlib import Path
import sys

import pandas as pd


ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))

import revenue_unreacted_range_source_snapshot_projection_v1_v2_diff as producer  # noqa: E402
import validate_revenue_unreacted_range_source_snapshot_projection_v1_v2_diff as validator  # noqa: E402


def _detail_row(
    episode_key: str,
    *,
    stock_id: str,
    hashes: str,
    generated_at: str = "2026-08-14 00:00:00 Asia/Taipei",
) -> dict[str, str]:
    return {
        "generated_at": generated_at,
        "monthly_revenue_history_blob_sha256": "1" * 64,
        "cross_market_resolution_registry_canonical_sha256": "2" * 64,
        "condition_variant_id": "absolute_or_two_month_yoy_ge15",
        "stock_id": stock_id,
        "episode_key": episode_key,
        "episode_start_source_date": "20250917",
        "episode_start_source_row_canonical_sha256": hashes.split("|")[0],
        "qualifying_source_row_canonical_sha256s": hashes,
    }


def _inputs(monkeypatch):
    v1_detail = pd.DataFrame(
        [
            _detail_row("variant|1111|20250917|1", stock_id="1111", hashes="a" * 64),
            _detail_row("variant|2222|20250917|1", stock_id="2222", hashes="b" * 64),
        ]
    )
    v2_detail = pd.DataFrame(
        [
            _detail_row("variant|1111|20250917|1", stock_id="1111", hashes="a" * 64),
            _detail_row("variant|3333|20250917|1", stock_id="3333", hashes="c" * 64),
        ]
    )
    v1_sha = validator._projected_source_detail_sha256(v1_detail)
    v2_sha = validator._projected_source_detail_sha256(v2_detail)
    monkeypatch.setattr(producer, "V1_DETAIL_SEMANTIC_SHA256", v1_sha)
    monkeypatch.setattr(validator, "V1_DETAIL_SEMANTIC_SHA256", v1_sha)
    v1_manifest = pd.DataFrame(
        [{"artifact_version": producer.V1_ARTIFACT_VERSION}]
    )
    v2_manifest = pd.DataFrame(
        [
            {
                "artifact_version": producer.V2_ARTIFACT_VERSION,
                "projected_episode_semantic_sha256": v2_sha,
            }
        ]
    )
    return (
        v1_manifest,
        v1_detail,
        v2_manifest,
        v2_detail,
    )


def test_diff_exact_episode_absence_and_v2_only_source_rows(monkeypatch) -> None:
    inputs = _inputs(monkeypatch)
    frame = producer.build_projection_v1_v2_diff(
        *inputs,
        generated_at="2026-08-14 00:00:00 Asia/Taipei",
    )
    assert validator.validate_frames(*inputs, frame) == []
    episodes = frame.loc[frame["record_type"].eq("episode_relation")]
    assert set(episodes["relation_status"]) == {
        "exact_episode_key_successor",
        "absent_after_repair",
        "v2_only_successor",
    }
    assert set(frame["promotion_gate_status"]) == {
        "not_promotion_evidence_source_diff_only"
    }


def test_diff_validator_rejects_forged_successor_and_row_set(monkeypatch) -> None:
    inputs = _inputs(monkeypatch)
    frame = producer.build_projection_v1_v2_diff(*inputs)
    forged = frame.copy()
    index = forged.index[forged["relation_status"].eq("exact_episode_key_successor")][0]
    forged.loc[index, "corrected_episode_key"] = "fabricated"
    errors = validator.validate_frames(*inputs, forged)
    assert "v1/v2 diff relation_row_sha256 mismatch" in errors
    assert "v1/v2 diff episode successor mapping mismatch" in errors


def test_diff_preserves_equal_overlap_tie_as_non_final_ambiguity(monkeypatch) -> None:
    v1_manifest, _v1_detail, v2_manifest, _v2_detail = _inputs(monkeypatch)
    shared_a = "a" * 64
    shared_b = "b" * 64
    v1_detail = pd.DataFrame(
        [
            _detail_row(
                "variant|4444|20250917|1",
                stock_id="4444",
                hashes=f"{shared_a}|{shared_b}",
            )
        ]
    )
    v2_detail = pd.DataFrame(
        [
            _detail_row(
                "variant|4444|20250918|1",
                stock_id="4444",
                hashes=shared_a,
            ),
            _detail_row(
                "variant|4444|20250919|1",
                stock_id="4444",
                hashes=shared_b,
            ),
        ]
    )
    v1_sha = validator._projected_source_detail_sha256(v1_detail)
    v2_sha = validator._projected_source_detail_sha256(v2_detail)
    monkeypatch.setattr(producer, "V1_DETAIL_SEMANTIC_SHA256", v1_sha)
    monkeypatch.setattr(validator, "V1_DETAIL_SEMANTIC_SHA256", v1_sha)
    v2_manifest.loc[0, "projected_episode_semantic_sha256"] = v2_sha

    frame = producer.build_projection_v1_v2_diff(
        v1_manifest,
        v1_detail,
        v2_manifest,
        v2_detail,
    )
    assert validator.validate_frames(
        v1_manifest,
        v1_detail,
        v2_manifest,
        v2_detail,
        frame,
    ) == []
    original = frame.loc[frame["original_episode_key"].ne("")].iloc[0]
    assert original["relation_status"] == "ambiguous_qualifying_source_overlap"
    assert original["corrected_episode_key"] == ""
    assert (
        original["absence_reason"]
        == "ambiguous_equal_maximum_qualifying_source_overlap"
    )


def test_diff_writer_emits_three_byte_identical_mirrors(monkeypatch, tmp_path: Path) -> None:
    inputs = _inputs(monkeypatch)
    frame = producer.build_projection_v1_v2_diff(*inputs)
    history = tmp_path / "history.csv"
    latest = tmp_path / "latest.csv"
    docs = tmp_path / "docs.csv"
    producer.write_projection_v1_v2_diff(
        frame,
        history_path=history,
        latest_path=latest,
        docs_path=docs,
    )
    assert history.read_bytes() == latest.read_bytes() == docs.read_bytes()


def test_diff_independent_validator_does_not_import_diff_producer() -> None:
    source = Path(validator.__file__).read_text(encoding="utf-8")
    assert "import revenue_unreacted_range_source_snapshot_projection_v1_v2_diff" not in source
    assert "from revenue_unreacted_range_source_snapshot_projection_v1_v2_diff" not in source
