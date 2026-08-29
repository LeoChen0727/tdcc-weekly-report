from __future__ import annotations

from bisect import bisect_left
from dataclasses import dataclass
from pathlib import Path
import math

import numpy as np
import pandas as pd

from revenue_unreacted_range_forward_confirmation_feature_audit import (
    OPERATION_RETURN_REVIEW_THRESHOLD_PCT,
    _bool_value,
    _normalize_source_detail as _normalize_forward_source_detail,
    _strict_launch_metrics,
    prepare_daily_by_stock,
)
from revenue_unreacted_range_source_snapshot_projection import (
    load_projected_source_detail,
    load_source_snapshot_projection_manifest,
    validate_projection_binding,
    V1_PROJECTION_VERSION,
    V2_PROJECTION_VERSION,
)
from revenue_unreacted_range_source_first_condition_audit import (
    attach_qualifying_event_anomaly_flags,
)

ROOT = Path(__file__).resolve().parents[1]
MODEL_ID = "revenue_unreacted_range"
ARTIFACT_ID = "revenue_unreacted_range_rearmed_operation_grid"
V1_ARTIFACT_VERSION = "rearmed_operation_grid_v1_20260713"
V2_ARTIFACT_VERSION = "rearmed_operation_grid_v2_20260822"
V3_ARTIFACT_VERSION = "rearmed_operation_grid_v3_20260829"
ARTIFACT_VERSION = V1_ARTIFACT_VERSION
EPISODE_AGGREGATE_ANOMALY_POLICY_ID = "episode_aggregate_v1"
TRIGGER_ASOF_ANOMALY_POLICY_ID = "trigger_asof_qualifying_event_v1_20260829"


def artifact_version_for_projection(
    projection_version: object,
    *,
    anomaly_attribution_policy_id: str = EPISODE_AGGREGATE_ANOMALY_POLICY_ID,
) -> str:
    version = str(projection_version).strip()
    if anomaly_attribution_policy_id == TRIGGER_ASOF_ANOMALY_POLICY_ID:
        if version != V2_PROJECTION_VERSION:
            raise RuntimeError(
                "trigger-as-of anomaly attribution requires the immutable v2 source "
                f"projection; received {version or '<empty>'}"
            )
        return V3_ARTIFACT_VERSION
    if anomaly_attribution_policy_id != EPISODE_AGGREGATE_ANOMALY_POLICY_ID:
        raise RuntimeError(
            "unsupported source anomaly attribution policy: "
            f"{anomaly_attribution_policy_id or '<empty>'}"
        )
    mapping = {
        V1_PROJECTION_VERSION: V1_ARTIFACT_VERSION,
        V2_PROJECTION_VERSION: V2_ARTIFACT_VERSION,
    }
    if version not in mapping:
        raise RuntimeError(
            f"unsupported canonical source projection version: {version or '<empty>'}"
        )
    return mapping[version]
PRICE_HISTORY_CUTOFF_DATE = "20260713"
EXPECTED_SOURCE_ARTIFACT_ID = "revenue_unreacted_range_source_first_condition_audit"
EXPECTED_SOURCE_ARTIFACT_VERSION = "source_first_condition_v3_20260720"
SOURCE_ARTIFACT_ID = EXPECTED_SOURCE_ARTIFACT_ID
SOURCE_VARIANT_ID = "absolute_or_two_month_yoy_ge15"

LATEST_CSV = ROOT / f"output/latest/research_backtest/{ARTIFACT_ID}_latest.csv"
DETAIL_CSV = ROOT / f"output/latest/research_backtest/{ARTIFACT_ID}_detail_latest.csv"
RETURN_REVIEW_CSV = ROOT / f"output/latest/research_backtest/{ARTIFACT_ID}_operation_return_review_latest.csv"
LATEST_MD = ROOT / f"output/latest/research_backtest/{ARTIFACT_ID}_latest.md"
HISTORY_CSV = ROOT / f"output/history/research/{ARTIFACT_ID}.csv"
HISTORY_RETURN_REVIEW_CSV = ROOT / f"output/history/research/{ARTIFACT_ID}_operation_return_review.csv"
DOCS_CSV = ROOT / f"docs/latest/{ARTIFACT_ID}_latest.csv"
DOCS_RETURN_REVIEW_CSV = ROOT / f"docs/latest/{ARTIFACT_ID}_operation_return_review_latest.csv"
DOCS_MD = ROOT / f"docs/latest/{ARTIFACT_ID}_latest.md"

PRIMARY_ANALYSIS_BASIS = "primary_candidate_retaining"
SENSITIVITY_ANALYSIS_BASIS = "excluding_unresolved_anomaly_candidates_sensitivity"
ANALYSIS_BASES = (PRIMARY_ANALYSIS_BASIS, SENSITIVITY_ANALYSIS_BASIS)
HOLD_DAYS = (10, 15, 20, 30)
DETAIL_MAX_BYTES = 50_000_000
DETAIL_ARTIFACT_DROP_COLUMNS = (
    "base_confirmation_rule",
    "bonus_timing_role",
    "stop_rule",
    "episode_status",
    "source_launch_date",
    "same_stock_non_overlap_policy",
    "outcome_definition",
    "operation_return_review_policy",
    "financial_statement_scope",
    "promotion_readiness",
    "lifecycle_role",
)

BASE_CONFIRMATION_RULE_ID = "close_cross_prev20_and_ma60_gt_ma120"
BASE_CONFIRMATION_RULE = "signal close crosses above the previous 20-day highest close and MA60 is above MA120"
BASE_ENTRY_RULE_ID = "trigger_close_confirmed_next_trading_day_open"
BONUS_CONFIRMATION_RULE_ID = "next_day_close_continuation"
BONUS_ENTRY_RULE_ID = "next_day_close_confirmed_following_trading_day_open"
NO_STOP_POLICY_ID = "none_no_stop_reference"
STOP_POLICY_ID = "ma20_ema23_close_stop_4d"
STOP_RULE_ID = "sustained_close_below_lower_ma20_ema23_4pct_4d"
STOP_RULE = "four consecutive closes at or below 96% of the lower of MA20 and EMA23, then exit at the next trading day open"
OPERATION_RETURN_REVIEW_POLICY = (
    "absolute realized operation return >= 80% is a review trigger only; retain in primary metrics "
    "and do not assign anomaly disposition without bottom-level root-cause evidence"
)
FINANCIAL_STATEMENT_SCOPE = (
    "monthly_revenue_only;EPS_gross_margin_operating_margin_operating_income_"
    "non_operating_income_net_income_excluded"
)


def _normalize_source_detail(frame: pd.DataFrame) -> pd.DataFrame:
    required = {"artifact_id", "artifact_version"}
    missing = sorted(required - set(frame.columns))
    if missing:
        raise RuntimeError(
            f"rearmed operation grid source lineage is missing columns: {missing}"
        )
    if set(frame["artifact_id"].astype(str)) != {EXPECTED_SOURCE_ARTIFACT_ID}:
        raise RuntimeError(
            "rearmed operation grid source artifact id drift: "
            f"expected={EXPECTED_SOURCE_ARTIFACT_ID}"
        )
    if set(frame["artifact_version"].astype(str)) != {
        EXPECTED_SOURCE_ARTIFACT_VERSION
    }:
        raise RuntimeError(
            "rearmed operation grid source artifact version drift: "
            f"expected={EXPECTED_SOURCE_ARTIFACT_VERSION}"
        )
    return _normalize_forward_source_detail(frame)


@dataclass(frozen=True)
class ConfirmationSpec:
    confirmation_order: int
    confirmation_variant_id: str
    information_cutoff: str
    entry_rule_id: str
    bonus_id: str
    bonus_timing_role: str
    require_next_close_continuation: bool


@dataclass(frozen=True)
class LifecycleSpec:
    lifecycle_order: int
    lifecycle_policy_id: str
    lifecycle_role: str
    allow_rearm: bool


CONFIRMATION_SPECS = (
    ConfirmationSpec(
        10,
        "base_close_confirmed",
        "trigger_date_close",
        BASE_ENTRY_RULE_ID,
        "none_base_metric",
        "next_day_continuation_is_post_entry_observation_not_available_for_d1_open_buy_ranking",
        False,
    ),
    ConfirmationSpec(
        20,
        "delayed_next_close_continuation_bonus",
        "next_trading_day_close",
        BONUS_ENTRY_RULE_ID,
        BONUS_CONFIRMATION_RULE_ID,
        "bonus_is_known_at_d1_close_and_requires_d2_open_entry",
        True,
    ),
)

LIFECYCLE_SPECS = (
    LifecycleSpec(10, "episode_first_match_once", "benchmark_no_rearm", False),
    LifecycleSpec(
        20,
        "rearm_after_realized_exit_next_trade_day",
        "user_adopted_rearmed_lifecycle",
        True,
    ),
)

STOP_POLICIES = (NO_STOP_POLICY_ID, STOP_POLICY_ID)


def _now_text() -> str:
    return pd.Timestamp.now(tz="Asia/Taipei").strftime("%Y-%m-%d %H:%M:%S Asia/Taipei")


def _stock_id(value: object) -> str:
    text = str(value or "").strip()
    return text[:-2] if text.endswith(".0") and text[:-2].isdigit() else text


def _number(value: object) -> float:
    number = pd.to_numeric(pd.Series([value]), errors="coerce").iloc[0]
    return float(number) if pd.notna(number) else math.nan


def _stable(value: object, digits: int = 4) -> float | str:
    number = _number(value)
    return round(number, digits) if np.isfinite(number) else ""


def _rate(numerator: int, denominator: int) -> float | str:
    return round(numerator / denominator * 100.0, 4) if denominator else ""


def _mean(values: pd.Series) -> float | str:
    numeric = pd.to_numeric(values, errors="coerce").dropna()
    return round(float(numeric.mean()), 4) if not numeric.empty else ""


def _median(values: pd.Series) -> float | str:
    numeric = pd.to_numeric(values, errors="coerce").dropna()
    return round(float(numeric.median()), 4) if not numeric.empty else ""


def _quantile(values: pd.Series, quantile: float) -> float | str:
    numeric = pd.to_numeric(values, errors="coerce").dropna()
    return round(float(numeric.quantile(quantile)), 4) if not numeric.empty else ""


def _normalize_stock_frame(frame: pd.DataFrame) -> pd.DataFrame:
    stock = frame.copy().sort_values("date", kind="mergesort").reset_index(drop=True)
    stock["date"] = stock["date"].astype(str).str.replace(r"\.0$", "", regex=True)
    for column in ("analysis_open", "analysis_close", "open", "close", "ma60", "ma120"):
        if column not in stock.columns:
            stock[column] = np.nan
        stock[column] = pd.to_numeric(stock[column], errors="coerce")
    stock["operation_ma20"] = stock["analysis_close"].rolling(20, min_periods=20).mean()
    stock["operation_ema23"] = stock["analysis_close"].ewm(span=23, adjust=False, min_periods=23).mean()
    if "cross_breakout_prev20" not in stock.columns:
        previous_high = stock["analysis_close"].shift(1).rolling(20, min_periods=20).max()
        above = stock["analysis_close"].gt(previous_high)
        stock["cross_breakout_prev20"] = above & ~above.shift(1, fill_value=False).astype(bool)
    stock["cross_breakout_prev20"] = stock["cross_breakout_prev20"].map(_bool_value)
    if "price_resolution_ids_on_date" not in stock.columns:
        stock["price_resolution_ids_on_date"] = ""
    return stock


def _apply_price_history_cutoff(
    daily_by_stock: dict[str, pd.DataFrame],
) -> dict[str, pd.DataFrame]:
    # This artifact version is immutable; newer sessions require a new version.
    pinned: dict[str, pd.DataFrame] = {}
    for stock_id, frame in daily_by_stock.items():
        stock = frame.copy()
        dates = stock["date"].astype(str).str.replace(r"\D", "", regex=True).str[:8]
        pinned[stock_id] = stock.loc[dates.le(PRICE_HISTORY_CUTOFF_DATE)].reset_index(drop=True)
    return pinned


def _assert_source_within_price_history_cutoff(source: pd.DataFrame) -> None:
    for column in ("episode_start_trade_date", "episode_end_date"):
        dates = source[column].astype(str).str.replace(r"\D", "", regex=True).str[:8]
        if dates.loc[dates.str.fullmatch(r"\d{8}")].gt(PRICE_HISTORY_CUTOFF_DATE).any():
            raise RuntimeError(
                f"{ARTIFACT_VERSION} source {column} exceeds pinned price cutoff "
                f"{PRICE_HISTORY_CUTOFF_DATE}"
            )


def _episode_bounds(stock: pd.DataFrame, episode: pd.Series) -> tuple[int, int] | None:
    starts = stock.index[stock["date"].eq(str(episode["episode_start_trade_date"]))]
    ends = stock.index[stock["date"].eq(str(episode["episode_end_date"]))]
    if not len(starts) or not len(ends):
        return None
    start = int(starts[0])
    end = int(ends[0])
    return (start, end) if start <= end else None


def _base_trigger_hit(stock: pd.DataFrame, trigger_index: int) -> bool:
    ma60 = _number(stock.at[trigger_index, "ma60"])
    ma120 = _number(stock.at[trigger_index, "ma120"])
    return bool(
        _bool_value(stock.at[trigger_index, "cross_breakout_prev20"])
        and np.isfinite(ma60)
        and np.isfinite(ma120)
        and ma60 > ma120
    )


def _confirmation_indices(
    stock: pd.DataFrame,
    trigger_index: int,
    spec: ConfirmationSpec,
) -> tuple[int, int, bool] | None:
    next_index = trigger_index + 1
    next_observed = next_index < len(stock)
    continuation = bool(
        next_observed
        and _number(stock.at[next_index, "analysis_close"])
        > _number(stock.at[trigger_index, "analysis_close"])
    )
    if spec.require_next_close_continuation and not continuation:
        return None
    confirmation_index = next_index if spec.require_next_close_continuation else trigger_index
    entry_index = confirmation_index + 1
    if entry_index >= len(stock):
        return confirmation_index, entry_index, continuation
    return confirmation_index, entry_index, continuation


def _stop_reference(stock: pd.DataFrame, index: int) -> float:
    ma20 = _number(stock.at[index, "operation_ma20"])
    ema23 = _number(stock.at[index, "operation_ema23"])
    references = [value for value in (ma20, ema23) if np.isfinite(value) and value > 0]
    return min(references) * 0.96 if references else math.nan


def _simulate_operation(
    stock: pd.DataFrame,
    *,
    trigger_index: int,
    confirmation_index: int,
    entry_index: int,
    hold_days: int,
    stop_policy_id: str,
) -> dict[str, object]:
    strict_launch = _strict_launch_metrics(stock, trigger_index)
    if entry_index >= len(stock):
        return {
            "operation_status": "right_censored_before_entry",
            "return_valid": False,
            "right_censored": True,
            "entry_index": entry_index,
            "exit_index": len(stock) - 1,
            **strict_launch,
        }
    entry_price = _number(stock.at[entry_index, "analysis_open"])
    if not np.isfinite(entry_price) or entry_price <= 0:
        return {
            "operation_status": "invalid_entry_open",
            "return_valid": False,
            "right_censored": False,
            "entry_index": entry_index,
            "exit_index": entry_index,
            **strict_launch,
        }
    planned_exit_index = entry_index + hold_days - 1
    if planned_exit_index >= len(stock):
        return {
            "operation_status": f"right_censored_before_d{hold_days}",
            "return_valid": False,
            "right_censored": True,
            "entry_index": entry_index,
            "entry_date": str(stock.at[entry_index, "date"]),
            "entry_price": round(entry_price, 8),
            "exit_index": len(stock) - 1,
            "planned_exit_index": planned_exit_index,
            **strict_launch,
        }

    exit_index = planned_exit_index
    exit_price = _number(stock.at[exit_index, "analysis_close"])
    exit_price_basis = "fixed_future_close"
    exit_reason = f"fixed_d{hold_days}_close"
    stop_confirmation_date = ""
    stop_reference = math.nan
    stop_days = 0
    if stop_policy_id == STOP_POLICY_ID:
        for index in range(entry_index, planned_exit_index):
            close = _number(stock.at[index, "analysis_close"])
            stop_reference = _stop_reference(stock, index)
            if np.isfinite(close) and np.isfinite(stop_reference) and close <= stop_reference:
                stop_days += 1
            else:
                stop_days = 0
            if stop_days >= 4:
                stop_confirmation_date = str(stock.at[index, "date"])
                exit_index = index + 1
                exit_price = _number(stock.at[exit_index, "analysis_open"])
                exit_price_basis = "next_trading_day_open_after_stop_close_confirmation"
                exit_reason = STOP_RULE_ID
                break

    if not np.isfinite(exit_price) or exit_price <= 0:
        return {
            "operation_status": "invalid_exit_price",
            "return_valid": False,
            "right_censored": False,
            "entry_index": entry_index,
            "exit_index": exit_index,
            "planned_exit_index": planned_exit_index,
            **strict_launch,
        }

    realized_return = (exit_price / entry_price - 1.0) * 100.0
    operation_path = pd.to_numeric(
        stock.loc[entry_index:exit_index, "analysis_close"], errors="coerce"
    ).dropna()
    max_close_return = (
        float(operation_path.max() / entry_price - 1.0) * 100.0 if not operation_path.empty else math.nan
    )
    min_close_return = (
        float(operation_path.min() / entry_price - 1.0) * 100.0 if not operation_path.empty else math.nan
    )
    outcome = "win" if realized_return > 1e-9 else "failure" if realized_return < -1e-9 else "neutral"
    return {
        "operation_status": "mature_operation",
        "return_valid": True,
        "right_censored": False,
        "entry_index": entry_index,
        "entry_date": str(stock.at[entry_index, "date"]),
        "entry_price": round(entry_price, 8),
        "planned_exit_index": planned_exit_index,
        "planned_exit_date": str(stock.at[planned_exit_index, "date"]),
        "exit_index": exit_index,
        "exit_date": str(stock.at[exit_index, "date"]),
        "exit_price": round(exit_price, 8),
        "exit_price_basis": exit_price_basis,
        "exit_reason": exit_reason,
        "stop_confirmation_date": stop_confirmation_date,
        "stop_reference_price": _stable(stop_reference, 8),
        "stop_confirmed_days": stop_days,
        "realized_return_pct": round(realized_return, 4),
        "return_outcome": outcome,
        "realized_return_ge20": realized_return >= 20.0,
        "max_close_return_pct": _stable(max_close_return),
        "min_close_return_pct": _stable(min_close_return),
        "operation_return_review_candidate_flag": abs(realized_return) >= OPERATION_RETURN_REVIEW_THRESHOLD_PCT,
        **strict_launch,
    }


def _source_anomaly(episode: pd.Series) -> bool:
    return _bool_value(episode["qualifying_source_revenue_anomaly_candidate_flag"]) or _bool_value(
        episode["unresolved_price_path_candidate_flag"]
    )


def _source_anomaly_as_of_trigger(episode: pd.Series, trigger_date: object) -> bool:
    required = (
        "qualifying_trade_dates",
        "qualifying_source_revenue_anomaly_candidate_flags",
    )
    missing = [column for column in required if column not in episode.index]
    if missing:
        raise RuntimeError(
            "trigger-as-of source anomaly attribution is missing columns: "
            f"{missing}"
        )
    trade_dates = [
        token.strip()
        for token in str(episode["qualifying_trade_dates"]).split("|")
        if token.strip()
    ]
    flags = [
        _bool_value(token)
        for token in str(
            episode["qualifying_source_revenue_anomaly_candidate_flags"]
        ).split("|")
        if token.strip()
    ]
    if len(trade_dates) != len(flags) or not trade_dates:
        raise RuntimeError(
            "trigger-as-of source anomaly event lineage is not parallel and non-empty: "
            f"{episode.get('episode_key', '<unknown>')}"
        )
    cutoff = str(trigger_date).strip()
    if len(cutoff) != 8 or not cutoff.isdigit():
        raise RuntimeError(f"trigger-as-of anomaly cutoff is not YYYYMMDD: {cutoff}")
    revenue_candidate = any(
        flag and trade_date <= cutoff
        for trade_date, flag in zip(trade_dates, flags)
    )
    return revenue_candidate or _bool_value(
        episode["unresolved_price_path_candidate_flag"]
    )


def _grid_id(
    lifecycle: LifecycleSpec,
    confirmation: ConfirmationSpec,
    hold_days: int,
    stop_policy_id: str,
) -> str:
    return "|".join(
        (
            lifecycle.lifecycle_policy_id,
            confirmation.confirmation_variant_id,
            f"d{hold_days}",
            stop_policy_id,
        )
    )


def build_operation_detail(
    source_detail: pd.DataFrame,
    daily_by_stock: dict[str, pd.DataFrame],
    generated_at: str,
    *,
    anomaly_attribution_policy_id: str = EPISODE_AGGREGATE_ANOMALY_POLICY_ID,
) -> pd.DataFrame:
    source = _normalize_source_detail(source_detail)
    daily = {stock_id: _normalize_stock_frame(frame) for stock_id, frame in daily_by_stock.items()}
    trigger_candidates: dict[
        tuple[str, str],
        tuple[tuple[int, ...], tuple[tuple[int, int, int, bool], ...]],
    ] = {}
    for stock_id, stock in daily.items():
        base_indices = [index for index in stock.index if _base_trigger_hit(stock, int(index))]
        for confirmation in CONFIRMATION_SPECS:
            candidates: list[tuple[int, int, int, bool]] = []
            for trigger_index in base_indices:
                confirmation_indices = _confirmation_indices(stock, trigger_index, confirmation)
                if confirmation_indices is None:
                    continue
                confirmation_index, entry_index, continuation = confirmation_indices
                candidates.append(
                    (trigger_index, confirmation_index, entry_index, continuation)
                )
            trigger_candidates[(stock_id, confirmation.confirmation_variant_id)] = (
                tuple(candidate[0] for candidate in candidates),
                tuple(candidates),
            )
    rows: list[dict[str, object]] = []
    for lifecycle in LIFECYCLE_SPECS:
        for confirmation in CONFIRMATION_SPECS:
            for hold_days in HOLD_DAYS:
                for stop_policy_id in STOP_POLICIES:
                    grid_id = _grid_id(lifecycle, confirmation, hold_days, stop_policy_id)
                    for stock_id, episodes in source.groupby("stock_id", sort=False):
                        stock = daily.get(stock_id)
                        if stock is None or stock.empty:
                            continue
                        candidate_indices, candidates = trigger_candidates[
                            (stock_id, confirmation.confirmation_variant_id)
                        ]
                        blocked_through_index = -1
                        stock_trade_sequence = 0
                        for _, episode in episodes.sort_values(
                            ["episode_start_trade_date", "episode_key"], kind="mergesort"
                        ).iterrows():
                            bounds = _episode_bounds(stock, episode)
                            if bounds is None:
                                continue
                            start_index, end_index = bounds
                            scan_index = max(start_index, blocked_through_index + 1)
                            episode_trade_sequence = 0
                            while scan_index <= end_index:
                                candidate_position = bisect_left(candidate_indices, scan_index)
                                if candidate_position >= len(candidates):
                                    break
                                selected = candidates[candidate_position]
                                trigger_index, confirmation_index, entry_index, continuation = selected
                                if trigger_index > end_index:
                                    break
                                simulated = _simulate_operation(
                                    stock,
                                    trigger_index=trigger_index,
                                    confirmation_index=confirmation_index,
                                    entry_index=entry_index,
                                    hold_days=hold_days,
                                    stop_policy_id=stop_policy_id,
                                )
                                episode_trade_sequence += 1
                                stock_trade_sequence += 1
                                exit_index = int(simulated.get("exit_index", len(stock) - 1))
                                row = {
                                    "generated_at": generated_at,
                                    "model_id": MODEL_ID,
                                    "artifact_id": ARTIFACT_ID,
                                    "artifact_version": ARTIFACT_VERSION,
                                    "source_artifact_id": SOURCE_ARTIFACT_ID,
                                    "source_variant_id": SOURCE_VARIANT_ID,
                                    "grid_id": grid_id,
                                    "lifecycle_order": lifecycle.lifecycle_order,
                                    "lifecycle_policy_id": lifecycle.lifecycle_policy_id,
                                    "lifecycle_role": lifecycle.lifecycle_role,
                                    "confirmation_order": confirmation.confirmation_order,
                                    "confirmation_variant_id": confirmation.confirmation_variant_id,
                                    "confirmation_information_cutoff": confirmation.information_cutoff,
                                    "base_confirmation_rule_id": BASE_CONFIRMATION_RULE_ID,
                                    "base_confirmation_rule": BASE_CONFIRMATION_RULE,
                                    "trigger_price_basis": "analysis_close",
                                    "confirmation_price_basis": "analysis_close",
                                    "bonus_id": confirmation.bonus_id,
                                    "bonus_timing_role": confirmation.bonus_timing_role,
                                    "entry_rule_id": confirmation.entry_rule_id,
                                    "entry_price_basis": "analysis_open",
                                    "holding_days": hold_days,
                                    "stop_policy_id": stop_policy_id,
                                    "stop_rule_id": STOP_RULE_ID if stop_policy_id == STOP_POLICY_ID else NO_STOP_POLICY_ID,
                                    "stop_rule": STOP_RULE if stop_policy_id == STOP_POLICY_ID else "no stop; fixed future close exit",
                                    "stop_confirmation_price_basis": "analysis_close",
                                    "fixed_exit_price_basis": "analysis_close",
                                    "intraday_operation_basis_used": False,
                                    "episode_key": str(episode["episode_key"]),
                                    "episode_start_trade_date": str(episode["episode_start_trade_date"]),
                                    "episode_end_date": str(episode["episode_end_date"]),
                                    "episode_status": str(episode["episode_status"]),
                                    "source_launch_date": str(episode["launch_date"]),
                                    "stock_id": stock_id,
                                    "stock_name": str(episode["stock_name"]),
                                    "stock_trade_sequence": stock_trade_sequence,
                                    "episode_trade_sequence": episode_trade_sequence,
                                    "rearmed_trade_flag": (
                                        lifecycle.allow_rearm and stock_trade_sequence > 1
                                    ),
                                    "trigger_date": str(stock.at[trigger_index, "date"]),
                                    "trigger_close": _stable(stock.at[trigger_index, "analysis_close"], 8),
                                    "confirmation_date": (
                                        str(stock.at[confirmation_index, "date"])
                                        if confirmation_index < len(stock)
                                        else ""
                                    ),
                                    "next_day_continuation_observed": trigger_index + 1 < len(stock),
                                    "next_day_continuation_hit": continuation,
                                    "source_anomaly_candidate_flag": (
                                        _source_anomaly_as_of_trigger(
                                            episode,
                                            stock.at[trigger_index, "date"],
                                        )
                                        if anomaly_attribution_policy_id
                                        == TRIGGER_ASOF_ANOMALY_POLICY_ID
                                        else _source_anomaly(episode)
                                    ),
                                    "unresolved_price_path_candidate_flag": _bool_value(
                                        episode["unresolved_price_path_candidate_flag"]
                                    ),
                                    "same_stock_non_overlap_policy": "entry must be after prior realized exit; rearm scans from the next trading day after exit",
                                    "outcome_definition": "win realized return > 0; neutral = 0; failure < 0",
                                    "operation_return_review_policy": OPERATION_RETURN_REVIEW_POLICY,
                                    "financial_statement_scope": FINANCIAL_STATEMENT_SCOPE,
                                    "approved_for_daily": False,
                                    "production_change": False,
                                    "promotion_readiness": "research_only_pending_operation_rule_selection",
                                }
                                if (
                                    anomaly_attribution_policy_id
                                    == TRIGGER_ASOF_ANOMALY_POLICY_ID
                                ):
                                    row["episode_source_anomaly_candidate_flag"] = (
                                        _source_anomaly(episode)
                                    )
                                    row["source_anomaly_attribution_policy_id"] = (
                                        anomaly_attribution_policy_id
                                    )
                                row.update(simulated)
                                rows.append(row)
                                blocked_through_index = max(blocked_through_index, exit_index)
                                if not lifecycle.allow_rearm or _bool_value(simulated.get("right_censored")):
                                    break
                                scan_index = blocked_through_index + 1
    detail = pd.DataFrame(rows)
    if detail.empty:
        raise RuntimeError("rearmed operation grid produced no selected operations")
    duplicate_key = ["grid_id", "stock_id", "episode_key", "trigger_date", "entry_date"]
    if detail.duplicated(duplicate_key).any():
        raise RuntimeError("rearmed operation grid has duplicate operation rows")
    return detail.sort_values(
        ["lifecycle_order", "confirmation_order", "holding_days", "stop_policy_id", "stock_id", "trigger_date"],
        kind="mergesort",
    ).reset_index(drop=True)


def _overlap_pair_count(detail: pd.DataFrame) -> int:
    group_columns = [
        "lifecycle_policy_id",
        "confirmation_variant_id",
        "holding_days",
        "stop_policy_id",
        "stock_id",
    ]
    part = detail.loc[
        detail["entry_date"].astype(str).str.fullmatch(r"\d{8}")
        & detail["exit_date"].astype(str).str.fullmatch(r"\d{8}")
    ].copy()
    if part.empty:
        return 0
    part = part.sort_values(
        [*group_columns, "entry_date", "exit_date"], kind="mergesort"
    )
    part["_entry_date_number"] = pd.to_numeric(part["entry_date"], errors="raise")
    part["_exit_date_number"] = pd.to_numeric(part["exit_date"], errors="raise")
    part["_cumulative_exit"] = part.groupby(
        group_columns, sort=False
    )["_exit_date_number"].cummax()
    part["_previous_max_exit"] = part.groupby(
        group_columns, sort=False
    )["_cumulative_exit"].shift()
    return int(part["_entry_date_number"].le(part["_previous_max_exit"]).sum())


RETURN_REVIEW_COLUMNS = [
    "generated_at",
    "model_id",
    "artifact_id",
    "artifact_version",
    "stock_id",
    "stock_name",
    "entry_date",
    "entry_price",
    "exit_date",
    "exit_price",
    "exit_price_basis",
    "realized_return_pct",
    "replayed_realized_return_pct",
    "review_trigger_threshold_pct",
    "review_candidate_grid_count",
    "review_candidate_grid_ids",
    "path_trading_row_count",
    "max_abs_raw_close_return_1d_pct",
    "max_abs_analysis_close_return_1d_pct",
    "max_abs_analysis_open_gap_pct",
    "price_resolution_ids_in_path",
    "bottom_level_price_path_result",
    "authoritative_corporate_action_layer_status",
    "review_disposition",
    "included_in_primary_metrics",
    "excluded_in_review_candidate_sensitivity",
    "approved_for_daily",
    "production_change",
]


def build_operation_return_review(
    detail: pd.DataFrame,
    daily_by_stock: dict[str, pd.DataFrame],
) -> pd.DataFrame:
    candidates = detail.loc[detail["operation_return_review_candidate_flag"].map(_bool_value)].copy()
    if candidates.empty:
        return pd.DataFrame(columns=RETURN_REVIEW_COLUMNS)
    daily = {stock_id: _normalize_stock_frame(frame) for stock_id, frame in daily_by_stock.items()}
    rows: list[dict[str, object]] = []
    key_columns = ["stock_id", "entry_date", "exit_date", "exit_price_basis"]
    for keys, group in candidates.groupby(key_columns, sort=False, dropna=False):
        stock_id, entry_date, exit_date, exit_basis = (str(value) for value in keys)
        stock = daily.get(stock_id)
        if stock is None:
            raise RuntimeError(f"operation return review is missing price history: {stock_id}")
        entry_matches = stock.index[stock["date"].eq(entry_date)]
        exit_matches = stock.index[stock["date"].eq(exit_date)]
        if not len(entry_matches) or not len(exit_matches):
            raise RuntimeError(f"operation return review path boundary is missing: {stock_id}/{entry_date}/{exit_date}")
        entry_index = int(entry_matches[0])
        exit_index = int(exit_matches[0])
        replay = stock.loc[max(0, entry_index - 1):exit_index].copy()
        path = stock.loc[entry_index:exit_index].copy()
        raw_close = pd.to_numeric(replay["close"], errors="coerce")
        analysis_close = pd.to_numeric(replay["analysis_close"], errors="coerce")
        analysis_open = pd.to_numeric(replay["analysis_open"], errors="coerce")
        raw_returns = raw_close.pct_change().iloc[1:] * 100.0
        analysis_returns = analysis_close.pct_change().iloc[1:] * 100.0
        open_gaps = (analysis_open / analysis_close.shift(1) - 1.0).iloc[1:] * 100.0
        max_raw = float(raw_returns.abs().max()) if raw_returns.notna().any() else math.nan
        max_analysis = float(analysis_returns.abs().max()) if analysis_returns.notna().any() else math.nan
        max_open_gap = float(open_gaps.abs().max()) if open_gaps.notna().any() else math.nan
        no_scale_break = all(
            np.isfinite(value) and value <= 20.0 for value in (max_raw, max_analysis, max_open_gap)
        )
        entry_price = _number(group.iloc[0]["entry_price"])
        exit_price = (
            _number(stock.at[exit_index, "analysis_open"])
            if exit_basis == "next_trading_day_open_after_stop_close_confirmation"
            else _number(stock.at[exit_index, "analysis_close"])
        )
        replayed_return = (exit_price / entry_price - 1.0) * 100.0
        recorded = pd.to_numeric(group["realized_return_pct"], errors="coerce").dropna()
        if recorded.empty or (recorded - replayed_return).abs().max() > 0.0001:
            raise RuntimeError(f"operation return review replay drift: {stock_id}/{entry_date}/{exit_date}")
        resolution_ids = sorted(
            {value for value in path["price_resolution_ids_on_date"].astype(str) if value}
        )
        first = group.iloc[0]
        rows.append(
            {
                "generated_at": str(detail["generated_at"].iloc[0]),
                "model_id": MODEL_ID,
                "artifact_id": ARTIFACT_ID,
                "artifact_version": ARTIFACT_VERSION,
                "stock_id": stock_id,
                "stock_name": str(first["stock_name"]),
                "entry_date": entry_date,
                "entry_price": round(entry_price, 8),
                "exit_date": exit_date,
                "exit_price": round(exit_price, 8),
                "exit_price_basis": exit_basis,
                "realized_return_pct": round(replayed_return, 4),
                "replayed_realized_return_pct": round(replayed_return, 4),
                "review_trigger_threshold_pct": OPERATION_RETURN_REVIEW_THRESHOLD_PCT,
                "review_candidate_grid_count": int(group["grid_id"].nunique()),
                "review_candidate_grid_ids": ";".join(sorted(set(group["grid_id"].astype(str)))),
                "path_trading_row_count": len(path),
                "max_abs_raw_close_return_1d_pct": _stable(max_raw),
                "max_abs_analysis_close_return_1d_pct": _stable(max_analysis),
                "max_abs_analysis_open_gap_pct": _stable(max_open_gap),
                "price_resolution_ids_in_path": ";".join(resolution_ids),
                "bottom_level_price_path_result": (
                    "no_single_day_scale_break_observed"
                    if no_scale_break
                    else "scale_break_or_incomplete_path_requires_root_cause_review"
                ),
                "authoritative_corporate_action_layer_status": (
                    "not_available_as_complete_shared_point_in_time_layer"
                ),
                "review_disposition": (
                    "unresolved_review_candidate_retained_in_primary_not_classified_as_anomaly"
                ),
                "included_in_primary_metrics": True,
                "excluded_in_review_candidate_sensitivity": True,
                "approved_for_daily": False,
                "production_change": False,
            }
        )
    return pd.DataFrame(rows, columns=RETURN_REVIEW_COLUMNS).sort_values(
        ["realized_return_pct", "stock_id"], ascending=[False, True], kind="mergesort"
    ).reset_index(drop=True)


def _known_trigger_dates(part: pd.DataFrame, stock_id: str) -> str:
    dates = sorted(set(part.loc[part["stock_id"].eq(stock_id), "trigger_date"].astype(str)))
    return ";".join(date for date in dates if date)


def build_operation_summary(detail: pd.DataFrame, source_detail: pd.DataFrame) -> pd.DataFrame:
    source = _normalize_source_detail(source_detail)
    source_anomaly = source.apply(_source_anomaly, axis=1)
    rows: list[dict[str, object]] = []
    group_columns = [
        "lifecycle_order",
        "lifecycle_policy_id",
        "lifecycle_role",
        "confirmation_order",
        "confirmation_variant_id",
        "confirmation_information_cutoff",
        "entry_rule_id",
        "bonus_id",
        "bonus_timing_role",
        "holding_days",
        "stop_policy_id",
        "stop_rule_id",
    ]
    for keys, full_part in detail.groupby(group_columns, sort=False, dropna=False):
        metadata = dict(zip(group_columns, keys))
        for basis in ANALYSIS_BASES:
            if basis == PRIMARY_ANALYSIS_BASIS:
                part = full_part.copy()
                basis_source = source
            else:
                part = full_part.loc[
                    ~full_part["source_anomaly_candidate_flag"].map(_bool_value)
                    & ~full_part["operation_return_review_candidate_flag"].map(_bool_value)
                ].copy()
                basis_source = source.loc[~source_anomaly].copy()
            mature = part.loc[part["return_valid"].map(_bool_value)].copy()
            outcomes = mature["return_outcome"].astype(str)
            win_count = int(outcomes.eq("win").sum())
            neutral_count = int(outcomes.eq("neutral").sum())
            failure_count = int(outcomes.eq("failure").sum())
            strict_classifiable = part.loc[
                ~part["outcome_status"].astype(str).str.startswith("right_censored")
            ].copy()
            strict_count = int(strict_classifiable["strict_success"].map(_bool_value).sum())
            stop_count = int(mature["exit_reason"].astype(str).eq(STOP_RULE_ID).sum())
            row = {
                "generated_at": str(detail["generated_at"].iloc[0]),
                "model_id": MODEL_ID,
                "artifact_id": ARTIFACT_ID,
                "artifact_version": ARTIFACT_VERSION,
                "source_artifact_id": SOURCE_ARTIFACT_ID,
                "source_variant_id": SOURCE_VARIANT_ID,
                "analysis_basis": basis,
                **metadata,
                "grid_id": "|".join(
                    (
                        str(metadata["lifecycle_policy_id"]),
                        str(metadata["confirmation_variant_id"]),
                        f"d{metadata['holding_days']}",
                        str(metadata["stop_policy_id"]),
                    )
                ),
                "base_confirmation_rule_id": BASE_CONFIRMATION_RULE_ID,
                "base_confirmation_rule": BASE_CONFIRMATION_RULE,
                "stop_rule": STOP_RULE if metadata["stop_policy_id"] == STOP_POLICY_ID else "no stop; fixed future close exit",
                "source_episode_count": len(basis_source),
                "selected_operation_count": len(part),
                "selected_episode_count": int(part["episode_key"].nunique()),
                "no_selected_operation_episode_count": int(
                    len(basis_source) - part["episode_key"].nunique()
                ),
                "unique_stock_count": int(part["stock_id"].nunique()),
                "mature_operation_count": len(mature),
                "right_censored_count": int(part["right_censored"].map(_bool_value).sum()),
                "invalid_non_censored_count": int(
                    (~part["return_valid"].map(_bool_value) & ~part["right_censored"].map(_bool_value)).sum()
                ),
                "win_count": win_count,
                "neutral_count": neutral_count,
                "failure_count": failure_count,
                "win_rate_pct": _rate(win_count, len(mature)),
                "neutral_rate_pct": _rate(neutral_count, len(mature)),
                "failure_rate_pct": _rate(failure_count, len(mature)),
                "avg_return_pct": _mean(mature["realized_return_pct"]),
                "median_return_pct": _median(mature["realized_return_pct"]),
                "p10_return_pct": _quantile(mature["realized_return_pct"], 0.10),
                "p90_return_pct": _quantile(mature["realized_return_pct"], 0.90),
                "realized_return_ge20_count": int(mature["realized_return_ge20"].map(_bool_value).sum()),
                "realized_return_ge20_rate_pct": _rate(
                    int(mature["realized_return_ge20"].map(_bool_value).sum()), len(mature)
                ),
                "strict_launch_classifiable_count": len(strict_classifiable),
                "strict_launch_success_count": strict_count,
                "strict_launch_success_rate_pct": _rate(strict_count, len(strict_classifiable)),
                "stop_exit_count": stop_count,
                "stop_exit_rate_pct": _rate(stop_count, len(mature)),
                "rearmed_operation_count": int(part["rearmed_trade_flag"].map(_bool_value).sum()),
                "same_stock_overlap_pair_count": _overlap_pair_count(part),
                "operation_return_review_candidate_count": int(
                    part["operation_return_review_candidate_flag"].map(_bool_value).sum()
                ),
                "known_4916_trigger_dates": _known_trigger_dates(part, "4916"),
                "known_1303_trigger_dates": _known_trigger_dates(part, "1303"),
                "outcome_definition": "win realized return > 0; neutral = 0; failure < 0",
                "sample_policy": "sample_count_disclosed_not_used_as_automatic_rejection",
                "anomaly_policy": "primary retains review candidates; sensitivity excludes unresolved source or return review candidates",
                "operation_return_review_policy": OPERATION_RETURN_REVIEW_POLICY,
                "same_stock_non_overlap_policy": "entry must be after prior realized exit; rearm scans from the next trading day after exit",
                "financial_statement_scope": FINANCIAL_STATEMENT_SCOPE,
                "approved_for_daily": False,
                "production_change": False,
                "promotion_readiness": "research_only_pending_operation_rule_selection",
            }
            rows.append(row)
    summary = pd.DataFrame(rows)
    benchmark = summary.loc[
        summary["lifecycle_policy_id"].eq("episode_first_match_once")
    ][
        [
            "analysis_basis",
            "confirmation_variant_id",
            "holding_days",
            "stop_policy_id",
            "selected_operation_count",
            "win_rate_pct",
            "avg_return_pct",
            "median_return_pct",
        ]
    ].rename(
        columns={
            "selected_operation_count": "benchmark_selected_operation_count",
            "win_rate_pct": "benchmark_win_rate_pct",
            "avg_return_pct": "benchmark_avg_return_pct",
            "median_return_pct": "benchmark_median_return_pct",
        }
    )
    summary = summary.merge(
        benchmark,
        on=["analysis_basis", "confirmation_variant_id", "holding_days", "stop_policy_id"],
        how="left",
        validate="many_to_one",
    )
    for metric in ("selected_operation_count", "win_rate_pct", "avg_return_pct", "median_return_pct"):
        baseline_column = f"benchmark_{metric}"
        summary[f"delta_vs_first_match_{metric}"] = pd.to_numeric(
            summary[metric], errors="coerce"
        ) - pd.to_numeric(summary[baseline_column], errors="coerce")
        summary[f"delta_vs_first_match_{metric}"] = summary[
            f"delta_vs_first_match_{metric}"
        ].round(4)
    summary["metric_threshold_met_ignoring_sample_size"] = (
        pd.to_numeric(summary["win_rate_pct"], errors="coerce").ge(60.0)
        & pd.to_numeric(summary["avg_return_pct"], errors="coerce").gt(0.0)
        & pd.to_numeric(summary["median_return_pct"], errors="coerce").gt(0.0)
    )
    return summary.sort_values(
        ["analysis_basis", "lifecycle_order", "confirmation_order", "holding_days", "stop_policy_id"],
        kind="mergesort",
    ).reset_index(drop=True)


def build_rearmed_operation_grid(
    prepared: pd.DataFrame | None = None,
    source_detail: pd.DataFrame | None = None,
    daily_by_stock: dict[str, pd.DataFrame] | None = None,
    source_projection_manifest: pd.DataFrame | None = None,
    *,
    anomaly_attribution_policy_id: str = EPISODE_AGGREGATE_ANOMALY_POLICY_ID,
    generated_at: str | None = None,
) -> tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    raw_source = load_projected_source_detail() if source_detail is None else source_detail
    projection_manifest = (
        load_source_snapshot_projection_manifest()
        if source_projection_manifest is None
        else source_projection_manifest
    )
    validate_projection_binding(projection_manifest, raw_source)
    if anomaly_attribution_policy_id == TRIGGER_ASOF_ANOMALY_POLICY_ID:
        raw_source = attach_qualifying_event_anomaly_flags(
            raw_source,
            observation_cutoff_date=PRICE_HISTORY_CUTOFF_DATE,
        )
    source = _normalize_source_detail(raw_source)
    _assert_source_within_price_history_cutoff(source)
    if daily_by_stock is None:
        if prepared is None:
            raise RuntimeError("prepared research frame is required when daily_by_stock is not supplied")
        daily_by_stock = prepare_daily_by_stock(
            prepared,
            source,
            observation_cutoff_date=PRICE_HISTORY_CUTOFF_DATE,
        )
    daily_by_stock = _apply_price_history_cutoff(daily_by_stock)
    generated_at_value = generated_at or _now_text()
    detail = build_operation_detail(
        source,
        daily_by_stock,
        generated_at_value,
        anomaly_attribution_policy_id=anomaly_attribution_policy_id,
    )
    review = build_operation_return_review(detail, daily_by_stock)
    summary = build_operation_summary(detail, source)
    selected_version = artifact_version_for_projection(
        projection_manifest.iloc[0]["projection_version"],
        anomaly_attribution_policy_id=anomaly_attribution_policy_id,
    )
    for frame in (summary, detail, review):
        frame.loc[:, "artifact_version"] = selected_version
        if anomaly_attribution_policy_id == TRIGGER_ASOF_ANOMALY_POLICY_ID:
            frame.loc[:, "source_anomaly_attribution_policy_id"] = (
                anomaly_attribution_policy_id
            )
    return summary, detail, review


def _markdown_table(frame: pd.DataFrame, columns: list[str], limit: int = 40) -> str:
    if frame.empty:
        return "_No rows._"
    view = frame.loc[:, columns].head(limit).astype(str).replace({"nan": "", "NaN": "", "<NA>": ""})
    lines = ["| " + " | ".join(columns) + " |", "| " + " | ".join(["---"] * len(columns)) + " |"]
    for _, row in view.iterrows():
        lines.append("| " + " | ".join(str(row[column]) for column in columns) + " |")
    return "\n".join(lines)


def _markdown(summary: pd.DataFrame, detail: pd.DataFrame, review: pd.DataFrame) -> str:
    primary = summary.loc[summary["analysis_basis"].eq(PRIMARY_ANALYSIS_BASIS)].copy()
    adopted = primary.loc[
        primary["lifecycle_policy_id"].eq("rearm_after_realized_exit_next_trade_day")
    ].sort_values(
        ["metric_threshold_met_ignoring_sample_size", "win_rate_pct", "avg_return_pct"],
        ascending=[False, False, False],
        kind="mergesort",
    )
    known = detail.loc[
        detail["lifecycle_policy_id"].eq("rearm_after_realized_exit_next_trade_day")
        & detail["stock_id"].isin(["4916", "1303"])
        & detail["holding_days"].eq(20)
        & detail["stop_policy_id"].eq(NO_STOP_POLICY_ID)
    ].copy()
    lines = [
        "# 營收改善尚未反應模型：重新武裝操作矩陣",
        "",
        f"- generated_at: `{summary['generated_at'].iloc[0]}`",
        f"- model_id: `{MODEL_ID}`",
        f"- artifact_version: `{summary['artifact_version'].iloc[0]}`",
        "- 狀態：`research_only`，不修改 production registry、operation adapter 或 PDF。",
        "- 基礎確認：訊號日收盤首次突破前 20 日最高收盤，且 MA60 > MA120；下一交易日開盤進場。",
        "- 隔日續攻加分：只能在 D+1 收盤確認，若用於買進決策必須改為 D+2 開盤進場，不能回填成 D+1 開盤資訊。",
        "- 重新武裝：前一筆實際出場後，最早從下一交易日重新尋找訊號；同股操作不得重疊。",
        "- 出場矩陣：D+10 / D+15 / D+20 / D+30 固定收盤，分別比較無停損與 MA20/EMA23 四日收盤停損。",
        "- 勝／和／敗：實現報酬 > 0 / = 0 / < 0。嚴格 +20% 發動標籤另列，不與操作勝率混用。",
        "- 盤中 high/low 不作 entry、exit、stop 或 realized return basis。",
        "- 月營收與財報分離：EPS、毛利率、營益率、營業利益、業外、淨利均未納入。",
        "",
        "## 採用 lifecycle 的主要矩陣",
        "",
        _markdown_table(
            adopted,
            [
                "confirmation_variant_id",
                "holding_days",
                "stop_policy_id",
                "mature_operation_count",
                "win_rate_pct",
                "neutral_rate_pct",
                "failure_rate_pct",
                "avg_return_pct",
                "median_return_pct",
                "realized_return_ge20_rate_pct",
                "rearmed_operation_count",
                "same_stock_overlap_pair_count",
            ],
        ),
        "",
        "## 事欣科與南亞",
        "",
        _markdown_table(
            known,
            [
                "stock_id",
                "stock_name",
                "confirmation_variant_id",
                "trigger_date",
                "entry_date",
                "exit_date",
                "realized_return_pct",
                "return_outcome",
                "episode_trade_sequence",
                "rearmed_trade_flag",
            ],
            limit=30,
        ),
        "",
        "## 高報酬底層 review",
        "",
        f"- review rows: `{len(review)}`。高低報酬只觸發查核，不直接判定異常。",
    ]
    return "\n".join(lines).rstrip() + "\n"


def write_rearmed_operation_grid(
    summary: pd.DataFrame,
    detail: pd.DataFrame,
    review: pd.DataFrame,
) -> None:
    for path in (
        LATEST_CSV,
        DETAIL_CSV,
        RETURN_REVIEW_CSV,
        LATEST_MD,
        HISTORY_CSV,
        HISTORY_RETURN_REVIEW_CSV,
        DOCS_CSV,
        DOCS_RETURN_REVIEW_CSV,
        DOCS_MD,
    ):
        path.parent.mkdir(parents=True, exist_ok=True)
    summary.to_csv(LATEST_CSV, index=False, encoding="utf-8-sig")
    detail_artifact = detail.drop(columns=list(DETAIL_ARTIFACT_DROP_COLUMNS), errors="raise")
    detail_artifact.to_csv(DETAIL_CSV, index=False, encoding="utf-8-sig")
    review.to_csv(RETURN_REVIEW_CSV, index=False, encoding="utf-8-sig")
    markdown = _markdown(summary, detail, review)
    LATEST_MD.write_text(markdown, encoding="utf-8")
    HISTORY_CSV.write_bytes(LATEST_CSV.read_bytes())
    HISTORY_RETURN_REVIEW_CSV.write_bytes(RETURN_REVIEW_CSV.read_bytes())
    DOCS_CSV.write_bytes(LATEST_CSV.read_bytes())
    DOCS_RETURN_REVIEW_CSV.write_bytes(RETURN_REVIEW_CSV.read_bytes())
    DOCS_MD.write_bytes(LATEST_MD.read_bytes())
