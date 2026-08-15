from __future__ import annotations

import argparse
from datetime import datetime
from decimal import Decimal, InvalidOperation
import hashlib
import io
import json
from pathlib import Path
import sys

import pandas as pd


ROOT = Path(__file__).resolve().parents[1]
MODEL_ID = "revenue_unreacted_range"
ARTIFACT_ID = (
    "revenue_unreacted_range_source_snapshot_projection_v1_v2_operation_diff"
)
ARTIFACT_VERSION = "source_snapshot_projection_v1_v2_operation_diff_v1_20260814"
SOURCE_DIFF_ARTIFACT_VERSION = "source_snapshot_projection_v1_v2_diff_v1_20260814"
V2_PROJECTION_ARTIFACT_VERSION = "source_snapshot_projection_v2_20260814"
V1_MANIFEST_RAW_SHA256 = (
    "d2dde5a1f05bc2f15baf4d77f326a7ea90b481492178fa6d2fd6262bf316c79e"
)
V1_MANIFEST_GIT_BLOB_SHA = "163f9874124fd3d1fd27f1d1564ac8ac1892e4a1"
V1_DETAIL_RAW_SHA256 = (
    "b9784e4df2d2eba2c511b1c87f4255a6485a1fe1d7ac67490802e396614ee49a"
)
V1_DETAIL_GIT_BLOB_SHA = "849f72c39588c47f1bfd2fe8acd96255087efdcb"
V1_DETAIL_SEMANTIC_SHA256 = (
    "92c68810ac2b5718d714d450fe83bf23f2f3469fec5db0ae2753330950ab2cf5"
)
PROJECTION_CANONICAL_JSON_VERSION = (
    "revenue_source_snapshot_projection_canonical_json_v1"
)
SOURCE_REPAIR_INPUT_HEAD_SHA = "8176fee986d1659896a681e89f99f0171c481b0a"
SOURCE_REPAIR_ARTIFACT_COMMIT_SHA = "7a9e981e2436af3dfc733905ec26b53f8cdd9f9e"
SOURCE_REPAIR_WORKFLOW_RUN_ID = "31799699472"
SOURCE_REPAIR_REPORT_GIT_BLOB_SHA = "f2d569b122e448f87e956cca771748946a9d7363"
SOURCE_REPAIR_REPORT_RAW_SHA256 = (
    "77bf1a1d7ee16beae5e0b0a0eb97212088d7ef7ca883644cdcf39b59fea8d447"
)
HISTORY_CSV = (
    ROOT
    / "output/history/research/"
    "revenue_unreacted_range_source_snapshot_projection_v1_v2_operation_diff_"
    "v1_20260814.csv"
)
LATEST_CSV = (
    ROOT
    / "output/latest/research_backtest/"
    "revenue_unreacted_range_source_snapshot_projection_v1_v2_operation_diff_"
    "latest.csv"
)
DOCS_CSV = (
    ROOT
    / "docs/latest/"
    "revenue_unreacted_range_source_snapshot_projection_v1_v2_operation_diff_"
    "latest.csv"
)
FINAL_SUCCESSOR = "final_successor"
FINAL_ABSENCE = "final_absence"
FINAL_RELATION_STATUSES = {FINAL_SUCCESSOR, FINAL_ABSENCE}
FORBIDDEN_PENDING_TOKENS = {"", "pending", "tbd", "todo", "unknown", "unresolved"}
SOURCE_LINEAGE_COLUMNS = (
    "projection_v1_manifest_git_blob_sha",
    "projection_v1_manifest_git_blob_raw_sha256",
    "projection_v1_detail_git_blob_sha",
    "projection_v1_detail_git_blob_raw_sha256",
    "projection_v1_detail_semantic_sha256",
    "projection_v2_manifest_canonical_sha256",
    "projection_v2_detail_semantic_sha256",
    "source_repair_input_head_sha",
    "source_repair_artifact_commit_sha",
    "source_repair_workflow_run_id",
    "source_repair_report_git_blob_sha",
    "source_repair_report_git_blob_raw_sha256",
)
SOURCE_COMPONENT_COLUMNS = (
    "relation_component_id",
    "relation_component_type",
    "relation_cardinality",
    "relation_component_original_count",
    "relation_component_corrected_count",
    "relation_component_edge_count",
    "relation_component_original_episode_keys_json",
    "relation_component_corrected_episode_keys_json",
    "relation_component_original_start_date",
    "relation_component_original_end_date",
    "relation_component_corrected_start_date",
    "relation_component_corrected_end_date",
    "condition_variant_id",
    "stock_id",
    "original_episode_number",
    "original_episode_start_source_date",
    "original_episode_end_date",
    "original_episode_status",
    "corrected_episode_number",
    "corrected_episode_start_source_date",
    "corrected_episode_end_date",
    "corrected_episode_status",
    "mapping_role",
    "mapping_basis",
    "edge_overlap_source_row_canonical_sha256s",
    "edge_overlap_count",
    "mapping_overlap_count",
    "original_token_fully_contained",
    "corrected_token_fully_contained",
    "component_original_source_row_canonical_sha256s",
    "component_corrected_source_row_canonical_sha256s",
    "component_added_source_row_canonical_sha256s",
    "component_removed_source_row_canonical_sha256s",
    "component_original_token_union_sha256",
    "component_corrected_token_union_sha256",
    "component_added_token_set_sha256",
    "component_removed_token_set_sha256",
    "component_token_set_relation",
    "boundary_change_status",
)
OUTPUT_COLUMNS = (
    "generated_at",
    "model_id",
    "artifact_id",
    "artifact_version",
    "record_type",
    "original_operation_key",
    "original_candidate_detail_row_sha256",
    "original_stock_id",
    "original_entry_date",
    "original_entry_price",
    "original_exit_date",
    "original_exit_price",
    "final_relation_status",
    "corrected_operation_key",
    "corrected_candidate_detail_row_sha256",
    "corrected_stock_id",
    "corrected_entry_date",
    "corrected_entry_price",
    "corrected_exit_date",
    "corrected_exit_price",
    "asof_latest_date",
    "repair_changed_relevant_input",
    "source_replay_relation",
    "price_replay_relation",
    "identity_calendar_status",
    "comparability_status",
    "independent_corroboration_status",
    "independent_corroboration_reference",
    "approved_non_comparable_reason_reference",
    "contradiction_count",
    "contradiction_evidence_reference",
    "approved_absence_reason",
    "approved_absence_reason_reference",
    "source_diff_artifact_version",
    "source_diff_relation_row_set_sha256",
    "anomaly_registry_canonical_sha256",
    *SOURCE_LINEAGE_COLUMNS,
    "projection_v2_manifest_raw_sha256",
    "projection_v2_detail_raw_sha256",
    "corrected_low_mid_summary_artifact_id",
    "corrected_low_mid_summary_artifact_version",
    "corrected_low_mid_summary_canonical_sha256",
    "original_low_mid_detail_artifact_id",
    "original_low_mid_detail_artifact_version",
    "original_low_mid_detail_canonical_sha256",
    "corrected_low_mid_detail_artifact_id",
    "corrected_low_mid_detail_artifact_version",
    "corrected_low_mid_detail_canonical_sha256",
    "corrected_low_mid_detail_row_set_sha256",
    "corrected_low_mid_report_artifact_id",
    "corrected_low_mid_report_artifact_version",
    "corrected_low_mid_report_canonical_sha256",
    "operation_relation_row_sha256",
    "operation_relation_row_set_sha256",
    "promotion_gate_status",
    "research_only",
    "formal_model_use_allowed",
    "approved_for_daily",
    "presentation_allowed",
    "production_change",
    "promotion_allowed",
    "promotion_evidence_allowed",
    "ranking_consumption_allowed",
    "pdf_consumption_allowed",
)
ROW_HASH_EXCLUDED_COLUMNS = {
    "generated_at",
    "operation_relation_row_sha256",
    "operation_relation_row_set_sha256",
}


def _value(value: object) -> str:
    if value is None or pd.isna(value):
        return ""
    if isinstance(value, bool):
        return "true" if value else "false"
    text = str(value).strip()
    if text.lower() in {"true", "false"}:
        return text.lower()
    return text


def _canonical_json_sha256(payload: object) -> str:
    return hashlib.sha256(
        json.dumps(
            payload,
            ensure_ascii=False,
            sort_keys=True,
            separators=(",", ":"),
        ).encode("utf-8")
    ).hexdigest()


def _canonical_frame_sha256(frame: pd.DataFrame) -> str:
    columns = list(frame.columns)
    rows = [
        {column: _value(row[column]) for column in columns}
        for _, row in frame.iterrows()
    ]
    return _canonical_json_sha256({"columns": columns, "rows": rows})


def _projection_detail_semantic_sha256(frame: pd.DataFrame) -> str:
    columns = [
        column
        for column in frame.columns
        if column
        not in {
            "generated_at",
            "monthly_revenue_history_blob_sha256",
            "cross_market_resolution_registry_canonical_sha256",
        }
    ]
    rows = [
        [_value(value) for value in row]
        for row in frame.loc[:, columns].itertuples(index=False, name=None)
    ]
    rows.sort()
    return _canonical_json_sha256(
        [PROJECTION_CANONICAL_JSON_VERSION, columns, rows]
    )


def _read_csv_bytes(payload: bytes, label: str) -> pd.DataFrame:
    if not payload:
        raise RuntimeError(f"{label} raw bytes must not be empty")
    return pd.read_csv(
        io.BytesIO(payload), dtype=str, keep_default_na=False, low_memory=False
    )


def _require(frame: pd.DataFrame, columns: set[str], label: str) -> None:
    missing = sorted(columns - set(frame.columns))
    if missing:
        raise RuntimeError(f"{label} missing required columns: {missing}")
    if frame.empty:
        raise RuntimeError(f"{label} must not be empty")


def _single(frame: pd.DataFrame, column: str, label: str) -> str:
    values = set(frame[column].map(_value))
    if len(values) != 1 or "" in values:
        raise RuntimeError(f"{label} {column} must have one non-empty value")
    return next(iter(values))


def _sha256(value: object, label: str) -> str:
    text = _value(value).lower()
    if len(text) != 64 or any(character not in "0123456789abcdef" for character in text):
        raise RuntimeError(f"{label} must be a lowercase SHA-256")
    return text


def _git_sha(value: object, label: str) -> str:
    text = _value(value).lower()
    if len(text) != 40 or any(character not in "0123456789abcdef" for character in text):
        raise RuntimeError(f"{label} must be a 40-character Git SHA")
    return text


def _date(value: object, label: str) -> str:
    text = _value(value)
    try:
        datetime.strptime(text, "%Y%m%d")
    except ValueError as exc:
        raise RuntimeError(f"{label} must be YYYYMMDD") from exc
    return text


def _price(value: object, label: str) -> Decimal:
    try:
        number = Decimal(_value(value))
    except InvalidOperation as exc:
        raise RuntimeError(f"{label} must be numeric") from exc
    if not number.is_finite() or number <= 0:
        raise RuntimeError(f"{label} must be a positive finite price")
    return number


def _source_tokens(value: object) -> set[str]:
    return {token for token in _value(value).split("|") if token}


def _source_component_value(
    frame: pd.DataFrame,
    column: str,
    label: str,
) -> str:
    values = set(frame[column].map(_value))
    if len(values) != 1:
        raise RuntimeError(f"{label} {column} must have one value")
    return next(iter(values))


def _source_token_sha(tokens: set[str]) -> str:
    return _canonical_json_sha256(sorted(tokens))


def _source_key_list(value: object, label: str) -> list[str]:
    try:
        parsed = json.loads(_value(value))
    except json.JSONDecodeError as exc:
        raise RuntimeError(f"source diff {label} is invalid JSON") from exc
    if (
        not isinstance(parsed, list)
        or any(not isinstance(item, str) or not item for item in parsed)
        or parsed != sorted(set(parsed))
        or _value(value)
        != json.dumps(parsed, ensure_ascii=False, separators=(",", ":"))
    ):
        raise RuntimeError(f"source diff {label} is not canonical key JSON")
    return parsed


def _source_record_map(
    component: pd.DataFrame,
    prefix: str,
) -> dict[str, pd.Series]:
    columns = (
        f"{prefix}_episode_key",
        f"{prefix}_episode_number",
        f"{prefix}_episode_start_source_date",
        f"{prefix}_episode_start_source_row_canonical_sha256",
        f"{prefix}_qualifying_source_row_canonical_sha256s",
        f"{prefix}_episode_end_date",
        f"{prefix}_episode_status",
    )
    records: dict[str, pd.Series] = {}
    signatures: dict[str, tuple[str, ...]] = {}
    for _, row in component.iterrows():
        key = _value(row[columns[0]])
        if not key:
            continue
        signature = tuple(_value(row[column]) for column in columns)
        if key in signatures and signatures[key] != signature:
            raise RuntimeError(f"source diff inconsistent repeated {prefix} episode")
        signatures[key] = signature
        records[key] = row
    return records


def _source_token_relation(original: set[str], corrected: set[str]) -> str:
    if original == corrected:
        return "token_sets_equal"
    if original < corrected:
        return "original_token_union_strict_subset_of_corrected"
    if corrected < original:
        return "corrected_token_union_strict_subset_of_original"
    if original & corrected:
        return "token_unions_partially_overlap"
    return "token_unions_disjoint"


def _validate_source_components(source_diff: pd.DataFrame) -> None:
    governance = {
        "promotion_gate_status": "not_promotion_evidence_source_diff_only",
        "research_only": "true",
        "formal_model_use_allowed": "false",
        "approved_for_daily": "false",
        "presentation_allowed": "false",
        "production_change": "false",
        "promotion_evidence_allowed": "false",
        "ranking_consumption_allowed": "false",
        "pdf_consumption_allowed": "false",
    }
    for column, expected in governance.items():
        if _single(source_diff, column, "source diff") != expected:
            raise RuntimeError(f"source diff governance mismatch: {column}")
    for component_id, component in source_diff.groupby(
        "relation_component_id", sort=False, dropna=False
    ):
        component_id = _sha256(component_id, "source relation_component_id")
        original_map = _source_record_map(component, "original")
        corrected_map = _source_record_map(component, "corrected")
        original_keys = sorted(original_map)
        corrected_keys = sorted(corrected_map)
        original_count = int(_source_component_value(component, "relation_component_original_count", "source component"))
        corrected_count = int(_source_component_value(component, "relation_component_corrected_count", "source component"))
        edge_count = int(_source_component_value(component, "relation_component_edge_count", "source component"))
        if (original_count, corrected_count) != (len(original_keys), len(corrected_keys)):
            raise RuntimeError("source component episode count mismatch")
        if _source_component_value(component, "relation_cardinality", "source component") != f"{original_count}:{corrected_count}":
            raise RuntimeError("source component cardinality mismatch")
        if original_count > 1 and corrected_count > 1:
            raise RuntimeError("source many-to-many component is forbidden")
        if (original_count, corrected_count) == (1, 1):
            component_type = "one_to_one"
        elif original_count > 1 and corrected_count == 1:
            component_type = "many_v1_to_one_v2"
        elif original_count == 1 and corrected_count > 1:
            component_type = "one_v1_to_many_v2"
        elif (original_count, corrected_count) == (1, 0):
            component_type = "v1_no_edge"
        elif (original_count, corrected_count) == (0, 1):
            component_type = "v2_no_edge"
        else:
            raise RuntimeError("source component cardinality is invalid")
        if _source_component_value(component, "relation_component_type", "source component") != component_type:
            raise RuntimeError("source component type mismatch")
        if _source_key_list(
            _source_component_value(component, "relation_component_original_episode_keys_json", "source component"),
            "original keys",
        ) != original_keys or _source_key_list(
            _source_component_value(component, "relation_component_corrected_episode_keys_json", "source component"),
            "corrected keys",
        ) != corrected_keys:
            raise RuntimeError("source component key set mismatch")
        edges = component.loc[
            component["original_episode_key"].map(_value).ne("")
            & component["corrected_episode_key"].map(_value).ne("")
        ]
        if len(edges) != edge_count or len(component) != (edge_count or 1):
            raise RuntimeError("source component edge count mismatch")
        pairs = list(
            zip(
                edges["original_episode_key"].map(_value),
                edges["corrected_episode_key"].map(_value),
                strict=True,
            )
        )
        if len(pairs) != len(set(pairs)):
            raise RuntimeError("source component edge pairs are not unique")
        original_union: set[str] = set()
        corrected_union: set[str] = set()
        for record_map, prefix, union in (
            (original_map, "original", original_union),
            (corrected_map, "corrected", corrected_union),
        ):
            owners: set[str] = set()
            for row in record_map.values():
                tokens = _source_tokens(
                    row[f"{prefix}_qualifying_source_row_canonical_sha256s"]
                )
                if not tokens or owners & tokens:
                    raise RuntimeError(f"source {prefix} episode token partition mismatch")
                for token in tokens:
                    _sha256(token, f"source {prefix} qualifying token")
                owners.update(tokens)
                union.update(tokens)
        added = corrected_union - original_union
        removed = original_union - corrected_union
        expected_token_fields = {
            "component_original_source_row_canonical_sha256s": "|".join(sorted(original_union)),
            "component_corrected_source_row_canonical_sha256s": "|".join(sorted(corrected_union)),
            "component_added_source_row_canonical_sha256s": "|".join(sorted(added)),
            "component_removed_source_row_canonical_sha256s": "|".join(sorted(removed)),
            "component_original_token_union_sha256": _source_token_sha(original_union),
            "component_corrected_token_union_sha256": _source_token_sha(corrected_union),
            "component_added_token_set_sha256": _source_token_sha(added),
            "component_removed_token_set_sha256": _source_token_sha(removed),
            "component_token_set_relation": _source_token_relation(original_union, corrected_union),
        }
        for column, expected in expected_token_fields.items():
            if _source_component_value(component, column, "source component") != expected:
                raise RuntimeError(f"source component token mismatch: {column}")
        edge_payload = []
        for _, row in edges.iterrows():
            original_tokens = _source_tokens(row["original_qualifying_source_row_canonical_sha256s"])
            corrected_tokens = _source_tokens(row["corrected_qualifying_source_row_canonical_sha256s"])
            overlap = original_tokens & corrected_tokens
            if not overlap or _value(row["edge_overlap_source_row_canonical_sha256s"]) != "|".join(sorted(overlap)):
                raise RuntimeError("source component edge overlap mismatch")
            if _value(row["edge_overlap_count"]) != str(len(overlap)) or _value(row["mapping_overlap_count"]) != str(len(overlap)):
                raise RuntimeError("source component edge overlap count mismatch")
            if _value(row["original_token_fully_contained"]) != _value(original_tokens <= corrected_tokens) or _value(row["corrected_token_fully_contained"]) != _value(corrected_tokens <= original_tokens):
                raise RuntimeError("source component containment flag mismatch")
            edge_payload.append(
                {
                    "original_episode_key": _value(row["original_episode_key"]),
                    "corrected_episode_key": _value(row["corrected_episode_key"]),
                    "overlap_tokens": sorted(overlap),
                }
            )
        original_start = min(
            (_value(row["original_episode_start_source_date"]) for row in original_map.values()), default=""
        )
        original_end = max(
            (_value(row["original_episode_end_date"]) for row in original_map.values()), default=""
        )
        corrected_start = min(
            (_value(row["corrected_episode_start_source_date"]) for row in corrected_map.values()), default=""
        )
        corrected_end = max(
            (_value(row["corrected_episode_end_date"]) for row in corrected_map.values()), default=""
        )
        for column, expected in {
            "relation_component_original_start_date": original_start,
            "relation_component_original_end_date": original_end,
            "relation_component_corrected_start_date": corrected_start,
            "relation_component_corrected_end_date": corrected_end,
        }.items():
            if _source_component_value(component, column, "source component") != expected:
                raise RuntimeError(f"source component boundary mismatch: {column}")
        payload = {
            "condition_variant_id": _source_component_value(component, "condition_variant_id", "source component"),
            "stock_id": _source_component_value(component, "stock_id", "source component"),
            "component_type": component_type,
            "original_episode_keys": original_keys,
            "corrected_episode_keys": corrected_keys,
            "edges": sorted(edge_payload, key=lambda edge: (edge["original_episode_key"], edge["corrected_episode_key"])),
            "original_token_union": sorted(original_union),
            "corrected_token_union": sorted(corrected_union),
            "original_start_date": original_start,
            "original_end_date": original_end,
            "corrected_start_date": corrected_start,
            "corrected_end_date": corrected_end,
        }
        if _canonical_json_sha256(payload) != component_id:
            raise RuntimeError("source relation_component_id mismatch")
        expected_boundary = {
            "many_v1_to_one_v2": "episode_boundaries_merged_after_price_repair",
            "one_v1_to_many_v2": "episode_boundary_split_after_price_repair",
            "v1_no_edge": "original_episode_absent_after_price_repair",
            "v2_no_edge": "new_corrected_episode_after_price_repair",
        }.get(component_type)
        if component_type == "one_to_one":
            original = next(iter(original_map.values()))
            corrected = next(iter(corrected_map.values()))
            expected_boundary = (
                "episode_boundary_preserved"
                if (
                    _value(original["original_episode_key"]),
                    _value(original["original_episode_start_source_date"]),
                    _value(original["original_episode_end_date"]),
                )
                == (
                    _value(corrected["corrected_episode_key"]),
                    _value(corrected["corrected_episode_start_source_date"]),
                    _value(corrected["corrected_episode_end_date"]),
                )
                else "episode_boundary_changed_after_price_repair"
            )
        if _source_component_value(component, "boundary_change_status", "source component") != expected_boundary:
            raise RuntimeError("source component boundary status mismatch")
        if component_type == "many_v1_to_one_v2":
            ordered = sorted(
                original_map.values(),
                key=lambda row: (
                    _value(row["original_episode_start_source_date"]),
                    int(_value(row["original_episode_number"])),
                ),
            )
            numbers = [int(_value(row["original_episode_number"])) for row in ordered]
            if numbers != list(range(numbers[0], numbers[0] + len(numbers))):
                raise RuntimeError("source merge episode sequence mismatch")
            if any(
                _date(previous["original_episode_end_date"], "source merge end")
                >= _date(current["original_episode_start_source_date"], "source merge start")
                for previous, current in zip(ordered, ordered[1:], strict=False)
            ):
                raise RuntimeError("source merge episode chronology mismatch")
            corrected_tokens = corrected_union
            if any(
                not _source_tokens(row["original_qualifying_source_row_canonical_sha256s"])
                <= corrected_tokens
                for row in original_map.values()
            ):
                raise RuntimeError("source merge containment mismatch")
            successor = next(iter(corrected_map.values()))
            anchor = ordered[0]
            if (
                _value(anchor["original_episode_key"]),
                _value(anchor["original_episode_start_source_date"]),
                _value(anchor["original_episode_start_source_row_canonical_sha256"]),
            ) != (
                _value(successor["corrected_episode_key"]),
                _value(successor["corrected_episode_start_source_date"]),
                _value(successor["corrected_episode_start_source_row_canonical_sha256"]),
            ) or _value(successor["corrected_episode_end_date"]) < original_end:
                raise RuntimeError("source merge anchor or boundary mismatch")
        elif component_type == "one_v1_to_many_v2":
            ordered = sorted(
                corrected_map.values(),
                key=lambda row: (
                    _value(row["corrected_episode_start_source_date"]),
                    int(_value(row["corrected_episode_number"])),
                ),
            )
            numbers = [int(_value(row["corrected_episode_number"])) for row in ordered]
            if numbers != list(range(numbers[0], numbers[0] + len(numbers))):
                raise RuntimeError("source split episode sequence mismatch")
            if any(
                _date(previous["corrected_episode_end_date"], "source split end")
                >= _date(current["corrected_episode_start_source_date"], "source split start")
                for previous, current in zip(ordered, ordered[1:], strict=False)
            ):
                raise RuntimeError("source split episode chronology mismatch")
            predecessor = next(iter(original_map.values()))
            anchor = ordered[0]
            if (
                _value(predecessor["original_episode_key"]),
                _value(predecessor["original_episode_start_source_date"]),
                _value(predecessor["original_episode_start_source_row_canonical_sha256"]),
            ) != (
                _value(anchor["corrected_episode_key"]),
                _value(anchor["corrected_episode_start_source_date"]),
                _value(anchor["corrected_episode_start_source_row_canonical_sha256"]),
            ) or _value(predecessor["original_episode_end_date"]) < corrected_end:
                raise RuntimeError("source split anchor or boundary mismatch")
        for _, row in component.iterrows():
            original_key = _value(row["original_episode_key"])
            corrected_key = _value(row["corrected_episode_key"])
            if component_type == "one_to_one":
                exact = original_key == corrected_key
                expected = (
                    "exact_episode_key_successor" if exact else "qualifying_source_overlap_successor",
                    "exact_key_anchor" if exact else "unique_overlap_successor",
                    "exact_episode_key_with_token_overlap" if exact else "unique_qualifying_source_token_overlap",
                    "",
                )
            elif component_type == "many_v1_to_one_v2":
                expected = ("many_to_one_merged_successor", "exact_key_anchor" if original_key == corrected_key else "merge_member", "many_to_one_component_token_overlap", "")
            elif component_type == "one_v1_to_many_v2":
                expected = ("one_to_many_split_successor", "exact_key_anchor" if original_key == corrected_key else "split_member", "one_to_many_component_token_overlap", "")
            elif component_type == "v1_no_edge":
                expected = ("absent_after_repair", "original_without_corrected_edge", "no_shared_qualifying_source_row", "no_shared_qualifying_source_row")
            else:
                expected = ("v2_only_successor", "corrected_without_original_edge", "no_v1_predecessor_episode", "no_v1_predecessor_episode")
            actual = (
                _value(row["relation_status"]),
                _value(row["mapping_role"]),
                _value(row["mapping_basis"]),
                _value(row["absence_reason"]),
            )
            if actual != expected:
                raise RuntimeError("source component edge semantics mismatch")


def _source_inputs(
    source_diff: pd.DataFrame,
) -> dict[str, str]:
    required = {
        "artifact_version",
        "record_type",
        "relation_status",
        "absence_reason",
        "relation_row_sha256",
        "relation_row_set_sha256",
        "original_episode_key",
        "corrected_episode_key",
        "original_episode_start_source_row_canonical_sha256",
        "corrected_episode_start_source_row_canonical_sha256",
        "original_qualifying_source_row_canonical_sha256s",
        "corrected_qualifying_source_row_canonical_sha256s",
        "promotion_gate_status",
        "research_only",
        "formal_model_use_allowed",
        "approved_for_daily",
        "presentation_allowed",
        "production_change",
        "promotion_evidence_allowed",
        "ranking_consumption_allowed",
        "pdf_consumption_allowed",
        *SOURCE_COMPONENT_COLUMNS,
        *SOURCE_LINEAGE_COLUMNS,
    }
    _require(source_diff, required, "source projection v1/v2 diff")
    if _single(source_diff, "artifact_version", "source diff") != SOURCE_DIFF_ARTIFACT_VERSION:
        raise RuntimeError("source diff artifact_version mismatch")
    payload_columns = [
        column
        for column in source_diff.columns
        if column not in {"generated_at", "relation_row_sha256", "relation_row_set_sha256"}
    ]
    row_hashes = [
        _canonical_json_sha256(
            {column: _value(row[column]) for column in payload_columns}
        )
        for _, row in source_diff.iterrows()
    ]
    if source_diff["relation_row_sha256"].map(_value).tolist() != row_hashes:
        raise RuntimeError("source diff relation_row_sha256 mismatch")
    if len(set(row_hashes)) != len(row_hashes):
        raise RuntimeError("source diff relation_row_sha256 must be unique")
    row_set_sha = _canonical_json_sha256(sorted(row_hashes))
    if set(source_diff["relation_row_set_sha256"].map(_value)) != {row_set_sha}:
        raise RuntimeError("source diff relation_row_set_sha256 mismatch")
    if set(source_diff["record_type"].map(_value)) != {"episode_relation"}:
        raise RuntimeError("source diff must contain episode_relation rows only")
    _validate_source_components(source_diff)
    context = {
        "source_diff_artifact_version": SOURCE_DIFF_ARTIFACT_VERSION,
        "source_diff_relation_row_set_sha256": row_set_sha,
    }
    for column in SOURCE_LINEAGE_COLUMNS:
        context[column] = _single(source_diff, column, "source diff")
    fixed = {
        "projection_v1_manifest_git_blob_sha": V1_MANIFEST_GIT_BLOB_SHA,
        "projection_v1_manifest_git_blob_raw_sha256": V1_MANIFEST_RAW_SHA256,
        "projection_v1_detail_git_blob_sha": V1_DETAIL_GIT_BLOB_SHA,
        "projection_v1_detail_git_blob_raw_sha256": V1_DETAIL_RAW_SHA256,
        "projection_v1_detail_semantic_sha256": V1_DETAIL_SEMANTIC_SHA256,
        "source_repair_input_head_sha": SOURCE_REPAIR_INPUT_HEAD_SHA,
        "source_repair_artifact_commit_sha": SOURCE_REPAIR_ARTIFACT_COMMIT_SHA,
        "source_repair_workflow_run_id": SOURCE_REPAIR_WORKFLOW_RUN_ID,
        "source_repair_report_git_blob_sha": SOURCE_REPAIR_REPORT_GIT_BLOB_SHA,
        "source_repair_report_git_blob_raw_sha256": SOURCE_REPAIR_REPORT_RAW_SHA256,
    }
    for column, expected in fixed.items():
        if context[column] != expected:
            raise RuntimeError(f"source diff fixed lineage mismatch: {column}")
    _sha256(context["projection_v2_manifest_canonical_sha256"], "v2 manifest canonical")
    _sha256(context["projection_v2_detail_semantic_sha256"], "v2 detail semantic")
    return context


def _anomaly_inputs(
    anomaly_registry: pd.DataFrame,
) -> tuple[dict[str, str], pd.DataFrame]:
    _require(
        anomaly_registry,
        {"model_id", "operation_key", "candidate_detail_row_sha256"},
        "anomaly disposition registry",
    )
    selected = anomaly_registry.loc[
        anomaly_registry["model_id"].map(_value).eq(MODEL_ID)
    ].copy()
    if len(selected) != 8:
        raise RuntimeError("anomaly registry must contain exactly eight model rows")
    pairs = [
        (_value(row["operation_key"]), _value(row["candidate_detail_row_sha256"]))
        for _, row in selected.iterrows()
    ]
    if len(set(pairs)) != 8 or any(not key for key, _digest in pairs):
        raise RuntimeError("anomaly registry operation pairs must be eight unique rows")
    for _key, digest in pairs:
        _sha256(digest, "anomaly registry candidate row")
    return (
        {"anomaly_registry_canonical_sha256": _canonical_frame_sha256(anomaly_registry)},
        selected,
    )


def _projection_v2_inputs(
    manifest_raw: bytes,
    detail_raw: bytes,
    source: dict[str, str],
) -> dict[str, str]:
    manifest = _read_csv_bytes(manifest_raw, "projection v2 manifest")
    detail = _read_csv_bytes(detail_raw, "projection v2 detail")
    if len(manifest) != 1 or "artifact_version" not in manifest.columns:
        raise RuntimeError("projection v2 manifest must contain one versioned row")
    if _value(manifest.iloc[0]["artifact_version"]) != V2_PROJECTION_ARTIFACT_VERSION:
        raise RuntimeError("projection v2 manifest artifact_version mismatch")
    if _canonical_frame_sha256(manifest) != source[
        "projection_v2_manifest_canonical_sha256"
    ]:
        raise RuntimeError("projection v2 manifest canonical binding mismatch")
    semantic = _projection_detail_semantic_sha256(detail)
    if semantic != source["projection_v2_detail_semantic_sha256"]:
        raise RuntimeError("projection v2 detail semantic binding mismatch")
    if "projected_episode_semantic_sha256" not in manifest.columns or _value(
        manifest.iloc[0]["projected_episode_semantic_sha256"]
    ) != semantic:
        raise RuntimeError("projection v2 manifest does not bind detail semantic SHA-256")
    return {
        "projection_v2_manifest_raw_sha256": hashlib.sha256(manifest_raw).hexdigest(),
        "projection_v2_detail_raw_sha256": hashlib.sha256(detail_raw).hexdigest(),
    }


def _original_inputs(
    original_detail: pd.DataFrame,
    originals: pd.DataFrame,
) -> tuple[dict[str, str], dict[tuple[str, str], pd.Series]]:
    _require(
        original_detail,
        {
            "model_id",
            "artifact_id",
            "artifact_version",
            "operation_key",
            "candidate_detail_row_sha256",
            "stock_id",
            "episode_key",
            "entry_date",
            "entry_price",
            "exit_date",
            "exit_price",
        },
        "original low/mid detail",
    )
    if _single(original_detail, "model_id", "original detail") != MODEL_ID:
        raise RuntimeError("original detail model_id mismatch")
    indexed: dict[tuple[str, str], pd.Series] = {}
    for _, source in originals.iterrows():
        pair = (
            _value(source["operation_key"]),
            _value(source["candidate_detail_row_sha256"]),
        )
        matches = original_detail.loc[
            original_detail["operation_key"].map(_value).eq(pair[0])
            & original_detail["candidate_detail_row_sha256"].map(_value).eq(pair[1])
        ]
        if len(matches) != 1:
            raise RuntimeError(f"original pair must bind exactly one detail row: {pair[0]}")
        row = matches.iloc[0]
        entry_date = _date(row["entry_date"], "original entry_date")
        exit_date = _date(row["exit_date"], "original exit_date")
        if entry_date > exit_date:
            raise RuntimeError("original entry_date must not follow exit_date")
        _price(row["entry_price"], "original entry_price")
        _price(row["exit_price"], "original exit_price")
        if not _value(row["stock_id"]):
            raise RuntimeError("original stock_id must not be empty")
        indexed[pair] = row
    return (
        {
            "original_low_mid_detail_artifact_id": _single(
                original_detail, "artifact_id", "original detail"
            ),
            "original_low_mid_detail_artifact_version": _single(
                original_detail, "artifact_version", "original detail"
            ),
            "original_low_mid_detail_canonical_sha256": _canonical_frame_sha256(
                original_detail
            ),
        },
        indexed,
    )


def _corrected_inputs(
    corrected_summary: pd.DataFrame,
    corrected_detail: pd.DataFrame,
    source: dict[str, str],
) -> tuple[dict[str, str], dict[str, str]]:
    detail_columns = {
        "model_id",
        "artifact_id",
        "artifact_version",
        "source_projection_artifact_version",
        "source_projection_manifest_canonical_sha256",
        "source_projection_projected_episode_semantic_sha256",
        "operation_key",
        "candidate_detail_row_sha256",
        "candidate_detail_row_set_sha256",
        "stock_id",
        "entry_date",
        "entry_price",
        "exit_date",
        "exit_price",
        "asof_latest_date",
    }
    _require(corrected_detail, detail_columns, "corrected low/mid detail")
    if _single(corrected_detail, "model_id", "corrected detail") != MODEL_ID:
        raise RuntimeError("corrected detail model_id mismatch")
    detail_expected = {
        "source_projection_artifact_version": V2_PROJECTION_ARTIFACT_VERSION,
        "source_projection_manifest_canonical_sha256": source[
            "projection_v2_manifest_canonical_sha256"
        ],
        "source_projection_projected_episode_semantic_sha256": source[
            "projection_v2_detail_semantic_sha256"
        ],
    }
    for column, expected in detail_expected.items():
        if _single(corrected_detail, column, "corrected detail") != expected:
            raise RuntimeError(f"corrected detail {column} binding mismatch")
    asof = _date(_single(corrected_detail, "asof_latest_date", "corrected detail"), "asof")
    pairs = []
    hashes = []
    for _, row in corrected_detail.iterrows():
        pair = (_value(row["operation_key"]), _value(row["candidate_detail_row_sha256"]))
        if not pair[0]:
            raise RuntimeError("corrected detail operation_key must not be empty")
        hashes.append(_sha256(pair[1], "corrected candidate row"))
        pairs.append(pair)
        entry_date = _date(row["entry_date"], "corrected entry_date")
        exit_date = _date(row["exit_date"], "corrected exit_date")
        if entry_date > exit_date or exit_date > asof:
            raise RuntimeError("corrected operation date chronology mismatch")
        _price(row["entry_price"], "corrected entry_price")
        _price(row["exit_price"], "corrected exit_price")
    if len(set(pairs)) != len(pairs):
        raise RuntimeError("corrected detail operation pairs must be unique")
    row_set_sha = _canonical_json_sha256(sorted(hashes))
    if set(corrected_detail["candidate_detail_row_set_sha256"].map(_value)) != {row_set_sha}:
        raise RuntimeError("corrected detail row set SHA-256 mismatch")
    detail_context = {
        "corrected_low_mid_detail_artifact_id": _single(
            corrected_detail, "artifact_id", "corrected detail"
        ),
        "corrected_low_mid_detail_artifact_version": _single(
            corrected_detail, "artifact_version", "corrected detail"
        ),
        "corrected_low_mid_detail_canonical_sha256": _canonical_frame_sha256(
            corrected_detail
        ),
        "corrected_low_mid_detail_row_set_sha256": row_set_sha,
        "asof_latest_date": asof,
    }
    summary_columns = {
        "model_id",
        "artifact_id",
        "artifact_version",
        "source_projection_artifact_version",
        "source_projection_manifest_canonical_sha256",
        "source_projection_projected_episode_semantic_sha256",
        "detail_artifact_canonical_sha256",
        "candidate_detail_row_set_sha256",
        "asof_latest_date",
    }
    _require(corrected_summary, summary_columns, "corrected low/mid summary")
    if _single(corrected_summary, "model_id", "corrected summary") != MODEL_ID:
        raise RuntimeError("corrected summary model_id mismatch")
    summary_expected = {
        **detail_expected,
        "detail_artifact_canonical_sha256": detail_context[
            "corrected_low_mid_detail_canonical_sha256"
        ],
        "candidate_detail_row_set_sha256": row_set_sha,
        "asof_latest_date": asof,
    }
    for column, expected in summary_expected.items():
        if _single(corrected_summary, column, "corrected summary") != expected:
            raise RuntimeError(f"corrected summary {column} binding mismatch")
    summary_context = {
        "corrected_low_mid_summary_artifact_id": _single(
            corrected_summary, "artifact_id", "corrected summary"
        ),
        "corrected_low_mid_summary_artifact_version": _single(
            corrected_summary, "artifact_version", "corrected summary"
        ),
        "corrected_low_mid_summary_canonical_sha256": _canonical_frame_sha256(
            corrected_summary
        ),
    }
    return summary_context, detail_context


def _source_facts(source_diff: pd.DataFrame, original: pd.Series) -> tuple[str, str]:
    episode_key = _value(original["episode_key"])
    matches = source_diff.loc[
        source_diff["record_type"].map(_value).eq("episode_relation")
        & source_diff["original_episode_key"].map(_value).eq(episode_key)
    ]
    if not episode_key or matches.empty:
        raise RuntimeError("operation does not bind a source episode relation")
    if len(matches) > 1:
        if (
            set(matches["relation_status"].map(_value))
            != {"one_to_many_split_successor"}
            or set(matches["relation_component_type"].map(_value))
            != {"one_v1_to_many_v2"}
            or len(set(matches["relation_component_id"].map(_value))) != 1
            or len(set(matches["corrected_episode_key"].map(_value))) != len(matches)
        ):
            raise RuntimeError("multiple source relations are not one audited split")
        return "true", "source_replay_episode_split_into_successors"
    row = matches.iloc[0]
    status = _value(row["relation_status"])
    relation_reason = _value(row["absence_reason"])
    if status == "absent_after_repair":
        if _value(row["corrected_episode_key"]):
            raise RuntimeError("absent source relation carries corrected key")
        if relation_reason != "no_shared_qualifying_source_row":
            raise RuntimeError(
                "absent source relation requires exact no-successor evidence"
            )
        return "true", "final_source_absence_after_repair"
    if status not in {
        "exact_episode_key_successor",
        "qualifying_source_overlap_successor",
        "many_to_one_merged_successor",
    }:
        raise RuntimeError(f"source relation is not final: {status!r}")
    if not _value(row["corrected_episode_key"]):
        raise RuntimeError("source successor is missing corrected key")
    if relation_reason:
        raise RuntimeError("source successor relation carries absence_reason")
    if status == "many_to_one_merged_successor":
        if _value(row["relation_component_type"]) != "many_v1_to_one_v2":
            raise RuntimeError("source merge component type mismatch")
        return "true", "source_replay_episode_merged_into_successor"
    changed = any(
        _value(row[original]) != _value(row[corrected])
        for original, corrected in (
            (
                "original_episode_start_source_row_canonical_sha256",
                "corrected_episode_start_source_row_canonical_sha256",
            ),
            (
                "original_qualifying_source_row_canonical_sha256s",
                "corrected_qualifying_source_row_canonical_sha256s",
            ),
        )
    )
    if not changed and status == "exact_episode_key_successor":
        return "false", "source_replay_equal"
    return "true", "source_replay_changed_successor"


def _replay_facts(
    original: pd.Series,
    corrected: pd.Series | None,
    asof: str,
) -> dict[str, str]:
    original_entry = _date(original["entry_date"], "original entry_date")
    original_exit = _date(original["exit_date"], "original exit_date")
    if original_entry > original_exit or original_exit > asof:
        raise RuntimeError("original operation date chronology mismatch")
    result = {
        "original_stock_id": _value(original["stock_id"]),
        "original_entry_date": original_entry,
        "original_entry_price": _value(original["entry_price"]),
        "original_exit_date": original_exit,
        "original_exit_price": _value(original["exit_price"]),
        "corrected_stock_id": "",
        "corrected_entry_date": "",
        "corrected_entry_price": "",
        "corrected_exit_date": "",
        "corrected_exit_price": "",
        "price_replay_relation": "not_applicable_final_absence",
        "identity_calendar_status": "original_identity_and_chronology_verified_no_successor",
    }
    if corrected is None:
        return result
    corrected_entry = _date(corrected["entry_date"], "corrected entry_date")
    corrected_exit = _date(corrected["exit_date"], "corrected exit_date")
    if corrected_entry > corrected_exit or corrected_exit > asof:
        raise RuntimeError("corrected operation date chronology mismatch")
    if _value(original["stock_id"]) != _value(corrected["stock_id"]):
        raise RuntimeError("successor stock identity mismatch")
    same = (
        _price(original["entry_price"], "original entry_price")
        == _price(corrected["entry_price"], "corrected entry_price")
        and _price(original["exit_price"], "original exit_price")
        == _price(corrected["exit_price"], "corrected exit_price")
        and original_entry == corrected_entry
        and original_exit == corrected_exit
    )
    result.update(
        {
            "corrected_stock_id": _value(corrected["stock_id"]),
            "corrected_entry_date": corrected_entry,
            "corrected_entry_price": _value(corrected["entry_price"]),
            "corrected_exit_date": corrected_exit,
            "corrected_exit_price": _value(corrected["exit_price"]),
            "price_replay_relation": (
                "entry_exit_price_and_date_equal"
                if same
                else "entry_exit_price_or_date_changed"
            ),
            "identity_calendar_status": "verified_same_identity_and_chronological_dates",
        }
    )
    return result


def _expected_rows(
    source_diff: pd.DataFrame,
    originals: pd.DataFrame,
    original_rows: dict[tuple[str, str], pd.Series],
    corrected_detail: pd.DataFrame,
    corrected_report: pd.DataFrame,
    common: dict[str, str],
) -> list[dict[str, str]]:
    required = {
        "model_id",
        "artifact_id",
        "artifact_version",
        "original_operation_key",
        "original_candidate_detail_row_sha256",
        "final_relation_status",
        "corrected_operation_key",
        "corrected_candidate_detail_row_sha256",
        "original_stock_id",
        "original_entry_date",
        "original_entry_price",
        "original_exit_date",
        "original_exit_price",
        "corrected_stock_id",
        "corrected_entry_date",
        "corrected_entry_price",
        "corrected_exit_date",
        "corrected_exit_price",
        "asof_latest_date",
        "repair_changed_relevant_input",
        "source_replay_relation",
        "price_replay_relation",
        "identity_calendar_status",
        "comparability_status",
        "independent_corroboration_status",
        "independent_corroboration_reference",
        "approved_non_comparable_reason_reference",
        "contradiction_count",
        "contradiction_evidence_reference",
        "approved_absence_reason",
        "approved_absence_reason_reference",
        "source_diff_relation_row_set_sha256",
        "corrected_low_mid_summary_canonical_sha256",
        "corrected_low_mid_detail_canonical_sha256",
        "corrected_low_mid_detail_row_set_sha256",
        *SOURCE_LINEAGE_COLUMNS,
    }
    _require(corrected_report, required, "corrected low/mid final report")
    if len(corrected_report) != 8:
        raise RuntimeError("corrected report must contain exactly eight rows")
    if _single(corrected_report, "model_id", "corrected report") != MODEL_ID:
        raise RuntimeError("corrected report model_id mismatch")
    for column in (
        "source_diff_relation_row_set_sha256",
        "corrected_low_mid_summary_canonical_sha256",
        "corrected_low_mid_detail_canonical_sha256",
        "corrected_low_mid_detail_row_set_sha256",
        "asof_latest_date",
        *SOURCE_LINEAGE_COLUMNS,
    ):
        if _single(corrected_report, column, "corrected report") != common[column]:
            raise RuntimeError(f"corrected report {column} binding mismatch")
    original_pairs = set(original_rows)
    report_pairs = [
        (_value(row["original_operation_key"]), _value(row["original_candidate_detail_row_sha256"]))
        for _, row in corrected_report.iterrows()
    ]
    if len(set(report_pairs)) != 8 or set(report_pairs) != original_pairs:
        raise RuntimeError("corrected report does not exactly cover original pairs")
    expected: list[dict[str, str]] = []
    for _, report in corrected_report.sort_values(
        ["original_operation_key", "original_candidate_detail_row_sha256"], kind="stable"
    ).iterrows():
        original_pair = (
            _value(report["original_operation_key"]),
            _value(report["original_candidate_detail_row_sha256"]),
        )
        status = _value(report["final_relation_status"])
        if status not in FINAL_RELATION_STATUSES:
            raise RuntimeError(f"corrected report relation is pending or invalid: {status!r}")
        corrected_pair = (
            _value(report["corrected_operation_key"]),
            _value(report["corrected_candidate_detail_row_sha256"]),
        )
        corrected: pd.Series | None = None
        if status == FINAL_SUCCESSOR:
            if not corrected_pair[0]:
                raise RuntimeError("successor is missing corrected_operation_key")
            _sha256(corrected_pair[1], "corrected successor row")
            matches = corrected_detail.loc[
                corrected_detail["operation_key"].map(_value).eq(corrected_pair[0])
                & corrected_detail["candidate_detail_row_sha256"].map(_value).eq(
                    corrected_pair[1]
                )
            ]
            if len(matches) != 1:
                raise RuntimeError("successor does not bind exactly one corrected detail row")
            corrected = matches.iloc[0]
            if _value(report["approved_absence_reason"]) or _value(
                report["approved_absence_reason_reference"]
            ):
                raise RuntimeError("successor carries an absence reason")
        else:
            if corrected_pair != ("", ""):
                raise RuntimeError("final absence carries a corrected pair")
            if _value(report["approved_absence_reason"]).lower() in FORBIDDEN_PENDING_TOKENS or _value(
                report["approved_absence_reason_reference"]
            ).lower() in FORBIDDEN_PENDING_TOKENS:
                raise RuntimeError("final absence lacks approved reason evidence")
        repair_changed, source_relation = _source_facts(
            source_diff,
            original_rows[original_pair],
        )
        derived = {
            **_replay_facts(original_rows[original_pair], corrected, common["asof_latest_date"]),
            "repair_changed_relevant_input": repair_changed,
            "source_replay_relation": source_relation,
        }
        for column, value in derived.items():
            if _value(report[column]) != value:
                raise RuntimeError(f"corrected report {column} is not input-derived")
        comparability = _value(report["comparability_status"])
        non_comparable_ref = _value(report["approved_non_comparable_reason_reference"])
        if comparability not in {"verified_comparable", "verified_non_comparable"}:
            raise RuntimeError("comparability_status is not final")
        if comparability == "verified_non_comparable":
            if non_comparable_ref.lower() in FORBIDDEN_PENDING_TOKENS:
                raise RuntimeError("non-comparable status lacks approved reference")
        elif non_comparable_ref:
            raise RuntimeError("comparable row carries non-comparable reference")
        if _value(report["independent_corroboration_status"]).lower() in FORBIDDEN_PENDING_TOKENS:
            raise RuntimeError("independent corroboration status is not final")
        if _value(report["independent_corroboration_reference"]).lower() in FORBIDDEN_PENDING_TOKENS:
            raise RuntimeError("independent corroboration lacks evidence reference")
        contradiction = _value(report["contradiction_count"])
        if not contradiction.isdigit():
            raise RuntimeError("contradiction_count must be a non-negative integer")
        if int(contradiction) > 0 and _value(
            report["contradiction_evidence_reference"]
        ).lower() in FORBIDDEN_PENDING_TOKENS:
            raise RuntimeError("positive contradiction count lacks evidence reference")
        row = dict(common)
        for column in (
            "original_operation_key",
            "original_candidate_detail_row_sha256",
            "original_stock_id",
            "original_entry_date",
            "original_entry_price",
            "original_exit_date",
            "original_exit_price",
            "final_relation_status",
            "corrected_operation_key",
            "corrected_candidate_detail_row_sha256",
            "corrected_stock_id",
            "corrected_entry_date",
            "corrected_entry_price",
            "corrected_exit_date",
            "corrected_exit_price",
            "asof_latest_date",
            "repair_changed_relevant_input",
            "source_replay_relation",
            "price_replay_relation",
            "identity_calendar_status",
            "comparability_status",
            "independent_corroboration_status",
            "independent_corroboration_reference",
            "approved_non_comparable_reason_reference",
            "contradiction_count",
            "contradiction_evidence_reference",
            "approved_absence_reason",
            "approved_absence_reason_reference",
        ):
            row[column] = _value(report[column])
        expected.append(row)
    return expected


def validate_frames(
    anomaly_registry: pd.DataFrame,
    source_diff: pd.DataFrame,
    projection_v2_manifest_raw: bytes,
    projection_v2_detail_raw: bytes,
    original_detail: pd.DataFrame,
    corrected_summary: pd.DataFrame,
    corrected_detail: pd.DataFrame,
    corrected_report: pd.DataFrame,
    operation_diff: pd.DataFrame,
) -> list[str]:
    if list(operation_diff.columns) != list(OUTPUT_COLUMNS):
        return ["operation diff schema mismatch"]
    if len(operation_diff) != 8:
        return [f"operation diff must contain exactly eight rows: {len(operation_diff)}"]
    try:
        generated_at = _single(operation_diff, "generated_at", "operation diff")
        source_context = _source_inputs(source_diff)
        anomaly_context, originals = _anomaly_inputs(anomaly_registry)
        projection_context = _projection_v2_inputs(
            projection_v2_manifest_raw,
            projection_v2_detail_raw,
            source_context,
        )
        original_context, original_rows = _original_inputs(original_detail, originals)
        summary_context, detail_context = _corrected_inputs(
            corrected_summary,
            corrected_detail,
            source_context,
        )
        report_context = {
            "corrected_low_mid_report_artifact_id": _single(
                corrected_report, "artifact_id", "corrected report"
            ),
            "corrected_low_mid_report_artifact_version": _single(
                corrected_report, "artifact_version", "corrected report"
            ),
            "corrected_low_mid_report_canonical_sha256": _canonical_frame_sha256(
                corrected_report
            ),
        }
        common: dict[str, str] = {
            "generated_at": generated_at,
            "model_id": MODEL_ID,
            "artifact_id": ARTIFACT_ID,
            "artifact_version": ARTIFACT_VERSION,
            "record_type": "operation_relation",
            **source_context,
            **anomaly_context,
            **projection_context,
            **summary_context,
            **original_context,
            **detail_context,
            **report_context,
            "operation_relation_row_sha256": "",
            "operation_relation_row_set_sha256": "",
            "promotion_gate_status": "blocked_requires_separate_promotion_decision",
            "research_only": "true",
            "formal_model_use_allowed": "false",
            "approved_for_daily": "false",
            "presentation_allowed": "false",
            "production_change": "false",
            "promotion_allowed": "false",
            "promotion_evidence_allowed": "false",
            "ranking_consumption_allowed": "false",
            "pdf_consumption_allowed": "false",
        }
        expected_rows = _expected_rows(
            source_diff,
            originals,
            original_rows,
            corrected_detail,
            corrected_report,
            common,
        )
        compare_columns = [
            column
            for column in OUTPUT_COLUMNS
            if column not in {
                "operation_relation_row_sha256",
                "operation_relation_row_set_sha256",
            }
        ]
        expected_payload = sorted(
            tuple(_value(row[column]) for column in compare_columns)
            for row in expected_rows
        )
        actual_payload = sorted(
            tuple(_value(value) for value in row)
            for row in operation_diff.loc[:, compare_columns].itertuples(
                index=False, name=None
            )
        )
        errors: list[str] = []
        if expected_payload != actual_payload:
            errors.append("operation diff final relation payload mismatch")
        payload_columns = [
            column for column in OUTPUT_COLUMNS if column not in ROW_HASH_EXCLUDED_COLUMNS
        ]
        expected_hashes = [
            _canonical_json_sha256(
                {column: _value(row[column]) for column in payload_columns}
            )
            for _, row in operation_diff.iterrows()
        ]
        actual_hashes = operation_diff["operation_relation_row_sha256"].map(_value).tolist()
        if actual_hashes != expected_hashes:
            errors.append("operation diff operation_relation_row_sha256 mismatch")
        if len(set(actual_hashes)) != 8:
            errors.append("operation diff relation row hashes must be eight unique values")
        expected_set = _canonical_json_sha256(sorted(expected_hashes))
        if set(operation_diff["operation_relation_row_set_sha256"].map(_value)) != {
            expected_set
        }:
            errors.append("operation diff operation_relation_row_set_sha256 mismatch")
        return errors
    except (KeyError, RuntimeError, ValueError) as exc:
        return [str(exc)]


def _read_csv(path: Path) -> pd.DataFrame:
    if not Path(path).is_file():
        raise RuntimeError(f"missing required operation-diff input: {path}")
    return pd.read_csv(path, dtype=str, keep_default_na=False, low_memory=False)


def validate_paths(
    *,
    anomaly_registry_path: Path,
    source_diff_path: Path,
    projection_v2_manifest_path: Path,
    projection_v2_detail_path: Path,
    original_detail_path: Path,
    corrected_summary_path: Path,
    corrected_detail_path: Path,
    corrected_report_path: Path,
    history_path: Path = HISTORY_CSV,
    latest_path: Path = LATEST_CSV,
    docs_path: Path = DOCS_CSV,
) -> list[str]:
    inputs = (
        Path(anomaly_registry_path),
        Path(source_diff_path),
        Path(projection_v2_manifest_path),
        Path(projection_v2_detail_path),
        Path(original_detail_path),
        Path(corrected_summary_path),
        Path(corrected_detail_path),
        Path(corrected_report_path),
    )
    missing = [str(path) for path in inputs if not path.is_file()]
    if missing:
        return [f"missing required exact-bound operation-diff inputs: {missing}"]
    mirrors = tuple(Path(path) for path in (history_path, latest_path, docs_path))
    missing_mirrors = [str(path) for path in mirrors if not path.is_file()]
    if missing_mirrors:
        return [f"missing operation-diff mirrors: {missing_mirrors}"]
    payloads = [path.read_bytes() for path in mirrors]
    errors: list[str] = []
    if len(set(payloads)) != 1:
        errors.append("operation-diff three mirrors are not byte-identical")
    errors.extend(
        validate_frames(
            _read_csv(inputs[0]),
            _read_csv(inputs[1]),
            inputs[2].read_bytes(),
            inputs[3].read_bytes(),
            _read_csv(inputs[4]),
            _read_csv(inputs[5]),
            _read_csv(inputs[6]),
            _read_csv(inputs[7]),
            _read_csv(mirrors[0]),
        )
    )
    return errors


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--anomaly-registry", type=Path, required=True)
    parser.add_argument("--source-diff", type=Path, required=True)
    parser.add_argument("--projection-v2-manifest", type=Path, required=True)
    parser.add_argument("--projection-v2-detail", type=Path, required=True)
    parser.add_argument("--original-detail", type=Path, required=True)
    parser.add_argument("--corrected-summary", type=Path, required=True)
    parser.add_argument("--corrected-detail", type=Path, required=True)
    parser.add_argument("--corrected-report", type=Path, required=True)
    parser.add_argument("--history", type=Path, default=HISTORY_CSV)
    parser.add_argument("--latest", type=Path, default=LATEST_CSV)
    parser.add_argument("--docs", type=Path, default=DOCS_CSV)
    args = parser.parse_args(argv)
    errors = validate_paths(
        anomaly_registry_path=args.anomaly_registry,
        source_diff_path=args.source_diff,
        projection_v2_manifest_path=args.projection_v2_manifest,
        projection_v2_detail_path=args.projection_v2_detail,
        original_detail_path=args.original_detail,
        corrected_summary_path=args.corrected_summary,
        corrected_detail_path=args.corrected_detail,
        corrected_report_path=args.corrected_report,
        history_path=args.history,
        latest_path=args.latest,
        docs_path=args.docs,
    )
    if errors:
        print("revenue_unreacted_range corrected-chain operation diff validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1
    print("revenue_unreacted_range corrected-chain operation diff validation passed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
