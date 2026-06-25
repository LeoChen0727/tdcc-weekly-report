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

SOURCE_DETAIL_CSV = RESEARCH_LATEST_DIR / "w_bottom_price_level_audit_detail_latest.csv"

LATEST_GRID_CSV = RESEARCH_LATEST_DIR / "w_bottom_price_level_filter_grid_latest.csv"
LATEST_GRID_MD = RESEARCH_LATEST_DIR / "w_bottom_price_level_filter_grid_latest.md"
HISTORY_GRID_CSV = RESEARCH_HISTORY_DIR / "w_bottom_price_level_filter_grid.csv"

MODEL_ID = "w_bottom_right_side"
CONFIRMATION_MODEL_ID = "neckline_volume_breakout_confirmation"
RESEARCH_ID = "w_bottom_price_level_filter_grid"
SOURCE_RESEARCH_ID = "w_bottom_price_level_audit"
RESEARCH_VARIANT_ID = "warning_research_variant_only"
PARAMETER_SET_ID = "w_bottom_price_level_filter_grid_20260625"

PRICE_POSITION_MAX_PCT = 40.0
OBSERVATION_TO_VOLUME = "observation_to_volume_confirmation"
WV_CATEGORY = "wv_multiple_turn_risk"
BASELINE_FILTER_ID = "baseline_no_price_level_filter"
PRICE_FILTER_ID = "price_position_252_le_40"
MIN_MATURE_FOR_DIRECTION = 5
PROMOTION_REVIEW_MIN_MATURE = 30

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
    "research_id",
    "source_research_id",
    "research_variant_id",
    "parameter_set_id",
    "advisory_status",
    "base_scope_id",
    "base_scope_description",
    "segment_dimension",
    "segment_value",
    "filter_id",
    "filter_description",
    "price_position_max_pct",
    "sample_size",
    "mature_sample_size",
    "win_count",
    "win_rate_pct",
    "avg_a_return_pct",
    "median_a_return_pct",
    "baseline_sample_size",
    "baseline_mature_sample_size",
    "baseline_win_rate_pct",
    "baseline_avg_a_return_pct",
    "baseline_median_a_return_pct",
    "delta_sample_size",
    "sample_retention_rate_pct",
    "delta_win_rate_pct",
    "delta_avg_a_return_pct",
    "delta_median_a_return_pct",
    "volume_confirmation_count",
    "tdcc_any_age7_count",
    "smooth_count",
    "sharp_v_count",
    "wv_multiple_turn_count",
    "slope_break_count",
    "bottom_quartile_count",
    "low_level_count",
    "mid_level_count",
    "high_level_count",
    "avg_price_position_252_pct",
    "median_price_position_252_pct",
    "stability_signal",
    "sample_warning",
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


def normalize_code(value: Any) -> str:
    text = safe_str(value)
    if text.endswith(".0"):
        text = text[:-2]
    return text.zfill(4) if text.isdigit() and len(text) < 4 else text


def normalize_date(value: Any) -> str:
    digits = "".join(ch for ch in safe_str(value) if ch.isdigit())
    return digits[:8]


def pct_text(value: float) -> str:
    if math.isnan(value) or math.isinf(value):
        return ""
    return f"{value:.4f}"


def read_source() -> pd.DataFrame:
    if not SOURCE_DETAIL_CSV.exists():
        raise SystemExit(f"ERROR: missing required input: {SOURCE_DETAIL_CSV}")
    detail = pd.read_csv(SOURCE_DETAIL_CSV, dtype=str, keep_default_na=False)
    required = {
        "stock_id",
        "signal_date",
        "transition_status",
        "slope_curvature_category",
        "a_mature",
        "a_return_pct",
        "tdcc_any_age7",
        "effective_mainstream_label",
        "price_position_252_pct",
        "price_level_bucket",
        "approved_for_daily",
        "production_readiness",
    }
    missing = sorted(required - set(detail.columns))
    if missing:
        raise SystemExit(f"ERROR: price-level audit detail missing columns: {missing}")
    detail = detail.copy()
    detail["stock_id"] = detail["stock_id"].map(normalize_code)
    detail["signal_date"] = detail["signal_date"].map(normalize_date)
    detail["signal_quarter"] = pd.to_datetime(detail["signal_date"], format="%Y%m%d", errors="coerce").dt.to_period("Q").astype(str)
    detail["signal_quarter"] = detail["signal_quarter"].replace("NaT", "unknown_quarter")
    detail["effective_mainstream_label"] = detail["effective_mainstream_label"].map(
        lambda value: safe_str(value) or "taxonomy_missing"
    )
    return detail


def write_csv(df: pd.DataFrame, path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(path, index=False, encoding="utf-8-sig")


def base_scope_specs() -> list[tuple[str, str, Callable[[pd.DataFrame], pd.Series]]]:
    return [
        (
            "all_w_bottom_candidates",
            "All W-bottom right-side candidates from the price-level audit.",
            lambda df: pd.Series(True, index=df.index),
        ),
        (
            "observation_to_volume_confirmation",
            "Candidates that started as right-side observation and later confirmed by neckline volume breakout.",
            lambda df: df["transition_status"].eq(OBSERVATION_TO_VOLUME),
        ),
        (
            "observation_volume_exclude_wv",
            "Observation-to-volume-confirmation candidates excluding WV/WVV multiple-turn paths.",
            lambda df: df["transition_status"].eq(OBSERVATION_TO_VOLUME) & ~df["slope_curvature_category"].eq(WV_CATEGORY),
        ),
        (
            "core_mainstream_observation_volume_exclude_wv",
            "Core-mainstream observation-to-volume-confirmation candidates excluding WV/WVV paths.",
            lambda df: df["transition_status"].eq(OBSERVATION_TO_VOLUME)
            & ~df["slope_curvature_category"].eq(WV_CATEGORY)
            & df["effective_mainstream_label"].eq("core_mainstream"),
        ),
    ]


def segment_specs(df: pd.DataFrame) -> list[tuple[str, str, pd.Series]]:
    specs: list[tuple[str, str, pd.Series]] = [
        ("overall", "all", pd.Series(True, index=df.index)),
    ]
    for column in ["signal_quarter", "effective_mainstream_label"]:
        for value in sorted(set(df[column].astype(str))):
            if not value:
                continue
            specs.append((column, value, df[column].astype(str).eq(value)))
    return specs


def filter_specs() -> list[tuple[str, str, Callable[[pd.DataFrame], pd.Series]]]:
    return [
        (
            BASELINE_FILTER_ID,
            "Baseline rows inside the base scope and segment, without an additional price-position filter.",
            lambda df: pd.Series(True, index=df.index),
        ),
        (
            PRICE_FILTER_ID,
            f"Keep only rows with price_position_252_pct <= {PRICE_POSITION_MAX_PCT}.",
            lambda df: pd.to_numeric(df["price_position_252_pct"], errors="coerce").le(PRICE_POSITION_MAX_PCT),
        ),
    ]


def metrics_for(sample: pd.DataFrame) -> dict[str, Any]:
    mature = sample[sample["a_mature"].map(bool_value)].copy() if not sample.empty else pd.DataFrame()
    returns = pd.to_numeric(mature["a_return_pct"], errors="coerce").dropna() if not mature.empty else pd.Series(dtype=float)
    positions = pd.to_numeric(sample["price_position_252_pct"], errors="coerce").dropna() if not sample.empty else pd.Series(dtype=float)
    buckets = sample["price_level_bucket"].value_counts().to_dict() if not sample.empty else {}
    categories = sample["slope_curvature_category"].value_counts().to_dict() if not sample.empty else {}
    sample_size = int(len(sample))
    volume_count = int(sample["transition_status"].eq(OBSERVATION_TO_VOLUME).sum()) if sample_size else 0
    return {
        "sample_size": sample_size,
        "mature_sample_size": int(len(returns)),
        "win_count": int(returns.gt(0).sum()),
        "win_rate_num": float(returns.gt(0).mean() * 100.0) if len(returns) else math.nan,
        "avg_a_return_pct_num": float(returns.mean()) if len(returns) else math.nan,
        "median_a_return_pct_num": float(returns.median()) if len(returns) else math.nan,
        "volume_confirmation_count": volume_count,
        "tdcc_any_age7_count": int(sample["tdcc_any_age7"].map(bool_value).sum()) if sample_size else 0,
        "smooth_count": int(categories.get("smooth_rounded_w_like", 0)),
        "sharp_v_count": int(categories.get("sharp_v_bottom_risk", 0)),
        "wv_multiple_turn_count": int(categories.get("wv_multiple_turn_risk", 0)),
        "slope_break_count": int(categories.get("slope_break_discontinuous", 0)),
        "bottom_quartile_count": int(buckets.get("bottom_quartile_level", 0)),
        "low_level_count": int(buckets.get("low_level", 0)),
        "mid_level_count": int(buckets.get("mid_level", 0)),
        "high_level_count": int(buckets.get("high_level", 0)),
        "avg_price_position_252_pct_num": float(positions.mean()) if len(positions) else math.nan,
        "median_price_position_252_pct_num": float(positions.median()) if len(positions) else math.nan,
    }


def sample_warning(mature_count: int) -> str:
    if mature_count < MIN_MATURE_FOR_DIRECTION:
        return "too_small_for_directional_read"
    if mature_count < PROMOTION_REVIEW_MIN_MATURE:
        return "directional_only_below_promotion_review_size"
    return "sample_size_ok_for_research_review"


def stability_signal(filter_id: str, current: dict[str, Any], baseline: dict[str, Any]) -> str:
    if filter_id == BASELINE_FILTER_ID:
        return "baseline"
    mature = int(current["mature_sample_size"])
    if mature < MIN_MATURE_FOR_DIRECTION:
        return "insufficient_sample"
    delta_win = safe_float(current["delta_win_rate_pct"])
    delta_avg = safe_float(current["delta_avg_a_return_pct"])
    delta_median = safe_float(current["delta_median_a_return_pct"])
    if delta_win > 0 and delta_avg > 0 and delta_median >= 0:
        return "directionally_improved"
    if delta_win > 0 and delta_avg > 0:
        return "improved_but_median_still_weak"
    if delta_win >= 0 and delta_avg >= 0:
        return "mixed_flat_to_slightly_better"
    return "not_improved"


def build_grid(generated_at: str) -> pd.DataFrame:
    source = read_source()
    rows: list[dict[str, Any]] = []
    for base_scope_id, base_description, base_predicate in base_scope_specs():
        base_scope = source[base_predicate(source)].copy()
        for segment_dimension, segment_value, segment_predicate in segment_specs(base_scope):
            segment = base_scope[segment_predicate].copy()
            if segment.empty:
                continue
            baseline_sample = segment.copy()
            baseline_metrics = metrics_for(baseline_sample)
            for filter_id, filter_description, filter_predicate in filter_specs():
                sample = segment[filter_predicate(segment)].copy()
                current_metrics = metrics_for(sample)
                sample_retention = (
                    current_metrics["sample_size"] / baseline_metrics["sample_size"] * 100.0
                    if baseline_metrics["sample_size"]
                    else math.nan
                )
                delta_win = (
                    current_metrics["win_rate_num"] - baseline_metrics["win_rate_num"]
                    if not math.isnan(current_metrics["win_rate_num"]) and not math.isnan(baseline_metrics["win_rate_num"])
                    else math.nan
                )
                delta_avg = (
                    current_metrics["avg_a_return_pct_num"] - baseline_metrics["avg_a_return_pct_num"]
                    if not math.isnan(current_metrics["avg_a_return_pct_num"])
                    and not math.isnan(baseline_metrics["avg_a_return_pct_num"])
                    else math.nan
                )
                delta_median = (
                    current_metrics["median_a_return_pct_num"] - baseline_metrics["median_a_return_pct_num"]
                    if not math.isnan(current_metrics["median_a_return_pct_num"])
                    and not math.isnan(baseline_metrics["median_a_return_pct_num"])
                    else math.nan
                )
                row = {
                    "model_id": MODEL_ID,
                    "confirmation_model_id": CONFIRMATION_MODEL_ID,
                    "research_id": RESEARCH_ID,
                    "source_research_id": SOURCE_RESEARCH_ID,
                    "research_variant_id": RESEARCH_VARIANT_ID,
                    "parameter_set_id": PARAMETER_SET_ID,
                    "advisory_status": RESEARCH_VARIANT_ID,
                    "base_scope_id": base_scope_id,
                    "base_scope_description": base_description,
                    "segment_dimension": segment_dimension,
                    "segment_value": segment_value,
                    "filter_id": filter_id,
                    "filter_description": filter_description,
                    "price_position_max_pct": "" if filter_id == BASELINE_FILTER_ID else PRICE_POSITION_MAX_PCT,
                    "sample_size": current_metrics["sample_size"],
                    "mature_sample_size": current_metrics["mature_sample_size"],
                    "win_count": current_metrics["win_count"],
                    "win_rate_pct": pct_text(current_metrics["win_rate_num"]),
                    "avg_a_return_pct": pct_text(current_metrics["avg_a_return_pct_num"]),
                    "median_a_return_pct": pct_text(current_metrics["median_a_return_pct_num"]),
                    "baseline_sample_size": baseline_metrics["sample_size"],
                    "baseline_mature_sample_size": baseline_metrics["mature_sample_size"],
                    "baseline_win_rate_pct": pct_text(baseline_metrics["win_rate_num"]),
                    "baseline_avg_a_return_pct": pct_text(baseline_metrics["avg_a_return_pct_num"]),
                    "baseline_median_a_return_pct": pct_text(baseline_metrics["median_a_return_pct_num"]),
                    "delta_sample_size": current_metrics["sample_size"] - baseline_metrics["sample_size"],
                    "sample_retention_rate_pct": pct_text(sample_retention),
                    "delta_win_rate_pct": pct_text(delta_win),
                    "delta_avg_a_return_pct": pct_text(delta_avg),
                    "delta_median_a_return_pct": pct_text(delta_median),
                    "volume_confirmation_count": current_metrics["volume_confirmation_count"],
                    "tdcc_any_age7_count": current_metrics["tdcc_any_age7_count"],
                    "smooth_count": current_metrics["smooth_count"],
                    "sharp_v_count": current_metrics["sharp_v_count"],
                    "wv_multiple_turn_count": current_metrics["wv_multiple_turn_count"],
                    "slope_break_count": current_metrics["slope_break_count"],
                    "bottom_quartile_count": current_metrics["bottom_quartile_count"],
                    "low_level_count": current_metrics["low_level_count"],
                    "mid_level_count": current_metrics["mid_level_count"],
                    "high_level_count": current_metrics["high_level_count"],
                    "avg_price_position_252_pct": pct_text(current_metrics["avg_price_position_252_pct_num"]),
                    "median_price_position_252_pct": pct_text(current_metrics["median_price_position_252_pct_num"]),
                    "sample_warning": sample_warning(current_metrics["mature_sample_size"]),
                    "approved_for_daily": "false",
                    "production_readiness": "not_production_ready_research_only",
                    "generated_at": generated_at,
                }
                row["stability_signal"] = stability_signal(filter_id, row, baseline_metrics)
                rows.append(row)
    grid = pd.DataFrame(rows)
    for column in OUTPUT_COLUMNS:
        if column not in grid.columns:
            grid[column] = ""
    forbidden = sorted(set(grid.columns) & FORBIDDEN_PRODUCTION_FIELDS)
    if forbidden:
        raise SystemExit(f"ERROR: forbidden production columns in price-level filter grid: {forbidden}")
    return grid[OUTPUT_COLUMNS]


def markdown_table(df: pd.DataFrame, columns: list[str], limit: int = 80) -> list[str]:
    if df.empty:
        return ["_No rows._"]
    lines = ["| " + " | ".join(columns) + " |", "| " + " | ".join(["---"] * len(columns)) + " |"]
    for _, row in df.loc[:, columns].head(limit).iterrows():
        lines.append("| " + " | ".join(safe_str(row.get(column)) for column in columns) + " |")
    return lines


def write_markdown(grid: pd.DataFrame, generated_at: str) -> None:
    overall = grid[grid["segment_dimension"].eq("overall")].copy()
    price_filter = grid[grid["filter_id"].eq(PRICE_FILTER_ID)].copy()
    stability_counts = (
        price_filter.groupby(["base_scope_id", "stability_signal"], dropna=False)
        .size()
        .reset_index(name="segment_count")
        .sort_values(["base_scope_id", "stability_signal"])
    )
    quarters = price_filter[price_filter["segment_dimension"].eq("signal_quarter")].copy()
    mainstream = price_filter[price_filter["segment_dimension"].eq("effective_mainstream_label")].copy()
    lines = [
        "# W-Bottom Price-Level Filter Grid",
        "",
        f"- generated_at: `{generated_at}`",
        f"- model_id: `{MODEL_ID}`",
        f"- confirmation_model_id: `{CONFIRMATION_MODEL_ID}`",
        f"- source_research_id: `{SOURCE_RESEARCH_ID}`",
        f"- filter_candidate: `{PRICE_FILTER_ID}`",
        f"- rule: `price_position_252_pct <= {PRICE_POSITION_MAX_PCT}`",
        f"- rows: `{len(grid)}`",
        f"- advisory_status: `{RESEARCH_VARIANT_ID}`",
        "- production impact: `none`; this grid does not update production model conditions, scoring, ranking, or baseline.",
        "- interpretation boundary: this is a research filter candidate and must not be promoted without a separate model-change PR.",
        "",
        "## Overall Base-Scope Comparison",
        "",
        *markdown_table(
            overall,
            [
                "base_scope_id",
                "filter_id",
                "sample_size",
                "mature_sample_size",
                "win_rate_pct",
                "avg_a_return_pct",
                "median_a_return_pct",
                "baseline_mature_sample_size",
                "delta_win_rate_pct",
                "delta_avg_a_return_pct",
                "sample_retention_rate_pct",
                "stability_signal",
                "sample_warning",
            ],
            limit=40,
        ),
        "",
        "## Price Filter Stability Counts",
        "",
        *markdown_table(stability_counts, ["base_scope_id", "stability_signal", "segment_count"], limit=80),
        "",
        "## Price Filter By Quarter",
        "",
        *markdown_table(
            quarters,
            [
                "base_scope_id",
                "segment_value",
                "sample_size",
                "mature_sample_size",
                "win_rate_pct",
                "avg_a_return_pct",
                "baseline_mature_sample_size",
                "delta_win_rate_pct",
                "delta_avg_a_return_pct",
                "stability_signal",
                "sample_warning",
            ],
            limit=80,
        ),
        "",
        "## Price Filter By Mainstream Label",
        "",
        *markdown_table(
            mainstream,
            [
                "base_scope_id",
                "segment_value",
                "sample_size",
                "mature_sample_size",
                "win_rate_pct",
                "avg_a_return_pct",
                "baseline_mature_sample_size",
                "delta_win_rate_pct",
                "delta_avg_a_return_pct",
                "stability_signal",
                "sample_warning",
            ],
            limit=80,
        ),
        "",
        "## Reading Notes",
        "",
        "- `sample_retention_rate_pct` shows how much sample remains after requiring bottom/low level.",
        "- A positive directional read is not enough for production if mature sample size remains below promotion review size.",
        "- This grid tests price level only; path shape quality and neckline-volume confirmation remain separate research gates.",
    ]
    LATEST_GRID_MD.parent.mkdir(parents=True, exist_ok=True)
    LATEST_GRID_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    generated_at = now_text()
    grid = build_grid(generated_at)
    if grid.empty:
        raise SystemExit("ERROR: price-level filter grid produced no rows")
    write_csv(grid, LATEST_GRID_CSV)
    write_csv(grid, HISTORY_GRID_CSV)
    write_markdown(grid, generated_at)
    print(f"Saved: {LATEST_GRID_CSV} rows={len(grid)}")
    print(f"Saved: {LATEST_GRID_MD}")
    print(f"Saved: {HISTORY_GRID_CSV} rows={len(grid)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
