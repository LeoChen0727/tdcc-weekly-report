from __future__ import annotations

from pathlib import Path

import pandas as pd

from build_structured_neckline_retest_review_shortlist import (
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
    REASON_ORDER,
    RESEARCH_ID,
    RESEARCH_VARIANT_ID,
    SOURCE_INDEX_CSV,
    SOURCE_PARAMETER_SET_ID,
    SOURCE_RESEARCH_ID,
    TARGET_SEGMENT_ID,
    TARGET_STOP_RULE_ID,
    normalize_code,
    normalize_date,
)


MAX_SHORTLIST_ROWS = 80


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


def expected_source_keys() -> tuple[set[tuple[str, str, str, str, str]], set[tuple[str, str]]]:
    source = read_csv(SOURCE_INDEX_CSV)
    required = {
        "research_id",
        "parameter_set_id",
        "exit_rule_id",
        "outcome_result",
        "stock_id",
        "signal_date",
        "retest_entry_date",
    }
    missing = sorted(required - set(source.columns))
    if missing:
        fail(f"source review packet missing columns: {missing}")
    source = source[
        source["research_id"].astype(str).eq(SOURCE_RESEARCH_ID)
        & source["parameter_set_id"].astype(str).eq(SOURCE_PARAMETER_SET_ID)
        & source["exit_rule_id"].astype(str).isin(FOCUS_EXIT_RULE_IDS)
    ].copy()
    if source.empty:
        fail("source review packet has no rows for focus exit rules")
    keys = {row_key(row) for _, row in source.iterrows()}
    outcome_pairs = set(zip(source["exit_rule_id"].astype(str), source["outcome_result"].astype(str)))
    return keys, outcome_pairs


def validate_reasons(latest: pd.DataFrame) -> None:
    allowed = set(REASON_ORDER)
    seen: set[str] = set()
    for row_number, text in enumerate(latest["selection_reasons"].astype(str), start=2):
        reasons = [reason for reason in text.split(";") if reason]
        if not reasons:
            fail(f"row {row_number} has no selection reason")
        unknown = sorted(set(reasons) - allowed)
        if unknown:
            fail(f"row {row_number} has unknown selection reasons: {unknown}")
        seen.update(reasons)
    missing = sorted(allowed - seen)
    if missing:
        fail(f"shortlist does not contain every required reason class: {missing}")


def main() -> int:
    latest = read_csv(LATEST_INDEX_CSV)
    history = read_csv(HISTORY_INDEX_CSV)
    if latest.empty:
        fail("latest shortlist must not be empty")
    if len(latest) > MAX_SHORTLIST_ROWS:
        fail(f"shortlist has too many rows for manual review: {len(latest)} > {MAX_SHORTLIST_ROWS}")
    if len(latest) != len(history):
        fail("latest/history row counts differ")
    if not LATEST_INDEX_MD.exists():
        fail(f"missing markdown shortlist: {LATEST_INDEX_MD}")
    if not CHART_ROOT.exists():
        fail(f"missing shortlist chart root: {CHART_ROOT}")

    missing = sorted(set(OUTPUT_COLUMNS) - set(latest.columns))
    if missing:
        fail(f"latest shortlist missing columns: {missing}")
    missing_history = sorted(set(OUTPUT_COLUMNS) - set(history.columns))
    if missing_history:
        fail(f"history shortlist missing columns: {missing_history}")
    forbidden = sorted((set(latest.columns) | set(history.columns)) & FORBIDDEN_PRODUCTION_FIELDS)
    if forbidden:
        fail(f"shortlist must not emit production decision fields: {forbidden}")

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
    }
    for column, expected in constants.items():
        values = set(latest[column].astype(str))
        if values != {expected}:
            fail(f"{column} must be {expected}; got {sorted(values)}")
    if set(latest["exit_rule_id"].astype(str)) != set(FOCUS_EXIT_RULE_IDS):
        fail("shortlist must cover exactly the two 10% exit rules")
    if not false_only(latest["approved_for_daily"]):
        fail("approved_for_daily must remain false")

    source_keys, source_outcome_pairs = expected_source_keys()
    actual_keys = {row_key(row) for _, row in latest.iterrows()}
    if len(actual_keys) != len(latest):
        fail("shortlist contains duplicate event rows")
    if not actual_keys <= source_keys:
        fail("shortlist contains rows that are not in the source review packet")
    actual_outcome_pairs = set(zip(latest["exit_rule_id"].astype(str), latest["outcome_result"].astype(str)))
    if actual_outcome_pairs != source_outcome_pairs:
        fail(f"shortlist outcome coverage differs from source: actual={sorted(actual_outcome_pairs)} source={sorted(source_outcome_pairs)}")
    validate_reasons(latest)

    png_paths = list(CHART_ROOT.rglob("*.png"))
    if len(png_paths) != len(latest):
        fail(f"shortlist chart png count mismatch: png={len(png_paths)} rows={len(latest)}")
    for row_number, row in latest.iterrows():
        for column in ["source_chart_path", "shortlist_chart_path"]:
            chart_path = Path(str(row.get(column, "")))
            if not chart_path.exists():
                fail(f"missing chart at row {row_number}: {chart_path}")
            if chart_path.suffix.lower() != ".png":
                fail(f"chart must be png at row {row_number}: {chart_path}")
            if chart_path.stat().st_size < 10_000:
                fail(f"chart suspiciously small at row {row_number}: {chart_path}")

    md_text = LATEST_INDEX_MD.read_text(encoding="utf-8", errors="replace")
    required_text = [
        "production impact: `none`",
        "manual review set",
        "two 10% exit rules",
        "not_production_ready_research_only",
        "does not regenerate signal logic",
    ]
    for text in required_text:
        if text not in md_text:
            fail(f"markdown missing required text: {text}")

    print(
        "structured neckline retest review shortlist validation passed "
        f"rows={len(latest)} charts={len(png_paths)} chart_root={CHART_ROOT}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
