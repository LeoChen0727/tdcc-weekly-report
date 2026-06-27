from __future__ import annotations

from pathlib import Path

import pandas as pd

from build_breakout_family_retest_grid import FORBIDDEN_PRODUCTION_FIELDS, PRODUCTION_READINESS, RESEARCH_VARIANT_ID
from build_structured_neckline_retest_entry_exit_grid import (
    DETAIL_COLUMNS,
    EVENT_FAMILY_ID,
    EXIT_RULE_IDS,
    HISTORY_DETAIL_CSV,
    HISTORY_SUMMARY_CSV,
    LATEST_DETAIL_CSV,
    LATEST_MD,
    LATEST_SUMMARY_CSV,
    OUTCOME_RULE_BY_EXIT,
    RESEARCH_ID,
    SEGMENTS,
    STOP_RULE_IDS,
    SUMMARY_COLUMNS,
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


def metric(series: pd.Series) -> pd.Series:
    return pd.to_numeric(series, errors="coerce")


def assert_common_contract(df: pd.DataFrame, columns: list[str], label: str) -> None:
    missing = sorted(set(columns) - set(df.columns))
    if missing:
        fail(f"{label} missing columns: {missing}")
    forbidden = sorted(set(df.columns) & FORBIDDEN_PRODUCTION_FIELDS)
    if forbidden:
        fail(f"{label} must not contain production decision fields: {forbidden}")
    if set(df["research_id"].astype(str)) != {RESEARCH_ID}:
        fail(f"{label} research_id must be {RESEARCH_ID}")
    if set(df["research_variant_id"].astype(str)) != {RESEARCH_VARIANT_ID}:
        fail(f"{label} research_variant_id must be {RESEARCH_VARIANT_ID}")
    if set(df["advisory_status"].astype(str)) != {RESEARCH_VARIANT_ID}:
        fail(f"{label} advisory_status must be {RESEARCH_VARIANT_ID}")
    if set(df["event_family_id"].astype(str)) != {EVENT_FAMILY_ID}:
        fail(f"{label} event_family_id must be {EVENT_FAMILY_ID}")
    if set(df["production_readiness"].astype(str)) != {PRODUCTION_READINESS}:
        fail(f"{label} production_readiness must be {PRODUCTION_READINESS}")
    if not false_only(df["approved_for_daily"]):
        fail(f"{label} approved_for_daily must remain false")


def validate_required_values(detail: pd.DataFrame, summary: pd.DataFrame) -> None:
    expected_segments = {item[0] for item in SEGMENTS}
    detail_segments = set(detail["segment_id"].astype(str))
    summary_segments = set(summary["segment_id"].astype(str))
    missing_detail_segments = sorted(expected_segments - detail_segments)
    missing_summary_segments = sorted(expected_segments - summary_segments)
    if missing_detail_segments:
        fail(f"detail missing expected segments: {missing_detail_segments}")
    if missing_summary_segments:
        fail(f"summary missing expected segments: {missing_summary_segments}")
    if set(detail["stop_rule_id"].astype(str)) != set(STOP_RULE_IDS):
        fail("detail stop_rule_id set does not match expected stop rules")
    if set(detail["exit_rule_id"].astype(str)) != set(EXIT_RULE_IDS):
        fail("detail exit_rule_id set does not match expected exit rules")
    expected_outcomes = set(OUTCOME_RULE_BY_EXIT.values())
    if set(detail["outcome_rule_id"].astype(str)) != expected_outcomes:
        fail("detail outcome_rule_id set does not match expected outcome rules")
    if set(summary["stop_rule_id"].astype(str)) != set(STOP_RULE_IDS):
        fail("summary stop_rule_id set does not match expected stop rules")
    if set(summary["exit_rule_id"].astype(str)) != set(EXIT_RULE_IDS):
        fail("summary exit_rule_id set does not match expected exit rules")
    if set(summary["outcome_rule_id"].astype(str)) != expected_outcomes:
        fail("summary outcome_rule_id set does not match expected outcome rules")
    outcomes = set(detail["outcome_result"].astype(str))
    if not outcomes <= {"win", "neutral", "loss", "incomplete"}:
        fail(f"unexpected detail outcome_result values: {sorted(outcomes)}")
    positives = set(detail["positive_return_result"].astype(str))
    if not positives <= {"positive", "non_positive", "incomplete"}:
        fail(f"unexpected detail positive_return_result values: {sorted(positives)}")


def validate_summary_math(detail: pd.DataFrame, summary: pd.DataFrame) -> None:
    keys = ["segment_id", "stop_rule_id", "exit_rule_id", "outcome_rule_id"]
    grouped = detail.groupby(keys, dropna=False)
    if len(grouped) != len(summary):
        fail("summary row count does not match detail grouping count")
    for _, row in summary.iterrows():
        key = tuple(row[col] for col in keys)
        if key not in grouped.groups:
            fail(f"summary key missing from detail: {key}")
        group = grouped.get_group(key)
        outcomes = group["outcome_result"].astype(str)
        wins = int(outcomes.eq("win").sum())
        neutral = int(outcomes.eq("neutral").sum())
        losses = int(outcomes.eq("loss").sum())
        incomplete = int(outcomes.eq("incomplete").sum())
        evaluated = wins + neutral + losses
        mature = wins + losses
        if int(row["sample_size"]) != len(group):
            fail(f"sample_size mismatch for {key}")
        if int(row["evaluated_sample_size"]) != evaluated:
            fail(f"evaluated_sample_size mismatch for {key}")
        if int(row["mature_sample_size"]) != mature:
            fail(f"mature_sample_size mismatch for {key}")
        if int(row["win_count"]) != wins or int(row["neutral_count"]) != neutral or int(row["loss_count"]) != losses:
            fail(f"outcome count mismatch for {key}")
        if int(row["incomplete_count"]) != incomplete:
            fail(f"incomplete_count mismatch for {key}")
        pure = metric(pd.Series([row["pure_win_rate_pct"]])).iloc[0]
        expected_pure = wins / mature * 100.0 if mature else float("nan")
        if mature and abs(pure - expected_pure) > 0.01:
            fail(f"pure_win_rate_pct mismatch for {key}")
        neutral_success = metric(pd.Series([row["neutral_inclusive_success_rate_pct"]])).iloc[0]
        expected_neutral_success = (wins + neutral) / evaluated * 100.0 if evaluated else float("nan")
        if evaluated and abs(neutral_success - expected_neutral_success) > 0.01:
            fail(f"neutral_inclusive_success_rate_pct mismatch for {key}")


def validate_markdown() -> None:
    if not LATEST_MD.exists():
        fail(f"missing markdown output: {LATEST_MD}")
    text = LATEST_MD.read_text(encoding="utf-8", errors="replace")
    required_text = [
        "not a production recommendation",
        "approved_for_daily=false",
        "retest-not-broken then renewed attack",
        "neutral is not silently renamed as win rate",
        "win rate alone is not enough",
        "`avg_return_pct`",
        "`median_return_pct`",
        "production model conditions, scoring, ranking",
        "does not write research variants into the production baseline",
        "A formal promotion/sync PR is still required",
    ]
    for item in required_text:
        if item not in text:
            fail(f"markdown missing required text: {item}")


def main() -> int:
    latest_detail = read_csv(LATEST_DETAIL_CSV)
    latest_summary = read_csv(LATEST_SUMMARY_CSV)
    history_detail = read_csv(HISTORY_DETAIL_CSV)
    history_summary = read_csv(HISTORY_SUMMARY_CSV)
    if latest_detail.empty:
        fail("latest detail must not be empty")
    if latest_summary.empty:
        fail("latest summary must not be empty")
    if len(latest_detail) != len(history_detail):
        fail("latest/history detail row counts differ")
    if len(latest_summary) != len(history_summary):
        fail("latest/history summary row counts differ")
    assert_common_contract(latest_detail, DETAIL_COLUMNS, "detail")
    assert_common_contract(latest_summary, SUMMARY_COLUMNS, "summary")
    validate_required_values(latest_detail, latest_summary)
    validate_summary_math(latest_detail, latest_summary)
    validate_markdown()
    print(
        "structured neckline retest entry/exit grid validation passed "
        f"detail_rows={len(latest_detail)} summary_rows={len(latest_summary)}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
