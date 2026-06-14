from __future__ import annotations

from pathlib import Path

import pandas as pd


ROOT = Path(".")
LATEST_DIR = ROOT / "output" / "latest"
RESEARCH_HISTORY_DIR = ROOT / "output" / "history" / "research"

LATEST_SUMMARY_CSV = LATEST_DIR / "volume_breakout_tdcc_confluence_backtest_latest.csv"
LATEST_SUMMARY_MD = LATEST_DIR / "volume_breakout_tdcc_confluence_backtest_latest.md"
HISTORY_SUMMARY_CSV = RESEARCH_HISTORY_DIR / "volume_breakout_tdcc_confluence_backtest.csv"
HISTORY_EVENTS_CSV = RESEARCH_HISTORY_DIR / "volume_breakout_tdcc_confluence_events.csv"

REQUIRED_SUMMARY_COLUMNS = {
    "model_id",
    "overlay_model_id",
    "research_id",
    "tdcc_list_type",
    "rank_bucket",
    "confluence_scope",
    "confluence_id",
    "pattern_id",
    "sample_size",
    "unique_signal_events",
    "win_rate",
    "avg_return",
    "median_return",
    "confidence_status",
    "out_of_sample_pass",
    "approved_for_daily",
    "ranking_research_score",
    "ranking_research_rank",
    "generated_at",
}

REQUIRED_EVENT_COLUMNS = {
    "model_id",
    "overlay_model_id",
    "research_id",
    "event_date",
    "tdcc_signal_date",
    "tdcc_signal_age_days",
    "stock_id",
    "event_filter_id",
    "model_hit_status",
    "pattern_id",
    "return_pct",
    "out_of_sample",
    "classification_id",
    "attack_method",
    "price_position_type",
    "follow_through_type",
    "risk_type",
    "tdcc_list_type",
    "tdcc_rank",
    "tdcc_ranking_score",
    "approved_for_daily",
}

EXPECTED_CONFLUENCE_SCOPES = {
    "tdcc_rank_only",
    "tdcc_classification",
    "tdcc_attack_method",
    "tdcc_price_position",
    "tdcc_follow_through",
    "tdcc_risk_type",
    "tdcc_candle_quality",
    "tdcc_consolidation",
    "tdcc_attack_follow",
}

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


def false_only(series: pd.Series) -> bool:
    return set(series.astype(str).str.lower().unique()) <= {"false", "0", ""}


def main() -> int:
    for path in [LATEST_SUMMARY_CSV, LATEST_SUMMARY_MD, HISTORY_SUMMARY_CSV, HISTORY_EVENTS_CSV]:
        check_file(path)

    summary = read_csv(LATEST_SUMMARY_CSV)
    history = read_csv(HISTORY_SUMMARY_CSV)
    events = read_csv(HISTORY_EVENTS_CSV)
    if summary.empty:
        fail(f"{LATEST_SUMMARY_CSV} has no rows")
    if history.empty:
        fail(f"{HISTORY_SUMMARY_CSV} has no rows")
    if events.empty:
        fail(f"{HISTORY_EVENTS_CSV} has no rows")

    missing_summary = sorted(REQUIRED_SUMMARY_COLUMNS - set(summary.columns))
    if missing_summary:
        fail(f"{LATEST_SUMMARY_CSV} missing columns: {missing_summary}")
    missing_events = sorted(REQUIRED_EVENT_COLUMNS - set(events.columns))
    if missing_events:
        fail(f"{HISTORY_EVENTS_CSV} missing columns: {missing_events}")

    forbidden = sorted((set(summary.columns) | set(events.columns)) & FORBIDDEN_PRODUCTION_FIELDS)
    if forbidden:
        fail(f"TDCC confluence research must not emit production decision fields: {forbidden}")

    if set(summary["model_id"].astype(str)) != {"volume_range_breakout"}:
        fail("summary model_id must be volume_range_breakout")
    if set(events["model_id"].astype(str)) != {"volume_range_breakout"}:
        fail("events model_id must be volume_range_breakout")
    if set(summary["overlay_model_id"].astype(str)) != {"tdcc_weekly_ranking_formula"}:
        fail("summary overlay_model_id must be tdcc_weekly_ranking_formula")
    if set(events["overlay_model_id"].astype(str)) != {"tdcc_weekly_ranking_formula"}:
        fail("events overlay_model_id must be tdcc_weekly_ranking_formula")

    if not false_only(summary["approved_for_daily"]):
        fail("summary approved_for_daily must remain false")
    if not false_only(events["approved_for_daily"]):
        fail("events approved_for_daily must remain false")

    valid_lists = {"weekly_increase", "consecutive_accumulation"}
    bad_lists = sorted(set(summary["tdcc_list_type"].astype(str)) - valid_lists)
    if bad_lists:
        fail(f"unexpected summary tdcc_list_type values: {bad_lists}")
    bad_event_lists = sorted(set(events["tdcc_list_type"].astype(str)) - valid_lists)
    if bad_event_lists:
        fail(f"unexpected event tdcc_list_type values: {bad_event_lists}")

    missing_scopes = sorted(EXPECTED_CONFLUENCE_SCOPES - set(summary["confluence_scope"].astype(str)))
    if missing_scopes:
        fail(f"summary missing confluence scopes: {missing_scopes}")

    signal_dates = pd.to_datetime(events["tdcc_signal_date"], format="%Y%m%d", errors="coerce")
    event_dates = pd.to_datetime(events["event_date"], format="%Y%m%d", errors="coerce")
    if signal_dates.isna().any() or event_dates.isna().any():
        fail("event_date and tdcc_signal_date must be valid YYYYMMDD dates")
    if (signal_dates > event_dates).any():
        fail("TDCC confluence contains future leak: tdcc_signal_date > event_date")

    ages = pd.to_numeric(events["tdcc_signal_age_days"], errors="coerce")
    if ages.isna().any() or (ages < 0).any() or (ages > 7).any():
        fail("tdcc_signal_age_days must be between 0 and 7")

    ranks = pd.to_numeric(events["tdcc_rank"], errors="coerce")
    if ranks.isna().any() or (ranks < 1).any() or (ranks > 50).any():
        fail("tdcc_rank must be numeric between 1 and 50")

    sample_size = pd.to_numeric(summary["sample_size"], errors="coerce")
    if sample_size.isna().any() or (sample_size <= 0).any():
        fail("summary sample_size must be positive")
    valid_confidence = {"low", "medium", "high"}
    bad_confidence = sorted(set(summary["confidence_status"].astype(str)) - valid_confidence)
    if bad_confidence:
        fail(f"unexpected confidence_status values: {bad_confidence}")

    print(
        "volume breakout TDCC confluence validation passed "
        f"summary_rows={len(summary)} event_rows={len(events)}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
