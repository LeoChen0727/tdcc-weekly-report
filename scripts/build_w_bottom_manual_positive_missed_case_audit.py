from __future__ import annotations

from datetime import datetime
from pathlib import Path
from typing import Any
from zoneinfo import ZoneInfo
import math
import shutil

import pandas as pd

import build_w_bottom_tdcc_abc_backtest as w_bottom
from build_w_bottom_candidate_chart_review_packet import draw_chart, normalize_code, normalize_date, safe_float, safe_str


ROOT = Path(".")
PRICE_DIR = ROOT / "data" / "stock_price_history"
RESEARCH_LATEST_DIR = ROOT / "output" / "latest" / "research_backtest"
RESEARCH_HISTORY_DIR = ROOT / "output" / "history" / "research"

SOURCE_QUALITY_CSV = RESEARCH_LATEST_DIR / "w_bottom_candidate_quality_audit_latest.csv"
SOURCE_PATH_DETAIL_CSV = RESEARCH_LATEST_DIR / "w_bottom_path_quality_filter_audit_detail_latest.csv"
SOURCE_PRICE_LEVEL_DETAIL_CSV = RESEARCH_LATEST_DIR / "w_bottom_price_level_audit_detail_latest.csv"

CHART_ROOT = RESEARCH_LATEST_DIR / "w_bottom_manual_positive_missed_case_audit"
LATEST_CSV = RESEARCH_LATEST_DIR / "w_bottom_manual_positive_missed_case_audit_latest.csv"
LATEST_MD = RESEARCH_LATEST_DIR / "w_bottom_manual_positive_missed_case_audit_latest.md"
HISTORY_CSV = RESEARCH_HISTORY_DIR / "w_bottom_manual_positive_missed_case_audit.csv"

MODEL_ID = "w_bottom_right_side"
CONFIRMATION_MODEL_ID = "neckline_volume_breakout_confirmation"
RESEARCH_ID = "w_bottom_manual_positive_missed_case_audit"
SOURCE_RESEARCH_ID = "manual_user_positive_examples"
RESEARCH_VARIANT_ID = "warning_research_variant_only"
PARAMETER_SET_ID = "w_bottom_manual_positive_missed_case_audit_20260625"

FORBIDDEN_PRODUCTION_FIELDS = {
    "trade_decision",
    "action_rating",
    "entry_style",
    "position_sizing",
    "decision_score",
    "daily_candidate_decision",
    "buy_signal",
}

MANUAL_CASES: list[dict[str, str]] = [
    {
        "manual_case_id": "user_4916_20260319_20260515",
        "stock_id": "4916",
        "stock_name": "\u4e8b\u6b23\u79d1",
        "user_interval_start": "20260319",
        "user_interval_end": "20260515",
        "manual_pattern_type": "higher_right_low_w_base",
        "manual_left_peak_date": "20260319",
        "manual_left_low_date": "20260407",
        "manual_neckline_date": "20260422",
        "manual_right_low_date": "20260508",
        "manual_observation_date": "20260515",
        "manual_breakout_date": "20260520",
        "first_high_volume_follow_through_date": "20260520",
        "relaxed_history_probe_date": "20260515",
        "primary_blocker": "second_low_gap_above_standard_w_max",
        "secondary_blocker": "pattern_should_route_to_higher_right_low_variant",
        "manual_read": "User-positive higher-right-low W/base. The second low is materially higher than the first low, so treating it as a standard double-bottom by widening the second-low gate would mix two pattern families.",
    },
    {
        "manual_case_id": "user_8069_20260312_20260508",
        "stock_id": "8069",
        "stock_name": "\u5143\u592a",
        "user_interval_start": "20260312",
        "user_interval_end": "20260508",
        "manual_pattern_type": "standard_w_missed_by_history_gate",
        "manual_left_peak_date": "20260312",
        "manual_left_low_date": "20260331",
        "manual_neckline_date": "20260422",
        "manual_right_low_date": "20260504",
        "manual_observation_date": "20260508",
        "manual_breakout_date": "20260511",
        "first_high_volume_follow_through_date": "20260512",
        "relaxed_history_probe_date": "20260507",
        "primary_blocker": "insufficient_long_position_history",
        "secondary_blocker": "observation_day_rebound_above_current_max_and_auto_left_peak_start_differs",
        "manual_read": "User-positive standard-W-like case. The current detector rejects it before shape evaluation because the stock has fewer than 180 valid closes in the 252-day price-position history; 20260508 is also already late for the current observation rebound gate.",
    },
]

OUTPUT_COLUMNS = [
    "model_id",
    "confirmation_model_id",
    "research_id",
    "source_research_id",
    "research_variant_id",
    "parameter_set_id",
    "advisory_status",
    "manual_case_id",
    "stock_id",
    "stock_name",
    "user_interval_start",
    "user_interval_end",
    "manual_pattern_type",
    "manual_left_peak_date",
    "manual_left_peak_price",
    "manual_left_low_date",
    "manual_left_low_price",
    "manual_neckline_date",
    "manual_neckline_price",
    "manual_right_low_date",
    "manual_right_low_price",
    "manual_observation_date",
    "manual_observation_close",
    "manual_breakout_date",
    "manual_breakout_close",
    "manual_breakout_volume_ratio",
    "first_high_volume_follow_through_date",
    "first_high_volume_follow_through_close",
    "first_high_volume_follow_through_volume_ratio",
    "second_low_gap_pct",
    "observation_to_neckline_pct",
    "observation_rebound_from_right_low_pct",
    "breakout_to_neckline_pct",
    "manual_first_arc_avg_volume",
    "manual_second_arc_avg_volume",
    "manual_second_arc_volume_ratio",
    "manual_first_arc_red_candle_ratio_pct",
    "manual_second_arc_red_candle_ratio_pct",
    "manual_second_minus_first_red_candle_ratio_pct",
    "valid_close_count_at_observation",
    "long_position_min_days",
    "observation_price_position_vs_median_pct",
    "current_quality_candidate_rows",
    "current_path_quality_candidate_rows",
    "current_price_level_candidate_rows",
    "missed_current_outputs",
    "current_detection_status",
    "current_detection_context",
    "relaxed_history_probe_date",
    "relaxed_history_detection_status",
    "relaxed_history_detection_context",
    "primary_blocker",
    "secondary_blocker",
    "current_gate_notes",
    "manual_read",
    "chart_path",
    "chart_path_absolute",
    "manual_review_status",
    "approved_for_daily",
    "production_readiness",
    "generated_at",
]


def now_text() -> str:
    return datetime.now(ZoneInfo("Asia/Taipei")).strftime("%Y-%m-%d %H:%M:%S Asia/Taipei")


def pct(value: float) -> float | str:
    if math.isnan(value) or math.isinf(value):
        return ""
    return round(value, 4)


def bool_text(value: bool) -> str:
    return "true" if value else "false"


def write_csv(df: pd.DataFrame, path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(path, index=False, encoding="utf-8-sig")


def markdown_table(df: pd.DataFrame, columns: list[str], limit: int = 20) -> list[str]:
    view = df.loc[:, columns].head(limit).copy()
    if view.empty:
        return ["_No rows._"]
    lines = ["| " + " | ".join(columns) + " |", "| " + " | ".join(["---"] * len(columns)) + " |"]
    for _, row in view.iterrows():
        lines.append("| " + " | ".join(safe_str(row.get(column)) for column in columns) + " |")
    return lines


def load_price(stock_id: str) -> pd.DataFrame:
    path = PRICE_DIR / f"{normalize_code(stock_id)}.csv"
    if not path.exists():
        raise SystemExit(f"ERROR: missing price history: {path}")
    price = pd.read_csv(path, dtype=str, keep_default_na=False)
    required = {"date", "stock_id", "stock_name", "open", "high", "low", "close", "volume"}
    missing = sorted(required - set(price.columns))
    if missing:
        raise SystemExit(f"ERROR: {path} missing columns: {missing}")
    price = w_bottom.add_price_metrics(price)
    price = price.copy()
    price["date"] = price["date"].map(normalize_date)
    for column in ["open", "high", "low", "close", "volume", "volume_ma20", "volume_ratio"]:
        if column in price.columns:
            price[column] = pd.to_numeric(price[column], errors="coerce")
    return price[price["date"].ne("")].sort_values("date").reset_index(drop=True)


def price_row(price: pd.DataFrame, date: str) -> pd.Series:
    normalized = normalize_date(date)
    rows = price[price["date"].eq(normalized)]
    if rows.empty:
        raise SystemExit(f"ERROR: missing price row for {safe_str(price.iloc[0].get('stock_id'))} {normalized}")
    return rows.iloc[0]


def index_for_date(price: pd.DataFrame, date: str) -> int:
    normalized = normalize_date(date)
    matches = price.index[price["date"].eq(normalized)]
    if len(matches) == 0:
        raise SystemExit(f"ERROR: missing date in price history: {normalized}")
    return int(matches[0])


def average_volume(price: pd.DataFrame, start_date: str, end_date: str) -> float:
    start_idx = index_for_date(price, start_date)
    end_idx = index_for_date(price, end_date)
    if end_idx < start_idx:
        return math.nan
    values = pd.to_numeric(price.iloc[start_idx : end_idx + 1]["volume"], errors="coerce").dropna()
    return float(values.mean()) if not values.empty else math.nan


def red_candle_ratio(price: pd.DataFrame, start_date: str, end_date: str) -> float:
    start_idx = index_for_date(price, start_date)
    end_idx = index_for_date(price, end_date)
    if end_idx < start_idx:
        return math.nan
    window = price.iloc[start_idx : end_idx + 1].copy()
    opens = pd.to_numeric(window["open"], errors="coerce")
    closes = pd.to_numeric(window["close"], errors="coerce")
    valid = opens.notna() & closes.notna()
    if int(valid.sum()) == 0:
        return math.nan
    return float((closes[valid] > opens[valid]).mean() * 100.0)


def valid_close_stats_at(price: pd.DataFrame, date: str) -> tuple[int, float, float]:
    idx = index_for_date(price, date)
    history = price.iloc[: idx + 1].tail(w_bottom.LONG_POSITION_LOOKBACK_DAYS)
    closes = pd.to_numeric(history["close"], errors="coerce").dropna()
    close = safe_float(price.iloc[idx].get("close"))
    if closes.empty or math.isnan(close):
        return 0, math.nan, math.nan
    median = float(closes.median())
    position = (close / median - 1.0) * 100.0 if median > 0 else math.nan
    return int(len(closes)), median, position


def count_source_rows(source: Path, stock_id: str, start_date: str, end_date: str) -> int:
    if not source.exists():
        return 0
    data = pd.read_csv(source, dtype=str, keep_default_na=False)
    if "stock_id" not in data.columns or "signal_date" not in data.columns:
        return 0
    stock = data["stock_id"].map(normalize_code).eq(normalize_code(stock_id))
    signal_date = data["signal_date"].map(normalize_date)
    in_interval = signal_date.ge(normalize_date(start_date)) & signal_date.le(normalize_date(end_date))
    return int((stock & in_interval).sum())


def context_text(context: dict[str, Any] | None) -> str:
    if not context:
        return ""
    fields = [
        "left_peak_date",
        "left_low_date",
        "neckline_date",
        "right_low_date",
        "neckline_price",
        "right_low_value",
        "second_arc_volume_ratio",
        "first_rebound_days",
        "right_rebound_days_at_signal",
    ]
    return ";".join(f"{field}={safe_str(context.get(field))}" for field in fields if safe_str(context.get(field)) != "")


def detect_context(price: pd.DataFrame, date: str) -> dict[str, Any] | None:
    return w_bottom.detect_w_bottom_context_at(price, index_for_date(price, date))


def detect_context_without_history_gate(price: pd.DataFrame, date: str) -> dict[str, Any] | None:
    original = w_bottom.long_position_ok
    try:
        w_bottom.long_position_ok = lambda history, current_close: True
        return w_bottom.detect_w_bottom_context_at(price, index_for_date(price, date))
    finally:
        w_bottom.long_position_ok = original


def clean_chart_root() -> None:
    root_abs = CHART_ROOT.resolve()
    latest_abs = RESEARCH_LATEST_DIR.resolve()
    if latest_abs not in root_abs.parents:
        raise SystemExit(f"ERROR: refused to clear chart root outside research latest dir: {root_abs}")
    if CHART_ROOT.exists():
        shutil.rmtree(CHART_ROOT)
    CHART_ROOT.mkdir(parents=True, exist_ok=True)


def chart_filename(case: dict[str, str]) -> str:
    return f"{normalize_code(case['stock_id'])}_{normalize_date(case['user_interval_start'])}_{normalize_date(case['user_interval_end'])}.png"


def chart_row(case: dict[str, str], values: dict[str, Any]) -> pd.Series:
    return pd.Series(
        {
            "stock_id": case["stock_id"],
            "stock_name": values["stock_name"],
            "signal_date": case["manual_observation_date"],
            "left_peak_date": case["manual_left_peak_date"],
            "left_low_date": case["manual_left_low_date"],
            "neckline_date": case["manual_neckline_date"],
            "right_low_date": case["manual_right_low_date"],
            "signal_close": values["observation_close"],
            "neckline_price": values["neckline_price"],
            "right_low_value": values["right_low_price"],
            "signal_distance_to_neckline_pct": values["observation_to_neckline_pct"],
            "signal_rebound_from_right_low_pct": values["observation_rebound_from_right_low_pct"],
            "second_arc_volume_ratio": values["manual_second_arc_volume_ratio"],
            "primary_review_flag": "manual_positive_missed_case",
            "sym1_5_completion_date": case["manual_breakout_date"],
            "sym1_5_breakout_date": case["first_high_volume_follow_through_date"],
            "sym1_5_right_low_broken_date": "",
        }
    )


def build_case(case: dict[str, str], generated_at: str) -> dict[str, Any]:
    stock_id = normalize_code(case["stock_id"])
    price = load_price(stock_id)

    left_peak_price = safe_float(price_row(price, case["manual_left_peak_date"]).get("high"))
    left_low_price = safe_float(price_row(price, case["manual_left_low_date"]).get("low"))
    neckline_price = safe_float(price_row(price, case["manual_neckline_date"]).get("high"))
    right_low_price = safe_float(price_row(price, case["manual_right_low_date"]).get("low"))
    observation_row = price_row(price, case["manual_observation_date"])
    breakout_row = price_row(price, case["manual_breakout_date"])
    follow_row = price_row(price, case["first_high_volume_follow_through_date"])

    observation_close = safe_float(observation_row.get("close"))
    breakout_close = safe_float(breakout_row.get("close"))
    follow_close = safe_float(follow_row.get("close"))
    first_arc_volume = average_volume(price, case["manual_left_peak_date"], case["manual_neckline_date"])
    second_arc_volume = average_volume(price, case["manual_neckline_date"], case["manual_observation_date"])
    second_arc_ratio = second_arc_volume / first_arc_volume if first_arc_volume > 0 else math.nan
    first_red_ratio = red_candle_ratio(price, case["manual_left_peak_date"], case["manual_neckline_date"])
    second_red_ratio = red_candle_ratio(price, case["manual_neckline_date"], case["manual_observation_date"])
    red_ratio_delta = second_red_ratio - first_red_ratio if not math.isnan(second_red_ratio) and not math.isnan(first_red_ratio) else math.nan
    valid_close_count, _, median_position = valid_close_stats_at(price, case["manual_observation_date"])

    current_context = detect_context(price, case["manual_observation_date"])
    relaxed_context = detect_context_without_history_gate(price, case["relaxed_history_probe_date"])
    quality_rows = count_source_rows(SOURCE_QUALITY_CSV, stock_id, case["user_interval_start"], case["user_interval_end"])
    path_rows = count_source_rows(SOURCE_PATH_DETAIL_CSV, stock_id, case["user_interval_start"], case["user_interval_end"])
    price_level_rows = count_source_rows(SOURCE_PRICE_LEVEL_DETAIL_CSV, stock_id, case["user_interval_start"], case["user_interval_end"])

    values = {
        "stock_name": safe_str(case.get("stock_name")) or safe_str(observation_row.get("stock_name")),
        "observation_close": observation_close,
        "neckline_price": neckline_price,
        "right_low_price": right_low_price,
        "observation_to_neckline_pct": (observation_close / neckline_price - 1.0) * 100.0 if neckline_price > 0 else math.nan,
        "observation_rebound_from_right_low_pct": (observation_close / right_low_price - 1.0) * 100.0 if right_low_price > 0 else math.nan,
        "manual_second_arc_volume_ratio": second_arc_ratio,
    }
    chart_path = CHART_ROOT / chart_filename(case)
    draw_chart(chart_row(case, values), chart_path)

    current_status = "detected_by_current_model" if current_context else "missed_by_current_standard_w_detection"
    relaxed_status = "detected_if_history_gate_bypassed" if relaxed_context else "still_not_detected_if_history_gate_bypassed"

    return {
        "model_id": MODEL_ID,
        "confirmation_model_id": CONFIRMATION_MODEL_ID,
        "research_id": RESEARCH_ID,
        "source_research_id": SOURCE_RESEARCH_ID,
        "research_variant_id": RESEARCH_VARIANT_ID,
        "parameter_set_id": PARAMETER_SET_ID,
        "advisory_status": RESEARCH_VARIANT_ID,
        "manual_case_id": case["manual_case_id"],
        "stock_id": stock_id,
        "stock_name": values["stock_name"],
        "user_interval_start": normalize_date(case["user_interval_start"]),
        "user_interval_end": normalize_date(case["user_interval_end"]),
        "manual_pattern_type": case["manual_pattern_type"],
        "manual_left_peak_date": normalize_date(case["manual_left_peak_date"]),
        "manual_left_peak_price": pct(left_peak_price),
        "manual_left_low_date": normalize_date(case["manual_left_low_date"]),
        "manual_left_low_price": pct(left_low_price),
        "manual_neckline_date": normalize_date(case["manual_neckline_date"]),
        "manual_neckline_price": pct(neckline_price),
        "manual_right_low_date": normalize_date(case["manual_right_low_date"]),
        "manual_right_low_price": pct(right_low_price),
        "manual_observation_date": normalize_date(case["manual_observation_date"]),
        "manual_observation_close": pct(observation_close),
        "manual_breakout_date": normalize_date(case["manual_breakout_date"]),
        "manual_breakout_close": pct(breakout_close),
        "manual_breakout_volume_ratio": pct(safe_float(breakout_row.get("volume_ratio"))),
        "first_high_volume_follow_through_date": normalize_date(case["first_high_volume_follow_through_date"]),
        "first_high_volume_follow_through_close": pct(follow_close),
        "first_high_volume_follow_through_volume_ratio": pct(safe_float(follow_row.get("volume_ratio"))),
        "second_low_gap_pct": pct((right_low_price / left_low_price - 1.0) * 100.0 if left_low_price > 0 else math.nan),
        "observation_to_neckline_pct": pct(values["observation_to_neckline_pct"]),
        "observation_rebound_from_right_low_pct": pct(values["observation_rebound_from_right_low_pct"]),
        "breakout_to_neckline_pct": pct((breakout_close / neckline_price - 1.0) * 100.0 if neckline_price > 0 else math.nan),
        "manual_first_arc_avg_volume": pct(first_arc_volume),
        "manual_second_arc_avg_volume": pct(second_arc_volume),
        "manual_second_arc_volume_ratio": pct(second_arc_ratio),
        "manual_first_arc_red_candle_ratio_pct": pct(first_red_ratio),
        "manual_second_arc_red_candle_ratio_pct": pct(second_red_ratio),
        "manual_second_minus_first_red_candle_ratio_pct": pct(red_ratio_delta),
        "valid_close_count_at_observation": valid_close_count,
        "long_position_min_days": w_bottom.LONG_POSITION_MIN_DAYS,
        "observation_price_position_vs_median_pct": pct(median_position),
        "current_quality_candidate_rows": quality_rows,
        "current_path_quality_candidate_rows": path_rows,
        "current_price_level_candidate_rows": price_level_rows,
        "missed_current_outputs": bool_text(quality_rows == 0 and path_rows == 0 and price_level_rows == 0),
        "current_detection_status": current_status,
        "current_detection_context": context_text(current_context),
        "relaxed_history_probe_date": normalize_date(case["relaxed_history_probe_date"]),
        "relaxed_history_detection_status": relaxed_status,
        "relaxed_history_detection_context": context_text(relaxed_context),
        "primary_blocker": case["primary_blocker"],
        "secondary_blocker": case["secondary_blocker"],
        "current_gate_notes": (
            f"SECOND_LOW_GAP_MIN={w_bottom.SECOND_LOW_GAP_MIN};"
            f"SECOND_LOW_GAP_MAX={w_bottom.SECOND_LOW_GAP_MAX};"
            f"RIGHT_SIDE_REBOUND_MIN={w_bottom.RIGHT_SIDE_REBOUND_MIN};"
            f"RIGHT_SIDE_REBOUND_MAX={w_bottom.RIGHT_SIDE_REBOUND_MAX};"
            f"LONG_POSITION_MIN_DAYS={w_bottom.LONG_POSITION_MIN_DAYS}"
        ),
        "manual_read": case["manual_read"],
        "chart_path": chart_path.as_posix(),
        "chart_path_absolute": str(chart_path.resolve()),
        "manual_review_status": "pending_user_model_review",
        "approved_for_daily": "false",
        "production_readiness": "not_production_ready_research_only",
        "generated_at": generated_at,
    }


def write_markdown(audit: pd.DataFrame, generated_at: str) -> None:
    lines = [
        "# W-Bottom Manual Positive Missed-Case Audit",
        "",
        f"- generated_at: `{generated_at}`",
        f"- model_id: `{MODEL_ID}`",
        f"- confirmation_model_id: `{CONFIRMATION_MODEL_ID}`",
        f"- research_id: `{RESEARCH_ID}`",
        f"- source_research_id: `{SOURCE_RESEARCH_ID}`",
        f"- rows: `{len(audit)}`",
        f"- advisory_status: `{RESEARCH_VARIANT_ID}`",
        "- production impact: `none`; this audit does not update production model conditions, scoring, ranking, or baseline.",
        "- interpretation boundary: manual positive examples are research evidence only and require a separate model-change or promotion PR before production use.",
        "",
        "## Missed-Case Summary",
        "",
        *markdown_table(
            audit,
            [
                "stock_id",
                "stock_name",
                "manual_pattern_type",
                "user_interval_start",
                "user_interval_end",
                "second_low_gap_pct",
                "observation_rebound_from_right_low_pct",
                "valid_close_count_at_observation",
                "primary_blocker",
                "relaxed_history_detection_status",
            ],
        ),
        "",
        "## Human-Review Interpretation",
        "",
        "- `4916` is a higher-right-low W/base candidate: it is user-positive, but it is not the same family as the current standard W gate because the right low is far above the left low.",
        "- `8069` is closer to a standard W: the current code misses it mainly because the 180-valid-close price-position history gate fails before shape evaluation.",
        "- Both cases also show that left-start selection needs a separate audit: the algorithm can pick the highest available pre-low peak, while the human visual anchor may use a nearer local pressure high.",
        "- This file is meant to preserve those positive missed examples for research/backtest iteration, not to approve production changes.",
        "",
        "## Chart Files",
        "",
        *markdown_table(audit, ["stock_id", "manual_case_id", "chart_path"], limit=10),
    ]
    LATEST_MD.parent.mkdir(parents=True, exist_ok=True)
    LATEST_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    generated_at = now_text()
    clean_chart_root()
    rows = [build_case(case, generated_at) for case in MANUAL_CASES]
    audit = pd.DataFrame(rows, columns=OUTPUT_COLUMNS)
    forbidden = sorted(set(audit.columns) & FORBIDDEN_PRODUCTION_FIELDS)
    if forbidden:
        raise SystemExit(f"ERROR: manual positive audit emitted forbidden production fields: {forbidden}")
    write_csv(audit, LATEST_CSV)
    write_csv(audit, HISTORY_CSV)
    write_markdown(audit, generated_at)
    print(f"Saved: {LATEST_CSV} rows={len(audit)}")
    print(f"Saved: {HISTORY_CSV} rows={len(audit)}")
    print(f"Saved: {LATEST_MD}")
    print(f"Saved charts: {CHART_ROOT}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
