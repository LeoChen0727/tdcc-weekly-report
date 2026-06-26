from __future__ import annotations

from pathlib import Path

import pandas as pd


ROOT = Path(".")
RESEARCH_LATEST_DIR = ROOT / "output" / "latest" / "research_backtest"
RESEARCH_HISTORY_DIR = ROOT / "output" / "history" / "research"

LATEST_CSV = RESEARCH_LATEST_DIR / "w_bottom_early_entry_outcome_diagnostics_latest.csv"
LATEST_MD = RESEARCH_LATEST_DIR / "w_bottom_early_entry_outcome_diagnostics_latest.md"
HISTORY_CSV = RESEARCH_HISTORY_DIR / "w_bottom_early_entry_outcome_diagnostics.csv"

RESEARCH_ID = "w_bottom_early_entry_outcome_diagnostics"
SOURCE_RESEARCH_ID = "w_bottom_early_entry_parameter_grid"
RESEARCH_VARIANT_ID = "warning_research_variant_only"
PRODUCTION_READINESS = "not_production_ready_research_only"
SURFACE_ID = "w_bottom_right_low_early_entry"
EXPECTED_EVENT_SETS = {"baseline_current_detector", "variant_nearest_micro_45d_event_replay"}
EXPECTED_OUTCOME_RULES = {
    "take_profit_10pct_close_40d",
    "tp10_or_neutral_after_5pct_close_40d",
}
EXPECTED_SEGMENTS = {
    "all_rows",
    "outcome_win",
    "outcome_neutral",
    "outcome_loss",
    "core_mainstream_price_le40",
    "core_mainstream_price_le40_red_delta_gte10",
    "core_mainstream_price_le40_volume_gte1_5",
    "near_neckline_m5_to_0",
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
    "baseline_win_rate_excl_neutral_pct",
    "baseline_neutral_rate_evaluated_pct",
    "delta_win_rate_pct_vs_all",
    "delta_neutral_rate_pct_vs_all",
    "avg_price_position_252_pct",
    "avg_second_arc_volume_ratio",
    "avg_red_ratio_delta_pct",
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
        "win_rate_excl_neutral_pct",
        "neutral_rate_evaluated_pct",
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
    if len(latest) < 90:
        fail(f"row count unexpectedly small: {len(latest)}")
    if set(latest["event_set_id"].astype(str)) != EXPECTED_EVENT_SETS:
        fail("event_set_id values mismatch")
    if set(latest["outcome_rule_id"].astype(str)) != EXPECTED_OUTCOME_RULES:
        fail("outcome_rule_id values mismatch")
    missing_segments = sorted(EXPECTED_SEGMENTS - set(latest["segment_id"].astype(str)))
    if missing_segments:
        fail(f"missing expected segment ids: {missing_segments}")
    if not {"segment_rate", "outcome_profile"}.issubset(set(latest["diagnostic_type"].astype(str))):
        fail("diagnostic types must include segment_rate and outcome_profile")

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
            "delta_win_rate_pct_vs_all",
            "delta_neutral_rate_pct_vs_all",
        ],
        "latest",
    )

    neutral_rule = latest[
        latest["event_set_id"].eq("variant_nearest_micro_45d_event_replay")
        & latest["outcome_rule_id"].eq("tp10_or_neutral_after_5pct_close_40d")
        & latest["segment_id"].eq("all_rows")
    ]
    if len(neutral_rule) != 1:
        fail("missing variant all_rows neutral-rule diagnostic")
    row = neutral_rule.iloc[0]
    if int(float(row["neutral_count"])) <= 0:
        fail("neutral rule must have neutral rows")
    if float(row["neutral_rate_evaluated_pct"]) <= 0:
        fail("neutral rule neutral_rate_evaluated_pct must be positive")

    candidate_rows = latest[
        latest["research_interpretation"].isin(
            [
                "candidate_improves_win_without_more_neutral",
                "candidate_reduces_neutral_without_losing_win_rate",
            ]
        )
    ]
    if candidate_rows.empty:
        fail("expected at least one candidate diagnostic row")

    print(f"W-bottom early-entry outcome diagnostics validation passed rows={len(latest)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
