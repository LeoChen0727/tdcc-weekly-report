from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Any
from zoneinfo import ZoneInfo
import math

import pandas as pd


ROOT = Path(".")
PRICE_DIR = ROOT / "data" / "stock_price_history"
DAILY_PRICE_DIR = ROOT / "data" / "daily_price"
RESEARCH_LATEST_DIR = ROOT / "output" / "latest" / "research_backtest"
RESEARCH_HISTORY_DIR = ROOT / "output" / "history" / "research"

LATEST_DETAIL_CSV = RESEARCH_LATEST_DIR / "breakout_family_retest_grid_detail_latest.csv"
LATEST_SUMMARY_CSV = RESEARCH_LATEST_DIR / "breakout_family_retest_grid_latest.csv"
LATEST_MD = RESEARCH_LATEST_DIR / "breakout_family_retest_grid_latest.md"
HISTORY_DETAIL_CSV = RESEARCH_HISTORY_DIR / "breakout_family_retest_grid_detail.csv"
HISTORY_SUMMARY_CSV = RESEARCH_HISTORY_DIR / "breakout_family_retest_grid.csv"

RESEARCH_ID = "breakout_family_retest_grid"
RESEARCH_VARIANT_ID = "warning_research_variant_only"
PRODUCTION_READINESS = "not_production_ready_research_only"
PARAMETER_SET_ID = "breakout_family_retest_grid_20260627"

MAX_HOLD_DAYS = 10
RETEST_MAX_DAYS = 10
RETEST_ATTACK_MAX_DAYS = 5
EVENT_COOLDOWN_DAYS = 20
MIN_SIGNAL_DATE = "20250101"
MAX_RECENT_SWING_POINTS = 12
MAX_CANDIDATE_DAYS_PER_STOCK = 25
LATEST_VOLUME_MA20_LOTS_MIN = 500.0
MAX_LATEST_VOLUME_STOCKS = 600

FORBIDDEN_PRODUCTION_FIELDS = {
    "trade_decision",
    "action_rating",
    "entry_style",
    "position_sizing",
    "decision_score",
    "daily_candidate_decision",
    "buy_signal",
}

DETAIL_COLUMNS = [
    "research_id",
    "research_variant_id",
    "parameter_set_id",
    "advisory_status",
    "event_family_id",
    "pattern_subtype",
    "entry_variant",
    "stock_id",
    "stock_name",
    "signal_date",
    "reference_date_1",
    "reference_date_2",
    "reference_price",
    "reference_rule",
    "breakout_distance_pct",
    "volume_ratio",
    "volume_ma20_lots",
    "normal_volume_breakout",
    "locked_limit_up_breakout",
    "signal_close",
    "signal_low",
    "low_position_120_pct",
    "base_width_pct",
    "support_touch_count",
    "descending_line_slope_pct_per_day",
    "direct_entry_date",
    "direct_return_pct",
    "direct_exit_reason",
    "retest_status",
    "retest_date",
    "retest_attack_date",
    "retest_entry_date",
    "retest_return_pct",
    "retest_exit_reason",
    "approved_for_daily",
    "production_readiness",
    "generated_at",
]

SUMMARY_COLUMNS = [
    "research_id",
    "research_variant_id",
    "parameter_set_id",
    "advisory_status",
    "event_family_id",
    "pattern_subtype",
    "entry_variant",
    "sample_size",
    "mature_sample_size",
    "win_count",
    "loss_count",
    "win_rate_pct",
    "avg_return_pct",
    "median_return_pct",
    "stop_signal_low_count",
    "fixed_10d_close_count",
    "retest_not_found_count",
    "retest_found_but_no_attack_count",
    "approved_for_daily",
    "production_readiness",
    "generated_at",
]


@dataclass(frozen=True)
class Event:
    event_family_id: str
    pattern_subtype: str
    signal_idx: int
    reference_idx_1: int | None
    reference_idx_2: int | None
    reference_price: float
    reference_rule: str
    base_width_pct: float
    support_touch_count: int
    descending_line_slope_pct_per_day: float


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
    except ValueError:
        return math.nan
    return number if not math.isnan(number) else math.nan


def metric_text(value: float, digits: int = 4) -> str:
    if math.isnan(value) or math.isinf(value):
        return ""
    return f"{value:.{digits}f}"


def bool_text(value: bool) -> str:
    return "true" if value else "false"


def normalize_code(value: Any) -> str:
    text = safe_str(value)
    if text.endswith(".0"):
        text = text[:-2]
    return text.zfill(4) if text.isdigit() and len(text) < 4 else text


def normalize_date(value: Any) -> str:
    text = safe_str(value)
    if text.endswith(".0"):
        text = text[:-2]
    digits = "".join(ch for ch in text if ch.isdigit())
    return digits[:8]


def read_price(path: Path) -> pd.DataFrame:
    df = pd.read_csv(path, dtype=str, keep_default_na=False)
    if df.empty:
        return df
    df = df.copy()
    df["date"] = df["date"].map(normalize_date)
    df = df[df["date"] != ""].sort_values("date").reset_index(drop=True)
    for column in ["open", "high", "low", "close", "volume", "volume_ma20", "volume_ratio"]:
        df[column] = pd.to_numeric(df.get(column, ""), errors="coerce")
    if "volume_ma20" not in df.columns or df["volume_ma20"].isna().all():
        df["volume_ma20"] = df["volume"].rolling(20, min_periods=20).mean()
    else:
        df["volume_ma20"] = df["volume_ma20"].fillna(df["volume"].rolling(20, min_periods=20).mean())
    df["volume_ratio_calc"] = df["volume"] / df["volume_ma20"].replace(0, pd.NA)
    df["volume_ratio"] = df["volume_ratio"].fillna(df["volume_ratio_calc"])
    df["prev_close"] = df["close"].shift(1)
    df["return_1d_calc"] = (df["close"] / df["prev_close"].replace(0, pd.NA) - 1.0) * 100.0
    df["high_20_prev"] = df["high"].shift(1).rolling(20, min_periods=20).max()
    df["low_40_prev"] = df["low"].shift(1).rolling(40, min_periods=40).min()
    df["high_40_prev"] = df["high"].shift(1).rolling(40, min_periods=40).max()
    df["low_120_prev"] = df["low"].shift(1).rolling(120, min_periods=80).min()
    df["high_120_prev"] = df["high"].shift(1).rolling(120, min_periods=80).max()
    df["range_width_40_pct"] = (df["high_40_prev"] / df["low_40_prev"].replace(0, pd.NA) - 1.0) * 100.0
    df["low_position_120_pct"] = (
        (df["close"] - df["low_120_prev"]) / (df["high_120_prev"] - df["low_120_prev"]).replace(0, pd.NA) * 100.0
    )
    return df


def write_csv(df: pd.DataFrame, path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(path, index=False, encoding="utf-8-sig")


def selected_price_paths() -> list[Path]:
    daily_files = sorted(DAILY_PRICE_DIR.glob("daily_price_*.csv"))
    if not daily_files:
        return sorted(PRICE_DIR.glob("*.csv"))
    latest = daily_files[-1]
    daily = pd.read_csv(latest, dtype=str, keep_default_na=False)
    if daily.empty or "stock_id" not in daily.columns:
        return sorted(PRICE_DIR.glob("*.csv"))
    daily = daily.copy()
    daily["stock_id"] = daily["stock_id"].map(normalize_code)
    daily["volume_num"] = pd.to_numeric(daily.get("volume", ""), errors="coerce")
    daily = daily[
        daily["stock_id"].astype(str).str.fullmatch(r"\d{4}")
        & ~daily["stock_id"].astype(str).str.startswith("00")
    ].copy()
    daily = daily.sort_values("volume_num", ascending=False).head(MAX_LATEST_VOLUME_STOCKS)
    paths = [PRICE_DIR / f"{stock_id}.csv" for stock_id in daily["stock_id"].tolist()]
    existing = [path for path in paths if path.exists()]
    return existing or sorted(PRICE_DIR.glob("*.csv"))


def bullish_attack_candle(row: pd.Series) -> bool:
    open_price = safe_float(row.get("open"))
    close = safe_float(row.get("close"))
    prev_close = safe_float(row.get("prev_close"))
    if math.isnan(open_price) or math.isnan(close):
        return False
    if close > open_price:
        return True
    return not math.isnan(prev_close) and close == open_price and close > prev_close


def locked_limit_up(row: pd.Series) -> bool:
    open_price = safe_float(row.get("open"))
    high = safe_float(row.get("high"))
    low = safe_float(row.get("low"))
    close = safe_float(row.get("close"))
    prev_close = safe_float(row.get("prev_close"))
    ret = safe_float(row.get("return_1d_calc"))
    if any(math.isnan(value) for value in [open_price, high, low, close, prev_close, ret]) or prev_close <= 0:
        return False
    tight_range = high == low or ((high - low) / prev_close * 100.0) <= 1.0
    return ret >= 9.0 and close >= high * 0.995 and open_price >= close * 0.995 and tight_range


def volume_confirmed(row: pd.Series) -> tuple[bool, bool, bool]:
    volume_ratio = safe_float(row.get("volume_ratio"))
    volume_ma20 = safe_float(row.get("volume_ma20"))
    lots = volume_ma20 / 1000.0 if not math.isnan(volume_ma20) and volume_ma20 >= 100000 else volume_ma20
    locked = locked_limit_up(row)
    normal = (
        not any(math.isnan(value) for value in [volume_ratio, lots])
        and volume_ratio >= 2.0
        and lots >= 1000
        and bullish_attack_candle(row)
    )
    return normal or locked, normal, locked


def local_min_indexes(values: list[float], radius: int = 2) -> list[int]:
    out: list[int] = []
    for idx, value in enumerate(values):
        if math.isnan(value):
            continue
        start = max(0, idx - radius)
        end = min(len(values), idx + radius + 1)
        window = [item for item in values[start:end] if not math.isnan(item)]
        if window and value <= min(window) * 1.002:
            out.append(idx)
    return out


def local_max_indexes(values: list[float], radius: int = 2) -> list[int]:
    out: list[int] = []
    for idx, value in enumerate(values):
        if math.isnan(value):
            continue
        start = max(0, idx - radius)
        end = min(len(values), idx + radius + 1)
        window = [item for item in values[start:end] if not math.isnan(item)]
        if window and value >= max(window) * 0.998:
            out.append(idx)
    return out


def detect_bottom_base_volume_attack(price: pd.DataFrame, idx: int) -> Event | None:
    row = price.iloc[idx]
    ok, _, _ = volume_confirmed(row)
    high20 = safe_float(row.get("high_20_prev"))
    close = safe_float(row.get("close"))
    if not ok or math.isnan(high20) or math.isnan(close) or close < high20 * 1.02:
        return None
    width = safe_float(row.get("range_width_40_pct"))
    low_pos = safe_float(row.get("low_position_120_pct"))
    if not math.isnan(width) and width > 45:
        subtype = "wide_base_review"
    elif not math.isnan(low_pos) and low_pos <= 60:
        subtype = "low_position_base_attack"
    else:
        subtype = "base_attack_position_review"
    return Event(
        event_family_id="bottom_base_volume_attack_reference",
        pattern_subtype=subtype,
        signal_idx=idx,
        reference_idx_1=None,
        reference_idx_2=None,
        reference_price=high20,
        reference_rule="recent_20_session_local_base_ceiling",
        base_width_pct=width,
        support_touch_count=0,
        descending_line_slope_pct_per_day=math.nan,
    )


def detect_structured_neckline(price: pd.DataFrame, idx: int) -> Event | None:
    row = price.iloc[idx]
    ok, _, _ = volume_confirmed(row)
    if not ok:
        return None
    close = safe_float(row.get("close"))
    if math.isnan(close) or idx < 90:
        return None
    start = max(0, idx - 90)
    window = price.iloc[start:idx].reset_index(drop=True)
    if len(window) < 70:
        return None
    highs = pd.to_numeric(window["high"], errors="coerce").tolist()
    lows = pd.to_numeric(window["low"], errors="coerce").tolist()
    troughs = [item for item in local_min_indexes(lows) if item <= len(window) - 5]
    troughs = troughs[-MAX_RECENT_SWING_POINTS:]
    if len(troughs) < 2:
        return None

    best: tuple[float, int, int, float, int] | None = None
    for left_pos, left in enumerate(troughs):
        for right in troughs[left_pos + 1 :]:
            separation = right - left
            if separation < 8 or separation > 80:
                continue
            if len(window) - 1 - right > 55:
                continue
            left_low = lows[left]
            right_low = lows[right]
            if left_low <= 0 or right_low <= 0 or math.isnan(left_low) or math.isnan(right_low):
                continue
            support_gap = abs(right_low / left_low - 1.0) * 100.0
            if support_gap > 9.0:
                continue
            support = (left_low + right_low) / 2.0
            high_segment = highs[left + 1 :]
            if len(high_segment) < 5:
                continue
            neckline = max(value for value in high_segment if not math.isnan(value))
            if neckline <= support:
                continue
            depth = (neckline / support - 1.0) * 100.0
            if depth < 6.0:
                continue
            touches = sum(1 for trough in troughs if left <= trough <= len(window) - 1 and abs(lows[trough] / support - 1.0) * 100.0 <= 6.0)
            score = depth + touches * 3.0 - support_gap
            if best is None or score > best[0]:
                best = (score, left, right, neckline, touches)

    if best is None:
        return None
    _, left, right, neckline, touches = best
    prev_close = safe_float(price.iloc[idx - 1].get("close")) if idx > 0 else math.nan
    if close < neckline or (not math.isnan(prev_close) and prev_close >= neckline):
        return None
    support = (lows[left] + lows[right]) / 2.0
    base_width = (neckline / support - 1.0) * 100.0 if support > 0 else math.nan
    if touches >= 3:
        subtype = "triple_or_multi_bottom_proxy"
    else:
        subtype = "double_bottom_or_structured_bottom_proxy"
    return Event(
        event_family_id="structured_neckline_volume_breakout_proxy",
        pattern_subtype=subtype,
        signal_idx=idx,
        reference_idx_1=start + left,
        reference_idx_2=start + right,
        reference_price=neckline,
        reference_rule="support_touches_plus_rebound_ceiling",
        base_width_pct=base_width,
        support_touch_count=touches,
        descending_line_slope_pct_per_day=math.nan,
    )


def detect_descending_resistance(price: pd.DataFrame, idx: int) -> Event | None:
    row = price.iloc[idx]
    ok, _, _ = volume_confirmed(row)
    if not ok or idx < 90:
        return None
    close = safe_float(row.get("close"))
    prev_close = safe_float(price.iloc[idx - 1].get("close")) if idx > 0 else math.nan
    if math.isnan(close) or math.isnan(prev_close):
        return None
    start = max(0, idx - 90)
    window = price.iloc[start:idx].reset_index(drop=True)
    highs = pd.to_numeric(window["high"], errors="coerce").tolist()
    peaks = local_max_indexes(highs)[-MAX_RECENT_SWING_POINTS:]
    if len(peaks) < 2:
        return None

    signal_rel = len(window)
    best: tuple[float, int, int, float, float] | None = None
    for left_pos, left in enumerate(peaks):
        for right in peaks[left_pos + 1 :]:
            separation = right - left
            if separation < 15 or separation > 90:
                continue
            h1 = highs[left]
            h2 = highs[right]
            if h1 <= 0 or h2 <= 0 or math.isnan(h1) or math.isnan(h2):
                continue
            if h2 > h1 * 0.98:
                continue
            slope = (h2 - h1) / separation
            line_price = h1 + slope * (signal_rel - left)
            if line_price <= 0:
                continue
            if close < line_price * 1.01 or prev_close >= line_price:
                continue
            score = (h1 / h2 - 1.0) * 100.0 + separation / 10.0
            if best is None or score > best[0]:
                best = (score, left, right, line_price, slope / h1 * 100.0)
    if best is None:
        return None
    _, left, right, line_price, slope_pct = best
    return Event(
        event_family_id="descending_resistance_volume_breakout_proxy",
        pattern_subtype="descending_resistance_line_proxy",
        signal_idx=idx,
        reference_idx_1=start + left,
        reference_idx_2=start + right,
        reference_price=line_price,
        reference_rule="two_descending_swing_high_line",
        base_width_pct=math.nan,
        support_touch_count=0,
        descending_line_slope_pct_per_day=slope_pct,
    )


def stop_price_for_day(row: pd.Series, stop_level: float) -> float:
    open_price = safe_float(row.get("open"))
    if not math.isnan(open_price) and open_price < stop_level:
        return open_price
    return stop_level


def simulate_trade(price: pd.DataFrame, entry_idx: int, signal_idx: int, stop_level: float | None = None) -> dict[str, Any]:
    planned_exit_idx = entry_idx + MAX_HOLD_DAYS - 1
    if entry_idx >= len(price) or planned_exit_idx >= len(price):
        return {"mature": False}
    entry_price = safe_float(price.iloc[entry_idx].get("open"))
    if math.isnan(entry_price) or entry_price <= 0:
        return {"mature": False}
    if stop_level is None:
        stop_level = safe_float(price.iloc[signal_idx].get("low"))
    if math.isnan(stop_level) or stop_level <= 0:
        return {"mature": False}
    exit_idx = planned_exit_idx
    exit_price = safe_float(price.iloc[planned_exit_idx].get("close"))
    exit_reason = "fixed_10d_close"
    if math.isnan(exit_price):
        return {"mature": False}
    for day_idx in range(entry_idx, planned_exit_idx + 1):
        low = safe_float(price.iloc[day_idx].get("low"))
        if not math.isnan(low) and low <= stop_level:
            exit_idx = day_idx
            exit_price = stop_price_for_day(price.iloc[day_idx], stop_level)
            exit_reason = "stop_signal_low"
            break
    return {
        "mature": True,
        "entry_date": normalize_date(price.iloc[entry_idx].get("date")),
        "exit_date": normalize_date(price.iloc[exit_idx].get("date")),
        "exit_reason": exit_reason,
        "return_pct": (exit_price / entry_price - 1.0) * 100.0,
    }


def simulate_retest_entry(price: pd.DataFrame, event: Event) -> dict[str, Any]:
    idx = event.signal_idx
    reference = event.reference_price
    if reference <= 0 or math.isnan(reference):
        return {"status": "invalid_reference", "mature": False}
    end_retest = min(len(price) - 2, idx + RETEST_MAX_DAYS)
    for retest_idx in range(idx + 1, end_retest + 1):
        row = price.iloc[retest_idx]
        low = safe_float(row.get("low"))
        close = safe_float(row.get("close"))
        if math.isnan(low) or math.isnan(close):
            continue
        if close < reference * 0.97:
            return {"status": "neckline_effectively_broken_before_retest", "mature": False}
        retest_ok = low <= reference * 1.03 and close >= reference * 0.98
        if not retest_ok:
            continue
        end_attack = min(len(price) - 2, retest_idx + RETEST_ATTACK_MAX_DAYS)
        retest_high = safe_float(row.get("high"))
        retest_low = safe_float(row.get("low"))
        for attack_idx in range(retest_idx + 1, end_attack + 1):
            attack = price.iloc[attack_idx]
            attack_close = safe_float(attack.get("close"))
            attack_open = safe_float(attack.get("open"))
            if math.isnan(attack_close) or math.isnan(attack_open):
                continue
            if attack_close < reference * 0.97:
                return {
                    "status": "neckline_effectively_broken_after_retest",
                    "retest_date": normalize_date(price.iloc[retest_idx].get("date")),
                    "mature": False,
                }
            attack_ok = attack_close >= max(reference * 1.02, retest_high) and attack_close >= attack_open
            if not attack_ok:
                continue
            stop_level = min(retest_low, reference * 0.98)
            trade = simulate_trade(price, attack_idx + 1, idx, stop_level=stop_level)
            return {
                **trade,
                "status": "retest_not_broken_then_attack",
                "retest_date": normalize_date(price.iloc[retest_idx].get("date")),
                "attack_date": normalize_date(price.iloc[attack_idx].get("date")),
            }
        return {
            "status": "retest_found_but_no_attack",
            "retest_date": normalize_date(price.iloc[retest_idx].get("date")),
            "mature": False,
        }
    return {"status": "retest_not_found", "mature": False}


def event_row(price: pd.DataFrame, event: Event, generated_at: str, entry_variant: str) -> dict[str, Any]:
    row = price.iloc[event.signal_idx]
    ok, normal, locked = volume_confirmed(row)
    assert ok
    direct = simulate_trade(price, event.signal_idx + 1, event.signal_idx)
    retest = simulate_retest_entry(price, event)
    selected = direct if entry_variant == "direct_breakout_next_open" else retest
    signal_close = safe_float(row.get("close"))
    volume_ma20 = safe_float(row.get("volume_ma20"))
    lots = volume_ma20 / 1000.0 if not math.isnan(volume_ma20) and volume_ma20 >= 100000 else volume_ma20
    reference_1 = "" if event.reference_idx_1 is None else normalize_date(price.iloc[event.reference_idx_1].get("date"))
    reference_2 = "" if event.reference_idx_2 is None else normalize_date(price.iloc[event.reference_idx_2].get("date"))
    return {
        "research_id": RESEARCH_ID,
        "research_variant_id": RESEARCH_VARIANT_ID,
        "parameter_set_id": PARAMETER_SET_ID,
        "advisory_status": RESEARCH_VARIANT_ID,
        "event_family_id": event.event_family_id,
        "pattern_subtype": event.pattern_subtype,
        "entry_variant": entry_variant,
        "stock_id": normalize_code(row.get("stock_id")),
        "stock_name": safe_str(row.get("stock_name")),
        "signal_date": normalize_date(row.get("date")),
        "reference_date_1": reference_1,
        "reference_date_2": reference_2,
        "reference_price": metric_text(event.reference_price),
        "reference_rule": event.reference_rule,
        "breakout_distance_pct": metric_text((signal_close / event.reference_price - 1.0) * 100.0 if event.reference_price > 0 else math.nan),
        "volume_ratio": metric_text(safe_float(row.get("volume_ratio"))),
        "volume_ma20_lots": metric_text(lots),
        "normal_volume_breakout": bool_text(normal),
        "locked_limit_up_breakout": bool_text(locked),
        "signal_close": metric_text(signal_close),
        "signal_low": metric_text(safe_float(row.get("low"))),
        "low_position_120_pct": metric_text(safe_float(row.get("low_position_120_pct"))),
        "base_width_pct": metric_text(event.base_width_pct),
        "support_touch_count": str(event.support_touch_count),
        "descending_line_slope_pct_per_day": metric_text(event.descending_line_slope_pct_per_day),
        "direct_entry_date": safe_str(direct.get("entry_date")),
        "direct_return_pct": metric_text(float(direct.get("return_pct", math.nan)) if direct.get("mature") else math.nan),
        "direct_exit_reason": safe_str(direct.get("exit_reason")),
        "retest_status": safe_str(retest.get("status")),
        "retest_date": safe_str(retest.get("retest_date")),
        "retest_attack_date": safe_str(retest.get("attack_date")),
        "retest_entry_date": safe_str(retest.get("entry_date")),
        "retest_return_pct": metric_text(float(retest.get("return_pct", math.nan)) if retest.get("mature") else math.nan),
        "retest_exit_reason": safe_str(retest.get("exit_reason")),
        "approved_for_daily": "false",
        "production_readiness": PRODUCTION_READINESS,
        "generated_at": generated_at,
    }


def scan_price(price: pd.DataFrame, generated_at: str) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    if len(price) < 150:
        return rows
    stock_id = normalize_code(price.iloc[-1].get("stock_id"))
    if not stock_id.isdigit() or stock_id.startswith("00"):
        return rows
    latest_volume_ma20 = safe_float(price.iloc[-1].get("volume_ma20"))
    latest_lots = latest_volume_ma20 / 1000.0 if not math.isnan(latest_volume_ma20) and latest_volume_ma20 >= 100000 else latest_volume_ma20
    if math.isnan(latest_lots) or latest_lots < LATEST_VOLUME_MA20_LOTS_MIN:
        return rows
    last_event_idx: dict[str, int] = {}
    detectors = [detect_bottom_base_volume_attack, detect_structured_neckline, detect_descending_resistance]
    close = pd.to_numeric(price["close"], errors="coerce")
    high20 = pd.to_numeric(price["high_20_prev"], errors="coerce")
    volume_ratio = pd.to_numeric(price["volume_ratio"], errors="coerce")
    volume_ma20 = pd.to_numeric(price["volume_ma20"], errors="coerce")
    volume_ma20_lots = volume_ma20.where(volume_ma20 < 100000, volume_ma20 / 1000.0)
    open_price = pd.to_numeric(price["open"], errors="coerce")
    high = pd.to_numeric(price["high"], errors="coerce")
    low = pd.to_numeric(price["low"], errors="coerce")
    prev_close = pd.to_numeric(price["prev_close"], errors="coerce")
    ret1 = pd.to_numeric(price["return_1d_calc"], errors="coerce")
    normal_volume = volume_ratio.ge(2.0) & volume_ma20_lots.ge(1000.0) & close.ge(open_price)
    tight_range = high.eq(low) | ((high - low) / prev_close.replace(0, pd.NA) * 100.0).le(1.0)
    locked = ret1.ge(9.0) & close.ge(high * 0.995) & open_price.ge(close * 0.995) & tight_range
    candidate_mask = (
        price["date"].astype(str).ge(MIN_SIGNAL_DATE)
        & (normal_volume | locked)
        & close.ge(high20)
    )
    max_idx = len(price) - MAX_HOLD_DAYS - RETEST_MAX_DAYS - RETEST_ATTACK_MAX_DAYS - 2
    candidate_indexes = [int(idx) for idx in price.index[candidate_mask] if 130 <= int(idx) < max_idx]
    candidate_indexes = candidate_indexes[-MAX_CANDIDATE_DAYS_PER_STOCK:]
    for idx in candidate_indexes:
        for detector in detectors:
            event = detector(price, idx)
            if event is None:
                continue
            last_idx = last_event_idx.get(event.event_family_id)
            if last_idx is not None and idx - last_idx < EVENT_COOLDOWN_DAYS:
                continue
            last_event_idx[event.event_family_id] = idx
            rows.append(event_row(price, event, generated_at, "direct_breakout_next_open"))
            rows.append(event_row(price, event, generated_at, "retest_hold_then_attack_next_open"))
    return rows


def build_detail(generated_at: str) -> pd.DataFrame:
    rows: list[dict[str, Any]] = []
    for path in selected_price_paths():
        price = read_price(path)
        if price.empty:
            continue
        rows.extend(scan_price(price, generated_at))
    detail = pd.DataFrame(rows)
    if detail.empty:
        raise SystemExit("ERROR: breakout family retest grid produced no rows")
    for column in DETAIL_COLUMNS:
        if column not in detail.columns:
            detail[column] = ""
    forbidden = sorted(set(detail.columns) & FORBIDDEN_PRODUCTION_FIELDS)
    if forbidden:
        raise SystemExit(f"ERROR: forbidden production fields in detail: {forbidden}")
    return detail[DETAIL_COLUMNS].sort_values(["event_family_id", "stock_id", "signal_date", "entry_variant"]).reset_index(drop=True)


def to_num(series: pd.Series) -> pd.Series:
    return pd.to_numeric(series, errors="coerce")


def build_summary(detail: pd.DataFrame, generated_at: str) -> pd.DataFrame:
    rows: list[dict[str, Any]] = []
    for (family, subtype, entry), group in detail.groupby(["event_family_id", "pattern_subtype", "entry_variant"], dropna=False):
        if entry == "direct_breakout_next_open":
            returns = to_num(group["direct_return_pct"]).dropna()
            exits = group["direct_exit_reason"].astype(str)
        else:
            returns = to_num(group["retest_return_pct"]).dropna()
            exits = group["retest_exit_reason"].astype(str)
        win_count = int((returns > 0).sum())
        loss_count = int((returns <= 0).sum())
        rows.append(
            {
                "research_id": RESEARCH_ID,
                "research_variant_id": RESEARCH_VARIANT_ID,
                "parameter_set_id": PARAMETER_SET_ID,
                "advisory_status": RESEARCH_VARIANT_ID,
                "event_family_id": family,
                "pattern_subtype": subtype,
                "entry_variant": entry,
                "sample_size": str(len(group)),
                "mature_sample_size": str(len(returns)),
                "win_count": str(win_count),
                "loss_count": str(loss_count),
                "win_rate_pct": metric_text(win_count / len(returns) * 100.0 if len(returns) else math.nan),
                "avg_return_pct": metric_text(float(returns.mean()) if len(returns) else math.nan),
                "median_return_pct": metric_text(float(returns.median()) if len(returns) else math.nan),
                "stop_signal_low_count": str(int(exits.eq("stop_signal_low").sum())),
                "fixed_10d_close_count": str(int(exits.eq("fixed_10d_close").sum())),
                "retest_not_found_count": str(int(group["retest_status"].eq("retest_not_found").sum())),
                "retest_found_but_no_attack_count": str(int(group["retest_status"].eq("retest_found_but_no_attack").sum())),
                "approved_for_daily": "false",
                "production_readiness": PRODUCTION_READINESS,
                "generated_at": generated_at,
            }
        )
    summary = pd.DataFrame(rows)
    for column in SUMMARY_COLUMNS:
        if column not in summary.columns:
            summary[column] = ""
    forbidden = sorted(set(summary.columns) & FORBIDDEN_PRODUCTION_FIELDS)
    if forbidden:
        raise SystemExit(f"ERROR: forbidden production fields in summary: {forbidden}")
    return summary[SUMMARY_COLUMNS].sort_values(["event_family_id", "pattern_subtype", "entry_variant"]).reset_index(drop=True)


def markdown_table(df: pd.DataFrame, columns: list[str], limit: int = 80) -> list[str]:
    if df.empty:
        return ["_No rows._"]
    lines = ["| " + " | ".join(columns) + " |", "| " + " | ".join(["---"] * len(columns)) + " |"]
    for _, row in df.head(limit).iterrows():
        lines.append("| " + " | ".join(safe_str(row.get(column)) for column in columns) + " |")
    return lines


def write_markdown(summary: pd.DataFrame, detail: pd.DataFrame, generated_at: str) -> None:
    direct = summary[summary["entry_variant"].eq("direct_breakout_next_open")]
    retest = summary[summary["entry_variant"].eq("retest_hold_then_attack_next_open")]
    lines = [
        "# Breakout Family Retest Grid",
        "",
        f"- generated_at: `{generated_at}`",
        f"- research_id: `{RESEARCH_ID}`",
        f"- parameter_set_id: `{PARAMETER_SET_ID}`",
        f"- detail_rows: `{len(detail)}`",
        "- production impact: `none`; this grid is advisory-only and does not modify production model conditions, scoring, ranking, PDF logic, or baseline.",
        "",
        "## Scope",
        "",
        "This grid is no longer limited to W-bottom. It compares broad structured-neckline proxy breakouts, descending-resistance proxy breakouts, and the current bottom/base volume-attack reference family.",
        "",
        "First-pass sampling limit: the builder uses the latest daily-price file to keep the top 600 individual stocks by latest trading volume, then scans at most the latest 25 candidate signal days per stock. Use this to compare rule direction before expanding to a heavier full-market replay.",
        "",
        "The 20-session line used by the bottom/base volume-attack reference is only a short local base ceiling used as a breakout threshold. It is not a previous-high model definition.",
        "",
        "## Entry Definitions",
        "",
        "- `direct_breakout_next_open`: buy next open after the breakout signal day.",
        "- `retest_hold_then_attack_next_open`: after the breakout, wait up to 10 trading days for a neckline/resistance retest that does not close below the reference by more than 3%, then buy next open after a renewed attack within 5 trading days.",
        "- Exit: stop if the relevant signal/retest support is broken; otherwise sell at the 10th trading-day close.",
        "",
        "## Summary",
        "",
        *markdown_table(
            summary,
            [
                "event_family_id",
                "pattern_subtype",
                "entry_variant",
                "sample_size",
                "mature_sample_size",
                "win_rate_pct",
                "avg_return_pct",
                "median_return_pct",
                "retest_not_found_count",
                "retest_found_but_no_attack_count",
            ],
            limit=80,
        ),
        "",
        "## Direct Entry Only",
        "",
        *markdown_table(
            direct,
            ["event_family_id", "pattern_subtype", "sample_size", "mature_sample_size", "win_rate_pct", "avg_return_pct", "median_return_pct"],
            limit=80,
        ),
        "",
        "## Retest Entry Only",
        "",
        *markdown_table(
            retest,
            ["event_family_id", "pattern_subtype", "sample_size", "mature_sample_size", "win_rate_pct", "avg_return_pct", "median_return_pct"],
            limit=80,
        ),
        "",
        "## Interpretation",
        "",
        "Use this as a first sample-finding grid, not as a production recommendation. If pattern subtypes do not show materially different results after validation, the neckline model can remain one broad structured-neckline model instead of separate W-bottom / triple-bottom / other models.",
    ]
    LATEST_MD.parent.mkdir(parents=True, exist_ok=True)
    LATEST_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    generated_at = now_text()
    detail = build_detail(generated_at)
    summary = build_summary(detail, generated_at)
    write_csv(detail, LATEST_DETAIL_CSV)
    write_csv(summary, LATEST_SUMMARY_CSV)
    write_csv(detail, HISTORY_DETAIL_CSV)
    write_csv(summary, HISTORY_SUMMARY_CSV)
    write_markdown(summary, detail, generated_at)
    print(f"Saved: {LATEST_DETAIL_CSV} rows={len(detail)}")
    print(f"Saved: {LATEST_SUMMARY_CSV} rows={len(summary)}")
    print(f"Saved: {LATEST_MD}")
    print(f"Saved: {HISTORY_DETAIL_CSV} rows={len(detail)}")
    print(f"Saved: {HISTORY_SUMMARY_CSV} rows={len(summary)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
