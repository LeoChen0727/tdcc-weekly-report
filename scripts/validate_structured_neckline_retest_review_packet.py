from __future__ import annotations

from pathlib import Path

import pandas as pd

from build_structured_neckline_retest_review_packet import (
    CHART_ROOT,
    EVENT_FAMILY_ID,
    EXIT_RULE_IDS,
    FORBIDDEN_PRODUCTION_FIELDS,
    HISTORY_INDEX_CSV,
    LATEST_INDEX_CSV,
    LATEST_INDEX_MD,
    MANUAL_REVIEW_STATUS,
    OUTPUT_COLUMNS,
    PRODUCTION_READINESS,
    RESEARCH_ID,
    RESEARCH_VARIANT_ID,
    SOURCE_DETAIL_CSV,
    TARGET_SEGMENT_ID,
    TARGET_STOP_RULE_ID,
    normalize_code,
    normalize_date,
    read_source_detail,
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


def expected_keys() -> set[tuple[str, str, str, str]]:
    if not SOURCE_DETAIL_CSV.exists():
        fail(f"missing source detail: {SOURCE_DETAIL_CSV}")
    source = read_source_detail()
    keys: set[tuple[str, str, str, str]] = set()
    for _, row in source.iterrows():
        keys.add(
            (
                str(row.get("exit_rule_id")),
                normalize_code(row.get("stock_id")),
                normalize_date(row.get("signal_date")),
                normalize_date(row.get("retest_entry_date")),
            )
        )
    return keys


def main() -> int:
    latest = read_csv(LATEST_INDEX_CSV)
    history = read_csv(HISTORY_INDEX_CSV)
    if latest.empty:
        fail("latest review packet must not be empty")
    if len(latest) != len(history):
        fail("latest/history row counts differ")
    if not LATEST_INDEX_MD.exists():
        fail(f"missing markdown packet: {LATEST_INDEX_MD}")
    if not CHART_ROOT.exists():
        fail(f"missing chart root: {CHART_ROOT}")
    missing = sorted(set(OUTPUT_COLUMNS) - set(latest.columns))
    if missing:
        fail(f"latest packet missing columns: {missing}")
    missing_history = sorted(set(OUTPUT_COLUMNS) - set(history.columns))
    if missing_history:
        fail(f"history packet missing columns: {missing_history}")
    forbidden = sorted((set(latest.columns) | set(history.columns)) & FORBIDDEN_PRODUCTION_FIELDS)
    if forbidden:
        fail(f"packet must not emit production decision fields: {forbidden}")

    constants = {
        "research_id": RESEARCH_ID,
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
    if set(latest["exit_rule_id"].astype(str)) != set(EXIT_RULE_IDS):
        fail("packet must include all exit rules for the target signal_low_stop segment")
    if set(latest["market_regime"].astype(str)) - {"strong_bull", "mild_bull"}:
        fail("target segment should contain only bull market regimes")
    if not false_only(latest["approved_for_daily"]):
        fail("approved_for_daily must remain false")

    actual_keys = set(
        zip(
            latest["exit_rule_id"].astype(str),
            latest["stock_id"].map(normalize_code),
            latest["signal_date"].map(normalize_date),
            latest["retest_entry_date"].map(normalize_date),
        )
    )
    expected = expected_keys()
    if actual_keys != expected:
        fail(f"packet keys do not match source selection: actual={len(actual_keys)} expected={len(expected)}")

    png_paths = list(CHART_ROOT.rglob("*.png"))
    if len(png_paths) != len(latest):
        fail(f"chart png count mismatch: png={len(png_paths)} rows={len(latest)}")
    for row_number, row in latest.iterrows():
        chart_path = Path(str(row.get("chart_path", "")))
        if not chart_path.exists():
            fail(f"missing chart at row {row_number}: {chart_path}")
        if chart_path.suffix.lower() != ".png":
            fail(f"chart must be png at row {row_number}: {chart_path}")
        if chart_path.stat().st_size < 10_000:
            fail(f"chart suspiciously small at row {row_number}: {chart_path}")

    md_text = LATEST_INDEX_MD.read_text(encoding="utf-8", errors="replace")
    required_text = [
        "production impact: `none`",
        "outlier concentration check",
        "avg_return_ex_top5_positive_pct",
        "research-only evidence",
        PRODUCTION_READINESS,
    ]
    for text in required_text:
        if text not in md_text:
            fail(f"markdown missing required text: {text}")

    print(
        "structured neckline retest review packet validation passed "
        f"rows={len(latest)} charts={len(png_paths)} chart_root={CHART_ROOT}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
