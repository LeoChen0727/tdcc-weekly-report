from __future__ import annotations

"""Formal revenue_unreacted_range/source_mid_falling v2 operation producer.

Runtime inputs are limited to objective monthly-revenue history, per-stock price
history, and repository taxonomy configuration. Candidate signals, research
outputs, readiness artifacts, and mutable latest artifacts are never inputs.
"""

import argparse
import csv
from datetime import datetime
import hashlib
import io
import json
import math
import os
from pathlib import Path
import re
from typing import Any, Iterable, Mapping, Sequence
from zoneinfo import ZoneInfo

import pandas as pd


ROOT = Path(__file__).resolve().parents[1]
MONTHLY_REVENUE_HISTORY_CSV = (
    ROOT / "data" / "monthly_revenue_history" / "monthly_revenue_history.csv"
)
STOCK_PRICE_HISTORY_DIR = ROOT / "data" / "stock_price_history"
TAXONOMY_PATHS = (
    ROOT / "config" / "stock_theme_map.csv",
    ROOT / "config" / "stock_theme_taxonomy_manual.csv",
    ROOT / "config" / "stock_theme_authorized_seed.csv",
)

OUT_CSV = (
    ROOT
    / "output"
    / "latest"
    / "daily_revenue_unreacted_range_operation_section_latest.csv"
)
OUT_MD = (
    ROOT
    / "output"
    / "latest"
    / "daily_revenue_unreacted_range_operation_section_latest.md"
)
DOCS_LATEST_DIR = ROOT / "docs" / "latest"
HISTORY_DIR = ROOT / "output" / "history" / "daily_model_snapshots"

MODEL_ID = "revenue_unreacted_range"
MODEL_NAME_ZH = "營收爆發但股價尚未反應模型"
MODEL_VARIANT_ID = "source_mid_falling"
MODEL_VARIANT_VERSION = "v2"
OPERATION_MODULE_ID = "revenue_unreacted_range_source_mid_falling_v2_operation_v2"
ADAPTER_SCHEMA_VERSION = "revenue_unreacted_range_operation_section_schema_v2"
LIFECYCLE_CONTRACT_VERSION = "revenue_unreacted_range_lifecycle_v2"
ADAPTER_MODE = "formal_production"
APPROVAL_VERSION = (
    "revenue_unreacted_range_source_mid_falling_formal_operation_v2_20260830"
)
APPROVAL_STATUS = "provisional_backtest_supported_oos_unconfirmed"
FORMAL_SIGNAL_EFFECTIVE_FROM = "20260831"
RULE_SPEC_ID = "revenue_unreacted_range_source_mid_falling_d30_v1"
RULE_CANONICAL_SHA256 = (
    "1d9fd669251180d2f7edbedb30b121660a218bad232ca49573353000db155633"
)
SELECTION_POLICY = "fixed_preselected_no_reselection"
HOLDOUT_USE_POLICY = "post_launch_monitoring_non_hard_no_tuning"
OPERATION_DIRECTIVE_LEVEL = "approved_daily_operation_guidance"

BASELINE_PERFORMANCE_STATUS = (
    "provisional_gross_historical_header_disclosure_only"
)
BASELINE_PERFORMANCE_SCOPE = (
    "whole_model_gross_historical_d2_open_to_d30_close"
)
BASELINE_PERFORMANCE_SOURCE = (
    "config/approved_operation_evidence/"
    "revenue_unreacted_range_source_mid_falling_"
    "frozen_rule_launch_evidence_v1_20260830_manifest.csv"
)
BASELINE_SAMPLE_SIZE = 53
BASELINE_WIN_RATE_PCT = 77.3585
BASELINE_NEUTRAL_RATE_PCT = 0.0
BASELINE_FAILURE_RATE_PCT = 22.6415
BASELINE_AVG_RETURN_PCT = 14.8950
BASELINE_MEDIAN_RETURN_PCT = 9.4077

CONFIRMATION_RULE_ID = "d1_analysis_close_above_trigger_analysis_close"
ENTRY_RULE_ID = "d2_analysis_open"
EXIT_RULE_ID = "d30_analysis_close_offset29"
STOP_POLICY_ID = "none_no_stop_reference"
CONFIRMATION_OFFSET_TRADING_DAYS = 1
ENTRY_OFFSET_TRADING_DAYS = 2
HOLDING_DAYS = 30
HOLDING_SESSION_INDEX_OFFSET = 29
ENTRY_PRICE_BASIS = "analysis_open"
EXIT_PRICE_BASIS = "analysis_close"
PRICE_CONFIRMATION_BASIS = "analysis_close_only"
SAME_STOCK_NON_OVERLAP_POLICY = (
    "entry_after_prior_realized_exit_next_trading_day"
)
FINANCIAL_STATEMENT_SCOPE = (
    "monthly_revenue_only_EPS_gross_margin_operating_margin_operating_income_"
    "non_operating_income_net_income_excluded"
)

ABSOLUTE_LATEST_YOY_MIN_PCT = 30.0
ABSOLUTE_CUMULATIVE_YOY_MIN_PCT = 20.0
TWO_MONTH_YOY_MIN_PCT = 15.0
SOURCE_TO_TRIGGER_MAX_TRADING_DAYS = 60
POSITION_LOOKBACK_PRIOR_SESSIONS = 120
POSITION_LOW_MAX_PCT = 40.0
POSITION_MID_MAX_PCT = 75.0
SHAPE_RETURN_LOOKBACK_SESSIONS = 20
SHAPE_EMA_SPAN_SESSIONS = 23
SHAPE_EMA_SLOPE_LOOKBACK_SESSIONS = 5
SHAPE_FALLING_RETURN_MAX_PCT = -5.0
SHAPE_FALLING_EMA_SLOPE_MAX_PCT = 0.0
TRIGGER_PREVIOUS_CLOSE_WINDOW_SESSIONS = 20
TRIGGER_MA_SHORT_SESSIONS = 60
TRIGGER_MA_LONG_SESSIONS = 120

REPORT_LINES = ("mainstream", "non_mainstream")
PDF_VIEWS = ("highlight", "full")
PDF_SECTIONS = (
    "confirmed_operation",
    "confirmed_unranked_operation",
    "pending_confirmation",
    "active_operation",
)
HIGHLIGHT_HIDDEN_SECTIONS = {
    "confirmed_unranked_operation",
    "pending_confirmation",
}
SECTION_ZH = {
    "confirmed_operation": "本日可買 / 已確認買入候選",
    "confirmed_unranked_operation": "已確認但未列買入",
    "pending_confirmation": "待確認",
    "active_operation": "操作中",
}
SECTION_EMPTY_TEXT_ZH = {
    "confirmed_operation": "本日無股票推薦",
    "confirmed_unranked_operation": "目前無已確認但未列入買進排序列",
    "pending_confirmation": "目前無待確認列",
    "active_operation": "目前無操作中追蹤列",
}
STATE_ZH = {
    "pending_confirmation": "待確認",
    "confirmed_operation": "已確認買入候選",
    "active_operation": "操作中",
}
ROW_ACTION_STATUS = {
    "pending_confirmation": "pending_confirmation",
    "confirmed_operation": "confirmed_buy_candidate",
    "confirmed_unranked_operation": "confirmed_not_buy_ranked",
    "active_operation": "active_operation",
}
QUALITY_ZH = {
    "pending_confirmation": "等待 close-only 確認",
    "confirmed_operation": "正向證據",
    "active_operation": "正式操作中",
    "empty_state": "empty_state",
}

FORBIDDEN_FINANCIAL_STATEMENT_FIELDS = frozenset(
    {
        "eps",
        "gross_margin",
        "operating_margin",
        "operating_income",
        "non_operating_income",
        "net_income",
        "quarterly_financial_statement",
        "annual_financial_statement",
    }
)
FORBIDDEN_RUNTIME_INPUT_PARTS = (
    ("output", "latest"),
    ("docs", "latest"),
    ("research_backtest",),
)

OUTPUT_COLUMNS = (
    "model_id",
    "model_name_zh",
    "model_variant_id",
    "model_variant_version",
    "operation_module_id",
    "adapter_schema_version",
    "lifecycle_contract_version",
    "adapter_mode",
    "approval_version",
    "approval_status",
    "formal_signal_effective_from",
    "rule_spec_id",
    "rule_canonical_sha256",
    "selection_policy",
    "holdout_use_policy",
    "pdf_view",
    "pdf_section",
    "pdf_section_zh",
    "row_type",
    "empty_text_zh",
    "operation_asof_date",
    "operation_source_date_status",
    "report_line",
    "report_line_memberships",
    "display_order",
    "operation_key",
    "stock_id",
    "stock_name",
    "stock_display",
    "rank_reason_zh",
    "risk_tags_zh",
    "taxonomy_status",
    "theme_mainstream_label",
    "primary_theme",
    "industry",
    "lifecycle_state",
    "operation_status",
    "operation_status_zh",
    "operation_quality",
    "operation_quality_zh",
    "row_action_status",
    "buy_rank_eligible",
    "sample_size",
    "win_rate_zh",
    "neutral_rate_zh",
    "failure_rate_zh",
    "avg_return_zh",
    "median_return_zh",
    "baseline_performance_status",
    "baseline_performance_scope",
    "baseline_performance_source",
    "row_metric_status",
    "row_metric_scope",
    "row_metric_id",
    "row_metric_label_zh",
    "row_metric_matched_add_score_ids",
    "row_metric_sample_size",
    "row_metric_win_rate_zh",
    "row_metric_neutral_rate_zh",
    "row_metric_failure_rate_zh",
    "row_metric_avg_return_zh",
    "row_metric_median_return_zh",
    "row_metric_source",
    "row_metric_selection_status",
    "operation_directive_level",
    "formal_model_use_allowed",
    "approved_for_daily",
    "presentation_allowed",
    "production_allowed",
    "source_revenue_period",
    "source_table_date",
    "source_trade_date",
    "source_sequence_index",
    "source_to_trigger_trading_days",
    "source_position_120d_pct",
    "source_shape_return20_pct",
    "source_shape_ema23_slope5_pct",
    "signal_date",
    "signal_sequence_index",
    "signal_close",
    "confirmation_date",
    "confirmation_sequence_index",
    "confirmation_close",
    "entry_date",
    "entry_sequence_index",
    "entry_price",
    "entry_basis_zh",
    "entry_price_status_zh",
    "stop_loss_rule_id",
    "stop_loss_price",
    "stop_loss_label_zh",
    "stop_basis_zh",
    "planned_exit_sequence_index",
    "exit_date",
    "exit_price",
    "exit_rule_zh",
    "confirmation_rule_id",
    "entry_rule_id",
    "exit_rule_id",
    "stop_policy_id",
    "confirmation_offset_trading_days",
    "entry_offset_trading_days",
    "holding_days",
    "planned_holding_days",
    "operation_age_days",
    "holding_session_index_offset",
    "entry_price_basis",
    "exit_price_basis",
    "price_confirmation_basis",
    "same_stock_non_overlap_policy",
    "financial_statement_scope",
    "source_revenue_anomaly_candidate_flag",
    "source_artifacts",
    "monthly_revenue_source_row_sha256",
    "price_source_sha256",
    "taxonomy_source_row_sha256",
    "confirmed_history_artifact",
    "confirmed_history_row_sha256",
    "lifecycle_replay_sha256",
    "adapter_source_status",
    "adapter_note_zh",
    "generated_at",
    "row_canonical_sha256",
)


class RevenueOperationAdapterError(RuntimeError):
    """An objective input or formal lifecycle contract is invalid."""


def now_taipei_text() -> str:
    return datetime.now(ZoneInfo("Asia/Taipei")).strftime(
        "%Y-%m-%d %H:%M:%S Asia/Taipei"
    )


def _text(value: Any) -> str:
    if value is None or (not isinstance(value, str) and pd.isna(value)):
        return ""
    return str(value).strip()


def _stock_id(value: Any) -> str:
    token = re.sub(r"\.0$", "", _text(value))
    if not re.fullmatch(r"[0-9A-Za-z]{2,8}", token):
        raise RevenueOperationAdapterError(f"invalid stock_id={value!r}")
    return token


def _date_text(value: Any, *, label: str) -> str:
    token = re.sub(r"[^0-9]", "", _text(value))
    if len(token) != 8:
        raise RevenueOperationAdapterError(
            f"{label} is not YYYYMMDD: {value!r}"
        )
    parsed = pd.to_datetime(token, format="%Y%m%d", errors="coerce")
    if pd.isna(parsed):
        raise RevenueOperationAdapterError(f"{label} is invalid: {value!r}")
    return token


def _period_text(value: Any) -> str:
    token = re.sub(r"[^0-9]", "", _text(value))
    if (
        not re.fullmatch(r"[0-9]{6}", token)
        or not 1 <= int(token[-2:]) <= 12
    ):
        raise RevenueOperationAdapterError(f"invalid revenue_period={value!r}")
    return token


def _period_ordinal(period: str) -> int:
    return int(period[:4]) * 12 + int(period[-2:]) - 1


def _number(value: Any) -> float:
    token = _text(value).replace(",", "")
    if token in {"", "-", "--", "nan", "None"}:
        return math.nan
    try:
        return float(token)
    except ValueError:
        return math.nan


def _strict_bool(value: Any, *, label: str) -> bool:
    token = _text(value).lower()
    if token in {"true", "1", "yes", "y"}:
        return True
    if token in {"false", "0", "no", "n", ""}:
        return False
    raise RevenueOperationAdapterError(
        f"{label} is not canonical boolean text: {value!r}"
    )


def _canonical_value(value: Any) -> str:
    if value is None or (not isinstance(value, str) and pd.isna(value)):
        return ""
    if isinstance(value, bool):
        return "True" if value else "False"
    if isinstance(value, int):
        return str(value)
    if isinstance(value, float):
        if not math.isfinite(value):
            return ""
        return format(value, ".15g")
    return str(value).strip()


def _mapping_sha256(
    mapping: Mapping[str, Any], columns: Sequence[str]
) -> str:
    payload = [
        [column, _canonical_value(mapping.get(column, ""))]
        for column in columns
    ]
    return hashlib.sha256(
        json.dumps(
            payload, ensure_ascii=False, separators=(",", ":")
        ).encode("utf-8")
    ).hexdigest()


def _file_sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def _display_path(path: Path) -> str:
    resolved = path.resolve()
    try:
        return resolved.relative_to(ROOT).as_posix()
    except ValueError:
        return resolved.as_posix()


def _assert_objective_input_path(path: Path, *, label: str) -> None:
    parts = tuple(part.lower() for part in path.resolve().parts)
    for forbidden in FORBIDDEN_RUNTIME_INPUT_PARTS:
        width = len(forbidden)
        if any(
            parts[index : index + width] == forbidden
            for index in range(len(parts) - width + 1)
        ):
            raise RevenueOperationAdapterError(
                f"{label} must not consume latest/research artifacts: "
                f"{_display_path(path)}"
            )


def _read_objective_csv(path: Path, *, label: str) -> pd.DataFrame:
    _assert_objective_input_path(path, label=label)
    if not path.is_file():
        raise RevenueOperationAdapterError(f"{label} is missing: {path}")
    frame = pd.read_csv(
        path,
        dtype=str,
        keep_default_na=False,
        encoding="utf-8-sig",
    )
    frame.columns = [
        str(column).lstrip("\ufeff").strip() for column in frame.columns
    ]
    return frame


def load_monthly_revenue_history(
    path: Path = MONTHLY_REVENUE_HISTORY_CSV,
) -> pd.DataFrame:
    frame = _read_objective_csv(path, label="monthly revenue history")
    forbidden = sorted(
        {column.lower() for column in frame.columns}
        & FORBIDDEN_FINANCIAL_STATEMENT_FIELDS
    )
    if forbidden:
        raise RevenueOperationAdapterError(
            "monthly-revenue-only boundary forbids financial-statement "
            f"fields: {forbidden}"
        )
    required = {
        "stock_id",
        "stock_name",
        "revenue_period",
        "source_table_date",
        "latest_revenue_yoy_pct",
        "cumulative_revenue_yoy_pct",
        "point_in_time_status",
    }
    missing = sorted(required - set(frame.columns))
    if missing:
        raise RevenueOperationAdapterError(
            f"monthly revenue history missing columns: {missing}"
        )

    ready = frame[
        frame["point_in_time_status"].astype(str).str.startswith("ready_")
    ].copy()
    if "research_join_allowed" in ready.columns:
        ready = ready[
            ready["research_join_allowed"].map(
                lambda value: _strict_bool(
                    value, label="research_join_allowed"
                )
            )
        ].copy()
    empty_columns = [
        "stock_id",
        "stock_name",
        "revenue_period",
        "source_table_date",
        "latest_revenue_yoy_pct",
        "cumulative_revenue_yoy_pct",
        "source_revenue_anomaly_candidate_flag",
        "monthly_revenue_source_row_sha256",
    ]
    if ready.empty:
        return pd.DataFrame(columns=empty_columns)

    ready["stock_id"] = ready["stock_id"].map(_stock_id)
    ready["revenue_period"] = ready["revenue_period"].map(_period_text)
    ready["source_table_date"] = ready["source_table_date"].map(
        lambda value: _date_text(value, label="source_table_date")
    )
    ready["latest_revenue_yoy_pct"] = ready[
        "latest_revenue_yoy_pct"
    ].map(_number)
    ready["cumulative_revenue_yoy_pct"] = ready[
        "cumulative_revenue_yoy_pct"
    ].map(_number)
    anomaly_column = (
        "revenue_numerical_anomaly_flag"
        if "revenue_numerical_anomaly_flag" in ready.columns
        else None
    )
    ready["source_revenue_anomaly_candidate_flag"] = (
        ready[anomaly_column].map(
            lambda value: _strict_bool(
                value, label="revenue_numerical_anomaly_flag"
            )
        )
        if anomaly_column
        else False
    )

    selected_rows: list[pd.Series] = []
    for (stock_id, period), group in ready.groupby(
        ["stock_id", "revenue_period"], sort=False, dropna=False
    ):
        comparisons = {
            (
                _canonical_value(row["latest_revenue_yoy_pct"]),
                _canonical_value(row["cumulative_revenue_yoy_pct"]),
            )
            for _, row in group.iterrows()
        }
        if len(comparisons) != 1:
            raise RevenueOperationAdapterError(
                "conflicting monthly revenue rows for stock/period: "
                f"{stock_id}/{period}"
            )
        selected_rows.append(
            group.sort_values(
                ["source_table_date", "stock_name"], kind="mergesort"
            ).iloc[0]
        )
    normalized = pd.DataFrame(selected_rows).sort_values(
        ["stock_id", "revenue_period", "source_table_date"],
        kind="mergesort",
    )

    qualifying_rows: list[dict[str, Any]] = []
    hash_columns = (
        "stock_id",
        "stock_name",
        "revenue_period",
        "source_table_date",
        "latest_revenue_yoy_pct",
        "cumulative_revenue_yoy_pct",
        "source_revenue_anomaly_candidate_flag",
    )
    for stock_id, group in normalized.groupby("stock_id", sort=True):
        previous: Mapping[str, Any] | None = None
        for _, row in group.iterrows():
            latest_yoy = float(row["latest_revenue_yoy_pct"])
            cumulative_yoy = float(row["cumulative_revenue_yoy_pct"])
            absolute_branch = (
                math.isfinite(latest_yoy)
                and latest_yoy >= ABSOLUTE_LATEST_YOY_MIN_PCT
            ) or (
                math.isfinite(cumulative_yoy)
                and cumulative_yoy >= ABSOLUTE_CUMULATIVE_YOY_MIN_PCT
            )
            consecutive_branch = False
            if previous is not None:
                previous_latest = float(
                    previous["latest_revenue_yoy_pct"]
                )
                consecutive_branch = bool(
                    _period_ordinal(str(row["revenue_period"]))
                    - _period_ordinal(str(previous["revenue_period"]))
                    == 1
                    and math.isfinite(latest_yoy)
                    and math.isfinite(previous_latest)
                    and latest_yoy >= TWO_MONTH_YOY_MIN_PCT
                    and previous_latest >= TWO_MONTH_YOY_MIN_PCT
                )
            payload: dict[str, Any] = {
                "stock_id": stock_id,
                "stock_name": _text(row["stock_name"]),
                "revenue_period": str(row["revenue_period"]),
                "source_table_date": str(row["source_table_date"]),
                "latest_revenue_yoy_pct": latest_yoy,
                "cumulative_revenue_yoy_pct": cumulative_yoy,
                "source_revenue_anomaly_candidate_flag": bool(
                    row["source_revenue_anomaly_candidate_flag"]
                ),
            }
            if absolute_branch or consecutive_branch:
                payload["monthly_revenue_source_row_sha256"] = (
                    _mapping_sha256(payload, hash_columns)
                )
                qualifying_rows.append(payload)
            previous = payload
    return pd.DataFrame(qualifying_rows, columns=empty_columns)


def load_taxonomy(
    paths: Sequence[Path] = TAXONOMY_PATHS,
) -> dict[str, dict[str, str]]:
    resolved: dict[str, dict[str, str]] = {}
    contributing: dict[str, list[str]] = {}
    for path in paths:
        frame = _read_objective_csv(path, label="stock taxonomy")
        stock_column = (
            "stock_id"
            if "stock_id" in frame.columns
            else "code"
            if "code" in frame.columns
            else ""
        )
        if not stock_column:
            raise RevenueOperationAdapterError(
                f"stock taxonomy lacks stock_id/code: {path}"
            )
        seen_in_file: set[str] = set()
        for _, source_row in frame.iterrows():
            stock_id = _stock_id(source_row[stock_column])
            if stock_id in seen_in_file:
                raise RevenueOperationAdapterError(
                    "stock taxonomy repeats stock_id in one file: "
                    f"{path}/{stock_id}"
                )
            seen_in_file.add(stock_id)
            current = dict(resolved.get(stock_id, {}))
            aliases = {
                "stock_name": ("stock_name", "name"),
                "theme_mainstream_label": ("theme_mainstream_label",),
                "primary_theme": ("primary_theme",),
                "industry": ("industry",),
            }
            for target, candidates in aliases.items():
                value = next(
                    (
                        _text(source_row[column])
                        for column in candidates
                        if column in frame.columns
                        and _text(source_row[column])
                    ),
                    "",
                )
                if value:
                    current[target] = value
            resolved[stock_id] = current
            contributing.setdefault(stock_id, []).append(
                _display_path(path)
            )
    for stock_id, row in resolved.items():
        row.setdefault("stock_name", "")
        row.setdefault("theme_mainstream_label", "")
        row.setdefault("primary_theme", "")
        row.setdefault("industry", "")
        row["taxonomy_status"] = (
            "mapped"
            if row["theme_mainstream_label"]
            or row["primary_theme"]
            or row["industry"]
            else "taxonomy_incomplete_fail_closed_non_mainstream"
        )
        row["taxonomy_source_artifacts"] = ";".join(
            contributing.get(stock_id, ())
        )
        row["taxonomy_source_row_sha256"] = _mapping_sha256(
            {"stock_id": stock_id, **row},
            (
                "stock_id",
                "stock_name",
                "theme_mainstream_label",
                "primary_theme",
                "industry",
                "taxonomy_source_artifacts",
            ),
        )
    return resolved


def _report_line(taxonomy: Mapping[str, str]) -> str:
    label = _text(taxonomy.get("theme_mainstream_label")).lower()
    return (
        "mainstream"
        if label in {"core_mainstream", "mainstream"}
        else "non_mainstream"
    )


def _price_file_map(directory: Path) -> dict[str, Path]:
    _assert_objective_input_path(
        directory, label="stock price history directory"
    )
    if not directory.is_dir():
        raise RevenueOperationAdapterError(
            f"stock price history directory is missing: {directory}"
        )
    result: dict[str, Path] = {}
    for path in sorted(directory.glob("*.csv")):
        stock_id = _stock_id(path.stem)
        if stock_id in result:
            raise RevenueOperationAdapterError(
                f"duplicate normalized price file: {stock_id}"
            )
        result[stock_id] = path
    return result


def load_price_history(path: Path) -> pd.DataFrame:
    frame = _read_objective_csv(path, label="stock price history")
    required = {"date", "open", "high", "low", "close"}
    missing = sorted(required - set(frame.columns))
    if missing:
        raise RevenueOperationAdapterError(
            f"stock price history missing columns: {path}/{missing}"
        )
    normalized = pd.DataFrame()
    normalized["date"] = frame["date"].map(
        lambda value: _date_text(
            value, label=f"{path.name}/date"
        )
    )
    if normalized["date"].duplicated().any():
        raise RevenueOperationAdapterError(
            f"stock price history has duplicate dates: {path}"
        )
    for column in ("open", "high", "low", "close"):
        normalized[f"analysis_{column}"] = pd.to_numeric(
            frame[column].astype(str).str.replace(",", "", regex=False),
            errors="coerce",
        )
    ohlc = [
        "analysis_open",
        "analysis_high",
        "analysis_low",
        "analysis_close",
    ]
    if normalized[ohlc].isna().any().any():
        raise RevenueOperationAdapterError(
            f"stock price history has nonnumeric OHLC: {path}"
        )
    if (normalized[ohlc] <= 0).any().any():
        raise RevenueOperationAdapterError(
            f"stock price history has nonpositive OHLC: {path}"
        )
    normalized = normalized.sort_values(
        "date", kind="mergesort"
    ).reset_index(drop=True)
    close = normalized["analysis_close"]
    normalized["analysis_ema23"] = close.ewm(
        span=SHAPE_EMA_SPAN_SESSIONS, adjust=False
    ).mean()
    normalized["analysis_ma60"] = close.rolling(
        TRIGGER_MA_SHORT_SESSIONS,
        min_periods=TRIGGER_MA_SHORT_SESSIONS,
    ).mean()
    normalized["analysis_ma120"] = close.rolling(
        TRIGGER_MA_LONG_SESSIONS,
        min_periods=TRIGGER_MA_LONG_SESSIONS,
    ).mean()
    previous_high = close.shift(1).rolling(
        TRIGGER_PREVIOUS_CLOSE_WINDOW_SESSIONS,
        min_periods=TRIGGER_PREVIOUS_CLOSE_WINDOW_SESSIONS,
    ).max()
    breakout = close.gt(previous_high)
    normalized["cross_breakout_prev20"] = (
        breakout & ~breakout.shift(1, fill_value=False).astype(bool)
    )
    normalized["sequence_index"] = normalized.index.astype(int)
    return normalized


def _source_anchor_features(
    frame: pd.DataFrame, index: int
) -> dict[str, Any]:
    prior = frame.iloc[
        index - POSITION_LOOKBACK_PRIOR_SESSIONS : index
    ]
    if len(prior) != POSITION_LOOKBACK_PRIOR_SESSIONS:
        return {
            "position_120d_pct": "",
            "shape_return20_pct": "",
            "shape_ema23_slope5_pct": "",
            "position_bucket": "insufficient_history",
            "shape_bucket": "insufficient_history",
        }
    high = float(prior["analysis_high"].max())
    low = float(prior["analysis_low"].min())
    close = float(frame.at[index, "analysis_close"])
    position = (
        (close - low) / (high - low) * 100.0
        if high > low
        else math.nan
    )
    return20 = (
        (
            close
            / float(
                frame.at[
                    index - SHAPE_RETURN_LOOKBACK_SESSIONS,
                    "analysis_close",
                ]
            )
            - 1.0
        )
        * 100.0
        if index >= SHAPE_RETURN_LOOKBACK_SESSIONS
        else math.nan
    )
    ema_now = float(frame.at[index, "analysis_ema23"])
    ema_prior = float(
        frame.at[
            index - SHAPE_EMA_SLOPE_LOOKBACK_SESSIONS,
            "analysis_ema23",
        ]
    )
    ema_slope = (
        (ema_now / ema_prior - 1.0) * 100.0
        if ema_prior > 0
        else math.nan
    )
    position_bucket = (
        "low_pos_le40"
        if math.isfinite(position)
        and position <= POSITION_LOW_MAX_PCT
        else "mid_pos_40_75"
        if math.isfinite(position)
        and position <= POSITION_MID_MAX_PCT
        else "high_pos_gt75"
        if math.isfinite(position)
        else "insufficient_history"
    )
    shape_bucket = (
        "falling"
        if math.isfinite(return20)
        and math.isfinite(ema_slope)
        and return20 < SHAPE_FALLING_RETURN_MAX_PCT
        and ema_slope < SHAPE_FALLING_EMA_SLOPE_MAX_PCT
        else "not_falling"
        if math.isfinite(return20) and math.isfinite(ema_slope)
        else "insufficient_history"
    )
    return {
        "position_120d_pct": (
            round(position, 4) if math.isfinite(position) else ""
        ),
        "shape_return20_pct": (
            round(return20, 4) if math.isfinite(return20) else ""
        ),
        "shape_ema23_slope5_pct": (
            round(ema_slope, 4) if math.isfinite(ema_slope) else ""
        ),
        "position_bucket": position_bucket,
        "shape_bucket": shape_bucket,
    }


def _attach_source_indices(
    revenue_rows: pd.DataFrame,
    frame: pd.DataFrame,
) -> list[dict[str, Any]]:
    sources: list[dict[str, Any]] = []
    dates = frame["date"].astype(str)
    for _, row in revenue_rows.sort_values(
        ["source_table_date", "revenue_period"], kind="mergesort"
    ).iterrows():
        matches = frame.index[
            dates.ge(str(row["source_table_date"]))
        ]
        if not len(matches):
            continue
        source_index = int(matches[0])
        sources.append(
            {
                **row.to_dict(),
                "source_sequence_index": source_index,
                "source_trade_date": str(
                    frame.at[source_index, "date"]
                ),
                **_source_anchor_features(frame, source_index),
            }
        )
    return sources


def _latest_source_asof(
    sources: Iterable[Mapping[str, Any]],
    trigger_index: int,
) -> Mapping[str, Any] | None:
    candidates = [
        source
        for source in sources
        if 0
        <= trigger_index - int(source["source_sequence_index"])
        <= SOURCE_TO_TRIGGER_MAX_TRADING_DAYS
    ]
    if not candidates:
        return None
    return max(
        candidates,
        key=lambda row: (
            int(row["source_sequence_index"]),
            str(row["source_table_date"]),
            str(row["revenue_period"]),
        ),
    )


def _base_trigger_hit(frame: pd.DataFrame, index: int) -> bool:
    ma60 = float(frame.at[index, "analysis_ma60"])
    ma120 = float(frame.at[index, "analysis_ma120"])
    return bool(
        bool(frame.at[index, "cross_breakout_prev20"])
        and math.isfinite(ma60)
        and math.isfinite(ma120)
        and ma60 > ma120
    )


def _selected_source_mid_falling(
    source: Mapping[str, Any],
) -> bool:
    return bool(
        source.get("position_bucket") == "mid_pos_40_75"
        and source.get("shape_bucket") == "falling"
    )


def _history_row_hash(row: Mapping[str, Any]) -> str:
    columns = tuple(
        column
        for column in OUTPUT_COLUMNS
        if column not in {"generated_at", "row_canonical_sha256"}
    )
    return _mapping_sha256(row, columns)


def load_prior_confirmed_history(
    history_dir: Path,
    *,
    report_date: str,
) -> dict[str, tuple[str, str]]:
    """Return prior formal confirmed keys and immutable row evidence."""

    if not history_dir.is_dir():
        return {}
    confirmed: dict[str, tuple[str, str]] = {}
    pattern = "daily_revenue_unreacted_range_operation_section_*.csv"
    for path in sorted(history_dir.glob(pattern)):
        frame = pd.read_csv(
            path,
            dtype=str,
            keep_default_na=False,
            encoding="utf-8-sig",
        )
        missing = sorted(set(OUTPUT_COLUMNS) - set(frame.columns))
        if missing:
            raise RevenueOperationAdapterError(
                f"formal history schema is incomplete: {path}/{missing}"
            )
        for row in frame.to_dict(orient="records"):
            asof_date = _date_text(
                row["operation_asof_date"],
                label=f"{path.name}/operation_asof_date",
            )
            if asof_date >= report_date:
                continue
            if (
                row["operation_module_id"] != OPERATION_MODULE_ID
                or row["row_type"] != "data"
                or row["pdf_section"] != "confirmed_operation"
                or not _strict_bool(
                    row["buy_rank_eligible"],
                    label=f"{path.name}/buy_rank_eligible",
                )
            ):
                continue
            expected_hash = _history_row_hash(row)
            if row["row_canonical_sha256"] != expected_hash:
                raise RevenueOperationAdapterError(
                    f"formal confirmed history row hash drift: {path}"
                )
            operation_key = _text(row["operation_key"])
            evidence = (_display_path(path), expected_hash)
            previous = confirmed.get(operation_key)
            if previous and previous[1] != expected_hash:
                # Highlight/full copies may differ only by presentation fields,
                # so retain the lexicographically first canonical row proof.
                confirmed[operation_key] = min(previous, evidence)
            else:
                confirmed[operation_key] = evidence
    return confirmed


def replay_stock_lifecycle(
    stock_id: str,
    stock_name: str,
    frame: pd.DataFrame,
    sources: Sequence[Mapping[str, Any]],
    *,
    report_date: str,
    report_line: str,
    taxonomy: Mapping[str, str],
    monthly_source_path: Path,
    price_source_path: Path,
    taxonomy_paths: Sequence[Path],
    prior_confirmed_history: Mapping[str, tuple[str, str]],
) -> list[dict[str, Any]]:
    records: list[dict[str, Any]] = []
    blocked_through_index = -1
    price_sha = _file_sha256(price_source_path)
    base_source_artifacts = [
        _display_path(monthly_source_path),
        _display_path(price_source_path),
        *(_display_path(path) for path in taxonomy_paths),
    ]
    for trigger_index in range(len(frame)):
        signal_date = str(frame.at[trigger_index, "date"])
        if signal_date < FORMAL_SIGNAL_EFFECTIVE_FROM:
            continue
        if (
            trigger_index <= blocked_through_index
            or not _base_trigger_hit(frame, trigger_index)
        ):
            continue
        source = _latest_source_asof(sources, trigger_index)
        if source is None:
            continue
        confirmation_index = (
            trigger_index + CONFIRMATION_OFFSET_TRADING_DAYS
        )
        entry_index = trigger_index + ENTRY_OFFSET_TRADING_DAYS
        planned_exit_index = (
            entry_index + HOLDING_SESSION_INDEX_OFFSET
        )
        selected_member = _selected_source_mid_falling(source)
        operation_key = "|".join(
            (
                MODEL_ID,
                MODEL_VARIANT_ID,
                stock_id,
                signal_date,
            )
        )
        base: dict[str, Any] = {
            "operation_key": operation_key,
            "stock_id": stock_id,
            "stock_name": stock_name,
            "report_line": report_line,
            "taxonomy_status": taxonomy.get(
                "taxonomy_status",
                "taxonomy_incomplete_fail_closed_non_mainstream",
            ),
            "theme_mainstream_label": taxonomy.get(
                "theme_mainstream_label", ""
            ),
            "primary_theme": taxonomy.get("primary_theme", ""),
            "industry": taxonomy.get("industry", ""),
            "source_revenue_period": source["revenue_period"],
            "source_table_date": source["source_table_date"],
            "source_trade_date": source["source_trade_date"],
            "source_sequence_index": int(
                source["source_sequence_index"]
            ),
            "source_to_trigger_trading_days": (
                trigger_index - int(source["source_sequence_index"])
            ),
            "source_position_120d_pct": source[
                "position_120d_pct"
            ],
            "source_shape_return20_pct": source[
                "shape_return20_pct"
            ],
            "source_shape_ema23_slope5_pct": source[
                "shape_ema23_slope5_pct"
            ],
            "source_revenue_anomaly_candidate_flag": bool(
                source["source_revenue_anomaly_candidate_flag"]
            ),
            "signal_date": signal_date,
            "signal_sequence_index": trigger_index,
            "signal_close": round(
                float(frame.at[trigger_index, "analysis_close"]), 8
            ),
            "confirmation_date": "",
            "confirmation_sequence_index": confirmation_index,
            "confirmation_close": "",
            "entry_date": "",
            "entry_sequence_index": entry_index,
            "entry_price": "",
            "planned_exit_sequence_index": planned_exit_index,
            "exit_date": "",
            "exit_price": "",
            "monthly_revenue_source_row_sha256": source[
                "monthly_revenue_source_row_sha256"
            ],
            "price_source_sha256": price_sha,
            "taxonomy_source_row_sha256": taxonomy.get(
                "taxonomy_source_row_sha256", ""
            ),
            "source_artifacts": ";".join(base_source_artifacts),
            "confirmed_history_artifact": "",
            "confirmed_history_row_sha256": "",
            "selected_member": selected_member,
            "report_date": report_date,
            "report_sequence_index": len(frame) - 1,
        }
        if confirmation_index >= len(frame):
            if selected_member:
                records.append(
                    {
                        **base,
                        "lifecycle_state": "pending_confirmation",
                    }
                )
            break
        confirmation_close = float(
            frame.at[confirmation_index, "analysis_close"]
        )
        if not confirmation_close > float(
            frame.at[trigger_index, "analysis_close"]
        ):
            continue
        base["confirmation_date"] = str(
            frame.at[confirmation_index, "date"]
        )
        base["confirmation_close"] = round(confirmation_close, 8)
        blocked_through_index = planned_exit_index
        if entry_index >= len(frame):
            if selected_member:
                records.append(
                    {
                        **base,
                        "lifecycle_state": "confirmed_operation",
                    }
                )
            break
        entry_price = float(frame.at[entry_index, "analysis_open"])
        if not math.isfinite(entry_price) or entry_price <= 0:
            raise RevenueOperationAdapterError(
                f"formal D+2 open is invalid: {stock_id}/{signal_date}"
            )
        base["entry_date"] = str(frame.at[entry_index, "date"])
        base["entry_price"] = round(entry_price, 8)
        if selected_member:
            proof = prior_confirmed_history.get(operation_key)
            if proof is None:
                raise RevenueOperationAdapterError(
                    "active operation lacks a prior formal buy-ranked "
                    f"confirmed history row: {operation_key}"
                )
            base["confirmed_history_artifact"] = proof[0]
            base["confirmed_history_row_sha256"] = proof[1]
            base["source_artifacts"] = ";".join(
                (*base_source_artifacts, proof[0])
            )
        if planned_exit_index >= len(frame):
            if selected_member:
                records.append(
                    {
                        **base,
                        "lifecycle_state": "active_operation",
                    }
                )
            break
        exit_price = float(
            frame.at[planned_exit_index, "analysis_close"]
        )
        if not math.isfinite(exit_price) or exit_price <= 0:
            raise RevenueOperationAdapterError(
                f"formal D+30 close is invalid: {stock_id}/{signal_date}"
            )
        base["exit_date"] = str(
            frame.at[planned_exit_index, "date"]
        )
        base["exit_price"] = round(exit_price, 8)
        if selected_member:
            records.append(
                {**base, "lifecycle_state": "exited_operation"}
            )
    return records


def _lifecycle_replay_sha256(
    records: Sequence[Mapping[str, Any]],
) -> str:
    columns = (
        "operation_key",
        "stock_id",
        "source_revenue_period",
        "source_table_date",
        "source_trade_date",
        "source_sequence_index",
        "signal_date",
        "signal_sequence_index",
        "confirmation_date",
        "confirmation_sequence_index",
        "entry_date",
        "entry_sequence_index",
        "planned_exit_sequence_index",
        "exit_date",
        "lifecycle_state",
        "confirmed_history_row_sha256",
    )
    payload = [
        [
            [
                column,
                _canonical_value(record.get(column, "")),
            ]
            for column in columns
        ]
        for record in sorted(
            records, key=lambda row: str(row["operation_key"])
        )
    ]
    return hashlib.sha256(
        json.dumps(
            payload, ensure_ascii=False, separators=(",", ":")
        ).encode("utf-8")
    ).hexdigest()


def _fixed_row_metadata() -> dict[str, Any]:
    return {
        "model_id": MODEL_ID,
        "model_name_zh": MODEL_NAME_ZH,
        "model_variant_id": MODEL_VARIANT_ID,
        "model_variant_version": MODEL_VARIANT_VERSION,
        "operation_module_id": OPERATION_MODULE_ID,
        "adapter_schema_version": ADAPTER_SCHEMA_VERSION,
        "lifecycle_contract_version": LIFECYCLE_CONTRACT_VERSION,
        "adapter_mode": ADAPTER_MODE,
        "approval_version": APPROVAL_VERSION,
        "approval_status": APPROVAL_STATUS,
        "formal_signal_effective_from": FORMAL_SIGNAL_EFFECTIVE_FROM,
        "rule_spec_id": RULE_SPEC_ID,
        "rule_canonical_sha256": RULE_CANONICAL_SHA256,
        "selection_policy": SELECTION_POLICY,
        "holdout_use_policy": HOLDOUT_USE_POLICY,
        "operation_directive_level": OPERATION_DIRECTIVE_LEVEL,
        "sample_size": BASELINE_SAMPLE_SIZE,
        "win_rate_zh": f"{BASELINE_WIN_RATE_PCT:.4f}%",
        "neutral_rate_zh": f"{BASELINE_NEUTRAL_RATE_PCT:.4f}%",
        "failure_rate_zh": f"{BASELINE_FAILURE_RATE_PCT:.4f}%",
        "avg_return_zh": f"+{BASELINE_AVG_RETURN_PCT:.4f}%",
        "median_return_zh": f"+{BASELINE_MEDIAN_RETURN_PCT:.4f}%",
        "baseline_performance_status": BASELINE_PERFORMANCE_STATUS,
        "baseline_performance_scope": BASELINE_PERFORMANCE_SCOPE,
        "baseline_performance_source": BASELINE_PERFORMANCE_SOURCE,
        "formal_model_use_allowed": True,
        "approved_for_daily": True,
        "presentation_allowed": True,
        "production_allowed": True,
        "confirmation_rule_id": CONFIRMATION_RULE_ID,
        "entry_rule_id": ENTRY_RULE_ID,
        "exit_rule_id": EXIT_RULE_ID,
        "stop_policy_id": STOP_POLICY_ID,
        "confirmation_offset_trading_days": (
            CONFIRMATION_OFFSET_TRADING_DAYS
        ),
        "entry_offset_trading_days": ENTRY_OFFSET_TRADING_DAYS,
        "holding_days": HOLDING_DAYS,
        "planned_holding_days": HOLDING_DAYS,
        "holding_session_index_offset": (
            HOLDING_SESSION_INDEX_OFFSET
        ),
        "entry_basis_zh": (
            "D+1 收盤高於訊號日收盤確認；D+2 開盤進場。"
        ),
        "stop_loss_rule_id": STOP_POLICY_ID,
        "stop_loss_price": "",
        "stop_loss_label_zh": "不設正式停損價",
        "stop_basis_zh": "不設停損；固定持有至 D+30 收盤。",
        "exit_rule_zh": (
            "進場後固定於 D+30（自進場日計第30個交易日）收盤出場。"
        ),
        "entry_price_basis": ENTRY_PRICE_BASIS,
        "exit_price_basis": EXIT_PRICE_BASIS,
        "price_confirmation_basis": PRICE_CONFIRMATION_BASIS,
        "same_stock_non_overlap_policy": (
            SAME_STOCK_NON_OVERLAP_POLICY
        ),
        "financial_statement_scope": FINANCIAL_STATEMENT_SCOPE,
        "adapter_source_status": (
            "objective_sources_recomputed_no_research_latest_input"
        ),
    }


def _data_row(
    record: Mapping[str, Any],
    *,
    pdf_view: str,
    display_order: int,
    lifecycle_replay_sha256: str,
    generated_at: str,
) -> dict[str, Any]:
    state = str(record["lifecycle_state"])
    buy_rank_eligible = state == "confirmed_operation"
    note = {
        "pending_confirmation": (
            "等待 D+1 收盤高於訊號收盤；尚未形成買進列。"
        ),
        "confirmed_operation": (
            "D+1 close-only 確認成立；下一交易日開盤為正式進場基準。"
        ),
        "active_operation": (
            "已由先前正式 confirmed_operation 進場；固定持有至 D+30 收盤。"
        ),
    }[state]
    return {
        **_fixed_row_metadata(),
        "pdf_view": pdf_view,
        "pdf_section": state,
        "pdf_section_zh": SECTION_ZH[state],
        "row_type": "data",
        "empty_text_zh": "",
        "operation_asof_date": record["report_date"],
        "operation_source_date_status": "matches_report_date",
        "report_line": record["report_line"],
        "report_line_memberships": record["report_line"],
        "display_order": display_order,
        "operation_key": record["operation_key"],
        "stock_id": record["stock_id"],
        "stock_name": record["stock_name"],
        "stock_display": (
            f"{record['stock_id']} {record['stock_name']}".strip()
        ),
        "rank_reason_zh": (
            "固定 source_mid_falling v2 規則命中；provisional gross "
            "historical 僅揭露、不作排序。"
        ),
        "risk_tags_zh": "",
        "taxonomy_status": record["taxonomy_status"],
        "theme_mainstream_label": record[
            "theme_mainstream_label"
        ],
        "primary_theme": record["primary_theme"],
        "industry": record["industry"],
        "lifecycle_state": state,
        "operation_status": state,
        "operation_status_zh": STATE_ZH[state],
        "operation_quality": state,
        "operation_quality_zh": QUALITY_ZH[state],
        "row_action_status": ROW_ACTION_STATUS[state],
        "buy_rank_eligible": buy_rank_eligible,
        "row_metric_status": (
            "unavailable_no_approved_add_score_metric"
        ),
        "row_metric_scope": "",
        "row_metric_id": "",
        "row_metric_label_zh": "",
        "row_metric_matched_add_score_ids": "",
        "row_metric_sample_size": "",
        "row_metric_win_rate_zh": "",
        "row_metric_neutral_rate_zh": "",
        "row_metric_failure_rate_zh": "",
        "row_metric_avg_return_zh": "",
        "row_metric_median_return_zh": "",
        "row_metric_source": "",
        "row_metric_selection_status": (
            "baseline_not_permitted_in_operation_row"
        ),
        "source_revenue_period": record["source_revenue_period"],
        "source_table_date": record["source_table_date"],
        "source_trade_date": record["source_trade_date"],
        "source_sequence_index": record[
            "source_sequence_index"
        ],
        "source_to_trigger_trading_days": record[
            "source_to_trigger_trading_days"
        ],
        "source_position_120d_pct": record[
            "source_position_120d_pct"
        ],
        "source_shape_return20_pct": record[
            "source_shape_return20_pct"
        ],
        "source_shape_ema23_slope5_pct": record[
            "source_shape_ema23_slope5_pct"
        ],
        "signal_date": record["signal_date"],
        "signal_sequence_index": record[
            "signal_sequence_index"
        ],
        "signal_close": record["signal_close"],
        "confirmation_date": record["confirmation_date"],
        "confirmation_sequence_index": record[
            "confirmation_sequence_index"
        ],
        "confirmation_close": record["confirmation_close"],
        "entry_date": record["entry_date"],
        "entry_sequence_index": record["entry_sequence_index"],
        "entry_price": record["entry_price"],
        "entry_basis_zh": (
            "D+1 收盤高於訊號日收盤確認；D+2 開盤進場。"
        ),
        "entry_price_status_zh": (
            "已由正式歷史 confirmed_operation 支撐的 D+2 開盤價"
            if state == "active_operation"
            else "尚未到正式進場日，等待 D+2 開盤價"
        ),
        "stop_loss_rule_id": STOP_POLICY_ID,
        "stop_loss_price": "",
        "stop_loss_label_zh": "不設正式停損價",
        "stop_basis_zh": "不設停損；固定持有至 D+30 收盤。",
        "planned_exit_sequence_index": record[
            "planned_exit_sequence_index"
        ],
        "exit_date": "",
        "exit_price": "",
        "exit_rule_zh": (
            "進場後固定於 D+30（自進場日計第30個交易日）收盤出場。"
        ),
        "planned_holding_days": HOLDING_DAYS,
        "operation_age_days": (
            int(record["report_sequence_index"])
            - int(record["entry_sequence_index"])
            + 1
            if state == "active_operation"
            else ""
        ),
        "source_revenue_anomaly_candidate_flag": record[
            "source_revenue_anomaly_candidate_flag"
        ],
        "source_artifacts": record["source_artifacts"],
        "monthly_revenue_source_row_sha256": record[
            "monthly_revenue_source_row_sha256"
        ],
        "price_source_sha256": record["price_source_sha256"],
        "taxonomy_source_row_sha256": record[
            "taxonomy_source_row_sha256"
        ],
        "confirmed_history_artifact": record[
            "confirmed_history_artifact"
        ],
        "confirmed_history_row_sha256": record[
            "confirmed_history_row_sha256"
        ],
        "lifecycle_replay_sha256": lifecycle_replay_sha256,
        "adapter_note_zh": note,
        "generated_at": generated_at,
        "row_canonical_sha256": "",
    }


def _empty_row(
    *,
    report_date: str,
    report_line: str,
    pdf_view: str,
    pdf_section: str,
    source_artifacts: str,
    lifecycle_replay_sha256: str,
    generated_at: str,
) -> dict[str, Any]:
    row = {column: "" for column in OUTPUT_COLUMNS}
    row.update(
        {
            **_fixed_row_metadata(),
            "pdf_view": pdf_view,
            "pdf_section": pdf_section,
            "pdf_section_zh": SECTION_ZH[pdf_section],
            "row_type": "empty_state",
            "empty_text_zh": SECTION_EMPTY_TEXT_ZH[
                pdf_section
            ],
            "operation_asof_date": report_date,
            "operation_source_date_status": (
                "pre_effective_empty_state"
                if report_date < FORMAL_SIGNAL_EFFECTIVE_FROM
                else "matches_report_date"
            ),
            "report_line": report_line,
            "report_line_memberships": report_line,
            "display_order": 1,
            "lifecycle_state": pdf_section,
            "operation_status": pdf_section,
            "operation_status_zh": SECTION_EMPTY_TEXT_ZH[
                pdf_section
            ],
            "operation_quality": "empty_state",
            "operation_quality_zh": QUALITY_ZH["empty_state"],
            "row_action_status": "empty_state",
            "buy_rank_eligible": False,
            "row_metric_status": "not_applicable_empty_state",
            "row_metric_selection_status": "empty_state",
            "source_artifacts": source_artifacts,
            "lifecycle_replay_sha256": (
                lifecycle_replay_sha256
            ),
            "adapter_note_zh": (
                "model-owned formal empty state; PDF must not infer "
                "lifecycle from candidate signals"
            ),
            "generated_at": generated_at,
        }
    )
    return row


def build_operation_section(
    *,
    monthly_revenue_path: Path = MONTHLY_REVENUE_HISTORY_CSV,
    stock_price_history_dir: Path = STOCK_PRICE_HISTORY_DIR,
    taxonomy_paths: Sequence[Path] = TAXONOMY_PATHS,
    prior_history_dir: Path = HISTORY_DIR,
    report_date: str | None = None,
    generated_at: str | None = None,
) -> tuple[pd.DataFrame, list[dict[str, Any]]]:
    revenue = load_monthly_revenue_history(monthly_revenue_path)
    taxonomy_map = load_taxonomy(taxonomy_paths)
    price_files = _price_file_map(stock_price_history_dir)
    normalized_report_date = (
        _date_text(report_date, label="report_date")
        if report_date
        else ""
    )
    loaded_prices: dict[str, tuple[pd.DataFrame, Path]] = {}
    if not (
        normalized_report_date
        and normalized_report_date < FORMAL_SIGNAL_EFFECTIVE_FROM
    ):
        stock_ids = sorted(
            set(
                revenue.get(
                    "stock_id", pd.Series(dtype=str)
                ).astype(str)
            )
        )
        for stock_id in stock_ids:
            price_path = price_files.get(stock_id)
            if price_path is None:
                continue
            loaded_prices[stock_id] = (
                load_price_history(price_path),
                price_path,
            )
    if not normalized_report_date:
        available_dates = [
            str(frame["date"].max())
            for frame, _path in loaded_prices.values()
            if not frame.empty
        ]
        if not available_dates:
            raise RevenueOperationAdapterError(
                "cannot derive report_date without price history"
            )
        normalized_report_date = max(available_dates)
    generated = generated_at or now_taipei_text()
    prior_confirmed = (
        load_prior_confirmed_history(
            prior_history_dir,
            report_date=normalized_report_date,
        )
        if normalized_report_date >= FORMAL_SIGNAL_EFFECTIVE_FROM
        else {}
    )

    all_records: list[dict[str, Any]] = []
    current_records: list[dict[str, Any]] = []
    if normalized_report_date >= FORMAL_SIGNAL_EFFECTIVE_FROM:
        for stock_id, revenue_rows in revenue.groupby(
            "stock_id", sort=True
        ):
            loaded = loaded_prices.get(str(stock_id))
            if loaded is None:
                continue
            full_frame, price_path = loaded
            frame = full_frame[
                full_frame["date"]
                .astype(str)
                .le(normalized_report_date)
            ].copy()
            frame = frame.reset_index(drop=True)
            frame["sequence_index"] = frame.index.astype(int)
            if (
                frame.empty
                or str(frame.iloc[-1]["date"])
                != normalized_report_date
            ):
                continue
            sources = _attach_source_indices(
                revenue_rows, frame
            )
            taxonomy = taxonomy_map.get(
                str(stock_id),
                {
                    "taxonomy_status": (
                        "taxonomy_incomplete_fail_closed_non_mainstream"
                    ),
                    "theme_mainstream_label": "",
                    "primary_theme": "",
                    "industry": "",
                    "taxonomy_source_row_sha256": "",
                },
            )
            stock_name = (
                taxonomy.get("stock_name")
                or _text(revenue_rows.iloc[-1]["stock_name"])
            )
            records = replay_stock_lifecycle(
                str(stock_id),
                stock_name,
                frame,
                sources,
                report_date=normalized_report_date,
                report_line=_report_line(taxonomy),
                taxonomy=taxonomy,
                monthly_source_path=monthly_revenue_path,
                price_source_path=price_path,
                taxonomy_paths=taxonomy_paths,
                prior_confirmed_history=prior_confirmed,
            )
            all_records.extend(records)
            current_records.extend(
                record
                for record in records
                if record["lifecycle_state"]
                in {
                    "pending_confirmation",
                    "confirmed_operation",
                    "active_operation",
                }
            )

    replay_sha = _lifecycle_replay_sha256(all_records)
    grouped_current: dict[
        tuple[str, str], list[dict[str, Any]]
    ] = {}
    for record in current_records:
        grouped_current.setdefault(
            (
                str(record["report_line"]),
                str(record["lifecycle_state"]),
            ),
            [],
        ).append(record)
    default_source_artifacts = ";".join(
        (
            _display_path(monthly_revenue_path),
            _display_path(stock_price_history_dir),
            *(_display_path(path) for path in taxonomy_paths),
        )
    )
    rows: list[dict[str, Any]] = []
    for report_line in REPORT_LINES:
        for pdf_view in PDF_VIEWS:
            for pdf_section in PDF_SECTIONS:
                if (
                    pdf_view == "highlight"
                    and pdf_section in HIGHLIGHT_HIDDEN_SECTIONS
                ):
                    continue
                records = sorted(
                    grouped_current.get(
                        (report_line, pdf_section), ()
                    ),
                    key=lambda row: (
                        str(row["signal_date"]),
                        str(row["stock_id"]),
                    ),
                )
                if pdf_section == "confirmed_unranked_operation":
                    records = []
                if records:
                    rows.extend(
                        _data_row(
                            record,
                            pdf_view=pdf_view,
                            display_order=index,
                            lifecycle_replay_sha256=replay_sha,
                            generated_at=generated,
                        )
                        for index, record in enumerate(
                            records, start=1
                        )
                    )
                else:
                    rows.append(
                        _empty_row(
                            report_date=normalized_report_date,
                            report_line=report_line,
                            pdf_view=pdf_view,
                            pdf_section=pdf_section,
                            source_artifacts=(
                                default_source_artifacts
                            ),
                            lifecycle_replay_sha256=replay_sha,
                            generated_at=generated,
                        )
                    )
    section = pd.DataFrame(rows, columns=OUTPUT_COLUMNS)
    for column in OUTPUT_COLUMNS:
        if column != "row_canonical_sha256":
            section[column] = section[column].map(
                _canonical_value
            )
    section["row_canonical_sha256"] = [
        _history_row_hash(row)
        for row in section.to_dict(orient="records")
    ]
    section = section.sort_values(
        [
            "pdf_view",
            "report_line",
            "pdf_section",
            "display_order",
            "stock_id",
        ],
        kind="mergesort",
    ).reset_index(drop=True)
    return section, all_records


def _csv_bytes(frame: pd.DataFrame) -> bytes:
    return frame.to_csv(
        index=False, lineterminator="\n"
    ).encode("utf-8")


def _canonical_semantic_csv_bytes(
    payload: bytes,
    *,
    source_name: str,
) -> bytes:
    try:
        text = payload.decode("utf-8-sig")
    except UnicodeDecodeError as exc:
        raise RevenueOperationAdapterError(
            f"formal history is not UTF-8: {source_name}"
        ) from exc
    records = list(csv.reader(io.StringIO(text, newline="")))
    if not records:
        raise RevenueOperationAdapterError(
            f"formal history is empty: {source_name}"
        )
    header = tuple(records[0])
    if header != OUTPUT_COLUMNS:
        raise RevenueOperationAdapterError(
            f"formal history schema drift: {source_name}"
        )
    generated_at_index = header.index("generated_at")
    output = io.StringIO(newline="")
    writer = csv.writer(output, lineterminator="\n")
    writer.writerow(header)
    for row_number, record in enumerate(records[1:], start=2):
        if len(record) != len(header):
            raise RevenueOperationAdapterError(
                "formal history row width drift: "
                f"{source_name}/row={row_number}"
            )
        normalized = list(record)
        normalized[generated_at_index] = ""
        writer.writerow(normalized)
    return output.getvalue().encode("utf-8")


def _atomic_write(path: Path, payload: bytes) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_name(
        f".{path.name}.{os.getpid()}.tmp"
    )
    temporary.write_bytes(payload)
    os.replace(temporary, path)


def _markdown_text(section: pd.DataFrame) -> str:
    columns = (
        "pdf_view",
        "pdf_section_zh",
        "row_type",
        "report_line",
        "stock_display",
        "operation_status_zh",
        "signal_date",
        "confirmation_date",
        "entry_date",
        "row_action_status",
        "buy_rank_eligible",
    )
    shown = section.loc[:, list(columns)].head(240)
    lines = [
        (
            "# revenue_unreacted_range/source_mid_falling v2 "
            "Daily Operation Section"
        ),
        "",
        "- Producer owner: daily_model_maintenance.",
        (
            "- Runtime selection inputs: objective monthly revenue, "
            "stock price history, and config taxonomy only."
        ),
        (
            "- Active rows additionally require a prior model-owned "
            "formal confirmed history row."
        ),
        (
            "- Rule is frozen; forward holdout is post-launch "
            "monitoring and cannot tune this producer."
        ),
        "",
        "| " + " | ".join(columns) + " |",
        "| " + " | ".join("---" for _ in columns) + " |",
    ]
    for row in shown.to_dict(orient="records"):
        values = [
            _canonical_value(row.get(column, ""))
            .replace("|", "\\|")
            .replace("\n", " ")
            for column in columns
        ]
        lines.append("| " + " | ".join(values) + " |")
    return "\n".join(lines).rstrip() + "\n"


def write_artifacts(
    section: pd.DataFrame,
    *,
    output_csv: Path = OUT_CSV,
    output_md: Path = OUT_MD,
    docs_latest_dir: Path = DOCS_LATEST_DIR,
    history_dir: Path = HISTORY_DIR,
) -> dict[str, str]:
    if tuple(section.columns) != OUTPUT_COLUMNS:
        raise RevenueOperationAdapterError(
            "formal operation section schema drift before write"
        )
    csv_payload = _csv_bytes(section)
    md_payload = _markdown_text(section).encode("utf-8")
    _atomic_write(output_csv, csv_payload)
    _atomic_write(output_md, md_payload)
    _atomic_write(
        docs_latest_dir / output_csv.name, csv_payload
    )
    _atomic_write(
        docs_latest_dir / output_md.name, md_payload
    )

    semantic = section.copy()
    semantic["generated_at"] = ""
    semantic_payload = _canonical_semantic_csv_bytes(
        _csv_bytes(semantic),
        source_name="generated formal operation section",
    )
    semantic_sha256 = hashlib.sha256(
        semantic_payload
    ).hexdigest()
    report_dates = sorted(
        set(section["operation_asof_date"].astype(str))
    )
    if len(report_dates) != 1:
        raise RevenueOperationAdapterError(
            "formal operation section must have one report date: "
            f"{report_dates}"
        )
    history_path = history_dir / (
        "daily_revenue_unreacted_range_operation_section_"
        f"{report_dates[0]}_{semantic_sha256}.csv"
    )
    if history_path.exists():
        existing_semantic_payload = _canonical_semantic_csv_bytes(
            history_path.read_bytes(),
            source_name=str(history_path),
        )
        if existing_semantic_payload != semantic_payload:
            raise RevenueOperationAdapterError(
                f"append-only history collision: {history_path}"
            )
    else:
        _atomic_write(history_path, semantic_payload)
    return {
        "output_csv": str(output_csv),
        "output_md": str(output_md),
        "docs_csv": str(
            docs_latest_dir / output_csv.name
        ),
        "docs_md": str(
            docs_latest_dir / output_md.name
        ),
        "history_csv": str(history_path),
        "artifact_semantic_sha256": semantic_sha256,
    }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Build the formal revenue_unreacted_range/"
            "source_mid_falling v2 operation section."
        )
    )
    parser.add_argument(
        "--monthly-revenue-history",
        type=Path,
        default=MONTHLY_REVENUE_HISTORY_CSV,
    )
    parser.add_argument(
        "--stock-price-history-dir",
        type=Path,
        default=STOCK_PRICE_HISTORY_DIR,
    )
    parser.add_argument(
        "--taxonomy", type=Path, action="append"
    )
    parser.add_argument("--prior-history-dir", type=Path, default=HISTORY_DIR)
    parser.add_argument("--report-date")
    parser.add_argument("--generated-at")
    parser.add_argument(
        "--output-csv", type=Path, default=OUT_CSV
    )
    parser.add_argument(
        "--output-md", type=Path, default=OUT_MD
    )
    parser.add_argument(
        "--docs-latest-dir",
        type=Path,
        default=DOCS_LATEST_DIR,
    )
    parser.add_argument(
        "--history-dir", type=Path, default=HISTORY_DIR
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    taxonomy_paths = (
        tuple(args.taxonomy)
        if args.taxonomy
        else TAXONOMY_PATHS
    )
    section, records = build_operation_section(
        monthly_revenue_path=args.monthly_revenue_history,
        stock_price_history_dir=(
            args.stock_price_history_dir
        ),
        taxonomy_paths=taxonomy_paths,
        prior_history_dir=args.prior_history_dir,
        report_date=args.report_date,
        generated_at=args.generated_at,
    )
    outputs = write_artifacts(
        section,
        output_csv=args.output_csv,
        output_md=args.output_md,
        docs_latest_dir=args.docs_latest_dir,
        history_dir=args.history_dir,
    )
    data_rows = int(
        section["row_type"].astype(str).eq("data").sum()
    )
    print(
        "Saved formal revenue operation adapter: "
        f"rows={len(section)} data_rows={data_rows} "
        f"lifecycle_records={len(records)} "
        "semantic_sha256="
        f"{outputs['artifact_semantic_sha256']}"
    )
    for label, path in outputs.items():
        if label != "artifact_semantic_sha256":
            print(f"Saved {label}: {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
