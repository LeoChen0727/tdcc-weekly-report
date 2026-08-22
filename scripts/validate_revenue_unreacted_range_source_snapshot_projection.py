from __future__ import annotations

import argparse
from decimal import Decimal, InvalidOperation
import hashlib
import json
from pathlib import Path
import re

import numpy as np
import pandas as pd

from validate_revenue_unreacted_range_source_snapshot_projection_v1_v2_diff import (
    validate as validate_projection_v1_v2_diff,
)


ROOT = Path(__file__).resolve().parents[1]
MODEL_ID = "revenue_unreacted_range"
ARTIFACT_ID = "revenue_unreacted_range_source_snapshot_projection"
V1_ARTIFACT_VERSION = "source_snapshot_projection_v1_20260731"
V2_ARTIFACT_VERSION = "source_snapshot_projection_v2_20260822"
ARTIFACT_VERSION = V1_ARTIFACT_VERSION
PROJECTION_ID = "revenue_unreacted_range_source_snapshot_asof_20260713"
PROJECTION_VERSION = V1_ARTIFACT_VERSION
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
CANONICAL_JSON_VERSION = "revenue_source_snapshot_projection_canonical_json_v1"
MONTHLY_CANONICAL_JSON_VERSION = "canonical_json_v1"
NO_RESOLUTION_ID = "none"
PROJECTED_CAPTURE_LINEAGE_COLUMNS = (
    "monthly_revenue_history_blob_sha256",
    "cross_market_resolution_registry_canonical_sha256",
)

MANIFEST_CSV = (
    ROOT
    / "output/latest/research_backtest/"
    "revenue_unreacted_range_source_snapshot_projection_manifest_latest.csv"
)
PROJECTED_DETAIL_CSV = (
    ROOT
    / "output/latest/research_backtest/"
    "revenue_unreacted_range_source_snapshot_projection_detail_latest.csv"
)
V2_MANIFEST_CSV = (
    ROOT
    / "output/history/research/"
    "revenue_unreacted_range_source_snapshot_projection_manifest_v2_20260822.csv"
)
V2_PROJECTED_DETAIL_CSV = (
    ROOT
    / "output/history/research/"
    "revenue_unreacted_range_source_snapshot_projection_detail_v2_20260822.csv"
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
V1_EXPECTED_CUTOFF_PRICE_INPUT_SEMANTIC_SHA256 = (
    "b6eec3d62cca5b32efbe9b81acc1dcc6709f37c77f7af59eb860c23603422787"
)
V1_EXPECTED_PREDECESSOR_MANIFEST_SHA256 = V1_EXPECTED_MANIFEST_BYTES_SHA256
V1_EXPECTED_PREDECESSOR_DETAIL_SHA256 = V1_EXPECTED_DETAIL_BYTES_SHA256
V1_ARCHIVE_EVIDENCE_COLUMNS = (
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
REVENUE_HISTORY_CSV = ROOT / "data/monthly_revenue_history/monthly_revenue_history.csv"
PRICE_HISTORY_DIR = ROOT / "data/stock_price_history"
MONTHLY_RESOLUTION_CSV = (
    ROOT / "config/revenue_unreacted_range_monthly_revenue_cross_market_resolution.csv"
)
PRICE_RESOLUTION_CSV = (
    ROOT / "config/revenue_unreacted_range_price_comparability_resolution.csv"
)

SOURCE_IDENTITY_COLUMNS = (
    "market",
    "source_market_name",
    "source_table_date",
    "source_kind",
    "source_url",
    "source_file",
)
BUSINESS_PAYLOAD_COLUMNS = (
    "stock_id",
    "stock_name",
    "industry",
    "revenue_period",
    "revenue_period_roc",
    "monthly_revenue",
    "previous_month_revenue",
    "last_year_month_revenue",
    "month_over_month_pct",
    "latest_revenue_yoy_pct",
    "cumulative_revenue",
    "last_year_cumulative_revenue",
    "cumulative_revenue_yoy_pct",
    "note",
    "revenue_positive_flag",
    "revenue_strong_flag",
    "revenue_numerical_anomaly_flag",
    "revenue_numerical_anomaly_reason",
    "point_in_time_status",
    "research_join_allowed",
    "allowed_for_formal_historical_model_use",
    "formal_use_blocker",
    "coverage_note",
)
RAW_ROW_CANONICAL_COLUMNS = SOURCE_IDENTITY_COLUMNS + BUSINESS_PAYLOAD_COLUMNS
RAW_ROW_NUMERIC_COLUMNS = (
    "monthly_revenue",
    "previous_month_revenue",
    "last_year_month_revenue",
    "month_over_month_pct",
    "latest_revenue_yoy_pct",
    "cumulative_revenue",
    "last_year_cumulative_revenue",
    "cumulative_revenue_yoy_pct",
)
RAW_ROW_BOOLEAN_COLUMNS = (
    "revenue_positive_flag",
    "revenue_strong_flag",
    "revenue_numerical_anomaly_flag",
    "research_join_allowed",
    "allowed_for_formal_historical_model_use",
)
MONTHLY_RESOLUTION_COLUMNS = (
    "resolution_id",
    "model_id",
    "stock_id",
    "revenue_period",
    "earlier_market",
    "earlier_source_market_name",
    "earlier_source_table_date",
    "earlier_source_kind",
    "earlier_source_url",
    "earlier_source_file",
    "earlier_raw_row_canonical_sha256",
    "later_market",
    "later_source_market_name",
    "later_source_table_date",
    "later_source_kind",
    "later_source_url",
    "later_source_file",
    "later_raw_row_canonical_sha256",
    "official_market_transition_date",
    "canonical_source_table_date",
    "canonical_row_canonical_sha256",
    "resolution_status",
    "canonicalization_policy",
    "evidence_url",
    "formal_model_use_allowed",
    "notes",
)
MONTHLY_REGISTRY_CANONICAL_COLUMNS = MONTHLY_RESOLUTION_COLUMNS[:-1]
MONTHLY_REGISTRY_SORT_KEYS = (
    "model_id",
    "stock_id",
    "revenue_period",
    "resolution_id",
)
MONTHLY_BINDING_COLUMNS = (
    "stock_id",
    "revenue_period",
    "source_row_canonical_sha256",
    "cross_market_resolution_id",
    "canonical_source_table_date",
)
PRICE_INPUT_COLUMNS = (
    "date",
    "open",
    "high",
    "low",
    "close",
    "volume",
    "volume_ratio",
)
PRICE_RESOLUTION_REQUIRED_COLUMNS = (
    "resolution_id",
    "model_id",
    "stock_id",
    "resume_date",
    "exchange_ratio",
    "root_cause_status",
)
SOURCE_FIRST_ARTIFACT_VERSION = "source_first_condition_v3_20260720"
DISCOVERY_HORIZON_DAYS = 126
OUTCOME_WINDOW_DAYS = 20
FIRST_HIT_DEADLINE_DAYS = 15
BASELINE_VARIANT_ID = "absolute_strong"
PRIMARY_VARIANT_ID = "absolute_or_two_month_yoy_ge15"
INCREMENTAL_VARIANT_ID = "two_month_yoy_ge15_only"
CONDITION_VARIANT_IDS = (
    BASELINE_VARIANT_ID,
    "absolute_or_latest_yoy_ge15",
    "absolute_or_two_month_yoy_ge10",
    "absolute_or_two_month_yoy_ge12_5",
    PRIMARY_VARIANT_ID,
    "absolute_or_two_month_yoy_ge17_5",
    "absolute_or_two_month_yoy_ge18",
    "absolute_or_two_month_yoy_ge20",
    "absolute_or_two_month_yoy_ge25",
    "absolute_or_two_month_yoy_ge15_cumulative_improving",
    "absolute_or_turn_positive_accel20",
    "absolute_or_positive_accel20",
    INCREMENTAL_VARIANT_ID,
)
FINANCIAL_STATEMENT_SCOPE = (
    "monthly_revenue_only;EPS_gross_margin_operating_margin_operating_income_"
    "non_operating_income_net_income_excluded"
)
SOURCE_DETAIL_COLUMNS = (
    "generated_at",
    "model_id",
    "artifact_id",
    "artifact_version",
    "monthly_revenue_history_blob_sha256",
    "monthly_revenue_canonical_table_sha256",
    "cross_market_resolution_registry_canonical_sha256",
    "condition_variant_id",
    "episode_key",
    "stock_id",
    "stock_name",
    "episode_number",
    "episode_start_revenue_period",
    "episode_start_source_date",
    "episode_start_cross_market_resolution_id",
    "episode_start_source_row_canonical_sha256",
    "episode_start_canonical_source_table_date",
    "episode_start_trade_date",
    "episode_start_sequence_index",
    "latest_qualifying_revenue_period",
    "latest_qualifying_source_date",
    "latest_qualifying_cross_market_resolution_id",
    "latest_qualifying_source_row_canonical_sha256",
    "latest_qualifying_canonical_source_table_date",
    "latest_qualifying_trade_date",
    "latest_qualifying_sequence_index",
    "qualifying_update_count",
    "qualifying_revenue_periods",
    "qualifying_source_dates",
    "qualifying_cross_market_resolution_ids",
    "qualifying_source_row_canonical_sha256s",
    "qualifying_canonical_source_table_dates",
    "qualifying_trade_dates",
    "qualifying_sequence_indices",
    "episode_end_sequence_index",
    "episode_end_date",
    "episode_status",
    "start_latest_revenue_yoy_pct",
    "start_cumulative_revenue_yoy_pct",
    "start_previous_latest_revenue_yoy_pct",
    "start_latest_yoy_delta_pct_points",
    "start_month_over_month_pct",
    "start_source_revenue_anomaly_candidate_flag",
    "qualifying_source_revenue_anomaly_candidate_flag",
    "source_price_unreacted_flag",
    "source_close",
    "source_return_5d_pct",
    "source_return_20d_pct",
    "source_volume_ratio",
    "source_range_width_23d_pct",
    "first_breakout_date",
    "first_breakout_lag_from_episode_start_days",
    "first_breakout_outcome",
    "first_breakout_d20_return_pct",
    "launch_date",
    "launch_lag_from_episode_start_days",
    "launch_lag_from_latest_source_days",
    "first_hit_20_day_offset",
    "launch_d20_return_pct",
    "launch_post_hit_min_return_pct",
    "price_path_threshold_candidate_flag",
    "price_path_resolution_ids",
    "unresolved_price_path_candidate_flag",
    "same_stock_non_overlap_applied",
    "right_censored_flag",
    "retrospective_label_status",
    "financial_statement_scope",
    "approved_for_daily",
    "production_change",
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
V2_MANIFEST_COLUMNS = V1_MANIFEST_COLUMNS + (
    "predecessor_projection_version",
    "predecessor_manifest_bytes_sha256",
    "predecessor_detail_bytes_sha256",
    "lineage_change_reason",
    "candidate_status",
)
MANIFEST_COLUMNS = V1_MANIFEST_COLUMNS
SHA256_PATTERN = re.compile(r"^[0-9a-f]{64}$")


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
    return hashlib.sha256(
        json.dumps(
            payload,
            ensure_ascii=False,
            separators=(",", ":"),
        ).encode("utf-8")
    ).hexdigest()


def _file_sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with Path(path).open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def _stock_id(value: object) -> str:
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


def _canonical_numeric(value: object) -> str:
    text = _payload_value(value)
    if not text:
        return ""
    try:
        number = Decimal(text)
    except InvalidOperation as exc:
        raise RuntimeError(f"invalid canonical numeric value: {text}") from exc
    if not number.is_finite():
        raise RuntimeError(f"non-finite canonical numeric value: {text}")
    if number == 0:
        return "0"
    rendered = format(number.normalize(), "f")
    return rendered.rstrip("0").rstrip(".") if "." in rendered else rendered


def _canonical_raw_value(column: str, value: object) -> str:
    if column == "stock_id":
        return _stock_id(value)
    if column == "revenue_period":
        return _digits(value, 6, label="revenue_period")
    if column == "source_table_date":
        return _digits(value, 8, label="source_table_date")
    if column == "market":
        return _payload_value(value).lower()
    if column == "source_market_name":
        return _payload_value(value).upper()
    if column in RAW_ROW_NUMERIC_COLUMNS:
        return _canonical_numeric(value)
    if column in RAW_ROW_BOOLEAN_COLUMNS:
        text = _payload_value(value).lower()
        if text not in {"true", "false"}:
            raise RuntimeError(f"invalid canonical boolean: {column}={text}")
        return text
    return _payload_value(value)


def _raw_row_sha256(row: pd.Series) -> str:
    missing = sorted(set(RAW_ROW_CANONICAL_COLUMNS) - set(row.index))
    if missing:
        raise RuntimeError(f"monthly raw row is missing columns: {missing}")
    values = [_canonical_raw_value(column, row[column]) for column in RAW_ROW_CANONICAL_COLUMNS]
    return _canonical_json_sha256(
        [MONTHLY_CANONICAL_JSON_VERSION, list(RAW_ROW_CANONICAL_COLUMNS), values]
    )


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


def _source_detail_sha256(frame: pd.DataFrame) -> str:
    return _canonical_frame_sha256(frame, excluded_columns=("generated_at",))


def _projected_source_detail_sha256(frame: pd.DataFrame) -> str:
    return _canonical_frame_sha256(
        frame,
        excluded_columns=("generated_at", *PROJECTED_CAPTURE_LINEAGE_COLUMNS),
    )


def _normalize_monthly_registry(registry: pd.DataFrame) -> pd.DataFrame:
    if tuple(registry.columns) != MONTHLY_RESOLUTION_COLUMNS:
        raise RuntimeError("monthly resolution registry schema mismatch")
    if registry.empty:
        raise RuntimeError("monthly resolution registry is empty")
    normalized = registry.copy()
    normalized["stock_id"] = normalized["stock_id"].map(_stock_id)
    normalized["revenue_period"] = normalized["revenue_period"].map(
        lambda value: _digits(value, 6, label="registry revenue_period")
    )
    for column in (
        "earlier_source_table_date",
        "later_source_table_date",
        "official_market_transition_date",
        "canonical_source_table_date",
    ):
        normalized[column] = normalized[column].map(
            lambda value: _digits(value, 8, label=f"registry {column}")
        )
    for column in ("earlier_market", "later_market"):
        normalized[column] = normalized[column].str.strip().str.lower()
    for column in ("earlier_source_market_name", "later_source_market_name"):
        normalized[column] = normalized[column].str.strip().str.upper()
    for column in (
        "earlier_source_kind",
        "earlier_source_url",
        "earlier_source_file",
        "later_source_kind",
        "later_source_url",
        "later_source_file",
    ):
        normalized[column] = normalized[column].astype(str).str.strip()
    for column in (
        "earlier_raw_row_canonical_sha256",
        "later_raw_row_canonical_sha256",
        "canonical_row_canonical_sha256",
    ):
        normalized[column] = normalized[column].astype(str).str.strip().str.lower()
    if normalized[["stock_id", "revenue_period"]].eq("").any(axis=None):
        raise RuntimeError("monthly resolution registry has blank keys")
    if normalized["resolution_id"].astype(str).str.strip().eq("").any():
        raise RuntimeError("monthly resolution registry has blank resolution ids")
    if normalized["resolution_id"].duplicated().any():
        raise RuntimeError("monthly resolution registry repeats a resolution id")
    if normalized.duplicated(["stock_id", "revenue_period"]).any():
        raise RuntimeError("monthly resolution registry repeats a stock-period")
    identity_columns = [
        column
        for prefix in ("earlier", "later")
        for column in (
            f"{prefix}_market",
            f"{prefix}_source_market_name",
            f"{prefix}_source_table_date",
            f"{prefix}_source_kind",
            f"{prefix}_source_url",
            f"{prefix}_source_file",
        )
    ]
    if normalized[identity_columns].eq("").any(axis=None):
        raise RuntimeError("monthly resolution registry has blank source identities")
    for column in (
        "earlier_raw_row_canonical_sha256",
        "later_raw_row_canonical_sha256",
        "canonical_row_canonical_sha256",
    ):
        if not normalized[column].map(
            lambda value: bool(SHA256_PATTERN.fullmatch(value))
        ).all():
            raise RuntimeError(f"monthly resolution registry has invalid {column}")
    if not normalized["model_id"].eq(MODEL_ID).all():
        raise RuntimeError("monthly resolution registry has a foreign model owner")
    if not normalized["resolution_status"].eq(
        "registered_equal_payload_cross_market_mirror"
    ).all():
        raise RuntimeError("monthly resolution registry has an invalid status")
    if not normalized["canonicalization_policy"].eq(
        "earliest_official_source_table_date"
    ).all():
        raise RuntimeError("monthly resolution registry has an invalid policy")
    if normalized["formal_model_use_allowed"].astype(str).str.lower().ne(
        "false"
    ).any():
        raise RuntimeError("monthly resolutions must remain research-only")
    if not normalized["evidence_url"].astype(str).str.startswith("https://").all():
        raise RuntimeError("monthly resolution evidence must use HTTPS")
    for row in normalized.itertuples(index=False):
        key = f"{row.stock_id}/{row.revenue_period}"
        if row.earlier_market == row.later_market:
            raise RuntimeError(f"monthly resolution repeats a market: {key}")
        if row.earlier_source_market_name == row.later_source_market_name:
            raise RuntimeError(f"monthly resolution repeats a source market: {key}")
        if not row.earlier_source_url.startswith(
            "https://"
        ) or not row.later_source_url.startswith("https://"):
            raise RuntimeError(f"monthly resolution source URLs must use HTTPS: {key}")
        if not row.earlier_source_file.startswith(
            "data/monthly_revenue_history/raw/"
        ) or not row.later_source_file.startswith(
            "data/monthly_revenue_history/raw/"
        ):
            raise RuntimeError(
                "monthly resolution source files must use canonical raw paths: "
                f"{key}"
            )
        if not (
            row.earlier_source_table_date
            < row.official_market_transition_date
            <= row.later_source_table_date
        ):
            raise RuntimeError(f"monthly resolution has invalid chronology: {key}")
        if row.canonical_source_table_date != min(
            row.earlier_source_table_date,
            row.later_source_table_date,
        ):
            raise RuntimeError(
                f"monthly resolution does not select earliest source date: {key}"
            )
        canonical_hash = (
            row.earlier_raw_row_canonical_sha256
            if row.canonical_source_table_date == row.earlier_source_table_date
            else row.later_raw_row_canonical_sha256
        )
        if row.canonical_row_canonical_sha256 != canonical_hash:
            raise RuntimeError(
                f"monthly resolution canonical hash does not bind selected side: {key}"
            )
    return normalized


def _monthly_registry_sha256(registry: pd.DataFrame) -> str:
    normalized = _normalize_monthly_registry(registry).loc[
        :, list(MONTHLY_REGISTRY_CANONICAL_COLUMNS)
    ].copy()
    for column in normalized.columns:
        normalized[column] = normalized[column].map(_payload_value)
    normalized["formal_model_use_allowed"] = normalized[
        "formal_model_use_allowed"
    ].str.lower()
    normalized = normalized.sort_values(
        list(MONTHLY_REGISTRY_SORT_KEYS), kind="mergesort"
    ).reset_index(drop=True)
    return _canonical_json_sha256(
        [
            MONTHLY_CANONICAL_JSON_VERSION,
            list(MONTHLY_REGISTRY_CANONICAL_COLUMNS),
            normalized.values.tolist(),
        ]
    )


def _canonical_monthly_table_sha256(frame: pd.DataFrame) -> str:
    missing = sorted(set(MONTHLY_BINDING_COLUMNS) - set(frame.columns))
    if missing:
        raise RuntimeError(f"canonical monthly table is missing columns: {missing}")
    canonical = frame.loc[:, list(MONTHLY_BINDING_COLUMNS)].copy()
    for column in canonical.columns:
        canonical[column] = canonical[column].map(_payload_value)
    canonical["stock_id"] = canonical["stock_id"].map(_stock_id)
    canonical["revenue_period"] = canonical["revenue_period"].map(
        lambda value: _digits(value, 6, label="monthly binding revenue_period")
    )
    canonical["canonical_source_table_date"] = canonical[
        "canonical_source_table_date"
    ].map(lambda value: _digits(value, 8, label="canonical source date"))
    canonical["source_row_canonical_sha256"] = canonical[
        "source_row_canonical_sha256"
    ].str.lower()
    if canonical.duplicated(["stock_id", "revenue_period"]).any():
        raise RuntimeError("canonical monthly table repeats a stock-period")
    canonical = canonical.sort_values(
        ["stock_id", "revenue_period"], kind="mergesort"
    ).reset_index(drop=True)
    return _canonical_json_sha256(
        [
            MONTHLY_CANONICAL_JSON_VERSION,
            list(MONTHLY_BINDING_COLUMNS),
            canonical.values.tolist(),
        ]
    )


def _normalize_raw_monthly(frame: pd.DataFrame, cutoff: str | None) -> pd.DataFrame:
    missing = sorted(set(RAW_ROW_CANONICAL_COLUMNS) - set(frame.columns))
    if missing:
        raise RuntimeError(f"monthly revenue history is missing columns: {missing}")
    output = frame.copy()
    output["stock_id"] = output["stock_id"].map(_stock_id)
    output["revenue_period"] = output["revenue_period"].map(
        lambda value: _digits(value, 6, label="monthly revenue_period")
    )
    output["source_table_date"] = output["source_table_date"].map(
        lambda value: _digits(value, 8, label="monthly source_table_date")
    )
    if cutoff is not None:
        output = output.loc[output["source_table_date"].le(cutoff)].copy()
    output["market"] = output["market"].str.strip().str.lower()
    output["source_market_name"] = output["source_market_name"].str.strip().str.upper()
    for column in ("source_kind", "source_url", "source_file"):
        output[column] = output[column].str.strip()
    identity_columns = [
        "stock_id",
        "revenue_period",
        *SOURCE_IDENTITY_COLUMNS,
    ]
    if output[identity_columns].eq("").any(axis=None):
        raise RuntimeError("monthly revenue history has blank source identities")
    output["source_row_canonical_sha256"] = output.apply(_raw_row_sha256, axis=1)
    output["cross_market_resolution_id"] = ""
    output["canonical_source_table_date"] = output["source_table_date"]
    return output


def _resolve_monthly(
    raw: pd.DataFrame,
    registry: pd.DataFrame,
    cutoff: str | None,
) -> pd.DataFrame:
    normalized_registry = _normalize_monthly_registry(registry)
    if cutoff is not None:
        normalized_registry = normalized_registry.loc[
            normalized_registry["earlier_source_table_date"].le(cutoff)
            & normalized_registry["later_source_table_date"].le(cutoff)
        ].copy()
    registrations = {
        (str(row.stock_id), str(row.revenue_period)): row
        for row in normalized_registry.itertuples(index=False)
    }
    resolved = _normalize_raw_monthly(raw, cutoff)
    duplicates = resolved.loc[
        resolved.duplicated(["stock_id", "revenue_period"], keep=False),
        ["stock_id", "revenue_period"],
    ].drop_duplicates()
    duplicate_keys = {tuple(row) for row in duplicates.itertuples(index=False, name=None)}
    unregistered = sorted(duplicate_keys - set(registrations))
    if unregistered:
        raise RuntimeError(f"unregistered monthly duplicate: {unregistered[0]}")
    drop_indices: list[object] = []
    for key, registration in registrations.items():
        group = resolved.loc[
            resolved["stock_id"].eq(key[0]) & resolved["revenue_period"].eq(key[1])
        ]
        if len(group) != 2:
            raise RuntimeError(f"registered monthly mirror pair is incomplete: {key}")
        expected_identities = {
            tuple(str(getattr(registration, f"earlier_{column}")) for column in SOURCE_IDENTITY_COLUMNS),
            tuple(str(getattr(registration, f"later_{column}")) for column in SOURCE_IDENTITY_COLUMNS),
        }
        actual_identities = {
            tuple(str(getattr(row, column)) for column in SOURCE_IDENTITY_COLUMNS)
            for row in group.itertuples(index=False)
        }
        if actual_identities != expected_identities:
            raise RuntimeError(f"registered monthly identities mismatch: {key}")
        conflicts = [
            column
            for column in BUSINESS_PAYLOAD_COLUMNS
            if group[column].map(_payload_value).nunique(dropna=False) != 1
        ]
        if conflicts:
            raise RuntimeError(f"registered monthly payload conflict: {key}/{conflicts}")
        canonical = group.loc[
            group["source_row_canonical_sha256"].eq(
                str(registration.canonical_row_canonical_sha256)
            )
        ]
        if len(canonical) != 1:
            raise RuntimeError(f"registered monthly canonical row mismatch: {key}")
        actual_hashes = set(group["source_row_canonical_sha256"].astype(str))
        expected_hashes = {
            str(registration.earlier_raw_row_canonical_sha256),
            str(registration.later_raw_row_canonical_sha256),
        }
        if actual_hashes != expected_hashes:
            raise RuntimeError(f"registered monthly raw hashes mismatch: {key}")
        if str(canonical.iloc[0]["source_table_date"]) != str(
            registration.canonical_source_table_date
        ):
            raise RuntimeError(f"registered monthly canonical date mismatch: {key}")
        resolved.loc[canonical.index, "cross_market_resolution_id"] = str(
            registration.resolution_id
        )
        resolved.loc[canonical.index, "canonical_source_table_date"] = str(
            registration.canonical_source_table_date
        )
        drop_indices.extend(index for index in group.index if index != canonical.index[0])
    output = resolved.drop(index=drop_indices).reset_index(drop=True)
    if output.duplicated(["stock_id", "revenue_period"]).any():
        raise RuntimeError("monthly resolution left duplicate stock-period rows")
    return output


def _resolution_subset_sha256(frame: pd.DataFrame) -> str:
    return _canonical_frame_sha256(
        frame,
        columns=[column for column in frame.columns if column != "notes"],
    )


def _applied_monthly_lineage(
    cutoff_revenue: pd.DataFrame,
    registry: pd.DataFrame,
) -> tuple[list[str], str]:
    ids = sorted(
        {
            _payload_value(value)
            for value in cutoff_revenue["cross_market_resolution_id"]
            if _payload_value(value) not in {"", NO_RESOLUTION_ID}
        }
    )
    normalized = _normalize_monthly_registry(registry)
    applied = normalized.loc[normalized["resolution_id"].isin(ids)].copy()
    if sorted(applied["resolution_id"].tolist()) != ids:
        raise RuntimeError("applied monthly resolution ids are incomplete")
    return ids, _resolution_subset_sha256(applied)


def _price_paths_by_stock(price_dir: Path) -> dict[str, Path]:
    paths: dict[str, Path] = {}
    for path in sorted(Path(price_dir).glob("*.csv")):
        stock_id = _stock_id(path.stem)
        if not stock_id:
            continue
        if stock_id in paths:
            raise RuntimeError(
                "price history directory repeats a normalized stock id: "
                f"{stock_id}/{paths[stock_id].name}/{path.name}"
            )
        paths[stock_id] = path
    return paths


def _cutoff_price_input_stock_ids(
    cutoff_monthly: pd.DataFrame,
    price_dir: Path,
) -> list[str]:
    if "stock_id" not in cutoff_monthly.columns:
        raise RuntimeError("cutoff canonical monthly revenue is missing stock_id")
    revenue_stock_ids = {
        _stock_id(value)
        for value in cutoff_monthly["stock_id"]
        if _stock_id(value)
    }
    return sorted(revenue_stock_ids & set(_price_paths_by_stock(price_dir)))


def _price_file(path: Path, stock_id: str, cutoff: str) -> pd.DataFrame:
    frame = pd.read_csv(path, dtype=str, keep_default_na=False, low_memory=False)
    missing = sorted(set(PRICE_INPUT_COLUMNS) - set(frame.columns))
    if missing:
        raise RuntimeError(f"price history {stock_id} is missing columns: {missing}")
    frame = frame.loc[:, list(PRICE_INPUT_COLUMNS)].copy()
    frame["date"] = frame["date"].map(
        lambda value: _digits(value, 8, label=f"price date for {stock_id}")
    )
    frame = frame.loc[frame["date"].le(cutoff)].copy()
    duplicate_dates = sorted(
        frame.loc[frame["date"].duplicated(keep=False), "date"].unique().tolist()
    )
    if duplicate_dates:
        raise RuntimeError(
            f"price history {stock_id} repeats trading dates within cutoff: "
            f"{duplicate_dates[:3]}"
        )
    return frame.sort_values("date", kind="mergesort").reset_index(drop=True)


def _price_input_lineage(
    cutoff_monthly: pd.DataFrame,
    price_dir: Path,
    cutoff: str,
) -> dict[str, object]:
    price_paths = _price_paths_by_stock(price_dir)
    descriptors: list[list[object]] = []
    total_rows = 0
    for stock_id in _cutoff_price_input_stock_ids(cutoff_monthly, price_dir):
        frame = _price_file(price_paths[stock_id], stock_id, cutoff)
        semantic_sha = _canonical_frame_sha256(frame, columns=list(PRICE_INPUT_COLUMNS))
        descriptors.append([stock_id, len(frame), semantic_sha])
        total_rows += len(frame)
    return {
        "stock_count": len(descriptors),
        "row_count": total_rows,
        "file_semantic_sha256s": "|".join(
            f"{stock_id}:{row_count}:{semantic_sha}"
            for stock_id, row_count, semantic_sha in descriptors
        ),
        "semantic_sha256": _canonical_json_sha256(
            [CANONICAL_JSON_VERSION, "cutoff_price_input_set", descriptors]
        ),
    }


def _applied_price_lineage(
    price_input_stock_ids: list[str],
    registry: pd.DataFrame,
    cutoff: str,
) -> tuple[list[str], str]:
    missing = sorted(set(PRICE_RESOLUTION_REQUIRED_COLUMNS) - set(registry.columns))
    if missing:
        raise RuntimeError(f"price resolution registry is missing columns: {missing}")
    normalized = registry.copy()
    normalized["stock_id"] = normalized["stock_id"].map(_stock_id)
    normalized["resume_date"] = normalized["resume_date"].map(
        lambda value: _digits(value, 8, label="price resolution resume_date")
    )
    eligible = normalized.loc[
        normalized["stock_id"].isin(set(price_input_stock_ids))
        & normalized["resume_date"].le(cutoff)
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


def _bool_value(value: object) -> bool:
    return _payload_value(value).lower() in {"true", "1", "yes"}


def _bool_series(series: pd.Series) -> pd.Series:
    return series.map(_bool_value)


def _number(value: object) -> float | None:
    number = pd.to_numeric(value, errors="coerce")
    return None if pd.isna(number) else float(number)


def _stable(value: object, digits: int = 4) -> float | str:
    number = _number(value)
    return "" if number is None else round(number, digits)


def _period_ordinal(series: pd.Series) -> pd.Series:
    text = series.astype(str).str.replace(r"\D", "", regex=True).str[:6]
    year = pd.to_numeric(text.str[:4], errors="coerce")
    month = pd.to_numeric(text.str[4:6], errors="coerce")
    return year * 12 + month


def _prepare_replay_revenue(cutoff_monthly: pd.DataFrame) -> pd.DataFrame:
    required = {
        "stock_id",
        "stock_name",
        "revenue_period",
        "source_table_date",
        "source_row_canonical_sha256",
        "cross_market_resolution_id",
        "canonical_source_table_date",
        "latest_revenue_yoy_pct",
        "cumulative_revenue_yoy_pct",
        "month_over_month_pct",
        "revenue_numerical_anomaly_flag",
        "research_join_allowed",
    }
    missing = sorted(required - set(cutoff_monthly.columns))
    if missing:
        raise RuntimeError(f"cutoff replay monthly revenue is missing columns: {missing}")
    frame = cutoff_monthly.copy()
    frame["stock_id"] = frame["stock_id"].map(_stock_id)
    frame["revenue_period"] = frame["revenue_period"].map(
        lambda value: _digits(value, 6, label="replay revenue_period")
    )
    for column in ("source_table_date", "canonical_source_table_date"):
        frame[column] = frame[column].map(
            lambda value: _digits(value, 8, label=f"replay {column}")
        )
        if frame[column].gt(CUTOFF_DATE).any():
            raise RuntimeError(f"cutoff replay monthly revenue exceeds cutoff: {column}")
    frame["source_row_canonical_sha256"] = (
        frame["source_row_canonical_sha256"].astype(str).str.strip().str.lower()
    )
    if not frame["source_row_canonical_sha256"].str.fullmatch(r"[0-9a-f]{64}").all():
        raise RuntimeError("cutoff replay monthly revenue has invalid row SHA-256")
    if frame["canonical_source_table_date"].ne(frame["source_table_date"]).any():
        raise RuntimeError("cutoff replay canonical source date differs from selected row")
    for column in (
        "latest_revenue_yoy_pct",
        "cumulative_revenue_yoy_pct",
        "month_over_month_pct",
    ):
        frame[column] = pd.to_numeric(frame[column], errors="coerce")
    frame = frame.sort_values(
        ["stock_id", "source_table_date", "revenue_period"],
        kind="mergesort",
    )
    if frame.duplicated(["stock_id", "revenue_period"]).any():
        raise RuntimeError("cutoff replay monthly revenue repeats a stock-period")
    grouped = frame.groupby("stock_id", sort=False, dropna=False)
    frame["previous_latest_revenue_yoy_pct"] = grouped[
        "latest_revenue_yoy_pct"
    ].shift(1)
    frame["previous_cumulative_revenue_yoy_pct"] = grouped[
        "cumulative_revenue_yoy_pct"
    ].shift(1)
    frame["previous_revenue_period"] = grouped["revenue_period"].shift(1)
    frame["latest_yoy_delta_pct_points"] = (
        frame["latest_revenue_yoy_pct"]
        - frame["previous_latest_revenue_yoy_pct"]
    )
    frame["cumulative_yoy_delta_pct_points"] = (
        frame["cumulative_revenue_yoy_pct"]
        - frame["previous_cumulative_revenue_yoy_pct"]
    )
    frame["consecutive_calendar_month_flag"] = (
        _period_ordinal(frame["revenue_period"])
        - _period_ordinal(frame["previous_revenue_period"])
    ).eq(1)
    frame["absolute_strong_flag"] = (
        frame["latest_revenue_yoy_pct"].ge(30.0)
        | frame["cumulative_revenue_yoy_pct"].ge(20.0)
    )
    frame["research_join_allowed_flag"] = _bool_series(
        frame["research_join_allowed"]
    )
    frame["source_revenue_anomaly_candidate_flag"] = _bool_series(
        frame["revenue_numerical_anomaly_flag"]
    )
    return frame.reset_index(drop=True)


def _replay_condition_masks(revenue: pd.DataFrame) -> dict[str, pd.Series]:
    latest = revenue["latest_revenue_yoy_pct"]
    previous = revenue["previous_latest_revenue_yoy_pct"]
    absolute = revenue["absolute_strong_flag"]
    consecutive = revenue["consecutive_calendar_month_flag"]

    def two_month(threshold: float) -> pd.Series:
        return consecutive & latest.ge(threshold) & previous.ge(threshold)

    turn_positive = (
        latest.gt(0.0)
        & previous.le(0.0)
        & revenue["latest_yoy_delta_pct_points"].ge(20.0)
    )
    positive_acceleration = (
        latest.gt(0.0)
        & revenue["latest_yoy_delta_pct_points"].ge(20.0)
    )
    masks = {
        BASELINE_VARIANT_ID: absolute,
        "absolute_or_latest_yoy_ge15": absolute | latest.ge(15.0),
        "absolute_or_two_month_yoy_ge10": absolute | two_month(10.0),
        "absolute_or_two_month_yoy_ge12_5": absolute | two_month(12.5),
        PRIMARY_VARIANT_ID: absolute | two_month(15.0),
        "absolute_or_two_month_yoy_ge17_5": absolute | two_month(17.5),
        "absolute_or_two_month_yoy_ge18": absolute | two_month(18.0),
        "absolute_or_two_month_yoy_ge20": absolute | two_month(20.0),
        "absolute_or_two_month_yoy_ge25": absolute | two_month(25.0),
        "absolute_or_two_month_yoy_ge15_cumulative_improving": (
            absolute
            | (
                two_month(15.0)
                & revenue["cumulative_yoy_delta_pct_points"].gt(0.0)
            )
        ),
        "absolute_or_turn_positive_accel20": absolute | turn_positive,
        "absolute_or_positive_accel20": absolute | positive_acceleration,
        INCREMENTAL_VARIANT_ID: two_month(15.0) & ~absolute,
    }
    return {key: value.fillna(False) for key, value in masks.items()}


def _replay_price_resolutions(registry: pd.DataFrame) -> pd.DataFrame:
    missing = sorted(set(PRICE_RESOLUTION_REQUIRED_COLUMNS) - set(registry.columns))
    if missing:
        raise RuntimeError(f"price resolution registry is missing columns: {missing}")
    frame = registry.copy()
    frame["stock_id"] = frame["stock_id"].map(_stock_id)
    frame["resume_date"] = frame["resume_date"].map(
        lambda value: _digits(value, 8, label="price resolution resume_date")
    )
    frame["exchange_ratio"] = pd.to_numeric(frame["exchange_ratio"], errors="coerce")
    frame = frame.loc[
        frame["model_id"].eq(MODEL_ID)
        & frame["root_cause_status"].eq(
            "verified_non_comparable_raw_price_scale"
        )
        & frame["resume_date"].le(CUTOFF_DATE)
    ].copy()
    if frame["exchange_ratio"].isna().any() or frame["exchange_ratio"].eq(0).any():
        raise RuntimeError("cutoff price resolution has invalid exchange_ratio")
    return frame


def _replay_stock_price(
    path: Path,
    stock_id: str,
    resolutions: pd.DataFrame,
) -> pd.DataFrame:
    frame = _price_file(path, stock_id, CUTOFF_DATE)
    for column in ("open", "high", "low", "close", "volume", "volume_ratio"):
        frame[column] = pd.to_numeric(frame[column], errors="coerce")
    frame = frame.dropna(subset=["close"]).reset_index(drop=True)
    frame["raw_close"] = frame["close"]
    frame["analysis_price_adjustment_factor"] = 1.0
    frame["price_resolution_ids_on_date"] = ""
    stock_resolutions = resolutions.loc[resolutions["stock_id"].eq(stock_id)]
    for event in stock_resolutions.itertuples(index=False):
        ratio = float(event.exchange_ratio)
        frame.loc[
            frame["date"].lt(str(event.resume_date)),
            "analysis_price_adjustment_factor",
        ] *= 1.0 / ratio
        frame.loc[
            frame["date"].eq(str(event.resume_date)),
            "price_resolution_ids_on_date",
        ] = str(event.resolution_id)
    frame["analysis_close"] = (
        frame["raw_close"] * frame["analysis_price_adjustment_factor"]
    )
    close = frame["analysis_close"]
    frame["analysis_return_1d_pct"] = close.pct_change() * 100.0
    frame["analysis_return_5d_pct"] = close.pct_change(5) * 100.0
    frame["analysis_return_20d_pct"] = close.pct_change(20) * 100.0
    frame["previous_20d_highest_close"] = (
        close.shift(1).rolling(20, min_periods=20).max()
    )
    frame["previous_23d_highest_close"] = (
        close.shift(1).rolling(23, min_periods=20).max()
    )
    frame["previous_23d_lowest_close"] = (
        close.shift(1).rolling(23, min_periods=20).min()
    )
    frame["range_width_23d_pct"] = (
        frame["previous_23d_highest_close"]
        / frame["previous_23d_lowest_close"]
        - 1.0
    ) * 100.0
    frame["close_breakout_prev20"] = close.gt(
        frame["previous_20d_highest_close"]
    )
    frame["range_breakout_prev20_pct"] = (
        close / frame["previous_20d_highest_close"] - 1.0
    ) * 100.0
    frame["close_location_pct"] = np.where(
        frame["high"].gt(frame["low"]),
        (frame["close"] - frame["low"])
        / (frame["high"] - frame["low"])
        * 100.0,
        100.0,
    )
    frame["locked_limit_up_like"] = (
        frame["analysis_return_1d_pct"].ge(9.0)
        & frame["close"].ge(frame["high"] - 1e-9)
    )
    volume_ma20 = frame["volume"].shift(1).rolling(20, min_periods=20).mean()
    normal_attack = (
        frame["volume_ratio"].ge(2.0)
        & frame["range_breakout_prev20_pct"].ge(2.0)
        & volume_ma20.ge(1_000_000.0)
        & frame["close"].gt(frame["open"])
    )
    frame["active_attack_flag"] = (
        normal_attack
        | frame["locked_limit_up_like"]
        | frame["volume_ratio"].ge(2.5)
        | frame["analysis_return_5d_pct"].ge(8.0)
        | frame["analysis_return_20d_pct"].ge(20.0)
    )
    frame["price_unreacted_flag"] = (
        frame["analysis_close"].ge(frame["previous_23d_lowest_close"] * 0.95)
        & frame["analysis_close"].le(
            frame["previous_23d_highest_close"] * 1.05
        )
        & ~frame["active_attack_flag"]
    ).fillna(False)
    frame["raw_price_jump_threshold_candidate_flag"] = (
        frame["raw_close"].pct_change().abs().ge(0.80)
    )
    frame["analysis_price_jump_threshold_candidate_flag"] = (
        frame["analysis_close"].pct_change().abs().ge(0.80)
    )
    return frame.reset_index(drop=True)


def _replay_strict_launch_metrics(price: pd.DataFrame, index: int) -> dict[str, object]:
    if index + OUTCOME_WINDOW_DAYS >= len(price):
        return {
            "mature": False,
            "strict_success": False,
            "first_hit_offset": "",
            "d20_return_pct": "",
            "post_hit_min_return_pct": "",
        }
    base = float(price.at[index, "analysis_close"])
    closes = pd.to_numeric(
        price.loc[index : index + OUTCOME_WINDOW_DAYS, "analysis_close"],
        errors="coerce",
    )
    first_window = closes.iloc[: FIRST_HIT_DEADLINE_DAYS + 1]
    hits = np.flatnonzero(first_window.to_numpy(dtype=float) >= base * 1.20)
    first_hit = int(hits[0]) if len(hits) else None
    post_min: float | str = ""
    strict = False
    if first_hit is not None:
        post_min = float(closes.iloc[first_hit:].min() / base - 1.0) * 100.0
        strict = post_min >= 20.0 - 1e-9
    return {
        "mature": True,
        "strict_success": strict,
        "first_hit_offset": first_hit if first_hit is not None else "",
        "d20_return_pct": float(closes.iloc[-1] / base - 1.0) * 100.0,
        "post_hit_min_return_pct": post_min,
    }


def _replay_source_events(
    revenue: pd.DataFrame,
    mask: pd.Series,
    price: pd.DataFrame,
) -> list[tuple[int, pd.Series]]:
    dates = price["date"].to_numpy(dtype=str)
    events: list[tuple[int, pd.Series]] = []
    for _, row in revenue.loc[
        mask & revenue["research_join_allowed_flag"]
    ].iterrows():
        source_date = str(row["source_table_date"])
        price_index = int(np.searchsorted(dates, source_date, side="left"))
        if source_date < str(dates[0]) or price_index >= len(price):
            continue
        if bool(price.at[price_index, "price_unreacted_flag"]):
            events.append((price_index, row))
    return sorted(events, key=lambda item: (item[0], str(item[1]["revenue_period"])))


def _resolution_id(value: object) -> str:
    text = _payload_value(value)
    return text if text else NO_RESOLUTION_ID


def _replay_episode_rows(
    *,
    generated_at: str,
    stock_id: str,
    stock_name: str,
    variant_id: str,
    events: list[tuple[int, pd.Series]],
    price: pd.DataFrame,
    monthly_lineage: dict[str, str],
) -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    position = 0
    episode_number = 0
    while position < len(events):
        start_index, start_event = events[position]
        latest_index = start_index
        used = [events[position]]
        position += 1
        natural_expiry = latest_index + DISCOVERY_HORIZON_DAYS
        day = start_index
        first_breakout_index: int | None = None
        launch_index: int | None = None
        while day <= min(natural_expiry, len(price) - 1):
            while position < len(events) and events[position][0] <= day:
                latest_index = events[position][0]
                used.append(events[position])
                position += 1
                natural_expiry = latest_index + DISCOVERY_HORIZON_DAYS
            if bool(price.at[day, "close_breakout_prev20"]):
                if first_breakout_index is None:
                    first_breakout_index = day
                metrics = _replay_strict_launch_metrics(price, day)
                if bool(metrics["strict_success"]):
                    launch_index = day
                    break
            day += 1
        if launch_index is not None:
            episode_status = "launch_within_active_horizon"
            episode_end_index = launch_index
        elif natural_expiry < len(price):
            episode_status = "no_launch_within_active_horizon"
            episode_end_index = natural_expiry
        else:
            episode_status = "right_censored_before_active_horizon"
            episode_end_index = len(price) - 1
        first_metrics = (
            _replay_strict_launch_metrics(price, first_breakout_index)
            if first_breakout_index is not None
            else None
        )
        if first_metrics is None:
            first_outcome = "no_breakout_observed"
        elif not bool(first_metrics["mature"]):
            first_outcome = "right_censored_before_d20"
        elif bool(first_metrics["strict_success"]):
            first_outcome = "strict_success"
        else:
            first_outcome = "mature_failure"
        launch_metrics = (
            _replay_strict_launch_metrics(price, launch_index)
            if launch_index is not None
            else None
        )
        observation = price.loc[start_index:episode_end_index]
        raw_candidate = bool(
            observation["raw_price_jump_threshold_candidate_flag"]
            .fillna(False)
            .any()
        )
        adjusted_candidate = bool(
            observation["analysis_price_jump_threshold_candidate_flag"]
            .fillna(False)
            .any()
        )
        resolution_ids = sorted(
            {
                value
                for value in observation["price_resolution_ids_on_date"].astype(str)
                if value
            }
        )
        latest_event = used[-1][1]
        episode_number += 1
        rows.append(
            {
                "generated_at": generated_at,
                "model_id": MODEL_ID,
                "artifact_id": SOURCE_FIRST_ARTIFACT_ID,
                "artifact_version": SOURCE_FIRST_ARTIFACT_VERSION,
                **monthly_lineage,
                "condition_variant_id": variant_id,
                "episode_key": (
                    f"{variant_id}|{stock_id}|"
                    f"{start_event['source_table_date']}|{episode_number}"
                ),
                "stock_id": stock_id,
                "stock_name": stock_name,
                "episode_number": episode_number,
                "episode_start_revenue_period": str(start_event["revenue_period"]),
                "episode_start_source_date": str(start_event["source_table_date"]),
                "episode_start_cross_market_resolution_id": _resolution_id(
                    start_event["cross_market_resolution_id"]
                ),
                "episode_start_source_row_canonical_sha256": str(
                    start_event["source_row_canonical_sha256"]
                ),
                "episode_start_canonical_source_table_date": str(
                    start_event["canonical_source_table_date"]
                ),
                "episode_start_trade_date": str(price.at[start_index, "date"]),
                "episode_start_sequence_index": start_index,
                "latest_qualifying_revenue_period": str(
                    latest_event["revenue_period"]
                ),
                "latest_qualifying_source_date": str(
                    latest_event["source_table_date"]
                ),
                "latest_qualifying_cross_market_resolution_id": _resolution_id(
                    latest_event["cross_market_resolution_id"]
                ),
                "latest_qualifying_source_row_canonical_sha256": str(
                    latest_event["source_row_canonical_sha256"]
                ),
                "latest_qualifying_canonical_source_table_date": str(
                    latest_event["canonical_source_table_date"]
                ),
                "latest_qualifying_trade_date": str(price.at[latest_index, "date"]),
                "latest_qualifying_sequence_index": latest_index,
                "qualifying_update_count": len(used),
                "qualifying_revenue_periods": "|".join(
                    str(event[1]["revenue_period"]) for event in used
                ),
                "qualifying_source_dates": "|".join(
                    str(event[1]["source_table_date"]) for event in used
                ),
                "qualifying_cross_market_resolution_ids": "|".join(
                    _resolution_id(event[1]["cross_market_resolution_id"])
                    for event in used
                ),
                "qualifying_source_row_canonical_sha256s": "|".join(
                    str(event[1]["source_row_canonical_sha256"])
                    for event in used
                ),
                "qualifying_canonical_source_table_dates": "|".join(
                    str(event[1]["canonical_source_table_date"])
                    for event in used
                ),
                "qualifying_trade_dates": "|".join(
                    str(price.at[event[0], "date"]) for event in used
                ),
                "qualifying_sequence_indices": "|".join(
                    str(event[0]) for event in used
                ),
                "episode_end_sequence_index": episode_end_index,
                "episode_end_date": str(price.at[episode_end_index, "date"]),
                "episode_status": episode_status,
                "start_latest_revenue_yoy_pct": _stable(
                    start_event["latest_revenue_yoy_pct"]
                ),
                "start_cumulative_revenue_yoy_pct": _stable(
                    start_event["cumulative_revenue_yoy_pct"]
                ),
                "start_previous_latest_revenue_yoy_pct": _stable(
                    start_event["previous_latest_revenue_yoy_pct"]
                ),
                "start_latest_yoy_delta_pct_points": _stable(
                    start_event["latest_yoy_delta_pct_points"]
                ),
                "start_month_over_month_pct": _stable(
                    start_event["month_over_month_pct"]
                ),
                "start_source_revenue_anomaly_candidate_flag": bool(
                    start_event["source_revenue_anomaly_candidate_flag"]
                ),
                "qualifying_source_revenue_anomaly_candidate_flag": any(
                    bool(event[1]["source_revenue_anomaly_candidate_flag"])
                    for event in used
                ),
                "source_price_unreacted_flag": True,
                "source_close": _stable(price.at[start_index, "analysis_close"]),
                "source_return_5d_pct": _stable(
                    price.at[start_index, "analysis_return_5d_pct"]
                ),
                "source_return_20d_pct": _stable(
                    price.at[start_index, "analysis_return_20d_pct"]
                ),
                "source_volume_ratio": _stable(
                    price.at[start_index, "volume_ratio"]
                ),
                "source_range_width_23d_pct": _stable(
                    price.at[start_index, "range_width_23d_pct"]
                ),
                "first_breakout_date": (
                    str(price.at[first_breakout_index, "date"])
                    if first_breakout_index is not None
                    else ""
                ),
                "first_breakout_lag_from_episode_start_days": (
                    first_breakout_index - start_index
                    if first_breakout_index is not None
                    else ""
                ),
                "first_breakout_outcome": first_outcome,
                "first_breakout_d20_return_pct": (
                    _stable(first_metrics["d20_return_pct"])
                    if first_metrics is not None
                    else ""
                ),
                "launch_date": (
                    str(price.at[launch_index, "date"])
                    if launch_index is not None
                    else ""
                ),
                "launch_lag_from_episode_start_days": (
                    launch_index - start_index if launch_index is not None else ""
                ),
                "launch_lag_from_latest_source_days": (
                    launch_index - latest_index if launch_index is not None else ""
                ),
                "first_hit_20_day_offset": (
                    launch_metrics["first_hit_offset"]
                    if launch_metrics is not None
                    else ""
                ),
                "launch_d20_return_pct": (
                    _stable(launch_metrics["d20_return_pct"])
                    if launch_metrics is not None
                    else ""
                ),
                "launch_post_hit_min_return_pct": (
                    _stable(launch_metrics["post_hit_min_return_pct"])
                    if launch_metrics is not None
                    else ""
                ),
                "price_path_threshold_candidate_flag": raw_candidate,
                "price_path_resolution_ids": ";".join(resolution_ids),
                "unresolved_price_path_candidate_flag": adjusted_candidate,
                "same_stock_non_overlap_applied": True,
                "right_censored_flag": episode_status.startswith("right_censored"),
                "retrospective_label_status": (
                    "research_only_future_outcome_label_not_tradable_confirmation"
                ),
                "financial_statement_scope": FINANCIAL_STATEMENT_SCOPE,
                "approved_for_daily": False,
                "production_change": False,
            }
        )
    return rows


def _rebuild_cutoff_source_detail(
    cutoff_monthly: pd.DataFrame,
    *,
    price_dir: Path,
    price_registry: pd.DataFrame,
    monthly_blob_sha: str,
    cutoff_monthly_sha: str,
    monthly_registry_sha: str,
) -> pd.DataFrame:
    revenue = _prepare_replay_revenue(cutoff_monthly)
    masks = _replay_condition_masks(revenue)
    resolutions = _replay_price_resolutions(price_registry)
    monthly_lineage = {
        "monthly_revenue_history_blob_sha256": monthly_blob_sha,
        "monthly_revenue_canonical_table_sha256": cutoff_monthly_sha,
        "cross_market_resolution_registry_canonical_sha256": monthly_registry_sha,
    }
    rows: list[dict[str, object]] = []
    for path in sorted(Path(price_dir).glob("*.csv")):
        stock_id = _stock_id(path.stem)
        stock_revenue = revenue.loc[revenue["stock_id"].eq(stock_id)].copy()
        if stock_revenue.empty:
            continue
        price = _replay_stock_price(path, stock_id, resolutions)
        if price.empty:
            continue
        stock_name = str(stock_revenue["stock_name"].iloc[-1])
        for variant_id in CONDITION_VARIANT_IDS:
            local_mask = masks[variant_id].loc[stock_revenue.index]
            events = _replay_source_events(stock_revenue, local_mask, price)
            rows.extend(
                _replay_episode_rows(
                    generated_at="independent_replay",
                    stock_id=stock_id,
                    stock_name=stock_name,
                    variant_id=variant_id,
                    events=events,
                    price=price,
                    monthly_lineage=monthly_lineage,
                )
            )
    return pd.DataFrame(rows, columns=list(SOURCE_DETAIL_COLUMNS))


def _replay_detail_errors(
    projected_detail: pd.DataFrame,
    rebuilt_detail: pd.DataFrame,
) -> list[str]:
    if tuple(projected_detail.columns) != SOURCE_DETAIL_COLUMNS:
        return ["projected detail schema does not match source-first detail contract"]
    errors: list[str] = []
    for frame, label in (
        (projected_detail, "projected detail"),
        (rebuilt_detail, "independent replay"),
    ):
        if frame["episode_key"].map(_payload_value).duplicated().any():
            errors.append(f"{label} repeats episode_key")
    if errors:
        return errors
    actual = projected_detail.copy()
    expected = rebuilt_detail.copy()
    actual.index = actual["episode_key"].map(_payload_value)
    expected.index = expected["episode_key"].map(_payload_value)
    actual_keys = set(actual.index)
    expected_keys = set(expected.index)
    missing = sorted(expected_keys - actual_keys)
    extra = sorted(actual_keys - expected_keys)
    if missing:
        errors.append(
            "projected detail is missing independently rebuilt episode keys: "
            f"{missing[:3]}"
        )
    if extra:
        errors.append(
            "projected detail has extra episode keys absent from independent replay: "
            f"{extra[:3]}"
        )
    comparison_columns = [
        column for column in SOURCE_DETAIL_COLUMNS if column != "generated_at"
    ]
    for episode_key in sorted(actual_keys & expected_keys):
        for column in comparison_columns:
            actual_value = _payload_value(actual.at[episode_key, column])
            expected_value = _payload_value(expected.at[episode_key, column])
            if actual_value != expected_value:
                errors.append(
                    "projected detail differs from independent replay: "
                    f"episode_key={episode_key} column={column} "
                    f"actual={actual_value!r} expected={expected_value!r}"
                )
                return errors
    return errors


def _date_tokens(frame: pd.DataFrame, columns: tuple[str, ...]) -> list[str]:
    tokens: list[str] = []
    for column in columns:
        if column not in frame.columns:
            raise RuntimeError(f"projected detail is missing date column: {column}")
        for value in frame[column]:
            for token in _payload_value(value).split("|"):
                if token.strip():
                    tokens.append(_digits(token.strip(), 8, label=column))
    return tokens


def _max_dates(detail: pd.DataFrame) -> tuple[str, str, str]:
    return (
        max(
            _date_tokens(
                detail,
                (
                    "episode_start_source_date",
                    "latest_qualifying_source_date",
                    "qualifying_source_dates",
                ),
            ),
            default="",
        ),
        max(
            _date_tokens(
                detail,
                (
                    "episode_start_trade_date",
                    "latest_qualifying_trade_date",
                    "qualifying_trade_dates",
                ),
            ),
            default="",
        ),
        max(_date_tokens(detail, ("episode_end_date",)), default=""),
    )


def _constant(frame: pd.DataFrame, column: str, *, label: str) -> str:
    if column not in frame.columns:
        raise RuntimeError(f"{label} is missing column: {column}")
    values = sorted({_payload_value(value) for value in frame[column]})
    if len(values) != 1 or not values[0]:
        raise RuntimeError(f"{label} must have one non-empty {column}: {values}")
    return values[0]


def _binding_errors(manifest: pd.DataFrame, detail: pd.DataFrame) -> list[str]:
    errors: list[str] = []
    actual_columns = list(manifest.columns)
    if actual_columns not in (
        list(V1_MANIFEST_COLUMNS),
        list(V2_MANIFEST_COLUMNS),
    ):
        return ["projection manifest schema mismatch"]
    if len(manifest) != 1:
        return [f"projection manifest must have exactly one row: {len(manifest)}"]
    row = manifest.iloc[0]
    version = _payload_value(row["projection_version"])
    if version == V1_ARTIFACT_VERSION:
        expected_policy = V1_PROJECTION_POLICY_ID
        if actual_columns != list(V1_MANIFEST_COLUMNS):
            errors.append("v1 projection manifest schema mismatch")
    elif version == V2_ARTIFACT_VERSION:
        expected_policy = V2_PROJECTION_POLICY_ID
        if actual_columns != list(V2_MANIFEST_COLUMNS):
            errors.append("v2 projection manifest schema mismatch")
        for column, expected in {
            "predecessor_projection_version": V1_ARTIFACT_VERSION,
            "predecessor_manifest_bytes_sha256": V1_EXPECTED_PREDECESSOR_MANIFEST_SHA256,
            "predecessor_detail_bytes_sha256": V1_EXPECTED_PREDECESSOR_DETAIL_SHA256,
            "lineage_change_reason": V2_LINEAGE_CHANGE_REASON,
            "candidate_status": V2_CANDIDATE_STATUS,
        }.items():
            if _payload_value(row[column]) != expected:
                errors.append(f"projection manifest {column} mismatch")
    else:
        expected_policy = ""
        errors.append(f"unsupported projection version: {version}")
    for column, expected in {
        "model_id": MODEL_ID,
        "artifact_id": ARTIFACT_ID,
        "artifact_version": version,
        "projection_id": PROJECTION_ID,
        "projection_version": version,
        "projection_policy_id": expected_policy,
        "cutoff_date": CUTOFF_DATE,
        "full_source_artifact_id": SOURCE_FIRST_ARTIFACT_ID,
    }.items():
        if _payload_value(row[column]) != expected:
            errors.append(f"projection manifest {column} mismatch")
    try:
        if _constant(detail, "artifact_id", label="projected detail") != _payload_value(
            row["full_source_artifact_id"]
        ):
            errors.append("projected detail artifact_id binding mismatch")
        if _constant(detail, "artifact_version", label="projected detail") != _payload_value(
            row["full_source_artifact_version"]
        ):
            errors.append("projected detail artifact_version binding mismatch")
        if len(detail) != int(row["projected_episode_row_count"]):
            errors.append("projected detail row-count binding mismatch")
        if _projected_source_detail_sha256(detail) != _payload_value(
            row["projected_episode_semantic_sha256"]
        ):
            errors.append("projected detail semantic SHA-256 binding mismatch")
        for column, manifest_column in (
            ("monthly_revenue_history_blob_sha256", "monthly_revenue_history_blob_sha256"),
            (
                "monthly_revenue_canonical_table_sha256",
                "cutoff_revenue_subset_semantic_sha256",
            ),
            (
                "cross_market_resolution_registry_canonical_sha256",
                "cross_market_resolution_registry_canonical_sha256",
            ),
        ):
            if _constant(detail, column, label="projected detail") != _payload_value(
                row[manifest_column]
            ):
                errors.append(f"projected detail {column} lineage mismatch")
        maxima = _max_dates(detail)
        for column, actual in zip(
            (
                "projected_max_source_date",
                "projected_max_trade_date",
                "projected_max_episode_end_date",
            ),
            maxima,
        ):
            if _payload_value(row[column]) != actual:
                errors.append(f"projected detail {column} binding mismatch")
            if actual and actual > CUTOFF_DATE:
                errors.append(f"projected detail {column} exceeds cutoff")
    except (RuntimeError, TypeError, ValueError) as exc:
        errors.append(str(exc))
    if _payload_value(row["research_only"]) != "true":
        errors.append("research_only must be true")
    for column in (
        "formal_model_use_allowed",
        "approved_for_daily",
        "production_change",
        "promotion_evidence_allowed",
        "ranking_consumption_allowed",
        "pdf_consumption_allowed",
    ):
        if _payload_value(row[column]) != "false":
            errors.append(f"{column} must be false")
    return errors


def validate_projection_binding_frames(
    manifest: pd.DataFrame,
    projected_detail: pd.DataFrame,
) -> list[str]:
    """Validate manifest/detail binding without importing the projection producer."""

    return _binding_errors(manifest, projected_detail)


def validate_frames(
    manifest: pd.DataFrame,
    projected_detail: pd.DataFrame,
    *,
    revenue_path: Path,
    price_dir: Path,
    monthly_resolution_path: Path,
    price_resolution_path: Path,
) -> list[str]:
    """Validate the pinned cutoff projection against cutoff-only current inputs.

    The mutable source-first latest artifact can legitimately advance after
    this projection was pinned, so it is deliberately not an input here.  The
    manifest/detail binding above preserves the historical capture hashes; the
    replay below independently verifies every cutoff-scoped input and row.
    """

    errors = _binding_errors(manifest, projected_detail)
    if errors:
        return errors
    try:
        row = manifest.iloc[0]
        raw = pd.read_csv(
            revenue_path,
            dtype=str,
            keep_default_na=False,
            low_memory=False,
        )
        monthly_registry = pd.read_csv(
            monthly_resolution_path,
            dtype=str,
            keep_default_na=False,
        )
        cutoff_monthly = _resolve_monthly(raw, monthly_registry, CUTOFF_DATE)
        price_registry = pd.read_csv(
            price_resolution_path,
            dtype=str,
            keep_default_na=False,
        )
        price_input_stock_ids = _cutoff_price_input_stock_ids(
            cutoff_monthly,
            price_dir,
        )
        price_lineage = _price_input_lineage(
            cutoff_monthly,
            price_dir,
            CUTOFF_DATE,
        )
        monthly_ids, monthly_resolution_sha = _applied_monthly_lineage(
            cutoff_monthly,
            monthly_registry,
        )
        price_ids, price_resolution_sha = _applied_price_lineage(
            price_input_stock_ids,
            price_registry,
            CUTOFF_DATE,
        )
        cutoff_monthly_sha = _canonical_monthly_table_sha256(cutoff_monthly)
        rebuilt_detail = _rebuild_cutoff_source_detail(
            cutoff_monthly,
            price_dir=price_dir,
            price_registry=price_registry,
            monthly_blob_sha=_payload_value(
                row["monthly_revenue_history_blob_sha256"]
            ),
            cutoff_monthly_sha=cutoff_monthly_sha,
            monthly_registry_sha=_payload_value(
                row["cross_market_resolution_registry_canonical_sha256"]
            ),
        )
        errors.extend(_replay_detail_errors(projected_detail, rebuilt_detail))
        max_source, max_trade, max_end = _max_dates(projected_detail)
        expected = {
            "cutoff_revenue_subset_row_count": len(cutoff_monthly),
            "cutoff_revenue_subset_semantic_sha256": cutoff_monthly_sha,
            "cutoff_price_input_stock_count": price_lineage["stock_count"],
            "cutoff_price_input_row_count": price_lineage["row_count"],
            "cutoff_price_input_file_semantic_sha256s": price_lineage[
                "file_semantic_sha256s"
            ],
            "cutoff_price_input_semantic_sha256": price_lineage["semantic_sha256"],
            "applied_monthly_resolution_count": len(monthly_ids),
            "applied_monthly_resolution_ids": "|".join(monthly_ids)
            or NO_RESOLUTION_ID,
            "applied_monthly_resolution_semantic_sha256": monthly_resolution_sha,
            "applied_price_resolution_count": len(price_ids),
            "applied_price_resolution_ids": "|".join(price_ids) or NO_RESOLUTION_ID,
            "applied_price_resolution_semantic_sha256": price_resolution_sha,
            "projected_max_source_date": max_source,
            "projected_max_trade_date": max_trade,
            "projected_max_episode_end_date": max_end,
        }
        for column, value in expected.items():
            if _payload_value(row[column]) != _payload_value(value):
                errors.append(
                    f"projection manifest {column} source recomputation mismatch"
                )
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
    except (OSError, RuntimeError, TypeError, ValueError, KeyError) as exc:
        errors.append(str(exc))
    return errors


def _validate_immutable_v1_files(
    manifest: pd.DataFrame,
    projected_detail: pd.DataFrame,
    *,
    manifest_path: Path,
    projected_detail_path: Path,
) -> list[str]:
    errors = _binding_errors(manifest, projected_detail)
    if errors:
        return errors
    row = manifest.iloc[0]
    expected = (
        (
            "canonical v1 manifest bytes",
            Path(manifest_path).stat().st_size,
            V1_EXPECTED_MANIFEST_BYTES,
        ),
        (
            "canonical v1 manifest bytes SHA-256",
            _file_sha256(Path(manifest_path)),
            V1_EXPECTED_MANIFEST_BYTES_SHA256,
        ),
        (
            "canonical v1 detail bytes",
            Path(projected_detail_path).stat().st_size,
            V1_EXPECTED_DETAIL_BYTES,
        ),
        (
            "canonical v1 detail bytes SHA-256",
            _file_sha256(Path(projected_detail_path)),
            V1_EXPECTED_DETAIL_BYTES_SHA256,
        ),
        (
            "canonical v1 detail row count",
            len(projected_detail),
            V1_EXPECTED_DETAIL_ROW_COUNT,
        ),
        (
            "canonical v1 detail semantic SHA-256",
            _projected_source_detail_sha256(projected_detail),
            V1_EXPECTED_DETAIL_SEMANTIC_SHA256,
        ),
        (
            "canonical v1 manifest detail semantic SHA-256",
            _payload_value(row["projected_episode_semantic_sha256"]),
            V1_EXPECTED_DETAIL_SEMANTIC_SHA256,
        ),
        (
            "canonical v1 cutoff price input semantic SHA-256",
            _payload_value(row["cutoff_price_input_semantic_sha256"]),
            V1_EXPECTED_CUTOFF_PRICE_INPUT_SEMANTIC_SHA256,
        ),
    )
    for label, actual, required in expected:
        if actual != required:
            errors.append(f"{label} mismatch: {actual}/{required}")
    return errors


def _validate_v1_archive_evidence(
    *,
    v1_manifest_path: Path,
    v1_detail_path: Path,
    evidence_path: Path,
) -> list[str]:
    errors: list[str] = []
    expected_files = (
        (
            "v1 archive manifest bytes",
            Path(v1_manifest_path).stat().st_size,
            V1_EXPECTED_MANIFEST_BYTES,
        ),
        (
            "v1 archive manifest SHA-256",
            _file_sha256(Path(v1_manifest_path)),
            V1_EXPECTED_MANIFEST_BYTES_SHA256,
        ),
        (
            "v1 archive detail bytes",
            Path(v1_detail_path).stat().st_size,
            V1_EXPECTED_DETAIL_BYTES,
        ),
        (
            "v1 archive detail SHA-256",
            _file_sha256(Path(v1_detail_path)),
            V1_EXPECTED_DETAIL_BYTES_SHA256,
        ),
    )
    for label, actual, expected in expected_files:
        if actual != expected:
            errors.append(f"{label} mismatch: {actual}/{expected}")
    try:
        evidence = pd.read_csv(evidence_path, dtype=str, keep_default_na=False)
    except (OSError, pd.errors.ParserError) as exc:
        return errors + [f"v1 archive evidence cannot be parsed: {exc}"]
    if list(evidence.columns) != list(V1_ARCHIVE_EVIDENCE_COLUMNS):
        return errors + ["v1 archive evidence schema mismatch"]
    if len(evidence) != 1:
        return errors + ["v1 archive evidence must contain exactly one row"]
    row = evidence.iloc[0]
    expected_values = {
        "model_id": MODEL_ID,
        "artifact_id": ARTIFACT_ID,
        "projection_id": PROJECTION_ID,
        "projection_version": V1_ARTIFACT_VERSION,
        "cutoff_date": CUTOFF_DATE,
        "canonical_manifest_path": (
            "output/latest/research_backtest/"
            "revenue_unreacted_range_source_snapshot_projection_manifest_latest.csv"
        ),
        "archive_manifest_path": (
            "output/history/research/"
            "revenue_unreacted_range_source_snapshot_projection_manifest_v1_20260731.csv"
        ),
        "canonical_manifest_bytes": str(V1_EXPECTED_MANIFEST_BYTES),
        "canonical_manifest_sha256": V1_EXPECTED_MANIFEST_BYTES_SHA256,
        "canonical_detail_path": (
            "output/latest/research_backtest/"
            "revenue_unreacted_range_source_snapshot_projection_detail_latest.csv"
        ),
        "archive_detail_path": (
            "output/history/research/"
            "revenue_unreacted_range_source_snapshot_projection_detail_v1_20260731.csv"
        ),
        "canonical_detail_bytes": str(V1_EXPECTED_DETAIL_BYTES),
        "canonical_detail_sha256": V1_EXPECTED_DETAIL_BYTES_SHA256,
        "projected_episode_row_count": str(V1_EXPECTED_DETAIL_ROW_COUNT),
        "projected_episode_semantic_sha256": V1_EXPECTED_DETAIL_SEMANTIC_SHA256,
        "immutable_copy_verified": "true",
        "research_only": "true",
        "formal_model_use_allowed": "false",
        "approved_for_daily": "false",
        "production_change": "false",
        "promotion_evidence_allowed": "false",
        "ranking_consumption_allowed": "false",
        "pdf_consumption_allowed": "false",
    }
    for column, expected in expected_values.items():
        if _payload_value(row[column]) != expected:
            errors.append(f"v1 archive evidence {column} mismatch")
    if not _payload_value(row["generated_at"]):
        errors.append("v1 archive evidence generated_at is empty")
    return errors


def _validate_versioned_v2_closure(
    *,
    revenue_path: Path,
    price_dir: Path,
    monthly_resolution_path: Path,
    price_resolution_path: Path,
    v1_manifest_path: Path = V1_ARCHIVE_MANIFEST_CSV,
    v1_detail_path: Path = V1_ARCHIVE_DETAIL_CSV,
    v1_evidence_path: Path = V1_ARCHIVE_EVIDENCE_CSV,
    v2_manifest_path: Path = V2_MANIFEST_CSV,
    v2_detail_path: Path = V2_PROJECTED_DETAIL_CSV,
    diff_summary_path: Path = V1_V2_DIFF_SUMMARY_CSV,
    diff_detail_path: Path = V1_V2_DIFF_DETAIL_CSV,
) -> list[str]:
    artifact_paths = {
        "v1 archive manifest": Path(v1_manifest_path),
        "v1 archive detail": Path(v1_detail_path),
        "v1 archive evidence": Path(v1_evidence_path),
        "v2 candidate manifest": Path(v2_manifest_path),
        "v2 candidate detail": Path(v2_detail_path),
        "v1/v2 diff summary": Path(diff_summary_path),
        "v1/v2 diff detail": Path(diff_detail_path),
    }
    started = {
        label: path.exists() or path.is_symlink()
        for label, path in artifact_paths.items()
    }
    if not any(started.values()):
        return []
    present = {label: path.is_file() for label, path in artifact_paths.items()}
    missing = [
        f"missing versioned source projection closure artifact: {label}: {artifact_paths[label]}"
        for label, exists in present.items()
        if not exists
    ]
    if missing:
        return missing
    errors = _validate_v1_archive_evidence(
        v1_manifest_path=Path(v1_manifest_path),
        v1_detail_path=Path(v1_detail_path),
        evidence_path=Path(v1_evidence_path),
    )
    replay_paths = (revenue_path, monthly_resolution_path, price_resolution_path)
    replay_missing = [str(path) for path in replay_paths if not Path(path).is_file()]
    if replay_missing:
        errors.extend(
            f"missing v2 source projection replay input: {path}"
            for path in replay_missing
        )
    else:
        try:
            v2_manifest = pd.read_csv(
                v2_manifest_path,
                dtype=str,
                keep_default_na=False,
            )
            v2_detail = pd.read_csv(
                v2_detail_path,
                dtype={"stock_id": str},
                keep_default_na=False,
                low_memory=False,
            )
            errors.extend(
                validate_frames(
                    v2_manifest,
                    v2_detail,
                    revenue_path=Path(revenue_path),
                    price_dir=Path(price_dir),
                    monthly_resolution_path=Path(monthly_resolution_path),
                    price_resolution_path=Path(price_resolution_path),
                )
            )
        except (OSError, pd.errors.ParserError) as exc:
            errors.append(f"v2 source projection candidate cannot be parsed: {exc}")
    errors.extend(
        validate_projection_v1_v2_diff(
            v1_manifest_path=Path(v1_manifest_path),
            v1_detail_path=Path(v1_detail_path),
            v2_manifest_path=Path(v2_manifest_path),
            v2_detail_path=Path(v2_detail_path),
            summary_path=Path(diff_summary_path),
            detail_path=Path(diff_detail_path),
        )
    )
    return errors


def validate(
    manifest_path: Path = MANIFEST_CSV,
    projected_detail_path: Path = PROJECTED_DETAIL_CSV,
    revenue_path: Path = REVENUE_HISTORY_CSV,
    price_dir: Path = PRICE_HISTORY_DIR,
    monthly_resolution_path: Path = MONTHLY_RESOLUTION_CSV,
    price_resolution_path: Path = PRICE_RESOLUTION_CSV,
) -> list[str]:
    projection_paths = (manifest_path, projected_detail_path)
    missing = [str(path) for path in projection_paths if not Path(path).is_file()]
    if missing:
        return [f"missing source snapshot projection input: {path}" for path in missing]
    manifest = pd.read_csv(manifest_path, dtype=str, keep_default_na=False)
    projected_detail = pd.read_csv(
        projected_detail_path,
        dtype={"stock_id": str},
        keep_default_na=False,
        low_memory=False,
    )
    canonical_paths = (
        Path(manifest_path).resolve() == MANIFEST_CSV.resolve()
        and Path(projected_detail_path).resolve() == PROJECTED_DETAIL_CSV.resolve()
    )
    canonical_projection_version = (
        _payload_value(manifest.iloc[0].get("projection_version", ""))
        if len(manifest) == 1
        else ""
    )
    if canonical_paths and canonical_projection_version == V2_ARTIFACT_VERSION:
        return [
            "canonical source snapshot projection latest must remain "
            f"{V1_ARTIFACT_VERSION}; found {V2_ARTIFACT_VERSION}"
        ]
    versioned_closure_started = any(
        path.exists() or path.is_symlink()
        for path in (
            V1_ARCHIVE_MANIFEST_CSV,
            V1_ARCHIVE_DETAIL_CSV,
            V1_ARCHIVE_EVIDENCE_CSV,
            V2_MANIFEST_CSV,
            V2_PROJECTED_DETAIL_CSV,
            V1_V2_DIFF_SUMMARY_CSV,
            V1_V2_DIFF_DETAIL_CSV,
        )
    )
    if (
        canonical_paths
        and versioned_closure_started
        and len(manifest) == 1
        and canonical_projection_version == V1_ARTIFACT_VERSION
    ):
        errors = _validate_immutable_v1_files(
            manifest,
            projected_detail,
            manifest_path=Path(manifest_path),
            projected_detail_path=Path(projected_detail_path),
        )
        errors.extend(
            _validate_versioned_v2_closure(
                revenue_path=Path(revenue_path),
                price_dir=Path(price_dir),
                monthly_resolution_path=Path(monthly_resolution_path),
                price_resolution_path=Path(price_resolution_path),
                v1_manifest_path=V1_ARCHIVE_MANIFEST_CSV,
                v1_detail_path=V1_ARCHIVE_DETAIL_CSV,
                v1_evidence_path=V1_ARCHIVE_EVIDENCE_CSV,
                v2_manifest_path=V2_MANIFEST_CSV,
                v2_detail_path=V2_PROJECTED_DETAIL_CSV,
                diff_summary_path=V1_V2_DIFF_SUMMARY_CSV,
                diff_detail_path=V1_V2_DIFF_DETAIL_CSV,
            )
        )
        return errors
    replay_paths = (revenue_path, monthly_resolution_path, price_resolution_path)
    missing = [str(path) for path in replay_paths if not Path(path).is_file()]
    if missing:
        return [f"missing source snapshot projection input: {path}" for path in missing]
    return validate_frames(
        manifest,
        projected_detail,
        revenue_path=Path(revenue_path),
        price_dir=Path(price_dir),
        monthly_resolution_path=Path(monthly_resolution_path),
        price_resolution_path=Path(price_resolution_path),
    )


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Independently validate the revenue source snapshot projection."
    )
    parser.add_argument("--manifest", type=Path, default=MANIFEST_CSV)
    parser.add_argument("--projected-detail", type=Path, default=PROJECTED_DETAIL_CSV)
    parser.add_argument("--revenue-history", type=Path, default=REVENUE_HISTORY_CSV)
    parser.add_argument("--price-dir", type=Path, default=PRICE_HISTORY_DIR)
    parser.add_argument("--monthly-resolution", type=Path, default=MONTHLY_RESOLUTION_CSV)
    parser.add_argument("--price-resolution", type=Path, default=PRICE_RESOLUTION_CSV)
    parser.add_argument(
        "--candidate-v2",
        action="store_true",
        help="Validate the exact versioned v2 candidate instead of canonical v1.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    manifest_path = V2_MANIFEST_CSV if args.candidate_v2 else args.manifest
    projected_detail_path = (
        V2_PROJECTED_DETAIL_CSV
        if args.candidate_v2
        else args.projected_detail
    )
    errors = validate(
        manifest_path=manifest_path,
        projected_detail_path=projected_detail_path,
        revenue_path=args.revenue_history,
        price_dir=args.price_dir,
        monthly_resolution_path=args.monthly_resolution,
        price_resolution_path=args.price_resolution,
    )
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1
    manifest = pd.read_csv(
        manifest_path,
        dtype=str,
        keep_default_na=False,
    ).iloc[0]
    print(
        "revenue source snapshot projection validation passed: "
        f"cutoff={manifest['cutoff_date']}; "
        f"episodes={manifest['projected_episode_row_count']}; "
        f"semantic_sha256={manifest['projected_episode_semantic_sha256']}; "
        "formal_model_use_allowed=false"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
