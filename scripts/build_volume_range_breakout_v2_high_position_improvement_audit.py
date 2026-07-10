from __future__ import annotations

from datetime import datetime
from itertools import combinations
from pathlib import Path
from zoneinfo import ZoneInfo
import math

import pandas as pd


ROOT = Path(".")
RESEARCH_LATEST_DIR = ROOT / "output" / "latest" / "research_backtest"
DOCS_LATEST_DIR = ROOT / "docs" / "latest"
RESEARCH_HISTORY_DIR = ROOT / "output" / "history" / "research"
PRICE_HISTORY_DIR = ROOT / "data" / "stock_price_history"

SOURCE_DETAIL_CSV = (
    RESEARCH_LATEST_DIR
    / "volume_range_breakout_v2_position_shape_matrix_detail_latest.csv"
)
RAW_MARKET_DETAIL_CSV = (
    RESEARCH_LATEST_DIR / "volume_range_breakout_v2_raw_market_rerun_detail_latest.csv"
)

LATEST_CSV = (
    RESEARCH_LATEST_DIR
    / "volume_range_breakout_v2_high_position_improvement_audit_latest.csv"
)
LATEST_MD = (
    RESEARCH_LATEST_DIR
    / "volume_range_breakout_v2_high_position_improvement_audit_latest.md"
)
LATEST_DETAIL_CSV = (
    RESEARCH_LATEST_DIR
    / "volume_range_breakout_v2_high_position_improvement_audit_detail_latest.csv"
)
DOCS_LATEST_CSV = (
    DOCS_LATEST_DIR
    / "volume_range_breakout_v2_high_position_improvement_audit_latest.csv"
)
DOCS_LATEST_MD = (
    DOCS_LATEST_DIR
    / "volume_range_breakout_v2_high_position_improvement_audit_latest.md"
)
HISTORY_CSV = (
    RESEARCH_HISTORY_DIR / "volume_range_breakout_v2_high_position_improvement_audit.csv"
)
HISTORY_DETAIL_CSV = (
    RESEARCH_HISTORY_DIR
    / "volume_range_breakout_v2_high_position_improvement_audit_detail.csv"
)

RESEARCH_ID = "volume_range_breakout_v2_high_position_improvement_audit"
ARTIFACT_VERSION = "volume_range_breakout_v2_high_position_improvement_audit_20260710"
SOURCE_RESEARCH_ID = "volume_range_breakout_v2_position_shape_matrix"
RAW_SOURCE_RESEARCH_ID = "volume_range_breakout_v2_raw_market_rerun"
ADVISORY_STATUS = "warning_research_variant_only"
PRODUCTION_READINESS = "not_production_ready_research_only"
PARENT_MODEL_ID = "volume_range_breakout"
CANDIDATE_MODEL_ID = "volume_range_breakout_v2_high_position_volume_attack"
CANDIDATE_MODEL_ZH = "High-position volume attack"

BASE_SCOPE_ID = "d15_close_only_next_day_continuation_ma20_ema23_stop"
BASE_POSITION_AXIS = "position_120d"
BASE_POSITION_BUCKET = "high_pos_gt75"
BASE_SHAPES = {"non_consolidation", "wide_range"}
UNIVERSE_CONDITION_ID = "high_pos_gt75_non_consolidation_or_wide"
UNIVERSE_CONDITION_LABEL = "High-position non-consolidation or wide-range reference universe"
BASE_MODEL_CONDITION_ID = "high_pos_gt75_nonconsolidation_or_wide_ma60_gt_ma120"
BASE_CONDITION_ID = BASE_MODEL_CONDITION_ID
BASE_CONDITION_ZH = "High-position non-consolidation/wide with MA60 > MA120"
WIN_RATE_THRESHOLD_PCT = 60.0

JOIN_KEYS = ["stock_id", "signal_date", "confirmation_date", "entry_date"]

SUMMARY_COLUMNS = [
    "research_id",
    "artifact_version",
    "source_research_id",
    "source_artifact_version",
    "raw_source_research_id",
    "raw_source_artifact_version",
    "advisory_status",
    "parent_model_id",
    "candidate_model_id",
    "candidate_model_zh",
    "row_type",
    "analysis_scope_id",
    "position_axis",
    "base_condition_id",
    "base_condition_zh",
    "feature_family",
    "feature_id",
    "feature_label",
    "condition_expression",
    "condition_role",
    "sample_size",
    "coverage_pct",
    "win_count",
    "neutral_count",
    "loss_count",
    "win_rate_pct",
    "neutral_rate_pct",
    "loss_rate_pct",
    "avg_return_pct",
    "median_return_pct",
    "p10_return_pct",
    "p90_return_pct",
    "baseline_sample_size",
    "baseline_win_rate_pct",
    "baseline_loss_rate_pct",
    "baseline_avg_return_pct",
    "baseline_median_return_pct",
    "win_rate_delta_pct",
    "loss_rate_delta_pct",
    "avg_return_delta_pct",
    "median_return_delta_pct",
    "success_with_feature_count",
    "failure_with_feature_count",
    "success_share_pct",
    "failure_share_pct",
    "success_minus_failure_share_pct",
    "success_median_value",
    "failure_median_value",
    "sample_count_context",
    "candidate_status",
    "decision_hint",
    "approved_for_daily",
    "production_readiness",
    "generated_at",
]

DETAIL_COLUMNS = [
    "research_id",
    "artifact_version",
    "source_research_id",
    "source_artifact_version",
    "raw_source_research_id",
    "raw_source_artifact_version",
    "advisory_status",
    "parent_model_id",
    "candidate_model_id",
    "candidate_model_zh",
    "analysis_scope_id",
    "position_axis",
    "base_condition_id",
    "source_scope_role",
    "base_model_member",
    "source_event_key",
    "stock_id",
    "stock_name",
    "market",
    "market_regime",
    "signal_date",
    "confirmation_date",
    "entry_date",
    "planned_exit_date",
    "exit_date",
    "entry_price",
    "exit_price",
    "return_pct",
    "return_outcome",
    "exit_reason",
    "holding_days",
    "stop_policy_id",
    "signal_open",
    "signal_high",
    "signal_low",
    "signal_close",
    "confirmation_open",
    "confirmation_high",
    "confirmation_low",
    "confirmation_close",
    "signal_close_location_pct",
    "signal_close_location_bucket",
    "signal_body_pct",
    "signal_body_bucket",
    "confirmation_return_pct",
    "confirmation_return_bucket",
    "kd_k_signal",
    "kd_d_signal",
    "kd_j_signal",
    "kd_k_minus_d_signal",
    "kd_k_prev_signal",
    "kd_d_prev_signal",
    "kdj_k_signal",
    "kdj_d_signal",
    "kdj_j_signal",
    "kdj_k_minus_d_signal",
    "kdj_phase",
    "kdj_k_bucket",
    "kdj_j_bucket",
    "kd_phase",
    "kd_k_bucket",
    "kd_j_bucket",
    "kd_bullish_not_overheated",
    "kd_overheated",
    "kd_bull_cross_signal",
    "kd_low_bull_cross_signal",
    "kd_value_rising_3d",
    "pdf_add_score_combo_id",
    "pdf_add_score_features",
    "pdf_add_score_count",
    "shape_bucket",
    "consolidation_type",
    "classification_id",
    "attack_method",
    "risk_type",
    "candle_quality",
    "follow_through_type",
    "limit_up_like",
    "breakout_over_prev60_pct",
    "volume_ratio",
    "signal_return_1d_pct",
    "range_width_20_pct",
    "range_width_60_pct",
    "off_60d_low_pct",
    "position_in_60d_range_pct",
    "off_120d_low_pct",
    "range_width_120_pct",
    "position_in_120d_range_pct",
    "hist_return_20d_pct",
    "hist_return_60d_pct",
    "dist_ema23_pct",
    "ma20_gt_ma60",
    "ma60_gt_ma120",
    "tdcc_list_type",
    "tdcc_rank",
    "tdcc_weekly_increase_top20",
    "tdcc_any_top20",
    "return_valid",
    "approved_for_daily",
    "production_readiness",
    "generated_at",
]


def now_text() -> str:
    return datetime.now(ZoneInfo("Asia/Taipei")).strftime("%Y-%m-%d %H:%M:%S Asia/Taipei")


def read_csv(path: Path) -> pd.DataFrame:
    if not path.exists():
        raise SystemExit(f"ERROR: missing required source: {path}")
    return pd.read_csv(path, dtype=str, keep_default_na=False)


def write_csv(frame: pd.DataFrame, path: Path, columns: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    out = frame.copy()
    for col in columns:
        if col not in out.columns:
            out[col] = ""
    out[columns].to_csv(path, index=False, encoding="utf-8-sig")


def to_float(value: object) -> float:
    text = "" if value is None else str(value).strip()
    if not text:
        return math.nan
    try:
        return float(text)
    except ValueError:
        return math.nan


def pct(value: object) -> str:
    parsed = to_float(value)
    if math.isnan(parsed):
        return ""
    return str(round(parsed, 4))


def boolish(value: object) -> bool:
    return str(value).strip().lower() in {"true", "1", "yes", "y"}


def numeric_series(frame: pd.DataFrame, col: str) -> pd.Series:
    if col not in frame.columns:
        return pd.Series(index=frame.index, dtype=float)
    return pd.to_numeric(frame[col], errors="coerce")


def bucket_float(value: object, cuts: list[tuple[float, str]], fallback: str) -> str:
    parsed = to_float(value)
    if math.isnan(parsed):
        return "missing"
    for limit, label in cuts:
        if parsed <= limit:
            return label
    return fallback


def price_history_path(stock_id: object) -> Path:
    return PRICE_HISTORY_DIR / f"{str(stock_id).strip()}.csv"


def kdj_frame_for_stock(stock_id: object) -> pd.DataFrame:
    path = price_history_path(stock_id)
    if not path.exists():
        return pd.DataFrame()
    price = pd.read_csv(path, dtype=str, keep_default_na=False)
    required = {"date", "high", "low", "close"}
    if not required <= set(price.columns):
        return pd.DataFrame()
    price = price.copy()
    price["date"] = price["date"].astype(str)
    price = price.sort_values("date").reset_index(drop=True)
    high = pd.to_numeric(price["high"], errors="coerce")
    low = pd.to_numeric(price["low"], errors="coerce")
    close = pd.to_numeric(price["close"], errors="coerce")
    low9 = low.rolling(9, min_periods=9).min()
    high9 = high.rolling(9, min_periods=9).max()
    rsv9 = (close - low9) / (high9 - low9).replace(0, pd.NA) * 100.0
    k_value = rsv9.ewm(alpha=1 / 3, adjust=False, min_periods=3).mean()
    d_value = k_value.ewm(alpha=1 / 3, adjust=False, min_periods=3).mean()
    j_value = 3 * k_value - 2 * d_value
    out = pd.DataFrame(
        {
            "date": price["date"],
            "kd_k_signal": k_value,
            "kd_d_signal": d_value,
            "kd_j_signal": j_value,
            "kd_k_prev_signal": k_value.shift(1),
            "kd_d_prev_signal": d_value.shift(1),
            "kd_k_3d_ago": k_value.shift(3),
        }
    )
    out["kd_k_minus_d_signal"] = out["kd_k_signal"] - out["kd_d_signal"]
    return out


def attach_kdj_features(frame: pd.DataFrame) -> pd.DataFrame:
    pieces: list[pd.DataFrame] = []
    stock_ids = sorted(set(frame["stock_id"].astype(str)))
    for stock_id in stock_ids:
        kdj = kdj_frame_for_stock(stock_id)
        if kdj.empty:
            continue
        kdj = kdj.copy()
        kdj["stock_id"] = stock_id
        pieces.append(kdj)
    out = frame.copy()
    if pieces:
        all_kdj = pd.concat(pieces, ignore_index=True)
        out = out.merge(
            all_kdj,
            left_on=["stock_id", "signal_date"],
            right_on=["stock_id", "date"],
            how="left",
        ).drop(columns=["date"], errors="ignore")
    for col in [
        "kd_k_signal",
        "kd_d_signal",
        "kd_j_signal",
        "kd_k_minus_d_signal",
        "kd_k_prev_signal",
        "kd_d_prev_signal",
        "kd_k_3d_ago",
    ]:
        if col not in out.columns:
            out[col] = math.nan
    kd_k = numeric_series(out, "kd_k_signal")
    kd_d = numeric_series(out, "kd_d_signal")
    kd_j = numeric_series(out, "kd_j_signal")
    kd_k_prev = numeric_series(out, "kd_k_prev_signal")
    kd_d_prev = numeric_series(out, "kd_d_prev_signal")
    kd_k_3d_ago = numeric_series(out, "kd_k_3d_ago")
    out["kd_bullish_not_overheated"] = ((kd_k > kd_d) & (kd_k < 80)).fillna(False)
    out["kd_overheated"] = ((kd_k >= 80) | (kd_d >= 80)).fillna(False)
    out["kd_bull_cross_signal"] = ((kd_k >= kd_d) & (kd_k_prev < kd_d_prev)).fillna(False)
    out["kd_low_bull_cross_signal"] = (out["kd_bull_cross_signal"] & (kd_k <= 30)).fillna(False)
    out["kd_value_rising_3d"] = (kd_k > kd_k_3d_ago).fillna(False)
    out["kd_phase"] = "kd_missing"
    out.loc[(kd_k > kd_d) & (kd_k < 80), "kd_phase"] = "kd_bullish_not_overheated"
    out.loc[(kd_k > kd_d) & (kd_k >= 80), "kd_phase"] = "kd_bullish_overheated"
    out.loc[(kd_k <= kd_d) & kd_k.notna() & kd_d.notna(), "kd_phase"] = "kd_bearish_or_flat"
    out["kd_k_bucket"] = kd_k.map(
        lambda value: bucket_float(value, [(30, "kd_k_le30"), (50, "kd_k_30_50"), (80, "kd_k_50_80")], "kd_k_gt80")
    )
    out["kd_j_bucket"] = kd_j.map(
        lambda value: bucket_float(value, [(50, "kd_j_le50"), (100, "kd_j_50_100")], "kd_j_gt100")
    )
    out["kdj_k_signal"] = out["kd_k_signal"]
    out["kdj_d_signal"] = out["kd_d_signal"]
    out["kdj_j_signal"] = out["kd_j_signal"]
    out["kdj_k_minus_d_signal"] = out["kd_k_minus_d_signal"]
    out["kdj_phase"] = out["kd_phase"].str.replace("kd_", "kdj_", regex=False)
    out["kdj_k_bucket"] = out["kd_k_bucket"].str.replace("kd_k_", "kdj_k_", regex=False)
    out["kdj_j_bucket"] = out["kd_j_bucket"].str.replace("kd_j_", "kdj_j_", regex=False)
    return out.drop(columns=["kd_k_3d_ago"], errors="ignore")


def add_feature_columns(frame: pd.DataFrame) -> pd.DataFrame:
    out = frame.copy()
    out["market_regime_bucket"] = out.get("market_regime", "").replace("", "missing")
    out["range60_bucket"] = out["range_width_60_pct"].map(
        lambda value: bucket_float(
            value,
            [(35, "range60_le35"), (45, "range60_35_45"), (60, "range60_45_60")],
            "range60_gt60",
        )
    )
    out["range20_bucket"] = out["range_width_20_pct"].map(
        lambda value: bucket_float(value, [(15, "range20_le15"), (25, "range20_15_25")], "range20_gt25")
    )
    out["off60_bucket"] = out["off_60d_low_pct"].map(
        lambda value: bucket_float(
            value,
            [(35, "off60_le35"), (50, "off60_35_50"), (75, "off60_50_75")],
            "off60_gt75",
        )
    )
    out["hist60_bucket"] = out["hist_return_60d_pct"].map(
        lambda value: bucket_float(
            value,
            [(0, "hist60_le0"), (25, "hist60_0_25"), (50, "hist60_25_50")],
            "hist60_gt50",
        )
    )
    out["volume_bucket"] = out["volume_ratio"].map(
        lambda value: bucket_float(value, [(2, "volume_lt2"), (6, "volume_2_to_6")], "volume_gt6")
    )
    out["breakout_bucket"] = out["breakout_over_prev60_pct"].map(
        lambda value: bucket_float(
            value,
            [(2, "breakout_le2"), (5, "breakout_2_5"), (10, "breakout_5_10")],
            "breakout_gt10",
        )
    )
    out["dist_ema23_bucket"] = out["dist_ema23_pct"].map(
        lambda value: bucket_float(
            value,
            [(0, "dist_ema23_le0"), (15, "dist_ema23_0_15"), (30, "dist_ema23_15_30")],
            "dist_ema23_gt30",
        )
    )

    signal_open = numeric_series(out, "signal_open")
    signal_high = numeric_series(out, "signal_high")
    signal_low = numeric_series(out, "signal_low")
    signal_close = numeric_series(out, "signal_close")
    confirmation_close = numeric_series(out, "confirmation_close")
    signal_range = signal_high - signal_low
    close_location = ((signal_close - signal_low) / signal_range * 100.0).where(signal_range > 0)
    signal_body = ((signal_close - signal_open).abs() / signal_open * 100.0).where(signal_open > 0)
    confirmation_return = ((confirmation_close / signal_close - 1.0) * 100.0).where(signal_close > 0)
    out["signal_close_location_pct"] = close_location
    out["signal_close_location_bucket"] = close_location.map(
        lambda value: bucket_float(value, [(80, "close_loc_le80"), (95, "close_loc_80_95")], "close_loc_gt95")
    )
    out["signal_body_pct"] = signal_body
    out["signal_body_bucket"] = signal_body.map(
        lambda value: bucket_float(value, [(3, "body_le3"), (7, "body_3_7")], "body_gt7")
    )
    out["confirmation_return_pct"] = confirmation_return
    out["confirmation_return_bucket"] = confirmation_return.map(
        lambda value: bucket_float(
            value,
            [(0, "confirm_ret_le0"), (3, "confirm_ret_0_3"), (7, "confirm_ret_3_7")],
            "confirm_ret_gt7",
        )
    )

    out["tdcc_any_top20_bool"] = out.get("tdcc_any_top20", "").map(boolish)
    out["tdcc_weekly_increase_top20_bool"] = out.get("tdcc_weekly_increase_top20", "").map(boolish)
    out["ma60_gt_ma120_bool"] = out.get("ma60_gt_ma120", "").map(boolish)
    out["ma20_gt_ma60_bool"] = out.get("ma20_gt_ma60", "").map(boolish)
    out["limit_up_like_bool"] = out.get("limit_up_like", "").map(boolish)
    out["base_model_member"] = out["ma60_gt_ma120_bool"].map(lambda value: "True" if value else "False")
    out["source_scope_role"] = out["ma60_gt_ma120_bool"].map(
        lambda value: "base_model_member" if value else "reference_universe_only"
    )
    return out


def source_scope() -> pd.DataFrame:
    detail = read_csv(SOURCE_DETAIL_CSV)
    raw = read_csv(RAW_MARKET_DETAIL_CSV)

    source = detail[
        detail["analysis_scope_id"].eq(BASE_SCOPE_ID)
        & detail["position_bucket_120d"].eq(BASE_POSITION_BUCKET)
        & detail["shape_bucket"].isin(BASE_SHAPES)
        & detail["return_valid"].astype(str).str.lower().eq("true")
    ].copy()
    if source.empty:
        raise SystemExit("ERROR: high-position source scope is empty")
    if source["source_event_key"].duplicated().any():
        raise SystemExit("ERROR: high-position source_event_key must be unique")

    raw_cols = [
        "stock_id",
        "signal_date",
        "confirmation_date",
        "entry_date",
        "market",
        "market_regime",
        "classification_id",
        "attack_method",
        "price_position_type",
        "risk_type",
        "candle_quality",
        "signal_open",
        "signal_high",
        "signal_low",
        "signal_close",
        "confirmation_open",
        "confirmation_high",
        "confirmation_low",
        "confirmation_close",
    ]
    missing_raw = sorted(set(raw_cols) - set(raw.columns))
    if missing_raw:
        raise SystemExit(f"ERROR: raw market detail missing columns: {missing_raw}")
    raw_small = raw[raw_cols].drop_duplicates(JOIN_KEYS, keep="first").copy()
    joined = source.merge(raw_small, on=JOIN_KEYS, how="left", suffixes=("", "_raw"))
    for col in [
        "market",
        "market_regime",
        "classification_id",
        "attack_method",
        "risk_type",
        "candle_quality",
    ]:
        if col not in joined.columns:
            joined[col] = ""
        joined[col] = joined[col].fillna("").astype(str).replace("", "missing")
    joined = attach_kdj_features(joined)
    joined = add_feature_columns(joined)
    return add_pdf_combo_columns(joined)


def metric_row(
    frame: pd.DataFrame,
    *,
    row_type: str,
    feature_family: str,
    feature_id: str,
    feature_label: str,
    condition_expression: str,
    condition_role: str,
    baseline: pd.DataFrame,
    generated_at: str,
    source_artifact_version: str,
    raw_source_artifact_version: str,
) -> dict[str, object]:
    returns = numeric_series(frame, "return_pct").dropna()
    sample = len(frame)
    wins = int(frame["return_outcome"].astype(str).eq("win").sum())
    neutrals = int(frame["return_outcome"].astype(str).eq("neutral").sum())
    losses = int(frame["return_outcome"].astype(str).eq("loss").sum())

    base_returns = numeric_series(baseline, "return_pct").dropna()
    base_sample = len(baseline)
    base_wins = int(baseline["return_outcome"].astype(str).eq("win").sum())
    base_losses = int(baseline["return_outcome"].astype(str).eq("loss").sum())

    win_rate = wins / sample * 100.0 if sample else math.nan
    neutral_rate = neutrals / sample * 100.0 if sample else math.nan
    loss_rate = losses / sample * 100.0 if sample else math.nan
    avg_ret = returns.mean() if len(returns) else math.nan
    median_ret = returns.median() if len(returns) else math.nan
    base_win_rate = base_wins / base_sample * 100.0 if base_sample else math.nan
    base_loss_rate = base_losses / base_sample * 100.0 if base_sample else math.nan
    base_avg_ret = base_returns.mean() if len(base_returns) else math.nan
    base_median_ret = base_returns.median() if len(base_returns) else math.nan

    candidate_status = "research_only_not_candidate_metric"
    if sample and win_rate >= WIN_RATE_THRESHOLD_PCT and avg_ret > 0 and median_ret > 0:
        candidate_status = "research_only_candidate_metric_met"
    elif sample and avg_ret > 0 and median_ret > 0:
        candidate_status = "research_only_positive_return_but_win_below_threshold"

    if row_type == "reference_universe":
        decision_hint = "reference_only_before_ma60_filter"
    elif row_type == "baseline":
        decision_hint = "base_model_research_only_candidate_met"
    elif row_type == "pdf_bonus_combo":
        decision_hint = "pdf_row_combo_metric_research_only"
    elif condition_role.startswith("add_score") and candidate_status == "research_only_candidate_metric_met":
        decision_hint = "add_score_candidate_research_only"
    elif condition_role.startswith("risk_filter") and sample and win_rate > base_win_rate:
        decision_hint = "risk_filter_candidate_research_only"
    elif sample and loss_rate > base_loss_rate and win_rate < base_win_rate:
        decision_hint = "risk_or_negative_stratification_subject"
    elif sample and win_rate > base_win_rate:
        decision_hint = "positive_stratification_research_only"
    else:
        decision_hint = "weak_or_mixed_feature_difference"

    return {
        "research_id": RESEARCH_ID,
        "artifact_version": ARTIFACT_VERSION,
        "source_research_id": SOURCE_RESEARCH_ID,
        "source_artifact_version": source_artifact_version,
        "raw_source_research_id": RAW_SOURCE_RESEARCH_ID,
        "raw_source_artifact_version": raw_source_artifact_version,
        "advisory_status": ADVISORY_STATUS,
        "parent_model_id": PARENT_MODEL_ID,
        "candidate_model_id": CANDIDATE_MODEL_ID,
        "candidate_model_zh": CANDIDATE_MODEL_ZH,
        "row_type": row_type,
        "analysis_scope_id": BASE_SCOPE_ID,
        "position_axis": BASE_POSITION_AXIS,
        "base_condition_id": BASE_CONDITION_ID,
        "base_condition_zh": BASE_CONDITION_ZH,
        "feature_family": feature_family,
        "feature_id": feature_id,
        "feature_label": feature_label,
        "condition_expression": condition_expression,
        "condition_role": condition_role,
        "sample_size": sample,
        "coverage_pct": pct(sample / base_sample * 100.0 if base_sample else math.nan),
        "win_count": wins,
        "neutral_count": neutrals,
        "loss_count": losses,
        "win_rate_pct": pct(win_rate),
        "neutral_rate_pct": pct(neutral_rate),
        "loss_rate_pct": pct(loss_rate),
        "avg_return_pct": pct(avg_ret),
        "median_return_pct": pct(median_ret),
        "p10_return_pct": pct(returns.quantile(0.10) if len(returns) else math.nan),
        "p90_return_pct": pct(returns.quantile(0.90) if len(returns) else math.nan),
        "baseline_sample_size": base_sample,
        "baseline_win_rate_pct": pct(base_win_rate),
        "baseline_loss_rate_pct": pct(base_loss_rate),
        "baseline_avg_return_pct": pct(base_avg_ret),
        "baseline_median_return_pct": pct(base_median_ret),
        "win_rate_delta_pct": pct(win_rate - base_win_rate),
        "loss_rate_delta_pct": pct(loss_rate - base_loss_rate),
        "avg_return_delta_pct": pct(avg_ret - base_avg_ret),
        "median_return_delta_pct": pct(median_ret - base_median_ret),
        "success_with_feature_count": "",
        "failure_with_feature_count": "",
        "success_share_pct": "",
        "failure_share_pct": "",
        "success_minus_failure_share_pct": "",
        "success_median_value": "",
        "failure_median_value": "",
        "sample_count_context": "reported_not_a_disqualifier",
        "candidate_status": candidate_status,
        "decision_hint": decision_hint,
        "approved_for_daily": "False",
        "production_readiness": PRODUCTION_READINESS,
        "generated_at": generated_at,
    }


def append_metric(
    rows: list[dict[str, object]],
    frame: pd.DataFrame,
    *,
    row_type: str,
    feature_family: str,
    feature_id: str,
    feature_label: str,
    condition_expression: str,
    condition_role: str,
    baseline: pd.DataFrame,
    generated_at: str,
    source_artifact_version: str,
    raw_source_artifact_version: str,
) -> None:
    rows.append(
        metric_row(
            frame,
            row_type=row_type,
            feature_family=feature_family,
            feature_id=feature_id,
            feature_label=feature_label,
            condition_expression=condition_expression,
            condition_role=condition_role,
            baseline=baseline,
            generated_at=generated_at,
            source_artifact_version=source_artifact_version,
            raw_source_artifact_version=raw_source_artifact_version,
        )
    )


def add_feature_slices(
    rows: list[dict[str, object]],
    baseline: pd.DataFrame,
    generated_at: str,
    source_artifact_version: str,
    raw_source_artifact_version: str,
) -> None:
    categorical_features = [
        ("shape", "shape_bucket", "shape_bucket"),
        ("market", "market_regime_bucket", "market_regime"),
        ("market", "market", "market"),
        ("classification", "classification_id", "classification_id"),
        ("classification", "attack_method", "attack_method"),
        ("classification", "risk_type", "risk_type"),
        ("classification", "candle_quality", "candle_quality"),
        ("price_shape_60d", "range60_bucket", "range_width_60_pct bucket"),
        ("price_shape_60d", "range20_bucket", "range_width_20_pct bucket"),
        ("price_shape_60d", "off60_bucket", "off_60d_low_pct bucket"),
        ("price_shape_60d", "hist60_bucket", "hist_return_60d_pct bucket"),
        ("technical", "volume_bucket", "volume_ratio bucket"),
        ("technical", "breakout_bucket", "breakout_over_prev60_pct bucket"),
        ("technical", "dist_ema23_bucket", "dist_ema23_pct bucket"),
        ("technical", "signal_close_location_bucket", "signal close location bucket"),
        ("technical", "signal_body_bucket", "signal body pct bucket"),
        ("technical", "confirmation_return_bucket", "confirmation return pct bucket"),
        ("technical_kdj", "kdj_phase", "KDJ phase"),
        ("technical_kdj", "kdj_k_bucket", "KDJ K bucket"),
        ("technical_kdj", "kdj_j_bucket", "KDJ J bucket"),
        ("technical_kdj", "kd_phase", "legacy KD phase alias"),
        ("technical_kdj", "kd_k_bucket", "legacy KD K bucket alias"),
        ("technical_kdj", "kd_j_bucket", "legacy KD J bucket alias"),
        ("tdcc", "tdcc_list_type", "tdcc_list_type"),
    ]
    for family, col, label in categorical_features:
        if col not in baseline.columns:
            continue
        for value in sorted(str(v) for v in baseline[col].fillna("").unique()):
            if value == "":
                continue
            mask = baseline[col].astype(str).eq(value)
            append_metric(
                rows,
                baseline[mask].copy(),
                row_type="feature_slice",
                feature_family=family,
                feature_id=f"{col}={value}",
                feature_label=f"{label}: {value}",
                condition_expression=f"{col} == {value}",
                condition_role="stratification_research_only_not_hidden_gate",
                baseline=baseline,
                generated_at=generated_at,
                source_artifact_version=source_artifact_version,
                raw_source_artifact_version=raw_source_artifact_version,
            )

    boolean_features = [
        ("tdcc", "tdcc_weekly_increase_top20_bool", "TDCC weekly increase top20"),
        ("tdcc", "tdcc_any_top20_bool", "TDCC any top20"),
        ("technical", "ma20_gt_ma60_bool", "MA20 > MA60"),
        ("technical", "limit_up_like_bool", "limit-up-like signal"),
        ("technical_kdj", "kd_bullish_not_overheated", "KDJ K>D and K not overheated"),
        ("technical_kdj", "kd_overheated", "KDJ K or D overheated"),
        ("technical_kdj", "kd_bull_cross_signal", "KDJ K/D bull cross on signal date"),
        ("technical_kdj", "kd_low_bull_cross_signal", "KDJ low-zone bull cross on signal date"),
        ("technical_kdj", "kd_value_rising_3d", "KDJ K rising vs three days ago"),
    ]
    for family, col, label in boolean_features:
        if col not in baseline.columns:
            continue
        append_metric(
            rows,
            baseline[baseline[col].astype(bool)].copy(),
            row_type="feature_slice",
            feature_family=family,
            feature_id=col,
            feature_label=label,
            condition_expression=f"{col} is True",
            condition_role="stratification_research_only_not_hidden_gate",
            baseline=baseline,
            generated_at=generated_at,
            source_artifact_version=source_artifact_version,
            raw_source_artifact_version=raw_source_artifact_version,
        )


def add_candidate_conditions(
    rows: list[dict[str, object]],
    baseline: pd.DataFrame,
    generated_at: str,
    source_artifact_version: str,
    raw_source_artifact_version: str,
) -> None:
    candidates = [
        (
            "high_pos_base_plus_market_mild_bull",
            "base + mild_bull market regime",
            "base condition and market_regime == mild_bull",
            baseline["market_regime_bucket"].eq("mild_bull"),
            "add_score_research_only_not_hidden_gate",
        ),
        (
            "high_pos_base_plus_tdcc_any_top20",
            "base + TDCC any top20",
            "base condition and tdcc_any_top20",
            baseline["tdcc_any_top20_bool"].astype(bool),
            "add_score_research_only_not_hidden_gate",
        ),
        (
            "high_pos_base_plus_tdcc_weekly_increase_top20",
            "base + TDCC weekly increase top20",
            "base condition and tdcc_weekly_increase_top20",
            baseline["tdcc_weekly_increase_top20_bool"].astype(bool),
            "add_score_research_only_not_hidden_gate",
        ),
        (
            "high_pos_base_plus_ma20_gt_ma60",
            "base + MA20 > MA60",
            "base condition and ma20_gt_ma60",
            baseline["ma20_gt_ma60_bool"].astype(bool),
            "add_score_research_only_not_hidden_gate",
        ),
        (
            "high_pos_base_plus_ret20_0_25",
            "base + 20d return 0%..25%",
            "base condition and 0 <= hist_return_20d_pct <= 25",
            numeric_series(baseline, "hist_return_20d_pct").between(0, 25, inclusive="both"),
            "add_score_research_only_not_hidden_gate",
        ),
        (
            "high_pos_base_plus_volume_2_to_6",
            "base + volume ratio 2..6",
            "base condition and 2 <= volume_ratio <= 6",
            baseline["volume_bucket"].eq("volume_2_to_6"),
            "add_score_research_only_not_hidden_gate",
        ),
        (
            "high_pos_base_plus_volume_lt2",
            "base + volume ratio <=2",
            "base condition and volume_ratio <= 2",
            baseline["volume_bucket"].eq("volume_lt2"),
            "add_score_research_only_not_hidden_gate",
        ),
        (
            "high_pos_base_plus_not_limit_up_like",
            "base + not limit-up-like",
            "base condition and limit_up_like is False",
            ~baseline["limit_up_like_bool"].astype(bool),
            "add_score_research_only_not_hidden_gate",
        ),
        (
            "high_pos_base_plus_breakout_2_5",
            "base + breakout over prev60 2%..5%",
            "base condition and 2 < breakout_over_prev60_pct <= 5",
            baseline["breakout_bucket"].eq("breakout_2_5"),
            "add_score_research_only_not_hidden_gate",
        ),
        (
            "high_pos_base_plus_close_location_gt95",
            "base + signal close location >95%",
            "base condition and signal_close_location_bucket == close_loc_gt95",
            baseline["signal_close_location_bucket"].eq("close_loc_gt95"),
            "add_score_research_only_not_hidden_gate",
        ),
        (
            "high_pos_base_plus_close_location_le80",
            "base + signal close location <=80%",
            "base condition and signal_close_location_bucket == close_loc_le80",
            baseline["signal_close_location_bucket"].eq("close_loc_le80"),
            "add_score_research_only_not_hidden_gate",
        ),
        (
            "high_pos_base_plus_signal_body_le3",
            "base + signal candle body <=3%",
            "base condition and signal_body_bucket == body_le3",
            baseline["signal_body_bucket"].eq("body_le3"),
            "add_score_research_only_not_hidden_gate",
        ),
        (
            "high_pos_base_plus_signal_body_3_7",
            "base + signal candle body 3%..7%",
            "base condition and signal_body_bucket == body_3_7",
            baseline["signal_body_bucket"].eq("body_3_7"),
            "add_score_research_only_not_hidden_gate",
        ),
        (
            "high_pos_base_plus_confirmation_return_3_7",
            "base + confirmation return 3%..7%",
            "base condition and confirmation_return_bucket == confirm_ret_3_7",
            baseline["confirmation_return_bucket"].eq("confirm_ret_3_7"),
            "add_score_research_only_not_hidden_gate",
        ),
        (
            "high_pos_base_plus_kd_bullish_not_overheated",
            "base + legacy KD alias bullish not overheated",
            "base condition and KDJ K > D and K < 80 on signal date",
            baseline["kd_bullish_not_overheated"].astype(bool),
            "add_score_research_only_not_hidden_gate",
        ),
        (
            "high_pos_base_plus_kd_value_rising_3d",
            "base + legacy KD alias K rising vs three days ago",
            "base condition and KDJ K signal > K signal lag3",
            baseline["kd_value_rising_3d"].astype(bool),
            "add_score_research_only_not_hidden_gate",
        ),
        (
            "high_pos_base_plus_kd_bull_cross_signal",
            "base + legacy KD alias bull cross on signal date",
            "base condition and KDJ K crosses above D on signal date",
            baseline["kd_bull_cross_signal"].astype(bool),
            "add_score_research_only_not_hidden_gate",
        ),
        (
            "high_pos_base_plus_kd_not_overheated",
            "base + legacy KD alias not overheated",
            "base condition and KDJ K < 80 and D < 80 on signal date",
            (~baseline["kd_overheated"].astype(bool)) & numeric_series(baseline, "kd_k_signal").notna(),
            "add_score_research_only_not_hidden_gate",
        ),
        (
            "high_pos_base_plus_kdj_bullish_not_overheated",
            "base + KDJ K>D and K not overheated",
            "base condition and KDJ K > D and K < 80 on signal date",
            baseline["kd_bullish_not_overheated"].astype(bool),
            "add_score_research_only_not_hidden_gate",
        ),
        (
            "high_pos_base_plus_kdj_overheated",
            "base + KDJ K or D overheated",
            "base condition and KDJ K >= 80 or D >= 80 on signal date",
            baseline["kd_overheated"].astype(bool),
            "add_score_research_only_not_hidden_gate",
        ),
        (
            "high_pos_base_plus_kdj_j_gt100",
            "base + KDJ J > 100",
            "base condition and KDJ J > 100 on signal date",
            baseline["kdj_j_bucket"].eq("kdj_j_gt100"),
            "add_score_research_only_not_hidden_gate",
        ),
        (
            "high_pos_base_plus_confirmation_return_gt3",
            "base + confirmation return >3%",
            "base condition and confirmation_return_pct > 3",
            baseline["confirmation_return_bucket"].isin({"confirm_ret_3_7", "confirm_ret_gt7"}),
            "add_score_research_only_not_hidden_gate",
        ),
        (
            "high_pos_base_plus_dist_ema23_0_15",
            "base + close distance to EMA23 0%..15%",
            "base condition and 0 < dist_ema23_pct <= 15",
            baseline["dist_ema23_bucket"].eq("dist_ema23_0_15"),
            "add_score_research_only_not_hidden_gate",
        ),
        (
            "high_pos_base_exclude_volume_gt6",
            "base excluding volume ratio >6",
            "base condition and volume_bucket != volume_gt6",
            ~baseline["volume_bucket"].eq("volume_gt6"),
            "risk_filter_research_only_not_hidden_gate",
        ),
    ]
    for fid, label, expression, mask, role in candidates:
        append_metric(
            rows,
            baseline[mask].copy(),
            row_type="candidate_condition",
            feature_family="combo",
            feature_id=fid,
            feature_label=label,
            condition_expression=expression,
            condition_role=role,
            baseline=baseline,
            generated_at=generated_at,
            source_artifact_version=source_artifact_version,
            raw_source_artifact_version=raw_source_artifact_version,
        )


def feature_gap_row(
    baseline: pd.DataFrame,
    *,
    feature_family: str,
    feature_id: str,
    feature_label: str,
    condition_expression: str,
    mask: pd.Series,
    generated_at: str,
    source_artifact_version: str,
    raw_source_artifact_version: str,
    numeric_col: str = "",
) -> dict[str, object]:
    mask = mask.reindex(baseline.index).fillna(False).astype(bool)
    success = baseline[baseline["return_outcome"].astype(str).eq("win")].copy()
    failure = baseline[baseline["return_outcome"].astype(str).eq("loss")].copy()
    success_mask = mask.loc[success.index] if len(success) else pd.Series(dtype=bool)
    failure_mask = mask.loc[failure.index] if len(failure) else pd.Series(dtype=bool)
    success_count = int(success_mask.sum()) if len(success_mask) else 0
    failure_count = int(failure_mask.sum()) if len(failure_mask) else 0
    success_share = success_count / len(success) * 100.0 if len(success) else math.nan
    failure_share = failure_count / len(failure) * 100.0 if len(failure) else math.nan

    if numeric_col:
        success_median = numeric_series(success, numeric_col).median()
        failure_median = numeric_series(failure, numeric_col).median()
    else:
        success_median = math.nan
        failure_median = math.nan

    gap = success_share - failure_share if not math.isnan(success_share) and not math.isnan(failure_share) else math.nan
    if numeric_col:
        hint = "numeric_feature_gap_for_win_loss_review"
    elif gap >= 10:
        hint = "success_feature_overrepresented_research_only"
    elif gap <= -10:
        hint = "failure_feature_overrepresented_risk_review"
    else:
        hint = "weak_or_mixed_win_loss_feature_gap"

    row = metric_row(
        baseline[mask].copy(),
        row_type="feature_gap",
        feature_family=feature_family,
        feature_id=feature_id,
        feature_label=feature_label,
        condition_expression=condition_expression,
        condition_role="win_loss_feature_gap_research_only_not_hidden_gate",
        baseline=baseline,
        generated_at=generated_at,
        source_artifact_version=source_artifact_version,
        raw_source_artifact_version=raw_source_artifact_version,
    )
    row.update(
        {
            "success_with_feature_count": success_count,
            "failure_with_feature_count": failure_count,
            "success_share_pct": pct(success_share),
            "failure_share_pct": pct(failure_share),
            "success_minus_failure_share_pct": pct(gap),
            "success_median_value": pct(success_median) if numeric_col else "",
            "failure_median_value": pct(failure_median) if numeric_col else "",
            "decision_hint": hint,
        }
    )
    return row


def add_gap_rows(
    rows: list[dict[str, object]],
    baseline: pd.DataFrame,
    generated_at: str,
    source_artifact_version: str,
    raw_source_artifact_version: str,
) -> None:
    gap_features = [
        ("tdcc", "tdcc_weekly_increase_top20_bool", "TDCC weekly increase top20", "tdcc_weekly_increase_top20_bool is True", ""),
        ("tdcc", "tdcc_any_top20_bool", "TDCC any top20", "tdcc_any_top20_bool is True", ""),
        ("technical", "ma20_gt_ma60_bool", "MA20 > MA60", "ma20_gt_ma60_bool is True", ""),
        ("technical", "limit_up_like_bool", "limit-up-like signal", "limit_up_like_bool is True", ""),
        ("technical", "volume_bucket=volume_gt6", "volume ratio > 6", "volume_bucket == volume_gt6", ""),
        ("technical", "volume_bucket=volume_2_to_6", "volume ratio 2..6", "volume_bucket == volume_2_to_6", ""),
        ("technical", "breakout_bucket=breakout_2_5", "breakout over prev60 2%..5%", "breakout_bucket == breakout_2_5", ""),
        ("technical", "dist_ema23_bucket=dist_ema23_0_15", "distance to EMA23 0%..15%", "dist_ema23_bucket == dist_ema23_0_15", ""),
        ("technical", "signal_close_location_bucket=close_loc_gt95", "signal close location >95%", "signal_close_location_bucket == close_loc_gt95", ""),
        ("technical", "signal_body_bucket=body_3_7", "signal body 3%..7%", "signal_body_bucket == body_3_7", ""),
        ("technical", "confirmation_return_bucket=confirm_ret_3_7", "confirmation return 3%..7%", "confirmation_return_bucket == confirm_ret_3_7", ""),
        ("technical", "confirmation_return_bucket=confirm_ret_gt7", "confirmation return >7%", "confirmation_return_bucket == confirm_ret_gt7", ""),
        ("technical_kdj", "kd_bullish_not_overheated", "legacy KD alias: KDJ K>D and K not overheated", "kd_bullish_not_overheated is True", ""),
        ("technical_kdj", "kd_overheated", "legacy KD alias: KDJ K or D overheated", "kd_overheated is True", ""),
        ("technical_kdj", "kd_bull_cross_signal", "legacy KD alias: KDJ K/D bull cross on signal date", "kd_bull_cross_signal is True", ""),
        ("technical_kdj", "kd_value_rising_3d", "legacy KD alias: KDJ K rising vs three days ago", "kd_value_rising_3d is True", ""),
        ("technical_kdj", "kd_phase=kd_bullish_not_overheated", "legacy KD alias: KDJ bullish not overheated phase", "kd_phase == kd_bullish_not_overheated", ""),
        ("technical_kdj", "kdj_phase=kdj_bullish_not_overheated", "KDJ bullish not overheated phase", "kdj_phase == kdj_bullish_not_overheated", ""),
        ("technical_kdj", "kd_k_bucket=kd_k_50_80", "legacy KD alias: KDJ K 50..80", "kd_k_bucket == kd_k_50_80", ""),
        ("technical_kdj", "kdj_k_bucket=kdj_k_50_80", "KDJ K 50..80", "kdj_k_bucket == kdj_k_50_80", ""),
        ("technical_kdj", "kd_k_bucket=kd_k_gt80", "legacy KD alias: KDJ K > 80", "kd_k_bucket == kd_k_gt80", ""),
        ("technical_kdj", "kdj_j_bucket=kdj_j_gt100", "KDJ J > 100", "kdj_j_bucket == kdj_j_gt100", ""),
        ("market", "market_regime_bucket=mild_bull", "market regime mild_bull", "market_regime_bucket == mild_bull", ""),
        ("price_shape_60d", "range60_bucket=range60_gt60", "range 60d > 60", "range60_bucket == range60_gt60", ""),
        ("price_shape_60d", "shape_bucket=wide_range", "wide range shape", "shape_bucket == wide_range", ""),
        ("price_shape_60d", "shape_bucket=non_consolidation", "non consolidation shape", "shape_bucket == non_consolidation", ""),
    ]
    for family, fid, label, expression, numeric_col in gap_features:
        if "=" in fid:
            col, value = fid.split("=", 1)
            mask = baseline[col].astype(str).eq(value)
        else:
            mask = baseline[fid].astype(bool)
        rows.append(
            feature_gap_row(
                baseline,
                feature_family=family,
                feature_id=fid,
                feature_label=label,
                condition_expression=expression,
                mask=mask,
                generated_at=generated_at,
                source_artifact_version=source_artifact_version,
                raw_source_artifact_version=raw_source_artifact_version,
                numeric_col=numeric_col,
            )
        )

    for col in [
        "breakout_over_prev60_pct",
        "volume_ratio",
        "range_width_20_pct",
        "range_width_60_pct",
        "hist_return_20d_pct",
        "hist_return_60d_pct",
        "dist_ema23_pct",
        "signal_close_location_pct",
        "signal_body_pct",
        "confirmation_return_pct",
        "kd_k_signal",
        "kd_d_signal",
        "kd_j_signal",
        "kd_k_minus_d_signal",
    ]:
        median_value = numeric_series(baseline, col).median()
        if pd.isna(median_value):
            continue
        rows.append(
            feature_gap_row(
                baseline,
                feature_family="numeric_median",
                feature_id=f"{col}_ge_median",
                feature_label=f"{col} >= median",
                condition_expression=f"{col} >= {round(float(median_value), 4)}",
                mask=numeric_series(baseline, col).ge(float(median_value)),
                generated_at=generated_at,
                source_artifact_version=source_artifact_version,
                raw_source_artifact_version=raw_source_artifact_version,
                numeric_col=col,
            )
        )


def selected_add_score_masks(baseline: pd.DataFrame) -> dict[str, pd.Series]:
    return {
        "mild_bull": baseline["market_regime_bucket"].eq("mild_bull"),
        "not_limit_up_like": ~baseline["limit_up_like_bool"].astype(bool),
        "breakout_2_5": baseline["breakout_bucket"].eq("breakout_2_5"),
        "volume_lt2": baseline["volume_bucket"].eq("volume_lt2"),
        "signal_body_le3": baseline["signal_body_bucket"].eq("body_le3"),
        "close_location_le80": baseline["signal_close_location_bucket"].eq("close_loc_le80"),
    }


def add_pdf_combo_columns(frame: pd.DataFrame) -> pd.DataFrame:
    out = frame.copy()
    masks = selected_add_score_masks(out)
    feature_lists: list[list[str]] = []
    for idx in out.index:
        features = [name for name, mask in masks.items() if bool(mask.reindex(out.index).fillna(False).loc[idx])]
        feature_lists.append(features)
    out["pdf_add_score_features"] = [";".join(features) if features else "none" for features in feature_lists]
    out["pdf_add_score_count"] = [len(features) for features in feature_lists]
    out["pdf_add_score_combo_id"] = [
        "pdf_combo__" + "__".join(features) if features else "pdf_combo__none"
        for features in feature_lists
    ]
    return out


def add_pdf_combo_rows(
    rows: list[dict[str, object]],
    baseline: pd.DataFrame,
    generated_at: str,
    source_artifact_version: str,
    raw_source_artifact_version: str,
) -> None:
    combo_ids = baseline["pdf_add_score_combo_id"].fillna("pdf_combo__none").astype(str)
    for combo_id in sorted(combo_ids.unique()):
        part = baseline[combo_ids.eq(combo_id)].copy()
        if part.empty:
            continue
        features = str(part["pdf_add_score_features"].iloc[0])
        count = str(part["pdf_add_score_count"].iloc[0])
        append_metric(
            rows,
            part,
            row_type="pdf_bonus_combo",
            feature_family="pdf_bonus_combo",
            feature_id=combo_id,
            feature_label=features,
            condition_expression=f"exact PDF add-score combo == {features}; add_score_count == {count}",
            condition_role="pdf_metric_combo_research_only_not_hidden_gate",
            baseline=baseline,
            generated_at=generated_at,
            source_artifact_version=source_artifact_version,
            raw_source_artifact_version=raw_source_artifact_version,
        )


def add_overlap_rows(
    rows: list[dict[str, object]],
    baseline: pd.DataFrame,
    generated_at: str,
    source_artifact_version: str,
    raw_source_artifact_version: str,
) -> None:
    masks = selected_add_score_masks(baseline)
    if not masks:
        return
    score_count = pd.Series(0, index=baseline.index)
    for mask in masks.values():
        score_count = score_count + mask.reindex(baseline.index).fillna(False).astype(bool).astype(int)

    for threshold in [1, 2, 3, 4]:
        mask = score_count.ge(threshold)
        append_metric(
            rows,
            baseline[mask].copy(),
            row_type="overlap_condition",
            feature_family="overlap_score_count",
            feature_id=f"add_score_count_ge{threshold}",
            feature_label=f"at least {threshold} selected add-score features",
            condition_expression=f"selected_add_score_count >= {threshold}",
            condition_role="overlap_research_only_not_hidden_gate",
            baseline=baseline,
            generated_at=generated_at,
            source_artifact_version=source_artifact_version,
            raw_source_artifact_version=raw_source_artifact_version,
        )

    names = list(masks)
    for left, right in combinations(names, 2):
        mask = masks[left].reindex(baseline.index).fillna(False).astype(bool) & masks[right].reindex(
            baseline.index
        ).fillna(False).astype(bool)
        if not mask.any():
            continue
        append_metric(
            rows,
            baseline[mask].copy(),
            row_type="overlap_condition",
            feature_family="overlap_pair",
            feature_id=f"overlap__{left}__{right}",
            feature_label=f"{left} and {right}",
            condition_expression=f"{left} and {right}",
            condition_role="overlap_research_only_not_hidden_gate",
            baseline=baseline,
            generated_at=generated_at,
            source_artifact_version=source_artifact_version,
            raw_source_artifact_version=raw_source_artifact_version,
        )

    for name, raw_mask in masks.items():
        mask = raw_mask.reindex(baseline.index).fillna(False).astype(bool) & score_count.eq(1)
        if not mask.any():
            continue
        append_metric(
            rows,
            baseline[mask].copy(),
            row_type="overlap_condition",
            feature_family="overlap_unique",
            feature_id=f"unique__{name}",
            feature_label=f"{name} only",
            condition_expression=f"{name} and no other selected add-score feature",
            condition_role="overlap_research_only_not_hidden_gate",
            baseline=baseline,
            generated_at=generated_at,
            source_artifact_version=source_artifact_version,
            raw_source_artifact_version=raw_source_artifact_version,
        )


def build_summary(detail: pd.DataFrame, generated_at: str) -> pd.DataFrame:
    source_artifact_version = str(detail.get("artifact_version", pd.Series([""])).iloc[0])
    raw = read_csv(RAW_MARKET_DETAIL_CSV)
    raw_source_artifact_version = str(raw.get("artifact_version", pd.Series([""])).iloc[0])

    universe = detail.copy()
    baseline = detail[detail["base_model_member"].eq("True")].copy()
    if universe.empty:
        raise SystemExit("ERROR: high-position reference universe is empty")
    if baseline.empty:
        raise SystemExit("ERROR: high-position MA60>MA120 baseline is empty")

    rows: list[dict[str, object]] = []
    append_metric(
        rows,
        universe,
        row_type="reference_universe",
        feature_family="reference_universe",
        feature_id=UNIVERSE_CONDITION_ID,
        feature_label=UNIVERSE_CONDITION_LABEL,
        condition_expression="position_bucket_120d == high_pos_gt75 and shape_bucket in {non_consolidation, wide_range}",
        condition_role="reference_universe_research_only_not_hidden_gate",
        baseline=universe,
        generated_at=generated_at,
        source_artifact_version=source_artifact_version,
        raw_source_artifact_version=raw_source_artifact_version,
    )
    append_metric(
        rows,
        baseline,
        row_type="baseline",
        feature_family="baseline",
        feature_id=BASE_MODEL_CONDITION_ID,
        feature_label=BASE_CONDITION_ZH,
        condition_expression="position_bucket_120d == high_pos_gt75 and shape_bucket in {non_consolidation, wide_range} and ma60_gt_ma120",
        condition_role="baseline_research_only_not_hidden_gate",
        baseline=baseline,
        generated_at=generated_at,
        source_artifact_version=source_artifact_version,
        raw_source_artifact_version=raw_source_artifact_version,
    )
    add_feature_slices(rows, baseline, generated_at, source_artifact_version, raw_source_artifact_version)
    add_candidate_conditions(rows, baseline, generated_at, source_artifact_version, raw_source_artifact_version)
    add_pdf_combo_rows(rows, baseline, generated_at, source_artifact_version, raw_source_artifact_version)
    add_overlap_rows(rows, baseline, generated_at, source_artifact_version, raw_source_artifact_version)
    add_gap_rows(rows, baseline, generated_at, source_artifact_version, raw_source_artifact_version)
    return pd.DataFrame(rows)


def detail_output(detail: pd.DataFrame, generated_at: str) -> pd.DataFrame:
    out = detail.copy()
    source_artifact_version = str(out.get("artifact_version", pd.Series([""])).iloc[0])
    raw = read_csv(RAW_MARKET_DETAIL_CSV)
    out["research_id"] = RESEARCH_ID
    out["artifact_version"] = ARTIFACT_VERSION
    out["source_research_id"] = SOURCE_RESEARCH_ID
    out["source_artifact_version"] = source_artifact_version
    out["raw_source_research_id"] = RAW_SOURCE_RESEARCH_ID
    out["raw_source_artifact_version"] = str(raw.get("artifact_version", pd.Series([""])).iloc[0])
    out["advisory_status"] = ADVISORY_STATUS
    out["parent_model_id"] = PARENT_MODEL_ID
    out["candidate_model_id"] = CANDIDATE_MODEL_ID
    out["candidate_model_zh"] = CANDIDATE_MODEL_ZH
    out["analysis_scope_id"] = BASE_SCOPE_ID
    out["position_axis"] = BASE_POSITION_AXIS
    out["base_condition_id"] = BASE_CONDITION_ID
    out["approved_for_daily"] = "False"
    out["production_readiness"] = PRODUCTION_READINESS
    out["generated_at"] = generated_at
    return out


def md_table(frame: pd.DataFrame, columns: list[str], limit: int | None = None) -> list[str]:
    subset = frame.copy()
    if limit is not None:
        subset = subset.head(limit)
    rows = ["| " + " | ".join(columns) + " |", "| " + " | ".join("---" for _ in columns) + " |"]
    for _, row in subset.iterrows():
        rows.append("| " + " | ".join(str(row.get(col, "")) for col in columns) + " |")
    return rows


def write_md(summary: pd.DataFrame, path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    lines = [
        "# volume_range_breakout v2 high-position improvement audit",
        "",
        "- status: research-only; no production registry, ranking, operation adapter, packet, or PDF change.",
        "- reference universe: 120d high position + non-consolidation or wide-range shape.",
        "- baseline model for this audit: reference universe + MA60 > MA120.",
        "- add-score rule: mild_bull and other technical/TDCC features are research-only score candidates, not hidden buy gates.",
        "- operation basis: D+15 close-only next-day continuation with MA20/EMA23 four-close stop from the source artifact.",
        "- sample_count_context: sample count is reported, not used as an automatic disqualifier.",
        "",
        "## Reference Universe And Baseline",
        "",
    ]
    base_rows = summary[summary["row_type"].isin({"reference_universe", "baseline"})].copy()
    lines.extend(
        md_table(
            base_rows,
            [
                "row_type",
                "feature_id",
                "sample_size",
                "win_rate_pct",
                "neutral_rate_pct",
                "loss_rate_pct",
                "avg_return_pct",
                "median_return_pct",
                "candidate_status",
            ],
        )
    )
    candidates = summary[summary["row_type"].eq("candidate_condition")].copy()
    candidates["_win"] = pd.to_numeric(candidates["win_rate_pct"], errors="coerce")
    candidates["_sample"] = pd.to_numeric(candidates["sample_size"], errors="coerce")
    candidates = candidates.sort_values(["candidate_status", "_win", "_sample"], ascending=[True, False, False])
    lines.extend(["", "## Add-Score / Risk-Filter Candidate Conditions", ""])
    lines.extend(
        md_table(
            candidates,
            [
                "feature_id",
                "condition_role",
                "sample_size",
                "win_rate_pct",
                "loss_rate_pct",
                "avg_return_pct",
                "median_return_pct",
                "candidate_status",
                "decision_hint",
            ],
            limit=30,
        )
    )
    pdf_combos = summary[summary["row_type"].eq("pdf_bonus_combo")].copy()
    pdf_combos["_count"] = pdf_combos["feature_label"].astype(str).map(
        lambda value: 0 if value == "none" else len([part for part in value.split(";") if part])
    )
    pdf_combos["_win"] = pd.to_numeric(pdf_combos["win_rate_pct"], errors="coerce")
    pdf_combos["_sample"] = pd.to_numeric(pdf_combos["sample_size"], errors="coerce")
    pdf_combos = pdf_combos.sort_values(["_count", "_win", "_sample"], ascending=[False, False, False])
    lines.extend(["", "## PDF Add-Score Exact Combo Metrics", ""])
    lines.extend(
        md_table(
            pdf_combos,
            [
                "feature_id",
                "feature_label",
                "sample_size",
                "win_rate_pct",
                "neutral_rate_pct",
                "loss_rate_pct",
                "avg_return_pct",
                "median_return_pct",
                "candidate_status",
                "decision_hint",
            ],
            limit=80,
        )
    )
    overlap = summary[summary["row_type"].eq("overlap_condition")].copy()
    overlap["_win"] = pd.to_numeric(overlap["win_rate_pct"], errors="coerce")
    overlap["_sample"] = pd.to_numeric(overlap["sample_size"], errors="coerce")
    overlap = overlap.sort_values(["feature_family", "_win", "_sample"], ascending=[True, False, False])
    lines.extend(["", "## Add-Score Overlap Effects", ""])
    lines.extend(
        md_table(
            overlap,
            [
                "feature_family",
                "feature_id",
                "sample_size",
                "win_rate_pct",
                "loss_rate_pct",
                "avg_return_pct",
                "median_return_pct",
                "decision_hint",
            ],
            limit=60,
        )
    )
    gaps = summary[summary["row_type"].eq("feature_gap")].copy()
    gaps["_abs_gap"] = pd.to_numeric(gaps["success_minus_failure_share_pct"], errors="coerce").abs()
    gaps = gaps.sort_values("_abs_gap", ascending=False)
    lines.extend(["", "## Win/Loss Feature Gaps", ""])
    lines.extend(
        md_table(
            gaps,
            [
                "feature_id",
                "sample_size",
                "success_share_pct",
                "failure_share_pct",
                "success_minus_failure_share_pct",
                "win_rate_pct",
                "loss_rate_pct",
                "decision_hint",
            ],
            limit=30,
        )
    )
    slices = summary[summary["row_type"].eq("feature_slice")].copy()
    slices["_win"] = pd.to_numeric(slices["win_rate_pct"], errors="coerce")
    slices["_sample"] = pd.to_numeric(slices["sample_size"], errors="coerce")
    slices = slices.sort_values(["_win", "_sample"], ascending=[False, False])
    lines.extend(["", "## Best Feature Slices By Win Rate", ""])
    lines.extend(
        md_table(
            slices,
            [
                "feature_family",
                "feature_id",
                "sample_size",
                "win_rate_pct",
                "loss_rate_pct",
                "avg_return_pct",
                "median_return_pct",
                "decision_hint",
            ],
            limit=40,
        )
    )
    lines.extend(
        [
            "",
            "## Promotion Boundary",
            "",
            "This artifact is diagnostic only. Any hard gate, score, risk tag, model split, operation contract, or PDF presentation change still requires a separate promotion review and production PR.",
        ]
    )
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    generated_at = now_text()
    detail = source_scope()
    summary = build_summary(detail, generated_at)
    detail_out = detail_output(detail, generated_at)

    write_csv(summary, LATEST_CSV, SUMMARY_COLUMNS)
    write_csv(summary, DOCS_LATEST_CSV, SUMMARY_COLUMNS)
    write_csv(summary, HISTORY_CSV, SUMMARY_COLUMNS)
    write_csv(detail_out, LATEST_DETAIL_CSV, DETAIL_COLUMNS)
    write_csv(detail_out, HISTORY_DETAIL_CSV, DETAIL_COLUMNS)
    write_md(summary, LATEST_MD)
    write_md(summary, DOCS_LATEST_MD)


if __name__ == "__main__":
    main()
