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

SOURCE_DETAIL_CSV = RESEARCH_LATEST_DIR / "w_bottom_path_quality_filter_audit_detail_latest.csv"
SOURCE_TAXONOMY_CSV = ROOT / "output" / "latest" / "stock_theme_taxonomy_latest.csv"

LATEST_GRID_CSV = RESEARCH_LATEST_DIR / "w_bottom_wv_filter_stability_grid_latest.csv"
LATEST_GRID_MD = RESEARCH_LATEST_DIR / "w_bottom_wv_filter_stability_grid_latest.md"
HISTORY_GRID_CSV = RESEARCH_HISTORY_DIR / "w_bottom_wv_filter_stability_grid.csv"

MODEL_ID = "w_bottom_right_side"
CONFIRMATION_MODEL_ID = "neckline_volume_breakout_confirmation"
RESEARCH_ID = "w_bottom_wv_filter_stability_grid"
SOURCE_RESEARCH_ID = "w_bottom_path_quality_filter_audit"
RESEARCH_VARIANT_ID = "warning_research_variant_only"
PARAMETER_SET_ID = "w_bottom_wv_filter_stability_grid_20260625"

BASELINE_FILTER_ID = "observation_to_volume_confirmation"
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
    "filter_id",
    "filter_description",
    "segment_dimension",
    "segment_value",
    "segment_source",
    "has_taxonomy",
    "baseline_filter_id",
    "sample_size",
    "mature_sample_size",
    "win_count",
    "win_rate",
    "avg_a_return_pct",
    "median_a_return_pct",
    "baseline_sample_size",
    "baseline_mature_sample_size",
    "baseline_win_rate",
    "baseline_avg_a_return_pct",
    "baseline_median_a_return_pct",
    "delta_sample_size",
    "sample_retention_rate",
    "delta_win_rate_pct",
    "delta_avg_a_return_pct",
    "delta_median_a_return_pct",
    "smooth_count",
    "sharp_v_count",
    "wv_multiple_turn_count",
    "slope_break_count",
    "tdcc_any_age7_count",
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


def write_csv(df: pd.DataFrame, path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(path, index=False, encoding="utf-8-sig")


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
        "approved_for_daily",
    }
    missing = sorted(required - set(detail.columns))
    if missing:
        raise SystemExit(f"ERROR: path quality detail missing columns: {missing}")
    detail = detail.copy()
    detail["stock_id"] = detail["stock_id"].map(normalize_code)
    detail["signal_date"] = detail["signal_date"].map(normalize_date)
    detail["signal_month"] = detail["signal_date"].str.slice(0, 6)
    detail["signal_month"] = detail["signal_month"].map(lambda value: f"{value[:4]}-{value[4:6]}" if len(value) == 6 else "unknown_month")
    signal_dt = pd.to_datetime(detail["signal_date"], format="%Y%m%d", errors="coerce")
    detail["signal_quarter"] = signal_dt.dt.to_period("Q").astype(str).replace("NaT", "unknown_quarter")
    detail["signal_half"] = signal_dt.map(lambda value: f"{value.year}H{1 if value.month <= 6 else 2}" if not pd.isna(value) else "unknown_half")

    taxonomy_status = "taxonomy_missing"
    if SOURCE_TAXONOMY_CSV.exists():
        taxonomy = pd.read_csv(SOURCE_TAXONOMY_CSV, dtype=str, keep_default_na=False)
        if "stock_id" in taxonomy.columns:
            taxonomy_status = "taxonomy_joined"
            taxonomy = taxonomy.copy()
            taxonomy["stock_id"] = taxonomy["stock_id"].map(normalize_code)
            wanted = [
                "stock_id",
                "effective_mainstream_label",
                "has_hot_theme",
                "structural_theme_bucket",
                "taxonomy_source",
                "confidence",
            ]
            for column in wanted:
                if column not in taxonomy.columns:
                    taxonomy[column] = ""
            detail = detail.merge(taxonomy[wanted], on="stock_id", how="left")

    detail["taxonomy_join_status"] = taxonomy_status
    if "effective_mainstream_label" not in detail.columns:
        detail["effective_mainstream_label"] = ""
    if "has_hot_theme" not in detail.columns:
        detail["has_hot_theme"] = ""
    if "structural_theme_bucket" not in detail.columns:
        detail["structural_theme_bucket"] = ""
    if "taxonomy_source" not in detail.columns:
        detail["taxonomy_source"] = ""

    detail["effective_mainstream_label"] = detail["effective_mainstream_label"].map(lambda value: safe_str(value) or "taxonomy_missing")
    detail["has_hot_theme"] = detail["has_hot_theme"].map(lambda value: safe_str(value).lower() if safe_str(value) else "taxonomy_missing")
    detail["structural_theme_bucket"] = detail["structural_theme_bucket"].map(lambda value: safe_str(value) or "theme_unknown")
    detail["taxonomy_source"] = detail["taxonomy_source"].map(lambda value: safe_str(value) or "taxonomy_missing")
    return detail


def filter_specs() -> list[tuple[str, str, Callable[[pd.DataFrame], pd.Series]]]:
    return [
        (
            BASELINE_FILTER_ID,
            "Baseline: candidates that started in the right-side observation zone and later confirmed by neckline volume breakout.",
            lambda df: df["transition_status"].eq("observation_to_volume_confirmation"),
        ),
        (
            "exclude_wv_multiple_turn",
            "Baseline excluding WV/WVV multiple-turn paths.",
            lambda df: df["transition_status"].eq("observation_to_volume_confirmation")
            & ~df["slope_curvature_category"].eq("wv_multiple_turn_risk"),
        ),
        (
            "exclude_slope_break",
            "Baseline excluding slope-break or discontinuous paths.",
            lambda df: df["transition_status"].eq("observation_to_volume_confirmation")
            & ~df["slope_curvature_category"].eq("slope_break_discontinuous"),
        ),
        (
            "exclude_wv_or_slope_break",
            "Baseline excluding WV/WVV and slope-break paths.",
            lambda df: df["transition_status"].eq("observation_to_volume_confirmation")
            & ~df["slope_curvature_category"].isin(["wv_multiple_turn_risk", "slope_break_discontinuous"]),
        ),
        (
            "exclude_sharp_v",
            "Baseline excluding sharp V low reversals.",
            lambda df: df["transition_status"].eq("observation_to_volume_confirmation")
            & ~df["slope_curvature_category"].eq("sharp_v_bottom_risk"),
        ),
        (
            "smooth_only",
            "Baseline keeping only smooth rounded W-like paths.",
            lambda df: df["transition_status"].eq("observation_to_volume_confirmation")
            & df["slope_curvature_category"].eq("smooth_rounded_w_like"),
        ),
    ]


def segment_specs(df: pd.DataFrame) -> list[tuple[str, str, str, pd.Series, bool]]:
    specs: list[tuple[str, str, str, pd.Series, bool]] = [
        ("overall", "all", "all", pd.Series(True, index=df.index), False),
    ]
    for column, source, has_taxonomy in [
        ("signal_month", "time", False),
        ("signal_quarter", "time", False),
        ("signal_half", "time", False),
        ("effective_mainstream_label", "taxonomy", True),
        ("has_hot_theme", "taxonomy", True),
        ("structural_theme_bucket", "taxonomy", True),
    ]:
        values = sorted(set(df[column].astype(str)))
        for value in values:
            if not value:
                continue
            specs.append((column, value, source, df[column].astype(str).eq(value), has_taxonomy))
    return specs


def pct_text(value: float) -> str:
    if math.isnan(value):
        return ""
    return f"{value:.2f}%"


def number_text(value: float) -> str:
    if math.isnan(value):
        return ""
    return f"{value:.4f}"


def metrics_for(sample: pd.DataFrame) -> dict[str, Any]:
    mature_mask = sample["a_mature"].map(bool_value) if not sample.empty else pd.Series(dtype=bool)
    returns = pd.to_numeric(sample.loc[mature_mask, "a_return_pct"], errors="coerce") if not sample.empty else pd.Series(dtype=float)
    returns = returns.dropna()
    mature = int(len(returns))
    wins = int(returns.gt(0).sum())
    categories = sample["slope_curvature_category"].value_counts().to_dict() if not sample.empty else {}
    return {
        "sample_size": int(len(sample)),
        "mature_sample_size": mature,
        "win_count": wins,
        "win_rate_num": wins / mature * 100.0 if mature else math.nan,
        "avg_a_return_pct_num": float(returns.mean()) if not returns.empty else math.nan,
        "median_a_return_pct_num": float(returns.median()) if not returns.empty else math.nan,
        "smooth_count": int(categories.get("smooth_rounded_w_like", 0)),
        "sharp_v_count": int(categories.get("sharp_v_bottom_risk", 0)),
        "wv_multiple_turn_count": int(categories.get("wv_multiple_turn_risk", 0)),
        "slope_break_count": int(categories.get("slope_break_discontinuous", 0)),
        "tdcc_any_age7_count": int(sample["tdcc_any_age7"].map(bool_value).sum()) if not sample.empty else 0,
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
    filters = filter_specs()
    for segment_dimension, segment_value, segment_source, segment_mask, segment_has_taxonomy in segment_specs(source):
        segment = source[segment_mask].copy()
        baseline_predicate = filters[0][2]
        baseline_sample = segment[baseline_predicate(segment)].copy()
        baseline_metrics = metrics_for(baseline_sample)
        for filter_id, description, predicate in filters:
            sample = segment[predicate(segment)].copy()
            current_metrics = metrics_for(sample)
            delta_sample = current_metrics["sample_size"] - baseline_metrics["sample_size"]
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
                "filter_id": filter_id,
                "filter_description": description,
                "segment_dimension": segment_dimension,
                "segment_value": segment_value,
                "segment_source": segment_source,
                "has_taxonomy": bool_text(segment_has_taxonomy and source["taxonomy_join_status"].astype(str).eq("taxonomy_joined").any()),
                "baseline_filter_id": BASELINE_FILTER_ID,
                "sample_size": current_metrics["sample_size"],
                "mature_sample_size": current_metrics["mature_sample_size"],
                "win_count": current_metrics["win_count"],
                "win_rate": pct_text(current_metrics["win_rate_num"]),
                "avg_a_return_pct": number_text(current_metrics["avg_a_return_pct_num"]),
                "median_a_return_pct": number_text(current_metrics["median_a_return_pct_num"]),
                "baseline_sample_size": baseline_metrics["sample_size"],
                "baseline_mature_sample_size": baseline_metrics["mature_sample_size"],
                "baseline_win_rate": pct_text(baseline_metrics["win_rate_num"]),
                "baseline_avg_a_return_pct": number_text(baseline_metrics["avg_a_return_pct_num"]),
                "baseline_median_a_return_pct": number_text(baseline_metrics["median_a_return_pct_num"]),
                "delta_sample_size": delta_sample,
                "sample_retention_rate": pct_text(sample_retention),
                "delta_win_rate_pct": number_text(delta_win),
                "delta_avg_a_return_pct": number_text(delta_avg),
                "delta_median_a_return_pct": number_text(delta_median),
                "smooth_count": current_metrics["smooth_count"],
                "sharp_v_count": current_metrics["sharp_v_count"],
                "wv_multiple_turn_count": current_metrics["wv_multiple_turn_count"],
                "slope_break_count": current_metrics["slope_break_count"],
                "tdcc_any_age7_count": current_metrics["tdcc_any_age7_count"],
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
        raise SystemExit(f"ERROR: forbidden production columns in stability grid: {forbidden}")
    return grid[OUTPUT_COLUMNS]


def markdown_table(data: pd.DataFrame, columns: list[str], limit: int = 40) -> list[str]:
    if data.empty:
        return ["_No rows._"]
    lines = ["| " + " | ".join(columns) + " |", "| " + " | ".join(["---"] * len(columns)) + " |"]
    for _, row in data.loc[:, columns].head(limit).iterrows():
        lines.append("| " + " | ".join(safe_str(row.get(column)) for column in columns) + " |")
    return lines


def write_markdown(grid: pd.DataFrame, generated_at: str) -> None:
    overall = grid[grid["segment_dimension"].eq("overall")].copy()
    exclude_wv = grid[grid["filter_id"].eq("exclude_wv_multiple_turn")].copy()
    stable_counts = (
        exclude_wv.groupby(["segment_dimension", "stability_signal"], dropna=False)
        .size()
        .reset_index(name="segment_count")
        .sort_values(["segment_dimension", "stability_signal"])
    )
    month = exclude_wv[exclude_wv["segment_dimension"].eq("signal_month")].copy()
    quarter = exclude_wv[exclude_wv["segment_dimension"].eq("signal_quarter")].copy()
    mainstream = exclude_wv[exclude_wv["segment_dimension"].eq("effective_mainstream_label")].copy()
    hot_theme = exclude_wv[exclude_wv["segment_dimension"].eq("has_hot_theme")].copy()
    theme = exclude_wv[exclude_wv["segment_dimension"].eq("structural_theme_bucket")].copy()
    theme = theme[pd.to_numeric(theme["baseline_mature_sample_size"], errors="coerce").ge(MIN_MATURE_FOR_DIRECTION)]

    lines = [
        "# W-Bottom WV/WVV Filter Stability Grid",
        "",
        f"- generated_at: `{generated_at}`",
        f"- model_id: `{MODEL_ID}`",
        f"- confirmation_model_id: `{CONFIRMATION_MODEL_ID}`",
        f"- source_research_id: `{SOURCE_RESEARCH_ID}`",
        f"- rows: `{len(grid)}`",
        f"- advisory_status: `{RESEARCH_VARIANT_ID}`",
        "- production impact: `none`; this grid does not update production model conditions, scoring, ranking, or baseline.",
        "- interpretation boundary: stability signals are research-only and require promotion review before any production use.",
        "",
        "## Overall Filter Comparison",
        "",
        *markdown_table(
            overall,
            [
                "filter_id",
                "sample_size",
                "mature_sample_size",
                "win_rate",
                "avg_a_return_pct",
                "median_a_return_pct",
                "delta_win_rate_pct",
                "delta_avg_a_return_pct",
                "sample_retention_rate",
                "stability_signal",
                "sample_warning",
            ],
            limit=20,
        ),
        "",
        "## Exclude WV/WVV Stability Signal Counts",
        "",
        *markdown_table(stable_counts, ["segment_dimension", "stability_signal", "segment_count"], limit=80),
        "",
        "## Exclude WV/WVV By Month",
        "",
        *markdown_table(
            month,
            [
                "segment_value",
                "sample_size",
                "mature_sample_size",
                "win_rate",
                "avg_a_return_pct",
                "baseline_mature_sample_size",
                "baseline_win_rate",
                "delta_win_rate_pct",
                "delta_avg_a_return_pct",
                "stability_signal",
                "sample_warning",
            ],
            limit=24,
        ),
        "",
        "## Exclude WV/WVV By Quarter",
        "",
        *markdown_table(
            quarter,
            [
                "segment_value",
                "sample_size",
                "mature_sample_size",
                "win_rate",
                "avg_a_return_pct",
                "baseline_mature_sample_size",
                "baseline_win_rate",
                "delta_win_rate_pct",
                "delta_avg_a_return_pct",
                "stability_signal",
                "sample_warning",
            ],
            limit=12,
        ),
        "",
        "## Exclude WV/WVV By Mainstream Label",
        "",
        *markdown_table(
            mainstream,
            [
                "segment_value",
                "sample_size",
                "mature_sample_size",
                "win_rate",
                "avg_a_return_pct",
                "baseline_mature_sample_size",
                "baseline_win_rate",
                "delta_win_rate_pct",
                "delta_avg_a_return_pct",
                "stability_signal",
                "sample_warning",
            ],
            limit=20,
        ),
        "",
        "## Exclude WV/WVV By Hot Theme Flag",
        "",
        *markdown_table(
            hot_theme,
            [
                "segment_value",
                "sample_size",
                "mature_sample_size",
                "win_rate",
                "avg_a_return_pct",
                "baseline_mature_sample_size",
                "baseline_win_rate",
                "delta_win_rate_pct",
                "delta_avg_a_return_pct",
                "stability_signal",
                "sample_warning",
            ],
            limit=12,
        ),
        "",
        "## Exclude WV/WVV By Structural Theme Bucket With At Least 5 Mature Baseline Rows",
        "",
        *markdown_table(
            theme,
            [
                "segment_value",
                "sample_size",
                "mature_sample_size",
                "win_rate",
                "avg_a_return_pct",
                "baseline_mature_sample_size",
                "baseline_win_rate",
                "delta_win_rate_pct",
                "delta_avg_a_return_pct",
                "stability_signal",
                "sample_warning",
            ],
            limit=40,
        ),
    ]
    LATEST_GRID_MD.parent.mkdir(parents=True, exist_ok=True)
    LATEST_GRID_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    generated_at = now_text()
    grid = build_grid(generated_at)
    if grid.empty:
        raise SystemExit("ERROR: W-bottom WV/WVV stability grid produced no rows")
    write_csv(grid, LATEST_GRID_CSV)
    write_csv(grid, HISTORY_GRID_CSV)
    write_markdown(grid, generated_at)
    print(f"Saved: {LATEST_GRID_CSV} rows={len(grid)}")
    print(f"Saved: {LATEST_GRID_MD}")
    print(f"Saved: {HISTORY_GRID_CSV} rows={len(grid)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
