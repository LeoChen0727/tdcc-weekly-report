from __future__ import annotations

from collections import Counter
from datetime import datetime
from pathlib import Path
from typing import Any
from zoneinfo import ZoneInfo
import math
import shutil

import pandas as pd


ROOT = Path(".")
PRICE_DIR = ROOT / "data" / "stock_price_history"
RESEARCH_LATEST_DIR = ROOT / "output" / "latest" / "research_backtest"
RESEARCH_HISTORY_DIR = ROOT / "output" / "history" / "research"

SOURCE_CHART_REVIEW_CSV = RESEARCH_LATEST_DIR / "w_bottom_candidate_chart_review_latest.csv"
SOURCE_CHART_ROOT = RESEARCH_LATEST_DIR / "w_bottom_candidate_chart_review"
SLOPE_REVIEW_ROOT = RESEARCH_LATEST_DIR / "w_bottom_candidate_slope_curvature_review"
LATEST_AUDIT_CSV = RESEARCH_LATEST_DIR / "w_bottom_candidate_slope_curvature_audit_latest.csv"
LATEST_AUDIT_MD = RESEARCH_LATEST_DIR / "w_bottom_candidate_slope_curvature_audit_latest.md"
HISTORY_AUDIT_CSV = RESEARCH_HISTORY_DIR / "w_bottom_candidate_slope_curvature_audit.csv"

MODEL_ID = "w_bottom_right_side"
RESEARCH_ID = "w_bottom_candidate_slope_curvature_audit"
SOURCE_RESEARCH_ID = "w_bottom_candidate_chart_review"
SOURCE_CANDIDATE_SET_ID = "grid_gap_2_20_rebound_7_12_vol_1_2"
RESEARCH_VARIANT_ID = "warning_research_variant_only"
PARAMETER_SET_ID = "w_bottom_slope_curvature_audit_20260625"

SMOOTH_WINDOW = 3
SLOPE_EPSILON_PCT = 0.4
ABRUPT_SLOPE_CHANGE_PCT = 3.5
SHARP_LOW_PRE_SLOPE_PCT = -1.0
SHARP_LOW_POST_SLOPE_PCT = 0.8
SHARP_LOW_CHANGE_PCT = 3.0
SIGNIFICANT_TURN_MOVE_PCT = 3.0

SLOPE_CATEGORY_FOLDERS = {
    "smooth_rounded_w_like": "01_smooth_rounded_w_like",
    "sharp_v_bottom_risk": "02_sharp_v_bottom_risk",
    "wv_multiple_turn_risk": "03_wv_multiple_turn_risk",
    "slope_break_discontinuous": "04_slope_break_discontinuous",
    "insufficient_price_path": "99_insufficient_price_path",
}

FORBIDDEN_PRODUCTION_FIELDS = {
    "trade_decision",
    "action_rating",
    "entry_style",
    "position_sizing",
    "decision_score",
    "daily_candidate_decision",
    "buy_signal",
}

OUTPUT_COLUMNS = [
    "model_id",
    "research_id",
    "source_research_id",
    "source_candidate_set_id",
    "research_variant_id",
    "parameter_set_id",
    "advisory_status",
    "stock_id",
    "stock_name",
    "signal_date",
    "outcome_category_id",
    "slope_curvature_category",
    "slope_category_folder",
    "source_chart_path",
    "slope_review_chart_path",
    "slope_review_chart_path_absolute",
    "left_peak_date",
    "left_low_date",
    "neckline_date",
    "right_low_date",
    "path_start_date",
    "path_end_date",
    "path_days",
    "full_path_significant_turn_count",
    "full_path_abrupt_slope_change_count",
    "full_path_direction_switch_count",
    "full_path_max_abs_daily_return_pct",
    "full_path_max_abs_smoothed_slope_change_pct",
    "left_descent_days",
    "first_rebound_days",
    "second_decline_days",
    "right_rebound_days",
    "left_descent_wrong_direction_rate",
    "first_rebound_wrong_direction_rate",
    "second_decline_wrong_direction_rate",
    "right_rebound_wrong_direction_rate",
    "first_low_pre3_avg_slope_pct",
    "first_low_post3_avg_slope_pct",
    "first_low_slope_reversal_change_pct",
    "first_low_sharp_v_flag",
    "second_low_pre3_avg_slope_pct",
    "second_low_post3_avg_slope_pct",
    "second_low_slope_reversal_change_pct",
    "second_low_sharp_v_flag",
    "slope_issue_reasons",
    "manual_review_status",
    "approved_for_daily",
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
        return float(text)
    except ValueError:
        return math.nan


def normalize_date(value: Any) -> str:
    text = safe_str(value)
    if text.endswith(".0"):
        text = text[:-2]
    digits = "".join(ch for ch in text if ch.isdigit())
    return digits[:8]


def normalize_code(value: Any) -> str:
    text = safe_str(value)
    if text.endswith(".0"):
        text = text[:-2]
    return text.zfill(4) if text.isdigit() and len(text) < 4 else text


def pct_round(value: float, digits: int = 4) -> float | str:
    if math.isnan(value) or math.isinf(value):
        return ""
    return round(value, digits)


def bool_text(value: bool) -> str:
    return "true" if value else "false"


def rate(numerator: int, denominator: int) -> float | str:
    if denominator <= 0:
        return ""
    return round(numerator / denominator * 100.0, 4)


def read_source() -> pd.DataFrame:
    if not SOURCE_CHART_REVIEW_CSV.exists():
        raise SystemExit(f"ERROR: missing required input: {SOURCE_CHART_REVIEW_CSV}")
    source = pd.read_csv(SOURCE_CHART_REVIEW_CSV, dtype=str, keep_default_na=False)
    required = {
        "stock_id",
        "stock_name",
        "signal_date",
        "category_id",
        "chart_path",
        "left_peak_date",
        "left_low_date",
        "neckline_date",
        "right_low_date",
        "approved_for_daily",
    }
    missing = sorted(required - set(source.columns))
    if missing:
        raise SystemExit(f"ERROR: source chart review missing columns: {missing}")
    return source


def load_price(stock_id: str) -> pd.DataFrame:
    path = PRICE_DIR / f"{normalize_code(stock_id)}.csv"
    if not path.exists():
        return pd.DataFrame()
    price = pd.read_csv(path, dtype=str, keep_default_na=False)
    if "date" not in price.columns:
        return pd.DataFrame()
    price = price.copy()
    price["date"] = price["date"].map(normalize_date)
    for column in ["open", "high", "low", "close", "volume"]:
        if column in price.columns:
            price[column] = pd.to_numeric(price[column], errors="coerce")
    price = price[price["date"].ne("")].sort_values("date").reset_index(drop=True)
    return price


def index_for_date(price: pd.DataFrame, date: str) -> int | None:
    matches = price.index[price["date"].eq(normalize_date(date))]
    if len(matches) == 0:
        return None
    return int(matches[0])


def clean_review_root() -> None:
    root_abs = SLOPE_REVIEW_ROOT.resolve()
    latest_abs = RESEARCH_LATEST_DIR.resolve()
    if latest_abs not in root_abs.parents:
        raise SystemExit(f"ERROR: refused to clear slope review root outside research latest dir: {root_abs}")
    if SLOPE_REVIEW_ROOT.exists():
        shutil.rmtree(SLOPE_REVIEW_ROOT)
    for folder in SLOPE_CATEGORY_FOLDERS.values():
        (SLOPE_REVIEW_ROOT / folder).mkdir(parents=True, exist_ok=True)


def path_slice(price: pd.DataFrame, row: pd.Series) -> tuple[pd.DataFrame, dict[str, int]]:
    dates = {
        "left_peak": normalize_date(row.get("left_peak_date")),
        "left_low": normalize_date(row.get("left_low_date")),
        "neckline": normalize_date(row.get("neckline_date")),
        "right_low": normalize_date(row.get("right_low_date")),
        "signal": normalize_date(row.get("signal_date")),
    }
    original_indexes = {name: index_for_date(price, date) for name, date in dates.items()}
    if any(index is None for index in original_indexes.values()):
        return pd.DataFrame(), {}
    start = int(original_indexes["left_peak"])
    end = int(original_indexes["signal"])
    if end <= start:
        return pd.DataFrame(), {}
    window = price.iloc[start : end + 1].reset_index(drop=True)
    relative = {name: int(index) - start for name, index in original_indexes.items() if index is not None}
    return window, relative


def close_slope(window: pd.DataFrame) -> pd.DataFrame:
    result = window[["date", "close"]].copy()
    result["daily_return_pct"] = result["close"].pct_change() * 100.0
    result["smoothed_slope_pct"] = result["daily_return_pct"].rolling(SMOOTH_WINDOW, min_periods=1).mean()
    result["smoothed_slope_change_pct"] = result["smoothed_slope_pct"].diff()
    return result


def sign_from_slope(value: float) -> int:
    if math.isnan(value) or abs(value) < SLOPE_EPSILON_PCT:
        return 0
    return 1 if value > 0 else -1


def direction_switch_count(slopes: pd.Series) -> int:
    signs = [sign_from_slope(safe_float(value)) for value in slopes]
    signs = [sign for sign in signs if sign != 0]
    if len(signs) < 2:
        return 0
    return sum(1 for previous, current in zip(signs, signs[1:]) if previous != current)


def abrupt_slope_change_count(slope_changes: pd.Series) -> int:
    values = pd.to_numeric(slope_changes, errors="coerce").abs()
    return int(values.ge(ABRUPT_SLOPE_CHANGE_PCT).sum())


def segment_wrong_direction_rate(slope_df: pd.DataFrame, start: int, end: int, expected_sign: int) -> float | str:
    if end <= start:
        return ""
    segment = slope_df.iloc[start + 1 : end + 1]["smoothed_slope_pct"].dropna()
    if segment.empty:
        return ""
    if expected_sign < 0:
        wrong = int(segment.gt(SLOPE_EPSILON_PCT).sum())
    else:
        wrong = int(segment.lt(-SLOPE_EPSILON_PCT).sum())
    return rate(wrong, len(segment))


def avg_slope(slope_df: pd.DataFrame, start: int, end: int) -> float:
    if end < start:
        return math.nan
    values = pd.to_numeric(slope_df.iloc[start : end + 1]["smoothed_slope_pct"], errors="coerce").dropna()
    if values.empty:
        return math.nan
    return float(values.mean())


def low_reversal_metrics(slope_df: pd.DataFrame, low_idx: int) -> tuple[float, float, float, bool]:
    pre = avg_slope(slope_df, max(1, low_idx - 3), max(1, low_idx - 1))
    post = avg_slope(slope_df, min(len(slope_df) - 1, low_idx + 1), min(len(slope_df) - 1, low_idx + 3))
    change = post - pre if not math.isnan(pre) and not math.isnan(post) else math.nan
    sharp = (
        not math.isnan(pre)
        and not math.isnan(post)
        and not math.isnan(change)
        and pre <= SHARP_LOW_PRE_SLOPE_PCT
        and post >= SHARP_LOW_POST_SLOPE_PCT
        and change >= SHARP_LOW_CHANGE_PCT
    )
    return pre, post, change, sharp


def significant_turn_count(close_values: pd.Series) -> int:
    closes = pd.to_numeric(close_values, errors="coerce").dropna().reset_index(drop=True)
    if len(closes) < 5:
        return 0
    smoothed = closes.rolling(3, min_periods=1).mean()
    raw_signs = []
    for value in smoothed.diff().tolist():
        if pd.isna(value):
            raw_signs.append(0)
        elif value > 0:
            raw_signs.append(1)
        elif value < 0:
            raw_signs.append(-1)
        else:
            raw_signs.append(0)
    turns: list[tuple[int, float]] = []
    previous_sign = 0
    previous_turn_price = float(smoothed.iloc[0])
    for idx, sign in enumerate(raw_signs):
        if sign == 0:
            continue
        if previous_sign == 0:
            previous_sign = sign
            continue
        if sign == previous_sign:
            continue
        current_price = float(smoothed.iloc[idx])
        move_pct = abs(current_price / previous_turn_price - 1.0) * 100.0 if previous_turn_price > 0 else 0.0
        if move_pct >= SIGNIFICANT_TURN_MOVE_PCT:
            turns.append((idx, current_price))
            previous_turn_price = current_price
            previous_sign = sign
    return len(turns)


def slope_chart_copy_path(row: pd.Series, category: str) -> Path:
    source_name = Path(safe_str(row.get("chart_path"))).name
    if not source_name:
        source_name = f"{normalize_date(row.get('signal_date'))}_{normalize_code(row.get('stock_id'))}.png"
    return SLOPE_REVIEW_ROOT / SLOPE_CATEGORY_FOLDERS[category] / source_name


def classify(metrics: dict[str, Any]) -> tuple[str, str]:
    reasons: list[str] = []
    if metrics["path_days"] < 20:
        return "insufficient_price_path", "path_too_short"
    if metrics["first_low_sharp_v_flag"] == "true":
        reasons.append("first_low_sharp_v")
    if metrics["second_low_sharp_v_flag"] == "true":
        reasons.append("second_low_sharp_v")
    if reasons:
        return "sharp_v_bottom_risk", ";".join(reasons)
    if safe_float(metrics["full_path_significant_turn_count"]) >= 5:
        reasons.append("too_many_significant_turns")
        return "wv_multiple_turn_risk", ";".join(reasons)
    if safe_float(metrics["full_path_abrupt_slope_change_count"]) >= 4:
        reasons.append("too_many_abrupt_slope_changes")
    if safe_float(metrics["full_path_max_abs_smoothed_slope_change_pct"]) >= 7.0:
        reasons.append("large_single_slope_break")
    if safe_float(metrics["full_path_direction_switch_count"]) >= 8:
        reasons.append("too_many_direction_switches")
    if reasons:
        return "slope_break_discontinuous", ";".join(reasons)
    return "smooth_rounded_w_like", "smooth_enough_for_manual_review"


def build_row(source_row: pd.Series) -> dict[str, Any]:
    stock_id = normalize_code(source_row.get("stock_id"))
    price = load_price(stock_id)
    window, relative = path_slice(price, source_row)
    base = {
        "model_id": MODEL_ID,
        "research_id": RESEARCH_ID,
        "source_research_id": SOURCE_RESEARCH_ID,
        "source_candidate_set_id": SOURCE_CANDIDATE_SET_ID,
        "research_variant_id": RESEARCH_VARIANT_ID,
        "parameter_set_id": PARAMETER_SET_ID,
        "advisory_status": RESEARCH_VARIANT_ID,
        "stock_id": stock_id,
        "stock_name": safe_str(source_row.get("stock_name")),
        "signal_date": normalize_date(source_row.get("signal_date")),
        "outcome_category_id": safe_str(source_row.get("category_id")),
        "source_chart_path": safe_str(source_row.get("chart_path")),
        "left_peak_date": normalize_date(source_row.get("left_peak_date")),
        "left_low_date": normalize_date(source_row.get("left_low_date")),
        "neckline_date": normalize_date(source_row.get("neckline_date")),
        "right_low_date": normalize_date(source_row.get("right_low_date")),
        "manual_review_status": "pending_user_shape_review",
        "approved_for_daily": "false",
    }
    if window.empty or not relative:
        category = "insufficient_price_path"
        chart_copy = slope_chart_copy_path(source_row, category)
        base.update(
            {
                "slope_curvature_category": category,
                "slope_category_folder": SLOPE_CATEGORY_FOLDERS[category],
                "slope_review_chart_path": chart_copy.as_posix(),
                "slope_review_chart_path_absolute": str(chart_copy.resolve()),
                "path_start_date": "",
                "path_end_date": "",
                "path_days": 0,
                "slope_issue_reasons": "missing_price_path",
            }
        )
        return base

    slope_df = close_slope(window)
    left_peak = relative["left_peak"]
    left_low = relative["left_low"]
    neckline = relative["neckline"]
    right_low = relative["right_low"]
    signal = relative["signal"]
    first_pre, first_post, first_change, first_sharp = low_reversal_metrics(slope_df, left_low)
    second_pre, second_post, second_change, second_sharp = low_reversal_metrics(slope_df, right_low)
    full_abs_returns = pd.to_numeric(slope_df["daily_return_pct"], errors="coerce").abs()
    full_abs_changes = pd.to_numeric(slope_df["smoothed_slope_change_pct"], errors="coerce").abs()
    metrics: dict[str, Any] = {
        "path_start_date": safe_str(window.iloc[0].get("date")),
        "path_end_date": safe_str(window.iloc[-1].get("date")),
        "path_days": len(window),
        "full_path_significant_turn_count": significant_turn_count(window["close"]),
        "full_path_abrupt_slope_change_count": abrupt_slope_change_count(slope_df["smoothed_slope_change_pct"]),
        "full_path_direction_switch_count": direction_switch_count(slope_df["smoothed_slope_pct"]),
        "full_path_max_abs_daily_return_pct": pct_round(float(full_abs_returns.max(skipna=True))),
        "full_path_max_abs_smoothed_slope_change_pct": pct_round(float(full_abs_changes.max(skipna=True))),
        "left_descent_days": max(0, left_low - left_peak + 1),
        "first_rebound_days": max(0, neckline - left_low + 1),
        "second_decline_days": max(0, right_low - neckline + 1),
        "right_rebound_days": max(0, signal - right_low + 1),
        "left_descent_wrong_direction_rate": segment_wrong_direction_rate(slope_df, left_peak, left_low, -1),
        "first_rebound_wrong_direction_rate": segment_wrong_direction_rate(slope_df, left_low, neckline, 1),
        "second_decline_wrong_direction_rate": segment_wrong_direction_rate(slope_df, neckline, right_low, -1),
        "right_rebound_wrong_direction_rate": segment_wrong_direction_rate(slope_df, right_low, signal, 1),
        "first_low_pre3_avg_slope_pct": pct_round(first_pre),
        "first_low_post3_avg_slope_pct": pct_round(first_post),
        "first_low_slope_reversal_change_pct": pct_round(first_change),
        "first_low_sharp_v_flag": bool_text(first_sharp),
        "second_low_pre3_avg_slope_pct": pct_round(second_pre),
        "second_low_post3_avg_slope_pct": pct_round(second_post),
        "second_low_slope_reversal_change_pct": pct_round(second_change),
        "second_low_sharp_v_flag": bool_text(second_sharp),
    }
    category, reasons = classify(metrics)
    chart_copy = slope_chart_copy_path(source_row, category)
    metrics.update(
        {
            "slope_curvature_category": category,
            "slope_category_folder": SLOPE_CATEGORY_FOLDERS[category],
            "slope_review_chart_path": chart_copy.as_posix(),
            "slope_review_chart_path_absolute": str(chart_copy.resolve()),
            "slope_issue_reasons": reasons,
        }
    )
    base.update(metrics)
    return base


def copy_chart(source_chart: str, target_path: Path) -> None:
    source_path = Path(source_chart)
    if not source_path.exists():
        raise SystemExit(f"ERROR: missing source chart: {source_path}")
    target_path.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(source_path, target_path)


def build_audit(generated_at: str) -> pd.DataFrame:
    source = read_source()
    clean_review_root()
    rows = []
    for _, source_row in source.iterrows():
        row = build_row(source_row)
        row["generated_at"] = generated_at
        copy_chart(row["source_chart_path"], Path(row["slope_review_chart_path"]))
        rows.append(row)
    audit = pd.DataFrame(rows)
    for column in OUTPUT_COLUMNS:
        if column not in audit.columns:
            audit[column] = ""
    forbidden = sorted(set(audit.columns) & FORBIDDEN_PRODUCTION_FIELDS)
    if forbidden:
        raise SystemExit(f"ERROR: forbidden production columns in slope audit: {forbidden}")
    return audit[OUTPUT_COLUMNS]


def write_csv(df: pd.DataFrame, path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(path, index=False, encoding="utf-8-sig")


def markdown_table(data: pd.DataFrame | list[dict[str, Any]], columns: list[str], limit: int = 30) -> list[str]:
    df = data if isinstance(data, pd.DataFrame) else pd.DataFrame(data)
    if df.empty:
        return ["_No rows._"]
    rows = df.head(limit).to_dict("records")
    lines = ["| " + " | ".join(columns) + " |", "| " + " | ".join(["---"] * len(columns)) + " |"]
    for row in rows:
        lines.append("| " + " | ".join(safe_str(row.get(column)) for column in columns) + " |")
    return lines


def write_markdown(audit: pd.DataFrame, generated_at: str) -> None:
    category_counts = (
        audit.groupby(["slope_curvature_category", "slope_category_folder"], dropna=False)
        .size()
        .reset_index(name="chart_count")
        .sort_values(["slope_category_folder"])
    )
    cross_counts = (
        audit.groupby(["outcome_category_id", "slope_curvature_category"], dropna=False)
        .size()
        .reset_index(name="count")
        .sort_values(["outcome_category_id", "slope_curvature_category"])
    )
    issue_counts = Counter()
    for text in audit["slope_issue_reasons"].astype(str):
        for reason in text.split(";"):
            reason = reason.strip()
            if reason:
                issue_counts[reason] += 1
    issue_rows = [{"issue_reason": reason, "count": count} for reason, count in issue_counts.most_common()]
    sample = audit[
        [
            "stock_id",
            "signal_date",
            "outcome_category_id",
            "slope_curvature_category",
            "full_path_significant_turn_count",
            "full_path_abrupt_slope_change_count",
            "first_low_sharp_v_flag",
            "second_low_sharp_v_flag",
            "slope_review_chart_path",
        ]
    ]
    lines = [
        "# W-Bottom Candidate Slope Curvature Audit",
        "",
        f"- generated_at: `{generated_at}`",
        f"- model_id: `{MODEL_ID}`",
        f"- source_research_id: `{SOURCE_RESEARCH_ID}`",
        f"- source_candidate_set_id: `{SOURCE_CANDIDATE_SET_ID}`",
        f"- rows: `{len(audit)}`",
        f"- slope_review_root: `{SLOPE_REVIEW_ROOT}`",
        f"- advisory_status: `{RESEARCH_VARIANT_ID}`",
        "- production impact: `none`; this audit does not update production model conditions, scoring, ranking, or baseline.",
        "",
        "## Classification Logic",
        "",
        "- Uses close-to-close daily slope and 3-day smoothed slope.",
        "- Flags sharp V when 3-day average slope before a low is strongly negative, after the low is strongly positive, and the slope reversal is abrupt.",
        "- Flags WV/multiple-turn risk when the smoothed close path has too many significant turns.",
        "- Flags slope discontinuity when slope changes or direction switches are too frequent.",
        "",
        "## Slope Category Counts",
        "",
        *markdown_table(category_counts, ["slope_curvature_category", "slope_category_folder", "chart_count"], limit=20),
        "",
        "## Issue Reasons",
        "",
        *markdown_table(issue_rows, ["issue_reason", "count"], limit=20),
        "",
        "## Outcome X Slope Category",
        "",
        *markdown_table(cross_counts, ["outcome_category_id", "slope_curvature_category", "count"], limit=80),
        "",
        "## Review Index Sample",
        "",
        *markdown_table(sample, list(sample.columns), limit=30),
    ]
    LATEST_AUDIT_MD.parent.mkdir(parents=True, exist_ok=True)
    LATEST_AUDIT_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    generated_at = now_text()
    audit = build_audit(generated_at)
    if audit.empty:
        raise SystemExit("ERROR: W-bottom slope curvature audit produced no rows")
    write_csv(audit, LATEST_AUDIT_CSV)
    write_csv(audit, HISTORY_AUDIT_CSV)
    write_markdown(audit, generated_at)
    print(f"Saved: {LATEST_AUDIT_CSV} rows={len(audit)}")
    print(f"Saved: {LATEST_AUDIT_MD}")
    print(f"Saved slope review root: {SLOPE_REVIEW_ROOT}")
    print(f"Saved: {HISTORY_AUDIT_CSV} rows={len(audit)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
