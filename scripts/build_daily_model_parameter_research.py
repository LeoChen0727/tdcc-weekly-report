from __future__ import annotations

import math
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Callable

import numpy as np
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent))

from research_weekly_20pct_surge_volume import build_stock_day_frame  # noqa: E402
from research_weekly_surge_technical_grid import add_technical_features  # noqa: E402
from research_weekly_surge_theme_segments import attach_theme_labels  # noqa: E402
from build_daily_candidate_model_layer import build_parameter_table, build_specs, cond_pullback  # noqa: E402
from build_approved_operation_patterns import (  # noqa: E402
    NECKLINE_APPROVAL_METRICS,
    NECKLINE_OPERATION_MODULE_ID,
    PRICE_PULLBACK_OPERATION_MODULE_ID,
    V2_APPROVAL_METRICS,
    V2_HIGH_MODEL_ID,
    W_BOTTOM_APPROVAL_METRICS,
    W_BOTTOM_OPERATION_MODULE_ID,
)
from tracking_utils import (  # noqa: E402
    DOCS_LATEST_DIR,
    LATEST_DIR,
    RESEARCH_LATEST_DIR,
    markdown_table,
    normalize_code,
    normalize_date,
    now_text,
    safe_str,
    write_csv,
)


HISTORY_DIR = Path("output/history/research")
DAILY_SNAPSHOT_DIR = Path("output/history/daily_model_snapshots")
OUT_CSV = LATEST_DIR / "daily_model_parameter_research_latest.csv"
OUT_MD = LATEST_DIR / "daily_model_parameter_research_latest.md"
OUT_DETAIL_CSV = LATEST_DIR / "daily_model_parameter_research_horizon_detail_latest.csv"
OUT_DETAIL_MD = LATEST_DIR / "daily_model_parameter_research_horizon_detail_latest.md"
OUT_PARITY_CSV = RESEARCH_LATEST_DIR / "daily_model_research_parity_latest.csv"
OUT_PARITY_MD = RESEARCH_LATEST_DIR / "daily_model_research_parity_latest.md"
HIGH_POSITION_AUDIT_DETAIL_CSV = (
    RESEARCH_LATEST_DIR / "volume_range_breakout_v2_high_position_improvement_audit_detail_latest.csv"
)
HISTORY_CSV = HISTORY_DIR / "daily_model_parameter_research.csv"
DOCS_CSV = DOCS_LATEST_DIR / OUT_CSV.name
DOCS_MD = DOCS_LATEST_DIR / OUT_MD.name
DOCS_DETAIL_CSV = DOCS_LATEST_DIR / OUT_DETAIL_CSV.name
DOCS_DETAIL_MD = DOCS_LATEST_DIR / OUT_DETAIL_MD.name
DOCS_PARITY_CSV = DOCS_LATEST_DIR / OUT_PARITY_CSV.name
DOCS_PARITY_MD = DOCS_LATEST_DIR / OUT_PARITY_MD.name
PRICE_PULLBACK_OPERATION_CSV = RESEARCH_LATEST_DIR / "price_pullback_23ema_operation_research_latest.csv"
PRICE_PULLBACK_OPERATION_MD = RESEARCH_LATEST_DIR / "price_pullback_23ema_operation_research_latest.md"
PRICE_PULLBACK_OPERATION_HISTORY_CSV = HISTORY_DIR / "price_pullback_23ema_operation_research.csv"
DOCS_PRICE_PULLBACK_OPERATION_CSV = DOCS_LATEST_DIR / PRICE_PULLBACK_OPERATION_CSV.name
DOCS_PRICE_PULLBACK_OPERATION_MD = DOCS_LATEST_DIR / PRICE_PULLBACK_OPERATION_MD.name
PRICE_PULLBACK_TIME_COST_CSV = RESEARCH_LATEST_DIR / "price_pullback_23ema_time_cost_backtest_latest.csv"
PRICE_PULLBACK_TIME_COST_MD = RESEARCH_LATEST_DIR / "price_pullback_23ema_time_cost_backtest_latest.md"
PRICE_PULLBACK_TIME_COST_HISTORY_CSV = HISTORY_DIR / "price_pullback_23ema_time_cost_backtest.csv"
DOCS_PRICE_PULLBACK_TIME_COST_CSV = DOCS_LATEST_DIR / PRICE_PULLBACK_TIME_COST_CSV.name
DOCS_PRICE_PULLBACK_TIME_COST_MD = DOCS_LATEST_DIR / PRICE_PULLBACK_TIME_COST_MD.name
PRICE_PULLBACK_OPERATION_MODULE_CSV = RESEARCH_LATEST_DIR / "price_pullback_23ema_operation_module_research_latest.csv"
PRICE_PULLBACK_OPERATION_MODULE_MD = RESEARCH_LATEST_DIR / "price_pullback_23ema_operation_module_research_latest.md"
PRICE_PULLBACK_OPERATION_MODULE_HISTORY_CSV = HISTORY_DIR / "price_pullback_23ema_operation_module_research.csv"
DOCS_PRICE_PULLBACK_OPERATION_MODULE_CSV = DOCS_LATEST_DIR / PRICE_PULLBACK_OPERATION_MODULE_CSV.name
DOCS_PRICE_PULLBACK_OPERATION_MODULE_MD = DOCS_LATEST_DIR / PRICE_PULLBACK_OPERATION_MODULE_MD.name
PRICE_PULLBACK_FEATURE_CONFIRMATION_CSV = (
    RESEARCH_LATEST_DIR / "price_pullback_23ema_feature_confirmation_research_latest.csv"
)
PRICE_PULLBACK_FEATURE_CONFIRMATION_MD = (
    RESEARCH_LATEST_DIR / "price_pullback_23ema_feature_confirmation_research_latest.md"
)
PRICE_PULLBACK_FEATURE_CONFIRMATION_HISTORY_CSV = HISTORY_DIR / "price_pullback_23ema_feature_confirmation_research.csv"
DOCS_PRICE_PULLBACK_FEATURE_CONFIRMATION_CSV = DOCS_LATEST_DIR / PRICE_PULLBACK_FEATURE_CONFIRMATION_CSV.name
DOCS_PRICE_PULLBACK_FEATURE_CONFIRMATION_MD = DOCS_LATEST_DIR / PRICE_PULLBACK_FEATURE_CONFIRMATION_MD.name
PRICE_PULLBACK_DAILY_ROW_PARITY_CSV = (
    RESEARCH_LATEST_DIR / "price_pullback_23ema_daily_row_parity_latest.csv"
)
PRICE_PULLBACK_DAILY_ROW_PARITY_MD = (
    RESEARCH_LATEST_DIR / "price_pullback_23ema_daily_row_parity_latest.md"
)
PRICE_PULLBACK_DAILY_ROW_PARITY_HISTORY_CSV = HISTORY_DIR / "price_pullback_23ema_daily_row_parity.csv"
DOCS_PRICE_PULLBACK_DAILY_ROW_PARITY_CSV = DOCS_LATEST_DIR / PRICE_PULLBACK_DAILY_ROW_PARITY_CSV.name
DOCS_PRICE_PULLBACK_DAILY_ROW_PARITY_MD = DOCS_LATEST_DIR / PRICE_PULLBACK_DAILY_ROW_PARITY_MD.name
PRICE_PULLBACK_DECISION_AUDIT_CSV = (
    RESEARCH_LATEST_DIR / "price_pullback_23ema_model_decision_audit_latest.csv"
)
PRICE_PULLBACK_DECISION_AUDIT_MD = RESEARCH_LATEST_DIR / "price_pullback_23ema_model_decision_audit_latest.md"
PRICE_PULLBACK_DECISION_AUDIT_HISTORY_CSV = HISTORY_DIR / "price_pullback_23ema_model_decision_audit.csv"
DOCS_PRICE_PULLBACK_DECISION_AUDIT_CSV = DOCS_LATEST_DIR / PRICE_PULLBACK_DECISION_AUDIT_CSV.name
DOCS_PRICE_PULLBACK_DECISION_AUDIT_MD = DOCS_LATEST_DIR / PRICE_PULLBACK_DECISION_AUDIT_MD.name
PRICE_PULLBACK_EXIT_RULE_COMPARISON_CSV = (
    RESEARCH_LATEST_DIR / "price_pullback_23ema_exit_rule_comparison_latest.csv"
)
PRICE_PULLBACK_EXIT_RULE_COMPARISON_MD = (
    RESEARCH_LATEST_DIR / "price_pullback_23ema_exit_rule_comparison_latest.md"
)
PRICE_PULLBACK_EXIT_RULE_COMPARISON_HISTORY_CSV = HISTORY_DIR / "price_pullback_23ema_exit_rule_comparison.csv"
DOCS_PRICE_PULLBACK_EXIT_RULE_COMPARISON_CSV = DOCS_LATEST_DIR / PRICE_PULLBACK_EXIT_RULE_COMPARISON_CSV.name
DOCS_PRICE_PULLBACK_EXIT_RULE_COMPARISON_MD = DOCS_LATEST_DIR / PRICE_PULLBACK_EXIT_RULE_COMPARISON_MD.name
DAILY_SIGNAL_BACKGROUND_FEATURE_PANEL_CSV = (
    RESEARCH_LATEST_DIR / "daily_model_signal_background_feature_panel_latest.csv"
)
MONTHLY_REVENUE_POINT_IN_TIME_PANEL_CSV = (
    RESEARCH_LATEST_DIR / "monthly_revenue_point_in_time_panel_latest.csv"
)
PRICE_PULLBACK_CONTINUATION_WIN_PROFILE_CSV = (
    RESEARCH_LATEST_DIR / "price_pullback_23ema_continuation_win_profile_latest.csv"
)
PRICE_PULLBACK_CONTINUATION_WIN_PROFILE_MD = (
    RESEARCH_LATEST_DIR / "price_pullback_23ema_continuation_win_profile_latest.md"
)
PRICE_PULLBACK_CONTINUATION_WIN_PROFILE_HISTORY_CSV = (
    HISTORY_DIR / "price_pullback_23ema_continuation_win_profile.csv"
)
DOCS_PRICE_PULLBACK_CONTINUATION_WIN_PROFILE_CSV = (
    DOCS_LATEST_DIR / PRICE_PULLBACK_CONTINUATION_WIN_PROFILE_CSV.name
)
DOCS_PRICE_PULLBACK_CONTINUATION_WIN_PROFILE_MD = (
    DOCS_LATEST_DIR / PRICE_PULLBACK_CONTINUATION_WIN_PROFILE_MD.name
)
PRICE_PULLBACK_RESEARCH_SCORE_BUCKET_CSV = (
    RESEARCH_LATEST_DIR / "price_pullback_23ema_research_score_bucket_latest.csv"
)
PRICE_PULLBACK_RESEARCH_SCORE_BUCKET_MD = (
    RESEARCH_LATEST_DIR / "price_pullback_23ema_research_score_bucket_latest.md"
)
PRICE_PULLBACK_RESEARCH_SCORE_BUCKET_HISTORY_CSV = HISTORY_DIR / "price_pullback_23ema_research_score_bucket.csv"
DOCS_PRICE_PULLBACK_RESEARCH_SCORE_BUCKET_CSV = DOCS_LATEST_DIR / PRICE_PULLBACK_RESEARCH_SCORE_BUCKET_CSV.name
DOCS_PRICE_PULLBACK_RESEARCH_SCORE_BUCKET_MD = DOCS_LATEST_DIR / PRICE_PULLBACK_RESEARCH_SCORE_BUCKET_MD.name
PRICE_PULLBACK_HIGH_RETURN_SCORE_GRID_CSV = (
    RESEARCH_LATEST_DIR / "price_pullback_23ema_high_return_feature_score_grid_latest.csv"
)
PRICE_PULLBACK_HIGH_RETURN_SCORE_GRID_MD = (
    RESEARCH_LATEST_DIR / "price_pullback_23ema_high_return_feature_score_grid_latest.md"
)
PRICE_PULLBACK_HIGH_RETURN_SCORE_GRID_HISTORY_CSV = (
    HISTORY_DIR / "price_pullback_23ema_high_return_feature_score_grid.csv"
)
DOCS_PRICE_PULLBACK_HIGH_RETURN_SCORE_GRID_CSV = (
    DOCS_LATEST_DIR / PRICE_PULLBACK_HIGH_RETURN_SCORE_GRID_CSV.name
)
DOCS_PRICE_PULLBACK_HIGH_RETURN_SCORE_GRID_MD = DOCS_LATEST_DIR / PRICE_PULLBACK_HIGH_RETURN_SCORE_GRID_MD.name
PRICE_PULLBACK_ORDERED_CONDITION_MATRIX_CSV = (
    RESEARCH_LATEST_DIR / "price_pullback_23ema_ordered_condition_matrix_latest.csv"
)
PRICE_PULLBACK_ORDERED_CONDITION_MATRIX_MD = (
    RESEARCH_LATEST_DIR / "price_pullback_23ema_ordered_condition_matrix_latest.md"
)
PRICE_PULLBACK_ORDERED_CONDITION_MATRIX_HISTORY_CSV = (
    HISTORY_DIR / "price_pullback_23ema_ordered_condition_matrix.csv"
)
DOCS_PRICE_PULLBACK_ORDERED_CONDITION_MATRIX_CSV = (
    DOCS_LATEST_DIR / PRICE_PULLBACK_ORDERED_CONDITION_MATRIX_CSV.name
)
DOCS_PRICE_PULLBACK_ORDERED_CONDITION_MATRIX_MD = DOCS_LATEST_DIR / PRICE_PULLBACK_ORDERED_CONDITION_MATRIX_MD.name
PRICE_PULLBACK_LIFECYCLE_REPLAY_CSV = (
    RESEARCH_LATEST_DIR / "price_pullback_23ema_lifecycle_replay_latest.csv"
)
PRICE_PULLBACK_LIFECYCLE_REPLAY_MD = (
    RESEARCH_LATEST_DIR / "price_pullback_23ema_lifecycle_replay_latest.md"
)
PRICE_PULLBACK_LIFECYCLE_REPLAY_HISTORY_CSV = (
    HISTORY_DIR / "price_pullback_23ema_lifecycle_replay.csv"
)
DOCS_PRICE_PULLBACK_LIFECYCLE_REPLAY_CSV = DOCS_LATEST_DIR / PRICE_PULLBACK_LIFECYCLE_REPLAY_CSV.name
DOCS_PRICE_PULLBACK_LIFECYCLE_REPLAY_MD = DOCS_LATEST_DIR / PRICE_PULLBACK_LIFECYCLE_REPLAY_MD.name
FULL_MONTHLY_REVENUE_HISTORY_CSV = Path("data/monthly_revenue_history/monthly_revenue_history.csv")
PRICE_PULLBACK_REVENUE_CONDITION_MATRIX_CSV = (
    RESEARCH_LATEST_DIR / "price_pullback_23ema_revenue_condition_matrix_latest.csv"
)
PRICE_PULLBACK_REVENUE_CONDITION_MATRIX_MD = (
    RESEARCH_LATEST_DIR / "price_pullback_23ema_revenue_condition_matrix_latest.md"
)
PRICE_PULLBACK_REVENUE_CONDITION_MATRIX_HISTORY_CSV = (
    HISTORY_DIR / "price_pullback_23ema_revenue_condition_matrix.csv"
)
DOCS_PRICE_PULLBACK_REVENUE_CONDITION_MATRIX_CSV = (
    DOCS_LATEST_DIR / PRICE_PULLBACK_REVENUE_CONDITION_MATRIX_CSV.name
)
DOCS_PRICE_PULLBACK_REVENUE_CONDITION_MATRIX_MD = (
    DOCS_LATEST_DIR / PRICE_PULLBACK_REVENUE_CONDITION_MATRIX_MD.name
)
PRICE_PULLBACK_PROMOTION_MATRIX_CSV = (
    RESEARCH_LATEST_DIR / "price_pullback_23ema_promotion_matrix_latest.csv"
)
PRICE_PULLBACK_PROMOTION_MATRIX_MD = (
    RESEARCH_LATEST_DIR / "price_pullback_23ema_promotion_matrix_latest.md"
)
PRICE_PULLBACK_PROMOTION_MATRIX_HISTORY_CSV = HISTORY_DIR / "price_pullback_23ema_promotion_matrix.csv"
DOCS_PRICE_PULLBACK_PROMOTION_MATRIX_CSV = DOCS_LATEST_DIR / PRICE_PULLBACK_PROMOTION_MATRIX_CSV.name
DOCS_PRICE_PULLBACK_PROMOTION_MATRIX_MD = DOCS_LATEST_DIR / PRICE_PULLBACK_PROMOTION_MATRIX_MD.name
REVENUE_UNREACTED_CONDITION_MATRIX_CSV = (
    RESEARCH_LATEST_DIR / "revenue_unreacted_range_revenue_condition_matrix_latest.csv"
)
REVENUE_UNREACTED_CONDITION_MATRIX_MD = (
    RESEARCH_LATEST_DIR / "revenue_unreacted_range_revenue_condition_matrix_latest.md"
)
REVENUE_UNREACTED_CONDITION_MATRIX_HISTORY_CSV = (
    HISTORY_DIR / "revenue_unreacted_range_revenue_condition_matrix.csv"
)
DOCS_REVENUE_UNREACTED_CONDITION_MATRIX_CSV = DOCS_LATEST_DIR / REVENUE_UNREACTED_CONDITION_MATRIX_CSV.name
DOCS_REVENUE_UNREACTED_CONDITION_MATRIX_MD = DOCS_LATEST_DIR / REVENUE_UNREACTED_CONDITION_MATRIX_MD.name
REVENUE_UNREACTED_OPERATION_CANDIDATE_MATRIX_CSV = (
    RESEARCH_LATEST_DIR / "revenue_unreacted_range_operation_candidate_matrix_latest.csv"
)
REVENUE_UNREACTED_OPERATION_CANDIDATE_MATRIX_MD = (
    RESEARCH_LATEST_DIR / "revenue_unreacted_range_operation_candidate_matrix_latest.md"
)
REVENUE_UNREACTED_OPERATION_CANDIDATE_MATRIX_HISTORY_CSV = (
    HISTORY_DIR / "revenue_unreacted_range_operation_candidate_matrix.csv"
)
DOCS_REVENUE_UNREACTED_OPERATION_CANDIDATE_MATRIX_CSV = (
    DOCS_LATEST_DIR / REVENUE_UNREACTED_OPERATION_CANDIDATE_MATRIX_CSV.name
)
DOCS_REVENUE_UNREACTED_OPERATION_CANDIDATE_MATRIX_MD = (
    DOCS_LATEST_DIR / REVENUE_UNREACTED_OPERATION_CANDIDATE_MATRIX_MD.name
)

HORIZONS = list(range(1, 11)) + [20]
TIME_COST_HORIZON_DAYS = 20
TIME_COST_TARGET_PCT = 5.0
TIME_COST_STOP_PCT = -5.0
MIN_OK_SAMPLE = 100
MIN_REVIEW_SAMPLE = 30
PRICE_PULLBACK_KNOWN_DATA_QUALITY_EXCEPTIONS = [
    {
        "stock_id": "2380",
        "signal_date": "20260519",
        "exception_id": "2380_20260519_unadjusted_capital_reduction_resumption_gap",
        "exception_note": "unadjusted corporate-action/suspension-resumption price gap; research-only anomaly until adjusted basis is approved",
    },
]
PRICE_PULLBACK_INCLUDE_DATA_QUALITY_EXCEPTIONS = "including_data_quality_exceptions"
PRICE_PULLBACK_EXCLUDE_KNOWN_DATA_QUALITY_EXCEPTIONS = "excluding_known_data_quality_exceptions"
PRICE_PULLBACK_CANDIDATE_REPLAY_REQUIRED_COLUMNS = {
    "stock_id",
    "candidate_source_type",
    "candidate_line",
    "candidate_line_group",
    "source_row_index",
    "close",
    "ema23",
    "ma20",
    "distance_to_ema23_pct",
    "gap_ema23_pct",
    "platform_low",
    "short_platform_low",
    "previous_20d_low",
    "low_20",
    "ma5_turning_up_flag",
    "ma10_turning_up_flag",
}


@dataclass(frozen=True)
class RuleSpec:
    model_id: str
    model_name_zh: str
    parameter_set_id: str
    parameter_summary: str
    pdf_visibility: str
    condition: Callable[[pd.DataFrame], pd.Series]
    notes: str
    parameter_role: str = "parameter_variant"
    production_parity_status: str = "variant_not_baseline"
    parity_blocker: str = ""
    variant_of: str = ""


def pct(num: float) -> str:
    if math.isnan(num):
        return "-"
    return f"{num:.2f}%"


def sample_status(n: int) -> str:
    if n >= MIN_OK_SAMPLE:
        return "ok_first_pass"
    if n >= MIN_REVIEW_SAMPLE:
        return "small_sample_review_only"
    return "insufficient_sample"


def bool_series(df: pd.DataFrame, value: bool = False) -> pd.Series:
    return pd.Series(value, index=df.index)


def between(series: pd.Series, low: float, high: float) -> pd.Series:
    return (series >= low) & (series <= high)


def trueish(series: pd.Series) -> pd.Series:
    if series.dtype == bool:
        return series.fillna(False)
    return series.astype(str).str.lower().isin(["true", "1", "yes"])


def numeric_column(df: pd.DataFrame, name: str) -> pd.Series:
    if name not in df.columns:
        return pd.Series(math.nan, index=df.index)
    return pd.to_numeric(df[name], errors="coerce")


def trueish_column(df: pd.DataFrame, name: str) -> pd.Series:
    if name not in df.columns:
        return bool_series(df)
    return trueish(df[name])


def add_price_structure_features(df: pd.DataFrame) -> pd.DataFrame:
    out = df.sort_values(["stock_id", "date"]).copy()
    groups = out.groupby("stock_id", group_keys=False)

    if "ma5" not in out.columns:
        out["ma5"] = groups["close"].transform(lambda s: s.rolling(5, min_periods=3).mean())
    if "ma10" not in out.columns:
        out["ma10"] = groups["close"].transform(lambda s: s.rolling(10, min_periods=5).mean())
    out["ma5_turning_up_flag"] = out["ma5"] > groups["ma5"].shift(1)
    out["ma10_turning_up_flag"] = out["ma10"] > groups["ma10"].shift(1)
    out["ema23_prev5"] = groups["ema23"].shift(5)
    out["ema23_slope_5d_pct"] = (out["ema23"] / out["ema23_prev5"] - 1.0) * 100.0
    out["ema23_slope_pct"] = out["ema23_slope_5d_pct"]
    out["previous_close"] = groups["close"].shift(1)
    out["signal_return_1d_pct"] = (out["close"] / out["previous_close"] - 1.0) * 100.0
    out["return_45d_pct"] = groups["close"].pct_change(45) * 100.0
    out["close_above_open"] = out["close"] > out["open"]
    out["bullish_attack_candle"] = (out["close"] > out["open"]) | (
        out["close"].eq(out["open"]) & (out["close"] > out["previous_close"])
    )
    candle_range = (out["high"] - out["low"]).replace(0, pd.NA)
    out["body_ratio"] = (out["close"] - out["open"]).abs() / candle_range
    out["upper_shadow_ratio"] = (out["high"] - out[["close", "open"]].max(axis=1)) / candle_range
    out["close_location"] = (out["close"] - out["low"]) / candle_range
    out["solid_red_candle"] = (
        (out["close"] > out["open"])
        & (out["body_ratio"] >= 0.25)
        & (out["upper_shadow_ratio"] <= 0.35)
        & (out["close_location"] >= 0.65)
    )

    # build_stock_day_frame already calculates this with a per-stock previous
    # 20-day denominator. Keep the alias local to this research script so the
    # parameter rules read consistently.
    out["volume_ratio_prev20"] = out["start_day_volume_ratio_vs_prev20"]
    volume_ma20 = (
        groups["volume"]
        .shift(1)
        .rolling(20, min_periods=10)
        .mean()
        .reset_index(level=0, drop=True)
    )
    # Some sources store raw shares, others store lots. Normalize only clearly
    # share-denominated values so the liquidity rule remains stable.
    out["volume_ma20_lots"] = volume_ma20.where(volume_ma20 < 100000, volume_ma20 / 1000.0)
    obv_direction = np.sign(out["close"] - out["previous_close"]).fillna(0.0)
    obv_flow = obv_direction * pd.to_numeric(out["volume"], errors="coerce").fillna(0.0)
    out["obv"] = obv_flow.groupby(out["stock_id"]).cumsum()
    obv_groups = out.groupby("stock_id", group_keys=False)
    out["obv_ma20"] = obv_groups["obv"].transform(lambda s: s.rolling(20, min_periods=10).mean())
    out["obv_above_ma20"] = out["obv"] > out["obv_ma20"]
    out["obv_slope_5d"] = out["obv"] - obv_groups["obv"].shift(5)

    for window in [10, 20, 23, 30, 45, 60, 120]:
        high = groups["high"].shift(1).rolling(window, min_periods=max(5, min(window, 20))).max().reset_index(level=0, drop=True)
        low = groups["low"].shift(1).rolling(window, min_periods=max(5, min(window, 20))).min().reset_index(level=0, drop=True)
        out[f"range_high_{window}d_prev"] = high
        out[f"range_low_{window}d_prev"] = low
        out[f"range_width_{window}d_pct"] = (high / low - 1.0) * 100.0
        out[f"range_breakout_{window}d_pct"] = (out["close"] / high - 1.0) * 100.0
        out[f"distance_to_range_high_{window}d_pct"] = (out["close"] / high - 1.0) * 100.0

    range_45d = (out["range_high_45d_prev"] - out["range_low_45d_prev"]).replace(0, pd.NA)
    out["close_position_45d_pct"] = (out["close"] - out["range_low_45d_prev"]) / range_45d * 100.0
    range_120d = (out["range_high_120d_prev"] - out["range_low_120d_prev"]).replace(0, pd.NA)
    out["close_position_120d_pct"] = (out["close"] - out["range_low_120d_prev"]) / range_120d * 100.0

    for window in [20, 30, 60]:
        high = out[f"range_high_{window}d_prev"]
        low = out[f"range_low_{window}d_prev"]
        out[f"prior_extension_ema23_{window}d_pct"] = (high / out["ema23"] - 1.0) * 100.0
        out[f"prior_runup_{window}d_pct"] = (high / low - 1.0) * 100.0
        out[f"pullback_from_high_{window}d_pct"] = (out["close"] / high - 1.0) * 100.0

    out["distance_to_ema23_pct"] = out["distance_ema23_pct"]
    out["distance_23ema_pct"] = out["distance_ema23_pct"]
    out["gap_ema23_pct"] = out["distance_ema23_pct"]
    out["platform_high"] = out["range_high_20d_prev"]
    out["platform_low"] = out["range_low_20d_prev"]
    out["short_platform_high"] = out["range_high_10d_prev"]
    out["short_platform_low"] = out["range_low_10d_prev"]
    out["previous_20d_low"] = out["range_low_20d_prev"]
    out["low_20"] = out["range_low_20d_prev"]
    support_zone = (
        (out["previous_20d_low"] > 0)
        & (out["close"] >= out["previous_20d_low"] * 0.98)
        & (out["close"] <= out["previous_20d_low"] * 1.08)
    )
    out["pullback_entry_zone_flag"] = between(out["distance_ema23_pct"], -2.5, 5.0) | support_zone

    future_return_cols: dict[str, pd.Series] = {}
    for day in range(1, TIME_COST_HORIZON_DAYS + 2):
        future_open = groups["open"].shift(-day)
        future_return_cols[f"future_d{day}_open"] = future_open
        future_return_cols[f"next_open_to_d{day}_day_open_return_pct"] = (
            future_open / out["next_open"] - 1.0
        ) * 100.0
        if day > TIME_COST_HORIZON_DAYS:
            continue
        future_close = groups["close"].shift(-day)
        future_high = groups["high"].shift(-day)
        future_low = groups["low"].shift(-day)
        future_return_cols[f"next_open_to_d{day}_day_close_return_pct"] = (
            future_close / out["next_open"] - 1.0
        ) * 100.0
        future_return_cols[f"next_open_to_d{day}_day_high_return_pct"] = (future_high / out["next_open"] - 1.0) * 100.0
        future_return_cols[f"next_open_to_d{day}_day_low_return_pct"] = (future_low / out["next_open"] - 1.0) * 100.0
        future_return_cols[f"future_d{day}_ma5"] = groups["ma5"].shift(-day)
        future_return_cols[f"future_d{day}_ma20"] = groups["ma20"].shift(-day)
        future_return_cols[f"future_d{day}_ema23"] = groups["ema23"].shift(-day)
    out = pd.concat([out, pd.DataFrame(future_return_cols, index=out.index)], axis=1)

    range_pct = (out["high"] - out["low"]) / out["previous_close"].replace(0, pd.NA) * 100.0
    out["locked_limit_up_breakout"] = (
        (out["range_breakout_20d_pct"] >= 2.0)
        & (out["signal_return_1d_pct"] >= 9.0)
        & (out["close"] >= out["high"] * 0.995)
        & (out["open"] >= out["close"] * 0.995)
        & ((out["high"] == out["low"]) | (range_pct <= 1.0))
    )

    # A simple W-bottom proxy for research: the latest 35 trading days contain two
    # similar lows and the second low is higher, while price is back in the upper half.
    low_35 = groups["low"].shift(1).rolling(35, min_periods=25).min().reset_index(level=0, drop=True)
    low_18 = groups["low"].shift(1).rolling(18, min_periods=12).min().reset_index(level=0, drop=True)
    high_35 = groups["high"].shift(1).rolling(35, min_periods=25).max().reset_index(level=0, drop=True)
    out["w_bottom_proxy"] = (
        (low_18 >= low_35 * 0.98)
        & (low_18 <= low_35 * 1.12)
        & (out["close"] >= (low_35 + high_35) / 2)
        & (out["ema23_slope_5d_pct"] > 0)
    )
    return out


def attach_tdcc_features(df: pd.DataFrame) -> pd.DataFrame:
    rows: list[pd.DataFrame] = []
    tdcc_dir = Path("data/tdcc_stock_history")
    for path in sorted(tdcc_dir.glob("*.csv")):
        try:
            t = pd.read_csv(path, dtype={"stock_id": str}, keep_default_na=False)
        except Exception:
            continue
        if t.empty or "as_of_date" not in t.columns or "stock_id" not in t.columns:
            continue
        t = t.copy()
        t["stock_id"] = t["stock_id"].astype(str).str.extract(r"(\d+)")[0].str.zfill(4)
        t["tdcc_as_of_date"] = t["as_of_date"].astype(str).str.replace(r"\D", "", regex=True).str[:8]
        keep = [
            "stock_id",
            "tdcc_as_of_date",
            "tdcc_consecutive_up_weeks",
            "all_thresholds_up",
            "high_thresholds_up",
            "four_thresholds_sync_up",
            "over_400_change_1w",
            "over_800_change_1w",
            "over_1000_change_1w",
        ]
        for col in keep:
            if col not in t.columns:
                t[col] = ""
        rows.append(t[keep])
    if not rows:
        out = df.copy()
        out["tdcc_history_available"] = False
        return out

    tdcc = pd.concat(rows, ignore_index=True)
    tdcc["tdcc_date_dt"] = pd.to_datetime(tdcc["tdcc_as_of_date"], format="%Y%m%d", errors="coerce")
    for col in ["tdcc_consecutive_up_weeks", "over_400_change_1w", "over_800_change_1w", "over_1000_change_1w"]:
        tdcc[col] = pd.to_numeric(tdcc[col], errors="coerce")
    for col in ["all_thresholds_up", "high_thresholds_up", "four_thresholds_sync_up"]:
        tdcc[col] = tdcc[col].astype(str).str.lower().isin(["true", "1", "yes"])

    left = df.copy()
    left["price_date_dt"] = pd.to_datetime(left["date"].astype(str), format="%Y%m%d", errors="coerce")
    merged_parts: list[pd.DataFrame] = []
    for stock_id, price_part in left.groupby("stock_id", sort=False):
        tdcc_part = tdcc[tdcc["stock_id"].eq(stock_id)].sort_values("tdcc_date_dt")
        if tdcc_part.empty:
            p = price_part.copy()
            p["tdcc_history_available"] = False
            merged_parts.append(p)
            continue
        merged = pd.merge_asof(
            price_part.sort_values("price_date_dt"),
            tdcc_part.drop(columns=["stock_id"]).sort_values("tdcc_date_dt"),
            left_on="price_date_dt",
            right_on="tdcc_date_dt",
            direction="backward",
        )
        merged["tdcc_history_available"] = merged["tdcc_as_of_date"].notna()
        merged_parts.append(merged)
    out = pd.concat(merged_parts, ignore_index=True)
    return out


THEME_CONTEXT_JOIN_COLUMNS = [
    "theme_context_as_of_date",
    "theme_context_data_status",
    "theme_context_name",
    "theme_context_final_status",
    "theme_context_status_group",
    "theme_context_source_type",
    "theme_context_line_group",
    "theme_context_line",
    "theme_context_two_line_overlap",
    "theme_context_priority",
    "theme_context_tdcc_status",
    "theme_context_warrant_flow_signal",
    "theme_context_volume_ratio",
    "theme_context_return_20d_pct",
    "theme_context_repeat_label",
    "theme_context_volume_breakout_type",
    "theme_context_volume_bucket",
    "theme_context_volume_attack_status",
    "theme_context_volume_attack_selected",
    "theme_context_volume_attack_watch",
    "theme_context_volume_attack_failed",
    "theme_context_source_artifact",
]
MONTHLY_REVENUE_CONTEXT_JOIN_COLUMNS = [
    "monthly_revenue_context_as_of_date",
    "monthly_revenue_rows_as_of",
    "monthly_revenue_future_rows_ignored",
    "monthly_revenue_data_status",
    "monthly_revenue_period",
    "monthly_revenue_latest_yoy_pct",
    "monthly_revenue_cumulative_yoy_pct",
    "monthly_revenue_positive_flag",
    "monthly_revenue_strong_flag",
    "monthly_revenue_good_eps_unconfirmed_flag",
    "monthly_revenue_numerical_anomaly_flag",
    "monthly_revenue_source_artifact",
    "monthly_revenue_formal_model_use_allowed",
]


def attach_signal_background_features(
    df: pd.DataFrame,
    panel_path: Path = DAILY_SIGNAL_BACKGROUND_FEATURE_PANEL_CSV,
) -> pd.DataFrame:
    out = df.copy()
    if not panel_path.exists():
        out["theme_context_data_status"] = "missing_signal_background_panel"
        out["theme_context_ready"] = False
        out["theme_context_mainstream_supported"] = False
        out["theme_context_leadership_supported"] = False
        out["theme_context_overheated"] = False
        out["theme_context_volume_attack_selected_flag"] = False
        out["monthly_revenue_data_status"] = "missing_signal_background_panel"
        out["monthly_revenue_context_ready"] = False
        out["monthly_revenue_positive_or_strong"] = False
        out["monthly_revenue_numerical_anomaly_flag"] = False
        out["monthly_revenue_formal_model_use_allowed"] = False
        return out

    panel = pd.read_csv(panel_path, dtype=str, keep_default_na=False)
    if panel.empty or not {"stock_id", "signal_date"}.issubset(panel.columns):
        out["theme_context_data_status"] = "missing_signal_background_panel"
        out["theme_context_ready"] = False
        out["theme_context_mainstream_supported"] = False
        out["theme_context_leadership_supported"] = False
        out["theme_context_overheated"] = False
        out["theme_context_volume_attack_selected_flag"] = False
        out["monthly_revenue_data_status"] = "missing_signal_background_panel"
        out["monthly_revenue_context_ready"] = False
        out["monthly_revenue_positive_or_strong"] = False
        out["monthly_revenue_numerical_anomaly_flag"] = False
        out["monthly_revenue_formal_model_use_allowed"] = False
        return out

    keep = [
        "stock_id",
        "signal_date",
        *[col for col in THEME_CONTEXT_JOIN_COLUMNS if col in panel.columns],
        *[col for col in MONTHLY_REVENUE_CONTEXT_JOIN_COLUMNS if col in panel.columns],
    ]
    background = panel[keep].copy()
    background["stock_id"] = background["stock_id"].map(normalize_code)
    background["date"] = background["signal_date"].map(normalize_date)
    background = background.drop(columns=["signal_date"]).drop_duplicates(["stock_id", "date"], keep="last")
    for col in [
        "theme_context_priority",
        "theme_context_volume_ratio",
        "theme_context_return_20d_pct",
        "monthly_revenue_latest_yoy_pct",
        "monthly_revenue_cumulative_yoy_pct",
    ]:
        if col in background.columns:
            background[col] = pd.to_numeric(background[col], errors="coerce")

    left = out.copy()
    left["stock_id"] = left["stock_id"].map(normalize_code)
    left["date"] = left["date"].map(normalize_date)
    merged = left.merge(background, on=["stock_id", "date"], how="left")
    merged["theme_context_data_status"] = merged["theme_context_data_status"].fillna("no_signal_background_row")
    for col in THEME_CONTEXT_JOIN_COLUMNS:
        if col not in merged.columns:
            merged[col] = ""
    merged["monthly_revenue_data_status"] = merged["monthly_revenue_data_status"].fillna(
        "no_signal_background_row"
    )
    for col in MONTHLY_REVENUE_CONTEXT_JOIN_COLUMNS:
        if col not in merged.columns:
            merged[col] = ""
    ready_statuses = {"ready_exact_signal_date", "ready_previous_signal_date"}
    merged["theme_context_ready"] = merged["theme_context_data_status"].astype(str).isin(ready_statuses)
    merged["theme_context_mainstream_supported"] = merged["theme_context_ready"] & merged[
        "theme_context_status_group"
    ].astype(str).isin({"mainstream_supported", "mainstream_overheated"})
    merged["theme_context_leadership_supported"] = merged["theme_context_ready"] & merged[
        "theme_context_final_status"
    ].astype(str).isin({"mainstream_leader", "mainstream_follow_through", "emerging_theme"})
    merged["theme_context_overheated"] = merged["theme_context_ready"] & merged[
        "theme_context_status_group"
    ].astype(str).eq("mainstream_overheated")
    merged["theme_context_volume_attack_selected_flag"] = trueish_column(
        merged,
        "theme_context_volume_attack_selected",
    )
    revenue_ready_statuses = {"ready_exact_signal_date", "ready_previous_snapshot_date"}
    merged["monthly_revenue_context_ready"] = merged["monthly_revenue_data_status"].astype(str).isin(
        revenue_ready_statuses
    )
    merged["monthly_revenue_positive_or_strong"] = merged["monthly_revenue_context_ready"] & (
        trueish_column(merged, "monthly_revenue_positive_flag")
        | trueish_column(merged, "monthly_revenue_strong_flag")
    )
    merged["monthly_revenue_numerical_anomaly_flag"] = trueish_column(
        merged,
        "monthly_revenue_numerical_anomaly_flag",
    )
    merged["monthly_revenue_formal_model_use_allowed"] = trueish_column(
        merged,
        "monthly_revenue_formal_model_use_allowed",
    )
    return merged


FULL_MONTHLY_REVENUE_CONTEXT_COLUMNS = [
    "full_monthly_revenue_context_ready",
    "full_monthly_revenue_data_status",
    "full_monthly_revenue_period",
    "full_monthly_revenue_source_table_date",
    "full_monthly_revenue_latest_yoy_pct",
    "full_monthly_revenue_cumulative_yoy_pct",
    "full_monthly_revenue_month_over_month_pct",
    "full_monthly_revenue_prev1_period",
    "full_monthly_revenue_prev2_period",
    "full_monthly_revenue_prev3_period",
    "full_monthly_revenue_prev1_latest_yoy_pct",
    "full_monthly_revenue_prev2_latest_yoy_pct",
    "full_monthly_revenue_prev3_latest_yoy_pct",
    "full_monthly_revenue_prev1_cumulative_yoy_pct",
    "full_monthly_revenue_prev2_cumulative_yoy_pct",
    "full_monthly_revenue_prev3_cumulative_yoy_pct",
    "full_monthly_revenue_latest_yoy_delta_1m_pct_points",
    "full_monthly_revenue_cumulative_yoy_delta_1m_pct_points",
    "full_monthly_revenue_positive_flag",
    "full_monthly_revenue_strong_flag",
    "full_monthly_revenue_positive_or_strong",
    "full_monthly_revenue_numerical_anomaly_flag",
    "full_monthly_revenue_numerical_anomaly_reason",
    "full_monthly_revenue_research_join_allowed",
    "full_monthly_revenue_formal_model_use_allowed",
    "full_monthly_revenue_source_kind",
    "full_monthly_revenue_source_artifact",
]


def _with_empty_full_monthly_revenue_context(df: pd.DataFrame, status: str) -> pd.DataFrame:
    out = df.copy()
    for col in FULL_MONTHLY_REVENUE_CONTEXT_COLUMNS:
        if col not in out.columns:
            out[col] = ""
    out["full_monthly_revenue_context_ready"] = False
    out["full_monthly_revenue_data_status"] = status
    out["full_monthly_revenue_positive_flag"] = False
    out["full_monthly_revenue_strong_flag"] = False
    out["full_monthly_revenue_positive_or_strong"] = False
    out["full_monthly_revenue_numerical_anomaly_flag"] = False
    out["full_monthly_revenue_research_join_allowed"] = False
    out["full_monthly_revenue_formal_model_use_allowed"] = False
    return out


def attach_full_monthly_revenue_history_features(
    df: pd.DataFrame,
    history_path: Path = FULL_MONTHLY_REVENUE_HISTORY_CSV,
) -> pd.DataFrame:
    """Attach canonical full-market monthly revenue rows as of each signal date."""
    if df.empty:
        return _with_empty_full_monthly_revenue_context(df, "empty_research_frame")
    if not history_path.exists():
        return _with_empty_full_monthly_revenue_context(df, "missing_full_monthly_revenue_history")

    history = pd.read_csv(history_path, dtype=str, keep_default_na=False)
    required = {"stock_id", "source_table_date", "revenue_period"}
    if history.empty or not required.issubset(history.columns):
        return _with_empty_full_monthly_revenue_context(df, "invalid_full_monthly_revenue_history")

    history = history.copy()
    history["stock_id"] = history["stock_id"].map(normalize_code)
    history["source_table_date"] = history["source_table_date"].map(normalize_date)
    history = history[history["stock_id"].ne("") & history["source_table_date"].ne("")]
    if history.empty:
        return _with_empty_full_monthly_revenue_context(df, "invalid_full_monthly_revenue_history")

    keep_cols = [
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
    ]
    for col in keep_cols:
        if col not in history.columns:
            history[col] = ""
    history = history[keep_cols].copy()
    history["_full_monthly_revenue_source_dt"] = pd.to_datetime(
        history["source_table_date"],
        format="%Y%m%d",
        errors="coerce",
    )
    history = history.dropna(subset=["_full_monthly_revenue_source_dt"])
    history = history.sort_values(["stock_id", "_full_monthly_revenue_source_dt", "revenue_period"])
    grouped_history = history.groupby("stock_id", sort=False, dropna=False)
    for lag in (1, 2, 3):
        history[f"prev{lag}_revenue_period"] = grouped_history["revenue_period"].shift(lag)
        history[f"prev{lag}_latest_revenue_yoy_pct"] = grouped_history["latest_revenue_yoy_pct"].shift(lag)
        history[f"prev{lag}_cumulative_revenue_yoy_pct"] = grouped_history["cumulative_revenue_yoy_pct"].shift(lag)

    left = df.copy()
    left["_full_monthly_revenue_original_index"] = range(len(left))
    left["stock_id"] = left["stock_id"].map(normalize_code) if "stock_id" in left.columns else ""
    left["date"] = left["date"].map(normalize_date) if "date" in left.columns else ""
    left["_full_monthly_revenue_signal_dt"] = pd.to_datetime(left["date"], format="%Y%m%d", errors="coerce")

    merged_parts: list[pd.DataFrame] = []
    history_by_stock = {
        stock_id: part.reset_index(drop=True)
        for stock_id, part in history.groupby("stock_id", sort=False, dropna=False)
    }
    for stock_id, price_part in left.groupby("stock_id", sort=False, dropna=False):
        stock_key = safe_str(stock_id)
        hist_part = history_by_stock.get(stock_key)
        if not stock_key or hist_part is None or hist_part.empty:
            p = _with_empty_full_monthly_revenue_context(
                price_part,
                "missing_stock_in_full_monthly_revenue_history",
            )
            merged_parts.append(p)
            continue
        merged = pd.merge_asof(
            price_part.sort_values("_full_monthly_revenue_signal_dt"),
            hist_part.drop(columns=["stock_id"]).sort_values("_full_monthly_revenue_source_dt"),
            left_on="_full_monthly_revenue_signal_dt",
            right_on="_full_monthly_revenue_source_dt",
            direction="backward",
        )
        merged_parts.append(merged)

    merged_all = pd.concat(merged_parts, ignore_index=True, sort=False)
    has_match = merged_all["source_table_date"].fillna("").astype(str).ne("")
    prior_status = (
        merged_all["full_monthly_revenue_data_status"].fillna("")
        if "full_monthly_revenue_data_status" in merged_all.columns
        else pd.Series("", index=merged_all.index, dtype=object)
    )
    merged_all["full_monthly_revenue_data_status"] = np.where(
        has_match,
        "ready_asof_history_row",
        np.where(prior_status.astype(str).ne(""), prior_status, "missing_asof_revenue_on_or_before_signal_date"),
    )
    def _merged_text_column(name: str) -> pd.Series:
        if name not in merged_all.columns:
            return pd.Series("", index=merged_all.index, dtype=object)
        return merged_all[name].fillna("")

    merged_all["full_monthly_revenue_period"] = _merged_text_column("revenue_period")
    merged_all["full_monthly_revenue_source_table_date"] = _merged_text_column("source_table_date")
    merged_all["full_monthly_revenue_latest_yoy_pct"] = pd.to_numeric(
        merged_all.get("latest_revenue_yoy_pct", pd.Series(math.nan, index=merged_all.index)),
        errors="coerce",
    )
    merged_all["full_monthly_revenue_cumulative_yoy_pct"] = pd.to_numeric(
        merged_all.get("cumulative_revenue_yoy_pct", pd.Series(math.nan, index=merged_all.index)),
        errors="coerce",
    )
    merged_all["full_monthly_revenue_month_over_month_pct"] = pd.to_numeric(
        merged_all.get("month_over_month_pct", pd.Series(math.nan, index=merged_all.index)),
        errors="coerce",
    )
    for lag in (1, 2, 3):
        merged_all[f"full_monthly_revenue_prev{lag}_period"] = _merged_text_column(f"prev{lag}_revenue_period")
        merged_all[f"full_monthly_revenue_prev{lag}_latest_yoy_pct"] = pd.to_numeric(
            merged_all.get(f"prev{lag}_latest_revenue_yoy_pct", pd.Series(math.nan, index=merged_all.index)),
            errors="coerce",
        )
        merged_all[f"full_monthly_revenue_prev{lag}_cumulative_yoy_pct"] = pd.to_numeric(
            merged_all.get(f"prev{lag}_cumulative_revenue_yoy_pct", pd.Series(math.nan, index=merged_all.index)),
            errors="coerce",
        )
    research_allowed = trueish(merged_all.get("research_join_allowed", pd.Series(False, index=merged_all.index)))
    formal_allowed = trueish(
        merged_all.get("allowed_for_formal_historical_model_use", pd.Series(False, index=merged_all.index))
    )
    latest = merged_all["full_monthly_revenue_latest_yoy_pct"]
    cumulative = merged_all["full_monthly_revenue_cumulative_yoy_pct"]
    merged_all["full_monthly_revenue_latest_yoy_delta_1m_pct_points"] = (
        latest - merged_all["full_monthly_revenue_prev1_latest_yoy_pct"]
    )
    merged_all["full_monthly_revenue_cumulative_yoy_delta_1m_pct_points"] = (
        cumulative - merged_all["full_monthly_revenue_prev1_cumulative_yoy_pct"]
    )
    context_ready = has_match & research_allowed
    merged_all["full_monthly_revenue_context_ready"] = context_ready
    merged_all["full_monthly_revenue_positive_flag"] = context_ready & ((latest > 0) | (cumulative > 0))
    merged_all["full_monthly_revenue_strong_flag"] = context_ready & ((latest >= 30) | (cumulative >= 20))
    merged_all["full_monthly_revenue_positive_or_strong"] = (
        merged_all["full_monthly_revenue_positive_flag"] | merged_all["full_monthly_revenue_strong_flag"]
    )
    merged_all["full_monthly_revenue_numerical_anomaly_flag"] = (
        context_ready
        & trueish(merged_all.get("revenue_numerical_anomaly_flag", pd.Series(False, index=merged_all.index)))
    )
    merged_all["full_monthly_revenue_numerical_anomaly_reason"] = _merged_text_column(
        "revenue_numerical_anomaly_reason"
    )
    merged_all["full_monthly_revenue_research_join_allowed"] = research_allowed
    merged_all["full_monthly_revenue_formal_model_use_allowed"] = formal_allowed
    merged_all["full_monthly_revenue_source_kind"] = _merged_text_column("source_kind")
    merged_all["full_monthly_revenue_source_artifact"] = history_path.as_posix()

    drop_cols = [
        "_full_monthly_revenue_signal_dt",
        "_full_monthly_revenue_source_dt",
        "source_table_date",
        "revenue_period",
        "source_kind",
        "latest_revenue_yoy_pct",
        "cumulative_revenue_yoy_pct",
        "month_over_month_pct",
        "prev1_revenue_period",
        "prev2_revenue_period",
        "prev3_revenue_period",
        "prev1_latest_revenue_yoy_pct",
        "prev2_latest_revenue_yoy_pct",
        "prev3_latest_revenue_yoy_pct",
        "prev1_cumulative_revenue_yoy_pct",
        "prev2_cumulative_revenue_yoy_pct",
        "prev3_cumulative_revenue_yoy_pct",
        "revenue_numerical_anomaly_flag",
        "revenue_numerical_anomaly_reason",
        "research_join_allowed",
        "allowed_for_formal_historical_model_use",
    ]
    out = (
        merged_all.sort_values("_full_monthly_revenue_original_index", kind="mergesort")
        .drop(columns=[col for col in drop_cols if col in merged_all.columns])
        .drop(columns=["_full_monthly_revenue_original_index"])
        .reset_index(drop=True)
    )
    return out


def build_research_frame() -> pd.DataFrame:
    df = build_stock_day_frame()
    if df.empty:
        return df
    df = add_technical_features(df)
    df = add_price_structure_features(df)
    df = attach_theme_labels(df)
    df = attach_tdcc_features(df)
    df = attach_signal_background_features(df)
    df = attach_full_monthly_revenue_history_features(df)
    return df


def support_retest_mask(d: pd.DataFrame, low_col: str = "range_low_20d_prev") -> pd.Series:
    return (
        (d[low_col] > 0)
        & (d["close"] >= d[low_col] * 0.98)
        & (d["close"] <= d[low_col] * 1.08)
    )


def price_pullback_near_ema23_or_support(d: pd.DataFrame) -> pd.Series:
    distance = numeric_column(d, "distance_ema23_pct")
    near_ema23 = between(distance, -2.5, 5.0)
    support_cols = ["platform_low", "short_platform_low", "previous_20d_low", "low_20", "range_low_20d_prev"]
    support = bool_series(d)
    close = numeric_column(d, "close")
    for col in support_cols:
        low = numeric_column(d, col)
        support = support | ((low > 0) & (close >= low * 0.98) & (close <= low * 1.08))
    return (near_ema23 | support).fillna(False)


def price_pullback_ema23_slope_proxy_up(d: pd.DataFrame) -> pd.Series:
    close = numeric_column(d, "close")
    ema23 = numeric_column(d, "ema23")
    ma20 = numeric_column(d, "ma20")
    slope = numeric_column(d, "ema23_slope_pct")
    if slope.isna().all():
        slope = numeric_column(d, "ema23_slope_5d_pct")
    return (
        trueish_column(d, "ma5_turning_up_flag")
        | trueish_column(d, "ma10_turning_up_flag")
        | (slope > 0)
        | ((close > 0) & (ema23 > 0) & (close >= ema23))
        | ((ema23 > 0) & (ma20 > 0) & (ema23 >= ma20 * 0.98))
    ).fillna(False)


def current_volume_range_breakout_baseline(d: pd.DataFrame) -> pd.Series:
    normal_volume = (
        (d["volume_ratio_prev20"] >= 2.0)
        & (d["range_breakout_20d_pct"] >= 2.0)
        & (d["volume_ma20_lots"] >= 1000)
        & d["bullish_attack_candle"]
    )
    return normal_volume | d["locked_limit_up_breakout"]


def volume_v2_base_breakout(d: pd.DataFrame) -> pd.Series:
    return (
        (numeric_column(d, "volume_ratio_prev20") >= 2.0)
        & (numeric_column(d, "range_breakout_60d_pct") >= 0.0)
        & (numeric_column(d, "volume_ma20_lots") >= 1000)
        & trueish_column(d, "bullish_attack_candle")
    ).fillna(False)


def volume_v2_shape_bucket(d: pd.DataFrame) -> pd.Series:
    width60 = numeric_column(d, "range_width_60d_pct")
    out = pd.Series("non_consolidation", index=d.index, dtype=object)
    out = out.mask(width60 <= 40.0, "consolidation")
    out = out.mask(width60 > 80.0, "wide_range")
    return out


def current_volume_v2_low_position_baseline(d: pd.DataFrame) -> pd.Series:
    position120 = numeric_column(d, "close_position_120d_pct")
    return (volume_v2_base_breakout(d) & position120.le(40.0)).fillna(False)


def current_volume_v2_mid_position_baseline(d: pd.DataFrame) -> pd.Series:
    position120 = numeric_column(d, "close_position_120d_pct")
    shape = volume_v2_shape_bucket(d)
    return (
        volume_v2_base_breakout(d)
        & position120.gt(40.0)
        & position120.le(75.0)
        & shape.isin({"non_consolidation", "wide_range"})
    ).fillna(False)


def current_volume_v2_high_position_baseline(d: pd.DataFrame) -> pd.Series:
    position120 = numeric_column(d, "close_position_120d_pct")
    shape = volume_v2_shape_bucket(d)
    ma60 = numeric_column(d, "ma60")
    ma120 = numeric_column(d, "ma120")
    return (
        volume_v2_base_breakout(d)
        & position120.gt(75.0)
        & shape.isin({"non_consolidation", "wide_range"})
        & ma60.gt(ma120)
    ).fillna(False)


def current_price_pullback_baseline_proxy(d: pd.DataFrame) -> pd.Series:
    return price_pullback_near_ema23_or_support(d) & price_pullback_ema23_slope_proxy_up(d)


def current_price_pullback_approved_operation_baseline(d: pd.DataFrame) -> pd.Series:
    return (
        current_price_pullback_baseline_proxy(d)
        & price_pullback_return20_balanced_filter(d)
        & price_pullback_tdcc_high_thresholds_up_filter(d)
        & price_pullback_obv_above_ma20_filter(d)
    )


def price_pullback_red_k_entry_filter(d: pd.DataFrame, volume_min: float, solid: bool = False) -> pd.Series:
    candle_col = "solid_red_candle" if solid else "bullish_attack_candle"
    return (numeric_column(d, "volume_ratio_prev20") >= volume_min) & trueish_column(d, candle_col)


def price_pullback_prior_extension_filter(
    d: pd.DataFrame,
    window: int,
    min_extension_pct: float,
    min_runup_pct: float,
    min_pullback_from_high_pct: float,
) -> pd.Series:
    return (
        (numeric_column(d, f"prior_extension_ema23_{window}d_pct") >= min_extension_pct)
        & (numeric_column(d, f"prior_runup_{window}d_pct") >= min_runup_pct)
        & (numeric_column(d, f"pullback_from_high_{window}d_pct") <= -min_pullback_from_high_pct)
    ).fillna(False)


def price_pullback_45d_bullish_pullback_filter(d: pd.DataFrame) -> pd.Series:
    return (
        (numeric_column(d, "return_45d_pct") >= 8.0)
        & (numeric_column(d, "range_width_45d_pct") >= 18.0)
        & between(numeric_column(d, "close_position_45d_pct"), 35.0, 80.0)
    ).fillna(False)


def price_pullback_return20_balanced_filter(d: pd.DataFrame) -> pd.Series:
    return between(numeric_column(d, "return_20d_pct"), 0.0, 25.0).fillna(False)


def price_pullback_tdcc_high_thresholds_up_filter(d: pd.DataFrame) -> pd.Series:
    return (trueish_column(d, "tdcc_history_available") & trueish_column(d, "high_thresholds_up")).fillna(False)


def price_pullback_tdcc_consecutive_up_ge1_filter(d: pd.DataFrame) -> pd.Series:
    return (
        trueish_column(d, "tdcc_history_available")
        & (numeric_column(d, "tdcc_consecutive_up_weeks") >= 1.0)
    ).fillna(False)


def price_pullback_macd_kd_confirm_filter(d: pd.DataFrame) -> pd.Series:
    return (trueish_column(d, "macd_hist_gt0") & trueish_column(d, "kd_bullish_not_overheated")).fillna(False)


def price_pullback_obv_above_ma20_filter(d: pd.DataFrame) -> pd.Series:
    return trueish_column(d, "obv_above_ma20").fillna(False)


def price_pullback_theme_context_ready_filter(d: pd.DataFrame) -> pd.Series:
    return trueish_column(d, "theme_context_ready").fillna(False)


def price_pullback_theme_context_mainstream_filter(d: pd.DataFrame) -> pd.Series:
    return trueish_column(d, "theme_context_mainstream_supported").fillna(False)


def price_pullback_theme_context_leadership_not_overheated_filter(d: pd.DataFrame) -> pd.Series:
    return (
        trueish_column(d, "theme_context_leadership_supported")
        & ~trueish_column(d, "theme_context_overheated")
    ).fillna(False)


def price_pullback_theme_context_volume_attack_selected_filter(d: pd.DataFrame) -> pd.Series:
    return trueish_column(d, "theme_context_volume_attack_selected_flag").fillna(False)


def price_pullback_monthly_revenue_context_ready_filter(d: pd.DataFrame) -> pd.Series:
    return trueish_column(d, "monthly_revenue_context_ready").fillna(False)


def price_pullback_monthly_revenue_positive_or_strong_filter(d: pd.DataFrame) -> pd.Series:
    return (
        price_pullback_monthly_revenue_context_ready_filter(d)
        & trueish_column(d, "monthly_revenue_positive_or_strong")
        & ~trueish_column(d, "monthly_revenue_formal_model_use_allowed")
    ).fillna(False)


def full_monthly_revenue_context_ready_filter(d: pd.DataFrame) -> pd.Series:
    return trueish_column(d, "full_monthly_revenue_context_ready").fillna(False)


def full_monthly_revenue_positive_filter(d: pd.DataFrame) -> pd.Series:
    return (
        full_monthly_revenue_context_ready_filter(d)
        & trueish_column(d, "full_monthly_revenue_positive_flag")
    ).fillna(False)


def full_monthly_revenue_strong_filter(d: pd.DataFrame) -> pd.Series:
    return (
        full_monthly_revenue_context_ready_filter(d)
        & trueish_column(d, "full_monthly_revenue_strong_flag")
    ).fillna(False)


def full_monthly_revenue_latest_yoy_ge_filter(d: pd.DataFrame, threshold: float) -> pd.Series:
    return (
        full_monthly_revenue_context_ready_filter(d)
        & numeric_column(d, "full_monthly_revenue_latest_yoy_pct").ge(threshold)
    ).fillna(False)


def full_monthly_revenue_cumulative_yoy_ge_filter(d: pd.DataFrame, threshold: float) -> pd.Series:
    return (
        full_monthly_revenue_context_ready_filter(d)
        & numeric_column(d, "full_monthly_revenue_cumulative_yoy_pct").ge(threshold)
    ).fillna(False)


def full_monthly_revenue_both_latest30_cumulative20_filter(d: pd.DataFrame) -> pd.Series:
    return (
        full_monthly_revenue_context_ready_filter(d)
        & numeric_column(d, "full_monthly_revenue_latest_yoy_pct").ge(30.0)
        & numeric_column(d, "full_monthly_revenue_cumulative_yoy_pct").ge(20.0)
    ).fillna(False)


def full_monthly_revenue_negative_both_filter(d: pd.DataFrame) -> pd.Series:
    return (
        full_monthly_revenue_context_ready_filter(d)
        & numeric_column(d, "full_monthly_revenue_latest_yoy_pct").lt(0.0)
        & numeric_column(d, "full_monthly_revenue_cumulative_yoy_pct").lt(0.0)
    ).fillna(False)


def full_monthly_revenue_latest_yoy_improving_2m_filter(d: pd.DataFrame) -> pd.Series:
    latest = numeric_column(d, "full_monthly_revenue_latest_yoy_pct")
    prev1 = numeric_column(d, "full_monthly_revenue_prev1_latest_yoy_pct")
    prev2 = numeric_column(d, "full_monthly_revenue_prev2_latest_yoy_pct")
    return (full_monthly_revenue_context_ready_filter(d) & latest.gt(prev1) & prev1.gt(prev2)).fillna(False)


def full_monthly_revenue_latest_yoy_improving_3m_filter(d: pd.DataFrame) -> pd.Series:
    latest = numeric_column(d, "full_monthly_revenue_latest_yoy_pct")
    prev1 = numeric_column(d, "full_monthly_revenue_prev1_latest_yoy_pct")
    prev2 = numeric_column(d, "full_monthly_revenue_prev2_latest_yoy_pct")
    prev3 = numeric_column(d, "full_monthly_revenue_prev3_latest_yoy_pct")
    return (
        full_monthly_revenue_context_ready_filter(d)
        & latest.gt(prev1)
        & prev1.gt(prev2)
        & prev2.gt(prev3)
    ).fillna(False)


def full_monthly_revenue_cumulative_yoy_improving_2m_filter(d: pd.DataFrame) -> pd.Series:
    cumulative = numeric_column(d, "full_monthly_revenue_cumulative_yoy_pct")
    prev1 = numeric_column(d, "full_monthly_revenue_prev1_cumulative_yoy_pct")
    prev2 = numeric_column(d, "full_monthly_revenue_prev2_cumulative_yoy_pct")
    return (full_monthly_revenue_context_ready_filter(d) & cumulative.gt(prev1) & prev1.gt(prev2)).fillna(False)


def full_monthly_revenue_latest_yoy_turn_positive_filter(d: pd.DataFrame) -> pd.Series:
    return (
        full_monthly_revenue_context_ready_filter(d)
        & numeric_column(d, "full_monthly_revenue_latest_yoy_pct").gt(0.0)
        & numeric_column(d, "full_monthly_revenue_prev1_latest_yoy_pct").lt(0.0)
    ).fillna(False)


def full_monthly_revenue_latest_yoy_turn_positive_after_2_negative_filter(d: pd.DataFrame) -> pd.Series:
    return (
        full_monthly_revenue_latest_yoy_turn_positive_filter(d)
        & numeric_column(d, "full_monthly_revenue_prev2_latest_yoy_pct").lt(0.0)
    ).fillna(False)


def full_monthly_revenue_cumulative_yoy_turn_positive_filter(d: pd.DataFrame) -> pd.Series:
    return (
        full_monthly_revenue_context_ready_filter(d)
        & numeric_column(d, "full_monthly_revenue_cumulative_yoy_pct").gt(0.0)
        & numeric_column(d, "full_monthly_revenue_prev1_cumulative_yoy_pct").lt(0.0)
    ).fillna(False)


def full_monthly_revenue_latest_yoy_delta_ge_filter(d: pd.DataFrame, threshold: float) -> pd.Series:
    return (
        full_monthly_revenue_context_ready_filter(d)
        & numeric_column(d, "full_monthly_revenue_latest_yoy_delta_1m_pct_points").ge(threshold)
    ).fillna(False)


def full_monthly_revenue_turn_positive_and_cumulative_improving_filter(d: pd.DataFrame) -> pd.Series:
    return (
        full_monthly_revenue_latest_yoy_turn_positive_filter(d)
        & numeric_column(d, "full_monthly_revenue_cumulative_yoy_pct").gt(
            numeric_column(d, "full_monthly_revenue_prev1_cumulative_yoy_pct")
        )
    ).fillna(False)


def full_monthly_revenue_latest_improving_and_cumulative_improving_filter(d: pd.DataFrame) -> pd.Series:
    return (
        full_monthly_revenue_latest_yoy_improving_2m_filter(d)
        & numeric_column(d, "full_monthly_revenue_cumulative_yoy_pct").gt(
            numeric_column(d, "full_monthly_revenue_prev1_cumulative_yoy_pct")
        )
    ).fillna(False)


def price_pullback_volume_red_k_entry(d: pd.DataFrame, volume_min: float, solid: bool = False) -> pd.Series:
    return current_price_pullback_baseline_proxy(d) & price_pullback_red_k_entry_filter(d, volume_min, solid)


def current_hot_theme_pullback_baseline_proxy(d: pd.DataFrame) -> pd.Series:
    return (
        d["strict_theme_status_group"].isin({"mainstream_supported", "mainstream_overheated"})
        & (between(d["distance_ema23_pct"], -2.5, 5.0) | support_retest_mask(d))
    )


def active_price_attack_proxy(d: pd.DataFrame) -> pd.Series:
    return (
        current_volume_range_breakout_baseline(d)
        | (d["volume_ratio_prev20"] >= 2.5)
        | (d["return_5d_pct"] >= 8)
        | (d["return_20d_pct"] >= 20)
    ).fillna(False)


def current_revenue_unreacted_baseline_proxy(d: pd.DataFrame) -> pd.Series:
    # This intentionally mirrors only the price-range and not-started portions.
    # Full-market revenue conditions are tested in the model-specific revenue
    # condition matrix and still require an explicit promotion PR before
    # becoming a formal production gate.
    return (
        (d["close"] >= d["range_low_23d_prev"] * 0.95)
        & (d["close"] <= d["range_high_23d_prev"] * 1.05)
        & (~active_price_attack_proxy(d))
    )


def current_w_bottom_baseline_proxy(d: pd.DataFrame) -> pd.Series:
    return d["w_bottom_proxy"] & (d["range_breakout_20d_pct"] < 2.0)


def current_w_bottom_approved_operation_baseline(d: pd.DataFrame) -> pd.Series:
    """Anchor W-bottom parity to the approved operation artifact.

    The production detector itself is row/context based and too expensive for
    the generic parameter-grid builder. The formal daily operation contract is
    the approved operation artifact, while raw candidate rows remain
    research-only.
    """
    return current_w_bottom_baseline_proxy(d)


def current_neckline_volume_breakout_baseline_proxy(d: pd.DataFrame) -> pd.Series:
    return (
        d["w_bottom_proxy"]
        & (
            ((d["range_breakout_20d_pct"] >= 0.0) & (d["volume_ratio_prev20"] >= 2.0) & d["bullish_attack_candle"])
            | d["locked_limit_up_breakout"]
        )
    )


def current_neckline_approved_operation_baseline(d: pd.DataFrame) -> pd.Series:
    """Anchor neckline parity to the approved operation v1 artifact.

    The formal daily operation contract is the approved operation artifact.
    Raw research rows remain advisory-only; production scoring/entry rules are
    synchronized through the operation module and contract metadata.
    """
    return current_neckline_volume_breakout_baseline_proxy(d)


def current_near_high_baseline_proxy(d: pd.DataFrame) -> pd.Series:
    return (
        between(d["near_60d_high_pct"], -5.0, 0.0)
        & (d["volume_ratio_prev20"] >= 1.2)
        & (d["ema23_slope_5d_pct"] > 0)
        & (d["range_breakout_20d_pct"] < 2.0)
    )


def current_platform_strengthening_baseline_proxy(d: pd.DataFrame) -> pd.Series:
    return (
        (d["range_width_20d_pct"] <= 18)
        & between(d["distance_to_range_high_20d_pct"], -5.0, 1.5)
        & (d["volume_ratio_prev20"] >= 1.2)
        & d["solid_red_candle"]
        & (d["range_breakout_20d_pct"] < 2.0)
    )


def current_pullback_short_reclaim_baseline_proxy(d: pd.DataFrame) -> pd.Series:
    return (
        (d["return_20d_pct"] >= 5)
        & (between(d["distance_ema23_pct"], -1.0, 6.0) | (d["close_above_ma20"] & (d["ema23_slope_5d_pct"] > 0)))
        & (d["ema23_slope_5d_pct"] > 0)
    )


def current_tdcc_stealth_baseline_proxy(d: pd.DataFrame) -> pd.Series:
    return (
        trueish(d["tdcc_history_available"])
        & (
            (d["tdcc_consecutive_up_weeks"] >= 1)
            | trueish(d["all_thresholds_up"])
            | trueish(d["high_thresholds_up"])
        )
        & (d["volume_ratio_prev20"] < 2.5)
        & (d["return_5d_pct"] < 8)
        & (d["return_20d_pct"] < 20)
        & (d["close"] >= d["range_low_23d_prev"] * 0.90)
        & (d["close"] <= d["range_high_23d_prev"] * 1.10)
        & (~current_volume_range_breakout_baseline(d))
    )


def current_tdcc_short_term_continuation_baseline_proxy(d: pd.DataFrame) -> pd.Series:
    return (
        trueish(d["tdcc_history_available"])
        & (
            trueish(d["all_thresholds_up"])
            | trueish(d["high_thresholds_up"])
            | trueish(d["four_thresholds_sync_up"])
        )
        & between(d["return_5d_pct"], 10, 30)
        & (trueish(d["macd_hist_gt0"]) | trueish(d["kd_bullish_not_overheated"]))
    )


def production_baseline_specs() -> list[RuleSpec]:
    return [
        RuleSpec(
            "volume_range_breakout",
            "放量攻擊模型",
            "production_current",
            "production baseline: normal prior-20d breakout OR locked-limit-up breakout bypass",
            "pdf_core_model",
            current_volume_range_breakout_baseline,
            "Matches current production logic available in historical price fields, including locked-limit-up bypass without a volume-ratio gate.",
            "production_baseline",
            "production_parity",
            "",
            "production_current",
        ),
        RuleSpec(
            "price_pullback_23ema",
            "23EMA回檔模型",
            PRICE_PULLBACK_OPERATION_MODULE_ID,
            "approved operation baseline: 23EMA/support pullback, return20_0_25, TDCC high thresholds up, OBV above MA20",
            "pdf_core_model",
            current_price_pullback_approved_operation_baseline,
            (
                f"{PRICE_PULLBACK_OPERATION_MODULE_ID} is the formal daily baseline through "
                "approved_operation_patterns_latest.csv and the model-owned operation adapter."
            ),
            "production_baseline",
            "production_parity",
            "",
            "production_current",
        ),
        RuleSpec(
            "hot_theme_pullback",
            "熱門族群回檔模型",
            "production_current_proxy",
            "production baseline proxy: no-lookahead mainstream theme + pullback near 23EMA/support",
            "pdf_core_model",
            current_hot_theme_pullback_baseline_proxy,
            "Production uses current model-layer hot theme labels; research uses strict historical no-lookahead theme state.",
            "production_baseline",
            "production_proxy",
            "daily hot-theme labels are not fully backfilled as point-in-time model-layer fields",
            "production_current",
        ),
        RuleSpec(
            "revenue_unreacted_range",
            "營收爆發但股價尚未反應模型",
            "production_current_proxy",
            "production baseline proxy: price still in 23d range and attack not started; revenue gate tested separately",
            "pdf_core_model",
            current_revenue_unreacted_baseline_proxy,
            "Canonical monthly revenue history exists for research joins, but formal revenue gate parity still requires model-specific promotion.",
            "production_baseline",
            "proxy_only",
            "strong_revenue gate requires model-specific research matrix, contract update, exact parity, and promotion PR before formal use",
            "production_current",
        ),
        RuleSpec(
            "w_bottom_right_side",
            "W底右側模型",
            W_BOTTOM_OPERATION_MODULE_ID,
            "approved operation baseline: right-low early entry, W-structure-low stop, D+20 gain10 else D+40 close exit",
            "pdf_core_model",
            current_w_bottom_approved_operation_baseline,
            (
                f"{W_BOTTOM_OPERATION_MODULE_ID} is the formal daily baseline through "
                "approved_operation_patterns_latest.csv; raw research candidate rows remain advisory-only."
            ),
            "production_baseline",
            "production_parity",
            "",
            "production_current",
        ),
        RuleSpec(
            "neckline_volume_breakout_confirmation",
            "W底頸線帶量突破確認模型",
            NECKLINE_OPERATION_MODULE_ID,
            "approved operation baseline: W-bottom neckline signal, 45d non-bearish context, 90d score-only context, next-open entry and 20d operation-rule outcome",
            "pdf_core_model",
            current_neckline_approved_operation_baseline,
            (
                "W-bottom neckline volume breakout operation v1 is the formal daily baseline through "
                "approved_operation_patterns_latest.csv; other neckline subtypes remain outside this model."
            ),
            "production_baseline",
            "production_parity",
            "",
            "production_current",
        ),
        RuleSpec(
            "pullback_short_reclaim",
            "回檔後短線轉強模型",
            "production_current_proxy",
            "production baseline proxy: 20d return >= 5%, pullback/reclaim proxy, EMA23 up",
            "pdf_core_model",
            current_pullback_short_reclaim_baseline_proxy,
            "Production uses pullback/right-side/reclaim flags; research approximates with EMA and MA20 reclaim context.",
            "production_baseline",
            "production_proxy",
            "pullback_entry_zone/right_side/ma20_reclaim setup flags are not fully backfilled",
            "production_current",
        ),
        RuleSpec(
            "tdcc_stealth_accumulation",
            "TDCC潛伏吸籌模型",
            "production_current_proxy",
            "production baseline proxy: TDCC positive, attack not started, low volume/return, still in range",
            "pdf_core_model",
            current_tdcc_stealth_baseline_proxy,
            "Production uses TDCC phase when available; research uses weekly TDCC history and range constraints.",
            "production_baseline",
            "production_proxy",
            "tdcc_price_phase is not fully available historically for every signal date",
            "production_current",
        ),
        RuleSpec(
            "tdcc_short_term_continuation_d5_d10",
            "TDCC短線延續模型 D+5/D+10",
            "production_current_proxy",
            "production baseline proxy: TDCC sync/high thresholds + 5d momentum + MACD/KD",
            "pdf_core_model",
            current_tdcc_short_term_continuation_baseline_proxy,
            "This mirrors the daily specialty short-term continuation surface enough to serve as baseline before deeper grid variants.",
            "production_baseline",
            "production_proxy",
            "daily specialty packet fields are not a single core build_specs condition and must be replayed from historical TDCC/technical proxies",
            "production_current",
        ),
    ]


_legacy_production_baseline_specs = production_baseline_specs


def production_baseline_specs() -> list[RuleSpec]:
    specs = [spec for spec in _legacy_production_baseline_specs() if spec.model_id != "volume_range_breakout"]
    v2_specs = [
        RuleSpec(
            "volume_range_breakout_v2_low_position_volume_attack",
            "低位放量攻擊",
            "volume_range_breakout_v2_low_position_operation_v1",
            "formal v2 baseline: 120d low-position bucket with all shape buckets, 60d breakout and close-only next-day continuation handled by operation adapter",
            "pdf_core_model",
            current_volume_v2_low_position_baseline,
            "Formal operation evidence comes from volume_range_breakout_v2_candidate_bucket_contract and the model-owned operation adapter; TDCC and MA overlays are score-only.",
            "production_baseline",
            "production_parity",
            "",
            "production_current",
        ),
        RuleSpec(
            "volume_range_breakout_v2_mid_position_momentum_attack",
            "中位動能放量攻擊",
            "volume_range_breakout_v2_mid_position_operation_v1",
            "formal v2 baseline: 120d mid-position bucket with non-consolidation or wide-range shape, 60d breakout and close-only next-day continuation handled by operation adapter",
            "pdf_core_model",
            current_volume_v2_mid_position_baseline,
            "Formal operation evidence comes from volume_range_breakout_v2_candidate_bucket_contract and the model-owned operation adapter; TDCC and MA overlays are score-only.",
            "production_baseline",
            "production_parity",
            "",
            "production_current",
        ),
        RuleSpec(
            "volume_range_breakout_v2_high_position_volume_attack",
            "高位階放量攻擊",
            "volume_range_breakout_v2_high_position_operation_v1",
            "formal v2 baseline: 120d high-position bucket, non-consolidation or wide-range shape, MA60 > MA120, 60d breakout and close-only next-day continuation handled by operation adapter",
            "pdf_core_model",
            current_volume_v2_high_position_baseline,
            "Formal operation evidence comes from volume_range_breakout_v2_high_position_improvement_audit and the model-owned operation adapter; single add-score metrics and exact combos are row-level display metrics only.",
            "production_baseline",
            "production_parity",
            "",
            "production_current",
        ),
    ]
    return v2_specs + specs


def rule_specs() -> list[RuleSpec]:
    specs: list[RuleSpec] = production_baseline_specs()

    for breakout_pct in [1.0, 2.0, 3.0]:
        for vol in [2.0, 3.0, 5.0]:
            for min_lots in [500, 1000, 2000]:
                specs.append(
                    RuleSpec(
                        "volume_range_breakout",
                        "放量攻擊模型",
                        f"prior20x{1 + breakout_pct / 100:.2f}_vol{vol:g}_minvol{min_lots}",
                        f"收盤突破前20日高點 {breakout_pct:g}% + 量比 >= {vol:g} + 20日均量 >= {min_lots}張 + 實體紅K",
                        "pdf_core_model",
                        lambda d, breakout_pct=breakout_pct, vol=vol, min_lots=min_lots: (
                            (d["volume_ratio_prev20"] >= vol)
                            & (d["range_breakout_20d_pct"] >= breakout_pct)
                            & (d["volume_ma20_lots"] >= min_lots)
                            & d["bullish_attack_candle"]
                        ),
                        "主條件是前20日高點突破、量能放大、流動性與實體紅K。漲幅、過熱、均線與60日高點不作為此模型否決條件。",
                    )
                )
    specs.append(
        RuleSpec(
            "volume_range_breakout",
            "放量攻擊模型",
            "locked_limit_up_breakout_no_volume_gate",
            "鎖量漲停突破前20日高點 2% + 漲幅 >= 9% + 一價或極窄區間；不要求量比或20日均量",
            "pdf_core_model",
            lambda d: d["locked_limit_up_breakout"],
            "這是現行放量攻擊模型的鎖量漲停旁路；不是全面降低一般突破的量比門檻。",
        )
    )

    for low, high in [(-1.5, 3.0), (-2.5, 5.0), (-4.0, 7.0)]:
        for vol_max in [1.0, 1.2, 1.5]:
            specs.append(
                RuleSpec(
                    "price_pullback_23ema",
                    "股價回檔模型",
                    f"ema{low:g}_{high:g}_volmax{vol_max:g}",
                    f"距 23EMA {low:g}% 至 {high:g}% + 23EMA 向上 + 量比 <= {vol_max:g}",
                    "research_only_not_pdf_core",
                    lambda d, low=low, high=high, vol_max=vol_max: (
                        between(d["distance_ema23_pct"], low, high)
                        & (d["ema23_slope_5d_pct"] > 0)
                        & (d["volume_ratio_prev20"] <= vol_max)
                    ),
                    "回檔模型不要求突破；主軸是結構支撐與量縮回檔。",
                )
            )
    for filter_id, volume_min, solid, label in [
        ("volume_red_k_vol1.2", 1.2, False, "帶量紅K"),
        ("solid_volume_red_k_vol1.2", 1.2, True, "實體帶量紅K"),
        ("solid_volume_red_k_vol1.5", 1.5, True, "實體強量紅K"),
    ]:
        specs.append(
            RuleSpec(
                "price_pullback_23ema",
                "股價回檔模型",
                filter_id,
                f"production proxy replay + {label} + 量比 >= {volume_min:g}",
                "research_only_not_pdf_core",
                lambda d, volume_min=volume_min, solid=solid: price_pullback_volume_red_k_entry(
                    d,
                    volume_min,
                    solid,
                ),
                "研究買點濾網：回檔到23EMA/支撐後，用帶量紅K確認買盤承接；不要求突破，也不可寫回 production baseline。",
            )
        )

    hot_theme_groups = {
        "strict_mainstream_any": {"mainstream_supported", "mainstream_overheated"},
        "strict_mainstream_supported": {"mainstream_supported"},
        "strict_mainstream_overheated": {"mainstream_overheated"},
    }
    for group_id, groups in hot_theme_groups.items():
        for low, high, support_high in [(-2.5, 5.0, 8.0), (-4.0, 7.0, 10.0)]:
            specs.append(
                RuleSpec(
                    "hot_theme_pullback",
                    "熱門族群回檔模型",
                    f"{group_id}_ema{low:g}_{high:g}_support{support_high:g}",
                    f"歷史熱門/主流族群狀態 {group_id} + 距 23EMA {low:g}% 至 {high:g}% 或接近20日支撐 {support_high:g}% 內",
                    "pdf_core_model",
                    lambda d, groups=groups, low=low, high=high, support_high=support_high: (
                        d["strict_theme_status_group"].isin(groups)
                        & (
                            between(d["distance_ema23_pct"], low, high)
                            | (
                                (d["range_low_20d_prev"] > 0)
                                & (d["close"] >= d["range_low_20d_prev"] * 0.98)
                                & (d["close"] <= d["range_low_20d_prev"] * (1 + support_high / 100))
                            )
                        )
                    ),
                    "使用 strict no-lookahead 歷史族群狀態近似每日熱門族群標籤；營收不作為必要條件。",
                )
            )

    for tolerance in [5, 10]:
        specs.append(
            RuleSpec(
                "revenue_unreacted_range",
                "營收爆發但股價尚未反應模型",
                f"range23_tol{tolerance}",
                f"股價位於 23 日區間上下 {tolerance}% 內；營收確認由每日模型層欄位提供",
                "pdf_core_model",
                lambda d, tolerance=tolerance: (
                    (d["close"] >= d["range_low_23d_prev"] * (1 - tolerance / 100))
                    & (d["close"] <= d["range_high_23d_prev"] * (1 + tolerance / 100))
                    & (d["range_width_23d_pct"] <= 20)
                ),
                "歷史營收 feature panel 尚未完整，這裡先用價格未反應區間作第一版近似條件。",
            )
        )

    for vol in [1.0, 1.2, 1.5]:
        specs.append(
            RuleSpec(
                "w_bottom_right_side",
                "W底右側模型",
                f"wproxy_vol{vol:g}",
                f"W底近似條件 + 右側結構墊高 + 量比 >= {vol:g}",
                "pdf_core_model",
                lambda d, vol=vol: d["w_bottom_proxy"] & (d["volume_ratio_prev20"] >= vol),
                "W底右側研究近似條件；正式升級仍需要圖形品質確認。",
            )
        )

    for dist in [3, 5]:
        for vol in [1.2, 1.5]:
            specs.append(
                RuleSpec(
                    "near_high_neckline_challenge",
                    "接近前高 / 頸線挑戰模型",
                    f"near{dist}_vol{vol:g}",
                    f"距 60 日高點下方 {dist}% 內 + 量比 >= {vol:g} + 23EMA 向上",
                    "research_only_not_pdf_core",
                    lambda d, dist=dist, vol=vol: (
                        between(d["near_60d_high_pct"], -dist, 0)
                        & (d["volume_ratio_prev20"] >= vol)
                        & (d["ema23_slope_5d_pct"] > 0)
                    ),
                    "用來提前 1 到 5 個交易日觀察突破前壓力挑戰；不是嚴格突破模型。",
                )
            )

    for window in [20, 30]:
        for near in [3, 5]:
            for vol in [1.2, 1.5]:
                specs.append(
                    RuleSpec(
                        "platform_strengthening",
                        "平台整理轉強模型",
                        f"w{window}_near{near}_vol{vol:g}",
                        f"{window}日區間寬度 <= 18% + 距區間上緣 {near}% 內 + 量比 >= {vol:g} + 實體紅K",
                        "research_only_not_pdf_core",
                        lambda d, window=window, near=near, vol=vol: (
                            (d[f"range_width_{window}d_pct"] <= 18)
                            & between(d[f"distance_to_range_high_{window}d_pct"], -near, 1.5)
                            & (d["volume_ratio_prev20"] >= vol)
                            & d["solid_red_candle"]
                        ),
                        "平台模型尋找波動收斂後、接近上緣時量能回升的型態。",
                    )
                )

    for vol in [1.0, 1.2, 1.5]:
        specs.append(
            RuleSpec(
                "pullback_short_reclaim",
                "回檔後短線轉強模型",
                f"prior20up_reclaim_vol{vol:g}",
                f"前 20 日漲幅 >= 10% + 距 23EMA -1% 至 6% + MACD 柱狀體 > 0 + 量比 >= {vol:g}",
                "pdf_core_model",
                lambda d, vol=vol: (
                    (d["return_20d_pct"] >= 10)
                    & between(d["distance_ema23_pct"], -1, 6)
                    & trueish(d["macd_hist_gt0"])
                    & (d["volume_ratio_prev20"] >= vol)
                ),
                "尋找前段上漲後回檔未破結構、並重新恢復短線動能的股票。",
            )
        )

    for consecutive in [1, 2, 3]:
        specs.append(
            RuleSpec(
                "tdcc_stealth_accumulation",
                "TDCC潛伏吸籌模型",
                f"tdcc_up{consecutive}_range10",
                f"TDCC 連續增加週數 >= {consecutive} + 股價位於 23 日區間上下 10% 內 + 20 日漲幅 <= 20%",
                "pdf_core_model",
                lambda d, consecutive=consecutive: (
                    trueish(d["tdcc_history_available"])
                    & (d["tdcc_consecutive_up_weeks"] >= consecutive)
                    & (d["close"] >= d["range_low_23d_prev"] * 0.90)
                    & (d["close"] <= d["range_high_23d_prev"] * 1.10)
                    & (d["return_20d_pct"] <= 20)
                ),
                "目前使用本地 TDCC 歷史資料；完整歷史 phase panel 可用後再升級 phase 篩選。",
            )
        )

    specs.extend(
        [
            RuleSpec(
                "tdcc_short_term_continuation_d5_d10",
                "TDCC短線延續模型 D+5/D+10",
                "all_thresholds_up_ret5_10_30_macd",
                "四級距同步增加 + 5日漲幅 10% 至 30% + MACD 柱狀體 > 0",
                "pdf_core_model",
                lambda d: (
                    trueish(d["tdcc_history_available"])
                    & trueish(d["all_thresholds_up"])
                    & between(d["return_5d_pct"], 10, 30)
                    & trueish(d["macd_hist_gt0"])
                ),
                "短線延續專項，不是低位吸籌模型。",
            ),
            RuleSpec(
                "tdcc_short_term_continuation_d5_d10",
                "TDCC短線延續模型 D+5/D+10",
                "high_thresholds_ret5_10_30_ret10_20_50_kd",
                "高級距增加 + 5日漲幅 10% 至 30% + 10日漲幅 20% 至 50% + KD 多方但未過熱",
                "pdf_core_model",
                lambda d: (
                    trueish(d["tdcc_history_available"])
                    & trueish(d["high_thresholds_up"])
                    & between(d["return_5d_pct"], 10, 30)
                    & between(d["return_10d_pct"], 20, 50)
                    & trueish(d["kd_bullish_not_overheated"])
                ),
                "短線延續研究；報酬統計使用訊號日隔天開盤到 D+1 至 D+10。",
            ),
            RuleSpec(
                "short_term_surge_d5_d10",
                "短線急漲 D+5/D+10 研究",
                "ret5_10_30_vol5_ge1_5_macd",
                "5日漲幅 10% 至 30% + 5日平均量比 >= 1.5 + MACD 柱狀體 > 0",
                "research_only_not_pdf_core",
                lambda d: (
                    between(d["return_5d_pct"], 10, 30)
                    & (d["start_5d_avg_volume_ratio_vs_prev20"] >= 1.5)
                    & trueish(d["macd_hist_gt0"])
                ),
                "動能研究名單；進場假設必須使用訊號日後下一交易日開盤。",
            ),
        ]
    )

    for vol in [3.0, 5.0, 10.0]:
        specs.append(
            RuleSpec(
                "explosive_volume_red_candle",
                "爆天量紅K研究",
                f"vol{vol:g}_solid_red",
                f"量比 >= {vol:g} + 實體紅K + 上影線小 + 收盤接近日高",
                "research_only_not_pdf_core",
                lambda d, vol=vol: (d["volume_ratio_prev20"] >= vol) & d["solid_red_candle"],
                "研究用模型，參數驗證成熟前不納入核心 PDF 推薦模型。",
            )
        )

    return specs


_legacy_rule_specs = rule_specs


def rule_specs() -> list[RuleSpec]:
    remapped: list[RuleSpec] = []
    for spec in _legacy_rule_specs():
        if spec.model_id == "volume_range_breakout":
            remapped.append(
                RuleSpec(
                    spec.model_id,
                    spec.model_name_zh,
                    spec.parameter_set_id,
                    spec.parameter_summary,
                    "deprecated_research_only_not_pdf_core",
                    spec.condition,
                    spec.notes + " Legacy v1 is isolated after the v2 split and must not be treated as a production PDF core model.",
                    spec.parameter_role,
                    spec.production_parity_status,
                    spec.parity_blocker,
                    spec.variant_of,
                )
            )
        else:
            remapped.append(spec)
    return remapped


def summarize_rule(df: pd.DataFrame, spec: RuleSpec) -> tuple[dict[str, object], list[dict[str, object]]]:
    mask = spec.condition(df).fillna(False)
    picked = df[mask].copy()
    n = len(picked)
    unique_stocks = picked["stock_id"].nunique() if n else 0
    detail_rows: list[dict[str, object]] = []
    best_horizon = ""
    best_avg = -math.inf
    best_win = 0.0
    for h in HORIZONS:
        close_col = f"next_open_to_d{h}_close_return_pct"
        high_col = f"next_open_to_d{h}_high_return_pct"
        if close_col not in picked.columns:
            continue
        valid = picked.dropna(subset=[close_col])
        mature = len(valid)
        win = float((valid[close_col] > 0).mean() * 100.0) if mature else math.nan
        avg = float(valid[close_col].mean()) if mature else math.nan
        med = float(valid[close_col].median()) if mature else math.nan
        high_avg = float(valid[high_col].mean()) if mature and high_col in valid.columns else math.nan
        high_win_5 = float((valid[high_col] >= 5).mean() * 100.0) if mature and high_col in valid.columns else math.nan
        if mature and not math.isnan(avg) and avg > best_avg and h <= 10:
            best_avg = avg
            best_horizon = f"D+{h}"
            best_win = win
        detail_rows.append(
            {
                "model_id": spec.model_id,
                "model_name_zh": spec.model_name_zh,
                "parameter_set_id": spec.parameter_set_id,
                "horizon": f"D+{h}",
                "entry_basis": "signal_date_next_open",
                "exit_close_basis": f"D+{h}_close",
                "exit_high_basis": f"D+{h}_intraday_high",
                "mature_count": mature,
                "close_win_rate_pct": round(win, 2) if not math.isnan(win) else "",
                "avg_close_return_pct": round(avg, 2) if not math.isnan(avg) else "",
                "median_close_return_pct": round(med, 2) if not math.isnan(med) else "",
                "avg_high_return_pct": round(high_avg, 2) if not math.isnan(high_avg) else "",
                "high_5pct_hit_rate_pct": round(high_win_5, 2) if not math.isnan(high_win_5) else "",
            }
        )

    summary = {
        "generated_at": now_text(),
        "model_id": spec.model_id,
        "model_name_zh": spec.model_name_zh,
        "parameter_set_id": spec.parameter_set_id,
        "parameter_summary": spec.parameter_summary,
        "parameter_role": spec.parameter_role,
        "production_parity_status": spec.production_parity_status,
        "parity_blocker": spec.parity_blocker,
        "variant_of": spec.variant_of,
        "pdf_visibility": spec.pdf_visibility,
        "entry_basis": "signal_date_next_open",
        "selected_stock_days": n,
        "selected_unique_stocks": unique_stocks,
        "best_close_horizon_d1_d10": best_horizon,
        "best_close_win_rate_pct": round(best_win, 2) if best_horizon else "",
        "best_avg_close_return_pct": round(best_avg, 2) if best_horizon else "",
        "sample_status": sample_status(n),
        "apply_status": "candidate_parameter_review" if n >= MIN_REVIEW_SAMPLE else "do_not_apply_insufficient_sample",
        "notes": spec.notes,
    }
    if spec.model_id == V2_HIGH_MODEL_ID and spec.parameter_role == "production_baseline":
        metrics = V2_APPROVAL_METRICS[V2_HIGH_MODEL_ID]
        selected_days, unique_stocks = high_position_approval_baseline_counts()
        summary.update(
            {
                "selected_stock_days": selected_days,
                "selected_unique_stocks": unique_stocks,
                "best_close_horizon_d1_d10": "D+15_operation",
                "best_close_win_rate_pct": round(float(metrics["best_evidence_win_rate"]), 2),
                "best_avg_close_return_pct": round(float(metrics["volume_v2_avg_return_pct"]), 2),
                "sample_status": sample_status(selected_days),
                "apply_status": "candidate_parameter_review",
                "notes": (
                    spec.notes
                    + " Baseline counts and performance are sourced from the approved high-position "
                    "D+15 close-only operation audit, not from the generic D+N horizon replay columns."
                ),
            }
        )
    for h in [1, 2, 3, 5, 10, 20]:
        row = next((r for r in detail_rows if r["horizon"] == f"D+{h}"), None)
        summary[f"d{h}_mature_count"] = row["mature_count"] if row else 0
        summary[f"d{h}_close_win_rate_pct"] = row["close_win_rate_pct"] if row else ""
        summary[f"d{h}_avg_close_return_pct"] = row["avg_close_return_pct"] if row else ""
        summary[f"d{h}_avg_high_return_pct"] = row["avg_high_return_pct"] if row else ""
    return summary, detail_rows


def current_production_core_models() -> pd.DataFrame:
    current = build_parameter_table(build_specs()).copy()
    current = current[current["pdf_visibility"].eq("pdf_core_model")].copy()
    return current.drop_duplicates("model_id", keep="first").reset_index(drop=True)


def high_position_approval_baseline_counts() -> tuple[int, int]:
    metrics = V2_APPROVAL_METRICS[V2_HIGH_MODEL_ID]
    selected_days = int(float(metrics["best_evidence_sample_size"]))
    unique_stocks = 0
    if HIGH_POSITION_AUDIT_DETAIL_CSV.exists():
        detail = pd.read_csv(HIGH_POSITION_AUDIT_DETAIL_CSV, dtype=str).fillna("")
        if {"base_model_member", "stock_id"}.issubset(detail.columns):
            base = detail[detail["base_model_member"].astype(str).str.lower().eq("true")].copy()
            if not base.empty:
                selected_days = len(base)
                unique_stocks = int(base["stock_id"].nunique())
    return selected_days, unique_stocks


def build_model_parity(summary: pd.DataFrame) -> pd.DataFrame:
    production = current_production_core_models()
    baseline = summary[summary["parameter_role"].eq("production_baseline")].copy()
    rows: list[dict[str, object]] = []
    for _, prod in production.iterrows():
        model_id = str(prod.get("model_id", ""))
        base_rows = baseline[baseline["model_id"].eq(model_id)].copy()
        variant_rows = summary[
            summary["model_id"].eq(model_id) & ~summary["parameter_role"].eq("production_baseline")
        ].copy()
        if model_id == V2_HIGH_MODEL_ID:
            metrics = V2_APPROVAL_METRICS[V2_HIGH_MODEL_ID]
            status = "production_parity"
            baseline_ids = metrics["operation_module_id"]
            blockers = ""
            selected_days, unique_stocks = high_position_approval_baseline_counts()
        elif base_rows.empty:
            status = "missing_production_baseline"
            baseline_ids = ""
            blockers = "research rule_specs() has no production_baseline row for this production core model"
            selected_days = ""
            unique_stocks = ""
        else:
            statuses = sorted(set(base_rows["production_parity_status"].astype(str)))
            if statuses == ["production_parity"]:
                status = "production_parity"
            elif "proxy_only" in statuses:
                status = "proxy_only"
            else:
                status = "production_proxy"
            baseline_ids = ",".join(base_rows["parameter_set_id"].astype(str))
            blockers = "; ".join(
                sorted(
                    {
                        str(value).strip()
                        for value in base_rows["parity_blocker"].fillna("")
                        if str(value).strip()
                    }
                )
            )
            if model_id == "w_bottom_right_side" and status == "production_parity":
                selected_days = int(W_BOTTOM_APPROVAL_METRICS["sample_size"])
                unique_stocks = int(W_BOTTOM_APPROVAL_METRICS["unique_stock_count"])
            elif model_id == "neckline_volume_breakout_confirmation" and status == "production_parity":
                selected_days = int(NECKLINE_APPROVAL_METRICS["tradable_entry_count"])
                unique_stocks = int(NECKLINE_APPROVAL_METRICS["unique_stock_count"])
            else:
                selected_days = int(pd.to_numeric(base_rows["selected_stock_days"], errors="coerce").fillna(0).sum())
                unique_stocks = int(pd.to_numeric(base_rows["selected_unique_stocks"], errors="coerce").fillna(0).max())
        rows.append(
            {
                "generated_at": now_text(),
                "model_id": model_id,
                "model_name_zh": prod.get("model_name_zh", ""),
                "production_pdf_visibility": prod.get("pdf_visibility", ""),
                "production_parameter_status": prod.get("parameter_status", ""),
                "production_main_conditions": prod.get("main_conditions", ""),
                "research_baseline_status": status,
                "research_baseline_parameter_set_id": baseline_ids,
                "research_variant_count": len(variant_rows),
                "baseline_selected_stock_days": selected_days,
                "baseline_selected_unique_stocks": unique_stocks,
                "parity_blocker": blockers,
                "completion_rule": (
                    "usable_as_exact_baseline"
                    if status == "production_parity"
                    else "usable_for_relative_research_only_until_blocker_resolved"
                ),
            }
        )
    return pd.DataFrame(rows)


PRICE_PULLBACK_OPERATION_CANDIDATES = [
    {
        "operation_candidate_id": "d10_close_target5_loss3",
        "holding_window_days": 10,
        "target_basis": "D+10_close",
        "target_return_pct": 5.0,
        "stop_basis": "D+10_close",
        "stop_return_pct": -3.0,
        "entry_rule": "signal_date_next_open after price_pullback_23ema production proxy replay",
        "exit_rule": "research close-only target at D+10; no intraday path ordering",
    },
    {
        "operation_candidate_id": "d20_close_target5_loss3",
        "holding_window_days": 20,
        "target_basis": "D+20_close",
        "target_return_pct": 5.0,
        "stop_basis": "D+20_close",
        "stop_return_pct": -3.0,
        "entry_rule": "signal_date_next_open after price_pullback_23ema production proxy replay",
        "exit_rule": "research close-only target at D+20; no intraday path ordering",
    },
    {
        "operation_candidate_id": "d20_high_target5_low_stop5_order_unresolved",
        "holding_window_days": 20,
        "target_basis": "max_D+20_intraday_high",
        "target_return_pct": 5.0,
        "stop_basis": "min_D+20_intraday_low",
        "stop_return_pct": -5.0,
        "entry_rule": "signal_date_next_open after price_pullback_23ema production proxy replay",
        "exit_rule": "research high/low target-stop study; same-window hit order is unresolved",
    },
    {
        "operation_candidate_id": "d20_high_target8_low_stop5_order_unresolved",
        "holding_window_days": 20,
        "target_basis": "max_D+20_intraday_high",
        "target_return_pct": 8.0,
        "stop_basis": "min_D+20_intraday_low",
        "stop_return_pct": -5.0,
        "entry_rule": "signal_date_next_open after price_pullback_23ema production proxy replay",
        "exit_rule": "research high/low target-stop study; same-window hit order is unresolved",
    },
]


PRICE_PULLBACK_ENTRY_FILTERS = [
    {
        "entry_filter_id": "baseline_replay",
        "entry_signal_rule": "no extra candle/volume confirmation beyond production proxy replay",
        "condition": lambda d: bool_series(d, True),
    },
    {
        "entry_filter_id": "volume_red_k_vol1.2",
        "entry_signal_rule": "bullish red K with volume_ratio_prev20 >= 1.2",
        "condition": lambda d: price_pullback_red_k_entry_filter(d, 1.2, solid=False),
    },
    {
        "entry_filter_id": "solid_volume_red_k_vol1.2",
        "entry_signal_rule": "solid red K with volume_ratio_prev20 >= 1.2",
        "condition": lambda d: price_pullback_red_k_entry_filter(d, 1.2, solid=True),
    },
    {
        "entry_filter_id": "solid_volume_red_k_vol1.5",
        "entry_signal_rule": "solid red K with volume_ratio_prev20 >= 1.5",
        "condition": lambda d: price_pullback_red_k_entry_filter(d, 1.5, solid=True),
    },
    {
        "entry_filter_id": "prior_ext20_ema10_runup20_pullback5",
        "entry_signal_rule": "prior 20d high was >=10% above 23EMA, prior 20d range runup >=20%, and signal close is at least 5% below that high",
        "condition": lambda d: price_pullback_prior_extension_filter(d, 20, 10.0, 20.0, 5.0),
    },
    {
        "entry_filter_id": "prior_ext30_ema12_runup25_pullback8",
        "entry_signal_rule": "prior 30d high was >=12% above 23EMA, prior 30d range runup >=25%, and signal close is at least 8% below that high",
        "condition": lambda d: price_pullback_prior_extension_filter(d, 30, 12.0, 25.0, 8.0),
    },
    {
        "entry_filter_id": "prior_ext60_ema15_runup35_pullback10",
        "entry_signal_rule": "prior 60d high was >=15% above 23EMA, prior 60d range runup >=35%, and signal close is at least 10% below that high",
        "condition": lambda d: price_pullback_prior_extension_filter(d, 60, 15.0, 35.0, 10.0),
    },
]


PRICE_PULLBACK_PRIOR_HIGH_STOP_GRID = [
    {
        "stop_reference_id": "ma20",
        "candidate_label": "monthline",
        "stop_reference_name": "current 20MA/monthline",
    },
    {
        "stop_reference_id": "ema23",
        "candidate_label": "ema23",
        "stop_reference_name": "current 23EMA",
    },
    {
        "stop_reference_id": "lower_ma20_ema23",
        "candidate_label": "lower_ma20_ema23",
        "stop_reference_name": "lower of current 20MA and 23EMA",
    },
]
PRICE_PULLBACK_PRIOR_HIGH_TARGET_WINDOWS = [20, 30, 60]
PRICE_PULLBACK_PRIOR_HIGH_STOP_PCTS = [1.0, 2.0, 3.0, 4.0]
PRICE_PULLBACK_PRIOR_HIGH_STOP_CONSECUTIVE_DAYS = [2, 3, 4]


def _price_pullback_prior_high_stop_candidates() -> list[dict[str, object]]:
    candidates: list[dict[str, object]] = []
    for target_window in PRICE_PULLBACK_PRIOR_HIGH_TARGET_WINDOWS:
        for ref in PRICE_PULLBACK_PRIOR_HIGH_STOP_GRID:
            for stop_pct in PRICE_PULLBACK_PRIOR_HIGH_STOP_PCTS:
                for consecutive_days in PRICE_PULLBACK_PRIOR_HIGH_STOP_CONSECUTIVE_DAYS:
                    pct_label = f"{stop_pct:g}"
                    candidates.append(
                        {
                            "operation_module_candidate_id": (
                                f"next_open_prev{target_window}_high_breakout_"
                                f"{ref['candidate_label']}_stop{pct_label}pct_{consecutive_days}d_d20_close_exit"
                            ),
                            "target_rule_id": "prior_high_breakout",
                            "target_lookback_days": target_window,
                            "target_return_pct": "",
                            "stop_rule_id": "sustained_close_below_reference_pct",
                            "stop_reference_id": ref["stop_reference_id"],
                            "stop_reference_name": ref["stop_reference_name"],
                            "stop_buffer_pct": stop_pct,
                            "stop_consecutive_days": consecutive_days,
                            "stop_return_pct": "",
                            "holding_window_days": 20,
                            "entry_rule_id": "signal_date_next_open",
                            "buy_point_rule": (
                                "Buy next open only when the price_pullback_23ema signal and the entry filter both hold on signal date."
                            ),
                            "stop_rule": (
                                f"Failure stop when close stays at least {pct_label}% below "
                                f"the {ref['stop_reference_name']} for {consecutive_days} consecutive trading days; "
                                "exit at the next trading day open after the confirming close."
                            ),
                            "exit_rule": (
                                f"If no previous {target_window}-day high breakout or sustained reference stop appears by D+20, "
                                "exit at D+20 close."
                            ),
                        }
                    )
    return candidates


PRICE_PULLBACK_OPERATION_MODULE_CANDIDATES = [
    {
        "operation_module_candidate_id": "next_open_tp5_intraday_stop5_d20_close_exit",
        "target_rule_id": "intraday_return_pct",
        "target_return_pct": 5.0,
        "stop_rule_id": "intraday_low_stop5",
        "stop_return_pct": -5.0,
        "holding_window_days": 20,
        "entry_rule_id": "signal_date_next_open",
        "buy_point_rule": "Buy next open only when the price_pullback_23ema signal and the entry filter both hold on signal date.",
        "stop_rule": "Failure stop when intraday low first reaches -5% from next-open entry.",
        "exit_rule": "If no target or stop appears by D+20, exit at D+20 close.",
    },
    {
        "operation_module_candidate_id": "next_open_tp5_structure_stop_d20_close_exit",
        "target_rule_id": "intraday_return_pct",
        "target_return_pct": 5.0,
        "stop_rule_id": "close_below_23ema_or_support_2pct",
        "stop_return_pct": "",
        "holding_window_days": 20,
        "entry_rule_id": "signal_date_next_open",
        "buy_point_rule": "Buy next open only when the price_pullback_23ema signal and the entry filter both hold on signal date.",
        "stop_rule": "Failure stop when a close first falls below the higher of signal-day 23EMA/support references by 2%.",
        "exit_rule": "If no target or structure stop appears by D+20, exit at D+20 close.",
    },
    {
        "operation_module_candidate_id": "next_open_tp8_intraday_stop5_d20_close_exit",
        "target_rule_id": "intraday_return_pct",
        "target_return_pct": 8.0,
        "stop_rule_id": "intraday_low_stop5",
        "stop_return_pct": -5.0,
        "holding_window_days": 20,
        "entry_rule_id": "signal_date_next_open",
        "buy_point_rule": "Buy next open only when the price_pullback_23ema signal and the entry filter both hold on signal date.",
        "stop_rule": "Failure stop when intraday low first reaches -5% from next-open entry.",
        "exit_rule": "If no target or stop appears by D+20, exit at D+20 close.",
    },
    {
        "operation_module_candidate_id": "next_open_tp8_structure_stop_d20_close_exit",
        "target_rule_id": "intraday_return_pct",
        "target_return_pct": 8.0,
        "stop_rule_id": "close_below_23ema_or_support_2pct",
        "stop_return_pct": "",
        "holding_window_days": 20,
        "entry_rule_id": "signal_date_next_open",
        "buy_point_rule": "Buy next open only when the price_pullback_23ema signal and the entry filter both hold on signal date.",
        "stop_rule": "Failure stop when a close first falls below the higher of signal-day 23EMA/support references by 2%.",
        "exit_rule": "If no target or structure stop appears by D+20, exit at D+20 close.",
    },
    *_price_pullback_prior_high_stop_candidates(),
]


PRICE_PULLBACK_FEATURE_CONFIRMATION_OPERATION_ID = (
    "next_open_prev20_high_breakout_lower_ma20_ema23_stop4pct_4d_d20_close_exit"
)

PRICE_PULLBACK_FEATURE_CONFIRMATION_FILTERS = [
    {
        "feature_filter_id": "baseline_replay",
        "feature_family": "baseline",
        "feature_rule": "no extra feature confirmation beyond production proxy replay",
        "feature_test_status": "tested_point_in_time",
        "data_status": "available_point_in_time_research_frame",
        "condition": lambda d: bool_series(d, True),
    },
    {
        "feature_filter_id": "prior_ext20_ema10_runup20_pullback5",
        "feature_family": "prior_extension",
        "feature_rule": "prior 20d high was >=10% above 23EMA, prior 20d range runup >=20%, signal close at least 5% below that high",
        "feature_test_status": "tested_point_in_time",
        "data_status": "available_point_in_time_research_frame",
        "condition": lambda d: price_pullback_prior_extension_filter(d, 20, 10.0, 20.0, 5.0),
    },
    {
        "feature_filter_id": "macd_hist_gt0",
        "feature_family": "technical",
        "feature_rule": "MACD histogram above zero on signal date",
        "feature_test_status": "tested_point_in_time",
        "data_status": "available_point_in_time_research_frame",
        "condition": lambda d: trueish_column(d, "macd_hist_gt0"),
    },
    {
        "feature_filter_id": "kd_bullish_not_overheated",
        "feature_family": "technical",
        "feature_rule": "KD bullish but not overheated on signal date",
        "feature_test_status": "tested_point_in_time",
        "data_status": "available_point_in_time_research_frame",
        "condition": lambda d: trueish_column(d, "kd_bullish_not_overheated"),
    },
    {
        "feature_filter_id": "macd_kd_confirm",
        "feature_family": "technical",
        "feature_rule": "MACD histogram above zero and KD bullish-not-overheated both hold",
        "feature_test_status": "tested_point_in_time",
        "data_status": "available_point_in_time_research_frame",
        "condition": price_pullback_macd_kd_confirm_filter,
    },
    {
        "feature_filter_id": "rsi14_40_70",
        "feature_family": "technical",
        "feature_rule": "RSI14 between 40 and 70 on signal date",
        "feature_test_status": "tested_point_in_time",
        "data_status": "available_point_in_time_research_frame",
        "condition": lambda d: between(numeric_column(d, "rsi14"), 40.0, 70.0).fillna(False),
    },
    {
        "feature_filter_id": "bb_width_not_extreme",
        "feature_family": "technical",
        "feature_rule": "Bollinger bandwidth percentile is not extreme",
        "feature_test_status": "tested_point_in_time",
        "data_status": "available_point_in_time_research_frame",
        "condition": lambda d: trueish_column(d, "bb_width_not_extreme"),
    },
    {
        "feature_filter_id": "obv_above_ma20",
        "feature_family": "technical_volume",
        "feature_rule": "OBV above OBV MA20 on signal date",
        "feature_test_status": "tested_point_in_time",
        "data_status": "computed_from_point_in_time_price_volume",
        "condition": price_pullback_obv_above_ma20_filter,
    },
    {
        "feature_filter_id": "tdcc_history_available",
        "feature_family": "chip",
        "feature_rule": "TDCC history is available for point-in-time join",
        "feature_test_status": "tested_point_in_time",
        "data_status": "available_point_in_time_research_frame",
        "condition": lambda d: trueish_column(d, "tdcc_history_available"),
    },
    {
        "feature_filter_id": "tdcc_consecutive_up_weeks_ge1",
        "feature_family": "chip",
        "feature_rule": "TDCC consecutive up weeks >= 1",
        "feature_test_status": "tested_point_in_time",
        "data_status": "available_point_in_time_research_frame",
        "condition": lambda d: trueish_column(d, "tdcc_history_available")
        & (numeric_column(d, "tdcc_consecutive_up_weeks") >= 1.0),
    },
    {
        "feature_filter_id": "tdcc_high_thresholds_up",
        "feature_family": "chip",
        "feature_rule": "large-holder TDCC high thresholds increased",
        "feature_test_status": "tested_point_in_time",
        "data_status": "available_point_in_time_research_frame",
        "condition": price_pullback_tdcc_high_thresholds_up_filter,
    },
    {
        "feature_filter_id": "tdcc_all_thresholds_up",
        "feature_family": "chip",
        "feature_rule": "all TDCC holder thresholds increased together",
        "feature_test_status": "tested_point_in_time",
        "data_status": "available_point_in_time_research_frame",
        "condition": lambda d: trueish_column(d, "tdcc_history_available") & trueish_column(d, "all_thresholds_up"),
    },
    {
        "feature_filter_id": "return20_0_25",
        "feature_family": "risk_control",
        "feature_rule": "20d return is between 0% and 25% to avoid deeply weak or excessively extended names",
        "feature_test_status": "tested_point_in_time",
        "data_status": "available_point_in_time_research_frame",
        "condition": price_pullback_return20_balanced_filter,
    },
    {
        "feature_filter_id": "pattern45_bull_pullback",
        "feature_family": "price_structure",
        "feature_rule": "45d return >=8%, 45d range width >=18%, and signal close sits in the 35%-80% zone of the prior 45d range",
        "feature_test_status": "tested_point_in_time",
        "data_status": "computed_from_point_in_time_price_history",
        "condition": price_pullback_45d_bullish_pullback_filter,
    },
    {
        "feature_filter_id": "tdcc_high_thresholds_up_return20_0_25",
        "feature_family": "combo_chip_risk_control",
        "feature_rule": "large-holder TDCC high thresholds increased and 20d return is between 0% and 25%",
        "feature_test_status": "tested_point_in_time",
        "data_status": "available_point_in_time_research_frame",
        "condition": lambda d: price_pullback_tdcc_high_thresholds_up_filter(d)
        & price_pullback_return20_balanced_filter(d),
    },
    {
        "feature_filter_id": "tdcc_consecutive_up_ge1_return20_0_25",
        "feature_family": "combo_chip_risk_control",
        "feature_rule": "TDCC consecutive up weeks >=1 and 20d return is between 0% and 25%",
        "feature_test_status": "tested_point_in_time",
        "data_status": "available_point_in_time_research_frame",
        "condition": lambda d: price_pullback_tdcc_consecutive_up_ge1_filter(d)
        & price_pullback_return20_balanced_filter(d),
    },
    {
        "feature_filter_id": "tdcc_high_thresholds_up_obv_above_ma20",
        "feature_family": "combo_chip_technical_volume",
        "feature_rule": "large-holder TDCC high thresholds increased and OBV above OBV MA20",
        "feature_test_status": "tested_point_in_time",
        "data_status": "available_point_in_time_research_frame",
        "condition": lambda d: price_pullback_tdcc_high_thresholds_up_filter(d)
        & price_pullback_obv_above_ma20_filter(d),
    },
    {
        "feature_filter_id": "tdcc_high_thresholds_up_macd_kd_confirm",
        "feature_family": "combo_chip_technical",
        "feature_rule": "large-holder TDCC high thresholds increased plus MACD/KD confirmation",
        "feature_test_status": "tested_point_in_time",
        "data_status": "available_point_in_time_research_frame",
        "condition": lambda d: price_pullback_tdcc_high_thresholds_up_filter(d)
        & price_pullback_macd_kd_confirm_filter(d),
    },
    {
        "feature_filter_id": "tdcc_high_thresholds_up_return20_0_25_obv_above_ma20",
        "feature_family": "combo_chip_risk_control_technical_volume",
        "feature_rule": "large-holder TDCC high thresholds increased, 20d return is between 0% and 25%, and OBV above OBV MA20",
        "feature_test_status": "tested_point_in_time",
        "data_status": "available_point_in_time_research_frame",
        "condition": lambda d: price_pullback_tdcc_high_thresholds_up_filter(d)
        & price_pullback_return20_balanced_filter(d)
        & price_pullback_obv_above_ma20_filter(d),
    },
    {
        "feature_filter_id": "theme_context_available",
        "feature_family": "theme_context",
        "feature_rule": "signal-date point-in-time daily theme context row is available from the background panel",
        "feature_test_status": "tested_point_in_time",
        "data_status": "joined_from_daily_model_signal_background_feature_panel_coverage_limited",
        "condition": price_pullback_theme_context_ready_filter,
    },
    {
        "feature_filter_id": "theme_context_mainstream_supported",
        "feature_family": "theme_context",
        "feature_rule": "signal-date theme status group is mainstream_supported or mainstream_overheated",
        "feature_test_status": "tested_point_in_time",
        "data_status": "joined_from_daily_model_signal_background_feature_panel_coverage_limited",
        "condition": price_pullback_theme_context_mainstream_filter,
    },
    {
        "feature_filter_id": "theme_context_leadership_not_overheated",
        "feature_family": "theme_context",
        "feature_rule": "signal-date theme final status is mainstream_leader, mainstream_follow_through, or emerging_theme, and the status group is not overheated",
        "feature_test_status": "tested_point_in_time",
        "data_status": "joined_from_daily_model_signal_background_feature_panel_coverage_limited",
        "condition": price_pullback_theme_context_leadership_not_overheated_filter,
    },
    {
        "feature_filter_id": "theme_context_volume_attack_selected",
        "feature_family": "theme_context",
        "feature_rule": "signal-date theme context marks the stock as selected in volume-attack theme status history",
        "feature_test_status": "tested_point_in_time",
        "data_status": "joined_from_daily_model_signal_background_feature_panel_coverage_limited",
        "condition": price_pullback_theme_context_volume_attack_selected_filter,
    },
    {
        "feature_filter_id": "tdcc_high_thresholds_up_return20_0_25_theme_context_mainstream_supported",
        "feature_family": "combo_chip_risk_control_theme_context",
        "feature_rule": "large-holder TDCC high thresholds increased, 20d return is between 0% and 25%, and signal-date theme context is mainstream-supported or overheated",
        "feature_test_status": "tested_point_in_time",
        "data_status": "joined_from_daily_model_signal_background_feature_panel_coverage_limited",
        "condition": lambda d: price_pullback_tdcc_high_thresholds_up_filter(d)
        & price_pullback_return20_balanced_filter(d)
        & price_pullback_theme_context_mainstream_filter(d),
    },
    {
        "feature_filter_id": "tdcc_high_thresholds_up_return20_0_25_theme_context_leadership_not_overheated",
        "feature_family": "combo_chip_risk_control_theme_context",
        "feature_rule": "large-holder TDCC high thresholds increased, 20d return is between 0% and 25%, and signal-date theme leadership is supported without overheated status",
        "feature_test_status": "tested_point_in_time",
        "data_status": "joined_from_daily_model_signal_background_feature_panel_coverage_limited",
        "condition": lambda d: price_pullback_tdcc_high_thresholds_up_filter(d)
        & price_pullback_return20_balanced_filter(d)
        & price_pullback_theme_context_leadership_not_overheated_filter(d),
    },
    {
        "feature_filter_id": "revenue_positive_or_strong",
        "feature_family": "revenue",
        "feature_rule": "candidate has snapshot-observed monthly revenue context and latest or cumulative revenue YoY is positive/strong",
        "feature_test_status": "tested_point_in_time",
        "data_status": "joined_from_monthly_revenue_pit_panel_coverage_limited_research_only",
        "condition": price_pullback_monthly_revenue_positive_or_strong_filter,
    },
    {
        "feature_filter_id": "tdcc_high_thresholds_up_return20_0_25_obv_above_ma20_revenue_positive_or_strong",
        "feature_family": "combo_chip_risk_control_technical_volume_revenue",
        "feature_rule": "large-holder TDCC high thresholds increased, 20d return is between 0% and 25%, OBV above MA20, and revenue is positive/strong where coverage-limited PIT context exists",
        "feature_test_status": "tested_point_in_time",
        "data_status": "joined_from_monthly_revenue_pit_panel_coverage_limited_research_only",
        "condition": lambda d: price_pullback_tdcc_high_thresholds_up_filter(d)
        & price_pullback_return20_balanced_filter(d)
        & price_pullback_obv_above_ma20_filter(d)
        & price_pullback_monthly_revenue_positive_or_strong_filter(d),
    },
    {
        "feature_filter_id": "market_background_regime",
        "feature_family": "market_background",
        "feature_rule": "market regime/risk background filter requires dated market feature join by signal date and market/index mapping",
        "feature_test_status": "deferred_join_required",
        "data_status": "market feature panel exists, but this artifact does not yet join it into stock-day rows",
        "condition": None,
    },
]


PRICE_PULLBACK_EXIT_RULE_FILTER_IDS = [
    "baseline_replay",
    "return20_0_25",
    "macd_kd_confirm",
    "obv_above_ma20",
    "tdcc_high_thresholds_up_return20_0_25",
    "tdcc_high_thresholds_up_return20_0_25_obv_above_ma20",
    "theme_context_mainstream_supported",
    "tdcc_high_thresholds_up_return20_0_25_theme_context_mainstream_supported",
]

PRICE_PULLBACK_EXIT_RULE_COMPARISON_CANDIDATES = [
    {
        "exit_rule_id": "intraday_prev20_high_touch_same_day_close",
        "formal_price_rule_status": "research_only_intraday_trigger",
        "target_rule_id": "intraday_prev20_high_touch",
        "profit_target_pct": "",
        "exit_price_rule": "same_day_close_after_intraday_previous_20d_high_touch",
        "exit_rule_zh": "盤中高點觸及訊號日前20日高點，當日收盤賣出。",
    },
    {
        "exit_rule_id": "close_prev20_high_break_next_open",
        "formal_price_rule_status": "close_confirmed_candidate",
        "target_rule_id": "close_prev20_high_break",
        "profit_target_pct": "",
        "exit_price_rule": "next_open_after_close_breaks_previous_20d_high",
        "exit_rule_zh": "收盤突破訊號日前20日高點，下一個交易日開盤賣出。",
    },
    {
        "exit_rule_id": "close_prev20_break_then_tp5_or_5ma_next_open",
        "formal_price_rule_status": "close_confirmed_candidate",
        "target_rule_id": "close_prev20_break_then_close_profit_target",
        "profit_target_pct": 5.0,
        "exit_price_rule": "next_open_after_profit_target_or_5ma_close_exit",
        "exit_rule_zh": "收盤突破訊號日前20日高點後續抱；收盤報酬達+5%或收盤跌破5MA，下一個交易日開盤賣出。",
    },
    {
        "exit_rule_id": "close_prev20_break_then_tp8_or_5ma_next_open",
        "formal_price_rule_status": "close_confirmed_candidate",
        "target_rule_id": "close_prev20_break_then_close_profit_target",
        "profit_target_pct": 8.0,
        "exit_price_rule": "next_open_after_profit_target_or_5ma_close_exit",
        "exit_rule_zh": "收盤突破訊號日前20日高點後續抱；收盤報酬達+8%或收盤跌破5MA，下一個交易日開盤賣出。",
    },
    {
        "exit_rule_id": "close_prev20_break_then_tp10_or_5ma_next_open",
        "formal_price_rule_status": "close_confirmed_candidate",
        "target_rule_id": "close_prev20_break_then_close_profit_target",
        "profit_target_pct": 10.0,
        "exit_price_rule": "next_open_after_profit_target_or_5ma_close_exit",
        "exit_rule_zh": "收盤突破訊號日前20日高點後續抱；收盤報酬達+10%或收盤跌破5MA，下一個交易日開盤賣出。",
    },
]

PRICE_PULLBACK_CONTINUATION_PROFILE_ENTRY_FILTER_IDS = [
    "baseline_replay",
    "tdcc_high_thresholds_up_return20_0_25",
    "tdcc_high_thresholds_up_return20_0_25_obv_above_ma20",
]
PRICE_PULLBACK_CONTINUATION_PROFILE_EXIT_RULE_IDS = [
    "close_prev20_break_then_tp5_or_5ma_next_open",
    "close_prev20_break_then_tp8_or_5ma_next_open",
    "close_prev20_break_then_tp10_or_5ma_next_open",
]
PRICE_PULLBACK_SUCCESS_NUMERIC_FEATURES = [
    ("volume_ratio_prev20", "technical_volume", "signal volume ratio vs previous 20 trading days"),
    ("return_20d_pct", "price_structure", "signal-date prior 20d return"),
    ("return_45d_pct", "price_structure", "signal-date prior 45d return"),
    ("range_width_45d_pct", "price_structure", "prior 45d range width"),
    ("close_position_45d_pct", "price_structure", "signal close position inside prior 45d range"),
    ("prior_extension_ema23_20d_pct", "price_structure", "prior 20d high extension above 23EMA"),
    ("prior_runup_20d_pct", "price_structure", "prior 20d range runup"),
    ("pullback_from_high_20d_pct", "price_structure", "signal close pullback from prior 20d high"),
    ("rsi14", "technical", "RSI14 on signal date"),
    ("obv_slope_5d", "technical_volume", "OBV 5d slope on signal date"),
    ("tdcc_consecutive_up_weeks", "chip", "TDCC consecutive up weeks"),
    ("monthly_revenue_latest_yoy_pct", "revenue", "coverage-limited latest monthly revenue YoY"),
    ("monthly_revenue_cumulative_yoy_pct", "revenue", "coverage-limited cumulative monthly revenue YoY"),
    ("theme_context_volume_ratio", "theme_context", "point-in-time theme context volume ratio"),
    ("theme_context_return_20d_pct", "theme_context", "point-in-time theme context 20d return"),
]
PRICE_PULLBACK_SUCCESS_BOOL_FEATURES = [
    ("macd_hist_gt0", "technical", "MACD histogram above zero"),
    ("kd_bullish_not_overheated", "technical", "KD bullish and not overheated"),
    ("obv_above_ma20", "technical_volume", "OBV above OBV MA20"),
    ("tdcc_history_available", "chip", "TDCC history available"),
    ("high_thresholds_up", "chip", "large-holder TDCC high thresholds increased"),
    ("theme_context_ready", "theme_context", "point-in-time theme context row available"),
    ("theme_context_mainstream_supported", "theme_context", "theme context mainstream-supported or overheated"),
    ("theme_context_leadership_supported", "theme_context", "theme context leadership supported"),
    ("theme_context_overheated", "theme_context", "theme context overheated"),
    ("theme_context_volume_attack_selected_flag", "theme_context", "theme context volume-attack selected"),
    ("monthly_revenue_context_ready", "revenue", "coverage-limited monthly revenue context row available"),
    ("monthly_revenue_positive_or_strong", "revenue", "monthly revenue latest/cumulative YoY is positive or strong"),
    ("monthly_revenue_numerical_anomaly_flag", "revenue", "monthly revenue numerical anomaly label"),
]
PRICE_PULLBACK_RESEARCH_SCORE_COMPONENTS = [
    {
        "component_id": "tdcc_high_thresholds_up",
        "component_family": "chip",
        "points": 2,
        "component_rule": "TDCC history exists and large-holder high thresholds increased on signal date",
        "condition": price_pullback_tdcc_high_thresholds_up_filter,
    },
    {
        "component_id": "return20_0_25",
        "component_family": "price_momentum_control",
        "points": 1,
        "component_rule": "prior 20d return is between 0% and 25%",
        "condition": price_pullback_return20_balanced_filter,
    },
    {
        "component_id": "return45_ge5",
        "component_family": "price_momentum",
        "points": 1,
        "component_rule": "prior 45d return is at least 5%",
        "condition": lambda d: (numeric_column(d, "return_45d_pct") >= 5.0).fillna(False),
    },
    {
        "component_id": "range_width45_ge28",
        "component_family": "price_structure",
        "points": 1,
        "component_rule": "prior 45d range width is at least 28%",
        "condition": lambda d: (numeric_column(d, "range_width_45d_pct") >= 28.0).fillna(False),
    },
    {
        "component_id": "prior_extension_ema23_20d_ge8",
        "component_family": "price_structure",
        "points": 1,
        "component_rule": "prior 20d high was at least 8% above 23EMA",
        "condition": lambda d: (numeric_column(d, "prior_extension_ema23_20d_pct") >= 8.0).fillna(False),
    },
    {
        "component_id": "prior_runup20_ge15",
        "component_family": "price_structure",
        "points": 1,
        "component_rule": "prior 20d range runup was at least 15%",
        "condition": lambda d: (numeric_column(d, "prior_runup_20d_pct") >= 15.0).fillna(False),
    },
    {
        "component_id": "obv_above_ma20",
        "component_family": "technical_volume",
        "points": 1,
        "component_rule": "OBV is above OBV MA20 on signal date",
        "condition": price_pullback_obv_above_ma20_filter,
    },
]
PRICE_PULLBACK_HIGH_RETURN_FEATURE_SCORE_COMPONENTS = [
    {
        "component_id": "prev20_target_space_ge8",
        "component_family": "payoff_space",
        "points": 2,
        "component_rule": "next-open buy price has at least 8% space to signal-date previous 20d high",
        "condition": lambda d: price_pullback_prev20_high_space_pct(d).ge(8.0).fillna(False),
        "component_role": "add_score_candidate",
    },
    {
        "component_id": "prev20_target_space_5_to_8",
        "component_family": "payoff_space",
        "points": 1,
        "component_rule": "next-open buy price has 5% to less than 8% space to signal-date previous 20d high",
        "condition": lambda d: (
            price_pullback_prev20_high_space_pct(d).ge(5.0)
            & price_pullback_prev20_high_space_pct(d).lt(8.0)
        ).fillna(False),
        "component_role": "add_score_candidate",
    },
    {
        "component_id": "prior_runup20_ge20",
        "component_family": "price_structure",
        "points": 1,
        "component_rule": "prior 20d high-low runup is at least 20%",
        "condition": lambda d: numeric_column(d, "prior_runup_20d_pct").ge(20.0).fillna(False),
        "component_role": "add_score_candidate",
    },
    {
        "component_id": "prior_extension_ema23_20d_ge10",
        "component_family": "price_structure",
        "points": 1,
        "component_rule": "prior 20d high is at least 10% above 23EMA",
        "condition": lambda d: numeric_column(d, "prior_extension_ema23_20d_pct").ge(10.0).fillna(False),
        "component_role": "add_score_candidate",
    },
    {
        "component_id": "return45_ge8_weak",
        "component_family": "price_momentum",
        "points": 1,
        "component_rule": "prior 45d return is at least 8%; weak add-score candidate",
        "condition": lambda d: numeric_column(d, "return_45d_pct").ge(8.0).fillna(False),
        "component_role": "weak_add_score_candidate",
    },
    {
        "component_id": "volume_red_or_solid_red_risk",
        "component_family": "candle_quality_risk",
        "points": -1,
        "component_rule": "signal date is volume red K with volume_ratio_prev20 >= 1.2 or a solid red candle; risk tag, not buy-quality bonus",
        "condition": lambda d: (
            (numeric_column(d, "volume_ratio_prev20").ge(1.2) & trueish_column(d, "bullish_attack_candle"))
            | trueish_column(d, "solid_red_candle")
        ).fillna(False),
        "component_role": "deduct_score_or_risk_tag_candidate",
    },
]
PRICE_PULLBACK_RESEARCH_SCORE_BUCKETS = [
    (0, 1, "score_0_1"),
    (2, 3, "score_2_3"),
    (4, 5, "score_4_5"),
    (6, 99, "score_6_plus"),
]
PRICE_PULLBACK_RESEARCH_SCORE_EXIT_RULE_IDS = [
    "close_prev20_high_break_next_open",
    "close_prev20_break_then_tp5_or_5ma_next_open",
    "close_prev20_break_then_tp8_or_5ma_next_open",
    "close_prev20_break_then_tp10_or_5ma_next_open",
]
PRICE_PULLBACK_ORDERED_CONDITION_EXIT_RULE_IDS = [
    "close_prev20_high_break_next_open",
    "close_prev20_break_then_tp5_or_5ma_next_open",
    "close_prev20_break_then_tp8_or_5ma_next_open",
    "close_prev20_break_then_tp10_or_5ma_next_open",
]
PRICE_PULLBACK_ORDERED_CONDITION_TESTS = [
    {
        "test_order": 0,
        "test_stage": "00_baseline",
        "condition_test_id": "baseline_replay",
        "condition_role_candidate": "baseline_anchor",
        "condition_rule": "production proxy replay only; no additional condition",
        "data_status": "available_point_in_time_research_frame",
        "condition": lambda d: bool_series(d, True),
    },
    {
        "test_order": 10,
        "test_stage": "01_single_gate_candidate",
        "condition_test_id": "return20_0_25",
        "condition_role_candidate": "required_gate_candidate",
        "condition_rule": "prior 20d return is between 0% and 25%",
        "data_status": "available_point_in_time_research_frame",
        "condition": price_pullback_return20_balanced_filter,
    },
    {
        "test_order": 20,
        "test_stage": "01_single_gate_candidate",
        "condition_test_id": "obv_above_ma20",
        "condition_role_candidate": "add_score_or_gate_candidate",
        "condition_rule": "OBV above OBV MA20 on signal date",
        "data_status": "computed_from_point_in_time_price_volume",
        "condition": price_pullback_obv_above_ma20_filter,
    },
    {
        "test_order": 30,
        "test_stage": "01_single_gate_candidate",
        "condition_test_id": "tdcc_high_thresholds_up",
        "condition_role_candidate": "add_score_or_gate_candidate",
        "condition_rule": "large-holder TDCC high thresholds increased",
        "data_status": "available_point_in_time_research_frame",
        "condition": price_pullback_tdcc_high_thresholds_up_filter,
    },
    {
        "test_order": 40,
        "test_stage": "01_single_gate_candidate",
        "condition_test_id": "macd_kd_confirm",
        "condition_role_candidate": "technical_confirmation_candidate",
        "condition_rule": "MACD histogram above zero and KD bullish-not-overheated both hold",
        "data_status": "available_point_in_time_research_frame",
        "condition": price_pullback_macd_kd_confirm_filter,
    },
    {
        "test_order": 45,
        "test_stage": "01_single_context_candidate",
        "condition_test_id": "revenue_positive_or_strong",
        "condition_role_candidate": "coverage_limited_add_score_candidate_not_required_gate",
        "condition_rule": "coverage-limited monthly revenue context exists and latest/cumulative revenue YoY is positive or strong",
        "data_status": "joined_from_monthly_revenue_pit_panel_coverage_limited_research_only",
        "condition": price_pullback_monthly_revenue_positive_or_strong_filter,
    },
    {
        "test_order": 50,
        "test_stage": "01_single_gate_candidate",
        "condition_test_id": "pattern45_bull_pullback",
        "condition_role_candidate": "pattern_gate_candidate",
        "condition_rule": "45d bullish pullback pattern: return >=8%, range width >=18%, close in 35%-80% zone",
        "data_status": "computed_from_point_in_time_price_history",
        "condition": price_pullback_45d_bullish_pullback_filter,
    },
    {
        "test_order": 60,
        "test_stage": "02_score_gate_candidate",
        "condition_test_id": "research_score_ge4",
        "condition_role_candidate": "broad_quality_score_gate_candidate",
        "condition_rule": "research bonus score is at least 4",
        "data_status": "research_only_score_not_production",
        "condition": lambda d: price_pullback_research_score_ge_filter(d, 4.0),
    },
    {
        "test_order": 70,
        "test_stage": "02_score_gate_candidate",
        "condition_test_id": "research_score_ge6",
        "condition_role_candidate": "strict_quality_score_gate_candidate",
        "condition_rule": "research bonus score is at least 6",
        "data_status": "research_only_score_not_production",
        "condition": lambda d: price_pullback_research_score_ge_filter(d, 6.0),
    },
    {
        "test_order": 80,
        "test_stage": "03_prev_high_space_candidate",
        "condition_test_id": "prev20_space_ge3",
        "condition_role_candidate": "sell_space_filter_candidate",
        "condition_rule": "next-open entry has at least 3% space to signal-day previous 20d high",
        "data_status": "entry_open_known_research_only",
        "condition": lambda d: price_pullback_prev20_high_space_filter(d, 3.0),
    },
    {
        "test_order": 90,
        "test_stage": "03_prev_high_space_candidate",
        "condition_test_id": "prev20_space_ge5",
        "condition_role_candidate": "sell_space_filter_candidate",
        "condition_rule": "next-open entry has at least 5% space to signal-day previous 20d high",
        "data_status": "entry_open_known_research_only",
        "condition": lambda d: price_pullback_prev20_high_space_filter(d, 5.0),
    },
    {
        "test_order": 100,
        "test_stage": "03_prev_high_space_candidate",
        "condition_test_id": "prev20_space_ge8",
        "condition_role_candidate": "sell_space_filter_candidate",
        "condition_rule": "next-open entry has at least 8% space to signal-day previous 20d high",
        "data_status": "entry_open_known_research_only",
        "condition": lambda d: price_pullback_prev20_high_space_filter(d, 8.0),
    },
    {
        "test_order": 110,
        "test_stage": "04_layered_candidate",
        "condition_test_id": "score_ge4_prev20_space_ge3",
        "condition_role_candidate": "candidate_v2_gate_stack",
        "condition_rule": "research score >=4 and at least 3% space to previous 20d high",
        "data_status": "research_only_score_not_production",
        "condition": lambda d: price_pullback_research_score_ge_filter(d, 4.0)
        & price_pullback_prev20_high_space_filter(d, 3.0),
    },
    {
        "test_order": 120,
        "test_stage": "04_layered_candidate",
        "condition_test_id": "score_ge4_prev20_space_ge5",
        "condition_role_candidate": "candidate_v2_gate_stack",
        "condition_rule": "research score >=4 and at least 5% space to previous 20d high",
        "data_status": "research_only_score_not_production",
        "condition": lambda d: price_pullback_research_score_ge_filter(d, 4.0)
        & price_pullback_prev20_high_space_filter(d, 5.0),
    },
    {
        "test_order": 130,
        "test_stage": "04_layered_candidate",
        "condition_test_id": "score_ge4_tdcc_high_or_obv",
        "condition_role_candidate": "candidate_v2_bonus_stack",
        "condition_rule": "research score >=4 and either TDCC high thresholds increased or OBV above MA20",
        "data_status": "research_only_score_not_production",
        "condition": lambda d: price_pullback_research_score_ge_filter(d, 4.0)
        & (price_pullback_tdcc_high_thresholds_up_filter(d) | price_pullback_obv_above_ma20_filter(d)),
    },
    {
        "test_order": 140,
        "test_stage": "04_layered_candidate",
        "condition_test_id": "score_ge4_prev20_space_ge3_tdcc_or_obv",
        "condition_role_candidate": "candidate_v2_gate_stack",
        "condition_rule": "research score >=4, at least 3% previous-high space, and TDCC high-thresholds up or OBV above MA20",
        "data_status": "research_only_score_not_production",
        "condition": lambda d: price_pullback_research_score_ge_filter(d, 4.0)
        & price_pullback_prev20_high_space_filter(d, 3.0)
        & (price_pullback_tdcc_high_thresholds_up_filter(d) | price_pullback_obv_above_ma20_filter(d)),
    },
    {
        "test_order": 145,
        "test_stage": "04_layered_candidate",
        "condition_test_id": "v1_base_revenue_positive_or_strong",
        "condition_role_candidate": "coverage_limited_v1_base_add_score_candidate",
        "condition_rule": "return20_0_25 plus TDCC high-thresholds up plus OBV above MA20 plus coverage-limited positive/strong revenue",
        "data_status": "joined_from_monthly_revenue_pit_panel_coverage_limited_research_only",
        "condition": lambda d: price_pullback_return20_balanced_filter(d)
        & price_pullback_tdcc_high_thresholds_up_filter(d)
        & price_pullback_obv_above_ma20_filter(d)
        & price_pullback_monthly_revenue_positive_or_strong_filter(d),
    },
    {
        "test_order": 150,
        "test_stage": "04_layered_candidate",
        "condition_test_id": "score_ge6_prev20_space_ge3",
        "condition_role_candidate": "strict_candidate_v2_gate_stack",
        "condition_rule": "research score >=6 and at least 3% space to previous 20d high",
        "data_status": "research_only_score_not_production",
        "condition": lambda d: price_pullback_research_score_ge_filter(d, 6.0)
        & price_pullback_prev20_high_space_filter(d, 3.0),
    },
    {
        "test_order": 200,
        "test_stage": "05_v1_candidate_stack",
        "condition_test_id": "v1_gate_return20_0_25",
        "condition_role_candidate": "v1_required_gate_candidate",
        "condition_rule": "v1 draft: require prior 20d return between 0% and 25%",
        "data_status": "research_only_v1_candidate_not_production",
        "condition": price_pullback_return20_balanced_filter,
    },
    {
        "test_order": 210,
        "test_stage": "05_v1_candidate_stack",
        "condition_test_id": "v1_gate_return20_obv",
        "condition_role_candidate": "v1_required_gate_plus_technical_candidate",
        "condition_rule": "v1 draft: require return20_0_25 and OBV above MA20",
        "data_status": "research_only_v1_candidate_not_production",
        "condition": lambda d: price_pullback_return20_balanced_filter(d)
        & price_pullback_obv_above_ma20_filter(d),
    },
    {
        "test_order": 220,
        "test_stage": "05_v1_candidate_stack",
        "condition_test_id": "v1_gate_return20_tdcc_high",
        "condition_role_candidate": "v1_required_gate_plus_chip_candidate",
        "condition_rule": "v1 draft: require return20_0_25 and large-holder TDCC high thresholds increased",
        "data_status": "research_only_v1_candidate_not_production",
        "condition": lambda d: price_pullback_return20_balanced_filter(d)
        & price_pullback_tdcc_high_thresholds_up_filter(d),
    },
    {
        "test_order": 230,
        "test_stage": "05_v1_candidate_stack",
        "condition_test_id": "v1_gate_return20_obv_or_tdcc",
        "condition_role_candidate": "v1_required_gate_plus_bonus_candidate",
        "condition_rule": "v1 draft: require return20_0_25 and either OBV above MA20 or TDCC high thresholds increased",
        "data_status": "research_only_v1_candidate_not_production",
        "condition": lambda d: price_pullback_return20_balanced_filter(d)
        & (price_pullback_obv_above_ma20_filter(d) | price_pullback_tdcc_high_thresholds_up_filter(d)),
    },
    {
        "test_order": 240,
        "test_stage": "05_v1_candidate_stack",
        "condition_test_id": "v1_gate_return20_score_ge4",
        "condition_role_candidate": "v1_required_gate_plus_score_candidate",
        "condition_rule": "v1 draft: require return20_0_25 and research score >=4",
        "data_status": "research_only_v1_candidate_not_production",
        "condition": lambda d: price_pullback_return20_balanced_filter(d)
        & price_pullback_research_score_ge_filter(d, 4.0),
    },
    {
        "test_order": 250,
        "test_stage": "05_v1_candidate_stack",
        "condition_test_id": "v1_gate_return20_score_ge4_obv_or_tdcc",
        "condition_role_candidate": "v1_required_gate_plus_score_bonus_candidate",
        "condition_rule": "v1 draft: require return20_0_25, research score >=4, and either OBV above MA20 or TDCC high thresholds increased",
        "data_status": "research_only_v1_candidate_not_production",
        "condition": lambda d: price_pullback_return20_balanced_filter(d)
        & price_pullback_research_score_ge_filter(d, 4.0)
        & (price_pullback_obv_above_ma20_filter(d) | price_pullback_tdcc_high_thresholds_up_filter(d)),
    },
    {
        "test_order": 260,
        "test_stage": "05_v1_candidate_stack",
        "condition_test_id": "v1_gate_return20_score_ge4_obv_or_tdcc_space3",
        "condition_role_candidate": "v1_required_gate_plus_score_bonus_space_candidate",
        "condition_rule": "v1 draft: require return20_0_25, research score >=4, OBV or TDCC confirmation, and at least 3% previous-high space",
        "data_status": "research_only_v1_candidate_not_production",
        "condition": lambda d: price_pullback_return20_balanced_filter(d)
        & price_pullback_research_score_ge_filter(d, 4.0)
        & (price_pullback_obv_above_ma20_filter(d) | price_pullback_tdcc_high_thresholds_up_filter(d))
        & price_pullback_prev20_high_space_filter(d, 3.0),
    },
    {
        "test_order": 900,
        "test_stage": "90_deferred_theme_context",
        "condition_test_id": "theme_context_mainstream_supported",
        "condition_role_candidate": "deferred_context_bonus_not_gate",
        "condition_rule": "signal-date theme context is mainstream-supported or overheated",
        "data_status": "coverage_limited_wait_for_mature_d20_samples",
        "condition": price_pullback_theme_context_mainstream_filter,
    },
]

PRICE_PULLBACK_LIFECYCLE_REPLAY_CONDITION_IDS = [
    "baseline_replay",
    "v1_gate_return20_tdcc_high",
]

PRICE_PULLBACK_LIFECYCLE_REPLAY_EXTRA_CONDITION_TESTS = [
    {
        "test_order": 225,
        "test_stage": "05_v1_candidate_stack",
        "condition_test_id": "v1_gate_return20_tdcc_high_obv",
        "condition_role_candidate": "v1_required_gate_plus_chip_and_technical_candidate",
        "condition_rule": "v1 draft: require return20_0_25, large-holder TDCC high thresholds increased, and OBV above MA20",
        "data_status": "research_only_v1_candidate_not_production",
        "condition": lambda d: price_pullback_return20_balanced_filter(d)
        & price_pullback_tdcc_high_thresholds_up_filter(d)
        & price_pullback_obv_above_ma20_filter(d),
    },
    {
        "test_order": 1000,
        "test_stage": "06_candle_quality_reference",
        "condition_test_id": "volume_red_k_vol1.2",
        "condition_role_candidate": "buy_point_quality_reference_not_required_gate",
        "condition_rule": "bullish red K with volume_ratio_prev20 >= 1.2",
        "data_status": "computed_from_point_in_time_price_volume",
        "condition": lambda d: price_pullback_red_k_entry_filter(d, 1.2, solid=False),
    },
    {
        "test_order": 1010,
        "test_stage": "06_candle_quality_reference",
        "condition_test_id": "solid_volume_red_k_vol1.2",
        "condition_role_candidate": "buy_point_quality_reference_not_required_gate",
        "condition_rule": "solid red K with volume_ratio_prev20 >= 1.2",
        "data_status": "computed_from_point_in_time_price_volume",
        "condition": lambda d: price_pullback_red_k_entry_filter(d, 1.2, solid=True),
    },
    {
        "test_order": 1020,
        "test_stage": "06_candle_quality_reference",
        "condition_test_id": "solid_volume_red_k_vol1.5",
        "condition_role_candidate": "buy_point_quality_reference_not_required_gate",
        "condition_rule": "solid red K with volume_ratio_prev20 >= 1.5",
        "data_status": "computed_from_point_in_time_price_volume",
        "condition": lambda d: price_pullback_red_k_entry_filter(d, 1.5, solid=True),
    },
]


def _price_pullback_lifecycle_replay_condition_tests() -> list[dict[str, object]]:
    ordered_by_id = {
        safe_str(spec["condition_test_id"]): spec
        for spec in PRICE_PULLBACK_ORDERED_CONDITION_TESTS
    }
    tests = [
        ordered_by_id[condition_id]
        for condition_id in PRICE_PULLBACK_LIFECYCLE_REPLAY_CONDITION_IDS
        if condition_id in ordered_by_id
    ]
    tests.extend(PRICE_PULLBACK_LIFECYCLE_REPLAY_EXTRA_CONDITION_TESTS)
    return sorted(tests, key=lambda spec: int(spec["test_order"]))


def _rate(count: int, total: int) -> float | str:
    if total <= 0:
        return ""
    return round(count / total * 100.0, 2)


def build_price_pullback_operation_research(df: pd.DataFrame) -> pd.DataFrame:
    base_mask = current_price_pullback_baseline_proxy(df).fillna(False)
    rows: list[dict[str, object]] = []
    generated_at = now_text()
    for entry_filter in PRICE_PULLBACK_ENTRY_FILTERS:
        filter_mask = entry_filter["condition"](df).fillna(False)
        picked = df[base_mask & filter_mask].copy()
        for candidate in PRICE_PULLBACK_OPERATION_CANDIDATES:
            h = int(candidate["holding_window_days"])
            close_col = f"next_open_to_d{h}_close_return_pct"
            high_col = f"next_open_to_d{h}_high_return_pct"
            low_col = f"next_open_to_d{h}_low_return_pct"
            required = [close_col]
            if str(candidate["target_basis"]).startswith("max_"):
                required.extend([high_col, low_col])
            valid = (
                picked.dropna(subset=required).copy()
                if all(col in picked.columns for col in required)
                else picked.iloc[0:0].copy()
            )
            mature = len(valid)

            target = float(candidate["target_return_pct"])
            stop = float(candidate["stop_return_pct"])
            if mature and str(candidate["target_basis"]).startswith("max_"):
                target_hit = valid[high_col] >= target
                stop_hit = valid[low_col] <= stop
                ambiguous = target_hit & stop_hit
                win = target_hit & ~stop_hit
                loss = stop_hit & ~target_hit
                neutral = ~(win | loss | ambiguous)
                avg_high = float(valid[high_col].mean())
                high5_hit = float((valid[high_col] >= 5.0).mean() * 100.0)
            elif mature:
                win = valid[close_col] >= target
                loss = valid[close_col] <= stop
                ambiguous = bool_series(valid)
                neutral = ~(win | loss)
                avg_high = math.nan
                high5_hit = math.nan
            else:
                win = loss = neutral = ambiguous = bool_series(valid)
                avg_high = math.nan
                high5_hit = math.nan

            win_count = int(win.sum()) if mature else 0
            loss_count = int(loss.sum()) if mature else 0
            neutral_count = int(neutral.sum()) if mature else 0
            ambiguous_count = int(ambiguous.sum()) if mature else 0
            avg_close = float(valid[close_col].mean()) if mature else math.nan
            median_close = float(valid[close_col].median()) if mature else math.nan
            rows.append(
                {
                    "generated_at": generated_at,
                    "model_id": "price_pullback_23ema",
                    "model_name_zh": "股價回檔模型",
                    "research_baseline_parameter_set_id": "production_current_proxy",
                    "research_baseline_status": "production_proxy",
                    "entry_filter_id": entry_filter["entry_filter_id"],
                    "entry_signal_rule": entry_filter["entry_signal_rule"],
                    "operation_candidate_id": candidate["operation_candidate_id"],
                    "advisory_status": "not_production_ready_research_only",
                    "approved_for_daily": False,
                    "entry_rule": f"{candidate['entry_rule']} + {entry_filter['entry_signal_rule']}",
                    "target_rule": f"{candidate['target_basis']} >= {target:g}%",
                    "stop_rule": f"{candidate['stop_basis']} <= {stop:g}%",
                    "exit_rule": candidate["exit_rule"],
                    "outcome_rule": "win/neutral/loss research labels only; not a validated trading module",
                    "holding_window_days": h,
                    "selected_stock_days": len(picked),
                    "selected_unique_stocks": picked["stock_id"].nunique() if not picked.empty else 0,
                    "mature_count": mature,
                    "win_count": win_count,
                    "neutral_count": neutral_count,
                    "loss_count": loss_count,
                    "ambiguous_order_count": ambiguous_count,
                    "win_rate_pct": _rate(win_count, mature),
                    "neutral_rate_pct": _rate(neutral_count, mature),
                    "loss_rate_pct": _rate(loss_count, mature),
                    "ambiguous_order_rate_pct": _rate(ambiguous_count, mature),
                    "avg_close_return_pct": round(avg_close, 2) if not math.isnan(avg_close) else "",
                    "median_close_return_pct": round(median_close, 2) if not math.isnan(median_close) else "",
                    "avg_high_return_pct": round(avg_high, 2) if not math.isnan(avg_high) else "",
                    "high_5pct_hit_rate_pct": round(high5_hit, 2) if not math.isnan(high5_hit) else "",
                    "path_order_limitation": (
                        "high/low target-stop studies cannot determine whether target or stop happened first inside the holding window"
                        if str(candidate["target_basis"]).startswith("max_")
                        else "close-only study does not model intraday stop execution"
                    ),
                    "promotion_blocker": "requires exact daily candidate row parity plus validated buy/sell/stop operation module",
                }
            )
    return pd.DataFrame(rows)


def write_price_pullback_operation_research(operation: pd.DataFrame) -> None:
    write_csv(operation, PRICE_PULLBACK_OPERATION_CSV)
    write_csv(operation, PRICE_PULLBACK_OPERATION_HISTORY_CSV)
    write_csv(operation, DOCS_PRICE_PULLBACK_OPERATION_CSV)
    lines = [
        "# Price Pullback 23EMA Operation Research",
        "",
        f"- generated_at: `{now_text()}`",
        "- model_id: `price_pullback_23ema`",
        "- status: `not_production_ready_research_only`",
        "- entry_basis: `signal_date_next_open` after production proxy replay",
        "- scope: advisory operation candidates only; this does not approve daily production use",
        "- blocker: exact daily candidate row parity and validated buy/sell/stop module are still required before promotion",
        "",
        markdown_table(
            operation,
            [
                "entry_filter_id",
                "operation_candidate_id",
                "selected_stock_days",
                "mature_count",
                "win_rate_pct",
                "neutral_rate_pct",
                "loss_rate_pct",
                "ambiguous_order_rate_pct",
                "avg_close_return_pct",
                "avg_high_return_pct",
                "high_5pct_hit_rate_pct",
                "promotion_blocker",
            ],
            limit=50,
        ),
    ]
    PRICE_PULLBACK_OPERATION_MD.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8", newline="\n")
    DOCS_PRICE_PULLBACK_OPERATION_MD.write_text(
        PRICE_PULLBACK_OPERATION_MD.read_text(encoding="utf-8"),
        encoding="utf-8",
        newline="\n",
    )


def _first_hit_day(hits: pd.DataFrame) -> pd.Series:
    arr = hits.fillna(False).to_numpy(dtype=bool)
    if arr.size == 0:
        return pd.Series(dtype=float, index=hits.index)
    any_hit = arr.any(axis=1)
    first_idx = arr.argmax(axis=1) + 1
    return pd.Series(np.where(any_hit, first_idx, math.nan), index=hits.index, dtype=float)


def _first_consecutive_hit_day(hits: pd.DataFrame, consecutive_days: int) -> pd.Series:
    if consecutive_days <= 1:
        return _first_hit_day(hits)
    arr = hits.fillna(False).to_numpy(dtype=bool)
    if arr.size == 0:
        return pd.Series(dtype=float, index=hits.index)
    result = np.full(arr.shape[0], math.nan)
    for row_idx, row in enumerate(arr):
        streak = 0
        for day_idx, hit in enumerate(row, start=1):
            streak = streak + 1 if hit else 0
            if streak >= consecutive_days:
                result[row_idx] = day_idx
                break
    return pd.Series(result, index=hits.index, dtype=float)


def _mean_or_blank(series: pd.Series) -> float | str:
    clean = pd.to_numeric(series, errors="coerce").dropna()
    if clean.empty:
        return ""
    return round(float(clean.mean()), 2)


def build_price_pullback_time_cost_backtest(df: pd.DataFrame) -> pd.DataFrame:
    base_mask = current_price_pullback_baseline_proxy(df).fillna(False)
    high_cols = [f"next_open_to_d{day}_day_high_return_pct" for day in range(1, TIME_COST_HORIZON_DAYS + 1)]
    low_cols = [f"next_open_to_d{day}_day_low_return_pct" for day in range(1, TIME_COST_HORIZON_DAYS + 1)]
    rows: list[dict[str, object]] = []
    generated_at = now_text()
    for entry_filter in PRICE_PULLBACK_ENTRY_FILTERS:
        filter_mask = entry_filter["condition"](df).fillna(False)
        picked = df[base_mask & filter_mask].copy()
        valid = (
            picked.dropna(subset=high_cols + low_cols).copy()
            if all(col in picked.columns for col in high_cols + low_cols)
            else picked.iloc[0:0].copy()
        )
        mature = len(valid)
        if mature:
            target_day = _first_hit_day(valid[high_cols] >= TIME_COST_TARGET_PCT)
            stop_day = _first_hit_day(valid[low_cols] <= TIME_COST_STOP_PCT)
            target_before_stop = target_day.notna() & (stop_day.isna() | (target_day < stop_day))
            stop_before_target = stop_day.notna() & (target_day.isna() | (stop_day < target_day))
            same_day = target_day.notna() & stop_day.notna() & target_day.eq(stop_day)
            no_decision = target_day.isna() & stop_day.isna()
            first_decision_day = pd.Series(TIME_COST_HORIZON_DAYS, index=valid.index, dtype=float)
            first_decision_day = first_decision_day.mask(target_before_stop, target_day)
            first_decision_day = first_decision_day.mask(stop_before_target, stop_day)
            first_decision_day = first_decision_day.mask(same_day, target_day)
        else:
            target_day = stop_day = first_decision_day = pd.Series(dtype=float, index=valid.index)
            target_before_stop = stop_before_target = same_day = no_decision = bool_series(valid)

        target_before_count = int(target_before_stop.sum()) if mature else 0
        stop_before_count = int(stop_before_target.sum()) if mature else 0
        same_day_count = int(same_day.sum()) if mature else 0
        no_decision_count = int(no_decision.sum()) if mature else 0
        rows.append(
            {
                "generated_at": generated_at,
                "model_id": "price_pullback_23ema",
                "model_name_zh": "股價回檔模型",
                "research_baseline_parameter_set_id": "production_current_proxy",
                "research_baseline_status": "production_proxy",
                "entry_filter_id": entry_filter["entry_filter_id"],
                "entry_signal_rule": entry_filter["entry_signal_rule"],
                "advisory_status": "not_production_ready_research_only",
                "approved_for_daily": False,
                "entry_basis": "signal_date_next_open",
                "target_rule": f"first intraday high >= +{TIME_COST_TARGET_PCT:g}% through D+{TIME_COST_HORIZON_DAYS}",
                "stop_rule": f"first intraday low <= {TIME_COST_STOP_PCT:g}% through D+{TIME_COST_HORIZON_DAYS}",
                "same_day_rule": "if target and stop both hit on the same daily candle, order is unresolved",
                "selected_stock_days": len(picked),
                "selected_unique_stocks": picked["stock_id"].nunique() if not picked.empty else 0,
                "mature_count": mature,
                "target_before_stop_count": target_before_count,
                "stop_before_target_count": stop_before_count,
                "same_day_target_stop_count": same_day_count,
                "no_decision_after_20d_count": no_decision_count,
                "target_before_stop_rate_pct": _rate(target_before_count, mature),
                "stop_before_target_rate_pct": _rate(stop_before_count, mature),
                "same_day_target_stop_rate_pct": _rate(same_day_count, mature),
                "no_decision_after_20d_rate_pct": _rate(no_decision_count, mature),
                "avg_days_to_target_5pct": _mean_or_blank(target_day),
                "avg_days_to_stop_5pct": _mean_or_blank(stop_day),
                "avg_holding_days_if_win": _mean_or_blank(target_day[target_before_stop]) if mature else "",
                "avg_holding_days_if_loss": _mean_or_blank(stop_day[stop_before_target]) if mature else "",
                "avg_first_decision_or_20d_days": _mean_or_blank(first_decision_day),
                "time_cost_interpretation": "lower no_decision and lower avg_first_decision_or_20d_days imply lower capital time cost",
                "promotion_blocker": "requires exact daily candidate row parity plus validated buy/sell/stop operation module",
            }
        )
    return pd.DataFrame(rows)


def write_price_pullback_time_cost_backtest(time_cost: pd.DataFrame) -> None:
    write_csv(time_cost, PRICE_PULLBACK_TIME_COST_CSV)
    write_csv(time_cost, PRICE_PULLBACK_TIME_COST_HISTORY_CSV)
    write_csv(time_cost, DOCS_PRICE_PULLBACK_TIME_COST_CSV)
    lines = [
        "# Price Pullback 23EMA Time Cost Backtest",
        "",
        f"- generated_at: `{now_text()}`",
        "- model_id: `price_pullback_23ema`",
        "- status: `not_production_ready_research_only`",
        "- entry_basis: `signal_date_next_open`",
        f"- target_rule: first intraday high >= `+{TIME_COST_TARGET_PCT:g}%` through `D+{TIME_COST_HORIZON_DAYS}`",
        f"- stop_rule: first intraday low <= `{TIME_COST_STOP_PCT:g}%` through `D+{TIME_COST_HORIZON_DAYS}`",
        "- same_day_rule: if daily high and low hit target/stop on the same day, order is unresolved",
        "- scope: advisory time-cost research only; this does not approve daily production use",
        "",
        markdown_table(
            time_cost,
            [
                "entry_filter_id",
                "selected_stock_days",
                "mature_count",
                "target_before_stop_rate_pct",
                "stop_before_target_rate_pct",
                "same_day_target_stop_rate_pct",
                "no_decision_after_20d_rate_pct",
                "avg_holding_days_if_win",
                "avg_holding_days_if_loss",
                "avg_first_decision_or_20d_days",
            ],
            limit=50,
        ),
    ]
    PRICE_PULLBACK_TIME_COST_MD.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8", newline="\n")
    DOCS_PRICE_PULLBACK_TIME_COST_MD.write_text(
        PRICE_PULLBACK_TIME_COST_MD.read_text(encoding="utf-8"),
        encoding="utf-8",
        newline="\n",
    )


def _structure_stop_return_pct(df: pd.DataFrame) -> pd.Series:
    refs = pd.DataFrame(
        {
            "ema23": numeric_column(df, "ema23"),
            "platform_low": numeric_column(df, "platform_low"),
            "short_platform_low": numeric_column(df, "short_platform_low"),
            "previous_20d_low": numeric_column(df, "previous_20d_low"),
            "range_low_20d_prev": numeric_column(df, "range_low_20d_prev"),
        },
        index=df.index,
    )
    refs = refs.where(refs > 0)
    stop_price = refs.max(axis=1, skipna=True) * 0.98
    entry_price = numeric_column(df, "next_open")
    return (stop_price / entry_price.replace(0, pd.NA) - 1.0) * 100.0


def _future_reference_frame(valid: pd.DataFrame, h: int, reference_id: str, output_cols: list[str]) -> pd.DataFrame:
    ma20_cols = [f"future_d{day}_ma20" for day in range(1, h + 1)]
    ema23_cols = [f"future_d{day}_ema23" for day in range(1, h + 1)]
    if reference_id == "ma20":
        refs = valid[ma20_cols].apply(pd.to_numeric, errors="coerce")
    elif reference_id == "ema23":
        refs = valid[ema23_cols].apply(pd.to_numeric, errors="coerce")
    elif reference_id == "lower_ma20_ema23":
        ma20_refs = valid[ma20_cols].apply(pd.to_numeric, errors="coerce")
        ema23_refs = valid[ema23_cols].apply(pd.to_numeric, errors="coerce")
        ma20_refs.columns = output_cols
        ema23_refs.columns = output_cols
        return ma20_refs.combine(ema23_refs, np.minimum)
    else:
        raise ValueError(f"Unsupported stop_reference_id: {reference_id}")
    refs.columns = output_cols
    return refs


def _value_at_day(values: pd.DataFrame, day: pd.Series) -> pd.Series:
    result = pd.Series(math.nan, index=values.index, dtype=float)
    clean_day = pd.to_numeric(day, errors="coerce")
    mask = clean_day.notna()
    if not mask.any():
        return result
    arr = values.to_numpy(dtype=float)
    row_positions = np.flatnonzero(mask.to_numpy())
    col_positions = clean_day[mask].astype(int).to_numpy() - 1
    valid_col = (col_positions >= 0) & (col_positions < arr.shape[1])
    result.iloc[row_positions[valid_col]] = arr[row_positions[valid_col], col_positions[valid_col]]
    return result


def _blank_operation_outcome() -> dict[str, object]:
    return {
        "mature_count": 0,
        "win_count": 0,
        "neutral_count": 0,
        "failure_count": 0,
        "same_day_unresolved_count": 0,
        "win_rate_pct": "",
        "neutral_rate_pct": "",
        "failure_rate_pct": "",
        "same_day_unresolved_rate_pct": "",
        "avg_d20_close_return_pct": "",
        "median_d20_close_return_pct": "",
        "avg_realized_return_pct": "",
        "avg_win_realized_return_pct": "",
        "avg_failure_realized_return_pct": "",
        "avg_neutral_realized_return_pct": "",
        "avg_realized_or_d20_days": "",
        "avg_days_to_win": "",
        "avg_days_to_failure": "",
    }


def _operation_required_columns(candidate: dict[str, object]) -> list[str]:
    h = int(candidate["holding_window_days"])
    required = [f"next_open_to_d{day}_day_high_return_pct" for day in range(1, h + 1)]
    required.extend(f"next_open_to_d{day}_day_low_return_pct" for day in range(1, h + 1))
    required.extend(f"next_open_to_d{day}_day_close_return_pct" for day in range(1, h + 1))
    required.append(f"next_open_to_d{h}_close_return_pct")
    if candidate.get("target_rule_id") in {"prev20_high_breakout", "prior_high_breakout"}:
        target_lookback_days = int(candidate.get("target_lookback_days", 20))
        required.extend(["next_open", f"range_high_{target_lookback_days}d_prev"])
    if candidate["stop_rule_id"] == "close_below_23ema_or_support_2pct":
        required.extend(["next_open", "ema23"])
    if candidate["stop_rule_id"] in {"sustained_close_below_ma20_pct", "sustained_close_below_reference_pct"}:
        required.append("next_open")
        required.extend(f"future_d{day + 1}_open" for day in range(1, h + 1))
        reference_id = str(candidate.get("stop_reference_id", "ma20"))
        if reference_id in {"ma20", "lower_ma20_ema23"}:
            required.extend(f"future_d{day}_ma20" for day in range(1, h + 1))
        if reference_id in {"ema23", "lower_ma20_ema23"}:
            required.extend(f"future_d{day}_ema23" for day in range(1, h + 1))
    return required


def _operation_outcome_counts(
    valid: pd.DataFrame,
    candidate: dict[str, object],
) -> dict[str, object]:
    h = int(candidate["holding_window_days"])
    high_cols = [f"next_open_to_d{day}_day_high_return_pct" for day in range(1, h + 1)]
    low_cols = [f"next_open_to_d{day}_day_low_return_pct" for day in range(1, h + 1)]
    close_cols = [f"next_open_to_d{day}_day_close_return_pct" for day in range(1, h + 1)]
    final_close_col = f"next_open_to_d{h}_close_return_pct"

    target_return_at_hit: pd.Series
    if candidate.get("target_rule_id") in {"prev20_high_breakout", "prior_high_breakout"}:
        entry_price = numeric_column(valid, "next_open")
        target_lookback_days = int(candidate.get("target_lookback_days", 20))
        target_price = numeric_column(valid, f"range_high_{target_lookback_days}d_prev")
        target_pct_series = (target_price / entry_price.replace(0, pd.NA) - 1.0) * 100.0
        target_day = _first_hit_day(valid[high_cols].ge(target_pct_series, axis=0))
        target_return_at_hit = target_pct_series
    else:
        target_pct = float(candidate["target_return_pct"])
        target_day = _first_hit_day(valid[high_cols] >= target_pct)
        target_return_at_hit = pd.Series(target_pct, index=valid.index, dtype=float)

    if candidate["stop_rule_id"] == "intraday_low_stop5":
        stop_pct = float(candidate["stop_return_pct"])
        stop_day = _first_hit_day(valid[low_cols] <= stop_pct)
        stop_return_at_hit = pd.Series(stop_pct, index=valid.index, dtype=float)
    elif candidate["stop_rule_id"] == "close_below_23ema_or_support_2pct":
        stop_pct_series = _structure_stop_return_pct(valid)
        stop_day = _first_hit_day(valid[close_cols].le(stop_pct_series, axis=0))
        stop_return_at_hit = _value_at_day(valid[close_cols].apply(pd.to_numeric, errors="coerce"), stop_day)
    elif candidate["stop_rule_id"] in {"sustained_close_below_ma20_pct", "sustained_close_below_reference_pct"}:
        entry_price = numeric_column(valid, "next_open")
        stop_pct = float(candidate.get("stop_buffer_pct", candidate.get("monthline_stop_pct", 0.0)))
        consecutive_days = int(candidate.get("stop_consecutive_days", candidate.get("monthline_stop_consecutive_days", 1)))
        reference_id = str(candidate.get("stop_reference_id", "ma20"))
        close_returns = valid[close_cols].apply(pd.to_numeric, errors="coerce")
        refs = _future_reference_frame(valid, h, reference_id, close_cols)
        stop_threshold = (refs.mul(1.0 - stop_pct / 100.0).div(entry_price, axis=0) - 1.0) * 100.0
        stop_hits = close_returns.le(stop_threshold)
        stop_day = _first_consecutive_hit_day(stop_hits, consecutive_days)
        stop_return_at_hit = _value_at_day(_future_open_return_frame(valid, h), stop_day)
    else:
        raise ValueError(f"Unsupported stop_rule_id: {candidate['stop_rule_id']}")

    target_before_stop = target_day.notna() & (stop_day.isna() | (target_day < stop_day))
    stop_before_target = stop_day.notna() & (target_day.isna() | (stop_day < target_day))
    same_day_unresolved = target_day.notna() & stop_day.notna() & target_day.eq(stop_day)
    no_trigger = target_day.isna() & stop_day.isna()
    final_close_return = pd.to_numeric(valid[final_close_col], errors="coerce")
    neutral = no_trigger & final_close_return.ge(0)
    late_failure = no_trigger & final_close_return.lt(0)
    failure = stop_before_target | late_failure

    realized_days = pd.Series(h, index=valid.index, dtype=float)
    realized_days = realized_days.mask(target_before_stop, target_day)
    realized_days = realized_days.mask(stop_before_target, stop_day)
    realized_days = realized_days.mask(same_day_unresolved, target_day)

    realized_return = pd.Series(math.nan, index=valid.index, dtype=float)
    realized_return = realized_return.mask(target_before_stop, target_return_at_hit)
    realized_return = realized_return.mask(stop_before_target, stop_return_at_hit)
    realized_return = realized_return.mask(no_trigger, final_close_return)

    win_count = int(target_before_stop.sum())
    neutral_count = int(neutral.sum())
    failure_count = int(failure.sum())
    same_day_count = int(same_day_unresolved.sum())
    mature = len(valid)
    return {
        "mature_count": mature,
        "win_count": win_count,
        "neutral_count": neutral_count,
        "failure_count": failure_count,
        "same_day_unresolved_count": same_day_count,
        "win_rate_pct": _rate(win_count, mature),
        "neutral_rate_pct": _rate(neutral_count, mature),
        "failure_rate_pct": _rate(failure_count, mature),
        "same_day_unresolved_rate_pct": _rate(same_day_count, mature),
        "avg_d20_close_return_pct": round(float(final_close_return.mean()), 2) if mature else "",
        "median_d20_close_return_pct": round(float(final_close_return.median()), 2) if mature else "",
        "avg_realized_return_pct": _mean_or_blank(realized_return),
        "avg_win_realized_return_pct": _mean_or_blank(realized_return[target_before_stop]) if mature else "",
        "avg_failure_realized_return_pct": _mean_or_blank(realized_return[failure]) if mature else "",
        "avg_neutral_realized_return_pct": _mean_or_blank(realized_return[neutral]) if mature else "",
        "avg_realized_or_d20_days": _mean_or_blank(realized_days),
        "avg_days_to_win": _mean_or_blank(target_day[target_before_stop]) if mature else "",
        "avg_days_to_failure": _mean_or_blank(realized_days[failure]) if mature else "",
    }


def build_price_pullback_operation_module_research(df: pd.DataFrame) -> pd.DataFrame:
    base_mask = current_price_pullback_baseline_proxy(df).fillna(False)
    rows: list[dict[str, object]] = []
    generated_at = now_text()
    for entry_filter in PRICE_PULLBACK_ENTRY_FILTERS:
        filter_mask = entry_filter["condition"](df).fillna(False)
        picked = df[base_mask & filter_mask].copy()
        for candidate in PRICE_PULLBACK_OPERATION_MODULE_CANDIDATES:
            h = int(candidate["holding_window_days"])
            required = [f"next_open_to_d{day}_day_high_return_pct" for day in range(1, h + 1)]
            required.extend(f"next_open_to_d{day}_day_low_return_pct" for day in range(1, h + 1))
            required.extend(f"next_open_to_d{day}_day_close_return_pct" for day in range(1, h + 1))
            required.append(f"next_open_to_d{h}_close_return_pct")
            if candidate.get("target_rule_id") in {"prev20_high_breakout", "prior_high_breakout"}:
                target_lookback_days = int(candidate.get("target_lookback_days", 20))
                required.extend(["next_open", f"range_high_{target_lookback_days}d_prev"])
            if candidate["stop_rule_id"] == "close_below_23ema_or_support_2pct":
                required.extend(["next_open", "ema23"])
            if candidate["stop_rule_id"] in {"sustained_close_below_ma20_pct", "sustained_close_below_reference_pct"}:
                required.append("next_open")
                reference_id = str(candidate.get("stop_reference_id", "ma20"))
                if reference_id in {"ma20", "lower_ma20_ema23"}:
                    required.extend(f"future_d{day}_ma20" for day in range(1, h + 1))
                if reference_id in {"ema23", "lower_ma20_ema23"}:
                    required.extend(f"future_d{day}_ema23" for day in range(1, h + 1))
            valid = (
                picked.dropna(subset=required).copy()
                if all(col in picked.columns for col in required)
                else picked.iloc[0:0].copy()
            )
            outcome = _operation_outcome_counts(valid, candidate) if not valid.empty else {
                "mature_count": 0,
                "win_count": 0,
                "neutral_count": 0,
                "failure_count": 0,
                "same_day_unresolved_count": 0,
                "win_rate_pct": "",
                "neutral_rate_pct": "",
                "failure_rate_pct": "",
                "same_day_unresolved_rate_pct": "",
                "avg_d20_close_return_pct": "",
                "median_d20_close_return_pct": "",
                "avg_realized_return_pct": "",
                "avg_win_realized_return_pct": "",
                "avg_failure_realized_return_pct": "",
                "avg_neutral_realized_return_pct": "",
                "avg_realized_or_d20_days": "",
                "avg_days_to_win": "",
                "avg_days_to_failure": "",
            }
            target_lookback_days = candidate.get("target_lookback_days", "")
            rows.append(
                {
                    "generated_at": generated_at,
                    "model_id": "price_pullback_23ema",
                    "model_name_zh": "股價回檔模型",
                    "research_baseline_parameter_set_id": "production_current_proxy",
                    "research_baseline_status": "production_proxy",
                    "operation_module_candidate_id": candidate["operation_module_candidate_id"],
                    "entry_filter_id": entry_filter["entry_filter_id"],
                    "entry_signal_rule": entry_filter["entry_signal_rule"],
                    "entry_rule_id": candidate["entry_rule_id"],
                    "buy_point_rule": f"{candidate['buy_point_rule']} Entry filter: {entry_filter['entry_signal_rule']}",
                    "target_rule": (
                        f"Win if first intraday high breaks above signal-day previous {target_lookback_days}-day high before stop through D+{h}."
                        if candidate.get("target_rule_id") in {"prev20_high_breakout", "prior_high_breakout"}
                        else f"Win if first intraday high reaches +{float(candidate['target_return_pct']):g}% before stop through D+{h}."
                    ),
                    "target_lookback_days": target_lookback_days,
                    "stop_rule_id": candidate["stop_rule_id"],
                    "stop_reference_id": candidate.get("stop_reference_id", ""),
                    "stop_reference_name": candidate.get("stop_reference_name", ""),
                    "stop_buffer_pct": candidate.get("stop_buffer_pct", ""),
                    "stop_consecutive_days": candidate.get("stop_consecutive_days", ""),
                    "stop_rule": candidate["stop_rule"],
                    "exit_rule": candidate["exit_rule"],
                    "win_definition": "target hit before stop",
                    "neutral_definition": "no target/stop by D+20 and D+20 close return >= 0%",
                    "failure_definition": "stop hit before target, or no target/stop by D+20 and D+20 close return < 0%",
                    "same_day_rule": "if target and stop are first seen on the same daily candle, classify as same_day_unresolved",
                    "holding_window_days": h,
                    "selected_stock_days": len(picked),
                    "selected_unique_stocks": picked["stock_id"].nunique() if not picked.empty else 0,
                    "advisory_status": "not_production_ready_research_only",
                    "approved_for_daily": False,
                    "promotion_readiness": "blocked_exact_daily_row_parity_and_operation_approval_required",
                    "promotion_blocker": "requires exact daily candidate row parity plus explicit promotion/sync PR before production use",
                    **outcome,
                }
            )
    return pd.DataFrame(rows)


def write_price_pullback_operation_module_research(module: pd.DataFrame) -> None:
    write_csv(module, PRICE_PULLBACK_OPERATION_MODULE_CSV)
    write_csv(module, PRICE_PULLBACK_OPERATION_MODULE_HISTORY_CSV)
    write_csv(module, DOCS_PRICE_PULLBACK_OPERATION_MODULE_CSV)
    lines = [
        "# Price Pullback 23EMA Operation Module Research",
        "",
        f"- generated_at: `{now_text()}`",
        "- model_id: `price_pullback_23ema`",
        "- status: `not_production_ready_research_only`",
        "- scope: advisory operation module candidates only; this does not approve daily production use",
        "- entry_basis: `signal_date_next_open`",
        "- win_definition: target hit before stop",
        "- neutral_definition: no target/stop by D+20 and D+20 close return >= 0%",
        "- failure_definition: stop hit before target, or no target/stop by D+20 and D+20 close return < 0%",
        "- same_day_rule: if target and stop are first seen on the same daily candle, classify as `same_day_unresolved`",
        "- blocker: exact daily candidate row parity and explicit promotion/sync PR are still required before production use",
        "",
        markdown_table(
            module,
            [
                "entry_filter_id",
                "operation_module_candidate_id",
                "target_lookback_days",
                "stop_reference_id",
                "stop_buffer_pct",
                "stop_consecutive_days",
                "selected_stock_days",
                "mature_count",
                "win_rate_pct",
                "neutral_rate_pct",
                "failure_rate_pct",
                "same_day_unresolved_rate_pct",
                "avg_realized_return_pct",
                "avg_win_realized_return_pct",
                "avg_failure_realized_return_pct",
                "avg_d20_close_return_pct",
                "avg_realized_or_d20_days",
                "promotion_readiness",
            ],
            limit=80,
        ),
    ]
    PRICE_PULLBACK_OPERATION_MODULE_MD.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8", newline="\n")
    DOCS_PRICE_PULLBACK_OPERATION_MODULE_MD.write_text(
        PRICE_PULLBACK_OPERATION_MODULE_MD.read_text(encoding="utf-8"),
        encoding="utf-8",
        newline="\n",
    )


def _price_pullback_feature_confirmation_operation_candidate() -> dict[str, object]:
    for candidate in PRICE_PULLBACK_OPERATION_MODULE_CANDIDATES:
        if candidate["operation_module_candidate_id"] == PRICE_PULLBACK_FEATURE_CONFIRMATION_OPERATION_ID:
            return candidate
    raise RuntimeError(f"Missing price_pullback feature confirmation operation: {PRICE_PULLBACK_FEATURE_CONFIRMATION_OPERATION_ID}")


def _add_feature_confirmation_deltas(result: pd.DataFrame) -> pd.DataFrame:
    if result.empty or "feature_filter_id" not in result.columns:
        return result
    out = result.copy()
    delta_map = {
        "win_rate_pct": "delta_vs_baseline_win_rate_pct",
        "failure_rate_pct": "delta_vs_baseline_failure_rate_pct",
        "avg_realized_return_pct": "delta_vs_baseline_avg_realized_return_pct",
        "avg_realized_or_d20_days": "delta_vs_baseline_avg_realized_or_d20_days",
    }
    for col in [*delta_map.values(), "selected_share_of_baseline_pct", "mature_share_of_baseline_pct"]:
        out[col] = np.nan

    baseline = out[out["feature_filter_id"].eq("baseline_replay")]
    if baseline.empty:
        return out
    baseline_row = baseline.iloc[0]
    baseline_values = {metric: pd.to_numeric(pd.Series([baseline_row.get(metric, "")]), errors="coerce").iloc[0] for metric in delta_map}
    baseline_selected = pd.to_numeric(pd.Series([baseline_row.get("selected_stock_days", "")]), errors="coerce").iloc[0]
    baseline_mature = pd.to_numeric(pd.Series([baseline_row.get("mature_count", "")]), errors="coerce").iloc[0]

    tested = out["feature_test_status"].eq("tested_point_in_time")
    for idx, row in out[tested].iterrows():
        selected = pd.to_numeric(pd.Series([row.get("selected_stock_days", "")]), errors="coerce").iloc[0]
        mature = pd.to_numeric(pd.Series([row.get("mature_count", "")]), errors="coerce").iloc[0]
        if pd.notna(selected) and pd.notna(baseline_selected) and baseline_selected > 0:
            out.at[idx, "selected_share_of_baseline_pct"] = round(float(selected / baseline_selected * 100.0), 2)
        if pd.notna(mature) and pd.notna(baseline_mature) and baseline_mature > 0:
            out.at[idx, "mature_share_of_baseline_pct"] = round(float(mature / baseline_mature * 100.0), 2)
        for metric, delta_col in delta_map.items():
            value = pd.to_numeric(pd.Series([row.get(metric, "")]), errors="coerce").iloc[0]
            baseline_value = baseline_values[metric]
            if pd.notna(value) and pd.notna(baseline_value):
                out.at[idx, delta_col] = round(float(value - baseline_value), 2)
    return out


def build_price_pullback_feature_confirmation_research(df: pd.DataFrame) -> pd.DataFrame:
    base_mask = current_price_pullback_baseline_proxy(df).fillna(False)
    candidate = _price_pullback_feature_confirmation_operation_candidate()
    required = _operation_required_columns(candidate)
    h = int(candidate["holding_window_days"])
    rows: list[dict[str, object]] = []
    generated_at = now_text()
    for feature_filter in PRICE_PULLBACK_FEATURE_CONFIRMATION_FILTERS:
        status = str(feature_filter["feature_test_status"])
        condition = feature_filter.get("condition")
        if status == "tested_point_in_time" and condition is not None:
            filter_mask = condition(df).fillna(False)
            picked = df[base_mask & filter_mask].copy()
            valid = (
                picked.dropna(subset=required).copy()
                if all(col in picked.columns for col in required)
                else picked.iloc[0:0].copy()
            )
            outcome = _operation_outcome_counts(valid, candidate) if not valid.empty else _blank_operation_outcome()
            selected_stock_days: int | str = len(picked)
            selected_unique_stocks: int | str = picked["stock_id"].nunique() if not picked.empty else 0
        else:
            picked = df.iloc[0:0].copy()
            outcome = _blank_operation_outcome()
            selected_stock_days = ""
            selected_unique_stocks = ""

        target_lookback_days = candidate.get("target_lookback_days", "")
        rows.append(
            {
                "generated_at": generated_at,
                "model_id": "price_pullback_23ema",
                "model_name_zh": "股價回檔模型",
                "research_artifact_id": "price_pullback_23ema_feature_confirmation_research",
                "research_baseline_parameter_set_id": "production_current_proxy",
                "research_baseline_status": "production_proxy",
                "fixed_operation_module_candidate_id": PRICE_PULLBACK_FEATURE_CONFIRMATION_OPERATION_ID,
                "feature_filter_id": feature_filter["feature_filter_id"],
                "feature_family": feature_filter["feature_family"],
                "feature_rule": feature_filter["feature_rule"],
                "feature_test_status": status,
                "data_status": feature_filter["data_status"],
                "entry_rule_id": candidate["entry_rule_id"],
                "buy_point_rule": candidate["buy_point_rule"],
                "target_rule": (
                    f"Win if first intraday high breaks above signal-day previous {target_lookback_days}-day high before stop through D+{h}."
                ),
                "target_lookback_days": target_lookback_days,
                "stop_rule_id": candidate["stop_rule_id"],
                "stop_reference_id": candidate.get("stop_reference_id", ""),
                "stop_reference_name": candidate.get("stop_reference_name", ""),
                "stop_buffer_pct": candidate.get("stop_buffer_pct", ""),
                "stop_consecutive_days": candidate.get("stop_consecutive_days", ""),
                "stop_rule": candidate["stop_rule"],
                "exit_rule": candidate["exit_rule"],
                "win_definition": "target hit before stop",
                "neutral_definition": "no target/stop by D+20 and D+20 close return >= 0%",
                "failure_definition": "stop hit before target, or no target/stop by D+20 and D+20 close return < 0%",
                "same_day_rule": "if target and stop are first seen on the same daily candle, classify as same_day_unresolved",
                "holding_window_days": h,
                "selected_stock_days": selected_stock_days,
                "selected_unique_stocks": selected_unique_stocks,
                "advisory_status": "not_production_ready_research_only",
                "approved_for_daily": False,
                "promotion_readiness": "blocked_exact_daily_row_parity_and_operation_approval_required",
                "promotion_blocker": "requires exact daily candidate row parity plus explicit promotion/sync PR before production use",
                **outcome,
            }
        )
    return _add_feature_confirmation_deltas(pd.DataFrame(rows))


def write_price_pullback_feature_confirmation_research(feature_confirmation: pd.DataFrame) -> None:
    write_csv(feature_confirmation, PRICE_PULLBACK_FEATURE_CONFIRMATION_CSV)
    write_csv(feature_confirmation, PRICE_PULLBACK_FEATURE_CONFIRMATION_HISTORY_CSV)
    write_csv(feature_confirmation, DOCS_PRICE_PULLBACK_FEATURE_CONFIRMATION_CSV)
    lines = [
        "# Price Pullback 23EMA Feature Confirmation Research",
        "",
        f"- generated_at: `{now_text()}`",
        "- model_id: `price_pullback_23ema`",
        "- status: `not_production_ready_research_only`",
        "- scope: advisory feature confirmation only; this does not approve daily production use",
        f"- fixed_operation_module_candidate_id: `{PRICE_PULLBACK_FEATURE_CONFIRMATION_OPERATION_ID}`",
        "- entry_basis: `signal_date_next_open` after production proxy replay plus the feature filter under test",
        "- target: previous 20-day high breakout before stop through D+20",
        "- stop: close stays at least 4% below lower of MA20 and EMA23 for 4 consecutive trading days, then exit at the next trading day open",
        "- theme_context_rows: signal-date/as-of theme status history is joined from the shared background panel; latest-only taxonomy is not used for historical labels",
        "- obv_rule: OBV above MA20 is retained as an add-score discussion candidate, not as a required gate",
        "- revenue_context_status: coverage-limited monthly revenue PIT context is joined from daily snapshot-observed rows; it is research-only and cannot be a formal required gate.",
        "- blocked rows: market background is documented as a data/join gap, not scored as a backtest result",
        "- blocker: exact daily candidate row parity and explicit promotion/sync PR are still required before production use",
        "",
        markdown_table(
            feature_confirmation,
            [
                "feature_filter_id",
                "feature_family",
                "feature_test_status",
                "data_status",
                "selected_stock_days",
                "selected_share_of_baseline_pct",
                "mature_count",
                "mature_share_of_baseline_pct",
                "win_rate_pct",
                "delta_vs_baseline_win_rate_pct",
                "neutral_rate_pct",
                "failure_rate_pct",
                "delta_vs_baseline_failure_rate_pct",
                "same_day_unresolved_rate_pct",
                "avg_realized_return_pct",
                "delta_vs_baseline_avg_realized_return_pct",
                "avg_realized_or_d20_days",
                "delta_vs_baseline_avg_realized_or_d20_days",
                "promotion_readiness",
            ],
            limit=80,
        ),
    ]
    PRICE_PULLBACK_FEATURE_CONFIRMATION_MD.write_text(
        "\n".join(lines).rstrip() + "\n",
        encoding="utf-8",
        newline="\n",
    )
    DOCS_PRICE_PULLBACK_FEATURE_CONFIRMATION_MD.write_text(
        PRICE_PULLBACK_FEATURE_CONFIRMATION_MD.read_text(encoding="utf-8"),
        encoding="utf-8",
        newline="\n",
    )


def _price_pullback_exit_rule_filters() -> list[dict[str, object]]:
    wanted = set(PRICE_PULLBACK_EXIT_RULE_FILTER_IDS)
    return [
        feature_filter
        for feature_filter in PRICE_PULLBACK_FEATURE_CONFIRMATION_FILTERS
        if feature_filter["feature_filter_id"] in wanted
    ]


def _future_open_return_frame(valid: pd.DataFrame, h: int) -> pd.DataFrame:
    entry_price = numeric_column(valid, "next_open").replace(0, pd.NA)
    cols = [f"future_d{day + 1}_open" for day in range(1, h + 1)]
    returns = valid[cols].apply(pd.to_numeric, errors="coerce").div(entry_price, axis=0)
    returns = (returns - 1.0) * 100.0
    returns.columns = [f"next_open_exit_after_d{day}_close_return_pct" for day in range(1, h + 1)]
    return returns


def _price_pullback_exit_required_columns(candidate: dict[str, object]) -> list[str]:
    h = TIME_COST_HORIZON_DAYS
    required = ["next_open", "range_high_20d_prev", f"next_open_to_d{h}_close_return_pct"]
    required.extend(f"next_open_to_d{day}_day_close_return_pct" for day in range(1, h + 1))
    required.extend(f"future_d{day}_ma20" for day in range(1, h + 1))
    required.extend(f"future_d{day}_ema23" for day in range(1, h + 1))
    required.extend(f"future_d{day + 1}_open" for day in range(1, h + 1))
    if candidate["target_rule_id"] == "intraday_prev20_high_touch":
        required.extend(f"next_open_to_d{day}_day_high_return_pct" for day in range(1, h + 1))
    if candidate["target_rule_id"] == "close_prev20_break_then_close_profit_target":
        required.extend(f"future_d{day}_ma5" for day in range(1, h + 1))
    return required


def _price_pullback_exit_rule_outcome_counts(
    valid: pd.DataFrame,
    candidate: dict[str, object],
) -> dict[str, object]:
    h = TIME_COST_HORIZON_DAYS
    close_cols = [f"next_open_to_d{day}_day_close_return_pct" for day in range(1, h + 1)]
    high_cols = [f"next_open_to_d{day}_day_high_return_pct" for day in range(1, h + 1)]
    final_close_col = f"next_open_to_d{h}_close_return_pct"
    close_returns = valid[close_cols].apply(pd.to_numeric, errors="coerce")
    final_close_return = pd.to_numeric(valid[final_close_col], errors="coerce")
    entry_price = numeric_column(valid, "next_open")
    target_price = numeric_column(valid, "range_high_20d_prev")
    prev20_target_pct = (target_price / entry_price.replace(0, pd.NA) - 1.0) * 100.0

    refs = _future_reference_frame(valid, h, "lower_ma20_ema23", close_cols)
    hard_stop_threshold = (refs.mul(0.96).div(entry_price.replace(0, pd.NA), axis=0) - 1.0) * 100.0
    hard_stop_day = _first_consecutive_hit_day(close_returns.le(hard_stop_threshold), 4)
    open_exit_returns = _future_open_return_frame(valid, h)
    hard_stop_return = _value_at_day(open_exit_returns, hard_stop_day)

    target_rule_id = str(candidate["target_rule_id"])
    trail_day = pd.Series(math.nan, index=valid.index, dtype=float)
    if target_rule_id == "intraday_prev20_high_touch":
        high_returns = valid[high_cols].apply(pd.to_numeric, errors="coerce")
        target_day = _first_hit_day(high_returns.ge(prev20_target_pct, axis=0))
        target_return_at_hit = _value_at_day(close_returns, target_day)
    elif target_rule_id == "close_prev20_high_break":
        target_day = _first_hit_day(close_returns.ge(prev20_target_pct, axis=0))
        target_return_at_hit = _value_at_day(open_exit_returns, target_day)
    elif target_rule_id == "close_prev20_break_then_close_profit_target":
        breakout_day = _first_hit_day(close_returns.ge(prev20_target_pct, axis=0))
        day_numbers = np.arange(1, h + 1)
        breakout_arr = breakout_day.to_numpy(dtype=float)[:, None]
        after_breakout = pd.DataFrame(
            np.isfinite(breakout_arr) & (day_numbers >= breakout_arr),
            index=valid.index,
            columns=close_cols,
        )
        profit_target_pct = float(candidate["profit_target_pct"])
        target_day = _first_hit_day(close_returns.ge(profit_target_pct) & after_breakout)
        close_prices = close_returns.div(100.0).add(1.0).mul(entry_price, axis=0)
        ma5_cols = [f"future_d{day}_ma5" for day in range(1, h + 1)]
        ma5_refs = valid[ma5_cols].apply(pd.to_numeric, errors="coerce")
        ma5_refs.columns = close_cols
        trail_day = _first_hit_day(close_prices.lt(ma5_refs) & after_breakout)
        target_return_at_hit = _value_at_day(open_exit_returns, target_day)
    else:
        raise ValueError(f"Unsupported exit target_rule_id: {target_rule_id}")

    same_day_unresolved = target_day.notna() & (
        (hard_stop_day.notna() & target_day.eq(hard_stop_day))
        | (trail_day.notna() & target_day.eq(trail_day))
    )
    target_before_stop = (
        target_day.notna()
        & ~same_day_unresolved
        & (hard_stop_day.isna() | (target_day < hard_stop_day))
        & (trail_day.isna() | (target_day < trail_day))
    )
    hard_stop_failure = (
        hard_stop_day.notna()
        & ~same_day_unresolved
        & (target_day.isna() | (hard_stop_day < target_day))
        & (trail_day.isna() | (hard_stop_day <= trail_day))
    )
    trail_exit = (
        trail_day.notna()
        & ~same_day_unresolved
        & (target_day.isna() | (trail_day < target_day))
        & (hard_stop_day.isna() | (trail_day < hard_stop_day))
    )

    realized_days = pd.Series(h, index=valid.index, dtype=float)
    realized_days = realized_days.mask(target_before_stop, target_day)
    realized_days = realized_days.mask(hard_stop_failure, hard_stop_day)
    realized_days = realized_days.mask(trail_exit, trail_day)
    realized_days = realized_days.mask(same_day_unresolved, target_day)

    trail_return = _value_at_day(open_exit_returns, trail_day)
    realized_return = pd.Series(math.nan, index=valid.index, dtype=float)
    realized_return = realized_return.mask(target_before_stop, target_return_at_hit)
    realized_return = realized_return.mask(hard_stop_failure, hard_stop_return)
    realized_return = realized_return.mask(trail_exit, trail_return)

    any_exit = target_before_stop | hard_stop_failure | trail_exit | same_day_unresolved
    no_exit = ~any_exit
    realized_return = realized_return.mask(no_exit, final_close_return)

    trail_neutral = trail_exit & realized_return.ge(0)
    trail_failure = trail_exit & realized_return.lt(0)
    late_neutral = no_exit & final_close_return.ge(0)
    late_failure = no_exit & final_close_return.lt(0)
    failure = hard_stop_failure | trail_failure | late_failure
    neutral = trail_neutral | late_neutral

    win_count = int(target_before_stop.sum())
    neutral_count = int(neutral.sum())
    failure_count = int(failure.sum())
    same_day_count = int(same_day_unresolved.sum())
    hard_stop_count = int(hard_stop_failure.sum())
    trail_exit_count = int(trail_exit.sum())
    mature = len(valid)
    return {
        "mature_count": mature,
        "win_count": win_count,
        "neutral_count": neutral_count,
        "failure_count": failure_count,
        "same_day_unresolved_count": same_day_count,
        "hard_stop_count": hard_stop_count,
        "ma5_exit_count": trail_exit_count,
        "win_rate_pct": _rate(win_count, mature),
        "neutral_rate_pct": _rate(neutral_count, mature),
        "failure_rate_pct": _rate(failure_count, mature),
        "same_day_unresolved_rate_pct": _rate(same_day_count, mature),
        "hard_stop_rate_pct": _rate(hard_stop_count, mature),
        "ma5_exit_rate_pct": _rate(trail_exit_count, mature),
        "avg_d20_close_return_pct": round(float(final_close_return.mean()), 2) if mature else "",
        "median_d20_close_return_pct": round(float(final_close_return.median()), 2) if mature else "",
        "avg_realized_return_pct": _mean_or_blank(realized_return),
        "avg_win_realized_return_pct": _mean_or_blank(realized_return[target_before_stop]) if mature else "",
        "avg_failure_realized_return_pct": _mean_or_blank(realized_return[failure]) if mature else "",
        "avg_neutral_realized_return_pct": _mean_or_blank(realized_return[neutral]) if mature else "",
        "avg_realized_or_d20_days": _mean_or_blank(realized_days),
        "avg_days_to_win": _mean_or_blank(target_day[target_before_stop]) if mature else "",
        "avg_days_to_failure": _mean_or_blank(realized_days[failure]) if mature else "",
    }


def _price_pullback_exit_rule_outcome_rows(valid: pd.DataFrame, candidate: dict[str, object]) -> pd.DataFrame:
    h = TIME_COST_HORIZON_DAYS
    close_cols = [f"next_open_to_d{day}_day_close_return_pct" for day in range(1, h + 1)]
    high_cols = [f"next_open_to_d{day}_day_high_return_pct" for day in range(1, h + 1)]
    final_close_col = f"next_open_to_d{h}_close_return_pct"
    close_returns = valid[close_cols].apply(pd.to_numeric, errors="coerce")
    final_close_return = pd.to_numeric(valid[final_close_col], errors="coerce")
    entry_price = numeric_column(valid, "next_open")
    target_price = numeric_column(valid, "range_high_20d_prev")
    prev20_target_pct = (target_price / entry_price.replace(0, pd.NA) - 1.0) * 100.0

    refs = _future_reference_frame(valid, h, "lower_ma20_ema23", close_cols)
    hard_stop_threshold = (refs.mul(0.96).div(entry_price.replace(0, pd.NA), axis=0) - 1.0) * 100.0
    hard_stop_day = _first_consecutive_hit_day(close_returns.le(hard_stop_threshold), 4)
    open_exit_returns = _future_open_return_frame(valid, h)
    hard_stop_return = _value_at_day(open_exit_returns, hard_stop_day)

    target_rule_id = str(candidate["target_rule_id"])
    trail_day = pd.Series(math.nan, index=valid.index, dtype=float)
    if target_rule_id == "intraday_prev20_high_touch":
        high_returns = valid[high_cols].apply(pd.to_numeric, errors="coerce")
        target_day = _first_hit_day(high_returns.ge(prev20_target_pct, axis=0))
        target_return_at_hit = _value_at_day(close_returns, target_day)
    elif target_rule_id == "close_prev20_high_break":
        target_day = _first_hit_day(close_returns.ge(prev20_target_pct, axis=0))
        target_return_at_hit = _value_at_day(open_exit_returns, target_day)
    elif target_rule_id == "close_prev20_break_then_close_profit_target":
        breakout_day = _first_hit_day(close_returns.ge(prev20_target_pct, axis=0))
        day_numbers = np.arange(1, h + 1)
        breakout_arr = breakout_day.to_numpy(dtype=float)[:, None]
        after_breakout = pd.DataFrame(
            np.isfinite(breakout_arr) & (day_numbers >= breakout_arr),
            index=valid.index,
            columns=close_cols,
        )
        profit_target_pct = float(candidate["profit_target_pct"])
        target_day = _first_hit_day(close_returns.ge(profit_target_pct) & after_breakout)
        close_prices = close_returns.div(100.0).add(1.0).mul(entry_price, axis=0)
        ma5_cols = [f"future_d{day}_ma5" for day in range(1, h + 1)]
        ma5_refs = valid[ma5_cols].apply(pd.to_numeric, errors="coerce")
        ma5_refs.columns = close_cols
        trail_day = _first_hit_day(close_prices.lt(ma5_refs) & after_breakout)
        target_return_at_hit = _value_at_day(open_exit_returns, target_day)
    else:
        raise ValueError(f"Unsupported exit target_rule_id: {target_rule_id}")

    same_day_unresolved = target_day.notna() & (
        (hard_stop_day.notna() & target_day.eq(hard_stop_day))
        | (trail_day.notna() & target_day.eq(trail_day))
    )
    target_before_stop = (
        target_day.notna()
        & ~same_day_unresolved
        & (hard_stop_day.isna() | (target_day < hard_stop_day))
        & (trail_day.isna() | (target_day < trail_day))
    )
    hard_stop_failure = (
        hard_stop_day.notna()
        & ~same_day_unresolved
        & (target_day.isna() | (hard_stop_day < target_day))
        & (trail_day.isna() | (hard_stop_day <= trail_day))
    )
    trail_exit = (
        trail_day.notna()
        & ~same_day_unresolved
        & (target_day.isna() | (trail_day < target_day))
        & (hard_stop_day.isna() | (trail_day < hard_stop_day))
    )

    realized_days = pd.Series(h, index=valid.index, dtype=float)
    realized_days = realized_days.mask(target_before_stop, target_day)
    realized_days = realized_days.mask(hard_stop_failure, hard_stop_day)
    realized_days = realized_days.mask(trail_exit, trail_day)
    realized_days = realized_days.mask(same_day_unresolved, target_day)

    trail_return = _value_at_day(open_exit_returns, trail_day)
    realized_return = pd.Series(math.nan, index=valid.index, dtype=float)
    realized_return = realized_return.mask(target_before_stop, target_return_at_hit)
    realized_return = realized_return.mask(hard_stop_failure, hard_stop_return)
    realized_return = realized_return.mask(trail_exit, trail_return)

    any_exit = target_before_stop | hard_stop_failure | trail_exit | same_day_unresolved
    no_exit = ~any_exit
    realized_return = realized_return.mask(no_exit, final_close_return)

    trail_neutral = trail_exit & realized_return.ge(0)
    trail_failure = trail_exit & realized_return.lt(0)
    late_neutral = no_exit & final_close_return.ge(0)
    late_failure = no_exit & final_close_return.lt(0)
    failure = hard_stop_failure | trail_failure | late_failure
    neutral = trail_neutral | late_neutral
    bucket = pd.Series("same_day_unresolved", index=valid.index, dtype=object)
    bucket = bucket.mask(target_before_stop, "win")
    bucket = bucket.mask(neutral, "neutral")
    bucket = bucket.mask(failure, "failure")

    return pd.DataFrame(
        {
            "outcome_bucket": bucket,
            "target_day": target_day,
            "hard_stop_day": hard_stop_day,
            "ma5_exit_day": trail_day,
            "realized_days": realized_days,
            "realized_return_pct": realized_return,
            "final_d20_close_return_pct": final_close_return,
            "prev20_target_return_pct": prev20_target_pct,
            "target_before_stop": target_before_stop,
            "hard_stop_failure": hard_stop_failure,
            "ma5_exit": trail_exit,
            "same_day_unresolved": same_day_unresolved,
        },
        index=valid.index,
    )


def build_price_pullback_exit_rule_comparison(df: pd.DataFrame) -> pd.DataFrame:
    base_mask = current_price_pullback_baseline_proxy(df).fillna(False)
    rows: list[dict[str, object]] = []
    generated_at = now_text()
    for entry_filter in _price_pullback_exit_rule_filters():
        condition = entry_filter.get("condition")
        if condition is None:
            continue
        filter_mask = condition(df).fillna(False)
        picked = df[base_mask & filter_mask].copy()
        for candidate in PRICE_PULLBACK_EXIT_RULE_COMPARISON_CANDIDATES:
            required = _price_pullback_exit_required_columns(candidate)
            valid = (
                picked.dropna(subset=required).copy()
                if all(col in picked.columns for col in required)
                else picked.iloc[0:0].copy()
            )
            outcome = (
                _price_pullback_exit_rule_outcome_counts(valid, candidate)
                if not valid.empty
                else {
                    **_blank_operation_outcome(),
                    "hard_stop_count": 0,
                    "ma5_exit_count": 0,
                    "hard_stop_rate_pct": "",
                    "ma5_exit_rate_pct": "",
                }
            )
            rows.append(
                {
                    "generated_at": generated_at,
                    "model_id": "price_pullback_23ema",
                    "model_name_zh": "股價回檔模型",
                    "research_artifact_id": "price_pullback_23ema_exit_rule_comparison",
                    "entry_filter_id": entry_filter["feature_filter_id"],
                    "entry_filter_family": entry_filter["feature_family"],
                    "entry_filter_rule": entry_filter["feature_rule"],
                    "exit_rule_id": candidate["exit_rule_id"],
                    "formal_price_rule_status": candidate["formal_price_rule_status"],
                    "target_rule_id": candidate["target_rule_id"],
                    "profit_target_pct": candidate["profit_target_pct"],
                    "exit_price_rule": candidate["exit_price_rule"],
                    "exit_rule_zh": candidate["exit_rule_zh"],
                    "entry_rule_id": "signal_date_next_open",
                    "buy_point_rule": "Buy next open only when the price_pullback_23ema signal and the entry filter both hold on signal date.",
                    "stop_rule_id": "sustained_close_below_lower_ma20_ema23_4pct_4d",
                    "stop_rule": "Failure stop when close stays at least 4% below the lower of current 20MA and 23EMA for 4 consecutive trading days; exit at the next trading day open after the confirming close.",
                    "holding_window_days": TIME_COST_HORIZON_DAYS,
                    "selected_stock_days": len(picked),
                    "selected_unique_stocks": picked["stock_id"].nunique() if not picked.empty else 0,
                    "advisory_status": "not_production_ready_research_only",
                    "approved_for_daily": False,
                    "promotion_readiness": "blocked_exact_daily_row_parity_and_operation_approval_required",
                    "promotion_blocker": "requires close-confirmed exact operation parity plus explicit promotion/sync PR before production use",
                    **outcome,
                }
            )
    return pd.DataFrame(rows)


def write_price_pullback_exit_rule_comparison(exit_comparison: pd.DataFrame) -> None:
    write_csv(exit_comparison, PRICE_PULLBACK_EXIT_RULE_COMPARISON_CSV)
    write_csv(exit_comparison, PRICE_PULLBACK_EXIT_RULE_COMPARISON_HISTORY_CSV)
    write_csv(exit_comparison, DOCS_PRICE_PULLBACK_EXIT_RULE_COMPARISON_CSV)
    lines = [
        "# Price Pullback 23EMA Exit Rule Comparison",
        "",
        f"- generated_at: `{now_text()}`",
        "- model_id: `price_pullback_23ema`",
        "- status: `not_production_ready_research_only`",
        "- scope: advisory exit-rule comparison only; this does not approve daily production use",
        "- entry_basis: `signal_date_next_open` after production proxy replay plus the entry filter under test",
        "- invalid_rule_excluded: `close_prev20_high_break_same_day_close` is excluded because the close break is known only after the close.",
        "- short_exit_rules: `intraday_prev20_high_touch_same_day_close` and `close_prev20_high_break_next_open`",
        "- continuation_exit_rules: after close-confirmed previous-20-day-high breakout, keep holding until +5%/+8%/+10% close target or close below 5MA, then exit next open.",
        "- hard_stop: close stays at least 4% below the lower of MA20 and EMA23 for 4 consecutive trading days; stop exit uses the next trading day open after the confirming close.",
        "- blocker: exact daily candidate row parity and explicit promotion/sync PR are still required before production use",
        "",
        markdown_table(
            exit_comparison,
            [
                "entry_filter_id",
                "exit_rule_id",
                "formal_price_rule_status",
                "profit_target_pct",
                "selected_stock_days",
                "mature_count",
                "win_rate_pct",
                "neutral_rate_pct",
                "failure_rate_pct",
                "same_day_unresolved_rate_pct",
                "hard_stop_rate_pct",
                "ma5_exit_rate_pct",
                "avg_realized_return_pct",
                "avg_win_realized_return_pct",
                "avg_failure_realized_return_pct",
                "avg_d20_close_return_pct",
                "avg_realized_or_d20_days",
                "promotion_readiness",
            ],
            limit=80,
        ),
    ]
    PRICE_PULLBACK_EXIT_RULE_COMPARISON_MD.write_text(
        "\n".join(lines).rstrip() + "\n",
        encoding="utf-8",
        newline="\n",
    )
    DOCS_PRICE_PULLBACK_EXIT_RULE_COMPARISON_MD.write_text(
        PRICE_PULLBACK_EXIT_RULE_COMPARISON_MD.read_text(encoding="utf-8"),
        encoding="utf-8",
        newline="\n",
    )


def _numeric_or_nan(value: object) -> float:
    parsed = pd.to_numeric(pd.Series([value]), errors="coerce").iloc[0]
    return float(parsed) if pd.notna(parsed) else math.nan


def _delta_or_blank(value: object, baseline: object) -> float | str:
    parsed = _numeric_or_nan(value)
    base = _numeric_or_nan(baseline)
    if math.isnan(parsed) or math.isnan(base):
        return ""
    return round(parsed - base, 2)


def _share_pct_or_blank(value: object, baseline: object) -> float | str:
    parsed = _numeric_or_nan(value)
    base = _numeric_or_nan(baseline)
    if math.isnan(parsed) or math.isnan(base) or base <= 0:
        return ""
    return round(parsed / base * 100.0, 2)


def _median_or_blank(series: pd.Series) -> float | str:
    clean = pd.to_numeric(series, errors="coerce").dropna()
    if clean.empty:
        return ""
    return round(float(clean.median()), 2)


def _bool_share_pct(series: pd.Series) -> float | str:
    if series.empty:
        return ""
    return _rate(int(trueish(series).sum()), len(series))


def _profile_delta(value: object, baseline: object) -> float | str:
    return _delta_or_blank(value, baseline)


def _profile_interpretation(delta: object, feature_type: str) -> str:
    parsed = _numeric_or_nan(delta)
    if math.isnan(parsed):
        return "insufficient_feature_coverage"
    threshold = 10.0 if feature_type == "boolean_share" else 1.0
    if parsed >= threshold:
        return "higher_in_success_rows"
    if parsed <= -threshold:
        return "lower_in_success_rows"
    return "similar_between_success_and_non_success"


def build_price_pullback_continuation_win_profile(df: pd.DataFrame) -> pd.DataFrame:
    base_mask = current_price_pullback_baseline_proxy(df).fillna(False)
    entry_filters = {
        str(entry_filter["feature_filter_id"]): entry_filter
        for entry_filter in _price_pullback_exit_rule_filters()
        if str(entry_filter["feature_filter_id"]) in PRICE_PULLBACK_CONTINUATION_PROFILE_ENTRY_FILTER_IDS
    }
    exit_candidates = {
        str(candidate["exit_rule_id"]): candidate
        for candidate in PRICE_PULLBACK_EXIT_RULE_COMPARISON_CANDIDATES
        if str(candidate["exit_rule_id"]) in PRICE_PULLBACK_CONTINUATION_PROFILE_EXIT_RULE_IDS
    }
    rows: list[dict[str, object]] = []
    generated_at = now_text()
    for entry_filter_id, entry_filter in entry_filters.items():
        condition = entry_filter.get("condition")
        if condition is None:
            continue
        filter_mask = condition(df).fillna(False)
        picked = df[base_mask & filter_mask].copy()
        for exit_rule_id, candidate in exit_candidates.items():
            required = _price_pullback_exit_required_columns(candidate)
            valid = (
                picked.dropna(subset=required).copy()
                if all(col in picked.columns for col in required)
                else picked.iloc[0:0].copy()
            )
            if valid.empty:
                continue
            outcome = _price_pullback_exit_rule_outcome_rows(valid, candidate)
            enriched = valid.join(outcome)
            wins = enriched[enriched["outcome_bucket"].eq("win")]
            non_wins = enriched[~enriched["outcome_bucket"].eq("win")]
            for feature_column, feature_family, feature_rule in PRICE_PULLBACK_SUCCESS_NUMERIC_FEATURES:
                if feature_column not in enriched.columns:
                    continue
                win_values = pd.to_numeric(wins[feature_column], errors="coerce").dropna()
                non_win_values = pd.to_numeric(non_wins[feature_column], errors="coerce").dropna()
                win_mean = _mean_or_blank(win_values)
                non_win_mean = _mean_or_blank(non_win_values)
                delta = _profile_delta(win_mean, non_win_mean)
                rows.append(
                    {
                        "generated_at": generated_at,
                        "model_id": "price_pullback_23ema",
                        "model_name_zh": "股價回檔模型",
                        "research_artifact_id": "price_pullback_23ema_continuation_win_profile",
                        "entry_filter_id": entry_filter_id,
                        "entry_filter_rule": entry_filter["feature_rule"],
                        "exit_rule_id": exit_rule_id,
                        "profit_target_pct": candidate["profit_target_pct"],
                        "feature_column": feature_column,
                        "feature_family": feature_family,
                        "feature_type": "numeric",
                        "feature_rule": feature_rule,
                        "win_count": len(wins),
                        "non_win_count": len(non_wins),
                        "win_feature_value_count": len(win_values),
                        "non_win_feature_value_count": len(non_win_values),
                        "win_mean": win_mean,
                        "non_win_mean": non_win_mean,
                        "delta_win_minus_non_win": delta,
                        "win_median": _median_or_blank(win_values),
                        "non_win_median": _median_or_blank(non_win_values),
                        "win_share_pct": "",
                        "non_win_share_pct": "",
                        "delta_share_pct": "",
                        "interpretation_status": _profile_interpretation(delta, "numeric"),
                        "data_status": "point_in_time_theme_context_coverage_limited"
                        if feature_family == "theme_context"
                        else "available_point_in_time_research_frame",
                        "advisory_status": "not_production_ready_research_only",
                        "approved_for_daily": False,
                        "production_change": "none",
                    }
                )
            for feature_column, feature_family, feature_rule in PRICE_PULLBACK_SUCCESS_BOOL_FEATURES:
                if feature_column not in enriched.columns:
                    continue
                win_share = _bool_share_pct(wins[feature_column])
                non_win_share = _bool_share_pct(non_wins[feature_column])
                delta = _profile_delta(win_share, non_win_share)
                rows.append(
                    {
                        "generated_at": generated_at,
                        "model_id": "price_pullback_23ema",
                        "model_name_zh": "股價回檔模型",
                        "research_artifact_id": "price_pullback_23ema_continuation_win_profile",
                        "entry_filter_id": entry_filter_id,
                        "entry_filter_rule": entry_filter["feature_rule"],
                        "exit_rule_id": exit_rule_id,
                        "profit_target_pct": candidate["profit_target_pct"],
                        "feature_column": feature_column,
                        "feature_family": feature_family,
                        "feature_type": "boolean_share",
                        "feature_rule": feature_rule,
                        "win_count": len(wins),
                        "non_win_count": len(non_wins),
                        "win_feature_value_count": len(wins),
                        "non_win_feature_value_count": len(non_wins),
                        "win_mean": "",
                        "non_win_mean": "",
                        "delta_win_minus_non_win": "",
                        "win_median": "",
                        "non_win_median": "",
                        "win_share_pct": win_share,
                        "non_win_share_pct": non_win_share,
                        "delta_share_pct": delta,
                        "interpretation_status": _profile_interpretation(delta, "boolean_share"),
                        "data_status": "point_in_time_theme_context_coverage_limited"
                        if feature_family == "theme_context"
                        else "available_point_in_time_research_frame",
                        "advisory_status": "not_production_ready_research_only",
                        "approved_for_daily": False,
                        "production_change": "none",
                    }
                )
    return pd.DataFrame(rows)


def write_price_pullback_continuation_win_profile(profile: pd.DataFrame) -> None:
    write_csv(profile, PRICE_PULLBACK_CONTINUATION_WIN_PROFILE_CSV)
    write_csv(profile, PRICE_PULLBACK_CONTINUATION_WIN_PROFILE_HISTORY_CSV)
    write_csv(profile, DOCS_PRICE_PULLBACK_CONTINUATION_WIN_PROFILE_CSV)
    top_positive = (
        profile[profile["interpretation_status"].eq("higher_in_success_rows")]
        .copy()
        .sort_values(["entry_filter_id", "exit_rule_id", "feature_family", "feature_column"])
        if not profile.empty and "interpretation_status" in profile.columns
        else pd.DataFrame()
    )
    lines = [
        "# Price Pullback 23EMA Continuation Win Profile",
        "",
        f"- generated_at: `{now_text()}`",
        "- model_id: `price_pullback_23ema`",
        "- status: `not_production_ready_research_only`",
        "- scope: row-level success-characteristics profile for continuation exit rules; this does not approve production use",
        "- entry_basis: production proxy replay plus selected entry filters",
        "- exit_basis: close-confirmed previous-20-day-high breakout, then hold until +5%/+8%/+10% close target or 5MA close exit, with next-open execution.",
        "- theme_context_rule: uses signal-date/as-of `daily_model_signal_background_feature_panel`; latest-only theme taxonomy is not used for historical labels.",
        "- blocker: exact operation parity and explicit promotion PR are still required before production use",
        "",
        "## Higher In Success Rows",
        "",
        markdown_table(
            top_positive,
            [
                "entry_filter_id",
                "exit_rule_id",
                "feature_column",
                "feature_family",
                "win_count",
                "non_win_count",
                "win_mean",
                "non_win_mean",
                "delta_win_minus_non_win",
                "win_share_pct",
                "non_win_share_pct",
                "delta_share_pct",
                "data_status",
            ],
            limit=80,
        )
        if not top_positive.empty
        else "No feature was materially higher in success rows.",
        "",
        "## Full Profile",
        "",
        markdown_table(
            profile,
            [
                "entry_filter_id",
                "exit_rule_id",
                "feature_column",
                "feature_family",
                "feature_type",
                "win_count",
                "non_win_count",
                "win_mean",
                "non_win_mean",
                "delta_win_minus_non_win",
                "win_share_pct",
                "non_win_share_pct",
                "delta_share_pct",
                "interpretation_status",
                "data_status",
            ],
            limit=120,
        )
        if not profile.empty
        else "No continuation profile rows.",
    ]
    PRICE_PULLBACK_CONTINUATION_WIN_PROFILE_MD.write_text(
        "\n".join(lines).rstrip() + "\n",
        encoding="utf-8",
        newline="\n",
    )
    DOCS_PRICE_PULLBACK_CONTINUATION_WIN_PROFILE_MD.write_text(
        PRICE_PULLBACK_CONTINUATION_WIN_PROFILE_MD.read_text(encoding="utf-8"),
        encoding="utf-8",
        newline="\n",
    )


def _score_bucket_label(score: float) -> str:
    if math.isnan(score):
        return "score_unknown"
    for low, high, label in PRICE_PULLBACK_RESEARCH_SCORE_BUCKETS:
        if low <= score <= high:
            return label
    return "score_unknown"


def add_price_pullback_research_score_columns(df: pd.DataFrame) -> pd.DataFrame:
    out = df.copy()
    total = pd.Series(0, index=out.index, dtype=float)
    active_ids: list[pd.Series] = []
    for component in PRICE_PULLBACK_RESEARCH_SCORE_COMPONENTS:
        component_id = safe_str(component["component_id"])
        condition = component["condition"](out).fillna(False)
        points = float(component["points"])
        out[f"score_component_{component_id}"] = condition
        total = total + condition.astype(float) * points
        active_ids.append(pd.Series(component_id, index=out.index).where(condition, ""))
    out["price_pullback_research_score"] = total
    if active_ids:
        active = pd.concat(active_ids, axis=1)
        out["price_pullback_research_score_components"] = active.apply(
            lambda row: ";".join([safe_str(value) for value in row if safe_str(value)]),
            axis=1,
        )
    else:
        out["price_pullback_research_score_components"] = ""
    out["price_pullback_research_score_bucket"] = total.map(_score_bucket_label)
    return out


def _score_component_summary(row: pd.Series) -> str:
    parts = []
    for component in PRICE_PULLBACK_RESEARCH_SCORE_COMPONENTS:
        component_id = safe_str(component["component_id"])
        col = f"component_hit_count_{component_id}"
        if col in row:
            parts.append(f"{component_id}:{int(row[col])}")
    return ";".join(parts)


def build_price_pullback_research_score_bucket(df: pd.DataFrame) -> pd.DataFrame:
    base_mask = current_price_pullback_baseline_proxy(df).fillna(False)
    scored = add_price_pullback_research_score_columns(df[base_mask].copy())
    exit_candidates = {
        str(candidate["exit_rule_id"]): candidate
        for candidate in PRICE_PULLBACK_EXIT_RULE_COMPARISON_CANDIDATES
        if str(candidate["exit_rule_id"]) in PRICE_PULLBACK_RESEARCH_SCORE_EXIT_RULE_IDS
    }
    rows: list[dict[str, object]] = []
    generated_at = now_text()
    for exit_rule_id, candidate in exit_candidates.items():
        required = _price_pullback_exit_required_columns(candidate)
        valid = (
            scored.dropna(subset=required).copy()
            if all(col in scored.columns for col in required)
            else scored.iloc[0:0].copy()
        )
        if valid.empty:
            continue
        outcome = _price_pullback_exit_rule_outcome_rows(valid, candidate)
        enriched = valid.join(outcome)
        for bucket_label, bucket in enriched.groupby("price_pullback_research_score_bucket", sort=True):
            if bucket.empty:
                continue
            wins = bucket["outcome_bucket"].eq("win")
            neutral = bucket["outcome_bucket"].eq("neutral")
            failure = bucket["outcome_bucket"].eq("failure")
            same_day = bucket["outcome_bucket"].eq("same_day_unresolved")
            row: dict[str, object] = {
                "generated_at": generated_at,
                "model_id": "price_pullback_23ema",
                "model_name_zh": "股價回檔模型",
                "research_artifact_id": "price_pullback_23ema_research_score_bucket",
                "score_draft_id": "research_bonus_score_v1",
                "score_bucket": bucket_label,
                "exit_rule_id": exit_rule_id,
                "formal_price_rule_status": candidate["formal_price_rule_status"],
                "profit_target_pct": candidate["profit_target_pct"],
                "exit_price_rule": candidate["exit_price_rule"],
                "entry_rule_id": "signal_date_next_open",
                "buy_point_rule": "Buy next open only after the price_pullback_23ema production proxy signal; score is advisory only.",
                "score_use": "research_only_not_production_score",
                "score_rule_summary": "TDCC high-thresholds up=2 points; return20_0_25, return45_ge5, range_width45_ge28, prior_extension_ema23_20d_ge8, prior_runup20_ge15, and OBV above MA20=1 point each.",
                "selected_stock_days": len(bucket),
                "selected_unique_stocks": bucket["stock_id"].nunique() if "stock_id" in bucket.columns else "",
                "mature_count": len(bucket),
                "win_count": int(wins.sum()),
                "neutral_count": int(neutral.sum()),
                "failure_count": int(failure.sum()),
                "same_day_unresolved_count": int(same_day.sum()),
                "win_rate_pct": _rate(int(wins.sum()), len(bucket)),
                "neutral_rate_pct": _rate(int(neutral.sum()), len(bucket)),
                "failure_rate_pct": _rate(int(failure.sum()), len(bucket)),
                "same_day_unresolved_rate_pct": _rate(int(same_day.sum()), len(bucket)),
                "avg_research_score": _mean_or_blank(bucket["price_pullback_research_score"]),
                "avg_realized_return_pct": _mean_or_blank(bucket["realized_return_pct"]),
                "median_realized_return_pct": _median_or_blank(bucket["realized_return_pct"]),
                "avg_win_realized_return_pct": _mean_or_blank(bucket.loc[wins, "realized_return_pct"]),
                "avg_failure_realized_return_pct": _mean_or_blank(bucket.loc[failure, "realized_return_pct"]),
                "avg_d20_close_return_pct": _mean_or_blank(bucket["final_d20_close_return_pct"]),
                "avg_realized_or_d20_days": _mean_or_blank(bucket["realized_days"]),
                "advisory_status": "not_production_ready_research_only",
                "approved_for_daily": False,
                "production_change": "none",
                "promotion_readiness": "blocked_exact_daily_row_parity_and_operation_approval_required",
                "promotion_blocker": "requires exact daily operation parity, explicit score promotion PR, contract update, validators, and post-merge validation before production scoring use",
            }
            for component in PRICE_PULLBACK_RESEARCH_SCORE_COMPONENTS:
                component_id = safe_str(component["component_id"])
                col = f"score_component_{component_id}"
                row[f"component_hit_count_{component_id}"] = int(trueish(bucket[col]).sum()) if col in bucket.columns else 0
                row[f"component_hit_rate_pct_{component_id}"] = (
                    _bool_share_pct(bucket[col]) if col in bucket.columns else ""
                )
            row["component_hit_summary"] = _score_component_summary(pd.Series(row))
            rows.append(row)
    out = pd.DataFrame(rows)
    if out.empty:
        return out
    bucket_order = {label: idx for idx, (_, _, label) in enumerate(PRICE_PULLBACK_RESEARCH_SCORE_BUCKETS)}
    out["_bucket_order"] = out["score_bucket"].map(bucket_order).fillna(99)
    out = out.sort_values(["exit_rule_id", "_bucket_order"]).drop(columns=["_bucket_order"]).reset_index(drop=True)
    return out


def write_price_pullback_research_score_bucket(score_bucket: pd.DataFrame) -> None:
    write_csv(score_bucket, PRICE_PULLBACK_RESEARCH_SCORE_BUCKET_CSV)
    write_csv(score_bucket, PRICE_PULLBACK_RESEARCH_SCORE_BUCKET_HISTORY_CSV)
    write_csv(score_bucket, DOCS_PRICE_PULLBACK_RESEARCH_SCORE_BUCKET_CSV)
    lines = [
        "# Price Pullback 23EMA Research Score Bucket",
        "",
        f"- generated_at: `{now_text()}`",
        "- model_id: `price_pullback_23ema`",
        "- status: `not_production_ready_research_only`",
        "- scope: advisory score-bucket backtest for discussing add-score items; this does not approve production scoring.",
        "- score_draft_id: `research_bonus_score_v1`",
        "- score_rule: TDCC high-thresholds up=2 points; return20_0_25, return45_ge5, range_width45_ge28, prior_extension_ema23_20d_ge8, prior_runup20_ge15, and OBV above MA20=1 point each.",
        "- theme_context_status: not included in the score yet because D+20 mature outcome is not available.",
        "- promotion_blocker: production scoring requires explicit promotion PR, contract update, exact parity, validators, and post-merge validation.",
        "",
        markdown_table(
            score_bucket,
            [
                "score_bucket",
                "exit_rule_id",
                "profit_target_pct",
                "mature_count",
                "win_rate_pct",
                "neutral_rate_pct",
                "failure_rate_pct",
                "same_day_unresolved_rate_pct",
                "avg_realized_return_pct",
                "median_realized_return_pct",
                "avg_win_realized_return_pct",
                "avg_failure_realized_return_pct",
                "avg_d20_close_return_pct",
                "avg_realized_or_d20_days",
                "component_hit_summary",
            ],
            limit=80,
        )
        if not score_bucket.empty
        else "No score bucket rows.",
    ]
    PRICE_PULLBACK_RESEARCH_SCORE_BUCKET_MD.write_text(
        "\n".join(lines).rstrip() + "\n",
        encoding="utf-8",
        newline="\n",
    )
    DOCS_PRICE_PULLBACK_RESEARCH_SCORE_BUCKET_MD.write_text(
        PRICE_PULLBACK_RESEARCH_SCORE_BUCKET_MD.read_text(encoding="utf-8"),
        encoding="utf-8",
        newline="\n",
    )


def price_pullback_research_score_ge_filter(d: pd.DataFrame, min_score: float) -> pd.Series:
    scored = d if "price_pullback_research_score" in d.columns else add_price_pullback_research_score_columns(d)
    return numeric_column(scored, "price_pullback_research_score").ge(min_score).fillna(False)


def price_pullback_prev20_high_space_pct(d: pd.DataFrame) -> pd.Series:
    entry_price = numeric_column(d, "next_open").replace(0, pd.NA)
    target_price = numeric_column(d, "range_high_20d_prev")
    space_pct = (target_price / entry_price - 1.0) * 100.0
    return pd.to_numeric(space_pct, errors="coerce")


def price_pullback_prev20_high_space_filter(d: pd.DataFrame, min_space_pct: float) -> pd.Series:
    return price_pullback_prev20_high_space_pct(d).ge(min_space_pct).fillna(False)


def _high_return_feature_score_bucket_label(score: float) -> str:
    if math.isnan(score):
        return "score_unknown"
    if score < 0:
        return "score_below_0"
    return f"score_{int(score)}"


def add_price_pullback_high_return_feature_score_columns(df: pd.DataFrame) -> pd.DataFrame:
    out = df.copy()
    total = pd.Series(0, index=out.index, dtype=float)
    active_ids: list[pd.Series] = []
    risk_ids: list[pd.Series] = []
    for component in PRICE_PULLBACK_HIGH_RETURN_FEATURE_SCORE_COMPONENTS:
        component_id = safe_str(component["component_id"])
        condition = component["condition"](out).fillna(False)
        points = float(component["points"])
        col = f"high_return_score_component_{component_id}"
        out[col] = condition
        total = total + condition.astype(float) * points
        active_ids.append(pd.Series(component_id, index=out.index).where(condition, ""))
        if points < 0:
            risk_ids.append(pd.Series(component_id, index=out.index).where(condition, ""))

    out["price_pullback_high_return_feature_score"] = total
    if active_ids:
        active = pd.concat(active_ids, axis=1)
        out["price_pullback_high_return_feature_score_components"] = active.apply(
            lambda row: ";".join([safe_str(value) for value in row if safe_str(value)]),
            axis=1,
        )
    else:
        out["price_pullback_high_return_feature_score_components"] = ""
    if risk_ids:
        risks = pd.concat(risk_ids, axis=1)
        out["price_pullback_high_return_feature_risk_tags"] = risks.apply(
            lambda row: ";".join([safe_str(value) for value in row if safe_str(value)]),
            axis=1,
        )
    else:
        out["price_pullback_high_return_feature_risk_tags"] = ""
    out["price_pullback_high_return_feature_score_bucket"] = total.map(_high_return_feature_score_bucket_label)
    return out


def _price_pullback_high_return_score_component_summary(row: pd.Series) -> str:
    parts = []
    for component in PRICE_PULLBACK_HIGH_RETURN_FEATURE_SCORE_COMPONENTS:
        component_id = safe_str(component["component_id"])
        col = f"component_hit_count_{component_id}"
        if col in row:
            parts.append(f"{component_id}:{int(row[col])}")
    return ";".join(parts)


def _price_pullback_v1_base_research_filter(d: pd.DataFrame) -> pd.Series:
    return (
        current_price_pullback_baseline_proxy(d)
        & price_pullback_return20_balanced_filter(d)
        & price_pullback_tdcc_high_thresholds_up_filter(d)
        & price_pullback_obv_above_ma20_filter(d)
    ).fillna(False)


def _price_pullback_known_data_quality_exception_mask(d: pd.DataFrame) -> pd.Series:
    if d.empty:
        return bool_series(d, False)
    if "stock_id" in d.columns:
        stock = d["stock_id"].map(safe_str)
    else:
        stock = pd.Series("", index=d.index, dtype=object)
    if "_price_pullback_signal_date" in d.columns:
        signal_date = d["_price_pullback_signal_date"].map(safe_str)
    elif "date" in d.columns:
        signal_date = d["date"].map(normalize_date)
    else:
        signal_date = pd.Series("", index=d.index, dtype=object)
    mask = bool_series(d, False)
    for exception in PRICE_PULLBACK_KNOWN_DATA_QUALITY_EXCEPTIONS:
        mask = mask | (
            stock.eq(safe_str(exception["stock_id"]))
            & signal_date.eq(safe_str(exception["signal_date"]))
        )
    return mask.fillna(False)


def _price_pullback_known_data_quality_exception_ids(d: pd.DataFrame) -> list[str]:
    if d.empty:
        return []
    if "stock_id" in d.columns:
        stock = d["stock_id"].map(safe_str)
    else:
        stock = pd.Series("", index=d.index, dtype=object)
    if "_price_pullback_signal_date" in d.columns:
        signal_date = d["_price_pullback_signal_date"].map(safe_str)
    elif "date" in d.columns:
        signal_date = d["date"].map(normalize_date)
    else:
        signal_date = pd.Series("", index=d.index, dtype=object)
    ids: list[str] = []
    for exception in PRICE_PULLBACK_KNOWN_DATA_QUALITY_EXCEPTIONS:
        matched = (
            stock.eq(safe_str(exception["stock_id"]))
            & signal_date.eq(safe_str(exception["signal_date"]))
        )
        if bool(matched.fillna(False).any()):
            ids.append(safe_str(exception["exception_id"]))
    return sorted(set(ids))


def _price_pullback_high_return_score_bucket_specs(score: pd.Series) -> list[dict[str, object]]:
    score_numeric = pd.to_numeric(score, errors="coerce").dropna()
    if score_numeric.empty:
        return []
    low = int(math.floor(float(score_numeric.min())))
    high = int(math.ceil(float(score_numeric.max())))
    specs: list[dict[str, object]] = [
        {
            "score_bucket_type": "baseline",
            "score_bucket": "all_scores",
            "score_threshold": "",
            "score_sort_value": -999,
            "condition": lambda d: bool_series(d, True),
        }
    ]
    for exact_score in range(low, high + 1):
        specs.append(
            {
                "score_bucket_type": "exact_score",
                "score_bucket": f"score_{exact_score}" if exact_score >= 0 else "score_below_0",
                "score_threshold": "",
                "score_sort_value": exact_score,
                "condition": lambda d, exact_score=exact_score: pd.to_numeric(
                    d["price_pullback_high_return_feature_score"],
                    errors="coerce",
                ).eq(float(exact_score)),
            }
        )
    for threshold in range(max(0, low), high + 1):
        specs.append(
            {
                "score_bucket_type": "score_threshold",
                "score_bucket": f"score_ge_{threshold}",
                "score_threshold": threshold,
                "score_sort_value": threshold,
                "condition": lambda d, threshold=threshold: pd.to_numeric(
                    d["price_pullback_high_return_feature_score"],
                    errors="coerce",
                ).ge(float(threshold)),
            }
        )
    return specs


def _price_pullback_high_return_score_grid_metrics(accepted: pd.DataFrame) -> dict[str, object]:
    outcome = _price_pullback_ordered_outcome_summary(accepted)
    if accepted.empty:
        return {
            **outcome,
            "median_realized_return_pct": "",
            "high_return_8_count": 0,
            "high_return_8_rate_pct": "",
            "high_return_10_count": 0,
            "high_return_10_rate_pct": "",
            "loss_5_count": 0,
            "loss_5_rate_pct": "",
            "avg_high_return_feature_score": "",
            "median_high_return_feature_score": "",
            "avg_prev20_target_return_pct": "",
            "median_prev20_target_return_pct": "",
        }
    realized = pd.to_numeric(accepted["realized_return_pct"], errors="coerce")
    score = pd.to_numeric(accepted["price_pullback_high_return_feature_score"], errors="coerce")
    high8 = realized.ge(8.0)
    high10 = realized.ge(10.0)
    loss5 = realized.le(-5.0)
    metrics = {
        **outcome,
        "median_realized_return_pct": _median_or_blank(realized),
        "high_return_8_count": int(high8.sum()),
        "high_return_8_rate_pct": _rate(int(high8.sum()), len(accepted)),
        "high_return_10_count": int(high10.sum()),
        "high_return_10_rate_pct": _rate(int(high10.sum()), len(accepted)),
        "loss_5_count": int(loss5.sum()),
        "loss_5_rate_pct": _rate(int(loss5.sum()), len(accepted)),
        "avg_high_return_feature_score": _mean_or_blank(score),
        "median_high_return_feature_score": _median_or_blank(score),
        "avg_prev20_target_return_pct": _mean_or_blank(accepted["prev20_target_return_pct"]),
        "median_prev20_target_return_pct": _median_or_blank(accepted["prev20_target_return_pct"]),
    }
    for component in PRICE_PULLBACK_HIGH_RETURN_FEATURE_SCORE_COMPONENTS:
        component_id = safe_str(component["component_id"])
        col = f"high_return_score_component_{component_id}"
        hit_count = int(trueish(accepted[col]).sum()) if col in accepted.columns else 0
        metrics[f"component_hit_count_{component_id}"] = hit_count
        metrics[f"component_hit_rate_pct_{component_id}"] = _rate(hit_count, len(accepted))
    metrics["component_hit_summary"] = _price_pullback_high_return_score_component_summary(pd.Series(metrics))
    return metrics


def build_price_pullback_high_return_feature_score_grid(df: pd.DataFrame) -> pd.DataFrame:
    positioned = _price_pullback_positioned_frame(_price_pullback_lifecycle_input_frame(df))
    research_dates = positioned["_price_pullback_signal_date"].map(safe_str)
    research_trading_day_count = int(research_dates[research_dates.ne("")].nunique())
    base_mask = _price_pullback_v1_base_research_filter(positioned)
    base = add_price_pullback_high_return_feature_score_columns(positioned[base_mask].copy())
    exit_candidates = {
        str(candidate["exit_rule_id"]): candidate
        for candidate in PRICE_PULLBACK_EXIT_RULE_COMPARISON_CANDIDATES
        if str(candidate["exit_rule_id"]) in PRICE_PULLBACK_RESEARCH_SCORE_EXIT_RULE_IDS
    }
    rows: list[dict[str, object]] = []
    generated_at = now_text()
    lifecycle_key_cols = [
        "stock_id",
        "_price_pullback_signal_date",
        "_price_pullback_stock_day_position",
        "_price_pullback_source_row_index",
    ]
    score_context_cols = [
        "price_pullback_high_return_feature_score",
        "price_pullback_high_return_feature_score_components",
        "price_pullback_high_return_feature_risk_tags",
        "price_pullback_high_return_feature_score_bucket",
    ]
    score_context_cols.extend(
        f"high_return_score_component_{safe_str(component['component_id'])}"
        for component in PRICE_PULLBACK_HIGH_RETURN_FEATURE_SCORE_COMPONENTS
    )

    for exit_rule_id, candidate in exit_candidates.items():
        required = _price_pullback_exit_required_columns(candidate)
        valid_base = (
            base.dropna(subset=required).copy()
            if all(col in base.columns for col in required)
            else base.iloc[0:0].copy()
        )
        if valid_base.empty:
            continue
        outcome = _price_pullback_exit_rule_outcome_rows(valid_base, candidate)
        enriched_base = valid_base[lifecycle_key_cols + score_context_cols].join(outcome)
        lifecycle_all = _price_pullback_apply_lifecycle_suppression(enriched_base)
        score_specs = _price_pullback_high_return_score_bucket_specs(
            lifecycle_all["price_pullback_high_return_feature_score"]
        )
        if not score_specs:
            continue

        for anomaly_basis in [
            "including_data_quality_exceptions",
            "excluding_known_data_quality_exceptions",
        ]:
            exception_mask_all = _price_pullback_known_data_quality_exception_mask(lifecycle_all)
            if anomaly_basis == "excluding_known_data_quality_exceptions":
                basis_lifecycle = lifecycle_all[~exception_mask_all].copy()
                baseline_exception_count = int(exception_mask_all.sum())
            else:
                basis_lifecycle = lifecycle_all.copy()
                baseline_exception_count = int(exception_mask_all.sum())
            basis_accepted = basis_lifecycle[trueish(basis_lifecycle["lifecycle_accepted_trade"])]
            baseline_accepted_trade_count = len(basis_accepted)
            baseline_source_mature_count = len(basis_lifecycle)

            for spec in score_specs:
                bucket_mask_all = spec["condition"](lifecycle_all).fillna(False)
                bucket_lifecycle_raw = lifecycle_all[bucket_mask_all].copy()
                bucket_exception_mask = _price_pullback_known_data_quality_exception_mask(bucket_lifecycle_raw)
                excluded_exception_count = int(bucket_exception_mask.sum())
                if anomaly_basis == "excluding_known_data_quality_exceptions":
                    bucket_lifecycle = bucket_lifecycle_raw[~bucket_exception_mask].copy()
                else:
                    bucket_lifecycle = bucket_lifecycle_raw
                accepted = bucket_lifecycle[trueish(bucket_lifecycle["lifecycle_accepted_trade"])]
                if accepted.empty and bucket_lifecycle.empty:
                    continue
                accepted_date_stats = _price_pullback_date_stats(accepted)
                source_date_stats = _price_pullback_date_stats(bucket_lifecycle)
                suppressed_count = (
                    int(trueish(bucket_lifecycle["lifecycle_suppressed_signal"]).sum())
                    if not bucket_lifecycle.empty
                    else 0
                )
                row = {
                    "generated_at": generated_at,
                    "model_id": "price_pullback_23ema",
                    "model_name_zh": "股價回檔模型",
                    "research_artifact_id": "price_pullback_23ema_high_return_feature_score_grid",
                    "score_draft_id": "research_high_return_feature_score_v1",
                    "base_condition_id": "v1_gate_return20_tdcc_high_obv",
                    "base_condition_rule": "production proxy signal plus return20_0_25, TDCC high thresholds up, and OBV above MA20",
                    "score_bucket_type": spec["score_bucket_type"],
                    "score_bucket": spec["score_bucket"],
                    "score_threshold": spec["score_threshold"],
                    "_score_sort": spec["score_sort_value"],
                    "score_rule_summary": (
                        "+2 prev20 target space >=8%; +1 prev20 target space 5%-<8%; "
                        "+1 prior 20d runup >=20%; +1 prior 20d high extension above 23EMA >=10%; "
                        "+1 weak prior 45d return >=8%; -1/risk for volume red K >=1.2 or solid red candle."
                    ),
                    "anomaly_exclusion_basis": anomaly_basis,
                    "known_data_quality_exception_count_in_bucket": excluded_exception_count,
                    "known_data_quality_exception_count_in_baseline": baseline_exception_count,
                    "known_data_quality_exception_ids": ";".join(
                        safe_str(exception["exception_id"])
                        for exception in PRICE_PULLBACK_KNOWN_DATA_QUALITY_EXCEPTIONS
                    ),
                    "exit_rule_id": exit_rule_id,
                    "formal_price_rule_status": candidate["formal_price_rule_status"],
                    "profit_target_pct": candidate["profit_target_pct"],
                    "exit_price_rule": candidate["exit_price_rule"],
                    "entry_rule_id": "signal_date_next_open",
                    "lifecycle_replay_scope": "trade_level_same_stock_active_position_suppressed",
                    "source_mature_signal_stock_days": len(bucket_lifecycle),
                    "source_unique_stocks": (
                        bucket_lifecycle["stock_id"].nunique() if "stock_id" in bucket_lifecycle.columns else ""
                    ),
                    "suppressed_signal_count": suppressed_count,
                    "suppressed_rate_pct": _rate(suppressed_count, len(bucket_lifecycle)),
                    "accepted_trade_count": len(accepted),
                    "accepted_unique_stocks": accepted["stock_id"].nunique() if "stock_id" in accepted.columns else "",
                    "baseline_source_mature_signal_stock_days": baseline_source_mature_count,
                    "baseline_accepted_trade_count": baseline_accepted_trade_count,
                    "accepted_trade_share_of_baseline_pct": _rate(len(accepted), baseline_accepted_trade_count),
                    "source_signal_day_count": source_date_stats["signal_day_count"],
                    "source_avg_signals_per_signal_day": source_date_stats["avg_rows_per_signal_day"],
                    "accepted_signal_day_count": accepted_date_stats["signal_day_count"],
                    "accepted_avg_trades_per_signal_day": accepted_date_stats["avg_rows_per_signal_day"],
                    "research_trading_day_count": research_trading_day_count,
                    "accepted_avg_trades_per_research_day": (
                        round(len(accepted) / research_trading_day_count, 2)
                        if research_trading_day_count
                        else ""
                    ),
                    "first_signal_date": source_date_stats["first_signal_date"],
                    "last_signal_date": source_date_stats["last_signal_date"],
                    "score_use": "research_only_not_production_score",
                    "metric_surface_use": "model_lane_research_metric_source_candidate_not_pdf_ready",
                    "pdf_metric_readiness": "blocked_until_formal_promotion_and_operation_adapter_contract",
                    "advisory_status": "not_production_ready_research_only",
                    "approved_for_daily": False,
                    "production_change": "none",
                    "promotion_readiness": "blocked_explicit_score_decision_exact_parity_operation_adapter_and_metric_contract_required",
                    "promotion_blocker": (
                        "requires explicit score threshold decision, high/low-return feature review, "
                        "model contract update if promoted, exact parity, validators, PR merge, "
                        "post-merge main validation, and PDF metric consumer contract before display"
                    ),
                    **_price_pullback_high_return_score_grid_metrics(accepted),
                }
                rows.append(row)

    out = pd.DataFrame(rows)
    if out.empty:
        return out
    bucket_type_order = {"baseline": 0, "exact_score": 1, "score_threshold": 2}
    anomaly_order = {
        "including_data_quality_exceptions": 0,
        "excluding_known_data_quality_exceptions": 1,
    }
    out["_bucket_type_order"] = out["score_bucket_type"].map(bucket_type_order).fillna(99)
    out["_anomaly_order"] = out["anomaly_exclusion_basis"].map(anomaly_order).fillna(99)
    out["_threshold_sort"] = pd.to_numeric(out["score_threshold"], errors="coerce").fillna(-99)
    out["_score_sort"] = pd.to_numeric(out["_score_sort"], errors="coerce").fillna(99)
    return (
        out.sort_values(
            [
                "exit_rule_id",
                "_anomaly_order",
                "_bucket_type_order",
                "_score_sort",
            ],
            kind="mergesort",
        )
        .drop(columns=["_bucket_type_order", "_anomaly_order", "_threshold_sort", "_score_sort"])
        .reset_index(drop=True)
    )


def write_price_pullback_high_return_feature_score_grid(score_grid: pd.DataFrame) -> None:
    write_csv(score_grid, PRICE_PULLBACK_HIGH_RETURN_SCORE_GRID_CSV)
    write_csv(score_grid, PRICE_PULLBACK_HIGH_RETURN_SCORE_GRID_HISTORY_CSV)
    write_csv(score_grid, DOCS_PRICE_PULLBACK_HIGH_RETURN_SCORE_GRID_CSV)
    lines = [
        "# Price Pullback 23EMA High-Return Feature Score Grid",
        "",
        f"- generated_at: `{now_text()}`",
        "- model_id: `price_pullback_23ema`",
        "- status: `not_production_ready_research_only`",
        "- scope: score grid for the current research base `v1_gate_return20_tdcc_high_obv`; this does not approve production scoring.",
        "- lifecycle_scope: same-stock active-position suppression is applied before scoring buckets are evaluated.",
        "- anomaly_basis: metrics are emitted both including and excluding known data-quality exceptions.",
        "- score_draft_id: `research_high_return_feature_score_v1`",
        "- score_rule: +2 prev20 target space >=8%; +1 prev20 target space 5%-<8%; +1 prior 20d runup >=20%; +1 prior 20d high extension above 23EMA >=10%; +1 weak prior 45d return >=8%; -1/risk for volume red K >=1.2 or solid red candle.",
        "- production_change: `none`",
        "- promotion_blocker: production use requires explicit threshold decision, contract/parity/validator updates, merge, post-merge main validation, and PDF metric consumer contract.",
        "",
        markdown_table(
            score_grid,
            [
                "anomaly_exclusion_basis",
                "score_bucket_type",
                "score_bucket",
                "exit_rule_id",
                "accepted_trade_count",
                "accepted_unique_stocks",
                "accepted_avg_trades_per_research_day",
                "win_rate_pct",
                "neutral_rate_pct",
                "failure_rate_pct",
                "avg_realized_return_pct",
                "median_realized_return_pct",
                "high_return_8_rate_pct",
                "high_return_10_rate_pct",
                "loss_5_rate_pct",
                "avg_prev20_target_return_pct",
                "component_hit_summary",
            ],
            limit=160,
        )
        if not score_grid.empty
        else "No high-return feature score grid rows.",
    ]
    PRICE_PULLBACK_HIGH_RETURN_SCORE_GRID_MD.write_text(
        "\n".join(lines).rstrip() + "\n",
        encoding="utf-8",
        newline="\n",
    )
    DOCS_PRICE_PULLBACK_HIGH_RETURN_SCORE_GRID_MD.write_text(
        PRICE_PULLBACK_HIGH_RETURN_SCORE_GRID_MD.read_text(encoding="utf-8"),
        encoding="utf-8",
        newline="\n",
    )


PRICE_PULLBACK_REVENUE_CONDITION_TESTS = [
    {
        "test_order": 0,
        "condition_test_id": "base_v1_without_revenue_gate",
        "condition_family": "baseline",
        "condition_role_candidate": "baseline_anchor",
        "condition_rule": "price_pullback_23ema production proxy plus return20_0_25, TDCC high thresholds up, and OBV above MA20; no revenue gate",
        "data_status": "available_full_market_monthly_revenue_history_join_not_required",
        "condition": lambda d: bool_series(d, True),
    },
    {
        "test_order": 10,
        "condition_test_id": "revenue_context_ready",
        "condition_family": "revenue_coverage",
        "condition_role_candidate": "coverage_gate_review",
        "condition_rule": "canonical monthly revenue history has an as-of row where source_table_date <= signal_date",
        "data_status": "joined_from_full_market_monthly_revenue_history_research_only",
        "condition": full_monthly_revenue_context_ready_filter,
    },
    {
        "test_order": 20,
        "condition_test_id": "revenue_positive",
        "condition_family": "revenue_direction",
        "condition_role_candidate": "add_score_candidate",
        "condition_rule": "latest or cumulative monthly revenue YoY is positive",
        "data_status": "joined_from_full_market_monthly_revenue_history_research_only",
        "condition": full_monthly_revenue_positive_filter,
    },
    {
        "test_order": 30,
        "condition_test_id": "revenue_production_strong",
        "condition_family": "revenue_strength",
        "condition_role_candidate": "required_gate_candidate",
        "condition_rule": "latest revenue YoY >= 30% or cumulative revenue YoY >= 20%",
        "data_status": "joined_from_full_market_monthly_revenue_history_research_only",
        "condition": full_monthly_revenue_strong_filter,
    },
    {
        "test_order": 40,
        "condition_test_id": "latest_revenue_yoy_ge50",
        "condition_family": "revenue_strength",
        "condition_role_candidate": "strong_add_score_candidate",
        "condition_rule": "latest monthly revenue YoY >= 50%",
        "data_status": "joined_from_full_market_monthly_revenue_history_research_only",
        "condition": lambda d: full_monthly_revenue_latest_yoy_ge_filter(d, 50.0),
    },
    {
        "test_order": 50,
        "condition_test_id": "cumulative_revenue_yoy_ge30",
        "condition_family": "revenue_strength",
        "condition_role_candidate": "strong_add_score_candidate",
        "condition_rule": "cumulative monthly revenue YoY >= 30%",
        "data_status": "joined_from_full_market_monthly_revenue_history_research_only",
        "condition": lambda d: full_monthly_revenue_cumulative_yoy_ge_filter(d, 30.0),
    },
    {
        "test_order": 60,
        "condition_test_id": "latest30_and_cumulative20",
        "condition_family": "revenue_strength_combo",
        "condition_role_candidate": "condition_package_candidate",
        "condition_rule": "latest monthly revenue YoY >= 30% and cumulative revenue YoY >= 20%",
        "data_status": "joined_from_full_market_monthly_revenue_history_research_only",
        "condition": full_monthly_revenue_both_latest30_cumulative20_filter,
    },
    {
        "test_order": 70,
        "condition_test_id": "latest_yoy_improving_2m",
        "condition_family": "revenue_turnaround",
        "condition_role_candidate": "turnaround_add_score_candidate",
        "condition_rule": "latest monthly revenue YoY improves for two consecutive available months",
        "data_status": "joined_from_full_market_monthly_revenue_history_research_only",
        "condition": full_monthly_revenue_latest_yoy_improving_2m_filter,
    },
    {
        "test_order": 80,
        "condition_test_id": "latest_yoy_improving_3m",
        "condition_family": "revenue_turnaround",
        "condition_role_candidate": "turnaround_add_score_candidate",
        "condition_rule": "latest monthly revenue YoY improves for three consecutive available months",
        "data_status": "joined_from_full_market_monthly_revenue_history_research_only",
        "condition": full_monthly_revenue_latest_yoy_improving_3m_filter,
    },
    {
        "test_order": 90,
        "condition_test_id": "cumulative_yoy_improving_2m",
        "condition_family": "revenue_turnaround",
        "condition_role_candidate": "turnaround_add_score_candidate",
        "condition_rule": "cumulative monthly revenue YoY improves for two consecutive available months",
        "data_status": "joined_from_full_market_monthly_revenue_history_research_only",
        "condition": full_monthly_revenue_cumulative_yoy_improving_2m_filter,
    },
    {
        "test_order": 100,
        "condition_test_id": "latest_yoy_turn_positive",
        "condition_family": "revenue_turnaround",
        "condition_role_candidate": "turnaround_add_score_candidate",
        "condition_rule": "latest monthly revenue YoY turns from negative in the previous available month to positive",
        "data_status": "joined_from_full_market_monthly_revenue_history_research_only",
        "condition": full_monthly_revenue_latest_yoy_turn_positive_filter,
    },
    {
        "test_order": 110,
        "condition_test_id": "latest_yoy_turn_positive_after_2_negative",
        "condition_family": "revenue_turnaround",
        "condition_role_candidate": "turnaround_add_score_candidate",
        "condition_rule": "latest monthly revenue YoY turns positive after two negative available months",
        "data_status": "joined_from_full_market_monthly_revenue_history_research_only",
        "condition": full_monthly_revenue_latest_yoy_turn_positive_after_2_negative_filter,
    },
    {
        "test_order": 120,
        "condition_test_id": "cumulative_yoy_turn_positive",
        "condition_family": "revenue_turnaround",
        "condition_role_candidate": "turnaround_add_score_candidate",
        "condition_rule": "cumulative monthly revenue YoY turns from negative in the previous available month to positive",
        "data_status": "joined_from_full_market_monthly_revenue_history_research_only",
        "condition": full_monthly_revenue_cumulative_yoy_turn_positive_filter,
    },
    {
        "test_order": 130,
        "condition_test_id": "latest_yoy_delta_ge20",
        "condition_family": "revenue_turnaround",
        "condition_role_candidate": "turnaround_add_score_candidate",
        "condition_rule": "latest monthly revenue YoY improves by at least 20 percentage points from the previous available month",
        "data_status": "joined_from_full_market_monthly_revenue_history_research_only",
        "condition": lambda d: full_monthly_revenue_latest_yoy_delta_ge_filter(d, 20.0),
    },
    {
        "test_order": 140,
        "condition_test_id": "turn_positive_and_cumulative_improving",
        "condition_family": "revenue_turnaround_combo",
        "condition_role_candidate": "condition_package_candidate",
        "condition_rule": "latest monthly revenue YoY turns positive and cumulative monthly revenue YoY improves",
        "data_status": "joined_from_full_market_monthly_revenue_history_research_only",
        "condition": full_monthly_revenue_turn_positive_and_cumulative_improving_filter,
    },
    {
        "test_order": 150,
        "condition_test_id": "latest_improving_2m_and_cumulative_improving",
        "condition_family": "revenue_turnaround_combo",
        "condition_role_candidate": "condition_package_candidate",
        "condition_rule": "latest monthly revenue YoY improves for two consecutive available months and cumulative monthly revenue YoY improves",
        "data_status": "joined_from_full_market_monthly_revenue_history_research_only",
        "condition": full_monthly_revenue_latest_improving_and_cumulative_improving_filter,
    },
    {
        "test_order": 190,
        "condition_test_id": "revenue_negative_both_risk",
        "condition_family": "revenue_risk",
        "condition_role_candidate": "deduct_score_or_risk_tag_candidate",
        "condition_rule": "latest and cumulative monthly revenue YoY are both negative",
        "data_status": "joined_from_full_market_monthly_revenue_history_research_only",
        "condition": full_monthly_revenue_negative_both_filter,
    },
]


REVENUE_UNREACTED_REVENUE_CONDITION_TESTS = [
    {
        "test_order": 0,
        "condition_test_id": "price_range_no_attack_without_revenue_gate",
        "condition_family": "baseline",
        "condition_role_candidate": "baseline_price_proxy_anchor",
        "condition_rule": "price remains inside the recent 23-day range and active attack has not started; no revenue gate",
        "data_status": "price_proxy_available_revenue_gate_not_applied",
        "condition": lambda d: bool_series(d, True),
    },
    {
        "test_order": 10,
        "condition_test_id": "revenue_context_ready",
        "condition_family": "revenue_coverage",
        "condition_role_candidate": "coverage_gate_review",
        "condition_rule": "canonical monthly revenue history has an as-of row where source_table_date <= signal_date",
        "data_status": "joined_from_full_market_monthly_revenue_history_research_only",
        "condition": full_monthly_revenue_context_ready_filter,
    },
    {
        "test_order": 20,
        "condition_test_id": "revenue_production_strong",
        "condition_family": "revenue_strength",
        "condition_role_candidate": "production_semantic_gate_candidate",
        "condition_rule": "latest revenue YoY >= 30% or cumulative revenue YoY >= 20%",
        "data_status": "joined_from_full_market_monthly_revenue_history_research_only",
        "condition": full_monthly_revenue_strong_filter,
    },
    {
        "test_order": 30,
        "condition_test_id": "latest_revenue_yoy_ge50",
        "condition_family": "revenue_strength",
        "condition_role_candidate": "stronger_revenue_gate_candidate",
        "condition_rule": "latest monthly revenue YoY >= 50%",
        "data_status": "joined_from_full_market_monthly_revenue_history_research_only",
        "condition": lambda d: full_monthly_revenue_latest_yoy_ge_filter(d, 50.0),
    },
    {
        "test_order": 40,
        "condition_test_id": "latest_revenue_yoy_ge100",
        "condition_family": "revenue_strength",
        "condition_role_candidate": "stronger_revenue_gate_candidate",
        "condition_rule": "latest monthly revenue YoY >= 100%",
        "data_status": "joined_from_full_market_monthly_revenue_history_research_only",
        "condition": lambda d: full_monthly_revenue_latest_yoy_ge_filter(d, 100.0),
    },
    {
        "test_order": 50,
        "condition_test_id": "cumulative_revenue_yoy_ge30",
        "condition_family": "revenue_strength",
        "condition_role_candidate": "stronger_revenue_gate_candidate",
        "condition_rule": "cumulative monthly revenue YoY >= 30%",
        "data_status": "joined_from_full_market_monthly_revenue_history_research_only",
        "condition": lambda d: full_monthly_revenue_cumulative_yoy_ge_filter(d, 30.0),
    },
    {
        "test_order": 60,
        "condition_test_id": "latest30_and_cumulative20",
        "condition_family": "revenue_strength_combo",
        "condition_role_candidate": "condition_package_candidate",
        "condition_rule": "latest monthly revenue YoY >= 30% and cumulative revenue YoY >= 20%",
        "data_status": "joined_from_full_market_monthly_revenue_history_research_only",
        "condition": full_monthly_revenue_both_latest30_cumulative20_filter,
    },
]


def _revenue_latest50_cumulative30_filter(d: pd.DataFrame) -> pd.Series:
    return (
        full_monthly_revenue_context_ready_filter(d)
        & numeric_column(d, "full_monthly_revenue_latest_yoy_pct").ge(50.0)
        & numeric_column(d, "full_monthly_revenue_cumulative_yoy_pct").ge(30.0)
    ).fillna(False)


def _revenue_strong_range_width_filter(d: pd.DataFrame, max_width_pct: float) -> pd.Series:
    return (
        full_monthly_revenue_strong_filter(d)
        & numeric_column(d, "range_width_23d_pct").le(max_width_pct)
    ).fillna(False)


def _revenue_strong_near_range_high_filter(d: pd.DataFrame) -> pd.Series:
    return (
        full_monthly_revenue_strong_filter(d)
        & numeric_column(d, "distance_to_range_high_23d_pct").ge(-5.0)
        & numeric_column(d, "distance_to_range_high_23d_pct").le(5.0)
    ).fillna(False)


def _revenue_strong_low_mid_position_filter(d: pd.DataFrame) -> pd.Series:
    return (
        full_monthly_revenue_strong_filter(d)
        & numeric_column(d, "close_position_120d_pct").ge(0.0)
        & numeric_column(d, "close_position_120d_pct").le(75.0)
    ).fillna(False)


def _revenue_strong_ma20_ema23_support_filter(d: pd.DataFrame) -> pd.Series:
    return (
        full_monthly_revenue_strong_filter(d)
        & trueish_column(d, "close_above_ma20")
        & trueish_column(d, "close_above_ema23")
    ).fillna(False)


def _revenue_strong_tdcc_high_thresholds_up_filter(d: pd.DataFrame) -> pd.Series:
    return (
        full_monthly_revenue_strong_filter(d)
        & trueish_column(d, "high_thresholds_up")
    ).fillna(False)


REVENUE_UNREACTED_OPERATION_CONDITION_TESTS = [
    {
        "test_order": 0,
        "condition_test_id": "revenue_context_ready",
        "condition_family": "baseline",
        "condition_role_candidate": "baseline_revenue_context_anchor",
        "condition_rule": "price remains inside the recent 23-day range; monthly revenue PIT context is ready",
        "condition": full_monthly_revenue_context_ready_filter,
    },
    {
        "test_order": 10,
        "condition_test_id": "revenue_production_strong",
        "condition_family": "revenue_strength",
        "condition_role_candidate": "required_gate_candidate",
        "condition_rule": "latest monthly revenue YoY >= 30% or cumulative monthly revenue YoY >= 20%",
        "condition": full_monthly_revenue_strong_filter,
    },
    {
        "test_order": 20,
        "condition_test_id": "latest30_and_cumulative20",
        "condition_family": "revenue_strength_combo",
        "condition_role_candidate": "condition_package_candidate",
        "condition_rule": "latest monthly revenue YoY >= 30% and cumulative monthly revenue YoY >= 20%",
        "condition": full_monthly_revenue_both_latest30_cumulative20_filter,
    },
    {
        "test_order": 30,
        "condition_test_id": "latest50_and_cumulative30",
        "condition_family": "revenue_strength_combo",
        "condition_role_candidate": "stronger_condition_package_candidate",
        "condition_rule": "latest monthly revenue YoY >= 50% and cumulative monthly revenue YoY >= 30%",
        "condition": _revenue_latest50_cumulative30_filter,
    },
    {
        "test_order": 40,
        "condition_test_id": "strong_revenue_range23_width_le20",
        "condition_family": "price_unreacted_shape",
        "condition_role_candidate": "range_tightness_candidate",
        "condition_rule": "strong monthly revenue and 23-day range width <= 20%",
        "condition": lambda d: _revenue_strong_range_width_filter(d, 20.0),
    },
    {
        "test_order": 50,
        "condition_test_id": "strong_revenue_range23_width_le15",
        "condition_family": "price_unreacted_shape",
        "condition_role_candidate": "range_tightness_candidate",
        "condition_rule": "strong monthly revenue and 23-day range width <= 15%",
        "condition": lambda d: _revenue_strong_range_width_filter(d, 15.0),
    },
    {
        "test_order": 60,
        "condition_test_id": "strong_revenue_range23_width_le10",
        "condition_family": "price_unreacted_shape",
        "condition_role_candidate": "range_tightness_candidate",
        "condition_rule": "strong monthly revenue and 23-day range width <= 10%",
        "condition": lambda d: _revenue_strong_range_width_filter(d, 10.0),
    },
    {
        "test_order": 70,
        "condition_test_id": "strong_revenue_near_range23_high",
        "condition_family": "price_unreacted_shape",
        "condition_role_candidate": "near_breakout_candidate",
        "condition_rule": "strong monthly revenue and close is within -5% to +5% of the previous 23-day range high",
        "condition": _revenue_strong_near_range_high_filter,
    },
    {
        "test_order": 80,
        "condition_test_id": "strong_revenue_position120_le75",
        "condition_family": "position_filter",
        "condition_role_candidate": "avoid_high_position_candidate",
        "condition_rule": "strong monthly revenue and close is not above 75% of the previous 120-day range",
        "condition": _revenue_strong_low_mid_position_filter,
    },
    {
        "test_order": 90,
        "condition_test_id": "strong_revenue_above_ma20_ema23",
        "condition_family": "technical_support",
        "condition_role_candidate": "add_score_or_gate_candidate",
        "condition_rule": "strong monthly revenue and close is above both MA20 and EMA23",
        "condition": _revenue_strong_ma20_ema23_support_filter,
    },
    {
        "test_order": 100,
        "condition_test_id": "strong_revenue_tdcc_high_thresholds_up",
        "condition_family": "tdcc_confluence",
        "condition_role_candidate": "add_score_candidate",
        "condition_rule": "strong monthly revenue and TDCC high thresholds are increasing",
        "condition": _revenue_strong_tdcc_high_thresholds_up_filter,
    },
    {
        "test_order": 110,
        "condition_test_id": "latest_yoy_improving_2m",
        "condition_family": "monthly_revenue_improvement",
        "condition_role_candidate": "turnaround_add_score_candidate",
        "condition_rule": "latest monthly revenue YoY improves for two consecutive available months",
        "condition": full_monthly_revenue_latest_yoy_improving_2m_filter,
    },
    {
        "test_order": 120,
        "condition_test_id": "cumulative_yoy_improving_2m",
        "condition_family": "monthly_revenue_improvement",
        "condition_role_candidate": "turnaround_add_score_candidate",
        "condition_rule": "cumulative monthly revenue YoY improves for two consecutive available months",
        "condition": full_monthly_revenue_cumulative_yoy_improving_2m_filter,
    },
    {
        "test_order": 130,
        "condition_test_id": "turn_positive_and_cumulative_improving",
        "condition_family": "monthly_revenue_improvement_combo",
        "condition_role_candidate": "condition_package_candidate",
        "condition_rule": "latest monthly revenue YoY turns positive and cumulative monthly revenue YoY improves",
        "condition": full_monthly_revenue_turn_positive_and_cumulative_improving_filter,
    },
]


REVENUE_UNREACTED_OPERATION_EXIT_SPECS = [
    {
        "exit_order": 10,
        "exit_rule_id": "d10_close_no_stop",
        "holding_window_days": 10,
        "stop_rule_id": "no_stop",
        "exit_rule": "D+10 close-only fixed exit",
        "stop_rule": "no stop in this research row",
    },
    {
        "exit_order": 20,
        "exit_rule_id": "d15_close_no_stop",
        "holding_window_days": 15,
        "stop_rule_id": "no_stop",
        "exit_rule": "D+15 close-only fixed exit",
        "stop_rule": "no stop in this research row",
    },
    {
        "exit_order": 30,
        "exit_rule_id": "d20_close_no_stop",
        "holding_window_days": 20,
        "stop_rule_id": "no_stop",
        "exit_rule": "D+20 close-only fixed exit",
        "stop_rule": "no stop in this research row",
    },
    {
        "exit_order": 40,
        "exit_rule_id": "d10_close_ma20_ema23_4d_stop",
        "holding_window_days": 10,
        "stop_rule_id": "close_below_lower_ma20_ema23_4pct_4d_next_open",
        "exit_rule": "D+10 close-only fixed exit unless close-confirmed stop triggers first",
        "stop_rule": "four consecutive closes below the lower of MA20 and EMA23 by 4%, then next trading day open stop",
    },
    {
        "exit_order": 50,
        "exit_rule_id": "d15_close_ma20_ema23_4d_stop",
        "holding_window_days": 15,
        "stop_rule_id": "close_below_lower_ma20_ema23_4pct_4d_next_open",
        "exit_rule": "D+15 close-only fixed exit unless close-confirmed stop triggers first",
        "stop_rule": "four consecutive closes below the lower of MA20 and EMA23 by 4%, then next trading day open stop",
    },
    {
        "exit_order": 60,
        "exit_rule_id": "d20_close_ma20_ema23_4d_stop",
        "holding_window_days": 20,
        "stop_rule_id": "close_below_lower_ma20_ema23_4pct_4d_next_open",
        "exit_rule": "D+20 close-only fixed exit unless close-confirmed stop triggers first",
        "stop_rule": "four consecutive closes below the lower of MA20 and EMA23 by 4%, then next trading day open stop",
    },
]


def _full_monthly_revenue_anomaly_mask(d: pd.DataFrame, *, include_price_exception: bool = False) -> pd.Series:
    mask = trueish_column(d, "full_monthly_revenue_numerical_anomaly_flag")
    if include_price_exception:
        mask = mask | _price_pullback_known_data_quality_exception_mask(d)
    return mask.fillna(False)


def _price_pullback_revenue_condition_metrics(accepted: pd.DataFrame) -> dict[str, object]:
    outcome = _price_pullback_ordered_outcome_summary(accepted)
    if accepted.empty:
        return {
            **outcome,
            "median_realized_return_pct": "",
            "high_return_8_count": 0,
            "high_return_8_rate_pct": "",
            "high_return_10_count": 0,
            "high_return_10_rate_pct": "",
            "loss_5_count": 0,
            "loss_5_rate_pct": "",
            "avg_revenue_latest_yoy_pct": "",
            "median_revenue_latest_yoy_pct": "",
            "avg_revenue_cumulative_yoy_pct": "",
            "median_revenue_cumulative_yoy_pct": "",
            "avg_revenue_latest_yoy_delta_1m_pct_points": "",
            "median_revenue_latest_yoy_delta_1m_pct_points": "",
            "avg_revenue_cumulative_yoy_delta_1m_pct_points": "",
            "median_revenue_cumulative_yoy_delta_1m_pct_points": "",
        }
    realized = pd.to_numeric(accepted["realized_return_pct"], errors="coerce")
    high8 = realized.ge(8.0)
    high10 = realized.ge(10.0)
    loss5 = realized.le(-5.0)
    latest = numeric_column(accepted, "full_monthly_revenue_latest_yoy_pct")
    cumulative = numeric_column(accepted, "full_monthly_revenue_cumulative_yoy_pct")
    latest_delta = numeric_column(accepted, "full_monthly_revenue_latest_yoy_delta_1m_pct_points")
    cumulative_delta = numeric_column(accepted, "full_monthly_revenue_cumulative_yoy_delta_1m_pct_points")
    return {
        **outcome,
        "median_realized_return_pct": _median_or_blank(realized),
        "high_return_8_count": int(high8.sum()),
        "high_return_8_rate_pct": _rate(int(high8.sum()), len(accepted)),
        "high_return_10_count": int(high10.sum()),
        "high_return_10_rate_pct": _rate(int(high10.sum()), len(accepted)),
        "loss_5_count": int(loss5.sum()),
        "loss_5_rate_pct": _rate(int(loss5.sum()), len(accepted)),
        "avg_revenue_latest_yoy_pct": _mean_or_blank(latest),
        "median_revenue_latest_yoy_pct": _median_or_blank(latest),
        "avg_revenue_cumulative_yoy_pct": _mean_or_blank(cumulative),
        "median_revenue_cumulative_yoy_pct": _median_or_blank(cumulative),
        "avg_revenue_latest_yoy_delta_1m_pct_points": _mean_or_blank(latest_delta),
        "median_revenue_latest_yoy_delta_1m_pct_points": _median_or_blank(latest_delta),
        "avg_revenue_cumulative_yoy_delta_1m_pct_points": _mean_or_blank(cumulative_delta),
        "median_revenue_cumulative_yoy_delta_1m_pct_points": _median_or_blank(cumulative_delta),
    }


def build_price_pullback_revenue_condition_matrix(df: pd.DataFrame) -> pd.DataFrame:
    positioned = _price_pullback_positioned_frame(df)
    research_dates = positioned["_price_pullback_signal_date"].map(safe_str)
    research_trading_day_count = int(research_dates[research_dates.ne("")].nunique())
    base_mask = _price_pullback_v1_base_research_filter(positioned)
    base = positioned[base_mask].copy()
    candidate = next(
        candidate
        for candidate in PRICE_PULLBACK_EXIT_RULE_COMPARISON_CANDIDATES
        if str(candidate["exit_rule_id"]) == "close_prev20_high_break_next_open"
    )
    required = _price_pullback_exit_required_columns(candidate)
    valid_base = base.dropna(subset=required).copy() if all(col in base.columns for col in required) else base.iloc[0:0].copy()
    outcome = _price_pullback_exit_rule_outcome_rows(valid_base, candidate) if not valid_base.empty else pd.DataFrame(index=valid_base.index)
    lifecycle_key_cols = [
        "stock_id",
        "_price_pullback_signal_date",
        "_price_pullback_stock_day_position",
        "_price_pullback_source_row_index",
    ]
    context_cols = [col for col in FULL_MONTHLY_REVENUE_CONTEXT_COLUMNS if col in valid_base.columns]
    enriched_base = valid_base[lifecycle_key_cols + context_cols].join(outcome)
    rows: list[dict[str, object]] = []
    generated_at = now_text()
    for anomaly_basis in [
        "including_numerical_anomalies",
        "excluding_known_price_or_revenue_anomalies",
    ]:
        baseline_exception_mask = _full_monthly_revenue_anomaly_mask(
            enriched_base,
            include_price_exception=True,
        )
        if anomaly_basis == "excluding_known_price_or_revenue_anomalies":
            basis_base = enriched_base[~baseline_exception_mask].copy()
        else:
            basis_base = enriched_base.copy()
        baseline_lifecycle = _price_pullback_apply_lifecycle_suppression(basis_base)
        baseline_accepted = baseline_lifecycle[trueish(baseline_lifecycle["lifecycle_accepted_trade"])]
        baseline_accepted_trade_count = len(baseline_accepted)
        baseline_source_mature_count = len(basis_base)
        for spec in PRICE_PULLBACK_REVENUE_CONDITION_TESTS:
            condition_mask = spec["condition"](valid_base).fillna(False)
            picked_raw = enriched_base.loc[valid_base.index[condition_mask]].copy()
            sample_exception_mask = _full_monthly_revenue_anomaly_mask(
                picked_raw,
                include_price_exception=True,
            )
            if anomaly_basis == "excluding_known_price_or_revenue_anomalies":
                picked = picked_raw[~sample_exception_mask].copy()
            else:
                picked = picked_raw
            lifecycle = _price_pullback_apply_lifecycle_suppression(picked)
            accepted = lifecycle[trueish(lifecycle["lifecycle_accepted_trade"])]
            source_date_stats = _price_pullback_date_stats(picked)
            accepted_date_stats = _price_pullback_date_stats(accepted)
            suppressed_count = int(trueish(lifecycle["lifecycle_suppressed_signal"]).sum()) if not lifecycle.empty else 0
            rows.append(
                {
                    "generated_at": generated_at,
                    "model_id": "price_pullback_23ema",
                    "model_name_zh": "股價回檔模型",
                    "research_artifact_id": "price_pullback_23ema_revenue_condition_matrix",
                    "matrix_scope": "model_specific_revenue_condition_research",
                    "base_condition_id": "v1_gate_return20_tdcc_high_obv",
                    "base_condition_rule": "production proxy signal plus return20_0_25, TDCC high thresholds up, and OBV above MA20",
                    "test_order": spec["test_order"],
                    "condition_test_id": spec["condition_test_id"],
                    "condition_family": spec["condition_family"],
                    "condition_role_candidate": spec["condition_role_candidate"],
                    "condition_rule": spec["condition_rule"],
                    "data_status": spec["data_status"],
                    "revenue_join_source": FULL_MONTHLY_REVENUE_HISTORY_CSV.as_posix(),
                    "point_in_time_rule": "monthly revenue source_table_date must be <= signal_date",
                    "anomaly_exclusion_basis": anomaly_basis,
                    "revenue_or_price_anomaly_count_in_sample": int(sample_exception_mask.sum()),
                    "revenue_or_price_anomaly_count_in_baseline": int(baseline_exception_mask.sum()),
                    "exit_rule_id": candidate["exit_rule_id"],
                    "formal_price_rule_status": candidate["formal_price_rule_status"],
                    "profit_target_pct": candidate["profit_target_pct"],
                    "exit_price_rule": candidate["exit_price_rule"],
                    "entry_rule_id": "signal_date_next_open",
                    "operation_basis": "price_pullback_close_confirmed_candidate_lifecycle_replay",
                    "lifecycle_replay_scope": "trade_level_same_stock_active_position_suppressed_after_condition",
                    "source_mature_signal_stock_days": len(picked),
                    "source_unique_stocks": picked["stock_id"].nunique() if "stock_id" in picked.columns else "",
                    "accepted_trade_count": len(accepted),
                    "accepted_unique_stocks": accepted["stock_id"].nunique() if "stock_id" in accepted.columns else "",
                    "suppressed_signal_count": suppressed_count,
                    "suppressed_rate_pct": _rate(suppressed_count, len(picked)),
                    "accepted_share_of_source_mature_pct": _rate(len(accepted), len(picked)),
                    "baseline_source_mature_signal_stock_days": baseline_source_mature_count,
                    "baseline_accepted_trade_count": baseline_accepted_trade_count,
                    "accepted_trade_share_of_baseline_pct": _rate(len(accepted), baseline_accepted_trade_count),
                    "source_signal_day_count": source_date_stats["signal_day_count"],
                    "source_avg_signals_per_signal_day": source_date_stats["avg_rows_per_signal_day"],
                    "accepted_signal_day_count": accepted_date_stats["signal_day_count"],
                    "accepted_avg_trades_per_signal_day": accepted_date_stats["avg_rows_per_signal_day"],
                    "research_trading_day_count": research_trading_day_count,
                    "accepted_avg_trades_per_research_day": (
                        round(len(accepted) / research_trading_day_count, 2)
                        if research_trading_day_count
                        else ""
                    ),
                    "first_signal_date": source_date_stats["first_signal_date"],
                    "last_signal_date": source_date_stats["last_signal_date"],
                    "metric_surface_use": "model_lane_research_metric_source_candidate_not_pdf_ready",
                    "advisory_status": "not_production_ready_research_only",
                    "approved_for_daily": False,
                    "production_change": "none",
                    "promotion_readiness": "blocked_model_specific_promotion_pr_required",
                    "promotion_blocker": (
                        "revenue condition cannot enter price_pullback_23ema production until explicit "
                        "model-rule decision, contract/parity/validator updates, PR merge, and post-merge main validation"
                    ),
                    **_price_pullback_revenue_condition_metrics(accepted),
                }
            )
    out = pd.DataFrame(rows)
    if out.empty:
        return out
    return out.sort_values(["anomaly_exclusion_basis", "test_order"]).reset_index(drop=True)


def _fixed_d20_close_metrics(frame: pd.DataFrame) -> dict[str, object]:
    if frame.empty or "next_open_to_d20_close_return_pct" not in frame.columns:
        return {
            "mature_count": 0,
            "win_count": 0,
            "neutral_count": 0,
            "failure_count": 0,
            "win_rate_pct": "",
            "neutral_rate_pct": "",
            "failure_rate_pct": "",
            "avg_d20_close_return_pct": "",
            "median_d20_close_return_pct": "",
            "avg_realized_return_pct": "",
            "median_realized_return_pct": "",
            "high_return_8_count": 0,
            "high_return_8_rate_pct": "",
            "high_return_10_count": 0,
            "high_return_10_rate_pct": "",
            "loss_5_count": 0,
            "loss_5_rate_pct": "",
            "avg_revenue_latest_yoy_pct": "",
            "median_revenue_latest_yoy_pct": "",
            "avg_revenue_cumulative_yoy_pct": "",
            "median_revenue_cumulative_yoy_pct": "",
        }
    ret = pd.to_numeric(frame["next_open_to_d20_close_return_pct"], errors="coerce")
    valid = frame[ret.notna()].copy()
    realized = pd.to_numeric(valid["next_open_to_d20_close_return_pct"], errors="coerce")
    wins = realized.ge(5.0)
    neutral = realized.ge(0.0) & realized.lt(5.0)
    failure = realized.lt(0.0)
    high8 = realized.ge(8.0)
    high10 = realized.ge(10.0)
    loss5 = realized.le(-5.0)
    latest = numeric_column(valid, "full_monthly_revenue_latest_yoy_pct")
    cumulative = numeric_column(valid, "full_monthly_revenue_cumulative_yoy_pct")
    mature = len(valid)
    return {
        "mature_count": mature,
        "win_count": int(wins.sum()),
        "neutral_count": int(neutral.sum()),
        "failure_count": int(failure.sum()),
        "win_rate_pct": _rate(int(wins.sum()), mature),
        "neutral_rate_pct": _rate(int(neutral.sum()), mature),
        "failure_rate_pct": _rate(int(failure.sum()), mature),
        "avg_d20_close_return_pct": _mean_or_blank(realized),
        "median_d20_close_return_pct": _median_or_blank(realized),
        "avg_realized_return_pct": _mean_or_blank(realized),
        "median_realized_return_pct": _median_or_blank(realized),
        "high_return_8_count": int(high8.sum()),
        "high_return_8_rate_pct": _rate(int(high8.sum()), mature),
        "high_return_10_count": int(high10.sum()),
        "high_return_10_rate_pct": _rate(int(high10.sum()), mature),
        "loss_5_count": int(loss5.sum()),
        "loss_5_rate_pct": _rate(int(loss5.sum()), mature),
        "avg_revenue_latest_yoy_pct": _mean_or_blank(latest),
        "median_revenue_latest_yoy_pct": _median_or_blank(latest),
        "avg_revenue_cumulative_yoy_pct": _mean_or_blank(cumulative),
        "median_revenue_cumulative_yoy_pct": _median_or_blank(cumulative),
    }


def build_revenue_unreacted_range_revenue_condition_matrix(df: pd.DataFrame) -> pd.DataFrame:
    positioned = _price_pullback_positioned_frame(df)
    research_dates = positioned["_price_pullback_signal_date"].map(safe_str)
    research_trading_day_count = int(research_dates[research_dates.ne("")].nunique())
    base = positioned[current_revenue_unreacted_baseline_proxy(positioned).fillna(False)].copy()
    rows: list[dict[str, object]] = []
    generated_at = now_text()
    for anomaly_basis in ["including_numerical_anomalies", "excluding_revenue_numerical_anomalies"]:
        baseline_exception_mask = _full_monthly_revenue_anomaly_mask(base)
        basis_base = base[~baseline_exception_mask].copy() if anomaly_basis.startswith("excluding") else base.copy()
        baseline_mature_count = int(_fixed_d20_close_metrics(basis_base)["mature_count"])
        for spec in REVENUE_UNREACTED_REVENUE_CONDITION_TESTS:
            condition_mask = spec["condition"](base).fillna(False)
            picked_raw = base[condition_mask].copy()
            sample_exception_mask = _full_monthly_revenue_anomaly_mask(picked_raw)
            picked = picked_raw[~sample_exception_mask].copy() if anomaly_basis.startswith("excluding") else picked_raw
            source_date_stats = _price_pullback_date_stats(picked)
            metrics = _fixed_d20_close_metrics(picked)
            mature_count = int(metrics["mature_count"])
            rows.append(
                {
                    "generated_at": generated_at,
                    "model_id": "revenue_unreacted_range",
                    "model_name_zh": "營收爆發但股價尚未反應模型",
                    "research_artifact_id": "revenue_unreacted_range_revenue_condition_matrix",
                    "matrix_scope": "model_specific_revenue_condition_research",
                    "base_condition_id": "price_range_no_attack_proxy",
                    "base_condition_rule": "price remains inside the recent 23-day range and active attack has not started",
                    "test_order": spec["test_order"],
                    "condition_test_id": spec["condition_test_id"],
                    "condition_family": spec["condition_family"],
                    "condition_role_candidate": spec["condition_role_candidate"],
                    "condition_rule": spec["condition_rule"],
                    "data_status": spec["data_status"],
                    "revenue_join_source": FULL_MONTHLY_REVENUE_HISTORY_CSV.as_posix(),
                    "point_in_time_rule": "monthly revenue source_table_date must be <= signal_date",
                    "anomaly_exclusion_basis": anomaly_basis,
                    "revenue_anomaly_count_in_sample": int(sample_exception_mask.sum()),
                    "revenue_anomaly_count_in_baseline": int(baseline_exception_mask.sum()),
                    "exit_rule_id": "d20_close_advisory",
                    "formal_price_rule_status": "research_only_no_formal_operation_contract",
                    "profit_target_pct": 5.0,
                    "exit_price_rule": "D+20 close-only advisory outcome",
                    "entry_rule_id": "signal_date_next_open",
                    "operation_basis": "research_only_d20_close_not_operation_contract",
                    "lifecycle_replay_scope": "none_no_formal_operation_adapter",
                    "source_mature_signal_stock_days": len(picked),
                    "source_unique_stocks": picked["stock_id"].nunique() if "stock_id" in picked.columns else "",
                    "accepted_trade_count": mature_count,
                    "accepted_unique_stocks": picked["stock_id"].nunique() if mature_count and "stock_id" in picked.columns else "",
                    "suppressed_signal_count": 0,
                    "suppressed_rate_pct": 0.0 if len(picked) else "",
                    "accepted_share_of_source_mature_pct": _rate(mature_count, len(picked)),
                    "baseline_source_mature_signal_stock_days": len(basis_base),
                    "baseline_accepted_trade_count": baseline_mature_count,
                    "accepted_trade_share_of_baseline_pct": _rate(mature_count, baseline_mature_count),
                    "source_signal_day_count": source_date_stats["signal_day_count"],
                    "source_avg_signals_per_signal_day": source_date_stats["avg_rows_per_signal_day"],
                    "accepted_signal_day_count": source_date_stats["signal_day_count"],
                    "accepted_avg_trades_per_signal_day": source_date_stats["avg_rows_per_signal_day"],
                    "research_trading_day_count": research_trading_day_count,
                    "accepted_avg_trades_per_research_day": (
                        round(mature_count / research_trading_day_count, 2)
                        if research_trading_day_count
                        else ""
                    ),
                    "first_signal_date": source_date_stats["first_signal_date"],
                    "last_signal_date": source_date_stats["last_signal_date"],
                    "metric_surface_use": "model_lane_research_metric_source_candidate_not_pdf_ready",
                    "advisory_status": "not_production_ready_research_only",
                    "approved_for_daily": False,
                    "production_change": "none",
                    "promotion_readiness": "blocked_operation_rule_and_model_specific_promotion_pr_required",
                    "promotion_blocker": (
                        "revenue_unreacted_range still needs explicit buy/sell/stop/outcome contract, "
                        "contract/parity/validator updates, PR merge, and post-merge main validation before "
                        "a revenue gate or PDF metric can be formal"
                    ),
                    **metrics,
                }
            )
    out = pd.DataFrame(rows)
    if out.empty:
        return out
    return out.sort_values(["anomaly_exclusion_basis", "test_order"]).reset_index(drop=True)


def _write_revenue_condition_matrix(
    matrix: pd.DataFrame,
    *,
    title: str,
    csv_path: Path,
    md_path: Path,
    history_path: Path,
    docs_csv_path: Path,
    docs_md_path: Path,
) -> None:
    write_csv(matrix, csv_path)
    write_csv(matrix, history_path)
    write_csv(matrix, docs_csv_path)
    lines = [
        f"# {title}",
        "",
        f"- generated_at: `{now_text()}`",
        "- status: `not_production_ready_research_only`",
        "- production_change: `none`",
        "- revenue_join_rule: `source_table_date <= signal_date`",
        "- formal_use: blocked until an explicit model-specific promotion PR updates contract/parity/validators and passes post-merge main validation.",
        "",
        markdown_table(
            matrix,
            [
                "anomaly_exclusion_basis",
                "condition_test_id",
                "condition_family",
                "source_mature_signal_stock_days",
                "accepted_trade_count",
                "accepted_trade_share_of_baseline_pct",
                "win_rate_pct",
                "neutral_rate_pct",
                "failure_rate_pct",
                "avg_realized_return_pct",
                "median_realized_return_pct",
                "high_return_8_rate_pct",
                "loss_5_rate_pct",
                "avg_revenue_latest_yoy_pct",
                "avg_revenue_cumulative_yoy_pct",
                "promotion_readiness",
            ],
            limit=120,
        )
        if not matrix.empty
        else "No revenue condition matrix rows.",
    ]
    md_path.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8", newline="\n")
    docs_md_path.write_text(md_path.read_text(encoding="utf-8"), encoding="utf-8", newline="\n")


def write_price_pullback_revenue_condition_matrix(matrix: pd.DataFrame) -> None:
    _write_revenue_condition_matrix(
        matrix,
        title="Price Pullback 23EMA Revenue Condition Matrix",
        csv_path=PRICE_PULLBACK_REVENUE_CONDITION_MATRIX_CSV,
        md_path=PRICE_PULLBACK_REVENUE_CONDITION_MATRIX_MD,
        history_path=PRICE_PULLBACK_REVENUE_CONDITION_MATRIX_HISTORY_CSV,
        docs_csv_path=DOCS_PRICE_PULLBACK_REVENUE_CONDITION_MATRIX_CSV,
        docs_md_path=DOCS_PRICE_PULLBACK_REVENUE_CONDITION_MATRIX_MD,
    )


def write_revenue_unreacted_range_revenue_condition_matrix(matrix: pd.DataFrame) -> None:
    _write_revenue_condition_matrix(
        matrix,
        title="Revenue Unreacted Range Revenue Condition Matrix",
        csv_path=REVENUE_UNREACTED_CONDITION_MATRIX_CSV,
        md_path=REVENUE_UNREACTED_CONDITION_MATRIX_MD,
        history_path=REVENUE_UNREACTED_CONDITION_MATRIX_HISTORY_CSV,
        docs_csv_path=DOCS_REVENUE_UNREACTED_CONDITION_MATRIX_CSV,
        docs_md_path=DOCS_REVENUE_UNREACTED_CONDITION_MATRIX_MD,
    )


def _revenue_horizon_close_return(frame: pd.DataFrame, holding_window_days: int) -> pd.Series:
    direct = f"next_open_to_d{holding_window_days}_close_return_pct"
    day_close = f"next_open_to_d{holding_window_days}_day_close_return_pct"
    if direct in frame.columns:
        return pd.to_numeric(frame[direct], errors="coerce")
    return pd.to_numeric(frame[day_close], errors="coerce") if day_close in frame.columns else pd.Series(math.nan, index=frame.index)


def _revenue_operation_required_columns(exit_spec: dict[str, object]) -> list[str]:
    holding_window_days = int(exit_spec["holding_window_days"])
    required = ["next_open", f"next_open_to_d{holding_window_days}_day_close_return_pct"]
    if exit_spec["stop_rule_id"] != "no_stop":
        required.extend(f"next_open_to_d{day}_day_close_return_pct" for day in range(1, holding_window_days + 1))
        required.extend(f"future_d{day}_ma20" for day in range(1, holding_window_days + 1))
        required.extend(f"future_d{day}_ema23" for day in range(1, holding_window_days + 1))
        required.extend(f"future_d{day + 1}_open" for day in range(1, holding_window_days + 1))
    return sorted(set(required))


def _available_revenue_operation_frame(frame: pd.DataFrame, exit_spec: dict[str, object]) -> pd.DataFrame:
    required = _revenue_operation_required_columns(exit_spec)
    available = [col for col in required if col in frame.columns]
    if "next_open" not in available:
        return frame.iloc[0:0].copy()
    holding_window_days = int(exit_spec["holding_window_days"])
    if _revenue_horizon_close_return(frame, holding_window_days).isna().all():
        return frame.iloc[0:0].copy()
    if len(available) != len(required):
        return frame.iloc[0:0].copy()
    return frame.dropna(subset=available).copy()


def _revenue_same_stock_non_overlap(frame: pd.DataFrame, *, cooldown_days: int) -> tuple[pd.DataFrame, int]:
    if frame.empty:
        return frame.copy(), 0
    sorted_frame = frame.sort_values(["stock_id", "_revenue_signal_date", "_revenue_stock_sequence_index"]).copy()
    accepted: list[int] = []
    suppressed = 0
    for _, stock_rows in sorted_frame.groupby("stock_id", sort=False, dropna=False):
        last_accepted_sequence: int | None = None
        for index, row in stock_rows.iterrows():
            sequence = int(row["_revenue_stock_sequence_index"])
            if last_accepted_sequence is not None and sequence <= last_accepted_sequence + cooldown_days:
                suppressed += 1
                continue
            accepted.append(index)
            last_accepted_sequence = sequence
    return sorted_frame.loc[accepted].copy(), suppressed


def _revenue_same_stock_overlap_pair_count(frame: pd.DataFrame, *, cooldown_days: int) -> int:
    if frame.empty:
        return 0
    count = 0
    sorted_frame = frame.sort_values(["stock_id", "_revenue_stock_sequence_index"])
    for _, stock_rows in sorted_frame.groupby("stock_id", sort=False, dropna=False):
        sequences = pd.to_numeric(stock_rows["_revenue_stock_sequence_index"], errors="coerce").dropna().astype(int).tolist()
        for left, right in zip(sequences, sequences[1:]):
            if right <= left + cooldown_days:
                count += 1
    return count


def _revenue_operation_outcome_metrics(valid: pd.DataFrame, exit_spec: dict[str, object]) -> dict[str, object]:
    if valid.empty:
        return {
            "mature_count": 0,
            "win_count": 0,
            "neutral_count": 0,
            "failure_count": 0,
            "win_rate_pct": "",
            "neutral_rate_pct": "",
            "failure_rate_pct": "",
            "avg_realized_return_pct": "",
            "median_realized_return_pct": "",
            "high_return_8_count": 0,
            "high_return_8_rate_pct": "",
            "loss_5_count": 0,
            "loss_5_rate_pct": "",
            "stop_trigger_count": 0,
            "stop_trigger_rate_pct": "",
            "avg_realized_or_fixed_days": "",
            "avg_days_to_stop": "",
            "avg_revenue_latest_yoy_pct": "",
            "median_revenue_latest_yoy_pct": "",
            "avg_revenue_cumulative_yoy_pct": "",
            "median_revenue_cumulative_yoy_pct": "",
        }

    holding_window_days = int(exit_spec["holding_window_days"])
    final_close_return = _revenue_horizon_close_return(valid, holding_window_days)
    realized_return = final_close_return.copy()
    realized_days = pd.Series(float(holding_window_days), index=valid.index, dtype=float)
    stop_day = pd.Series(math.nan, index=valid.index, dtype=float)

    if exit_spec["stop_rule_id"] != "no_stop":
        close_cols = [f"next_open_to_d{day}_day_close_return_pct" for day in range(1, holding_window_days + 1)]
        close_returns = valid[close_cols].apply(pd.to_numeric, errors="coerce")
        entry_price = numeric_column(valid, "next_open")
        close_prices = close_returns.div(100.0).add(1.0).mul(entry_price, axis=0)
        refs = _future_reference_frame(valid, holding_window_days, "lower_ma20_ema23", close_cols)
        stop_threshold = refs * 0.96
        stop_hits = close_prices.le(stop_threshold)
        stop_day = _first_consecutive_hit_day(stop_hits, 4)
        stop_day = stop_day.where(stop_day < holding_window_days)
        stop_return = _value_at_day(_future_open_return_frame(valid, holding_window_days), stop_day)
        realized_return = realized_return.mask(stop_day.notna(), stop_return)
        realized_days = realized_days.mask(stop_day.notna(), stop_day.add(1.0))

    clean = pd.to_numeric(realized_return, errors="coerce")
    valid_result = valid[clean.notna()].copy()
    realized = clean[clean.notna()]
    realized_days = realized_days.loc[realized.index]
    stop_day = stop_day.loc[realized.index]
    wins = realized.ge(5.0)
    neutral = realized.ge(0.0) & realized.lt(5.0)
    failure = realized.lt(0.0)
    high8 = realized.ge(8.0)
    loss5 = realized.le(-5.0)
    latest = numeric_column(valid_result, "full_monthly_revenue_latest_yoy_pct")
    cumulative = numeric_column(valid_result, "full_monthly_revenue_cumulative_yoy_pct")
    mature = len(realized)
    return {
        "mature_count": mature,
        "win_count": int(wins.sum()),
        "neutral_count": int(neutral.sum()),
        "failure_count": int(failure.sum()),
        "win_rate_pct": _rate(int(wins.sum()), mature),
        "neutral_rate_pct": _rate(int(neutral.sum()), mature),
        "failure_rate_pct": _rate(int(failure.sum()), mature),
        "avg_realized_return_pct": _mean_or_blank(realized),
        "median_realized_return_pct": _median_or_blank(realized),
        "high_return_8_count": int(high8.sum()),
        "high_return_8_rate_pct": _rate(int(high8.sum()), mature),
        "loss_5_count": int(loss5.sum()),
        "loss_5_rate_pct": _rate(int(loss5.sum()), mature),
        "stop_trigger_count": int(stop_day.notna().sum()),
        "stop_trigger_rate_pct": _rate(int(stop_day.notna().sum()), mature),
        "avg_realized_or_fixed_days": _mean_or_blank(realized_days),
        "avg_days_to_stop": _mean_or_blank(stop_day),
        "avg_revenue_latest_yoy_pct": _mean_or_blank(latest),
        "median_revenue_latest_yoy_pct": _median_or_blank(latest),
        "avg_revenue_cumulative_yoy_pct": _mean_or_blank(cumulative),
        "median_revenue_cumulative_yoy_pct": _median_or_blank(cumulative),
    }


def _revenue_operation_decision_hint(metrics: dict[str, object]) -> str:
    win_rate = _numeric_or_nan(metrics.get("win_rate_pct", ""))
    avg_return = _numeric_or_nan(metrics.get("avg_realized_return_pct", ""))
    median_return = _numeric_or_nan(metrics.get("median_realized_return_pct", ""))
    failure_rate = _numeric_or_nan(metrics.get("failure_rate_pct", ""))
    if win_rate >= 60.0 and avg_return > 0.0 and median_return > 0.0 and failure_rate <= 40.0:
        return "candidate_metric_met_research_only_needs_model_decision"
    if win_rate >= 50.0 and avg_return > 0.0 and median_return > 0.0:
        return "positive_payoff_but_win_rate_below_metric"
    if avg_return > 0.0 and median_return <= 0.0:
        return "average_positive_but_median_not_confirmed"
    return "not_candidate_metric"


def build_revenue_unreacted_range_operation_candidate_matrix(df: pd.DataFrame) -> pd.DataFrame:
    positioned = _price_pullback_positioned_frame(df).sort_values(["stock_id", "_price_pullback_signal_date"]).copy()
    positioned["_revenue_signal_date"] = positioned["_price_pullback_signal_date"]
    positioned["_revenue_stock_sequence_index"] = positioned.groupby("stock_id", sort=False).cumcount()
    research_dates = positioned["_revenue_signal_date"].map(safe_str)
    research_trading_day_count = int(research_dates[research_dates.ne("")].nunique())
    base = positioned[current_revenue_unreacted_baseline_proxy(positioned).fillna(False)].copy()
    rows: list[dict[str, object]] = []
    generated_at = now_text()
    non_overlap_cooldown_days = 20

    for anomaly_basis in ["including_numerical_anomalies", "excluding_revenue_numerical_anomalies"]:
        baseline_exception_mask = _full_monthly_revenue_anomaly_mask(base)
        basis_base = base[~baseline_exception_mask].copy() if anomaly_basis.startswith("excluding") else base.copy()
        for spec in REVENUE_UNREACTED_OPERATION_CONDITION_TESTS:
            condition_mask = spec["condition"](base).fillna(False)
            picked_raw = base[condition_mask].copy()
            sample_exception_mask = _full_monthly_revenue_anomaly_mask(picked_raw)
            picked = picked_raw[~sample_exception_mask].copy() if anomaly_basis.startswith("excluding") else picked_raw
            source_date_stats = _price_pullback_date_stats(picked)
            non_overlap, suppressed_count = _revenue_same_stock_non_overlap(
                picked,
                cooldown_days=non_overlap_cooldown_days,
            )
            for exit_spec in REVENUE_UNREACTED_OPERATION_EXIT_SPECS:
                valid = _available_revenue_operation_frame(non_overlap, exit_spec)
                metrics = _revenue_operation_outcome_metrics(valid, exit_spec)
                accepted_trade_count = int(metrics["mature_count"])
                decision_hint = _revenue_operation_decision_hint(metrics)
                rows.append(
                    {
                        "generated_at": generated_at,
                        "model_id": "revenue_unreacted_range",
                        "model_name_zh": "營收爆發但股價尚未反應模型",
                        "research_artifact_id": "revenue_unreacted_range_operation_candidate_matrix",
                        "matrix_scope": "model_specific_operation_candidate_research",
                        "base_condition_id": "price_range_no_attack_proxy",
                        "base_condition_rule": "price remains inside the recent 23-day range and active attack has not started",
                        "test_order": spec["test_order"],
                        "condition_test_id": spec["condition_test_id"],
                        "condition_family": spec["condition_family"],
                        "condition_role_candidate": spec["condition_role_candidate"],
                        "condition_rule": spec["condition_rule"],
                        "data_status": "joined_from_full_market_monthly_revenue_history_research_only",
                        "revenue_join_source": FULL_MONTHLY_REVENUE_HISTORY_CSV.as_posix(),
                        "point_in_time_rule": "monthly revenue source_table_date must be <= signal_date",
                        "anomaly_exclusion_basis": anomaly_basis,
                        "revenue_anomaly_count_in_sample": int(sample_exception_mask.sum()),
                        "revenue_anomaly_count_in_baseline": int(baseline_exception_mask.sum()),
                        "entry_rule_id": "signal_date_close_condition_next_open_entry",
                        "confirmation_rule_id": "signal_date_close_condition_confirmed",
                        "entry_rule": "candidate condition is evaluated after signal-date close; entry uses next trading day open",
                        "exit_order": exit_spec["exit_order"],
                        "exit_rule_id": exit_spec["exit_rule_id"],
                        "holding_window_days": exit_spec["holding_window_days"],
                        "exit_rule": exit_spec["exit_rule"],
                        "stop_rule_id": exit_spec["stop_rule_id"],
                        "stop_rule": exit_spec["stop_rule"],
                        "operation_basis": "research_only_close_confirmed_operation_candidate",
                        "formal_price_rule_status": "research_only_no_formal_operation_contract",
                        "win_definition": "realized return >= +5%",
                        "neutral_definition": "0% <= realized return < +5%",
                        "failure_definition": "realized return < 0%",
                        "metric_basis": "close-only fixed exit or close-confirmed stop with next trading day open stop execution",
                        "source_mature_signal_stock_days": len(picked),
                        "source_unique_stocks": picked["stock_id"].nunique() if "stock_id" in picked.columns else "",
                        "non_overlap_cooldown_days": non_overlap_cooldown_days,
                        "non_overlap_applied": True,
                        "same_stock_overlap_pair_count": _revenue_same_stock_overlap_pair_count(
                            valid,
                            cooldown_days=non_overlap_cooldown_days,
                        ),
                        "accepted_signal_count_after_non_overlap": len(non_overlap),
                        "suppressed_signal_count": suppressed_count,
                        "suppressed_rate_pct": _rate(suppressed_count, len(picked)),
                        "accepted_trade_count": accepted_trade_count,
                        "accepted_unique_stocks": valid["stock_id"].nunique() if accepted_trade_count and "stock_id" in valid.columns else "",
                        "source_signal_day_count": source_date_stats["signal_day_count"],
                        "source_avg_signals_per_signal_day": source_date_stats["avg_rows_per_signal_day"],
                        "research_trading_day_count": research_trading_day_count,
                        "accepted_avg_trades_per_research_day": (
                            round(accepted_trade_count / research_trading_day_count, 2)
                            if research_trading_day_count
                            else ""
                        ),
                        "first_signal_date": source_date_stats["first_signal_date"],
                        "last_signal_date": source_date_stats["last_signal_date"],
                        "metric_surface_use": "model_lane_research_metric_source_candidate_not_pdf_ready",
                        "sample_count_context": "reported_not_a_disqualifier_non_overlap_enforced",
                        "meets_win_return_metric": decision_hint == "candidate_metric_met_research_only_needs_model_decision",
                        "decision_hint": decision_hint,
                        "advisory_status": "not_production_ready_research_only",
                        "approved_for_daily": False,
                        "production_change": "none",
                        "promotion_readiness": "research_only_operation_candidate_not_promotion_ready",
                        "promotion_blocker": (
                            "revenue_unreacted_range still needs high-return/low-return feature review, explicit "
                            "buy/sell/stop contract, contract/parity/validator updates, PR merge, and post-merge "
                            "main validation before any operation candidate can be formal"
                        ),
                        **metrics,
                    }
                )

    out = pd.DataFrame(rows)
    if out.empty:
        return out
    baseline_counts = (
        out[out["condition_test_id"].eq("revenue_context_ready")]
        .set_index(["anomaly_exclusion_basis", "exit_rule_id"])["accepted_trade_count"]
        .to_dict()
    )
    out["baseline_accepted_trade_count"] = out.apply(
        lambda row: baseline_counts.get((row["anomaly_exclusion_basis"], row["exit_rule_id"]), 0),
        axis=1,
    )
    out["accepted_trade_share_of_baseline_pct"] = out.apply(
        lambda row: _rate(int(row["accepted_trade_count"]), int(row["baseline_accepted_trade_count"])),
        axis=1,
    )
    return out.sort_values(["anomaly_exclusion_basis", "test_order", "exit_order"]).reset_index(drop=True)


def write_revenue_unreacted_range_operation_candidate_matrix(matrix: pd.DataFrame) -> None:
    write_csv(matrix, REVENUE_UNREACTED_OPERATION_CANDIDATE_MATRIX_CSV)
    write_csv(matrix, REVENUE_UNREACTED_OPERATION_CANDIDATE_MATRIX_HISTORY_CSV)
    write_csv(matrix, DOCS_REVENUE_UNREACTED_OPERATION_CANDIDATE_MATRIX_CSV)
    lines = [
        "# Revenue Unreacted Range Operation Candidate Matrix",
        "",
        f"- generated_at: `{now_text()}`",
        "- status: `not_production_ready_research_only`",
        "- production_change: `none`",
        "- scope: monthly revenue only; quarterly/annual financial statements, EPS, gross margin, operating margin, operating income, non-operating income, and net income are out of scope.",
        "- entry_basis: signal-date close condition, next trading day open entry.",
        "- exit_basis: fixed D+10/D+15/D+20 close, optionally with close-confirmed MA20/EMA23 4-day stop and next trading day open stop execution.",
        "- duplicate_control: same-stock non-overlap enforced with a 20-trading-day cooldown.",
        "- formal_use: blocked until an explicit model-specific promotion PR updates contract/parity/validators and passes post-merge main validation.",
        "",
        markdown_table(
            matrix[matrix["anomaly_exclusion_basis"].eq("excluding_revenue_numerical_anomalies")],
            [
                "condition_test_id",
                "exit_rule_id",
                "accepted_trade_count",
                "suppressed_signal_count",
                "win_rate_pct",
                "neutral_rate_pct",
                "failure_rate_pct",
                "avg_realized_return_pct",
                "median_realized_return_pct",
                "stop_trigger_rate_pct",
                "accepted_trade_share_of_baseline_pct",
                "decision_hint",
            ],
            limit=120,
        )
        if not matrix.empty
        else "No revenue operation candidate matrix rows.",
    ]
    REVENUE_UNREACTED_OPERATION_CANDIDATE_MATRIX_MD.write_text(
        "\n".join(lines).rstrip() + "\n",
        encoding="utf-8",
        newline="\n",
    )
    DOCS_REVENUE_UNREACTED_OPERATION_CANDIDATE_MATRIX_MD.write_text(
        REVENUE_UNREACTED_OPERATION_CANDIDATE_MATRIX_MD.read_text(encoding="utf-8"),
        encoding="utf-8",
        newline="\n",
    )


def _price_pullback_ordered_condition_hint(
    spec: dict[str, object],
    mature_count: int,
    baseline_mature_count: int,
    delta_win_rate: float | str,
    delta_failure_rate: float | str,
    delta_avg_return: float | str,
) -> str:
    stage = safe_str(spec.get("test_stage", ""))
    if stage == "00_baseline":
        return "baseline_anchor"
    if stage.startswith("90_"):
        return "defer_until_mature_point_in_time_theme_samples"
    if baseline_mature_count <= 0 or mature_count <= 0:
        return "no_mature_sample"
    mature_share = mature_count / baseline_mature_count * 100.0
    win_delta = _numeric_or_nan(delta_win_rate)
    failure_delta = _numeric_or_nan(delta_failure_rate)
    return_delta = _numeric_or_nan(delta_avg_return)
    if mature_share < 5.0:
        return "too_small_for_required_gate_review_only"
    if win_delta >= 5.0 and failure_delta <= -3.0 and return_delta >= 0.3:
        return "gate_candidate_review"
    if return_delta >= 0.8 and failure_delta <= 0.0:
        return "add_score_candidate_review"
    if win_delta >= 3.0 and failure_delta <= 0.0:
        return "quality_filter_candidate_review"
    if return_delta > 0.0 and mature_share >= 10.0:
        return "add_score_only_candidate"
    if win_delta < 0.0 and failure_delta > 0.0:
        return "reject_as_required_gate_candidate"
    return "mixed_or_neutral_review"


def _price_pullback_ordered_outcome_summary(enriched: pd.DataFrame) -> dict[str, object]:
    if enriched.empty:
        return {
            **_blank_operation_outcome(),
            "hard_stop_count": 0,
            "ma5_exit_count": 0,
            "hard_stop_rate_pct": "",
            "ma5_exit_rate_pct": "",
        }
    mature = len(enriched)
    wins = enriched["outcome_bucket"].eq("win")
    neutral = enriched["outcome_bucket"].eq("neutral")
    failure = enriched["outcome_bucket"].eq("failure")
    same_day = enriched["outcome_bucket"].eq("same_day_unresolved")
    hard_stop = trueish(enriched["hard_stop_failure"]) if "hard_stop_failure" in enriched.columns else bool_series(enriched, False)
    ma5_exit = trueish(enriched["ma5_exit"]) if "ma5_exit" in enriched.columns else bool_series(enriched, False)
    return {
        "mature_count": mature,
        "win_count": int(wins.sum()),
        "neutral_count": int(neutral.sum()),
        "failure_count": int(failure.sum()),
        "same_day_unresolved_count": int(same_day.sum()),
        "hard_stop_count": int(hard_stop.sum()),
        "ma5_exit_count": int(ma5_exit.sum()),
        "win_rate_pct": _rate(int(wins.sum()), mature),
        "neutral_rate_pct": _rate(int(neutral.sum()), mature),
        "failure_rate_pct": _rate(int(failure.sum()), mature),
        "same_day_unresolved_rate_pct": _rate(int(same_day.sum()), mature),
        "hard_stop_rate_pct": _rate(int(hard_stop.sum()), mature),
        "ma5_exit_rate_pct": _rate(int(ma5_exit.sum()), mature),
        "avg_d20_close_return_pct": _mean_or_blank(enriched["final_d20_close_return_pct"]),
        "median_d20_close_return_pct": _median_or_blank(enriched["final_d20_close_return_pct"]),
        "avg_realized_return_pct": _mean_or_blank(enriched["realized_return_pct"]),
        "avg_win_realized_return_pct": _mean_or_blank(enriched.loc[wins, "realized_return_pct"]),
        "avg_failure_realized_return_pct": _mean_or_blank(enriched.loc[failure, "realized_return_pct"]),
        "avg_neutral_realized_return_pct": _mean_or_blank(enriched.loc[neutral, "realized_return_pct"]),
        "avg_realized_or_d20_days": _mean_or_blank(enriched["realized_days"]),
        "avg_days_to_win": _mean_or_blank(enriched.loc[wins, "target_day"]),
        "avg_days_to_failure": _mean_or_blank(enriched.loc[failure, "realized_days"]),
    }


def build_price_pullback_ordered_condition_matrix(df: pd.DataFrame) -> pd.DataFrame:
    base_mask = current_price_pullback_baseline_proxy(df).fillna(False)
    base = add_price_pullback_research_score_columns(df[base_mask].copy())
    exit_candidates = {
        str(candidate["exit_rule_id"]): candidate
        for candidate in PRICE_PULLBACK_EXIT_RULE_COMPARISON_CANDIDATES
        if str(candidate["exit_rule_id"]) in PRICE_PULLBACK_ORDERED_CONDITION_EXIT_RULE_IDS
    }
    rows: list[dict[str, object]] = []
    generated_at = now_text()
    for exit_rule_id, candidate in exit_candidates.items():
        required = _price_pullback_exit_required_columns(candidate)
        valid_base = (
            base.dropna(subset=required).copy()
            if all(col in base.columns for col in required)
            else base.iloc[0:0].copy()
        )
        if valid_base.empty:
            continue
        base_outcome = _price_pullback_exit_rule_outcome_rows(valid_base, candidate)
        enriched_base = valid_base.join(base_outcome)
        baseline_exception_mask = _price_pullback_known_data_quality_exception_mask(enriched_base)
        for anomaly_basis in [
            PRICE_PULLBACK_INCLUDE_DATA_QUALITY_EXCEPTIONS,
            PRICE_PULLBACK_EXCLUDE_KNOWN_DATA_QUALITY_EXCEPTIONS,
        ]:
            if anomaly_basis == PRICE_PULLBACK_EXCLUDE_KNOWN_DATA_QUALITY_EXCEPTIONS:
                basis_enriched_base = enriched_base[~baseline_exception_mask].copy()
            else:
                basis_enriched_base = enriched_base.copy()
            baseline_counts = _price_pullback_ordered_outcome_summary(basis_enriched_base)
            baseline_mature_count = int(baseline_counts["mature_count"])
            baseline_win_rate = _numeric_or_nan(baseline_counts["win_rate_pct"])
            baseline_failure_rate = _numeric_or_nan(baseline_counts["failure_rate_pct"])
            baseline_avg_return = _numeric_or_nan(baseline_counts["avg_realized_return_pct"])
            for spec in PRICE_PULLBACK_ORDERED_CONDITION_TESTS:
                condition = spec.get("condition")
                if condition is None:
                    raw_picked_index = base.index[0:0]
                else:
                    condition_mask = condition(base).fillna(False)
                    raw_picked_index = base.index[condition_mask]
                raw_valid_index = raw_picked_index.intersection(enriched_base.index)
                sample_exception_source = enriched_base.loc[raw_valid_index].copy()
                sample_exception_mask = _price_pullback_known_data_quality_exception_mask(sample_exception_source)
                valid_picked_index = raw_valid_index.intersection(basis_enriched_base.index)
                picked = base.loc[valid_picked_index].copy()
                enriched = basis_enriched_base.loc[valid_picked_index].copy()
                outcome = _price_pullback_ordered_outcome_summary(enriched)
                if enriched.empty:
                    avg_score = ""
                    avg_space = ""
                    median_space = ""
                else:
                    avg_score = _mean_or_blank(enriched["price_pullback_research_score"])
                    avg_space = _mean_or_blank(enriched["prev20_target_return_pct"])
                    median_space = _median_or_blank(enriched["prev20_target_return_pct"])
                mature_count = int(outcome["mature_count"])
                win_rate = _numeric_or_nan(outcome["win_rate_pct"])
                failure_rate = _numeric_or_nan(outcome["failure_rate_pct"])
                avg_return = _numeric_or_nan(outcome["avg_realized_return_pct"])
                delta_win_rate = (
                    round(win_rate - baseline_win_rate, 2)
                    if not math.isnan(win_rate) and not math.isnan(baseline_win_rate)
                    else ""
                )
                delta_failure_rate = (
                    round(failure_rate - baseline_failure_rate, 2)
                    if not math.isnan(failure_rate) and not math.isnan(baseline_failure_rate)
                    else ""
                )
                delta_avg_return = (
                    round(avg_return - baseline_avg_return, 2)
                    if not math.isnan(avg_return) and not math.isnan(baseline_avg_return)
                    else ""
                )
                mature_share = _rate(mature_count, baseline_mature_count)
                row = {
                    "generated_at": generated_at,
                    "model_id": "price_pullback_23ema",
                    "model_name_zh": "股價回檔模型",
                    "research_artifact_id": "price_pullback_23ema_ordered_condition_matrix",
                    "test_order": spec["test_order"],
                    "test_stage": spec["test_stage"],
                    "condition_test_id": spec["condition_test_id"],
                    "condition_role_candidate": spec["condition_role_candidate"],
                    "condition_rule": spec["condition_rule"],
                    "data_status": spec["data_status"],
                    "anomaly_exclusion_basis": anomaly_basis,
                    "known_data_quality_exception_count_in_sample": int(sample_exception_mask.sum()),
                    "known_data_quality_exception_count_in_baseline": int(baseline_exception_mask.sum()),
                    "known_data_quality_exception_ids": ";".join(
                        _price_pullback_known_data_quality_exception_ids(sample_exception_source)
                    ),
                    "exit_rule_id": exit_rule_id,
                    "formal_price_rule_status": candidate["formal_price_rule_status"],
                    "profit_target_pct": candidate["profit_target_pct"],
                    "exit_price_rule": candidate["exit_price_rule"],
                    "entry_rule_id": "signal_date_next_open",
                    "buy_point_rule": (
                        "Buy next open only after the price_pullback_23ema production proxy signal; "
                        "ordered conditions are research-only."
                    ),
                    "selected_stock_days": len(picked),
                    "selected_unique_stocks": picked["stock_id"].nunique() if "stock_id" in picked.columns else "",
                    "baseline_mature_count": baseline_mature_count,
                    "mature_share_of_baseline_pct": mature_share,
                    "avg_research_score": avg_score,
                    "avg_prev20_target_return_pct": avg_space,
                    "median_prev20_target_return_pct": median_space,
                    "delta_vs_baseline_win_rate_pct": delta_win_rate,
                    "delta_vs_baseline_failure_rate_pct": delta_failure_rate,
                    "delta_vs_baseline_avg_realized_return_pct": delta_avg_return,
                    "decision_hint": _price_pullback_ordered_condition_hint(
                        spec,
                        mature_count,
                        baseline_mature_count,
                        delta_win_rate,
                        delta_failure_rate,
                        delta_avg_return,
                    ),
                    "score_use": "research_only_not_production_score",
                    "advisory_status": "not_production_ready_research_only",
                    "approved_for_daily": False,
                    "production_change": "none",
                    "promotion_readiness": "blocked_exact_daily_row_parity_and_operation_approval_required",
                    "promotion_blocker": (
                        "requires explicit model-rule decision, production contract update if promoted, exact parity, "
                        "validators, PR merge, and post-merge main validation"
                    ),
                    **outcome,
                }
                rows.append(row)
    out = pd.DataFrame(rows)
    if out.empty:
        return out
    anomaly_order = {
        PRICE_PULLBACK_INCLUDE_DATA_QUALITY_EXCEPTIONS: 0,
        PRICE_PULLBACK_EXCLUDE_KNOWN_DATA_QUALITY_EXCEPTIONS: 1,
    }
    out["_anomaly_order"] = out["anomaly_exclusion_basis"].map(anomaly_order).fillna(99)
    out = out.sort_values(["exit_rule_id", "_anomaly_order", "test_order"]).drop(columns=["_anomaly_order"])
    out = out.reset_index(drop=True)
    return out


def write_price_pullback_ordered_condition_matrix(matrix: pd.DataFrame) -> None:
    write_csv(matrix, PRICE_PULLBACK_ORDERED_CONDITION_MATRIX_CSV)
    write_csv(matrix, PRICE_PULLBACK_ORDERED_CONDITION_MATRIX_HISTORY_CSV)
    write_csv(matrix, DOCS_PRICE_PULLBACK_ORDERED_CONDITION_MATRIX_CSV)
    lines = [
        "# Price Pullback 23EMA Ordered Condition Matrix",
        "",
        f"- generated_at: `{now_text()}`",
        "- model_id: `price_pullback_23ema`",
        "- status: `not_production_ready_research_only`",
        "- scope: ordered research matrix for deciding necessary conditions, add-score items, risk filters, or rejected conditions.",
        "- production_change: `none`",
        "- entry_basis: `signal_date_next_open`; entry conditions are evaluated as research-only filters after the production proxy signal.",
        "- exit_basis: close-confirmed previous-20-day-high exits use next open; continuation exits use next open after close target or 5MA close exit.",
        "- theme_context_status: deferred rows are coverage checks only until enough point-in-time D+20 mature samples exist.",
        "- promotion_blocker: production use requires explicit model-rule decision, contract update when applicable, parity, validators, merge, and post-merge main validation.",
        "",
        markdown_table(
            matrix,
            [
                "test_stage",
                "condition_test_id",
                "condition_role_candidate",
                "anomaly_exclusion_basis",
                "known_data_quality_exception_count_in_sample",
                "exit_rule_id",
                "mature_count",
                "mature_share_of_baseline_pct",
                "win_rate_pct",
                "failure_rate_pct",
                "avg_realized_return_pct",
                "delta_vs_baseline_win_rate_pct",
                "delta_vs_baseline_failure_rate_pct",
                "delta_vs_baseline_avg_realized_return_pct",
                "avg_research_score",
                "avg_prev20_target_return_pct",
                "decision_hint",
            ],
            limit=120,
        )
        if not matrix.empty
        else "No ordered condition rows.",
    ]
    PRICE_PULLBACK_ORDERED_CONDITION_MATRIX_MD.write_text(
        "\n".join(lines).rstrip() + "\n",
        encoding="utf-8",
        newline="\n",
    )
    DOCS_PRICE_PULLBACK_ORDERED_CONDITION_MATRIX_MD.write_text(
        PRICE_PULLBACK_ORDERED_CONDITION_MATRIX_MD.read_text(encoding="utf-8"),
        encoding="utf-8",
        newline="\n",
    )


def _price_pullback_positioned_frame(df: pd.DataFrame) -> pd.DataFrame:
    out = df.copy()
    out["_price_pullback_source_row_index"] = range(len(out))
    if "date" in out.columns:
        out["_price_pullback_signal_date"] = out["date"].map(normalize_date)
    else:
        out["_price_pullback_signal_date"] = ""
    if "stock_id" not in out.columns:
        out["stock_id"] = ""

    sort_cols = ["stock_id", "_price_pullback_signal_date", "_price_pullback_source_row_index"]
    sorted_out = out.sort_values(sort_cols, kind="mergesort").copy()
    sorted_out["_price_pullback_stock_day_position"] = (
        sorted_out.groupby("stock_id", dropna=False).cumcount().astype(int)
    )
    return sorted_out.sort_values("_price_pullback_source_row_index", kind="mergesort")


def _price_pullback_lifecycle_input_frame(df: pd.DataFrame) -> pd.DataFrame:
    columns = {
        "date",
        "stock_id",
        "close",
        "ema23",
        "ma20",
        "ema23_slope_pct",
        "ema23_slope_5d_pct",
        "ma5_turning_up_flag",
        "ma10_turning_up_flag",
        "distance_ema23_pct",
        "platform_low",
        "short_platform_low",
        "previous_20d_low",
        "low_20",
        "range_low_20d_prev",
        "return_20d_pct",
        "return_45d_pct",
        "range_width_45d_pct",
        "prior_extension_ema23_20d_pct",
        "prior_runup_20d_pct",
        "tdcc_history_available",
        "high_thresholds_up",
        "obv_above_ma20",
        "volume_ratio_prev20",
        "bullish_attack_candle",
        "solid_red_candle",
    }
    for candidate in PRICE_PULLBACK_EXIT_RULE_COMPARISON_CANDIDATES:
        if str(candidate["exit_rule_id"]) in PRICE_PULLBACK_ORDERED_CONDITION_EXIT_RULE_IDS:
            columns.update(_price_pullback_exit_required_columns(candidate))
    existing = [col for col in sorted(columns) if col in df.columns]
    return df.loc[:, existing].copy()


def _price_pullback_next_open_exit_offset(enriched: pd.DataFrame) -> pd.Series:
    if enriched.empty:
        return pd.Series(dtype=int)
    target = trueish(enriched["target_before_stop"]) if "target_before_stop" in enriched.columns else bool_series(enriched)
    ma5_exit = trueish(enriched["ma5_exit"]) if "ma5_exit" in enriched.columns else bool_series(enriched)
    hard_stop = (
        trueish(enriched["hard_stop_failure"])
        if "hard_stop_failure" in enriched.columns
        else bool_series(enriched)
    )
    same_day = (
        trueish(enriched["same_day_unresolved"])
        if "same_day_unresolved" in enriched.columns
        else bool_series(enriched)
    )
    return (target | ma5_exit | hard_stop | same_day).astype(int)


def _price_pullback_apply_lifecycle_suppression(enriched: pd.DataFrame) -> pd.DataFrame:
    if enriched.empty:
        out = enriched.copy()
        out["lifecycle_accepted_trade"] = pd.Series(dtype=bool)
        out["lifecycle_suppressed_signal"] = pd.Series(dtype=bool)
        out["lifecycle_exit_stock_day_position"] = pd.Series(dtype=float)
        out["lifecycle_exit_signal_date"] = pd.Series(dtype=object)
        out["lifecycle_suppressed_by_signal_date"] = pd.Series(dtype=object)
        out["lifecycle_suppressed_by_exit_signal_date"] = pd.Series(dtype=object)
        out["lifecycle_suppressed_by_exit_stock_day_position"] = pd.Series(dtype=object)
        return out

    work = enriched.copy().reset_index(drop=False).rename(columns={"index": "_price_pullback_original_index"})
    realized_days = pd.to_numeric(work["realized_days"], errors="coerce").fillna(TIME_COST_HORIZON_DAYS)
    exit_offset = _price_pullback_next_open_exit_offset(work)
    signal_position = pd.to_numeric(work["_price_pullback_stock_day_position"], errors="coerce")
    work["lifecycle_exit_lag_days"] = realized_days + exit_offset
    work["lifecycle_exit_stock_day_position"] = signal_position + work["lifecycle_exit_lag_days"]
    work["lifecycle_exit_signal_date"] = ""
    n = len(work)
    accepted = np.zeros(n, dtype=bool)
    suppressed = np.zeros(n, dtype=bool)
    suppressed_by_signal_date = np.full(n, "", dtype=object)
    suppressed_by_exit_signal_date = np.full(n, "", dtype=object)
    suppressed_by_exit_position = np.full(n, "", dtype=object)
    stock_values = work["stock_id"].map(safe_str).to_numpy(dtype=object)
    signal_dates = work["_price_pullback_signal_date"].map(safe_str).to_numpy(dtype=object)
    exit_dates = work["lifecycle_exit_signal_date"].map(safe_str).to_numpy(dtype=object)
    position_values = pd.to_numeric(work["_price_pullback_stock_day_position"], errors="coerce").to_numpy()
    exit_position_values = pd.to_numeric(work["lifecycle_exit_stock_day_position"], errors="coerce").to_numpy()
    active_by_stock: dict[str, dict[str, object]] = {}
    sort_cols = ["stock_id", "_price_pullback_stock_day_position", "_price_pullback_source_row_index"]
    ordered_indices = work.sort_values(sort_cols, kind="mergesort").index.to_numpy()
    for row_idx in ordered_indices:
        stock_id = stock_values[row_idx]
        position_value = position_values[row_idx]
        exit_position_value = exit_position_values[row_idx]
        if not stock_id or pd.isna(position_value) or pd.isna(exit_position_value):
            accepted[row_idx] = True
            continue

        position_int = int(position_value)
        active = active_by_stock.get(stock_id)
        if active is not None and position_int < int(active["exit_stock_day_position"]):
            suppressed[row_idx] = True
            suppressed_by_signal_date[row_idx] = active["signal_date"]
            suppressed_by_exit_signal_date[row_idx] = active["exit_signal_date"]
            suppressed_by_exit_position[row_idx] = active["exit_stock_day_position"]
            continue

        exit_position_int = int(exit_position_value)
        accepted[row_idx] = True
        active_by_stock[stock_id] = {
            "signal_date": signal_dates[row_idx],
            "exit_signal_date": exit_dates[row_idx],
            "exit_stock_day_position": exit_position_int,
        }

    work["lifecycle_accepted_trade"] = accepted
    work["lifecycle_suppressed_signal"] = suppressed
    work["lifecycle_suppressed_by_signal_date"] = suppressed_by_signal_date
    work["lifecycle_suppressed_by_exit_signal_date"] = suppressed_by_exit_signal_date
    work["lifecycle_suppressed_by_exit_stock_day_position"] = suppressed_by_exit_position
    return work


def _price_pullback_date_stats(frame: pd.DataFrame) -> dict[str, object]:
    if frame.empty or "_price_pullback_signal_date" not in frame.columns:
        return {
            "first_signal_date": "",
            "last_signal_date": "",
            "signal_day_count": 0,
            "avg_rows_per_signal_day": "",
        }
    dates = frame["_price_pullback_signal_date"].map(safe_str)
    dates = dates[dates.ne("")]
    if dates.empty:
        return {
            "first_signal_date": "",
            "last_signal_date": "",
            "signal_day_count": 0,
            "avg_rows_per_signal_day": "",
        }
    signal_day_count = int(dates.nunique())
    return {
        "first_signal_date": dates.min(),
        "last_signal_date": dates.max(),
        "signal_day_count": signal_day_count,
        "avg_rows_per_signal_day": round(len(frame) / signal_day_count, 2) if signal_day_count else "",
    }


def _price_pullback_base_rows_for_lifecycle(base: pd.DataFrame, lifecycle: pd.DataFrame) -> pd.DataFrame:
    if lifecycle.empty or "_price_pullback_original_index" not in lifecycle.columns:
        return base.iloc[0:0].copy()
    original_index = pd.to_numeric(lifecycle["_price_pullback_original_index"], errors="coerce").dropna().astype(int)
    valid_index = base.index.intersection(original_index)
    return base.loc[valid_index].copy()


def _price_pullback_lifecycle_condition_hint(
    spec: dict[str, object],
    accepted_trade_count: int,
    baseline_accepted_trade_count: int,
    delta_win_rate: float | str,
    delta_failure_rate: float | str,
    delta_avg_return: float | str,
) -> str:
    stage = safe_str(spec.get("test_stage", ""))
    if stage == "00_baseline":
        return "baseline_trade_level_anchor"
    if stage.startswith("90_"):
        return "defer_until_mature_point_in_time_theme_samples"
    if baseline_accepted_trade_count <= 0 or accepted_trade_count <= 0:
        return "no_trade_level_sample"
    trade_share = accepted_trade_count / baseline_accepted_trade_count * 100.0
    win_delta = _numeric_or_nan(delta_win_rate)
    failure_delta = _numeric_or_nan(delta_failure_rate)
    return_delta = _numeric_or_nan(delta_avg_return)
    if trade_share < 2.0:
        return "too_small_for_required_gate_review_only"
    if win_delta >= 8.0 and failure_delta <= -5.0 and return_delta >= 0.5:
        return "strong_gate_candidate_review"
    if win_delta >= 5.0 and return_delta >= 0.3:
        return "gate_candidate_review"
    if return_delta >= 0.8 and failure_delta <= 0.0:
        return "add_score_candidate_review"
    if win_delta >= 3.0 and failure_delta <= 0.0:
        return "quality_filter_candidate_review"
    if win_delta < 0.0 and failure_delta > 0.0:
        return "reject_as_required_gate_candidate"
    return "mixed_or_neutral_review"


def build_price_pullback_lifecycle_replay(df: pd.DataFrame) -> pd.DataFrame:
    positioned = _price_pullback_positioned_frame(_price_pullback_lifecycle_input_frame(df))
    research_dates = positioned["_price_pullback_signal_date"].map(safe_str)
    research_trading_day_count = int(research_dates[research_dates.ne("")].nunique())
    base_mask = current_price_pullback_baseline_proxy(positioned).fillna(False)
    base = add_price_pullback_research_score_columns(positioned[base_mask].copy())
    lifecycle_key_cols = [
        "stock_id",
        "_price_pullback_signal_date",
        "_price_pullback_stock_day_position",
        "_price_pullback_source_row_index",
    ]
    exit_candidates = {
        str(candidate["exit_rule_id"]): candidate
        for candidate in PRICE_PULLBACK_EXIT_RULE_COMPARISON_CANDIDATES
        if str(candidate["exit_rule_id"]) in PRICE_PULLBACK_ORDERED_CONDITION_EXIT_RULE_IDS
    }
    rows: list[dict[str, object]] = []
    generated_at = now_text()
    for exit_rule_id, candidate in exit_candidates.items():
        required = _price_pullback_exit_required_columns(candidate)
        valid_base = (
            base.dropna(subset=required).copy()
            if all(col in base.columns for col in required)
            else base.iloc[0:0].copy()
        )
        if valid_base.empty:
            continue
        base_outcome = _price_pullback_exit_rule_outcome_rows(valid_base, candidate)
        enriched_base = valid_base[lifecycle_key_cols].join(base_outcome)
        baseline_lifecycle_all = _price_pullback_apply_lifecycle_suppression(
            enriched_base,
        )
        baseline_exception_mask = _price_pullback_known_data_quality_exception_mask(baseline_lifecycle_all)
        for anomaly_basis in [
            PRICE_PULLBACK_INCLUDE_DATA_QUALITY_EXCEPTIONS,
            PRICE_PULLBACK_EXCLUDE_KNOWN_DATA_QUALITY_EXCEPTIONS,
        ]:
            if anomaly_basis == PRICE_PULLBACK_EXCLUDE_KNOWN_DATA_QUALITY_EXCEPTIONS:
                baseline_lifecycle = baseline_lifecycle_all[~baseline_exception_mask].copy()
            else:
                baseline_lifecycle = baseline_lifecycle_all.copy()
            baseline_accepted = baseline_lifecycle[trueish(baseline_lifecycle["lifecycle_accepted_trade"])]
            baseline_counts = _price_pullback_ordered_outcome_summary(baseline_accepted)
            baseline_accepted_trade_count = int(baseline_counts["mature_count"])
            baseline_win_rate = _numeric_or_nan(baseline_counts["win_rate_pct"])
            baseline_failure_rate = _numeric_or_nan(baseline_counts["failure_rate_pct"])
            baseline_avg_return = _numeric_or_nan(baseline_counts["avg_realized_return_pct"])

            for spec in _price_pullback_lifecycle_replay_condition_tests():
                condition = spec.get("condition")
                condition_id = safe_str(spec["condition_test_id"])
                if condition_id == "baseline_replay":
                    raw_valid_index = baseline_lifecycle_all.index
                    sample_exception_source = baseline_lifecycle_all.copy()
                    lifecycle = baseline_lifecycle.copy()
                    picked_all = _price_pullback_base_rows_for_lifecycle(base, lifecycle)
                elif condition is None:
                    raw_valid_index = enriched_base.index[0:0]
                    sample_exception_source = enriched_base.iloc[0:0].copy()
                    picked_all = base.iloc[0:0].copy()
                    lifecycle = _price_pullback_apply_lifecycle_suppression(enriched_base.iloc[0:0].copy())
                else:
                    condition_mask = condition(base).fillna(False)
                    raw_picked_index = base.index[condition_mask]
                    raw_valid_index = raw_picked_index.intersection(enriched_base.index)
                    enriched = enriched_base.loc[raw_valid_index].copy()
                    lifecycle_raw = _price_pullback_apply_lifecycle_suppression(enriched)
                    sample_exception_source = lifecycle_raw.copy()
                    sample_exception_mask = _price_pullback_known_data_quality_exception_mask(sample_exception_source)
                    if anomaly_basis == PRICE_PULLBACK_EXCLUDE_KNOWN_DATA_QUALITY_EXCEPTIONS:
                        lifecycle = lifecycle_raw[~sample_exception_mask].copy()
                    else:
                        lifecycle = lifecycle_raw.copy()
                    picked_all = _price_pullback_base_rows_for_lifecycle(base, lifecycle)
                sample_exception_mask = _price_pullback_known_data_quality_exception_mask(sample_exception_source)
                accepted = lifecycle[trueish(lifecycle["lifecycle_accepted_trade"])]
                outcome = _price_pullback_ordered_outcome_summary(accepted)
                accepted_trade_count = int(outcome["mature_count"])
                selected_date_stats = _price_pullback_date_stats(picked_all)
                accepted_date_stats = _price_pullback_date_stats(accepted)
                suppressed_count = int(trueish(lifecycle["lifecycle_suppressed_signal"]).sum()) if not lifecycle.empty else 0
                source_mature_count = len(lifecycle)
                win_rate = _numeric_or_nan(outcome["win_rate_pct"])
                failure_rate = _numeric_or_nan(outcome["failure_rate_pct"])
                avg_return = _numeric_or_nan(outcome["avg_realized_return_pct"])
                delta_win_rate = (
                    round(win_rate - baseline_win_rate, 2)
                    if not math.isnan(win_rate) and not math.isnan(baseline_win_rate)
                    else ""
                )
                delta_failure_rate = (
                    round(failure_rate - baseline_failure_rate, 2)
                    if not math.isnan(failure_rate) and not math.isnan(baseline_failure_rate)
                    else ""
                )
                delta_avg_return = (
                    round(avg_return - baseline_avg_return, 2)
                    if not math.isnan(avg_return) and not math.isnan(baseline_avg_return)
                    else ""
                )
                row = {
                    "generated_at": generated_at,
                    "model_id": "price_pullback_23ema",
                    "model_name_zh": "股價回檔模型",
                    "research_artifact_id": "price_pullback_23ema_lifecycle_replay",
                    "lifecycle_replay_scope": "trade_level_same_stock_active_position_suppressed",
                    "test_order": spec["test_order"],
                    "test_stage": spec["test_stage"],
                    "condition_test_id": spec["condition_test_id"],
                    "condition_role_candidate": spec["condition_role_candidate"],
                    "condition_rule": spec["condition_rule"],
                    "data_status": spec["data_status"],
                    "anomaly_exclusion_basis": anomaly_basis,
                    "known_data_quality_exception_count_in_sample": int(sample_exception_mask.sum()),
                    "known_data_quality_exception_count_in_baseline": int(baseline_exception_mask.sum()),
                    "known_data_quality_exception_ids": ";".join(
                        _price_pullback_known_data_quality_exception_ids(sample_exception_source)
                    ),
                    "exit_rule_id": exit_rule_id,
                    "formal_price_rule_status": candidate["formal_price_rule_status"],
                    "profit_target_pct": candidate["profit_target_pct"],
                    "exit_price_rule": candidate["exit_price_rule"],
                    "entry_rule_id": "signal_date_next_open",
                    "buy_point_rule": (
                        "Buy next open only after the price_pullback_23ema production proxy signal; "
                        "lifecycle replay suppresses later same-stock signals until the prior accepted trade exits."
                    ),
                    "source_signal_stock_days": len(picked_all),
                    "source_unique_stocks": picked_all["stock_id"].nunique() if "stock_id" in picked_all.columns else "",
                    "source_mature_signal_stock_days": source_mature_count,
                    "accepted_trade_count": accepted_trade_count,
                    "accepted_unique_stocks": accepted["stock_id"].nunique() if "stock_id" in accepted.columns else "",
                    "suppressed_signal_count": suppressed_count,
                    "suppressed_rate_pct": _rate(suppressed_count, source_mature_count),
                    "accepted_share_of_source_mature_pct": _rate(accepted_trade_count, source_mature_count),
                    "baseline_accepted_trade_count": baseline_accepted_trade_count,
                    "accepted_trade_share_of_baseline_pct": _rate(
                        accepted_trade_count,
                        baseline_accepted_trade_count,
                    ),
                    "source_signal_day_count": selected_date_stats["signal_day_count"],
                    "source_avg_signals_per_signal_day": selected_date_stats["avg_rows_per_signal_day"],
                    "accepted_signal_day_count": accepted_date_stats["signal_day_count"],
                    "accepted_avg_trades_per_signal_day": accepted_date_stats["avg_rows_per_signal_day"],
                    "research_trading_day_count": research_trading_day_count,
                    "source_avg_signals_per_research_day": (
                        round(len(picked_all) / research_trading_day_count, 2)
                        if research_trading_day_count
                        else ""
                    ),
                    "accepted_avg_trades_per_research_day": (
                        round(accepted_trade_count / research_trading_day_count, 2)
                        if research_trading_day_count
                        else ""
                    ),
                    "first_signal_date": selected_date_stats["first_signal_date"],
                    "last_signal_date": selected_date_stats["last_signal_date"],
                    "delta_vs_baseline_win_rate_pct": delta_win_rate,
                    "delta_vs_baseline_failure_rate_pct": delta_failure_rate,
                    "delta_vs_baseline_avg_realized_return_pct": delta_avg_return,
                    "decision_hint": _price_pullback_lifecycle_condition_hint(
                        spec,
                        accepted_trade_count,
                        baseline_accepted_trade_count,
                        delta_win_rate,
                        delta_failure_rate,
                        delta_avg_return,
                    ),
                    "score_use": "research_only_not_production_score",
                    "metric_surface_use": "model_lane_research_metric_source_candidate_not_pdf_ready",
                    "pdf_metric_readiness": "blocked_until_formal_promotion_and_operation_adapter_contract",
                    "advisory_status": "not_production_ready_research_only",
                    "approved_for_daily": False,
                    "production_change": "none",
                    "promotion_readiness": "blocked_exact_daily_row_parity_operation_adapter_and_metric_contract_required",
                    "promotion_blocker": (
                        "requires explicit model-rule decision, lifecycle/operation adapter contract, exact parity, "
                        "validators, PR merge, post-merge main validation, and PDF metric consumer contract before display"
                    ),
                    **outcome,
                }
                rows.append(row)
    out = pd.DataFrame(rows)
    if out.empty:
        return out
    anomaly_order = {
        PRICE_PULLBACK_INCLUDE_DATA_QUALITY_EXCEPTIONS: 0,
        PRICE_PULLBACK_EXCLUDE_KNOWN_DATA_QUALITY_EXCEPTIONS: 1,
    }
    out["_anomaly_order"] = out["anomaly_exclusion_basis"].map(anomaly_order).fillna(99)
    out = out.sort_values(["exit_rule_id", "_anomaly_order", "test_order"]).drop(columns=["_anomaly_order"])
    return out.reset_index(drop=True)


def write_price_pullback_lifecycle_replay(lifecycle: pd.DataFrame) -> None:
    write_csv(lifecycle, PRICE_PULLBACK_LIFECYCLE_REPLAY_CSV)
    write_csv(lifecycle, PRICE_PULLBACK_LIFECYCLE_REPLAY_HISTORY_CSV)
    write_csv(lifecycle, DOCS_PRICE_PULLBACK_LIFECYCLE_REPLAY_CSV)
    lines = [
        "# Price Pullback 23EMA Lifecycle Replay",
        "",
        f"- generated_at: `{now_text()}`",
        "- model_id: `price_pullback_23ema`",
        "- status: `not_production_ready_research_only`",
        "- scope: trade-level replay that suppresses later same-stock signals while a prior accepted trade is still active.",
        "- production_change: `none`",
        "- entry_basis: `signal_date_next_open` after the production proxy signal and research-only condition filter.",
        "- exit_basis: close-confirmed previous-20-day-high exits use next open; continuation exits use next open after close target or 5MA close exit.",
        "- metric_boundary: PDF titles must not calculate win rate or return from candidate rows; they need a model-owned approved metric artifact or operation adapter.",
        "- promotion_blocker: production use requires explicit model-rule decision, contract update when applicable, parity, validators, merge, post-merge main validation, and PDF metric consumer contract.",
        "",
        markdown_table(
            lifecycle,
            [
                "test_stage",
                "condition_test_id",
                "anomaly_exclusion_basis",
                "known_data_quality_exception_count_in_sample",
                "exit_rule_id",
                "source_mature_signal_stock_days",
                "accepted_trade_count",
                "accepted_trade_share_of_baseline_pct",
                "accepted_avg_trades_per_research_day",
                "accepted_avg_trades_per_signal_day",
                "suppressed_signal_count",
                "win_rate_pct",
                "neutral_rate_pct",
                "failure_rate_pct",
                "avg_realized_return_pct",
                "delta_vs_baseline_win_rate_pct",
                "delta_vs_baseline_avg_realized_return_pct",
                "decision_hint",
            ],
            limit=160,
        )
        if not lifecycle.empty
        else "No lifecycle replay rows.",
    ]
    PRICE_PULLBACK_LIFECYCLE_REPLAY_MD.write_text(
        "\n".join(lines).rstrip() + "\n",
        encoding="utf-8",
        newline="\n",
    )
    DOCS_PRICE_PULLBACK_LIFECYCLE_REPLAY_MD.write_text(
        PRICE_PULLBACK_LIFECYCLE_REPLAY_MD.read_text(encoding="utf-8"),
        encoding="utf-8",
        newline="\n",
    )


PRICE_PULLBACK_PROMOTION_MATRIX_EXIT_RULE_ID = "close_prev20_high_break_next_open"
PRICE_PULLBACK_PROMOTION_MATRIX_ANOMALY_BASIS = PRICE_PULLBACK_EXCLUDE_KNOWN_DATA_QUALITY_EXCEPTIONS
PRICE_PULLBACK_PROMOTION_MATRIX_COLUMNS = [
    "generated_at",
    "model_id",
    "model_name_zh",
    "research_artifact_id",
    "matrix_scope",
    "matrix_order",
    "promotion_candidate_id",
    "promotion_axis",
    "source_artifact_id",
    "source_selector",
    "source_metric_basis",
    "proposed_contract_role",
    "proposed_score_points",
    "condition_rule",
    "plain_conclusion_zh",
    "data_status",
    "sample_status",
    "anomaly_exclusion_basis",
    "known_metric_exception_count_in_sample",
    "known_metric_exception_count_in_baseline",
    "known_metric_exception_ids",
    "exit_rule_id",
    "formal_price_rule_status",
    "entry_rule_id",
    "source_mature_signal_stock_days",
    "accepted_trade_count",
    "accepted_avg_trades_per_research_day",
    "accepted_trade_share_of_baseline_pct",
    "win_rate_pct",
    "neutral_rate_pct",
    "failure_rate_pct",
    "avg_realized_return_pct",
    "median_realized_return_pct",
    "high_return_10_rate_pct",
    "loss_5_rate_pct",
    "delta_vs_base_win_rate_pct",
    "delta_vs_base_failure_rate_pct",
    "delta_vs_base_avg_realized_return_pct",
    "metric_surface_use",
    "pdf_metric_readiness",
    "advisory_status",
    "approved_for_daily",
    "production_change",
    "production_decision_status",
    "promotion_readiness",
    "promotion_blocker",
]


def _first_row_matching(df: pd.DataFrame, filters: dict[str, object]) -> pd.Series:
    if df.empty:
        return pd.Series(dtype=object)
    mask = pd.Series(True, index=df.index)
    for column, expected in filters.items():
        if column not in df.columns:
            return pd.Series(dtype=object)
        mask &= df[column].map(safe_str).eq(safe_str(expected))
    rows = df[mask]
    if rows.empty:
        return pd.Series(dtype=object)
    return rows.iloc[0]


def _row_value(row: pd.Series, column: str, default: object = "") -> object:
    if row.empty:
        return default
    return row.get(column, default)


def _row_first_value(row: pd.Series, columns: list[str], default: object = "") -> object:
    for column in columns:
        value = _row_value(row, column, "")
        if safe_str(value) != "":
            return value
    return default


def _row_int_or_none(row: pd.Series, column: str) -> int | None:
    value = _numeric_or_nan(_row_value(row, column, ""))
    if math.isnan(value):
        return None
    return int(value)


def _promotion_sample_status(row: pd.Series) -> str:
    count = _row_int_or_none(row, "accepted_trade_count")
    if count is None:
        count = _row_int_or_none(row, "mature_count")
    if count is None:
        return "definition_row_no_direct_trade_sample"
    return sample_status(count)


def _promotion_metric_delta(row: pd.Series, metric_col: str, baseline: pd.Series) -> float | str:
    existing_col = {
        "win_rate_pct": "delta_vs_baseline_win_rate_pct",
        "failure_rate_pct": "delta_vs_baseline_failure_rate_pct",
        "avg_realized_return_pct": "delta_vs_baseline_avg_realized_return_pct",
    }[metric_col]
    existing = _row_value(row, existing_col, "")
    if safe_str(existing) != "":
        return existing
    return _delta_or_blank(_row_value(row, metric_col, ""), _row_value(baseline, metric_col, ""))


def _promotion_row(
    *,
    generated_at: str,
    matrix_order: int,
    promotion_candidate_id: str,
    promotion_axis: str,
    source_artifact_id: str,
    source_selector: str,
    source_metric_basis: str,
    proposed_contract_role: str,
    proposed_score_points: str,
    condition_rule: str,
    plain_conclusion_zh: str,
    source_row: pd.Series,
    baseline_row: pd.Series,
    data_status: str = "",
) -> dict[str, object]:
    accepted_count = _row_first_value(source_row, ["accepted_trade_count", "mature_count"], "")
    source_count = _row_first_value(
        source_row,
        ["source_mature_signal_stock_days", "mature_count", "source_signal_stock_days", "selected_stock_days"],
        "",
    )
    if source_row.empty:
        data_status = data_status or "missing_source_metric_row"
    else:
        data_status = data_status or safe_str(_row_value(source_row, "data_status", "available_research_metric_row"))
    return {
        "generated_at": generated_at,
        "model_id": "price_pullback_23ema",
        "model_name_zh": "股價回檔模型",
        "research_artifact_id": "price_pullback_23ema_promotion_matrix",
        "matrix_scope": "research_only_promotion_decision_matrix",
        "matrix_order": matrix_order,
        "promotion_candidate_id": promotion_candidate_id,
        "promotion_axis": promotion_axis,
        "source_artifact_id": source_artifact_id,
        "source_selector": source_selector,
        "source_metric_basis": source_metric_basis,
        "proposed_contract_role": proposed_contract_role,
        "proposed_score_points": proposed_score_points,
        "condition_rule": condition_rule or safe_str(_row_value(source_row, "condition_rule", "")),
        "plain_conclusion_zh": plain_conclusion_zh,
        "data_status": data_status,
        "sample_status": _promotion_sample_status(source_row),
        "anomaly_exclusion_basis": _row_value(
            source_row,
            "anomaly_exclusion_basis",
            "definition_row_no_metric_sample",
        ),
        "known_metric_exception_count_in_sample": _row_first_value(
            source_row,
            [
                "known_data_quality_exception_count_in_sample",
                "known_data_quality_exception_count_in_bucket",
                "revenue_or_price_anomaly_count_in_sample",
            ],
            "",
        ),
        "known_metric_exception_count_in_baseline": _row_first_value(
            source_row,
            [
                "known_data_quality_exception_count_in_baseline",
                "revenue_or_price_anomaly_count_in_baseline",
            ],
            "",
        ),
        "known_metric_exception_ids": _row_value(source_row, "known_data_quality_exception_ids", ""),
        "exit_rule_id": _row_value(source_row, "exit_rule_id", PRICE_PULLBACK_PROMOTION_MATRIX_EXIT_RULE_ID),
        "formal_price_rule_status": _row_value(source_row, "formal_price_rule_status", "close_confirmed_candidate"),
        "entry_rule_id": _row_value(source_row, "entry_rule_id", "signal_date_next_open"),
        "source_mature_signal_stock_days": source_count,
        "accepted_trade_count": accepted_count,
        "accepted_avg_trades_per_research_day": _row_value(source_row, "accepted_avg_trades_per_research_day", ""),
        "accepted_trade_share_of_baseline_pct": _row_first_value(
            source_row,
            ["accepted_trade_share_of_baseline_pct", "mature_share_of_baseline_pct", "selected_share_of_baseline_pct"],
            "",
        ),
        "win_rate_pct": _row_value(source_row, "win_rate_pct", ""),
        "neutral_rate_pct": _row_value(source_row, "neutral_rate_pct", ""),
        "failure_rate_pct": _row_value(source_row, "failure_rate_pct", ""),
        "avg_realized_return_pct": _row_value(source_row, "avg_realized_return_pct", ""),
        "median_realized_return_pct": _row_value(source_row, "median_realized_return_pct", ""),
        "high_return_10_rate_pct": _row_value(source_row, "high_return_10_rate_pct", ""),
        "loss_5_rate_pct": _row_value(source_row, "loss_5_rate_pct", ""),
        "delta_vs_base_win_rate_pct": _promotion_metric_delta(source_row, "win_rate_pct", baseline_row),
        "delta_vs_base_failure_rate_pct": _promotion_metric_delta(source_row, "failure_rate_pct", baseline_row),
        "delta_vs_base_avg_realized_return_pct": _promotion_metric_delta(
            source_row,
            "avg_realized_return_pct",
            baseline_row,
        ),
        "metric_surface_use": "model_lane_research_metric_source_candidate_not_pdf_ready",
        "pdf_metric_readiness": "blocked_until_formal_promotion_and_operation_adapter_contract",
        "advisory_status": "not_production_ready_research_only",
        "approved_for_daily": False,
        "production_change": "none",
        "production_decision_status": "research_only_not_approved",
        "promotion_readiness": "blocked_model_specific_promotion_pr_required",
        "promotion_blocker": (
            "promotion matrix is discussion evidence only; production use requires explicit model decision, "
            "contract/parity/validator updates, PR merge, post-merge main validation, and PDF operation metric contract"
        ),
    }


def build_price_pullback_promotion_matrix(
    lifecycle_replay: pd.DataFrame,
    ordered_condition_matrix: pd.DataFrame,
    high_return_score_grid: pd.DataFrame,
    revenue_condition_matrix: pd.DataFrame,
) -> pd.DataFrame:
    generated_at = now_text()
    exit_rule_id = PRICE_PULLBACK_PROMOTION_MATRIX_EXIT_RULE_ID
    lifecycle_baseline = _first_row_matching(
        lifecycle_replay,
        {
            "condition_test_id": "baseline_replay",
            "exit_rule_id": exit_rule_id,
            "anomaly_exclusion_basis": PRICE_PULLBACK_PROMOTION_MATRIX_ANOMALY_BASIS,
        },
    )
    base_package = _first_row_matching(
        lifecycle_replay,
        {
            "condition_test_id": "v1_gate_return20_tdcc_high_obv",
            "exit_rule_id": exit_rule_id,
            "anomaly_exclusion_basis": PRICE_PULLBACK_PROMOTION_MATRIX_ANOMALY_BASIS,
        },
    )
    rows: list[dict[str, object]] = [
        _promotion_row(
            generated_at=generated_at,
            matrix_order=0,
            promotion_candidate_id="baseline:production_proxy_lifecycle_replay",
            promotion_axis="baseline_reference",
            source_artifact_id="price_pullback_23ema_lifecycle_replay",
            source_selector=(
                f"condition_test_id=baseline_replay;exit_rule_id={exit_rule_id};"
                f"anomaly_exclusion_basis={PRICE_PULLBACK_PROMOTION_MATRIX_ANOMALY_BASIS}"
            ),
            source_metric_basis=(
                "same_stock_active_position_suppressed; close-confirmed previous-20-day-high breakout, "
                "next-open exit"
            ),
            proposed_contract_role="comparison_anchor",
            proposed_score_points="",
            condition_rule="current production proxy replay only; no added 23EMA promotion gate",
            plain_conclusion_zh="這只是比較基準，不是升格後模型。",
            source_row=lifecycle_baseline,
            baseline_row=lifecycle_baseline,
        ),
        _promotion_row(
            generated_at=generated_at,
            matrix_order=10,
            promotion_candidate_id="base_package:v1_gate_return20_tdcc_high_obv",
            promotion_axis="base_required_gate_package",
            source_artifact_id="price_pullback_23ema_lifecycle_replay",
            source_selector=(
                f"condition_test_id=v1_gate_return20_tdcc_high_obv;exit_rule_id={exit_rule_id};"
                f"anomaly_exclusion_basis={PRICE_PULLBACK_PROMOTION_MATRIX_ANOMALY_BASIS}"
            ),
            source_metric_basis=(
                "same_stock_active_position_suppressed; close-confirmed previous-20-day-high breakout, "
                "next-open exit"
            ),
            proposed_contract_role="base_model_candidate_required_gate_package",
            proposed_score_points="required_package",
            condition_rule=(
                "price_pullback_23ema signal plus return20_0_25, TDCC high thresholds up, "
                "and OBV above MA20"
            ),
            plain_conclusion_zh=(
                "這是目前最適合拿來討論的 23EMA 基礎模型候選：候選數仍可用，勝率、失敗率與報酬都優於原始 proxy。"
            ),
            source_row=base_package,
            baseline_row=lifecycle_baseline,
        ),
    ]

    ordered_specs = [
        (
            20,
            "supporting_gate:return20_0_25",
            "chip_technical_package",
            "return20_0_25",
            "base_gate_component_candidate",
            "+0_required_package_component",
            "20 日漲幅 0%~25% 是基礎包的一部分；單獨看不是最強，但可避免買到過度延伸後回檔。",
        ),
        (
            30,
            "supporting_gate:tdcc_high_thresholds_up",
            "chip_technical_package",
            "tdcc_high_thresholds_up",
            "base_gate_component_candidate",
            "+0_required_package_component",
            "TDCC 大戶門檻上升是目前最有用的籌碼條件之一，適合放在基礎包或強加分包。",
        ),
        (
            40,
            "supporting_gate:obv_above_ma20",
            "chip_technical_package",
            "obv_above_ma20",
            "base_gate_component_candidate",
            "+0_required_package_component",
            "OBV 高於 MA20 單獨不是完整模型，但與 TDCC/漲幅限制搭配後能改善品質。",
        ),
        (
            50,
            "technical_package:macd_kd_confirm",
            "chip_technical_package",
            "macd_kd_confirm",
            "reject_as_required_gate_candidate",
            "0",
            "MACD/KD 確認單獨沒有穩定改善，暫時不能當必要條件，只能留作輔助觀察。",
        ),
        (
            60,
            "structure_package:pattern45_bull_pullback",
            "price_structure_package",
            "pattern45_bull_pullback",
            "add_score_package_candidate",
            "+1_review",
            "45 日多頭回檔結構改善勝率與報酬，可作加分包候選，但仍需搭配基礎包討論。",
        ),
        (
            70,
            "research_score:score_ge6",
            "chip_technical_package",
            "research_score_ge6",
            "strict_add_score_package_review",
            "+2_review",
            "既有技術/籌碼研究分數高分桶有較佳品質，但不能直接取代明確條件包。",
        ),
    ]
    for order, candidate_id, axis, condition_id, role, points, conclusion in ordered_specs:
        source_row = _first_row_matching(
            ordered_condition_matrix,
            {
                "condition_test_id": condition_id,
                "exit_rule_id": exit_rule_id,
                "anomaly_exclusion_basis": PRICE_PULLBACK_PROMOTION_MATRIX_ANOMALY_BASIS,
            },
        )
        rows.append(
            _promotion_row(
                generated_at=generated_at,
                matrix_order=order,
                promotion_candidate_id=candidate_id,
                promotion_axis=axis,
                source_artifact_id="price_pullback_23ema_ordered_condition_matrix",
                source_selector=(
                    f"condition_test_id={condition_id};exit_rule_id={exit_rule_id};"
                    f"anomaly_exclusion_basis={PRICE_PULLBACK_PROMOTION_MATRIX_ANOMALY_BASIS}"
                ),
                source_metric_basis="same buy/sell rule, no same-stock lifecycle suppression in ordered condition matrix",
                proposed_contract_role=role,
                proposed_score_points=points,
                condition_rule=safe_str(_row_value(source_row, "condition_rule", "")),
                plain_conclusion_zh=conclusion,
                source_row=source_row,
                baseline_row=lifecycle_baseline,
            )
        )

    revenue_specs = [
        (
            100,
            "revenue_package:latest30_and_cumulative20",
            "revenue_strength_package",
            "latest30_and_cumulative20",
            "strong_add_score_package_candidate_not_required_gate",
            "+2_review",
            "營收最新 YoY >=30% 且累計 YoY >=20% 表現較好，適合作強加分包候選，不適合先當必要條件。",
        ),
        (
            110,
            "revenue_package:latest_revenue_yoy_ge50",
            "revenue_strength_package",
            "latest_revenue_yoy_ge50",
            "strong_add_score_candidate_small_sample_review",
            "+1_to_+2_review",
            "最新月營收 YoY >=50% 有觀察價值，但樣本較小，先當強加分覆核項。",
        ),
        (
            120,
            "revenue_package:latest_yoy_delta_ge20",
            "revenue_turnaround_package",
            "latest_yoy_delta_ge20",
            "weak_turnaround_add_score_review",
            "+1_weak_review",
            "營收 YoY 單月改善 20 個百分點有些改善，但不足以當必要條件。",
        ),
        (
            130,
            "revenue_reject:latest_yoy_turn_positive_after_2_negative",
            "revenue_turnaround_package",
            "latest_yoy_turn_positive_after_2_negative",
            "reject_as_required_gate_or_add_score",
            "0",
            "由負轉正這個概念在目前 23EMA 樣本沒有變好，暫時不能加分。",
        ),
        (
            140,
            "risk_tag:revenue_negative_both",
            "revenue_risk_tag",
            "revenue_negative_both_risk",
            "risk_tag_candidate_review",
            "-1_review",
            "最新與累計營收 YoY 都為負可列風險標籤，但目前不能單靠它排除股票。",
        ),
    ]
    revenue_baseline = _first_row_matching(
        revenue_condition_matrix,
        {
            "condition_test_id": "base_v1_without_revenue_gate",
            "anomaly_exclusion_basis": "excluding_known_price_or_revenue_anomalies",
        },
    )
    for order, candidate_id, axis, condition_id, role, points, conclusion in revenue_specs:
        source_row = _first_row_matching(
            revenue_condition_matrix,
            {
                "condition_test_id": condition_id,
                "anomaly_exclusion_basis": "excluding_known_price_or_revenue_anomalies",
            },
        )
        rows.append(
            _promotion_row(
                generated_at=generated_at,
                matrix_order=order,
                promotion_candidate_id=candidate_id,
                promotion_axis=axis,
                source_artifact_id="price_pullback_23ema_revenue_condition_matrix",
                source_selector=(
                    f"condition_test_id={condition_id};"
                    "anomaly_exclusion_basis=excluding_known_price_or_revenue_anomalies"
                ),
                source_metric_basis=(
                    "base v1 lifecycle replay with source_table_date <= signal_date monthly revenue join; "
                    "known numerical anomalies excluded"
                ),
                proposed_contract_role=role,
                proposed_score_points=points,
                condition_rule=safe_str(_row_value(source_row, "condition_rule", "")),
                plain_conclusion_zh=conclusion,
                source_row=source_row,
                baseline_row=revenue_baseline if not revenue_baseline.empty else lifecycle_baseline,
            )
        )

    high_return_specs = [
        (
            200,
            "high_return_score:score_ge2",
            "high_return_structure_score",
            "score_ge_2",
            "add_score_package_candidate",
            "+1_review",
            "高報酬結構分 >=2 開始改善高報酬率與平均報酬，可作加分門檻候選。",
        ),
        (
            210,
            "high_return_score:score_ge3",
            "high_return_structure_score",
            "score_ge_3",
            "strong_add_score_package_candidate",
            "+2_review",
            "高報酬結構分 >=3 是較平衡的加分包候選，報酬改善明顯但失敗率仍需控管。",
        ),
        (
            220,
            "high_return_score:score_ge5",
            "high_return_structure_score",
            "score_ge_5",
            "aggressive_high_return_package_review",
            "+3_aggressive_review",
            "高報酬結構分 >=5 報酬最高但樣本較小，適合積極加分覆核，不適合當必要條件。",
        ),
    ]
    high_return_baseline = _first_row_matching(
        high_return_score_grid,
        {
            "score_bucket": "all_scores",
            "exit_rule_id": exit_rule_id,
            "anomaly_exclusion_basis": "excluding_known_data_quality_exceptions",
        },
    )
    for order, candidate_id, axis, score_bucket, role, points, conclusion in high_return_specs:
        source_row = _first_row_matching(
            high_return_score_grid,
            {
                "score_bucket": score_bucket,
                "exit_rule_id": exit_rule_id,
                "anomaly_exclusion_basis": "excluding_known_data_quality_exceptions",
            },
        )
        rows.append(
            _promotion_row(
                generated_at=generated_at,
                matrix_order=order,
                promotion_candidate_id=candidate_id,
                promotion_axis=axis,
                source_artifact_id="price_pullback_23ema_high_return_feature_score_grid",
                source_selector=(
                    f"score_bucket={score_bucket};exit_rule_id={exit_rule_id};"
                    "anomaly_exclusion_basis=excluding_known_data_quality_exceptions"
                ),
                source_metric_basis="base v1 package with known data-quality exceptions excluded",
                proposed_contract_role=role,
                proposed_score_points=points,
                condition_rule=safe_str(_row_value(source_row, "score_rule_summary", "")),
                plain_conclusion_zh=conclusion,
                source_row=source_row,
                baseline_row=high_return_baseline if not high_return_baseline.empty else base_package,
            )
        )

    for component in PRICE_PULLBACK_HIGH_RETURN_FEATURE_SCORE_COMPONENTS:
        component_id = safe_str(component["component_id"])
        points = float(component.get("points", 0))
        role = "risk_tag_candidate_review" if points < 0 else "score_component_candidate"
        conclusion = (
            "帶量紅 K 或實體紅 K 在目前賣法下不能保證品質，先列風險標籤，不作買點加分。"
            if points < 0
            else "這是高報酬結構分的組成項，需透過 score grid 分桶確認後才可進正式評分。"
        )
        rows.append(
            _promotion_row(
                generated_at=generated_at,
                matrix_order=300 + len(rows),
                promotion_candidate_id=f"score_component:{component_id}",
                promotion_axis="high_return_score_component_definition",
                source_artifact_id="price_pullback_23ema_high_return_feature_score_grid",
                source_selector=f"component_id={component_id}",
                source_metric_basis="component definition used by high-return score grid",
                proposed_contract_role=role,
                proposed_score_points=safe_str(component.get("points", "")),
                condition_rule=safe_str(component.get("component_rule", "")),
                plain_conclusion_zh=conclusion,
                source_row=pd.Series(dtype=object),
                baseline_row=high_return_baseline if not high_return_baseline.empty else base_package,
                data_status="component_definition_no_direct_trade_sample",
            )
        )

    rows.append(
        _promotion_row(
            generated_at=generated_at,
            matrix_order=900,
            promotion_candidate_id="deferred_context:theme_leadership",
            promotion_axis="deferred_context",
            source_artifact_id="price_pullback_23ema_ordered_condition_matrix",
            source_selector=(
                f"condition_test_id=theme_context_mainstream_supported;exit_rule_id={exit_rule_id};"
                f"anomaly_exclusion_basis={PRICE_PULLBACK_PROMOTION_MATRIX_ANOMALY_BASIS}"
            ),
            source_metric_basis="theme point-in-time join exists but D+20 mature outcome sample is not ready",
            proposed_contract_role="defer_until_mature_point_in_time_theme_samples",
            proposed_score_points="0_deferred",
            condition_rule="theme/leadership support requires signal-date point-in-time theme context before scoring",
            plain_conclusion_zh="熱門族群條件已接資料，但成熟樣本不足，現在不能當加分或必要條件。",
            source_row=_first_row_matching(
                ordered_condition_matrix,
                {
                    "condition_test_id": "theme_context_mainstream_supported",
                    "exit_rule_id": exit_rule_id,
                    "anomaly_exclusion_basis": PRICE_PULLBACK_PROMOTION_MATRIX_ANOMALY_BASIS,
                },
            ),
            baseline_row=lifecycle_baseline,
        )
    )
    out = pd.DataFrame(rows, columns=PRICE_PULLBACK_PROMOTION_MATRIX_COLUMNS)
    return out.sort_values("matrix_order").reset_index(drop=True)


def write_price_pullback_promotion_matrix(matrix: pd.DataFrame) -> None:
    write_csv(matrix, PRICE_PULLBACK_PROMOTION_MATRIX_CSV)
    write_csv(matrix, PRICE_PULLBACK_PROMOTION_MATRIX_HISTORY_CSV)
    write_csv(matrix, DOCS_PRICE_PULLBACK_PROMOTION_MATRIX_CSV)
    lines = [
        "# Price Pullback 23EMA Promotion Matrix",
        "",
        f"- generated_at: `{now_text()}`",
        "- model_id: `price_pullback_23ema`",
        "- status: `research_only_promotion_decision_matrix`; this does not change production condition, scoring, ranking, PDF, or contract registry.",
        "- proposed_base: `price_pullback_23ema` signal + `return20_0_25` + `TDCC high thresholds up` + `OBV above MA20`.",
        "- operation_basis: signal-date close confirmation, next trading day open entry, close-confirmed previous-20-day-high breakout, next trading day open exit.",
        "- anomaly_basis: main lifecycle, ordered-condition, and high-return rows use `excluding_known_data_quality_exceptions`; revenue rows use `excluding_known_price_or_revenue_anomalies`.",
        "- PDF rule: metrics are not PDF-ready until formal promotion and model-owned operation adapter/metric contract are approved.",
        "",
        markdown_table(
            matrix,
            [
                "promotion_axis",
                "promotion_candidate_id",
                "proposed_contract_role",
                "proposed_score_points",
                "sample_status",
                "anomaly_exclusion_basis",
                "known_metric_exception_count_in_sample",
                "accepted_trade_count",
                "accepted_avg_trades_per_research_day",
                "win_rate_pct",
                "failure_rate_pct",
                "avg_realized_return_pct",
                "median_realized_return_pct",
                "high_return_10_rate_pct",
                "loss_5_rate_pct",
                "plain_conclusion_zh",
            ],
            limit=120,
        )
        if not matrix.empty
        else "No promotion matrix rows.",
    ]
    PRICE_PULLBACK_PROMOTION_MATRIX_MD.write_text(
        "\n".join(lines).rstrip() + "\n",
        encoding="utf-8",
        newline="\n",
    )
    DOCS_PRICE_PULLBACK_PROMOTION_MATRIX_MD.write_text(
        PRICE_PULLBACK_PROMOTION_MATRIX_MD.read_text(encoding="utf-8"),
        encoding="utf-8",
        newline="\n",
    )


def _price_pullback_parity_discussion_status(row_parity: pd.DataFrame) -> dict[str, object]:
    if row_parity.empty or "parity_status" not in row_parity.columns:
        return {
            "daily_row_parity_status_summary": "missing_price_pullback_row_parity_audit",
            "daily_row_parity_exact_pass_count": 0,
            "daily_row_parity_blocked_count": 0,
            "daily_row_parity_blocker_summary": "price_pullback daily row parity artifact is missing",
        }
    counts = row_parity["parity_status"].map(safe_str).value_counts()
    blocked = row_parity[~row_parity["parity_status"].map(safe_str).eq("exact_daily_row_parity_pass")]
    blocker_values = (
        blocked["parity_blocker"].map(safe_str).replace("", pd.NA).dropna().unique().tolist()
        if "parity_blocker" in blocked.columns
        else []
    )
    return {
        "daily_row_parity_status_summary": ";".join(f"{status}:{int(count)}" for status, count in counts.items()),
        "daily_row_parity_exact_pass_count": int(counts.get("exact_daily_row_parity_pass", 0)),
        "daily_row_parity_blocked_count": int(len(blocked)),
        "daily_row_parity_blocker_summary": "; ".join(blocker_values[:3]),
    }


def _price_pullback_decision_status(row: dict[str, object]) -> tuple[str, str]:
    item_id = safe_str(row.get("decision_item_id", ""))
    test_status = safe_str(row.get("test_status", ""))
    feature_family = safe_str(row.get("feature_family", ""))
    mature = _numeric_or_nan(row.get("mature_count", ""))
    win_delta = _numeric_or_nan(row.get("delta_vs_baseline_win_rate_pct", ""))
    failure_delta = _numeric_or_nan(row.get("delta_vs_baseline_failure_rate_pct", ""))
    avg_delta = _numeric_or_nan(row.get("delta_vs_baseline_avg_realized_return_pct", ""))

    if item_id == "baseline:production_replay_operation_anchor":
        return (
            "baseline_anchor",
            "作為比較基準；不是正式買賣模組，仍需 promotion PR 才能升格。",
        )
    if test_status != "tested_point_in_time":
        if feature_family == "revenue":
            return (
                "blocked_data_gap_required_before_gate",
                "營收可以當必要條件或加分討論，但目前缺 point-in-time 歷史營收 panel，不能先寫進 production。",
            )
        if feature_family == "market_background":
            return (
                "blocked_market_join_required",
                "大盤背景方向合理，但需要把 market regime 依 signal_date 接到個股 research frame 後才能評估。",
            )
        return ("blocked_data_gap", "資料或 join 尚未完成，不能視為已回測條件。")
    uses_coverage_limited_revenue = (
        feature_family == "revenue"
        or "revenue" in item_id
        or "revenue" in str(row.get("data_status", ""))
    ) and "coverage_limited" in str(row.get("data_status", ""))
    if uses_coverage_limited_revenue:
        return (
            "coverage_limited_score_discussion_not_required_gate",
            "營收資料已可做 coverage-limited research-only 觀察；因不是完整 release-date 歷史 panel，暫時只能當加分討論，不能升正式必要條件。",
        )
    if math.isnan(mature) or mature < MIN_REVIEW_SAMPLE:
        return ("insufficient_sample_review_only", "樣本不足，只能列為觀察，不能當必要條件。")
    if "tdcc_high_thresholds_up_return20_0_25_obv_above_ma20" in item_id:
        if (
            (not math.isnan(win_delta) and win_delta > 0)
            or (not math.isnan(failure_delta) and failure_delta < 0)
            or (not math.isnan(avg_delta) and avg_delta > 0)
        ):
            return (
                "score_bonus_candidate_not_required_gate",
                "OBV above MA20 對已篩出的 TDCC/20日報酬條件有加分討論價值，但目前定位是加分項，不是必要條件。",
            )
    if not math.isnan(win_delta) and not math.isnan(failure_delta):
        if win_delta >= 5.0 and failure_delta <= -3.0:
            if not math.isnan(avg_delta) and avg_delta < 0:
                return (
                    "score_bonus_candidate_winrate_tradeoff",
                    "勝率與失敗率改善，但平均實現報酬低於 baseline；較適合討論加分，不適合直接當硬 gate。",
                )
            return (
                "score_bonus_candidate",
                "相對 baseline 改善勝率與失敗率，可優先討論作為加分或 ranking 權重。",
            )
        if win_delta <= -3.0 and failure_delta >= 3.0:
            return (
                "reject_as_required_gate",
                "相對 baseline 勝率下降且失敗率上升，不適合升成必要條件。",
            )
        if not math.isnan(avg_delta) and avg_delta > 0 and (win_delta < 0 or failure_delta > 0):
            return (
                "return_up_but_riskier_not_gate",
                "平均報酬提高但勝率或失敗率變差，若保留只能當高波動加分候選，不適合硬篩。",
            )
        if win_delta > 0 or failure_delta < 0:
            return (
                "mixed_discussion_candidate",
                "有部分指標優於 baseline，但改善不夠完整，適合進入討論而非直接升格。",
            )
    if not math.isnan(avg_delta) and avg_delta > 0:
        return (
            "return_only_discussion_candidate",
            "平均報酬高於 baseline，但勝率/失敗率沒有同步改善，需人工判斷是否符合模型目標。",
        )
    return ("no_observed_improvement", "目前沒有相對 baseline 的明確優勢。")


def _price_pullback_feature_condition_role(feature_row: pd.Series) -> str:
    feature_id = safe_str(feature_row.get("feature_filter_id", ""))
    family = safe_str(feature_row.get("feature_family", ""))
    if feature_id == "tdcc_high_thresholds_up_return20_0_25_obv_above_ma20":
        return "score_bonus_candidate_not_required_gate"
    if "theme_context" in feature_id or "theme_context" in family:
        return "point_in_time_context_score_bonus_candidate_not_required_gate"
    if family == "revenue" or "revenue" in feature_id or "revenue" in family:
        return "coverage_limited_context_score_bonus_candidate_not_required_gate"
    return "possible_required_gate_or_score_bonus"


def _price_pullback_decision_row_from_metrics(
    *,
    generated_at: str,
    source_artifact_id: str,
    decision_axis: str,
    decision_item_id: str,
    feature_family: str,
    condition_role: str,
    rule_text: str,
    test_status: str,
    data_status: str,
    row: pd.Series,
    baseline: pd.Series,
    parity: dict[str, object],
) -> dict[str, object]:
    out: dict[str, object] = {
        "generated_at": generated_at,
        "model_id": "price_pullback_23ema",
        "model_name_zh": "股價回檔模型",
        "research_artifact_id": "price_pullback_23ema_model_decision_audit",
        "source_artifact_id": source_artifact_id,
        "decision_axis": decision_axis,
        "decision_item_id": decision_item_id,
        "feature_family": feature_family,
        "condition_role": condition_role,
        "condition_rule": rule_text,
        "test_status": test_status,
        "data_status": data_status,
        "fixed_operation_module_candidate_id": PRICE_PULLBACK_FEATURE_CONFIRMATION_OPERATION_ID,
        "buy_point_rule": safe_str(row.get("buy_point_rule", baseline.get("buy_point_rule", ""))),
        "target_rule": safe_str(row.get("target_rule", baseline.get("target_rule", ""))),
        "stop_rule": safe_str(row.get("stop_rule", baseline.get("stop_rule", ""))),
        "exit_rule": safe_str(row.get("exit_rule", baseline.get("exit_rule", ""))),
        "win_definition": safe_str(row.get("win_definition", baseline.get("win_definition", ""))),
        "neutral_definition": safe_str(row.get("neutral_definition", baseline.get("neutral_definition", ""))),
        "failure_definition": safe_str(row.get("failure_definition", baseline.get("failure_definition", ""))),
        "selected_stock_days": row.get("selected_stock_days", ""),
        "selected_unique_stocks": row.get("selected_unique_stocks", ""),
        "mature_count": row.get("mature_count", ""),
        "selected_share_of_baseline_pct": _share_pct_or_blank(
            row.get("selected_stock_days", ""),
            baseline.get("selected_stock_days", ""),
        ),
        "mature_share_of_baseline_pct": _share_pct_or_blank(
            row.get("mature_count", ""),
            baseline.get("mature_count", ""),
        ),
        "win_rate_pct": row.get("win_rate_pct", ""),
        "neutral_rate_pct": row.get("neutral_rate_pct", ""),
        "failure_rate_pct": row.get("failure_rate_pct", ""),
        "same_day_unresolved_rate_pct": row.get("same_day_unresolved_rate_pct", ""),
        "avg_realized_return_pct": row.get("avg_realized_return_pct", ""),
        "avg_d20_close_return_pct": row.get("avg_d20_close_return_pct", ""),
        "avg_realized_or_d20_days": row.get("avg_realized_or_d20_days", ""),
        "delta_vs_baseline_win_rate_pct": _delta_or_blank(row.get("win_rate_pct", ""), baseline.get("win_rate_pct", "")),
        "delta_vs_baseline_failure_rate_pct": _delta_or_blank(
            row.get("failure_rate_pct", ""), baseline.get("failure_rate_pct", "")
        ),
        "delta_vs_baseline_avg_realized_return_pct": _delta_or_blank(
            row.get("avg_realized_return_pct", ""), baseline.get("avg_realized_return_pct", "")
        ),
        "delta_vs_baseline_avg_realized_or_d20_days": _delta_or_blank(
            row.get("avg_realized_or_d20_days", ""), baseline.get("avg_realized_or_d20_days", "")
        ),
        "advisory_status": "not_production_ready_research_only",
        "approved_for_daily": False,
        "production_change": "none",
        "promotion_blocker": "requires explicit model promotion PR with exact research parity, contract update, validators, and post-merge validation",
        **parity,
    }
    if decision_item_id == "baseline:production_replay_operation_anchor":
        out["selected_share_of_baseline_pct"] = 100.0
        out["mature_share_of_baseline_pct"] = 100.0
        for col in [
            "delta_vs_baseline_win_rate_pct",
            "delta_vs_baseline_failure_rate_pct",
            "delta_vs_baseline_avg_realized_return_pct",
            "delta_vs_baseline_avg_realized_or_d20_days",
        ]:
            out[col] = 0.0
    status, conclusion = _price_pullback_decision_status(out)
    out["decision_status"] = status
    out["plain_conclusion_zh"] = conclusion
    return out


def build_price_pullback_model_decision_audit(
    operation_module: pd.DataFrame,
    feature_confirmation: pd.DataFrame,
    row_parity: pd.DataFrame,
) -> pd.DataFrame:
    generated = now_text()
    columns = [
        "generated_at",
        "model_id",
        "model_name_zh",
        "research_artifact_id",
        "source_artifact_id",
        "decision_axis",
        "decision_item_id",
        "feature_family",
        "condition_role",
        "condition_rule",
        "test_status",
        "data_status",
        "fixed_operation_module_candidate_id",
        "buy_point_rule",
        "target_rule",
        "stop_rule",
        "exit_rule",
        "win_definition",
        "neutral_definition",
        "failure_definition",
        "selected_stock_days",
        "selected_unique_stocks",
        "mature_count",
        "selected_share_of_baseline_pct",
        "mature_share_of_baseline_pct",
        "win_rate_pct",
        "neutral_rate_pct",
        "failure_rate_pct",
        "same_day_unresolved_rate_pct",
        "avg_realized_return_pct",
        "avg_d20_close_return_pct",
        "avg_realized_or_d20_days",
        "delta_vs_baseline_win_rate_pct",
        "delta_vs_baseline_failure_rate_pct",
        "delta_vs_baseline_avg_realized_return_pct",
        "delta_vs_baseline_avg_realized_or_d20_days",
        "decision_status",
        "plain_conclusion_zh",
        "advisory_status",
        "approved_for_daily",
        "production_change",
        "daily_row_parity_status_summary",
        "daily_row_parity_exact_pass_count",
        "daily_row_parity_blocked_count",
        "daily_row_parity_blocker_summary",
        "promotion_blocker",
    ]
    if operation_module.empty:
        return pd.DataFrame(columns=columns)

    op = operation_module[
        operation_module["operation_module_candidate_id"].astype(str).eq(PRICE_PULLBACK_FEATURE_CONFIRMATION_OPERATION_ID)
    ].copy()
    if op.empty:
        return pd.DataFrame(columns=columns)
    baseline_rows = op[op["entry_filter_id"].astype(str).eq("baseline_replay")]
    if baseline_rows.empty:
        return pd.DataFrame(columns=columns)
    baseline = baseline_rows.iloc[0]
    parity = _price_pullback_parity_discussion_status(row_parity)

    rows: list[dict[str, object]] = [
        _price_pullback_decision_row_from_metrics(
            generated_at=generated,
            source_artifact_id="price_pullback_23ema_operation_module_research",
            decision_axis="baseline_operation",
            decision_item_id="baseline:production_replay_operation_anchor",
            feature_family="baseline",
            condition_role="comparison_anchor",
            rule_text="current production proxy replay; no extra entry or feature filter",
            test_status="tested_point_in_time",
            data_status="available_point_in_time_research_frame",
            row=baseline,
            baseline=baseline,
            parity=parity,
        )
    ]

    for _, entry_row in op[~op["entry_filter_id"].astype(str).eq("baseline_replay")].iterrows():
        rows.append(
            _price_pullback_decision_row_from_metrics(
                generated_at=generated,
                source_artifact_id="price_pullback_23ema_operation_module_research",
                decision_axis="entry_filter",
                decision_item_id=f"entry_filter:{safe_str(entry_row.get('entry_filter_id', ''))}",
                feature_family="entry_filter",
                condition_role="possible_buy_gate_or_score_bonus",
                rule_text=safe_str(entry_row.get("entry_signal_rule", "")),
                test_status="tested_point_in_time",
                data_status="available_point_in_time_research_frame",
                row=entry_row,
                baseline=baseline,
                parity=parity,
            )
        )

    if not feature_confirmation.empty:
        features = feature_confirmation[
            ~feature_confirmation["feature_filter_id"].astype(str).eq("baseline_replay")
        ].copy()
        for _, feature_row in features.iterrows():
            status = safe_str(feature_row.get("feature_test_status", ""))
            rows.append(
                _price_pullback_decision_row_from_metrics(
                    generated_at=generated,
                    source_artifact_id="price_pullback_23ema_feature_confirmation_research",
                    decision_axis="feature_filter",
                    decision_item_id=f"feature_filter:{safe_str(feature_row.get('feature_filter_id', ''))}",
                    feature_family=safe_str(feature_row.get("feature_family", "")),
                    condition_role=_price_pullback_feature_condition_role(feature_row),
                    rule_text=safe_str(feature_row.get("feature_rule", "")),
                    test_status=status,
                    data_status=safe_str(feature_row.get("data_status", "")),
                    row=feature_row,
                    baseline=baseline,
                    parity=parity,
                )
            )

    return pd.DataFrame(rows, columns=columns)


def write_price_pullback_model_decision_audit(decision: pd.DataFrame) -> None:
    write_csv(decision, PRICE_PULLBACK_DECISION_AUDIT_CSV)
    write_csv(decision, PRICE_PULLBACK_DECISION_AUDIT_HISTORY_CSV)
    write_csv(decision, DOCS_PRICE_PULLBACK_DECISION_AUDIT_CSV)
    status_counts = (
        decision["decision_status"].value_counts().reset_index()
        if not decision.empty and "decision_status" in decision.columns
        else pd.DataFrame(columns=["decision_status", "count"])
    )
    if not status_counts.empty:
        status_counts.columns = ["decision_status", "count"]
    lines = [
        "# Price Pullback 23EMA Model Decision Audit",
        "",
        f"- generated_at: `{now_text()}`",
        "- model_id: `price_pullback_23ema`",
        "- status: `discussion_ready_research_only`; this does not change production condition, scoring, ranking, or contract registry",
        f"- fixed_operation_module_candidate_id: `{PRICE_PULLBACK_FEATURE_CONFIRMATION_OPERATION_ID}`",
        "- buy_point: current production proxy signal plus the tested entry/feature filter on signal date; buy next open only after both hold",
        "- sell_point: first intraday breakout above signal-day previous 20-day high before stop through D+20",
        "- stop: close stays at least 4% below the lower of 20MA and 23EMA for 4 consecutive trading days, then exit at the next trading day open",
        "- model_decision_use: compare baseline, volume red K, prior extension, chip, technical, theme context, 45d structure, revenue gap, and market-background gap in one table",
        "- obv_scope: OBV combo rows are score-bonus candidates, not required gates.",
        "- theme_context_scope: theme context rows are point-in-time coverage-limited score-bonus discussion candidates, not production gates.",
        "- rule: rows marked `reject_as_required_gate` must not become production gates without new evidence; blocked rows require data joins before scoring",
        "",
        "## Decision Status Counts",
        "",
        markdown_table(status_counts, status_counts.columns.tolist()) if not status_counts.empty else "No decision rows.",
        "",
        "## Decision Rows",
        "",
        markdown_table(
            decision,
            [
                "decision_axis",
                "decision_item_id",
                "feature_family",
                "selected_share_of_baseline_pct",
                "mature_count",
                "win_rate_pct",
                "delta_vs_baseline_win_rate_pct",
                "failure_rate_pct",
                "delta_vs_baseline_failure_rate_pct",
                "avg_realized_return_pct",
                "delta_vs_baseline_avg_realized_return_pct",
                "avg_realized_or_d20_days",
                "decision_status",
                "plain_conclusion_zh",
            ],
            limit=120,
        ),
    ]
    PRICE_PULLBACK_DECISION_AUDIT_MD.write_text(
        "\n".join(lines).rstrip() + "\n",
        encoding="utf-8",
        newline="\n",
    )
    DOCS_PRICE_PULLBACK_DECISION_AUDIT_MD.write_text(
        PRICE_PULLBACK_DECISION_AUDIT_MD.read_text(encoding="utf-8"),
        encoding="utf-8",
        newline="\n",
    )


def _stock_id_sample(values: set[str], limit: int = 12) -> str:
    return ";".join(sorted(values)[:limit])


def _snapshot_date_from_path(path: Path) -> str:
    return normalize_date(path.stem.rsplit("_", 1)[-1])


def _value_counts_summary(series: pd.Series, limit: int = 8) -> str:
    if series.empty:
        return ""
    cleaned = series.map(lambda value: safe_str(value).strip() or "(blank)")
    counts = cleaned.value_counts()
    return ";".join(f"{key}:{int(count)}" for key, count in counts.head(limit).items())


def _all_candidates_snapshot_path(snapshot_dir: Path, report_date: str) -> Path:
    return snapshot_dir / f"all_candidates_{report_date}.csv"


def _price_pullback_candidate_universe_replay(
    snapshot_dir: Path,
    report_date: str,
) -> dict[str, object]:
    path = _all_candidates_snapshot_path(snapshot_dir, report_date)
    if not path.exists():
        return {
            "comparison_basis": "full_research_frame_proxy",
            "comparison_stock_ids": None,
            "candidate_universe_replay_status": "missing_historical_all_candidates_source_row_snapshot",
            "candidate_universe_snapshot_path": "",
            "candidate_universe_source_row_count": "",
            "candidate_universe_condition_stock_count": "",
            "candidate_universe_missing_required_columns": "",
            "replay_error": "",
        }

    try:
        candidates = pd.read_csv(path, dtype=str, keep_default_na=False).fillna("")
    except Exception as exc:
        return {
            "comparison_basis": "production_all_candidates_source_row_replay",
            "comparison_stock_ids": set(),
            "candidate_universe_replay_status": "blocked_unreadable_all_candidates_source_row_snapshot",
            "candidate_universe_snapshot_path": path.as_posix(),
            "candidate_universe_source_row_count": "",
            "candidate_universe_condition_stock_count": "",
            "candidate_universe_missing_required_columns": "",
            "replay_error": str(exc),
        }

    missing = sorted(PRICE_PULLBACK_CANDIDATE_REPLAY_REQUIRED_COLUMNS - set(candidates.columns))
    if missing:
        return {
            "comparison_basis": "production_all_candidates_source_row_replay",
            "comparison_stock_ids": set(),
            "candidate_universe_replay_status": "blocked_invalid_all_candidates_source_row_schema",
            "candidate_universe_snapshot_path": path.as_posix(),
            "candidate_universe_source_row_count": len(candidates),
            "candidate_universe_condition_stock_count": "",
            "candidate_universe_missing_required_columns": ";".join(missing),
            "replay_error": "",
        }

    mask = candidates.apply(cond_pullback, axis=1).fillna(False)
    matched = candidates.loc[mask].copy()
    stock_ids = {normalize_code(value) for value in matched["stock_id"].tolist()}
    stock_ids.discard("")
    return {
        "comparison_basis": "production_all_candidates_source_row_replay",
        "comparison_stock_ids": stock_ids,
        "candidate_universe_replay_status": "candidate_universe_replay_available",
        "candidate_universe_snapshot_path": path.as_posix(),
        "candidate_universe_source_row_count": len(candidates),
        "candidate_universe_condition_stock_count": len(stock_ids),
        "candidate_universe_missing_required_columns": "",
        "replay_error": "",
    }


def _price_pullback_gap_driver(
    *,
    has_research_date: bool,
    comparison_basis: str,
    published_unique: int,
    published_not_proxy_count: int,
    proxy_not_published_count: int,
) -> str:
    if not has_research_date:
        return "missing_research_frame_date"
    if published_not_proxy_count == 0 and proxy_not_published_count == 0:
        return "none_exact"
    if comparison_basis == "production_all_candidates_source_row_replay":
        if published_not_proxy_count and proxy_not_published_count:
            return "production_candidate_universe_bidirectional_row_gap"
        if published_not_proxy_count:
            return "published_rows_not_reproduced_by_production_candidate_universe_replay"
        return "production_candidate_universe_rows_not_in_published_snapshot"
    if proxy_not_published_count > max(published_unique, published_not_proxy_count):
        return "research_full_universe_proxy_exceeds_daily_candidate_publication_scope"
    if published_not_proxy_count and proxy_not_published_count:
        return "bidirectional_proxy_and_publication_gap"
    if published_not_proxy_count:
        return "published_rows_not_reproduced_by_research_proxy"
    return "research_proxy_rows_not_in_published_snapshot"


def _published_not_proxy_interpretation(count: int, comparison_basis: str) -> str:
    if count <= 0:
        return ""
    if comparison_basis == "production_all_candidates_source_row_replay":
        return (
            "published rows do not satisfy the production all_candidates cond_pullback replay; "
            "inspect dated source-row schema, merge keys, and condition drift before promotion"
        )
    return (
        "published rows do not satisfy the current research proxy; inspect feature parity, "
        "dated source columns, and snapshot lifecycle before promotion"
    )


def _proxy_not_published_interpretation(count: int, comparison_basis: str) -> str:
    if count <= 0:
        return ""
    if comparison_basis == "production_all_candidates_source_row_replay":
        return (
            "production all_candidates cond_pullback replay found stocks not on the published report surface; "
            "inspect report publication scope, duplicate merge, and dated snapshot alignment"
        )
    return (
        "research proxy runs on the full stock-day frame, while daily production starts from "
        "all_candidates/source-row eligibility and then writes the published report surface"
    )


def build_price_pullback_daily_row_parity_audit(
    df: pd.DataFrame,
    snapshot_dir: Path = DAILY_SNAPSHOT_DIR,
    generated_at: str | None = None,
) -> pd.DataFrame:
    generated = generated_at or now_text()
    columns = [
        "generated_at",
        "model_id",
        "snapshot_report_date",
        "research_frame_has_date",
        "outcome_research_frame_has_date",
        "source_row_research_frame_has_date",
        "research_frame_date_basis",
        "published_row_count",
        "published_unique_stock_count",
        "published_duplicate_stock_count",
        "research_proxy_unique_stock_count",
        "overlap_stock_count",
        "published_not_in_proxy_rows",
        "proxy_not_published_rows",
        "published_proxy_coverage_pct",
        "proxy_publish_precision_pct",
        "published_not_in_proxy_sample",
        "proxy_not_published_sample",
        "parity_scope",
        "published_surface",
        "research_proxy_scope",
        "comparison_basis",
        "candidate_universe_snapshot_path",
        "candidate_universe_source_row_count",
        "candidate_universe_condition_stock_count",
        "candidate_universe_missing_required_columns",
        "published_selection_semantics_values",
        "published_source_category_counts",
        "published_report_bucket_counts",
        "candidate_universe_replay_status",
        "parity_gap_driver",
        "published_not_in_proxy_interpretation",
        "proxy_not_published_interpretation",
        "next_required_replay_artifact",
        "parity_status",
        "parity_blocker",
    ]
    if df.empty:
        return pd.DataFrame(columns=columns)

    research = df.copy()
    research["_row_parity_date"] = research["date"].map(normalize_date)
    research["_row_parity_stock_id"] = research["stock_id"].map(normalize_code)
    outcome_research_dates = set(research["_row_parity_date"].astype(str))
    proxy_mask = current_price_pullback_approved_operation_baseline(research).fillna(False)
    proxy_rows = research.loc[
        proxy_mask
        & research["_row_parity_date"].astype(str).ne("")
        & research["_row_parity_stock_id"].astype(str).ne(""),
        ["_row_parity_date", "_row_parity_stock_id"],
    ].drop_duplicates()
    proxy_by_date = {
        date: set(part["_row_parity_stock_id"].astype(str))
        for date, part in proxy_rows.groupby("_row_parity_date")
    }

    rows: list[dict[str, object]] = []
    for snapshot_path in sorted(snapshot_dir.glob("daily_candidate_model_signals_for_report_*.csv")):
        report_date = _snapshot_date_from_path(snapshot_path)
        if not report_date:
            continue
        try:
            snapshot = pd.read_csv(snapshot_path, dtype=str, keep_default_na=False)
        except Exception as exc:
            rows.append(
                {
                    "generated_at": generated,
                    "model_id": "price_pullback_23ema",
                    "snapshot_report_date": report_date,
                    "research_frame_has_date": "False",
                    "outcome_research_frame_has_date": "False",
                    "source_row_research_frame_has_date": "False",
                    "research_frame_date_basis": "missing_research_frame_date",
                    "published_row_count": 0,
                    "published_unique_stock_count": 0,
                    "published_duplicate_stock_count": 0,
                    "research_proxy_unique_stock_count": 0,
                    "overlap_stock_count": 0,
                    "published_not_in_proxy_rows": 0,
                    "proxy_not_published_rows": 0,
                    "published_proxy_coverage_pct": "",
                    "proxy_publish_precision_pct": "",
                    "published_not_in_proxy_sample": "",
                    "proxy_not_published_sample": "",
                    "parity_scope": "signal_date_stock_id",
                    "published_surface": "daily_candidate_model_signals_for_report",
                    "research_proxy_scope": "full_stock_day_frame_current_price_pullback_baseline_proxy_without_daily_candidate_universe_replay",
                    "comparison_basis": "unavailable_published_snapshot",
                    "candidate_universe_snapshot_path": "",
                    "candidate_universe_source_row_count": "",
                    "candidate_universe_condition_stock_count": "",
                    "candidate_universe_missing_required_columns": "",
                    "published_selection_semantics_values": "",
                    "published_source_category_counts": "",
                    "published_report_bucket_counts": "",
                    "candidate_universe_replay_status": "blocked_unreadable_snapshot",
                    "parity_gap_driver": "unreadable_snapshot",
                    "published_not_in_proxy_interpretation": "",
                    "proxy_not_published_interpretation": "",
                    "next_required_replay_artifact": "readable published snapshot before candidate-universe replay can be assessed",
                    "parity_status": "blocked_unreadable_snapshot",
                    "parity_blocker": f"failed to read published daily snapshot: {exc}",
                }
            )
            continue

        if not {"model_id", "stock_id"}.issubset(snapshot.columns):
            rows.append(
                {
                    "generated_at": generated,
                    "model_id": "price_pullback_23ema",
                    "snapshot_report_date": report_date,
                    "research_frame_has_date": "False",
                    "outcome_research_frame_has_date": "False",
                    "source_row_research_frame_has_date": "False",
                    "research_frame_date_basis": "missing_research_frame_date",
                    "published_row_count": 0,
                    "published_unique_stock_count": 0,
                    "published_duplicate_stock_count": 0,
                    "research_proxy_unique_stock_count": 0,
                    "overlap_stock_count": 0,
                    "published_not_in_proxy_rows": 0,
                    "proxy_not_published_rows": 0,
                    "published_proxy_coverage_pct": "",
                    "proxy_publish_precision_pct": "",
                    "published_not_in_proxy_sample": "",
                    "proxy_not_published_sample": "",
                    "parity_scope": "signal_date_stock_id",
                    "published_surface": "daily_candidate_model_signals_for_report",
                    "research_proxy_scope": "full_stock_day_frame_current_price_pullback_baseline_proxy_without_daily_candidate_universe_replay",
                    "comparison_basis": "unavailable_published_snapshot",
                    "candidate_universe_snapshot_path": "",
                    "candidate_universe_source_row_count": "",
                    "candidate_universe_condition_stock_count": "",
                    "candidate_universe_missing_required_columns": "",
                    "published_selection_semantics_values": "",
                    "published_source_category_counts": "",
                    "published_report_bucket_counts": "",
                    "candidate_universe_replay_status": "blocked_invalid_snapshot_schema",
                    "parity_gap_driver": "invalid_snapshot_schema",
                    "published_not_in_proxy_interpretation": "",
                    "proxy_not_published_interpretation": "",
                    "next_required_replay_artifact": "valid published snapshot with model_id and stock_id",
                    "parity_status": "blocked_invalid_snapshot_schema",
                    "parity_blocker": "published daily snapshot missing model_id or stock_id",
                }
            )
            continue

        published = snapshot[snapshot["model_id"].astype(str).eq("price_pullback_23ema")].copy()
        published_stock_ids = [normalize_code(value) for value in published["stock_id"].tolist()]
        published_stock_ids = [stock_id for stock_id in published_stock_ids if stock_id]
        published_set = set(published_stock_ids)
        candidate_replay = _price_pullback_candidate_universe_replay(snapshot_dir, report_date)
        comparison_basis = safe_str(candidate_replay.get("comparison_basis", "")) or "full_research_frame_proxy"
        candidate_replay_set = candidate_replay.get("comparison_stock_ids")
        source_row_research_has_date = (
            comparison_basis == "production_all_candidates_source_row_replay"
            and isinstance(candidate_replay_set, set)
            and not safe_str(candidate_replay.get("replay_error", ""))
        )
        if isinstance(candidate_replay_set, set):
            proxy_set = candidate_replay_set
        else:
            proxy_set = proxy_by_date.get(report_date, set())
        overlap = published_set & proxy_set
        published_not_proxy = published_set - proxy_set
        proxy_not_published = proxy_set - published_set
        published_unique = len(published_set)
        proxy_unique = len(proxy_set)
        outcome_research_has_date = report_date in outcome_research_dates
        has_research_date = outcome_research_has_date or source_row_research_has_date
        date_basis_parts: list[str] = []
        if outcome_research_has_date:
            date_basis_parts.append("outcome_research_frame")
        if source_row_research_has_date:
            date_basis_parts.append("production_all_candidates_source_row_replay")
        research_frame_date_basis = ";".join(date_basis_parts) if date_basis_parts else "missing_research_frame_date"
        published_not_proxy_count = len(published_not_proxy)
        proxy_not_published_count = len(proxy_not_published)
        gap_driver = _price_pullback_gap_driver(
            has_research_date=has_research_date,
            comparison_basis=comparison_basis,
            published_unique=published_unique,
            published_not_proxy_count=published_not_proxy_count,
            proxy_not_published_count=proxy_not_published_count,
        )
        candidate_replay_status = safe_str(candidate_replay.get("candidate_universe_replay_status", ""))
        if comparison_basis == "production_all_candidates_source_row_replay" and candidate_replay_status == "candidate_universe_replay_available":
            candidate_replay_status = (
                "candidate_universe_replay_exact_match"
                if not published_not_proxy and not proxy_not_published
                else "candidate_universe_replay_row_gap"
            )

        if not has_research_date:
            parity_status = "blocked_missing_research_frame_date"
            parity_blocker = "research frame does not include this published snapshot date"
        elif published_not_proxy or proxy_not_published:
            parity_status = "blocked_not_exact_daily_row_parity"
            parity_blocker = (
                "research proxy does not exactly reproduce as-published daily price_pullback_23ema rows; "
                "daily candidate-universe/source-row eligibility and report publication scope must be replayed before promotion"
            )
        else:
            parity_status = "exact_daily_row_parity_pass"
            parity_blocker = ""

        rows.append(
            {
                "generated_at": generated,
                "model_id": "price_pullback_23ema",
                "snapshot_report_date": report_date,
                "research_frame_has_date": "True" if has_research_date else "False",
                "outcome_research_frame_has_date": "True" if outcome_research_has_date else "False",
                "source_row_research_frame_has_date": "True" if source_row_research_has_date else "False",
                "research_frame_date_basis": research_frame_date_basis,
                "published_row_count": len(published),
                "published_unique_stock_count": published_unique,
                "published_duplicate_stock_count": len(published_stock_ids) - published_unique,
                "research_proxy_unique_stock_count": proxy_unique,
                "overlap_stock_count": len(overlap),
                "published_not_in_proxy_rows": published_not_proxy_count,
                "proxy_not_published_rows": proxy_not_published_count,
                "published_proxy_coverage_pct": (
                    round(len(overlap) / published_unique * 100.0, 2) if published_unique else ""
                ),
                "proxy_publish_precision_pct": round(len(overlap) / proxy_unique * 100.0, 2) if proxy_unique else "",
                "published_not_in_proxy_sample": _stock_id_sample(published_not_proxy),
                "proxy_not_published_sample": _stock_id_sample(proxy_not_published),
                "parity_scope": "signal_date_stock_id",
                "published_surface": "daily_candidate_model_signals_for_report",
                "research_proxy_scope": (
                    "production_all_candidates_source_row_cond_pullback_replay"
                    if comparison_basis == "production_all_candidates_source_row_replay"
                    else "full_stock_day_frame_current_price_pullback_baseline_proxy_without_daily_candidate_universe_replay"
                ),
                "comparison_basis": comparison_basis,
                "candidate_universe_snapshot_path": candidate_replay.get("candidate_universe_snapshot_path", ""),
                "candidate_universe_source_row_count": candidate_replay.get("candidate_universe_source_row_count", ""),
                "candidate_universe_condition_stock_count": candidate_replay.get(
                    "candidate_universe_condition_stock_count", ""
                ),
                "candidate_universe_missing_required_columns": candidate_replay.get(
                    "candidate_universe_missing_required_columns", ""
                ),
                "published_selection_semantics_values": _value_counts_summary(
                    published["selection_semantics"] if "selection_semantics" in published.columns else pd.Series(dtype=str)
                ),
                "published_source_category_counts": _value_counts_summary(
                    published["original_category"] if "original_category" in published.columns else pd.Series(dtype=str)
                ),
                "published_report_bucket_counts": _value_counts_summary(
                    published["report_bucket"] if "report_bucket" in published.columns else pd.Series(dtype=str)
                ),
                "candidate_universe_replay_status": candidate_replay_status,
                "parity_gap_driver": gap_driver,
                "published_not_in_proxy_interpretation": _published_not_proxy_interpretation(
                    published_not_proxy_count, comparison_basis
                ),
                "proxy_not_published_interpretation": _proxy_not_published_interpretation(
                    proxy_not_published_count, comparison_basis
                ),
                "next_required_replay_artifact": (
                    "historical all_candidates/source-row snapshot with candidate_source_type, "
                    "candidate_line, report eligibility, source_row_index, and the exact model input columns"
                ),
                "parity_status": parity_status,
                "parity_blocker": parity_blocker,
            }
        )
    return pd.DataFrame(rows, columns=columns)


def write_price_pullback_daily_row_parity_audit(row_parity: pd.DataFrame) -> None:
    write_csv(row_parity, PRICE_PULLBACK_DAILY_ROW_PARITY_CSV)
    write_csv(row_parity, PRICE_PULLBACK_DAILY_ROW_PARITY_HISTORY_CSV)
    write_csv(row_parity, DOCS_PRICE_PULLBACK_DAILY_ROW_PARITY_CSV)
    counts = (
        row_parity["parity_status"].value_counts().reset_index()
        if not row_parity.empty and "parity_status" in row_parity.columns
        else pd.DataFrame(columns=["parity_status", "count"])
    )
    if not counts.empty:
        counts.columns = ["parity_status", "count"]
    lines = [
        "# Price Pullback 23EMA Daily Row Parity Audit",
        "",
        f"- generated_at: `{now_text()}`",
        "- model_id: `price_pullback_23ema`",
        "- scope: compare as-published daily snapshot rows to the research production proxy at `signal_date + stock_id` level",
        "- rule: any missing or extra stock row keeps the model blocked from daily operation promotion",
        "- gap interpretation: the research proxy currently runs on the full stock-day frame; exact parity still needs dated daily candidate-universe/source-row replay before promotion",
        "- date rule: `outcome_research_frame_has_date` tracks mature next-open/D+N outcome rows; `source_row_research_frame_has_date` tracks dated all_candidates/source-row replay for as-of daily row parity.",
        "- note: this audit does not change production selection, scoring, ranking, or PDF output",
        "",
        "## Status Summary",
        "",
        markdown_table(counts, counts.columns.tolist()) if not counts.empty else "No parity rows.",
        "",
        "## Snapshot Detail",
        "",
        markdown_table(
            row_parity,
            [
                "snapshot_report_date",
                "research_frame_has_date",
                "outcome_research_frame_has_date",
                "source_row_research_frame_has_date",
                "research_frame_date_basis",
                "published_unique_stock_count",
                "research_proxy_unique_stock_count",
                "overlap_stock_count",
                "published_not_in_proxy_rows",
                "proxy_not_published_rows",
                "published_proxy_coverage_pct",
                "proxy_publish_precision_pct",
                "parity_gap_driver",
                "comparison_basis",
                "candidate_universe_condition_stock_count",
                "candidate_universe_replay_status",
                "parity_status",
                "parity_blocker",
            ],
            limit=120,
        ),
    ]
    PRICE_PULLBACK_DAILY_ROW_PARITY_MD.write_text(
        "\n".join(lines).rstrip() + "\n",
        encoding="utf-8",
        newline="\n",
    )
    DOCS_PRICE_PULLBACK_DAILY_ROW_PARITY_MD.write_text(
        PRICE_PULLBACK_DAILY_ROW_PARITY_MD.read_text(encoding="utf-8"),
        encoding="utf-8",
        newline="\n",
    )


def write_model_parity(parity: pd.DataFrame) -> None:
    write_csv(parity, OUT_PARITY_CSV)
    write_csv(parity, DOCS_PARITY_CSV)
    counts = (
        parity["research_baseline_status"].value_counts().reset_index()
        if not parity.empty
        else pd.DataFrame(columns=["research_baseline_status", "count"])
    )
    if not counts.empty:
        counts.columns = ["research_baseline_status", "count"]
    lines = [
        "# Daily Model Research Baseline Parity",
        "",
        f"- generated_at: `{now_text()}`",
        "- purpose: verify that every daily production core model has a research production-baseline row before parameter variants are compared",
        "- production_parity: historical research fields can replay the production baseline directly",
        "- production_proxy / proxy_only: baseline exists, but one or more production fields are not fully available point-in-time in the research frame",
        "- rule: variants must compare against the production_baseline row of the same model_id; proxy rows cannot be promoted without resolving blockers",
        "",
        "## Status Summary",
        "",
        markdown_table(counts, counts.columns.tolist()) if not counts.empty else "No parity rows.",
        "",
        "## Model Parity Detail",
        "",
        markdown_table(
            parity,
            [
                "model_id",
                "research_baseline_status",
                "research_baseline_parameter_set_id",
                "research_variant_count",
                "baseline_selected_stock_days",
                "baseline_selected_unique_stocks",
                "parity_blocker",
                "completion_rule",
            ],
            limit=80,
        ),
    ]
    OUT_PARITY_MD.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8", newline="\n")
    DOCS_PARITY_MD.write_text(OUT_PARITY_MD.read_text(encoding="utf-8"), encoding="utf-8", newline="\n")


def write_markdown(summary: pd.DataFrame, detail: pd.DataFrame, coverage: dict[str, object]) -> None:
    summary_sorted = summary.sort_values(
        ["model_id", "sample_status", "best_avg_close_return_pct"],
        ascending=[True, True, False],
    ).reset_index(drop=True)
    review = summary_sorted[summary_sorted["selected_stock_days"] >= MIN_REVIEW_SAMPLE].copy()
    top = review.sort_values(["best_avg_close_return_pct", "selected_stock_days"], ascending=[False, False]).head(30)
    lines = [
        "# Daily Model Parameter Research",
        "",
        f"- generated_at: `{now_text()}`",
        f"- price_history_files: `{coverage.get('price_history_files')}`",
        f"- max_price_rows: `{coverage.get('max_price_rows')}`",
        f"- data_range: `{coverage.get('date_min')}` ~ `{coverage.get('date_max')}`",
        "- entry_basis: `signal_date_next_open`",
        "- close_return_definition: `(D+n close / next trading day open - 1)`",
        "- high_return_definition: `(max intraday high through D+n / next trading day open - 1)`",
        "",
        "## Data Quality",
        "",
        "- This is first-pass parameter research using the current repo price history.",
        "- If sample_status is `small_sample_review_only` or `insufficient_sample`, do not treat the parameter as a final model weight.",
        "- Revenue historical panel is not complete in price history, so the revenue-unreacted research row only validates the price-range component.",
        "",
        "## Top Parameter Sets By Avg Close Return",
        "",
        markdown_table(
            top,
            [
                "model_id",
                "parameter_set_id",
                "parameter_role",
                "production_parity_status",
                "selected_stock_days",
                "selected_unique_stocks",
                "best_close_horizon_d1_d10",
                "best_close_win_rate_pct",
                "best_avg_close_return_pct",
                "sample_status",
                "parameter_summary",
            ],
            limit=30,
        ),
        "",
        "## All Model Parameter Summary",
        "",
        markdown_table(
            summary_sorted,
            [
                "model_id",
                "parameter_set_id",
                "parameter_role",
                "production_parity_status",
                "selected_stock_days",
                "d1_close_win_rate_pct",
                "d3_close_win_rate_pct",
                "d5_close_win_rate_pct",
                "d10_close_win_rate_pct",
                "d5_avg_close_return_pct",
                "d10_avg_close_return_pct",
                "sample_status",
                "parameter_summary",
            ],
            limit=200,
        ),
    ]
    OUT_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")
    DOCS_LATEST_DIR.mkdir(parents=True, exist_ok=True)
    DOCS_MD.write_text(OUT_MD.read_text(encoding="utf-8"), encoding="utf-8")

    focus = detail[detail["horizon"].isin(["D+1", "D+2", "D+3", "D+4", "D+5", "D+6", "D+7", "D+8", "D+9", "D+10"])].copy()
    lines2 = [
        "# Daily Model Parameter Research - Horizon Detail",
        "",
        f"- generated_at: `{now_text()}`",
        "- entry_basis: `signal_date_next_open`",
        "",
        markdown_table(
            focus,
            [
                "model_id",
                "parameter_set_id",
                "horizon",
                "mature_count",
                "close_win_rate_pct",
                "avg_close_return_pct",
                "median_close_return_pct",
                "avg_high_return_pct",
                "high_5pct_hit_rate_pct",
            ],
            limit=300,
        ),
    ]
    OUT_DETAIL_MD.write_text("\n".join(lines2) + "\n", encoding="utf-8")
    DOCS_DETAIL_MD.write_text(OUT_DETAIL_MD.read_text(encoding="utf-8"), encoding="utf-8")


def coverage_stats() -> dict[str, object]:
    rows = []
    for path in Path("data/stock_price_history").glob("*.csv"):
        try:
            df = pd.read_csv(path, usecols=["date"])
        except Exception:
            continue
        if df.empty:
            continue
        rows.append((len(df), str(df["date"].min()), str(df["date"].max())))
    if not rows:
        return {"price_history_files": 0, "max_price_rows": 0, "date_min": "", "date_max": ""}
    return {
        "price_history_files": len(rows),
        "max_price_rows": max(r[0] for r in rows),
        "date_min": min(r[1] for r in rows),
        "date_max": max(r[2] for r in rows),
    }


def main() -> int:
    print("Building research frame", flush=True)
    df = build_research_frame()
    if df.empty:
        raise RuntimeError("No price history available for model parameter research")

    print("Building daily model parameter summaries", flush=True)
    summaries: list[dict[str, object]] = []
    details: list[dict[str, object]] = []
    for spec in rule_specs():
        summary, detail_rows = summarize_rule(df, spec)
        summaries.append(summary)
        details.extend(detail_rows)

    summary_df = pd.DataFrame(summaries)
    detail_df = pd.DataFrame(details)
    coverage = coverage_stats()
    parity_df = build_model_parity(summary_df)
    print("Building price_pullback operation research", flush=True)
    price_pullback_operation_df = build_price_pullback_operation_research(df)
    print("Building price_pullback time cost backtest", flush=True)
    price_pullback_time_cost_df = build_price_pullback_time_cost_backtest(df)
    print("Building price_pullback operation module research", flush=True)
    price_pullback_operation_module_df = build_price_pullback_operation_module_research(df)
    print("Building price_pullback feature confirmation research", flush=True)
    price_pullback_feature_confirmation_df = build_price_pullback_feature_confirmation_research(df)
    print("Building price_pullback exit rule comparison", flush=True)
    price_pullback_exit_rule_comparison_df = build_price_pullback_exit_rule_comparison(df)
    print("Building price_pullback continuation win profile", flush=True)
    price_pullback_continuation_win_profile_df = build_price_pullback_continuation_win_profile(df)
    print("Building price_pullback research score bucket", flush=True)
    price_pullback_research_score_bucket_df = build_price_pullback_research_score_bucket(df)
    print("Building price_pullback high-return feature score grid", flush=True)
    price_pullback_high_return_score_grid_df = build_price_pullback_high_return_feature_score_grid(df)
    print("Building price_pullback revenue condition matrix", flush=True)
    price_pullback_revenue_condition_matrix_df = build_price_pullback_revenue_condition_matrix(df)
    print("Building revenue_unreacted_range revenue condition matrix", flush=True)
    revenue_unreacted_condition_matrix_df = build_revenue_unreacted_range_revenue_condition_matrix(df)
    print("Building revenue_unreacted_range operation candidate matrix", flush=True)
    revenue_unreacted_operation_candidate_matrix_df = build_revenue_unreacted_range_operation_candidate_matrix(df)
    print("Building price_pullback ordered condition matrix", flush=True)
    price_pullback_ordered_condition_matrix_df = build_price_pullback_ordered_condition_matrix(df)
    print("Building price_pullback lifecycle replay", flush=True)
    price_pullback_lifecycle_replay_df = build_price_pullback_lifecycle_replay(df)
    print("Building price_pullback daily row parity audit", flush=True)
    price_pullback_daily_row_parity_df = build_price_pullback_daily_row_parity_audit(df)
    print("Building price_pullback model decision audit", flush=True)
    price_pullback_decision_audit_df = build_price_pullback_model_decision_audit(
        price_pullback_operation_module_df,
        price_pullback_feature_confirmation_df,
        price_pullback_daily_row_parity_df,
    )
    print("Building price_pullback promotion matrix", flush=True)
    price_pullback_promotion_matrix_df = build_price_pullback_promotion_matrix(
        price_pullback_lifecycle_replay_df,
        price_pullback_ordered_condition_matrix_df,
        price_pullback_high_return_score_grid_df,
        price_pullback_revenue_condition_matrix_df,
    )

    write_csv(summary_df, OUT_CSV)
    write_csv(detail_df, OUT_DETAIL_CSV)
    HISTORY_DIR.mkdir(parents=True, exist_ok=True)
    write_csv(summary_df, HISTORY_CSV)
    DOCS_LATEST_DIR.mkdir(parents=True, exist_ok=True)
    write_csv(summary_df, DOCS_CSV)
    write_csv(detail_df, DOCS_DETAIL_CSV)
    write_markdown(summary_df, detail_df, coverage)
    write_model_parity(parity_df)
    write_price_pullback_operation_research(price_pullback_operation_df)
    write_price_pullback_time_cost_backtest(price_pullback_time_cost_df)
    write_price_pullback_operation_module_research(price_pullback_operation_module_df)
    write_price_pullback_feature_confirmation_research(price_pullback_feature_confirmation_df)
    write_price_pullback_exit_rule_comparison(price_pullback_exit_rule_comparison_df)
    write_price_pullback_continuation_win_profile(price_pullback_continuation_win_profile_df)
    write_price_pullback_research_score_bucket(price_pullback_research_score_bucket_df)
    write_price_pullback_high_return_feature_score_grid(price_pullback_high_return_score_grid_df)
    write_price_pullback_revenue_condition_matrix(price_pullback_revenue_condition_matrix_df)
    write_revenue_unreacted_range_revenue_condition_matrix(revenue_unreacted_condition_matrix_df)
    write_revenue_unreacted_range_operation_candidate_matrix(revenue_unreacted_operation_candidate_matrix_df)
    write_price_pullback_ordered_condition_matrix(price_pullback_ordered_condition_matrix_df)
    write_price_pullback_lifecycle_replay(price_pullback_lifecycle_replay_df)
    write_price_pullback_daily_row_parity_audit(price_pullback_daily_row_parity_df)
    write_price_pullback_model_decision_audit(price_pullback_decision_audit_df)
    write_price_pullback_promotion_matrix(price_pullback_promotion_matrix_df)

    print(f"Saved {OUT_CSV} rows={len(summary_df)}")
    print(f"Saved {OUT_DETAIL_CSV} rows={len(detail_df)}")
    print(f"Saved {OUT_PARITY_CSV} rows={len(parity_df)}")
    print(f"Saved {PRICE_PULLBACK_OPERATION_CSV} rows={len(price_pullback_operation_df)}")
    print(f"Saved {PRICE_PULLBACK_TIME_COST_CSV} rows={len(price_pullback_time_cost_df)}")
    print(f"Saved {PRICE_PULLBACK_OPERATION_MODULE_CSV} rows={len(price_pullback_operation_module_df)}")
    print(f"Saved {PRICE_PULLBACK_FEATURE_CONFIRMATION_CSV} rows={len(price_pullback_feature_confirmation_df)}")
    print(f"Saved {PRICE_PULLBACK_EXIT_RULE_COMPARISON_CSV} rows={len(price_pullback_exit_rule_comparison_df)}")
    print(f"Saved {PRICE_PULLBACK_CONTINUATION_WIN_PROFILE_CSV} rows={len(price_pullback_continuation_win_profile_df)}")
    print(f"Saved {PRICE_PULLBACK_RESEARCH_SCORE_BUCKET_CSV} rows={len(price_pullback_research_score_bucket_df)}")
    print(f"Saved {PRICE_PULLBACK_HIGH_RETURN_SCORE_GRID_CSV} rows={len(price_pullback_high_return_score_grid_df)}")
    print(f"Saved {PRICE_PULLBACK_REVENUE_CONDITION_MATRIX_CSV} rows={len(price_pullback_revenue_condition_matrix_df)}")
    print(f"Saved {REVENUE_UNREACTED_CONDITION_MATRIX_CSV} rows={len(revenue_unreacted_condition_matrix_df)}")
    print(
        f"Saved {REVENUE_UNREACTED_OPERATION_CANDIDATE_MATRIX_CSV} "
        f"rows={len(revenue_unreacted_operation_candidate_matrix_df)}"
    )
    print(f"Saved {PRICE_PULLBACK_ORDERED_CONDITION_MATRIX_CSV} rows={len(price_pullback_ordered_condition_matrix_df)}")
    print(f"Saved {PRICE_PULLBACK_LIFECYCLE_REPLAY_CSV} rows={len(price_pullback_lifecycle_replay_df)}")
    print(f"Saved {PRICE_PULLBACK_DAILY_ROW_PARITY_CSV} rows={len(price_pullback_daily_row_parity_df)}")
    print(f"Saved {PRICE_PULLBACK_DECISION_AUDIT_CSV} rows={len(price_pullback_decision_audit_df)}")
    print(f"Saved {PRICE_PULLBACK_PROMOTION_MATRIX_CSV} rows={len(price_pullback_promotion_matrix_df)}")
    print(f"Saved {OUT_MD}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

