from __future__ import annotations

from pathlib import Path

import pandas as pd

from revenue_unreacted_range_close_confirmation_timing import (
    ANOMALY_CANDIDATE_SENSITIVITY_BASIS,
    ANOMALY_CSV,
    ARTIFACT_ID,
    CONFIRMATION_SPECS,
    CONTROL_SPEC,
    DECISION_BASIS,
    DETAIL_CSV,
    EXIT_CLOCK_SPECS,
    MODEL_ID,
    SUMMARY_CSV,
    SUMMARY_MD,
)


SUMMARY_REQUIRED = {
    "generated_at",
    "model_id",
    "research_artifact_id",
    "row_type",
    "anomaly_exclusion_basis",
    "decision_basis",
    "confirmation_variant_id",
    "confirmation_variant_name_zh",
    "pending_window_days",
    "exit_clock_id",
    "source_signal_count",
    "approved_for_daily",
    "production_change",
    "promotion_readiness",
}

PERFORMANCE_REQUIRED = {
    "pending_episode_count",
    "confirmed_episode_count",
    "unconfirmed_episode_count",
    "not_evaluable_episode_count",
    "confirmation_rate_pct",
    "suppressed_source_signal_count",
    "source_signal_accounted_count",
    "source_signal_accounting_status",
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
    "high_return_8_rate_pct",
    "loss_5_rate_pct",
    "avoided_failure_count",
    "missed_win_count",
    "uses_intraday_operation_price",
}

DETAIL_REQUIRED = {
    "episode_key",
    "model_id",
    "research_artifact_id",
    "decision_basis",
    "stock_id",
    "signal_date",
    "signal_sequence_index",
    "confirmation_variant_id",
    "pending_window_days",
    "exit_clock_id",
    "confirmation_date",
    "confirmation_sequence_index",
    "entry_date",
    "entry_sequence_index",
    "exit_date",
    "exit_sequence_index",
    "realized_return_pct",
    "outcome_label",
    "metric_included",
    "price_path_anomaly_candidate_flag",
    "known_before_entry_open",
    "uses_post_entry_information",
    "full_monthly_revenue_source_table_date",
    "approved_for_daily",
    "production_change",
}

ANOMALY_REQUIRED = {
    "generated_at",
    "model_id",
    "research_artifact_id",
    "row_type",
    "anomaly_exclusion_basis",
    "confirmation_variant_id",
    "pending_window_days",
    "exit_clock_id",
    "accepted_trade_count_before_candidate_sensitivity_exclusion",
    "price_path_anomaly_candidate_count",
    "metric_sample_count",
    "top1_abs_return_share_pct",
    "top5_abs_return_share_pct",
    "trimmed_1pct_avg_return_pct",
    "return_abs_ge80_anomaly_candidate_count",
    "potential_return_dominance_flag",
    "interpretation_status",
    "approved_for_daily",
    "production_change",
}


def _trueish(series: pd.Series) -> pd.Series:
    return series.astype(str).str.strip().str.lower().isin({"true", "1", "yes"})


def _numbers(frame: pd.DataFrame, column: str) -> pd.Series:
    return pd.to_numeric(frame[column], errors="coerce")


def _performance_key(frame: pd.DataFrame) -> set[tuple[str, str, str, str]]:
    return set(
        zip(
            frame["anomaly_exclusion_basis"].astype(str),
            frame["confirmation_variant_id"].astype(str),
            frame["pending_window_days"].astype(str),
            frame["exit_clock_id"].astype(str),
        )
    )


def validate_frames(
    summary: pd.DataFrame,
    detail: pd.DataFrame,
    anomaly: pd.DataFrame,
    markdown_text: str | None = None,
) -> list[str]:
    errors: list[str] = []
    for name, frame, required in (
        ("summary", summary, SUMMARY_REQUIRED),
        ("detail", detail, DETAIL_REQUIRED),
        ("anomaly", anomaly, ANOMALY_REQUIRED),
    ):
        missing = required - set(frame.columns)
        if missing:
            errors.append(f"{name} missing columns: {sorted(missing)}")
        if frame.empty:
            errors.append(f"{name} is empty")
    if errors:
        return errors

    for name, frame in (("summary", summary), ("detail", detail), ("anomaly", anomaly)):
        if set(frame["model_id"].astype(str)) != {MODEL_ID}:
            errors.append(f"{name} has unexpected model_id")
        if set(frame["research_artifact_id"].astype(str)) != {ARTIFACT_ID}:
            errors.append(f"{name} has unexpected research_artifact_id")
        if _trueish(frame["approved_for_daily"]).any():
            errors.append(f"{name} must remain approved_for_daily=False")
        if set(frame["production_change"].astype(str)) != {"none"}:
            errors.append(f"{name} must remain production_change=none")

    summary_timestamps = summary["generated_at"].dropna().astype(str).unique().tolist()
    anomaly_timestamps = anomaly["generated_at"].dropna().astype(str).unique().tolist()
    if len(summary_timestamps) != 1:
        errors.append("summary must contain exactly one generated_at timestamp")
    elif anomaly_timestamps != summary_timestamps:
        errors.append("summary and anomaly artifacts must share generated_at")
    elif markdown_text is not None:
        expected_timestamp_line = f"- generated_at: `{summary_timestamps[0]}`"
        if expected_timestamp_line not in markdown_text:
            errors.append("markdown generated_at must match summary and anomaly artifacts")

    expected_bases = {DECISION_BASIS, ANOMALY_CANDIDATE_SENSITIVITY_BASIS}
    if set(summary["anomaly_exclusion_basis"].astype(str)) != expected_bases:
        errors.append("summary must publish primary and candidate-exclusion sensitivity bases")
    if set(anomaly["anomaly_exclusion_basis"].astype(str)) != expected_bases:
        errors.append("anomaly audit must publish primary and candidate-exclusion sensitivity bases")
    if not _trueish(detail["decision_basis"]).all():
        errors.append("detail rows must all be decision_basis=True")

    performance = summary[summary["row_type"].isin({"control_baseline", "variant_performance"})].copy()
    missing_performance = PERFORMANCE_REQUIRED - set(performance.columns)
    if missing_performance:
        errors.append(f"performance rows missing columns: {sorted(missing_performance)}")
        return errors

    expected_variants = {CONTROL_SPEC.confirmation_variant_id} | {
        spec.confirmation_variant_id for spec in CONFIRMATION_SPECS
    }
    if set(performance["confirmation_variant_id"].astype(str)) != expected_variants:
        errors.append("performance rows do not contain exactly the control plus three research variants")
    expected_exits = {spec.exit_clock_id for spec in EXIT_CLOCK_SPECS}
    variants = performance[performance["row_type"].eq("variant_performance")]
    if set(variants["exit_clock_id"].astype(str)) != expected_exits:
        errors.append("variant performance rows must compare both D+20 exit clocks")

    for _, row in performance.iterrows():
        accepted = int(float(row["accepted_trade_count"]))
        wins = int(float(row["win_count"]))
        neutrals = int(float(row["neutral_count"]))
        failures = int(float(row["failure_count"]))
        if accepted != wins + neutrals + failures:
            errors.append(
                "win/neutral/failure counts do not sum to accepted_trade_count for "
                f"{row['confirmation_variant_id']}:{row['pending_window_days']}:{row['exit_clock_id']}"
            )
        if accepted > 0:
            rate_sum = sum(float(row[column]) for column in ("win_rate_pct", "neutral_rate_pct", "failure_rate_pct"))
            if abs(rate_sum - 100.0) > 0.02:
                errors.append("win/neutral/failure rates must sum to 100%")
        if str(row["source_signal_accounting_status"]) != "pass":
            errors.append("every source signal must be accounted for by one episode or suppression")
        if int(float(row["source_signal_accounted_count"])) != int(float(row["source_signal_count"])):
            errors.append("source signal accounting count mismatch")
        if int(float(row["same_stock_overlap_pair_count"])) != 0:
            errors.append("same-stock overlap must be zero for every replay row")
        intraday = str(row["uses_intraday_operation_price"]).strip().lower()
        if intraday not in {"false", "0"}:
            errors.append("timing audit must not use intraday operation prices")

    decision_control = performance[
        performance["anomaly_exclusion_basis"].eq(DECISION_BASIS)
        & performance["row_type"].eq("control_baseline")
    ]
    if len(decision_control) != 1:
        errors.append("decision basis must contain exactly one direct-entry control row")
    elif str(decision_control.iloc[0].get("control_parity_status", "")) != "pass":
        errors.append("direct-entry control must reproduce the existing feature-contrast baseline")

    partitions = summary[summary["row_type"].eq("source_partition")].copy()
    if partitions.empty:
        errors.append("source partition rows are required")
    else:
        for basis, part in partitions.groupby("anomaly_exclusion_basis", sort=False):
            partition_sum = int(_numbers(part, "partition_count").sum())
            source_counts = set(_numbers(part, "source_signal_count").dropna().astype(int))
            if len(source_counts) != 1 or partition_sum != next(iter(source_counts), -1):
                errors.append(f"source partition does not cover all source signals for {basis}")
            if set(part["source_partition_status"].astype(str)) != {"pass"}:
                errors.append(f"source partition status must pass for {basis}")

    if detail["episode_key"].astype(str).duplicated().any():
        errors.append("detail episode_key values must be unique")
    if _trueish(detail["uses_post_entry_information"]).any():
        errors.append("confirmation timing must not use post-entry information")

    source_date = _numbers(detail, "signal_date")
    revenue_date = _numbers(detail, "full_monthly_revenue_source_table_date")
    dated = source_date.notna() & revenue_date.notna()
    if (revenue_date[dated] > source_date[dated]).any():
        errors.append("monthly revenue source_table_date must be on or before signal_date")

    included = detail[_trueish(detail["metric_included"])].copy()
    if not included.empty:
        confirmation = _numbers(included, "confirmation_sequence_index")
        entry = _numbers(included, "entry_sequence_index")
        exit_sequence = _numbers(included, "exit_sequence_index")
        if not ((confirmation < entry) & (entry <= exit_sequence)).all():
            errors.append("confirmation must precede next-open entry and entry must not follow exit")
        if not _trueish(included["known_before_entry_open"]).all():
            errors.append("every metric-included confirmation must be known before entry open")

        included = included.assign(
            _entry_sequence_numeric=_numbers(included, "entry_sequence_index"),
            _exit_sequence_numeric=_numbers(included, "exit_sequence_index"),
        )
        for _, part in included.sort_values(
            [
                "confirmation_variant_id",
                "pending_window_days",
                "exit_clock_id",
                "stock_id",
                "_entry_sequence_numeric",
            ],
            kind="mergesort",
        ).groupby(
            ["confirmation_variant_id", "pending_window_days", "exit_clock_id", "stock_id"],
            sort=False,
            dropna=False,
        ):
            entries = part["_entry_sequence_numeric"].tolist()
            exits = part["_exit_sequence_numeric"].tolist()
            if any(next_entry <= previous_exit for previous_exit, next_entry in zip(exits, entries[1:])):
                errors.append("detail contains overlapping same-stock accepted trades")
                break

    performance_keys = _performance_key(performance)
    anomaly_keys = _performance_key(anomaly)
    if performance_keys != anomaly_keys:
        errors.append("anomaly rows must map one-to-one to performance rows")
    decision_anomaly = anomaly[anomaly["anomaly_exclusion_basis"].eq(DECISION_BASIS)]
    dominance = _trueish(decision_anomaly["potential_return_dominance_flag"])
    candidate_count = pd.to_numeric(
        decision_anomaly["return_abs_ge80_anomaly_candidate_count"], errors="coerce"
    ).fillna(0)
    candidate_rows = candidate_count.gt(0)
    if (
        candidate_rows
        & ~decision_anomaly["interpretation_status"].eq(
            "blocked_pending_root_cause_anomaly_candidate_review"
        )
    ).any():
        errors.append("decision-basis threshold candidates must block root-cause review")
    if (
        (~candidate_rows)
        & dominance
        & ~decision_anomaly["interpretation_status"].eq(
            "blocked_non_threshold_return_dominance_review"
        )
    ).any():
        errors.append("non-threshold return dominance must block interpretation")
    if (
        (~candidate_rows)
        & (~dominance)
        & ~decision_anomaly["interpretation_status"].eq("anomaly_check_pass")
    ).any():
        errors.append("clean decision-basis anomaly rows must report anomaly_check_pass")

    sensitivity_anomaly = anomaly[
        anomaly["anomaly_exclusion_basis"].eq(ANOMALY_CANDIDATE_SENSITIVITY_BASIS)
    ]
    if not sensitivity_anomaly["interpretation_status"].eq(
        "sensitivity_only_not_anomaly_disposition"
    ).all():
        errors.append("candidate-exclusion basis must be labeled sensitivity-only")

    return errors


def _read(path: Path) -> pd.DataFrame:
    if not path.exists():
        raise SystemExit(f"ERROR: missing required artifact: {path}")
    return pd.read_csv(path, dtype=str, keep_default_na=False)


def main() -> int:
    summary = _read(SUMMARY_CSV)
    detail = _read(DETAIL_CSV)
    anomaly = _read(ANOMALY_CSV)
    if not SUMMARY_MD.exists():
        raise SystemExit(f"ERROR: missing required artifact: {SUMMARY_MD}")
    markdown_text = SUMMARY_MD.read_text(encoding="utf-8")
    errors = validate_frames(summary, detail, anomaly, markdown_text)
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1
    print(f"validated_revenue_unreacted_close_confirmation_summary_rows={len(summary)}")
    print(f"validated_revenue_unreacted_close_confirmation_detail_rows={len(detail)}")
    print(f"validated_revenue_unreacted_close_confirmation_anomaly_rows={len(anomaly)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
