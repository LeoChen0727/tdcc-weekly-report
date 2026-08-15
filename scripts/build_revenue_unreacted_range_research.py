from __future__ import annotations

import argparse
import gc
from contextlib import contextmanager
import os
from pathlib import Path
import shutil
import sys
import tempfile
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
    build_source_first_condition_audit,
    write_source_first_condition_audit,
)
from revenue_unreacted_range_source_snapshot_projection import (
    ARTIFACT_VERSION as SOURCE_SNAPSHOT_LEGACY_ARTIFACT_VERSION,
    CUTOFF_DATE as SOURCE_SNAPSHOT_PROJECTION_CUTOFF_DATE,
    MONTHLY_RESOLUTION_CSV as SOURCE_SNAPSHOT_MONTHLY_RESOLUTION_CSV,
    PRICE_HISTORY_DIR as SOURCE_SNAPSHOT_PRICE_HISTORY_DIR,
    PRICE_RESOLUTION_CSV as SOURCE_SNAPSHOT_PRICE_RESOLUTION_CSV,
    REBASELINE_ARTIFACT_VERSION as SOURCE_SNAPSHOT_REBASELINE_ARTIFACT_VERSION,
    REVENUE_HISTORY_CSV as SOURCE_SNAPSHOT_REVENUE_HISTORY_CSV,
    VERSIONED_V1_DETAIL_CSV,
    VERSIONED_V1_MANIFEST_CSV,
    VERSIONED_V2_DETAIL_CSV,
    VERSIONED_V2_MANIFEST_CSV,
    build_source_snapshot_projection_manifest,
    load_committed_v1_projection_predecessor,
    load_projected_source_detail,
    load_source_snapshot_projection_manifest,
    source_repair_provenance,
    validate_projection_binding,
    write_source_snapshot_projection,
)
from revenue_unreacted_range_source_snapshot_projection_v1_v2_diff import (
    DOCS_CSV as SOURCE_SNAPSHOT_DIFF_DOCS_CSV,
    HISTORY_CSV as SOURCE_SNAPSHOT_DIFF_HISTORY_CSV,
    LATEST_CSV as SOURCE_SNAPSHOT_DIFF_LATEST_CSV,
    build_projection_v1_v2_diff,
    write_projection_v1_v2_diff,
)
from revenue_unreacted_range_source_snapshot_projection_v1_v2_operation_diff import (
    DOCS_CSV as SOURCE_SNAPSHOT_OPERATION_DIFF_DOCS_CSV,
    HISTORY_CSV as SOURCE_SNAPSHOT_OPERATION_DIFF_HISTORY_CSV,
    LATEST_CSV as SOURCE_SNAPSHOT_OPERATION_DIFF_LATEST_CSV,
    build_operation_diff as build_source_snapshot_operation_diff,
    write_operation_diff as write_source_snapshot_operation_diff,
)
from revenue_unreacted_range_research_frame import (
    build_revenue_unreacted_range_research_frame,
)
from validate_revenue_unreacted_range_source_first_condition_audit import (
    validate as validate_source_first_condition_audit_independently,
)
from validate_revenue_unreacted_range_source_snapshot_projection import (
    validate as validate_source_snapshot_projection_independently,
)
from validate_revenue_unreacted_range_source_snapshot_projection_v1_v2_diff import (
    validate_paths as validate_source_snapshot_projection_diff_independently,
)
from validate_revenue_unreacted_range_source_snapshot_projection_v1_v2_operation_diff import (
    validate_frames as validate_source_snapshot_operation_diff_independently,
)


MODEL_ID = "revenue_unreacted_range"
PRODUCER = "scripts/build_revenue_unreacted_range_research.py"
SOURCE_SNAPSHOT_PROJECTION_REBASELINE_ALLOWED_ARTIFACT_PATHS = (
    "output/latest/research_backtest/revenue_unreacted_range_source_first_condition_audit_latest.csv",
    "output/latest/research_backtest/revenue_unreacted_range_source_first_condition_audit_detail_latest.csv",
    "output/latest/research_backtest/revenue_unreacted_range_source_first_condition_audit_latest.md",
    "output/history/research/revenue_unreacted_range_source_first_condition_audit.csv",
    "docs/latest/revenue_unreacted_range_source_first_condition_audit_latest.csv",
    "docs/latest/revenue_unreacted_range_source_first_condition_audit_latest.md",
    "output/history/research/revenue_unreacted_range_source_snapshot_projection_v1_20260731_manifest.csv",
    "output/history/research/revenue_unreacted_range_source_snapshot_projection_v1_20260731_detail.csv",
    "output/history/research/revenue_unreacted_range_source_snapshot_projection_v2_20260814_manifest.csv",
    "output/history/research/revenue_unreacted_range_source_snapshot_projection_v2_20260814_detail.csv",
    "output/history/research/revenue_unreacted_range_source_snapshot_projection_v1_v2_diff_v1_20260814.csv",
    "output/latest/research_backtest/revenue_unreacted_range_source_snapshot_projection_v1_v2_diff_latest.csv",
    "docs/latest/revenue_unreacted_range_source_snapshot_projection_v1_v2_diff_latest.csv",
)


def validate_source_snapshot_projection_rebaseline_stage_changed_paths(
    changed_paths: list[str],
    *,
    existing_paths: list[str] | None = None,
) -> list[str]:
    allowed = set(SOURCE_SNAPSHOT_PROJECTION_REBASELINE_ALLOWED_ARTIFACT_PATHS)
    changed = set(changed_paths)
    errors = [
        f"source snapshot projection rebaseline stage artifact allowlist violation: {path}"
        for path in sorted(changed - allowed)
    ]
    errors.extend(
        f"source snapshot projection rebaseline stage expected artifact unchanged: {path}"
        for path in sorted(allowed - changed)
    )
    if existing_paths is not None:
        errors.extend(
            f"source snapshot projection rebaseline stage required artifact missing: {path}"
            for path in sorted(allowed - set(existing_paths))
        )
    return errors


def _source_snapshot_projection_rebaseline_payload_snapshot(
    root: Path,
) -> dict[str, bytes | None]:
    return {
        relative_path: (
            (root / relative_path).read_bytes()
            if (root / relative_path).is_file()
            else None
        )
        for relative_path in SOURCE_SNAPSHOT_PROJECTION_REBASELINE_ALLOWED_ARTIFACT_PATHS
    }


def _restore_source_snapshot_projection_rebaseline_payloads(
    root: Path,
    payloads: Mapping[str, bytes | None],
) -> None:
    for relative_path, payload in payloads.items():
        path = root / relative_path
        if payload is None:
            if path.exists():
                path.unlink()
            continue
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(payload)


@contextmanager
def source_snapshot_projection_rebaseline_stage_artifact_guard(
    *,
    root: Path = ROOT,
) -> Iterator[None]:
    before = _dirty_snapshot(root)
    before_payloads = _source_snapshot_projection_rebaseline_payload_snapshot(root)
    try:
        yield
        existing_paths = [
            relative_path
            for relative_path in SOURCE_SNAPSHOT_PROJECTION_REBASELINE_ALLOWED_ARTIFACT_PATHS
            if (root / relative_path).is_file()
        ]
        errors = validate_source_snapshot_projection_rebaseline_stage_changed_paths(
            changed_during_run(root, before),
            existing_paths=existing_paths,
        )
        if errors:
            details = "\n".join(f"- {error}" for error in errors)
            raise RuntimeError(
                "source snapshot projection rebaseline stage artifact guard failed:\n"
                + details
            )
    except BaseException:
        _restore_source_snapshot_projection_rebaseline_payloads(root, before_payloads)
        raise


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


def load_immutable_source_snapshot_projection() -> tuple[pd.DataFrame, pd.DataFrame]:
    manifest = load_source_snapshot_projection_manifest()
    projected_detail = load_projected_source_detail()
    validate_projection_binding(
        manifest,
        projected_detail,
        expected_cutoff_date=PRICE_HISTORY_CUTOFF_DATE,
        expected_artifact_version=SOURCE_SNAPSHOT_LEGACY_ARTIFACT_VERSION,
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
        source_projection_manifest=source_projection_manifest,
        source_projection_artifact_version=(
            SOURCE_SNAPSHOT_LEGACY_ARTIFACT_VERSION
        ),
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


def _rebaseline_temp_path(temp_root: Path, target: Path) -> Path:
    relative = target.resolve().relative_to(ROOT.resolve())
    return temp_root / relative


def _write_projection_frame(path: Path, frame: pd.DataFrame) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    frame.to_csv(path, index=False, lineterminator="\n")


def _replace_rebaseline_path(source: Path, destination: Path) -> None:
    """Injection seam used by transaction rollback regression tests."""

    os.replace(source, destination)


def _validate_rebaseline_temp_bundle(
    *,
    temp_root: Path,
    v1_manifest_path: Path,
    v1_detail_path: Path,
    v2_manifest_path: Path,
    v2_detail_path: Path,
) -> None:
    source_summary = _rebaseline_temp_path(
        temp_root,
        ROOT
        / "output/latest/research_backtest/"
        "revenue_unreacted_range_source_first_condition_audit_latest.csv",
    )
    source_detail = _rebaseline_temp_path(
        temp_root,
        ROOT
        / "output/latest/research_backtest/"
        "revenue_unreacted_range_source_first_condition_audit_detail_latest.csv",
    )
    source_markdown = _rebaseline_temp_path(
        temp_root,
        ROOT
        / "output/latest/research_backtest/"
        "revenue_unreacted_range_source_first_condition_audit_latest.md",
    )
    errors = validate_source_first_condition_audit_independently(
        revenue_path=SOURCE_SNAPSHOT_REVENUE_HISTORY_CSV,
        resolution_path=SOURCE_SNAPSHOT_MONTHLY_RESOLUTION_CSV,
        projection_manifest_path=v2_manifest_path,
        summary_path=source_summary,
        detail_path=source_detail,
        markdown_path=source_markdown,
    )
    if errors:
        raise RuntimeError(
            "independent source-first rebaseline validation failed: "
            + "; ".join(errors)
        )
    errors = validate_source_snapshot_projection_independently(
        manifest_path=v2_manifest_path,
        projected_detail_path=v2_detail_path,
        revenue_path=SOURCE_SNAPSHOT_REVENUE_HISTORY_CSV,
        price_dir=SOURCE_SNAPSHOT_PRICE_HISTORY_DIR,
        monthly_resolution_path=SOURCE_SNAPSHOT_MONTHLY_RESOLUTION_CSV,
        price_resolution_path=SOURCE_SNAPSHOT_PRICE_RESOLUTION_CSV,
        expected_artifact_version=SOURCE_SNAPSHOT_REBASELINE_ARTIFACT_VERSION,
        repo_root=ROOT,
    )
    if errors:
        raise RuntimeError(
            "independent v2 projection rebaseline validation failed: "
            + "; ".join(errors)
        )
    errors = validate_source_snapshot_projection_diff_independently(
        v1_manifest_path=v1_manifest_path,
        v1_detail_path=v1_detail_path,
        v2_manifest_path=v2_manifest_path,
        v2_detail_path=v2_detail_path,
        history_path=_rebaseline_temp_path(
            temp_root, SOURCE_SNAPSHOT_DIFF_HISTORY_CSV
        ),
        latest_path=_rebaseline_temp_path(temp_root, SOURCE_SNAPSHOT_DIFF_LATEST_CSV),
        docs_path=_rebaseline_temp_path(temp_root, SOURCE_SNAPSHOT_DIFF_DOCS_CSV),
    )
    if errors:
        raise RuntimeError(
            "independent v1/v2 diff validation failed: " + "; ".join(errors)
        )


def _publish_rebaseline_temp_bundle(
    temp_root: Path,
    *,
    root: Path = ROOT,
) -> None:
    targets = [
        root / relative_path
        for relative_path in SOURCE_SNAPSHOT_PROJECTION_REBASELINE_ALLOWED_ARTIFACT_PATHS
    ]
    staged = [
        temp_root / relative_path
        for relative_path in SOURCE_SNAPSHOT_PROJECTION_REBASELINE_ALLOWED_ARTIFACT_PATHS
    ]
    missing = [
        target.relative_to(root).as_posix()
        for target, staged_path in zip(targets, staged)
        if not staged_path.is_file() or staged_path.is_symlink()
    ]
    staged_files = {
        path.relative_to(temp_root).as_posix()
        for path in temp_root.rglob("*")
        if path.is_file()
    }
    expected_files = set(SOURCE_SNAPSHOT_PROJECTION_REBASELINE_ALLOWED_ARTIFACT_PATHS)
    target_symlinks = [
        target.relative_to(root).as_posix() for target in targets if target.is_symlink()
    ]
    if missing or staged_files != expected_files or target_symlinks:
        raise RuntimeError(
            "rebaseline temp bundle exact-set validation failed: "
            f"missing={missing}; extra={sorted(staged_files - expected_files)}; "
            f"target_symlinks={target_symlinks}"
        )
    backup_root = temp_root / "__backup__"
    prior_exists: dict[Path, bool] = {}
    for target in targets:
        prior_exists[target] = target.is_file()
        if target.is_file():
            backup = backup_root / target.relative_to(root)
            backup.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(target, backup)
    replaced: list[Path] = []
    try:
        for staged_path, target in zip(staged, targets):
            target.parent.mkdir(parents=True, exist_ok=True)
            _replace_rebaseline_path(staged_path, target)
            replaced.append(target)
    except BaseException as publish_error:
        rollback_errors: list[str] = []
        for target in reversed(replaced):
            try:
                if prior_exists[target]:
                    backup = backup_root / target.relative_to(root)
                    os.replace(backup, target)
                elif target.exists():
                    target.unlink()
            except OSError as rollback_error:
                rollback_errors.append(f"{target}: {rollback_error}")
        if rollback_errors:
            raise RuntimeError(
                "rebaseline transaction publish and rollback both failed: "
                f"publish={publish_error}; rollback={rollback_errors}"
            ) from publish_error
        raise


def build_and_write_source_snapshot_projection_rebaseline() -> None:
    """Build, independently validate, then atomically publish the v2 capture."""

    (
        v1_manifest,
        v1_detail,
        v1_manifest_payload,
        v1_detail_payload,
    ) = load_committed_v1_projection_predecessor(root=ROOT)
    repair_provenance = source_repair_provenance(root=ROOT)
    full_summary, full_detail = build_source_first_condition_audit()
    _projected_summary, projected_detail = build_source_first_condition_audit(
        observation_cutoff_date=SOURCE_SNAPSHOT_PROJECTION_CUTOFF_DATE,
    )
    v2_manifest = build_source_snapshot_projection_manifest(
        full_detail,
        projected_detail,
        artifact_version=SOURCE_SNAPSHOT_REBASELINE_ARTIFACT_VERSION,
        predecessor_manifest=v1_manifest,
        predecessor_detail=v1_detail,
        repair_provenance_payload=repair_provenance,
    )
    diff = build_projection_v1_v2_diff(
        v1_manifest,
        v1_detail,
        v2_manifest,
        projected_detail,
    )

    with tempfile.TemporaryDirectory(
        prefix=".revenue-source-projection-rebaseline-",
        dir=ROOT,
    ) as temporary_directory:
        temp_root = Path(temporary_directory)
        write_source_first_condition_audit(
            full_summary,
            full_detail,
            latest_csv_path=_rebaseline_temp_path(
                temp_root,
                ROOT
                / "output/latest/research_backtest/"
                "revenue_unreacted_range_source_first_condition_audit_latest.csv",
            ),
            detail_csv_path=_rebaseline_temp_path(
                temp_root,
                ROOT
                / "output/latest/research_backtest/"
                "revenue_unreacted_range_source_first_condition_audit_detail_latest.csv",
            ),
            history_csv_path=_rebaseline_temp_path(
                temp_root,
                ROOT
                / "output/history/research/"
                "revenue_unreacted_range_source_first_condition_audit.csv",
            ),
            docs_csv_path=_rebaseline_temp_path(
                temp_root,
                ROOT
                / "docs/latest/"
                "revenue_unreacted_range_source_first_condition_audit_latest.csv",
            ),
            latest_markdown_path=_rebaseline_temp_path(
                temp_root,
                ROOT
                / "output/latest/research_backtest/"
                "revenue_unreacted_range_source_first_condition_audit_latest.md",
            ),
            docs_markdown_path=_rebaseline_temp_path(
                temp_root,
                ROOT
                / "docs/latest/"
                "revenue_unreacted_range_source_first_condition_audit_latest.md",
            ),
        )
        v1_manifest_path = _rebaseline_temp_path(temp_root, VERSIONED_V1_MANIFEST_CSV)
        v1_detail_path = _rebaseline_temp_path(temp_root, VERSIONED_V1_DETAIL_CSV)
        v1_manifest_path.parent.mkdir(parents=True, exist_ok=True)
        v1_detail_path.parent.mkdir(parents=True, exist_ok=True)
        v1_manifest_path.write_bytes(v1_manifest_payload)
        v1_detail_path.write_bytes(v1_detail_payload)
        v2_manifest_path = _rebaseline_temp_path(temp_root, VERSIONED_V2_MANIFEST_CSV)
        v2_detail_path = _rebaseline_temp_path(temp_root, VERSIONED_V2_DETAIL_CSV)
        _write_projection_frame(v2_manifest_path, v2_manifest)
        _write_projection_frame(v2_detail_path, projected_detail)
        write_projection_v1_v2_diff(
            diff,
            history_path=_rebaseline_temp_path(temp_root, SOURCE_SNAPSHOT_DIFF_HISTORY_CSV),
            latest_path=_rebaseline_temp_path(temp_root, SOURCE_SNAPSHOT_DIFF_LATEST_CSV),
            docs_path=_rebaseline_temp_path(temp_root, SOURCE_SNAPSHOT_DIFF_DOCS_CSV),
        )
        _validate_rebaseline_temp_bundle(
            temp_root=temp_root,
            v1_manifest_path=v1_manifest_path,
            v1_detail_path=v1_detail_path,
            v2_manifest_path=v2_manifest_path,
            v2_detail_path=v2_detail_path,
        )
        _publish_rebaseline_temp_bundle(temp_root)


def build_and_write_source_snapshot_projection_operation_diff(
    *,
    anomaly_registry_path: Path,
    source_diff_path: Path,
    projection_v2_manifest_path: Path,
    projection_v2_detail_path: Path,
    original_detail_path: Path,
    corrected_summary_path: Path,
    corrected_detail_path: Path,
    corrected_report_path: Path,
    history_path: Path = SOURCE_SNAPSHOT_OPERATION_DIFF_HISTORY_CSV,
    latest_path: Path = SOURCE_SNAPSHOT_OPERATION_DIFF_LATEST_CSV,
    docs_path: Path = SOURCE_SNAPSHOT_OPERATION_DIFF_DOCS_CSV,
) -> pd.DataFrame:
    """Build the future corrected-chain operation diff only after all inputs exist.

    This callable intentionally is not a CLI stage yet.  The corrected summary,
    detail, and final report do not have approved canonical history paths, so the
    operation diff must remain fail-closed and unpublished until a separate
    consumer/writer migration binds those paths.
    """

    input_paths = tuple(
        Path(path)
        for path in (
            anomaly_registry_path,
            source_diff_path,
            projection_v2_manifest_path,
            projection_v2_detail_path,
            original_detail_path,
            corrected_summary_path,
            corrected_detail_path,
            corrected_report_path,
        )
    )
    missing = [path.as_posix() for path in input_paths if not path.is_file()]
    if missing:
        raise RuntimeError(
            "operation diff publication requires all eight exact-bound inputs "
            f"before write: {missing}"
        )

    def read_frame(path: Path) -> pd.DataFrame:
        return pd.read_csv(
            path,
            dtype=str,
            keep_default_na=False,
            low_memory=False,
        )

    inputs = (
        read_frame(input_paths[0]),
        read_frame(input_paths[1]),
        input_paths[2].read_bytes(),
        input_paths[3].read_bytes(),
        read_frame(input_paths[4]),
        read_frame(input_paths[5]),
        read_frame(input_paths[6]),
        read_frame(input_paths[7]),
    )
    frame = build_source_snapshot_operation_diff(*inputs)
    errors = validate_source_snapshot_operation_diff_independently(*inputs, frame)
    if errors:
        raise RuntimeError(
            "independent corrected-chain operation diff validation failed: "
            + "; ".join(errors)
        )
    write_source_snapshot_operation_diff(
        frame,
        history_path=history_path,
        latest_path=latest_path,
        docs_path=docs_path,
    )
    return frame


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
        source_projection_manifest=manifest,
        source_projection_artifact_version=(
            SOURCE_SNAPSHOT_LEGACY_ARTIFACT_VERSION
        ),
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
    validate_projection_binding(
        source_projection_manifest,
        source_first_detail,
        expected_artifact_version=SOURCE_SNAPSHOT_LEGACY_ARTIFACT_VERSION,
    )
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
        source_projection_manifest=source_projection_manifest,
        source_projection_artifact_version=(
            SOURCE_SNAPSHOT_LEGACY_ARTIFACT_VERSION
        ),
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
    training_source_projection_detail: pd.DataFrame,
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
        training_source_projection_detail=training_source_projection_detail,
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
            with source_snapshot_projection_rebaseline_stage_artifact_guard():
                build_and_write_source_snapshot_projection_rebaseline()
        elif args.stage == "source_snapshot_projection_chain":
            build_and_write_source_snapshot_projection_chain()
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
