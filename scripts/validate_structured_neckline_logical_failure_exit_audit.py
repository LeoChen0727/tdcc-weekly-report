from __future__ import annotations

from pathlib import Path

import pandas as pd

from build_structured_neckline_logical_failure_exit_audit import (
    BASELINE_RULE_ID,
    DETAIL_COLUMNS,
    FAILURE_EXIT_RULE_IDS,
    FAILURE_EXIT_SCOPE_ID,
    HISTORY_DETAIL_CSV,
    HISTORY_SUMMARY_CSV,
    LATEST_DETAIL_CSV,
    LATEST_MD,
    LATEST_SUMMARY_CSV,
    PARAMETER_SET_ID,
    PRODUCTION_READINESS,
    RESEARCH_ID,
    RESEARCH_VARIANT_ID,
    SUMMARY_COLUMNS,
)


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
    if not path.exists():
        fail(f"missing required file: {path}")
    try:
        return pd.read_csv(path, dtype=str, keep_default_na=False)
    except Exception as exc:
        fail(f"{path} is not readable CSV: {exc}")


def false_only(series: pd.Series) -> bool:
    return set(series.astype(str).str.lower().unique()) <= {"false", "0", ""}


def require_columns(frame: pd.DataFrame, columns: list[str], label: str) -> None:
    missing = sorted(set(columns) - set(frame.columns))
    if missing:
        fail(f"{label} missing columns: {missing}")


def validate_constants(frame: pd.DataFrame, label: str) -> None:
    constants = {
        "research_id": RESEARCH_ID,
        "research_variant_id": RESEARCH_VARIANT_ID,
        "parameter_set_id": PARAMETER_SET_ID,
        "advisory_status": RESEARCH_VARIANT_ID,
        "failure_exit_scope_id": FAILURE_EXIT_SCOPE_ID,
        "production_readiness": PRODUCTION_READINESS,
    }
    for column, expected in constants.items():
        values = set(frame[column].astype(str))
        if values != {expected}:
            fail(f"{label} {column} must be {expected}; got {sorted(values)}")
    if not false_only(frame["approved_for_daily"]):
        fail(f"{label} approved_for_daily must remain false")


def main() -> int:
    detail = read_csv(LATEST_DETAIL_CSV)
    summary = read_csv(LATEST_SUMMARY_CSV)
    history_detail = read_csv(HISTORY_DETAIL_CSV)
    history_summary = read_csv(HISTORY_SUMMARY_CSV)
    if detail.empty or summary.empty:
        fail("latest outputs must not be empty")
    if len(detail) != len(history_detail):
        fail("detail latest/history row counts differ")
    if len(summary) != len(history_summary):
        fail("summary latest/history row counts differ")
    if not LATEST_MD.exists():
        fail(f"missing markdown output: {LATEST_MD}")

    require_columns(detail, DETAIL_COLUMNS, "detail")
    require_columns(summary, SUMMARY_COLUMNS, "summary")
    forbidden = sorted((set(detail.columns) | set(summary.columns)) & FORBIDDEN_PRODUCTION_FIELDS)
    if forbidden:
        fail(f"outputs must not emit production decision fields: {forbidden}")
    validate_constants(detail, "detail")
    validate_constants(summary, "summary")

    expected_detail_rows = 23 * len(FAILURE_EXIT_RULE_IDS)
    if len(detail) != expected_detail_rows:
        fail(f"expected {expected_detail_rows} detail rows; got {len(detail)}")
    if len(summary) != len(FAILURE_EXIT_RULE_IDS):
        fail(f"expected {len(FAILURE_EXIT_RULE_IDS)} summary rows; got {len(summary)}")
    if list(summary["failure_exit_rule_id"].astype(str)) != FAILURE_EXIT_RULE_IDS:
        fail(f"summary failure_exit_rule_id order mismatch: {list(summary['failure_exit_rule_id'].astype(str))}")
    if set(detail["failure_exit_rule_id"].astype(str)) != set(FAILURE_EXIT_RULE_IDS):
        fail(f"detail failure_exit_rule_id mismatch: {sorted(set(detail['failure_exit_rule_id'].astype(str)))}")

    event_counts = detail.groupby("failure_exit_rule_id").size().to_dict()
    for rule_id in FAILURE_EXIT_RULE_IDS:
        if int(event_counts.get(rule_id, 0)) != 23:
            fail(f"{rule_id} must have 23 events; got {event_counts.get(rule_id, 0)}")

    if "bearish" in set(detail["visual_pre_signal_context"].astype(str)):
        fail("detail must not include bearish pre-signal context rows")
    names = detail["stock_name"].astype(str)
    bad_names = detail[names.str.contains("\ufffd", regex=False) | names.str.contains("嚙", regex=False)]
    if not bad_names.empty:
        fail(f"stock_name contains replacement/mojibake characters for ids: {sorted(bad_names['stock_id'].astype(str).unique())}")

    outcomes = set(detail["outcome_result"].astype(str))
    if not outcomes <= {"win", "neutral", "loss", "incomplete"}:
        fail(f"unexpected outcomes: {sorted(outcomes)}")
    if "win" not in outcomes or "loss" not in outcomes:
        fail("detail must include both win and loss outcomes")

    baseline = detail[detail["failure_exit_rule_id"].astype(str).eq(BASELINE_RULE_ID)]
    if baseline.empty:
        fail("missing baseline rows")
    if not baseline["baseline_outcome"].astype(str).eq(baseline["outcome_result"].astype(str)).all():
        fail("baseline rule must preserve baseline outcomes")
    baseline_summary = summary[summary["failure_exit_rule_id"].astype(str).eq(BASELINE_RULE_ID)]
    if baseline_summary.empty:
        fail("missing baseline summary")
    if int(baseline_summary["changed_from_baseline_count"].iloc[0]) != 0:
        fail("baseline changed_from_baseline_count must be 0")

    non_baseline = summary[~summary["failure_exit_rule_id"].astype(str).eq(BASELINE_RULE_ID)]
    if non_baseline.empty:
        fail("missing non-baseline rule summaries")
    changed_total = pd.to_numeric(non_baseline["changed_from_baseline_count"], errors="coerce").fillna(0).sum()
    if changed_total <= 0:
        fail("at least one logical failure rule must change a baseline outcome")

    numeric_columns = [
        "sample_size",
        "unique_stock_count",
        "win_count",
        "neutral_count",
        "loss_count",
        "avg_return_pct",
        "median_return_pct",
        "avg_max_close_return_pct",
        "median_max_close_return_pct",
        "avg_min_close_return_pct",
        "median_min_close_return_pct",
        "changed_from_baseline_count",
        "baseline_loss_to_non_loss_count",
        "baseline_non_loss_to_loss_count",
    ]
    for column in numeric_columns:
        if pd.to_numeric(summary[column], errors="coerce").isna().any():
            fail(f"summary column must be numeric: {column}")

    md_text = LATEST_MD.read_text(encoding="utf-8", errors="replace")
    required_text = [
        "Logical Failure Exit Audit",
        "intraday high/low trigger is not used",
        "production impact: `none`",
        "No production model condition, scoring, ranking, PDF logic, or baseline was changed.",
        PRODUCTION_READINESS,
    ]
    for text in required_text:
        if text not in md_text:
            fail(f"markdown missing required text: {text}")

    print(
        "structured neckline logical failure exit audit validation passed "
        f"detail_rows={len(detail)} summary_rows={len(summary)}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
