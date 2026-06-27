from __future__ import annotations

from datetime import datetime
from pathlib import Path
from typing import Any
from zoneinfo import ZoneInfo
import math

import pandas as pd

import build_w_bottom_manual_positive_missed_case_audit as manual_audit
import build_w_bottom_tdcc_abc_backtest as w_bottom
from build_w_bottom_candidate_chart_review_packet import normalize_code, normalize_date, safe_float, safe_str


ROOT = Path(".")
RESEARCH_LATEST_DIR = ROOT / "output" / "latest" / "research_backtest"
RESEARCH_HISTORY_DIR = ROOT / "output" / "history" / "research"

SOURCE_QUALITY_CSV = RESEARCH_LATEST_DIR / "w_bottom_candidate_quality_audit_latest.csv"
SOURCE_PRICE_LEVEL_DETAIL_CSV = RESEARCH_LATEST_DIR / "w_bottom_price_level_audit_detail_latest.csv"
SOURCE_MANUAL_POSITIVE_CSV = RESEARCH_LATEST_DIR / "w_bottom_manual_positive_missed_case_audit_latest.csv"
SOURCE_CORE_REVIEW_CSV = RESEARCH_LATEST_DIR / "w_bottom_core_mainstream_exclude_wv_review_latest.csv"

LATEST_DETAIL_CSV = RESEARCH_LATEST_DIR / "w_bottom_left_anchor_pattern_family_audit_detail_latest.csv"
LATEST_SUMMARY_CSV = RESEARCH_LATEST_DIR / "w_bottom_left_anchor_pattern_family_audit_latest.csv"
LATEST_MD = RESEARCH_LATEST_DIR / "w_bottom_left_anchor_pattern_family_audit_latest.md"
HISTORY_DETAIL_CSV = RESEARCH_HISTORY_DIR / "w_bottom_left_anchor_pattern_family_audit_detail.csv"
HISTORY_SUMMARY_CSV = RESEARCH_HISTORY_DIR / "w_bottom_left_anchor_pattern_family_audit.csv"

MODEL_ID = "w_bottom_right_side"
CONFIRMATION_MODEL_ID = "neckline_volume_breakout_confirmation"
RESEARCH_ID = "w_bottom_left_anchor_pattern_family_audit"
SOURCE_RESEARCH_ID = "w_bottom_candidate_quality_audit"
MANUAL_SOURCE_RESEARCH_ID = "w_bottom_manual_positive_missed_case_audit"
RESEARCH_VARIANT_ID = "warning_research_variant_only"
PARAMETER_SET_ID = "w_bottom_left_anchor_pattern_family_audit_20260625"

AUTO_LEFT_PEAK_LOOKBACK_DAYS = 45
PRE_LOW_ALTERNATIVE_LOOKBACK_DAYS = 90
SEARCH_EDGE_DAYS = 43
ALT_HIGH_DIFF_MIN_PCT = 20.0

CASE_REVIEW_TAGS = {
    ("6415", "20260115"): "user_question_auto_anchor_only",
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

DETAIL_COLUMNS = [
    "model_id",
    "confirmation_model_id",
    "research_id",
    "source_research_id",
    "research_variant_id",
    "parameter_set_id",
    "advisory_status",
    "audit_scope",
    "case_review_tag",
    "manual_case_id",
    "stock_id",
    "stock_name",
    "signal_date",
    "user_interval_start",
    "user_interval_end",
    "transition_status",
    "slope_curvature_category",
    "price_level_bucket",
    "effective_mainstream_label",
    "human_pattern_type",
    "computed_pattern_family",
    "human_left_peak_date",
    "human_left_low_date",
    "human_neckline_date",
    "human_right_low_date",
    "auto_left_peak_date",
    "auto_left_peak_price",
    "auto_left_low_date",
    "auto_left_low_price",
    "auto_neckline_date",
    "auto_neckline_price",
    "auto_right_low_date",
    "auto_right_low_price",
    "second_low_gap_pct",
    "first_drop_pct",
    "neckline_depth_from_left_low_pct",
    "neckline_depth_from_right_low_pct",
    "auto_left_peak_days_before_left_low",
    "auto_selected_at_search_window_edge",
    "highest_pre_left_low_90_date",
    "highest_pre_left_low_90_price",
    "highest_pre_left_low_90_days_before_low",
    "highest_pre_left_low_90_diff_vs_auto_peak_pct",
    "higher_pre_left_low_90_outside_current_window",
    "human_auto_left_peak_delta_trading_days",
    "human_auto_left_low_delta_trading_days",
    "human_auto_neckline_delta_trading_days",
    "human_auto_right_low_delta_trading_days",
    "anchor_issue_type",
    "anchor_issue_reason",
    "recommended_next_research_action",
    "chart_path",
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
    "summary_dimension",
    "summary_value",
    "row_count",
    "current_candidate_count",
    "manual_positive_count",
    "anchor_issue_count",
    "anchor_issue_rate_pct",
    "standard_double_bottom_w_count",
    "higher_right_low_base_w_count",
    "search_window_edge_count",
    "higher_alt_peak_count",
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


def read_csv(path: Path) -> pd.DataFrame:
    if not path.exists():
        raise SystemExit(f"ERROR: missing required input: {path}")
    return pd.read_csv(path, dtype=str, keep_default_na=False)


def markdown_table(df: pd.DataFrame, columns: list[str], limit: int = 40) -> list[str]:
    if df.empty:
        return ["_No rows._"]
    view = df.loc[:, columns].head(limit).copy()
    lines = ["| " + " | ".join(columns) + " |", "| " + " | ".join(["---"] * len(columns)) + " |"]
    for _, row in view.iterrows():
        lines.append("| " + " | ".join(safe_str(row.get(column)) for column in columns) + " |")
    return lines


def trading_day_delta(price: pd.DataFrame, start_date: str, end_date: str) -> int | str:
    start = index_for_date(price, start_date)
    end = index_for_date(price, end_date)
    if start is None or end is None:
        return ""
    return end - start


def index_for_date(price: pd.DataFrame, date: str) -> int | None:
    normalized = normalize_date(date)
    if not normalized:
        return None
    matches = price.index[price["date"].eq(normalized)]
    if len(matches) == 0:
        return None
    return int(matches[0])


def price_row(price: pd.DataFrame, date: str) -> pd.Series | None:
    idx = index_for_date(price, date)
    if idx is None:
        return None
    return price.iloc[idx]


def load_price(stock_id: str) -> pd.DataFrame:
    return manual_audit.load_price(stock_id)


def price_value(price: pd.DataFrame, date: str, column: str) -> float:
    row = price_row(price, date)
    if row is None:
        return math.nan
    return safe_float(row.get(column))


def highest_pre_left_low(price: pd.DataFrame, left_low_date: str) -> dict[str, Any]:
    low_idx = index_for_date(price, left_low_date)
    if low_idx is None:
        return {
            "date": "",
            "price": math.nan,
            "days_before_low": "",
        }
    start = max(0, low_idx - PRE_LOW_ALTERNATIVE_LOOKBACK_DAYS)
    end = max(start, low_idx - 2)
    window = price.iloc[start:end].copy()
    if window.empty:
        return {
            "date": "",
            "price": math.nan,
            "days_before_low": "",
        }
    highs = pd.to_numeric(window["high"], errors="coerce")
    if highs.dropna().empty:
        return {
            "date": "",
            "price": math.nan,
            "days_before_low": "",
        }
    local_idx = int(highs.idxmax())
    peak_date = normalize_date(price.iloc[local_idx].get("date"))
    return {
        "date": peak_date,
        "price": safe_float(price.iloc[local_idx].get("high")),
        "days_before_low": low_idx - local_idx,
    }


def classify_pattern_family(second_low_gap_pct: float) -> str:
    if math.isnan(second_low_gap_pct):
        return "pending_pattern_review"
    if w_bottom.SECOND_LOW_GAP_MIN <= second_low_gap_pct <= w_bottom.SECOND_LOW_GAP_MAX:
        return "standard_double_bottom_w"
    if second_low_gap_pct > w_bottom.SECOND_LOW_GAP_MAX and second_low_gap_pct <= 20.0:
        return "higher_right_low_base_w"
    if second_low_gap_pct < w_bottom.SECOND_LOW_GAP_MIN:
        return "lower_second_low_undercut_w"
    return "pending_pattern_review"


def detect_context_without_history_gate(price: pd.DataFrame, date: str) -> dict[str, Any] | None:
    idx = index_for_date(price, date)
    if idx is None:
        return None
    original = w_bottom.long_position_ok
    try:
        w_bottom.long_position_ok = lambda history, current_close: True
        return w_bottom.detect_w_bottom_context_at(price, idx)
    finally:
        w_bottom.long_position_ok = original


def context_from_quality_row(row: pd.Series) -> dict[str, str]:
    return {
        "left_peak_date": normalize_date(row.get("left_peak_date")),
        "left_low_date": normalize_date(row.get("left_low_date")),
        "neckline_date": normalize_date(row.get("neckline_date")),
        "right_low_date": normalize_date(row.get("right_low_date")),
    }


def context_from_manual_row(row: pd.Series) -> dict[str, str]:
    return {
        "left_peak_date": normalize_date(row.get("manual_left_peak_date")),
        "left_low_date": normalize_date(row.get("manual_left_low_date")),
        "neckline_date": normalize_date(row.get("manual_neckline_date")),
        "right_low_date": normalize_date(row.get("manual_right_low_date")),
    }


def auto_context_for_manual(price: pd.DataFrame, row: pd.Series) -> dict[str, Any]:
    probe_date = normalize_date(row.get("relaxed_history_probe_date")) or normalize_date(row.get("manual_observation_date"))
    context = detect_context_without_history_gate(price, probe_date)
    if context:
        return context
    return {
        "left_peak_date": "",
        "left_low_date": "",
        "neckline_date": "",
        "right_low_date": "",
        "neckline_price": math.nan,
        "right_low_value": math.nan,
    }


def joined_source_tables() -> tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    quality = read_csv(SOURCE_QUALITY_CSV)
    price_level = read_csv(SOURCE_PRICE_LEVEL_DETAIL_CSV)
    manual = read_csv(SOURCE_MANUAL_POSITIVE_CSV)
    core_review = read_csv(SOURCE_CORE_REVIEW_CSV) if SOURCE_CORE_REVIEW_CSV.exists() else pd.DataFrame()

    for df in [quality, price_level, manual, core_review]:
        if df.empty:
            continue
        if "stock_id" in df.columns:
            df["stock_id"] = df["stock_id"].map(normalize_code)
        for column in ["signal_date", "manual_observation_date", "relaxed_history_probe_date"]:
            if column in df.columns:
                df[column] = df[column].map(normalize_date)

    price_cols = [
        "stock_id",
        "signal_date",
        "transition_status",
        "slope_curvature_category",
        "price_level_bucket",
        "effective_mainstream_label",
    ]
    for column in price_cols:
        if column not in price_level.columns:
            price_level[column] = ""
    quality = quality.merge(price_level[price_cols], on=["stock_id", "signal_date"], how="left", suffixes=("", "_price"))

    chart_cols = ["stock_id", "signal_date", "chart_path"]
    if core_review.empty:
        core_review = pd.DataFrame(columns=chart_cols)
    for column in chart_cols:
        if column not in core_review.columns:
            core_review[column] = ""
    quality = quality.merge(core_review[chart_cols], on=["stock_id", "signal_date"], how="left", suffixes=("", "_core"))
    return quality, price_level, manual


def anchor_metrics(price: pd.DataFrame, context: dict[str, Any], human_context: dict[str, str] | None = None) -> dict[str, Any]:
    left_peak_date = normalize_date(context.get("left_peak_date"))
    left_low_date = normalize_date(context.get("left_low_date"))
    neckline_date = normalize_date(context.get("neckline_date"))
    right_low_date = normalize_date(context.get("right_low_date"))

    left_peak_price = price_value(price, left_peak_date, "high")
    left_low_price = price_value(price, left_low_date, "low")
    neckline_price = safe_float(context.get("neckline_price"))
    if math.isnan(neckline_price):
        neckline_price = price_value(price, neckline_date, "high")
    right_low_price = safe_float(context.get("right_low_value"))
    if math.isnan(right_low_price):
        right_low_price = price_value(price, right_low_date, "low")

    second_low_gap = (right_low_price / left_low_price - 1.0) * 100.0 if left_low_price > 0 else math.nan
    first_drop = (left_low_price / left_peak_price - 1.0) * 100.0 if left_peak_price > 0 else math.nan
    neckline_from_left = (neckline_price / left_low_price - 1.0) * 100.0 if left_low_price > 0 else math.nan
    neckline_from_right = (neckline_price / right_low_price - 1.0) * 100.0 if right_low_price > 0 else math.nan

    left_peak_idx = index_for_date(price, left_peak_date)
    left_low_idx = index_for_date(price, left_low_date)
    auto_days_before_low: int | str = ""
    if left_peak_idx is not None and left_low_idx is not None:
        auto_days_before_low = left_low_idx - left_peak_idx

    pre_high = highest_pre_left_low(price, left_low_date)
    high_diff = math.nan
    higher_outside = False
    if not math.isnan(pre_high["price"]) and left_peak_price > 0:
        high_diff = (pre_high["price"] / left_peak_price - 1.0) * 100.0
        higher_outside = (
            bool(pre_high["days_before_low"])
            and int(pre_high["days_before_low"]) > AUTO_LEFT_PEAK_LOOKBACK_DAYS
            and high_diff >= ALT_HIGH_DIFF_MIN_PCT
        )

    selected_at_edge = isinstance(auto_days_before_low, int) and auto_days_before_low >= SEARCH_EDGE_DAYS

    human_delta = {
        "human_auto_left_peak_delta_trading_days": "",
        "human_auto_left_low_delta_trading_days": "",
        "human_auto_neckline_delta_trading_days": "",
        "human_auto_right_low_delta_trading_days": "",
    }
    if human_context:
        human_delta = {
            "human_auto_left_peak_delta_trading_days": trading_day_delta(
                price, safe_str(human_context.get("left_peak_date")), left_peak_date
            ),
            "human_auto_left_low_delta_trading_days": trading_day_delta(
                price, safe_str(human_context.get("left_low_date")), left_low_date
            ),
            "human_auto_neckline_delta_trading_days": trading_day_delta(
                price, safe_str(human_context.get("neckline_date")), neckline_date
            ),
            "human_auto_right_low_delta_trading_days": trading_day_delta(
                price, safe_str(human_context.get("right_low_date")), right_low_date
            ),
        }

    return {
        "auto_left_peak_date": left_peak_date,
        "auto_left_peak_price": pct(left_peak_price),
        "auto_left_low_date": left_low_date,
        "auto_left_low_price": pct(left_low_price),
        "auto_neckline_date": neckline_date,
        "auto_neckline_price": pct(neckline_price),
        "auto_right_low_date": right_low_date,
        "auto_right_low_price": pct(right_low_price),
        "second_low_gap_pct": pct(second_low_gap),
        "first_drop_pct": pct(first_drop),
        "neckline_depth_from_left_low_pct": pct(neckline_from_left),
        "neckline_depth_from_right_low_pct": pct(neckline_from_right),
        "auto_left_peak_days_before_left_low": auto_days_before_low,
        "auto_selected_at_search_window_edge": bool_text(selected_at_edge),
        "highest_pre_left_low_90_date": pre_high["date"],
        "highest_pre_left_low_90_price": pct(pre_high["price"]),
        "highest_pre_left_low_90_days_before_low": pre_high["days_before_low"],
        "highest_pre_left_low_90_diff_vs_auto_peak_pct": pct(high_diff),
        "higher_pre_left_low_90_outside_current_window": bool_text(higher_outside),
        "computed_pattern_family": classify_pattern_family(second_low_gap),
        **human_delta,
    }


def anchor_issue(metrics: dict[str, Any], audit_scope: str, human_context: dict[str, str] | None) -> tuple[str, str, str]:
    auto_left_peak = safe_str(metrics.get("auto_left_peak_date"))
    human_left_peak = safe_str(human_context.get("left_peak_date")) if human_context else ""
    if audit_scope == "manual_positive_missed_case" and not auto_left_peak:
        return (
            "manual_positive_no_current_auto_anchor",
            "Current detector produced no comparable auto anchor for the manual positive case.",
            "review_as_separate_pattern_family_or_gate_before_promotion",
        )
    if human_left_peak and auto_left_peak and human_left_peak != auto_left_peak:
        return (
            "human_auto_left_peak_mismatch",
            f"Human left peak {human_left_peak} differs from auto left peak {auto_left_peak}.",
            "audit_left_start_selection_before_model_change",
        )
    if safe_str(metrics.get("higher_pre_left_low_90_outside_current_window")).lower() == "true":
        return (
            "higher_pre_left_low_peak_outside_45d_window",
            "A higher pre-left-low peak exists outside the current 45-trading-day left-peak search window.",
            "review_left_anchor_window_or_structural_start_rule",
        )
    if safe_str(metrics.get("auto_selected_at_search_window_edge")).lower() == "true":
        return (
            "auto_left_peak_near_search_window_edge",
            "Auto left peak is near the 45-trading-day search boundary, so the structural start may be truncated.",
            "manual_confirm_left_start_before_using_as_positive",
        )
    return (
        "no_anchor_issue_detected",
        "No left-anchor issue detected by this audit.",
        "no_immediate_anchor_action",
    )


def base_detail_row(generated_at: str) -> dict[str, Any]:
    return {
        "model_id": MODEL_ID,
        "confirmation_model_id": CONFIRMATION_MODEL_ID,
        "research_id": RESEARCH_ID,
        "research_variant_id": RESEARCH_VARIANT_ID,
        "parameter_set_id": PARAMETER_SET_ID,
        "advisory_status": RESEARCH_VARIANT_ID,
        "manual_review_status": "pending_research_review",
        "approved_for_daily": "false",
        "production_readiness": "not_production_ready_research_only",
        "generated_at": generated_at,
    }


def build_current_candidate_rows(quality: pd.DataFrame, generated_at: str) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    required = {"stock_id", "signal_date", "left_peak_date", "left_low_date", "neckline_date", "right_low_date"}
    missing = sorted(required - set(quality.columns))
    if missing:
        raise SystemExit(f"ERROR: quality audit missing columns: {missing}")

    for _, source_row in quality.iterrows():
        stock_id = normalize_code(source_row.get("stock_id"))
        signal_date = normalize_date(source_row.get("signal_date"))
        price = load_price(stock_id)
        context = context_from_quality_row(source_row)
        metrics = anchor_metrics(price, context)
        case_review_tag = CASE_REVIEW_TAGS.get((stock_id, signal_date), "")
        issue_type, issue_reason, action = anchor_issue(metrics, "current_model_candidate", None)
        if case_review_tag == "user_question_auto_anchor_only" and issue_type == "no_anchor_issue_detected":
            issue_type = "user_question_auto_anchor_pending_manual_confirmation"
            issue_reason = "User asked why the current detector selected this left start; no human replacement anchor is confirmed yet."
            action = "manual_confirm_left_start_before_using_as_positive"
        row = {
            **base_detail_row(generated_at),
            "source_research_id": SOURCE_RESEARCH_ID,
            "audit_scope": "current_model_candidate",
            "case_review_tag": case_review_tag,
            "manual_case_id": "",
            "stock_id": stock_id,
            "stock_name": safe_str(source_row.get("stock_name")),
            "signal_date": signal_date,
            "user_interval_start": "",
            "user_interval_end": "",
            "transition_status": safe_str(source_row.get("transition_status")),
            "slope_curvature_category": safe_str(source_row.get("slope_curvature_category")),
            "price_level_bucket": safe_str(source_row.get("price_level_bucket")),
            "effective_mainstream_label": safe_str(source_row.get("effective_mainstream_label")),
            "human_pattern_type": "",
            "human_left_peak_date": "",
            "human_left_low_date": "",
            "human_neckline_date": "",
            "human_right_low_date": "",
            "anchor_issue_type": issue_type,
            "anchor_issue_reason": issue_reason,
            "recommended_next_research_action": action,
            "chart_path": safe_str(source_row.get("chart_path")),
        }
        row.update(metrics)
        rows.append(row)
    return rows


def build_manual_positive_rows(manual: pd.DataFrame, generated_at: str) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for _, source_row in manual.iterrows():
        stock_id = normalize_code(source_row.get("stock_id"))
        price = load_price(stock_id)
        human_context = context_from_manual_row(source_row)
        auto_context = auto_context_for_manual(price, source_row)
        metrics = anchor_metrics(price, auto_context, human_context=human_context)
        if not safe_str(metrics.get("computed_pattern_family")) or metrics["computed_pattern_family"] == "pending_pattern_review":
            manual_gap = safe_float(source_row.get("second_low_gap_pct"))
            metrics["computed_pattern_family"] = classify_pattern_family(manual_gap)
            metrics["second_low_gap_pct"] = pct(manual_gap)
        issue_type, issue_reason, action = anchor_issue(metrics, "manual_positive_missed_case", human_context)
        if metrics["computed_pattern_family"] == "higher_right_low_base_w":
            action = "split_higher_right_low_base_from_standard_w"
        row = {
            **base_detail_row(generated_at),
            "source_research_id": MANUAL_SOURCE_RESEARCH_ID,
            "audit_scope": "manual_positive_missed_case",
            "case_review_tag": "user_manual_positive",
            "manual_case_id": safe_str(source_row.get("manual_case_id")),
            "stock_id": stock_id,
            "stock_name": safe_str(source_row.get("stock_name")),
            "signal_date": normalize_date(source_row.get("manual_observation_date")),
            "user_interval_start": normalize_date(source_row.get("user_interval_start")),
            "user_interval_end": normalize_date(source_row.get("user_interval_end")),
            "transition_status": "",
            "slope_curvature_category": "",
            "price_level_bucket": "",
            "effective_mainstream_label": "",
            "human_pattern_type": safe_str(source_row.get("manual_pattern_type")),
            "human_left_peak_date": human_context["left_peak_date"],
            "human_left_low_date": human_context["left_low_date"],
            "human_neckline_date": human_context["neckline_date"],
            "human_right_low_date": human_context["right_low_date"],
            "anchor_issue_type": issue_type,
            "anchor_issue_reason": issue_reason,
            "recommended_next_research_action": action,
            "chart_path": safe_str(source_row.get("chart_path")),
            "manual_review_status": "pending_user_model_review",
        }
        row.update(metrics)
        rows.append(row)
    return rows


def summarize(detail: pd.DataFrame, generated_at: str) -> pd.DataFrame:
    rows: list[dict[str, Any]] = []

    def add_summary(dimension: str, value: str, frame: pd.DataFrame) -> None:
        if frame.empty:
            return
        issue_count = int((~frame["anchor_issue_type"].eq("no_anchor_issue_detected")).sum())
        count = len(frame)
        rows.append(
            {
                "model_id": MODEL_ID,
                "confirmation_model_id": CONFIRMATION_MODEL_ID,
                "research_id": RESEARCH_ID,
                "research_variant_id": RESEARCH_VARIANT_ID,
                "parameter_set_id": PARAMETER_SET_ID,
                "advisory_status": RESEARCH_VARIANT_ID,
                "summary_dimension": dimension,
                "summary_value": value,
                "row_count": count,
                "current_candidate_count": int(detail.loc[frame.index, "audit_scope"].eq("current_model_candidate").sum()),
                "manual_positive_count": int(detail.loc[frame.index, "audit_scope"].eq("manual_positive_missed_case").sum()),
                "anchor_issue_count": issue_count,
                "anchor_issue_rate_pct": pct(issue_count / count * 100.0 if count else math.nan),
                "standard_double_bottom_w_count": int(frame["computed_pattern_family"].eq("standard_double_bottom_w").sum()),
                "higher_right_low_base_w_count": int(frame["computed_pattern_family"].eq("higher_right_low_base_w").sum()),
                "search_window_edge_count": int(frame["auto_selected_at_search_window_edge"].astype(str).str.lower().eq("true").sum()),
                "higher_alt_peak_count": int(frame["higher_pre_left_low_90_outside_current_window"].astype(str).str.lower().eq("true").sum()),
                "production_readiness": "not_production_ready_research_only",
                "generated_at": generated_at,
            }
        )

    add_summary("overall", "all", detail)
    for column in ["audit_scope", "computed_pattern_family", "anchor_issue_type", "case_review_tag"]:
        for value, frame in detail.groupby(column, dropna=False):
            value_text = safe_str(value) or "blank"
            add_summary(column, value_text, frame)
    return pd.DataFrame(rows, columns=SUMMARY_COLUMNS)


def write_markdown(detail: pd.DataFrame, summary: pd.DataFrame, generated_at: str) -> None:
    key_cases = detail[
        detail["case_review_tag"].isin(["user_manual_positive", "user_question_auto_anchor_only"])
    ].copy()
    issue_summary = summary[summary["summary_dimension"].eq("anchor_issue_type")].copy()
    issue_summary = issue_summary.sort_values(["row_count", "summary_value"], ascending=[False, True])
    family_summary = summary[summary["summary_dimension"].eq("computed_pattern_family")].copy()
    family_summary = family_summary.sort_values(["row_count", "summary_value"], ascending=[False, True])

    lines = [
        "# W-Bottom Left-Anchor And Pattern-Family Audit",
        "",
        f"- generated_at: `{generated_at}`",
        f"- model_id: `{MODEL_ID}`",
        f"- confirmation_model_id: `{CONFIRMATION_MODEL_ID}`",
        f"- research_id: `{RESEARCH_ID}`",
        f"- source_research_id: `{SOURCE_RESEARCH_ID}`",
        f"- manual_source_research_id: `{MANUAL_SOURCE_RESEARCH_ID}`",
        f"- detail_rows: `{len(detail)}`",
        f"- summary_rows: `{len(summary)}`",
        f"- advisory_status: `{RESEARCH_VARIANT_ID}`",
        "- production impact: `none`; this audit does not update production model conditions, scoring, ranking, or baseline.",
        "- interpretation boundary: this is a research-only left_peak_start_selection and pattern-family audit.",
        "",
        "## What This Tests",
        "",
        f"- Current detector picks the left peak from at most `{AUTO_LEFT_PEAK_LOOKBACK_DAYS}` trading days before the first low.",
        f"- This audit checks whether the selected left peak is near that search-window edge, or whether a pre-low peak at least `{ALT_HIGH_DIFF_MIN_PCT}`% higher exists in a `{PRE_LOW_ALTERNATIVE_LOOKBACK_DAYS}`-trading-day window.",
        "- It also separates `standard_double_bottom_w` from `higher_right_low_base_w` so those families do not get mixed by simply widening the second-low gap.",
        "",
        "## Pattern-Family Summary",
        "",
        *markdown_table(
            family_summary,
            [
                "summary_value",
                "row_count",
                "current_candidate_count",
                "manual_positive_count",
                "anchor_issue_count",
                "search_window_edge_count",
                "higher_alt_peak_count",
            ],
        ),
        "",
        "## Anchor-Issue Summary",
        "",
        *markdown_table(
            issue_summary,
            [
                "summary_value",
                "row_count",
                "current_candidate_count",
                "manual_positive_count",
                "anchor_issue_rate_pct",
            ],
        ),
        "",
        "## Key Review Cases",
        "",
        *markdown_table(
            key_cases,
            [
                "stock_id",
                "stock_name",
                "case_review_tag",
                "computed_pattern_family",
                "human_left_peak_date",
                "auto_left_peak_date",
                "auto_left_peak_days_before_left_low",
                "anchor_issue_type",
                "recommended_next_research_action",
            ],
            limit=20,
        ),
        "",
        "## Reading Notes",
        "",
        "- `4916` supports a separate higher-right-low base/W family rather than widening the current standard-W gate.",
        "- `8069` shows a standard-W-like manual positive where the auto anchor can differ from the human visual anchor once the history gate is bypassed.",
        "- `6415` is not assigned a replacement human anchor here; it is preserved as a user-questioned auto-anchor case for manual confirmation.",
        "- This audit is not a production promotion artifact.",
    ]
    LATEST_MD.parent.mkdir(parents=True, exist_ok=True)
    LATEST_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    generated_at = now_text()
    quality, _, manual = joined_source_tables()
    current_rows = build_current_candidate_rows(quality, generated_at)
    manual_rows = build_manual_positive_rows(manual, generated_at)
    detail = pd.DataFrame(current_rows + manual_rows, columns=DETAIL_COLUMNS)
    if detail.empty:
        raise SystemExit("ERROR: no left-anchor audit rows generated")
    forbidden = sorted(set(detail.columns) & FORBIDDEN_PRODUCTION_FIELDS)
    if forbidden:
        raise SystemExit(f"ERROR: left-anchor audit emitted forbidden production fields: {forbidden}")
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
