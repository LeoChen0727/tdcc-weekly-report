from __future__ import annotations

import math
from pathlib import Path
from typing import Any

import pandas as pd

from revenue_unreacted_range_close_confirmation_timing import (
    ANOMALY_CANDIDATE_SENSITIVITY_BASIS as SOURCE_ANOMALY_CANDIDATE_SENSITIVITY_BASIS,
    DECISION_BASIS,
    FIXED_FEATURE_CONTRAST_EXIT_CLOCK_ID,
    FIXED_FEATURE_CONTRAST_PENDING_WINDOW_DAYS,
    FIXED_FEATURE_CONTRAST_VARIANT_ID,
    build_fixed_confirmation_episode_source,
)
from tracking_utils import (
    DOCS_LATEST_DIR,
    RESEARCH_LATEST_DIR,
    markdown_table,
    now_text,
    safe_str,
    write_csv,
)


HISTORY_DIR = Path("output/history/research")
ARTIFACT_ID = "revenue_unreacted_range_fixed_confirmation_feature_contrast_audit"
ANOMALY_ARTIFACT_ID = f"{ARTIFACT_ID}_anomaly_audit"
ARTIFACT_VERSION = "fixed_range23_breakout_3d_confirmation_d20_v2_anomaly_candidate_primary"
MODEL_ID = "revenue_unreacted_range"
MODEL_NAME_ZH = "營收爆發但股價尚未反應模型"
RETURN_ANOMALY_CANDIDATE_SENSITIVITY_BASIS = (
    "excluding_abs_ge80_anomaly_candidates_sensitivity_only"
)

SUMMARY_CSV = RESEARCH_LATEST_DIR / f"{ARTIFACT_ID}_latest.csv"
DETAIL_CSV = RESEARCH_LATEST_DIR / f"{ARTIFACT_ID}_detail_latest.csv"
ANOMALY_CSV = RESEARCH_LATEST_DIR / f"{ANOMALY_ARTIFACT_ID}_latest.csv"
SUMMARY_MD = RESEARCH_LATEST_DIR / f"{ARTIFACT_ID}_latest.md"
HISTORY_SUMMARY_CSV = HISTORY_DIR / f"{ARTIFACT_ID}.csv"
HISTORY_ANOMALY_CSV = HISTORY_DIR / f"{ANOMALY_ARTIFACT_ID}.csv"
DOCS_SUMMARY_CSV = DOCS_LATEST_DIR / SUMMARY_CSV.name
DOCS_ANOMALY_CSV = DOCS_LATEST_DIR / ANOMALY_CSV.name
DOCS_SUMMARY_MD = DOCS_LATEST_DIR / SUMMARY_MD.name

FEATURE_TIME_BASES = (
    {
        "feature_time_basis": "signal_date_close",
        "feature_time_basis_zh": "候選訊號日收盤已知",
        "sequence_column": "signal_sequence_index",
        "information_cutoff": "signal_date_close_before_pending_confirmation",
    },
    {
        "feature_time_basis": "confirmation_date_close",
        "feature_time_basis_zh": "確認日收盤已知",
        "sequence_column": "confirmation_sequence_index",
        "information_cutoff": "confirmation_date_close_before_entry_next_open",
    },
)

FINANCIAL_STATEMENT_EXCLUSIONS = (
    "quarterly_or_annual_financial_statements|EPS|gross_margin|operating_margin|"
    "operating_income|non_operating_income|net_income"
)

FEATURE_REQUIRED_COLUMNS: dict[str, tuple[str, ...]] = {
    "revenue_latest30_and_cumulative20": (
        "full_monthly_revenue_latest_yoy_pct",
        "full_monthly_revenue_cumulative_yoy_pct",
    ),
    "revenue_latest50_and_cumulative30": (
        "full_monthly_revenue_latest_yoy_pct",
        "full_monthly_revenue_cumulative_yoy_pct",
    ),
    "revenue_latest_yoy_ge100": ("full_monthly_revenue_latest_yoy_pct",),
    "revenue_latest_yoy_improving_2m": (
        "full_monthly_revenue_latest_yoy_pct",
        "full_monthly_revenue_prev1_latest_yoy_pct",
        "full_monthly_revenue_prev2_latest_yoy_pct",
    ),
    "revenue_cumulative_yoy_improving_2m": (
        "full_monthly_revenue_cumulative_yoy_pct",
        "full_monthly_revenue_prev1_cumulative_yoy_pct",
        "full_monthly_revenue_prev2_cumulative_yoy_pct",
    ),
    "revenue_latest_yoy_delta_ge20": ("full_monthly_revenue_latest_yoy_delta_1m_pct_points",),
    "tdcc_high_thresholds_up": ("tdcc_as_of_date",),
    "tdcc_all_thresholds_up": ("tdcc_as_of_date",),
    "tdcc_four_thresholds_sync_up": ("tdcc_as_of_date",),
    "tdcc_consecutive_up_ge1": ("tdcc_as_of_date", "tdcc_consecutive_up_weeks"),
    "tdcc_consecutive_up_ge2": ("tdcc_as_of_date", "tdcc_consecutive_up_weeks"),
    "technical_macd_hist_gt0": ("macd_hist",),
    "technical_rsi14_ge60": ("rsi14",),
    "technical_rsi14_40_70": ("rsi14",),
    "technical_kd_bullish_not_overheated": ("k_value", "d_value"),
    "technical_kdj_bullish_not_extreme": ("k_value", "d_value"),
    "technical_kdj_j_ge100": ("k_value", "d_value"),
    "technical_bb_width_not_extreme": ("bb_width_pct",),
    "technical_close_above_ma20_ema23": ("close", "ma20", "ema23"),
    "technical_ema23_slope_positive": ("ema23_slope_5d_pct",),
    "technical_obv_above_ma20": ("obv", "obv_ma20"),
    "technical_ma20_above_ma60": ("ma20", "ma60"),
    "shape_range23_width_le10": ("range_width_23d_pct",),
    "shape_range23_width_le15": ("range_width_23d_pct",),
    "shape_range23_width_le20": ("range_width_23d_pct",),
    "shape_near_range23_high": ("distance_to_range_high_23d_pct",),
    "position120_low_le40": ("close_position_120d_pct",),
    "position120_mid_40_75": ("close_position_120d_pct",),
    "position120_high_gt75": ("close_position_120d_pct",),
    "momentum_return20_0_25": ("return_20d_pct",),
    "volume_ratio_le1_5": ("volume_ratio_prev20",),
    "volume_ratio_le2": ("volume_ratio_prev20",),
    "candle_bullish_attack": ("open", "close", "previous_close"),
    "candle_solid_red": ("open", "close", "previous_close"),
    "market_strong_bull": ("signal_market_regime",),
    "market_mild_bull": ("signal_market_regime",),
    "market_bull": ("signal_market_regime",),
    "market_correction_or_high_risk": ("signal_market_regime",),
    "market_range_bound": ("signal_market_regime",),
    "market_unknown": ("signal_market_regime",),
}

CONTEXT_COLUMNS = [
    "stock_id",
    "market",
    "_revenue_signal_date",
    "_revenue_stock_sequence_index",
    "open",
    "close",
    "previous_close",
    "ma20",
    "ma60",
    "ema23",
    "range_width_23d_pct",
    "distance_to_range_high_23d_pct",
    "close_position_120d_pct",
    "return_5d_pct",
    "return_20d_pct",
    "volume_ratio_prev20",
    "bullish_attack_candle",
    "solid_red_candle",
    "macd_hist",
    "rsi14",
    "k_value",
    "d_value",
    "kdj_j_value",
    "kd_bullish_not_overheated",
    "bb_width_pct",
    "bb_width_not_extreme",
    "ema23_slope_5d_pct",
    "distance_to_ema23_pct",
    "obv",
    "obv_ma20",
    "obv_above_ma20",
    "tdcc_history_available",
    "tdcc_as_of_date",
    "tdcc_consecutive_up_weeks",
    "high_thresholds_up",
    "all_thresholds_up",
    "four_thresholds_sync_up",
    "full_monthly_revenue_context_ready",
    "full_monthly_revenue_period",
    "full_monthly_revenue_source_table_date",
    "full_monthly_revenue_latest_yoy_pct",
    "full_monthly_revenue_cumulative_yoy_pct",
    "full_monthly_revenue_prev1_latest_yoy_pct",
    "full_monthly_revenue_prev2_latest_yoy_pct",
    "full_monthly_revenue_prev3_latest_yoy_pct",
    "full_monthly_revenue_prev1_cumulative_yoy_pct",
    "full_monthly_revenue_prev2_cumulative_yoy_pct",
    "full_monthly_revenue_prev3_cumulative_yoy_pct",
    "full_monthly_revenue_latest_yoy_delta_1m_pct_points",
    "full_monthly_revenue_cumulative_yoy_delta_1m_pct_points",
    "full_monthly_revenue_numerical_anomaly_flag",
    "benchmark_index",
    "signal_market_regime",
]


def _numeric(frame: pd.DataFrame, column: str) -> pd.Series:
    return pd.to_numeric(frame.get(column, pd.Series(math.nan, index=frame.index)), errors="coerce")


def _boolish(series: pd.Series) -> pd.Series:
    if pd.api.types.is_bool_dtype(series):
        return series.fillna(False).astype(bool)
    return series.astype(str).str.strip().str.lower().isin({"true", "1", "yes"})


def _round(value: Any, digits: int = 4) -> float | str:
    try:
        number = float(value)
    except (TypeError, ValueError):
        return ""
    return round(number, digits) if math.isfinite(number) else ""


def _rate(numerator: int, denominator: int) -> float | str:
    return "" if denominator <= 0 else round(numerator / denominator * 100.0, 4)


def _delta(left: Any, right: Any) -> float | str:
    left_number = pd.to_numeric(pd.Series([left]), errors="coerce").iloc[0]
    right_number = pd.to_numeric(pd.Series([right]), errors="coerce").iloc[0]
    if pd.isna(left_number) or pd.isna(right_number):
        return ""
    return round(float(left_number - right_number), 4)


def feature_observed_mask(frame: pd.DataFrame, feature_id: str, feature_family: str) -> pd.Series:
    observed = pd.Series(True, index=frame.index, dtype=bool)
    if feature_family == "monthly_revenue":
        observed &= _boolish(
            frame.get("full_monthly_revenue_context_ready", pd.Series(False, index=frame.index))
        )
    elif feature_family == "tdcc":
        observed &= _boolish(frame.get("tdcc_history_available", pd.Series(False, index=frame.index)))
    elif feature_family.startswith("market_regime"):
        regime = frame.get("signal_market_regime", pd.Series("unknown", index=frame.index)).astype(str)
        if feature_id != "market_unknown":
            observed &= regime.ne("unknown")
    for column in FEATURE_REQUIRED_COLUMNS.get(feature_id, ()):
        if column not in frame.columns:
            observed &= False
        elif column.endswith("_date") or column == "signal_market_regime":
            observed &= frame[column].astype(str).str.strip().ne("")
        else:
            observed &= pd.to_numeric(frame[column], errors="coerce").notna()
    return observed.fillna(False)


def numeric_feature_observed_mask(
    frame: pd.DataFrame,
    feature_family: str,
    column: str,
) -> pd.Series:
    observed = _numeric(frame, column).notna()
    if feature_family == "monthly_revenue":
        observed &= _boolish(
            frame.get("full_monthly_revenue_context_ready", pd.Series(False, index=frame.index))
        )
    elif feature_family == "tdcc":
        observed &= _boolish(
            frame.get("tdcc_history_available", pd.Series(False, index=frame.index))
        )
    return observed.fillna(False)


def _outcome_metrics(frame: pd.DataFrame) -> dict[str, Any]:
    realized = _numeric(frame, "realized_return_pct").dropna()
    sample = len(realized)
    wins = realized.ge(5.0)
    neutral = realized.ge(0.0) & realized.lt(5.0)
    failure = realized.lt(0.0)
    high = realized.ge(8.0)
    loss = realized.le(-5.0)
    return {
        "accepted_trade_count": sample,
        "win_count": int(wins.sum()),
        "neutral_count": int(neutral.sum()),
        "failure_count": int(failure.sum()),
        "win_rate_pct": _rate(int(wins.sum()), sample),
        "neutral_rate_pct": _rate(int(neutral.sum()), sample),
        "failure_rate_pct": _rate(int(failure.sum()), sample),
        "avg_realized_return_pct": "" if not sample else round(float(realized.mean()), 4),
        "median_realized_return_pct": "" if not sample else round(float(realized.median()), 4),
        "high_return_8_count": int(high.sum()),
        "high_return_8_rate_pct": _rate(int(high.sum()), sample),
        "loss_5_count": int(loss.sum()),
        "loss_5_rate_pct": _rate(int(loss.sum()), sample),
    }


def _same_stock_overlap_pair_count(frame: pd.DataFrame) -> int:
    count = 0
    trades = frame.drop_duplicates(["anomaly_exclusion_basis", "episode_key"]).copy()
    for _, part in trades.groupby("stock_id", sort=False, dropna=False):
        ordered = part.assign(
            _entry=pd.to_numeric(part["entry_sequence_index"], errors="coerce"),
            _exit=pd.to_numeric(part["exit_sequence_index"], errors="coerce"),
        ).dropna(subset=["_entry", "_exit"]).sort_values("_entry")
        active_exit: float | None = None
        for _, row in ordered.iterrows():
            entry = float(row["_entry"])
            exit_value = float(row["_exit"])
            if active_exit is not None and entry <= active_exit:
                count += 1
            active_exit = exit_value if active_exit is None else max(active_exit, exit_value)
    return count


def _revenue_period_repeat_count(frame: pd.DataFrame) -> int:
    trades = frame.drop_duplicates(["anomaly_exclusion_basis", "episode_key"])
    groups = trades.groupby(["stock_id", "source_monthly_revenue_period"], dropna=False).size()
    return int((groups - 1).clip(lower=0).sum())


def _prepare_context(
    prepared_frame: pd.DataFrame,
    binary_specs: list[dict[str, Any]],
    numeric_specs: list[tuple[int, str, str, str]],
) -> pd.DataFrame:
    context = prepared_frame.copy()
    context["kdj_j_value"] = 3.0 * _numeric(context, "k_value") - 2.0 * _numeric(context, "d_value")
    if context.duplicated(["stock_id", "_revenue_stock_sequence_index"]).any():
        raise ValueError("fixed feature context has duplicate stock/sequence rows")
    for spec in binary_specs:
        feature_id = safe_str(spec["feature_id"])
        feature_family = safe_str(spec["feature_family"])
        mask = spec["condition"](context)
        observed = feature_observed_mask(
            context,
            feature_id,
            feature_family,
        )
        context[f"feature__{feature_id}"] = (
            pd.Series(mask, index=context.index).fillna(False).astype(bool) & observed
        )
        context[f"feature_observed__{feature_id}"] = observed
    for _, _, _, column in numeric_specs:
        if column not in context.columns:
            context[column] = math.nan
    for column in CONTEXT_COLUMNS:
        if column not in context.columns:
            context[column] = ""
    feature_columns = [f"feature__{safe_str(spec['feature_id'])}" for spec in binary_specs]
    observed_columns = [f"feature_observed__{safe_str(spec['feature_id'])}" for spec in binary_specs]
    keep = list(dict.fromkeys(CONTEXT_COLUMNS + feature_columns + observed_columns))
    return context[keep]


def _target_timing_rows(timing_summary: pd.DataFrame) -> pd.DataFrame:
    return timing_summary[
        timing_summary["row_type"].eq("variant_performance")
        & timing_summary["confirmation_variant_id"].eq(FIXED_FEATURE_CONTRAST_VARIANT_ID)
        & pd.to_numeric(timing_summary["pending_window_days"], errors="coerce").eq(
            FIXED_FEATURE_CONTRAST_PENDING_WINDOW_DAYS
        )
        & timing_summary["exit_clock_id"].eq(FIXED_FEATURE_CONTRAST_EXIT_CLOCK_ID)
    ].copy()


def _build_detail(
    prepared_frame: pd.DataFrame,
    binary_specs: list[dict[str, Any]],
    numeric_specs: list[tuple[int, str, str, str]],
    generated_at: str,
) -> pd.DataFrame:
    episodes = build_fixed_confirmation_episode_source(prepared_frame, generated_at=generated_at)
    mature = episodes[
        episodes["lifecycle_status"].eq("confirmed_mature")
        & episodes["metric_included"].astype(bool)
    ].copy()
    decision = mature[mature["anomaly_exclusion_basis"].eq(DECISION_BASIS)].copy()
    sensitivity = decision[_numeric(decision, "realized_return_pct").abs().lt(80.0)].copy()
    sensitivity["anomaly_exclusion_basis"] = RETURN_ANOMALY_CANDIDATE_SENSITIVITY_BASIS
    sensitivity["decision_basis"] = False
    mature["sensitivity_basis"] = mature["anomaly_exclusion_basis"].ne(DECISION_BASIS)
    sensitivity["sensitivity_basis"] = True
    trades = pd.concat([mature, sensitivity], ignore_index=True, sort=False)
    trades = trades.rename(
        columns={
            "full_monthly_revenue_period": "source_monthly_revenue_period",
            "full_monthly_revenue_source_table_date": "source_monthly_revenue_source_table_date",
            "full_monthly_revenue_latest_yoy_pct": "source_monthly_revenue_latest_yoy_pct",
            "full_monthly_revenue_cumulative_yoy_pct": "source_monthly_revenue_cumulative_yoy_pct",
        }
    )
    context = _prepare_context(prepared_frame, binary_specs, numeric_specs)
    details: list[pd.DataFrame] = []
    for time_spec in FEATURE_TIME_BASES:
        sequence_column = safe_str(time_spec["sequence_column"])
        joined = trades.merge(
            context,
            left_on=["stock_id", sequence_column],
            right_on=["stock_id", "_revenue_stock_sequence_index"],
            how="left",
            validate="many_to_one",
        )
        joined["feature_context_join_status"] = joined["_revenue_signal_date"].astype(str).str.strip().map(
            lambda value: "matched_unique_stock_sequence" if value else "missing_feature_context"
        )
        if joined["feature_context_join_status"].ne("matched_unique_stock_sequence").any():
            raise ValueError(f"missing {time_spec['feature_time_basis']} feature context rows")
        joined["generated_at"] = generated_at
        joined["model_id"] = MODEL_ID
        joined["model_name_zh"] = MODEL_NAME_ZH
        joined["research_artifact_id"] = ARTIFACT_ID
        joined["artifact_version"] = ARTIFACT_VERSION
        joined["source_timing_artifact_id"] = "revenue_unreacted_range_close_confirmation_timing_audit"
        joined["feature_time_basis"] = time_spec["feature_time_basis"]
        joined["feature_time_basis_zh"] = time_spec["feature_time_basis_zh"]
        joined["feature_information_cutoff"] = time_spec["information_cutoff"]
        joined["feature_context_date"] = joined["_revenue_signal_date"]
        joined["candidate_confirmation_rule_id"] = FIXED_FEATURE_CONTRAST_VARIANT_ID
        joined["pending_window_days_fixed"] = FIXED_FEATURE_CONTRAST_PENDING_WINDOW_DAYS
        joined["exit_clock_id_fixed"] = FIXED_FEATURE_CONTRAST_EXIT_CLOCK_ID
        joined["entry_rule_id"] = "confirmation_close_next_trading_day_open"
        joined["stop_rule_id"] = "no_stop_in_fixed_feature_contrast"
        joined["monthly_revenue_scope"] = "monthly_revenue_point_in_time_only"
        joined["financial_statement_scope"] = "excluded_no_formal_point_in_time_layer"
        joined["financial_statement_fields_excluded"] = FINANCIAL_STATEMENT_EXCLUSIONS
        joined["same_stock_non_overlap_applied"] = True
        joined["approved_for_daily"] = False
        joined["production_change"] = "none"
        joined["promotion_readiness"] = "blocked_pending_root_cause_anomaly_candidate_review"
        details.append(joined)
    detail = pd.concat(details, ignore_index=True, sort=False)
    identity = [
        "generated_at",
        "model_id",
        "model_name_zh",
        "research_artifact_id",
        "artifact_version",
        "source_timing_artifact_id",
        "anomaly_exclusion_basis",
        "decision_basis",
        "sensitivity_basis",
        "feature_time_basis",
        "feature_time_basis_zh",
        "feature_information_cutoff",
        "feature_context_join_status",
        "feature_context_date",
        "candidate_confirmation_rule_id",
        "pending_window_days_fixed",
        "exit_clock_id_fixed",
        "entry_rule_id",
        "stop_rule_id",
        "episode_key",
        "stock_id",
        "signal_date",
        "signal_sequence_index",
        "confirmation_date",
        "confirmation_sequence_index",
        "entry_date",
        "entry_sequence_index",
        "entry_price",
        "exit_date",
        "exit_sequence_index",
        "exit_price",
        "realized_return_pct",
        "outcome_label",
        "high_return_8_flag",
        "loss_5_flag",
        "price_path_anomaly_candidate_flag",
        "price_path_anomaly_candidate_reason",
        "source_revenue_or_price_anomaly_candidate_flag",
        "source_monthly_revenue_period",
        "source_monthly_revenue_source_table_date",
        "source_monthly_revenue_latest_yoy_pct",
        "source_monthly_revenue_cumulative_yoy_pct",
        "monthly_revenue_scope",
        "financial_statement_scope",
        "financial_statement_fields_excluded",
        "same_stock_non_overlap_applied",
        "approved_for_daily",
        "production_change",
        "promotion_readiness",
    ]
    feature_columns = [f"feature__{safe_str(spec['feature_id'])}" for spec in binary_specs]
    observed_columns = [f"feature_observed__{safe_str(spec['feature_id'])}" for spec in binary_specs]
    keep = [column for column in dict.fromkeys(identity + CONTEXT_COLUMNS + feature_columns + observed_columns) if column in detail]
    return detail[keep].sort_values(
        ["anomaly_exclusion_basis", "feature_time_basis", "stock_id", "signal_sequence_index"],
        kind="mergesort",
    ).reset_index(drop=True)


def _anomaly_audit(detail: pd.DataFrame) -> pd.DataFrame:
    rows: list[dict[str, Any]] = []
    signal_detail = detail[detail["feature_time_basis"].eq("signal_date_close")]
    for basis, part in signal_detail.groupby("anomaly_exclusion_basis", sort=False):
        basis_detail = detail[detail["anomaly_exclusion_basis"].eq(basis)]
        signal_revenue_anomalies = int(
            _boolish(
                basis_detail.loc[
                    basis_detail["feature_time_basis"].eq("signal_date_close"),
                    "full_monthly_revenue_numerical_anomaly_flag",
                ]
            ).sum()
        )
        confirmation_revenue_anomalies = int(
            _boolish(
                basis_detail.loc[
                    basis_detail["feature_time_basis"].eq("confirmation_date_close"),
                    "full_monthly_revenue_numerical_anomaly_flag",
                ]
            ).sum()
        )
        realized = _numeric(part, "realized_return_pct").dropna().sort_values()
        if realized.empty:
            continue
        max_index = realized.idxmax()
        min_index = realized.idxmin()
        absolute = realized.abs().sort_values(ascending=False)
        absolute_total = float(absolute.sum())
        trim_count = max(1, int(math.ceil(len(realized) * 0.01))) if len(realized) >= 20 else 0
        trimmed = realized.iloc[trim_count : len(realized) - trim_count] if trim_count else realized
        without_extremes = realized.drop(index=list(dict.fromkeys([max_index, min_index])))
        top1 = round(float(absolute.iloc[:1].sum()) / absolute_total * 100.0, 4) if absolute_total else 0.0
        top5 = round(float(absolute.iloc[:5].sum()) / absolute_total * 100.0, 4) if absolute_total else 0.0
        path_count = int(_boolish(part["price_path_anomaly_candidate_flag"]).sum())
        abs80_candidate_count = int(realized.abs().ge(80.0).sum())
        dominance = path_count > 0 or top1 >= 10.0 or top5 >= 30.0
        source_candidate_count = int(
            _boolish(part["source_revenue_or_price_anomaly_candidate_flag"]).sum()
        )
        if basis in {
            SOURCE_ANOMALY_CANDIDATE_SENSITIVITY_BASIS,
            RETURN_ANOMALY_CANDIDATE_SENSITIVITY_BASIS,
        }:
            interpretation = "candidate_threshold_sensitivity_only_not_anomaly_disposition"
        elif abs80_candidate_count > 0 or path_count > 0 or source_candidate_count > 0:
            interpretation = "blocked_pending_root_cause_anomaly_candidate_review"
        elif dominance:
            interpretation = "blocked_pending_non_threshold_anomaly_review"
        else:
            interpretation = "anomaly_check_pass_no_threshold_candidates"
        rows.append(
            {
                "generated_at": safe_str(part["generated_at"].iloc[0]),
                "model_id": MODEL_ID,
                "research_artifact_id": ANOMALY_ARTIFACT_ID,
                "artifact_version": ARTIFACT_VERSION,
                "source_timing_artifact_id": "revenue_unreacted_range_close_confirmation_timing_audit",
                "anomaly_exclusion_basis": basis,
                "decision_basis": basis == DECISION_BASIS,
                "sensitivity_basis": basis in {
                    SOURCE_ANOMALY_CANDIDATE_SENSITIVITY_BASIS,
                    RETURN_ANOMALY_CANDIDATE_SENSITIVITY_BASIS,
                },
                "accepted_trade_count": len(realized),
                "same_stock_overlap_pair_count": _same_stock_overlap_pair_count(part),
                "same_stock_revenue_period_repeat_count": _revenue_period_repeat_count(part),
                "price_path_anomaly_candidate_count": path_count,
                "return_abs_ge80_anomaly_candidate_count": abs80_candidate_count,
                "source_revenue_or_price_anomaly_candidate_count": source_candidate_count,
                "signal_feature_context_revenue_anomaly_candidate_count": signal_revenue_anomalies,
                "confirmation_feature_context_revenue_anomaly_candidate_count": confirmation_revenue_anomalies,
                "feature_context_candidate_values_retained_in_feature_evidence": True,
                "max_realized_return_pct": round(float(realized.loc[max_index]), 4),
                "max_return_stock_id": safe_str(part.loc[max_index, "stock_id"]),
                "max_return_signal_date": safe_str(part.loc[max_index, "signal_date"]),
                "min_realized_return_pct": round(float(realized.loc[min_index]), 4),
                "min_return_stock_id": safe_str(part.loc[min_index, "stock_id"]),
                "min_return_signal_date": safe_str(part.loc[min_index, "signal_date"]),
                "top1_abs_return_share_pct": top1,
                "top5_abs_return_share_pct": top5,
                "avg_realized_return_pct": round(float(realized.mean()), 4),
                "median_realized_return_pct": round(float(realized.median()), 4),
                "avg_without_max_min_pct": round(float(without_extremes.mean()), 4) if not without_extremes.empty else "",
                "trimmed_1pct_avg_return_pct": round(float(trimmed.mean()), 4) if not trimmed.empty else "",
                "potential_return_dominance_flag": dominance,
                "interpretation_status": interpretation,
                "approved_for_daily": False,
                "production_change": "none",
            }
        )
    return pd.DataFrame(rows)


def _numeric_group_stats(
    part: pd.DataFrame,
    column: str,
    observed: pd.Series,
) -> dict[str, Any]:
    values = _numeric(part, column).where(observed)
    realized = _numeric(part, "realized_return_pct")
    output: dict[str, Any] = {}
    for group_id, mask in {
        "high_return": realized.ge(8.0),
        "win": realized.ge(5.0),
        "failure": realized.lt(0.0),
    }.items():
        group = values[mask].dropna()
        output[f"{group_id}_group_count"] = int(mask.sum())
        output[f"{group_id}_feature_value_count"] = len(group)
        output[f"{group_id}_feature_mean"] = "" if group.empty else round(float(group.mean()), 4)
        output[f"{group_id}_feature_median"] = "" if group.empty else round(float(group.median()), 4)
    output["high_return_minus_failure_feature_mean"] = _delta(
        output["high_return_feature_mean"],
        output["failure_feature_mean"],
    )
    output["high_return_minus_failure_feature_median"] = _delta(
        output["high_return_feature_median"],
        output["failure_feature_median"],
    )
    return output


def _feature_interpretation(
    metrics: dict[str, Any],
    baseline: dict[str, Any],
    observed_discrimination: Any,
) -> str:
    if int(metrics.get("accepted_trade_count", 0)) == 0:
        return "no_feature_hits"
    discrimination = pd.to_numeric(pd.Series([observed_discrimination]), errors="coerce").iloc[0]
    avg_delta = pd.to_numeric(
        pd.Series([_delta(metrics.get("avg_realized_return_pct"), baseline.get("avg_realized_return_pct"))]),
        errors="coerce",
    ).iloc[0]
    failure_delta = pd.to_numeric(
        pd.Series([_delta(metrics.get("failure_rate_pct"), baseline.get("failure_rate_pct"))]),
        errors="coerce",
    ).iloc[0]
    high_delta = pd.to_numeric(
        pd.Series([_delta(metrics.get("high_return_8_rate_pct"), baseline.get("high_return_8_rate_pct"))]),
        errors="coerce",
    ).iloc[0]
    if pd.notna(discrimination) and discrimination > 0 and avg_delta > 0 and failure_delta <= 0 and high_delta > 0:
        return "positive_discriminator_single_feature_candidate"
    if pd.notna(discrimination) and discrimination < 0 and avg_delta < 0 and failure_delta > 0:
        return "failure_associated_risk_feature_candidate"
    return "mixed_or_low_discrimination_research_only"


def _summary(
    detail: pd.DataFrame,
    anomaly: pd.DataFrame,
    timing_summary: pd.DataFrame,
    binary_specs: list[dict[str, Any]],
    numeric_specs: list[tuple[int, str, str, str]],
) -> pd.DataFrame:
    rows: list[dict[str, Any]] = []
    target_timing = _target_timing_rows(timing_summary)
    timing_map = target_timing.set_index("anomaly_exclusion_basis").to_dict("index")
    anomaly_map = anomaly.set_index("anomaly_exclusion_basis")["interpretation_status"].to_dict()
    for (basis, time_basis), part in detail.groupby(
        ["anomaly_exclusion_basis", "feature_time_basis"], sort=False
    ):
        baseline = _outcome_metrics(part)
        source_basis = (
            DECISION_BASIS
            if basis == RETURN_ANOMALY_CANDIDATE_SENSITIVITY_BASIS
            else basis
        )
        timing_row = timing_map.get(source_basis, {})
        expected_count = (
            baseline["accepted_trade_count"]
            if basis == RETURN_ANOMALY_CANDIDATE_SENSITIVITY_BASIS
            else int(float(timing_row.get("accepted_trade_count", -1)))
        )
        common = {
            "generated_at": safe_str(part["generated_at"].iloc[0]),
            "model_id": MODEL_ID,
            "model_name_zh": MODEL_NAME_ZH,
            "research_artifact_id": ARTIFACT_ID,
            "artifact_version": ARTIFACT_VERSION,
            "source_timing_artifact_id": "revenue_unreacted_range_close_confirmation_timing_audit",
            "anomaly_exclusion_basis": basis,
            "decision_basis": basis == DECISION_BASIS,
            "sensitivity_basis": basis in {
                SOURCE_ANOMALY_CANDIDATE_SENSITIVITY_BASIS,
                RETURN_ANOMALY_CANDIDATE_SENSITIVITY_BASIS,
            },
            "feature_time_basis": time_basis,
            "feature_time_basis_zh": safe_str(part["feature_time_basis_zh"].iloc[0]),
            "feature_information_cutoff": safe_str(part["feature_information_cutoff"].iloc[0]),
            "candidate_confirmation_rule_id": FIXED_FEATURE_CONTRAST_VARIANT_ID,
            "pending_window_days": FIXED_FEATURE_CONTRAST_PENDING_WINDOW_DAYS,
            "exit_clock_id": FIXED_FEATURE_CONTRAST_EXIT_CLOCK_ID,
            "entry_rule_id": "confirmation_close_next_trading_day_open",
            "stop_rule_id": "no_stop_in_fixed_feature_contrast",
            "win_definition": "realized return >= +5%",
            "neutral_definition": "0% <= realized return < +5%",
            "failure_definition": "realized return < 0%",
            "high_return_definition": "realized return >= +8%",
            "monthly_revenue_scope": "monthly_revenue_point_in_time_only",
            "financial_statement_scope": "excluded_no_formal_point_in_time_layer",
            "financial_statement_fields_excluded": FINANCIAL_STATEMENT_EXCLUSIONS,
            "same_stock_non_overlap_applied": True,
            "same_stock_overlap_pair_count": _same_stock_overlap_pair_count(part),
            "same_stock_revenue_period_repeat_count": _revenue_period_repeat_count(part),
            "timing_expected_accepted_trade_count": expected_count,
            "timing_accepted_trade_count_parity_status": (
                "pass" if baseline["accepted_trade_count"] == expected_count else "fail"
            ),
            "anomaly_interpretation_status": anomaly_map.get(basis, "missing_anomaly_audit"),
            "feature_context_revenue_anomaly_candidate_count": int(
                _boolish(part["full_monthly_revenue_numerical_anomaly_flag"]).sum()
            ),
            "feature_context_candidate_values_retained_in_feature_evidence": True,
            "sample_count_context": "reported_not_a_disqualifier_non_overlap_and_revenue_period_dedup_enforced",
            "combination_policy": "single_features_only_no_arbitrary_condition_stacking",
            "approved_for_daily": False,
            "production_change": "none",
            "promotion_readiness": "blocked_pending_root_cause_anomaly_candidate_review",
        }
        rows.append(
            {
                **common,
                "row_type": "baseline",
                "feature_order": 0,
                "feature_id": "fixed_range23_breakout_3d_confirmation_d20_baseline",
                "feature_family": "baseline",
                "feature_rule": "23-day highest-close breakout within three trading days; next-open entry; confirmation-relative D+20 close exit",
                "feature_column": "",
                "feature_observed_column": "",
                "feature_independence_status": "baseline_not_applicable",
                "equivalent_to_feature_id": "",
                "feature_observed_count": baseline["accepted_trade_count"],
                "feature_coverage_pct": 100.0 if baseline["accepted_trade_count"] else "",
                "feature_hit_count": baseline["accepted_trade_count"],
                "evidence_interpretation": "baseline_anchor",
                **baseline,
            }
        )
        realized = _numeric(part, "realized_return_pct")
        group_masks = {
            "high_return": realized.ge(8.0),
            "win": realized.ge(5.0),
            "failure": realized.lt(0.0),
        }
        prior_masks: list[tuple[str, pd.Series]] = []
        for spec in binary_specs:
            feature_id = safe_str(spec["feature_id"])
            feature_column = f"feature__{feature_id}"
            observed_column = f"feature_observed__{feature_id}"
            observed = _boolish(part[observed_column])
            hit = _boolish(part[feature_column]) & observed
            equivalent_to = next(
                (prior_id for prior_id, prior_mask in prior_masks if hit.equals(prior_mask)),
                "",
            ) if hit.any() else ""
            if hit.any():
                prior_masks.append((feature_id, hit))
            selected = part[hit]
            metrics = _outcome_metrics(selected)
            group_values: dict[str, Any] = {}
            for group_id, group_mask in group_masks.items():
                group_count = int(group_mask.sum())
                observed_count = int((group_mask & observed).sum())
                hit_count = int((group_mask & hit).sum())
                group_values[f"{group_id}_group_count"] = group_count
                group_values[f"{group_id}_feature_observed_count"] = observed_count
                group_values[f"{group_id}_feature_hit_count"] = hit_count
                group_values[f"{group_id}_feature_hit_rate_pct"] = _rate(hit_count, group_count)
                group_values[f"{group_id}_feature_hit_rate_within_observed_pct"] = _rate(
                    hit_count,
                    observed_count,
                )
            observed_discrimination = _delta(
                group_values["high_return_feature_hit_rate_within_observed_pct"],
                group_values["failure_feature_hit_rate_within_observed_pct"],
            )
            rows.append(
                {
                    **common,
                    "row_type": "binary_feature",
                    "feature_order": spec["feature_order"],
                    "feature_id": feature_id,
                    "feature_family": spec["feature_family"],
                    "feature_rule": f"{spec['feature_rule']} evaluated at {time_basis}",
                    "feature_column": feature_column,
                    "feature_observed_column": observed_column,
                    "feature_independence_status": (
                        "no_observed_hits_not_evaluable"
                        if not hit.any()
                        else "duplicate_mask_not_independent_evidence"
                        if equivalent_to
                        else "distinct_observed_mask"
                    ),
                    "equivalent_to_feature_id": equivalent_to,
                    "feature_observed_count": int(observed.sum()),
                    "feature_coverage_pct": _rate(int(observed.sum()), len(part)),
                    "feature_hit_count": int(hit.sum()),
                    "feature_hit_rate_within_observed_pct": _rate(int(hit.sum()), int(observed.sum())),
                    **group_values,
                    "high_return_minus_failure_hit_rate_pct": _delta(
                        group_values["high_return_feature_hit_rate_pct"],
                        group_values["failure_feature_hit_rate_pct"],
                    ),
                    "high_return_minus_failure_hit_rate_within_observed_pct": observed_discrimination,
                    "delta_vs_baseline_win_rate_pct": _delta(metrics["win_rate_pct"], baseline["win_rate_pct"]),
                    "delta_vs_baseline_failure_rate_pct": _delta(
                        metrics["failure_rate_pct"], baseline["failure_rate_pct"]
                    ),
                    "delta_vs_baseline_avg_return_pct": _delta(
                        metrics["avg_realized_return_pct"], baseline["avg_realized_return_pct"]
                    ),
                    "delta_vs_baseline_median_return_pct": _delta(
                        metrics["median_realized_return_pct"], baseline["median_realized_return_pct"]
                    ),
                    "delta_vs_baseline_high_return_8_rate_pct": _delta(
                        metrics["high_return_8_rate_pct"], baseline["high_return_8_rate_pct"]
                    ),
                    "delta_vs_baseline_loss_5_rate_pct": _delta(
                        metrics["loss_5_rate_pct"], baseline["loss_5_rate_pct"]
                    ),
                    "evidence_interpretation": _feature_interpretation(
                        metrics,
                        baseline,
                        observed_discrimination,
                    ),
                    **metrics,
                }
            )
        for order, feature_id, family, column in numeric_specs:
            observed = numeric_feature_observed_mask(part, family, column)
            rows.append(
                {
                    **common,
                    "row_type": "numeric_feature",
                    "feature_order": order,
                    "feature_id": feature_id,
                    "feature_family": family,
                    "feature_rule": f"compare {column} between high-return, win, and failure groups at {time_basis}",
                    "feature_column": column,
                    "feature_observed_column": column,
                    "feature_independence_status": "numeric_contrast_not_binary_mask",
                    "equivalent_to_feature_id": "",
                    "feature_observed_count": int(observed.sum()),
                    "feature_coverage_pct": _rate(int(observed.sum()), len(part)),
                    "feature_hit_count": "",
                    "evidence_interpretation": "numeric_high_return_vs_failure_contrast_only",
                    **_numeric_group_stats(part, column, observed),
                }
            )
    summary = pd.DataFrame(rows)
    summary["candidate_threshold_sensitivity_direction_status"] = "not_applicable"
    decision_rows = summary[summary["anomaly_exclusion_basis"].eq(DECISION_BASIS)]
    sensitivity_rows = summary[
        summary["anomaly_exclusion_basis"].eq(RETURN_ANOMALY_CANDIDATE_SENSITIVITY_BASIS)
    ]
    sensitivity_map = sensitivity_rows.set_index(["feature_time_basis", "row_type", "feature_id"]).to_dict("index")
    for index, row in decision_rows.iterrows():
        counterpart = sensitivity_map.get((row["feature_time_basis"], row["row_type"], row["feature_id"]))
        if counterpart is None:
            summary.loc[index, "candidate_threshold_sensitivity_direction_status"] = (
                "missing_sensitivity_counterpart"
            )
        elif row["row_type"] == "binary_feature":
            left = safe_str(row.get("evidence_interpretation"))
            right = safe_str(counterpart.get("evidence_interpretation"))
            summary.loc[index, "candidate_threshold_sensitivity_direction_status"] = (
                "stable_positive" if left.startswith("positive_") and right.startswith("positive_")
                else "stable_risk" if left.startswith("failure_") and right.startswith("failure_")
                else "mixed_or_unstable"
            )
        elif row["row_type"] == "numeric_feature":
            left = pd.to_numeric(pd.Series([row.get("high_return_minus_failure_feature_mean")]), errors="coerce").iloc[0]
            right = pd.to_numeric(
                pd.Series([counterpart.get("high_return_minus_failure_feature_mean")]), errors="coerce"
            ).iloc[0]
            summary.loc[index, "candidate_threshold_sensitivity_direction_status"] = (
                "stable_same_direction"
                if pd.notna(left) and pd.notna(right) and (left == 0 or right == 0 or (left > 0) == (right > 0))
                else "mixed_or_unstable"
            )
        else:
            summary.loc[index, "candidate_threshold_sensitivity_direction_status"] = (
                "baseline_sensitivity_published"
            )
    return summary.sort_values(
        ["anomaly_exclusion_basis", "feature_time_basis", "row_type", "feature_order", "feature_id"],
        kind="mergesort",
    ).reset_index(drop=True)


def build_fixed_confirmation_feature_contrast(
    prepared_frame: pd.DataFrame,
    timing_summary: pd.DataFrame,
    *,
    binary_specs: list[dict[str, Any]],
    numeric_specs: list[tuple[int, str, str, str]],
) -> tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    generated_at = now_text()
    detail = _build_detail(prepared_frame, binary_specs, numeric_specs, generated_at)
    anomaly = _anomaly_audit(detail)
    summary = _summary(detail, anomaly, timing_summary, binary_specs, numeric_specs)
    return summary, detail, anomaly


def write_fixed_confirmation_feature_contrast(
    summary: pd.DataFrame,
    detail: pd.DataFrame,
    anomaly: pd.DataFrame,
) -> None:
    for frame, latest, history, docs in (
        (summary, SUMMARY_CSV, HISTORY_SUMMARY_CSV, DOCS_SUMMARY_CSV),
        (anomaly, ANOMALY_CSV, HISTORY_ANOMALY_CSV, DOCS_ANOMALY_CSV),
    ):
        write_csv(frame, latest)
        write_csv(frame, history)
        write_csv(frame, docs)
    write_csv(detail, DETAIL_CSV)

    decision = summary[summary["anomaly_exclusion_basis"].eq(DECISION_BASIS)]
    positive = decision[
        decision["row_type"].eq("binary_feature")
        & decision["feature_independence_status"].eq("distinct_observed_mask")
        & decision["candidate_threshold_sensitivity_direction_status"].eq("stable_positive")
    ].copy()
    positive["_sort"] = pd.to_numeric(
        positive["high_return_minus_failure_hit_rate_within_observed_pct"], errors="coerce"
    )
    positive = positive.sort_values(["feature_time_basis", "_sort"], ascending=[True, False])
    risk = decision[
        decision["row_type"].eq("binary_feature")
        & decision["candidate_threshold_sensitivity_direction_status"].eq("stable_risk")
    ].copy()
    lines = [
        "# 營收低反應模型：固定確認口徑勝敗特徵比較",
        "",
        f"- generated_at: `{safe_str(summary['generated_at'].iloc[0])}`",
        "- status: `blocked_pending_root_cause_anomaly_candidate_review`",
        "- 固定候選：強月營收且股價仍在近期 23 日區間、攻擊尚未開始。",
        "- 固定確認：候選後最多三個交易日，收盤突破候選日前 23 日最高收盤價。",
        "- 固定操作：確認後次一交易日開盤進場；確認日 D+20 收盤出場；本輪不加停損。",
        "- 特徵時點：分開比較候選訊號日收盤已知與確認日收盤已知資訊，兩者不得混用。",
        "- 去重：同股操作區間不得重疊；decision basis 同股同月營收期間不得重複計算。",
        "- 候選異常：|報酬| >= 80% 只產生 anomaly candidate；未完成底層根因查核前不得定名為極端值。",
        "- 門檻敏感度：另列排除候選列的數字影響，但不得稱為異常排除、修正後績效或 promotion evidence。",
        "- 月營收候選：未完成底層根因查核前，交易與已觀測 feature value 都保留在 primary evidence；候選排除只能另列 sensitivity。",
        "- 條件政策：本 artifact 只比較單一特徵，不任意疊條件；組合必須另行真實重算。",
        "- 樣本政策：樣本數揭露但不單獨作為否定條件。",
        "- 財務範圍：本輪僅使用 PIT 月營收；EPS、毛利率、營益率、營業利益、業外、淨利及季／年財報全部排除。",
        "- production_change: `none`",
        "",
        "## 數字異常檢查",
        "",
        markdown_table(
            anomaly,
            [
                "anomaly_exclusion_basis",
                "accepted_trade_count",
                "same_stock_overlap_pair_count",
                "same_stock_revenue_period_repeat_count",
                "price_path_anomaly_candidate_count",
                "return_abs_ge80_anomaly_candidate_count",
                "source_revenue_or_price_anomaly_candidate_count",
                "signal_feature_context_revenue_anomaly_candidate_count",
                "confirmation_feature_context_revenue_anomaly_candidate_count",
                "feature_context_candidate_values_retained_in_feature_evidence",
                "max_realized_return_pct",
                "max_return_stock_id",
                "max_return_signal_date",
                "min_realized_return_pct",
                "min_return_stock_id",
                "min_return_signal_date",
                "top1_abs_return_share_pct",
                "top5_abs_return_share_pct",
                "avg_realized_return_pct",
                "median_realized_return_pct",
                "trimmed_1pct_avg_return_pct",
                "interpretation_status",
            ],
            limit=10,
        ),
        "",
        "## 固定基準",
        "",
        markdown_table(
            decision[decision["row_type"].eq("baseline")],
            [
                "feature_time_basis_zh",
                "accepted_trade_count",
                "win_rate_pct",
                "neutral_rate_pct",
                "failure_rate_pct",
                "avg_realized_return_pct",
                "median_realized_return_pct",
                "high_return_8_rate_pct",
                "loss_5_rate_pct",
                "timing_accepted_trade_count_parity_status",
            ],
            limit=10,
        ),
        "",
        "## 成功共同特徵候選",
        "",
        markdown_table(
            positive,
            [
                "feature_time_basis_zh",
                "feature_id",
                "feature_family",
                "feature_observed_count",
                "feature_hit_count",
                "high_return_feature_hit_rate_within_observed_pct",
                "failure_feature_hit_rate_within_observed_pct",
                "high_return_minus_failure_hit_rate_within_observed_pct",
                "win_rate_pct",
                "neutral_rate_pct",
                "failure_rate_pct",
                "avg_realized_return_pct",
                "median_realized_return_pct",
                "loss_5_rate_pct",
                "candidate_threshold_sensitivity_direction_status",
            ],
            limit=40,
        ),
        "",
        "## 失敗共同特徵候選",
        "",
        markdown_table(
            risk,
            [
                "feature_time_basis_zh",
                "feature_id",
                "feature_family",
                "feature_observed_count",
                "feature_hit_count",
                "high_return_feature_hit_rate_within_observed_pct",
                "failure_feature_hit_rate_within_observed_pct",
                "high_return_minus_failure_hit_rate_within_observed_pct",
                "win_rate_pct",
                "failure_rate_pct",
                "avg_realized_return_pct",
                "median_realized_return_pct",
                "loss_5_rate_pct",
                "candidate_threshold_sensitivity_direction_status",
            ],
            limit=40,
        ),
        "",
        "## Large Detail Policy",
        "",
        f"逐筆重算 evidence 僅保留於 `{DETAIL_CSV.as_posix()}`；不複製到 docs/latest 或 output/history。",
    ]
    SUMMARY_MD.parent.mkdir(parents=True, exist_ok=True)
    SUMMARY_MD.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8", newline="\n")
    DOCS_SUMMARY_MD.parent.mkdir(parents=True, exist_ok=True)
    DOCS_SUMMARY_MD.write_text(SUMMARY_MD.read_text(encoding="utf-8"), encoding="utf-8", newline="\n")
