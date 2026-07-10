import sys
from pathlib import Path

import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent))

from build_daily_model_parameter_research import (  # noqa: E402
    DOCS_REVENUE_UNREACTED_OPERATION_CANDIDATE_MATRIX_CSV,
    DOCS_REVENUE_UNREACTED_OPERATION_CANDIDATE_MATRIX_MD,
    REVENUE_UNREACTED_OPERATION_CANDIDATE_MATRIX_CSV,
    REVENUE_UNREACTED_OPERATION_CANDIDATE_MATRIX_MD,
)


REQUIRED_COLUMNS = {
    "generated_at",
    "model_id",
    "research_artifact_id",
    "matrix_scope",
    "condition_test_id",
    "condition_family",
    "condition_role_candidate",
    "condition_rule",
    "point_in_time_rule",
    "anomaly_exclusion_basis",
    "entry_rule_id",
    "confirmation_rule_id",
    "entry_rule",
    "exit_rule_id",
    "holding_window_days",
    "exit_rule",
    "stop_rule_id",
    "stop_rule",
    "operation_basis",
    "formal_price_rule_status",
    "win_definition",
    "neutral_definition",
    "failure_definition",
    "metric_basis",
    "source_mature_signal_stock_days",
    "non_overlap_cooldown_days",
    "non_overlap_applied",
    "same_stock_overlap_pair_count",
    "accepted_signal_count_after_non_overlap",
    "suppressed_signal_count",
    "accepted_trade_count",
    "baseline_accepted_trade_count",
    "accepted_trade_share_of_baseline_pct",
    "win_rate_pct",
    "neutral_rate_pct",
    "failure_rate_pct",
    "avg_realized_return_pct",
    "median_realized_return_pct",
    "stop_trigger_count",
    "stop_trigger_rate_pct",
    "meets_win_return_metric",
    "decision_hint",
    "advisory_status",
    "approved_for_daily",
    "production_change",
    "promotion_readiness",
    "promotion_blocker",
}

REQUIRED_EXIT_RULES = {
    "d10_close_no_stop",
    "d15_close_no_stop",
    "d20_close_no_stop",
    "d10_close_ma20_ema23_4d_stop",
    "d15_close_ma20_ema23_4d_stop",
    "d20_close_ma20_ema23_4d_stop",
}

REQUIRED_CONDITIONS = {
    "revenue_context_ready",
    "revenue_production_strong",
    "latest30_and_cumulative20",
    "strong_revenue_range23_width_le20",
    "strong_revenue_above_ma20_ema23",
    "strong_revenue_tdcc_high_thresholds_up",
}


def read_csv(path: Path) -> pd.DataFrame:
    if not path.exists():
        raise FileNotFoundError(path)
    return pd.read_csv(path, dtype=str, keep_default_na=False)


def validate_mirror(left: Path, right: Path, errors: list[str]) -> None:
    if not left.exists():
        errors.append(f"missing revenue operation candidate matrix artifact: {left.as_posix()}")
        return
    if not right.exists():
        errors.append(f"missing revenue operation candidate matrix mirror: {right.as_posix()}")
        return
    if left.read_bytes() != right.read_bytes():
        errors.append(f"revenue operation candidate matrix mirror differs: {right.as_posix()}")


def validate_matrix(df: pd.DataFrame) -> list[str]:
    errors: list[str] = []
    missing = REQUIRED_COLUMNS - set(df.columns)
    if missing:
        return [f"revenue_unreacted_range_operation_candidate_matrix missing columns: {sorted(missing)}"]
    if df.empty:
        return ["revenue_unreacted_range_operation_candidate_matrix is empty"]

    if set(df["model_id"].astype(str)) != {"revenue_unreacted_range"}:
        errors.append(
            "revenue_unreacted_range_operation_candidate_matrix has unexpected model_id values: "
            + ", ".join(sorted(set(df["model_id"].astype(str))))
        )
    if set(df["research_artifact_id"].astype(str)) != {"revenue_unreacted_range_operation_candidate_matrix"}:
        errors.append("operation candidate matrix has unexpected research_artifact_id values")
    if not df["matrix_scope"].astype(str).eq("model_specific_operation_candidate_research").all():
        errors.append("operation candidate matrix must stay model_specific_operation_candidate_research")
    if not df["advisory_status"].astype(str).eq("not_production_ready_research_only").all():
        errors.append("operation candidate matrix must stay research-only")
    if not df["approved_for_daily"].astype(str).eq("False").all():
        errors.append("operation candidate matrix must not mark approved_for_daily=True")
    if not df["production_change"].astype(str).eq("none").all():
        errors.append("operation candidate matrix must not change production")
    if not df["formal_price_rule_status"].astype(str).eq("research_only_no_formal_operation_contract").all():
        errors.append("operation candidate matrix must not claim a formal operation contract")
    if not df["operation_basis"].astype(str).eq("research_only_close_confirmed_operation_candidate").all():
        errors.append("operation candidate matrix must use close-confirmed research operation candidate basis")
    if not df["point_in_time_rule"].astype(str).str.contains("source_table_date", regex=False).all():
        errors.append("operation candidate matrix must document source_table_date point-in-time joins")
    if set(df["anomaly_exclusion_basis"].astype(str)) != {
        "including_numerical_anomalies",
        "excluding_revenue_numerical_anomalies",
    }:
        errors.append("operation candidate matrix must include both including and excluding anomaly bases")
    missing_exits = REQUIRED_EXIT_RULES - set(df["exit_rule_id"].astype(str))
    if missing_exits:
        errors.append("operation candidate matrix missing exit rules: " + ", ".join(sorted(missing_exits)))
    missing_conditions = REQUIRED_CONDITIONS - set(df["condition_test_id"].astype(str))
    if missing_conditions:
        errors.append("operation candidate matrix missing condition tests: " + ", ".join(sorted(missing_conditions)))
    if not df["non_overlap_applied"].astype(str).eq("True").all():
        errors.append("operation candidate matrix must apply same-stock non-overlap")
    overlap = pd.to_numeric(df["same_stock_overlap_pair_count"], errors="coerce").fillna(-1)
    if not overlap.eq(0).all():
        errors.append("operation candidate matrix has same-stock overlap pairs after non-overlap enforcement")
    if not df["sample_count_context"].astype(str).str.contains("not_a_disqualifier", regex=False).all():
        errors.append("operation candidate matrix must state that sample count is reported, not a disqualifier")

    text_surface = (
        df["entry_rule"].astype(str)
        + " "
        + df["exit_rule"].astype(str)
        + " "
        + df["stop_rule"].astype(str)
        + " "
        + df["metric_basis"].astype(str)
    ).str.lower()
    if text_surface.str.contains("intraday", regex=False).any():
        errors.append("operation candidate matrix must not use intraday operation wording")
    if not df.loc[df["stop_rule_id"].astype(str).ne("no_stop"), "stop_rule"].astype(str).str.contains(
        "consecutive closes",
        regex=False,
    ).all():
        errors.append("stop-rule rows must be close-confirmed")
    if not df.loc[df["stop_rule_id"].astype(str).ne("no_stop"), "stop_rule"].astype(str).str.contains(
        "next trading day open",
        regex=False,
    ).all():
        errors.append("stop-rule rows must execute on next trading day open")

    return errors


def main() -> int:
    errors: list[str] = []
    validate_mirror(
        REVENUE_UNREACTED_OPERATION_CANDIDATE_MATRIX_CSV,
        DOCS_REVENUE_UNREACTED_OPERATION_CANDIDATE_MATRIX_CSV,
        errors,
    )
    validate_mirror(
        REVENUE_UNREACTED_OPERATION_CANDIDATE_MATRIX_MD,
        DOCS_REVENUE_UNREACTED_OPERATION_CANDIDATE_MATRIX_MD,
        errors,
    )
    try:
        matrix = read_csv(REVENUE_UNREACTED_OPERATION_CANDIDATE_MATRIX_CSV)
    except FileNotFoundError as exc:
        errors.append(f"missing revenue operation candidate matrix: {exc}")
        matrix = pd.DataFrame()
    if not matrix.empty:
        errors.extend(validate_matrix(matrix))
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1
    print(f"validated_revenue_unreacted_operation_candidate_matrix_rows={len(matrix)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
