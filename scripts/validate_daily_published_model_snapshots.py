from __future__ import annotations

import argparse
import re
import sys
from collections.abc import Collection
from pathlib import Path

import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent))

from tracking_utils import LATEST_DIR, normalize_date, read_csv, safe_str  # noqa: E402
from update_daily_published_model_snapshots import (  # noqa: E402
    ARTIFACTS,
    MANIFEST_PATH,
    MANIFEST_COLUMNS,
    SNAPSHOT_DIR,
    SnapshotArtifact,
    approved_source_repository_path,
    freshness_state,
    manifest_v1_sha256_candidates,
    normalize_known_manifest_schema,
    repository_root_for_snapshot_dir,
    resolve_approved_manifest_path,
    resolve_manifest_snapshot_path,
    selected_artifacts,
    sha256_file,
    validate_artifact_frame,
    validate_revision_group,
)


FORBIDDEN_SNAPSHOT_PATH_FRAGMENTS = (
    "volume_breakout_operation_pdf_preview",
    "volume_breakout_confirmed_operation_rank",
    "volume_breakout_pending_operation_queue",
    "historical_pattern_operation_registry",
    "approved_operation_patterns",
    "daily_model_parameter_research",
    "daily_model_parameter_recommendations",
    "research/",
    "research\\",
    "tdcc_signals/",
    "tdcc_signals\\",
)


def true_text(value: object) -> bool:
    return safe_str(value).lower() in {"true", "1", "yes", "y"}


def warrant_grace_allows_publish(row: dict[str, str]) -> bool:
    return bool(
        safe_str(row.get("warrant_source_status", "")) == "warning_grace"
        and true_text(row.get("warrant_daily_publish_allowed", ""))
        and safe_str(row.get("warrant_pdf_visibility", "")) == "hidden_unavailable"
        and not true_text(row.get("warrant_model_effect_allowed", ""))
        and not true_text(row.get("warrant_pdf_effect_allowed", ""))
    )


def load_manifest(manifest_path: Path = MANIFEST_PATH) -> pd.DataFrame:
    manifest = read_csv(manifest_path, dtype=str)
    if manifest.empty:
        raise RuntimeError(f"{manifest_path.as_posix()} is missing or empty")
    return normalize_known_manifest_schema(
        manifest,
        context=f"daily snapshot manifest {manifest_path.as_posix()}",
    )


def validate_manifest_paths(
    manifest: pd.DataFrame,
    snapshot_dir: Path = SNAPSHOT_DIR,
) -> list[str]:
    errors: list[str] = []
    try:
        repository_root = repository_root_for_snapshot_dir(snapshot_dir)
    except RuntimeError as exc:
        return [str(exc)]
    artifacts_by_id = {artifact.artifact_id: artifact for artifact in ARTIFACTS}
    for _, row in manifest.iterrows():
        source_path = safe_str(row.get("source_path", ""))
        snapshot_path = safe_str(row.get("snapshot_path", ""))
        combined = f"{source_path}\n{snapshot_path}"
        for fragment in FORBIDDEN_SNAPSHOT_PATH_FRAGMENTS:
            if fragment in combined:
                errors.append(f"{snapshot_path}: forbidden research/backtest artifact fragment {fragment}")
        artifact_id = safe_str(row.get("artifact_id", ""))
        artifact = artifacts_by_id.get(artifact_id)
        if artifact is None:
            continue
        report_date = normalize_date(row.get("snapshot_report_date", ""))
        revision = safe_str(row.get("snapshot_revision", ""))
        snapshot_sha = safe_str(row.get("snapshot_sha256", ""))
        reason = safe_str(row.get("revision_reason", ""))
        try:
            resolve_approved_manifest_path(
                source_path,
                repository_root=repository_root,
                approved_relative_path=approved_source_repository_path(artifact),
                path_kind="source_path",
            )
        except RuntimeError as exc:
            errors.append(f"{report_date}/{artifact_id}/{revision}: {exc}")
        try:
            resolve_manifest_snapshot_path(
                snapshot_path,
                repository_root=repository_root,
                artifact=artifact,
                report_date=report_date,
                snapshot_revision=revision,
                snapshot_sha256=snapshot_sha,
                revision_reason=reason,
            )
        except RuntimeError as exc:
            errors.append(f"{report_date}/{artifact_id}/{revision}: {exc}")
    return errors


def validate_no_unreferenced_versioned_snapshots(
    manifest: pd.DataFrame,
    snapshot_dir: Path = SNAPSHOT_DIR,
    artifacts: Collection[SnapshotArtifact] = ARTIFACTS,
    report_date: str = "",
) -> list[str]:
    """Reject content-addressed snapshot files absent from the manifest."""

    if not snapshot_dir.exists():
        return []
    repository_root = repository_root_for_snapshot_dir(snapshot_dir)
    artifacts_by_id = {artifact.artifact_id: artifact for artifact in artifacts}
    referenced: set[Path] = set()
    for _, row in manifest.iterrows():
        artifact = artifacts_by_id.get(safe_str(row.get("artifact_id", "")))
        if artifact is None:
            continue
        try:
            referenced.add(
                resolve_manifest_snapshot_path(
                    row.get("snapshot_path", ""),
                    repository_root=repository_root,
                    artifact=artifact,
                    report_date=normalize_date(row.get("snapshot_report_date", "")),
                    snapshot_revision=safe_str(row.get("snapshot_revision", "")),
                    snapshot_sha256=safe_str(row.get("snapshot_sha256", "")),
                    revision_reason=safe_str(row.get("revision_reason", "")),
                )
            )
        except RuntimeError:
            continue
    patterns = tuple(
        re.compile(
            rf"{re.escape(artifact.snapshot_stem)}_\d{{8}}_r[1-9][0-9]*_[0-9a-f]{{12}}\.csv"
        )
        for artifact in artifacts
    )
    errors: list[str] = []
    for path in snapshot_dir.glob("*.csv"):
        if not any(pattern.fullmatch(path.name) for pattern in patterns):
            continue
        if report_date and f"_{report_date}_" not in path.name:
            continue
        if path.resolve() not in referenced:
            errors.append(
                "unreferenced versioned daily snapshot file is forbidden: "
                f"{path.as_posix()}"
            )
    return errors


def validate_historical_snapshot_frame(
    path: Path,
    artifact: SnapshotArtifact,
    report_date: str,
) -> pd.DataFrame:
    """Validate historical shape/date facts without applying today's schema."""

    df = pd.read_csv(path, dtype=str)
    for col in artifact.date_columns:
        if col not in df.columns:
            raise RuntimeError(f"{path.as_posix()} missing required date column: {col}")
        values = {normalize_date(value) for value in df[col].tolist()}
        values.discard("")
        if values and values != {report_date}:
            raise RuntimeError(
                f"{path.as_posix()} column {col} must match report date "
                f"{report_date}; observed={sorted(values)}"
            )
    return df


def validate_current_report_snapshots(
    latest_dir: Path = LATEST_DIR,
    snapshot_dir: Path = SNAPSHOT_DIR,
    manifest_path: Path = MANIFEST_PATH,
    artifact_ids: Collection[str] | None = None,
    phase: str = "full",
) -> list[str]:
    errors: list[str] = []
    if phase not in {"full", "runtime"}:
        return [f"unsupported daily snapshot validation phase: {phase}"]
    try:
        state = freshness_state(latest_dir)
    except Exception as exc:
        return [str(exc)]

    report_date = state["main_price_date"]
    try:
        full_manifest = load_manifest(manifest_path)
    except Exception as exc:
        return [str(exc)]

    manifest = full_manifest.copy()
    if phase == "runtime":
        manifest = manifest[
            manifest["snapshot_report_date"].map(normalize_date).eq(report_date)
        ].copy()

    try:
        artifacts = selected_artifacts(artifact_ids)
    except RuntimeError as exc:
        return [str(exc)]
    selected_ids = {artifact.artifact_id for artifact in artifacts}
    if artifact_ids is None:
        unknown_manifest_ids = sorted(
            {
                safe_str(value)
                for value in manifest["artifact_id"].tolist()
                if safe_str(value) not in selected_ids
            }
        )
        if unknown_manifest_ids:
            errors.append(
                "manifest contains unknown artifact_id rows: "
                f"{unknown_manifest_ids}"
            )
    manifest = manifest[manifest["artifact_id"].map(safe_str).isin(selected_ids)].copy()

    errors.extend(validate_manifest_paths(manifest, snapshot_dir))
    errors.extend(
        validate_no_unreferenced_versioned_snapshots(
            manifest,
            snapshot_dir,
            artifacts,
            report_date=report_date if phase == "runtime" else "",
        )
    )
    manifest = manifest.copy()
    manifest["_report_date"] = manifest["snapshot_report_date"].map(normalize_date)
    duplicate_keys = manifest.duplicated(
        subset=["_report_date", "artifact_id", "snapshot_revision"],
        keep=False,
    )
    if duplicate_keys.any():
        duplicates = manifest.loc[
            duplicate_keys,
            ["snapshot_report_date", "artifact_id", "snapshot_revision"],
        ].to_dict("records")
        errors.append(f"manifest has duplicate snapshot revision rows: {duplicates}")

    duplicate_paths = manifest["snapshot_path"].astype(str).duplicated(keep=False)
    if duplicate_paths.any():
        paths = sorted(set(manifest.loc[duplicate_paths, "snapshot_path"].astype(str)))
        errors.append(f"manifest reuses immutable snapshot paths: {paths}")

    artifacts_by_id = {artifact.artifact_id: artifact for artifact in artifacts}
    repository_root = repository_root_for_snapshot_dir(snapshot_dir)
    active_rows: dict[tuple[str, str], pd.Series] = {}
    for (row_report_date, artifact_id), group in manifest.groupby(
        ["_report_date", "artifact_id"],
        sort=False,
        dropna=False,
    ):
        label_date = safe_str(row_report_date)
        label_artifact = safe_str(artifact_id)
        try:
            ordered = validate_revision_group(
                group.drop(columns=["_report_date"]),
                report_date=label_date,
                artifact_id=label_artifact,
            )
        except RuntimeError as exc:
            errors.append(str(exc))
            continue
        canonical_payloads: set[str] = set()
        for _, revision_row in ordered.iterrows():
            revision = safe_str(revision_row.get("snapshot_revision", ""))
            try:
                revision_path = resolve_manifest_snapshot_path(
                    revision_row.get("snapshot_path", ""),
                    repository_root=repository_root,
                    artifact=artifacts_by_id[label_artifact],
                    report_date=label_date,
                    snapshot_revision=revision,
                    snapshot_sha256=safe_str(
                        revision_row.get("snapshot_sha256", "")
                    ),
                    revision_reason=safe_str(
                        revision_row.get("revision_reason", "")
                    ),
                )
                if revision_path.is_file():
                    canonical_sha = sha256_file(revision_path)
                    if canonical_sha in canonical_payloads:
                        errors.append(
                            f"{label_date}/{label_artifact}/{revision}: "
                            "canonical duplicate payload revision is forbidden"
                        )
                    canonical_payloads.add(canonical_sha)
            except (KeyError, RuntimeError):
                pass
        if not ordered.empty:
            active_rows[(label_date, label_artifact)] = ordered.iloc[-1]

    current = manifest[manifest["_report_date"].eq(report_date)]
    required_artifact_ids = selected_ids
    observed_artifact_ids = {safe_str(value) for value in current["artifact_id"].tolist()}
    missing = sorted(required_artifact_ids - observed_artifact_ids)
    if missing:
        errors.append(f"manifest missing current report_date={report_date} artifact rows: {missing}")

    for _, row in manifest.iterrows():
        row_report_date = safe_str(row.get("_report_date", ""))
        artifact_id = safe_str(row.get("artifact_id", ""))
        revision = safe_str(row.get("snapshot_revision", ""))
        label = f"{row_report_date}/{artifact_id}/{revision}"
        artifact = artifacts_by_id.get(artifact_id)
        if artifact is None:
            errors.append(f"{label}: unknown artifact_id in manifest")
            continue

        snapshot_sha = safe_str(row.get("snapshot_sha256", ""))
        try:
            snapshot = resolve_manifest_snapshot_path(
                row.get("snapshot_path", ""),
                repository_root=repository_root,
                artifact=artifact,
                report_date=row_report_date,
                snapshot_revision=revision,
                snapshot_sha256=snapshot_sha,
                revision_reason=safe_str(row.get("revision_reason", "")),
            )
        except RuntimeError as exc:
            errors.append(f"{label}: {exc}")
            continue

        if not snapshot.exists():
            errors.append(f"{label}: snapshot missing: {snapshot.as_posix()}")
            continue

        accepted_hashes = (
            manifest_v1_sha256_candidates(snapshot)
            if revision == "r1"
            else {sha256_file(snapshot)}
        )
        if snapshot_sha not in accepted_hashes:
            errors.append(f"{label}: snapshot_sha256 does not match snapshot file")
        if safe_str(row.get("source_sha256", "")) != snapshot_sha:
            errors.append(f"{label}: source_sha256 must equal snapshot_sha256")

        try:
            df = validate_historical_snapshot_frame(
                snapshot,
                artifact,
                row_report_date,
            )
        except Exception as exc:
            errors.append(f"{label}: failed to read snapshot CSV: {exc}")
            continue
        if safe_str(row.get("row_count", "")) != str(len(df)):
            errors.append(f"{label}: row_count mismatch")
        if safe_str(row.get("column_count", "")) != str(len(df.columns)):
            errors.append(f"{label}: column_count mismatch")
        if normalize_date(row.get("main_price_date", "")) != row_report_date:
            errors.append(f"{label}: main_price_date mismatch")
        for col in ("report_ready", "daily_pdf_ready"):
            if safe_str(row.get(col, "")) != "True":
                errors.append(f"{label}: {col} must be True")
        if safe_str(row.get("warrant_ready", "")) != "True" and not warrant_grace_allows_publish(row):
            errors.append(
                f"{label}: warrant_ready must be True unless bounded warrant grace hides effects"
            )
        if safe_str(row.get("purpose", "")) != "as_published_daily_model_snapshot":
            errors.append(f"{label}: unexpected purpose")

    for artifact in artifacts:
        artifact_id = artifact.artifact_id
        active = active_rows.get((report_date, artifact_id))
        if active is None:
            continue
        source = latest_dir / artifact.source_name
        if not source.exists():
            errors.append(f"{report_date}/{artifact_id}: source missing: {source.as_posix()}")
            continue
        try:
            validate_artifact_frame(source, artifact, report_date)
        except Exception as exc:
            errors.append(f"{report_date}/{artifact_id}: current source {exc}")
        try:
            active_snapshot = resolve_manifest_snapshot_path(
                active.get("snapshot_path", ""),
                repository_root=repository_root,
                artifact=artifact,
                report_date=report_date,
                snapshot_revision=safe_str(active.get("snapshot_revision", "")),
                snapshot_sha256=safe_str(active.get("snapshot_sha256", "")),
                revision_reason=safe_str(active.get("revision_reason", "")),
            )
        except RuntimeError:
            continue
        if active_snapshot.exists():
            try:
                validate_artifact_frame(active_snapshot, artifact, report_date)
            except Exception as exc:
                errors.append(
                    f"{report_date}/{artifact_id}: current max revision {exc}"
                )
        source_hash = sha256_file(source)
        active_revision = safe_str(active.get("snapshot_revision", ""))
        active_content_hash = (
            sha256_file(active_snapshot) if active_snapshot.exists() else ""
        )
        if source_hash != active_content_hash:
            errors.append(
                f"{report_date}/{artifact_id}/{active_revision}: max revision does not match current source"
            )

    return errors


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Validate immutable daily published model snapshots"
    )
    parser.add_argument(
        "--artifact-id",
        action="append",
        choices=sorted(artifact.artifact_id for artifact in ARTIFACTS),
        help=(
            "Validate only this artifact's full revision/current-source contract; "
            "repeat for multiple artifacts. Omit for the full contract."
        ),
    )
    parser.add_argument(
        "--phase",
        choices=("full", "runtime"),
        default="full",
        help=(
            "Use runtime to validate only the current report-date revision chains; "
            "the default full phase preserves complete manifest/history validation."
        ),
    )
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    errors = validate_current_report_snapshots(
        artifact_ids=args.artifact_id,
        phase=args.phase,
    )
    if errors:
        print("ERROR: daily published model snapshot validation failed")
        for error in errors:
            print(f"ERROR: {error}")
        return 1
    state = freshness_state()
    scope = ",".join(args.artifact_id or []) or "full"
    print(
        "daily published model snapshot validation passed for "
        f"report_date={state['main_price_date']} scope={scope} phase={args.phase}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
