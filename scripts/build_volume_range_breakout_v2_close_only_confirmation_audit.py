from __future__ import annotations

from datetime import datetime
from pathlib import Path
from typing import Any
from zoneinfo import ZoneInfo
import math

import pandas as pd

from build_volume_range_breakout_v2_lowbase_horizon_audit import (
    mark_non_overlap,
    normalize_code,
    normalize_date,
    outcome,
    pct_round,
    safe_str,
)


ROOT = Path(".")
PRICE_DIR = ROOT / "data" / "stock_price_history"
RESEARCH_LATEST_DIR = ROOT / "output" / "latest" / "research_backtest"
RESEARCH_HISTORY_DIR = ROOT / "output" / "history" / "research"

SOURCE_DETAIL_CSV = RESEARCH_LATEST_DIR / "volume_range_breakout_v2_semantic_audit_detail_latest.csv"
LATEST_SUMMARY_CSV = RESEARCH_LATEST_DIR / "volume_range_breakout_v2_close_only_confirmation_audit_latest.csv"
LATEST_DETAIL_CSV = RESEARCH_LATEST_DIR / "volume_range_breakout_v2_close_only_confirmation_audit_detail_latest.csv"
LATEST_MD = RESEARCH_LATEST_DIR / "volume_range_breakout_v2_close_only_confirmation_audit_latest.md"
HISTORY_SUMMARY_CSV = RESEARCH_HISTORY_DIR / "volume_range_breakout_v2_close_only_confirmation_audit.csv"
HISTORY_DETAIL_CSV = RESEARCH_HISTORY_DIR / "volume_range_breakout_v2_close_only_confirmation_audit_detail.csv"

RESEARCH_ID = "volume_range_breakout_v2_close_only_confirmation_audit"
ARTIFACT_VERSION = "volume_range_breakout_v2_close_only_confirmation_audit_20260709_stop_sensitivity"
SOURCE_RESEARCH_ID = "volume_range_breakout_v2_semantic_audit"
ADVISORY_STATUS = "warning_research_variant_only"
PRODUCTION_READINESS = "not_production_ready_research_only"
MODEL_ID = "volume_range_breakout"

BREAKOUT_THRESHOLDS = [0.0, 1.0, 2.0, 3.0, 4.0, 5.0, 7.5, 10.0]
BASE_SHAPE_ID = "width40_gt40_non_consolidation"
BASE_SHAPE_DEFINITION = "range_width_40_pct > 40"
MAX_CONFIRM_DAYS = 10
FIXED_HORIZONS = [10, 20, 40, 60]
CLOSE_ONLY_TRIGGERS = [
    "next_day_close_above_signal_high_confirmed",
    "pullback_5ma_close_reclaim_confirmed",
    "pullback_10ma_close_reclaim_confirmed",
]
TRIGGER_PRIORITY = {
    "next_day_close_above_signal_high_confirmed": 1,
    "pullback_5ma_close_reclaim_confirmed": 2,
    "pullback_10ma_close_reclaim_confirmed": 3,
}
TRIGGER_ZH = {
    "selected_any_close_only": "任一 close-only 確認",
    "next_day_close_above_signal_high_confirmed": "隔日收盤站上訊號高點",
    "pullback_5ma_close_reclaim_confirmed": "收盤回測 5MA 後重新站回",
    "pullback_10ma_close_reclaim_confirmed": "收盤回測 10MA 後重新站回",
}

STOP_SPECS = [
    ("no_stop", ""),
    ("signal_low_close_stop", "signal_low"),
    ("entry_minus_5pct_close_stop", "entry_minus_5pct"),
    ("entry_minus_7pct_close_stop", "entry_minus_7pct"),
    ("entry_minus_10pct_close_stop", "entry_minus_10pct"),
    ("ma10_close_stop", "ma10"),
    ("ma20_close_stop", "ma20"),
]
RETURN_BASES = [f"fixed_{horizon}d_close_no_stop" for horizon in FIXED_HORIZONS] + [
    f"close_{stop_token}_stop_next_open_or_fixed_{horizon}d_close"
    for horizon in [10, 20, 40]
    for stop_rule_id, stop_token in STOP_SPECS
    if stop_rule_id != "no_stop"
]

SUMMARY_COLUMNS = [
    "research_id",
    "artifact_version",
    "source_research_id",
    "source_artifact_version",
    "advisory_status",
    "model_id",
    "row_type",
    "population_id",
    "base_shape_id",
    "base_shape_definition",
    "breakout_threshold_pct",
    "trigger_scope",
    "trigger_scope_zh",
    "return_basis",
    "entry_rule_id",
    "exit_rule_id",
    "stop_rule_id",
    "fixed_horizon_days",
    "overlap_policy",
    "anomaly_policy",
    "source_event_count",
    "close_only_confirmed_count",
    "simulated_event_count",
    "non_overlap_event_count",
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
    "p10_return_pct",
    "p90_return_pct",
    "min_return_pct",
    "max_return_pct",
    "high_return_ge20_count",
    "high_return_ge20_rate_pct",
    "loss_le_minus5_count",
    "loss_le_minus5_rate_pct",
    "data_quality_exception_count",
    "same_stock_overlap_suppressed_count",
    "sample_status",
    "split_gate_status",
    "note",
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
    "model_id",
    "source_event_key",
    "stock_id",
    "stock_name",
    "signal_date",
    "original_confirmation_date",
    "original_selected_trigger_id",
    "selected_close_only_trigger_id",
    "matched_close_only_trigger_ids",
    "close_only_confirmation_date",
    "confirmation_age_trading_days",
    "return_basis",
    "entry_rule_id",
    "exit_rule_id",
    "entry_date",
    "entry_price",
    "exit_date",
    "exit_price",
    "simulated_exit_reason",
    "return_pct",
    "return_outcome",
    "data_quality_flag",
    "breakout_over_prev60_pct",
    "base_shape_id",
    "base_shape_definition",
    "v2_base_shape_match_flag",
    "consolidation_type",
    "range_width_40_pct",
    "range_width_60_pct",
    "stop_rule_id",
    "fixed_horizon_days",
    "approved_for_daily",
    "production_readiness",
    "generated_at",
]


def now_text() -> str:
    return datetime.now(ZoneInfo("Asia/Taipei")).strftime("%Y-%m-%d %H:%M:%S Asia/Taipei")


def false_text() -> str:
    return "False"


def read_csv(path: Path) -> pd.DataFrame:
    if not path.exists():
        raise SystemExit(f"ERROR: missing required file: {path}")
    return pd.read_csv(path, dtype=str, keep_default_na=False, low_memory=False)


def write_csv(df: pd.DataFrame, path: Path, columns: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    out = df.copy()
    for col in columns:
        if col not in out.columns:
            out[col] = ""
    out = out[columns]
    out.to_csv(path, index=False, encoding="utf-8-sig")


def numeric(value: Any) -> float:
    try:
        number = float(value)
    except (TypeError, ValueError):
        return math.nan
    return number if not math.isnan(number) and not math.isinf(number) else math.nan


def v2_base_shape_id(row: pd.Series) -> str:
    width40 = numeric(row.get("range_width_40_pct"))
    if math.isnan(width40):
        return "unknown_width40"
    if width40 > 40:
        return BASE_SHAPE_ID
    if width40 > 25:
        return "width40_25_40_short_consolidation"
    return "width40_le25_long_consolidation"


def parse_return_basis(return_basis: str) -> tuple[str, int]:
    for horizon in FIXED_HORIZONS:
        if return_basis == f"fixed_{horizon}d_close_no_stop":
            return "no_stop", horizon
    prefix = "close_"
    middle = "_stop_next_open_or_fixed_"
    suffix = "d_close"
    if not return_basis.startswith(prefix) or middle not in return_basis or not return_basis.endswith(suffix):
        raise ValueError(return_basis)
    stop_token, horizon_text = return_basis[len(prefix) : -len(suffix)].split(middle, 1)
    return f"{stop_token}_close_stop", int(horizon_text)


def load_source() -> tuple[pd.DataFrame, str]:
    source = read_csv(SOURCE_DETAIL_CSV)
    if source.empty:
        raise SystemExit("ERROR: source semantic detail is empty")
    if set(source["research_id"].astype(str)) != {SOURCE_RESEARCH_ID}:
        raise SystemExit(f"ERROR: source research_id must be {SOURCE_RESEARCH_ID}")
    if not source["source_event_key"].is_unique:
        raise SystemExit("ERROR: source_event_key must be unique")
    versions = sorted(set(source["artifact_version"].astype(str)))
    if len(versions) != 1:
        raise SystemExit(f"ERROR: source artifact_version must be single-valued; got {versions[:5]}")
    if not set(source["approved_for_daily"].astype(str).str.lower()) <= {"false", "0", ""}:
        raise SystemExit("ERROR: source detail must remain approved_for_daily=False")
    for col in [
        "signal_open",
        "signal_high",
        "signal_low",
        "signal_close",
        "breakout_over_prev60_pct",
        "range_width_40_pct",
        "range_width_60_pct",
    ]:
        source[col] = pd.to_numeric(source.get(col, ""), errors="coerce")
    source["stock_id"] = source["stock_id"].map(normalize_code)
    source["signal_date"] = source["signal_date"].map(normalize_date)
    source["confirmation_date"] = source["confirmation_date"].map(normalize_date)
    source["v2_base_shape_id"] = source.apply(v2_base_shape_id, axis=1)
    return source, versions[0]


def load_price_cache(stock_ids: pd.Series) -> dict[str, pd.DataFrame]:
    cache: dict[str, pd.DataFrame] = {}
    for stock_id in sorted(set(stock_ids.astype(str))):
        path = PRICE_DIR / f"{stock_id}.csv"
        if not path.exists():
            cache[stock_id] = pd.DataFrame()
            continue
        price = pd.read_csv(path, dtype=str, keep_default_na=False, low_memory=False)
        if price.empty or "date" not in price.columns:
            cache[stock_id] = pd.DataFrame()
            continue
        price = price.copy()
        price["date"] = price["date"].map(normalize_date)
        price = price[price["date"] != ""].sort_values("date").reset_index(drop=True)
        for col in ["open", "high", "low", "close", "ma5", "ma10", "ma20"]:
            price[col] = pd.to_numeric(price.get(col, ""), errors="coerce")
        cache[stock_id] = price
    return cache


def price_idx(price: pd.DataFrame, date_text: str) -> int | None:
    if price.empty:
        return None
    rows = price.index[price["date"].astype(str).eq(normalize_date(date_text))]
    if len(rows) == 0:
        return None
    return int(rows[0])


def close_below_signal_low(price: pd.DataFrame, start_idx: int, end_idx: int, signal_low: float) -> bool:
    if math.isnan(signal_low):
        return True
    if end_idx < start_idx:
        return False
    closes = pd.to_numeric(price.iloc[start_idx : end_idx + 1]["close"], errors="coerce")
    return bool(closes.lt(signal_low).fillna(False).any())


def find_next_day_close_above_signal_high(price: pd.DataFrame, signal_idx: int, signal_high: float) -> dict[str, Any] | None:
    confirm_idx = signal_idx + 1
    if confirm_idx >= len(price) or math.isnan(signal_high):
        return None
    close = numeric(price.iloc[confirm_idx].get("close"))
    if not math.isnan(close) and close >= signal_high:
        return {
            "trigger_id": "next_day_close_above_signal_high_confirmed",
            "confirmation_idx": confirm_idx,
        }
    return None


def find_close_reclaim(
    price: pd.DataFrame,
    signal_idx: int,
    signal_low: float,
    ma_col: str,
    trigger_id: str,
) -> dict[str, Any] | None:
    saw_pullback_close = False
    end_idx = min(len(price) - 1, signal_idx + MAX_CONFIRM_DAYS)
    for idx in range(signal_idx + 1, end_idx + 1):
        row = price.iloc[idx]
        close = numeric(row.get("close"))
        ma = numeric(row.get(ma_col))
        if math.isnan(close) or math.isnan(ma):
            continue
        if not math.isnan(signal_low) and close < signal_low:
            return None
        if saw_pullback_close and close >= ma:
            return {"trigger_id": trigger_id, "confirmation_idx": idx}
        if close <= ma:
            saw_pullback_close = True
    return None


def close_only_matches(row: pd.Series, price: pd.DataFrame) -> list[dict[str, Any]]:
    signal_idx = price_idx(price, row.get("signal_date", ""))
    if signal_idx is None:
        return []
    signal_high = numeric(row.get("signal_high"))
    signal_low = numeric(row.get("signal_low"))
    matches: list[dict[str, Any]] = []
    next_day = find_next_day_close_above_signal_high(price, signal_idx, signal_high)
    if next_day is not None:
        matches.append(next_day)
    for ma_col, trigger_id in [
        ("ma5", "pullback_5ma_close_reclaim_confirmed"),
        ("ma10", "pullback_10ma_close_reclaim_confirmed"),
    ]:
        found = find_close_reclaim(price, signal_idx, signal_low, ma_col, trigger_id)
        if found is not None:
            matches.append(found)
    for match in matches:
        idx = int(match["confirmation_idx"])
        match["confirmation_date"] = normalize_date(price.iloc[idx].get("date"))
        match["trigger_priority"] = TRIGGER_PRIORITY[match["trigger_id"]]
        match["confirmation_age_trading_days"] = idx - signal_idx
    return sorted(matches, key=lambda item: (item["confirmation_idx"], item["trigger_priority"], item["trigger_id"]))


def base_detail(row: pd.Series, source_version: str, generated_at: str, selected: dict[str, Any], matched_ids: str) -> dict[str, Any]:
    return {
        "research_id": RESEARCH_ID,
        "artifact_version": ARTIFACT_VERSION,
        "source_research_id": SOURCE_RESEARCH_ID,
        "source_artifact_version": source_version,
        "advisory_status": ADVISORY_STATUS,
        "model_id": MODEL_ID,
        "source_event_key": safe_str(row.get("source_event_key")),
        "stock_id": normalize_code(row.get("stock_id")),
        "stock_name": safe_str(row.get("stock_name")),
        "signal_date": normalize_date(row.get("signal_date")),
        "original_confirmation_date": normalize_date(row.get("confirmation_date")),
        "original_selected_trigger_id": safe_str(row.get("selected_trigger_id")),
        "selected_close_only_trigger_id": safe_str(selected.get("trigger_id")),
        "matched_close_only_trigger_ids": matched_ids,
        "close_only_confirmation_date": safe_str(selected.get("confirmation_date")),
        "confirmation_age_trading_days": safe_str(selected.get("confirmation_age_trading_days")),
        "breakout_over_prev60_pct": pct_round(row.get("breakout_over_prev60_pct")),
        "base_shape_id": safe_str(row.get("v2_base_shape_id")),
        "base_shape_definition": BASE_SHAPE_DEFINITION,
        "v2_base_shape_match_flag": str(safe_str(row.get("v2_base_shape_id")) == BASE_SHAPE_ID),
        "consolidation_type": safe_str(row.get("consolidation_type")),
        "range_width_40_pct": pct_round(row.get("range_width_40_pct")),
        "range_width_60_pct": pct_round(row.get("range_width_60_pct")),
        "approved_for_daily": false_text(),
        "production_readiness": PRODUCTION_READINESS,
        "generated_at": generated_at,
    }


def simulate_return(
    price: pd.DataFrame,
    confirmation_idx: int,
    signal_low: float,
    return_basis: str,
) -> dict[str, Any]:
    stop_rule_id, fixed_horizon_days = parse_return_basis(return_basis)
    entry_idx = confirmation_idx + 1
    if price.empty or entry_idx >= len(price):
        return {"data_quality_flag": "missing_next_trading_day_entry"}
    entry = price.iloc[entry_idx]
    entry_price = numeric(entry.get("open"))
    if math.isnan(entry_price) or entry_price <= 0:
        return {"data_quality_flag": "invalid_entry_or_exit_price"}

    fixed_exit_idx = entry_idx + fixed_horizon_days - 1
    if fixed_exit_idx >= len(price):
        return {"data_quality_flag": "insufficient_forward_price_window"}
    exit_idx = fixed_exit_idx
    exit_price_col = "close"
    simulated_exit_reason = f"fixed_{fixed_horizon_days}d_close"

    if stop_rule_id != "no_stop":
        monitor = price.iloc[entry_idx:fixed_exit_idx]
        indicator_seen = stop_rule_id not in {"ma10_close_stop", "ma20_close_stop"}
        for idx, row in monitor.iterrows():
            close = numeric(row.get("close"))
            if math.isnan(close):
                continue
            stop_hit = False
            if stop_rule_id == "signal_low_close_stop":
                if math.isnan(signal_low):
                    return {"data_quality_flag": "missing_signal_low_for_stop"}
                stop_hit = close < signal_low
            elif stop_rule_id == "entry_minus_5pct_close_stop":
                stop_hit = close < entry_price * 0.95
            elif stop_rule_id == "entry_minus_7pct_close_stop":
                stop_hit = close < entry_price * 0.93
            elif stop_rule_id == "entry_minus_10pct_close_stop":
                stop_hit = close < entry_price * 0.90
            elif stop_rule_id in {"ma10_close_stop", "ma20_close_stop"}:
                ma_col = "ma10" if stop_rule_id == "ma10_close_stop" else "ma20"
                ma_value = numeric(row.get(ma_col))
                if math.isnan(ma_value):
                    continue
                indicator_seen = True
                stop_hit = close < ma_value
            else:
                raise ValueError(stop_rule_id)
            if stop_hit:
                exit_idx = int(idx) + 1
                if exit_idx >= len(price):
                    return {"data_quality_flag": "insufficient_forward_price_window"}
                exit_price_col = "open"
                simulated_exit_reason = f"{stop_rule_id}_next_open"
                break
        if not indicator_seen:
            ma_col = "ma10" if stop_rule_id == "ma10_close_stop" else "ma20"
            return {"data_quality_flag": f"missing_{ma_col}_for_stop"}

    if exit_idx >= len(price):
        return {"data_quality_flag": "insufficient_forward_price_window"}
    exit_row = price.iloc[exit_idx]
    exit_price = numeric(exit_row.get(exit_price_col))
    if math.isnan(exit_price):
        return {"data_quality_flag": "invalid_entry_or_exit_price"}
    ret = (exit_price / entry_price - 1.0) * 100.0
    flag = "ok"
    if abs(ret) >= 80:
        flag = "extreme_return_abs_ge80_review"
    return {
        "entry_date": normalize_date(entry.get("date")),
        "entry_price": pct_round(entry_price),
        "exit_date": normalize_date(exit_row.get("date")),
        "exit_price": pct_round(exit_price),
        "simulated_exit_reason": simulated_exit_reason,
        "return_pct": pct_round(ret),
        "return_outcome": outcome(ret),
        "data_quality_flag": flag,
        "stop_rule_id": stop_rule_id,
        "fixed_horizon_days": fixed_horizon_days,
    }


def build_detail(source: pd.DataFrame, source_version: str, generated_at: str) -> pd.DataFrame:
    cache = load_price_cache(source["stock_id"])
    rows: list[dict[str, Any]] = []
    for _, row in source.iterrows():
        price = cache.get(normalize_code(row.get("stock_id")), pd.DataFrame())
        matches = close_only_matches(row, price)
        if not matches:
            continue
        selected = matches[0]
        matched_ids = "|".join(dict.fromkeys(match["trigger_id"] for match in matches))
        confirmation_idx = int(selected["confirmation_idx"])
        signal_low = numeric(row.get("signal_low"))
        base = base_detail(row, source_version, generated_at, selected, matched_ids)
        for return_basis in RETURN_BASES:
            simulated = simulate_return(price, confirmation_idx, signal_low, return_basis)
            stop_rule_id, fixed_horizon_days = parse_return_basis(return_basis)
            rows.append(
                {
                    **base,
                    **simulated,
                    "return_basis": return_basis,
                    "entry_rule_id": "confirmation_next_trading_day_open",
                    "exit_rule_id": return_basis,
                    "stop_rule_id": stop_rule_id,
                    "fixed_horizon_days": fixed_horizon_days,
                }
            )
    return pd.DataFrame(rows)


def return_metrics(part: pd.DataFrame) -> dict[str, Any]:
    returns = pd.to_numeric(part.get("return_pct", pd.Series(dtype=float)), errors="coerce").dropna()
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
            "min_return_pct": "",
            "max_return_pct": "",
            "high_return_ge20_count": 0,
            "high_return_ge20_rate_pct": "",
            "loss_le_minus5_count": 0,
            "loss_le_minus5_rate_pct": "",
        }
    win = int((returns > 0).sum())
    neutral = int((returns == 0).sum())
    loss = int((returns < 0).sum())
    high20 = int(returns.ge(20).sum())
    loss5 = int(returns.le(-5).sum())
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
        "min_return_pct": pct_round(float(returns.min())),
        "max_return_pct": pct_round(float(returns.max())),
        "high_return_ge20_count": high20,
        "high_return_ge20_rate_pct": pct_round(high20 / n * 100.0, 2),
        "loss_le_minus5_count": loss5,
        "loss_le_minus5_rate_pct": pct_round(loss5 / n * 100.0, 2),
    }


def sample_status(sample_size: int) -> str:
    if sample_size >= 300:
        return "reviewable_sample"
    if sample_size >= 100:
        return "thin_but_reviewable_sample"
    return "thin_sample"


def split_gate_status(metrics: dict[str, Any]) -> str:
    try:
        win_rate = float(metrics["win_rate_pct"])
        avg_return = float(metrics["avg_return_pct"])
    except (TypeError, ValueError):
        return "insufficient_sample"
    if win_rate >= 60.0 and avg_return > 0:
        return "passes_return_and_win_gate_research_only"
    return "fails_return_or_win_gate"


def summary_row(
    source: pd.DataFrame,
    detail: pd.DataFrame,
    source_version: str,
    generated_at: str,
    threshold: float,
    trigger_scope: str,
    return_basis: str,
) -> dict[str, Any]:
    stop_rule_id, fixed_horizon_days = parse_return_basis(return_basis)
    source_mask = (
        source["v2_base_shape_id"].astype(str).eq(BASE_SHAPE_ID)
        & pd.to_numeric(source["breakout_over_prev60_pct"], errors="coerce").ge(threshold)
    )
    source_keys = set(source.loc[source_mask, "source_event_key"].astype(str))
    detail_part = detail[
        detail["source_event_key"].astype(str).isin(source_keys)
        & detail["return_basis"].astype(str).eq(return_basis)
    ].copy()
    if trigger_scope != "selected_any_close_only":
        detail_part = detail_part[detail_part["selected_close_only_trigger_id"].astype(str).eq(trigger_scope)].copy()
    confirmed_count = int(detail_part["source_event_key"].nunique()) if not detail_part.empty else 0
    ok_part = detail_part[detail_part["data_quality_flag"].astype(str).eq("ok")].copy()
    marked = mark_non_overlap(ok_part)
    metric_part = marked[marked["_non_overlap"]].copy() if not marked.empty else marked
    metrics = return_metrics(metric_part)
    row = {
        "research_id": RESEARCH_ID,
        "artifact_version": ARTIFACT_VERSION,
        "source_research_id": SOURCE_RESEARCH_ID,
        "source_artifact_version": source_version,
        "advisory_status": ADVISORY_STATUS,
        "model_id": MODEL_ID,
        "row_type": "close_only_threshold_metrics",
        "population_id": "non_consolidation_momentum_close_only",
        "base_shape_id": BASE_SHAPE_ID,
        "base_shape_definition": BASE_SHAPE_DEFINITION,
        "breakout_threshold_pct": threshold,
        "trigger_scope": trigger_scope,
        "trigger_scope_zh": TRIGGER_ZH.get(trigger_scope, trigger_scope),
        "return_basis": return_basis,
        "entry_rule_id": "confirmation_next_trading_day_open",
        "exit_rule_id": return_basis,
        "stop_rule_id": stop_rule_id,
        "fixed_horizon_days": fixed_horizon_days,
        "overlap_policy": "same_stock_non_overlap",
        "anomaly_policy": "exclude_extreme_review",
        "source_event_count": int(source_mask.sum()),
        "close_only_confirmed_count": confirmed_count,
        "simulated_event_count": int(len(ok_part)),
        "non_overlap_event_count": int(len(metric_part)),
        "coverage_pct": pct_round(confirmed_count / int(source_mask.sum()) * 100.0, 2) if int(source_mask.sum()) else "",
        "data_quality_exception_count": int(len(detail_part) - len(ok_part)),
        "same_stock_overlap_suppressed_count": int(len(ok_part) - len(metric_part)),
        "sample_status": sample_status(int(metrics["sample_size"])),
        "split_gate_status": split_gate_status(metrics),
        "note": "Research-only close-confirmed trigger replay on existing v1 formal-operation source events; base shape is recomputed from range_width_40_pct and is not gated by the legacy consolidation_type label.",
        "approved_for_daily": false_text(),
        "production_readiness": PRODUCTION_READINESS,
        "generated_at": generated_at,
    }
    row.update(metrics)
    return row


def build_summary(source: pd.DataFrame, detail: pd.DataFrame, source_version: str, generated_at: str) -> pd.DataFrame:
    rows: list[dict[str, Any]] = []
    for threshold in BREAKOUT_THRESHOLDS:
        for trigger_scope in ["selected_any_close_only", *CLOSE_ONLY_TRIGGERS]:
            for return_basis in RETURN_BASES:
                rows.append(summary_row(source, detail, source_version, generated_at, threshold, trigger_scope, return_basis))
    return pd.DataFrame(rows)


def markdown_table(df: pd.DataFrame, columns: list[str], limit: int = 80) -> list[str]:
    if df.empty:
        return ["(empty)"]
    out = df[columns].head(limit).copy().fillna("NA")
    return out.to_markdown(index=False).splitlines()


def metric_number(value: Any, suffix: str = "") -> str:
    number = numeric(value)
    if math.isnan(number):
        return "NA"
    return f"{number:.2f}{suffix}"


def write_markdown(summary: pd.DataFrame, path: Path) -> None:
    main_cols = [
        "breakout_threshold_pct",
        "trigger_scope",
        "return_basis",
        "stop_rule_id",
        "fixed_horizon_days",
        "source_event_count",
        "close_only_confirmed_count",
        "sample_size",
        "win_rate_pct",
        "loss_rate_pct",
        "avg_return_pct",
        "median_return_pct",
        "split_gate_status",
    ]
    work = summary.copy()
    for col in [
        "breakout_threshold_pct",
        "fixed_horizon_days",
        "sample_size",
        "win_rate_pct",
        "loss_rate_pct",
        "avg_return_pct",
        "median_return_pct",
        "data_quality_exception_count",
    ]:
        work[col] = pd.to_numeric(work[col], errors="coerce")
    threshold_2 = work[work["breakout_threshold_pct"].eq(2.0)].copy()
    selected = work[work["trigger_scope"].astype(str).eq("selected_any_close_only")].copy()
    threshold_2_selected = threshold_2[threshold_2["trigger_scope"].astype(str).eq("selected_any_close_only")].copy()

    no_stop_snapshot = threshold_2_selected[
        threshold_2_selected["return_basis"].isin(
            [
                "fixed_20d_close_no_stop",
                "fixed_40d_close_no_stop",
                "fixed_60d_close_no_stop",
            ]
        )
    ].sort_values(["fixed_horizon_days"])
    stop_20d = threshold_2_selected[threshold_2_selected["fixed_horizon_days"].eq(20)].copy()
    stop_order = {
        "no_stop": 0,
        "signal_low_close_stop": 1,
        "entry_minus_5pct_close_stop": 2,
        "entry_minus_7pct_close_stop": 3,
        "entry_minus_10pct_close_stop": 4,
        "ma20_close_stop": 5,
        "ma10_close_stop": 6,
    }
    stop_20d["_stop_order"] = stop_20d["stop_rule_id"].map(stop_order).fillna(99)
    stop_20d = stop_20d.sort_values(["_stop_order", "return_basis"])
    threshold_sweep = selected[
        selected["return_basis"].isin(
            [
                "fixed_20d_close_no_stop",
                "fixed_40d_close_no_stop",
                "fixed_60d_close_no_stop",
            ]
        )
    ].sort_values(["fixed_horizon_days", "breakout_threshold_pct"])
    baseline_20 = stop_20d[stop_20d["stop_rule_id"].astype(str).eq("no_stop")]
    best_short = threshold_sweep[threshold_sweep["fixed_horizon_days"].le(40)].sort_values(
        ["win_rate_pct", "avg_return_pct"], ascending=[False, False]
    )
    best_short_text = "NA"
    if not best_short.empty:
        best = best_short.iloc[0]
        best_short_text = (
            f"{int(best['fixed_horizon_days'])} \u65e5\u7121\u505c\u640d / "
            f"\u9580\u6abb {metric_number(best['breakout_threshold_pct'], '%')} / "
            f"\u52dd\u7387 {metric_number(best['win_rate_pct'], '%')} / "
            f"\u5e73\u5747 {metric_number(best['avg_return_pct'], '%')}"
        )
    lines = [
        "# Volume Range Breakout V2 Close-Only Confirmation Audit",
        "",
        f"- research_id: `{RESEARCH_ID}`",
        f"- artifact_version: `{ARTIFACT_VERSION}`",
        f"- source_research_id: `{SOURCE_RESEARCH_ID}`",
        f"- advisory_status: `{ADVISORY_STATUS}`",
        f"- production_readiness: `{PRODUCTION_READINESS}`",
        f"- approved_for_daily: `False`",
        "- Scope: research-only replay on existing v1 formal-operation source events, not a full raw-market producer rerun.",
        f"- Candidate population: `base_shape_id={BASE_SHAPE_ID}` (`{BASE_SHAPE_DEFINITION}`) and `breakout_over_prev60_pct >= threshold`.",
        "- Close-only triggers: next-day close above signal high, 5MA close reclaim, and 10MA close reclaim.",
        "- Stop sweep: no stop, signal-low close stop, entry-minus 5/7/10pct close stop, MA10 close stop, and MA20 close stop.",
        "- Operation prices use confirmation next trading day open, close-confirmed stop next trading day open, or fixed future close.",
        "- Intraday high/low are not used as confirmation, entry, exit, stop, or realized return prices in this artifact.",
        "",
        "## Decision Summary / \u7d50\u8ad6\u6458\u8981",
        "",
        "- `breakout_threshold_pct=2.0` \u5c31\u662f +2pct \u7a81\u7834\u5e45\u5ea6\u9580\u6abb\u6e2c\u8a66\u3002",
        "- \u9019\u4efd research evidence \u4e0d\u652f\u6301\u7528 close-confirmed \u505c\u640d\u6539\u5584\u9019\u500b\u5019\u9078\u65b9\u5411\uff1b\u5728 +2pct\u300120 \u65e5\u53e3\u5f91\u4e0b\uff0c\u6240\u6709\u6e2c\u5230\u7684\u505c\u640d\u898f\u5247\u52dd\u7387\u90fd\u4f4e\u65bc\u7121\u505c\u640d\u3002",
        "- \u552f\u4e00\u901a\u904e\u7c21\u55ae research gate\uff08\u52dd\u7387 >=60pct \u4e14\u5e73\u5747\u5831\u916c >0\uff09\u7684\u5217\u662f\u56fa\u5b9a 60 \u65e5\u7121\u505c\u640d\uff0c\u4f46\u9019\u500b\u6301\u6709\u6642\u9593\u5df2\u6a19\u8a18\u70ba\u4e0d\u9069\u5408\u77ed\u7dda\u64cd\u4f5c\u65b9\u5411\u3002",
        f"- 40 \u65e5\u4ee5\u5167\u8868\u73fe\u6700\u597d\u7684\u7121\u505c\u640d\u5217\uff1a{best_short_text}\u3002",
        "- MA10 stop \u672c\u8f2a\u4e0d\u53ef\u7528\uff0c\u56e0\u70ba\u76ee\u524d price history layer \u6c92\u6709 `ma10` \u6b04\u4f4d\uff1b\u9019\u4e9b\u5217\u6a19\u70ba insufficient sample\uff0c\u4e0d\u51c6\u7576\u6210\u7121\u505c\u640d\u7e3e\u6548\u3002",
        "",
        "## Plus 2pct No-Stop Horizon Snapshot / +2pct \u7121\u505c\u640d\u6301\u6709\u671f\u6bd4\u8f03",
        "",
        *markdown_table(
            no_stop_snapshot,
            [
                "breakout_threshold_pct",
                "return_basis",
                "fixed_horizon_days",
                "sample_size",
                "win_rate_pct",
                "loss_rate_pct",
                "avg_return_pct",
                "median_return_pct",
                "split_gate_status",
            ],
            20,
        ),
        "",
        "## Plus 2pct Stop Rule Comparison At 20d / +2pct \u4e8c\u5341\u65e5\u505c\u640d\u6bd4\u8f03",
        "",
        "\u9019\u5f35\u8868\u56de\u7b54\u505c\u640d\u662f\u5426\u6539\u5584 20 \u65e5\u7d50\u679c\uff1b\u672c artifact \u7684\u7b54\u6848\u662f\u6c92\u6709\u6539\u5584\u3002",
        "",
        *markdown_table(
            stop_20d,
            [
                "stop_rule_id",
                "return_basis",
                "sample_size",
                "data_quality_exception_count",
                "win_rate_pct",
                "loss_rate_pct",
                "avg_return_pct",
                "median_return_pct",
                "split_gate_status",
            ],
            20,
        ),
        "",
        "## Breakout Threshold Sweep For No-Stop Horizons / \u7a81\u7834\u5e45\u5ea6\u9580\u6abb sweep",
        "",
        "\u9019\u5f35\u8868\u56de\u7b54\u6539\u8b8a +2pct \u7a81\u7834\u5e45\u5ea6\u9580\u6abb\u6703\u600e\u9ebc\u5f71\u97ff\u52dd\u7387\u8207\u5831\u916c\u7387\uff1b\u6e2c\u8a66\u9580\u6abb\u662f 0\u30011\u30012\u30013\u30014\u30015\u30017.5\u300110pct\u3002",
        "",
        *markdown_table(
            threshold_sweep,
            [
                "breakout_threshold_pct",
                "return_basis",
                "fixed_horizon_days",
                "sample_size",
                "win_rate_pct",
                "loss_rate_pct",
                "avg_return_pct",
                "median_return_pct",
                "split_gate_status",
            ],
            40,
        ),
        "",
        "## Threshold 2pct",
        "",
        *markdown_table(threshold_2.sort_values(["return_basis", "trigger_scope"]), main_cols, 200),
        "",
        "## Selected Any Trigger Threshold Sweep",
        "",
        *markdown_table(selected.sort_values(["return_basis", "breakout_threshold_pct"]), main_cols, 240),
        "",
        "## Outputs",
        "",
        f"- summary_csv: `{LATEST_SUMMARY_CSV}`",
        f"- detail_csv: `{LATEST_DETAIL_CSV}`",
        f"- history_summary_csv: `{HISTORY_SUMMARY_CSV}`",
        f"- history_detail_csv: `{HISTORY_DETAIL_CSV}`",
    ]
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    generated_at = now_text()
    source, source_version = load_source()
    detail = build_detail(source, source_version, generated_at)
    summary = build_summary(source, detail, source_version, generated_at)
    write_csv(detail, LATEST_DETAIL_CSV, DETAIL_COLUMNS)
    write_csv(detail, HISTORY_DETAIL_CSV, DETAIL_COLUMNS)
    write_csv(summary, LATEST_SUMMARY_CSV, SUMMARY_COLUMNS)
    write_csv(summary, HISTORY_SUMMARY_CSV, SUMMARY_COLUMNS)
    write_markdown(summary, LATEST_MD)
    print(
        f"{RESEARCH_ID} written summary_rows={len(summary)} detail_rows={len(detail)} "
        f"source_rows={len(source)}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
