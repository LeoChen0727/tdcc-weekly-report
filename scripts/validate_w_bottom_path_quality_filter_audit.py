from __future__ import annotations

from pathlib import Path

import pandas as pd


ROOT = Path(".")
RESEARCH_LATEST_DIR = ROOT / "output" / "latest" / "research_backtest"
RESEARCH_HISTORY_DIR = ROOT / "output" / "history" / "research"

SOURCE_OBSERVATION_CSV = RESEARCH_LATEST_DIR / "w_bottom_observation_confirmation_audit_latest.csv"
LATEST_SUMMARY_CSV = RESEARCH_LATEST_DIR / "w_bottom_path_quality_filter_audit_latest.csv"
LATEST_DETAIL_CSV = RESEARCH_LATEST_DIR / "w_bottom_path_quality_filter_audit_detail_latest.csv"
LATEST_MD = RESEARCH_LATEST_DIR / "w_bottom_path_quality_filter_audit_latest.md"
HISTORY_SUMMARY_CSV = RESEARCH_HISTORY_DIR / "w_bottom_path_quality_filter_audit.csv"
HISTORY_DETAIL_CSV = RESEARCH_HISTORY_DIR / "w_bottom_path_quality_filter_audit_detail.csv"

DETAIL_REQUIRED_COLUMNS = {
    "model_id",
    "confirmation_model_id",
    "research_id",
    "source_research_id",
    "research_variant_id",
    "advisory_status",
    "stock_id",
    "signal_date",
    "initial_stage",
    "confirmation_stage",
    "transition_status",
    "slope_curvature_category",
    "slope_issue_reasons",
    "path_days",
    "full_path_significant_turn_count",
    "full_path_abrupt_slope_change_count",
    "first_low_sharp_v_flag",
    "second_low_sharp_v_flag",
    "observation_stage_eligible",
    "confirmation_stage_eligible",
    "a_mature",
    "a_return_pct",
    "tdcc_any_age7",
    "approved_for_daily",
    "production_readiness",
    "generated_at",
}

SUMMARY_REQUIRED_COLUMNS = {
    "model_id",
    "confirmation_model_id",
    "research_id",
    "source_research_id",
    "research_variant_id",
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
}

EXPECTED_FILTERS = {
    "all_volume_confirmed",
    "observation_to_volume_confirmation",
    "observation_volume_exclude_sharp_v",
    "observation_volume_exclude_wv_multiple_turn",
    "observation_volume_exclude_slope_break",
    "observation_volume_exclude_sharp_v_and_wv",
    "observation_volume_smooth_only",
    "observation_volume_smooth_or_slope_break",
}

SLOPE_CATEGORIES = {
    "smooth_rounded_w_like",
    "sharp_v_bottom_risk",
    "wv_multiple_turn_risk",
    "slope_break_discontinuous",
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


def fail(message: str) -> None:
    print(f"ERROR: {message}")
    raise SystemExit(1)


def read_csv(path: Path) -> pd.DataFrame:
    if not path.exists():
        fail(f"missing required file: {path}")
    try:
        return pd.read_csv(path, dtype=str, keep_default_na=False)
    except Exception as exc:
        fail(f"{path} is not readable CSV: {exc}")


def false_only(series: pd.Series) -> bool:
    return set(series.astype(str).str.lower().unique()) <= {"false", "0", ""}


def boolish_only(series: pd.Series) -> bool:
    return set(series.astype(str).str.lower().unique()) <= {"true", "false", "1", "0"}


def main() -> int:
    source = read_csv(SOURCE_OBSERVATION_CSV)
    detail = read_csv(LATEST_DETAIL_CSV)
    detail_history = read_csv(HISTORY_DETAIL_CSV)
    summary = read_csv(LATEST_SUMMARY_CSV)
    summary_history = read_csv(HISTORY_SUMMARY_CSV)
    if not LATEST_MD.exists():
        fail(f"missing required file: {LATEST_MD}")
    md_lines = LATEST_MD.read_text(encoding="utf-8", errors="replace").splitlines()
    if len(md_lines) < 40:
        fail(f"{LATEST_MD} is suspiciously short")

    if len(detail) != len(source):
        fail(f"detail rows must equal observation audit rows: detail={len(detail)} source={len(source)}")
    if len(detail) != len(detail_history):
        fail("latest and history detail row counts differ")
    if len(summary) != len(summary_history):
        fail("latest and history summary row counts differ")
    if summary.empty:
        fail("summary has no rows")

    missing_detail = sorted(DETAIL_REQUIRED_COLUMNS - set(detail.columns))
    missing_summary = sorted(SUMMARY_REQUIRED_COLUMNS - set(summary.columns))
    if missing_detail:
        fail(f"{LATEST_DETAIL_CSV} missing columns: {missing_detail}")
    if missing_summary:
        fail(f"{LATEST_SUMMARY_CSV} missing columns: {missing_summary}")

    forbidden = sorted((set(detail.columns) | set(summary.columns)) & FORBIDDEN_PRODUCTION_FIELDS)
    if forbidden:
        fail(f"path quality audit must not emit production decision fields: {forbidden}")

    if set(detail["model_id"].astype(str)) != {"w_bottom_right_side"}:
        fail("detail model_id must be w_bottom_right_side")
    if set(summary["model_id"].astype(str)) != {"w_bottom_right_side"}:
        fail("summary model_id must be w_bottom_right_side")
    if set(detail["confirmation_model_id"].astype(str)) != {"neckline_volume_breakout_confirmation"}:
        fail("detail confirmation_model_id must be neckline_volume_breakout_confirmation")
    if set(summary["confirmation_model_id"].astype(str)) != {"neckline_volume_breakout_confirmation"}:
        fail("summary confirmation_model_id must be neckline_volume_breakout_confirmation")
    if set(detail["research_id"].astype(str)) != {"w_bottom_path_quality_filter_audit"}:
        fail("detail research_id must be w_bottom_path_quality_filter_audit")
    if set(summary["research_id"].astype(str)) != {"w_bottom_path_quality_filter_audit"}:
        fail("summary research_id must be w_bottom_path_quality_filter_audit")
    if set(detail["research_variant_id"].astype(str)) != {"warning_research_variant_only"}:
        fail("detail must be warning_research_variant_only")
    if set(summary["research_variant_id"].astype(str)) != {"warning_research_variant_only"}:
        fail("summary must be warning_research_variant_only")
    if set(detail["production_readiness"].astype(str)) != {"not_production_ready_research_only"}:
        fail("detail production_readiness must be not_production_ready_research_only")
    if set(summary["production_readiness"].astype(str)) != {"not_production_ready_research_only"}:
        fail("summary production_readiness must be not_production_ready_research_only")
    if not false_only(detail["approved_for_daily"]):
        fail("detail approved_for_daily must remain false")
    if not false_only(summary["approved_for_daily"]):
        fail("summary approved_for_daily must remain false")

    invalid_categories = sorted(set(detail["slope_curvature_category"].astype(str)) - SLOPE_CATEGORIES)
    if invalid_categories:
        fail(f"unexpected slope categories: {invalid_categories}")
    missing_filters = sorted(EXPECTED_FILTERS - set(summary["filter_id"].astype(str)))
    extra_filters = sorted(set(summary["filter_id"].astype(str)) - EXPECTED_FILTERS)
    if missing_filters or extra_filters:
        fail(f"unexpected summary filters missing={missing_filters} extra={extra_filters}")

    for column in [
        "first_low_sharp_v_flag",
        "second_low_sharp_v_flag",
        "observation_stage_eligible",
        "confirmation_stage_eligible",
        "a_mature",
        "tdcc_any_age7",
    ]:
        if not boolish_only(detail[column]):
            fail(f"{column} must be boolean-like")

    for column in ["path_days", "sample_size", "mature_sample_size", "win_count"]:
        target = detail[column] if column == "path_days" else summary[column]
        values = pd.to_numeric(target, errors="coerce")
        if values.isna().any():
            fail(f"{column} must be numeric")

    baseline = summary[summary["filter_id"].eq("observation_to_volume_confirmation")]
    smooth_only = summary[summary["filter_id"].eq("observation_volume_smooth_only")]
    if baseline.empty:
        fail("missing observation_to_volume_confirmation baseline filter")
    if smooth_only.empty:
        fail("missing observation_volume_smooth_only filter")
    if int(pd.to_numeric(baseline.iloc[0]["sample_size"], errors="coerce")) <= 0:
        fail("baseline observation_to_volume_confirmation sample_size must be positive")

    print(
        "W-bottom path quality filter audit validation passed "
        f"detail_rows={len(detail)} summary_rows={len(summary)} "
        f"categories={sorted(set(detail['slope_curvature_category']))}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
