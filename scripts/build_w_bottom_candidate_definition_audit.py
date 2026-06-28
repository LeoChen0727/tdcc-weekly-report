from __future__ import annotations

from collections import Counter
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

SOURCE_CHART_REVIEW_CSV = RESEARCH_LATEST_DIR / "w_bottom_candidate_chart_review_latest.csv"
SOURCE_SLOPE_AUDIT_CSV = RESEARCH_LATEST_DIR / "w_bottom_candidate_slope_curvature_audit_latest.csv"
LATEST_AUDIT_CSV = RESEARCH_LATEST_DIR / "w_bottom_candidate_definition_audit_latest.csv"
LATEST_AUDIT_MD = RESEARCH_LATEST_DIR / "w_bottom_candidate_definition_audit_latest.md"
HISTORY_AUDIT_CSV = RESEARCH_HISTORY_DIR / "w_bottom_candidate_definition_audit.csv"

MODEL_ID = "w_bottom_right_side"
RESEARCH_ID = "w_bottom_candidate_definition_audit"
SOURCE_RESEARCH_ID = "w_bottom_candidate_chart_review"
SOURCE_CANDIDATE_SET_ID = "grid_gap_2_20_rebound_7_12_vol_1_2"
RESEARCH_VARIANT_ID = "warning_research_variant_only"
PARAMETER_SET_ID = "w_bottom_definition_audit_20260625"

PRIOR_DOWNTREND_MIN_PCT = 8.0
SUPPORT_ZONE_ABS_MAX_PCT = 6.0
SECOND_LOW_EFFECTIVE_BREAK_PCT = -3.0
NECKLINE_DEPTH_MIN_PCT = 6.0
RIGHT_SUPPORT_BREAK_RATIO = 0.97

DEFINITION_STATUSES = {
    "definition_confirmed_with_volume",
    "price_confirmed_without_volume",
    "valid_right_side_watch",
    "late_or_no_breakout",
    "support_failed",
    "invalid_definition_structure",
    "insufficient_price_path",
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
    "definition_status",
    "definition_issue_reasons",
    "chart_path",
    "left_peak_date",
    "left_low_date",
    "neckline_date",
    "right_low_date",
    "left_peak_high",
    "first_low_value",
    "neckline_price",
    "right_low_value",
    "signal_close",
    "prior_downtrend_pct",
    "support_gap_pct",
    "first_low_to_neckline_pct",
    "right_low_to_neckline_pct",
    "signal_distance_to_neckline_pct",
    "prior_downtrend_ok",
    "two_lows_same_support_zone",
    "second_low_not_effectively_broken",
    "neckline_valid",
    "right_side_holding_support",
    "price_neckline_breakout_confirmed",
    "volume_confirmed_breakout",
    "late_completion_not_w",
    "definition_base_ok",
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


def bool_value(value: Any) -> bool:
    return safe_str(value).lower() in {"true", "1", "yes", "y"}


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
        "signal_close",
        "neckline_price",
        "right_low_value",
        "signal_distance_to_neckline_pct",
        "sym1_5_w_shape_completed",
        "sym1_5_neckline_volume_breakout",
        "sym1_5_right_low_broken",
        "sym1_5_quality_bucket",
        "approved_for_daily",
    }
    missing = sorted(required - set(source.columns))
    if missing:
        raise SystemExit(f"ERROR: source chart review missing columns: {missing}")
    if SOURCE_SLOPE_AUDIT_CSV.exists():
        slope = pd.read_csv(SOURCE_SLOPE_AUDIT_CSV, dtype=str, keep_default_na=False)
        slope = slope[["stock_id", "signal_date", "slope_curvature_category"]].copy()
        source = source.merge(slope, on=["stock_id", "signal_date"], how="left")
    if "slope_curvature_category" not in source.columns:
        source["slope_curvature_category"] = ""
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
    return price[price["date"].ne("")].sort_values("date").reset_index(drop=True)


def index_for_date(price: pd.DataFrame, date: str) -> int | None:
    matches = price.index[price["date"].eq(normalize_date(date))]
    if len(matches) == 0:
        return None
    return int(matches[0])


def price_value(price: pd.DataFrame, date: str, column: str) -> float:
    idx = index_for_date(price, date)
    if idx is None or column not in price.columns:
        return math.nan
    return safe_float(price.iloc[idx].get(column))


def classify(row: dict[str, Any]) -> tuple[str, str]:
    issues: list[str] = []
    if not row["price_path_available"]:
        return "insufficient_price_path", "missing_price_path"
    checks = {
        "prior_downtrend_ok": row["prior_downtrend_ok"],
        "two_lows_same_support_zone": row["two_lows_same_support_zone"],
        "second_low_not_effectively_broken": row["second_low_not_effectively_broken"],
        "neckline_valid": row["neckline_valid"],
    }
    for name, passed in checks.items():
        if not passed:
            issues.append(name.replace("_ok", "_missing").replace("_valid", "_invalid"))
    if issues:
        return "invalid_definition_structure", ";".join(issues)
    if not row["right_side_holding_support"]:
        return "support_failed", "right_low_support_broken_after_signal"
    if row["volume_confirmed_breakout"]:
        return "definition_confirmed_with_volume", "definition_confirmed_and_volume_breakout"
    if row["price_neckline_breakout_confirmed"]:
        return "price_confirmed_without_volume", "neckline_price_confirmed_volume_missing"
    if row["late_completion_not_w"]:
        return "late_or_no_breakout", "neckline_completion_or_breakout_too_late"
    if safe_str(row["outcome_category_id"]) == "did_not_complete_w":
        return "late_or_no_breakout", "no_neckline_breakout_observed"
    return "valid_right_side_watch", "definition_base_ok_waiting_for_breakout"


def build_row(source_row: pd.Series, generated_at: str) -> dict[str, Any]:
    stock_id = normalize_code(source_row.get("stock_id"))
    price = load_price(stock_id)
    dates = {
        "left_peak": normalize_date(source_row.get("left_peak_date")),
        "left_low": normalize_date(source_row.get("left_low_date")),
        "neckline": normalize_date(source_row.get("neckline_date")),
        "right_low": normalize_date(source_row.get("right_low_date")),
        "signal": normalize_date(source_row.get("signal_date")),
    }
    indexes = {name: index_for_date(price, date) for name, date in dates.items()} if not price.empty else {}
    price_path_available = bool(indexes) and all(index is not None for index in indexes.values())

    left_peak_high = price_value(price, dates["left_peak"], "high") if price_path_available else math.nan
    first_low = price_value(price, dates["left_low"], "low") if price_path_available else math.nan
    neckline = price_value(price, dates["neckline"], "high") if price_path_available else safe_float(source_row.get("neckline_price"))
    right_low = price_value(price, dates["right_low"], "low") if price_path_available else safe_float(source_row.get("right_low_value"))
    signal_close = price_value(price, dates["signal"], "close") if price_path_available else safe_float(source_row.get("signal_close"))

    prior_downtrend_pct = (first_low / left_peak_high - 1.0) * 100.0 if first_low > 0 and left_peak_high > 0 else math.nan
    support_gap_pct = (right_low / first_low - 1.0) * 100.0 if right_low > 0 and first_low > 0 else math.nan
    first_low_to_neckline_pct = (neckline / first_low - 1.0) * 100.0 if neckline > 0 and first_low > 0 else math.nan
    right_low_to_neckline_pct = (neckline / right_low - 1.0) * 100.0 if neckline > 0 and right_low > 0 else math.nan
    signal_distance_to_neckline_pct = (
        (signal_close / neckline - 1.0) * 100.0 if signal_close > 0 and neckline > 0 else safe_float(source_row.get("signal_distance_to_neckline_pct"))
    )

    date_order_ok = (
        price_path_available
        and indexes["left_peak"] < indexes["left_low"] < indexes["neckline"] < indexes["right_low"] <= indexes["signal"]
    )
    prior_downtrend_ok = date_order_ok and not math.isnan(prior_downtrend_pct) and prior_downtrend_pct <= -PRIOR_DOWNTREND_MIN_PCT
    two_lows_same_support_zone = not math.isnan(support_gap_pct) and abs(support_gap_pct) <= SUPPORT_ZONE_ABS_MAX_PCT
    second_low_not_effectively_broken = not math.isnan(support_gap_pct) and support_gap_pct >= SECOND_LOW_EFFECTIVE_BREAK_PCT
    neckline_valid = (
        date_order_ok
        and not math.isnan(first_low_to_neckline_pct)
        and not math.isnan(right_low_to_neckline_pct)
        and first_low_to_neckline_pct >= NECKLINE_DEPTH_MIN_PCT
        and right_low_to_neckline_pct >= NECKLINE_DEPTH_MIN_PCT
        and neckline > max(first_low, right_low)
    )
    right_support_broken = bool_value(source_row.get("sym1_5_right_low_broken"))
    right_side_holding_support = not right_support_broken
    price_neckline_breakout_confirmed = bool_value(source_row.get("sym1_5_w_shape_completed"))
    volume_confirmed_breakout = bool_value(source_row.get("sym1_5_neckline_volume_breakout"))
    late_completion_not_w = safe_str(source_row.get("sym1_5_quality_bucket")) in {
        "late_volume_breakout_not_w",
        "late_neckline_completion_not_w",
    } or safe_str(source_row.get("outcome_category_id")) == "completion_too_late_for_w"

    row: dict[str, Any] = {
        "model_id": MODEL_ID,
        "research_id": RESEARCH_ID,
        "source_research_id": SOURCE_RESEARCH_ID,
        "source_candidate_set_id": SOURCE_CANDIDATE_SET_ID,
        "research_variant_id": RESEARCH_VARIANT_ID,
        "parameter_set_id": PARAMETER_SET_ID,
        "advisory_status": RESEARCH_VARIANT_ID,
        "stock_id": stock_id,
        "stock_name": safe_str(source_row.get("stock_name")),
        "signal_date": dates["signal"],
        "outcome_category_id": safe_str(source_row.get("category_id")),
        "slope_curvature_category": safe_str(source_row.get("slope_curvature_category")),
        "chart_path": safe_str(source_row.get("chart_path")),
        "left_peak_date": dates["left_peak"],
        "left_low_date": dates["left_low"],
        "neckline_date": dates["neckline"],
        "right_low_date": dates["right_low"],
        "left_peak_high": pct_round(left_peak_high),
        "first_low_value": pct_round(first_low),
        "neckline_price": pct_round(neckline),
        "right_low_value": pct_round(right_low),
        "signal_close": pct_round(signal_close),
        "prior_downtrend_pct": pct_round(prior_downtrend_pct),
        "support_gap_pct": pct_round(support_gap_pct),
        "first_low_to_neckline_pct": pct_round(first_low_to_neckline_pct),
        "right_low_to_neckline_pct": pct_round(right_low_to_neckline_pct),
        "signal_distance_to_neckline_pct": pct_round(signal_distance_to_neckline_pct),
        "prior_downtrend_ok": bool_text(prior_downtrend_ok),
        "two_lows_same_support_zone": bool_text(two_lows_same_support_zone),
        "second_low_not_effectively_broken": bool_text(second_low_not_effectively_broken),
        "neckline_valid": bool_text(neckline_valid),
        "right_side_holding_support": bool_text(right_side_holding_support),
        "price_neckline_breakout_confirmed": bool_text(price_neckline_breakout_confirmed),
        "volume_confirmed_breakout": bool_text(volume_confirmed_breakout),
        "late_completion_not_w": bool_text(late_completion_not_w),
        "definition_base_ok": bool_text(False),
        "manual_review_status": "pending_user_shape_review",
        "approved_for_daily": "false",
        "generated_at": generated_at,
        "price_path_available": price_path_available,
    }
    base_ok = prior_downtrend_ok and two_lows_same_support_zone and second_low_not_effectively_broken and neckline_valid
    row["definition_base_ok"] = bool_text(base_ok)
    status, reasons = classify(
        {
            "price_path_available": price_path_available,
            "prior_downtrend_ok": prior_downtrend_ok,
            "two_lows_same_support_zone": two_lows_same_support_zone,
            "second_low_not_effectively_broken": second_low_not_effectively_broken,
            "neckline_valid": neckline_valid,
            "right_side_holding_support": right_side_holding_support,
            "volume_confirmed_breakout": volume_confirmed_breakout,
            "price_neckline_breakout_confirmed": price_neckline_breakout_confirmed,
            "late_completion_not_w": late_completion_not_w,
            "outcome_category_id": row["outcome_category_id"],
        }
    )
    row["definition_status"] = status
    row["definition_issue_reasons"] = reasons
    row.pop("price_path_available", None)
    return row


def build_audit(generated_at: str) -> pd.DataFrame:
    source = read_source()
    rows = [build_row(row, generated_at) for _, row in source.iterrows()]
    audit = pd.DataFrame(rows)
    for column in OUTPUT_COLUMNS:
        if column not in audit.columns:
            audit[column] = ""
    invalid = sorted(set(audit["definition_status"].astype(str)) - DEFINITION_STATUSES)
    if invalid:
        raise SystemExit(f"ERROR: invalid definition statuses: {invalid}")
    forbidden = sorted(set(audit.columns) & FORBIDDEN_PRODUCTION_FIELDS)
    if forbidden:
        raise SystemExit(f"ERROR: forbidden production columns in definition audit: {forbidden}")
    return audit[OUTPUT_COLUMNS]


def write_csv(df: pd.DataFrame, path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(path, index=False, encoding="utf-8-sig")


def rate(numerator: int, denominator: int) -> str:
    if denominator <= 0:
        return ""
    return f"{numerator / denominator * 100.0:.2f}%"


def markdown_table(data: pd.DataFrame | list[dict[str, Any]], columns: list[str], limit: int = 40) -> list[str]:
    df = data if isinstance(data, pd.DataFrame) else pd.DataFrame(data)
    if df.empty:
        return ["_No rows._"]
    rows = df.head(limit).to_dict("records")
    lines = ["| " + " | ".join(columns) + " |", "| " + " | ".join(["---"] * len(columns)) + " |"]
    for row in rows:
        lines.append("| " + " | ".join(safe_str(row.get(column)) for column in columns) + " |")
    return lines


def write_markdown(audit: pd.DataFrame, generated_at: str) -> None:
    total = len(audit)
    status_counts = (
        audit.groupby("definition_status", dropna=False)
        .size()
        .reset_index(name="count")
        .sort_values("count", ascending=False)
    )
    base_ok_count = int(audit["definition_base_ok"].astype(str).eq("true").sum())
    volume_count = int(audit["volume_confirmed_breakout"].astype(str).eq("true").sum())
    price_count = int(audit["price_neckline_breakout_confirmed"].astype(str).eq("true").sum())
    issue_counter = Counter()
    for text in audit["definition_issue_reasons"].astype(str):
        for reason in text.split(";"):
            reason = reason.strip()
            if reason:
                issue_counter[reason] += 1
    issue_rows = [{"issue_reason": reason, "count": count} for reason, count in issue_counter.most_common()]
    cross = (
        audit.groupby(["definition_status", "slope_curvature_category"], dropna=False)
        .size()
        .reset_index(name="count")
        .sort_values(["definition_status", "slope_curvature_category"])
    )
    sample = audit[
        [
            "stock_id",
            "signal_date",
            "definition_status",
            "definition_issue_reasons",
            "support_gap_pct",
            "prior_downtrend_pct",
            "right_low_to_neckline_pct",
            "chart_path",
        ]
    ]
    lines = [
        "# W-Bottom Candidate Definition Audit",
        "",
        f"- generated_at: `{generated_at}`",
        f"- model_id: `{MODEL_ID}`",
        f"- source_research_id: `{SOURCE_RESEARCH_ID}`",
        f"- source_candidate_set_id: `{SOURCE_CANDIDATE_SET_ID}`",
        f"- rows: `{total}`",
        f"- advisory_status: `{RESEARCH_VARIANT_ID}`",
        "- production impact: `none`; this audit does not update production model conditions, scoring, ranking, or baseline.",
        "",
        "## Definition Rules Tested",
        "",
        f"- prior downtrend: left peak to first low decline at least `{PRIOR_DOWNTREND_MIN_PCT}%`.",
        f"- support zone: second low must be within `+/-{SUPPORT_ZONE_ABS_MAX_PCT}%` of first low.",
        f"- effective break: second low must not be more than `{abs(SECOND_LOW_EFFECTIVE_BREAK_PCT)}%` below first low.",
        f"- neckline: middle rebound high must be at least `{NECKLINE_DEPTH_MIN_PCT}%` above both lows.",
        f"- right-side support: right low must not later be broken by `{round((1 - RIGHT_SUPPORT_BREAK_RATIO) * 100, 2)}%`.",
        "",
        "## Headline Counts",
        "",
        "| metric | count | rate |",
        "| --- | ---: | ---: |",
        f"| definition base ok | {base_ok_count} | {rate(base_ok_count, total)} |",
        f"| price neckline breakout confirmed | {price_count} | {rate(price_count, total)} |",
        f"| volume confirmed breakout | {volume_count} | {rate(volume_count, total)} |",
        "",
        "## Definition Status Counts",
        "",
        *markdown_table(status_counts, ["definition_status", "count"], limit=20),
        "",
        "## Issue Reasons",
        "",
        *markdown_table(issue_rows, ["issue_reason", "count"], limit=30),
        "",
        "## Definition X Slope Category",
        "",
        *markdown_table(cross, ["definition_status", "slope_curvature_category", "count"], limit=80),
        "",
        "## Review Sample",
        "",
        *markdown_table(sample, list(sample.columns), limit=30),
    ]
    LATEST_AUDIT_MD.parent.mkdir(parents=True, exist_ok=True)
    LATEST_AUDIT_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    generated_at = now_text()
    audit = build_audit(generated_at)
    if audit.empty:
        raise SystemExit("ERROR: W-bottom definition audit produced no rows")
    write_csv(audit, LATEST_AUDIT_CSV)
    write_csv(audit, HISTORY_AUDIT_CSV)
    write_markdown(audit, generated_at)
    print(f"Saved: {LATEST_AUDIT_CSV} rows={len(audit)}")
    print(f"Saved: {LATEST_AUDIT_MD}")
    print(f"Saved: {HISTORY_AUDIT_CSV} rows={len(audit)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
