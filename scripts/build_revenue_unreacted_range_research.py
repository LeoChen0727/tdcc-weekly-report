from __future__ import annotations

import argparse
import gc
from contextlib import contextmanager
from pathlib import Path
import sys
from typing import Iterator, Mapping

import pandas as pd


ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from build_daily_model_parameter_research import (
    REVENUE_UNREACTED_FEATURE_CONTRAST_BINARY_SPECS,
    REVENUE_UNREACTED_FEATURE_CONTRAST_NUMERIC_SPECS,
    _attach_revenue_signal_market_regime,
    _revenue_unreacted_timing_prepared_frame,
    build_revenue_unreacted_range_close_confirmation_timing_audit,
    build_revenue_unreacted_range_feature_contrast_audit,
    build_revenue_unreacted_range_operation_candidate_matrix,
    build_revenue_unreacted_range_revenue_condition_matrix,
    write_revenue_unreacted_range_feature_contrast_audit,
    write_revenue_unreacted_range_operation_candidate_matrix,
    write_revenue_unreacted_range_revenue_condition_matrix,
)
from model_research_artifact_guard import (
    _dirty_snapshot,
    changed_during_run,
    model_owned_artifact_guard,
)
from revenue_unreacted_range_close_confirmation_timing import write_close_confirmation_timing_audit
from revenue_unreacted_range_fixed_confirmation_feature_contrast import (
    build_fixed_confirmation_feature_contrast,
    write_fixed_confirmation_feature_contrast,
)
from revenue_unreacted_range_forward_confirmation_feature_audit import (
    build_forward_confirmation_feature_audit,
    prepare_daily_by_stock,
    write_forward_confirmation_feature_audit,
)
from revenue_unreacted_range_forward_holdout import (
    FORWARD_HOLDOUT_ALLOWED_ARTIFACT_PATHS,
    build_and_write_current_forward_holdout,
)
from scripts.validate_revenue_unreacted_range_forward_holdout import validate_frames
from revenue_unreacted_range_rearmed_operation_grid import (
    PRICE_HISTORY_CUTOFF_DATE,
    build_rearmed_operation_grid,
    write_rearmed_operation_grid,
)
from revenue_unreacted_range_extreme_return_path_audit import (
    build_extreme_return_path_audit,
    write_extreme_return_path_audit,
)
from revenue_unreacted_range_lag_strength_matrix import (
    DETAIL_CSV as LAG_STRENGTH_DETAIL_CSV,
    SOURCE_DETAIL as FIXED_CONFIRMATION_DETAIL_CSV,
    build_lag_strength_matrix,
    write_lag_strength_matrix,
)
from revenue_unreacted_range_launch_timing_feature_audit import (
    build_launch_timing_feature_audit,
    write_launch_timing_feature_audit,
)
from revenue_unreacted_range_low_mid_falling_candidate_audit import (
    build_low_mid_falling_candidate_audit,
    write_low_mid_falling_candidate_audit,
)
from revenue_unreacted_range_operation_lag_bucket_audit import (
    build_operation_lag_bucket_audit,
    write_operation_lag_bucket_audit,
)
from revenue_unreacted_range_position_shape_transition_matrix import (
    build_position_shape_transition_matrix,
    write_position_shape_transition_matrix,
)
from revenue_unreacted_range_source_first_condition_audit import (
    DETAIL_CSV as SOURCE_FIRST_DETAIL_CSV,
    DOCS_CSV as SOURCE_FIRST_DOCS_CSV,
    DOCS_MD as SOURCE_FIRST_DOCS_MD,
    HISTORY_CSV as SOURCE_FIRST_HISTORY_CSV,
    LATEST_CSV as SOURCE_FIRST_LATEST_CSV,
    LATEST_MD as SOURCE_FIRST_LATEST_MD,
    build_source_first_condition_audit,
    write_source_first_condition_audit,
)
from revenue_unreacted_range_source_snapshot_projection import (
    CUTOFF_DATE as SOURCE_SNAPSHOT_CUTOFF_DATE,
    LATEST_DETAIL_CSV as SOURCE_SNAPSHOT_V1_CANONICAL_DETAIL_CSV,
    LATEST_MANIFEST_CSV as SOURCE_SNAPSHOT_V1_CANONICAL_MANIFEST_CSV,
    V1_ARCHIVE_DETAIL_CSV,
    V1_ARCHIVE_EVIDENCE_CSV,
    V1_ARCHIVE_MANIFEST_CSV,
    V1_PROJECTION_VERSION,
    V2_CANDIDATE_DETAIL_CSV,
    V2_CANDIDATE_MANIFEST_CSV,
    V2_PROJECTION_VERSION,
    archive_immutable_v1_projection,
    build_source_snapshot_projection_v2_manifest,
    load_projected_source_detail,
    load_source_snapshot_projection_manifest,
    supersede_source_snapshot_projection_v2_candidate,
    validate_projection_binding,
    write_source_snapshot_projection,
    write_source_snapshot_projection_v2_candidate,
)
from scripts.validate_revenue_unreacted_range_source_snapshot_projection import (
    validate as validate_source_snapshot_projection,
)
from revenue_unreacted_range_research_frame import (
    build_revenue_unreacted_range_research_frame,
)


MODEL_ID = "revenue_unreacted_range"
PRODUCER = "scripts/build_revenue_unreacted_range_research.py"
SOURCE_SNAPSHOT_V1_V2_DIFF_SUMMARY_CSV = (
    ROOT
    / "output/history/research/"
    "revenue_unreacted_range_source_snapshot_projection_v1_20260731_to_v2_20260822_diff_summary.csv"
)
SOURCE_SNAPSHOT_V1_V2_DIFF_DETAIL_CSV = (
    ROOT
    / "output/history/research/"
    "revenue_unreacted_range_source_snapshot_projection_v1_20260731_to_v2_20260822_diff_detail.csv"
)
SOURCE_SNAPSHOT_PROJECTION_REBASELINE_ALLOWED_ARTIFACT_PATHS = tuple(
    path.relative_to(ROOT).as_posix()
    for path in (
        SOURCE_FIRST_LATEST_CSV,
        SOURCE_FIRST_DETAIL_CSV,
        SOURCE_FIRST_LATEST_MD,
        SOURCE_FIRST_HISTORY_CSV,
        SOURCE_FIRST_DOCS_CSV,
        SOURCE_FIRST_DOCS_MD,
        V1_ARCHIVE_MANIFEST_CSV,
        V1_ARCHIVE_DETAIL_CSV,
        V1_ARCHIVE_EVIDENCE_CSV,
        V2_CANDIDATE_MANIFEST_CSV,
        V2_CANDIDATE_DETAIL_CSV,
        SOURCE_SNAPSHOT_V1_V2_DIFF_SUMMARY_CSV,
        SOURCE_SNAPSHOT_V1_V2_DIFF_DETAIL_CSV,
    )
)


def validate_forward_holdout_stage_changed_paths(
    changed_paths: list[str],
) -> list[str]:
    """Restrict the forward-only stage to its exact seventeen research artifacts."""

    allowed = set(FORWARD_HOLDOUT_ALLOWED_ARTIFACT_PATHS)
    return [
        f"forward holdout stage artifact allowlist violation: {path}"
        for path in sorted(set(changed_paths) - allowed)
    ]


@contextmanager
def forward_holdout_stage_artifact_guard(
    *,
    root: Path = ROOT,
) -> Iterator[None]:
    before = _dirty_snapshot(root)
    try:
        yield
    finally:
        errors = validate_forward_holdout_stage_changed_paths(
            changed_during_run(root, before)
        )
        if errors:
            details = "\n".join(f"- {error}" for error in errors)
            raise RuntimeError(
                "forward holdout stage artifact guard failed:\n" + details
            )


def validate_source_snapshot_projection_rebaseline_changed_paths(
    changed_paths: list[str],
) -> list[str]:
    allowed = set(SOURCE_SNAPSHOT_PROJECTION_REBASELINE_ALLOWED_ARTIFACT_PATHS)
    return [
        f"source snapshot projection rebaseline artifact allowlist violation: {path}"
        for path in sorted(set(changed_paths) - allowed)
    ]


@contextmanager
def source_snapshot_projection_rebaseline_artifact_guard(
    *,
    root: Path = ROOT,
) -> Iterator[None]:
    before = _dirty_snapshot(root)
    try:
        yield
    finally:
        errors = validate_source_snapshot_projection_rebaseline_changed_paths(
            changed_during_run(root, before)
        )
        if errors:
            details = "\n".join(f"- {error}" for error in errors)
            raise RuntimeError(
                "source snapshot projection rebaseline artifact guard failed:\n"
                + details
            )


def load_immutable_source_snapshot_projection() -> tuple[pd.DataFrame, pd.DataFrame]:
    manifest = load_source_snapshot_projection_manifest()
    projection_version = (
        str(manifest.iloc[0].get("projection_version", "")).strip()
        if len(manifest) == 1
        else ""
    )
    if projection_version == V2_PROJECTION_VERSION:
        supersede_errors = validate_source_snapshot_projection()
        if supersede_errors:
            raise RuntimeError(
                "canonical v2 source snapshot projection supersede closure failed: "
                + "; ".join(supersede_errors)
            )
    elif projection_version != V1_PROJECTION_VERSION:
        raise RuntimeError(
            "canonical source snapshot projection loader accepts only immutable v1 "
            "or evidence-bound canonical v2; received "
            f"{projection_version or '<invalid>'}"
        )
    projected_detail = load_projected_source_detail()
    validate_projection_binding(
        manifest,
        projected_detail,
        expected_cutoff_date=PRICE_HISTORY_CUTOFF_DATE,
    )
    return manifest, projected_detail


def build_and_write() -> None:
    frame = build_revenue_unreacted_range_research_frame()
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
    source_first_summary, source_first_detail = build_source_first_condition_audit()
    source_projection_manifest, projected_source_detail = (
        load_immutable_source_snapshot_projection()
    )
    lag_strength_summary, lag_strength_detail = build_lag_strength_matrix(
        fixed_detail,
        source_projection_manifest=source_projection_manifest,
        projected_source_detail=projected_source_detail,
    )
    launch_summary, launch_detail, launch_feature = build_launch_timing_feature_audit(
        prepared,
        lag_strength_detail,
        observation_cutoff_date=PRICE_HISTORY_CUTOFF_DATE,
    )
    projected_daily_by_stock = prepare_daily_by_stock(
        prepared,
        projected_source_detail,
        observation_cutoff_date=PRICE_HISTORY_CUTOFF_DATE,
    )
    forward_summary, forward_detail, forward_events, forward_feature, forward_return_review = (
        build_forward_confirmation_feature_audit(
            source_detail=projected_source_detail,
            daily_by_stock=projected_daily_by_stock,
            source_projection_manifest=source_projection_manifest,
        )
    )
    rearmed_summary, rearmed_detail, rearmed_return_review = build_rearmed_operation_grid(
        source_detail=projected_source_detail,
        daily_by_stock=projected_daily_by_stock,
        source_projection_manifest=source_projection_manifest,
    )
    operation_lag_summary, operation_lag_detail = build_operation_lag_bucket_audit(
        operation_detail=rearmed_detail,
        source_detail=projected_source_detail,
        source_projection_manifest=source_projection_manifest,
    )
    (
        low_mid_falling_summary,
        low_mid_falling_detail,
        low_mid_falling_paired,
        low_mid_falling_contrast,
    ) = build_low_mid_falling_candidate_audit(
        projected_source_detail,
        rearmed_detail,
        projected_daily_by_stock,
    )

    write_revenue_unreacted_range_revenue_condition_matrix(condition_matrix)
    write_revenue_unreacted_range_operation_candidate_matrix(operation_matrix)
    write_revenue_unreacted_range_feature_contrast_audit(feature_summary, feature_detail, feature_anomaly)
    write_close_confirmation_timing_audit(timing_summary, timing_detail, timing_anomaly)
    write_fixed_confirmation_feature_contrast(fixed_summary, fixed_detail, fixed_anomaly)
    write_extreme_return_path_audit(extreme_return_audit)
    write_lag_strength_matrix(lag_strength_summary, lag_strength_detail)
    write_launch_timing_feature_audit(launch_summary, launch_detail, launch_feature)
    write_source_first_condition_audit(source_first_summary, source_first_detail)
    write_forward_confirmation_feature_audit(
        forward_summary,
        forward_detail,
        forward_events,
        forward_feature,
        forward_return_review,
    )
    write_rearmed_operation_grid(rearmed_summary, rearmed_detail, rearmed_return_review)
    write_operation_lag_bucket_audit(operation_lag_summary, operation_lag_detail)
    write_low_mid_falling_candidate_audit(
        low_mid_falling_summary,
        low_mid_falling_detail,
        low_mid_falling_paired,
        low_mid_falling_contrast,
    )
    position_shape_summary, position_shape_detail, position_shape_transition = (
        build_position_shape_transition_matrix()
    )
    write_position_shape_transition_matrix(
        position_shape_summary,
        position_shape_detail,
        position_shape_transition,
    )


def build_and_write_launch_timing_feature_audit() -> None:
    if not LAG_STRENGTH_DETAIL_CSV.is_file():
        raise RuntimeError(
            "Launch timing stage requires the existing model-owned lag-strength detail artifact: "
            f"{LAG_STRENGTH_DETAIL_CSV}"
        )
    frame = build_revenue_unreacted_range_research_frame()
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
        observation_cutoff_date=PRICE_HISTORY_CUTOFF_DATE,
    )
    write_launch_timing_feature_audit(launch_summary, launch_detail, launch_feature)


def build_and_write_source_first_condition_audit() -> None:
    summary, detail = build_source_first_condition_audit()
    write_source_first_condition_audit(summary, detail)


def build_and_write_source_snapshot_projection() -> None:
    manifest, projected_detail = load_immutable_source_snapshot_projection()
    write_source_snapshot_projection(manifest, projected_detail)


def build_and_write_source_snapshot_projection_rebaseline() -> None:
    """Create the v2 candidate without promoting or refreshing downstream consumers."""

    canonical_manifest_bytes = SOURCE_SNAPSHOT_V1_CANONICAL_MANIFEST_CSV.read_bytes()
    canonical_detail_bytes = SOURCE_SNAPSHOT_V1_CANONICAL_DETAIL_CSV.read_bytes()
    archive_evidence = archive_immutable_v1_projection()
    evidence_row = archive_evidence.iloc[0]

    source_first_summary, full_source_detail = build_source_first_condition_audit()
    _projected_summary, projected_detail = build_source_first_condition_audit(
        observation_cutoff_date=SOURCE_SNAPSHOT_CUTOFF_DATE,
    )
    candidate_manifest = build_source_snapshot_projection_v2_manifest(
        full_source_detail,
        projected_detail,
        predecessor_manifest_bytes_sha256=str(
            evidence_row["canonical_manifest_sha256"]
        ),
        predecessor_detail_bytes_sha256=str(
            evidence_row["canonical_detail_sha256"]
        ),
    )
    write_source_first_condition_audit(source_first_summary, full_source_detail)
    write_source_snapshot_projection_v2_candidate(
        candidate_manifest,
        projected_detail,
    )

    from revenue_unreacted_range_source_snapshot_projection_v1_v2_diff import (
        build_diff_from_paths,
        write_diff_artifacts,
    )

    diff_summary, diff_detail = build_diff_from_paths()
    write_diff_artifacts(diff_summary, diff_detail)

    if SOURCE_SNAPSHOT_V1_CANONICAL_MANIFEST_CSV.read_bytes() != canonical_manifest_bytes:
        raise RuntimeError("canonical v1 manifest changed during v2 rebaseline")
    if SOURCE_SNAPSHOT_V1_CANONICAL_DETAIL_CSV.read_bytes() != canonical_detail_bytes:
        raise RuntimeError("canonical v1 detail changed during v2 rebaseline")


def build_and_write_source_snapshot_projection_chain() -> None:
    """Refresh only the cutoff-pinned source projection consumer chain."""

    manifest, projected_detail = load_immutable_source_snapshot_projection()

    frame = build_revenue_unreacted_range_research_frame()
    if frame.empty:
        raise RuntimeError(
            "No price history available for revenue_unreacted_range source snapshot "
            "projection chain"
        )
    prepared = _attach_revenue_signal_market_regime(
        _revenue_unreacted_timing_prepared_frame(frame)
    )
    del frame
    gc.collect()
    fixed_detail = pd.read_csv(
        FIXED_CONFIRMATION_DETAIL_CSV,
        dtype={
            "stock_id": str,
            "source_monthly_revenue_source_table_date": str,
            "signal_date": str,
            "confirmation_date": str,
            "entry_date": str,
            "exit_date": str,
        },
        keep_default_na=False,
        low_memory=False,
    )
    lag_strength_summary, lag_strength_detail = build_lag_strength_matrix(
        fixed_detail,
        source_projection_manifest=manifest,
        projected_source_detail=projected_detail,
    )
    launch_summary, launch_detail, launch_feature = build_launch_timing_feature_audit(
        prepared,
        lag_strength_detail,
        observation_cutoff_date=PRICE_HISTORY_CUTOFF_DATE,
    )
    projected_daily_by_stock = prepare_daily_by_stock(
        prepared,
        projected_detail,
        observation_cutoff_date=PRICE_HISTORY_CUTOFF_DATE,
    )
    forward_summary, forward_detail, forward_events, forward_feature, forward_return_review = (
        build_forward_confirmation_feature_audit(
            source_detail=projected_detail,
            daily_by_stock=projected_daily_by_stock,
            source_projection_manifest=manifest,
        )
    )
    rearmed_summary, rearmed_detail, rearmed_return_review = (
        build_rearmed_operation_grid(
            source_detail=projected_detail,
            daily_by_stock=projected_daily_by_stock,
            source_projection_manifest=manifest,
        )
    )
    operation_lag_summary, operation_lag_detail = build_operation_lag_bucket_audit(
        operation_detail=rearmed_detail,
        source_detail=projected_detail,
        source_projection_manifest=manifest,
    )
    (
        low_mid_falling_summary,
        low_mid_falling_detail,
        low_mid_falling_paired,
        low_mid_falling_contrast,
    ) = build_low_mid_falling_candidate_audit(
        projected_detail,
        rearmed_detail,
        projected_daily_by_stock,
    )

    # Persist the cutoff consumers in dependency order before the position/shape
    # builder reads their exact artifacts and enforces the immutable 955 pins.
    write_lag_strength_matrix(lag_strength_summary, lag_strength_detail)
    write_launch_timing_feature_audit(
        launch_summary,
        launch_detail,
        launch_feature,
    )
    write_forward_confirmation_feature_audit(
        forward_summary,
        forward_detail,
        forward_events,
        forward_feature,
        forward_return_review,
    )
    write_rearmed_operation_grid(
        rearmed_summary,
        rearmed_detail,
        rearmed_return_review,
    )
    write_operation_lag_bucket_audit(operation_lag_summary, operation_lag_detail)
    position_shape_summary, position_shape_detail, position_shape_transition = (
        build_position_shape_transition_matrix()
    )
    write_position_shape_transition_matrix(
        position_shape_summary,
        position_shape_detail,
        position_shape_transition,
    )
    write_low_mid_falling_candidate_audit(
        low_mid_falling_summary,
        low_mid_falling_detail,
        low_mid_falling_paired,
        low_mid_falling_contrast,
    )


def build_and_write_source_snapshot_projection_supersede_and_chain() -> None:
    """Select canonical v2, then refresh its research-only consumer chain."""

    supersede_source_snapshot_projection_v2_candidate()
    build_and_write_source_snapshot_projection_chain()


def build_and_write_forward_confirmation_feature_audit() -> None:
    projected_source_detail = load_projected_source_detail()
    source_projection_manifest = load_source_snapshot_projection_manifest()
    validate_projection_binding(source_projection_manifest, projected_source_detail)
    frame = build_revenue_unreacted_range_research_frame()
    if frame.empty:
        raise RuntimeError("No price history available for revenue_unreacted_range forward confirmation research")
    prepared = _attach_revenue_signal_market_regime(_revenue_unreacted_timing_prepared_frame(frame))
    del frame
    gc.collect()
    projected_daily_by_stock = prepare_daily_by_stock(
        prepared,
        projected_source_detail,
        observation_cutoff_date=PRICE_HISTORY_CUTOFF_DATE,
    )
    summary, detail, events, feature, return_review = build_forward_confirmation_feature_audit(
        source_detail=projected_source_detail,
        daily_by_stock=projected_daily_by_stock,
        source_projection_manifest=source_projection_manifest,
    )
    write_forward_confirmation_feature_audit(summary, detail, events, feature, return_review)


def build_and_write_rearmed_operation_grid() -> None:
    frame = build_revenue_unreacted_range_research_frame()
    if frame.empty:
        raise RuntimeError("No price history available for revenue_unreacted_range rearmed operation grid")
    prepared = _attach_revenue_signal_market_regime(_revenue_unreacted_timing_prepared_frame(frame))
    del frame
    gc.collect()
    summary, detail, return_review = build_rearmed_operation_grid(prepared=prepared)
    write_rearmed_operation_grid(summary, detail, return_review)


def build_and_write_operation_lag_bucket_audit() -> None:
    summary, detail = build_operation_lag_bucket_audit()
    write_operation_lag_bucket_audit(summary, detail)


def build_and_write_position_shape_transition_matrix() -> None:
    projected_source_detail = load_projected_source_detail()
    source_projection_manifest = load_source_snapshot_projection_manifest()
    validate_projection_binding(source_projection_manifest, projected_source_detail)
    summary, detail, transition = build_position_shape_transition_matrix()
    write_position_shape_transition_matrix(summary, detail, transition)


def build_and_write_low_mid_falling_candidate_audit() -> None:
    source_first_detail = load_projected_source_detail()
    source_projection_manifest = load_source_snapshot_projection_manifest()
    validate_projection_binding(source_projection_manifest, source_first_detail)
    frame = build_revenue_unreacted_range_research_frame()
    if frame.empty:
        raise RuntimeError(
            "No price history available for revenue_unreacted_range low/mid falling "
            "candidate audit"
        )
    prepared = _attach_revenue_signal_market_regime(
        _revenue_unreacted_timing_prepared_frame(frame)
    )
    del frame
    gc.collect()
    daily_by_stock = prepare_daily_by_stock(
        prepared,
        source_first_detail,
        observation_cutoff_date=PRICE_HISTORY_CUTOFF_DATE,
    )
    _rearmed_summary, rearmed_detail, _rearmed_return_review = (
        build_rearmed_operation_grid(
            source_detail=source_first_detail,
            daily_by_stock=daily_by_stock,
            source_projection_manifest=source_projection_manifest,
        )
    )
    summary, detail, paired, contrast = build_low_mid_falling_candidate_audit(
        source_first_detail,
        rearmed_detail,
        daily_by_stock,
    )
    write_low_mid_falling_candidate_audit(
        summary,
        detail,
        paired,
        contrast,
    )


def validate_forward_holdout_persisted_frames(
    manifest_readback: pd.DataFrame,
    detail_readback: pd.DataFrame,
    summary_readback: pd.DataFrame,
    comparison_readback: pd.DataFrame,
    anomaly_readback: pd.DataFrame,
    *,
    source_detail: pd.DataFrame,
    price_inputs: Mapping[str, pd.DataFrame],
    source_manifest: pd.DataFrame,
    history_frames: Mapping[str, pd.DataFrame],
    immutable_history_base_frames: Mapping[str, pd.DataFrame] | None,
) -> None:
    errors = validate_frames(
        manifest_readback,
        detail_readback,
        summary_readback,
        comparison_readback,
        anomaly_readback,
        source_detail=source_detail,
        daily_by_stock=price_inputs,
        source_manifest=source_manifest,
        history_frames=history_frames,
        immutable_history_base_frames=immutable_history_base_frames,
    )
    if errors:
        raise RuntimeError(
            "forward holdout model-owned persisted replay failed: "
            + "; ".join(errors)
        )


def build_and_write_forward_holdout() -> None:
    build_and_write_current_forward_holdout(
        final_validation=validate_forward_holdout_persisted_frames
    )


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Build model-owned revenue_unreacted_range research artifacts.")
    parser.add_argument(
        "--stage",
        choices=(
            "all",
            "launch_timing_feature_audit",
            "source_first_condition_audit",
            "source_snapshot_projection",
            "source_snapshot_projection_rebaseline",
            "source_snapshot_projection_chain",
            "source_snapshot_projection_supersede_and_chain",
            "forward_confirmation_feature_audit",
            "rearmed_operation_grid",
            "operation_lag_bucket_audit",
            "position_shape_transition_matrix",
            "low_mid_falling_candidate_audit",
            "forward_holdout",
        ),
        default="all",
        help="Run the full producer or one model-owned audit stage.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    with model_owned_artifact_guard(MODEL_ID, PRODUCER):
        if args.stage == "launch_timing_feature_audit":
            build_and_write_launch_timing_feature_audit()
        elif args.stage == "source_first_condition_audit":
            build_and_write_source_first_condition_audit()
        elif args.stage == "source_snapshot_projection":
            build_and_write_source_snapshot_projection()
        elif args.stage == "source_snapshot_projection_rebaseline":
            with source_snapshot_projection_rebaseline_artifact_guard():
                build_and_write_source_snapshot_projection_rebaseline()
        elif args.stage == "source_snapshot_projection_chain":
            build_and_write_source_snapshot_projection_chain()
        elif args.stage == "source_snapshot_projection_supersede_and_chain":
            build_and_write_source_snapshot_projection_supersede_and_chain()
        elif args.stage == "forward_confirmation_feature_audit":
            build_and_write_forward_confirmation_feature_audit()
        elif args.stage == "rearmed_operation_grid":
            build_and_write_rearmed_operation_grid()
        elif args.stage == "operation_lag_bucket_audit":
            build_and_write_operation_lag_bucket_audit()
        elif args.stage == "position_shape_transition_matrix":
            build_and_write_position_shape_transition_matrix()
        elif args.stage == "low_mid_falling_candidate_audit":
            build_and_write_low_mid_falling_candidate_audit()
        elif args.stage == "forward_holdout":
            with forward_holdout_stage_artifact_guard():
                build_and_write_forward_holdout()
        else:
            build_and_write()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
