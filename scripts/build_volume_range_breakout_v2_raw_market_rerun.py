from __future__ import annotations

from concurrent.futures import ThreadPoolExecutor
from datetime import datetime
from pathlib import Path
from typing import Any
from zoneinfo import ZoneInfo
import math
import os
import sys

import pandas as pd


sys.path.insert(0, str(Path(__file__).resolve().parent))

from build_volume_breakout_confirmed_operation_backtest import (  # noqa: E402
    ENTRY_RULE_ID,
    EXIT_RULE_ID,
    LIFECYCLE_DEFINITION_ID,
    MAX_HOLD_DAYS,
    MODEL_ID,
    STOP_RULE_ID,
    TRIGGER_MAP,
    event_payload,
    find_confirmation,
    formal_model_hit_mask,
    is_equity_stock_id,
    load_market_regime_map,
    load_price_csv,
    selected_confirmation_for_signal,
    simulate_confirmed_trade,
)
from build_volume_breakout_watch import PRICE_HISTORY_DIR  # noqa: E402
from tracking_utils import normalize_code, normalize_date, safe_str  # noqa: E402


ROOT = Path(".")
RESEARCH_LATEST_DIR = ROOT / "output" / "latest" / "research_backtest"
RESEARCH_HISTORY_DIR = ROOT / "output" / "history" / "research"

SOURCE_TIMING_DETAIL_CSV = (
    RESEARCH_LATEST_DIR / "volume_range_breakout_v2_next_day_continuation_timing_audit_detail_latest.csv"
)
LATEST_SUMMARY_CSV = RESEARCH_LATEST_DIR / "volume_range_breakout_v2_raw_market_rerun_latest.csv"
LATEST_DETAIL_CSV = RESEARCH_LATEST_DIR / "volume_range_breakout_v2_raw_market_rerun_detail_latest.csv"
LATEST_MD = RESEARCH_LATEST_DIR / "volume_range_breakout_v2_raw_market_rerun_latest.md"
HISTORY_SUMMARY_CSV = RESEARCH_HISTORY_DIR / "volume_range_breakout_v2_raw_market_rerun.csv"
HISTORY_DETAIL_CSV = RESEARCH_HISTORY_DIR / "volume_range_breakout_v2_raw_market_rerun_detail.csv"

RESEARCH_ID = "volume_range_breakout_v2_raw_market_rerun"
ARTIFACT_VERSION = "volume_range_breakout_v2_raw_market_rerun_20260708"
SOURCE_RESEARCH_ID = "volume_range_breakout_v2_next_day_continuation_timing_audit"
ADVISORY_STATUS = "warning_research_variant_only"
PRODUCTION_READINESS = "not_production_ready_research_only"
NEXT_DAY_TRIGGER_ID = "next_day_continuation_confirmed"
OUT_OF_SAMPLE_FRACTION = 0.7

DETAIL_COLUMNS = [
    "research_id",
    "artifact_version",
    "source_research_id",
    "advisory_status",
    "model_id",
    "source_event_key",
    "stock_id",
    "stock_name",
    "market",
    "market_regime",
    "signal_date",
    "confirmation_date",
    "entry_date",
    "exit_date",
    "entry_price",
    "exit_price",
    "return_pct",
    "return_bucket",
    "out_of_sample",
    "trigger_id_required",
    "selected_trigger_id_current_v1",
    "matched_trigger_ids_current_v1",
    "selected_confirmation_date_current_v1",
    "confirmation_age_trading_days",
    "entry_rule_id",
    "stop_loss_rule_id",
    "stop_loss_level",
    "exit_rule_id",
    "exit_reason",
    "holding_days",
    "mfe_pct",
    "mae_pct",
    "base_v1_signal",
    "high_breakout_60d_met",
    "next_day_continuation_confirmed",
    "known_before_entry_open",
    "uses_post_entry_information",
    "present_in_timing_audit_60d",
    "previous_20d_high",
    "previous_60d_high",
    "breakout_over_prev60_pct",
    "volume_ratio",
    "signal_return_1d_pct",
    "signal_open",
    "signal_high",
    "signal_low",
    "signal_close",
    "confirmation_open",
    "confirmation_high",
    "confirmation_low",
    "confirmation_close",
    "classification_id",
    "attack_method",
    "price_position_type",
    "consolidation_type",
    "risk_type",
    "candle_quality",
    "follow_through_type",
    "limit_up_like",
    "anomaly_flag",
    "approved_for_daily",
    "production_readiness",
    "generated_at",
]

SUMMARY_COLUMNS = [
    "research_id",
    "artifact_version",
    "source_research_id",
    "advisory_status",
    "model_id",
    "row_type",
    "audit_scope",
    "audit_key",
    "sample_size",
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
    "min_return_pct",
    "max_return_pct",
    "trim_sample_size",
    "trim_avg_return_pct",
    "trim_median_return_pct",
    "anomaly_count",
    "scanned_price_files",
    "equity_price_files",
    "base_v1_signal_count",
    "base_v1_mature_trade_count",
    "next_day_trigger_mature_count",
    "trigger_only_excluded_by_follow_through_count",
    "v2_raw_candidate_count",
    "v2_raw_mature_event_count",
    "timing_audit_60d_event_count",
    "raw_minus_timing_count",
    "timing_minus_raw_count",
    "timing_audit_max_signal_date",
    "raw_extension_after_timing_count",
    "raw_minus_timing_within_timing_window_count",
    "future_leak_count",
    "value_a",
    "value_b",
    "value_c",
    "status",
    "note",
    "approved_for_daily",
    "production_readiness",
    "generated_at",
]


def now_text() -> str:
    return datetime.now(ZoneInfo("Asia/Taipei")).strftime("%Y-%m-%d %H:%M:%S Asia/Taipei")


def false_text() -> str:
    return "False"


def true_text() -> str:
    return "True"


def pct_round(value: Any, digits: int = 4) -> float | str:
    try:
        number = float(value)
    except (TypeError, ValueError):
        return ""
    if math.isnan(number) or math.isinf(number):
        return ""
    return round(number, digits)


def safe_float(value: Any) -> float:
    text = safe_str(value).replace(",", "").replace("%", "")
    if not text:
        return math.nan
    try:
        return float(text)
    except Exception:
        return math.nan


def numeric_series(df: pd.DataFrame, col: str) -> pd.Series:
    if col not in df.columns:
        return pd.Series([math.nan] * len(df), index=df.index, dtype="float64")
    return pd.to_numeric(df[col], errors="coerce")


def read_csv(path: Path) -> pd.DataFrame:
    if not path.exists():
        raise SystemExit(f"ERROR: missing required file: {path}")
    return pd.read_csv(path, dtype=str, keep_default_na=False)


def write_csv(df: pd.DataFrame, path: Path, columns: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    out = df.copy()
    for col in columns:
        if col not in out.columns:
            out[col] = ""
    out = out[columns]
    out.to_csv(path, index=False, encoding="utf-8-sig")


def return_bucket(value: Any) -> str:
    ret = safe_float(value)
    if math.isnan(ret):
        return ""
    if ret > 0:
        return "win"
    if ret < 0:
        return "loss"
    return "neutral"


def event_key(row: dict[str, Any]) -> str:
    parts = [
        row.get("stock_id", ""),
        row.get("signal_date", ""),
        row.get("confirmation_date", ""),
        row.get("selected_trigger_id_current_v1", ""),
        row.get("entry_date", ""),
        row.get("exit_date", ""),
        safe_str(row.get("entry_price", "")),
        safe_str(row.get("exit_price", "")),
    ]
    return "|".join(safe_str(part) for part in parts)


def out_of_sample_start_date(df: pd.DataFrame) -> str:
    dates = sorted({normalize_date(value) for value in df.get("confirmation_date", []) if normalize_date(value)})
    if len(dates) < 5:
        return ""
    return dates[int(len(dates) * OUT_OF_SAMPLE_FRACTION)]


def timing_audit_60d_keys() -> set[str]:
    timing = read_csv(SOURCE_TIMING_DETAIL_CSV)
    part = timing[
        timing.get("high_breakout_60d_met", pd.Series(dtype=str)).astype(str).eq("True")
        & timing.get("known_before_entry_open", pd.Series(dtype=str)).astype(str).eq("True")
    ].copy()
    if part.empty:
        raise SystemExit("ERROR: timing audit 60d next-day continuation subset is empty")
    return set(part["source_event_key"].astype(str))


def high60_mask(price: pd.DataFrame) -> pd.Series:
    close = numeric_series(price, "close")
    prev60 = numeric_series(price, "previous_60d_high_calc")
    return (close >= prev60 * 1.02).fillna(False)


def process_price_path(path: Path, market_regimes: dict[str, str]) -> tuple[list[dict[str, Any]], dict[str, int]]:
    counters = {
        "scanned_price_files": 1,
        "equity_price_files": 0,
        "base_v1_signal_count": 0,
        "base_v1_mature_trade_count": 0,
        "next_day_trigger_mature_count": 0,
        "trigger_only_excluded_by_follow_through_count": 0,
        "v2_raw_candidate_count": 0,
        "v2_raw_mature_event_count": 0,
    }
    rows: list[dict[str, Any]] = []
    raw = load_price_csv(path)
    if raw.empty or len(raw) < 90:
        return rows, counters
    if not {"date", "stock_id", "stock_name", "open", "high", "low", "close", "volume"}.issubset(raw.columns):
        return rows, counters
    first_id = normalize_code(raw.iloc[0].get("stock_id"))
    if not is_equity_stock_id(first_id):
        return rows, counters
    counters["equity_price_files"] = 1
    price = add_research_features_for_v2(raw)
    if price.empty:
        return rows, counters
    base_mask = formal_model_hit_mask(price)
    v2_high60 = high60_mask(price)
    next_day_spec = TRIGGER_MAP[NEXT_DAY_TRIGGER_ID]
    for signal_idx in [int(idx) for idx in base_mask[base_mask].index]:
        counters["base_v1_signal_count"] += 1
        selected = selected_confirmation_for_signal(price, signal_idx)
        if selected is not None:
            selected_trade = simulate_confirmed_trade(price, signal_idx, int(selected["confirmation_idx"]))
            if selected_trade is not None:
                counters["base_v1_mature_trade_count"] += 1
        if not bool(v2_high60.loc[signal_idx]):
            continue
        confirmation = find_confirmation(price, signal_idx, next_day_spec)
        if confirmation is None:
            continue
        confirmation_idx = int(confirmation["confirmation_idx"])
        trade = simulate_confirmed_trade(price, signal_idx, confirmation_idx)
        if trade is None:
            continue
        counters["next_day_trigger_mature_count"] += 1
        selected = selected_confirmation_for_signal(price, signal_idx)
        selected_trigger = safe_str(selected.get("trigger_id")) if selected else ""
        selected_confirmation_date = safe_str(selected.get("confirmation_date")) if selected else ""
        matched_trigger_ids = safe_str(selected.get("matched_trigger_ids")) if selected else ""
        payload = event_payload(price, signal_idx, confirmation_idx, market_regimes)
        if safe_str(payload.get("follow_through_type")) != "next_day_continuation":
            counters["trigger_only_excluded_by_follow_through_count"] += 1
            continue
        counters["v2_raw_candidate_count"] += 1
        counters["v2_raw_mature_event_count"] += 1
        signal = price.iloc[signal_idx]
        confirmation_row = price.iloc[confirmation_idx]
        previous_60d_high = safe_float(signal.get("previous_60d_high_calc"))
        signal_close = safe_float(signal.get("close"))
        breakout_over_prev60 = (
            (signal_close / previous_60d_high - 1.0) * 100.0
            if previous_60d_high and not math.isnan(previous_60d_high)
            else math.nan
        )
        row = {
            "research_id": RESEARCH_ID,
            "artifact_version": ARTIFACT_VERSION,
            "source_research_id": SOURCE_RESEARCH_ID,
            "advisory_status": ADVISORY_STATUS,
            "model_id": MODEL_ID,
            "stock_id": normalize_code(payload.get("stock_id")),
            "stock_name": safe_str(payload.get("stock_name")),
            "market": safe_str(payload.get("market")),
            "market_regime": safe_str(payload.get("market_regime")),
            "signal_date": normalize_date(payload.get("signal_date")),
            "confirmation_date": normalize_date(payload.get("confirmation_date")),
            "entry_date": normalize_date(trade.get("entry_date")),
            "exit_date": normalize_date(trade.get("exit_date")),
            "entry_price": pct_round(trade.get("entry_price")),
            "exit_price": pct_round(trade.get("exit_price")),
            "return_pct": pct_round(trade.get("return_pct")),
            "return_bucket": return_bucket(trade.get("return_pct")),
            "out_of_sample": false_text(),
            "trigger_id_required": NEXT_DAY_TRIGGER_ID,
            "selected_trigger_id_current_v1": selected_trigger,
            "matched_trigger_ids_current_v1": matched_trigger_ids,
            "selected_confirmation_date_current_v1": selected_confirmation_date,
            "confirmation_age_trading_days": confirmation_idx - signal_idx,
            "entry_rule_id": ENTRY_RULE_ID,
            "stop_loss_rule_id": STOP_RULE_ID,
            "stop_loss_level": pct_round(trade.get("stop_loss_level")),
            "exit_rule_id": EXIT_RULE_ID,
            "exit_reason": safe_str(trade.get("exit_reason")),
            "holding_days": safe_str(trade.get("holding_days")),
            "mfe_pct": pct_round(trade.get("mfe_pct")),
            "mae_pct": pct_round(trade.get("mae_pct")),
            "base_v1_signal": true_text(),
            "high_breakout_60d_met": true_text(),
            "next_day_continuation_confirmed": true_text(),
            "known_before_entry_open": true_text(),
            "uses_post_entry_information": false_text(),
            "present_in_timing_audit_60d": false_text(),
            "previous_20d_high": pct_round(signal.get("previous_20d_high_calc")),
            "previous_60d_high": pct_round(previous_60d_high),
            "breakout_over_prev60_pct": pct_round(breakout_over_prev60),
            "volume_ratio": pct_round(signal.get("volume_ratio")),
            "signal_return_1d_pct": pct_round(signal.get("signal_return_1d_pct")),
            "signal_open": pct_round(signal.get("open")),
            "signal_high": pct_round(signal.get("high")),
            "signal_low": pct_round(signal.get("low")),
            "signal_close": pct_round(signal.get("close")),
            "confirmation_open": pct_round(confirmation_row.get("open")),
            "confirmation_high": pct_round(confirmation_row.get("high")),
            "confirmation_low": pct_round(confirmation_row.get("low")),
            "confirmation_close": pct_round(confirmation_row.get("close")),
            "classification_id": safe_str(payload.get("classification_id")),
            "attack_method": safe_str(payload.get("attack_method")),
            "price_position_type": safe_str(payload.get("price_position_type")),
            "consolidation_type": safe_str(payload.get("consolidation_type")),
            "risk_type": safe_str(payload.get("risk_type")),
            "candle_quality": safe_str(payload.get("candle_quality")),
            "follow_through_type": safe_str(payload.get("follow_through_type")),
            "limit_up_like": safe_str(payload.get("limit_up_like")),
            "anomaly_flag": "none",
            "approved_for_daily": false_text(),
            "production_readiness": PRODUCTION_READINESS,
        }
        row["source_event_key"] = event_key(row)
        rows.append(row)
    return rows, counters


def add_research_features_for_v2(raw: pd.DataFrame) -> pd.DataFrame:
    # Reuse the official v1 research feature builder through the existing producer import path.
    from build_historical_pattern_operation_registry import add_research_features

    return add_research_features(raw)


def build_raw_events(generated_at: str) -> tuple[pd.DataFrame, dict[str, int]]:
    market_regimes = load_market_regime_map()
    paths = sorted(PRICE_HISTORY_DIR.glob("*.csv"))
    worker_count = min(12, max(2, os.cpu_count() or 4))
    all_rows: list[dict[str, Any]] = []
    total = {
        "scanned_price_files": 0,
        "equity_price_files": 0,
        "base_v1_signal_count": 0,
        "base_v1_mature_trade_count": 0,
        "next_day_trigger_mature_count": 0,
        "trigger_only_excluded_by_follow_through_count": 0,
        "v2_raw_candidate_count": 0,
        "v2_raw_mature_event_count": 0,
    }
    with ThreadPoolExecutor(max_workers=worker_count) as executor:
        for rows, counters in executor.map(lambda p: process_price_path(p, market_regimes), paths):
            all_rows.extend(rows)
            for key, value in counters.items():
                total[key] += int(value)
    detail = pd.DataFrame(all_rows)
    if detail.empty:
        raise SystemExit("ERROR: v2 raw market rerun produced no mature events")
    split = out_of_sample_start_date(detail)
    detail["out_of_sample"] = detail["confirmation_date"].astype(str).map(
        lambda value: true_text() if split and value >= split else false_text()
    )
    timing_keys = timing_audit_60d_keys()
    detail["present_in_timing_audit_60d"] = detail["source_event_key"].map(lambda key: true_text() if key in timing_keys else false_text())
    lower = pd.to_numeric(detail["return_pct"], errors="coerce").quantile(0.01)
    upper = pd.to_numeric(detail["return_pct"], errors="coerce").quantile(0.99)
    returns = pd.to_numeric(detail["return_pct"], errors="coerce")
    detail["anomaly_flag"] = "none"
    detail.loc[returns <= lower, "anomaly_flag"] = "bottom_1pct_return"
    detail.loc[returns >= upper, "anomaly_flag"] = "top_1pct_return"
    detail["generated_at"] = generated_at
    detail = detail.sort_values(["confirmation_date", "stock_id", "source_event_key"]).reset_index(drop=True)
    return detail, total


def return_metrics(part: pd.DataFrame) -> dict[str, Any]:
    returns = pd.to_numeric(part.get("return_pct", pd.Series(dtype=float)), errors="coerce").dropna()
    sample_size = int(len(returns))
    if sample_size == 0:
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
            "min_return_pct": "",
            "max_return_pct": "",
        }
    win_count = int((returns > 0).sum())
    neutral_count = int((returns == 0).sum())
    loss_count = int((returns < 0).sum())
    return {
        "sample_size": sample_size,
        "win_count": win_count,
        "neutral_count": neutral_count,
        "loss_count": loss_count,
        "win_rate_pct": pct_round(win_count / sample_size * 100.0, 2),
        "neutral_rate_pct": pct_round(neutral_count / sample_size * 100.0, 2),
        "loss_rate_pct": pct_round(loss_count / sample_size * 100.0, 2),
        "avg_return_pct": pct_round(float(returns.mean())),
        "median_return_pct": pct_round(float(returns.median())),
        "p10_return_pct": pct_round(float(returns.quantile(0.10))),
        "p90_return_pct": pct_round(float(returns.quantile(0.90))),
        "min_return_pct": pct_round(float(returns.min())),
        "max_return_pct": pct_round(float(returns.max())),
    }


def summary_base(row_type: str, scope: str, key: str, generated_at: str, note: str = "") -> dict[str, Any]:
    return {
        "research_id": RESEARCH_ID,
        "artifact_version": ARTIFACT_VERSION,
        "source_research_id": SOURCE_RESEARCH_ID,
        "advisory_status": ADVISORY_STATUS,
        "model_id": MODEL_ID,
        "row_type": row_type,
        "audit_scope": scope,
        "audit_key": key,
        "sample_size": "",
        "win_count": "",
        "neutral_count": "",
        "loss_count": "",
        "win_rate_pct": "",
        "neutral_rate_pct": "",
        "loss_rate_pct": "",
        "avg_return_pct": "",
        "median_return_pct": "",
        "p10_return_pct": "",
        "p90_return_pct": "",
        "min_return_pct": "",
        "max_return_pct": "",
        "trim_sample_size": "",
        "trim_avg_return_pct": "",
        "trim_median_return_pct": "",
        "anomaly_count": "",
        "scanned_price_files": "",
        "equity_price_files": "",
        "base_v1_signal_count": "",
        "base_v1_mature_trade_count": "",
        "next_day_trigger_mature_count": "",
        "trigger_only_excluded_by_follow_through_count": "",
        "v2_raw_candidate_count": "",
        "v2_raw_mature_event_count": "",
        "timing_audit_60d_event_count": "",
        "raw_minus_timing_count": "",
        "timing_minus_raw_count": "",
        "timing_audit_max_signal_date": "",
        "raw_extension_after_timing_count": "",
        "raw_minus_timing_within_timing_window_count": "",
        "future_leak_count": "",
        "value_a": "",
        "value_b": "",
        "value_c": "",
        "status": "",
        "note": note,
        "approved_for_daily": false_text(),
        "production_readiness": PRODUCTION_READINESS,
        "generated_at": generated_at,
    }


def build_summary(detail: pd.DataFrame, counters: dict[str, int], generated_at: str) -> pd.DataFrame:
    rows: list[dict[str, Any]] = []
    timing = read_csv(SOURCE_TIMING_DETAIL_CSV)
    timing_60 = timing[
        timing.get("high_breakout_60d_met", pd.Series(dtype=str)).astype(str).eq("True")
        & timing.get("known_before_entry_open", pd.Series(dtype=str)).astype(str).eq("True")
    ].copy()
    timing_keys = set(timing_60["source_event_key"].astype(str))
    timing_max_signal_date = safe_str(timing_60["signal_date"].astype(str).max()) if not timing_60.empty else ""
    raw_keys = set(detail["source_event_key"].astype(str))
    raw_minus_timing = raw_keys - timing_keys
    timing_minus_raw = timing_keys - raw_keys
    raw_minus_detail = detail[detail["source_event_key"].astype(str).isin(raw_minus_timing)].copy()
    raw_extension_after_timing = raw_minus_detail[
        raw_minus_detail["signal_date"].astype(str).gt(timing_max_signal_date)
    ].copy()
    raw_minus_within_timing = raw_minus_detail[
        raw_minus_detail["signal_date"].astype(str).le(timing_max_signal_date)
    ].copy()
    all_row = summary_base(
        "raw_market_metrics",
        "all_raw_v2_mature_events",
        "prev60_high_next_day_continuation",
        generated_at,
        "raw price-history rerun of base v1 signal plus 60d high breakout and next-day continuation",
    )
    all_row.update(return_metrics(detail))
    trim = detail[detail["anomaly_flag"].astype(str).eq("none")]
    trim_metrics = return_metrics(trim)
    all_row["trim_sample_size"] = trim_metrics["sample_size"]
    all_row["trim_avg_return_pct"] = trim_metrics["avg_return_pct"]
    all_row["trim_median_return_pct"] = trim_metrics["median_return_pct"]
    all_row["anomaly_count"] = int(detail["anomaly_flag"].astype(str).ne("none").sum())
    all_row["scanned_price_files"] = counters["scanned_price_files"]
    all_row["equity_price_files"] = counters["equity_price_files"]
    all_row["base_v1_signal_count"] = counters["base_v1_signal_count"]
    all_row["base_v1_mature_trade_count"] = counters["base_v1_mature_trade_count"]
    all_row["next_day_trigger_mature_count"] = counters["next_day_trigger_mature_count"]
    all_row["trigger_only_excluded_by_follow_through_count"] = counters["trigger_only_excluded_by_follow_through_count"]
    all_row["v2_raw_candidate_count"] = counters["v2_raw_candidate_count"]
    all_row["v2_raw_mature_event_count"] = counters["v2_raw_mature_event_count"]
    all_row["timing_audit_60d_event_count"] = len(timing_keys)
    all_row["raw_minus_timing_count"] = len(raw_minus_timing)
    all_row["timing_minus_raw_count"] = len(timing_minus_raw)
    all_row["timing_audit_max_signal_date"] = timing_max_signal_date
    all_row["raw_extension_after_timing_count"] = len(raw_extension_after_timing)
    all_row["raw_minus_timing_within_timing_window_count"] = len(raw_minus_within_timing)
    all_row["future_leak_count"] = int(detail["uses_post_entry_information"].astype(str).eq("True").sum())
    if timing_minus_raw:
        all_row["status"] = "membership_mismatch_review_required"
    elif not raw_minus_timing:
        all_row["status"] = "raw_rerun_matches_timing_window"
    elif raw_minus_within_timing.empty:
        all_row["status"] = "raw_rerun_matches_timing_window_with_freshness_extension"
    else:
        all_row["status"] = "raw_rerun_detected_timing_source_gap_research_only"
    all_row["value_a"] = "gate=base_v1_signal_and_prev60_high_plus_2pct"
    all_row["value_b"] = "confirmation=next_day_continuation_confirmed"
    all_row["value_c"] = f"entry_rule={ENTRY_RULE_ID};exit_rule={EXIT_RULE_ID}"
    rows.append(all_row)

    oos = detail[detail["out_of_sample"].astype(str).eq("True")]
    oos_row = summary_base(
        "out_of_sample_metrics",
        "out_of_sample",
        "prev60_high_next_day_continuation",
        generated_at,
        "same raw v2 events restricted to the chronological out-of-sample segment",
    )
    oos_row.update(return_metrics(oos))
    oos_row["status"] = "research_only_oos_check"
    rows.append(oos_row)

    trim_row = summary_base(
        "anomaly_check",
        "trim_return_tail",
        "trim_1pct_each_tail",
        generated_at,
        "extreme rows are excluded only for anomaly sensitivity, not silently removed from detail",
    )
    trim_row.update(return_metrics(trim))
    trim_row["sample_size"] = len(trim)
    trim_row["anomaly_count"] = int(detail["anomaly_flag"].astype(str).ne("none").sum())
    trim_row["value_a"] = f"removed_rows={int(detail['anomaly_flag'].astype(str).ne('none').sum())}"
    trim_row["status"] = "anomaly_rows_marked_review_before_promotion"
    rows.append(trim_row)

    for key, values in [
        ("raw_minus_timing_count", sorted(raw_minus_timing)[:5]),
        ("timing_minus_raw_count", sorted(timing_minus_raw)[:5]),
        ("raw_minus_timing_within_timing_window_count", sorted(raw_minus_within_timing["source_event_key"].astype(str))[:5]),
    ]:
        row = summary_base("membership_check", "raw_vs_timing_audit_60d", key, generated_at)
        if key == "raw_minus_timing_count":
            row["sample_size"] = len(raw_minus_timing)
            if not raw_minus_timing:
                row["status"] = "match"
            elif len(raw_minus_timing) == len(raw_extension_after_timing):
                row["status"] = "freshness_extension_after_timing_window"
            else:
                row["status"] = "source_gap_plus_freshness_extension"
        elif key == "timing_minus_raw_count":
            row["sample_size"] = len(timing_minus_raw)
            row["status"] = "match" if int(row["sample_size"]) == 0 else "mismatch_review_required"
        else:
            row["sample_size"] = len(raw_minus_within_timing)
            row["status"] = "match" if int(row["sample_size"]) == 0 else "source_gap_detected_promotion_blocker"
        row["value_a"] = ";".join(values)
        row["value_b"] = f"timing_audit_max_signal_date={timing_max_signal_date}"
        rows.append(row)

    return pd.DataFrame(rows)


def write_markdown(summary: pd.DataFrame, detail: pd.DataFrame, path: Path) -> None:
    def md_table(df: pd.DataFrame, cols: list[str], limit: int = 20) -> list[str]:
        if df.empty:
            return ["_No rows._"]
        view = df[cols].head(limit).astype(str).replace({"nan": "", "NaN": "", "<NA>": ""})
        lines = ["| " + " | ".join(cols) + " |", "| " + " | ".join(["---"] * len(cols)) + " |"]
        for _, row in view.iterrows():
            lines.append("| " + " | ".join(str(row[col]) for col in cols) + " |")
        return lines

    metrics = summary[summary["row_type"].eq("raw_market_metrics")]
    oos = summary[summary["row_type"].eq("out_of_sample_metrics")]
    anomaly = summary[summary["row_type"].eq("anomaly_check")]
    membership = summary[summary["row_type"].eq("membership_check")]
    lines = [
        "# Volume Range Breakout V2 Raw-Market Rerun",
        "",
        f"- research_id: `{RESEARCH_ID}`",
        f"- artifact_version: `{ARTIFACT_VERSION}`",
        f"- source_research_id: `{SOURCE_RESEARCH_ID}`",
        f"- advisory_status: `{ADVISORY_STATUS}`",
        f"- production_readiness: `{PRODUCTION_READINESS}`",
        "- approved_for_daily: `False`",
        "- This raw-market rerun is research-only and does not change `stock_model_contract_registry.csv`.",
        "- Gate tested: base v1 volume_range_breakout signal, signal close >= previous 60d high + 2pct, and next-day continuation confirmed.",
        "- Entry/exit basis stays unchanged: confirmation next open entry, signal-low stop, otherwise fixed 10-trading-day close exit.",
        "- Membership is compared against the prior timing-audit 60d subset to check whether the earlier artifact was biased by a narrower sample.",
        "- Any raw row inside the timing-audit date window that is absent from the timing artifact is a research/backtest source-gap blocker before promotion.",
        "",
        "## Raw V2 Metrics",
        "",
        *md_table(
            metrics,
            [
                "sample_size",
                "win_rate_pct",
                "neutral_rate_pct",
                "loss_rate_pct",
                "avg_return_pct",
                "median_return_pct",
                "trim_avg_return_pct",
                "trim_median_return_pct",
                "status",
            ],
            limit=5,
        ),
        "",
        "## Data Scope",
        "",
        *md_table(
            metrics,
            [
                "scanned_price_files",
                "equity_price_files",
                "base_v1_signal_count",
                "base_v1_mature_trade_count",
                "next_day_trigger_mature_count",
                "trigger_only_excluded_by_follow_through_count",
                "v2_raw_candidate_count",
                "v2_raw_mature_event_count",
                "timing_audit_60d_event_count",
                "timing_audit_max_signal_date",
                "raw_extension_after_timing_count",
                "raw_minus_timing_within_timing_window_count",
            ],
            limit=5,
        ),
        "",
        "## Out Of Sample",
        "",
        *md_table(
            oos,
            ["sample_size", "win_rate_pct", "loss_rate_pct", "avg_return_pct", "median_return_pct", "status"],
            limit=5,
        ),
        "",
        "## Anomaly Check",
        "",
        *md_table(
            anomaly,
            ["sample_size", "win_rate_pct", "avg_return_pct", "median_return_pct", "anomaly_count", "status"],
            limit=5,
        ),
        "",
        "## Membership Check",
        "",
        *md_table(membership, ["audit_key", "sample_size", "status", "value_a"], limit=10),
        "",
        "## Outputs",
        "",
        f"- summary_csv: `{LATEST_SUMMARY_CSV.as_posix()}`",
        f"- detail_csv: `{LATEST_DETAIL_CSV.as_posix()}`",
        f"- detail_rows: `{len(detail)}`",
    ]
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines) + "\n", encoding="utf-8", newline="\n")


def main() -> int:
    generated_at = now_text()
    detail, counters = build_raw_events(generated_at)
    summary = build_summary(detail, counters, generated_at)
    write_csv(detail, LATEST_DETAIL_CSV, DETAIL_COLUMNS)
    write_csv(detail, HISTORY_DETAIL_CSV, DETAIL_COLUMNS)
    write_csv(summary, LATEST_SUMMARY_CSV, SUMMARY_COLUMNS)
    write_csv(summary, HISTORY_SUMMARY_CSV, SUMMARY_COLUMNS)
    write_markdown(summary, detail, LATEST_MD)
    print(f"Saved: {LATEST_SUMMARY_CSV} rows={len(summary)}")
    print(f"Saved: {LATEST_DETAIL_CSV} rows={len(detail)}")
    print(f"Saved: {LATEST_MD}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
