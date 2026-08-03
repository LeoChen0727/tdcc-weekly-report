from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
import math
from pathlib import Path
from typing import Callable
from zoneinfo import ZoneInfo

import numpy as np
import pandas as pd

from revenue_unreacted_range_source_first_condition_audit import (
    FINANCIAL_STATEMENT_SCOPE,
    FIRST_HIT_DEADLINE_DAYS,
    OUTCOME_WINDOW_DAYS,
    PRICE_HISTORY_DIR,
    PRIMARY_VARIANT_ID,
    _load_price_resolutions,
    load_stock_price,
)
from revenue_unreacted_range_source_snapshot_projection import (
    CUTOFF_DATE as SOURCE_PROJECTION_CUTOFF_DATE,
    LATEST_DETAIL_CSV as SOURCE_DETAIL_CSV,
    LATEST_MANIFEST_CSV as SOURCE_PROJECTION_MANIFEST_CSV,
    load_projected_source_detail,
    load_source_snapshot_projection_manifest,
    validate_projection_binding,
)


ROOT = Path(__file__).resolve().parents[1]
MODEL_ID = "revenue_unreacted_range"
ARTIFACT_ID = "revenue_unreacted_range_forward_confirmation_feature_audit"
ARTIFACT_VERSION = "forward_confirmation_v2_20260713"
EXPECTED_SOURCE_ARTIFACT_ID = "revenue_unreacted_range_source_first_condition_audit"
EXPECTED_SOURCE_ARTIFACT_VERSION = "source_first_condition_v3_20260720"

SOURCE_PROJECTION_SUMMARY_COLUMNS = (
    "source_projection_artifact_id",
    "source_projection_artifact_version",
    "source_projection_id",
    "source_projection_version",
    "source_projection_policy_id",
    "source_projection_cutoff_date",
    "source_projection_episode_row_count",
    "source_projection_detail_semantic_sha256",
)

LATEST_CSV = ROOT / f"output/latest/research_backtest/{ARTIFACT_ID}_latest.csv"
DETAIL_CSV = ROOT / f"output/latest/research_backtest/{ARTIFACT_ID}_detail_latest.csv"
EVENT_DETAIL_CSV = ROOT / f"output/latest/research_backtest/{ARTIFACT_ID}_event_detail_latest.csv"
FEATURE_CSV = ROOT / f"output/latest/research_backtest/{ARTIFACT_ID}_feature_contrast_latest.csv"
RETURN_REVIEW_CSV = ROOT / f"output/latest/research_backtest/{ARTIFACT_ID}_operation_return_review_latest.csv"
LATEST_MD = ROOT / f"output/latest/research_backtest/{ARTIFACT_ID}_latest.md"
HISTORY_CSV = ROOT / f"output/history/research/{ARTIFACT_ID}.csv"
HISTORY_FEATURE_CSV = ROOT / f"output/history/research/{ARTIFACT_ID}_feature_contrast.csv"
HISTORY_RETURN_REVIEW_CSV = ROOT / f"output/history/research/{ARTIFACT_ID}_operation_return_review.csv"
DOCS_CSV = ROOT / f"docs/latest/{ARTIFACT_ID}_latest.csv"
DOCS_FEATURE_CSV = ROOT / f"docs/latest/{ARTIFACT_ID}_feature_contrast_latest.csv"
DOCS_RETURN_REVIEW_CSV = ROOT / f"docs/latest/{ARTIFACT_ID}_operation_return_review_latest.csv"
DOCS_MD = ROOT / f"docs/latest/{ARTIFACT_ID}_latest.md"

PRIMARY_ANALYSIS_BASIS = "primary_candidate_retaining"
SENSITIVITY_ANALYSIS_BASIS = "excluding_unresolved_anomaly_candidates_sensitivity"
ANALYSIS_BASES = (PRIMARY_ANALYSIS_BASIS, SENSITIVITY_ANALYSIS_BASIS)
OPERATION_RETURN_REVIEW_THRESHOLD_PCT = 80.0
OPERATION_RETURN_REVIEW_POLICY = (
    "absolute D+20 operation return >= 80% is a review trigger only; retain in primary metrics "
    "and do not assign anomaly disposition without bottom-level root-cause evidence"
)

KNOWN_CASES = {
    "4916": {
        "failure_date": "20251209",
        "success_date": "20260518",
    },
    "1303": {
        "success_date": "20260527",
    },
}

FEATURE_COLUMNS = (
    "stock_name",
    "market",
    "open",
    "high",
    "low",
    "close",
    "volume",
    "ma20",
    "ma60",
    "ma120",
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
    "range_width_23d_pct",
    "range_width_60d_pct",
    "close_position_120d_pct",
    "body_ratio",
    "close_location",
    "bullish_attack_candle",
    "solid_red_candle",
    "obv_above_ma20",
    "tdcc_history_available",
    "tdcc_consecutive_up_weeks",
    "high_thresholds_up",
    "all_thresholds_up",
    "four_thresholds_sync_up",
    "signal_market_regime",
    "full_monthly_revenue_context_ready",
    "full_monthly_revenue_period",
    "full_monthly_revenue_source_table_date",
    "full_monthly_revenue_latest_yoy_pct",
    "full_monthly_revenue_cumulative_yoy_pct",
    "full_monthly_revenue_prev1_latest_yoy_pct",
    "full_monthly_revenue_latest_yoy_delta_1m_pct_points",
    "full_monthly_revenue_cumulative_yoy_delta_1m_pct_points",
    "full_monthly_revenue_numerical_anomaly_flag",
)


@dataclass(frozen=True)
class RuleSpec:
    rule_order: int
    rule_id: str
    rule_family: str
    rule_definition: str
    trigger_window: int = 20
    trigger_mode: str = "cross"
    condition_ids: tuple[str, ...] = ()
    next_day_mode: str = "none"

    @property
    def information_cutoff(self) -> str:
        return "next_trading_day_close" if self.next_day_mode != "none" else "trigger_date_close"


RULE_SPECS = (
    RuleSpec(
        -10,
        "source_first_close_above_prev20_reference",
        "source_parity_reference",
        "source-first legacy reference: first episode day with close above the previous 20-day highest close",
        trigger_mode="level",
    ),
    RuleSpec(0, "first_close_cross_prev20", "baseline", "first close crossover above the previous 20-day highest close"),
    RuleSpec(10, "first_close_cross_prev40", "breakout_window", "first close crossover above the previous 40-day highest close", 40),
    RuleSpec(20, "first_close_cross_prev60", "breakout_window", "first close crossover above the previous 60-day highest close", 60),
    RuleSpec(30, "prev20_next_close_continuation", "close_confirmation", "20-day close crossover followed by next-day close above trigger close", next_day_mode="close_gt_trigger_close"),
    RuleSpec(40, "prev20_next_close_holds_breakout", "close_confirmation", "20-day close crossover followed by next-day close not below the trigger's previous 20-day highest close", next_day_mode="hold_previous_close_high"),
    RuleSpec(100, "prev20_volume_ge1_5", "volume", "20-day close crossover with volume ratio >= 1.5", condition_ids=("volume_ge1_5",)),
    RuleSpec(110, "prev20_volume_ge2", "volume", "20-day close crossover with volume ratio >= 2.0", condition_ids=("volume_ge2",)),
    RuleSpec(120, "prev20_ma60_gt_ma120", "technical", "20-day close crossover with MA60 > MA120", condition_ids=("ma60_gt_ma120",)),
    RuleSpec(130, "prev20_obv_above_ma20", "technical", "20-day close crossover with OBV above OBV MA20", condition_ids=("obv_above_ma20",)),
    RuleSpec(140, "prev20_kdj_bullish_not_extreme", "technical", "20-day close crossover with K > D, J > K, and J < 100", condition_ids=("kdj_bullish_not_extreme",)),
    RuleSpec(150, "prev20_close_above_ma20_ema23", "technical", "20-day close crossover with close above MA20 and EMA23", condition_ids=("close_above_ma20_ema23",)),
    RuleSpec(160, "prev20_return20_0_25", "price_momentum", "20-day close crossover with prior 20-day close return between 0% and 25%", condition_ids=("return20_0_25",)),
    RuleSpec(170, "prev20_range23_le15", "price_shape", "20-day close crossover with previous 23-day range width <= 15%", condition_ids=("range23_le15",)),
    RuleSpec(180, "prev20_solid_red_candle", "candle", "20-day close crossover with a solid red candle", condition_ids=("solid_red_candle",)),
    RuleSpec(200, "prev20_tdcc_high_thresholds_up", "tdcc", "20-day close crossover with TDCC high thresholds increasing", condition_ids=("tdcc_high_thresholds_up",)),
    RuleSpec(210, "prev20_tdcc_consecutive_up_ge1", "tdcc", "20-day close crossover with TDCC consecutive up weeks >= 1", condition_ids=("tdcc_consecutive_up_ge1",)),
    RuleSpec(220, "prev20_market_bull", "market_regime", "20-day close crossover in strong_bull or mild_bull market regime", condition_ids=("market_bull",)),
    RuleSpec(230, "prev20_revenue_lag_0_14", "revenue_freshness", "20-day close crossover 0-14 trading days after latest available qualifying revenue source", condition_ids=("revenue_lag_0_14",)),
    RuleSpec(240, "prev20_revenue_lag_15_30", "revenue_freshness", "20-day close crossover 15-30 trading days after latest available qualifying revenue source", condition_ids=("revenue_lag_15_30",)),
    RuleSpec(250, "prev20_revenue_lag_31_60", "revenue_freshness", "20-day close crossover 31-60 trading days after latest available qualifying revenue source", condition_ids=("revenue_lag_31_60",)),
    RuleSpec(260, "prev20_revenue_lag_61_90", "revenue_freshness", "20-day close crossover 61-90 trading days after latest available qualifying revenue source", condition_ids=("revenue_lag_61_90",)),
    RuleSpec(270, "prev20_revenue_lag_91_126", "revenue_freshness", "20-day close crossover 91-126 trading days after latest available qualifying revenue source", condition_ids=("revenue_lag_91_126",)),
    RuleSpec(300, "prev20_next_close_volume_ge1_5", "close_confirmation_combo", "next-day close continuation plus trigger-day volume ratio >= 1.5", condition_ids=("volume_ge1_5",), next_day_mode="close_gt_trigger_close"),
    RuleSpec(310, "prev20_next_close_ma60_gt_ma120", "close_confirmation_combo", "next-day close continuation plus trigger-day MA60 > MA120", condition_ids=("ma60_gt_ma120",), next_day_mode="close_gt_trigger_close"),
    RuleSpec(320, "prev20_next_close_obv_above_ma20", "close_confirmation_combo", "next-day close continuation plus trigger-day OBV above OBV MA20", condition_ids=("obv_above_ma20",), next_day_mode="close_gt_trigger_close"),
    RuleSpec(330, "prev20_next_close_kdj_bullish", "close_confirmation_combo", "next-day close continuation plus trigger-day KDJ bullish and not extreme", condition_ids=("kdj_bullish_not_extreme",), next_day_mode="close_gt_trigger_close"),
    RuleSpec(340, "prev20_next_close_tdcc_high", "close_confirmation_combo", "next-day close continuation plus TDCC high thresholds increasing", condition_ids=("tdcc_high_thresholds_up",), next_day_mode="close_gt_trigger_close"),
    RuleSpec(350, "prev20_next_close_market_bull", "close_confirmation_combo", "next-day close continuation plus bull market regime", condition_ids=("market_bull",), next_day_mode="close_gt_trigger_close"),
)


BINARY_FEATURE_SPECS = (
    (10, "breakout_prev40", "breakout", "trigger close is above previous 40-day highest close", "breakout_prev40", None),
    (20, "breakout_prev60", "breakout", "trigger close is above previous 60-day highest close", "breakout_prev60", None),
    (30, "next_close_continuation", "close_confirmation", "next-day close is above trigger close", "next_day_close_gt_trigger_close", "next_day_observed"),
    (40, "next_close_holds_breakout", "close_confirmation", "next-day close holds the trigger's previous 20-day highest close", "next_day_close_holds_previous_close_high", "next_day_observed"),
    (100, "volume_ge1_5", "volume", "trigger-day volume ratio >= 1.5", "volume_ge1_5", None),
    (110, "volume_ge2", "volume", "trigger-day volume ratio >= 2.0", "volume_ge2", None),
    (120, "ma60_gt_ma120", "technical", "MA60 > MA120", "ma60_gt_ma120", "ma120_observed"),
    (130, "obv_above_ma20", "technical", "OBV above OBV MA20", "obv_above_ma20", "obv_observed"),
    (140, "kdj_bullish_not_extreme", "technical", "K > D, J > K, and J < 100", "kdj_bullish_not_extreme", "kdj_observed"),
    (150, "close_above_ma20_ema23", "technical", "close above MA20 and EMA23", "close_above_ma20_ema23", "ma20_ema23_observed"),
    (160, "macd_hist_gt0", "technical", "MACD histogram > 0", "macd_hist_gt0", "macd_observed"),
    (170, "rsi14_40_70", "technical", "40 <= RSI14 <= 70", "rsi14_40_70", "rsi_observed"),
    (180, "rsi14_ge60", "technical", "RSI14 >= 60", "rsi14_ge60", "rsi_observed"),
    (190, "kdj_j_ge100", "technical_risk", "KDJ J >= 100", "kdj_j_ge100", "kdj_observed"),
    (200, "return20_0_25", "price_momentum", "20-day close return between 0% and 25%", "return20_0_25", "return20_observed"),
    (210, "range23_le15", "price_shape", "previous 23-day range width <= 15%", "range23_le15", "range23_observed"),
    (220, "position120_low_le40", "price_position", "close position in previous 120-day range <= 40%", "position120_low_le40", "position120_observed"),
    (230, "position120_mid_40_75", "price_position", "40% < close position in previous 120-day range <= 75%", "position120_mid_40_75", "position120_observed"),
    (240, "position120_high_gt75", "price_position", "close position in previous 120-day range > 75%", "position120_high_gt75", "position120_observed"),
    (250, "solid_red_candle", "candle", "solid red candle", "solid_red_candle", None),
    (300, "tdcc_high_thresholds_up", "tdcc", "TDCC high thresholds increasing", "tdcc_high_thresholds_up", "tdcc_observed"),
    (310, "tdcc_consecutive_up_ge1", "tdcc", "TDCC consecutive up weeks >= 1", "tdcc_consecutive_up_ge1", "tdcc_observed"),
    (320, "market_bull", "market_regime", "market regime is strong_bull or mild_bull", "market_bull", "market_observed"),
    (330, "market_correction_or_high_risk", "market_regime_risk", "market regime is correction or high_risk", "market_correction_or_high_risk", "market_observed"),
    (400, "revenue_latest_ge50", "monthly_revenue", "latest monthly revenue YoY >= 50%", "revenue_latest_ge50", "revenue_observed"),
    (410, "revenue_cumulative_ge30", "monthly_revenue", "cumulative monthly revenue YoY >= 30%", "revenue_cumulative_ge30", "revenue_observed"),
    (420, "revenue_two_month_yoy_ge15", "monthly_revenue", "latest and previous monthly revenue YoY >= 15%", "revenue_two_month_yoy_ge15", "revenue_two_month_observed"),
    (430, "revenue_lag_0_14", "revenue_freshness", "0-14 trading days after latest available revenue source", "revenue_lag_0_14", "revenue_lag_observed"),
    (440, "revenue_lag_15_30", "revenue_freshness", "15-30 trading days after latest available revenue source", "revenue_lag_15_30", "revenue_lag_observed"),
    (450, "revenue_lag_31_60", "revenue_freshness", "31-60 trading days after latest available revenue source", "revenue_lag_31_60", "revenue_lag_observed"),
    (460, "revenue_lag_61_90", "revenue_freshness", "61-90 trading days after latest available revenue source", "revenue_lag_61_90", "revenue_lag_observed"),
    (470, "revenue_lag_91_126", "revenue_freshness", "91-126 trading days after latest available revenue source", "revenue_lag_91_126", "revenue_lag_observed"),
)


NUMERIC_FEATURE_SPECS = (
    (10, "revenue_lag_trading_days", "revenue_freshness", "revenue_lag_trading_days"),
    (20, "revenue_latest_yoy_pct", "monthly_revenue", "revenue_latest_yoy_pct"),
    (30, "revenue_cumulative_yoy_pct", "monthly_revenue", "revenue_cumulative_yoy_pct"),
    (40, "revenue_latest_yoy_delta_1m", "monthly_revenue", "revenue_latest_yoy_delta_1m_pct_points"),
    (100, "return_5d_pct", "price_momentum", "return_5d_pct"),
    (110, "return_20d_pct", "price_momentum", "return_20d_pct"),
    (120, "volume_ratio_prev20", "volume", "volume_ratio_prev20"),
    (130, "range_width_23d_pct", "price_shape", "range_width_23d_pct"),
    (140, "range_width_60d_pct", "price_shape", "range_width_60d_pct"),
    (150, "close_position_120d_pct", "price_position", "close_position_120d_pct"),
    (160, "signal_body_pct", "candle", "signal_body_pct"),
    (170, "close_location_pct", "candle_advisory", "close_location_pct"),
    (200, "rsi14", "technical", "rsi14"),
    (210, "macd_hist", "technical", "macd_hist"),
    (220, "kd_k_value", "technical", "k_value"),
    (230, "kd_d_value", "technical", "d_value"),
    (240, "kdj_j_value", "technical", "kdj_j_value"),
    (250, "ema23_slope_5d_pct", "technical", "ema23_slope_5d_pct"),
    (260, "distance_to_ema23_pct", "technical", "distance_to_ema23_pct"),
    (270, "ma60_minus_ma120_pct", "technical", "ma60_minus_ma120_pct"),
    (280, "obv_slope_5d", "technical", "obv_slope_5d"),
    (300, "tdcc_consecutive_up_weeks", "tdcc", "tdcc_consecutive_up_weeks"),
    (400, "next_day_close_return_pct", "close_confirmation", "next_day_close_return_pct"),
)


RULE_DETAIL_EVENT_FIELDS = (
    "trigger_date",
    "trigger_close",
    "previous_20d_highest_close",
    "next_day_observed",
    "next_day_date",
    "next_day_close",
    "next_day_close_return_pct",
    "qualifying_revenue_source_date_asof",
)


def _now_text() -> str:
    return datetime.now(ZoneInfo("Asia/Taipei")).strftime("%Y-%m-%d %H:%M:%S Asia/Taipei")


def _normalize_stock_id(value: object) -> str:
    text = str(value).strip().replace(".0", "")
    return text.zfill(4) if text else ""


def _normalize_date(series: pd.Series) -> pd.Series:
    return series.astype(str).str.replace(r"\D", "", regex=True).str[:8]


def _bool_value(value: object) -> bool:
    return str(value).strip().lower() in {"true", "1", "yes"}


def _number(value: object) -> float | None:
    result = pd.to_numeric(value, errors="coerce")
    return None if pd.isna(result) else float(result)


def _stable(value: object, digits: int = 4) -> float | str:
    result = _number(value)
    return "" if result is None else round(result, digits)


def _rate(numerator: int, denominator: int) -> float | str:
    return round(numerator / denominator * 100.0, 4) if denominator else ""


def _mean(values: pd.Series) -> float | str:
    numeric = pd.to_numeric(values, errors="coerce").dropna()
    return round(float(numeric.mean()), 4) if len(numeric) else ""


def _median(values: pd.Series) -> float | str:
    numeric = pd.to_numeric(values, errors="coerce").dropna()
    return round(float(numeric.median()), 4) if len(numeric) else ""


def _pooled_effect(success: pd.Series, failure: pd.Series) -> float | str:
    left = pd.to_numeric(success, errors="coerce").dropna()
    right = pd.to_numeric(failure, errors="coerce").dropna()
    if len(left) < 2 or len(right) < 2:
        return ""
    denominator = len(left) + len(right) - 2
    variance = ((len(left) - 1) * left.var(ddof=1) + (len(right) - 1) * right.var(ddof=1)) / denominator
    if not np.isfinite(variance) or variance <= 0:
        return ""
    return round(float((left.mean() - right.mean()) / math.sqrt(variance)), 4)


def _normalize_source_detail(frame: pd.DataFrame) -> pd.DataFrame:
    frame = frame.copy()
    required = {
        "artifact_id",
        "artifact_version",
        "condition_variant_id",
        "episode_key",
        "stock_id",
        "stock_name",
        "episode_start_trade_date",
        "episode_start_source_date",
        "episode_end_date",
        "episode_status",
        "first_breakout_date",
        "first_breakout_outcome",
        "launch_date",
        "qualifying_source_revenue_anomaly_candidate_flag",
        "unresolved_price_path_candidate_flag",
        "same_stock_non_overlap_applied",
    }
    missing = sorted(required - set(frame.columns))
    if missing:
        raise RuntimeError(f"forward confirmation source detail is missing columns: {missing}")
    if set(frame["artifact_id"].astype(str)) != {EXPECTED_SOURCE_ARTIFACT_ID}:
        raise RuntimeError(
            "forward confirmation source artifact id drift: "
            f"expected={EXPECTED_SOURCE_ARTIFACT_ID}"
        )
    if set(frame["artifact_version"].astype(str)) != {
        EXPECTED_SOURCE_ARTIFACT_VERSION
    }:
        raise RuntimeError(
            "forward confirmation source artifact version drift: "
            f"expected={EXPECTED_SOURCE_ARTIFACT_VERSION}"
        )
    frame = frame.loc[frame["condition_variant_id"].eq(PRIMARY_VARIANT_ID)].copy()
    frame["stock_id"] = frame["stock_id"].map(_normalize_stock_id)
    for column in ("episode_start_trade_date", "episode_end_date", "first_breakout_date", "launch_date"):
        frame[column] = _normalize_date(frame[column])
    if frame["episode_key"].duplicated().any():
        raise RuntimeError("forward confirmation source detail has duplicate episode keys")
    if not frame["same_stock_non_overlap_applied"].map(_bool_value).all():
        raise RuntimeError("forward confirmation source detail is not non-overlap governed")
    return frame.sort_values(["stock_id", "episode_start_trade_date", "episode_key"], kind="mergesort").reset_index(drop=True)


def load_source_projection(
    *,
    detail_path: Path = SOURCE_DETAIL_CSV,
    manifest_path: Path = SOURCE_PROJECTION_MANIFEST_CSV,
) -> tuple[pd.DataFrame, pd.DataFrame]:
    manifest = load_source_snapshot_projection_manifest(Path(manifest_path))
    projected_detail = load_projected_source_detail(Path(detail_path))
    validate_projection_binding(
        manifest,
        projected_detail,
        expected_cutoff_date=SOURCE_PROJECTION_CUTOFF_DATE,
    )
    return manifest, projected_detail


def load_source_detail(
    path: Path = SOURCE_DETAIL_CSV,
    *,
    manifest_path: Path = SOURCE_PROJECTION_MANIFEST_CSV,
) -> pd.DataFrame:
    _manifest, projected_detail = load_source_projection(
        detail_path=path,
        manifest_path=manifest_path,
    )
    return _normalize_source_detail(projected_detail)


def _source_projection_summary_lineage(manifest: pd.DataFrame) -> dict[str, object]:
    if len(manifest) != 1:
        raise RuntimeError(
            "forward confirmation source projection manifest must have exactly one row"
        )
    row = manifest.iloc[0]
    return {
        "source_projection_artifact_id": str(row["artifact_id"]),
        "source_projection_artifact_version": str(row["artifact_version"]),
        "source_projection_id": str(row["projection_id"]),
        "source_projection_version": str(row["projection_version"]),
        "source_projection_policy_id": str(row["projection_policy_id"]),
        "source_projection_cutoff_date": str(row["cutoff_date"]),
        "source_projection_episode_row_count": int(row["projected_episode_row_count"]),
        "source_projection_detail_semantic_sha256": str(
            row["projected_episode_semantic_sha256"]
        ),
    }


def _prepared_feature_frame(prepared: pd.DataFrame) -> pd.DataFrame:
    required = {"stock_id", "_revenue_signal_date"}
    missing = sorted(required - set(prepared.columns))
    if missing:
        raise RuntimeError(f"forward confirmation prepared frame is missing columns: {missing}")
    keep = ["stock_id", "_revenue_signal_date", *[column for column in FEATURE_COLUMNS if column in prepared.columns]]
    frame = prepared.loc[:, list(dict.fromkeys(keep))].copy()
    frame["stock_id"] = frame["stock_id"].map(_normalize_stock_id)
    frame["date"] = _normalize_date(frame["_revenue_signal_date"])
    frame = frame.drop(columns=["_revenue_signal_date"])
    frame = frame.sort_values(["stock_id", "date"], kind="mergesort")
    if frame.duplicated(["stock_id", "date"]).any():
        raise RuntimeError("forward confirmation prepared frame has duplicate stock/date rows")
    return frame


def prepare_daily_by_stock(
    prepared: pd.DataFrame,
    source_detail: pd.DataFrame,
    *,
    price_dir: Path = PRICE_HISTORY_DIR,
    observation_cutoff_date: str | None = None,
) -> dict[str, pd.DataFrame]:
    features = _prepared_feature_frame(prepared)
    resolutions = _load_price_resolutions()
    output: dict[str, pd.DataFrame] = {}
    stock_ids = sorted(set(source_detail["stock_id"]))
    feature_by_stock = {
        stock_id: part.drop(columns=["stock_id"]).reset_index(drop=True)
        for stock_id, part in features.groupby("stock_id", sort=False)
    }
    for stock_id in stock_ids:
        path = price_dir / f"{stock_id}.csv"
        if not path.is_file():
            continue
        price = load_stock_price(
            stock_id,
            path,
            resolutions,
            observation_cutoff_date=observation_cutoff_date,
        )
        price["analysis_open"] = price["open"] * price["analysis_price_adjustment_factor"]
        price["analysis_high"] = price["high"] * price["analysis_price_adjustment_factor"]
        price["analysis_low"] = price["low"] * price["analysis_price_adjustment_factor"]
        feature = feature_by_stock.get(stock_id)
        if feature is not None:
            overlap = set(price.columns) & set(feature.columns) - {"date"}
            feature = feature.drop(columns=sorted(overlap))
            price = price.merge(feature, on="date", how="left", validate="one_to_one")
        for column in FEATURE_COLUMNS:
            if column not in price.columns:
                price[column] = np.nan
        price["volume_ratio_prev20"] = pd.to_numeric(price["volume_ratio_prev20"], errors="coerce").fillna(
            pd.to_numeric(price["volume_ratio"], errors="coerce")
        )
        price["return_5d_pct"] = pd.to_numeric(price["return_5d_pct"], errors="coerce").fillna(
            pd.to_numeric(price["analysis_return_5d_pct"], errors="coerce")
        )
        price["return_20d_pct"] = pd.to_numeric(price["return_20d_pct"], errors="coerce").fillna(
            pd.to_numeric(price["analysis_return_20d_pct"], errors="coerce")
        )
        close = pd.to_numeric(price["analysis_close"], errors="coerce")
        for window in (20, 40, 60):
            high_column = f"previous_{window}d_highest_close"
            if high_column not in price.columns:
                price[high_column] = close.shift(1).rolling(window, min_periods=window).max()
            breakout_column = f"close_breakout_prev{window}"
            price[breakout_column] = close.gt(pd.to_numeric(price[high_column], errors="coerce"))
            previous_breakout = price[breakout_column].shift(1, fill_value=False).astype(bool)
            price[f"cross_breakout_prev{window}"] = price[breakout_column] & ~previous_breakout
        latest_yoy = pd.to_numeric(price["full_monthly_revenue_latest_yoy_pct"], errors="coerce")
        cumulative_yoy = pd.to_numeric(
            price["full_monthly_revenue_cumulative_yoy_pct"], errors="coerce"
        )
        previous_yoy = pd.to_numeric(
            price["full_monthly_revenue_prev1_latest_yoy_pct"], errors="coerce"
        )
        qualifying_revenue = (
            latest_yoy.ge(30.0)
            | cumulative_yoy.ge(20.0)
            | (latest_yoy.ge(15.0) & previous_yoy.ge(15.0))
        ) & price["full_monthly_revenue_context_ready"].map(_bool_value)
        source_dates = price["full_monthly_revenue_source_table_date"].astype(str).str.strip()
        price["latest_qualifying_revenue_source_date_asof"] = (
            source_dates.where(qualifying_revenue & source_dates.ne(""), np.nan)
            .ffill()
            .fillna("")
        )
        price["kdj_j_value"] = 3.0 * pd.to_numeric(price["k_value"], errors="coerce") - 2.0 * pd.to_numeric(
            price["d_value"], errors="coerce"
        )
        price["signal_body_pct"] = (
            (pd.to_numeric(price["close"], errors="coerce") - pd.to_numeric(price["open"], errors="coerce")).abs()
            / pd.to_numeric(price["open"], errors="coerce").replace(0, np.nan)
            * 100.0
        )
        price["close_location_pct"] = pd.to_numeric(price["close_location"], errors="coerce") * 100.0
        price["ma60_minus_ma120_pct"] = (
            pd.to_numeric(price["ma60"], errors="coerce")
            / pd.to_numeric(price["ma120"], errors="coerce").replace(0, np.nan)
            - 1.0
        ) * 100.0
        price["stock_sequence_index"] = np.arange(len(price), dtype=int)
        output[stock_id] = price.reset_index(drop=True)
    return output


def _require_projection_daily_cutoff(
    daily_by_stock: dict[str, pd.DataFrame],
) -> None:
    for stock_id, frame in daily_by_stock.items():
        if "date" not in frame.columns:
            raise RuntimeError(
                f"forward confirmation daily frame is missing date: {stock_id}"
            )
        dates = _normalize_date(frame["date"])
        after_cutoff = dates.loc[dates.gt(SOURCE_PROJECTION_CUTOFF_DATE)]
        if not after_cutoff.empty:
            raise RuntimeError(
                "forward confirmation daily frame exceeds source projection cutoff: "
                f"stock_id={stock_id}; max_date={after_cutoff.max()}; "
                f"cutoff={SOURCE_PROJECTION_CUTOFF_DATE}"
            )


def _strict_launch_metrics(stock: pd.DataFrame, trigger_index: int) -> dict[str, object]:
    if trigger_index + OUTCOME_WINDOW_DAYS >= len(stock):
        return {
            "outcome_status": "right_censored_before_d20",
            "strict_success": False,
            "first_hit_offset": "",
            "d20_return_pct": "",
            "post_hit_min_return_pct": "",
        }
    base = float(stock.at[trigger_index, "analysis_close"])
    closes = pd.to_numeric(
        stock.loc[trigger_index : trigger_index + OUTCOME_WINDOW_DAYS, "analysis_close"],
        errors="coerce",
    )
    if len(closes) != OUTCOME_WINDOW_DAYS + 1 or closes.isna().any() or not np.isfinite(base) or base <= 0:
        return {
            "outcome_status": "right_censored_before_d20",
            "strict_success": False,
            "first_hit_offset": "",
            "d20_return_pct": "",
            "post_hit_min_return_pct": "",
        }
    first_window = closes.iloc[: FIRST_HIT_DEADLINE_DAYS + 1]
    hits = np.flatnonzero(first_window.to_numpy(dtype=float) >= base * 1.20)
    first_hit = int(hits[0]) if len(hits) else None
    post_min = ""
    strict = False
    if first_hit is not None:
        post_min = float(closes.iloc[first_hit:].min() / base - 1.0) * 100.0
        strict = post_min >= 20.0 - 1e-9
    return {
        "outcome_status": "strict_success" if strict else "mature_failure",
        "strict_success": strict,
        "first_hit_offset": first_hit if first_hit is not None else "",
        "d20_return_pct": round(float(closes.iloc[-1] / base - 1.0) * 100.0, 4),
        "post_hit_min_return_pct": round(float(post_min), 4) if post_min != "" else "",
    }


def _operation_metrics(stock: pd.DataFrame, confirmation_index: int) -> dict[str, object]:
    entry_index = confirmation_index + 1
    exit_index = confirmation_index + OUTCOME_WINDOW_DAYS
    if exit_index >= len(stock) or entry_index >= len(stock):
        return {
            "operation_mature": False,
            "entry_date": "",
            "entry_open": "",
            "fixed_exit_date": "",
            "fixed_exit_close": "",
            "fixed_d20_return_pct": "",
            "max_close_return_pct": "",
            "min_close_return_pct": "",
        }
    entry_open = _number(stock.at[entry_index, "analysis_open"])
    exit_close = _number(stock.at[exit_index, "analysis_close"])
    closes = pd.to_numeric(stock.loc[entry_index:exit_index, "analysis_close"], errors="coerce")
    if entry_open is None or exit_close is None or entry_open <= 0 or closes.isna().any():
        return {
            "operation_mature": False,
            "entry_date": "",
            "entry_open": "",
            "fixed_exit_date": "",
            "fixed_exit_close": "",
            "fixed_d20_return_pct": "",
            "max_close_return_pct": "",
            "min_close_return_pct": "",
        }
    returns = closes / entry_open - 1.0
    return {
        "operation_mature": True,
        "entry_date": str(stock.at[entry_index, "date"]),
        "entry_open": round(entry_open, 8),
        "fixed_exit_date": str(stock.at[exit_index, "date"]),
        "fixed_exit_close": round(exit_close, 8),
        "fixed_d20_return_pct": round((exit_close / entry_open - 1.0) * 100.0, 4),
        "max_close_return_pct": round(float(returns.max()) * 100.0, 4),
        "min_close_return_pct": round(float(returns.min()) * 100.0, 4),
    }


def _revenue_lag(
    stock: pd.DataFrame,
    trigger_index: int,
    minimum_source_date: str = "",
) -> tuple[float | None, str]:
    source_date = str(stock.at[trigger_index, "latest_qualifying_revenue_source_date_asof"]).strip()
    if minimum_source_date:
        source_date = max(source_date, minimum_source_date) if source_date else minimum_source_date
    if not source_date:
        return None, ""
    candidates = stock.index[stock["date"].ge(source_date)]
    if not len(candidates):
        return None, source_date
    source_index = int(candidates[0])
    lag = float(trigger_index - source_index) if source_index <= trigger_index else None
    return lag, source_date


def _event_features(
    stock: pd.DataFrame,
    trigger_index: int,
    minimum_source_date: str = "",
) -> dict[str, object]:
    trigger = stock.loc[trigger_index]
    next_index = trigger_index + 1
    next_observed = next_index < len(stock)
    trigger_close = _number(trigger.get("analysis_close"))
    next_close = _number(stock.at[next_index, "analysis_close"]) if next_observed else None
    previous_high = _number(trigger.get("previous_20d_highest_close"))
    revenue_lag, qualifying_source_date = _revenue_lag(
        stock,
        trigger_index,
        minimum_source_date,
    )
    k = _number(trigger.get("k_value"))
    d = _number(trigger.get("d_value"))
    j = _number(trigger.get("kdj_j_value"))
    ma20 = _number(trigger.get("ma20"))
    ma60 = _number(trigger.get("ma60"))
    ma120 = _number(trigger.get("ma120"))
    ema23 = _number(trigger.get("ema23"))
    volume_ratio = _number(trigger.get("volume_ratio_prev20"))
    return20 = _number(trigger.get("return_20d_pct"))
    rsi14 = _number(trigger.get("rsi14"))
    range23 = _number(trigger.get("range_width_23d_pct"))
    position120 = _number(trigger.get("close_position_120d_pct"))
    latest_yoy = _number(trigger.get("full_monthly_revenue_latest_yoy_pct"))
    cumulative_yoy = _number(trigger.get("full_monthly_revenue_cumulative_yoy_pct"))
    previous_yoy = _number(trigger.get("full_monthly_revenue_prev1_latest_yoy_pct"))
    tdcc_observed = _bool_value(trigger.get("tdcc_history_available"))
    market_regime = str(trigger.get("signal_market_regime", "")).strip()
    revenue_observed = _bool_value(trigger.get("full_monthly_revenue_context_ready"))
    next_return = (
        (next_close / trigger_close - 1.0) * 100.0
        if next_close is not None and trigger_close is not None and trigger_close > 0
        else None
    )
    return {
        "trigger_date": str(trigger["date"]),
        "trigger_close": _stable(trigger_close, 8),
        "previous_20d_highest_close": _stable(previous_high, 8),
        "breakout_prev40": _bool_value(trigger.get("close_breakout_prev40")),
        "breakout_prev60": _bool_value(trigger.get("close_breakout_prev60")),
        "next_day_observed": next_observed,
        "next_day_date": str(stock.at[next_index, "date"]) if next_observed else "",
        "next_day_close": _stable(next_close, 8),
        "next_day_close_gt_trigger_close": bool(
            next_close is not None and trigger_close is not None and next_close > trigger_close
        ),
        "next_day_close_holds_previous_close_high": bool(
            next_close is not None and previous_high is not None and next_close >= previous_high
        ),
        "next_day_close_return_pct": _stable(next_return),
        "volume_ratio_prev20": _stable(volume_ratio),
        "volume_ge1_5": bool(volume_ratio is not None and volume_ratio >= 1.5),
        "volume_ge2": bool(volume_ratio is not None and volume_ratio >= 2.0),
        "ma120_observed": ma60 is not None and ma120 is not None,
        "ma60_gt_ma120": bool(ma60 is not None and ma120 is not None and ma60 > ma120),
        "ma60_minus_ma120_pct": _stable(trigger.get("ma60_minus_ma120_pct")),
        "obv_observed": _number(trigger.get("obv_slope_5d")) is not None,
        "obv_above_ma20": _bool_value(trigger.get("obv_above_ma20")),
        "kdj_observed": k is not None and d is not None and j is not None,
        "kdj_bullish_not_extreme": bool(
            k is not None and d is not None and j is not None and k > d and j > k and j < 100.0
        ),
        "kdj_j_ge100": bool(j is not None and j >= 100.0),
        "ma20_ema23_observed": trigger_close is not None and ma20 is not None and ema23 is not None,
        "close_above_ma20_ema23": bool(
            trigger_close is not None
            and ma20 is not None
            and ema23 is not None
            and trigger_close > ma20
            and trigger_close > ema23
        ),
        "macd_observed": _number(trigger.get("macd_hist")) is not None,
        "macd_hist_gt0": bool((_number(trigger.get("macd_hist")) or 0.0) > 0.0),
        "rsi_observed": rsi14 is not None,
        "rsi14_40_70": bool(rsi14 is not None and 40.0 <= rsi14 <= 70.0),
        "rsi14_ge60": bool(rsi14 is not None and rsi14 >= 60.0),
        "return20_observed": return20 is not None,
        "return20_0_25": bool(return20 is not None and 0.0 <= return20 <= 25.0),
        "range23_observed": range23 is not None,
        "range23_le15": bool(range23 is not None and range23 <= 15.0),
        "position120_observed": position120 is not None,
        "position120_low_le40": bool(position120 is not None and position120 <= 40.0),
        "position120_mid_40_75": bool(position120 is not None and 40.0 < position120 <= 75.0),
        "position120_high_gt75": bool(position120 is not None and position120 > 75.0),
        "solid_red_candle": _bool_value(trigger.get("solid_red_candle")),
        "tdcc_observed": tdcc_observed,
        "tdcc_high_thresholds_up": bool(tdcc_observed and _bool_value(trigger.get("high_thresholds_up"))),
        "tdcc_consecutive_up_ge1": bool(
            tdcc_observed
            and _number(trigger.get("tdcc_consecutive_up_weeks")) is not None
            and float(trigger.get("tdcc_consecutive_up_weeks")) >= 1.0
        ),
        "market_observed": market_regime not in {"", "unknown", "nan"},
        "market_bull": market_regime in {"strong_bull", "mild_bull"},
        "market_correction_or_high_risk": market_regime in {"correction", "high_risk"},
        "revenue_observed": revenue_observed,
        "revenue_two_month_observed": revenue_observed and latest_yoy is not None and previous_yoy is not None,
        "revenue_latest_ge50": bool(latest_yoy is not None and latest_yoy >= 50.0),
        "revenue_cumulative_ge30": bool(cumulative_yoy is not None and cumulative_yoy >= 30.0),
        "revenue_two_month_yoy_ge15": bool(
            latest_yoy is not None and previous_yoy is not None and latest_yoy >= 15.0 and previous_yoy >= 15.0
        ),
        "revenue_lag_observed": revenue_lag is not None,
        "revenue_lag_0_14": bool(revenue_lag is not None and 0 <= revenue_lag <= 14),
        "revenue_lag_15_30": bool(revenue_lag is not None and 15 <= revenue_lag <= 30),
        "revenue_lag_31_60": bool(revenue_lag is not None and 31 <= revenue_lag <= 60),
        "revenue_lag_61_90": bool(revenue_lag is not None and 61 <= revenue_lag <= 90),
        "revenue_lag_91_126": bool(revenue_lag is not None and 91 <= revenue_lag <= 126),
        "revenue_lag_trading_days": _stable(revenue_lag),
        "qualifying_revenue_source_date_asof": qualifying_source_date,
        "revenue_latest_yoy_pct": _stable(latest_yoy),
        "revenue_cumulative_yoy_pct": _stable(cumulative_yoy),
        "revenue_latest_yoy_delta_1m_pct_points": _stable(
            trigger.get("full_monthly_revenue_latest_yoy_delta_1m_pct_points")
        ),
        "return_5d_pct": _stable(trigger.get("return_5d_pct")),
        "return_20d_pct": _stable(return20),
        "range_width_23d_pct": _stable(range23),
        "range_width_60d_pct": _stable(trigger.get("range_width_60d_pct")),
        "close_position_120d_pct": _stable(position120),
        "signal_body_pct": _stable(trigger.get("signal_body_pct")),
        "close_location_pct": _stable(trigger.get("close_location_pct")),
        "rsi14": _stable(rsi14),
        "macd_hist": _stable(trigger.get("macd_hist")),
        "k_value": _stable(k),
        "d_value": _stable(d),
        "kdj_j_value": _stable(j),
        "ema23_slope_5d_pct": _stable(trigger.get("ema23_slope_5d_pct")),
        "distance_to_ema23_pct": _stable(trigger.get("distance_to_ema23_pct")),
        "obv_slope_5d": _stable(trigger.get("obv_slope_5d")),
        "tdcc_consecutive_up_weeks": _stable(trigger.get("tdcc_consecutive_up_weeks")),
        "market_regime": market_regime,
        "revenue_period": str(trigger.get("full_monthly_revenue_period", "")),
        "revenue_source_table_date": str(trigger.get("full_monthly_revenue_source_table_date", "")),
    }


def _episode_indices(stock: pd.DataFrame, episode: pd.Series) -> tuple[int, int] | None:
    starts = stock.index[stock["date"].eq(str(episode["episode_start_trade_date"]))]
    ends = stock.index[stock["date"].eq(str(episode["episode_end_date"]))]
    if not len(starts) or not len(ends):
        return None
    start = int(starts[0])
    end = int(ends[0])
    return (start, end) if start <= end else None


def _condition_hit(features: dict[str, object], condition_id: str) -> bool:
    return bool(features.get(condition_id, False))


def _select_rule_event(
    stock: pd.DataFrame,
    start_index: int,
    end_index: int,
    rule: RuleSpec,
    minimum_source_date: str = "",
) -> tuple[int, int, dict[str, object]] | None:
    trigger_prefix = "close_breakout" if rule.trigger_mode == "level" else "cross_breakout"
    trigger_column = f"{trigger_prefix}_prev{rule.trigger_window}"
    for trigger_index in range(start_index, end_index + 1):
        if not _bool_value(stock.at[trigger_index, trigger_column]):
            continue
        features = _event_features(stock, trigger_index, minimum_source_date)
        if not all(_condition_hit(features, condition_id) for condition_id in rule.condition_ids):
            continue
        confirmation_index = trigger_index
        if rule.next_day_mode != "none":
            next_index = trigger_index + 1
            if next_index >= len(stock):
                continue
            if rule.next_day_mode == "close_gt_trigger_close":
                confirmed = bool(features["next_day_close_gt_trigger_close"])
            elif rule.next_day_mode == "hold_previous_close_high":
                confirmed = bool(features["next_day_close_holds_previous_close_high"])
            else:
                raise RuntimeError(f"unknown next-day confirmation mode: {rule.next_day_mode}")
            if not confirmed:
                continue
            confirmation_index = next_index
        return trigger_index, confirmation_index, features
    return None


def _episode_anomaly(episode: pd.Series) -> bool:
    return _bool_value(episode["qualifying_source_revenue_anomaly_candidate_flag"]) or _bool_value(
        episode["unresolved_price_path_candidate_flag"]
    )


def _detail_row(
    *,
    generated_at: str,
    episode: pd.Series,
    rule: RuleSpec,
    stock: pd.DataFrame | None,
) -> dict[str, object]:
    base = {
        "generated_at": generated_at,
        "model_id": MODEL_ID,
        "artifact_id": ARTIFACT_ID,
        "artifact_version": ARTIFACT_VERSION,
        "condition_variant_id": PRIMARY_VARIANT_ID,
        "episode_key": str(episode["episode_key"]),
        "stock_id": str(episode["stock_id"]),
        "stock_name": str(episode["stock_name"]),
        "episode_start_trade_date": str(episode["episode_start_trade_date"]),
        "episode_start_source_date": str(episode.get("episode_start_source_date", "")),
        "episode_end_date": str(episode["episode_end_date"]),
        "source_episode_status": str(episode["episode_status"]),
        "source_first_breakout_date": str(episode["first_breakout_date"]),
        "source_first_breakout_outcome": str(episode["first_breakout_outcome"]),
        "source_launch_date": str(episode["launch_date"]),
        "rule_order": rule.rule_order,
        "rule_id": rule.rule_id,
        "rule_family": rule.rule_family,
        "rule_definition": rule.rule_definition,
        "rule_information_cutoff": rule.information_cutoff,
        "trigger_window_trading_days": rule.trigger_window,
        "rule_trigger_mode": rule.trigger_mode,
        "rule_condition_ids": ";".join(rule.condition_ids),
        "rule_next_day_mode": rule.next_day_mode,
        "entry_rule": "confirmation_close_then_next_trading_day_open",
        "fixed_exit_rule": "confirmation_relative_d20_close_research_only",
        "strict_outcome_rule": "trigger close reaches +20% by D+15 and never closes below +20% through D+20",
        "source_anomaly_candidate_flag": _bool_value(
            episode["qualifying_source_revenue_anomaly_candidate_flag"]
        ),
        "unresolved_price_path_candidate_flag": _bool_value(
            episode["unresolved_price_path_candidate_flag"]
        ),
        "anomaly_candidate_flag": _episode_anomaly(episode),
        "same_stock_non_overlap_applied": True,
        "first_match_policy": "first_rule_match_only_no_retrospective_reselection",
        "operation_return_review_candidate_flag": False,
        "operation_return_review_status": "not_triggered",
        "operation_return_review_policy": OPERATION_RETURN_REVIEW_POLICY,
        "approved_for_daily": False,
        "production_change": False,
    }
    if stock is None:
        return {
            **base,
            "selection_status": "missing_daily_price_or_feature_context",
            "trigger_date": "",
            "confirmation_date": "",
            "outcome_status": "",
            "operation_mature": False,
        }
    indices = _episode_indices(stock, episode)
    if indices is None:
        return {
            **base,
            "selection_status": "missing_episode_boundary_date",
            "trigger_date": "",
            "confirmation_date": "",
            "outcome_status": "",
            "operation_mature": False,
        }
    selected = _select_rule_event(
        stock,
        indices[0],
        indices[1],
        rule,
        str(episode.get("episode_start_source_date", "")),
    )
    if selected is None:
        if str(episode["episode_status"]) == "right_censored_before_active_horizon":
            status = "right_censored_no_confirmation"
        elif str(episode["episode_status"]) == "launch_within_active_horizon":
            status = "missed_retrospective_launch_no_confirmation"
        else:
            status = "no_confirmation_before_mature_episode_end"
        return {
            **base,
            "selection_status": status,
            "trigger_date": "",
            "confirmation_date": "",
            "outcome_status": "",
            "operation_mature": False,
        }
    trigger_index, confirmation_index, features = selected
    outcome = _strict_launch_metrics(stock, trigger_index)
    operation = _operation_metrics(stock, confirmation_index)
    compact_features = {column: features.get(column, "") for column in RULE_DETAIL_EVENT_FIELDS}
    operation_return = _number(operation.get("fixed_d20_return_pct"))
    operation_return_review_candidate = bool(
        operation.get("operation_mature")
        and operation_return is not None
        and abs(operation_return) >= OPERATION_RETURN_REVIEW_THRESHOLD_PCT
    )
    return {
        **base,
        "selection_status": "confirmed_first_rule_match",
        **compact_features,
        "confirmation_date": str(stock.at[confirmation_index, "date"]),
        "confirmation_close": _stable(stock.at[confirmation_index, "analysis_close"], 8),
        "confirmation_lag_from_trigger_days": confirmation_index - trigger_index,
        "outcome_status": str(outcome["outcome_status"]),
        "first_hit_20_day_offset": outcome["first_hit_offset"],
        "trigger_d20_close_return_pct": outcome["d20_return_pct"],
        "trigger_post_hit_min_return_pct": outcome["post_hit_min_return_pct"],
        **operation,
        "operation_return_review_candidate_flag": operation_return_review_candidate,
        "operation_return_review_status": (
            "candidate_only_pending_bottom_level_root_cause_disposition"
            if operation_return_review_candidate
            else "not_triggered"
        ),
        "operation_return_review_policy": OPERATION_RETURN_REVIEW_POLICY,
    }


def build_rule_detail(
    source_detail: pd.DataFrame,
    daily_by_stock: dict[str, pd.DataFrame],
) -> pd.DataFrame:
    generated_at = _now_text()
    rows = [
        _detail_row(
            generated_at=generated_at,
            episode=episode,
            rule=rule,
            stock=daily_by_stock.get(str(episode["stock_id"])),
        )
        for _, episode in source_detail.iterrows()
        for rule in RULE_SPECS
    ]
    detail = pd.DataFrame(rows)
    if detail.duplicated(["episode_key", "rule_id"]).any():
        raise RuntimeError("forward confirmation detail duplicates an episode/rule pair")
    return detail.sort_values(["rule_order", "stock_id", "episode_start_trade_date"], kind="mergesort").reset_index(drop=True)


def _event_row(
    *,
    generated_at: str,
    episode: pd.Series,
    stock: pd.DataFrame,
    trigger_index: int,
    contrast_group: str,
) -> dict[str, object]:
    return {
        "generated_at": generated_at,
        "model_id": MODEL_ID,
        "artifact_id": ARTIFACT_ID,
        "artifact_version": ARTIFACT_VERSION,
        "condition_variant_id": PRIMARY_VARIANT_ID,
        "episode_key": str(episode["episode_key"]),
        "stock_id": str(episode["stock_id"]),
        "stock_name": str(episode["stock_name"]),
        "contrast_group": contrast_group,
        "contrast_scope": "one_retrospective_source_launch_and_at_most_one_source_first_mature_failure_per_episode_not_trade_counting",
        "source_episode_status": str(episode["episode_status"]),
        "source_launch_date": str(episode["launch_date"]),
        "anomaly_candidate_flag": _episode_anomaly(episode),
        **_event_features(
            stock,
            trigger_index,
            str(episode.get("episode_start_source_date", "")),
        ),
        **_strict_launch_metrics(stock, trigger_index),
        "approved_for_daily": False,
        "production_change": False,
    }


def build_event_detail(
    source_detail: pd.DataFrame,
    daily_by_stock: dict[str, pd.DataFrame],
) -> pd.DataFrame:
    generated_at = _now_text()
    rows: list[dict[str, object]] = []
    for _, episode in source_detail.iterrows():
        stock = daily_by_stock.get(str(episode["stock_id"]))
        if stock is None:
            continue
        date_to_index = {str(value): int(index) for index, value in stock["date"].items()}
        launch_date = str(episode["launch_date"])
        if launch_date:
            if launch_date not in date_to_index:
                raise RuntimeError(f"forward confirmation launch date is missing from price history: {episode['episode_key']}")
            launch_index = date_to_index[launch_date]
            if _strict_launch_metrics(stock, launch_index)["outcome_status"] != "strict_success":
                raise RuntimeError(f"forward confirmation source launch label is not reproducible: {episode['episode_key']}")
            rows.append(
                _event_row(
                    generated_at=generated_at,
                    episode=episode,
                    stock=stock,
                    trigger_index=launch_index,
                    contrast_group="strict_success_launch_event",
                )
            )
        first_breakout_date = str(episode["first_breakout_date"])
        if str(episode["first_breakout_outcome"]) == "mature_failure":
            if first_breakout_date not in date_to_index:
                raise RuntimeError(f"forward confirmation first failure date is missing from price history: {episode['episode_key']}")
            rows.append(
                _event_row(
                    generated_at=generated_at,
                    episode=episode,
                    stock=stock,
                    trigger_index=date_to_index[first_breakout_date],
                    contrast_group="first_mature_failure_event",
                )
            )
    event_detail = pd.DataFrame(rows)
    if event_detail.empty:
        raise RuntimeError("forward confirmation event contrast is empty")
    if event_detail.duplicated(["episode_key", "contrast_group"]).any():
        raise RuntimeError("forward confirmation event contrast duplicates an episode/group")
    return event_detail.sort_values(["stock_id", "trigger_date", "contrast_group"], kind="mergesort").reset_index(drop=True)


def _same_stock_overlap_pair_count(source_detail: pd.DataFrame) -> int:
    count = 0
    for _, stock in source_detail.sort_values(["stock_id", "episode_start_trade_date"]).groupby("stock_id", sort=False):
        previous_end = ""
        for row in stock.itertuples(index=False):
            start = str(row.episode_start_trade_date)
            end = str(row.episode_end_date)
            if previous_end and start <= previous_end:
                count += 1
            previous_end = max(previous_end, end)
    return count


def build_rule_summary(
    detail: pd.DataFrame,
    source_detail: pd.DataFrame,
    *,
    source_projection_manifest: pd.DataFrame,
) -> pd.DataFrame:
    overlap_count = _same_stock_overlap_pair_count(source_detail)
    projection_lineage = _source_projection_summary_lineage(
        source_projection_manifest
    )
    rows: list[dict[str, object]] = []
    for basis in ANALYSIS_BASES:
        source = source_detail.copy()
        part = detail.copy()
        if basis == SENSITIVITY_ANALYSIS_BASIS:
            allowed_keys = set(source.loc[~source.apply(_episode_anomaly, axis=1), "episode_key"])
            source = source.loc[source["episode_key"].isin(allowed_keys)]
            part = part.loc[part["episode_key"].isin(allowed_keys)]
        for rule in RULE_SPECS:
            selected = part.loc[part["rule_id"].eq(rule.rule_id)].copy()
            confirmed = selected["selection_status"].eq("confirmed_first_rule_match")
            success = confirmed & selected["outcome_status"].eq("strict_success")
            failure = confirmed & selected["outcome_status"].eq("mature_failure")
            censored = confirmed & selected["outcome_status"].eq("right_censored_before_d20")
            classifiable = success | failure
            operation_mature = confirmed & selected["operation_mature"].map(_bool_value)
            operation_return_review = (
                operation_mature
                & selected["operation_return_review_candidate_flag"].map(_bool_value)
            )
            operation_without_return_review = operation_mature & ~operation_return_review
            source_launch = selected["source_episode_status"].eq("launch_within_active_horizon")
            known_4916 = selected.loc[
                selected["stock_id"].eq("4916") & selected["source_launch_date"].eq("20260518")
            ]
            known_1303 = selected.loc[
                selected["stock_id"].eq("1303") & selected["source_launch_date"].eq("20260527")
            ]
            row4916 = known_4916.iloc[0] if len(known_4916) else None
            row1303 = known_1303.iloc[0] if len(known_1303) else None
            rows.append(
                {
                    "generated_at": str(detail["generated_at"].iloc[0]),
                    "model_id": MODEL_ID,
                    "artifact_id": ARTIFACT_ID,
                    "artifact_version": ARTIFACT_VERSION,
                    **projection_lineage,
                    "analysis_basis": basis,
                    "rule_order": rule.rule_order,
                    "rule_id": rule.rule_id,
                    "rule_family": rule.rule_family,
                    "rule_definition": rule.rule_definition,
                    "rule_information_cutoff": rule.information_cutoff,
                    "source_episode_count": len(source),
                    "confirmed_episode_count": int(confirmed.sum()),
                    "confirmation_coverage_pct": _rate(int(confirmed.sum()), len(source)),
                    "no_confirmation_count": int((~confirmed).sum()),
                    "strict_success_count": int(success.sum()),
                    "neutral_count": 0,
                    "mature_failure_count": int(failure.sum()),
                    "outcome_right_censored_count": int(censored.sum()),
                    "classifiable_confirmation_count": int(classifiable.sum()),
                    "strict_success_rate_pct": _rate(int(success.sum()), int(classifiable.sum())),
                    "neutral_rate_pct": 0.0 if int(classifiable.sum()) else "",
                    "mature_failure_rate_pct": _rate(int(failure.sum()), int(classifiable.sum())),
                    "source_launch_episode_count": int(source_launch.sum()),
                    "source_launch_selected_strict_success_count": int((source_launch & success).sum()),
                    "source_launch_selected_mature_failure_count": int((source_launch & failure).sum()),
                    "source_launch_missed_confirmation_count": int((source_launch & ~confirmed).sum()),
                    "operation_mature_count": int(operation_mature.sum()),
                    "avg_confirmation_next_open_to_d20_close_return_pct": _mean(
                        selected.loc[operation_mature, "fixed_d20_return_pct"]
                    ),
                    "median_confirmation_next_open_to_d20_close_return_pct": _median(
                        selected.loc[operation_mature, "fixed_d20_return_pct"]
                    ),
                    "avg_confirmation_next_open_to_d20_max_close_return_pct": _mean(
                        selected.loc[operation_mature, "max_close_return_pct"]
                    ),
                    "avg_confirmation_next_open_to_d20_min_close_return_pct": _mean(
                        selected.loc[operation_mature, "min_close_return_pct"]
                    ),
                    "operation_return_review_candidate_count": int(operation_return_review.sum()),
                    "avg_fixed_d20_return_excluding_review_candidates_sensitivity_pct": _mean(
                        selected.loc[operation_without_return_review, "fixed_d20_return_pct"]
                    ),
                    "median_fixed_d20_return_excluding_review_candidates_sensitivity_pct": _median(
                        selected.loc[operation_without_return_review, "fixed_d20_return_pct"]
                    ),
                    "operation_return_review_policy": OPERATION_RETURN_REVIEW_POLICY,
                    "confirmed_anomaly_candidate_count": int(
                        (confirmed & selected["anomaly_candidate_flag"].map(_bool_value)).sum()
                    ),
                    "known_4916_selected_date": str(row4916["trigger_date"]) if row4916 is not None else "",
                    "known_4916_selected_outcome": str(row4916["outcome_status"]) if row4916 is not None else "",
                    "known_1303_selected_date": str(row1303["trigger_date"]) if row1303 is not None else "",
                    "known_1303_selected_outcome": str(row1303["outcome_status"]) if row1303 is not None else "",
                    "same_stock_overlap_pair_count": overlap_count,
                    "sample_policy": "sample_count_disclosed_not_used_as_automatic_rejection",
                    "neutral_policy": "no_neutral_outcome_defined; strict launch label is binary and right-censored rows are separate",
                    "anomaly_policy": "primary retains candidates; sensitivity excludes unresolved revenue or price-path candidates",
                    "retrospective_label_status": "research_only_confirmation_discrimination_not_operation_contract",
                    "financial_statement_scope": FINANCIAL_STATEMENT_SCOPE,
                    "approved_for_daily": False,
                    "production_change": False,
                    "promotion_readiness": "blocked_pending_rule_selection_and_formal_operation_contract",
                }
            )
    return pd.DataFrame(rows).sort_values(["analysis_basis", "rule_order"], kind="mergesort").reset_index(drop=True)


RETURN_REVIEW_COLUMNS = [
    "generated_at",
    "model_id",
    "artifact_id",
    "artifact_version",
    "stock_id",
    "stock_name",
    "entry_date",
    "entry_open",
    "fixed_exit_date",
    "fixed_exit_close",
    "fixed_d20_return_pct",
    "replayed_fixed_d20_return_pct",
    "review_trigger_threshold_pct",
    "review_candidate_rule_count",
    "review_candidate_rule_ids",
    "path_trading_row_count",
    "max_abs_raw_close_return_1d_pct",
    "max_abs_analysis_close_return_1d_pct",
    "max_abs_analysis_open_gap_pct",
    "price_resolution_ids_in_path",
    "bottom_level_price_path_result",
    "authoritative_corporate_action_layer_status",
    "review_disposition",
    "included_in_primary_metrics",
    "excluded_in_review_candidate_sensitivity",
    "approved_for_daily",
    "production_change",
]


def build_operation_return_review(
    detail: pd.DataFrame,
    daily_by_stock: dict[str, pd.DataFrame],
) -> pd.DataFrame:
    candidates = detail.loc[
        detail["operation_return_review_candidate_flag"].map(_bool_value)
    ].copy()
    if candidates.empty:
        return pd.DataFrame(columns=RETURN_REVIEW_COLUMNS)
    rows: list[dict[str, object]] = []
    key_columns = ["stock_id", "entry_date", "fixed_exit_date"]
    for keys, group in candidates.groupby(key_columns, sort=False, dropna=False):
        stock_id, entry_date, exit_date = (str(value) for value in keys)
        stock = daily_by_stock.get(stock_id)
        if stock is None:
            raise RuntimeError(f"operation return review is missing price history: {stock_id}")
        entry_indices = stock.index[stock["date"].eq(entry_date)]
        exit_indices = stock.index[stock["date"].eq(exit_date)]
        if not len(entry_indices) or not len(exit_indices):
            raise RuntimeError(f"operation return review path boundary is missing: {stock_id}/{entry_date}/{exit_date}")
        entry_index = int(entry_indices[0])
        exit_index = int(exit_indices[0])
        if entry_index <= 0 or exit_index < entry_index:
            raise RuntimeError(f"operation return review path boundary is invalid: {stock_id}/{entry_date}/{exit_date}")
        replay = stock.loc[entry_index - 1 : exit_index].copy()
        operation_path = stock.loc[entry_index:exit_index].copy()
        raw_close = pd.to_numeric(replay["close"], errors="coerce")
        analysis_close = pd.to_numeric(replay["analysis_close"], errors="coerce")
        analysis_open = pd.to_numeric(replay["analysis_open"], errors="coerce")
        prior_analysis_close = analysis_close.shift(1)
        raw_returns = raw_close.pct_change().iloc[1:] * 100.0
        analysis_returns = analysis_close.pct_change().iloc[1:] * 100.0
        open_gaps = (analysis_open / prior_analysis_close - 1.0).iloc[1:] * 100.0
        resolution_ids = sorted(
            {
                value
                for value in operation_path["price_resolution_ids_on_date"].astype(str)
                if value
            }
        )
        max_raw = float(raw_returns.abs().max()) if raw_returns.notna().any() else math.nan
        max_analysis = (
            float(analysis_returns.abs().max()) if analysis_returns.notna().any() else math.nan
        )
        max_open_gap = float(open_gaps.abs().max()) if open_gaps.notna().any() else math.nan
        no_scale_break = all(
            np.isfinite(value) and value <= 20.0
            for value in (max_raw, max_analysis, max_open_gap)
        )
        returns = pd.to_numeric(group["fixed_d20_return_pct"], errors="coerce").dropna()
        if returns.empty or returns.max() - returns.min() > 1e-9:
            raise RuntimeError(f"operation return review has inconsistent duplicated returns: {stock_id}/{entry_date}")
        replayed_return = (
            float(stock.at[exit_index, "analysis_close"])
            / float(stock.at[entry_index, "analysis_open"])
            - 1.0
        ) * 100.0
        if abs(replayed_return - float(returns.iloc[0])) > 0.0001:
            raise RuntimeError(f"operation return review replay drift: {stock_id}/{entry_date}")
        first = group.iloc[0]
        rows.append(
            {
                "generated_at": str(detail["generated_at"].iloc[0]),
                "model_id": MODEL_ID,
                "artifact_id": ARTIFACT_ID,
                "artifact_version": ARTIFACT_VERSION,
                "stock_id": stock_id,
                "stock_name": str(first["stock_name"]),
                "entry_date": entry_date,
                "entry_open": first["entry_open"],
                "fixed_exit_date": exit_date,
                "fixed_exit_close": first["fixed_exit_close"],
                "fixed_d20_return_pct": round(float(returns.iloc[0]), 4),
                "replayed_fixed_d20_return_pct": round(replayed_return, 4),
                "review_trigger_threshold_pct": OPERATION_RETURN_REVIEW_THRESHOLD_PCT,
                "review_candidate_rule_count": int(group["rule_id"].nunique()),
                "review_candidate_rule_ids": ";".join(sorted(set(group["rule_id"].astype(str)))),
                "path_trading_row_count": len(operation_path),
                "max_abs_raw_close_return_1d_pct": _stable(max_raw),
                "max_abs_analysis_close_return_1d_pct": _stable(max_analysis),
                "max_abs_analysis_open_gap_pct": _stable(max_open_gap),
                "price_resolution_ids_in_path": ";".join(resolution_ids),
                "bottom_level_price_path_result": (
                    "no_single_day_scale_break_observed"
                    if no_scale_break
                    else "scale_break_or_incomplete_path_requires_root_cause_review"
                ),
                "authoritative_corporate_action_layer_status": (
                    "not_available_as_complete_shared_point_in_time_layer"
                ),
                "review_disposition": (
                    "unresolved_review_candidate_retained_in_primary_not_classified_as_anomaly"
                ),
                "included_in_primary_metrics": True,
                "excluded_in_review_candidate_sensitivity": True,
                "approved_for_daily": False,
                "production_change": False,
            }
        )
    return pd.DataFrame(rows, columns=RETURN_REVIEW_COLUMNS).sort_values(
        ["fixed_d20_return_pct", "stock_id"],
        ascending=[False, True],
        kind="mergesort",
    ).reset_index(drop=True)


def build_feature_contrast(event_detail: pd.DataFrame) -> pd.DataFrame:
    rows: list[dict[str, object]] = []
    for basis in ANALYSIS_BASES:
        part = event_detail.copy()
        if basis == SENSITIVITY_ANALYSIS_BASIS:
            part = part.loc[~part["anomaly_candidate_flag"].map(_bool_value)].copy()
        success = part.loc[part["contrast_group"].eq("strict_success_launch_event")]
        failure = part.loc[part["contrast_group"].eq("first_mature_failure_event")]
        for order, feature_id, family, rule, column, observed_column in BINARY_FEATURE_SPECS:
            success_observed = (
                success[observed_column].map(_bool_value)
                if observed_column
                else pd.Series(True, index=success.index)
            )
            failure_observed = (
                failure[observed_column].map(_bool_value)
                if observed_column
                else pd.Series(True, index=failure.index)
            )
            success_hit = success[column].map(_bool_value) & success_observed
            failure_hit = failure[column].map(_bool_value) & failure_observed
            hit_count = int(success_hit.sum() + failure_hit.sum())
            miss_success = int(success_observed.sum() - success_hit.sum())
            miss_failure = int(failure_observed.sum() - failure_hit.sum())
            miss_count = miss_success + miss_failure
            success_hit_rate = _rate(int(success_hit.sum()), int(success_observed.sum()))
            failure_hit_rate = _rate(int(failure_hit.sum()), int(failure_observed.sum()))
            success_hit_rate_n = _number(success_hit_rate)
            failure_hit_rate_n = _number(failure_hit_rate)
            rows.append(
                {
                    "generated_at": str(event_detail["generated_at"].iloc[0]),
                    "model_id": MODEL_ID,
                    "artifact_id": ARTIFACT_ID,
                    "artifact_version": ARTIFACT_VERSION,
                    "analysis_basis": basis,
                    "row_type": "binary_feature",
                    "feature_order": order,
                    "feature_id": feature_id,
                    "feature_family": family,
                    "feature_rule": rule,
                    "success_group_count": len(success),
                    "failure_group_count": len(failure),
                    "success_observed_count": int(success_observed.sum()),
                    "failure_observed_count": int(failure_observed.sum()),
                    "success_hit_count": int(success_hit.sum()),
                    "failure_hit_count": int(failure_hit.sum()),
                    "success_hit_rate_pct": success_hit_rate,
                    "failure_hit_rate_pct": failure_hit_rate,
                    "success_minus_failure_hit_rate_pct_points": (
                        round(success_hit_rate_n - failure_hit_rate_n, 4)
                        if success_hit_rate_n is not None and failure_hit_rate_n is not None
                        else ""
                    ),
                    "feature_hit_event_count": hit_count,
                    "strict_success_share_when_feature_hit_pct": _rate(int(success_hit.sum()), hit_count),
                    "feature_miss_event_count": miss_count,
                    "strict_success_share_when_feature_miss_pct": _rate(miss_success, miss_count),
                    "success_mean": "",
                    "success_median": "",
                    "failure_mean": "",
                    "failure_median": "",
                    "success_minus_failure_mean": "",
                    "standardized_mean_difference": "",
                    "contrast_scope": "descriptive_retrospective_source_launch_vs_source_first_mature_failure_not_trade_win_rate",
                    "sample_policy": "sample_count_disclosed_not_used_as_automatic_rejection",
                    "approved_for_daily": False,
                    "production_change": False,
                    "promotion_readiness": "blocked_pending_rule_matrix_decision",
                }
            )
        for order, feature_id, family, column in NUMERIC_FEATURE_SPECS:
            left = pd.to_numeric(success[column], errors="coerce").dropna()
            right = pd.to_numeric(failure[column], errors="coerce").dropna()
            left_mean = _mean(left)
            right_mean = _mean(right)
            left_mean_n = _number(left_mean)
            right_mean_n = _number(right_mean)
            rows.append(
                {
                    "generated_at": str(event_detail["generated_at"].iloc[0]),
                    "model_id": MODEL_ID,
                    "artifact_id": ARTIFACT_ID,
                    "artifact_version": ARTIFACT_VERSION,
                    "analysis_basis": basis,
                    "row_type": "numeric_feature",
                    "feature_order": order,
                    "feature_id": feature_id,
                    "feature_family": family,
                    "feature_rule": f"compare {column} between strict-success and first-mature-failure events",
                    "success_group_count": len(success),
                    "failure_group_count": len(failure),
                    "success_observed_count": len(left),
                    "failure_observed_count": len(right),
                    "success_hit_count": "",
                    "failure_hit_count": "",
                    "success_hit_rate_pct": "",
                    "failure_hit_rate_pct": "",
                    "success_minus_failure_hit_rate_pct_points": "",
                    "feature_hit_event_count": "",
                    "strict_success_share_when_feature_hit_pct": "",
                    "feature_miss_event_count": "",
                    "strict_success_share_when_feature_miss_pct": "",
                    "success_mean": left_mean,
                    "success_median": _median(left),
                    "failure_mean": right_mean,
                    "failure_median": _median(right),
                    "success_minus_failure_mean": (
                        round(left_mean_n - right_mean_n, 4)
                        if left_mean_n is not None and right_mean_n is not None
                        else ""
                    ),
                    "standardized_mean_difference": _pooled_effect(left, right),
                    "contrast_scope": "descriptive_retrospective_source_launch_vs_source_first_mature_failure_not_trade_win_rate",
                    "sample_policy": "sample_count_disclosed_not_used_as_automatic_rejection",
                    "approved_for_daily": False,
                    "production_change": False,
                    "promotion_readiness": "blocked_pending_rule_matrix_decision",
                }
            )
    return pd.DataFrame(rows).sort_values(
        ["analysis_basis", "row_type", "feature_order", "feature_id"], kind="mergesort"
    ).reset_index(drop=True)


def build_forward_confirmation_feature_audit(
    prepared: pd.DataFrame | None = None,
    source_detail: pd.DataFrame | None = None,
    *,
    daily_by_stock: dict[str, pd.DataFrame] | None = None,
    source_projection_manifest: pd.DataFrame | None = None,
) -> tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    if source_detail is None:
        if source_projection_manifest is not None:
            raise ValueError(
                "source_projection_manifest cannot be supplied without explicit source_detail"
            )
        source_projection_manifest, projected_source_detail = load_source_projection()
    else:
        if source_projection_manifest is None:
            raise ValueError(
                "source_projection_manifest is required with explicit source_detail"
            )
        projected_source_detail = source_detail
        validate_projection_binding(
            source_projection_manifest,
            projected_source_detail,
            expected_cutoff_date=SOURCE_PROJECTION_CUTOFF_DATE,
        )
    source = _normalize_source_detail(projected_source_detail)
    if daily_by_stock is None:
        if prepared is None:
            raise ValueError("prepared frame is required when daily_by_stock is not supplied")
        daily_by_stock = prepare_daily_by_stock(
            prepared,
            source,
            observation_cutoff_date=SOURCE_PROJECTION_CUTOFF_DATE,
        )
    _require_projection_daily_cutoff(daily_by_stock)
    detail = build_rule_detail(source, daily_by_stock)
    events = build_event_detail(source, daily_by_stock)
    summary = build_rule_summary(
        detail,
        source,
        source_projection_manifest=source_projection_manifest,
    )
    feature = build_feature_contrast(events)
    return_review = build_operation_return_review(detail, daily_by_stock)
    return summary, detail, events, feature, return_review


def _markdown_table(frame: pd.DataFrame, columns: list[str], limit: int = 100) -> str:
    if frame.empty:
        return "無資料。"
    view = frame.loc[:, [column for column in columns if column in frame.columns]].head(limit)
    headers = list(view.columns)
    rows = ["| " + " | ".join(headers) + " |", "| " + " | ".join(["---"] * len(headers)) + " |"]
    for record in view.astype(str).itertuples(index=False, name=None):
        rows.append("| " + " | ".join(value.replace("|", "/") for value in record) + " |")
    return "\n".join(rows)


def _markdown(
    summary: pd.DataFrame,
    event_detail: pd.DataFrame,
    feature: pd.DataFrame,
    return_review: pd.DataFrame,
) -> str:
    primary = summary.loc[summary["analysis_basis"].eq(PRIMARY_ANALYSIS_BASIS)].copy()
    baseline = primary.loc[primary["rule_id"].eq("first_close_cross_prev20")].iloc[0]
    ranked = primary.sort_values(
        ["strict_success_rate_pct", "confirmed_episode_count"], ascending=[False, False], kind="mergesort"
    )
    binary = feature.loc[
        feature["analysis_basis"].eq(PRIMARY_ANALYSIS_BASIS) & feature["row_type"].eq("binary_feature")
    ].copy()
    binary["_delta"] = pd.to_numeric(binary["success_minus_failure_hit_rate_pct_points"], errors="coerce")
    binary = binary.sort_values("_delta", ascending=False, kind="mergesort").drop(columns=["_delta"])
    known = event_detail.loc[event_detail["stock_id"].isin(KNOWN_CASES)].copy()
    lines = [
        "# 營收改善尚未反應模型：前向確認與特徵稽核",
        "",
        f"- generated_at: `{_now_text()}`",
        f"- model_id: `{MODEL_ID}`",
        f"- artifact_version: `{ARTIFACT_VERSION}`",
        "- 狀態：`research_only`，不可直接升格或進入 PDF 操作列。",
        "- 來源母體：固定綁定 `20260713` source snapshot projection 中 `absolute_or_two_month_yoy_ge15` 的同股不重疊 episodes。",
        "- 截止防線：cutoff 後新增的 current source-first episodes 不得改變本 artifact。",
        "- 突破事件：收盤由未高於前高，首次跨到高於前 N 日最高收盤價。",
        "- 前向選取：每條確認規則只採第一次符合事件；後來成功不得回頭取代較早已確認的失敗。",
        "- 特徵對照：成功組使用 source 標記的真正發動日，失敗組使用 source 第一個成熟失敗突破；僅供找差異，不是可交易勝率。",
        "- 嚴格成功：觸發收盤後 D+15 內達 +20%，且至 D+20 每日收盤均未跌回 +20% 以下。",
        "- 操作報酬：確認日收盤成立，下一交易日開盤進場，確認日起算 D+20 收盤固定出場；本稽核尚未定義停損。",
        "- 和局口徑：本次尚未核准和局定義；資料不足者獨立列為 right-censored，不得算失敗。",
        "- 盤中高低：僅可用於 K 棒與收盤位置等 advisory 特徵，不得單獨支撐 promotion。",
        "- 高報酬查核：D+20 絕對報酬達 80% 只會觸發 review candidate；primary 保留，未完成底層根因前不得判定為異常。",
        f"- 基準第一個突破嚴格成功率：`{baseline['strict_success_rate_pct']}%`。",
        "- 財報範圍：本次只使用月營收；EPS、毛利率、營益率、營業利益、業外與淨利均未納入。",
        "",
        "## 確認規則矩陣",
        "",
        _markdown_table(
            ranked,
            [
                "rule_id",
                "rule_information_cutoff",
                "confirmed_episode_count",
                "confirmation_coverage_pct",
                "strict_success_rate_pct",
                "mature_failure_rate_pct",
                "avg_confirmation_next_open_to_d20_close_return_pct",
                "median_confirmation_next_open_to_d20_close_return_pct",
                "known_4916_selected_date",
                "known_4916_selected_outcome",
                "known_1303_selected_date",
                "known_1303_selected_outcome",
            ],
        ),
        "",
        "## 成功與失敗事件的特徵差異",
        "",
        _markdown_table(
            binary,
            [
                "feature_id",
                "feature_family",
                "success_observed_count",
                "failure_observed_count",
                "success_hit_rate_pct",
                "failure_hit_rate_pct",
                "success_minus_failure_hit_rate_pct_points",
                "strict_success_share_when_feature_hit_pct",
            ],
            limit=40,
        ),
        "",
        "## 指定案例",
        "",
        _markdown_table(
            known,
            [
                "stock_id",
                "stock_name",
                "contrast_group",
                "trigger_date",
                "outcome_status",
                "next_day_close_gt_trigger_close",
                "volume_ratio_prev20",
                "ma60_gt_ma120",
                "obv_above_ma20",
                "kdj_bullish_not_extreme",
                "tdcc_high_thresholds_up",
                "market_regime",
                "revenue_lag_trading_days",
            ],
        ),
        "",
        "## 高報酬底層路徑查核候選",
        "",
        _markdown_table(
            return_review,
            [
                "stock_id",
                "stock_name",
                "entry_date",
                "fixed_exit_date",
                "fixed_d20_return_pct",
                "path_trading_row_count",
                "max_abs_raw_close_return_1d_pct",
                "max_abs_analysis_open_gap_pct",
                "price_resolution_ids_in_path",
                "bottom_level_price_path_result",
                "review_disposition",
            ],
        ),
        "",
    ]
    return "\n".join(lines)


def write_forward_confirmation_feature_audit(
    summary: pd.DataFrame,
    detail: pd.DataFrame,
    event_detail: pd.DataFrame,
    feature: pd.DataFrame,
    return_review: pd.DataFrame,
) -> None:
    for path in (
        LATEST_CSV,
        DETAIL_CSV,
        EVENT_DETAIL_CSV,
        FEATURE_CSV,
        RETURN_REVIEW_CSV,
        LATEST_MD,
        HISTORY_CSV,
        HISTORY_FEATURE_CSV,
        HISTORY_RETURN_REVIEW_CSV,
        DOCS_CSV,
        DOCS_FEATURE_CSV,
        DOCS_RETURN_REVIEW_CSV,
        DOCS_MD,
    ):
        path.parent.mkdir(parents=True, exist_ok=True)
    summary.to_csv(LATEST_CSV, index=False, encoding="utf-8-sig", lineterminator="\n")
    detail.to_csv(DETAIL_CSV, index=False, encoding="utf-8-sig", lineterminator="\n")
    event_detail.to_csv(EVENT_DETAIL_CSV, index=False, encoding="utf-8-sig", lineterminator="\n")
    feature.to_csv(FEATURE_CSV, index=False, encoding="utf-8-sig", lineterminator="\n")
    return_review.to_csv(RETURN_REVIEW_CSV, index=False, encoding="utf-8-sig", lineterminator="\n")
    summary.to_csv(HISTORY_CSV, index=False, encoding="utf-8-sig", lineterminator="\n")
    feature.to_csv(HISTORY_FEATURE_CSV, index=False, encoding="utf-8-sig", lineterminator="\n")
    return_review.to_csv(HISTORY_RETURN_REVIEW_CSV, index=False, encoding="utf-8-sig", lineterminator="\n")
    summary.to_csv(DOCS_CSV, index=False, encoding="utf-8-sig", lineterminator="\n")
    feature.to_csv(DOCS_FEATURE_CSV, index=False, encoding="utf-8-sig", lineterminator="\n")
    return_review.to_csv(DOCS_RETURN_REVIEW_CSV, index=False, encoding="utf-8-sig", lineterminator="\n")
    markdown = _markdown(summary, event_detail, feature, return_review)
    LATEST_MD.write_text(markdown, encoding="utf-8", newline="\n")
    DOCS_MD.write_text(markdown, encoding="utf-8", newline="\n")


if __name__ == "__main__":
    raise SystemExit(
        "Use scripts/build_revenue_unreacted_range_research.py --stage forward_confirmation_feature_audit"
    )
