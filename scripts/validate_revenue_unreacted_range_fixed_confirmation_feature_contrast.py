from __future__ import annotations

import math
import sys
from pathlib import Path

import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent))

from build_daily_model_parameter_research import (  # noqa: E402
    REVENUE_UNREACTED_FEATURE_CONTRAST_BINARY_SPECS,
    REVENUE_UNREACTED_FEATURE_CONTRAST_NUMERIC_SPECS,
)
from revenue_unreacted_range_close_confirmation_timing import (  # noqa: E402
    DECISION_BASIS,
    FIXED_FEATURE_CONTRAST_EXIT_CLOCK_ID,
    FIXED_FEATURE_CONTRAST_PENDING_WINDOW_DAYS,
    FIXED_FEATURE_CONTRAST_VARIANT_ID,
    INCLUDING_BASIS,
    SUMMARY_CSV as TIMING_SUMMARY_CSV,
)
from revenue_unreacted_range_fixed_confirmation_feature_contrast import (  # noqa: E402
    ANOMALY_CSV,
    ARTIFACT_ID,
    DETAIL_CSV,
    DOCS_ANOMALY_CSV,
    DOCS_SUMMARY_CSV,
    DOCS_SUMMARY_MD,
    EXTREME_SENSITIVITY_BASIS,
    FEATURE_TIME_BASES,
    FINANCIAL_STATEMENT_EXCLUSIONS,
    HISTORY_ANOMALY_CSV,
    HISTORY_SUMMARY_CSV,
    SUMMARY_CSV,
    SUMMARY_MD,
    feature_observed_mask,
    numeric_feature_observed_mask,
)
from tracking_utils import DOCS_LATEST_DIR  # noqa: E402


EXPECTED_BASES = {INCLUDING_BASIS, DECISION_BASIS, EXTREME_SENSITIVITY_BASIS}
EXPECTED_TIME_BASES = {str(item["feature_time_basis"]) for item in FEATURE_TIME_BASES}
SUMMARY_REQUIRED = {
    "model_id",
    "research_artifact_id",
    "anomaly_exclusion_basis",
    "decision_basis",
    "sensitivity_basis",
    "feature_time_basis",
    "feature_information_cutoff",
    "candidate_confirmation_rule_id",
    "pending_window_days",
    "exit_clock_id",
    "entry_rule_id",
    "stop_rule_id",
    "row_type",
    "feature_id",
    "feature_family",
    "feature_column",
    "feature_observed_column",
    "feature_independence_status",
    "equivalent_to_feature_id",
    "feature_observed_count",
    "feature_coverage_pct",
    "feature_hit_count",
    "accepted_trade_count",
    "win_count",
    "neutral_count",
    "failure_count",
    "win_rate_pct",
    "neutral_rate_pct",
    "failure_rate_pct",
    "avg_realized_return_pct",
    "median_realized_return_pct",
    "high_return_8_count",
    "high_return_8_rate_pct",
    "loss_5_count",
    "loss_5_rate_pct",
    "same_stock_overlap_pair_count",
    "same_stock_revenue_period_repeat_count",
    "timing_expected_accepted_trade_count",
    "timing_accepted_trade_count_parity_status",
    "extreme_sensitivity_direction_status",
    "monthly_revenue_scope",
    "financial_statement_scope",
    "financial_statement_fields_excluded",
    "combination_policy",
    "sample_count_context",
    "feature_context_revenue_anomaly_count",
    "feature_context_revenue_anomalies_excluded_from_feature_evidence",
    "approved_for_daily",
    "production_change",
}
DETAIL_REQUIRED = {
    "model_id",
    "research_artifact_id",
    "anomaly_exclusion_basis",
    "decision_basis",
    "sensitivity_basis",
    "feature_time_basis",
    "feature_context_join_status",
    "feature_context_date",
    "candidate_confirmation_rule_id",
    "pending_window_days_fixed",
    "exit_clock_id_fixed",
    "entry_rule_id",
    "stop_rule_id",
    "episode_key",
    "stock_id",
    "signal_date",
    "signal_sequence_index",
    "confirmation_date",
    "confirmation_sequence_index",
    "entry_date",
    "entry_sequence_index",
    "exit_date",
    "exit_sequence_index",
    "realized_return_pct",
    "outcome_label",
    "price_path_anomaly_flag",
    "source_revenue_or_price_anomaly_flag",
    "source_monthly_revenue_period",
    "source_monthly_revenue_source_table_date",
    "full_monthly_revenue_source_table_date",
    "full_monthly_revenue_numerical_anomaly_flag",
    "tdcc_as_of_date",
    "same_stock_non_overlap_applied",
    "monthly_revenue_scope",
    "financial_statement_scope",
    "financial_statement_fields_excluded",
    "approved_for_daily",
    "production_change",
}
ANOMALY_REQUIRED = {
    "model_id",
    "research_artifact_id",
    "anomaly_exclusion_basis",
    "decision_basis",
    "sensitivity_basis",
    "accepted_trade_count",
    "same_stock_overlap_pair_count",
    "same_stock_revenue_period_repeat_count",
    "price_path_anomaly_count",
    "return_abs_ge80_count",
    "signal_feature_context_revenue_anomaly_count",
    "confirmation_feature_context_revenue_anomaly_count",
    "feature_context_revenue_anomalies_excluded_from_feature_evidence",
    "max_realized_return_pct",
    "max_return_stock_id",
    "max_return_signal_date",
    "min_realized_return_pct",
    "min_return_stock_id",
    "min_return_signal_date",
    "top1_abs_return_share_pct",
    "top5_abs_return_share_pct",
    "avg_realized_return_pct",
    "median_realized_return_pct",
    "trimmed_1pct_avg_return_pct",
    "interpretation_status",
    "approved_for_daily",
    "production_change",
}


def read_csv(path: Path) -> pd.DataFrame:
    return pd.read_csv(path, dtype=str, keep_default_na=False)


def boolish(series: pd.Series) -> pd.Series:
    return series.astype(str).str.strip().str.lower().isin({"true", "1", "yes"})


def number(value: object) -> float:
    parsed = pd.to_numeric(pd.Series([value]), errors="coerce").iloc[0]
    return float(parsed) if pd.notna(parsed) else math.nan


def close_enough(actual: object, expected: float, tolerance: float = 0.011) -> bool:
    parsed = number(actual)
    return not math.isnan(parsed) and abs(parsed - expected) <= tolerance


def rate(count: int, total: int) -> float:
    return round(count / total * 100.0, 4) if total else math.nan


def outcome_metrics(part: pd.DataFrame) -> dict[str, float | int]:
    realized = pd.to_numeric(part["realized_return_pct"], errors="coerce").dropna()
    wins = realized.ge(5.0)
    neutral = realized.ge(0.0) & realized.lt(5.0)
    failure = realized.lt(0.0)
    high = realized.ge(8.0)
    loss = realized.le(-5.0)
    return {
        "accepted_trade_count": len(realized),
        "win_count": int(wins.sum()),
        "neutral_count": int(neutral.sum()),
        "failure_count": int(failure.sum()),
        "win_rate_pct": rate(int(wins.sum()), len(realized)),
        "neutral_rate_pct": rate(int(neutral.sum()), len(realized)),
        "failure_rate_pct": rate(int(failure.sum()), len(realized)),
        "avg_realized_return_pct": round(float(realized.mean()), 4) if len(realized) else math.nan,
        "median_realized_return_pct": round(float(realized.median()), 4) if len(realized) else math.nan,
        "high_return_8_count": int(high.sum()),
        "high_return_8_rate_pct": rate(int(high.sum()), len(realized)),
        "loss_5_count": int(loss.sum()),
        "loss_5_rate_pct": rate(int(loss.sum()), len(realized)),
    }


def validate_outcome_row(row: pd.Series, part: pd.DataFrame, label: str, errors: list[str]) -> None:
    expected = outcome_metrics(part)
    integer_columns = {
        "accepted_trade_count",
        "win_count",
        "neutral_count",
        "failure_count",
        "high_return_8_count",
        "loss_5_count",
    }
    for column, expected_value in expected.items():
        if column in integer_columns:
            if int(number(row.get(column, -1))) != int(expected_value):
                errors.append(f"{label} {column} mismatch")
        elif math.isnan(float(expected_value)):
            if not math.isnan(number(row.get(column))):
                errors.append(f"{label} {column} must be blank")
        elif not close_enough(row.get(column), float(expected_value)):
            errors.append(f"{label} {column} mismatch: {row.get(column)} != {expected_value}")


def validate_contract_columns(frame: pd.DataFrame, required: set[str], label: str) -> list[str]:
    missing = required - set(frame.columns)
    if missing:
        return [f"{label} missing columns: {sorted(missing)}"]
    if frame.empty:
        return [f"{label} is empty"]
    return []


def validate_detail(detail: pd.DataFrame) -> list[str]:
    errors = validate_contract_columns(detail, DETAIL_REQUIRED, "fixed feature detail")
    if errors:
        return errors
    if set(detail["model_id"]) != {"revenue_unreacted_range"} or set(detail["research_artifact_id"]) != {
        ARTIFACT_ID
    }:
        errors.append("detail model/artifact identity mismatch")
    if set(detail["anomaly_exclusion_basis"]) != EXPECTED_BASES:
        errors.append("detail anomaly bases mismatch")
    if set(detail["feature_time_basis"]) != EXPECTED_TIME_BASES:
        errors.append("detail feature time bases mismatch")
    if set(detail["candidate_confirmation_rule_id"]) != {FIXED_FEATURE_CONTRAST_VARIANT_ID}:
        errors.append("detail confirmation rule drifted")
    if pd.to_numeric(detail["pending_window_days_fixed"], errors="coerce").ne(
        FIXED_FEATURE_CONTRAST_PENDING_WINDOW_DAYS
    ).any():
        errors.append("detail pending window drifted")
    if set(detail["exit_clock_id_fixed"]) != {FIXED_FEATURE_CONTRAST_EXIT_CLOCK_ID}:
        errors.append("detail exit clock drifted")
    if set(detail["entry_rule_id"]) != {"confirmation_close_next_trading_day_open"}:
        errors.append("detail entry rule drifted")
    if set(detail["stop_rule_id"]) != {"no_stop_in_fixed_feature_contrast"}:
        errors.append("detail stop rule drifted")
    if set(detail["feature_context_join_status"]) != {"matched_unique_stock_sequence"}:
        errors.append("detail contains missing/duplicate feature context joins")
    if not boolish(detail["same_stock_non_overlap_applied"]).all():
        errors.append("detail must enforce same-stock non-overlap")
    if boolish(detail["approved_for_daily"]).any() or set(detail["production_change"]) != {"none"}:
        errors.append("detail must remain research-only")
    if set(detail["monthly_revenue_scope"]) != {"monthly_revenue_point_in_time_only"}:
        errors.append("detail monthly revenue scope mismatch")
    if set(detail["financial_statement_scope"]) != {"excluded_no_formal_point_in_time_layer"}:
        errors.append("detail financial statement scope mismatch")
    if set(detail["financial_statement_fields_excluded"]) != {FINANCIAL_STATEMENT_EXCLUSIONS}:
        errors.append("detail financial statement exclusions mismatch")

    realized = pd.to_numeric(detail["realized_return_pct"], errors="coerce")
    expected_label = pd.Series("failure", index=detail.index)
    expected_label = expected_label.mask(realized.ge(0.0) & realized.lt(5.0), "neutral")
    expected_label = expected_label.mask(realized.ge(5.0), "win")
    if not detail["outcome_label"].eq(expected_label).all():
        errors.append("detail outcome labels drifted")

    decision = detail[detail["anomaly_exclusion_basis"].eq(DECISION_BASIS)]
    if boolish(decision["price_path_anomaly_flag"]).any() or boolish(
        decision["source_revenue_or_price_anomaly_flag"]
    ).any():
        errors.append("decision-basis detail contains a known revenue/price/path anomaly")
    if not boolish(decision["decision_basis"]).all() or boolish(decision["sensitivity_basis"]).any():
        errors.append("decision-basis flags mismatch")
    sensitivity = detail[detail["anomaly_exclusion_basis"].eq(EXTREME_SENSITIVITY_BASIS)]
    if boolish(sensitivity["decision_basis"]).any() or not boolish(sensitivity["sensitivity_basis"]).all():
        errors.append("extreme sensitivity flags mismatch")
    if pd.to_numeric(sensitivity["realized_return_pct"], errors="coerce").abs().ge(80.0).any():
        errors.append("extreme sensitivity detail still contains |return| >= 80%")
    decision_keys = set(zip(decision["feature_time_basis"], decision["episode_key"]))
    sensitivity_keys = set(zip(sensitivity["feature_time_basis"], sensitivity["episode_key"]))
    if not sensitivity_keys.issubset(decision_keys):
        errors.append("extreme sensitivity is not a strict decision-basis subset")

    for _, row in detail.iterrows():
        source_date = str(row["source_monthly_revenue_source_table_date"])
        signal_date = str(row["signal_date"])
        context_date = str(row["feature_context_date"])
        revenue_date = str(row["full_monthly_revenue_source_table_date"])
        tdcc_date = str(row["tdcc_as_of_date"])
        if source_date and source_date > signal_date:
            errors.append(f"future source monthly revenue row: {row['stock_id']} {signal_date}")
        if revenue_date and revenue_date > context_date:
            errors.append(f"future feature monthly revenue row: {row['stock_id']} {context_date}")
        if tdcc_date and tdcc_date > context_date:
            errors.append(f"future TDCC row: {row['stock_id']} {context_date}")

    for (basis, time_basis), part in detail.groupby(
        ["anomaly_exclusion_basis", "feature_time_basis"], sort=False
    ):
        if part.duplicated(["episode_key"]).any():
            errors.append(f"duplicate feature episode rows: {basis}/{time_basis}")
        for stock_id, stock_part in part.groupby("stock_id", sort=False):
            ordered = stock_part.assign(
                _entry=pd.to_numeric(stock_part["entry_sequence_index"], errors="coerce"),
                _exit=pd.to_numeric(stock_part["exit_sequence_index"], errors="coerce"),
            ).dropna(subset=["_entry", "_exit"]).sort_values("_entry")
            active_exit: float | None = None
            for _, trade in ordered.iterrows():
                entry = float(trade["_entry"])
                exit_value = float(trade["_exit"])
                if active_exit is not None and entry <= active_exit:
                    errors.append(f"same-stock overlap: {basis}/{time_basis}/{stock_id}")
                active_exit = exit_value if active_exit is None else max(active_exit, exit_value)
        if basis in {DECISION_BASIS, EXTREME_SENSITIVITY_BASIS}:
            repeats = part.groupby(["stock_id", "source_monthly_revenue_period"], dropna=False).size()
            if repeats.gt(1).any():
                errors.append(f"same stock/revenue period repeated: {basis}/{time_basis}")
    return errors


def validate_summary(summary: pd.DataFrame, detail: pd.DataFrame, timing: pd.DataFrame) -> list[str]:
    errors = validate_contract_columns(summary, SUMMARY_REQUIRED, "fixed feature summary")
    if errors:
        return errors
    if set(summary["model_id"]) != {"revenue_unreacted_range"} or set(summary["research_artifact_id"]) != {
        ARTIFACT_ID
    }:
        errors.append("summary model/artifact identity mismatch")
    if set(summary["anomaly_exclusion_basis"]) != EXPECTED_BASES:
        errors.append("summary anomaly bases mismatch")
    if set(summary["feature_time_basis"]) != EXPECTED_TIME_BASES:
        errors.append("summary feature time bases mismatch")
    if set(summary["candidate_confirmation_rule_id"]) != {FIXED_FEATURE_CONTRAST_VARIANT_ID}:
        errors.append("summary confirmation rule drifted")
    if pd.to_numeric(summary["pending_window_days"], errors="coerce").ne(
        FIXED_FEATURE_CONTRAST_PENDING_WINDOW_DAYS
    ).any():
        errors.append("summary pending window drifted")
    if set(summary["exit_clock_id"]) != {FIXED_FEATURE_CONTRAST_EXIT_CLOCK_ID}:
        errors.append("summary exit clock drifted")
    if set(summary["combination_policy"]) != {"single_features_only_no_arbitrary_condition_stacking"}:
        errors.append("summary combination policy drifted")
    if boolish(summary["approved_for_daily"]).any() or set(summary["production_change"]) != {"none"}:
        errors.append("summary must remain research-only")
    if pd.to_numeric(summary["same_stock_overlap_pair_count"], errors="coerce").ne(0).any():
        errors.append("summary same-stock overlap must be zero")
    decision_or_sensitivity = summary[summary["anomaly_exclusion_basis"].isin({DECISION_BASIS, EXTREME_SENSITIVITY_BASIS})]
    if pd.to_numeric(decision_or_sensitivity["same_stock_revenue_period_repeat_count"], errors="coerce").ne(0).any():
        errors.append("decision/sensitivity same stock/revenue period repeat count must be zero")
    if set(summary["financial_statement_fields_excluded"]) != {FINANCIAL_STATEMENT_EXCLUSIONS}:
        errors.append("summary financial statement exclusions mismatch")

    expected_binary = {str(spec["feature_id"]) for spec in REVENUE_UNREACTED_FEATURE_CONTRAST_BINARY_SPECS}
    expected_numeric = {str(spec[1]) for spec in REVENUE_UNREACTED_FEATURE_CONTRAST_NUMERIC_SPECS}
    timing_target = timing[
        timing["row_type"].eq("variant_performance")
        & timing["confirmation_variant_id"].eq(FIXED_FEATURE_CONTRAST_VARIANT_ID)
        & pd.to_numeric(timing["pending_window_days"], errors="coerce").eq(
            FIXED_FEATURE_CONTRAST_PENDING_WINDOW_DAYS
        )
        & timing["exit_clock_id"].eq(FIXED_FEATURE_CONTRAST_EXIT_CLOCK_ID)
    ]
    timing_counts = {
        row["anomaly_exclusion_basis"]: int(number(row["accepted_trade_count"]))
        for _, row in timing_target.iterrows()
    }
    for (basis, time_basis), part in detail.groupby(
        ["anomaly_exclusion_basis", "feature_time_basis"], sort=False
    ):
        part_summary = summary[
            summary["anomaly_exclusion_basis"].eq(basis)
            & summary["feature_time_basis"].eq(time_basis)
        ]
        baseline_rows = part_summary[part_summary["row_type"].eq("baseline")]
        if len(baseline_rows) != 1:
            errors.append(f"missing/duplicate baseline: {basis}/{time_basis}")
            continue
        baseline = baseline_rows.iloc[0]
        validate_outcome_row(baseline, part, f"baseline {basis}/{time_basis}", errors)
        expected_revenue_anomaly_count = int(
            boolish(part["full_monthly_revenue_numerical_anomaly_flag"]).sum()
        )
        if pd.to_numeric(
            part_summary["feature_context_revenue_anomaly_count"], errors="coerce"
        ).ne(expected_revenue_anomaly_count).any():
            errors.append(f"feature-context revenue anomaly count mismatch: {basis}/{time_basis}")
        if not boolish(
            part_summary["feature_context_revenue_anomalies_excluded_from_feature_evidence"]
        ).all():
            errors.append(f"feature-context revenue anomaly exclusion flag failed: {basis}/{time_basis}")
        expected_count = len(part) if basis == EXTREME_SENSITIVITY_BASIS else timing_counts.get(basis, -1)
        if int(number(baseline["timing_expected_accepted_trade_count"])) != expected_count:
            errors.append(f"timing expected count mismatch: {basis}/{time_basis}")
        if baseline["timing_accepted_trade_count_parity_status"] != "pass":
            errors.append(f"timing parity failed: {basis}/{time_basis}")

        binary_rows = part_summary[part_summary["row_type"].eq("binary_feature")]
        if set(binary_rows["feature_id"]) != expected_binary:
            errors.append(f"binary feature coverage mismatch: {basis}/{time_basis}")
        prior_masks: list[tuple[str, pd.Series]] = []
        for spec in REVENUE_UNREACTED_FEATURE_CONTRAST_BINARY_SPECS:
            feature_id = str(spec["feature_id"])
            rows = binary_rows[binary_rows["feature_id"].eq(feature_id)]
            if len(rows) != 1:
                errors.append(f"missing binary row: {basis}/{time_basis}/{feature_id}")
                continue
            row = rows.iloc[0]
            expected_observed = feature_observed_mask(part, feature_id, str(spec["feature_family"]))
            expected_hit = pd.Series(spec["condition"](part), index=part.index).fillna(False).astype(bool) & expected_observed
            stored_observed = boolish(part[f"feature_observed__{feature_id}"])
            stored_hit = boolish(part[f"feature__{feature_id}"])
            if not stored_observed.equals(expected_observed):
                errors.append(f"observed mask drifted: {basis}/{time_basis}/{feature_id}")
            if not stored_hit.equals(expected_hit):
                errors.append(f"feature mask drifted: {basis}/{time_basis}/{feature_id}")
            validate_outcome_row(
                row,
                part[expected_hit],
                f"feature {basis}/{time_basis}/{feature_id}",
                errors,
            )
            if int(number(row["feature_observed_count"])) != int(expected_observed.sum()):
                errors.append(f"feature observed count mismatch: {basis}/{time_basis}/{feature_id}")
            if int(number(row["feature_hit_count"])) != int(expected_hit.sum()):
                errors.append(f"feature hit count mismatch: {basis}/{time_basis}/{feature_id}")
            equivalent_to = next(
                (prior_id for prior_id, prior_mask in prior_masks if expected_hit.equals(prior_mask)),
                "",
            ) if expected_hit.any() else ""
            if expected_hit.any():
                prior_masks.append((feature_id, expected_hit))
            if row["equivalent_to_feature_id"] != equivalent_to:
                errors.append(f"duplicate-mask identity mismatch: {basis}/{time_basis}/{feature_id}")
            realized = pd.to_numeric(part["realized_return_pct"], errors="coerce")
            for group_id, group_mask in {
                "high_return": realized.ge(8.0),
                "win": realized.ge(5.0),
                "failure": realized.lt(0.0),
            }.items():
                observed_count = int((group_mask & expected_observed).sum())
                hit_count = int((group_mask & expected_hit).sum())
                if int(number(row[f"{group_id}_feature_observed_count"])) != observed_count:
                    errors.append(f"group observed count mismatch: {basis}/{time_basis}/{feature_id}/{group_id}")
                if int(number(row[f"{group_id}_feature_hit_count"])) != hit_count:
                    errors.append(f"group hit count mismatch: {basis}/{time_basis}/{feature_id}/{group_id}")
                expected_rate = rate(hit_count, observed_count)
                if not math.isnan(expected_rate) and not close_enough(
                    row[f"{group_id}_feature_hit_rate_within_observed_pct"], expected_rate
                ):
                    errors.append(f"group observed hit rate mismatch: {basis}/{time_basis}/{feature_id}/{group_id}")

        numeric_rows = part_summary[part_summary["row_type"].eq("numeric_feature")]
        if set(numeric_rows["feature_id"]) != expected_numeric:
            errors.append(f"numeric feature coverage mismatch: {basis}/{time_basis}")
        for _, feature_id, family, column in REVENUE_UNREACTED_FEATURE_CONTRAST_NUMERIC_SPECS:
            rows = numeric_rows[numeric_rows["feature_id"].eq(feature_id)]
            if len(rows) != 1 or column not in part.columns:
                errors.append(f"numeric row/column missing: {basis}/{time_basis}/{feature_id}")
                continue
            row = rows.iloc[0]
            observed = numeric_feature_observed_mask(part, family, column)
            if int(number(row["feature_observed_count"])) != int(observed.sum()):
                errors.append(f"numeric observed count mismatch: {basis}/{time_basis}/{feature_id}")
            expected_coverage = rate(int(observed.sum()), len(part))
            if not math.isnan(expected_coverage) and not close_enough(
                row["feature_coverage_pct"], expected_coverage
            ):
                errors.append(f"numeric coverage mismatch: {basis}/{time_basis}/{feature_id}")
            values = pd.to_numeric(part[column], errors="coerce").where(observed)
            realized = pd.to_numeric(part["realized_return_pct"], errors="coerce")
            for group_id, mask in {
                "high_return": realized.ge(8.0),
                "win": realized.ge(5.0),
                "failure": realized.lt(0.0),
            }.items():
                group = values[mask].dropna()
                if len(group):
                    if not close_enough(row[f"{group_id}_feature_mean"], round(float(group.mean()), 4)):
                        errors.append(f"numeric mean mismatch: {basis}/{time_basis}/{feature_id}/{group_id}")
                    if not close_enough(row[f"{group_id}_feature_median"], round(float(group.median()), 4)):
                        errors.append(f"numeric median mismatch: {basis}/{time_basis}/{feature_id}/{group_id}")
    decision_rows = summary[summary["anomaly_exclusion_basis"].eq(DECISION_BASIS)]
    if decision_rows["extreme_sensitivity_direction_status"].isin(
        {"not_applicable", "missing_sensitivity_counterpart"}
    ).any():
        errors.append("decision rows must have an extreme-return sensitivity direction result")
    return errors


def validate_anomaly(anomaly: pd.DataFrame, detail: pd.DataFrame) -> list[str]:
    errors = validate_contract_columns(anomaly, ANOMALY_REQUIRED, "fixed feature anomaly audit")
    if errors:
        return errors
    if set(anomaly["anomaly_exclusion_basis"]) != EXPECTED_BASES or len(anomaly) != 3:
        errors.append("anomaly audit must have exactly three bases")
    if boolish(anomaly["approved_for_daily"]).any() or set(anomaly["production_change"]) != {"none"}:
        errors.append("anomaly audit must remain research-only")
    signal = detail[detail["feature_time_basis"].eq("signal_date_close")]
    for _, row in anomaly.iterrows():
        basis = row["anomaly_exclusion_basis"]
        part = signal[signal["anomaly_exclusion_basis"].eq(basis)]
        realized = pd.to_numeric(part["realized_return_pct"], errors="coerce").dropna().sort_values()
        if len(realized) != int(number(row["accepted_trade_count"])):
            errors.append(f"anomaly accepted count mismatch: {basis}")
            continue
        max_index = realized.idxmax()
        min_index = realized.idxmin()
        if not close_enough(row["max_realized_return_pct"], float(realized.loc[max_index]), 0.00011):
            errors.append(f"anomaly max return mismatch: {basis}")
        if not close_enough(row["min_realized_return_pct"], float(realized.loc[min_index]), 0.00011):
            errors.append(f"anomaly min return mismatch: {basis}")
        if row["max_return_stock_id"] != str(part.loc[max_index, "stock_id"]):
            errors.append(f"anomaly max stock mismatch: {basis}")
        if row["min_return_stock_id"] != str(part.loc[min_index, "stock_id"]):
            errors.append(f"anomaly min stock mismatch: {basis}")
        absolute = realized.abs().sort_values(ascending=False)
        total = float(absolute.sum())
        top1 = round(float(absolute.iloc[:1].sum()) / total * 100.0, 4) if total else 0.0
        top5 = round(float(absolute.iloc[:5].sum()) / total * 100.0, 4) if total else 0.0
        if not close_enough(row["top1_abs_return_share_pct"], top1):
            errors.append(f"anomaly top1 share mismatch: {basis}")
        if not close_enough(row["top5_abs_return_share_pct"], top5):
            errors.append(f"anomaly top5 share mismatch: {basis}")
        if int(number(row["return_abs_ge80_count"])) != int(realized.abs().ge(80.0).sum()):
            errors.append(f"anomaly abs80 count mismatch: {basis}")
        basis_detail = detail[detail["anomaly_exclusion_basis"].eq(basis)]
        signal_revenue_anomalies = int(
            boolish(
                basis_detail.loc[
                    basis_detail["feature_time_basis"].eq("signal_date_close"),
                    "full_monthly_revenue_numerical_anomaly_flag",
                ]
            ).sum()
        )
        confirmation_revenue_anomalies = int(
            boolish(
                basis_detail.loc[
                    basis_detail["feature_time_basis"].eq("confirmation_date_close"),
                    "full_monthly_revenue_numerical_anomaly_flag",
                ]
            ).sum()
        )
        if int(number(row["signal_feature_context_revenue_anomaly_count"])) != signal_revenue_anomalies:
            errors.append(f"signal feature-context revenue anomaly count mismatch: {basis}")
        if int(number(row["confirmation_feature_context_revenue_anomaly_count"])) != confirmation_revenue_anomalies:
            errors.append(f"confirmation feature-context revenue anomaly count mismatch: {basis}")
        if not boolish(
            pd.Series([row["feature_context_revenue_anomalies_excluded_from_feature_evidence"]])
        ).all():
            errors.append(f"feature-context revenue anomaly exclusion flag failed: {basis}")
    return errors


def validate_mirrors(errors: list[str]) -> None:
    for left, right in (
        (SUMMARY_CSV, HISTORY_SUMMARY_CSV),
        (SUMMARY_CSV, DOCS_SUMMARY_CSV),
        (ANOMALY_CSV, HISTORY_ANOMALY_CSV),
        (ANOMALY_CSV, DOCS_ANOMALY_CSV),
        (SUMMARY_MD, DOCS_SUMMARY_MD),
    ):
        if not left.exists() or not right.exists():
            errors.append(f"missing mirror: {left} / {right}")
        elif left.read_bytes() != right.read_bytes():
            errors.append(f"mirror mismatch: {left} / {right}")
    forbidden = [
        DOCS_LATEST_DIR / DETAIL_CSV.name,
        HISTORY_SUMMARY_CSV.parent / DETAIL_CSV.name.replace("_latest", ""),
    ]
    for path in forbidden:
        if path.exists():
            errors.append(f"large detail must not be mirrored: {path}")


def validate_frames(
    summary: pd.DataFrame,
    detail: pd.DataFrame,
    anomaly: pd.DataFrame,
    timing: pd.DataFrame,
) -> list[str]:
    errors: list[str] = []
    errors.extend(validate_detail(detail))
    errors.extend(validate_summary(summary, detail, timing))
    errors.extend(validate_anomaly(anomaly, detail))
    return errors


def main() -> int:
    required_paths = [SUMMARY_CSV, DETAIL_CSV, ANOMALY_CSV, SUMMARY_MD, TIMING_SUMMARY_CSV]
    missing = [str(path) for path in required_paths if not path.exists()]
    if missing:
        print(f"missing fixed feature contrast artifacts: {missing}", file=sys.stderr)
        return 1
    summary = read_csv(SUMMARY_CSV)
    detail = read_csv(DETAIL_CSV)
    anomaly = read_csv(ANOMALY_CSV)
    timing = read_csv(TIMING_SUMMARY_CSV)
    errors = validate_frames(summary, detail, anomaly, timing)
    validate_mirrors(errors)
    generated = summary["generated_at"].drop_duplicates().tolist() if "generated_at" in summary else []
    if len(generated) != 1 or f"- generated_at: `{generated[0]}`" not in SUMMARY_MD.read_text(encoding="utf-8"):
        errors.append("markdown generated_at does not match summary")
    if errors:
        for error in errors:
            print(error, file=sys.stderr)
        return 1
    print(f"validated_fixed_confirmation_feature_summary_rows={len(summary)}")
    print(f"validated_fixed_confirmation_feature_detail_rows={len(detail)}")
    print(f"validated_fixed_confirmation_feature_anomaly_rows={len(anomaly)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
