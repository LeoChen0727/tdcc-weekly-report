from __future__ import annotations

from pathlib import Path

import pandas as pd


ROOT = Path(".")
RESEARCH_LATEST_DIR = ROOT / "output" / "latest" / "research_backtest"
RESEARCH_HISTORY_DIR = ROOT / "output" / "history" / "research"

LATEST_CSV = RESEARCH_LATEST_DIR / "w_bottom_early_entry_stability_audit_latest.csv"
LATEST_MD = RESEARCH_LATEST_DIR / "w_bottom_early_entry_stability_audit_latest.md"
HISTORY_CSV = RESEARCH_HISTORY_DIR / "w_bottom_early_entry_stability_audit.csv"

RESEARCH_ID = "w_bottom_early_entry_stability_audit"
SOURCE_RESEARCH_ID = "w_bottom_early_entry_parameter_grid"
RESEARCH_VARIANT_ID = "warning_research_variant_only"
PRODUCTION_READINESS = "not_production_ready_research_only"
SURFACE_ID = "w_bottom_right_low_early_entry"
EVENT_SET_ID = "variant_nearest_micro_45d_event_replay"
EXPECTED_OUTCOME_RULES = {
    "take_profit_10pct_close_40d",
    "tp10_or_neutral_after_5pct_close_40d",
}
EXPECTED_SEGMENTS = {
    "all_rows",
    "smooth_right_rebound_5_20",
    "smooth_price_le40_right_rebound_5_20",
    "smooth_core_mainstream_right_rebound_5_20",
    "smooth_core_mainstream_price_le40_right_rebound_5_20",
    "smooth_right_rebound_5_20_red_ratio_gt_first",
    "smooth_right_rebound_5_20_near_neckline",
}
BLOCKING_STABILITY_STATUSES = {
    "insufficient_period_coverage_for_promotion",
    "insufficient_monthly_repetition",
    "unstable_period_win_rate",
}

REQUIRED_COLUMNS = {
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
    "segment_id",
    "row_type",
    "period_type",
    "period_id",
    "period_start_date",
    "period_end_date",
    "period_count",
    "periods_with_evaluated_ge5",
    "periods_with_mature_ge5",
    "periods_with_mature_ge10",
    "sample_size",
    "evaluated_sample_size",
    "mature_sample_size",
    "win_count",
    "neutral_count",
    "loss_count",
    "incomplete_count",
    "win_rate_excl_neutral_pct",
    "neutral_rate_evaluated_pct",
    "incomplete_rate_pct",
    "min_period_win_rate_pct",
    "max_period_win_rate_pct",
    "win_rate_range_pct",
    "stability_status",
    "sample_warning",
    "research_interpretation",
    "approved_for_daily",
    "production_readiness",
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
    raise SystemExit(f"ERROR: {message}")


def read_csv(path: Path) -> pd.DataFrame:
    if not path.exists():
        fail(f"missing required file: {path}")
    return pd.read_csv(path, dtype=str, keep_default_na=False)


def false_only(series: pd.Series) -> bool:
    return set(series.astype(str).str.lower()).issubset({"false"})


def validate_constants(df: pd.DataFrame, name: str) -> None:
    expected = {
        "research_id": RESEARCH_ID,
        "source_research_id": SOURCE_RESEARCH_ID,
        "research_variant_id": RESEARCH_VARIANT_ID,
        "advisory_status": RESEARCH_VARIANT_ID,
        "surface_id": SURFACE_ID,
        "event_set_id": EVENT_SET_ID,
        "approved_for_daily": "false",
        "production_readiness": PRODUCTION_READINESS,
    }
    for column, expected_value in expected.items():
        values = set(df[column].astype(str))
        if values != {expected_value}:
            fail(f"{name} unexpected {column}: {sorted(values)}")
    if not false_only(df["approved_for_daily"]):
        fail(f"{name} approved_for_daily must remain false")


def validate_numeric(df: pd.DataFrame, columns: list[str], name: str) -> None:
    for column in columns:
        values = pd.to_numeric(df[column], errors="coerce")
        populated = df[column].astype(str).ne("")
        if values[populated].isna().any():
            fail(f"{name} column must be numeric when populated: {column}")


def validate_markdown() -> None:
    if not LATEST_MD.exists():
        fail(f"missing markdown: {LATEST_MD}")
    text = LATEST_MD.read_text(encoding="utf-8")
    required = [
        "production impact: `none`",
        "short-window stability check",
        "Strict Segment Monthly Rollup",
        "smooth_right_rebound_5_20 Monthly Detail",
        "does not modify production conditions, scoring, ranking, PDFs, baselines, or daily_full_pipeline",
        "approved_for_daily=false",
    ]
    for item in required:
        if item not in text:
            fail(f"markdown missing required text: {item}")


def main() -> int:
    latest = read_csv(LATEST_CSV)
    history = read_csv(HISTORY_CSV)
    validate_markdown()

    for df, name in [(latest, "latest"), (history, "history")]:
        missing = sorted(REQUIRED_COLUMNS - set(df.columns))
        if missing:
            fail(f"{name} missing columns: {missing}")
        forbidden = sorted(set(df.columns) & FORBIDDEN_PRODUCTION_FIELDS)
        if forbidden:
            fail(f"{name} must not emit production decision fields: {forbidden}")
        validate_constants(df, name)

    if len(latest) != len(history):
        fail("latest/history row counts differ")
    if len(latest) < 120:
        fail(f"row count unexpectedly small: {len(latest)}")
    if set(latest["outcome_rule_id"].astype(str)) != EXPECTED_OUTCOME_RULES:
        fail("outcome_rule_id values mismatch")
    missing_segments = sorted(EXPECTED_SEGMENTS - set(latest["segment_id"].astype(str)))
    if missing_segments:
        fail(f"missing expected segment ids: {missing_segments}")
    if not {"period", "summary"}.issubset(set(latest["row_type"].astype(str))):
        fail("row_type must include period and summary")
    if not {"all", "quarter", "month"}.issubset(set(latest["period_type"].astype(str))):
        fail("period_type must include all, quarter, and month")

    validate_numeric(
        latest,
        [
            "sample_size",
            "evaluated_sample_size",
            "mature_sample_size",
            "win_count",
            "neutral_count",
            "loss_count",
            "incomplete_count",
            "win_rate_excl_neutral_pct",
            "neutral_rate_evaluated_pct",
            "incomplete_rate_pct",
        ],
        "latest",
    )

    summary = latest[
        latest["row_type"].eq("summary")
        & latest["outcome_rule_id"].eq("tp10_or_neutral_after_5pct_close_40d")
    ].copy()
    if summary.empty:
        fail("missing neutral-rule summary rows")
    strict_summary = summary[summary["segment_id"].eq("smooth_right_rebound_5_20")]
    if len(strict_summary) != 1:
        fail("missing smooth_right_rebound_5_20 neutral-rule summary")
    status = strict_summary.iloc[0]["stability_status"]
    if status not in BLOCKING_STABILITY_STATUSES:
        fail(f"smooth_right_rebound_5_20 must remain blocked from promotion; got {status}")

    months = latest[
        latest["row_type"].eq("period")
        & latest["period_type"].eq("month")
        & latest["outcome_rule_id"].eq("tp10_or_neutral_after_5pct_close_40d")
        & latest["segment_id"].eq("smooth_right_rebound_5_20")
    ]
    if months["period_id"].nunique() < 4:
        fail("smooth_right_rebound_5_20 must cover at least four signal months for this audit")

    print(f"W-bottom early-entry stability audit validation passed rows={len(latest)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
