from __future__ import annotations

from datetime import datetime
import hashlib
import json
from pathlib import Path
from typing import Callable
from zoneinfo import ZoneInfo

import pandas as pd

from revenue_unreacted_range_monthly_revenue_cross_market_resolution import (
    RESOLUTION_CSV as MONTHLY_REVENUE_CROSS_MARKET_RESOLUTION_CSV,
    canonical_monthly_revenue_history_table_sha256,
)
from revenue_unreacted_range_source_snapshot_projection import (
    CUTOFF_DATE as SOURCE_SNAPSHOT_CUTOFF_DATE,
    LATEST_DETAIL_CSV as SOURCE_SNAPSHOT_DETAIL_CSV,
    LATEST_MANIFEST_CSV as SOURCE_SNAPSHOT_MANIFEST_CSV,
    REVENUE_HISTORY_CSV as MONTHLY_REVENUE_HISTORY,
    load_cutoff_monthly_revenue_subset,
    load_projected_source_detail,
    load_source_snapshot_projection_manifest,
    validate_projection_binding,
    V1_PROJECTION_VERSION,
    V2_PROJECTION_VERSION,
)


ROOT = Path(__file__).resolve().parents[1]
MODEL_ID = "revenue_unreacted_range"
ARTIFACT_ID = "revenue_unreacted_range_lag_strength_matrix"
V1_ARTIFACT_VERSION = "trading_day_lag_strength_root_cause_pending_v5_20260802"
V2_ARTIFACT_VERSION = "trading_day_lag_strength_root_cause_pending_v6_20260822"
ARTIFACT_VERSION = V1_ARTIFACT_VERSION


def artifact_version_for_projection(projection_version: object) -> str:
    version = str(projection_version).strip()
    mapping = {
        V1_PROJECTION_VERSION: V1_ARTIFACT_VERSION,
        V2_PROJECTION_VERSION: V2_ARTIFACT_VERSION,
    }
    if version not in mapping:
        raise RuntimeError(
            f"unsupported canonical source projection version: {version or '<empty>'}"
        )
    return mapping[version]
SOURCE_DETAIL = ROOT / "output/latest/research_backtest/revenue_unreacted_range_fixed_confirmation_feature_contrast_audit_detail_latest.csv"
PRICE_HISTORY_DIR = ROOT / "data/stock_price_history"
LATEST_CSV = ROOT / f"output/latest/research_backtest/{ARTIFACT_ID}_latest.csv"
DETAIL_CSV = ROOT / f"output/latest/research_backtest/{ARTIFACT_ID}_detail_latest.csv"
LATEST_MD = ROOT / f"output/latest/research_backtest/{ARTIFACT_ID}_latest.md"
HISTORY_CSV = ROOT / f"output/history/research/{ARTIFACT_ID}.csv"
DOCS_CSV = ROOT / f"docs/latest/{ARTIFACT_ID}_latest.csv"
DOCS_MD = ROOT / f"docs/latest/{ARTIFACT_ID}_latest.md"

WIN_RETURN_PCT = 5.0
HIGH_RETURN_PCT = 8.0
LARGE_LOSS_PCT = -5.0
ANOMALY_CANDIDATE_ABS_RETURN_PCT = 80.0
MONTHLY_REVENUE_RUNTIME_LINEAGE_COLUMNS = (
    "monthly_revenue_history_blob_sha256",
    "monthly_revenue_canonical_table_sha256",
    "cross_market_resolution_registry_canonical_sha256",
)
SOURCE_SNAPSHOT_LINEAGE_COLUMNS = (
    "source_projection_id",
    "source_projection_version",
    "source_projection_policy_id",
    "source_projection_cutoff_date",
    "source_projection_cutoff_revenue_subset_semantic_sha256",
    "source_projection_cutoff_price_input_semantic_sha256",
    "source_projection_applied_monthly_resolution_semantic_sha256",
    "source_projection_applied_price_resolution_semantic_sha256",
)
FIXED_SOURCE_LINEAGE_COLUMNS = (
    "source_fixed_confirmation_artifact_id",
    "source_fixed_confirmation_artifact_version",
    "source_fixed_confirmation_cutoff_row_count",
    "source_fixed_confirmation_cutoff_semantic_sha256",
)
ALL_LINEAGE_COLUMNS = (
    *MONTHLY_REVENUE_RUNTIME_LINEAGE_COLUMNS,
    *SOURCE_SNAPSHOT_LINEAGE_COLUMNS,
    *FIXED_SOURCE_LINEAGE_COLUMNS,
)
SOURCE_DATE_COLUMNS = (
    "source_monthly_revenue_source_table_date",
    "signal_date",
    "confirmation_date",
    "entry_date",
    "exit_date",
)

CURRENT_LAG_BUCKETS = (
    ("lag_d0_3", "0至3個交易日", 0, 3),
    ("lag_d4_7", "4至7個交易日", 4, 7),
    ("lag_d8_14", "8至14個交易日", 8, 14),
    ("lag_d15_30", "15至30個交易日", 15, 30),
    ("lag_d31_plus", "31個交易日以上", 31, None),
)

STREAK_LAG_BUCKETS = (
    ("streak_lag_d0_7", "連續強勢起點後0至7個交易日", 0, 7),
    ("streak_lag_d8_20", "連續強勢起點後8至20個交易日", 8, 20),
    ("streak_lag_d21_40", "連續強勢起點後21至40個交易日", 21, 40),
    ("streak_lag_d41_80", "連續強勢起點後41至80個交易日", 41, 80),
    ("streak_lag_d81_plus", "連續強勢起點後81個交易日以上", 81, None),
)

SUMMARY_COLUMNS = [
    "generated_at",
    "model_id",
    "artifact_id",
    "artifact_version",
    *ALL_LINEAGE_COLUMNS,
    "matrix_order",
    "matrix_family",
    "condition_test_id",
    "condition_label_zh",
    "condition_rule",
    "current_revenue_lag_bucket",
    "strength_condition_id",
    "feature_observed_count",
    "accepted_trade_count",
    "unique_stock_count",
    "win_count",
    "neutral_count",
    "failure_count",
    "win_rate_pct",
    "neutral_rate_pct",
    "failure_rate_pct",
    "avg_realized_return_pct",
    "median_realized_return_pct",
    "high_return_8_rate_pct",
    "loss_5_rate_pct",
    "abs_ge80_anomaly_candidate_count",
    "source_anomaly_candidate_count",
    "sensitivity_trade_count",
    "sensitivity_win_rate_pct",
    "sensitivity_neutral_rate_pct",
    "sensitivity_failure_rate_pct",
    "sensitivity_avg_realized_return_pct",
    "sensitivity_median_realized_return_pct",
    "delta_vs_baseline_win_rate_pct",
    "delta_vs_baseline_failure_rate_pct",
    "delta_vs_baseline_avg_return_pct",
    "same_stock_overlap_pair_count",
    "same_stock_revenue_period_repeat_count",
    "sample_policy",
    "tail_sensitivity_status",
    "interpretation_status",
    "availability_date_semantics",
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
    *ALL_LINEAGE_COLUMNS,
    "episode_key",
    "stock_id",
    "stock_name",
    "source_monthly_revenue_period",
    "source_monthly_revenue_source_table_date",
    "signal_date",
    "confirmation_date",
    "entry_date",
    "exit_date",
    "source_to_signal_trading_days",
    "source_to_confirmation_trading_days",
    "source_to_entry_trading_days",
    "current_revenue_lag_bucket",
    "latest_revenue_yoy_pct",
    "cumulative_revenue_yoy_pct",
    "previous_1m_latest_revenue_yoy_pct",
    "previous_2m_latest_revenue_yoy_pct",
    "previous_3m_latest_revenue_yoy_pct",
    "latest_revenue_yoy_delta_1m_pct_points",
    "strict_30_20_streak_months",
    "strict_30_20_streak_start_period",
    "strict_30_20_streak_start_source_date",
    "strict_streak_start_to_signal_trading_days",
    "strict_streak_lag_bucket",
    "flag_any_strong_30_or20",
    "flag_latest_ge30",
    "flag_latest_ge50",
    "flag_latest_ge80",
    "flag_latest_ge100",
    "flag_cumulative_ge20",
    "flag_cumulative_ge30",
    "flag_cumulative_ge50",
    "flag_latest30_cumulative20",
    "flag_latest50_cumulative30",
    "flag_latest80_cumulative50",
    "flag_latest100_cumulative80",
    "flag_latest_delta_gt0",
    "flag_latest_delta_ge20",
    "flag_latest_delta_ge50",
    "flag_latest_improving_2m",
    "flag_latest_improving_3m",
    "flag_strict30_20_consecutive_ge2",
    "flag_strict30_20_consecutive_ge3",
    "flag_latest50_consecutive_ge2",
    "flag_latest50_consecutive_ge3",
    "realized_return_pct",
    "outcome_label",
    "abs_ge80_anomaly_candidate_flag",
    "same_stock_non_overlap_applied",
    "revenue_period_dedup_applied",
    "source_revenue_or_price_anomaly_candidate_flag",
    "availability_date_semantics",
    "approved_for_daily",
    "production_change",
]


def _now_text() -> str:
    return datetime.now(ZoneInfo("Asia/Taipei")).strftime("%Y-%m-%d %H:%M:%S Asia/Taipei")


def _boolish(series: pd.Series) -> pd.Series:
    return series.astype(str).str.strip().str.lower().isin({"true", "1", "yes"})


def _numeric(frame: pd.DataFrame, column: str) -> pd.Series:
    return pd.to_numeric(frame.get(column, pd.Series(index=frame.index, dtype=float)), errors="coerce")


def _stable_float(value: object, digits: int = 8) -> float:
    number = pd.to_numeric(value, errors="coerce")
    return float("nan") if pd.isna(number) else round(float(number), digits)


def _rate(numerator: int, denominator: int) -> float | str:
    return round(numerator / denominator * 100.0, 4) if denominator else ""


def _lag_bucket(values: pd.Series, buckets: tuple[tuple[str, str, int, int | None], ...]) -> pd.Series:
    output = pd.Series("", index=values.index, dtype=object)
    for bucket_id, _label, lower, upper in buckets:
        mask = values.ge(lower) & (values.le(upper) if upper is not None else True)
        output.loc[mask] = bucket_id
    return output


def _load_price_dates(stock_id: str, cache: dict[str, pd.Series]) -> pd.Series:
    if stock_id in cache:
        return cache[stock_id]
    path = PRICE_HISTORY_DIR / f"{stock_id}.csv"
    if not path.is_file():
        raise RuntimeError(f"missing stock price history for lag matrix: {path}")
    frame = pd.read_csv(path, usecols=["date"], dtype={"date": str})
    dates = frame["date"].astype(str).str.strip()
    if not dates.str.fullmatch(r"\d{8}").all():
        raise RuntimeError(f"price history {stock_id} contains invalid trading dates")
    dates = dates.loc[dates.le(SOURCE_SNAPSHOT_CUTOFF_DATE)].sort_values()
    duplicate_dates = sorted(dates.loc[dates.duplicated(keep=False)].unique().tolist())
    if duplicate_dates:
        raise RuntimeError(
            f"price history {stock_id} repeats trading dates within cutoff: "
            f"{duplicate_dates[:3]}"
        )
    cache[stock_id] = dates.reset_index(drop=True)
    return cache[stock_id]


def _trading_day_lag(stock_id: str, start_date: str, end_date: str, cache: dict[str, pd.Series]) -> int:
    if (
        not start_date
        or not end_date
        or start_date > end_date
        or end_date > SOURCE_SNAPSHOT_CUTOFF_DATE
    ):
        raise RuntimeError(
            f"invalid lag dates: stock_id={stock_id}; start_date={start_date}; end_date={end_date}"
        )
    dates = _load_price_dates(stock_id, cache)
    return int((dates.gt(start_date) & dates.le(end_date)).sum())


def _source_episodes(source: pd.DataFrame) -> pd.DataFrame:
    required = {
        "research_artifact_id",
        "artifact_version",
        "episode_key",
        "stock_id",
        "source_monthly_revenue_period",
        "source_monthly_revenue_source_table_date",
        "signal_date",
        "confirmation_date",
        "entry_date",
        "exit_date",
        "realized_return_pct",
        "decision_basis",
        "sensitivity_basis",
        "feature_time_basis",
        "source_revenue_or_price_anomaly_candidate_flag",
    }
    missing = sorted(required - set(source.columns))
    if missing:
        raise RuntimeError(f"lag strength source detail missing columns: {missing}")
    mask = (
        _boolish(source["decision_basis"])
        & ~_boolish(source["sensitivity_basis"])
        & source["feature_time_basis"].astype(str).eq("signal_date_close")
    )
    selected = source.loc[mask].copy()
    for column in SOURCE_DATE_COLUMNS:
        values = selected[column].astype(str).str.strip()
        if not values.str.fullmatch(r"\d{8}").all():
            raise RuntimeError(f"lag strength source contains invalid {column}")
        selected[column] = values
    cutoff_mask = pd.Series(True, index=selected.index)
    for column in SOURCE_DATE_COLUMNS:
        cutoff_mask &= selected[column].le(SOURCE_SNAPSHOT_CUTOFF_DATE)
    episodes = selected.loc[cutoff_mask].copy()
    if episodes.empty:
        raise RuntimeError("lag strength source has no fully observed cutoff cohort")
    if episodes["episode_key"].duplicated().any():
        raise RuntimeError("lag strength source contains duplicate episodes")
    repeat = episodes.groupby(["stock_id", "source_monthly_revenue_period"], dropna=False).size()
    if int((repeat - 1).clip(lower=0).sum()) != 0:
        raise RuntimeError("lag strength source repeats a same-stock revenue period")
    return episodes.sort_values(["stock_id", "signal_date"], kind="mergesort").reset_index(drop=True)


_FIXED_SOURCE_SEMANTIC_STRING_COLUMNS = (
    "research_artifact_id",
    "artifact_version",
    "episode_key",
    "stock_id",
    "stock_name",
    "source_monthly_revenue_period",
    "source_monthly_revenue_source_table_date",
    "signal_date",
    "confirmation_date",
    "entry_date",
    "exit_date",
    "feature_time_basis",
)
_FIXED_SOURCE_FILTER_BOOLEAN_COLUMNS = (
    "decision_basis",
    "sensitivity_basis",
)
_FIXED_SOURCE_SEMANTIC_NUMERIC_COLUMNS = (
    "full_monthly_revenue_latest_yoy_pct",
    "full_monthly_revenue_cumulative_yoy_pct",
    "full_monthly_revenue_prev1_latest_yoy_pct",
    "full_monthly_revenue_prev2_latest_yoy_pct",
    "full_monthly_revenue_prev3_latest_yoy_pct",
    "full_monthly_revenue_latest_yoy_delta_1m_pct_points",
)


def _fixed_source_semantic_text(value: object) -> str:
    return "" if pd.isna(value) else str(value).replace("\ufeff", "").strip()


def _fixed_source_semantic_number(value: object) -> str:
    number = _stable_float(value)
    return "" if pd.isna(number) else format(number, ".15g")


def _fixed_source_realized_semantics(value: object) -> tuple[str, str, str]:
    realized = float(pd.to_numeric(value, errors="coerce"))
    rounded = "" if pd.isna(realized) else format(round(realized, 4), ".15g")
    outcome = (
        "win"
        if realized >= WIN_RETURN_PCT
        else "neutral"
        if realized >= 0
        else "failure"
    )
    anomaly = (
        "true"
        if abs(realized) >= ANOMALY_CANDIDATE_ABS_RETURN_PCT
        else "false"
    )
    return rounded, outcome, anomaly


def canonical_fixed_source_slice_sha256(source: pd.DataFrame) -> str:
    required = {
        *_FIXED_SOURCE_SEMANTIC_STRING_COLUMNS,
        *_FIXED_SOURCE_FILTER_BOOLEAN_COLUMNS,
        *_FIXED_SOURCE_SEMANTIC_NUMERIC_COLUMNS,
        "realized_return_pct",
        "source_revenue_or_price_anomaly_candidate_flag",
    } - {"stock_name"}
    missing = sorted(required - set(source.columns))
    if missing:
        raise RuntimeError(
            f"lag strength semantic source is missing consumed columns: {missing}"
        )
    string_columns = tuple(
        column
        for column in _FIXED_SOURCE_SEMANTIC_STRING_COLUMNS
        if column in source.columns
    )
    columns = (
        *string_columns,
        *_FIXED_SOURCE_FILTER_BOOLEAN_COLUMNS,
        "source_revenue_or_price_anomaly_candidate_flag",
        *_FIXED_SOURCE_SEMANTIC_NUMERIC_COLUMNS,
        "realized_return_pct_rounded4",
        "realized_outcome_label",
        "realized_abs_ge80_anomaly_candidate_flag",
    )
    canonical = source.loc[:, list(string_columns)].copy()
    for column in string_columns:
        canonical[column] = canonical[column].map(_fixed_source_semantic_text)
    for column in _FIXED_SOURCE_FILTER_BOOLEAN_COLUMNS:
        canonical[column] = _boolish(source[column]).map(
            lambda value: "true" if value else "false"
        )
    canonical["source_revenue_or_price_anomaly_candidate_flag"] = source[
        "source_revenue_or_price_anomaly_candidate_flag"
    ].map(lambda value: "true" if str(value).lower() == "true" else "false")
    for column in _FIXED_SOURCE_SEMANTIC_NUMERIC_COLUMNS:
        canonical[column] = source[column].map(_fixed_source_semantic_number)
    realized_semantics = source["realized_return_pct"].map(
        _fixed_source_realized_semantics
    )
    canonical["realized_return_pct_rounded4"] = realized_semantics.map(
        lambda values: values[0]
    )
    canonical["realized_outcome_label"] = realized_semantics.map(
        lambda values: values[1]
    )
    canonical["realized_abs_ge80_anomaly_candidate_flag"] = realized_semantics.map(
        lambda values: values[2]
    )
    canonical = canonical.loc[:, list(columns)]
    payload = json.dumps(
        [
            "revenue_lag_fixed_source_consumed_slice_v2",
            list(columns),
            canonical.values.tolist(),
        ],
        ensure_ascii=False,
        separators=(",", ":"),
    ).encode("utf-8")
    return hashlib.sha256(payload).hexdigest()


def _fixed_source_lineage(episodes: pd.DataFrame) -> dict[str, object]:
    if episodes.empty:
        raise RuntimeError("lag strength fixed-confirmation cutoff source is empty")
    artifact_ids = set(episodes["research_artifact_id"].astype(str))
    versions = set(episodes["artifact_version"].astype(str))
    if len(artifact_ids) != 1 or len(versions) != 1:
        raise RuntimeError("lag strength fixed-confirmation source identity is not constant")
    return {
        "source_fixed_confirmation_artifact_id": next(iter(artifact_ids)),
        "source_fixed_confirmation_artifact_version": next(iter(versions)),
        "source_fixed_confirmation_cutoff_row_count": len(episodes),
        "source_fixed_confirmation_cutoff_semantic_sha256": (
            canonical_fixed_source_slice_sha256(episodes)
        ),
    }


def _monthly_revenue_runtime_context(
    source_projection_manifest: pd.DataFrame | None = None,
    projected_source_detail: pd.DataFrame | None = None,
) -> tuple[pd.DataFrame, dict[str, str]]:
    manifest = (
        source_projection_manifest.copy()
        if source_projection_manifest is not None
        else load_source_snapshot_projection_manifest(SOURCE_SNAPSHOT_MANIFEST_CSV)
    )
    projected_detail = (
        projected_source_detail.copy()
        if projected_source_detail is not None
        else load_projected_source_detail(SOURCE_SNAPSHOT_DETAIL_CSV)
    )
    validate_projection_binding(
        manifest,
        projected_detail,
        expected_cutoff_date=SOURCE_SNAPSHOT_CUTOFF_DATE,
    )
    if len(manifest) != 1:
        raise RuntimeError(
            "lag strength source snapshot manifest must contain exactly one row"
        )
    manifest_row = manifest.iloc[0]
    history = load_cutoff_monthly_revenue_subset(
        MONTHLY_REVENUE_HISTORY,
        MONTHLY_REVENUE_CROSS_MARKET_RESOLUTION_CSV,
        cutoff_date=SOURCE_SNAPSHOT_CUTOFF_DATE,
    )
    cutoff_sha = canonical_monthly_revenue_history_table_sha256(history)
    expected_cutoff_sha = str(
        manifest_row["cutoff_revenue_subset_semantic_sha256"]
    ).strip().lower()
    if cutoff_sha != expected_cutoff_sha:
        raise RuntimeError(
            "lag strength cutoff monthly revenue no longer matches source snapshot projection"
        )
    lineage = {
        "monthly_revenue_history_blob_sha256": str(
            manifest_row["monthly_revenue_history_blob_sha256"]
        ).strip().lower(),
        "monthly_revenue_canonical_table_sha256": expected_cutoff_sha,
        "cross_market_resolution_registry_canonical_sha256": str(
            manifest_row["cross_market_resolution_registry_canonical_sha256"]
        ).strip().lower(),
        "source_projection_id": str(manifest_row["projection_id"]),
        "source_projection_version": str(manifest_row["projection_version"]),
        "source_projection_policy_id": str(manifest_row["projection_policy_id"]),
        "source_projection_cutoff_date": str(manifest_row["cutoff_date"]),
        "source_projection_cutoff_revenue_subset_semantic_sha256": expected_cutoff_sha,
        "source_projection_cutoff_price_input_semantic_sha256": str(
            manifest_row["cutoff_price_input_semantic_sha256"]
        ).strip().lower(),
        "source_projection_applied_monthly_resolution_semantic_sha256": str(
            manifest_row["applied_monthly_resolution_semantic_sha256"]
        ).strip().lower(),
        "source_projection_applied_price_resolution_semantic_sha256": str(
            manifest_row["applied_price_resolution_semantic_sha256"]
        ).strip().lower(),
    }
    return history, lineage


def _monthly_history_lookup(
    history: pd.DataFrame | None = None,
) -> dict[str, dict[str, dict[str, object]]]:
    if history is None:
        history, _lineage = _monthly_revenue_runtime_context()
    if history.duplicated(["stock_id", "revenue_period"]).any():
        raise RuntimeError("monthly revenue history contains duplicate stock-period rows")
    lookup: dict[str, dict[str, dict[str, object]]] = {}
    for row in history.itertuples(index=False):
        stock_id = str(row.stock_id).zfill(4)
        period = str(row.revenue_period)
        lookup.setdefault(stock_id, {})[period] = {
            "source_table_date": str(row.source_table_date),
            "latest": pd.to_numeric(row.latest_revenue_yoy_pct, errors="coerce"),
            "cumulative": pd.to_numeric(row.cumulative_revenue_yoy_pct, errors="coerce"),
        }
    return lookup


def _previous_period(period: str) -> str:
    return (pd.Period(period, freq="M") - 1).strftime("%Y%m")


def _strict_streak(
    stock_id: str,
    current_period: str,
    lookup: dict[str, dict[str, dict[str, object]]],
) -> tuple[int, str, str]:
    stock_history = lookup.get(stock_id, {})
    period = current_period
    streak = 0
    start_period = ""
    start_date = ""
    for _ in range(12):
        row = stock_history.get(period)
        if not row:
            break
        latest = pd.to_numeric(row["latest"], errors="coerce")
        cumulative = pd.to_numeric(row["cumulative"], errors="coerce")
        if pd.isna(latest) or pd.isna(cumulative) or latest < 30.0 or cumulative < 20.0:
            break
        streak += 1
        start_period = period
        start_date = str(row["source_table_date"])
        period = _previous_period(period)
    return streak, start_period, start_date


def build_lag_strength_detail(
    source: pd.DataFrame,
    *,
    source_projection_manifest: pd.DataFrame | None = None,
    projected_source_detail: pd.DataFrame | None = None,
) -> pd.DataFrame:
    episodes = _source_episodes(source)
    fixed_source_lineage = _fixed_source_lineage(episodes)
    generated_at = _now_text()
    price_cache: dict[str, pd.Series] = {}
    monthly_revenue_history, runtime_lineage = _monthly_revenue_runtime_context(
        source_projection_manifest,
        projected_source_detail,
    )
    revenue_lookup = _monthly_history_lookup(monthly_revenue_history)
    rows: list[dict[str, object]] = []
    for episode in episodes.itertuples(index=False):
        stock_id = str(episode.stock_id).zfill(4)
        source_date = str(episode.source_monthly_revenue_source_table_date)
        signal_date = str(episode.signal_date)
        confirmation_date = str(episode.confirmation_date)
        entry_date = str(episode.entry_date)
        current_period = str(episode.source_monthly_revenue_period)
        latest = _stable_float(episode.full_monthly_revenue_latest_yoy_pct)
        cumulative = _stable_float(episode.full_monthly_revenue_cumulative_yoy_pct)
        prev1 = _stable_float(episode.full_monthly_revenue_prev1_latest_yoy_pct)
        prev2 = _stable_float(episode.full_monthly_revenue_prev2_latest_yoy_pct)
        prev3 = _stable_float(episode.full_monthly_revenue_prev3_latest_yoy_pct)
        delta = _stable_float(episode.full_monthly_revenue_latest_yoy_delta_1m_pct_points)
        source_to_signal = _trading_day_lag(stock_id, source_date, signal_date, price_cache)
        streak, streak_start_period, streak_start_date = _strict_streak(stock_id, current_period, revenue_lookup)
        streak_lag = (
            _trading_day_lag(stock_id, streak_start_date, signal_date, price_cache)
            if streak_start_date
            else pd.NA
        )
        realized = float(pd.to_numeric(episode.realized_return_pct, errors="coerce"))
        strict_current = bool(pd.notna(latest) and pd.notna(cumulative) and latest >= 30 and cumulative >= 20)
        row = {
            "generated_at": generated_at,
            "model_id": MODEL_ID,
            "artifact_id": ARTIFACT_ID,
            "artifact_version": ARTIFACT_VERSION,
            **runtime_lineage,
            **fixed_source_lineage,
            "episode_key": str(episode.episode_key),
            "stock_id": stock_id,
            "stock_name": str(getattr(episode, "stock_name", "")),
            "source_monthly_revenue_period": current_period,
            "source_monthly_revenue_source_table_date": source_date,
            "signal_date": signal_date,
            "confirmation_date": confirmation_date,
            "entry_date": entry_date,
            "exit_date": str(episode.exit_date),
            "source_to_signal_trading_days": source_to_signal,
            "source_to_confirmation_trading_days": _trading_day_lag(stock_id, source_date, confirmation_date, price_cache),
            "source_to_entry_trading_days": _trading_day_lag(stock_id, source_date, entry_date, price_cache),
            "current_revenue_lag_bucket": "",
            "latest_revenue_yoy_pct": latest,
            "cumulative_revenue_yoy_pct": cumulative,
            "previous_1m_latest_revenue_yoy_pct": prev1,
            "previous_2m_latest_revenue_yoy_pct": prev2,
            "previous_3m_latest_revenue_yoy_pct": prev3,
            "latest_revenue_yoy_delta_1m_pct_points": delta,
            "strict_30_20_streak_months": streak,
            "strict_30_20_streak_start_period": streak_start_period,
            "strict_30_20_streak_start_source_date": streak_start_date,
            "strict_streak_start_to_signal_trading_days": streak_lag,
            "strict_streak_lag_bucket": "",
            "flag_any_strong_30_or20": bool(pd.notna(latest) and pd.notna(cumulative) and (latest >= 30 or cumulative >= 20)),
            "flag_latest_ge30": bool(pd.notna(latest) and latest >= 30),
            "flag_latest_ge50": bool(pd.notna(latest) and latest >= 50),
            "flag_latest_ge80": bool(pd.notna(latest) and latest >= 80),
            "flag_latest_ge100": bool(pd.notna(latest) and latest >= 100),
            "flag_cumulative_ge20": bool(pd.notna(cumulative) and cumulative >= 20),
            "flag_cumulative_ge30": bool(pd.notna(cumulative) and cumulative >= 30),
            "flag_cumulative_ge50": bool(pd.notna(cumulative) and cumulative >= 50),
            "flag_latest30_cumulative20": strict_current,
            "flag_latest50_cumulative30": bool(pd.notna(latest) and pd.notna(cumulative) and latest >= 50 and cumulative >= 30),
            "flag_latest80_cumulative50": bool(pd.notna(latest) and pd.notna(cumulative) and latest >= 80 and cumulative >= 50),
            "flag_latest100_cumulative80": bool(pd.notna(latest) and pd.notna(cumulative) and latest >= 100 and cumulative >= 80),
            "flag_latest_delta_gt0": bool(pd.notna(delta) and delta > 0),
            "flag_latest_delta_ge20": bool(pd.notna(delta) and delta >= 20),
            "flag_latest_delta_ge50": bool(pd.notna(delta) and delta >= 50),
            "flag_latest_improving_2m": bool(pd.notna(latest) and pd.notna(prev1) and pd.notna(prev2) and latest > prev1 > prev2),
            "flag_latest_improving_3m": bool(pd.notna(latest) and pd.notna(prev1) and pd.notna(prev2) and pd.notna(prev3) and latest > prev1 > prev2 > prev3),
            "flag_strict30_20_consecutive_ge2": streak >= 2,
            "flag_strict30_20_consecutive_ge3": streak >= 3,
            "flag_latest50_consecutive_ge2": bool(pd.notna(latest) and pd.notna(prev1) and latest >= 50 and prev1 >= 50),
            "flag_latest50_consecutive_ge3": bool(pd.notna(latest) and pd.notna(prev1) and pd.notna(prev2) and latest >= 50 and prev1 >= 50 and prev2 >= 50),
            "realized_return_pct": round(realized, 4),
            "outcome_label": "win" if realized >= WIN_RETURN_PCT else "neutral" if realized >= 0 else "failure",
            "abs_ge80_anomaly_candidate_flag": (
                abs(realized) >= ANOMALY_CANDIDATE_ABS_RETURN_PCT
            ),
            "same_stock_non_overlap_applied": True,
            "revenue_period_dedup_applied": True,
            "source_revenue_or_price_anomaly_candidate_flag": bool(
                str(episode.source_revenue_or_price_anomaly_candidate_flag).lower() == "true"
            ),
            "availability_date_semantics": "conservative_next_month_17th_or_first_official_snapshot_not_exact_company_release_timestamp",
            "approved_for_daily": False,
            "production_change": False,
        }
        rows.append(row)
    detail = pd.DataFrame(rows)
    detail["current_revenue_lag_bucket"] = _lag_bucket(
        pd.to_numeric(detail["source_to_signal_trading_days"], errors="coerce"), CURRENT_LAG_BUCKETS
    )
    detail["strict_streak_lag_bucket"] = _lag_bucket(
        pd.to_numeric(detail["strict_streak_start_to_signal_trading_days"], errors="coerce"),
        STREAK_LAG_BUCKETS,
    )
    return detail[DETAIL_COLUMNS].sort_values(["stock_id", "signal_date"], kind="mergesort").reset_index(drop=True)


STRENGTH_SPECS: tuple[tuple[str, str, str, str], ...] = (
    ("absolute_strength", "any_strong_30_or20", "單月YoY至少30%或累計YoY至少20%", "flag_any_strong_30_or20"),
    ("absolute_strength", "latest_ge30", "單月YoY至少30%", "flag_latest_ge30"),
    ("absolute_strength", "latest_ge50", "單月YoY至少50%", "flag_latest_ge50"),
    ("absolute_strength", "latest_ge80", "單月YoY至少80%", "flag_latest_ge80"),
    ("absolute_strength", "latest_ge100", "單月YoY至少100%", "flag_latest_ge100"),
    ("absolute_strength", "cumulative_ge20", "累計YoY至少20%", "flag_cumulative_ge20"),
    ("absolute_strength", "cumulative_ge30", "累計YoY至少30%", "flag_cumulative_ge30"),
    ("absolute_strength", "cumulative_ge50", "累計YoY至少50%", "flag_cumulative_ge50"),
    ("absolute_strength", "latest30_cumulative20", "單月YoY至少30%且累計YoY至少20%", "flag_latest30_cumulative20"),
    ("absolute_strength", "latest50_cumulative30", "單月YoY至少50%且累計YoY至少30%", "flag_latest50_cumulative30"),
    ("absolute_strength", "latest80_cumulative50", "單月YoY至少80%且累計YoY至少50%", "flag_latest80_cumulative50"),
    ("absolute_strength", "latest100_cumulative80", "單月YoY至少100%且累計YoY至少80%", "flag_latest100_cumulative80"),
    ("acceleration", "latest_delta_gt0", "單月YoY較前月改善", "flag_latest_delta_gt0"),
    ("acceleration", "latest_delta_ge20", "單月YoY月增幅至少20個百分點", "flag_latest_delta_ge20"),
    ("acceleration", "latest_delta_ge50", "單月YoY月增幅至少50個百分點", "flag_latest_delta_ge50"),
    ("acceleration", "latest_improving_2m", "單月YoY連續兩段改善", "flag_latest_improving_2m"),
    ("acceleration", "latest_improving_3m", "單月YoY連續三段改善", "flag_latest_improving_3m"),
    ("persistence", "strict30_20_consecutive_ge2", "30/20嚴格強勢至少連續2個月", "flag_strict30_20_consecutive_ge2"),
    ("persistence", "strict30_20_consecutive_ge3", "30/20嚴格強勢至少連續3個月", "flag_strict30_20_consecutive_ge3"),
    ("persistence", "latest50_consecutive_ge2", "單月YoY至少50%連續2個月", "flag_latest50_consecutive_ge2"),
    ("persistence", "latest50_consecutive_ge3", "單月YoY至少50%連續3個月", "flag_latest50_consecutive_ge3"),
)


def _metrics(frame: pd.DataFrame) -> dict[str, object]:
    realized = pd.to_numeric(frame["realized_return_pct"], errors="coerce").dropna()
    count = len(realized)
    wins = int(realized.ge(WIN_RETURN_PCT).sum())
    neutral = int((realized.ge(0) & realized.lt(WIN_RETURN_PCT)).sum())
    failure = int(realized.lt(0).sum())
    return {
        "accepted_trade_count": count,
        "unique_stock_count": int(frame.loc[realized.index, "stock_id"].nunique()) if count else 0,
        "win_count": wins,
        "neutral_count": neutral,
        "failure_count": failure,
        "win_rate_pct": _rate(wins, count),
        "neutral_rate_pct": _rate(neutral, count),
        "failure_rate_pct": _rate(failure, count),
        "avg_realized_return_pct": round(float(realized.mean()), 4) if count else "",
        "median_realized_return_pct": round(float(realized.median()), 4) if count else "",
        "high_return_8_rate_pct": _rate(int(realized.ge(HIGH_RETURN_PCT).sum()), count),
        "loss_5_rate_pct": _rate(int(realized.le(LARGE_LOSS_PCT).sum()), count),
        "abs_ge80_anomaly_candidate_count": int(
            realized.abs().ge(ANOMALY_CANDIDATE_ABS_RETURN_PCT).sum()
        ),
        "source_anomaly_candidate_count": int(
            _boolish(frame.loc[realized.index, "source_revenue_or_price_anomaly_candidate_flag"]).sum()
        ),
    }


def _number(value: object) -> float | None:
    number = pd.to_numeric(value, errors="coerce")
    return None if pd.isna(number) else float(number)


def _interpret(metrics: dict[str, object], sensitivity: dict[str, object]) -> tuple[str, str]:
    if not metrics["accepted_trade_count"]:
        return "no_sample", "not_applicable"
    base_values = [_number(metrics[key]) for key in ("win_rate_pct", "avg_realized_return_pct", "median_realized_return_pct")]
    sensitivity_values = [
        _number(sensitivity[key])
        for key in ("win_rate_pct", "avg_realized_return_pct", "median_realized_return_pct")
    ]
    including_meets = all(value is not None for value in base_values) and base_values[0] >= 60 and base_values[1] > 0 and base_values[2] > 0
    excluding_meets = all(value is not None for value in sensitivity_values) and sensitivity_values[0] >= 60 and sensitivity_values[1] > 0 and sensitivity_values[2] > 0
    if including_meets and excluding_meets:
        return "provisional_meets_60pct_positive_return_both_threshold_bases", "not_tail_dependent"
    if including_meets and not excluding_meets:
        return "including_candidates_meets_but_threshold_sensitivity_fails", "tail_dependent"
    return "does_not_meet_60pct_positive_return_package", "not_candidate_or_inconclusive"


def _summary_row(
    detail: pd.DataFrame,
    *,
    order: int,
    family: str,
    test_id: str,
    label: str,
    rule: str,
    mask: pd.Series,
    observed_mask: pd.Series,
    current_lag_bucket: str,
    strength_condition_id: str,
    baseline_metrics: dict[str, object],
) -> dict[str, object]:
    selected = detail.loc[mask.fillna(False)]
    metrics = _metrics(selected)
    sensitivity = _metrics(selected.loc[~_boolish(selected["abs_ge80_anomaly_candidate_flag"])])
    interpretation, tail_status = _interpret(metrics, sensitivity)
    if (
        int(metrics["abs_ge80_anomaly_candidate_count"]) > 0
        or int(metrics["source_anomaly_candidate_count"]) > 0
    ):
        interpretation = "blocked_pending_root_cause_anomaly_candidate_review"
        tail_status = "source_or_return_candidates_unresolved"

    def delta(metric_key: str) -> float | str:
        current = _number(metrics[metric_key])
        baseline = _number(baseline_metrics[metric_key])
        return round(current - baseline, 4) if current is not None and baseline is not None else ""

    return {
        "generated_at": str(detail["generated_at"].iloc[0]),
        "model_id": MODEL_ID,
        "artifact_id": ARTIFACT_ID,
        "artifact_version": ARTIFACT_VERSION,
        **{
            column: str(detail[column].iloc[0])
            for column in ALL_LINEAGE_COLUMNS
        },
        "matrix_order": order,
        "matrix_family": family,
        "condition_test_id": test_id,
        "condition_label_zh": label,
        "condition_rule": rule,
        "current_revenue_lag_bucket": current_lag_bucket,
        "strength_condition_id": strength_condition_id,
        "feature_observed_count": int(observed_mask.fillna(False).sum()),
        **metrics,
        "sensitivity_trade_count": sensitivity["accepted_trade_count"],
        "sensitivity_win_rate_pct": sensitivity["win_rate_pct"],
        "sensitivity_neutral_rate_pct": sensitivity["neutral_rate_pct"],
        "sensitivity_failure_rate_pct": sensitivity["failure_rate_pct"],
        "sensitivity_avg_realized_return_pct": sensitivity["avg_realized_return_pct"],
        "sensitivity_median_realized_return_pct": sensitivity["median_realized_return_pct"],
        "delta_vs_baseline_win_rate_pct": delta("win_rate_pct"),
        "delta_vs_baseline_failure_rate_pct": delta("failure_rate_pct"),
        "delta_vs_baseline_avg_return_pct": delta("avg_realized_return_pct"),
        "same_stock_overlap_pair_count": 0,
        "same_stock_revenue_period_repeat_count": 0,
        "sample_policy": "sample_count_disclosed_not_used_as_automatic_rejection",
        "tail_sensitivity_status": tail_status,
        "interpretation_status": interpretation,
        "availability_date_semantics": "conservative_next_month_17th_or_first_official_snapshot_not_exact_company_release_timestamp",
        "financial_statement_scope": "monthly_revenue_only;EPS_gross_margin_operating_margin_operating_income_non_operating_income_net_income_excluded",
        "approved_for_daily": False,
        "production_change": False,
        "promotion_readiness": "blocked_pending_root_cause_anomaly_candidate_review",
    }


def build_lag_strength_summary(detail: pd.DataFrame) -> pd.DataFrame:
    if detail.empty:
        return pd.DataFrame(columns=SUMMARY_COLUMNS)
    all_rows = pd.Series(True, index=detail.index)
    baseline_metrics = _metrics(detail)
    rows: list[dict[str, object]] = []
    rows.append(
        _summary_row(
            detail,
            order=0,
            family="baseline",
            test_id="all_confirmed_non_overlap",
            label="全部已確認且同股不重疊樣本",
            rule="fixed 3-trading-day close confirmation; next open entry; confirmation D+20 close exit",
            mask=all_rows,
            observed_mask=all_rows,
            current_lag_bucket="all",
            strength_condition_id="all",
            baseline_metrics=baseline_metrics,
        )
    )
    order = 100
    for bucket_id, label, lower, upper in CURRENT_LAG_BUCKETS:
        mask = detail["current_revenue_lag_bucket"].eq(bucket_id)
        rule = f"source_to_signal_trading_days between {lower} and {upper if upper is not None else 'infinity'}"
        rows.append(
            _summary_row(
                detail,
                order=order,
                family="current_revenue_trading_day_lag",
                test_id=bucket_id,
                label=f"當期營收可得日後{label}",
                rule=rule,
                mask=mask,
                observed_mask=all_rows,
                current_lag_bucket=bucket_id,
                strength_condition_id="all",
                baseline_metrics=baseline_metrics,
            )
        )
        order += 1

    order = 200
    strength_masks: dict[str, pd.Series] = {}
    for family, test_id, label, flag_column in STRENGTH_SPECS:
        mask = _boolish(detail[flag_column])
        strength_masks[test_id] = mask
        observed = detail["latest_revenue_yoy_pct"].notna()
        if "cumulative" in test_id or "strict" in test_id or test_id == "any_strong_30_or20":
            observed &= detail["cumulative_revenue_yoy_pct"].notna()
        rows.append(
            _summary_row(
                detail,
                order=order,
                family=family,
                test_id=test_id,
                label=label,
                rule=f"{flag_column}=True",
                mask=mask,
                observed_mask=observed,
                current_lag_bucket="all",
                strength_condition_id=test_id,
                baseline_metrics=baseline_metrics,
            )
        )
        order += 1

    order = 1000
    for bucket_id, bucket_label, lower, upper in CURRENT_LAG_BUCKETS:
        lag_mask = detail["current_revenue_lag_bucket"].eq(bucket_id)
        for family, test_id, label, _flag_column in STRENGTH_SPECS:
            mask = lag_mask & strength_masks[test_id]
            rows.append(
                _summary_row(
                    detail,
                    order=order,
                    family="lag_x_strength",
                    test_id=f"{bucket_id}__{test_id}",
                    label=f"{bucket_label}；{label}",
                    rule=(
                        f"current_revenue_lag_bucket={bucket_id} AND strength_condition_id={test_id}"
                    ),
                    mask=mask,
                    observed_mask=lag_mask,
                    current_lag_bucket=bucket_id,
                    strength_condition_id=test_id,
                    baseline_metrics=baseline_metrics,
                )
            )
            order += 1

    order = 2000
    for bucket_id, label, lower, upper in STREAK_LAG_BUCKETS:
        mask = detail["strict_streak_lag_bucket"].eq(bucket_id)
        observed = detail["strict_30_20_streak_months"].ge(1)
        rows.append(
            _summary_row(
                detail,
                order=order,
                family="strict_strength_streak_start_lag",
                test_id=bucket_id,
                label=label,
                rule=f"strict_streak_start_to_signal_trading_days between {lower} and {upper if upper is not None else 'infinity'}",
                mask=mask,
                observed_mask=observed,
                current_lag_bucket="all",
                strength_condition_id="strict30_20_streak",
                baseline_metrics=baseline_metrics,
            )
        )
        order += 1
    return pd.DataFrame(rows, columns=SUMMARY_COLUMNS).sort_values("matrix_order").reset_index(drop=True)


def build_lag_strength_matrix(
    source: pd.DataFrame,
    *,
    source_projection_manifest: pd.DataFrame | None = None,
    projected_source_detail: pd.DataFrame | None = None,
) -> tuple[pd.DataFrame, pd.DataFrame]:
    detail = build_lag_strength_detail(
        source,
        source_projection_manifest=source_projection_manifest,
        projected_source_detail=projected_source_detail,
    )
    summary = build_lag_strength_summary(detail)
    versions = set(detail["source_projection_version"].astype(str).str.strip())
    if len(versions) != 1:
        raise RuntimeError("lag strength source projection version is not constant")
    selected_version = artifact_version_for_projection(next(iter(versions)))
    summary.loc[:, "artifact_version"] = selected_version
    detail.loc[:, "artifact_version"] = selected_version
    return summary, detail


def _markdown(summary: pd.DataFrame) -> str:
    candidate = summary[
        summary["interpretation_status"].isin(
            {
                "provisional_meets_60pct_positive_return_both_threshold_bases",
                "including_candidates_meets_but_threshold_sensitivity_fails",
                "blocked_pending_root_cause_anomaly_candidate_review",
            }
        )
    ].copy()
    display_columns = [
        "matrix_family",
        "condition_label_zh",
        "accepted_trade_count",
        "win_rate_pct",
        "neutral_rate_pct",
        "failure_rate_pct",
        "avg_realized_return_pct",
        "median_realized_return_pct",
        "sensitivity_win_rate_pct",
        "sensitivity_avg_realized_return_pct",
        "tail_sensitivity_status",
        "interpretation_status",
    ]
    lines = [
        "# 營收低反應模型：反應時間差與營收強度矩陣",
        "",
        f"- artifact_version: `{summary['artifact_version'].iloc[0]}`",
        "- source sample: 固定 3 個交易日收盤確認、確認後下一交易日開盤進場、確認日 D+20 收盤出場。",
        "- outcome: 勝為報酬至少 +5%；和為 0% 至未滿 +5%；敗為負報酬。",
        "- dedup: 同股持有區間不得重疊；同股同一營收月份只接受一筆。",
        "- lag basis: 股票本身可交易日，而非曆日。",
        "- availability caveat: 歷史回填採保守次月 17 日，最新資料採第一個官方 snapshot；不是公司實際發布時分。",
        "- anomaly candidate: abs >= 80% 只觸發待查列，不能直接判定極端值、錯價或非可比事件。",
        "- threshold sensitivity: 主樣本保留候選列並另列門檻排除結果；排除結果不是修正後績效。",
        "- promotion gate: 14 筆候選仍缺完整底層根因證據，本矩陣全部維持 blocked。",
        "- sample rule: 樣本少不會自動否決，但樣本數必須完整揭露。",
        "- scope: 僅月營收；EPS、毛利率、營益率、營業利益、業外與淨利未納入。",
        "- status: research-only；不修改 production registry、operation adapter、ranking、PDF 或 snapshots。",
        "",
        "## 達到六成與正報酬門檻的研究列",
        "",
        candidate[display_columns].to_markdown(index=False) if not candidate.empty else "目前沒有符合列。",
        "",
        "## 基準與單一維度",
        "",
        summary[summary["matrix_family"].ne("lag_x_strength")][display_columns].to_markdown(index=False),
        "",
    ]
    return "\n".join(lines)


def write_lag_strength_matrix(summary: pd.DataFrame, detail: pd.DataFrame) -> None:
    for path, frame in (
        (LATEST_CSV, summary),
        (DETAIL_CSV, detail),
        (HISTORY_CSV, summary),
        (DOCS_CSV, summary),
    ):
        path.parent.mkdir(parents=True, exist_ok=True)
        frame.to_csv(path, index=False, encoding="utf-8-sig", lineterminator="\n")
    markdown = _markdown(summary)
    for path in (LATEST_MD, DOCS_MD):
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(markdown, encoding="utf-8", newline="\n")
