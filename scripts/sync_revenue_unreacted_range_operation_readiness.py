from __future__ import annotations

import argparse
from bisect import bisect_left
import csv
from dataclasses import dataclass
from decimal import Decimal, InvalidOperation
import hashlib
import importlib.metadata
import io
import json
import math
import numbers
import os
import re
import subprocess
import sys
import tempfile
from pathlib import Path
from typing import Any, Callable

import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent))

from tracking_utils import markdown_table, now_text, safe_str  # noqa: E402


MODEL_ID = "revenue_unreacted_range"
REVENUE_MODEL_ID = MODEL_ID
REVENUE_ANOMALY_VALIDATOR_REL = (
    "scripts/validate_revenue_unreacted_range_anomaly_dispositions.py"
)
REVENUE_ANOMALY_REGISTRY_PATH = Path(
    "config/revenue_unreacted_range_anomaly_disposition_registry_v3_20260829.csv"
)


@dataclass(frozen=True)
class RevenuePromotionReadinessProfile:
    decision_id: str
    contract_version: str
    decision_status: str
    anomaly_disposition_gate: str
    formal_adapter_gate: str
    promotion_scope: str
    registry_canonical_sha256: str
    adapter_validation_required: bool
    operation_module_status: str
    daily_adapter_status: str
    operation_module_id: str


REVENUE_PROMOTION_DECISION_V4 = (
    "revenue_unreacted_range_source_mid_falling_promotion_preparation_v4_20260829"
)
REVENUE_PROMOTION_DECISION_V5 = (
    "revenue_unreacted_range_source_mid_falling_promotion_preparation_v5_20260829"
)
REVENUE_ANOMALY_DISPOSITION_GATE = (
    "verified_8_real_extreme_1_data_error_repaired_effective_blockers_0"
)
REVENUE_DISABLED_OPERATION_MODULE_ID = (
    "revenue_unreacted_range_source_mid_falling_v2_operation_v1"
)
REVENUE_PROMOTION_PROFILES = {
    REVENUE_PROMOTION_DECISION_V4: RevenuePromotionReadinessProfile(
        decision_id=REVENUE_PROMOTION_DECISION_V4,
        contract_version=(
            "revenue_unreacted_range_promotion_preparation_contract_v5_20260829"
        ),
        decision_status=(
            "anomaly_disposition_complete_promotion_blocked_waiting_forward_holdout_"
            "and_formal_adapter"
        ),
        anomaly_disposition_gate=REVENUE_ANOMALY_DISPOSITION_GATE,
        formal_adapter_gate=(
            "disabled_adapter_preparation_non_hard_production_approval_hard_gate"
        ),
        promotion_scope=(
            "research_only_anomaly_disposition_closed_waiting_forward_holdout_and_"
            "disabled_adapter_no_production_daily_full_pdf_or_apps_script"
        ),
        registry_canonical_sha256=(
            "520b453f22f1b943d6c6241094e5b4df9729810c980e680e9f2027698d9bf5db"
        ),
        adapter_validation_required=False,
        operation_module_status=(
            "research_matrix_complete_formal_adapter_not_started"
        ),
        daily_adapter_status="not_started",
        operation_module_id="",
    ),
    REVENUE_PROMOTION_DECISION_V5: RevenuePromotionReadinessProfile(
        decision_id=REVENUE_PROMOTION_DECISION_V5,
        contract_version=(
            "revenue_unreacted_range_promotion_preparation_contract_v6_20260829"
        ),
        decision_status="promotion_blocked_waiting_forward_holdout_v2_maturity",
        anomaly_disposition_gate=REVENUE_ANOMALY_DISPOSITION_GATE,
        formal_adapter_gate=(
            "disabled_adapter_preparation_validated_non_hard_production_approval_"
            "hard_gate"
        ),
        promotion_scope=(
            "research_only_anomaly_closed_disabled_adapter_preparation_validated_"
            "waiting_forward_holdout_v2_maturity_no_production_daily_full_pdf_"
            "packet_runtime_artifact_or_apps_script"
        ),
        registry_canonical_sha256=(
            "da74a4a96d5db27e5ec8209c7d2b57c6dfe19f79761f844ef160ce86bba34869"
        ),
        adapter_validation_required=True,
        operation_module_status="disabled_adapter_preparation_validated",
        daily_adapter_status="disabled_no_runtime_artifact",
        operation_module_id=REVENUE_DISABLED_OPERATION_MODULE_ID,
    ),
}
REVENUE_CURRENT_PROMOTION_PROFILE = REVENUE_PROMOTION_PROFILES[
    REVENUE_PROMOTION_DECISION_V5
]
# Current-profile aliases remain available to older model-owned callers.  Row
# validation itself is decision-id keyed so an append-only v4 source still
# validates against the exact v4 contract instead of being silently reinterpreted.
REVENUE_EXPECTED_PROMOTION_DECISION = {
    "contract_version": REVENUE_CURRENT_PROMOTION_PROFILE.contract_version,
    "decision_status": REVENUE_CURRENT_PROMOTION_PROFILE.decision_status,
    "anomaly_disposition_gate": (
        REVENUE_CURRENT_PROMOTION_PROFILE.anomaly_disposition_gate
    ),
    "formal_adapter_gate": REVENUE_CURRENT_PROMOTION_PROFILE.formal_adapter_gate,
    "promotion_scope": REVENUE_CURRENT_PROMOTION_PROFILE.promotion_scope,
}
REVENUE_PROMOTION_CONTRACT_VERSION = (
    REVENUE_CURRENT_PROMOTION_PROFILE.contract_version
)
REVENUE_ADAPTER_VALIDATOR_REL = (
    "scripts/validate_revenue_unreacted_range_operation_adapter.py"
)
REVENUE_ADAPTER_MODULE_REL = (
    "scripts/revenue_unreacted_range_operation_adapter.py"
)
REVENUE_ADAPTER_VALIDATION_TIMEOUT_SECONDS = 300
REVENUE_ADAPTER_VALIDATION_PASS = (
    "revenue_unreacted_range disabled adapter preparation validation passed: "
    "8 in-memory empty rows; no runtime artifact; all permissions false"
)
REVENUE_FORWARD_HOLDOUT_V2_ARTIFACT_ID = (
    "revenue_unreacted_range_forward_holdout_v2"
)
REVENUE_FORWARD_HOLDOUT_V2_ARTIFACT_VERSION = "forward_holdout_v2_20260828"
REVENUE_FORWARD_HOLDOUT_V2_START_DATE = "20260831"
REVENUE_SOURCE_VARIANT_ID = "source_mid_falling"
REVENUE_PROMOTION_FINANCIAL_STATEMENT_SCOPE = (
    "monthly_revenue_only_EPS_gross_margin_operating_margin_operating_income_"
    "non_operating_income_net_income_excluded"
)
REVENUE_HOLDOUT_FINANCIAL_STATEMENT_SCOPE = (
    "monthly_revenue_only;EPS_gross_margin_operating_margin_operating_income_"
    "non_operating_income_net_income_excluded"
)
REVENUE_RESEARCH_MATRIX_STATUS = "research_matrix_complete"
REVENUE_OPERATION_MODULE_STATUS = (
    REVENUE_CURRENT_PROMOTION_PROFILE.operation_module_status
)

PREREGISTRATION_PR_NUMBER = "462"
PREREGISTRATION_MERGE_COMMIT = "436c25cd0d037c3425ab2ac4fa76cb464cf96de4"
RULE_CONTRACT_VERSION = "revenue_low_mid_falling_forward_holdout_rule_v2"
RULE_CANONICAL_SHA256 = (
    "3918b336ff995b9a8f1425cd48cc51a84c8c015a58e81668f357ca048145f9e3"
)
DATA_CONTRACT_VERSION = "revenue_low_mid_falling_forward_holdout_data_v3_20260829"
DATA_CONTRACT_SHA256 = (
    "1fe90402b55f57cb3f7070d5b2c7ea8d8560fe4d284450efc0616e147ce51532"
)
PRICE_SEMANTIC_PROJECTION_VERSION = (
    "revenue_forward_holdout_raw_price_source_projection_v1_20260829"
)
PRICE_SEMANTIC_PROJECTION_SCHEMA_SHA256 = (
    "7ef675db9ab08c7fc88dc0382571f0a16ad346a646fe3ccdf0ccfe18bb5106a9"
)
PRICE_SEMANTIC_PROJECTION_COLUMNS = (
    "session_sequence_index",
    "date",
    "open",
    "high",
    "low",
    "close",
    "analysis_price_adjustment_factor",
    "price_resolution_ids_on_date",
)
PRICE_SEMANTIC_PROJECTION_DECIMAL_SCALE = 8
PRICE_SEMANTIC_PROJECTION_ROLE = "composite_promotion_input_lineage_component"
PRICE_SEMANTIC_PROJECTION_MIGRATION_ID = (
    "revenue_forward_holdout_v2_price_semantic_projection_v1_20260829"
)
PRICE_SEMANTIC_PROJECTION_AUTHORIZATION_REFERENCE = (
    "user_authorized_3A_3C_20260829"
)
PRICE_INPUT_LEGACY_LINEAGE_ROLE = (
    "provenance_diagnostic_only_not_promotion_gate"
)
TRAINING_CUTOFF_DATE = "20260713"
BRIDGE_START_DATE = "20260714"
BRIDGE_END_DATE = "20260830"
HOLDOUT_START_DATE = REVENUE_FORWARD_HOLDOUT_V2_START_DATE
HOLDING_DAYS = 30
HOLDING_SESSION_INDEX_OFFSET = HOLDING_DAYS - 1
OPERATION_RETURN_REVIEW_THRESHOLD_PCT = 80.0
SOURCE_ARTIFACT_ID = "revenue_unreacted_range_source_first_condition_audit"
SOURCE_ARTIFACT_VERSION = "source_first_condition_v3_20260720"
SOURCE_PROJECTION_ARTIFACT_ID = "revenue_unreacted_range_source_snapshot_projection"
SOURCE_PROJECTION_ARTIFACT_VERSION = "source_snapshot_projection_v2_20260822"
PROJECTED_EPISODE_ROW_COUNT = 19565
PROJECTED_EPISODE_SEMANTIC_SHA256 = (
    "dacd5046e8af9abcd766b11b9557035481cc82af9d7fba746a8dad1ff183a967"
)
SELECTED_V2_MANIFEST_CANONICAL_SHA256 = (
    "74b51a715c560777ea302fe559d89f74575ff94381c8cee1fa49496c25b7db2b"
)
SELECTED_V2_MANIFEST_PROMOTION_SEMANTIC_SHA256 = (
    "897553efa0f569f8edc16f8f1ac126316a6dcbb5ac073a5c29e527f7e198c2eb"
)
PRIMARY_VARIANT_ID = REVENUE_SOURCE_VARIANT_ID
ALL_VARIANT_IDS = (
    PRIMARY_VARIANT_ID,
    "source_low_falling",
    "source_low_or_mid_falling_union",
)
VARIANT_MEMBERSHIP_COLUMNS = {
    PRIMARY_VARIANT_ID: "primary_variant_member",
    "source_low_falling": "low_falling_member",
    "source_low_or_mid_falling_union": "low_or_mid_falling_union_member",
}
CONFIRMATION_VARIANT_ID = "delayed_next_close_continuation_bonus"
LIFECYCLE_POLICY_ID = "rearm_after_realized_exit_next_trade_day"
STOP_POLICY_ID = "none_no_stop_reference"
SOURCE_VARIANT_ID = "absolute_or_two_month_yoy_ge15"
MONTHLY_LINEAGE_COLUMNS = (
    "monthly_revenue_history_blob_sha256",
    "monthly_revenue_canonical_table_sha256",
    "cross_market_resolution_registry_canonical_sha256",
)
CANONICAL_LINEAGE_VERSION = "canonical_json_numeric_text_v1"
PROMOTION_REGISTRY_CANONICAL_SHA256 = (
    REVENUE_CURRENT_PROMOTION_PROFILE.registry_canonical_sha256
)
OUT_CSV_REL = "output/latest/model_operation_readiness_latest.csv"
OUT_MD_REL = "output/latest/model_operation_readiness_latest.md"
DOCS_CSV_REL = "docs/latest/model_operation_readiness_latest.csv"
DOCS_MD_REL = "docs/latest/model_operation_readiness_latest.md"
READINESS_MIRROR_RELS = (
    OUT_CSV_REL,
    OUT_MD_REL,
    DOCS_CSV_REL,
    DOCS_MD_REL,
)
EXACT_PREDECESSOR_READINESS_CANONICAL_SHA256 = {
    OUT_CSV_REL: "0ef5c470d7dd87e191e5efefe00f6f65af87b1d7af1b6d9ec6b4e45f5bb754d8",
    OUT_MD_REL: "28b8c0b276d18e4ed59d04373a59b886806d464c54a79f28486cdccd49494526",
    DOCS_CSV_REL: "0ef5c470d7dd87e191e5efefe00f6f65af87b1d7af1b6d9ec6b4e45f5bb754d8",
    DOCS_MD_REL: "28b8c0b276d18e4ed59d04373a59b886806d464c54a79f28486cdccd49494526",
}
# Raw Git blob ids are recorded only for transition diagnostics.  They are not
# gates because checkout line endings may differ while canonical semantics do not.
EXACT_PREDECESSOR_READINESS_RAW_BLOB_OID_DIAGNOSTIC = {
    OUT_CSV_REL: "a4f7d644266bac5c531a83ac3f8cb90dc63f7f47",
    OUT_MD_REL: "3f227660876bb16792d34d918d2314809d129bac",
    DOCS_CSV_REL: "a4f7d644266bac5c531a83ac3f8cb90dc63f7f47",
    DOCS_MD_REL: "3f227660876bb16792d34d918d2314809d129bac",
}

PROMOTION_REGISTRY_REL = (
    "config/revenue_unreacted_range_promotion_preparation_registry.csv"
)
ANOMALY_REGISTRY_REL = (
    REVENUE_ANOMALY_REGISTRY_PATH.as_posix()
)
FORWARD_HOLDOUT_V2_MANIFEST_REL = (
    "output/latest/research_backtest/"
    "revenue_unreacted_range_forward_holdout_v2_manifest_latest.csv"
)
FORWARD_HOLDOUT_V2_DETAIL_REL = (
    "output/latest/research_backtest/"
    "revenue_unreacted_range_forward_holdout_v2_event_detail_latest.csv"
)
FORWARD_HOLDOUT_V2_SUMMARY_REL = (
    "output/latest/research_backtest/"
    "revenue_unreacted_range_forward_holdout_v2_maturity_status_latest.csv"
)
FORWARD_HOLDOUT_V2_COMPARISON_REL = (
    "output/latest/research_backtest/"
    "revenue_unreacted_range_forward_holdout_v2_comparison_latest.csv"
)
FORWARD_HOLDOUT_V2_ANOMALY_SENSITIVITY_REL = (
    "output/latest/research_backtest/"
    "revenue_unreacted_range_forward_holdout_v2_anomaly_sensitivity_latest.csv"
)
FORWARD_HOLDOUT_V2_REPLAY_SOURCE_REL = (
    "output/latest/research_backtest/"
    "revenue_unreacted_range_forward_holdout_v2_replay_source_detail_latest.csv"
)
SOURCE_PROJECTION_MANIFEST_REL = (
    "output/latest/research_backtest/"
    "revenue_unreacted_range_source_snapshot_projection_manifest_latest.csv"
)
PRICE_HISTORY_DIR_REL = "data/stock_price_history"
MONTHLY_REVENUE_HISTORY_REL = (
    "data/monthly_revenue_history/monthly_revenue_history.csv"
)
MONTHLY_REVENUE_CROSS_MARKET_RESOLUTION_REL = (
    "config/revenue_unreacted_range_monthly_revenue_cross_market_resolution.csv"
)
PRICE_RESOLUTION_REL = (
    "config/revenue_unreacted_range_price_comparability_resolution.csv"
)
CANONICAL_SOURCE_RELS = (
    PROMOTION_REGISTRY_REL,
    ANOMALY_REGISTRY_REL,
    FORWARD_HOLDOUT_V2_MANIFEST_REL,
    FORWARD_HOLDOUT_V2_DETAIL_REL,
    FORWARD_HOLDOUT_V2_SUMMARY_REL,
    FORWARD_HOLDOUT_V2_COMPARISON_REL,
    FORWARD_HOLDOUT_V2_ANOMALY_SENSITIVITY_REL,
    FORWARD_HOLDOUT_V2_REPLAY_SOURCE_REL,
    SOURCE_PROJECTION_MANIFEST_REL,
    PRICE_RESOLUTION_REL,
)

REVENUE_PROMOTION_REGISTRY_CSV = Path(PROMOTION_REGISTRY_REL)
REVENUE_ANOMALY_REGISTRY_CSV = Path(ANOMALY_REGISTRY_REL)
REVENUE_FORWARD_HOLDOUT_V2_MANIFEST_CSV = Path(
    FORWARD_HOLDOUT_V2_MANIFEST_REL
)
REVENUE_FORWARD_HOLDOUT_V2_DETAIL_CSV = Path(FORWARD_HOLDOUT_V2_DETAIL_REL)
REVENUE_FORWARD_HOLDOUT_V2_SUMMARY_CSV = Path(FORWARD_HOLDOUT_V2_SUMMARY_REL)
REVENUE_FORWARD_HOLDOUT_V2_REPLAY_SOURCE_CSV = Path(
    FORWARD_HOLDOUT_V2_REPLAY_SOURCE_REL
)
REVENUE_SOURCE_PROJECTION_MANIFEST_CSV = Path(SOURCE_PROJECTION_MANIFEST_REL)

LEGACY_COLUMNS = (
    "generated_at",
    "model_id",
    "model_name_zh",
    "parity_status",
    "blocker",
    "operation_module_status",
    "daily_adapter_status",
    "approved_for_daily",
    "approval_status",
    "operation_module_id",
    "approval_version",
    "presentation_allowed",
    "operation_directive_level",
    "pdf_integration_status",
    "packet_integration_status",
    "registry_pattern_count",
    "registry_current_model_pattern_count",
    "registry_best_pattern_id",
    "registry_best_sample_size",
    "registry_best_win_rate",
    "registry_best_median_return",
    "daily_adapter_row_count",
    "daily_adapter_data_row_count",
    "daily_adapter_sections",
    "status_note_zh",
)
TARGET_COLUMNS = (
    *LEGACY_COLUMNS[:7],
    "formal_model_use_allowed",
    *LEGACY_COLUMNS[7:12],
    "production_allowed",
    *LEGACY_COLUMNS[12:],
)
REVENUE_PERMISSION_COLUMNS = {
    "formal_model_use_allowed",
    "production_allowed",
}
ROW_IDENTITY_COLUMNS = {"generated_at", "model_id", "model_name_zh"}
SUMMARY_COLUMNS = set(TARGET_COLUMNS) - ROW_IDENTITY_COLUMNS
STATUS_TABLE_COLUMNS = (
    "model_id",
    "parity_status",
    "operation_module_status",
    "daily_adapter_status",
    "formal_model_use_allowed",
    "approved_for_daily",
    "approval_status",
    "operation_module_id",
    "approval_version",
    "presentation_allowed",
    "production_allowed",
    "operation_directive_level",
    "pdf_integration_status",
    "packet_integration_status",
    "blocker",
    "status_note_zh",
)
SHA256_RE = re.compile(r"^[0-9a-f]{64}$")
HOLDOUT_FALSE_FIELDS = (
    "formal_model_use_allowed",
    "approved_for_daily",
    "presentation_allowed",
    "promotion_evidence_allowed",
    "production_change",
)
MANIFEST_EXTRA_FALSE_FIELDS = (
    "ranking_consumption_allowed",
    "pdf_consumption_allowed",
)
_EXACT_PRICE_LINEAGE_CACHE: dict[tuple[str, ...], dict[str, Any]] = {}
EXACT_REPLAY_CHILD_MODULES = (
    "revenue_unreacted_range_forward_holdout_v2",
    "validate_revenue_unreacted_range_forward_holdout_v2",
)
EXACT_REPLAY_CHILD_MODE = "trusted_same_model_in_memory_canonical_replay"
EXACT_REPLAY_PROTOCOL_VERSION = "revenue_readiness_exact_replay_v3_20260829"
EXACT_REPLAY_SENTINEL = "REVENUE_EXACT_PRICE_LINEAGE_JSON="
EXACT_REPLAY_TIMEOUT_SECONDS = 1800
RAW_MONTHLY_REVENUE_PROVENANCE_COLUMN = "monthly_revenue_history_blob_sha256"
SOURCE_DETAIL_LEGACY_ENVELOPE_COLUMN = "source_detail_canonical_sha256"
CAPTURE_LEGACY_ENVELOPE_COLUMN = "capture_id"
EVENT_LEGACY_ENVELOPE_COLUMN = "event_row_canonical_sha256"
LEGACY_ENVELOPE_COLUMNS = (
    SOURCE_DETAIL_LEGACY_ENVELOPE_COLUMN,
    CAPTURE_LEGACY_ENVELOPE_COLUMN,
)
LEGACY_PRICE_PROVENANCE_COLUMNS = (
    "price_input_stock_count",
    "price_input_row_count",
    "price_input_stock_canonical_sha256s",
    "price_input_canonical_sha256",
)
PROMOTION_SEMANTIC_FRAME_EXCLUSIONS = {
    "manifest": (
        "generated_at",
        RAW_MONTHLY_REVENUE_PROVENANCE_COLUMN,
        *LEGACY_ENVELOPE_COLUMNS,
        *LEGACY_PRICE_PROVENANCE_COLUMNS,
    ),
    "detail": (
        "generated_at",
        RAW_MONTHLY_REVENUE_PROVENANCE_COLUMN,
        *LEGACY_ENVELOPE_COLUMNS,
        EVENT_LEGACY_ENVELOPE_COLUMN,
        *LEGACY_PRICE_PROVENANCE_COLUMNS,
    ),
    "summary": ("generated_at", CAPTURE_LEGACY_ENVELOPE_COLUMN),
    "comparison": ("generated_at", CAPTURE_LEGACY_ENVELOPE_COLUMN),
    "anomaly": ("generated_at", CAPTURE_LEGACY_ENVELOPE_COLUMN),
}

_EXACT_REPLAY_CHILD_BOOTSTRAP_TEMPLATE = r'''
import sys

EXPECTED_COMMIT_SHA = __EXPECTED_COMMIT_SHA__
EXPECTED_TREE_SHA = __EXPECTED_TREE_SHA__
'''


def _canonical_numeric_text(text: str) -> str | None:
    candidate = text.strip()
    if not re.fullmatch(
        r"[+-]?(?:(?:\d+(?:\.\d*)?)|(?:\.\d+))(?:[eE][+-]?\d+)?",
        candidate,
    ):
        return None
    unsigned = candidate.lstrip("+-")
    integer_part = re.split(r"[eE]", unsigned, maxsplit=1)[0].split(".", maxsplit=1)[0]
    if len(integer_part) > 1 and integer_part.startswith("0"):
        return None
    if len(integer_part) > 18:
        return None
    try:
        number = Decimal(candidate)
    except InvalidOperation:
        return None
    if not number.is_finite():
        return None
    if number == 0:
        return "0"
    rendered = format(number.normalize(), "f")
    return rendered.rstrip("0").rstrip(".") if "." in rendered else rendered


def _canonical_value(value: object) -> str:
    if value is None:
        return ""
    if isinstance(value, bool):
        return "true" if value else "false"
    if isinstance(value, numbers.Integral):
        return str(int(value))
    if isinstance(value, numbers.Real):
        number = float(value)
        return format(number, ".15g") if math.isfinite(number) else ""
    if not isinstance(value, (str, bytes, list, dict, tuple)):
        try:
            if pd.isna(value):
                return ""
        except (TypeError, ValueError):
            pass
    text = str(value).strip()
    if text.lower() in {"true", "false"}:
        return text.lower()
    numeric = _canonical_numeric_text(text)
    return numeric if numeric is not None else text


def _canonical_json_sha256(payload: object) -> str:
    return hashlib.sha256(
        json.dumps(
            payload,
            ensure_ascii=False,
            separators=(",", ":"),
            sort_keys=True,
        ).encode("utf-8")
    ).hexdigest()


def _source_mapping_sha256(mapping: dict[str, object]) -> str:
    payload = [
        [str(column), _canonical_value(value)]
        for column, value in sorted(mapping.items(), key=lambda item: str(item[0]))
        if str(column) != "generated_at"
    ]
    return hashlib.sha256(
        json.dumps(payload, ensure_ascii=False, separators=(",", ":")).encode("utf-8")
    ).hexdigest()


def _canonical_mapping_sha256(mapping: dict[str, object]) -> str:
    payload = [
        [str(key), _canonical_value(value)]
        for key, value in sorted(mapping.items())
        if str(key) != "generated_at"
    ]
    return _canonical_json_sha256([CANONICAL_LINEAGE_VERSION, payload])


def _canonical_frame_sha256(
    frame: pd.DataFrame,
    *,
    excluded_columns: tuple[str, ...] = ("generated_at",),
) -> str:
    excluded = set(excluded_columns)
    columns = sorted(column for column in frame.columns if column not in excluded)
    rows = [
        [_canonical_value(value) for value in row]
        for row in frame.loc[:, columns].itertuples(index=False, name=None)
    ]
    rows.sort()
    return _canonical_json_sha256([CANONICAL_LINEAGE_VERSION, columns, rows])


def _is_transport_provenance_column(column: object) -> bool:
    normalized = str(column).strip().lower()
    return (
        normalized == "generated_at"
        or "raw_file_sha" in normalized
        or "blob_sha256" in normalized
        or "byte_sha256" in normalized
        or "bytes_sha256" in normalized
        or "crlf" in normalized
        or "line_ending" in normalized
    )


def _promotion_semantic_source_sha256(frame: pd.DataFrame) -> str:
    """Bind every source business/PIT cell, excluding transport provenance."""

    return _canonical_frame_sha256(
        frame,
        excluded_columns=tuple(
            column
            for column in frame.columns
            if _is_transport_provenance_column(column)
        ),
    )


def _promotion_semantic_frame_sha256(
    frame: pd.DataFrame,
    *,
    frame_name: str,
) -> str:
    """Hash every non-envelope field; legacy hashes stay internally validated."""

    if frame_name not in PROMOTION_SEMANTIC_FRAME_EXCLUSIONS:
        raise RuntimeError(
            f"unsupported revenue promotion semantic frame: {frame_name}"
        )
    excluded = set(PROMOTION_SEMANTIC_FRAME_EXCLUSIONS[frame_name])
    excluded.update(
        column
        for column in frame.columns
        if _is_transport_provenance_column(column)
    )
    return _canonical_frame_sha256(
        frame,
        excluded_columns=tuple(sorted(excluded)),
    )


def _projection_manifest_promotion_semantic_sha256(frame: pd.DataFrame) -> str:
    return _canonical_frame_sha256(
        frame,
        excluded_columns=tuple(
            column
            for column in frame.columns
            if _is_transport_provenance_column(column)
        ),
    )


def _canonical_table_sha256(frame: pd.DataFrame) -> str:
    columns = sorted(column for column in frame.columns if column != "generated_at")
    rows = sorted(
        [
            [_canonical_value(row[column]) for column in columns]
            for _, row in frame.loc[:, columns].iterrows()
        ]
    )
    payload = {
        "canonical_lineage_version": CANONICAL_LINEAGE_VERSION,
        "columns": columns,
        "rows": rows,
    }
    return hashlib.sha256(
        json.dumps(payload, ensure_ascii=False, separators=(",", ":")).encode("utf-8")
    ).hexdigest()


def _stock_id(value: object) -> str:
    text = str(value or "").strip()
    return text[:-2] if text.endswith(".0") and text[:-2].isdigit() else text


def _normalize_replay_source(source_first_detail: pd.DataFrame) -> pd.DataFrame:
    required = {
        "model_id",
        "artifact_id",
        "artifact_version",
        "condition_variant_id",
        "episode_key",
        "stock_id",
        "stock_name",
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
        *MONTHLY_LINEAGE_COLUMNS,
    }
    missing = sorted(required - set(source_first_detail.columns))
    if missing:
        raise RuntimeError(
            f"revenue readiness replay source missing columns: {missing}"
        )
    for field_name, expected in {
        "model_id": MODEL_ID,
        "artifact_id": SOURCE_ARTIFACT_ID,
        "artifact_version": SOURCE_ARTIFACT_VERSION,
    }.items():
        if set(source_first_detail[field_name].astype(str).str.strip()) != {expected}:
            raise RuntimeError(
                f"revenue readiness replay source {field_name} drift"
            )
    for field_name in MONTHLY_LINEAGE_COLUMNS:
        values = set(source_first_detail[field_name].astype(str).str.strip().str.lower())
        if len(values) != 1 or SHA256_RE.fullmatch(next(iter(values))) is None:
            raise RuntimeError(
                f"revenue readiness replay source {field_name} is not constant SHA-256"
            )
    source = source_first_detail.loc[
        source_first_detail["condition_variant_id"].astype(str).eq(SOURCE_VARIANT_ID)
    ].copy()
    if source.empty:
        raise RuntimeError("revenue readiness replay source selected variant is empty")
    source["stock_id"] = source["stock_id"].map(_stock_id)
    if source["episode_key"].astype(str).duplicated().any():
        raise RuntimeError("revenue readiness replay source duplicate episode_key")
    selected_slice_sha256 = _canonical_table_sha256(source)
    source["source_first_canonical_row_sha256"] = source.apply(
        lambda row: _source_mapping_sha256(row.to_dict()),
        axis=1,
    )
    source["source_first_selected_slice_canonical_sha256"] = (
        selected_slice_sha256
    )
    return source.set_index("episode_key", drop=False)


def _replay_lineage_values(
    episode: pd.Series,
) -> dict[str, list[str] | list[int]]:
    episode_key = safe_str(episode.get("episode_key"))

    def split(field_name: str) -> list[str]:
        values = [part.strip() for part in str(episode.get(field_name, "")).split("|")]
        if not values or any(not value for value in values):
            raise RuntimeError(
                "revenue readiness replay source qualifying lineage contains a blank "
                f"value: {episode_key}/{field_name}"
            )
        return values

    periods = split("qualifying_revenue_periods")
    source_dates = [
        _strict_date(value, f"replay source qualifying_source_dates {episode_key}")
        for value in split("qualifying_source_dates")
    ]
    resolution_ids = split("qualifying_cross_market_resolution_ids")
    source_hashes = [
        _require_sha(
            value,
            f"replay source qualifying_source_row_canonical_sha256s {episode_key}",
        )
        for value in split("qualifying_source_row_canonical_sha256s")
    ]
    if any(value == "0" * 64 for value in source_hashes):
        raise RuntimeError(
            "revenue readiness replay source qualifying row lineage contains a "
            f"placeholder SHA-256: {episode_key}"
        )
    canonical_dates = [
        _strict_date(
            value,
            f"replay source qualifying_canonical_source_table_dates {episode_key}",
        )
        for value in split("qualifying_canonical_source_table_dates")
    ]
    trade_dates = [
        _strict_date(value, f"replay source qualifying_trade_dates {episode_key}")
        for value in split("qualifying_trade_dates")
    ]
    sequence_indices = [
        _strict_nonnegative_int(
            value,
            f"replay source qualifying_sequence_indices {episode_key}",
        )
        for value in split("qualifying_sequence_indices")
    ]
    expected_count = _strict_nonnegative_int(
        episode.get("qualifying_update_count"),
        f"replay source qualifying_update_count {episode_key}",
    )
    aligned_lengths = {
        len(periods),
        len(source_dates),
        len(resolution_ids),
        len(source_hashes),
        len(canonical_dates),
        len(trade_dates),
        len(sequence_indices),
        expected_count,
    }
    if len(aligned_lengths) != 1 or expected_count == 0:
        raise RuntimeError(
            "revenue readiness replay source qualifying lineage is not aligned: "
            f"{episode_key}"
        )
    if any(re.fullmatch(r"\d{6}", value) is None for value in periods):
        raise RuntimeError(
            f"revenue readiness replay source revenue period is invalid: {episode_key}"
        )
    scalar_expectations: dict[str, str | int] = {
        "episode_start_revenue_period": periods[0],
        "episode_start_source_date": source_dates[0],
        "episode_start_cross_market_resolution_id": resolution_ids[0],
        "episode_start_source_row_canonical_sha256": source_hashes[0],
        "episode_start_canonical_source_table_date": canonical_dates[0],
        "episode_start_trade_date": trade_dates[0],
        "episode_start_sequence_index": sequence_indices[0],
        "latest_qualifying_revenue_period": periods[-1],
        "latest_qualifying_source_date": source_dates[-1],
        "latest_qualifying_cross_market_resolution_id": resolution_ids[-1],
        "latest_qualifying_source_row_canonical_sha256": source_hashes[-1],
        "latest_qualifying_canonical_source_table_date": canonical_dates[-1],
        "latest_qualifying_trade_date": trade_dates[-1],
        "latest_qualifying_sequence_index": sequence_indices[-1],
    }
    integer_fields = {
        "episode_start_sequence_index",
        "latest_qualifying_sequence_index",
    }
    mismatches: list[str] = []
    for field_name, expected in scalar_expectations.items():
        if field_name in integer_fields:
            observed: str | int = _strict_nonnegative_int(
                episode.get(field_name), f"replay source {field_name} {episode_key}"
            )
        elif "date" in field_name:
            observed = _strict_date(
                episode.get(field_name), f"replay source {field_name} {episode_key}"
            )
        else:
            observed = _canonical_value(episode.get(field_name))
        if observed != expected:
            mismatches.append(field_name)
    if mismatches:
        raise RuntimeError(
            "revenue readiness replay source scalar/list lineage drift: "
            f"{episode_key}/{mismatches}"
        )
    return {
        "periods": periods,
        "source_dates": source_dates,
        "resolution_ids": resolution_ids,
        "source_hashes": source_hashes,
        "canonical_dates": canonical_dates,
        "trade_dates": trade_dates,
        "sequence_indices": sequence_indices,
    }


def _validate_replay_source_pit_lineage(
    normalized_source: pd.DataFrame,
    *,
    observed_through: str,
    registered_prices: dict[str, pd.DataFrame],
) -> None:
    price_dates = {
        stock_id: frame["date"].astype(str).tolist()
        for stock_id, frame in registered_prices.items()
    }
    price_date_indices = {
        stock_id: {date: index for index, date in enumerate(dates)}
        for stock_id, dates in price_dates.items()
    }
    for episode_key, episode in normalized_source.iterrows():
        lineage = _replay_lineage_values(episode)
        periods = lineage["periods"]
        source_dates = lineage["source_dates"]
        canonical_dates = lineage["canonical_dates"]
        trade_dates = lineage["trade_dates"]
        sequence_indices = lineage["sequence_indices"]
        if periods != sorted(set(periods)):
            raise RuntimeError(
                f"revenue readiness replay source periods are not strictly increasing: {episode_key}"
            )
        if source_dates != sorted(set(source_dates)):
            raise RuntimeError(
                f"revenue readiness replay source dates are not strictly increasing: {episode_key}"
            )
        if trade_dates != sorted(set(trade_dates)):
            raise RuntimeError(
                f"revenue readiness replay source trade dates are not strictly increasing: {episode_key}"
            )
        if sequence_indices != sorted(set(sequence_indices)):
            raise RuntimeError(
                "revenue readiness replay source sequence indices are not strictly "
                f"increasing: {episode_key}"
            )
        if canonical_dates != source_dates:
            raise RuntimeError(
                "revenue readiness replay source canonical/source date lineage drift: "
                f"{episode_key}"
            )
        if any(
            source_date > trade_date
            for source_date, trade_date in zip(source_dates, trade_dates)
        ):
            raise RuntimeError(
                f"revenue readiness replay source date exceeds trade date: {episode_key}"
            )
        if any(
            date > observed_through
            for date in [*source_dates, *canonical_dates, *trade_dates]
        ):
            raise RuntimeError(
                "revenue readiness replay source contains future PIT lineage beyond "
                f"observed_through_date: {episode_key}"
            )
        stock_id = _stock_id(episode.get("stock_id"))
        lineage_rows = list(
            zip(
                source_dates,
                trade_dates,
                sequence_indices,
            )
        )
        ordered_dates = price_dates.get(stock_id)
        if ordered_dates is None:
            raise RuntimeError(
                f"revenue readiness replay source lacks registered prices: {stock_id}"
            )
        date_index = price_date_indices[stock_id]
        for (
            source_date,
            trade_date,
            sequence_index,
        ) in lineage_rows:
            first_position = bisect_left(ordered_dates, source_date)
            first_available = (
                ordered_dates[first_position]
                if first_position < len(ordered_dates)
                else ""
            )
            if (
                first_available != trade_date
                or date_index.get(trade_date) != sequence_index
            ):
                raise RuntimeError(
                    "revenue readiness replay source trade date is not the first "
                    "normalized registered session on or after source availability: "
                    f"{episode_key}/{source_date}/{trade_date}"
                )


def _validate_detail_source_asof_against_replay(
    detail: pd.DataFrame,
    *,
    normalized_source: pd.DataFrame,
    registered_prices: dict[str, pd.DataFrame],
) -> None:
    for row_index, event in detail.iterrows():
        episode_key = safe_str(event.get("episode_key"))
        if episode_key not in normalized_source.index:
            raise RuntimeError(
                "revenue readiness holdout detail episode is absent from committed "
                f"replay source: {episode_key}"
            )
        episode = normalized_source.loc[episode_key]
        if isinstance(episode, pd.DataFrame):
            raise RuntimeError(
                f"revenue readiness replay source duplicate episode_key: {episode_key}"
            )
        stock_id = _stock_id(event.get("stock_id"))
        if _stock_id(episode.get("stock_id")) != stock_id:
            raise RuntimeError(
                f"revenue readiness detail/replay source stock identity drift: {episode_key}"
            )
        prices = registered_prices.get(stock_id)
        if prices is None:
            raise RuntimeError(
                f"revenue readiness detail source-asof lacks registered prices: {stock_id}"
            )
        lineage = _replay_lineage_values(episode)
        date_index = {
            safe_str(date): int(index) for index, date in prices["date"].items()
        }
        trigger_index = _strict_nonnegative_int(
            event.get("trigger_index"),
            f"holdout detail trigger_index row={row_index}",
        )
        positions: list[int] = []
        for position, (source_date, trade_date, sequence_index) in enumerate(
            zip(
                lineage["source_dates"],
                lineage["trade_dates"],
                lineage["sequence_indices"],
            )
        ):
            if (
                date_index.get(trade_date) == sequence_index
                and source_date <= trade_date
                and sequence_index <= trigger_index
            ):
                positions.append(position)
        if not positions:
            raise RuntimeError(
                f"revenue readiness detail has no PIT source known by trigger: {episode_key}"
            )
        position = positions[-1]
        expected = {
            "source_asof_date": lineage["source_dates"][position],
            "source_asof_trade_date": lineage["trade_dates"][position],
            "source_asof_revenue_period": lineage["periods"][position],
            "source_asof_row_canonical_sha256": lineage["source_hashes"][position],
            "source_asof_canonical_source_table_date": lineage["canonical_dates"][position],
            "source_asof_sequence_index": lineage["sequence_indices"][position],
            "source_to_trigger_trading_days": (
                trigger_index - lineage["sequence_indices"][position]
            ),
            "future_qualifying_update_ignored_count": (
                len(lineage["periods"]) - position - 1
            ),
        }
        integer_fields = {
            "source_asof_sequence_index",
            "source_to_trigger_trading_days",
            "future_qualifying_update_ignored_count",
        }
        mismatches: list[str] = []
        for field_name, expected_value in expected.items():
            observed_value: str | int
            if field_name in integer_fields:
                observed_value = _strict_nonnegative_int(
                    event.get(field_name),
                    f"holdout detail {field_name} row={row_index}",
                )
            else:
                observed_value = safe_str(event.get(field_name))
            if observed_value != expected_value:
                mismatches.append(field_name)
        if mismatches:
            raise RuntimeError(
                "revenue readiness detail source-asof drift from committed replay "
                f"source: {episode_key}/{mismatches}"
            )


def _validate_selected_v2_manifest(
    source_manifest: pd.DataFrame,
    *,
    diagnostics: list[str] | None = None,
) -> None:
    if len(source_manifest) != 1:
        raise RuntimeError("forward holdout v2 selected manifest must have one row")
    row = source_manifest.iloc[0]
    expected = {
        "artifact_id": SOURCE_PROJECTION_ARTIFACT_ID,
        "artifact_version": SOURCE_PROJECTION_ARTIFACT_VERSION,
        "projection_version": SOURCE_PROJECTION_ARTIFACT_VERSION,
        "cutoff_date": TRAINING_CUTOFF_DATE,
        "projected_episode_row_count": str(PROJECTED_EPISODE_ROW_COUNT),
        "projected_episode_semantic_sha256": PROJECTED_EPISODE_SEMANTIC_SHA256,
        "candidate_status": "generated_pending_supersede_approval",
    }
    for field_name, expected_value in expected.items():
        if safe_str(row.get(field_name)) != expected_value:
            raise RuntimeError(
                f"forward holdout v2 selected manifest drift: {field_name}"
            )
    observed_semantic_sha = _projection_manifest_promotion_semantic_sha256(
        source_manifest
    )
    if observed_semantic_sha != SELECTED_V2_MANIFEST_PROMOTION_SEMANTIC_SHA256:
        raise RuntimeError(
            "forward holdout v2 selected manifest promotion semantic SHA-256 drift: "
            f"expected={SELECTED_V2_MANIFEST_PROMOTION_SEMANTIC_SHA256} "
            f"observed={observed_semantic_sha}"
        )
    observed_legacy_sha = _canonical_frame_sha256(source_manifest)
    if (
        observed_legacy_sha != SELECTED_V2_MANIFEST_CANONICAL_SHA256
        and diagnostics is not None
    ):
        diagnostics.append(
            "selected v2 source manifest legacy raw/envelope SHA differs; "
            "promotion semantic SHA remains the hard gate"
        )


def _required_columns(
    frame: pd.DataFrame,
    required: set[str],
    source_name: str,
) -> None:
    if frame.empty and not len(frame.columns):
        raise RuntimeError(
            f"missing required revenue readiness source: {source_name}"
        )
    missing = sorted(required - set(frame.columns))
    if missing:
        raise RuntimeError(
            f"revenue readiness source {source_name} missing columns: {missing}"
        )


def _strict_nonnegative_int(value: Any, field_name: str) -> int:
    text = safe_str(value)
    if not text.isdigit():
        raise RuntimeError(
            f"revenue readiness {field_name} must be a non-negative integer, "
            f"got {text!r}"
        )
    return int(text)


def _strict_bool(value: Any, expected: bool, field_name: str) -> None:
    text = safe_str(value).lower()
    expected_text = "true" if expected else "false"
    if text != expected_text:
        raise RuntimeError(
            f"revenue readiness {field_name} must be {expected_text!r}, got {text!r}"
        )


def _require_sha(value: Any, field_name: str, *, expected: str | None = None) -> str:
    text = safe_str(value)
    if not SHA256_RE.fullmatch(text):
        raise RuntimeError(
            f"revenue readiness {field_name} must be a canonical lowercase SHA-256"
        )
    if expected is not None and text != expected:
        raise RuntimeError(
            f"revenue readiness {field_name} drift: expected={expected} observed={text}"
        )
    return text


def _strict_date(value: Any, field_name: str) -> str:
    text = safe_str(value)
    if not re.fullmatch(r"[0-9]{8}", text):
        raise RuntimeError(
            f"revenue readiness {field_name} must be YYYYMMDD, got {text!r}"
        )
    return text


def _bool_series(frame: pd.DataFrame, column: str) -> pd.Series:
    values: list[bool] = []
    for row_index, value in frame[column].items():
        text = safe_str(value).lower()
        if text not in {"true", "false"}:
            raise RuntimeError(
                f"revenue readiness {column} row={row_index} must be canonical bool"
            )
        values.append(text == "true")
    return pd.Series(values, index=frame.index, dtype=bool)


def _variant_membership(detail: pd.DataFrame, variant_id: str) -> pd.Series:
    column = VARIANT_MEMBERSHIP_COLUMNS.get(variant_id)
    if column is None:
        raise RuntimeError(
            f"revenue readiness unknown holdout variant membership: {variant_id}"
        )
    if column not in detail.columns:
        raise RuntimeError(
            f"revenue readiness holdout detail missing membership column: {column}"
        )
    return _bool_series(detail, column)


def _validate_disabled_frame(
    frame: pd.DataFrame,
    *,
    source_name: str,
    extra_false_fields: tuple[str, ...] = (),
) -> None:
    if "research_only" not in frame.columns:
        raise RuntimeError(f"revenue readiness {source_name} missing research_only")
    if not _bool_series(frame, "research_only").all():
        raise RuntimeError(f"revenue readiness {source_name} must remain research-only")
    for field_name in (*HOLDOUT_FALSE_FIELDS, *extra_false_fields):
        if field_name not in frame.columns:
            raise RuntimeError(
                f"revenue readiness {source_name} missing disabled flag {field_name}"
            )
        if _bool_series(frame, field_name).any():
            raise RuntimeError(
                f"revenue readiness {source_name} {field_name} must remain false"
            )


def _strict_finite_number(value: Any, field_name: str) -> float:
    text = safe_str(value)
    try:
        number = float(text)
    except (TypeError, ValueError) as exc:
        raise RuntimeError(
            f"revenue readiness {field_name} must be a finite number"
        ) from exc
    if not math.isfinite(number):
        raise RuntimeError(
            f"revenue readiness {field_name} must be a finite number"
        )
    return number


def _require_number_close(
    value: Any,
    expected: float,
    field_name: str,
    *,
    tolerance: float,
) -> None:
    observed = _strict_finite_number(value, field_name)
    if not math.isclose(observed, expected, rel_tol=0.0, abs_tol=tolerance):
        raise RuntimeError(
            f"revenue readiness {field_name} disagrees with registered price input: "
            f"expected={expected} observed={observed}"
        )


def _parse_stock_sha_set(
    manifest_row: pd.Series,
    *,
    sha_set_field: str,
    stock_count_field: str,
    row_count_field: str,
    label: str,
) -> dict[str, str]:
    text = safe_str(manifest_row.get(sha_set_field))
    if not text:
        raise RuntimeError(
            f"revenue readiness holdout {sha_set_field} is empty"
        )
    result: dict[str, str] = {}
    ordered_ids: list[str] = []
    for token in text.split("|"):
        stock_id, separator, digest = token.partition(":")
        stock_id = _stock_id(stock_id)
        if not separator or not re.fullmatch(r"[0-9A-Za-z]{1,12}", stock_id):
            raise RuntimeError(
                f"revenue readiness holdout malformed {label} token"
            )
        _require_sha(digest, f"holdout.{label}/{stock_id}")
        if digest == "0" * 64:
            raise RuntimeError(
                f"revenue readiness holdout {label} contains a "
                f"placeholder SHA-256: {stock_id}"
            )
        if stock_id in result:
            raise RuntimeError(
                f"revenue readiness holdout duplicate {label}: {stock_id}"
            )
        result[stock_id] = digest
        ordered_ids.append(stock_id)
    if ordered_ids != sorted(ordered_ids):
        raise RuntimeError(
            f"revenue readiness holdout {label} is not canonical sorted"
        )
    expected_stock_count = _strict_nonnegative_int(
        manifest_row.get(stock_count_field),
        f"holdout.{stock_count_field}",
    )
    if expected_stock_count != len(result):
        raise RuntimeError(
            f"revenue readiness holdout {label} count drift: "
            f"manifest={expected_stock_count} parsed={len(result)}"
        )
    if _strict_nonnegative_int(
        manifest_row.get(row_count_field),
        f"holdout.{row_count_field}",
    ) <= 0:
        raise RuntimeError(
            f"revenue readiness holdout {row_count_field} must be positive"
        )
    return result


def _parse_price_stock_sha_set(manifest_row: pd.Series) -> dict[str, str]:
    """Parse the legacy prepared-frame lineage for diagnostics and old fixtures."""

    return _parse_stock_sha_set(
        manifest_row,
        sha_set_field="price_input_stock_canonical_sha256s",
        stock_count_field="price_input_stock_count",
        row_count_field="price_input_row_count",
        label="legacy per-stock prepared-price lineage",
    )


def _parse_price_semantic_projection_stock_sha_set(
    manifest_row: pd.Series,
) -> dict[str, str]:
    return _parse_stock_sha_set(
        manifest_row,
        sha_set_field="price_semantic_projection_stock_canonical_sha256s",
        stock_count_field="price_semantic_projection_stock_count",
        row_count_field="price_semantic_projection_row_count",
        label="per-stock canonical raw-price projection lineage",
    )


def _exact_replay_child_bootstrap_source(head_sha: str, tree_sha: str) -> str:
    for field_name, object_id in (
        ("head_sha", head_sha),
        ("tree_sha", tree_sha),
    ):
        if not re.fullmatch(r"(?:[0-9a-f]{40}|[0-9a-f]{64})", object_id):
            raise RuntimeError(
                "revenue readiness exact_replay."
                f"{field_name} must be a canonical Git object id"
            )
    return (
        _EXACT_REPLAY_CHILD_BOOTSTRAP_TEMPLATE.replace(
            "__EXPECTED_COMMIT_SHA__", json.dumps(head_sha)
        ).replace("__EXPECTED_TREE_SHA__", json.dumps(tree_sha))
    )


def _exact_replay_child_env() -> dict[str, str]:
    child_env = dict(os.environ)
    forbidden_python_names = {
        "PYTHONHOME",
        "PYTHONINSPECT",
        "PYTHONPATH",
        "PYTHONSTARTUP",
        "PYTHONUSERBASE",
    }
    for name in tuple(child_env):
        upper_name = name.upper()
        if upper_name in forbidden_python_names or upper_name.startswith("GIT_"):
            child_env.pop(name, None)
    child_env.update(
        {
            "PYTHONDONTWRITEBYTECODE": "1",
            "PYTHONNOUSERSITE": "1",
            "PYTHONWARNINGS": "ignore",
            "GIT_OPTIONAL_LOCKS": "0",
            "GIT_NO_REPLACE_OBJECTS": "1",
            "GIT_CONFIG_NOSYSTEM": "1",
            "GIT_CONFIG_GLOBAL": os.devnull,
            "GIT_CONFIG_COUNT": "1",
            "GIT_CONFIG_KEY_0": "core.fsmonitor",
            "GIT_CONFIG_VALUE_0": "false",
            "NoDefaultCurrentDirectoryInExePath": "1",
        }
    )
    return child_env


def _combined_exact_replay_error(
    primary_error: str | None,
    cleanup_errors: list[str],
) -> RuntimeError | None:
    if primary_error is None and not cleanup_errors:
        return None
    if primary_error is None:
        return RuntimeError(
            "exact revenue replay cleanup failed: " + " | ".join(cleanup_errors)
        )
    if cleanup_errors:
        primary_error += "; cleanup failures: " + " | ".join(cleanup_errors)
    return RuntimeError(primary_error)


def _run_exact_replay_child(
    repo: Path,
    head_sha: str,
    child_source: str,
    *,
    timeout_seconds: int = EXACT_REPLAY_TIMEOUT_SECONDS,
    run_command: Callable[..., subprocess.CompletedProcess[str]] | None = None,
    make_temp_dir: Callable[..., str] | None = None,
) -> subprocess.CompletedProcess[str]:
    """Run one isolated child and preserve primary failures through cleanup."""

    runner = subprocess.run if run_command is None else run_command
    temp_maker = tempfile.mkdtemp if make_temp_dir is None else make_temp_dir
    temp_parent = Path(
        temp_maker(prefix="revenue-readiness-exact-replay-")
    ).resolve()
    clean_repo = temp_parent / "repo"
    primary_error: str | None = None
    cleanup_errors: list[str] = []
    child_result: subprocess.CompletedProcess[str] | None = None
    worktree_added = False

    try:
        add_result = runner(
            [
                "git",
                "-c",
                "core.autocrlf=false",
                "--no-replace-objects",
                "worktree",
                "add",
                "--detach",
                str(clean_repo),
                head_sha,
            ],
            cwd=repo,
            check=False,
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
        if add_result.returncode:
            detail = add_result.stderr.strip() or add_result.stdout.strip()
            primary_error = (
                "cannot create exact committed replay worktree: "
                + (detail or "git worktree add failed")
            )
        else:
            worktree_added = True
            try:
                child_result = runner(
                    [sys.executable, "-I", "-B", "-c", child_source],
                    cwd=clean_repo,
                    check=False,
                    text=True,
                    env=_exact_replay_child_env(),
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                    timeout=timeout_seconds,
                )
            except subprocess.TimeoutExpired:
                primary_error = (
                    "exact revenue price-lineage replay timed out after "
                    f"{timeout_seconds} seconds"
                )
            except OSError as exc:
                primary_error = (
                    "cannot launch exact revenue price-lineage replay child: "
                    f"{exc}"
                )
            else:
                if child_result.returncode:
                    detail = child_result.stderr.strip() or child_result.stdout.strip()
                    primary_error = (
                        "exact revenue price-lineage replay failed: " + detail[-4000:]
                    )

            status_result = runner(
                [
                    "git",
                    "--no-replace-objects",
                    "status",
                    "--porcelain=v1",
                    "--untracked-files=all",
                ],
                cwd=clean_repo,
                check=False,
                text=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
            )
            if status_result.returncode:
                detail = status_result.stderr.strip() or status_result.stdout.strip()
                security_error = (
                    "post-child exact replay worktree clean check failed: "
                    + (detail or "git status failed")
                )
                primary_error = (
                    security_error
                    if primary_error is None
                    else primary_error + "; " + security_error
                )
            elif status_result.stdout.strip():
                security_error = (
                    "exact revenue replay child mutated its clean worktree: "
                    + status_result.stdout.strip().replace("\n", "; ")
                )
                primary_error = (
                    security_error
                    if primary_error is None
                    else primary_error + "; " + security_error
                )
    except OSError as exc:
        if primary_error is None:
            primary_error = f"exact revenue replay worktree transaction failed: {exc}"
        else:
            primary_error += f"; worktree transaction failed: {exc}"
    finally:
        if worktree_added or clean_repo.exists():
            try:
                remove_result = runner(
                    [
                        "git",
                        "--no-replace-objects",
                        "worktree",
                        "remove",
                        "--force",
                        str(clean_repo),
                    ],
                    cwd=repo,
                    check=False,
                    text=True,
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE,
                )
            except OSError as exc:
                cleanup_errors.append(
                    f"cannot remove exact committed replay worktree: {exc}"
                )
            else:
                if remove_result.returncode:
                    detail = remove_result.stderr.strip() or remove_result.stdout.strip()
                    cleanup_errors.append(
                        "cannot remove exact committed replay worktree: "
                        + (detail or "git worktree remove failed")
                    )
        if clean_repo.exists():
            try:
                clean_repo.rmdir()
            except OSError as exc:
                cleanup_errors.append(
                    f"exact replay worktree path remains after cleanup: {exc}"
                )
        try:
            temp_parent.rmdir()
        except OSError as exc:
            cleanup_errors.append(
                f"cannot remove exact replay temporary directory: {exc}"
            )

    combined_error = _combined_exact_replay_error(primary_error, cleanup_errors)
    if combined_error is not None:
        raise combined_error
    if child_result is None:
        raise RuntimeError("exact revenue replay child returned no process result")
    return child_result


def _parse_exact_replay_payload(
    result: subprocess.CompletedProcess[str],
    *,
    head_sha: str,
    tree_sha: str,
    runtime_fingerprint: dict[str, str],
) -> dict[str, Any]:
    stdout_lines = [line for line in result.stdout.splitlines() if line.strip()]
    if len(stdout_lines) != 1 or not stdout_lines[0].startswith(
        EXACT_REPLAY_SENTINEL
    ):
        raise RuntimeError("exact revenue price-lineage replay stdout protocol drift")

    def unique_json_object(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
        parsed: dict[str, Any] = {}
        for key, value in pairs:
            if key in parsed:
                raise ValueError(f"duplicate JSON key: {key}")
            parsed[key] = value
        return parsed

    try:
        payload = json.loads(
            stdout_lines[0][len(EXACT_REPLAY_SENTINEL) :],
            object_pairs_hook=unique_json_object,
        )
    except (json.JSONDecodeError, ValueError) as exc:
        raise RuntimeError(
            "exact revenue price-lineage replay returned malformed JSON"
        ) from exc
    if not isinstance(payload, dict):
        raise RuntimeError("exact revenue price-lineage replay payload must be an object")
    expected_payload_keys = {
        "protocol_version",
        "commit_sha",
        "tree_sha",
        "runtime_fingerprint",
        "capture_id",
        "data_contract_version",
        "data_contract_sha256",
        "source_detail_promotion_semantic_sha256",
        "price_semantic_projection_version",
        "price_semantic_projection_schema_sha256",
        "price_semantic_projection_columns",
        "price_semantic_projection_decimal_scale",
        "price_semantic_projection_stock_canonical_sha256s",
        "price_semantic_projection_canonical_sha256",
        "price_semantic_projection_stock_count",
        "price_semantic_projection_row_count",
        "price_semantic_projection_role",
        "price_semantic_projection_migration_id",
        "price_semantic_projection_authorization_reference",
        "observed_through_date",
        "expected_manifest_canonical_sha256",
        "expected_detail_canonical_sha256",
        "expected_summary_canonical_sha256",
        "frame_attestations",
        "replay_child_mode",
        "replay_child_modules",
    }
    if set(payload) != expected_payload_keys:
        raise RuntimeError("exact revenue replay top-level payload schema drift")
    if payload.get("protocol_version") != EXACT_REPLAY_PROTOCOL_VERSION:
        raise RuntimeError("exact revenue replay protocol version drift")
    if payload.get("commit_sha") != head_sha or payload.get("tree_sha") != tree_sha:
        raise RuntimeError("exact revenue replay committed identity drift")
    if payload.get("runtime_fingerprint") != runtime_fingerprint:
        raise RuntimeError("exact revenue replay runtime fingerprint drift")
    _require_sha(payload.get("capture_id"), "exact_holdout.capture_id")
    if payload.get("data_contract_version") != DATA_CONTRACT_VERSION:
        raise RuntimeError("exact revenue replay data contract version drift")
    _require_sha(
        payload.get("data_contract_sha256"),
        "exact_holdout.data_contract_sha256",
        expected=DATA_CONTRACT_SHA256,
    )
    _require_sha(
        payload.get("source_detail_promotion_semantic_sha256"),
        "exact_holdout.source_detail_promotion_semantic_sha256",
    )
    _require_sha(
        payload.get("price_semantic_projection_schema_sha256"),
        "exact_holdout.price_semantic_projection_schema_sha256",
        expected=PRICE_SEMANTIC_PROJECTION_SCHEMA_SHA256,
    )
    exact_projection_sha = _require_sha(
        payload.get("price_semantic_projection_canonical_sha256"),
        "exact_holdout.price_semantic_projection_canonical_sha256",
    )
    if exact_projection_sha == "0" * 64:
        raise RuntimeError(
            "exact revenue replay canonical price-projection SHA is a placeholder"
        )
    exact_projection_fields = {
        "price_semantic_projection_version": PRICE_SEMANTIC_PROJECTION_VERSION,
        "price_semantic_projection_columns": "|".join(
            PRICE_SEMANTIC_PROJECTION_COLUMNS
        ),
        "price_semantic_projection_decimal_scale": (
            PRICE_SEMANTIC_PROJECTION_DECIMAL_SCALE
        ),
        "price_semantic_projection_role": PRICE_SEMANTIC_PROJECTION_ROLE,
        "price_semantic_projection_migration_id": (
            PRICE_SEMANTIC_PROJECTION_MIGRATION_ID
        ),
        "price_semantic_projection_authorization_reference": (
            PRICE_SEMANTIC_PROJECTION_AUTHORIZATION_REFERENCE
        ),
    }
    for field_name, expected in exact_projection_fields.items():
        if payload.get(field_name) != expected:
            raise RuntimeError(
                f"exact revenue replay {field_name} drift"
            )
    frame_attestations = payload.get("frame_attestations")
    if not isinstance(frame_attestations, dict) or set(frame_attestations) != {
        "manifest",
        "detail",
        "summary",
        "comparison",
        "anomaly",
    }:
        raise RuntimeError("exact revenue replay five-frame attestation drift")
    for frame_name, frame_attestation in frame_attestations.items():
        if not isinstance(frame_attestation, dict) or set(frame_attestation) != {
            "canonical_sha256",
            "row_count",
            "column_count",
        }:
            raise RuntimeError(
                f"exact revenue replay frame attestation schema drift: {frame_name}"
            )
        _require_sha(
            frame_attestation.get("canonical_sha256"),
            f"exact_holdout.frame_attestation/{frame_name}",
        )
        if _strict_nonnegative_int(
            frame_attestation.get("column_count"),
            f"exact_holdout.frame_column_count/{frame_name}",
        ) <= 0:
            raise RuntimeError(f"exact revenue replay frame has no columns: {frame_name}")
        _strict_nonnegative_int(
            frame_attestation.get("row_count"),
            f"exact_holdout.frame_row_count/{frame_name}",
        )
    for frame_name in ("manifest", "detail", "summary"):
        if payload.get(
            f"expected_{frame_name}_canonical_sha256"
        ) != frame_attestations[frame_name]["canonical_sha256"]:
            raise RuntimeError(
                "exact revenue replay top-level/frame attestation drift: "
                f"{frame_name}"
            )
    if payload.get("replay_child_mode") != EXACT_REPLAY_CHILD_MODE or tuple(
        payload.get("replay_child_modules", [])
    ) != EXACT_REPLAY_CHILD_MODULES:
        raise RuntimeError("exact revenue replay child dependency identity drift")
    return payload


def _recompute_exact_registered_price_lineage(
    repo_root: Path | str,
) -> dict[str, Any]:
    """Replay the exact producer/independent-validator price canonicalization.

    The parent writer keeps the same-model research modules outside its module
    graph.  A trusted same-model child process materializes the registered v2
    bundle, requires producer/independent-validator full-frame parity, and runs
    the official persisted-frame replay gate without writing any artifact.
    """

    repo = Path(repo_root).resolve()
    head_result = subprocess.run(
        ["git", "--no-replace-objects", "rev-parse", "HEAD"],
        cwd=repo,
        check=False,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    if head_result.returncode:
        raise RuntimeError(
            "cannot resolve HEAD for exact revenue price-lineage replay: "
            + head_result.stderr.strip()
        )
    head_sha = head_result.stdout.strip()
    tree_result = subprocess.run(
        ["git", "--no-replace-objects", "rev-parse", "HEAD^{tree}"],
        cwd=repo,
        check=False,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    if tree_result.returncode:
        raise RuntimeError(
            "cannot resolve HEAD tree for exact revenue replay: "
            + tree_result.stderr.strip()
        )
    tree_sha = tree_result.stdout.strip()
    runtime_fingerprint = {
        "python": sys.version.split()[0],
        "pandas": pd.__version__,
        "numpy": importlib.metadata.version("numpy"),
    }
    cache_key = (
        str(repo),
        EXACT_REPLAY_PROTOCOL_VERSION,
        head_sha,
        tree_sha,
        runtime_fingerprint["python"],
        runtime_fingerprint["pandas"],
        runtime_fingerprint["numpy"],
    )
    cached = _EXACT_PRICE_LINEAGE_CACHE.get(cache_key)
    if cached is not None:
        return cached

    child_source = _exact_replay_child_bootstrap_source(head_sha, tree_sha) + r'''
import json
import subprocess
from pathlib import Path

import pandas as pd

sys.path.insert(0, str(Path.cwd() / "scripts"))

import revenue_unreacted_range_forward_holdout_v2 as producer_v2
import validate_revenue_unreacted_range_forward_holdout_v2 as validator_v2

RAW_MONTHLY_REVENUE_PROVENANCE_COLUMN = "monthly_revenue_history_blob_sha256"
SOURCE_DETAIL_LEGACY_ENVELOPE_COLUMN = "source_detail_canonical_sha256"
CAPTURE_LEGACY_ENVELOPE_COLUMN = "capture_id"
EVENT_LEGACY_ENVELOPE_COLUMN = "event_row_canonical_sha256"
LEGACY_ENVELOPE_COLUMNS = (
    SOURCE_DETAIL_LEGACY_ENVELOPE_COLUMN,
    CAPTURE_LEGACY_ENVELOPE_COLUMN,
)
LEGACY_PRICE_PROVENANCE_COLUMNS = (
    "price_input_stock_count",
    "price_input_row_count",
    "price_input_stock_canonical_sha256s",
    "price_input_canonical_sha256",
)
PROMOTION_SEMANTIC_FRAME_EXCLUSIONS = {
    "manifest": (
        "generated_at",
        RAW_MONTHLY_REVENUE_PROVENANCE_COLUMN,
        *LEGACY_ENVELOPE_COLUMNS,
        *LEGACY_PRICE_PROVENANCE_COLUMNS,
    ),
    "detail": (
        "generated_at",
        RAW_MONTHLY_REVENUE_PROVENANCE_COLUMN,
        *LEGACY_ENVELOPE_COLUMNS,
        EVENT_LEGACY_ENVELOPE_COLUMN,
        *LEGACY_PRICE_PROVENANCE_COLUMNS,
    ),
    "summary": ("generated_at", CAPTURE_LEGACY_ENVELOPE_COLUMN),
    "comparison": ("generated_at", CAPTURE_LEGACY_ENVELOPE_COLUMN),
    "anomaly": ("generated_at", CAPTURE_LEGACY_ENVELOPE_COLUMN),
}


def is_transport_provenance_column(column):
    normalized = str(column).strip().lower()
    return (
        normalized == "generated_at"
        or "raw_file_sha" in normalized
        or "blob_sha256" in normalized
        or "byte_sha256" in normalized
        or "bytes_sha256" in normalized
        or "crlf" in normalized
        or "line_ending" in normalized
    )


def promotion_semantic_source_sha256(frame):
    semantic = frame.drop(
        columns=[
            column
            for column in frame.columns
            if is_transport_provenance_column(column)
        ],
        errors="ignore",
    )
    return validator_v2.validator._frame_sha(semantic)


def promotion_semantic_frame_sha256(frame, frame_name):
    if frame_name not in PROMOTION_SEMANTIC_FRAME_EXCLUSIONS:
        raise RuntimeError(
            "unsupported revenue promotion semantic frame: " + frame_name
        )
    excluded = set(PROMOTION_SEMANTIC_FRAME_EXCLUSIONS[frame_name])
    excluded.update(
        column
        for column in frame.columns
        if is_transport_provenance_column(column)
    )
    semantic = frame.drop(
        columns=list(excluded),
        errors="ignore",
    )
    return validator_v2.validator._frame_sha(semantic)


commit_sha = EXPECTED_COMMIT_SHA
tree_sha = EXPECTED_TREE_SHA
observed_commit_sha = subprocess.run(
    ["git", "--no-replace-objects", "rev-parse", "HEAD^{commit}"],
    check=True,
    text=True,
    stdout=subprocess.PIPE,
).stdout.strip()
observed_tree_sha = subprocess.run(
    ["git", "--no-replace-objects", "rev-parse", "HEAD^{tree}"],
    check=True,
    text=True,
    stdout=subprocess.PIPE,
).stdout.strip()
if observed_commit_sha != commit_sha or observed_tree_sha != tree_sha:
    raise RuntimeError("exact revenue replay child no-replace identity drift")
producer_v2.validate_v1_exact17_freeze(
    root=Path.cwd(),
    git_ref=commit_sha,
)

try:
    with producer_v2.engine_v2_context():
        source_detail, daily_by_stock, source_manifest = (
            producer_v2.engine._materialize_current_forward_holdout_inputs()
        )
        producer_v2.validate_selected_v2_manifest(source_manifest)
        frames = producer_v2.engine.build_forward_holdout(
            source_detail,
            daily_by_stock,
            source_manifest=source_manifest,
            generated_at="exact-readiness-replay",
        )

    errors = validator_v2.validate_frames(
        *frames,
        source_detail=source_detail,
        daily_by_stock=daily_by_stock,
        source_manifest=source_manifest,
    )
    if errors:
        raise RuntimeError(
            "official v2 forward-holdout replay failed: " + " | ".join(errors[:20])
        )

    frame_names = ("manifest", "detail", "summary", "comparison", "anomaly")
    persisted_frames = [
        pd.read_csv(
            validator_v2.DEFAULT_PATHS[name],
            dtype=str,
            keep_default_na=False,
        )
        for name in frame_names
    ]
    persisted_source_detail = pd.read_csv(
        producer_v2.REPLAY_SOURCE_OUTPUT_RELATIVE_PATHS["replay_source_latest"],
        dtype=str,
        keep_default_na=False,
    )
    if promotion_semantic_source_sha256(
        persisted_source_detail
    ) != promotion_semantic_source_sha256(source_detail):
        raise RuntimeError(
            "persisted v2 forward-holdout source semantic drift from exact build"
        )
    for name, exact_frame, persisted_frame in zip(
        frame_names, frames, persisted_frames
    ):
        if promotion_semantic_frame_sha256(
            persisted_frame, name
        ) != promotion_semantic_frame_sha256(exact_frame, name):
            raise RuntimeError(
                "persisted v2 forward-holdout promotion semantic frame drift "
                "from exact build: " + name
            )
finally:
    producer_v2.validate_v1_exact17_freeze(
        root=Path.cwd(),
        git_ref=commit_sha,
    )

manifest_row = frames[0].iloc[0]
aggregate_sha = str(manifest_row["price_semantic_projection_canonical_sha256"])
sha_set_text = str(
    manifest_row["price_semantic_projection_stock_canonical_sha256s"]
)
stock_count = int(manifest_row["price_semantic_projection_stock_count"])
row_count = int(manifest_row["price_semantic_projection_row_count"])
per_stock_sha = {}
for token in sha_set_text.split("|"):
    stock_id, separator, digest = token.partition(":")
    if not separator or stock_id in per_stock_sha:
        raise RuntimeError("independent validator returned malformed price lineage")
    per_stock_sha[stock_id] = digest
observed_through_date = str(manifest_row["observed_through_date"])
frame_attestations = {
    name: {
        "canonical_sha256": promotion_semantic_frame_sha256(
            frame, name
        ),
        "row_count": len(frame),
        "column_count": len(frame.columns),
    }
    for name, frame in zip(frame_names, frames)
}
print(
    "REVENUE_EXACT_PRICE_LINEAGE_JSON="
    + json.dumps(
        {
            "protocol_version": "revenue_readiness_exact_replay_v3_20260829",
            "commit_sha": commit_sha,
            "tree_sha": tree_sha,
            "runtime_fingerprint": {
                "python": sys.version.split()[0],
                "pandas": pd.__version__,
                "numpy": __import__("numpy").__version__,
            },
            "capture_id": str(manifest_row["capture_id"]),
            "data_contract_version": str(manifest_row["data_contract_version"]),
            "data_contract_sha256": str(manifest_row["data_contract_sha256"]),
            "source_detail_promotion_semantic_sha256": (
                promotion_semantic_source_sha256(source_detail)
            ),
            "price_semantic_projection_version": str(
                manifest_row["price_semantic_projection_version"]
            ),
            "price_semantic_projection_schema_sha256": str(
                manifest_row["price_semantic_projection_schema_sha256"]
            ),
            "price_semantic_projection_columns": str(
                manifest_row["price_semantic_projection_columns"]
            ),
            "price_semantic_projection_decimal_scale": int(
                manifest_row["price_semantic_projection_decimal_scale"]
            ),
            "price_semantic_projection_stock_canonical_sha256s": per_stock_sha,
            "price_semantic_projection_canonical_sha256": aggregate_sha,
            "price_semantic_projection_stock_count": stock_count,
            "price_semantic_projection_row_count": row_count,
            "price_semantic_projection_role": str(
                manifest_row["price_semantic_projection_role"]
            ),
            "price_semantic_projection_migration_id": str(
                manifest_row["price_semantic_projection_migration_id"]
            ),
            "price_semantic_projection_authorization_reference": str(
                manifest_row["price_semantic_projection_authorization_reference"]
            ),
            "observed_through_date": observed_through_date,
            "expected_manifest_canonical_sha256": (
                promotion_semantic_frame_sha256(frames[0], "manifest")
            ),
            "expected_detail_canonical_sha256": (
                promotion_semantic_frame_sha256(frames[1], "detail")
            ),
            "expected_summary_canonical_sha256": (
                promotion_semantic_frame_sha256(frames[2], "summary")
            ),
            "frame_attestations": frame_attestations,
            "replay_child_mode": "trusted_same_model_in_memory_canonical_replay",
            "replay_child_modules": [
                "revenue_unreacted_range_forward_holdout_v2",
                "validate_revenue_unreacted_range_forward_holdout_v2",
            ],
        },
        separators=(",", ":"),
        sort_keys=True,
    )
)
'''
    result = _run_exact_replay_child(repo, head_sha, child_source)
    payload = _parse_exact_replay_payload(
        result,
        head_sha=head_sha,
        tree_sha=tree_sha,
        runtime_fingerprint=runtime_fingerprint,
    )
    _EXACT_PRICE_LINEAGE_CACHE[cache_key] = payload
    return payload


def _validate_exact_registered_price_lineage(
    repo_root: Path | str,
    manifest_row: pd.Series,
    *,
    manifest: pd.DataFrame,
    detail: pd.DataFrame,
    summary: pd.DataFrame,
    replay_source: pd.DataFrame,
    observed_through: str,
    per_stock_manifest_sha: dict[str, str],
) -> None:
    exact = _recompute_exact_registered_price_lineage(repo_root)
    expected_source_semantic_sha = _require_sha(
        exact.get("source_detail_promotion_semantic_sha256"),
        "exact_holdout.source_detail_promotion_semantic_sha256",
    )
    observed_source_semantic_sha = _promotion_semantic_source_sha256(replay_source)
    if observed_source_semantic_sha != expected_source_semantic_sha:
        raise RuntimeError(
            "revenue readiness holdout replay source promotion semantic drift "
            "from independent exact replay"
        )
    for label, frame in (
        ("manifest", manifest),
        ("detail", detail),
        ("summary", summary),
    ):
        expected_frame_sha = _require_sha(
            exact.get(f"expected_{label}_canonical_sha256"),
            f"exact_holdout.expected_{label}_canonical_sha256",
        )
        observed_frame_sha = _promotion_semantic_frame_sha256(
            frame,
            frame_name=label,
        )
        if observed_frame_sha != expected_frame_sha:
            raise RuntimeError(
                "revenue readiness holdout candidate "
                f"{label} promotion semantic drift from independent exact replay"
            )
    for field_name, expected in {
        "data_contract_version": DATA_CONTRACT_VERSION,
        "data_contract_sha256": DATA_CONTRACT_SHA256,
        "price_semantic_projection_version": PRICE_SEMANTIC_PROJECTION_VERSION,
        "price_semantic_projection_schema_sha256": (
            PRICE_SEMANTIC_PROJECTION_SCHEMA_SHA256
        ),
        "price_semantic_projection_columns": "|".join(
            PRICE_SEMANTIC_PROJECTION_COLUMNS
        ),
        "price_semantic_projection_decimal_scale": str(
            PRICE_SEMANTIC_PROJECTION_DECIMAL_SCALE
        ),
        "price_semantic_projection_role": PRICE_SEMANTIC_PROJECTION_ROLE,
        "price_semantic_projection_migration_id": (
            PRICE_SEMANTIC_PROJECTION_MIGRATION_ID
        ),
        "price_semantic_projection_authorization_reference": (
            PRICE_SEMANTIC_PROJECTION_AUTHORIZATION_REFERENCE
        ),
    }.items():
        if safe_str(manifest_row.get(field_name)) != expected:
            raise RuntimeError(
                f"revenue readiness holdout {field_name} drift from canonical contract"
            )
    exact_mapping = exact.get(
        "price_semantic_projection_stock_canonical_sha256s"
    )
    if not isinstance(exact_mapping, dict) or not exact_mapping:
        raise RuntimeError(
            "exact revenue price-lineage replay returned no per-stock digests"
        )
    normalized_exact_mapping: dict[str, str] = {}
    for raw_stock_id, raw_digest in exact_mapping.items():
        stock_id = _stock_id(raw_stock_id)
        if not re.fullmatch(r"[0-9A-Za-z]{1,12}", stock_id):
            raise RuntimeError(
                "exact revenue canonical price-projection replay returned unsafe stock identity"
            )
        digest = _require_sha(
            raw_digest,
            f"exact_holdout.price_semantic_projection_stock_sha/{stock_id}",
        )
        if digest == "0" * 64 or stock_id in normalized_exact_mapping:
            raise RuntimeError(
                "exact revenue canonical price-projection replay returned invalid per-stock lineage"
            )
        normalized_exact_mapping[stock_id] = digest
    if normalized_exact_mapping != per_stock_manifest_sha:
        mismatched = sorted(
            stock_id
            for stock_id in set(normalized_exact_mapping) | set(per_stock_manifest_sha)
            if normalized_exact_mapping.get(stock_id)
            != per_stock_manifest_sha.get(stock_id)
        )
        raise RuntimeError(
            "revenue readiness holdout per-stock canonical raw-price projection "
            "SHA drift from "
            f"exact producer replay: {mismatched[:10]}"
        )
    exact_aggregate_sha = _require_sha(
        exact.get("price_semantic_projection_canonical_sha256"),
        "exact_holdout.price_semantic_projection_canonical_sha256",
    )
    manifest_aggregate_sha = _require_sha(
        manifest_row.get("price_semantic_projection_canonical_sha256"),
        "holdout.price_semantic_projection_canonical_sha256",
    )
    if exact_aggregate_sha != manifest_aggregate_sha:
        raise RuntimeError(
            "revenue readiness holdout canonical raw-price projection SHA drift from "
            "exact producer replay"
        )

    exact_stock_count = _strict_nonnegative_int(
        exact.get("price_semantic_projection_stock_count"),
        "exact_holdout.price_semantic_projection_stock_count",
    )
    manifest_stock_count = _strict_nonnegative_int(
        manifest_row.get("price_semantic_projection_stock_count"),
        "holdout.price_semantic_projection_stock_count",
    )
    if exact_stock_count != len(normalized_exact_mapping):
        raise RuntimeError(
            "exact revenue canonical price-projection stock count disagrees with "
            "per-stock set"
        )
    if exact_stock_count != manifest_stock_count:
        raise RuntimeError(
            "revenue readiness holdout canonical price-projection stock count drift "
            "from exact replay"
        )
    exact_row_count = _strict_nonnegative_int(
        exact.get("price_semantic_projection_row_count"),
        "exact_holdout.price_semantic_projection_row_count",
    )
    manifest_row_count = _strict_nonnegative_int(
        manifest_row.get("price_semantic_projection_row_count"),
        "holdout.price_semantic_projection_row_count",
    )
    if exact_row_count <= 0 or exact_row_count != manifest_row_count:
        raise RuntimeError(
            "revenue readiness holdout canonical price-projection row count drift "
            "from exact replay"
        )
    exact_observed_through = _strict_date(
        exact.get("observed_through_date"),
        "exact_holdout.observed_through_date",
    )
    if exact_observed_through != observed_through:
        raise RuntimeError(
            "revenue readiness holdout observed_through_date drift from exact "
            "registered price replay"
        )


def _normalized_registered_price_frame(
    raw: pd.DataFrame,
    resolutions: pd.DataFrame,
    *,
    stock_id: str,
    observed_through: str,
) -> pd.DataFrame:
    required = {"date", "open", "close"}
    missing = sorted(required - set(raw.columns))
    if missing:
        raise RuntimeError(
            f"registered price input missing columns for {stock_id}: {missing}"
        )
    frame = raw.copy()
    if "stock_id" in frame.columns:
        observed_stock_ids = {
            _stock_id(value) for value in frame["stock_id"] if safe_str(value)
        }
        if observed_stock_ids != {stock_id}:
            raise RuntimeError(
                "registered price input stock identity drift: "
                f"path={stock_id} rows={sorted(observed_stock_ids)}"
            )

    def normalized_date(value: Any) -> str:
        text = "".join(character for character in str(value) if character.isdigit())
        return text[:8] if len(text) >= 8 else ""

    frame["date"] = frame["date"].map(normalized_date)
    if frame["date"].eq("").any():
        raise RuntimeError(
            f"registered price input has invalid trading date for {stock_id}"
        )
    frame = (
        frame.sort_values("date", kind="mergesort")
        .drop_duplicates("date", keep="last")
        .copy()
    )
    frame["open"] = pd.to_numeric(frame["open"], errors="coerce")
    frame["close"] = pd.to_numeric(frame["close"], errors="coerce")
    frame = frame.dropna(subset=["close"])
    frame = frame.loc[frame["date"].le(observed_through)].reset_index(drop=True)
    if frame.empty:
        raise RuntimeError(
            f"registered price input has no rows through {observed_through}: {stock_id}"
        )
    frame["analysis_price_adjustment_factor"] = 1.0
    if not resolutions.empty:
        required_resolution = {
            "stock_id",
            "resume_date",
            "exchange_ratio",
            "root_cause_status",
        }
        missing_resolution = sorted(required_resolution - set(resolutions.columns))
        if missing_resolution:
            raise RuntimeError(
                "registered price resolution input missing columns: "
                f"{missing_resolution}"
            )
        applicable = resolutions.loc[
            resolutions["root_cause_status"]
            .astype(str)
            .eq("verified_non_comparable_raw_price_scale")
        ].copy()
        applicable["stock_id"] = applicable["stock_id"].map(_stock_id)
        applicable = applicable.loc[applicable["stock_id"].eq(stock_id)]
        for resolution_index, resolution in applicable.iterrows():
            resume_date = _strict_date(
                resolution.get("resume_date"),
                f"price resolution resume_date row={resolution_index}",
            )
            ratio = _strict_finite_number(
                resolution.get("exchange_ratio"),
                f"price resolution exchange_ratio row={resolution_index}",
            )
            if ratio <= 0:
                raise RuntimeError(
                    "registered price resolution exchange ratio must be positive"
                )
            frame.loc[
                frame["date"].lt(resume_date),
                "analysis_price_adjustment_factor",
            ] *= 1.0 / ratio
    frame["analysis_open"] = (
        frame["open"] * frame["analysis_price_adjustment_factor"]
    )
    frame["analysis_close"] = (
        frame["close"] * frame["analysis_price_adjustment_factor"]
    )
    if frame["date"].duplicated().any() or not frame["date"].is_monotonic_increasing:
        raise RuntimeError(
            f"registered price input trading dates are not unique and sorted: {stock_id}"
        )
    return frame


def _load_registered_price_frames(
    repo_root: Path | str,
    detail: pd.DataFrame,
    *,
    observed_through: str,
    per_stock_manifest_sha: dict[str, str],
    required_stock_ids: set[str] | None = None,
) -> dict[str, pd.DataFrame]:
    stock_ids = sorted(
        {_stock_id(value) for value in detail.get("stock_id", [])}
        | {_stock_id(value) for value in (required_stock_ids or set())}
    )
    if any(not re.fullmatch(r"[0-9A-Za-z]{1,12}", stock_id) for stock_id in stock_ids):
        raise RuntimeError("revenue readiness holdout detail contains unsafe stock_id")
    missing_lineage = sorted(set(stock_ids) - set(per_stock_manifest_sha))
    if missing_lineage:
        raise RuntimeError(
            "revenue readiness holdout detail stock missing from normalized price "
            f"lineage: {missing_lineage}"
        )
    if not stock_ids:
        return {}
    repo = Path(repo_root).resolve()
    logical_paths = [
        PRICE_RESOLUTION_REL,
        *(f"{PRICE_HISTORY_DIR_REL}/{stock_id}.csv" for stock_id in stock_ids),
    ]
    committed_sources = _bulk_committed_registered_price_sources(
        repo,
        logical_paths,
    )
    resolution_bytes = committed_sources[PRICE_RESOLUTION_REL]
    resolutions = _frame_from_csv_bytes(resolution_bytes, PRICE_RESOLUTION_REL)
    result: dict[str, pd.DataFrame] = {}
    for stock_id in stock_ids:
        logical_path = f"{PRICE_HISTORY_DIR_REL}/{stock_id}.csv"
        price_bytes = committed_sources[logical_path]
        raw = _frame_from_csv_bytes(price_bytes, logical_path)
        result[stock_id] = _normalized_registered_price_frame(
            raw,
            resolutions,
            stock_id=stock_id,
            observed_through=observed_through,
        )
    return result


def _validate_detail_maturity_against_registered_prices(
    detail: pd.DataFrame,
    *,
    observed_through: str,
    registered_prices: dict[str, pd.DataFrame],
    manifest_price_projection_sha: str,
) -> None:
    required = {
        "price_input_canonical_sha256",
        "price_semantic_projection_version",
        "price_semantic_projection_schema_sha256",
        "price_semantic_projection_canonical_sha256",
        "holding_days",
        "holding_session_index_offset",
        "stock_id",
        "trigger_index",
        "trigger_date",
        "trigger_close",
        "confirmation_index",
        "confirmation_date",
        "confirmation_close",
        "entry_index",
        "entry_price_basis",
        "entry_date",
        "entry_price",
        "planned_exit_index",
        "planned_exit_date",
        "exit_index",
        "exit_date",
        "exit_price",
        "exit_price_basis",
        "exit_reason",
        "return_valid",
        "right_censored",
        "realized_return_pct",
        "return_outcome",
        "realized_return_ge20",
        "operation_return_review_candidate_flag",
        "operation_status",
    }
    _required_columns(detail, required, FORWARD_HOLDOUT_V2_DETAIL_REL)
    for row_index, event in detail.iterrows():
        stock_id = _stock_id(event.get("stock_id"))
        frame = registered_prices.get(stock_id)
        if frame is None:
            raise RuntimeError(
                f"revenue readiness missing registered price evidence for {stock_id}"
            )
        if safe_str(event.get("price_semantic_projection_version")) != (
            PRICE_SEMANTIC_PROJECTION_VERSION
        ):
            raise RuntimeError(
                "revenue readiness holdout detail canonical price-projection version "
                f"drift: row={row_index}"
            )
        _require_sha(
            event.get("price_semantic_projection_schema_sha256"),
            f"holdout detail price_semantic_projection_schema_sha256 row={row_index}",
            expected=PRICE_SEMANTIC_PROJECTION_SCHEMA_SHA256,
        )
        if safe_str(event.get("price_semantic_projection_canonical_sha256")) != (
            manifest_price_projection_sha
        ):
            raise RuntimeError(
                "revenue readiness holdout detail is not bound to the manifest "
                f"canonical raw-price projection SHA: row={row_index}"
            )
        if _strict_nonnegative_int(
            event.get("holding_days"), f"holdout detail holding_days row={row_index}"
        ) != HOLDING_DAYS:
            raise RuntimeError("revenue readiness holdout holding_days drift")
        if _strict_nonnegative_int(
            event.get("holding_session_index_offset"),
            f"holdout detail holding_session_index_offset row={row_index}",
        ) != HOLDING_SESSION_INDEX_OFFSET:
            raise RuntimeError(
                "revenue readiness holdout holding-session offset drift"
            )
        trigger_date = _strict_date(
            event.get("trigger_date"),
            f"holdout detail trigger_date row={row_index}",
        )
        trigger_matches = frame.index[frame["date"].eq(trigger_date)].tolist()
        if len(trigger_matches) != 1:
            raise RuntimeError(
                "revenue readiness holdout trigger is absent from registered trading-"
                f"date evidence: {stock_id}/{trigger_date}"
            )
        trigger_index = int(trigger_matches[0])
        confirmation_index = trigger_index + 1
        entry_index = trigger_index + 2
        planned_exit_index = entry_index + HOLDING_SESSION_INDEX_OFFSET
        expected_indices = {
            "trigger_index": trigger_index,
            "confirmation_index": confirmation_index,
            "entry_index": entry_index,
            "planned_exit_index": planned_exit_index,
        }
        for field_name, expected in expected_indices.items():
            observed = _strict_nonnegative_int(
                event.get(field_name),
                f"holdout detail {field_name} row={row_index}",
            )
            if observed != expected:
                raise RuntimeError(
                    "revenue readiness holdout trading-session index drift: "
                    f"{stock_id}/{field_name}/expected={expected}/observed={observed}"
                )
        if confirmation_index >= len(frame):
            raise RuntimeError(
                "revenue readiness holdout event lacks independently observed D+1 "
                f"confirmation: {stock_id}/{trigger_date}"
            )
        confirmation_date = str(frame.at[confirmation_index, "date"])
        if safe_str(event.get("confirmation_date")) != confirmation_date:
            raise RuntimeError(
                "revenue readiness holdout D+1 confirmation date drift: "
                f"{stock_id}/{trigger_date}"
            )
        registered_trigger_close = round(
            float(frame.at[trigger_index, "analysis_close"]), 8
        )
        registered_confirmation_close = round(
            float(frame.at[confirmation_index, "analysis_close"]), 8
        )
        _require_number_close(
            event.get("trigger_close"),
            registered_trigger_close,
            f"holdout detail trigger_close row={row_index}",
            tolerance=5e-8,
        )
        _require_number_close(
            event.get("confirmation_close"),
            registered_confirmation_close,
            f"holdout detail confirmation_close row={row_index}",
            tolerance=5e-8,
        )
        if not registered_confirmation_close > registered_trigger_close:
            raise RuntimeError(
                "revenue readiness holdout frozen D+1 confirmation rule failed: "
                "confirmation_close must be greater than trigger_close; "
                f"{stock_id}/{trigger_date}"
            )
        if safe_str(event.get("entry_price_basis")) != "analysis_open":
            raise RuntimeError("revenue readiness holdout entry price basis drift")
        if safe_str(event.get("exit_price_basis")) != "analysis_close":
            raise RuntimeError("revenue readiness holdout exit price basis drift")
        if safe_str(event.get("exit_reason")) != "fixed_d30_close":
            raise RuntimeError("revenue readiness holdout exit reason drift")

        independently_mature = planned_exit_index < len(frame)
        return_valid = _bool_series(detail.loc[[row_index]], "return_valid").iloc[0]
        right_censored = _bool_series(
            detail.loc[[row_index]], "right_censored"
        ).iloc[0]
        if independently_mature != return_valid or right_censored == return_valid:
            raise RuntimeError(
                "revenue readiness holdout maturity disagrees with independently "
                "replayed D+2 entry and D+30 exit trading sessions: "
                f"{stock_id}/{trigger_date}/observed_through={observed_through}"
            )

        entry_observed = entry_index < len(frame)
        if entry_observed:
            expected_entry_date = str(frame.at[entry_index, "date"])
            if safe_str(event.get("entry_date")) != expected_entry_date:
                raise RuntimeError(
                    "revenue readiness holdout D+2 entry date drift: "
                    f"{stock_id}/{trigger_date}"
                )
            entry_price = float(frame.at[entry_index, "analysis_open"])
            if not math.isfinite(entry_price) or entry_price <= 0:
                raise RuntimeError(
                    f"registered D+2 entry open is invalid: {stock_id}/{trigger_date}"
                )
            _require_number_close(
                event.get("entry_price"),
                round(entry_price, 8),
                f"holdout detail entry_price row={row_index}",
                tolerance=5e-8,
            )
        else:
            if safe_str(event.get("entry_date")) or safe_str(event.get("entry_price")):
                raise RuntimeError(
                    "revenue readiness right-censored-before-entry event contains D+2 "
                    "entry data"
                )

        if not independently_mature:
            non_mature_fields = (
                "planned_exit_date",
                "exit_index",
                "exit_date",
                "exit_price",
                "realized_return_pct",
                "return_outcome",
            )
            if any(safe_str(event.get(field_name)) for field_name in non_mature_fields):
                raise RuntimeError(
                    "revenue readiness right-censored event contains unobserved realized "
                    f"outcome fields: {stock_id}/{trigger_date}"
                )
            expected_status = (
                "right_censored_before_d30"
                if entry_observed
                else "right_censored_before_entry"
            )
            if safe_str(event.get("operation_status")) != expected_status:
                raise RuntimeError(
                    "revenue readiness right-censored operation status drift: "
                    f"{stock_id}/{trigger_date}"
                )
            _strict_bool(
                event.get("realized_return_ge20"),
                False,
                f"holdout detail realized_return_ge20 row={row_index}",
            )
            _strict_bool(
                event.get("operation_return_review_candidate_flag"),
                False,
                f"holdout detail operation_return_review_candidate_flag row={row_index}",
            )
            continue

        exit_date = str(frame.at[planned_exit_index, "date"])
        if exit_date > observed_through:
            raise RuntimeError(
                "revenue readiness holdout independently replayed exit exceeds "
                f"observed_through: {stock_id}/{exit_date}/{observed_through}"
            )
        if safe_str(event.get("planned_exit_date")) != exit_date:
            raise RuntimeError(
                f"revenue readiness holdout planned D+30 exit date drift: {stock_id}"
            )
        if _strict_nonnegative_int(
            event.get("exit_index"), f"holdout detail exit_index row={row_index}"
        ) != planned_exit_index:
            raise RuntimeError(f"revenue readiness holdout D+30 exit index drift: {stock_id}")
        if safe_str(event.get("exit_date")) != exit_date:
            raise RuntimeError(f"revenue readiness holdout D+30 exit date drift: {stock_id}")
        exit_price = float(frame.at[planned_exit_index, "analysis_close"])
        if not math.isfinite(exit_price) or exit_price <= 0:
            raise RuntimeError(
                f"registered D+30 exit close is invalid: {stock_id}/{trigger_date}"
            )
        _require_number_close(
            event.get("exit_price"),
            round(exit_price, 8),
            f"holdout detail exit_price row={row_index}",
            tolerance=5e-8,
        )
        entry_price = float(frame.at[entry_index, "analysis_open"])
        realized_return = (exit_price / entry_price - 1.0) * 100.0
        rounded_return = round(realized_return, 4)
        _require_number_close(
            event.get("realized_return_pct"),
            rounded_return,
            f"holdout detail realized_return_pct row={row_index}",
            tolerance=5e-5,
        )
        expected_outcome = (
            "win"
            if realized_return > 1e-9
            else "failure"
            if realized_return < -1e-9
            else "neutral"
        )
        if safe_str(event.get("return_outcome")) != expected_outcome:
            raise RuntimeError(
                f"revenue readiness holdout return outcome drift: {stock_id}/{trigger_date}"
            )
        if safe_str(event.get("operation_status")) != "mature_operation":
            raise RuntimeError(
                f"revenue readiness mature operation status drift: {stock_id}/{trigger_date}"
            )
        _strict_bool(
            event.get("realized_return_ge20"),
            realized_return >= 20.0,
            f"holdout detail realized_return_ge20 row={row_index}",
        )
        _strict_bool(
            event.get("operation_return_review_candidate_flag"),
            abs(realized_return) >= OPERATION_RETURN_REVIEW_THRESHOLD_PCT,
            f"holdout detail operation_return_review_candidate_flag row={row_index}",
        )


def _validate_holdout_manifest_lineage(
    manifest: pd.DataFrame,
    detail: pd.DataFrame,
    summary: pd.DataFrame,
    replay_source: pd.DataFrame,
    source_projection_manifest: pd.DataFrame,
    *,
    repo_root: Path | str,
    diagnostics: list[str] | None = None,
) -> pd.Series:
    manifest_required = {
        "model_id",
        "artifact_id",
        "artifact_version",
        "capture_id",
        "artifact_row_key",
        "preregistration_pr_number",
        "preregistration_merge_commit",
        "rule_contract_version",
        "rule_canonical_sha256",
        "data_contract_version",
        "data_contract_sha256",
        "training_cutoff_date",
        "bridge_start_date",
        "bridge_end_date",
        "holdout_start_date",
        "observed_through_date",
        "source_artifact_id",
        "source_artifact_version",
        "source_detail_row_count",
        "source_detail_canonical_sha256",
        "monthly_revenue_history_blob_sha256",
        "monthly_revenue_canonical_table_sha256",
        "cross_market_resolution_registry_canonical_sha256",
        "training_source_projection_semantic_sha256",
        "training_source_projected_episode_row_count",
        "training_source_manifest_canonical_sha256",
        "price_input_stock_count",
        "price_input_row_count",
        "price_input_stock_canonical_sha256s",
        "price_input_canonical_sha256",
        "price_input_legacy_lineage_role",
        "price_semantic_projection_version",
        "price_semantic_projection_schema_sha256",
        "price_semantic_projection_columns",
        "price_semantic_projection_decimal_scale",
        "price_semantic_projection_stock_count",
        "price_semantic_projection_row_count",
        "price_semantic_projection_stock_canonical_sha256s",
        "price_semantic_projection_canonical_sha256",
        "price_semantic_projection_role",
        "price_semantic_projection_migration_id",
        "price_semantic_projection_authorization_reference",
        "bridge_excluded_signal_count",
        "holdout_event_count",
        "mature_event_count",
        "right_censored_event_count",
        "primary_mature_count",
        "primary_right_censored_count",
        "holdout_status",
        "append_only_history",
        "research_only",
        *HOLDOUT_FALSE_FIELDS,
        *MANIFEST_EXTRA_FALSE_FIELDS,
        "financial_statement_scope",
    }
    _required_columns(manifest, manifest_required, FORWARD_HOLDOUT_V2_MANIFEST_REL)
    if len(manifest) != 1:
        raise RuntimeError(
            "revenue forward holdout v2 latest manifest must contain exactly one row"
        )
    row = manifest.iloc[0]
    exact_fields = {
        "model_id": MODEL_ID,
        "artifact_id": REVENUE_FORWARD_HOLDOUT_V2_ARTIFACT_ID,
        "artifact_version": REVENUE_FORWARD_HOLDOUT_V2_ARTIFACT_VERSION,
        "artifact_row_key": "manifest",
        "preregistration_pr_number": PREREGISTRATION_PR_NUMBER,
        "preregistration_merge_commit": PREREGISTRATION_MERGE_COMMIT,
        "rule_contract_version": RULE_CONTRACT_VERSION,
        "data_contract_version": DATA_CONTRACT_VERSION,
        "price_input_legacy_lineage_role": PRICE_INPUT_LEGACY_LINEAGE_ROLE,
        "price_semantic_projection_version": PRICE_SEMANTIC_PROJECTION_VERSION,
        "price_semantic_projection_columns": "|".join(
            PRICE_SEMANTIC_PROJECTION_COLUMNS
        ),
        "price_semantic_projection_decimal_scale": str(
            PRICE_SEMANTIC_PROJECTION_DECIMAL_SCALE
        ),
        "price_semantic_projection_role": PRICE_SEMANTIC_PROJECTION_ROLE,
        "price_semantic_projection_migration_id": (
            PRICE_SEMANTIC_PROJECTION_MIGRATION_ID
        ),
        "price_semantic_projection_authorization_reference": (
            PRICE_SEMANTIC_PROJECTION_AUTHORIZATION_REFERENCE
        ),
        "training_cutoff_date": TRAINING_CUTOFF_DATE,
        "bridge_start_date": BRIDGE_START_DATE,
        "bridge_end_date": BRIDGE_END_DATE,
        "holdout_start_date": HOLDOUT_START_DATE,
        "source_artifact_id": SOURCE_ARTIFACT_ID,
        "source_artifact_version": SOURCE_ARTIFACT_VERSION,
        "financial_statement_scope": REVENUE_HOLDOUT_FINANCIAL_STATEMENT_SCOPE,
    }
    for field_name, expected in exact_fields.items():
        observed = safe_str(row.get(field_name))
        if observed != expected:
            if field_name == "artifact_version":
                raise RuntimeError(
                    "revenue forward holdout v2 artifact_version must be "
                    f"{expected!r}, got {observed!r}"
                )
            raise RuntimeError(
                f"revenue readiness holdout.{field_name} drift: "
                f"expected={expected!r} observed={observed!r}"
            )
    if not (
        TRAINING_CUTOFF_DATE < BRIDGE_START_DATE
        <= BRIDGE_END_DATE
        < HOLDOUT_START_DATE
    ):
        raise RuntimeError("revenue readiness holdout timing constants are invalid")
    _require_sha(
        row.get("rule_canonical_sha256"),
        "holdout.rule_canonical_sha256",
        expected=RULE_CANONICAL_SHA256,
    )
    _require_sha(
        row.get("data_contract_sha256"),
        "holdout.data_contract_sha256",
        expected=DATA_CONTRACT_SHA256,
    )
    _require_sha(
        row.get("price_semantic_projection_schema_sha256"),
        "holdout.price_semantic_projection_schema_sha256",
        expected=PRICE_SEMANTIC_PROJECTION_SCHEMA_SHA256,
    )
    projection_sha = _require_sha(
        row.get("price_semantic_projection_canonical_sha256"),
        "holdout.price_semantic_projection_canonical_sha256",
    )
    if projection_sha == "0" * 64:
        raise RuntimeError(
            "revenue readiness holdout canonical price-projection SHA is a "
            "placeholder SHA-256"
        )
    _require_sha(
        row.get("training_source_projection_semantic_sha256"),
        "holdout.training_source_projection_semantic_sha256",
        expected=PROJECTED_EPISODE_SEMANTIC_SHA256,
    )
    observed_training_manifest_legacy_sha = _require_sha(
        row.get("training_source_manifest_canonical_sha256"),
        "holdout.training_source_manifest_canonical_sha256",
    )
    if (
        observed_training_manifest_legacy_sha
        != SELECTED_V2_MANIFEST_CANONICAL_SHA256
        and diagnostics is not None
    ):
        diagnostics.append(
            "holdout training source manifest legacy raw/envelope SHA differs; "
            "selected manifest promotion semantic SHA remains the hard gate"
        )
    for field_name in (
        "source_detail_canonical_sha256",
        "monthly_revenue_history_blob_sha256",
        "monthly_revenue_canonical_table_sha256",
        "cross_market_resolution_registry_canonical_sha256",
        "capture_id",
    ):
        _require_sha(row.get(field_name), f"holdout.{field_name}")
    try:
        _parse_price_stock_sha_set(row)
    except RuntimeError as exc:
        if diagnostics is not None:
            diagnostics.append(
                "legacy prepared-frame price lineage is malformed; diagnostic "
                f"only: {exc}"
            )
    per_stock_price_sha = _parse_price_semantic_projection_stock_sha_set(row)
    projected_count = _strict_nonnegative_int(
        row.get("training_source_projected_episode_row_count"),
        "holdout.training_source_projected_episode_row_count",
    )
    if projected_count != PROJECTED_EPISODE_ROW_COUNT:
        raise RuntimeError(
            "revenue readiness holdout projected episode row count drift: "
            f"expected={PROJECTED_EPISODE_ROW_COUNT} "
            f"observed={projected_count}"
        )
    try:
        _validate_selected_v2_manifest(
            source_projection_manifest,
            diagnostics=diagnostics,
        )
    except RuntimeError as exc:
        raise RuntimeError(f"revenue readiness selected v2 source manifest invalid: {exc}") from exc

    observed_through = _strict_date(
        row.get("observed_through_date"), "holdout.observed_through_date"
    )
    normalized_source = _normalize_replay_source(replay_source)
    expected_source_rows = _strict_nonnegative_int(
        row.get("source_detail_row_count"), "holdout.source_detail_row_count"
    )
    if len(normalized_source) != expected_source_rows:
        raise RuntimeError(
            "revenue readiness holdout source detail row count drift: "
            f"manifest={expected_source_rows} replay={len(normalized_source)}"
        )
    observed_source_legacy_sha = _canonical_frame_sha256(normalized_source)
    expected_source_legacy_sha = safe_str(row.get("source_detail_canonical_sha256"))
    if observed_source_legacy_sha != expected_source_legacy_sha and diagnostics is not None:
        diagnostics.append(
            "holdout source detail legacy raw/envelope SHA differs; promotion "
            "semantic source replay remains the hard gate"
        )
    for field_name in MONTHLY_LINEAGE_COLUMNS:
        values = set(normalized_source[field_name].astype(str))
        expected = safe_str(row.get(field_name))
        if field_name == "monthly_revenue_history_blob_sha256":
            if values != {expected} and diagnostics is not None:
                diagnostics.append(
                    "raw monthly-revenue blob lineage differs between replay and "
                    "manifest; diagnostic only"
                )
            continue
        if values != {expected}:
            raise RuntimeError(
                f"revenue readiness holdout {field_name} disagrees with replay source"
            )

    expected_status = (
        "preregistered_waiting_for_start"
        if observed_through < HOLDOUT_START_DATE
        else "holdout_accumulating"
    )
    if safe_str(row.get("holdout_status")) != expected_status:
        raise RuntimeError(
            "revenue forward holdout v2 holdout_status is inconsistent with "
            "future-only timing"
        )
    _strict_bool(row.get("append_only_history"), True, "holdout.append_only_history")
    _validate_disabled_frame(
        manifest,
        source_name="holdout manifest",
        extra_false_fields=MANIFEST_EXTRA_FALSE_FIELDS,
    )

    capture_envelope = {
        "artifact_version": REVENUE_FORWARD_HOLDOUT_V2_ARTIFACT_VERSION,
        "rule_canonical_sha256": RULE_CANONICAL_SHA256,
        "data_contract_sha256": DATA_CONTRACT_SHA256,
        "preregistration_merge_commit": PREREGISTRATION_MERGE_COMMIT,
        "observed_through_date": observed_through,
        "source_detail_canonical_sha256": expected_source_legacy_sha,
        "price_semantic_projection_version": PRICE_SEMANTIC_PROJECTION_VERSION,
        "price_semantic_projection_schema_sha256": (
            PRICE_SEMANTIC_PROJECTION_SCHEMA_SHA256
        ),
        "price_semantic_projection_canonical_sha256": safe_str(
            row.get("price_semantic_projection_canonical_sha256")
        ),
        **{
            field_name: safe_str(row.get(field_name))
            for field_name in MONTHLY_LINEAGE_COLUMNS
        },
        "training_source_projection_semantic_sha256": (
            PROJECTED_EPISODE_SEMANTIC_SHA256
        ),
        "training_source_projected_episode_row_count": (
            PROJECTED_EPISODE_ROW_COUNT
        ),
        "training_source_manifest_canonical_sha256": (
            SELECTED_V2_MANIFEST_CANONICAL_SHA256
        ),
    }
    observed_capture = _canonical_json_sha256(capture_envelope)
    if safe_str(row.get("capture_id")) != observed_capture and diagnostics is not None:
        diagnostics.append(
            "holdout legacy capture_id differs; raw-excluded promotion frame and "
            "source semantic hashes remain the hard gates"
        )

    detail_required = {
        "model_id",
        "artifact_id",
        "artifact_version",
        "capture_id",
        "artifact_row_key",
        "event_key",
        "episode_key",
        "variant_id",
        "candidate_variant_id",
        *VARIANT_MEMBERSHIP_COLUMNS.values(),
        "lifecycle_policy_id",
        "confirmation_variant_id",
        "stop_policy_id",
        "same_stock_non_overlap_applied",
        "trigger_date",
        "source_asof_date",
        "source_asof_trade_date",
        "source_asof_revenue_period",
        "source_asof_row_canonical_sha256",
        "source_asof_canonical_source_table_date",
        "source_asof_sequence_index",
        "source_to_trigger_trading_days",
        "future_qualifying_update_ignored_count",
        "return_valid",
        "right_censored",
        "realized_return_pct",
        "return_outcome",
        "primary_metric_included",
        "event_row_canonical_sha256",
        "price_input_canonical_sha256",
        "price_semantic_projection_version",
        "price_semantic_projection_schema_sha256",
        "price_semantic_projection_canonical_sha256",
        "data_contract_version",
        "data_contract_sha256",
        "financial_statement_scope",
        "research_only",
        *HOLDOUT_FALSE_FIELDS,
    }
    _required_columns(detail, detail_required, FORWARD_HOLDOUT_V2_DETAIL_REL)
    _validate_disabled_frame(detail, source_name="holdout detail")
    for field_name, expected in {
        "model_id": MODEL_ID,
        "artifact_id": REVENUE_FORWARD_HOLDOUT_V2_ARTIFACT_ID,
        "artifact_version": REVENUE_FORWARD_HOLDOUT_V2_ARTIFACT_VERSION,
        "price_semantic_projection_version": PRICE_SEMANTIC_PROJECTION_VERSION,
        "price_semantic_projection_schema_sha256": (
            PRICE_SEMANTIC_PROJECTION_SCHEMA_SHA256
        ),
        "price_semantic_projection_canonical_sha256": safe_str(
            row.get("price_semantic_projection_canonical_sha256")
        ),
        "data_contract_version": DATA_CONTRACT_VERSION,
        "data_contract_sha256": DATA_CONTRACT_SHA256,
        "financial_statement_scope": REVENUE_HOLDOUT_FINANCIAL_STATEMENT_SCOPE,
    }.items():
        if not detail[field_name].astype(str).eq(expected).all():
            raise RuntimeError(
                f"revenue readiness holdout detail {field_name} drift"
            )
    invalid_capture_ids = sorted(
        {
            safe_str(value)
            for value in detail["capture_id"]
            if SHA256_RE.fullmatch(safe_str(value)) is None
        }
    )
    if invalid_capture_ids:
        raise RuntimeError("revenue readiness holdout detail capture_id is malformed")
    if (
        not detail["capture_id"].astype(str).eq(safe_str(row.get("capture_id"))).all()
        and diagnostics is not None
    ):
        diagnostics.append(
            "holdout detail legacy capture_id differs from manifest; diagnostic only"
        )
    if not set(detail["variant_id"].astype(str)).issubset(
        set(ALL_VARIANT_IDS)
    ):
        raise RuntimeError("revenue readiness holdout detail variant set drift")
    if detail["event_key"].astype(str).eq("").any() or detail[
        "event_key"
    ].astype(str).duplicated().any():
        raise RuntimeError("revenue readiness holdout detail event_key is blank or duplicate")
    if detail["artifact_row_key"].astype(str).eq("").any() or detail[
        "artifact_row_key"
    ].astype(str).duplicated().any():
        raise RuntimeError(
            "revenue readiness holdout detail artifact_row_key is blank or duplicate"
        )
    if not detail["artifact_row_key"].astype(str).eq(
        detail["event_key"].astype(str)
    ).all():
        raise RuntimeError(
            "revenue readiness holdout detail artifact/event key identity drift"
        )
    registered_prices = _load_registered_price_frames(
        repo_root,
        detail,
        observed_through=observed_through,
        per_stock_manifest_sha=per_stock_price_sha,
        required_stock_ids={
            _stock_id(value) for value in normalized_source["stock_id"]
        },
    )
    _validate_replay_source_pit_lineage(
        normalized_source,
        observed_through=observed_through,
        registered_prices=registered_prices,
    )
    _validate_detail_maturity_against_registered_prices(
        detail,
        observed_through=observed_through,
        registered_prices=registered_prices,
        manifest_price_projection_sha=safe_str(
            row.get("price_semantic_projection_canonical_sha256")
        ),
    )
    _validate_detail_source_asof_against_replay(
        detail,
        normalized_source=normalized_source,
        registered_prices=registered_prices,
    )
    mature_mask = _bool_series(detail, "return_valid")
    censored_mask = _bool_series(detail, "right_censored")
    if (mature_mask & censored_mask).any():
        raise RuntimeError("revenue readiness holdout row cannot be mature and right-censored")
    if not detail.empty:
        if (~_bool_series(detail, "primary_metric_included")).any():
            raise RuntimeError("revenue readiness holdout detail left primary metrics")
        for row_index, event in detail.iterrows():
            episode_key = safe_str(event.get("episode_key"))
            if episode_key not in normalized_source.index:
                raise RuntimeError(
                    "revenue readiness holdout detail episode is absent from committed "
                    f"replay source: {episode_key}"
                )
            for field_name, expected in {
                "lifecycle_policy_id": LIFECYCLE_POLICY_ID,
                "confirmation_variant_id": CONFIRMATION_VARIANT_ID,
                "stop_policy_id": STOP_POLICY_ID,
            }.items():
                if safe_str(event.get(field_name)) != expected:
                    raise RuntimeError(
                        "revenue readiness holdout frozen event contract drift: "
                        f"{field_name}/row={row_index}"
                    )
            primary_member = _bool_series(
                detail.loc[[row_index]], "primary_variant_member"
            ).iloc[0]
            low_member = _bool_series(
                detail.loc[[row_index]], "low_falling_member"
            ).iloc[0]
            union_member = _bool_series(
                detail.loc[[row_index]], "low_or_mid_falling_union_member"
            ).iloc[0]
            if primary_member == low_member or not union_member:
                raise RuntimeError(
                    "revenue readiness holdout frozen variant membership drift: "
                    f"row={row_index}"
                )
            expected_candidate_variant = (
                PRIMARY_VARIANT_ID
                if primary_member
                else "source_low_falling"
            )
            if safe_str(event.get("variant_id")) != expected_candidate_variant or safe_str(
                event.get("candidate_variant_id")
            ) != expected_candidate_variant:
                raise RuntimeError(
                    "revenue readiness holdout candidate variant/member drift: "
                    f"row={row_index}"
                )
            _strict_bool(
                event.get("same_stock_non_overlap_applied"),
                True,
                f"holdout detail same_stock_non_overlap_applied row={row_index}",
            )
            trigger_date = _strict_date(
                event.get("trigger_date"), f"holdout detail trigger_date row={row_index}"
            )
            if trigger_date < HOLDOUT_START_DATE:
                raise RuntimeError("revenue readiness holdout contains a bridge event")
            if trigger_date > observed_through:
                raise RuntimeError("revenue readiness holdout contains a future event")
            for field_name in (
                "source_asof_date",
                "source_asof_trade_date",
                "source_asof_canonical_source_table_date",
            ):
                source_date = _strict_date(
                    event.get(field_name),
                    f"holdout detail {field_name} row={row_index}",
                )
                if source_date > trigger_date:
                    raise RuntimeError(
                        f"revenue readiness holdout future source leakage: {field_name}"
                    )
            expected_event_sha = _canonical_mapping_sha256(
                event.drop(labels=["event_row_canonical_sha256"]).to_dict()
            )
            if safe_str(event.get("event_row_canonical_sha256")) != expected_event_sha:
                if diagnostics is not None:
                    diagnostics.append(
                        "holdout detail legacy event-row envelope differs; "
                        "promotion-semantic detail SHA and exact replay remain the hard gates: "
                        f"row={row_index}"
                    )
            if censored_mask.loc[row_index] and (
                safe_str(event.get("realized_return_pct"))
                or safe_str(event.get("return_outcome"))
            ):
                raise RuntimeError(
                    "revenue readiness right-censored event entered mature results"
                )
    if expected_status == "preregistered_waiting_for_start" and not detail.empty:
        raise RuntimeError("revenue readiness pre-start holdout detail must be empty")

    summary_required = {
        "variant_id",
        "variant_role",
        "holdout_status",
        "bridge_excluded_signal_count",
        "event_count",
        "mature_count",
        "right_censored_count",
        "research_only",
        *HOLDOUT_FALSE_FIELDS,
        "financial_statement_scope",
    }
    _required_columns(summary, summary_required, FORWARD_HOLDOUT_V2_SUMMARY_REL)
    _validate_disabled_frame(summary, source_name="holdout summary")
    if not summary["financial_statement_scope"].astype(str).eq(
        REVENUE_HOLDOUT_FINANCIAL_STATEMENT_SCOPE
    ).all():
        raise RuntimeError("revenue readiness holdout summary scope drift")
    if len(summary) != len(ALL_VARIANT_IDS):
        raise RuntimeError("revenue readiness holdout summary variant count drift")
    if set(summary["variant_id"].astype(str)) != set(
        ALL_VARIANT_IDS
    ):
        raise RuntimeError("revenue readiness holdout summary variant set drift")
    if summary["variant_id"].astype(str).duplicated().any():
        raise RuntimeError("revenue readiness holdout summary duplicate variant")

    manifest_bridge = _strict_nonnegative_int(
        row.get("bridge_excluded_signal_count"),
        "holdout.bridge_excluded_signal_count",
    )
    for _, summary_row in summary.iterrows():
        variant_id = safe_str(summary_row.get("variant_id"))
        expected_role = (
            "primary"
            if variant_id == PRIMARY_VARIANT_ID
            else "challenger"
        )
        if safe_str(summary_row.get("variant_role")) != expected_role:
            raise RuntimeError(
                f"revenue readiness holdout summary role drift for {variant_id}"
            )
        variant_detail = detail.loc[_variant_membership(detail, variant_id)]
        expected_event_count = len(variant_detail)
        expected_mature = int(
            _bool_series(variant_detail, "return_valid").sum()
        )
        expected_censored = int(
            _bool_series(variant_detail, "right_censored").sum()
        )
        expected_values = {
            "bridge_excluded_signal_count": manifest_bridge,
            "event_count": expected_event_count,
            "mature_count": expected_mature,
            "right_censored_count": expected_censored,
        }
        for field_name, expected in expected_values.items():
            observed = _strict_nonnegative_int(
                summary_row.get(field_name), f"holdout summary.{field_name}"
            )
            if observed != expected:
                raise RuntimeError(
                    f"revenue readiness holdout summary {field_name} drift for "
                    f"{variant_id}: expected={expected} observed={observed}"
                )
        if expected_mature + expected_censored != expected_event_count:
            raise RuntimeError(
                f"revenue readiness holdout maturity partition drift for {variant_id}"
            )
        if safe_str(summary_row.get("holdout_status")) != expected_status:
            raise RuntimeError("revenue readiness holdout summary status drift")

    manifest_counts = {
        "holdout_event_count": len(detail),
        "mature_event_count": int(mature_mask.sum()),
        "right_censored_event_count": int(censored_mask.sum()),
    }
    primary_detail = detail.loc[_variant_membership(detail, PRIMARY_VARIANT_ID)]
    manifest_counts.update(
        {
            "primary_mature_count": int(
                _bool_series(primary_detail, "return_valid").sum()
            ),
            "primary_right_censored_count": int(
                _bool_series(primary_detail, "right_censored").sum()
            ),
        }
    )
    for field_name, expected in manifest_counts.items():
        observed = _strict_nonnegative_int(
            row.get(field_name), f"holdout.{field_name}"
        )
        if observed != expected:
            raise RuntimeError(
                f"revenue readiness holdout {field_name} drift: "
                f"expected={expected} observed={observed}"
            )
    if manifest_counts["mature_event_count"] + manifest_counts[
        "right_censored_event_count"
    ] != manifest_counts["holdout_event_count"]:
        raise RuntimeError("revenue readiness holdout total maturity partition drift")
    return row


def validate_revenue_readiness_exact_replay(
    forward_holdout_v2_manifest: pd.DataFrame,
    *,
    holdout_detail: pd.DataFrame,
    holdout_summary: pd.DataFrame,
    replay_source: pd.DataFrame,
    repo_root: Path | str = Path("."),
) -> None:
    """Run the one canonical exact replay gate immediately before a writer."""

    _required_columns(
        forward_holdout_v2_manifest,
        {
            "observed_through_date",
            "data_contract_version",
            "data_contract_sha256",
            "price_semantic_projection_version",
            "price_semantic_projection_schema_sha256",
            "price_semantic_projection_stock_canonical_sha256s",
            "price_semantic_projection_canonical_sha256",
        },
        FORWARD_HOLDOUT_V2_MANIFEST_REL,
    )
    if len(forward_holdout_v2_manifest) != 1:
        raise RuntimeError(
            "revenue forward holdout v2 latest manifest must contain exactly one row"
        )
    row = forward_holdout_v2_manifest.iloc[0]
    _validate_exact_registered_price_lineage(
        repo_root,
        row,
        manifest=forward_holdout_v2_manifest,
        detail=holdout_detail,
        summary=holdout_summary,
        replay_source=replay_source,
        observed_through=_strict_date(
            row.get("observed_through_date"),
            "holdout.observed_through_date",
        ),
        per_stock_manifest_sha=(
            _parse_price_semantic_projection_stock_sha_set(row)
        ),
    )


def validate_revenue_readiness_source_files(
    repo_root: Path | str = Path("."),
) -> list[str]:
    root = Path(repo_root)
    _, promotion_errors = validate_revenue_promotion_registry(
        root / REVENUE_PROMOTION_REGISTRY_CSV
    )
    anomaly_result = validate_current_anomaly_dispositions(
        root,
        require_effective_nonblocking=True,
    )
    anomaly_errors = anomaly_result.errors
    errors = [
        *(f"revenue promotion readiness source: {error}" for error in promotion_errors),
        *(f"revenue anomaly readiness source: {error}" for error in anomaly_errors),
    ]
    if errors:
        return errors
    try:
        summarize_revenue_promotion_readiness(
            pd.read_csv(root / REVENUE_PROMOTION_REGISTRY_CSV, dtype=str).fillna(""),
            pd.read_csv(root / REVENUE_ANOMALY_REGISTRY_CSV, dtype=str).fillna(""),
            pd.read_csv(
                root / REVENUE_FORWARD_HOLDOUT_V2_MANIFEST_CSV, dtype=str
            ).fillna(""),
            holdout_detail=pd.read_csv(
                root / REVENUE_FORWARD_HOLDOUT_V2_DETAIL_CSV, dtype=str
            ).fillna(""),
            holdout_summary=pd.read_csv(
                root / REVENUE_FORWARD_HOLDOUT_V2_SUMMARY_CSV, dtype=str
            ).fillna(""),
            replay_source=pd.read_csv(
                root / REVENUE_FORWARD_HOLDOUT_V2_REPLAY_SOURCE_CSV, dtype=str
            ).fillna(""),
            source_projection_manifest=pd.read_csv(
                root / REVENUE_SOURCE_PROJECTION_MANIFEST_CSV, dtype=str
            ).fillna(""),
            repo_root=root,
            anomaly_result=anomaly_result,
        )
    except (OSError, pd.errors.ParserError, RuntimeError) as exc:
        errors.append(f"revenue readiness holdout source: {exc}")
    return errors


def _promotion_profile_for_row(
    promotion: pd.Series | dict[str, Any],
) -> RevenuePromotionReadinessProfile:
    decision_id = safe_str(promotion.get("decision_id"))
    profile = REVENUE_PROMOTION_PROFILES.get(decision_id)
    if profile is None:
        raise RuntimeError(
            "revenue readiness latest decision_id is not an exact supported v4/v5 "
            f"profile: {decision_id!r}"
        )
    return profile


def _validated_revenue_promotion_row(
    promotion_registry: pd.DataFrame,
) -> tuple[pd.Series, int, int]:
    promotion_required = {
        "decision_id",
        "decision_date",
        "model_id",
        "contract_version",
        "candidate_variant_id",
        "operation_count",
        "win_rate_pct",
        "median_return_pct",
        "combined_exclusion_candidate_count",
        "forward_holdout_first_interpretation_min_mature",
        "formal_adapter_gate",
        "decision_status",
        "anomaly_disposition_gate",
        "approved_for_daily",
        "presentation_allowed",
        "formal_model_use_allowed",
        "production_change",
        "financial_statement_scope",
        "promotion_scope",
    }
    _required_columns(
        promotion_registry,
        promotion_required,
        str(REVENUE_PROMOTION_REGISTRY_CSV),
    )
    promotion_rows = promotion_registry[
        promotion_registry["model_id"].astype(str).eq(MODEL_ID)
    ].copy()
    if promotion_rows.empty:
        raise RuntimeError("revenue promotion registry has no model row")
    if promotion_rows["decision_id"].astype(str).duplicated().any():
        raise RuntimeError("revenue promotion registry contains duplicate decision_id")
    decision_dates = pd.to_datetime(promotion_rows["decision_date"], errors="coerce")
    if decision_dates.isna().any() or not decision_dates.is_monotonic_increasing:
        raise RuntimeError("revenue promotion decision_date must be append-only")
    promotion = promotion_rows.iloc[-1]
    profile = _promotion_profile_for_row(promotion)
    expected_promotion = {
        "decision_id": profile.decision_id,
        "contract_version": profile.contract_version,
        "candidate_variant_id": REVENUE_SOURCE_VARIANT_ID,
        "financial_statement_scope": REVENUE_PROMOTION_FINANCIAL_STATEMENT_SCOPE,
        "decision_status": profile.decision_status,
        "anomaly_disposition_gate": profile.anomaly_disposition_gate,
        "formal_adapter_gate": profile.formal_adapter_gate,
        "promotion_scope": profile.promotion_scope,
    }
    for field_name, expected in expected_promotion.items():
        observed = safe_str(promotion.get(field_name))
        if observed != expected:
            if field_name == "contract_version":
                raise RuntimeError(
                    "revenue readiness promotion contract is mixed with decision profile "
                    f"{profile.decision_id!r}: expected={expected!r}; got={observed!r}"
                )
            raise RuntimeError(
                f"revenue readiness promotion.{field_name} must be "
                f"{expected!r}, got {observed!r}"
            )
    for field_name in (
        "approved_for_daily",
        "presentation_allowed",
        "formal_model_use_allowed",
        "production_change",
    ):
        _strict_bool(promotion.get(field_name), False, f"promotion.{field_name}")
    minimum_mature = _strict_nonnegative_int(
        promotion.get("forward_holdout_first_interpretation_min_mature"),
        "promotion.forward_holdout_first_interpretation_min_mature",
    )
    if minimum_mature <= 0:
        raise RuntimeError("revenue readiness holdout maturity threshold must be positive")
    candidate_count = _strict_nonnegative_int(
        promotion.get("combined_exclusion_candidate_count"),
        "promotion.combined_exclusion_candidate_count",
    )
    return promotion, minimum_mature, candidate_count


@dataclass(frozen=True)
class CanonicalAnomalyValidationResult:
    rows: dict[str, dict[str, str]]
    row_count: int
    effective_blocker_count: int
    verified_real_extreme_count: int
    verified_data_error_repaired_count: int
    errors: tuple[str, ...]
    diagnostics: tuple[str, ...]


@dataclass(frozen=True)
class DisabledAdapterPreparationValidationResult:
    validator_rel: str
    module_rel: str
    protocol_line: str


@dataclass(frozen=True)
class AttestedAdapterSource:
    logical_path: str
    committed_object_id: str
    blob: bytes


def _committed_adapter_source(repo: Path, logical_path: str) -> AttestedAdapterSource:
    """Bind validation to the exact tracked HEAD blob after Git clean filters."""

    candidate = repo / logical_path
    resolved = candidate.resolve()
    try:
        resolved.relative_to(repo)
    except ValueError as exc:
        raise RuntimeError(
            f"disabled adapter validation path escapes repository root: {logical_path}"
        ) from exc
    if candidate.is_symlink():
        raise RuntimeError(
            f"disabled adapter validation path must not be a symlink: {logical_path}"
        )
    if not resolved.is_file():
        raise RuntimeError(
            f"disabled adapter validation source is missing: {logical_path}"
        )
    commands = {
        "committed": [
            "git",
            "--no-replace-objects",
            "rev-parse",
            "--verify",
            f"HEAD:{logical_path}",
        ],
        "worktree": [
            "git",
            "--no-replace-objects",
            "hash-object",
            f"--path={logical_path}",
            "--",
            logical_path,
        ],
    }
    object_ids: dict[str, str] = {}
    for source_name, command in commands.items():
        try:
            completed = subprocess.run(
                command,
                cwd=repo,
                check=False,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
                encoding="utf-8",
                errors="replace",
                timeout=30,
            )
        except (OSError, subprocess.TimeoutExpired) as exc:
            raise RuntimeError(
                f"cannot attest disabled adapter {source_name} identity: {logical_path}"
            ) from exc
        object_id = completed.stdout.strip()
        if (
            completed.returncode != 0
            or completed.stderr != ""
            or re.fullmatch(r"[0-9a-f]{40}(?:[0-9a-f]{24})?", object_id) is None
        ):
            raise RuntimeError(
                f"cannot attest disabled adapter {source_name} identity: {logical_path}"
            )
        object_ids[source_name] = object_id
    if object_ids["worktree"] != object_ids["committed"]:
        raise RuntimeError(
            "disabled adapter validation source differs from committed HEAD blob: "
            f"{logical_path}"
        )
    try:
        blob_result = subprocess.run(
            [
                "git",
                "--no-replace-objects",
                "cat-file",
                "blob",
                object_ids["committed"],
            ],
            cwd=repo,
            check=False,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            timeout=30,
        )
    except (OSError, subprocess.TimeoutExpired) as exc:
        raise RuntimeError(
            f"cannot materialize committed disabled adapter blob: {logical_path}"
        ) from exc
    if blob_result.returncode != 0 or blob_result.stderr != b"":
        raise RuntimeError(
            f"cannot materialize committed disabled adapter blob: {logical_path}"
        )
    return AttestedAdapterSource(
        logical_path=logical_path,
        committed_object_id=object_ids["committed"],
        blob=blob_result.stdout,
    )


def validate_disabled_adapter_preparation(
    repo_root: Path | str,
) -> DisabledAdapterPreparationValidationResult:
    """Run the model-owned validator in an isolated child without importing it."""

    repo = Path(repo_root).resolve()
    validator = _committed_adapter_source(repo, REVENUE_ADAPTER_VALIDATOR_REL)
    module = _committed_adapter_source(repo, REVENUE_ADAPTER_MODULE_REL)
    child_env = dict(os.environ)
    child_env.update(
        {
            "PYTHONDONTWRITEBYTECODE": "1",
            "PYTHONNOUSERSITE": "1",
            "NoDefaultCurrentDirectoryInExePath": "1",
        }
    )
    try:
        with tempfile.TemporaryDirectory(
            prefix="revenue-disabled-adapter-validation-"
        ) as temp_name:
            isolated_root = Path(temp_name).resolve()
            isolated_scripts = isolated_root / "scripts"
            isolated_scripts.mkdir()
            validator_path = isolated_scripts / Path(validator.logical_path).name
            module_path = isolated_scripts / Path(module.logical_path).name
            validator_path.write_bytes(validator.blob)
            module_path.write_bytes(module.blob)
            command = [
                sys.executable,
                "-I",
                "-B",
                str(validator_path),
                "--phase",
                "disabled-preparation",
                "--module",
                str(module_path),
            ]
            completed = subprocess.run(
                command,
                cwd=isolated_root,
                env=child_env,
                check=False,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
                encoding="utf-8",
                errors="replace",
                timeout=REVENUE_ADAPTER_VALIDATION_TIMEOUT_SECONDS,
            )
    except subprocess.TimeoutExpired as exc:
        raise RuntimeError("disabled adapter preparation validator timed out") from exc
    except OSError as exc:
        raise RuntimeError(
            "disabled adapter preparation validator could not start"
        ) from exc
    stdout = completed.stdout
    stderr = completed.stderr
    if not isinstance(stdout, str) or not isinstance(stderr, str):
        raise RuntimeError(
            "disabled adapter preparation validator returned a non-text protocol"
        )
    if stderr != "":
        raise RuntimeError(
            "disabled adapter preparation validator emitted stderr: " + stderr
        )
    if completed.returncode != 0:
        raise RuntimeError(
            "disabled adapter preparation validator failed with exit "
            f"{completed.returncode}" + (f": {stdout}" if stdout else "")
        )
    accepted_stdout = {
        REVENUE_ADAPTER_VALIDATION_PASS,
        REVENUE_ADAPTER_VALIDATION_PASS + "\n",
        REVENUE_ADAPTER_VALIDATION_PASS + "\r\n",
    }
    if stdout not in accepted_stdout:
        raise RuntimeError(
            "disabled adapter preparation validator PASS protocol missing, duplicated, "
            f"or unknown: {stdout!r}"
        )
    return DisabledAdapterPreparationValidationResult(
        validator_rel=REVENUE_ADAPTER_VALIDATOR_REL,
        module_rel=REVENUE_ADAPTER_MODULE_REL,
        protocol_line=REVENUE_ADAPTER_VALIDATION_PASS,
    )


def validate_current_anomaly_dispositions(
    repo_root: Path | str,
    *,
    require_effective_nonblocking: bool,
) -> CanonicalAnomalyValidationResult:
    """Run the research-owner canonical gate without importing its semantics."""

    if not require_effective_nonblocking:
        raise RuntimeError(
            "readiness must invoke the canonical anomaly gate in effective-nonblocking mode"
        )
    repo = Path(repo_root).resolve()
    validator = (repo / REVENUE_ANOMALY_VALIDATOR_REL).resolve()
    try:
        validator.relative_to(repo)
    except ValueError as exc:
        raise RuntimeError("canonical anomaly validator escapes repository root") from exc
    if not validator.is_file():
        raise RuntimeError(
            f"missing canonical anomaly validator: {REVENUE_ANOMALY_VALIDATOR_REL}"
        )
    command = [
        sys.executable,
        "-I",
        "-B",
        str(validator),
        "--repo-root",
        str(repo),
        "--require-effective-nonblocking",
    ]
    try:
        completed = subprocess.run(
            command,
            cwd=repo,
            check=False,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            encoding="utf-8",
            errors="replace",
            timeout=300,
        )
    except subprocess.TimeoutExpired as exc:
        raise RuntimeError("canonical anomaly validator timed out") from exc
    except OSError as exc:
        raise RuntimeError("canonical anomaly validator could not start") from exc
    stdout_lines = [line.strip() for line in completed.stdout.splitlines() if line.strip()]
    diagnostics = tuple(
        line.removeprefix("DIAGNOSTIC:").strip()
        for line in stdout_lines
        if line.startswith("DIAGNOSTIC:")
    )
    errors: list[str] = [
        line.removeprefix("ERROR:").strip()
        for line in stdout_lines
        if line.startswith("ERROR:")
    ]
    pass_pattern = re.compile(
        r"^PASS: revenue_unreacted_range anomaly dispositions validated; "
        r"rows=(?P<rows>\d+); effective_blockers=(?P<blockers>\d+); "
        r"verified_real_extreme=(?P<real>\d+); "
        r"verified_data_error_repaired=(?P<repaired>\d+); "
        r"raw-byte and line-ending identities=diagnostic-only$"
    )
    pass_matches = [
        match for line in stdout_lines if (match := pass_pattern.fullmatch(line))
    ]
    unknown_lines = [
        line
        for line in stdout_lines
        if not line.startswith("DIAGNOSTIC:")
        and not line.startswith("ERROR:")
        and pass_pattern.fullmatch(line) is None
    ]
    if unknown_lines:
        errors.append(
            "canonical anomaly validator emitted unknown output: "
            + " | ".join(unknown_lines)
        )
    if completed.stderr.strip():
        errors.append(
            "canonical anomaly validator emitted stderr: " + completed.stderr.strip()
        )
    if completed.returncode:
        detail = completed.stdout.strip()
        errors.append(
            f"canonical revenue anomaly disposition gate failed with exit "
            f"{completed.returncode}" + (f": {detail}" if detail else "")
        )
    if completed.returncode == 0 and len(pass_matches) != 1:
        errors.append("canonical anomaly validator PASS protocol missing or duplicated")

    row_count = blocker_count = real_count = repaired_count = 0
    if len(pass_matches) == 1:
        match = pass_matches[0]
        row_count = int(match.group("rows"))
        blocker_count = int(match.group("blockers"))
        real_count = int(match.group("real"))
        repaired_count = int(match.group("repaired"))

    rows: dict[str, dict[str, str]] = {}
    registry = repo / REVENUE_ANOMALY_REGISTRY_PATH
    try:
        frame = pd.read_csv(registry, dtype=str).fillna("")
        if "operation_key" not in frame.columns:
            raise RuntimeError("canonical anomaly registry missing operation_key")
        if frame["operation_key"].astype(str).duplicated().any():
            raise RuntimeError("canonical anomaly registry contains duplicate operation_key")
        rows = {
            safe_str(row["operation_key"]): {
                str(key): safe_str(value) for key, value in row.items()
            }
            for row in frame.to_dict(orient="records")
        }
    except (OSError, ValueError, RuntimeError) as exc:
        errors.append(str(exc))
    if len(rows) != row_count:
        errors.append(
            "canonical anomaly validator protocol row count disagrees with registry"
        )
    return CanonicalAnomalyValidationResult(
        rows=rows,
        row_count=row_count,
        effective_blocker_count=blocker_count,
        verified_real_extreme_count=real_count,
        verified_data_error_repaired_count=repaired_count,
        errors=tuple(errors),
        diagnostics=diagnostics,
    )


def summarize_revenue_promotion_readiness(
    promotion_registry: pd.DataFrame,
    anomaly_registry: pd.DataFrame,
    forward_holdout_v2_manifest: pd.DataFrame,
    *,
    holdout_detail: pd.DataFrame,
    holdout_summary: pd.DataFrame,
    replay_source: pd.DataFrame,
    source_projection_manifest: pd.DataFrame,
    repo_root: Path | str = Path("."),
    diagnostics: list[str] | None = None,
    anomaly_result: Any | None = None,
) -> dict[str, Any]:
    promotion, minimum_mature, candidate_count = (
        _validated_revenue_promotion_row(promotion_registry)
    )
    profile = _promotion_profile_for_row(promotion)
    if profile.adapter_validation_required:
        validate_disabled_adapter_preparation(repo_root)

    holdout = _validate_holdout_manifest_lineage(
        forward_holdout_v2_manifest,
        holdout_detail,
        holdout_summary,
        replay_source,
        source_projection_manifest,
        repo_root=repo_root,
        diagnostics=diagnostics,
    )
    mature_count = _strict_nonnegative_int(
        holdout.get("primary_mature_count"), "holdout.primary_mature_count"
    )
    # The anomaly validator is the sole owner of disposition semantics, evidence,
    # repaired-rerun closure, and the effective blocker calculation.  Readiness
    # consumes its result instead of maintaining a second policy implementation.
    del anomaly_registry
    if anomaly_result is None:
        anomaly_result = validate_current_anomaly_dispositions(
            Path(repo_root),
            require_effective_nonblocking=True,
        )
    if anomaly_result.errors:
        raise RuntimeError(
            "canonical revenue anomaly disposition gate failed: "
            + "; ".join(anomaly_result.errors)
        )
    if diagnostics is not None:
        diagnostics.extend(anomaly_result.diagnostics)
    if candidate_count != anomaly_result.verified_real_extreme_count:
        raise RuntimeError(
            "revenue promotion current anomaly count disagrees with canonical gate"
        )
    unresolved_count = sum(
        row.get("final_disposition") == "unresolved_anomaly_candidate"
        for row in anomaly_result.rows.values()
    )
    blocking_anomaly_count = anomaly_result.effective_blocker_count
    if profile.adapter_validation_required:
        blocker = f"forward_holdout_v2_mature={mature_count}/{minimum_mature}"
        status_note = (
            "revenue_unreacted_range／source_mid_falling v2 的模型專屬研究矩陣、"
            "九筆 anomaly disposition 與 disabled formal adapter preparation 均已完成；"
            "八筆 verified_real_extreme 保留於 Primary，6177 的衍生 attribution data "
            "error 已完成固定規則修復重跑。adapter 僅為 model-owned in-memory disabled "
            "preparation，沒有 writer、runtime artifact、PDF／packet consumer 或操作指令；"
            f"目前 promotion blocker 僅為 forward holdout v2 成熟度 "
            f"{mature_count}/{minimum_mature}。月營收以外的 EPS、毛利率、營益率、"
            "營業利益、業外損益、淨利及季度／年度財報欄位均不在模型範圍；"
            "formal_model_use_allowed、approved_for_daily、presentation_allowed 與 "
            "production_allowed 均維持 False。"
        )
    else:
        blocker = (
            f"anomaly_disposition_blockers={blocking_anomaly_count}; "
            f"unresolved_anomalies={unresolved_count}; "
            f"forward_holdout_v2_mature={mature_count}/{minimum_mature}; "
            "formal_adapter=not_started"
        )
        status_note = (
            "revenue_unreacted_range／source_mid_falling v2 的模型專屬研究矩陣已完成；"
            "九筆 anomaly 已完成逐筆 disposition，八筆 verified_real_extreme 保留於 "
            "Primary，6177 的衍生 attribution data error 已完成固定規則修復重跑；"
            f"目前 anomaly effective blocker={blocking_anomaly_count}、未定案={unresolved_count}，"
            "仍待 forward holdout v2 "
            f"成熟度 {mature_count}/{minimum_mature} 與 disabled formal adapter preparation 尚未完成。"
            "月營收以外的 EPS、毛利率、營益率、營業利益、業外損益、淨利及季度／年度財報欄位均不在模型範圍；"
            "不得產生 production、PDF、packet 或操作指令。"
        )
    return {
        "parity_status": REVENUE_RESEARCH_MATRIX_STATUS,
        "blocker": blocker,
        "operation_module_status": profile.operation_module_status,
        "daily_adapter_status": profile.daily_adapter_status,
        "formal_model_use_allowed": "False",
        "approved_for_daily": "False",
        "approval_status": "not_started",
        "operation_module_id": profile.operation_module_id,
        "approval_version": "",
        "presentation_allowed": "False",
        "production_allowed": "False",
        "operation_directive_level": "no_operation_directive",
        "pdf_integration_status": "not_started",
        "packet_integration_status": "not_started",
        "registry_pattern_count": 1,
        "registry_current_model_pattern_count": 0,
        "registry_best_pattern_id": safe_str(
            promotion.get("candidate_variant_id")
        ),
        "registry_best_sample_size": _strict_nonnegative_int(
            promotion.get("operation_count"), "promotion.operation_count"
        ),
        "registry_best_win_rate": safe_str(promotion.get("win_rate_pct")),
        "registry_best_median_return": safe_str(
            promotion.get("median_return_pct")
        ),
        "daily_adapter_row_count": 0,
        "daily_adapter_data_row_count": 0,
        "daily_adapter_sections": "",
        "status_note_zh": status_note,
    }


def _git_blob(repo: Path, logical_path: str) -> bytes:
    result = subprocess.run(
        [
            "git",
            "--no-replace-objects",
            "show",
            f"HEAD:{logical_path}",
        ],
        cwd=repo,
        check=False,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    if result.returncode:
        raise RuntimeError(
            f"cannot read committed source HEAD:{logical_path}: "
            + result.stderr.decode("utf-8", errors="replace").strip()
        )
    return result.stdout


def _parse_csv_bytes(data: bytes, source_name: str) -> tuple[list[str], list[dict[str, str]]]:
    previous_field_limit = csv.field_size_limit()
    try:
        csv.field_size_limit(max(previous_field_limit, 10_000_000))
        text = data.decode("utf-8-sig")
        reader = csv.DictReader(io.StringIO(text))
        fieldnames = reader.fieldnames
        if not fieldnames:
            raise ValueError("missing CSV header")
        if any(not field.strip() for field in fieldnames):
            raise ValueError("blank CSV header")
        if len(fieldnames) != len(set(fieldnames)):
            raise ValueError("duplicate CSV header")
        rows = list(reader)
        if any(None in row for row in rows):
            raise ValueError("CSV row has more values than the header")
    except (UnicodeDecodeError, csv.Error, ValueError) as exc:
        raise RuntimeError(f"malformed committed CSV source {source_name}: {exc}") from exc
    finally:
        csv.field_size_limit(previous_field_limit)
    return fieldnames, rows


def _canonical_csv(data: bytes, source_name: str) -> bytes:
    fieldnames, rows = _parse_csv_bytes(data, source_name)
    return json.dumps(
        {"fieldnames": fieldnames, "rows": rows},
        ensure_ascii=False,
        separators=(",", ":"),
    ).encode("utf-8")


def _canonical_csv_excluding_transport_provenance(
    data: bytes,
    source_name: str,
) -> bytes:
    fieldnames, rows = _parse_csv_bytes(data, source_name)
    semantic_fields = [
        field_name
        for field_name in fieldnames
        if not _is_transport_provenance_column(field_name)
    ]
    return json.dumps(
        {
            "fieldnames": semantic_fields,
            "rows": [
                {
                    field_name: _canonical_value(row.get(field_name, ""))
                    for field_name in semantic_fields
                }
                for row in rows
            ],
        },
        ensure_ascii=False,
        separators=(",", ":"),
    ).encode("utf-8")


def _registry_semantic_sha256(path: Path) -> str:
    data = path.read_bytes()
    return hashlib.sha256(
        _canonical_csv_excluding_transport_provenance(data, str(path))
    ).hexdigest()


def validate_revenue_promotion_registry(
    path: Path,
) -> tuple[dict[str, str] | None, list[str]]:
    errors: list[str] = []
    try:
        fieldnames, rows = _parse_csv_bytes(path.read_bytes(), str(path))
        del fieldnames
        observed_sha = _registry_semantic_sha256(path)
    except (OSError, RuntimeError) as exc:
        return None, [str(exc)]
    if not rows:
        return None, [*errors, "promotion preparation registry is empty"]
    try:
        latest, _minimum_mature, _candidate_count = (
            _validated_revenue_promotion_row(pd.DataFrame(rows, dtype=str).fillna(""))
        )
        profile = _promotion_profile_for_row(latest)
    except RuntimeError as exc:
        errors.append(str(exc))
        return None, errors
    if observed_sha != profile.registry_canonical_sha256:
        errors.append(
            "promotion preparation registry canonical semantic SHA-256 drift for "
            f"{profile.decision_id}: expected={profile.registry_canonical_sha256}; "
            f"actual={observed_sha}"
        )
    return {str(key): safe_str(value) for key, value in latest.items()}, errors


def validate_revenue_anomaly_registry(
    path: Path,
) -> tuple[dict[str, dict[str, str]], list[str]]:
    # Compatibility signature for the readiness writer.  All anomaly business
    # semantics live in validate_revenue_unreacted_range_anomaly_dispositions.
    resolved = path.resolve()
    repo = resolved.parents[1]
    expected_path = (repo / REVENUE_ANOMALY_REGISTRY_PATH).resolve()
    if resolved != expected_path:
        return {}, [
            "readiness anomaly source must be the canonical v3 registry: "
            f"expected={expected_path}; actual={resolved}"
        ]
    result = validate_current_anomaly_dispositions(
        repo,
        require_effective_nonblocking=True,
    )
    return result.rows, result.errors


def _canonical_markdown(data: bytes, source_name: str) -> bytes:
    try:
        text = data.decode("utf-8-sig")
    except UnicodeDecodeError as exc:
        raise RuntimeError(f"malformed committed Markdown source {source_name}: {exc}") from exc
    normalized = text.replace("\r\n", "\n")
    if "\r" in normalized:
        raise RuntimeError(
            f"malformed committed Markdown source {source_name}: bare carriage return"
        )
    return normalized.encode("utf-8")


def validate_exact_predecessor_readiness_mirrors(
    repo_root: Path | str,
) -> tuple[pd.DataFrame, list[str]]:
    """Validate the one-shot pre-v5 mirror set by canonical semantics only."""

    repo = Path(repo_root).resolve()
    canonical_data: dict[str, bytes] = {}
    worktree_data: dict[str, bytes] = {}
    diagnostics: list[str] = []
    for logical_path in READINESS_MIRROR_RELS:
        path = repo / logical_path
        try:
            observed = path.read_bytes()
            committed = _git_blob(repo, logical_path)
        except OSError as exc:
            raise RuntimeError(
                f"exact predecessor readiness mirror is missing: {logical_path}"
            ) from exc
        canonicalizer = (
            _canonical_csv if logical_path.endswith(".csv") else _canonical_markdown
        )
        committed_canonical = canonicalizer(
            committed,
            f"HEAD:{logical_path}",
        )
        observed_canonical = canonicalizer(observed, logical_path)
        expected_sha = EXACT_PREDECESSOR_READINESS_CANONICAL_SHA256[logical_path]
        committed_sha = hashlib.sha256(committed_canonical).hexdigest()
        observed_sha = hashlib.sha256(observed_canonical).hexdigest()
        if committed_sha != expected_sha:
            raise RuntimeError(
                "exact predecessor committed readiness semantic drift: "
                f"{logical_path}; expected={expected_sha}; actual={committed_sha}"
            )
        if observed_sha != committed_sha:
            raise RuntimeError(
                "exact predecessor readiness worktree semantic drift from HEAD: "
                f"{logical_path}; committed={committed_sha}; actual={observed_sha}"
            )
        if observed != committed:
            diagnostics.append(
                "raw-byte/line-ending diagnostic only; canonical predecessor semantics "
                f"match HEAD: {logical_path}"
            )
        canonical_data[logical_path] = observed_canonical
        worktree_data[logical_path] = observed

    if canonical_data[OUT_CSV_REL] != canonical_data[DOCS_CSV_REL]:
        raise RuntimeError("exact predecessor output/docs readiness CSV mirrors differ")
    if canonical_data[OUT_MD_REL] != canonical_data[DOCS_MD_REL]:
        raise RuntimeError(
            "exact predecessor output/docs readiness Markdown mirrors differ"
        )
    fieldnames, rows = _parse_csv_bytes(worktree_data[OUT_CSV_REL], OUT_CSV_REL)
    predecessor = pd.DataFrame(rows, columns=fieldnames).fillna("")
    validate_markdown_status_table_matches_csv(
        worktree_data[OUT_MD_REL],
        predecessor,
        source_name=OUT_MD_REL,
    )
    validate_markdown_status_table_matches_csv(
        worktree_data[DOCS_MD_REL],
        predecessor,
        source_name=DOCS_MD_REL,
    )
    return predecessor, diagnostics


def _committed_semantic_source(
    repo: Path,
    logical_path: str,
    *,
    csv_source: bool,
) -> tuple[bytes, str | None]:
    path = repo / logical_path
    try:
        worktree_data = path.read_bytes()
    except OSError as exc:
        raise RuntimeError(f"missing readiness sync source {logical_path}: {exc}") from exc
    committed_data = _git_blob(repo, logical_path)
    if logical_path == ANOMALY_REGISTRY_REL:
        worktree_semantic = hashlib.sha256(
            _canonical_csv_excluding_transport_provenance(
                worktree_data,
                logical_path,
            )
        ).hexdigest()
        committed_semantic = hashlib.sha256(
            _canonical_csv_excluding_transport_provenance(
                committed_data,
                f"HEAD:{logical_path}",
            )
        ).hexdigest()
        if worktree_semantic != committed_semantic:
            raise RuntimeError(
                f"readiness sync source has semantic drift from HEAD: {logical_path}"
            )
        diagnostic = None
        if worktree_data != committed_data:
            diagnostic = (
                "raw-byte or raw-file-SHA diagnostic only "
                f"(canonical semantics match HEAD): {logical_path}"
            )
        return committed_data, diagnostic
    frame_names = {
        FORWARD_HOLDOUT_V2_MANIFEST_REL: "manifest",
        FORWARD_HOLDOUT_V2_DETAIL_REL: "detail",
        FORWARD_HOLDOUT_V2_SUMMARY_REL: "summary",
        FORWARD_HOLDOUT_V2_COMPARISON_REL: "comparison",
        FORWARD_HOLDOUT_V2_ANOMALY_SENSITIVITY_REL: "anomaly",
    }
    semantic_digest: Callable[[bytes, str], str] | None = None
    if logical_path == PROMOTION_REGISTRY_REL:
        semantic_digest = lambda data, label: hashlib.sha256(
            _canonical_csv_excluding_transport_provenance(data, label)
        ).hexdigest()
    elif logical_path == FORWARD_HOLDOUT_V2_REPLAY_SOURCE_REL:
        semantic_digest = lambda data, label: _promotion_semantic_source_sha256(
            _frame_from_csv_bytes(data, label)
        )
    elif logical_path == SOURCE_PROJECTION_MANIFEST_REL:
        semantic_digest = (
            lambda data, label: _projection_manifest_promotion_semantic_sha256(
                _frame_from_csv_bytes(data, label)
            )
        )
    elif logical_path in frame_names:
        frame_name = frame_names[logical_path]
        semantic_digest = lambda data, label: _promotion_semantic_frame_sha256(
            _frame_from_csv_bytes(data, label),
            frame_name=frame_name,
        )
    if semantic_digest is not None:
        if semantic_digest(worktree_data, logical_path) != semantic_digest(
            committed_data,
            f"HEAD:{logical_path}",
        ):
            raise RuntimeError(
                f"readiness sync source has semantic drift from HEAD: {logical_path}"
            )
        diagnostic = None
        if worktree_data != committed_data:
            diagnostic = (
                "raw-byte or legacy-envelope diagnostic only "
                f"(promotion semantics match HEAD): {logical_path}"
            )
        return committed_data, diagnostic
    canonical = _canonical_csv if csv_source else _canonical_markdown
    if canonical(worktree_data, logical_path) != canonical(
        committed_data,
        f"HEAD:{logical_path}",
    ):
        raise RuntimeError(
            f"readiness sync source has semantic drift from HEAD: {logical_path}"
        )
    diagnostic = None
    if worktree_data != committed_data:
        diagnostic = (
            f"raw-byte diagnostic only (canonical semantics match HEAD): {logical_path}"
        )
    return committed_data, diagnostic


def _bulk_committed_registered_price_sources(
    repo: Path,
    logical_paths: list[str],
    *,
    popen_factory: Callable[..., subprocess.Popen[bytes]] | None = None,
) -> dict[str, bytes]:
    """Read registered price inputs from HEAD with one cross-platform Git call."""

    expected_paths = set(logical_paths)
    if len(expected_paths) != len(logical_paths):
        raise RuntimeError("registered price bulk read contains duplicate logical paths")
    allowed_prefix = f"{PRICE_HISTORY_DIR_REL}/"
    for logical_path in expected_paths:
        if logical_path != PRICE_RESOLUTION_REL and not (
            logical_path.startswith(allowed_prefix)
            and logical_path.endswith(".csv")
        ):
            raise RuntimeError(
                f"unsafe registered price bulk-read path: {logical_path}"
            )
        if (
            "\\" in logical_path
            or ".." in Path(logical_path).parts
            or any(character in logical_path for character in ("\n", "\r", "\0", ":"))
        ):
            raise RuntimeError(
                f"unsafe registered price bulk-read path: {logical_path}"
            )

    process_factory = subprocess.Popen if popen_factory is None else popen_factory
    child_env = dict(os.environ)
    child_env["GIT_NO_REPLACE_OBJECTS"] = "1"
    process = process_factory(
        [
            "git",
            "--no-replace-objects",
            "cat-file",
            "--batch",
        ],
        cwd=repo,
        env=child_env,
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    ordered_paths = sorted(expected_paths)
    query = b"".join(
        f"HEAD:{logical_path}\n".encode("utf-8")
        for logical_path in ordered_paths
    )
    stdout, stderr_bytes = process.communicate(input=query)
    if process.returncode:
        stderr = stderr_bytes.decode("utf-8", errors="replace").strip()
        raise RuntimeError(
            "cannot bulk-read committed registered price inputs: "
            + (stderr or "git cat-file --batch failed")
        )

    committed: dict[str, bytes] = {}
    stream = io.BytesIO(stdout)
    for logical_path in ordered_paths:
        header = stream.readline()
        if not header.endswith(b"\n"):
            raise RuntimeError(
                "malformed committed registered price batch header: "
                f"{logical_path}"
            )
        parts = header[:-1].split(b" ")
        if len(parts) == 2 and parts[1] == b"missing":
            raise RuntimeError(
                f"committed registered price source is missing: {logical_path}"
            )
        if len(parts) != 3:
            raise RuntimeError(
                "malformed committed registered price batch header: "
                f"{logical_path}/{header!r}"
            )
        object_id, object_type, raw_size = parts
        if (
            re.fullmatch(rb"[0-9a-f]{40}(?:[0-9a-f]{24})?", object_id) is None
            or object_type != b"blob"
            or not raw_size.isdigit()
        ):
            raise RuntimeError(
                "committed registered price batch entry is not an exact blob: "
                f"{logical_path}/{header!r}"
            )
        size = int(raw_size)
        data = stream.read(size)
        if len(data) != size or stream.read(1) != b"\n":
            raise RuntimeError(
                "malformed committed registered price batch payload: "
                f"{logical_path}"
            )
        committed[logical_path] = data
    if stream.read(1) != b"":
        raise RuntimeError(
            "committed registered price batch returned unexpected extra output"
        )
    for logical_path, committed_data in committed.items():
        try:
            worktree_data = (repo / logical_path).read_bytes()
        except OSError as exc:
            raise RuntimeError(
                f"missing readiness sync source {logical_path}: {exc}"
            ) from exc
        if _canonical_csv(worktree_data, logical_path) != _canonical_csv(
            committed_data,
            f"HEAD:{logical_path}",
        ):
            raise RuntimeError(
                "readiness sync source has semantic drift from HEAD: "
                f"{logical_path}"
            )
    return committed


def _frame_from_csv_bytes(data: bytes, source_name: str) -> pd.DataFrame:
    fieldnames, rows = _parse_csv_bytes(data, source_name)
    return pd.DataFrame(rows, columns=fieldnames).fillna("")


def _markdown_cell(value: Any) -> str:
    return safe_str(value).replace("|", "/").replace("\n", " ")


def _parse_markdown_status_table(
    data: bytes,
    source_name: str,
) -> tuple[list[str], list[list[str]]]:
    text = _canonical_markdown(data, source_name).decode("utf-8")
    lines = text.splitlines()
    try:
        heading_index = lines.index("## Status Table")
    except ValueError as exc:
        raise RuntimeError(
            f"committed readiness Markdown missing Status Table: {source_name}"
        ) from exc
    table_lines = [line for line in lines[heading_index + 1 :] if line.strip()]
    if len(table_lines) < 2:
        raise RuntimeError(
            f"committed readiness Markdown malformed Status Table: {source_name}"
        )

    def split_row(line: str) -> list[str]:
        stripped = line.strip()
        if not stripped.startswith("|") or not stripped.endswith("|"):
            raise RuntimeError(
                f"committed readiness Markdown malformed table row: {source_name}"
            )
        return [cell.strip() for cell in stripped[1:-1].split("|")]

    header = split_row(table_lines[0])
    separator = split_row(table_lines[1])
    if len(separator) != len(header) or any(
        not re.fullmatch(r":?-{3,}:?", cell) for cell in separator
    ):
        raise RuntimeError(
            f"committed readiness Markdown malformed table separator: {source_name}"
        )
    rows: list[list[str]] = []
    for line in table_lines[2:]:
        if line.startswith("## "):
            break
        if not line.strip().startswith("|"):
            break
        cells = split_row(line)
        if len(cells) != len(header):
            raise RuntimeError(
                f"committed readiness Markdown Status Table width drift: {source_name}"
            )
        rows.append(cells)
    return header, rows


def validate_markdown_status_table_matches_csv(
    markdown_data: bytes,
    readiness: pd.DataFrame,
    *,
    source_name: str,
) -> None:
    columns = [column for column in STATUS_TABLE_COLUMNS if column in readiness.columns]
    header, rows = _parse_markdown_status_table(markdown_data, source_name)
    if header != columns:
        raise RuntimeError(
            f"committed readiness Markdown Status Table header drift: {source_name}"
        )
    expected_rows = [
        [_markdown_cell(row.get(column)) for column in columns]
        for _, row in readiness.iterrows()
    ]
    if rows != expected_rows:
        raise RuntimeError(
            "committed readiness Markdown Status Table disagrees with canonical CSV: "
            f"{source_name}"
        )


def load_committed_inputs(
    repo: Path,
) -> tuple[
    pd.DataFrame,
    pd.DataFrame,
    pd.DataFrame,
    pd.DataFrame,
    pd.DataFrame,
    pd.DataFrame,
    pd.DataFrame,
    pd.DataFrame,
    list[str],
]:
    committed: dict[str, bytes] = {}
    diagnostics: list[str] = []
    for logical_path in READINESS_MIRROR_RELS:
        data, diagnostic = _committed_semantic_source(
            repo,
            logical_path,
            csv_source=logical_path.endswith(".csv"),
        )
        committed[logical_path] = data
        if diagnostic:
            diagnostics.append(diagnostic)
    for logical_path in CANONICAL_SOURCE_RELS:
        data, diagnostic = _committed_semantic_source(
            repo,
            logical_path,
            csv_source=True,
        )
        committed[logical_path] = data
        if diagnostic:
            diagnostics.append(diagnostic)
    if _canonical_csv(
        committed[OUT_CSV_REL], OUT_CSV_REL
    ) != _canonical_csv(committed[DOCS_CSV_REL], DOCS_CSV_REL):
        raise RuntimeError("committed output/docs readiness CSV mirrors differ")
    if _canonical_markdown(
        committed[OUT_MD_REL], OUT_MD_REL
    ) != _canonical_markdown(committed[DOCS_MD_REL], DOCS_MD_REL):
        raise RuntimeError("committed output/docs readiness Markdown mirrors differ")

    base = _frame_from_csv_bytes(committed[OUT_CSV_REL], OUT_CSV_REL)
    validate_markdown_status_table_matches_csv(
        committed[OUT_MD_REL],
        base,
        source_name=OUT_MD_REL,
    )
    return (
        base,
        _frame_from_csv_bytes(committed[PROMOTION_REGISTRY_REL], PROMOTION_REGISTRY_REL),
        _frame_from_csv_bytes(committed[ANOMALY_REGISTRY_REL], ANOMALY_REGISTRY_REL),
        _frame_from_csv_bytes(
            committed[FORWARD_HOLDOUT_V2_MANIFEST_REL],
            FORWARD_HOLDOUT_V2_MANIFEST_REL,
        ),
        _frame_from_csv_bytes(
            committed[FORWARD_HOLDOUT_V2_DETAIL_REL],
            FORWARD_HOLDOUT_V2_DETAIL_REL,
        ),
        _frame_from_csv_bytes(
            committed[FORWARD_HOLDOUT_V2_SUMMARY_REL],
            FORWARD_HOLDOUT_V2_SUMMARY_REL,
        ),
        _frame_from_csv_bytes(
            committed[FORWARD_HOLDOUT_V2_REPLAY_SOURCE_REL],
            FORWARD_HOLDOUT_V2_REPLAY_SOURCE_REL,
        ),
        _frame_from_csv_bytes(
            committed[SOURCE_PROJECTION_MANIFEST_REL],
            SOURCE_PROJECTION_MANIFEST_REL,
        ),
        diagnostics,
    )


def validate_base_readiness(frame: pd.DataFrame) -> None:
    columns = tuple(frame.columns)
    if columns not in {LEGACY_COLUMNS, TARGET_COLUMNS}:
        raise RuntimeError(
            "committed readiness schema drift: expected exact legacy or revenue-extended "
            f"schema, got {list(columns)}"
        )
    if frame.empty:
        raise RuntimeError("committed readiness CSV is empty")
    model_ids = frame["model_id"].astype(str)
    if model_ids.str.strip().eq("").any():
        raise RuntimeError("committed readiness contains a blank model_id")
    duplicate_ids = sorted(model_ids[model_ids.duplicated(keep=False)].unique().tolist())
    if duplicate_ids:
        raise RuntimeError(
            f"committed readiness contains duplicate model_id values: {duplicate_ids}"
        )
    if int(model_ids.eq(MODEL_ID).sum()) != 1:
        raise RuntimeError(f"committed readiness must contain exactly one {MODEL_ID} row")
    for field_name in ("approved_for_daily", "presentation_allowed"):
        invalid = sorted(set(frame[field_name].astype(str)) - {"True", "False"})
        if invalid:
            raise RuntimeError(
                f"committed readiness {field_name} has non-canonical values: {invalid}"
            )

    if columns == TARGET_COLUMNS:
        revenue_mask = model_ids.eq(MODEL_ID)
        for field_name in sorted(REVENUE_PERMISSION_COLUMNS):
            values = frame[field_name].astype(str)
            if not values[revenue_mask].eq("False").all():
                raise RuntimeError(
                    f"committed {MODEL_ID} readiness {field_name} must be explicit False"
                )
            conflicting = frame.loc[~revenue_mask & values.ne(""), "model_id"]
            if not conflicting.empty:
                raise RuntimeError(
                    f"committed readiness {field_name} is revenue-only; non-revenue "
                    f"rows must remain neutral blank: {sorted(conflicting.tolist())}"
                )


def build_revenue_only_readiness(
    base: pd.DataFrame,
    revenue_summary: dict[str, Any],
    *,
    generated_at: str,
) -> pd.DataFrame:
    validate_base_readiness(base)
    if set(revenue_summary) != SUMMARY_COLUMNS:
        missing = sorted(SUMMARY_COLUMNS - set(revenue_summary))
        extra = sorted(set(revenue_summary) - SUMMARY_COLUMNS)
        raise RuntimeError(
            f"revenue readiness summary schema drift: missing={missing}; extra={extra}"
        )

    out = base.copy()
    if tuple(out.columns) == LEGACY_COLUMNS:
        out.insert(
            out.columns.get_loc("approved_for_daily"),
            "formal_model_use_allowed",
            "",
        )
        out.insert(
            out.columns.get_loc("presentation_allowed") + 1,
            "production_allowed",
            "",
        )
    if tuple(out.columns) != TARGET_COLUMNS:
        raise RuntimeError("revenue readiness target column order is not canonical")

    revenue_mask = out["model_id"].astype(str).eq(MODEL_ID)
    revenue_index = out.index[revenue_mask][0]
    preserved_model_name = str(out.at[revenue_index, "model_name_zh"])
    replacement = {
        "generated_at": generated_at,
        "model_id": MODEL_ID,
        "model_name_zh": preserved_model_name,
        **{
            field_name: "" if value is None else str(value)
            for field_name, value in revenue_summary.items()
        },
    }
    out.loc[revenue_index, list(TARGET_COLUMNS)] = [
        replacement[field_name] for field_name in TARGET_COLUMNS
    ]

    base_non_revenue = base.loc[~revenue_mask].reset_index(drop=True)
    out_non_revenue = out.loc[~revenue_mask].reset_index(drop=True)
    for field_name in LEGACY_COLUMNS:
        if not out_non_revenue[field_name].equals(base_non_revenue[field_name]):
            raise RuntimeError(
                f"revenue-only readiness sync changed non-revenue field {field_name}"
            )
    for field_name in sorted(REVENUE_PERMISSION_COLUMNS):
        if not out_non_revenue[field_name].astype(str).eq("").all():
            raise RuntimeError(
                f"revenue-only readiness sync populated non-revenue field {field_name}"
            )
    validate_base_readiness(out)
    return out


def render_markdown(readiness: pd.DataFrame, *, generated_at: str) -> bytes:
    lines: list[str] = [
        "# Model Operation Readiness",
        "",
        f"- generated_at: `{generated_at}`",
        "- purpose: track model parity, operation-module readiness, daily adapter status, and promotion boundaries",
        "- rule: `approved_for_daily=True` requires an explicit approved operation artifact",
        "- rule: raw research evidence rows can remain research-only even after an operation module is approved",
        "- rule: PDF/packet integration 必須 render adapter artifact，不得重新計算操作規則",
        "",
    ]
    summary_cols = [
        "operation_module_status",
        "daily_adapter_status",
        "formal_model_use_allowed",
        "approved_for_daily",
        "presentation_allowed",
        "production_allowed",
    ]
    for field_name in summary_cols:
        counts = readiness[field_name].value_counts().reset_index()
        counts.columns = [field_name, "count"]
        lines.extend(
            [
                f"## {field_name}",
                "",
                markdown_table(counts, [field_name, "count"]),
                "",
            ]
        )

    show_cols = list(STATUS_TABLE_COLUMNS)
    lines.extend(
        [
            "## Status Table",
            "",
            markdown_table(readiness, show_cols, limit=200),
            "",
        ]
    )
    return ("\n".join(lines).rstrip() + "\n").encode("utf-8")


def write_readiness_mirrors(
    repo: Path,
    readiness: pd.DataFrame,
    *,
    generated_at: str,
) -> None:
    csv_data = readiness.to_csv(index=False, lineterminator="\n").encode("utf-8")
    markdown_data = render_markdown(readiness, generated_at=generated_at)
    payloads = {
        OUT_CSV_REL: csv_data,
        DOCS_CSV_REL: csv_data,
        OUT_MD_REL: markdown_data,
        DOCS_MD_REL: markdown_data,
    }
    if set(payloads) != set(READINESS_MIRROR_RELS):
        raise RuntimeError("readiness sync output scope drifted from the exact four mirrors")
    for logical_path, data in payloads.items():
        path = repo / logical_path
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(data)
    if (repo / OUT_CSV_REL).read_bytes() != (repo / DOCS_CSV_REL).read_bytes():
        raise RuntimeError("written output/docs readiness CSV mirrors differ")
    if (repo / OUT_MD_REL).read_bytes() != (repo / DOCS_MD_REL).read_bytes():
        raise RuntimeError("written output/docs readiness Markdown mirrors differ")


def sync(repo: Path, *, generated_at: str | None = None) -> tuple[pd.DataFrame, list[str]]:
    repo = repo.resolve()
    (
        base,
        promotion_registry,
        anomaly_registry,
        forward_holdout_v2_manifest,
        holdout_detail,
        holdout_summary,
        replay_source,
        source_projection_manifest,
        diagnostics,
    ) = load_committed_inputs(repo)

    promotion_source, promotion_errors = validate_revenue_promotion_registry(
        repo / PROMOTION_REGISTRY_REL
    )
    anomaly_result = validate_current_anomaly_dispositions(
        repo,
        require_effective_nonblocking=True,
    )
    anomaly_errors = anomaly_result.errors
    source_errors = [
        *(f"promotion source: {error}" for error in promotion_errors),
        *(f"anomaly source: {error}" for error in anomaly_errors),
    ]
    if source_errors:
        raise RuntimeError("; ".join(source_errors))
    if promotion_source is None:
        raise RuntimeError("promotion source validation returned no current decision")
    _promotion_profile_for_row(promotion_source)

    revenue_summary = summarize_revenue_promotion_readiness(
        promotion_registry,
        anomaly_registry,
        forward_holdout_v2_manifest,
        holdout_detail=holdout_detail,
        holdout_summary=holdout_summary,
        replay_source=replay_source,
        source_projection_manifest=source_projection_manifest,
        repo_root=repo,
        diagnostics=diagnostics,
        anomaly_result=anomaly_result,
    )
    generated = generated_at or now_text()
    readiness = build_revenue_only_readiness(
        base,
        revenue_summary,
        generated_at=generated,
    )
    validate_revenue_readiness_exact_replay(
        forward_holdout_v2_manifest,
        holdout_detail=holdout_detail,
        holdout_summary=holdout_summary,
        replay_source=replay_source,
        repo_root=repo,
    )
    write_readiness_mirrors(repo, readiness, generated_at=generated)
    return readiness, diagnostics


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo-root", type=Path, default=Path("."))
    args = parser.parse_args()
    try:
        readiness, diagnostics = sync(args.repo_root)
    except RuntimeError as exc:
        print(f"ERROR: {exc}")
        return 1
    for diagnostic in diagnostics:
        print(f"DIAGNOSTIC: {diagnostic}")
    print(
        "Saved exact four revenue-only readiness mirrors; "
        f"rows={len(readiness)}; model_id={MODEL_ID}."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
