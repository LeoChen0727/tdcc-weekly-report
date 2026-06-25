from __future__ import annotations

from pathlib import Path

import pandas as pd


ROOT = Path(".")
RESEARCH_LATEST_DIR = ROOT / "output" / "latest" / "research_backtest"
RESEARCH_HISTORY_DIR = ROOT / "output" / "history" / "research"

SOURCE_QUALITY_CSV = RESEARCH_LATEST_DIR / "w_bottom_candidate_quality_audit_latest.csv"
SOURCE_DEFINITION_CSV = RESEARCH_LATEST_DIR / "w_bottom_candidate_definition_audit_latest.csv"
LATEST_AUDIT_CSV = RESEARCH_LATEST_DIR / "w_bottom_observation_confirmation_audit_latest.csv"
LATEST_AUDIT_MD = RESEARCH_LATEST_DIR / "w_bottom_observation_confirmation_audit_latest.md"
HISTORY_AUDIT_CSV = RESEARCH_HISTORY_DIR / "w_bottom_observation_confirmation_audit.csv"

REQUIRED_COLUMNS = {
    "model_id",
    "confirmation_model_id",
    "research_id",
    "source_research_id",
    "source_definition_research_id",
    "research_variant_id",
    "advisory_status",
    "sample_mode",
    "stock_id",
    "signal_date",
    "initial_stage",
    "confirmation_stage",
    "transition_status",
    "surface_recommendation",
    "observation_stage_eligible",
    "confirmation_stage_eligible",
    "price_confirmation_only",
    "in_manual_review_packet",
    "primary_review_flag",
    "sym1_5_quality_bucket",
    "definition_status",
    "slope_curvature_category",
    "sym1_5_w_shape_completed",
    "sym1_5_neckline_volume_breakout",
    "sym1_5_right_low_broken",
    "a_mature",
    "a_return_pct",
    "tdcc_any_age7",
    "tdcc_any_age14",
    "manual_review_status",
    "approved_for_daily",
    "production_readiness",
    "generated_at",
}

INITIAL_STAGES = {
    "right_side_observation_zone",
    "right_side_extended_rebound",
    "near_neckline_at_signal",
    "already_above_neckline_at_signal",
    "right_side_rebound_too_early",
    "right_side_unclassified",
}

CONFIRMATION_STAGES = {
    "volume_confirmed_neckline_breakout",
    "price_confirmed_without_volume",
    "right_low_support_failed",
    "late_confirmation_not_w",
    "no_confirmation_within_symmetry",
    "future_window_incomplete",
    "invalid_or_missing_confirmation_path",
}

TRANSITION_STATUSES = {
    "observation_to_volume_confirmation",
    "observation_to_price_only_confirmation",
    "observation_support_failed",
    "observation_late_confirmation_not_w",
    "observation_no_confirmation",
    "observation_future_window_incomplete",
    "near_neckline_or_above_volume_confirmation",
    "not_observation_near_neckline_or_above",
    "not_primary_observation_extended_rebound",
    "not_primary_observation_too_early",
    "not_primary_observation_unclassified",
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


def boolish_only(series: pd.Series) -> bool:
    return set(series.astype(str).str.lower().unique()) <= {"true", "false", "1", "0"}


def false_only(series: pd.Series) -> bool:
    return set(series.astype(str).str.lower().unique()) <= {"false", "0", ""}


def main() -> int:
    quality = read_csv(SOURCE_QUALITY_CSV)
    latest = read_csv(LATEST_AUDIT_CSV)
    history = read_csv(HISTORY_AUDIT_CSV)
    if not LATEST_AUDIT_MD.exists():
        fail(f"missing required file: {LATEST_AUDIT_MD}")
    md_lines = LATEST_AUDIT_MD.read_text(encoding="utf-8", errors="replace").splitlines()
    if len(md_lines) < 40:
        fail(f"{LATEST_AUDIT_MD} is suspiciously short")
    if latest.empty:
        fail(f"{LATEST_AUDIT_CSV} has no rows")
    if len(latest) != len(history):
        fail("latest and history observation/confirmation audit row counts differ")
    if len(latest) != len(quality):
        fail(f"latest rows must equal quality audit rows: latest={len(latest)} quality={len(quality)}")

    missing = sorted(REQUIRED_COLUMNS - set(latest.columns))
    if missing:
        fail(f"{LATEST_AUDIT_CSV} missing columns: {missing}")
    missing_history = sorted(REQUIRED_COLUMNS - set(history.columns))
    if missing_history:
        fail(f"{HISTORY_AUDIT_CSV} missing columns: {missing_history}")

    forbidden = sorted((set(latest.columns) | set(history.columns)) & FORBIDDEN_PRODUCTION_FIELDS)
    if forbidden:
        fail(f"W-bottom observation/confirmation audit must not emit production decision fields: {forbidden}")

    if set(latest["model_id"].astype(str)) != {"w_bottom_right_side"}:
        fail("audit model_id must be w_bottom_right_side")
    if set(latest["confirmation_model_id"].astype(str)) != {"neckline_volume_breakout_confirmation"}:
        fail("audit confirmation_model_id must be neckline_volume_breakout_confirmation")
    if set(latest["research_id"].astype(str)) != {"w_bottom_observation_confirmation_audit"}:
        fail("audit research_id must be w_bottom_observation_confirmation_audit")
    if set(latest["source_research_id"].astype(str)) != {"w_bottom_candidate_quality_audit"}:
        fail("audit source_research_id must be w_bottom_candidate_quality_audit")
    if set(latest["research_variant_id"].astype(str)) != {"warning_research_variant_only"}:
        fail("audit must be marked warning_research_variant_only")
    if set(latest["advisory_status"].astype(str)) != {"warning_research_variant_only"}:
        fail("audit advisory_status must be warning_research_variant_only")
    if set(latest["production_readiness"].astype(str)) != {"not_production_ready_research_only"}:
        fail("audit production_readiness must remain not_production_ready_research_only")
    if not false_only(latest["approved_for_daily"]):
        fail("audit approved_for_daily must remain false")

    invalid_initial = sorted(set(latest["initial_stage"].astype(str)) - INITIAL_STAGES)
    invalid_confirmation = sorted(set(latest["confirmation_stage"].astype(str)) - CONFIRMATION_STAGES)
    invalid_transition = sorted(set(latest["transition_status"].astype(str)) - TRANSITION_STATUSES)
    if invalid_initial:
        fail(f"unexpected initial_stage values: {invalid_initial}")
    if invalid_confirmation:
        fail(f"unexpected confirmation_stage values: {invalid_confirmation}")
    if invalid_transition:
        fail(f"unexpected transition_status values: {invalid_transition}")

    for column in [
        "observation_stage_eligible",
        "confirmation_stage_eligible",
        "price_confirmation_only",
        "in_manual_review_packet",
        "sym1_5_w_shape_completed",
        "sym1_5_neckline_volume_breakout",
        "sym1_5_right_low_broken",
        "a_mature",
        "tdcc_any_age7",
        "tdcc_any_age14",
    ]:
        if not boolish_only(latest[column]):
            fail(f"{column} must be boolean-like")

    if SOURCE_DEFINITION_CSV.exists():
        definition = read_csv(SOURCE_DEFINITION_CSV)
        review_count = int(latest["in_manual_review_packet"].astype(str).str.lower().eq("true").sum())
        if review_count != len(definition):
            fail(
                "manual review packet row count must equal definition audit rows: "
                f"review_count={review_count} definition={len(definition)}"
            )

    confirmation = latest[latest["confirmation_stage"].eq("volume_confirmed_neckline_breakout")]
    if confirmation.empty:
        fail("audit must include at least one volume-confirmed confirmation candidate")
    if not confirmation["confirmation_stage_eligible"].astype(str).str.lower().eq("true").all():
        fail("volume-confirmed rows must have confirmation_stage_eligible=true")

    print(
        "W-bottom observation/confirmation audit validation passed "
        f"rows={len(latest)} observation_stage_eligible="
        f"{int(latest['observation_stage_eligible'].astype(str).str.lower().eq('true').sum())} "
        f"confirmation_stage_eligible={len(confirmation)}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
