from __future__ import annotations

from datetime import datetime
from pathlib import Path
from typing import Any, Callable
from zoneinfo import ZoneInfo
import math

import pandas as pd


ROOT = Path(".")
PRICE_DIR = ROOT / "data" / "stock_price_history"
RESEARCH_LATEST_DIR = ROOT / "output" / "latest" / "research_backtest"
RESEARCH_HISTORY_DIR = ROOT / "output" / "history" / "research"

SOURCE_DETAIL_CSV = RESEARCH_LATEST_DIR / "w_bottom_split_entry_outcome_backtest_detail_latest.csv"

LATEST_DETAIL_CSV = RESEARCH_LATEST_DIR / "w_bottom_early_entry_parameter_grid_detail_latest.csv"
LATEST_GRID_CSV = RESEARCH_LATEST_DIR / "w_bottom_early_entry_parameter_grid_latest.csv"
LATEST_MD = RESEARCH_LATEST_DIR / "w_bottom_early_entry_parameter_grid_latest.md"
HISTORY_DETAIL_CSV = RESEARCH_HISTORY_DIR / "w_bottom_early_entry_parameter_grid_detail.csv"
HISTORY_GRID_CSV = RESEARCH_HISTORY_DIR / "w_bottom_early_entry_parameter_grid.csv"

MODEL_ID = "w_bottom_right_side"
CONFIRMATION_MODEL_ID = "neckline_volume_breakout_confirmation"
OVERLAY_MODEL_ID = "tdcc_weekly_ranking_formula"
RESEARCH_ID = "w_bottom_early_entry_parameter_grid"
SOURCE_RESEARCH_ID = "w_bottom_split_entry_outcome_backtest"
RESEARCH_VARIANT_ID = "warning_research_variant_only"
PARAMETER_SET_ID = "w_bottom_early_entry_parameter_grid_20260626"
SURFACE_ID = "w_bottom_right_low_early_entry"
PRODUCTION_READINESS = "not_production_ready_research_only"
BASELINE_CONDITION_ID = "all_early_entry_rows"
TARGET_HORIZON_DAYS = 40
PROFIT_TARGET_PCT = 10.0
NEUTRAL_PROFIT_FLOOR_PCT = 5.0
TAKE_PROFIT_OUTCOME_ID = "take_profit_10pct_close_40d"
NEUTRAL_AFTER_GAIN_OUTCOME_ID = "tp10_or_neutral_after_5pct_close_40d"

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
    "model_id",
    "confirmation_model_id",
    "overlay_model_id",
    "research_id",
    "source_research_id",
    "research_variant_id",
    "parameter_set_id",
    "advisory_status",
    "surface_id",
    "event_set_id",
    "comparison_status",
    "entry_rule_id",
    "outcome_rule_id",
    "outcome_rule_description",
    "horizon_trading_days",
    "stock_id",
    "stock_name",
    "source_signal_date",
    "entry_signal_date",
    "left_peak_date",
    "left_low_date",
    "neckline_date",
    "right_low_date",
    "neckline_price",
    "signal_close",
    "left_low_price",
    "right_low_price",
    "second_low_gap_pct",
    "signal_rebound_from_right_low_pct",
    "neckline_distance_pct",
    "second_arc_volume_ratio",
    "first_arc_red_ratio_pct",
    "second_arc_red_ratio_pct",
    "red_ratio_delta_pct",
    "first_arc_red_count",
    "first_arc_bar_count",
    "second_arc_red_count",
    "second_arc_bar_count",
    "price_position_252_pct",
    "price_level_bucket",
    "slope_curvature_category",
    "effective_mainstream_label",
    "has_hot_theme",
    "tdcc_any_age7",
    "tdcc_any_age14",
    "entry_date",
    "entry_open_price",
    "exit_date",
    "exit_close_price",
    "exit_reason",
    "return_pct",
    "mature",
    "success",
    "positive_return",
    "neutral_outcome",
    "outcome_result",
    "approved_for_daily",
    "production_readiness",
    "generated_at",
]

GRID_COLUMNS = [
    "model_id",
    "confirmation_model_id",
    "overlay_model_id",
    "research_id",
    "source_research_id",
    "research_variant_id",
    "parameter_set_id",
    "advisory_status",
    "surface_id",
    "event_set_id",
    "entry_rule_id",
    "outcome_rule_id",
    "outcome_rule_description",
    "condition_set_id",
    "condition_set_description",
    "horizon_trading_days",
    "sample_size",
    "mature_sample_size",
    "success_count",
    "success_rate_pct",
    "positive_return_count",
    "positive_return_rate_pct",
    "neutral_count",
    "neutral_rate_pct",
    "avg_return_pct",
    "median_return_pct",
    "baseline_condition_set_id",
    "baseline_sample_size",
    "baseline_mature_sample_size",
    "baseline_success_rate_pct",
    "baseline_avg_return_pct",
    "delta_success_rate_pct_vs_all",
    "delta_avg_return_pct_vs_all",
    "sample_retention_rate_pct",
    "core_mainstream_count",
    "hot_theme_count",
    "bottom_quartile_count",
    "low_level_count",
    "mid_level_count",
    "high_level_count",
    "wv_multiple_turn_count",
    "sharp_v_count",
    "slope_break_count",
    "smooth_count",
    "avg_price_position_252_pct",
    "median_price_position_252_pct",
    "avg_second_low_gap_pct",
    "median_second_low_gap_pct",
    "avg_signal_rebound_from_right_low_pct",
    "median_signal_rebound_from_right_low_pct",
    "avg_neckline_distance_pct",
    "median_neckline_distance_pct",
    "avg_second_arc_volume_ratio",
    "median_second_arc_volume_ratio",
    "avg_red_ratio_delta_pct",
    "median_red_ratio_delta_pct",
    "sample_warning",
    "research_interpretation",
    "approved_for_daily",
    "production_readiness",
    "generated_at",
]


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


def bool_value(value: Any) -> bool:
    return safe_str(value).lower() in {"true", "1", "yes", "y"}


def bool_text(value: bool) -> str:
    return "true" if value else "false"


def metric_text(value: float, digits: int = 4) -> str:
    if math.isnan(value) or math.isinf(value):
        return ""
    return f"{value:.{digits}f}"


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


def read_csv(path: Path) -> pd.DataFrame:
    if not path.exists():
        raise SystemExit(f"ERROR: missing required input: {path}")
    return pd.read_csv(path, dtype=str, keep_default_na=False)


def write_csv(df: pd.DataFrame, path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(path, index=False, encoding="utf-8-sig")


def load_price(stock_id: str) -> pd.DataFrame:
    path = PRICE_DIR / f"{normalize_code(stock_id)}.csv"
    if not path.exists():
        return pd.DataFrame()
    price = pd.read_csv(path, dtype=str, keep_default_na=False)
    required = {"date", "open", "high", "low", "close", "volume"}
    if not required.issubset(price.columns):
        return pd.DataFrame()
    price = price.copy()
    price["date"] = price["date"].map(normalize_date)
    for column in ["open", "high", "low", "close", "volume"]:
        price[column] = pd.to_numeric(price[column], errors="coerce")
    return price[price["date"].ne("")].sort_values("date").reset_index(drop=True)


def date_index(price: pd.DataFrame, date: str) -> int | None:
    date = normalize_date(date)
    if not date or price.empty:
        return None
    matches = price.index[price["date"].eq(date)]
    if len(matches) == 0:
        return None
    return int(matches[0])


def window_by_dates(price: pd.DataFrame, start_date: str, end_date: str) -> pd.DataFrame:
    start_idx = date_index(price, start_date)
    end_idx = date_index(price, end_date)
    if start_idx is None or end_idx is None or end_idx < start_idx:
        return pd.DataFrame()
    return price.iloc[start_idx : end_idx + 1].copy()


def red_stats(window: pd.DataFrame) -> tuple[int, int, float]:
    if window.empty:
        return 0, 0, math.nan
    valid = window[window["open"].notna() & window["close"].notna()].copy()
    if valid.empty:
        return 0, 0, math.nan
    red_count = int(valid["close"].gt(valid["open"]).sum())
    bar_count = int(len(valid))
    return red_count, bar_count, red_count / bar_count * 100.0


def avg_volume(window: pd.DataFrame) -> float:
    if window.empty or "volume" not in window.columns:
        return math.nan
    values = pd.to_numeric(window["volume"], errors="coerce").dropna()
    return float(values.mean()) if len(values) else math.nan


def price_at(price: pd.DataFrame, date: str, column: str) -> float:
    idx = date_index(price, date)
    if idx is None or column not in price.columns:
        return math.nan
    return safe_float(price.iloc[idx].get(column))


def feature_key(row: pd.Series) -> tuple[str, str, str, str, str, str]:
    return (
        normalize_code(row.get("stock_id")),
        normalize_date(row.get("source_signal_date")),
        normalize_date(row.get("left_peak_date")),
        normalize_date(row.get("left_low_date")),
        normalize_date(row.get("neckline_date")),
        normalize_date(row.get("right_low_date")),
    )


def compute_features(row: pd.Series, cache: dict[tuple[str, str, str, str, str, str], dict[str, str]]) -> dict[str, str]:
    key = feature_key(row)
    if key in cache:
        return cache[key]

    stock_id, signal_date, left_peak_date, left_low_date, neckline_date, right_low_date = key
    price = load_price(stock_id)

    signal_close = price_at(price, signal_date, "close")
    left_low_price = price_at(price, left_low_date, "low")
    right_low_price = price_at(price, right_low_date, "low")
    neckline_price = safe_float(row.get("neckline_price"))

    second_low_gap = (
        (right_low_price / left_low_price - 1.0) * 100.0
        if right_low_price > 0 and left_low_price > 0
        else math.nan
    )
    rebound_from_right_low = (
        (signal_close / right_low_price - 1.0) * 100.0
        if signal_close > 0 and right_low_price > 0
        else math.nan
    )
    neckline_distance = (
        (signal_close / neckline_price - 1.0) * 100.0
        if signal_close > 0 and neckline_price > 0
        else math.nan
    )

    first_arc = window_by_dates(price, left_peak_date, neckline_date)
    second_arc = window_by_dates(price, neckline_date, signal_date)
    first_red_count, first_bar_count, first_red_ratio = red_stats(first_arc)
    second_red_count, second_bar_count, second_red_ratio = red_stats(second_arc)
    first_volume = avg_volume(first_arc)
    second_volume = avg_volume(second_arc)
    second_arc_volume_ratio = second_volume / first_volume if first_volume > 0 and second_volume > 0 else math.nan
    red_ratio_delta = second_red_ratio - first_red_ratio if not math.isnan(second_red_ratio) and not math.isnan(first_red_ratio) else math.nan

    features = {
        "signal_close": metric_text(signal_close),
        "left_low_price": metric_text(left_low_price),
        "right_low_price": metric_text(right_low_price),
        "second_low_gap_pct": metric_text(second_low_gap),
        "signal_rebound_from_right_low_pct": metric_text(rebound_from_right_low),
        "neckline_distance_pct": metric_text(neckline_distance),
        "second_arc_volume_ratio": metric_text(second_arc_volume_ratio),
        "first_arc_red_ratio_pct": metric_text(first_red_ratio),
        "second_arc_red_ratio_pct": metric_text(second_red_ratio),
        "red_ratio_delta_pct": metric_text(red_ratio_delta),
        "first_arc_red_count": str(first_red_count),
        "first_arc_bar_count": str(first_bar_count),
        "second_arc_red_count": str(second_red_count),
        "second_arc_bar_count": str(second_bar_count),
    }
    cache[key] = features
    return features


def event_key(row: pd.Series) -> tuple[str, str, str, str, str, str, str]:
    return (
        safe_str(row.get("event_set_id")),
        normalize_code(row.get("stock_id")),
        normalize_date(row.get("source_signal_date")),
        normalize_date(row.get("entry_signal_date")),
        normalize_date(row.get("left_peak_date")),
        normalize_date(row.get("neckline_date")),
        normalize_date(row.get("right_low_date")),
    )


def result_label(*, mature: bool, success: bool, neutral: bool) -> str:
    if neutral:
        return "neutral"
    if not mature:
        return "incomplete"
    return "win" if success else "loss"


def base_detail_row(row: pd.Series, features: dict[str, str], generated_at: str) -> dict[str, Any]:
    out = {
        "model_id": MODEL_ID,
        "confirmation_model_id": CONFIRMATION_MODEL_ID,
        "overlay_model_id": OVERLAY_MODEL_ID,
        "research_id": RESEARCH_ID,
        "source_research_id": SOURCE_RESEARCH_ID,
        "research_variant_id": RESEARCH_VARIANT_ID,
        "parameter_set_id": PARAMETER_SET_ID,
        "advisory_status": RESEARCH_VARIANT_ID,
        "surface_id": SURFACE_ID,
        "event_set_id": safe_str(row.get("event_set_id")),
        "comparison_status": safe_str(row.get("comparison_status")),
        "entry_rule_id": "right_low_signal_next_open",
        "stock_id": normalize_code(row.get("stock_id")),
        "stock_name": safe_str(row.get("stock_name")),
        "source_signal_date": normalize_date(row.get("source_signal_date")),
        "entry_signal_date": normalize_date(row.get("entry_signal_date")),
        "left_peak_date": normalize_date(row.get("left_peak_date")),
        "left_low_date": normalize_date(row.get("left_low_date")),
        "neckline_date": normalize_date(row.get("neckline_date")),
        "right_low_date": normalize_date(row.get("right_low_date")),
        "neckline_price": safe_str(row.get("neckline_price")),
        "price_position_252_pct": safe_str(row.get("price_position_252_pct")),
        "price_level_bucket": safe_str(row.get("price_level_bucket")),
        "slope_curvature_category": safe_str(row.get("slope_curvature_category")),
        "effective_mainstream_label": safe_str(row.get("effective_mainstream_label")),
        "has_hot_theme": bool_text(bool_value(row.get("has_hot_theme"))),
        "tdcc_any_age7": bool_text(bool_value(row.get("tdcc_any_age7"))),
        "tdcc_any_age14": bool_text(bool_value(row.get("tdcc_any_age14"))),
        "approved_for_daily": "false",
        "production_readiness": PRODUCTION_READINESS,
        "generated_at": generated_at,
    }
    out.update(features)
    return out


def copy_source_outcome_row(row: pd.Series, features: dict[str, str], generated_at: str) -> dict[str, Any]:
    mature = bool_value(row.get("mature"))
    success = bool_value(row.get("success"))
    out = base_detail_row(row, features, generated_at)
    out.update(
        {
            "entry_rule_id": safe_str(row.get("entry_rule_id")),
            "outcome_rule_id": safe_str(row.get("outcome_rule_id")),
            "outcome_rule_description": safe_str(row.get("outcome_rule_description")),
            "horizon_trading_days": safe_str(row.get("horizon_trading_days")),
            "entry_date": normalize_date(row.get("entry_date")),
            "entry_open_price": safe_str(row.get("entry_open_price")),
            "exit_date": normalize_date(row.get("exit_date")),
            "exit_close_price": safe_str(row.get("exit_close_price")),
            "exit_reason": safe_str(row.get("exit_reason")),
            "return_pct": safe_str(row.get("return_pct")),
            "mature": bool_text(mature),
            "success": bool_text(success),
            "positive_return": bool_text(bool_value(row.get("positive_return"))),
            "neutral_outcome": "false",
            "outcome_result": result_label(mature=mature, success=success, neutral=False),
        }
    )
    return out


def incomplete_target_row(
    row: pd.Series,
    features: dict[str, str],
    generated_at: str,
    *,
    outcome_rule_id: str,
    description: str,
    exit_reason: str,
) -> dict[str, Any]:
    out = base_detail_row(row, features, generated_at)
    out.update(
        {
            "outcome_rule_id": outcome_rule_id,
            "outcome_rule_description": description,
            "horizon_trading_days": str(TARGET_HORIZON_DAYS),
            "entry_date": "",
            "entry_open_price": "",
            "exit_date": "",
            "exit_close_price": "",
            "exit_reason": exit_reason,
            "return_pct": "",
            "mature": "false",
            "success": "false",
            "positive_return": "false",
            "neutral_outcome": "false",
            "outcome_result": "incomplete",
        }
    )
    return out


def close_return_pct(close: float, entry_open: float) -> float:
    return (close / entry_open - 1.0) * 100.0 if close > 0 and entry_open > 0 else math.nan


def target_profit_row(
    row: pd.Series,
    features: dict[str, str],
    generated_at: str,
    *,
    outcome_rule_id: str,
    description: str,
    neutral_after_gain: bool,
) -> dict[str, Any]:
    stock_id = normalize_code(row.get("stock_id"))
    signal_date = normalize_date(row.get("entry_signal_date") or row.get("source_signal_date"))
    price = load_price(stock_id)
    signal_idx = date_index(price, signal_date)
    if signal_idx is None:
        return incomplete_target_row(
            row,
            features,
            generated_at,
            outcome_rule_id=outcome_rule_id,
            description=description,
            exit_reason="missing_entry_signal_date",
        )
    entry_idx = signal_idx + 1
    exit_limit = entry_idx + TARGET_HORIZON_DAYS - 1
    if exit_limit >= len(price):
        return incomplete_target_row(
            row,
            features,
            generated_at,
            outcome_rule_id=outcome_rule_id,
            description=description,
            exit_reason="insufficient_future_price",
        )

    entry_open = safe_float(price.iloc[entry_idx].get("open"))
    if math.isnan(entry_open) or entry_open <= 0:
        return incomplete_target_row(
            row,
            features,
            generated_at,
            outcome_rule_id=outcome_rule_id,
            description=description,
            exit_reason="missing_entry_price",
        )

    exit_idx = exit_limit
    exit_reason = f"fixed_{TARGET_HORIZON_DAYS}d_close_no_10pct_target"
    success = False
    neutral = False
    exceeded_neutral_floor = False
    for idx in range(entry_idx, exit_limit + 1):
        close = safe_float(price.iloc[idx].get("close"))
        ret = close_return_pct(close, entry_open)
        if math.isnan(ret):
            continue
        if ret >= PROFIT_TARGET_PCT:
            exit_idx = idx
            exit_reason = "target_10pct_close"
            success = True
            neutral = False
            break
        if neutral_after_gain:
            if exceeded_neutral_floor and ret <= NEUTRAL_PROFIT_FLOOR_PCT:
                exit_idx = idx
                exit_reason = "neutral_returned_to_5pct_after_above_5pct"
                success = False
                neutral = True
                break
            if ret > NEUTRAL_PROFIT_FLOOR_PCT:
                exceeded_neutral_floor = True

    exit_close = safe_float(price.iloc[exit_idx].get("close"))
    if math.isnan(exit_close):
        return incomplete_target_row(
            row,
            features,
            generated_at,
            outcome_rule_id=outcome_rule_id,
            description=description,
            exit_reason="missing_exit_price",
        )
    return_pct = close_return_pct(exit_close, entry_open)
    mature = not neutral
    out = base_detail_row(row, features, generated_at)
    out.update(
        {
            "outcome_rule_id": outcome_rule_id,
            "outcome_rule_description": description,
            "horizon_trading_days": str(TARGET_HORIZON_DAYS),
            "entry_date": normalize_date(price.iloc[entry_idx].get("date")),
            "entry_open_price": metric_text(entry_open),
            "exit_date": normalize_date(price.iloc[exit_idx].get("date")),
            "exit_close_price": metric_text(exit_close),
            "exit_reason": exit_reason,
            "return_pct": metric_text(return_pct),
            "mature": bool_text(mature),
            "success": bool_text(success),
            "positive_return": bool_text(return_pct > 0),
            "neutral_outcome": bool_text(neutral),
            "outcome_result": result_label(mature=mature, success=success, neutral=neutral),
        }
    )
    return out


def derived_target_rows(row: pd.Series, features: dict[str, str], generated_at: str) -> list[dict[str, Any]]:
    return [
        target_profit_row(
            row,
            features,
            generated_at,
            outcome_rule_id=TAKE_PROFIT_OUTCOME_ID,
            description=(
                "Buy next open after right-low observation signal; first close at +10% or better "
                "within 40 trading days is a win, otherwise sell day-40 close."
            ),
            neutral_after_gain=False,
        ),
        target_profit_row(
            row,
            features,
            generated_at,
            outcome_rule_id=NEUTRAL_AFTER_GAIN_OUTCOME_ID,
            description=(
                "Buy next open; first close at +10% or better is a win. If close return first exceeds "
                "+5% but returns to +5% before +10%, record a neutral sample excluded from win/loss."
            ),
            neutral_after_gain=True,
        ),
    ]


def build_detail(generated_at: str) -> pd.DataFrame:
    source = read_csv(SOURCE_DETAIL_CSV)
    required = {
        "surface_id",
        "event_set_id",
        "entry_rule_id",
        "outcome_rule_id",
        "stock_id",
        "source_signal_date",
        "left_peak_date",
        "left_low_date",
        "neckline_date",
        "right_low_date",
        "entry_open_price",
        "exit_close_price",
        "return_pct",
        "mature",
        "success",
        "approved_for_daily",
    }
    missing = sorted(required - set(source.columns))
    if missing:
        raise SystemExit(f"ERROR: source split outcome detail missing columns: {missing}")

    early = source[source["surface_id"].eq(SURFACE_ID)].copy()
    cache: dict[tuple[str, str, str, str, str, str], dict[str, str]] = {}
    rows: list[dict[str, Any]] = []
    target_seen: set[tuple[str, str, str, str, str, str, str]] = set()
    for _, row in early.iterrows():
        features = compute_features(row, cache)
        rows.append(copy_source_outcome_row(row, features, generated_at))
        key = event_key(row)
        if key not in target_seen:
            rows.extend(derived_target_rows(row, features, generated_at))
            target_seen.add(key)

    detail = pd.DataFrame(rows)
    for column in DETAIL_COLUMNS:
        if column not in detail.columns:
            detail[column] = ""
    forbidden = sorted(set(detail.columns) & FORBIDDEN_PRODUCTION_FIELDS)
    if forbidden:
        raise SystemExit(f"ERROR: forbidden production columns in early-entry detail: {forbidden}")
    return detail[DETAIL_COLUMNS]


def num(series: pd.Series) -> pd.Series:
    return pd.to_numeric(series, errors="coerce")


def condition_specs() -> list[tuple[str, str, Callable[[pd.DataFrame], pd.Series]]]:
    return [
        (BASELINE_CONDITION_ID, "All W-bottom early-entry outcome rows.", lambda df: pd.Series(True, index=df.index)),
        ("price_position_le_40", "price_position_252_pct <= 40.", lambda df: num(df["price_position_252_pct"]).le(40.0)),
        ("price_position_le_30", "price_position_252_pct <= 30.", lambda df: num(df["price_position_252_pct"]).le(30.0)),
        ("price_position_le_25", "price_position_252_pct <= 25.", lambda df: num(df["price_position_252_pct"]).le(25.0)),
        ("bottom_quartile_level", "Signal is in the bottom-quartile price level bucket.", lambda df: df["price_level_bucket"].eq("bottom_quartile_level")),
        ("bottom_or_low_level", "Signal is bottom-quartile or low-level.", lambda df: df["price_level_bucket"].isin(["bottom_quartile_level", "low_level"])),
        ("core_mainstream", "Taxonomy segment is core_mainstream.", lambda df: df["effective_mainstream_label"].eq("core_mainstream")),
        ("core_mainstream_price_le40", "core_mainstream and price_position_252_pct <= 40.", lambda df: df["effective_mainstream_label"].eq("core_mainstream") & num(df["price_position_252_pct"]).le(40.0)),
        ("core_mainstream_price_le30", "core_mainstream and price_position_252_pct <= 30.", lambda df: df["effective_mainstream_label"].eq("core_mainstream") & num(df["price_position_252_pct"]).le(30.0)),
        ("core_mainstream_price_le25", "core_mainstream and price_position_252_pct <= 25.", lambda df: df["effective_mainstream_label"].eq("core_mainstream") & num(df["price_position_252_pct"]).le(25.0)),
        ("second_low_gap_m3_p6", "Right low is -3% to +6% versus left low.", lambda df: num(df["second_low_gap_pct"]).between(-3.0, 6.0, inclusive="both")),
        ("second_low_gap_m5_p8", "Right low is -5% to +8% versus left low.", lambda df: num(df["second_low_gap_pct"]).between(-5.0, 8.0, inclusive="both")),
        ("right_rebound_3_12", "Signal close is 3% to 12% above right low.", lambda df: num(df["signal_rebound_from_right_low_pct"]).between(3.0, 12.0, inclusive="both")),
        ("right_rebound_3_20", "Signal close is 3% to 20% above right low.", lambda df: num(df["signal_rebound_from_right_low_pct"]).between(3.0, 20.0, inclusive="both")),
        ("right_rebound_5_20", "Signal close is 5% to 20% above right low.", lambda df: num(df["signal_rebound_from_right_low_pct"]).between(5.0, 20.0, inclusive="both")),
        ("second_arc_volume_gte1_2", "Second arc average volume is at least 1.2x first arc average volume.", lambda df: num(df["second_arc_volume_ratio"]).ge(1.2)),
        ("second_arc_volume_gte1_5", "Second arc average volume is at least 1.5x first arc average volume.", lambda df: num(df["second_arc_volume_ratio"]).ge(1.5)),
        ("second_red_ratio_gt_first", "Second arc red-candle ratio is greater than first arc red-candle ratio.", lambda df: num(df["red_ratio_delta_pct"]).gt(0.0)),
        ("second_red_delta_gte10", "Second arc red-candle ratio is at least 10 pct points above first arc.", lambda df: num(df["red_ratio_delta_pct"]).ge(10.0)),
        ("exclude_wv_multiple_turn", "Exclude WV/WVV multiple-turn path category.", lambda df: ~df["slope_curvature_category"].eq("wv_multiple_turn_risk")),
        ("below_neckline_at_least_5", "Signal close is at least 5% below neckline.", lambda df: num(df["neckline_distance_pct"]).le(-5.0)),
        ("below_neckline_5_to_30", "Signal close is 5% to 30% below neckline.", lambda df: num(df["neckline_distance_pct"]).between(-30.0, -5.0, inclusive="both")),
        ("price_le40_volume_gte1_2", "price_position_252_pct <= 40 and second_arc_volume_ratio >= 1.2.", lambda df: num(df["price_position_252_pct"]).le(40.0) & num(df["second_arc_volume_ratio"]).ge(1.2)),
        ("price_le40_red_ratio_gt_first", "price_position_252_pct <= 40 and second arc red ratio > first arc.", lambda df: num(df["price_position_252_pct"]).le(40.0) & num(df["red_ratio_delta_pct"]).gt(0.0)),
        ("price_le40_volume_red", "price_position_252_pct <= 40, second_arc_volume_ratio >= 1.2, and second arc red ratio > first arc.", lambda df: num(df["price_position_252_pct"]).le(40.0) & num(df["second_arc_volume_ratio"]).ge(1.2) & num(df["red_ratio_delta_pct"]).gt(0.0)),
        ("bottom_or_low_volume_red", "bottom-or-low level, second_arc_volume_ratio >= 1.2, and second arc red ratio > first arc.", lambda df: df["price_level_bucket"].isin(["bottom_quartile_level", "low_level"]) & num(df["second_arc_volume_ratio"]).ge(1.2) & num(df["red_ratio_delta_pct"]).gt(0.0)),
        ("core_mainstream_price_le40_volume_gte1_2", "core_mainstream, price_position_252_pct <= 40, and second_arc_volume_ratio >= 1.2.", lambda df: df["effective_mainstream_label"].eq("core_mainstream") & num(df["price_position_252_pct"]).le(40.0) & num(df["second_arc_volume_ratio"]).ge(1.2)),
        ("core_mainstream_price_le40_red_ratio_gt_first", "core_mainstream, price_position_252_pct <= 40, and second arc red ratio > first arc.", lambda df: df["effective_mainstream_label"].eq("core_mainstream") & num(df["price_position_252_pct"]).le(40.0) & num(df["red_ratio_delta_pct"]).gt(0.0)),
        ("core_mainstream_price_le40_volume_red", "core_mainstream, price_position_252_pct <= 40, second_arc_volume_ratio >= 1.2, and second arc red ratio > first arc.", lambda df: df["effective_mainstream_label"].eq("core_mainstream") & num(df["price_position_252_pct"]).le(40.0) & num(df["second_arc_volume_ratio"]).ge(1.2) & num(df["red_ratio_delta_pct"]).gt(0.0)),
        ("core_mainstream_price_le40_gap_m5_p8_rebound_3_20", "core_mainstream, price_position_252_pct <= 40, right low -5% to +8%, and signal rebound 3% to 20%.", lambda df: df["effective_mainstream_label"].eq("core_mainstream") & num(df["price_position_252_pct"]).le(40.0) & num(df["second_low_gap_pct"]).between(-5.0, 8.0, inclusive="both") & num(df["signal_rebound_from_right_low_pct"]).between(3.0, 20.0, inclusive="both")),
        ("core_mainstream_price_le40_gap_m3_p6_rebound_3_12", "core_mainstream, price_position_252_pct <= 40, right low -3% to +6%, and signal rebound 3% to 12%.", lambda df: df["effective_mainstream_label"].eq("core_mainstream") & num(df["price_position_252_pct"]).le(40.0) & num(df["second_low_gap_pct"]).between(-3.0, 6.0, inclusive="both") & num(df["signal_rebound_from_right_low_pct"]).between(3.0, 12.0, inclusive="both")),
        ("core_mainstream_price_le40_exclude_wv", "core_mainstream, price_position_252_pct <= 40, and exclude WV/WVV.", lambda df: df["effective_mainstream_label"].eq("core_mainstream") & num(df["price_position_252_pct"]).le(40.0) & ~df["slope_curvature_category"].eq("wv_multiple_turn_risk")),
        ("core_mainstream_price_le40_volume_exclude_wv", "core_mainstream, price_position_252_pct <= 40, second_arc_volume_ratio >= 1.2, and exclude WV/WVV.", lambda df: df["effective_mainstream_label"].eq("core_mainstream") & num(df["price_position_252_pct"]).le(40.0) & num(df["second_arc_volume_ratio"]).ge(1.2) & ~df["slope_curvature_category"].eq("wv_multiple_turn_risk")),
        ("core_mainstream_price_le40_below_neckline5", "core_mainstream, price_position_252_pct <= 40, and signal is at least 5% below neckline.", lambda df: df["effective_mainstream_label"].eq("core_mainstream") & num(df["price_position_252_pct"]).le(40.0) & num(df["neckline_distance_pct"]).le(-5.0)),
        ("core_mainstream_price_le40_volume_red_below_neckline5", "core_mainstream, price_position_252_pct <= 40, second_arc_volume_ratio >= 1.2, second arc red ratio > first arc, and signal at least 5% below neckline.", lambda df: df["effective_mainstream_label"].eq("core_mainstream") & num(df["price_position_252_pct"]).le(40.0) & num(df["second_arc_volume_ratio"]).ge(1.2) & num(df["red_ratio_delta_pct"]).gt(0.0) & num(df["neckline_distance_pct"]).le(-5.0)),
    ]


def metric_series(sample: pd.DataFrame, column: str) -> pd.Series:
    if sample.empty or column not in sample.columns:
        return pd.Series(dtype=float)
    return pd.to_numeric(sample[column], errors="coerce").dropna()


def metrics(sample: pd.DataFrame) -> dict[str, Any]:
    mature = sample[sample["mature"].map(bool_value)].copy() if not sample.empty else pd.DataFrame()
    returns = metric_series(mature, "return_pct")
    sample_size = int(len(sample))
    mature_size = int(len(returns))
    success_count = int(mature["success"].map(bool_value).sum()) if mature_size else 0
    positive_count = int(mature["positive_return"].map(bool_value).sum()) if mature_size else 0
    neutral_count = int(sample["neutral_outcome"].map(bool_value).sum()) if sample_size else 0
    level_counts = sample["price_level_bucket"].value_counts().to_dict() if sample_size else {}
    path_counts = sample["slope_curvature_category"].value_counts().to_dict() if sample_size else {}
    return {
        "sample_size": sample_size,
        "mature_sample_size": mature_size,
        "success_count": success_count,
        "success_rate_pct_num": success_count / mature_size * 100.0 if mature_size else math.nan,
        "positive_return_count": positive_count,
        "positive_return_rate_pct_num": positive_count / mature_size * 100.0 if mature_size else math.nan,
        "neutral_count": neutral_count,
        "neutral_rate_pct_num": neutral_count / sample_size * 100.0 if sample_size else math.nan,
        "avg_return_pct_num": float(returns.mean()) if mature_size else math.nan,
        "median_return_pct_num": float(returns.median()) if mature_size else math.nan,
        "core_mainstream_count": int(sample["effective_mainstream_label"].eq("core_mainstream").sum()) if sample_size else 0,
        "hot_theme_count": int(sample["has_hot_theme"].map(bool_value).sum()) if sample_size else 0,
        "bottom_quartile_count": int(level_counts.get("bottom_quartile_level", 0)),
        "low_level_count": int(level_counts.get("low_level", 0)),
        "mid_level_count": int(level_counts.get("mid_level", 0)),
        "high_level_count": int(level_counts.get("high_level", 0)),
        "wv_multiple_turn_count": int(path_counts.get("wv_multiple_turn_risk", 0)),
        "sharp_v_count": int(path_counts.get("sharp_v_bottom_risk", 0)),
        "slope_break_count": int(path_counts.get("slope_break_discontinuous", 0)),
        "smooth_count": int(path_counts.get("smooth_rounded_w_like", 0)),
        "avg_price_position_252_pct_num": float(metric_series(sample, "price_position_252_pct").mean()) if sample_size else math.nan,
        "median_price_position_252_pct_num": float(metric_series(sample, "price_position_252_pct").median()) if sample_size else math.nan,
        "avg_second_low_gap_pct_num": float(metric_series(sample, "second_low_gap_pct").mean()) if sample_size else math.nan,
        "median_second_low_gap_pct_num": float(metric_series(sample, "second_low_gap_pct").median()) if sample_size else math.nan,
        "avg_signal_rebound_from_right_low_pct_num": float(metric_series(sample, "signal_rebound_from_right_low_pct").mean()) if sample_size else math.nan,
        "median_signal_rebound_from_right_low_pct_num": float(metric_series(sample, "signal_rebound_from_right_low_pct").median()) if sample_size else math.nan,
        "avg_neckline_distance_pct_num": float(metric_series(sample, "neckline_distance_pct").mean()) if sample_size else math.nan,
        "median_neckline_distance_pct_num": float(metric_series(sample, "neckline_distance_pct").median()) if sample_size else math.nan,
        "avg_second_arc_volume_ratio_num": float(metric_series(sample, "second_arc_volume_ratio").mean()) if sample_size else math.nan,
        "median_second_arc_volume_ratio_num": float(metric_series(sample, "second_arc_volume_ratio").median()) if sample_size else math.nan,
        "avg_red_ratio_delta_pct_num": float(metric_series(sample, "red_ratio_delta_pct").mean()) if sample_size else math.nan,
        "median_red_ratio_delta_pct_num": float(metric_series(sample, "red_ratio_delta_pct").median()) if sample_size else math.nan,
    }


def sample_warning(mature_sample_size: int) -> str:
    if mature_sample_size < 5:
        return "tiny_mature_sample_research_only"
    if mature_sample_size < 15:
        return "low_mature_sample_research_only"
    if mature_sample_size < 30:
        return "directional_only_below_promotion_review_size"
    return "medium_mature_sample_research_only"


def interpretation(row_metrics: dict[str, Any], baseline_metrics: dict[str, Any], condition_set_id: str) -> str:
    if condition_set_id == BASELINE_CONDITION_ID:
        return "baseline_reference"
    if row_metrics["mature_sample_size"] < 30:
        return "too_small_for_parameter_decision"
    success_delta = row_metrics["success_rate_pct_num"] - baseline_metrics["success_rate_pct_num"]
    avg_delta = row_metrics["avg_return_pct_num"] - baseline_metrics["avg_return_pct_num"]
    median_delta = row_metrics["median_return_pct_num"] - baseline_metrics["median_return_pct_num"]
    if math.isnan(success_delta) or math.isnan(avg_delta) or math.isnan(median_delta):
        return "insufficient_baseline_comparison"
    if success_delta >= 5.0 and avg_delta > 0 and median_delta >= 0:
        return "candidate_for_manual_promotion_review"
    if success_delta > 0 and avg_delta > 0:
        return "directionally_better_than_all_same_event"
    if success_delta > 0 or avg_delta > 0:
        return "mixed_vs_all_same_event"
    return "not_better_than_all_same_event"


def grid_row(
    *,
    base: pd.DataFrame,
    condition_sample: pd.DataFrame,
    condition_set_id: str,
    condition_set_description: str,
    event_set_id: str,
    entry_rule_id: str,
    outcome_rule_id: str,
    outcome_rule_description: str,
    horizon_days: str,
    generated_at: str,
) -> dict[str, Any]:
    row_metrics = metrics(condition_sample)
    baseline_metrics = metrics(base)
    sample_size = row_metrics["sample_size"]
    baseline_size = baseline_metrics["sample_size"]
    success_delta = row_metrics["success_rate_pct_num"] - baseline_metrics["success_rate_pct_num"]
    avg_delta = row_metrics["avg_return_pct_num"] - baseline_metrics["avg_return_pct_num"]
    return {
        "model_id": MODEL_ID,
        "confirmation_model_id": CONFIRMATION_MODEL_ID,
        "overlay_model_id": OVERLAY_MODEL_ID,
        "research_id": RESEARCH_ID,
        "source_research_id": SOURCE_RESEARCH_ID,
        "research_variant_id": RESEARCH_VARIANT_ID,
        "parameter_set_id": PARAMETER_SET_ID,
        "advisory_status": RESEARCH_VARIANT_ID,
        "surface_id": SURFACE_ID,
        "event_set_id": event_set_id,
        "entry_rule_id": entry_rule_id,
        "outcome_rule_id": outcome_rule_id,
        "outcome_rule_description": outcome_rule_description,
        "condition_set_id": condition_set_id,
        "condition_set_description": condition_set_description,
        "horizon_trading_days": horizon_days,
        "sample_size": row_metrics["sample_size"],
        "mature_sample_size": row_metrics["mature_sample_size"],
        "success_count": row_metrics["success_count"],
        "success_rate_pct": metric_text(row_metrics["success_rate_pct_num"]),
        "positive_return_count": row_metrics["positive_return_count"],
        "positive_return_rate_pct": metric_text(row_metrics["positive_return_rate_pct_num"]),
        "neutral_count": row_metrics["neutral_count"],
        "neutral_rate_pct": metric_text(row_metrics["neutral_rate_pct_num"]),
        "avg_return_pct": metric_text(row_metrics["avg_return_pct_num"]),
        "median_return_pct": metric_text(row_metrics["median_return_pct_num"]),
        "baseline_condition_set_id": BASELINE_CONDITION_ID,
        "baseline_sample_size": baseline_metrics["sample_size"],
        "baseline_mature_sample_size": baseline_metrics["mature_sample_size"],
        "baseline_success_rate_pct": metric_text(baseline_metrics["success_rate_pct_num"]),
        "baseline_avg_return_pct": metric_text(baseline_metrics["avg_return_pct_num"]),
        "delta_success_rate_pct_vs_all": metric_text(success_delta),
        "delta_avg_return_pct_vs_all": metric_text(avg_delta),
        "sample_retention_rate_pct": metric_text(sample_size / baseline_size * 100.0 if baseline_size else math.nan),
        "core_mainstream_count": row_metrics["core_mainstream_count"],
        "hot_theme_count": row_metrics["hot_theme_count"],
        "bottom_quartile_count": row_metrics["bottom_quartile_count"],
        "low_level_count": row_metrics["low_level_count"],
        "mid_level_count": row_metrics["mid_level_count"],
        "high_level_count": row_metrics["high_level_count"],
        "wv_multiple_turn_count": row_metrics["wv_multiple_turn_count"],
        "sharp_v_count": row_metrics["sharp_v_count"],
        "slope_break_count": row_metrics["slope_break_count"],
        "smooth_count": row_metrics["smooth_count"],
        "avg_price_position_252_pct": metric_text(row_metrics["avg_price_position_252_pct_num"]),
        "median_price_position_252_pct": metric_text(row_metrics["median_price_position_252_pct_num"]),
        "avg_second_low_gap_pct": metric_text(row_metrics["avg_second_low_gap_pct_num"]),
        "median_second_low_gap_pct": metric_text(row_metrics["median_second_low_gap_pct_num"]),
        "avg_signal_rebound_from_right_low_pct": metric_text(row_metrics["avg_signal_rebound_from_right_low_pct_num"]),
        "median_signal_rebound_from_right_low_pct": metric_text(row_metrics["median_signal_rebound_from_right_low_pct_num"]),
        "avg_neckline_distance_pct": metric_text(row_metrics["avg_neckline_distance_pct_num"]),
        "median_neckline_distance_pct": metric_text(row_metrics["median_neckline_distance_pct_num"]),
        "avg_second_arc_volume_ratio": metric_text(row_metrics["avg_second_arc_volume_ratio_num"]),
        "median_second_arc_volume_ratio": metric_text(row_metrics["median_second_arc_volume_ratio_num"]),
        "avg_red_ratio_delta_pct": metric_text(row_metrics["avg_red_ratio_delta_pct_num"]),
        "median_red_ratio_delta_pct": metric_text(row_metrics["median_red_ratio_delta_pct_num"]),
        "sample_warning": sample_warning(row_metrics["mature_sample_size"]),
        "research_interpretation": interpretation(row_metrics, baseline_metrics, condition_set_id),
        "approved_for_daily": "false",
        "production_readiness": PRODUCTION_READINESS,
        "generated_at": generated_at,
    }


def build_grid(detail: pd.DataFrame, generated_at: str) -> pd.DataFrame:
    rows: list[dict[str, Any]] = []
    group_keys = ["event_set_id", "entry_rule_id", "outcome_rule_id", "outcome_rule_description", "horizon_trading_days"]
    for group_values, group in detail.groupby(group_keys, dropna=False):
        event_set_id, entry_rule_id, outcome_rule_id, description, horizon_days = [safe_str(v) for v in group_values]
        base = group.copy()
        for condition_id, condition_description, condition in condition_specs():
            mask = condition(group).fillna(False)
            sample = group[mask].copy()
            rows.append(
                grid_row(
                    base=base,
                    condition_sample=sample,
                    condition_set_id=condition_id,
                    condition_set_description=condition_description,
                    event_set_id=event_set_id,
                    entry_rule_id=entry_rule_id,
                    outcome_rule_id=outcome_rule_id,
                    outcome_rule_description=description,
                    horizon_days=horizon_days,
                    generated_at=generated_at,
                )
            )
    grid = pd.DataFrame(rows)
    for column in GRID_COLUMNS:
        if column not in grid.columns:
            grid[column] = ""
    forbidden = sorted(set(grid.columns) & FORBIDDEN_PRODUCTION_FIELDS)
    if forbidden:
        raise SystemExit(f"ERROR: forbidden production columns in early-entry grid: {forbidden}")
    return grid[GRID_COLUMNS]


def markdown_table(rows: pd.DataFrame, columns: list[str], limit: int) -> list[str]:
    if rows.empty:
        return ["_No rows._"]
    clipped = rows.head(limit)
    lines = [
        "| " + " | ".join(columns) + " |",
        "| " + " | ".join(["---"] * len(columns)) + " |",
    ]
    for _, row in clipped.iterrows():
        lines.append("| " + " | ".join(safe_str(row.get(column)) for column in columns) + " |")
    return lines


def write_markdown(grid: pd.DataFrame, generated_at: str) -> None:
    variant = grid[
        grid["event_set_id"].eq("variant_nearest_micro_45d_event_replay")
        & pd.to_numeric(grid["mature_sample_size"], errors="coerce").ge(30)
        & ~grid["condition_set_id"].eq(BASELINE_CONDITION_ID)
    ].copy()
    variant["success_rate_sort"] = pd.to_numeric(variant["success_rate_pct"], errors="coerce")
    variant["avg_return_sort"] = pd.to_numeric(variant["avg_return_pct"], errors="coerce")
    variant["delta_success_sort"] = pd.to_numeric(variant["delta_success_rate_pct_vs_all"], errors="coerce")
    top_variant = variant.sort_values(
        ["success_rate_sort", "avg_return_sort", "delta_success_sort"], ascending=[False, False, False]
    )
    review = variant[variant["research_interpretation"].isin(["candidate_for_manual_promotion_review", "directionally_better_than_all_same_event"])].copy()
    review = review.sort_values(["delta_success_sort", "avg_return_sort"], ascending=[False, False])

    lines = [
        "# W-Bottom Early-Entry Parameter Grid",
        "",
        f"- generated_at: `{generated_at}`",
        f"- source_research_id: `{SOURCE_RESEARCH_ID}`",
        "- production impact: `none`",
        "- price convention: entry uses next trading day's open; exit uses exit day's close.",
        "- surface: `w_bottom_right_low_early_entry` only.",
        "- purpose: compare second-low early-entry conditions before any production model promotion.",
        "- added outcome rules: `take_profit_10pct_close_40d` and `tp10_or_neutral_after_5pct_close_40d`.",
        "- neutral rule: after a close return first exceeds +5%, a later close back to +5% before +10% remains in `sample_size` but is excluded from win/loss denominator.",
        "",
        "## Top Variant Rows",
        "",
        *markdown_table(
            top_variant,
            [
                "outcome_rule_id",
                "condition_set_id",
                "sample_size",
                "mature_sample_size",
                "success_rate_pct",
                "neutral_count",
                "neutral_rate_pct",
                "avg_return_pct",
                "median_return_pct",
                "delta_success_rate_pct_vs_all",
                "delta_avg_return_pct_vs_all",
                "sample_warning",
            ],
            30,
        ),
        "",
        "## Candidate Review Rows",
        "",
        *markdown_table(
            review,
            [
                "outcome_rule_id",
                "condition_set_id",
                "sample_size",
                "mature_sample_size",
                "success_rate_pct",
                "neutral_count",
                "neutral_rate_pct",
                "avg_return_pct",
                "median_return_pct",
                "research_interpretation",
            ],
            30,
        ),
        "",
        "## Guardrails",
        "",
        "- This is research/backtest advisory-only work.",
        "- Rows remain `approved_for_daily=false` and `warning_research_variant_only`.",
        "- This grid does not modify production conditions, scoring, ranking, PDFs, or baselines.",
        "- Neutral outcomes remain research-only and must not be treated as production approval.",
        "- Strong-looking rows are promotion-review candidates only; they are not production rules.",
    ]
    LATEST_MD.parent.mkdir(parents=True, exist_ok=True)
    LATEST_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    generated_at = now_text()
    detail = build_detail(generated_at)
    grid = build_grid(detail, generated_at)
    if detail.empty or grid.empty:
        raise SystemExit("ERROR: early-entry parameter grid generated no rows")
    write_csv(detail, LATEST_DETAIL_CSV)
    write_csv(detail, HISTORY_DETAIL_CSV)
    write_csv(grid, LATEST_GRID_CSV)
    write_csv(grid, HISTORY_GRID_CSV)
    write_markdown(grid, generated_at)
    print(f"Saved: {LATEST_DETAIL_CSV} rows={len(detail)}")
    print(f"Saved: {LATEST_GRID_CSV} rows={len(grid)}")
    print(f"Saved: {LATEST_MD}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
