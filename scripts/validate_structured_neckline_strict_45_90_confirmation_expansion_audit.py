from __future__ import annotations

from pathlib import Path

import pandas as pd

from build_structured_neckline_strict_45_90_confirmation_expansion_audit import (
    CONFIRMATION_SCOPE_ID,
    DETAIL_COLUMNS,
    EVENT_COLUMNS,
    FORBIDDEN_PRODUCTION_FIELDS,
    FOLLOW_THROUGH_THRESHOLDS,
    HISTORY_DETAIL_CSV,
    HISTORY_EVENT_CSV,
    HISTORY_SUMMARY_CSV,
    LATEST_DETAIL_CSV,
    LATEST_EVENT_CSV,
    LATEST_MD,
    LATEST_SUMMARY_CSV,
    PARAMETER_SET_ID,
    PRODUCTION_READINESS,
    RESEARCH_ID,
    RESEARCH_VARIANT_ID,
    SUMMARY_COLUMNS,
    TARGET_RISK_RULE_ID,
    WINDOW_SESSIONS,
)

EXPECTED_EVENT_COUNT = 313
EXPECTED_DETAIL_ROWS = 1782
EXPECTED_SCOPES = {
    "all_strict_45_90": 313,
    "low_position_le60_market_bull": 48,
    "non_low_position_le60_market_bull": 265,
    "low_position_le60_any_market": 56,
    "low_position_gt60_or_unknown": 257,
    "market_regime_strong_bull": 234,
    "market_regime_mild_bull": 35,
    "market_regime_range_or_mixed": 24,
    "market_regime_correction": 20,
}
EXPECTED_FOLLOW_THROUGH_STATUSES = {"available": 282, "unavailable": 31}


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
        "confirmation_scope_id": CONFIRMATION_SCOPE_ID,
        "production_readiness": PRODUCTION_READINESS,
    }
    for column, expected in constants.items():
        values = set(frame[column].astype(str))
        if values != {expected}:
            fail(f"{label} {column} must be {expected}; got {sorted(values)}")
    if not false_only(frame["approved_for_daily"]):
        fail(f"{label} approved_for_daily must remain false")


def parse_scopes(series: pd.Series) -> pd.Series:
    return series.astype(str).str.split(";")


def has_scope(frame: pd.DataFrame, scope_id: str) -> pd.Series:
    return parse_scopes(frame["analysis_scope_ids"]).apply(lambda parts: scope_id in parts)


def validate_events(events: pd.DataFrame, label: str) -> None:
    require_columns(events, EVENT_COLUMNS, label)
    if len(events) != EXPECTED_EVENT_COUNT:
        fail(f"{label} must contain {EXPECTED_EVENT_COUNT} strict 45/90 rows; got {len(events)}")
    validate_constants(events, label)
    if set(events["risk_penalty_rule_id"].astype(str)) != {TARGET_RISK_RULE_ID}:
        fail(f"{label} risk_penalty_rule_id must be {TARGET_RISK_RULE_ID}")
    if events["source_event_key"].duplicated().any():
        fail(f"{label} source_event_key must be unique")
    statuses = events["follow_through_data_status"].astype(str).value_counts().to_dict()
    if statuses != EXPECTED_FOLLOW_THROUGH_STATUSES:
        fail(f"{label} follow_through_data_status changed: got={statuses} expected={EXPECTED_FOLLOW_THROUGH_STATUSES}")
    for scope_id, expected_count in EXPECTED_SCOPES.items():
        actual = int(has_scope(events, scope_id).sum())
        if actual != expected_count:
            fail(f"{label} {scope_id} count changed: got={actual} expected={expected_count}")
    for column in [
        "entry_price",
        "original_return_pct",
        "max_close_return_1_session_pct",
        "max_close_return_2_session_pct",
        "max_close_return_3_session_pct",
        "max_close_return_5_session_pct",
    ]:
        available = events["follow_through_data_status"].astype(str).eq("available")
        values = pd.to_numeric(events.loc[available, column], errors="coerce")
        if values.isna().any():
            fail(f"{label} {column} must be numeric for every available row")
    forbidden = sorted(set(events.columns) & FORBIDDEN_PRODUCTION_FIELDS)
    if forbidden:
        fail(f"{label} contains forbidden production fields: {forbidden}")


def validate_detail(detail: pd.DataFrame, label: str) -> None:
    require_columns(detail, DETAIL_COLUMNS, label)
    if len(detail) != EXPECTED_DETAIL_ROWS:
        fail(f"{label} must contain {EXPECTED_DETAIL_ROWS} rows; got {len(detail)}")
    validate_constants(detail, label)
    rule_count = len(WINDOW_SESSIONS) * len(FOLLOW_THROUGH_THRESHOLDS)
    if detail["confirmation_rule_id"].nunique() != rule_count:
        fail(f"{label} must cover {rule_count} confirmation rules")
    statuses = set(detail["tradability_status"].astype(str))
    if statuses != {"tradable"}:
        fail(f"{label} currently expects all detail rows tradable; got {sorted(statuses)}")
    outcomes = set(detail["outcome_result"].astype(str))
    if not outcomes <= {"win", "neutral", "loss"}:
        fail(f"{label} unexpected outcome_result: {sorted(outcomes)}")
    for column in ["confirmation_entry_price", "return_pct", "max_close_return_pct", "min_close_return_pct"]:
        values = pd.to_numeric(detail[column], errors="coerce")
        if values.isna().any():
            fail(f"{label} {column} must be numeric")
    forbidden = sorted(set(detail.columns) & FORBIDDEN_PRODUCTION_FIELDS)
    if forbidden:
        fail(f"{label} contains forbidden production fields: {forbidden}")


def validate_summary(summary: pd.DataFrame, label: str) -> None:
    require_columns(summary, SUMMARY_COLUMNS, label)
    expected_rows = len(EXPECTED_SCOPES) * len(WINDOW_SESSIONS) * len(FOLLOW_THROUGH_THRESHOLDS)
    if len(summary) != expected_rows:
        fail(f"{label} must contain {expected_rows} grid rows; got {len(summary)}")
    validate_constants(summary, label)
    if set(summary["analysis_scope_id"].astype(str)) != set(EXPECTED_SCOPES):
        fail(f"{label} analysis_scope_id mismatch")
    if set(pd.to_numeric(summary["max_window_sessions"], errors="coerce").astype(int)) != set(WINDOW_SESSIONS):
        fail(f"{label} max_window_sessions mismatch")
    if set(pd.to_numeric(summary["min_follow_through_pct"], errors="coerce").round(4)) != set(FOLLOW_THROUGH_THRESHOLDS):
        fail(f"{label} min_follow_through_pct mismatch")
    for scope_id, expected_count in EXPECTED_SCOPES.items():
        scoped = summary[summary["analysis_scope_id"].astype(str).eq(scope_id)]
        counts = set(pd.to_numeric(scoped["scope_event_count"], errors="coerce").astype(int))
        if counts != {expected_count}:
            fail(f"{label} {scope_id} scope_event_count changed: {sorted(counts)}")
    source_accepted = pd.to_numeric(summary["source_accepted_count"], errors="coerce")
    tradable = pd.to_numeric(summary["tradable_entry_count"], errors="coerce")
    incomplete = pd.to_numeric(summary["incomplete_count"], errors="coerce")
    if not ((tradable + incomplete) == source_accepted).all():
        fail(f"{label} tradable + incomplete must equal source_accepted")
    if set(incomplete.astype(int)) != {0}:
        fail(f"{label} currently expects incomplete_count=0")
    if not summary["interpretation"].astype(str).str.contains("confirmation_next_open_expansion_research_only", regex=False).all():
        fail(f"{label} interpretation must stay research-only")
    forbidden = sorted(set(summary.columns) & FORBIDDEN_PRODUCTION_FIELDS)
    if forbidden:
        fail(f"{label} contains forbidden production fields: {forbidden}")


def validate_markdown() -> None:
    if not LATEST_MD.exists():
        fail(f"missing markdown summary: {LATEST_MD}")
    text = LATEST_MD.read_text(encoding="utf-8", errors="replace")
    required = [
        "production impact: `none`",
        "strict 45/90 confirmation-next-open hypothesis",
        "research-only",
        "not a production promotion",
        PRODUCTION_READINESS,
    ]
    for item in required:
        if item not in text:
            fail(f"markdown missing required text: {item}")


def main() -> int:
    latest_events = read_csv(LATEST_EVENT_CSV)
    latest_detail = read_csv(LATEST_DETAIL_CSV)
    latest_summary = read_csv(LATEST_SUMMARY_CSV)
    history_events = read_csv(HISTORY_EVENT_CSV)
    history_detail = read_csv(HISTORY_DETAIL_CSV)
    history_summary = read_csv(HISTORY_SUMMARY_CSV)

    validate_events(latest_events, "latest events")
    validate_events(history_events, "history events")
    validate_detail(latest_detail, "latest detail")
    validate_detail(history_detail, "history detail")
    validate_summary(latest_summary, "latest summary")
    validate_summary(history_summary, "history summary")
    validate_markdown()
    print(
        "structured neckline strict 45/90 confirmation expansion audit validation passed "
        f"events={len(latest_events)} detail_rows={len(latest_detail)} summary_rows={len(latest_summary)}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
