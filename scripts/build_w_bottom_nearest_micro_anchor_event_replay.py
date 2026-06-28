from __future__ import annotations

from datetime import datetime
from pathlib import Path
from typing import Any
from zoneinfo import ZoneInfo
import math

import pandas as pd

import build_w_bottom_tdcc_abc_backtest as w_bottom


ROOT = Path(".")
RESEARCH_LATEST_DIR = ROOT / "output" / "latest" / "research_backtest"
RESEARCH_HISTORY_DIR = ROOT / "output" / "history" / "research"

BASELINE_EVENTS_CSV = RESEARCH_HISTORY_DIR / "w_bottom_tdcc_abc_events.csv"
LATEST_EVENTS_CSV = RESEARCH_LATEST_DIR / "w_bottom_nearest_micro_anchor_event_replay_events_latest.csv"
LATEST_DETAIL_CSV = RESEARCH_LATEST_DIR / "w_bottom_nearest_micro_anchor_event_replay_detail_latest.csv"
LATEST_SUMMARY_CSV = RESEARCH_LATEST_DIR / "w_bottom_nearest_micro_anchor_event_replay_latest.csv"
LATEST_MD = RESEARCH_LATEST_DIR / "w_bottom_nearest_micro_anchor_event_replay_latest.md"
HISTORY_EVENTS_CSV = RESEARCH_HISTORY_DIR / "w_bottom_nearest_micro_anchor_event_replay_events.csv"
HISTORY_DETAIL_CSV = RESEARCH_HISTORY_DIR / "w_bottom_nearest_micro_anchor_event_replay_detail.csv"
HISTORY_SUMMARY_CSV = RESEARCH_HISTORY_DIR / "w_bottom_nearest_micro_anchor_event_replay.csv"

MODEL_ID = "w_bottom_right_side"
CONFIRMATION_MODEL_ID = "neckline_volume_breakout_confirmation"
OVERLAY_MODEL_ID = "tdcc_weekly_ranking_formula"
RESEARCH_ID = "w_bottom_nearest_micro_anchor_event_replay"
SOURCE_RESEARCH_ID = "w_bottom_left_anchor_rule_replay"
RESEARCH_VARIANT_ID = "warning_research_variant_only"
PARAMETER_SET_ID = "w_bottom_nearest_micro_anchor_event_replay_20260625"
LEFT_ANCHOR_RULE_ID = "nearest_micro_pressure_45d_min15_before_left_low"
LEFT_ANCHOR_WINDOW_DAYS = 45
MIN_LEFT_DESCENT_DAYS = 8
MICRO_PRESSURE_MIN_DROP_PCT = 15.0
MICRO_PEAK_RADIUS = 1
BASELINE_EVENT_SET_ID = "baseline_current_detector"
VARIANT_EVENT_SET_ID = "variant_nearest_micro_45d_event_replay"
PRIMARY_SYMMETRY_RATIO = 1.5
PRODUCTION_READINESS = "not_production_ready_research_only"

EVENT_COLUMNS = [
    "model_id",
    "confirmation_model_id",
    "overlay_model_id",
    "research_id",
    "source_research_id",
    "research_variant_id",
    "parameter_set_id",
    "advisory_status",
    "sample_mode",
    "left_anchor_rule_id",
    "left_anchor_rule_reason",
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
    "production_readiness",
    "generated_at",
]

DETAIL_COLUMNS = [
    "model_id",
    "confirmation_model_id",
    "overlay_model_id",
    "research_id",
    "source_research_id",
    "research_variant_id",
    "parameter_set_id",
    "advisory_status",
    "comparison_status",
    "stock_id",
    "stock_name",
    "signal_date",
    "baseline_present",
    "variant_present",
    "baseline_left_peak_date",
    "variant_left_peak_date",
    "baseline_left_low_date",
    "variant_left_low_date",
    "baseline_neckline_date",
    "variant_neckline_date",
    "baseline_right_low_date",
    "variant_right_low_date",
    "baseline_breakout_date",
    "variant_breakout_date",
    "baseline_late_breakout_not_w",
    "variant_late_breakout_not_w",
    "baseline_a_mature",
    "variant_a_mature",
    "baseline_a_return_pct",
    "variant_a_return_pct",
    "baseline_tdcc_any_age7",
    "variant_tdcc_any_age7",
    "variant_left_anchor_rule_id",
    "variant_left_anchor_rule_reason",
    "approved_for_daily",
    "production_readiness",
    "generated_at",
]

SUMMARY_COLUMNS = [
    "model_id",
    "confirmation_model_id",
    "overlay_model_id",
    "research_id",
    "source_research_id",
    "research_variant_id",
    "parameter_set_id",
    "advisory_status",
    "summary_type",
    "event_set_id",
    "comparison_status",
    "sample_mode",
    "symmetry_ratio",
    "sample_size",
    "unique_stocks",
    "breakout_signal_count",
    "late_breakout_not_w_count",
    "post_confirmation_count",
    "mature_sample_size",
    "win_count",
    "win_rate_pct",
    "avg_a_return_pct",
    "median_a_return_pct",
    "tdcc_any_age7_count",
    "baseline_sample_size",
    "baseline_mature_sample_size",
    "delta_sample_size_vs_baseline",
    "delta_win_rate_pct_vs_baseline",
    "delta_avg_a_return_pct_vs_baseline",
    "sample_warning",
    "approved_for_daily",
    "production_readiness",
    "generated_at",
]

FORBIDDEN_PRODUCTION_FIELDS = {
    "trade_decision",
    "action_rating",
    "entry_style",
    "position_sizing",
    "decision_score",
    "daily_candidate_decision",
    "buy_signal",
}


def now_text() -> str:
    return datetime.now(ZoneInfo("Asia/Taipei")).strftime("%Y-%m-%d %H:%M:%S Asia/Taipei")


def safe_str(value: Any) -> str:
    return w_bottom.safe_str(value)


def safe_float(value: Any) -> float:
    return w_bottom.safe_float(value)


def normalize_code(value: Any) -> str:
    return w_bottom.normalize_code(value)


def normalize_date(value: Any) -> str:
    return w_bottom.normalize_date(value)


def pct_round(value: float, digits: int = 4) -> float | str:
    return w_bottom.pct_round(value, digits)


def bool_text(value: bool) -> str:
    return "true" if value else "false"


def bool_series(series: pd.Series) -> pd.Series:
    return series.astype(str).str.lower().isin(["true", "1", "yes"])


def write_csv(df: pd.DataFrame, path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(path, index=False, encoding="utf-8-sig")


def markdown_table(df: pd.DataFrame, columns: list[str], limit: int = 40) -> list[str]:
    if df.empty:
        return ["_No rows._"]
    view = df.loc[:, columns].head(limit).copy()
    lines = ["| " + " | ".join(columns) + " |", "| " + " | ".join(["---"] * len(columns)) + " |"]
    for _, row in view.iterrows():
        lines.append("| " + " | ".join(safe_str(row.get(column)) for column in columns) + " |")
    return lines


def micro_peak_indexes(highs: list[float]) -> list[int]:
    indexes: list[int] = []
    for idx, high in enumerate(highs):
        if math.isnan(high):
            continue
        start = max(0, idx - MICRO_PEAK_RADIUS)
        end = min(len(highs), idx + MICRO_PEAK_RADIUS + 1)
        local_highs = [value for value in highs[start:end] if not math.isnan(value)]
        if local_highs and high >= max(local_highs) * 0.998:
            indexes.append(idx)
    return indexes


def nearest_micro_pressure_before_left_low(
    highs: list[float],
    lows: list[float],
    micro_peaks: list[int],
    left_low_idx: int,
) -> tuple[int | None, str]:
    left_low = lows[left_low_idx]
    if left_low <= 0 or math.isnan(left_low):
        return None, "invalid_left_low_price"
    min_idx = max(0, left_low_idx - LEFT_ANCHOR_WINDOW_DAYS)
    max_idx = min(left_low_idx - 2, left_low_idx - MIN_LEFT_DESCENT_DAYS)
    if max_idx < min_idx:
        return None, f"no_room_for_min_{MIN_LEFT_DESCENT_DAYS}d_left_leg"
    candidates = [
        idx
        for idx in micro_peaks
        if min_idx <= idx <= max_idx and (highs[idx] / left_low - 1.0) * 100.0 >= MICRO_PRESSURE_MIN_DROP_PCT
    ]
    if candidates:
        return max(candidates), (
            f"selected_nearest_micro_peak_with_min_{MICRO_PRESSURE_MIN_DROP_PCT:g}pct_drop"
            f"_and_min_{MIN_LEFT_DESCENT_DAYS}d_left_leg"
        )
    return None, (
        f"no_micro_peak_with_min_{MICRO_PRESSURE_MIN_DROP_PCT:g}pct_drop"
        f"_and_min_{MIN_LEFT_DESCENT_DAYS}d_left_leg"
    )


def detect_nearest_micro_context_at(price: pd.DataFrame, signal_idx: int) -> dict[str, Any] | None:
    current_close = safe_float(price.iloc[signal_idx].get("close"))
    if not w_bottom.long_position_ok(price.iloc[: signal_idx + 1], current_close):
        return None
    window = price.iloc[max(0, signal_idx - w_bottom.LOOKBACK_DAYS + 1) : signal_idx + 1].reset_index(drop=True)
    if len(window) < 80:
        return None

    dates = [normalize_date(value) for value in window["date"].tolist()]
    highs = [safe_float(value) for value in window["high"].tolist()]
    lows = [safe_float(value) for value in window["low"].tolist()]
    closes = [safe_float(value) for value in window["close"].tolist()]
    volumes = [safe_float(value) for value in window["volume"].tolist()]

    high_120 = max(highs)
    low_120 = min(lows)
    if math.isnan(high_120) or math.isnan(low_120) or high_120 <= low_120:
        return None
    range_span = high_120 - low_120
    _, troughs = w_bottom.local_peaks_troughs(highs, lows)
    micro_peaks = micro_peak_indexes(highs)
    best: dict[str, Any] | None = None

    for left_low_idx in troughs:
        left_peak_idx, selection_reason = nearest_micro_pressure_before_left_low(
            highs,
            lows,
            micro_peaks,
            left_low_idx,
        )
        if left_peak_idx is None:
            continue

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
            if right_low_age > w_bottom.MAX_RIGHT_LOW_AGE_DAYS:
                continue
            right_low = lows[right_low_idx]
            if right_low <= 0:
                continue
            second_low_gap = (right_low / left_low - 1.0) * 100.0
            if second_low_gap < w_bottom.SECOND_LOW_GAP_MIN or second_low_gap > w_bottom.SECOND_LOW_GAP_MAX:
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

            quality = w_bottom.segment_quality(highs, lows, closes, left_peak_idx, left_low_idx, neckline_idx, right_low_idx, current_close)
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
            if not (w_bottom.RIGHT_SIDE_REBOUND_MIN <= attack2_gain <= w_bottom.RIGHT_SIDE_REBOUND_MAX):
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
                "left_anchor_rule_id": LEFT_ANCHOR_RULE_ID,
                "left_anchor_rule_reason": selection_reason,
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


def build_variant_event_rows(price: pd.DataFrame, tdcc_index: dict[tuple[str, str], list[w_bottom.TdccRecord]], generated_at: str) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    if len(price) < w_bottom.LONG_POSITION_MIN_DAYS:
        return rows
    stock_id = normalize_code(price.iloc[-1].get("stock_id"))
    for signal_idx in range(80, len(price) - 1):
        close = safe_float(price.iloc[signal_idx].get("close"))
        if math.isnan(close) or close <= 0:
            continue
        close_history = pd.to_numeric(price.iloc[: signal_idx + 1]["close"], errors="coerce").dropna()
        if len(close_history) < w_bottom.LONG_POSITION_MIN_DAYS:
            continue
        if close > float(close_history.tail(w_bottom.LONG_POSITION_LOOKBACK_DAYS).median()):
            continue
        recent_low = pd.to_numeric(price.iloc[max(0, signal_idx - w_bottom.MAX_RIGHT_LOW_AGE_DAYS) : signal_idx + 1]["low"], errors="coerce").min()
        if math.isnan(recent_low) or recent_low <= 0:
            continue
        rebound = (close / float(recent_low) - 1.0) * 100.0
        if rebound < 2.0 or rebound > 25.0:
            continue
        context = detect_nearest_micro_context_at(price, signal_idx)
        if context is None:
            continue

        signal_date = normalize_date(price.iloc[signal_idx].get("date"))
        for ratio in w_bottom.SYMMETRY_RATIOS:
            breakout_idx, late_breakout, deadline_total = w_bottom.find_symmetric_breakout(price, signal_idx, context, ratio)
            breakout_date = normalize_date(price.iloc[breakout_idx].get("date")) if breakout_idx is not None else ""
            tdcc_age7 = w_bottom.tdcc_asof(tdcc_index, stock_id, breakout_date, 7) if breakout_date else []
            tdcc_age14 = w_bottom.tdcc_asof(tdcc_index, stock_id, breakout_date, 14) if breakout_date else []
            trade_a = w_bottom.simulate_confirmed_trade(price, breakout_idx, breakout_idx) if breakout_idx is not None else None
            selected = w_bottom.selected_confirmation_for_signal(price, breakout_idx) if breakout_idx is not None else None
            trade_c = (
                w_bottom.simulate_confirmed_trade(price, breakout_idx, int(selected["confirmation_idx"]))
                if breakout_idx is not None and selected is not None
                else None
            )
            rows.append(
                {
                    "model_id": MODEL_ID,
                    "confirmation_model_id": CONFIRMATION_MODEL_ID,
                    "overlay_model_id": OVERLAY_MODEL_ID,
                    "research_id": RESEARCH_ID,
                    "source_research_id": SOURCE_RESEARCH_ID,
                    "research_variant_id": RESEARCH_VARIANT_ID,
                    "parameter_set_id": PARAMETER_SET_ID,
                    "advisory_status": RESEARCH_VARIANT_ID,
                    "sample_mode": "raw_daily_signal",
                    "left_anchor_rule_id": context["left_anchor_rule_id"],
                    "left_anchor_rule_reason": context["left_anchor_rule_reason"],
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
                    "tdcc_top50_age7": w_bottom.tdcc_filter_match(tdcc_age7, "all", 50),
                    "tdcc_top20_age7": w_bottom.tdcc_filter_match(tdcc_age7, "all", 20),
                    "tdcc_top10_age7": w_bottom.tdcc_filter_match(tdcc_age7, "all", 10),
                    "tdcc_weekly_top20_age7": w_bottom.tdcc_filter_match(tdcc_age7, "weekly_increase", 20),
                    "tdcc_consecutive_top20_age7": w_bottom.tdcc_filter_match(tdcc_age7, "consecutive_accumulation", 20),
                    "tdcc_match_detail_age7": w_bottom.match_detail(tdcc_age7, breakout_date),
                    "tdcc_match_detail_age14": w_bottom.match_detail(tdcc_age14, breakout_date),
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
                    "production_readiness": PRODUCTION_READINESS,
                    "generated_at": generated_at,
                }
            )
    return rows


def comparable_events(events: pd.DataFrame) -> pd.DataFrame:
    sample = events[
        events["symmetry_ratio"].astype(float).eq(PRIMARY_SYMMETRY_RATIO)
        & bool_series(events["dedup_20d_eligible"])
    ].copy()
    sample["stock_id"] = sample["stock_id"].map(normalize_code)
    sample["signal_date"] = sample["signal_date"].map(normalize_date)
    return sample.sort_values(["stock_id", "signal_date"]).drop_duplicates(["stock_id", "signal_date"], keep="first")


def load_baseline_events() -> pd.DataFrame:
    if not BASELINE_EVENTS_CSV.exists():
        raise SystemExit(f"ERROR: missing baseline events: {BASELINE_EVENTS_CSV}")
    baseline = pd.read_csv(BASELINE_EVENTS_CSV, dtype=str, keep_default_na=False)
    missing = sorted(set(w_bottom.EVENT_COLUMNS + ["dedup_20d_eligible"]) - set(baseline.columns))
    if missing:
        raise SystemExit(f"ERROR: baseline events missing columns: {missing}")
    return baseline


def row_by_key(df: pd.DataFrame) -> dict[tuple[str, str], pd.Series]:
    rows: dict[tuple[str, str], pd.Series] = {}
    for _, row in df.iterrows():
        rows[(normalize_code(row.get("stock_id")), normalize_date(row.get("signal_date")))] = row
    return rows


def build_comparison_detail(baseline_events: pd.DataFrame, variant_events: pd.DataFrame, generated_at: str) -> pd.DataFrame:
    baseline = comparable_events(baseline_events)
    variant = comparable_events(variant_events)
    baseline_by_key = row_by_key(baseline)
    variant_by_key = row_by_key(variant)
    keys = sorted(set(baseline_by_key) | set(variant_by_key))
    rows: list[dict[str, Any]] = []

    for stock_id, signal_date in keys:
        base = baseline_by_key.get((stock_id, signal_date))
        var = variant_by_key.get((stock_id, signal_date))
        if base is not None and var is not None:
            status = "common"
        elif var is not None:
            status = "variant_only"
        else:
            status = "baseline_only"
        source = var if var is not None else base
        rows.append(
            {
                "model_id": MODEL_ID,
                "confirmation_model_id": CONFIRMATION_MODEL_ID,
                "overlay_model_id": OVERLAY_MODEL_ID,
                "research_id": RESEARCH_ID,
                "source_research_id": SOURCE_RESEARCH_ID,
                "research_variant_id": RESEARCH_VARIANT_ID,
                "parameter_set_id": PARAMETER_SET_ID,
                "advisory_status": RESEARCH_VARIANT_ID,
                "comparison_status": status,
                "stock_id": stock_id,
                "stock_name": safe_str(source.get("stock_name")) if source is not None else "",
                "signal_date": signal_date,
                "baseline_present": bool_text(base is not None),
                "variant_present": bool_text(var is not None),
                "baseline_left_peak_date": safe_str(base.get("left_peak_date")) if base is not None else "",
                "variant_left_peak_date": safe_str(var.get("left_peak_date")) if var is not None else "",
                "baseline_left_low_date": safe_str(base.get("left_low_date")) if base is not None else "",
                "variant_left_low_date": safe_str(var.get("left_low_date")) if var is not None else "",
                "baseline_neckline_date": safe_str(base.get("neckline_date")) if base is not None else "",
                "variant_neckline_date": safe_str(var.get("neckline_date")) if var is not None else "",
                "baseline_right_low_date": safe_str(base.get("right_low_date")) if base is not None else "",
                "variant_right_low_date": safe_str(var.get("right_low_date")) if var is not None else "",
                "baseline_breakout_date": safe_str(base.get("breakout_date")) if base is not None else "",
                "variant_breakout_date": safe_str(var.get("breakout_date")) if var is not None else "",
                "baseline_late_breakout_not_w": safe_str(base.get("late_breakout_not_w")) if base is not None else "",
                "variant_late_breakout_not_w": safe_str(var.get("late_breakout_not_w")) if var is not None else "",
                "baseline_a_mature": safe_str(base.get("a_mature")) if base is not None else "",
                "variant_a_mature": safe_str(var.get("a_mature")) if var is not None else "",
                "baseline_a_return_pct": safe_str(base.get("a_return_pct")) if base is not None else "",
                "variant_a_return_pct": safe_str(var.get("a_return_pct")) if var is not None else "",
                "baseline_tdcc_any_age7": safe_str(base.get("tdcc_any_age7")) if base is not None else "",
                "variant_tdcc_any_age7": safe_str(var.get("tdcc_any_age7")) if var is not None else "",
                "variant_left_anchor_rule_id": safe_str(var.get("left_anchor_rule_id")) if var is not None else "",
                "variant_left_anchor_rule_reason": safe_str(var.get("left_anchor_rule_reason")) if var is not None else "",
                "approved_for_daily": False,
                "production_readiness": PRODUCTION_READINESS,
                "generated_at": generated_at,
            }
        )
    return pd.DataFrame(rows, columns=DETAIL_COLUMNS)


def event_metrics(sample: pd.DataFrame) -> dict[str, Any]:
    mature = sample[bool_series(sample["a_mature"])].copy()
    returns = pd.to_numeric(mature["a_return_pct"], errors="coerce").dropna()
    wins = int((returns > 0).sum()) if not returns.empty else 0
    return {
        "sample_size": len(sample),
        "unique_stocks": sample["stock_id"].nunique() if not sample.empty else 0,
        "breakout_signal_count": int(sample["breakout_date"].astype(str).ne("").sum()) if not sample.empty else 0,
        "late_breakout_not_w_count": int(bool_series(sample["late_breakout_not_w"]).sum()) if not sample.empty else 0,
        "post_confirmation_count": int(sample["post_confirmation_trigger_id"].astype(str).ne("").sum()) if not sample.empty else 0,
        "mature_sample_size": len(mature),
        "win_count": wins,
        "win_rate_pct": pct_round(wins / len(returns) * 100.0 if len(returns) else math.nan, 4),
        "avg_a_return_pct": pct_round(float(returns.mean()) if len(returns) else math.nan, 4),
        "median_a_return_pct": pct_round(float(returns.median()) if len(returns) else math.nan, 4),
        "tdcc_any_age7_count": int(bool_series(sample["tdcc_any_age7"]).sum()) if not sample.empty else 0,
    }


def sample_warning(mature_sample_size: int) -> str:
    if mature_sample_size < 30:
        return "low_mature_sample_size;research_only"
    if mature_sample_size < 100:
        return "medium_mature_sample_size;research_only"
    return "research_only"


def summary_row(
    *,
    summary_type: str,
    event_set_id: str,
    comparison_status: str,
    sample_mode: str,
    metrics: dict[str, Any],
    baseline_metrics: dict[str, Any] | None,
    generated_at: str,
) -> dict[str, Any]:
    baseline_sample_size = "" if baseline_metrics is None else baseline_metrics["sample_size"]
    baseline_mature_size = "" if baseline_metrics is None else baseline_metrics["mature_sample_size"]
    delta_sample_size = ""
    delta_win_rate = ""
    delta_avg_return = ""
    if baseline_metrics is not None and event_set_id != BASELINE_EVENT_SET_ID:
        delta_sample_size = metrics["sample_size"] - baseline_metrics["sample_size"]
        metric_win = safe_float(metrics["win_rate_pct"])
        baseline_win = safe_float(baseline_metrics["win_rate_pct"])
        if not math.isnan(metric_win) and not math.isnan(baseline_win):
            delta_win_rate = pct_round(metric_win - baseline_win, 4)
        metric_avg = safe_float(metrics["avg_a_return_pct"])
        baseline_avg = safe_float(baseline_metrics["avg_a_return_pct"])
        if not math.isnan(metric_avg) and not math.isnan(baseline_avg):
            delta_avg_return = pct_round(metric_avg - baseline_avg, 4)
    return {
        "model_id": MODEL_ID,
        "confirmation_model_id": CONFIRMATION_MODEL_ID,
        "overlay_model_id": OVERLAY_MODEL_ID,
        "research_id": RESEARCH_ID,
        "source_research_id": SOURCE_RESEARCH_ID,
        "research_variant_id": RESEARCH_VARIANT_ID,
        "parameter_set_id": PARAMETER_SET_ID,
        "advisory_status": RESEARCH_VARIANT_ID,
        "summary_type": summary_type,
        "event_set_id": event_set_id,
        "comparison_status": comparison_status,
        "sample_mode": sample_mode,
        "symmetry_ratio": PRIMARY_SYMMETRY_RATIO,
        "sample_size": metrics["sample_size"],
        "unique_stocks": metrics["unique_stocks"],
        "breakout_signal_count": metrics["breakout_signal_count"],
        "late_breakout_not_w_count": metrics["late_breakout_not_w_count"],
        "post_confirmation_count": metrics["post_confirmation_count"],
        "mature_sample_size": metrics["mature_sample_size"],
        "win_count": metrics["win_count"],
        "win_rate_pct": metrics["win_rate_pct"],
        "avg_a_return_pct": metrics["avg_a_return_pct"],
        "median_a_return_pct": metrics["median_a_return_pct"],
        "tdcc_any_age7_count": metrics["tdcc_any_age7_count"],
        "baseline_sample_size": baseline_sample_size,
        "baseline_mature_sample_size": baseline_mature_size,
        "delta_sample_size_vs_baseline": delta_sample_size,
        "delta_win_rate_pct_vs_baseline": delta_win_rate,
        "delta_avg_a_return_pct_vs_baseline": delta_avg_return,
        "sample_warning": sample_warning(int(metrics["mature_sample_size"])),
        "approved_for_daily": False,
        "production_readiness": PRODUCTION_READINESS,
        "generated_at": generated_at,
    }


def build_summary(baseline_events: pd.DataFrame, variant_events: pd.DataFrame, detail: pd.DataFrame, generated_at: str) -> pd.DataFrame:
    baseline = comparable_events(baseline_events)
    variant = comparable_events(variant_events)
    baseline_metrics = event_metrics(baseline)
    variant_metrics = event_metrics(variant)
    rows = [
        summary_row(
            summary_type="event_set",
            event_set_id=BASELINE_EVENT_SET_ID,
            comparison_status="",
            sample_mode="dedup_approx_20_trading_days",
            metrics=baseline_metrics,
            baseline_metrics=baseline_metrics,
            generated_at=generated_at,
        ),
        summary_row(
            summary_type="event_set",
            event_set_id=VARIANT_EVENT_SET_ID,
            comparison_status="",
            sample_mode="dedup_approx_20_trading_days",
            metrics=variant_metrics,
            baseline_metrics=baseline_metrics,
            generated_at=generated_at,
        ),
    ]
    for status in ["all_union", "common", "variant_only", "baseline_only"]:
        subset = detail if status == "all_union" else detail[detail["comparison_status"].eq(status)].copy()
        metrics = {
            "sample_size": len(subset),
            "unique_stocks": subset["stock_id"].nunique() if not subset.empty else 0,
            "breakout_signal_count": "",
            "late_breakout_not_w_count": "",
            "post_confirmation_count": "",
            "mature_sample_size": 0,
            "win_count": 0,
            "win_rate_pct": "",
            "avg_a_return_pct": "",
            "median_a_return_pct": "",
            "tdcc_any_age7_count": "",
        }
        rows.append(
            summary_row(
                summary_type="candidate_set_comparison",
                event_set_id="baseline_vs_variant",
                comparison_status=status,
                sample_mode="dedup_approx_20_trading_days",
                metrics=metrics,
                baseline_metrics=baseline_metrics,
                generated_at=generated_at,
            )
        )
    return pd.DataFrame(rows, columns=SUMMARY_COLUMNS)


def write_markdown(summary: pd.DataFrame, detail: pd.DataFrame, generated_at: str) -> None:
    event_set = summary[summary["summary_type"].eq("event_set")].copy()
    comparison = summary[summary["summary_type"].eq("candidate_set_comparison")].copy()
    variant_only = detail[detail["comparison_status"].eq("variant_only")].copy()
    variant_only = variant_only.sort_values(["signal_date", "stock_id"])
    lines = [
        "# W-Bottom Nearest Micro Anchor Event Replay",
        "",
        f"- generated_at: `{generated_at}`",
        f"- model_id: `{MODEL_ID}`",
        f"- confirmation_model_id: `{CONFIRMATION_MODEL_ID}`",
        f"- overlay_model_id: `{OVERLAY_MODEL_ID}`",
        f"- research_id: `{RESEARCH_ID}`",
        f"- source_research_id: `{SOURCE_RESEARCH_ID}`",
        f"- tested_left_anchor_rule_id: `{LEFT_ANCHOR_RULE_ID}`",
        "- scope: research/backtest only; `approved_for_daily=False` and `not_production_ready_research_only`.",
        "- production impact: `none`; this does not modify daily model conditions, scoring, ranking, PDF consumers, or production baselines.",
        "",
        "## Event Set Summary",
        "",
        *markdown_table(
            event_set,
            [
                "event_set_id",
                "sample_size",
                "unique_stocks",
                "breakout_signal_count",
                "mature_sample_size",
                "win_rate_pct",
                "avg_a_return_pct",
                "delta_sample_size_vs_baseline",
                "delta_win_rate_pct_vs_baseline",
                "delta_avg_a_return_pct_vs_baseline",
                "sample_warning",
            ],
            20,
        ),
        "",
        "## Candidate Set Comparison",
        "",
        *markdown_table(
            comparison,
            ["comparison_status", "sample_size", "unique_stocks", "sample_warning"],
            20,
        ),
        "",
        "## Variant-Only Sample",
        "",
        *markdown_table(
            variant_only,
            [
                "stock_id",
                "stock_name",
                "signal_date",
                "variant_left_peak_date",
                "variant_left_low_date",
                "variant_neckline_date",
                "variant_right_low_date",
                "variant_breakout_date",
                "variant_a_return_pct",
            ],
            30,
        ),
        "",
        "## Interpretation Guardrails",
        "",
        "- This is a candidate event replay, not a production model promotion.",
        "- The production-like 180-trading-day history gate remains active; manual positive examples are not force-added.",
        "- Only the left anchor selector changes from the current detector to nearest micro pressure high in the 45-trading-day window.",
        "- A better-looking anchor is insufficient for promotion unless it improves stable event outcomes across broader samples.",
    ]
    LATEST_MD.parent.mkdir(parents=True, exist_ok=True)
    LATEST_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    generated_at = now_text()
    tdcc_index = w_bottom.load_tdcc_index()
    all_rows: list[dict[str, Any]] = []
    price_files = sorted(w_bottom.PRICE_DIR.glob("*.csv"))
    for index, path in enumerate(price_files, start=1):
        try:
            price = pd.read_csv(path, dtype={"stock_id": str}, keep_default_na=False)
        except Exception:
            continue
        required = {"date", "stock_id", "stock_name", "open", "high", "low", "close", "volume"}
        if not required.issubset(price.columns):
            continue
        price = w_bottom.add_price_metrics(price).sort_values("date").reset_index(drop=True)
        all_rows.extend(build_variant_event_rows(price, tdcc_index, generated_at))
        if index % 250 == 0:
            print(f"progress price_files={index}/{len(price_files)} variant_event_rows={len(all_rows)}", flush=True)

    events = pd.DataFrame(all_rows, columns=EVENT_COLUMNS)
    if events.empty:
        raise SystemExit("ERROR: no nearest-micro W-bottom event replay rows generated")
    events = w_bottom.mark_dedup(events)
    baseline_events = load_baseline_events()
    detail = build_comparison_detail(baseline_events, events, generated_at)
    summary = build_summary(baseline_events, events, detail, generated_at)
    if detail.empty or summary.empty:
        raise SystemExit("ERROR: no nearest-micro W-bottom event replay comparison generated")

    write_csv(events, LATEST_EVENTS_CSV)
    write_csv(events, HISTORY_EVENTS_CSV)
    write_csv(detail, LATEST_DETAIL_CSV)
    write_csv(detail, HISTORY_DETAIL_CSV)
    write_csv(summary, LATEST_SUMMARY_CSV)
    write_csv(summary, HISTORY_SUMMARY_CSV)
    write_markdown(summary, detail, generated_at)

    print(f"Saved: {LATEST_EVENTS_CSV} rows={len(events)}")
    print(f"Saved: {LATEST_DETAIL_CSV} rows={len(detail)}")
    print(f"Saved: {LATEST_SUMMARY_CSV} rows={len(summary)}")
    print(f"Saved: {LATEST_MD}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
