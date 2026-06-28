from __future__ import annotations

from pathlib import Path

import pandas as pd

from build_breakout_family_retest_grid import (
    DETAIL_COLUMNS,
    FORBIDDEN_PRODUCTION_FIELDS,
    HISTORY_DETAIL_CSV,
    HISTORY_SUMMARY_CSV,
    LATEST_DETAIL_CSV,
    LATEST_MD,
    LATEST_SUMMARY_CSV,
    PRODUCTION_READINESS,
    RESEARCH_ID,
    RESEARCH_VARIANT_ID,
    SUMMARY_COLUMNS,
)


EXPECTED_FAMILIES = {
    "bottom_base_volume_attack_reference",
    "structured_neckline_volume_breakout_proxy",
    "descending_resistance_volume_breakout_proxy",
}

EXPECTED_ENTRY_VARIANTS = {
    "direct_breakout_next_open",
    "retest_hold_then_attack_next_open",
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
    detail = read_csv(LATEST_DETAIL_CSV)
    summary = read_csv(LATEST_SUMMARY_CSV)
    history_detail = read_csv(HISTORY_DETAIL_CSV)
    history_summary = read_csv(HISTORY_SUMMARY_CSV)
    if not LATEST_MD.exists():
        fail(f"missing markdown output: {LATEST_MD}")
    if detail.empty:
        fail("detail output must not be empty")
    if summary.empty:
        fail("summary output must not be empty")
    if len(detail) != len(history_detail):
        fail("latest/history detail row counts differ")
    if len(summary) != len(history_summary):
        fail("latest/history summary row counts differ")
    missing_detail = sorted(set(DETAIL_COLUMNS) - set(detail.columns))
    missing_summary = sorted(set(SUMMARY_COLUMNS) - set(summary.columns))
    if missing_detail:
        fail(f"detail missing columns: {missing_detail}")
    if missing_summary:
        fail(f"summary missing columns: {missing_summary}")
    forbidden = sorted((set(detail.columns) | set(summary.columns)) & FORBIDDEN_PRODUCTION_FIELDS)
    if forbidden:
        fail(f"outputs must not contain production decision fields: {forbidden}")
    for df_name, df in [("detail", detail), ("summary", summary)]:
        if set(df["research_id"].astype(str)) != {RESEARCH_ID}:
            fail(f"{df_name} research_id must be {RESEARCH_ID}")
        if set(df["research_variant_id"].astype(str)) != {RESEARCH_VARIANT_ID}:
            fail(f"{df_name} research_variant_id must be {RESEARCH_VARIANT_ID}")
        if set(df["advisory_status"].astype(str)) != {RESEARCH_VARIANT_ID}:
            fail(f"{df_name} advisory_status must be {RESEARCH_VARIANT_ID}")
        if set(df["production_readiness"].astype(str)) != {PRODUCTION_READINESS}:
            fail(f"{df_name} production_readiness must be {PRODUCTION_READINESS}")
        if not false_only(df["approved_for_daily"]):
            fail(f"{df_name} approved_for_daily must remain false")
    families = set(detail["event_family_id"].astype(str))
    missing_families = sorted(EXPECTED_FAMILIES - families)
    if missing_families:
        fail(f"missing expected event families: {missing_families}")
    entry_variants = set(detail["entry_variant"].astype(str))
    if entry_variants != EXPECTED_ENTRY_VARIANTS:
        fail(f"entry variants must be {sorted(EXPECTED_ENTRY_VARIANTS)}; got {sorted(entry_variants)}")
    summary_keys = set(
        zip(
            summary["event_family_id"].astype(str),
            summary["pattern_subtype"].astype(str),
            summary["entry_variant"].astype(str),
        )
    )
    detail_keys = set(
        zip(
            detail["event_family_id"].astype(str),
            detail["pattern_subtype"].astype(str),
            detail["entry_variant"].astype(str),
        )
    )
    if summary_keys != detail_keys:
        fail("summary keys do not match detail keys")
    for key, group in detail.groupby(["event_family_id", "pattern_subtype", "entry_variant"], dropna=False):
        row = summary[
            summary["event_family_id"].astype(str).eq(str(key[0]))
            & summary["pattern_subtype"].astype(str).eq(str(key[1]))
            & summary["entry_variant"].astype(str).eq(str(key[2]))
        ].iloc[0]
        if int(row["sample_size"]) != len(group):
            fail(f"sample_size mismatch for {key}")
        if key[2] == "direct_breakout_next_open":
            mature = pd.to_numeric(group["direct_return_pct"], errors="coerce").notna().sum()
        else:
            mature = pd.to_numeric(group["retest_return_pct"], errors="coerce").notna().sum()
        if int(row["mature_sample_size"]) != int(mature):
            fail(f"mature_sample_size mismatch for {key}")
    md_text = LATEST_MD.read_text(encoding="utf-8", errors="replace")
    required_text = [
        "no longer limited to W-bottom",
        "short local base ceiling",
        "direct_breakout_next_open",
        "retest_hold_then_attack_next_open",
        "not as a production recommendation",
    ]
    for text in required_text:
        if text not in md_text:
            fail(f"markdown missing required text: {text}")
    print(
        "breakout family retest grid validation passed "
        f"detail_rows={len(detail)} summary_rows={len(summary)} families={sorted(families)}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
