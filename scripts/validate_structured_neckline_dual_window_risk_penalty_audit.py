from __future__ import annotations

from pathlib import Path

import pandas as pd

from build_structured_neckline_dual_window_risk_penalty_audit import (
    DETAIL_COLUMNS,
    HISTORY_DETAIL_CSV,
    HISTORY_MANUAL_ALIGNMENT_CSV,
    HISTORY_SUMMARY_CSV,
    LATEST_DETAIL_CSV,
    LATEST_MANUAL_ALIGNMENT_CSV,
    LATEST_MD,
    LATEST_SUMMARY_CSV,
    MANUAL_ALIGNMENT_COLUMNS,
    PARAMETER_SET_ID,
    PRODUCTION_READINESS,
    RESEARCH_ID,
    RESEARCH_VARIANT_ID,
    RISK_PENALTY_SCOPE_ID,
    RISK_RULE_IDS,
    SOURCE_RULE_ID,
    SUMMARY_COLUMNS,
)


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


def require_columns(frame: pd.DataFrame, columns: list[str], label: str) -> None:
    missing = sorted(set(columns) - set(frame.columns))
    if missing:
        fail(f"{label} missing columns: {missing}")


def false_only(series: pd.Series) -> bool:
    return set(series.astype(str).str.lower().unique()) <= {"false", "0", ""}


def validate_constants(frame: pd.DataFrame, label: str) -> None:
    constants = {
        "research_id": RESEARCH_ID,
        "research_variant_id": RESEARCH_VARIANT_ID,
        "parameter_set_id": PARAMETER_SET_ID,
        "advisory_status": RESEARCH_VARIANT_ID,
        "risk_penalty_scope_id": RISK_PENALTY_SCOPE_ID,
        "production_readiness": PRODUCTION_READINESS,
    }
    for column, expected in constants.items():
        values = set(frame[column].astype(str))
        if values != {expected}:
            fail(f"{label} {column} must be {expected}; got {sorted(values)}")
    if not false_only(frame["approved_for_daily"]):
        fail(f"{label} approved_for_daily must remain false")


def validate_rule_ids(frame: pd.DataFrame, column: str, label: str) -> None:
    got = sorted(set(frame[column].astype(str)))
    if got != sorted(RISK_RULE_IDS):
        fail(f"{label} {column} must be {RISK_RULE_IDS}; got {got}")


def validate_detail(detail: pd.DataFrame) -> None:
    require_columns(detail, DETAIL_COLUMNS, "detail")
    validate_constants(detail, "detail")
    validate_rule_ids(detail, "risk_penalty_rule_id", "detail")

    source_rules = set(detail["source_candidate_rule_id"].astype(str))
    if source_rules != {SOURCE_RULE_ID}:
        fail(f"detail source_candidate_rule_id must be {SOURCE_RULE_ID}; got {sorted(source_rules)}")

    source_events = detail["source_event_key"].nunique()
    if source_events < 300:
        fail(f"detail source events too small: {source_events}")
    expected_rows = source_events * len(RISK_RULE_IDS)
    if len(detail) != expected_rows:
        fail(f"detail rows must equal source_events * risk_rule_count; got {len(detail)} vs {expected_rows}")

    accepts = set(detail["risk_penalty_candidate_accept"].astype(str))
    if not accepts <= {"true", "false"}:
        fail(f"risk_penalty_candidate_accept has unexpected values: {sorted(accepts - {'true', 'false'})}")
    if not detail.groupby("risk_penalty_rule_id")["risk_penalty_candidate_accept"].apply(lambda s: (s == "true").any()).all():
        fail("every risk penalty rule must accept at least one row")

    points = pd.to_numeric(detail["risk_penalty_points"], errors="coerce")
    if points.isna().any() or (points < 0).any():
        fail("risk_penalty_points must be non-negative numeric values")

    manual = detail.loc[detail["manual_label_status"].isin(["manual_good", "manual_bad"])]
    if manual["source_event_key"].nunique() < 10:
        fail("detail must retain at least 10 non-conflict manually labeled events")

    if FORBIDDEN_PRODUCTION_FIELDS & set(detail.columns):
        fail(f"detail contains forbidden production fields: {sorted(FORBIDDEN_PRODUCTION_FIELDS & set(detail.columns))}")


def validate_summary(summary: pd.DataFrame) -> None:
    require_columns(summary, SUMMARY_COLUMNS, "summary")
    if summary.empty:
        fail("summary must not be empty")
    validate_constants(summary, "summary")
    validate_rule_ids(summary, "risk_penalty_rule_id", "summary")
    if "low_position_le60_market_bull" not in set(summary["analysis_scope_id"].astype(str)):
        fail("summary must include low_position_le60_market_bull")
    if FORBIDDEN_PRODUCTION_FIELDS & set(summary.columns):
        fail(f"summary contains forbidden production fields: {sorted(FORBIDDEN_PRODUCTION_FIELDS & set(summary.columns))}")


def validate_manual_alignment(alignment: pd.DataFrame) -> None:
    require_columns(alignment, MANUAL_ALIGNMENT_COLUMNS, "manual_alignment")
    if alignment.empty:
        fail("manual_alignment must not be empty")
    validate_constants(alignment, "manual_alignment")
    validate_rule_ids(alignment, "risk_penalty_rule_id", "manual_alignment")
    good_rows = pd.to_numeric(alignment["manual_good_rows"], errors="coerce").fillna(0)
    bad_rows = pd.to_numeric(alignment["manual_bad_rows"], errors="coerce").fillna(0)
    if not (good_rows > 0).all() or not (bad_rows > 0).all():
        fail("manual_alignment must include positive manual good and bad rows for every rule")
    if FORBIDDEN_PRODUCTION_FIELDS & set(alignment.columns):
        fail(f"manual_alignment contains forbidden production fields: {sorted(FORBIDDEN_PRODUCTION_FIELDS & set(alignment.columns))}")


def main() -> int:
    detail = read_csv(LATEST_DETAIL_CSV)
    summary = read_csv(LATEST_SUMMARY_CSV)
    alignment = read_csv(LATEST_MANUAL_ALIGNMENT_CSV)
    history_detail = read_csv(HISTORY_DETAIL_CSV)
    history_summary = read_csv(HISTORY_SUMMARY_CSV)
    history_alignment = read_csv(HISTORY_MANUAL_ALIGNMENT_CSV)

    validate_detail(detail)
    validate_detail(history_detail)
    validate_summary(summary)
    validate_summary(history_summary)
    validate_manual_alignment(alignment)
    validate_manual_alignment(history_alignment)

    if not LATEST_MD.exists():
        fail(f"missing markdown summary: {LATEST_MD}")

    print(
        "structured neckline dual window risk penalty audit validation passed "
        f"detail_rows={len(detail)} summary_rows={len(summary)} manual_alignment_rows={len(alignment)}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
