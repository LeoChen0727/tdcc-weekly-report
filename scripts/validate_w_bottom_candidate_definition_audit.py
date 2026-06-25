from __future__ import annotations

from pathlib import Path

import pandas as pd


ROOT = Path(".")
RESEARCH_LATEST_DIR = ROOT / "output" / "latest" / "research_backtest"
RESEARCH_HISTORY_DIR = ROOT / "output" / "history" / "research"

SOURCE_CHART_REVIEW_CSV = RESEARCH_LATEST_DIR / "w_bottom_candidate_chart_review_latest.csv"
LATEST_AUDIT_CSV = RESEARCH_LATEST_DIR / "w_bottom_candidate_definition_audit_latest.csv"
LATEST_AUDIT_MD = RESEARCH_LATEST_DIR / "w_bottom_candidate_definition_audit_latest.md"
HISTORY_AUDIT_CSV = RESEARCH_HISTORY_DIR / "w_bottom_candidate_definition_audit.csv"

REQUIRED_COLUMNS = {
    "model_id",
    "research_id",
    "source_research_id",
    "source_candidate_set_id",
    "research_variant_id",
    "advisory_status",
    "stock_id",
    "signal_date",
    "outcome_category_id",
    "slope_curvature_category",
    "definition_status",
    "definition_issue_reasons",
    "chart_path",
    "prior_downtrend_pct",
    "support_gap_pct",
    "first_low_to_neckline_pct",
    "right_low_to_neckline_pct",
    "prior_downtrend_ok",
    "two_lows_same_support_zone",
    "second_low_not_effectively_broken",
    "neckline_valid",
    "right_side_holding_support",
    "price_neckline_breakout_confirmed",
    "volume_confirmed_breakout",
    "definition_base_ok",
    "manual_review_status",
    "approved_for_daily",
    "generated_at",
}

DEFINITION_STATUSES = {
    "definition_confirmed_with_volume",
    "price_confirmed_without_volume",
    "valid_right_side_watch",
    "late_or_no_breakout",
    "support_failed",
    "invalid_definition_structure",
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
    source = read_csv(SOURCE_CHART_REVIEW_CSV)
    latest = read_csv(LATEST_AUDIT_CSV)
    history = read_csv(HISTORY_AUDIT_CSV)
    if not LATEST_AUDIT_MD.exists():
        fail(f"missing required file: {LATEST_AUDIT_MD}")
    md_lines = LATEST_AUDIT_MD.read_text(encoding="utf-8", errors="replace").splitlines()
    if len(md_lines) < 30:
        fail(f"{LATEST_AUDIT_MD} is suspiciously short")
    if latest.empty:
        fail(f"{LATEST_AUDIT_CSV} has no rows")
    if len(latest) != len(history):
        fail("latest and history definition audit row counts differ")
    if len(latest) != len(source):
        fail(f"definition audit rows must equal chart review rows: latest={len(latest)} source={len(source)}")

    missing = sorted(REQUIRED_COLUMNS - set(latest.columns))
    if missing:
        fail(f"{LATEST_AUDIT_CSV} missing columns: {missing}")
    missing_history = sorted(REQUIRED_COLUMNS - set(history.columns))
    if missing_history:
        fail(f"{HISTORY_AUDIT_CSV} missing columns: {missing_history}")

    forbidden = sorted((set(latest.columns) | set(history.columns)) & FORBIDDEN_PRODUCTION_FIELDS)
    if forbidden:
        fail(f"W-bottom definition audit must not emit production decision fields: {forbidden}")

    if set(latest["model_id"].astype(str)) != {"w_bottom_right_side"}:
        fail("definition audit model_id must be w_bottom_right_side")
    if set(latest["research_id"].astype(str)) != {"w_bottom_candidate_definition_audit"}:
        fail("definition audit research_id must be w_bottom_candidate_definition_audit")
    if set(latest["source_research_id"].astype(str)) != {"w_bottom_candidate_chart_review"}:
        fail("definition audit source_research_id must be w_bottom_candidate_chart_review")
    if set(latest["research_variant_id"].astype(str)) != {"warning_research_variant_only"}:
        fail("definition audit must be marked warning_research_variant_only")
    if set(latest["advisory_status"].astype(str)) != {"warning_research_variant_only"}:
        fail("definition audit advisory_status must be warning_research_variant_only")
    if set(latest["manual_review_status"].astype(str)) != {"pending_user_shape_review"}:
        fail("definition audit manual_review_status must remain pending_user_shape_review")
    if not false_only(latest["approved_for_daily"]):
        fail("definition audit approved_for_daily must remain false")

    invalid_statuses = sorted(set(latest["definition_status"].astype(str)) - DEFINITION_STATUSES)
    if invalid_statuses:
        fail(f"unexpected definition_status values: {invalid_statuses}")
    for column in [
        "prior_downtrend_ok",
        "two_lows_same_support_zone",
        "second_low_not_effectively_broken",
        "neckline_valid",
        "right_side_holding_support",
        "price_neckline_breakout_confirmed",
        "volume_confirmed_breakout",
        "definition_base_ok",
    ]:
        if not boolish_only(latest[column]):
            fail(f"{column} must be boolean-like")

    for column in [
        "prior_downtrend_pct",
        "support_gap_pct",
        "first_low_to_neckline_pct",
        "right_low_to_neckline_pct",
    ]:
        values = pd.to_numeric(latest[column], errors="coerce")
        if values.isna().any():
            fail(f"{column} must be numeric for every audited row")

    for row_number, row in latest.iterrows():
        chart_path = Path(str(row.get("chart_path", "")))
        if not chart_path.exists():
            fail(f"missing chart image at row {row_number}: {chart_path}")

    print(
        "W-bottom candidate definition audit validation passed "
        f"rows={len(latest)} definition_statuses={sorted(set(latest['definition_status']))}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
