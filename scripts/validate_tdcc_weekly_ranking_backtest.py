from __future__ import annotations

from pathlib import Path
import sys

import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent))

from research_tdcc_dataset_consumer import load_research_tdcc_dataset_contract  # noqa: E402


ROOT = Path(__file__).resolve().parents[1]
LATEST_CSV = ROOT / "output/latest/tdcc_weekly_ranking_backtest_latest.csv"
LATEST_MD = ROOT / "output/latest/tdcc_weekly_ranking_backtest_latest.md"
HISTORY_SUMMARY = ROOT / "output/history/research/tdcc_weekly_ranking_backtest.csv"
HISTORY_EVENTS = ROOT / "output/history/research/tdcc_weekly_ranking_backtest_events.csv"

REQUIRED_SUMMARY_COLUMNS = {
    "model_id",
    "ranking_model_version",
    "tdcc_list_type",
    "rank_bucket",
    "horizon",
    "event_count",
    "win_rate",
    "avg_return",
    "median_return",
    "out_of_sample_pass",
    "confidence_status",
    "approved_for_daily",
    "source_tdcc_dataset_id",
}

REQUIRED_EVENT_COLUMNS = {
    "model_id",
    "ranking_model_version",
    "tdcc_list_type",
    "signal_date",
    "source_tdcc_dataset_id",
    "source_tdcc_prior_date",
    "tdcc_interval_status",
    "stock_id",
    "tdcc_rank",
    "tdcc_ranking_score",
    "tdcc_weighted_weekly_increase_score",
    "tdcc_effective_increase_count",
    "tdcc_high_pair_effective_streak_weeks",
    "d5_return_pct",
    "d10_return_pct",
    "d20_return_pct",
    "approved_for_daily",
}

FORBIDDEN_COLUMNS = {
    "trade_decision",
    "action_rating",
    "entry_style",
    "position_sizing",
    "buy_signal",
}


def read(path: Path) -> pd.DataFrame:
    if not path.exists():
        raise FileNotFoundError(path)
    return pd.read_csv(path, dtype=str)


def bool_false_only(series: pd.Series) -> bool:
    return set(series.fillna("").astype(str).str.lower().unique()) <= {"false", "0", ""}


def main() -> int:
    errors: list[str] = []
    try:
        contract = load_research_tdcc_dataset_contract()
    except Exception as exc:
        print(f"ERROR: cannot load canonical TDCC dataset contract: {exc}")
        return 1
    for path in [LATEST_CSV, LATEST_MD, HISTORY_SUMMARY, HISTORY_EVENTS]:
        if not path.exists():
            errors.append(f"missing required output: {path.relative_to(ROOT)}")

    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1

    summary = read(LATEST_CSV)
    history = read(HISTORY_SUMMARY)
    events = read(HISTORY_EVENTS)

    if summary.empty:
        errors.append("latest summary is empty")
    if history.empty:
        errors.append("history summary is empty")
    if events.empty:
        errors.append("event history is empty")

    missing_summary = REQUIRED_SUMMARY_COLUMNS - set(summary.columns)
    missing_events = REQUIRED_EVENT_COLUMNS - set(events.columns)
    if missing_summary:
        errors.append(f"latest summary missing columns: {sorted(missing_summary)}")
    if missing_events:
        errors.append(f"event history missing columns: {sorted(missing_events)}")

    bad_cols = FORBIDDEN_COLUMNS & (set(summary.columns) | set(events.columns))
    if bad_cols:
        errors.append(f"research output contains production decision columns: {sorted(bad_cols)}")

    if "model_id" in summary.columns and set(summary["model_id"].dropna().unique()) != {"tdcc_weekly_ranking_formula"}:
        errors.append("summary model_id must be tdcc_weekly_ranking_formula")
    if "tdcc_list_type" in summary.columns:
        allowed = {"weekly_increase", "consecutive_accumulation"}
        bad = set(summary["tdcc_list_type"].dropna().unique()) - allowed
        if bad:
            errors.append(f"unexpected tdcc_list_type values: {sorted(bad)}")
    if "rank_bucket" in summary.columns:
        allowed = {"top_10", "top_20", "top_50"}
        bad = set(summary["rank_bucket"].dropna().unique()) - allowed
        if bad:
            errors.append(f"unexpected rank_bucket values: {sorted(bad)}")
    if "horizon" in summary.columns:
        allowed = {"D+5", "D+10", "D+20"}
        bad = set(summary["horizon"].dropna().unique()) - allowed
        if bad:
            errors.append(f"unexpected horizon values: {sorted(bad)}")
    if "confidence_status" in summary.columns:
        allowed = {"low", "medium", "high"}
        bad = set(summary["confidence_status"].dropna().unique()) - allowed
        if bad:
            errors.append(f"unexpected confidence_status values: {sorted(bad)}")

    if "approved_for_daily" in summary.columns and not bool_false_only(summary["approved_for_daily"]):
        errors.append("summary approved_for_daily must remain false")
    if "approved_for_daily" in events.columns and not bool_false_only(events["approved_for_daily"]):
        errors.append("events approved_for_daily must remain false")

    for label, frame in [("summary", summary), ("history summary", history), ("events", events)]:
        if "source_tdcc_dataset_id" in frame.columns:
            values = sorted({value for value in frame["source_tdcc_dataset_id"].fillna("").astype(str) if value})
            if values != [contract.dataset_id]:
                errors.append(
                    f"{label} source_tdcc_dataset_id mismatch: expected {contract.dataset_id}, got {values}"
                )

    if {"signal_date", "source_tdcc_prior_date", "tdcc_interval_status"}.issubset(events.columns):
        date_positions = {date: index for index, date in enumerate(contract.history_dates)}
        for _, row in events.iterrows():
            signal_date = str(row["signal_date"])
            position = date_positions.get(signal_date)
            if position is None or position == 0:
                errors.append(f"event signal_date is outside canonical history intervals: {signal_date}")
                break
            expected_prior = contract.history_dates[position - 1]
            if str(row["source_tdcc_prior_date"]) != expected_prior:
                errors.append(
                    f"event source_tdcc_prior_date mismatch for {signal_date}: expected {expected_prior}"
                )
                break
            if str(row["tdcc_interval_status"]) != "complete_official_period":
                errors.append("ranked TDCC event must come from a complete official-period interval")
                break

    if "tdcc_rank" in events.columns:
        ranks = pd.to_numeric(events["tdcc_rank"], errors="coerce")
        if ranks.isna().any() or ranks.min() < 1 or ranks.max() > 50:
            errors.append("event tdcc_rank must be numeric between 1 and 50")

    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1

    print("TDCC weekly ranking backtest validation passed")
    print(f"summary_rows={len(summary)}")
    print(f"event_rows={len(events)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
