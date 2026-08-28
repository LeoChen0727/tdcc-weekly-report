from __future__ import annotations

from datetime import datetime
import hashlib
import json
import os
from pathlib import Path
import re
import tempfile
import warnings
from zoneinfo import ZoneInfo

import pandas as pd

from revenue_unreacted_range_monthly_revenue_cross_market_resolution import (
    BUSINESS_PAYLOAD_COLUMNS,
    RESOLUTION_COLUMNS as MONTHLY_RESOLUTION_COLUMNS,
    SOURCE_IDENTITY_COLUMNS,
    canonical_monthly_revenue_history_table_sha256,
    cross_market_resolution_registry_canonical_sha256,
    load_canonical_monthly_revenue_history,
    load_cross_market_resolutions,
    monthly_revenue_history_blob_sha256,
    resolve_monthly_revenue_cross_market_mirrors,
)


ROOT = Path(__file__).resolve().parents[1]
MODEL_ID = "revenue_unreacted_range"
ARTIFACT_ID = "revenue_unreacted_range_source_snapshot_projection"
V1_ARTIFACT_VERSION = "source_snapshot_projection_v1_20260731"
V2_ARTIFACT_VERSION = "source_snapshot_projection_v2_20260822"
ARTIFACT_VERSION = V1_ARTIFACT_VERSION
PROJECTION_ID = "revenue_unreacted_range_source_snapshot_asof_20260713"
V1_PROJECTION_VERSION = V1_ARTIFACT_VERSION
V2_PROJECTION_VERSION = V2_ARTIFACT_VERSION
PROJECTION_VERSION = V1_PROJECTION_VERSION
V1_PROJECTION_POLICY_ID = (
    "raw_source_and_price_truncated_before_source_first_episode_assembly_v1"
)
V2_PROJECTION_POLICY_ID = (
    "raw_source_and_corrected_official_price_truncated_before_source_first_episode_assembly_v2"
)
PROJECTION_POLICY_ID = V1_PROJECTION_POLICY_ID
V2_LINEAGE_CHANGE_REASON = (
    "corrected_official_pre_cutoff_price_history_lineage_rebaseline_20260822"
)
V2_CANDIDATE_STATUS = "generated_pending_supersede_approval"
CUTOFF_DATE = "20260713"
SOURCE_FIRST_ARTIFACT_ID = "revenue_unreacted_range_source_first_condition_audit"

REVENUE_HISTORY_CSV = ROOT / "data/monthly_revenue_history/monthly_revenue_history.csv"
PRICE_HISTORY_DIR = ROOT / "data/stock_price_history"
MONTHLY_RESOLUTION_CSV = (
    ROOT / "config/revenue_unreacted_range_monthly_revenue_cross_market_resolution.csv"
)
PRICE_RESOLUTION_CSV = (
    ROOT / "config/revenue_unreacted_range_price_comparability_resolution.csv"
)
FULL_SOURCE_DETAIL_CSV = (
    ROOT
    / "output/latest/research_backtest/"
    "revenue_unreacted_range_source_first_condition_audit_detail_latest.csv"
)
LATEST_MANIFEST_CSV = (
    ROOT
    / "output/latest/research_backtest/"
    "revenue_unreacted_range_source_snapshot_projection_manifest_latest.csv"
)
LATEST_DETAIL_CSV = (
    ROOT
    / "output/latest/research_backtest/"
    "revenue_unreacted_range_source_snapshot_projection_detail_latest.csv"
)
HISTORY_MANIFEST_CSV = (
    ROOT
    / "output/history/research/"
    "revenue_unreacted_range_source_snapshot_projection_manifest.csv"
)
DOCS_MANIFEST_CSV = (
    ROOT
    / "docs/latest/"
    "revenue_unreacted_range_source_snapshot_projection_manifest_latest.csv"
)
V1_ARCHIVE_MANIFEST_CSV = (
    ROOT
    / "output/history/research/"
    "revenue_unreacted_range_source_snapshot_projection_manifest_v1_20260731.csv"
)
V1_ARCHIVE_DETAIL_CSV = (
    ROOT
    / "output/history/research/"
    "revenue_unreacted_range_source_snapshot_projection_detail_v1_20260731.csv"
)
V1_ARCHIVE_EVIDENCE_CSV = (
    ROOT
    / "output/history/research/"
    "revenue_unreacted_range_source_snapshot_projection_archive_evidence_v1_20260731.csv"
)
V2_CANDIDATE_MANIFEST_CSV = (
    ROOT
    / "output/history/research/"
    "revenue_unreacted_range_source_snapshot_projection_manifest_v2_20260822.csv"
)
V2_CANDIDATE_DETAIL_CSV = (
    ROOT
    / "output/history/research/"
    "revenue_unreacted_range_source_snapshot_projection_detail_v2_20260822.csv"
)
V1_V2_DIFF_SUMMARY_CSV = (
    ROOT
    / "output/history/research/"
    "revenue_unreacted_range_source_snapshot_projection_v1_20260731_to_v2_20260822_diff_summary.csv"
)
V1_V2_DIFF_DETAIL_CSV = (
    ROOT
    / "output/history/research/"
    "revenue_unreacted_range_source_snapshot_projection_v1_20260731_to_v2_20260822_diff_detail.csv"
)
V2_SUPERSEDE_EVIDENCE_CSV = (
    ROOT
    / "output/history/research/"
    "revenue_unreacted_range_source_snapshot_projection_supersede_evidence_v2_20260822.csv"
)

V2_SUPERSEDE_EVIDENCE_ARTIFACT_ID = (
    "revenue_unreacted_range_source_snapshot_projection_supersede_evidence"
)
V2_SUPERSEDE_EVIDENCE_ARTIFACT_VERSION = (
    "source_snapshot_projection_supersede_evidence_v1_20260822"
)
V2_SUPERSEDE_SELECTION_STATUS = "canonical_research_source_projection_current"
V2_DIFF_CLASSIFIED_STATUS = "classified_corrected_official_cutoff_price_lineage"

V1_EXPECTED_MANIFEST_BYTES = 148157
V1_EXPECTED_MANIFEST_BYTES_SHA256 = (
    "d2dde5a1f05bc2f15baf4d77f326a7ea90b481492178fa6d2fd6262bf316c79e"
)
V1_EXPECTED_DETAIL_BYTES = 26633382
V1_EXPECTED_DETAIL_BYTES_SHA256 = (
    "b9784e4df2d2eba2c511b1c87f4255a6485a1fe1d7ac67490802e396614ee49a"
)
V1_EXPECTED_DETAIL_ROW_COUNT = 19569
V1_EXPECTED_DETAIL_SEMANTIC_SHA256 = (
    "92c68810ac2b5718d714d450fe83bf23f2f3469fec5db0ae2753330950ab2cf5"
)

CANONICAL_JSON_VERSION = "revenue_source_snapshot_projection_canonical_json_v1"
PRICE_INPUT_COLUMNS = (
    "date",
    "open",
    "high",
    "low",
    "close",
    "volume",
    "volume_ratio",
)
MONTHLY_CANONICAL_BINDING_COLUMNS = (
    "stock_id",
    "revenue_period",
    "source_row_canonical_sha256",
    "cross_market_resolution_id",
    "canonical_source_table_date",
)
MONTHLY_RAW_REQUIRED_COLUMNS = SOURCE_IDENTITY_COLUMNS + BUSINESS_PAYLOAD_COLUMNS
PRICE_RESOLUTION_REQUIRED_COLUMNS = (
    "resolution_id",
    "model_id",
    "stock_id",
    "resume_date",
    "exchange_ratio",
    "root_cause_status",
)
V1_MANIFEST_COLUMNS = (
    "generated_at",
    "model_id",
    "artifact_id",
    "artifact_version",
    "projection_id",
    "projection_version",
    "projection_policy_id",
    "cutoff_date",
    "full_source_artifact_id",
    "full_source_artifact_version",
    "full_source_episode_row_count",
    "full_source_episode_semantic_sha256",
    "monthly_revenue_history_blob_sha256",
    "monthly_revenue_canonical_table_sha256",
    "cross_market_resolution_registry_canonical_sha256",
    "cutoff_revenue_subset_row_count",
    "cutoff_revenue_subset_semantic_sha256",
    "cutoff_price_input_stock_count",
    "cutoff_price_input_row_count",
    "cutoff_price_input_file_semantic_sha256s",
    "cutoff_price_input_semantic_sha256",
    "applied_monthly_resolution_count",
    "applied_monthly_resolution_ids",
    "applied_monthly_resolution_semantic_sha256",
    "applied_price_resolution_count",
    "applied_price_resolution_ids",
    "applied_price_resolution_semantic_sha256",
    "projected_episode_row_count",
    "projected_episode_semantic_sha256",
    "projected_max_source_date",
    "projected_max_trade_date",
    "projected_max_episode_end_date",
    "research_only",
    "formal_model_use_allowed",
    "approved_for_daily",
    "production_change",
    "promotion_evidence_allowed",
    "ranking_consumption_allowed",
    "pdf_consumption_allowed",
)
V2_MANIFEST_EXTENSION_COLUMNS = (
    "predecessor_projection_version",
    "predecessor_manifest_bytes_sha256",
    "predecessor_detail_bytes_sha256",
    "lineage_change_reason",
    "candidate_status",
)
V2_MANIFEST_COLUMNS = V1_MANIFEST_COLUMNS + V2_MANIFEST_EXTENSION_COLUMNS
MANIFEST_COLUMNS = V1_MANIFEST_COLUMNS
ARCHIVE_EVIDENCE_COLUMNS = (
    "generated_at",
    "model_id",
    "artifact_id",
    "projection_id",
    "projection_version",
    "cutoff_date",
    "canonical_manifest_path",
    "archive_manifest_path",
    "canonical_manifest_bytes",
    "canonical_manifest_sha256",
    "canonical_detail_path",
    "archive_detail_path",
    "canonical_detail_bytes",
    "canonical_detail_sha256",
    "projected_episode_row_count",
    "projected_episode_semantic_sha256",
    "immutable_copy_verified",
    "research_only",
    "formal_model_use_allowed",
    "approved_for_daily",
    "production_change",
    "promotion_evidence_allowed",
    "ranking_consumption_allowed",
    "pdf_consumption_allowed",
)
V2_SUPERSEDE_EVIDENCE_COLUMNS = (
    "superseded_at",
    "model_id",
    "artifact_id",
    "artifact_version",
    "projection_id",
    "selected_projection_version",
    "selection_status",
    "candidate_status",
    "candidate_manifest_path",
    "candidate_manifest_bytes",
    "candidate_manifest_sha256",
    "candidate_detail_path",
    "candidate_detail_bytes",
    "candidate_detail_sha256",
    "v1_archive_manifest_path",
    "v1_archive_manifest_sha256",
    "v1_archive_detail_path",
    "v1_archive_detail_sha256",
    "v1_v2_diff_summary_path",
    "v1_v2_diff_summary_sha256",
    "v1_v2_diff_detail_path",
    "v1_v2_diff_detail_sha256",
    "canonical_latest_manifest_path",
    "canonical_latest_detail_path",
    "canonical_history_manifest_path",
    "canonical_docs_manifest_path",
    "canonical_exact3_manifest_sha256",
    "canonical_exact3_detail_sha256",
    "canonical_exact3_verified",
    "canonical_history_preimage_bytes",
    "canonical_history_preimage_sha256",
    "canonical_history_preimage_row_count",
    "canonical_history_preimage_semantic_sha256",
    "canonical_history_postimage_bytes",
    "canonical_history_postimage_sha256",
    "canonical_history_postimage_row_count",
    "canonical_history_postimage_v1_row_count",
    "canonical_history_postimage_v2_row_count",
    "canonical_history_append_only_verified",
    "research_only",
    "formal_model_use_allowed",
    "approved_for_daily",
    "production_change",
    "promotion_evidence_allowed",
    "ranking_consumption_allowed",
    "pdf_consumption_allowed",
    "forward_holdout_refreshed",
)
SHA256_PATTERN = re.compile(r"^[0-9a-f]{64}$")
NO_RESOLUTION_ID = "none"
PROJECTED_CAPTURE_LINEAGE_COLUMNS = (
    "monthly_revenue_history_blob_sha256",
    "cross_market_resolution_registry_canonical_sha256",
)


def _now_text() -> str:
    return datetime.now(ZoneInfo("Asia/Taipei")).strftime(
        "%Y-%m-%d %H:%M:%S Asia/Taipei"
    )


def _payload_value(value: object) -> str:
    if value is None or pd.isna(value):
        return ""
    if isinstance(value, bool):
        return "true" if value else "false"
    text = str(value).strip()
    if text.lower() in {"true", "false"}:
        return text.lower()
    return text


def _canonical_json_sha256(payload: object) -> str:
    encoded = json.dumps(
        payload,
        ensure_ascii=False,
        separators=(",", ":"),
    ).encode("utf-8")
    return hashlib.sha256(encoded).hexdigest()


def _file_sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with Path(path).open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def _normalize_stock_id(value: object) -> str:
    text = _payload_value(value).replace(".0", "")
    return text.zfill(4) if text else ""


def _digits(value: object, length: int, *, label: str) -> str:
    text = _payload_value(value)
    exact = re.fullmatch(rf"\d{{{length}}}", text)
    if exact:
        return text
    numeric_export = re.fullmatch(rf"(\d{{{length}}})\.0+", text)
    if numeric_export:
        return numeric_export.group(1)
    raise RuntimeError(f"{label} must contain exactly {length} digits: {text!r}")


def _canonical_frame_sha256(
    frame: pd.DataFrame,
    *,
    columns: tuple[str, ...] | list[str] | None = None,
    excluded_columns: tuple[str, ...] = (),
) -> str:
    selected = (
        list(columns)
        if columns is not None
        else [column for column in frame.columns if column not in excluded_columns]
    )
    missing = sorted(set(selected) - set(frame.columns))
    if missing:
        raise RuntimeError(f"canonical frame is missing columns: {missing}")
    rows = [
        [_payload_value(value) for value in row]
        for row in frame.loc[:, selected].itertuples(index=False, name=None)
    ]
    rows.sort()
    return _canonical_json_sha256([CANONICAL_JSON_VERSION, selected, rows])


def canonical_source_detail_semantic_sha256(frame: pd.DataFrame) -> str:
    return _canonical_frame_sha256(frame, excluded_columns=("generated_at",))


def canonical_projected_source_detail_semantic_sha256(frame: pd.DataFrame) -> str:
    return _canonical_frame_sha256(
        frame,
        excluded_columns=("generated_at", *PROJECTED_CAPTURE_LINEAGE_COLUMNS),
    )


def _constant(frame: pd.DataFrame, column: str, *, label: str) -> str:
    if column not in frame.columns:
        raise RuntimeError(f"{label} is missing column: {column}")
    values = sorted({_payload_value(value) for value in frame[column]})
    if len(values) != 1 or not values[0]:
        raise RuntimeError(f"{label} must have one non-empty {column}: {values}")
    return values[0]


def _read_raw_monthly_revenue(path: Path, cutoff_date: str | None) -> pd.DataFrame:
    if not path.is_file():
        raise RuntimeError(f"missing monthly revenue history: {path}")
    frame = pd.read_csv(path, dtype=str, keep_default_na=False, low_memory=False)
    missing = sorted(set(MONTHLY_RAW_REQUIRED_COLUMNS) - set(frame.columns))
    if missing:
        raise RuntimeError(f"monthly revenue history is missing columns: {missing}")
    dates = frame["source_table_date"].map(
        lambda value: _digits(value, 8, label="monthly source_table_date")
    )
    frame = frame.copy()
    frame["source_table_date"] = dates
    if cutoff_date is not None:
        frame = frame.loc[frame["source_table_date"].le(cutoff_date)].copy()
    return frame.reset_index(drop=True)


def load_cutoff_monthly_revenue_subset(
    revenue_path: Path = REVENUE_HISTORY_CSV,
    monthly_resolution_path: Path = MONTHLY_RESOLUTION_CSV,
    *,
    cutoff_date: str = CUTOFF_DATE,
) -> pd.DataFrame:
    cutoff = _digits(cutoff_date, 8, label="projection cutoff_date")
    raw = _read_raw_monthly_revenue(Path(revenue_path), cutoff)
    return resolve_monthly_revenue_cross_market_mirrors(
        raw,
        Path(monthly_resolution_path),
        observation_cutoff_date=cutoff,
    )


def _price_file_projection(path: Path, stock_id: str, cutoff_date: str) -> pd.DataFrame:
    if not path.is_file():
        raise RuntimeError(f"missing projected stock price history: {path}")
    frame = pd.read_csv(path, dtype=str, keep_default_na=False, low_memory=False)
    missing = sorted(set(PRICE_INPUT_COLUMNS) - set(frame.columns))
    if missing:
        raise RuntimeError(f"price history {stock_id} is missing columns: {missing}")
    frame = frame.loc[:, list(PRICE_INPUT_COLUMNS)].copy()
    frame["date"] = frame["date"].map(
        lambda value: _digits(value, 8, label=f"price date for {stock_id}")
    )
    frame = frame.loc[frame["date"].le(cutoff_date)].copy()
    duplicate_dates = sorted(
        frame.loc[frame["date"].duplicated(keep=False), "date"].unique().tolist()
    )
    if duplicate_dates:
        raise RuntimeError(
            f"price history {stock_id} repeats trading dates within cutoff: "
            f"{duplicate_dates[:3]}"
        )
    frame = frame.sort_values("date", kind="mergesort").reset_index(drop=True)
    return frame


def _price_paths_by_stock(price_dir: Path) -> dict[str, Path]:
    paths: dict[str, Path] = {}
    for path in sorted(Path(price_dir).glob("*.csv")):
        stock_id = _normalize_stock_id(path.stem)
        if not stock_id:
            continue
        if stock_id in paths:
            raise RuntimeError(
                "price history directory repeats a normalized stock id: "
                f"{stock_id}/{paths[stock_id].name}/{path.name}"
            )
        paths[stock_id] = path
    return paths


def cutoff_price_input_stock_ids(
    cutoff_revenue: pd.DataFrame,
    price_dir: Path = PRICE_HISTORY_DIR,
) -> list[str]:
    if "stock_id" not in cutoff_revenue.columns:
        raise RuntimeError("cutoff canonical monthly revenue is missing stock_id")
    revenue_stock_ids = {
        _normalize_stock_id(value)
        for value in cutoff_revenue["stock_id"]
        if _normalize_stock_id(value)
    }
    return sorted(revenue_stock_ids & set(_price_paths_by_stock(Path(price_dir))))


def cutoff_price_input_lineage(
    cutoff_revenue: pd.DataFrame,
    price_dir: Path = PRICE_HISTORY_DIR,
    *,
    cutoff_date: str = CUTOFF_DATE,
) -> dict[str, object]:
    cutoff = _digits(cutoff_date, 8, label="projection cutoff_date")
    price_paths = _price_paths_by_stock(Path(price_dir))
    descriptors: list[list[object]] = []
    total_rows = 0
    for stock_id in cutoff_price_input_stock_ids(cutoff_revenue, Path(price_dir)):
        frame = _price_file_projection(price_paths[stock_id], stock_id, cutoff)
        semantic_sha = _canonical_frame_sha256(
            frame,
            columns=list(PRICE_INPUT_COLUMNS),
        )
        total_rows += len(frame)
        descriptors.append([stock_id, len(frame), semantic_sha])
    descriptor_text = "|".join(
        f"{stock_id}:{row_count}:{semantic_sha}"
        for stock_id, row_count, semantic_sha in descriptors
    )
    return {
        "stock_count": len(descriptors),
        "row_count": total_rows,
        "file_semantic_sha256s": descriptor_text,
        "semantic_sha256": _canonical_json_sha256(
            [CANONICAL_JSON_VERSION, "cutoff_price_input_set", descriptors]
        ),
    }


def _read_registry(path: Path, *, label: str) -> pd.DataFrame:
    if not path.is_file():
        raise RuntimeError(f"missing {label}: {path}")
    return pd.read_csv(path, dtype=str, keep_default_na=False)


def _resolution_subset_sha256(frame: pd.DataFrame) -> str:
    columns = tuple(column for column in frame.columns if column != "notes")
    return _canonical_frame_sha256(frame, columns=columns)


def _applied_monthly_resolutions(
    cutoff_revenue: pd.DataFrame,
    monthly_registry: pd.DataFrame,
    cutoff_date: str,
) -> tuple[list[str], str]:
    required = {"cross_market_resolution_id"}
    missing = sorted(required - set(cutoff_revenue.columns))
    if missing:
        raise RuntimeError(f"cutoff monthly revenue is missing columns: {missing}")
    ids = sorted(
        {
            _payload_value(value)
            for value in cutoff_revenue["cross_market_resolution_id"]
            if _payload_value(value) not in {"", NO_RESOLUTION_ID}
        }
    )
    if tuple(monthly_registry.columns) != tuple(MONTHLY_RESOLUTION_COLUMNS):
        raise RuntimeError("monthly resolution registry schema mismatch")
    eligible = monthly_registry.copy()
    for column in ("earlier_source_table_date", "later_source_table_date"):
        eligible[column] = eligible[column].map(
            lambda value: _digits(value, 8, label=f"monthly resolution {column}")
        )
    eligible = eligible.loc[
        eligible["resolution_id"].isin(ids)
        & eligible["earlier_source_table_date"].le(cutoff_date)
        & eligible["later_source_table_date"].le(cutoff_date)
    ].copy()
    if sorted(eligible["resolution_id"].tolist()) != ids:
        raise RuntimeError("cutoff monthly resolution ids are not fully eligible")
    return ids, _resolution_subset_sha256(eligible)


def _applied_price_resolutions(
    price_input_stock_ids: list[str],
    price_registry: pd.DataFrame,
    cutoff_date: str,
) -> tuple[list[str], str]:
    missing = sorted(set(PRICE_RESOLUTION_REQUIRED_COLUMNS) - set(price_registry.columns))
    if missing:
        raise RuntimeError(f"price resolution registry is missing columns: {missing}")
    stock_ids = set(price_input_stock_ids)
    normalized = price_registry.copy()
    normalized["stock_id"] = normalized["stock_id"].map(_normalize_stock_id)
    normalized["resume_date"] = normalized["resume_date"].map(
        lambda value: _digits(value, 8, label="price resolution resume_date")
    )
    eligible = normalized.loc[
        normalized["stock_id"].isin(stock_ids)
        & normalized["resume_date"].le(cutoff_date)
        & normalized["root_cause_status"].eq(
            "verified_non_comparable_raw_price_scale"
        )
    ].copy()
    foreign_models = sorted(
        set(eligible.loc[~eligible["model_id"].eq(MODEL_ID), "model_id"])
    )
    if foreign_models:
        raise RuntimeError(
            "cutoff source-first price inputs contain foreign-model resolutions: "
            f"{foreign_models}"
        )
    applied = eligible.loc[eligible["model_id"].eq(MODEL_ID)].copy()
    ids = sorted(applied["resolution_id"].astype(str).tolist())
    return ids, _resolution_subset_sha256(applied)


def _date_tokens(frame: pd.DataFrame, columns: tuple[str, ...]) -> list[str]:
    tokens: list[str] = []
    for column in columns:
        if column not in frame.columns:
            raise RuntimeError(f"projected source detail is missing date column: {column}")
        for value in frame[column]:
            for token in _payload_value(value).split("|"):
                token = token.strip()
                if token:
                    tokens.append(_digits(token, 8, label=column))
    return tokens


def _max_projected_dates(projected_detail: pd.DataFrame) -> tuple[str, str, str]:
    source_dates = _date_tokens(
        projected_detail,
        (
            "episode_start_source_date",
            "latest_qualifying_source_date",
            "qualifying_source_dates",
        ),
    )
    trade_dates = _date_tokens(
        projected_detail,
        (
            "episode_start_trade_date",
            "latest_qualifying_trade_date",
            "qualifying_trade_dates",
        ),
    )
    end_dates = _date_tokens(projected_detail, ("episode_end_date",))
    return (
        max(source_dates, default=""),
        max(trade_dates, default=""),
        max(end_dates, default=""),
    )


def _require_source_identity(
    full_source_detail: pd.DataFrame,
    projected_detail: pd.DataFrame,
) -> tuple[str, str]:
    source_artifact_id = _constant(
        full_source_detail,
        "artifact_id",
        label="full source detail",
    )
    source_artifact_version = _constant(
        full_source_detail,
        "artifact_version",
        label="full source detail",
    )
    if source_artifact_id != SOURCE_FIRST_ARTIFACT_ID:
        raise RuntimeError(f"unexpected full source artifact_id: {source_artifact_id}")
    if _constant(projected_detail, "artifact_id", label="projected source detail") != source_artifact_id:
        raise RuntimeError("projected detail artifact_id differs from full source")
    if (
        _constant(projected_detail, "artifact_version", label="projected source detail")
        != source_artifact_version
    ):
        raise RuntimeError("projected detail artifact_version differs from full source")
    if list(projected_detail.columns) != list(full_source_detail.columns):
        raise RuntimeError("projected detail must preserve the full source detail schema")
    return source_artifact_id, source_artifact_version


def build_source_snapshot_projection_manifest(
    full_source_detail: pd.DataFrame,
    projected_detail: pd.DataFrame,
    *,
    revenue_path: Path = REVENUE_HISTORY_CSV,
    price_dir: Path = PRICE_HISTORY_DIR,
    monthly_resolution_path: Path = MONTHLY_RESOLUTION_CSV,
    price_resolution_path: Path = PRICE_RESOLUTION_CSV,
    cutoff_date: str = CUTOFF_DATE,
    generated_at: str | None = None,
    projection_version: str = V1_PROJECTION_VERSION,
    projection_policy_id: str = V1_PROJECTION_POLICY_ID,
    predecessor_manifest_bytes_sha256: str = "",
    predecessor_detail_bytes_sha256: str = "",
) -> pd.DataFrame:
    cutoff = _digits(cutoff_date, 8, label="projection cutoff_date")
    if cutoff != CUTOFF_DATE:
        raise RuntimeError(f"projection cutoff drift: {cutoff}/{CUTOFF_DATE}")
    source_artifact_id, source_artifact_version = _require_source_identity(
        full_source_detail,
        projected_detail,
    )
    cutoff_revenue = load_cutoff_monthly_revenue_subset(
        Path(revenue_path),
        Path(monthly_resolution_path),
        cutoff_date=cutoff,
    )
    full_revenue = load_canonical_monthly_revenue_history(
        Path(revenue_path),
        Path(monthly_resolution_path),
    )
    monthly_registry = load_cross_market_resolutions(Path(monthly_resolution_path))
    price_registry = _read_registry(
        Path(price_resolution_path),
        label="price resolution registry",
    )
    monthly_ids, monthly_resolution_sha = _applied_monthly_resolutions(
        cutoff_revenue,
        monthly_registry,
        cutoff,
    )
    price_input_stock_ids = cutoff_price_input_stock_ids(
        cutoff_revenue,
        Path(price_dir),
    )
    price_ids, price_resolution_sha = _applied_price_resolutions(
        price_input_stock_ids,
        price_registry,
        cutoff,
    )
    price_lineage = cutoff_price_input_lineage(
        cutoff_revenue,
        Path(price_dir),
        cutoff_date=cutoff,
    )
    max_source_date, max_trade_date, max_end_date = _max_projected_dates(
        projected_detail
    )
    if any(value and value > cutoff for value in (max_source_date, max_trade_date, max_end_date)):
        raise RuntimeError(
            "projected source detail exceeds cutoff: "
            f"source={max_source_date}; trade={max_trade_date}; end={max_end_date}; cutoff={cutoff}"
        )
    monthly_blob_sha = monthly_revenue_history_blob_sha256(Path(revenue_path))
    monthly_table_sha = canonical_monthly_revenue_history_table_sha256(full_revenue)
    cutoff_monthly_table_sha = canonical_monthly_revenue_history_table_sha256(
        cutoff_revenue
    )
    monthly_registry_sha = cross_market_resolution_registry_canonical_sha256(
        monthly_registry
    )
    for frame, label in (
        (full_source_detail, "full source detail"),
        (projected_detail, "projected source detail"),
    ):
        captured_raw_blob_sha = _constant(
            frame,
            "monthly_revenue_history_blob_sha256",
            label=label,
        )
        if captured_raw_blob_sha != monthly_blob_sha:
            warnings.warn(
                f"{label} monthly_revenue_history_blob_sha256 differs from the current "
                "mutable blob; raw byte identity is provenance-only and canonical "
                "semantic lineage remains blocking",
                RuntimeWarning,
                stacklevel=2,
            )
        if (
            _constant(
                frame,
                "cross_market_resolution_registry_canonical_sha256",
                label=label,
            )
            != monthly_registry_sha
        ):
            raise RuntimeError(
                f"{label} cross_market_resolution_registry_canonical_sha256 "
                "does not match current canonical lineage"
            )
    if (
        _constant(
            full_source_detail,
            "monthly_revenue_canonical_table_sha256",
            label="full source detail",
        )
        != monthly_table_sha
    ):
        raise RuntimeError("full source detail canonical monthly lineage mismatch")
    if (
        _constant(
            projected_detail,
            "monthly_revenue_canonical_table_sha256",
            label="projected source detail",
        )
        != cutoff_monthly_table_sha
    ):
        raise RuntimeError("projected source detail cutoff monthly lineage mismatch")
    if projection_version == V1_PROJECTION_VERSION:
        if projection_policy_id != V1_PROJECTION_POLICY_ID:
            raise RuntimeError("v1 projection policy drift")
        manifest_columns = V1_MANIFEST_COLUMNS
    elif projection_version == V2_PROJECTION_VERSION:
        if projection_policy_id != V2_PROJECTION_POLICY_ID:
            raise RuntimeError("v2 projection policy drift")
        for label, value in (
            ("predecessor manifest", predecessor_manifest_bytes_sha256),
            ("predecessor detail", predecessor_detail_bytes_sha256),
        ):
            if not SHA256_PATTERN.fullmatch(value):
                raise RuntimeError(f"{label} bytes SHA-256 is invalid")
        if predecessor_manifest_bytes_sha256 != V1_EXPECTED_MANIFEST_BYTES_SHA256:
            raise RuntimeError("v2 predecessor manifest is not the canonical v1 bytes")
        if predecessor_detail_bytes_sha256 != V1_EXPECTED_DETAIL_BYTES_SHA256:
            raise RuntimeError("v2 predecessor detail is not the canonical v1 bytes")
        manifest_columns = V2_MANIFEST_COLUMNS
    else:
        raise RuntimeError(f"unsupported projection version: {projection_version}")
    row = {
        "generated_at": generated_at or _now_text(),
        "model_id": MODEL_ID,
        "artifact_id": ARTIFACT_ID,
        "artifact_version": projection_version,
        "projection_id": PROJECTION_ID,
        "projection_version": projection_version,
        "projection_policy_id": projection_policy_id,
        "cutoff_date": cutoff,
        "full_source_artifact_id": source_artifact_id,
        "full_source_artifact_version": source_artifact_version,
        "full_source_episode_row_count": len(full_source_detail),
        "full_source_episode_semantic_sha256": canonical_source_detail_semantic_sha256(
            full_source_detail
        ),
        "monthly_revenue_history_blob_sha256": monthly_blob_sha,
        "monthly_revenue_canonical_table_sha256": monthly_table_sha,
        "cross_market_resolution_registry_canonical_sha256": monthly_registry_sha,
        "cutoff_revenue_subset_row_count": len(cutoff_revenue),
        "cutoff_revenue_subset_semantic_sha256": cutoff_monthly_table_sha,
        "cutoff_price_input_stock_count": price_lineage["stock_count"],
        "cutoff_price_input_row_count": price_lineage["row_count"],
        "cutoff_price_input_file_semantic_sha256s": price_lineage[
            "file_semantic_sha256s"
        ],
        "cutoff_price_input_semantic_sha256": price_lineage["semantic_sha256"],
        "applied_monthly_resolution_count": len(monthly_ids),
        "applied_monthly_resolution_ids": "|".join(monthly_ids) or NO_RESOLUTION_ID,
        "applied_monthly_resolution_semantic_sha256": monthly_resolution_sha,
        "applied_price_resolution_count": len(price_ids),
        "applied_price_resolution_ids": "|".join(price_ids) or NO_RESOLUTION_ID,
        "applied_price_resolution_semantic_sha256": price_resolution_sha,
        "projected_episode_row_count": len(projected_detail),
        "projected_episode_semantic_sha256": (
            canonical_projected_source_detail_semantic_sha256(projected_detail)
        ),
        "projected_max_source_date": max_source_date,
        "projected_max_trade_date": max_trade_date,
        "projected_max_episode_end_date": max_end_date,
        "research_only": True,
        "formal_model_use_allowed": False,
        "approved_for_daily": False,
        "production_change": False,
        "promotion_evidence_allowed": False,
        "ranking_consumption_allowed": False,
        "pdf_consumption_allowed": False,
    }
    if projection_version == V2_PROJECTION_VERSION:
        row.update(
            {
                "predecessor_projection_version": V1_PROJECTION_VERSION,
                "predecessor_manifest_bytes_sha256": predecessor_manifest_bytes_sha256,
                "predecessor_detail_bytes_sha256": predecessor_detail_bytes_sha256,
                "lineage_change_reason": V2_LINEAGE_CHANGE_REASON,
                "candidate_status": V2_CANDIDATE_STATUS,
            }
        )
    manifest = pd.DataFrame([row], columns=list(manifest_columns))
    validate_projection_binding(manifest, projected_detail)
    return manifest


def build_source_snapshot_projection_v2_manifest(
    full_source_detail: pd.DataFrame,
    projected_detail: pd.DataFrame,
    *,
    predecessor_manifest_bytes_sha256: str,
    predecessor_detail_bytes_sha256: str,
    revenue_path: Path = REVENUE_HISTORY_CSV,
    price_dir: Path = PRICE_HISTORY_DIR,
    monthly_resolution_path: Path = MONTHLY_RESOLUTION_CSV,
    price_resolution_path: Path = PRICE_RESOLUTION_CSV,
    generated_at: str | None = None,
) -> pd.DataFrame:
    """Build the non-canonical v2 candidate bound to immutable v1 bytes."""

    return build_source_snapshot_projection_manifest(
        full_source_detail,
        projected_detail,
        revenue_path=revenue_path,
        price_dir=price_dir,
        monthly_resolution_path=monthly_resolution_path,
        price_resolution_path=price_resolution_path,
        cutoff_date=CUTOFF_DATE,
        generated_at=generated_at,
        projection_version=V2_PROJECTION_VERSION,
        projection_policy_id=V2_PROJECTION_POLICY_ID,
        predecessor_manifest_bytes_sha256=predecessor_manifest_bytes_sha256,
        predecessor_detail_bytes_sha256=predecessor_detail_bytes_sha256,
    )


def projection_binding_errors(
    manifest: pd.DataFrame,
    projected_detail: pd.DataFrame,
    *,
    expected_cutoff_date: str = CUTOFF_DATE,
) -> list[str]:
    errors: list[str] = []
    actual_columns = list(manifest.columns)
    if actual_columns not in (
        list(V1_MANIFEST_COLUMNS),
        list(V2_MANIFEST_COLUMNS),
    ):
        errors.append(
            "projection manifest schema mismatch: "
            f"expected_v1={list(V1_MANIFEST_COLUMNS)}; "
            f"expected_v2={list(V2_MANIFEST_COLUMNS)}; actual={actual_columns}"
        )
        return errors
    if len(manifest) != 1:
        errors.append(f"projection manifest must have exactly one row: {len(manifest)}")
        return errors
    row = manifest.iloc[0]
    version = _payload_value(row["projection_version"])
    if version == V1_PROJECTION_VERSION:
        expected_version = V1_PROJECTION_VERSION
        expected_policy = V1_PROJECTION_POLICY_ID
        if actual_columns != list(V1_MANIFEST_COLUMNS):
            errors.append("v1 projection manifest must use the immutable v1 schema")
    elif version == V2_PROJECTION_VERSION:
        expected_version = V2_PROJECTION_VERSION
        expected_policy = V2_PROJECTION_POLICY_ID
        if actual_columns != list(V2_MANIFEST_COLUMNS):
            errors.append("v2 projection manifest must use the v2 candidate schema")
        for column, expected in {
            "predecessor_projection_version": V1_PROJECTION_VERSION,
            "lineage_change_reason": V2_LINEAGE_CHANGE_REASON,
            "candidate_status": V2_CANDIDATE_STATUS,
        }.items():
            if _payload_value(row[column]) != expected:
                errors.append(
                    f"projection manifest {column} mismatch: "
                    f"{_payload_value(row[column])}/{expected}"
                )
        for column in (
            "predecessor_manifest_bytes_sha256",
            "predecessor_detail_bytes_sha256",
        ):
            if not SHA256_PATTERN.fullmatch(_payload_value(row[column])):
                errors.append(f"projection manifest {column} is not a SHA-256")
        if (
            _payload_value(row["predecessor_manifest_bytes_sha256"])
            != V1_EXPECTED_MANIFEST_BYTES_SHA256
        ):
            errors.append("projection manifest predecessor manifest is not canonical v1")
        if (
            _payload_value(row["predecessor_detail_bytes_sha256"])
            != V1_EXPECTED_DETAIL_BYTES_SHA256
        ):
            errors.append("projection manifest predecessor detail is not canonical v1")
    else:
        expected_version = version
        expected_policy = ""
        errors.append(f"unsupported projection version: {version}")
    expected_constants = {
        "model_id": MODEL_ID,
        "artifact_id": ARTIFACT_ID,
        "artifact_version": expected_version,
        "projection_id": PROJECTION_ID,
        "projection_version": expected_version,
        "projection_policy_id": expected_policy,
        "cutoff_date": expected_cutoff_date,
        "full_source_artifact_id": SOURCE_FIRST_ARTIFACT_ID,
    }
    for column, expected in expected_constants.items():
        if _payload_value(row[column]) != expected:
            errors.append(
                f"projection manifest {column} mismatch: {_payload_value(row[column])}/{expected}"
            )
    try:
        detail_artifact_id = _constant(
            projected_detail,
            "artifact_id",
            label="projected source detail",
        )
        detail_artifact_version = _constant(
            projected_detail,
            "artifact_version",
            label="projected source detail",
        )
        if detail_artifact_id != _payload_value(row["full_source_artifact_id"]):
            errors.append("projected detail artifact_id is not bound to manifest")
        if detail_artifact_version != _payload_value(row["full_source_artifact_version"]):
            errors.append("projected detail artifact_version is not bound to manifest")
        actual_sha = canonical_projected_source_detail_semantic_sha256(projected_detail)
        if actual_sha != _payload_value(row["projected_episode_semantic_sha256"]):
            errors.append("projected detail semantic SHA-256 is not bound to manifest")
        if len(projected_detail) != int(row["projected_episode_row_count"]):
            errors.append("projected detail row count is not bound to manifest")
        detail_raw_blob_sha = _constant(
            projected_detail,
            "monthly_revenue_history_blob_sha256",
            label="projected source detail",
        )
        manifest_raw_blob_sha = _payload_value(
            row["monthly_revenue_history_blob_sha256"]
        )
        if detail_raw_blob_sha != manifest_raw_blob_sha:
            warnings.warn(
                "projected detail monthly_revenue_history_blob_sha256 differs from the "
                "manifest provenance; raw byte identity is diagnostic-only",
                RuntimeWarning,
                stacklevel=2,
            )
        for column, manifest_column in (
            (
                "monthly_revenue_canonical_table_sha256",
                "cutoff_revenue_subset_semantic_sha256",
            ),
            (
                "cross_market_resolution_registry_canonical_sha256",
                "cross_market_resolution_registry_canonical_sha256",
            ),
        ):
            if _constant(
                projected_detail,
                column,
                label="projected source detail",
            ) != _payload_value(row[manifest_column]):
                errors.append(f"projected detail {column} is not bound to manifest")
        max_source, max_trade, max_end = _max_projected_dates(projected_detail)
        for column, actual in (
            ("projected_max_source_date", max_source),
            ("projected_max_trade_date", max_trade),
            ("projected_max_episode_end_date", max_end),
        ):
            if _payload_value(row[column]) != actual:
                errors.append(f"projected detail {column} is not bound to manifest")
            if actual and actual > expected_cutoff_date:
                errors.append(f"projected detail {column} exceeds cutoff: {actual}")
    except (RuntimeError, TypeError, ValueError) as exc:
        errors.append(str(exc))
    if _payload_value(row["research_only"]) != "true":
        errors.append("projection manifest research_only must be true")
    for column in (
        "formal_model_use_allowed",
        "approved_for_daily",
        "production_change",
        "promotion_evidence_allowed",
        "ranking_consumption_allowed",
        "pdf_consumption_allowed",
    ):
        if _payload_value(row[column]) != "false":
            errors.append(f"projection manifest {column} must be false")
    for column in (
        "full_source_episode_semantic_sha256",
        "monthly_revenue_history_blob_sha256",
        "monthly_revenue_canonical_table_sha256",
        "cross_market_resolution_registry_canonical_sha256",
        "cutoff_revenue_subset_semantic_sha256",
        "cutoff_price_input_semantic_sha256",
        "applied_monthly_resolution_semantic_sha256",
        "applied_price_resolution_semantic_sha256",
        "projected_episode_semantic_sha256",
    ):
        if not SHA256_PATTERN.fullmatch(_payload_value(row[column])):
            errors.append(f"projection manifest {column} is not a SHA-256")
    return errors


def validate_projection_binding(
    manifest: pd.DataFrame,
    projected_detail: pd.DataFrame,
    *,
    expected_cutoff_date: str = CUTOFF_DATE,
) -> None:
    errors = projection_binding_errors(
        manifest,
        projected_detail,
        expected_cutoff_date=expected_cutoff_date,
    )
    if errors:
        raise RuntimeError("source snapshot projection binding failed: " + "; ".join(errors))


def write_source_snapshot_projection(
    manifest: pd.DataFrame,
    projected_detail: pd.DataFrame,
    *,
    latest_manifest_path: Path = LATEST_MANIFEST_CSV,
    latest_detail_path: Path = LATEST_DETAIL_CSV,
    history_manifest_path: Path = HISTORY_MANIFEST_CSV,
    docs_manifest_path: Path = DOCS_MANIFEST_CSV,
) -> None:
    validate_projection_binding(manifest, projected_detail)
    projection_version = _payload_value(manifest.iloc[0]["projection_version"])
    if projection_version != V1_PROJECTION_VERSION:
        raise RuntimeError(
            "legacy canonical source snapshot projection writer accepts only "
            f"{V1_PROJECTION_VERSION}; received {projection_version}"
        )
    for path in (
        latest_manifest_path,
        latest_detail_path,
        history_manifest_path,
        docs_manifest_path,
    ):
        Path(path).parent.mkdir(parents=True, exist_ok=True)
    if Path(history_manifest_path).is_file():
        history = pd.read_csv(history_manifest_path, dtype=str, keep_default_na=False)
        if list(history.columns) != list(MANIFEST_COLUMNS):
            raise RuntimeError("source snapshot projection history schema mismatch")
        key_columns = ("projection_id", "projection_version", "cutoff_date")
        key_mask = pd.Series(True, index=history.index)
        for column in key_columns:
            key_mask &= history[column].eq(_payload_value(manifest.iloc[0][column]))
        matching = history.loc[key_mask]
        if not matching.empty:
            capture_columns = {
                "generated_at",
                "full_source_episode_row_count",
                "full_source_episode_semantic_sha256",
                "monthly_revenue_history_blob_sha256",
                "monthly_revenue_canonical_table_sha256",
                "cross_market_resolution_registry_canonical_sha256",
            }
            immutable_columns = [
                column for column in MANIFEST_COLUMNS if column not in capture_columns
            ]
            current_immutable_sha = _canonical_frame_sha256(
                manifest,
                columns=immutable_columns,
            )
            prior_immutable_shas = {
                _canonical_frame_sha256(
                    matching.loc[[index]],
                    columns=immutable_columns,
                )
                for index in matching.index
            }
            if prior_immutable_shas != {current_immutable_sha}:
                raise RuntimeError(
                    "source snapshot projection immutable history key changed semantics"
                )
            capture_identity_columns = [
                column for column in MANIFEST_COLUMNS if column != "generated_at"
            ]
            current_capture_sha = _canonical_frame_sha256(
                manifest,
                columns=capture_identity_columns,
            )
            prior_capture_shas = {
                _canonical_frame_sha256(
                    matching.loc[[index]],
                    columns=capture_identity_columns,
                )
                for index in matching.index
            }
            if current_capture_sha not in prior_capture_shas:
                history = pd.concat([history, manifest], ignore_index=True)
        else:
            history = pd.concat([history, manifest], ignore_index=True)
    else:
        history = manifest.copy()
    manifest.to_csv(latest_manifest_path, index=False)
    projected_detail.to_csv(latest_detail_path, index=False)
    manifest.to_csv(docs_manifest_path, index=False)
    history.to_csv(history_manifest_path, index=False)


def _artifact_path_text(path: Path) -> str:
    resolved = Path(path).resolve()
    try:
        return resolved.relative_to(ROOT.resolve()).as_posix()
    except ValueError:
        return resolved.as_posix()


def _write_immutable_bytes(path: Path, payload: bytes, *, label: str) -> None:
    target = Path(path)
    if target.is_file():
        if target.read_bytes() != payload:
            raise RuntimeError(f"{label} immutable target already exists with different bytes: {target}")
        return
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_bytes(payload)


def archive_immutable_v1_projection(
    *,
    canonical_manifest_path: Path = LATEST_MANIFEST_CSV,
    canonical_detail_path: Path = LATEST_DETAIL_CSV,
    archive_manifest_path: Path = V1_ARCHIVE_MANIFEST_CSV,
    archive_detail_path: Path = V1_ARCHIVE_DETAIL_CSV,
    evidence_path: Path = V1_ARCHIVE_EVIDENCE_CSV,
    expected_manifest_bytes: int = V1_EXPECTED_MANIFEST_BYTES,
    expected_manifest_bytes_sha256: str = V1_EXPECTED_MANIFEST_BYTES_SHA256,
    expected_detail_bytes: int = V1_EXPECTED_DETAIL_BYTES,
    expected_detail_bytes_sha256: str = V1_EXPECTED_DETAIL_BYTES_SHA256,
    expected_detail_row_count: int = V1_EXPECTED_DETAIL_ROW_COUNT,
    expected_detail_semantic_sha256: str = V1_EXPECTED_DETAIL_SEMANTIC_SHA256,
) -> pd.DataFrame:
    """Archive canonical v1 as raw bytes and emit immutable copy evidence."""

    for path, label in (
        (canonical_manifest_path, "canonical v1 manifest"),
        (canonical_detail_path, "canonical v1 detail"),
    ):
        if not Path(path).is_file():
            raise RuntimeError(f"missing {label}: {path}")
    manifest_bytes = Path(canonical_manifest_path).read_bytes()
    detail_bytes = Path(canonical_detail_path).read_bytes()
    manifest_sha = hashlib.sha256(manifest_bytes).hexdigest()
    detail_sha = hashlib.sha256(detail_bytes).hexdigest()
    for label, actual, expected in (
        ("canonical v1 manifest bytes", len(manifest_bytes), expected_manifest_bytes),
        ("canonical v1 manifest SHA-256", manifest_sha, expected_manifest_bytes_sha256),
        ("canonical v1 detail bytes", len(detail_bytes), expected_detail_bytes),
        ("canonical v1 detail SHA-256", detail_sha, expected_detail_bytes_sha256),
    ):
        if actual != expected:
            raise RuntimeError(f"{label} mismatch: {actual}/{expected}")
    manifest = pd.read_csv(
        canonical_manifest_path,
        dtype=str,
        keep_default_na=False,
    )
    detail = pd.read_csv(
        canonical_detail_path,
        dtype={"stock_id": str},
        keep_default_na=False,
        low_memory=False,
    )
    validate_projection_binding(manifest, detail)
    row = manifest.iloc[0]
    detail_semantic_sha = canonical_projected_source_detail_semantic_sha256(detail)
    for label, actual, expected in (
        ("canonical v1 projection version", _payload_value(row["projection_version"]), V1_PROJECTION_VERSION),
        ("canonical v1 policy", _payload_value(row["projection_policy_id"]), V1_PROJECTION_POLICY_ID),
        ("canonical v1 cutoff", _payload_value(row["cutoff_date"]), CUTOFF_DATE),
        ("canonical v1 detail row count", len(detail), expected_detail_row_count),
        (
            "canonical v1 detail semantic SHA-256",
            detail_semantic_sha,
            expected_detail_semantic_sha256,
        ),
    ):
        if actual != expected:
            raise RuntimeError(f"{label} mismatch: {actual}/{expected}")
    evidence = pd.DataFrame(
        [
            {
                "generated_at": _payload_value(row["generated_at"]),
                "model_id": MODEL_ID,
                "artifact_id": ARTIFACT_ID,
                "projection_id": PROJECTION_ID,
                "projection_version": V1_PROJECTION_VERSION,
                "cutoff_date": CUTOFF_DATE,
                "canonical_manifest_path": _artifact_path_text(canonical_manifest_path),
                "archive_manifest_path": _artifact_path_text(archive_manifest_path),
                "canonical_manifest_bytes": len(manifest_bytes),
                "canonical_manifest_sha256": manifest_sha,
                "canonical_detail_path": _artifact_path_text(canonical_detail_path),
                "archive_detail_path": _artifact_path_text(archive_detail_path),
                "canonical_detail_bytes": len(detail_bytes),
                "canonical_detail_sha256": detail_sha,
                "projected_episode_row_count": len(detail),
                "projected_episode_semantic_sha256": detail_semantic_sha,
                "immutable_copy_verified": True,
                "research_only": True,
                "formal_model_use_allowed": False,
                "approved_for_daily": False,
                "production_change": False,
                "promotion_evidence_allowed": False,
                "ranking_consumption_allowed": False,
                "pdf_consumption_allowed": False,
            }
        ],
        columns=list(ARCHIVE_EVIDENCE_COLUMNS),
    )
    evidence_bytes = evidence.to_csv(index=False, lineterminator="\n").encode("utf-8")
    _write_immutable_bytes(
        Path(archive_manifest_path),
        manifest_bytes,
        label="v1 manifest archive",
    )
    _write_immutable_bytes(
        Path(archive_detail_path),
        detail_bytes,
        label="v1 detail archive",
    )
    _write_immutable_bytes(
        Path(evidence_path),
        evidence_bytes,
        label="v1 archive evidence",
    )
    if Path(canonical_manifest_path).read_bytes() != manifest_bytes:
        raise RuntimeError("canonical v1 manifest changed during archive")
    if Path(canonical_detail_path).read_bytes() != detail_bytes:
        raise RuntimeError("canonical v1 detail changed during archive")
    return evidence


def write_source_snapshot_projection_v2_candidate(
    manifest: pd.DataFrame,
    projected_detail: pd.DataFrame,
    *,
    manifest_path: Path = V2_CANDIDATE_MANIFEST_CSV,
    detail_path: Path = V2_CANDIDATE_DETAIL_CSV,
    predecessor_manifest_path: Path = V1_ARCHIVE_MANIFEST_CSV,
    predecessor_detail_path: Path = V1_ARCHIVE_DETAIL_CSV,
) -> None:
    """Write v2 only to versioned candidate paths; canonical latest is untouched."""

    repository_root = Path(ROOT).resolve(strict=False)
    allowed_repository_destinations = {
        "manifest": Path(V2_CANDIDATE_MANIFEST_CSV).resolve(strict=False),
        "detail": Path(V2_CANDIDATE_DETAIL_CSV).resolve(strict=False),
    }
    for label, destination in (
        ("manifest", Path(manifest_path)),
        ("detail", Path(detail_path)),
    ):
        resolved = destination.resolve(strict=False)
        try:
            resolved.relative_to(repository_root)
        except ValueError:
            continue
        if os.path.normcase(str(resolved)) != os.path.normcase(
            str(allowed_repository_destinations[label])
        ):
            raise RuntimeError(
                "v2 candidate writer refuses a non-versioned repository "
                f"destination: {destination}"
            )

    validate_projection_binding(manifest, projected_detail)
    row = manifest.iloc[0]
    if _payload_value(row["projection_version"]) != V2_PROJECTION_VERSION:
        raise RuntimeError("v2 candidate writer received a non-v2 manifest")
    for path, column, label in (
        (
            predecessor_manifest_path,
            "predecessor_manifest_bytes_sha256",
            "v1 predecessor manifest",
        ),
        (
            predecessor_detail_path,
            "predecessor_detail_bytes_sha256",
            "v1 predecessor detail",
        ),
    ):
        if not Path(path).is_file():
            raise RuntimeError(f"missing {label}: {path}")
        if _file_sha256(Path(path)) != _payload_value(row[column]):
            raise RuntimeError(f"{label} SHA-256 does not match v2 manifest")
    manifest_bytes = manifest.to_csv(index=False, lineterminator="\n").encode("utf-8")
    detail_bytes = projected_detail.to_csv(index=False, lineterminator="\n").encode("utf-8")
    _write_immutable_bytes(
        Path(manifest_path),
        manifest_bytes,
        label="v2 candidate manifest",
    )
    _write_immutable_bytes(
        Path(detail_path),
        detail_bytes,
        label="v2 candidate detail",
    )


def _require_regular_file(path: Path, *, label: str) -> None:
    target = Path(path)
    if target.is_symlink() or not target.is_file():
        raise RuntimeError(f"missing or unsafe {label}: {target}")


def _single_row_csv(path: Path, *, label: str) -> pd.DataFrame:
    _require_regular_file(path, label=label)
    try:
        frame = pd.read_csv(path, dtype=str, keep_default_na=False, low_memory=False)
    except (OSError, pd.errors.ParserError) as exc:
        raise RuntimeError(f"{label} is unreadable: {path}: {exc}") from exc
    if len(frame) != 1:
        raise RuntimeError(f"{label} must contain exactly one row: {len(frame)}")
    return frame


def _supersede_source_identities(
    *,
    v1_manifest_path: Path,
    v1_detail_path: Path,
    candidate_manifest_path: Path,
    candidate_detail_path: Path,
    diff_summary_path: Path,
    diff_detail_path: Path,
) -> dict[str, object]:
    paths = {
        "immutable v1 manifest": Path(v1_manifest_path),
        "immutable v1 detail": Path(v1_detail_path),
        "v2 candidate manifest": Path(candidate_manifest_path),
        "v2 candidate detail": Path(candidate_detail_path),
        "v1/v2 diff summary": Path(diff_summary_path),
        "v1/v2 diff detail": Path(diff_detail_path),
    }
    for label, path in paths.items():
        _require_regular_file(path, label=label)

    payloads = {label: path.read_bytes() for label, path in paths.items()}
    shas = {
        label: hashlib.sha256(payload).hexdigest()
        for label, payload in payloads.items()
    }
    if len(payloads["immutable v1 manifest"]) != V1_EXPECTED_MANIFEST_BYTES:
        raise RuntimeError("immutable v1 manifest bytes changed before supersede")
    if shas["immutable v1 manifest"] != V1_EXPECTED_MANIFEST_BYTES_SHA256:
        raise RuntimeError("immutable v1 manifest SHA-256 changed before supersede")
    if len(payloads["immutable v1 detail"]) != V1_EXPECTED_DETAIL_BYTES:
        raise RuntimeError("immutable v1 detail bytes changed before supersede")
    if shas["immutable v1 detail"] != V1_EXPECTED_DETAIL_BYTES_SHA256:
        raise RuntimeError("immutable v1 detail SHA-256 changed before supersede")

    candidate_manifest = _single_row_csv(
        Path(candidate_manifest_path),
        label="v2 candidate manifest",
    )
    candidate_detail = pd.read_csv(
        candidate_detail_path,
        dtype={"stock_id": str},
        keep_default_na=False,
        low_memory=False,
    )
    validate_projection_binding(candidate_manifest, candidate_detail)
    candidate_row = candidate_manifest.iloc[0]
    expected_candidate = {
        "artifact_version": V2_PROJECTION_VERSION,
        "projection_version": V2_PROJECTION_VERSION,
        "projection_policy_id": V2_PROJECTION_POLICY_ID,
        "predecessor_projection_version": V1_PROJECTION_VERSION,
        "predecessor_manifest_bytes_sha256": V1_EXPECTED_MANIFEST_BYTES_SHA256,
        "predecessor_detail_bytes_sha256": V1_EXPECTED_DETAIL_BYTES_SHA256,
        "lineage_change_reason": V2_LINEAGE_CHANGE_REASON,
        "candidate_status": V2_CANDIDATE_STATUS,
    }
    for column, expected in expected_candidate.items():
        if _payload_value(candidate_row.get(column, "")) != expected:
            raise RuntimeError(
                f"v2 candidate {column} is not supersede eligible: "
                f"{_payload_value(candidate_row.get(column, ''))}/{expected}"
            )
    if _payload_value(candidate_row.get("research_only", "")).lower() != "true":
        raise RuntimeError("v2 candidate research_only must remain true")
    for column in (
        "formal_model_use_allowed",
        "approved_for_daily",
        "production_change",
        "promotion_evidence_allowed",
        "ranking_consumption_allowed",
        "pdf_consumption_allowed",
    ):
        if _payload_value(candidate_row.get(column, "")).lower() != "false":
            raise RuntimeError(f"v2 candidate {column} must remain false")

    diff_summary = _single_row_csv(
        Path(diff_summary_path),
        label="v1/v2 diff summary",
    )
    diff_row = diff_summary.iloc[0]
    expected_diff = {
        "v1_projection_version": V1_PROJECTION_VERSION,
        "v2_projection_version": V2_PROJECTION_VERSION,
        "v1_manifest_sha256": V1_EXPECTED_MANIFEST_BYTES_SHA256,
        "v1_detail_sha256": V1_EXPECTED_DETAIL_BYTES_SHA256,
        "v2_manifest_sha256": shas["v2 candidate manifest"],
        "v2_detail_sha256": shas["v2 candidate detail"],
        "unclassified_semantic_drift_count": "0",
        "semantic_drift_status": V2_DIFF_CLASSIFIED_STATUS,
    }
    for column, expected in expected_diff.items():
        if _payload_value(diff_row.get(column, "")) != expected:
            raise RuntimeError(
                f"v1/v2 diff {column} is not supersede eligible: "
                f"{_payload_value(diff_row.get(column, ''))}/{expected}"
            )
    if _payload_value(diff_row.get("research_only", "")).lower() != "true":
        raise RuntimeError("v1/v2 diff research_only must remain true")
    for column in (
        "formal_model_use_allowed",
        "approved_for_daily",
        "production_change",
        "promotion_evidence_allowed",
        "ranking_consumption_allowed",
        "pdf_consumption_allowed",
    ):
        if _payload_value(diff_row.get(column, "")).lower() != "false":
            raise RuntimeError(f"v1/v2 diff {column} must remain false")

    return {
        "payloads": payloads,
        "shas": shas,
        "candidate_manifest": candidate_manifest,
        "candidate_detail": candidate_detail,
    }


def _build_append_only_superseded_history(
    *,
    history_manifest_path: Path,
    candidate_manifest: pd.DataFrame,
) -> dict[str, object]:
    """Evolve the v1 history schema and append v2 without dropping a v1 row."""

    path = Path(history_manifest_path)
    _require_regular_file(path, label="canonical history manifest preimage")
    preimage_payload = path.read_bytes()
    try:
        preimage = pd.read_csv(path, dtype=str, keep_default_na=False)
    except (OSError, pd.errors.ParserError) as exc:
        raise RuntimeError(f"canonical history manifest is unreadable: {path}: {exc}") from exc
    if list(preimage.columns) != list(V1_MANIFEST_COLUMNS):
        raise RuntimeError(
            "canonical history manifest preimage must use the immutable v1 schema"
        )
    if preimage.empty:
        raise RuntimeError("canonical history manifest preimage has no v1 capture")
    if not preimage["projection_version"].eq(V1_PROJECTION_VERSION).all():
        raise RuntimeError(
            "canonical history manifest preimage contains a non-v1 projection"
        )
    reconstructed_preimage = preimage.to_csv(
        index=False,
        lineterminator="\n",
    ).encode("utf-8")
    if reconstructed_preimage != preimage_payload:
        raise RuntimeError(
            "canonical history manifest preimage is not canonical UTF-8/LF CSV"
        )
    if list(candidate_manifest.columns) != list(V2_MANIFEST_COLUMNS):
        raise RuntimeError("v2 candidate manifest schema cannot extend canonical history")
    if len(candidate_manifest) != 1:
        raise RuntimeError("v2 candidate manifest must contain exactly one history row")

    migrated_v1 = preimage.reindex(columns=V2_MANIFEST_COLUMNS, fill_value="")
    postimage = pd.concat([migrated_v1, candidate_manifest], ignore_index=True)
    postimage_payload = postimage.to_csv(
        index=False,
        lineterminator="\n",
    ).encode("utf-8")
    return {
        "preimage": preimage,
        "preimage_payload": preimage_payload,
        "preimage_sha256": hashlib.sha256(preimage_payload).hexdigest(),
        "preimage_semantic_sha256": _canonical_frame_sha256(
            preimage,
            columns=V1_MANIFEST_COLUMNS,
        ),
        "postimage": postimage,
        "postimage_payload": postimage_payload,
        "postimage_sha256": hashlib.sha256(postimage_payload).hexdigest(),
    }


def build_source_snapshot_projection_v2_supersede_evidence(
    *,
    superseded_at: str | None = None,
    v1_manifest_path: Path = V1_ARCHIVE_MANIFEST_CSV,
    v1_detail_path: Path = V1_ARCHIVE_DETAIL_CSV,
    candidate_manifest_path: Path = V2_CANDIDATE_MANIFEST_CSV,
    candidate_detail_path: Path = V2_CANDIDATE_DETAIL_CSV,
    diff_summary_path: Path = V1_V2_DIFF_SUMMARY_CSV,
    diff_detail_path: Path = V1_V2_DIFF_DETAIL_CSV,
    canonical_manifest_path: Path = LATEST_MANIFEST_CSV,
    canonical_detail_path: Path = LATEST_DETAIL_CSV,
    history_manifest_path: Path = HISTORY_MANIFEST_CSV,
    docs_manifest_path: Path = DOCS_MANIFEST_CSV,
) -> pd.DataFrame:
    identities = _supersede_source_identities(
        v1_manifest_path=Path(v1_manifest_path),
        v1_detail_path=Path(v1_detail_path),
        candidate_manifest_path=Path(candidate_manifest_path),
        candidate_detail_path=Path(candidate_detail_path),
        diff_summary_path=Path(diff_summary_path),
        diff_detail_path=Path(diff_detail_path),
    )
    payloads = identities["payloads"]
    shas = identities["shas"]
    candidate_row = identities["candidate_manifest"].iloc[0]
    canonical_v1_preimages = (
        (
            Path(canonical_manifest_path),
            payloads["immutable v1 manifest"],
            "canonical latest v1 manifest preimage",
        ),
        (
            Path(canonical_detail_path),
            payloads["immutable v1 detail"],
            "canonical latest v1 detail preimage",
        ),
        (
            Path(docs_manifest_path),
            payloads["immutable v1 manifest"],
            "canonical docs v1 manifest preimage",
        ),
    )
    for path, expected_payload, label in canonical_v1_preimages:
        _require_regular_file(path, label=label)
        if path.read_bytes() != expected_payload:
            raise RuntimeError(f"{label} differs from immutable v1 archive bytes")
    history = _build_append_only_superseded_history(
        history_manifest_path=Path(history_manifest_path),
        candidate_manifest=identities["candidate_manifest"],
    )
    preimage = history["preimage"]
    postimage = history["postimage"]
    row = {
        "superseded_at": superseded_at or _now_text(),
        "model_id": MODEL_ID,
        "artifact_id": V2_SUPERSEDE_EVIDENCE_ARTIFACT_ID,
        "artifact_version": V2_SUPERSEDE_EVIDENCE_ARTIFACT_VERSION,
        "projection_id": PROJECTION_ID,
        "selected_projection_version": V2_PROJECTION_VERSION,
        "selection_status": V2_SUPERSEDE_SELECTION_STATUS,
        "candidate_status": V2_CANDIDATE_STATUS,
        "candidate_manifest_path": _artifact_path_text(candidate_manifest_path),
        "candidate_manifest_bytes": len(payloads["v2 candidate manifest"]),
        "candidate_manifest_sha256": shas["v2 candidate manifest"],
        "candidate_detail_path": _artifact_path_text(candidate_detail_path),
        "candidate_detail_bytes": len(payloads["v2 candidate detail"]),
        "candidate_detail_sha256": shas["v2 candidate detail"],
        "v1_archive_manifest_path": _artifact_path_text(v1_manifest_path),
        "v1_archive_manifest_sha256": shas["immutable v1 manifest"],
        "v1_archive_detail_path": _artifact_path_text(v1_detail_path),
        "v1_archive_detail_sha256": shas["immutable v1 detail"],
        "v1_v2_diff_summary_path": _artifact_path_text(diff_summary_path),
        "v1_v2_diff_summary_sha256": shas["v1/v2 diff summary"],
        "v1_v2_diff_detail_path": _artifact_path_text(diff_detail_path),
        "v1_v2_diff_detail_sha256": shas["v1/v2 diff detail"],
        "canonical_latest_manifest_path": _artifact_path_text(canonical_manifest_path),
        "canonical_latest_detail_path": _artifact_path_text(canonical_detail_path),
        "canonical_history_manifest_path": _artifact_path_text(history_manifest_path),
        "canonical_docs_manifest_path": _artifact_path_text(docs_manifest_path),
        "canonical_exact3_manifest_sha256": shas["v2 candidate manifest"],
        "canonical_exact3_detail_sha256": shas["v2 candidate detail"],
        "canonical_exact3_verified": True,
        "canonical_history_preimage_bytes": len(history["preimage_payload"]),
        "canonical_history_preimage_sha256": history["preimage_sha256"],
        "canonical_history_preimage_row_count": len(preimage),
        "canonical_history_preimage_semantic_sha256": history[
            "preimage_semantic_sha256"
        ],
        "canonical_history_postimage_bytes": len(history["postimage_payload"]),
        "canonical_history_postimage_sha256": history["postimage_sha256"],
        "canonical_history_postimage_row_count": len(postimage),
        "canonical_history_postimage_v1_row_count": len(preimage),
        "canonical_history_postimage_v2_row_count": 1,
        "canonical_history_append_only_verified": True,
        "research_only": _payload_value(candidate_row["research_only"]),
        "formal_model_use_allowed": False,
        "approved_for_daily": False,
        "production_change": False,
        "promotion_evidence_allowed": False,
        "ranking_consumption_allowed": False,
        "pdf_consumption_allowed": False,
        "forward_holdout_refreshed": False,
    }
    return pd.DataFrame([row], columns=list(V2_SUPERSEDE_EVIDENCE_COLUMNS))


def source_snapshot_projection_v2_supersede_errors(
    *,
    evidence_path: Path = V2_SUPERSEDE_EVIDENCE_CSV,
    v1_manifest_path: Path = V1_ARCHIVE_MANIFEST_CSV,
    v1_detail_path: Path = V1_ARCHIVE_DETAIL_CSV,
    candidate_manifest_path: Path = V2_CANDIDATE_MANIFEST_CSV,
    candidate_detail_path: Path = V2_CANDIDATE_DETAIL_CSV,
    diff_summary_path: Path = V1_V2_DIFF_SUMMARY_CSV,
    diff_detail_path: Path = V1_V2_DIFF_DETAIL_CSV,
    canonical_manifest_path: Path = LATEST_MANIFEST_CSV,
    canonical_detail_path: Path = LATEST_DETAIL_CSV,
    history_manifest_path: Path = HISTORY_MANIFEST_CSV,
    docs_manifest_path: Path = DOCS_MANIFEST_CSV,
) -> list[str]:
    try:
        identities = _supersede_source_identities(
            v1_manifest_path=Path(v1_manifest_path),
            v1_detail_path=Path(v1_detail_path),
            candidate_manifest_path=Path(candidate_manifest_path),
            candidate_detail_path=Path(candidate_detail_path),
            diff_summary_path=Path(diff_summary_path),
            diff_detail_path=Path(diff_detail_path),
        )
        evidence = _single_row_csv(Path(evidence_path), label="v2 supersede evidence")
    except (RuntimeError, OSError, ValueError, KeyError, pd.errors.ParserError) as exc:
        return [str(exc)]

    errors: list[str] = []
    if list(evidence.columns) != list(V2_SUPERSEDE_EVIDENCE_COLUMNS):
        errors.append("v2 supersede evidence schema mismatch")
        return errors
    actual_row = evidence.iloc[0]
    superseded_at = _payload_value(actual_row.get("superseded_at", ""))
    if re.fullmatch(r"\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2} Asia/Taipei", superseded_at) is None:
        errors.append("v2 supersede evidence superseded_at is invalid")
    payloads = identities["payloads"]
    shas = identities["shas"]
    expected_values = {
        "model_id": MODEL_ID,
        "artifact_id": V2_SUPERSEDE_EVIDENCE_ARTIFACT_ID,
        "artifact_version": V2_SUPERSEDE_EVIDENCE_ARTIFACT_VERSION,
        "projection_id": PROJECTION_ID,
        "selected_projection_version": V2_PROJECTION_VERSION,
        "selection_status": V2_SUPERSEDE_SELECTION_STATUS,
        "candidate_status": V2_CANDIDATE_STATUS,
        "candidate_manifest_path": _artifact_path_text(candidate_manifest_path),
        "candidate_manifest_bytes": len(payloads["v2 candidate manifest"]),
        "candidate_manifest_sha256": shas["v2 candidate manifest"],
        "candidate_detail_path": _artifact_path_text(candidate_detail_path),
        "candidate_detail_bytes": len(payloads["v2 candidate detail"]),
        "candidate_detail_sha256": shas["v2 candidate detail"],
        "v1_archive_manifest_path": _artifact_path_text(v1_manifest_path),
        "v1_archive_manifest_sha256": shas["immutable v1 manifest"],
        "v1_archive_detail_path": _artifact_path_text(v1_detail_path),
        "v1_archive_detail_sha256": shas["immutable v1 detail"],
        "v1_v2_diff_summary_path": _artifact_path_text(diff_summary_path),
        "v1_v2_diff_summary_sha256": shas["v1/v2 diff summary"],
        "v1_v2_diff_detail_path": _artifact_path_text(diff_detail_path),
        "v1_v2_diff_detail_sha256": shas["v1/v2 diff detail"],
        "canonical_latest_manifest_path": _artifact_path_text(canonical_manifest_path),
        "canonical_latest_detail_path": _artifact_path_text(canonical_detail_path),
        "canonical_history_manifest_path": _artifact_path_text(history_manifest_path),
        "canonical_docs_manifest_path": _artifact_path_text(docs_manifest_path),
        "canonical_exact3_manifest_sha256": shas["v2 candidate manifest"],
        "canonical_exact3_detail_sha256": shas["v2 candidate detail"],
        "canonical_exact3_verified": True,
        "research_only": True,
        "formal_model_use_allowed": False,
        "approved_for_daily": False,
        "production_change": False,
        "promotion_evidence_allowed": False,
        "ranking_consumption_allowed": False,
        "pdf_consumption_allowed": False,
        "forward_holdout_refreshed": False,
    }
    for column, expected_value in expected_values.items():
        if _payload_value(actual_row.get(column, "")) != _payload_value(expected_value):
            errors.append(f"v2 supersede evidence {column} mismatch")

    candidate_manifest_bytes = Path(candidate_manifest_path).read_bytes()
    candidate_detail_bytes = Path(candidate_detail_path).read_bytes()
    exact3 = (
        (Path(canonical_manifest_path), candidate_manifest_bytes, "canonical latest manifest"),
        (Path(canonical_detail_path), candidate_detail_bytes, "canonical latest detail"),
        (Path(docs_manifest_path), candidate_manifest_bytes, "canonical docs manifest"),
    )
    for path, expected_bytes, label in exact3:
        if path.is_symlink() or not path.is_file():
            errors.append(f"missing or unsafe {label}: {path}")
        elif path.read_bytes() != expected_bytes:
            errors.append(f"{label} differs from immutable v2 candidate bytes")

    history_path = Path(history_manifest_path)
    if history_path.is_symlink() or not history_path.is_file():
        errors.append(f"missing or unsafe canonical history manifest: {history_path}")
        return errors
    try:
        history_payload = history_path.read_bytes()
        history = pd.read_csv(history_path, dtype=str, keep_default_na=False)
    except (OSError, pd.errors.ParserError) as exc:
        errors.append(f"canonical history manifest is unreadable: {exc}")
        return errors
    if list(history.columns) != list(V2_MANIFEST_COLUMNS):
        errors.append("canonical history manifest postimage schema mismatch")
        return errors
    versions = history["projection_version"]
    v1_history = history.loc[versions.eq(V1_PROJECTION_VERSION)].copy()
    v2_history = history.loc[versions.eq(V2_PROJECTION_VERSION)].copy()
    if len(v1_history) + len(v2_history) != len(history):
        errors.append("canonical history manifest contains an unexpected projection version")
    if len(v1_history) < 1 or len(v2_history) != 1:
        errors.append("canonical history manifest must retain v1 rows and append one v2 row")
    if not versions.iloc[:-1].eq(V1_PROJECTION_VERSION).all() or (
        versions.iloc[-1] != V2_PROJECTION_VERSION
    ):
        errors.append("canonical history manifest is not append-only v1 then v2")
    for column in V2_MANIFEST_EXTENSION_COLUMNS:
        if not v1_history[column].eq("").all():
            errors.append(f"canonical history v1 row changed extension column: {column}")
    candidate_manifest = identities["candidate_manifest"].reset_index(drop=True)
    if not v2_history.reset_index(drop=True).equals(candidate_manifest):
        errors.append("canonical history v2 row differs from immutable v2 candidate")

    reconstructed_preimage = v1_history.loc[:, V1_MANIFEST_COLUMNS].to_csv(
        index=False,
        lineterminator="\n",
    ).encode("utf-8")
    history_values = {
        "canonical_history_preimage_bytes": len(reconstructed_preimage),
        "canonical_history_preimage_sha256": hashlib.sha256(
            reconstructed_preimage
        ).hexdigest(),
        "canonical_history_preimage_row_count": len(v1_history),
        "canonical_history_preimage_semantic_sha256": _canonical_frame_sha256(
            v1_history,
            columns=V1_MANIFEST_COLUMNS,
        ),
        "canonical_history_postimage_bytes": len(history_payload),
        "canonical_history_postimage_sha256": hashlib.sha256(history_payload).hexdigest(),
        "canonical_history_postimage_row_count": len(history),
        "canonical_history_postimage_v1_row_count": len(v1_history),
        "canonical_history_postimage_v2_row_count": len(v2_history),
        "canonical_history_append_only_verified": True,
    }
    for column, expected_value in history_values.items():
        if _payload_value(actual_row.get(column, "")) != _payload_value(expected_value):
            errors.append(f"v2 supersede evidence {column} mismatch")
    return errors


def validate_source_snapshot_projection_v2_supersede(
    **kwargs: object,
) -> None:
    errors = source_snapshot_projection_v2_supersede_errors(**kwargs)
    if errors:
        raise RuntimeError("source snapshot projection v2 supersede binding failed: " + "; ".join(errors))


def _write_temp_payload(path: Path, payload: bytes) -> Path:
    target = Path(path)
    target.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.NamedTemporaryFile(
        mode="wb",
        delete=False,
        dir=target.parent,
        prefix=f".{target.name}.",
        suffix=".tmp",
    ) as handle:
        handle.write(payload)
        handle.flush()
        os.fsync(handle.fileno())
        return Path(handle.name)


def _replace_payloads_with_rollback(payloads: tuple[tuple[Path, bytes], ...]) -> None:
    previous: dict[Path, bytes | None] = {}
    staged: dict[Path, Path] = {}
    replaced: list[Path] = []
    try:
        for path, payload in payloads:
            target = Path(path)
            if target.is_symlink() or target.is_dir():
                raise RuntimeError(f"supersede destination is unsafe: {target}")
            previous[target] = target.read_bytes() if target.is_file() else None
            staged[target] = _write_temp_payload(target, payload)
        for path, _payload in payloads:
            target = Path(path)
            os.replace(staged[target], target)
            replaced.append(target)
    except Exception:
        for target in reversed(replaced):
            prior = previous[target]
            if prior is None:
                target.unlink(missing_ok=True)
            else:
                restore = _write_temp_payload(target, prior)
                os.replace(restore, target)
        raise
    finally:
        for temporary in staged.values():
            temporary.unlink(missing_ok=True)


def supersede_source_snapshot_projection_v2_candidate(
    *,
    superseded_at: str | None = None,
    evidence_path: Path = V2_SUPERSEDE_EVIDENCE_CSV,
    v1_manifest_path: Path = V1_ARCHIVE_MANIFEST_CSV,
    v1_detail_path: Path = V1_ARCHIVE_DETAIL_CSV,
    candidate_manifest_path: Path = V2_CANDIDATE_MANIFEST_CSV,
    candidate_detail_path: Path = V2_CANDIDATE_DETAIL_CSV,
    diff_summary_path: Path = V1_V2_DIFF_SUMMARY_CSV,
    diff_detail_path: Path = V1_V2_DIFF_DETAIL_CSV,
    canonical_manifest_path: Path = LATEST_MANIFEST_CSV,
    canonical_detail_path: Path = LATEST_DETAIL_CSV,
    history_manifest_path: Path = HISTORY_MANIFEST_CSV,
    docs_manifest_path: Path = DOCS_MANIFEST_CSV,
) -> pd.DataFrame:
    """Select immutable v2 as research canonical without changing formal-use flags."""

    repository_root = Path(ROOT).resolve(strict=False)
    repository_contract = {
        "evidence_path": (Path(evidence_path), V2_SUPERSEDE_EVIDENCE_CSV),
        "v1_manifest_path": (Path(v1_manifest_path), V1_ARCHIVE_MANIFEST_CSV),
        "v1_detail_path": (Path(v1_detail_path), V1_ARCHIVE_DETAIL_CSV),
        "candidate_manifest_path": (
            Path(candidate_manifest_path),
            V2_CANDIDATE_MANIFEST_CSV,
        ),
        "candidate_detail_path": (Path(candidate_detail_path), V2_CANDIDATE_DETAIL_CSV),
        "diff_summary_path": (Path(diff_summary_path), V1_V2_DIFF_SUMMARY_CSV),
        "diff_detail_path": (Path(diff_detail_path), V1_V2_DIFF_DETAIL_CSV),
        "canonical_manifest_path": (Path(canonical_manifest_path), LATEST_MANIFEST_CSV),
        "canonical_detail_path": (Path(canonical_detail_path), LATEST_DETAIL_CSV),
        "history_manifest_path": (Path(history_manifest_path), HISTORY_MANIFEST_CSV),
        "docs_manifest_path": (Path(docs_manifest_path), DOCS_MANIFEST_CSV),
    }
    for label, (actual, required) in repository_contract.items():
        resolved = actual.resolve(strict=False)
        try:
            resolved.relative_to(repository_root)
        except ValueError:
            continue
        if resolved != Path(required).resolve(strict=False):
            raise RuntimeError(
                "source snapshot projection v2 supersede repository path is not "
                f"authorized: {label}: {actual}"
            )

    common = {
        "evidence_path": Path(evidence_path),
        "v1_manifest_path": Path(v1_manifest_path),
        "v1_detail_path": Path(v1_detail_path),
        "candidate_manifest_path": Path(candidate_manifest_path),
        "candidate_detail_path": Path(candidate_detail_path),
        "diff_summary_path": Path(diff_summary_path),
        "diff_detail_path": Path(diff_detail_path),
        "canonical_manifest_path": Path(canonical_manifest_path),
        "canonical_detail_path": Path(canonical_detail_path),
        "history_manifest_path": Path(history_manifest_path),
        "docs_manifest_path": Path(docs_manifest_path),
    }
    if Path(evidence_path).exists() or Path(evidence_path).is_symlink():
        validate_source_snapshot_projection_v2_supersede(**common)
        return pd.read_csv(evidence_path, dtype=str, keep_default_na=False)

    evidence = build_source_snapshot_projection_v2_supersede_evidence(
        superseded_at=superseded_at,
        **{key: value for key, value in common.items() if key != "evidence_path"},
    )
    evidence_bytes = evidence.to_csv(index=False, lineterminator="\n").encode("utf-8")
    candidate_manifest_bytes = Path(candidate_manifest_path).read_bytes()
    candidate_detail_bytes = Path(candidate_detail_path).read_bytes()
    candidate_manifest = _single_row_csv(
        Path(candidate_manifest_path),
        label="v2 candidate manifest",
    )
    history = _build_append_only_superseded_history(
        history_manifest_path=Path(history_manifest_path),
        candidate_manifest=candidate_manifest,
    )
    writes = (
        (Path(canonical_manifest_path), candidate_manifest_bytes),
        (Path(canonical_detail_path), candidate_detail_bytes),
        (Path(history_manifest_path), history["postimage_payload"]),
        (Path(docs_manifest_path), candidate_manifest_bytes),
        (Path(evidence_path), evidence_bytes),
    )
    originals = {
        path: path.read_bytes() if path.is_file() and not path.is_symlink() else None
        for path, _payload in writes
    }
    _replace_payloads_with_rollback(writes)
    try:
        validate_source_snapshot_projection_v2_supersede(**common)
        if Path(candidate_manifest_path).read_bytes() != candidate_manifest_bytes:
            raise RuntimeError("immutable v2 candidate manifest changed during supersede")
        if Path(candidate_detail_path).read_bytes() != candidate_detail_bytes:
            raise RuntimeError("immutable v2 candidate detail changed during supersede")
    except Exception:
        rollback = tuple(
            (path, payload)
            for path, payload in originals.items()
            if payload is not None
        )
        for path, payload in originals.items():
            if payload is None:
                path.unlink(missing_ok=True)
        if rollback:
            _replace_payloads_with_rollback(rollback)
        raise
    return evidence


def load_source_snapshot_projection_manifest(
    path: Path = LATEST_MANIFEST_CSV,
) -> pd.DataFrame:
    if not Path(path).is_file():
        raise RuntimeError(f"missing source snapshot projection manifest: {path}")
    return pd.read_csv(path, dtype=str, keep_default_na=False)


def load_projected_source_detail(path: Path = LATEST_DETAIL_CSV) -> pd.DataFrame:
    if not Path(path).is_file():
        raise RuntimeError(f"missing projected source detail: {path}")
    return pd.read_csv(
        path,
        dtype={"stock_id": str},
        keep_default_na=False,
        low_memory=False,
    )
