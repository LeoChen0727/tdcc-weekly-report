from __future__ import annotations

from pathlib import Path

import pandas as pd


ROOT = Path(".")
LATEST_DIR = ROOT / "output" / "latest"
RESEARCH_HISTORY_DIR = ROOT / "output" / "history" / "research"

LATEST_SUMMARY_CSV = LATEST_DIR / "volume_breakout_confirmed_operation_backtest_latest.csv"
LATEST_SUMMARY_MD = LATEST_DIR / "volume_breakout_confirmed_operation_backtest_latest.md"
HISTORY_SUMMARY_CSV = RESEARCH_HISTORY_DIR / "volume_breakout_confirmed_operation_backtest.csv"
HISTORY_EVENTS_CSV = RESEARCH_HISTORY_DIR / "volume_breakout_confirmed_operation_events.csv"
LATEST_RANK_CSV = LATEST_DIR / "volume_breakout_confirmed_operation_rank_latest.csv"
LATEST_RANK_MD = LATEST_DIR / "volume_breakout_confirmed_operation_rank_latest.md"
LATEST_PENDING_CSV = LATEST_DIR / "volume_breakout_pending_operation_queue_latest.csv"
LATEST_PENDING_MD = LATEST_DIR / "volume_breakout_pending_operation_queue_latest.md"

REQUIRED_SUMMARY_COLUMNS = {
    "model_id",
    "overlay_model_id",
    "research_id",
    "tdcc_list_type",
    "rank_bucket",
    "trigger_id",
    "confluence_scope",
    "confluence_id",
    "entry_rule_id",
    "stop_loss_rule_id",
    "exit_rule_id",
    "sample_size",
    "win_rate",
    "avg_return",
    "median_return",
    "out_of_sample_pass",
    "confidence_status",
    "approved_for_daily",
    "ranking_research_score",
    "ranking_research_rank",
}

REQUIRED_EVENT_COLUMNS = {
    "model_id",
    "overlay_model_id",
    "research_id",
    "signal_date",
    "confirmation_date",
    "confirmation_age_trading_days",
    "tdcc_signal_date",
    "tdcc_signal_age_days",
    "stock_id",
    "trigger_id",
    "entry_rule_id",
    "entry_date",
    "entry_price",
    "entry_price_source",
    "stop_loss_rule_id",
    "stop_loss_level",
    "exit_rule_id",
    "exit_date",
    "exit_price",
    "exit_reason",
    "return_pct",
    "out_of_sample",
    "classification_id",
    "attack_method",
    "price_position_type",
    "tdcc_list_type",
    "tdcc_rank",
    "tdcc_ranking_score",
    "approved_for_daily",
}

REQUIRED_RANK_COLUMNS = {
    "operation_rank",
    "model_id",
    "research_id",
    "latest_price_date",
    "signal_date",
    "confirmation_date",
    "stock_id",
    "trigger_id",
    "entry_rule_id",
    "entry_price_status",
    "stop_loss_rule_id",
    "exit_rule_id",
    "tdcc_list_type",
    "evidence_sample_size",
    "ranking_research_score",
    "approved_for_daily",
}

REQUIRED_PENDING_COLUMNS = {
    "queue_date",
    "model_id",
    "research_id",
    "signal_date",
    "signal_age_trading_days",
    "stock_id",
    "pending_trigger_ids",
    "expired",
    "broken_signal_low",
    "approved_for_daily",
}

EXPECTED_TRIGGERS = {
    "next_day_continuation_confirmed",
    "pullback_5ma_confirmed",
    "pullback_10ma_confirmed",
}

EXPECTED_SCOPES = {
    "operation_trigger",
    "operation_classification",
    "operation_attack_method",
    "operation_price_position",
    "operation_attack_position",
}

VALID_TDCC_LIST_TYPES = {"no_tdcc", "weekly_increase", "consecutive_accumulation"}

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


def check_file(path: Path, allow_short_md: bool = False) -> None:
    if not path.exists():
        fail(f"missing required file: {path}")
    if path.suffix.lower() == ".md":
        lines = path.read_text(encoding="utf-8", errors="replace").splitlines()
        if not allow_short_md and len(lines) < 10:
            fail(f"{path} is suspiciously short")


def false_only(series: pd.Series) -> bool:
    return set(series.astype(str).str.lower().unique()) <= {"false", "0", ""}


def date_series(series: pd.Series) -> pd.Series:
    return pd.to_datetime(series.astype(str), format="%Y%m%d", errors="coerce")


def main() -> int:
    for path in [
        LATEST_SUMMARY_CSV,
        LATEST_SUMMARY_MD,
        HISTORY_SUMMARY_CSV,
        HISTORY_EVENTS_CSV,
        LATEST_RANK_CSV,
        LATEST_RANK_MD,
        LATEST_PENDING_CSV,
        LATEST_PENDING_MD,
    ]:
        check_file(path, allow_short_md=path in {LATEST_RANK_MD, LATEST_PENDING_MD})

    summary = read_csv(LATEST_SUMMARY_CSV)
    history = read_csv(HISTORY_SUMMARY_CSV)
    events = read_csv(HISTORY_EVENTS_CSV)
    rank = read_csv(LATEST_RANK_CSV)
    pending = read_csv(LATEST_PENDING_CSV)
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
    missing_rank = sorted(REQUIRED_RANK_COLUMNS - set(rank.columns))
    if missing_rank:
        fail(f"{LATEST_RANK_CSV} missing columns: {missing_rank}")
    missing_pending = sorted(REQUIRED_PENDING_COLUMNS - set(pending.columns))
    if missing_pending:
        fail(f"{LATEST_PENDING_CSV} missing columns: {missing_pending}")

    forbidden = sorted(
        (set(summary.columns) | set(events.columns) | set(rank.columns) | set(pending.columns))
        & FORBIDDEN_PRODUCTION_FIELDS
    )
    if forbidden:
        fail(f"confirmed operation research must not emit production decision fields: {forbidden}")

    if set(summary["model_id"].astype(str)) != {"volume_range_breakout"}:
        fail("summary model_id must be volume_range_breakout")
    if set(events["model_id"].astype(str)) != {"volume_range_breakout"}:
        fail("event model_id must be volume_range_breakout")
    if set(summary["overlay_model_id"].astype(str)) != {"tdcc_weekly_ranking_formula"}:
        fail("summary overlay_model_id must be tdcc_weekly_ranking_formula")
    if set(events["overlay_model_id"].astype(str)) != {"tdcc_weekly_ranking_formula"}:
        fail("event overlay_model_id must be tdcc_weekly_ranking_formula")

    for label, df in [("summary", summary), ("events", events), ("rank", rank), ("pending", pending)]:
        if "approved_for_daily" in df.columns and not false_only(df["approved_for_daily"]):
            fail(f"{label} approved_for_daily must remain false")

    bad_summary_lists = sorted(set(summary["tdcc_list_type"].astype(str)) - VALID_TDCC_LIST_TYPES)
    if bad_summary_lists:
        fail(f"unexpected summary tdcc_list_type values: {bad_summary_lists}")
    bad_event_lists = sorted(set(events["tdcc_list_type"].astype(str)) - VALID_TDCC_LIST_TYPES)
    if bad_event_lists:
        fail(f"unexpected event tdcc_list_type values: {bad_event_lists}")

    missing_triggers = sorted(EXPECTED_TRIGGERS - set(summary["trigger_id"].astype(str)))
    if missing_triggers:
        fail(f"summary missing trigger rows: {missing_triggers}")
    bad_triggers = sorted(set(events["trigger_id"].astype(str)) - EXPECTED_TRIGGERS)
    if bad_triggers:
        fail(f"unexpected event trigger_id values: {bad_triggers}")
    missing_scopes = sorted(EXPECTED_SCOPES - set(summary["confluence_scope"].astype(str)))
    if missing_scopes:
        fail(f"summary missing confluence scopes: {missing_scopes}")

    if set(summary["entry_rule_id"].astype(str)) != {"confirmation_next_open"}:
        fail("summary entry_rule_id must be confirmation_next_open")
    if set(events["entry_rule_id"].astype(str)) != {"confirmation_next_open"}:
        fail("events entry_rule_id must be confirmation_next_open")
    if set(events["entry_price_source"].astype(str)) != {"confirmation_next_open"}:
        fail("events entry_price_source must be confirmation_next_open")

    signal_dates = date_series(events["signal_date"])
    confirmation_dates = date_series(events["confirmation_date"])
    entry_dates = date_series(events["entry_date"])
    exit_dates = date_series(events["exit_date"])
    if signal_dates.isna().any() or confirmation_dates.isna().any() or entry_dates.isna().any() or exit_dates.isna().any():
        fail("signal/confirmation/entry/exit dates must be valid YYYYMMDD")
    if (confirmation_dates <= signal_dates).any():
        fail("confirmation_date must be after signal_date")
    if (entry_dates <= confirmation_dates).any():
        fail("entry_date must be after confirmation_date")
    if (exit_dates < entry_dates).any():
        fail("exit_date must not be before entry_date")

    ages = pd.to_numeric(events["confirmation_age_trading_days"], errors="coerce")
    if ages.isna().any() or (ages < 1).any() or (ages > 10).any():
        fail("confirmation_age_trading_days must be between 1 and 10")

    tdcc_events = events[events["tdcc_list_type"].astype(str) != "no_tdcc"].copy()
    if not tdcc_events.empty:
        tdcc_dates = date_series(tdcc_events["tdcc_signal_date"])
        conf_dates = date_series(tdcc_events["confirmation_date"])
        if tdcc_dates.isna().any() or (tdcc_dates > conf_dates).any():
            fail("TDCC overlay contains future leak: tdcc_signal_date > confirmation_date")
        tdcc_ages = pd.to_numeric(tdcc_events["tdcc_signal_age_days"], errors="coerce")
        if tdcc_ages.isna().any() or (tdcc_ages < 0).any() or (tdcc_ages > 7).any():
            fail("tdcc_signal_age_days must be between 0 and 7")
        tdcc_ranks = pd.to_numeric(tdcc_events["tdcc_rank"], errors="coerce")
        if tdcc_ranks.isna().any() or (tdcc_ranks < 1).any():
            fail("tdcc_rank must be positive numeric when TDCC is attached")

    sample_size = pd.to_numeric(summary["sample_size"], errors="coerce")
    if sample_size.isna().any() or (sample_size <= 0).any():
        fail("summary sample_size must be positive")
    bad_confidence = sorted(set(summary["confidence_status"].astype(str)) - {"low", "medium", "high"})
    if bad_confidence:
        fail(f"unexpected confidence_status values: {bad_confidence}")

    if not rank.empty:
        if set(rank["entry_price_status"].astype(str)) != {"next_open_pending"}:
            fail("rank entry_price_status must be next_open_pending")
        if rank.duplicated(["confirmation_date", "stock_id", "trigger_id"]).any():
            fail("rank output must not duplicate stock/trigger confirmation rows")

    print(
        "volume breakout confirmed operation validation passed "
        f"summary_rows={len(summary)} event_rows={len(events)} "
        f"rank_rows={len(rank)} pending_rows={len(pending)}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
