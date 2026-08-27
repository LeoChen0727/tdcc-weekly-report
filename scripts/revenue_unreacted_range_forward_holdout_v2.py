from __future__ import annotations

from contextlib import contextmanager
import hashlib
from pathlib import Path
import subprocess
from typing import Callable, Iterator, Mapping

import pandas as pd

import revenue_unreacted_range_forward_holdout as engine


ROOT = Path(__file__).resolve().parents[1]
MODEL_ID = "revenue_unreacted_range"
ARTIFACT_ID = "revenue_unreacted_range_forward_holdout_v2"
ARTIFACT_VERSION = "forward_holdout_v2_20260828"

# The business rule and its original PR #462 preregistration remain unchanged.
# This family changes only the immutable source-projection binding and starts a
# new, future-only observation window after the 2A authorization.
PREREGISTRATION_PR_NUMBER = engine.PREREGISTRATION_PR_NUMBER
PREREGISTRATION_MERGE_COMMIT = engine.PREREGISTRATION_MERGE_COMMIT
TRAINING_CUTOFF_DATE = engine.TRAINING_CUTOFF_DATE
BRIDGE_START_DATE = "20260714"
BRIDGE_END_DATE = "20260830"
HOLDOUT_START_DATE = "20260831"
MIGRATION_AUTHORIZATION_REFERENCE = "user_authorized_2A_20260828"

SOURCE_PROJECTION_ARTIFACT_ID = engine.SOURCE_PROJECTION_ARTIFACT_ID
SOURCE_PROJECTION_ARTIFACT_VERSION = "source_snapshot_projection_v2_20260822"
PROJECTED_EPISODE_ROW_COUNT = 19565
PROJECTED_EPISODE_SEMANTIC_SHA256 = (
    "dacd5046e8af9abcd766b11b9557035481cc82af9d7fba746a8dad1ff183a967"
)

RULE_CONTRACT_VERSION = engine.RULE_CONTRACT_VERSION
RULE_CONTRACT = engine.RULE_CONTRACT
RULE_CANONICAL_SHA256 = engine.RULE_CANONICAL_SHA256
FINANCIAL_STATEMENT_SCOPE = engine.FINANCIAL_STATEMENT_SCOPE
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
    "source_artifact_id": engine.SOURCE_ARTIFACT_ID,
    "source_artifact_version": engine.SOURCE_ARTIFACT_VERSION,
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
DATA_CONTRACT_SHA256 = engine._canonical_json_sha256(DATA_CONTRACT)


def _output_relative_paths() -> dict[str, str]:
    return {
        name: relative
        for surface, base in (
            ("latest", "output/latest/research_backtest"),
            ("history", "output/history/research"),
            ("docs", "docs/latest"),
        )
        for artifact, suffix in (
            ("manifest", "manifest"),
            ("detail", "event_detail"),
            ("summary", "maturity_status"),
            ("comparison", "comparison"),
            ("anomaly", "anomaly_sensitivity"),
        )
        for name, relative in (
            (
                f"{artifact}_{surface}",
                (
                    f"{base}/{ARTIFACT_ID}_{suffix}_latest.csv"
                    if surface in {"latest", "docs"}
                    else f"{base}/{ARTIFACT_ID}_{suffix}.csv"
                ),
            ),
        )
    }


DEFAULT_OUTPUT_RELATIVE_PATHS = _output_relative_paths()
REPLAY_SOURCE_OUTPUT_RELATIVE_PATHS = {
    "replay_source_latest": (
        f"output/latest/research_backtest/{ARTIFACT_ID}_replay_source_detail_latest.csv"
    ),
    "replay_source_docs": (
        f"docs/latest/{ARTIFACT_ID}_replay_source_detail_latest.csv"
    ),
}
FORWARD_HOLDOUT_V2_ALLOWED_ARTIFACT_PATHS = tuple(
    sorted(
        (
            *DEFAULT_OUTPUT_RELATIVE_PATHS.values(),
            *REPLAY_SOURCE_OUTPUT_RELATIVE_PATHS.values(),
        )
    )
)

SELECTED_V2_MANIFEST_CANONICAL_SHA256 = (
    "74b51a715c560777ea302fe559d89f74575ff94381c8cee1fa49496c25b7db2b"
)
V1_EXACT17_BUNDLE_SHA256 = (
    "445b53afa31525e18adb86b91d9b90f055d1d9858cc4643038e256431537488c"
)
V1_EXACT17_PATH_EVIDENCE = {
    "docs/latest/revenue_unreacted_range_forward_holdout_anomaly_sensitivity_latest.csv": (3996, "83649279ca8661d159a7e40fc020c0ee5818c69eafb66124b55decb82f4d8efa"),
    "docs/latest/revenue_unreacted_range_forward_holdout_comparison_latest.csv": (2058, "1996e6bfdf36f975d1eb6b6e3fe9152b8eefd5800db6a93cfbcfe47deff25803"),
    "docs/latest/revenue_unreacted_range_forward_holdout_event_detail_latest.csv": (71084, "e7251aa2824b7b05bf856b70aa0f5986119f88f1b79c2eb85b660def19f9a5e9"),
    "docs/latest/revenue_unreacted_range_forward_holdout_manifest_latest.csv": (122637, "5dcf5c122a4daea93fac3fd61e39b662e0c84725ddd407c93d7e04b257df90d3"),
    "docs/latest/revenue_unreacted_range_forward_holdout_maturity_status_latest.csv": (2334, "b091ee5d56c04fa95b27e58c129337394b254332ec4706aefb2953e177c37b47"),
    "docs/latest/revenue_unreacted_range_forward_holdout_replay_source_detail_latest.csv": (29640066, "b4c0df788ff427f64b562c53f623e92f6d2ee5d910c33bc1fef26dde9f8400ec"),
    "output/history/research/revenue_unreacted_range_forward_holdout_anomaly_sensitivity.csv": (7420, "e3495e76e94550f2d17f57cd8b8033f2dba7c672de1aa72f4df19414df0f24ca"),
    "output/history/research/revenue_unreacted_range_forward_holdout_comparison.csv": (3569, "64ab39b8e190c8c017119f71384c2f4052f976bb20103607c94fc89a16dc0d81"),
    "output/history/research/revenue_unreacted_range_forward_holdout_event_detail.csv": (125550, "d4fd164e02757b23c9510cb28da31f04a09340ad09288b962d4327da2f288759"),
    "output/history/research/revenue_unreacted_range_forward_holdout_manifest.csv": (244109, "c664a002bd543153305c0f081b4235198d66011a00600827c79a947783457085"),
    "output/history/research/revenue_unreacted_range_forward_holdout_maturity_status.csv": (4064, "27b0c6e3c49290c1294037b31075f268a1700aedf906c4a113011e798cbafe12"),
    "output/latest/research_backtest/revenue_unreacted_range_forward_holdout_anomaly_sensitivity_latest.csv": (3996, "83649279ca8661d159a7e40fc020c0ee5818c69eafb66124b55decb82f4d8efa"),
    "output/latest/research_backtest/revenue_unreacted_range_forward_holdout_comparison_latest.csv": (2058, "1996e6bfdf36f975d1eb6b6e3fe9152b8eefd5800db6a93cfbcfe47deff25803"),
    "output/latest/research_backtest/revenue_unreacted_range_forward_holdout_event_detail_latest.csv": (71084, "e7251aa2824b7b05bf856b70aa0f5986119f88f1b79c2eb85b660def19f9a5e9"),
    "output/latest/research_backtest/revenue_unreacted_range_forward_holdout_manifest_latest.csv": (122637, "5dcf5c122a4daea93fac3fd61e39b662e0c84725ddd407c93d7e04b257df90d3"),
    "output/latest/research_backtest/revenue_unreacted_range_forward_holdout_maturity_status_latest.csv": (2334, "b091ee5d56c04fa95b27e58c129337394b254332ec4706aefb2953e177c37b47"),
    "output/latest/research_backtest/revenue_unreacted_range_forward_holdout_replay_source_detail_latest.csv": (29640066, "b4c0df788ff427f64b562c53f623e92f6d2ee5d910c33bc1fef26dde9f8400ec"),
}


def validate_selected_v2_manifest(source_manifest: pd.DataFrame) -> None:
    """Bind the v2 family to the one selected canonical v2 source manifest."""

    if len(source_manifest) != 1:
        raise RuntimeError("forward holdout v2 selected manifest must have one row")
    row = source_manifest.iloc[0]
    expected = {
        "artifact_id": SOURCE_PROJECTION_ARTIFACT_ID,
        "artifact_version": SOURCE_PROJECTION_ARTIFACT_VERSION,
        "projection_version": SOURCE_PROJECTION_ARTIFACT_VERSION,
        "cutoff_date": TRAINING_CUTOFF_DATE,
        "projected_episode_row_count": str(PROJECTED_EPISODE_ROW_COUNT),
        "projected_episode_semantic_sha256": PROJECTED_EPISODE_SEMANTIC_SHA256,
        "candidate_status": "generated_pending_supersede_approval",
    }
    for column, expected_value in expected.items():
        if str(row.get(column, "")).strip() != expected_value:
            raise RuntimeError(
                f"forward holdout v2 selected manifest drift: {column}"
            )
    observed_sha = engine._canonical_frame_sha256(source_manifest)
    if observed_sha != SELECTED_V2_MANIFEST_CANONICAL_SHA256:
        raise RuntimeError(
            "forward holdout v2 selected manifest canonical SHA-256 drift: "
            f"expected={SELECTED_V2_MANIFEST_CANONICAL_SHA256} observed={observed_sha}"
        )


def _git_worktree_root(base: Path) -> Path | None:
    result = subprocess.run(
        ["git", "rev-parse", "--show-toplevel"],
        cwd=base,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
        text=True,
    )
    if result.returncode != 0:
        return None
    resolved = Path(result.stdout.strip()).resolve()
    return resolved if resolved == base.resolve() else None


def _git_blob_payload(base: Path, relative: str, git_ref: str) -> bytes:
    result = subprocess.run(
        ["git", "cat-file", "blob", f"{git_ref}:{relative}"],
        cwd=base,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
    )
    if result.returncode != 0:
        detail = result.stderr.decode("utf-8", errors="replace").strip()
        raise RuntimeError(
            "forward holdout v1 exact17 Git blob missing: "
            f"{git_ref}:{relative}; {detail or 'git cat-file failed'}"
        )
    return result.stdout


def _dirty_v1_exact17_paths(base: Path) -> list[str]:
    relative_paths = sorted(V1_EXACT17_PATH_EVIDENCE)
    result = subprocess.run(
        [
            "git",
            "status",
            "--porcelain=v1",
            "--untracked-files=all",
            "--",
            *relative_paths,
        ],
        cwd=base,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
        text=True,
    )
    if result.returncode != 0:
        detail = result.stderr.strip() or result.stdout.strip()
        raise RuntimeError(
            "forward holdout v1 exact17 Git dirty check failed: "
            f"{detail or 'git status failed'}"
        )
    return [line for line in result.stdout.splitlines() if line.strip()]


def validate_v1_exact17_freeze(
    *,
    root: Path | str = ROOT,
    git_ref: str = "HEAD",
) -> str:
    """Fail closed on immutable Git blobs and any v1 working-tree mutation.

    Git stores the authorized evidence as LF-normalized blobs.  A clean Windows
    checkout may materialize those text files with CRLF, so filesystem bytes are
    not an identity check.  In a repository, compare the immutable Git blobs and
    separately require Git to report all exact17 paths clean.  Filesystem-byte
    mode is retained only for isolated test fixtures outside a Git worktree.
    """

    base = Path(root)
    git_root = _git_worktree_root(base)
    if git_root is not None:
        dirty = _dirty_v1_exact17_paths(base)
        if dirty:
            raise RuntimeError(
                "forward holdout v1 exact17 working-tree drift: " + "; ".join(dirty)
            )
    lines: list[str] = []
    for relative in sorted(V1_EXACT17_PATH_EVIDENCE):
        if git_root is not None:
            payload = _git_blob_payload(base, relative, git_ref)
        else:
            path = base / relative
            if not path.is_file():
                raise RuntimeError(
                    f"forward holdout v1 exact17 path missing: {relative}"
                )
            payload = path.read_bytes()
        observed = (len(payload), hashlib.sha256(payload).hexdigest())
        expected = V1_EXACT17_PATH_EVIDENCE[relative]
        if observed != expected:
            raise RuntimeError(
                "forward holdout v1 exact17 drift: "
                f"{relative}; expected={expected} observed={observed}"
            )
        lines.append(f"{relative}|{observed[0]}|{observed[1]}\n")
    bundle_sha = hashlib.sha256("".join(lines).encode("utf-8")).hexdigest()
    if bundle_sha != V1_EXACT17_BUNDLE_SHA256:
        raise RuntimeError(
            "forward holdout v1 exact17 bundle SHA-256 drift: "
            f"expected={V1_EXACT17_BUNDLE_SHA256} observed={bundle_sha}"
        )
    return bundle_sha


def _engine_overrides() -> dict[str, object]:
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
        "DEFAULT_OUTPUT_RELATIVE_PATHS": DEFAULT_OUTPUT_RELATIVE_PATHS,
        "REPLAY_SOURCE_OUTPUT_RELATIVE_PATHS": (
            REPLAY_SOURCE_OUTPUT_RELATIVE_PATHS
        ),
        "FORWARD_HOLDOUT_ALLOWED_ARTIFACT_PATHS": (
            FORWARD_HOLDOUT_V2_ALLOWED_ARTIFACT_PATHS
        ),
    }


@contextmanager
def engine_v2_context() -> Iterator[None]:
    """Apply the v2 data envelope without changing the frozen v1 defaults."""

    overrides = _engine_overrides()
    previous = {name: getattr(engine, name) for name in overrides}
    try:
        for name, value in overrides.items():
            setattr(engine, name, value)
        yield
    finally:
        for name, value in previous.items():
            setattr(engine, name, value)


def build_forward_holdout(
    source_detail: pd.DataFrame,
    daily_by_stock: Mapping[str, pd.DataFrame],
    *,
    source_manifest: pd.DataFrame,
    generated_at: str | None = None,
) -> tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    validate_selected_v2_manifest(source_manifest)
    with engine_v2_context():
        return engine.build_forward_holdout(
            source_detail,
            daily_by_stock,
            source_manifest=source_manifest,
            generated_at=generated_at,
        )


def write_forward_holdout(
    manifest: pd.DataFrame,
    detail: pd.DataFrame,
    summary: pd.DataFrame,
    comparison: pd.DataFrame,
    anomaly_sensitivity: pd.DataFrame,
    *,
    replay_source_detail: pd.DataFrame | None = None,
    output_root: Path | str = ROOT,
    history_base_ref: str | None = None,
    immutable_history_bases: Mapping[str, pd.DataFrame] | None = None,
    post_publish_check: Callable[[Mapping[str, Path]], None] | None = None,
) -> dict[str, Path]:
    with engine_v2_context():
        return engine.write_forward_holdout(
            manifest,
            detail,
            summary,
            comparison,
            anomaly_sensitivity,
            replay_source_detail=replay_source_detail,
            output_root=output_root,
            history_base_ref=history_base_ref,
            immutable_history_bases=immutable_history_bases,
            post_publish_check=post_publish_check,
        )


def build_current_forward_holdout() -> tuple[
    pd.DataFrame,
    pd.DataFrame,
    pd.DataFrame,
    pd.DataFrame,
    pd.DataFrame,
]:
    with engine_v2_context():
        source_detail, daily_by_stock, source_manifest = (
            engine._materialize_current_forward_holdout_inputs()
        )
        validate_selected_v2_manifest(source_manifest)
        return engine.build_forward_holdout(
            source_detail,
            daily_by_stock,
            source_manifest=source_manifest,
        )


def build_and_write_current_forward_holdout(
    *,
    final_validation: Callable[..., None] | None = None,
) -> dict[str, Path]:
    # The original orchestrator imports its independent validator by name at
    # runtime.  Apply the separately owned v2 validator envelope for the full
    # build/write/replay transaction, then restore both v1 modules exactly.
    from validate_revenue_unreacted_range_forward_holdout_v2 import (
        validator_v2_context,
    )

    with engine_v2_context(), validator_v2_context():
        selected_manifest = engine.load_source_snapshot_projection_manifest()
        validate_selected_v2_manifest(selected_manifest)
        return engine.build_and_write_current_forward_holdout(
            final_validation=final_validation
        )
