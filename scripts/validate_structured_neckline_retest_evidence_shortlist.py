from __future__ import annotations

from pathlib import Path

import pandas as pd

from build_structured_neckline_retest_evidence_shortlist import (
    CHART_ROOT,
    EVENT_FAMILY_ID,
    FOCUS_EXIT_RULE_IDS,
    FORBIDDEN_PRODUCTION_FIELDS,
    HISTORY_INDEX_CSV,
    LATEST_INDEX_CSV,
    LATEST_INDEX_MD,
    MANUAL_REVIEW_STATUS,
    OUTPUT_COLUMNS,
    PRODUCTION_READINESS,
    RESEARCH_ID,
    RESEARCH_VARIANT_ID,
    SOURCE_PARAMETER_SET_ID,
    SOURCE_RESEARCH_ID,
    SOURCE_SHORTLIST_CSV,
    TARGET_SEGMENT_ID,
    TARGET_STOP_RULE_ID,
    normalize_code,
    normalize_date,
)


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


def row_key(row: pd.Series) -> tuple[str, str, str, str, str]:
    return (
        str(row.get("exit_rule_id", "")),
        str(row.get("outcome_result", "")),
        normalize_code(row.get("stock_id", "")),
        normalize_date(row.get("signal_date", "")),
        normalize_date(row.get("retest_entry_date", "")),
    )


def expected_source_keys() -> set[tuple[str, str, str, str, str]]:
    source = read_csv(SOURCE_SHORTLIST_CSV)
    required = {"exit_rule_id", "outcome_result", "stock_id", "signal_date", "retest_entry_date"}
    missing = sorted(required - set(source.columns))
    if missing:
        fail(f"source shortlist missing columns: {missing}")
    return {row_key(row) for _, row in source.iterrows()}


def main() -> int:
    latest = read_csv(LATEST_INDEX_CSV)
    history = read_csv(HISTORY_INDEX_CSV)
    if latest.empty:
        fail("latest evidence shortlist must not be empty")
    if len(latest) != len(history):
        fail("latest/history row counts differ")
    if not LATEST_INDEX_MD.exists():
        fail(f"missing markdown evidence shortlist: {LATEST_INDEX_MD}")
    if not CHART_ROOT.exists():
        fail(f"missing evidence chart root: {CHART_ROOT}")

    missing = sorted(set(OUTPUT_COLUMNS) - set(latest.columns))
    if missing:
        fail(f"latest evidence shortlist missing columns: {missing}")
    missing_history = sorted(set(OUTPUT_COLUMNS) - set(history.columns))
    if missing_history:
        fail(f"history evidence shortlist missing columns: {missing_history}")
    forbidden = sorted((set(latest.columns) | set(history.columns)) & FORBIDDEN_PRODUCTION_FIELDS)
    if forbidden:
        fail(f"evidence shortlist must not emit production decision fields: {forbidden}")

    constants = {
        "research_id": RESEARCH_ID,
        "source_research_id": SOURCE_RESEARCH_ID,
        "source_parameter_set_id": SOURCE_PARAMETER_SET_ID,
        "research_variant_id": RESEARCH_VARIANT_ID,
        "advisory_status": RESEARCH_VARIANT_ID,
        "event_family_id": EVENT_FAMILY_ID,
        "segment_id": TARGET_SEGMENT_ID,
        "stop_rule_id": TARGET_STOP_RULE_ID,
        "manual_review_status": MANUAL_REVIEW_STATUS,
        "production_readiness": PRODUCTION_READINESS,
        "evidence_status": "reconstructed_from_signal_90d_window",
    }
    for column, expected in constants.items():
        values = set(latest[column].astype(str))
        if values != {expected}:
            fail(f"{column} must be {expected}; got {sorted(values)}")
    if set(latest["exit_rule_id"].astype(str)) != set(FOCUS_EXIT_RULE_IDS):
        fail("evidence shortlist must cover exactly the two 10% exit rules")
    if not false_only(latest["approved_for_daily"]):
        fail("approved_for_daily must remain false")

    actual_keys = {row_key(row) for _, row in latest.iterrows()}
    if len(actual_keys) != len(latest):
        fail("evidence shortlist contains duplicate event rows")
    if actual_keys != expected_source_keys():
        fail("evidence shortlist keys must match source shortlist keys exactly")

    numeric_checks = [
        "reference_price",
        "reconstructed_neckline_price",
        "neckline_anchor_high",
        "left_support_low",
        "right_support_low",
        "support_price",
        "support_gap_pct",
        "visual_pre_signal_sessions",
        "visual_pre_signal_return_pct",
        "visual_pre_signal_range_pct",
        "base_age_sessions",
        "support_pair_span_sessions",
        "neckline_anchor_age_sessions",
    ]
    for column in numeric_checks:
        values = pd.to_numeric(latest[column], errors="coerce")
        if values.isna().any():
            fail(f"{column} contains non-numeric values")
        if column == "support_gap_pct" and (values > 9.0001).any():
            fail("support_gap_pct exceeds structured-neckline rule")
        if column.endswith("_sessions") and (values < 0).any():
            fail(f"{column} must not contain negative values")
    reference = pd.to_numeric(latest["reference_price"], errors="coerce")
    reconstructed = pd.to_numeric(latest["reconstructed_neckline_price"], errors="coerce")
    if ((reference - reconstructed).abs() > 0.011).any():
        fail("reconstructed neckline price differs from source reference_price")

    date_columns = [
        "neckline_anchor_date",
        "left_support_date",
        "right_support_date",
        "detection_window_start",
        "detection_window_end",
        "visible_context_start",
        "visible_context_end",
    ]
    for column in date_columns:
        if latest[column].astype(str).str.len().ne(8).any():
            fail(f"{column} must contain YYYYMMDD dates")
    allowed_context = {"bearish", "sideways_or_consolidation", "bullish", "mixed", "unknown"}
    context_values = set(latest["visual_pre_signal_context"].astype(str))
    unknown_context = context_values - allowed_context
    if unknown_context:
        fail(f"visual_pre_signal_context contains unexpected values: {sorted(unknown_context)}")
    if context_values == {"unknown"}:
        fail("visual_pre_signal_context should not be entirely unknown")

    png_paths = list(CHART_ROOT.rglob("*.png"))
    if len(png_paths) != len(latest):
        fail(f"evidence chart png count mismatch: png={len(png_paths)} rows={len(latest)}")
    for row_number, row in latest.iterrows():
        chart_path = Path(str(row.get("evidence_chart_path", "")))
        if not chart_path.exists():
            fail(f"missing evidence chart at row {row_number}: {chart_path}")
        if chart_path.suffix.lower() != ".png":
            fail(f"evidence chart must be png at row {row_number}: {chart_path}")
        if chart_path.stat().st_size < 10_000:
            fail(f"evidence chart suspiciously small at row {row_number}: {chart_path}")

    md_text = LATEST_INDEX_MD.read_text(encoding="utf-8", errors="replace")
    required_text = [
        "90-session reference window",
        "left/right support lows",
        "high anchor",
        "visual_pre_signal_context",
        "production impact: `none`",
        "not_production_ready_research_only",
    ]
    for text in required_text:
        if text not in md_text:
            fail(f"markdown missing required text: {text}")

    print(
        "structured neckline retest evidence shortlist validation passed "
        f"rows={len(latest)} charts={len(png_paths)} chart_root={CHART_ROOT}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
