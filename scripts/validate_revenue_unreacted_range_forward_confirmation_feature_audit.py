from __future__ import annotations

import math

import pandas as pd

from revenue_unreacted_range_forward_confirmation_feature_audit import (
    ANALYSIS_BASES,
    ARTIFACT_ID,
    ARTIFACT_VERSION,
    DETAIL_CSV,
    DOCS_CSV,
    DOCS_FEATURE_CSV,
    DOCS_MD,
    DOCS_RETURN_REVIEW_CSV,
    EVENT_DETAIL_CSV,
    FEATURE_CSV,
    FINANCIAL_STATEMENT_SCOPE,
    HISTORY_CSV,
    HISTORY_FEATURE_CSV,
    HISTORY_RETURN_REVIEW_CSV,
    LATEST_CSV,
    LATEST_MD,
    MODEL_ID,
    PRIMARY_ANALYSIS_BASIS,
    OPERATION_RETURN_REVIEW_POLICY,
    OPERATION_RETURN_REVIEW_THRESHOLD_PCT,
    RETURN_REVIEW_COLUMNS,
    RETURN_REVIEW_CSV,
    RULE_SPECS,
    SENSITIVITY_ANALYSIS_BASIS,
    SOURCE_DETAIL_CSV,
)
from revenue_unreacted_range_source_first_condition_audit import (
    PRICE_RESOLUTION_CSV,
    PRIMARY_VARIANT_ID,
)


DETAIL_MAX_BYTES = 50_000_000

SUMMARY_REQUIRED = {
    "model_id",
    "artifact_id",
    "artifact_version",
    "analysis_basis",
    "rule_id",
    "rule_information_cutoff",
    "source_episode_count",
    "confirmed_episode_count",
    "no_confirmation_count",
    "strict_success_count",
    "neutral_count",
    "mature_failure_count",
    "outcome_right_censored_count",
    "classifiable_confirmation_count",
    "strict_success_rate_pct",
    "neutral_rate_pct",
    "mature_failure_rate_pct",
    "operation_mature_count",
    "operation_return_review_candidate_count",
    "avg_fixed_d20_return_excluding_review_candidates_sensitivity_pct",
    "median_fixed_d20_return_excluding_review_candidates_sensitivity_pct",
    "operation_return_review_policy",
    "same_stock_overlap_pair_count",
    "financial_statement_scope",
    "approved_for_daily",
    "production_change",
    "promotion_readiness",
}

DETAIL_REQUIRED = {
    "model_id",
    "artifact_id",
    "artifact_version",
    "episode_key",
    "stock_id",
    "episode_start_trade_date",
    "episode_start_source_date",
    "episode_end_date",
    "source_first_breakout_date",
    "source_first_breakout_outcome",
    "rule_id",
    "rule_information_cutoff",
    "rule_trigger_mode",
    "rule_condition_ids",
    "rule_next_day_mode",
    "selection_status",
    "trigger_date",
    "confirmation_date",
    "entry_date",
    "entry_open",
    "fixed_exit_date",
    "fixed_exit_close",
    "fixed_d20_return_pct",
    "outcome_status",
    "operation_mature",
    "operation_return_review_candidate_flag",
    "operation_return_review_status",
    "operation_return_review_policy",
    "anomaly_candidate_flag",
    "same_stock_non_overlap_applied",
    "first_match_policy",
    "entry_rule",
    "fixed_exit_rule",
    "approved_for_daily",
    "production_change",
}

EVENT_REQUIRED = {
    "model_id",
    "artifact_id",
    "artifact_version",
    "episode_key",
    "stock_id",
    "contrast_group",
    "trigger_date",
    "outcome_status",
    "next_day_close_gt_trigger_close",
    "volume_ratio_prev20",
    "ma60_gt_ma120",
    "obv_above_ma20",
    "kdj_bullish_not_extreme",
    "tdcc_high_thresholds_up",
    "market_regime",
    "revenue_lag_trading_days",
    "anomaly_candidate_flag",
    "approved_for_daily",
    "production_change",
}

FEATURE_REQUIRED = {
    "model_id",
    "artifact_id",
    "artifact_version",
    "analysis_basis",
    "row_type",
    "feature_id",
    "feature_family",
    "success_group_count",
    "failure_group_count",
    "contrast_scope",
    "sample_policy",
    "approved_for_daily",
    "production_change",
}


def _boolish(series: pd.Series) -> pd.Series:
    return series.astype(str).str.strip().str.lower().isin({"true", "1", "yes"})


def _number(value: object) -> float | None:
    number = pd.to_numeric(value, errors="coerce")
    return None if pd.isna(number) else float(number)


def _check_governance(name: str, frame: pd.DataFrame, errors: list[str]) -> None:
    if set(frame["model_id"].astype(str)) != {MODEL_ID}:
        errors.append(f"forward confirmation {name} model_id drift")
    if set(frame["artifact_id"].astype(str)) != {ARTIFACT_ID}:
        errors.append(f"forward confirmation {name} artifact_id drift")
    if set(frame["artifact_version"].astype(str)) != {ARTIFACT_VERSION}:
        errors.append(f"forward confirmation {name} artifact_version drift")
    if _boolish(frame["approved_for_daily"]).any():
        errors.append(f"forward confirmation {name} must remain research-only")
    if _boolish(frame["production_change"]).any():
        errors.append(f"forward confirmation {name} must not change production")


def validate() -> list[str]:
    errors: list[str] = []
    paths = (
        LATEST_CSV,
        DETAIL_CSV,
        EVENT_DETAIL_CSV,
        FEATURE_CSV,
        RETURN_REVIEW_CSV,
        LATEST_MD,
        HISTORY_CSV,
        HISTORY_FEATURE_CSV,
        HISTORY_RETURN_REVIEW_CSV,
        DOCS_CSV,
        DOCS_FEATURE_CSV,
        DOCS_RETURN_REVIEW_CSV,
        DOCS_MD,
        SOURCE_DETAIL_CSV,
        PRICE_RESOLUTION_CSV,
    )
    for path in paths:
        if not path.is_file():
            errors.append(f"forward confirmation artifact is missing: {path}")
    if errors:
        return errors

    if DETAIL_CSV.stat().st_size >= DETAIL_MAX_BYTES:
        errors.append("forward confirmation rule detail exceeds the Git-safe 50 MB policy")

    summary = pd.read_csv(LATEST_CSV, keep_default_na=False, low_memory=False)
    detail = pd.read_csv(
        DETAIL_CSV,
        dtype={
            "stock_id": str,
            "episode_start_trade_date": str,
            "episode_start_source_date": str,
            "episode_end_date": str,
            "source_first_breakout_date": str,
            "trigger_date": str,
            "confirmation_date": str,
            "entry_date": str,
            "fixed_exit_date": str,
        },
        keep_default_na=False,
        low_memory=False,
    )
    events = pd.read_csv(
        EVENT_DETAIL_CSV,
        dtype={"stock_id": str, "trigger_date": str},
        keep_default_na=False,
        low_memory=False,
    )
    feature = pd.read_csv(FEATURE_CSV, keep_default_na=False, low_memory=False)
    return_review = pd.read_csv(
        RETURN_REVIEW_CSV,
        dtype={"stock_id": str, "entry_date": str, "fixed_exit_date": str},
        keep_default_na=False,
        low_memory=False,
    )
    source = pd.read_csv(
        SOURCE_DETAIL_CSV,
        dtype={"stock_id": str, "first_breakout_date": str},
        keep_default_na=False,
        low_memory=False,
    )
    source = source.loc[source["condition_variant_id"].eq(PRIMARY_VARIANT_ID)].copy()
    price_resolutions = pd.read_csv(
        PRICE_RESOLUTION_CSV,
        dtype={"stock_id": str},
        keep_default_na=False,
    )
    if not price_resolutions["approved_scope"].eq(
        "revenue_unreacted_range_model_owned_research_only"
    ).all():
        errors.append("forward confirmation price resolution scope is not model-owned research only")

    for name, frame, required in (
        ("summary", summary, SUMMARY_REQUIRED),
        ("detail", detail, DETAIL_REQUIRED),
        ("event detail", events, EVENT_REQUIRED),
        ("feature contrast", feature, FEATURE_REQUIRED),
        ("operation return review", return_review, set(RETURN_REVIEW_COLUMNS)),
    ):
        missing = sorted(required - set(frame.columns))
        if missing:
            errors.append(f"forward confirmation {name} schema is missing columns: {missing}")
    if errors:
        return errors

    for name, frame in (
        ("summary", summary),
        ("detail", detail),
        ("event detail", events),
        ("feature contrast", feature),
        ("operation return review", return_review),
    ):
        _check_governance(name, frame, errors)

    if "volume_ratio_prev20" in detail.columns or "k_value" in detail.columns:
        errors.append("forward confirmation detail repeats normalized event features across rules")
    if detail.duplicated(["episode_key", "rule_id"]).any():
        errors.append("forward confirmation detail repeats an episode/rule pair")
    if events.duplicated(["episode_key", "contrast_group"]).any():
        errors.append("forward confirmation event detail repeats an episode/group pair")
    if return_review.duplicated(["stock_id", "entry_date", "fixed_exit_date"]).any():
        errors.append("forward confirmation operation return review repeats an operation path")
    review_detail = detail.loc[
        _boolish(detail["operation_return_review_candidate_flag"])
    ].copy()
    expected_review_keys = set(
        zip(review_detail["stock_id"], review_detail["entry_date"], review_detail["fixed_exit_date"])
    )
    observed_review_keys = set(
        zip(return_review["stock_id"], return_review["entry_date"], return_review["fixed_exit_date"])
    )
    if expected_review_keys != observed_review_keys:
        errors.append("forward confirmation operation return review coverage drift")
    review_returns = pd.to_numeric(return_review["fixed_d20_return_pct"], errors="coerce")
    if review_returns.isna().any() or not review_returns.abs().ge(
        OPERATION_RETURN_REVIEW_THRESHOLD_PCT
    ).all():
        errors.append("forward confirmation operation return review threshold drift")
    replayed_review_returns = pd.to_numeric(
        return_review["replayed_fixed_d20_return_pct"], errors="coerce"
    )
    if replayed_review_returns.isna().any() or not (
        replayed_review_returns - review_returns
    ).abs().le(0.0001).all():
        errors.append("forward confirmation operation return review replay drift")
    review_thresholds = pd.to_numeric(
        return_review["review_trigger_threshold_pct"], errors="coerce"
    )
    if review_thresholds.isna().any() or not review_thresholds.eq(
        OPERATION_RETURN_REVIEW_THRESHOLD_PCT
    ).all():
        errors.append("forward confirmation operation return review trigger disclosure drift")
    if not _boolish(return_review["included_in_primary_metrics"]).all():
        errors.append("forward confirmation operation return candidates must remain in primary metrics")
    if not _boolish(return_review["excluded_in_review_candidate_sensitivity"]).all():
        errors.append("forward confirmation operation return review sensitivity flag drift")
    if not return_review["review_disposition"].eq(
        "unresolved_review_candidate_retained_in_primary_not_classified_as_anomaly"
    ).all():
        errors.append("forward confirmation operation return candidates received an unapproved disposition")

    expected_rules = {rule.rule_id for rule in RULE_SPECS}
    expected_summary = {(basis, rule) for basis in ANALYSIS_BASES for rule in expected_rules}
    observed_summary = set(zip(summary["analysis_basis"], summary["rule_id"]))
    if observed_summary != expected_summary:
        errors.append("forward confirmation summary rule/basis coverage drift")
    if set(detail["rule_id"]) != expected_rules:
        errors.append("forward confirmation detail rule coverage drift")
    if set(detail["episode_key"]) != set(source["episode_key"]):
        errors.append("forward confirmation detail source episode coverage drift")
    expected_detail_rows = len(source) * len(RULE_SPECS)
    if len(detail) != expected_detail_rows:
        errors.append(
            "forward confirmation detail does not contain exactly one row per source episode/rule"
        )
    per_episode = detail.groupby("episode_key")["rule_id"].nunique()
    if not per_episode.eq(len(RULE_SPECS)).all():
        errors.append("forward confirmation episode rule coverage is incomplete")

    if not _boolish(detail["same_stock_non_overlap_applied"]).all():
        errors.append("forward confirmation detail does not preserve same-stock non-overlap")
    if set(detail["first_match_policy"]) != {
        "first_rule_match_only_no_retrospective_reselection"
    }:
        errors.append("forward confirmation first-match policy drift")
    if set(detail["entry_rule"]) != {"confirmation_close_then_next_trading_day_open"}:
        errors.append("forward confirmation entry timing drift")
    if set(detail["fixed_exit_rule"]) != {
        "confirmation_relative_d20_close_research_only"
    }:
        errors.append("forward confirmation fixed exit timing drift")

    source_reference = detail.loc[
        detail["rule_id"].eq("source_first_close_above_prev20_reference")
    ].set_index("episode_key")
    source_by_key = source.set_index("episode_key")
    for episode_key, source_row in source_by_key.iterrows():
        observed = source_reference.loc[episode_key]
        source_date = str(source_row["first_breakout_date"])
        if source_date:
            if str(observed["trigger_date"]) != source_date:
                errors.append(f"forward confirmation baseline first breakout date drift: {episode_key}")
            if str(observed["outcome_status"]) != str(source_row["first_breakout_outcome"]):
                errors.append(f"forward confirmation baseline first breakout outcome drift: {episode_key}")
        elif str(observed["trigger_date"]):
            errors.append(f"forward confirmation baseline invents a source breakout: {episode_key}")

    for row in summary.itertuples(index=False):
        part = detail.loc[detail["rule_id"].eq(row.rule_id)].copy()
        if row.analysis_basis == SENSITIVITY_ANALYSIS_BASIS:
            part = part.loc[~_boolish(part["anomaly_candidate_flag"])]
        confirmed = part["selection_status"].eq("confirmed_first_rule_match")
        success = confirmed & part["outcome_status"].eq("strict_success")
        failure = confirmed & part["outcome_status"].eq("mature_failure")
        censored = confirmed & part["outcome_status"].eq("right_censored_before_d20")
        classifiable = success | failure
        operation_mature = confirmed & _boolish(part["operation_mature"])
        operation_return_review = (
            operation_mature
            & _boolish(part["operation_return_review_candidate_flag"])
        )
        if int(row.source_episode_count) != len(part):
            errors.append(f"forward confirmation source count drift: {row.analysis_basis}/{row.rule_id}")
        if int(row.confirmed_episode_count) != int(confirmed.sum()):
            errors.append(f"forward confirmation selected count drift: {row.analysis_basis}/{row.rule_id}")
        if int(row.no_confirmation_count) + int(row.confirmed_episode_count) != len(part):
            errors.append(f"forward confirmation selection partition drift: {row.analysis_basis}/{row.rule_id}")
        if (
            int(row.strict_success_count) != int(success.sum())
            or int(row.mature_failure_count) != int(failure.sum())
            or int(row.outcome_right_censored_count) != int(censored.sum())
            or int(row.classifiable_confirmation_count) != int(classifiable.sum())
        ):
            errors.append(f"forward confirmation outcome count drift: {row.analysis_basis}/{row.rule_id}")
        if int(row.neutral_count) != 0:
            errors.append(f"forward confirmation silently introduced neutral rows: {row.rule_id}")
        if int(row.operation_return_review_candidate_count) != int(operation_return_review.sum()):
            errors.append(
                f"forward confirmation operation return review count drift: {row.analysis_basis}/{row.rule_id}"
            )
        if str(row.operation_return_review_policy) != OPERATION_RETURN_REVIEW_POLICY:
            errors.append(f"forward confirmation operation return review policy drift: {row.rule_id}")
        without_review = operation_mature & ~operation_return_review
        if int(without_review.sum()):
            without_review_returns = pd.to_numeric(
                part.loc[without_review, "fixed_d20_return_pct"], errors="coerce"
            )
            expected_review_mean = round(float(without_review_returns.mean()), 4)
            expected_review_median = round(float(without_review_returns.median()), 4)
            if not math.isclose(
                float(row.avg_fixed_d20_return_excluding_review_candidates_sensitivity_pct),
                expected_review_mean,
                abs_tol=1e-9,
            ):
                errors.append(
                    f"forward confirmation operation return review mean drift: {row.analysis_basis}/{row.rule_id}"
                )
            if not math.isclose(
                float(row.median_fixed_d20_return_excluding_review_candidates_sensitivity_pct),
                expected_review_median,
                abs_tol=1e-9,
            ):
                errors.append(
                    f"forward confirmation operation return review median drift: {row.analysis_basis}/{row.rule_id}"
                )
        if int(classifiable.sum()):
            expected_win = round(int(success.sum()) / int(classifiable.sum()) * 100.0, 4)
            expected_loss = round(int(failure.sum()) / int(classifiable.sum()) * 100.0, 4)
            if not math.isclose(float(row.strict_success_rate_pct), expected_win, abs_tol=1e-9):
                errors.append(f"forward confirmation win-rate drift: {row.analysis_basis}/{row.rule_id}")
            if not math.isclose(float(row.mature_failure_rate_pct), expected_loss, abs_tol=1e-9):
                errors.append(f"forward confirmation failure-rate drift: {row.analysis_basis}/{row.rule_id}")
        if int(row.same_stock_overlap_pair_count) != 0:
            errors.append(f"forward confirmation source overlap remains: {row.analysis_basis}/{row.rule_id}")
        if str(row.financial_statement_scope) != FINANCIAL_STATEMENT_SCOPE:
            errors.append(f"forward confirmation financial statement scope drift: {row.rule_id}")

    mature = detail.loc[_boolish(detail["operation_mature"])].copy()
    if mature.empty:
        errors.append("forward confirmation detail has no mature next-open operations")
    else:
        if not mature["entry_date"].gt(mature["confirmation_date"]).all():
            errors.append("forward confirmation entry is not after confirmation close")
        if not mature["fixed_exit_date"].gt(mature["entry_date"]).all():
            errors.append("forward confirmation fixed exit is not after next-open entry")
        if pd.to_numeric(mature["entry_open"], errors="coerce").isna().any():
            errors.append("forward confirmation mature operations contain invalid next-open prices")
        if pd.to_numeric(mature["fixed_exit_close"], errors="coerce").isna().any():
            errors.append("forward confirmation mature operations contain invalid fixed close exits")

    expected_groups = {"strict_success_launch_event", "first_mature_failure_event"}
    if not set(events["contrast_group"]) <= expected_groups:
        errors.append("forward confirmation event contrast contains an unknown group")
    expected_success_events = int(source["episode_status"].eq("launch_within_active_horizon").sum())
    expected_failure_events = int(source["first_breakout_outcome"].eq("mature_failure").sum())
    if int(events["contrast_group"].eq("strict_success_launch_event").sum()) != expected_success_events:
        errors.append("forward confirmation feature contrast omits source launch events")
    if int(events["contrast_group"].eq("first_mature_failure_event").sum()) != expected_failure_events:
        errors.append("forward confirmation feature contrast omits source first mature failures")
    known_4916 = events.loc[events["stock_id"].eq("4916")]
    known_1303 = events.loc[events["stock_id"].eq("1303")]
    expected_4916 = {
        ("first_mature_failure_event", "20251209", "mature_failure"),
        ("strict_success_launch_event", "20260518", "strict_success"),
    }
    observed_4916 = set(
        zip(known_4916["contrast_group"], known_4916["trigger_date"], known_4916["outcome_status"])
    )
    if not expected_4916 <= observed_4916:
        errors.append("forward confirmation 4916 success/failure event coverage drift")
    if (
        "strict_success_launch_event",
        "20260527",
        "strict_success",
    ) not in set(zip(known_1303["contrast_group"], known_1303["trigger_date"], known_1303["outcome_status"])):
        errors.append("forward confirmation 1303 success event coverage drift")

    if set(feature["analysis_basis"]) != set(ANALYSIS_BASES):
        errors.append("forward confirmation feature analysis-basis coverage drift")
    if set(feature["row_type"]) != {"binary_feature", "numeric_feature"}:
        errors.append("forward confirmation feature row-type coverage drift")
    for basis in ANALYSIS_BASES:
        part = feature.loc[feature["analysis_basis"].eq(basis)]
        if part["feature_id"].duplicated().any():
            errors.append(f"forward confirmation feature rows repeat within basis: {basis}")

    if len(summary.loc[summary["analysis_basis"].eq(PRIMARY_ANALYSIS_BASIS)]) != len(RULE_SPECS):
        errors.append("forward confirmation primary rule matrix is incomplete")
    if len(summary.loc[summary["analysis_basis"].eq(SENSITIVITY_ANALYSIS_BASIS)]) != len(RULE_SPECS):
        errors.append("forward confirmation anomaly sensitivity matrix is incomplete")

    if LATEST_CSV.read_bytes() != HISTORY_CSV.read_bytes() or LATEST_CSV.read_bytes() != DOCS_CSV.read_bytes():
        errors.append("forward confirmation summary mirrors drift")
    if FEATURE_CSV.read_bytes() != HISTORY_FEATURE_CSV.read_bytes() or FEATURE_CSV.read_bytes() != DOCS_FEATURE_CSV.read_bytes():
        errors.append("forward confirmation feature mirrors drift")
    if RETURN_REVIEW_CSV.read_bytes() != HISTORY_RETURN_REVIEW_CSV.read_bytes() or RETURN_REVIEW_CSV.read_bytes() != DOCS_RETURN_REVIEW_CSV.read_bytes():
        errors.append("forward confirmation operation return review mirrors drift")
    if LATEST_MD.read_bytes() != DOCS_MD.read_bytes():
        errors.append("forward confirmation markdown mirror drift")
    markdown = LATEST_MD.read_text(encoding="utf-8")
    for token in (
        "前向確認與特徵稽核",
        "後來成功不得回頭取代較早已確認的失敗",
        "成功組使用 source 標記的真正發動日",
        "下一交易日開盤進場",
        "right-censored，不得算失敗",
        "EPS、毛利率、營益率、營業利益、業外與淨利均未納入",
        "只會觸發 review candidate",
    ):
        if token not in markdown:
            errors.append(f"forward confirmation markdown omits required rule: {token}")
    return errors


def main() -> int:
    errors = validate()
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1
    print("revenue_unreacted_range forward confirmation feature audit validation passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
