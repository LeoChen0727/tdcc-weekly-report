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
    metric_text,
    normalize_code,
    normalize_date,
    safe_float,
    safe_str,
)
from volume_breakout_operation_utils import load_market_regime_map


ROOT = Path(".")
TDCC_DIR = ROOT / "data" / "tdcc_stock_history"
RESEARCH_LATEST_DIR = ROOT / "output" / "latest" / "research_backtest"
RESEARCH_HISTORY_DIR = ROOT / "output" / "history" / "research"

LATEST_DETAIL_CSV = RESEARCH_LATEST_DIR / "structured_neckline_retest_entry_exit_grid_detail_latest.csv"
LATEST_SUMMARY_CSV = RESEARCH_LATEST_DIR / "structured_neckline_retest_entry_exit_grid_latest.csv"
LATEST_MD = RESEARCH_LATEST_DIR / "structured_neckline_retest_entry_exit_grid_latest.md"
HISTORY_DETAIL_CSV = RESEARCH_HISTORY_DIR / "structured_neckline_retest_entry_exit_grid_detail.csv"
HISTORY_SUMMARY_CSV = RESEARCH_HISTORY_DIR / "structured_neckline_retest_entry_exit_grid.csv"

RESEARCH_ID = "structured_neckline_retest_entry_exit_grid"
PARAMETER_SET_ID = "structured_neckline_retest_entry_exit_grid_20260627"
EVENT_FAMILY_ID = "structured_neckline_volume_breakout_proxy"
ENTRY_DIRECT = "direct_breakout_next_open"
RETEST_STATUS = "retest_not_broken_then_attack"
TDCC_FRESH_DAYS = 10

STOP_RULE_IDS = [
    "signal_low_stop",
    "retest_low_stop",
    "neckline_minus_2pct_stop",
    "source_retest_or_neckline_2pct_stop",
]

EXIT_RULE_IDS = [
    "fixed_10d_close",
    "fixed_20d_close",
    "tp10_intraday_or_fixed_20d_close",
    "tp10_close_or_neutral_after_5pct_close_20d",
]

OUTCOME_RULE_BY_EXIT = {
    "fixed_10d_close": "positive_return_after_fixed_10d",
    "fixed_20d_close": "positive_return_after_fixed_20d",
    "tp10_intraday_or_fixed_20d_close": "tp10_intraday_required_else_loss",
    "tp10_close_or_neutral_after_5pct_close_20d": "tp10_close_win_5pct_pullback_neutral",
}

DETAIL_COLUMNS = [
    "research_id",
    "research_variant_id",
    "parameter_set_id",
    "source_research_id",
    "source_parameter_set_id",
    "advisory_status",
    "event_family_id",
    "pattern_subtype",
    "segment_id",
    "stock_id",
    "stock_name",
    "signal_date",
    "retest_date",
    "retest_attack_date",
    "retest_entry_date",
    "reference_price",
    "stop_rule_id",
    "stop_level",
    "exit_rule_id",
    "outcome_rule_id",
    "entry_price",
    "exit_date",
    "exit_price",
    "exit_reason",
    "holding_days",
    "return_pct",
    "mfe_pct",
    "mae_pct",
    "outcome_result",
    "positive_return_result",
    "market_regime",
    "low_position_120_pct",
    "base_width_pct",
    "support_touch_count",
    "tdcc_fresh",
    "tdcc_supportive",
    "tdcc_age_days",
    "approved_for_daily",
    "production_readiness",
    "generated_at",
]

SUMMARY_COLUMNS = [
    "research_id",
    "research_variant_id",
    "parameter_set_id",
    "source_research_id",
    "source_parameter_set_id",
    "advisory_status",
    "event_family_id",
    "segment_id",
    "segment_name",
    "stop_rule_id",
    "exit_rule_id",
    "outcome_rule_id",
    "sample_size",
    "evaluated_sample_size",
    "mature_sample_size",
    "win_count",
    "neutral_count",
    "loss_count",
    "incomplete_count",
    "pure_win_rate_pct",
    "neutral_inclusive_success_rate_pct",
    "positive_return_count",
    "positive_return_rate_pct",
    "stop_hit_count",
    "tp10_hit_count",
    "avg_return_pct",
    "median_return_pct",
    "avg_mfe_pct",
    "median_mfe_pct",
    "avg_mae_pct",
    "median_mae_pct",
    "approved_for_daily",
    "production_readiness",
    "generated_at",
]

SEGMENTS: list[tuple[str, str, Callable[[pd.DataFrame], pd.Series]]] = [
    ("all_retest_entries", "all retest-not-broken then renewed-attack entries", lambda d: pd.Series(True, index=d.index)),
    ("low_position_le60", "low position <= 60", lambda d: d["low_position_120_pct"].le(60)),
    ("market_regime_strong_bull", "signal date market regime is strong_bull", lambda d: d["market_regime"].eq("strong_bull")),
    (
        "market_regime_bull",
        "signal date market regime is strong_bull or mild_bull",
        lambda d: d["market_regime"].isin(["strong_bull", "mild_bull"]),
    ),
    (
        "market_regime_correction",
        "signal date market regime is correction",
        lambda d: d["market_regime"].eq("correction"),
    ),
    (
        "market_regime_range_or_mixed",
        "signal date market regime is range_or_mixed",
        lambda d: d["market_regime"].eq("range_or_mixed"),
    ),
    (
        "low_position_le60_market_bull",
        "low position <= 60 and bull market regime",
        lambda d: d["low_position_120_pct"].le(60) & d["market_regime"].isin(["strong_bull", "mild_bull"]),
    ),
    ("tdcc_fresh_supportive", "fresh supportive TDCC observation at retest entry", lambda d: d["tdcc_supportive"].astype(bool)),
    (
        "tdcc_fresh_supportive_market_bull",
        "fresh supportive TDCC observation plus bull market regime",
        lambda d: d["tdcc_supportive"].astype(bool) & d["market_regime"].isin(["strong_bull", "mild_bull"]),
    ),
]


def now_text() -> str:
    return datetime.now(ZoneInfo("Asia/Taipei")).strftime("%Y-%m-%d %H:%M:%S Asia/Taipei")


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
        & detail["retest_status"].astype(str).eq(RETEST_STATUS)
        & detail["retest_entry_date"].astype(str).ne("")
    ].copy()
    if events.empty:
        raise SystemExit(f"ERROR: no {RETEST_STATUS} rows in {SOURCE_DETAIL_CSV}")
    events["stock_id"] = events["stock_id"].map(normalize_code)
    for col in ["signal_date", "retest_date", "retest_attack_date", "retest_entry_date"]:
        events[col] = events[col].map(normalize_date)
    for col in ["reference_price", "signal_low", "low_position_120_pct", "base_width_pct", "support_touch_count"]:
        events[col] = pd.to_numeric(events.get(col, ""), errors="coerce")
    market_regimes = load_market_regime_map()
    events["market_regime"] = events["signal_date"].map(lambda value: market_regimes.get(normalize_date(value), "unknown"))
    return attach_tdcc_features(events)


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
    df = df[df["date"] != ""].sort_values("date").reset_index(drop=True)
    for col in ["open", "high", "low", "close"]:
        df[col] = pd.to_numeric(df.get(col, ""), errors="coerce")
    return df


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
        entry_dt = pd.to_datetime(normalize_date(row.get("retest_entry_date")), format="%Y%m%d", errors="coerce")
        if stock_id not in tdcc_cache:
            tdcc_cache[stock_id] = read_tdcc_file(stock_id)
        tdcc = tdcc_cache[stock_id]
        if tdcc.empty or pd.isna(entry_dt):
            rows.append({"tdcc_fresh": False, "tdcc_supportive": False, "tdcc_age_days": ""})
            continue
        eligible = tdcc[tdcc["tdcc_date_dt"].le(entry_dt)].tail(1)
        if eligible.empty:
            rows.append({"tdcc_fresh": False, "tdcc_supportive": False, "tdcc_age_days": ""})
            continue
        latest = eligible.iloc[0]
        age_days = int((entry_dt - latest["tdcc_date_dt"]).days)
        fresh = 0 <= age_days <= TDCC_FRESH_DAYS
        rows.append(
            {
                "tdcc_fresh": fresh,
                "tdcc_supportive": fresh and tdcc_supportive(latest),
                "tdcc_age_days": str(age_days) if fresh else "",
            }
        )
    return pd.concat([events.reset_index(drop=True), pd.DataFrame(rows)], axis=1)


def index_for_date(price: pd.DataFrame, date_text: Any) -> int | None:
    date = normalize_date(date_text)
    if not date:
        return None
    matches = price.index[price["date"].astype(str).eq(date)].tolist()
    return int(matches[0]) if matches else None


def stop_level_for(rule_id: str, row: pd.Series, price: pd.DataFrame) -> float:
    reference = safe_float(row.get("reference_price"))
    signal_low = safe_float(row.get("signal_low"))
    retest_idx = index_for_date(price, row.get("retest_date"))
    retest_low = safe_float(price.iloc[retest_idx].get("low")) if retest_idx is not None else math.nan
    if rule_id == "signal_low_stop":
        return signal_low
    if rule_id == "retest_low_stop":
        return retest_low
    if rule_id == "neckline_minus_2pct_stop":
        return reference * 0.98 if not math.isnan(reference) else math.nan
    if rule_id == "source_retest_or_neckline_2pct_stop":
        levels = [value for value in [retest_low, reference * 0.98 if not math.isnan(reference) else math.nan] if not math.isnan(value)]
        return min(levels) if levels else math.nan
    raise ValueError(f"unknown stop rule: {rule_id}")


def stop_price_for_day(day: pd.Series, stop_level: float) -> float:
    open_price = safe_float(day.get("open"))
    if not math.isnan(open_price) and open_price < stop_level:
        return open_price
    return stop_level


def mfe_mae(price: pd.DataFrame, entry_idx: int, exit_idx: int, entry_price: float) -> tuple[float, float]:
    window = price.iloc[entry_idx : exit_idx + 1]
    highs = pd.to_numeric(window["high"], errors="coerce").dropna()
    lows = pd.to_numeric(window["low"], errors="coerce").dropna()
    mfe = (float(highs.max()) / entry_price - 1.0) * 100.0 if not highs.empty else math.nan
    mae = (float(lows.min()) / entry_price - 1.0) * 100.0 if not lows.empty else math.nan
    return mfe, mae


def incomplete_trade(reason: str) -> dict[str, Any]:
    return {
        "entry_price": math.nan,
        "exit_date": "",
        "exit_price": math.nan,
        "exit_reason": reason,
        "holding_days": "",
        "return_pct": math.nan,
        "mfe_pct": math.nan,
        "mae_pct": math.nan,
        "outcome_result": "incomplete",
        "positive_return_result": "incomplete",
    }


def finish_trade(
    price: pd.DataFrame,
    entry_idx: int,
    exit_idx: int,
    entry_price: float,
    exit_price: float,
    exit_reason: str,
    outcome_result: str,
) -> dict[str, Any]:
    return_pct = (exit_price / entry_price - 1.0) * 100.0 if entry_price > 0 else math.nan
    mfe, mae = mfe_mae(price, entry_idx, exit_idx, entry_price)
    positive = "positive" if not math.isnan(return_pct) and return_pct > 0 else "non_positive"
    return {
        "entry_price": entry_price,
        "exit_date": normalize_date(price.iloc[exit_idx].get("date")),
        "exit_price": exit_price,
        "exit_reason": exit_reason,
        "holding_days": str(exit_idx - entry_idx + 1),
        "return_pct": return_pct,
        "mfe_pct": mfe,
        "mae_pct": mae,
        "outcome_result": outcome_result,
        "positive_return_result": positive,
    }


def simulate_exit_rule(price: pd.DataFrame, entry_idx: int, stop_level: float, exit_rule_id: str) -> dict[str, Any]:
    hold_days = 10 if exit_rule_id == "fixed_10d_close" else 20
    planned_exit_idx = entry_idx + hold_days - 1
    if entry_idx >= len(price) or planned_exit_idx >= len(price):
        return incomplete_trade("insufficient_forward_price_history")
    entry_price = safe_float(price.iloc[entry_idx].get("open"))
    if math.isnan(entry_price) or entry_price <= 0:
        return incomplete_trade("invalid_entry_open")
    if math.isnan(stop_level) or stop_level <= 0:
        return incomplete_trade("invalid_stop_level")

    reached_five_close = False
    for day_idx in range(entry_idx, planned_exit_idx + 1):
        day = price.iloc[day_idx]
        low = safe_float(day.get("low"))
        high = safe_float(day.get("high"))
        close = safe_float(day.get("close"))
        if not math.isnan(low) and low <= stop_level:
            exit_price = stop_price_for_day(day, stop_level)
            return finish_trade(price, entry_idx, day_idx, entry_price, exit_price, "stop_hit", "loss")
        if exit_rule_id == "tp10_intraday_or_fixed_20d_close" and not math.isnan(high) and high >= entry_price * 1.10:
            return finish_trade(price, entry_idx, day_idx, entry_price, entry_price * 1.10, "tp10_intraday", "win")
        if exit_rule_id == "tp10_close_or_neutral_after_5pct_close_20d" and not math.isnan(close):
            close_return_pct = (close / entry_price - 1.0) * 100.0
            if close_return_pct >= 10.0:
                return finish_trade(price, entry_idx, day_idx, entry_price, close, "tp10_close", "win")
            if reached_five_close and close_return_pct <= 5.0:
                return finish_trade(price, entry_idx, day_idx, entry_price, close, "neutral_after_5pct_pullback", "neutral")
            if close_return_pct >= 5.0:
                reached_five_close = True

    close_exit = safe_float(price.iloc[planned_exit_idx].get("close"))
    if math.isnan(close_exit) or close_exit <= 0:
        return incomplete_trade("invalid_planned_exit_close")
    if exit_rule_id in {"fixed_10d_close", "fixed_20d_close"}:
        outcome = "win" if close_exit > entry_price else "loss"
    else:
        outcome = "loss"
    return finish_trade(price, entry_idx, planned_exit_idx, entry_price, close_exit, exit_rule_id, outcome)


def build_base_trades(events: pd.DataFrame, generated_at: str) -> pd.DataFrame:
    rows: list[dict[str, Any]] = []
    price_cache: dict[str, pd.DataFrame] = {}
    for _, source in events.iterrows():
        stock_id = safe_str(source.get("stock_id"))
        if stock_id not in price_cache:
            price_cache[stock_id] = read_price_file(stock_id)
        price = price_cache[stock_id]
        entry_idx = index_for_date(price, source.get("retest_entry_date")) if not price.empty else None
        for stop_rule_id in STOP_RULE_IDS:
            stop_level = stop_level_for(stop_rule_id, source, price) if not price.empty else math.nan
            for exit_rule_id in EXIT_RULE_IDS:
                trade = (
                    simulate_exit_rule(price, entry_idx, stop_level, exit_rule_id)
                    if entry_idx is not None
                    else incomplete_trade("missing_retest_entry_price_row")
                )
                rows.append(
                    {
                        "research_id": RESEARCH_ID,
                        "research_variant_id": RESEARCH_VARIANT_ID,
                        "parameter_set_id": PARAMETER_SET_ID,
                        "source_research_id": SOURCE_RESEARCH_ID,
                        "source_parameter_set_id": SOURCE_PARAMETER_SET_ID,
                        "advisory_status": RESEARCH_VARIANT_ID,
                        "event_family_id": EVENT_FAMILY_ID,
                        "pattern_subtype": safe_str(source.get("pattern_subtype")),
                        "stock_id": stock_id,
                        "stock_name": safe_str(source.get("stock_name")),
                        "signal_date": normalize_date(source.get("signal_date")),
                        "retest_date": normalize_date(source.get("retest_date")),
                        "retest_attack_date": normalize_date(source.get("retest_attack_date")),
                        "retest_entry_date": normalize_date(source.get("retest_entry_date")),
                        "reference_price": safe_float(source.get("reference_price")),
                        "stop_rule_id": stop_rule_id,
                        "stop_level": stop_level,
                        "exit_rule_id": exit_rule_id,
                        "outcome_rule_id": OUTCOME_RULE_BY_EXIT[exit_rule_id],
                        "market_regime": safe_str(source.get("market_regime")) or "unknown",
                        "low_position_120_pct": safe_float(source.get("low_position_120_pct")),
                        "base_width_pct": safe_float(source.get("base_width_pct")),
                        "support_touch_count": safe_str(source.get("support_touch_count")),
                        "tdcc_fresh": bool(source.get("tdcc_fresh")),
                        "tdcc_supportive": bool(source.get("tdcc_supportive")),
                        "tdcc_age_days": safe_str(source.get("tdcc_age_days")),
                        "approved_for_daily": "false",
                        "production_readiness": PRODUCTION_READINESS,
                        "generated_at": generated_at,
                        **trade,
                    }
                )
    base = pd.DataFrame(rows)
    for column in ["reference_price", "stop_level", "entry_price", "exit_price", "return_pct", "mfe_pct", "mae_pct"]:
        base[column] = pd.to_numeric(base.get(column, ""), errors="coerce")
    return base


def expand_segments(base: pd.DataFrame) -> pd.DataFrame:
    rows: list[pd.DataFrame] = []
    for segment_id, _segment_name, mask_fn in SEGMENTS:
        segment = base[mask_fn(base)].copy()
        if segment.empty:
            continue
        segment["segment_id"] = segment_id
        rows.append(segment)
    if not rows:
        raise SystemExit("ERROR: no segment rows generated")
    detail = pd.concat(rows, ignore_index=True)
    for col in DETAIL_COLUMNS:
        if col not in detail.columns:
            detail[col] = ""
    forbidden = sorted(set(detail.columns) & FORBIDDEN_PRODUCTION_FIELDS)
    if forbidden:
        raise SystemExit(f"ERROR: forbidden production fields in detail: {forbidden}")
    return detail[DETAIL_COLUMNS]


def summarize_group(group: pd.DataFrame, segment_name: str, generated_at: str) -> dict[str, str]:
    outcomes = group["outcome_result"].astype(str)
    wins = int(outcomes.eq("win").sum())
    neutral = int(outcomes.eq("neutral").sum())
    losses = int(outcomes.eq("loss").sum())
    incomplete = int(outcomes.eq("incomplete").sum())
    evaluated = wins + neutral + losses
    mature = wins + losses
    returns = to_num(group.loc[outcomes.isin(["win", "neutral", "loss"]), "return_pct"]).dropna()
    mfe = to_num(group.loc[outcomes.isin(["win", "neutral", "loss"]), "mfe_pct"]).dropna()
    mae = to_num(group.loc[outcomes.isin(["win", "neutral", "loss"]), "mae_pct"]).dropna()
    positive_count = int((returns > 0).sum())
    positive_rate = positive_count / len(returns) * 100.0 if len(returns) else math.nan
    pure_win_rate = wins / mature * 100.0 if mature else math.nan
    neutral_success = (wins + neutral) / evaluated * 100.0 if evaluated else math.nan
    return {
        "research_id": RESEARCH_ID,
        "research_variant_id": RESEARCH_VARIANT_ID,
        "parameter_set_id": PARAMETER_SET_ID,
        "source_research_id": SOURCE_RESEARCH_ID,
        "source_parameter_set_id": SOURCE_PARAMETER_SET_ID,
        "advisory_status": RESEARCH_VARIANT_ID,
        "event_family_id": EVENT_FAMILY_ID,
        "segment_id": safe_str(group["segment_id"].iloc[0]),
        "segment_name": segment_name,
        "stop_rule_id": safe_str(group["stop_rule_id"].iloc[0]),
        "exit_rule_id": safe_str(group["exit_rule_id"].iloc[0]),
        "outcome_rule_id": safe_str(group["outcome_rule_id"].iloc[0]),
        "sample_size": str(int(len(group))),
        "evaluated_sample_size": str(evaluated),
        "mature_sample_size": str(mature),
        "win_count": str(wins),
        "neutral_count": str(neutral),
        "loss_count": str(losses),
        "incomplete_count": str(incomplete),
        "pure_win_rate_pct": metric_text(pure_win_rate),
        "neutral_inclusive_success_rate_pct": metric_text(neutral_success),
        "positive_return_count": str(positive_count),
        "positive_return_rate_pct": metric_text(positive_rate),
        "stop_hit_count": str(int(group["exit_reason"].astype(str).eq("stop_hit").sum())),
        "tp10_hit_count": str(int(group["exit_reason"].astype(str).isin(["tp10_intraday", "tp10_close"]).sum())),
        "avg_return_pct": metric_text(float(returns.mean()) if len(returns) else math.nan),
        "median_return_pct": metric_text(float(returns.median()) if len(returns) else math.nan),
        "avg_mfe_pct": metric_text(float(mfe.mean()) if len(mfe) else math.nan),
        "median_mfe_pct": metric_text(float(mfe.median()) if len(mfe) else math.nan),
        "avg_mae_pct": metric_text(float(mae.mean()) if len(mae) else math.nan),
        "median_mae_pct": metric_text(float(mae.median()) if len(mae) else math.nan),
        "approved_for_daily": "false",
        "production_readiness": PRODUCTION_READINESS,
        "generated_at": generated_at,
    }


def build_summary(detail: pd.DataFrame, generated_at: str) -> pd.DataFrame:
    segment_names = {segment_id: segment_name for segment_id, segment_name, _ in SEGMENTS}
    rows: list[dict[str, str]] = []
    grouped = detail.groupby(["segment_id", "stop_rule_id", "exit_rule_id", "outcome_rule_id"], dropna=False)
    for (segment_id, _stop_rule_id, _exit_rule_id, _outcome_rule_id), group in grouped:
        rows.append(summarize_group(group, segment_names.get(safe_str(segment_id), ""), generated_at))
    summary = pd.DataFrame(rows)
    for col in SUMMARY_COLUMNS:
        if col not in summary.columns:
            summary[col] = ""
    return summary[SUMMARY_COLUMNS].sort_values(
        ["segment_id", "stop_rule_id", "exit_rule_id", "outcome_rule_id"]
    ).reset_index(drop=True)


def write_csv(df: pd.DataFrame, path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(path, index=False, encoding="utf-8-sig")


def markdown_table(df: pd.DataFrame, columns: list[str], limit: int = 30) -> list[str]:
    if df.empty:
        return ["_No rows._"]
    lines = ["| " + " | ".join(columns) + " |", "| " + " | ".join(["---"] * len(columns)) + " |"]
    for _, row in df.head(limit).iterrows():
        lines.append("| " + " | ".join(safe_str(row.get(column)) for column in columns) + " |")
    return lines


def write_markdown(summary: pd.DataFrame, detail: pd.DataFrame, generated_at: str) -> None:
    all_segment = summary[summary["segment_id"].astype(str).eq("all_retest_entries")].copy()
    ranked = all_segment.copy()
    ranked["_neutral_success"] = pd.to_numeric(ranked["neutral_inclusive_success_rate_pct"], errors="coerce")
    ranked["_pure_win"] = pd.to_numeric(ranked["pure_win_rate_pct"], errors="coerce")
    ranked["_avg_return"] = pd.to_numeric(ranked["avg_return_pct"], errors="coerce")
    ranked = ranked.sort_values(["_neutral_success", "_pure_win", "_avg_return"], ascending=[False, False, False])
    lines = [
        "# Structured Neckline Retest Entry Exit Grid",
        "",
        f"- generated_at: `{generated_at}`",
        f"- research_id: `{RESEARCH_ID}`",
        f"- source_research_id: `{SOURCE_RESEARCH_ID}`",
        f"- source_parameter_set_id: `{SOURCE_PARAMETER_SET_ID}`",
        "- production impact: `none`; this is not a production recommendation and does not modify production model conditions, scoring, ranking, PDF logic, or baseline.",
        "- advisory status: `warning_research_variant_only`; approved_for_daily=false; production readiness is `not_production_ready_research_only`.",
        "",
        "## Scope",
        "",
        "This grid only evaluates structured neckline events that already passed the research retest-not-broken then renewed attack entry path. It asks which stop and exit/outcome definition works better after that entry exists.",
        "",
        "Stop rules tested: `signal_low_stop`, `retest_low_stop`, `neckline_minus_2pct_stop`, and `source_retest_or_neckline_2pct_stop`.",
        "",
        "Exit/outcome rules tested: `fixed_10d_close`, `fixed_20d_close`, `tp10_intraday_or_fixed_20d_close`, and `tp10_close_or_neutral_after_5pct_close_20d`.",
        "",
        "Metric definitions: `pure_win_rate_pct` excludes neutral rows and is win / (win + loss). `neutral_inclusive_success_rate_pct` counts win plus neutral over evaluated rows. These are intentionally separate, so neutral is not silently renamed as win rate. `positive_return_rate_pct`, `avg_return_pct`, and `median_return_pct` are included because win rate alone is not enough when rule results are close.",
        "",
        "Intraday ordering is conservative: if a stop and a 10% target are both touched on the same day, the stop is counted first because the intraday sequence is unknown.",
        "",
        "TDCC segmentation is evaluated at the retest-entry date, not the original signal date, because this grid is about the actual retest-entry buy point.",
        "",
        "## Top All-Retest Rule Combinations",
        "",
        *markdown_table(
            ranked,
            [
                "stop_rule_id",
                "exit_rule_id",
                "sample_size",
                "evaluated_sample_size",
                "pure_win_rate_pct",
                "neutral_inclusive_success_rate_pct",
                "positive_return_rate_pct",
                "avg_return_pct",
                "median_return_pct",
                "stop_hit_count",
                "tp10_hit_count",
            ],
            limit=16,
        ),
        "",
        "## Segment Summary",
        "",
        *markdown_table(
            summary,
            [
                "segment_id",
                "stop_rule_id",
                "exit_rule_id",
                "sample_size",
                "pure_win_rate_pct",
                "neutral_inclusive_success_rate_pct",
                "positive_return_rate_pct",
                "avg_return_pct",
                "median_return_pct",
            ],
            limit=80,
        ),
        "",
        "## Research Boundary",
        "",
        "- This grid does not promote structured neckline or W-bottom breakout logic to production.",
        "- It does not write research variants into the production baseline.",
        "- It does not modify `daily_full_pipeline`, production PDF renderers, stock model contracts, ranking, or scoring.",
        "- A formal promotion/sync PR is still required before any production model change.",
        "",
        f"Detail rows: `{len(detail)}`",
        f"Summary rows: `{len(summary)}`",
        "",
    ]
    LATEST_MD.parent.mkdir(parents=True, exist_ok=True)
    LATEST_MD.write_text("\n".join(lines), encoding="utf-8")


def main() -> int:
    generated_at = now_text()
    events = read_source_events()
    base = build_base_trades(events, generated_at)
    detail = expand_segments(base)
    summary = build_summary(detail, generated_at)
    write_csv(detail, LATEST_DETAIL_CSV)
    write_csv(summary, LATEST_SUMMARY_CSV)
    write_csv(detail, HISTORY_DETAIL_CSV)
    write_csv(summary, HISTORY_SUMMARY_CSV)
    write_markdown(summary, detail, generated_at)
    print(
        "structured neckline retest entry/exit grid built "
        f"events={len(events)} detail_rows={len(detail)} summary_rows={len(summary)}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
