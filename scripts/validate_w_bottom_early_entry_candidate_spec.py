from __future__ import annotations

from pathlib import Path
import math

import pandas as pd

from build_w_bottom_early_entry_candidate_spec import (
    FORBIDDEN_PRODUCTION_FIELDS,
    HISTORY_CSV,
    LATEST_CSV,
    LATEST_MD,
    MODEL_ID,
    OUTPUT_COLUMNS,
    PRODUCTION_READINESS,
    RESEARCH_ID,
    RESEARCH_VARIANT_ID,
    SELECTED_SEGMENT_ID,
    SOURCE_REVIEW_CSV,
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


def close_enough(left: str, right: float, tolerance: float = 0.0002) -> bool:
    try:
        return abs(float(left) - right) <= tolerance
    except ValueError:
        return False


def expected_metrics() -> dict[str, float | int]:
    review = read_csv(SOURCE_REVIEW_CSV)
    sample = review[review["segment_id"].eq(SELECTED_SEGMENT_ID)].copy()
    if sample.empty:
        fail(f"selected source segment is empty: {SELECTED_SEGMENT_ID}")
    win = int(sample["outcome_result"].eq("win").sum())
    neutral = int(sample["outcome_result"].eq("neutral").sum())
    loss = int(sample["outcome_result"].eq("loss").sum())
    incomplete = int(sample["outcome_result"].eq("incomplete").sum())
    sample_size = int(len(sample))
    evaluated = win + neutral + loss
    mature = win + loss
    return {
        "sample_size": sample_size,
        "evaluated_sample_size": evaluated,
        "mature_sample_size": mature,
        "win_count": win,
        "neutral_count": neutral,
        "loss_count": loss,
        "incomplete_count": incomplete,
        "pure_win_rate_pct": win / mature * 100 if mature else math.nan,
        "neutral_inclusive_success_rate_pct": (win + neutral) / evaluated * 100 if evaluated else math.nan,
        "total_sample_win_or_neutral_rate_pct": (win + neutral) / sample_size * 100 if sample_size else math.nan,
    }


def main() -> int:
    latest = read_csv(LATEST_CSV)
    history = read_csv(HISTORY_CSV)
    if not LATEST_MD.exists():
        fail(f"missing markdown spec: {LATEST_MD}")
    if len(latest) != 1:
        fail(f"{LATEST_CSV} must contain exactly one current-best candidate row")
    if len(history) != 1:
        fail(f"{HISTORY_CSV} must contain exactly one current-best candidate row")
    missing = sorted(REQUIRED_COLUMNS - set(latest.columns))
    if missing:
        fail(f"{LATEST_CSV} missing columns: {missing}")
    missing_history = sorted(REQUIRED_COLUMNS - set(history.columns))
    if missing_history:
        fail(f"{HISTORY_CSV} missing columns: {missing_history}")
    forbidden = sorted((set(latest.columns) | set(history.columns)) & FORBIDDEN_PRODUCTION_FIELDS)
    if forbidden:
        fail(f"candidate spec must not emit production decision fields: {forbidden}")
    row = latest.iloc[0]
    constants = {
        "model_id": MODEL_ID,
        "research_id": RESEARCH_ID,
        "research_variant_id": RESEARCH_VARIANT_ID,
        "advisory_status": RESEARCH_VARIANT_ID,
        "selected_segment_id": SELECTED_SEGMENT_ID,
        "production_readiness": PRODUCTION_READINESS,
    }
    for column, expected in constants.items():
        if str(row[column]) != expected:
            fail(f"{column} must be {expected}; got {row[column]}")
    if not false_only(latest["approved_for_daily"]):
        fail("approved_for_daily must remain false")

    expected = expected_metrics()
    for column in [
        "sample_size",
        "evaluated_sample_size",
        "mature_sample_size",
        "win_count",
        "neutral_count",
        "loss_count",
        "incomplete_count",
    ]:
        if int(row[column]) != int(expected[column]):
            fail(f"{column} mismatch: spec={row[column]} expected={expected[column]}")
    for column in [
        "pure_win_rate_pct",
        "neutral_inclusive_success_rate_pct",
        "total_sample_win_or_neutral_rate_pct",
    ]:
        if not close_enough(str(row[column]), float(expected[column])):
            fail(f"{column} mismatch: spec={row[column]} expected={expected[column]:.4f}")

    md_text = LATEST_MD.read_text(encoding="utf-8", errors="replace")
    required_text = [
        "production impact: `none`",
        "W-bottom neckline breakout confirmation must be reviewed as a separate model surface",
        "pure_win_rate_pct",
        "neutral_inclusive_success_rate_pct",
        "signal_rebound_from_right_low_pct",
        "40 trading days",
    ]
    for text in required_text:
        if text not in md_text:
            fail(f"markdown missing required text: {text}")
    print(
        "W-bottom early-entry candidate spec validation passed "
        f"segment={SELECTED_SEGMENT_ID} sample={row['sample_size']} "
        f"pure_win_rate={row['pure_win_rate_pct']} neutral_inclusive={row['neutral_inclusive_success_rate_pct']}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
