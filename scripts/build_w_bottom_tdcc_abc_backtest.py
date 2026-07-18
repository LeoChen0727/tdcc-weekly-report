from __future__ import annotations

from collections import defaultdict
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Any
from zoneinfo import ZoneInfo
import bisect
import math

import pandas as pd

from volume_breakout_operation_utils import (
    add_price_metrics,
    selected_confirmation_for_signal,
    simulate_confirmed_trade,
)
from research_tdcc_dataset_consumer import load_research_tdcc_dataset_contract, require_dataset_id


ROOT = Path(".")
PRICE_DIR = ROOT / "data" / "stock_price_history"
RESEARCH_LATEST_DIR = ROOT / "output" / "latest" / "research_backtest"
RESEARCH_HISTORY_DIR = ROOT / "output" / "history" / "research"
TDCC_EVENTS_CSV = RESEARCH_HISTORY_DIR / "tdcc_weekly_ranking_backtest_events.csv"

LATEST_SUMMARY_CSV = RESEARCH_LATEST_DIR / "w_bottom_tdcc_abc_backtest_latest.csv"
LATEST_SUMMARY_MD = RESEARCH_LATEST_DIR / "w_bottom_tdcc_abc_backtest_latest.md"
HISTORY_SUMMARY_CSV = RESEARCH_HISTORY_DIR / "w_bottom_tdcc_abc_backtest.csv"
HISTORY_EVENTS_CSV = RESEARCH_HISTORY_DIR / "w_bottom_tdcc_abc_events.csv"

MODEL_ID = "w_bottom_right_side"
CONFIRMATION_MODEL_ID = "neckline_volume_breakout_confirmation"
OVERLAY_MODEL_ID = "tdcc_weekly_ranking_formula"
RESEARCH_ID = "w_bottom_tdcc_abc_backtest"
RESEARCH_VARIANT_ID = "warning_research_variant_only"
PARAMETER_SET_ID = "w_bottom_symmetric_tdcc_abc_research_20260624"

LOOKBACK_DAYS = 120
LONG_POSITION_LOOKBACK_DAYS = 252
LONG_POSITION_MIN_DAYS = 180
SECOND_LOW_GAP_MIN = -3.0
SECOND_LOW_GAP_MAX = 6.0
RIGHT_SIDE_REBOUND_MIN = 3.0
RIGHT_SIDE_REBOUND_MAX = 15.0
MAX_RIGHT_LOW_AGE_DAYS = 45
MAX_ABSOLUTE_W_COMPLETION_DAYS = 60
TOUCH_RATIO = 1.00
CLOSE_ZONE_RATIO = 0.98
INVALID_UNDERCUT_RATIO = 0.97
COOLDOWN_CALENDAR_DAYS = 28

SYMMETRY_RATIOS = [1.5, 2.0]
TDCC_AGE_WINDOWS = [7, 14]
TDCC_LIST_TYPES = ["all", "weekly_increase", "consecutive_accumulation"]
TDCC_RANK_BUCKETS: list[int | None] = [None, 50, 20, 10]

FORBIDDEN_PRODUCTION_FIELDS = {
    "trade_decision",
    "action_rating",
    "entry_style",
    "position_sizing",
    "decision_score",
    "daily_candidate_decision",
    "buy_signal",
}

EVENT_COLUMNS = [
    "source_tdcc_dataset_id",
    "model_id",
    "confirmation_model_id",
    "overlay_model_id",
    "research_id",
    "research_variant_id",
    "parameter_set_id",
    "advisory_status",
    "sample_mode",
    "symmetry_ratio",
    "signal_date",
    "stock_id",
    "stock_name",
    "signal_close",
    "left_peak_date",
    "left_low_date",
    "neckline_date",
    "right_low_date",
    "neckline_price",
    "first_rebound_days",
    "right_rebound_days_at_signal",
    "symmetry_deadline_total_days",
    "breakout_date",
    "late_breakout_not_w",
    "second_arc_volume_ratio",
    "tdcc_any_age7",
    "tdcc_any_age14",
    "tdcc_top50_age7",
    "tdcc_top20_age7",
    "tdcc_top10_age7",
    "tdcc_weekly_top20_age7",
    "tdcc_consecutive_top20_age7",
    "tdcc_match_detail_age7",
    "tdcc_match_detail_age14",
    "post_confirmation_trigger_id",
    "post_confirmation_date",
    "a_mature",
    "a_return_pct",
    "a_entry_date",
    "a_exit_date",
    "a_exit_reason",
    "c_mature",
    "c_return_pct",
    "c_entry_date",
    "c_exit_date",
    "c_exit_reason",
    "approved_for_daily",
    "generated_at",
]

SUMMARY_COLUMNS = [
    "source_tdcc_dataset_id",
    "model_id",
    "confirmation_model_id",
    "overlay_model_id",
    "research_id",
    "research_variant_id",
    "parameter_set_id",
    "advisory_status",
    "sample_mode",
    "symmetry_ratio",
    "abc_stage",
    "tdcc_filter_id",
    "tdcc_age_days",
    "tdcc_rank_bucket",
    "sample_size",
    "unique_stocks",
    "mature_sample_size",
    "immature_sample_size",
    "win_rate",
    "avg_return",
    "median_return",
    "avg_mfe",
    "avg_mae",
    "breakout_signal_count",
    "late_breakout_not_w_count",
    "post_confirmation_count",
    "confidence_status",
    "approved_for_daily",
    "risk_notes",
    "generated_at",
]


@dataclass(frozen=True)
class TdccRecord:
    date: str
    list_type: str
    rank: int
    score: float


def now_text() -> str:
    return datetime.now(ZoneInfo("Asia/Taipei")).strftime("%Y-%m-%d %H:%M:%S Asia/Taipei")


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


def safe_float(value: Any) -> float:
    text = safe_str(value).replace(",", "").replace("%", "")
    if not text:
        return math.nan
    try:
        number = float(text)
    except Exception:
        return math.nan
    return number if not math.isnan(number) else math.nan


def normalize_code(value: Any) -> str:
    text = safe_str(value)
    if text.endswith(".0"):
        text = text[:-2]
    return text.zfill(4) if text.isdigit() and len(text) < 4 else text


def normalize_date(value: Any) -> str:
    digits = "".join(ch for ch in safe_str(value) if ch.isdigit())
    if len(digits) >= 8 and digits.startswith("20"):
        return digits[:8]
    return ""


def pct_round(value: float, digits: int = 4) -> float | str:
    if math.isnan(value):
        return ""
    return round(value, digits)


def write_csv(df: pd.DataFrame, path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(path, index=False, encoding="utf-8-sig")


def markdown_table(df: pd.DataFrame, columns: list[str], limit: int = 40) -> list[str]:
    if df.empty:
        return ["_No rows._"]
    view = df.loc[:, columns].head(limit).copy()
    lines = ["| " + " | ".join(columns) + " |", "| " + " | ".join(["---"] * len(columns)) + " |"]
    for _, row in view.iterrows():
        lines.append("| " + " | ".join(safe_str(row.get(col)) for col in columns) + " |")
    return lines


def long_position_ok(history: pd.DataFrame, current_close: float) -> bool:
    lookback = history.tail(LONG_POSITION_LOOKBACK_DAYS)
    valid_close = pd.to_numeric(lookback["close"], errors="coerce").dropna()
    if len(valid_close) < LONG_POSITION_MIN_DAYS or math.isnan(current_close):
        return False
    median_close = float(valid_close.median())
    if median_close <= 0:
        return False
    return (current_close / median_close - 1.0) * 100.0 <= 0


def local_peaks_troughs(highs: list[float], lows: list[float]) -> tuple[list[int], list[int]]:
    peaks: list[int] = []
    troughs: list[int] = []
    for idx in range(3, len(highs) - 3):
        high = highs[idx]
        low = lows[idx]
        if math.isnan(high) or math.isnan(low):
            continue
        local_highs = [value for value in highs[idx - 3 : idx + 4] if not math.isnan(value)]
        local_lows = [value for value in lows[idx - 3 : idx + 4] if not math.isnan(value)]
        if local_highs and high >= max(local_highs) * 0.998:
            peaks.append(idx)
        if local_lows and low <= min(local_lows) * 1.002:
            troughs.append(idx)
    return peaks, troughs


def segment_quality(
    highs: list[float],
    lows: list[float],
    closes: list[float],
    left_peak_idx: int,
    left_low_idx: int,
    neckline_idx: int,
    right_low_idx: int,
    current_close: float,
) -> dict[str, Any]:
    failures: list[str] = []
    left_descent_days = left_low_idx - left_peak_idx + 1
    first_rebound_days = neckline_idx - left_low_idx + 1
    second_decline_days = right_low_idx - neckline_idx + 1
    right_rebound_days = len(closes) - right_low_idx
    if left_descent_days < 3:
        failures.append("left_descent_too_short")
    if first_rebound_days < 5:
        failures.append("first_rebound_too_short")
    if second_decline_days < 5:
        failures.append("second_decline_too_short")
    if right_rebound_days < 3:
        failures.append("right_rebound_too_short")

    first_low = lows[left_low_idx]
    second_low = lows[right_low_idx]
    neckline = highs[neckline_idx]
    first_close_undercuts = sum(1 for value in closes[left_low_idx + 1 : neckline_idx + 1] if value < first_low * 0.985)
    second_close_undercuts = sum(1 for value in closes[right_low_idx + 1 :] if value < second_low * 0.985)
    if min(closes[left_low_idx : neckline_idx + 1]) < first_low * 0.98 or first_close_undercuts >= 2:
        failures.append("first_low_close_repeatedly_undercut")
    if highs[neckline_idx + 1 : right_low_idx + 1] and max(highs[neckline_idx + 1 : right_low_idx + 1]) > neckline * 1.02:
        failures.append("higher_high_after_neckline_before_second_low")
    if lows[right_low_idx:] and min(lows[right_low_idx:]) < second_low * 0.97:
        failures.append("second_low_undercut_after_right_side")
    if second_close_undercuts >= 2:
        failures.append("second_low_close_repeatedly_undercut")

    right_rebound_high = max(highs[right_low_idx:]) if highs[right_low_idx:] else second_low
    span = right_rebound_high - second_low
    if span > 0 and (current_close - second_low) / span * 100.0 < 45.0:
        failures.append("right_rebound_faded")

    return {
        "passed": not failures,
        "left_descent_days": left_descent_days,
        "first_rebound_days": first_rebound_days,
        "second_decline_days": second_decline_days,
        "right_rebound_days_at_signal": right_rebound_days,
    }


def detect_w_bottom_context_at(price: pd.DataFrame, signal_idx: int) -> dict[str, Any] | None:
    current_close = safe_float(price.iloc[signal_idx].get("close"))
    if not long_position_ok(price.iloc[: signal_idx + 1], current_close):
        return None
    window = price.iloc[max(0, signal_idx - LOOKBACK_DAYS + 1) : signal_idx + 1].reset_index(drop=True)
    if len(window) < 80:
        return None

    dates = [normalize_date(value) for value in window["date"].tolist()]
    opens = [safe_float(value) for value in window["open"].tolist()]
    highs = [safe_float(value) for value in window["high"].tolist()]
    lows = [safe_float(value) for value in window["low"].tolist()]
    closes = [safe_float(value) for value in window["close"].tolist()]
    volumes = [safe_float(value) for value in window["volume"].tolist()]

    high_120 = max(highs)
    low_120 = min(lows)
    if math.isnan(high_120) or math.isnan(low_120) or high_120 <= low_120:
        return None
    range_span = high_120 - low_120
    peaks, troughs = local_peaks_troughs(highs, lows)
    best: dict[str, Any] | None = None

    for left_low_idx in troughs:
        pre_peak_start = max(0, left_low_idx - 45)
        pre_peak_end = left_low_idx - 2
        if pre_peak_end <= pre_peak_start:
            continue
        left_peak_candidates = [idx for idx in peaks if pre_peak_start <= idx <= pre_peak_end]
        if left_peak_candidates:
            left_peak_idx = max(left_peak_candidates, key=lambda idx: highs[idx])
        else:
            segment = highs[pre_peak_start:pre_peak_end]
            if not segment:
                continue
            left_peak_idx = pre_peak_start + max(range(len(segment)), key=lambda idx: segment[idx])

        left_peak = highs[left_peak_idx]
        left_low = lows[left_low_idx]
        if left_low <= 0 or (left_peak / left_low - 1.0) * 100.0 < 8.0:
            continue
        if min(lows[left_peak_idx : left_low_idx + 1]) < left_low * 0.98:
            continue

        for right_low_idx in troughs:
            if right_low_idx <= left_low_idx:
                continue
            separation = right_low_idx - left_low_idx
            if separation < 8 or separation > 60:
                continue
            right_low_age = len(window) - 1 - right_low_idx
            if right_low_age > MAX_RIGHT_LOW_AGE_DAYS:
                continue
            right_low = lows[right_low_idx]
            if right_low <= 0:
                continue
            second_low_gap = (right_low / left_low - 1.0) * 100.0
            if second_low_gap < SECOND_LOW_GAP_MIN or second_low_gap > SECOND_LOW_GAP_MAX:
                continue

            middle_highs = highs[left_low_idx : right_low_idx + 1]
            neckline_idx = left_low_idx + max(range(len(middle_highs)), key=lambda idx: middle_highs[idx])
            if neckline_idx <= left_low_idx + 1 or neckline_idx >= right_low_idx - 1:
                continue
            neckline = highs[neckline_idx]
            if neckline <= min(left_low, right_low):
                continue
            depth_left = (neckline / left_low - 1.0) * 100.0
            depth_right = (neckline / right_low - 1.0) * 100.0
            if min(depth_left, depth_right) < 6.0 or (neckline / min(left_low, right_low) - 1.0) * 100.0 < 8.0:
                continue

            quality = segment_quality(highs, lows, closes, left_peak_idx, left_low_idx, neckline_idx, right_low_idx, current_close)
            if not quality["passed"]:
                continue

            pre_base_start = max(0, left_peak_idx - 30)
            pre_base_closes = closes[pre_base_start:left_peak_idx]
            if len(pre_base_closes) < 8:
                continue
            pre_base_lows = lows[pre_base_start:left_peak_idx]
            pre_base_highs = highs[pre_base_start:left_peak_idx]
            pre_low = min(pre_base_lows)
            pre_high = max(pre_base_highs)
            pre_width = (pre_high / pre_low - 1.0) * 100.0 if pre_low > 0 else math.nan
            pre_return = (pre_base_closes[-1] / pre_base_closes[0] - 1.0) * 100.0 if pre_base_closes[0] > 0 else math.nan
            if (not math.isnan(pre_width) and pre_width > 35.0) or (not math.isnan(pre_return) and abs(pre_return) > 25.0):
                continue

            current_to_neckline = (current_close / neckline - 1.0) * 100.0
            close_position = (current_close - low_120) / range_span * 100.0
            attack2_gain = (current_close / right_low - 1.0) * 100.0
            if not (RIGHT_SIDE_REBOUND_MIN <= attack2_gain <= RIGHT_SIDE_REBOUND_MAX):
                continue
            if not (current_to_neckline <= 1.0 and close_position <= 65.0):
                continue

            first_arc_volumes = volumes[left_peak_idx : neckline_idx + 1]
            second_arc_volumes = volumes[neckline_idx:]
            if len(first_arc_volumes) < 3 or len(second_arc_volumes) < 3:
                continue
            first_volume = sum(first_arc_volumes) / len(first_arc_volumes)
            second_volume = sum(second_arc_volumes) / len(second_arc_volumes)
            second_arc_volume_ratio = second_volume / first_volume if first_volume > 0 else math.nan
            if math.isnan(second_arc_volume_ratio) or second_arc_volume_ratio < 1.2:
                continue

            candidate = {
                "left_peak_date": dates[left_peak_idx],
                "left_low_date": dates[left_low_idx],
                "neckline_date": dates[neckline_idx],
                "right_low_date": dates[right_low_idx],
                "neckline_price": neckline,
                "right_low_value": right_low,
                "second_arc_volume_ratio": second_arc_volume_ratio,
                "first_rebound_days": quality["first_rebound_days"],
                "right_rebound_days_at_signal": quality["right_rebound_days_at_signal"],
            }
            if best is None or candidate["right_low_date"] > best["right_low_date"] or (
                candidate["right_low_date"] == best["right_low_date"]
                and candidate["second_arc_volume_ratio"] > best["second_arc_volume_ratio"]
            ):
                best = candidate
    return best


def load_tdcc_index() -> dict[tuple[str, str], list[TdccRecord]]:
    index: dict[tuple[str, str], list[TdccRecord]] = defaultdict(list)
    if not TDCC_EVENTS_CSV.exists():
        return index
    tdcc = pd.read_csv(TDCC_EVENTS_CSV, dtype=str, keep_default_na=False)
    require_dataset_id(
        tdcc,
        load_research_tdcc_dataset_contract(),
        label=TDCC_EVENTS_CSV.as_posix(),
    )
    tdcc = tdcc[tdcc.get("model_id", "").astype(str).eq(OVERLAY_MODEL_ID)].copy()
    for _, row in tdcc.iterrows():
        stock_id = normalize_code(row.get("stock_id"))
        date = normalize_date(row.get("signal_date"))
        list_type = safe_str(row.get("tdcc_list_type"))
        if not stock_id or not date or not list_type:
            continue
        rank = int(safe_float(row.get("tdcc_rank")) if not math.isnan(safe_float(row.get("tdcc_rank"))) else 999999)
        index[(stock_id, list_type)].append(
            TdccRecord(
                date=date,
                list_type=list_type,
                rank=rank,
                score=safe_float(row.get("tdcc_ranking_score")),
            )
        )
    for key in list(index):
        index[key].sort(key=lambda item: item.date)
    return index


def tdcc_asof(index: dict[tuple[str, str], list[TdccRecord]], stock_id: str, event_date: str, age_days: int) -> list[TdccRecord]:
    event_dt = pd.to_datetime(event_date, format="%Y%m%d", errors="coerce")
    if pd.isna(event_dt):
        return []
    matches: list[TdccRecord] = []
    for list_type in ["weekly_increase", "consecutive_accumulation"]:
        records = index.get((stock_id, list_type), [])
        if not records:
            continue
        dates = [item.date for item in records]
        pos = bisect.bisect_right(dates, event_date) - 1
        if pos < 0:
            continue
        record = records[pos]
        signal_dt = pd.to_datetime(record.date, format="%Y%m%d", errors="coerce")
        if pd.isna(signal_dt):
            continue
        age = int((event_dt - signal_dt).days)
        if 0 <= age <= age_days:
            matches.append(record)
    return matches


def match_detail(matches: list[TdccRecord], event_date: str) -> str:
    event_dt = pd.to_datetime(event_date, format="%Y%m%d", errors="coerce")
    parts: list[str] = []
    for item in matches:
        signal_dt = pd.to_datetime(item.date, format="%Y%m%d", errors="coerce")
        age = int((event_dt - signal_dt).days) if not pd.isna(event_dt) and not pd.isna(signal_dt) else -1
        parts.append(f"{item.list_type}:rank{item.rank}:age{age}:date{item.date}")
    return ";".join(parts)


def tdcc_filter_id(list_type: str, rank_bucket: int | None, age_days: int) -> str:
    bucket = "any_rank" if rank_bucket is None else f"top{rank_bucket}"
    return f"{list_type}_{bucket}_age{age_days}"


def tdcc_filter_match(matches: list[TdccRecord], list_type: str, rank_bucket: int | None) -> bool:
    if list_type != "all":
        matches = [item for item in matches if item.list_type == list_type]
    if rank_bucket is not None:
        matches = [item for item in matches if item.rank <= rank_bucket]
    return bool(matches)


def is_neckline_breakout_row(price: pd.DataFrame, idx: int, neckline: float) -> bool:
    row = price.iloc[idx]
    close = safe_float(row.get("close"))
    if math.isnan(close) or close < neckline:
        return False
    open_price = safe_float(row.get("open"))
    high = safe_float(row.get("high"))
    low = safe_float(row.get("low"))
    volume_ratio = safe_float(row.get("volume_ratio"))
    volume_ma20 = safe_float(row.get("volume_ma20"))
    ma20_lots = volume_ma20 / 1000.0 if not math.isnan(volume_ma20) and volume_ma20 >= 100000 else volume_ma20
    prev_close = safe_float(price.iloc[idx - 1].get("close")) if idx > 0 else math.nan

    normal_volume_breakout = False
    if not any(math.isnan(value) for value in [open_price, volume_ratio, ma20_lots]):
        bullish = close > open_price or (close == open_price and not math.isnan(prev_close) and close > prev_close)
        normal_volume_breakout = volume_ratio >= 2.0 and ma20_lots >= 1000 and bullish

    daily_return = safe_float(row.get("return_1d"))
    if math.isnan(daily_return) and not math.isnan(prev_close) and prev_close > 0:
        daily_return = (close / prev_close - 1.0) * 100.0
    locked_limit_breakout = False
    if not any(math.isnan(value) for value in [open_price, high, low, daily_return]):
        one_price = high == low
        tight_range = one_price or (not math.isnan(prev_close) and prev_close > 0 and ((high - low) / prev_close * 100.0) <= 1.0)
        locked_limit_breakout = daily_return >= 9.0 and close >= high * 0.995 and open_price >= close * 0.995 and tight_range
    return normal_volume_breakout or locked_limit_breakout


def find_symmetric_breakout(price: pd.DataFrame, signal_idx: int, context: dict[str, Any], ratio: float) -> tuple[int | None, bool, int]:
    first_rebound_days = int(context["first_rebound_days"])
    right_rebound_days = int(context["right_rebound_days_at_signal"])
    deadline_total = min(MAX_ABSOLUTE_W_COMPLETION_DAYS, max(first_rebound_days + 2, math.ceil(first_rebound_days * ratio)))
    neckline = safe_float(context["neckline_price"])
    right_low = safe_float(context["right_low_value"])
    late_breakout = False
    end_idx = min(len(price), signal_idx + 1 + MAX_ABSOLUTE_W_COMPLETION_DAYS)
    for idx in range(signal_idx + 1, end_idx):
        low = safe_float(price.iloc[idx].get("low"))
        if not math.isnan(right_low) and not math.isnan(low) and low < right_low * INVALID_UNDERCUT_RATIO:
            return None, late_breakout, deadline_total
        total_right_days = right_rebound_days + (idx - signal_idx)
        within_symmetry = total_right_days <= deadline_total
        if is_neckline_breakout_row(price, idx, neckline):
            if within_symmetry:
                return idx, late_breakout, deadline_total
            late_breakout = True
    return None, late_breakout, deadline_total


def build_event_rows(price: pd.DataFrame, tdcc_index: dict[tuple[str, str], list[TdccRecord]], generated_at: str) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    if len(price) < LONG_POSITION_MIN_DAYS:
        return rows
    stock_id = normalize_code(price.iloc[-1].get("stock_id"))
    for signal_idx in range(80, len(price) - 1):
        close = safe_float(price.iloc[signal_idx].get("close"))
        if math.isnan(close) or close <= 0:
            continue
        close_history = pd.to_numeric(price.iloc[: signal_idx + 1]["close"], errors="coerce").dropna()
        if len(close_history) < LONG_POSITION_MIN_DAYS:
            continue
        if close > float(close_history.tail(LONG_POSITION_LOOKBACK_DAYS).median()):
            continue
        recent_low = pd.to_numeric(price.iloc[max(0, signal_idx - MAX_RIGHT_LOW_AGE_DAYS) : signal_idx + 1]["low"], errors="coerce").min()
        if math.isnan(recent_low) or recent_low <= 0:
            continue
        rebound = (close / float(recent_low) - 1.0) * 100.0
        if rebound < 2.0 or rebound > 25.0:
            continue
        context = detect_w_bottom_context_at(price, signal_idx)
        if context is None:
            continue

        signal_date = normalize_date(price.iloc[signal_idx].get("date"))
        for ratio in SYMMETRY_RATIOS:
            breakout_idx, late_breakout, deadline_total = find_symmetric_breakout(price, signal_idx, context, ratio)
            breakout_date = normalize_date(price.iloc[breakout_idx].get("date")) if breakout_idx is not None else ""
            tdcc_age7 = tdcc_asof(tdcc_index, stock_id, breakout_date, 7) if breakout_date else []
            tdcc_age14 = tdcc_asof(tdcc_index, stock_id, breakout_date, 14) if breakout_date else []
            trade_a = simulate_confirmed_trade(price, breakout_idx, breakout_idx) if breakout_idx is not None else None
            selected = selected_confirmation_for_signal(price, breakout_idx) if breakout_idx is not None else None
            trade_c = (
                simulate_confirmed_trade(price, breakout_idx, int(selected["confirmation_idx"]))
                if breakout_idx is not None and selected is not None
                else None
            )
            rows.append(
                {
                    "model_id": MODEL_ID,
                    "confirmation_model_id": CONFIRMATION_MODEL_ID,
                    "overlay_model_id": OVERLAY_MODEL_ID,
                    "research_id": RESEARCH_ID,
                    "research_variant_id": RESEARCH_VARIANT_ID,
                    "parameter_set_id": PARAMETER_SET_ID,
                    "advisory_status": "warning_research_variant_only",
                    "sample_mode": "raw_daily_signal",
                    "symmetry_ratio": ratio,
                    "signal_date": signal_date,
                    "stock_id": stock_id,
                    "stock_name": safe_str(price.iloc[signal_idx].get("stock_name")),
                    "signal_close": pct_round(close),
                    "left_peak_date": context["left_peak_date"],
                    "left_low_date": context["left_low_date"],
                    "neckline_date": context["neckline_date"],
                    "right_low_date": context["right_low_date"],
                    "neckline_price": pct_round(safe_float(context["neckline_price"])),
                    "first_rebound_days": context["first_rebound_days"],
                    "right_rebound_days_at_signal": context["right_rebound_days_at_signal"],
                    "symmetry_deadline_total_days": deadline_total,
                    "breakout_date": breakout_date,
                    "late_breakout_not_w": late_breakout,
                    "second_arc_volume_ratio": pct_round(safe_float(context["second_arc_volume_ratio"])),
                    "tdcc_any_age7": bool(tdcc_age7),
                    "tdcc_any_age14": bool(tdcc_age14),
                    "tdcc_top50_age7": tdcc_filter_match(tdcc_age7, "all", 50),
                    "tdcc_top20_age7": tdcc_filter_match(tdcc_age7, "all", 20),
                    "tdcc_top10_age7": tdcc_filter_match(tdcc_age7, "all", 10),
                    "tdcc_weekly_top20_age7": tdcc_filter_match(tdcc_age7, "weekly_increase", 20),
                    "tdcc_consecutive_top20_age7": tdcc_filter_match(tdcc_age7, "consecutive_accumulation", 20),
                    "tdcc_match_detail_age7": match_detail(tdcc_age7, breakout_date),
                    "tdcc_match_detail_age14": match_detail(tdcc_age14, breakout_date),
                    "post_confirmation_trigger_id": safe_str(selected.get("trigger_id")) if selected else "",
                    "post_confirmation_date": safe_str(selected.get("confirmation_date")) if selected else "",
                    "a_mature": trade_a is not None,
                    "a_return_pct": "" if trade_a is None else trade_a.get("return_pct", ""),
                    "a_entry_date": "" if trade_a is None else trade_a.get("entry_date", ""),
                    "a_exit_date": "" if trade_a is None else trade_a.get("exit_date", ""),
                    "a_exit_reason": "" if trade_a is None else trade_a.get("exit_reason", ""),
                    "c_mature": trade_c is not None,
                    "c_return_pct": "" if trade_c is None else trade_c.get("return_pct", ""),
                    "c_entry_date": "" if trade_c is None else trade_c.get("entry_date", ""),
                    "c_exit_date": "" if trade_c is None else trade_c.get("exit_date", ""),
                    "c_exit_reason": "" if trade_c is None else trade_c.get("exit_reason", ""),
                    "approved_for_daily": False,
                    "generated_at": generated_at,
                }
            )
    return rows


def mark_dedup(events: pd.DataFrame) -> pd.DataFrame:
    events = events.copy()
    events["dedup_20d_eligible"] = False
    base = events[events["symmetry_ratio"].astype(str).eq(str(SYMMETRY_RATIOS[0]))].copy()
    base = base.sort_values(["stock_id", "signal_date"])
    last_date_by_stock: dict[str, str] = {}
    keep_keys: set[tuple[str, str]] = set()
    for _, row in base.iterrows():
        stock_id = safe_str(row.get("stock_id"))
        signal_date = safe_str(row.get("signal_date"))
        if stock_id in last_date_by_stock:
            try:
                delta = (pd.to_datetime(signal_date) - pd.to_datetime(last_date_by_stock[stock_id])).days
            except Exception:
                delta = 999
            if delta < COOLDOWN_CALENDAR_DAYS:
                continue
        keep_keys.add((stock_id, signal_date))
        last_date_by_stock[stock_id] = signal_date
    events["dedup_20d_eligible"] = events.apply(
        lambda row: (safe_str(row.get("stock_id")), safe_str(row.get("signal_date"))) in keep_keys,
        axis=1,
    )
    return events


def confidence_status(sample_size: int) -> str:
    if sample_size >= 100:
        return "high"
    if sample_size >= 30:
        return "medium"
    return "low"


def summarize(events: pd.DataFrame, generated_at: str) -> pd.DataFrame:
    rows: list[dict[str, Any]] = []
    sample_modes = {
        "raw_daily_signal": events,
        "dedup_approx_20_trading_days": events[events["dedup_20d_eligible"].astype(bool)].copy(),
    }
    for sample_mode, sample in sample_modes.items():
        for ratio in SYMMETRY_RATIOS:
            ratio_sample = sample[sample["symmetry_ratio"].astype(float).eq(float(ratio))].copy()
            breakout_sample = ratio_sample[ratio_sample["breakout_date"].astype(str).ne("")].copy()
            late_count = int(ratio_sample["late_breakout_not_w"].astype(str).str.lower().isin(["true", "1"]).sum())
            post_count = int(breakout_sample["post_confirmation_trigger_id"].astype(str).ne("").sum())
            filters: list[tuple[str, int | None, int, pd.DataFrame]] = [("all_any_rank_age0", None, 0, breakout_sample)]
            for age_days in TDCC_AGE_WINDOWS:
                detail_col = f"tdcc_match_detail_age{age_days}"
                for list_type in TDCC_LIST_TYPES:
                    for rank_bucket in TDCC_RANK_BUCKETS:
                        filter_id = tdcc_filter_id(list_type, rank_bucket, age_days)
                        matched_index = []
                        for index, row in breakout_sample.iterrows():
                            details = safe_str(row.get(detail_col))
                            if not details:
                                continue
                            records: list[TdccRecord] = []
                            for part in details.split(";"):
                                pieces = part.split(":")
                                if len(pieces) < 4:
                                    continue
                                records.append(
                                    TdccRecord(
                                        date=pieces[3].replace("date", ""),
                                        list_type=pieces[0],
                                        rank=int(pieces[1].replace("rank", "")),
                                        score=math.nan,
                                    )
                                )
                            if tdcc_filter_match(records, list_type, rank_bucket):
                                matched_index.append(index)
                        filters.append((filter_id, rank_bucket, age_days, breakout_sample.loc[matched_index].copy()))

            for filter_id, rank_bucket, age_days, filtered in filters:
                if filter_id == "all_any_rank_age0":
                    stage_defs = [
                        ("A_w_neckline_breakout_next_open", "a_return_pct", "a_mature"),
                    ]
                else:
                    stage_defs = [
                        ("B_tdcc_filter_next_open", "a_return_pct", "a_mature"),
                        ("C_tdcc_filter_post_confirmation_next_open", "c_return_pct", "c_mature"),
                    ]
                for stage, return_col, mature_col in stage_defs:
                    stage_sample = filtered.copy()
                    if stage.startswith("C_"):
                        stage_sample = stage_sample[stage_sample["post_confirmation_trigger_id"].astype(str).ne("")]
                    mature = stage_sample[stage_sample[mature_col].astype(str).str.lower().isin(["true", "1"])].copy()
                    returns = pd.to_numeric(mature[return_col], errors="coerce").dropna()
                    if stage_sample.empty:
                        continue
                    wins = int((returns > 0).sum()) if not returns.empty else 0
                    rows.append(
                        {
                            "model_id": MODEL_ID,
                            "confirmation_model_id": CONFIRMATION_MODEL_ID,
                            "overlay_model_id": OVERLAY_MODEL_ID,
                            "research_id": RESEARCH_ID,
                            "research_variant_id": RESEARCH_VARIANT_ID,
                            "parameter_set_id": PARAMETER_SET_ID,
                            "advisory_status": "warning_research_variant_only",
                            "sample_mode": sample_mode,
                            "symmetry_ratio": ratio,
                            "abc_stage": stage,
                            "tdcc_filter_id": filter_id,
                            "tdcc_age_days": age_days,
                            "tdcc_rank_bucket": "" if rank_bucket is None else rank_bucket,
                            "sample_size": len(stage_sample),
                            "unique_stocks": stage_sample["stock_id"].nunique(),
                            "mature_sample_size": len(mature),
                            "immature_sample_size": len(stage_sample) - len(mature),
                            "win_rate": pct_round(wins / len(returns) * 100.0 if len(returns) else math.nan, 2),
                            "avg_return": pct_round(float(returns.mean()) if len(returns) else math.nan, 4),
                            "median_return": pct_round(float(returns.median()) if len(returns) else math.nan, 4),
                            "avg_mfe": "",
                            "avg_mae": "",
                            "breakout_signal_count": len(breakout_sample),
                            "late_breakout_not_w_count": late_count,
                            "post_confirmation_count": post_count,
                            "confidence_status": confidence_status(len(mature)),
                            "approved_for_daily": False,
                            "risk_notes": "advisory_only;research_variant_only;not_production_baseline",
                            "generated_at": generated_at,
                        }
                    )
    return pd.DataFrame(rows, columns=SUMMARY_COLUMNS)


def write_markdown(summary: pd.DataFrame, events: pd.DataFrame, generated_at: str) -> None:
    primary = summary[
        summary["sample_mode"].eq("dedup_approx_20_trading_days")
        & summary["symmetry_ratio"].astype(float).eq(1.5)
    ].copy()
    primary = primary.sort_values(["abc_stage", "tdcc_filter_id"])
    best = primary.copy()
    best["mature_sample_size_num"] = pd.to_numeric(best["mature_sample_size"], errors="coerce").fillna(0)
    best["win_rate_num"] = pd.to_numeric(best["win_rate"], errors="coerce").fillna(-999)
    best = best[best["mature_sample_size_num"] > 0].sort_values(
        ["mature_sample_size_num", "win_rate_num"],
        ascending=[False, False],
    )
    lines = [
        "# W-Bottom TDCC A/B/C Backtest",
        "",
        f"- generated_at: `{generated_at}`",
        f"- source_tdcc_dataset_id: `{events['source_tdcc_dataset_id'].iloc[0] if not events.empty else ''}`",
        f"- model_id: `{MODEL_ID}`",
        f"- confirmation_model_id: `{CONFIRMATION_MODEL_ID}`",
        f"- overlay_model_id: `{OVERLAY_MODEL_ID}`",
        f"- research_id: `{RESEARCH_ID}`",
        f"- advisory_status: `{RESEARCH_VARIANT_ID}`",
        "- scope: research only; all rows keep `approved_for_daily=False`.",
        "- note: this uses a research-only W-bottom symmetric-time parameter set while the production PR is still unmerged.",
        "",
        "## Event Counts",
        "",
        f"- raw_event_rows: `{len(events)}`",
        f"- dedup_event_rows: `{int(events['dedup_20d_eligible'].astype(bool).sum())}`",
        "",
        "## Primary Rows",
        "",
        *markdown_table(
            primary,
            [
                "abc_stage",
                "tdcc_filter_id",
                "sample_size",
                "mature_sample_size",
                "win_rate",
                "avg_return",
                "median_return",
                "confidence_status",
            ],
            80,
        ),
        "",
        "## Largest Mature Samples",
        "",
        *markdown_table(
            best,
            [
                "abc_stage",
                "tdcc_filter_id",
                "sample_size",
                "mature_sample_size",
                "win_rate",
                "avg_return",
                "median_return",
                "confidence_status",
            ],
            40,
        ),
        "",
        "## Interpretation Guardrails",
        "",
        "- `A_w_neckline_breakout_next_open`: W-bottom symmetric neckline volume breakout, enter next open.",
        "- `B_tdcc_filter_next_open`: A plus an as-of TDCC filter, enter next open after W neckline breakout.",
        "- `C_tdcc_filter_post_confirmation_next_open`: B plus a volume-breakout-style post confirmation trigger.",
        "- TDCC filters use as-of matching only; future TDCC rows are not allowed.",
        "- Low sample rows are directional research evidence only and must not be promoted directly into production.",
    ]
    LATEST_SUMMARY_MD.parent.mkdir(parents=True, exist_ok=True)
    LATEST_SUMMARY_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    contract = load_research_tdcc_dataset_contract()
    generated_at = now_text()
    tdcc_index = load_tdcc_index()
    all_rows: list[dict[str, Any]] = []
    price_files = sorted(PRICE_DIR.glob("*.csv"))
    for index, path in enumerate(price_files, start=1):
        try:
            price = pd.read_csv(path, dtype={"stock_id": str}, keep_default_na=False)
        except Exception:
            continue
        required = {"date", "stock_id", "stock_name", "open", "high", "low", "close", "volume"}
        if not required.issubset(price.columns):
            continue
        price = add_price_metrics(price).sort_values("date").reset_index(drop=True)
        all_rows.extend(build_event_rows(price, tdcc_index, generated_at))
        if index % 500 == 0:
            print(f"progress price_files={index}/{len(price_files)} event_rows={len(all_rows)}")

    events = pd.DataFrame(all_rows, columns=EVENT_COLUMNS)
    if events.empty:
        raise SystemExit("ERROR: no W-bottom research events generated")
    events = mark_dedup(events)
    summary = summarize(events, generated_at)
    if summary.empty:
        raise SystemExit("ERROR: no W-bottom research summary generated")
    events["source_tdcc_dataset_id"] = contract.dataset_id
    summary["source_tdcc_dataset_id"] = contract.dataset_id

    write_csv(summary, LATEST_SUMMARY_CSV)
    write_csv(summary, HISTORY_SUMMARY_CSV)
    write_csv(events, HISTORY_EVENTS_CSV)
    write_markdown(summary, events, generated_at)

    print(f"Saved: {LATEST_SUMMARY_CSV} rows={len(summary)}")
    print(f"Saved: {HISTORY_EVENTS_CSV} rows={len(events)}")
    print(f"Saved: {LATEST_SUMMARY_MD}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
