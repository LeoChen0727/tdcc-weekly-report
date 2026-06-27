from __future__ import annotations

from pathlib import Path
import math

import pandas as pd

from build_neckline_volume_breakout_candidate_spec import (
    FORBIDDEN_PRODUCTION_FIELDS,
    HISTORY_CSV,
    LATEST_CSV,
    LATEST_MD,
    MODEL_ID,
    OUTPUT_COLUMNS,
    PRODUCTION_READINESS,
    RESEARCH_ID,
    RESEARCH_VARIANT_ID,
    SOURCE_EVENTS_CSV,
    base_breakout_sample,
    build,
    read_csv,
)


REQUIRED_COLUMNS = set(OUTPUT_COLUMNS)


def fail(message: str) -> None:
    print(f"ERROR: {message}")
    raise SystemExit(1)


def false_only(series: pd.Series) -> bool:
    return set(series.astype(str).str.lower().unique()) <= {"false", "0", ""}


def close_enough(left: str, right: str, tolerance: float = 0.0002) -> bool:
    if not left and not right:
        return True
    try:
        return abs(float(left) - float(right)) <= tolerance
    except ValueError:
        return False


def main() -> int:
    latest = read_csv(LATEST_CSV)
    history = read_csv(HISTORY_CSV)
    if not LATEST_MD.exists():
        fail(f"missing markdown spec: {LATEST_MD}")
    if latest.empty:
        fail(f"{LATEST_CSV} must not be empty")
    if len(latest) != len(history):
        fail("latest/history candidate spec row counts differ")
    missing = sorted(REQUIRED_COLUMNS - set(latest.columns))
    if missing:
        fail(f"{LATEST_CSV} missing columns: {missing}")
    missing_history = sorted(REQUIRED_COLUMNS - set(history.columns))
    if missing_history:
        fail(f"{HISTORY_CSV} missing columns: {missing_history}")
    forbidden = sorted((set(latest.columns) | set(history.columns)) & FORBIDDEN_PRODUCTION_FIELDS)
    if forbidden:
        fail(f"candidate spec must not emit production decision fields: {forbidden}")
    constants = {
        "model_id": MODEL_ID,
        "research_id": RESEARCH_ID,
        "research_variant_id": RESEARCH_VARIANT_ID,
        "advisory_status": RESEARCH_VARIANT_ID,
        "production_readiness": PRODUCTION_READINESS,
    }
    for column, expected in constants.items():
        values = set(latest[column].astype(str))
        if values != {expected}:
            fail(f"{column} must be {expected}; got {sorted(values)}")
    if not false_only(latest["approved_for_daily"]):
        fail("approved_for_daily must remain false")

    expected = build("VALIDATION_GENERATED_AT")
    comparable_columns = [column for column in OUTPUT_COLUMNS if column != "generated_at"]
    latest_cmp = latest[comparable_columns].reset_index(drop=True)
    expected_cmp = expected[comparable_columns].reset_index(drop=True)
    if list(latest_cmp["segment_id"]) != list(expected_cmp["segment_id"]):
        fail("segment_id order or membership changed unexpectedly")
    metric_columns = [
        "sample_size",
        "unique_stock_count",
        "post_confirmation_count",
        "tdcc_any_age7_count",
        "second_arc_ratio_ge_1p5_count",
        "a_evaluated_sample_size",
        "a_win_count",
        "a_loss_count",
        "a_win_rate_pct",
        "a_avg_return_pct",
        "a_median_return_pct",
        "a_stop_signal_low_count",
        "a_fixed_10d_close_count",
        "c_evaluated_sample_size",
        "c_win_count",
        "c_loss_count",
        "c_win_rate_pct",
        "c_avg_return_pct",
        "c_median_return_pct",
        "c_stop_signal_low_count",
        "c_fixed_10d_close_count",
    ]
    for idx, row in latest_cmp.iterrows():
        expected_row = expected_cmp.iloc[idx]
        for column in comparable_columns:
            if column in metric_columns:
                if not close_enough(str(row[column]), str(expected_row[column])):
                    fail(
                        f"{row['segment_id']} {column} mismatch: "
                        f"spec={row[column]} expected={expected_row[column]}"
                    )
            elif str(row[column]) != str(expected_row[column]):
                fail(
                    f"{row['segment_id']} {column} mismatch: "
                    f"spec={row[column]} expected={expected_row[column]}"
                )

    source = read_csv(SOURCE_EVENTS_CSV)
    base = base_breakout_sample(source)
    all_row = latest[latest["segment_id"].eq("w_bottom_breakout_all_sym1p5")].iloc[0]
    if int(all_row["sample_size"]) != len(base):
        fail("all-breakout sample size no longer matches source breakout sample")
    post_row = latest[latest["segment_id"].eq("w_bottom_breakout_post_confirmation_sym1p5")].iloc[0]
    if "not tradable" not in str(post_row["future_leakage_warning"]):
        fail("post-confirmation A-entry leakage warning is missing")
    if float(post_row["a_win_rate_pct"]) <= float(all_row["a_win_rate_pct"]):
        fail("expected post-confirmation A-entry observed view to exceed all-breakout A-entry")
    if not math.isfinite(float(post_row["c_win_rate_pct"])):
        fail("post-confirmation C-entry win rate must be finite")

    md_text = Path(LATEST_MD).read_text(encoding="utf-8", errors="replace")
    required_text = [
        "production impact: `none`",
        "future information",
        "does not yet support promotion to production",
        "Win rate here means positive",
        "separate model-change PR",
    ]
    for text in required_text:
        if text not in md_text:
            fail(f"markdown missing required text: {text}")
    print(
        "Neckline volume breakout candidate spec validation passed "
        f"rows={len(latest)} all_sample={all_row['sample_size']} "
        f"all_a_win_rate={all_row['a_win_rate_pct']} post_c_win_rate={post_row['c_win_rate_pct']}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
