from __future__ import annotations

from pathlib import Path

import pandas as pd

from build_volume_range_breakout_v2_source_gap_reconciliation import (
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
        fail(f"source-gap reconciliation must not contain production decision fields: {forbidden}")
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


def validate_gap_detail(detail: pd.DataFrame) -> None:
    if detail["source_event_key"].duplicated().any():
        dupes = detail[detail["source_event_key"].duplicated()]["source_event_key"].head(5).tolist()
        fail(f"detail contains duplicate source_event_key values: {dupes}")
    if len(detail) != 10:
        fail(f"expected 10 raw-minus-timing rows; got {len(detail)}")
    allowed = {
        "freshness_extension_after_timing_window",
        "source_gap_inside_timing_window_promotion_blocker",
    }
    if not set(detail["gap_classification"].astype(str)) <= allowed:
        fail("detail contains unexpected gap_classification values")
    freshness = detail[detail["gap_classification"].astype(str).eq("freshness_extension_after_timing_window")]
    source_gap = detail[
        detail["gap_classification"].astype(str).eq("source_gap_inside_timing_window_promotion_blocker")
    ]
    if len(freshness) != 8:
        fail(f"expected 8 freshness-extension rows; got {len(freshness)}")
    if len(source_gap) != 2:
        fail(f"expected 2 inside-window source-gap rows; got {len(source_gap)}")
    if not freshness["signal_date"].astype(str).gt(freshness["timing_audit_max_signal_date"].astype(str)).all():
        fail("freshness-extension rows must have signal_date after timing_audit_max_signal_date")
    if not source_gap["signal_date"].astype(str).le(source_gap["timing_audit_max_signal_date"].astype(str)).all():
        fail("inside-window source-gap rows must be within timing audit max signal date")
    for col in [
        "present_in_raw_rerun",
        "present_in_timing_audit_60d",
        "present_in_semantic_audit",
        "present_in_formal_operation_events",
    ]:
        if not set(detail[col].astype(str)) <= {"True", "False"}:
            fail(f"{col} must be True/False")
    if set(detail["present_in_raw_rerun"].astype(str)) != {"True"}:
        fail("every detail row must be present in raw rerun")
    for col in ["present_in_timing_audit_60d", "present_in_semantic_audit", "present_in_formal_operation_events"]:
        if not source_gap[col].astype(str).eq("False").all():
            fail(f"inside-window source-gap rows must be absent from {col}")
    source_gap_stocks = set(source_gap["stock_id"].astype(str))
    if source_gap_stocks != {"8077"}:
        fail(f"inside-window source-gap rows should isolate 8077; got {sorted(source_gap_stocks)}")
    source_gap_dates = set(source_gap["signal_date"].astype(str))
    if source_gap_dates != {"20260529", "20260603"}:
        fail(f"inside-window source-gap dates changed; got {sorted(source_gap_dates)}")
    if set(source_gap["promotion_impact"].astype(str)) != {"promotion_blocked_pending_research_source_sync"}:
        fail("inside-window source-gap rows must block promotion pending research source sync")


def validate_summary(summary: pd.DataFrame, detail: pd.DataFrame) -> None:
    profile = require_single(summary, "source_profile", "raw_market_rerun", "source_counts")
    membership = require_single(summary, "membership_check", "raw_vs_timing_audit_60d", "raw_minus_timing_count")
    freshness = require_single(
        summary,
        "gap_classification",
        "raw_minus_timing",
        "freshness_extension_after_timing_window",
    )
    source_gap = require_single(
        summary,
        "gap_classification",
        "raw_minus_timing",
        "source_gap_inside_timing_window_promotion_blocker",
    )
    blocker = require_single(summary, "promotion_gate", "promotion_readiness", "source_gap_blocker")
    if int(profile["sample_size"]) != 808:
        fail("source profile sample_size must match raw rerun detail count 808")
    if "timing_60d_count=798" not in str(profile["value_a"]):
        fail("source profile must record timing_60d_count=798")
    if int(membership["sample_size"]) != len(detail):
        fail("membership sample_size must match detail row count")
    if membership["status"] != "source_gap_plus_freshness_extension":
        fail("membership status must record source gap plus freshness extension")
    if int(freshness["sample_size"]) != 8:
        fail("freshness summary count must be 8")
    if freshness["status"] != "requires_research_artifact_refresh_before_promotion":
        fail("freshness summary must require research artifact refresh before promotion")
    if int(source_gap["sample_size"]) != 2:
        fail("inside-window source-gap summary count must be 2")
    if source_gap["status"] != "promotion_blocked_pending_research_source_sync":
        fail("inside-window source-gap summary must block promotion pending source sync")
    if int(blocker["sample_size"]) != 2:
        fail("promotion gate blocker count must be 2")
    if blocker["status"] != "promotion_blocked_pending_research_source_sync":
        fail("promotion gate must remain blocked")
    if blocker["value_c"] != "production_registry_changed=False":
        fail("promotion gate must explicitly record production registry unchanged")


def validate_markdown() -> None:
    if not LATEST_MD.exists():
        fail(f"missing markdown output: {LATEST_MD}")
    text = LATEST_MD.read_text(encoding="utf-8", errors="replace")
    required = [
        "research-only source reconciliation artifact",
        "does not change `stock_model_contract_registry.csv`",
        "freshness extension",
        "source-gap blocker before promotion",
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
    validate_gap_detail(detail)
    validate_summary(summary, detail)
    validate_markdown()
    print(
        "volume range breakout v2 source-gap reconciliation validation passed "
        f"summary_rows={len(summary)} detail_rows={len(detail)}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
