from __future__ import annotations

from datetime import datetime
from pathlib import Path
from typing import Any
from zoneinfo import ZoneInfo
import math

import pandas as pd


ROOT = Path(".")
PRICE_DIR = ROOT / "data" / "stock_price_history"
RESEARCH_LATEST_DIR = ROOT / "output" / "latest" / "research_backtest"
RESEARCH_HISTORY_DIR = ROOT / "output" / "history" / "research"

SOURCE_CSV = RESEARCH_LATEST_DIR / "w_bottom_market_regime_gated_review_latest.csv"

LATEST_DETAIL_CSV = RESEARCH_LATEST_DIR / "w_bottom_early_entry_stop_loss_audit_detail_latest.csv"
LATEST_SUMMARY_CSV = RESEARCH_LATEST_DIR / "w_bottom_early_entry_stop_loss_audit_latest.csv"
LATEST_MD = RESEARCH_LATEST_DIR / "w_bottom_early_entry_stop_loss_audit_latest.md"
HISTORY_DETAIL_CSV = RESEARCH_HISTORY_DIR / "w_bottom_early_entry_stop_loss_audit_detail.csv"
HISTORY_SUMMARY_CSV = RESEARCH_HISTORY_DIR / "w_bottom_early_entry_stop_loss_audit.csv"

MODEL_ID = "w_bottom_right_side"
CONFIRMATION_MODEL_ID = "neckline_volume_breakout_confirmation"
OVERLAY_MODEL_ID = "tdcc_weekly_ranking_formula"
RESEARCH_ID = "w_bottom_early_entry_stop_loss_audit"
SOURCE_RESEARCH_ID = "w_bottom_market_regime_gated_review"
RESEARCH_VARIANT_ID = "warning_research_variant_only"
PARAMETER_SET_ID = "w_bottom_structure_stop_loss_review_20260629"
SURFACE_ID = "w_bottom_right_low_early_entry"
EVENT_SET_ID = "variant_nearest_micro_45d_event_replay"
ENTRY_RULE_ID = "right_low_signal_next_open"
SOURCE_OUTCOME_RULE_ID = "tp10_or_neutral_after_5pct_close_40d"
PRODUCTION_READINESS = "research_only_pending_promotion_decision"
SELECTED_SEGMENT_ID = "smooth_core_mainstream_right_rebound_5_20_bull"

TARGET_HORIZON_DAYS = 40
PROFIT_TARGET_PCT = 10.0
NEUTRAL_PROFIT_FLOOR_PCT = 5.0

STOP_RULES = [
    {
        "stop_rule_id": "no_fixed_stop_d40_v1",
        "stop_rule_description": "Baseline v1: no structure stop; win at +10% close, neutral after +5% rollback, otherwise D+40 close.",
        "stop_basis": "none",
        "stop_buffer_pct": "",
        "outcome_policy": "tp10_neutral5_d40",
    },
    {
        "stop_rule_id": "right_low_close_stop_d40",
        "stop_rule_description": "Stop when a close breaks the detected right-low price.",
        "stop_basis": "right_low_price",
        "stop_buffer_pct": "0.0000",
        "outcome_policy": "tp10_neutral5_d40",
    },
    {
        "stop_rule_id": "w_structure_low_close_stop_d40",
        "stop_rule_description": "Stop when a close breaks the lower of the detected left-low and right-low prices.",
        "stop_basis": "min_left_right_low_price",
        "stop_buffer_pct": "0.0000",
        "outcome_policy": "tp10_neutral5_d40",
    },
    {
        "stop_rule_id": "w_structure_low_stop_d20_gain10_else_d40",
        "stop_rule_description": "Stop when a close breaks the W-structure low; otherwise sell at D+20 close if D+20 return is >=10%, else hold to D+40 close.",
        "stop_basis": "min_left_right_low_price",
        "stop_buffer_pct": "0.0000",
        "outcome_policy": "d20_gain10_else_d40_positive_return",
        "early_exit_day": "20",
        "early_exit_return_pct": "10.0000",
    },
    {
        "stop_rule_id": "w_structure_low_close_stop_1pct_buffer_d40",
        "stop_rule_description": "Stop when a close breaks 1% below the lower of the detected left-low and right-low prices.",
        "stop_basis": "min_left_right_low_price",
        "stop_buffer_pct": "-1.0000",
        "outcome_policy": "tp10_neutral5_d40",
    },
]

TARGET_SEGMENT_IDS = [
    "smooth_right_rebound_5_20_strong_bull",
    "smooth_right_rebound_5_20_bull",
    "smooth_core_mainstream_right_rebound_5_20_strong_bull",
    SELECTED_SEGMENT_ID,
    "core_mainstream_price_le30_rebound_3_20_volume_red_bull",
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
    "production_readiness",
    "approved_for_daily",
    "surface_id",
    "event_set_id",
    "entry_rule_id",
    "source_outcome_rule_id",
    "stop_rule_id",
    "stop_rule_description",
    "stop_basis",
    "stop_buffer_pct",
    "segment_id",
    "segment_description",
    "stock_id",
    "stock_name",
    "source_signal_date",
    "entry_signal_date",
    "entry_date",
    "entry_open_price",
    "left_low_date",
    "right_low_date",
    "left_low_price",
    "right_low_price",
    "w_structure_low_stop_level",
    "stop_hit",
    "stop_hit_date",
    "exit_date",
    "exit_close_price",
    "exit_reason",
    "return_pct",
    "mature",
    "success",
    "positive_return",
    "neutral_outcome",
    "outcome_result",
    "signal_market_regime",
    "price_position_252_pct",
    "price_level_bucket",
    "slope_curvature_category",
    "effective_mainstream_label",
    "second_arc_volume_ratio",
    "red_ratio_delta_pct",
    "generated_at",
]

SUMMARY_COLUMNS = [
    "model_id",
    "research_id",
    "source_research_id",
    "research_variant_id",
    "parameter_set_id",
    "advisory_status",
    "production_readiness",
    "approved_for_daily",
    "surface_id",
    "event_set_id",
    "entry_rule_id",
    "source_outcome_rule_id",
    "segment_id",
    "segment_description",
    "stop_rule_id",
    "stop_rule_description",
    "stop_basis",
    "stop_buffer_pct",
    "sample_size",
    "evaluated_sample_size",
    "mature_sample_size",
    "win_count",
    "neutral_count",
    "loss_count",
    "incomplete_count",
    "stop_hit_count",
    "pure_win_rate_pct",
    "neutral_inclusive_success_rate_pct",
    "positive_return_rate_pct",
    "avg_return_pct",
    "median_return_pct",
    "min_return_pct",
    "loss_avg_return_pct",
    "baseline_stop_rule_id",
    "baseline_pure_win_rate_pct",
    "baseline_neutral_inclusive_success_rate_pct",
    "baseline_avg_return_pct",
    "baseline_min_return_pct",
    "delta_pure_win_rate_pct",
    "delta_neutral_inclusive_success_rate_pct",
    "delta_avg_return_pct",
    "min_return_improvement_pct",
    "recommendation_status",
    "interpretation",
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


def normalize_code(value: Any) -> str:
    text = safe_str(value)
    return text.zfill(4) if text.isdigit() and len(text) < 4 else text


def normalize_date(value: Any) -> str:
    text = safe_str(value).replace("-", "").replace("/", "")
    return text[:8]


def safe_float(value: Any) -> float:
    text = safe_str(value).replace(",", "").replace("%", "")
    if not text:
        return math.nan
    try:
        number = float(text)
    except ValueError:
        return math.nan
    return number if not math.isnan(number) else math.nan


def bool_text(value: bool) -> str:
    return "true" if value else "false"


def metric_text(value: float, digits: int = 4) -> str:
    if math.isnan(value) or math.isinf(value):
        return ""
    return f"{value:.{digits}f}"


def read_csv(path: Path) -> pd.DataFrame:
    if not path.exists():
        raise SystemExit(f"ERROR: missing required input: {path}")
    return pd.read_csv(path, dtype=str, keep_default_na=False)


def write_csv(df: pd.DataFrame, path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(path, index=False, encoding="utf-8-sig")


def load_price(stock_id: str) -> pd.DataFrame:
    code = normalize_code(stock_id)
    path = PRICE_DIR / f"{code}.csv"
    if not path.exists():
        raise SystemExit(f"ERROR: missing stock price history for {code}: {path}")
    df = pd.read_csv(path, dtype=str, keep_default_na=False)
    if "date" not in df.columns:
        raise SystemExit(f"ERROR: stock price history missing date column: {path}")
    df = df.copy()
    df["date_norm"] = df["date"].map(normalize_date)
    return df


def date_index(price: pd.DataFrame, date_value: Any) -> int | None:
    date = normalize_date(date_value)
    if not date:
        return None
    matches = price.index[price["date_norm"].eq(date)].tolist()
    return int(matches[0]) if matches else None


def price_value_at(price: pd.DataFrame, date_value: Any, column: str) -> float:
    idx = date_index(price, date_value)
    if idx is None or column not in price.columns:
        return math.nan
    return safe_float(price.iloc[idx].get(column))


def close_return_pct(close: float, entry_open: float) -> float:
    return (close / entry_open - 1.0) * 100.0 if close > 0 and entry_open > 0 else math.nan


def stop_level_for_rule(rule: dict[str, str], left_low: float, right_low: float) -> float:
    basis = rule["stop_basis"]
    if basis == "none":
        return math.nan
    if basis == "right_low_price":
        return right_low
    if basis == "min_left_right_low_price":
        base = min(left_low, right_low)
        buffer_pct = safe_float(rule.get("stop_buffer_pct"))
        buffer = 0.0 if math.isnan(buffer_pct) else buffer_pct / 100.0
        return base * (1.0 + buffer)
    raise ValueError(f"unknown stop basis: {basis}")


def result_label(*, success: bool, neutral: bool, incomplete: bool) -> str:
    if incomplete:
        return "incomplete"
    if success:
        return "win"
    if neutral:
        return "neutral"
    return "loss"


def source_rows() -> pd.DataFrame:
    source = read_csv(SOURCE_CSV)
    required = {
        "model_id",
        "research_id",
        "surface_id",
        "event_set_id",
        "entry_rule_id",
        "outcome_rule_id",
        "segment_id",
        "segment_description",
        "stock_id",
        "stock_name",
        "source_signal_date",
        "entry_signal_date",
        "left_low_date",
        "right_low_date",
        "signal_market_regime",
        "price_position_252_pct",
        "price_level_bucket",
        "slope_curvature_category",
        "effective_mainstream_label",
        "second_arc_volume_ratio",
        "red_ratio_delta_pct",
    }
    missing = sorted(required - set(source.columns))
    if missing:
        raise SystemExit(f"ERROR: source rows missing columns: {missing}")
    filtered = source[
        source["model_id"].eq(MODEL_ID)
        & source["research_id"].eq(SOURCE_RESEARCH_ID)
        & source["surface_id"].eq(SURFACE_ID)
        & source["event_set_id"].eq(EVENT_SET_ID)
        & source["entry_rule_id"].eq(ENTRY_RULE_ID)
        & source["outcome_rule_id"].eq(SOURCE_OUTCOME_RULE_ID)
        & source["segment_id"].isin(TARGET_SEGMENT_IDS)
    ].copy()
    if filtered.empty:
        raise SystemExit("ERROR: no W-bottom rows after source filter")
    filtered["stock_id"] = filtered["stock_id"].map(normalize_code)
    return filtered


def evaluate_row(row: pd.Series, rule: dict[str, str], generated_at: str) -> dict[str, Any]:
    stock_id = normalize_code(row.get("stock_id"))
    price = load_price(stock_id)
    signal_date = normalize_date(row.get("entry_signal_date") or row.get("source_signal_date"))
    signal_idx = date_index(price, signal_date)

    left_low = price_value_at(price, row.get("left_low_date"), "low")
    right_low = price_value_at(price, row.get("right_low_date"), "low")
    stop_level = stop_level_for_rule(rule, left_low, right_low)
    structure_low = min(left_low, right_low) if not math.isnan(left_low) and not math.isnan(right_low) else math.nan

    base = {
        "model_id": MODEL_ID,
        "confirmation_model_id": CONFIRMATION_MODEL_ID,
        "overlay_model_id": OVERLAY_MODEL_ID,
        "research_id": RESEARCH_ID,
        "source_research_id": SOURCE_RESEARCH_ID,
        "research_variant_id": RESEARCH_VARIANT_ID,
        "parameter_set_id": PARAMETER_SET_ID,
        "advisory_status": RESEARCH_VARIANT_ID,
        "production_readiness": PRODUCTION_READINESS,
        "approved_for_daily": "false",
        "surface_id": SURFACE_ID,
        "event_set_id": EVENT_SET_ID,
        "entry_rule_id": ENTRY_RULE_ID,
        "source_outcome_rule_id": SOURCE_OUTCOME_RULE_ID,
        "stop_rule_id": rule["stop_rule_id"],
        "stop_rule_description": rule["stop_rule_description"],
        "stop_basis": rule["stop_basis"],
        "stop_buffer_pct": rule["stop_buffer_pct"],
        "segment_id": safe_str(row.get("segment_id")),
        "segment_description": safe_str(row.get("segment_description")),
        "stock_id": stock_id,
        "stock_name": safe_str(row.get("stock_name")),
        "source_signal_date": normalize_date(row.get("source_signal_date")),
        "entry_signal_date": signal_date,
        "left_low_date": normalize_date(row.get("left_low_date")),
        "right_low_date": normalize_date(row.get("right_low_date")),
        "left_low_price": metric_text(left_low),
        "right_low_price": metric_text(right_low),
        "w_structure_low_stop_level": metric_text(stop_level),
        "signal_market_regime": safe_str(row.get("signal_market_regime")),
        "price_position_252_pct": safe_str(row.get("price_position_252_pct")),
        "price_level_bucket": safe_str(row.get("price_level_bucket")),
        "slope_curvature_category": safe_str(row.get("slope_curvature_category")),
        "effective_mainstream_label": safe_str(row.get("effective_mainstream_label")),
        "second_arc_volume_ratio": safe_str(row.get("second_arc_volume_ratio")),
        "red_ratio_delta_pct": safe_str(row.get("red_ratio_delta_pct")),
        "generated_at": generated_at,
    }

    if signal_idx is None:
        return incomplete_row(base, "missing_entry_signal_date")
    entry_idx = signal_idx + 1
    exit_limit = entry_idx + TARGET_HORIZON_DAYS - 1
    if exit_limit >= len(price):
        return incomplete_row(base, "insufficient_future_price")

    entry_open = safe_float(price.iloc[entry_idx].get("open"))
    if math.isnan(entry_open) or entry_open <= 0:
        return incomplete_row(base, "missing_entry_price")
    if rule["stop_basis"] != "none" and math.isnan(stop_level):
        return incomplete_row(base, "missing_stop_basis_price")

    exit_idx = exit_limit
    exit_reason = f"fixed_{TARGET_HORIZON_DAYS}d_close_no_10pct_target"
    stop_hit = False
    stop_hit_date = ""
    success = False
    neutral = False
    exceeded_neutral_floor = False
    outcome_policy = rule.get("outcome_policy", "tp10_neutral5_d40")
    early_exit_day = int(safe_float(rule.get("early_exit_day")) if safe_str(rule.get("early_exit_day")) else 0)
    early_exit_return = safe_float(rule.get("early_exit_return_pct"))
    early_exit_idx = entry_idx + early_exit_day - 1 if early_exit_day > 0 else -1

    for idx in range(entry_idx, exit_limit + 1):
        close = safe_float(price.iloc[idx].get("close"))
        if math.isnan(close):
            continue
        ret = close_return_pct(close, entry_open)
        if rule["stop_basis"] != "none" and close <= stop_level:
            exit_idx = idx
            exit_reason = rule["stop_rule_id"]
            stop_hit = True
            stop_hit_date = normalize_date(price.iloc[idx].get("date"))
            success = False
            neutral = False
            break
        if outcome_policy == "d20_gain10_else_d40_positive_return":
            if idx == early_exit_idx and not math.isnan(early_exit_return) and ret >= early_exit_return:
                exit_idx = idx
                exit_reason = "d20_gain10_close_exit"
                success = True
                neutral = False
                break
            continue
        if ret >= PROFIT_TARGET_PCT:
            exit_idx = idx
            exit_reason = "target_10pct_close"
            success = True
            neutral = False
            break
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
        return incomplete_row(base, "missing_exit_price")
    return_pct = close_return_pct(exit_close, entry_open)
    if outcome_policy == "d20_gain10_else_d40_positive_return" and not success:
        success = return_pct > 0
    output = dict(base)
    output.update(
        {
            "entry_date": normalize_date(price.iloc[entry_idx].get("date")),
            "entry_open_price": metric_text(entry_open),
            "stop_hit": bool_text(stop_hit),
            "stop_hit_date": stop_hit_date,
            "exit_date": normalize_date(price.iloc[exit_idx].get("date")),
            "exit_close_price": metric_text(exit_close),
            "exit_reason": exit_reason,
            "return_pct": metric_text(return_pct),
            "mature": bool_text(not neutral),
            "success": bool_text(success),
            "positive_return": bool_text(return_pct > 0),
            "neutral_outcome": bool_text(neutral),
            "outcome_result": result_label(success=success, neutral=neutral, incomplete=False),
        }
    )
    return output


def incomplete_row(base: dict[str, Any], exit_reason: str) -> dict[str, Any]:
    output = dict(base)
    output.update(
        {
            "entry_date": "",
            "entry_open_price": "",
            "stop_hit": "false",
            "stop_hit_date": "",
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
    return output


def build_detail(generated_at: str) -> pd.DataFrame:
    source = source_rows()
    rows: list[dict[str, Any]] = []
    for _, row in source.iterrows():
        for rule in STOP_RULES:
            rows.append(evaluate_row(row, rule, generated_at))
    return pd.DataFrame(rows, columns=DETAIL_COLUMNS)


def numeric_series(df: pd.DataFrame, column: str) -> pd.Series:
    return pd.to_numeric(df[column], errors="coerce")


def summarize_group(group: pd.DataFrame, generated_at: str) -> dict[str, Any]:
    evaluated = group[group["outcome_result"].isin(["win", "neutral", "loss"])].copy()
    mature = evaluated[evaluated["outcome_result"].isin(["win", "loss"])].copy()
    returns = numeric_series(evaluated, "return_pct").dropna()
    loss_returns = numeric_series(evaluated[evaluated["outcome_result"].eq("loss")], "return_pct").dropna()

    win_count = int(evaluated["outcome_result"].eq("win").sum())
    neutral_count = int(evaluated["outcome_result"].eq("neutral").sum())
    loss_count = int(evaluated["outcome_result"].eq("loss").sum())
    evaluated_count = win_count + neutral_count + loss_count
    mature_count = win_count + loss_count
    positive_count = int(numeric_series(evaluated, "return_pct").gt(0).sum())

    first = group.iloc[0]
    return {
        "model_id": MODEL_ID,
        "research_id": RESEARCH_ID,
        "source_research_id": SOURCE_RESEARCH_ID,
        "research_variant_id": RESEARCH_VARIANT_ID,
        "parameter_set_id": PARAMETER_SET_ID,
        "advisory_status": RESEARCH_VARIANT_ID,
        "production_readiness": PRODUCTION_READINESS,
        "approved_for_daily": "false",
        "surface_id": SURFACE_ID,
        "event_set_id": EVENT_SET_ID,
        "entry_rule_id": ENTRY_RULE_ID,
        "source_outcome_rule_id": SOURCE_OUTCOME_RULE_ID,
        "segment_id": safe_str(first.get("segment_id")),
        "segment_description": safe_str(first.get("segment_description")),
        "stop_rule_id": safe_str(first.get("stop_rule_id")),
        "stop_rule_description": safe_str(first.get("stop_rule_description")),
        "stop_basis": safe_str(first.get("stop_basis")),
        "stop_buffer_pct": safe_str(first.get("stop_buffer_pct")),
        "sample_size": len(group),
        "evaluated_sample_size": evaluated_count,
        "mature_sample_size": mature_count,
        "win_count": win_count,
        "neutral_count": neutral_count,
        "loss_count": loss_count,
        "incomplete_count": int(group["outcome_result"].eq("incomplete").sum()),
        "stop_hit_count": int(group["stop_hit"].eq("true").sum()),
        "pure_win_rate_pct": metric_text(win_count / mature_count * 100.0 if mature_count else math.nan),
        "neutral_inclusive_success_rate_pct": metric_text(
            (win_count + neutral_count) / evaluated_count * 100.0 if evaluated_count else math.nan
        ),
        "positive_return_rate_pct": metric_text(positive_count / evaluated_count * 100.0 if evaluated_count else math.nan),
        "avg_return_pct": metric_text(float(returns.mean()) if len(returns) else math.nan),
        "median_return_pct": metric_text(float(returns.median()) if len(returns) else math.nan),
        "min_return_pct": metric_text(float(returns.min()) if len(returns) else math.nan),
        "loss_avg_return_pct": metric_text(float(loss_returns.mean()) if len(loss_returns) else math.nan),
        "baseline_stop_rule_id": "no_fixed_stop_d40_v1",
        "baseline_pure_win_rate_pct": "",
        "baseline_neutral_inclusive_success_rate_pct": "",
        "baseline_avg_return_pct": "",
        "baseline_min_return_pct": "",
        "delta_pure_win_rate_pct": "",
        "delta_neutral_inclusive_success_rate_pct": "",
        "delta_avg_return_pct": "",
        "min_return_improvement_pct": "",
        "recommendation_status": "pending_baseline_comparison",
        "interpretation": "",
        "generated_at": generated_at,
    }


def add_baseline_comparison(summary: pd.DataFrame) -> pd.DataFrame:
    out = summary.copy()
    baseline_by_segment = {
        row["segment_id"]: row
        for _, row in out[out["stop_rule_id"].eq("no_fixed_stop_d40_v1")].iterrows()
    }
    for idx, row in out.iterrows():
        baseline = baseline_by_segment.get(row["segment_id"])
        if baseline is None:
            continue
        for column in [
            "pure_win_rate_pct",
            "neutral_inclusive_success_rate_pct",
            "avg_return_pct",
            "min_return_pct",
        ]:
            out.at[idx, f"baseline_{column}"] = baseline[column]

        pure_delta = safe_float(row["pure_win_rate_pct"]) - safe_float(baseline["pure_win_rate_pct"])
        inclusive_delta = safe_float(row["neutral_inclusive_success_rate_pct"]) - safe_float(
            baseline["neutral_inclusive_success_rate_pct"]
        )
        avg_delta = safe_float(row["avg_return_pct"]) - safe_float(baseline["avg_return_pct"])
        min_improvement = safe_float(row["min_return_pct"]) - safe_float(baseline["min_return_pct"])
        out.at[idx, "delta_pure_win_rate_pct"] = metric_text(pure_delta)
        out.at[idx, "delta_neutral_inclusive_success_rate_pct"] = metric_text(inclusive_delta)
        out.at[idx, "delta_avg_return_pct"] = metric_text(avg_delta)
        out.at[idx, "min_return_improvement_pct"] = metric_text(min_improvement)

        if row["stop_rule_id"] == "no_fixed_stop_d40_v1":
            out.at[idx, "recommendation_status"] = "current_v1_baseline"
            out.at[idx, "interpretation"] = "Current approved operation v1; no fixed structure stop."
        elif row["segment_id"] == SELECTED_SEGMENT_ID and row["stop_rule_id"] == "w_structure_low_close_stop_d40":
            out.at[idx, "recommendation_status"] = "risk_repair_candidate_tradeoff_review"
            out.at[idx, "interpretation"] = (
                "Structure-low stop improves average return and left-tail loss, but lowers pure win rate; "
                "requires explicit promotion decision before production sync."
            )
        elif row["segment_id"] == SELECTED_SEGMENT_ID and row["stop_rule_id"] == "w_structure_low_stop_d20_gain10_else_d40":
            out.at[idx, "recommendation_status"] = "preferred_v2_candidate_tradeoff_review"
            out.at[idx, "interpretation"] = (
                "Hybrid D+20/D+40 exit captures fast W-bottom rebounds while retaining the W-structure stop; "
                "requires explicit promotion decision before production sync."
            )
        elif avg_delta > 0 and min_improvement > 0:
            out.at[idx, "recommendation_status"] = "risk_repair_candidate_research_only"
            out.at[idx, "interpretation"] = "Stop rule improves average return and left-tail loss in this segment."
        else:
            out.at[idx, "recommendation_status"] = "not_preferred_in_current_grid"
            out.at[idx, "interpretation"] = "Stop rule does not improve both average return and left-tail loss."
    return out


def build_summary(detail: pd.DataFrame, generated_at: str) -> pd.DataFrame:
    rows: list[dict[str, Any]] = []
    group_cols = ["segment_id", "stop_rule_id"]
    for _, group in detail.groupby(group_cols, dropna=False):
        rows.append(summarize_group(group, generated_at))
    summary = pd.DataFrame(rows, columns=SUMMARY_COLUMNS)
    summary = add_baseline_comparison(summary)
    order = {rule["stop_rule_id"]: idx for idx, rule in enumerate(STOP_RULES)}
    summary["_segment_order"] = summary["segment_id"].map({segment: idx for idx, segment in enumerate(TARGET_SEGMENT_IDS)})
    summary["_stop_order"] = summary["stop_rule_id"].map(order)
    summary = summary.sort_values(["_segment_order", "_stop_order"]).drop(columns=["_segment_order", "_stop_order"])
    return summary[SUMMARY_COLUMNS].reset_index(drop=True)


def markdown_table(df: pd.DataFrame, columns: list[str], limit: int = 50) -> list[str]:
    if df.empty:
        return ["(no rows)"]
    view = df.loc[:, columns].head(limit).copy()
    widths = {column: max(len(column), *(len(safe_str(value)) for value in view[column])) for column in columns}
    lines = [
        "| " + " | ".join(column.ljust(widths[column]) for column in columns) + " |",
        "| " + " | ".join("-" * widths[column] for column in columns) + " |",
    ]
    for _, row in view.iterrows():
        lines.append("| " + " | ".join(safe_str(row[column]).ljust(widths[column]) for column in columns) + " |")
    return lines


def write_markdown(summary: pd.DataFrame, detail: pd.DataFrame) -> None:
    selected = summary[summary["segment_id"].eq(SELECTED_SEGMENT_ID)].copy()
    candidate = selected[selected["stop_rule_id"].eq("w_structure_low_stop_d20_gain10_else_d40")].copy()
    structure = selected[selected["stop_rule_id"].eq("w_structure_low_close_stop_d40")].copy()
    baseline = selected[selected["stop_rule_id"].eq("no_fixed_stop_d40_v1")].copy()
    lines = [
        "# W-bottom Early Entry Stop-loss Audit",
        "",
        "- production impact: `none`",
        f"- model_id: `{MODEL_ID}`",
        f"- selected segment: `{SELECTED_SEGMENT_ID}`",
        f"- entry rule: `{ENTRY_RULE_ID}`",
        f"- source outcome rule: `{SOURCE_OUTCOME_RULE_ID}`",
        "- stop-loss candidates: no stop, right-low close stop, W-structure-low close stop, W-structure-low stop with D+20 gain exit, W-structure-low close stop with 1% buffer.",
        "- price convention: entry uses next trading day's open; stop/target/neutral/expiry exits use close.",
        "",
        "## Selected Segment Comparison",
        "",
        *markdown_table(
            selected,
            [
                "stop_rule_id",
                "evaluated_sample_size",
                "win_count",
                "neutral_count",
                "loss_count",
                "stop_hit_count",
                "pure_win_rate_pct",
                "neutral_inclusive_success_rate_pct",
                "avg_return_pct",
                "median_return_pct",
                "min_return_pct",
                "delta_pure_win_rate_pct",
                "delta_avg_return_pct",
                "min_return_improvement_pct",
                "recommendation_status",
            ],
            limit=20,
        ),
        "",
        "## Interpretation",
        "",
    ]
    if not baseline.empty and not candidate.empty:
        b = baseline.iloc[0]
        c = candidate.iloc[0]
        lines.extend(
            [
                (
                    f"- Baseline `no_fixed_stop_d40_v1`: pure win `{b['pure_win_rate_pct']}%`, "
                    f"inclusive success `{b['neutral_inclusive_success_rate_pct']}%`, avg return `{b['avg_return_pct']}%`, "
                    f"min return `{b['min_return_pct']}%`."
                ),
                (
                    f"- Candidate `w_structure_low_stop_d20_gain10_else_d40`: positive-return rate `{c['pure_win_rate_pct']}%`, "
                    f"inclusive success `{c['neutral_inclusive_success_rate_pct']}%`, avg return `{c['avg_return_pct']}%`, "
                    f"min return `{c['min_return_pct']}%`."
                ),
                (
                    "- The hybrid D+20/D+40 rule repairs left-tail risk, avoids early +10% profit truncation, and improves average return. "
                    "It must not be promoted silently as production v2 without an explicit model-change PR."
                ),
            ]
        )
    if not structure.empty:
        s = structure.iloc[0]
        lines.extend(
            [
                (
                    f"- Structure-stop with old +10%/+5% rule: pure win `{s['pure_win_rate_pct']}%`, "
                    f"avg return `{s['avg_return_pct']}%`, min return `{s['min_return_pct']}%`."
                ),
            ]
        )
    lines.extend(
        [
            "",
            "## All Segment Summary",
            "",
            *markdown_table(
                summary,
                [
                    "segment_id",
                    "stop_rule_id",
                    "evaluated_sample_size",
                    "pure_win_rate_pct",
                    "neutral_inclusive_success_rate_pct",
                    "avg_return_pct",
                    "min_return_pct",
                    "recommendation_status",
                ],
                limit=80,
            ),
            "",
        ]
    )
    LATEST_MD.write_text("\n".join(lines), encoding="utf-8")


def validate_no_forbidden_columns(df: pd.DataFrame, name: str) -> None:
    forbidden = sorted(set(df.columns) & FORBIDDEN_PRODUCTION_FIELDS)
    if forbidden:
        raise SystemExit(f"ERROR: {name} emitted production decision fields: {forbidden}")


def main() -> int:
    generated_at = now_text()
    detail = build_detail(generated_at)
    summary = build_summary(detail, generated_at)
    validate_no_forbidden_columns(detail, "detail")
    validate_no_forbidden_columns(summary, "summary")

    write_csv(detail, LATEST_DETAIL_CSV)
    write_csv(detail, HISTORY_DETAIL_CSV)
    write_csv(summary, LATEST_SUMMARY_CSV)
    write_csv(summary, HISTORY_SUMMARY_CSV)
    write_markdown(summary, detail)

    selected = summary[
        summary["segment_id"].eq(SELECTED_SEGMENT_ID)
        & summary["stop_rule_id"].eq("w_structure_low_stop_d20_gain10_else_d40")
    ].iloc[0]
    print(f"saved_detail={LATEST_DETAIL_CSV} rows={len(detail)}")
    print(f"saved_summary={LATEST_SUMMARY_CSV} rows={len(summary)}")
    print(
        "selected_hybrid_rule="
        f"pure_win={selected['pure_win_rate_pct']} "
        f"inclusive_success={selected['neutral_inclusive_success_rate_pct']} "
        f"avg_return={selected['avg_return_pct']} "
        f"min_return={selected['min_return_pct']}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
