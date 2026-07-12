from __future__ import annotations

import argparse
import gc

import pandas as pd

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
    DETAIL_CSV as LAG_STRENGTH_DETAIL_CSV,
    build_lag_strength_matrix,
    write_lag_strength_matrix,
)
from revenue_unreacted_range_launch_timing_feature_audit import (
    build_launch_timing_feature_audit,
    write_launch_timing_feature_audit,
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
    del frame
    gc.collect()
    fixed_summary, fixed_detail, fixed_anomaly = build_fixed_confirmation_feature_contrast(
        prepared,
        timing_summary,
        binary_specs=REVENUE_UNREACTED_FEATURE_CONTRAST_BINARY_SPECS,
        numeric_specs=REVENUE_UNREACTED_FEATURE_CONTRAST_NUMERIC_SPECS,
    )
    extreme_return_audit = build_extreme_return_path_audit(fixed_detail)
    lag_strength_summary, lag_strength_detail = build_lag_strength_matrix(fixed_detail)
    launch_summary, launch_detail, launch_feature = build_launch_timing_feature_audit(
        prepared,
        lag_strength_detail,
    )

    write_revenue_unreacted_range_revenue_condition_matrix(condition_matrix)
    write_revenue_unreacted_range_operation_candidate_matrix(operation_matrix)
    write_revenue_unreacted_range_feature_contrast_audit(feature_summary, feature_detail, feature_anomaly)
    write_close_confirmation_timing_audit(timing_summary, timing_detail, timing_anomaly)
    write_fixed_confirmation_feature_contrast(fixed_summary, fixed_detail, fixed_anomaly)
    write_extreme_return_path_audit(extreme_return_audit)
    write_lag_strength_matrix(lag_strength_summary, lag_strength_detail)
    write_launch_timing_feature_audit(launch_summary, launch_detail, launch_feature)


def build_and_write_launch_timing_feature_audit() -> None:
    if not LAG_STRENGTH_DETAIL_CSV.is_file():
        raise RuntimeError(
            "Launch timing stage requires the existing model-owned lag-strength detail artifact: "
            f"{LAG_STRENGTH_DETAIL_CSV}"
        )
    frame = build_research_frame()
    if frame.empty:
        raise RuntimeError("No price history available for revenue_unreacted_range launch timing research")
    prepared = _attach_revenue_signal_market_regime(_revenue_unreacted_timing_prepared_frame(frame))
    del frame
    gc.collect()
    lag_strength_detail = pd.read_csv(
        LAG_STRENGTH_DETAIL_CSV,
        dtype={"stock_id": str},
        keep_default_na=False,
        low_memory=False,
    )
    launch_summary, launch_detail, launch_feature = build_launch_timing_feature_audit(
        prepared,
        lag_strength_detail,
    )
    write_launch_timing_feature_audit(launch_summary, launch_detail, launch_feature)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Build model-owned revenue_unreacted_range research artifacts.")
    parser.add_argument(
        "--stage",
        choices=("all", "launch_timing_feature_audit"),
        default="all",
        help="Run the full producer or only the launch timing feature audit stage.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    with model_owned_artifact_guard(MODEL_ID, PRODUCER):
        if args.stage == "launch_timing_feature_audit":
            build_and_write_launch_timing_feature_audit()
        else:
            build_and_write()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
