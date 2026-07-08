from __future__ import annotations

from pathlib import Path

import pandas as pd

from build_volume_range_breakout_v2_next_day_continuation_timing_audit import (
    ADVISORY_STATUS,
    ARTIFACT_VERSION,
    DETAIL_COLUMNS,
    HISTORY_DETAIL_CSV,
    HISTORY_SUMMARY_CSV,
    LATEST_DETAIL_CSV,
    LATEST_MD,
    LATEST_SUMMARY_CSV,
    MODEL_ID,
    NEXT_DAY_TRIGGER_ID,
    PRODUCTION_READINESS,
    RESEARCH_ID,
    SOURCE_RESEARCH_ID,
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


def false_only(series: pd.Series) -> bool:
    return set(series.astype(str).str.lower().unique()) <= {"false", "0", ""}


def require_single(summary: pd.DataFrame, row_type: str, audit_scope: str, audit_key: str) -> pd.Series:
    rows = summary[
        summary["row_type"].astype(str).eq(row_type)
        & summary["audit_scope"].astype(str).eq(audit_scope)
        & summary["audit_key"].astype(str).eq(audit_key)
    ]
    if len(rows) != 1:
        fail(f"expected exactly one summary row for {row_type}/{audit_scope}/{audit_key}; got {len(rows)}")
    return rows.iloc[0]


def validate_common(summary: pd.DataFrame, detail: pd.DataFrame, history_summary: pd.DataFrame, history_detail: pd.DataFrame) -> None:
    if summary.empty:
        fail("summary output must not be empty")
    if detail.empty:
        fail("detail output must not be empty")
    if len(summary) != len(history_summary):
        fail("latest/history summary row counts differ")
    if len(detail) != len(history_detail):
        fail("latest/history detail row counts differ")
    missing_summary = sorted(set(SUMMARY_COLUMNS) - set(summary.columns))
    missing_detail = sorted(set(DETAIL_COLUMNS) - set(detail.columns))
    if missing_summary:
        fail(f"summary missing columns: {missing_summary}")
    if missing_detail:
        fail(f"detail missing columns: {missing_detail}")
    forbidden = sorted((set(summary.columns) | set(detail.columns)) & FORBIDDEN_PRODUCTION_FIELDS)
    if forbidden:
        fail(f"timing audit outputs must not contain production decision fields: {forbidden}")
    for name, df in [("summary", summary), ("detail", detail)]:
        if set(df["research_id"].astype(str)) != {RESEARCH_ID}:
            fail(f"{name} research_id must be {RESEARCH_ID}")
        if set(df["artifact_version"].astype(str)) != {ARTIFACT_VERSION}:
            fail(f"{name} artifact_version must be {ARTIFACT_VERSION}")
        if set(df["source_research_id"].astype(str)) != {SOURCE_RESEARCH_ID}:
            fail(f"{name} source_research_id must be {SOURCE_RESEARCH_ID}")
        if set(df["advisory_status"].astype(str)) != {ADVISORY_STATUS}:
            fail(f"{name} advisory_status must be {ADVISORY_STATUS}")
        if set(df["model_id"].astype(str)) != {MODEL_ID}:
            fail(f"{name} model_id must be {MODEL_ID}")
        if set(df["production_readiness"].astype(str)) != {PRODUCTION_READINESS}:
            fail(f"{name} production_readiness must be {PRODUCTION_READINESS}")
        if not false_only(df["approved_for_daily"]):
            fail(f"{name} approved_for_daily must remain false")


def validate_detail_timing(detail: pd.DataFrame) -> None:
    if detail["source_event_key"].duplicated().any():
        dupes = detail[detail["source_event_key"].duplicated()]["source_event_key"].head(5).tolist()
        fail(f"detail contains duplicate source_event_key values: {dupes}")
    if set(detail["follow_through_type"].astype(str)) != {"next_day_continuation"}:
        fail("detail must contain only next_day_continuation rows")
    if not detail["matched_trigger_ids"].astype(str).str.contains(NEXT_DAY_TRIGGER_ID, regex=False).all():
        fail("every detail row must match next_day_continuation_confirmed")
    if not detail["confirmation_age_trading_days"].astype(str).eq("1").all():
        fail("next_day_continuation rows must have confirmation_age_trading_days=1")
    if not detail["entry_rule_id"].astype(str).eq("confirmation_next_open").all():
        fail("entry_rule_id must remain confirmation_next_open")
    if not (detail["entry_date"].astype(str) > detail["confirmation_date"].astype(str)).all():
        fail("entry_date must be after confirmation_date for every row")
    if not (detail["confirmation_date"].astype(str) > detail["signal_date"].astype(str)).all():
        fail("confirmation_date must be after signal_date for every row")
    if not detail["known_before_entry_open"].astype(str).eq("True").all():
        fail("next_day_continuation must be known before entry open")
    if detail["uses_post_entry_information"].astype(str).eq("True").any():
        fail("next_day_continuation audit must not use post-entry information")
    if detail["would_change_confirmation_date"].astype(str).eq("True").any():
        fail("next_day_continuation filter must not change current confirmation_date in this artifact")
    if detail["would_change_entry_date"].astype(str).eq("True").any():
        fail("next_day_continuation filter must not change current entry_date in this artifact")
    if not detail["timing_audit_status"].astype(str).eq("known_after_confirmation_close_before_entry_open").all():
        fail("all detail rows must be classified as known_after_confirmation_close_before_entry_open")


def validate_summary(summary: pd.DataFrame, detail: pd.DataFrame) -> None:
    availability = require_single(
        summary,
        "timing_availability",
        "all_next_day_continuation",
        "all_next_day_continuation",
    )
    if int(availability["sample_size"]) != len(detail):
        fail("timing availability sample_size must match detail rows")
    if int(availability["known_before_entry_open_count"]) != len(detail):
        fail("all next_day_continuation rows must be known before entry open")
    if int(availability["future_leak_count"]) != 0:
        fail("future_leak_count must be zero")
    if int(availability["would_change_confirmation_date_count"]) != 0:
        fail("would_change_confirmation_date_count must be zero")
    if int(availability["would_change_entry_date_count"]) != 0:
        fail("would_change_entry_date_count must be zero")
    if availability["status"] != "timing_verified_research_only":
        fail("timing availability status must be timing_verified_research_only")
    if "not_known_on_signal_date_close" not in str(availability["value_c"]):
        fail("timing availability must record that condition is not known on signal-date close")

    counts: dict[int, int] = {}
    for window in [20, 40, 60]:
        row = require_single(
            summary,
            "high_window_timing_metrics",
            "next_day_continuation_by_previous_high_window",
            f"previous_{window}d_high_next_day_continuation",
        )
        counts[window] = int(row["sample_size"])
        if int(row["known_before_entry_open_count"]) != int(row["sample_size"]):
            fail(f"window {window} must be fully known before entry open")
        if row["status"] != "timing_verified_research_only":
            fail(f"window {window} status must be timing_verified_research_only")
    if not (counts[20] >= counts[40] >= counts[60] > 0):
        fail(f"high-window timing counts must be monotonic 20>=40>=60>0; got {counts}")

    impact = require_single(
        summary,
        "operation_date_impact",
        "confirmation_and_entry_dates",
        "no_date_change_if_used_as_additional_filter",
    )
    if impact["status"] != "does_not_change_current_confirmation_or_entry_dates":
        fail("operation date impact must record no date change")
    leak = require_single(summary, "future_leak_check", "post_entry_information", "no_post_entry_information_required")
    if leak["status"] != "no_future_leak_detected":
        fail("future-leak summary must record no_future_leak_detected")


def validate_markdown() -> None:
    if not LATEST_MD.exists():
        fail(f"missing markdown output: {LATEST_MD}")
    text = LATEST_MD.read_text(encoding="utf-8", errors="replace")
    required = [
        "research-only",
        "does not change `stock_model_contract_registry.csv`",
        "not known at signal-date close",
        "available before the formal buy open",
        "no row uses post-entry information",
    ]
    for item in required:
        if item not in text:
            fail(f"markdown missing required text: {item}")


def main() -> int:
    summary = read_csv(LATEST_SUMMARY_CSV)
    detail = read_csv(LATEST_DETAIL_CSV)
    history_summary = read_csv(HISTORY_SUMMARY_CSV)
    history_detail = read_csv(HISTORY_DETAIL_CSV)
    validate_common(summary, detail, history_summary, history_detail)
    validate_detail_timing(detail)
    validate_summary(summary, detail)
    validate_markdown()
    print(
        "volume range breakout v2 next-day continuation timing audit validation passed "
        f"summary_rows={len(summary)} detail_rows={len(detail)}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
