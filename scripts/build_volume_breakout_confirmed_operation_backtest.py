from __future__ import annotations

from concurrent.futures import ThreadPoolExecutor
from dataclasses import dataclass
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


ROOT = Path(".")
LATEST_DIR = ROOT / "output" / "latest"
RESEARCH_HISTORY_DIR = ROOT / "output" / "history" / "research"
TDCC_EVENTS_CSV = RESEARCH_HISTORY_DIR / "tdcc_weekly_ranking_backtest_events.csv"

LATEST_SUMMARY_CSV = LATEST_DIR / "volume_breakout_confirmed_operation_backtest_latest.csv"
LATEST_SUMMARY_MD = LATEST_DIR / "volume_breakout_confirmed_operation_backtest_latest.md"
HISTORY_SUMMARY_CSV = RESEARCH_HISTORY_DIR / "volume_breakout_confirmed_operation_backtest.csv"
HISTORY_EVENTS_CSV = RESEARCH_HISTORY_DIR / "volume_breakout_confirmed_operation_events.csv"
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


@dataclass(frozen=True)
class TriggerSpec:
    trigger_id: str
    trigger_name_zh: str
    confirmation_rule_zh: str
    max_confirm_days: int
    ma_col: str = ""


TRIGGERS = [
    TriggerSpec(
        "next_day_continuation_confirmed",
        ZH["next_day_continuation_confirmed"],
        "訊號後第1個交易日收盤價高於訊號收盤，且收盤不低於訊號高點；確認前不得跌破訊號低點。",
        1,
    ),
    TriggerSpec(
        "pullback_5ma_confirmed",
        ZH["pullback_5ma_confirmed"],
        "訊號後10個交易日內首次回測5MA且收盤站回5MA；確認前不得跌破訊號低點。",
        MAX_CONFIRM_DAYS,
        ma_col="ma5",
    ),
    TriggerSpec(
        "pullback_10ma_confirmed",
        ZH["pullback_10ma_confirmed"],
        "訊號後10個交易日內首次回測10MA且收盤站回10MA；確認前不得跌破訊號低點。",
        MAX_CONFIRM_DAYS,
        ma_col="ma10",
    ),
]
TRIGGER_MAP = {item.trigger_id: item for item in TRIGGERS}

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
                    **trade,
                }
            )
            rows.append(payload)
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
    events = attach_tdcc_asof(events, read_tdcc_events(), "confirmation_date")
    return ensure_columns(events, EVENT_COLUMNS).sort_values(
        ["confirmation_date", "stock_id", "trigger_id", "tdcc_list_type"]
    ).reset_index(drop=True)


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
    rank_base = pd.DataFrame(rank_rows)
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
    out = out.drop_duplicates(["confirmation_date", "stock_id", "trigger_id"], keep="first").reset_index(drop=True)
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


def main() -> int:
    events = build_base_events()
    summary = summarize(events)
    rank_base, pending = build_latest_confirmation_frames()
    rank = build_rank_output(rank_base, summary)

    write_csv(events, HISTORY_EVENTS_CSV)
    write_csv(summary, HISTORY_SUMMARY_CSV)
    write_csv(summary, LATEST_SUMMARY_CSV)
    write_csv(rank, LATEST_RANK_CSV)
    write_csv(pending, LATEST_PENDING_CSV)
    write_summary_markdown(summary, events)
    write_rank_markdown(rank, pending)

    print(f"Saved: {LATEST_SUMMARY_CSV} rows={len(summary)}")
    print(f"Saved: {HISTORY_EVENTS_CSV} rows={len(events)}")
    print(f"Saved: {LATEST_RANK_CSV} rows={len(rank)}")
    print(f"Saved: {LATEST_PENDING_CSV} rows={len(pending)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
