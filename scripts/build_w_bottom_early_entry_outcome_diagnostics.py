from __future__ import annotations

from datetime import datetime
from pathlib import Path
from typing import Any, Callable
from zoneinfo import ZoneInfo
import math

import pandas as pd


ROOT = Path(".")
RESEARCH_LATEST_DIR = ROOT / "output" / "latest" / "research_backtest"
RESEARCH_HISTORY_DIR = ROOT / "output" / "history" / "research"

SOURCE_DETAIL_CSV = RESEARCH_LATEST_DIR / "w_bottom_early_entry_parameter_grid_detail_latest.csv"
LATEST_CSV = RESEARCH_LATEST_DIR / "w_bottom_early_entry_outcome_diagnostics_latest.csv"
LATEST_MD = RESEARCH_LATEST_DIR / "w_bottom_early_entry_outcome_diagnostics_latest.md"
HISTORY_CSV = RESEARCH_HISTORY_DIR / "w_bottom_early_entry_outcome_diagnostics.csv"

MODEL_ID = "w_bottom_right_side"
CONFIRMATION_MODEL_ID = "neckline_volume_breakout_confirmation"
OVERLAY_MODEL_ID = "tdcc_weekly_ranking_formula"
RESEARCH_ID = "w_bottom_early_entry_outcome_diagnostics"
SOURCE_RESEARCH_ID = "w_bottom_early_entry_parameter_grid"
RESEARCH_VARIANT_ID = "warning_research_variant_only"
PRODUCTION_READINESS = "not_production_ready_research_only"
SURFACE_ID = "w_bottom_right_low_early_entry"
BASELINE_SEGMENT_ID = "all_rows"
TARGET_OUTCOME_RULES = {
    "take_profit_10pct_close_40d",
    "tp10_or_neutral_after_5pct_close_40d",
}
STRICT_SMOOTH_REBOUND_SEGMENTS = [
    "smooth_right_rebound_5_20",
    "smooth_price_le40_right_rebound_5_20",
    "smooth_core_mainstream_right_rebound_5_20",
    "smooth_core_mainstream_price_le40_right_rebound_5_20",
    "smooth_right_rebound_5_20_red_ratio_gt_first",
    "smooth_right_rebound_5_20_near_neckline",
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

OUTPUT_COLUMNS = [
    "model_id",
    "confirmation_model_id",
    "overlay_model_id",
    "research_id",
    "source_research_id",
    "research_variant_id",
    "advisory_status",
    "surface_id",
    "event_set_id",
    "outcome_rule_id",
    "diagnostic_type",
    "segment_id",
    "segment_description",
    "sample_size",
    "evaluated_sample_size",
    "mature_sample_size",
    "win_count",
    "neutral_count",
    "loss_count",
    "incomplete_count",
    "win_rate_excl_neutral_pct",
    "neutral_rate_evaluated_pct",
    "loss_rate_excl_neutral_pct",
    "avg_return_pct",
    "median_return_pct",
    "baseline_segment_id",
    "baseline_evaluated_sample_size",
    "baseline_win_rate_excl_neutral_pct",
    "baseline_neutral_rate_evaluated_pct",
    "delta_win_rate_pct_vs_all",
    "delta_neutral_rate_pct_vs_all",
    "avg_price_position_252_pct",
    "median_price_position_252_pct",
    "avg_second_arc_volume_ratio",
    "median_second_arc_volume_ratio",
    "avg_red_ratio_delta_pct",
    "median_red_ratio_delta_pct",
    "avg_neckline_distance_pct",
    "median_neckline_distance_pct",
    "avg_signal_rebound_from_right_low_pct",
    "median_signal_rebound_from_right_low_pct",
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


def num(series: pd.Series) -> pd.Series:
    return pd.to_numeric(series, errors="coerce")


def metric_series(sample: pd.DataFrame, column: str) -> pd.Series:
    if sample.empty or column not in sample.columns:
        return pd.Series(dtype=float)
    return pd.to_numeric(sample[column], errors="coerce").dropna()


def segment_specs() -> list[tuple[str, str, str, Callable[[pd.DataFrame], pd.Series]]]:
    return [
        (BASELINE_SEGMENT_ID, "segment_rate", "All evaluated early-entry rows.", lambda df: pd.Series(True, index=df.index)),
        ("outcome_win", "outcome_profile", "Rows whose result is win.", lambda df: df["outcome_result"].eq("win")),
        ("outcome_neutral", "outcome_profile", "Rows whose result is neutral.", lambda df: df["outcome_result"].eq("neutral")),
        ("outcome_loss", "outcome_profile", "Rows whose result is loss.", lambda df: df["outcome_result"].eq("loss")),
        ("core_mainstream", "segment_rate", "Taxonomy segment is core_mainstream.", lambda df: df["effective_mainstream_label"].eq("core_mainstream")),
        ("non_mainstream", "segment_rate", "Taxonomy segment is not core_mainstream.", lambda df: ~df["effective_mainstream_label"].eq("core_mainstream")),
        ("price_position_le_25", "segment_rate", "price_position_252_pct <= 25.", lambda df: num(df["price_position_252_pct"]).le(25.0)),
        ("price_position_le_40", "segment_rate", "price_position_252_pct <= 40.", lambda df: num(df["price_position_252_pct"]).le(40.0)),
        ("bottom_quartile_level", "segment_rate", "Signal is in the bottom-quartile price bucket.", lambda df: df["price_level_bucket"].eq("bottom_quartile_level")),
        ("bottom_or_low_level", "segment_rate", "Signal is bottom-quartile or low-level.", lambda df: df["price_level_bucket"].isin(["bottom_quartile_level", "low_level"])),
        ("smooth_rounded_w_like", "segment_rate", "Path quality is smooth rounded W-like.", lambda df: df["slope_curvature_category"].eq("smooth_rounded_w_like")),
        ("exclude_wv_multiple_turn", "segment_rate", "Exclude WV/WVV multiple-turn path category.", lambda df: ~df["slope_curvature_category"].eq("wv_multiple_turn_risk")),
        ("sharp_v_bottom_risk", "segment_rate", "Path category is sharp V bottom risk.", lambda df: df["slope_curvature_category"].eq("sharp_v_bottom_risk")),
        ("slope_break_discontinuous", "segment_rate", "Path category has a slope break discontinuity.", lambda df: df["slope_curvature_category"].eq("slope_break_discontinuous")),
        ("second_arc_volume_gte1_5", "segment_rate", "Second arc average volume is at least 1.5x first arc.", lambda df: num(df["second_arc_volume_ratio"]).ge(1.5)),
        ("second_red_ratio_gt_first", "segment_rate", "Second arc red-candle ratio is greater than first arc.", lambda df: num(df["red_ratio_delta_pct"]).gt(0.0)),
        ("second_red_delta_gte10", "segment_rate", "Second arc red-candle ratio is at least 10 pct points above first arc.", lambda df: num(df["red_ratio_delta_pct"]).ge(10.0)),
        ("right_rebound_5_20", "segment_rate", "Signal close is 5% to 20% above right low.", lambda df: num(df["signal_rebound_from_right_low_pct"]).between(5.0, 20.0, inclusive="both")),
        ("smooth_right_rebound_5_20", "segment_rate", "Smooth rounded W-like path and signal close is 5% to 20% above right low.", lambda df: df["slope_curvature_category"].eq("smooth_rounded_w_like") & num(df["signal_rebound_from_right_low_pct"]).between(5.0, 20.0, inclusive="both")),
        ("below_neckline_5_to_30", "segment_rate", "Signal close is 5% to 30% below neckline.", lambda df: num(df["neckline_distance_pct"]).between(-30.0, -5.0, inclusive="both")),
        ("near_neckline_m5_to_0", "segment_rate", "Signal close is within 5% below neckline.", lambda df: num(df["neckline_distance_pct"]).between(-5.0, 0.0, inclusive="both")),
        ("core_mainstream_price_le40", "segment_rate", "core_mainstream and price_position_252_pct <= 40.", lambda df: df["effective_mainstream_label"].eq("core_mainstream") & num(df["price_position_252_pct"]).le(40.0)),
        ("core_mainstream_price_le40_red_ratio_gt_first", "segment_rate", "core_mainstream, price <= 40, and second arc red ratio > first arc.", lambda df: df["effective_mainstream_label"].eq("core_mainstream") & num(df["price_position_252_pct"]).le(40.0) & num(df["red_ratio_delta_pct"]).gt(0.0)),
        ("core_mainstream_price_le40_red_delta_gte10", "segment_rate", "core_mainstream, price <= 40, and second arc red delta >= 10 pct points.", lambda df: df["effective_mainstream_label"].eq("core_mainstream") & num(df["price_position_252_pct"]).le(40.0) & num(df["red_ratio_delta_pct"]).ge(10.0)),
        ("core_mainstream_price_le40_volume_gte1_5", "segment_rate", "core_mainstream, price <= 40, and second arc volume >= 1.5x first arc.", lambda df: df["effective_mainstream_label"].eq("core_mainstream") & num(df["price_position_252_pct"]).le(40.0) & num(df["second_arc_volume_ratio"]).ge(1.5)),
        ("core_mainstream_price_le40_smooth", "segment_rate", "core_mainstream, price <= 40, and smooth rounded W-like path.", lambda df: df["effective_mainstream_label"].eq("core_mainstream") & num(df["price_position_252_pct"]).le(40.0) & df["slope_curvature_category"].eq("smooth_rounded_w_like")),
        ("core_mainstream_price_le40_exclude_wv", "segment_rate", "core_mainstream, price <= 40, and exclude WV/WVV.", lambda df: df["effective_mainstream_label"].eq("core_mainstream") & num(df["price_position_252_pct"]).le(40.0) & ~df["slope_curvature_category"].eq("wv_multiple_turn_risk")),
        ("smooth_price_le40_right_rebound_5_20", "segment_rate", "Smooth rounded W-like path, price <= 40, and signal rebound 5% to 20%.", lambda df: df["slope_curvature_category"].eq("smooth_rounded_w_like") & num(df["price_position_252_pct"]).le(40.0) & num(df["signal_rebound_from_right_low_pct"]).between(5.0, 20.0, inclusive="both")),
        ("smooth_core_mainstream_right_rebound_5_20", "segment_rate", "Smooth rounded W-like path, core_mainstream, and signal rebound 5% to 20%.", lambda df: df["slope_curvature_category"].eq("smooth_rounded_w_like") & df["effective_mainstream_label"].eq("core_mainstream") & num(df["signal_rebound_from_right_low_pct"]).between(5.0, 20.0, inclusive="both")),
        ("smooth_core_mainstream_price_le40_right_rebound_5_20", "segment_rate", "Smooth rounded W-like path, core_mainstream, price <= 40, and signal rebound 5% to 20%.", lambda df: df["slope_curvature_category"].eq("smooth_rounded_w_like") & df["effective_mainstream_label"].eq("core_mainstream") & num(df["price_position_252_pct"]).le(40.0) & num(df["signal_rebound_from_right_low_pct"]).between(5.0, 20.0, inclusive="both")),
        ("smooth_right_rebound_5_20_red_ratio_gt_first", "segment_rate", "Smooth rounded W-like path, signal rebound 5% to 20%, and second arc red ratio > first arc.", lambda df: df["slope_curvature_category"].eq("smooth_rounded_w_like") & num(df["signal_rebound_from_right_low_pct"]).between(5.0, 20.0, inclusive="both") & num(df["red_ratio_delta_pct"]).gt(0.0)),
        ("smooth_right_rebound_5_20_near_neckline", "segment_rate", "Smooth rounded W-like path, signal rebound 5% to 20%, and signal is within 5% below neckline.", lambda df: df["slope_curvature_category"].eq("smooth_rounded_w_like") & num(df["signal_rebound_from_right_low_pct"]).between(5.0, 20.0, inclusive="both") & num(df["neckline_distance_pct"]).between(-5.0, 0.0, inclusive="both")),
    ]


def metrics(sample: pd.DataFrame) -> dict[str, Any]:
    sample_size = int(len(sample))
    win_count = int(sample["outcome_result"].eq("win").sum()) if sample_size else 0
    neutral_count = int(sample["outcome_result"].eq("neutral").sum()) if sample_size else 0
    loss_count = int(sample["outcome_result"].eq("loss").sum()) if sample_size else 0
    incomplete_count = int(sample["outcome_result"].eq("incomplete").sum()) if sample_size else 0
    mature_size = win_count + loss_count
    evaluated_size = win_count + neutral_count + loss_count
    evaluated = sample[sample["outcome_result"].isin(["win", "neutral", "loss"])].copy()
    returns = metric_series(evaluated, "return_pct")
    return {
        "sample_size": sample_size,
        "evaluated_sample_size": evaluated_size,
        "mature_sample_size": mature_size,
        "win_count": win_count,
        "neutral_count": neutral_count,
        "loss_count": loss_count,
        "incomplete_count": incomplete_count,
        "win_rate_num": win_count / mature_size * 100.0 if mature_size else math.nan,
        "neutral_rate_num": neutral_count / evaluated_size * 100.0 if evaluated_size else math.nan,
        "loss_rate_num": loss_count / mature_size * 100.0 if mature_size else math.nan,
        "avg_return_num": float(returns.mean()) if len(returns) else math.nan,
        "median_return_num": float(returns.median()) if len(returns) else math.nan,
        "avg_price_position_252_pct_num": float(metric_series(sample, "price_position_252_pct").mean()) if sample_size else math.nan,
        "median_price_position_252_pct_num": float(metric_series(sample, "price_position_252_pct").median()) if sample_size else math.nan,
        "avg_second_arc_volume_ratio_num": float(metric_series(sample, "second_arc_volume_ratio").mean()) if sample_size else math.nan,
        "median_second_arc_volume_ratio_num": float(metric_series(sample, "second_arc_volume_ratio").median()) if sample_size else math.nan,
        "avg_red_ratio_delta_pct_num": float(metric_series(sample, "red_ratio_delta_pct").mean()) if sample_size else math.nan,
        "median_red_ratio_delta_pct_num": float(metric_series(sample, "red_ratio_delta_pct").median()) if sample_size else math.nan,
        "avg_neckline_distance_pct_num": float(metric_series(sample, "neckline_distance_pct").mean()) if sample_size else math.nan,
        "median_neckline_distance_pct_num": float(metric_series(sample, "neckline_distance_pct").median()) if sample_size else math.nan,
        "avg_signal_rebound_from_right_low_pct_num": float(metric_series(sample, "signal_rebound_from_right_low_pct").mean()) if sample_size else math.nan,
        "median_signal_rebound_from_right_low_pct_num": float(metric_series(sample, "signal_rebound_from_right_low_pct").median()) if sample_size else math.nan,
    }


def sample_warning(mature_size: int) -> str:
    if mature_size < 5:
        return "tiny_mature_sample_research_only"
    if mature_size < 15:
        return "low_mature_sample_research_only"
    if mature_size < 30:
        return "directional_only_below_promotion_review_size"
    return "medium_mature_sample_research_only"


def interpretation(segment_id: str, row_metrics: dict[str, Any], baseline_metrics: dict[str, Any]) -> str:
    if segment_id == BASELINE_SEGMENT_ID:
        return "baseline_reference"
    if segment_id.startswith("outcome_"):
        return "outcome_profile_reference"
    if row_metrics["mature_sample_size"] < 30:
        return "too_small_for_parameter_decision"
    win_delta = row_metrics["win_rate_num"] - baseline_metrics["win_rate_num"]
    neutral_delta = row_metrics["neutral_rate_num"] - baseline_metrics["neutral_rate_num"]
    if math.isnan(win_delta) or math.isnan(neutral_delta):
        return "insufficient_baseline_comparison"
    if win_delta >= 5.0 and neutral_delta <= 0.0:
        return "candidate_improves_win_without_more_neutral"
    if win_delta >= 5.0:
        return "improves_win_but_neutral_watch"
    if neutral_delta <= -5.0 and win_delta >= 0.0:
        return "candidate_reduces_neutral_without_losing_win_rate"
    if neutral_delta < 0.0:
        return "reduces_neutral_only"
    if win_delta > 0.0:
        return "mixed_small_win_improvement"
    return "not_better_than_all_same_event"


def output_row(
    *,
    event_set_id: str,
    outcome_rule_id: str,
    diagnostic_type: str,
    segment_id: str,
    segment_description: str,
    row_metrics: dict[str, Any],
    baseline_metrics: dict[str, Any],
    generated_at: str,
) -> dict[str, Any]:
    win_delta = row_metrics["win_rate_num"] - baseline_metrics["win_rate_num"]
    neutral_delta = row_metrics["neutral_rate_num"] - baseline_metrics["neutral_rate_num"]
    return {
        "model_id": MODEL_ID,
        "confirmation_model_id": CONFIRMATION_MODEL_ID,
        "overlay_model_id": OVERLAY_MODEL_ID,
        "research_id": RESEARCH_ID,
        "source_research_id": SOURCE_RESEARCH_ID,
        "research_variant_id": RESEARCH_VARIANT_ID,
        "advisory_status": RESEARCH_VARIANT_ID,
        "surface_id": SURFACE_ID,
        "event_set_id": event_set_id,
        "outcome_rule_id": outcome_rule_id,
        "diagnostic_type": diagnostic_type,
        "segment_id": segment_id,
        "segment_description": segment_description,
        "sample_size": row_metrics["sample_size"],
        "evaluated_sample_size": row_metrics["evaluated_sample_size"],
        "mature_sample_size": row_metrics["mature_sample_size"],
        "win_count": row_metrics["win_count"],
        "neutral_count": row_metrics["neutral_count"],
        "loss_count": row_metrics["loss_count"],
        "incomplete_count": row_metrics["incomplete_count"],
        "win_rate_excl_neutral_pct": metric_text(row_metrics["win_rate_num"]),
        "neutral_rate_evaluated_pct": metric_text(row_metrics["neutral_rate_num"]),
        "loss_rate_excl_neutral_pct": metric_text(row_metrics["loss_rate_num"]),
        "avg_return_pct": metric_text(row_metrics["avg_return_num"]),
        "median_return_pct": metric_text(row_metrics["median_return_num"]),
        "baseline_segment_id": BASELINE_SEGMENT_ID,
        "baseline_evaluated_sample_size": baseline_metrics["evaluated_sample_size"],
        "baseline_win_rate_excl_neutral_pct": metric_text(baseline_metrics["win_rate_num"]),
        "baseline_neutral_rate_evaluated_pct": metric_text(baseline_metrics["neutral_rate_num"]),
        "delta_win_rate_pct_vs_all": metric_text(win_delta),
        "delta_neutral_rate_pct_vs_all": metric_text(neutral_delta),
        "avg_price_position_252_pct": metric_text(row_metrics["avg_price_position_252_pct_num"]),
        "median_price_position_252_pct": metric_text(row_metrics["median_price_position_252_pct_num"]),
        "avg_second_arc_volume_ratio": metric_text(row_metrics["avg_second_arc_volume_ratio_num"]),
        "median_second_arc_volume_ratio": metric_text(row_metrics["median_second_arc_volume_ratio_num"]),
        "avg_red_ratio_delta_pct": metric_text(row_metrics["avg_red_ratio_delta_pct_num"]),
        "median_red_ratio_delta_pct": metric_text(row_metrics["median_red_ratio_delta_pct_num"]),
        "avg_neckline_distance_pct": metric_text(row_metrics["avg_neckline_distance_pct_num"]),
        "median_neckline_distance_pct": metric_text(row_metrics["median_neckline_distance_pct_num"]),
        "avg_signal_rebound_from_right_low_pct": metric_text(row_metrics["avg_signal_rebound_from_right_low_pct_num"]),
        "median_signal_rebound_from_right_low_pct": metric_text(row_metrics["median_signal_rebound_from_right_low_pct_num"]),
        "sample_warning": sample_warning(row_metrics["mature_sample_size"]),
        "research_interpretation": interpretation(segment_id, row_metrics, baseline_metrics),
        "approved_for_daily": "false",
        "production_readiness": PRODUCTION_READINESS,
        "generated_at": generated_at,
    }


def build_diagnostics(generated_at: str) -> pd.DataFrame:
    source = read_csv(SOURCE_DETAIL_CSV)
    required = {
        "model_id",
        "surface_id",
        "event_set_id",
        "outcome_rule_id",
        "outcome_result",
        "return_pct",
        "price_position_252_pct",
        "second_arc_volume_ratio",
        "red_ratio_delta_pct",
        "neckline_distance_pct",
        "signal_rebound_from_right_low_pct",
        "effective_mainstream_label",
        "price_level_bucket",
        "slope_curvature_category",
        "approved_for_daily",
        "production_readiness",
    }
    missing = sorted(required - set(source.columns))
    if missing:
        raise SystemExit(f"ERROR: source detail missing columns: {missing}")

    detail = source[
        source["surface_id"].eq(SURFACE_ID)
        & source["outcome_rule_id"].isin(TARGET_OUTCOME_RULES)
    ].copy()
    rows: list[dict[str, Any]] = []
    for (event_set_id, outcome_rule_id), group in detail.groupby(["event_set_id", "outcome_rule_id"], dropna=False):
        event_set_id = safe_str(event_set_id)
        outcome_rule_id = safe_str(outcome_rule_id)
        base = group.copy()
        baseline_metrics = metrics(base)
        for segment_id, diagnostic_type, description, condition in segment_specs():
            mask = condition(group).fillna(False)
            sample = group[mask].copy()
            row_metrics = metrics(sample)
            rows.append(
                output_row(
                    event_set_id=event_set_id,
                    outcome_rule_id=outcome_rule_id,
                    diagnostic_type=diagnostic_type,
                    segment_id=segment_id,
                    segment_description=description,
                    row_metrics=row_metrics,
                    baseline_metrics=baseline_metrics,
                    generated_at=generated_at,
                )
            )

    output = pd.DataFrame(rows)
    for column in OUTPUT_COLUMNS:
        if column not in output.columns:
            output[column] = ""
    forbidden = sorted(set(output.columns) & FORBIDDEN_PRODUCTION_FIELDS)
    if forbidden:
        raise SystemExit(f"ERROR: forbidden production columns in outcome diagnostics: {forbidden}")
    return output[OUTPUT_COLUMNS]


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


def write_markdown(diagnostics: pd.DataFrame, generated_at: str) -> None:
    variant = diagnostics[
        diagnostics["event_set_id"].eq("variant_nearest_micro_45d_event_replay")
        & diagnostics["outcome_rule_id"].eq("tp10_or_neutral_after_5pct_close_40d")
        & diagnostics["diagnostic_type"].eq("segment_rate")
    ].copy()
    variant["mature_sort"] = pd.to_numeric(variant["mature_sample_size"], errors="coerce")
    variant["win_sort"] = pd.to_numeric(variant["win_rate_excl_neutral_pct"], errors="coerce")
    variant["neutral_sort"] = pd.to_numeric(variant["neutral_rate_evaluated_pct"], errors="coerce")
    variant["delta_win_sort"] = pd.to_numeric(variant["delta_win_rate_pct_vs_all"], errors="coerce")
    candidate = variant[variant["mature_sort"].ge(30)].sort_values(
        ["win_sort", "neutral_sort", "delta_win_sort"], ascending=[False, True, False]
    )

    profiles = diagnostics[
        diagnostics["event_set_id"].eq("variant_nearest_micro_45d_event_replay")
        & diagnostics["outcome_rule_id"].eq("tp10_or_neutral_after_5pct_close_40d")
        & diagnostics["diagnostic_type"].eq("outcome_profile")
    ].copy()
    strict = diagnostics[
        diagnostics["event_set_id"].eq("variant_nearest_micro_45d_event_replay")
        & diagnostics["outcome_rule_id"].eq("tp10_or_neutral_after_5pct_close_40d")
        & diagnostics["segment_id"].isin(STRICT_SMOOTH_REBOUND_SEGMENTS)
    ].copy()
    strict["segment_order"] = strict["segment_id"].map(
        {segment_id: idx for idx, segment_id in enumerate(STRICT_SMOOTH_REBOUND_SEGMENTS)}
    )
    strict = strict.sort_values("segment_order")

    lines = [
        "# W-Bottom Early-Entry Outcome Diagnostics",
        "",
        f"- generated_at: `{generated_at}`",
        f"- source_research_id: `{SOURCE_RESEARCH_ID}`",
        "- production impact: `none`",
        "- surface: `w_bottom_right_low_early_entry` only.",
        "- purpose: separate +10% wins, +5%-then-back-to-5% neutral rows, and losses for the right-low early-entry model.",
        "- rates: `win_rate_excl_neutral_pct` excludes neutral rows from the win/loss denominator; `neutral_rate_evaluated_pct` uses win+neutral+loss as denominator.",
        "",
        "## Variant Neutral Rule Candidate Segments",
        "",
        *markdown_table(
            candidate,
            [
                "segment_id",
                "sample_size",
                "evaluated_sample_size",
                "mature_sample_size",
                "win_count",
                "neutral_count",
                "loss_count",
                "win_rate_excl_neutral_pct",
                "neutral_rate_evaluated_pct",
                "delta_win_rate_pct_vs_all",
                "delta_neutral_rate_pct_vs_all",
                "research_interpretation",
            ],
            30,
        ),
        "",
        "## Variant Outcome Feature Profiles",
        "",
        *markdown_table(
            profiles,
            [
                "segment_id",
                "sample_size",
                "avg_price_position_252_pct",
                "median_price_position_252_pct",
                "avg_second_arc_volume_ratio",
                "avg_red_ratio_delta_pct",
                "avg_neckline_distance_pct",
                "avg_signal_rebound_from_right_low_pct",
            ],
            10,
        ),
        "",
        "## Strict Smooth-Rebound Segments",
        "",
        *markdown_table(
            strict,
            [
                "segment_id",
                "sample_size",
                "evaluated_sample_size",
                "mature_sample_size",
                "win_count",
                "neutral_count",
                "loss_count",
                "win_rate_excl_neutral_pct",
                "neutral_rate_evaluated_pct",
                "sample_warning",
                "research_interpretation",
            ],
            20,
        ),
        "",
        "## Guardrails",
        "",
        "- This is research/backtest advisory-only work.",
        "- Rows remain `approved_for_daily=false` and `warning_research_variant_only`.",
        "- This diagnostic does not modify production conditions, scoring, ranking, PDFs, baselines, or daily_full_pipeline.",
        "- Strong-looking segments are research candidates only; they are not production rules.",
    ]
    LATEST_MD.parent.mkdir(parents=True, exist_ok=True)
    LATEST_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    generated_at = now_text()
    diagnostics = build_diagnostics(generated_at)
    if diagnostics.empty:
        raise SystemExit("ERROR: W-bottom early-entry outcome diagnostics generated no rows")
    write_csv(diagnostics, LATEST_CSV)
    write_csv(diagnostics, HISTORY_CSV)
    write_markdown(diagnostics, generated_at)
    print(f"Saved: {LATEST_CSV} rows={len(diagnostics)}")
    print(f"Saved: {LATEST_MD}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
