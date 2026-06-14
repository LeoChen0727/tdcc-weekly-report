from __future__ import annotations

from pathlib import Path

import pandas as pd


LATEST_DIR = Path("output/latest")
RESEARCH_HISTORY_DIR = Path("output/history/research")

SUMMARY_CSV = LATEST_DIR / "volume_breakout_pattern_classification_latest.csv"
SUMMARY_MD = LATEST_DIR / "volume_breakout_pattern_classification_latest.md"
DIMENSION_CSV = LATEST_DIR / "volume_breakout_pattern_dimension_latest.csv"
DIMENSION_MD = LATEST_DIR / "volume_breakout_pattern_dimension_latest.md"
HISTORY_SUMMARY_CSV = RESEARCH_HISTORY_DIR / "volume_breakout_pattern_classification.csv"
HISTORY_EVENTS_CSV = RESEARCH_HISTORY_DIR / "volume_breakout_pattern_classification_events.csv"
HISTORY_DIMENSION_CSV = RESEARCH_HISTORY_DIR / "volume_breakout_pattern_dimension.csv"

REQUIRED_SUMMARY_COLUMNS = {
    "model_id",
    "classification_id",
    "classification_name_zh",
    "pattern_id",
    "event_count",
    "win_rate",
    "avg_return",
    "median_return",
    "confidence_status",
    "out_of_sample_pass",
    "approved_for_daily",
    "generated_at",
}

REQUIRED_EVENT_COLUMNS = {
    "model_id",
    "event_date",
    "stock_id",
    "classification_id",
    "classification_name_zh",
    "pattern_tags",
    "consolidation_type",
    "price_position_type",
    "attack_method",
    "candle_quality",
    "follow_through_type",
    "follow_through_tags",
    "risk_type",
    "volume_ratio",
    "limit_up_like",
    "touch_5ma_10d",
    "touch_10ma_10d",
    "break_signal_low_5d",
}

REQUIRED_DIMENSION_COLUMNS = {
    "model_id",
    "dimension_type",
    "dimension_id",
    "dimension_name_zh",
    "pattern_id",
    "event_count",
    "win_rate",
    "avg_return",
    "median_return",
    "confidence_status",
    "out_of_sample_pass",
    "approved_for_daily",
    "generated_at",
}

EXPECTED_DIMENSION_TYPES = {
    "consolidation_type",
    "price_position_type",
    "attack_method",
    "candle_quality",
    "follow_through_type",
    "risk_type",
}

EXPECTED_PRICE_POSITIONS = {
    "low_position",
    "middle_position",
    "high_position",
}

EXPECTED_FOLLOW_THROUGH_TAGS = {
    "pullback_5ma",
    "pullback_10ma",
    "next_day_continuation",
    "next_day_gap_fade",
    "break_signal_low",
}

FORBIDDEN_PRODUCTION_FIELDS = {
    "trade_decision",
    "action_rating",
    "entry_style",
    "position_sizing",
    "decision_score",
    "daily_candidate_decision",
}


def fail(message: str) -> None:
    print(f"ERROR: {message}")
    raise SystemExit(1)


def read_csv(path: Path) -> pd.DataFrame:
    try:
        return pd.read_csv(path, dtype=str, keep_default_na=False)
    except Exception as exc:
        fail(f"{path} is not readable CSV: {exc}")


def check_file(path: Path) -> None:
    if not path.exists():
        fail(f"missing required file: {path}")
    if path.suffix.lower() == ".md":
        lines = path.read_text(encoding="utf-8", errors="replace").splitlines()
        if len(lines) < 10:
            fail(f"{path} is suspiciously short")


def main() -> int:
    for path in [
        SUMMARY_CSV,
        SUMMARY_MD,
        DIMENSION_CSV,
        DIMENSION_MD,
        HISTORY_SUMMARY_CSV,
        HISTORY_EVENTS_CSV,
        HISTORY_DIMENSION_CSV,
    ]:
        check_file(path)

    summary = read_csv(SUMMARY_CSV)
    dimension = read_csv(DIMENSION_CSV)
    events = read_csv(HISTORY_EVENTS_CSV)
    if summary.empty:
        fail(f"{SUMMARY_CSV} has no rows")
    if dimension.empty:
        fail(f"{DIMENSION_CSV} has no rows")
    if events.empty:
        fail(f"{HISTORY_EVENTS_CSV} has no rows")

    missing_summary = sorted(REQUIRED_SUMMARY_COLUMNS - set(summary.columns))
    if missing_summary:
        fail(f"{SUMMARY_CSV} missing columns: {missing_summary}")
    missing_events = sorted(REQUIRED_EVENT_COLUMNS - set(events.columns))
    if missing_events:
        fail(f"{HISTORY_EVENTS_CSV} missing columns: {missing_events}")
    missing_dimension = sorted(REQUIRED_DIMENSION_COLUMNS - set(dimension.columns))
    if missing_dimension:
        fail(f"{DIMENSION_CSV} missing columns: {missing_dimension}")

    forbidden = sorted((set(summary.columns) | set(events.columns) | set(dimension.columns)) & FORBIDDEN_PRODUCTION_FIELDS)
    if forbidden:
        fail(f"pattern classification must not emit production decision fields: {forbidden}")

    if set(summary["model_id"].astype(str)) != {"volume_range_breakout"}:
        fail(f"unexpected model_id values: {sorted(set(summary['model_id'].astype(str)))}")
    if set(dimension["model_id"].astype(str)) != {"volume_range_breakout"}:
        fail(f"unexpected dimension model_id values: {sorted(set(dimension['model_id'].astype(str)))}")

    approved = set(summary["approved_for_daily"].astype(str).str.lower())
    if approved - {"false"}:
        fail("pattern classification must keep approved_for_daily=False")
    dimension_approved = set(dimension["approved_for_daily"].astype(str).str.lower())
    if dimension_approved - {"false"}:
        fail("pattern dimension summary must keep approved_for_daily=False")

    valid_confidence = {"low", "medium", "high"}
    bad_confidence = sorted(set(summary["confidence_status"].astype(str)) - valid_confidence)
    if bad_confidence:
        fail(f"unexpected confidence_status values: {bad_confidence}")
    bad_dimension_confidence = sorted(set(dimension["confidence_status"].astype(str)) - valid_confidence)
    if bad_dimension_confidence:
        fail(f"unexpected dimension confidence_status values: {bad_dimension_confidence}")

    dimension_types = set(dimension["dimension_type"].astype(str))
    missing_types = sorted(EXPECTED_DIMENSION_TYPES - dimension_types)
    if missing_types:
        fail(f"dimension summary missing dimension types: {missing_types}")

    event_price_positions = set(events["price_position_type"].astype(str))
    missing_positions = sorted(EXPECTED_PRICE_POSITIONS - event_price_positions)
    if missing_positions:
        fail(f"event classification missing price position buckets: {missing_positions}")

    follow_tags_text = "|".join(events["follow_through_tags"].astype(str).tolist())
    missing_follow_tags = sorted(tag for tag in EXPECTED_FOLLOW_THROUGH_TAGS if tag not in follow_tags_text)
    if missing_follow_tags:
        fail(f"event classification missing follow-through tag coverage: {missing_follow_tags}")

    event_count = pd.to_numeric(summary["event_count"], errors="coerce")
    if event_count.isna().any() or (event_count <= 0).any():
        fail("event_count must be positive for every classification summary row")
    dimension_event_count = pd.to_numeric(dimension["event_count"], errors="coerce")
    if dimension_event_count.isna().any() or (dimension_event_count <= 0).any():
        fail("dimension event_count must be positive for every row")

    print(
        "volume breakout pattern classification validation passed "
        f"summary_rows={len(summary)} dimension_rows={len(dimension)} event_rows={len(events)}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
