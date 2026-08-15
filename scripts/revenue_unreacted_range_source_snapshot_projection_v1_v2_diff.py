from __future__ import annotations

from datetime import datetime
import hashlib
import json
from pathlib import Path
from zoneinfo import ZoneInfo

import pandas as pd


ROOT = Path(__file__).resolve().parents[1]
MODEL_ID = "revenue_unreacted_range"
ARTIFACT_ID = "revenue_unreacted_range_source_snapshot_projection_v1_v2_diff"
ARTIFACT_VERSION = "source_snapshot_projection_v1_v2_diff_v1_20260814"
HISTORY_CSV = (
    ROOT
    / "output/history/research/"
    "revenue_unreacted_range_source_snapshot_projection_v1_v2_diff_v1_20260814.csv"
)
LATEST_CSV = (
    ROOT
    / "output/latest/research_backtest/"
    "revenue_unreacted_range_source_snapshot_projection_v1_v2_diff_latest.csv"
)
DOCS_CSV = (
    ROOT
    / "docs/latest/"
    "revenue_unreacted_range_source_snapshot_projection_v1_v2_diff_latest.csv"
)
V1_ARTIFACT_VERSION = "source_snapshot_projection_v1_20260731"
V2_ARTIFACT_VERSION = "source_snapshot_projection_v2_20260814"
V1_MANIFEST_GIT_BLOB_SHA = "163f9874124fd3d1fd27f1d1564ac8ac1892e4a1"
V1_MANIFEST_GIT_BLOB_RAW_SHA256 = (
    "d2dde5a1f05bc2f15baf4d77f326a7ea90b481492178fa6d2fd6262bf316c79e"
)
V1_DETAIL_GIT_BLOB_SHA = "849f72c39588c47f1bfd2fe8acd96255087efdcb"
V1_DETAIL_GIT_BLOB_RAW_SHA256 = (
    "b9784e4df2d2eba2c511b1c87f4255a6485a1fe1d7ac67490802e396614ee49a"
)
V1_DETAIL_SEMANTIC_SHA256 = (
    "92c68810ac2b5718d714d450fe83bf23f2f3469fec5db0ae2753330950ab2cf5"
)
SOURCE_REPAIR_INPUT_HEAD_SHA = "8176fee986d1659896a681e89f99f0171c481b0a"
SOURCE_REPAIR_ARTIFACT_COMMIT_SHA = "7a9e981e2436af3dfc733905ec26b53f8cdd9f9e"
SOURCE_REPAIR_WORKFLOW_RUN_ID = "31799699472"
SOURCE_REPAIR_REPORT_GIT_BLOB_SHA = "f2d569b122e448f87e956cca771748946a9d7363"
SOURCE_REPAIR_REPORT_GIT_BLOB_RAW_SHA256 = (
    "77bf1a1d7ee16beae5e0b0a0eb97212088d7ef7ca883644cdcf39b59fea8d447"
)

RELATION_COLUMNS = (
    "generated_at",
    "model_id",
    "artifact_id",
    "artifact_version",
    "record_type",
    "relation_row_sha256",
    "relation_row_set_sha256",
    "relation_status",
    "absence_reason",
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
    "original_episode_key",
    "original_episode_number",
    "original_episode_start_source_date",
    "original_episode_start_source_row_canonical_sha256",
    "original_qualifying_source_row_canonical_sha256s",
    "original_episode_end_date",
    "original_episode_status",
    "corrected_episode_key",
    "corrected_episode_number",
    "corrected_episode_start_source_date",
    "corrected_episode_start_source_row_canonical_sha256",
    "corrected_qualifying_source_row_canonical_sha256s",
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
    "promotion_gate_status",
    "research_only",
    "formal_model_use_allowed",
    "approved_for_daily",
    "presentation_allowed",
    "production_change",
    "promotion_evidence_allowed",
    "ranking_consumption_allowed",
    "pdf_consumption_allowed",
)
ROW_HASH_EXCLUDED_COLUMNS = {
    "generated_at",
    "relation_row_sha256",
    "relation_row_set_sha256",
}
SOURCE_RELATION_COMPARE_COLUMNS = tuple(
    column
    for column in RELATION_COLUMNS
    if column
    not in {
        "generated_at",
        "relation_row_sha256",
        "relation_row_set_sha256",
    }
)
SHA256_PATTERN_LENGTH = 64


def _now_text() -> str:
    return datetime.now(ZoneInfo("Asia/Taipei")).strftime(
        "%Y-%m-%d %H:%M:%S Asia/Taipei"
    )


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


def canonical_frame_sha256(frame: pd.DataFrame) -> str:
    columns = list(frame.columns)
    rows = [
        {column: _value(row[column]) for column in columns}
        for _, row in frame.iterrows()
    ]
    return _canonical_json_sha256({"columns": columns, "rows": rows})


def _token_set(value: object) -> set[str]:
    return {token for token in _value(value).split("|") if token}


def _base_row(
    *,
    generated_at: str,
    v2_manifest_sha256: str,
    v2_detail_sha256: str,
) -> dict[str, object]:
    return {
        "generated_at": generated_at,
        "model_id": MODEL_ID,
        "artifact_id": ARTIFACT_ID,
        "artifact_version": ARTIFACT_VERSION,
        "record_type": "",
        "relation_row_sha256": "",
        "relation_row_set_sha256": "",
        "relation_status": "",
        "absence_reason": "",
        "relation_component_id": "",
        "relation_component_type": "",
        "relation_cardinality": "",
        "relation_component_original_count": 0,
        "relation_component_corrected_count": 0,
        "relation_component_edge_count": 0,
        "relation_component_original_episode_keys_json": "",
        "relation_component_corrected_episode_keys_json": "",
        "relation_component_original_start_date": "",
        "relation_component_original_end_date": "",
        "relation_component_corrected_start_date": "",
        "relation_component_corrected_end_date": "",
        "condition_variant_id": "",
        "stock_id": "",
        "original_episode_key": "",
        "original_episode_number": "",
        "original_episode_start_source_date": "",
        "original_episode_start_source_row_canonical_sha256": "",
        "original_qualifying_source_row_canonical_sha256s": "",
        "original_episode_end_date": "",
        "original_episode_status": "",
        "corrected_episode_key": "",
        "corrected_episode_number": "",
        "corrected_episode_start_source_date": "",
        "corrected_episode_start_source_row_canonical_sha256": "",
        "corrected_qualifying_source_row_canonical_sha256s": "",
        "corrected_episode_end_date": "",
        "corrected_episode_status": "",
        "mapping_role": "",
        "mapping_basis": "",
        "edge_overlap_source_row_canonical_sha256s": "",
        "edge_overlap_count": 0,
        "mapping_overlap_count": 0,
        "original_token_fully_contained": "",
        "corrected_token_fully_contained": "",
        "component_original_source_row_canonical_sha256s": "",
        "component_corrected_source_row_canonical_sha256s": "",
        "component_added_source_row_canonical_sha256s": "",
        "component_removed_source_row_canonical_sha256s": "",
        "component_original_token_union_sha256": "",
        "component_corrected_token_union_sha256": "",
        "component_added_token_set_sha256": "",
        "component_removed_token_set_sha256": "",
        "component_token_set_relation": "",
        "boundary_change_status": "",
        "projection_v1_manifest_git_blob_sha": V1_MANIFEST_GIT_BLOB_SHA,
        "projection_v1_manifest_git_blob_raw_sha256": (
            V1_MANIFEST_GIT_BLOB_RAW_SHA256
        ),
        "projection_v1_detail_git_blob_sha": V1_DETAIL_GIT_BLOB_SHA,
        "projection_v1_detail_git_blob_raw_sha256": V1_DETAIL_GIT_BLOB_RAW_SHA256,
        "projection_v1_detail_semantic_sha256": V1_DETAIL_SEMANTIC_SHA256,
        "projection_v2_manifest_canonical_sha256": v2_manifest_sha256,
        "projection_v2_detail_semantic_sha256": v2_detail_sha256,
        "source_repair_input_head_sha": SOURCE_REPAIR_INPUT_HEAD_SHA,
        "source_repair_artifact_commit_sha": SOURCE_REPAIR_ARTIFACT_COMMIT_SHA,
        "source_repair_workflow_run_id": SOURCE_REPAIR_WORKFLOW_RUN_ID,
        "source_repair_report_git_blob_sha": SOURCE_REPAIR_REPORT_GIT_BLOB_SHA,
        "source_repair_report_git_blob_raw_sha256": (
            SOURCE_REPAIR_REPORT_GIT_BLOB_RAW_SHA256
        ),
        "promotion_gate_status": "not_promotion_evidence_source_diff_only",
        "research_only": True,
        "formal_model_use_allowed": False,
        "approved_for_daily": False,
        "presentation_allowed": False,
        "production_change": False,
        "promotion_evidence_allowed": False,
        "ranking_consumption_allowed": False,
        "pdf_consumption_allowed": False,
    }


def _episode_payload(prefix: str, row: pd.Series | None) -> dict[str, str]:
    if row is None:
        return {
            f"{prefix}_episode_key": "",
            f"{prefix}_episode_number": "",
            f"{prefix}_episode_start_source_date": "",
            f"{prefix}_episode_start_source_row_canonical_sha256": "",
            f"{prefix}_qualifying_source_row_canonical_sha256s": "",
            f"{prefix}_episode_end_date": "",
            f"{prefix}_episode_status": "",
        }
    return {
        f"{prefix}_episode_key": _value(row["episode_key"]),
        f"{prefix}_episode_number": _value(row["episode_number"]),
        f"{prefix}_episode_start_source_date": _value(
            row["episode_start_source_date"]
        ),
        f"{prefix}_episode_start_source_row_canonical_sha256": _value(
            row["episode_start_source_row_canonical_sha256"]
        ),
        f"{prefix}_qualifying_source_row_canonical_sha256s": _value(
            row["qualifying_source_row_canonical_sha256s"]
        ),
        f"{prefix}_episode_end_date": _value(row["episode_end_date"]),
        f"{prefix}_episode_status": _value(row["episode_status"]),
    }


def _json_list(values: list[str]) -> str:
    return json.dumps(values, ensure_ascii=False, separators=(",", ":"))


def _token_text(tokens: set[str]) -> str:
    return "|".join(sorted(tokens))


def _token_set_sha256(tokens: set[str]) -> str:
    return _canonical_json_sha256(sorted(tokens))


def _episode_sort_key(row: pd.Series) -> tuple[str, int, str]:
    return (
        _value(row["episode_start_source_date"]),
        int(_value(row["episode_number"])),
        _value(row["episode_key"]),
    )


def _validate_episode_groups(
    frame: pd.DataFrame,
    label: str,
) -> dict[tuple[str, str], list[pd.Series]]:
    required = {
        "condition_variant_id",
        "stock_id",
        "episode_key",
        "episode_number",
        "episode_start_source_date",
        "episode_start_source_row_canonical_sha256",
        "qualifying_source_row_canonical_sha256s",
        "episode_end_date",
        "episode_status",
    }
    missing = sorted(required - set(frame.columns))
    if missing:
        raise RuntimeError(f"{label} missing relation columns: {missing}")
    if frame["episode_key"].map(_value).duplicated().any():
        raise RuntimeError(f"{label} episode_key must be unique")
    groups: dict[tuple[str, str], list[pd.Series]] = {}
    token_owners: dict[tuple[str, str], dict[str, str]] = {}
    for _, row in frame.iterrows():
        variant = _value(row["condition_variant_id"])
        stock_id = _value(row["stock_id"])
        episode_key = _value(row["episode_key"])
        if not variant or not stock_id or not episode_key:
            raise RuntimeError(f"{label} episode identity fields must be nonblank")
        try:
            episode_number = int(_value(row["episode_number"]))
        except ValueError as exc:
            raise RuntimeError(f"{label} episode_number must be an integer") from exc
        if episode_number <= 0:
            raise RuntimeError(f"{label} episode_number must be positive")
        start = _value(row["episode_start_source_date"])
        end = _value(row["episode_end_date"])
        try:
            start_date = datetime.strptime(start, "%Y%m%d")
            end_date = datetime.strptime(end, "%Y%m%d")
        except ValueError as exc:
            raise RuntimeError(f"{label} episode boundary date is invalid") from exc
        if start_date > end_date:
            raise RuntimeError(f"{label} episode start is after episode end")
        tokens = _token_set(row["qualifying_source_row_canonical_sha256s"])
        if not tokens:
            raise RuntimeError(f"{label} qualifying source token set must be nonempty")
        if any(
            len(token) != SHA256_PATTERN_LENGTH
            or any(character not in "0123456789abcdef" for character in token)
            for token in tokens
        ):
            raise RuntimeError(f"{label} qualifying source token is not SHA-256")
        group_key = (variant, stock_id)
        owners = token_owners.setdefault(group_key, {})
        for token in tokens:
            prior = owners.get(token)
            if prior is not None:
                raise RuntimeError(
                    f"{label} qualifying source token belongs to multiple episodes: "
                    f"{prior};{episode_key}"
                )
            owners[token] = episode_key
        groups.setdefault(group_key, []).append(row)
    for rows in groups.values():
        rows.sort(key=_episode_sort_key)
    return groups


def _assert_ordered_episode_sequence(
    rows: list[pd.Series],
    *,
    label: str,
) -> None:
    ordered = sorted(rows, key=_episode_sort_key)
    numbers = [int(_value(row["episode_number"])) for row in ordered]
    if numbers != list(range(numbers[0], numbers[0] + len(numbers))):
        raise RuntimeError(f"{label} episode numbers are not consecutive")
    for previous, current in zip(ordered, ordered[1:], strict=False):
        previous_end = datetime.strptime(_value(previous["episode_end_date"]), "%Y%m%d")
        current_start = datetime.strptime(
            _value(current["episode_start_source_date"]), "%Y%m%d"
        )
        if previous_end >= current_start:
            raise RuntimeError(f"{label} episode boundaries overlap or are unordered")


def _token_set_relation(original: set[str], corrected: set[str]) -> str:
    if original == corrected:
        return "token_sets_equal"
    if original < corrected:
        return "original_token_union_strict_subset_of_corrected"
    if corrected < original:
        return "corrected_token_union_strict_subset_of_original"
    if original & corrected:
        return "token_unions_partially_overlap"
    return "token_unions_disjoint"


def _component_rows(
    originals: list[pd.Series],
    corrected: list[pd.Series],
    edges: list[tuple[pd.Series, pd.Series, set[str]]],
    *,
    group_key: tuple[str, str],
    base: dict[str, object],
) -> list[dict[str, object]]:
    originals = sorted(originals, key=_episode_sort_key)
    corrected = sorted(corrected, key=_episode_sort_key)
    original_keys = [_value(row["episode_key"]) for row in originals]
    corrected_keys = [_value(row["episode_key"]) for row in corrected]
    original_union = set().union(
        *(
            _token_set(row["qualifying_source_row_canonical_sha256s"])
            for row in originals
        ),
        set(),
    )
    corrected_union = set().union(
        *(
            _token_set(row["qualifying_source_row_canonical_sha256s"])
            for row in corrected
        ),
        set(),
    )
    added = corrected_union - original_union
    removed = original_union - corrected_union
    original_count = len(originals)
    corrected_count = len(corrected)
    if original_count > 1 and corrected_count > 1:
        raise RuntimeError(
            "many-to-many source episode component is not an approved structural "
            f"relation: {group_key[0]}|{group_key[1]}|"
            f"{_json_list(original_keys)}|{_json_list(corrected_keys)}"
        )
    if original_count == 1 and corrected_count == 1:
        component_type = "one_to_one"
    elif original_count > 1 and corrected_count == 1:
        component_type = "many_v1_to_one_v2"
    elif original_count == 1 and corrected_count > 1:
        component_type = "one_v1_to_many_v2"
    elif original_count == 1 and corrected_count == 0:
        component_type = "v1_no_edge"
    elif original_count == 0 and corrected_count == 1:
        component_type = "v2_no_edge"
    else:
        raise RuntimeError("invalid source episode relation component cardinality")
    edge_keys = [
        {
            "original_episode_key": _value(original["episode_key"]),
            "corrected_episode_key": _value(successor["episode_key"]),
            "overlap_tokens": sorted(overlap),
        }
        for original, successor, overlap in sorted(
            edges,
            key=lambda edge: (
                _value(edge[0]["episode_key"]),
                _value(edge[1]["episode_key"]),
            ),
        )
    ]
    original_start = (
        min(_value(row["episode_start_source_date"]) for row in originals)
        if originals
        else ""
    )
    original_end = (
        max(_value(row["episode_end_date"]) for row in originals) if originals else ""
    )
    corrected_start = (
        min(_value(row["episode_start_source_date"]) for row in corrected)
        if corrected
        else ""
    )
    corrected_end = (
        max(_value(row["episode_end_date"]) for row in corrected) if corrected else ""
    )
    component_id = _canonical_json_sha256(
        {
            "condition_variant_id": group_key[0],
            "stock_id": group_key[1],
            "component_type": component_type,
            "original_episode_keys": original_keys,
            "corrected_episode_keys": corrected_keys,
            "edges": edge_keys,
            "original_token_union": sorted(original_union),
            "corrected_token_union": sorted(corrected_union),
            "original_start_date": original_start,
            "original_end_date": original_end,
            "corrected_start_date": corrected_start,
            "corrected_end_date": corrected_end,
        }
    )
    if component_type == "many_v1_to_one_v2":
        _assert_ordered_episode_sequence(originals, label="v1 merge predecessor")
        successor = corrected[0]
        if any(
            not _token_set(row["qualifying_source_row_canonical_sha256s"])
            <= _token_set(successor["qualifying_source_row_canonical_sha256s"])
            for row in originals
        ):
            raise RuntimeError("v1 merge predecessor token set is not contained in successor")
        anchor = originals[0]
        if any(
            _value(anchor[column]) != _value(successor[column])
            for column in (
                "episode_key",
                "episode_start_source_date",
                "episode_start_source_row_canonical_sha256",
            )
        ):
            raise RuntimeError("v1 merge successor is not anchored to earliest predecessor")
        if _value(successor["episode_end_date"]) < max(
            _value(row["episode_end_date"]) for row in originals
        ):
            raise RuntimeError("v1 merge successor does not cover predecessor boundaries")
        boundary_status = "episode_boundaries_merged_after_price_repair"
    elif component_type == "one_v1_to_many_v2":
        _assert_ordered_episode_sequence(corrected, label="v2 split successor")
        predecessor = originals[0]
        anchor = corrected[0]
        if any(
            _value(predecessor[column]) != _value(anchor[column])
            for column in (
                "episode_key",
                "episode_start_source_date",
                "episode_start_source_row_canonical_sha256",
            )
        ):
            raise RuntimeError("v2 split is not anchored to original predecessor")
        if _value(predecessor["episode_end_date"]) < max(
            _value(row["episode_end_date"]) for row in corrected
        ):
            raise RuntimeError("v2 split successors exceed original episode boundary")
        boundary_status = "episode_boundary_split_after_price_repair"
    elif component_type == "one_to_one":
        boundary_status = (
            "episode_boundary_preserved"
            if all(
                _value(originals[0][column]) == _value(corrected[0][column])
                for column in (
                    "episode_key",
                    "episode_start_source_date",
                    "episode_end_date",
                )
            )
            else "episode_boundary_changed_after_price_repair"
        )
    elif component_type == "v1_no_edge":
        boundary_status = "original_episode_absent_after_price_repair"
    else:
        boundary_status = "new_corrected_episode_after_price_repair"
    component = {
        "relation_component_id": component_id,
        "relation_component_type": component_type,
        "relation_cardinality": f"{original_count}:{corrected_count}",
        "relation_component_original_count": original_count,
        "relation_component_corrected_count": corrected_count,
        "relation_component_edge_count": len(edges),
        "relation_component_original_episode_keys_json": _json_list(original_keys),
        "relation_component_corrected_episode_keys_json": _json_list(corrected_keys),
        "relation_component_original_start_date": original_start,
        "relation_component_original_end_date": original_end,
        "relation_component_corrected_start_date": corrected_start,
        "relation_component_corrected_end_date": corrected_end,
        "component_original_source_row_canonical_sha256s": _token_text(original_union),
        "component_corrected_source_row_canonical_sha256s": _token_text(corrected_union),
        "component_added_source_row_canonical_sha256s": _token_text(added),
        "component_removed_source_row_canonical_sha256s": _token_text(removed),
        "component_original_token_union_sha256": _token_set_sha256(original_union),
        "component_corrected_token_union_sha256": _token_set_sha256(corrected_union),
        "component_added_token_set_sha256": _token_set_sha256(added),
        "component_removed_token_set_sha256": _token_set_sha256(removed),
        "component_token_set_relation": _token_set_relation(
            original_union, corrected_union
        ),
        "boundary_change_status": boundary_status,
    }
    relation_rows: list[dict[str, object]] = []
    edge_iterable: list[tuple[pd.Series | None, pd.Series | None, set[str]]]
    if edges:
        edge_iterable = [(left, right, overlap) for left, right, overlap in edges]
    else:
        edge_iterable = [(originals[0] if originals else None, corrected[0] if corrected else None, set())]
    for original, successor, overlap in edge_iterable:
        original_key = _value(original["episode_key"]) if original is not None else ""
        corrected_key = _value(successor["episode_key"]) if successor is not None else ""
        if component_type == "one_to_one":
            exact = original_key == corrected_key
            status = (
                "exact_episode_key_successor"
                if exact
                else "qualifying_source_overlap_successor"
            )
            mapping_role = "exact_key_anchor" if exact else "unique_overlap_successor"
            mapping_basis = (
                "exact_episode_key_with_token_overlap"
                if exact
                else "unique_qualifying_source_token_overlap"
            )
            absence_reason = ""
        elif component_type == "many_v1_to_one_v2":
            status = "many_to_one_merged_successor"
            mapping_role = (
                "exact_key_anchor" if original_key == corrected_key else "merge_member"
            )
            mapping_basis = "many_to_one_component_token_overlap"
            absence_reason = ""
        elif component_type == "one_v1_to_many_v2":
            status = "one_to_many_split_successor"
            mapping_role = (
                "exact_key_anchor" if original_key == corrected_key else "split_member"
            )
            mapping_basis = "one_to_many_component_token_overlap"
            absence_reason = ""
        elif component_type == "v1_no_edge":
            status = "absent_after_repair"
            mapping_role = "original_without_corrected_edge"
            mapping_basis = "no_shared_qualifying_source_row"
            absence_reason = "no_shared_qualifying_source_row"
        else:
            status = "v2_only_successor"
            mapping_role = "corrected_without_original_edge"
            mapping_basis = "no_v1_predecessor_episode"
            absence_reason = "no_v1_predecessor_episode"
        original_tokens = (
            _token_set(original["qualifying_source_row_canonical_sha256s"])
            if original is not None
            else set()
        )
        corrected_tokens = (
            _token_set(successor["qualifying_source_row_canonical_sha256s"])
            if successor is not None
            else set()
        )
        row = dict(base)
        row.update(
            {
                "record_type": "episode_relation",
                "relation_status": status,
                "absence_reason": absence_reason,
                "condition_variant_id": group_key[0],
                "stock_id": group_key[1],
                "mapping_role": mapping_role,
                "mapping_basis": mapping_basis,
                "edge_overlap_source_row_canonical_sha256s": _token_text(overlap),
                "edge_overlap_count": len(overlap),
                "mapping_overlap_count": len(overlap),
                "original_token_fully_contained": (
                    original_tokens <= corrected_tokens
                    if original is not None and successor is not None
                    else ""
                ),
                "corrected_token_fully_contained": (
                    corrected_tokens <= original_tokens
                    if original is not None and successor is not None
                    else ""
                ),
                **component,
                **_episode_payload("original", original),
                **_episode_payload("corrected", successor),
            }
        )
        relation_rows.append(row)
    return relation_rows


def _source_relation_rows(
    v1_detail: pd.DataFrame,
    v2_detail: pd.DataFrame,
    *,
    base: dict[str, object],
) -> list[dict[str, object]]:
    v1_groups = _validate_episode_groups(v1_detail, "v1 detail")
    v2_groups = _validate_episode_groups(v2_detail, "v2 detail")
    v1_key_groups = {
        _value(row["episode_key"]): key
        for key, group in v1_groups.items()
        for row in group
    }
    v2_key_groups = {
        _value(row["episode_key"]): key
        for key, group in v2_groups.items()
        for row in group
    }
    for episode_key in sorted(set(v1_key_groups) & set(v2_key_groups)):
        if v1_key_groups[episode_key] != v2_key_groups[episode_key]:
            raise RuntimeError(
                "same episode_key changed stock or condition variant: "
                f"{episode_key}"
            )
    relation_rows: list[dict[str, object]] = []
    for group_key in sorted(set(v1_groups) | set(v2_groups)):
        originals = v1_groups.get(group_key, [])
        corrected = v2_groups.get(group_key, [])
        original_by_key = {_value(row["episode_key"]): row for row in originals}
        corrected_by_key = {_value(row["episode_key"]): row for row in corrected}
        for episode_key in sorted(set(original_by_key) & set(corrected_by_key)):
            if not (
                _token_set(
                    original_by_key[episode_key][
                        "qualifying_source_row_canonical_sha256s"
                    ]
                )
                & _token_set(
                    corrected_by_key[episode_key][
                        "qualifying_source_row_canonical_sha256s"
                    ]
                )
            ):
                raise RuntimeError(
                    "exact episode_key has contradictory qualifying source tokens: "
                    f"{episode_key}"
                )
        nodes = {
            **{("v1", key): row for key, row in original_by_key.items()},
            **{("v2", key): row for key, row in corrected_by_key.items()},
        }
        adjacency: dict[tuple[str, str], set[tuple[str, str]]] = {
            node: set() for node in nodes
        }
        edge_overlap: dict[tuple[str, str], set[str]] = {}
        for original_key, original in original_by_key.items():
            original_tokens = _token_set(
                original["qualifying_source_row_canonical_sha256s"]
            )
            for corrected_key, successor in corrected_by_key.items():
                overlap = original_tokens & _token_set(
                    successor["qualifying_source_row_canonical_sha256s"]
                )
                if not overlap:
                    continue
                adjacency[("v1", original_key)].add(("v2", corrected_key))
                adjacency[("v2", corrected_key)].add(("v1", original_key))
                edge_overlap[(original_key, corrected_key)] = overlap
        visited: set[tuple[str, str]] = set()
        for initial in sorted(nodes):
            if initial in visited:
                continue
            stack = [initial]
            visited.add(initial)
            component_nodes: list[tuple[str, str]] = []
            while stack:
                node = stack.pop()
                component_nodes.append(node)
                for neighbor in sorted(adjacency[node]):
                    if neighbor not in visited:
                        visited.add(neighbor)
                        stack.append(neighbor)
            component_originals = [
                nodes[node] for node in component_nodes if node[0] == "v1"
            ]
            component_corrected = [
                nodes[node] for node in component_nodes if node[0] == "v2"
            ]
            component_edges = [
                (
                    original_by_key[original_key],
                    corrected_by_key[corrected_key],
                    overlap,
                )
                for (original_key, corrected_key), overlap in edge_overlap.items()
                if ("v1", original_key) in component_nodes
                and ("v2", corrected_key) in component_nodes
            ]
            relation_rows.extend(
                _component_rows(
                    component_originals,
                    component_corrected,
                    component_edges,
                    group_key=group_key,
                    base=base,
                )
            )
    return relation_rows


def _attach_relation_hashes(frame: pd.DataFrame) -> pd.DataFrame:
    payload_columns = [
        column for column in RELATION_COLUMNS if column not in ROW_HASH_EXCLUDED_COLUMNS
    ]
    result = frame.copy()
    result["relation_row_sha256"] = [
        _canonical_json_sha256(
            {column: _value(row[column]) for column in payload_columns}
        )
        for _, row in result.iterrows()
    ]
    if result["relation_row_sha256"].duplicated().any():
        raise RuntimeError("v1/v2 diff relation row SHA-256 must be unique")
    row_set_sha = _canonical_json_sha256(
        sorted(result["relation_row_sha256"].map(_value).unique().tolist())
    )
    result["relation_row_set_sha256"] = row_set_sha
    return result


def build_projection_v1_v2_diff(
    v1_manifest: pd.DataFrame,
    v1_detail: pd.DataFrame,
    v2_manifest: pd.DataFrame,
    v2_detail: pd.DataFrame,
    *,
    generated_at: str | None = None,
) -> pd.DataFrame:
    for frame, label, version in (
        (v1_manifest, "v1 manifest", V1_ARTIFACT_VERSION),
        (v2_manifest, "v2 manifest", V2_ARTIFACT_VERSION),
    ):
        if len(frame) != 1 or "artifact_version" not in frame.columns:
            raise RuntimeError(f"{label} must contain exactly one versioned row")
        if _value(frame.iloc[0]["artifact_version"]) != version:
            raise RuntimeError(f"{label} artifact_version mismatch")
    v2_detail_sha = _value(v2_manifest.iloc[0]["projected_episode_semantic_sha256"])
    if len(v2_detail_sha) != SHA256_PATTERN_LENGTH:
        raise RuntimeError("v2 manifest projected detail semantic SHA-256 is invalid")
    base = _base_row(
        generated_at=generated_at or _now_text(),
        v2_manifest_sha256=canonical_frame_sha256(v2_manifest),
        v2_detail_sha256=v2_detail_sha,
    )
    rows = _source_relation_rows(v1_detail, v2_detail, base=base)
    frame = pd.DataFrame(rows, columns=list(RELATION_COLUMNS))
    sort_columns = [
        "record_type",
        "original_episode_key",
        "corrected_episode_key",
    ]
    frame = frame.sort_values(sort_columns, kind="stable").reset_index(drop=True)
    return _attach_relation_hashes(frame).loc[:, list(RELATION_COLUMNS)]


def write_projection_v1_v2_diff(
    frame: pd.DataFrame,
    *,
    history_path: Path = HISTORY_CSV,
    latest_path: Path = LATEST_CSV,
    docs_path: Path = DOCS_CSV,
) -> None:
    if list(frame.columns) != list(RELATION_COLUMNS) or frame.empty:
        raise RuntimeError("v1/v2 diff frame is empty or has an invalid schema")
    payload = frame.to_csv(index=False).encode("utf-8")
    for path in (history_path, latest_path, docs_path):
        path = Path(path)
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(payload)
