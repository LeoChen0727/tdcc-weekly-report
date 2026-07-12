from __future__ import annotations

from build_daily_model_parameter_research import (
    REVENUE_UNREACTED_FEATURE_CONTRAST_BINARY_SPECS,
    REVENUE_UNREACTED_FEATURE_CONTRAST_NUMERIC_SPECS,
    _attach_revenue_signal_market_regime,
    _revenue_unreacted_timing_prepared_frame,
    build_research_frame,
    build_revenue_unreacted_range_close_confirmation_timing_audit,
    build_revenue_unreacted_range_feature_contrast_audit,
    build_revenue_unreacted_range_operation_candidate_matrix,
    build_revenue_unreacted_range_revenue_condition_matrix,
    write_revenue_unreacted_range_feature_contrast_audit,
    write_revenue_unreacted_range_operation_candidate_matrix,
    write_revenue_unreacted_range_revenue_condition_matrix,
)
from model_research_artifact_guard import model_owned_artifact_guard
from revenue_unreacted_range_close_confirmation_timing import write_close_confirmation_timing_audit
from revenue_unreacted_range_fixed_confirmation_feature_contrast import (
    build_fixed_confirmation_feature_contrast,
    write_fixed_confirmation_feature_contrast,
)
from revenue_unreacted_range_extreme_return_path_audit import (
    build_extreme_return_path_audit,
    write_extreme_return_path_audit,
)
from revenue_unreacted_range_lag_strength_matrix import (
    build_lag_strength_matrix,
    write_lag_strength_matrix,
)


MODEL_ID = "revenue_unreacted_range"
PRODUCER = "scripts/build_revenue_unreacted_range_research.py"


def build_and_write() -> None:
    frame = build_research_frame()
    if frame.empty:
        raise RuntimeError("No price history available for revenue_unreacted_range research")

    condition_matrix = build_revenue_unreacted_range_revenue_condition_matrix(frame)
    operation_matrix = build_revenue_unreacted_range_operation_candidate_matrix(frame)
    feature_summary, feature_detail, feature_anomaly = build_revenue_unreacted_range_feature_contrast_audit(frame)
    timing_summary, timing_detail, timing_anomaly = build_revenue_unreacted_range_close_confirmation_timing_audit(
        frame,
        feature_anomaly,
    )
    prepared = _attach_revenue_signal_market_regime(_revenue_unreacted_timing_prepared_frame(frame))
    fixed_summary, fixed_detail, fixed_anomaly = build_fixed_confirmation_feature_contrast(
        prepared,
        timing_summary,
        binary_specs=REVENUE_UNREACTED_FEATURE_CONTRAST_BINARY_SPECS,
        numeric_specs=REVENUE_UNREACTED_FEATURE_CONTRAST_NUMERIC_SPECS,
    )
    extreme_return_audit = build_extreme_return_path_audit(fixed_detail)
    lag_strength_summary, lag_strength_detail = build_lag_strength_matrix(fixed_detail)

    write_revenue_unreacted_range_revenue_condition_matrix(condition_matrix)
    write_revenue_unreacted_range_operation_candidate_matrix(operation_matrix)
    write_revenue_unreacted_range_feature_contrast_audit(feature_summary, feature_detail, feature_anomaly)
    write_close_confirmation_timing_audit(timing_summary, timing_detail, timing_anomaly)
    write_fixed_confirmation_feature_contrast(fixed_summary, fixed_detail, fixed_anomaly)
    write_extreme_return_path_audit(extreme_return_audit)
    write_lag_strength_matrix(lag_strength_summary, lag_strength_detail)


def main() -> int:
    with model_owned_artifact_guard(MODEL_ID, PRODUCER):
        build_and_write()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
