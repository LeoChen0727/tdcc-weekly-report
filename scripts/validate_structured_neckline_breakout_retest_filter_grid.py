from __future__ import annotations

from pathlib import Path

import pandas as pd

from build_breakout_family_retest_grid import FORBIDDEN_PRODUCTION_FIELDS, PRODUCTION_READINESS, RESEARCH_VARIANT_ID
from build_structured_neckline_breakout_retest_filter_grid import (
    EVENT_FAMILY_ID,
    HISTORY_CSV,
    LATEST_CSV,
    LATEST_MD,
    OUTPUT_COLUMNS,
    RESEARCH_ID,
)


EXPECTED_SEGMENTS = {
    "all_structured_neckline",
    "triple_or_multi_bottom_proxy",
    "double_bottom_or_structured_bottom_proxy",
    "low_position_le60",
    "clean_attack_candle",
    "weak_or_upper_shadow_candle",
    "locked_limit_down_risk",
    "formal_volume_gate_reference",
    "formal_volume_gate_low_position_le60",
    "tdcc_fresh_supportive",
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


def main() -> int:
    latest = read_csv(LATEST_CSV)
    history = read_csv(HISTORY_CSV)
    if latest.empty:
        fail("latest grid must not be empty")
    if len(latest) != len(history):
        fail("latest/history row counts differ")
    if not LATEST_MD.exists():
        fail(f"missing markdown output: {LATEST_MD}")
    missing = sorted(set(OUTPUT_COLUMNS) - set(latest.columns))
    if missing:
        fail(f"grid missing columns: {missing}")
    forbidden = sorted(set(latest.columns) & FORBIDDEN_PRODUCTION_FIELDS)
    if forbidden:
        fail(f"grid must not contain production decision fields: {forbidden}")
    if set(latest["research_id"].astype(str)) != {RESEARCH_ID}:
        fail(f"research_id must be {RESEARCH_ID}")
    if set(latest["research_variant_id"].astype(str)) != {RESEARCH_VARIANT_ID}:
        fail(f"research_variant_id must be {RESEARCH_VARIANT_ID}")
    if set(latest["advisory_status"].astype(str)) != {RESEARCH_VARIANT_ID}:
        fail(f"advisory_status must be {RESEARCH_VARIANT_ID}")
    if set(latest["event_family_id"].astype(str)) != {EVENT_FAMILY_ID}:
        fail(f"event_family_id must be {EVENT_FAMILY_ID}")
    if set(latest["production_readiness"].astype(str)) != {PRODUCTION_READINESS}:
        fail(f"production_readiness must be {PRODUCTION_READINESS}")
    if not false_only(latest["approved_for_daily"]):
        fail("approved_for_daily must remain false")
    segments = set(latest["segment_id"].astype(str))
    missing_segments = sorted(EXPECTED_SEGMENTS - segments)
    if missing_segments:
        fail(f"missing expected segments: {missing_segments}")
    if not latest["revenue_layer_status"].astype(str).eq("pending_missing_historical_revenue_panel").all():
        fail("revenue layer must stay pending instead of guessed")
    md_text = LATEST_MD.read_text(encoding="utf-8", errors="replace")
    required_text = [
        "broad structured-neckline",
        "retest-not-broken",
        "not a production recommendation",
        "current formal `volume_range_breakout` volume/candle gate",
        "not a selective filter",
        "locked limit-up can count",
        "locked limit-down is risk",
        "TDCC",
        "Revenue remains pending",
        "does not yet support production promotion",
    ]
    for text in required_text:
        if text not in md_text:
            fail(f"markdown missing required text: {text}")
    print(
        "structured neckline breakout retest filter grid validation passed "
        f"rows={len(latest)} segments={sorted(segments)}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
