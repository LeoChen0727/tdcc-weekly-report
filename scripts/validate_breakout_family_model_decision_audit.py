from __future__ import annotations

from pathlib import Path

import pandas as pd

from build_breakout_family_model_decision_audit import (
    HISTORY_CSV,
    LATEST_CSV,
    LATEST_MD,
    OUTPUT_COLUMNS,
    PRODUCTION_READINESS,
    RESEARCH_ID,
    RESEARCH_VARIANT_ID,
)
from build_breakout_family_retest_grid import FORBIDDEN_PRODUCTION_FIELDS


EXPECTED_FAMILY_ROWS = {
    "bottom_base_volume_attack_reference",
    "descending_resistance_volume_breakout_proxy",
    "structured_neckline_volume_breakout_proxy",
}

EXPECTED_ENTRY_DECISIONS = {
    "prioritize_retest_confirmation_research",
    "insufficient_retest_sample",
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
        fail("latest audit must not be empty")
    if len(latest) != len(history):
        fail("latest/history row counts differ")
    if not LATEST_MD.exists():
        fail(f"missing markdown output: {LATEST_MD}")
    missing = sorted(set(OUTPUT_COLUMNS) - set(latest.columns))
    if missing:
        fail(f"audit missing columns: {missing}")
    forbidden = sorted(set(latest.columns) & FORBIDDEN_PRODUCTION_FIELDS)
    if forbidden:
        fail(f"audit must not contain production decision fields: {forbidden}")
    if set(latest["research_id"].astype(str)) != {RESEARCH_ID}:
        fail(f"research_id must be {RESEARCH_ID}")
    if set(latest["research_variant_id"].astype(str)) != {RESEARCH_VARIANT_ID}:
        fail(f"research_variant_id must be {RESEARCH_VARIANT_ID}")
    if set(latest["advisory_status"].astype(str)) != {RESEARCH_VARIANT_ID}:
        fail(f"advisory_status must be {RESEARCH_VARIANT_ID}")
    if set(latest["production_readiness"].astype(str)) != {PRODUCTION_READINESS}:
        fail(f"production_readiness must be {PRODUCTION_READINESS}")
    if not false_only(latest["approved_for_daily"]):
        fail("approved_for_daily must remain false")
    family_rows = latest[latest["decision_scope"].astype(str).eq("family")]
    families = set(family_rows["event_family_id"].astype(str))
    missing_families = sorted(EXPECTED_FAMILY_ROWS - families)
    if missing_families:
        fail(f"missing expected family rows: {missing_families}")
    entry_decisions = set(latest["entry_decision"].astype(str))
    missing_entry_decisions = sorted(EXPECTED_ENTRY_DECISIONS - entry_decisions)
    if missing_entry_decisions:
        fail(f"missing expected entry decisions: {missing_entry_decisions}")
    if not latest["split_decision"].astype(str).str.contains("do_not_split|keep_broad|insufficient|keep_as|keep_separate").any():
        fail("audit must include explicit split/governance decisions")
    md_text = LATEST_MD.read_text(encoding="utf-8", errors="replace")
    required_text = [
        "not a production recommendation",
        "retest-not-broken",
        "do not split",
        "bottom/base volume attack",
        "approved_for_daily=false",
    ]
    for text in required_text:
        if text not in md_text:
            fail(f"markdown missing required text: {text}")
    print(
        "breakout family model decision audit validation passed "
        f"rows={len(latest)} families={sorted(families)}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
