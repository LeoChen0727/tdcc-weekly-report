from __future__ import annotations

from io import StringIO

import pandas as pd

from revenue_unreacted_range_lag_strength_matrix import (
    ARTIFACT_VERSION,
    DETAIL_COLUMNS,
    DETAIL_CSV,
    LATEST_CSV,
    SOURCE_DETAIL,
    SUMMARY_COLUMNS,
    build_lag_strength_matrix,
)


DETAIL_DTYPES = {
        "episode_key": str,
        "stock_id": str,
        "source_monthly_revenue_period": str,
        "source_monthly_revenue_source_table_date": str,
        "signal_date": str,
        "confirmation_date": str,
        "entry_date": str,
        "exit_date": str,
        "strict_30_20_streak_start_period": str,
        "strict_30_20_streak_start_source_date": str,
}
SUMMARY_DTYPES = {"condition_test_id": str}
EXPECTED_AVAILABILITY_SEMANTICS = (
    "conservative_next_month_17th_or_first_official_snapshot_not_exact_company_release_timestamp"
)


def _read(path, *, detail: bool = False) -> pd.DataFrame:
    return pd.read_csv(
        path,
        dtype=DETAIL_DTYPES if detail else SUMMARY_DTYPES,
        keep_default_na=False,
        low_memory=False,
    )


def _serialized(frame: pd.DataFrame, *, detail: bool = False) -> pd.DataFrame:
    return pd.read_csv(
        StringIO(frame.to_csv(index=False)),
        dtype=DETAIL_DTYPES if detail else SUMMARY_DTYPES,
        keep_default_na=False,
        low_memory=False,
    )


def validate() -> list[str]:
    errors: list[str] = []
    if not LATEST_CSV.is_file() or not DETAIL_CSV.is_file():
        return ["lag strength matrix summary/detail artifact is missing"]
    summary = _read(LATEST_CSV)
    detail = _read(DETAIL_CSV, detail=True)
    if list(summary.columns) != SUMMARY_COLUMNS:
        errors.append("lag strength matrix summary schema drift")
    if list(detail.columns) != DETAIL_COLUMNS:
        errors.append("lag strength matrix detail schema drift")
    if errors:
        return errors
    if set(summary["artifact_version"].astype(str)) != {ARTIFACT_VERSION}:
        errors.append("lag strength matrix summary version drift")
    if set(detail["artifact_version"].astype(str)) != {ARTIFACT_VERSION}:
        errors.append("lag strength matrix detail version drift")
    source = pd.read_csv(SOURCE_DETAIL, dtype={"stock_id": str}, low_memory=False)
    source_mask = (
        source["decision_basis"].astype(str).str.lower().isin({"true", "1", "yes"})
        & ~source["sensitivity_basis"].astype(str).str.lower().isin({"true", "1", "yes"})
        & source["feature_time_basis"].astype(str).eq("signal_date_close")
    )
    expected_source_count = len(source.loc[source_mask].drop_duplicates("episode_key"))
    if len(detail) != expected_source_count:
        errors.append(
            f"lag strength detail source count drift: expected={expected_source_count} actual={len(detail)}"
        )
    if detail["episode_key"].duplicated().any():
        errors.append("lag strength detail contains duplicate episodes")
    repeats = detail.groupby(["stock_id", "source_monthly_revenue_period"]).size()
    if int((repeats - 1).clip(lower=0).sum()) != 0:
        errors.append("lag strength detail repeats same-stock revenue periods")
    if pd.to_numeric(detail["source_to_signal_trading_days"], errors="coerce").lt(0).any():
        errors.append("lag strength detail contains negative trading-day lag")
    if detail["current_revenue_lag_bucket"].astype(str).eq("").any():
        errors.append("lag strength detail has unbucketed current revenue lags")
    if set(detail["availability_date_semantics"].astype(str)) != {EXPECTED_AVAILABILITY_SEMANTICS}:
        errors.append("lag strength detail availability-date semantics drift")
    baseline = summary[summary["condition_test_id"].eq("all_confirmed_non_overlap")]
    if len(baseline) != 1 or int(baseline.iloc[0]["accepted_trade_count"]) != len(detail):
        errors.append("lag strength baseline count drift")
    candidate_flags = detail["abs_ge80_anomaly_candidate_flag"].astype(str).str.lower().isin(
        {"true", "1", "yes"}
    )
    source_candidate_flags = detail[
        "source_revenue_or_price_anomaly_candidate_flag"
    ].astype(str).str.lower().isin({"true", "1", "yes"})
    if len(baseline) == 1:
        if int(baseline.iloc[0]["abs_ge80_anomaly_candidate_count"]) != int(candidate_flags.sum()):
            errors.append("lag strength baseline return-candidate count drift")
        if int(baseline.iloc[0]["source_anomaly_candidate_count"]) != int(source_candidate_flags.sum()):
            errors.append("lag strength baseline source-candidate count drift")
    if set(summary["promotion_readiness"].astype(str)) != {
        "blocked_pending_root_cause_anomaly_candidate_review"
    }:
        errors.append("lag strength matrix must remain blocked pending root-cause review")
    required_families = {
        "baseline",
        "current_revenue_trading_day_lag",
        "absolute_strength",
        "acceleration",
        "persistence",
        "lag_x_strength",
        "strict_strength_streak_start_lag",
    }
    if set(summary["matrix_family"]) != required_families:
        errors.append("lag strength matrix family coverage drift")
    for row in summary.itertuples(index=False):
        count = int(row.accepted_trade_count)
        if count:
            total = float(row.win_rate_pct) + float(row.neutral_rate_pct) + float(row.failure_rate_pct)
            if abs(total - 100.0) > 0.02:
                errors.append(f"lag strength outcome rates do not sum to 100: {row.condition_test_id}")
        if int(row.same_stock_overlap_pair_count) != 0 or int(row.same_stock_revenue_period_repeat_count) != 0:
            errors.append(f"lag strength non-overlap contract failed: {row.condition_test_id}")
        if (
            int(row.abs_ge80_anomaly_candidate_count) > 0
            or int(row.source_anomaly_candidate_count) > 0
        ) and row.interpretation_status != (
            "blocked_pending_root_cause_anomaly_candidate_review"
        ):
            errors.append(
                f"lag strength row with unresolved candidates is not blocked: {row.condition_test_id}"
            )
    rebuilt_summary, rebuilt_detail = build_lag_strength_matrix(source)
    rebuilt_summary = _serialized(rebuilt_summary)
    rebuilt_detail = _serialized(rebuilt_detail, detail=True)
    current_summary = summary.drop(columns=["generated_at"]).reset_index(drop=True)
    current_detail = detail.drop(columns=["generated_at"]).reset_index(drop=True)
    rebuilt_summary = rebuilt_summary.drop(columns=["generated_at"]).reset_index(drop=True)
    rebuilt_detail = rebuilt_detail.drop(columns=["generated_at"]).reset_index(drop=True)
    try:
        pd.testing.assert_frame_equal(current_summary, rebuilt_summary, check_dtype=False)
    except AssertionError as exc:
        errors.append(f"lag strength summary is not reproducible: {exc}")
    try:
        pd.testing.assert_frame_equal(current_detail, rebuilt_detail, check_dtype=False)
    except AssertionError as exc:
        errors.append(f"lag strength detail is not reproducible: {exc}")
    return errors


def main() -> int:
    errors = validate()
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1
    summary = _read(LATEST_CSV)
    baseline = summary[summary["condition_test_id"].eq("all_confirmed_non_overlap")].iloc[0]
    print(
        "revenue lag strength matrix validation passed: "
        f"source_trades={int(baseline['accepted_trade_count'])} "
        f"return_candidates={int(baseline['abs_ge80_anomaly_candidate_count'])} "
        f"source_candidates={int(baseline['source_anomaly_candidate_count'])}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
