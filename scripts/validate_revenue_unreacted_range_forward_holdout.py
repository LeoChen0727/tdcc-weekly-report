from __future__ import annotations

import argparse
from decimal import Decimal, InvalidOperation, ROUND_HALF_EVEN
import hashlib
import io
import json
import math
import numbers
from pathlib import Path
import re
import subprocess
from typing import Mapping

import numpy as np
import pandas as pd


ROOT = Path(__file__).resolve().parents[1]
MODEL_ID = "revenue_unreacted_range"
ARTIFACT_ID = "revenue_unreacted_range_forward_holdout"
ARTIFACT_VERSION = "forward_holdout_v1_20260811"
CANONICAL_LINEAGE_VERSION = "canonical_json_numeric_text_v1"

# Disabled for the frozen v1 family.  The independently owned v2 validator
# supplies the exact migration constants through its isolated context.
PRICE_SEMANTIC_PROJECTION_ENABLED = False
PRICE_SEMANTIC_PROJECTION_VERSION = ""
PRICE_SEMANTIC_PROJECTION_DECIMAL_SCALE = 8
PRICE_SEMANTIC_PROJECTION_SCHEMA_SHA256 = ""
PRICE_SEMANTIC_PROJECTION_MIGRATION_ID = ""
PRICE_SEMANTIC_PROJECTION_AUTHORIZATION_REFERENCE = ""
PRICE_SEMANTIC_PROJECTION_NUMERIC_COLUMNS = (
    "open",
    "high",
    "low",
    "close",
    "analysis_price_adjustment_factor",
)
PRICE_SEMANTIC_PROJECTION_TEXT_COLUMNS = ("price_resolution_ids_on_date",)
PRICE_SEMANTIC_PROJECTION_COLUMNS = (
    "session_sequence_index",
    "date",
    *PRICE_SEMANTIC_PROJECTION_NUMERIC_COLUMNS,
    *PRICE_SEMANTIC_PROJECTION_TEXT_COLUMNS,
)
PRICE_INPUT_PROVENANCE_DIAGNOSTIC_COLUMNS = (
    "price_input_stock_canonical_sha256s",
    "price_input_canonical_sha256",
)
APPEND_ONLY_SCHEMA_EXTENSION_COLUMNS_BY_ARTIFACT: Mapping[
    str, tuple[str, ...]
] = {}

PREREGISTRATION_MERGE_COMMIT = "436c25cd0d037c3425ab2ac4fa76cb464cf96de4"
PREREGISTRATION_PR_NUMBER = "462"
PR462_PROJECTED_EPISODE_ROW_COUNT = 19569
PR462_PROJECTED_EPISODE_SEMANTIC_SHA256 = (
    "92c68810ac2b5718d714d450fe83bf23f2f3469fec5db0ae2753330950ab2cf5"
)
TRAINING_CUTOFF_DATE = "20260713"
BRIDGE_START_DATE = "20260714"
BRIDGE_END_DATE = "20260803"
HOLDOUT_START_DATE = "20260804"
SOURCE_PROJECTION_ARTIFACT_ID = "revenue_unreacted_range_source_snapshot_projection"
SOURCE_PROJECTION_ARTIFACT_VERSION = "source_snapshot_projection_v1_20260731"
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
HOLDING_SESSION_INDEX_OFFSET = 29
WATCH_HORIZON_TRADING_DAYS = 60
OPERATION_RETURN_REVIEW_THRESHOLD_PCT = 80.0
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
FINANCIAL_STATEMENT_SCOPE = str(RULE_CONTRACT["financial_statement_scope"])
ANOMALY_POLICY = str(RULE_CONTRACT["anomaly_policy"])
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

# The original v1 validator remains fail closed before 20260804.  A separately
# registered v2 wrapper enables this only for its one pre-start empty capture.
ALLOW_PRE_START_EMPTY_CAPTURE = False

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
DETAIL_BUSINESS_BOOLEAN_COLUMNS = (
    "primary_variant_member",
    "low_falling_member",
    "low_or_mid_falling_union_member",
    "return_valid",
    "right_censored",
    "realized_return_ge20",
    "operation_return_review_candidate_flag",
    "anomaly_candidate_flag",
    "source_anomaly_candidate_flag",
    "unresolved_price_path_candidate_flag",
    "primary_metric_included",
    "sensitivity_metric_included",
    "same_stock_non_overlap_applied",
)
INTEGER_METRIC_COLUMNS = (
    "event_count",
    "mature_count",
    "right_censored_count",
    "win_count",
    "neutral_count",
    "failure_count",
    "return_ge20_count",
    "loss_count",
    "same_stock_overlap_pair_count",
)
CONTINUOUS_METRIC_COLUMNS = (
    "win_rate_pct",
    "average_return_pct",
    "median_return_pct",
    "p10_return_pct",
    "p90_return_pct",
)
SHA256_PATTERN = re.compile(r"^[0-9a-f]{64}$")

DEFAULT_PATHS = {
    "manifest": ROOT / f"output/latest/research_backtest/{ARTIFACT_ID}_manifest_latest.csv",
    "detail": ROOT / f"output/latest/research_backtest/{ARTIFACT_ID}_event_detail_latest.csv",
    "summary": ROOT / f"output/latest/research_backtest/{ARTIFACT_ID}_maturity_status_latest.csv",
    "comparison": ROOT / f"output/latest/research_backtest/{ARTIFACT_ID}_comparison_latest.csv",
    "anomaly": ROOT / f"output/latest/research_backtest/{ARTIFACT_ID}_anomaly_sensitivity_latest.csv",
    "manifest_history": ROOT / f"output/history/research/{ARTIFACT_ID}_manifest.csv",
    "detail_history": ROOT / f"output/history/research/{ARTIFACT_ID}_event_detail.csv",
    "summary_history": ROOT / f"output/history/research/{ARTIFACT_ID}_maturity_status.csv",
    "comparison_history": ROOT / f"output/history/research/{ARTIFACT_ID}_comparison.csv",
    "anomaly_history": ROOT / f"output/history/research/{ARTIFACT_ID}_anomaly_sensitivity.csv",
    "source_manifest": ROOT / "output/latest/research_backtest/revenue_unreacted_range_source_snapshot_projection_manifest_latest.csv",
}


def _bool(value: object) -> bool:
    return str(value).strip().lower() in {"true", "1", "yes"}


def _strict_bool(value: object, *, label: str) -> bool:
    token = str(value).strip().lower()
    if token in {"true", "1", "yes"}:
        return True
    if token in {"false", "0", "no"}:
        return False
    raise RuntimeError(f"{label} is not canonical boolean text")


def _validate_source_anomaly_boolean_contract(source: pd.DataFrame) -> None:
    scalar_columns = (
        "qualifying_source_revenue_anomaly_candidate_flag",
        "unresolved_price_path_candidate_flag",
    )
    if "start_source_revenue_anomaly_candidate_flag" in source.columns:
        scalar_columns = (*scalar_columns, "start_source_revenue_anomaly_candidate_flag")
    for column in scalar_columns:
        if column not in source.columns:
            raise RuntimeError(f"source anomaly contract missing column: {column}")
        for row_index, value in source[column].items():
            _strict_bool(
                value,
                label=f"source anomaly {column} row={row_index}",
            )
    list_column = "qualifying_source_revenue_anomaly_candidate_flags"
    if list_column not in source.columns:
        raise RuntimeError(f"source anomaly contract missing column: {list_column}")
    for row_index, value in source[list_column].items():
        tokens = [token.strip() for token in str(value).split("|") if token.strip()]
        if not tokens:
            raise RuntimeError(f"source anomaly flag lineage is empty: row={row_index}")
        for position, token in enumerate(tokens):
            _strict_bool(
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
        raise RuntimeError(f"source integer contract missing: {missing}")
    for row_index, row in source.iterrows():
        count_valid, count = _exact_integer_value(row["qualifying_update_count"])
        if not count_valid or count is None or count <= 0:
            raise RuntimeError(
                f"source qualifying update count is not a positive exact integer: row={row_index}"
            )
        sequence_tokens = [
            token.strip()
            for token in str(row["qualifying_sequence_indices"]).split("|")
            if token.strip()
        ]
        sequences: list[int] = []
        for position, token in enumerate(sequence_tokens):
            valid, sequence = _exact_integer_value(token)
            if not valid or sequence is None or sequence < 0:
                raise RuntimeError(
                    "source qualifying sequence is not an exact non-negative integer: "
                    f"row={row_index} position={position}"
                )
            sequences.append(sequence)
        if len(sequences) != count:
            raise RuntimeError(f"source sequence/count contract drift: row={row_index}")
        start_valid, start = _exact_integer_value(row["episode_start_sequence_index"])
        latest_valid, latest = _exact_integer_value(
            row["latest_qualifying_sequence_index"]
        )
        if (
            not start_valid
            or not latest_valid
            or start is None
            or latest is None
            or start != sequences[0]
            or latest != sequences[-1]
        ):
            raise RuntimeError(f"source scalar/list sequence drift: row={row_index}")


def _validate_strict_boolean_columns(
    frame: pd.DataFrame,
    columns: tuple[str, ...],
    *,
    label: str,
    errors: list[str],
) -> None:
    for column in columns:
        if column not in frame.columns:
            errors.append(f"{label} missing boolean contract column: {column}")
            continue
        for row_index, value in frame[column].items():
            try:
                _strict_bool(
                    value,
                    label=f"{label} {column} row={row_index}",
                )
            except RuntimeError as exc:
                errors.append(str(exc))


def _date(value: object) -> str:
    text = "".join(character for character in str(value or "") if character.isdigit())
    return text[:8] if len(text) >= 8 else ""


def _stock_id(value: object) -> str:
    text = str(value or "").strip()
    if text.endswith(".0") and text[:-2].isdigit():
        text = text[:-2]
    return text.zfill(4) if text.isdigit() else text


def _number(value: object) -> float:
    result = pd.to_numeric(value, errors="coerce")
    return float(result) if pd.notna(result) else math.nan


def _is_canonical_blank_numeric(value: object) -> bool:
    if value is None:
        return True
    if isinstance(value, (str, bytes)):
        return not str(value).strip()
    try:
        return bool(pd.isna(value))
    except (TypeError, ValueError):
        return False


def _equal_number(left: object, right: object, tolerance: float = 0.00011) -> bool:
    left_number = _number(left)
    right_number = _number(right)
    if not np.isfinite(left_number) and not np.isfinite(right_number):
        return _is_canonical_blank_numeric(left) and _is_canonical_blank_numeric(
            right
        )
    return bool(
        np.isfinite(left_number)
        and np.isfinite(right_number)
        and math.isclose(left_number, right_number, abs_tol=tolerance)
    )


def _exact_integer_value(value: object) -> tuple[bool, int | None]:
    if value is None or (
        not isinstance(value, (str, bytes)) and pd.isna(value)
    ):
        return True, None
    text = str(value).strip()
    if not text:
        return True, None
    try:
        number = Decimal(text)
    except InvalidOperation:
        return False, None
    if not number.is_finite() or number != number.to_integral_value():
        return False, None
    return True, int(number)


def _equal_exact_integer(left: object, right: object) -> bool:
    left_valid, left_value = _exact_integer_value(left)
    right_valid, right_value = _exact_integer_value(right)
    return left_valid and right_valid and left_value == right_value


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
    if value is None or (
        not isinstance(value, (list, dict, tuple)) and pd.isna(value)
    ):
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


def _json_sha(payload: object) -> str:
    return hashlib.sha256(
        json.dumps(payload, ensure_ascii=False, separators=(",", ":"), sort_keys=True).encode(
            "utf-8"
        )
    ).hexdigest()


RULE_CANONICAL_SHA256 = _json_sha(RULE_CONTRACT)
DATA_CONTRACT_SHA256 = _json_sha(DATA_CONTRACT)


def _frame_sha(frame: pd.DataFrame) -> str:
    columns = sorted(column for column in frame.columns if column != "generated_at")
    rows = [
        [_canonical_value(value) for value in row]
        for row in frame.loc[:, columns].itertuples(index=False, name=None)
    ]
    rows.sort()
    return _json_sha([CANONICAL_LINEAGE_VERSION, columns, rows])


def _mapping_sha(
    mapping: Mapping[str, object],
    *,
    excluded_columns: tuple[str, ...] = ("generated_at",),
) -> str:
    payload = [
        [str(key), _canonical_value(value)]
        for key, value in sorted(mapping.items())
        if str(key) not in excluded_columns
    ]
    return _json_sha([CANONICAL_LINEAGE_VERSION, payload])


def _source_numeric_text(text: str) -> str | None:
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


def _source_value(value: object) -> str:
    if value is None or (not isinstance(value, (str, bytes)) and pd.isna(value)):
        return ""
    if isinstance(value, (bool, np.bool_)):
        return "true" if bool(value) else "false"
    if isinstance(value, (numbers.Integral, numbers.Real, Decimal)):
        number = float(value)
        if not np.isfinite(number):
            return ""
        numeric = _source_numeric_text(str(value))
        return numeric if numeric is not None else str(value).strip()
    text = str(value).strip()
    if text.lower() in {"true", "false"}:
        return text.lower()
    numeric = _source_numeric_text(text)
    return numeric if numeric is not None else text


def _source_mapping_sha(mapping: Mapping[str, object]) -> str:
    payload = [
        [str(key), _source_value(value)]
        for key, value in sorted(mapping.items())
        if str(key) != "generated_at"
    ]
    return hashlib.sha256(
        json.dumps(payload, ensure_ascii=False, separators=(",", ":")).encode("utf-8")
    ).hexdigest()


def _source_table_sha(frame: pd.DataFrame) -> str:
    columns = sorted(column for column in frame.columns if column != "generated_at")
    rows = sorted(
        [[_source_value(row[column]) for column in columns] for _, row in frame.iterrows()]
    )
    payload = {
        "canonical_lineage_version": CANONICAL_LINEAGE_VERSION,
        "columns": columns,
        "rows": rows,
    }
    return hashlib.sha256(
        json.dumps(payload, ensure_ascii=False, separators=(",", ":")).encode("utf-8")
    ).hexdigest()


def _normalize_source(source_detail: pd.DataFrame) -> pd.DataFrame:
    required = {
        "artifact_id",
        "artifact_version",
        "condition_variant_id",
        "episode_key",
        "stock_id",
        "stock_name",
        "episode_start_trade_date",
        "qualifying_update_count",
        "qualifying_revenue_periods",
        "qualifying_source_dates",
        "qualifying_cross_market_resolution_ids",
        "qualifying_source_row_canonical_sha256s",
        "qualifying_canonical_source_table_dates",
        "qualifying_trade_dates",
        "qualifying_sequence_indices",
        "qualifying_source_revenue_anomaly_candidate_flags",
        "qualifying_source_revenue_anomaly_candidate_flag",
        "unresolved_price_path_candidate_flag",
        *MONTHLY_LINEAGE_COLUMNS,
    }
    missing = sorted(required - set(source_detail.columns))
    if missing:
        raise RuntimeError(f"source detail missing columns: {missing}")
    source = source_detail.loc[
        source_detail["condition_variant_id"].astype(str).eq(SOURCE_VARIANT_ID)
    ].copy()
    if source.empty:
        raise RuntimeError("source detail has no pre-registered source variant")
    if not source["artifact_id"].astype(str).eq(SOURCE_ARTIFACT_ID).all():
        raise RuntimeError("source artifact id drift")
    if not source["artifact_version"].astype(str).eq(SOURCE_ARTIFACT_VERSION).all():
        raise RuntimeError("source artifact version drift")
    if source["episode_key"].astype(str).duplicated().any():
        raise RuntimeError("source detail has duplicate episode keys")
    source["stock_id"] = source["stock_id"].map(
        lambda value: str(value)[:-2]
        if str(value).endswith(".0") and str(value)[:-2].isdigit()
        else str(value).strip()
    )
    slice_sha = _source_table_sha(source)
    source["source_first_canonical_row_sha256"] = source.apply(
        lambda row: _source_mapping_sha(row.to_dict()), axis=1
    )
    source["source_first_selected_slice_canonical_sha256"] = slice_sha
    return source.reset_index(drop=True)


def _normalize_prices(
    daily_by_stock: Mapping[str, pd.DataFrame],
) -> dict[str, pd.DataFrame]:
    result: dict[str, pd.DataFrame] = {}
    for raw_stock_id, raw in daily_by_stock.items():
        stock_id = _stock_id(raw_stock_id)
        frame = raw.copy()
        if "date" not in frame.columns:
            raise RuntimeError(f"price input missing date: {stock_id}")
        frame["date"] = frame["date"].map(_date)
        if frame["date"].eq("").any() or frame["date"].duplicated().any():
            raise RuntimeError(f"price input has invalid or duplicate dates: {stock_id}")
        frame = frame.sort_values("date", kind="mergesort").reset_index(drop=True)
        for basis in ("open", "high", "low", "close"):
            analysis = f"analysis_{basis}"
            if analysis not in frame.columns:
                if basis not in frame.columns:
                    raise RuntimeError(f"price input missing {analysis}: {stock_id}")
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
                        "derived price field differs from frozen analysis_close "
                        f"formula: {stock_id}/{column}/row={first + 2}"
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
                lambda value: _strict_bool(
                    value,
                    label=f"cross_breakout_prev20/{stock_id}",
                )
            )
            if not observed_cross.equals(canonical_cross):
                mismatch = observed_cross.ne(canonical_cross)
                first = int(np.flatnonzero(mismatch.to_numpy())[0])
                raise RuntimeError(
                    "derived price field differs from frozen analysis_close formula: "
                    f"{stock_id}/cross_breakout_prev20/row={first + 2}"
                )
        frame["cross_breakout_prev20"] = canonical_cross
        result[stock_id] = frame
    if not result:
        raise RuntimeError("price input is empty")
    return result


def _price_lineage(
    prices: Mapping[str, pd.DataFrame],
) -> tuple[str, str, int, int]:
    rows = [
        {"stock_id": stock_id, "price_canonical_sha256": _frame_sha(frame)}
        for stock_id, frame in sorted(prices.items())
    ]
    return (
        _frame_sha(pd.DataFrame(rows)),
        "|".join(
            f"{row['stock_id']}:{row['price_canonical_sha256']}" for row in rows
        ),
        len(rows),
        sum(len(frame) for frame in prices.values()),
    )


def _price_semantic_decimal_text(value: object, *, column: str) -> str:
    if value is None or pd.isna(value):
        return ""
    try:
        number = Decimal(str(value).strip())
        quantum = Decimal(1).scaleb(-PRICE_SEMANTIC_PROJECTION_DECIMAL_SCALE)
        quantized = number.quantize(quantum, rounding=ROUND_HALF_EVEN)
    except (InvalidOperation, ValueError) as exc:
        raise RuntimeError(
            f"price semantic projection has invalid {column}"
        ) from exc
    if not quantized.is_finite():
        raise RuntimeError(f"price semantic projection has non-finite {column}")
    if quantized == 0:
        quantized = abs(quantized)
    return f"{quantized:.{PRICE_SEMANTIC_PROJECTION_DECIMAL_SCALE}f}"


def _price_semantic_lineage(
    prices: Mapping[str, pd.DataFrame],
    *,
    cutoff_date: str,
) -> tuple[str, str, int, int]:
    """Independently hash canonical raw price rows, not derived floats."""

    if not PRICE_SEMANTIC_PROJECTION_VERSION:
        raise RuntimeError("price semantic projection version is blank")
    if not SHA256_PATTERN.fullmatch(PRICE_SEMANTIC_PROJECTION_SCHEMA_SHA256):
        raise RuntimeError("price semantic projection schema SHA-256 is invalid")
    cutoff = _date(cutoff_date)
    if not cutoff:
        raise RuntimeError("price semantic projection cutoff is invalid")
    canonical_inputs: dict[str, pd.DataFrame] = {}
    for raw_stock_id, frame in prices.items():
        stock_id = _stock_id(raw_stock_id)
        if stock_id in canonical_inputs:
            raise RuntimeError(
                f"price semantic projection duplicate stock: {stock_id}"
            )
        canonical_inputs[stock_id] = frame
    stock_rows: list[list[object]] = []
    stock_tokens: list[str] = []
    row_count = 0
    required_columns = {
        "date",
        *PRICE_SEMANTIC_PROJECTION_NUMERIC_COLUMNS,
        *PRICE_SEMANTIC_PROJECTION_TEXT_COLUMNS,
    }
    for stock_id, raw in sorted(canonical_inputs.items()):
        missing = sorted(required_columns - set(raw.columns))
        if missing:
            raise RuntimeError(
                f"price semantic projection missing columns: {stock_id}/{missing}"
            )
        frame = raw.loc[
            :,
            [
                "date",
                *PRICE_SEMANTIC_PROJECTION_NUMERIC_COLUMNS,
                *PRICE_SEMANTIC_PROJECTION_TEXT_COLUMNS,
            ],
        ].copy()
        frame["date"] = frame["date"].map(_date)
        if frame["date"].eq("").any() or frame["date"].duplicated().any():
            raise RuntimeError(f"price semantic projection date/order drift: {stock_id}")
        frame = frame.loc[frame["date"].le(cutoff)].sort_values(
            "date", kind="mergesort"
        ).reset_index(drop=True)
        rows: list[list[str]] = []
        for sequence_index, (_, row) in enumerate(frame.iterrows()):
            rows.append(
                [
                    str(sequence_index),
                    str(row["date"]).strip(),
                    *[
                        _price_semantic_decimal_text(row[column], column=column)
                        for column in PRICE_SEMANTIC_PROJECTION_NUMERIC_COLUMNS
                    ],
                    *[
                        ""
                        if row[column] is None or pd.isna(row[column])
                        else str(row[column]).strip()
                        for column in PRICE_SEMANTIC_PROJECTION_TEXT_COLUMNS
                    ],
                ]
            )
        digest = _json_sha(
            [
                PRICE_SEMANTIC_PROJECTION_VERSION,
                PRICE_SEMANTIC_PROJECTION_SCHEMA_SHA256,
                RULE_CANONICAL_SHA256,
                DATA_CONTRACT_SHA256,
                stock_id,
                cutoff,
                list(PRICE_SEMANTIC_PROJECTION_COLUMNS),
                rows,
            ]
        )
        stock_rows.append([stock_id, len(rows), digest])
        stock_tokens.append(f"{stock_id}:{digest}")
        row_count += len(rows)
    return (
        _json_sha(
            [
                PRICE_SEMANTIC_PROJECTION_VERSION,
                PRICE_SEMANTIC_PROJECTION_SCHEMA_SHA256,
                RULE_CANONICAL_SHA256,
                DATA_CONTRACT_SHA256,
                cutoff,
                stock_rows,
            ]
        ),
        "|".join(stock_tokens),
        len(stock_rows),
        row_count,
    )


def _training_lineage(source_manifest: pd.DataFrame) -> dict[str, object]:
    if len(source_manifest) != 1:
        raise RuntimeError("training source manifest must contain exactly one row")
    row = source_manifest.iloc[0]
    expected = {
        "artifact_id": SOURCE_PROJECTION_ARTIFACT_ID,
        "artifact_version": SOURCE_PROJECTION_ARTIFACT_VERSION,
        "cutoff_date": TRAINING_CUTOFF_DATE,
    }
    for column, value in expected.items():
        if str(row.get(column, "")).strip() != value:
            raise RuntimeError(f"training source projection drift: {column}")
    row_count_valid, row_count = _exact_integer_value(
        row.get("projected_episode_row_count", "")
    )
    if not row_count_valid or row_count is None:
        raise RuntimeError("training projected episode row count is not an exact integer")
    if row_count != PR462_PROJECTED_EPISODE_ROW_COUNT:
        raise RuntimeError(
            "PR462 projected episode row count drift: "
            f"expected={PR462_PROJECTED_EPISODE_ROW_COUNT} observed={row_count}"
        )
    semantic_sha = str(row.get("projected_episode_semantic_sha256", "")).strip().lower()
    if semantic_sha != PR462_PROJECTED_EPISODE_SEMANTIC_SHA256:
        raise RuntimeError("PR462 projected episode semantic SHA-256 drift")
    if not _strict_bool(
        row.get("research_only", ""),
        label="training source projection research_only",
    ):
        raise RuntimeError("training source projection must remain research-only")
    for column in (
        "formal_model_use_allowed",
        "approved_for_daily",
        "production_change",
        "promotion_evidence_allowed",
        "ranking_consumption_allowed",
        "pdf_consumption_allowed",
    ):
        if column not in source_manifest.columns:
            raise RuntimeError(
                f"training source projection formal consumer flag missing: {column}"
            )
        if _strict_bool(
            row.get(column, ""),
            label=f"training source projection {column}",
        ):
            raise RuntimeError(
                f"training source projection formal consumer flag drift: {column}"
            )
    return {
        "training_source_projection_semantic_sha256": semantic_sha,
        "training_source_projected_episode_row_count": row_count,
        "training_source_manifest_canonical_sha256": _frame_sha(source_manifest),
    }


def _anchor_features(frame: pd.DataFrame, index: int) -> dict[str, object]:
    close = _number(frame.at[index, "analysis_close"])
    prior = frame.iloc[max(0, index - POSITION_LOOKBACK_PRIOR_SESSIONS) : index]
    prior_high = pd.to_numeric(prior["analysis_high"], errors="coerce")
    prior_low = pd.to_numeric(prior["analysis_low"], errors="coerce")
    observed = bool(
        len(prior) == POSITION_LOOKBACK_PRIOR_SESSIONS
        and prior_high.notna().all()
        and prior_low.notna().all()
        and np.isfinite(close)
    )
    high = float(prior_high.max()) if observed else math.nan
    low = float(prior_low.min()) if observed else math.nan
    observed = bool(observed and np.isfinite(high) and np.isfinite(low) and high > low)
    position = (close - low) / (high - low) * 100.0 if observed else math.nan
    position_bucket = (
        "low_pos_le40"
        if observed and position <= POSITION_LOW_MAX_PCT
        else "mid_pos_40_75"
        if observed and position <= POSITION_MID_MAX_PCT
        else "high_pos_gt75"
        if observed
        else "insufficient_history"
    )
    return20 = math.nan
    if index >= SHAPE_RETURN_LOOKBACK_SESSIONS:
        close20 = _number(
            frame.at[index - SHAPE_RETURN_LOOKBACK_SESSIONS, "analysis_close"]
        )
        if np.isfinite(close) and np.isfinite(close20) and close20 > 0:
            return20 = (close / close20 - 1.0) * 100.0
    recent = pd.to_numeric(
        frame.iloc[
            max(0, index - SHAPE_RANGE_WINDOW_SESSIONS + 1) : index + 1
        ]["analysis_close"],
        errors="coerce",
    )
    range23 = (
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
    slope = (
        (ema_now / ema_prior - 1.0) * 100.0
        if np.isfinite(ema_now) and np.isfinite(ema_prior) and ema_prior > 0
        else math.nan
    )
    if not all(np.isfinite(value) for value in (return20, range23, slope)):
        shape = "insufficient_history"
    elif (
        return20 > SHAPE_RISING_RETURN_MIN_PCT
        and slope > SHAPE_RISING_EMA_SLOPE_MIN_PCT
    ):
        shape = "rising"
    elif (
        return20 < SHAPE_FALLING_RETURN_MAX_PCT
        and slope < SHAPE_FALLING_EMA_SLOPE_MAX_PCT
    ):
        shape = "falling"
    elif (
        abs(return20) <= SHAPE_CONSOLIDATION_RETURN_ABS_MAX_PCT
        and range23 <= SHAPE_CONSOLIDATION_RANGE_MAX_PCT
    ):
        shape = "consolidation"
    else:
        shape = "mixed_or_turn"
    return {
        "source_position_120d_pct": round(position, 4) if np.isfinite(position) else "",
        "source_shape_return20_pct": round(return20, 4) if np.isfinite(return20) else "",
        "source_shape_range23_pct": round(range23, 4) if np.isfinite(range23) else "",
        "source_shape_ema23_slope5_pct": round(slope, 4) if np.isfinite(slope) else "",
        "source_position_bucket": position_bucket,
        "source_shape_bucket": shape,
        "source_position_shape_cell_id": (
            f"{position_bucket}__{shape}"
            if position_bucket != "insufficient_history" and shape != "insufficient_history"
            else "insufficient_history"
        ),
    }


def _lineage(episode: pd.Series, frame: pd.DataFrame) -> list[dict[str, object]]:
    names = (
        "qualifying_revenue_periods",
        "qualifying_source_dates",
        "qualifying_cross_market_resolution_ids",
        "qualifying_source_row_canonical_sha256s",
        "qualifying_canonical_source_table_dates",
        "qualifying_trade_dates",
        "qualifying_sequence_indices",
        "qualifying_source_revenue_anomaly_candidate_flags",
    )
    lists = {
        name: [part.strip() for part in str(episode[name]).split("|") if part.strip()]
        for name in names
    }
    count_valid, expected_count = _exact_integer_value(
        episode["qualifying_update_count"]
    )
    if not count_valid or expected_count is None or expected_count <= 0:
        raise RuntimeError("source qualifying update count is not a positive exact integer")
    lengths = {len(values) for values in lists.values()}
    lengths.add(expected_count)
    if len(lengths) != 1 or not lists[names[0]]:
        raise RuntimeError(f"source point-in-time lineage is not aligned: {episode['episode_key']}")
    date_index = {str(date): int(index) for index, date in frame["date"].items()}
    rows: list[dict[str, object]] = []
    for values in zip(*(lists[name] for name in names), strict=True):
        (
            period,
            source_date,
            resolution,
            row_sha,
            table_date,
            trade_date,
            sequence,
            anomaly_flag,
        ) = values
        source_date = _date(source_date)
        table_date = _date(table_date)
        trade_date = _date(trade_date)
        if not source_date or not table_date or not trade_date:
            raise RuntimeError("source point-in-time date lineage is incomplete")
        sequence_valid, sequence_index = _exact_integer_value(sequence)
        if not sequence_valid or sequence_index is None or sequence_index < 0:
            raise RuntimeError("source point-in-time sequence is not an exact integer")
        if not SHA256_PATTERN.fullmatch(str(row_sha).lower()):
            raise RuntimeError("source point-in-time row SHA is invalid")
        first_available = next(
            (str(date) for date in frame["date"] if str(date) >= source_date), ""
        )
        if trade_date not in date_index or date_index[trade_date] != sequence_index:
            raise RuntimeError("source point-in-time sequence/date lineage drift")
        if first_available != trade_date or source_date > trade_date:
            raise RuntimeError("source point-in-time availability uses future information")
        rows.append(
            {
                "period": period,
                "source_date": source_date,
                "resolution": resolution,
                "row_sha": str(row_sha).lower(),
                "table_date": table_date,
                "trade_date": trade_date,
                "sequence_index": sequence_index,
                "source_anomaly_candidate_flag": _strict_bool(
                    anomaly_flag,
                    label=(
                        "source point-in-time anomaly flag/"
                        f"{episode['episode_key']}/{row_sha}"
                    ),
                ),
            }
        )
    if [row["sequence_index"] for row in rows] != sorted(
        {row["sequence_index"] for row in rows}
    ):
        raise RuntimeError("source point-in-time sequence is not strictly increasing")
    if _strict_bool(
        episode["qualifying_source_revenue_anomaly_candidate_flag"],
        label="source episode aggregate anomaly flag",
    ) != any(bool(row["source_anomaly_candidate_flag"]) for row in rows):
        raise RuntimeError("source point-in-time anomaly flag aggregate drift")
    if "start_source_revenue_anomaly_candidate_flag" in episode.index and (
        _strict_bool(
            episode["start_source_revenue_anomaly_candidate_flag"],
            label="source episode-start anomaly flag",
        )
        != bool(rows[0]["source_anomaly_candidate_flag"])
    ):
        raise RuntimeError("source point-in-time episode-start anomaly flag drift")
    return rows


def _operation(frame: pd.DataFrame, trigger: int) -> dict[str, object]:
    confirmation = trigger + 1
    entry = confirmation + 1
    trigger_close = _number(frame.at[trigger, "analysis_close"])
    confirmation_close = _number(frame.at[confirmation, "analysis_close"])
    base = {
        "trigger_index": trigger,
        "trigger_date": str(frame.at[trigger, "date"]),
        "trigger_close": round(trigger_close, 8),
        "confirmation_index": confirmation,
        "confirmation_date": str(frame.at[confirmation, "date"]),
        "confirmation_close": round(confirmation_close, 8),
        "entry_index": entry,
        "entry_price_basis": "analysis_open",
        "planned_exit_index": entry + HOLDING_SESSION_INDEX_OFFSET,
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
    if entry >= len(frame):
        return {
            **base,
            "entry_date": "",
            "entry_price": "",
            "operation_status": "right_censored_before_entry",
            "blocked": len(frame) - 1,
        }
    entry_price = _number(frame.at[entry, "analysis_open"])
    base.update({"entry_date": str(frame.at[entry, "date"]), "entry_price": round(entry_price, 8)})
    exit_index = entry + HOLDING_SESSION_INDEX_OFFSET
    if exit_index >= len(frame):
        return {
            **base,
            "operation_status": f"right_censored_before_d{HOLDING_DAYS}",
            "blocked": len(frame) - 1,
        }
    exit_price = _number(frame.at[exit_index, "analysis_close"])
    realized = (exit_price / entry_price - 1.0) * 100.0
    outcome = "win" if realized > 1e-9 else "failure" if realized < -1e-9 else "neutral"
    return {
        **base,
        "planned_exit_date": str(frame.at[exit_index, "date"]),
        "exit_index": exit_index,
        "exit_date": str(frame.at[exit_index, "date"]),
        "exit_price": round(exit_price, 8),
        "return_valid": True,
        "right_censored": False,
        "realized_return_pct": round(realized, 4),
        "return_outcome": outcome,
        "realized_return_ge20": realized >= 20.0,
        "operation_return_review_candidate_flag": abs(realized) >= OPERATION_RETURN_REVIEW_THRESHOLD_PCT,
        "entry_date": str(frame.at[entry, "date"]),
        "entry_price": round(entry_price, 8),
        "operation_status": "mature_operation",
        "blocked": exit_index,
    }


def _expected_window(
    source: pd.DataFrame,
    prices: Mapping[str, pd.DataFrame],
    *,
    start_date: str,
    end_date: str,
) -> list[dict[str, object]]:
    expected: list[dict[str, object]] = []
    for raw_stock_id, episodes in source.groupby("stock_id", sort=False):
        stock_id = _stock_id(raw_stock_id)
        frame = prices.get(stock_id)
        if frame is None or frame.empty:
            continue
        date_index = {str(date): int(index) for index, date in frame["date"].items()}
        start_matches = frame.index[frame["date"].astype(str).ge(start_date)]
        end_matches = frame.index[frame["date"].astype(str).le(end_date)]
        if not len(start_matches) or not len(end_matches):
            continue
        window_start = int(start_matches[0])
        window_end = int(end_matches[-1])
        triggers: list[int] = []
        for index in range(window_start, window_end + 1):
            ma60 = _number(frame.at[index, "ma60"])
            ma120 = _number(frame.at[index, "ma120"])
            if not (_bool(frame.at[index, "cross_breakout_prev20"]) and np.isfinite(ma60) and np.isfinite(ma120) and ma60 > ma120):
                continue
            if index + 1 >= len(frame):
                continue
            trigger_close = _number(frame.at[index, "analysis_close"])
            confirmation_close = _number(frame.at[index + 1, "analysis_close"])
            if np.isfinite(trigger_close) and np.isfinite(confirmation_close) and confirmation_close > trigger_close:
                triggers.append(index)
        blocked = window_start - 1
        for _, episode in episodes.sort_values(
            ["episode_start_trade_date", "episode_key"], kind="mergesort"
        ).iterrows():
            episode_lineage = _lineage(episode, frame)
            start = max(
                date_index[_date(episode["episode_start_trade_date"])],
                window_start,
                blocked + 1,
            )
            end = min(
                max(row["sequence_index"] for row in episode_lineage) + WATCH_HORIZON_TRADING_DAYS,
                window_end,
            )
            for trigger in triggers:
                if trigger < start or trigger <= blocked:
                    continue
                if trigger > end:
                    break
                trigger_date = str(frame.at[trigger, "date"])
                available = [
                    row
                    for row in episode_lineage
                    if int(row["sequence_index"]) <= trigger
                    and str(row["source_date"]) <= trigger_date
                    and str(row["trade_date"]) <= trigger_date
                    and str(row["table_date"]) <= trigger_date
                ]
                if not available:
                    raise RuntimeError("source as-of point-in-time row is missing at trigger")
                asof = available[-1]
                lag = trigger - int(asof["sequence_index"])
                if lag > WATCH_HORIZON_TRADING_DAYS:
                    continue
                operation = _operation(frame, trigger)
                blocked = max(blocked, int(operation.pop("blocked")))
                features = _anchor_features(frame, int(asof["sequence_index"]))
                position = str(features["source_position_bucket"])
                shape = str(features["source_shape_bucket"])
                low = position == "low_pos_le40" and shape == "falling"
                mid = position == "mid_pos_40_75" and shape == "falling"
                if low or mid:
                    source_candidate = bool(asof["source_anomaly_candidate_flag"])
                    price_candidate = _bool(episode["unresolved_price_path_candidate_flag"])
                    return_candidate = _bool(operation["operation_return_review_candidate_flag"])
                    event_key = "|".join(
                        (
                            LIFECYCLE_POLICY_ID,
                            CONFIRMATION_VARIANT_ID,
                            stock_id,
                            str(episode["episode_key"]),
                            str(operation["trigger_date"]),
                        )
                    )
                    expected.append(
                        {
                                "event_key": event_key,
                                "stock_id": stock_id,
                                "stock_name": str(episode["stock_name"]),
                                "episode_key": str(episode["episode_key"]),
                                "variant_id": PRIMARY_VARIANT_ID if mid else CHALLENGER_VARIANT_IDS[0],
                                "primary_variant_member": mid,
                                "low_falling_member": low,
                                "low_or_mid_falling_union_member": True,
                                "source_asof_date": asof["source_date"],
                                "source_asof_trade_date": asof["trade_date"],
                                "source_asof_revenue_period": asof["period"],
                                "source_asof_row_canonical_sha256": asof["row_sha"],
                                "source_asof_canonical_source_table_date": asof["table_date"],
                                "source_asof_sequence_index": asof["sequence_index"],
                                "source_to_trigger_trading_days": lag,
                                "future_qualifying_update_ignored_count": len(episode_lineage) - len(available),
                                **features,
                                **operation,
                                "anomaly_candidate_flag": source_candidate or price_candidate or return_candidate,
                                "source_anomaly_candidate_flag": source_candidate,
                                "unresolved_price_path_candidate_flag": price_candidate,
                        }
                    )
                if _bool(operation["right_censored"]):
                    break
    return expected


def _membership(detail: pd.DataFrame, variant_id: str) -> pd.Series:
    column = {
        PRIMARY_VARIANT_ID: "primary_variant_member",
        CHALLENGER_VARIANT_IDS[0]: "low_falling_member",
        CHALLENGER_VARIANT_IDS[1]: "low_or_mid_falling_union_member",
    }[variant_id]
    return detail[column].map(_bool)


def _overlap_count(detail: pd.DataFrame) -> int:
    count = 0
    for _, stock in detail.groupby("stock_id", sort=False):
        prior_exit = -1
        for row in stock.sort_values("trigger_index", kind="mergesort").itertuples(index=False):
            entry = int(row.entry_index)
            if prior_exit >= 0 and entry <= prior_exit:
                count += 1
            prior_exit = max(
                prior_exit,
                entry if _bool(row.right_censored) else int(row.exit_index),
            )
    return count


def _metrics(part: pd.DataFrame) -> dict[str, object]:
    mature = part.loc[part["return_valid"].map(_bool)]
    returns = pd.to_numeric(mature["realized_return_pct"], errors="coerce").dropna()
    outcomes = mature["return_outcome"].astype(str)
    count = len(mature)
    return {
        "event_count": len(part),
        "mature_count": count,
        "right_censored_count": int(part["right_censored"].map(_bool).sum()),
        "win_count": int(outcomes.eq("win").sum()),
        "neutral_count": int(outcomes.eq("neutral").sum()),
        "failure_count": int(outcomes.eq("failure").sum()),
        "win_rate_pct": round(float(outcomes.eq("win").mean()) * 100.0, 4) if count else "",
        "average_return_pct": round(float(returns.mean()), 4) if len(returns) else "",
        "median_return_pct": round(float(returns.median()), 4) if len(returns) else "",
        "p10_return_pct": round(float(returns.quantile(0.10)), 4) if len(returns) else "",
        "p90_return_pct": round(float(returns.quantile(0.90)), 4) if len(returns) else "",
        "return_ge20_count": int(returns.ge(20.0).sum()),
        "loss_count": int(returns.lt(0.0).sum()),
        "same_stock_overlap_pair_count": _overlap_count(part),
    }


def _check_metric_row(
    row: pd.Series,
    expected: Mapping[str, object],
    *,
    label: str,
    errors: list[str],
) -> None:
    for column in INTEGER_METRIC_COLUMNS:
        if column not in row.index:
            errors.append(f"{label} missing metric column: {column}")
        elif not _equal_exact_integer(row[column], expected[column]):
            errors.append(f"{label} exact-integer metric drift: {column}")
    for column in CONTINUOUS_METRIC_COLUMNS:
        if column not in row.index:
            errors.append(f"{label} missing metric column: {column}")
        elif not _equal_number(row[column], expected[column]):
            errors.append(f"{label} metric drift: {column}")


def _validate_capture_surfaces(
    frames: Mapping[str, pd.DataFrame],
    *,
    expected_capture_id: str,
    errors: list[str],
) -> None:
    common = {
        "model_id": MODEL_ID,
        "artifact_id": ARTIFACT_ID,
        "artifact_version": ARTIFACT_VERSION,
        "capture_id": expected_capture_id,
        "rule_canonical_sha256": RULE_CANONICAL_SHA256,
        "data_contract_sha256": DATA_CONTRACT_SHA256,
    }
    for label, frame in frames.items():
        missing = sorted({*common, "artifact_row_key"} - set(frame.columns))
        if missing:
            errors.append(f"{label} capture surface missing columns: {missing}")
            continue
        if frame["artifact_row_key"].astype(str).eq("").any():
            errors.append(f"{label} capture surface has blank artifact_row_key")
        if frame["artifact_row_key"].astype(str).duplicated().any():
            errors.append(f"{label} capture surface has duplicate artifact_row_key")
        for column, expected in common.items():
            observed = set(frame[column].astype(str).str.strip())
            if frame.empty:
                continue
            if observed != {str(expected)}:
                errors.append(f"{label} capture-envelope parity drift: {column}")


def _align_exact_history_schema_extension(
    predecessor: pd.DataFrame,
    current_columns: list[str],
    *,
    allowed_extension_columns: tuple[str, ...],
) -> pd.DataFrame | None:
    if list(predecessor.columns) == current_columns:
        return predecessor.copy()
    missing = [column for column in current_columns if column not in predecessor.columns]
    retained = [column for column in current_columns if column in predecessor.columns]
    if (
        tuple(missing) != allowed_extension_columns
        or retained != list(predecessor.columns)
        or any(column not in current_columns for column in predecessor.columns)
    ):
        return None
    aligned = predecessor.copy()
    for column in allowed_extension_columns:
        aligned[column] = ""
    return aligned.loc[:, current_columns]


def validate_history_surfaces(
    current_frames: Mapping[str, pd.DataFrame],
    history_frames: Mapping[str, pd.DataFrame],
    *,
    immutable_base_frames: Mapping[str, pd.DataFrame] | None = None,
) -> list[str]:
    """Validate append-only base prefix, structure, and current-capture parity.

    Historical rows are not replayed because their original input bundles are not
    part of this validator invocation.  Their immutable rows are instead anchored
    to the explicit Git/base frames supplied by the caller.
    """

    errors: list[str] = []
    expected_names = set(current_frames)
    if set(history_frames) != expected_names:
        errors.append(
            "history surface set drift: "
            f"expected={sorted(expected_names)} observed={sorted(history_frames)}"
        )
        return errors
    if immutable_base_frames is not None and set(immutable_base_frames) not in (
        set(),
        expected_names,
    ):
        errors.append(
            "history immutable base surface set drift: "
            f"observed={sorted(immutable_base_frames)}"
        )
        return errors
    manifest = current_frames["manifest"]
    if len(manifest) != 1 or "capture_id" not in manifest.columns:
        return ["history validation requires one current manifest capture"]
    current_capture_id = str(manifest.iloc[0]["capture_id"]).strip()
    for label in sorted(expected_names):
        current = current_frames[label]
        history = history_frames[label]
        extension_columns = APPEND_ONLY_SCHEMA_EXTENSION_COLUMNS_BY_ARTIFACT.get(
            label, ()
        )
        history = _align_exact_history_schema_extension(
            history,
            list(current.columns),
            allowed_extension_columns=extension_columns,
        )
        if history is None:
            errors.append(f"{label} history schema drift")
            continue
        required = {"capture_id", "artifact_row_key"}
        missing = sorted(required - set(history.columns))
        if missing:
            errors.append(f"{label} history missing structural keys: {missing}")
            continue
        if history[list(required)].astype(str).eq("").any().any():
            errors.append(f"{label} history has blank structural key")
        if history.duplicated(["capture_id", "artifact_row_key"]).any():
            errors.append(f"{label} history has duplicate capture/artifact row keys")
            continue
        capture_blocks: set[str] = set()
        previous_capture_id: str | None = None
        non_contiguous_capture = False
        for capture_id in history["capture_id"].astype(str):
            if capture_id == previous_capture_id:
                continue
            if capture_id in capture_blocks:
                non_contiguous_capture = True
                break
            capture_blocks.add(capture_id)
            previous_capture_id = capture_id
        if non_contiguous_capture:
            errors.append(f"{label} history has non-contiguous capture blocks")
            continue
        base = (
            immutable_base_frames.get(label)
            if immutable_base_frames is not None
            else None
        )
        if base is not None:
            base = _align_exact_history_schema_extension(
                base,
                list(history.columns),
                allowed_extension_columns=extension_columns,
            )
            if base is None:
                errors.append(f"{label} history immutable base schema drift")
                continue
            if len(history) < len(base):
                errors.append(f"{label} history deleted immutable base rows")
                continue
            if base.empty and history["capture_id"].astype(str).nunique() > 1:
                errors.append(
                    f"{label} history has prior captures but immutable base is empty"
                )
                continue
            for offset in range(len(base)):
                if _mapping_sha(
                    base.iloc[offset].to_dict(),
                    excluded_columns=(),
                ) != _mapping_sha(
                    history.iloc[offset].to_dict(),
                    excluded_columns=(),
                ):
                    errors.append(
                        f"{label} history immutable base prefix drift at row {offset + 2}"
                    )
                    break
        persisted = history.loc[
            history["capture_id"].astype(str).eq(current_capture_id)
        ].copy()
        current_keys = set(current["artifact_row_key"].astype(str))
        persisted_keys = set(persisted["artifact_row_key"].astype(str))
        if persisted_keys != current_keys:
            errors.append(f"{label} history current-capture row presence drift")
            continue
        if persisted["artifact_row_key"].astype(str).tolist() != current[
            "artifact_row_key"
        ].astype(str).tolist():
            errors.append(f"{label} history current-capture row order drift")
            continue
        if not current.empty:
            terminal = history.tail(len(current))
            if (
                len(terminal) != len(current)
                or not terminal["capture_id"].astype(str).eq(current_capture_id).all()
            ):
                errors.append(
                    f"{label} history current capture is not the contiguous terminal suffix"
                )
                continue
        current_index = current.set_index("artifact_row_key", drop=False)
        persisted_index = persisted.set_index("artifact_row_key", drop=False)
        base_row_count = len(base) if base is not None else 0
        uncommitted_tail = history.iloc[base_row_count:].copy()
        if not uncommitted_tail.empty:
            tail_keys = set(
                zip(
                    uncommitted_tail["capture_id"].astype(str),
                    uncommitted_tail["artifact_row_key"].astype(str),
                    strict=True,
                )
            )
            current_composite_keys = {
                (current_capture_id, str(key)) for key in current_keys
            }
            if tail_keys != current_composite_keys:
                errors.append(
                    f"{label} history has an uncommitted prior capture outside the "
                    "immutable base"
                )
                continue
            tail_composite_order = list(
                zip(
                    uncommitted_tail["capture_id"].astype(str),
                    uncommitted_tail["artifact_row_key"].astype(str),
                    strict=True,
                )
            )
            current_composite_order = [
                (current_capture_id, str(key))
                for key in current["artifact_row_key"].astype(str)
            ]
            if tail_composite_order != current_composite_order:
                errors.append(
                    f"{label} history uncommitted current-capture row order drift"
                )
                continue
            tail_index = uncommitted_tail.set_index("artifact_row_key", drop=False)
            tail_mismatch = False
            for key in sorted(current_keys):
                semantic_exclusions = (
                    "generated_at",
                    *(
                        PRICE_INPUT_PROVENANCE_DIAGNOSTIC_COLUMNS
                        if PRICE_SEMANTIC_PROJECTION_ENABLED
                        else ()
                    ),
                )
                if _mapping_sha(
                    tail_index.loc[key].to_dict(),
                    excluded_columns=semantic_exclusions,
                ) != _mapping_sha(
                    current_index.loc[key].to_dict(),
                    excluded_columns=semantic_exclusions,
                ):
                    errors.append(
                        f"{label} history current-capture semantic parity drift "
                        f"(uncommitted tail): {key}"
                    )
                    tail_mismatch = True
                    break
            if tail_mismatch:
                continue
        for key in sorted(current_keys):
            semantic_exclusions = (
                "generated_at",
                *(
                    PRICE_INPUT_PROVENANCE_DIAGNOSTIC_COLUMNS
                    if PRICE_SEMANTIC_PROJECTION_ENABLED
                    else ()
                ),
            )
            if _mapping_sha(
                current_index.loc[key].to_dict(),
                excluded_columns=semantic_exclusions,
            ) != _mapping_sha(
                persisted_index.loc[key].to_dict(),
                excluded_columns=semantic_exclusions,
            ):
                errors.append(
                    f"{label} history current-capture semantic parity drift: {key}"
                )
    return errors


def validate_frames(
    manifest: pd.DataFrame,
    detail: pd.DataFrame,
    summary: pd.DataFrame,
    comparison: pd.DataFrame,
    anomaly: pd.DataFrame,
    *,
    source_detail: pd.DataFrame,
    daily_by_stock: Mapping[str, pd.DataFrame],
    source_manifest: pd.DataFrame,
    history_frames: Mapping[str, pd.DataFrame] | None = None,
    immutable_history_base_frames: Mapping[str, pd.DataFrame] | None = None,
) -> list[str]:
    """Independently replay the frozen forward-holdout contract."""

    errors: list[str] = []
    frames = {
        "manifest": manifest,
        "detail": detail,
        "summary": summary,
        "comparison": comparison,
        "anomaly": anomaly,
    }
    for label, frame in frames.items():
        if "research_only" not in frame.columns:
            errors.append(f"{label} must remain research-only")
        else:
            for row_index, value in frame["research_only"].items():
                try:
                    research_only = _strict_bool(
                        value,
                        label=f"{label} research_only row={row_index}",
                    )
                except RuntimeError as exc:
                    errors.append(str(exc))
                    continue
                if not research_only:
                    errors.append(f"{label} must remain research-only")
        for column in FALSE_FLAG_COLUMNS:
            if column not in frame.columns:
                errors.append(f"{label} formal consumer flag must remain false: {column}")
                continue
            for row_index, value in frame[column].items():
                try:
                    enabled = _strict_bool(
                        value,
                        label=f"{label} {column} row={row_index}",
                    )
                except RuntimeError as exc:
                    errors.append(str(exc))
                    continue
                if enabled:
                    errors.append(
                        f"{label} formal consumer flag must remain false: {column}"
                    )
    if len(manifest) != 1:
        errors.append("manifest must contain exactly one row")
        return errors
    manifest_row = manifest.iloc[0]
    observed_manifest_date = str(manifest_row.get("observed_through_date", "")).strip()
    expected_holdout_status = (
        "preregistered_waiting_for_start"
        if ALLOW_PRE_START_EMPTY_CAPTURE
        and observed_manifest_date
        and observed_manifest_date < HOLDOUT_START_DATE
        else "holdout_accumulating"
    )
    for column, expected in (
        ("preregistration_pr_number", PREREGISTRATION_PR_NUMBER),
        ("preregistration_merge_commit", PREREGISTRATION_MERGE_COMMIT),
        ("training_cutoff_date", TRAINING_CUTOFF_DATE),
        ("bridge_start_date", BRIDGE_START_DATE),
        ("bridge_end_date", BRIDGE_END_DATE),
        ("holdout_start_date", HOLDOUT_START_DATE),
        ("artifact_row_key", "manifest"),
        ("rule_contract_version", RULE_CONTRACT_VERSION),
        ("rule_canonical_sha256", RULE_CANONICAL_SHA256),
        ("data_contract_version", DATA_CONTRACT_VERSION),
        ("data_contract_sha256", DATA_CONTRACT_SHA256),
        ("holdout_status", expected_holdout_status),
        ("financial_statement_scope", FINANCIAL_STATEMENT_SCOPE),
    ):
        if column not in manifest.columns or str(manifest_row[column]).strip() != expected:
            errors.append(f"manifest preregistration/rule/cutoff drift: {column}")
    for column in ("ranking_consumption_allowed", "pdf_consumption_allowed"):
        if column not in manifest.columns:
            errors.append(f"manifest formal consumer flag must remain false: {column}")
            continue
        try:
            enabled = _strict_bool(
                manifest_row[column],
                label=f"manifest {column}",
            )
        except RuntimeError as exc:
            errors.append(str(exc))
            continue
        if enabled:
            errors.append(f"manifest formal consumer flag must remain false: {column}")
    if "append_only_history" not in manifest.columns:
        errors.append("manifest append_only_history contract is missing")
    else:
        try:
            append_only = _strict_bool(
                manifest_row["append_only_history"],
                label="manifest append_only_history",
            )
        except RuntimeError as exc:
            errors.append(str(exc))
        else:
            if not append_only:
                errors.append("manifest append_only_history must remain true")

    try:
        training_lineage = _training_lineage(source_manifest)
        source = _normalize_source(source_detail)
        _validate_source_anomaly_boolean_contract(source)
        _validate_source_integer_contract(source)
        prices = _normalize_prices(daily_by_stock)
        observed = max(str(frame["date"].iloc[-1]) for frame in prices.values())
        pre_start_capture = observed < HOLDOUT_START_DATE
        if pre_start_capture and not ALLOW_PRE_START_EMPTY_CAPTURE:
            raise RuntimeError(
                f"price observation ends before holdout start: {observed}"
            )
        if set(source["artifact_id"].astype(str)) != {SOURCE_ARTIFACT_ID}:
            raise RuntimeError("source artifact id drift")
        if set(source["artifact_version"].astype(str)) != {SOURCE_ARTIFACT_VERSION}:
            raise RuntimeError("source artifact version drift")
        current_monthly_lineage: dict[str, str] = {}
        for column in MONTHLY_LINEAGE_COLUMNS:
            values = {
                str(value).strip().lower()
                for value in source[column]
                if str(value).strip()
            }
            if len(values) != 1 or not SHA256_PATTERN.fullmatch(next(iter(values), "")):
                raise RuntimeError(
                    f"source monthly-revenue lineage is not one canonical SHA-256: {column}"
                )
            current_monthly_lineage[column] = next(iter(values))
        for column in (
            "qualifying_source_dates",
            "qualifying_canonical_source_table_dates",
            "qualifying_trade_dates",
        ):
            tokens = [
                _date(token)
                for value in source[column]
                for token in str(value).split("|")
                if str(token).strip()
            ]
            if any(not token for token in tokens):
                raise RuntimeError(f"source lineage has an invalid date: {column}")
            if any(token > observed for token in tokens):
                raise RuntimeError(
                    f"source lineage exceeds observation cutoff: {column}"
                )
        expected = (
            []
            if pre_start_capture
            else _expected_window(
                source, prices, start_date=HOLDOUT_START_DATE, end_date=observed
            )
        )
        bridge = _expected_window(
            source,
            prices,
            start_date=BRIDGE_START_DATE,
            end_date=min(BRIDGE_END_DATE, observed),
        ) if observed >= BRIDGE_START_DATE else []
    except Exception as exc:  # validation boundary reports input defects as evidence
        errors.append(f"point-in-time source/price replay failed: {exc}")
        return errors

    source_sha = _frame_sha(source)
    price_sha, price_sha_set, price_stock_count, price_row_count = _price_lineage(prices)
    price_semantic_lineage: dict[str, object] = {}
    if PRICE_SEMANTIC_PROJECTION_ENABLED:
        (
            semantic_price_sha,
            semantic_price_sha_set,
            semantic_price_stock_count,
            semantic_price_row_count,
        ) = _price_semantic_lineage(
            daily_by_stock,
            cutoff_date=observed,
        )
        price_semantic_lineage = {
            "price_semantic_projection_version": (
                PRICE_SEMANTIC_PROJECTION_VERSION
            ),
            "price_semantic_projection_schema_sha256": (
                PRICE_SEMANTIC_PROJECTION_SCHEMA_SHA256
            ),
            "price_semantic_projection_canonical_sha256": semantic_price_sha,
        }
        capture_price_lineage = dict(price_semantic_lineage)
    else:
        semantic_price_sha = ""
        semantic_price_sha_set = ""
        semantic_price_stock_count = 0
        semantic_price_row_count = 0
        capture_price_lineage = {"price_input_canonical_sha256": price_sha}
    capture_envelope = {
        "artifact_version": ARTIFACT_VERSION,
        "rule_canonical_sha256": RULE_CANONICAL_SHA256,
        "data_contract_sha256": DATA_CONTRACT_SHA256,
        "preregistration_merge_commit": PREREGISTRATION_MERGE_COMMIT,
        "observed_through_date": observed,
        "source_detail_canonical_sha256": source_sha,
        **capture_price_lineage,
        **current_monthly_lineage,
        **training_lineage,
    }
    expected_capture_id = _json_sha(capture_envelope)
    manifest_lineage = {
        "capture_id": expected_capture_id,
        "observed_through_date": observed,
        "source_artifact_id": SOURCE_ARTIFACT_ID,
        "source_artifact_version": SOURCE_ARTIFACT_VERSION,
        "source_detail_row_count": len(source),
        "source_detail_canonical_sha256": source_sha,
        "price_input_stock_count": price_stock_count,
        "price_input_row_count": price_row_count,
        **current_monthly_lineage,
        **training_lineage,
    }
    if PRICE_SEMANTIC_PROJECTION_ENABLED:
        manifest_lineage.update(
            {
                "price_input_legacy_lineage_role": (
                    "provenance_diagnostic_only_not_promotion_gate"
                ),
                "price_semantic_projection_version": (
                    PRICE_SEMANTIC_PROJECTION_VERSION
                ),
                "price_semantic_projection_schema_sha256": (
                    PRICE_SEMANTIC_PROJECTION_SCHEMA_SHA256
                ),
                "price_semantic_projection_columns": "|".join(
                    PRICE_SEMANTIC_PROJECTION_COLUMNS
                ),
                "price_semantic_projection_decimal_scale": (
                    PRICE_SEMANTIC_PROJECTION_DECIMAL_SCALE
                ),
                "price_semantic_projection_stock_count": (
                    semantic_price_stock_count
                ),
                "price_semantic_projection_row_count": semantic_price_row_count,
                "price_semantic_projection_stock_canonical_sha256s": (
                    semantic_price_sha_set
                ),
                "price_semantic_projection_canonical_sha256": semantic_price_sha,
                "price_semantic_projection_role": (
                    "composite_promotion_input_lineage_component"
                ),
                "price_semantic_projection_migration_id": (
                    PRICE_SEMANTIC_PROJECTION_MIGRATION_ID
                ),
                "price_semantic_projection_authorization_reference": (
                    PRICE_SEMANTIC_PROJECTION_AUTHORIZATION_REFERENCE
                ),
            }
        )
        legacy_global = str(
            manifest_row.get("price_input_canonical_sha256", "")
        ).strip().lower()
        if not SHA256_PATTERN.fullmatch(legacy_global):
            errors.append("manifest legacy price global diagnostic SHA-256 is invalid")
        legacy_tokens = str(
            manifest_row.get("price_input_stock_canonical_sha256s", "")
        ).split("|")
        legacy_ids: list[str] = []
        for token in legacy_tokens:
            stock_id, separator, digest = token.partition(":")
            if (
                not separator
                or not stock_id.strip()
                or not SHA256_PATTERN.fullmatch(digest.strip().lower())
            ):
                errors.append("manifest legacy price per-stock diagnostics are invalid")
                break
            legacy_ids.append(stock_id.strip())
        if (
            legacy_ids != sorted(prices)
            or len(legacy_ids) != price_stock_count
            or len(set(legacy_ids)) != len(legacy_ids)
        ):
            errors.append("manifest legacy price per-stock diagnostic identity drift")
    else:
        manifest_lineage.update(
            {
                "price_input_stock_canonical_sha256s": price_sha_set,
                "price_input_canonical_sha256": price_sha,
            }
        )
    for column, expected_value in manifest_lineage.items():
        if _canonical_value(manifest_row.get(column, "")) != _canonical_value(
            expected_value
        ):
            errors.append(f"manifest capture-envelope lineage drift: {column}")
    _validate_capture_surfaces(
        frames,
        expected_capture_id=expected_capture_id,
        errors=errors,
    )
    _validate_strict_boolean_columns(
        detail,
        DETAIL_BUSINESS_BOOLEAN_COLUMNS,
        label="detail",
        errors=errors,
    )
    detail_lineage = {
        "preregistration_merge_commit": PREREGISTRATION_MERGE_COMMIT,
        "rule_contract_version": RULE_CONTRACT_VERSION,
        "data_contract_version": DATA_CONTRACT_VERSION,
        "source_artifact_id": SOURCE_ARTIFACT_ID,
        "source_artifact_version": SOURCE_ARTIFACT_VERSION,
        "source_detail_canonical_sha256": source_sha,
        **current_monthly_lineage,
        **training_lineage,
    }
    if PRICE_SEMANTIC_PROJECTION_ENABLED:
        detail_lineage.update(price_semantic_lineage)
        if "price_input_canonical_sha256" not in detail.columns:
            errors.append("detail legacy price diagnostic column is missing")
        elif not detail.empty and not detail[
            "price_input_canonical_sha256"
        ].astype(str).str.strip().str.lower().map(
            lambda value: bool(SHA256_PATTERN.fullmatch(value))
        ).all():
            errors.append("detail legacy price diagnostic SHA-256 is invalid")
    else:
        detail_lineage["price_input_canonical_sha256"] = price_sha
    for column, expected_value in detail_lineage.items():
        if column not in detail.columns:
            errors.append(f"detail capture-envelope lineage missing: {column}")
            continue
        if detail.empty:
            continue
        observed_values = {
            _canonical_value(value) for value in detail[column]
        }
        if observed_values != {_canonical_value(expected_value)}:
            errors.append(f"detail capture-envelope lineage drift: {column}")

    if detail["event_key"].astype(str).duplicated().any():
        errors.append("detail has duplicate event keys")
    if detail["trigger_date"].astype(str).lt(HOLDOUT_START_DATE).any():
        errors.append("bridge period leaked before holdout start")
    expected_by_key = {str(row["event_key"]): row for row in expected}
    actual_keys = set(detail["event_key"].astype(str))
    if actual_keys != set(expected_by_key):
        errors.append("holdout event completeness/bridge/as-of replay drift")
    row_columns = (
        "stock_id",
        "stock_name",
        "episode_key",
        "variant_id",
        "source_asof_date",
        "source_asof_trade_date",
        "source_asof_revenue_period",
        "source_asof_row_canonical_sha256",
        "source_asof_canonical_source_table_date",
        "source_position_bucket",
        "source_shape_bucket",
        "source_position_shape_cell_id",
        "trigger_date",
        "confirmation_date",
        "entry_date",
        "planned_exit_date",
        "exit_date",
        "operation_status",
        "return_outcome",
    )
    exact_integer_columns = (
        "source_asof_sequence_index",
        "source_to_trigger_trading_days",
        "future_qualifying_update_ignored_count",
        "trigger_index",
        "confirmation_index",
        "entry_index",
        "planned_exit_index",
        "exit_index",
    )
    continuous_numeric_columns = (
        "source_position_120d_pct",
        "source_shape_return20_pct",
        "source_shape_range23_pct",
        "source_shape_ema23_slope5_pct",
        "trigger_close",
        "confirmation_close",
        "entry_price",
        "exit_price",
        "realized_return_pct",
    )
    bool_columns = (
        "primary_variant_member",
        "low_falling_member",
        "low_or_mid_falling_union_member",
        "return_valid",
        "right_censored",
        "realized_return_ge20",
        "operation_return_review_candidate_flag",
        "anomaly_candidate_flag",
        "source_anomaly_candidate_flag",
        "unresolved_price_path_candidate_flag",
    )
    for _, row in detail.iterrows():
        key = str(row.get("event_key", ""))
        expected_row = expected_by_key.get(key)
        if expected_row is None:
            continue
        if str(row.get("artifact_row_key", "")) != key:
            errors.append(f"detail artifact/event key drift: {key}")
        for column in row_columns:
            if str(row.get(column, "")) != str(expected_row.get(column, "")):
                errors.append(f"detail point-in-time/timing drift: {key}/{column}")
        for column in exact_integer_columns:
            if not _equal_exact_integer(
                row.get(column, ""), expected_row.get(column, "")
            ):
                errors.append(
                    f"detail exact-integer timing replay drift: {key}/{column}"
                )
        for column in continuous_numeric_columns:
            if not _equal_number(row.get(column, ""), expected_row.get(column, "")):
                errors.append(f"detail D+2/D+30 numeric replay drift: {key}/{column}")
        for column in bool_columns:
            if _bool(row.get(column, "")) != _bool(expected_row.get(column, "")):
                errors.append(f"detail anomaly/censor/member drift: {key}/{column}")
        if str(row.get("confirmation_variant_id", "")) != CONFIRMATION_VARIANT_ID:
            errors.append(f"detail confirmation contract drift: {key}")
        if str(row.get("candidate_variant_id", "")) != str(
            expected_row.get("variant_id", "")
        ):
            errors.append(f"detail candidate variant contract drift: {key}")
        if str(row.get("lifecycle_policy_id", "")) != LIFECYCLE_POLICY_ID:
            errors.append(f"detail lifecycle policy drift: {key}")
        if not _equal_exact_integer(row.get("holding_days", ""), HOLDING_DAYS):
            errors.append(f"detail holding days must remain {HOLDING_DAYS}: {key}")
        if str(row.get("entry_price_basis", "")) != "analysis_open":
            errors.append(f"detail D+2 entry basis drift: {key}")
        if str(row.get("exit_price_basis", "")) != "analysis_close":
            errors.append(f"detail D+30 exit basis drift: {key}")
        if not _equal_exact_integer(
            row.get("holding_session_index_offset", ""), HOLDING_SESSION_INDEX_OFFSET
        ):
            errors.append(f"detail D+30 holding offset must remain 29: {key}")
        if str(row.get("stop_policy_id", "")) != STOP_POLICY_ID:
            errors.append(f"detail stop policy drift: {key}")
        if str(row.get("exit_reason", "")) != EXIT_RULE_ID:
            errors.append(f"detail D+30 exit reason drift: {key}")
        if str(row.get("financial_statement_scope", "")) != FINANCIAL_STATEMENT_SCOPE:
            errors.append(f"detail financial statement isolation drift: {key}")
        trigger_date = str(row.get("trigger_date", ""))
        for column in (
            "source_asof_date",
            "source_asof_trade_date",
            "source_asof_canonical_source_table_date",
        ):
            if str(row.get(column, "")) > trigger_date:
                errors.append(f"detail future source as-of leakage: {key}/{column}")
        if _number(row.get("source_asof_sequence_index", "")) > _number(
            row.get("trigger_index", "")
        ):
            errors.append(f"detail future source sequence leakage: {key}")
        if not _bool(row.get("primary_metric_included", False)):
            errors.append(f"detail anomaly candidate must remain in primary metric: {key}")
        if not _bool(row.get("same_stock_non_overlap_applied", False)):
            errors.append(f"detail same-stock non-overlap contract drift: {key}")
        expected_sensitivity = not _bool(row.get("anomaly_candidate_flag", False))
        if _bool(row.get("sensitivity_metric_included", False)) != expected_sensitivity:
            errors.append(f"detail anomaly sensitivity inclusion drift: {key}")
        if _bool(row.get("right_censored", False)) and (
            _bool(row.get("return_valid", False))
            or np.isfinite(_number(row.get("realized_return_pct", "")))
            or str(row.get("return_outcome", "")).strip()
        ):
            errors.append(f"right-censored row entered mature metrics: {key}")
        if "event_row_canonical_sha256" in row.index:
            mapping = row.drop(labels=["event_row_canonical_sha256"]).to_dict()
            event_hash_exclusions = ("generated_at",)
            if PRICE_SEMANTIC_PROJECTION_ENABLED:
                event_hash_exclusions = (
                    *event_hash_exclusions,
                    *PRICE_INPUT_PROVENANCE_DIAGNOSTIC_COLUMNS,
                )
            if str(row["event_row_canonical_sha256"]).strip() != _mapping_sha(
                mapping,
                excluded_columns=event_hash_exclusions,
            ):
                errors.append(f"detail event row canonical SHA drift: {key}")

    overlap = _overlap_count(detail)
    if overlap:
        errors.append(f"same-stock overlap/rearm prior exit violation: {overlap}")

    if not _equal_exact_integer(
        manifest_row.get("bridge_excluded_signal_count", ""), len(bridge)
    ):
        errors.append("manifest bridge exclusion count drift")
    if not _equal_exact_integer(
        manifest_row.get("holdout_event_count", ""), len(detail)
    ):
        errors.append("manifest holdout event count drift")
    mature_total = int(detail["return_valid"].map(_bool).sum())
    if not _equal_exact_integer(
        manifest_row.get("mature_event_count", ""), mature_total
    ):
        errors.append("manifest mature/right-censored count drift")
    right_censored_total = int(detail["right_censored"].map(_bool).sum())
    if not _equal_exact_integer(
        manifest_row.get("right_censored_event_count", ""),
        right_censored_total,
    ):
        errors.append("manifest right-censored event count drift")
    primary_metrics = _metrics(detail.loc[_membership(detail, PRIMARY_VARIANT_ID)])
    if not _equal_exact_integer(
        manifest_row.get("primary_mature_count", ""),
        primary_metrics["mature_count"],
    ):
        errors.append("manifest primary mature count drift")
    if not _equal_exact_integer(
        manifest_row.get("primary_right_censored_count", ""),
        primary_metrics["right_censored_count"],
    ):
        errors.append("manifest primary right-censored count drift")

    for surface_label, frame in (("summary", summary), ("comparison", comparison)):
        if len(frame) != len(ALL_VARIANT_IDS):
            errors.append(f"{surface_label} row multiplicity drift")
            continue
        if frame["variant_id"].astype(str).duplicated().any():
            errors.append(f"{surface_label} duplicate variant business key")
            continue
        if set(frame["variant_id"].astype(str)) != set(ALL_VARIANT_IDS):
            errors.append(f"{surface_label} primary/challenger variant set drift")
            continue
        if not frame.apply(
            lambda row: str(row.get("artifact_row_key", ""))
            == str(row.get("variant_id", "")),
            axis=1,
        ).all():
            errors.append(f"{surface_label} artifact/business key drift")
            continue
        for variant_id in ALL_VARIANT_IDS:
            part = detail.loc[_membership(detail, variant_id)]
            expected_metrics = _metrics(part)
            row = frame.loc[frame["variant_id"].astype(str).eq(variant_id)].iloc[0]
            expected_order = ALL_VARIANT_IDS.index(variant_id) + 1
            expected_role = "primary" if variant_id == PRIMARY_VARIANT_ID else "challenger"
            if not _equal_exact_integer(
                row.get("variant_order", ""), expected_order
            ):
                errors.append(f"{surface_label} variant order drift: {variant_id}")
            if str(row.get("variant_role", "")) != expected_role:
                errors.append(f"{surface_label} variant role drift: {variant_id}")
            _check_metric_row(
                row,
                expected_metrics,
                label=f"{surface_label}/{variant_id}",
                errors=errors,
            )
            if str(row.get("holdout_status", "")) != expected_holdout_status:
                errors.append(f"{surface_label} holdout status drift: {variant_id}")
            if surface_label == "summary":
                if not _equal_exact_integer(
                    row.get("bridge_excluded_signal_count", ""), len(bridge)
                ):
                    errors.append(f"summary bridge exclusion count drift: {variant_id}")
                expected_anomaly_count = int(
                    part["anomaly_candidate_flag"].map(_bool).sum()
                )
                if not _equal_exact_integer(
                    row.get("anomaly_candidate_count", ""), expected_anomaly_count
                ):
                    errors.append(f"summary anomaly candidate count drift: {variant_id}")
                if str(row.get("financial_statement_scope", "")) != (
                    FINANCIAL_STATEMENT_SCOPE
                ):
                    errors.append(
                        f"summary financial statement isolation drift: {variant_id}"
                    )
            elif str(row.get("comparison_conclusion", "")) != (
                f"no_promotion_conclusion_{expected_holdout_status}"
            ):
                errors.append(f"comparison conclusion drift: {variant_id}")

    expected_anomaly_keys = {
        (variant_id, basis)
        for variant_id in ALL_VARIANT_IDS
        for basis in (
            "primary_candidate_retaining",
            "excluding_unresolved_anomaly_candidates_sensitivity",
        )
    }
    actual_anomaly_keys = set(
        zip(anomaly["variant_id"].astype(str), anomaly["analysis_basis"].astype(str))
    )
    anomaly_business_keys = list(
        zip(anomaly["variant_id"].astype(str), anomaly["analysis_basis"].astype(str))
    )
    if len(anomaly) != len(expected_anomaly_keys):
        errors.append("anomaly row multiplicity drift")
    elif len(set(anomaly_business_keys)) != len(anomaly_business_keys):
        errors.append("anomaly duplicate variant/analysis business key")
    elif actual_anomaly_keys != expected_anomaly_keys:
        errors.append("anomaly primary/sensitivity surface key drift")
    elif not anomaly.apply(
        lambda row: str(row.get("artifact_row_key", ""))
        == f"{row.get('variant_id', '')}|{row.get('analysis_basis', '')}",
        axis=1,
    ).all():
        errors.append("anomaly artifact/business key drift")
    else:
        for variant_id, basis in sorted(expected_anomaly_keys):
            part = detail.loc[_membership(detail, variant_id)]
            candidates = part["anomaly_candidate_flag"].map(_bool)
            basis_part = part if basis == "primary_candidate_retaining" else part.loc[~candidates]
            row = anomaly.loc[
                anomaly["variant_id"].astype(str).eq(variant_id)
                & anomaly["analysis_basis"].astype(str).eq(basis)
            ].iloc[0]
            expected_variant_order = ALL_VARIANT_IDS.index(variant_id) + 1
            expected_basis_order = (
                1 if basis == "primary_candidate_retaining" else 2
            )
            if not _equal_exact_integer(
                row.get("variant_order", ""), expected_variant_order
            ):
                errors.append(f"anomaly variant order drift: {variant_id}/{basis}")
            if not _equal_exact_integer(
                row.get("basis_order", ""), expected_basis_order
            ):
                errors.append(f"anomaly basis order drift: {variant_id}/{basis}")
            if str(row.get("anomaly_policy", "")) != ANOMALY_POLICY:
                errors.append(f"anomaly policy drift: {variant_id}/{basis}")
            _check_metric_row(
                row,
                _metrics(basis_part),
                label=f"anomaly/{variant_id}/{basis}",
                errors=errors,
            )
            expected_excluded = 0 if basis == "primary_candidate_retaining" else int(candidates.sum())
            if not _equal_exact_integer(
                row.get("excluded_anomaly_candidate_count", ""), expected_excluded
            ):
                errors.append(f"anomaly primary retention/sensitivity drift: {variant_id}/{basis}")
    if history_frames is not None:
        errors.extend(
            validate_history_surfaces(
                frames,
                history_frames,
                immutable_base_frames=immutable_history_base_frames,
            )
        )
    return errors


def load_history_base_frames_from_git(
    base_ref: str,
    *,
    root: Path = ROOT,
    history_paths: Mapping[str, Path] | None = None,
) -> dict[str, pd.DataFrame]:
    """Load immutable history prefixes directly from an explicit Git commit."""

    if not base_ref.strip():
        raise RuntimeError("forward holdout history base ref is blank")
    paths = history_paths or {
        name: DEFAULT_PATHS[f"{name}_history"]
        for name in ("manifest", "detail", "summary", "comparison", "anomaly")
    }
    frames: dict[str, pd.DataFrame] = {}
    for name, path in paths.items():
        try:
            relative = path.resolve().relative_to(root.resolve()).as_posix()
        except ValueError as exc:
            raise RuntimeError(
                f"forward holdout history path is outside repository root: {path}"
            ) from exc
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
                f"cannot read forward holdout history base {base_ref}:{relative}: {exc}"
            ) from exc
        if result.returncode == 0:
            frames[name] = pd.read_csv(
                io.BytesIO(result.stdout),
                dtype={"stock_id": str, "capture_id": str, "artifact_row_key": str},
                keep_default_na=False,
                low_memory=False,
            )
            continue
        missing_markers = (
            b"does not exist in",
            b"exists on disk, but not in",
            b"Path '",
        )
        if any(marker in result.stderr for marker in missing_markers):
            continue
        detail = result.stderr.decode("utf-8", errors="replace").strip()
        raise RuntimeError(
            f"cannot resolve forward holdout history base {base_ref}:{relative}"
            + (f": {detail}" if detail else "")
        )
    if set(frames) not in (set(), set(paths)):
        raise RuntimeError(
            "forward holdout immutable history Git base must contain either zero "
            "or all five surfaces"
        )
    return frames


def _read_csv(path: Path) -> pd.DataFrame:
    return pd.read_csv(
        path,
        dtype={"stock_id": str, "trigger_date": str, "entry_date": str, "exit_date": str},
        keep_default_na=False,
        low_memory=False,
    )


def _load_explicit_price_inputs(directory: Path) -> dict[str, pd.DataFrame]:
    if not directory.is_dir():
        raise RuntimeError(f"explicit price input directory is missing: {directory}")
    output: dict[str, pd.DataFrame] = {}
    for path in sorted(directory.glob("*.csv")):
        # Price bundles contain sparse numeric columns.  The general artifact
        # reader intentionally preserves empty text, but doing that here makes
        # pandas infer an entire sparse numeric column as object/string.  Its
        # lexical decimal then hashes differently from the producer's float
        # canonical form even when the numeric value is unchanged.  Restore
        # only the explicit empty token as missing and request round-trip float
        # parsing so persisted price inputs reproduce the in-memory lineage.
        frame = pd.read_csv(
            path,
            dtype={
                "stock_id": str,
                "trigger_date": str,
                "entry_date": str,
                "exit_date": str,
            },
            keep_default_na=False,
            na_values=[""],
            float_precision="round_trip",
            low_memory=False,
        )
        if "stock_id" in frame.columns:
            if frame["stock_id"].isna().any():
                raise RuntimeError(
                    f"explicit price input stock identity is invalid: {path}"
                )
            stock_ids = sorted({_stock_id(value) for value in frame["stock_id"]})
            if len(stock_ids) != 1:
                raise RuntimeError(
                    f"explicit price input must contain one stock identity: {path}"
                )
            stock_id = stock_ids[0]
        else:
            stock_id = _stock_id(path.stem)
        if not stock_id or stock_id in output:
            raise RuntimeError(f"explicit price input stock identity is invalid: {path}")
        output[stock_id] = frame
    if not output:
        raise RuntimeError("explicit price input directory contains no CSV inputs")
    return output


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Validate the independent revenue forward holdout replay"
    )
    for name, path in DEFAULT_PATHS.items():
        if name in {"manifest", "source_manifest"}:
            continue
        parser.add_argument(f"--{name.replace('_', '-')}", type=Path, default=path)
    parser.add_argument(
        "--manifest",
        type=Path,
        required=True,
        help="Explicit persisted forward-holdout manifest for this capture",
    )
    parser.add_argument(
        "--source-manifest",
        type=Path,
        required=True,
        help="Explicit immutable PR #462 source-projection manifest",
    )
    parser.add_argument(
        "--source-detail",
        type=Path,
        required=True,
        help="Explicit source-detail evidence used by the capture",
    )
    parser.add_argument(
        "--price-input-directory",
        type=Path,
        required=True,
        help="Directory containing one explicit normalized price CSV per stock",
    )
    parser.add_argument(
        "--history-base-ref",
        required=True,
        help="Explicit immutable Git base commit/ref for append-only history prefixes",
    )
    args = parser.parse_args(argv)
    source = _read_csv(args.source_detail)
    daily = _load_explicit_price_inputs(args.price_input_directory)
    history_paths = {
        name: getattr(args, f"{name}_history")
        for name in ("manifest", "detail", "summary", "comparison", "anomaly")
    }
    immutable_history_base_frames = load_history_base_frames_from_git(
        args.history_base_ref,
        history_paths=history_paths,
    )
    errors = validate_frames(
        _read_csv(args.manifest),
        _read_csv(args.detail),
        _read_csv(args.summary),
        _read_csv(args.comparison),
        _read_csv(args.anomaly),
        source_detail=source,
        daily_by_stock=daily,
        source_manifest=_read_csv(args.source_manifest),
        history_frames={
            name: _read_csv(path) for name, path in history_paths.items()
        },
        immutable_history_base_frames=immutable_history_base_frames,
    )
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1
    print("PASS: revenue_unreacted_range forward holdout independently validated")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
