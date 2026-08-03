from __future__ import annotations

from pathlib import Path

import numpy as np
import pandas as pd

from build_daily_model_parameter_research import build_research_frame as _build_shared_research_frame
from revenue_unreacted_range_monthly_revenue_cross_market_resolution import (
    ROOT,
    RESOLUTION_CSV as MONTHLY_REVENUE_CROSS_MARKET_RESOLUTION_CSV,
    load_canonical_monthly_revenue_history,
)


MONTHLY_REVENUE_HISTORY = ROOT / "data/monthly_revenue_history/monthly_revenue_history.csv"
CANONICAL_MONTHLY_REVENUE_SOURCE_ARTIFACT = (
    "data/monthly_revenue_history/monthly_revenue_history.csv"
)
FULL_MONTHLY_REVENUE_PREFIX = "full_monthly_revenue_"


def _normalize_stock_id(value: object) -> str:
    text = str(value).strip().replace(".0", "")
    return text.zfill(4) if text else ""


def _digits(value: object, length: int) -> str:
    text = str(value).strip()
    if pd.isna(value):
        text = ""
    if text.isdigit() and len(text) == length:
        return text
    numeric_export = text.removesuffix(".0")
    if numeric_export.isdigit() and len(numeric_export) == length and text.endswith(".0"):
        return numeric_export
    raise RuntimeError(
        "revenue_unreacted_range date/period identity must be exact digits or an "
        f"equivalent numeric export: value={text!r}; digits={length}"
    )


def _trueish(series: pd.Series) -> pd.Series:
    return series.astype(str).str.strip().str.lower().isin({"true", "1", "yes"})


def attach_revenue_unreacted_range_canonical_monthly_history(
    frame: pd.DataFrame,
    history_path: Path = MONTHLY_REVENUE_HISTORY,
    resolution_path: Path = MONTHLY_REVENUE_CROSS_MARKET_RESOLUTION_CSV,
) -> pd.DataFrame:
    """Replace shared monthly fields with the model-owned canonical history view."""
    if frame.empty:
        return frame.copy()
    missing_frame = sorted({"stock_id", "date"} - set(frame.columns))
    if missing_frame:
        raise RuntimeError(
            f"revenue_unreacted_range research frame is missing join columns: {missing_frame}"
        )

    history = load_canonical_monthly_revenue_history(history_path, resolution_path)
    required_history = {
        "stock_id",
        "source_table_date",
        "revenue_period",
        "source_kind",
        "latest_revenue_yoy_pct",
        "cumulative_revenue_yoy_pct",
        "month_over_month_pct",
        "revenue_numerical_anomaly_flag",
        "revenue_numerical_anomaly_reason",
        "research_join_allowed",
        "allowed_for_formal_historical_model_use",
        "cross_market_resolution_id",
        "source_row_canonical_sha256",
        "canonical_source_table_date",
    }
    missing_history = sorted(required_history - set(history.columns))
    if missing_history:
        raise RuntimeError(
            "canonical monthly revenue history is missing research-frame columns: "
            f"{missing_history}"
        )

    history = history.copy()
    history["stock_id"] = history["stock_id"].map(_normalize_stock_id)
    history["source_table_date"] = history["source_table_date"].map(
        lambda value: _digits(value, 8)
    )
    history["revenue_period"] = history["revenue_period"].map(lambda value: _digits(value, 6))
    if history[["stock_id", "source_table_date", "revenue_period"]].eq("").any(axis=None):
        raise RuntimeError("canonical monthly revenue history has blank join identities")
    if history.duplicated(["stock_id", "revenue_period"]).any():
        raise RuntimeError("canonical monthly revenue history repeats a stock-period")
    history["_rr_source_dt"] = pd.to_datetime(
        history["source_table_date"], format="%Y%m%d", errors="coerce"
    )
    if history["_rr_source_dt"].isna().any():
        raise RuntimeError("canonical monthly revenue history has an invalid source table date")
    history = history.sort_values(
        ["stock_id", "_rr_source_dt", "revenue_period"], kind="mergesort"
    ).reset_index(drop=True)
    grouped = history.groupby("stock_id", sort=False, dropna=False)
    for lag in (1, 2, 3):
        history[f"prev{lag}_revenue_period"] = grouped["revenue_period"].shift(lag)
        history[f"prev{lag}_latest_revenue_yoy_pct"] = grouped[
            "latest_revenue_yoy_pct"
        ].shift(lag)
        history[f"prev{lag}_cumulative_revenue_yoy_pct"] = grouped[
            "cumulative_revenue_yoy_pct"
        ].shift(lag)

    keep = [
        "stock_id",
        "_rr_source_dt",
        "source_table_date",
        "revenue_period",
        "source_kind",
        "latest_revenue_yoy_pct",
        "cumulative_revenue_yoy_pct",
        "month_over_month_pct",
        "revenue_numerical_anomaly_flag",
        "revenue_numerical_anomaly_reason",
        "research_join_allowed",
        "allowed_for_formal_historical_model_use",
        "cross_market_resolution_id",
        "source_row_canonical_sha256",
        "canonical_source_table_date",
        *[
            f"prev{lag}_{field}"
            for lag in (1, 2, 3)
            for field in (
                "revenue_period",
                "latest_revenue_yoy_pct",
                "cumulative_revenue_yoy_pct",
            )
        ],
    ]
    history = history[keep].rename(
        columns={column: f"_rr_{column}" for column in keep if column != "stock_id"}
    )

    stale_columns = [
        column for column in frame.columns if column.startswith(FULL_MONTHLY_REVENUE_PREFIX)
    ]
    left = frame.drop(columns=stale_columns).copy()
    left["stock_id"] = left["stock_id"].map(_normalize_stock_id)
    left["date"] = left["date"].map(lambda value: _digits(value, 8))
    left["_rr_original_index"] = range(len(left))
    left["_rr_signal_dt"] = pd.to_datetime(left["date"], format="%Y%m%d", errors="coerce")
    if left["stock_id"].eq("").any() or left["_rr_signal_dt"].isna().any():
        raise RuntimeError("revenue_unreacted_range research frame has invalid stock/date join identities")

    history_by_stock = {
        stock_id: part.reset_index(drop=True)
        for stock_id, part in history.groupby("stock_id", sort=False, dropna=False)
    }
    merged_parts: list[pd.DataFrame] = []
    right_columns = [column for column in history.columns if column != "stock_id"]
    for stock_id, price_part in left.groupby("stock_id", sort=False, dropna=False):
        hist_part = history_by_stock.get(str(stock_id))
        if hist_part is None or hist_part.empty:
            missing = price_part.copy()
            for column in right_columns:
                missing[column] = pd.NaT if column == "_rr__rr_source_dt" else ""
            missing["_rr_history_stock_status"] = (
                "missing_stock_in_full_monthly_revenue_history"
            )
            merged_parts.append(missing)
            continue
        stock_merged = pd.merge_asof(
            price_part.sort_values("_rr_signal_dt"),
            hist_part.drop(columns=["stock_id"]).sort_values("_rr__rr_source_dt"),
            left_on="_rr_signal_dt",
            right_on="_rr__rr_source_dt",
            direction="backward",
        )
        stock_merged["_rr_history_stock_status"] = ""
        merged_parts.append(stock_merged)
    merged = pd.concat(merged_parts, ignore_index=True, sort=False)

    def text(name: str) -> pd.Series:
        return merged.get(name, pd.Series("", index=merged.index, dtype=object)).fillna("")

    source_date = text("_rr_source_table_date")
    has_match = source_date.ne("")
    merged["full_monthly_revenue_data_status"] = np.where(
        has_match,
        "ready_asof_history_row",
        np.where(
            text("_rr_history_stock_status").ne(""),
            text("_rr_history_stock_status"),
            "missing_asof_revenue_on_or_before_signal_date",
        ),
    )
    merged["full_monthly_revenue_period"] = text("_rr_revenue_period")
    merged["full_monthly_revenue_source_table_date"] = source_date
    merged["full_monthly_revenue_latest_yoy_pct"] = pd.to_numeric(
        text("_rr_latest_revenue_yoy_pct"), errors="coerce"
    )
    merged["full_monthly_revenue_cumulative_yoy_pct"] = pd.to_numeric(
        text("_rr_cumulative_revenue_yoy_pct"), errors="coerce"
    )
    merged["full_monthly_revenue_month_over_month_pct"] = pd.to_numeric(
        text("_rr_month_over_month_pct"), errors="coerce"
    )
    for lag in (1, 2, 3):
        merged[f"full_monthly_revenue_prev{lag}_period"] = text(
            f"_rr_prev{lag}_revenue_period"
        )
        merged[f"full_monthly_revenue_prev{lag}_latest_yoy_pct"] = pd.to_numeric(
            text(f"_rr_prev{lag}_latest_revenue_yoy_pct"), errors="coerce"
        )
        merged[f"full_monthly_revenue_prev{lag}_cumulative_yoy_pct"] = pd.to_numeric(
            text(f"_rr_prev{lag}_cumulative_revenue_yoy_pct"), errors="coerce"
        )
    latest = merged["full_monthly_revenue_latest_yoy_pct"]
    cumulative = merged["full_monthly_revenue_cumulative_yoy_pct"]
    merged["full_monthly_revenue_latest_yoy_delta_1m_pct_points"] = (
        latest - merged["full_monthly_revenue_prev1_latest_yoy_pct"]
    )
    merged["full_monthly_revenue_cumulative_yoy_delta_1m_pct_points"] = (
        cumulative - merged["full_monthly_revenue_prev1_cumulative_yoy_pct"]
    )
    research_allowed = _trueish(text("_rr_research_join_allowed"))
    cross_market_resolution_id = text("_rr_cross_market_resolution_id")
    formal_allowed = _trueish(
        text("_rr_allowed_for_formal_historical_model_use")
    ) & cross_market_resolution_id.eq("")
    context_ready = has_match & research_allowed
    merged["full_monthly_revenue_context_ready"] = context_ready
    merged["full_monthly_revenue_positive_flag"] = context_ready & (
        latest.gt(0) | cumulative.gt(0)
    )
    merged["full_monthly_revenue_strong_flag"] = context_ready & (
        latest.ge(30) | cumulative.ge(20)
    )
    merged["full_monthly_revenue_positive_or_strong"] = (
        merged["full_monthly_revenue_positive_flag"]
        | merged["full_monthly_revenue_strong_flag"]
    )
    merged["full_monthly_revenue_numerical_anomaly_flag"] = context_ready & _trueish(
        text("_rr_revenue_numerical_anomaly_flag")
    )
    merged["full_monthly_revenue_numerical_anomaly_reason"] = text(
        "_rr_revenue_numerical_anomaly_reason"
    )
    merged["full_monthly_revenue_research_join_allowed"] = research_allowed
    merged["full_monthly_revenue_formal_model_use_allowed"] = formal_allowed
    merged["full_monthly_revenue_cross_market_resolution_id"] = (
        cross_market_resolution_id
    )
    merged["full_monthly_revenue_source_row_canonical_sha256"] = text(
        "_rr_source_row_canonical_sha256"
    )
    merged["full_monthly_revenue_canonical_source_table_date"] = text(
        "_rr_canonical_source_table_date"
    )
    merged["full_monthly_revenue_source_kind"] = text("_rr_source_kind")
    merged["full_monthly_revenue_source_artifact"] = (
        CANONICAL_MONTHLY_REVENUE_SOURCE_ARTIFACT
    )

    drop = [column for column in merged.columns if column.startswith("_rr_")]
    return (
        merged.sort_values("_rr_original_index", kind="mergesort")
        .drop(columns=drop)
        .reset_index(drop=True)
    )


def build_revenue_unreacted_range_research_frame() -> pd.DataFrame:
    return attach_revenue_unreacted_range_canonical_monthly_history(
        _build_shared_research_frame()
    )
