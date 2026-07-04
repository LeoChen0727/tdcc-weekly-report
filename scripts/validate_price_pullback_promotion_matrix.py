from __future__ import annotations

import sys
from pathlib import Path

import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent))

from build_daily_model_parameter_research import (  # noqa: E402
    DOCS_PRICE_PULLBACK_PROMOTION_MATRIX_CSV,
    DOCS_PRICE_PULLBACK_PROMOTION_MATRIX_MD,
    PRICE_PULLBACK_PROMOTION_MATRIX_CSV,
    PRICE_PULLBACK_PROMOTION_MATRIX_MD,
)


REQUIRED_COLUMNS = {
    "generated_at",
    "model_id",
    "model_name_zh",
    "research_artifact_id",
    "matrix_scope",
    "matrix_order",
    "promotion_candidate_id",
    "promotion_axis",
    "source_artifact_id",
    "source_selector",
    "source_metric_basis",
    "proposed_contract_role",
    "proposed_score_points",
    "condition_rule",
    "plain_conclusion_zh",
    "data_status",
    "sample_status",
    "anomaly_exclusion_basis",
    "known_metric_exception_count_in_sample",
    "known_metric_exception_count_in_baseline",
    "known_metric_exception_ids",
    "exit_rule_id",
    "formal_price_rule_status",
    "entry_rule_id",
    "source_mature_signal_stock_days",
    "accepted_trade_count",
    "accepted_avg_trades_per_research_day",
    "accepted_trade_share_of_baseline_pct",
    "win_rate_pct",
    "neutral_rate_pct",
    "failure_rate_pct",
    "avg_realized_return_pct",
    "median_realized_return_pct",
    "high_return_10_rate_pct",
    "loss_5_rate_pct",
    "delta_vs_base_win_rate_pct",
    "delta_vs_base_failure_rate_pct",
    "delta_vs_base_avg_realized_return_pct",
    "metric_surface_use",
    "pdf_metric_readiness",
    "advisory_status",
    "approved_for_daily",
    "production_change",
    "production_decision_status",
    "promotion_readiness",
    "promotion_blocker",
}

REQUIRED_CANDIDATE_IDS = {
    "baseline:production_proxy_lifecycle_replay",
    "base_package:v1_gate_return20_tdcc_high_obv",
    "supporting_gate:return20_0_25",
    "supporting_gate:tdcc_high_thresholds_up",
    "supporting_gate:obv_above_ma20",
    "revenue_package:latest30_and_cumulative20",
    "revenue_package:latest_revenue_yoy_ge50",
    "revenue_reject:latest_yoy_turn_positive_after_2_negative",
    "high_return_score:score_ge3",
    "score_component:volume_red_or_solid_red_risk",
    "deferred_context:theme_leadership",
}
EXPECTED_EXIT_RULE_ID = "close_prev20_high_break_next_open"
PRICE_PULLBACK_EXCLUDING_EXCEPTION_BASIS = "excluding_known_data_quality_exceptions"
REVENUE_EXCLUDING_EXCEPTION_BASIS = "excluding_known_price_or_revenue_anomalies"
FORBIDDEN_PROMOTION_BASIS_TEXT = {
    "close_prev20_break_then_tp5_or_5ma_next_open",
    "close_prev20_break_then_tp8_or_5ma_next_open",
    "close_prev20_break_then_tp10_or_5ma_next_open",
    "close-confirmed continuation exit",
}


def read_csv(path: Path) -> pd.DataFrame:
    if not path.exists():
        raise FileNotFoundError(path)
    return pd.read_csv(path, dtype=str, keep_default_na=False)


def validate_mirror(left: Path, right: Path, errors: list[str]) -> None:
    if not left.exists():
        errors.append(f"missing price_pullback promotion matrix artifact: {left.as_posix()}")
        return
    if not right.exists():
        errors.append(f"missing price_pullback promotion matrix mirror: {right.as_posix()}")
        return
    if left.read_bytes() != right.read_bytes():
        errors.append(f"price_pullback promotion matrix mirror differs: {right.as_posix()}")


def validate_matrix(df: pd.DataFrame) -> list[str]:
    errors: list[str] = []
    missing = REQUIRED_COLUMNS - set(df.columns)
    if missing:
        return [f"price_pullback_23ema_promotion_matrix missing columns: {sorted(missing)}"]
    if df.empty:
        return ["price_pullback_23ema_promotion_matrix is empty"]
    if set(df["model_id"].astype(str)) != {"price_pullback_23ema"}:
        errors.append("promotion matrix has unexpected model_id values")
    if set(df["research_artifact_id"].astype(str)) != {"price_pullback_23ema_promotion_matrix"}:
        errors.append("promotion matrix has unexpected research_artifact_id values")
    if not df["matrix_scope"].astype(str).eq("research_only_promotion_decision_matrix").all():
        errors.append("promotion matrix must stay research_only_promotion_decision_matrix")
    if not df["approved_for_daily"].astype(str).eq("False").all():
        errors.append("promotion matrix must not approve daily production")
    if not df["production_change"].astype(str).eq("none").all():
        errors.append("promotion matrix must not change production")
    if not df["production_decision_status"].astype(str).eq("research_only_not_approved").all():
        errors.append("promotion matrix must not mark any row production-approved")
    if not df["advisory_status"].astype(str).eq("not_production_ready_research_only").all():
        errors.append("promotion matrix must remain research-only")
    if not df["pdf_metric_readiness"].astype(str).str.contains("blocked_until_formal_promotion", regex=False).all():
        errors.append("promotion matrix metrics must stay blocked from PDF use")
    if df["promotion_blocker"].astype(str).str.strip().eq("").any():
        errors.append("promotion matrix has empty promotion_blocker")
    if df["proposed_contract_role"].astype(str).str.strip().eq("").any():
        errors.append("promotion matrix has empty proposed_contract_role")
    metric_rows = df["accepted_trade_count"].astype(str).str.strip().ne("")
    allowed_exception_basis = {
        PRICE_PULLBACK_EXCLUDING_EXCEPTION_BASIS,
        REVENUE_EXCLUDING_EXCEPTION_BASIS,
    }
    unexpected_basis = sorted(
        set(df.loc[metric_rows, "anomaly_exclusion_basis"].astype(str)) - allowed_exception_basis
    )
    if unexpected_basis:
        errors.append(
            "promotion matrix metric rows must use excluding anomaly basis only; "
            f"unexpected anomaly_exclusion_basis values: {unexpected_basis}"
        )
    forbidden_basis_rows = df["anomaly_exclusion_basis"].astype(str).isin(
        {
            "including_data_quality_exceptions",
            "including_numerical_anomalies",
        }
    )
    if forbidden_basis_rows.any():
        errors.append("promotion matrix must not use including-anomaly metric rows")
    if df.loc[metric_rows, "known_metric_exception_count_in_baseline"].astype(str).str.strip().eq("").any():
        errors.append("promotion matrix metric rows must expose baseline exception counts")
    if not df["exit_rule_id"].astype(str).eq(EXPECTED_EXIT_RULE_ID).all():
        unexpected_mask = ~df["exit_rule_id"].astype(str).eq(EXPECTED_EXIT_RULE_ID)
        unexpected = sorted(set(df.loc[unexpected_mask, "exit_rule_id"].astype(str)))
        errors.append(
            "promotion matrix must use the approved close-confirmed prev20 breakout next-open exit rule only; "
            f"unexpected exit_rule_id values: {unexpected}"
        )
    matrix_text = "\n".join(df.astype(str).agg("|".join, axis=1).tolist())
    for forbidden in sorted(FORBIDDEN_PROMOTION_BASIS_TEXT):
        if forbidden in matrix_text:
            errors.append(f"promotion matrix must not use continuation/research-only exit basis: {forbidden}")
    missing_ids = REQUIRED_CANDIDATE_IDS - set(df["promotion_candidate_id"].astype(str))
    if missing_ids:
        errors.append("promotion matrix missing candidate rows: " + ", ".join(sorted(missing_ids)))

    role_by_id = dict(zip(df["promotion_candidate_id"].astype(str), df["proposed_contract_role"].astype(str)))
    if role_by_id.get("base_package:v1_gate_return20_tdcc_high_obv") != "base_model_candidate_required_gate_package":
        errors.append("base package must be the only base required-gate package candidate")
    if role_by_id.get("revenue_package:latest30_and_cumulative20", "").startswith("required_gate"):
        errors.append("latest30_and_cumulative20 must not be promoted as a required gate by this matrix")
    if role_by_id.get("revenue_reject:latest_yoy_turn_positive_after_2_negative") != "reject_as_required_gate_or_add_score":
        errors.append("turn-positive-after-negative revenue test must stay rejected until new evidence")
    if role_by_id.get("score_component:volume_red_or_solid_red_risk") != "risk_tag_candidate_review":
        errors.append("volume red/solid red component must stay a risk-tag candidate")
    if role_by_id.get("deferred_context:theme_leadership") != "defer_until_mature_point_in_time_theme_samples":
        errors.append("theme leadership context must remain deferred")
    return errors


def main() -> int:
    errors: list[str] = []
    validate_mirror(
        PRICE_PULLBACK_PROMOTION_MATRIX_CSV,
        DOCS_PRICE_PULLBACK_PROMOTION_MATRIX_CSV,
        errors,
    )
    validate_mirror(
        PRICE_PULLBACK_PROMOTION_MATRIX_MD,
        DOCS_PRICE_PULLBACK_PROMOTION_MATRIX_MD,
        errors,
    )
    try:
        matrix = read_csv(PRICE_PULLBACK_PROMOTION_MATRIX_CSV)
    except FileNotFoundError as exc:
        errors.append(f"missing price_pullback promotion matrix: {exc}")
        matrix = pd.DataFrame()
    if not matrix.empty:
        errors.extend(validate_matrix(matrix))
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1
    print(f"validated_price_pullback_promotion_matrix_rows={len(matrix)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
