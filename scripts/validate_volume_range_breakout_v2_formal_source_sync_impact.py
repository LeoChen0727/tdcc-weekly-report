from __future__ import annotations

from pathlib import Path

import pandas as pd

from build_volume_range_breakout_v2_formal_source_sync_impact import (
    ADVISORY_STATUS,
    ARTIFACT_VERSION,
    DETAIL_COLUMNS,
    HISTORY_DETAIL_CSV,
    HISTORY_SUMMARY_CSV,
    LATEST_DETAIL_CSV,
    LATEST_MD,
    LATEST_SUMMARY_CSV,
    MODEL_ID,
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
        fail(f"expected one summary row for {row_type}/{audit_scope}/{audit_key}; got {len(rows)}")
    return rows.iloc[0]


def validate_common(summary: pd.DataFrame, detail: pd.DataFrame, history_summary: pd.DataFrame, history_detail: pd.DataFrame) -> None:
    if summary.empty:
        fail("summary must not be empty")
    if detail.empty:
        fail("detail must not be empty")
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
        fail(f"formal source sync impact outputs must not contain production decision fields: {forbidden}")
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


def validate_summary(summary: pd.DataFrame) -> None:
    profile = require_single(summary, "source_profile", "formal_source_sync", "current_vs_existing_formal_events")
    inside = require_single(summary, "discussion_item", "formal_source_sync", "inside_existing_artifact_window_rows")
    extension = require_single(summary, "discussion_item", "formal_source_sync", "after_existing_artifact_window_rows")
    expected = {
        "current_formal_rows": 3292,
        "existing_formal_rows": 3245,
        "current_minus_existing_unique_keys": 39,
        "existing_minus_current_unique_keys": 0,
        "current_minus_existing_rows": 47,
        "inside_existing_window_rows": 7,
        "after_existing_window_rows": 40,
        "inside_existing_window_stocks": 4,
    }
    for col, value in expected.items():
        if int(profile[col]) != value:
            fail(f"profile {col} expected {value}; got {profile[col]}")
    if profile["status"] != "source_sync_required_before_promotion":
        fail("profile status must require source sync before promotion")
    if int(inside["sample_size"]) != 7:
        fail("inside existing-window discussion sample_size must be 7")
    if inside["status"] != "requires_user_discussion_source_sync_scope":
        fail("inside existing-window row must require user discussion")
    if int(extension["sample_size"]) != 40:
        fail("freshness-extension discussion sample_size must be 40")
    if extension["status"] != "expected_freshness_extension_requires_refresh":
        fail("freshness-extension row must require refresh")


def validate_detail(detail: pd.DataFrame) -> None:
    if len(detail) != 47:
        fail(f"detail expected 47 rows; got {len(detail)}")
    if detail["formal_row_key"].duplicated().any():
        dupes = detail[detail["formal_row_key"].duplicated()]["formal_row_key"].head(5).tolist()
        fail(f"detail formal_row_key must be unique: {dupes}")
    if detail["source_event_key"].nunique() != 39:
        fail(f"detail source_event_key unique count expected 39; got {detail['source_event_key'].nunique()}")
    if set(detail["diff_side"].astype(str)) != {"current_minus_existing"}:
        fail("detail must only list current_minus_existing rows")
    inside = detail[
        detail["sync_impact_classification"].astype(str).eq("inside_existing_artifact_window_source_sync_required")
    ]
    extension = detail[
        detail["sync_impact_classification"].astype(str).eq("after_existing_artifact_window_freshness_extension")
    ]
    if len(inside) != 7:
        fail(f"inside existing-window detail rows expected 7; got {len(inside)}")
    if len(extension) != 40:
        fail(f"freshness extension detail rows expected 40; got {len(extension)}")
    if set(inside["stock_id"].astype(str)) != {"8077", "9914", "3290", "9928"}:
        fail(f"inside existing-window stocks changed: {sorted(set(inside['stock_id'].astype(str)))}")
    if not inside["signal_date"].astype(str).le(inside["existing_max_signal_date"].astype(str)).all():
        fail("inside existing-window rows must have signal_date <= existing_max_signal_date")
    if not extension["signal_date"].astype(str).gt(extension["existing_max_signal_date"].astype(str)).all():
        fail("freshness extension rows must have signal_date > existing_max_signal_date")
    required_8077 = {"20260528", "20260529", "20260603", "20260604"}
    actual_8077 = set(inside[inside["stock_id"].astype(str).eq("8077")]["signal_date"].astype(str))
    if actual_8077 != required_8077:
        fail(f"8077 inside-window signal dates changed: {sorted(actual_8077)}")


def validate_markdown() -> None:
    if not LATEST_MD.exists():
        fail(f"missing markdown output: {LATEST_MD}")
    text = LATEST_MD.read_text(encoding="utf-8", errors="replace")
    required = [
        "non-writing research-only formal source sync impact audit",
        "does not rewrite `volume_breakout_formal_operation_events.csv`",
        "Discussion point",
        "inside the existing artifact window",
        "approved_for_daily: `False`",
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
    validate_summary(summary)
    validate_detail(detail)
    validate_markdown()
    print(
        "volume range breakout v2 formal source sync impact validation passed "
        f"summary_rows={len(summary)} detail_rows={len(detail)}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
