from __future__ import annotations

import math
import sys
from pathlib import Path

import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent))

from build_daily_model_parameter_research import (  # noqa: E402
    DOCS_REVENUE_UNREACTED_FEATURE_CONTRAST_ANOMALY_CSV,
    DOCS_REVENUE_UNREACTED_FEATURE_CONTRAST_CSV,
    DOCS_REVENUE_UNREACTED_FEATURE_CONTRAST_MD,
    REVENUE_UNREACTED_FEATURE_CONTRAST_ANOMALY_CSV,
    REVENUE_UNREACTED_FEATURE_CONTRAST_ANOMALY_HISTORY_CSV,
    REVENUE_UNREACTED_FEATURE_CONTRAST_BINARY_SPECS,
    REVENUE_UNREACTED_FEATURE_CONTRAST_CSV,
    REVENUE_UNREACTED_FEATURE_CONTRAST_DETAIL_CSV,
    REVENUE_UNREACTED_FEATURE_CONTRAST_HISTORY_CSV,
    REVENUE_UNREACTED_FEATURE_CONTRAST_MD,
    REVENUE_UNREACTED_FEATURE_CONTRAST_NUMERIC_SPECS,
)


EXPECTED_BASES = {
    "including_known_anomalies",
    "excluding_known_revenue_and_price_anomalies",
}
DECISION_BASIS = "excluding_known_revenue_and_price_anomalies"
SUMMARY_REQUIRED = {
    "model_id",
    "research_artifact_id",
    "artifact_scope",
    "row_type",
    "feature_id",
    "feature_family",
    "feature_rule",
    "feature_column",
    "feature_independence_status",
    "equivalent_to_feature_id",
    "anomaly_exclusion_basis",
    "decision_basis",
    "entry_rule_id",
    "exit_rule_id",
    "non_overlap_cooldown_days",
    "non_overlap_applied",
    "same_stock_overlap_pair_count",
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
    "sample_count_context",
    "combination_policy",
    "anomaly_interpretation_status",
    "approved_for_daily",
    "production_change",
    "promotion_readiness",
}
DETAIL_REQUIRED = {
    "model_id",
    "research_artifact_id",
    "anomaly_exclusion_basis",
    "decision_basis",
    "stock_id",
    "_revenue_signal_date",
    "_revenue_stock_sequence_index",
    "entry_rule_id",
    "exit_rule_id",
    "realized_return_pct",
    "outcome_label",
    "high_return_8_flag",
    "loss_5_flag",
    "same_stock_non_overlap_included",
    "non_overlap_cooldown_days",
    "known_revenue_or_price_anomaly_flag",
    "feature_context_revenue_anomaly_flag",
    "future_close_max_step_ratio",
    "future_close_max_step_day",
    "future_close_min_step_ratio",
    "future_close_min_step_day",
    "future_close_discontinuity_flag",
    "future_close_discontinuity_reason",
}
ANOMALY_REQUIRED = {
    "model_id",
    "research_artifact_id",
    "anomaly_exclusion_basis",
    "decision_basis",
    "known_anomaly_count_in_source",
    "accepted_trade_count",
    "same_stock_overlap_pair_count",
    "max_realized_return_pct",
    "max_return_stock_id",
    "max_return_signal_date",
    "min_realized_return_pct",
    "min_return_stock_id",
    "min_return_signal_date",
    "return_abs_ge80_count",
    "return_path_discontinuity_count_after_non_overlap",
    "return_path_discontinuity_count_excluded",
    "return_path_discontinuity_count_in_metric_sample",
    "top1_abs_return_share_pct",
    "top5_abs_return_share_pct",
    "avg_realized_return_pct",
    "median_realized_return_pct",
    "avg_without_max_min_pct",
    "trimmed_1pct_avg_return_pct",
    "potential_return_dominance_flag",
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


def close_enough(actual: object, expected: float, *, tolerance: float = 0.011) -> bool:
    parsed = number(actual)
    return not math.isnan(parsed) and abs(parsed - expected) <= tolerance


def rate(count: int, total: int) -> float:
    return round(count / total * 100.0, 2) if total else math.nan


def validate_mirror(left: Path, right: Path, errors: list[str]) -> None:
    if not left.exists() or not right.exists():
        errors.append(f"missing mirror pair: {left} / {right}")
    elif left.read_bytes() != right.read_bytes():
        errors.append(f"mirror mismatch: {left} / {right}")


def outcome_metrics(part: pd.DataFrame) -> dict[str, float | int]:
    realized = pd.to_numeric(part["realized_return_pct"], errors="coerce").dropna()
    wins = realized.ge(5.0)
    neutral = realized.ge(0.0) & realized.lt(5.0)
    failure = realized.lt(0.0)
    high8 = realized.ge(8.0)
    loss5 = realized.le(-5.0)
    return {
        "accepted_trade_count": len(realized),
        "win_count": int(wins.sum()),
        "neutral_count": int(neutral.sum()),
        "failure_count": int(failure.sum()),
        "win_rate_pct": rate(int(wins.sum()), len(realized)),
        "neutral_rate_pct": rate(int(neutral.sum()), len(realized)),
        "failure_rate_pct": rate(int(failure.sum()), len(realized)),
        "avg_realized_return_pct": round(float(realized.mean()), 2) if len(realized) else math.nan,
        "median_realized_return_pct": round(float(realized.median()), 2) if len(realized) else math.nan,
        "high_return_8_count": int(high8.sum()),
        "high_return_8_rate_pct": rate(int(high8.sum()), len(realized)),
        "loss_5_count": int(loss5.sum()),
        "loss_5_rate_pct": rate(int(loss5.sum()), len(realized)),
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
                errors.append(f"{label} {column} mismatch: {row.get(column)} != {expected_value}")
        elif math.isnan(float(expected_value)):
            if not math.isnan(number(row.get(column))):
                errors.append(f"{label} {column} must be blank when no mature feature rows exist")
        elif not close_enough(row.get(column), float(expected_value)):
            errors.append(f"{label} {column} mismatch: {row.get(column)} != {expected_value}")


def validate_non_overlap(detail: pd.DataFrame, errors: list[str]) -> None:
    if not boolish(detail["same_stock_non_overlap_included"]).all():
        errors.append("detail must contain accepted same-stock non-overlap rows only")
    if pd.to_numeric(detail["non_overlap_cooldown_days"], errors="coerce").ne(20).any():
        errors.append("detail non_overlap_cooldown_days must equal 20")
    for basis, basis_part in detail.groupby("anomaly_exclusion_basis", sort=False):
        for stock_id, stock_part in basis_part.groupby("stock_id", sort=False):
            sequence = (
                pd.to_numeric(stock_part["_revenue_stock_sequence_index"], errors="coerce")
                .dropna()
                .sort_values()
                .astype(int)
                .tolist()
            )
            for left, right in zip(sequence, sequence[1:]):
                if right <= left + 20:
                    errors.append(f"same-stock overlap remains: basis={basis} stock={stock_id} {left}->{right}")


def validate_summary(summary: pd.DataFrame, detail: pd.DataFrame, anomaly: pd.DataFrame) -> list[str]:
    errors: list[str] = []
    missing = SUMMARY_REQUIRED - set(summary.columns)
    if missing:
        return [f"feature contrast summary missing columns: {sorted(missing)}"]
    if summary.empty:
        return ["feature contrast summary is empty"]
    if set(summary["model_id"]) != {"revenue_unreacted_range"}:
        errors.append("summary model_id must be revenue_unreacted_range")
    if set(summary["research_artifact_id"]) != {"revenue_unreacted_range_feature_contrast_audit"}:
        errors.append("summary research_artifact_id mismatch")
    if set(summary["anomaly_exclusion_basis"]) != EXPECTED_BASES:
        errors.append("summary must contain both anomaly bases")
    if boolish(summary["approved_for_daily"]).any() or set(summary["production_change"]) != {"none"}:
        errors.append("feature contrast summary must remain research-only with production_change=none")
    if set(summary["entry_rule_id"]) != {"signal_date_close_condition_next_open_entry"}:
        errors.append("summary entry rule drifted from close-confirmed next-open entry")
    if set(summary["exit_rule_id"]) != {"d20_close_no_stop"}:
        errors.append("summary exit rule drifted from D+20 close no-stop basis")
    if set(summary["combination_policy"]) != {"single_features_only_in_this_audit_no_arbitrary_condition_stacking"}:
        errors.append("summary must forbid arbitrary combination stacking")
    if set(summary["sample_count_context"]) != {"reported_not_a_disqualifier_non_overlap_enforced"}:
        errors.append("summary must not use sample count alone as a disqualifier")
    if pd.to_numeric(summary["same_stock_overlap_pair_count"], errors="coerce").ne(0).any():
        errors.append("summary same_stock_overlap_pair_count must be zero")

    expected_binary = {str(spec["feature_id"]) for spec in REVENUE_UNREACTED_FEATURE_CONTRAST_BINARY_SPECS}
    expected_numeric = {str(spec[1]) for spec in REVENUE_UNREACTED_FEATURE_CONTRAST_NUMERIC_SPECS}
    anomaly_status = anomaly.set_index("anomaly_exclusion_basis")["interpretation_status"].to_dict()
    for basis in EXPECTED_BASES:
        basis_summary = summary[summary["anomaly_exclusion_basis"].eq(basis)]
        basis_detail = detail[detail["anomaly_exclusion_basis"].eq(basis)]
        baseline_rows = basis_summary[basis_summary["row_type"].eq("baseline")]
        if len(baseline_rows) != 1:
            errors.append(f"basis={basis} must have exactly one baseline row")
            continue
        baseline = baseline_rows.iloc[0]
        validate_outcome_row(baseline, basis_detail, f"basis={basis} baseline", errors)
        if safe_set := set(basis_summary["anomaly_interpretation_status"]):
            if safe_set != {anomaly_status.get(basis, "")}:
                errors.append(f"basis={basis} anomaly status does not match anomaly audit")

        binary_rows = basis_summary[basis_summary["row_type"].eq("binary_feature")]
        if set(binary_rows["feature_id"]) != expected_binary:
            errors.append(f"basis={basis} binary feature coverage mismatch")
        prior_masks: list[tuple[str, pd.Series]] = []
        binary_rows = binary_rows.assign(
            _feature_order_numeric=pd.to_numeric(binary_rows["feature_order"], errors="coerce")
        ).sort_values(["_feature_order_numeric", "feature_id"], kind="mergesort")
        for _, row in binary_rows.iterrows():
            feature_id = row["feature_id"]
            feature_column = row["feature_column"]
            if feature_column not in basis_detail.columns:
                errors.append(f"basis={basis} feature={feature_id} missing detail column {feature_column}")
                continue
            feature_mask = boolish(basis_detail[feature_column])
            has_hits = bool(feature_mask.any())
            equivalent_to = (
                next(
                    (prior_feature_id for prior_feature_id, prior_mask in prior_masks if feature_mask.equals(prior_mask)),
                    "",
                )
                if has_hits
                else ""
            )
            if has_hits:
                prior_masks.append((feature_id, feature_mask))
            expected_independence = (
                "no_observed_hits_not_evaluable"
                if not has_hits
                else "duplicate_mask_not_independent_evidence"
                if equivalent_to
                else "distinct_observed_mask"
            )
            if row["feature_independence_status"] != expected_independence:
                errors.append(f"basis={basis} feature={feature_id} independence status mismatch")
            if row["equivalent_to_feature_id"] != equivalent_to:
                errors.append(f"basis={basis} feature={feature_id} equivalent feature id mismatch")
            selected = basis_detail[feature_mask]
            validate_outcome_row(row, selected, f"basis={basis} feature={feature_id}", errors)
            realized = pd.to_numeric(basis_detail["realized_return_pct"], errors="coerce")
            high_mask = realized.ge(8.0)
            win_mask = realized.ge(5.0)
            failure_mask = realized.lt(0.0)
            expected_values = {
                "feature_hit_count": int(feature_mask.sum()),
                "high_return_group_count": int(high_mask.sum()),
                "high_return_feature_hit_count": int((feature_mask & high_mask).sum()),
                "high_return_feature_hit_rate_pct": rate(int((feature_mask & high_mask).sum()), int(high_mask.sum())),
                "win_group_count": int(win_mask.sum()),
                "win_feature_hit_count": int((feature_mask & win_mask).sum()),
                "win_feature_hit_rate_pct": rate(int((feature_mask & win_mask).sum()), int(win_mask.sum())),
                "failure_group_count": int(failure_mask.sum()),
                "failure_feature_hit_count": int((feature_mask & failure_mask).sum()),
                "failure_feature_hit_rate_pct": rate(int((feature_mask & failure_mask).sum()), int(failure_mask.sum())),
            }
            for column, expected_value in expected_values.items():
                if column.endswith("_count"):
                    if int(number(row.get(column, -1))) != int(expected_value):
                        errors.append(f"basis={basis} feature={feature_id} {column} mismatch")
                elif not math.isnan(float(expected_value)) and not close_enough(row.get(column), float(expected_value)):
                    errors.append(f"basis={basis} feature={feature_id} {column} mismatch")
            high_share = float(expected_values["high_return_feature_hit_rate_pct"])
            failure_share = float(expected_values["failure_feature_hit_rate_pct"])
            if not math.isnan(high_share) and not math.isnan(failure_share):
                if not close_enough(row.get("high_return_minus_failure_hit_rate_pct"), round(high_share - failure_share, 2)):
                    errors.append(f"basis={basis} feature={feature_id} discrimination delta mismatch")

        numeric_rows = basis_summary[basis_summary["row_type"].eq("numeric_feature")]
        if set(numeric_rows["feature_id"]) != expected_numeric:
            errors.append(f"basis={basis} numeric feature coverage mismatch")
        for _, row in numeric_rows.iterrows():
            column = row["feature_column"]
            if column not in basis_detail.columns:
                errors.append(f"basis={basis} numeric feature missing detail column {column}")
                continue
            values = pd.to_numeric(basis_detail[column], errors="coerce")
            realized = pd.to_numeric(basis_detail["realized_return_pct"], errors="coerce")
            for prefix, mask in {
                "high_return": realized.ge(8.0),
                "win": realized.ge(5.0),
                "failure": realized.lt(0.0),
            }.items():
                group = values[mask].dropna()
                if len(group):
                    if not close_enough(row.get(f"{prefix}_feature_mean"), round(float(group.mean()), 2)):
                        errors.append(f"basis={basis} numeric={row['feature_id']} {prefix} mean mismatch")
                    if not close_enough(row.get(f"{prefix}_feature_median"), round(float(group.median()), 2)):
                        errors.append(f"basis={basis} numeric={row['feature_id']} {prefix} median mismatch")
    return errors


def validate_detail(detail: pd.DataFrame) -> list[str]:
    errors: list[str] = []
    missing = DETAIL_REQUIRED - set(detail.columns)
    if missing:
        return [f"feature contrast detail missing columns: {sorted(missing)}"]
    if detail.empty:
        return ["feature contrast detail is empty"]
    if set(detail["anomaly_exclusion_basis"]) != EXPECTED_BASES:
        errors.append("detail must contain both anomaly bases")
    if set(detail["entry_rule_id"]) != {"signal_date_close_condition_next_open_entry"}:
        errors.append("detail entry rule mismatch")
    if set(detail["exit_rule_id"]) != {"d20_close_no_stop"}:
        errors.append("detail exit rule mismatch")
    decision = detail[detail["anomaly_exclusion_basis"].eq(DECISION_BASIS)]
    if boolish(decision["known_revenue_or_price_anomaly_flag"]).any():
        errors.append("decision-basis detail contains a known revenue or price anomaly")
    if boolish(decision["feature_context_revenue_anomaly_flag"]).any():
        errors.append("decision-basis detail contains a lagged monthly-revenue context anomaly")
    if boolish(decision["future_close_discontinuity_flag"]).any():
        errors.append("decision-basis detail contains a future close-path discontinuity")
    if not boolish(decision["decision_basis"]).all():
        errors.append("decision-basis rows must set decision_basis=True")
    nondecision = detail[~detail["anomaly_exclusion_basis"].eq(DECISION_BASIS)]
    if boolish(nondecision["decision_basis"]).any():
        errors.append("including-anomaly rows must not be marked as decision basis")
    realized = pd.to_numeric(detail["realized_return_pct"], errors="coerce")
    expected_labels = pd.Series("failure", index=detail.index)
    expected_labels = expected_labels.mask(realized.ge(0.0) & realized.lt(5.0), "neutral")
    expected_labels = expected_labels.mask(realized.ge(5.0), "win")
    if not detail["outcome_label"].eq(expected_labels).all():
        errors.append("detail outcome_label does not match win/neutral/failure definitions")
    validate_non_overlap(detail, errors)
    return errors


def validate_anomaly(anomaly: pd.DataFrame, detail: pd.DataFrame) -> list[str]:
    errors: list[str] = []
    missing = ANOMALY_REQUIRED - set(anomaly.columns)
    if missing:
        return [f"feature contrast anomaly audit missing columns: {sorted(missing)}"]
    if set(anomaly["anomaly_exclusion_basis"]) != EXPECTED_BASES or len(anomaly) != 2:
        errors.append("anomaly audit must have exactly one row per anomaly basis")
    if boolish(anomaly["approved_for_daily"]).any() or set(anomaly["production_change"]) != {"none"}:
        errors.append("anomaly audit must remain research-only")
    for _, row in anomaly.iterrows():
        basis = row["anomaly_exclusion_basis"]
        part = detail[detail["anomaly_exclusion_basis"].eq(basis)]
        realized = pd.to_numeric(part["realized_return_pct"], errors="coerce").dropna().sort_values()
        if len(realized) != int(number(row["accepted_trade_count"])):
            errors.append(f"basis={basis} anomaly accepted_trade_count mismatch")
            continue
        max_index = realized.idxmax()
        min_index = realized.idxmin()
        if not close_enough(row["max_realized_return_pct"], float(realized.loc[max_index]), tolerance=0.00011):
            errors.append(f"basis={basis} max return mismatch")
        if not close_enough(row["min_realized_return_pct"], float(realized.loc[min_index]), tolerance=0.00011):
            errors.append(f"basis={basis} min return mismatch")
        if row["max_return_stock_id"] != str(part.loc[max_index, "stock_id"]):
            errors.append(f"basis={basis} max-return stock mismatch")
        if row["min_return_stock_id"] != str(part.loc[min_index, "stock_id"]):
            errors.append(f"basis={basis} min-return stock mismatch")
        absolute = realized.abs().sort_values(ascending=False)
        total = float(absolute.sum())
        top1 = round(float(absolute.iloc[:1].sum()) / total * 100.0, 2) if total else 0.0
        top5 = round(float(absolute.iloc[:5].sum()) / total * 100.0, 2) if total else 0.0
        if not close_enough(row["top1_abs_return_share_pct"], top1):
            errors.append(f"basis={basis} top1 absolute-return share mismatch")
        if not close_enough(row["top5_abs_return_share_pct"], top5):
            errors.append(f"basis={basis} top5 absolute-return share mismatch")
        remaining_discontinuities = int(boolish(part["future_close_discontinuity_flag"]).sum())
        reported_total_discontinuities = int(number(row["return_path_discontinuity_count_after_non_overlap"]))
        reported_excluded_discontinuities = int(number(row["return_path_discontinuity_count_excluded"]))
        reported_remaining_discontinuities = int(number(row["return_path_discontinuity_count_in_metric_sample"]))
        if reported_remaining_discontinuities != remaining_discontinuities:
            errors.append(f"basis={basis} return-path discontinuity metric-sample count mismatch")
        if basis == DECISION_BASIS:
            if reported_remaining_discontinuities != 0:
                errors.append("decision basis must remove all detected close-path discontinuities")
            if reported_excluded_discontinuities != reported_total_discontinuities:
                errors.append("decision basis must report every detected close-path discontinuity as excluded")
        else:
            if reported_excluded_discontinuities != 0:
                errors.append("including-anomaly basis must not claim close-path discontinuities were excluded")
            if reported_remaining_discontinuities != reported_total_discontinuities:
                errors.append("including-anomaly basis close-path discontinuity count mismatch")
        expected_dominance = remaining_discontinuities > 0 or top1 >= 10.0 or top5 >= 30.0
        if boolish(pd.Series([row["potential_return_dominance_flag"]])).iloc[0] != expected_dominance:
            errors.append(f"basis={basis} potential_return_dominance_flag mismatch")
        if int(number(row["same_stock_overlap_pair_count"])) != 0:
            errors.append(f"basis={basis} anomaly audit overlap_pair_count must be zero")
        status = row["interpretation_status"]
        if basis == DECISION_BASIS:
            expected_status = (
                "blocked_pending_extreme_return_row_review" if expected_dominance else "anomaly_check_pass"
            )
            if status != expected_status:
                errors.append("decision-basis anomaly audit interpretation status mismatch")
        if basis != DECISION_BASIS and status != "not_decision_basis_known_anomalies_included":
            errors.append("including-anomaly audit must be explicitly non-decision-basis")
    return errors


def validate_frames(summary: pd.DataFrame, detail: pd.DataFrame, anomaly: pd.DataFrame) -> list[str]:
    errors = validate_detail(detail)
    errors.extend(validate_anomaly(anomaly, detail))
    errors.extend(validate_summary(summary, detail, anomaly))
    return errors


def main() -> int:
    errors: list[str] = []
    for left, right in [
        (REVENUE_UNREACTED_FEATURE_CONTRAST_CSV, DOCS_REVENUE_UNREACTED_FEATURE_CONTRAST_CSV),
        (REVENUE_UNREACTED_FEATURE_CONTRAST_ANOMALY_CSV, DOCS_REVENUE_UNREACTED_FEATURE_CONTRAST_ANOMALY_CSV),
        (REVENUE_UNREACTED_FEATURE_CONTRAST_MD, DOCS_REVENUE_UNREACTED_FEATURE_CONTRAST_MD),
        (REVENUE_UNREACTED_FEATURE_CONTRAST_CSV, REVENUE_UNREACTED_FEATURE_CONTRAST_HISTORY_CSV),
        (
            REVENUE_UNREACTED_FEATURE_CONTRAST_ANOMALY_CSV,
            REVENUE_UNREACTED_FEATURE_CONTRAST_ANOMALY_HISTORY_CSV,
        ),
    ]:
        validate_mirror(left, right, errors)
    try:
        summary = read_csv(REVENUE_UNREACTED_FEATURE_CONTRAST_CSV)
        detail = read_csv(REVENUE_UNREACTED_FEATURE_CONTRAST_DETAIL_CSV)
        anomaly = read_csv(REVENUE_UNREACTED_FEATURE_CONTRAST_ANOMALY_CSV)
    except (OSError, pd.errors.ParserError) as exc:
        errors.append(f"failed to read feature contrast artifacts: {exc}")
        summary = detail = anomaly = pd.DataFrame()
    if not summary.empty and not detail.empty and not anomaly.empty:
        errors.extend(validate_frames(summary, detail, anomaly))
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1
    print(f"validated_revenue_unreacted_feature_contrast_summary_rows={len(summary)}")
    print(f"validated_revenue_unreacted_feature_contrast_detail_rows={len(detail)}")
    print(f"validated_revenue_unreacted_feature_contrast_anomaly_rows={len(anomaly)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
