from __future__ import annotations

from pathlib import Path
import sys

import pandas as pd
import pytest


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
    variant_id: str = "absolute_or_two_month_yoy_ge15",
    episode_number: int = 1,
    start_date: str = "20250917",
    end_date: str = "20260713",
    episode_status: str = "right_censored_before_active_horizon",
    generated_at: str = "2026-08-14 00:00:00 Asia/Taipei",
) -> dict[str, str]:
    return {
        "generated_at": generated_at,
        "monthly_revenue_history_blob_sha256": "1" * 64,
        "cross_market_resolution_registry_canonical_sha256": "2" * 64,
        "condition_variant_id": variant_id,
        "stock_id": stock_id,
        "episode_key": episode_key,
        "episode_number": str(episode_number),
        "episode_start_source_date": start_date,
        "episode_start_source_row_canonical_sha256": hashes.split("|")[0],
        "qualifying_source_row_canonical_sha256s": hashes,
        "episode_end_date": end_date,
        "episode_status": episode_status,
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


def test_diff_emits_observed_3059_edge_level_one_to_many_split_component(
    monkeypatch,
) -> None:
    v1_manifest, _v1_detail, v2_manifest, _v2_detail = _inputs(monkeypatch)
    shared_a = "a" * 64
    shared_b = "b" * 64
    v1_detail = pd.DataFrame(
        [
            _detail_row(
                "absolute_or_latest_yoy_ge15|3059|20250617|1",
                stock_id="3059",
                hashes=f"{shared_a}|{shared_b}",
                variant_id="absolute_or_latest_yoy_ge15",
                start_date="20250617",
            )
        ]
    )
    v2_detail = pd.DataFrame(
        [
            _detail_row(
                "absolute_or_latest_yoy_ge15|3059|20250617|1",
                stock_id="3059",
                hashes=shared_a,
                variant_id="absolute_or_latest_yoy_ge15",
                start_date="20250617",
                end_date="20250816",
            ),
            _detail_row(
                "absolute_or_latest_yoy_ge15|3059|20250817|2",
                stock_id="3059",
                hashes=shared_b,
                variant_id="absolute_or_latest_yoy_ge15",
                episode_number=2,
                start_date="20250817",
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
    relations = frame.loc[frame["original_episode_key"].ne("")]
    assert len(relations) == 2
    assert set(relations["relation_status"]) == {"one_to_many_split_successor"}
    assert set(relations["relation_component_type"]) == {"one_v1_to_many_v2"}
    assert set(relations["relation_cardinality"]) == {"1:2"}
    assert set(relations["relation_component_edge_count"].astype(str)) == {"2"}
    assert set(relations["mapping_role"]) == {"exact_key_anchor", "split_member"}


def test_diff_emits_strict_many_to_one_merge_component(monkeypatch) -> None:
    v1_manifest, _v1_detail, v2_manifest, _v2_detail = _inputs(monkeypatch)
    a, b, c, added = (character * 64 for character in "abcd")
    v1_detail = pd.DataFrame(
        [
            _detail_row(
                "absolute_or_two_month_yoy_ge15|2451|20250517|1",
                stock_id="2451",
                hashes=f"{a}|{b}",
                start_date="20250517",
                end_date="20251014",
            ),
            _detail_row(
                "absolute_or_two_month_yoy_ge15|2451|20251217|2",
                stock_id="2451",
                hashes=c,
                episode_number=2,
                start_date="20251217",
            ),
        ]
    )
    v2_detail = pd.DataFrame(
        [
            _detail_row(
                "absolute_or_two_month_yoy_ge15|2451|20250517|1",
                stock_id="2451",
                hashes=f"{a}|{b}|{c}|{added}",
                start_date="20250517",
            )
        ]
    )
    v1_sha = validator._projected_source_detail_sha256(v1_detail)
    v2_sha = validator._projected_source_detail_sha256(v2_detail)
    monkeypatch.setattr(producer, "V1_DETAIL_SEMANTIC_SHA256", v1_sha)
    monkeypatch.setattr(validator, "V1_DETAIL_SEMANTIC_SHA256", v1_sha)
    v2_manifest.loc[0, "projected_episode_semantic_sha256"] = v2_sha
    frame = producer.build_projection_v1_v2_diff(
        v1_manifest, v1_detail, v2_manifest, v2_detail,
        generated_at="2026-08-14 00:00:00 Asia/Taipei",
    )
    assert validator.validate_frames(
        v1_manifest, v1_detail, v2_manifest, v2_detail, frame
    ) == []
    assert len(frame) == 2
    assert set(frame["relation_status"]) == {"many_to_one_merged_successor"}
    assert set(frame["relation_cardinality"]) == {"2:1"}
    assert set(frame["mapping_role"]) == {"exact_key_anchor", "merge_member"}
    assert set(frame["component_token_set_relation"]) == {
        "original_token_union_strict_subset_of_corrected"
    }

    shuffled = producer.build_projection_v1_v2_diff(
        v1_manifest,
        v1_detail.sample(frac=1, random_state=7).reset_index(drop=True),
        v2_manifest,
        v2_detail,
        generated_at="2026-08-14 00:00:00 Asia/Taipei",
    )
    pd.testing.assert_frame_equal(frame, shuffled)


def test_diff_rejects_merge_partial_containment_and_nonconsecutive_episodes(
    monkeypatch,
) -> None:
    v1_manifest, _v1_detail, v2_manifest, _v2_detail = _inputs(monkeypatch)
    a, b, c = (character * 64 for character in "abc")
    v1_detail = pd.DataFrame(
        [
            _detail_row(
                "variant|3665|20250717|2",
                stock_id="3665",
                hashes=a,
                episode_number=2,
                start_date="20250717",
                end_date="20251016",
            ),
            _detail_row(
                "variant|3665|20251217|4",
                stock_id="3665",
                hashes=f"{b}|{c}",
                episode_number=4,
                start_date="20251217",
            ),
        ]
    )
    v2_detail = pd.DataFrame(
        [
            _detail_row(
                "variant|3665|20250717|2",
                stock_id="3665",
                hashes=f"{a}|{b}",
                episode_number=2,
                start_date="20250717",
            )
        ]
    )
    monkeypatch.setattr(
        producer, "V1_DETAIL_SEMANTIC_SHA256", validator._projected_source_detail_sha256(v1_detail)
    )
    v2_manifest.loc[0, "projected_episode_semantic_sha256"] = (
        validator._projected_source_detail_sha256(v2_detail)
    )
    with pytest.raises(RuntimeError, match="episode numbers are not consecutive"):
        producer.build_projection_v1_v2_diff(
            v1_manifest, v1_detail, v2_manifest, v2_detail
        )

    v1_detail.loc[1, "episode_number"] = "3"
    with pytest.raises(RuntimeError, match="token set is not contained"):
        producer.build_projection_v1_v2_diff(
            v1_manifest, v1_detail, v2_manifest, v2_detail
        )


def test_diff_rejects_many_to_many_and_same_version_duplicate_tokens(
    monkeypatch,
) -> None:
    v1_manifest, _v1_detail, v2_manifest, _v2_detail = _inputs(monkeypatch)
    a, b, c, d = (character * 64 for character in "abcd")
    v1_detail = pd.DataFrame(
        [
            _detail_row("v|3002|20250117|1", stock_id="3002", hashes=f"{a}|{b}", start_date="20250117", end_date="20250316"),
            _detail_row("v|3002|20250317|2", stock_id="3002", hashes=f"{c}|{d}", episode_number=2, start_date="20250317"),
        ]
    )
    v2_detail = pd.DataFrame(
        [
            _detail_row("v|3002|20250117|1", stock_id="3002", hashes=f"{a}|{c}", start_date="20250117", end_date="20250316"),
            _detail_row("v|3002|20250317|2", stock_id="3002", hashes=f"{b}|{d}", episode_number=2, start_date="20250317"),
        ]
    )
    monkeypatch.setattr(producer, "V1_DETAIL_SEMANTIC_SHA256", validator._projected_source_detail_sha256(v1_detail))
    v2_manifest.loc[0, "projected_episode_semantic_sha256"] = validator._projected_source_detail_sha256(v2_detail)
    with pytest.raises(RuntimeError, match="many-to-many"):
        producer.build_projection_v1_v2_diff(v1_manifest, v1_detail, v2_manifest, v2_detail)

    v1_detail.loc[1, "qualifying_source_row_canonical_sha256s"] = f"{a}|{c}"
    with pytest.raises(RuntimeError, match="multiple episodes"):
        producer.build_projection_v1_v2_diff(v1_manifest, v1_detail, v2_manifest, v2_detail)


def test_diff_rejects_exact_key_token_contradiction(monkeypatch) -> None:
    v1_manifest, _v1_detail, v2_manifest, _v2_detail = _inputs(monkeypatch)
    key = "variant|3002|20250917|1"
    v1_detail = pd.DataFrame([_detail_row(key, stock_id="3002", hashes="a" * 64)])
    v2_detail = pd.DataFrame([_detail_row(key, stock_id="3002", hashes="b" * 64)])
    monkeypatch.setattr(producer, "V1_DETAIL_SEMANTIC_SHA256", validator._projected_source_detail_sha256(v1_detail))
    v2_manifest.loc[0, "projected_episode_semantic_sha256"] = validator._projected_source_detail_sha256(v2_detail)
    with pytest.raises(RuntimeError, match="contradictory qualifying source tokens"):
        producer.build_projection_v1_v2_diff(v1_manifest, v1_detail, v2_manifest, v2_detail)


def test_diff_validator_rejects_rehashed_no_edge_component_mutation(
    monkeypatch,
) -> None:
    inputs = _inputs(monkeypatch)
    frame = producer.build_projection_v1_v2_diff(*inputs)
    forged = frame.copy()
    index = forged.index[forged["relation_status"].eq("absent_after_repair")][0]
    forged.loc[index, "relation_component_type"] = "one_to_one"
    forged.loc[:, "relation_row_sha256"] = ""
    forged.loc[:, "relation_row_set_sha256"] = ""
    forged = producer._attach_relation_hashes(forged)

    errors = validator.validate_frames(*inputs, forged)
    assert "v1/v2 diff episode successor mapping mismatch" in errors


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
