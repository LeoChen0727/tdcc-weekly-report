from __future__ import annotations

from contextlib import contextmanager
from pathlib import Path
from typing import Iterator, Mapping

import pandas as pd

import validate_revenue_unreacted_range_forward_holdout as validator


ROOT = Path(__file__).resolve().parents[1]
MODEL_ID = "revenue_unreacted_range"
ARTIFACT_ID = "revenue_unreacted_range_forward_holdout_v2"
ARTIFACT_VERSION = "forward_holdout_v2_20260828"
PREREGISTRATION_PR_NUMBER = "462"
PREREGISTRATION_MERGE_COMMIT = "436c25cd0d037c3425ab2ac4fa76cb464cf96de4"
TRAINING_CUTOFF_DATE = "20260713"
BRIDGE_START_DATE = "20260714"
BRIDGE_END_DATE = "20260830"
HOLDOUT_START_DATE = "20260831"
SOURCE_PROJECTION_ARTIFACT_ID = (
    "revenue_unreacted_range_source_snapshot_projection"
)
SOURCE_PROJECTION_ARTIFACT_VERSION = "source_snapshot_projection_v2_20260822"
PROJECTED_EPISODE_ROW_COUNT = 19565
PROJECTED_EPISODE_SEMANTIC_SHA256 = (
    "dacd5046e8af9abcd766b11b9557035481cc82af9d7fba746a8dad1ff183a967"
)
MIGRATION_AUTHORIZATION_REFERENCE = "user_authorized_2A_20260828"
DATA_CONTRACT_VERSION = "revenue_low_mid_falling_forward_holdout_data_v2_20260828"
DATA_CONTRACT = {
    "training_cutoff_date": TRAINING_CUTOFF_DATE,
    "bridge_start_date": BRIDGE_START_DATE,
    "bridge_end_date": BRIDGE_END_DATE,
    "holdout_start_date": HOLDOUT_START_DATE,
    "source_projection_artifact_id": SOURCE_PROJECTION_ARTIFACT_ID,
    "source_projection_artifact_version": SOURCE_PROJECTION_ARTIFACT_VERSION,
    "projected_episode_row_count": PROJECTED_EPISODE_ROW_COUNT,
    "projected_episode_semantic_sha256": PROJECTED_EPISODE_SEMANTIC_SHA256,
    "source_artifact_id": validator.SOURCE_ARTIFACT_ID,
    "source_artifact_version": validator.SOURCE_ARTIFACT_VERSION,
    "migration_authorization_reference": MIGRATION_AUTHORIZATION_REFERENCE,
    "pre_start_empty_capture_allowed": True,
    "append_only_history": True,
    "research_only": True,
    "formal_model_use_allowed": False,
    "approved_for_daily": False,
    "presentation_allowed": False,
    "promotion_evidence_allowed": False,
    "production_change": False,
}
DATA_CONTRACT_SHA256 = validator._json_sha(DATA_CONTRACT)
SELECTED_V2_MANIFEST_CANONICAL_SHA256 = (
    "74b51a715c560777ea302fe559d89f74575ff94381c8cee1fa49496c25b7db2b"
)

DEFAULT_PATHS = {
    "manifest": ROOT
    / f"output/latest/research_backtest/{ARTIFACT_ID}_manifest_latest.csv",
    "detail": ROOT
    / f"output/latest/research_backtest/{ARTIFACT_ID}_event_detail_latest.csv",
    "summary": ROOT
    / f"output/latest/research_backtest/{ARTIFACT_ID}_maturity_status_latest.csv",
    "comparison": ROOT
    / f"output/latest/research_backtest/{ARTIFACT_ID}_comparison_latest.csv",
    "anomaly": ROOT
    / f"output/latest/research_backtest/{ARTIFACT_ID}_anomaly_sensitivity_latest.csv",
    "manifest_history": ROOT
    / f"output/history/research/{ARTIFACT_ID}_manifest.csv",
    "detail_history": ROOT
    / f"output/history/research/{ARTIFACT_ID}_event_detail.csv",
    "summary_history": ROOT
    / f"output/history/research/{ARTIFACT_ID}_maturity_status.csv",
    "comparison_history": ROOT
    / f"output/history/research/{ARTIFACT_ID}_comparison.csv",
    "anomaly_history": ROOT
    / f"output/history/research/{ARTIFACT_ID}_anomaly_sensitivity.csv",
    "source_manifest": ROOT
    / "output/latest/research_backtest/"
    "revenue_unreacted_range_source_snapshot_projection_manifest_latest.csv",
}


def _validator_overrides() -> dict[str, object]:
    return {
        "ARTIFACT_ID": ARTIFACT_ID,
        "ARTIFACT_VERSION": ARTIFACT_VERSION,
        "PR462_PROJECTED_EPISODE_ROW_COUNT": PROJECTED_EPISODE_ROW_COUNT,
        "PR462_PROJECTED_EPISODE_SEMANTIC_SHA256": (
            PROJECTED_EPISODE_SEMANTIC_SHA256
        ),
        "BRIDGE_START_DATE": BRIDGE_START_DATE,
        "BRIDGE_END_DATE": BRIDGE_END_DATE,
        "HOLDOUT_START_DATE": HOLDOUT_START_DATE,
        "SOURCE_PROJECTION_ARTIFACT_VERSION": (
            SOURCE_PROJECTION_ARTIFACT_VERSION
        ),
        "DATA_CONTRACT_VERSION": DATA_CONTRACT_VERSION,
        "DATA_CONTRACT": DATA_CONTRACT,
        "DATA_CONTRACT_SHA256": DATA_CONTRACT_SHA256,
        "ALLOW_PRE_START_EMPTY_CAPTURE": True,
        "DEFAULT_PATHS": DEFAULT_PATHS,
    }


@contextmanager
def validator_v2_context() -> Iterator[None]:
    """Run the independent replay engine under the v2 evidence envelope."""

    overrides = _validator_overrides()
    previous = {name: getattr(validator, name) for name in overrides}
    try:
        for name, value in overrides.items():
            setattr(validator, name, value)
        yield
    finally:
        for name, value in previous.items():
            setattr(validator, name, value)


def validate_frames(
    manifest: pd.DataFrame,
    detail: pd.DataFrame,
    summary: pd.DataFrame,
    comparison: pd.DataFrame,
    anomaly: pd.DataFrame,
    *,
    source_detail: pd.DataFrame,
    daily_by_stock: Mapping[str, pd.DataFrame],
    source_manifest: pd.DataFrame,
    history_frames: Mapping[str, pd.DataFrame] | None = None,
    immutable_history_base_frames: Mapping[str, pd.DataFrame] | None = None,
) -> list[str]:
    if len(source_manifest) != 1:
        return ["v2 selected source manifest must contain exactly one row"]
    selected = source_manifest.iloc[0]
    expected_selected = {
        "artifact_id": SOURCE_PROJECTION_ARTIFACT_ID,
        "artifact_version": SOURCE_PROJECTION_ARTIFACT_VERSION,
        "projection_version": SOURCE_PROJECTION_ARTIFACT_VERSION,
        "cutoff_date": TRAINING_CUTOFF_DATE,
        "projected_episode_row_count": str(PROJECTED_EPISODE_ROW_COUNT),
        "projected_episode_semantic_sha256": PROJECTED_EPISODE_SEMANTIC_SHA256,
        "candidate_status": "generated_pending_supersede_approval",
    }
    for column, expected_value in expected_selected.items():
        if str(selected.get(column, "")).strip() != expected_value:
            return [f"v2 selected source manifest drift: {column}"]
    observed_manifest_sha = validator._frame_sha(source_manifest)
    if observed_manifest_sha != SELECTED_V2_MANIFEST_CANONICAL_SHA256:
        return [
            "v2 selected source manifest canonical SHA-256 drift: "
            f"expected={SELECTED_V2_MANIFEST_CANONICAL_SHA256} "
            f"observed={observed_manifest_sha}"
        ]
    with validator_v2_context():
        return validator.validate_frames(
            manifest,
            detail,
            summary,
            comparison,
            anomaly,
            source_detail=source_detail,
            daily_by_stock=daily_by_stock,
            source_manifest=source_manifest,
            history_frames=history_frames,
            immutable_history_base_frames=immutable_history_base_frames,
        )


def load_history_base_frames_from_git(
    base_ref: str,
    *,
    history_paths: Mapping[str, Path] | None = None,
) -> dict[str, pd.DataFrame]:
    with validator_v2_context():
        return validator.load_history_base_frames_from_git(
            base_ref,
            history_paths=history_paths,
        )


def main(argv: list[str] | None = None) -> int:
    with validator_v2_context():
        return validator.main(argv)


if __name__ == "__main__":
    raise SystemExit(main())
