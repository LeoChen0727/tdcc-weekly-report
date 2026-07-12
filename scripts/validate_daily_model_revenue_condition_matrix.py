from __future__ import annotations

import sys
from pathlib import Path

import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent))

from build_daily_model_parameter_research import (  # noqa: E402
    ANOMALY_CANDIDATE_SENSITIVITY_BASIS,
    DOCS_PRICE_PULLBACK_REVENUE_CONDITION_MATRIX_CSV,
    DOCS_PRICE_PULLBACK_REVENUE_CONDITION_MATRIX_MD,
    DOCS_REVENUE_UNREACTED_CONDITION_MATRIX_CSV,
    DOCS_REVENUE_UNREACTED_CONDITION_MATRIX_MD,
    PRIMARY_ANOMALY_BASIS,
    PRICE_PULLBACK_REVENUE_CONDITION_MATRIX_CSV,
    PRICE_PULLBACK_REVENUE_CONDITION_MATRIX_MD,
    REVENUE_UNREACTED_CONDITION_MATRIX_CSV,
    REVENUE_UNREACTED_CONDITION_MATRIX_MD,
)


REQUIRED_COLUMNS = {
    "generated_at",
    "model_id",
    "research_artifact_id",
    "matrix_scope",
    "base_condition_id",
    "condition_test_id",
    "condition_family",
    "condition_role_candidate",
    "condition_rule",
    "data_status",
    "revenue_join_source",
    "point_in_time_rule",
    "anomaly_exclusion_basis",
    "decision_basis",
    "sensitivity_basis",
    "exit_rule_id",
    "formal_price_rule_status",
    "entry_rule_id",
    "operation_basis",
    "source_mature_signal_stock_days",
    "accepted_trade_count",
    "baseline_accepted_trade_count",
    "win_rate_pct",
    "neutral_rate_pct",
    "failure_rate_pct",
    "avg_realized_return_pct",
    "median_realized_return_pct",
    "advisory_status",
    "approved_for_daily",
    "production_change",
    "promotion_readiness",
    "promotion_blocker",
}


def read_csv(path: Path) -> pd.DataFrame:
    if not path.exists():
        raise FileNotFoundError(path)
    return pd.read_csv(path, dtype=str, keep_default_na=False)


def validate_mirror(left: Path, right: Path, errors: list[str]) -> None:
    if not left.exists():
        errors.append(f"missing revenue condition matrix artifact: {left.as_posix()}")
        return
    if not right.exists():
        errors.append(f"missing revenue condition matrix mirror: {right.as_posix()}")
        return
    if left.read_bytes() != right.read_bytes():
        errors.append(f"revenue condition matrix mirror differs: {right.as_posix()}")


def validate_matrix(df: pd.DataFrame, *, model_id: str, artifact_id: str) -> list[str]:
    errors: list[str] = []
    missing = REQUIRED_COLUMNS - set(df.columns)
    if missing:
        return [f"{artifact_id} missing columns: {sorted(missing)}"]
    if df.empty:
        return [f"{artifact_id} is empty"]
    if set(df["model_id"].astype(str)) != {model_id}:
        errors.append(f"{artifact_id} has unexpected model_id values: {sorted(set(df['model_id'].astype(str)))}")
    if set(df["research_artifact_id"].astype(str)) != {artifact_id}:
        errors.append(f"{artifact_id} has unexpected research_artifact_id values")
    if not df["matrix_scope"].astype(str).eq("model_specific_revenue_condition_research").all():
        errors.append(f"{artifact_id} must stay model_specific_revenue_condition_research")
    if not df["approved_for_daily"].astype(str).eq("False").all():
        errors.append(f"{artifact_id} must not mark approved_for_daily=True")
    if not df["production_change"].astype(str).eq("none").all():
        errors.append(f"{artifact_id} must not change production")
    if not df["advisory_status"].astype(str).eq("not_production_ready_research_only").all():
        errors.append(f"{artifact_id} must stay research-only")
    if not df["point_in_time_rule"].astype(str).str.contains("source_table_date", regex=False).all():
        errors.append(f"{artifact_id} must document source_table_date point-in-time join")
    if "revenue_context_ready" not in set(df["condition_test_id"].astype(str)):
        errors.append(f"{artifact_id} missing revenue_context_ready coverage row")
    if "revenue_production_strong" not in set(df["condition_test_id"].astype(str)):
        errors.append(f"{artifact_id} missing revenue_production_strong row")
    if df["promotion_blocker"].astype(str).str.strip().eq("").any():
        errors.append(f"{artifact_id} has empty promotion_blocker")
    if set(df["anomaly_exclusion_basis"].astype(str)) != {
        PRIMARY_ANOMALY_BASIS,
        ANOMALY_CANDIDATE_SENSITIVITY_BASIS,
    }:
        errors.append(f"{artifact_id} must publish primary and candidate-exclusion sensitivity bases")
    primary = df[df["anomaly_exclusion_basis"].eq(PRIMARY_ANOMALY_BASIS)]
    sensitivity = df[df["anomaly_exclusion_basis"].eq(ANOMALY_CANDIDATE_SENSITIVITY_BASIS)]
    if not primary["decision_basis"].astype(str).eq("True").all():
        errors.append(f"{artifact_id} primary rows must set decision_basis=True")
    if not sensitivity["sensitivity_basis"].astype(str).eq("True").all():
        errors.append(f"{artifact_id} sensitivity rows must set sensitivity_basis=True")
    return errors


def validate_price_pullback(df: pd.DataFrame) -> list[str]:
    errors = validate_matrix(
        df,
        model_id="price_pullback_23ema",
        artifact_id="price_pullback_23ema_revenue_condition_matrix",
    )
    if df.empty or errors:
        return errors
    if not df["formal_price_rule_status"].astype(str).eq("close_confirmed_candidate").all():
        errors.append("price_pullback_23ema revenue matrix must use close-confirmed candidate operation basis")
    if not df["operation_basis"].astype(str).eq("price_pullback_close_confirmed_candidate_lifecycle_replay").all():
        errors.append("price_pullback_23ema revenue matrix must use lifecycle replay operation basis")
    required_candidate_columns = {
        "revenue_or_price_anomaly_candidate_count_in_sample",
        "revenue_or_price_anomaly_candidate_count_in_baseline",
    }
    missing_candidate_columns = required_candidate_columns - set(df.columns)
    if missing_candidate_columns:
        errors.append(
            "price_pullback_23ema revenue matrix missing anomaly candidate columns: "
            + ", ".join(sorted(missing_candidate_columns))
        )
    else:
        primary = df[df["anomaly_exclusion_basis"].eq(PRIMARY_ANOMALY_BASIS)]
        unresolved = pd.to_numeric(
            primary["revenue_or_price_anomaly_candidate_count_in_sample"], errors="coerce"
        ).fillna(0).gt(0)
        if not primary.loc[unresolved, "promotion_readiness"].eq(
            "blocked_pending_root_cause_anomaly_candidate_review"
        ).all():
            errors.append("price_pullback primary anomaly candidates must block promotion")
    required_turnaround_tests = {
        "latest_yoy_improving_2m",
        "latest_yoy_improving_3m",
        "latest_yoy_turn_positive",
        "latest_yoy_turn_positive_after_2_negative",
        "turn_positive_and_cumulative_improving",
        "latest_improving_2m_and_cumulative_improving",
    }
    missing_turnaround_tests = required_turnaround_tests - set(df["condition_test_id"].astype(str))
    if missing_turnaround_tests:
        errors.append(
            "price_pullback_23ema revenue matrix missing turnaround tests: "
            + ", ".join(sorted(missing_turnaround_tests))
        )
    required_delta_columns = {
        "avg_revenue_latest_yoy_delta_1m_pct_points",
        "median_revenue_latest_yoy_delta_1m_pct_points",
        "avg_revenue_cumulative_yoy_delta_1m_pct_points",
        "median_revenue_cumulative_yoy_delta_1m_pct_points",
    }
    missing_delta_columns = required_delta_columns - set(df.columns)
    if missing_delta_columns:
        errors.append(
            "price_pullback_23ema revenue matrix missing turnaround metric columns: "
            + ", ".join(sorted(missing_delta_columns))
        )
    return errors


def validate_revenue_unreacted(df: pd.DataFrame) -> list[str]:
    errors = validate_matrix(
        df,
        model_id="revenue_unreacted_range",
        artifact_id="revenue_unreacted_range_revenue_condition_matrix",
    )
    if df.empty or errors:
        return errors
    if not df["formal_price_rule_status"].astype(str).eq("research_only_no_formal_operation_contract").all():
        errors.append("revenue_unreacted_range matrix must not claim a formal operation contract")
    if not df["operation_basis"].astype(str).eq("research_only_d20_close_not_operation_contract").all():
        errors.append("revenue_unreacted_range matrix must stay D+20 close advisory")
    required_candidate_columns = {
        "revenue_anomaly_candidate_count_in_sample",
        "revenue_anomaly_candidate_count_in_baseline",
    }
    missing_candidate_columns = required_candidate_columns - set(df.columns)
    if missing_candidate_columns:
        errors.append(
            "revenue_unreacted_range matrix missing anomaly candidate columns: "
            + ", ".join(sorted(missing_candidate_columns))
        )
    else:
        primary = df[df["anomaly_exclusion_basis"].eq(PRIMARY_ANOMALY_BASIS)]
        unresolved = pd.to_numeric(
            primary["revenue_anomaly_candidate_count_in_sample"], errors="coerce"
        ).fillna(0).gt(0)
        if not primary.loc[unresolved, "promotion_readiness"].eq(
            "blocked_pending_root_cause_anomaly_candidate_review"
        ).all():
            errors.append("revenue_unreacted primary anomaly candidates must block promotion")
    return errors


def main() -> int:
    errors: list[str] = []
    validate_mirror(
        PRICE_PULLBACK_REVENUE_CONDITION_MATRIX_CSV,
        DOCS_PRICE_PULLBACK_REVENUE_CONDITION_MATRIX_CSV,
        errors,
    )
    validate_mirror(
        PRICE_PULLBACK_REVENUE_CONDITION_MATRIX_MD,
        DOCS_PRICE_PULLBACK_REVENUE_CONDITION_MATRIX_MD,
        errors,
    )
    validate_mirror(
        REVENUE_UNREACTED_CONDITION_MATRIX_CSV,
        DOCS_REVENUE_UNREACTED_CONDITION_MATRIX_CSV,
        errors,
    )
    validate_mirror(
        REVENUE_UNREACTED_CONDITION_MATRIX_MD,
        DOCS_REVENUE_UNREACTED_CONDITION_MATRIX_MD,
        errors,
    )
    try:
        price_pullback = read_csv(PRICE_PULLBACK_REVENUE_CONDITION_MATRIX_CSV)
    except FileNotFoundError as exc:
        errors.append(f"missing price_pullback revenue condition matrix: {exc}")
        price_pullback = pd.DataFrame()
    try:
        revenue_unreacted = read_csv(REVENUE_UNREACTED_CONDITION_MATRIX_CSV)
    except FileNotFoundError as exc:
        errors.append(f"missing revenue_unreacted revenue condition matrix: {exc}")
        revenue_unreacted = pd.DataFrame()
    if not price_pullback.empty:
        errors.extend(validate_price_pullback(price_pullback))
    if not revenue_unreacted.empty:
        errors.extend(validate_revenue_unreacted(revenue_unreacted))
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1
    print(f"validated_price_pullback_revenue_condition_matrix_rows={len(price_pullback)}")
    print(f"validated_revenue_unreacted_condition_matrix_rows={len(revenue_unreacted)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
    PRIMARY_ANOMALY_BASIS,
