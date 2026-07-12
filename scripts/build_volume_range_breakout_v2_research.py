from __future__ import annotations

import subprocess
import sys

from model_research_artifact_guard import model_owned_artifact_guard


MODEL_ID = "volume_range_breakout_v2"
PRODUCER = "scripts/build_volume_range_breakout_v2_research.py"
STEPS = (
    ("build_volume_range_breakout_v2_semantic_audit.py", "validate_volume_range_breakout_v2_semantic_audit.py"),
    (
        "build_volume_range_breakout_v2_next_day_continuation_timing_audit.py",
        "validate_volume_range_breakout_v2_next_day_continuation_timing_audit.py",
    ),
    ("build_volume_range_breakout_v2_raw_market_rerun.py", "validate_volume_range_breakout_v2_raw_market_rerun.py"),
    (
        "build_volume_range_breakout_v2_feature_slice_analysis.py",
        "validate_volume_range_breakout_v2_feature_slice_analysis.py",
    ),
    ("build_volume_range_breakout_v2_deep_low_base_matrix.py", "validate_volume_range_breakout_v2_deep_low_base_matrix.py"),
    ("build_volume_range_breakout_v2_condition_matrix.py", "validate_volume_range_breakout_v2_condition_matrix.py"),
    ("build_volume_range_breakout_v2_overlap_sensitivity.py", "validate_volume_range_breakout_v2_overlap_sensitivity.py"),
    ("build_volume_range_breakout_v2_split_feature_audit.py", "validate_volume_range_breakout_v2_split_feature_audit.py"),
    ("build_volume_range_breakout_v2_research_contract.py", "validate_volume_range_breakout_v2_research_contract.py"),
    (
        "build_volume_range_breakout_v2_promotion_readiness_audit.py",
        "validate_volume_range_breakout_v2_promotion_readiness_audit.py",
    ),
    ("build_volume_range_breakout_v2_position_shape_matrix.py", "validate_volume_range_breakout_v2_position_shape_matrix.py"),
    (
        "build_volume_range_breakout_v2_high_position_improvement_audit.py",
        "validate_volume_range_breakout_v2_high_position_improvement_audit.py",
    ),
    (
        "build_volume_range_breakout_v2_candidate_bucket_contract.py",
        "validate_volume_range_breakout_v2_candidate_bucket_contract.py",
    ),
)


def main() -> int:
    with model_owned_artifact_guard(MODEL_ID, PRODUCER):
        for builder, validator in STEPS:
            subprocess.run([sys.executable, f"scripts/{builder}"], check=True)
            subprocess.run([sys.executable, f"scripts/{validator}"], check=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
