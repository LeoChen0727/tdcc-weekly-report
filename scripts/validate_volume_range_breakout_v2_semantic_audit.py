from __future__ import annotations

from pathlib import Path

import pandas as pd

from build_volume_range_breakout_v2_semantic_audit import (
    ADVISORY_STATUS,
    ARTIFACT_VERSION,
    DETAIL_COLUMNS,
    HISTORY_DETAIL_CSV,
    HISTORY_SUMMARY_CSV,
    LATEST_DETAIL_CSV,
    LATEST_MD,
    LATEST_OPERATION_SECTION_CSV,
    LATEST_SUMMARY_CSV,
    MODEL_ID,
    PRODUCTION_READINESS,
    RESEARCH_ID,
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


def numeric(series: pd.Series) -> pd.Series:
    return pd.to_numeric(series, errors="coerce")


def require_single(summary: pd.DataFrame, row_type: str, audit_scope: str, audit_key: str) -> pd.Series:
    rows = summary[
        summary["row_type"].astype(str).eq(row_type)
        & summary["audit_scope"].astype(str).eq(audit_scope)
        & summary["audit_key"].astype(str).eq(audit_key)
    ]
    if len(rows) != 1:
        fail(f"expected exactly one summary row for {row_type}/{audit_scope}/{audit_key}; got {len(rows)}")
    return rows.iloc[0]


def validate_common(summary: pd.DataFrame, detail: pd.DataFrame) -> None:
    if summary.empty:
        fail("summary output must not be empty")
    if detail.empty:
        fail("detail output must not be empty")
    missing_summary = sorted(set(SUMMARY_COLUMNS) - set(summary.columns))
    missing_detail = sorted(set(DETAIL_COLUMNS) - set(detail.columns))
    if missing_summary:
        fail(f"summary missing columns: {missing_summary}")
    if missing_detail:
        fail(f"detail missing columns: {missing_detail}")
    forbidden = sorted((set(summary.columns) | set(detail.columns)) & FORBIDDEN_PRODUCTION_FIELDS)
    if forbidden:
        fail(f"audit outputs must not contain production decision fields: {forbidden}")
    for name, df in [("summary", summary), ("detail", detail)]:
        if set(df["research_id"].astype(str)) != {RESEARCH_ID}:
            fail(f"{name} research_id must be {RESEARCH_ID}")
        if set(df["artifact_version"].astype(str)) != {ARTIFACT_VERSION}:
            fail(f"{name} artifact_version must be {ARTIFACT_VERSION}")
        if set(df["advisory_status"].astype(str)) != {ADVISORY_STATUS}:
            fail(f"{name} advisory_status must be {ADVISORY_STATUS}")
        if set(df["model_id"].astype(str)) != {MODEL_ID}:
            fail(f"{name} model_id must be {MODEL_ID}")
        if set(df["production_readiness"].astype(str)) != {PRODUCTION_READINESS}:
            fail(f"{name} production_readiness must be {PRODUCTION_READINESS}")
        if not false_only(df["approved_for_daily"]):
            fail(f"{name} approved_for_daily must remain false")
    if detail["source_event_key"].duplicated().any():
        dupes = detail[detail["source_event_key"].duplicated()]["source_event_key"].head(5).tolist()
        fail(f"detail contains duplicate deduped event keys: {dupes}")


def validate_dataset_profile(summary: pd.DataFrame, detail: pd.DataFrame) -> None:
    profile = require_single(summary, "dataset_profile", "dedupe", "raw_vs_dedup")
    all_row = require_single(summary, "dataset_profile", "overall", "all_dedup_mature_formal_operations")
    sample_size = int(all_row["sample_size"])
    if sample_size != len(detail):
        fail(f"overall sample_size {sample_size} does not match detail rows {len(detail)}")
    if sample_size < 3000:
        fail(f"deduped mature sample too small for semantic audit: {sample_size}")
    if "duplicate_extra_rows=" not in str(profile["value_c"]):
        fail("dedupe profile must record duplicate_extra_rows")


def validate_high_windows(summary: pd.DataFrame, detail: pd.DataFrame) -> None:
    rows = summary[summary["row_type"].astype(str).eq("high_window_threshold_metrics")]
    expected = {"previous_20d_high", "previous_40d_high", "previous_60d_high"}
    got = set(rows["audit_key"].astype(str))
    missing = sorted(expected - got)
    if missing:
        fail(f"missing high-window rows: {missing}")
    counts = {
        key: int(rows[rows["audit_key"].astype(str).eq(key)].iloc[0]["sample_size"])
        for key in expected
    }
    if not (counts["previous_20d_high"] >= counts["previous_40d_high"] >= counts["previous_60d_high"]):
        fail(f"high-window sample counts must be monotonic 20>=40>=60; got {counts}")
    if counts["previous_60d_high"] <= 0:
        fail("60-day previous-high subset must not be empty")
    for flag in ["high_breakout_20d_met", "high_breakout_40d_met", "high_breakout_60d_met"]:
        if flag not in detail.columns:
            fail(f"detail missing flag {flag}")
        if not set(detail[flag].astype(str).unique()) <= {"True", "False"}:
            fail(f"{flag} must contain only True/False")


def validate_anomaly_and_features(summary: pd.DataFrame, detail: pd.DataFrame) -> None:
    require_single(summary, "anomaly_check", "trim_return_tail", "trim_1pct_each_tail")
    if not detail["anomaly_flag"].astype(str).isin({"none", "bottom_1pct_return", "top_1pct_return"}).all():
        fail("detail anomaly_flag contains unexpected values")
    if not detail["anomaly_flag"].astype(str).ne("none").any():
        fail("detail must mark top/bottom 1pct anomaly candidates")
    required_feature_scopes = {
        "price_position_type",
        "consolidation_type",
        "classification_id",
        "risk_type",
        "limit_up_like",
    }
    feature_rows = summary[summary["row_type"].astype(str).eq("high_low_feature_share")]
    missing = sorted(required_feature_scopes - set(feature_rows["audit_scope"].astype(str)))
    if missing:
        fail(f"missing high/low feature-share scopes: {missing}")
    for scope in ["low_position_60_pct", "off_60d_low_pct", "range_width_20_pct", "range_width_40_pct", "range_width_60_pct"]:
        rows = summary[
            summary["row_type"].astype(str).eq("high_low_numeric_median")
            & summary["audit_scope"].astype(str).eq(scope)
        ]
        if rows.empty:
            fail(f"missing numeric high/low median scope: {scope}")


def validate_semantic_slices(summary: pd.DataFrame) -> None:
    subset_rows = summary[summary["row_type"].astype(str).eq("semantic_subset_metrics")]
    required = {
        "all_dedup",
        "low_position_60_le_80_and_consolidated",
        "high_position_60_gt_80_non_consolidation",
        "locked_limit_up",
        "not_locked_limit_up",
    }
    missing = sorted(required - set(subset_rows["audit_key"].astype(str)))
    if missing:
        fail(f"missing semantic subset rows: {missing}")


def validate_4989_guard(summary: pd.DataFrame) -> None:
    row = require_single(
        summary,
        "evidence_matching_guard",
        "4989_20260703",
        "legacy_locked_limit_up_mismatch",
    )
    value_a = str(row["value_a"])
    value_b = str(row["value_b"])
    value_c = str(row["value_c"])
    if row["status"] != "guard_required":
        fail("4989 guard status must be guard_required")
    if "source_locked_limit_up_met=False" not in value_a:
        fail("4989 guard must record that source locked-limit-up condition is false")
    if "legacy_evidence_confluence_id=locked_limit_up_breakout" not in value_b:
        fail("4989 guard must record legacy locked_limit_up_breakout evidence mismatch")
    if "current_included_in_confirmed_or_active=False" not in value_c:
        fail("4989 must not be included in current confirmed/active operation adapter rows")
    if LATEST_OPERATION_SECTION_CSV.exists():
        current = read_csv(LATEST_OPERATION_SECTION_CSV)
        leaked = current[
            current.get("stock_id", pd.Series(dtype=str)).astype(str).eq("4989")
            & current.get("row_type", pd.Series(dtype=str)).astype(str).eq("data")
            & current.get("pdf_section", pd.Series(dtype=str)).astype(str).isin(["confirmed_operation", "active_operation"])
        ]
        if not leaked.empty:
            fail("4989 leaked into current confirmed/active operation adapter rows")


def validate_markdown() -> None:
    if not LATEST_MD.exists():
        fail(f"missing markdown output: {LATEST_MD}")
    text = LATEST_MD.read_text(encoding="utf-8", errors="replace")
    required = [
        "not a production recommendation",
        "20-day breakout against stricter 40-day and 60-day previous-high gates",
        "4989 20260703 legacy locked-limit-up mismatch",
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
    if len(summary) != len(history_summary):
        fail("latest/history summary row counts differ")
    if len(detail) != len(history_detail):
        fail("latest/history detail row counts differ")
    validate_common(summary, detail)
    validate_dataset_profile(summary, detail)
    validate_high_windows(summary, detail)
    validate_anomaly_and_features(summary, detail)
    validate_semantic_slices(summary)
    validate_4989_guard(summary)
    validate_markdown()
    print(
        "volume range breakout v2 semantic audit validation passed "
        f"summary_rows={len(summary)} detail_rows={len(detail)}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
