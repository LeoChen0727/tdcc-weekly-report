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

SOURCE_DETAIL_CSV = RESEARCH_LATEST_DIR / "w_bottom_combined_condition_backtest_detail_latest.csv"

LATEST_DETAIL_CSV = RESEARCH_LATEST_DIR / "w_bottom_split_entry_outcome_backtest_detail_latest.csv"
LATEST_SUMMARY_CSV = RESEARCH_LATEST_DIR / "w_bottom_split_entry_outcome_backtest_latest.csv"
LATEST_MD = RESEARCH_LATEST_DIR / "w_bottom_split_entry_outcome_backtest_latest.md"
HISTORY_DETAIL_CSV = RESEARCH_HISTORY_DIR / "w_bottom_split_entry_outcome_backtest_detail.csv"
HISTORY_SUMMARY_CSV = RESEARCH_HISTORY_DIR / "w_bottom_split_entry_outcome_backtest.csv"

MODEL_ID = "w_bottom_right_side"
CONFIRMATION_MODEL_ID = "neckline_volume_breakout_confirmation"
OVERLAY_MODEL_ID = "tdcc_weekly_ranking_formula"
RESEARCH_ID = "w_bottom_split_entry_outcome_backtest"
SOURCE_RESEARCH_ID = "w_bottom_combined_condition_backtest"
RESEARCH_VARIANT_ID = "warning_research_variant_only"
PARAMETER_SET_ID = "w_bottom_split_entry_outcome_backtest_20260626"
PRODUCTION_READINESS = "not_production_ready_research_only"

BASELINE_EVENT_SET_ID = "baseline_current_detector"
VARIANT_EVENT_SET_ID = "variant_nearest_micro_45d_event_replay"

SURFACE_BREAKOUT = "w_bottom_neckline_volume_breakout_confirmation"
SURFACE_EARLY = "w_bottom_right_low_early_entry"

FORBIDDEN_PRODUCTION_FIELDS = {
    "trade_decision",
    "action_rating",
    "entry_style",
    "position_sizing",
    "decision_score",
    "daily_candidate_decision",
    "buy_signal",
}

BREAKOUT_HORIZONS = [5, 10, 20, 30]
EARLY_FIXED_HORIZONS = [10, 20, 30, 40]
TARGET_HORIZON_DAYS = 40

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
    "breakout_date",
    "post_confirmation_date",
    "neckline_price",
    "right_low_stop_level",
    "entry_date",
    "entry_open_price",
    "exit_date",
    "exit_close_price",
    "exit_reason",
    "return_pct",
    "mature",
    "success",
    "positive_return",
    "has_neckline_breakout",
    "has_post_confirmation",
    "tdcc_any_age7",
    "tdcc_any_age14",
    "price_position_252_pct",
    "price_level_bucket",
    "slope_curvature_category",
    "effective_mainstream_label",
    "has_hot_theme",
    "manual_review_status",
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
    "surface_id",
    "event_set_id",
    "entry_rule_id",
    "outcome_rule_id",
    "condition_set_id",
    "condition_set_description",
    "horizon_trading_days",
    "sample_size",
    "mature_sample_size",
    "success_count",
    "success_rate_pct",
    "positive_return_count",
    "positive_return_rate_pct",
    "avg_return_pct",
    "median_return_pct",
    "baseline_sample_size",
    "baseline_mature_sample_size",
    "baseline_success_rate_pct",
    "baseline_avg_return_pct",
    "delta_success_rate_pct_vs_baseline",
    "delta_avg_return_pct_vs_baseline",
    "sample_retention_rate_pct",
    "tdcc_any_age7_count",
    "tdcc_any_age14_count",
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
    required = {"date", "open", "close"}
    if not required.issubset(price.columns):
        return pd.DataFrame()
    price = price.copy()
    price["date"] = price["date"].map(normalize_date)
    for column in ["open", "close"]:
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


def base_output_row(source: pd.Series, generated_at: str) -> dict[str, Any]:
    return {
        "model_id": MODEL_ID,
        "confirmation_model_id": CONFIRMATION_MODEL_ID,
        "overlay_model_id": OVERLAY_MODEL_ID,
        "research_id": RESEARCH_ID,
        "source_research_id": SOURCE_RESEARCH_ID,
        "research_variant_id": RESEARCH_VARIANT_ID,
        "parameter_set_id": PARAMETER_SET_ID,
        "advisory_status": RESEARCH_VARIANT_ID,
        "event_set_id": safe_str(source.get("event_set_id")),
        "comparison_status": safe_str(source.get("comparison_status")),
        "stock_id": normalize_code(source.get("stock_id")),
        "stock_name": safe_str(source.get("stock_name")),
        "source_signal_date": normalize_date(source.get("signal_date")),
        "left_peak_date": normalize_date(source.get("left_peak_date")),
        "left_low_date": normalize_date(source.get("left_low_date")),
        "neckline_date": normalize_date(source.get("neckline_date")),
        "right_low_date": normalize_date(source.get("right_low_date")),
        "breakout_date": normalize_date(source.get("breakout_date")),
        "post_confirmation_date": normalize_date(source.get("post_confirmation_date")),
        "neckline_price": safe_str(source.get("neckline_price")),
        "has_neckline_breakout": bool_text(bool_value(source.get("has_neckline_breakout"))),
        "has_post_confirmation": bool_text(bool_value(source.get("has_post_confirmation"))),
        "tdcc_any_age7": bool_text(bool_value(source.get("tdcc_any_age7"))),
        "tdcc_any_age14": bool_text(bool_value(source.get("tdcc_any_age14"))),
        "price_position_252_pct": safe_str(source.get("price_position_252_pct")),
        "price_level_bucket": safe_str(source.get("price_level_bucket")),
        "slope_curvature_category": safe_str(source.get("slope_curvature_category")),
        "effective_mainstream_label": safe_str(source.get("effective_mainstream_label")),
        "has_hot_theme": bool_text(bool_value(source.get("has_hot_theme"))),
        "manual_review_status": "pending_user_model_review",
        "approved_for_daily": "false",
        "production_readiness": PRODUCTION_READINESS,
        "generated_at": generated_at,
    }


def failed_trade_row(
    source: pd.Series,
    generated_at: str,
    *,
    surface_id: str,
    entry_rule_id: str,
    outcome_rule_id: str,
    description: str,
    horizon_days: int,
    entry_signal_date: str,
    exit_reason: str,
) -> dict[str, Any]:
    row = base_output_row(source, generated_at)
    row.update(
        {
            "surface_id": surface_id,
            "entry_rule_id": entry_rule_id,
            "outcome_rule_id": outcome_rule_id,
            "outcome_rule_description": description,
            "horizon_trading_days": horizon_days,
            "entry_signal_date": entry_signal_date,
            "right_low_stop_level": right_low_close(source),
            "entry_date": "",
            "entry_open_price": "",
            "exit_date": "",
            "exit_close_price": "",
            "exit_reason": exit_reason,
            "return_pct": "",
            "mature": "false",
            "success": "false",
            "positive_return": "false",
        }
    )
    return row


def right_low_close(source: pd.Series) -> str:
    stock_id = normalize_code(source.get("stock_id"))
    right_low_date = normalize_date(source.get("right_low_date"))
    price = load_price(stock_id)
    idx = date_index(price, right_low_date)
    if idx is None:
        return ""
    close = safe_float(price.iloc[idx].get("close"))
    return metric_text(close) if not math.isnan(close) else ""


def fixed_horizon_trade(
    source: pd.Series,
    generated_at: str,
    *,
    surface_id: str,
    entry_rule_id: str,
    outcome_rule_id: str,
    description: str,
    signal_date: str,
    horizon_days: int,
) -> dict[str, Any]:
    stock_id = normalize_code(source.get("stock_id"))
    price = load_price(stock_id)
    signal_idx = date_index(price, signal_date)
    if signal_idx is None:
        return failed_trade_row(
            source,
            generated_at,
            surface_id=surface_id,
            entry_rule_id=entry_rule_id,
            outcome_rule_id=outcome_rule_id,
            description=description,
            horizon_days=horizon_days,
            entry_signal_date=signal_date,
            exit_reason="missing_entry_signal_date",
        )
    entry_idx = signal_idx + 1
    exit_idx = entry_idx + horizon_days - 1
    if exit_idx >= len(price):
        return failed_trade_row(
            source,
            generated_at,
            surface_id=surface_id,
            entry_rule_id=entry_rule_id,
            outcome_rule_id=outcome_rule_id,
            description=description,
            horizon_days=horizon_days,
            entry_signal_date=signal_date,
            exit_reason="insufficient_future_price",
        )
    entry_open = safe_float(price.iloc[entry_idx].get("open"))
    exit_close = safe_float(price.iloc[exit_idx].get("close"))
    if math.isnan(entry_open) or math.isnan(exit_close) or entry_open <= 0:
        return failed_trade_row(
            source,
            generated_at,
            surface_id=surface_id,
            entry_rule_id=entry_rule_id,
            outcome_rule_id=outcome_rule_id,
            description=description,
            horizon_days=horizon_days,
            entry_signal_date=signal_date,
            exit_reason="missing_entry_or_exit_price",
        )
    return_pct = (exit_close / entry_open - 1.0) * 100.0
    row = base_output_row(source, generated_at)
    row.update(
        {
            "surface_id": surface_id,
            "entry_rule_id": entry_rule_id,
            "outcome_rule_id": outcome_rule_id,
            "outcome_rule_description": description,
            "horizon_trading_days": horizon_days,
            "entry_signal_date": signal_date,
            "right_low_stop_level": right_low_close(source),
            "entry_date": normalize_date(price.iloc[entry_idx].get("date")),
            "entry_open_price": metric_text(entry_open),
            "exit_date": normalize_date(price.iloc[exit_idx].get("date")),
            "exit_close_price": metric_text(exit_close),
            "exit_reason": f"fixed_{horizon_days}d_close",
            "return_pct": metric_text(return_pct),
            "mature": "true",
            "success": bool_text(return_pct > 0),
            "positive_return": bool_text(return_pct > 0),
        }
    )
    return row


def target_or_stop_trade(
    source: pd.Series,
    generated_at: str,
    *,
    outcome_rule_id: str,
    description: str,
    target_mode: str,
) -> dict[str, Any]:
    stock_id = normalize_code(source.get("stock_id"))
    signal_date = normalize_date(source.get("signal_date"))
    price = load_price(stock_id)
    signal_idx = date_index(price, signal_date)
    if signal_idx is None:
        return failed_trade_row(
            source,
            generated_at,
            surface_id=SURFACE_EARLY,
            entry_rule_id="right_low_signal_next_open",
            outcome_rule_id=outcome_rule_id,
            description=description,
            horizon_days=TARGET_HORIZON_DAYS,
            entry_signal_date=signal_date,
            exit_reason="missing_entry_signal_date",
        )
    entry_idx = signal_idx + 1
    exit_limit = entry_idx + TARGET_HORIZON_DAYS - 1
    if exit_limit >= len(price):
        return failed_trade_row(
            source,
            generated_at,
            surface_id=SURFACE_EARLY,
            entry_rule_id="right_low_signal_next_open",
            outcome_rule_id=outcome_rule_id,
            description=description,
            horizon_days=TARGET_HORIZON_DAYS,
            entry_signal_date=signal_date,
            exit_reason="insufficient_future_price",
        )
    entry_open = safe_float(price.iloc[entry_idx].get("open"))
    if math.isnan(entry_open) or entry_open <= 0:
        return failed_trade_row(
            source,
            generated_at,
            surface_id=SURFACE_EARLY,
            entry_rule_id="right_low_signal_next_open",
            outcome_rule_id=outcome_rule_id,
            description=description,
            horizon_days=TARGET_HORIZON_DAYS,
            entry_signal_date=signal_date,
            exit_reason="missing_entry_price",
        )

    neckline = safe_float(source.get("neckline_price"))
    right_low_stop = safe_float(right_low_close(source))
    breakout_date = normalize_date(source.get("breakout_date"))
    exit_idx = exit_limit
    exit_reason = f"fixed_{TARGET_HORIZON_DAYS}d_close_no_target"
    success = False

    for idx in range(entry_idx, exit_limit + 1):
        row = price.iloc[idx]
        close = safe_float(row.get("close"))
        date = normalize_date(row.get("date"))
        if not math.isnan(right_low_stop) and not math.isnan(close) and close <= right_low_stop:
            exit_idx = idx
            exit_reason = "right_low_close_stop"
            success = False
            break
        if target_mode == "neckline_close" and not math.isnan(neckline) and not math.isnan(close) and close >= neckline:
            exit_idx = idx
            exit_reason = "target_neckline_close"
            success = True
            break
        if target_mode == "volume_breakout" and breakout_date and date == breakout_date:
            exit_idx = idx
            exit_reason = "target_volume_breakout_close"
            success = True
            break

    exit_close = safe_float(price.iloc[exit_idx].get("close"))
    if math.isnan(exit_close):
        return failed_trade_row(
            source,
            generated_at,
            surface_id=SURFACE_EARLY,
            entry_rule_id="right_low_signal_next_open",
            outcome_rule_id=outcome_rule_id,
            description=description,
            horizon_days=TARGET_HORIZON_DAYS,
            entry_signal_date=signal_date,
            exit_reason="missing_exit_price",
        )
    return_pct = (exit_close / entry_open - 1.0) * 100.0
    output = base_output_row(source, generated_at)
    output.update(
        {
            "surface_id": SURFACE_EARLY,
            "entry_rule_id": "right_low_signal_next_open",
            "outcome_rule_id": outcome_rule_id,
            "outcome_rule_description": description,
            "horizon_trading_days": TARGET_HORIZON_DAYS,
            "entry_signal_date": signal_date,
            "right_low_stop_level": metric_text(right_low_stop),
            "entry_date": normalize_date(price.iloc[entry_idx].get("date")),
            "entry_open_price": metric_text(entry_open),
            "exit_date": normalize_date(price.iloc[exit_idx].get("date")),
            "exit_close_price": metric_text(exit_close),
            "exit_reason": exit_reason,
            "return_pct": metric_text(return_pct),
            "mature": "true",
            "success": bool_text(success),
            "positive_return": bool_text(return_pct > 0),
        }
    )
    return output


def build_detail(generated_at: str) -> pd.DataFrame:
    source = read_csv(SOURCE_DETAIL_CSV)
    rows: list[dict[str, Any]] = []
    for _, source_row in source.iterrows():
        signal_date = normalize_date(source_row.get("signal_date"))
        breakout_date = normalize_date(source_row.get("breakout_date"))
        post_confirmation_date = normalize_date(source_row.get("post_confirmation_date"))

        for horizon in BREAKOUT_HORIZONS:
            if breakout_date:
                rows.append(
                    fixed_horizon_trade(
                        source_row,
                        generated_at,
                        surface_id=SURFACE_BREAKOUT,
                        entry_rule_id="neckline_volume_breakout_next_open",
                        outcome_rule_id=f"fixed_{horizon}d_close_positive_return",
                        description=f"Buy next open after neckline volume breakout; sell close after {horizon} trading days; success is positive return.",
                        signal_date=breakout_date,
                        horizon_days=horizon,
                    )
                )
            if post_confirmation_date:
                rows.append(
                    fixed_horizon_trade(
                        source_row,
                        generated_at,
                        surface_id=SURFACE_BREAKOUT,
                        entry_rule_id="post_confirmation_next_open",
                        outcome_rule_id=f"fixed_{horizon}d_close_positive_return",
                        description=f"Buy next open after post-confirmation trigger; sell close after {horizon} trading days; success is positive return.",
                        signal_date=post_confirmation_date,
                        horizon_days=horizon,
                    )
                )

        for horizon in EARLY_FIXED_HORIZONS:
            rows.append(
                fixed_horizon_trade(
                    source_row,
                    generated_at,
                    surface_id=SURFACE_EARLY,
                    entry_rule_id="right_low_signal_next_open",
                    outcome_rule_id=f"fixed_{horizon}d_close_positive_return",
                    description=f"Buy next open after right-low observation signal; sell close after {horizon} trading days; success is positive return.",
                    signal_date=signal_date,
                    horizon_days=horizon,
                )
            )
        rows.append(
            target_or_stop_trade(
                source_row,
                generated_at,
                outcome_rule_id="reach_neckline_close_before_right_low_stop_40d",
                description="Buy next open after right-low observation signal; sell close when close reaches neckline, when close breaks right-low stop, or at 40 trading days. Success is reaching neckline first.",
                target_mode="neckline_close",
            )
        )
        rows.append(
            target_or_stop_trade(
                source_row,
                generated_at,
                outcome_rule_id="volume_breakout_close_before_right_low_stop_40d",
                description="Buy next open after right-low observation signal; sell close on volume breakout date, when close breaks right-low stop, or at 40 trading days. Success is volume breakout first.",
                target_mode="volume_breakout",
            )
        )

    detail = pd.DataFrame(rows)
    for column in DETAIL_COLUMNS:
        if column not in detail.columns:
            detail[column] = ""
    forbidden = sorted(set(detail.columns) & FORBIDDEN_PRODUCTION_FIELDS)
    if forbidden:
        raise SystemExit(f"ERROR: forbidden production columns in split detail: {forbidden}")
    return detail[DETAIL_COLUMNS]


def condition_specs() -> list[tuple[str, str, Callable[[pd.DataFrame], pd.Series]]]:
    return [
        ("all", "All rows in this surface/entry/outcome group.", lambda df: pd.Series(True, index=df.index)),
        ("price_position_252_le_40", "price_position_252_pct <= 40.", lambda df: pd.to_numeric(df["price_position_252_pct"], errors="coerce").le(40.0)),
        ("bottom_or_low_level", "bottom_quartile_level or low_level.", lambda df: df["price_level_bucket"].isin(["bottom_quartile_level", "low_level"])),
        ("core_mainstream", "effective_mainstream_label is core_mainstream.", lambda df: df["effective_mainstream_label"].eq("core_mainstream")),
        ("core_mainstream_price_le40", "core_mainstream and price_position_252_pct <= 40.", lambda df: df["effective_mainstream_label"].eq("core_mainstream") & pd.to_numeric(df["price_position_252_pct"], errors="coerce").le(40.0)),
        ("exclude_wv_multiple_turn", "Exclude WV/WVV multiple-turn path category.", lambda df: ~df["slope_curvature_category"].eq("wv_multiple_turn_risk")),
        ("price_le40_exclude_wv", "price_position_252_pct <= 40 and exclude WV/WVV.", lambda df: pd.to_numeric(df["price_position_252_pct"], errors="coerce").le(40.0) & ~df["slope_curvature_category"].eq("wv_multiple_turn_risk")),
        ("tdcc_any_age7", "TDCC age<=7 match.", lambda df: df["tdcc_any_age7"].map(bool_value)),
        ("tdcc_any_age14", "TDCC age<=14 match.", lambda df: df["tdcc_any_age14"].map(bool_value)),
    ]


def metrics(sample: pd.DataFrame) -> dict[str, Any]:
    mature = sample[sample["mature"].map(bool_value)].copy() if not sample.empty else pd.DataFrame()
    returns = pd.to_numeric(mature["return_pct"], errors="coerce").dropna() if not mature.empty else pd.Series(dtype=float)
    success_count = int(mature["success"].map(bool_value).sum()) if not mature.empty else 0
    positive_count = int(mature["positive_return"].map(bool_value).sum()) if not mature.empty else 0
    mature_count = int(len(returns))
    sample_size = int(len(sample))
    level_counts = sample["price_level_bucket"].value_counts().to_dict() if sample_size else {}
    category_counts = sample["slope_curvature_category"].value_counts().to_dict() if sample_size else {}
    return {
        "sample_size": sample_size,
        "mature_sample_size": mature_count,
        "success_count": success_count,
        "success_rate_pct_num": success_count / mature_count * 100.0 if mature_count else math.nan,
        "positive_return_count": positive_count,
        "positive_return_rate_pct_num": positive_count / mature_count * 100.0 if mature_count else math.nan,
        "avg_return_pct_num": float(returns.mean()) if mature_count else math.nan,
        "median_return_pct_num": float(returns.median()) if mature_count else math.nan,
        "tdcc_any_age7_count": int(sample["tdcc_any_age7"].map(bool_value).sum()) if sample_size else 0,
        "tdcc_any_age14_count": int(sample["tdcc_any_age14"].map(bool_value).sum()) if sample_size else 0,
        "core_mainstream_count": int(sample["effective_mainstream_label"].eq("core_mainstream").sum()) if sample_size else 0,
        "hot_theme_count": int(sample["has_hot_theme"].map(bool_value).sum()) if sample_size else 0,
        "bottom_quartile_count": int(level_counts.get("bottom_quartile_level", 0)),
        "low_level_count": int(level_counts.get("low_level", 0)),
        "mid_level_count": int(level_counts.get("mid_level", 0)),
        "high_level_count": int(level_counts.get("high_level", 0)),
        "wv_multiple_turn_count": int(category_counts.get("wv_multiple_turn_risk", 0)),
        "sharp_v_count": int(category_counts.get("sharp_v_bottom_risk", 0)),
        "slope_break_count": int(category_counts.get("slope_break_discontinuous", 0)),
        "smooth_count": int(category_counts.get("smooth_rounded_w_like", 0)),
    }


def sample_warning(mature_count: int) -> str:
    if mature_count < 5:
        return "tiny_mature_sample_research_only"
    if mature_count < 15:
        return "low_mature_sample_research_only"
    if mature_count < 30:
        return "directional_only_below_promotion_review_size"
    return "medium_mature_sample_research_only"


def interpretation(row_metrics: dict[str, Any], baseline_metrics: dict[str, Any], event_set_id: str) -> str:
    if row_metrics["mature_sample_size"] < 5:
        return "too_small_for_directional_read"
    if event_set_id == BASELINE_EVENT_SET_ID:
        return "baseline_reference"
    success_delta = row_metrics["success_rate_pct_num"] - baseline_metrics["success_rate_pct_num"]
    avg_delta = row_metrics["avg_return_pct_num"] - baseline_metrics["avg_return_pct_num"]
    if math.isnan(success_delta) or math.isnan(avg_delta):
        return "insufficient_baseline_comparison"
    if success_delta > 0 and avg_delta > 0:
        return "directionally_better_than_baseline_same_definition"
    if success_delta > 0 or avg_delta > 0:
        return "mixed_vs_baseline_same_definition"
    return "not_better_than_baseline_same_definition"


def summary_row(
    *,
    group: tuple[str, str, str, str, int],
    condition_id: str,
    condition_description: str,
    row_metrics: dict[str, Any],
    baseline_metrics: dict[str, Any],
    generated_at: str,
) -> dict[str, Any]:
    surface_id, event_set_id, entry_rule_id, outcome_rule_id, horizon_days = group
    baseline_sample = baseline_metrics["sample_size"]
    row_sample = row_metrics["sample_size"]
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
        "surface_id": surface_id,
        "event_set_id": event_set_id,
        "entry_rule_id": entry_rule_id,
        "outcome_rule_id": outcome_rule_id,
        "condition_set_id": condition_id,
        "condition_set_description": condition_description,
        "horizon_trading_days": horizon_days,
        "sample_size": row_metrics["sample_size"],
        "mature_sample_size": row_metrics["mature_sample_size"],
        "success_count": row_metrics["success_count"],
        "success_rate_pct": metric_text(row_metrics["success_rate_pct_num"]),
        "positive_return_count": row_metrics["positive_return_count"],
        "positive_return_rate_pct": metric_text(row_metrics["positive_return_rate_pct_num"]),
        "avg_return_pct": metric_text(row_metrics["avg_return_pct_num"]),
        "median_return_pct": metric_text(row_metrics["median_return_pct_num"]),
        "baseline_sample_size": baseline_metrics["sample_size"],
        "baseline_mature_sample_size": baseline_metrics["mature_sample_size"],
        "baseline_success_rate_pct": metric_text(baseline_metrics["success_rate_pct_num"]),
        "baseline_avg_return_pct": metric_text(baseline_metrics["avg_return_pct_num"]),
        "delta_success_rate_pct_vs_baseline": metric_text(success_delta),
        "delta_avg_return_pct_vs_baseline": metric_text(avg_delta),
        "sample_retention_rate_pct": metric_text(row_sample / baseline_sample * 100.0 if baseline_sample else math.nan),
        "tdcc_any_age7_count": row_metrics["tdcc_any_age7_count"],
        "tdcc_any_age14_count": row_metrics["tdcc_any_age14_count"],
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
        "sample_warning": sample_warning(row_metrics["mature_sample_size"]),
        "research_interpretation": interpretation(row_metrics, baseline_metrics, event_set_id),
        "approved_for_daily": "false",
        "production_readiness": PRODUCTION_READINESS,
        "generated_at": generated_at,
    }


def build_summary(detail: pd.DataFrame, generated_at: str) -> pd.DataFrame:
    rows: list[dict[str, Any]] = []
    group_cols = ["surface_id", "entry_rule_id", "outcome_rule_id", "horizon_trading_days"]
    for group_values, group_df in detail.groupby(group_cols, dropna=False):
        surface_id, entry_rule_id, outcome_rule_id, horizon_days_text = group_values
        horizon_days = int(float(horizon_days_text)) if safe_str(horizon_days_text) else 0
        baseline_group = group_df[group_df["event_set_id"].eq(BASELINE_EVENT_SET_ID)].copy()
        for condition_id, description, condition in condition_specs():
            baseline_subset = baseline_group[condition(baseline_group)].copy()
            baseline_metrics = metrics(baseline_subset)
            for event_set_id in [BASELINE_EVENT_SET_ID, VARIANT_EVENT_SET_ID]:
                event_subset = group_df[group_df["event_set_id"].eq(event_set_id)].copy()
                subset = event_subset[condition(event_subset)].copy()
                rows.append(
                    summary_row(
                        group=(surface_id, event_set_id, entry_rule_id, outcome_rule_id, horizon_days),
                        condition_id=condition_id,
                        condition_description=description,
                        row_metrics=metrics(subset),
                        baseline_metrics=baseline_metrics,
                        generated_at=generated_at,
                    )
                )
    return pd.DataFrame(rows, columns=SUMMARY_COLUMNS)


def markdown_table(df: pd.DataFrame, columns: list[str], limit: int = 20) -> list[str]:
    if df.empty:
        return ["_No rows._"]
    rows = ["| " + " | ".join(columns) + " |", "| " + " | ".join(["---"] * len(columns)) + " |"]
    for _, row in df.head(limit).iterrows():
        rows.append("| " + " | ".join(safe_str(row.get(column)) for column in columns) + " |")
    return rows


def write_markdown(summary: pd.DataFrame, generated_at: str) -> None:
    variant = summary[
        summary["event_set_id"].eq(VARIANT_EVENT_SET_ID)
        & pd.to_numeric(summary["mature_sample_size"], errors="coerce").ge(15)
    ].copy()
    variant["success_sort"] = pd.to_numeric(variant["success_rate_pct"], errors="coerce")
    variant["avg_sort"] = pd.to_numeric(variant["avg_return_pct"], errors="coerce")
    variant["mature_sort"] = pd.to_numeric(variant["mature_sample_size"], errors="coerce")
    top_variant = variant.sort_values(["surface_id", "success_sort", "avg_sort", "mature_sort"], ascending=[True, False, False, False])
    lines = [
        "# W-Bottom Split Entry Outcome Backtest",
        "",
        f"- generated_at: `{generated_at}`",
        f"- source_research_id: `{SOURCE_RESEARCH_ID}`",
        "- production impact: `none`",
        "- price convention: entry uses next trading day's open; exit uses exit day's close.",
        "- breakout surface: neckline volume breakout confirmation and optional post-confirmation entries.",
        "- early-entry surface: second-low/right-low observation entry before neckline completion.",
        "- success definition is outcome-rule specific; fixed-horizon rules use positive return, target rules use target-before-stop.",
        "",
        "## Top Variant Rows By Split Surface",
        "",
        *markdown_table(
            top_variant,
            [
                "surface_id",
                "entry_rule_id",
                "outcome_rule_id",
                "condition_set_id",
                "sample_size",
                "mature_sample_size",
                "success_rate_pct",
                "positive_return_rate_pct",
                "avg_return_pct",
                "median_return_pct",
                "sample_warning",
            ],
            40,
        ),
        "",
        "## Guardrails",
        "",
        "- This is research/backtest advisory-only work.",
        "- Rows remain `approved_for_daily=false` and `warning_research_variant_only`.",
        "- The prior 10-day hold metric is only one outcome rule, not the W model definition.",
        "- Early-entry success is separated from breakout-confirmation success.",
    ]
    LATEST_MD.parent.mkdir(parents=True, exist_ok=True)
    LATEST_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    generated_at = now_text()
    detail = build_detail(generated_at)
    summary = build_summary(detail, generated_at)
    if detail.empty or summary.empty:
        raise SystemExit("ERROR: split W-bottom outcome backtest generated no rows")
    write_csv(detail, LATEST_DETAIL_CSV)
    write_csv(detail, HISTORY_DETAIL_CSV)
    write_csv(summary, LATEST_SUMMARY_CSV)
    write_csv(summary, HISTORY_SUMMARY_CSV)
    write_markdown(summary, generated_at)
    print(f"Saved: {LATEST_DETAIL_CSV} rows={len(detail)}")
    print(f"Saved: {LATEST_SUMMARY_CSV} rows={len(summary)}")
    print(f"Saved: {LATEST_MD}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
