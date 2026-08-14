from __future__ import annotations

from datetime import datetime
from decimal import Decimal, InvalidOperation
import hashlib
import io
import json
import os
from pathlib import Path
import tempfile
from zoneinfo import ZoneInfo

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
SHA256_LENGTH = 64

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
        io.BytesIO(payload),
        dtype=str,
        keep_default_na=False,
        low_memory=False,
    )


def _require_columns(frame: pd.DataFrame, required: set[str], label: str) -> None:
    missing = sorted(required - set(frame.columns))
    if missing:
        raise RuntimeError(f"{label} missing required columns: {missing}")
    if frame.empty:
        raise RuntimeError(f"{label} must not be empty")


def _single_value(frame: pd.DataFrame, column: str, label: str) -> str:
    values = set(frame[column].map(_value))
    if len(values) != 1 or "" in values:
        raise RuntimeError(f"{label} {column} must have one non-empty value")
    return next(iter(values))


def _require_sha256(value: object, label: str) -> str:
    text = _value(value).lower()
    if len(text) != SHA256_LENGTH or any(ch not in "0123456789abcdef" for ch in text):
        raise RuntimeError(f"{label} must be a lowercase SHA-256")
    return text


def _require_git_sha(value: object, label: str) -> str:
    text = _value(value).lower()
    if len(text) != 40 or any(ch not in "0123456789abcdef" for ch in text):
        raise RuntimeError(f"{label} must be a 40-character Git SHA")
    return text


def _require_date(value: object, label: str) -> str:
    text = _value(value)
    try:
        datetime.strptime(text, "%Y%m%d")
    except ValueError as exc:
        raise RuntimeError(f"{label} must be YYYYMMDD") from exc
    return text


def _require_positive_decimal(value: object, label: str) -> Decimal:
    try:
        number = Decimal(_value(value))
    except InvalidOperation as exc:
        raise RuntimeError(f"{label} must be numeric") from exc
    if not number.is_finite() or number <= 0:
        raise RuntimeError(f"{label} must be a positive finite price")
    return number


def _original_detail_context(
    original_detail: pd.DataFrame,
    originals: pd.DataFrame,
) -> tuple[dict[str, str], dict[tuple[str, str], pd.Series]]:
    required = {
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
    }
    _require_columns(original_detail, required, "original low/mid detail")
    if _single_value(original_detail, "model_id", "original detail") != MODEL_ID:
        raise RuntimeError("original detail model_id mismatch")
    source_pairs = {
        (
            _value(row["operation_key"]),
            _value(row["candidate_detail_row_sha256"]),
        )
        for _, row in originals.iterrows()
    }
    indexed: dict[tuple[str, str], pd.Series] = {}
    for pair in source_pairs:
        matches = original_detail.loc[
            original_detail["operation_key"].map(_value).eq(pair[0])
            & original_detail["candidate_detail_row_sha256"].map(_value).eq(pair[1])
        ]
        if len(matches) != 1:
            raise RuntimeError(
                "original source-diff pair must bind exactly one original detail row: "
                f"{pair[0]}"
            )
        row = matches.iloc[0]
        entry_date = _require_date(row["entry_date"], "original entry_date")
        exit_date = _require_date(row["exit_date"], "original exit_date")
        if entry_date > exit_date:
            raise RuntimeError("original entry_date must not follow exit_date")
        _require_positive_decimal(row["entry_price"], "original entry_price")
        _require_positive_decimal(row["exit_price"], "original exit_price")
        if not _value(row["stock_id"]):
            raise RuntimeError("original stock_id must not be empty")
        indexed[pair] = row
    return (
        {
            "original_low_mid_detail_artifact_id": _single_value(
                original_detail, "artifact_id", "original detail"
            ),
            "original_low_mid_detail_artifact_version": _single_value(
                original_detail, "artifact_version", "original detail"
            ),
            "original_low_mid_detail_canonical_sha256": canonical_frame_sha256(
                original_detail
            ),
        },
        indexed,
    )


def _source_diff_context(
    source_diff: pd.DataFrame,
) -> dict[str, str]:
    required = {
        "artifact_version",
        "record_type",
        "relation_row_sha256",
        "relation_row_set_sha256",
        "relation_status",
        "absence_reason",
        "original_episode_key",
        "corrected_episode_key",
        "original_episode_start_source_row_canonical_sha256",
        "corrected_episode_start_source_row_canonical_sha256",
        "original_qualifying_source_row_canonical_sha256s",
        "corrected_qualifying_source_row_canonical_sha256s",
        *SOURCE_LINEAGE_COLUMNS,
    }
    _require_columns(source_diff, required, "source projection v1/v2 diff")
    if _single_value(source_diff, "artifact_version", "source diff") != (
        SOURCE_DIFF_ARTIFACT_VERSION
    ):
        raise RuntimeError("source diff artifact_version mismatch")
    payload_columns = [
        column
        for column in source_diff.columns
        if column not in {"generated_at", "relation_row_sha256", "relation_row_set_sha256"}
    ]
    expected_row_hashes = [
        _canonical_json_sha256(
            {column: _value(row[column]) for column in payload_columns}
        )
        for _, row in source_diff.iterrows()
    ]
    actual_row_hashes = source_diff["relation_row_sha256"].map(_value).tolist()
    if actual_row_hashes != expected_row_hashes:
        raise RuntimeError("source diff relation_row_sha256 mismatch")
    if len(set(actual_row_hashes)) != len(actual_row_hashes):
        raise RuntimeError("source diff relation_row_sha256 must be unique")
    relation_row_set_sha256 = _canonical_json_sha256(sorted(actual_row_hashes))
    if set(source_diff["relation_row_set_sha256"].map(_value)) != {
        relation_row_set_sha256
    }:
        raise RuntimeError("source diff relation_row_set_sha256 mismatch")
    if set(source_diff["record_type"].map(_value)) != {"episode_relation"}:
        raise RuntimeError("source diff must contain episode_relation rows only")
    context = {
        "source_diff_artifact_version": SOURCE_DIFF_ARTIFACT_VERSION,
        "source_diff_relation_row_set_sha256": relation_row_set_sha256,
    }
    for column in SOURCE_LINEAGE_COLUMNS:
        context[column] = _single_value(source_diff, column, "source diff")
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
    for column in (
        "projection_v2_manifest_canonical_sha256",
        "projection_v2_detail_semantic_sha256",
    ):
        _require_sha256(context[column], f"source diff {column}")
    return context


def _anomaly_registry_context(
    anomaly_registry: pd.DataFrame,
) -> tuple[dict[str, str], pd.DataFrame]:
    _require_columns(
        anomaly_registry,
        {"model_id", "operation_key", "candidate_detail_row_sha256"},
        "anomaly disposition registry",
    )
    selected = anomaly_registry.loc[
        anomaly_registry["model_id"].map(_value).eq(MODEL_ID)
    ].copy()
    if len(selected) != 8:
        raise RuntimeError(
            "anomaly registry must contain exactly eight revenue_unreacted_range rows: "
            f"{len(selected)}"
        )
    pairs = list(
        zip(
            selected["operation_key"].map(_value),
            selected["candidate_detail_row_sha256"].map(_value),
            strict=True,
        )
    )
    if len(set(pairs)) != 8 or any(not key for key, _digest in pairs):
        raise RuntimeError("anomaly registry operation pairs must be eight unique rows")
    for _key, digest in pairs:
        _require_sha256(digest, "anomaly registry candidate detail row")
    return (
        {
            "anomaly_registry_canonical_sha256": canonical_frame_sha256(
                anomaly_registry
            )
        },
        selected,
    )


def _projection_v2_context(
    manifest_raw: bytes,
    detail_raw: bytes,
    source_context: dict[str, str],
) -> dict[str, str]:
    manifest = _read_csv_bytes(manifest_raw, "projection v2 manifest")
    detail = _read_csv_bytes(detail_raw, "projection v2 detail")
    if len(manifest) != 1 or "artifact_version" not in manifest.columns:
        raise RuntimeError("projection v2 manifest must contain one versioned row")
    if _value(manifest.iloc[0]["artifact_version"]) != V2_PROJECTION_ARTIFACT_VERSION:
        raise RuntimeError("projection v2 manifest artifact_version mismatch")
    manifest_canonical = canonical_frame_sha256(manifest)
    if manifest_canonical != source_context["projection_v2_manifest_canonical_sha256"]:
        raise RuntimeError("projection v2 manifest canonical binding mismatch")
    detail_semantic = _projection_detail_semantic_sha256(detail)
    if detail_semantic != source_context["projection_v2_detail_semantic_sha256"]:
        raise RuntimeError("projection v2 detail semantic binding mismatch")
    if "projected_episode_semantic_sha256" not in manifest.columns or _value(
        manifest.iloc[0]["projected_episode_semantic_sha256"]
    ) != detail_semantic:
        raise RuntimeError("projection v2 manifest does not bind the detail semantic SHA-256")
    return {
        "projection_v2_manifest_raw_sha256": hashlib.sha256(manifest_raw).hexdigest(),
        "projection_v2_detail_raw_sha256": hashlib.sha256(detail_raw).hexdigest(),
    }


def _corrected_detail_context(
    corrected_detail: pd.DataFrame,
    source_context: dict[str, str],
) -> dict[str, str]:
    required = {
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
    _require_columns(corrected_detail, required, "corrected low/mid detail")
    if _single_value(corrected_detail, "model_id", "corrected detail") != MODEL_ID:
        raise RuntimeError("corrected detail model_id mismatch")
    if _single_value(
        corrected_detail,
        "source_projection_artifact_version",
        "corrected detail",
    ) != V2_PROJECTION_ARTIFACT_VERSION:
        raise RuntimeError("corrected detail is not pinned to projection v2")
    if _single_value(
        corrected_detail,
        "source_projection_manifest_canonical_sha256",
        "corrected detail",
    ) != source_context["projection_v2_manifest_canonical_sha256"]:
        raise RuntimeError("corrected detail projection v2 manifest binding mismatch")
    if _single_value(
        corrected_detail,
        "source_projection_projected_episode_semantic_sha256",
        "corrected detail",
    ) != source_context["projection_v2_detail_semantic_sha256"]:
        raise RuntimeError("corrected detail projection v2 detail binding mismatch")
    operation_pairs = list(
        zip(
            corrected_detail["operation_key"].map(_value),
            corrected_detail["candidate_detail_row_sha256"].map(_value),
            strict=True,
        )
    )
    if any(not key for key, _sha in operation_pairs) or len(set(operation_pairs)) != len(
        operation_pairs
    ):
        raise RuntimeError("corrected detail operation pairs must be non-empty and unique")
    detail_hashes = []
    asof_latest_date = _require_date(
        _single_value(corrected_detail, "asof_latest_date", "corrected detail"),
        "corrected detail asof_latest_date",
    )
    for index, (_key, candidate_sha) in enumerate(operation_pairs):
        detail_hashes.append(_require_sha256(candidate_sha, "corrected candidate detail row"))
        row = corrected_detail.iloc[index]
        entry_date = _require_date(row["entry_date"], "corrected entry_date")
        exit_date = _require_date(row["exit_date"], "corrected exit_date")
        if entry_date > exit_date or exit_date > asof_latest_date:
            raise RuntimeError(
                "corrected operation dates must satisfy entry_date <= exit_date <= "
                "asof_latest_date"
            )
        _require_positive_decimal(row["entry_price"], "corrected entry_price")
        _require_positive_decimal(row["exit_price"], "corrected exit_price")
        if not _value(row["stock_id"]):
            raise RuntimeError("corrected stock_id must not be empty")
    detail_row_set_sha256 = _canonical_json_sha256(sorted(detail_hashes))
    if set(corrected_detail["candidate_detail_row_set_sha256"].map(_value)) != {
        detail_row_set_sha256
    }:
        raise RuntimeError("corrected detail candidate_detail_row_set_sha256 mismatch")
    return {
        "corrected_low_mid_detail_artifact_id": _single_value(
            corrected_detail, "artifact_id", "corrected detail"
        ),
        "corrected_low_mid_detail_artifact_version": _single_value(
            corrected_detail, "artifact_version", "corrected detail"
        ),
        "corrected_low_mid_detail_canonical_sha256": canonical_frame_sha256(
            corrected_detail
        ),
        "corrected_low_mid_detail_row_set_sha256": detail_row_set_sha256,
        "asof_latest_date": asof_latest_date,
    }


def _corrected_summary_context(
    corrected_summary: pd.DataFrame,
    source_context: dict[str, str],
    detail_context: dict[str, str],
) -> dict[str, str]:
    required = {
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
    _require_columns(corrected_summary, required, "corrected low/mid summary")
    if _single_value(corrected_summary, "model_id", "corrected summary") != MODEL_ID:
        raise RuntimeError("corrected summary model_id mismatch")
    expected = {
        "source_projection_artifact_version": V2_PROJECTION_ARTIFACT_VERSION,
        "source_projection_manifest_canonical_sha256": source_context[
            "projection_v2_manifest_canonical_sha256"
        ],
        "source_projection_projected_episode_semantic_sha256": source_context[
            "projection_v2_detail_semantic_sha256"
        ],
        "detail_artifact_canonical_sha256": detail_context[
            "corrected_low_mid_detail_canonical_sha256"
        ],
        "candidate_detail_row_set_sha256": detail_context[
            "corrected_low_mid_detail_row_set_sha256"
        ],
        "asof_latest_date": detail_context["asof_latest_date"],
    }
    for column, value in expected.items():
        if _single_value(corrected_summary, column, "corrected summary") != value:
            raise RuntimeError(f"corrected summary {column} binding mismatch")
    return {
        "corrected_low_mid_summary_artifact_id": _single_value(
            corrected_summary, "artifact_id", "corrected summary"
        ),
        "corrected_low_mid_summary_artifact_version": _single_value(
            corrected_summary, "artifact_version", "corrected summary"
        ),
        "corrected_low_mid_summary_canonical_sha256": canonical_frame_sha256(
            corrected_summary
        ),
    }


def _source_replay_facts(
    source_diff: pd.DataFrame,
    original_detail_row: pd.Series,
) -> tuple[str, str]:
    episode_key = _value(original_detail_row["episode_key"])
    matches = source_diff.loc[
        source_diff["record_type"].map(_value).eq("episode_relation")
        & source_diff["original_episode_key"].map(_value).eq(episode_key)
    ]
    if not episode_key or len(matches) != 1:
        raise RuntimeError(
            "each original operation must bind exactly one source episode relation: "
            f"{_value(original_detail_row['operation_key'])}"
        )
    relation = matches.iloc[0]
    status = _value(relation["relation_status"])
    relation_reason = _value(relation["absence_reason"])
    if status not in {
        "exact_episode_key_successor",
        "qualifying_source_overlap_successor",
        "absent_after_repair",
    }:
        raise RuntimeError(f"source episode relation is not final: {status!r}")
    corrected_key = _value(relation["corrected_episode_key"])
    if status == "absent_after_repair":
        if corrected_key:
            raise RuntimeError("absent source episode must not carry corrected_episode_key")
        if relation_reason != "no_shared_qualifying_source_row":
            raise RuntimeError(
                "absent source episode requires exact no-successor evidence"
            )
        return "true", "final_source_absence_after_repair"
    if not corrected_key:
        raise RuntimeError("source successor relation requires corrected_episode_key")
    if relation_reason:
        raise RuntimeError("source successor relation must not carry absence_reason")
    comparable_columns = (
        (
            "original_episode_start_source_row_canonical_sha256",
            "corrected_episode_start_source_row_canonical_sha256",
        ),
        (
            "original_qualifying_source_row_canonical_sha256s",
            "corrected_qualifying_source_row_canonical_sha256s",
        ),
    )
    changed = any(
        _value(relation[original]) != _value(relation[corrected])
        for original, corrected in comparable_columns
    )
    if not changed and status == "exact_episode_key_successor":
        return "false", "source_replay_equal"
    return "true", "source_replay_changed_successor"


def _operation_replay_facts(
    original: pd.Series,
    corrected: pd.Series | None,
    *,
    asof_latest_date: str,
) -> dict[str, str]:
    original_entry_date = _require_date(original["entry_date"], "original entry_date")
    original_exit_date = _require_date(original["exit_date"], "original exit_date")
    if original_entry_date > original_exit_date or original_exit_date > asof_latest_date:
        raise RuntimeError(
            "original operation dates must satisfy entry_date <= exit_date <= "
            "asof_latest_date"
        )
    result = {
        "original_stock_id": _value(original["stock_id"]),
        "original_entry_date": original_entry_date,
        "original_entry_price": _value(original["entry_price"]),
        "original_exit_date": original_exit_date,
        "original_exit_price": _value(original["exit_price"]),
        "corrected_stock_id": "",
        "corrected_entry_date": "",
        "corrected_entry_price": "",
        "corrected_exit_date": "",
        "corrected_exit_price": "",
        "price_replay_relation": "not_applicable_final_absence",
        "identity_calendar_status": (
            "original_identity_and_chronology_verified_no_successor"
        ),
    }
    if corrected is None:
        return result
    corrected_entry_date = _require_date(corrected["entry_date"], "corrected entry_date")
    corrected_exit_date = _require_date(corrected["exit_date"], "corrected exit_date")
    if (
        corrected_entry_date > corrected_exit_date
        or corrected_exit_date > asof_latest_date
    ):
        raise RuntimeError(
            "corrected operation dates must satisfy entry_date <= exit_date <= "
            "asof_latest_date"
        )
    if _value(original["stock_id"]) != _value(corrected["stock_id"]):
        raise RuntimeError("successor operation stock identity mismatch")
    original_prices = (
        _require_positive_decimal(original["entry_price"], "original entry_price"),
        _require_positive_decimal(original["exit_price"], "original exit_price"),
    )
    corrected_prices = (
        _require_positive_decimal(corrected["entry_price"], "corrected entry_price"),
        _require_positive_decimal(corrected["exit_price"], "corrected exit_price"),
    )
    same_replay = (
        original_prices == corrected_prices
        and original_entry_date == corrected_entry_date
        and original_exit_date == corrected_exit_date
    )
    result.update(
        {
            "corrected_stock_id": _value(corrected["stock_id"]),
            "corrected_entry_date": corrected_entry_date,
            "corrected_entry_price": _value(corrected["entry_price"]),
            "corrected_exit_date": corrected_exit_date,
            "corrected_exit_price": _value(corrected["exit_price"]),
            "price_replay_relation": (
                "entry_exit_price_and_date_equal"
                if same_replay
                else "entry_exit_price_or_date_changed"
            ),
            "identity_calendar_status": (
                "verified_same_identity_and_chronological_dates"
            ),
        }
    )
    return result


def _validated_report_rows(
    corrected_report: pd.DataFrame,
    source_diff: pd.DataFrame,
    originals: pd.DataFrame,
    original_detail_rows: dict[tuple[str, str], pd.Series],
    corrected_detail: pd.DataFrame,
    source_context: dict[str, str],
    summary_context: dict[str, str],
    detail_context: dict[str, str],
) -> tuple[dict[str, str], pd.DataFrame]:
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
    _require_columns(corrected_report, required, "corrected low/mid final report")
    if len(corrected_report) != 8:
        raise RuntimeError(
            "corrected low/mid final report must contain exactly eight operation rows: "
            f"{len(corrected_report)}"
        )
    if _single_value(corrected_report, "model_id", "corrected report") != MODEL_ID:
        raise RuntimeError("corrected report model_id mismatch")
    expected_bindings = {
        "source_diff_relation_row_set_sha256": source_context[
            "source_diff_relation_row_set_sha256"
        ],
        "corrected_low_mid_summary_canonical_sha256": summary_context[
            "corrected_low_mid_summary_canonical_sha256"
        ],
        "corrected_low_mid_detail_canonical_sha256": detail_context[
            "corrected_low_mid_detail_canonical_sha256"
        ],
        "corrected_low_mid_detail_row_set_sha256": detail_context[
            "corrected_low_mid_detail_row_set_sha256"
        ],
        "asof_latest_date": detail_context["asof_latest_date"],
        **{column: source_context[column] for column in SOURCE_LINEAGE_COLUMNS},
    }
    for column, expected in expected_bindings.items():
        if _single_value(corrected_report, column, "corrected report") != expected:
            raise RuntimeError(f"corrected report {column} binding mismatch")
    expected_pairs = {
        (
            _value(row["operation_key"]),
            _value(row["candidate_detail_row_sha256"]),
        )
        for _, row in originals.iterrows()
    }
    report_pairs = list(
        zip(
            corrected_report["original_operation_key"].map(_value),
            corrected_report["original_candidate_detail_row_sha256"].map(_value),
            strict=True,
        )
    )
    if len(set(report_pairs)) != 8 or set(report_pairs) != expected_pairs:
        raise RuntimeError("corrected report does not exactly cover the eight original pairs")
    detail_pairs = list(
        zip(
            corrected_detail["operation_key"].map(_value),
            corrected_detail["candidate_detail_row_sha256"].map(_value),
            strict=True,
        )
    )
    for _, row in corrected_report.iterrows():
        original_pair = (
            _value(row["original_operation_key"]),
            _value(row["original_candidate_detail_row_sha256"]),
        )
        status = _value(row["final_relation_status"])
        if status not in FINAL_RELATION_STATUSES:
            raise RuntimeError(
                "corrected report contains a pending or invalid final relation status: "
                f"{status!r}"
            )
        corrected_pair = (
            _value(row["corrected_operation_key"]),
            _value(row["corrected_candidate_detail_row_sha256"]),
        )
        reason = _value(row["approved_absence_reason"])
        reference = _value(row["approved_absence_reason_reference"])
        original = original_detail_rows[original_pair]
        repair_changed, source_relation = _source_replay_facts(
            source_diff,
            original,
        )
        corrected: pd.Series | None = None
        if status == FINAL_SUCCESSOR:
            if not corrected_pair[0]:
                raise RuntimeError("final successor requires corrected_operation_key")
            _require_sha256(corrected_pair[1], "final successor corrected candidate row")
            if detail_pairs.count(corrected_pair) != 1:
                raise RuntimeError(
                    "final successor must bind exactly one corrected detail row: "
                    f"{corrected_pair[0]}"
                )
            if reason or reference:
                raise RuntimeError("final successor must not carry an absence reason")
            corrected = corrected_detail.loc[
                corrected_detail["operation_key"].map(_value).eq(corrected_pair[0])
                & corrected_detail["candidate_detail_row_sha256"]
                .map(_value)
                .eq(corrected_pair[1])
            ].iloc[0]
        else:
            if corrected_pair != ("", ""):
                raise RuntimeError("final absence must not carry a corrected operation pair")
            if reason.lower() in FORBIDDEN_PENDING_TOKENS or reference.lower() in (
                FORBIDDEN_PENDING_TOKENS
            ):
                raise RuntimeError(
                    "final absence requires an approved explicit reason and reference"
                )
        replay_facts = _operation_replay_facts(
            original,
            corrected,
            asof_latest_date=detail_context["asof_latest_date"],
        )
        derived = {
            **replay_facts,
            "repair_changed_relevant_input": repair_changed,
            "source_replay_relation": source_relation,
        }
        for column, expected in derived.items():
            if _value(row[column]) != expected:
                raise RuntimeError(
                    f"corrected report {column} is not derived from replay inputs for "
                    f"{original_pair[0]}"
                )
        comparability = _value(row["comparability_status"])
        non_comparable_reference = _value(
            row["approved_non_comparable_reason_reference"]
        )
        if comparability not in {"verified_comparable", "verified_non_comparable"}:
            raise RuntimeError("comparability_status must be a verified final status")
        if comparability == "verified_non_comparable":
            if non_comparable_reference.lower() in FORBIDDEN_PENDING_TOKENS:
                raise RuntimeError(
                    "verified_non_comparable requires an approved reason reference"
                )
        elif non_comparable_reference:
            raise RuntimeError(
                "verified_comparable must not carry a non-comparable reason reference"
            )
        corroboration = _value(row["independent_corroboration_status"])
        corroboration_reference = _value(
            row["independent_corroboration_reference"]
        )
        if (
            corroboration.lower() in FORBIDDEN_PENDING_TOKENS
            or corroboration_reference.lower() in FORBIDDEN_PENDING_TOKENS
        ):
            raise RuntimeError(
                "independent corroboration requires a final status and evidence reference"
            )
        contradiction_text = _value(row["contradiction_count"])
        if not contradiction_text.isdigit():
            raise RuntimeError("contradiction_count must be a non-negative integer")
        contradiction_reference = _value(row["contradiction_evidence_reference"])
        if int(contradiction_text) > 0 and (
            contradiction_reference.lower() in FORBIDDEN_PENDING_TOKENS
        ):
            raise RuntimeError(
                "positive contradiction_count requires an evidence reference"
            )
    report_context = {
        "corrected_low_mid_report_artifact_id": _single_value(
            corrected_report, "artifact_id", "corrected report"
        ),
        "corrected_low_mid_report_artifact_version": _single_value(
            corrected_report, "artifact_version", "corrected report"
        ),
        "corrected_low_mid_report_canonical_sha256": canonical_frame_sha256(
            corrected_report
        ),
    }
    return report_context, corrected_report.copy()


def _attach_output_hashes(frame: pd.DataFrame) -> pd.DataFrame:
    payload_columns = [
        column for column in OUTPUT_COLUMNS if column not in ROW_HASH_EXCLUDED_COLUMNS
    ]
    result = frame.copy()
    result["operation_relation_row_sha256"] = [
        _canonical_json_sha256(
            {column: _value(row[column]) for column in payload_columns}
        )
        for _, row in result.iterrows()
    ]
    if result["operation_relation_row_sha256"].duplicated().any():
        raise RuntimeError("operation diff relation row SHA-256 must be unique")
    row_set_sha = _canonical_json_sha256(
        sorted(result["operation_relation_row_sha256"].map(_value).tolist())
    )
    result["operation_relation_row_set_sha256"] = row_set_sha
    return result


def build_operation_diff(
    anomaly_registry: pd.DataFrame,
    source_diff: pd.DataFrame,
    projection_v2_manifest_raw: bytes,
    projection_v2_detail_raw: bytes,
    original_detail: pd.DataFrame,
    corrected_summary: pd.DataFrame,
    corrected_detail: pd.DataFrame,
    corrected_report: pd.DataFrame,
    *,
    generated_at: str | None = None,
) -> pd.DataFrame:
    source_context = _source_diff_context(source_diff)
    anomaly_context, originals = _anomaly_registry_context(anomaly_registry)
    projection_v2_context = _projection_v2_context(
        projection_v2_manifest_raw,
        projection_v2_detail_raw,
        source_context,
    )
    original_detail_context, original_detail_rows = _original_detail_context(
        original_detail,
        originals,
    )
    detail_context = _corrected_detail_context(corrected_detail, source_context)
    summary_context = _corrected_summary_context(
        corrected_summary,
        source_context,
        detail_context,
    )
    report_context, report_rows = _validated_report_rows(
        corrected_report,
        source_diff,
        originals,
        original_detail_rows,
        corrected_detail,
        source_context,
        summary_context,
        detail_context,
    )
    common: dict[str, object] = {
        "generated_at": generated_at or _now_text(),
        "model_id": MODEL_ID,
        "artifact_id": ARTIFACT_ID,
        "artifact_version": ARTIFACT_VERSION,
        "record_type": "operation_relation",
        **source_context,
        **anomaly_context,
        **projection_v2_context,
        **original_detail_context,
        **summary_context,
        **detail_context,
        **report_context,
        "operation_relation_row_sha256": "",
        "operation_relation_row_set_sha256": "",
        "promotion_gate_status": "blocked_requires_separate_promotion_decision",
        "research_only": True,
        "formal_model_use_allowed": False,
        "approved_for_daily": False,
        "presentation_allowed": False,
        "production_change": False,
        "promotion_allowed": False,
        "promotion_evidence_allowed": False,
        "ranking_consumption_allowed": False,
        "pdf_consumption_allowed": False,
    }
    rows: list[dict[str, object]] = []
    for _, relation in report_rows.sort_values(
        ["original_operation_key", "original_candidate_detail_row_sha256"],
        kind="stable",
    ).iterrows():
        row = dict(common)
        for column in (
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
        ):
            row[column] = _value(relation[column])
        rows.append(row)
    frame = pd.DataFrame(rows, columns=list(OUTPUT_COLUMNS))
    return _attach_output_hashes(frame).loc[:, list(OUTPUT_COLUMNS)]


def write_operation_diff(
    frame: pd.DataFrame,
    *,
    history_path: Path = HISTORY_CSV,
    latest_path: Path = LATEST_CSV,
    docs_path: Path = DOCS_CSV,
) -> None:
    if list(frame.columns) != list(OUTPUT_COLUMNS) or len(frame) != 8:
        raise RuntimeError("operation diff must have the exact schema and eight rows")
    payload = frame.to_csv(index=False).encode("utf-8")
    targets = tuple(Path(path) for path in (history_path, latest_path, docs_path))
    prior = {path: path.read_bytes() if path.is_file() else None for path in targets}
    temporary: list[Path] = []
    replaced: list[Path] = []
    try:
        for path in targets:
            path.parent.mkdir(parents=True, exist_ok=True)
            handle, temp_name = tempfile.mkstemp(
                prefix=f".{path.name}.", suffix=".tmp", dir=path.parent
            )
            os.close(handle)
            temp_path = Path(temp_name)
            temp_path.write_bytes(payload)
            temporary.append(temp_path)
        for temp_path, target in zip(temporary, targets, strict=True):
            os.replace(temp_path, target)
            replaced.append(target)
    except Exception:
        for target in reversed(replaced):
            previous = prior[target]
            if previous is None:
                target.unlink(missing_ok=True)
            else:
                target.write_bytes(previous)
        raise
    finally:
        for temp_path in temporary:
            temp_path.unlink(missing_ok=True)


def _read_csv(path: Path) -> pd.DataFrame:
    if not Path(path).is_file():
        raise RuntimeError(f"missing required corrected-chain input: {path}")
    return pd.read_csv(path, dtype=str, keep_default_na=False, low_memory=False)


def build_and_write_operation_diff_from_paths(
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
    generated_at: str | None = None,
) -> pd.DataFrame:
    input_paths = (
        Path(anomaly_registry_path),
        Path(source_diff_path),
        Path(projection_v2_manifest_path),
        Path(projection_v2_detail_path),
        Path(original_detail_path),
        Path(corrected_summary_path),
        Path(corrected_detail_path),
        Path(corrected_report_path),
    )
    missing = [str(path) for path in input_paths if not path.is_file()]
    if missing:
        raise RuntimeError(
            "operation diff publication requires all eight exact-bound inputs before write: "
            f"{missing}"
        )
    frame = build_operation_diff(
        _read_csv(input_paths[0]),
        _read_csv(input_paths[1]),
        input_paths[2].read_bytes(),
        input_paths[3].read_bytes(),
        _read_csv(input_paths[4]),
        _read_csv(input_paths[5]),
        _read_csv(input_paths[6]),
        _read_csv(input_paths[7]),
        generated_at=generated_at,
    )
    from validate_revenue_unreacted_range_source_snapshot_projection_v1_v2_operation_diff import (
        validate_frames as validate_operation_diff_independently,
    )

    validation_inputs = (
        _read_csv(input_paths[0]),
        _read_csv(input_paths[1]),
        input_paths[2].read_bytes(),
        input_paths[3].read_bytes(),
        _read_csv(input_paths[4]),
        _read_csv(input_paths[5]),
        _read_csv(input_paths[6]),
        _read_csv(input_paths[7]),
    )
    errors = validate_operation_diff_independently(*validation_inputs, frame)
    if errors:
        raise RuntimeError(
            "independent corrected-chain operation diff validation failed: "
            + "; ".join(errors)
        )
    write_operation_diff(
        frame,
        history_path=history_path,
        latest_path=latest_path,
        docs_path=docs_path,
    )
    return frame
