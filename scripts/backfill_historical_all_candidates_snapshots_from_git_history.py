from __future__ import annotations

import argparse
import hashlib
import re
import subprocess
import sys
import tempfile
from io import BytesIO
from pathlib import Path

import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent))

from tracking_utils import normalize_date, now_text, safe_str  # noqa: E402
from update_daily_published_model_snapshots import (  # noqa: E402
    ARTIFACTS,
    MANIFEST_COLUMNS,
    MANIFEST_PATH,
    SNAPSHOT_DIR,
    SnapshotArtifact,
    approved_snapshot_repository_path,
    csv_shape,
    manifest_v1_sha256_candidates,
    manifest_publication_lock,
    normalize_known_manifest_schema,
    parse_snapshot_revision,
    publish_snapshot_transaction,
    read_existing_manifest_strict,
    repository_root_for_snapshot_dir,
    resolve_manifest_snapshot_path,
    sha256_file,
    snapshot_name,
    validate_artifact_frame,
    validate_revision_group,
)


ROOT = Path(__file__).resolve().parents[1]
ALL_CANDIDATES_SOURCE = "output/latest/all_candidates_latest.csv"
FORMAL_SIGNAL_ARTIFACT_ID = "model_signals_for_report"
PUBLISHED_MODEL_SIGNALS_RE = re.compile(
    r"daily_candidate_model_signals_for_report_(\d{8})(?:_r[1-9][0-9]*_[0-9a-f]{12})?\.csv$"
)


def all_candidates_artifact() -> SnapshotArtifact:
    for artifact in ARTIFACTS:
        if artifact.artifact_id == "all_candidates_source_rows":
            return artifact
    raise RuntimeError("all_candidates_source_rows artifact is not registered")


def formal_signal_artifact() -> SnapshotArtifact:
    for artifact in ARTIFACTS:
        if artifact.artifact_id == FORMAL_SIGNAL_ARTIFACT_ID:
            return artifact
    raise RuntimeError(f"{FORMAL_SIGNAL_ARTIFACT_ID} artifact is not registered")


def git_output(repo_root: Path, *args: str) -> bytes:
    return subprocess.check_output(["git", *args], cwd=repo_root, stderr=subprocess.DEVNULL)


def canonical_lf_payload(payload: bytes) -> bytes:
    return payload.replace(b"\r\n", b"\n").replace(b"\r", b"\n")


def git_tree_path(path: Path | str, repo_root: Path) -> str:
    candidate = Path(path)
    if not candidate.is_absolute():
        return candidate.as_posix()
    try:
        return candidate.resolve().relative_to(repo_root.resolve()).as_posix()
    except ValueError as exc:
        raise RuntimeError(
            f"path is outside the git repository: {candidate.as_posix()}"
        ) from exc


def git_show_path(repo_root: Path, commit_sha: str, path: str) -> bytes:
    try:
        return git_output(repo_root, "show", f"{commit_sha}:{path}")
    except subprocess.CalledProcessError as exc:
        raise RuntimeError(
            f"git commit {commit_sha} is missing required paired path: {path}"
        ) from exc


def git_manifest_commits(repo_root: Path, manifest_path: Path) -> list[str]:
    manifest_tree_path = git_tree_path(manifest_path, repo_root)
    output = git_output(
        repo_root,
        "log",
        "--first-parent",
        "--reverse",
        "--format=%H",
        "--",
        manifest_tree_path,
    )
    return output.decode("ascii").splitlines()


def git_changed_paths(repo_root: Path, commit_sha: str) -> set[str]:
    ancestry = git_output(
        repo_root,
        "rev-list",
        "--parents",
        "-n",
        "1",
        commit_sha,
    ).decode("ascii").split()
    if not ancestry or ancestry[0] != commit_sha:
        raise RuntimeError(f"failed to resolve git commit ancestry: {commit_sha}")
    if len(ancestry) == 1:
        output = git_output(
            repo_root,
            "diff-tree",
            "--root",
            "--no-commit-id",
            "--name-only",
            "-r",
            commit_sha,
        )
    else:
        output = git_output(
            repo_root,
            "diff",
            "--name-only",
            ancestry[1],
            commit_sha,
            "--",
        )
    return {line for line in output.decode("utf-8").splitlines() if line}


def published_model_signal_dates(snapshot_dir: Path = SNAPSHOT_DIR) -> list[str]:
    dates: set[str] = set()
    for path in snapshot_dir.glob("daily_candidate_model_signals_for_report_*.csv"):
        match = PUBLISHED_MODEL_SIGNALS_RE.match(path.name)
        if match:
            dates.add(match.group(1))
    return sorted(dates)


def candidate_blob_report_dates(blob: bytes, artifact: SnapshotArtifact) -> set[str]:
    df = pd.read_csv(BytesIO(blob), dtype=str, keep_default_na=False).fillna("")
    missing = [col for col in artifact.required_columns if col not in df.columns]
    if missing:
        raise RuntimeError(f"{ALL_CANDIDATES_SOURCE} missing required columns: {missing}")

    values: set[str] = set()
    for col in artifact.date_columns:
        if col not in df.columns:
            raise RuntimeError(f"{ALL_CANDIDATES_SOURCE} missing required date column: {col}")
        col_values = {normalize_date(value) for value in df[col].tolist()}
        col_values.discard("")
        if col_values:
            values.update(col_values)
    return values


def normalized_manifest(blob: bytes) -> pd.DataFrame:
    try:
        manifest = pd.read_csv(BytesIO(blob), dtype=str, keep_default_na=False).fillna("")
    except Exception as exc:
        raise RuntimeError("paired publication manifest is not a readable CSV") from exc
    return normalize_known_manifest_schema(
        manifest,
        context="paired publication manifest from Git history",
    )


def manifest_row_identity(row: pd.Series) -> tuple[str, ...]:
    return tuple(safe_str(row.get(column, "")) for column in MANIFEST_COLUMNS)


def exact_formal_signal_rows(
    manifest: pd.DataFrame,
    report_date: str,
) -> pd.DataFrame:
    rows = manifest[
        manifest["snapshot_report_date"].map(normalize_date).eq(report_date)
        & manifest["artifact_id"].astype(str).eq(FORMAL_SIGNAL_ARTIFACT_ID)
    ].copy()
    if rows.empty:
        raise RuntimeError(
            "manifest has no model_signals_for_report revision rows for "
            f"report_date={report_date}"
        )
    return validate_revision_group(
        rows,
        report_date=report_date,
        artifact_id=FORMAL_SIGNAL_ARTIFACT_ID,
    )


def verify_formal_snapshot_blob(
    blob: bytes,
    *,
    report_date: str,
    target_row: pd.Series,
) -> None:
    revision = safe_str(target_row.get("snapshot_revision", ""))
    revision_number = parse_snapshot_revision(revision)
    expected_sha = safe_str(target_row.get("snapshot_sha256", ""))
    canonical_blob = canonical_lf_payload(blob)
    canonical_sha = hashlib.sha256(canonical_blob).hexdigest()
    payload_sha_candidates = (
        {
            hashlib.sha256(candidate).hexdigest()
            for candidate in (
                blob,
                canonical_blob,
                canonical_blob.replace(b"\n", b"\r\n"),
            )
        }
        if revision_number == 1
        else {canonical_sha}
    )
    if expected_sha not in payload_sha_candidates:
        raise RuntimeError(
            "paired formal snapshot SHA does not match its exact manifest row: "
            f"report_date={report_date} revision={revision}"
        )
    try:
        frame = pd.read_csv(BytesIO(blob), dtype=str, keep_default_na=False).fillna("")
    except Exception as exc:
        raise RuntimeError(
            "paired formal snapshot is not a readable CSV: "
            f"report_date={report_date} revision={revision}"
        ) from exc
    expected_rows = safe_str(target_row.get("row_count", ""))
    expected_columns = safe_str(target_row.get("column_count", ""))
    if expected_rows != str(len(frame)) or expected_columns != str(len(frame.columns)):
        raise RuntimeError(
            "paired formal snapshot shape does not match its exact manifest row: "
            f"report_date={report_date} revision={revision} "
            f"observed={len(frame)}x{len(frame.columns)} "
            f"expected={expected_rows}x{expected_columns}"
        )
    if "signal_date" not in frame.columns:
        raise RuntimeError(
            "paired formal snapshot is missing signal_date: "
            f"report_date={report_date} revision={revision}"
        )
    signal_dates = {normalize_date(value) for value in frame["signal_date"].tolist()}
    signal_dates.discard("")
    if signal_dates != {report_date}:
        raise RuntimeError(
            "paired formal snapshot signal_date does not match its manifest row: "
            f"report_date={report_date} revision={revision} "
            f"observed={sorted(signal_dates)}"
        )


def find_exact_paired_all_candidates_blob(
    target_row: pd.Series,
    *,
    repo_root: Path,
    manifest_path: Path,
    manifest_commits: list[str],
    artifact: SnapshotArtifact,
) -> tuple[str, bytes]:
    report_date = normalize_date(target_row.get("snapshot_report_date", ""))
    revision = safe_str(target_row.get("snapshot_revision", ""))
    target_identity = manifest_row_identity(target_row)
    manifest_tree_path = git_tree_path(manifest_path, repo_root)

    publication_commit = ""
    publication_manifest_row: pd.Series | None = None
    for commit_sha in manifest_commits:
        try:
            commit_manifest_blob = git_show_path(
                repo_root,
                commit_sha,
                manifest_tree_path,
            )
        except RuntimeError:
            continue
        commit_manifest = normalized_manifest(commit_manifest_blob)
        matching_key = commit_manifest[
            commit_manifest["snapshot_report_date"].map(normalize_date).eq(report_date)
            & commit_manifest["artifact_id"].astype(str).eq(FORMAL_SIGNAL_ARTIFACT_ID)
            & commit_manifest["snapshot_revision"].astype(str).eq(revision)
        ]
        exact = matching_key[
            matching_key.apply(manifest_row_identity, axis=1).map(
                lambda identity: identity == target_identity
            )
        ]
        if len(exact) > 1:
            raise RuntimeError(
                "paired publication manifest contains duplicate exact formal rows: "
                f"report_date={report_date} revision={revision} commit={commit_sha}"
            )
        if len(exact) == 1:
            publication_commit = commit_sha
            publication_manifest_row = exact.iloc[0]
            break

    if not publication_commit or publication_manifest_row is None:
        raise RuntimeError(
            "no exact formal publication commit found for model_signals_for_report: "
            f"report_date={report_date} revision={revision}"
        )

    resolved_formal_snapshot = resolve_manifest_snapshot_path(
        publication_manifest_row.get("snapshot_path", ""),
        repository_root=repo_root,
        artifact=formal_signal_artifact(),
        report_date=report_date,
        snapshot_revision=revision,
        snapshot_sha256=safe_str(
            publication_manifest_row.get("snapshot_sha256", "")
        ),
        revision_reason=safe_str(
            publication_manifest_row.get("revision_reason", "")
        ),
    )
    formal_snapshot_path = git_tree_path(resolved_formal_snapshot, repo_root)
    changed_paths = git_changed_paths(repo_root, publication_commit)
    if manifest_tree_path not in changed_paths or formal_snapshot_path not in changed_paths:
        raise RuntimeError(
            "exact formal row was not introduced by a manifest plus snapshot publication commit: "
            f"report_date={report_date} revision={revision} commit={publication_commit}"
        )

    formal_blob = git_show_path(repo_root, publication_commit, formal_snapshot_path)
    verify_formal_snapshot_blob(
        formal_blob,
        report_date=report_date,
        target_row=publication_manifest_row,
    )
    candidate_blob = git_show_path(repo_root, publication_commit, ALL_CANDIDATES_SOURCE)
    if candidate_blob_report_dates(candidate_blob, artifact) != {report_date}:
        raise RuntimeError(
            "paired all_candidates payload does not match the exact formal publication date: "
            f"report_date={report_date} revision={revision} commit={publication_commit}"
        )
    return publication_commit, candidate_blob


def _backfill_historical_all_candidates_snapshots_under_lock(
    *,
    repo_root: Path = ROOT,
    snapshot_dir: Path = SNAPSHOT_DIR,
    manifest_path: Path = MANIFEST_PATH,
    dates: list[str] | None = None,
    overwrite: bool = False,
    dry_run: bool = False,
    generated_at: str | None = None,
) -> pd.DataFrame:
    repo_root = Path(repo_root).resolve()
    snapshot_dir = Path(snapshot_dir)
    manifest_path = Path(manifest_path)
    inferred_repository_root = repository_root_for_snapshot_dir(snapshot_dir)
    if inferred_repository_root != repo_root:
        raise RuntimeError(
            "backfill snapshot_dir and repo_root must identify the same repository: "
            f"snapshot_root={inferred_repository_root.as_posix()} "
            f"repo_root={repo_root.as_posix()}"
        )
    artifact = all_candidates_artifact()
    dates = dates if dates is not None else published_model_signal_dates(snapshot_dir)
    dates = sorted({normalize_date(date) for date in dates if normalize_date(date)})
    if not dates:
        raise RuntimeError("no report dates were selected for all_candidates backfill")

    manifest, planning_manifest_bytes = read_existing_manifest_strict(manifest_path)
    manifest = normalize_known_manifest_schema(
        manifest,
        context=f"existing backfill manifest {manifest_path.as_posix()}",
    )

    generated_at = generated_at or now_text()
    manifest_commits = git_manifest_commits(repo_root, manifest_path)
    if not manifest_commits:
        raise RuntimeError(
            "git history has no publication commits for "
            f"{git_tree_path(manifest_path, repo_root)}"
        )
    rows: list[dict[str, str]] = []
    copy_plans: list[tuple[Path, Path, str]] = []
    staging = tempfile.TemporaryDirectory(prefix="daily-all-candidates-backfill-")
    try:
        staging_dir = Path(staging.name)
        for report_date in dates:
            formal_rows = exact_formal_signal_rows(manifest, report_date)
            existing_rows = manifest[
                manifest["snapshot_report_date"].map(normalize_date).eq(report_date)
                & manifest["artifact_id"].astype(str).eq(artifact.artifact_id)
            ].copy()
            if not existing_rows.empty and not overwrite:
                continue
            if not existing_rows.empty:
                existing_rows = validate_revision_group(
                    existing_rows,
                    report_date=report_date,
                    artifact_id=artifact.artifact_id,
                )
            formal_revision_numbers = {
                parse_snapshot_revision(value)
                for value in formal_rows["snapshot_revision"].tolist()
            }
            existing_revision_numbers = {
                parse_snapshot_revision(value)
                for value in existing_rows["snapshot_revision"].tolist()
            }
            unexpected_revisions = existing_revision_numbers - formal_revision_numbers
            if unexpected_revisions:
                raise RuntimeError(
                    "all_candidates revisions have no same-date same-revision formal source: "
                    f"report_date={report_date} revisions={sorted(unexpected_revisions)}"
                )

            existing_by_revision = {
                safe_str(row.get("snapshot_revision", "")): row
                for _, row in existing_rows.iterrows()
            }
            previous_sha = (
                safe_str(existing_rows.iloc[-1].get("snapshot_sha256", ""))
                if not existing_rows.empty
                else ""
            )
            previous_payload: bytes | None = None
            expected_next_revision = len(existing_rows) + 1

            for _, formal_row in formal_rows.iterrows():
                snapshot_revision = safe_str(formal_row.get("snapshot_revision", ""))
                revision_number = parse_snapshot_revision(snapshot_revision)
                commit_sha, blob = find_exact_paired_all_candidates_blob(
                    formal_row,
                    repo_root=repo_root,
                    manifest_path=manifest_path,
                    manifest_commits=manifest_commits,
                    artifact=artifact,
                )
                canonical_blob = canonical_lf_payload(blob)
                digest = hashlib.sha256(canonical_blob).hexdigest()

                existing_row = existing_by_revision.get(snapshot_revision)
                if existing_row is not None:
                    existing_path = resolve_manifest_snapshot_path(
                        existing_row.get("snapshot_path", ""),
                        repository_root=repo_root,
                        artifact=artifact,
                        report_date=report_date,
                        snapshot_revision=snapshot_revision,
                        snapshot_sha256=safe_str(
                            existing_row.get("snapshot_sha256", "")
                        ),
                        revision_reason=safe_str(
                            existing_row.get("revision_reason", "")
                        ),
                    )
                    if not existing_path.exists():
                        raise RuntimeError(
                            "existing all_candidates revision snapshot is missing: "
                            f"report_date={report_date} revision={snapshot_revision} "
                            f"path={existing_path.as_posix()}"
                        )
                    existing_sha = safe_str(existing_row.get("snapshot_sha256", ""))
                    accepted_existing_hashes = (
                        manifest_v1_sha256_candidates(existing_path)
                        if revision_number == 1
                        else {sha256_file(existing_path)}
                    )
                    if existing_sha not in accepted_existing_hashes:
                        raise RuntimeError(
                            "existing all_candidates revision snapshot SHA does not match manifest: "
                            f"report_date={report_date} revision={snapshot_revision}"
                        )
                    if canonical_lf_payload(existing_path.read_bytes()) == canonical_blob:
                        previous_payload = canonical_blob
                        continue
                    raise RuntimeError(
                        "existing all_candidates revision conflicts with its exact paired "
                        "formal publication payload: "
                        f"report_date={report_date} revision={snapshot_revision}"
                    )

                if revision_number != expected_next_revision:
                    raise RuntimeError(
                        "cannot backfill an all_candidates revision gap: "
                        f"report_date={report_date} revision={snapshot_revision} "
                        f"expected=r{expected_next_revision}"
                    )
                if previous_payload is not None and previous_payload == canonical_blob:
                    raise RuntimeError(
                        "same-revision formal publication did not produce a distinct "
                        "all_candidates payload: "
                        f"report_date={report_date} revision={snapshot_revision}"
                    )

                target = snapshot_dir / snapshot_name(
                    artifact,
                    report_date,
                    snapshot_revision,
                    digest,
                )
                if target.exists():
                    raise RuntimeError(
                        "unreferenced immutable all_candidates target already exists: "
                        f"{target.as_posix()}"
                    )
                if not dry_run:
                    staged = staging_dir / f"{len(rows):04d}_{target.name}"
                    staged.write_bytes(canonical_blob)
                    validate_artifact_frame(staged, artifact, report_date)
                    row_count, column_count = csv_shape(staged)
                    if sha256_file(staged) != digest:
                        raise RuntimeError(
                            f"backfilled snapshot hash mismatch: {target.as_posix()}"
                        )
                    copy_plans.append((staged, target, digest))
                else:
                    df = pd.read_csv(
                        BytesIO(canonical_blob),
                        dtype=str,
                        keep_default_na=False,
                    )
                    row_count, column_count = len(df), len(df.columns)

                template = {
                    column: safe_str(formal_row.get(column, ""))
                    for column in MANIFEST_COLUMNS
                }
                row = {
                    **template,
                    "snapshot_report_date": report_date,
                    "generated_at": generated_at,
                    "pipeline_commit_sha": commit_sha,
                    "main_price_date": report_date,
                    "artifact_id": artifact.artifact_id,
                    "snapshot_revision": snapshot_revision,
                    "supersedes_snapshot_sha256": previous_sha,
                    "revision_reason": (
                        "git_history_backfill"
                        if revision_number == 1
                        else "git_history_backfill_correction"
                    ),
                    "source_path": ALL_CANDIDATES_SOURCE,
                    "snapshot_path": approved_snapshot_repository_path(
                        artifact,
                        report_date,
                        snapshot_revision,
                        digest,
                    ).as_posix(),
                    "source_sha256": digest,
                    "snapshot_sha256": digest,
                    "row_count": str(row_count),
                    "column_count": str(column_count),
                    "purpose": "as_published_daily_model_snapshot",
                }
                rows.append(row)
                existing_by_revision[snapshot_revision] = pd.Series(row)
                previous_sha = digest
                previous_payload = canonical_blob
                expected_next_revision += 1

        new_rows = pd.DataFrame(rows, columns=MANIFEST_COLUMNS)
        if not dry_run and not new_rows.empty:
            combined = pd.concat([manifest, new_rows], ignore_index=True)
            combined = combined[MANIFEST_COLUMNS]
            combined["_revision"] = (
                combined["snapshot_revision"]
                .astype(str)
                .str.lstrip("r")
                .astype(int)
            )
            combined = (
                combined.sort_values(
                    ["snapshot_report_date", "artifact_id", "_revision"]
                )
                .drop(columns=["_revision"])
                .reset_index(drop=True)
            )
            publish_snapshot_transaction(
                copy_plans,
                combined,
                manifest_path,
                expected_manifest_bytes=planning_manifest_bytes,
            )

        return new_rows
    finally:
        staging.cleanup()


def backfill_historical_all_candidates_snapshots(
    *,
    repo_root: Path = ROOT,
    snapshot_dir: Path = SNAPSHOT_DIR,
    manifest_path: Path = MANIFEST_PATH,
    dates: list[str] | None = None,
    overwrite: bool = False,
    dry_run: bool = False,
    generated_at: str | None = None,
) -> pd.DataFrame:
    """Backfill under the same manifest lock used by the live publisher."""

    manifest_path = Path(manifest_path)
    with manifest_publication_lock(manifest_path):
        return _backfill_historical_all_candidates_snapshots_under_lock(
            repo_root=repo_root,
            snapshot_dir=snapshot_dir,
            manifest_path=manifest_path,
            dates=dates,
            overwrite=overwrite,
            dry_run=dry_run,
            generated_at=generated_at,
        )


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Backfill historical all_candidates source-row snapshots from git history."
    )
    parser.add_argument(
        "--dates",
        help="Comma-separated YYYYMMDD report dates. Defaults to all published model signal snapshot dates.",
    )
    parser.add_argument(
        "--overwrite",
        action="store_true",
        help=(
            "Append an immutable correction revision when a same-date all_candidates "
            "snapshot already exists; prior revisions are never overwritten."
        ),
    )
    parser.add_argument("--dry-run", action="store_true", help="Print planned rows without writing files.")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    selected_dates = None
    if args.dates:
        selected_dates = [part.strip() for part in args.dates.split(",") if part.strip()]

    try:
        rows = backfill_historical_all_candidates_snapshots(
            dates=selected_dates,
            overwrite=args.overwrite,
            dry_run=args.dry_run,
        )
    except Exception as exc:
        print(f"ERROR: {exc}")
        return 1

    action = "planned" if args.dry_run else "backfilled"
    print(f"{action} historical all_candidates snapshots: {len(rows)}")
    for _, row in rows.iterrows():
        print(
            f"{row['snapshot_report_date']} {row['snapshot_path']} "
            f"rows={row['row_count']} commit={str(row['pipeline_commit_sha'])[:10]}"
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
