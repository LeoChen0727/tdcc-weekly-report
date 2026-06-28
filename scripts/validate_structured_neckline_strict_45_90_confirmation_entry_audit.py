from __future__ import annotations

from pathlib import Path

import pandas as pd

from build_structured_neckline_strict_45_90_confirmation_entry_audit import (
    CONFIRMATION_SCOPE_ID,
    DETAIL_COLUMNS,
    FOLLOW_THROUGH_THRESHOLDS,
    FORBIDDEN_PRODUCTION_FIELDS,
    HISTORY_DETAIL_CSV,
    HISTORY_SUMMARY_CSV,
    LATEST_DETAIL_CSV,
    LATEST_MD,
    LATEST_SUMMARY_CSV,
    PARAMETER_SET_ID,
    PRODUCTION_READINESS,
    RESEARCH_ID,
    RESEARCH_VARIANT_ID,
    SUMMARY_COLUMNS,
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
        "confirmation_scope_id": CONFIRMATION_SCOPE_ID,
        "production_readiness": PRODUCTION_READINESS,
    }
    for column, expected in constants.items():
        values = set(frame[column].astype(str))
        if values != {expected}:
            fail(f"{label} {column} must be {expected}; got {sorted(values)}")
    if not false_only(frame["approved_for_daily"]):
        fail(f"{label} approved_for_daily must remain false")


def validate_detail(detail: pd.DataFrame, label: str) -> None:
    require_columns(detail, DETAIL_COLUMNS, label)
    if detail.empty:
        fail(f"{label} must not be empty")
    validate_constants(detail, label)
    statuses = set(detail["tradability_status"].astype(str))
    if not statuses <= {"tradable", "missing_price_history_file", "confirmation_signal_date_missing", "missing_next_open_after_confirmation", "insufficient_exit_window", "invalid_confirmation_entry_price"}:
        fail(f"{label} unexpected tradability_status: {sorted(statuses)}")
    tradable = detail["tradability_status"].astype(str).eq("tradable")
    if not tradable.any():
        fail(f"{label} must include tradable rows")
    outcomes = set(detail.loc[tradable, "outcome_result"].astype(str))
    if not outcomes <= {"win", "neutral", "loss"}:
        fail(f"{label} unexpected outcome_result: {sorted(outcomes)}")
    for column in ["confirmation_entry_price", "return_pct", "max_close_return_pct", "min_close_return_pct"]:
        values = pd.to_numeric(detail.loc[tradable, column], errors="coerce")
        if values.isna().any():
            fail(f"{label} {column} must be numeric for tradable rows")
    forbidden = sorted(set(detail.columns) & FORBIDDEN_PRODUCTION_FIELDS)
    if forbidden:
        fail(f"{label} contains forbidden production fields: {forbidden}")


def validate_summary(summary: pd.DataFrame, label: str) -> None:
    require_columns(summary, SUMMARY_COLUMNS, label)
    expected_rows = len(WINDOW_SESSIONS) * len(FOLLOW_THROUGH_THRESHOLDS)
    if len(summary) != expected_rows:
        fail(f"{label} must contain {expected_rows} grid rows; got {len(summary)}")
    validate_constants(summary, label)
    if set(pd.to_numeric(summary["max_window_sessions"], errors="coerce").astype(int)) != set(WINDOW_SESSIONS):
        fail(f"{label} max_window_sessions mismatch")
    if set(pd.to_numeric(summary["min_follow_through_pct"], errors="coerce").round(4)) != set(FOLLOW_THROUGH_THRESHOLDS):
        fail(f"{label} min_follow_through_pct mismatch")
    source_accepted = pd.to_numeric(summary["source_accepted_count"], errors="coerce")
    tradable = pd.to_numeric(summary["tradable_entry_count"], errors="coerce")
    incomplete = pd.to_numeric(summary["incomplete_count"], errors="coerce")
    if not ((tradable + incomplete) == source_accepted).all():
        fail(f"{label} tradable + incomplete must equal source_accepted")
    if not summary["interpretation"].astype(str).str.contains("confirmation_next_open_research_only", regex=False).all():
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
        "next open after the confirmation close",
        "research-only",
        "not a production promotion",
        PRODUCTION_READINESS,
    ]
    for item in required:
        if item not in text:
            fail(f"markdown missing required text: {item}")


def main() -> int:
    latest_detail = read_csv(LATEST_DETAIL_CSV)
    latest_summary = read_csv(LATEST_SUMMARY_CSV)
    history_detail = read_csv(HISTORY_DETAIL_CSV)
    history_summary = read_csv(HISTORY_SUMMARY_CSV)
    validate_detail(latest_detail, "latest detail")
    validate_detail(history_detail, "history detail")
    validate_summary(latest_summary, "latest summary")
    validate_summary(history_summary, "history summary")
    validate_markdown()
    print(
        "structured neckline strict 45/90 confirmation entry audit validation passed "
        f"detail_rows={len(latest_detail)} summary_rows={len(latest_summary)}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
