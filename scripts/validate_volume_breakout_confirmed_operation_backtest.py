from __future__ import annotations

from pathlib import Path

import pandas as pd


ROOT = Path(".")
LATEST_DIR = ROOT / "output" / "latest"
RESEARCH_LATEST_DIR = LATEST_DIR / "research_backtest"
RESEARCH_HISTORY_DIR = ROOT / "output" / "history" / "research"

LATEST_SUMMARY_CSV = RESEARCH_LATEST_DIR / "volume_breakout_confirmed_operation_backtest_latest.csv"
LATEST_SUMMARY_MD = RESEARCH_LATEST_DIR / "volume_breakout_confirmed_operation_backtest_latest.md"
HISTORY_SUMMARY_CSV = RESEARCH_HISTORY_DIR / "volume_breakout_confirmed_operation_backtest.csv"
HISTORY_EVENTS_CSV = RESEARCH_HISTORY_DIR / "volume_breakout_confirmed_operation_events.csv"
LATEST_FORMAL_SUMMARY_CSV = LATEST_DIR / "volume_breakout_formal_operation_backtest_latest.csv"
LATEST_FORMAL_SUMMARY_MD = LATEST_DIR / "volume_breakout_formal_operation_backtest_latest.md"
HISTORY_FORMAL_EVENTS_CSV = RESEARCH_HISTORY_DIR / "volume_breakout_formal_operation_events.csv"
LATEST_FORMAL_LIFECYCLE_CSV = LATEST_DIR / "volume_breakout_formal_operation_lifecycle_latest.csv"
HISTORY_FORMAL_LIFECYCLE_CSV = RESEARCH_HISTORY_DIR / "volume_breakout_formal_operation_lifecycle_events.csv"
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
    "metric_sample_scope",
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
    "matched_trigger_ids",
    "selected_trigger_id",
    "selected_confirmation_date",
    "selected_trigger_priority",
    "selected_for_formal_operation",
    "operation_selection_status",
    "operation_lifecycle_definition_id",
    "operation_lifecycle_state",
    "sample_maturity_status",
    "mature_sample_eligible",
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

REQUIRED_LIFECYCLE_COLUMNS = {
    "model_id",
    "overlay_model_id",
    "research_id",
    "operation_lifecycle_definition_id",
    "latest_price_date",
    "signal_date",
    "stock_id",
    "operation_lifecycle_state",
    "sample_maturity_status",
    "mature_sample_eligible",
    "matched_trigger_ids",
    "selected_trigger_id",
    "selected_confirmation_date",
    "selected_trigger_priority",
    "confirmation_date",
    "confirmation_age_trading_days",
    "entry_date",
    "planned_exit_date",
    "exit_date",
    "exit_reason",
    "terminal_reason",
    "stop_loss_rule_id",
    "stop_loss_level",
    "exit_rule_id",
    "return_pct",
    "classification_id",
    "attack_method",
    "price_position_type",
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
    "matched_trigger_ids",
    "selected_trigger_id",
    "selected_confirmation_date",
    "selected_trigger_priority",
    "operation_selection_status",
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
    "pullback_5ma_confirmed",
    "next_day_break_signal_high_confirmed",
    "next_day_continuation_confirmed",
    "pullback_10ma_confirmed",
}

EXPECTED_SCOPES = {
    "operation_trigger",
    "operation_classification",
    "operation_attack_method",
    "operation_price_position",
    "operation_attack_position",
}

EXPECTED_LIFECYCLE_STATES = {
    "pending_confirmation",
    "confirmed_operation",
    "active_operation",
    "expired",
}

LIFECYCLE_DEFINITION_ID = "daily_volume_breakout_operation_lifecycle_v1"
METRIC_SAMPLE_SCOPE = "mature_selected_operation_only"

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
        LATEST_FORMAL_SUMMARY_CSV,
        LATEST_FORMAL_SUMMARY_MD,
        HISTORY_SUMMARY_CSV,
        HISTORY_EVENTS_CSV,
        HISTORY_FORMAL_EVENTS_CSV,
        LATEST_FORMAL_LIFECYCLE_CSV,
        HISTORY_FORMAL_LIFECYCLE_CSV,
        LATEST_RANK_CSV,
        LATEST_RANK_MD,
        LATEST_PENDING_CSV,
        LATEST_PENDING_MD,
    ]:
        check_file(path, allow_short_md=path in {LATEST_RANK_MD, LATEST_PENDING_MD})

    summary = read_csv(LATEST_SUMMARY_CSV)
    history = read_csv(HISTORY_SUMMARY_CSV)
    events = read_csv(HISTORY_EVENTS_CSV)
    formal_summary = read_csv(LATEST_FORMAL_SUMMARY_CSV)
    formal_events = read_csv(HISTORY_FORMAL_EVENTS_CSV)
    formal_lifecycle = read_csv(LATEST_FORMAL_LIFECYCLE_CSV)
    lifecycle_history = read_csv(HISTORY_FORMAL_LIFECYCLE_CSV)
    rank = read_csv(LATEST_RANK_CSV)
    pending = read_csv(LATEST_PENDING_CSV)
    if summary.empty:
        fail(f"{LATEST_SUMMARY_CSV} has no rows")
    if history.empty:
        fail(f"{HISTORY_SUMMARY_CSV} has no rows")
    if events.empty:
        fail(f"{HISTORY_EVENTS_CSV} has no rows")
    if formal_summary.empty:
        fail(f"{LATEST_FORMAL_SUMMARY_CSV} has no rows")
    if formal_events.empty:
        fail(f"{HISTORY_FORMAL_EVENTS_CSV} has no rows")
    if formal_lifecycle.empty:
        fail(f"{LATEST_FORMAL_LIFECYCLE_CSV} has no rows")
    if lifecycle_history.empty:
        fail(f"{HISTORY_FORMAL_LIFECYCLE_CSV} has no rows")

    missing_summary = sorted(REQUIRED_SUMMARY_COLUMNS - set(summary.columns))
    if missing_summary:
        fail(f"{LATEST_SUMMARY_CSV} missing columns: {missing_summary}")
    missing_events = sorted(REQUIRED_EVENT_COLUMNS - set(events.columns))
    if missing_events:
        fail(f"{HISTORY_EVENTS_CSV} missing columns: {missing_events}")
    missing_formal_summary = sorted(REQUIRED_SUMMARY_COLUMNS - set(formal_summary.columns))
    if missing_formal_summary:
        fail(f"{LATEST_FORMAL_SUMMARY_CSV} missing columns: {missing_formal_summary}")
    missing_formal_events = sorted(REQUIRED_EVENT_COLUMNS - set(formal_events.columns))
    if missing_formal_events:
        fail(f"{HISTORY_FORMAL_EVENTS_CSV} missing columns: {missing_formal_events}")
    missing_lifecycle = sorted(REQUIRED_LIFECYCLE_COLUMNS - set(formal_lifecycle.columns))
    if missing_lifecycle:
        fail(f"{LATEST_FORMAL_LIFECYCLE_CSV} missing columns: {missing_lifecycle}")
    missing_lifecycle_history = sorted(REQUIRED_LIFECYCLE_COLUMNS - set(lifecycle_history.columns))
    if missing_lifecycle_history:
        fail(f"{HISTORY_FORMAL_LIFECYCLE_CSV} missing columns: {missing_lifecycle_history}")
    missing_rank = sorted(REQUIRED_RANK_COLUMNS - set(rank.columns))
    if missing_rank:
        fail(f"{LATEST_RANK_CSV} missing columns: {missing_rank}")
    missing_pending = sorted(REQUIRED_PENDING_COLUMNS - set(pending.columns))
    if missing_pending:
        fail(f"{LATEST_PENDING_CSV} missing columns: {missing_pending}")

    forbidden = sorted(
        (
            set(summary.columns)
            | set(events.columns)
            | set(formal_summary.columns)
            | set(formal_events.columns)
            | set(formal_lifecycle.columns)
            | set(rank.columns)
            | set(pending.columns)
        )
        & FORBIDDEN_PRODUCTION_FIELDS
    )
    if forbidden:
        fail(f"confirmed operation research must not emit production decision fields: {forbidden}")

    if set(summary["model_id"].astype(str)) != {"volume_range_breakout"}:
        fail("summary model_id must be volume_range_breakout")
    if set(events["model_id"].astype(str)) != {"volume_range_breakout"}:
        fail("event model_id must be volume_range_breakout")
    if set(formal_summary["model_id"].astype(str)) != {"volume_range_breakout"}:
        fail("formal summary model_id must be volume_range_breakout")
    if set(formal_events["model_id"].astype(str)) != {"volume_range_breakout"}:
        fail("formal event model_id must be volume_range_breakout")
    if set(formal_lifecycle["model_id"].astype(str)) != {"volume_range_breakout"}:
        fail("formal lifecycle model_id must be volume_range_breakout")
    if set(summary["overlay_model_id"].astype(str)) != {"tdcc_weekly_ranking_formula"}:
        fail("summary overlay_model_id must be tdcc_weekly_ranking_formula")
    if set(events["overlay_model_id"].astype(str)) != {"tdcc_weekly_ranking_formula"}:
        fail("event overlay_model_id must be tdcc_weekly_ranking_formula")
    if set(formal_summary["overlay_model_id"].astype(str)) != {"tdcc_weekly_ranking_formula"}:
        fail("formal summary overlay_model_id must be tdcc_weekly_ranking_formula")
    if set(formal_events["overlay_model_id"].astype(str)) != {"tdcc_weekly_ranking_formula"}:
        fail("formal event overlay_model_id must be tdcc_weekly_ranking_formula")
    if set(formal_lifecycle["overlay_model_id"].astype(str)) != {"tdcc_weekly_ranking_formula"}:
        fail("formal lifecycle overlay_model_id must be tdcc_weekly_ranking_formula")

    for label, df in [
        ("summary", summary),
        ("events", events),
        ("formal_summary", formal_summary),
        ("formal_events", formal_events),
        ("formal_lifecycle", formal_lifecycle),
        ("rank", rank),
        ("pending", pending),
    ]:
        if "approved_for_daily" in df.columns and not false_only(df["approved_for_daily"]):
            fail(f"{label} approved_for_daily must remain false")

    bad_summary_lists = sorted(set(summary["tdcc_list_type"].astype(str)) - VALID_TDCC_LIST_TYPES)
    if bad_summary_lists:
        fail(f"unexpected summary tdcc_list_type values: {bad_summary_lists}")
    bad_event_lists = sorted(set(events["tdcc_list_type"].astype(str)) - VALID_TDCC_LIST_TYPES)
    if bad_event_lists:
        fail(f"unexpected event tdcc_list_type values: {bad_event_lists}")
    bad_formal_lists = sorted(set(formal_events["tdcc_list_type"].astype(str)) - VALID_TDCC_LIST_TYPES)
    if bad_formal_lists:
        fail(f"unexpected formal event tdcc_list_type values: {bad_formal_lists}")

    missing_triggers = sorted(EXPECTED_TRIGGERS - set(summary["trigger_id"].astype(str)))
    if missing_triggers:
        fail(f"summary missing trigger rows: {missing_triggers}")
    bad_triggers = sorted(set(events["trigger_id"].astype(str)) - EXPECTED_TRIGGERS)
    if bad_triggers:
        fail(f"unexpected event trigger_id values: {bad_triggers}")
    bad_formal_triggers = sorted(set(formal_events["trigger_id"].astype(str)) - EXPECTED_TRIGGERS)
    if bad_formal_triggers:
        fail(f"unexpected formal event trigger_id values: {bad_formal_triggers}")
    missing_scopes = sorted(EXPECTED_SCOPES - set(summary["confluence_scope"].astype(str)))
    if missing_scopes:
        fail(f"summary missing confluence scopes: {missing_scopes}")

    if set(summary["entry_rule_id"].astype(str)) != {"confirmation_next_open"}:
        fail("summary entry_rule_id must be confirmation_next_open")
    if set(events["entry_rule_id"].astype(str)) != {"confirmation_next_open"}:
        fail("events entry_rule_id must be confirmation_next_open")
    if set(formal_events["entry_rule_id"].astype(str)) != {"confirmation_next_open"}:
        fail("formal events entry_rule_id must be confirmation_next_open")
    if set(events["entry_price_source"].astype(str)) != {"confirmation_next_open"}:
        fail("events entry_price_source must be confirmation_next_open")
    if set(formal_events["entry_price_source"].astype(str)) != {"confirmation_next_open"}:
        fail("formal events entry_price_source must be confirmation_next_open")

    if set(formal_summary["metric_sample_scope"].astype(str)) != {METRIC_SAMPLE_SCOPE}:
        fail(f"formal summary metric_sample_scope must be {METRIC_SAMPLE_SCOPE}")
    if set(formal_events["selected_for_formal_operation"].astype(str)) != {"True"}:
        fail("formal operation events must contain only selected_for_formal_operation=True rows")
    if set(formal_events["operation_lifecycle_definition_id"].astype(str)) != {LIFECYCLE_DEFINITION_ID}:
        fail(f"formal events must use lifecycle definition {LIFECYCLE_DEFINITION_ID}")
    if set(formal_events["sample_maturity_status"].astype(str)) != {"mature"}:
        fail("formal operation events must contain only mature samples")
    if set(formal_events["mature_sample_eligible"].astype(str).str.lower()) != {"true"}:
        fail("formal operation events must be mature_sample_eligible=True")
    bad_formal_lifecycle_states = sorted(set(formal_events["operation_lifecycle_state"].astype(str)) - EXPECTED_LIFECYCLE_STATES)
    if bad_formal_lifecycle_states:
        fail(f"formal operation events have unexpected lifecycle states: {bad_formal_lifecycle_states}")
    formal_group = formal_events.groupby(["signal_date", "stock_id"], dropna=False)
    multi_trigger = formal_group["trigger_id"].nunique()
    if (multi_trigger > 1).any():
        bad = multi_trigger[multi_trigger > 1].head(20).to_dict()
        fail(f"formal operation events must use one selected trigger per signal: {bad}")
    multi_confirmation = formal_group["confirmation_date"].nunique()
    if (multi_confirmation > 1).any():
        bad = multi_confirmation[multi_confirmation > 1].head(20).to_dict()
        fail(f"formal operation events must use one selected confirmation date per signal: {bad}")

    for (signal_date, stock_id), part in events.groupby(["signal_date", "stock_id"], dropna=False):
        unique = part.drop_duplicates(["confirmation_date", "trigger_id"]).copy()
        unique["_confirmation_dt"] = date_series(unique["confirmation_date"])
        unique["_trigger_priority"] = unique["trigger_id"].astype(str).map(
            {
                "pullback_5ma_confirmed": 1,
                "next_day_break_signal_high_confirmed": 2,
                "next_day_continuation_confirmed": 3,
                "pullback_10ma_confirmed": 4,
            }
        ).fillna(999)
        expected = unique.sort_values(["_confirmation_dt", "_trigger_priority", "trigger_id"]).iloc[0]
        selected_ids = set(part["selected_trigger_id"].astype(str))
        if selected_ids != {str(expected["trigger_id"])}:
            fail(
                "selected_trigger_id must use earliest confirmation date then trigger priority "
                f"for signal={signal_date} stock={stock_id}"
            )
        selected_dates = set(part["selected_confirmation_date"].astype(str))
        if selected_dates != {str(expected["confirmation_date"])}:
            fail(
                "selected_confirmation_date must use earliest confirmation date "
                f"for signal={signal_date} stock={stock_id}"
            )

    lifecycle_states = set(formal_lifecycle["operation_lifecycle_state"].astype(str))
    bad_lifecycle_states = sorted(lifecycle_states - EXPECTED_LIFECYCLE_STATES)
    if bad_lifecycle_states:
        fail(f"unexpected formal lifecycle states: {bad_lifecycle_states}")
    missing_lifecycle_states = sorted(EXPECTED_LIFECYCLE_STATES - lifecycle_states)
    if missing_lifecycle_states:
        fail(f"formal lifecycle artifact must separate all states; missing: {missing_lifecycle_states}")
    if set(formal_lifecycle["operation_lifecycle_definition_id"].astype(str)) != {LIFECYCLE_DEFINITION_ID}:
        fail(f"formal lifecycle must use lifecycle definition {LIFECYCLE_DEFINITION_ID}")
    if formal_lifecycle.duplicated(["signal_date", "stock_id"]).any():
        fail("formal lifecycle must contain one terminal lifecycle row per signal/stock")
    mature_lifecycle = formal_lifecycle[formal_lifecycle["mature_sample_eligible"].astype(str).str.lower().eq("true")]
    if mature_lifecycle.empty:
        fail("formal lifecycle has no mature_sample_eligible rows")
    formal_keys = set(zip(formal_events["signal_date"].astype(str), formal_events["stock_id"].astype(str)))
    lifecycle_mature_keys = set(zip(mature_lifecycle["signal_date"].astype(str), mature_lifecycle["stock_id"].astype(str)))
    missing_mature_lifecycle = sorted(formal_keys - lifecycle_mature_keys)[:20]
    if missing_mature_lifecycle:
        fail(f"formal events missing matching mature lifecycle rows: {missing_mature_lifecycle}")
    lifecycle_state_lookup = {
        (str(row["signal_date"]), str(row["stock_id"])): str(row["operation_lifecycle_state"])
        for _, row in formal_lifecycle.iterrows()
    }
    for _, row in formal_events.iterrows():
        key = (str(row["signal_date"]), str(row["stock_id"]))
        if str(row["operation_lifecycle_state"]) != lifecycle_state_lookup.get(key):
            fail(f"formal event lifecycle state must match lifecycle artifact for signal={key[0]} stock={key[1]}")

    trigger_scope = formal_summary[
        formal_summary["confluence_scope"].astype(str).eq("operation_trigger")
        & formal_summary["confluence_id"].astype(str).eq("all_confirmed_volume_breakout")
    ].copy()
    for _, row in trigger_scope.iterrows():
        tdcc_list_type = str(row["tdcc_list_type"])
        rank_bucket = str(row["rank_bucket"])
        trigger_id = str(row["trigger_id"])
        part = formal_events[
            formal_events["tdcc_list_type"].astype(str).eq(tdcc_list_type)
            & formal_events["trigger_id"].astype(str).eq(trigger_id)
        ].copy()
        if tdcc_list_type != "no_tdcc":
            rank_values = pd.to_numeric(part["tdcc_rank"], errors="coerce")
            if rank_bucket == "top_10":
                part = part[rank_values <= 10]
            elif rank_bucket == "top_20":
                part = part[rank_values <= 20]
            elif rank_bucket == "top_50":
                part = part[rank_values <= 50]
        expected_sample = int(pd.to_numeric(part["return_pct"], errors="coerce").dropna().shape[0])
        actual_sample = int(pd.to_numeric(pd.Series([row["sample_size"]]), errors="coerce").fillna(-1).iloc[0])
        if actual_sample != expected_sample:
            fail(
                "formal summary sample_size must be recomputable from mature formal events "
                f"tdcc={tdcc_list_type} bucket={rank_bucket} trigger={trigger_id} "
                f"actual={actual_sample} expected={expected_sample}"
            )

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
    formal_ages = pd.to_numeric(formal_events["confirmation_age_trading_days"], errors="coerce")
    if formal_ages.isna().any() or (formal_ages < 1).any() or (formal_ages > 10).any():
        fail("formal confirmation_age_trading_days must be between 1 and 10")

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
    formal_sample_size = pd.to_numeric(formal_summary["sample_size"], errors="coerce")
    if formal_sample_size.isna().any() or (formal_sample_size <= 0).any():
        fail("formal summary sample_size must be positive")
    bad_confidence = sorted(set(summary["confidence_status"].astype(str)) - {"low", "medium", "high"})
    if bad_confidence:
        fail(f"unexpected confidence_status values: {bad_confidence}")

    if not rank.empty:
        if set(rank["entry_price_status"].astype(str)) != {"next_open_pending"}:
            fail("rank entry_price_status must be next_open_pending")
        if rank.duplicated(["confirmation_date", "stock_id"]).any():
            fail("rank output must not duplicate stock confirmation rows")
        if "selected_trigger_id" in rank.columns:
            bad_selected = rank[rank["selected_trigger_id"].astype(str).ne(rank["trigger_id"].astype(str))]
            if not bad_selected.empty:
                fail("rank trigger_id must match selected_trigger_id")

    print(
        "volume breakout confirmed operation validation passed "
        f"summary_rows={len(summary)} event_rows={len(events)} "
        f"formal_summary_rows={len(formal_summary)} formal_event_rows={len(formal_events)} "
        f"formal_lifecycle_rows={len(formal_lifecycle)} rank_rows={len(rank)} pending_rows={len(pending)}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
