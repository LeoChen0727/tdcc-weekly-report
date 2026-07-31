from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo

import numpy as np
import pandas as pd

from revenue_unreacted_range_rearmed_operation_grid import (
    ARTIFACT_ID as SOURCE_OPERATION_ARTIFACT_ID,
    ARTIFACT_VERSION as SOURCE_OPERATION_ARTIFACT_VERSION,
    DETAIL_CSV as SOURCE_OPERATION_DETAIL_CSV,
    FINANCIAL_STATEMENT_SCOPE,
    NO_STOP_POLICY_ID,
    SOURCE_VARIANT_ID,
)
from revenue_unreacted_range_source_first_condition_audit import (
    ARTIFACT_ID as SOURCE_CONDITION_ARTIFACT_ID,
    ARTIFACT_VERSION as SOURCE_CONDITION_ARTIFACT_VERSION,
    DISCOVERY_HORIZON_DAYS,
)
from revenue_unreacted_range_source_snapshot_projection import (
    LATEST_DETAIL_CSV as SOURCE_CONDITION_DETAIL_CSV,
    load_projected_source_detail,
    load_source_snapshot_projection_manifest,
    validate_projection_binding,
)


ROOT = Path(__file__).resolve().parents[1]
MODEL_ID = "revenue_unreacted_range"
ARTIFACT_ID = "revenue_unreacted_range_operation_lag_bucket_audit"
ARTIFACT_VERSION = "operation_lag_bucket_v1_20260714"

PRICE_HISTORY_DIR = ROOT / "data/stock_price_history"
LATEST_CSV = ROOT / f"output/latest/research_backtest/{ARTIFACT_ID}_latest.csv"
DETAIL_CSV = ROOT / f"output/latest/research_backtest/{ARTIFACT_ID}_detail_latest.csv"
LATEST_MD = ROOT / f"output/latest/research_backtest/{ARTIFACT_ID}_latest.md"
HISTORY_CSV = ROOT / f"output/history/research/{ARTIFACT_ID}.csv"
DOCS_CSV = ROOT / f"docs/latest/{ARTIFACT_ID}_latest.csv"
DOCS_MD = ROOT / f"docs/latest/{ARTIFACT_ID}_latest.md"

ADOPTED_LIFECYCLE_POLICY_ID = "rearm_after_realized_exit_next_trade_day"
ADOPTED_CONFIRMATION_VARIANT_ID = "delayed_next_close_continuation_bonus"
ADOPTED_HOLDING_DAYS = 30
ADOPTED_GRID_ID = "|".join(
    (
        ADOPTED_LIFECYCLE_POLICY_ID,
        ADOPTED_CONFIRMATION_VARIANT_ID,
        f"d{ADOPTED_HOLDING_DAYS}",
        NO_STOP_POLICY_ID,
    )
)

PRIMARY_ANALYSIS_BASIS = "primary_candidate_retaining"
SENSITIVITY_ANALYSIS_BASIS = "excluding_unresolved_anomaly_candidates_sensitivity"
TIME_TRAVEL_POLICY = (
    "latest qualifying revenue must be the last qualifying source mapped to a trading day "
    "on or before the operation trigger; later episode updates are ignored"
)
ANOMALY_POLICY = (
    "primary retains unresolved source and operation-return review candidates; exclusion is "
    "reported only as a separately labeled sensitivity"
)
SAMPLE_POLICY = "sample_count_disclosed_not_used_as_automatic_rejection"


@dataclass(frozen=True)
class LagBucket:
    order: int
    bucket_id: str
    label_zh: str
    lower: int
    upper: int | None


LATEST_SOURCE_BUCKETS = (
    LagBucket(10, "latest_lag_d0_20", "距最新合格營收 0 至 20 個交易日", 0, 20),
    LagBucket(20, "latest_lag_d21_40", "距最新合格營收 21 至 40 個交易日", 21, 40),
    LagBucket(30, "latest_lag_d41_60", "距最新合格營收 41 至 60 個交易日", 41, 60),
    LagBucket(40, "latest_lag_d61_90", "距最新合格營收 61 至 90 個交易日", 61, 90),
    LagBucket(50, "latest_lag_d91_126", "距最新合格營收 91 至 126 個交易日", 91, 126),
)

FIRST_SOURCE_BUCKETS = (
    LagBucket(10, "first_lag_d0_20", "距首次合格營收 0 至 20 個交易日", 0, 20),
    LagBucket(20, "first_lag_d21_40", "距首次合格營收 21 至 40 個交易日", 21, 40),
    LagBucket(30, "first_lag_d41_60", "距首次合格營收 41 至 60 個交易日", 41, 60),
    LagBucket(40, "first_lag_d61_90", "距首次合格營收 61 至 90 個交易日", 61, 90),
    LagBucket(50, "first_lag_d91_126", "距首次合格營收 91 至 126 個交易日", 91, 126),
    LagBucket(60, "first_lag_d127_plus", "距首次合格營收 127 個交易日以上", 127, None),
)

LATEST_WATCH_DECISION_BUCKETS = (
    LagBucket(10, "latest_watch_d0_60", "距最新合格營收 0 至 60 個交易日", 0, 60),
    LagBucket(20, "latest_watch_d61_126", "距最新合格營收 61 至 126 個交易日", 61, 126),
)

SUMMARY_COLUMNS = [
    "generated_at",
    "model_id",
    "artifact_id",
    "artifact_version",
    "source_operation_artifact_id",
    "source_operation_artifact_version",
    "source_condition_artifact_id",
    "source_condition_artifact_version",
    "source_variant_id",
    "grid_id",
    "analysis_basis",
    "lag_basis_order",
    "lag_basis_id",
    "lag_basis_label_zh",
    "bucket_order",
    "lag_bucket_id",
    "lag_bucket_label_zh",
    "lag_min_trading_days",
    "lag_max_trading_days",
    "operation_count",
    "unique_stock_count",
    "win_count",
    "neutral_count",
    "failure_count",
    "win_rate_pct",
    "neutral_rate_pct",
    "failure_rate_pct",
    "avg_return_pct",
    "median_return_pct",
    "p10_return_pct",
    "p90_return_pct",
    "return_ge20_count",
    "return_ge20_rate_pct",
    "delta_vs_overall_win_rate_pct_points",
    "delta_vs_overall_avg_return_pct_points",
    "source_anomaly_candidate_count",
    "operation_return_review_candidate_count",
    "future_qualifying_update_ignored_operation_count",
    "same_stock_overlap_pair_count",
    "unclassified_operation_count",
    "time_travel_policy",
    "sample_policy",
    "anomaly_policy",
    "financial_statement_scope",
    "approved_for_daily",
    "production_change",
    "promotion_readiness",
]

DETAIL_COLUMNS = [
    "generated_at",
    "model_id",
    "artifact_id",
    "artifact_version",
    "source_operation_artifact_id",
    "source_operation_artifact_version",
    "source_condition_artifact_id",
    "source_condition_artifact_version",
    "source_variant_id",
    "grid_id",
    "episode_key",
    "stock_id",
    "stock_name",
    "qualifying_update_count",
    "qualifying_revenue_periods",
    "qualifying_source_dates",
    "qualifying_trade_dates",
    "qualifying_sequence_indices",
    "episode_first_qualifying_revenue_period",
    "episode_first_qualifying_source_date",
    "episode_first_qualifying_trade_date",
    "asof_latest_qualifying_revenue_period",
    "asof_latest_qualifying_source_date",
    "asof_latest_qualifying_trade_date",
    "final_episode_latest_qualifying_trade_date",
    "future_qualifying_update_ignored_count",
    "final_episode_latest_after_trigger_flag",
    "trigger_date",
    "confirmation_date",
    "entry_date",
    "exit_date",
    "holding_days",
    "latest_source_to_trigger_trading_days",
    "latest_source_lag_bucket",
    "latest_watch_segment",
    "first_source_to_trigger_trading_days",
    "first_source_lag_bucket",
    "realized_return_pct",
    "return_outcome",
    "realized_return_ge20",
    "source_anomaly_candidate_flag",
    "operation_return_review_candidate_flag",
    "time_travel_guard_passed",
    "same_stock_non_overlap_applied",
    "financial_statement_scope",
    "approved_for_daily",
    "production_change",
]


def _now_text() -> str:
    return datetime.now(ZoneInfo("Asia/Taipei")).strftime("%Y-%m-%d %H:%M:%S Asia/Taipei")


def _bool_value(value: object) -> bool:
    return str(value).strip().lower() in {"true", "1", "yes"}


def _boolish(series: pd.Series) -> pd.Series:
    return series.astype(str).str.strip().str.lower().isin({"true", "1", "yes"})


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
    else:
        raise ValueError(f"unsupported metric method: {method}")
    return round(float(value), 4)


def _split(value: object) -> list[str]:
    return [part for part in str(value).split("|") if part]


def _bucket_id(value: int, buckets: tuple[LagBucket, ...]) -> str:
    for bucket in buckets:
        if value >= bucket.lower and (bucket.upper is None or value <= bucket.upper):
            return bucket.bucket_id
    return ""


def _price_date_indices(stock_id: str, cache: dict[str, dict[str, int]]) -> dict[str, int]:
    if stock_id in cache:
        return cache[stock_id]
    path = PRICE_HISTORY_DIR / f"{stock_id}.csv"
    if not path.is_file():
        raise RuntimeError(f"operation lag bucket price history is missing: {path}")
    dates = pd.read_csv(path, usecols=["date"], dtype={"date": str}, keep_default_na=False)[
        "date"
    ]
    dates = dates.astype(str).str.replace(r"\D", "", regex=True).str[:8]
    dates = dates.loc[dates.str.fullmatch(r"\d{8}")].drop_duplicates().sort_values(
        kind="mergesort"
    )
    cache[stock_id] = {date: index for index, date in enumerate(dates.tolist())}
    return cache[stock_id]


def _selected_operations(operation_detail: pd.DataFrame) -> pd.DataFrame:
    required = {
        "artifact_version",
        "grid_id",
        "source_variant_id",
        "episode_key",
        "stock_id",
        "stock_name",
        "trigger_date",
        "confirmation_date",
        "entry_date",
        "exit_date",
        "holding_days",
        "return_valid",
        "realized_return_pct",
        "return_outcome",
        "realized_return_ge20",
        "source_anomaly_candidate_flag",
        "operation_return_review_candidate_flag",
    }
    missing = sorted(required - set(operation_detail.columns))
    if missing:
        raise RuntimeError(f"operation lag bucket source operation detail is missing: {missing}")
    selected = operation_detail.loc[
        operation_detail["grid_id"].astype(str).eq(ADOPTED_GRID_ID)
        & _boolish(operation_detail["return_valid"])
    ].copy()
    if selected.empty:
        raise RuntimeError("operation lag bucket source grid has no mature operations")
    if set(selected["source_variant_id"].astype(str)) != {SOURCE_VARIANT_ID}:
        raise RuntimeError("operation lag bucket source variant drift")
    if set(selected["artifact_version"].astype(str)) != {SOURCE_OPERATION_ARTIFACT_VERSION}:
        raise RuntimeError("operation lag bucket source operation version drift")
    if selected.duplicated(["grid_id", "stock_id", "episode_key", "trigger_date", "entry_date"]).any():
        raise RuntimeError("operation lag bucket source contains duplicate operations")
    return selected.sort_values(["stock_id", "entry_date"], kind="mergesort").reset_index(
        drop=True
    )


def _source_episodes(source_detail: pd.DataFrame) -> pd.DataFrame:
    required = {
        "artifact_version",
        "condition_variant_id",
        "episode_key",
        "episode_start_revenue_period",
        "episode_start_source_date",
        "episode_start_trade_date",
        "latest_qualifying_trade_date",
        "qualifying_update_count",
        "qualifying_revenue_periods",
        "qualifying_source_dates",
        "qualifying_trade_dates",
        "qualifying_sequence_indices",
    }
    missing = sorted(required - set(source_detail.columns))
    if missing:
        raise RuntimeError(f"operation lag bucket source episode detail is missing: {missing}")
    source = source_detail.loc[
        source_detail["condition_variant_id"].astype(str).eq(SOURCE_VARIANT_ID)
    ].copy()
    if source.empty or source["episode_key"].duplicated().any():
        raise RuntimeError("operation lag bucket source episodes are empty or duplicated")
    if set(source["artifact_version"].astype(str)) != {SOURCE_CONDITION_ARTIFACT_VERSION}:
        raise RuntimeError("operation lag bucket source condition version drift")
    return source.set_index("episode_key", drop=False)


def build_operation_lag_detail(
    operation_detail: pd.DataFrame,
    source_detail: pd.DataFrame,
    generated_at: str | None = None,
) -> pd.DataFrame:
    generated_at = generated_at or _now_text()
    operations = _selected_operations(operation_detail)
    episodes = _source_episodes(source_detail)
    date_cache: dict[str, dict[str, int]] = {}
    rows: list[dict[str, object]] = []
    for operation in operations.itertuples(index=False):
        if operation.episode_key not in episodes.index:
            raise RuntimeError(f"operation lag bucket episode is missing: {operation.episode_key}")
        episode = episodes.loc[operation.episode_key]
        periods = _split(episode["qualifying_revenue_periods"])
        source_dates = _split(episode["qualifying_source_dates"])
        trade_dates = _split(episode["qualifying_trade_dates"])
        try:
            sequence_indices = [int(value) for value in _split(episode["qualifying_sequence_indices"])]
        except ValueError as exc:
            raise RuntimeError(
                f"operation lag bucket qualifying index is invalid: {operation.episode_key}"
            ) from exc
        lengths = {
            len(periods),
            len(source_dates),
            len(trade_dates),
            len(sequence_indices),
            int(episode["qualifying_update_count"]),
        }
        if len(lengths) != 1 or not periods:
            raise RuntimeError(
                f"operation lag bucket qualifying lineage is not aligned: {operation.episode_key}"
            )
        date_indices = _price_date_indices(str(operation.stock_id), date_cache)
        trigger_date = str(operation.trigger_date)
        if trigger_date not in date_indices:
            raise RuntimeError(
                f"operation lag bucket trigger date is absent from price history: "
                f"{operation.stock_id}/{trigger_date}"
            )
        trigger_index = date_indices[trigger_date]
        asof_positions = [
            position
            for position, (trade_date, sequence_index) in enumerate(
                zip(trade_dates, sequence_indices)
            )
            if trade_date <= trigger_date and sequence_index <= trigger_index
        ]
        if not asof_positions:
            raise RuntimeError(
                f"operation lag bucket has no qualifying source known by trigger: "
                f"{operation.episode_key}/{trigger_date}"
            )
        latest_position = asof_positions[-1]
        latest_lag = trigger_index - sequence_indices[latest_position]
        first_lag = trigger_index - sequence_indices[0]
        latest_bucket = _bucket_id(latest_lag, LATEST_SOURCE_BUCKETS)
        latest_watch_segment = _bucket_id(latest_lag, LATEST_WATCH_DECISION_BUCKETS)
        first_bucket = _bucket_id(first_lag, FIRST_SOURCE_BUCKETS)
        if (
            latest_lag < 0
            or latest_lag > DISCOVERY_HORIZON_DAYS
            or not latest_bucket
            or not latest_watch_segment
        ):
            raise RuntimeError(
                f"operation lag bucket latest-source lag is outside the active horizon: "
                f"{operation.episode_key}/{trigger_date}/{latest_lag}"
            )
        if first_lag < 0 or not first_bucket:
            raise RuntimeError(
                f"operation lag bucket first-source lag is invalid: "
                f"{operation.episode_key}/{trigger_date}/{first_lag}"
            )
        future_count = len(periods) - latest_position - 1
        rows.append(
            {
                "generated_at": generated_at,
                "model_id": MODEL_ID,
                "artifact_id": ARTIFACT_ID,
                "artifact_version": ARTIFACT_VERSION,
                "source_operation_artifact_id": SOURCE_OPERATION_ARTIFACT_ID,
                "source_operation_artifact_version": SOURCE_OPERATION_ARTIFACT_VERSION,
                "source_condition_artifact_id": SOURCE_CONDITION_ARTIFACT_ID,
                "source_condition_artifact_version": SOURCE_CONDITION_ARTIFACT_VERSION,
                "source_variant_id": SOURCE_VARIANT_ID,
                "grid_id": ADOPTED_GRID_ID,
                "episode_key": str(operation.episode_key),
                "stock_id": str(operation.stock_id),
                "stock_name": str(operation.stock_name),
                "qualifying_update_count": len(periods),
                "qualifying_revenue_periods": "|".join(periods),
                "qualifying_source_dates": "|".join(source_dates),
                "qualifying_trade_dates": "|".join(trade_dates),
                "qualifying_sequence_indices": "|".join(str(value) for value in sequence_indices),
                "episode_first_qualifying_revenue_period": periods[0],
                "episode_first_qualifying_source_date": source_dates[0],
                "episode_first_qualifying_trade_date": trade_dates[0],
                "asof_latest_qualifying_revenue_period": periods[latest_position],
                "asof_latest_qualifying_source_date": source_dates[latest_position],
                "asof_latest_qualifying_trade_date": trade_dates[latest_position],
                "final_episode_latest_qualifying_trade_date": trade_dates[-1],
                "future_qualifying_update_ignored_count": future_count,
                "final_episode_latest_after_trigger_flag": future_count > 0,
                "trigger_date": trigger_date,
                "confirmation_date": str(operation.confirmation_date),
                "entry_date": str(operation.entry_date),
                "exit_date": str(operation.exit_date),
                "holding_days": int(operation.holding_days),
                "latest_source_to_trigger_trading_days": latest_lag,
                "latest_source_lag_bucket": latest_bucket,
                "latest_watch_segment": latest_watch_segment,
                "first_source_to_trigger_trading_days": first_lag,
                "first_source_lag_bucket": first_bucket,
                "realized_return_pct": round(float(operation.realized_return_pct), 8),
                "return_outcome": str(operation.return_outcome),
                "realized_return_ge20": _bool_value(operation.realized_return_ge20),
                "source_anomaly_candidate_flag": _bool_value(
                    operation.source_anomaly_candidate_flag
                ),
                "operation_return_review_candidate_flag": _bool_value(
                    operation.operation_return_review_candidate_flag
                ),
                "time_travel_guard_passed": trade_dates[latest_position] <= trigger_date,
                "same_stock_non_overlap_applied": True,
                "financial_statement_scope": FINANCIAL_STATEMENT_SCOPE,
                "approved_for_daily": False,
                "production_change": False,
            }
        )
    detail = pd.DataFrame(rows, columns=DETAIL_COLUMNS)
    if detail.empty or not _boolish(detail["time_travel_guard_passed"]).all():
        raise RuntimeError("operation lag bucket time-travel guard failed")
    return detail.sort_values(["stock_id", "entry_date"], kind="mergesort").reset_index(
        drop=True
    )


def _overlap_pair_count(detail: pd.DataFrame) -> int:
    overlaps = 0
    for _stock_id, stock in detail.groupby("stock_id", sort=False):
        ordered = stock.sort_values("entry_date", kind="mergesort")
        previous_exit = ""
        for row in ordered.itertuples(index=False):
            if previous_exit and str(row.entry_date) <= previous_exit:
                overlaps += 1
            previous_exit = max(previous_exit, str(row.exit_date))
    return overlaps


def _summary_row(
    *,
    generated_at: str,
    analysis_basis: str,
    lag_basis_order: int,
    lag_basis_id: str,
    lag_basis_label_zh: str,
    bucket_order: int,
    lag_bucket_id: str,
    lag_bucket_label_zh: str,
    lower: int | str,
    upper: int | str,
    part: pd.DataFrame,
    overall: pd.DataFrame,
    overlap_pair_count: int,
) -> dict[str, object]:
    outcomes = part["return_outcome"].astype(str)
    wins = int(outcomes.eq("win").sum())
    neutral = int(outcomes.eq("neutral").sum())
    failures = int(outcomes.eq("failure").sum())
    count = len(part)
    overall_win_rate = _rate(int(overall["return_outcome"].astype(str).eq("win").sum()), len(overall))
    overall_average = _metric(overall["realized_return_pct"], "mean")
    win_rate = _rate(wins, count)
    average = _metric(part["realized_return_pct"], "mean")
    return {
        "generated_at": generated_at,
        "model_id": MODEL_ID,
        "artifact_id": ARTIFACT_ID,
        "artifact_version": ARTIFACT_VERSION,
        "source_operation_artifact_id": SOURCE_OPERATION_ARTIFACT_ID,
        "source_operation_artifact_version": SOURCE_OPERATION_ARTIFACT_VERSION,
        "source_condition_artifact_id": SOURCE_CONDITION_ARTIFACT_ID,
        "source_condition_artifact_version": SOURCE_CONDITION_ARTIFACT_VERSION,
        "source_variant_id": SOURCE_VARIANT_ID,
        "grid_id": ADOPTED_GRID_ID,
        "analysis_basis": analysis_basis,
        "lag_basis_order": lag_basis_order,
        "lag_basis_id": lag_basis_id,
        "lag_basis_label_zh": lag_basis_label_zh,
        "bucket_order": bucket_order,
        "lag_bucket_id": lag_bucket_id,
        "lag_bucket_label_zh": lag_bucket_label_zh,
        "lag_min_trading_days": lower,
        "lag_max_trading_days": upper,
        "operation_count": count,
        "unique_stock_count": part["stock_id"].nunique(),
        "win_count": wins,
        "neutral_count": neutral,
        "failure_count": failures,
        "win_rate_pct": win_rate,
        "neutral_rate_pct": _rate(neutral, count),
        "failure_rate_pct": _rate(failures, count),
        "avg_return_pct": average,
        "median_return_pct": _metric(part["realized_return_pct"], "median"),
        "p10_return_pct": _metric(part["realized_return_pct"], "p10"),
        "p90_return_pct": _metric(part["realized_return_pct"], "p90"),
        "return_ge20_count": int(_boolish(part["realized_return_ge20"]).sum()),
        "return_ge20_rate_pct": _rate(int(_boolish(part["realized_return_ge20"]).sum()), count),
        "delta_vs_overall_win_rate_pct_points": (
            round(float(win_rate) - float(overall_win_rate), 4)
            if win_rate != "" and overall_win_rate != ""
            else ""
        ),
        "delta_vs_overall_avg_return_pct_points": (
            round(float(average) - float(overall_average), 4)
            if average != "" and overall_average != ""
            else ""
        ),
        "source_anomaly_candidate_count": int(
            _boolish(part["source_anomaly_candidate_flag"]).sum()
        ),
        "operation_return_review_candidate_count": int(
            _boolish(part["operation_return_review_candidate_flag"]).sum()
        ),
        "future_qualifying_update_ignored_operation_count": int(
            pd.to_numeric(
                part["future_qualifying_update_ignored_count"], errors="coerce"
            ).gt(0).sum()
        ),
        "same_stock_overlap_pair_count": overlap_pair_count,
        "unclassified_operation_count": 0,
        "time_travel_policy": TIME_TRAVEL_POLICY,
        "sample_policy": SAMPLE_POLICY,
        "anomaly_policy": ANOMALY_POLICY,
        "financial_statement_scope": FINANCIAL_STATEMENT_SCOPE,
        "approved_for_daily": False,
        "production_change": False,
        "promotion_readiness": "research_only_pending_watch_horizon_selection",
    }


def build_operation_lag_summary(
    detail: pd.DataFrame, generated_at: str | None = None
) -> pd.DataFrame:
    generated_at = generated_at or str(detail["generated_at"].iloc[0])
    overlap_pair_count = _overlap_pair_count(detail)
    if overlap_pair_count:
        raise RuntimeError("operation lag bucket source operations overlap")
    analysis_parts = {
        PRIMARY_ANALYSIS_BASIS: detail.copy(),
        SENSITIVITY_ANALYSIS_BASIS: detail.loc[
            ~_boolish(detail["source_anomaly_candidate_flag"])
            & ~_boolish(detail["operation_return_review_candidate_flag"])
        ].copy(),
    }
    lag_specs = (
        (
            10,
            "latest_qualifying_source_asof_trigger",
            "距觸發日前最新一筆合格營收",
            "latest_source_lag_bucket",
            LATEST_SOURCE_BUCKETS,
        ),
        (
            20,
            "episode_first_qualifying_source",
            "距本次 episode 首次合格營收",
            "first_source_lag_bucket",
            FIRST_SOURCE_BUCKETS,
        ),
        (
            30,
            "latest_qualifying_source_watch_horizon_comparison",
            "最新合格營收觀察期限決策分段",
            "latest_watch_segment",
            LATEST_WATCH_DECISION_BUCKETS,
        ),
    )
    rows: list[dict[str, object]] = []
    for analysis_basis, overall in analysis_parts.items():
        for lag_order, lag_id, lag_label, bucket_column, buckets in lag_specs:
            rows.append(
                _summary_row(
                    generated_at=generated_at,
                    analysis_basis=analysis_basis,
                    lag_basis_order=lag_order,
                    lag_basis_id=lag_id,
                    lag_basis_label_zh=lag_label,
                    bucket_order=0,
                    lag_bucket_id="all",
                    lag_bucket_label_zh="全部已確認交易",
                    lower="",
                    upper="",
                    part=overall,
                    overall=overall,
                    overlap_pair_count=overlap_pair_count,
                )
            )
            for bucket in buckets:
                part = overall.loc[overall[bucket_column].astype(str).eq(bucket.bucket_id)]
                rows.append(
                    _summary_row(
                        generated_at=generated_at,
                        analysis_basis=analysis_basis,
                        lag_basis_order=lag_order,
                        lag_basis_id=lag_id,
                        lag_basis_label_zh=lag_label,
                        bucket_order=bucket.order,
                        lag_bucket_id=bucket.bucket_id,
                        lag_bucket_label_zh=bucket.label_zh,
                        lower=bucket.lower,
                        upper=bucket.upper if bucket.upper is not None else "",
                        part=part,
                        overall=overall,
                        overlap_pair_count=overlap_pair_count,
                    )
                )
            classified = sum(
                int(overall[bucket_column].astype(str).eq(bucket.bucket_id).sum())
                for bucket in buckets
            )
            if classified != len(overall):
                raise RuntimeError(
                    f"operation lag bucket does not conserve operations: "
                    f"{analysis_basis}/{lag_id}/{classified}/{len(overall)}"
                )
    return pd.DataFrame(rows, columns=SUMMARY_COLUMNS).sort_values(
        ["analysis_basis", "lag_basis_order", "bucket_order"], kind="mergesort"
    ).reset_index(drop=True)


def build_operation_lag_bucket_audit(
    operation_detail: pd.DataFrame | None = None,
    source_detail: pd.DataFrame | None = None,
    source_projection_manifest: pd.DataFrame | None = None,
) -> tuple[pd.DataFrame, pd.DataFrame]:
    if operation_detail is None:
        operation_detail = pd.read_csv(
            SOURCE_OPERATION_DETAIL_CSV,
            dtype={"stock_id": str, "trigger_date": str, "entry_date": str, "exit_date": str},
            keep_default_na=False,
            low_memory=False,
        )
    if source_detail is None:
        source_detail = load_projected_source_detail(SOURCE_CONDITION_DETAIL_CSV)
    projection_manifest = (
        load_source_snapshot_projection_manifest()
        if source_projection_manifest is None
        else source_projection_manifest
    )
    validate_projection_binding(
        projection_manifest,
        source_detail,
    )
    generated_at = _now_text()
    detail = build_operation_lag_detail(operation_detail, source_detail, generated_at)
    summary = build_operation_lag_summary(detail, generated_at)
    return summary, detail


def _markdown(summary: pd.DataFrame, detail: pd.DataFrame) -> str:
    columns = [
        "lag_bucket_label_zh",
        "operation_count",
        "win_rate_pct",
        "neutral_rate_pct",
        "failure_rate_pct",
        "avg_return_pct",
        "median_return_pct",
        "return_ge20_rate_pct",
        "delta_vs_overall_win_rate_pct_points",
        "delta_vs_overall_avg_return_pct_points",
    ]
    primary = summary.loc[summary["analysis_basis"].eq(PRIMARY_ANALYSIS_BASIS)]
    sensitivity = summary.loc[
        summary["analysis_basis"].eq(SENSITIVITY_ANALYSIS_BASIS)
    ]
    primary_count = int(
        primary.loc[
            primary["lag_basis_id"].eq("latest_qualifying_source_asof_trigger")
            & primary["lag_bucket_id"].eq("all"),
            "operation_count",
        ].iloc[0]
    )
    sensitivity_count = int(
        sensitivity.loc[
            sensitivity["lag_basis_id"].eq("latest_qualifying_source_asof_trigger")
            & sensitivity["lag_bucket_id"].eq("all"),
            "operation_count",
        ].iloc[0]
    )
    future_ignored = int(
        pd.to_numeric(detail["future_qualifying_update_ignored_count"], errors="coerce")
        .gt(0)
        .sum()
    )
    sections: list[str] = [
        "# 營收低反應區間模型：營收轉強後發動時間差績效稽核",
        "",
        f"- generated_at: `{summary['generated_at'].iloc[0]}`",
        f"- model_id: `{MODEL_ID}`",
        f"- artifact_version: `{ARTIFACT_VERSION}`",
        "- 狀態：research-only，不修改 production registry、正式 operation adapter、PDF 或 ranking。",
        f"- 固定操作口徑：`{ADOPTED_GRID_ID}`。",
        f"- Primary 共 `{primary_count}` 筆；待查資料排除敏感度共 `{sensitivity_count}` 筆。",
        f"- 時間穿越防錯：逐筆只採用 trigger 當日以前已知的最後一筆合格營收；共有 `{future_ignored}` 筆交易忽略 episode 後續才公布的合格營收。",
        "- 最新營收時間桶為 0-20、21-40、41-60、61-90、91-126 個交易日；首次營收另保留 127 日以上桶，確保所有交易不遺漏、不重疊。",
        "- Primary 保留所有待查數字；排除版本只作敏感度，不取代主要結果。",
        f"- 財務資料範圍：`{FINANCIAL_STATEMENT_SCOPE}`。EPS、毛利率、營益率、營業利益、業外、淨利與年報欄位未納入。",
        "",
    ]
    for analysis_basis, frame, title in (
        (PRIMARY_ANALYSIS_BASIS, primary, "Primary：保留待查資料"),
        (SENSITIVITY_ANALYSIS_BASIS, sensitivity, "敏感度：排除待查資料"),
    ):
        sections.extend([f"## {title}", ""])
        for lag_basis_id, lag_title in (
            ("latest_qualifying_source_asof_trigger", "距觸發日前最新一筆合格營收"),
            ("episode_first_qualifying_source", "距本次 episode 首次合格營收"),
        ):
            view = frame.loc[
                frame["lag_basis_id"].eq(lag_basis_id)
                & ~frame["lag_bucket_id"].eq("all"),
                columns,
            ]
            sections.extend([f"### {lag_title}", "", view.to_markdown(index=False), ""])
        decision = frame.loc[
            frame["lag_basis_id"].eq(
                "latest_qualifying_source_watch_horizon_comparison"
            )
            & ~frame["lag_bucket_id"].eq("all"),
            columns,
        ]
        sections.extend(["### 觀察期限決策分段", "", decision.to_markdown(index=False), ""])
    late_review = detail.loc[
        detail["latest_watch_segment"].eq("latest_watch_d61_126")
        & (
            _boolish(detail["source_anomaly_candidate_flag"])
            | _boolish(detail["operation_return_review_candidate_flag"])
        ),
        [
            "stock_id",
            "stock_name",
            "trigger_date",
            "latest_source_to_trigger_trading_days",
            "realized_return_pct",
            "source_anomaly_candidate_flag",
            "operation_return_review_candidate_flag",
        ],
    ]
    sections.extend(
        [
            "## 研究判斷",
            "",
            "- 目前結果支持把 60 個交易日列為下一輪 research-only 觀察期限候選；61 至 126 日另列晚發動研究桶。",
            "- 這不是 promotion：0 至 60 日合併勝率仍未達 60%，且待查數字不得被自動刪除或宣稱已修正。",
            "- episode 首次營收的 127 日以上桶不代表同一筆舊營收仍有效；必須同時查看觸發前最新一筆合格營收，避免忽略期間的月營收更新。",
            "",
            "## 61 至 126 日待查交易",
            "",
            late_review.to_markdown(index=False) if not late_review.empty else "_無待查交易。_",
            "",
        ]
    )
    return "\n".join(sections).rstrip() + "\n"


def write_operation_lag_bucket_audit(summary: pd.DataFrame, detail: pd.DataFrame) -> None:
    for path, frame in (
        (LATEST_CSV, summary),
        (DETAIL_CSV, detail),
        (HISTORY_CSV, summary),
        (DOCS_CSV, summary),
    ):
        path.parent.mkdir(parents=True, exist_ok=True)
        frame.to_csv(path, index=False, encoding="utf-8-sig", lineterminator="\n")
    markdown = _markdown(summary, detail)
    for path in (LATEST_MD, DOCS_MD):
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(markdown, encoding="utf-8", newline="\n")


if __name__ == "__main__":
    built_summary, built_detail = build_operation_lag_bucket_audit()
    write_operation_lag_bucket_audit(built_summary, built_detail)
    print(
        f"wrote {LATEST_CSV.relative_to(ROOT)} rows={len(built_summary)} "
        f"detail_rows={len(built_detail)}"
    )
