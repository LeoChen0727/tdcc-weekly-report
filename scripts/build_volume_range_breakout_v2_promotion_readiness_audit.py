from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Any, Callable
from zoneinfo import ZoneInfo
import math

import pandas as pd

from build_volume_range_breakout_v2_research_contract import (
    ADVISORY_STATUS,
    CONFIRMATION_RULE_ID,
    ENTRY_RULE_ID,
    EMA23_STOP_RULE_ID,
    MODEL_SPECS,
    PARENT_MODEL_ID,
    PRICE_HISTORY_DIR,
    PRODUCTION_READINESS,
    false_text,
    normalize_date,
    normalize_stock_id,
    pct_round,
    read_csv,
    safe_str,
    to_float,
    write_csv,
)


ROOT = Path(".")
RESEARCH_LATEST_DIR = ROOT / "output" / "latest" / "research_backtest"
RESEARCH_HISTORY_DIR = ROOT / "output" / "history" / "research"

SOURCE_DETAIL_CSV = RESEARCH_LATEST_DIR / "volume_range_breakout_v2_research_contract_detail_latest.csv"

LATEST_SUMMARY_CSV = RESEARCH_LATEST_DIR / "volume_range_breakout_v2_promotion_readiness_audit_latest.csv"
LATEST_DETAIL_CSV = RESEARCH_LATEST_DIR / "volume_range_breakout_v2_promotion_readiness_audit_detail_latest.csv"
LATEST_MATRIX_CSV = RESEARCH_LATEST_DIR / "volume_range_breakout_v2_promotion_readiness_audit_matrix_latest.csv"
LATEST_MD = RESEARCH_LATEST_DIR / "volume_range_breakout_v2_promotion_readiness_audit_latest.md"

HISTORY_SUMMARY_CSV = RESEARCH_HISTORY_DIR / "volume_range_breakout_v2_promotion_readiness_audit.csv"
HISTORY_DETAIL_CSV = RESEARCH_HISTORY_DIR / "volume_range_breakout_v2_promotion_readiness_audit_detail.csv"
HISTORY_MATRIX_CSV = RESEARCH_HISTORY_DIR / "volume_range_breakout_v2_promotion_readiness_audit_matrix.csv"

RESEARCH_ID = "volume_range_breakout_v2_promotion_readiness_audit"
ARTIFACT_VERSION = "volume_range_breakout_v2_promotion_readiness_audit_20260709"
SOURCE_RESEARCH_ID = "volume_range_breakout_v2_research_contract"

HOLD_DAYS = [10, 15, 20, 30]
STOP_POLICIES = ["no_stop_reference", "ma20_ema23_close_stop_4d"]
PROMOTION_WIN_RATE_THRESHOLD = 60.0
PROMOTION_MIN_SAMPLE = 100

SUMMARY_COLUMNS = [
    "research_id",
    "artifact_version",
    "source_research_id",
    "source_artifact_version",
    "advisory_status",
    "row_type",
    "parent_model_id",
    "model_id",
    "model_zh",
    "holding_days",
    "stop_policy_id",
    "candidate_condition_id",
    "confirmation_rule_id",
    "entry_rule_id",
    "base_metric_scope",
    "sample_size",
    "invalid_return_count",
    "invalid_return_rate_pct",
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
    "trim_sample_size",
    "trim_avg_return_pct",
    "trim_median_return_pct",
    "top_1pct_return_threshold",
    "bottom_1pct_return_threshold",
    "tail_outlier_count",
    "stop_exit_count",
    "stop_exit_rate_pct",
    "metric_threshold_met",
    "promotion_blockers",
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
    "advisory_status",
    "parent_model_id",
    "model_id",
    "model_zh",
    "source_event_key",
    "stock_id",
    "stock_name",
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
    "stop_rule_id",
    "stop_price",
    "stop_confirmed_days",
    "candidate_condition_id",
    "confirmation_rule_id",
    "entry_rule_id",
    "split_group_id",
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
    "off_240d_low_pct",
    "range_width_240_pct",
    "position_in_240d_range_pct",
    "consolidation_type",
    "follow_through_type",
    "limit_up_like",
    "low_base_loose_flag",
    "consolidated_any_flag",
    "hist_return_20d_pct",
    "hist_return_60d_pct",
    "dist_ema23_pct",
    "close_gt_ema23",
    "close_gt_ma20",
    "ma20_gt_ma60",
    "ma60_gt_ma120",
    "tdcc_list_type",
    "tdcc_rank",
    "tdcc_weekly_increase_top20",
    "tdcc_any_top20",
    "return_valid",
    "invalid_reason",
    "approved_for_daily",
    "production_readiness",
    "generated_at",
]

MATRIX_COLUMNS = [
    "research_id",
    "artifact_version",
    "source_research_id",
    "source_artifact_version",
    "advisory_status",
    "row_type",
    "parent_model_id",
    "model_id",
    "model_zh",
    "holding_days",
    "stop_policy_id",
    "stratification_family",
    "stratification_id",
    "stratification_label",
    "condition_expression",
    "condition_role",
    "baseline_sample_size",
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
    "baseline_win_rate_pct",
    "baseline_loss_rate_pct",
    "baseline_avg_return_pct",
    "baseline_median_return_pct",
    "win_rate_delta_pct",
    "loss_rate_delta_pct",
    "avg_return_delta_pct",
    "median_return_delta_pct",
    "decision_hint",
    "approved_for_daily",
    "production_readiness",
    "generated_at",
]


@dataclass(frozen=True)
class StratificationSpec:
    family: str
    stratification_id: str
    label: str
    expression: str
    mask_builder: Callable[[pd.DataFrame], pd.Series]


def now_text() -> str:
    return datetime.now(ZoneInfo("Asia/Taipei")).strftime("%Y-%m-%d %H:%M:%S Asia/Taipei")


def bool_text(value: bool) -> str:
    return "True" if bool(value) else "False"


def trueish(series: pd.Series) -> pd.Series:
    return series.astype(str).str.lower().isin({"true", "1", "1.0", "yes", "y"})


def numeric(frame: pd.DataFrame, column: str) -> pd.Series:
    return pd.to_numeric(frame.get(column, pd.Series(index=frame.index, dtype=float)), errors="coerce")


def source_model_specs_by_id() -> dict[str, dict[str, str]]:
    return {safe_str(spec["model_id"]): spec for spec in MODEL_SPECS.values()}


def prepare_source() -> pd.DataFrame:
    source = read_csv(SOURCE_DETAIL_CSV)
    if source.empty:
        raise SystemExit("ERROR: research contract detail is empty")
    if set(source.get("research_id", pd.Series(dtype=str)).astype(str)) != {SOURCE_RESEARCH_ID}:
        raise SystemExit("ERROR: source detail must come from volume_range_breakout_v2_research_contract")
    if not set(source.get("approved_for_daily", pd.Series(dtype=str)).astype(str).str.lower()) <= {"false", "0", ""}:
        raise SystemExit("ERROR: source must remain research-only approved_for_daily=False")
    source = source[source["exit_policy_id"].astype(str).eq("fixed_d20_close_no_stop_reference")].copy()
    if source.empty:
        raise SystemExit("ERROR: no source rows for fixed_d20_close_no_stop_reference")
    if source["source_event_key"].duplicated().any():
        raise SystemExit("ERROR: source_event_key must be unique after source exit-policy filter")
    for col in [
        "breakout_over_prev60_pct",
        "volume_ratio",
        "signal_return_1d_pct",
        "range_width_20_pct",
        "range_width_60_pct",
        "off_60d_low_pct",
        "position_in_60d_range_pct",
        "hist_return_20d_pct",
        "hist_return_60d_pct",
        "dist_ema23_pct",
        "tdcc_rank",
    ]:
        source[col] = pd.to_numeric(source.get(col, ""), errors="coerce")
    return source


def price_for_stock(stock_id: str) -> pd.DataFrame:
    path = PRICE_HISTORY_DIR / f"{normalize_stock_id(stock_id)}.csv"
    if not path.exists():
        return pd.DataFrame()
    price = pd.read_csv(path, dtype=str, keep_default_na=False)
    if price.empty or "date" not in price.columns:
        return pd.DataFrame()
    out = price.copy()
    out["date"] = out["date"].map(normalize_date)
    for col in ["open", "high", "low", "close"]:
        out[col] = pd.to_numeric(out.get(col, ""), errors="coerce")
    out = out.dropna(subset=["date", "open", "high", "low", "close"]).sort_values("date").reset_index(drop=True)
    out["ma20"] = out["close"].rolling(20, min_periods=20).mean()
    out["ema23"] = out["close"].ewm(span=23, adjust=False, min_periods=23).mean()
    return out


def exact_index_for_date(price: pd.DataFrame, date: Any) -> int | None:
    matches = price.index[price["date"].astype(str).eq(normalize_date(date))].tolist()
    return int(matches[0]) if matches else None


def lower_ma_stop_price(price_row: pd.Series) -> float:
    refs = [to_float(price_row.get("ma20")), to_float(price_row.get("ema23"))]
    refs = [value for value in refs if not math.isnan(value) and value > 0]
    if not refs:
        return math.nan
    return min(refs) * 0.96


def trailing_position_features(price: pd.DataFrame, signal_idx: int, days: int) -> dict[str, Any]:
    start = max(0, signal_idx - days + 1)
    window = price.iloc[start : signal_idx + 1]
    if len(window) < min(days, 30):
        return {
            f"off_{days}d_low_pct": "",
            f"range_width_{days}_pct": "",
            f"position_in_{days}d_range_pct": "",
        }
    signal_close = to_float(price.iloc[signal_idx].get("close"))
    low = pd.to_numeric(window["low"], errors="coerce").min()
    high = pd.to_numeric(window["high"], errors="coerce").max()
    if math.isnan(signal_close) or math.isnan(low) or math.isnan(high) or low <= 0 or high <= low:
        return {
            f"off_{days}d_low_pct": "",
            f"range_width_{days}_pct": "",
            f"position_in_{days}d_range_pct": "",
        }
    return {
        f"off_{days}d_low_pct": pct_round((signal_close / low - 1.0) * 100.0),
        f"range_width_{days}_pct": pct_round((high / low - 1.0) * 100.0),
        f"position_in_{days}d_range_pct": pct_round((signal_close - low) / (high - low) * 100.0),
    }


def simulate_trade(row: pd.Series, hold_days: int, stop_policy_id: str, price_cache: dict[str, pd.DataFrame]) -> dict[str, Any]:
    stock_id = normalize_stock_id(row.get("stock_id"))
    price = price_cache.setdefault(stock_id, price_for_stock(stock_id))
    if price.empty:
        return {"return_valid": "False", "invalid_reason": "missing_price_history"}
    entry_idx = exact_index_for_date(price, row.get("entry_date"))
    signal_idx = exact_index_for_date(price, row.get("signal_date"))
    if entry_idx is None:
        return {"return_valid": "False", "invalid_reason": "missing_entry_date"}
    planned_exit_idx = entry_idx + hold_days - 1
    if planned_exit_idx >= len(price):
        return {"return_valid": "False", "invalid_reason": f"insufficient_{hold_days}d_forward_price"}
    entry_price = to_float(price.iloc[entry_idx].get("open"))
    if math.isnan(entry_price) or entry_price <= 0:
        return {"return_valid": "False", "invalid_reason": "missing_entry_open"}

    exit_idx = planned_exit_idx
    exit_price = to_float(price.iloc[planned_exit_idx].get("close"))
    exit_reason = f"fixed_{hold_days}d_close"
    stop_price = math.nan
    stop_days = 0
    if stop_policy_id == "ma20_ema23_close_stop_4d":
        for idx in range(entry_idx, planned_exit_idx):
            current = price.iloc[idx]
            close = to_float(current.get("close"))
            stop_price = lower_ma_stop_price(current)
            if not math.isnan(stop_price) and not math.isnan(close) and close <= stop_price:
                stop_days += 1
            else:
                stop_days = 0
            if stop_days >= 4:
                exit_idx = idx + 1
                exit_price = to_float(price.iloc[exit_idx].get("open"))
                exit_reason = EMA23_STOP_RULE_ID
                break

    if math.isnan(exit_price) or exit_price <= 0:
        return {"return_valid": "False", "invalid_reason": "missing_exit_price"}
    ret = (exit_price / entry_price - 1.0) * 100.0
    features: dict[str, Any] = {}
    if signal_idx is not None:
        features.update(trailing_position_features(price, signal_idx, 120))
        features.update(trailing_position_features(price, signal_idx, 240))
    return {
        "planned_exit_date": safe_str(price.iloc[planned_exit_idx].get("date")),
        "exit_date": safe_str(price.iloc[exit_idx].get("date")),
        "entry_price": pct_round(entry_price),
        "exit_price": pct_round(exit_price),
        "return_pct": pct_round(ret),
        "return_outcome": "win" if ret > 0 else "loss" if ret < 0 else "neutral",
        "exit_reason": exit_reason,
        "stop_price": pct_round(stop_price),
        "stop_confirmed_days": stop_days,
        "return_valid": "True",
        "invalid_reason": "",
        **features,
    }


def build_detail(source: pd.DataFrame, generated_at: str) -> pd.DataFrame:
    source_version = safe_str(source["artifact_version"].iloc[0])
    specs = source_model_specs_by_id()
    price_cache: dict[str, pd.DataFrame] = {}
    rows: list[dict[str, Any]] = []
    for _, row in source.iterrows():
        model_id = safe_str(row.get("model_id"))
        spec = specs.get(model_id, {})
        for hold_days in HOLD_DAYS:
            for stop_policy_id in STOP_POLICIES:
                simulated = simulate_trade(row, hold_days, stop_policy_id, price_cache)
                out = {
                    "research_id": RESEARCH_ID,
                    "artifact_version": ARTIFACT_VERSION,
                    "source_research_id": SOURCE_RESEARCH_ID,
                    "source_artifact_version": source_version,
                    "advisory_status": ADVISORY_STATUS,
                    "parent_model_id": PARENT_MODEL_ID,
                    "model_id": model_id,
                    "model_zh": safe_str(row.get("model_zh")),
                    "source_event_key": safe_str(row.get("source_event_key")),
                    "stock_id": normalize_stock_id(row.get("stock_id")),
                    "stock_name": safe_str(row.get("stock_name")),
                    "signal_date": normalize_date(row.get("signal_date")),
                    "confirmation_date": normalize_date(row.get("confirmation_date")),
                    "entry_date": normalize_date(row.get("entry_date")),
                    "holding_days": hold_days,
                    "stop_policy_id": stop_policy_id,
                    "stop_rule_id": EMA23_STOP_RULE_ID if stop_policy_id == "ma20_ema23_close_stop_4d" else "none_no_stop_reference",
                    "candidate_condition_id": safe_str(spec.get("candidate_condition_id")),
                    "confirmation_rule_id": CONFIRMATION_RULE_ID,
                    "entry_rule_id": ENTRY_RULE_ID,
                    "split_group_id": safe_str(row.get("split_group_id")),
                    "breakout_over_prev60_pct": pct_round(to_float(row.get("breakout_over_prev60_pct"))),
                    "volume_ratio": pct_round(to_float(row.get("volume_ratio"))),
                    "signal_return_1d_pct": pct_round(to_float(row.get("signal_return_1d_pct"))),
                    "range_width_20_pct": pct_round(to_float(row.get("range_width_20_pct"))),
                    "range_width_60_pct": pct_round(to_float(row.get("range_width_60_pct"))),
                    "off_60d_low_pct": pct_round(to_float(row.get("off_60d_low_pct"))),
                    "position_in_60d_range_pct": pct_round(to_float(row.get("position_in_60d_range_pct"))),
                    "consolidation_type": safe_str(row.get("consolidation_type")),
                    "follow_through_type": safe_str(row.get("follow_through_type")),
                    "limit_up_like": safe_str(row.get("limit_up_like")),
                    "low_base_loose_flag": safe_str(row.get("low_base_loose_flag")),
                    "consolidated_any_flag": safe_str(row.get("consolidated_any_flag")),
                    "hist_return_20d_pct": pct_round(to_float(row.get("hist_return_20d_pct"))),
                    "hist_return_60d_pct": pct_round(to_float(row.get("hist_return_60d_pct"))),
                    "dist_ema23_pct": pct_round(to_float(row.get("dist_ema23_pct"))),
                    "close_gt_ema23": safe_str(row.get("close_gt_ema23")),
                    "close_gt_ma20": safe_str(row.get("close_gt_ma20")),
                    "ma20_gt_ma60": safe_str(row.get("ma20_gt_ma60")),
                    "ma60_gt_ma120": safe_str(row.get("ma60_gt_ma120")),
                    "tdcc_list_type": safe_str(row.get("tdcc_list_type")),
                    "tdcc_rank": safe_str(row.get("tdcc_rank")),
                    "tdcc_weekly_increase_top20": safe_str(row.get("tdcc_weekly_increase_top20")),
                    "tdcc_any_top20": safe_str(row.get("tdcc_any_top20")),
                    "approved_for_daily": false_text(),
                    "production_readiness": PRODUCTION_READINESS,
                    "generated_at": generated_at,
                }
                out.update(simulated)
                rows.append(out)
    return pd.DataFrame(rows)


def valid_returns(part: pd.DataFrame) -> pd.DataFrame:
    return part[part["return_valid"].astype(str).eq("True")].copy()


def metrics(part: pd.DataFrame) -> dict[str, Any]:
    valid = valid_returns(part)
    returns = pd.to_numeric(valid.get("return_pct", pd.Series(dtype=float)), errors="coerce").dropna()
    n = int(len(returns))
    if n == 0:
        return {
            "sample_size": 0,
            "win_count": 0,
            "neutral_count": 0,
            "loss_count": 0,
            "win_rate_pct": "",
            "neutral_rate_pct": "",
            "loss_rate_pct": "",
            "avg_return_pct": "",
            "median_return_pct": "",
            "p10_return_pct": "",
            "p90_return_pct": "",
        }
    outcomes = valid["return_outcome"].astype(str)
    win = int(outcomes.eq("win").sum())
    neutral = int(outcomes.eq("neutral").sum())
    loss = int(outcomes.eq("loss").sum())
    return {
        "sample_size": n,
        "win_count": win,
        "neutral_count": neutral,
        "loss_count": loss,
        "win_rate_pct": pct_round(win / n * 100.0, 2),
        "neutral_rate_pct": pct_round(neutral / n * 100.0, 2),
        "loss_rate_pct": pct_round(loss / n * 100.0, 2),
        "avg_return_pct": pct_round(float(returns.mean())),
        "median_return_pct": pct_round(float(returns.median())),
        "p10_return_pct": pct_round(float(returns.quantile(0.10))),
        "p90_return_pct": pct_round(float(returns.quantile(0.90))),
    }


def trim_metrics(part: pd.DataFrame) -> dict[str, Any]:
    returns = pd.to_numeric(valid_returns(part).get("return_pct", pd.Series(dtype=float)), errors="coerce").dropna()
    if returns.empty:
        return {
            "trim_sample_size": 0,
            "trim_avg_return_pct": "",
            "trim_median_return_pct": "",
            "top_1pct_return_threshold": "",
            "bottom_1pct_return_threshold": "",
            "tail_outlier_count": 0,
        }
    low = float(returns.quantile(0.01))
    high = float(returns.quantile(0.99))
    trimmed = returns[(returns >= low) & (returns <= high)]
    return {
        "trim_sample_size": int(len(trimmed)),
        "trim_avg_return_pct": pct_round(float(trimmed.mean())) if not trimmed.empty else "",
        "trim_median_return_pct": pct_round(float(trimmed.median())) if not trimmed.empty else "",
        "top_1pct_return_threshold": pct_round(high),
        "bottom_1pct_return_threshold": pct_round(low),
        "tail_outlier_count": int(len(returns) - len(trimmed)),
    }


def summary_base(part: pd.DataFrame, row_type: str, generated_at: str) -> dict[str, Any]:
    source_version = safe_str(part["source_artifact_version"].iloc[0]) if not part.empty else ""
    invalid = int(part["return_valid"].astype(str).ne("True").sum()) if not part.empty else 0
    valid_count = int(part["return_valid"].astype(str).eq("True").sum()) if not part.empty else 0
    stop_count = int(part["exit_reason"].astype(str).eq(EMA23_STOP_RULE_ID).sum()) if not part.empty else 0
    row = {
        "research_id": RESEARCH_ID,
        "artifact_version": ARTIFACT_VERSION,
        "source_research_id": SOURCE_RESEARCH_ID,
        "source_artifact_version": source_version,
        "advisory_status": ADVISORY_STATUS,
        "row_type": row_type,
        "parent_model_id": PARENT_MODEL_ID,
        "model_id": safe_str(part["model_id"].iloc[0]) if not part.empty else "",
        "model_zh": safe_str(part["model_zh"].iloc[0]) if not part.empty else "",
        "holding_days": safe_str(part["holding_days"].iloc[0]) if not part.empty else "",
        "stop_policy_id": safe_str(part["stop_policy_id"].iloc[0]) if not part.empty else "",
        "candidate_condition_id": safe_str(part["candidate_condition_id"].iloc[0]) if not part.empty else "",
        "confirmation_rule_id": CONFIRMATION_RULE_ID,
        "entry_rule_id": ENTRY_RULE_ID,
        "base_metric_scope": "confirmed_same_stock_non_overlap_only",
        "invalid_return_count": invalid,
        "invalid_return_rate_pct": pct_round(invalid / (invalid + valid_count) * 100.0, 2) if invalid + valid_count else "",
        "stop_exit_count": stop_count,
        "stop_exit_rate_pct": pct_round(stop_count / valid_count * 100.0, 2) if valid_count else "",
        "approved_for_daily": false_text(),
        "production_readiness": PRODUCTION_READINESS,
        "generated_at": generated_at,
    }
    row.update(metrics(part))
    row.update(trim_metrics(part))
    return row


def readiness_for(row: dict[str, Any]) -> tuple[str, str, str]:
    blockers = ["research_only_not_production_contract", "no_registry_change", "no_operation_adapter"]
    try:
        sample = int(float(row.get("sample_size") or 0))
        win_rate = float(row.get("win_rate_pct") or 0.0)
        avg_return = float(row.get("avg_return_pct") or 0.0)
        median_return = float(row.get("median_return_pct") or 0.0)
        invalid = int(float(row.get("invalid_return_count") or 0))
    except (TypeError, ValueError):
        return "False", "metric_parse_failed", "blocked_metric_parse_failed"
    if sample < PROMOTION_MIN_SAMPLE:
        blockers.append("sample_below_100")
    if win_rate < PROMOTION_WIN_RATE_THRESHOLD:
        blockers.append("win_rate_below_60")
    if avg_return <= 0:
        blockers.append("avg_return_not_positive")
    if median_return <= 0:
        blockers.append("median_return_not_positive")
    if invalid > 0:
        blockers.append("invalid_return_rows_need_review")
    metric_met = (
        sample >= PROMOTION_MIN_SAMPLE
        and win_rate >= PROMOTION_WIN_RATE_THRESHOLD
        and avg_return > 0
        and median_return > 0
    )
    if metric_met:
        hint = "metric_threshold_met_research_only_needs_promotion_pr"
    else:
        hint = "not_ready_for_promotion_metric_gap"
    return bool_text(metric_met), ";".join(blockers), hint


def build_summary(detail: pd.DataFrame, generated_at: str) -> pd.DataFrame:
    rows: list[dict[str, Any]] = []
    for _, part in detail.groupby(["model_id", "holding_days", "stop_policy_id"], dropna=False):
        base = summary_base(part, "base_performance", generated_at)
        metric_met, blockers, hint = readiness_for(base)
        base["metric_threshold_met"] = metric_met
        base["promotion_blockers"] = blockers
        base["decision_hint"] = hint
        rows.append(base)
        trim = dict(base)
        trim["row_type"] = "trimmed_anomaly_sensitivity"
        trim["decision_hint"] = "tail_trim_for_anomaly_review_not_promotion_basis"
        rows.append(trim)
        invalid = dict(base)
        invalid["row_type"] = "invalid_return_summary"
        invalid["decision_hint"] = "invalid_rows_must_be_explained_before_promotion"
        rows.append(invalid)
    return pd.DataFrame(rows)


def stratification_specs() -> list[StratificationSpec]:
    return [
        StratificationSpec("tdcc", "tdcc_weekly_increase_top20", "TDCC weekly_increase rank <=20", "tdcc_list_type == weekly_increase AND tdcc_rank <= 20", lambda d: trueish(d["tdcc_weekly_increase_top20"])),
        StratificationSpec("tdcc", "tdcc_any_top20", "TDCC any list rank <=20", "tdcc_rank <= 20", lambda d: trueish(d["tdcc_any_top20"])),
        StratificationSpec("technical_23ema", "tech_dist_ema23_0_to_15", "0% <= distance to EMA23 <= 15%", "0 <= dist_ema23_pct <= 15", lambda d: numeric(d, "dist_ema23_pct").between(0, 15, inclusive="both")),
        StratificationSpec("technical_23ema", "tech_ret20_0_to_25", "20d return 0% to 25%", "0 <= hist_return_20d_pct <= 25", lambda d: numeric(d, "hist_return_20d_pct").between(0, 25, inclusive="both")),
        StratificationSpec("technical_ma", "tech_ma60_gt_ma120", "MA60 > MA120", "ma60_gt_ma120 == True", lambda d: trueish(d["ma60_gt_ma120"])),
        StratificationSpec("signal_quality", "volume_ratio_2_to_6", "volume ratio 2..6", "2 <= volume_ratio <= 6", lambda d: numeric(d, "volume_ratio").between(2, 6, inclusive="both")),
        StratificationSpec("signal_quality", "not_limit_up_like", "not limit-up-like signal", "limit_up_like != True", lambda d: ~trueish(d["limit_up_like"])),
        StratificationSpec("low_base_redefinition", "off120_le40_range120_le60", "off 120d low <=40 and 120d range <=60", "off_120d_low_pct <= 40 AND range_width_120_pct <= 60", lambda d: numeric(d, "off_120d_low_pct").le(40) & numeric(d, "range_width_120_pct").le(60)),
        StratificationSpec("low_base_redefinition", "off120_le30_range120_le45", "off 120d low <=30 and 120d range <=45", "off_120d_low_pct <= 30 AND range_width_120_pct <= 45", lambda d: numeric(d, "off_120d_low_pct").le(30) & numeric(d, "range_width_120_pct").le(45)),
        StratificationSpec("low_base_redefinition", "off240_le50_range240_le80", "off 240d low <=50 and 240d range <=80", "off_240d_low_pct <= 50 AND range_width_240_pct <= 80", lambda d: numeric(d, "off_240d_low_pct").le(50) & numeric(d, "range_width_240_pct").le(80)),
        StratificationSpec("low_base_redefinition", "off240_le40_range240_le60", "off 240d low <=40 and 240d range <=60", "off_240d_low_pct <= 40 AND range_width_240_pct <= 60", lambda d: numeric(d, "off_240d_low_pct").le(40) & numeric(d, "range_width_240_pct").le(60)),
        StratificationSpec("low_base_redefinition", "off120_le40_range120_le60_ma60_gt_ma120", "120d low/base plus MA60 > MA120", "off_120d_low_pct <= 40 AND range_width_120_pct <= 60 AND ma60_gt_ma120", lambda d: numeric(d, "off_120d_low_pct").le(40) & numeric(d, "range_width_120_pct").le(60) & trueish(d["ma60_gt_ma120"])),
    ]


def add_delta(row: dict[str, Any], baseline: dict[str, Any]) -> None:
    for source, target in [
        ("win_rate_pct", "win_rate_delta_pct"),
        ("loss_rate_pct", "loss_rate_delta_pct"),
        ("avg_return_pct", "avg_return_delta_pct"),
        ("median_return_pct", "median_return_delta_pct"),
    ]:
        try:
            row[target] = pct_round(float(row.get(source) or 0.0) - float(baseline.get(source) or 0.0))
        except (TypeError, ValueError):
            row[target] = ""
    row["baseline_win_rate_pct"] = baseline.get("win_rate_pct", "")
    row["baseline_loss_rate_pct"] = baseline.get("loss_rate_pct", "")
    row["baseline_avg_return_pct"] = baseline.get("avg_return_pct", "")
    row["baseline_median_return_pct"] = baseline.get("median_return_pct", "")


def matrix_hint(row: dict[str, Any]) -> str:
    sample = int(row.get("sample_size") or 0)
    if sample < 30:
        return "thin_sample_do_not_use_as_gate"
    try:
        win_delta = float(row.get("win_rate_delta_pct") or 0.0)
        avg_delta = float(row.get("avg_return_delta_pct") or 0.0)
        median_delta = float(row.get("median_return_delta_pct") or 0.0)
    except (TypeError, ValueError):
        return "research_only_review_required"
    if win_delta >= 5.0 and avg_delta >= 1.0 and median_delta >= 0:
        return "positive_stratification_candidate_not_gate"
    if win_delta <= -5.0 or avg_delta <= -1.0:
        return "risk_stratification_candidate_not_gate"
    return "mixed_or_weak_stratification_not_gate"


def build_matrix(detail: pd.DataFrame, summary: pd.DataFrame, generated_at: str) -> pd.DataFrame:
    base_rows = summary[summary["row_type"].astype(str).eq("base_performance")].copy()
    base_lookup = {
        (row["model_id"], str(row["holding_days"]), row["stop_policy_id"]): row.to_dict()
        for _, row in base_rows.iterrows()
    }
    rows: list[dict[str, Any]] = []
    for (model_id, hold_days, stop_policy), part in detail.groupby(["model_id", "holding_days", "stop_policy_id"], dropna=False):
        baseline = base_lookup[(model_id, str(hold_days), stop_policy)]
        baseline_n = int(float(baseline.get("sample_size") or 0))
        for spec in stratification_specs():
            mask = spec.mask_builder(part).fillna(False)
            selected = part[mask].copy()
            row = {
                "research_id": RESEARCH_ID,
                "artifact_version": ARTIFACT_VERSION,
                "source_research_id": SOURCE_RESEARCH_ID,
                "source_artifact_version": safe_str(part["source_artifact_version"].iloc[0]),
                "advisory_status": ADVISORY_STATUS,
                "row_type": "stratification",
                "parent_model_id": PARENT_MODEL_ID,
                "model_id": safe_str(model_id),
                "model_zh": safe_str(part["model_zh"].iloc[0]),
                "holding_days": safe_str(hold_days),
                "stop_policy_id": safe_str(stop_policy),
                "stratification_family": spec.family,
                "stratification_id": spec.stratification_id,
                "stratification_label": spec.label,
                "condition_expression": spec.expression,
                "condition_role": "stratification_only_not_candidate_or_confirmation_gate",
                "baseline_sample_size": baseline_n,
                "coverage_pct": "",
                "approved_for_daily": false_text(),
                "production_readiness": PRODUCTION_READINESS,
                "generated_at": generated_at,
            }
            row.update(metrics(selected))
            row["coverage_pct"] = pct_round(int(row["sample_size"]) / baseline_n * 100.0, 2) if baseline_n else ""
            add_delta(row, baseline)
            row["decision_hint"] = matrix_hint(row)
            rows.append(row)
    return pd.DataFrame(rows)


def md_table(frame: pd.DataFrame, columns: list[str], limit: int = 20) -> list[str]:
    if frame.empty:
        return ["_No rows._"]
    view = frame[columns].head(limit).astype(str).replace({"nan": "", "NaN": "", "<NA>": ""})
    lines = ["| " + " | ".join(columns) + " |", "| " + " | ".join(["---"] * len(columns)) + " |"]
    for _, row in view.iterrows():
        lines.append("| " + " | ".join(str(row[col]) for col in columns) + " |")
    return lines


def write_markdown(summary: pd.DataFrame, matrix: pd.DataFrame) -> None:
    base = summary[summary["row_type"].eq("base_performance")].copy()
    base["_hold"] = pd.to_numeric(base["holding_days"], errors="coerce")
    base = base.sort_values(["model_id", "stop_policy_id", "_hold"])
    ready = base[base["metric_threshold_met"].astype(str).eq("True")].copy()
    lowbase = matrix[matrix["stratification_family"].eq("low_base_redefinition")].copy()
    lowbase["_sample"] = pd.to_numeric(lowbase["sample_size"], errors="coerce")
    lowbase = lowbase.sort_values(["model_id", "holding_days", "stop_policy_id", "_sample"], ascending=[True, True, True, False])
    lines = [
        "# Volume Range Breakout V2 Promotion Readiness Audit",
        "",
        f"- research_id: `{RESEARCH_ID}`",
        f"- artifact_version: `{ARTIFACT_VERSION}`",
        f"- source_research_id: `{SOURCE_RESEARCH_ID}`",
        "- status: research-only; no production registry, ranking, adapter, packet, or PDF change.",
        "- base metrics use confirmed same-stock non-overlap samples only.",
        "- D+10/D+15/D+20/D+30 are compared with no-stop and close-confirmed MA20/EMA23 stop.",
        "- TDCC, 23EMA, and low-base redefinition rows are stratification-only, not hidden gates.",
        "",
        "## Base Performance",
        "",
        *md_table(
            base,
            [
                "model_id",
                "holding_days",
                "stop_policy_id",
                "sample_size",
                "win_rate_pct",
                "loss_rate_pct",
                "avg_return_pct",
                "median_return_pct",
                "invalid_return_count",
                "metric_threshold_met",
            ],
            limit=40,
        ),
        "",
        "## Metric Threshold Rows",
        "",
        *md_table(
            ready,
            [
                "model_id",
                "holding_days",
                "stop_policy_id",
                "sample_size",
                "win_rate_pct",
                "avg_return_pct",
                "median_return_pct",
                "promotion_blockers",
            ],
            limit=20,
        ),
        "",
        "## Low-Base Redefinition Matrix",
        "",
        *md_table(
            lowbase,
            [
                "model_id",
                "holding_days",
                "stop_policy_id",
                "stratification_id",
                "sample_size",
                "win_rate_pct",
                "avg_return_pct",
                "median_return_pct",
                "decision_hint",
            ],
            limit=40,
        ),
        "",
        "## Outputs",
        "",
        f"- summary_csv: `{LATEST_SUMMARY_CSV.as_posix()}`",
        f"- detail_csv: `{LATEST_DETAIL_CSV.as_posix()}`",
        f"- matrix_csv: `{LATEST_MATRIX_CSV.as_posix()}`",
    ]
    LATEST_MD.parent.mkdir(parents=True, exist_ok=True)
    LATEST_MD.write_text("\n".join(lines) + "\n", encoding="utf-8", newline="\n")


def main() -> int:
    generated_at = now_text()
    source = prepare_source()
    detail = build_detail(source, generated_at)
    summary = build_summary(detail, generated_at)
    matrix = build_matrix(detail, summary, generated_at)
    write_csv(detail, LATEST_DETAIL_CSV, DETAIL_COLUMNS)
    write_csv(detail, HISTORY_DETAIL_CSV, DETAIL_COLUMNS)
    write_csv(summary, LATEST_SUMMARY_CSV, SUMMARY_COLUMNS)
    write_csv(summary, HISTORY_SUMMARY_CSV, SUMMARY_COLUMNS)
    write_csv(matrix, LATEST_MATRIX_CSV, MATRIX_COLUMNS)
    write_csv(matrix, HISTORY_MATRIX_CSV, MATRIX_COLUMNS)
    write_markdown(summary, matrix)
    print(f"Saved: {LATEST_SUMMARY_CSV} rows={len(summary)}")
    print(f"Saved: {LATEST_DETAIL_CSV} rows={len(detail)}")
    print(f"Saved: {LATEST_MATRIX_CSV} rows={len(matrix)}")
    print(f"Saved: {LATEST_MD}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
