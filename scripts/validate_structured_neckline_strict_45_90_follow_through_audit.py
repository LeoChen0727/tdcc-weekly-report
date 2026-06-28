from __future__ import annotations

from pathlib import Path

import pandas as pd

from build_structured_neckline_strict_45_90_follow_through_audit import (
    EVENT_COLUMNS,
    FOLLOW_THROUGH_SCOPE_ID,
    FOLLOW_THROUGH_THRESHOLDS,
    FORBIDDEN_PRODUCTION_FIELDS,
    HISTORY_EVENT_CSV,
    HISTORY_SUMMARY_CSV,
    LATEST_EVENT_CSV,
    LATEST_MD,
    LATEST_SUMMARY_CSV,
    PARAMETER_SET_ID,
    PRODUCTION_READINESS,
    RESEARCH_ID,
    RESEARCH_VARIANT_ID,
    SUMMARY_COLUMNS,
    TARGET_RISK_RULE_ID,
    TARGET_SEGMENT_ID,
    WINDOW_SESSIONS,
)


def fail(message: str) -> None:
    print(f"ERROR: {message}")
    raise SystemExit(1)


def read_csv(path: Path) -> pd.DataFrame:
    if not path.exists():
        fail(f"missing required file: {path}")
    try:
        return pd.read_csv(path, dtype=str, keep_default_na=False, encoding="utf-8-sig")
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
        "follow_through_scope_id": FOLLOW_THROUGH_SCOPE_ID,
        "production_readiness": PRODUCTION_READINESS,
    }
    for column, expected in constants.items():
        values = set(frame[column].astype(str))
        if values != {expected}:
            fail(f"{label} {column} must be {expected}; got {sorted(values)}")
    if not false_only(frame["approved_for_daily"]):
        fail(f"{label} approved_for_daily must remain false")


def validate_events(events: pd.DataFrame, label: str) -> None:
    require_columns(events, EVENT_COLUMNS, label)
    if len(events) != 48:
        fail(f"{label} must contain 48 strict 45/90 rows; got {len(events)}")
    validate_constants(events, label)
    if set(events["risk_penalty_rule_id"].astype(str)) != {TARGET_RISK_RULE_ID}:
        fail(f"{label} risk_penalty_rule_id must be {TARGET_RISK_RULE_ID}")
    if set(events["segment_id"].astype(str)) != {TARGET_SEGMENT_ID}:
        fail(f"{label} segment_id must be {TARGET_SEGMENT_ID}")
    outcomes = events["outcome_result"].astype(str).value_counts().to_dict()
    expected = {"win": 27, "neutral": 11, "loss": 10}
    if outcomes != expected:
        fail(f"{label} outcome counts changed: got={outcomes} expected={expected}")
    if events.duplicated(["stock_id", "signal_date", "retest_entry_date"]).any():
        fail(f"{label} has duplicate event keys")
    statuses = events["follow_through_data_status"].astype(str).value_counts().to_dict()
    if statuses != {"available": 47, "unavailable": 1}:
        fail(f"{label} follow_through_data_status changed: {statuses}")
    available = events["follow_through_data_status"].astype(str).eq("available")
    for column in [
        "entry_price",
        "return_pct",
        "max_close_return_1_session_pct",
        "max_close_return_2_session_pct",
        "max_close_return_3_session_pct",
        "max_close_return_5_session_pct",
        "min_close_return_5_session_pct",
    ]:
        values = pd.to_numeric(events.loc[available, column], errors="coerce")
        if values.isna().any():
            fail(f"{label} {column} must be numeric for every available row")
    bool_columns = ["weak_follow_through_5d_lt5pct", "weak_follow_through_3d_lt3pct", "early_adverse_3d_le_minus5pct"]
    for column in bool_columns:
        values = set(events[column].astype(str).str.lower().unique())
        if values - {"true", "false", "unknown"}:
            fail(f"{label} {column} has unexpected boolean values: {sorted(values)}")
    if not events.loc[events["outcome_result"].eq("loss") & available, "weak_follow_through_5d_lt5pct"].astype(str).str.lower().eq("true").all():
        fail(f"{label} loss rows should still show weak 5-session follow-through")
    forbidden = sorted(set(events.columns) & FORBIDDEN_PRODUCTION_FIELDS)
    if forbidden:
        fail(f"{label} contains forbidden production fields: {forbidden}")


def validate_summary(summary: pd.DataFrame, label: str) -> None:
    require_columns(summary, SUMMARY_COLUMNS, label)
    expected_rows = len(WINDOW_SESSIONS) * len(FOLLOW_THROUGH_THRESHOLDS)
    if len(summary) != expected_rows:
        fail(f"{label} must contain {expected_rows} grid rows; got {len(summary)}")
    validate_constants(summary, label)
    if set(summary["rule_type"].astype(str)) != {"diagnostic_future_known_filter_not_original_entry_rule"}:
        fail(f"{label} rule_type must preserve future-known diagnostic boundary")
    if not summary["interpretation"].astype(str).str.contains("confirmation_entry_hypothesis_or_risk_label_only", regex=False).all():
        fail(f"{label} interpretation must state confirmation-entry or risk-label only")
    if set(pd.to_numeric(summary["max_window_sessions"], errors="coerce").astype(int)) != set(WINDOW_SESSIONS):
        fail(f"{label} max_window_sessions mismatch")
    if set(pd.to_numeric(summary["min_follow_through_pct"], errors="coerce").round(4)) != set(FOLLOW_THROUGH_THRESHOLDS):
        fail(f"{label} min_follow_through_pct mismatch")
    accepted = pd.to_numeric(summary["accepted_count"], errors="coerce")
    rejected = pd.to_numeric(summary["rejected_count"], errors="coerce")
    unavailable = pd.to_numeric(summary["unavailable_count"], errors="coerce")
    if not ((accepted + rejected + unavailable) == 48).all():
        fail(f"{label} every rule must partition all 48 rows")
    if set(unavailable.astype(int)) != {1}:
        fail(f"{label} unavailable_count must be 1 for every rule")
    if pd.to_numeric(summary["accepted_loss_count"], errors="coerce").min() < 0:
        fail(f"{label} accepted_loss_count must be non-negative")
    forbidden = sorted(set(summary.columns) & FORBIDDEN_PRODUCTION_FIELDS)
    if forbidden:
        fail(f"{label} contains forbidden production fields: {forbidden}")


def validate_markdown() -> None:
    if not LATEST_MD.exists():
        fail(f"missing markdown summary: {LATEST_MD}")
    text = LATEST_MD.read_text(encoding="utf-8", errors="replace")
    required = [
        "production impact: `none`",
        "known only after the original entry date",
        "must not be used as original-entry filters",
        "follow_through_data_status=unavailable",
        "confirmation_next_open",
        "not themselves a production rule",
        PRODUCTION_READINESS,
    ]
    for item in required:
        if item not in text:
            fail(f"markdown missing required text: {item}")


def main() -> int:
    latest_events = read_csv(LATEST_EVENT_CSV)
    latest_summary = read_csv(LATEST_SUMMARY_CSV)
    history_events = read_csv(HISTORY_EVENT_CSV)
    history_summary = read_csv(HISTORY_SUMMARY_CSV)

    validate_events(latest_events, "latest events")
    validate_events(history_events, "history events")
    validate_summary(latest_summary, "latest summary")
    validate_summary(history_summary, "history summary")
    if len(latest_events) != len(history_events):
        fail("latest/history event counts differ")
    if len(latest_summary) != len(history_summary):
        fail("latest/history summary counts differ")
    validate_markdown()

    print(
        "structured neckline strict 45/90 follow-through audit validation passed "
        f"events={len(latest_events)} summary_rows={len(latest_summary)}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
