from __future__ import annotations

import pandas as pd

from revenue_unreacted_range_launch_timing_feature_audit import (
    ALL_LINEAGE_COLUMNS,
    ANALYSIS_BASES,
    ARTIFACT_VERSION,
    DETAIL_COLUMNS,
    DETAIL_CSV,
    FEATURE_COLUMNS,
    FEATURE_CSV,
    FINANCIAL_STATEMENT_SCOPE,
    FULL_OBSERVATION_NON_OVERLAP_DAYS,
    HORIZONS,
    LATEST_CSV,
    LATEST_MD,
    EXPECTED_SOURCE_ARTIFACT_ID,
    EXPECTED_SOURCE_ARTIFACT_VERSION,
    OUTCOME_SPECS,
    PRIMARY_ANALYSIS_BASIS,
    PRIMARY_OUTCOME_ID,
    PRIMARY_TRIGGER_ID,
    PRICE_COMPARABILITY_RESOLUTION_CSV,
    SENSITIVITY_ANALYSIS_BASIS,
    SIX_MONTH_HORIZON_DAYS,
    SOURCE_DETAIL,
    SOURCE_SNAPSHOT_CUTOFF_DATE,
    SUMMARY_COLUMNS,
    TRIGGER_SPECS,
    _assert_source_detail_lineage,
    _source_cohort,
)


DETAIL_DTYPES = {
    "episode_key": str,
    "stock_id": str,
    "source_monthly_revenue_period": str,
    "source_monthly_revenue_source_table_date": str,
    "source_trade_date": str,
    "signal_date": str,
    "first_trigger_date": str,
    "launch_date": str,
}

def _read(path, *, detail: bool = False) -> pd.DataFrame:
    return pd.read_csv(
        path,
        dtype=DETAIL_DTYPES if detail else None,
        keep_default_na=False,
        low_memory=False,
    )


def _boolish(series: pd.Series) -> pd.Series:
    return series.astype(str).str.strip().str.lower().isin({"true", "1", "yes"})


def _source_lineage_errors(
    source: pd.DataFrame,
    *,
    expected_runtime_lineage: dict[str, object] | None = None,
) -> list[str]:
    required = {
        "artifact_id",
        "artifact_version",
        *ALL_LINEAGE_COLUMNS[:-2],
    }
    missing = sorted(required - set(source.columns))
    if missing:
        return [f"launch timing source lineage is missing columns: {missing}"]
    errors: list[str] = []
    if set(source["artifact_id"].astype(str)) != {EXPECTED_SOURCE_ARTIFACT_ID}:
        errors.append("launch timing source artifact id drift")
    if set(source["artifact_version"].astype(str)) != {
        EXPECTED_SOURCE_ARTIFACT_VERSION
    }:
        errors.append("launch timing source artifact version drift")
    for column in ALL_LINEAGE_COLUMNS[:-2]:
        values = set(source[column].astype(str).str.strip().str.lower())
        if len(values) != 1:
            errors.append(f"launch timing source runtime lineage is not constant: {column}")
            continue
        value = next(iter(values))
        if column.endswith("sha256") and (
            len(value) != 64
            or any(character not in "0123456789abcdef" for character in value)
        ):
            errors.append(
                f"launch timing source runtime lineage is not canonical SHA-256: {column}"
            )
            continue
        if (
            expected_runtime_lineage is not None
            and value != str(expected_runtime_lineage[column]).strip().lower()
        ):
            errors.append(f"launch timing source current input lineage drift: {column}")
    return errors


def validate() -> list[str]:
    errors: list[str] = []
    for path in (LATEST_CSV, DETAIL_CSV, FEATURE_CSV, SOURCE_DETAIL):
        if not path.is_file():
            errors.append(f"launch timing feature artifact is missing: {path}")
    if errors:
        return errors
    if not LATEST_MD.is_file():
        return [f"launch timing markdown artifact is missing: {LATEST_MD}"]

    source = pd.read_csv(
        SOURCE_DETAIL,
        dtype={
            "stock_id": str,
            "source_monthly_revenue_source_table_date": str,
            "signal_date": str,
            "confirmation_date": str,
            "entry_date": str,
            "exit_date": str,
        },
        keep_default_na=False,
        low_memory=False,
    )
    try:
        expected_runtime_lineage = _assert_source_detail_lineage(source)
    except (RuntimeError, ValueError, KeyError, pd.errors.ParserError) as exc:
        return [f"launch timing cutoff source lineage cannot be verified: {exc}"]

    try:
        resolution = pd.read_csv(
            PRICE_COMPARABILITY_RESOLUTION_CSV,
            dtype={
                "resolution_id": str,
                "model_id": str,
                "stock_id": str,
                "pre_event_last_trade_date": str,
                "suspension_start_date": str,
                "suspension_end_date": str,
                "resume_date": str,
            },
            keep_default_na=False,
        )
    except Exception as exc:
        return [f"launch timing price comparability resolution cannot be read: {exc}"]
    force = resolution.loc[
        resolution["resolution_id"].eq("3593_20251222_loss_offset_capital_reduction")
    ]
    if len(force) != 1:
        errors.append("3593 capital-reduction price comparability resolution is missing")
    else:
        row = force.iloc[0]
        ratio = pd.to_numeric(row["exchange_ratio"], errors="coerce")
        pre_close = pd.to_numeric(row["pre_event_close"], errors="coerce")
        reference = pd.to_numeric(row["resume_reference_price"], errors="coerce")
        if not pd.notna(ratio) or abs(pre_close / ratio - reference) > 0.005:
            errors.append("3593 capital-reduction adjustment math drift")
        if row["authority"] != "TWSE" or not row["authority_source_url"].startswith(
            "https://www.twse.com.tw/"
        ):
            errors.append("3593 capital-reduction resolution lacks official TWSE evidence")
    avision = resolution.loc[
        resolution["resolution_id"].eq("2380_20260629_loss_offset_capital_reduction")
    ]
    if len(avision) != 1:
        errors.append("2380 capital-reduction price comparability resolution is missing")
    else:
        row = avision.iloc[0]
        ratio = pd.to_numeric(row["exchange_ratio"], errors="coerce")
        pre_close = pd.to_numeric(row["pre_event_close"], errors="coerce")
        reference = pd.to_numeric(row["resume_reference_price"], errors="coerce")
        if not pd.notna(ratio) or abs(pre_close / ratio - reference) > 0.005:
            errors.append("2380 capital-reduction adjustment math drift")
        if (
            row["pre_event_last_trade_date"] != "20260616"
            or row["suspension_start_date"] != "20260617"
            or row["resume_date"] != "20260629"
        ):
            errors.append("2380 capital-reduction lifecycle dates drift")
        if row["authority"] != "TWSE" or not row["authority_source_url"].startswith(
            "https://www.twse.com.tw/"
        ):
            errors.append("2380 capital-reduction resolution lacks official TWSE evidence")

    summary = _read(LATEST_CSV)
    detail = _read(DETAIL_CSV, detail=True)
    feature = _read(FEATURE_CSV)
    markdown = LATEST_MD.read_text(encoding="utf-8")
    if list(summary.columns) != SUMMARY_COLUMNS:
        errors.append("launch timing summary schema drift")
    if list(detail.columns) != DETAIL_COLUMNS:
        errors.append("launch timing detail schema drift")
    if list(feature.columns) != FEATURE_COLUMNS:
        errors.append("launch timing feature contrast schema drift")
    if errors:
        return errors

    if set(detail["observation_cutoff_date"].astype(str)) != {
        SOURCE_SNAPSHOT_CUTOFF_DATE
    }:
        errors.append("launch timing observation cutoff drift")
    for column in (
        "source_monthly_revenue_source_table_date",
        "source_trade_date",
        "signal_date",
        "first_trigger_date",
        "launch_date",
        "observation_last_trade_date",
    ):
        values = detail[column].astype(str).str.strip()
        if values.loc[values.ne("")].gt(SOURCE_SNAPSHOT_CUTOFF_DATE).any():
            errors.append(f"launch timing {column} exceeds cutoff")
    accepted_last_dates = detail.loc[
        detail["observation_selection_status"].eq("accepted"),
        "observation_last_trade_date",
    ].astype(str)
    if accepted_last_dates.eq("").any():
        errors.append("launch timing accepted observation omits last trade date")
    eligible_resolution_ids = set(
        resolution.loc[
            resolution["resume_date"].astype(str).le(SOURCE_SNAPSHOT_CUTOFF_DATE),
            "resolution_id",
        ].astype(str)
    )
    used_resolution_ids = {
        item
        for value in detail["observation_price_comparability_resolution_ids"].astype(str)
        for item in value.split(";")
        if item
    }
    if not used_resolution_ids <= eligible_resolution_ids:
        errors.append("launch timing uses a post-cutoff price resolution")

    canonical_markdown = summary.loc[
        summary["analysis_basis"].eq(PRIMARY_ANALYSIS_BASIS)
        & summary["trigger_id"].eq(PRIMARY_TRIGGER_ID)
        & summary["outcome_definition_id"].eq(PRIMARY_OUTCOME_ID)
    ].copy()
    six_month_markdown = canonical_markdown.loc[
        pd.to_numeric(canonical_markdown["horizon_trading_days"], errors="coerce").eq(
            SIX_MONTH_HORIZON_DAYS
        )
    ].iloc[0]
    full_markdown = canonical_markdown.loc[
        pd.to_numeric(canonical_markdown["horizon_trading_days"], errors="coerce").eq(max(HORIZONS))
    ].iloc[0]
    required_markdown_tokens = (
        "主要嚴格發動定義要求 D+15 前收盤達 +20%",
        f"六個月內觀察到 {int(six_month_markdown['launch_count'])}/{int(full_markdown['launch_count'])} 筆已觀察發動",
        "252 日列的 100% 不代表全部股票最終都會發動",
        f"{int(full_markdown['right_censored_count'])} 筆右設限",
    )
    for token in required_markdown_tokens:
        if token not in markdown:
            errors.append(f"launch timing markdown omits required interpretation: {token}")

    for name, frame in (("summary", summary), ("detail", detail), ("feature", feature)):
        if set(frame["artifact_version"].astype(str)) != {ARTIFACT_VERSION}:
            errors.append(f"launch timing {name} version drift")
        if _boolish(frame["approved_for_daily"]).any():
            errors.append(f"launch timing {name} must remain research-only")
        if _boolish(frame["production_change"]).any():
            errors.append(f"launch timing {name} must not change production")
        for column, expected in expected_runtime_lineage.items():
            expected_text = str(expected).strip().lower()
            if set(frame[column].astype(str).str.strip().str.lower()) != {
                expected_text
            }:
                errors.append(f"launch timing {name} runtime lineage drift: {column}")

    expected_combinations = len(ANALYSIS_BASES) * len(TRIGGER_SPECS) * len(OUTCOME_SPECS) * len(HORIZONS)
    if len(summary) != expected_combinations:
        errors.append(
            f"launch timing summary combination count drift: expected={expected_combinations} actual={len(summary)}"
        )
    if set(summary["analysis_basis"].astype(str)) != set(ANALYSIS_BASES):
        errors.append("launch timing summary analysis basis drift")
    if set(pd.to_numeric(summary["horizon_trading_days"], errors="coerce")) != set(HORIZONS):
        errors.append("launch timing summary horizon coverage drift")
    if set(summary["trigger_id"].astype(str)) != {str(row["trigger_id"]) for row in TRIGGER_SPECS}:
        errors.append("launch timing trigger coverage drift")
    if set(summary["outcome_definition_id"].astype(str)) != {
        str(row["outcome_definition_id"]) for row in OUTCOME_SPECS
    }:
        errors.append("launch timing outcome definition coverage drift")

    errors.extend(
        _source_lineage_errors(
            source,
            expected_runtime_lineage=expected_runtime_lineage,
        )
    )
    expected_source_counts = {
        basis: len(_source_cohort(source, basis))
        for basis in ANALYSIS_BASES
    }
    for basis, expected_count in expected_source_counts.items():
        observed = set(
            pd.to_numeric(
                summary.loc[summary["analysis_basis"].eq(basis), "source_cohort_count"],
                errors="coerce",
            ).dropna()
        )
        if observed != {expected_count}:
            errors.append(
                f"launch timing source cohort count drift: basis={basis} expected={expected_count} observed={observed}"
            )

    identity_columns = ["analysis_basis", "episode_key", "trigger_id", "outcome_definition_id"]
    if detail.duplicated(identity_columns).any():
        errors.append("launch timing detail duplicates analysis-basis episode trigger outcome rows")
    expected_detail_count = sum(expected_source_counts.values()) * len(TRIGGER_SPECS) * len(OUTCOME_SPECS)
    if len(detail) != expected_detail_count:
        errors.append(
            f"launch timing detail row count drift: expected={expected_detail_count} actual={len(detail)}"
        )

    canonical = detail.loc[
        detail["trigger_id"].eq(PRIMARY_TRIGGER_ID)
        & detail["outcome_definition_id"].eq(PRIMARY_OUTCOME_ID)
    ].copy()
    for basis in ANALYSIS_BASES:
        current = canonical.loc[canonical["analysis_basis"].eq(basis)]
        if current["episode_key"].nunique() != expected_source_counts[basis]:
            errors.append(f"launch timing canonical detail omits source episodes: {basis}")
        accepted = current.loc[current["observation_selection_status"].eq("accepted")].copy()
        for stock_id, stock in accepted.groupby("stock_id", sort=False):
            positions = pd.to_numeric(stock["source_stock_sequence_index"], errors="coerce").dropna().sort_values()
            if len(positions) > 1 and positions.diff().dropna().le(FULL_OBSERVATION_NON_OVERLAP_DAYS).any():
                errors.append(f"launch timing same-stock full observation overlap: {basis} {stock_id}")
        if accepted["episode_key"].duplicated().any():
            errors.append(f"launch timing accepted episodes repeat: {basis}")
        available = pd.to_numeric(accepted["observation_available_candidate_days"], errors="coerce")
        mature = _boolish(accepted["mature_for_126d_classification"])
        if not mature.eq(available.ge(SIX_MONTH_HORIZON_DAYS)).all():
            errors.append(f"launch timing right-censor maturity drift: {basis}")
        classifications = set(accepted["classification_at_126d"].astype(str))
        if not classifications <= {
            "launch_within_126d",
            "no_launch_within_126d",
            "right_censored_before_126d",
        }:
            errors.append(f"launch timing accepted classification drift: {basis}")

    primary = canonical.loc[
        canonical["analysis_basis"].eq(PRIMARY_ANALYSIS_BASIS)
        & canonical["observation_selection_status"].eq("accepted")
    ]
    sensitivity = canonical.loc[
        canonical["analysis_basis"].eq(SENSITIVITY_ANALYSIS_BASIS)
        & canonical["observation_selection_status"].eq("accepted")
    ]
    primary_candidates = _boolish(primary["source_revenue_or_price_anomaly_candidate_flag"]) | _boolish(
        primary["abs_ge80_anomaly_candidate_flag"]
    )
    sensitivity_candidates = _boolish(
        sensitivity["source_revenue_or_price_anomaly_candidate_flag"]
    ) | _boolish(sensitivity["abs_ge80_anomaly_candidate_flag"])
    if not primary_candidates.any():
        errors.append("launch timing primary basis unexpectedly excludes every unresolved candidate")
    if sensitivity_candidates.any():
        errors.append("launch timing legacy sensitivity basis still contains threshold candidates")

    force_detail = primary.loc[primary["stock_id"].eq("3593")]
    if len(force_detail) != 1:
        errors.append("launch timing canonical primary must contain one accepted 3593 episode")
    else:
        force_row = force_detail.iloc[0]
        if not _boolish(pd.Series([force_row["observation_price_path_resolved_flag"]])).iloc[0]:
            errors.append("3593 raw price discontinuity must be marked resolved")
        if _boolish(
            pd.Series([force_row["observation_unresolved_price_path_anomaly_candidate_flag"]])
        ).iloc[0]:
            errors.append("3593 adjusted price path must not remain unresolved")
        if force_row["observation_price_comparability_resolution_ids"] != (
            "3593_20251222_loss_offset_capital_reduction"
        ):
            errors.append("3593 detail does not cite its price comparability resolution")
        if str(force_row["launch_date"]) == "20251203":
            errors.append("3593 capital-reduction raw jump is still misclassified as a launch")

    for row in summary.itertuples(index=False):
        accepted_count = int(row.accepted_episode_count)
        launch_count = int(row.launch_count)
        no_launch_count = int(row.no_launch_count)
        censored_count = int(row.right_censored_count)
        classifiable_count = int(row.classifiable_episode_count)
        if launch_count + no_launch_count != classifiable_count:
            errors.append(
                f"launch timing classifiable count mismatch: {row.analysis_basis}/{row.trigger_id}/"
                f"{row.outcome_definition_id}/{row.horizon_trading_days}"
            )
        if classifiable_count + censored_count != accepted_count:
            errors.append(
                f"launch timing accepted partition mismatch: {row.analysis_basis}/{row.trigger_id}/"
                f"{row.outcome_definition_id}/{row.horizon_trading_days}"
            )
        if int(row.same_stock_overlap_pair_count) != 0:
            errors.append("launch timing summary reports same-stock overlap")
        if int(row.observation_unresolved_price_path_anomaly_candidate_count) != 0:
            errors.append("launch timing summary retains an unresolved adjusted price-path candidate")
        if row.right_censor_policy != "insufficient_future_trading_days_are_right_censored_not_failures":
            errors.append("launch timing right-censor policy drift")
        if row.financial_statement_scope != FINANCIAL_STATEMENT_SCOPE:
            errors.append("launch timing financial-statement scope drift")
        if row.promotion_readiness != (
            "blocked_pending_root_cause_anomaly_candidate_review_and_forward_trigger_test"
        ):
            errors.append("launch timing summary must remain blocked from promotion")

    required_time_bases = {
        "source_signal_date",
        "retrospective_breakout_anchor",
        "pre_breakout_week_change",
    }
    if set(feature["feature_time_basis"].astype(str)) != required_time_bases:
        errors.append("launch timing feature time-basis coverage drift")
    required_families = {
        "monthly_revenue",
        "tdcc",
        "technical",
        "price_momentum",
        "price_shape",
        "price_position",
        "volume",
        "breakout",
        "candle",
        "market_regime",
        "market_regime_risk",
    }
    if not required_families <= set(feature["feature_family"].astype(str)):
        errors.append("launch timing feature family coverage drift")
    if feature.duplicated(["analysis_basis", "feature_time_basis", "feature_id"]).any():
        errors.append("launch timing feature contrast duplicates feature rows")
    if not set(feature["classification_trigger_id"].astype(str)) == {PRIMARY_TRIGGER_ID}:
        errors.append("launch timing feature contrast trigger basis drift")
    if not set(feature["classification_outcome_definition_id"].astype(str)) == {PRIMARY_OUTCOME_ID}:
        errors.append("launch timing feature contrast outcome basis drift")
    binary = feature.loc[feature["feature_kind"].eq("binary")].copy()
    for row in binary.itertuples(index=False):
        expected_hit_count = int(row.launch_hit_count) + int(row.no_launch_hit_count)
        if int(row.feature_hit_sample_count) != expected_hit_count:
            errors.append(
                f"launch timing conditional feature hit count drift: {row.analysis_basis}/{row.feature_time_basis}/{row.feature_id}"
            )
        observed_total = int(row.launch_observed_count) + int(row.no_launch_observed_count)
        if int(row.feature_hit_sample_count) + int(row.feature_miss_sample_count) != observed_total:
            errors.append(
                f"launch timing conditional feature partition drift: {row.analysis_basis}/{row.feature_time_basis}/{row.feature_id}"
            )
        if int(row.feature_hit_sample_count) > 0:
            expected_rate = round(
                int(row.launch_hit_count) / int(row.feature_hit_sample_count) * 100.0,
                4,
            )
            if abs(float(row.launch_rate_when_feature_hit_pct) - expected_rate) > 0.0001:
                errors.append(
                    f"launch timing conditional feature rate drift: {row.analysis_basis}/{row.feature_time_basis}/{row.feature_id}"
                )
    return errors


def main() -> int:
    errors = validate()
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1
    summary = _read(LATEST_CSV)
    row = summary.loc[
        summary["analysis_basis"].eq(PRIMARY_ANALYSIS_BASIS)
        & summary["trigger_id"].eq(PRIMARY_TRIGGER_ID)
        & summary["outcome_definition_id"].eq(PRIMARY_OUTCOME_ID)
        & pd.to_numeric(summary["horizon_trading_days"], errors="coerce").eq(SIX_MONTH_HORIZON_DAYS)
    ].iloc[0]
    print(
        "revenue launch timing feature audit validation passed: "
        f"source={int(row['source_cohort_count'])} accepted={int(row['accepted_episode_count'])} "
        f"launch={int(row['launch_count'])} no_launch={int(row['no_launch_count'])} "
        f"right_censored={int(row['right_censored_count'])}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
