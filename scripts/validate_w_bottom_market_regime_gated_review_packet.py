from __future__ import annotations

from pathlib import Path

import pandas as pd

from build_w_bottom_market_regime_gated_review_packet import (
    CHART_ROOT,
    EVENT_SET_ID,
    FORBIDDEN_PRODUCTION_FIELDS,
    HISTORY_INDEX_CSV,
    LATEST_INDEX_CSV,
    LATEST_INDEX_MD,
    MODEL_ID,
    OUTCOME_RULE_ID,
    OUTPUT_COLUMNS,
    PRODUCTION_READINESS,
    RESEARCH_ID,
    RESEARCH_VARIANT_ID,
    SOURCE_DETAIL_CSV,
    TARGET_SEGMENT_IDS,
    normalize_code,
    normalize_date,
    segment_map,
    source_detail,
)


REQUIRED_COLUMNS = set(OUTPUT_COLUMNS)


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


def expected_keys() -> set[tuple[str, str, str]]:
    if not SOURCE_DETAIL_CSV.exists():
        fail(f"missing source detail: {SOURCE_DETAIL_CSV}")
    detail = source_detail()
    segments = segment_map()
    keys: set[tuple[str, str, str]] = set()
    for segment_id in TARGET_SEGMENT_IDS:
        if segment_id not in segments:
            fail(f"target segment missing from segment specs: {segment_id}")
        _, selector = segments[segment_id]
        sample = detail[selector(detail)].copy()
        if sample.empty:
            fail(f"target segment produced no rows: {segment_id}")
        for _, row in sample.iterrows():
            keys.add(
                (
                    segment_id,
                    normalize_code(row.get("stock_id")),
                    normalize_date(row.get("source_signal_date")),
                )
            )
    return keys


def main() -> int:
    latest = read_csv(LATEST_INDEX_CSV)
    history = read_csv(HISTORY_INDEX_CSV)
    if not LATEST_INDEX_MD.exists():
        fail(f"missing markdown packet: {LATEST_INDEX_MD}")
    if not CHART_ROOT.exists():
        fail(f"missing chart root: {CHART_ROOT}")
    if latest.empty:
        fail(f"{LATEST_INDEX_CSV} has no rows")
    if len(latest) != len(history):
        fail("latest and history row counts differ")
    missing = sorted(REQUIRED_COLUMNS - set(latest.columns))
    if missing:
        fail(f"{LATEST_INDEX_CSV} missing columns: {missing}")
    missing_history = sorted(REQUIRED_COLUMNS - set(history.columns))
    if missing_history:
        fail(f"{HISTORY_INDEX_CSV} missing columns: {missing_history}")
    forbidden = sorted((set(latest.columns) | set(history.columns)) & FORBIDDEN_PRODUCTION_FIELDS)
    if forbidden:
        fail(f"review packet must not emit production decision fields: {forbidden}")

    constants = {
        "model_id": MODEL_ID,
        "research_id": RESEARCH_ID,
        "research_variant_id": RESEARCH_VARIANT_ID,
        "advisory_status": RESEARCH_VARIANT_ID,
        "event_set_id": EVENT_SET_ID,
        "outcome_rule_id": OUTCOME_RULE_ID,
        "manual_review_status": "pending_user_shape_review",
        "production_readiness": PRODUCTION_READINESS,
    }
    for column, expected in constants.items():
        values = set(latest[column].astype(str))
        if values != {expected}:
            fail(f"{column} must be {expected}; got {sorted(values)}")
    if not false_only(latest["approved_for_daily"]):
        fail("approved_for_daily must remain false")
    if sorted(latest["segment_id"].drop_duplicates().tolist()) != sorted(TARGET_SEGMENT_IDS):
        fail("review packet segment set does not match target segment set")
    if set(latest["signal_market_regime"].astype(str)) - {"strong_bull", "mild_bull"}:
        fail("market-regime gated packet should contain only strong_bull or mild_bull rows")

    actual_keys = set(
        zip(
            latest["segment_id"].astype(str),
            latest["stock_id"].map(normalize_code),
            latest["source_signal_date"].map(normalize_date),
        )
    )
    expected = expected_keys()
    if actual_keys != expected:
        fail(f"review packet keys do not match expected gated selection: actual={len(actual_keys)} expected={len(expected)}")

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
        PRODUCTION_READINESS,
        "Month grouping is only a sample-distribution check",
    ]
    for text in required_text:
        if text not in md_text:
            fail(f"markdown missing required boundary text: {text}")

    print(
        "W-bottom market-regime gated review packet validation passed "
        f"rows={len(latest)} charts={len(png_paths)} segments={len(TARGET_SEGMENT_IDS)}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
