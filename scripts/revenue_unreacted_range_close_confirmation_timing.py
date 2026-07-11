from __future__ import annotations

import math
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import numpy as np
import pandas as pd

from tracking_utils import DOCS_LATEST_DIR, RESEARCH_LATEST_DIR, markdown_table, now_text, safe_str, write_csv


HISTORY_DIR = Path("output/history/research")

ARTIFACT_ID = "revenue_unreacted_range_close_confirmation_timing_audit"
ARTIFACT_VERSION = "close_confirmation_timing_v1"
MODEL_ID = "revenue_unreacted_range"
MODEL_NAME_ZH = "營收爆發但股價尚未反應模型"

SUMMARY_CSV = RESEARCH_LATEST_DIR / f"{ARTIFACT_ID}_latest.csv"
DETAIL_CSV = RESEARCH_LATEST_DIR / f"{ARTIFACT_ID}_detail_latest.csv"
ANOMALY_CSV = RESEARCH_LATEST_DIR / f"{ARTIFACT_ID}_anomaly_audit_latest.csv"
SUMMARY_MD = RESEARCH_LATEST_DIR / f"{ARTIFACT_ID}_latest.md"
HISTORY_SUMMARY_CSV = HISTORY_DIR / f"{ARTIFACT_ID}.csv"
HISTORY_ANOMALY_CSV = HISTORY_DIR / f"{ARTIFACT_ID}_anomaly_audit.csv"
DOCS_SUMMARY_CSV = DOCS_LATEST_DIR / SUMMARY_CSV.name
DOCS_ANOMALY_CSV = DOCS_LATEST_DIR / ANOMALY_CSV.name
DOCS_SUMMARY_MD = DOCS_LATEST_DIR / SUMMARY_MD.name

DECISION_BASIS = "excluding_known_revenue_and_price_anomalies"
INCLUDING_BASIS = "including_known_anomalies"

WIN_RETURN_PCT = 5.0
HIGH_RETURN_PCT = 8.0
LARGE_LOSS_PCT = -5.0
FIXED_HORIZON_DAYS = 20
MAX_PENDING_WINDOW_DAYS = 10


@dataclass(frozen=True)
class ConfirmationSpec:
    confirmation_variant_id: str
    confirmation_variant_name_zh: str
    confirmation_rule: str
    pending_windows: tuple[int, ...]


@dataclass(frozen=True)
class ExitClockSpec:
    exit_clock_id: str
    exit_clock_name_zh: str
    exit_rule: str


CONTROL_SPEC = ConfirmationSpec(
    confirmation_variant_id="signal_close_control",
    confirmation_variant_name_zh="訊號日直接進場對照組",
    confirmation_rule="候選條件於訊號日收盤成立，不等待額外確認；僅供研究對照，不是新模型。",
    pending_windows=(0,),
)

CONFIRMATION_SPECS = (
    ConfirmationSpec(
        confirmation_variant_id="next_day_close_continuation",
        confirmation_variant_name_zh="隔日續強確認型",
        confirmation_rule="訊號後第一個交易日收盤價高於訊號日收盤價。",
        pending_windows=(1,),
    ),
    ConfirmationSpec(
        confirmation_variant_id="range23_highest_close_breakout",
        confirmation_variant_name_zh="區間突破確認型",
        confirmation_rule="等待期間內第一次收盤突破訊號日前 23 個交易日最高收盤價。",
        pending_windows=(3, 5, 10),
    ),
    ConfirmationSpec(
        confirmation_variant_id="ma20_ema23_close_reclaim",
        confirmation_variant_name_zh="均線站回確認型",
        confirmation_rule="等待期間內第一次收盤同時高於當日 MA20 與 EMA23。",
        pending_windows=(3, 5, 10),
    ),
)

EXIT_CLOCK_SPECS = (
    ExitClockSpec(
        exit_clock_id="signal_d20_close",
        exit_clock_name_zh="維持原訊號日 D+20 收盤",
        exit_rule="確認後次一交易日開盤進場，但仍於原訊號日後第 20 個交易日收盤出場。",
    ),
    ExitClockSpec(
        exit_clock_id="confirmation_d20_close",
        exit_clock_name_zh="確認日 D+20 收盤",
        exit_rule="確認後次一交易日開盤進場，於確認日後第 20 個交易日收盤出場。",
    ),
)


EPISODE_COLUMNS = [
    "generated_at",
    "model_id",
    "model_name_zh",
    "research_artifact_id",
    "artifact_version",
    "anomaly_exclusion_basis",
    "decision_basis",
    "episode_key",
    "stock_id",
    "stock_name",
    "market",
    "signal_date",
    "signal_sequence_index",
    "confirmation_variant_id",
    "confirmation_variant_name_zh",
    "confirmation_rule",
    "pending_window_days",
    "exit_clock_id",
    "exit_clock_name_zh",
    "exit_rule",
    "confirmation_status",
    "lifecycle_status",
    "confirmation_date",
    "confirmation_sequence_index",
    "confirmation_delay_trading_days",
    "entry_date",
    "entry_sequence_index",
    "entry_price",
    "exit_date",
    "exit_sequence_index",
    "exit_price",
    "realized_return_pct",
    "outcome_label",
    "high_return_8_flag",
    "loss_5_flag",
    "metric_included",
    "price_path_anomaly_flag",
    "price_path_anomaly_reason",
    "price_path_max_step_ratio",
    "price_path_min_step_ratio",
    "direct_signal_d20_return_pct",
    "direct_signal_d20_outcome_label",
    "direct_signal_d20_path_anomaly_flag",
    "direct_signal_d20_path_anomaly_reason",
    "timing_cost_vs_direct_signal_d20_pct",
    "signal_close",
    "signal_range23_highest_close",
    "signal_already_above_ma20_ema23",
    "suppressed_source_signal_count",
    "same_stock_non_overlap_applied",
    "known_before_entry_open",
    "uses_post_entry_information",
    "timing_information_cutoff",
    "full_monthly_revenue_period",
    "full_monthly_revenue_source_table_date",
    "full_monthly_revenue_latest_yoy_pct",
    "full_monthly_revenue_cumulative_yoy_pct",
    "source_revenue_or_price_anomaly_flag",
    "approved_for_daily",
    "production_change",
    "promotion_readiness",
]


DETAIL_COLUMNS = [
    "model_id",
    "research_artifact_id",
    "decision_basis",
    "episode_key",
    "stock_id",
    "signal_date",
    "signal_sequence_index",
    "confirmation_variant_id",
    "pending_window_days",
    "exit_clock_id",
    "confirmation_date",
    "confirmation_sequence_index",
    "confirmation_delay_trading_days",
    "entry_date",
    "entry_sequence_index",
    "entry_price",
    "exit_date",
    "exit_sequence_index",
    "exit_price",
    "realized_return_pct",
    "outcome_label",
    "metric_included",
    "price_path_anomaly_flag",
    "price_path_anomaly_reason",
    "direct_signal_d20_return_pct",
    "direct_signal_d20_path_anomaly_flag",
    "timing_cost_vs_direct_signal_d20_pct",
    "signal_range23_highest_close",
    "signal_already_above_ma20_ema23",
    "suppressed_source_signal_count",
    "known_before_entry_open",
    "uses_post_entry_information",
    "full_monthly_revenue_period",
    "full_monthly_revenue_source_table_date",
    "full_monthly_revenue_latest_yoy_pct",
    "full_monthly_revenue_cumulative_yoy_pct",
    "approved_for_daily",
    "production_change",
]


SUMMARY_REQUIRED_ID_COLUMNS = [
    "generated_at",
    "model_id",
    "model_name_zh",
    "research_artifact_id",
    "artifact_version",
    "row_type",
    "anomaly_exclusion_basis",
    "decision_basis",
    "confirmation_variant_id",
    "confirmation_variant_name_zh",
    "pending_window_days",
    "exit_clock_id",
]


def _safe_float(value: Any) -> float:
    try:
        result = float(value)
    except (TypeError, ValueError):
        return math.nan
    return result if math.isfinite(result) else math.nan


def _round(value: Any, digits: int = 4) -> float | str:
    number = _safe_float(value)
    return "" if math.isnan(number) else round(number, digits)


def _rate(numerator: int, denominator: int) -> float | str:
    return "" if denominator <= 0 else round(numerator / denominator * 100.0, 4)


def _mean(values: pd.Series) -> float | str:
    clean = pd.to_numeric(values, errors="coerce").dropna()
    return "" if clean.empty else round(float(clean.mean()), 4)


def _median(values: pd.Series) -> float | str:
    clean = pd.to_numeric(values, errors="coerce").dropna()
    return "" if clean.empty else round(float(clean.median()), 4)


def _outcome_label(return_pct: Any) -> str:
    value = _safe_float(return_pct)
    if math.isnan(value):
        return ""
    if value >= WIN_RETURN_PCT:
        return "win"
    if value >= 0.0:
        return "neutral"
    return "failure"


def _return_metrics(frame: pd.DataFrame, column: str = "realized_return_pct") -> dict[str, Any]:
    returns = pd.to_numeric(frame.get(column, pd.Series(dtype=float)), errors="coerce").dropna()
    sample = len(returns)
    wins = int(returns.ge(WIN_RETURN_PCT).sum())
    neutrals = int((returns.ge(0.0) & returns.lt(WIN_RETURN_PCT)).sum())
    failures = int(returns.lt(0.0).sum())
    high = int(returns.ge(HIGH_RETURN_PCT).sum())
    loss = int(returns.le(LARGE_LOSS_PCT).sum())
    return {
        "accepted_trade_count": sample,
        "win_count": wins,
        "neutral_count": neutrals,
        "failure_count": failures,
        "win_rate_pct": _rate(wins, sample),
        "neutral_rate_pct": _rate(neutrals, sample),
        "failure_rate_pct": _rate(failures, sample),
        "avg_realized_return_pct": _mean(returns),
        "median_realized_return_pct": _median(returns),
        "high_return_8_count": high,
        "high_return_8_rate_pct": _rate(high, sample),
        "loss_5_count": loss,
        "loss_5_rate_pct": _rate(loss, sample),
    }


def _price_path_audit(
    part: pd.DataFrame,
    *,
    confirmation_position: int,
    entry_position: int,
    exit_position: int,
) -> tuple[bool, str, float | str, float | str]:
    if entry_position >= len(part) or exit_position >= len(part) or entry_position > exit_position:
        return False, "missing_mature_price_path", "", ""
    entry_price = _safe_float(part.iloc[entry_position].get("open"))
    confirmation_close = _safe_float(part.iloc[confirmation_position].get("close"))
    closes = pd.to_numeric(part.iloc[entry_position : exit_position + 1]["close"], errors="coerce")
    if math.isnan(entry_price) or entry_price <= 0 or closes.isna().any() or (closes <= 0).any():
        return True, "invalid_nonpositive_or_missing_price", "", ""

    levels = pd.Series([entry_price, *closes.astype(float).tolist()], dtype=float)
    ratios = levels.iloc[1:].reset_index(drop=True) / levels.iloc[:-1].reset_index(drop=True)
    if not math.isnan(confirmation_close) and confirmation_close > 0:
        ratios = pd.concat(
            [pd.Series([entry_price / confirmation_close], dtype=float), ratios],
            ignore_index=True,
        )
    maximum = float(ratios.max())
    minimum = float(ratios.min())
    upward = maximum >= 1.5
    downward = minimum <= 0.67
    if upward and downward:
        reason = "upward_and_downward_price_discontinuity"
    elif upward:
        reason = "upward_price_discontinuity_ge_1_5x"
    elif downward:
        reason = "downward_price_discontinuity_le_0_67x"
    else:
        reason = "none"
    return upward or downward, reason, _round(maximum, 6), _round(minimum, 6)


def _compute_confirmation_position(
    part: pd.DataFrame,
    *,
    signal_position: int,
    spec: ConfirmationSpec,
    pending_window_days: int,
) -> tuple[int | None, bool, bool]:
    if spec.confirmation_variant_id == CONTROL_SPEC.confirmation_variant_id:
        return signal_position, True, True

    end_position = signal_position + pending_window_days
    complete_window = end_position < len(part)
    available_end = min(end_position, len(part) - 1)
    if available_end <= signal_position:
        return None, False, False

    signal = part.iloc[signal_position]
    signal_close = _safe_float(signal.get("close"))
    range_threshold = _safe_float(signal.get("_revenue_range23_highest_close_prev"))
    all_inputs_available = True

    for position in range(signal_position + 1, available_end + 1):
        row = part.iloc[position]
        close = _safe_float(row.get("close"))
        if spec.confirmation_variant_id == "next_day_close_continuation":
            valid = not math.isnan(close) and not math.isnan(signal_close)
            all_inputs_available &= valid
            if valid and close > signal_close:
                return position, complete_window, True
        elif spec.confirmation_variant_id == "range23_highest_close_breakout":
            valid = not math.isnan(close) and not math.isnan(range_threshold)
            all_inputs_available &= valid
            if valid and close > range_threshold:
                return position, complete_window, True
        elif spec.confirmation_variant_id == "ma20_ema23_close_reclaim":
            ma20 = _safe_float(row.get("ma20"))
            ema23 = _safe_float(row.get("ema23"))
            valid = not any(math.isnan(value) for value in (close, ma20, ema23))
            all_inputs_available &= valid
            if valid and close > ma20 and close > ema23:
                return position, complete_window, True
        else:
            raise ValueError(f"Unsupported confirmation variant: {spec.confirmation_variant_id}")

    return None, complete_window, complete_window and all_inputs_available


def _confirmation_position(
    part: pd.DataFrame,
    *,
    signal_position: int,
    spec: ConfirmationSpec,
    pending_window_days: int,
    cache: dict[tuple[str, int, str, int], tuple[int | None, bool, bool]] | None = None,
) -> tuple[int | None, bool, bool]:
    stock_id = safe_str(part.iloc[0].get("stock_id")) if not part.empty else ""
    key = (stock_id, signal_position, spec.confirmation_variant_id, pending_window_days)
    if cache is not None and key in cache:
        return cache[key]
    result = _compute_confirmation_position(
        part,
        signal_position=signal_position,
        spec=spec,
        pending_window_days=pending_window_days,
    )
    if cache is not None:
        cache[key] = result
    return result


def _exit_position(
    *,
    signal_position: int,
    confirmation_position: int,
    exit_clock: ExitClockSpec,
) -> int:
    if exit_clock.exit_clock_id == "signal_d20_close":
        return signal_position + FIXED_HORIZON_DAYS
    if exit_clock.exit_clock_id == "confirmation_d20_close":
        return confirmation_position + FIXED_HORIZON_DAYS
    raise ValueError(f"Unsupported exit clock: {exit_clock.exit_clock_id}")


def _direct_signal_d20_outcome(
    part: pd.DataFrame,
    *,
    signal_position: int,
    cache: dict[tuple[str, int], tuple[float | str, str, bool, str]] | None = None,
) -> tuple[float | str, str, bool, str]:
    stock_id = safe_str(part.iloc[0].get("stock_id")) if not part.empty else ""
    key = (stock_id, signal_position)
    if cache is not None and key in cache:
        return cache[key]
    entry_position = signal_position + 1
    exit_position = signal_position + FIXED_HORIZON_DAYS
    if entry_position >= len(part) or exit_position >= len(part):
        result = ("", "", False, "missing_mature_price_path")
        if cache is not None:
            cache[key] = result
        return result
    entry_price = _safe_float(part.iloc[entry_position].get("open"))
    exit_price = _safe_float(part.iloc[exit_position].get("close"))
    if any(math.isnan(value) or value <= 0 for value in (entry_price, exit_price)):
        result = ("", "", True, "invalid_nonpositive_or_missing_price")
        if cache is not None:
            cache[key] = result
        return result
    result = (exit_price / entry_price - 1.0) * 100.0
    path_flag, path_reason, _, _ = _price_path_audit(
        part,
        confirmation_position=signal_position,
        entry_position=entry_position,
        exit_position=exit_position,
    )
    outcome = (_round(result), _outcome_label(result), path_flag, path_reason)
    if cache is not None:
        cache[key] = outcome
    return outcome


def _episode_row(
    part: pd.DataFrame,
    *,
    signal_position: int,
    spec: ConfirmationSpec,
    pending_window_days: int,
    exit_clock: ExitClockSpec,
    basis: str,
    suppressed_count: int,
    confirmation_position: int | None,
    complete_confirmation_window: bool,
    confirmation_evaluable: bool,
    generated_at: str,
    direct_outcome_cache: dict[tuple[str, int], tuple[float | str, str, bool, str]],
    trade_outcome_cache: dict[
        tuple[str, int, int],
        tuple[float | str, float | str, float | str, str, bool, str, float | str, float | str],
    ],
) -> dict[str, Any]:
    signal = part.iloc[signal_position]
    stock_id = safe_str(signal.get("stock_id"))
    signal_date = safe_str(signal.get("_revenue_signal_date", signal.get("date")))
    signal_sequence = int(signal.get("_revenue_stock_sequence_index", signal_position))
    source_anomaly = bool(signal.get("_revenue_timing_source_anomaly_flag", False))
    direct_return, direct_outcome, direct_path_flag, direct_path_reason = _direct_signal_d20_outcome(
        part,
        signal_position=signal_position,
        cache=direct_outcome_cache,
    )

    confirmation_status = "confirmed" if confirmation_position is not None else (
        "unconfirmed" if complete_confirmation_window and confirmation_evaluable else "not_evaluable"
    )
    confirmation_date = ""
    confirmation_sequence: int | str = ""
    confirmation_delay: int | str = ""
    entry_date = ""
    entry_sequence: int | str = ""
    entry_price: float | str = ""
    exit_date = ""
    exit_sequence: int | str = ""
    exit_price: float | str = ""
    realized_return: float | str = ""
    outcome = ""
    path_flag = False
    path_reason = "not_applicable_unconfirmed"
    path_max: float | str = ""
    path_min: float | str = ""
    lifecycle_status = "unconfirmed" if confirmation_status == "unconfirmed" else "confirmation_not_evaluable"
    known_before_entry_open = False

    if confirmation_position is not None:
        confirmation = part.iloc[confirmation_position]
        confirmation_date = safe_str(confirmation.get("_revenue_signal_date", confirmation.get("date")))
        confirmation_sequence = int(confirmation.get("_revenue_stock_sequence_index", confirmation_position))
        confirmation_delay = confirmation_position - signal_position
        entry_position = confirmation_position + 1
        planned_exit_position = _exit_position(
            signal_position=signal_position,
            confirmation_position=confirmation_position,
            exit_clock=exit_clock,
        )
        known_before_entry_open = entry_position < len(part)
        if entry_position < len(part):
            entry = part.iloc[entry_position]
            entry_date = safe_str(entry.get("_revenue_signal_date", entry.get("date")))
            entry_sequence = int(entry.get("_revenue_stock_sequence_index", entry_position))
            entry_price = _round(entry.get("open"))
        if entry_position < len(part) and planned_exit_position < len(part):
            exit_row = part.iloc[planned_exit_position]
            exit_date = safe_str(exit_row.get("_revenue_signal_date", exit_row.get("date")))
            exit_sequence = int(exit_row.get("_revenue_stock_sequence_index", planned_exit_position))
            trade_key = (stock_id, confirmation_position, planned_exit_position)
            cached_trade = trade_outcome_cache.get(trade_key)
            if cached_trade is None:
                exit_price = _round(exit_row.get("close"))
                entry_number = _safe_float(entry_price)
                exit_number = _safe_float(exit_price)
                if not math.isnan(entry_number) and entry_number > 0 and not math.isnan(exit_number) and exit_number > 0:
                    realized_return = _round((exit_number / entry_number - 1.0) * 100.0)
                    outcome = _outcome_label(realized_return)
                    path_flag, path_reason, path_max, path_min = _price_path_audit(
                        part,
                        confirmation_position=confirmation_position,
                        entry_position=entry_position,
                        exit_position=planned_exit_position,
                    )
                    lifecycle_status = "confirmed_mature"
                else:
                    path_flag = True
                    path_reason = "invalid_nonpositive_or_missing_price"
                    lifecycle_status = "confirmed_invalid_price"
                cached_trade = (
                    entry_price,
                    exit_price,
                    realized_return,
                    outcome,
                    path_flag,
                    path_reason,
                    path_max,
                    path_min,
                )
                trade_outcome_cache[trade_key] = cached_trade
            (
                entry_price,
                exit_price,
                realized_return,
                outcome,
                path_flag,
                path_reason,
                path_max,
                path_min,
            ) = cached_trade
            lifecycle_status = (
                "confirmed_invalid_price"
                if path_reason == "invalid_nonpositive_or_missing_price"
                else "confirmed_mature"
            )
        else:
            path_reason = "missing_mature_price_path"
            lifecycle_status = "confirmed_immature_exit"

    decision_basis = basis == DECISION_BASIS
    metric_included = lifecycle_status == "confirmed_mature" and not (decision_basis and path_flag)
    direct_number = _safe_float(direct_return)
    realized_number = _safe_float(realized_return)
    timing_cost = (
        _round(realized_number - direct_number)
        if not math.isnan(realized_number) and not math.isnan(direct_number)
        else ""
    )
    signal_close = _safe_float(signal.get("close"))
    signal_ma20 = _safe_float(signal.get("ma20"))
    signal_ema23 = _safe_float(signal.get("ema23"))
    already_above = (
        not any(math.isnan(value) for value in (signal_close, signal_ma20, signal_ema23))
        and signal_close > signal_ma20
        and signal_close > signal_ema23
    )

    return {
        "generated_at": generated_at,
        "model_id": MODEL_ID,
        "model_name_zh": MODEL_NAME_ZH,
        "research_artifact_id": ARTIFACT_ID,
        "artifact_version": ARTIFACT_VERSION,
        "anomaly_exclusion_basis": basis,
        "decision_basis": decision_basis,
        "episode_key": "|".join(
            [
                stock_id,
                signal_date,
                spec.confirmation_variant_id,
                str(pending_window_days),
                exit_clock.exit_clock_id,
            ]
        ),
        "stock_id": stock_id,
        "stock_name": safe_str(signal.get("stock_name")),
        "market": safe_str(signal.get("market")),
        "signal_date": signal_date,
        "signal_sequence_index": signal_sequence,
        "confirmation_variant_id": spec.confirmation_variant_id,
        "confirmation_variant_name_zh": spec.confirmation_variant_name_zh,
        "confirmation_rule": spec.confirmation_rule,
        "pending_window_days": pending_window_days,
        "exit_clock_id": exit_clock.exit_clock_id,
        "exit_clock_name_zh": exit_clock.exit_clock_name_zh,
        "exit_rule": exit_clock.exit_rule,
        "confirmation_status": confirmation_status,
        "lifecycle_status": lifecycle_status,
        "confirmation_date": confirmation_date,
        "confirmation_sequence_index": confirmation_sequence,
        "confirmation_delay_trading_days": confirmation_delay,
        "entry_date": entry_date,
        "entry_sequence_index": entry_sequence,
        "entry_price": entry_price,
        "exit_date": exit_date,
        "exit_sequence_index": exit_sequence,
        "exit_price": exit_price,
        "realized_return_pct": realized_return,
        "outcome_label": outcome,
        "high_return_8_flag": not math.isnan(realized_number) and realized_number >= HIGH_RETURN_PCT,
        "loss_5_flag": not math.isnan(realized_number) and realized_number <= LARGE_LOSS_PCT,
        "metric_included": metric_included,
        "price_path_anomaly_flag": path_flag,
        "price_path_anomaly_reason": path_reason,
        "price_path_max_step_ratio": path_max,
        "price_path_min_step_ratio": path_min,
        "direct_signal_d20_return_pct": direct_return,
        "direct_signal_d20_outcome_label": direct_outcome,
        "direct_signal_d20_path_anomaly_flag": direct_path_flag,
        "direct_signal_d20_path_anomaly_reason": direct_path_reason,
        "timing_cost_vs_direct_signal_d20_pct": timing_cost,
        "signal_close": _round(signal_close),
        "signal_range23_highest_close": _round(signal.get("_revenue_range23_highest_close_prev")),
        "signal_already_above_ma20_ema23": already_above,
        "suppressed_source_signal_count": suppressed_count,
        "same_stock_non_overlap_applied": True,
        "known_before_entry_open": known_before_entry_open,
        "uses_post_entry_information": False,
        "timing_information_cutoff": "confirmation_date_close_before_entry_next_open",
        "full_monthly_revenue_period": safe_str(signal.get("full_monthly_revenue_period")),
        "full_monthly_revenue_source_table_date": safe_str(
            signal.get("full_monthly_revenue_source_table_date")
        ),
        "full_monthly_revenue_latest_yoy_pct": _round(
            signal.get("full_monthly_revenue_latest_yoy_pct")
        ),
        "full_monthly_revenue_cumulative_yoy_pct": _round(
            signal.get("full_monthly_revenue_cumulative_yoy_pct")
        ),
        "source_revenue_or_price_anomaly_flag": source_anomaly,
        "approved_for_daily": False,
        "production_change": "none",
        "promotion_readiness": "research_only_not_promotion_ready",
    }


def _replay_variant(
    frame: pd.DataFrame,
    *,
    source_mask: pd.Series,
    spec: ConfirmationSpec,
    pending_window_days: int,
    exit_clock: ExitClockSpec,
    basis: str,
    generated_at: str,
    confirmation_cache: dict[tuple[str, int, str, int], tuple[int | None, bool, bool]],
    direct_outcome_cache: dict[tuple[str, int], tuple[float | str, str, bool, str]],
    trade_outcome_cache: dict[
        tuple[str, int, int],
        tuple[float | str, float | str, float | str, str, bool, str, float | str, float | str],
    ],
) -> pd.DataFrame:
    rows: list[dict[str, Any]] = []
    sorted_frame = frame.sort_values(
        ["stock_id", "_revenue_stock_sequence_index"],
        kind="mergesort",
    ).copy()
    sorted_mask = source_mask.reindex(sorted_frame.index).fillna(False).astype(bool)

    for _, original_part in sorted_frame.groupby("stock_id", sort=False, dropna=False):
        original_indices = original_part.index
        part = original_part.reset_index(drop=True)
        part_source_mask = sorted_mask.loc[original_indices].to_numpy(dtype=bool)
        source_positions = np.flatnonzero(part_source_mask)
        cursor = 0
        while cursor < len(source_positions):
            signal_position = int(source_positions[cursor])
            confirmation_position, complete_window, evaluable = _confirmation_position(
                part,
                signal_position=signal_position,
                spec=spec,
                pending_window_days=pending_window_days,
                cache=confirmation_cache,
            )
            if confirmation_position is None:
                lifecycle_end = min(signal_position + pending_window_days, len(part) - 1)
            else:
                planned_exit = _exit_position(
                    signal_position=signal_position,
                    confirmation_position=confirmation_position,
                    exit_clock=exit_clock,
                )
                lifecycle_end = min(planned_exit, len(part) - 1)
            next_cursor = int(np.searchsorted(source_positions, lifecycle_end, side="right"))
            suppressed_count = max(0, next_cursor - cursor - 1)
            rows.append(
                _episode_row(
                    part,
                    signal_position=signal_position,
                    spec=spec,
                    pending_window_days=pending_window_days,
                    exit_clock=exit_clock,
                    basis=basis,
                    suppressed_count=suppressed_count,
                    confirmation_position=confirmation_position,
                    complete_confirmation_window=complete_window,
                    confirmation_evaluable=evaluable,
                    generated_at=generated_at,
                    direct_outcome_cache=direct_outcome_cache,
                    trade_outcome_cache=trade_outcome_cache,
                )
            )
            cursor = max(cursor + 1, next_cursor)

    return pd.DataFrame(rows, columns=EPISODE_COLUMNS)


def _anomaly_metrics(episodes: pd.DataFrame) -> dict[str, Any]:
    mature = episodes[episodes["lifecycle_status"].eq("confirmed_mature")].copy()
    raw_returns = pd.to_numeric(mature["realized_return_pct"], errors="coerce").dropna()
    path_anomaly_count = int(mature["price_path_anomaly_flag"].astype(bool).sum()) if not mature.empty else 0
    metric = episodes[episodes["metric_included"].astype(bool)].copy()
    returns = pd.to_numeric(metric["realized_return_pct"], errors="coerce").dropna()
    if returns.empty:
        return {
            "accepted_trade_count_before_path_exclusion": len(raw_returns),
            "price_path_anomaly_count": path_anomaly_count,
            "metric_sample_count": 0,
            "max_realized_return_pct": "",
            "max_return_stock_id": "",
            "max_return_signal_date": "",
            "min_realized_return_pct": "",
            "min_return_stock_id": "",
            "min_return_signal_date": "",
            "return_abs_ge80_count": 0,
            "top1_abs_return_share_pct": "",
            "top5_abs_return_share_pct": "",
            "trimmed_1pct_avg_return_pct": "",
            "potential_return_dominance_flag": False,
        }

    abs_returns = returns.abs().sort_values(ascending=False)
    abs_total = float(abs_returns.sum())
    max_index = returns.idxmax()
    min_index = returns.idxmin()
    trim_count = int(math.floor(len(returns) * 0.01))
    trimmed = returns.sort_values()
    if trim_count > 0 and len(trimmed) > trim_count * 2:
        trimmed = trimmed.iloc[trim_count:-trim_count]
    top1 = float(abs_returns.iloc[:1].sum()) / abs_total * 100.0 if abs_total else 0.0
    top5 = float(abs_returns.iloc[:5].sum()) / abs_total * 100.0 if abs_total else 0.0
    dominance = top1 > 10.0 or top5 > 25.0
    return {
        "accepted_trade_count_before_path_exclusion": len(raw_returns),
        "price_path_anomaly_count": path_anomaly_count,
        "metric_sample_count": len(returns),
        "max_realized_return_pct": _round(returns.loc[max_index]),
        "max_return_stock_id": safe_str(metric.loc[max_index, "stock_id"]),
        "max_return_signal_date": safe_str(metric.loc[max_index, "signal_date"]),
        "min_realized_return_pct": _round(returns.loc[min_index]),
        "min_return_stock_id": safe_str(metric.loc[min_index, "stock_id"]),
        "min_return_signal_date": safe_str(metric.loc[min_index, "signal_date"]),
        "return_abs_ge80_count": int(returns.abs().ge(80.0).sum()),
        "top1_abs_return_share_pct": _round(top1),
        "top5_abs_return_share_pct": _round(top5),
        "trimmed_1pct_avg_return_pct": _mean(trimmed),
        "potential_return_dominance_flag": dominance,
    }


def _performance_summary(
    episodes: pd.DataFrame,
    *,
    source_signal_count: int,
    source_unique_stock_count: int,
    source_anomaly_count: int,
    spec: ConfirmationSpec,
    pending_window_days: int,
    exit_clock: ExitClockSpec,
    basis: str,
    generated_at: str,
) -> tuple[dict[str, Any], dict[str, Any]]:
    confirmed = episodes[episodes["confirmation_status"].eq("confirmed")]
    unconfirmed = episodes[episodes["confirmation_status"].eq("unconfirmed")]
    not_evaluable = episodes[episodes["confirmation_status"].eq("not_evaluable")]
    entered = confirmed[confirmed["entry_date"].astype(str).ne("")]
    metrics = _return_metrics(episodes[episodes["metric_included"].astype(bool)])
    confirmation_denominator = len(confirmed) + len(unconfirmed)
    unconfirmed_counterfactual = unconfirmed.copy()
    if basis == DECISION_BASIS:
        unconfirmed_counterfactual = unconfirmed_counterfactual[
            ~unconfirmed_counterfactual["direct_signal_d20_path_anomaly_flag"].astype(bool)
        ]
    unconfirmed_counterfactual = unconfirmed_counterfactual[
        pd.to_numeric(unconfirmed_counterfactual["direct_signal_d20_return_pct"], errors="coerce").notna()
    ]
    counterfactual_metrics = _return_metrics(
        unconfirmed_counterfactual,
        column="direct_signal_d20_return_pct",
    )
    paired = episodes[
        episodes["metric_included"].astype(bool)
        & pd.to_numeric(episodes["direct_signal_d20_return_pct"], errors="coerce").notna()
    ].copy()
    if basis == DECISION_BASIS:
        paired = paired[~paired["direct_signal_d20_path_anomaly_flag"].astype(bool)]
    timing_cost = pd.to_numeric(paired["timing_cost_vs_direct_signal_d20_pct"], errors="coerce")
    suppressed = int(pd.to_numeric(episodes["suppressed_source_signal_count"], errors="coerce").fillna(0).sum())
    anomaly = _anomaly_metrics(episodes)
    decision_basis = basis == DECISION_BASIS
    dominance = bool(anomaly["potential_return_dominance_flag"])
    promotion_readiness = (
        "research_only_blocked_return_dominance_review"
        if decision_basis and dominance
        else "research_only_not_promotion_ready"
    )
    row = {
        "generated_at": generated_at,
        "model_id": MODEL_ID,
        "model_name_zh": MODEL_NAME_ZH,
        "research_artifact_id": ARTIFACT_ID,
        "artifact_version": ARTIFACT_VERSION,
        "row_type": "control_baseline" if spec == CONTROL_SPEC else "variant_performance",
        "anomaly_exclusion_basis": basis,
        "decision_basis": decision_basis,
        "confirmation_variant_id": spec.confirmation_variant_id,
        "confirmation_variant_name_zh": spec.confirmation_variant_name_zh,
        "confirmation_rule": spec.confirmation_rule,
        "pending_window_days": pending_window_days,
        "exit_clock_id": exit_clock.exit_clock_id,
        "exit_clock_name_zh": exit_clock.exit_clock_name_zh,
        "exit_rule": exit_clock.exit_rule,
        "candidate_source_name_zh": "營收爆發但股價尚未反應候選池",
        "candidate_source_rule": (
            "canonical monthly revenue as-of strong condition plus recent 23-day range/no-active-attack proxy"
        ),
        "point_in_time_rule": "monthly revenue source_table_date <= signal_date",
        "source_signal_count": source_signal_count,
        "source_unique_stock_count": source_unique_stock_count,
        "source_known_anomaly_count": source_anomaly_count,
        "pending_episode_count": len(episodes),
        "confirmed_episode_count": len(confirmed),
        "unconfirmed_episode_count": len(unconfirmed),
        "not_evaluable_episode_count": len(not_evaluable),
        "confirmation_rate_pct": _rate(len(confirmed), confirmation_denominator),
        "avg_confirmation_delay_trading_days": _mean(confirmed["confirmation_delay_trading_days"]),
        "median_confirmation_delay_trading_days": _median(confirmed["confirmation_delay_trading_days"]),
        "suppressed_source_signal_count": suppressed,
        "source_signal_accounted_count": len(episodes) + suppressed,
        "source_signal_accounting_status": (
            "pass" if len(episodes) + suppressed == source_signal_count else "fail"
        ),
        "same_stock_overlap_pair_count": _same_stock_overlap_pair_count(episodes),
        "unconfirmed_counterfactual_mature_count": counterfactual_metrics["accepted_trade_count"],
        "avoided_failure_count": counterfactual_metrics["failure_count"],
        "avoided_failure_rate_of_unconfirmed_pct": counterfactual_metrics["failure_rate_pct"],
        "missed_win_count": counterfactual_metrics["win_count"],
        "missed_win_rate_of_unconfirmed_pct": counterfactual_metrics["win_rate_pct"],
        "unconfirmed_counterfactual_avg_return_pct": counterfactual_metrics["avg_realized_return_pct"],
        "unconfirmed_counterfactual_median_return_pct": counterfactual_metrics["median_realized_return_pct"],
        "paired_timing_cost_count": int(timing_cost.notna().sum()),
        "avg_timing_cost_vs_direct_signal_d20_pct": _mean(timing_cost),
        "median_timing_cost_vs_direct_signal_d20_pct": _median(timing_cost),
        "win_definition": "realized return >= +5%",
        "neutral_definition": "0% <= realized return < +5%",
        "failure_definition": "realized return < 0%",
        "entry_rule": "confirmation date close known first, then next trading day open entry",
        "stop_rule": "none in timing audit; isolate confirmation timing before stop research",
        "uses_intraday_operation_price": False,
        "known_before_entry_open_rate_pct": _rate(
            int(entered["known_before_entry_open"].astype(bool).sum()),
            len(entered),
        ),
        "sample_count_policy": "reported_not_a_disqualifier",
        "approved_for_daily": False,
        "production_change": "none",
        "promotion_readiness": promotion_readiness,
        **metrics,
    }
    anomaly_row = {
        **{column: row.get(column, "") for column in SUMMARY_REQUIRED_ID_COLUMNS},
        "source_signal_count": source_signal_count,
        "source_known_anomaly_count": source_anomaly_count,
        **anomaly,
        "interpretation_status": (
            "not_decision_basis_known_anomalies_included"
            if not decision_basis
            else "blocked_return_dominance_review"
            if dominance
            else "anomaly_check_pass"
        ),
        "approved_for_daily": False,
        "production_change": "none",
    }
    return row, anomaly_row


def _same_stock_overlap_pair_count(episodes: pd.DataFrame) -> int:
    accepted = episodes[
        episodes["lifecycle_status"].eq("confirmed_mature")
        & episodes["metric_included"].astype(bool)
    ].copy()
    if accepted.empty:
        return 0
    count = 0
    for _, part in accepted.sort_values(
        ["stock_id", "entry_sequence_index", "exit_sequence_index"],
        kind="mergesort",
    ).groupby("stock_id", sort=False, dropna=False):
        entries = pd.to_numeric(part["entry_sequence_index"], errors="coerce").tolist()
        exits = pd.to_numeric(part["exit_sequence_index"], errors="coerce").tolist()
        for previous_exit, next_entry in zip(exits, entries[1:]):
            if not math.isnan(previous_exit) and not math.isnan(next_entry) and next_entry <= previous_exit:
                count += 1
    return count


def _source_partition_rows(
    frame: pd.DataFrame,
    *,
    source_mask: pd.Series,
    basis: str,
    source_anomaly_count: int,
    generated_at: str,
    confirmation_cache: dict[tuple[str, int, str, int], tuple[int | None, bool, bool]],
) -> list[dict[str, Any]]:
    counts: dict[str, int] = {}
    total = int(source_mask.sum())
    sorted_frame = frame.sort_values(["stock_id", "_revenue_stock_sequence_index"], kind="mergesort")
    sorted_mask = source_mask.reindex(sorted_frame.index).fillna(False).astype(bool)
    next_day_spec = CONFIRMATION_SPECS[0]
    range_spec = CONFIRMATION_SPECS[1]
    ma_spec = CONFIRMATION_SPECS[2]
    for _, original_part in sorted_frame.groupby("stock_id", sort=False, dropna=False):
        original_indices = original_part.index
        part = original_part.reset_index(drop=True)
        positions = np.flatnonzero(sorted_mask.loc[original_indices].to_numpy(dtype=bool))
        for position_value in positions:
            position = int(position_value)
            if position + MAX_PENDING_WINDOW_DAYS >= len(part):
                key = "insufficient_future_10d_window"
            else:
                next_position, _, _ = _confirmation_position(
                    part,
                    signal_position=position,
                    spec=next_day_spec,
                    pending_window_days=1,
                    cache=confirmation_cache,
                )
                range_position, _, _ = _confirmation_position(
                    part,
                    signal_position=position,
                    spec=range_spec,
                    pending_window_days=10,
                    cache=confirmation_cache,
                )
                ma_position, _, _ = _confirmation_position(
                    part,
                    signal_position=position,
                    spec=ma_spec,
                    pending_window_days=10,
                    cache=confirmation_cache,
                )
                key = (
                    f"next_day={int(next_position is not None)}|"
                    f"range23={int(range_position is not None)}|"
                    f"ma20_ema23={int(ma_position is not None)}"
                )
            counts[key] = counts.get(key, 0) + 1

    rows: list[dict[str, Any]] = []
    for key, count in sorted(counts.items()):
        rows.append(
            {
                "generated_at": generated_at,
                "model_id": MODEL_ID,
                "model_name_zh": MODEL_NAME_ZH,
                "research_artifact_id": ARTIFACT_ID,
                "artifact_version": ARTIFACT_VERSION,
                "row_type": "source_partition",
                "anomaly_exclusion_basis": basis,
                "decision_basis": basis == DECISION_BASIS,
                "confirmation_variant_id": "three_variant_source_partition",
                "confirmation_variant_name_zh": "三種確認分支來源交集",
                "confirmation_rule": "raw source-signal confirmation overlap; performance is not pooled",
                "pending_window_days": MAX_PENDING_WINDOW_DAYS,
                "exit_clock_id": "not_applicable_source_partition",
                "exit_clock_name_zh": "不適用",
                "exit_rule": "不適用",
                "candidate_source_name_zh": "營收爆發但股價尚未反應候選池",
                "source_signal_count": total,
                "source_unique_stock_count": int(frame.loc[source_mask, "stock_id"].nunique()),
                "source_known_anomaly_count": source_anomaly_count,
                "partition_key": key,
                "partition_count": count,
                "partition_rate_pct": _rate(count, total),
                "source_partition_total_count": total,
                "source_partition_status": "pass" if sum(counts.values()) == total else "fail",
                "approved_for_daily": False,
                "production_change": "none",
                "promotion_readiness": "research_only_not_promotion_ready",
            }
        )
    return rows


def build_close_confirmation_timing_audit(
    prepared_frame: pd.DataFrame,
    *,
    expected_control: dict[str, Any] | None = None,
) -> tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    required = {
        "stock_id",
        "open",
        "close",
        "ma20",
        "ema23",
        "_revenue_signal_date",
        "_revenue_stock_sequence_index",
        "_revenue_range23_highest_close_prev",
        "_revenue_timing_source_flag",
        "_revenue_timing_source_anomaly_flag",
    }
    missing = required - set(prepared_frame.columns)
    if missing:
        raise ValueError(f"close-confirmation timing input missing columns: {sorted(missing)}")

    frame = prepared_frame.copy()
    source_all = frame["_revenue_timing_source_flag"].astype(bool)
    source_anomaly = frame["_revenue_timing_source_anomaly_flag"].astype(bool) & source_all
    summary_rows: list[dict[str, Any]] = []
    anomaly_rows: list[dict[str, Any]] = []
    decision_detail: list[pd.DataFrame] = []
    generated_at = now_text()
    confirmation_cache: dict[tuple[str, int, str, int], tuple[int | None, bool, bool]] = {}
    direct_outcome_cache: dict[tuple[str, int], tuple[float | str, str, bool, str]] = {}
    trade_outcome_cache: dict[
        tuple[str, int, int],
        tuple[float | str, float | str, float | str, str, bool, str, float | str, float | str],
    ] = {}

    for basis in (INCLUDING_BASIS, DECISION_BASIS):
        source_mask = source_all if basis == INCLUDING_BASIS else source_all & ~source_anomaly
        source_count = int(source_mask.sum())
        source_unique = int(frame.loc[source_mask, "stock_id"].nunique())
        source_anomaly_count = int(source_anomaly.sum())
        summary_rows.extend(
            _source_partition_rows(
                frame,
                source_mask=source_mask,
                basis=basis,
                source_anomaly_count=source_anomaly_count,
                generated_at=generated_at,
                confirmation_cache=confirmation_cache,
            )
        )

        control_exit = EXIT_CLOCK_SPECS[0]
        control_episodes = _replay_variant(
            frame,
            source_mask=source_mask,
            spec=CONTROL_SPEC,
            pending_window_days=0,
            exit_clock=control_exit,
            basis=basis,
            generated_at=generated_at,
            confirmation_cache=confirmation_cache,
            direct_outcome_cache=direct_outcome_cache,
            trade_outcome_cache=trade_outcome_cache,
        )
        control_row, control_anomaly = _performance_summary(
            control_episodes,
            source_signal_count=source_count,
            source_unique_stock_count=source_unique,
            source_anomaly_count=source_anomaly_count,
            spec=CONTROL_SPEC,
            pending_window_days=0,
            exit_clock=control_exit,
            basis=basis,
            generated_at=generated_at,
        )
        if basis == DECISION_BASIS and expected_control:
            expected_source = int(expected_control.get("basis_source_signal_count", -1))
            expected_trades = int(expected_control.get("accepted_trade_count", -1))
            actual_source = int(control_row["source_signal_count"])
            actual_trades = int(control_row["accepted_trade_count"])
            control_row["control_expected_source_signal_count"] = expected_source
            control_row["control_expected_accepted_trade_count"] = expected_trades
            control_row["control_parity_status"] = (
                "pass" if (actual_source, actual_trades) == (expected_source, expected_trades) else "fail"
            )
        else:
            control_row["control_expected_source_signal_count"] = ""
            control_row["control_expected_accepted_trade_count"] = ""
            control_row["control_parity_status"] = "not_applicable"
        summary_rows.append(control_row)
        anomaly_rows.append(control_anomaly)
        if basis == DECISION_BASIS:
            decision_detail.append(
                control_episodes.loc[
                    control_episodes["lifecycle_status"].eq("confirmed_mature"),
                    DETAIL_COLUMNS,
                ].copy()
            )

        for spec in CONFIRMATION_SPECS:
            for pending_window_days in spec.pending_windows:
                for exit_clock in EXIT_CLOCK_SPECS:
                    episodes = _replay_variant(
                        frame,
                        source_mask=source_mask,
                        spec=spec,
                        pending_window_days=pending_window_days,
                        exit_clock=exit_clock,
                        basis=basis,
                        generated_at=generated_at,
                        confirmation_cache=confirmation_cache,
                        direct_outcome_cache=direct_outcome_cache,
                        trade_outcome_cache=trade_outcome_cache,
                    )
                    summary_row, anomaly_row = _performance_summary(
                        episodes,
                        source_signal_count=source_count,
                        source_unique_stock_count=source_unique,
                        source_anomaly_count=source_anomaly_count,
                        spec=spec,
                        pending_window_days=pending_window_days,
                        exit_clock=exit_clock,
                        basis=basis,
                        generated_at=generated_at,
                    )
                    summary_row["control_expected_source_signal_count"] = ""
                    summary_row["control_expected_accepted_trade_count"] = ""
                    summary_row["control_parity_status"] = "not_applicable"
                    summary_rows.append(summary_row)
                    anomaly_rows.append(anomaly_row)
                    if basis == DECISION_BASIS:
                        # Persist mature confirmed rows only. Unconfirmed and
                        # not-evaluable episodes remain fully counted in the
                        # summary, but duplicating them for every timing sweep
                        # creates a large artifact without adding row-level
                        # return evidence.
                        decision_detail.append(
                            episodes.loc[
                                episodes["lifecycle_status"].eq("confirmed_mature"),
                                DETAIL_COLUMNS,
                            ].copy()
                        )

    summary = pd.DataFrame(summary_rows)
    detail = pd.concat(decision_detail, ignore_index=True, sort=False) if decision_detail else pd.DataFrame()
    anomaly = pd.DataFrame(anomaly_rows)
    if not detail.empty:
        detail = detail[DETAIL_COLUMNS].sort_values(
            [
                "confirmation_variant_id",
                "pending_window_days",
                "exit_clock_id",
                "stock_id",
                "signal_sequence_index",
            ],
            kind="mergesort",
        ).reset_index(drop=True)
    return summary, detail, anomaly


def write_close_confirmation_timing_audit(
    summary: pd.DataFrame,
    detail: pd.DataFrame,
    anomaly: pd.DataFrame,
) -> None:
    summary_timestamps = summary["generated_at"].dropna().astype(str).unique().tolist()
    anomaly_timestamps = anomaly["generated_at"].dropna().astype(str).unique().tolist()
    if len(summary_timestamps) != 1 or anomaly_timestamps != summary_timestamps:
        raise ValueError("summary and anomaly artifacts must share one generated_at timestamp")
    generated_at = summary_timestamps[0]

    for frame, latest, history, docs in (
        (summary, SUMMARY_CSV, HISTORY_SUMMARY_CSV, DOCS_SUMMARY_CSV),
        (anomaly, ANOMALY_CSV, HISTORY_ANOMALY_CSV, DOCS_ANOMALY_CSV),
    ):
        write_csv(frame, latest)
        write_csv(frame, history)
        write_csv(frame, docs)
    write_csv(detail, DETAIL_CSV)

    decision = summary[
        summary["anomaly_exclusion_basis"].eq(DECISION_BASIS)
        & summary["row_type"].isin(["control_baseline", "variant_performance"])
    ].copy()
    partitions = summary[
        summary["anomaly_exclusion_basis"].eq(DECISION_BASIS)
        & summary["row_type"].eq("source_partition")
    ].copy()
    anomaly_decision = anomaly[anomaly["anomaly_exclusion_basis"].eq(DECISION_BASIS)].copy()
    lines = [
        "# 營收爆發但股價尚未反應模型：收盤確認時點稽核",
        "",
        f"- generated_at: `{generated_at}`",
        "- status: `research_only_not_promotion_ready`",
        "- 候選池：強月營收條件使用 `source_table_date <= signal_date` 的歷史 as-of join，股價仍在近期 23 日區間且攻擊尚未開始。",
        "- 三個研究分支分開回放與計算，績效不得混算：隔日續強確認型、區間突破確認型、均線站回確認型。",
        "- 進場：確認日收盤後才成立，次一交易日開盤進場。",
        "- 出場時鐘：同時比較原訊號日 D+20 收盤與確認日 D+20 收盤；本稽核不加停損，先隔離確認時點效果。",
        "- 勝／和／敗：報酬 >= +5% 為勝；0% 至未滿 +5% 為和；報酬 < 0% 為敗。",
        "- 去重：逐股 chronological lifecycle replay；待確認與持有期間的後續同股訊號全部壓掉。",
        "- 樣本數只揭露，不會單獨作為否定研究分支的理由。",
        "- scope：僅使用月營收；EPS、毛利率、營益率、營業利益、業外、淨利與季／年財報不在本輪範圍。",
        "- production_change: `none`",
        "",
        "## 三分支績效",
        "",
        markdown_table(
            decision,
            [
                "confirmation_variant_name_zh",
                "pending_window_days",
                "exit_clock_name_zh",
                "pending_episode_count",
                "confirmation_rate_pct",
                "accepted_trade_count",
                "win_rate_pct",
                "neutral_rate_pct",
                "failure_rate_pct",
                "avg_realized_return_pct",
                "median_realized_return_pct",
                "high_return_8_rate_pct",
                "loss_5_rate_pct",
                "avoided_failure_count",
                "missed_win_count",
                "avg_timing_cost_vs_direct_signal_d20_pct",
                "same_stock_overlap_pair_count",
            ],
            limit=40,
        ),
        "",
        "## 候選來源交集",
        "",
        markdown_table(
            partitions,
            ["partition_key", "partition_count", "partition_rate_pct", "source_partition_status"],
            limit=20,
        ),
        "",
        "## 數字異常檢查",
        "",
        markdown_table(
            anomaly_decision,
            [
                "confirmation_variant_name_zh",
                "pending_window_days",
                "exit_clock_id",
                "accepted_trade_count_before_path_exclusion",
                "price_path_anomaly_count",
                "metric_sample_count",
                "max_realized_return_pct",
                "max_return_stock_id",
                "max_return_signal_date",
                "min_realized_return_pct",
                "min_return_stock_id",
                "min_return_signal_date",
                "top1_abs_return_share_pct",
                "top5_abs_return_share_pct",
                "trimmed_1pct_avg_return_pct",
                "interpretation_status",
            ],
            limit=40,
        ),
        "",
        "## Large Detail Policy",
        "",
        f"逐筆 detail 僅保留確認後已成熟交易與價格路徑異常 evidence，位於 `{DETAIL_CSV.as_posix()}`；未確認／資料未成熟列由 summary 全量計數，不複製到 `docs/latest` 或 `output/history`。",
    ]
    SUMMARY_MD.parent.mkdir(parents=True, exist_ok=True)
    SUMMARY_MD.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8", newline="\n")
    DOCS_SUMMARY_MD.parent.mkdir(parents=True, exist_ok=True)
    DOCS_SUMMARY_MD.write_text(SUMMARY_MD.read_text(encoding="utf-8"), encoding="utf-8", newline="\n")
