from __future__ import annotations

import pandas as pd

from revenue_unreacted_range_extreme_return_path_audit import (
    ARTIFACT_VERSION,
    COLUMNS,
    LATEST_CSV,
    build_extreme_return_path_audit,
)


SOURCE_DETAIL = "output/latest/research_backtest/revenue_unreacted_range_fixed_confirmation_feature_contrast_audit_detail_latest.csv"
EXPECTED_STOCK_IDS = {
    "2327",
    "3090",
    "3093",
    "3229",
    "3339",
    "3443",
    "4908",
    "5464",
    "5475",
    "6588",
    "6658",
    "6683",
    "6949",
    "7750",
}


def _boolish(series: pd.Series) -> pd.Series:
    return series.astype(str).str.strip().str.lower().isin({"true", "1", "yes"})


def validate() -> list[str]:
    errors: list[str] = []
    if not LATEST_CSV.is_file():
        return [f"missing extreme return path audit: {LATEST_CSV}"]
    audit = pd.read_csv(
        LATEST_CSV,
        dtype={
            "episode_key": str,
            "stock_id": str,
            "signal_date": str,
            "confirmation_date": str,
            "entry_date": str,
            "exit_date": str,
        },
        keep_default_na=False,
        low_memory=False,
    )
    if list(audit.columns) != COLUMNS:
        errors.append("extreme return path audit schema drift")
        return errors
    if len(audit) != 14:
        errors.append(f"extreme return path audit must contain 14 rows; actual={len(audit)}")
    if set(audit["stock_id"].astype(str).str.zfill(4)) != EXPECTED_STOCK_IDS:
        errors.append("extreme return path audit stock membership drift")
    if audit["episode_key"].duplicated().any():
        errors.append("extreme return path audit contains duplicate episodes")
    if set(audit["artifact_version"].astype(str)) != {ARTIFACT_VERSION}:
        errors.append("extreme return path audit version drift")
    for column in ("entry_open_raw_match", "exit_close_raw_match", "all_ohlc_raw_match"):
        if not _boolish(audit[column]).all():
            errors.append(f"extreme return path audit raw match failed: {column}")
    if _boolish(audit["impossible_return_flag"]).any():
        errors.append("a currently audited extreme trade is classified as impossible")
    if not audit["price_path_trading_rows"].eq(20).all():
        errors.append("extreme return path must contain exactly 20 entry-to-exit trading rows")
    if not audit["raw_source_rows_matched"].eq(audit["raw_source_rows_expected"]).all():
        errors.append("extreme return path raw row counts do not match")
    if not audit["market_limit_violation_count"].eq(0).all():
        errors.append("extreme return path contains an over-11-percent daily price movement")
    if set(audit["price_path_classification"].astype(str)) != {"plausible_extreme_continuous_gain"}:
        errors.append("extreme return path classification drift")

    source = pd.read_csv(SOURCE_DETAIL, dtype={"stock_id": str}, low_memory=False)
    rebuilt = build_extreme_return_path_audit(source).drop(columns=["generated_at"]).reset_index(drop=True)
    current = audit.drop(columns=["generated_at"]).reset_index(drop=True)
    try:
        pd.testing.assert_frame_equal(current, rebuilt, check_dtype=False, check_like=False)
    except AssertionError as exc:
        errors.append(f"extreme return path audit is not reproducible from source detail: {exc}")
    return errors


def main() -> int:
    errors = validate()
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1
    print(f"revenue extreme return path audit validation passed: rows=14 artifact_version={ARTIFACT_VERSION}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
