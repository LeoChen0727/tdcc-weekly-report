from __future__ import annotations

from datetime import datetime
from pathlib import Path
from typing import Any
from zoneinfo import ZoneInfo
import math

import pandas as pd

import build_w_bottom_left_anchor_pattern_family_audit as anchor_audit
import build_w_bottom_tdcc_abc_backtest as w_bottom
from build_w_bottom_candidate_chart_review_packet import normalize_code, normalize_date, safe_float, safe_str


ROOT = Path(".")
RESEARCH_LATEST_DIR = ROOT / "output" / "latest" / "research_backtest"
RESEARCH_HISTORY_DIR = ROOT / "output" / "history" / "research"

SOURCE_ANCHOR_DETAIL_CSV = RESEARCH_LATEST_DIR / "w_bottom_left_anchor_pattern_family_audit_detail_latest.csv"
LATEST_DETAIL_CSV = RESEARCH_LATEST_DIR / "w_bottom_left_anchor_rule_grid_detail_latest.csv"
LATEST_SUMMARY_CSV = RESEARCH_LATEST_DIR / "w_bottom_left_anchor_rule_grid_latest.csv"
LATEST_MD = RESEARCH_LATEST_DIR / "w_bottom_left_anchor_rule_grid_latest.md"
HISTORY_DETAIL_CSV = RESEARCH_HISTORY_DIR / "w_bottom_left_anchor_rule_grid_detail.csv"
HISTORY_SUMMARY_CSV = RESEARCH_HISTORY_DIR / "w_bottom_left_anchor_rule_grid.csv"

MODEL_ID = "w_bottom_right_side"
CONFIRMATION_MODEL_ID = "neckline_volume_breakout_confirmation"
RESEARCH_ID = "w_bottom_left_anchor_rule_grid"
SOURCE_RESEARCH_ID = "w_bottom_left_anchor_pattern_family_audit"
RESEARCH_VARIANT_ID = "warning_research_variant_only"
PARAMETER_SET_ID = "w_bottom_left_anchor_rule_grid_20260625"

STANDARD_W_FAMILY = "standard_double_bottom_w"
MIN_LEFT_DROP_PCT = 8.0
MIN_LEFT_DESCENT_DAYS = 8
MICRO_PRESSURE_MIN_DROP_PCT = 15.0
MICRO_PEAK_RADIUS = 1
MAX_HUMAN_MATCH_DAYS = 2

RULE_SPECS = [
    {
        "rule_id": "current_detector_left_peak",
        "window_days": 45,
        "selector_method": "current_detector_output",
        "description": "Use the left peak already selected by the current research detector.",
    },
    {
        "rule_id": "highest_high_45d_before_left_low",
        "window_days": 45,
        "selector_method": "highest_high_before_left_low",
        "description": "Choose the highest high in the 45 trading days before the first low.",
    },
    {
        "rule_id": "highest_high_90d_before_left_low",
        "window_days": 90,
        "selector_method": "highest_high_before_left_low",
        "description": "Choose the highest high in the 90 trading days before the first low.",
    },
    {
        "rule_id": "nearest_micro_pressure_45d_min15_before_left_low",
        "window_days": 45,
        "selector_method": "nearest_micro_pressure_before_left_low",
        "description": "Choose the nearest micro-turn pressure high in the 45 trading days before the first low with at least a 15% drop and an 8-trading-day left leg into the first low.",
    },
    {
        "rule_id": "nearest_micro_pressure_90d_min15_before_left_low",
        "window_days": 90,
        "selector_method": "nearest_micro_pressure_before_left_low",
        "description": "Choose the nearest micro-turn pressure high in the 90 trading days before the first low with at least a 15% drop and an 8-trading-day left leg into the first low.",
    },
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

DETAIL_COLUMNS = [
    "model_id",
    "confirmation_model_id",
    "research_id",
    "source_research_id",
    "research_variant_id",
    "parameter_set_id",
    "advisory_status",
    "source_audit_scope",
    "case_review_tag",
    "manual_case_id",
    "stock_id",
    "stock_name",
    "signal_date",
    "source_pattern_family",
    "rule_id",
    "rule_window_days",
    "selector_method",
    "baseline_current_left_peak_date",
    "human_left_peak_date",
    "left_low_date",
    "neckline_date",
    "right_low_date",
    "candidate_left_peak_date",
    "candidate_left_peak_price",
    "candidate_days_before_left_low",
    "candidate_drop_to_left_low_pct",
    "candidate_left_descent_wrong_direction_rate_pct",
    "candidate_anchor_delta_vs_current_days",
    "candidate_anchor_delta_vs_human_days",
    "candidate_matches_current_left_peak",
    "candidate_matches_human_left_peak",
    "candidate_anchor_changed_from_current",
    "candidate_inside_current_45d_window",
    "candidate_selection_status",
    "candidate_selection_reason",
    "transition_status",
    "slope_curvature_category",
    "price_level_bucket",
    "anchor_issue_type",
    "recommended_next_research_action",
    "manual_review_status",
    "approved_for_daily",
    "production_readiness",
    "generated_at",
]

SUMMARY_COLUMNS = [
    "model_id",
    "confirmation_model_id",
    "research_id",
    "research_variant_id",
    "parameter_set_id",
    "advisory_status",
    "rule_id",
    "rule_window_days",
    "selector_method",
    "row_count",
    "selected_count",
    "selection_rate_pct",
    "anchor_changed_count",
    "anchor_changed_rate_pct",
    "human_match_count",
    "human_match_rate_pct",
    "avg_candidate_days_before_left_low",
    "median_candidate_days_before_left_low",
    "avg_drop_to_left_low_pct",
    "median_drop_to_left_low_pct",
    "avg_left_descent_wrong_direction_rate_pct",
    "median_left_descent_wrong_direction_rate_pct",
    "inside_current_45d_window_count",
    "manual_positive_rows",
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


def read_csv(path: Path) -> pd.DataFrame:
    if not path.exists():
        raise SystemExit(f"ERROR: missing required input: {path}")
    return pd.read_csv(path, dtype=str, keep_default_na=False)


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


def index_for_date(price: pd.DataFrame, date: str) -> int | None:
    return anchor_audit.index_for_date(price, date)


def trading_day_delta(price: pd.DataFrame, start_date: str, end_date: str) -> int | str:
    return anchor_audit.trading_day_delta(price, start_date, end_date)


def load_source() -> pd.DataFrame:
    source = read_csv(SOURCE_ANCHOR_DETAIL_CSV)
    required = {
        "audit_scope",
        "stock_id",
        "stock_name",
        "signal_date",
        "computed_pattern_family",
        "auto_left_peak_date",
        "auto_left_low_date",
        "auto_neckline_date",
        "auto_right_low_date",
        "human_left_peak_date",
        "case_review_tag",
        "manual_case_id",
    }
    missing = sorted(required - set(source.columns))
    if missing:
        raise SystemExit(f"ERROR: source anchor detail missing columns: {missing}")
    source = source.copy()
    source["stock_id"] = source["stock_id"].map(normalize_code)
    for column in [
        "signal_date",
        "auto_left_peak_date",
        "auto_left_low_date",
        "auto_neckline_date",
        "auto_right_low_date",
        "human_left_peak_date",
    ]:
        source[column] = source[column].map(normalize_date)
    standard = source[source["computed_pattern_family"].eq(STANDARD_W_FAMILY)].copy()
    if standard.empty:
        raise SystemExit("ERROR: no standard W rows available for left-anchor rule grid")
    return standard.reset_index(drop=True)


def local_peak_indexes(price: pd.DataFrame) -> set[int]:
    highs = [safe_float(value) for value in price["high"].tolist()]
    lows = [safe_float(value) for value in price["low"].tolist()]
    peaks, _ = w_bottom.local_peaks_troughs(highs, lows)
    return set(peaks)


def window_bounds(left_low_idx: int, window_days: int) -> tuple[int, int]:
    start = max(0, left_low_idx - window_days)
    end = left_low_idx - 2
    return start, end


def highest_high_before_left_low(price: pd.DataFrame, left_low_idx: int, window_days: int) -> tuple[int | None, str]:
    start, end = window_bounds(left_low_idx, window_days)
    if end <= start:
        return None, "insufficient_pre_left_low_window"
    window = price.iloc[start:end].copy()
    highs = pd.to_numeric(window["high"], errors="coerce")
    if highs.dropna().empty:
        return None, "no_valid_high_in_window"
    return int(highs.idxmax()), f"selected_highest_high_in_{window_days}d_window"


def nearest_valid_pressure_before_left_low(price: pd.DataFrame, left_low_idx: int, window_days: int) -> tuple[int | None, str]:
    left_low = safe_float(price.iloc[left_low_idx].get("low"))
    if left_low <= 0 or math.isnan(left_low):
        return None, "invalid_left_low_price"
    start, end = window_bounds(left_low_idx, window_days)
    if end <= start:
        return None, "insufficient_pre_left_low_window"
    peak_indexes = local_peak_indexes(price)
    min_idx = start
    max_idx = min(end, left_low_idx - MIN_LEFT_DESCENT_DAYS)
    if max_idx < min_idx:
        return None, f"no_room_for_min_{MIN_LEFT_DESCENT_DAYS}d_left_leg"
    candidates = [
        idx
        for idx in sorted(peak_indexes)
        if min_idx <= idx <= max_idx and (safe_float(price.iloc[idx].get("high")) / left_low - 1.0) * 100.0 >= MIN_LEFT_DROP_PCT
    ]
    if candidates:
        return max(candidates), f"selected_nearest_local_peak_with_min_{MIN_LEFT_DROP_PCT:g}pct_drop_and_min_{MIN_LEFT_DESCENT_DAYS}d_left_leg"

    fallback = price.iloc[min_idx : max_idx + 1].copy()
    highs = pd.to_numeric(fallback["high"], errors="coerce")
    eligible = fallback[highs.ge(left_low * (1.0 + MIN_LEFT_DROP_PCT / 100.0))].copy()
    if eligible.empty:
        return None, f"no_pressure_high_with_min_{MIN_LEFT_DROP_PCT:g}pct_drop_and_min_{MIN_LEFT_DESCENT_DAYS}d_left_leg"
    return int(eligible.index.max()), f"selected_nearest_high_with_min_{MIN_LEFT_DROP_PCT:g}pct_drop_and_min_{MIN_LEFT_DESCENT_DAYS}d_left_leg_fallback"


def is_micro_peak(price: pd.DataFrame, idx: int) -> bool:
    high = safe_float(price.iloc[idx].get("high"))
    if math.isnan(high):
        return False
    start = max(0, idx - MICRO_PEAK_RADIUS)
    end = min(len(price), idx + MICRO_PEAK_RADIUS + 1)
    local_highs = [safe_float(value) for value in price.iloc[start:end]["high"].tolist()]
    local_highs = [value for value in local_highs if not math.isnan(value)]
    return bool(local_highs) and high >= max(local_highs) * 0.998


def nearest_micro_pressure_before_left_low(price: pd.DataFrame, left_low_idx: int, window_days: int) -> tuple[int | None, str]:
    left_low = safe_float(price.iloc[left_low_idx].get("low"))
    if left_low <= 0 or math.isnan(left_low):
        return None, "invalid_left_low_price"
    start, end = window_bounds(left_low_idx, window_days)
    min_idx = start
    max_idx = min(end, left_low_idx - MIN_LEFT_DESCENT_DAYS)
    if max_idx < min_idx:
        return None, f"no_room_for_min_{MIN_LEFT_DESCENT_DAYS}d_left_leg"
    candidates = [
        idx
        for idx in range(min_idx, max_idx + 1)
        if is_micro_peak(price, idx)
        and (safe_float(price.iloc[idx].get("high")) / left_low - 1.0) * 100.0 >= MICRO_PRESSURE_MIN_DROP_PCT
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


def select_candidate(price: pd.DataFrame, source_row: pd.Series, spec: dict[str, Any]) -> tuple[int | None, str]:
    left_low_idx = index_for_date(price, source_row.get("auto_left_low_date"))
    if left_low_idx is None:
        return None, "missing_left_low_date_in_price_history"
    selector = spec["selector_method"]
    if selector == "current_detector_output":
        idx = index_for_date(price, source_row.get("auto_left_peak_date"))
        return idx, "selected_current_detector_left_peak" if idx is not None else "current_detector_left_peak_missing"
    if selector == "highest_high_before_left_low":
        return highest_high_before_left_low(price, left_low_idx, int(spec["window_days"]))
    if selector == "nearest_valid_pressure_before_left_low":
        return nearest_valid_pressure_before_left_low(price, left_low_idx, int(spec["window_days"]))
    if selector == "nearest_micro_pressure_before_left_low":
        return nearest_micro_pressure_before_left_low(price, left_low_idx, int(spec["window_days"]))
    raise SystemExit(f"ERROR: unknown selector method: {selector}")


def descent_wrong_direction_rate(price: pd.DataFrame, peak_idx: int, low_idx: int) -> float:
    if low_idx <= peak_idx:
        return math.nan
    closes = pd.to_numeric(price.iloc[peak_idx : low_idx + 1]["close"], errors="coerce").dropna().tolist()
    if len(closes) < 2:
        return math.nan
    wrong = 0
    total = 0
    for prev, current in zip(closes, closes[1:]):
        total += 1
        if current > prev:
            wrong += 1
    return wrong / total * 100.0 if total else math.nan


def detail_for_rule(source_row: pd.Series, spec: dict[str, Any], generated_at: str, price: pd.DataFrame | None = None) -> dict[str, Any]:
    stock_id = normalize_code(source_row.get("stock_id"))
    if price is None:
        price = anchor_audit.load_price(stock_id)
    left_low_idx = index_for_date(price, source_row.get("auto_left_low_date"))
    candidate_idx, reason = select_candidate(price, source_row, spec)

    selected = candidate_idx is not None and left_low_idx is not None
    candidate_date = ""
    candidate_price = math.nan
    days_before_low: int | str = ""
    drop_pct = math.nan
    wrong_direction_rate = math.nan
    delta_current: int | str = ""
    delta_human: int | str = ""
    matches_current = False
    matches_human = False
    changed_from_current = False
    inside_45d = False

    current_left_peak_date = normalize_date(source_row.get("auto_left_peak_date"))
    human_left_peak_date = normalize_date(source_row.get("human_left_peak_date"))
    left_low_date = normalize_date(source_row.get("auto_left_low_date"))

    if selected:
        candidate_date = normalize_date(price.iloc[candidate_idx].get("date"))
        candidate_price = safe_float(price.iloc[candidate_idx].get("high"))
        left_low_price = safe_float(price.iloc[left_low_idx].get("low"))
        days_before_low = left_low_idx - candidate_idx
        drop_pct = (left_low_price / candidate_price - 1.0) * 100.0 if candidate_price > 0 else math.nan
        wrong_direction_rate = descent_wrong_direction_rate(price, candidate_idx, left_low_idx)
        delta_current = trading_day_delta(price, current_left_peak_date, candidate_date)
        if human_left_peak_date:
            delta_human = trading_day_delta(price, human_left_peak_date, candidate_date)
            matches_human = isinstance(delta_human, int) and abs(delta_human) <= MAX_HUMAN_MATCH_DAYS
        matches_current = candidate_date == current_left_peak_date
        changed_from_current = bool(current_left_peak_date and candidate_date != current_left_peak_date)
        inside_45d = isinstance(days_before_low, int) and days_before_low <= 45

    return {
        "model_id": MODEL_ID,
        "confirmation_model_id": CONFIRMATION_MODEL_ID,
        "research_id": RESEARCH_ID,
        "source_research_id": SOURCE_RESEARCH_ID,
        "research_variant_id": RESEARCH_VARIANT_ID,
        "parameter_set_id": PARAMETER_SET_ID,
        "advisory_status": RESEARCH_VARIANT_ID,
        "source_audit_scope": safe_str(source_row.get("audit_scope")),
        "case_review_tag": safe_str(source_row.get("case_review_tag")),
        "manual_case_id": safe_str(source_row.get("manual_case_id")),
        "stock_id": stock_id,
        "stock_name": safe_str(source_row.get("stock_name")),
        "signal_date": normalize_date(source_row.get("signal_date")),
        "source_pattern_family": safe_str(source_row.get("computed_pattern_family")),
        "rule_id": safe_str(spec["rule_id"]),
        "rule_window_days": int(spec["window_days"]),
        "selector_method": safe_str(spec["selector_method"]),
        "baseline_current_left_peak_date": current_left_peak_date,
        "human_left_peak_date": human_left_peak_date,
        "left_low_date": left_low_date,
        "neckline_date": normalize_date(source_row.get("auto_neckline_date")),
        "right_low_date": normalize_date(source_row.get("auto_right_low_date")),
        "candidate_left_peak_date": candidate_date,
        "candidate_left_peak_price": pct(candidate_price),
        "candidate_days_before_left_low": days_before_low,
        "candidate_drop_to_left_low_pct": pct(drop_pct),
        "candidate_left_descent_wrong_direction_rate_pct": pct(wrong_direction_rate),
        "candidate_anchor_delta_vs_current_days": delta_current,
        "candidate_anchor_delta_vs_human_days": delta_human,
        "candidate_matches_current_left_peak": bool_text(matches_current),
        "candidate_matches_human_left_peak": bool_text(matches_human),
        "candidate_anchor_changed_from_current": bool_text(changed_from_current),
        "candidate_inside_current_45d_window": bool_text(inside_45d),
        "candidate_selection_status": "selected" if selected else "not_selected",
        "candidate_selection_reason": reason,
        "transition_status": safe_str(source_row.get("transition_status")),
        "slope_curvature_category": safe_str(source_row.get("slope_curvature_category")),
        "price_level_bucket": safe_str(source_row.get("price_level_bucket")),
        "anchor_issue_type": safe_str(source_row.get("anchor_issue_type")),
        "recommended_next_research_action": safe_str(source_row.get("recommended_next_research_action")),
        "manual_review_status": "pending_research_review",
        "approved_for_daily": "false",
        "production_readiness": "not_production_ready_research_only",
        "generated_at": generated_at,
    }


def build_detail(source: pd.DataFrame, generated_at: str) -> pd.DataFrame:
    rows: list[dict[str, Any]] = []
    for _, source_row in source.iterrows():
        price = anchor_audit.load_price(normalize_code(source_row.get("stock_id")))
        for spec in RULE_SPECS:
            rows.append(detail_for_rule(source_row, spec, generated_at, price=price))
    detail = pd.DataFrame(rows, columns=DETAIL_COLUMNS)
    if detail.empty:
        raise SystemExit("ERROR: no left-anchor rule-grid detail rows generated")
    return detail


def summarize(detail: pd.DataFrame, generated_at: str) -> pd.DataFrame:
    rows: list[dict[str, Any]] = []
    for spec in RULE_SPECS:
        rule = detail[detail["rule_id"].eq(spec["rule_id"])].copy()
        if rule.empty:
            continue
        selected = rule[rule["candidate_selection_status"].eq("selected")].copy()
        row_count = len(rule)
        selected_count = len(selected)
        changed_count = int(selected["candidate_anchor_changed_from_current"].astype(str).str.lower().eq("true").sum())
        human_candidates = selected[selected["human_left_peak_date"].astype(str).ne("")].copy()
        human_match_count = int(human_candidates["candidate_matches_human_left_peak"].astype(str).str.lower().eq("true").sum())
        numeric_days = pd.to_numeric(selected["candidate_days_before_left_low"], errors="coerce")
        numeric_drop = pd.to_numeric(selected["candidate_drop_to_left_low_pct"], errors="coerce")
        numeric_wrong = pd.to_numeric(selected["candidate_left_descent_wrong_direction_rate_pct"], errors="coerce")
        rows.append(
            {
                "model_id": MODEL_ID,
                "confirmation_model_id": CONFIRMATION_MODEL_ID,
                "research_id": RESEARCH_ID,
                "research_variant_id": RESEARCH_VARIANT_ID,
                "parameter_set_id": PARAMETER_SET_ID,
                "advisory_status": RESEARCH_VARIANT_ID,
                "rule_id": spec["rule_id"],
                "rule_window_days": spec["window_days"],
                "selector_method": spec["selector_method"],
                "row_count": row_count,
                "selected_count": selected_count,
                "selection_rate_pct": pct(selected_count / row_count * 100.0 if row_count else math.nan),
                "anchor_changed_count": changed_count,
                "anchor_changed_rate_pct": pct(changed_count / selected_count * 100.0 if selected_count else math.nan),
                "human_match_count": human_match_count,
                "human_match_rate_pct": pct(human_match_count / len(human_candidates) * 100.0 if len(human_candidates) else math.nan),
                "avg_candidate_days_before_left_low": pct(float(numeric_days.mean())) if not numeric_days.dropna().empty else "",
                "median_candidate_days_before_left_low": pct(float(numeric_days.median())) if not numeric_days.dropna().empty else "",
                "avg_drop_to_left_low_pct": pct(float(numeric_drop.mean())) if not numeric_drop.dropna().empty else "",
                "median_drop_to_left_low_pct": pct(float(numeric_drop.median())) if not numeric_drop.dropna().empty else "",
                "avg_left_descent_wrong_direction_rate_pct": pct(float(numeric_wrong.mean())) if not numeric_wrong.dropna().empty else "",
                "median_left_descent_wrong_direction_rate_pct": pct(float(numeric_wrong.median())) if not numeric_wrong.dropna().empty else "",
                "inside_current_45d_window_count": int(selected["candidate_inside_current_45d_window"].astype(str).str.lower().eq("true").sum()),
                "manual_positive_rows": int(rule["source_audit_scope"].eq("manual_positive_missed_case").sum()),
                "production_readiness": "not_production_ready_research_only",
                "generated_at": generated_at,
            }
        )
    return pd.DataFrame(rows, columns=SUMMARY_COLUMNS)


def write_markdown(detail: pd.DataFrame, summary: pd.DataFrame, generated_at: str) -> None:
    key_cases = detail[detail["stock_id"].isin(["6415", "8069"])].copy()
    key_cases = key_cases.sort_values(["stock_id", "rule_id"])
    lines = [
        "# W-Bottom Left-Anchor Rule Grid",
        "",
        f"- generated_at: `{generated_at}`",
        f"- model_id: `{MODEL_ID}`",
        f"- confirmation_model_id: `{CONFIRMATION_MODEL_ID}`",
        f"- research_id: `{RESEARCH_ID}`",
        f"- source_research_id: `{SOURCE_RESEARCH_ID}`",
        f"- source_rows: `{detail[['stock_id', 'signal_date', 'source_audit_scope']].drop_duplicates().shape[0]}`",
        f"- detail_rows: `{len(detail)}`",
        f"- summary_rows: `{len(summary)}`",
        f"- advisory_status: `{RESEARCH_VARIANT_ID}`",
        "- production impact: `none`; this grid does not update production model conditions, scoring, ranking, or baseline.",
        "- interpretation boundary: this is a research-only comparison of left-anchor selection rules for standard-W candidates.",
        "",
        "## Rule Summary",
        "",
        *markdown_table(
            summary,
            [
                "rule_id",
                "selected_count",
                "anchor_changed_count",
                "human_match_count",
                "avg_candidate_days_before_left_low",
                "median_candidate_days_before_left_low",
                "avg_drop_to_left_low_pct",
                "avg_left_descent_wrong_direction_rate_pct",
            ],
        ),
        "",
        "## Key Cases",
        "",
        *markdown_table(
            key_cases,
            [
                "stock_id",
                "stock_name",
                "rule_id",
                "human_left_peak_date",
                "baseline_current_left_peak_date",
                "candidate_left_peak_date",
                "candidate_days_before_left_low",
                "candidate_drop_to_left_low_pct",
                "candidate_matches_human_left_peak",
                "candidate_selection_reason",
            ],
            limit=20,
        ),
        "",
        "## Reading Notes",
        "",
        "- `current_detector_left_peak` preserves the existing research detector output.",
        "- `highest_high_90d_before_left_low` exposes whether the current 45-day window truncates a much earlier, higher structural start.",
        f"- `nearest_micro_pressure_*` tests a human-like idea: prefer the nearest small-turn pressure high before the first low instead of the absolute highest high, while still requiring at least `{MICRO_PRESSURE_MIN_DROP_PCT}`% drop and `{MIN_LEFT_DESCENT_DAYS}` trading days for the left leg.",
        "- This grid compares anchor choices only. It does not prove a production model improvement and must not be promoted without a separate backtest/promotion PR.",
    ]
    LATEST_MD.parent.mkdir(parents=True, exist_ok=True)
    LATEST_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    generated_at = now_text()
    source = load_source()
    detail = build_detail(source, generated_at)
    forbidden = sorted(set(detail.columns) & FORBIDDEN_PRODUCTION_FIELDS)
    if forbidden:
        raise SystemExit(f"ERROR: left-anchor rule grid emitted forbidden production fields: {forbidden}")
    summary = summarize(detail, generated_at)
    write_csv(detail, LATEST_DETAIL_CSV)
    write_csv(detail, HISTORY_DETAIL_CSV)
    write_csv(summary, LATEST_SUMMARY_CSV)
    write_csv(summary, HISTORY_SUMMARY_CSV)
    write_markdown(detail, summary, generated_at)
    print(f"Saved: {LATEST_DETAIL_CSV} rows={len(detail)}")
    print(f"Saved: {LATEST_SUMMARY_CSV} rows={len(summary)}")
    print(f"Saved: {LATEST_MD}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
