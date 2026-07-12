from __future__ import annotations

from datetime import datetime
import math
from pathlib import Path
from typing import Callable
from zoneinfo import ZoneInfo

import numpy as np
import pandas as pd


ROOT = Path(__file__).resolve().parents[1]
MODEL_ID = "revenue_unreacted_range"
ARTIFACT_ID = "revenue_unreacted_range_launch_timing_feature_audit"
ARTIFACT_VERSION = "launch_timing_breakout_feature_v2_20260713"

SOURCE_DETAIL = (
    ROOT
    / "output/latest/research_backtest/"
    "revenue_unreacted_range_lag_strength_matrix_detail_latest.csv"
)
LATEST_CSV = ROOT / f"output/latest/research_backtest/{ARTIFACT_ID}_latest.csv"
DETAIL_CSV = ROOT / f"output/latest/research_backtest/{ARTIFACT_ID}_detail_latest.csv"
FEATURE_CSV = ROOT / f"output/latest/research_backtest/{ARTIFACT_ID}_feature_contrast_latest.csv"
LATEST_MD = ROOT / f"output/latest/research_backtest/{ARTIFACT_ID}_latest.md"
HISTORY_CSV = ROOT / f"output/history/research/{ARTIFACT_ID}.csv"
HISTORY_FEATURE_CSV = ROOT / f"output/history/research/{ARTIFACT_ID}_feature_contrast.csv"
DOCS_CSV = ROOT / f"docs/latest/{ARTIFACT_ID}_latest.csv"
DOCS_FEATURE_CSV = ROOT / f"docs/latest/{ARTIFACT_ID}_feature_contrast_latest.csv"
DOCS_MD = ROOT / f"docs/latest/{ARTIFACT_ID}_latest.md"
PRICE_COMPARABILITY_RESOLUTION_CSV = (
    ROOT / "config/revenue_unreacted_range_price_comparability_resolution.csv"
)

OUTCOME_WINDOW_DAYS = 20
SIX_MONTH_HORIZON_DAYS = 126
MAX_DISCOVERY_DAYS = 252
FULL_OBSERVATION_NON_OVERLAP_DAYS = MAX_DISCOVERY_DAYS + OUTCOME_WINDOW_DAYS
MIN_POST_HIT_OBSERVATION_DAYS = 5
HORIZONS = (20, 40, 60, 80, 100, 126, 168, 252)

PRIMARY_ANALYSIS_BASIS = "primary_candidate_retaining"
SENSITIVITY_ANALYSIS_BASIS = "legacy_candidate_exclusion_sensitivity_only"
PRIMARY_TRIGGER_ID = "close_breakout_prev20"
PRIMARY_OUTCOME_ID = "hit20_by15_hold20_to_d20"

AVAILABILITY_SEMANTICS = (
    "conservative_next_month_17th_or_first_official_snapshot_not_exact_company_release_timestamp"
)
FINANCIAL_STATEMENT_SCOPE = (
    "monthly_revenue_only;EPS_gross_margin_operating_margin_operating_income_"
    "non_operating_income_net_income_excluded"
)

ANALYSIS_BASES = (
    PRIMARY_ANALYSIS_BASIS,
    SENSITIVITY_ANALYSIS_BASIS,
)

OUTCOME_SPECS = (
    {
        "outcome_definition_id": "d20_close_ge20",
        "outcome_label_zh": "發動後第 20 個交易日收盤仍上漲至少 20%",
        "first_hit_deadline": OUTCOME_WINDOW_DAYS,
        "post_hit_floor_return": None,
    },
    {
        "outcome_definition_id": "hit20_by15_retain10_to_d20",
        "outcome_label_zh": "15 日內收盤達 +20%，之後至 D+20 守住 +10%，且 D+20 仍達 +20%",
        "first_hit_deadline": OUTCOME_WINDOW_DAYS - MIN_POST_HIT_OBSERVATION_DAYS,
        "post_hit_floor_return": 0.10,
    },
    {
        "outcome_definition_id": PRIMARY_OUTCOME_ID,
        "outcome_label_zh": "15 日內收盤達 +20%，之後至 D+20 每日收盤都不跌回 +20% 以下",
        "first_hit_deadline": OUTCOME_WINDOW_DAYS - MIN_POST_HIT_OBSERVATION_DAYS,
        "post_hit_floor_return": 0.20,
    },
)

TRIGGER_SPECS = (
    {
        "trigger_id": "no_breakout_requirement",
        "trigger_label_zh": "只找可持續上漲起點，不要求高點突破",
        "window": 0,
    },
    {
        "trigger_id": PRIMARY_TRIGGER_ID,
        "trigger_label_zh": "收盤突破前 20 日最高收盤價",
        "window": 20,
    },
    {
        "trigger_id": "close_breakout_prev40",
        "trigger_label_zh": "收盤突破前 40 日最高收盤價",
        "window": 40,
    },
    {
        "trigger_id": "close_breakout_prev60",
        "trigger_label_zh": "收盤突破前 60 日最高收盤價",
        "window": 60,
    },
)

SUMMARY_COLUMNS = [
    "generated_at",
    "model_id",
    "artifact_id",
    "artifact_version",
    "analysis_basis",
    "trigger_id",
    "trigger_label_zh",
    "outcome_definition_id",
    "outcome_label_zh",
    "horizon_trading_days",
    "source_cohort_count",
    "accepted_episode_count",
    "suppressed_overlap_count",
    "trigger_observed_episode_count",
    "launch_count",
    "no_launch_count",
    "right_censored_count",
    "classifiable_episode_count",
    "launch_rate_pct",
    "late_launch_after_horizon_count",
    "launch_lag_mean_trading_days",
    "launch_lag_median_trading_days",
    "launch_lag_p75_trading_days",
    "launch_lag_p80_trading_days",
    "launch_lag_p90_trading_days",
    "launch_lag_p95_trading_days",
    "launch_lag_max_trading_days",
    "source_anomaly_candidate_count",
    "return_anomaly_candidate_count",
    "observation_price_path_anomaly_candidate_count",
    "observation_price_path_resolved_count",
    "observation_unresolved_price_path_anomaly_candidate_count",
    "same_stock_overlap_pair_count",
    "sample_policy",
    "right_censor_policy",
    "retrospective_label_status",
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
    "analysis_basis",
    "episode_key",
    "stock_id",
    "stock_name",
    "source_monthly_revenue_period",
    "source_monthly_revenue_source_table_date",
    "source_trade_date",
    "source_stock_sequence_index",
    "signal_date",
    "strict_30_20_streak_months",
    "source_to_signal_trading_days",
    "source_revenue_or_price_anomaly_candidate_flag",
    "abs_ge80_anomaly_candidate_flag",
    "observation_selection_status",
    "observation_suppression_reason",
    "observation_available_candidate_days",
    "mature_for_126d_classification",
    "trigger_id",
    "trigger_label_zh",
    "trigger_observed_flag",
    "first_trigger_date",
    "first_trigger_lag_trading_days",
    "outcome_definition_id",
    "outcome_label_zh",
    "launch_found_flag",
    "launch_date",
    "launch_lag_trading_days",
    "launch_close",
    "launch_raw_close",
    "launch_analysis_price_adjustment_factor",
    "first_hit_20_day_offset",
    "d20_close_return_pct",
    "post_hit_min_close_return_pct",
    "d20_max_close_return_pct",
    "launch_path_anomaly_candidate_flag",
    "launch_raw_path_anomaly_candidate_flag",
    "observation_price_path_anomaly_candidate_flag",
    "observation_price_path_resolved_flag",
    "observation_price_comparability_resolution_ids",
    "observation_unresolved_price_path_anomaly_candidate_flag",
    "classification_at_126d",
    "late_launch_after_126d_flag",
    "same_stock_full_observation_non_overlap_applied",
    "retrospective_label_status",
    "availability_date_semantics",
    "approved_for_daily",
    "production_change",
]

FEATURE_COLUMNS = [
    "generated_at",
    "model_id",
    "artifact_id",
    "artifact_version",
    "analysis_basis",
    "classification_trigger_id",
    "classification_outcome_definition_id",
    "classification_horizon_trading_days",
    "feature_time_basis",
    "feature_order",
    "feature_id",
    "feature_family",
    "feature_kind",
    "feature_rule",
    "launch_group_count",
    "no_launch_group_count",
    "launch_observed_count",
    "no_launch_observed_count",
    "launch_hit_count",
    "no_launch_hit_count",
    "feature_hit_sample_count",
    "launch_rate_when_feature_hit_pct",
    "feature_miss_sample_count",
    "launch_rate_when_feature_miss_pct",
    "feature_hit_launch_rate_uplift_pct_points",
    "launch_hit_rate_pct",
    "no_launch_hit_rate_pct",
    "launch_minus_no_launch_hit_rate_pct",
    "launch_mean",
    "launch_median",
    "no_launch_mean",
    "no_launch_median",
    "launch_minus_no_launch_mean",
    "standardized_mean_difference",
    "launch_source_anomaly_candidate_count",
    "no_launch_source_anomaly_candidate_count",
    "launch_unresolved_price_path_candidate_count",
    "no_launch_unresolved_price_path_candidate_count",
    "discrimination_status",
    "sample_policy",
    "retrospective_label_status",
    "approved_for_daily",
    "production_change",
    "promotion_readiness",
]


def _now_text() -> str:
    return datetime.now(ZoneInfo("Asia/Taipei")).strftime("%Y-%m-%d %H:%M:%S Asia/Taipei")


def _boolish(series: pd.Series) -> pd.Series:
    return series.astype(str).str.strip().str.lower().isin({"true", "1", "yes"})


def _numeric(frame: pd.DataFrame, column: str) -> pd.Series:
    return pd.to_numeric(frame.get(column, pd.Series(index=frame.index, dtype=float)), errors="coerce")


def _number(value: object) -> float | None:
    number = pd.to_numeric(value, errors="coerce")
    return None if pd.isna(number) else float(number)


def _stable(value: object, digits: int = 4) -> float | str:
    number = _number(value)
    return "" if number is None else round(number, digits)


def _rate(numerator: int, denominator: int) -> float | str:
    return round(numerator / denominator * 100.0, 4) if denominator else ""


def _quantile(values: pd.Series, quantile: float) -> float | str:
    numeric = pd.to_numeric(values, errors="coerce").dropna()
    return round(float(numeric.quantile(quantile)), 4) if len(numeric) else ""


def _normalize_date(series: pd.Series) -> pd.Series:
    return series.astype(str).str.replace(r"\D", "", regex=True).str[:8]


def _load_price_comparability_resolutions() -> pd.DataFrame:
    required = {
        "resolution_id",
        "model_id",
        "stock_id",
        "event_type",
        "pre_event_last_trade_date",
        "suspension_start_date",
        "suspension_end_date",
        "resume_date",
        "exchange_ratio",
        "pre_event_close",
        "resume_reference_price",
        "authority",
        "authority_source_url",
        "root_cause_status",
        "adjustment_basis",
        "approved_scope",
    }
    if not PRICE_COMPARABILITY_RESOLUTION_CSV.is_file():
        raise RuntimeError(
            f"launch timing price comparability resolution is missing: {PRICE_COMPARABILITY_RESOLUTION_CSV}"
        )
    frame = pd.read_csv(
        PRICE_COMPARABILITY_RESOLUTION_CSV,
        dtype={"stock_id": str},
        keep_default_na=False,
    )
    missing = sorted(required - set(frame.columns))
    if missing:
        raise RuntimeError(f"price comparability resolution schema is missing columns: {missing}")
    if frame["resolution_id"].duplicated().any():
        raise RuntimeError("price comparability resolution ids must be unique")
    if set(frame["model_id"].astype(str)) != {MODEL_ID}:
        raise RuntimeError("price comparability resolutions must remain model-owned")
    if set(frame["approved_scope"].astype(str)) != {
        "revenue_unreacted_range_launch_timing_feature_audit_only"
    }:
        raise RuntimeError("price comparability resolution scope drift")
    if not frame["authority"].astype(str).eq("TWSE").all():
        raise RuntimeError("price comparability resolution must cite TWSE authority")
    if not frame["authority_source_url"].astype(str).str.startswith(
        "https://www.twse.com.tw/"
    ).all():
        raise RuntimeError("price comparability resolution must cite an official TWSE URL")
    if not frame["root_cause_status"].astype(str).eq(
        "verified_non_comparable_raw_price_scale"
    ).all():
        raise RuntimeError("price comparability resolution root-cause status drift")
    ratio = pd.to_numeric(frame["exchange_ratio"], errors="coerce")
    pre_close = pd.to_numeric(frame["pre_event_close"], errors="coerce")
    reference = pd.to_numeric(frame["resume_reference_price"], errors="coerce")
    if ratio.isna().any() or ratio.le(0).any() or ratio.ge(1).any():
        raise RuntimeError("price comparability exchange ratio must be between zero and one")
    if not np.isclose(pre_close / ratio, reference, rtol=0, atol=0.005).all():
        raise RuntimeError("price comparability adjustment math does not match TWSE reference price")
    for column in (
        "pre_event_last_trade_date",
        "suspension_start_date",
        "suspension_end_date",
        "resume_date",
    ):
        frame[column] = _normalize_date(frame[column])
    frame["stock_id"] = (
        frame["stock_id"].astype(str).str.replace(r"\.0$", "", regex=True).str.zfill(4)
    )
    frame["exchange_ratio"] = ratio
    return frame


def _source_cohort(source: pd.DataFrame, analysis_basis: str) -> pd.DataFrame:
    required = {
        "episode_key",
        "stock_id",
        "stock_name",
        "source_monthly_revenue_period",
        "source_monthly_revenue_source_table_date",
        "signal_date",
        "strict_30_20_streak_months",
        "source_to_signal_trading_days",
        "current_revenue_lag_bucket",
        "flag_strict30_20_consecutive_ge3",
        "source_revenue_or_price_anomaly_candidate_flag",
        "abs_ge80_anomaly_candidate_flag",
    }
    missing = sorted(required - set(source.columns))
    if missing:
        raise RuntimeError(f"launch timing source is missing columns: {missing}")
    mask = (
        _boolish(source["flag_strict30_20_consecutive_ge3"])
        & source["current_revenue_lag_bucket"].astype(str).eq("lag_d8_14")
    )
    cohort = source.loc[mask].copy()
    if analysis_basis == SENSITIVITY_ANALYSIS_BASIS:
        unresolved = _boolish(cohort["source_revenue_or_price_anomaly_candidate_flag"]) | _boolish(
            cohort["abs_ge80_anomaly_candidate_flag"]
        )
        cohort = cohort.loc[~unresolved].copy()
    if cohort["episode_key"].duplicated().any():
        raise RuntimeError(f"launch timing source has duplicate episode keys: {analysis_basis}")
    return cohort.sort_values(
        ["stock_id", "source_monthly_revenue_source_table_date", "episode_key"],
        kind="mergesort",
    ).reset_index(drop=True)


def _prepare_daily_rows(prepared: pd.DataFrame) -> tuple[pd.DataFrame, dict[str, pd.DataFrame]]:
    required = {
        "stock_id",
        "stock_name",
        "_revenue_signal_date",
        "close",
        "ma20",
        "ma60",
        "ema23",
        "return_5d_pct",
        "return_20d_pct",
        "volume_ratio_prev20",
        "macd_hist",
        "rsi14",
        "k_value",
        "d_value",
        "bb_width_pct",
        "ema23_slope_5d_pct",
        "distance_to_ema23_pct",
        "obv_slope_5d",
        "range_width_20d_pct",
        "range_width_60d_pct",
        "close_position_120d_pct",
        "tdcc_history_available",
        "tdcc_consecutive_up_weeks",
        "high_thresholds_up",
        "all_thresholds_up",
        "four_thresholds_sync_up",
        "full_monthly_revenue_context_ready",
        "full_monthly_revenue_latest_yoy_pct",
        "full_monthly_revenue_cumulative_yoy_pct",
        "full_monthly_revenue_latest_yoy_delta_1m_pct_points",
        "bullish_attack_candle",
        "solid_red_candle",
        "signal_market_regime",
        "obv_above_ma20",
    }
    missing = sorted(required - set(prepared.columns))
    if missing:
        raise RuntimeError(f"launch timing prepared frame is missing columns: {missing}")

    daily = prepared.loc[:, sorted(required)].copy()
    daily["stock_id"] = daily["stock_id"].astype(str).str.replace(r"\.0$", "", regex=True).str.zfill(4)
    daily["feature_date"] = _normalize_date(daily["_revenue_signal_date"])
    daily = daily.sort_values(["stock_id", "feature_date"], kind="mergesort")
    if daily.duplicated(["stock_id", "feature_date"]).any():
        duplicated = daily.loc[daily.duplicated(["stock_id", "feature_date"], keep=False), ["stock_id", "feature_date"]]
        raise RuntimeError(f"launch timing prepared frame has duplicate stock dates: {duplicated.head().to_dict('records')}")

    numeric_columns = [
        "close",
        "ma20",
        "ma60",
        "ema23",
        "return_5d_pct",
        "return_20d_pct",
        "volume_ratio_prev20",
        "macd_hist",
        "rsi14",
        "k_value",
        "d_value",
        "bb_width_pct",
        "ema23_slope_5d_pct",
        "distance_to_ema23_pct",
        "obv_slope_5d",
        "range_width_20d_pct",
        "range_width_60d_pct",
        "close_position_120d_pct",
        "tdcc_consecutive_up_weeks",
        "full_monthly_revenue_latest_yoy_pct",
        "full_monthly_revenue_cumulative_yoy_pct",
        "full_monthly_revenue_latest_yoy_delta_1m_pct_points",
    ]
    for column in numeric_columns:
        daily[column] = pd.to_numeric(daily[column], errors="coerce")
    daily["raw_close"] = daily["close"]
    daily["kdj_j_value"] = 3.0 * daily["k_value"] - 2.0 * daily["d_value"]

    resolutions = _load_price_comparability_resolutions()

    grouped: dict[str, pd.DataFrame] = {}
    chunks: list[pd.DataFrame] = []
    for stock_id, stock in daily.groupby("stock_id", sort=False):
        current = stock.reset_index(drop=True).copy()
        current["analysis_price_adjustment_factor"] = 1.0
        current["price_comparability_resolution_ids_on_resume_date"] = ""
        stock_resolutions = resolutions.loc[resolutions["stock_id"].eq(str(stock_id))]
        for event in stock_resolutions.itertuples(index=False):
            prior_mask = current["feature_date"].lt(str(event.resume_date))
            current.loc[prior_mask, "analysis_price_adjustment_factor"] *= (
                1.0 / float(event.exchange_ratio)
            )
            resume_mask = current["feature_date"].eq(str(event.resume_date))
            current.loc[resume_mask, "price_comparability_resolution_ids_on_resume_date"] = str(
                event.resolution_id
            )
        current["analysis_close"] = (
            current["raw_close"] * current["analysis_price_adjustment_factor"]
        )
        current["stock_sequence_index"] = np.arange(len(current), dtype=int)
        for window in (20, 40, 60):
            current[f"previous_{window}d_highest_close"] = (
                current["analysis_close"].shift(1).rolling(
                    window,
                    min_periods=window,
                ).max()
            )
            current[f"close_breakout_prev{window}"] = current["analysis_close"].gt(
                current[f"previous_{window}d_highest_close"]
            )
        grouped[str(stock_id)] = current
        chunks.append(current)
    return pd.concat(chunks, ignore_index=True), grouped


def _episode_inventory(
    source: pd.DataFrame,
    daily_by_stock: dict[str, pd.DataFrame],
    analysis_basis: str,
) -> pd.DataFrame:
    cohort = _source_cohort(source, analysis_basis)
    rows: list[dict[str, object]] = []
    last_accepted_sequence: dict[str, int] = {}
    for episode in cohort.itertuples(index=False):
        stock_id = str(episode.stock_id).replace(".0", "").zfill(4)
        stock = daily_by_stock.get(stock_id)
        source_date = str(episode.source_monthly_revenue_source_table_date)
        selection_status = "accepted"
        suppression_reason = "none"
        source_position: int | None = None
        source_trade_date = ""
        available = -1
        if stock is None or stock.empty:
            selection_status = "suppressed_missing_price_history"
            suppression_reason = "stock_missing_from_prepared_point_in_time_frame"
        else:
            candidates = stock.index[stock["feature_date"].ge(source_date)]
            if not len(candidates):
                selection_status = "suppressed_missing_source_trade_date"
                suppression_reason = "no_trading_date_on_or_after_revenue_availability_date"
            else:
                source_position = int(candidates[0])
                source_trade_date = str(stock.at[source_position, "feature_date"])
                previous = last_accepted_sequence.get(stock_id)
                if previous is not None and source_position <= previous + FULL_OBSERVATION_NON_OVERLAP_DAYS:
                    selection_status = "suppressed_same_stock_full_observation_overlap"
                    suppression_reason = (
                        f"source_sequence_within_{FULL_OBSERVATION_NON_OVERLAP_DAYS}d_of_prior_accepted_episode"
                    )
                else:
                    last_accepted_sequence[stock_id] = source_position
                    available = min(
                        MAX_DISCOVERY_DAYS,
                        len(stock) - OUTCOME_WINDOW_DAYS - 1 - source_position,
                    )
        rows.append(
            {
                "analysis_basis": analysis_basis,
                "episode_key": str(episode.episode_key),
                "stock_id": stock_id,
                "stock_name": str(episode.stock_name),
                "source_monthly_revenue_period": str(episode.source_monthly_revenue_period),
                "source_monthly_revenue_source_table_date": source_date,
                "source_trade_date": source_trade_date,
                "source_stock_sequence_index": source_position if source_position is not None else "",
                "signal_date": str(episode.signal_date),
                "strict_30_20_streak_months": int(episode.strict_30_20_streak_months),
                "source_to_signal_trading_days": int(episode.source_to_signal_trading_days),
                "source_revenue_or_price_anomaly_candidate_flag": bool(
                    str(episode.source_revenue_or_price_anomaly_candidate_flag).lower() == "true"
                ),
                "abs_ge80_anomaly_candidate_flag": bool(
                    str(episode.abs_ge80_anomaly_candidate_flag).lower() == "true"
                ),
                "observation_selection_status": selection_status,
                "observation_suppression_reason": suppression_reason,
                "observation_available_candidate_days": max(available, -1),
                "mature_for_126d_classification": available >= SIX_MONTH_HORIZON_DAYS,
            }
        )
    return pd.DataFrame(rows)


def _path_rows(stock: pd.DataFrame, source_position: int, available: int) -> pd.DataFrame:
    rows: list[dict[str, object]] = []
    close_values = pd.to_numeric(
        stock["analysis_close"] if "analysis_close" in stock.columns else stock["close"],
        errors="coerce",
    ).to_numpy(dtype=float)
    raw_close_values = pd.to_numeric(
        stock["raw_close"] if "raw_close" in stock.columns else stock["close"],
        errors="coerce",
    ).to_numpy(dtype=float)
    adjustment_values = pd.to_numeric(
        stock["analysis_price_adjustment_factor"]
        if "analysis_price_adjustment_factor" in stock.columns
        else pd.Series(1.0, index=stock.index),
        errors="coerce",
    ).to_numpy(dtype=float)
    for candidate_lag in range(max(available, -1) + 1):
        position = source_position + candidate_lag
        base = close_values[position]
        future = close_values[position + 1 : position + OUTCOME_WINDOW_DAYS + 1]
        if not np.isfinite(base) or len(future) != OUTCOME_WINDOW_DAYS or not np.isfinite(future).all():
            continue
        returns = future / base - 1.0
        hits = np.flatnonzero(returns >= 0.20)
        first_hit_offset = int(hits[0] + 1) if len(hits) else None
        post_hit_min = float(np.min(returns[hits[0] :])) if len(hits) else math.nan
        levels = np.concatenate(([base], future))
        step_ratios = levels[1:] / levels[:-1]
        path_anomaly = bool(np.any(step_ratios >= 1.5) or np.any(step_ratios <= 0.67))
        raw_base = raw_close_values[position]
        raw_future = raw_close_values[position + 1 : position + OUTCOME_WINDOW_DAYS + 1]
        raw_levels = np.concatenate(([raw_base], raw_future))
        raw_step_ratios = raw_levels[1:] / raw_levels[:-1]
        raw_path_anomaly = bool(
            np.any(raw_step_ratios >= 1.5) or np.any(raw_step_ratios <= 0.67)
        )
        record = {
            "candidate_lag": candidate_lag,
            "candidate_date": str(stock.at[position, "feature_date"]),
            "candidate_position": position,
            "candidate_close": round(float(base), 8),
            "candidate_raw_close": round(float(raw_base), 8),
            "candidate_analysis_price_adjustment_factor": round(
                float(adjustment_values[position]), 8
            ),
            "first_hit_20_day_offset": first_hit_offset,
            "d20_close_return_pct": round(float(returns[-1] * 100.0), 4),
            "post_hit_min_close_return_pct": (
                round(post_hit_min * 100.0, 4) if np.isfinite(post_hit_min) else ""
            ),
            "d20_max_close_return_pct": round(float(np.max(returns) * 100.0), 4),
            "launch_path_anomaly_candidate_flag": path_anomaly,
            "launch_raw_path_anomaly_candidate_flag": raw_path_anomaly,
            "no_breakout_requirement": True,
            "close_breakout_prev20": bool(stock.at[position, "close_breakout_prev20"]),
            "close_breakout_prev40": bool(stock.at[position, "close_breakout_prev40"]),
            "close_breakout_prev60": bool(stock.at[position, "close_breakout_prev60"]),
        }
        for spec in OUTCOME_SPECS:
            first_deadline = int(spec["first_hit_deadline"])
            floor = spec["post_hit_floor_return"]
            success = bool(
                first_hit_offset is not None
                and first_hit_offset <= first_deadline
                and returns[-1] >= 0.20
                and (floor is None or post_hit_min >= float(floor))
            )
            record[str(spec["outcome_definition_id"])] = success
        rows.append(record)
    return pd.DataFrame(rows)


def _observation_path_anomaly(
    stock: pd.DataFrame,
    source_position: int,
    available: int,
    *,
    close_column: str,
) -> bool:
    if available < 0:
        return False
    end = min(len(stock) - 1, source_position + available + OUTCOME_WINDOW_DAYS)
    closes = pd.to_numeric(
        stock.loc[source_position:end, close_column], errors="coerce"
    ).dropna().to_numpy()
    if len(closes) < 2:
        return False
    ratios = closes[1:] / closes[:-1]
    return bool(np.any(ratios >= 1.5) or np.any(ratios <= 0.67))


def _observation_resolution_ids(
    stock: pd.DataFrame,
    source_position: int,
    available: int,
) -> str:
    if available < 0:
        return ""
    end = min(len(stock) - 1, source_position + available + OUTCOME_WINDOW_DAYS)
    values = stock.loc[
        source_position:end,
        "price_comparability_resolution_ids_on_resume_date",
    ].astype(str)
    ids = sorted({value for value in values if value})
    return ";".join(ids)


def build_launch_detail(
    source: pd.DataFrame,
    prepared: pd.DataFrame | None = None,
    *,
    daily_by_stock: dict[str, pd.DataFrame] | None = None,
) -> tuple[pd.DataFrame, pd.DataFrame]:
    if daily_by_stock is None:
        if prepared is None:
            raise ValueError("prepared frame is required when daily_by_stock is not provided")
        _daily, daily_by_stock = _prepare_daily_rows(prepared)
    generated_at = _now_text()
    inventory_parts = [
        _episode_inventory(source, daily_by_stock, basis)
        for basis in ANALYSIS_BASES
    ]
    inventory = pd.concat(inventory_parts, ignore_index=True)
    rows: list[dict[str, object]] = []
    for episode in inventory.itertuples(index=False):
        accepted = episode.observation_selection_status == "accepted"
        stock = daily_by_stock.get(str(episode.stock_id))
        source_position = int(episode.source_stock_sequence_index) if accepted else -1
        available = int(episode.observation_available_candidate_days)
        paths = _path_rows(stock, source_position, available) if accepted and stock is not None else pd.DataFrame()
        observation_raw_path_candidate = (
            _observation_path_anomaly(
                stock,
                source_position,
                available,
                close_column="raw_close",
            )
            if accepted and stock is not None
            else False
        )
        observation_adjusted_path_candidate = (
            _observation_path_anomaly(
                stock,
                source_position,
                available,
                close_column="analysis_close",
            )
            if accepted and stock is not None
            else False
        )
        observation_resolution_ids = (
            _observation_resolution_ids(stock, source_position, available)
            if accepted and stock is not None
            else ""
        )
        observation_path_resolved = bool(
            observation_raw_path_candidate
            and observation_resolution_ids
            and not observation_adjusted_path_candidate
        )
        for trigger in TRIGGER_SPECS:
            trigger_id = str(trigger["trigger_id"])
            triggered = paths.loc[paths[trigger_id]] if not paths.empty else paths
            first_trigger = triggered.iloc[0] if not triggered.empty else None
            for outcome in OUTCOME_SPECS:
                outcome_id = str(outcome["outcome_definition_id"])
                matched = triggered.loc[triggered[outcome_id]] if not triggered.empty else triggered
                launch = matched.iloc[0] if not matched.empty else None
                launch_lag = int(launch["candidate_lag"]) if launch is not None else None
                if not accepted:
                    classification = "suppressed_non_overlap_or_missing_source"
                elif launch_lag is not None and launch_lag <= SIX_MONTH_HORIZON_DAYS:
                    classification = "launch_within_126d"
                elif available >= SIX_MONTH_HORIZON_DAYS:
                    classification = "no_launch_within_126d"
                else:
                    classification = "right_censored_before_126d"
                rows.append(
                    {
                        "generated_at": generated_at,
                        "model_id": MODEL_ID,
                        "artifact_id": ARTIFACT_ID,
                        "artifact_version": ARTIFACT_VERSION,
                        **episode._asdict(),
                        "trigger_id": trigger_id,
                        "trigger_label_zh": str(trigger["trigger_label_zh"]),
                        "trigger_observed_flag": first_trigger is not None,
                        "first_trigger_date": str(first_trigger["candidate_date"]) if first_trigger is not None else "",
                        "first_trigger_lag_trading_days": (
                            int(first_trigger["candidate_lag"]) if first_trigger is not None else ""
                        ),
                        "outcome_definition_id": outcome_id,
                        "outcome_label_zh": str(outcome["outcome_label_zh"]),
                        "launch_found_flag": launch is not None,
                        "launch_date": str(launch["candidate_date"]) if launch is not None else "",
                        "launch_lag_trading_days": launch_lag if launch_lag is not None else "",
                        "launch_close": _stable(launch["candidate_close"]) if launch is not None else "",
                        "launch_raw_close": (
                            _stable(launch["candidate_raw_close"]) if launch is not None else ""
                        ),
                        "launch_analysis_price_adjustment_factor": (
                            _stable(launch["candidate_analysis_price_adjustment_factor"], 8)
                            if launch is not None
                            else ""
                        ),
                        "first_hit_20_day_offset": (
                            int(launch["first_hit_20_day_offset"]) if launch is not None else ""
                        ),
                        "d20_close_return_pct": _stable(launch["d20_close_return_pct"]) if launch is not None else "",
                        "post_hit_min_close_return_pct": (
                            _stable(launch["post_hit_min_close_return_pct"]) if launch is not None else ""
                        ),
                        "d20_max_close_return_pct": (
                            _stable(launch["d20_max_close_return_pct"]) if launch is not None else ""
                        ),
                        "launch_path_anomaly_candidate_flag": (
                            bool(launch["launch_path_anomaly_candidate_flag"]) if launch is not None else False
                        ),
                        "launch_raw_path_anomaly_candidate_flag": (
                            bool(launch["launch_raw_path_anomaly_candidate_flag"])
                            if launch is not None
                            else False
                        ),
                        "observation_price_path_anomaly_candidate_flag": observation_raw_path_candidate,
                        "observation_price_path_resolved_flag": observation_path_resolved,
                        "observation_price_comparability_resolution_ids": observation_resolution_ids,
                        "observation_unresolved_price_path_anomaly_candidate_flag": (
                            observation_adjusted_path_candidate
                        ),
                        "classification_at_126d": classification,
                        "late_launch_after_126d_flag": bool(
                            launch_lag is not None and launch_lag > SIX_MONTH_HORIZON_DAYS
                        ),
                        "same_stock_full_observation_non_overlap_applied": True,
                        "retrospective_label_status": "research_only_future_outcome_label_not_tradable_trigger",
                        "availability_date_semantics": AVAILABILITY_SEMANTICS,
                        "approved_for_daily": False,
                        "production_change": False,
                    }
                )
    detail = pd.DataFrame(rows)
    return detail[DETAIL_COLUMNS].sort_values(
        ["analysis_basis", "stock_id", "source_trade_date", "trigger_id", "outcome_definition_id"],
        kind="mergesort",
    ).reset_index(drop=True), inventory


def _summary_row(
    detail: pd.DataFrame,
    inventory: pd.DataFrame,
    *,
    analysis_basis: str,
    trigger: dict[str, object],
    outcome: dict[str, object],
    horizon: int,
) -> dict[str, object]:
    source_inventory = inventory.loc[inventory["analysis_basis"].eq(analysis_basis)]
    accepted_inventory = source_inventory.loc[source_inventory["observation_selection_status"].eq("accepted")]
    selected = detail.loc[
        detail["analysis_basis"].eq(analysis_basis)
        & detail["trigger_id"].eq(trigger["trigger_id"])
        & detail["outcome_definition_id"].eq(outcome["outcome_definition_id"])
        & detail["observation_selection_status"].eq("accepted")
    ].copy()
    launch_lag = pd.to_numeric(selected["launch_lag_trading_days"], errors="coerce")
    available = pd.to_numeric(selected["observation_available_candidate_days"], errors="coerce")
    launch_by = launch_lag.notna() & launch_lag.le(horizon)
    no_launch_by = available.ge(horizon) & (~launch_by)
    censored = available.lt(horizon) & (~launch_by)
    classifiable = launch_by | no_launch_by
    launch_values = launch_lag.loc[launch_by]
    source_candidates = _boolish(selected.loc[classifiable, "source_revenue_or_price_anomaly_candidate_flag"])
    return_candidates = _boolish(selected.loc[classifiable, "abs_ge80_anomaly_candidate_flag"])
    price_candidates = _boolish(selected.loc[classifiable, "observation_price_path_anomaly_candidate_flag"])
    price_resolved = _boolish(selected.loc[classifiable, "observation_price_path_resolved_flag"])
    price_unresolved = _boolish(
        selected.loc[classifiable, "observation_unresolved_price_path_anomaly_candidate_flag"]
    )
    stock_overlap = 0
    identity = accepted_inventory.sort_values(["stock_id", "source_stock_sequence_index"])
    for _stock_id, stock_rows in identity.groupby("stock_id", sort=False):
        positions = pd.to_numeric(stock_rows["source_stock_sequence_index"], errors="coerce").dropna().sort_values()
        if len(positions) > 1:
            stock_overlap += int(positions.diff().dropna().le(FULL_OBSERVATION_NON_OVERLAP_DAYS).sum())
    return {
        "generated_at": str(detail["generated_at"].iloc[0]),
        "model_id": MODEL_ID,
        "artifact_id": ARTIFACT_ID,
        "artifact_version": ARTIFACT_VERSION,
        "analysis_basis": analysis_basis,
        "trigger_id": str(trigger["trigger_id"]),
        "trigger_label_zh": str(trigger["trigger_label_zh"]),
        "outcome_definition_id": str(outcome["outcome_definition_id"]),
        "outcome_label_zh": str(outcome["outcome_label_zh"]),
        "horizon_trading_days": horizon,
        "source_cohort_count": len(source_inventory),
        "accepted_episode_count": len(accepted_inventory),
        "suppressed_overlap_count": int(
            source_inventory["observation_selection_status"].ne("accepted").sum()
        ),
        "trigger_observed_episode_count": int(_boolish(selected["trigger_observed_flag"]).sum()),
        "launch_count": int(launch_by.sum()),
        "no_launch_count": int(no_launch_by.sum()),
        "right_censored_count": int(censored.sum()),
        "classifiable_episode_count": int(classifiable.sum()),
        "launch_rate_pct": _rate(int(launch_by.sum()), int(classifiable.sum())),
        "late_launch_after_horizon_count": int((launch_lag.gt(horizon)).sum()),
        "launch_lag_mean_trading_days": _stable(launch_values.mean()),
        "launch_lag_median_trading_days": _quantile(launch_values, 0.50),
        "launch_lag_p75_trading_days": _quantile(launch_values, 0.75),
        "launch_lag_p80_trading_days": _quantile(launch_values, 0.80),
        "launch_lag_p90_trading_days": _quantile(launch_values, 0.90),
        "launch_lag_p95_trading_days": _quantile(launch_values, 0.95),
        "launch_lag_max_trading_days": _stable(launch_values.max()),
        "source_anomaly_candidate_count": int(source_candidates.sum()),
        "return_anomaly_candidate_count": int(return_candidates.sum()),
        "observation_price_path_anomaly_candidate_count": int(price_candidates.sum()),
        "observation_price_path_resolved_count": int(price_resolved.sum()),
        "observation_unresolved_price_path_anomaly_candidate_count": int(
            price_unresolved.sum()
        ),
        "same_stock_overlap_pair_count": stock_overlap,
        "sample_policy": "sample_count_disclosed_not_used_as_automatic_rejection",
        "right_censor_policy": "insufficient_future_trading_days_are_right_censored_not_failures",
        "retrospective_label_status": "research_only_future_outcome_label_not_tradable_trigger",
        "availability_date_semantics": AVAILABILITY_SEMANTICS,
        "financial_statement_scope": FINANCIAL_STATEMENT_SCOPE,
        "approved_for_daily": False,
        "production_change": False,
        "promotion_readiness": "blocked_pending_root_cause_anomaly_candidate_review_and_forward_trigger_test",
    }


def build_launch_summary(detail: pd.DataFrame, inventory: pd.DataFrame) -> pd.DataFrame:
    rows = [
        _summary_row(
            detail,
            inventory,
            analysis_basis=basis,
            trigger=trigger,
            outcome=outcome,
            horizon=horizon,
        )
        for basis in ANALYSIS_BASES
        for trigger in TRIGGER_SPECS
        for outcome in OUTCOME_SPECS
        for horizon in HORIZONS
    ]
    return pd.DataFrame(rows, columns=SUMMARY_COLUMNS)


SNAPSHOT_NUMERIC_FEATURES = (
    (10, "revenue_latest_yoy_pct", "monthly_revenue", "full_monthly_revenue_latest_yoy_pct"),
    (20, "revenue_cumulative_yoy_pct", "monthly_revenue", "full_monthly_revenue_cumulative_yoy_pct"),
    (30, "revenue_latest_yoy_delta_1m", "monthly_revenue", "full_monthly_revenue_latest_yoy_delta_1m_pct_points"),
    (100, "return_5d_pct", "price_momentum", "return_5d_pct"),
    (110, "return_20d_pct", "price_momentum", "return_20d_pct"),
    (120, "volume_ratio_prev20", "volume", "volume_ratio_prev20"),
    (130, "range20_width_pct", "price_shape", "range_width_20d_pct"),
    (140, "range60_width_pct", "price_shape", "range_width_60d_pct"),
    (150, "close_position_120d_pct", "price_position", "close_position_120d_pct"),
    (200, "rsi14", "technical", "rsi14"),
    (210, "macd_hist", "technical", "macd_hist"),
    (220, "kd_k_value", "technical", "k_value"),
    (230, "kd_d_value", "technical", "d_value"),
    (240, "kdj_j_value", "technical", "kdj_j_value"),
    (250, "bb_width_pct", "technical", "bb_width_pct"),
    (260, "ema23_slope_5d_pct", "technical", "ema23_slope_5d_pct"),
    (270, "distance_to_ema23_pct", "technical", "distance_to_ema23_pct"),
    (280, "obv_slope_5d", "technical", "obv_slope_5d"),
    (300, "tdcc_consecutive_up_weeks", "tdcc", "tdcc_consecutive_up_weeks"),
)

PREWEEK_NUMERIC_FEATURES = tuple(
    feature for feature in SNAPSHOT_NUMERIC_FEATURES if feature[2] not in {"monthly_revenue", "tdcc"}
)


def _binary_specs() -> tuple[tuple[int, str, str, str, tuple[str, ...], Callable[[pd.DataFrame], pd.Series]], ...]:
    return (
        (10, "revenue_latest50_cumulative30", "monthly_revenue", "latest YoY >= 50% and cumulative YoY >= 30%", ("full_monthly_revenue_latest_yoy_pct", "full_monthly_revenue_cumulative_yoy_pct"), lambda d: _numeric(d, "full_monthly_revenue_latest_yoy_pct").ge(50) & _numeric(d, "full_monthly_revenue_cumulative_yoy_pct").ge(30)),
        (20, "revenue_latest_yoy_delta_ge20", "monthly_revenue", "latest YoY improves >= 20 percentage points", ("full_monthly_revenue_latest_yoy_delta_1m_pct_points",), lambda d: _numeric(d, "full_monthly_revenue_latest_yoy_delta_1m_pct_points").ge(20)),
        (100, "tdcc_high_thresholds_up", "tdcc", "TDCC high thresholds increase", ("tdcc_history_available", "high_thresholds_up"), lambda d: _boolish(d["tdcc_history_available"]) & _boolish(d["high_thresholds_up"])),
        (110, "tdcc_all_thresholds_up", "tdcc", "TDCC all thresholds increase", ("tdcc_history_available", "all_thresholds_up"), lambda d: _boolish(d["tdcc_history_available"]) & _boolish(d["all_thresholds_up"])),
        (120, "tdcc_consecutive_up_ge2", "tdcc", "TDCC consecutive up weeks >= 2", ("tdcc_history_available", "tdcc_consecutive_up_weeks"), lambda d: _boolish(d["tdcc_history_available"]) & _numeric(d, "tdcc_consecutive_up_weeks").ge(2)),
        (200, "technical_macd_hist_gt0", "technical", "MACD histogram > 0", ("macd_hist",), lambda d: _numeric(d, "macd_hist").gt(0)),
        (210, "technical_rsi14_40_70", "technical", "40 <= RSI14 <= 70", ("rsi14",), lambda d: _numeric(d, "rsi14").between(40, 70)),
        (220, "technical_rsi14_ge60", "technical", "RSI14 >= 60", ("rsi14",), lambda d: _numeric(d, "rsi14").ge(60)),
        (230, "technical_kd_bullish_not_overheated", "technical", "K > D and K < 80", ("k_value", "d_value"), lambda d: _numeric(d, "k_value").gt(_numeric(d, "d_value")) & _numeric(d, "k_value").lt(80)),
        (240, "technical_kdj_bullish_not_extreme", "technical", "K > D, J > K, J < 100", ("k_value", "d_value", "kdj_j_value"), lambda d: _numeric(d, "k_value").gt(_numeric(d, "d_value")) & _numeric(d, "kdj_j_value").gt(_numeric(d, "k_value")) & _numeric(d, "kdj_j_value").lt(100)),
        (250, "technical_close_above_ma20_ema23", "technical", "close > MA20 and close > EMA23", ("close", "ma20", "ema23"), lambda d: _numeric(d, "close").gt(_numeric(d, "ma20")) & _numeric(d, "close").gt(_numeric(d, "ema23"))),
        (260, "technical_ma20_above_ma60", "technical", "MA20 > MA60", ("ma20", "ma60"), lambda d: _numeric(d, "ma20").gt(_numeric(d, "ma60"))),
        (270, "technical_ema23_slope_positive", "technical", "EMA23 five-day slope > 0", ("ema23_slope_5d_pct",), lambda d: _numeric(d, "ema23_slope_5d_pct").gt(0)),
        (280, "technical_obv_above_ma20", "technical", "OBV > OBV MA20", ("obv_above_ma20",), lambda d: _boolish(d["obv_above_ma20"])),
        (300, "volume_ratio_ge1_5", "volume", "volume / previous 20-day average >= 1.5", ("volume_ratio_prev20",), lambda d: _numeric(d, "volume_ratio_prev20").ge(1.5)),
        (310, "volume_ratio_ge2", "volume", "volume / previous 20-day average >= 2", ("volume_ratio_prev20",), lambda d: _numeric(d, "volume_ratio_prev20").ge(2)),
        (400, "close_breakout_prev20", "breakout", "close > previous 20-day highest close", ("close_breakout_prev20",), lambda d: _boolish(d["close_breakout_prev20"])),
        (410, "close_breakout_prev40", "breakout", "close > previous 40-day highest close", ("close_breakout_prev40",), lambda d: _boolish(d["close_breakout_prev40"])),
        (420, "close_breakout_prev60", "breakout", "close > previous 60-day highest close", ("close_breakout_prev60",), lambda d: _boolish(d["close_breakout_prev60"])),
        (500, "candle_bullish_attack", "candle", "bullish attack candle", ("bullish_attack_candle",), lambda d: _boolish(d["bullish_attack_candle"])),
        (510, "candle_solid_red", "candle", "solid red candle", ("solid_red_candle",), lambda d: _boolish(d["solid_red_candle"])),
        (600, "market_bull", "market_regime", "market regime is strong_bull or mild_bull", ("signal_market_regime",), lambda d: d["signal_market_regime"].astype(str).isin({"strong_bull", "mild_bull"})),
        (610, "market_correction_or_high_risk", "market_regime_risk", "market regime is correction or high_risk", ("signal_market_regime",), lambda d: d["signal_market_regime"].astype(str).isin({"correction", "high_risk"})),
    )


def _snapshot_rows(
    detail: pd.DataFrame,
    daily_by_stock: dict[str, pd.DataFrame],
    analysis_basis: str,
) -> pd.DataFrame:
    selected = detail.loc[
        detail["analysis_basis"].eq(analysis_basis)
        & detail["trigger_id"].eq(PRIMARY_TRIGGER_ID)
        & detail["outcome_definition_id"].eq(PRIMARY_OUTCOME_ID)
        & detail["observation_selection_status"].eq("accepted")
        & detail["classification_at_126d"].isin({"launch_within_126d", "no_launch_within_126d"})
    ].copy()
    rows: list[dict[str, object]] = []
    for episode in selected.itertuples(index=False):
        stock = daily_by_stock.get(str(episode.stock_id))
        if stock is None:
            continue
        group = "launch" if episode.classification_at_126d == "launch_within_126d" else "no_launch"
        dates = {
            "source_signal_date": str(episode.signal_date),
            "retrospective_breakout_anchor": (
                str(episode.launch_date) if group == "launch" else str(episode.first_trigger_date)
            ),
        }
        for time_basis, feature_date in dates.items():
            if not feature_date:
                continue
            matches = stock.index[stock["feature_date"].eq(feature_date)]
            if not len(matches):
                continue
            position = int(matches[0])
            snapshot = stock.loc[position].to_dict()
            snapshot.update(
                {
                    "analysis_basis": analysis_basis,
                    "episode_key": str(episode.episode_key),
                    "classification_group": group,
                    "feature_time_basis": time_basis,
                    "feature_date": feature_date,
                    "source_revenue_or_price_anomaly_candidate_flag": bool(
                        episode.source_revenue_or_price_anomaly_candidate_flag
                    ),
                    "abs_ge80_anomaly_candidate_flag": bool(episode.abs_ge80_anomaly_candidate_flag),
                    "observation_price_path_resolved_flag": bool(
                        episode.observation_price_path_resolved_flag
                    ),
                    "observation_unresolved_price_path_anomaly_candidate_flag": bool(
                        episode.observation_unresolved_price_path_anomaly_candidate_flag
                    ),
                }
            )
            if time_basis == "retrospective_breakout_anchor" and position >= 5:
                previous = stock.loc[position - 5]
                for _order, feature_id, _family, column in PREWEEK_NUMERIC_FEATURES:
                    current_value = _number(snapshot.get(column))
                    previous_value = _number(previous.get(column))
                    snapshot[f"preweek_change__{feature_id}"] = (
                        current_value - previous_value
                        if current_value is not None and previous_value is not None
                        else math.nan
                    )
            rows.append(snapshot)
    return pd.DataFrame(rows)


def _feature_discrimination_binary(launch_rate: float | None, no_launch_rate: float | None) -> str:
    if launch_rate is None or no_launch_rate is None:
        return "insufficient_observed_values"
    delta = launch_rate - no_launch_rate
    if launch_rate >= 60 and no_launch_rate >= 60 and abs(delta) < 10:
        return "common_to_both_groups_low_discrimination"
    if delta >= 10:
        return "launch_enriched_candidate_feature"
    if delta <= -10:
        return "no_launch_enriched_risk_feature"
    return "weak_or_mixed_discrimination"


def _feature_discrimination_numeric(effect: float | None) -> str:
    if effect is None:
        return "insufficient_observed_values"
    if effect >= 0.5:
        return "launch_higher_candidate_feature"
    if effect <= -0.5:
        return "no_launch_higher_risk_feature"
    if abs(effect) >= 0.2:
        return "small_numeric_separation"
    return "weak_or_mixed_discrimination"


def _pooled_effect(launch: pd.Series, no_launch: pd.Series) -> float | None:
    left = pd.to_numeric(launch, errors="coerce").dropna()
    right = pd.to_numeric(no_launch, errors="coerce").dropna()
    if len(left) < 2 or len(right) < 2:
        return None
    denominator = len(left) + len(right) - 2
    pooled_variance = ((len(left) - 1) * left.var(ddof=1) + (len(right) - 1) * right.var(ddof=1)) / denominator
    if not np.isfinite(pooled_variance) or pooled_variance <= 0:
        return None
    return float((left.mean() - right.mean()) / math.sqrt(pooled_variance))


def _feature_base_row(
    snapshots: pd.DataFrame,
    *,
    generated_at: str,
    analysis_basis: str,
    time_basis: str,
    order: int,
    feature_id: str,
    family: str,
    kind: str,
    rule: str,
) -> dict[str, object]:
    launch = snapshots.loc[snapshots["classification_group"].eq("launch")]
    no_launch = snapshots.loc[snapshots["classification_group"].eq("no_launch")]
    return {
        "generated_at": generated_at,
        "model_id": MODEL_ID,
        "artifact_id": ARTIFACT_ID,
        "artifact_version": ARTIFACT_VERSION,
        "analysis_basis": analysis_basis,
        "classification_trigger_id": PRIMARY_TRIGGER_ID,
        "classification_outcome_definition_id": PRIMARY_OUTCOME_ID,
        "classification_horizon_trading_days": SIX_MONTH_HORIZON_DAYS,
        "feature_time_basis": time_basis,
        "feature_order": order,
        "feature_id": feature_id,
        "feature_family": family,
        "feature_kind": kind,
        "feature_rule": rule,
        "launch_group_count": int(launch["episode_key"].nunique()),
        "no_launch_group_count": int(no_launch["episode_key"].nunique()),
        "launch_source_anomaly_candidate_count": int(
            _boolish(launch["source_revenue_or_price_anomaly_candidate_flag"]).sum()
        ),
        "no_launch_source_anomaly_candidate_count": int(
            _boolish(no_launch["source_revenue_or_price_anomaly_candidate_flag"]).sum()
        ),
        "launch_unresolved_price_path_candidate_count": int(
            _boolish(launch["observation_unresolved_price_path_anomaly_candidate_flag"]).sum()
        ),
        "no_launch_unresolved_price_path_candidate_count": int(
            _boolish(no_launch["observation_unresolved_price_path_anomaly_candidate_flag"]).sum()
        ),
        "sample_policy": "sample_count_disclosed_not_used_as_automatic_rejection",
        "retrospective_label_status": "research_only_future_outcome_label_not_tradable_trigger",
        "approved_for_daily": False,
        "production_change": False,
        "promotion_readiness": "blocked_pending_forward_trigger_test_and_root_cause_review",
    }


def build_feature_contrast(
    detail: pd.DataFrame,
    prepared: pd.DataFrame | None = None,
    *,
    daily_by_stock: dict[str, pd.DataFrame] | None = None,
) -> pd.DataFrame:
    if daily_by_stock is None:
        if prepared is None:
            raise ValueError("prepared frame is required when daily_by_stock is not provided")
        _daily, daily_by_stock = _prepare_daily_rows(prepared)
    generated_at = str(detail["generated_at"].iloc[0])
    rows: list[dict[str, object]] = []
    for basis in ANALYSIS_BASES:
        snapshots = _snapshot_rows(detail, daily_by_stock, basis)
        for time_basis in ("source_signal_date", "retrospective_breakout_anchor"):
            current = snapshots.loc[snapshots["feature_time_basis"].eq(time_basis)].copy()
            if current.empty:
                continue
            launch = current.loc[current["classification_group"].eq("launch")]
            no_launch = current.loc[current["classification_group"].eq("no_launch")]
            for order, feature_id, family, rule, required, condition in _binary_specs():
                observed = current[list(required)].notna().all(axis=1)
                if family == "tdcc":
                    observed &= _boolish(current["tdcc_history_available"])
                if family.startswith("market_regime"):
                    observed &= current["signal_market_regime"].astype(str).ne("unknown")
                hits = condition(current).fillna(False)
                launch_observed = observed.loc[launch.index]
                no_launch_observed = observed.loc[no_launch.index]
                launch_hit = int((hits.loc[launch.index] & launch_observed).sum())
                no_launch_hit = int((hits.loc[no_launch.index] & no_launch_observed).sum())
                feature_hit_count = launch_hit + no_launch_hit
                launch_miss = int(launch_observed.sum()) - launch_hit
                no_launch_miss = int(no_launch_observed.sum()) - no_launch_hit
                feature_miss_count = launch_miss + no_launch_miss
                conditional_hit_rate = _rate(launch_hit, feature_hit_count)
                conditional_miss_rate = _rate(launch_miss, feature_miss_count)
                conditional_hit_rate_number = _number(conditional_hit_rate)
                conditional_miss_rate_number = _number(conditional_miss_rate)
                launch_rate = _rate(launch_hit, int(launch_observed.sum()))
                no_launch_rate = _rate(no_launch_hit, int(no_launch_observed.sum()))
                launch_rate_number = _number(launch_rate)
                no_launch_rate_number = _number(no_launch_rate)
                base = _feature_base_row(
                    current,
                    generated_at=generated_at,
                    analysis_basis=basis,
                    time_basis=time_basis,
                    order=order,
                    feature_id=feature_id,
                    family=family,
                    kind="binary",
                    rule=rule,
                )
                rows.append(
                    {
                        **base,
                        "launch_observed_count": int(launch_observed.sum()),
                        "no_launch_observed_count": int(no_launch_observed.sum()),
                        "launch_hit_count": launch_hit,
                        "no_launch_hit_count": no_launch_hit,
                        "feature_hit_sample_count": feature_hit_count,
                        "launch_rate_when_feature_hit_pct": conditional_hit_rate,
                        "feature_miss_sample_count": feature_miss_count,
                        "launch_rate_when_feature_miss_pct": conditional_miss_rate,
                        "feature_hit_launch_rate_uplift_pct_points": (
                            round(
                                conditional_hit_rate_number - conditional_miss_rate_number,
                                4,
                            )
                            if conditional_hit_rate_number is not None
                            and conditional_miss_rate_number is not None
                            else ""
                        ),
                        "launch_hit_rate_pct": launch_rate,
                        "no_launch_hit_rate_pct": no_launch_rate,
                        "launch_minus_no_launch_hit_rate_pct": (
                            round(launch_rate_number - no_launch_rate_number, 4)
                            if launch_rate_number is not None and no_launch_rate_number is not None
                            else ""
                        ),
                        "launch_mean": "",
                        "launch_median": "",
                        "no_launch_mean": "",
                        "no_launch_median": "",
                        "launch_minus_no_launch_mean": "",
                        "standardized_mean_difference": "",
                        "discrimination_status": _feature_discrimination_binary(
                            launch_rate_number,
                            no_launch_rate_number,
                        ),
                    }
                )
            for order, feature_id, family, column in SNAPSHOT_NUMERIC_FEATURES:
                launch_values = pd.to_numeric(launch[column], errors="coerce").dropna()
                no_launch_values = pd.to_numeric(no_launch[column], errors="coerce").dropna()
                effect = _pooled_effect(launch_values, no_launch_values)
                base = _feature_base_row(
                    current,
                    generated_at=generated_at,
                    analysis_basis=basis,
                    time_basis=time_basis,
                    order=1000 + order,
                    feature_id=feature_id,
                    family=family,
                    kind="numeric",
                    rule=f"compare {column} between launch and no-launch groups",
                )
                launch_mean = launch_values.mean() if len(launch_values) else math.nan
                no_launch_mean = no_launch_values.mean() if len(no_launch_values) else math.nan
                rows.append(
                    {
                        **base,
                        "launch_observed_count": len(launch_values),
                        "no_launch_observed_count": len(no_launch_values),
                        "launch_hit_count": "",
                        "no_launch_hit_count": "",
                        "feature_hit_sample_count": "",
                        "launch_rate_when_feature_hit_pct": "",
                        "feature_miss_sample_count": "",
                        "launch_rate_when_feature_miss_pct": "",
                        "feature_hit_launch_rate_uplift_pct_points": "",
                        "launch_hit_rate_pct": "",
                        "no_launch_hit_rate_pct": "",
                        "launch_minus_no_launch_hit_rate_pct": "",
                        "launch_mean": _stable(launch_mean),
                        "launch_median": _stable(launch_values.median()),
                        "no_launch_mean": _stable(no_launch_mean),
                        "no_launch_median": _stable(no_launch_values.median()),
                        "launch_minus_no_launch_mean": (
                            _stable(launch_mean - no_launch_mean)
                            if np.isfinite(launch_mean) and np.isfinite(no_launch_mean)
                            else ""
                        ),
                        "standardized_mean_difference": _stable(effect),
                        "discrimination_status": _feature_discrimination_numeric(effect),
                    }
                )

        anchor = snapshots.loc[snapshots["feature_time_basis"].eq("retrospective_breakout_anchor")].copy()
        if not anchor.empty:
            launch = anchor.loc[anchor["classification_group"].eq("launch")]
            no_launch = anchor.loc[anchor["classification_group"].eq("no_launch")]
            for order, feature_id, family, _column in PREWEEK_NUMERIC_FEATURES:
                column = f"preweek_change__{feature_id}"
                launch_values = pd.to_numeric(launch.get(column), errors="coerce").dropna()
                no_launch_values = pd.to_numeric(no_launch.get(column), errors="coerce").dropna()
                effect = _pooled_effect(launch_values, no_launch_values)
                base = _feature_base_row(
                    anchor,
                    generated_at=generated_at,
                    analysis_basis=basis,
                    time_basis="pre_breakout_week_change",
                    order=2000 + order,
                    feature_id=f"preweek_change__{feature_id}",
                    family=family,
                    kind="numeric_change",
                    rule=f"anchor-day {feature_id} minus value five trading days earlier",
                )
                launch_mean = launch_values.mean() if len(launch_values) else math.nan
                no_launch_mean = no_launch_values.mean() if len(no_launch_values) else math.nan
                rows.append(
                    {
                        **base,
                        "launch_observed_count": len(launch_values),
                        "no_launch_observed_count": len(no_launch_values),
                        "launch_hit_count": "",
                        "no_launch_hit_count": "",
                        "feature_hit_sample_count": "",
                        "launch_rate_when_feature_hit_pct": "",
                        "feature_miss_sample_count": "",
                        "launch_rate_when_feature_miss_pct": "",
                        "feature_hit_launch_rate_uplift_pct_points": "",
                        "launch_hit_rate_pct": "",
                        "no_launch_hit_rate_pct": "",
                        "launch_minus_no_launch_hit_rate_pct": "",
                        "launch_mean": _stable(launch_mean),
                        "launch_median": _stable(launch_values.median()),
                        "no_launch_mean": _stable(no_launch_mean),
                        "no_launch_median": _stable(no_launch_values.median()),
                        "launch_minus_no_launch_mean": (
                            _stable(launch_mean - no_launch_mean)
                            if np.isfinite(launch_mean) and np.isfinite(no_launch_mean)
                            else ""
                        ),
                        "standardized_mean_difference": _stable(effect),
                        "discrimination_status": _feature_discrimination_numeric(effect),
                    }
                )
    return pd.DataFrame(rows, columns=FEATURE_COLUMNS).sort_values(
        ["analysis_basis", "feature_time_basis", "feature_order"],
        kind="mergesort",
    ).reset_index(drop=True)


def build_launch_timing_feature_audit(
    prepared: pd.DataFrame,
    lag_detail: pd.DataFrame,
) -> tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    _daily, daily_by_stock = _prepare_daily_rows(prepared)
    detail, inventory = build_launch_detail(
        lag_detail,
        daily_by_stock=daily_by_stock,
    )
    summary = build_launch_summary(detail, inventory)
    feature = build_feature_contrast(
        detail,
        daily_by_stock=daily_by_stock,
    )
    return summary, detail, feature


def _markdown(summary: pd.DataFrame, feature: pd.DataFrame) -> str:
    primary = summary.loc[
        summary["analysis_basis"].eq(PRIMARY_ANALYSIS_BASIS)
        & summary["horizon_trading_days"].eq(SIX_MONTH_HORIZON_DAYS)
    ].copy()
    primary_timing = summary.loc[
        summary["analysis_basis"].eq(PRIMARY_ANALYSIS_BASIS)
        & summary["trigger_id"].eq(PRIMARY_TRIGGER_ID)
        & summary["outcome_definition_id"].eq(PRIMARY_OUTCOME_ID)
    ].copy()
    feature_primary = feature.loc[feature["analysis_basis"].eq(PRIMARY_ANALYSIS_BASIS)].copy()
    binary = feature_primary.loc[feature_primary["feature_kind"].eq("binary")].copy()
    binary["_rank"] = pd.to_numeric(binary["launch_minus_no_launch_hit_rate_pct"], errors="coerce").abs()
    numeric = feature_primary.loc[feature_primary["feature_kind"].ne("binary")].copy()
    numeric["_rank"] = pd.to_numeric(numeric["standardized_mean_difference"], errors="coerce").abs()
    six_month_row = primary_timing.loc[
        primary_timing["horizon_trading_days"].eq(SIX_MONTH_HORIZON_DAYS)
    ].iloc[0]
    full_discovery_row = primary_timing.loc[
        primary_timing["horizon_trading_days"].eq(MAX_DISCOVERY_DAYS)
    ].iloc[0]
    observed_launch_count = int(full_discovery_row["launch_count"])
    six_month_launch_count = int(six_month_row["launch_count"])
    six_month_observed_launch_coverage = _rate(
        six_month_launch_count,
        observed_launch_count,
    )
    summary_columns = [
        "trigger_label_zh",
        "outcome_label_zh",
        "accepted_episode_count",
        "launch_count",
        "no_launch_count",
        "right_censored_count",
        "launch_rate_pct",
        "launch_lag_median_trading_days",
        "launch_lag_p90_trading_days",
    ]
    feature_columns = [
        "feature_time_basis",
        "feature_id",
        "launch_group_count",
        "no_launch_group_count",
        "launch_hit_rate_pct",
        "no_launch_hit_rate_pct",
        "launch_minus_no_launch_hit_rate_pct",
        "feature_hit_sample_count",
        "launch_rate_when_feature_hit_pct",
        "feature_miss_sample_count",
        "launch_rate_when_feature_miss_pct",
        "feature_hit_launch_rate_uplift_pct_points",
        "standardized_mean_difference",
        "discrimination_status",
    ]
    lines = [
        "# 營收低反應模型：發動時間與突破特徵研究",
        "",
        f"- artifact_version: `{ARTIFACT_VERSION}`",
        "- 母體：營收強勢連續至少 3 個月，且營收可得日至既有訊號日相隔 8～14 個交易日。",
        "- primary 會保留所有未完成根因查核的候選；舊 109 筆只能作 candidate-exclusion sensitivity。",
        "- 3593 力銘原始價格跳升已查明為彌補虧損減資；本 artifact 依 TWSE 0.6 換股率將減資前價格除以 0.6 後重算，不把 8.10 到 12.30 誤認為經濟報酬。",
        "- 價格跳動門檻只會觸發 anomaly candidate；沒有官方事件、換股率與調整公式證據時，不得自行排除。",
        "- `launch_hit_rate_pct` 是成功組內特徵盛行率；真正的條件發動率請看 `launch_rate_when_feature_hit_pct`，兩者不可混用。",
        "- 主要嚴格發動定義要求 D+15 前收盤達 +20%，且其後到 D+20 每個收盤都不低於 +20%；D+15 截止是為了至少保留 5 個交易日檢查是否回落。",
        f"- 六個月內觀察到 {six_month_launch_count}/{observed_launch_count} 筆已觀察發動，覆蓋率 {six_month_observed_launch_coverage}%；若把大部分定為約 80%，六個月合理；90% 發動時間約為 {full_discovery_row['launch_lag_p90_trading_days']} 個交易日。",
        f"- 252 日列的 100% 不代表全部股票最終都會發動：該列仍有 {int(full_discovery_row['right_censored_count'])} 筆右設限，完整一年未發動樣本為 {int(full_discovery_row['no_launch_count'])}，存在 survivor bias。",
        f"- 最長發動探索：{MAX_DISCOVERY_DAYS} 個交易日；六個月分類：{SIX_MONTH_HORIZON_DAYS} 個交易日；結果窗：{OUTCOME_WINDOW_DAYS} 個交易日。",
        f"- 同股 non-overlap：完整探索與結果窗合計 {FULL_OBSERVATION_NON_OVERLAP_DAYS} 個交易日，後續重疊事件壓掉。",
        "- right censor：未來資料不足者不算未發動。",
        "- 發動日是使用未來結果回看得到的研究標籤，不是可直接操作的確認訊號。",
        "- 價格與來源異常候選保留在 primary；數字門檻不能直接判定極端值或排除。",
        f"- 財報範圍：`{FINANCIAL_STATEMENT_SCOPE}`。",
        "- status: research-only；不修改 production registry、operation adapter、ranking、PDF 或正式 snapshots。",
        "",
        "## 六個月發動定義比較",
        "",
        primary[summary_columns].to_markdown(index=False),
        "",
        "## 主要嚴格定義的等待時間",
        "",
        primary_timing[
            [
                "horizon_trading_days",
                "launch_count",
                "no_launch_count",
                "right_censored_count",
                "launch_rate_pct",
                "launch_lag_median_trading_days",
                "launch_lag_p80_trading_days",
                "launch_lag_p90_trading_days",
                "launch_lag_p95_trading_days",
            ]
        ].to_markdown(index=False),
        "",
        "## 命中率差異最大的單項特徵",
        "",
        binary.sort_values("_rank", ascending=False)[feature_columns].head(20).to_markdown(index=False),
        "",
        "## 數值差異最大的技術與前一週變化",
        "",
        numeric.sort_values("_rank", ascending=False)[feature_columns].head(20).to_markdown(index=False),
        "",
    ]
    return "\n".join(lines)


def write_launch_timing_feature_audit(
    summary: pd.DataFrame,
    detail: pd.DataFrame,
    feature: pd.DataFrame,
) -> None:
    for path, frame in (
        (LATEST_CSV, summary),
        (DETAIL_CSV, detail),
        (FEATURE_CSV, feature),
        (HISTORY_CSV, summary),
        (HISTORY_FEATURE_CSV, feature),
        (DOCS_CSV, summary),
        (DOCS_FEATURE_CSV, feature),
    ):
        path.parent.mkdir(parents=True, exist_ok=True)
        frame.to_csv(path, index=False, encoding="utf-8-sig", lineterminator="\n")
    markdown = _markdown(summary, feature)
    for path in (LATEST_MD, DOCS_MD):
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(markdown, encoding="utf-8", newline="\n")
