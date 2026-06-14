from __future__ import annotations

from pathlib import Path

import pandas as pd


LATEST_DIR = Path("output/latest")
RESEARCH_HISTORY_DIR = Path("output/history/research")

SUMMARY_CSV = LATEST_DIR / "volume_breakout_pattern_classification_latest.csv"
SUMMARY_MD = LATEST_DIR / "volume_breakout_pattern_classification_latest.md"
HISTORY_SUMMARY_CSV = RESEARCH_HISTORY_DIR / "volume_breakout_pattern_classification.csv"
HISTORY_EVENTS_CSV = RESEARCH_HISTORY_DIR / "volume_breakout_pattern_classification_events.csv"

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
    "volume_ratio",
    "limit_up_like",
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
    for path in [SUMMARY_CSV, SUMMARY_MD, HISTORY_SUMMARY_CSV, HISTORY_EVENTS_CSV]:
        check_file(path)

    summary = read_csv(SUMMARY_CSV)
    events = read_csv(HISTORY_EVENTS_CSV)
    if summary.empty:
        fail(f"{SUMMARY_CSV} has no rows")
    if events.empty:
        fail(f"{HISTORY_EVENTS_CSV} has no rows")

    missing_summary = sorted(REQUIRED_SUMMARY_COLUMNS - set(summary.columns))
    if missing_summary:
        fail(f"{SUMMARY_CSV} missing columns: {missing_summary}")
    missing_events = sorted(REQUIRED_EVENT_COLUMNS - set(events.columns))
    if missing_events:
        fail(f"{HISTORY_EVENTS_CSV} missing columns: {missing_events}")

    forbidden = sorted((set(summary.columns) | set(events.columns)) & FORBIDDEN_PRODUCTION_FIELDS)
    if forbidden:
        fail(f"pattern classification must not emit production decision fields: {forbidden}")

    if set(summary["model_id"].astype(str)) != {"volume_range_breakout"}:
        fail(f"unexpected model_id values: {sorted(set(summary['model_id'].astype(str)))}")

    approved = set(summary["approved_for_daily"].astype(str).str.lower())
    if approved - {"false"}:
        fail("pattern classification must keep approved_for_daily=False")

    valid_confidence = {"low", "medium", "high"}
    bad_confidence = sorted(set(summary["confidence_status"].astype(str)) - valid_confidence)
    if bad_confidence:
        fail(f"unexpected confidence_status values: {bad_confidence}")

    event_count = pd.to_numeric(summary["event_count"], errors="coerce")
    if event_count.isna().any() or (event_count <= 0).any():
        fail("event_count must be positive for every classification summary row")

    print(f"volume breakout pattern classification validation passed summary_rows={len(summary)} event_rows={len(events)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
