from __future__ import annotations

from pathlib import Path

import pandas as pd

from build_w_bottom_research_overlap_guardrails import (
    ADVISORY_STATUS,
    ARTIFACT_VERSION,
    HISTORY_SUMMARY_CSV,
    INPUT_ARTIFACTS,
    LATEST_MD,
    LATEST_SUMMARY_CSV,
    MODEL_ID,
    PRODUCTION_READINESS,
    RESEARCH_ID,
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
    "approved_for_daily_true",
}

ALLOWED_SOURCE_PRODUCTION_READINESS = {
    "not_production_ready_research_only",
    "research_only_pending_promotion_decision",
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


def numeric(series: pd.Series) -> pd.Series:
    return pd.to_numeric(series, errors="coerce")


def validate_common(latest: pd.DataFrame, history: pd.DataFrame) -> None:
    if latest.empty:
        fail("guardrail summary must not be empty")
    if len(latest) != len(history):
        fail("latest/history guardrail row counts differ")
    missing = sorted(set(SUMMARY_COLUMNS) - set(latest.columns))
    if missing:
        fail(f"guardrail summary missing columns: {missing}")
    forbidden = sorted(set(latest.columns) & FORBIDDEN_PRODUCTION_FIELDS)
    if forbidden:
        fail(f"guardrail summary must not contain production decision fields: {forbidden}")
    if set(latest["research_id"].astype(str)) != {RESEARCH_ID}:
        fail(f"research_id must be {RESEARCH_ID}")
    if set(latest["artifact_version"].astype(str)) != {ARTIFACT_VERSION}:
        fail(f"artifact_version must be {ARTIFACT_VERSION}")
    if set(latest["advisory_status"].astype(str)) != {ADVISORY_STATUS}:
        fail(f"advisory_status must be {ADVISORY_STATUS}")
    if set(latest["model_id"].astype(str)) != {MODEL_ID}:
        fail(f"model_id must be {MODEL_ID}")
    if set(latest["production_readiness"].astype(str)) != {PRODUCTION_READINESS}:
        fail(f"production_readiness must be {PRODUCTION_READINESS}")
    if not false_only(latest["approved_for_daily"]):
        fail("guardrail rows must remain approved_for_daily=False")


def validate_inputs_are_represented(summary: pd.DataFrame) -> None:
    expected_ids = {artifact.artifact_id for artifact in INPUT_ARTIFACTS}
    actual_ids = set(summary["input_artifact_id"].astype(str))
    if actual_ids != expected_ids:
        fail(f"input artifact set mismatch; expected={sorted(expected_ids)} actual={sorted(actual_ids)}")
    for artifact in INPUT_ARTIFACTS:
        if not artifact.path.exists():
            fail(f"missing input artifact: {artifact.path}")
        source = read_csv(artifact.path)
        forbidden = sorted(set(source.columns) & FORBIDDEN_PRODUCTION_FIELDS)
        if forbidden:
            fail(f"{artifact.artifact_id} contains forbidden production fields: {forbidden}")
        if "approved_for_daily" in source.columns and not false_only(source["approved_for_daily"]):
            fail(f"{artifact.artifact_id} must remain approved_for_daily=False")
        if "production_readiness" in source.columns:
            values = set(source["production_readiness"].astype(str))
            if not values <= ALLOWED_SOURCE_PRODUCTION_READINESS:
                fail(f"{artifact.artifact_id} production_readiness mismatch: {sorted(values)}")


def validate_overlap_guardrail(summary: pd.DataFrame) -> None:
    overlap = numeric(summary["overlap_pair_count"])
    if overlap.isna().any() or overlap.lt(0).any():
        fail("overlap_pair_count must be non-negative numeric")
    checked = numeric(summary["checked_rows"])
    unique_stocks = numeric(summary["unique_stocks"])
    if checked.isna().any() or unique_stocks.isna().any():
        fail("checked_rows and unique_stocks must be numeric")
    if overlap.sum() <= 0:
        fail("current W-bottom guardrail fixture must expose at least one overlap pair")

    blocked = summary[summary["overlap_pair_count"].astype(int).gt(0)].copy()
    if blocked.empty:
        fail("expected blocked overlap rows")
    if not blocked["promotion_evidence_status"].astype(str).eq(
        "blocked_requires_same_stock_non_overlap_artifact"
    ).all():
        fail("every overlapping strategy must be blocked from promotion evidence")
    if not blocked["required_followup"].astype(str).eq(
        "publish_same_stock_non_overlap_basis_before_promotion_evidence"
    ).all():
        fail("every overlapping strategy must require a same-stock non-overlap follow-up")

    unblocked = summary[summary["overlap_pair_count"].astype(int).eq(0)].copy()
    if not unblocked.empty and not unblocked["promotion_evidence_status"].astype(str).eq(
        "no_overlap_detected_for_strategy"
    ).all():
        fail("non-overlapping strategies must be labeled no_overlap_detected_for_strategy")

    # Regression: these artifacts are known to contain same-stock active-window overlap.
    for artifact_id in [
        "w_bottom_split_entry_outcome_backtest_detail",
        "w_bottom_early_entry_parameter_grid_detail",
    ]:
        part = summary[summary["input_artifact_id"].astype(str).eq(artifact_id)]
        if numeric(part["overlap_pair_count"]).sum() <= 0:
            fail(f"{artifact_id} should remain blocked until a non-overlap basis exists")


def validate_markdown() -> None:
    if not LATEST_MD.exists():
        fail(f"missing markdown summary: {LATEST_MD}")
    text = LATEST_MD.read_text(encoding="utf-8")
    for needle in [
        RESEARCH_ID,
        "same-stock non-overlap basis",
        "blocked_requires_same_stock_non_overlap_artifact",
        "no production registry, daily adapter, or PDF behavior change",
    ]:
        if needle not in text:
            fail(f"markdown summary missing required text: {needle}")


def main() -> int:
    latest = read_csv(LATEST_SUMMARY_CSV)
    history = read_csv(HISTORY_SUMMARY_CSV)
    validate_common(latest, history)
    validate_inputs_are_represented(latest)
    validate_overlap_guardrail(latest)
    validate_markdown()
    print(f"Validated {LATEST_SUMMARY_CSV} rows={len(latest)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
