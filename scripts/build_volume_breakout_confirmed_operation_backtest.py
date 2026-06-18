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

from build_historical_pattern_operation_registry import (  # noqa: E402
    add_research_features,
    formal_model_hit_mask,
    is_equity_stock_id,
    load_market_regime_map,
)
from build_volume_breakout_pattern_classification import classify_event  # noqa: E402
from build_volume_breakout_watch import PRICE_HISTORY_DIR, normalize_stock_id  # noqa: E402
from tracking_utils import latest_stock_price_history_date, normalize_code, normalize_date, safe_str, to_number, write_csv  # noqa: E402
from volume_breakout_operation_utils import (  # noqa: E402
    TRIGGERS as SHARED_TRIGGERS,
    TRIGGER_MAP as SHARED_TRIGGER_MAP,
    TRIGGER_PRIORITY as SHARED_TRIGGER_PRIORITY,
    TriggerSpec,
)


ROOT = Path(".")
LATEST_DIR = ROOT / "output" / "latest"
RESEARCH_HISTORY_DIR = ROOT / "output" / "history" / "research"
TDCC_EVENTS_CSV = RESEARCH_HISTORY_DIR / "tdcc_weekly_ranking_backtest_events.csv"

LATEST_SUMMARY_CSV = LATEST_DIR / "volume_breakout_confirmed_operation_backtest_latest.csv"
LATEST_SUMMARY_MD = LATEST_DIR / "volume_breakout_confirmed_operation_backtest_latest.md"
HISTORY_SUMMARY_CSV = RESEARCH_HISTORY_DIR / "volume_breakout_confirmed_operation_backtest.csv"
HISTORY_EVENTS_CSV = RESEARCH_HISTORY_DIR / "volume_breakout_confirmed_operation_events.csv"
LATEST_FORMAL_SUMMARY_CSV = LATEST_DIR / "volume_breakout_formal_operation_backtest_latest.csv"
LATEST_FORMAL_SUMMARY_MD = LATEST_DIR / "volume_breakout_formal_operation_backtest_latest.md"
HISTORY_FORMAL_EVENTS_CSV = RESEARCH_HISTORY_DIR / "volume_breakout_formal_operation_events.csv"
LATEST_FORMAL_LIFECYCLE_CSV = LATEST_DIR / "volume_breakout_formal_operation_lifecycle_latest.csv"
HISTORY_FORMAL_LIFECYCLE_CSV = RESEARCH_HISTORY_DIR / "volume_breakout_formal_operation_lifecycle_events.csv"
LATEST_RANK_CSV = LATEST_DIR / "volume_breakout_confirmed_operation_rank_latest.csv"
LATEST_RANK_MD = LATEST_DIR / "volume_breakout_confirmed_operation_rank_latest.md"
LATEST_PENDING_CSV = LATEST_DIR / "volume_breakout_pending_operation_queue_latest.csv"
LATEST_PENDING_MD = LATEST_DIR / "volume_breakout_pending_operation_queue_latest.md"

MODEL_ID = "volume_range_breakout"
OVERLAY_MODEL_ID = "tdcc_weekly_ranking_formula"
RESEARCH_ID = "volume_breakout_confirmed_operation"
MAX_CONFIRM_DAYS = 10
MAX_HOLD_DAYS = 10
MAX_TDCC_SIGNAL_AGE_DAYS = 7
OUT_OF_SAMPLE_FRACTION = 0.7

ENTRY_RULE_ID = "confirmation_next_open"
STOP_RULE_ID = "signal_low_stop"
EXIT_RULE_ID = "signal_low_stop_or_fixed_10d_close"
LIFECYCLE_DEFINITION_ID = "daily_volume_breakout_operation_lifecycle_v1"
METRIC_SAMPLE_SCOPE = "mature_selected_operation_only"

FORBIDDEN_PRODUCTION_FIELDS = {
    "trade_decision",
    "action_rating",
    "entry_style",
    "position_sizing",
    "decision_score",
    "daily_candidate_decision",
    "buy_signal",
}

ZH = {
    "next_day_continuation_confirmed": "隔日續強確認",
    "pullback_5ma_confirmed": "回測5MA確認",
    "pullback_10ma_confirmed": "回測10MA確認",
    "no_tdcc": "無TDCC疊加",
    "weekly_increase": "當週大戶增幅排名",
    "consecutive_accumulation": "連續累積排名",
    "all": "全部",
    "top_10": "前10名",
    "top_20": "前20名",
    "top_50": "前50名",
    "operation_trigger": "確認型態",
    "operation_classification": "放量攻擊分類",
    "operation_attack_method": "攻擊方式",
    "operation_price_position": "位階",
    "operation_attack_position": "攻擊方式+位階",
}


# Formal operation trigger order is shared with the daily adapter.
TRIGGERS = list(SHARED_TRIGGERS)
TRIGGER_MAP = dict(SHARED_TRIGGER_MAP)
TRIGGER_PRIORITY = dict(SHARED_TRIGGER_PRIORITY)
SELECTION_COLUMNS = [
    "matched_trigger_ids",
    "selected_trigger_id",
    "selected_confirmation_date",
    "selected_trigger_priority",
    "selected_for_formal_operation",
    "operation_selection_status",
]

SUMMARY_COLUMNS = [
    "model_id",
    "overlay_model_id",
    "research_id",
    "tdcc_list_type",
    "tdcc_list_name_zh",
    "rank_bucket",
    "rank_bucket_name_zh",
    "trigger_id",
    "trigger_name_zh",
    "confluence_scope",
    "confluence_scope_zh",
    "confluence_id",
    "confluence_name_zh",
    "entry_rule_id",
    "entry_rule_zh",
    "stop_loss_rule_id",
    "stop_loss_rule_zh",
    "exit_rule_id",
    "exit_rule_zh",
    "metric_sample_scope",
    "sample_size",
    "unique_signal_events",
    "unique_confirmation_events",
    "unique_stocks",
    "win_rate",
    "avg_return",
    "median_return",
    "max_drawdown",
    "avg_mfe",
    "avg_mae",
    "avg_holding_days",
    "profit_factor",
    "avg_tdcc_rank",
    "avg_tdcc_ranking_score",
    "avg_tdcc_signal_age_days",
    "out_of_sample_size",
    "out_of_sample_win_rate",
    "out_of_sample_avg_return",
    "out_of_sample_median_return",
    "out_of_sample_pass",
    "confidence_status",
    "approved_for_daily",
    "ranking_research_score",
    "ranking_research_rank",
    "risk_notes_zh",
    "generated_at",
    "data_start_date",
    "data_end_date",
    "out_of_sample_start_date",
]

EVENT_COLUMNS = [
    "model_id",
    "overlay_model_id",
    "research_id",
    "signal_date",
    "confirmation_date",
    "confirmation_age_trading_days",
    "tdcc_signal_date",
    "tdcc_signal_age_days",
    "stock_id",
    "stock_name",
    "market",
    "market_regime",
    "trigger_id",
    "trigger_name_zh",
    "confirmation_rule_zh",
    "matched_trigger_ids",
    "selected_trigger_id",
    "selected_confirmation_date",
    "selected_trigger_priority",
    "selected_for_formal_operation",
    "operation_selection_status",
    "operation_lifecycle_definition_id",
    "operation_lifecycle_state",
    "sample_maturity_status",
    "mature_sample_eligible",
    "entry_rule_id",
    "entry_date",
    "entry_price",
    "entry_price_source",
    "stop_loss_rule_id",
    "stop_loss_level",
    "exit_rule_id",
    "exit_date",
    "exit_price",
    "exit_reason",
    "holding_days",
    "return_pct",
    "mfe_pct",
    "mae_pct",
    "out_of_sample",
    "classification_id",
    "classification_name_zh",
    "attack_method",
    "attack_method_name_zh",
    "price_position_type",
    "price_position_name_zh",
    "follow_through_type",
    "follow_through_name_zh",
    "risk_type",
    "risk_name_zh",
    "candle_quality",
    "candle_quality_name_zh",
    "consolidation_type",
    "consolidation_name_zh",
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
    "confirmation_ma5",
    "confirmation_ma10",
    "range_width_20_pct",
    "range_width_40_pct",
    "range_width_60_pct",
    "low_position_60_pct",
    "limit_up_like",
    "tdcc_list_type",
    "tdcc_rank",
    "tdcc_ranking_score",
    "tdcc_weekly_increase_score",
    "tdcc_consecutive_accumulation_score",
    "tdcc_effective_increase_count",
    "tdcc_high_pair_effective_streak_weeks",
    "tdcc_1w_change_400",
    "tdcc_1w_change_600",
    "tdcc_1w_change_800",
    "tdcc_1w_change_1000",
    "theme",
    "theme_mainstream_status",
    "approved_for_daily",
]

LIFECYCLE_COLUMNS = [
    "model_id",
    "overlay_model_id",
    "research_id",
    "operation_lifecycle_definition_id",
    "latest_price_date",
    "signal_date",
    "stock_id",
    "stock_name",
    "market",
    "market_regime",
    "operation_lifecycle_state",
    "operation_lifecycle_state_zh",
    "sample_maturity_status",
    "mature_sample_eligible",
    "matched_trigger_ids",
    "selected_trigger_id",
    "selected_confirmation_date",
    "selected_trigger_priority",
    "confirmation_date",
    "confirmation_age_trading_days",
    "entry_date",
    "planned_exit_date",
    "exit_date",
    "exit_reason",
    "terminal_reason",
    "stop_loss_rule_id",
    "stop_loss_level",
    "exit_rule_id",
    "return_pct",
    "mfe_pct",
    "mae_pct",
    "classification_id",
    "classification_name_zh",
    "attack_method",
    "attack_method_name_zh",
    "price_position_type",
    "price_position_name_zh",
    "follow_through_type",
    "follow_through_name_zh",
    "risk_type",
    "risk_name_zh",
    "candle_quality",
    "candle_quality_name_zh",
    "consolidation_type",
    "consolidation_name_zh",
    "volume_ratio",
    "signal_return_1d_pct",
    "signal_open",
    "signal_high",
    "signal_low",
    "signal_close",
    "range_width_20_pct",
    "range_width_40_pct",
    "range_width_60_pct",
    "low_position_60_pct",
    "limit_up_like",
    "approved_for_daily",
]

RANK_COLUMNS = [
    "operation_rank",
    "model_id",
    "overlay_model_id",
    "research_id",
    "latest_price_date",
    "signal_date",
    "confirmation_date",
    "confirmation_age_trading_days",
    "stock_id",
    "stock_name",
    "market",
    "trigger_id",
    "trigger_name_zh",
    "confirmation_rule_zh",
    "matched_trigger_ids",
    "selected_trigger_id",
    "selected_confirmation_date",
    "selected_trigger_priority",
    "operation_selection_status",
    "entry_rule_id",
    "entry_rule_zh",
    "planned_entry_timing_zh",
    "entry_price_status",
    "stop_loss_rule_id",
    "stop_loss_rule_zh",
    "stop_loss_level",
    "exit_rule_id",
    "exit_rule_zh",
    "tdcc_list_type",
    "tdcc_signal_date",
    "tdcc_signal_age_days",
    "tdcc_rank",
    "tdcc_ranking_score",
    "classification_id",
    "classification_name_zh",
    "attack_method",
    "attack_method_name_zh",
    "price_position_type",
    "price_position_name_zh",
    "risk_type",
    "risk_name_zh",
    "evidence_confluence_scope",
    "evidence_confluence_id",
    "evidence_rank_bucket",
    "evidence_sample_size",
    "evidence_win_rate",
    "evidence_avg_return",
    "evidence_median_return",
    "evidence_confidence_status",
    "evidence_out_of_sample_pass",
    "ranking_research_score",
    "approved_for_daily",
]

PENDING_COLUMNS = [
    "queue_date",
    "model_id",
    "research_id",
    "signal_date",
    "signal_age_trading_days",
    "stock_id",
    "stock_name",
    "market",
    "pending_trigger_ids",
    "expired",
    "broken_signal_low",
    "stop_loss_level",
    "watch_until_trading_date",
    "classification_id",
    "attack_method",
    "price_position_type",
    "approved_for_daily",
]

DIMENSION_SCOPES = [
    ("operation_classification", "classification_id", "classification_name_zh"),
    ("operation_attack_method", "attack_method", "attack_method_name_zh"),
    ("operation_price_position", "price_position_type", "price_position_name_zh"),
]


def now_text() -> str:
    return datetime.now(ZoneInfo("Asia/Taipei")).strftime("%Y-%m-%d %H:%M:%S Asia/Taipei")


def read_csv(path: Path) -> pd.DataFrame:
    if not path.exists():
        return pd.DataFrame()
    try:
        return pd.read_csv(path, dtype=str, keep_default_na=False)
    except Exception:
        return pd.DataFrame()


def pct_round(value: Any, digits: int = 4) -> float | str:
    num = to_number(value)
    if math.isnan(num):
        return ""
    return round(num, digits)


def boolish(value: Any) -> bool:
    return safe_str(value).lower() in {"true", "1", "1.0", "yes", "y", "t"}


def safe_price(value: Any) -> float:
    num = to_number(value)
    return num if not math.isnan(num) and num > 0 else math.nan


def load_price_csv(path: Path) -> pd.DataFrame:
    try:
        return pd.read_csv(path, dtype=str, keep_default_na=False)
    except Exception:
        return pd.DataFrame()


def stop_price_for_day(row: pd.Series, stop_level: float) -> float:
    open_price = safe_price(row.get("open"))
    if not math.isnan(open_price) and open_price < stop_level:
        return open_price
    return stop_level


def signal_low_broken(price: pd.DataFrame, signal_idx: int, through_idx: int, signal_low: float) -> bool:
    if math.isnan(signal_low):
        return True
    if through_idx <= signal_idx:
        return False
    lows = pd.to_numeric(price.iloc[signal_idx + 1 : through_idx + 1]["low"], errors="coerce")
    return bool(lows.lt(signal_low).fillna(False).any())


def find_confirmation(price: pd.DataFrame, signal_idx: int, spec: TriggerSpec) -> dict[str, Any] | None:
    signal = price.iloc[signal_idx]
    signal_close = safe_price(signal.get("close"))
    signal_high = safe_price(signal.get("high"))
    signal_low = safe_price(signal.get("low"))
    if any(math.isnan(x) for x in [signal_close, signal_high, signal_low]):
        return None

    if spec.trigger_id == "next_day_break_signal_high_confirmed":
        confirm_idx = signal_idx + 1
        if confirm_idx >= len(price) or signal_low_broken(price, signal_idx, confirm_idx, signal_low):
            return None
        row = price.iloc[confirm_idx]
        high = safe_price(row.get("high"))
        close = safe_price(row.get("close"))
        if not math.isnan(high) and not math.isnan(close) and high >= signal_high and close >= signal_close:
            return {"confirmation_idx": confirm_idx}
        return None

    if spec.trigger_id == "next_day_continuation_confirmed":
        confirm_idx = signal_idx + 1
        if confirm_idx >= len(price) or signal_low_broken(price, signal_idx, confirm_idx, signal_low):
            return None
        row = price.iloc[confirm_idx]
        close = safe_price(row.get("close"))
        if not math.isnan(close) and close > signal_close and close >= signal_high:
            return {"confirmation_idx": confirm_idx}
        return None

    if spec.ma_col:
        end_idx = min(len(price) - 1, signal_idx + spec.max_confirm_days)
        for confirm_idx in range(signal_idx + 1, end_idx + 1):
            if signal_low_broken(price, signal_idx, confirm_idx, signal_low):
                return None
            row = price.iloc[confirm_idx]
            ma = safe_price(row.get(spec.ma_col))
            low = safe_price(row.get("low"))
            close = safe_price(row.get("close"))
            if any(math.isnan(x) for x in [ma, low, close]):
                continue
            if low <= ma and close >= ma:
                return {"confirmation_idx": confirm_idx}
    return None


def confirmation_matches(price: pd.DataFrame, signal_idx: int, through_idx: int | None = None) -> list[dict[str, Any]]:
    matches: list[dict[str, Any]] = []
    for spec in TRIGGERS:
        found = find_confirmation(price, signal_idx, spec)
        if found is None:
            continue
        confirmation_idx = int(found["confirmation_idx"])
        if through_idx is not None and confirmation_idx > through_idx:
            continue
        matches.append(
            {
                "trigger_id": spec.trigger_id,
                "trigger_name_zh": spec.trigger_name_zh,
                "confirmation_rule_zh": spec.confirmation_rule_zh,
                "confirmation_idx": confirmation_idx,
                "confirmation_date": normalize_date(price.iloc[confirmation_idx].get("date")),
                "trigger_priority": trigger_priority(spec.trigger_id),
            }
        )
    return sorted(matches, key=lambda row: (row["confirmation_idx"], row["trigger_priority"], row["trigger_id"]))


def selected_confirmation_for_signal(
    price: pd.DataFrame,
    signal_idx: int,
    through_idx: int | None = None,
) -> dict[str, Any] | None:
    matches = confirmation_matches(price, signal_idx, through_idx)
    if not matches:
        return None
    selected = dict(matches[0])
    selected["matched_trigger_ids"] = "|".join(dict.fromkeys(row["trigger_id"] for row in matches))
    return selected


def simulate_confirmed_trade(price: pd.DataFrame, signal_idx: int, confirmation_idx: int) -> dict[str, Any] | None:
    entry_idx = confirmation_idx + 1
    planned_exit_idx = entry_idx + MAX_HOLD_DAYS - 1
    if planned_exit_idx >= len(price):
        return None

    signal = price.iloc[signal_idx]
    entry = price.iloc[entry_idx]
    signal_low = safe_price(signal.get("low"))
    entry_price = safe_price(entry.get("open"))
    if any(math.isnan(x) for x in [signal_low, entry_price]):
        return None

    exit_idx = planned_exit_idx
    exit_price = safe_price(price.iloc[planned_exit_idx].get("close"))
    exit_reason = f"fixed_{MAX_HOLD_DAYS}d_close"
    if math.isnan(exit_price):
        return None

    for day_idx in range(entry_idx, planned_exit_idx + 1):
        day = price.iloc[day_idx]
        low = safe_price(day.get("low"))
        if not math.isnan(low) and low <= signal_low:
            exit_idx = day_idx
            exit_price = stop_price_for_day(day, signal_low)
            exit_reason = "stop_signal_low"
            break

    holding_window = price.iloc[entry_idx : exit_idx + 1]
    max_high = pd.to_numeric(holding_window["high"], errors="coerce").max()
    min_low = pd.to_numeric(holding_window["low"], errors="coerce").min()
    return_pct = (exit_price / entry_price - 1.0) * 100.0
    mfe_pct = (max_high / entry_price - 1.0) * 100.0 if not math.isnan(max_high) else math.nan
    mae_pct = (min_low / entry_price - 1.0) * 100.0 if not math.isnan(min_low) else math.nan

    return {
        "entry_date": normalize_date(entry.get("date")),
        "entry_price": round(entry_price, 4),
        "entry_price_source": ENTRY_RULE_ID,
        "stop_loss_rule_id": STOP_RULE_ID,
        "stop_loss_level": round(signal_low, 4),
        "exit_rule_id": EXIT_RULE_ID,
        "exit_date": normalize_date(price.iloc[exit_idx].get("date")),
        "exit_price": round(exit_price, 4),
        "exit_reason": exit_reason,
        "holding_days": exit_idx - entry_idx + 1,
        "return_pct": round(return_pct, 4),
        "mfe_pct": round(mfe_pct, 4) if not math.isnan(mfe_pct) else "",
        "mae_pct": round(mae_pct, 4) if not math.isnan(mae_pct) else "",
    }


def stop_hit_index(price: pd.DataFrame, entry_idx: int, through_idx: int, signal_low: float) -> int | None:
    if math.isnan(signal_low):
        return None
    for idx in range(entry_idx, min(through_idx, len(price) - 1) + 1):
        low = safe_price(price.iloc[idx].get("low"))
        if not math.isnan(low) and low <= signal_low:
            return idx
    return None


def lifecycle_state_for_signal(price: pd.DataFrame, signal_idx: int, asof_idx: int) -> dict[str, Any]:
    latest_idx = min(max(asof_idx, signal_idx), len(price) - 1)
    signal = price.iloc[signal_idx]
    signal_low = safe_price(signal.get("low"))
    selected = selected_confirmation_for_signal(price, signal_idx, latest_idx)
    state = "expired"
    state_zh = "已失效"
    terminal_reason = ""
    maturity_status = "not_mature"
    mature_eligible = False
    trade: dict[str, Any] | None = None
    entry_idx: int | None = None
    planned_exit_idx: int | None = None

    if selected is not None:
        confirmation_idx = int(selected["confirmation_idx"])
        entry_idx = confirmation_idx + 1
        planned_exit_idx = entry_idx + MAX_HOLD_DAYS - 1
        trade = simulate_confirmed_trade(price, signal_idx, confirmation_idx)
        if trade is not None:
            mature_eligible = True
            maturity_status = "mature"
        elif latest_idx < entry_idx:
            maturity_status = "confirmed_not_entered"
        else:
            maturity_status = "immature_active"

        if confirmation_idx == latest_idx:
            state = "confirmed_operation"
            state_zh = "已確認操作"
            terminal_reason = "confirmation_on_asof_date"
        elif entry_idx < len(price) and latest_idx >= entry_idx:
            stopped_idx = stop_hit_index(price, entry_idx, latest_idx, signal_low)
            if stopped_idx is None and planned_exit_idx is not None and latest_idx <= planned_exit_idx:
                state = "active_operation"
                state_zh = "操作中"
                terminal_reason = "within_d0_d10_hold_window"
            else:
                state = "expired"
                state_zh = "已失效"
                terminal_reason = "stop_or_fixed_hold_window_finished"
        else:
            state = "confirmed_operation"
            state_zh = "已確認操作"
            terminal_reason = "confirmed_waiting_next_open"
    else:
        signal_age = latest_idx - signal_idx
        broken = signal_low_broken(price, signal_idx, latest_idx, signal_low)
        if signal_age <= MAX_CONFIRM_DAYS and not broken:
            state = "pending_confirmation"
            state_zh = "待確認"
            terminal_reason = "within_confirmation_window"
            maturity_status = "pending_confirmation"
        else:
            state = "expired"
            state_zh = "已失效"
            terminal_reason = "signal_low_broken_before_confirmation" if broken else "confirmation_window_expired"
            maturity_status = "expired_unconfirmed"

    out: dict[str, Any] = {
        "operation_lifecycle_state": state,
        "operation_lifecycle_state_zh": state_zh,
        "sample_maturity_status": maturity_status,
        "mature_sample_eligible": mature_eligible,
        "terminal_reason": terminal_reason,
        "selected": selected,
        "trade": trade,
        "entry_idx": entry_idx,
        "planned_exit_idx": planned_exit_idx,
    }
    return out


def future_context(price: pd.DataFrame, signal_idx: int) -> dict[str, Any]:
    signal = price.iloc[signal_idx]
    out: dict[str, Any] = {
        "signal_open": pct_round(signal.get("open")),
        "signal_high": pct_round(signal.get("high")),
        "signal_low": pct_round(signal.get("low")),
        "signal_close": pct_round(signal.get("close")),
        "next_open": "",
        "next_high": "",
        "next_low": "",
        "next_close": "",
        "touch_5ma_10d": False,
        "touch_10ma_10d": False,
        "break_signal_low_5d": False,
    }
    if signal_idx + 1 < len(price):
        nxt = price.iloc[signal_idx + 1]
        out.update(
            {
                "next_open": pct_round(nxt.get("open")),
                "next_high": pct_round(nxt.get("high")),
                "next_low": pct_round(nxt.get("low")),
                "next_close": pct_round(nxt.get("close")),
            }
        )
    window = price.iloc[signal_idx + 1 : min(len(price), signal_idx + MAX_CONFIRM_DAYS + 1)]
    signal_low = to_number(out["signal_low"])
    if not window.empty:
        low = pd.to_numeric(window.get("low", pd.Series(index=window.index, dtype=float)), errors="coerce")
        ma5 = pd.to_numeric(window.get("ma5", pd.Series(index=window.index, dtype=float)), errors="coerce")
        ma10 = pd.to_numeric(window.get("ma10", pd.Series(index=window.index, dtype=float)), errors="coerce")
        out["touch_5ma_10d"] = bool((low <= ma5).fillna(False).any())
        out["touch_10ma_10d"] = bool((low <= ma10).fillna(False).any())
        out["break_signal_low_5d"] = bool(
            not math.isnan(signal_low) and (low.head(5) < signal_low).fillna(False).any()
        )
    return out


def event_payload(price: pd.DataFrame, signal_idx: int, confirmation_idx: int, market_regimes: dict[str, str]) -> dict[str, Any]:
    signal = price.iloc[signal_idx]
    confirmation = price.iloc[confirmation_idx]
    signal_date = normalize_date(signal.get("date"))
    base = {
        "model_id": MODEL_ID,
        "overlay_model_id": OVERLAY_MODEL_ID,
        "research_id": RESEARCH_ID,
        "signal_date": signal_date,
        "confirmation_date": normalize_date(confirmation.get("date")),
        "confirmation_age_trading_days": confirmation_idx - signal_idx,
        "stock_id": normalize_stock_id(signal.get("stock_id")),
        "stock_name": safe_str(signal.get("stock_name")),
        "market": safe_str(signal.get("market")),
        "market_regime": market_regimes.get(signal_date, "unknown"),
        "entry_rule_id": ENTRY_RULE_ID,
        "volume_ratio": pct_round(signal.get("volume_ratio")),
        "signal_return_1d_pct": pct_round(signal.get("signal_return_1d_pct")),
        "previous_20d_high": pct_round(signal.get("previous_20d_high_calc")),
        "range_width_20_pct": pct_round(signal.get("range_width_20_pct")),
        "range_width_40_pct": pct_round(signal.get("range_width_40_pct")),
        "range_width_60_pct": pct_round(signal.get("range_width_60_pct")),
        "low_position_60_pct": pct_round(signal.get("low_position_60_pct")),
        "limit_up_like": boolish(signal.get("limit_up_like")),
        "confirmation_open": pct_round(confirmation.get("open")),
        "confirmation_high": pct_round(confirmation.get("high")),
        "confirmation_low": pct_round(confirmation.get("low")),
        "confirmation_close": pct_round(confirmation.get("close")),
        "confirmation_ma5": pct_round(confirmation.get("ma5")),
        "confirmation_ma10": pct_round(confirmation.get("ma10")),
    }
    class_context = {**base, **future_context(price, signal_idx)}
    class_context["previous_20d_high"] = base["previous_20d_high"]
    class_context.update(classify_event(pd.Series(class_context)))
    return {**base, **class_context}


def signal_lifecycle_payload(price: pd.DataFrame, signal_idx: int, asof_idx: int, market_regimes: dict[str, str]) -> dict[str, Any]:
    signal = price.iloc[signal_idx]
    asof = price.iloc[asof_idx]
    signal_date = normalize_date(signal.get("date"))
    base = {
        "model_id": MODEL_ID,
        "overlay_model_id": OVERLAY_MODEL_ID,
        "research_id": RESEARCH_ID,
        "operation_lifecycle_definition_id": LIFECYCLE_DEFINITION_ID,
        "latest_price_date": normalize_date(asof.get("date")),
        "signal_date": signal_date,
        "stock_id": normalize_stock_id(signal.get("stock_id")),
        "stock_name": safe_str(signal.get("stock_name")),
        "market": safe_str(signal.get("market")),
        "market_regime": market_regimes.get(signal_date, "unknown"),
        "volume_ratio": pct_round(signal.get("volume_ratio")),
        "signal_return_1d_pct": pct_round(signal.get("signal_return_1d_pct")),
        "previous_20d_high": pct_round(signal.get("previous_20d_high_calc")),
        "range_width_20_pct": pct_round(signal.get("range_width_20_pct")),
        "range_width_40_pct": pct_round(signal.get("range_width_40_pct")),
        "range_width_60_pct": pct_round(signal.get("range_width_60_pct")),
        "low_position_60_pct": pct_round(signal.get("low_position_60_pct")),
        "limit_up_like": boolish(signal.get("limit_up_like")),
        "signal_open": pct_round(signal.get("open")),
        "signal_high": pct_round(signal.get("high")),
        "signal_low": pct_round(signal.get("low")),
        "signal_close": pct_round(signal.get("close")),
    }
    class_context = {**base, **future_context(price, signal_idx)}
    class_context["previous_20d_high"] = base["previous_20d_high"]
    class_context.update(classify_event(pd.Series(class_context)))
    return {**base, **class_context}


def lifecycle_event_payload(price: pd.DataFrame, signal_idx: int, asof_idx: int, market_regimes: dict[str, str]) -> dict[str, Any]:
    payload = signal_lifecycle_payload(price, signal_idx, asof_idx, market_regimes)
    lifecycle = lifecycle_state_for_signal(price, signal_idx, asof_idx)
    selected = lifecycle.get("selected") or {}
    trade = lifecycle.get("trade") or {}
    signal_low = safe_price(price.iloc[signal_idx].get("low"))
    entry_idx = lifecycle.get("entry_idx")
    planned_exit_idx = lifecycle.get("planned_exit_idx")
    confirmation_idx = selected.get("confirmation_idx")

    payload.update(
        {
            "operation_lifecycle_state": lifecycle["operation_lifecycle_state"],
            "operation_lifecycle_state_zh": lifecycle["operation_lifecycle_state_zh"],
            "sample_maturity_status": lifecycle["sample_maturity_status"],
            "mature_sample_eligible": lifecycle["mature_sample_eligible"],
            "matched_trigger_ids": safe_str(selected.get("matched_trigger_ids")),
            "selected_trigger_id": safe_str(selected.get("trigger_id")),
            "selected_confirmation_date": safe_str(selected.get("confirmation_date")),
            "selected_trigger_priority": safe_str(selected.get("trigger_priority")),
            "confirmation_date": safe_str(selected.get("confirmation_date")),
            "confirmation_age_trading_days": (
                int(confirmation_idx) - signal_idx if confirmation_idx is not None else ""
            ),
            "entry_date": (
                normalize_date(price.iloc[int(entry_idx)].get("date"))
                if isinstance(entry_idx, int) and entry_idx < len(price)
                else ""
            ),
            "planned_exit_date": (
                normalize_date(price.iloc[int(planned_exit_idx)].get("date"))
                if isinstance(planned_exit_idx, int) and planned_exit_idx < len(price)
                else ""
            ),
            "exit_date": safe_str(trade.get("exit_date")),
            "exit_reason": safe_str(trade.get("exit_reason")),
            "terminal_reason": safe_str(lifecycle.get("terminal_reason")),
            "stop_loss_rule_id": STOP_RULE_ID,
            "stop_loss_level": round(signal_low, 4) if not math.isnan(signal_low) else "",
            "exit_rule_id": EXIT_RULE_ID,
            "return_pct": safe_str(trade.get("return_pct")),
            "mfe_pct": safe_str(trade.get("mfe_pct")),
            "mae_pct": safe_str(trade.get("mae_pct")),
            "approved_for_daily": False,
        }
    )
    return payload


def process_price_history_path(path: Path, market_regimes: dict[str, str]) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    raw = load_price_csv(path)
    if raw.empty or len(raw) < 90:
        return rows
    if not {"date", "stock_id", "stock_name", "open", "high", "low", "close", "volume"}.issubset(raw.columns):
        return rows
    first_id = normalize_code(raw.iloc[0].get("stock_id"))
    if not is_equity_stock_id(first_id):
        return rows
    price = add_research_features(raw)
    if price.empty:
        return rows
    model_mask = formal_model_hit_mask(price)
    for signal_idx in [int(idx) for idx in model_mask[model_mask].index]:
        for spec in TRIGGERS:
            confirmation = find_confirmation(price, signal_idx, spec)
            if confirmation is None:
                continue
            confirmation_idx = int(confirmation["confirmation_idx"])
            trade = simulate_confirmed_trade(price, signal_idx, confirmation_idx)
            if trade is None:
                continue
            payload = event_payload(price, signal_idx, confirmation_idx, market_regimes)
            payload.update(
                {
                    "trigger_id": spec.trigger_id,
                    "trigger_name_zh": spec.trigger_name_zh,
                    "confirmation_rule_zh": spec.confirmation_rule_zh,
                    "approved_for_daily": False,
                    "operation_lifecycle_definition_id": LIFECYCLE_DEFINITION_ID,
                    "operation_lifecycle_state": "expired",
                    "sample_maturity_status": "mature",
                    "mature_sample_eligible": True,
                    **trade,
                }
            )
            rows.append(payload)
    return rows


def process_lifecycle_path(path: Path, market_regimes: dict[str, str]) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    raw = load_price_csv(path)
    if raw.empty or len(raw) < 90:
        return rows
    if not {"date", "stock_id", "stock_name", "open", "high", "low", "close", "volume"}.issubset(raw.columns):
        return rows
    first_id = normalize_code(raw.iloc[0].get("stock_id"))
    if not is_equity_stock_id(first_id):
        return rows
    price = add_research_features(raw)
    if price.empty:
        return rows
    asof_idx = len(price) - 1
    model_mask = formal_model_hit_mask(price)
    for signal_idx in [int(idx) for idx in model_mask[model_mask].index]:
        if signal_idx > asof_idx:
            continue
        rows.append(lifecycle_event_payload(price, signal_idx, asof_idx, market_regimes))
    return rows


def build_base_events() -> pd.DataFrame:
    market_regimes = load_market_regime_map()
    paths = sorted(PRICE_HISTORY_DIR.glob("*.csv"))
    worker_count = min(12, max(2, os.cpu_count() or 4))
    rows: list[dict[str, Any]] = []
    with ThreadPoolExecutor(max_workers=worker_count) as executor:
        for part in executor.map(lambda p: process_price_history_path(p, market_regimes), paths):
            rows.extend(part)
    if not rows:
        return pd.DataFrame(columns=EVENT_COLUMNS)
    events = pd.DataFrame(rows)
    split_date = out_of_sample_start_date(events, "confirmation_date")
    events["out_of_sample"] = events["confirmation_date"].map(lambda value: bool(split_date and safe_str(value) >= split_date))
    events = add_operation_selection_columns(events)
    events = attach_tdcc_asof(events, read_tdcc_events(), "confirmation_date")
    return ensure_columns(events, EVENT_COLUMNS).sort_values(
        ["confirmation_date", "stock_id", "trigger_id", "tdcc_list_type"]
    ).reset_index(drop=True)


def build_lifecycle_events() -> pd.DataFrame:
    market_regimes = load_market_regime_map()
    paths = sorted(PRICE_HISTORY_DIR.glob("*.csv"))
    worker_count = min(12, max(2, os.cpu_count() or 4))
    rows: list[dict[str, Any]] = []
    with ThreadPoolExecutor(max_workers=worker_count) as executor:
        for part in executor.map(lambda p: process_lifecycle_path(p, market_regimes), paths):
            rows.extend(part)
    if not rows:
        return pd.DataFrame(columns=LIFECYCLE_COLUMNS)
    out = ensure_columns(pd.DataFrame(rows), LIFECYCLE_COLUMNS)
    return out.sort_values(["signal_date", "stock_id"]).reset_index(drop=True)


def apply_lifecycle_state_columns(events: pd.DataFrame, lifecycle: pd.DataFrame) -> pd.DataFrame:
    if events.empty or lifecycle.empty:
        return events
    keys = ["signal_date", "stock_id"]
    state_cols = [
        "operation_lifecycle_definition_id",
        "operation_lifecycle_state",
        "sample_maturity_status",
        "mature_sample_eligible",
    ]
    lookup = lifecycle[keys + state_cols].drop_duplicates(keys).copy()
    out = events.drop(columns=state_cols, errors="ignore").merge(lookup, on=keys, how="left")
    out["operation_lifecycle_definition_id"] = out["operation_lifecycle_definition_id"].fillna(LIFECYCLE_DEFINITION_ID)
    out["operation_lifecycle_state"] = out["operation_lifecycle_state"].fillna("expired")
    out["sample_maturity_status"] = out["sample_maturity_status"].fillna("mature")
    out["mature_sample_eligible"] = out["mature_sample_eligible"].fillna(True)
    return out


def out_of_sample_start_date(df: pd.DataFrame, date_col: str) -> str:
    dates = sorted({normalize_date(value) for value in df.get(date_col, []) if normalize_date(value)})
    if len(dates) < 5:
        return ""
    return dates[int(len(dates) * OUT_OF_SAMPLE_FRACTION)]


def read_tdcc_events() -> pd.DataFrame:
    tdcc = read_csv(TDCC_EVENTS_CSV)
    if tdcc.empty:
        return tdcc
    if "stock_id" in tdcc.columns:
        tdcc["stock_id"] = tdcc["stock_id"].map(normalize_code)
    if "signal_date" in tdcc.columns:
        tdcc["signal_date"] = tdcc["signal_date"].map(normalize_date)
    tdcc = tdcc[tdcc.get("model_id", "").astype(str).eq(OVERLAY_MODEL_ID)].copy()
    tdcc = tdcc[(tdcc.get("stock_id", "") != "") & (tdcc.get("signal_date", "") != "")]
    return tdcc


def baseline_rows(events: pd.DataFrame) -> pd.DataFrame:
    out = events.copy()
    out["tdcc_list_type"] = "no_tdcc"
    out["tdcc_signal_date"] = ""
    out["tdcc_signal_age_days"] = ""
    for col in [
        "tdcc_rank",
        "tdcc_ranking_score",
        "tdcc_weekly_increase_score",
        "tdcc_consecutive_accumulation_score",
        "tdcc_effective_increase_count",
        "tdcc_high_pair_effective_streak_weeks",
        "tdcc_1w_change_400",
        "tdcc_1w_change_600",
        "tdcc_1w_change_800",
        "tdcc_1w_change_1000",
        "theme",
        "theme_mainstream_status",
    ]:
        out[col] = ""
    return out


def attach_tdcc_asof(events: pd.DataFrame, tdcc: pd.DataFrame, asof_date_col: str) -> pd.DataFrame:
    if events.empty:
        return pd.DataFrame(columns=EVENT_COLUMNS)
    base = baseline_rows(events)
    if tdcc.empty:
        return base

    events = events.copy()
    tdcc = tdcc.copy()
    events["asof_dt"] = pd.to_datetime(events[asof_date_col].map(normalize_date), format="%Y%m%d", errors="coerce")
    tdcc["signal_dt"] = pd.to_datetime(tdcc["signal_date"].map(normalize_date), format="%Y%m%d", errors="coerce")
    events = events.dropna(subset=["asof_dt"])
    tdcc = tdcc.dropna(subset=["signal_dt"])

    rows: list[pd.DataFrame] = [base]
    for list_type in sorted(set(tdcc.get("tdcc_list_type", "").astype(str)) - {""}):
        part = tdcc[tdcc["tdcc_list_type"].astype(str).eq(list_type)].copy()
        if part.empty:
            continue
        merged = pd.merge_asof(
            events.sort_values(["asof_dt", "stock_id"]),
            part.sort_values(["signal_dt", "stock_id"]),
            by="stock_id",
            left_on="asof_dt",
            right_on="signal_dt",
            direction="backward",
            tolerance=pd.Timedelta(days=MAX_TDCC_SIGNAL_AGE_DAYS),
            suffixes=("", "_tdcc"),
        )
        tdcc_signal_col = "signal_date_tdcc" if "signal_date_tdcc" in merged.columns else "signal_date"
        merged = merged[merged.get(tdcc_signal_col, "").map(safe_str) != ""].copy()
        if merged.empty:
            continue
        merged["tdcc_signal_date"] = merged[tdcc_signal_col]
        merged["tdcc_signal_age_days"] = (merged["asof_dt"] - merged["signal_dt"]).dt.days
        merged["tdcc_list_type"] = list_type
        for col in [
            "tdcc_rank",
            "tdcc_ranking_score",
            "tdcc_weekly_increase_score",
            "tdcc_consecutive_accumulation_score",
            "tdcc_effective_increase_count",
            "tdcc_high_pair_effective_streak_weeks",
            "tdcc_1w_change_400",
            "tdcc_1w_change_600",
            "tdcc_1w_change_800",
            "tdcc_1w_change_1000",
            "theme",
            "theme_mainstream_status",
        ]:
            suffixed = f"{col}_tdcc"
            if suffixed in merged.columns:
                merged[col] = merged[suffixed]
        rows.append(merged)

    out = pd.concat(rows, ignore_index=True, sort=False)
    out["overlay_model_id"] = OVERLAY_MODEL_ID
    out["research_id"] = RESEARCH_ID
    out["approved_for_daily"] = False
    return ensure_columns(out, EVENT_COLUMNS)


def ensure_columns(df: pd.DataFrame, columns: list[str]) -> pd.DataFrame:
    out = df.copy()
    for col in columns:
        if col not in out.columns:
            out[col] = ""
    return out[columns]


def trigger_priority(trigger_id: Any) -> int:
    return TRIGGER_PRIORITY.get(safe_str(trigger_id), 999)


def add_operation_selection_columns(events: pd.DataFrame) -> pd.DataFrame:
    """Mark the single formal operation row for each signal while preserving research matches."""
    out = events.copy()
    for col in SELECTION_COLUMNS:
        if col not in out.columns:
            out[col] = ""
    if out.empty:
        return out

    out["_selection_confirmation_dt"] = pd.to_datetime(
        out.get("confirmation_date", pd.Series(dtype=str)).map(normalize_date),
        format="%Y%m%d",
        errors="coerce",
    )
    out["_selection_age"] = pd.to_numeric(out.get("confirmation_age_trading_days"), errors="coerce").fillna(999)
    out["_selection_priority"] = out.get("trigger_id", pd.Series(dtype=str)).map(trigger_priority)
    out["_original_order"] = range(len(out))

    group_cols = ["signal_date", "stock_id"]
    for col in group_cols:
        if col not in out.columns:
            out[col] = ""

    sort_cols = [
        "_selection_confirmation_dt",
        "_selection_age",
        "_selection_priority",
        "trigger_id",
        "_original_order",
    ]
    for _, part in out.groupby(group_cols, dropna=False, sort=False):
        ordered = part.sort_values(sort_cols, ascending=[True, True, True, True, True])
        if ordered.empty:
            continue
        trigger_ids: list[str] = []
        for trigger_id in ordered["trigger_id"].map(safe_str).tolist():
            if trigger_id and trigger_id not in trigger_ids:
                trigger_ids.append(trigger_id)
        selected_idx = ordered.index[0]
        selected = out.loc[selected_idx]
        matched_text = "|".join(trigger_ids)
        out.loc[part.index, "matched_trigger_ids"] = matched_text
        out.loc[part.index, "selected_trigger_id"] = safe_str(selected.get("trigger_id"))
        out.loc[part.index, "selected_confirmation_date"] = normalize_date(selected.get("confirmation_date"))
        out.loc[part.index, "selected_trigger_priority"] = str(trigger_priority(selected.get("trigger_id")))
        out.loc[part.index, "selected_for_formal_operation"] = "False"
        out.loc[part.index, "operation_selection_status"] = "research_duplicate_trigger_not_selected"
        out.loc[selected_idx, "selected_for_formal_operation"] = "True"
        out.loc[selected_idx, "operation_selection_status"] = "selected_formal_operation"

    return out.drop(
        columns=[
            "_selection_confirmation_dt",
            "_selection_age",
            "_selection_priority",
            "_original_order",
        ],
        errors="ignore",
    )


def formal_operation_events(events: pd.DataFrame) -> pd.DataFrame:
    if events.empty or "selected_for_formal_operation" not in events.columns:
        return pd.DataFrame(columns=EVENT_COLUMNS)
    return events[events["selected_for_formal_operation"].astype(str).eq("True")].copy()


def profit_factor(returns: pd.Series) -> float | str:
    ret = pd.to_numeric(returns, errors="coerce").dropna()
    if ret.empty:
        return ""
    gains = ret[ret > 0].sum()
    losses = ret[ret < 0].sum()
    if losses == 0:
        return "" if gains == 0 else round(999.0, 4)
    return round(float(gains / abs(losses)), 4)


def out_of_sample_pass(part: pd.DataFrame) -> bool:
    oos = part[part["out_of_sample"].map(boolish)]
    returns = pd.to_numeric(oos["return_pct"], errors="coerce").dropna()
    if len(returns) < 10:
        return False
    return bool((returns > 0).mean() >= 0.5 and returns.mean() > 0 and returns.median() > 0)


def confidence_status(sample_size: int, out_of_sample_size: int, row_pass: bool) -> str:
    if sample_size >= 100 and out_of_sample_size >= 30 and row_pass:
        return "high"
    if sample_size >= 30 and out_of_sample_size >= 10:
        return "medium"
    return "low"


def ranking_score(row: dict[str, Any]) -> float:
    win = to_number(row.get("win_rate"))
    avg = to_number(row.get("avg_return"))
    median = to_number(row.get("median_return"))
    sample = to_number(row.get("sample_size"))
    if any(math.isnan(x) for x in [win, avg, median, sample]):
        return -999.0
    if sample < 10:
        return -100.0 + sample
    score = median * 2.0 + avg + max(0.0, win - 50.0) * 0.35 + min(math.log10(max(sample, 1.0)), 2.0)
    if row.get("confidence_status") == "low":
        score *= 0.45
    elif row.get("confidence_status") == "medium":
        score *= 0.75
    if not boolish(row.get("out_of_sample_pass")):
        score -= 2.0
    return round(float(score), 4)


def metric_row(
    part: pd.DataFrame,
    tdcc_list_type: str,
    rank_bucket: str,
    trigger_id: str,
    confluence_scope: str,
    confluence_id: str,
    confluence_name_zh: str,
    generated_at: str,
    data_start: str,
    data_end: str,
    split_date: str,
) -> dict[str, Any]:
    returns = pd.to_numeric(part["return_pct"], errors="coerce").dropna()
    mfe = pd.to_numeric(part.get("mfe_pct"), errors="coerce")
    mae = pd.to_numeric(part.get("mae_pct"), errors="coerce")
    holding = pd.to_numeric(part.get("holding_days"), errors="coerce")
    tdcc_rank = pd.to_numeric(part.get("tdcc_rank"), errors="coerce")
    tdcc_score = pd.to_numeric(part.get("tdcc_ranking_score"), errors="coerce")
    tdcc_age = pd.to_numeric(part.get("tdcc_signal_age_days"), errors="coerce")
    oos = part[part["out_of_sample"].map(boolish)]
    oos_returns = pd.to_numeric(oos["return_pct"], errors="coerce").dropna()
    sample_size = int(len(returns))
    out_size = int(len(oos_returns))
    row_pass = out_of_sample_pass(part)
    trigger = TRIGGER_MAP.get(trigger_id)
    row: dict[str, Any] = {
        "model_id": MODEL_ID,
        "overlay_model_id": OVERLAY_MODEL_ID,
        "research_id": RESEARCH_ID,
        "tdcc_list_type": tdcc_list_type,
        "tdcc_list_name_zh": ZH.get(tdcc_list_type, tdcc_list_type),
        "rank_bucket": rank_bucket,
        "rank_bucket_name_zh": ZH.get(rank_bucket, rank_bucket),
        "trigger_id": trigger_id,
        "trigger_name_zh": trigger.trigger_name_zh if trigger else trigger_id,
        "confluence_scope": confluence_scope,
        "confluence_scope_zh": ZH.get(confluence_scope, confluence_scope),
        "confluence_id": confluence_id,
        "confluence_name_zh": confluence_name_zh,
        "entry_rule_id": ENTRY_RULE_ID,
        "entry_rule_zh": "確認日收盤後才列入；下一個交易日開盤價進場。",
        "stop_loss_rule_id": STOP_RULE_ID,
        "stop_loss_rule_zh": "持有期間觸及訊號K低點先停損。",
        "exit_rule_id": EXIT_RULE_ID,
        "exit_rule_zh": f"先碰訊號K低點停損，否則持有{MAX_HOLD_DAYS}個交易日收盤出場。",
        "metric_sample_scope": METRIC_SAMPLE_SCOPE,
        "sample_size": sample_size,
        "unique_signal_events": int(part[["signal_date", "stock_id"]].drop_duplicates().shape[0]),
        "unique_confirmation_events": int(part[["confirmation_date", "stock_id", "trigger_id"]].drop_duplicates().shape[0]),
        "unique_stocks": int(part["stock_id"].astype(str).nunique()),
        "win_rate": pct_round((returns > 0).mean() * 100 if sample_size else math.nan, 2),
        "avg_return": pct_round(returns.mean() if sample_size else math.nan),
        "median_return": pct_round(returns.median() if sample_size else math.nan),
        "max_drawdown": pct_round(mae.min()),
        "avg_mfe": pct_round(mfe.mean()),
        "avg_mae": pct_round(mae.mean()),
        "avg_holding_days": pct_round(holding.mean(), 2),
        "profit_factor": profit_factor(returns),
        "avg_tdcc_rank": pct_round(tdcc_rank.mean(), 2),
        "avg_tdcc_ranking_score": pct_round(tdcc_score.mean()),
        "avg_tdcc_signal_age_days": pct_round(tdcc_age.mean(), 2),
        "out_of_sample_size": out_size,
        "out_of_sample_win_rate": pct_round((oos_returns > 0).mean() * 100 if out_size else math.nan, 2),
        "out_of_sample_avg_return": pct_round(oos_returns.mean() if out_size else math.nan),
        "out_of_sample_median_return": pct_round(oos_returns.median() if out_size else math.nan),
        "out_of_sample_pass": row_pass,
        "approved_for_daily": False,
        "risk_notes_zh": "research only; entry uses confirmation next open; tdcc overlay uses confirmation-date as-of data; approved_for_daily remains False",
        "generated_at": generated_at,
        "data_start_date": data_start,
        "data_end_date": data_end,
        "out_of_sample_start_date": split_date,
    }
    row["confidence_status"] = confidence_status(sample_size, out_size, row_pass)
    row["ranking_research_score"] = ranking_score(row)
    row["ranking_research_rank"] = ""
    return row


def scoped_parts(events: pd.DataFrame) -> list[tuple[str, str, str, pd.DataFrame]]:
    parts: list[tuple[str, str, str, pd.DataFrame]] = []
    parts.append(("operation_trigger", "all_confirmed_volume_breakout", "全部已確認放量攻擊", events))
    for scope, value_col, name_col in DIMENSION_SCOPES:
        if value_col not in events.columns:
            continue
        for value, part in events.groupby(value_col, dropna=False):
            value = safe_str(value) or "unknown"
            name = safe_str(part[name_col].iloc[0]) if name_col in part.columns else value
            parts.append((scope, value, name, part))
    if {"attack_method", "price_position_type"}.issubset(events.columns):
        combo = events.copy()
        combo["attack_position_id"] = combo["attack_method"].map(safe_str) + "__" + combo["price_position_type"].map(safe_str)
        combo["attack_position_name_zh"] = combo["attack_method_name_zh"].map(safe_str) + " + " + combo["price_position_name_zh"].map(safe_str)
        for value, part in combo.groupby("attack_position_id", dropna=False):
            parts.append(("operation_attack_position", safe_str(value), safe_str(part["attack_position_name_zh"].iloc[0]), part))
    return parts


def summarize(events: pd.DataFrame) -> pd.DataFrame:
    if events.empty:
        return pd.DataFrame(columns=SUMMARY_COLUMNS)
    generated_at = now_text()
    data_start = safe_str(events["confirmation_date"].min())
    data_end = safe_str(events["confirmation_date"].max())
    split_date = out_of_sample_start_date(events, "confirmation_date")
    rows: list[dict[str, Any]] = []
    for tdcc_list_type, list_part in events.groupby("tdcc_list_type", dropna=False):
        if safe_str(tdcc_list_type) == "no_tdcc":
            bucket_parts = [("all", list_part)]
        else:
            rank = pd.to_numeric(list_part["tdcc_rank"], errors="coerce")
            bucket_parts = [
                ("top_10", list_part[rank <= 10]),
                ("top_20", list_part[rank <= 20]),
                ("top_50", list_part[rank <= 50]),
            ]
        for rank_bucket, bucket_part in bucket_parts:
            if bucket_part.empty:
                continue
            for trigger_id, trigger_part in bucket_part.groupby("trigger_id", dropna=False):
                for scope, confluence_id, confluence_name, part in scoped_parts(trigger_part):
                    if part.empty:
                        continue
                    rows.append(
                        metric_row(
                            part,
                            safe_str(tdcc_list_type),
                            rank_bucket,
                            safe_str(trigger_id),
                            scope,
                            confluence_id,
                            confluence_name,
                            generated_at,
                            data_start,
                            data_end,
                            split_date,
                        )
                    )
    out = pd.DataFrame(rows)
    if out.empty:
        return pd.DataFrame(columns=SUMMARY_COLUMNS)
    out = ensure_columns(out, SUMMARY_COLUMNS)
    out["_score"] = pd.to_numeric(out["ranking_research_score"], errors="coerce").fillna(-999)
    out["_sample"] = pd.to_numeric(out["sample_size"], errors="coerce").fillna(0)
    out = out.sort_values(
        ["tdcc_list_type", "rank_bucket", "_score", "_sample"],
        ascending=[True, True, False, False],
    ).reset_index(drop=True)
    out["ranking_research_rank"] = out.groupby(["tdcc_list_type", "rank_bucket"]).cumcount() + 1
    return out.drop(columns=["_score", "_sample"])[SUMMARY_COLUMNS]


def active_signal_candidates(price: pd.DataFrame, latest_date: str) -> list[tuple[int, pd.Series]]:
    if price.empty:
        return []
    latest_positions = price.index[price["date"].map(normalize_date).eq(latest_date)].tolist()
    if not latest_positions:
        return []
    latest_idx = int(latest_positions[-1])
    model_mask = formal_model_hit_mask(price)
    out: list[tuple[int, pd.Series]] = []
    for signal_idx in [int(idx) for idx in model_mask[model_mask].index]:
        if signal_idx >= latest_idx:
            continue
        if latest_idx - signal_idx > MAX_CONFIRM_DAYS:
            continue
        out.append((signal_idx, price.iloc[signal_idx]))
    return out


def process_latest_path(path: Path, latest_date: str, market_regimes: dict[str, str]) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    rank_rows: list[dict[str, Any]] = []
    pending_rows: list[dict[str, Any]] = []
    raw = load_price_csv(path)
    if raw.empty or len(raw) < 90:
        return rank_rows, pending_rows
    if not {"date", "stock_id", "stock_name", "open", "high", "low", "close", "volume"}.issubset(raw.columns):
        return rank_rows, pending_rows
    first_id = normalize_code(raw.iloc[0].get("stock_id"))
    if not is_equity_stock_id(first_id):
        return rank_rows, pending_rows
    price = add_research_features(raw)
    latest_positions = price.index[price["date"].map(normalize_date).eq(latest_date)].tolist()
    if not latest_positions:
        return rank_rows, pending_rows
    latest_idx = int(latest_positions[-1])
    for signal_idx, signal in active_signal_candidates(price, latest_date):
        confirmed_today: list[str] = []
        for spec in TRIGGERS:
            confirmation = find_confirmation(price, signal_idx, spec)
            if confirmation is None:
                continue
            confirmation_idx = int(confirmation["confirmation_idx"])
            if confirmation_idx == latest_idx:
                base = event_payload(price, signal_idx, confirmation_idx, market_regimes)
                signal_low = safe_price(signal.get("low"))
                row = {
                    **base,
                    "latest_price_date": latest_date,
                    "trigger_id": spec.trigger_id,
                    "trigger_name_zh": spec.trigger_name_zh,
                    "confirmation_rule_zh": spec.confirmation_rule_zh,
                    "stop_loss_rule_id": STOP_RULE_ID,
                    "stop_loss_level": round(signal_low, 4) if not math.isnan(signal_low) else "",
                    "exit_rule_id": EXIT_RULE_ID,
                    "approved_for_daily": False,
                }
                rank_rows.append(row)
                confirmed_today.append(spec.trigger_id)
        signal_low = safe_price(signal.get("low"))
        broken = signal_low_broken(price, signal_idx, latest_idx, signal_low)
        signal_age = latest_idx - signal_idx
        if confirmed_today or broken or signal_age > MAX_CONFIRM_DAYS:
            continue
        pending = event_payload(price, signal_idx, latest_idx, market_regimes)
        pending_rows.append(
            {
                "queue_date": latest_date,
                "model_id": MODEL_ID,
                "research_id": RESEARCH_ID,
                "signal_date": normalize_date(signal.get("date")),
                "signal_age_trading_days": signal_age,
                "stock_id": normalize_stock_id(signal.get("stock_id")),
                "stock_name": safe_str(signal.get("stock_name")),
                "market": safe_str(signal.get("market")),
                "pending_trigger_ids": "|".join(item.trigger_id for item in TRIGGERS),
                "expired": False,
                "broken_signal_low": broken,
                "stop_loss_level": round(signal_low, 4) if not math.isnan(signal_low) else "",
                "watch_until_trading_date": normalize_date(price.iloc[min(len(price) - 1, signal_idx + MAX_CONFIRM_DAYS)].get("date")),
                "classification_id": pending.get("classification_id", ""),
                "attack_method": pending.get("attack_method", ""),
                "price_position_type": pending.get("price_position_type", ""),
                "approved_for_daily": False,
            }
        )
    return rank_rows, pending_rows


def build_latest_confirmation_frames() -> tuple[pd.DataFrame, pd.DataFrame]:
    latest_date = latest_stock_price_history_date()
    if not latest_date:
        return pd.DataFrame(columns=RANK_COLUMNS), pd.DataFrame(columns=PENDING_COLUMNS)
    market_regimes = load_market_regime_map()
    paths = sorted(PRICE_HISTORY_DIR.glob("*.csv"))
    rank_rows: list[dict[str, Any]] = []
    pending_rows: list[dict[str, Any]] = []
    worker_count = min(12, max(2, os.cpu_count() or 4))
    with ThreadPoolExecutor(max_workers=worker_count) as executor:
        for rank_part, pending_part in executor.map(lambda p: process_latest_path(p, latest_date, market_regimes), paths):
            rank_rows.extend(rank_part)
            pending_rows.extend(pending_part)
    rank_base = add_operation_selection_columns(pd.DataFrame(rank_rows))
    rank_base = formal_operation_events(rank_base)
    if not rank_base.empty:
        rank_base = attach_tdcc_asof(rank_base, read_tdcc_events(), "confirmation_date")
    pending = ensure_columns(pd.DataFrame(pending_rows), PENDING_COLUMNS)
    return rank_base, pending


def applicable_rank_buckets(row: pd.Series) -> list[str]:
    list_type = safe_str(row.get("tdcc_list_type"))
    if list_type == "no_tdcc":
        return ["all"]
    rank = to_number(row.get("tdcc_rank"))
    buckets: list[str] = []
    if not math.isnan(rank):
        if rank <= 10:
            buckets.append("top_10")
        if rank <= 20:
            buckets.append("top_20")
        if rank <= 50:
            buckets.append("top_50")
    return buckets


def evidence_candidates_for_row(row: pd.Series) -> list[tuple[str, str]]:
    out = [
        ("operation_attack_position", f"{safe_str(row.get('attack_method'))}__{safe_str(row.get('price_position_type'))}"),
        ("operation_classification", safe_str(row.get("classification_id"))),
        ("operation_attack_method", safe_str(row.get("attack_method"))),
        ("operation_price_position", safe_str(row.get("price_position_type"))),
        ("operation_trigger", "all_confirmed_volume_breakout"),
    ]
    return [(scope, key) for scope, key in out if key and key != "__"]


def best_evidence(row: pd.Series, summary: pd.DataFrame) -> pd.Series | None:
    if summary.empty:
        return None
    buckets = applicable_rank_buckets(row)
    if not buckets:
        return None
    part = summary[
        summary["tdcc_list_type"].astype(str).eq(safe_str(row.get("tdcc_list_type")))
        & summary["rank_bucket"].astype(str).isin(buckets)
        & summary["trigger_id"].astype(str).eq(safe_str(row.get("trigger_id")))
    ].copy()
    if part.empty:
        return None
    frames: list[pd.DataFrame] = []
    for scope, key in evidence_candidates_for_row(row):
        match = part[
            part["confluence_scope"].astype(str).eq(scope)
            & part["confluence_id"].astype(str).eq(key)
        ].copy()
        if not match.empty:
            match["_scope_order"] = len(frames)
            frames.append(match)
    if not frames:
        return None
    candidates = pd.concat(frames, ignore_index=True, sort=False)
    candidates["_score"] = pd.to_numeric(candidates["ranking_research_score"], errors="coerce").fillna(-999)
    candidates["_sample"] = pd.to_numeric(candidates["sample_size"], errors="coerce").fillna(0)
    candidates = candidates.sort_values(["_score", "_sample"], ascending=[False, False])
    return candidates.iloc[0]


def build_rank_output(rank_base: pd.DataFrame, summary: pd.DataFrame) -> pd.DataFrame:
    if rank_base.empty:
        return pd.DataFrame(columns=RANK_COLUMNS)
    rows: list[dict[str, Any]] = []
    for _, row in rank_base.iterrows():
        evidence = best_evidence(row, summary)
        rows.append(
            {
                "operation_rank": "",
                "model_id": MODEL_ID,
                "overlay_model_id": OVERLAY_MODEL_ID,
                "research_id": RESEARCH_ID,
                "latest_price_date": safe_str(row.get("latest_price_date")),
                "signal_date": safe_str(row.get("signal_date")),
                "confirmation_date": safe_str(row.get("confirmation_date")),
                "confirmation_age_trading_days": safe_str(row.get("confirmation_age_trading_days")),
                "stock_id": safe_str(row.get("stock_id")),
                "stock_name": safe_str(row.get("stock_name")),
                "market": safe_str(row.get("market")),
                "trigger_id": safe_str(row.get("trigger_id")),
                "trigger_name_zh": safe_str(row.get("trigger_name_zh")),
                "confirmation_rule_zh": safe_str(row.get("confirmation_rule_zh")),
                "matched_trigger_ids": safe_str(row.get("matched_trigger_ids")),
                "selected_trigger_id": safe_str(row.get("selected_trigger_id")),
                "selected_confirmation_date": safe_str(row.get("selected_confirmation_date")),
                "selected_trigger_priority": safe_str(row.get("selected_trigger_priority")),
                "operation_selection_status": safe_str(row.get("operation_selection_status")),
                "entry_rule_id": ENTRY_RULE_ID,
                "entry_rule_zh": "確認日收盤後列入；下一個交易日開盤價進場。",
                "planned_entry_timing_zh": "下一個交易日開盤",
                "entry_price_status": "next_open_pending",
                "stop_loss_rule_id": STOP_RULE_ID,
                "stop_loss_rule_zh": "跌破訊號K低點停損",
                "stop_loss_level": safe_str(row.get("stop_loss_level")),
                "exit_rule_id": EXIT_RULE_ID,
                "exit_rule_zh": f"先碰訊號K低點停損，否則持有{MAX_HOLD_DAYS}個交易日收盤出場。",
                "tdcc_list_type": safe_str(row.get("tdcc_list_type")),
                "tdcc_signal_date": safe_str(row.get("tdcc_signal_date")),
                "tdcc_signal_age_days": safe_str(row.get("tdcc_signal_age_days")),
                "tdcc_rank": safe_str(row.get("tdcc_rank")),
                "tdcc_ranking_score": safe_str(row.get("tdcc_ranking_score")),
                "classification_id": safe_str(row.get("classification_id")),
                "classification_name_zh": safe_str(row.get("classification_name_zh")),
                "attack_method": safe_str(row.get("attack_method")),
                "attack_method_name_zh": safe_str(row.get("attack_method_name_zh")),
                "price_position_type": safe_str(row.get("price_position_type")),
                "price_position_name_zh": safe_str(row.get("price_position_name_zh")),
                "risk_type": safe_str(row.get("risk_type")),
                "risk_name_zh": safe_str(row.get("risk_name_zh")),
                "evidence_confluence_scope": "" if evidence is None else safe_str(evidence.get("confluence_scope")),
                "evidence_confluence_id": "" if evidence is None else safe_str(evidence.get("confluence_id")),
                "evidence_rank_bucket": "" if evidence is None else safe_str(evidence.get("rank_bucket")),
                "evidence_sample_size": "" if evidence is None else safe_str(evidence.get("sample_size")),
                "evidence_win_rate": "" if evidence is None else safe_str(evidence.get("win_rate")),
                "evidence_avg_return": "" if evidence is None else safe_str(evidence.get("avg_return")),
                "evidence_median_return": "" if evidence is None else safe_str(evidence.get("median_return")),
                "evidence_confidence_status": "" if evidence is None else safe_str(evidence.get("confidence_status")),
                "evidence_out_of_sample_pass": "" if evidence is None else safe_str(evidence.get("out_of_sample_pass")),
                "ranking_research_score": -999.0 if evidence is None else to_number(evidence.get("ranking_research_score"), -999.0),
                "approved_for_daily": False,
            }
        )
    out = ensure_columns(pd.DataFrame(rows), RANK_COLUMNS)
    out["_score"] = pd.to_numeric(out["ranking_research_score"], errors="coerce").fillna(-999)
    out["_tdcc_rank"] = pd.to_numeric(out["tdcc_rank"], errors="coerce").fillna(999999)
    out = out.sort_values(["_score", "_tdcc_rank", "stock_id"], ascending=[False, True, True])
    out = out.drop_duplicates(["confirmation_date", "stock_id"], keep="first").reset_index(drop=True)
    out["operation_rank"] = range(1, len(out) + 1)
    return out.drop(columns=["_score", "_tdcc_rank"])[RANK_COLUMNS]


def markdown_table(df: pd.DataFrame, columns: list[str], limit: int) -> list[str]:
    if df.empty:
        return ["_No rows._"]
    lines = ["| " + " | ".join(columns) + " |", "| " + " | ".join(["---"] * len(columns)) + " |"]
    for _, row in df.head(limit).iterrows():
        values = [safe_str(row.get(col)).replace("|", "/").replace("\n", " ")[:160] for col in columns]
        lines.append("| " + " | ".join(values) + " |")
    return lines


def write_summary_markdown(summary: pd.DataFrame, events: pd.DataFrame) -> None:
    best = summary.copy()
    if not best.empty:
        best["_sample"] = pd.to_numeric(best["sample_size"], errors="coerce").fillna(0)
        best["_score"] = pd.to_numeric(best["ranking_research_score"], errors="coerce").fillna(-999)
        best = best[best["_sample"] >= 10].sort_values(["_score", "_sample"], ascending=[False, False]).drop(columns=["_sample", "_score"])
    counts = (
        events.groupby(["tdcc_list_type", "trigger_id"], dropna=False)
        .agg(event_rows=("stock_id", "size"), unique_confirmations=("confirmation_date", lambda s: events.loc[s.index, ["confirmation_date", "stock_id", "trigger_id"]].drop_duplicates().shape[0]))
        .reset_index()
    ) if not events.empty else pd.DataFrame()
    lines = [
        "# Volume Breakout Confirmed Operation Backtest",
        "",
        f"- generated_at: `{now_text()}`",
        f"- model_id: `{MODEL_ID}`",
        f"- entry_rule: `{ENTRY_RULE_ID}`",
        f"- stop_exit_rule: `{EXIT_RULE_ID}`",
        f"- tdcc_as_of_rule: `tdcc_signal_date <= confirmation_date and tdcc_signal_age_days <= {MAX_TDCC_SIGNAL_AGE_DAYS}`",
        f"- event_rows: `{len(events)}`",
        f"- summary_rows: `{len(summary)}`",
        "- scope: research only; all rows keep `approved_for_daily=False`.",
        "",
        "## Event Counts",
        "",
        *markdown_table(counts, ["tdcc_list_type", "trigger_id", "event_rows", "unique_confirmations"], 40),
        "",
        "## Best Rows",
        "",
        *markdown_table(
            best,
            [
                "tdcc_list_type",
                "rank_bucket",
                "trigger_id",
                "confluence_scope",
                "confluence_id",
                "sample_size",
                "win_rate",
                "avg_return",
                "median_return",
                "confidence_status",
                "out_of_sample_pass",
                "ranking_research_score",
                "ranking_research_rank",
            ],
            80,
        ),
    ]
    LATEST_SUMMARY_MD.write_text("\n".join(lines) + "\n", encoding="utf-8", newline="\n")


def write_rank_markdown(rank: pd.DataFrame, pending: pd.DataFrame) -> None:
    lines = [
        "# Volume Breakout Confirmed Operation Rank",
        "",
        f"- generated_at: `{now_text()}`",
        f"- latest_price_date: `{latest_stock_price_history_date()}`",
        "- rank_rule: only confirmation rows with `confirmation_date == latest_price_date` appear here.",
        "- entry_rule: confirmation after close, next trading day open.",
        "- scope: research only; all rows keep `approved_for_daily=False`.",
        "",
        "## Confirmed Rank",
        "",
        *markdown_table(
            rank,
            [
                "operation_rank",
                "stock_id",
                "stock_name",
                "trigger_id",
                "tdcc_list_type",
                "tdcc_rank",
                "classification_id",
                "attack_method",
                "price_position_type",
                "evidence_sample_size",
                "evidence_win_rate",
                "evidence_avg_return",
                "evidence_median_return",
                "ranking_research_score",
            ],
            80,
        ),
        "",
        "## Pending Queue",
        "",
        *markdown_table(
            pending,
            [
                "queue_date",
                "signal_date",
                "signal_age_trading_days",
                "stock_id",
                "stock_name",
                "pending_trigger_ids",
                "classification_id",
                "attack_method",
                "price_position_type",
            ],
            80,
        ),
    ]
    LATEST_RANK_MD.write_text("\n".join(lines) + "\n", encoding="utf-8", newline="\n")

    pending_lines = [
        "# Volume Breakout Pending Operation Queue",
        "",
        f"- generated_at: `{now_text()}`",
        f"- queue_date: `{latest_stock_price_history_date()}`",
        "- pending rows are not ranked operation rows; they are waiting for confirmation.",
        "- scope: research only; all rows keep `approved_for_daily=False`.",
        "",
        *markdown_table(
            pending,
            [
                "queue_date",
                "signal_date",
                "signal_age_trading_days",
                "stock_id",
                "stock_name",
                "pending_trigger_ids",
                "classification_id",
                "attack_method",
                "price_position_type",
            ],
            120,
        ),
    ]
    LATEST_PENDING_MD.write_text("\n".join(pending_lines) + "\n", encoding="utf-8", newline="\n")


def write_formal_summary_markdown(summary: pd.DataFrame, events: pd.DataFrame, lifecycle: pd.DataFrame) -> None:
    state_counts = (
        lifecycle.groupby(["operation_lifecycle_state", "sample_maturity_status"], dropna=False)
        .agg(signal_events=("stock_id", "size"), mature_samples=("mature_sample_eligible", lambda s: int(pd.Series(s).map(boolish).sum())))
        .reset_index()
    ) if not lifecycle.empty else pd.DataFrame()
    lines = [
        "# Volume Breakout Formal Operation Backtest",
        "",
        f"- generated_at: `{now_text()}`",
        f"- model_id: `{MODEL_ID}`",
        "- purpose: one signal produces one formal operation event.",
        f"- lifecycle_definition: `{LIFECYCLE_DEFINITION_ID}`",
        f"- metric_sample_scope: `{METRIC_SAMPLE_SCOPE}`",
        "- trigger_selection_rule: earliest confirmation date wins; if multiple triggers confirm on the same date, use trigger priority order.",
        "- trigger_priority: `next_day_continuation_confirmed`, `pullback_5ma_confirmed`, `pullback_10ma_confirmed`.",
        "- research note: multi-trigger events remain in `volume_breakout_confirmed_operation_events.csv`; this formal artifact is the production-operation statistics source.",
        f"- formal_event_rows: `{len(events)}`",
        f"- lifecycle_event_rows: `{len(lifecycle)}`",
        "",
        "## Lifecycle State Counts",
        "",
        *markdown_table(
            state_counts,
            [
                "operation_lifecycle_state",
                "sample_maturity_status",
                "signal_events",
                "mature_samples",
            ],
            20,
        ),
        "",
    ]
    if not summary.empty:
        lines.extend(
            markdown_table(
                summary,
                [
                    "tdcc_list_type",
                    "rank_bucket",
                    "trigger_id",
                    "confluence_scope",
                    "confluence_id",
                    "metric_sample_scope",
                    "sample_size",
                    "win_rate",
                    "median_return",
                    "out_of_sample_pass",
                    "confidence_status",
                    "ranking_research_score",
                ],
                80,
            )
        )
    else:
        lines.append("_No formal summary rows._")
    LATEST_FORMAL_SUMMARY_MD.write_text("\n".join(lines) + "\n", encoding="utf-8", newline="\n")


def main() -> int:
    formal_lifecycle = build_lifecycle_events()
    events = apply_lifecycle_state_columns(build_base_events(), formal_lifecycle)
    summary = summarize(events)
    formal_events = formal_operation_events(events)
    formal_summary = summarize(formal_events)
    rank_base, pending = build_latest_confirmation_frames()
    rank = build_rank_output(rank_base, formal_summary if not formal_summary.empty else summary)

    write_csv(events, HISTORY_EVENTS_CSV)
    write_csv(formal_events, HISTORY_FORMAL_EVENTS_CSV)
    write_csv(formal_lifecycle, HISTORY_FORMAL_LIFECYCLE_CSV)
    write_csv(formal_lifecycle, LATEST_FORMAL_LIFECYCLE_CSV)
    write_csv(summary, HISTORY_SUMMARY_CSV)
    write_csv(summary, LATEST_SUMMARY_CSV)
    write_csv(formal_summary, LATEST_FORMAL_SUMMARY_CSV)
    write_csv(rank, LATEST_RANK_CSV)
    write_csv(pending, LATEST_PENDING_CSV)
    write_summary_markdown(summary, events)
    write_formal_summary_markdown(formal_summary, formal_events, formal_lifecycle)
    write_rank_markdown(rank, pending)

    print(f"Saved: {LATEST_SUMMARY_CSV} rows={len(summary)}")
    print(f"Saved: {HISTORY_EVENTS_CSV} rows={len(events)}")
    print(f"Saved: {LATEST_FORMAL_SUMMARY_CSV} rows={len(formal_summary)}")
    print(f"Saved: {HISTORY_FORMAL_EVENTS_CSV} rows={len(formal_events)}")
    print(f"Saved: {LATEST_FORMAL_LIFECYCLE_CSV} rows={len(formal_lifecycle)}")
    print(f"Saved: {LATEST_RANK_CSV} rows={len(rank)}")
    print(f"Saved: {LATEST_PENDING_CSV} rows={len(pending)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
