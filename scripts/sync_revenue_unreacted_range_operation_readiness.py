from __future__ import annotations

import argparse
import csv
from decimal import Decimal, InvalidOperation
import hashlib
import io
import json
import math
import numbers
import re
import subprocess
import sys
from pathlib import Path
from typing import Any

import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent))

from tracking_utils import markdown_table, now_text, safe_str  # noqa: E402


MODEL_ID = "revenue_unreacted_range"
REVENUE_MODEL_ID = MODEL_ID
REVENUE_EXPECTED_PROMOTION_DECISION = {
    "contract_version": (
        "revenue_unreacted_range_promotion_preparation_contract_v4_20260828"
    ),
    "decision_status": (
        "research_complete_promotion_blocked_waiting_anomaly_forward_holdout_and_"
        "formal_adapter"
    ),
    "anomaly_disposition_gate": (
        "research_non_hard_promotion_candidate_hard_pending_9_root_cause_"
        "dispositions"
    ),
    "formal_adapter_gate": (
        "disabled_adapter_preparation_non_hard_production_approval_hard_gate"
    ),
    "promotion_scope": (
        "staged_contract_research_only_and_disabled_adapter_preparation_no_"
        "production_daily_full_pdf_or_apps_script"
    ),
}
REVENUE_PROMOTION_CONTRACT_VERSION = (
    REVENUE_EXPECTED_PROMOTION_DECISION["contract_version"]
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
    "research_matrix_complete_formal_adapter_not_started"
)
REVENUE_ANOMALY_DISPOSITION_POLICIES = {
    "unresolved_anomaly_candidate": (
        "retain_in_primary_metrics_and_allow_exclusion_sensitivity_only",
        "blocked_pending_root_cause",
    ),
    "verified_real_extreme": (
        "retain_in_primary_metrics",
        "eligible_only_after_all_other_model_gates",
    ),
    "verified_data_error": (
        "repair_source_and_rerun_old_metrics_forbidden",
        "blocked_until_repaired_rerun",
    ),
    "verified_non_comparable": (
        "exclude_only_with_approved_reason_and_rerun",
        "requires_model_governance_review",
    ),
}
REVENUE_EXPECTED_ANOMALIES = {
    "rearm_after_realized_exit_next_trade_day|delayed_next_close_continuation_bonus|2408|absolute_or_two_month_yoy_ge15|2408|20260417|2|20260427|20260429": "8642cd7286a0eee22ba76d69e6ab826c9ec22c3e83a3ed63fef27753e81f0168",
    "rearm_after_realized_exit_next_trade_day|delayed_next_close_continuation_bonus|2451|absolute_or_two_month_yoy_ge15|2451|20250517|1|20260313|20260317": "e5eed6f2f6d39d9da369041116395383580ef98274e7490bcaadc6a23a22d20e",
    "rearm_after_realized_exit_next_trade_day|delayed_next_close_continuation_bonus|2478|absolute_or_two_month_yoy_ge15|2478|20260217|2|20260416|20260420": "facf4234439f7b5627a00b3bfa82c2976559357c218b0a341ca0a5a0e2d53a9b",
    "rearm_after_realized_exit_next_trade_day|delayed_next_close_continuation_bonus|2527|absolute_or_two_month_yoy_ge15|2527|20260517|1|20260526|20260528": "34d2b8aa9258ae1a686feaa937ada66e56c238c7dd5994299b4a3c74ee5d8c6a",
    "rearm_after_realized_exit_next_trade_day|delayed_next_close_continuation_bonus|3535|absolute_or_two_month_yoy_ge15|3535|20251017|1|20251128|20251202": "f7ed7ce96221e2754d299f73ee1025763d7d8b858b19232c18a4e3b21032c5c2",
    "rearm_after_realized_exit_next_trade_day|delayed_next_close_continuation_bonus|3535|absolute_or_two_month_yoy_ge15|3535|20251017|1|20260119|20260121": "e4b00d986b4af400e6cc05ce38687964f7de9944914d77eb31fc0a9755a64596",
    "rearm_after_realized_exit_next_trade_day|delayed_next_close_continuation_bonus|4142|absolute_or_two_month_yoy_ge15|4142|20250617|1|20260109|20260113": "2f36fb8d8e6bd05b879a164e5748d318088ebc6936d1d97dc9a9cd728c0bc35b",
    "rearm_after_realized_exit_next_trade_day|delayed_next_close_continuation_bonus|5484|absolute_or_two_month_yoy_ge15|5484|20251017|1|20260515|20260519": "5f3ca72b872eeb3f02e078e9544b456751e6dc2c4fc7942a7a023c961a6ce514",
    "rearm_after_realized_exit_next_trade_day|delayed_next_close_continuation_bonus|6177|absolute_or_two_month_yoy_ge15|6177|20250517|1|20251204|20251208": "e3ff0aa0f2af328e8e959321235acc79af9efdf0a7df508db4d55bac57b88e23",
}

PREREGISTRATION_PR_NUMBER = "462"
PREREGISTRATION_MERGE_COMMIT = "436c25cd0d037c3425ab2ac4fa76cb464cf96de4"
RULE_CONTRACT_VERSION = "revenue_low_mid_falling_forward_holdout_rule_v2"
RULE_CANONICAL_SHA256 = (
    "3918b336ff995b9a8f1425cd48cc51a84c8c015a58e81668f357ca048145f9e3"
)
DATA_CONTRACT_VERSION = "revenue_low_mid_falling_forward_holdout_data_v2_20260828"
DATA_CONTRACT_SHA256 = (
    "c2d70f73c6b9b5f097529852c7e35e58224c5dab2ee84762d13e9fe74ad7316b"
)
TRAINING_CUTOFF_DATE = "20260713"
BRIDGE_START_DATE = "20260714"
BRIDGE_END_DATE = "20260830"
HOLDOUT_START_DATE = REVENUE_FORWARD_HOLDOUT_V2_START_DATE
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
PRIMARY_VARIANT_ID = REVENUE_SOURCE_VARIANT_ID
ALL_VARIANT_IDS = (
    PRIMARY_VARIANT_ID,
    "source_low_falling",
    "source_low_or_mid_falling_union",
)
SOURCE_VARIANT_ID = "absolute_or_two_month_yoy_ge15"
MONTHLY_LINEAGE_COLUMNS = (
    "monthly_revenue_history_blob_sha256",
    "monthly_revenue_canonical_table_sha256",
    "cross_market_resolution_registry_canonical_sha256",
)
CANONICAL_LINEAGE_VERSION = "canonical_json_numeric_text_v1"
PROMOTION_REGISTRY_CANONICAL_SHA256 = (
    "dbe1fbfc2b02801a25afee4a0eda2aaf6b464f2334282c5109141c7f1023419b"
)
ANOMALY_REGISTRY_CANONICAL_SHA256 = (
    "109fc2f15e8f82e7644df677a8f4e92ebbe03ede960753267d46587c882afedc"
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

PROMOTION_REGISTRY_REL = (
    "config/revenue_unreacted_range_promotion_preparation_registry.csv"
)
ANOMALY_REGISTRY_REL = (
    "config/revenue_unreacted_range_anomaly_disposition_registry_v2_20260828.csv"
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
FORWARD_HOLDOUT_V2_REPLAY_SOURCE_REL = (
    "output/latest/research_backtest/"
    "revenue_unreacted_range_forward_holdout_v2_replay_source_detail_latest.csv"
)
SOURCE_PROJECTION_MANIFEST_REL = (
    "output/latest/research_backtest/"
    "revenue_unreacted_range_source_snapshot_projection_manifest_latest.csv"
)
CANONICAL_SOURCE_RELS = (
    PROMOTION_REGISTRY_REL,
    ANOMALY_REGISTRY_REL,
    FORWARD_HOLDOUT_V2_MANIFEST_REL,
    FORWARD_HOLDOUT_V2_DETAIL_REL,
    FORWARD_HOLDOUT_V2_SUMMARY_REL,
    FORWARD_HOLDOUT_V2_REPLAY_SOURCE_REL,
    SOURCE_PROJECTION_MANIFEST_REL,
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


def _canonical_frame_sha256(frame: pd.DataFrame) -> str:
    columns = sorted(column for column in frame.columns if column != "generated_at")
    rows = [
        [_canonical_value(value) for value in row]
        for row in frame.loc[:, columns].itertuples(index=False, name=None)
    ]
    rows.sort()
    return _canonical_json_sha256([CANONICAL_LINEAGE_VERSION, columns, rows])


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


def _validate_selected_v2_manifest(source_manifest: pd.DataFrame) -> None:
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
    observed_sha = _canonical_frame_sha256(source_manifest)
    if observed_sha != SELECTED_V2_MANIFEST_CANONICAL_SHA256:
        raise RuntimeError(
            "forward holdout v2 selected manifest canonical SHA-256 drift: "
            f"expected={SELECTED_V2_MANIFEST_CANONICAL_SHA256} observed={observed_sha}"
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


def _validate_holdout_manifest_lineage(
    manifest: pd.DataFrame,
    detail: pd.DataFrame,
    summary: pd.DataFrame,
    replay_source: pd.DataFrame,
    source_projection_manifest: pd.DataFrame,
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
        "price_input_canonical_sha256",
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
        row.get("training_source_projection_semantic_sha256"),
        "holdout.training_source_projection_semantic_sha256",
        expected=PROJECTED_EPISODE_SEMANTIC_SHA256,
    )
    _require_sha(
        row.get("training_source_manifest_canonical_sha256"),
        "holdout.training_source_manifest_canonical_sha256",
        expected=SELECTED_V2_MANIFEST_CANONICAL_SHA256,
    )
    for field_name in (
        "source_detail_canonical_sha256",
        "monthly_revenue_history_blob_sha256",
        "monthly_revenue_canonical_table_sha256",
        "cross_market_resolution_registry_canonical_sha256",
        "price_input_canonical_sha256",
        "capture_id",
    ):
        _require_sha(row.get(field_name), f"holdout.{field_name}")
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
        _validate_selected_v2_manifest(source_projection_manifest)
    except RuntimeError as exc:
        raise RuntimeError(f"revenue readiness selected v2 source manifest invalid: {exc}") from exc

    normalized_source = _normalize_replay_source(replay_source).reset_index(
        drop=True
    )
    expected_source_rows = _strict_nonnegative_int(
        row.get("source_detail_row_count"), "holdout.source_detail_row_count"
    )
    if len(normalized_source) != expected_source_rows:
        raise RuntimeError(
            "revenue readiness holdout source detail row count drift: "
            f"manifest={expected_source_rows} replay={len(normalized_source)}"
        )
    observed_source_sha = _canonical_frame_sha256(normalized_source)
    expected_source_sha = safe_str(row.get("source_detail_canonical_sha256"))
    if observed_source_sha != expected_source_sha:
        raise RuntimeError(
            "revenue readiness holdout source detail canonical SHA drift: "
            f"manifest={expected_source_sha} replay={observed_source_sha}"
        )
    for field_name in MONTHLY_LINEAGE_COLUMNS:
        values = set(normalized_source[field_name].astype(str))
        expected = safe_str(row.get(field_name))
        if values != {expected}:
            raise RuntimeError(
                f"revenue readiness holdout {field_name} disagrees with replay source"
            )

    observed_through = _strict_date(
        row.get("observed_through_date"), "holdout.observed_through_date"
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
        "source_detail_canonical_sha256": expected_source_sha,
        "price_input_canonical_sha256": safe_str(
            row.get("price_input_canonical_sha256")
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
    if safe_str(row.get("capture_id")) != observed_capture:
        raise RuntimeError("revenue readiness holdout capture_id canonical SHA drift")

    detail_required = {
        "model_id",
        "artifact_id",
        "artifact_version",
        "capture_id",
        "variant_id",
        "trigger_date",
        "source_asof_date",
        "source_asof_trade_date",
        "source_asof_canonical_source_table_date",
        "return_valid",
        "right_censored",
        "realized_return_pct",
        "return_outcome",
        "primary_metric_included",
        "event_row_canonical_sha256",
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
        "capture_id": safe_str(row.get("capture_id")),
        "financial_statement_scope": REVENUE_HOLDOUT_FINANCIAL_STATEMENT_SCOPE,
    }.items():
        if not detail[field_name].astype(str).eq(expected).all():
            raise RuntimeError(
                f"revenue readiness holdout detail {field_name} drift"
            )
    if not set(detail["variant_id"].astype(str)).issubset(
        set(ALL_VARIANT_IDS)
    ):
        raise RuntimeError("revenue readiness holdout detail variant set drift")
    mature_mask = _bool_series(detail, "return_valid")
    censored_mask = _bool_series(detail, "right_censored")
    if (mature_mask & censored_mask).any():
        raise RuntimeError("revenue readiness holdout row cannot be mature and right-censored")
    if not detail.empty:
        if (~_bool_series(detail, "primary_metric_included")).any():
            raise RuntimeError("revenue readiness holdout detail left primary metrics")
        for row_index, event in detail.iterrows():
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
                raise RuntimeError("revenue readiness holdout event row canonical SHA drift")
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
        variant_detail = detail[detail["variant_id"].astype(str).eq(variant_id)]
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
    primary_detail = detail[
        detail["variant_id"].astype(str).eq(PRIMARY_VARIANT_ID)
    ]
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


def validate_revenue_readiness_source_files(
    repo_root: Path | str = Path("."),
) -> list[str]:
    root = Path(repo_root)
    _, promotion_errors = validate_revenue_promotion_registry(
        root / REVENUE_PROMOTION_REGISTRY_CSV
    )
    _, anomaly_errors = validate_revenue_anomaly_registry(
        root / REVENUE_ANOMALY_REGISTRY_CSV,
        expected_anomalies=REVENUE_EXPECTED_ANOMALIES,
        version_label="v2",
    )
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
        )
    except (OSError, pd.errors.ParserError, RuntimeError) as exc:
        errors.append(f"revenue readiness holdout source: {exc}")
    return errors


def summarize_revenue_promotion_readiness(
    promotion_registry: pd.DataFrame,
    anomaly_registry: pd.DataFrame,
    forward_holdout_v2_manifest: pd.DataFrame,
    *,
    holdout_detail: pd.DataFrame,
    holdout_summary: pd.DataFrame,
    replay_source: pd.DataFrame,
    source_projection_manifest: pd.DataFrame,
) -> dict[str, Any]:
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
    expected_promotion = {
        "contract_version": REVENUE_PROMOTION_CONTRACT_VERSION,
        "candidate_variant_id": REVENUE_SOURCE_VARIANT_ID,
        "financial_statement_scope": REVENUE_PROMOTION_FINANCIAL_STATEMENT_SCOPE,
        **{
            field_name: REVENUE_EXPECTED_PROMOTION_DECISION[field_name]
            for field_name in (
                "decision_status",
                "anomaly_disposition_gate",
                "promotion_scope",
            )
        },
    }
    for field_name, expected in expected_promotion.items():
        observed = safe_str(promotion.get(field_name))
        if observed != expected:
            if field_name == "contract_version":
                raise RuntimeError(
                    "revenue readiness requires latest decision v3 / promotion contract "
                    f"v4; got {observed!r}"
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

    anomaly_required = {
        "model_id",
        "operation_key",
        "candidate_detail_row_sha256",
        "final_disposition",
        "primary_handling",
        "promotion_gate_status",
    }
    _required_columns(anomaly_registry, anomaly_required, str(REVENUE_ANOMALY_REGISTRY_CSV))
    anomaly_rows = anomaly_registry[
        anomaly_registry["model_id"].astype(str).eq(MODEL_ID)
    ].copy()
    if anomaly_rows.empty:
        raise RuntimeError("revenue anomaly registry has no model rows")
    if anomaly_rows["operation_key"].astype(str).str.strip().eq("").any():
        raise RuntimeError("revenue anomaly registry contains blank operation_key")
    if anomaly_rows["candidate_detail_row_sha256"].astype(str).map(
        lambda value: SHA256_RE.fullmatch(value) is not None
    ).ne(True).any():
        raise RuntimeError("revenue anomaly registry contains invalid row SHA")
    latest_anomalies = anomaly_rows.drop_duplicates(
        subset=["operation_key"], keep="last"
    )
    if len(latest_anomalies) != candidate_count:
        raise RuntimeError("revenue anomaly count disagrees with promotion row")
    invalid_dispositions = sorted(
        set(latest_anomalies["final_disposition"].astype(str))
        - set(REVENUE_ANOMALY_DISPOSITION_POLICIES)
    )
    if invalid_dispositions:
        raise RuntimeError(
            f"revenue anomaly registry has invalid dispositions: {invalid_dispositions}"
        )
    for _, anomaly in latest_anomalies.iterrows():
        disposition = safe_str(anomaly.get("final_disposition"))
        expected_policy = REVENUE_ANOMALY_DISPOSITION_POLICIES[disposition]
        actual_policy = (
            safe_str(anomaly.get("primary_handling")),
            safe_str(anomaly.get("promotion_gate_status")),
        )
        if actual_policy != expected_policy:
            raise RuntimeError(
                f"revenue anomaly disposition policy mismatch: "
                f"{safe_str(anomaly.get('operation_key'))}"
            )
    unresolved_rows = latest_anomalies[
        latest_anomalies["final_disposition"]
        .astype(str)
        .eq("unresolved_anomaly_candidate")
    ]
    unresolved_count = len(unresolved_rows)
    non_blocking_gate = REVENUE_ANOMALY_DISPOSITION_POLICIES[
        "verified_real_extreme"
    ][1]
    blocking_anomaly_count = int(
        latest_anomalies["promotion_gate_status"]
        .astype(str)
        .ne(non_blocking_gate)
        .sum()
    )

    holdout = _validate_holdout_manifest_lineage(
        forward_holdout_v2_manifest,
        holdout_detail,
        holdout_summary,
        replay_source,
        source_projection_manifest,
    )
    mature_count = _strict_nonnegative_int(
        holdout.get("primary_mature_count"), "holdout.primary_mature_count"
    )
    expected_adapter_gate = REVENUE_EXPECTED_PROMOTION_DECISION[
        "formal_adapter_gate"
    ]
    if safe_str(promotion.get("formal_adapter_gate")) != expected_adapter_gate:
        raise RuntimeError("revenue readiness formal adapter gate drift")
    blocker = (
        f"anomaly_disposition_blockers={blocking_anomaly_count}; "
        f"unresolved_anomalies={unresolved_count}; "
        f"forward_holdout_v2_mature={mature_count}/{minimum_mature}; "
        "formal_adapter=not_started"
    )
    return {
        "parity_status": REVENUE_RESEARCH_MATRIX_STATUS,
        "blocker": blocker,
        "operation_module_status": REVENUE_OPERATION_MODULE_STATUS,
        "daily_adapter_status": "not_started",
        "formal_model_use_allowed": "False",
        "approved_for_daily": "False",
        "approval_status": "not_started",
        "operation_module_id": "",
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
        "status_note_zh": (
            "revenue_unreacted_range／source_mid_falling v2 的模型專屬研究矩陣已完成；"
            f"目前仍有 {blocking_anomaly_count} 筆 anomaly disposition 阻擋項目（其中 "
            f"{unresolved_count} 筆尚未定案）、forward holdout v2 "
            f"成熟度 {mature_count}/{minimum_mature} 與 disabled formal adapter preparation 尚未完成。"
            "月營收以外的 EPS、毛利率、營益率、營業利益、業外損益、淨利及季度／年度財報欄位均不在模型範圍；"
            "不得產生 production、PDF、packet 或操作指令。"
        ),
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


def _registry_semantic_sha256(path: Path) -> str:
    data = path.read_bytes()
    return hashlib.sha256(_canonical_csv(data, str(path))).hexdigest()


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
    if observed_sha != PROMOTION_REGISTRY_CANONICAL_SHA256:
        errors.append(
            "promotion preparation registry canonical semantic SHA-256 drift: "
            f"expected={PROMOTION_REGISTRY_CANONICAL_SHA256}; actual={observed_sha}"
        )
    if not rows:
        return None, [*errors, "promotion preparation registry is empty"]
    latest = rows[-1]
    for field_name, expected in REVENUE_EXPECTED_PROMOTION_DECISION.items():
        if latest.get(field_name, "") != expected:
            errors.append(
                f"promotion preparation {field_name} mismatch in latest staged row"
            )
    return latest, errors


def validate_revenue_anomaly_registry(
    path: Path,
    *,
    expected_anomalies: dict[str, str] = REVENUE_EXPECTED_ANOMALIES,
    version_label: str = "v2",
) -> tuple[dict[str, dict[str, str]], list[str]]:
    errors: list[str] = []
    try:
        fieldnames, rows = _parse_csv_bytes(path.read_bytes(), str(path))
        del fieldnames
        observed_sha = _registry_semantic_sha256(path)
    except (OSError, RuntimeError) as exc:
        return {}, [str(exc)]
    if observed_sha != ANOMALY_REGISTRY_CANONICAL_SHA256:
        errors.append(
            "anomaly disposition registry canonical semantic SHA-256 drift: "
            f"expected={ANOMALY_REGISTRY_CANONICAL_SHA256}; actual={observed_sha}"
        )
    actual = {row.get("operation_key", ""): row for row in rows}
    if len(actual) != len(rows):
        errors.append("anomaly disposition registry has duplicate operation_key rows")
    if set(actual) != set(expected_anomalies):
        errors.append(
            f"anomaly disposition registry {version_label} operation-key set drift"
        )
    for operation_key, expected_sha in expected_anomalies.items():
        row = actual.get(operation_key)
        if row is None:
            continue
        if row.get("candidate_detail_row_sha256", "") != expected_sha:
            errors.append(
                f"{operation_key}: candidate_detail_row_sha256 mismatch"
            )
        disposition = row.get("final_disposition", "")
        expected_policy = REVENUE_ANOMALY_DISPOSITION_POLICIES.get(disposition)
        if expected_policy is None:
            errors.append(f"{operation_key}: invalid final_disposition={disposition!r}")
        elif (
            row.get("primary_handling", ""),
            row.get("promotion_gate_status", ""),
        ) != expected_policy:
            errors.append(
                f"{operation_key}: disposition policy mismatch for {disposition}"
            )
    return actual, errors


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

    _, promotion_errors = validate_revenue_promotion_registry(
        repo / PROMOTION_REGISTRY_REL
    )
    _, anomaly_errors = validate_revenue_anomaly_registry(
        repo / ANOMALY_REGISTRY_REL,
        expected_anomalies=REVENUE_EXPECTED_ANOMALIES,
        version_label="v2",
    )
    source_errors = [
        *(f"promotion source: {error}" for error in promotion_errors),
        *(f"anomaly source: {error}" for error in anomaly_errors),
    ]
    if source_errors:
        raise RuntimeError("; ".join(source_errors))

    revenue_summary = summarize_revenue_promotion_readiness(
        promotion_registry,
        anomaly_registry,
        forward_holdout_v2_manifest,
        holdout_detail=holdout_detail,
        holdout_summary=holdout_summary,
        replay_source=replay_source,
        source_projection_manifest=source_projection_manifest,
    )
    generated = generated_at or now_text()
    readiness = build_revenue_only_readiness(
        base,
        revenue_summary,
        generated_at=generated,
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
