from __future__ import annotations

from datetime import datetime
from decimal import Decimal, InvalidOperation
import hashlib
import json
import math
import numbers
from pathlib import Path
import re
from typing import Mapping
from zoneinfo import ZoneInfo

import numpy as np
import pandas as pd

import revenue_unreacted_range_rearmed_operation_grid as rearmed_producer
import revenue_unreacted_range_source_first_condition_audit as source_first_producer
import revenue_unreacted_range_source_snapshot_projection as source_projection
import revenue_unreacted_range_position_shape_transition_matrix as position_shape_producer
from revenue_unreacted_range_position_shape_transition_matrix import (
    _anchor_features,
    _normalize_price_frame,
)


ROOT = Path(__file__).resolve().parents[1]
MODEL_ID = "revenue_unreacted_range"
ARTIFACT_ID = "revenue_unreacted_range_low_mid_falling_candidate_audit"
V1_ARTIFACT_VERSION = "low_mid_falling_candidate_v1_20260720"
V2_ARTIFACT_VERSION = "low_mid_falling_candidate_v2_20260822"
V3_ARTIFACT_VERSION = "low_mid_falling_candidate_v3_20260829"
ARTIFACT_VERSION = V1_ARTIFACT_VERSION
SOURCE_FIRST_ARTIFACT_ID = "revenue_unreacted_range_source_first_condition_audit"
SOURCE_FIRST_ARTIFACT_VERSION = "source_first_condition_v3_20260720"
REARMED_ARTIFACT_ID = "revenue_unreacted_range_rearmed_operation_grid"
REARMED_ARTIFACT_VERSION = rearmed_producer.ARTIFACT_VERSION
V2_REARMED_ARTIFACT_VERSION = rearmed_producer.V2_ARTIFACT_VERSION
V3_REARMED_ARTIFACT_VERSION = rearmed_producer.V3_ARTIFACT_VERSION
REARMED_SOURCE_ARTIFACT_ID = "revenue_unreacted_range_source_first_condition_audit"
REARMED_SOURCE_VARIANT_ID = "absolute_or_two_month_yoy_ge15"
SOURCE_VARIANT_ID = "absolute_or_two_month_yoy_ge15"
NO_STOP_POLICY_ID = "none_no_stop_reference"
POSITION_SHAPE_ARTIFACT_ID = (
    "revenue_unreacted_range_position_shape_transition_matrix"
)
POSITION_SHAPE_ARTIFACT_VERSION = position_shape_producer.ARTIFACT_VERSION
V2_POSITION_SHAPE_ARTIFACT_VERSION = position_shape_producer.V2_ARTIFACT_VERSION
V3_POSITION_SHAPE_ARTIFACT_VERSION = position_shape_producer.V3_ARTIFACT_VERSION
PRICE_HISTORY_CUTOFF_DATE = "20260713"
SOURCE_PROJECTION_ARTIFACT_ID = "revenue_unreacted_range_source_snapshot_projection"
SOURCE_PROJECTION_ARTIFACT_VERSION = source_projection.V1_PROJECTION_VERSION
V2_SOURCE_PROJECTION_ARTIFACT_VERSION = source_projection.V2_PROJECTION_VERSION
SOURCE_PROJECTION_CUTOFF_DATE = "20260713"


def versions_for_rearmed_artifact(
    source_artifact_version: object,
) -> tuple[str, str, str]:
    version = str(source_artifact_version).strip()
    mapping = {
        REARMED_ARTIFACT_VERSION: (
            V1_ARTIFACT_VERSION,
            POSITION_SHAPE_ARTIFACT_VERSION,
            SOURCE_PROJECTION_ARTIFACT_VERSION,
        ),
        V2_REARMED_ARTIFACT_VERSION: (
            V2_ARTIFACT_VERSION,
            V2_POSITION_SHAPE_ARTIFACT_VERSION,
            V2_SOURCE_PROJECTION_ARTIFACT_VERSION,
        ),
        V3_REARMED_ARTIFACT_VERSION: (
            V3_ARTIFACT_VERSION,
            V3_POSITION_SHAPE_ARTIFACT_VERSION,
            V2_SOURCE_PROJECTION_ARTIFACT_VERSION,
        ),
    }
    if version not in mapping:
        raise RuntimeError(
            f"unsupported rearmed artifact version: {version or '<empty>'}"
        )
    return mapping[version]
POSITION_POLICY = (
    "anchor adjusted close positioned within the adjusted analysis-high/analysis-low range "
    "of exactly 120 prior trading sessions, excluding the anchor"
)
SHAPE_POLICY = (
    "revenue-model-owned descriptive shape: adjusted close return from t-20 to anchor; "
    "adjusted-close range across the 23 sessions ending at anchor; EMA23 through anchor "
    "with five-session slope"
)
WATCH_HORIZON_TRADING_DAYS = 60
HOLDING_DAYS = 30
DATA_CONTRACT_SHA256 = (
    "4aff77863a07ba5fe7c574731ea84ac778b85daffbbfe7123d38cccd4cc61432"
)
CANONICAL_LINEAGE_VERSION = "canonical_json_numeric_text_v1"
MONTHLY_REVENUE_RUN_LINEAGE_COLUMNS = (
    "monthly_revenue_history_blob_sha256",
    "monthly_revenue_canonical_table_sha256",
    "cross_market_resolution_registry_canonical_sha256",
)
PRICE_HISTORY_CANONICAL_COLUMNS = (
    "date",
    "analysis_open",
    "analysis_high",
    "analysis_low",
    "analysis_close",
)
REARMED_ENTRY_PRICE_BASIS = "analysis_open"
REARMED_FIXED_EXIT_PRICE_BASIS = "analysis_close"
REARMED_EXIT_PRICE_BASIS = "fixed_future_close"
REARMED_EXIT_REASON = "fixed_d30_close"
REARMED_PERSISTED_DETAIL_DROP_COLUMNS = (
    "base_confirmation_rule",
    "bonus_timing_role",
    "stop_rule",
    "episode_status",
    "source_launch_date",
    "same_stock_non_overlap_policy",
    "outcome_definition",
    "operation_return_review_policy",
    "financial_statement_scope",
    "promotion_readiness",
    "lifecycle_role",
)
HOLDING_SESSION_INDEX_OFFSET = HOLDING_DAYS - 1
HOLDING_SESSION_CONTRACT = "inclusive_entry_session_count_30_exit_offset_29"

PRIMARY_ANALYSIS_BASIS = "primary_candidate_retaining"
SENSITIVITY_ANALYSIS_BASIS = (
    "excluding_unresolved_anomaly_candidates_sensitivity"
)
ANALYSIS_BASES = (PRIMARY_ANALYSIS_BASIS, SENSITIVITY_ANALYSIS_BASIS)

LIFECYCLE_POLICY_IDS = (
    "rearm_after_realized_exit_next_trade_day",
    "episode_first_match_once",
)
CONFIRMATION_VARIANT_IDS = (
    "base_close_confirmed",
    "delayed_next_close_continuation_bonus",
)
VARIANT_SPECS = (
    (10, "source_mid_falling", "mid_falling_member"),
    (20, "source_low_falling", "low_falling_member"),
    (30, "source_low_or_mid_falling_union", "low_or_mid_falling_union_member"),
)

FINANCIAL_STATEMENT_SCOPE = (
    "monthly_revenue_only;EPS_gross_margin_operating_margin_operating_income_"
    "non_operating_income_net_income_excluded"
)
ANOMALY_POLICY = (
    "primary retains unresolved source price-path and operation-return review candidates; "
    "candidate exclusion is sensitivity only"
)
SAMPLE_POLICY = "sample_count_disclosed_not_used_as_automatic_rejection"
NON_OVERLAP_POLICY = (
    "same-stock entry must be after the prior realized exit within each lifecycle and "
    "confirmation variant"
)

DEFAULT_OUTPUT_RELATIVE_PATHS = {
    "summary_latest": f"output/latest/research_backtest/{ARTIFACT_ID}_latest.csv",
    "detail_latest": f"output/latest/research_backtest/{ARTIFACT_ID}_detail_latest.csv",
    "paired_latest": (
        f"output/latest/research_backtest/{ARTIFACT_ID}_paired_confirmation_latest.csv"
    ),
    "contrast_latest": (
        f"output/latest/research_backtest/{ARTIFACT_ID}_feature_contrast_latest.csv"
    ),
    "markdown_latest": f"output/latest/research_backtest/{ARTIFACT_ID}_latest.md",
    "summary_history": f"output/history/research/{ARTIFACT_ID}.csv",
    "detail_history": f"output/history/research/{ARTIFACT_ID}_detail.csv",
    "paired_history": (
        f"output/history/research/{ARTIFACT_ID}_paired_confirmation.csv"
    ),
    "contrast_history": (
        f"output/history/research/{ARTIFACT_ID}_feature_contrast.csv"
    ),
    "summary_docs": f"docs/latest/{ARTIFACT_ID}_latest.csv",
    "detail_docs": f"docs/latest/{ARTIFACT_ID}_detail_latest.csv",
    "paired_docs": f"docs/latest/{ARTIFACT_ID}_paired_confirmation_latest.csv",
    "contrast_docs": f"docs/latest/{ARTIFACT_ID}_feature_contrast_latest.csv",
    "markdown_docs": f"docs/latest/{ARTIFACT_ID}_latest.md",
}

FEATURE_SPECS = (
    (10, "source_position_120d_pct"),
    (20, "source_shape_return20_pct"),
    (30, "source_shape_range23_pct"),
    (40, "source_shape_ema23_slope5_pct"),
    (50, "latest_source_to_trigger_trading_days"),
)


def _now_text() -> str:
    return datetime.now(ZoneInfo("Asia/Taipei")).strftime(
        "%Y-%m-%d %H:%M:%S Asia/Taipei"
    )


def _stock_id(value: object) -> str:
    text = str(value or "").strip()
    return text[:-2] if text.endswith(".0") and text[:-2].isdigit() else text


def _date_text(value: object) -> str:
    text = "".join(character for character in str(value or "") if character.isdigit())
    return text[:8] if len(text) >= 8 else ""


def _bool_value(value: object) -> bool:
    return str(value).strip().lower() in {"true", "1", "yes"}


def _boolish(series: pd.Series) -> pd.Series:
    return series.astype(str).str.strip().str.lower().isin({"true", "1", "yes"})


def _number(value: object) -> float:
    number = pd.to_numeric(value, errors="coerce")
    return float(number) if pd.notna(number) else math.nan


def _stable(value: object, digits: int = 4) -> float | str:
    number = _number(value)
    return round(number, digits) if np.isfinite(number) else ""


def _rate(numerator: int, denominator: int) -> float | str:
    return round(numerator / denominator * 100.0, 4) if denominator else ""


def _metric(values: pd.Series, method: str) -> float | str:
    numeric = pd.to_numeric(values, errors="coerce").dropna()
    if numeric.empty:
        return ""
    if method == "mean":
        value = numeric.mean()
    elif method == "median":
        value = numeric.median()
    elif method == "p10":
        value = numeric.quantile(0.10)
    elif method == "p90":
        value = numeric.quantile(0.90)
    elif method == "min":
        value = numeric.min()
    elif method == "max":
        value = numeric.max()
    else:
        raise ValueError(f"unsupported metric method: {method}")
    return round(float(value), 4)


def _top_abs_share(values: pd.Series, count: int) -> float | str:
    numeric = pd.to_numeric(values, errors="coerce").dropna().abs()
    denominator = float(numeric.sum())
    if numeric.empty or denominator <= 0:
        return ""
    return round(float(numeric.nlargest(count).sum()) / denominator * 100.0, 4)


def _split(value: object) -> list[str]:
    return [part.strip() for part in str(value).split("|") if part.strip()]


def _canonical_numeric_text(text: str) -> str | None:
    candidate = text.strip()
    if not re.fullmatch(
        r"[+-]?(?:(?:\d+(?:\.\d*)?)|(?:\.\d+))(?:[eE][+-]?\d+)?",
        candidate,
    ):
        return None
    unsigned = candidate.lstrip("+-")
    mantissa = re.split(r"[eE]", unsigned, maxsplit=1)[0]
    integer_part = mantissa.split(".", maxsplit=1)[0]
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


def _canonical_value(value: object) -> str:
    if value is None or (not isinstance(value, (str, bytes)) and pd.isna(value)):
        return ""
    if isinstance(value, (bool, np.bool_)):
        return "true" if bool(value) else "false"
    if isinstance(value, (numbers.Integral, numbers.Real, Decimal)):
        number = float(value)
        if not np.isfinite(number):
            return ""
        numeric = _canonical_numeric_text(str(value))
        if numeric is None:
            raise RuntimeError(f"canonical numeric value is invalid: {value!r}")
        return numeric
    text = str(value).strip()
    if text.lower() in {"true", "false"}:
        return text.lower()
    numeric = _canonical_numeric_text(text)
    return numeric if numeric is not None else text


def _canonical_mapping_sha256(
    values: Mapping[str, object],
    *,
    excluded_columns: frozenset[str] = frozenset({"generated_at"}),
) -> str:
    payload = [
        [str(column), _canonical_value(value)]
        for column, value in sorted(values.items(), key=lambda item: str(item[0]))
        if str(column) not in excluded_columns
    ]
    encoded = json.dumps(
        payload,
        ensure_ascii=False,
        separators=(",", ":"),
    ).encode("utf-8")
    return hashlib.sha256(encoded).hexdigest()


def _canonical_table_sha256(
    frame: pd.DataFrame,
    *,
    excluded_columns: frozenset[str] = frozenset({"generated_at"}),
) -> str:
    columns = sorted(
        str(column)
        for column in frame.columns
        if str(column) not in excluded_columns
    )
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
    encoded = json.dumps(
        payload,
        ensure_ascii=False,
        separators=(",", ":"),
    ).encode("utf-8")
    return hashlib.sha256(encoded).hexdigest()


def _v3_diagnostic_provenance_columns(columns: object) -> frozenset[str]:
    excluded = {"generated_at"}
    for column in columns:
        name = str(column).strip().lower()
        if name.startswith("raw_") or "blob_sha256" in name or "crlf" in name:
            excluded.add(str(column))
    return frozenset(excluded)


def _v3_provenance_excluded_mapping_sha256(
    values: Mapping[str, object],
) -> str:
    return _canonical_mapping_sha256(
        values,
        excluded_columns=_v3_diagnostic_provenance_columns(values),
    )


def _v3_provenance_excluded_table_sha256(frame: pd.DataFrame) -> str:
    return _canonical_table_sha256(
        frame,
        excluded_columns=_v3_diagnostic_provenance_columns(frame.columns),
    )


def _candidate_detail_row_sha256(
    values: Mapping[str, object],
    *,
    artifact_version: str,
) -> str:
    return (
        _v3_provenance_excluded_mapping_sha256(values)
        if artifact_version == V3_ARTIFACT_VERSION
        else _canonical_mapping_sha256(values)
    )


def _candidate_detail_artifact_sha256(
    detail: pd.DataFrame,
    *,
    artifact_version: str,
) -> str:
    return (
        _v3_provenance_excluded_table_sha256(detail)
        if artifact_version == V3_ARTIFACT_VERSION
        else _canonical_table_sha256(detail)
    )


def _canonical_frame_sha256(frame: pd.DataFrame) -> str:
    missing = sorted(set(PRICE_HISTORY_CANONICAL_COLUMNS) - set(frame.columns))
    if missing:
        raise RuntimeError(
            f"low/mid falling price-history canonical columns are missing: {missing}"
        )
    columns = list(PRICE_HISTORY_CANONICAL_COLUMNS)
    canonical = frame.loc[:, columns].sort_values("date", kind="mergesort").reset_index(
        drop=True
    )
    rows = [
        [[column, _canonical_value(row[column])] for column in columns]
        for _, row in canonical.iterrows()
    ]
    payload = {
        "canonical_lineage_version": CANONICAL_LINEAGE_VERSION,
        "columns": columns,
        "rows": rows,
    }
    encoded = json.dumps(
        payload,
        ensure_ascii=False,
        separators=(",", ":"),
    ).encode("utf-8")
    return hashlib.sha256(encoded).hexdigest()


def _normalized_file_sha256(path: Path | str) -> str:
    payload = Path(path).read_bytes().replace(b"\r\n", b"\n")
    return hashlib.sha256(payload).hexdigest()


def _require_sha256(value: object, *, label: str) -> str:
    digest = str(value).strip().lower()
    if not re.fullmatch(r"[0-9a-f]{64}", digest):
        raise RuntimeError(f"low/mid falling {label} is not a canonical SHA-256")
    return digest


def _assert_literal_upstream_contracts() -> None:
    expected = (
        (
            "source-first artifact id",
            source_first_producer.ARTIFACT_ID,
            SOURCE_FIRST_ARTIFACT_ID,
        ),
        (
            "source-first artifact version",
            source_first_producer.ARTIFACT_VERSION,
            SOURCE_FIRST_ARTIFACT_VERSION,
        ),
        (
            "source-first source variant",
            source_first_producer.PRIMARY_VARIANT_ID,
            SOURCE_VARIANT_ID,
        ),
        (
            "source projection artifact id",
            source_projection.ARTIFACT_ID,
            SOURCE_PROJECTION_ARTIFACT_ID,
        ),
        (
            "source projection cutoff date",
            source_projection.CUTOFF_DATE,
            SOURCE_PROJECTION_CUTOFF_DATE,
        ),
        ("rearmed artifact id", rearmed_producer.ARTIFACT_ID, REARMED_ARTIFACT_ID),
        (
            "rearmed artifact version",
            rearmed_producer.ARTIFACT_VERSION,
            REARMED_ARTIFACT_VERSION,
        ),
        (
            "rearmed source artifact id",
            rearmed_producer.SOURCE_ARTIFACT_ID,
            REARMED_SOURCE_ARTIFACT_ID,
        ),
        (
            "rearmed source variant",
            rearmed_producer.SOURCE_VARIANT_ID,
            REARMED_SOURCE_VARIANT_ID,
        ),
        (
            "rearmed no-stop policy",
            rearmed_producer.NO_STOP_POLICY_ID,
            NO_STOP_POLICY_ID,
        ),
        (
            "rearmed persisted detail drop columns",
            tuple(rearmed_producer.DETAIL_ARTIFACT_DROP_COLUMNS),
            REARMED_PERSISTED_DETAIL_DROP_COLUMNS,
        ),
        (
            "position-shape artifact id",
            position_shape_producer.ARTIFACT_ID,
            POSITION_SHAPE_ARTIFACT_ID,
        ),
        (
            "position-shape artifact version",
            position_shape_producer.ARTIFACT_VERSION,
            POSITION_SHAPE_ARTIFACT_VERSION,
        ),
        (
            "position-shape source variant",
            position_shape_producer.SOURCE_VARIANT_ID,
            SOURCE_VARIANT_ID,
        ),
        (
            "position-shape position policy",
            position_shape_producer.POSITION_POLICY,
            POSITION_POLICY,
        ),
        (
            "position-shape shape policy",
            position_shape_producer.SHAPE_POLICY,
            SHAPE_POLICY,
        ),
        (
            "position-shape price-history cutoff",
            position_shape_producer.PRICE_HISTORY_CUTOFF_DATE,
            PRICE_HISTORY_CUTOFF_DATE,
        ),
    )
    for label, observed, literal in expected:
        if observed != literal:
            raise RuntimeError(
                f"low/mid falling pinned upstream contract drift: {label}; "
                f"observed={observed!r} expected={literal!r}"
            )


def _require_constant(
    frame: pd.DataFrame,
    column: str,
    expected: str,
    *,
    label: str,
) -> None:
    observed = set(frame[column].astype(str).str.strip())
    if observed != {expected}:
        raise RuntimeError(
            f"low/mid falling {label} drift: observed={sorted(observed)} "
            f"expected={expected}"
        )


def _require_false(frame: pd.DataFrame, column: str, *, label: str) -> None:
    observed = frame[column].map(_canonical_value).str.lower()
    if not observed.isin({"false", "0", "no"}).all():
        raise RuntimeError(f"low/mid falling {label} must be explicitly false")


def _lineage_set_sha256(frame: pd.DataFrame, column: str) -> str:
    values = sorted(
        {
            _require_sha256(value, label=column)
            for value in frame[column].astype(str)
        }
    )
    payload = json.dumps(
        values,
        ensure_ascii=False,
        separators=(",", ":"),
    ).encode("utf-8")
    return hashlib.sha256(payload).hexdigest()


def _normalize_source(
    source_first_detail: pd.DataFrame,
    *,
    provenance_excluded_hashes: bool = False,
) -> pd.DataFrame:
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
        *MONTHLY_REVENUE_RUN_LINEAGE_COLUMNS,
    }
    missing = sorted(required - set(source_first_detail.columns))
    if missing:
        raise RuntimeError(f"low/mid falling source detail is missing columns: {missing}")
    _require_constant(source_first_detail, "model_id", MODEL_ID, label="source model")
    _require_constant(
        source_first_detail,
        "artifact_id",
        SOURCE_FIRST_ARTIFACT_ID,
        label="source-first artifact id",
    )
    _require_constant(
        source_first_detail,
        "artifact_version",
        SOURCE_FIRST_ARTIFACT_VERSION,
        label="source-first artifact version",
    )
    for column in MONTHLY_REVENUE_RUN_LINEAGE_COLUMNS:
        observed = {
            str(value).strip().lower()
            for value in source_first_detail[column]
        }
        if len(observed) != 1:
            raise RuntimeError(
                f"low/mid falling source-first run lineage is not constant: {column}"
            )
        _require_sha256(next(iter(observed)), label=f"source-first {column}")
    source = source_first_detail.loc[
        source_first_detail["condition_variant_id"].astype(str).eq(SOURCE_VARIANT_ID)
    ].copy()
    if source.empty:
        raise RuntimeError(
            f"low/mid falling source variant is empty or drifted: {SOURCE_VARIANT_ID}"
        )
    _require_constant(
        source,
        "condition_variant_id",
        SOURCE_VARIANT_ID,
        label="source-first variant",
    )
    source["stock_id"] = source["stock_id"].map(_stock_id)
    if source["episode_key"].astype(str).duplicated().any():
        raise RuntimeError("low/mid falling source has duplicate episode keys")
    selected_slice_sha256 = (
        _v3_provenance_excluded_table_sha256(source)
        if provenance_excluded_hashes
        else _canonical_table_sha256(source)
    )
    source["source_first_canonical_row_sha256"] = source.apply(
        lambda row: (
            _v3_provenance_excluded_mapping_sha256(row.to_dict())
            if provenance_excluded_hashes
            else _canonical_mapping_sha256(row.to_dict())
        ),
        axis=1,
    )
    source["source_first_selected_slice_canonical_sha256"] = selected_slice_sha256
    return source.set_index("episode_key", drop=False)


def _normalize_operations(
    rearmed_detail: pd.DataFrame,
    *,
    expected_artifact_version: str = REARMED_ARTIFACT_VERSION,
    provenance_excluded_hashes: bool = False,
) -> pd.DataFrame:
    required = {
        "model_id",
        "artifact_id",
        "artifact_version",
        "source_artifact_id",
        "source_variant_id",
        "grid_id",
        "lifecycle_policy_id",
        "confirmation_variant_id",
        "holding_days",
        "stop_policy_id",
        "return_valid",
        "episode_key",
        "stock_id",
        "stock_name",
        "trigger_date",
        "confirmation_date",
        "entry_index",
        "entry_date",
        "entry_price",
        "planned_exit_index",
        "planned_exit_date",
        "exit_index",
        "exit_date",
        "exit_price",
        "entry_price_basis",
        "fixed_exit_price_basis",
        "exit_price_basis",
        "exit_reason",
        "realized_return_pct",
        "return_outcome",
        "source_anomaly_candidate_flag",
        "unresolved_price_path_candidate_flag",
        "operation_return_review_candidate_flag",
        "intraday_operation_basis_used",
    }
    missing = sorted(required - set(rearmed_detail.columns))
    if missing:
        raise RuntimeError(f"low/mid falling operation detail is missing columns: {missing}")
    _require_constant(rearmed_detail, "model_id", MODEL_ID, label="rearmed model")
    _require_constant(
        rearmed_detail,
        "artifact_id",
        REARMED_ARTIFACT_ID,
        label="rearmed artifact id",
    )
    _require_constant(
        rearmed_detail,
        "artifact_version",
        expected_artifact_version,
        label="rearmed artifact version",
    )
    _require_constant(
        rearmed_detail,
        "source_artifact_id",
        REARMED_SOURCE_ARTIFACT_ID,
        label="rearmed source artifact id",
    )
    _require_constant(
        rearmed_detail,
        "source_variant_id",
        REARMED_SOURCE_VARIANT_ID,
        label="rearmed source variant",
    )
    _require_false(
        rearmed_detail,
        "intraday_operation_basis_used",
        label="rearmed intraday operation basis",
    )
    lifecycle_values = set(
        rearmed_detail["lifecycle_policy_id"].astype(str).str.strip()
    )
    if not lifecycle_values or not lifecycle_values.issubset(LIFECYCLE_POLICY_IDS):
        raise RuntimeError(
            f"low/mid falling rearmed lifecycle drift: {sorted(lifecycle_values)}"
        )
    confirmation_values = set(
        rearmed_detail["confirmation_variant_id"].astype(str).str.strip()
    )
    if not confirmation_values or not confirmation_values.issubset(
        CONFIRMATION_VARIANT_IDS
    ):
        raise RuntimeError(
            f"low/mid falling rearmed confirmation drift: {sorted(confirmation_values)}"
        )
    holding = pd.to_numeric(rearmed_detail["holding_days"], errors="coerce")
    if holding.isna().any() or not np.isclose(holding, holding.round()).all():
        raise RuntimeError("low/mid falling rearmed holding-days contract is invalid")
    expected_grid = (
        rearmed_detail["lifecycle_policy_id"].astype(str).str.strip()
        + "|"
        + rearmed_detail["confirmation_variant_id"].astype(str).str.strip()
        + "|d"
        + holding.round().astype("int64").astype(str)
        + "|"
        + rearmed_detail["stop_policy_id"].astype(str).str.strip()
    )
    if not rearmed_detail["grid_id"].astype(str).str.strip().eq(expected_grid).all():
        raise RuntimeError("low/mid falling rearmed grid contract drift")
    if not rearmed_detail["entry_price_basis"].astype(str).str.strip().eq(
        REARMED_ENTRY_PRICE_BASIS
    ).all():
        raise RuntimeError("low/mid falling rearmed entry price basis drift")

    selected_mask = (
        rearmed_detail["lifecycle_policy_id"].astype(str).isin(LIFECYCLE_POLICY_IDS)
        & rearmed_detail["confirmation_variant_id"].astype(str).isin(
            CONFIRMATION_VARIANT_IDS
        )
        & holding.eq(HOLDING_DAYS)
        & rearmed_detail["stop_policy_id"].astype(str).eq(NO_STOP_POLICY_ID)
        & _boolish(rearmed_detail["return_valid"])
    )
    operations = rearmed_detail.loc[selected_mask].copy()
    if operations.empty:
        raise RuntimeError("low/mid falling operation slice is empty")
    if set(operations["lifecycle_policy_id"].astype(str)) != set(
        LIFECYCLE_POLICY_IDS
    ):
        raise RuntimeError("low/mid falling selected lifecycle contract is incomplete")
    if set(operations["confirmation_variant_id"].astype(str)) != set(
        CONFIRMATION_VARIANT_IDS
    ):
        raise RuntimeError("low/mid falling selected confirmation contract is incomplete")
    _require_constant(
        operations,
        "stop_policy_id",
        NO_STOP_POLICY_ID,
        label="selected stop policy",
    )
    _require_constant(
        operations,
        "entry_price_basis",
        REARMED_ENTRY_PRICE_BASIS,
        label="selected entry price basis",
    )
    _require_constant(
        operations,
        "fixed_exit_price_basis",
        REARMED_FIXED_EXIT_PRICE_BASIS,
        label="selected fixed exit price basis",
    )
    _require_constant(
        operations,
        "exit_price_basis",
        REARMED_EXIT_PRICE_BASIS,
        label="selected exit price basis",
    )
    _require_constant(
        operations,
        "exit_reason",
        REARMED_EXIT_REASON,
        label="selected exit reason",
    )
    operations["stock_id"] = operations["stock_id"].map(_stock_id)
    for column in ("trigger_date", "confirmation_date", "entry_date", "exit_date"):
        operations[column] = operations[column].map(_date_text)
        if operations[column].eq("").any():
            raise RuntimeError(f"low/mid falling operation has invalid {column}")
    operations["realized_return_pct"] = pd.to_numeric(
        operations["realized_return_pct"], errors="coerce"
    )
    if operations["realized_return_pct"].isna().any():
        raise RuntimeError("low/mid falling operation has invalid realized return")
    first_match = operations.loc[
        operations["lifecycle_policy_id"].eq("episode_first_match_once")
    ]
    if first_match.duplicated(
        ["confirmation_variant_id", "stock_id", "episode_key"]
    ).any():
        raise RuntimeError(
            "low/mid falling rearmed episode_first_match_once has multiple operations "
            "per episode"
        )
    duplicate_columns = [
        "grid_id",
        "stock_id",
        "episode_key",
        "trigger_date",
        "entry_date",
    ]
    if operations.duplicated(duplicate_columns).any():
        raise RuntimeError("low/mid falling rearmed D30/no-stop slice has duplicate rows")
    overlap_count = _operation_overlap_pair_count(operations)
    if overlap_count:
        raise RuntimeError(
            f"low/mid falling rearmed D30/no-stop slice contains same-stock overlap: "
            f"{overlap_count}"
        )
    drop_columns = set(REARMED_PERSISTED_DETAIL_DROP_COLUMNS)
    present_drop_columns = drop_columns.intersection(operations.columns)
    if present_drop_columns and present_drop_columns != drop_columns:
        missing_drop_columns = sorted(drop_columns - present_drop_columns)
        raise RuntimeError(
            "low/mid falling rearmed persisted-schema projection is partial; "
            f"missing drop columns: {missing_drop_columns}"
        )
    persisted_hash_view = (
        operations.drop(columns=list(REARMED_PERSISTED_DETAIL_DROP_COLUMNS))
        if present_drop_columns
        else operations.copy()
    )
    selected_slice_sha256 = (
        _v3_provenance_excluded_table_sha256(persisted_hash_view)
        if provenance_excluded_hashes
        else _canonical_table_sha256(persisted_hash_view)
    )
    operations["rearmed_operation_canonical_row_sha256"] = persisted_hash_view.apply(
        lambda row: (
            _v3_provenance_excluded_mapping_sha256(row.to_dict())
            if provenance_excluded_hashes
            else _canonical_mapping_sha256(row.to_dict())
        ),
        axis=1,
    )
    operations["rearmed_d30_no_stop_slice_canonical_sha256"] = (
        selected_slice_sha256
    )
    return operations.sort_values(
        [
            "lifecycle_policy_id",
            "confirmation_variant_id",
            "stock_id",
            "entry_date",
            "episode_key",
        ],
        kind="mergesort",
    ).reset_index(drop=True)


def _asof_source(
    episode: pd.Series,
    stock: pd.DataFrame,
    trigger_index: int,
) -> dict[str, object]:
    periods = _split(episode["qualifying_revenue_periods"])
    source_dates = [_date_text(value) for value in _split(episode["qualifying_source_dates"])]
    resolution_ids = [
        _canonical_value(value)
        for value in _split(episode["qualifying_cross_market_resolution_ids"])
    ]
    source_row_sha256s = [
        _require_sha256(value, label="qualifying source-row lineage")
        for value in _split(episode["qualifying_source_row_canonical_sha256s"])
    ]
    canonical_source_table_dates = [
        _date_text(value)
        for value in _split(episode["qualifying_canonical_source_table_dates"])
    ]
    trade_dates = [_date_text(value) for value in _split(episode["qualifying_trade_dates"])]
    try:
        sequence_indices = [int(value) for value in _split(episode["qualifying_sequence_indices"])]
    except ValueError as exc:
        raise RuntimeError(
            f"low/mid falling qualifying sequence is invalid: {episode['episode_key']}"
        ) from exc
    lengths = {
        len(periods),
        len(source_dates),
        len(resolution_ids),
        len(source_row_sha256s),
        len(canonical_source_table_dates),
        len(trade_dates),
        len(sequence_indices),
        int(episode["qualifying_update_count"]),
    }
    if len(lengths) != 1 or not periods:
        raise RuntimeError(
            f"low/mid falling qualifying lineage is not aligned: {episode['episode_key']}"
        )
    aligned_text_values = (
        source_dates + resolution_ids + canonical_source_table_dates + trade_dates
    )
    if any(not value for value in aligned_text_values):
        raise RuntimeError(
            f"low/mid falling qualifying source lineage contains an empty value: "
            f"{episode['episode_key']}"
        )
    scalar_lineage = (
        (
            "episode_start_revenue_period",
            periods[0],
            _canonical_value,
        ),
        ("episode_start_source_date", source_dates[0], _date_text),
        (
            "episode_start_cross_market_resolution_id",
            resolution_ids[0],
            _canonical_value,
        ),
        (
            "episode_start_source_row_canonical_sha256",
            source_row_sha256s[0],
            lambda value: _require_sha256(value, label="episode-start source row"),
        ),
        (
            "episode_start_canonical_source_table_date",
            canonical_source_table_dates[0],
            _date_text,
        ),
        ("episode_start_trade_date", trade_dates[0], _date_text),
        (
            "episode_start_sequence_index",
            sequence_indices[0],
            lambda value: int(value),
        ),
        (
            "latest_qualifying_revenue_period",
            periods[-1],
            _canonical_value,
        ),
        ("latest_qualifying_source_date", source_dates[-1], _date_text),
        (
            "latest_qualifying_cross_market_resolution_id",
            resolution_ids[-1],
            _canonical_value,
        ),
        (
            "latest_qualifying_source_row_canonical_sha256",
            source_row_sha256s[-1],
            lambda value: _require_sha256(value, label="latest qualifying source row"),
        ),
        (
            "latest_qualifying_canonical_source_table_date",
            canonical_source_table_dates[-1],
            _date_text,
        ),
        ("latest_qualifying_trade_date", trade_dates[-1], _date_text),
        (
            "latest_qualifying_sequence_index",
            sequence_indices[-1],
            lambda value: int(value),
        ),
    )
    try:
        scalar_mismatches = [
            column
            for column, expected, normalizer in scalar_lineage
            if normalizer(episode[column]) != expected
        ]
    except (TypeError, ValueError) as exc:
        raise RuntimeError(
            f"low/mid falling qualifying scalar lineage is invalid: {episode['episode_key']}"
        ) from exc
    if scalar_mismatches:
        raise RuntimeError(
            "low/mid falling qualifying scalar/list lineage drift: "
            f"{episode['episode_key']}/{scalar_mismatches}"
        )
    if sequence_indices != sorted(set(sequence_indices)):
        raise RuntimeError(
            f"low/mid falling qualifying sequence is not strictly increasing: "
            f"{episode['episode_key']}"
        )
    if trade_dates != sorted(set(trade_dates)):
        raise RuntimeError(
            f"low/mid falling qualifying trade dates are not strictly increasing: "
            f"{episode['episode_key']}"
        )
    date_index = {str(date): int(index) for index, date in stock["date"].items()}
    if len(date_index) != len(stock):
        raise RuntimeError(
            f"low/mid falling price history has duplicate dates: {episode['stock_id']}"
        )
    for trade_date, sequence_index in zip(trade_dates, sequence_indices):
        if trade_date not in date_index:
            raise RuntimeError(
                "low/mid falling qualifying trade date is absent from normalized price "
                f"history: {episode['episode_key']}/{trade_date}"
            )
        if date_index[trade_date] != sequence_index:
            raise RuntimeError(
                "low/mid falling qualifying sequence index drift: "
                f"{episode['episode_key']}/{trade_date}/"
                f"{sequence_index}/{date_index[trade_date]}"
            )
    ordered_dates = stock["date"].astype(str).tolist()
    for source_date, trade_date in zip(source_dates, trade_dates):
        first_available = next(
            (date for date in ordered_dates if date >= source_date),
            "",
        )
        if first_available != trade_date:
            raise RuntimeError(
                "low/mid falling qualifying trade date is not the first normalized "
                f"session on or after source availability: "
                f"{episode['episode_key']}/{source_date}/{trade_date}/{first_available}"
            )
    asof_positions = [
        position
        for position, (source_date, trade_date, sequence_index) in enumerate(
            zip(source_dates, trade_dates, sequence_indices)
        )
        if source_date
        and source_date <= trade_date
        and date_index[trade_date] <= trigger_index
        and sequence_index == date_index[trade_date]
        and sequence_index <= trigger_index
    ]
    if not asof_positions:
        raise RuntimeError(
            f"low/mid falling operation has no qualifying source known by trigger: "
            f"{episode['episode_key']}"
        )
    position = asof_positions[-1]
    source_index = date_index[trade_dates[position]]
    return {
        "asof_latest_qualifying_revenue_period": periods[position],
        "asof_latest_qualifying_source_date": source_dates[position],
        "asof_latest_qualifying_cross_market_resolution_id": (
            resolution_ids[position]
        ),
        "asof_latest_qualifying_source_row_canonical_sha256": (
            source_row_sha256s[position]
        ),
        "asof_latest_qualifying_canonical_source_table_date": (
            canonical_source_table_dates[position]
        ),
        "asof_latest_qualifying_trade_date": trade_dates[position],
        "asof_latest_qualifying_sequence_index": sequence_indices[position],
        "latest_source_to_trigger_trading_days": trigger_index - source_index,
        "future_qualifying_update_ignored_count": len(periods) - position - 1,
        "source_index": source_index,
    }


def _validate_operation_timing(operation: pd.Series, stock: pd.DataFrame) -> dict[str, int]:
    date_index = {str(date): int(index) for index, date in stock["date"].items()}
    named = {
        "trigger": str(operation["trigger_date"]),
        "confirmation": str(operation["confirmation_date"]),
        "entry": str(operation["entry_date"]),
        "exit": str(operation["exit_date"]),
    }
    missing = [name for name, date in named.items() if date not in date_index]
    if missing:
        raise RuntimeError(
            f"low/mid falling operation dates are absent from price history: "
            f"{operation['stock_id']}/{operation['episode_key']}/{missing}"
        )
    indices = {name: date_index[date] for name, date in named.items()}
    confirmation_variant = str(operation["confirmation_variant_id"])
    expected_confirmation_offset = (
        0 if confirmation_variant == "base_close_confirmed" else 1
    )
    if indices["confirmation"] != indices["trigger"] + expected_confirmation_offset:
        raise RuntimeError(
            f"low/mid falling confirmation timing drift: {confirmation_variant}"
        )
    if indices["entry"] != indices["confirmation"] + 1:
        raise RuntimeError(f"low/mid falling entry timing drift: {confirmation_variant}")
    if indices["exit"] != indices["entry"] + HOLDING_SESSION_INDEX_OFFSET:
        raise RuntimeError(f"low/mid falling D30 exit timing drift: {confirmation_variant}")
    recorded_indices = {
        "entry": "entry_index",
        "exit": "exit_index",
        "planned_exit": "planned_exit_index",
    }
    try:
        recorded = {
            name: int(operation[column])
            for name, column in recorded_indices.items()
        }
    except (TypeError, ValueError) as exc:
        raise RuntimeError(
            f"low/mid falling operation index lineage is invalid: "
            f"{operation['stock_id']}/{operation['episode_key']}"
        ) from exc
    if recorded["entry"] != indices["entry"]:
        raise RuntimeError("low/mid falling recorded entry index drift")
    if recorded["exit"] != indices["exit"]:
        raise RuntimeError("low/mid falling recorded exit index drift")
    if recorded["planned_exit"] != indices["exit"]:
        raise RuntimeError("low/mid falling recorded planned exit index drift")
    if _date_text(operation["planned_exit_date"]) != str(operation["exit_date"]):
        raise RuntimeError("low/mid falling recorded planned exit date drift")
    if confirmation_variant == "delayed_next_close_continuation_bonus":
        trigger_close = _number(stock.at[indices["trigger"], "analysis_close"])
        confirmation_close = _number(stock.at[indices["confirmation"], "analysis_close"])
        if not (
            np.isfinite(trigger_close)
            and np.isfinite(confirmation_close)
            and confirmation_close > trigger_close
        ):
            raise RuntimeError("low/mid falling delayed confirmation lacks continuation")
    if "intraday_operation_basis_used" in operation.index and _bool_value(
        operation["intraday_operation_basis_used"]
    ):
        raise RuntimeError("low/mid falling operation cannot use intraday price basis")
    entry_open = _number(stock.at[indices["entry"], "analysis_open"])
    exit_close = _number(stock.at[indices["exit"], "analysis_close"])
    if not (
        np.isfinite(entry_open)
        and entry_open > 0
        and np.isfinite(exit_close)
        and exit_close > 0
    ):
        raise RuntimeError("low/mid falling operation has invalid entry or exit price")
    recorded_entry = _number(operation["entry_price"])
    recorded_exit = _number(operation["exit_price"])
    if not math.isclose(recorded_entry, entry_open, abs_tol=0.00000001):
        raise RuntimeError("low/mid falling recorded entry price drift")
    if not math.isclose(recorded_exit, exit_close, abs_tol=0.00000001):
        raise RuntimeError("low/mid falling recorded exit price drift")
    replayed = (exit_close / entry_open - 1.0) * 100.0
    if not math.isclose(
        replayed,
        float(operation["realized_return_pct"]),
        abs_tol=0.00011,
    ):
        raise RuntimeError(
            f"low/mid falling realized return replay drift: "
            f"{operation['stock_id']}/{operation['entry_date']}"
        )
    return indices


def _operation_overlap_pair_count(detail: pd.DataFrame) -> int:
    if detail.empty:
        return 0
    overlaps = 0
    group_columns = ["lifecycle_policy_id", "confirmation_variant_id", "stock_id"]
    for _keys, group in detail.groupby(group_columns, sort=False, dropna=False):
        prior_exit = ""
        for row in group.sort_values("entry_date", kind="mergesort").itertuples(
            index=False
        ):
            if prior_exit and str(row.entry_date) <= prior_exit:
                overlaps += 1
            prior_exit = max(prior_exit, str(row.exit_date))
    return overlaps


def _build_detail(
    source: pd.DataFrame,
    operations: pd.DataFrame,
    daily_by_stock: Mapping[str, pd.DataFrame],
    generated_at: str,
    *,
    producer_semantic_sha256: str,
    source_first_producer_semantic_sha256: str,
    rearmed_producer_semantic_sha256: str,
    position_shape_producer_semantic_sha256: str,
    data_contract_sha256: str,
    artifact_version: str = ARTIFACT_VERSION,
    rearmed_artifact_version: str = REARMED_ARTIFACT_VERSION,
) -> pd.DataFrame:
    daily = {
        _stock_id(stock_id): _normalize_price_frame(frame, _stock_id(stock_id))
        for stock_id, frame in daily_by_stock.items()
    }
    price_history_sha256: dict[str, str] = {}
    for stock_id, stock in daily.items():
        if stock["date"].astype(str).duplicated().any():
            raise RuntimeError(
                f"low/mid falling normalized price history has duplicate dates: {stock_id}"
            )
        price_history_sha256[stock_id] = _canonical_frame_sha256(stock)
    price_history_manifest_sha256 = _canonical_table_sha256(
        pd.DataFrame(
            [
                {
                    "stock_id": stock_id,
                    "price_history_canonical_sha256": digest,
                }
                for stock_id, digest in sorted(price_history_sha256.items())
            ]
        )
    )
    rows: list[dict[str, object]] = []
    for _, operation in operations.iterrows():
        episode_key = str(operation["episode_key"])
        if episode_key not in source.index:
            raise RuntimeError(f"low/mid falling source episode is missing: {episode_key}")
        episode = source.loc[episode_key]
        stock_id = str(operation["stock_id"])
        if str(episode["stock_id"]) != stock_id:
            raise RuntimeError(f"low/mid falling source stock drift: {episode_key}")
        stock = daily.get(stock_id)
        if stock is None:
            raise RuntimeError(f"low/mid falling price history is missing: {stock_id}")
        indices = _validate_operation_timing(operation, stock)
        asof = _asof_source(episode, stock, indices["trigger"])
        lag = int(asof["latest_source_to_trigger_trading_days"])
        if lag < 0:
            raise RuntimeError(f"low/mid falling source is after trigger: {episode_key}")
        if lag > WATCH_HORIZON_TRADING_DAYS:
            continue
        features = _anchor_features(stock, int(asof["source_index"]))
        position_bucket = str(features["position_bucket"])
        shape_bucket = str(features["shape_bucket"])
        low_member = position_bucket == "low_pos_le40" and shape_bucket == "falling"
        mid_member = position_bucket == "mid_pos_40_75" and shape_bucket == "falling"
        union_member = low_member or mid_member
        if not union_member:
            continue
        realized_return = float(operation["realized_return_pct"])
        expected_outcome = (
            "win" if realized_return > 1e-9 else "failure" if realized_return < -1e-9 else "neutral"
        )
        if str(operation["return_outcome"]) != expected_outcome:
            raise RuntimeError(f"low/mid falling return outcome drift: {episode_key}")
        source_candidate = _bool_value(operation["source_anomaly_candidate_flag"])
        price_candidate = _bool_value(
            operation["unresolved_price_path_candidate_flag"]
        )
        return_candidate = _bool_value(
            operation["operation_return_review_candidate_flag"]
        )
        combined_candidate = source_candidate or price_candidate or return_candidate
        operation_key = "|".join(
            (
                str(operation["lifecycle_policy_id"]),
                str(operation["confirmation_variant_id"]),
                stock_id,
                episode_key,
                str(operation["trigger_date"]),
                str(operation["entry_date"]),
            )
        )
        rows.append(
            {
                "generated_at": generated_at,
                "model_id": MODEL_ID,
                "artifact_id": ARTIFACT_ID,
                "artifact_version": artifact_version,
                "canonical_lineage_version": CANONICAL_LINEAGE_VERSION,
                "data_contract_sha256": data_contract_sha256,
                "producer_semantic_sha256": producer_semantic_sha256,
                "source_first_producer_semantic_sha256": (
                    source_first_producer_semantic_sha256
                ),
                "rearmed_producer_semantic_sha256": (
                    rearmed_producer_semantic_sha256
                ),
                "position_shape_producer_semantic_sha256": (
                    position_shape_producer_semantic_sha256
                ),
                "source_first_artifact_id": SOURCE_FIRST_ARTIFACT_ID,
                "source_first_artifact_version": SOURCE_FIRST_ARTIFACT_VERSION,
                "source_variant_id": SOURCE_VARIANT_ID,
                **{
                    column: str(episode[column]).strip().lower()
                    for column in MONTHLY_REVENUE_RUN_LINEAGE_COLUMNS
                },
                "source_first_canonical_row_sha256": str(
                    episode["source_first_canonical_row_sha256"]
                ),
                "source_first_selected_slice_canonical_sha256": str(
                    episode["source_first_selected_slice_canonical_sha256"]
                ),
                "rearmed_artifact_id": REARMED_ARTIFACT_ID,
                "rearmed_artifact_version": rearmed_artifact_version,
                "rearmed_grid_id": str(operation["grid_id"]),
                "rearmed_operation_canonical_row_sha256": str(
                    operation["rearmed_operation_canonical_row_sha256"]
                ),
                "rearmed_d30_no_stop_slice_canonical_sha256": str(
                    operation["rearmed_d30_no_stop_slice_canonical_sha256"]
                ),
                "price_history_canonical_sha256": price_history_sha256[stock_id],
                "price_history_manifest_canonical_sha256": (
                    price_history_manifest_sha256
                ),
                "operation_key": operation_key,
                "paired_trigger_key": "|".join(
                    (
                        str(operation["lifecycle_policy_id"]),
                        stock_id,
                        episode_key,
                        str(operation["trigger_date"]),
                    )
                ),
                "lifecycle_policy_id": str(operation["lifecycle_policy_id"]),
                "confirmation_variant_id": str(operation["confirmation_variant_id"]),
                "holding_days": HOLDING_DAYS,
                "stop_policy_id": NO_STOP_POLICY_ID,
                "episode_key": episode_key,
                "stock_id": stock_id,
                "stock_name": str(operation["stock_name"]),
                **{key: value for key, value in asof.items() if key != "source_index"},
                "trigger_date": str(operation["trigger_date"]),
                "confirmation_date": str(operation["confirmation_date"]),
                "trigger_index": indices["trigger"],
                "confirmation_index": indices["confirmation"],
                "entry_index": indices["entry"],
                "entry_date": str(operation["entry_date"]),
                "entry_price": round(float(operation["entry_price"]), 8),
                "planned_exit_index": int(operation["planned_exit_index"]),
                "planned_exit_date": _date_text(operation["planned_exit_date"]),
                "exit_index": indices["exit"],
                "exit_date": str(operation["exit_date"]),
                "exit_price": round(float(operation["exit_price"]), 8),
                "entry_price_basis": str(operation["entry_price_basis"]),
                "fixed_exit_price_basis": str(operation["fixed_exit_price_basis"]),
                "exit_price_basis": str(operation["exit_price_basis"]),
                "exit_reason": str(operation["exit_reason"]),
                "holding_session_index_offset": HOLDING_SESSION_INDEX_OFFSET,
                "holding_session_contract": HOLDING_SESSION_CONTRACT,
                "intraday_operation_basis_used": False,
                "realized_return_pct": round(realized_return, 4),
                "return_outcome": expected_outcome,
                "realized_return_ge20": realized_return >= 20.0,
                "realized_return_le_minus20": realized_return <= -20.0,
                "source_anchor_date": str(asof["asof_latest_qualifying_trade_date"]),
                "source_position_120d_pct": features["position_120d_pct"],
                "source_shape_return20_pct": features["shape_return20_pct"],
                "source_shape_range23_pct": features["shape_range23_pct"],
                "source_shape_ema23_slope5_pct": features[
                    "shape_ema23_slope5_pct"
                ],
                "source_position_bucket": position_bucket,
                "source_shape_bucket": shape_bucket,
                "source_position_shape_cell_id": features["position_shape_cell_id"],
                "source_classification_observed": features[
                    "classification_observed"
                ],
                "mid_falling_member": mid_member,
                "low_falling_member": low_member,
                "low_or_mid_falling_union_member": union_member,
                "source_anomaly_candidate_flag": source_candidate,
                "unresolved_price_path_candidate_flag": price_candidate,
                "operation_return_review_candidate_flag": return_candidate,
                "combined_exclusion_candidate_flag": combined_candidate,
                "primary_included": True,
                "sensitivity_included": not combined_candidate,
                "same_stock_non_overlap_applied": True,
                "watch_horizon_trading_days": WATCH_HORIZON_TRADING_DAYS,
                "watch_horizon_passed": True,
                "position_policy": POSITION_POLICY,
                "shape_policy": SHAPE_POLICY,
                "anomaly_policy": ANOMALY_POLICY,
                "financial_statement_scope": FINANCIAL_STATEMENT_SCOPE,
                "approved_for_daily": False,
                "presentation_allowed": False,
                "formal_model_use_allowed": False,
                "production_change": False,
                "promotion_readiness": "research_only_pending_holdout_validation",
            }
        )
    if not rows:
        raise RuntimeError("low/mid falling candidate slice is empty")
    detail = pd.DataFrame(rows).sort_values(
        [
            "lifecycle_policy_id",
            "confirmation_variant_id",
            "stock_id",
            "entry_date",
        ],
        kind="mergesort",
    ).reset_index(drop=True)
    first_match = detail.loc[
        detail["lifecycle_policy_id"].eq("episode_first_match_once")
    ]
    if first_match.duplicated(
        ["confirmation_variant_id", "stock_id", "episode_key"]
    ).any():
        raise RuntimeError(
            "low/mid falling episode_first_match_once has multiple operations per episode"
        )
    if detail["operation_key"].duplicated().any():
        raise RuntimeError("low/mid falling detail has duplicate operation keys")
    overlap_count = _operation_overlap_pair_count(detail)
    if overlap_count:
        raise RuntimeError(
            f"low/mid falling detail contains same-stock overlap: {overlap_count}"
        )
    detail["candidate_detail_row_sha256"] = detail.apply(
        lambda row: _candidate_detail_row_sha256(
            row.to_dict(), artifact_version=artifact_version
        ),
        axis=1,
    )
    detail_artifact_sha256 = _candidate_detail_artifact_sha256(
        detail,
        artifact_version=artifact_version,
    )
    detail["detail_artifact_canonical_sha256"] = detail_artifact_sha256
    for source_column, set_column in (
        (
            "source_first_canonical_row_sha256",
            "source_first_canonical_row_set_sha256",
        ),
        (
            "rearmed_operation_canonical_row_sha256",
            "rearmed_operation_canonical_row_set_sha256",
        ),
        (
            "price_history_canonical_sha256",
            "price_history_canonical_set_sha256",
        ),
        (
            "candidate_detail_row_sha256",
            "candidate_detail_row_set_sha256",
        ),
    ):
        detail[set_column] = _lineage_set_sha256(detail, source_column)
    return detail


def _performance_metrics(part: pd.DataFrame) -> dict[str, object]:
    returns = pd.to_numeric(part["realized_return_pct"], errors="coerce")
    outcomes = part["return_outcome"].astype(str)
    count = len(part)
    wins = int(outcomes.eq("win").sum())
    neutral = int(outcomes.eq("neutral").sum())
    failures = int(outcomes.eq("failure").sum())
    ge20 = int(returns.ge(20.0).sum())
    le_minus20 = int(returns.le(-20.0).sum())
    return {
        "operation_count": count,
        "unique_stock_count": int(part["stock_id"].nunique()),
        "unique_episode_count": int(part["episode_key"].nunique()),
        "win_count": wins,
        "neutral_count": neutral,
        "failure_count": failures,
        "win_rate_pct": _rate(wins, count),
        "neutral_rate_pct": _rate(neutral, count),
        "failure_rate_pct": _rate(failures, count),
        "avg_return_pct": _metric(returns, "mean"),
        "median_return_pct": _metric(returns, "median"),
        "p10_return_pct": _metric(returns, "p10"),
        "p90_return_pct": _metric(returns, "p90"),
        "min_return_pct": _metric(returns, "min"),
        "max_return_pct": _metric(returns, "max"),
        "return_ge20_count": ge20,
        "return_ge20_rate_pct": _rate(ge20, count),
        "return_le_minus20_count": le_minus20,
        "return_le_minus20_rate_pct": _rate(le_minus20, count),
        "top1_abs_return_share_pct": _top_abs_share(returns, 1),
        "top5_abs_return_share_pct": _top_abs_share(returns, 5),
        "source_anomaly_candidate_count": int(
            _boolish(part["source_anomaly_candidate_flag"]).sum()
        ),
        "unresolved_price_path_candidate_count": int(
            _boolish(part["unresolved_price_path_candidate_flag"]).sum()
        ),
        "operation_return_review_candidate_count": int(
            _boolish(part["operation_return_review_candidate_flag"]).sum()
        ),
        "combined_exclusion_candidate_count": int(
            _boolish(part["combined_exclusion_candidate_flag"]).sum()
        ),
        "same_stock_overlap_pair_count": _operation_overlap_pair_count(part),
    }


def _artifact_lineage(detail: pd.DataFrame) -> dict[str, str]:
    first = detail.iloc[0]
    return {
        "canonical_lineage_version": str(first["canonical_lineage_version"]),
        "data_contract_sha256": str(first["data_contract_sha256"]),
        "producer_semantic_sha256": str(first["producer_semantic_sha256"]),
        "source_first_producer_semantic_sha256": str(
            first["source_first_producer_semantic_sha256"]
        ),
        "rearmed_producer_semantic_sha256": str(
            first["rearmed_producer_semantic_sha256"]
        ),
        "position_shape_producer_semantic_sha256": str(
            first["position_shape_producer_semantic_sha256"]
        ),
        "source_first_artifact_id": str(first["source_first_artifact_id"]),
        "source_first_artifact_version": str(
            first["source_first_artifact_version"]
        ),
        **{
            column: str(first[column])
            for column in MONTHLY_REVENUE_RUN_LINEAGE_COLUMNS
        },
        "rearmed_artifact_id": str(first["rearmed_artifact_id"]),
        "rearmed_artifact_version": str(first["rearmed_artifact_version"]),
        "source_first_selected_slice_canonical_sha256": str(
            first["source_first_selected_slice_canonical_sha256"]
        ),
        "rearmed_d30_no_stop_slice_canonical_sha256": str(
            first["rearmed_d30_no_stop_slice_canonical_sha256"]
        ),
        "price_history_manifest_canonical_sha256": str(
            first["price_history_manifest_canonical_sha256"]
        ),
        "detail_artifact_canonical_sha256": str(
            first["detail_artifact_canonical_sha256"]
        ),
        "source_first_canonical_row_set_sha256": str(
            first["source_first_canonical_row_set_sha256"]
        ),
        "rearmed_operation_canonical_row_set_sha256": str(
            first["rearmed_operation_canonical_row_set_sha256"]
        ),
        "price_history_canonical_set_sha256": str(
            first["price_history_canonical_set_sha256"]
        ),
        "candidate_detail_row_set_sha256": str(
            first["candidate_detail_row_set_sha256"]
        ),
    }


def _build_summary(detail: pd.DataFrame) -> pd.DataFrame:
    rows: list[dict[str, object]] = []
    for analysis_basis in ANALYSIS_BASES:
        basis = (
            detail
            if analysis_basis == PRIMARY_ANALYSIS_BASIS
            else detail.loc[_boolish(detail["sensitivity_included"])]
        )
        for lifecycle_order, lifecycle_id in enumerate(LIFECYCLE_POLICY_IDS, start=1):
            for confirmation_order, confirmation_id in enumerate(
                CONFIRMATION_VARIANT_IDS, start=1
            ):
                grid = basis.loc[
                    basis["lifecycle_policy_id"].eq(lifecycle_id)
                    & basis["confirmation_variant_id"].eq(confirmation_id)
                ]
                for variant_order, variant_id, member_column in VARIANT_SPECS:
                    part = grid.loc[_boolish(grid[member_column])]
                    rows.append(
                        {
                            "generated_at": str(detail["generated_at"].iloc[0]),
                            "model_id": MODEL_ID,
                            "artifact_id": ARTIFACT_ID,
                            "artifact_version": ARTIFACT_VERSION,
                            **_artifact_lineage(detail),
                            "source_variant_id": SOURCE_VARIANT_ID,
                            "analysis_basis": analysis_basis,
                            "lifecycle_order": lifecycle_order * 10,
                            "lifecycle_policy_id": lifecycle_id,
                            "confirmation_order": confirmation_order * 10,
                            "confirmation_variant_id": confirmation_id,
                            "candidate_variant_order": variant_order,
                            "candidate_variant_id": variant_id,
                            "candidate_member_column": member_column,
                            "holding_days": HOLDING_DAYS,
                            "stop_policy_id": NO_STOP_POLICY_ID,
                            "watch_horizon_trading_days": WATCH_HORIZON_TRADING_DAYS,
                            **_performance_metrics(part),
                            "sample_policy": SAMPLE_POLICY,
                            "anomaly_policy": ANOMALY_POLICY,
                            "same_stock_non_overlap_policy": NON_OVERLAP_POLICY,
                            "financial_statement_scope": FINANCIAL_STATEMENT_SCOPE,
                            "approved_for_daily": False,
                            "presentation_allowed": False,
                            "formal_model_use_allowed": False,
                            "production_change": False,
                            "promotion_readiness": "research_only_pending_holdout_validation",
                        }
                    )
    return pd.DataFrame(rows).sort_values(
        [
            "analysis_basis",
            "lifecycle_order",
            "confirmation_order",
            "candidate_variant_order",
        ],
        kind="mergesort",
    ).reset_index(drop=True)


def _build_paired_confirmation(detail: pd.DataFrame) -> pd.DataFrame:
    key_columns = [
        "lifecycle_policy_id",
        "stock_id",
        "episode_key",
        "trigger_date",
    ]
    common_columns = [
        *key_columns,
        "stock_name",
        "source_first_canonical_row_sha256",
        "price_history_canonical_sha256",
        "asof_latest_qualifying_source_date",
        "asof_latest_qualifying_trade_date",
        "latest_source_to_trigger_trading_days",
        "source_position_120d_pct",
        "source_shape_return20_pct",
        "source_shape_range23_pct",
        "source_shape_ema23_slope5_pct",
        "source_position_bucket",
        "source_shape_bucket",
        "source_position_shape_cell_id",
        "mid_falling_member",
        "low_falling_member",
        "low_or_mid_falling_union_member",
        "source_anomaly_candidate_flag",
        "unresolved_price_path_candidate_flag",
    ]
    base = detail.loc[
        detail["confirmation_variant_id"].eq("base_close_confirmed"),
        [
            *common_columns,
            "confirmation_date",
            "entry_date",
            "exit_date",
            "realized_return_pct",
            "rearmed_operation_canonical_row_sha256",
            "candidate_detail_row_sha256",
            "operation_return_review_candidate_flag",
            "combined_exclusion_candidate_flag",
        ],
    ].copy()
    delayed = detail.loc[
        detail["confirmation_variant_id"].eq(
            "delayed_next_close_continuation_bonus"
        ),
        [
            *common_columns,
            "confirmation_date",
            "entry_date",
            "exit_date",
            "realized_return_pct",
            "rearmed_operation_canonical_row_sha256",
            "candidate_detail_row_sha256",
            "operation_return_review_candidate_flag",
            "combined_exclusion_candidate_flag",
        ],
    ].copy()
    if base.duplicated(key_columns).any() or delayed.duplicated(key_columns).any():
        raise RuntimeError("low/mid falling paired confirmation keys are duplicated")
    paired = base.merge(
        delayed,
        on=key_columns,
        how="inner",
        suffixes=("_base", "_delayed"),
        validate="one_to_one",
    )
    rows: list[dict[str, object]] = []
    for pair in paired.itertuples(index=False):
        for column in common_columns[4:]:
            left = getattr(pair, f"{column}_base")
            right = getattr(pair, f"{column}_delayed")
            if str(left) != str(right):
                raise RuntimeError(f"low/mid falling paired source drift: {column}")
        rows.append(
            {
                "generated_at": str(detail["generated_at"].iloc[0]),
                "model_id": MODEL_ID,
                "artifact_id": ARTIFACT_ID,
                "artifact_version": ARTIFACT_VERSION,
                **_artifact_lineage(detail),
                "source_variant_id": SOURCE_VARIANT_ID,
                **{column: getattr(pair, column) for column in key_columns},
                **{
                    column: getattr(pair, f"{column}_base")
                    for column in common_columns[4:]
                },
                "base_confirmation_date": pair.confirmation_date_base,
                "base_entry_date": pair.entry_date_base,
                "base_exit_date": pair.exit_date_base,
                "base_realized_return_pct": round(
                    float(pair.realized_return_pct_base), 4
                ),
                "base_rearmed_operation_canonical_row_sha256": (
                    pair.rearmed_operation_canonical_row_sha256_base
                ),
                "base_candidate_detail_row_sha256": (
                    pair.candidate_detail_row_sha256_base
                ),
                "delayed_confirmation_date": pair.confirmation_date_delayed,
                "delayed_entry_date": pair.entry_date_delayed,
                "delayed_exit_date": pair.exit_date_delayed,
                "delayed_realized_return_pct": round(
                    float(pair.realized_return_pct_delayed), 4
                ),
                "delayed_rearmed_operation_canonical_row_sha256": (
                    pair.rearmed_operation_canonical_row_sha256_delayed
                ),
                "delayed_candidate_detail_row_sha256": (
                    pair.candidate_detail_row_sha256_delayed
                ),
                "delayed_minus_base_return_pct_points": round(
                    float(pair.realized_return_pct_delayed)
                    - float(pair.realized_return_pct_base),
                    4,
                ),
                "base_operation_return_review_candidate_flag": _bool_value(
                    pair.operation_return_review_candidate_flag_base
                ),
                "delayed_operation_return_review_candidate_flag": _bool_value(
                    pair.operation_return_review_candidate_flag_delayed
                ),
                "paired_combined_exclusion_candidate_flag": bool(
                    _bool_value(pair.combined_exclusion_candidate_flag_base)
                    or _bool_value(pair.combined_exclusion_candidate_flag_delayed)
                ),
                "paired_sensitivity_included": not bool(
                    _bool_value(pair.combined_exclusion_candidate_flag_base)
                    or _bool_value(pair.combined_exclusion_candidate_flag_delayed)
                ),
                "paired_comparison_role": (
                    "same_trigger_distinct_information_cutoff_not_independent_operations"
                ),
                "financial_statement_scope": FINANCIAL_STATEMENT_SCOPE,
                "approved_for_daily": False,
                "presentation_allowed": False,
                "formal_model_use_allowed": False,
                "production_change": False,
                "promotion_readiness": "research_only_pending_holdout_validation",
            }
        )
    return pd.DataFrame(rows)


def _standardized_mean_difference(left: pd.Series, right: pd.Series) -> float | str:
    a = pd.to_numeric(left, errors="coerce").dropna()
    b = pd.to_numeric(right, errors="coerce").dropna()
    if len(a) < 2 or len(b) < 2:
        return ""
    denominator = len(a) + len(b) - 2
    variance = ((len(a) - 1) * a.var(ddof=1) + (len(b) - 1) * b.var(ddof=1)) / denominator
    if not np.isfinite(variance) or variance <= 0:
        return ""
    return round(float((a.mean() - b.mean()) / math.sqrt(variance)), 4)


def _build_feature_contrast(detail: pd.DataFrame) -> pd.DataFrame:
    rows: list[dict[str, object]] = []
    for analysis_basis in ANALYSIS_BASES:
        basis = (
            detail
            if analysis_basis == PRIMARY_ANALYSIS_BASIS
            else detail.loc[_boolish(detail["sensitivity_included"])]
        )
        for lifecycle_id in LIFECYCLE_POLICY_IDS:
            for confirmation_id in CONFIRMATION_VARIANT_IDS:
                grid = basis.loc[
                    basis["lifecycle_policy_id"].eq(lifecycle_id)
                    & basis["confirmation_variant_id"].eq(confirmation_id)
                ]
                for variant_order, variant_id, member_column in VARIANT_SPECS:
                    part = grid.loc[_boolish(grid[member_column])]
                    returns = pd.to_numeric(part["realized_return_pct"], errors="coerce")
                    high = part.loc[returns.ge(20.0)]
                    low = part.loc[returns.le(0.0)]
                    for feature_order, feature_id in FEATURE_SPECS:
                        high_values = pd.to_numeric(high[feature_id], errors="coerce").dropna()
                        low_values = pd.to_numeric(low[feature_id], errors="coerce").dropna()
                        high_mean = _metric(high_values, "mean")
                        low_mean = _metric(low_values, "mean")
                        rows.append(
                            {
                                "generated_at": str(detail["generated_at"].iloc[0]),
                                "model_id": MODEL_ID,
                                "artifact_id": ARTIFACT_ID,
                                "artifact_version": ARTIFACT_VERSION,
                                **_artifact_lineage(detail),
                                "source_variant_id": SOURCE_VARIANT_ID,
                                "analysis_basis": analysis_basis,
                                "lifecycle_policy_id": lifecycle_id,
                                "confirmation_variant_id": confirmation_id,
                                "candidate_variant_order": variant_order,
                                "candidate_variant_id": variant_id,
                                "feature_order": feature_order,
                                "feature_id": feature_id,
                                "high_return_definition": "realized_return_pct>=20",
                                "low_return_definition": "realized_return_pct<=0",
                                "high_return_operation_count": len(high),
                                "low_return_operation_count": len(low),
                                "high_observed_count": len(high_values),
                                "low_observed_count": len(low_values),
                                "high_mean": high_mean,
                                "high_median": _metric(high_values, "median"),
                                "low_mean": low_mean,
                                "low_median": _metric(low_values, "median"),
                                "high_minus_low_mean": (
                                    round(float(high_mean) - float(low_mean), 4)
                                    if high_mean != "" and low_mean != ""
                                    else ""
                                ),
                                "standardized_mean_difference": (
                                    _standardized_mean_difference(high_values, low_values)
                                ),
                                "contrast_scope": (
                                    "descriptive_same_operation_contract_not_promotion_evidence"
                                ),
                                "sample_policy": SAMPLE_POLICY,
                                "anomaly_policy": ANOMALY_POLICY,
                                "financial_statement_scope": FINANCIAL_STATEMENT_SCOPE,
                                "approved_for_daily": False,
                                "presentation_allowed": False,
                                "formal_model_use_allowed": False,
                                "production_change": False,
                                "promotion_readiness": (
                                    "research_only_pending_holdout_validation"
                                ),
                            }
                        )
    return pd.DataFrame(rows).sort_values(
        [
            "analysis_basis",
            "lifecycle_policy_id",
            "confirmation_variant_id",
            "candidate_variant_order",
            "feature_order",
        ],
        kind="mergesort",
    ).reset_index(drop=True)


def build_low_mid_falling_candidate_audit(
    source_first_detail: pd.DataFrame,
    rearmed_detail: pd.DataFrame,
    daily_by_stock: Mapping[str, pd.DataFrame],
    *,
    generated_at: str | None = None,
    data_contract_sha256: str | None = None,
) -> tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    _assert_literal_upstream_contracts()
    contract_sha = _require_sha256(
        data_contract_sha256 or DATA_CONTRACT_SHA256,
        label="data contract SHA-256",
    )
    if contract_sha != DATA_CONTRACT_SHA256:
        raise RuntimeError(
            "low/mid falling data contract SHA-256 drift: "
            f"{contract_sha}/{DATA_CONTRACT_SHA256}"
        )
    producer_sha = _require_sha256(
        _normalized_file_sha256(__file__), label="producer semantic SHA-256"
    )
    source_first_producer_sha = _require_sha256(
        _normalized_file_sha256(source_first_producer.__file__),
        label="source-first producer semantic SHA-256",
    )
    rearmed_producer_sha = _require_sha256(
        _normalized_file_sha256(rearmed_producer.__file__),
        label="rearmed producer semantic SHA-256",
    )
    position_shape_producer_sha = _require_sha256(
        _normalized_file_sha256(position_shape_producer.__file__),
        label="position-shape producer semantic SHA-256",
    )
    rearmed_versions = set(rearmed_detail["artifact_version"].astype(str).str.strip())
    if len(rearmed_versions) != 1:
        raise RuntimeError(
            "rearmed artifact version drift: "
            "low/mid falling rearmed artifact version is not constant"
        )
    rearmed_artifact_version = next(iter(rearmed_versions))
    (
        selected_artifact_version,
        expected_position_shape_artifact_version,
        expected_source_projection_artifact_version,
    ) = versions_for_rearmed_artifact(rearmed_artifact_version)
    v3_provenance_excluded_hashes = (
        selected_artifact_version == V3_ARTIFACT_VERSION
    )
    source = _normalize_source(
        source_first_detail,
        provenance_excluded_hashes=v3_provenance_excluded_hashes,
    )
    operations = _normalize_operations(
        rearmed_detail,
        expected_artifact_version=rearmed_artifact_version,
        provenance_excluded_hashes=v3_provenance_excluded_hashes,
    )
    v3_detail_versions = (
        {
            "artifact_version": selected_artifact_version,
            "rearmed_artifact_version": rearmed_artifact_version,
        }
        if selected_artifact_version == V3_ARTIFACT_VERSION
        else {}
    )
    detail = _build_detail(
        source,
        operations,
        daily_by_stock,
        generated_at or _now_text(),
        producer_semantic_sha256=producer_sha,
        source_first_producer_semantic_sha256=source_first_producer_sha,
        rearmed_producer_semantic_sha256=rearmed_producer_sha,
        position_shape_producer_semantic_sha256=position_shape_producer_sha,
        data_contract_sha256=contract_sha,
        **v3_detail_versions,
    )
    summary = _build_summary(detail)
    paired = _build_paired_confirmation(detail)
    contrast = _build_feature_contrast(detail)
    for frame in (summary, detail, paired, contrast):
        frame.loc[:, "artifact_version"] = selected_artifact_version
        if "rearmed_artifact_version" in frame.columns:
            frame.loc[:, "rearmed_artifact_version"] = rearmed_artifact_version
        if "position_shape_artifact_version" in frame.columns:
            frame.loc[:, "position_shape_artifact_version"] = (
                expected_position_shape_artifact_version
            )
        if "source_projection_artifact_version" in frame.columns:
            frame.loc[:, "source_projection_artifact_version"] = (
                expected_source_projection_artifact_version
            )
    return summary, detail, paired, contrast


def resolve_output_paths(
    *,
    output_root: Path | str = ROOT,
    output_paths: Mapping[str, Path | str] | None = None,
) -> dict[str, Path]:
    root = Path(output_root)
    resolved = {
        key: root / relative for key, relative in DEFAULT_OUTPUT_RELATIVE_PATHS.items()
    }
    if output_paths:
        unknown = sorted(set(output_paths) - set(resolved))
        if unknown:
            raise ValueError(f"unknown low/mid falling output path keys: {unknown}")
        for key, path in output_paths.items():
            resolved[key] = Path(path)
    return resolved


def _markdown_table(frame: pd.DataFrame, columns: list[str]) -> str:
    if frame.empty:
        return "_No rows._"
    view = frame.loc[:, columns].astype(str)
    lines = [
        "| " + " | ".join(columns) + " |",
        "| " + " | ".join(["---"] * len(columns)) + " |",
    ]
    for record in view.itertuples(index=False, name=None):
        lines.append("| " + " | ".join(value.replace("|", "/") for value in record) + " |")
    return "\n".join(lines)


def _markdown(summary: pd.DataFrame, paired: pd.DataFrame) -> str:
    primary = summary.loc[summary["analysis_basis"].eq(PRIMARY_ANALYSIS_BASIS)]
    return "\n".join(
        [
            "# 營收改善但股價尚未反應：低／中位下降型態候選稽核",
            "",
            f"- generated_at: `{summary['generated_at'].iloc[0]}`",
            f"- artifact_version: `{summary['artifact_version'].iloc[0]}`",
            "- 狀態：`research_only`；不是正式 gate、ranking、operation adapter、PDF 或 promotion evidence。",
            "- 月營收與季／年財報分離；EPS、毛利率、營益率、營業利益、業外與淨利全部排除。",
            "- 來源錨點使用 trigger 當下最後一筆已知 qualifying revenue，觀察期限固定 0～60 交易日。",
            "- D+1 與 continuation-confirmed D+2 採不同 information cutoff；paired rows 不是獨立樣本。",
            "- Primary 保留 anomaly candidates；候選排除僅是 sensitivity。",
            "",
            "## Primary 候選矩陣",
            "",
            _markdown_table(
                primary,
                [
                    "lifecycle_policy_id",
                    "confirmation_variant_id",
                    "candidate_variant_id",
                    "operation_count",
                    "unique_stock_count",
                    "unique_episode_count",
                    "win_rate_pct",
                    "avg_return_pct",
                    "median_return_pct",
                    "p10_return_pct",
                    "p90_return_pct",
                    "return_ge20_rate_pct",
                    "return_le_minus20_rate_pct",
                ],
            ),
            "",
            f"- paired_confirmation_rows: `{len(paired)}`",
            "",
        ]
    )


def write_low_mid_falling_candidate_audit(
    summary: pd.DataFrame,
    detail: pd.DataFrame,
    paired: pd.DataFrame,
    contrast: pd.DataFrame,
    *,
    output_root: Path | str = ROOT,
    output_paths: Mapping[str, Path | str] | None = None,
) -> dict[str, Path]:
    paths = resolve_output_paths(output_root=output_root, output_paths=output_paths)
    for path in paths.values():
        path.parent.mkdir(parents=True, exist_ok=True)
    frames = {
        "summary": summary,
        "detail": detail,
        "paired": paired,
        "contrast": contrast,
    }
    for family, frame in frames.items():
        latest = paths[f"{family}_latest"]
        frame.to_csv(latest, index=False, encoding="utf-8-sig", lineterminator="\n")
        paths[f"{family}_history"].write_bytes(latest.read_bytes())
        paths[f"{family}_docs"].write_bytes(latest.read_bytes())
    markdown = _markdown(summary, paired)
    paths["markdown_latest"].write_text(markdown, encoding="utf-8", newline="\n")
    paths["markdown_docs"].write_bytes(paths["markdown_latest"].read_bytes())
    return paths


if __name__ == "__main__":
    raise SystemExit(
        "Use scripts/build_revenue_unreacted_range_research.py with the model-owned "
        "low/mid falling candidate audit stage"
    )
