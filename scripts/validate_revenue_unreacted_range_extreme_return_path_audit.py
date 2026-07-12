from __future__ import annotations

import pandas as pd

from revenue_unreacted_range_extreme_return_path_audit import (
    ARTIFACT_VERSION,
    COLUMNS,
    LATEST_CSV,
    RAW_PRICE_SOURCE_HASH_BASIS,
    build_extreme_return_path_audit,
)


SOURCE_DETAIL = "output/latest/research_backtest/revenue_unreacted_range_fixed_confirmation_feature_contrast_audit_detail_latest.csv"
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
    source = pd.read_csv(SOURCE_DETAIL, dtype={"stock_id": str}, low_memory=False)
    source_returns = pd.to_numeric(source["realized_return_pct"], errors="coerce")
    source_target = source[
        _boolish(source["decision_basis"])
        & ~_boolish(source["sensitivity_basis"])
        & source["feature_time_basis"].astype(str).eq("signal_date_close")
        & source_returns.abs().ge(80.0)
    ].drop_duplicates("episode_key")
    if len(audit) != len(source_target):
        errors.append(
            f"extreme return path audit source membership count drift: "
            f"expected={len(source_target)} actual={len(audit)}"
        )
    if set(audit["episode_key"].astype(str)) != set(source_target["episode_key"].astype(str)):
        errors.append("extreme return path audit episode membership drift")
    if audit["episode_key"].duplicated().any():
        errors.append("extreme return path audit contains duplicate episodes")
    if set(audit["artifact_version"].astype(str)) != {ARTIFACT_VERSION}:
        errors.append("extreme return path audit version drift")
    if set(audit["raw_price_source_sha256_basis"].astype(str)) != {RAW_PRICE_SOURCE_HASH_BASIS}:
        errors.append("extreme return path raw source hash basis drift")
    if not audit["raw_price_source_sha256"].astype(str).str.fullmatch(r"[0-9a-f]{64}").all():
        errors.append("extreme return path raw source hash is malformed")
    for column in ("entry_open_raw_match", "exit_close_raw_match", "all_ohlc_raw_match"):
        if not _boolish(audit[column]).all():
            errors.append(f"extreme return path audit raw match failed: {column}")
    if _boolish(audit["impossible_return_flag"]).any():
        errors.append("a currently audited anomaly candidate has a repo price-path mismatch")
    if not audit["price_path_trading_rows"].eq(20).all():
        errors.append("extreme return path must contain exactly 20 entry-to-exit trading rows")
    if not audit["raw_source_rows_matched"].eq(audit["raw_source_rows_expected"]).all():
        errors.append("extreme return path raw row counts do not match")
    if not audit["market_limit_violation_count"].eq(0).all():
        errors.append("extreme return path contains an over-11-percent daily price movement")
    if set(audit["statistical_trigger_status"].astype(str)) != {"anomaly_candidate"}:
        errors.append("return threshold must create anomaly candidates only")
    if set(audit["price_path_classification"].astype(str)) != {
        "candidate_continuous_price_path_repo_source_matched"
    }:
        errors.append("anomaly candidate price-path classification drift")
    if set(audit["root_cause_verification_status"].astype(str)) != {
        "partial_root_checks_incomplete"
    }:
        errors.append("anomaly candidate root-cause status drift")
    if set(audit["final_disposition"].astype(str)) != {"unresolved_anomaly_candidate"}:
        errors.append("anomaly candidates received a premature final disposition")
    if audit["root_cause_checks_missing"].astype(str).eq("").any():
        errors.append("anomaly candidates must disclose missing bottom-level checks")
    if set(audit["primary_metric_handling"].astype(str)) != {
        "retain_observed_candidate_and_block_promotion_until_resolved"
    }:
        errors.append("anomaly candidate primary metric handling drift")
    if set(audit["candidate_threshold_sensitivity_handling"].astype(str)) != {
        "threshold_sensitivity_only_not_anomaly_disposition"
    }:
        errors.append("anomaly candidate threshold sensitivity is mislabeled")

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
    print(
        "revenue anomaly candidate root-cause audit validation passed: "
        f"rows={len(pd.read_csv(LATEST_CSV))} artifact_version={ARTIFACT_VERSION} "
        "final_disposition=unresolved"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
