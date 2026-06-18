from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Any
import math

import pandas as pd


ROOT = Path(__file__).resolve().parents[1]
MARKET_INDEX_HISTORY = ROOT / "data" / "market_index_history.csv"
TDCC_EVENTS_CSV = ROOT / "output" / "history" / "research" / "tdcc_weekly_ranking_backtest_events.csv"

MODEL_ID = "volume_range_breakout"
OVERLAY_MODEL_ID = "tdcc_weekly_ranking_formula"
RESEARCH_ID = "volume_breakout_confirmed_operation"
ENTRY_RULE_ID = "confirmation_next_open"
STOP_RULE_ID = "signal_low_stop"
EXIT_RULE_ID = "signal_low_stop_or_fixed_10d_close"
LIFECYCLE_DEFINITION_ID = "daily_volume_breakout_operation_lifecycle_v1"
MAX_CONFIRM_DAYS = 10
MAX_HOLD_DAYS = 10
MAX_TDCC_SIGNAL_AGE_DAYS = 7


@dataclass(frozen=True)
class TriggerSpec:
    trigger_id: str
    trigger_name_zh: str
    confirmation_rule_zh: str
    max_confirm_days: int
    ma_col: str = ""


TRIGGERS = [
    TriggerSpec(
        "pullback_5ma_confirmed",
        "pullback_5ma_confirmed",
        "Confirm when price pulls back to 5MA and closes back above 5MA before breaking signal-date low.",
        MAX_CONFIRM_DAYS,
        ma_col="ma5",
    ),
    TriggerSpec(
        "next_day_break_signal_high_confirmed",
        "next_day_break_signal_high_confirmed",
        "Confirm on D+1 when intraday high breaks signal-date high and close remains above signal-date close.",
        1,
    ),
    TriggerSpec(
        "next_day_continuation_confirmed",
        "next_day_continuation_confirmed",
        "Confirm on D+1 when close is above signal-date close and at or above signal-date high.",
        1,
    ),
    TriggerSpec(
        "pullback_10ma_confirmed",
        "pullback_10ma_confirmed",
        "Confirm when price pulls back to 10MA and closes back above 10MA before breaking signal-date low.",
        MAX_CONFIRM_DAYS,
        ma_col="ma10",
    ),
]
TRIGGER_MAP = {item.trigger_id: item for item in TRIGGERS}
TRIGGER_PRIORITY = {item.trigger_id: index + 1 for index, item in enumerate(TRIGGERS)}
TRIGGER_ZH = {item.trigger_id: item.trigger_name_zh for item in TRIGGERS}

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
    "entry_rule_id",
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


def safe_str(value: Any) -> str:
    if value is None:
        return ""
    try:
        if pd.isna(value):
            return ""
    except Exception:
        pass
    text = str(value).replace("\ufeff", "").strip()
    if text.lower() in {"nan", "none", "nat", "<na>"}:
        return ""
    return text


def safe_float(value: Any, default: float = math.nan) -> float:
    text = safe_str(value).replace(",", "").replace("%", "")
    if not text:
        return default
    try:
        return float(text)
    except Exception:
        return default


def boolish(value: Any) -> bool:
    return safe_str(value).lower() in {"true", "1", "1.0", "yes", "y", "t"}


def normalize_date(value: Any) -> str:
    digits = "".join(ch for ch in safe_str(value) if ch.isdigit())
    if len(digits) >= 8 and digits.startswith("20"):
        return digits[:8]
    return ""


def normalize_stock_id(value: Any) -> str:
    text = safe_str(value)
    if text.endswith(".0"):
        text = text[:-2]
    return text.zfill(4) if text.isdigit() and len(text) < 4 else text


def read_csv(path: Path) -> pd.DataFrame:
    if not path.exists():
        return pd.DataFrame()
    try:
        return pd.read_csv(path, dtype=str, keep_default_na=False)
    except Exception:
        return pd.DataFrame()


def ensure_numeric(df: pd.DataFrame, columns: list[str]) -> pd.DataFrame:
    out = df.copy()
    for col in columns:
        if col in out.columns:
            out[col] = pd.to_numeric(out[col], errors="coerce")
    return out


def numeric_series(df: pd.DataFrame, col: str) -> pd.Series:
    if col not in df.columns:
        return pd.Series([math.nan] * len(df), index=df.index, dtype="float64")
    return pd.to_numeric(df[col], errors="coerce")


def add_price_metrics(df: pd.DataFrame) -> pd.DataFrame:
    out = df.copy()
    out["date"] = out["date"].map(normalize_date)
    out = out[out["date"] != ""].sort_values("date").reset_index(drop=True)
    out = ensure_numeric(
        out,
        ["open", "high", "low", "close", "volume", "ma5", "ma10", "ma20", "ma60", "ema23", "volume_ma20"],
    )
    for window, col in [(5, "ma5"), (10, "ma10"), (20, "ma20"), (60, "ma60")]:
        if col not in out.columns or out[col].isna().all():
            out[col] = out["close"].rolling(window, min_periods=window).mean()
    if "ema23" not in out.columns or out["ema23"].isna().all():
        out["ema23"] = out["close"].ewm(span=23, adjust=False, min_periods=23).mean()
    if "volume_ma20" not in out.columns or out["volume_ma20"].isna().all():
        out["volume_ma20"] = out["volume"].rolling(20, min_periods=20).mean()
    out["volume_ratio_calc"] = out["volume"] / out["volume_ma20"].replace(0, pd.NA)
    if "volume_ratio" not in out.columns:
        out["volume_ratio"] = out["volume_ratio_calc"]
    else:
        out["volume_ratio"] = pd.to_numeric(out["volume_ratio"], errors="coerce").fillna(out["volume_ratio_calc"])
    for days in [1, 5, 20, 60]:
        out[f"return_{days}d_calc"] = (out["close"] / out["close"].shift(days) - 1.0) * 100.0
        col = f"return_{days}d"
        if col not in out.columns:
            out[col] = out[f"return_{days}d_calc"]
        else:
            out[col] = pd.to_numeric(out[col], errors="coerce").fillna(out[f"return_{days}d_calc"])
    out["previous_20d_high_calc"] = out["high"].shift(1).rolling(20, min_periods=20).max()
    out["previous_60d_high_calc"] = out["high"].shift(1).rolling(60, min_periods=60).max()
    out["previous_20d_low_calc"] = out["low"].shift(1).rolling(20, min_periods=20).min()
    out["previous_60d_low_calc"] = out["low"].shift(1).rolling(60, min_periods=60).min()
    out["previous_close_calc"] = out["close"].shift(1)
    out["close_position_in_range"] = (out["close"] - out["low"]) / (out["high"] - out["low"]).replace(0, pd.NA)
    out["upper_shadow_pct"] = (out["high"] - out[["close", "open"]].max(axis=1)) / out["close"].replace(0, pd.NA) * 100.0
    out["daily_return_calc"] = (out["close"] / out["close"].shift(1) - 1.0) * 100.0
    return out


def add_research_features(df: pd.DataFrame) -> pd.DataFrame:
    out = add_price_metrics(df)
    high = numeric_series(out, "high")
    low = numeric_series(out, "low")
    close = numeric_series(out, "close")
    prev_close = numeric_series(out, "previous_close_calc")
    volume_ratio = numeric_series(out, "volume_ratio")

    out["previous_40d_high_calc"] = high.shift(1).rolling(40, min_periods=40).max()
    out["previous_40d_low_calc"] = low.shift(1).rolling(40, min_periods=40).min()
    for window in [20, 40, 60]:
        hi = numeric_series(out, f"previous_{window}d_high_calc")
        lo = numeric_series(out, f"previous_{window}d_low_calc")
        out[f"range_width_{window}_pct"] = (hi - lo) / lo.replace(0, pd.NA) * 100.0
    hi60 = numeric_series(out, "previous_60d_high_calc")
    lo60 = numeric_series(out, "previous_60d_low_calc")
    out["low_position_60_pct"] = (close - lo60) / (hi60 - lo60).replace(0, pd.NA) * 100.0
    out["signal_return_1d_pct"] = (close / prev_close.replace(0, pd.NA) - 1.0) * 100.0
    one_price_or_close_high = high.eq(low) | (out["close_position_in_range"] >= 0.9)
    out["limit_up_like"] = (
        (out["signal_return_1d_pct"] >= 9.0)
        & one_price_or_close_high
        & (close >= numeric_series(out, "previous_20d_high_calc") * 1.02)
    )
    out["volume_ratio_bucket"] = pd.cut(
        volume_ratio,
        bins=[-math.inf, 1.0, 1.5, 2.0, 3.0, math.inf],
        labels=["lt_1", "1_1p5", "1p5_2", "2_3", "ge_3"],
    ).astype(str)
    return out


def classify_market_regime(row: pd.Series) -> str:
    above_ma20 = boolish(row.get("above_ma20"))
    above_ma60 = boolish(row.get("above_ma60"))
    ret20 = safe_float(row.get("return_20d"))
    if above_ma20 and above_ma60 and not math.isnan(ret20) and ret20 >= 3:
        return "strong_bull"
    if above_ma20 and above_ma60:
        return "mild_bull"
    if not above_ma20 and not math.isnan(ret20) and ret20 <= -3:
        return "correction"
    return "range_or_mixed"


def load_market_regime_map() -> dict[str, str]:
    df = read_csv(MARKET_INDEX_HISTORY)
    if df.empty or "date" not in df.columns:
        return {}
    if "index_code" in df.columns:
        twse = df[df["index_code"].map(safe_str).eq("TWSE")].copy()
        if not twse.empty:
            df = twse
    df["date"] = df["date"].map(normalize_date)
    df = df[df["date"] != ""].sort_values("date")
    return {safe_str(row.get("date")): classify_market_regime(row) for _, row in df.iterrows()}


def pct_round(value: Any, digits: int = 4) -> float | str:
    num = safe_float(value)
    if math.isnan(num):
        return ""
    return round(num, digits)


def safe_price(value: Any) -> float:
    num = safe_float(value)
    return num if not math.isnan(num) and num > 0 else math.nan


def trigger_priority(trigger_id: Any) -> int:
    return TRIGGER_PRIORITY.get(safe_str(trigger_id), 999)


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
    if any(math.isnan(value) for value in [signal_close, signal_high, signal_low]):
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
            if any(math.isnan(value) for value in [ma, low, close]):
                continue
            if low <= ma and close >= ma:
                return {"confirmation_idx": confirm_idx}
    return None


def confirmation_matches(
    price: pd.DataFrame,
    signal_idx: int,
    through_idx: int | None = None,
) -> list[dict[str, Any]]:
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
                "trigger_zh": spec.trigger_name_zh,
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
    if any(math.isnan(value) for value in [signal_low, entry_price]):
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
    state_zh = "expired"
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
            state_zh = "confirmed_operation"
            terminal_reason = "confirmation_on_asof_date"
        elif entry_idx < len(price) and latest_idx >= entry_idx:
            stopped_idx = stop_hit_index(price, entry_idx, latest_idx, signal_low)
            if stopped_idx is None and planned_exit_idx is not None and latest_idx <= planned_exit_idx:
                state = "active_operation"
                state_zh = "active_operation"
                terminal_reason = "within_d0_d10_hold_window"
            else:
                state = "expired"
                state_zh = "expired"
                terminal_reason = "stop_or_fixed_hold_window_finished"
        else:
            state = "confirmed_operation"
            state_zh = "confirmed_operation"
            terminal_reason = "confirmed_waiting_next_open"
    else:
        signal_age = latest_idx - signal_idx
        broken = signal_low_broken(price, signal_idx, latest_idx, signal_low)
        if signal_age <= MAX_CONFIRM_DAYS and not broken:
            state = "pending_confirmation"
            state_zh = "pending_confirmation"
            terminal_reason = "within_confirmation_window"
            maturity_status = "pending_confirmation"
        else:
            state = "expired"
            state_zh = "expired"
            terminal_reason = "signal_low_broken_before_confirmation" if broken else "confirmation_window_expired"
            maturity_status = "expired_unconfirmed"

    return {
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


def classify_event(row: pd.Series) -> dict[str, str]:
    volume_ratio = safe_float(row.get("volume_ratio"))
    width40 = safe_float(row.get("range_width_40_pct"))
    low_pos60 = safe_float(row.get("low_position_60_pct"))
    limit_up_like = boolish(row.get("limit_up_like"))

    if math.isnan(width40):
        consolidation_type = "unknown_consolidation"
    elif width40 <= 25:
        consolidation_type = "long_consolidation"
    elif width40 <= 40:
        consolidation_type = "short_consolidation"
    else:
        consolidation_type = "non_consolidation"

    if math.isnan(low_pos60):
        price_position_type = "unknown_position"
    elif low_pos60 <= 60:
        price_position_type = "low_position"
    elif low_pos60 >= 80:
        price_position_type = "high_position"
    else:
        price_position_type = "middle_position"

    if limit_up_like:
        attack_method = "locked_limit_up"
    elif not math.isnan(volume_ratio) and volume_ratio >= 3:
        attack_method = "volume_attack"
    else:
        attack_method = "general_breakout"

    if limit_up_like:
        classification_id = "locked_limit_up_breakout"
    elif not math.isnan(width40) and not math.isnan(low_pos60) and width40 <= 25 and low_pos60 <= 60:
        classification_id = "long_base_low_position"
    elif not math.isnan(low_pos60) and low_pos60 <= 60:
        classification_id = "low_position_breakout"
    elif not math.isnan(low_pos60) and low_pos60 >= 80:
        classification_id = "high_position_breakout"
    elif not math.isnan(width40) and width40 > 25:
        classification_id = "wide_range_breakout"
    else:
        classification_id = "standard_breakout"

    return {
        "classification_id": classification_id,
        "classification_name_zh": classification_id,
        "attack_method": attack_method,
        "attack_method_name_zh": attack_method,
        "price_position_type": price_position_type,
        "price_position_name_zh": price_position_type,
        "follow_through_type": "not_evaluated",
        "follow_through_name_zh": "not_evaluated",
        "risk_type": "normal_risk",
        "risk_name_zh": "normal_risk",
        "candle_quality": "not_evaluated",
        "candle_quality_name_zh": "not_evaluated",
        "consolidation_type": consolidation_type,
        "consolidation_name_zh": consolidation_type,
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
    return out


def event_payload(price: pd.DataFrame, signal_idx: int, confirmation_idx: int, market_regimes: dict[str, str]) -> dict[str, Any]:
    signal = price.iloc[signal_idx]
    confirmation = price.iloc[confirmation_idx]
    signal_date = normalize_date(signal.get("date"))
    base: dict[str, Any] = {
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
    class_context.update(classify_event(pd.Series(class_context)))
    return {**base, **class_context}


def ensure_columns(df: pd.DataFrame, columns: list[str]) -> pd.DataFrame:
    out = df.copy()
    for col in columns:
        if col not in out.columns:
            out[col] = ""
    return out[columns]


def read_tdcc_events() -> pd.DataFrame:
    tdcc = read_csv(TDCC_EVENTS_CSV)
    if tdcc.empty:
        return tdcc
    if "stock_id" in tdcc.columns:
        tdcc["stock_id"] = tdcc["stock_id"].map(normalize_stock_id)
    if "signal_date" in tdcc.columns:
        tdcc["signal_date"] = tdcc["signal_date"].map(normalize_date)
    tdcc = tdcc[tdcc.get("model_id", "").astype(str).eq(OVERLAY_MODEL_ID)].copy()
    return tdcc[(tdcc.get("stock_id", "") != "") & (tdcc.get("signal_date", "") != "")]


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
        return ensure_columns(base, EVENT_COLUMNS)

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


def rank_buckets_for_row(row: pd.Series) -> list[str]:
    list_type = safe_str(row.get("tdcc_list_type"))
    if list_type == "no_tdcc":
        return ["all"]
    rank = safe_float(row.get("tdcc_rank"))
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
    buckets = rank_buckets_for_row(row)
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
