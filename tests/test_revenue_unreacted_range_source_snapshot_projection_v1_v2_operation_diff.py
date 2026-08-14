from __future__ import annotations

from io import BytesIO
import json
from pathlib import Path
import sys

import pandas as pd
import pytest


ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))

import revenue_unreacted_range_source_snapshot_projection_v1_v2_operation_diff as producer  # noqa: E402
import revenue_unreacted_range_source_snapshot_projection_v1_v2_diff as source_diff_builder  # noqa: E402
import validate_revenue_unreacted_range_source_snapshot_projection_v1_v2_operation_diff as validator  # noqa: E402


BASE_LINEAGE = {
    "projection_v1_manifest_git_blob_sha": producer.V1_MANIFEST_GIT_BLOB_SHA,
    "projection_v1_manifest_git_blob_raw_sha256": producer.V1_MANIFEST_RAW_SHA256,
    "projection_v1_detail_git_blob_sha": producer.V1_DETAIL_GIT_BLOB_SHA,
    "projection_v1_detail_git_blob_raw_sha256": producer.V1_DETAIL_RAW_SHA256,
    "projection_v1_detail_semantic_sha256": producer.V1_DETAIL_SEMANTIC_SHA256,
    "source_repair_input_head_sha": producer.SOURCE_REPAIR_INPUT_HEAD_SHA,
    "source_repair_artifact_commit_sha": producer.SOURCE_REPAIR_ARTIFACT_COMMIT_SHA,
    "source_repair_workflow_run_id": producer.SOURCE_REPAIR_WORKFLOW_RUN_ID,
    "source_repair_report_git_blob_sha": producer.SOURCE_REPAIR_REPORT_GIT_BLOB_SHA,
    "source_repair_report_git_blob_raw_sha256": producer.SOURCE_REPAIR_REPORT_RAW_SHA256,
}
ASOF_LATEST_DATE = "20260831"


def _attach_source_hashes(frame: pd.DataFrame) -> pd.DataFrame:
    payload_columns = [
        column
        for column in frame.columns
        if column not in {"generated_at", "relation_row_sha256", "relation_row_set_sha256"}
    ]
    result = frame.copy()
    result["relation_row_sha256"] = [
        producer._canonical_json_sha256(
            {column: producer._value(row[column]) for column in payload_columns}
        )
        for _, row in result.iterrows()
    ]
    result["relation_row_set_sha256"] = producer._canonical_json_sha256(
        sorted(result["relation_row_sha256"].tolist())
    )
    return result


def _projection_v2_pair() -> tuple[bytes, bytes, dict[str, str]]:
    detail = pd.DataFrame(
        [
            {
                "generated_at": "2026-08-14 00:00:00 Asia/Taipei",
                "monthly_revenue_history_blob_sha256": "7" * 64,
                "cross_market_resolution_registry_canonical_sha256": "8" * 64,
                "artifact_version": producer.V2_PROJECTION_ARTIFACT_VERSION,
                "episode_key": "projection-v2-episode",
                "stock_id": "2400",
            }
        ]
    )
    semantic = producer._projection_detail_semantic_sha256(detail)
    manifest = pd.DataFrame(
        [
            {
                "artifact_version": producer.V2_PROJECTION_ARTIFACT_VERSION,
                "projected_episode_semantic_sha256": semantic,
            }
        ]
    )
    manifest_raw = manifest.to_csv(index=False).encode("utf-8")
    detail_raw = detail.to_csv(index=False).encode("utf-8")
    lineage = {
        **BASE_LINEAGE,
        "projection_v2_manifest_canonical_sha256": producer.canonical_frame_sha256(
            manifest
        ),
        "projection_v2_detail_semantic_sha256": semantic,
    }
    return manifest_raw, detail_raw, lineage


def _source_diff(lineage: dict[str, str]) -> pd.DataFrame:
    rows: list[dict[str, object]] = []
    for index in range(8):
        episode_key = f"episode|{2400 + index}|{index}"
        stock_id = str(2400 + index)
        original_source_sha = f"{100 + index:064x}"
        if index == 7:
            relation_status = "absent_after_repair"
            absence_reason = "no_shared_qualifying_source_row"
            corrected_episode_key = ""
            corrected_start_sha = ""
            corrected_source_shas = ""
            corrected_tokens: set[str] = set()
            component_type = "v1_no_edge"
            mapping_role = "original_without_corrected_edge"
            mapping_basis = "no_shared_qualifying_source_row"
            boundary_status = "original_episode_absent_after_price_repair"
        else:
            relation_status = "exact_episode_key_successor"
            absence_reason = ""
            corrected_episode_key = episode_key
            corrected_start_sha = (
                f"{900 + index:064x}" if index == 6 else original_source_sha
            )
            corrected_source_shas = (
                f"{original_source_sha}|{corrected_start_sha}"
                if index == 6
                else original_source_sha
            )
            corrected_tokens = set(corrected_source_shas.split("|"))
            component_type = "one_to_one"
            mapping_role = "exact_key_anchor"
            mapping_basis = "exact_episode_key_with_token_overlap"
            boundary_status = "episode_boundary_preserved"
        original_tokens = {original_source_sha}
        overlap = original_tokens & corrected_tokens
        added = corrected_tokens - original_tokens
        removed = original_tokens - corrected_tokens
        original_keys = [episode_key]
        corrected_keys = [corrected_episode_key] if corrected_episode_key else []
        edge_payload = (
            [
                {
                    "original_episode_key": episode_key,
                    "corrected_episode_key": corrected_episode_key,
                    "overlap_tokens": sorted(overlap),
                }
            ]
            if corrected_episode_key
            else []
        )
        component_id = producer._canonical_json_sha256(
            {
                "condition_variant_id": "absolute_or_two_month_yoy_ge15",
                "stock_id": stock_id,
                "component_type": component_type,
                "original_episode_keys": original_keys,
                "corrected_episode_keys": corrected_keys,
                "edges": edge_payload,
                "original_token_union": sorted(original_tokens),
                "corrected_token_union": sorted(corrected_tokens),
                "original_start_date": "20250917",
                "original_end_date": "20260713",
                "corrected_start_date": "20250917" if corrected_episode_key else "",
                "corrected_end_date": "20260713" if corrected_episode_key else "",
            }
        )
        episode = {
            "generated_at": "2026-08-14 00:00:00 Asia/Taipei",
            "model_id": producer.MODEL_ID,
            "artifact_id": "revenue_unreacted_range_source_snapshot_projection_v1_v2_diff",
            "artifact_version": producer.SOURCE_DIFF_ARTIFACT_VERSION,
            "record_type": "episode_relation",
            "relation_status": relation_status,
            "absence_reason": absence_reason,
            "relation_component_id": component_id,
            "relation_component_type": component_type,
            "relation_cardinality": "1:1" if corrected_episode_key else "1:0",
            "relation_component_original_count": "1",
            "relation_component_corrected_count": "1" if corrected_episode_key else "0",
            "relation_component_edge_count": "1" if corrected_episode_key else "0",
            "relation_component_original_episode_keys_json": json.dumps(original_keys, separators=(",", ":")),
            "relation_component_corrected_episode_keys_json": json.dumps(corrected_keys, separators=(",", ":")),
            "relation_component_original_start_date": "20250917",
            "relation_component_original_end_date": "20260713",
            "relation_component_corrected_start_date": "20250917" if corrected_episode_key else "",
            "relation_component_corrected_end_date": "20260713" if corrected_episode_key else "",
            "condition_variant_id": "absolute_or_two_month_yoy_ge15",
            "stock_id": stock_id,
            "relation_row_sha256": "",
            "relation_row_set_sha256": "",
            "original_operation_key": "",
            "original_candidate_detail_row_sha256": "",
            "original_episode_key": episode_key,
            "original_episode_number": "1",
            "original_episode_start_source_date": "20250917",
            "corrected_episode_key": corrected_episode_key,
            "corrected_episode_number": "1" if corrected_episode_key else "",
            "corrected_episode_start_source_date": "20250917" if corrected_episode_key else "",
            "original_episode_start_source_row_canonical_sha256": original_source_sha,
            "corrected_episode_start_source_row_canonical_sha256": corrected_start_sha,
            "original_qualifying_source_row_canonical_sha256s": original_source_sha,
            "corrected_qualifying_source_row_canonical_sha256s": corrected_source_shas,
            "original_episode_end_date": "20260713",
            "original_episode_status": "right_censored_before_active_horizon",
            "corrected_episode_end_date": "20260713" if corrected_episode_key else "",
            "corrected_episode_status": "right_censored_before_active_horizon" if corrected_episode_key else "",
            "mapping_role": mapping_role,
            "mapping_basis": mapping_basis,
            "edge_overlap_source_row_canonical_sha256s": "|".join(sorted(overlap)),
            "edge_overlap_count": str(len(overlap)),
            "mapping_overlap_count": str(len(overlap)),
            "original_token_fully_contained": str(original_tokens <= corrected_tokens).lower() if corrected_episode_key else "",
            "corrected_token_fully_contained": str(corrected_tokens <= original_tokens).lower() if corrected_episode_key else "",
            "component_original_source_row_canonical_sha256s": "|".join(sorted(original_tokens)),
            "component_corrected_source_row_canonical_sha256s": "|".join(sorted(corrected_tokens)),
            "component_added_source_row_canonical_sha256s": "|".join(sorted(added)),
            "component_removed_source_row_canonical_sha256s": "|".join(sorted(removed)),
            "component_original_token_union_sha256": producer._canonical_json_sha256(sorted(original_tokens)),
            "component_corrected_token_union_sha256": producer._canonical_json_sha256(sorted(corrected_tokens)),
            "component_added_token_set_sha256": producer._canonical_json_sha256(sorted(added)),
            "component_removed_token_set_sha256": producer._canonical_json_sha256(sorted(removed)),
            "component_token_set_relation": (
                "token_sets_equal"
                if original_tokens == corrected_tokens
                else "original_token_union_strict_subset_of_corrected"
                if original_tokens < corrected_tokens
                else "corrected_token_union_strict_subset_of_original"
            ),
            "boundary_change_status": boundary_status,
            "promotion_gate_status": "not_promotion_evidence_source_diff_only",
            "research_only": True,
            "formal_model_use_allowed": False,
            "approved_for_daily": False,
            "presentation_allowed": False,
            "production_change": False,
            "promotion_evidence_allowed": False,
            "ranking_consumption_allowed": False,
            "pdf_consumption_allowed": False,
            **lineage,
        }
        rows.append(episode)
    return _attach_source_hashes(pd.DataFrame(rows))


def _source_episode(
    episode_key: str,
    *,
    stock_id: str,
    episode_number: int,
    start_date: str,
    end_date: str,
    tokens: str,
) -> pd.Series:
    return pd.Series(
        {
            "condition_variant_id": "absolute_or_two_month_yoy_ge15",
            "stock_id": stock_id,
            "episode_key": episode_key,
            "episode_number": str(episode_number),
            "episode_start_source_date": start_date,
            "episode_start_source_row_canonical_sha256": tokens.split("|")[0],
            "qualifying_source_row_canonical_sha256s": tokens,
            "episode_end_date": end_date,
            "episode_status": "right_censored_before_active_horizon",
        }
    )


def _replace_source_component(
    source_diff: pd.DataFrame,
    *,
    stock_id: str,
    originals: list[pd.Series],
    corrected: list[pd.Series],
) -> pd.DataFrame:
    lineage = source_diff.iloc[0]
    base = source_diff_builder._base_row(
        generated_at="2026-08-14 00:00:00 Asia/Taipei",
        v2_manifest_sha256=lineage["projection_v2_manifest_canonical_sha256"],
        v2_detail_sha256=lineage["projection_v2_detail_semantic_sha256"],
    )
    edges = []
    for original in originals:
        original_tokens = set(original["qualifying_source_row_canonical_sha256s"].split("|"))
        for successor in corrected:
            corrected_tokens = set(successor["qualifying_source_row_canonical_sha256s"].split("|"))
            overlap = original_tokens & corrected_tokens
            if overlap:
                edges.append((original, successor, overlap))
    rows = source_diff_builder._component_rows(
        originals,
        corrected,
        edges,
        group_key=("absolute_or_two_month_yoy_ge15", stock_id),
        base=base,
    )
    replacement = pd.DataFrame(rows, columns=list(source_diff_builder.RELATION_COLUMNS))
    retained = source_diff.loc[source_diff["stock_id"].ne(stock_id)].copy()
    raw = pd.concat(
        [
            retained.drop(columns=["relation_row_sha256", "relation_row_set_sha256"]),
            replacement.drop(columns=["relation_row_sha256", "relation_row_set_sha256"]),
        ],
        ignore_index=True,
        sort=False,
    ).fillna("")
    return _attach_source_hashes(raw)


def _anomaly_registry() -> pd.DataFrame:
    return pd.DataFrame(
        [
            {
                "model_id": producer.MODEL_ID,
                "operation_key": f"operation|{2400 + index}|{index}",
                "candidate_detail_row_sha256": f"{10 + index:064x}",
                "final_disposition": "unresolved_anomaly_candidate",
            }
            for index in range(8)
        ]
    )


def _original_detail() -> pd.DataFrame:
    return pd.DataFrame(
        [
            {
                "model_id": producer.MODEL_ID,
                "artifact_id": "revenue_unreacted_range_low_mid_falling_candidate_audit",
                "artifact_version": "low_mid_falling_candidate_v1_20260720",
                "operation_key": f"operation|{2400 + index}|{index}",
                "candidate_detail_row_sha256": f"{10 + index:064x}",
                "stock_id": str(2400 + index),
                "episode_key": f"episode|{2400 + index}|{index}",
                "entry_date": f"2026{index + 1:02d}03",
                "entry_price": str(20 + index),
                "exit_date": f"2026{index + 1:02d}20",
                "exit_price": str(21 + index),
            }
            for index in range(8)
        ]
    )


def _corrected_detail(lineage: dict[str, str]) -> pd.DataFrame:
    rows = []
    for index in range(7):
        entry_price = str(20 + index)
        exit_price = str(21 + index)
        if index == 6:
            exit_price = "99"
        rows.append(
            {
                "model_id": producer.MODEL_ID,
                "artifact_id": "revenue_unreacted_range_low_mid_falling_candidate_audit",
                "artifact_version": "low_mid_falling_candidate_v2_20260814",
                "source_projection_artifact_version": (
                    producer.V2_PROJECTION_ARTIFACT_VERSION
                ),
                "source_projection_manifest_canonical_sha256": lineage[
                    "projection_v2_manifest_canonical_sha256"
                ],
                "source_projection_projected_episode_semantic_sha256": lineage[
                    "projection_v2_detail_semantic_sha256"
                ],
                "operation_key": f"corrected_operation|{2400 + index}|{index}",
                "candidate_detail_row_sha256": f"{1000 + index:064x}",
                "candidate_detail_row_set_sha256": "",
                "stock_id": str(2400 + index),
                "entry_date": f"2026{index + 1:02d}03",
                "entry_price": entry_price,
                "exit_date": f"2026{index + 1:02d}20",
                "exit_price": exit_price,
                "asof_latest_date": ASOF_LATEST_DATE,
            }
        )
    frame = pd.DataFrame(rows)
    frame["candidate_detail_row_set_sha256"] = producer._canonical_json_sha256(
        sorted(frame["candidate_detail_row_sha256"].tolist())
    )
    return frame


def _summary(detail: pd.DataFrame, lineage: dict[str, str]) -> pd.DataFrame:
    return pd.DataFrame(
        [
            {
                "model_id": producer.MODEL_ID,
                "artifact_id": "revenue_unreacted_range_low_mid_falling_candidate_audit",
                "artifact_version": "low_mid_falling_candidate_v2_20260814",
                "source_projection_artifact_version": (
                    producer.V2_PROJECTION_ARTIFACT_VERSION
                ),
                "source_projection_manifest_canonical_sha256": lineage[
                    "projection_v2_manifest_canonical_sha256"
                ],
                "source_projection_projected_episode_semantic_sha256": lineage[
                    "projection_v2_detail_semantic_sha256"
                ],
                "detail_artifact_canonical_sha256": producer.canonical_frame_sha256(
                    detail
                ),
                "candidate_detail_row_set_sha256": detail.iloc[0][
                    "candidate_detail_row_set_sha256"
                ],
                "asof_latest_date": ASOF_LATEST_DATE,
                "operation_count": str(len(detail)),
            }
        ]
    )


def _report(
    source_diff: pd.DataFrame,
    original: pd.DataFrame,
    summary: pd.DataFrame,
    detail: pd.DataFrame,
    lineage: dict[str, str],
) -> pd.DataFrame:
    source_row_set = source_diff.iloc[0]["relation_row_set_sha256"]
    summary_sha = producer.canonical_frame_sha256(summary)
    detail_sha = producer.canonical_frame_sha256(detail)
    detail_row_set = detail.iloc[0]["candidate_detail_row_set_sha256"]
    rows = []
    for index in range(8):
        source_relation = (
            "source_replay_equal"
            if index < 6
            else (
                "source_replay_changed_successor"
                if index == 6
                else "final_source_absence_after_repair"
            )
        )
        final_status = producer.FINAL_SUCCESSOR if index < 7 else producer.FINAL_ABSENCE
        corrected = detail.iloc[index] if index < 7 else None
        original_row = original.iloc[index]
        rows.append(
            {
                "model_id": producer.MODEL_ID,
                "artifact_id": "revenue_unreacted_range_low_mid_falling_final_report",
                "artifact_version": "low_mid_falling_final_report_v1_20260814",
                "original_operation_key": original_row["operation_key"],
                "original_candidate_detail_row_sha256": original_row[
                    "candidate_detail_row_sha256"
                ],
                "final_relation_status": final_status,
                "corrected_operation_key": (
                    corrected["operation_key"] if corrected is not None else ""
                ),
                "corrected_candidate_detail_row_sha256": (
                    corrected["candidate_detail_row_sha256"]
                    if corrected is not None
                    else ""
                ),
                "original_stock_id": original_row["stock_id"],
                "original_entry_date": original_row["entry_date"],
                "original_entry_price": original_row["entry_price"],
                "original_exit_date": original_row["exit_date"],
                "original_exit_price": original_row["exit_price"],
                "corrected_stock_id": (
                    corrected["stock_id"] if corrected is not None else ""
                ),
                "corrected_entry_date": (
                    corrected["entry_date"] if corrected is not None else ""
                ),
                "corrected_entry_price": (
                    corrected["entry_price"] if corrected is not None else ""
                ),
                "corrected_exit_date": (
                    corrected["exit_date"] if corrected is not None else ""
                ),
                "corrected_exit_price": (
                    corrected["exit_price"] if corrected is not None else ""
                ),
                "asof_latest_date": ASOF_LATEST_DATE,
                "repair_changed_relevant_input": "true" if index >= 6 else "false",
                "source_replay_relation": source_relation,
                "price_replay_relation": (
                    "entry_exit_price_and_date_equal"
                    if index < 6
                    else (
                        "entry_exit_price_or_date_changed"
                        if index == 6
                        else "not_applicable_final_absence"
                    )
                ),
                "identity_calendar_status": (
                    "verified_same_identity_and_chronological_dates"
                    if index < 7
                    else "original_identity_and_chronology_verified_no_successor"
                ),
                "comparability_status": (
                    "verified_comparable" if index < 7 else "verified_non_comparable"
                ),
                "independent_corroboration_status": "verified_independent_corroboration",
                "independent_corroboration_reference": f"evidence://case/{index}",
                "approved_non_comparable_reason_reference": (
                    "approval://source-absence/7" if index == 7 else ""
                ),
                "contradiction_count": "0",
                "contradiction_evidence_reference": "",
                "approved_absence_reason": (
                    "source repair removes the qualifying operation" if index == 7 else ""
                ),
                "approved_absence_reason_reference": (
                    "approval://operation-absence/7" if index == 7 else ""
                ),
                "source_diff_relation_row_set_sha256": source_row_set,
                "corrected_low_mid_summary_canonical_sha256": summary_sha,
                "corrected_low_mid_detail_canonical_sha256": detail_sha,
                "corrected_low_mid_detail_row_set_sha256": detail_row_set,
                **lineage,
            }
        )
    return pd.DataFrame(rows)


def _inputs():
    manifest_raw, projection_detail_raw, lineage = _projection_v2_pair()
    anomaly_registry = _anomaly_registry()
    source_diff = _source_diff(lineage)
    original = _original_detail()
    detail = _corrected_detail(lineage)
    summary = _summary(detail, lineage)
    report = _report(source_diff, original, summary, detail, lineage)
    return (
        anomaly_registry,
        source_diff,
        manifest_raw,
        projection_detail_raw,
        original,
        summary,
        detail,
        report,
    )


def _inputs_with_merge_and_split():
    inputs = list(_inputs())
    a, b, c, d = (character * 64 for character in "abcd")
    source_diff = _replace_source_component(
        inputs[1],
        stock_id="2400",
        originals=[
            _source_episode(
                "episode|2400|0",
                stock_id="2400",
                episode_number=1,
                start_date="20250917",
                end_date="20251216",
                tokens=a,
            ),
            _source_episode(
                "episode|2400|merge2",
                stock_id="2400",
                episode_number=2,
                start_date="20251217",
                end_date="20260713",
                tokens=b,
            ),
        ],
        corrected=[
            _source_episode(
                "episode|2400|0",
                stock_id="2400",
                episode_number=1,
                start_date="20250917",
                end_date="20260713",
                tokens=f"{a}|{b}",
            )
        ],
    )
    source_diff = _replace_source_component(
        source_diff,
        stock_id="2401",
        originals=[
            _source_episode(
                "episode|2401|1",
                stock_id="2401",
                episode_number=1,
                start_date="20250917",
                end_date="20260713",
                tokens=f"{c}|{d}",
            )
        ],
        corrected=[
            _source_episode(
                "episode|2401|1",
                stock_id="2401",
                episode_number=1,
                start_date="20250917",
                end_date="20251216",
                tokens=c,
            ),
            _source_episode(
                "episode|2401|split2",
                stock_id="2401",
                episode_number=2,
                start_date="20251217",
                end_date="20260713",
                tokens=d,
            ),
        ],
    )
    inputs[1] = source_diff
    lineage = {
        column: source_diff.iloc[0][column]
        for column in producer.SOURCE_LINEAGE_COLUMNS
    }
    report = _report(
        source_diff,
        inputs[4],
        inputs[5],
        inputs[6],
        lineage,
    )
    report.loc[0, "repair_changed_relevant_input"] = "true"
    report.loc[0, "source_replay_relation"] = (
        "source_replay_episode_merged_into_successor"
    )
    report.loc[1, "repair_changed_relevant_input"] = "true"
    report.loc[1, "source_replay_relation"] = (
        "source_replay_episode_split_into_successors"
    )
    inputs[7] = report
    return tuple(inputs)


def test_operation_diff_exact_eight_final_rows_and_machine_facts() -> None:
    inputs = _inputs()
    frame = producer.build_operation_diff(
        *inputs,
        generated_at="2026-08-14 00:00:00 Asia/Taipei",
    )
    assert validator.validate_frames(*inputs, frame) == []
    assert len(frame) == 8
    assert set(frame["final_relation_status"]) == {
        producer.FINAL_SUCCESSOR,
        producer.FINAL_ABSENCE,
    }
    assert set(frame["repair_changed_relevant_input"]) == {"true", "false"}
    assert set(frame["source_replay_relation"]) == {
        "source_replay_equal",
        "source_replay_changed_successor",
        "final_source_absence_after_repair",
    }
    assert set(frame["formal_model_use_allowed"]) == {False}
    assert set(frame["promotion_allowed"]) == {False}
    assert frame["original_entry_price"].ne("").all()
    assert set(frame["asof_latest_date"]) == {ASOF_LATEST_DATE}


def test_operation_diff_merge_and_split_require_exact_corrected_operation_replay() -> None:
    inputs = _inputs_with_merge_and_split()
    frame = producer.build_operation_diff(*inputs)
    assert validator.validate_frames(*inputs, frame) == []
    assert {
        "source_replay_episode_merged_into_successor",
        "source_replay_episode_split_into_successors",
    } <= set(frame["source_replay_relation"])

    forged_inputs = list(inputs)
    forged_report = forged_inputs[7].copy()
    forged_report.loc[1, "corrected_operation_key"] = "episode|2401|split2"
    forged_inputs[7] = forged_report
    with pytest.raises(RuntimeError, match="exactly one corrected detail row"):
        producer.build_operation_diff(*forged_inputs)


def test_operation_diff_rejects_mutated_source_component_metadata() -> None:
    inputs = list(_inputs_with_merge_and_split())
    forged_source = inputs[1].copy()
    target = forged_source.index[
        forged_source["relation_component_type"].eq("many_v1_to_one_v2")
    ][0]
    forged_source.loc[target, "relation_component_original_count"] = "99"
    inputs[1] = _attach_source_hashes(
        forged_source.drop(columns=["relation_row_sha256", "relation_row_set_sha256"])
    )
    inputs[7] = inputs[7].copy()
    inputs[7]["source_diff_relation_row_set_sha256"] = inputs[1].iloc[0][
        "relation_row_set_sha256"
    ]
    with pytest.raises(RuntimeError, match="must have one value|component count"):
        producer.build_operation_diff(*inputs)


def test_operation_diff_rejects_pending_and_freely_labeled_machine_fact() -> None:
    inputs = list(_inputs())
    pending = inputs[7].copy()
    pending.loc[0, "final_relation_status"] = "pending_corrected_operation_replay"
    with pytest.raises(RuntimeError, match="pending or invalid"):
        producer.build_operation_diff(*inputs[:7], pending)

    forged = inputs[7].copy()
    forged.loc[0, "price_replay_relation"] = "freely_labeled"
    with pytest.raises(RuntimeError, match="not derived from replay inputs"):
        producer.build_operation_diff(*inputs[:7], forged)


def test_operation_diff_requires_exact_eight_and_approved_absence_evidence() -> None:
    inputs = list(_inputs())
    seven = inputs[7].iloc[:-1].copy()
    with pytest.raises(RuntimeError, match="exactly eight"):
        producer.build_operation_diff(*inputs[:7], seven)

    no_reference = inputs[7].copy()
    no_reference.loc[7, "approved_non_comparable_reason_reference"] = ""
    with pytest.raises(RuntimeError, match="approved reason reference"):
        producer.build_operation_diff(*inputs[:7], no_reference)


def test_operation_diff_rejects_ambiguous_or_unproven_source_absence() -> None:
    inputs = list(_inputs())
    source_diff = inputs[1].copy()
    target = source_diff.index[
        source_diff["original_episode_key"].eq("episode|2407|7")
    ][0]
    source_diff.loc[target, "relation_status"] = (
        "ambiguous_qualifying_source_overlap"
    )
    source_diff.loc[target, "absence_reason"] = (
        "ambiguous_equal_maximum_qualifying_source_overlap"
    )
    inputs[1] = _attach_source_hashes(
        source_diff.drop(columns=["relation_row_sha256", "relation_row_set_sha256"])
    )
    inputs[7] = inputs[7].copy()
    inputs[7]["source_diff_relation_row_set_sha256"] = inputs[1].iloc[0][
        "relation_row_set_sha256"
    ]
    with pytest.raises(RuntimeError, match="component edge semantics"):
        producer.build_operation_diff(*inputs)

    inputs = list(_inputs())
    source_diff = inputs[1].copy()
    target = source_diff.index[
        source_diff["original_episode_key"].eq("episode|2407|7")
    ][0]
    source_diff.loc[target, "absence_reason"] = ""
    inputs[1] = _attach_source_hashes(
        source_diff.drop(columns=["relation_row_sha256", "relation_row_set_sha256"])
    )
    inputs[7] = inputs[7].copy()
    inputs[7]["source_diff_relation_row_set_sha256"] = inputs[1].iloc[0][
        "relation_row_set_sha256"
    ]
    with pytest.raises(RuntimeError, match="component edge semantics"):
        producer.build_operation_diff(*inputs)


def test_operation_diff_validator_rejects_mutated_output_and_hashes() -> None:
    inputs = _inputs()
    frame = producer.build_operation_diff(*inputs)
    forged = frame.copy()
    forged.loc[0, "original_entry_price"] = "999"
    errors = validator.validate_frames(*inputs, forged)
    assert "operation diff final relation payload mismatch" in errors
    assert "operation diff operation_relation_row_sha256 mismatch" in errors


def test_operation_diff_rejects_mutated_projection_v2_raw_pair() -> None:
    inputs = list(_inputs())
    manifest = pd.read_csv(
        BytesIO(inputs[2]),
        dtype=str,
        keep_default_na=False,
    )
    manifest.loc[0, "projected_episode_semantic_sha256"] = "f" * 64
    inputs[2] = manifest.to_csv(index=False).encode("utf-8")
    with pytest.raises(RuntimeError, match="manifest canonical binding mismatch"):
        producer.build_operation_diff(*inputs)


def test_operation_diff_missing_corrected_input_fails_before_any_write(
    tmp_path: Path,
) -> None:
    inputs = _inputs()
    input_paths = []
    for index, value in enumerate(inputs[:-1]):
        path = tmp_path / f"input-{index}.csv"
        if isinstance(value, bytes):
            path.write_bytes(value)
        else:
            value.to_csv(path, index=False)
        input_paths.append(path)
    missing_report = tmp_path / "missing-report.csv"
    outputs = [tmp_path / f"mirror-{index}.csv" for index in range(3)]
    for output in outputs:
        output.write_bytes(b"sentinel")
    with pytest.raises(RuntimeError, match="all eight exact-bound inputs"):
        producer.build_and_write_operation_diff_from_paths(
            anomaly_registry_path=input_paths[0],
            source_diff_path=input_paths[1],
            projection_v2_manifest_path=input_paths[2],
            projection_v2_detail_path=input_paths[3],
            original_detail_path=input_paths[4],
            corrected_summary_path=input_paths[5],
            corrected_detail_path=input_paths[6],
            corrected_report_path=missing_report,
            history_path=outputs[0],
            latest_path=outputs[1],
            docs_path=outputs[2],
        )
    assert [output.read_bytes() for output in outputs] == [b"sentinel"] * 3


def test_operation_diff_three_mirrors_and_path_validator(tmp_path: Path) -> None:
    inputs = _inputs()
    frame = producer.build_operation_diff(*inputs)
    input_paths = []
    for index, value in enumerate(inputs):
        path = tmp_path / f"input-{index}.csv"
        if isinstance(value, bytes):
            path.write_bytes(value)
        else:
            value.to_csv(path, index=False)
        input_paths.append(path)
    outputs = [tmp_path / f"mirror-{index}.csv" for index in range(3)]
    producer.write_operation_diff(
        frame,
        history_path=outputs[0],
        latest_path=outputs[1],
        docs_path=outputs[2],
    )
    assert outputs[0].read_bytes() == outputs[1].read_bytes() == outputs[2].read_bytes()
    assert validator.validate_paths(
        anomaly_registry_path=input_paths[0],
        source_diff_path=input_paths[1],
        projection_v2_manifest_path=input_paths[2],
        projection_v2_detail_path=input_paths[3],
        original_detail_path=input_paths[4],
        corrected_summary_path=input_paths[5],
        corrected_detail_path=input_paths[6],
        corrected_report_path=input_paths[7],
        history_path=outputs[0],
        latest_path=outputs[1],
        docs_path=outputs[2],
    ) == []
    outputs[2].write_bytes(outputs[2].read_bytes() + b"\n")
    assert "operation-diff three mirrors are not byte-identical" in validator.validate_paths(
        anomaly_registry_path=input_paths[0],
        source_diff_path=input_paths[1],
        projection_v2_manifest_path=input_paths[2],
        projection_v2_detail_path=input_paths[3],
        original_detail_path=input_paths[4],
        corrected_summary_path=input_paths[5],
        corrected_detail_path=input_paths[6],
        corrected_report_path=input_paths[7],
        history_path=outputs[0],
        latest_path=outputs[1],
        docs_path=outputs[2],
    )


def test_operation_diff_validator_is_independent_of_producer() -> None:
    source = Path(validator.__file__).read_text(encoding="utf-8")
    assert (
        "import revenue_unreacted_range_source_snapshot_projection_v1_v2_operation_diff"
        not in source
    )
    assert (
        "from revenue_unreacted_range_source_snapshot_projection_v1_v2_operation_diff"
        not in source
    )
