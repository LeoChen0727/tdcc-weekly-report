from __future__ import annotations

from datetime import datetime
from pathlib import Path
from typing import Any, Callable
from zoneinfo import ZoneInfo
import math

import pandas as pd

from build_breakout_family_retest_grid import (
    FORBIDDEN_PRODUCTION_FIELDS,
    LATEST_DETAIL_CSV as SOURCE_DETAIL_CSV,
    PARAMETER_SET_ID as SOURCE_PARAMETER_SET_ID,
    PRICE_DIR,
    PRODUCTION_READINESS,
    RESEARCH_ID as SOURCE_RESEARCH_ID,
    RESEARCH_VARIANT_ID,
    normalize_code,
    normalize_date,
    safe_float,
    safe_str,
)
from volume_breakout_operation_utils import (
    ENTRY_RULE_ID as CONFIRMATION_ENTRY_RULE_ID,
    MAX_CONFIRM_DAYS,
    TRIGGERS,
    load_market_regime_map,
    selected_confirmation_for_signal,
    simulate_confirmed_trade,
)


ROOT = Path(".")
TDCC_DIR = ROOT / "data" / "tdcc_stock_history"
RESEARCH_LATEST_DIR = ROOT / "output" / "latest" / "research_backtest"
RESEARCH_HISTORY_DIR = ROOT / "output" / "history" / "research"

LATEST_CSV = RESEARCH_LATEST_DIR / "structured_neckline_breakout_retest_filter_grid_latest.csv"
LATEST_MD = RESEARCH_LATEST_DIR / "structured_neckline_breakout_retest_filter_grid_latest.md"
HISTORY_CSV = RESEARCH_HISTORY_DIR / "structured_neckline_breakout_retest_filter_grid.csv"

RESEARCH_ID = "structured_neckline_breakout_retest_filter_grid"
PARAMETER_SET_ID = "structured_neckline_breakout_retest_filter_grid_20260627"
EVENT_FAMILY_ID = "structured_neckline_volume_breakout_proxy"
ENTRY_DIRECT = "direct_breakout_next_open"

TDCC_FRESH_DAYS = 10

OUTPUT_COLUMNS = [
    "research_id",
    "research_variant_id",
    "parameter_set_id",
    "source_research_id",
    "source_parameter_set_id",
    "advisory_status",
    "event_family_id",
    "segment_id",
    "segment_name",
    "segment_basis",
    "event_count",
    "unique_stock_count",
    "direct_mature_sample_size",
    "direct_win_rate_pct",
    "direct_avg_return_pct",
    "direct_median_return_pct",
    "retest_mature_sample_size",
    "retest_trigger_rate_pct",
    "retest_win_rate_pct",
    "retest_avg_return_pct",
    "retest_median_return_pct",
    "win_rate_lift_pct",
    "avg_return_lift_pct",
    "retest_not_found_count",
    "retest_found_but_no_attack_count",
    "retest_broken_count",
    "tdcc_fresh_sample_size",
    "tdcc_supportive_sample_size",
    "tdcc_supportive_rate_pct",
    "confirmation_signal_sample_size",
    "confirmation_signal_rate_pct",
    "confirmation_signal_mature_sample_size",
    "confirmation_signal_win_rate_pct",
    "confirmation_signal_avg_return_pct",
    "confirmation_signal_median_return_pct",
    "confirmation_signal_vs_direct_win_rate_lift_pct",
    "confirmation_signal_vs_retest_win_rate_lift_pct",
    "revenue_layer_status",
    "interpretation",
    "next_action",
    "approved_for_daily",
    "production_readiness",
    "generated_at",
]


def now_text() -> str:
    return datetime.now(ZoneInfo("Asia/Taipei")).strftime("%Y-%m-%d %H:%M:%S Asia/Taipei")


def metric_text(value: float, digits: int = 4) -> str:
    if value is None or math.isnan(value) or math.isinf(value):
        return ""
    return f"{value:.{digits}f}"


def to_num(series: pd.Series) -> pd.Series:
    return pd.to_numeric(series, errors="coerce")


def trueish(value: Any) -> bool:
    return safe_str(value).lower() in {"true", "1", "1.0", "yes", "y", "t"}


def read_source_events() -> pd.DataFrame:
    if not SOURCE_DETAIL_CSV.exists():
        raise SystemExit(f"ERROR: missing source detail: {SOURCE_DETAIL_CSV}")
    detail = pd.read_csv(SOURCE_DETAIL_CSV, dtype=str, keep_default_na=False)
    if detail.empty:
        raise SystemExit(f"ERROR: source detail is empty: {SOURCE_DETAIL_CSV}")
    forbidden = sorted(set(detail.columns) & FORBIDDEN_PRODUCTION_FIELDS)
    if forbidden:
        raise SystemExit(f"ERROR: source detail contains production decision fields: {forbidden}")
    events = detail[
        detail["event_family_id"].astype(str).eq(EVENT_FAMILY_ID)
        & detail["entry_variant"].astype(str).eq(ENTRY_DIRECT)
    ].copy()
    if events.empty:
        raise SystemExit(f"ERROR: no {EVENT_FAMILY_ID} rows in {SOURCE_DETAIL_CSV}")
    events["stock_id"] = events["stock_id"].map(normalize_code)
    events["signal_date"] = events["signal_date"].map(normalize_date)
    for col in [
        "support_touch_count",
        "base_width_pct",
        "low_position_120_pct",
        "direct_return_pct",
        "retest_return_pct",
        "breakout_distance_pct",
        "volume_ratio",
        "volume_ma20_lots",
    ]:
        events[col] = pd.to_numeric(events.get(col, ""), errors="coerce")
    return events


def read_price_file(stock_id: str) -> pd.DataFrame:
    path = PRICE_DIR / f"{stock_id}.csv"
    if not path.exists():
        return pd.DataFrame()
    try:
        df = pd.read_csv(path, dtype=str, keep_default_na=False)
    except Exception:
        return pd.DataFrame()
    if df.empty:
        return df
    df = df.copy()
    df["date"] = df["date"].map(normalize_date)
    for col in ["open", "high", "low", "close", "return_1d", "volume", "volume_ma20", "volume_ratio", "ma5", "ma10"]:
        df[col] = pd.to_numeric(df.get(col, ""), errors="coerce")
    df = df.sort_values("date").reset_index(drop=True)
    df["prev_close_calc"] = df["close"].shift(1)
    for window, col in [(5, "ma5"), (10, "ma10")]:
        if col not in df.columns or df[col].isna().all():
            df[col] = df["close"].rolling(window, min_periods=window).mean()
        else:
            df[col] = df[col].fillna(df["close"].rolling(window, min_periods=window).mean())
    if "volume_ma20" not in df.columns or df["volume_ma20"].isna().all():
        df["volume_ma20"] = df["volume"].rolling(20, min_periods=20).mean()
    else:
        df["volume_ma20"] = df["volume_ma20"].fillna(df["volume"].rolling(20, min_periods=20).mean())
    df["volume_ratio_calc"] = df["volume"] / df["volume_ma20"].replace(0, pd.NA)
    df["volume_ratio"] = df["volume_ratio"].fillna(df["volume_ratio_calc"])
    df["return_1d_calc"] = (df["close"] / df["prev_close_calc"].replace(0, pd.NA) - 1.0) * 100.0
    df["return_1d"] = df["return_1d"].fillna(df["return_1d_calc"])
    return df


def attach_signal_candle_features(events: pd.DataFrame) -> pd.DataFrame:
    rows: list[dict[str, Any]] = []
    price_cache: dict[str, pd.DataFrame] = {}
    for _, row in events.iterrows():
        stock_id = safe_str(row.get("stock_id"))
        signal_date = normalize_date(row.get("signal_date"))
        if stock_id not in price_cache:
            price_cache[stock_id] = read_price_file(stock_id)
        price = price_cache[stock_id]
        found = price[price["date"].astype(str).eq(signal_date)] if not price.empty else pd.DataFrame()
        if found.empty:
            rows.append(
                {
                    "signal_open": math.nan,
                    "signal_high": math.nan,
                    "signal_low_price": math.nan,
                    "signal_close_price": math.nan,
                    "prev_close_price": math.nan,
                    "signal_return_1d_pct": math.nan,
                    "signal_body_pct": math.nan,
                    "signal_upper_shadow_range_pct": math.nan,
                    "clean_attack_candle": False,
                    "weak_or_upper_shadow_candle": False,
                    "locked_limit_down_risk": False,
                }
            )
            continue
        candle = found.iloc[0]
        open_price = safe_float(candle.get("open"))
        high = safe_float(candle.get("high"))
        low = safe_float(candle.get("low"))
        close = safe_float(candle.get("close"))
        prev_close = safe_float(candle.get("prev_close_calc"))
        signal_return = safe_float(candle.get("return_1d"))
        price_range = high - low if not any(math.isnan(v) for v in [high, low]) else math.nan
        body_pct = abs(close - open_price) / open_price * 100.0 if open_price and not math.isnan(open_price) else math.nan
        upper_shadow_pct = (
            (high - max(open_price, close)) / price_range * 100.0
            if not math.isnan(price_range) and price_range > 0 and not any(math.isnan(v) for v in [open_price, close, high])
            else 0.0
        )
        locked_limit = trueish(row.get("locked_limit_up_breakout"))
        clean_attack = locked_limit or (
            not any(math.isnan(v) for v in [open_price, close, body_pct, upper_shadow_pct])
            and close > open_price
            and body_pct >= 1.0
            and upper_shadow_pct <= 35.0
        )
        weak_or_upper = not clean_attack
        locked_down = False
        if not any(math.isnan(v) for v in [open_price, high, low, close, prev_close, signal_return]):
            one_price_locked = high == low
            range_pct = (high - low) / prev_close * 100.0 if prev_close > 0 else math.nan
            locked_or_tight_range = one_price_locked or (not math.isnan(range_pct) and range_pct <= 1.0)
            locked_down = (
                signal_return <= -9.0
                and close <= low * 1.005
                and open_price <= close * 1.005
                and locked_or_tight_range
            )
        rows.append(
            {
            "signal_open": open_price,
            "signal_high": high,
            "signal_low_price": low,
            "signal_close_price": close,
            "prev_close_price": prev_close,
            "signal_return_1d_pct": signal_return,
            "signal_body_pct": body_pct,
            "signal_upper_shadow_range_pct": upper_shadow_pct,
            "clean_attack_candle": clean_attack,
            "weak_or_upper_shadow_candle": weak_or_upper,
                "locked_limit_down_risk": locked_down,
            }
        )
    features = pd.DataFrame(rows)
    return pd.concat([events.reset_index(drop=True), features], axis=1)


def attach_confirmation_signal_features(events: pd.DataFrame) -> pd.DataFrame:
    rows: list[dict[str, Any]] = []
    price_cache: dict[str, pd.DataFrame] = {}
    for _, row in events.iterrows():
        stock_id = safe_str(row.get("stock_id"))
        signal_date = normalize_date(row.get("signal_date"))
        if stock_id not in price_cache:
            price_cache[stock_id] = read_price_file(stock_id)
        price = price_cache[stock_id]
        found = price.index[price["date"].astype(str).eq(signal_date)].tolist() if not price.empty else []
        base = {
            "confirmation_signal_matched": False,
            "confirmation_signal_trigger_id": "",
            "confirmation_signal_matched_trigger_ids": "",
            "confirmation_signal_date": "",
            "confirmation_signal_age_trading_days": "",
            "confirmation_signal_entry_rule_id": CONFIRMATION_ENTRY_RULE_ID,
            "confirmation_signal_entry_date": "",
            "confirmation_signal_exit_date": "",
            "confirmation_signal_exit_reason": "",
            "confirmation_signal_holding_days": "",
            "confirmation_signal_return_pct": math.nan,
            "confirmation_signal_mfe_pct": math.nan,
            "confirmation_signal_mae_pct": math.nan,
        }
        if not found:
            rows.append(base)
            continue
        signal_idx = int(found[0])
        selected = selected_confirmation_for_signal(price, signal_idx)
        if selected is None:
            rows.append(base)
            continue
        confirmation_idx = int(selected["confirmation_idx"])
        trade = simulate_confirmed_trade(price, signal_idx, confirmation_idx)
        out = {
            **base,
            "confirmation_signal_matched": True,
            "confirmation_signal_trigger_id": safe_str(selected.get("trigger_id")),
            "confirmation_signal_matched_trigger_ids": safe_str(selected.get("matched_trigger_ids")),
            "confirmation_signal_date": safe_str(selected.get("confirmation_date")),
            "confirmation_signal_age_trading_days": str(confirmation_idx - signal_idx),
        }
        if trade is not None:
            out.update(
                {
                    "confirmation_signal_entry_date": safe_str(trade.get("entry_date")),
                    "confirmation_signal_exit_date": safe_str(trade.get("exit_date")),
                    "confirmation_signal_exit_reason": safe_str(trade.get("exit_reason")),
                    "confirmation_signal_holding_days": safe_str(trade.get("holding_days")),
                    "confirmation_signal_return_pct": safe_float(trade.get("return_pct")),
                    "confirmation_signal_mfe_pct": safe_float(trade.get("mfe_pct")),
                    "confirmation_signal_mae_pct": safe_float(trade.get("mae_pct")),
                }
            )
        rows.append(out)
    features = pd.DataFrame(rows)
    return pd.concat([events.reset_index(drop=True), features], axis=1)


def attach_market_regime_features(events: pd.DataFrame) -> pd.DataFrame:
    market_regimes = load_market_regime_map()
    out = events.copy()
    out["signal_market_regime"] = out["signal_date"].map(lambda date: market_regimes.get(normalize_date(date), "unknown"))
    return out


def read_tdcc_file(stock_id: str) -> pd.DataFrame:
    path = TDCC_DIR / f"{stock_id}.csv"
    if not path.exists():
        return pd.DataFrame()
    try:
        tdcc = pd.read_csv(path, dtype=str, keep_default_na=False)
    except Exception:
        return pd.DataFrame()
    if tdcc.empty or "as_of_date" not in tdcc.columns:
        return pd.DataFrame()
    tdcc = tdcc.copy()
    tdcc["tdcc_as_of_date"] = tdcc["as_of_date"].map(normalize_date)
    tdcc["tdcc_date_dt"] = pd.to_datetime(tdcc["tdcc_as_of_date"], format="%Y%m%d", errors="coerce")
    for col in [
        "tdcc_consecutive_up_weeks",
        "over_400_change_1w",
        "over_800_change_1w",
        "over_1000_change_1w",
    ]:
        tdcc[col] = pd.to_numeric(tdcc.get(col, ""), errors="coerce")
    return tdcc.dropna(subset=["tdcc_date_dt"]).sort_values("tdcc_date_dt")


def tdcc_supportive(row: pd.Series) -> bool:
    return (
        safe_float(row.get("tdcc_consecutive_up_weeks")) >= 1
        or trueish(row.get("all_thresholds_up"))
        or trueish(row.get("high_thresholds_up"))
        or trueish(row.get("four_thresholds_sync_up"))
        or safe_float(row.get("over_400_change_1w")) > 0
        or safe_float(row.get("over_800_change_1w")) > 0
        or safe_float(row.get("over_1000_change_1w")) > 0
    )


def attach_tdcc_features(events: pd.DataFrame) -> pd.DataFrame:
    rows: list[dict[str, Any]] = []
    tdcc_cache: dict[str, pd.DataFrame] = {}
    for _, row in events.iterrows():
        stock_id = safe_str(row.get("stock_id"))
        signal_dt = pd.to_datetime(normalize_date(row.get("signal_date")), format="%Y%m%d", errors="coerce")
        if stock_id not in tdcc_cache:
            tdcc_cache[stock_id] = read_tdcc_file(stock_id)
        tdcc = tdcc_cache[stock_id]
        if tdcc.empty or pd.isna(signal_dt):
            rows.append({"tdcc_fresh": False, "tdcc_supportive": False, "tdcc_age_days": ""})
            continue
        eligible = tdcc[tdcc["tdcc_date_dt"].le(signal_dt)].tail(1)
        if eligible.empty:
            rows.append({"tdcc_fresh": False, "tdcc_supportive": False, "tdcc_age_days": ""})
            continue
        latest = eligible.iloc[0]
        age_days = int((signal_dt - latest["tdcc_date_dt"]).days)
        fresh = 0 <= age_days <= TDCC_FRESH_DAYS
        rows.append(
            {
                "tdcc_fresh": fresh,
                "tdcc_supportive": fresh and tdcc_supportive(latest),
                "tdcc_age_days": str(age_days) if fresh else "",
            }
        )
    features = pd.DataFrame(rows)
    return pd.concat([events.reset_index(drop=True), features], axis=1)


def enrich_events(events: pd.DataFrame) -> pd.DataFrame:
    events = attach_signal_candle_features(events)
    events = attach_confirmation_signal_features(events)
    events = attach_market_regime_features(events)
    events = attach_tdcc_features(events)
    return events


def return_stats(series: pd.Series) -> dict[str, float | int]:
    returns = to_num(series).dropna()
    mature = int(len(returns))
    if mature == 0:
        return {
            "mature": 0,
            "win_rate_pct": math.nan,
            "avg_return_pct": math.nan,
            "median_return_pct": math.nan,
        }
    wins = int((returns > 0).sum())
    return {
        "mature": mature,
        "win_rate_pct": wins / mature * 100.0,
        "avg_return_pct": float(returns.mean()),
        "median_return_pct": float(returns.median()),
    }


def row_for_segment(
    events: pd.DataFrame,
    segment_id: str,
    segment_name: str,
    segment_basis: str,
    mask_fn: Callable[[pd.DataFrame], pd.Series],
    generated_at: str,
) -> dict[str, str]:
    segment = events[mask_fn(events)].copy()
    direct = return_stats(segment["direct_return_pct"])
    retest = return_stats(segment["retest_return_pct"])
    event_count = int(len(segment))
    retest_trigger_rate = retest["mature"] / event_count * 100.0 if event_count else math.nan
    statuses = segment["retest_status"].astype(str)
    broken = int(
        statuses.isin(
            {
                "neckline_effectively_broken_before_retest",
                "neckline_effectively_broken_after_retest",
            }
        ).sum()
    )
    tdcc_fresh_count = int(segment["tdcc_fresh"].astype(bool).sum()) if "tdcc_fresh" in segment.columns else 0
    tdcc_supportive_count = int(segment["tdcc_supportive"].astype(bool).sum()) if "tdcc_supportive" in segment.columns else 0
    confirmation_matched = segment["confirmation_signal_matched"].astype(bool) if "confirmation_signal_matched" in segment.columns else pd.Series(False, index=segment.index)
    confirmation_count = int(confirmation_matched.sum())
    confirmation = return_stats(segment.loc[confirmation_matched, "confirmation_signal_return_pct"] if confirmation_count else pd.Series(dtype="float64"))
    win_lift = float(retest["win_rate_pct"]) - float(direct["win_rate_pct"])
    avg_lift = float(retest["avg_return_pct"]) - float(direct["avg_return_pct"])
    confirmation_direct_lift = float(confirmation["win_rate_pct"]) - float(direct["win_rate_pct"])
    confirmation_retest_lift = float(confirmation["win_rate_pct"]) - float(retest["win_rate_pct"])
    interpretation, action = interpretation_for(segment_id, event_count, retest, direct, win_lift, avg_lift)
    return {
        "research_id": RESEARCH_ID,
        "research_variant_id": RESEARCH_VARIANT_ID,
        "parameter_set_id": PARAMETER_SET_ID,
        "source_research_id": SOURCE_RESEARCH_ID,
        "source_parameter_set_id": SOURCE_PARAMETER_SET_ID,
        "advisory_status": RESEARCH_VARIANT_ID,
        "event_family_id": EVENT_FAMILY_ID,
        "segment_id": segment_id,
        "segment_name": segment_name,
        "segment_basis": segment_basis,
        "event_count": str(event_count),
        "unique_stock_count": str(int(segment["stock_id"].nunique())) if event_count else "0",
        "direct_mature_sample_size": str(int(direct["mature"])),
        "direct_win_rate_pct": metric_text(float(direct["win_rate_pct"])),
        "direct_avg_return_pct": metric_text(float(direct["avg_return_pct"])),
        "direct_median_return_pct": metric_text(float(direct["median_return_pct"])),
        "retest_mature_sample_size": str(int(retest["mature"])),
        "retest_trigger_rate_pct": metric_text(retest_trigger_rate),
        "retest_win_rate_pct": metric_text(float(retest["win_rate_pct"])),
        "retest_avg_return_pct": metric_text(float(retest["avg_return_pct"])),
        "retest_median_return_pct": metric_text(float(retest["median_return_pct"])),
        "win_rate_lift_pct": metric_text(win_lift),
        "avg_return_lift_pct": metric_text(avg_lift),
        "retest_not_found_count": str(int(statuses.eq("retest_not_found").sum())),
        "retest_found_but_no_attack_count": str(int(statuses.eq("retest_found_but_no_attack").sum())),
        "retest_broken_count": str(broken),
        "tdcc_fresh_sample_size": str(tdcc_fresh_count),
        "tdcc_supportive_sample_size": str(tdcc_supportive_count),
        "tdcc_supportive_rate_pct": metric_text(tdcc_supportive_count / tdcc_fresh_count * 100.0 if tdcc_fresh_count else math.nan),
        "confirmation_signal_sample_size": str(confirmation_count),
        "confirmation_signal_rate_pct": metric_text(confirmation_count / event_count * 100.0 if event_count else math.nan),
        "confirmation_signal_mature_sample_size": str(int(confirmation["mature"])),
        "confirmation_signal_win_rate_pct": metric_text(float(confirmation["win_rate_pct"])),
        "confirmation_signal_avg_return_pct": metric_text(float(confirmation["avg_return_pct"])),
        "confirmation_signal_median_return_pct": metric_text(float(confirmation["median_return_pct"])),
        "confirmation_signal_vs_direct_win_rate_lift_pct": metric_text(confirmation_direct_lift),
        "confirmation_signal_vs_retest_win_rate_lift_pct": metric_text(confirmation_retest_lift),
        "revenue_layer_status": "pending_missing_historical_revenue_panel",
        "interpretation": interpretation,
        "next_action": action,
        "approved_for_daily": "false",
        "production_readiness": PRODUCTION_READINESS,
        "generated_at": generated_at,
    }


def interpretation_for(
    segment_id: str,
    event_count: int,
    retest: dict[str, float | int],
    direct: dict[str, float | int],
    win_lift: float,
    avg_lift: float,
) -> tuple[str, str]:
    if event_count < 30 or int(retest["mature"]) < 20:
        return "sample_too_thin_for_model_decision", "expand_or_drop_segment_before_promotion_discussion"
    if segment_id == "all_structured_neckline":
        return "broad_neckline_retest_improves_win_rate_but_not_ready", "continue_retest_confirmation_grid_not_production"
    if segment_id == "double_bottom_or_structured_bottom_proxy":
        return "double_bottom_proxy_is_currently_weak_or_thin", "do_not_split_double_bottom_model_yet"
    if segment_id.startswith("confirmation_signal"):
        return "existing_volume_breakout_operation_confirmation_reference", "compare_confirmation_entry_against_retest_entry_not_production"
    if segment_id.startswith("confirmation_trigger_"):
        return "trigger_specific_confirmation_reference_only", "keep_trigger_as_research_diagnostic"
    if segment_id.startswith("market_regime_") or "_market_" in segment_id:
        return "market_regime_research_filter_only", "compare_market_regime_stability_not_production_gate"
    if "tdcc" in segment_id:
        return "tdcc_layer_is_observation_only_due_coverage", "keep_tdcc_as_scoring_research_not_required_gate"
    if win_lift >= 8.0 and avg_lift >= 0.5:
        return "candidate_filter_for_second_pass_review", "review_chart_quality_and_expand_replay"
    if win_lift >= 5.0:
        return "mixed_filter_improvement", "keep_as_advisory_filter_until_broader_replay"
    return "not_a_useful_filter_yet", "do_not_promote_filter"


def build_grid(events: pd.DataFrame, generated_at: str) -> pd.DataFrame:
    strong_bull = lambda d: d["signal_market_regime"].astype(str).eq("strong_bull")
    bull = lambda d: d["signal_market_regime"].astype(str).isin(["strong_bull", "mild_bull"])
    not_correction = lambda d: d["signal_market_regime"].astype(str).isin(["strong_bull", "mild_bull", "range_or_mixed"])
    low_position = lambda d: d["low_position_120_pct"].le(60)
    confirmation_signal = lambda d: d["confirmation_signal_matched"].astype(bool)
    segments: list[tuple[str, str, str, Callable[[pd.DataFrame], pd.Series]]] = [
        ("all_structured_neckline", "all broad structured-neckline proxy rows", "all structured-neckline events", lambda d: pd.Series(True, index=d.index)),
        ("triple_or_multi_bottom_proxy", "triple or multi-bottom proxy", "pattern_subtype", lambda d: d["pattern_subtype"].astype(str).eq("triple_or_multi_bottom_proxy")),
        ("double_bottom_or_structured_bottom_proxy", "double-bottom or structured-bottom proxy", "pattern_subtype", lambda d: d["pattern_subtype"].astype(str).eq("double_bottom_or_structured_bottom_proxy")),
        ("low_position_le60", "low position <= 60", "low_position_120_pct", lambda d: d["low_position_120_pct"].le(60)),
        ("mid_position_60_100", "mid position 60 to 100", "low_position_120_pct", lambda d: d["low_position_120_pct"].gt(60) & d["low_position_120_pct"].le(100)),
        ("high_position_gt100", "high position > 100", "low_position_120_pct", lambda d: d["low_position_120_pct"].gt(100)),
        ("base_width_le15", "base width <= 15%", "base_width_pct", lambda d: d["base_width_pct"].le(15)),
        ("base_width_15_30", "base width 15% to 30%", "base_width_pct", lambda d: d["base_width_pct"].gt(15) & d["base_width_pct"].le(30)),
        ("base_width_gt30", "base width > 30%", "base_width_pct", lambda d: d["base_width_pct"].gt(30)),
        ("support_touches_ge3", "support touches >= 3", "support_touch_count", lambda d: d["support_touch_count"].ge(3)),
        ("clean_attack_candle", "clean attack candle", "body and upper-shadow quality", lambda d: d["clean_attack_candle"].astype(bool)),
        ("weak_or_upper_shadow_candle", "weak body or upper-shadow review", "body and upper-shadow quality", lambda d: d["weak_or_upper_shadow_candle"].astype(bool)),
        ("normal_volume_breakout", "normal volume-confirmed breakout", "volume confirmation type", lambda d: d["normal_volume_breakout"].astype(str).str.lower().eq("true")),
        ("locked_limit_up_breakout", "locked limit-up breakout", "volume confirmation type", lambda d: d["locked_limit_up_breakout"].astype(str).str.lower().eq("true")),
        ("locked_limit_down_risk", "locked limit-down risk", "limit-down special case", lambda d: d["locked_limit_down_risk"].astype(bool)),
        ("market_regime_strong_bull", "signal date market regime is strong_bull", "signal_market_regime", strong_bull),
        ("market_regime_bull", "signal date market regime is strong_bull or mild_bull", "signal_market_regime", bull),
        ("market_regime_not_correction", "signal date market regime is known non-correction", "signal_market_regime", not_correction),
        ("market_regime_range_or_mixed", "signal date market regime is range_or_mixed", "signal_market_regime", lambda d: d["signal_market_regime"].astype(str).eq("range_or_mixed")),
        ("market_regime_correction", "signal date market regime is correction", "signal_market_regime", lambda d: d["signal_market_regime"].astype(str).eq("correction")),
        ("market_regime_unknown", "signal date market regime is unknown", "signal_market_regime", lambda d: d["signal_market_regime"].astype(str).eq("unknown")),
        ("low_position_le60_market_bull", "low position <= 60 and bull market regime", "low_position_120_pct + signal_market_regime", lambda d: low_position(d) & bull(d)),
        ("confirmation_signal_reference", "existing confirmed-operation signal matched", "volume_breakout_confirmed_operation confirmation rules", confirmation_signal),
        ("confirmation_signal_low_position_le60", "confirmed-operation signal plus low position <= 60", "volume_breakout_confirmed_operation confirmation rules + low_position_120_pct", lambda d: confirmation_signal(d) & low_position(d)),
        ("confirmation_signal_market_bull", "confirmed-operation signal plus bull market regime", "volume_breakout_confirmed_operation confirmation rules + signal_market_regime", lambda d: confirmation_signal(d) & bull(d)),
        ("confirmation_signal_low_position_le60_market_bull", "confirmed-operation signal plus low position <= 60 and bull market regime", "volume_breakout_confirmed_operation confirmation rules + low_position_120_pct + signal_market_regime", lambda d: confirmation_signal(d) & low_position(d) & bull(d)),
        ("tdcc_fresh_supportive", "fresh supportive TDCC observation", "TDCC <= 10 calendar days", lambda d: d["tdcc_supportive"].astype(bool)),
        ("tdcc_fresh_supportive_market_bull", "fresh supportive TDCC observation plus bull market regime", "TDCC <= 10 calendar days + signal_market_regime", lambda d: d["tdcc_supportive"].astype(bool) & bull(d)),
        ("tdcc_no_fresh_support", "no fresh supportive TDCC observation", "TDCC <= 10 calendar days", lambda d: ~d["tdcc_supportive"].astype(bool)),
    ]
    for trigger in TRIGGERS:
        segments.append(
            (
                f"confirmation_trigger_{trigger.trigger_id}",
                f"confirmation trigger: {trigger.trigger_id}",
                "volume_breakout_confirmed_operation selected trigger",
                lambda d, trigger_id=trigger.trigger_id: d["confirmation_signal_trigger_id"].astype(str).eq(trigger_id),
            )
        )
    rows = [
        row_for_segment(events, segment_id, segment_name, segment_basis, mask_fn, generated_at)
        for segment_id, segment_name, segment_basis, mask_fn in segments
    ]
    grid = pd.DataFrame(rows)
    for column in OUTPUT_COLUMNS:
        if column not in grid.columns:
            grid[column] = ""
    forbidden = sorted(set(grid.columns) & FORBIDDEN_PRODUCTION_FIELDS)
    if forbidden:
        raise SystemExit(f"ERROR: forbidden production fields in grid: {forbidden}")
    return grid[OUTPUT_COLUMNS]


def write_csv(df: pd.DataFrame, path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(path, index=False, encoding="utf-8-sig")


def markdown_table(df: pd.DataFrame, columns: list[str], limit: int = 80) -> list[str]:
    if df.empty:
        return ["_No rows._"]
    lines = ["| " + " | ".join(columns) + " |", "| " + " | ".join(["---"] * len(columns)) + " |"]
    for _, row in df.head(limit).iterrows():
        lines.append("| " + " | ".join(safe_str(row.get(column)) for column in columns) + " |")
    return lines


def write_markdown(grid: pd.DataFrame, generated_at: str) -> None:
    priority = grid[
        grid["interpretation"].astype(str).isin(
            {
                "candidate_filter_for_second_pass_review",
                "broad_neckline_retest_improves_win_rate_but_not_ready",
            }
        )
    ].copy()
    lines = [
        "# Structured Neckline Breakout Retest Filter Grid",
        "",
        f"- generated_at: `{generated_at}`",
        f"- research_id: `{RESEARCH_ID}`",
        f"- source_research_id: `{SOURCE_RESEARCH_ID}`",
        f"- source_parameter_set_id: `{SOURCE_PARAMETER_SET_ID}`",
        "- production impact: `none`; this is not a production recommendation and does not modify production model conditions, scoring, ranking, PDF logic, or baseline.",
        "",
        "## Scope",
        "",
        "This is the second-pass research grid for the broad structured-neckline breakout model. It keeps W-bottom / triple-bottom / other labels advisory and does not split them into separate production models yet.",
        "",
        f"The confirmation-signal reference intentionally uses the existing `volume_breakout_confirmed_operation` rules, entry_rule_id `{CONFIRMATION_ENTRY_RULE_ID}`, and max confirmation window `{MAX_CONFIRM_DAYS}` trading days. This is not the initial `cond_volume_breakout` stock-screening gate, and it is not a replay of the initial volume/candle entry filter. The reference asks a different question: after a structured neckline breakout signal exists, does the existing confirmed-operation logic later produce a usable operation entry?",
        "",
        "Confirmation trigger ids referenced here: `pullback_5ma_confirmed`, `next_day_break_signal_high_confirmed`, `next_day_continuation_confirmed`, and `pullback_10ma_confirmed`. Confirmed-operation performance uses the existing rule: buy at the next open after confirmation, stop at the signal-day low, otherwise exit at the fixed 10-trading-day close.",
        "",
        "The main entry hypotheses are now compared separately: direct next-open after neckline breakout, retest-not-broken then renewed attack, and existing confirmed-operation signal after the neckline event. Limit special cases remain diagnostic tags: locked limit-up may be part of the source attack-volume confirmation, while locked limit-down is risk and must not count as confirmation. TDCC is included only as an observation layer because historical coverage is short. Revenue remains pending because a point-in-time historical revenue panel is not available in this worktree.",
        "",
        "Market regime is included as a research-only segmentation layer, using the same `strong_bull`, `mild_bull`, `range_or_mixed`, `correction`, and `unknown` categories used by W-bottom early-entry research. These rows test whether broad-market context improves structured-neckline behavior; they are not production gates.",
        "",
        "## Filter Grid",
        "",
        *markdown_table(
            grid,
            [
                "segment_id",
                "event_count",
                "direct_win_rate_pct",
                "retest_mature_sample_size",
                "retest_win_rate_pct",
                "win_rate_lift_pct",
                "retest_avg_return_pct",
                "tdcc_fresh_sample_size",
                "tdcc_supportive_sample_size",
                "confirmation_signal_sample_size",
                "confirmation_signal_rate_pct",
                "confirmation_signal_win_rate_pct",
                "confirmation_signal_avg_return_pct",
                "interpretation",
                "next_action",
            ],
        ),
        "",
        "## Priority Rows",
        "",
        *markdown_table(
            priority,
            [
                "segment_id",
                "event_count",
                "retest_mature_sample_size",
                "retest_win_rate_pct",
                "retest_avg_return_pct",
                "confirmation_signal_mature_sample_size",
                "confirmation_signal_win_rate_pct",
                "confirmation_signal_avg_return_pct",
                "win_rate_lift_pct",
                "next_action",
            ],
        ),
        "",
        "## Interpretation",
        "",
        "Current evidence supports continuing broad neckline retest-confirmation research. It does not yet support production promotion or splitting the neckline model into W-bottom / triple-bottom / other subtype models.",
    ]
    LATEST_MD.parent.mkdir(parents=True, exist_ok=True)
    LATEST_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    generated_at = now_text()
    events = read_source_events()
    events = enrich_events(events)
    grid = build_grid(events, generated_at)
    write_csv(grid, LATEST_CSV)
    write_csv(grid, HISTORY_CSV)
    write_markdown(grid, generated_at)
    print(f"wrote {LATEST_CSV} rows={len(grid)}")
    print(f"wrote {LATEST_MD}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
