from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import re
import sys

import pandas as pd


ROOT = Path(__file__).resolve().parents[1]
MODEL_ID = "revenue_unreacted_range"
ARTIFACT_ID = "revenue_unreacted_range_source_snapshot_projection_v1_v2_diff"
ARTIFACT_VERSION = "source_snapshot_projection_v1_v2_diff_v1_20260814"
V1_ARTIFACT_VERSION = "source_snapshot_projection_v1_20260731"
V2_ARTIFACT_VERSION = "source_snapshot_projection_v2_20260814"
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
CANONICAL_JSON_VERSION = "revenue_source_snapshot_projection_canonical_json_v1"
PROJECTED_CAPTURE_LINEAGE_COLUMNS = (
    "monthly_revenue_history_blob_sha256",
    "cross_market_resolution_registry_canonical_sha256",
)
SHA256_PATTERN = re.compile(r"^[0-9a-f]{64}$")

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
    "condition_variant_id",
    "stock_id",
    "original_episode_key",
    "original_episode_start_source_date",
    "original_episode_start_source_row_canonical_sha256",
    "original_qualifying_source_row_canonical_sha256s",
    "corrected_episode_key",
    "corrected_episode_start_source_date",
    "corrected_episode_start_source_row_canonical_sha256",
    "corrected_qualifying_source_row_canonical_sha256s",
    "mapping_overlap_count",
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


def _projection_canonical_json_sha256(payload: object) -> str:
    return hashlib.sha256(
        json.dumps(payload, ensure_ascii=False, separators=(",", ":")).encode(
            "utf-8"
        )
    ).hexdigest()


def _canonical_frame_sha256(frame: pd.DataFrame) -> str:
    columns = list(frame.columns)
    rows = [
        {column: _value(row[column]) for column in columns}
        for _, row in frame.iterrows()
    ]
    return _canonical_json_sha256({"columns": columns, "rows": rows})


def _projected_source_detail_sha256(frame: pd.DataFrame) -> str:
    selected = [
        column
        for column in frame.columns
        if column not in ("generated_at", *PROJECTED_CAPTURE_LINEAGE_COLUMNS)
    ]
    rows = [
        [_value(value) for value in row]
        for row in frame.loc[:, selected].itertuples(index=False, name=None)
    ]
    rows.sort()
    return _projection_canonical_json_sha256(
        [CANONICAL_JSON_VERSION, selected, rows]
    )


def _token_set(value: object) -> set[str]:
    return {token for token in _value(value).split("|") if token}


def _match_corrected_episode(
    original: pd.Series,
    corrected_group: pd.DataFrame,
) -> tuple[pd.Series | None, str, str, int]:
    exact = corrected_group.loc[
        corrected_group["episode_key"].map(_value).eq(_value(original["episode_key"]))
    ]
    if len(exact) == 1:
        return (
            exact.iloc[0],
            "exact_episode_key_successor",
            "",
            len(
                _token_set(original["qualifying_source_row_canonical_sha256s"])
                & _token_set(exact.iloc[0]["qualifying_source_row_canonical_sha256s"])
            ),
        )
    original_tokens = _token_set(original["qualifying_source_row_canonical_sha256s"])
    scored = [
        (
            len(
                original_tokens
                & _token_set(candidate["qualifying_source_row_canonical_sha256s"])
            ),
            index,
        )
        for index, candidate in corrected_group.iterrows()
    ]
    scored = [(score, index) for score, index in scored if score]
    if not scored:
        return None, "absent_after_repair", "no_shared_qualifying_source_row", 0
    best = max(score for score, _index in scored)
    winners = [index for score, index in scored if score == best]
    if len(winners) != 1:
        return (
            None,
            "ambiguous_qualifying_source_overlap",
            "ambiguous_equal_maximum_qualifying_source_overlap",
            best,
        )
    return (
        corrected_group.loc[winners[0]],
        "qualifying_source_overlap_successor",
        "",
        best,
    )


def _expected_episode_relations(
    v1_detail: pd.DataFrame,
    v2_detail: pd.DataFrame,
) -> list[dict[str, str]]:
    required = {
        "condition_variant_id",
        "stock_id",
        "episode_key",
        "episode_start_source_date",
        "episode_start_source_row_canonical_sha256",
        "qualifying_source_row_canonical_sha256s",
    }
    for frame, label in ((v1_detail, "v1 detail"), (v2_detail, "v2 detail")):
        missing = sorted(required - set(frame.columns))
        if missing:
            raise RuntimeError(f"{label} missing relation columns: {missing}")
        if frame["episode_key"].map(_value).duplicated().any():
            raise RuntimeError(f"{label} episode_key must be unique")
    grouped_v2 = {
        key: group
        for key, group in v2_detail.groupby(
            ["condition_variant_id", "stock_id"], dropna=False, sort=False
        )
    }
    matched: set[str] = set()
    expected: list[dict[str, str]] = []
    for _, original in v1_detail.sort_values("episode_key", kind="stable").iterrows():
        key = (
            _value(original["condition_variant_id"]),
            _value(original["stock_id"]),
        )
        corrected, status, reason, overlap = _match_corrected_episode(
            original,
            grouped_v2.get(key, v2_detail.iloc[0:0]),
        )
        corrected_key = _value(corrected["episode_key"]) if corrected is not None else ""
        if corrected_key:
            if corrected_key in matched:
                raise RuntimeError(f"corrected episode has multiple predecessors: {corrected_key}")
            matched.add(corrected_key)
        expected.append(
            {
                "condition_variant_id": key[0],
                "stock_id": key[1],
                "original_episode_key": _value(original["episode_key"]),
                "original_episode_start_source_date": _value(
                    original["episode_start_source_date"]
                ),
                "original_episode_start_source_row_canonical_sha256": _value(
                    original["episode_start_source_row_canonical_sha256"]
                ),
                "original_qualifying_source_row_canonical_sha256s": _value(
                    original["qualifying_source_row_canonical_sha256s"]
                ),
                "corrected_episode_key": corrected_key,
                "corrected_episode_start_source_date": (
                    _value(corrected["episode_start_source_date"])
                    if corrected is not None
                    else ""
                ),
                "corrected_episode_start_source_row_canonical_sha256": (
                    _value(corrected["episode_start_source_row_canonical_sha256"])
                    if corrected is not None
                    else ""
                ),
                "corrected_qualifying_source_row_canonical_sha256s": (
                    _value(corrected["qualifying_source_row_canonical_sha256s"])
                    if corrected is not None
                    else ""
                ),
                "mapping_overlap_count": str(overlap),
                "relation_status": status,
                "absence_reason": reason,
            }
        )
    for _, corrected in v2_detail.sort_values("episode_key", kind="stable").iterrows():
        corrected_key = _value(corrected["episode_key"])
        if corrected_key in matched:
            continue
        expected.append(
            {
                "condition_variant_id": _value(corrected["condition_variant_id"]),
                "stock_id": _value(corrected["stock_id"]),
                "original_episode_key": "",
                "original_episode_start_source_date": "",
                "original_episode_start_source_row_canonical_sha256": "",
                "original_qualifying_source_row_canonical_sha256s": "",
                "corrected_episode_key": corrected_key,
                "corrected_episode_start_source_date": _value(
                    corrected["episode_start_source_date"]
                ),
                "corrected_episode_start_source_row_canonical_sha256": _value(
                    corrected["episode_start_source_row_canonical_sha256"]
                ),
                "corrected_qualifying_source_row_canonical_sha256s": _value(
                    corrected["qualifying_source_row_canonical_sha256s"]
                ),
                "mapping_overlap_count": "0",
                "relation_status": "v2_only_successor",
                "absence_reason": "no_v1_predecessor_episode",
            }
        )
    return expected


def _normalize_relation_payload(frame: pd.DataFrame, columns: list[str]) -> list[tuple[str, ...]]:
    return sorted(
        tuple(_value(value) for value in row)
        for row in frame.loc[:, columns].itertuples(index=False, name=None)
    )


def validate_frames(
    v1_manifest: pd.DataFrame,
    v1_detail: pd.DataFrame,
    v2_manifest: pd.DataFrame,
    v2_detail: pd.DataFrame,
    diff: pd.DataFrame,
) -> list[str]:
    errors: list[str] = []
    if list(diff.columns) != list(RELATION_COLUMNS):
        return ["v1/v2 diff schema mismatch"]
    if diff.empty:
        return ["v1/v2 diff is empty"]
    for manifest, label, version in (
        (v1_manifest, "v1 manifest", V1_ARTIFACT_VERSION),
        (v2_manifest, "v2 manifest", V2_ARTIFACT_VERSION),
    ):
        if len(manifest) != 1 or "artifact_version" not in manifest.columns:
            errors.append(f"{label} must contain exactly one versioned row")
        elif _value(manifest.iloc[0]["artifact_version"]) != version:
            errors.append(f"{label} artifact_version mismatch")
    if errors:
        return errors
    v1_detail_sha = _projected_source_detail_sha256(v1_detail)
    v2_detail_sha = _projected_source_detail_sha256(v2_detail)
    if v1_detail_sha != V1_DETAIL_SEMANTIC_SHA256:
        errors.append("v1 detail semantic SHA-256 does not match pinned predecessor")
    if v2_detail_sha != _value(
        v2_manifest.iloc[0].get("projected_episode_semantic_sha256", "")
    ):
        errors.append("v2 detail semantic SHA-256 is not bound to v2 manifest")
    constants = {
        "model_id": MODEL_ID,
        "artifact_id": ARTIFACT_ID,
        "artifact_version": ARTIFACT_VERSION,
        "projection_v1_manifest_git_blob_sha": V1_MANIFEST_GIT_BLOB_SHA,
        "projection_v1_manifest_git_blob_raw_sha256": V1_MANIFEST_GIT_BLOB_RAW_SHA256,
        "projection_v1_detail_git_blob_sha": V1_DETAIL_GIT_BLOB_SHA,
        "projection_v1_detail_git_blob_raw_sha256": V1_DETAIL_GIT_BLOB_RAW_SHA256,
        "projection_v1_detail_semantic_sha256": V1_DETAIL_SEMANTIC_SHA256,
        "projection_v2_manifest_canonical_sha256": _canonical_frame_sha256(v2_manifest),
        "projection_v2_detail_semantic_sha256": v2_detail_sha,
        "source_repair_input_head_sha": SOURCE_REPAIR_INPUT_HEAD_SHA,
        "source_repair_artifact_commit_sha": SOURCE_REPAIR_ARTIFACT_COMMIT_SHA,
        "source_repair_workflow_run_id": SOURCE_REPAIR_WORKFLOW_RUN_ID,
        "source_repair_report_git_blob_sha": SOURCE_REPAIR_REPORT_GIT_BLOB_SHA,
        "source_repair_report_git_blob_raw_sha256": SOURCE_REPAIR_REPORT_GIT_BLOB_RAW_SHA256,
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
    for column, expected in constants.items():
        values = set(diff[column].map(_value))
        if values != {expected}:
            errors.append(f"v1/v2 diff {column} mismatch: {sorted(values)}/{expected}")
    payload_columns = [
        column for column in RELATION_COLUMNS if column not in ROW_HASH_EXCLUDED_COLUMNS
    ]
    expected_row_hashes = [
        _canonical_json_sha256(
            {column: _value(row[column]) for column in payload_columns}
        )
        for _, row in diff.iterrows()
    ]
    actual_row_hashes = diff["relation_row_sha256"].map(_value).tolist()
    if actual_row_hashes != expected_row_hashes:
        errors.append("v1/v2 diff relation_row_sha256 mismatch")
    if len(set(actual_row_hashes)) != len(actual_row_hashes):
        errors.append("v1/v2 diff relation_row_sha256 must be unique")
    expected_set_sha = _canonical_json_sha256(sorted(set(expected_row_hashes)))
    if set(diff["relation_row_set_sha256"].map(_value)) != {expected_set_sha}:
        errors.append("v1/v2 diff relation_row_set_sha256 mismatch")
    episode = diff.loc[diff["record_type"].map(_value).eq("episode_relation")]
    if set(diff["record_type"].map(_value)) != {"episode_relation"}:
        errors.append("v1/v2 diff record_type set mismatch")
    try:
        expected_episode = pd.DataFrame(_expected_episode_relations(v1_detail, v2_detail))
        compare_columns = list(expected_episode.columns)
        if _normalize_relation_payload(episode, compare_columns) != _normalize_relation_payload(
            expected_episode, compare_columns
        ):
            errors.append("v1/v2 diff episode successor mapping mismatch")
    except (KeyError, RuntimeError, ValueError) as exc:
        errors.append(str(exc))
    return errors


def _read_csv(path: Path, *, stock_id: bool = False) -> pd.DataFrame:
    if not Path(path).is_file():
        raise RuntimeError(f"missing required v1/v2 diff input: {path}")
    return pd.read_csv(
        path,
        dtype={"stock_id": str} if stock_id else str,
        keep_default_na=False,
        low_memory=False,
    )


def validate_paths(
    *,
    v1_manifest_path: Path,
    v1_detail_path: Path,
    v2_manifest_path: Path,
    v2_detail_path: Path,
    history_path: Path = HISTORY_CSV,
    latest_path: Path = LATEST_CSV,
    docs_path: Path = DOCS_CSV,
) -> list[str]:
    for path in (v1_manifest_path, v1_detail_path, v2_manifest_path, v2_detail_path):
        if not Path(path).is_file():
            return [f"missing required versioned projection input: {path}"]
    payloads = []
    for path in (history_path, latest_path, docs_path):
        if not Path(path).is_file():
            return [f"missing v1/v2 diff mirror: {path}"]
        payloads.append(Path(path).read_bytes())
    errors: list[str] = []
    if len(set(payloads)) != 1:
        errors.append("v1/v2 diff three mirrors are not byte-identical")
    if hashlib.sha256(Path(v1_manifest_path).read_bytes()).hexdigest() != (
        V1_MANIFEST_GIT_BLOB_RAW_SHA256
    ):
        errors.append("versioned v1 manifest bytes do not match pinned Git blob")
    if hashlib.sha256(Path(v1_detail_path).read_bytes()).hexdigest() != (
        V1_DETAIL_GIT_BLOB_RAW_SHA256
    ):
        errors.append("versioned v1 detail bytes do not match pinned Git blob")
    errors.extend(
        validate_frames(
            _read_csv(v1_manifest_path),
            _read_csv(v1_detail_path, stock_id=True),
            _read_csv(v2_manifest_path),
            _read_csv(v2_detail_path, stock_id=True),
            _read_csv(history_path, stock_id=True),
        )
    )
    return errors


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--v1-manifest", type=Path, required=True)
    parser.add_argument("--v1-detail", type=Path, required=True)
    parser.add_argument("--v2-manifest", type=Path, required=True)
    parser.add_argument("--v2-detail", type=Path, required=True)
    parser.add_argument("--history", type=Path, default=HISTORY_CSV)
    parser.add_argument("--latest", type=Path, default=LATEST_CSV)
    parser.add_argument("--docs", type=Path, default=DOCS_CSV)
    args = parser.parse_args(argv)
    errors = validate_paths(
        v1_manifest_path=args.v1_manifest,
        v1_detail_path=args.v1_detail,
        v2_manifest_path=args.v2_manifest,
        v2_detail_path=args.v2_detail,
        history_path=args.history,
        latest_path=args.latest,
        docs_path=args.docs,
    )
    if errors:
        print("revenue_unreacted_range projection v1/v2 diff validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1
    print("revenue_unreacted_range projection v1/v2 diff validation passed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
