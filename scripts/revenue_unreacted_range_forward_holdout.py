from __future__ import annotations

from decimal import Decimal, InvalidOperation
from datetime import datetime
import hashlib
import io
import json
import math
import os
from pathlib import Path
import re
import subprocess
import tempfile
from typing import Callable, Mapping
from zoneinfo import ZoneInfo

import numpy as np
import pandas as pd

from revenue_unreacted_range_forward_confirmation_feature_audit import (
    prepare_daily_by_stock,
)
from revenue_unreacted_range_low_mid_falling_candidate_audit import (
    _asof_source,
    _normalize_source,
)
from revenue_unreacted_range_rearmed_operation_grid import (
    OPERATION_RETURN_REVIEW_THRESHOLD_PCT,
)
from revenue_unreacted_range_source_first_condition_audit import (
    build_source_first_condition_audit,
)
from revenue_unreacted_range_source_snapshot_projection import (
    ARTIFACT_ID as SOURCE_PROJECTION_ARTIFACT_ID,
    ARTIFACT_VERSION as SOURCE_PROJECTION_ARTIFACT_VERSION,
    load_source_snapshot_projection_manifest,
)


ROOT = Path(__file__).resolve().parents[1]
MODEL_ID = "revenue_unreacted_range"
ARTIFACT_ID = "revenue_unreacted_range_forward_holdout"
ARTIFACT_VERSION = "forward_holdout_v1_20260811"
CANONICAL_LINEAGE_VERSION = "canonical_json_numeric_text_v1"

PREREGISTRATION_PR_NUMBER = "462"
PREREGISTRATION_MERGE_COMMIT = "436c25cd0d037c3425ab2ac4fa76cb464cf96de4"
PR462_PROJECTED_EPISODE_ROW_COUNT = 19569
PR462_PROJECTED_EPISODE_SEMANTIC_SHA256 = (
    "92c68810ac2b5718d714d450fe83bf23f2f3469fec5db0ae2753330950ab2cf5"
)
TRAINING_CUTOFF_DATE = "20260713"
BRIDGE_START_DATE = "20260714"
BRIDGE_END_DATE = "20260803"
HOLDOUT_START_DATE = "20260804"

SOURCE_ARTIFACT_ID = "revenue_unreacted_range_source_first_condition_audit"
SOURCE_ARTIFACT_VERSION = "source_first_condition_v3_20260720"
SOURCE_VARIANT_ID = "absolute_or_two_month_yoy_ge15"
PRIMARY_VARIANT_ID = "source_mid_falling"
CHALLENGER_VARIANT_IDS = (
    "source_low_falling",
    "source_low_or_mid_falling_union",
)
ALL_VARIANT_IDS = (PRIMARY_VARIANT_ID, *CHALLENGER_VARIANT_IDS)
CONFIRMATION_VARIANT_ID = "delayed_next_close_continuation_bonus"
LIFECYCLE_POLICY_ID = "rearm_after_realized_exit_next_trade_day"
BASE_CONFIRMATION_RULE_ID = "close_cross_prev20_and_ma60_gt_ma120"
CONFIRMATION_RULE_ID = "next_trading_day_close_above_trigger_close"
ENTRY_RULE_ID = "next_day_close_confirmed_following_trading_day_open"
STOP_POLICY_ID = "none_no_stop_reference"
EXIT_RULE_ID = "fixed_d30_close"
HOLDING_DAYS = 30
HOLDING_SESSION_INDEX_OFFSET = HOLDING_DAYS - 1
WATCH_HORIZON_TRADING_DAYS = 60
BASE_TRIGGER_PREVIOUS_HIGH_WINDOW_SESSIONS = 20
BASE_TRIGGER_MA_SHORT_WINDOW_SESSIONS = 60
BASE_TRIGGER_MA_LONG_WINDOW_SESSIONS = 120

POSITION_LOOKBACK_PRIOR_SESSIONS = 120
POSITION_LOW_MAX_PCT = 40.0
POSITION_MID_MAX_PCT = 75.0
SHAPE_RETURN_LOOKBACK_SESSIONS = 20
SHAPE_RANGE_WINDOW_SESSIONS = 23
SHAPE_EMA_SPAN_SESSIONS = 23
SHAPE_EMA_SLOPE_LOOKBACK_SESSIONS = 5
SHAPE_RISING_RETURN_MIN_PCT = 5.0
SHAPE_FALLING_RETURN_MAX_PCT = -5.0
SHAPE_RISING_EMA_SLOPE_MIN_PCT = 0.0
SHAPE_FALLING_EMA_SLOPE_MAX_PCT = 0.0
SHAPE_CONSOLIDATION_RETURN_ABS_MAX_PCT = 5.0
SHAPE_CONSOLIDATION_RANGE_MAX_PCT = 15.0

RULE_CONTRACT_VERSION = "revenue_low_mid_falling_forward_holdout_rule_v2"
RULE_CONTRACT = {
    "model_id": MODEL_ID,
    "source_variant_id": SOURCE_VARIANT_ID,
    "source_variant_contract": {
        "logic": "absolute_branch_or_two_consecutive_month_branch",
        "absolute_latest_yoy_min_pct_inclusive": 30.0,
        "absolute_cumulative_yoy_min_pct_inclusive": 20.0,
        "two_month_requires_consecutive_calendar_months": True,
        "two_month_latest_yoy_min_pct_inclusive": 15.0,
        "two_month_previous_latest_yoy_min_pct_inclusive": 15.0,
    },
    "primary_variant_id": PRIMARY_VARIANT_ID,
    "challenger_variant_ids": list(CHALLENGER_VARIANT_IDS),
    "position_buckets": {
        "source_low_falling": "low_pos_le40",
        "source_mid_falling": "mid_pos_40_75",
        "source_low_or_mid_falling_union": "low_pos_le40|mid_pos_40_75",
    },
    "shape_bucket": "falling",
    "position_feature_contract": {
        "lookback_prior_sessions": POSITION_LOOKBACK_PRIOR_SESSIONS,
        "anchor_included": False,
        "formula": "(anchor_analysis_close-prior_analysis_low_min)/(prior_analysis_high_max-prior_analysis_low_min)*100",
        "low_max_pct_inclusive": POSITION_LOW_MAX_PCT,
        "mid_lower_pct_exclusive": POSITION_LOW_MAX_PCT,
        "mid_max_pct_inclusive": POSITION_MID_MAX_PCT,
        "high_lower_pct_exclusive": POSITION_MID_MAX_PCT,
    },
    "shape_feature_contract": {
        "return_lookback_sessions": SHAPE_RETURN_LOOKBACK_SESSIONS,
        "return_formula": "(anchor_analysis_close/analysis_close_t_minus_20-1)*100",
        "range_window_sessions": SHAPE_RANGE_WINDOW_SESSIONS,
        "range_window_includes_anchor": True,
        "range_formula": "(window_analysis_close_max/window_analysis_close_min-1)*100",
        "ema_span_sessions": SHAPE_EMA_SPAN_SESSIONS,
        "ema_adjust": False,
        "ema_source": "analysis_close",
        "ema_slope_lookback_sessions": SHAPE_EMA_SLOPE_LOOKBACK_SESSIONS,
        "ema_slope_formula": "(anchor_ema23/ema23_t_minus_5-1)*100",
        "rising_return_min_pct_exclusive": SHAPE_RISING_RETURN_MIN_PCT,
        "rising_ema_slope_min_pct_exclusive": SHAPE_RISING_EMA_SLOPE_MIN_PCT,
        "falling_return_max_pct_exclusive": SHAPE_FALLING_RETURN_MAX_PCT,
        "falling_ema_slope_max_pct_exclusive": SHAPE_FALLING_EMA_SLOPE_MAX_PCT,
        "consolidation_return_abs_max_pct_inclusive": SHAPE_CONSOLIDATION_RETURN_ABS_MAX_PCT,
        "consolidation_range_max_pct_inclusive": SHAPE_CONSOLIDATION_RANGE_MAX_PCT,
    },
    "base_trigger_contract": {
        "previous_close_high_window_sessions": BASE_TRIGGER_PREVIOUS_HIGH_WINDOW_SESSIONS,
        "crossing_requires_prior_day_not_breakout": True,
        "cross_breakout_recomputed_from_analysis_close": True,
        "ma_short_window_sessions": BASE_TRIGGER_MA_SHORT_WINDOW_SESSIONS,
        "ma_long_window_sessions": BASE_TRIGGER_MA_LONG_WINDOW_SESSIONS,
        "ma60_input_contract": "authoritative_prepared_input_numeric_pr462_compatible",
        "ma120_input_contract": "authoritative_prepared_input_numeric_pr462_compatible",
        "missing_or_nonfinite_ma_behavior": "not_a_base_trigger",
        "condition": "cross_breakout_prev20_and_ma60_gt_ma120",
    },
    "watch_horizon_trading_days": WATCH_HORIZON_TRADING_DAYS,
    "source_eligibility_before_lifecycle": (
        "point_in_time_latest_qualifying_source_lag_le_60_before_operation_block"
    ),
    "base_confirmation_rule_id": BASE_CONFIRMATION_RULE_ID,
    "confirmation_variant_id": CONFIRMATION_VARIANT_ID,
    "confirmation_rule_id": CONFIRMATION_RULE_ID,
    "entry_rule_id": ENTRY_RULE_ID,
    "entry_price_basis": "analysis_open",
    "holding_days": HOLDING_DAYS,
    "holding_session_index_offset": HOLDING_SESSION_INDEX_OFFSET,
    "holding_session_contract": "inclusive_entry_session_count_30_exit_offset_29",
    "stop_policy_id": STOP_POLICY_ID,
    "exit_rule_id": EXIT_RULE_ID,
    "exit_price_basis": "analysis_close",
    "lifecycle_policy_id": LIFECYCLE_POLICY_ID,
    "same_stock_non_overlap": "entry_after_prior_realized_exit_next_trading_day",
    "lifecycle_then_stratification_order": (
        "pr462_global_source_universe_rearm_non_overlap_before_low_mid_falling_membership"
    ),
    "anomaly_policy": "primary_retains_unresolved_candidates_sensitivity_excludes",
    "operation_return_review_threshold_pct": OPERATION_RETURN_REVIEW_THRESHOLD_PCT,
    "financial_statement_scope": (
        "monthly_revenue_only;EPS_gross_margin_operating_margin_operating_income_"
        "non_operating_income_net_income_excluded"
    ),
}

DATA_CONTRACT_VERSION = "revenue_low_mid_falling_forward_holdout_data_v1"
DATA_CONTRACT = {
    "training_cutoff_date": TRAINING_CUTOFF_DATE,
    "bridge_start_date": BRIDGE_START_DATE,
    "bridge_end_date": BRIDGE_END_DATE,
    "holdout_start_date": HOLDOUT_START_DATE,
    "source_projection_artifact_id": SOURCE_PROJECTION_ARTIFACT_ID,
    "source_projection_artifact_version": SOURCE_PROJECTION_ARTIFACT_VERSION,
    "pr462_projected_episode_row_count": PR462_PROJECTED_EPISODE_ROW_COUNT,
    "pr462_projected_episode_semantic_sha256": (
        PR462_PROJECTED_EPISODE_SEMANTIC_SHA256
    ),
    "source_artifact_id": SOURCE_ARTIFACT_ID,
    "source_artifact_version": SOURCE_ARTIFACT_VERSION,
    "append_only_history": True,
    "research_only": True,
    "formal_model_use_allowed": False,
    "approved_for_daily": False,
    "presentation_allowed": False,
    "promotion_evidence_allowed": False,
    "production_change": False,
}


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
    if value is None or (not isinstance(value, (list, dict, tuple)) and pd.isna(value)):
        return ""
    if isinstance(value, (bool, np.bool_)):
        return "true" if bool(value) else "false"
    if isinstance(value, (int, np.integer)):
        return str(int(value))
    if isinstance(value, (float, np.floating)):
        if not math.isfinite(float(value)):
            return ""
        return format(float(value), ".15g")
    text_value = str(value).strip()
    if text_value.lower() in {"true", "false"}:
        return text_value.lower()
    numeric = _canonical_numeric_text(text_value)
    return numeric if numeric is not None else text_value


def _canonical_json_sha256(payload: object) -> str:
    return hashlib.sha256(
        json.dumps(payload, ensure_ascii=False, separators=(",", ":"), sort_keys=True).encode(
            "utf-8"
        )
    ).hexdigest()


RULE_CANONICAL_SHA256 = _canonical_json_sha256(RULE_CONTRACT)
DATA_CONTRACT_SHA256 = _canonical_json_sha256(DATA_CONTRACT)

FINANCIAL_STATEMENT_SCOPE = str(RULE_CONTRACT["financial_statement_scope"])
ANOMALY_POLICY = str(RULE_CONTRACT["anomaly_policy"])
NON_OVERLAP_POLICY = str(RULE_CONTRACT["same_stock_non_overlap"])

DEFAULT_OUTPUT_RELATIVE_PATHS = {
    name: relative
    for surface, base in (
        ("latest", "output/latest/research_backtest"),
        ("history", "output/history/research"),
        ("docs", "docs/latest"),
    )
    for artifact, suffix in (
        ("manifest", "manifest"),
        ("detail", "event_detail"),
        ("summary", "maturity_status"),
        ("comparison", "comparison"),
        ("anomaly", "anomaly_sensitivity"),
    )
    for name, relative in (
        (
            f"{artifact}_{surface}",
            (
                f"{base}/{ARTIFACT_ID}_{suffix}_latest.csv"
                if surface in {"latest", "docs"}
                else f"{base}/{ARTIFACT_ID}_{suffix}.csv"
            ),
        ),
    )
}
FORWARD_HOLDOUT_ALLOWED_ARTIFACT_PATHS = tuple(
    sorted(DEFAULT_OUTPUT_RELATIVE_PATHS.values())
)

SHA256_PATTERN = re.compile(r"^[0-9a-f]{64}$")
MONTHLY_LINEAGE_COLUMNS = (
    "monthly_revenue_history_blob_sha256",
    "monthly_revenue_canonical_table_sha256",
    "cross_market_resolution_registry_canonical_sha256",
)
FALSE_FLAG_COLUMNS = (
    "formal_model_use_allowed",
    "approved_for_daily",
    "presentation_allowed",
    "promotion_evidence_allowed",
    "production_change",
)
DETAIL_COLUMNS = (
    "generated_at",
    "model_id",
    "artifact_id",
    "artifact_version",
    "capture_id",
    "artifact_row_key",
    "rule_contract_version",
    "rule_canonical_sha256",
    "data_contract_version",
    "data_contract_sha256",
    "preregistration_merge_commit",
    "source_artifact_id",
    "source_artifact_version",
    "source_detail_canonical_sha256",
    "price_input_canonical_sha256",
    *MONTHLY_LINEAGE_COLUMNS,
    "training_source_projection_semantic_sha256",
    "training_source_projected_episode_row_count",
    "training_source_manifest_canonical_sha256",
    "event_key",
    "variant_id",
    "candidate_variant_id",
    "primary_variant_member",
    "low_falling_member",
    "low_or_mid_falling_union_member",
    "lifecycle_policy_id",
    "confirmation_variant_id",
    "holding_days",
    "holding_session_index_offset",
    "stop_policy_id",
    "stock_id",
    "stock_name",
    "episode_key",
    "source_asof_date",
    "source_asof_trade_date",
    "source_asof_revenue_period",
    "source_asof_row_canonical_sha256",
    "source_asof_canonical_source_table_date",
    "source_asof_sequence_index",
    "source_to_trigger_trading_days",
    "future_qualifying_update_ignored_count",
    "source_position_120d_pct",
    "source_shape_return20_pct",
    "source_shape_range23_pct",
    "source_shape_ema23_slope5_pct",
    "source_position_bucket",
    "source_shape_bucket",
    "source_position_shape_cell_id",
    "trigger_index",
    "trigger_date",
    "trigger_close",
    "confirmation_index",
    "confirmation_date",
    "confirmation_close",
    "entry_index",
    "entry_price_basis",
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
    "entry_date",
    "entry_price",
    "operation_status",
    "anomaly_candidate_flag",
    "source_anomaly_candidate_flag",
    "unresolved_price_path_candidate_flag",
    "primary_metric_included",
    "sensitivity_metric_included",
    "same_stock_non_overlap_applied",
    "financial_statement_scope",
    "research_only",
    *FALSE_FLAG_COLUMNS,
    "event_row_canonical_sha256",
)


def _now_text() -> str:
    return datetime.now(ZoneInfo("Asia/Taipei")).strftime(
        "%Y-%m-%d %H:%M:%S Asia/Taipei"
    )


def _date_text(value: object) -> str:
    text = "".join(character for character in str(value or "") if character.isdigit())
    return text[:8] if len(text) >= 8 else ""


def _stock_id(value: object) -> str:
    text = str(value or "").strip()
    if text.endswith(".0") and text[:-2].isdigit():
        text = text[:-2]
    return text.zfill(4) if text.isdigit() else text


def _bool_value(value: object) -> bool:
    return str(value).strip().lower() in {"true", "1", "yes"}


def _number(value: object) -> float:
    result = pd.to_numeric(value, errors="coerce")
    return float(result) if pd.notna(result) else math.nan


def _require_exact_integer(value: object, *, label: str) -> int:
    try:
        number = Decimal(str(value).strip())
    except InvalidOperation as exc:
        raise RuntimeError(f"forward holdout {label} is not an exact integer") from exc
    if not number.is_finite() or number != number.to_integral_value():
        raise RuntimeError(f"forward holdout {label} is not an exact integer")
    return int(number)


def _require_sha256(value: object, *, label: str) -> str:
    digest = str(value).strip().lower()
    if not SHA256_PATTERN.fullmatch(digest):
        raise RuntimeError(f"forward holdout {label} is not a canonical SHA-256")
    return digest


def _canonical_mapping_sha256(
    mapping: Mapping[str, object],
    *,
    excluded_columns: tuple[str, ...] = ("generated_at",),
) -> str:
    payload = [
        [str(key), _canonical_value(value)]
        for key, value in sorted(mapping.items())
        if str(key) not in excluded_columns
    ]
    return _canonical_json_sha256([CANONICAL_LINEAGE_VERSION, payload])


def _canonical_frame_sha256(
    frame: pd.DataFrame,
    *,
    excluded_columns: tuple[str, ...] = ("generated_at",),
) -> str:
    columns = sorted(column for column in frame.columns if column not in excluded_columns)
    rows = [
        [_canonical_value(value) for value in row]
        for row in frame.loc[:, columns].itertuples(index=False, name=None)
    ]
    rows.sort()
    return _canonical_json_sha256([CANONICAL_LINEAGE_VERSION, columns, rows])


def _constant(frame: pd.DataFrame, column: str, *, label: str) -> str:
    if column not in frame.columns:
        raise RuntimeError(f"forward holdout {label} missing column: {column}")
    values = sorted({_canonical_value(value) for value in frame[column]})
    if len(values) != 1 or not values[0]:
        raise RuntimeError(f"forward holdout {label} must have one non-empty {column}")
    return values[0]


def _validate_source_manifest(source_manifest: pd.DataFrame) -> dict[str, str]:
    if len(source_manifest) != 1:
        raise RuntimeError("forward holdout source projection manifest must have one row")
    required = {
        "artifact_id",
        "artifact_version",
        "cutoff_date",
        "projected_episode_semantic_sha256",
        "projected_episode_row_count",
        "research_only",
        "formal_model_use_allowed",
        "approved_for_daily",
        "production_change",
        "promotion_evidence_allowed",
        "ranking_consumption_allowed",
        "pdf_consumption_allowed",
    }
    missing = sorted(required - set(source_manifest.columns))
    if missing:
        raise RuntimeError(f"forward holdout source projection manifest missing: {missing}")
    row = source_manifest.iloc[0]
    expected = {
        "artifact_id": SOURCE_PROJECTION_ARTIFACT_ID,
        "artifact_version": SOURCE_PROJECTION_ARTIFACT_VERSION,
        "cutoff_date": TRAINING_CUTOFF_DATE,
    }
    for column, value in expected.items():
        if str(row[column]).strip() != value:
            raise RuntimeError(f"forward holdout source projection {column} drift")
    projected_row_count = _require_exact_integer(
        row["projected_episode_row_count"],
        label="training projected episode row count",
    )
    if projected_row_count != PR462_PROJECTED_EPISODE_ROW_COUNT:
        raise RuntimeError(
            "forward holdout PR462 projected episode row count drift: "
            f"expected={PR462_PROJECTED_EPISODE_ROW_COUNT} "
            f"observed={projected_row_count}"
        )
    projected_semantic_sha256 = _require_sha256(
        row["projected_episode_semantic_sha256"],
        label="training projected episode semantic SHA-256",
    )
    if projected_semantic_sha256 != PR462_PROJECTED_EPISODE_SEMANTIC_SHA256:
        raise RuntimeError(
            "forward holdout PR462 projected episode semantic SHA-256 drift"
        )
    if not _strict_bool_value(
        row["research_only"],
        label="training projection research_only",
    ):
        raise RuntimeError("forward holdout training projection must be research_only")
    for column in (
        "formal_model_use_allowed",
        "approved_for_daily",
        "production_change",
        "promotion_evidence_allowed",
        "ranking_consumption_allowed",
        "pdf_consumption_allowed",
    ):
        if _strict_bool_value(
            row[column],
            label=f"training projection {column}",
        ):
            raise RuntimeError(f"forward holdout training projection {column} must be false")
    return {
        "training_source_projection_semantic_sha256": projected_semantic_sha256,
        "training_source_projected_episode_row_count": projected_row_count,
        "training_source_manifest_canonical_sha256": _canonical_frame_sha256(
            source_manifest
        ),
    }


def _strict_bool_value(value: object, *, label: str) -> bool:
    token = str(value).strip().lower()
    if token in {"true", "1", "yes"}:
        return True
    if token in {"false", "0", "no"}:
        return False
    raise RuntimeError(f"forward holdout {label} is not canonical boolean text")


def _validate_source_anomaly_boolean_contract(source: pd.DataFrame) -> None:
    scalar_columns = (
        "qualifying_source_revenue_anomaly_candidate_flag",
        "unresolved_price_path_candidate_flag",
    )
    if "start_source_revenue_anomaly_candidate_flag" in source.columns:
        scalar_columns = (*scalar_columns, "start_source_revenue_anomaly_candidate_flag")
    for column in scalar_columns:
        if column not in source.columns:
            raise RuntimeError(
                f"forward holdout source anomaly contract missing column: {column}"
            )
        for row_index, value in source[column].items():
            _strict_bool_value(
                value,
                label=f"source anomaly {column} row={row_index}",
            )
    list_column = "qualifying_source_revenue_anomaly_candidate_flags"
    if list_column not in source.columns:
        raise RuntimeError(
            f"forward holdout source anomaly contract missing column: {list_column}"
        )
    for row_index, value in source[list_column].items():
        tokens = _split_pipe(value)
        if not tokens:
            raise RuntimeError(
                "forward holdout source anomaly flag lineage is empty: "
                f"row={row_index}"
            )
        for position, token in enumerate(tokens):
            _strict_bool_value(
                token,
                label=(
                    f"source anomaly {list_column} row={row_index} position={position}"
                ),
            )


def _validate_source_integer_contract(source: pd.DataFrame) -> None:
    required = (
        "qualifying_update_count",
        "qualifying_sequence_indices",
        "episode_start_sequence_index",
        "latest_qualifying_sequence_index",
    )
    missing = sorted(set(required) - set(source.columns))
    if missing:
        raise RuntimeError(f"forward holdout source integer contract missing: {missing}")
    for row_index, row in source.iterrows():
        count = _require_exact_integer(
            row["qualifying_update_count"],
            label=f"source qualifying update count row={row_index}",
        )
        sequence_tokens = _split_pipe(row["qualifying_sequence_indices"])
        sequences = [
            _require_exact_integer(
                token,
                label=f"source qualifying sequence row={row_index} position={position}",
            )
            for position, token in enumerate(sequence_tokens)
        ]
        if count <= 0 or len(sequences) != count or any(value < 0 for value in sequences):
            raise RuntimeError(
                f"forward holdout source sequence/count contract drift: row={row_index}"
            )
        start = _require_exact_integer(
            row["episode_start_sequence_index"],
            label=f"source episode-start sequence row={row_index}",
        )
        latest = _require_exact_integer(
            row["latest_qualifying_sequence_index"],
            label=f"source latest sequence row={row_index}",
        )
        if start != sequences[0] or latest != sequences[-1]:
            raise RuntimeError(
                f"forward holdout source scalar/list sequence drift: row={row_index}"
            )


def _split_pipe(value: object) -> list[str]:
    return [token.strip() for token in str(value).split("|") if token.strip()]


def _attach_qualifying_anomaly_flags(
    source_detail: pd.DataFrame,
    prepared_research_frame: pd.DataFrame,
) -> pd.DataFrame:
    """Bind every qualifying source-row SHA to its own PIT anomaly flag."""

    source_sha_column = "full_monthly_revenue_source_row_canonical_sha256"
    anomaly_column = "full_monthly_revenue_numerical_anomaly_flag"
    missing = sorted(
        {source_sha_column, anomaly_column} - set(prepared_research_frame.columns)
    )
    if missing:
        raise RuntimeError(
            "forward holdout prepared revenue anomaly evidence missing columns: "
            f"{missing}"
        )
    evidence: dict[str, bool] = {}
    for row in prepared_research_frame[[source_sha_column, anomaly_column]].itertuples(
        index=False, name=None
    ):
        digest = str(row[0]).strip().lower()
        if not digest:
            continue
        _require_sha256(digest, label="prepared monthly-revenue source row")
        flag = _strict_bool_value(
            row[1], label=f"prepared monthly-revenue anomaly flag/{digest}"
        )
        if digest in evidence and evidence[digest] != flag:
            raise RuntimeError(
                "forward holdout prepared monthly-revenue anomaly evidence conflicts: "
                f"{digest}"
            )
        evidence[digest] = flag
    if not evidence:
        raise RuntimeError(
            "forward holdout prepared monthly-revenue anomaly evidence is empty"
        )

    attached = source_detail.copy()
    aligned_flags: list[str] = []
    for _, episode in attached.iterrows():
        hashes = [
            _require_sha256(token, label="qualifying source-row anomaly lineage")
            for token in _split_pipe(
                episode.get("qualifying_source_row_canonical_sha256s", "")
            )
        ]
        if not hashes:
            raise RuntimeError(
                "forward holdout qualifying source-row anomaly lineage is empty"
            )
        missing_hashes = [digest for digest in hashes if digest not in evidence]
        if missing_hashes:
            raise RuntimeError(
                "forward holdout qualifying source-row anomaly evidence is missing: "
                f"{missing_hashes[:5]}"
            )
        flags = [evidence[digest] for digest in hashes]
        if "start_source_revenue_anomaly_candidate_flag" in episode.index and (
            _strict_bool_value(
                episode["start_source_revenue_anomaly_candidate_flag"],
                label="episode-start source anomaly flag",
            )
            != flags[0]
        ):
            raise RuntimeError(
                "forward holdout episode-start source anomaly flag disagrees with row evidence"
            )
        if "qualifying_source_revenue_anomaly_candidate_flag" in episode.index and (
            _strict_bool_value(
                episode["qualifying_source_revenue_anomaly_candidate_flag"],
                label="episode aggregate source anomaly flag",
            )
            != any(flags)
        ):
            raise RuntimeError(
                "forward holdout episode aggregate source anomaly flag disagrees with row evidence"
            )
        aligned_flags.append("|".join("True" if flag else "False" for flag in flags))
    attached["qualifying_source_revenue_anomaly_candidate_flags"] = aligned_flags
    return attached


def _asof_source_anomaly_flag(
    episode: pd.Series,
    asof: Mapping[str, object],
) -> bool:
    names = (
        "qualifying_source_dates",
        "qualifying_source_row_canonical_sha256s",
        "qualifying_canonical_source_table_dates",
        "qualifying_trade_dates",
        "qualifying_sequence_indices",
        "qualifying_source_revenue_anomaly_candidate_flags",
    )
    values = {name: _split_pipe(episode.get(name, "")) for name in names}
    expected_count = int(episode["qualifying_update_count"])
    if {len(items) for items in values.values()} != {expected_count} or not expected_count:
        raise RuntimeError(
            "forward holdout qualifying anomaly lineage is not exactly aligned: "
            f"{episode['episode_key']}"
        )
    matches: list[int] = []
    for position in range(expected_count):
        try:
            sequence_index = int(values["qualifying_sequence_indices"][position])
        except ValueError as exc:
            raise RuntimeError(
                "forward holdout qualifying anomaly sequence index is invalid: "
                f"{episode['episode_key']}"
            ) from exc
        if (
            sequence_index == int(asof["asof_latest_qualifying_sequence_index"])
            and _date_text(values["qualifying_source_dates"][position])
            == str(asof["asof_latest_qualifying_source_date"])
            and values["qualifying_source_row_canonical_sha256s"][position].lower()
            == str(asof["asof_latest_qualifying_source_row_canonical_sha256"]).lower()
            and _date_text(values["qualifying_canonical_source_table_dates"][position])
            == str(asof["asof_latest_qualifying_canonical_source_table_date"])
            and _date_text(values["qualifying_trade_dates"][position])
            == str(asof["asof_latest_qualifying_trade_date"])
        ):
            matches.append(position)
    if len(matches) != 1:
        raise RuntimeError(
            "forward holdout as-of source anomaly row is not uniquely identified: "
            f"{episode['episode_key']}"
        )
    return _strict_bool_value(
        values["qualifying_source_revenue_anomaly_candidate_flags"][matches[0]],
        label=f"as-of qualifying source anomaly flag/{episode['episode_key']}",
    )


def _normalize_prices(
    daily_by_stock: Mapping[str, pd.DataFrame],
) -> dict[str, pd.DataFrame]:
    normalized: dict[str, pd.DataFrame] = {}
    for raw_stock_id, raw in daily_by_stock.items():
        stock_id = _stock_id(raw_stock_id)
        frame = raw.copy()
        if "date" not in frame.columns:
            raise RuntimeError(f"forward holdout price history missing date: {stock_id}")
        frame["date"] = frame["date"].map(_date_text)
        if frame["date"].eq("").any() or frame["date"].duplicated().any():
            raise RuntimeError(f"forward holdout price dates invalid or duplicate: {stock_id}")
        frame = frame.sort_values("date", kind="mergesort").reset_index(drop=True)
        for basis in ("open", "high", "low", "close"):
            analysis = f"analysis_{basis}"
            if analysis not in frame.columns:
                if basis not in frame.columns:
                    raise RuntimeError(
                        f"forward holdout price history missing {analysis}: {stock_id}"
                    )
                frame[analysis] = pd.to_numeric(frame[basis], errors="coerce")
            frame[analysis] = pd.to_numeric(frame[analysis], errors="coerce")
        close = frame["analysis_close"]
        for column in ("ma60", "ma120"):
            if column not in frame.columns:
                frame[column] = np.nan
            frame[column] = pd.to_numeric(frame[column], errors="coerce")
        canonical_numeric = {
            "analysis_ema23": close.ewm(
                span=SHAPE_EMA_SPAN_SESSIONS,
                adjust=False,
            ).mean(),
        }
        for column, canonical in canonical_numeric.items():
            if column in frame.columns:
                observed = pd.to_numeric(frame[column], errors="coerce")
                parity = np.isclose(
                    observed.to_numpy(dtype=float),
                    canonical.to_numpy(dtype=float),
                    rtol=1e-12,
                    atol=1e-10,
                    equal_nan=True,
                )
                if not bool(parity.all()):
                    first = int(np.flatnonzero(~parity)[0])
                    raise RuntimeError(
                        "forward holdout derived price field differs from the frozen "
                        f"analysis_close formula: {stock_id}/{column}/row={first + 2}"
                    )
            frame[column] = canonical
        if "operation_ma20" not in frame.columns:
            frame["operation_ma20"] = close.rolling(20, min_periods=20).mean()
        if "operation_ema23" not in frame.columns:
            frame["operation_ema23"] = close.ewm(span=23, adjust=False).mean()
        previous_high = close.shift(1).rolling(
            BASE_TRIGGER_PREVIOUS_HIGH_WINDOW_SESSIONS,
            min_periods=BASE_TRIGGER_PREVIOUS_HIGH_WINDOW_SESSIONS,
        ).max()
        breakout = close.gt(previous_high)
        canonical_cross = breakout & ~breakout.shift(
            1, fill_value=False
        ).astype(bool)
        if "cross_breakout_prev20" in frame.columns:
            observed_cross = frame["cross_breakout_prev20"].map(
                lambda value: _strict_bool_value(
                    value,
                    label=f"cross_breakout_prev20/{stock_id}",
                )
            )
            if not observed_cross.equals(canonical_cross):
                mismatch = observed_cross.ne(canonical_cross)
                first = int(np.flatnonzero(mismatch.to_numpy())[0])
                raise RuntimeError(
                    "forward holdout derived price field differs from the frozen "
                    f"analysis_close formula: {stock_id}/cross_breakout_prev20/"
                    f"row={first + 2}"
                )
        frame["cross_breakout_prev20"] = canonical_cross
        normalized[stock_id] = frame
    if not normalized:
        raise RuntimeError("forward holdout has no normalized price inputs")
    return normalized


def _frozen_anchor_features(frame: pd.DataFrame, index: int) -> dict[str, object]:
    close = _number(frame.at[index, "analysis_close"])
    prior = frame.iloc[
        max(0, index - POSITION_LOOKBACK_PRIOR_SESSIONS) : index
    ]
    prior_high = pd.to_numeric(prior["analysis_high"], errors="coerce")
    prior_low = pd.to_numeric(prior["analysis_low"], errors="coerce")
    position_observed = bool(
        len(prior) == POSITION_LOOKBACK_PRIOR_SESSIONS
        and prior_high.notna().all()
        and prior_low.notna().all()
        and np.isfinite(close)
    )
    high = float(prior_high.max()) if position_observed else math.nan
    low = float(prior_low.min()) if position_observed else math.nan
    position_observed = bool(
        position_observed
        and np.isfinite(high)
        and np.isfinite(low)
        and high > low
    )
    position = (
        (close - low) / (high - low) * 100.0 if position_observed else math.nan
    )
    position_bucket = (
        "low_pos_le40"
        if position_observed and position <= POSITION_LOW_MAX_PCT
        else "mid_pos_40_75"
        if position_observed and position <= POSITION_MID_MAX_PCT
        else "high_pos_gt75"
        if position_observed
        else "insufficient_history"
    )

    return_value = math.nan
    if index >= SHAPE_RETURN_LOOKBACK_SESSIONS:
        prior_close = _number(
            frame.at[
                index - SHAPE_RETURN_LOOKBACK_SESSIONS,
                "analysis_close",
            ]
        )
        if np.isfinite(close) and np.isfinite(prior_close) and prior_close > 0:
            return_value = (close / prior_close - 1.0) * 100.0
    recent = pd.to_numeric(
        frame.iloc[
            max(0, index - SHAPE_RANGE_WINDOW_SESSIONS + 1) : index + 1
        ]["analysis_close"],
        errors="coerce",
    )
    range_value = (
        (float(recent.max()) / float(recent.min()) - 1.0) * 100.0
        if len(recent) == SHAPE_RANGE_WINDOW_SESSIONS
        and recent.notna().all()
        and float(recent.min()) > 0
        else math.nan
    )
    ema_now = (
        _number(frame.at[index, "analysis_ema23"])
        if index >= SHAPE_EMA_SLOPE_LOOKBACK_SESSIONS
        else math.nan
    )
    ema_prior = (
        _number(
            frame.at[
                index - SHAPE_EMA_SLOPE_LOOKBACK_SESSIONS,
                "analysis_ema23",
            ]
        )
        if index >= SHAPE_EMA_SLOPE_LOOKBACK_SESSIONS
        else math.nan
    )
    ema_slope = (
        (ema_now / ema_prior - 1.0) * 100.0
        if np.isfinite(ema_now) and np.isfinite(ema_prior) and ema_prior > 0
        else math.nan
    )
    if not all(
        np.isfinite(value) for value in (return_value, range_value, ema_slope)
    ):
        shape_bucket = "insufficient_history"
    elif (
        return_value > SHAPE_RISING_RETURN_MIN_PCT
        and ema_slope > SHAPE_RISING_EMA_SLOPE_MIN_PCT
    ):
        shape_bucket = "rising"
    elif (
        return_value < SHAPE_FALLING_RETURN_MAX_PCT
        and ema_slope < SHAPE_FALLING_EMA_SLOPE_MAX_PCT
    ):
        shape_bucket = "falling"
    elif (
        abs(return_value) <= SHAPE_CONSOLIDATION_RETURN_ABS_MAX_PCT
        and range_value <= SHAPE_CONSOLIDATION_RANGE_MAX_PCT
    ):
        shape_bucket = "consolidation"
    else:
        shape_bucket = "mixed_or_turn"
    cell_id = (
        f"{position_bucket}__{shape_bucket}"
        if position_observed and shape_bucket != "insufficient_history"
        else "insufficient_history"
    )
    return {
        "position_120d_pct": round(position, 4) if np.isfinite(position) else "",
        "shape_return20_pct": (
            round(return_value, 4) if np.isfinite(return_value) else ""
        ),
        "shape_range23_pct": (
            round(range_value, 4) if np.isfinite(range_value) else ""
        ),
        "shape_ema23_slope5_pct": (
            round(ema_slope, 4) if np.isfinite(ema_slope) else ""
        ),
        "position_bucket": position_bucket,
        "shape_bucket": shape_bucket,
        "position_shape_cell_id": cell_id,
    }


def _price_lineage(prices: Mapping[str, pd.DataFrame]) -> tuple[str, str, int, int]:
    rows: list[dict[str, object]] = []
    row_count = 0
    for stock_id, frame in sorted(prices.items()):
        digest = _canonical_frame_sha256(frame)
        rows.append({"stock_id": stock_id, "price_canonical_sha256": digest})
        row_count += len(frame)
    manifest = pd.DataFrame(rows)
    return (
        _canonical_frame_sha256(manifest),
        "|".join(f"{row['stock_id']}:{row['price_canonical_sha256']}" for row in rows),
        len(rows),
        row_count,
    )


def _date_index(frame: pd.DataFrame) -> dict[str, int]:
    result = {str(date): int(index) for index, date in frame["date"].items()}
    if len(result) != len(frame):
        raise RuntimeError("forward holdout normalized price history has duplicate dates")
    return result


def _first_index_on_or_after(frame: pd.DataFrame, date: str) -> int | None:
    matches = frame.index[frame["date"].astype(str).ge(date)]
    return int(matches[0]) if len(matches) else None


def _base_trigger_hit(frame: pd.DataFrame, index: int) -> bool:
    ma60 = _number(frame.at[index, "ma60"])
    ma120 = _number(frame.at[index, "ma120"])
    return bool(
        _bool_value(frame.at[index, "cross_breakout_prev20"])
        and np.isfinite(ma60)
        and np.isfinite(ma120)
        and ma60 > ma120
    )


def _operation_result(frame: pd.DataFrame, trigger_index: int) -> dict[str, object]:
    confirmation_index = trigger_index + 1
    entry_index = confirmation_index + 1
    if confirmation_index >= len(frame):
        raise RuntimeError("forward holdout selected a trigger without an observed D+1 close")
    trigger_close = _number(frame.at[trigger_index, "analysis_close"])
    confirmation_close = _number(frame.at[confirmation_index, "analysis_close"])
    if not (
        np.isfinite(trigger_close)
        and np.isfinite(confirmation_close)
        and confirmation_close > trigger_close
    ):
        raise RuntimeError("forward holdout selected a trigger without D+1 continuation")
    base = {
        "trigger_index": trigger_index,
        "trigger_date": str(frame.at[trigger_index, "date"]),
        "trigger_close": round(trigger_close, 8),
        "confirmation_index": confirmation_index,
        "confirmation_date": str(frame.at[confirmation_index, "date"]),
        "confirmation_close": round(confirmation_close, 8),
        "entry_index": entry_index,
        "entry_price_basis": "analysis_open",
        "planned_exit_index": entry_index + HOLDING_SESSION_INDEX_OFFSET,
        "planned_exit_date": "",
        "exit_index": "",
        "exit_date": "",
        "exit_price": "",
        "exit_price_basis": "analysis_close",
        "exit_reason": EXIT_RULE_ID,
        "return_valid": False,
        "right_censored": True,
        "realized_return_pct": "",
        "return_outcome": "",
        "realized_return_ge20": False,
        "operation_return_review_candidate_flag": False,
    }
    if entry_index >= len(frame):
        return {
            **base,
            "operation_status": "right_censored_before_entry",
            "entry_date": "",
            "entry_price": "",
            "blocked_through_index": len(frame) - 1,
        }
    entry_price = _number(frame.at[entry_index, "analysis_open"])
    if not np.isfinite(entry_price) or entry_price <= 0:
        raise RuntimeError("forward holdout D+2 entry open is invalid")
    base.update(
        {
            "entry_date": str(frame.at[entry_index, "date"]),
            "entry_price": round(entry_price, 8),
        }
    )
    planned_exit_index = int(base["planned_exit_index"])
    if planned_exit_index >= len(frame):
        return {
            **base,
            "operation_status": f"right_censored_before_d{HOLDING_DAYS}",
            "blocked_through_index": len(frame) - 1,
        }
    exit_price = _number(frame.at[planned_exit_index, "analysis_close"])
    if not np.isfinite(exit_price) or exit_price <= 0:
        raise RuntimeError("forward holdout D+30 fixed close is invalid")
    realized_return = (exit_price / entry_price - 1.0) * 100.0
    outcome = (
        "win"
        if realized_return > 1e-9
        else "failure"
        if realized_return < -1e-9
        else "neutral"
    )
    return {
        **base,
        "operation_status": "mature_operation",
        "planned_exit_date": str(frame.at[planned_exit_index, "date"]),
        "exit_index": planned_exit_index,
        "exit_date": str(frame.at[planned_exit_index, "date"]),
        "exit_price": round(exit_price, 8),
        "return_valid": True,
        "right_censored": False,
        "realized_return_pct": round(realized_return, 4),
        "return_outcome": outcome,
        "realized_return_ge20": realized_return >= 20.0,
        "operation_return_review_candidate_flag": (
            abs(realized_return) >= OPERATION_RETURN_REVIEW_THRESHOLD_PCT
        ),
        "blocked_through_index": planned_exit_index,
    }


def _event_rows_for_window(
    source: pd.DataFrame,
    prices: Mapping[str, pd.DataFrame],
    *,
    window_start: str,
    window_end: str,
    generated_at: str,
    capture_id: str,
    lineage: Mapping[str, object],
) -> list[dict[str, object]]:
    rows: list[dict[str, object]] = []
    for stock_id, episodes in source.groupby("stock_id", sort=False):
        stock_id = _stock_id(stock_id)
        frame = prices.get(stock_id)
        if frame is None or frame.empty:
            continue
        date_index = _date_index(frame)
        window_start_index = _first_index_on_or_after(frame, window_start)
        if window_start_index is None:
            continue
        window_end_indices = frame.index[frame["date"].astype(str).le(window_end)]
        if not len(window_end_indices):
            continue
        window_end_index = int(window_end_indices[-1])
        candidate_indices: list[int] = []
        for index in range(window_start_index, window_end_index + 1):
            if not _base_trigger_hit(frame, index):
                continue
            confirmation_index = index + 1
            if confirmation_index >= len(frame):
                continue
            trigger_close = _number(frame.at[index, "analysis_close"])
            confirmation_close = _number(frame.at[confirmation_index, "analysis_close"])
            if (
                np.isfinite(trigger_close)
                and np.isfinite(confirmation_close)
                and confirmation_close > trigger_close
            ):
                candidate_indices.append(index)
        blocked_through_index = window_start_index - 1
        for _, episode in episodes.sort_values(
            ["episode_start_trade_date", "episode_key"], kind="mergesort"
        ).iterrows():
            start_date = _date_text(episode["episode_start_trade_date"])
            if start_date not in date_index:
                continue
            try:
                source_sequence_indices = [
                    int(value)
                    for value in str(episode["qualifying_sequence_indices"]).split("|")
                    if str(value).strip()
                ]
            except ValueError as exc:
                raise RuntimeError(
                    "forward holdout qualifying sequence index is invalid: "
                    f"{episode['episode_key']}"
                ) from exc
            if not source_sequence_indices:
                raise RuntimeError(
                    "forward holdout qualifying sequence index is empty: "
                    f"{episode['episode_key']}"
                )
            start_index = max(
                date_index[start_date], window_start_index, blocked_through_index + 1
            )
            # The source projection's episode_end_date is a retrospective training
            # boundary.  It must not truncate a pre-registered forward observation.
            # Each point-in-time revenue availability opens the same frozen 60-session
            # watch horizon; the observed price boundary supplies right censoring.
            end_index = min(
                max(source_sequence_indices) + WATCH_HORIZON_TRADING_DAYS,
                window_end_index,
            )
            if start_index > end_index:
                continue
            for trigger_index in candidate_indices:
                if trigger_index < start_index:
                    continue
                if trigger_index <= blocked_through_index:
                    continue
                if trigger_index > end_index:
                    break
                asof = _asof_source(episode, frame, trigger_index)
                trigger_date = str(frame.at[trigger_index, "date"])
                asof_dates = {
                    "source": str(asof["asof_latest_qualifying_source_date"]),
                    "trade": str(asof["asof_latest_qualifying_trade_date"]),
                    "canonical_source_table": str(
                        asof["asof_latest_qualifying_canonical_source_table_date"]
                    ),
                }
                future_asof_dates = {
                    label: date for label, date in asof_dates.items() if date > trigger_date
                }
                if future_asof_dates:
                    raise RuntimeError(
                        "forward holdout source as-of date exceeds trigger date: "
                        f"episode={episode['episode_key']} trigger={trigger_date} "
                        f"dates={future_asof_dates}"
                    )
                if int(asof["asof_latest_qualifying_sequence_index"]) > trigger_index:
                    raise RuntimeError(
                        "forward holdout source as-of sequence exceeds trigger index: "
                        f"episode={episode['episode_key']}"
                    )
                lag = int(asof["latest_source_to_trigger_trading_days"])
                if lag > WATCH_HORIZON_TRADING_DAYS:
                    # A price trigger outside every point-in-time revenue watch
                    # window is not part of the frozen source universe and must
                    # not consume the same-stock operation lifecycle.  A later
                    # qualifying revenue update may open a new 60-session window.
                    continue
                result = _operation_result(frame, trigger_index)
                blocked_through_index = max(
                    blocked_through_index, int(result.pop("blocked_through_index"))
                )
                features = _frozen_anchor_features(
                    frame, int(asof["source_index"])
                )
                position_bucket = str(features["position_bucket"])
                shape_bucket = str(features["shape_bucket"])
                low_member = (
                    position_bucket == "low_pos_le40" and shape_bucket == "falling"
                )
                mid_member = (
                    position_bucket == "mid_pos_40_75" and shape_bucket == "falling"
                )
                if low_member or mid_member:
                    source_candidate = _asof_source_anomaly_flag(episode, asof)
                    price_candidate = _bool_value(
                        episode["unresolved_price_path_candidate_flag"]
                    )
                    return_candidate = _bool_value(
                        result["operation_return_review_candidate_flag"]
                    )
                    anomaly_candidate = (
                        source_candidate or price_candidate or return_candidate
                    )
                    variant_id = PRIMARY_VARIANT_ID if mid_member else CHALLENGER_VARIANT_IDS[0]
                    event_key = "|".join(
                        (
                            LIFECYCLE_POLICY_ID,
                            CONFIRMATION_VARIANT_ID,
                            stock_id,
                            str(episode["episode_key"]),
                            str(result["trigger_date"]),
                        )
                    )
                    row = {
                            "generated_at": generated_at,
                            "model_id": MODEL_ID,
                            "artifact_id": ARTIFACT_ID,
                            "artifact_version": ARTIFACT_VERSION,
                            "capture_id": capture_id,
                            "artifact_row_key": event_key,
                            "rule_contract_version": RULE_CONTRACT_VERSION,
                            "rule_canonical_sha256": RULE_CANONICAL_SHA256,
                            "data_contract_version": DATA_CONTRACT_VERSION,
                            "data_contract_sha256": DATA_CONTRACT_SHA256,
                            "preregistration_merge_commit": PREREGISTRATION_MERGE_COMMIT,
                            **lineage,
                            "event_key": event_key,
                            "variant_id": variant_id,
                            "candidate_variant_id": variant_id,
                            "primary_variant_member": mid_member,
                            "low_falling_member": low_member,
                            "low_or_mid_falling_union_member": True,
                            "lifecycle_policy_id": LIFECYCLE_POLICY_ID,
                            "confirmation_variant_id": CONFIRMATION_VARIANT_ID,
                            "holding_days": HOLDING_DAYS,
                            "holding_session_index_offset": HOLDING_SESSION_INDEX_OFFSET,
                            "stop_policy_id": STOP_POLICY_ID,
                            "stock_id": stock_id,
                            "stock_name": str(episode["stock_name"]),
                            "episode_key": str(episode["episode_key"]),
                            "source_asof_date": str(asof["asof_latest_qualifying_source_date"]),
                            "source_asof_trade_date": str(
                                asof["asof_latest_qualifying_trade_date"]
                            ),
                            "source_asof_revenue_period": str(
                                asof["asof_latest_qualifying_revenue_period"]
                            ),
                            "source_asof_row_canonical_sha256": str(
                                asof["asof_latest_qualifying_source_row_canonical_sha256"]
                            ),
                            "source_asof_canonical_source_table_date": str(
                                asof[
                                    "asof_latest_qualifying_canonical_source_table_date"
                                ]
                            ),
                            "source_asof_sequence_index": int(
                                asof["asof_latest_qualifying_sequence_index"]
                            ),
                            "source_to_trigger_trading_days": lag,
                            "future_qualifying_update_ignored_count": int(
                                asof["future_qualifying_update_ignored_count"]
                            ),
                            "source_position_120d_pct": features["position_120d_pct"],
                            "source_shape_return20_pct": features["shape_return20_pct"],
                            "source_shape_range23_pct": features["shape_range23_pct"],
                            "source_shape_ema23_slope5_pct": features[
                                "shape_ema23_slope5_pct"
                            ],
                            "source_position_bucket": position_bucket,
                            "source_shape_bucket": shape_bucket,
                            "source_position_shape_cell_id": features[
                                "position_shape_cell_id"
                            ],
                            **result,
                            "anomaly_candidate_flag": anomaly_candidate,
                            "source_anomaly_candidate_flag": source_candidate,
                            "unresolved_price_path_candidate_flag": price_candidate,
                            "operation_return_review_candidate_flag": return_candidate,
                            "primary_metric_included": True,
                            "sensitivity_metric_included": not anomaly_candidate,
                            "same_stock_non_overlap_applied": True,
                            "financial_statement_scope": FINANCIAL_STATEMENT_SCOPE,
                            "research_only": True,
                            "formal_model_use_allowed": False,
                            "approved_for_daily": False,
                            "presentation_allowed": False,
                            "promotion_evidence_allowed": False,
                            "production_change": False,
                        }
                    row["event_row_canonical_sha256"] = _canonical_mapping_sha256(row)
                    rows.append(row)
                if _bool_value(result["right_censored"]):
                    break
    return rows


def _membership(detail: pd.DataFrame, variant_id: str) -> pd.Series:
    if variant_id == PRIMARY_VARIANT_ID:
        return detail["primary_variant_member"].map(_bool_value)
    if variant_id == CHALLENGER_VARIANT_IDS[0]:
        return detail["low_falling_member"].map(_bool_value)
    if variant_id == CHALLENGER_VARIANT_IDS[1]:
        return detail["low_or_mid_falling_union_member"].map(_bool_value)
    raise RuntimeError(f"unsupported forward holdout variant: {variant_id}")


def _overlap_pair_count(part: pd.DataFrame) -> int:
    overlaps = 0
    for _stock_id_value, stock in part.groupby("stock_id", sort=False):
        prior_exit_index = -1
        for row in stock.sort_values("trigger_index", kind="mergesort").itertuples(
            index=False
        ):
            entry_index = int(row.entry_index)
            if prior_exit_index >= 0 and entry_index <= prior_exit_index:
                overlaps += 1
            if _bool_value(row.right_censored):
                prior_exit_index = max(prior_exit_index, int(row.entry_index))
            elif _bool_value(row.return_valid):
                prior_exit_index = max(prior_exit_index, int(row.exit_index))
    return overlaps


def _metric_row(part: pd.DataFrame) -> dict[str, object]:
    mature = part.loc[part["return_valid"].map(_bool_value)].copy()
    returns = pd.to_numeric(mature["realized_return_pct"], errors="coerce").dropna()
    outcomes = mature["return_outcome"].astype(str)
    count = len(mature)
    return {
        "event_count": len(part),
        "mature_count": count,
        "right_censored_count": int(part["right_censored"].map(_bool_value).sum()),
        "win_count": int(outcomes.eq("win").sum()),
        "neutral_count": int(outcomes.eq("neutral").sum()),
        "failure_count": int(outcomes.eq("failure").sum()),
        "win_rate_pct": round(float(outcomes.eq("win").mean()) * 100.0, 4) if count else "",
        "average_return_pct": round(float(returns.mean()), 4) if len(returns) else "",
        "median_return_pct": round(float(returns.median()), 4) if len(returns) else "",
        "p10_return_pct": round(float(returns.quantile(0.10)), 4) if len(returns) else "",
        "p90_return_pct": round(float(returns.quantile(0.90)), 4) if len(returns) else "",
        "return_ge20_count": int(pd.to_numeric(returns, errors="coerce").ge(20.0).sum()),
        "loss_count": int(pd.to_numeric(returns, errors="coerce").lt(0.0).sum()),
        "same_stock_overlap_pair_count": _overlap_pair_count(part),
    }


def _summary_frames(
    detail: pd.DataFrame,
    *,
    generated_at: str,
    capture_id: str,
    bridge_excluded_count: int,
) -> tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    summary_rows: list[dict[str, object]] = []
    comparison_rows: list[dict[str, object]] = []
    anomaly_rows: list[dict[str, object]] = []
    base = {
        "generated_at": generated_at,
        "model_id": MODEL_ID,
        "artifact_id": ARTIFACT_ID,
        "artifact_version": ARTIFACT_VERSION,
        "capture_id": capture_id,
        "rule_canonical_sha256": RULE_CANONICAL_SHA256,
        "data_contract_sha256": DATA_CONTRACT_SHA256,
        "research_only": True,
        "formal_model_use_allowed": False,
        "approved_for_daily": False,
        "presentation_allowed": False,
        "promotion_evidence_allowed": False,
        "production_change": False,
    }
    for variant_order, variant_id in enumerate(ALL_VARIANT_IDS, start=1):
        part = detail.loc[_membership(detail, variant_id)].copy()
        metrics = _metric_row(part)
        status = "holdout_accumulating"
        summary_row = {
            **base,
            "artifact_row_key": variant_id,
            "variant_order": variant_order,
            "variant_id": variant_id,
            "variant_role": "primary" if variant_id == PRIMARY_VARIANT_ID else "challenger",
            "holdout_status": status,
            "bridge_excluded_signal_count": bridge_excluded_count,
            **metrics,
            "anomaly_candidate_count": int(
                part["anomaly_candidate_flag"].map(_bool_value).sum()
            ),
            "financial_statement_scope": FINANCIAL_STATEMENT_SCOPE,
        }
        summary_rows.append(summary_row)
        comparison_rows.append(
            {
                **base,
                "artifact_row_key": variant_id,
                "variant_order": variant_order,
                "variant_id": variant_id,
                "variant_role": summary_row["variant_role"],
                "holdout_status": status,
                **metrics,
                "comparison_conclusion": "no_promotion_conclusion_holdout_accumulating",
            }
        )
        for basis_order, (basis, basis_part) in enumerate(
            (
                ("primary_candidate_retaining", part),
                (
                    "excluding_unresolved_anomaly_candidates_sensitivity",
                    part.loc[~part["anomaly_candidate_flag"].map(_bool_value)],
                ),
            ),
            start=1,
        ):
            anomaly_rows.append(
                {
                    **base,
                    "artifact_row_key": f"{variant_id}|{basis}",
                    "variant_order": variant_order,
                    "basis_order": basis_order,
                    "variant_id": variant_id,
                    "analysis_basis": basis,
                    "excluded_anomaly_candidate_count": (
                        0
                        if basis == "primary_candidate_retaining"
                        else int(part["anomaly_candidate_flag"].map(_bool_value).sum())
                    ),
                    **_metric_row(basis_part),
                    "anomaly_policy": ANOMALY_POLICY,
                }
            )
    return (
        pd.DataFrame(summary_rows),
        pd.DataFrame(comparison_rows),
        pd.DataFrame(anomaly_rows),
    )


def build_forward_holdout(
    source_detail: pd.DataFrame,
    daily_by_stock: Mapping[str, pd.DataFrame],
    *,
    source_manifest: pd.DataFrame,
    generated_at: str | None = None,
) -> tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    """Build the pre-registered forward holdout without mutating upstream artifacts."""

    generated = generated_at or _now_text()
    training_lineage = _validate_source_manifest(source_manifest)
    source = _normalize_source(source_detail).reset_index(drop=True)
    _validate_source_anomaly_boolean_contract(source)
    _validate_source_integer_contract(source)
    prices = _normalize_prices(daily_by_stock)
    observed_through_date = max(
        str(frame["date"].iloc[-1]) for frame in prices.values() if not frame.empty
    )
    if observed_through_date < HOLDOUT_START_DATE:
        raise RuntimeError(
            f"forward holdout price observation ends before holdout: {observed_through_date}"
        )
    if _constant(source.reset_index(drop=True), "artifact_id", label="source detail") != SOURCE_ARTIFACT_ID:
        raise RuntimeError("forward holdout source artifact id drift")
    if _constant(source.reset_index(drop=True), "artifact_version", label="source detail") != SOURCE_ARTIFACT_VERSION:
        raise RuntimeError("forward holdout source artifact version drift")
    current_monthly_lineage = {
        column: _require_sha256(
            _constant(source.reset_index(drop=True), column, label="source detail"),
            label=column,
        )
        for column in MONTHLY_LINEAGE_COLUMNS
    }
    for column in (
        "qualifying_source_dates",
        "qualifying_canonical_source_table_dates",
        "qualifying_trade_dates",
    ):
        tokens = (
            source[column]
            .astype(str)
            .str.split("|")
            .explode()
            .map(_date_text)
        )
        tokens = tokens.loc[tokens.ne("")]
        if tokens.gt(observed_through_date).any():
            raise RuntimeError(
                f"forward holdout source lineage exceeds observation cutoff: {column}"
            )
    source_sha = _canonical_frame_sha256(source.reset_index(drop=True))
    price_sha, price_sha_set, price_stock_count, price_row_count = _price_lineage(prices)
    capture_envelope = {
        "artifact_version": ARTIFACT_VERSION,
        "rule_canonical_sha256": RULE_CANONICAL_SHA256,
        "data_contract_sha256": DATA_CONTRACT_SHA256,
        "preregistration_merge_commit": PREREGISTRATION_MERGE_COMMIT,
        "observed_through_date": observed_through_date,
        "source_detail_canonical_sha256": source_sha,
        "price_input_canonical_sha256": price_sha,
        **current_monthly_lineage,
        **training_lineage,
    }
    capture_id = _canonical_json_sha256(capture_envelope)
    lineage = {
        "source_artifact_id": SOURCE_ARTIFACT_ID,
        "source_artifact_version": SOURCE_ARTIFACT_VERSION,
        "source_detail_canonical_sha256": source_sha,
        "price_input_canonical_sha256": price_sha,
        **current_monthly_lineage,
        **training_lineage,
    }
    bridge_rows = _event_rows_for_window(
        source,
        prices,
        window_start=BRIDGE_START_DATE,
        window_end=min(BRIDGE_END_DATE, observed_through_date),
        generated_at=generated,
        capture_id=capture_id,
        lineage=lineage,
    ) if observed_through_date >= BRIDGE_START_DATE else []
    event_rows = _event_rows_for_window(
        source,
        prices,
        window_start=HOLDOUT_START_DATE,
        window_end=observed_through_date,
        generated_at=generated,
        capture_id=capture_id,
        lineage=lineage,
    )
    detail = pd.DataFrame(event_rows, columns=DETAIL_COLUMNS)
    if detail.empty:
        detail = detail.copy()
    else:
        detail = detail.sort_values(
            ["stock_id", "trigger_date", "episode_key"], kind="mergesort"
        ).reset_index(drop=True)
        if detail["event_key"].duplicated().any():
            raise RuntimeError("forward holdout event detail has duplicate event keys")
        if detail["trigger_date"].astype(str).lt(HOLDOUT_START_DATE).any():
            raise RuntimeError("forward holdout bridge signal leaked into event detail")
        if _overlap_pair_count(detail):
            raise RuntimeError("forward holdout event detail contains same-stock overlap")
    summary, comparison, anomaly = _summary_frames(
        detail,
        generated_at=generated,
        capture_id=capture_id,
        bridge_excluded_count=len(bridge_rows),
    )
    primary_summary = summary.loc[summary["variant_id"].eq(PRIMARY_VARIANT_ID)].iloc[0]
    manifest_row = {
        "generated_at": generated,
        "model_id": MODEL_ID,
        "artifact_id": ARTIFACT_ID,
        "artifact_version": ARTIFACT_VERSION,
        "capture_id": capture_id,
        "artifact_row_key": "manifest",
        "preregistration_pr_number": PREREGISTRATION_PR_NUMBER,
        "preregistration_merge_commit": PREREGISTRATION_MERGE_COMMIT,
        "rule_contract_version": RULE_CONTRACT_VERSION,
        "rule_canonical_sha256": RULE_CANONICAL_SHA256,
        "data_contract_version": DATA_CONTRACT_VERSION,
        "data_contract_sha256": DATA_CONTRACT_SHA256,
        "training_cutoff_date": TRAINING_CUTOFF_DATE,
        "bridge_start_date": BRIDGE_START_DATE,
        "bridge_end_date": BRIDGE_END_DATE,
        "holdout_start_date": HOLDOUT_START_DATE,
        "observed_through_date": observed_through_date,
        "source_artifact_id": SOURCE_ARTIFACT_ID,
        "source_artifact_version": SOURCE_ARTIFACT_VERSION,
        "source_detail_row_count": len(source),
        "source_detail_canonical_sha256": source_sha,
        **current_monthly_lineage,
        **training_lineage,
        "price_input_stock_count": price_stock_count,
        "price_input_row_count": price_row_count,
        "price_input_stock_canonical_sha256s": price_sha_set,
        "price_input_canonical_sha256": price_sha,
        "bridge_excluded_signal_count": len(bridge_rows),
        "holdout_event_count": len(detail),
        "mature_event_count": int(detail["return_valid"].map(_bool_value).sum()),
        "right_censored_event_count": int(
            detail["right_censored"].map(_bool_value).sum()
        ),
        "primary_mature_count": int(primary_summary["mature_count"]),
        "primary_right_censored_count": int(primary_summary["right_censored_count"]),
        "holdout_status": "holdout_accumulating",
        "append_only_history": True,
        "research_only": True,
        "formal_model_use_allowed": False,
        "approved_for_daily": False,
        "presentation_allowed": False,
        "promotion_evidence_allowed": False,
        "ranking_consumption_allowed": False,
        "pdf_consumption_allowed": False,
        "production_change": False,
        "financial_statement_scope": FINANCIAL_STATEMENT_SCOPE,
    }
    manifest = pd.DataFrame([manifest_row])
    return manifest, detail, summary, comparison, anomaly


def _history_prefix_matches(base: pd.DataFrame, current: pd.DataFrame) -> bool:
    if list(base.columns) != list(current.columns) or len(current) < len(base):
        return False
    for offset in range(len(base)):
        left = base.iloc[offset]
        right = current.iloc[offset]
        left_mapping = {column: left[column] for column in base.columns}
        right_mapping = {column: right[column] for column in current.columns}
        if _canonical_mapping_sha256(
            left_mapping, excluded_columns=()
        ) != _canonical_mapping_sha256(
            right_mapping, excluded_columns=()
        ):
            return False
    return True


def _capture_blocks_are_contiguous(frame: pd.DataFrame) -> bool:
    """Return true when every capture_id occupies one contiguous history block."""

    seen: set[str] = set()
    previous: str | None = None
    for value in frame["capture_id"].astype(str):
        if value == previous:
            continue
        if value in seen:
            return False
        seen.add(value)
        previous = value
    return True


def validate_append_only_history(
    existing: pd.DataFrame,
    new: pd.DataFrame,
    *,
    immutable_base: pd.DataFrame | None = None,
) -> None:
    """Reject history rewrites; exact duplicate capture rows are idempotent.

    A different capture may be appended only when an immutable Git/base frame is
    supplied.  The current/new intersection alone cannot prove that an older,
    non-current capture was not rewritten.
    """

    required = {"capture_id", "artifact_row_key"}
    frames_to_check = [(existing, "existing"), (new, "new")]
    if immutable_base is not None:
        frames_to_check.append((immutable_base, "immutable base"))
    for frame, label in frames_to_check:
        missing = sorted(required - set(frame.columns))
        if missing:
            raise RuntimeError(f"forward holdout {label} history missing keys: {missing}")
        structural = frame[list(required)].astype(str).apply(
            lambda series: series.str.strip()
        )
        if structural.eq("").any().any():
            raise RuntimeError(f"forward holdout {label} history has blank structural keys")
        if frame.duplicated(["capture_id", "artifact_row_key"]).any():
            raise RuntimeError(f"forward holdout {label} history has duplicate keys")
        if not _capture_blocks_are_contiguous(frame):
            raise RuntimeError(
                f"forward holdout {label} history has non-contiguous capture blocks"
            )
    if list(existing.columns) != list(new.columns):
        raise RuntimeError("forward holdout append-only history schema drift")
    if immutable_base is not None:
        if not _history_prefix_matches(immutable_base, existing):
            raise RuntimeError(
                "forward holdout append-only immutable base prefix drift"
            )
    new_capture_ids = set(new["capture_id"].astype(str))
    if len(new_capture_ids) > 1:
        raise RuntimeError("forward holdout new history contains multiple captures")
    if existing.empty:
        return
    existing_index = existing.set_index(["capture_id", "artifact_row_key"], drop=False)
    new_index = new.set_index(["capture_id", "artifact_row_key"], drop=False)

    base_row_count = len(immutable_base) if immutable_base is not None else 0
    uncommitted_tail = existing.iloc[base_row_count:].copy()
    if not uncommitted_tail.empty:
        tail_index = uncommitted_tail.set_index(
            ["capture_id", "artifact_row_key"], drop=False
        )
        if set(tail_index.index) != set(new_index.index):
            if immutable_base is None:
                boundary = "immutable base is required"
            elif immutable_base.empty:
                boundary = "immutable base is absent for prior capture history"
            else:
                boundary = "uncommitted history tail is not the current capture"
            raise RuntimeError(
                f"forward holdout append-only {boundary}; commit the prior capture "
                "into the immutable base before appending another capture"
            )
        if list(tail_index.index) != list(new_index.index):
            raise RuntimeError(
                "forward holdout append-only uncommitted current-capture row order drift"
            )
        for key in tail_index.index:
            left = tail_index.loc[key]
            right = new_index.loc[key]
            left_mapping = {
                column: left[column]
                for column in uncommitted_tail.columns
                if column != "generated_at"
            }
            right_mapping = {
                column: right[column]
                for column in new.columns
                if column != "generated_at"
            }
            if _canonical_mapping_sha256(
                left_mapping
            ) != _canonical_mapping_sha256(right_mapping):
                raise RuntimeError(
                    "forward holdout append-only uncommitted history tail rewrite "
                    f"detected: {key}"
                )
    elif immutable_base is None and not set(existing_index.index).issubset(
        set(new_index.index)
    ):
        raise RuntimeError(
            "forward holdout append-only immutable base is required before a new "
            "capture can be appended"
        )
    if new_capture_ids:
        current_capture_id = next(iter(new_capture_ids))
        persisted_current = existing.loc[
            existing["capture_id"].astype(str).eq(current_capture_id)
        ]
        if not persisted_current.empty:
            if str(existing.iloc[-1]["capture_id"]) != current_capture_id:
                raise RuntimeError(
                    "forward holdout append-only current capture is stale; an existing "
                    "capture may be reused only when it is the terminal history block"
                )
            persisted_index = persisted_current.set_index(
                ["capture_id", "artifact_row_key"], drop=False
            )
            if set(persisted_index.index) != set(new_index.index):
                raise RuntimeError(
                    "forward holdout append-only terminal current-capture row presence drift"
                )
            if list(persisted_index.index) != list(new_index.index):
                raise RuntimeError(
                    "forward holdout append-only terminal current-capture row order drift"
                )
    for key in existing_index.index.intersection(new_index.index):
        left = existing_index.loc[key]
        right = new_index.loc[key]
        left_mapping = {
            column: left[column]
            for column in existing.columns
            if column != "generated_at"
        }
        right_mapping = {
            column: right[column]
            for column in new.columns
            if column != "generated_at"
        }
        if _canonical_mapping_sha256(left_mapping) != _canonical_mapping_sha256(
            right_mapping
        ):
            raise RuntimeError(
                f"forward holdout append-only history rewrite detected: {key}"
            )


def _csv_payload(frame: pd.DataFrame) -> bytes:
    buffer = io.StringIO(newline="")
    frame.to_csv(buffer, index=False, lineterminator="\n")
    return b"\xef\xbb\xbf" + buffer.getvalue().encode("utf-8")


def _stage_payload(target: Path, payload: bytes, *, role: str) -> Path:
    target.parent.mkdir(parents=True, exist_ok=True)
    temporary_path: Path | None = None
    try:
        with tempfile.NamedTemporaryFile(
            mode="wb",
            prefix=f".{target.name}.",
            suffix=f".{role}.tmp",
            dir=target.parent,
            delete=False,
        ) as handle:
            temporary_path = Path(handle.name)
            handle.write(payload)
            handle.flush()
            os.fsync(handle.fileno())
        return temporary_path
    except Exception:
        if temporary_path is not None:
            temporary_path.unlink(missing_ok=True)
        raise


def _replace_file(source: Path, target: Path) -> None:
    os.replace(source, target)


def _publish_payloads_transactionally(
    payloads: Mapping[Path, bytes],
    *,
    post_publish_check: Callable[[], None] | None = None,
) -> None:
    if len(payloads) != 15:
        raise RuntimeError(
            f"forward holdout publish transaction requires 15 paths, got {len(payloads)}"
        )
    targets = list(payloads)
    original_payloads: dict[Path, bytes | None] = {}
    staged: dict[Path, Path] = {}
    backups: dict[Path, Path | None] = {}
    try:
        for target in targets:
            if target.exists() and not target.is_file():
                raise RuntimeError(
                    f"forward holdout publish target is not a file: {target}"
                )
            original = target.read_bytes() if target.is_file() else None
            original_payloads[target] = original
            staged[target] = _stage_payload(target, payloads[target], role="staged")
            backups[target] = (
                _stage_payload(target, original, role="backup")
                if original is not None
                else None
            )
    except Exception as exc:
        for temporary in (*staged.values(), *backups.values()):
            if temporary is not None:
                temporary.unlink(missing_ok=True)
        raise RuntimeError(
            "forward holdout 15-path publish staging failed before target mutation"
        ) from exc

    try:
        for target in targets:
            _replace_file(staged[target], target)
        for target, expected in payloads.items():
            if target.read_bytes() != expected:
                raise RuntimeError(
                    f"forward holdout publish verification mismatch: {target}"
                )
        if post_publish_check is not None:
            post_publish_check()
    except Exception as exc:
        rollback_errors: list[str] = []
        for target in reversed(targets):
            original = original_payloads[target]
            try:
                if original is None:
                    target.unlink(missing_ok=True)
                    continue
                if target.is_file() and target.read_bytes() == original:
                    continue
                backup = backups[target]
                if backup is None or not backup.is_file():
                    backup = _stage_payload(target, original, role="rollback")
                    backups[target] = backup
                _replace_file(backup, target)
                backups[target] = None
                if target.read_bytes() != original:
                    raise RuntimeError("restored bytes do not match original")
            except Exception as rollback_exc:  # pragma: no cover - catastrophic I/O
                rollback_errors.append(f"{target}: {rollback_exc}")
        for temporary in (*staged.values(), *backups.values()):
            if temporary is not None:
                temporary.unlink(missing_ok=True)
        if rollback_errors:
            raise RuntimeError(
                "forward holdout 15-path publish failed and rollback was incomplete: "
                + "; ".join(rollback_errors)
            ) from exc
        raise RuntimeError(
            "forward holdout 15-path publish failed; every target was rolled back: "
            f"{exc}"
        ) from exc
    finally:
        for temporary in (*staged.values(), *backups.values()):
            if temporary is not None:
                temporary.unlink(missing_ok=True)


def _read_history_bytes(payload: bytes) -> pd.DataFrame:
    return pd.read_csv(
        io.BytesIO(payload),
        dtype={"stock_id": str, "capture_id": str, "artifact_row_key": str},
        keep_default_na=False,
        low_memory=False,
    )


def _ordered_frame_matches(
    expected: pd.DataFrame,
    observed: pd.DataFrame,
    *,
    excluded_columns: tuple[str, ...] = (),
) -> bool:
    """Compare one capture in row order with canonical numeric stability."""

    if list(expected.columns) != list(observed.columns) or len(expected) != len(observed):
        return False
    for offset in range(len(expected)):
        expected_mapping = {
            column: expected.iloc[offset][column]
            for column in expected.columns
            if column not in excluded_columns
        }
        observed_mapping = {
            column: observed.iloc[offset][column]
            for column in observed.columns
            if column not in excluded_columns
        }
        if _canonical_mapping_sha256(
            expected_mapping, excluded_columns=()
        ) != _canonical_mapping_sha256(observed_mapping, excluded_columns=()):
            return False
    return True


def _idempotent_mirror_payload(
    path: Path,
    persisted_capture: pd.DataFrame,
    *,
    authoritative_payload: bytes,
) -> bytes:
    """Validate one mirror, then return the history-owned current payload."""

    if not path.is_file():
        raise RuntimeError(
            "forward holdout idempotent capture is missing an existing mirror: "
            f"{path}"
        )
    existing_payload = path.read_bytes()
    observed = _read_history_bytes(existing_payload)
    if not _ordered_frame_matches(
        persisted_capture,
        observed,
        excluded_columns=("generated_at",),
    ):
        raise RuntimeError(
            "forward holdout idempotent mirror semantic drift detected: "
            f"{path}"
        )
    if existing_payload == authoritative_payload:
        return existing_payload
    # History owns the immutable capture timestamp and, when it contains only
    # this capture, its exact raw serialization.  Multi-capture histories cannot
    # be a latest/docs payload, so their caller supplies the canonical current
    # capture serialization instead.  Normalize any mirror drift only after the
    # semantic comparison above has passed fail closed.
    return authoritative_payload


def _git_history_base_frame(
    root: Path,
    path: Path,
    *,
    base_ref: str,
) -> pd.DataFrame | None:
    relative = path.relative_to(root).as_posix()
    try:
        result = subprocess.run(
            ["git", "show", f"{base_ref}:{relative}"],
            cwd=root,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            check=False,
            timeout=15,
        )
    except (OSError, subprocess.TimeoutExpired) as exc:
        raise RuntimeError(
            f"cannot read forward holdout immutable history base {base_ref}:{relative}: {exc}"
        ) from exc
    if result.returncode == 0:
        return _read_history_bytes(result.stdout)
    missing_markers = (
        b"does not exist in",
        b"exists on disk, but not in",
        b"Path '",
    )
    if any(marker in result.stderr for marker in missing_markers):
        return None
    detail = result.stderr.decode("utf-8", errors="replace").strip()
    raise RuntimeError(
        f"cannot resolve forward holdout immutable history base {base_ref}:{relative}"
        + (f": {detail}" if detail else "")
    )


def _combined_append_only_history(
    path: Path,
    frame: pd.DataFrame,
    *,
    immutable_base: pd.DataFrame | None = None,
) -> pd.DataFrame:
    if path.is_file():
        existing = pd.read_csv(
            path,
            dtype={"stock_id": str, "capture_id": str, "artifact_row_key": str},
            keep_default_na=False,
            low_memory=False,
        )
        validate_append_only_history(existing, frame, immutable_base=immutable_base)
        existing_keys = set(
            zip(existing["capture_id"].astype(str), existing["artifact_row_key"].astype(str))
        )
        additions = frame.loc[
            [
                (str(row.capture_id), str(row.artifact_row_key)) not in existing_keys
                for row in frame.itertuples(index=False)
            ]
        ]
        combined = pd.concat([existing, additions], ignore_index=True)
    else:
        if immutable_base is not None and not immutable_base.empty:
            raise RuntimeError(
                "forward holdout append-only history deleted its immutable base prefix: "
                f"{path}"
            )
        combined = frame.copy()
    return combined


def write_forward_holdout(
    manifest: pd.DataFrame,
    detail: pd.DataFrame,
    summary: pd.DataFrame,
    comparison: pd.DataFrame,
    anomaly_sensitivity: pd.DataFrame,
    *,
    output_root: Path | str = ROOT,
    history_base_ref: str | None = None,
    immutable_history_bases: Mapping[str, pd.DataFrame] | None = None,
    post_publish_check: Callable[[Mapping[str, Path]], None] | None = None,
) -> dict[str, Path]:
    frames = {
        "manifest": manifest,
        "detail": detail,
        "summary": summary,
        "comparison": comparison,
        "anomaly": anomaly_sensitivity,
    }
    root = Path(output_root)
    paths = {
        name: root / relative for name, relative in DEFAULT_OUTPUT_RELATIVE_PATHS.items()
    }
    lock_path = (
        root
        / "output/history/research"
        / f".{ARTIFACT_ID}.publish.lock"
    )
    lock_path.parent.mkdir(parents=True, exist_ok=True)
    lock_created = False
    lock_released = False
    try:
        try:
            descriptor = os.open(
                lock_path,
                os.O_CREAT | os.O_EXCL | os.O_WRONLY,
            )
        except FileExistsError as exc:
            raise RuntimeError(
                f"forward holdout publish lock is already held: {lock_path}"
            ) from exc
        lock_created = True
        try:
            os.write(descriptor, f"pid={os.getpid()}\n".encode("ascii"))
            os.fsync(descriptor)
        finally:
            os.close(descriptor)

        effective_base_ref = history_base_ref
        if effective_base_ref is None and root.resolve() == ROOT.resolve():
            effective_base_ref = os.environ.get(
                "REVENUE_FORWARD_HOLDOUT_HISTORY_BASE_REF", "HEAD"
            ).strip()
            if not effective_base_ref:
                raise RuntimeError(
                    "forward holdout immutable history base ref is blank"
                )
        if immutable_history_bases is not None:
            if set(immutable_history_bases) != set(frames):
                raise RuntimeError(
                    "forward holdout immutable history base surface set drift"
                )
            resolved_history_bases: dict[str, pd.DataFrame | None] = {
                artifact: immutable_history_bases[artifact]
                for artifact in frames
            }
        elif effective_base_ref is not None:
            resolved_history_bases = {
                artifact: _git_history_base_frame(
                    root,
                    paths[f"{artifact}_history"],
                    base_ref=effective_base_ref,
                )
                for artifact in frames
            }
            present_base_surfaces = {
                artifact
                for artifact, base in resolved_history_bases.items()
                if base is not None
            }
            if present_base_surfaces not in (set(), set(frames)):
                raise RuntimeError(
                    "forward holdout immutable history Git base must contain either "
                    "zero or all five surfaces"
                )
        else:
            resolved_history_bases = {artifact: None for artifact in frames}
        histories: dict[str, pd.DataFrame] = {}
        for artifact, frame in frames.items():
            immutable_base = resolved_history_bases[artifact]
            histories[artifact] = _combined_append_only_history(
                paths[f"{artifact}_history"],
                frame,
                immutable_base=immutable_base,
            )
        current_capture_ids = set(manifest["capture_id"].astype(str))
        if len(current_capture_ids) != 1:
            raise RuntimeError(
                "forward holdout publish requires exactly one current manifest capture"
            )
        current_capture_id = next(iter(current_capture_ids))
        existing_history_frames: dict[str, pd.DataFrame | None] = {}
        existing_history_payloads: dict[str, bytes | None] = {}
        for artifact in frames:
            history_path = paths[f"{artifact}_history"]
            if history_path.is_file():
                existing_payload = history_path.read_bytes()
                existing_history_payloads[artifact] = existing_payload
                existing_history_frames[artifact] = _read_history_bytes(existing_payload)
            else:
                existing_history_payloads[artifact] = None
                existing_history_frames[artifact] = None
        existing_manifest_history = existing_history_frames["manifest"]
        idempotent_capture = bool(
            existing_manifest_history is not None
            and not existing_manifest_history.empty
            and existing_manifest_history["capture_id"]
            .astype(str)
            .eq(current_capture_id)
            .any()
        )
        payloads: dict[Path, bytes] = {}
        for artifact, frame in frames.items():
            if not idempotent_capture:
                payloads[paths[f"{artifact}_history"]] = _csv_payload(
                    histories[artifact]
                )
                payloads[paths[f"{artifact}_latest"]] = _csv_payload(frame)
                payloads[paths[f"{artifact}_docs"]] = _csv_payload(frame)
                continue

            existing_history = existing_history_frames[artifact]
            existing_history_payload = existing_history_payloads[artifact]
            if existing_history is None or existing_history_payload is None:
                raise RuntimeError(
                    "forward holdout idempotent capture has a partial history surface set"
                )
            if frame.empty:
                persisted_capture = frame.copy()
            else:
                persisted_capture = existing_history.loc[
                    existing_history["capture_id"]
                    .astype(str)
                    .eq(current_capture_id)
                ].copy()
                if persisted_capture.empty:
                    raise RuntimeError(
                        "forward holdout idempotent capture is missing from history "
                        f"surface: {artifact}"
                    )
                if not _ordered_frame_matches(
                    persisted_capture,
                    frame,
                    excluded_columns=("generated_at",),
                ):
                    raise RuntimeError(
                        "forward holdout idempotent capture semantic drift detected in "
                        f"history surface: {artifact}"
                    )
            payloads[paths[f"{artifact}_history"]] = existing_history_payload
            history_capture_ids = set(existing_history["capture_id"].astype(str))
            history_is_current_only = history_capture_ids == {current_capture_id}
            if frame.empty and existing_history.empty:
                history_is_current_only = True
            authoritative_mirror_payload = (
                existing_history_payload
                if history_is_current_only
                else _csv_payload(persisted_capture)
            )
            payloads[paths[f"{artifact}_latest"]] = _idempotent_mirror_payload(
                paths[f"{artifact}_latest"],
                persisted_capture,
                authoritative_payload=authoritative_mirror_payload,
            )
            payloads[paths[f"{artifact}_docs"]] = _idempotent_mirror_payload(
                paths[f"{artifact}_docs"],
                persisted_capture,
                authoritative_payload=authoritative_mirror_payload,
            )
        if set(payloads) != set(paths.values()):
            raise RuntimeError("forward holdout publish path set drift")

        def validate_persisted_publish() -> None:
            if post_publish_check is not None:
                post_publish_check(paths)

        _publish_payloads_transactionally(
            payloads,
            post_publish_check=validate_persisted_publish,
        )
        # _publish_payloads_transactionally returns only after its staged and
        # backup temporaries have been cleaned, so no second writer can enter
        # while any part of this transaction is still live.
        lock_path.unlink()
        lock_released = True
        return paths
    finally:
        if lock_created and not lock_released:
            lock_path.unlink(missing_ok=True)


def _materialize_current_forward_holdout_inputs() -> tuple[
    pd.DataFrame,
    dict[str, pd.DataFrame],
    pd.DataFrame,
]:
    """Materialize one explicitly bounded input bundle for build and replay."""

    from build_daily_model_parameter_research import (
        _attach_revenue_signal_market_regime,
        _revenue_unreacted_timing_prepared_frame,
    )
    from revenue_unreacted_range_research_frame import (
        build_revenue_unreacted_range_research_frame,
    )

    frame = build_revenue_unreacted_range_research_frame()
    if frame.empty:
        raise RuntimeError("No price history available for revenue forward holdout")
    prepared = _attach_revenue_signal_market_regime(
        _revenue_unreacted_timing_prepared_frame(frame)
    )
    if "date" not in prepared.columns:
        raise RuntimeError("revenue forward holdout prepared price frame missing date")
    observed_price_dates = prepared["date"].map(_date_text)
    if observed_price_dates.eq("").any():
        raise RuntimeError("revenue forward holdout prepared price frame has invalid date")
    observation_cutoff_date = str(observed_price_dates.max())
    _summary, source_detail = build_source_first_condition_audit(
        observation_cutoff_date=observation_cutoff_date
    )
    source_detail = _attach_qualifying_anomaly_flags(source_detail, prepared)
    daily_by_stock = prepare_daily_by_stock(prepared, source_detail)
    source_manifest = load_source_snapshot_projection_manifest()
    return source_detail, daily_by_stock, source_manifest


def build_current_forward_holdout() -> tuple[
    pd.DataFrame,
    pd.DataFrame,
    pd.DataFrame,
    pd.DataFrame,
    pd.DataFrame,
]:
    """Build current forward evidence from one price-capped input bundle."""

    source_detail, daily_by_stock, source_manifest = (
        _materialize_current_forward_holdout_inputs()
    )
    return build_forward_holdout(
        source_detail,
        daily_by_stock,
        source_manifest=source_manifest,
    )


def build_and_write_current_forward_holdout(
    *,
    final_validation: Callable[..., None] | None = None,
) -> dict[str, Path]:
    source_detail, daily_by_stock, source_manifest = (
        _materialize_current_forward_holdout_inputs()
    )
    frames = build_forward_holdout(
        source_detail,
        daily_by_stock,
        source_manifest=source_manifest,
    )
    # The independent validator receives the exact explicit input bundle used by
    # this capture.  It does not import this producer or rebuild business inputs.
    from validate_revenue_unreacted_range_forward_holdout import (
        load_history_base_frames_from_git,
        validate_frames,
    )

    def replay(
        candidate_frames: tuple[pd.DataFrame, ...] | list[pd.DataFrame],
        *,
        history_frames: Mapping[str, pd.DataFrame] | None = None,
        immutable_history_base_frames: Mapping[str, pd.DataFrame] | None = None,
    ) -> None:
        errors = validate_frames(
            *candidate_frames,
            source_detail=source_detail,
            daily_by_stock=daily_by_stock,
            source_manifest=source_manifest,
            history_frames=history_frames,
            immutable_history_base_frames=immutable_history_base_frames,
        )
        if not errors:
            return
        raise RuntimeError(
            "forward holdout independent replay failed: " + "; ".join(errors)
        )

    def read_persisted(
        paths: Mapping[str, Path],
    ) -> tuple[list[pd.DataFrame], dict[str, pd.DataFrame]]:
        def read(path: Path) -> pd.DataFrame:
            return pd.read_csv(
                path,
                dtype={
                    "stock_id": str,
                    "trigger_date": str,
                    "entry_date": str,
                    "exit_date": str,
                    "capture_id": str,
                    "artifact_row_key": str,
                },
                keep_default_na=False,
                low_memory=False,
            )

        names = ("manifest", "detail", "summary", "comparison", "anomaly")
        latest = [read(paths[f"{name}_latest"]) for name in names]
        histories = {name: read(paths[f"{name}_history"]) for name in names}
        return latest, histories

    replay(frames)

    def replay_persisted(paths: Mapping[str, Path]) -> None:
        persisted_latest, persisted_histories = read_persisted(paths)
        immutable_bases: Mapping[str, pd.DataFrame] | None = None
        try:
            is_repository_publish = all(
                path.resolve().is_relative_to(ROOT.resolve()) for path in paths.values()
            )
        except AttributeError:  # pragma: no cover - Python <3.9 compatibility
            is_repository_publish = all(
                str(path.resolve()).startswith(str(ROOT.resolve()))
                for path in paths.values()
            )
        if is_repository_publish:
            base_ref = os.environ.get(
                "REVENUE_FORWARD_HOLDOUT_HISTORY_BASE_REF", "HEAD"
            ).strip()
            immutable_bases = load_history_base_frames_from_git(base_ref)
        replay(
            persisted_latest,
            history_frames=persisted_histories,
            immutable_history_base_frames=immutable_bases,
        )
        if final_validation is not None:
            final_validation(
                manifest_readback=persisted_latest[0],
                detail_readback=persisted_latest[1],
                summary_readback=persisted_latest[2],
                comparison_readback=persisted_latest[3],
                anomaly_readback=persisted_latest[4],
                source_detail=source_detail,
                price_inputs=daily_by_stock,
                source_manifest=source_manifest,
                history_frames=persisted_histories,
                immutable_history_base_frames=immutable_bases,
            )

    with tempfile.TemporaryDirectory(
        prefix="revenue-forward-holdout-",
        dir=str(ROOT.parent),
    ) as temporary_root:
        staged_paths = write_forward_holdout(
            *frames,
            output_root=temporary_root,
            post_publish_check=replay_persisted,
        )

    paths = write_forward_holdout(*frames, post_publish_check=replay_persisted)
    return paths
