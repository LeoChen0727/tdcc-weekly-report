from __future__ import annotations

from datetime import datetime
from pathlib import Path
from typing import Any, Callable
from zoneinfo import ZoneInfo
import math

import pandas as pd

from build_w_bottom_candidate_slope_curvature_audit import (
    SLOPE_CATEGORY_FOLDERS,
    abrupt_slope_change_count,
    classify,
    close_slope,
    direction_switch_count,
    load_price,
    low_reversal_metrics,
    path_slice,
    pct_round,
    segment_wrong_direction_rate,
    significant_turn_count,
)


ROOT = Path(".")
RESEARCH_LATEST_DIR = ROOT / "output" / "latest" / "research_backtest"
RESEARCH_HISTORY_DIR = ROOT / "output" / "history" / "research"

SOURCE_OBSERVATION_CSV = RESEARCH_LATEST_DIR / "w_bottom_observation_confirmation_audit_latest.csv"

LATEST_SUMMARY_CSV = RESEARCH_LATEST_DIR / "w_bottom_path_quality_filter_audit_latest.csv"
LATEST_DETAIL_CSV = RESEARCH_LATEST_DIR / "w_bottom_path_quality_filter_audit_detail_latest.csv"
LATEST_MD = RESEARCH_LATEST_DIR / "w_bottom_path_quality_filter_audit_latest.md"
HISTORY_SUMMARY_CSV = RESEARCH_HISTORY_DIR / "w_bottom_path_quality_filter_audit.csv"
HISTORY_DETAIL_CSV = RESEARCH_HISTORY_DIR / "w_bottom_path_quality_filter_audit_detail.csv"

MODEL_ID = "w_bottom_right_side"
CONFIRMATION_MODEL_ID = "neckline_volume_breakout_confirmation"
RESEARCH_ID = "w_bottom_path_quality_filter_audit"
SOURCE_RESEARCH_ID = "w_bottom_observation_confirmation_audit"
RESEARCH_VARIANT_ID = "warning_research_variant_only"
PARAMETER_SET_ID = "w_bottom_path_quality_filter_audit_20260625"

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
    "sample_mode",
    "stock_id",
    "stock_name",
    "signal_date",
    "initial_stage",
    "confirmation_stage",
    "transition_status",
    "slope_curvature_category",
    "slope_issue_reasons",
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
    "observation_stage_eligible",
    "confirmation_stage_eligible",
    "price_confirmation_only",
    "a_mature",
    "a_return_pct",
    "c_mature",
    "c_return_pct",
    "tdcc_any_age7",
    "tdcc_any_age14",
    "manual_review_status",
    "approved_for_daily",
    "production_readiness",
    "generated_at",
]

SUMMARY_COLUMNS = [
    "model_id",
    "confirmation_model_id",
    "research_id",
    "source_research_id",
    "research_variant_id",
    "parameter_set_id",
    "advisory_status",
    "filter_id",
    "filter_description",
    "sample_size",
    "mature_sample_size",
    "win_count",
    "win_rate",
    "avg_a_return_pct",
    "median_a_return_pct",
    "tdcc_any_age7_count",
    "smooth_count",
    "sharp_v_count",
    "wv_multiple_turn_count",
    "slope_break_count",
    "insufficient_path_count",
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


def write_csv(df: pd.DataFrame, path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(path, index=False, encoding="utf-8-sig")


def read_source() -> pd.DataFrame:
    if not SOURCE_OBSERVATION_CSV.exists():
        raise SystemExit(f"ERROR: missing required input: {SOURCE_OBSERVATION_CSV}")
    source = pd.read_csv(SOURCE_OBSERVATION_CSV, dtype=str, keep_default_na=False)
    required = {
        "stock_id",
        "stock_name",
        "signal_date",
        "left_peak_date",
        "left_low_date",
        "neckline_date",
        "right_low_date",
        "initial_stage",
        "confirmation_stage",
        "transition_status",
        "observation_stage_eligible",
        "confirmation_stage_eligible",
        "a_mature",
        "a_return_pct",
        "tdcc_any_age7",
        "approved_for_daily",
    }
    missing = sorted(required - set(source.columns))
    if missing:
        raise SystemExit(f"ERROR: observation audit missing columns: {missing}")
    return source


def build_path_metrics(source_row: pd.Series) -> dict[str, Any]:
    stock_id = normalize_code(source_row.get("stock_id"))
    price = load_price(stock_id)
    window, relative = path_slice(price, source_row)
    if window.empty or not relative:
        return {
            "slope_curvature_category": "insufficient_price_path",
            "slope_issue_reasons": "missing_price_path",
            "path_start_date": "",
            "path_end_date": "",
            "path_days": 0,
        }

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
    metrics["slope_curvature_category"] = category
    metrics["slope_issue_reasons"] = reasons
    return metrics


def build_detail(generated_at: str) -> pd.DataFrame:
    source = read_source()
    rows: list[dict[str, Any]] = []
    for _, source_row in source.iterrows():
        metrics = build_path_metrics(source_row)
        row = {
            "model_id": MODEL_ID,
            "confirmation_model_id": CONFIRMATION_MODEL_ID,
            "research_id": RESEARCH_ID,
            "source_research_id": SOURCE_RESEARCH_ID,
            "research_variant_id": RESEARCH_VARIANT_ID,
            "parameter_set_id": PARAMETER_SET_ID,
            "advisory_status": RESEARCH_VARIANT_ID,
            "sample_mode": safe_str(source_row.get("sample_mode")),
            "stock_id": normalize_code(source_row.get("stock_id")),
            "stock_name": safe_str(source_row.get("stock_name")),
            "signal_date": normalize_date(source_row.get("signal_date")),
            "initial_stage": safe_str(source_row.get("initial_stage")),
            "confirmation_stage": safe_str(source_row.get("confirmation_stage")),
            "transition_status": safe_str(source_row.get("transition_status")),
            "observation_stage_eligible": bool_text(bool_value(source_row.get("observation_stage_eligible"))),
            "confirmation_stage_eligible": bool_text(bool_value(source_row.get("confirmation_stage_eligible"))),
            "price_confirmation_only": bool_text(bool_value(source_row.get("price_confirmation_only"))),
            "a_mature": bool_text(bool_value(source_row.get("a_mature"))),
            "a_return_pct": safe_str(source_row.get("a_return_pct")),
            "c_mature": bool_text(bool_value(source_row.get("c_mature"))),
            "c_return_pct": safe_str(source_row.get("c_return_pct")),
            "tdcc_any_age7": bool_text(bool_value(source_row.get("tdcc_any_age7"))),
            "tdcc_any_age14": bool_text(bool_value(source_row.get("tdcc_any_age14"))),
            "manual_review_status": safe_str(source_row.get("manual_review_status")),
            "approved_for_daily": "false",
            "production_readiness": "not_production_ready_research_only",
            "generated_at": generated_at,
        }
        row.update(metrics)
        rows.append(row)
    detail = pd.DataFrame(rows)
    for column in DETAIL_COLUMNS:
        if column not in detail.columns:
            detail[column] = ""
    forbidden = sorted(set(detail.columns) & FORBIDDEN_PRODUCTION_FIELDS)
    if forbidden:
        raise SystemExit(f"ERROR: forbidden production columns in path quality detail: {forbidden}")
    invalid_categories = sorted(set(detail["slope_curvature_category"].astype(str)) - set(SLOPE_CATEGORY_FOLDERS))
    if invalid_categories:
        raise SystemExit(f"ERROR: invalid slope categories: {invalid_categories}")
    return detail[DETAIL_COLUMNS]


def pct(value: float) -> str:
    if math.isnan(value):
        return ""
    return f"{value:.2f}%"


def filter_specs() -> list[tuple[str, str, Callable[[pd.DataFrame], pd.Series]]]:
    return [
        (
            "all_volume_confirmed",
            "All volume-confirmed neckline breakouts.",
            lambda df: df["confirmation_stage"].eq("volume_confirmed_neckline_breakout"),
        ),
        (
            "observation_to_volume_confirmation",
            "Only candidates that started in the right-side observation zone and later confirmed by neckline volume breakout.",
            lambda df: df["transition_status"].eq("observation_to_volume_confirmation"),
        ),
        (
            "observation_volume_exclude_sharp_v",
            "Observation-to-volume-confirmation candidates excluding sharp V low reversals.",
            lambda df: df["transition_status"].eq("observation_to_volume_confirmation")
            & ~df["slope_curvature_category"].eq("sharp_v_bottom_risk"),
        ),
        (
            "observation_volume_exclude_wv_multiple_turn",
            "Observation-to-volume-confirmation candidates excluding WV/WVV multiple-turn paths.",
            lambda df: df["transition_status"].eq("observation_to_volume_confirmation")
            & ~df["slope_curvature_category"].eq("wv_multiple_turn_risk"),
        ),
        (
            "observation_volume_exclude_slope_break",
            "Observation-to-volume-confirmation candidates excluding slope-break/discontinuous paths.",
            lambda df: df["transition_status"].eq("observation_to_volume_confirmation")
            & ~df["slope_curvature_category"].eq("slope_break_discontinuous"),
        ),
        (
            "observation_volume_exclude_sharp_v_and_wv",
            "Observation-to-volume-confirmation candidates excluding sharp V and WV/WVV paths.",
            lambda df: df["transition_status"].eq("observation_to_volume_confirmation")
            & ~df["slope_curvature_category"].isin(["sharp_v_bottom_risk", "wv_multiple_turn_risk"]),
        ),
        (
            "observation_volume_smooth_only",
            "Observation-to-volume-confirmation candidates classified as smooth rounded W-like.",
            lambda df: df["transition_status"].eq("observation_to_volume_confirmation")
            & df["slope_curvature_category"].eq("smooth_rounded_w_like"),
        ),
        (
            "observation_volume_smooth_or_slope_break",
            "Observation-to-volume-confirmation candidates classified as smooth or slope-break, excluding sharp V and WV/WVV.",
            lambda df: df["transition_status"].eq("observation_to_volume_confirmation")
            & df["slope_curvature_category"].isin(["smooth_rounded_w_like", "slope_break_discontinuous"]),
        ),
    ]


def build_summary(detail: pd.DataFrame, generated_at: str) -> pd.DataFrame:
    rows: list[dict[str, Any]] = []
    for filter_id, description, predicate in filter_specs():
        sample = detail[predicate(detail)].copy()
        mature_mask = sample["a_mature"].map(bool_value) if not sample.empty else pd.Series(dtype=bool)
        mature_returns = pd.to_numeric(sample.loc[mature_mask, "a_return_pct"], errors="coerce") if not sample.empty else pd.Series(dtype=float)
        mature_returns = mature_returns.dropna()
        win_count = int(mature_returns.gt(0).sum())
        mature_count = int(len(mature_returns))
        sample_size = int(len(sample))
        category_counts = sample["slope_curvature_category"].value_counts().to_dict() if not sample.empty else {}
        rows.append(
            {
                "model_id": MODEL_ID,
                "confirmation_model_id": CONFIRMATION_MODEL_ID,
                "research_id": RESEARCH_ID,
                "source_research_id": SOURCE_RESEARCH_ID,
                "research_variant_id": RESEARCH_VARIANT_ID,
                "parameter_set_id": PARAMETER_SET_ID,
                "advisory_status": RESEARCH_VARIANT_ID,
                "filter_id": filter_id,
                "filter_description": description,
                "sample_size": sample_size,
                "mature_sample_size": mature_count,
                "win_count": win_count,
                "win_rate": pct(win_count / mature_count * 100.0) if mature_count else "",
                "avg_a_return_pct": "" if mature_returns.empty else f"{float(mature_returns.mean()):.4f}",
                "median_a_return_pct": "" if mature_returns.empty else f"{float(mature_returns.median()):.4f}",
                "tdcc_any_age7_count": int(sample["tdcc_any_age7"].map(bool_value).sum()) if not sample.empty else 0,
                "smooth_count": int(category_counts.get("smooth_rounded_w_like", 0)),
                "sharp_v_count": int(category_counts.get("sharp_v_bottom_risk", 0)),
                "wv_multiple_turn_count": int(category_counts.get("wv_multiple_turn_risk", 0)),
                "slope_break_count": int(category_counts.get("slope_break_discontinuous", 0)),
                "insufficient_path_count": int(category_counts.get("insufficient_price_path", 0)),
                "approved_for_daily": "false",
                "production_readiness": "not_production_ready_research_only",
                "generated_at": generated_at,
            }
        )
    summary = pd.DataFrame(rows)
    for column in SUMMARY_COLUMNS:
        if column not in summary.columns:
            summary[column] = ""
    forbidden = sorted(set(summary.columns) & FORBIDDEN_PRODUCTION_FIELDS)
    if forbidden:
        raise SystemExit(f"ERROR: forbidden production columns in path quality summary: {forbidden}")
    return summary[SUMMARY_COLUMNS]


def markdown_table(data: pd.DataFrame, columns: list[str], limit: int = 40) -> list[str]:
    if data.empty:
        return ["_No rows._"]
    lines = ["| " + " | ".join(columns) + " |", "| " + " | ".join(["---"] * len(columns)) + " |"]
    for _, row in data.loc[:, columns].head(limit).iterrows():
        lines.append("| " + " | ".join(safe_str(row.get(column)) for column in columns) + " |")
    return lines


def write_markdown(detail: pd.DataFrame, summary: pd.DataFrame, generated_at: str) -> None:
    category_counts = (
        detail.groupby("slope_curvature_category", dropna=False)
        .size()
        .reset_index(name="count")
        .sort_values("count", ascending=False)
    )
    cross = (
        detail.groupby(["transition_status", "slope_curvature_category"], dropna=False)
        .size()
        .reset_index(name="count")
        .sort_values(["transition_status", "slope_curvature_category"])
    )
    lines = [
        "# W-Bottom Path Quality Filter Audit",
        "",
        f"- generated_at: `{generated_at}`",
        f"- model_id: `{MODEL_ID}`",
        f"- confirmation_model_id: `{CONFIRMATION_MODEL_ID}`",
        f"- source_research_id: `{SOURCE_RESEARCH_ID}`",
        f"- rows: `{len(detail)}` dedup candidates",
        f"- advisory_status: `{RESEARCH_VARIANT_ID}`",
        "- production impact: `none`; this audit does not update production model conditions, scoring, ranking, or baseline.",
        "- interpretation boundary: path-quality filters are research-only candidates for manual review and later promotion analysis.",
        "",
        "## Path Category Counts",
        "",
        *markdown_table(category_counts, ["slope_curvature_category", "count"], limit=20),
        "",
        "## Filter Performance",
        "",
        *markdown_table(
            summary,
            [
                "filter_id",
                "sample_size",
                "mature_sample_size",
                "win_rate",
                "avg_a_return_pct",
                "median_a_return_pct",
                "smooth_count",
                "sharp_v_count",
                "wv_multiple_turn_count",
                "slope_break_count",
            ],
            limit=30,
        ),
        "",
        "## Transition X Path Category",
        "",
        *markdown_table(cross, ["transition_status", "slope_curvature_category", "count"], limit=100),
        "",
        "## Review Sample",
        "",
        *markdown_table(
            detail[
                [
                    "stock_id",
                    "signal_date",
                    "transition_status",
                    "slope_curvature_category",
                    "slope_issue_reasons",
                    "a_return_pct",
                ]
            ],
            ["stock_id", "signal_date", "transition_status", "slope_curvature_category", "slope_issue_reasons", "a_return_pct"],
            limit=40,
        ),
    ]
    LATEST_MD.parent.mkdir(parents=True, exist_ok=True)
    LATEST_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    generated_at = now_text()
    detail = build_detail(generated_at)
    if detail.empty:
        raise SystemExit("ERROR: W-bottom path quality detail produced no rows")
    summary = build_summary(detail, generated_at)
    write_csv(detail, LATEST_DETAIL_CSV)
    write_csv(detail, HISTORY_DETAIL_CSV)
    write_csv(summary, LATEST_SUMMARY_CSV)
    write_csv(summary, HISTORY_SUMMARY_CSV)
    write_markdown(detail, summary, generated_at)
    print(f"Saved: {LATEST_DETAIL_CSV} rows={len(detail)}")
    print(f"Saved: {LATEST_SUMMARY_CSV} rows={len(summary)}")
    print(f"Saved: {LATEST_MD}")
    print(f"Saved: {HISTORY_DETAIL_CSV} rows={len(detail)}")
    print(f"Saved: {HISTORY_SUMMARY_CSV} rows={len(summary)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
