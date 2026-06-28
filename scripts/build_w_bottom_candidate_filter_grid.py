from __future__ import annotations

from datetime import datetime
from pathlib import Path
from typing import Any
from zoneinfo import ZoneInfo
import itertools
import math

import pandas as pd


ROOT = Path(".")
RESEARCH_LATEST_DIR = ROOT / "output" / "latest" / "research_backtest"
RESEARCH_HISTORY_DIR = ROOT / "output" / "history" / "research"

SOURCE_AUDIT_CSV = RESEARCH_LATEST_DIR / "w_bottom_candidate_quality_audit_latest.csv"
LATEST_GRID_CSV = RESEARCH_LATEST_DIR / "w_bottom_candidate_filter_grid_latest.csv"
LATEST_GRID_MD = RESEARCH_LATEST_DIR / "w_bottom_candidate_filter_grid_latest.md"
HISTORY_GRID_CSV = RESEARCH_HISTORY_DIR / "w_bottom_candidate_filter_grid.csv"

MODEL_ID = "w_bottom_right_side"
RESEARCH_ID = "w_bottom_candidate_filter_grid"
SOURCE_RESEARCH_ID = "w_bottom_candidate_quality_audit"
RESEARCH_VARIANT_ID = "warning_research_variant_only"
PARAMETER_SET_ID = "w_bottom_candidate_filter_grid_20260624"

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
    "research_variant_id",
    "parameter_set_id",
    "advisory_status",
    "candidate_set_id",
    "candidate_set_family",
    "neckline_gap_min_pct",
    "neckline_gap_max_pct",
    "right_rebound_min_pct",
    "right_rebound_max_pct",
    "second_arc_volume_ratio_min",
    "sample_size",
    "unique_stocks",
    "w_shape_completed_count",
    "w_shape_completed_rate",
    "neckline_volume_breakout_count",
    "neckline_volume_breakout_rate",
    "right_low_failed_count",
    "right_low_failed_rate",
    "too_near_neckline_count",
    "too_near_neckline_rate",
    "completed_without_volume_breakout_count",
    "completed_without_volume_breakout_rate",
    "late_completion_count",
    "late_completion_rate",
    "no_completion_count",
    "no_completion_rate",
    "future_window_incomplete_count",
    "future_window_incomplete_rate",
    "review_score",
    "sample_status",
    "interpretation",
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


def bool_series(series: pd.Series) -> pd.Series:
    return series.astype(str).str.lower().isin(["true", "1", "yes", "y"])


def pct(numerator: int, denominator: int) -> float | str:
    if denominator <= 0:
        return ""
    return round(numerator / denominator * 100.0, 4)


def write_csv(df: pd.DataFrame, path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(path, index=False, encoding="utf-8-sig")


def read_audit() -> pd.DataFrame:
    if not SOURCE_AUDIT_CSV.exists():
        raise SystemExit(f"ERROR: missing required input: {SOURCE_AUDIT_CSV}")
    audit = pd.read_csv(SOURCE_AUDIT_CSV, dtype=str, keep_default_na=False)
    required = {
        "model_id",
        "stock_id",
        "signal_distance_to_neckline_pct",
        "signal_rebound_from_right_low_pct",
        "second_arc_volume_ratio",
        "sym1_5_w_shape_completed",
        "sym1_5_neckline_volume_breakout",
        "sym1_5_quality_bucket",
        "primary_review_flag",
        "approved_for_daily",
    }
    missing = sorted(required - set(audit.columns))
    if missing:
        raise SystemExit(f"ERROR: source audit missing columns: {missing}")
    return audit


def candidate_specs() -> list[dict[str, Any]]:
    specs: list[dict[str, Any]] = [
        {
            "candidate_set_id": "baseline_current_audit_all",
            "candidate_set_family": "baseline",
            "neckline_gap_min_pct": "",
            "neckline_gap_max_pct": "",
            "right_rebound_min_pct": "",
            "right_rebound_max_pct": "",
            "second_arc_volume_ratio_min": "",
        }
    ]
    for gap_min in [2.0, 3.0, 5.0]:
        specs.append(
            {
                "candidate_set_id": f"single_not_near_neckline_gap_ge_{int(gap_min)}",
                "candidate_set_family": "single_gap_filter",
                "neckline_gap_min_pct": gap_min,
                "neckline_gap_max_pct": "",
                "right_rebound_min_pct": "",
                "right_rebound_max_pct": "",
                "second_arc_volume_ratio_min": "",
            }
        )
    for rebound_min in [5.0, 7.0]:
        specs.append(
            {
                "candidate_set_id": f"single_right_rebound_ge_{int(rebound_min)}",
                "candidate_set_family": "single_rebound_filter",
                "neckline_gap_min_pct": "",
                "neckline_gap_max_pct": "",
                "right_rebound_min_pct": rebound_min,
                "right_rebound_max_pct": "",
                "second_arc_volume_ratio_min": "",
            }
        )
    for volume_min in [1.5, 2.0]:
        specs.append(
            {
                "candidate_set_id": f"single_second_arc_volume_ge_{str(volume_min).replace('.', '_')}",
                "candidate_set_family": "single_volume_filter",
                "neckline_gap_min_pct": "",
                "neckline_gap_max_pct": "",
                "right_rebound_min_pct": "",
                "right_rebound_max_pct": "",
                "second_arc_volume_ratio_min": volume_min,
            }
        )

    for gap_min, gap_max, rebound_min, rebound_max, volume_min in itertools.product(
        [2.0, 3.0, 5.0],
        [15.0, 20.0, 30.0],
        [3.0, 5.0, 7.0],
        [12.0, 15.0],
        [1.2, 1.5, 2.0],
    ):
        if gap_min >= gap_max:
            continue
        specs.append(
            {
                "candidate_set_id": (
                    f"grid_gap_{int(gap_min)}_{int(gap_max)}_"
                    f"rebound_{int(rebound_min)}_{int(rebound_max)}_vol_{str(volume_min).replace('.', '_')}"
                ),
                "candidate_set_family": "combined_grid",
                "neckline_gap_min_pct": gap_min,
                "neckline_gap_max_pct": gap_max,
                "right_rebound_min_pct": rebound_min,
                "right_rebound_max_pct": rebound_max,
                "second_arc_volume_ratio_min": volume_min,
            }
        )
    return specs


def apply_spec(audit: pd.DataFrame, spec: dict[str, Any]) -> pd.DataFrame:
    df = audit.copy()
    distance = pd.to_numeric(df["signal_distance_to_neckline_pct"], errors="coerce")
    rebound = pd.to_numeric(df["signal_rebound_from_right_low_pct"], errors="coerce")
    volume_ratio = pd.to_numeric(df["second_arc_volume_ratio"], errors="coerce")
    mask = pd.Series(True, index=df.index)

    gap_min = safe_float(spec.get("neckline_gap_min_pct"))
    if not math.isnan(gap_min):
        mask &= distance <= -gap_min
    gap_max = safe_float(spec.get("neckline_gap_max_pct"))
    if not math.isnan(gap_max):
        mask &= distance >= -gap_max
    rebound_min = safe_float(spec.get("right_rebound_min_pct"))
    if not math.isnan(rebound_min):
        mask &= rebound >= rebound_min
    rebound_max = safe_float(spec.get("right_rebound_max_pct"))
    if not math.isnan(rebound_max):
        mask &= rebound <= rebound_max
    volume_min = safe_float(spec.get("second_arc_volume_ratio_min"))
    if not math.isnan(volume_min):
        mask &= volume_ratio >= volume_min
    return df[mask].copy()


def sample_status(sample_size: int) -> str:
    if sample_size >= 200:
        return "broad_sample"
    if sample_size >= 100:
        return "medium_sample"
    if sample_size >= 50:
        return "thin_but_reviewable"
    if sample_size >= 20:
        return "low_sample"
    return "too_small"


def interpretation(row: dict[str, Any]) -> str:
    sample = int(row["sample_size"])
    if sample < 50:
        return "too_small_for_directional_review"
    breakout_rate = safe_float(row["neckline_volume_breakout_rate"])
    right_low_failed_rate = safe_float(row["right_low_failed_rate"])
    too_near_rate = safe_float(row["too_near_neckline_rate"])
    if breakout_rate >= 16 and right_low_failed_rate <= 24 and too_near_rate <= 5:
        return "promising_for_manual_shape_review"
    if too_near_rate > 10:
        return "still_selects_too_close_to_neckline"
    if right_low_failed_rate > 28:
        return "right_low_failure_still_high"
    if breakout_rate < 10:
        return "breakout_conversion_weaker_than_baseline"
    return "mixed_needs_chart_review"


def summarize_spec(audit: pd.DataFrame, spec: dict[str, Any], generated_at: str) -> dict[str, Any]:
    sample = apply_spec(audit, spec)
    total = len(sample)
    bucket = sample["sym1_5_quality_bucket"].astype(str) if total else pd.Series(dtype=str)
    completed = int(bool_series(sample["sym1_5_w_shape_completed"]).sum()) if total else 0
    breakout = int(bool_series(sample["sym1_5_neckline_volume_breakout"]).sum()) if total else 0
    right_low_failed = int(sample["primary_review_flag"].astype(str).eq("right_low_failed").sum()) if total else 0
    too_near = int(bucket.eq("already_near_neckline_at_signal").sum()) if total else 0
    completed_without_breakout = int(bucket.eq("completed_without_volume_breakout").sum()) if total else 0
    late = int(bucket.isin(["late_volume_breakout_not_w", "late_neckline_completion_not_w"]).sum()) if total else 0
    no_completion = int(bucket.eq("no_completion_within_symmetry").sum()) if total else 0
    future_incomplete = int(bucket.eq("future_window_incomplete").sum()) if total else 0
    breakout_rate = pct(breakout, total)
    right_low_failed_rate = pct(right_low_failed, total)
    too_near_rate = pct(too_near, total)
    completed_rate = pct(completed, total)

    numeric_breakout = safe_float(breakout_rate)
    numeric_failed = safe_float(right_low_failed_rate)
    numeric_near = safe_float(too_near_rate)
    numeric_completed = safe_float(completed_rate)
    review_score = ""
    if total > 0:
        review_score = round(numeric_breakout + numeric_completed * 0.2 - numeric_failed * 0.35 - numeric_near * 0.5, 4)

    row = {
        "model_id": MODEL_ID,
        "research_id": RESEARCH_ID,
        "source_research_id": SOURCE_RESEARCH_ID,
        "research_variant_id": RESEARCH_VARIANT_ID,
        "parameter_set_id": PARAMETER_SET_ID,
        "advisory_status": RESEARCH_VARIANT_ID,
        "candidate_set_id": spec["candidate_set_id"],
        "candidate_set_family": spec["candidate_set_family"],
        "neckline_gap_min_pct": spec.get("neckline_gap_min_pct", ""),
        "neckline_gap_max_pct": spec.get("neckline_gap_max_pct", ""),
        "right_rebound_min_pct": spec.get("right_rebound_min_pct", ""),
        "right_rebound_max_pct": spec.get("right_rebound_max_pct", ""),
        "second_arc_volume_ratio_min": spec.get("second_arc_volume_ratio_min", ""),
        "sample_size": total,
        "unique_stocks": sample["stock_id"].nunique() if total else 0,
        "w_shape_completed_count": completed,
        "w_shape_completed_rate": completed_rate,
        "neckline_volume_breakout_count": breakout,
        "neckline_volume_breakout_rate": breakout_rate,
        "right_low_failed_count": right_low_failed,
        "right_low_failed_rate": right_low_failed_rate,
        "too_near_neckline_count": too_near,
        "too_near_neckline_rate": too_near_rate,
        "completed_without_volume_breakout_count": completed_without_breakout,
        "completed_without_volume_breakout_rate": pct(completed_without_breakout, total),
        "late_completion_count": late,
        "late_completion_rate": pct(late, total),
        "no_completion_count": no_completion,
        "no_completion_rate": pct(no_completion, total),
        "future_window_incomplete_count": future_incomplete,
        "future_window_incomplete_rate": pct(future_incomplete, total),
        "review_score": review_score,
        "sample_status": sample_status(total),
        "interpretation": "",
        "approved_for_daily": "false",
        "generated_at": generated_at,
    }
    row["interpretation"] = interpretation(row)
    return row


def build_grid(audit: pd.DataFrame, generated_at: str) -> pd.DataFrame:
    rows = [summarize_spec(audit, spec, generated_at) for spec in candidate_specs()]
    grid = pd.DataFrame(rows)
    for col in OUTPUT_COLUMNS:
        if col not in grid.columns:
            grid[col] = ""
    forbidden = sorted(set(grid.columns) & FORBIDDEN_PRODUCTION_FIELDS)
    if forbidden:
        raise SystemExit(f"ERROR: forbidden production columns in grid output: {forbidden}")
    return grid[OUTPUT_COLUMNS]


def markdown_table(df: pd.DataFrame, columns: list[str], limit: int = 20) -> list[str]:
    if df.empty:
        return ["_No rows._"]
    rows = df.head(limit).to_dict("records")
    lines = ["| " + " | ".join(columns) + " |", "| " + " | ".join(["---"] * len(columns)) + " |"]
    for row in rows:
        lines.append("| " + " | ".join(safe_str(row.get(col)) for col in columns) + " |")
    return lines


def write_markdown(grid: pd.DataFrame, generated_at: str) -> None:
    baseline = grid[grid["candidate_set_id"].eq("baseline_current_audit_all")].iloc[0]
    reviewable = grid[pd.to_numeric(grid["sample_size"], errors="coerce").ge(50)].copy()
    reviewable["_review_score"] = pd.to_numeric(reviewable["review_score"], errors="coerce")
    reviewable["_breakout_rate"] = pd.to_numeric(reviewable["neckline_volume_breakout_rate"], errors="coerce")
    reviewable["_failed_rate"] = pd.to_numeric(reviewable["right_low_failed_rate"], errors="coerce")
    top = reviewable.sort_values(
        ["_review_score", "_breakout_rate", "_failed_rate", "sample_size"],
        ascending=[False, False, True, False],
    )
    promising = grid[grid["interpretation"].eq("promising_for_manual_shape_review")].copy()
    promising["_sample_size"] = pd.to_numeric(promising["sample_size"], errors="coerce")
    promising = promising.sort_values("_sample_size", ascending=False)

    columns = [
        "candidate_set_id",
        "sample_size",
        "neckline_volume_breakout_rate",
        "right_low_failed_rate",
        "too_near_neckline_rate",
        "w_shape_completed_rate",
        "review_score",
        "interpretation",
    ]
    lines = [
        "# W-Bottom Candidate Filter Grid",
        "",
        f"- generated_at: `{generated_at}`",
        f"- model_id: `{MODEL_ID}`",
        f"- source_research_id: `{SOURCE_RESEARCH_ID}`",
        f"- rows: `{len(grid)}` candidate filter sets",
        f"- advisory_status: `{RESEARCH_VARIANT_ID}`",
        "- production impact: `none`; this grid does not update production model conditions, scoring, ranking, or baseline.",
        "- purpose: compare research-only filters for reducing candidates that are too close to neckline or break the right-side low.",
        "",
        "## Baseline",
        "",
        "| metric | value |",
        "| --- | ---: |",
        f"| sample_size | {baseline['sample_size']} |",
        f"| neckline_volume_breakout_rate | {baseline['neckline_volume_breakout_rate']}% |",
        f"| right_low_failed_rate | {baseline['right_low_failed_rate']}% |",
        f"| too_near_neckline_rate | {baseline['too_near_neckline_rate']}% |",
        f"| w_shape_completed_rate | {baseline['w_shape_completed_rate']}% |",
        "",
        "## Promising Sets",
        "",
        *markdown_table(promising[columns], columns, limit=20),
        "",
        "## Top Reviewable Sets By Descriptive Score",
        "",
        *markdown_table(top[columns], columns, limit=20),
        "",
        "## Reading Notes",
        "",
        "- `neckline_gap_min_pct=3` means the signal must be at least 3% below the neckline, which removes candidates already too close to the neckline.",
        "- `neckline_gap_max_pct=15` means the signal cannot still be more than 15% below the neckline, which removes candidates that may be too early or not actually completing a W.",
        "- `right_rebound_min_pct` tests whether waiting for a stronger rebound from the second low reduces right-low failure.",
        "- `second_arc_volume_ratio_min` tests the user's W-bottom volume idea: the second arc average volume should exceed the first arc.",
        "- `review_score` is only a descriptive research sorting aid, not a production ranking rule.",
    ]
    LATEST_GRID_MD.parent.mkdir(parents=True, exist_ok=True)
    LATEST_GRID_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> int:
    generated_at = now_text()
    audit = read_audit()
    grid = build_grid(audit, generated_at)
    if grid.empty:
        raise SystemExit("ERROR: W-bottom candidate filter grid produced no rows")
    write_csv(grid, LATEST_GRID_CSV)
    write_csv(grid, HISTORY_GRID_CSV)
    write_markdown(grid, generated_at)
    print(f"Saved: {LATEST_GRID_CSV} rows={len(grid)}")
    print(f"Saved: {LATEST_GRID_MD}")
    print(f"Saved: {HISTORY_GRID_CSV} rows={len(grid)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
