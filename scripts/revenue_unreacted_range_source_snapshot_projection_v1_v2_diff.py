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
        "condition_variant_id": "",
        "stock_id": "",
        "original_episode_key": "",
        "original_episode_start_source_date": "",
        "original_episode_start_source_row_canonical_sha256": "",
        "original_qualifying_source_row_canonical_sha256s": "",
        "corrected_episode_key": "",
        "corrected_episode_start_source_date": "",
        "corrected_episode_start_source_row_canonical_sha256": "",
        "corrected_qualifying_source_row_canonical_sha256s": "",
        "mapping_overlap_count": 0,
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
            f"{prefix}_episode_start_source_date": "",
            f"{prefix}_episode_start_source_row_canonical_sha256": "",
            f"{prefix}_qualifying_source_row_canonical_sha256s": "",
        }
    return {
        f"{prefix}_episode_key": _value(row["episode_key"]),
        f"{prefix}_episode_start_source_date": _value(
            row["episode_start_source_date"]
        ),
        f"{prefix}_episode_start_source_row_canonical_sha256": _value(
            row["episode_start_source_row_canonical_sha256"]
        ),
        f"{prefix}_qualifying_source_row_canonical_sha256s": _value(
            row["qualifying_source_row_canonical_sha256s"]
        ),
    }


def _match_corrected_episode(
    original: pd.Series,
    corrected_group: pd.DataFrame,
) -> tuple[pd.Series | None, str, str, int]:
    exact = corrected_group.loc[
        corrected_group["episode_key"].map(_value).eq(_value(original["episode_key"]))
    ]
    if len(exact) == 1:
        overlap = len(
            _token_set(original["qualifying_source_row_canonical_sha256s"])
            & _token_set(exact.iloc[0]["qualifying_source_row_canonical_sha256s"])
        )
        return exact.iloc[0], "exact_episode_key_successor", "", overlap
    original_tokens = _token_set(original["qualifying_source_row_canonical_sha256s"])
    scored: list[tuple[int, int]] = []
    for index, candidate in corrected_group.iterrows():
        overlap = len(
            original_tokens
            & _token_set(candidate["qualifying_source_row_canonical_sha256s"])
        )
        if overlap:
            scored.append((overlap, index))
    if not scored:
        return None, "absent_after_repair", "no_shared_qualifying_source_row", 0
    best_overlap = max(score for score, _index in scored)
    winners = [index for score, index in scored if score == best_overlap]
    if len(winners) != 1:
        return (
            None,
            "ambiguous_qualifying_source_overlap",
            "ambiguous_equal_maximum_qualifying_source_overlap",
            best_overlap,
        )
    return (
        corrected_group.loc[winners[0]],
        "qualifying_source_overlap_successor",
        "",
        best_overlap,
    )


def _source_relation_rows(
    v1_detail: pd.DataFrame,
    v2_detail: pd.DataFrame,
    *,
    base: dict[str, object],
) -> list[dict[str, object]]:
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
    rows: list[dict[str, object]] = []
    matched_v2: set[str] = set()
    grouped_v2 = {
        key: group
        for key, group in v2_detail.groupby(
            ["condition_variant_id", "stock_id"], dropna=False, sort=False
        )
    }
    for _, original in v1_detail.sort_values("episode_key", kind="stable").iterrows():
        group_key = (
            _value(original["condition_variant_id"]),
            _value(original["stock_id"]),
        )
        corrected_group = grouped_v2.get(group_key, v2_detail.iloc[0:0])
        corrected, status, reason, overlap = _match_corrected_episode(
            original,
            corrected_group,
        )
        if corrected is not None:
            corrected_key = _value(corrected["episode_key"])
            if corrected_key in matched_v2:
                raise RuntimeError(
                    "multiple v1 episodes mapped to one corrected episode: "
                    f"{corrected_key}"
                )
            matched_v2.add(corrected_key)
        row = dict(base)
        row.update(
            {
                "record_type": "episode_relation",
                "relation_status": status,
                "absence_reason": reason,
                "condition_variant_id": group_key[0],
                "stock_id": group_key[1],
                "mapping_overlap_count": overlap,
                **_episode_payload("original", original),
                **_episode_payload("corrected", corrected),
            }
        )
        rows.append(row)
    for _, corrected in v2_detail.sort_values("episode_key", kind="stable").iterrows():
        corrected_key = _value(corrected["episode_key"])
        if corrected_key in matched_v2:
            continue
        row = dict(base)
        row.update(
            {
                "record_type": "episode_relation",
                "relation_status": "v2_only_successor",
                "absence_reason": "no_v1_predecessor_episode",
                "condition_variant_id": _value(corrected["condition_variant_id"]),
                "stock_id": _value(corrected["stock_id"]),
                **_episode_payload("corrected", corrected),
            }
        )
        rows.append(row)
    return rows


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
