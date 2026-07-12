from __future__ import annotations

from build_daily_model_parameter_research import (
    build_price_pullback_continuation_win_profile,
    build_price_pullback_daily_row_parity_audit,
    build_price_pullback_exit_rule_comparison,
    build_price_pullback_feature_confirmation_research,
    build_price_pullback_high_return_feature_score_grid,
    build_price_pullback_lifecycle_replay,
    build_price_pullback_model_decision_audit,
    build_price_pullback_operation_module_research,
    build_price_pullback_operation_research,
    build_price_pullback_ordered_condition_matrix,
    build_price_pullback_promotion_matrix,
    build_price_pullback_research_score_bucket,
    build_price_pullback_revenue_condition_matrix,
    build_price_pullback_time_cost_backtest,
    build_research_frame,
    write_price_pullback_continuation_win_profile,
    write_price_pullback_daily_row_parity_audit,
    write_price_pullback_exit_rule_comparison,
    write_price_pullback_feature_confirmation_research,
    write_price_pullback_high_return_feature_score_grid,
    write_price_pullback_lifecycle_replay,
    write_price_pullback_model_decision_audit,
    write_price_pullback_operation_module_research,
    write_price_pullback_operation_research,
    write_price_pullback_ordered_condition_matrix,
    write_price_pullback_promotion_matrix,
    write_price_pullback_research_score_bucket,
    write_price_pullback_revenue_condition_matrix,
    write_price_pullback_time_cost_backtest,
)
from model_research_artifact_guard import model_owned_artifact_guard


MODEL_ID = "price_pullback_23ema"
PRODUCER = "scripts/build_price_pullback_23ema_research.py"


def build_and_write() -> None:
    frame = build_research_frame()
    if frame.empty:
        raise RuntimeError("No price history available for price_pullback_23ema research")

    operation = build_price_pullback_operation_research(frame)
    time_cost = build_price_pullback_time_cost_backtest(frame)
    operation_module = build_price_pullback_operation_module_research(frame)
    feature_confirmation = build_price_pullback_feature_confirmation_research(frame)
    exit_comparison = build_price_pullback_exit_rule_comparison(frame)
    continuation = build_price_pullback_continuation_win_profile(frame)
    score_bucket = build_price_pullback_research_score_bucket(frame)
    high_return_grid = build_price_pullback_high_return_feature_score_grid(frame)
    revenue_matrix = build_price_pullback_revenue_condition_matrix(frame)
    ordered_matrix = build_price_pullback_ordered_condition_matrix(frame)
    lifecycle = build_price_pullback_lifecycle_replay(frame)
    row_parity = build_price_pullback_daily_row_parity_audit(frame)
    decision = build_price_pullback_model_decision_audit(
        operation_module,
        feature_confirmation,
        row_parity,
    )
    promotion = build_price_pullback_promotion_matrix(
        lifecycle,
        ordered_matrix,
        high_return_grid,
        revenue_matrix,
    )

    write_price_pullback_operation_research(operation)
    write_price_pullback_time_cost_backtest(time_cost)
    write_price_pullback_operation_module_research(operation_module)
    write_price_pullback_feature_confirmation_research(feature_confirmation)
    write_price_pullback_exit_rule_comparison(exit_comparison)
    write_price_pullback_continuation_win_profile(continuation)
    write_price_pullback_research_score_bucket(score_bucket)
    write_price_pullback_high_return_feature_score_grid(high_return_grid)
    write_price_pullback_revenue_condition_matrix(revenue_matrix)
    write_price_pullback_ordered_condition_matrix(ordered_matrix)
    write_price_pullback_lifecycle_replay(lifecycle)
    write_price_pullback_daily_row_parity_audit(row_parity)
    write_price_pullback_model_decision_audit(decision)
    write_price_pullback_promotion_matrix(promotion)


def main() -> int:
    with model_owned_artifact_guard(MODEL_ID, PRODUCER):
        build_and_write()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
