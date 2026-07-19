from __future__ import annotations

import argparse
from io import BytesIO
import os
from pathlib import Path
import subprocess
import sys
import uuid

import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent))

from tracking_utils import normalize_date, safe_str  # noqa: E402
from update_daily_published_model_snapshots import (  # noqa: E402
    ARTIFACTS_BY_ID,
    MANIFEST_COLUMNS,
    MANIFEST_PATH,
    SNAPSHOT_DIR,
    manifest_v1_sha256_candidates,
    normalize_known_manifest_schema,
    read_existing_manifest_strict,
    repository_root_for_snapshot_dir,
    resolve_manifest_snapshot_path,
    sha256_file,
    validate_revision_group,
)


def _git_staged_paths(repository_root: Path) -> set[str]:
    completed = subprocess.run(
        ["git", "diff", "--cached", "--name-only"],
        cwd=repository_root,
        check=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )
    return {
        line.strip().replace("\\", "/")
        for line in completed.stdout.splitlines()
        if line.strip()
    }


def _git_index_snapshot(repository_root: Path) -> tuple[Path, bytes | None]:
    completed = subprocess.run(
        ["git", "rev-parse", "--git-path", "index"],
        cwd=repository_root,
        check=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )
    raw_path = completed.stdout.strip()
    if not raw_path:
        raise RuntimeError("git did not return an index path")
    index_path = Path(raw_path)
    if not index_path.is_absolute():
        index_path = repository_root / index_path
    index_path = index_path.resolve()
    return index_path, index_path.read_bytes() if index_path.is_file() else None


def _restore_git_index(index_path: Path, payload: bytes | None) -> None:
    if payload is None:
        index_path.unlink(missing_ok=True)
        return
    index_path.parent.mkdir(parents=True, exist_ok=True)
    temporary = index_path.with_name(
        f".{index_path.name}.{uuid.uuid4().hex}.restore.tmp"
    )
    try:
        temporary.write_bytes(payload)
        os.replace(temporary, index_path)
    finally:
        temporary.unlink(missing_ok=True)


def _git_head_manifest(
    repository_root: Path,
    manifest_relative: str,
) -> pd.DataFrame:
    head = subprocess.run(
        ["git", "rev-parse", "--verify", "HEAD"],
        cwd=repository_root,
        check=False,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )
    if head.returncode != 0:
        return pd.DataFrame(columns=MANIFEST_COLUMNS)
    completed = subprocess.run(
        ["git", "show", f"HEAD:{manifest_relative}"],
        cwd=repository_root,
        check=False,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    if completed.returncode != 0:
        return pd.DataFrame(columns=MANIFEST_COLUMNS)
    try:
        manifest = pd.read_csv(
            BytesIO(completed.stdout),
            dtype=str,
            keep_default_na=False,
        ).fillna("")
    except Exception as exc:
        raise RuntimeError(
            f"failed to read HEAD daily snapshot manifest: {exc}"
        ) from exc
    if manifest.empty:
        raise RuntimeError("HEAD daily snapshot manifest has no data rows")
    return normalize_known_manifest_schema(
        manifest,
        context=f"HEAD daily snapshot manifest {manifest_relative}",
    )


def _git_index_manifest(
    repository_root: Path,
    manifest_relative: str,
) -> pd.DataFrame:
    completed = subprocess.run(
        ["git", "show", f":{manifest_relative}"],
        cwd=repository_root,
        check=False,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    if completed.returncode != 0:
        raise RuntimeError(
            "staged daily snapshot manifest could not be read from the git index: "
            f"{manifest_relative}"
        )
    try:
        manifest = pd.read_csv(
            BytesIO(completed.stdout),
            dtype=str,
            keep_default_na=False,
        ).fillna("")
    except Exception as exc:
        raise RuntimeError(
            f"failed to read staged daily snapshot manifest: {exc}"
        ) from exc
    if manifest.empty:
        raise RuntimeError("staged daily snapshot manifest has no data rows")
    return normalize_known_manifest_schema(
        manifest,
        context=f"staged daily snapshot manifest {manifest_relative}",
    )


def _git_head_has_path(repository_root: Path, repository_relative: str) -> bool:
    completed = subprocess.run(
        ["git", "cat-file", "-e", f"HEAD:{repository_relative}"],
        cwd=repository_root,
        check=False,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )
    return completed.returncode == 0


def _manifest_row_identity(row: pd.Series) -> tuple[str, ...]:
    return tuple(safe_str(row.get(column)) for column in MANIFEST_COLUMNS)


def _repository_relative(path: Path, repository_root: Path) -> str:
    try:
        relative = path.resolve().relative_to(repository_root.resolve())
    except ValueError as exc:
        raise RuntimeError(
            f"daily snapshot staging path escapes repository: {path.as_posix()}"
        ) from exc
    text = relative.as_posix()
    if not text or any(part in {"", ".", ".."} for part in text.split("/")):
        raise RuntimeError(f"invalid repository-relative staging path: {text!r}")
    return text


def _registered_manifest_snapshot_paths(
    manifest: pd.DataFrame,
    *,
    repository_root: Path,
) -> dict[tuple[str, ...], str]:
    """Resolve every registered manifest row to its exact repository path."""

    registered: dict[tuple[str, ...], str] = {}
    grouped = manifest.groupby(
        ["snapshot_report_date", "artifact_id"],
        sort=True,
        dropna=False,
    )
    for (raw_report_date, raw_artifact_id), group in grouped:
        report_date = normalize_date(raw_report_date)
        artifact_id = safe_str(raw_artifact_id)
        if report_date != safe_str(raw_report_date) or len(report_date) != 8:
            raise RuntimeError(
                "daily snapshot manifest has an invalid report date: "
                f"{raw_report_date!r}"
            )
        artifact = ARTIFACTS_BY_ID.get(artifact_id)
        if artifact is None:
            raise RuntimeError(
                "daily snapshot manifest has an unregistered artifact_id: "
                f"{artifact_id!r}"
            )
        ordered = validate_revision_group(
            group,
            report_date=report_date,
            artifact_id=artifact_id,
        )
        for _, row in ordered.iterrows():
            identity = _manifest_row_identity(row)
            if identity in registered:
                raise RuntimeError(
                    "daily snapshot manifest contains a duplicate normalized row: "
                    f"report_date={report_date} artifact_id={artifact_id}"
                )
            snapshot_path = resolve_manifest_snapshot_path(
                row.get("snapshot_path", ""),
                repository_root=repository_root,
                artifact=artifact,
                report_date=report_date,
                snapshot_revision=safe_str(row.get("snapshot_revision")),
                snapshot_sha256=safe_str(row.get("snapshot_sha256")),
                revision_reason=safe_str(row.get("revision_reason")),
            )
            registered[identity] = _repository_relative(
                snapshot_path,
                repository_root,
            )
    return registered


def stage_registered_snapshot_revisions(
    *,
    report_date: str,
    artifact_ids: set[str],
    manifest_path: Path = MANIFEST_PATH,
    snapshot_dir: Path = SNAPSHOT_DIR,
    repository_root: Path | None = None,
) -> list[str]:
    normalized_date = normalize_date(report_date)
    if normalized_date != safe_str(report_date) or len(normalized_date) != 8:
        raise RuntimeError(f"invalid snapshot report date: {report_date!r}")
    if not artifact_ids:
        raise RuntimeError("at least one artifact_id is required for snapshot staging")
    unknown = sorted(set(artifact_ids) - set(ARTIFACTS_BY_ID))
    if unknown:
        raise RuntimeError(f"unknown daily snapshot artifact_ids: {unknown}")

    manifest_path = Path(manifest_path)
    snapshot_dir = Path(snapshot_dir)
    repository_root = (
        Path(repository_root).resolve()
        if repository_root is not None
        else repository_root_for_snapshot_dir(snapshot_dir)
    )
    index_path, index_payload = _git_index_snapshot(repository_root)
    try:
        manifest, _ = read_existing_manifest_strict(manifest_path)
        manifest = normalize_known_manifest_schema(
            manifest,
            context=f"snapshot staging manifest {manifest_path.as_posix()}",
        )
        manifest_relative = _repository_relative(manifest_path, repository_root)
        snapshot_prefix = (
            _repository_relative(snapshot_dir, repository_root).rstrip("/") + "/"
        )
        registered_by_identity = _registered_manifest_snapshot_paths(
            manifest,
            repository_root=repository_root,
        )
        registered_paths = set(registered_by_identity.values())
        allowed_prefix_paths = {manifest_relative, *registered_paths}

        before = _git_staged_paths(repository_root)
        pre_staged_unregistered = sorted(
            path
            for path in before
            if path.startswith(snapshot_prefix) and path not in allowed_prefix_paths
        )
        if pre_staged_unregistered:
            raise RuntimeError(
                "unregistered daily snapshot paths are already staged: "
                f"{pre_staged_unregistered}"
            )

        selected = manifest[
            manifest["snapshot_report_date"].map(normalize_date).eq(normalized_date)
            & manifest["artifact_id"].astype(str).isin(artifact_ids)
        ].copy()
        paths: list[str] = []
        for artifact_id in sorted(artifact_ids):
            group = selected[selected["artifact_id"].astype(str).eq(artifact_id)]
            if group.empty:
                raise RuntimeError(
                    "snapshot staging manifest is missing a registered artifact: "
                    f"report_date={normalized_date} artifact_id={artifact_id}"
                )
            ordered = validate_revision_group(
                group,
                report_date=normalized_date,
                artifact_id=artifact_id,
            )
            artifact = ARTIFACTS_BY_ID[artifact_id]
            for _, row in ordered.iterrows():
                revision = safe_str(row.get("snapshot_revision"))
                expected_sha = safe_str(row.get("snapshot_sha256"))
                snapshot_path = resolve_manifest_snapshot_path(
                    row.get("snapshot_path", ""),
                    repository_root=repository_root,
                    artifact=artifact,
                    report_date=normalized_date,
                    snapshot_revision=revision,
                    snapshot_sha256=expected_sha,
                    revision_reason=safe_str(row.get("revision_reason")),
                )
                if not snapshot_path.is_file():
                    raise RuntimeError(
                        "registered daily snapshot is missing: "
                        f"{snapshot_path.as_posix()}"
                    )
                accepted_hashes = (
                    manifest_v1_sha256_candidates(snapshot_path)
                    if revision == "r1"
                    else {sha256_file(snapshot_path)}
                )
                if expected_sha not in accepted_hashes:
                    raise RuntimeError(
                        "registered daily snapshot hash mismatch before staging: "
                        f"report_date={normalized_date} artifact_id={artifact_id} "
                        f"revision={revision}"
                    )
                paths.append(_repository_relative(snapshot_path, repository_root))

        exact_paths = sorted(set([manifest_relative, *paths]))
        subprocess.run(
            ["git", "add", "--", *exact_paths],
            cwd=repository_root,
            check=True,
        )
        after = _git_staged_paths(repository_root)
        staged_unregistered = sorted(
            path
            for path in after
            if path.startswith(snapshot_prefix) and path not in allowed_prefix_paths
        )
        if staged_unregistered:
            raise RuntimeError(
                f"unregistered daily snapshot paths were staged: {staged_unregistered}"
            )

        head_manifest = _git_head_manifest(repository_root, manifest_relative)
        staged_manifest = _git_index_manifest(repository_root, manifest_relative)
        staged_by_identity = _registered_manifest_snapshot_paths(
            staged_manifest,
            repository_root=repository_root,
        )
        head_identities = {
            _manifest_row_identity(row)
            for _, row in head_manifest.iterrows()
        }
        staged_rows_by_identity = {
            _manifest_row_identity(row): row
            for _, row in staged_manifest.iterrows()
        }
        staged_identities = set(staged_by_identity)
        removed_or_modified = head_identities - staged_identities
        if removed_or_modified:
            raise RuntimeError(
                "daily snapshot manifest is not append-only from HEAD to index; "
                f"removed_or_modified_rows={len(removed_or_modified)}"
            )

        unselected_new_rows: list[str] = []
        missing_new_paths: list[str] = []
        for identity in sorted(staged_identities - head_identities):
            row = staged_rows_by_identity[identity]
            row_report_date = normalize_date(row.get("snapshot_report_date"))
            row_artifact_id = safe_str(row.get("artifact_id"))
            snapshot_relative = staged_by_identity[identity]
            if (
                row_report_date != normalized_date
                or row_artifact_id not in artifact_ids
            ):
                unselected_new_rows.append(
                    f"{row_report_date}/{row_artifact_id}/"
                    f"{safe_str(row.get('snapshot_revision'))}"
                )
                continue
            if (
                snapshot_relative not in after
                and not _git_head_has_path(repository_root, snapshot_relative)
            ):
                missing_new_paths.append(snapshot_relative)
        if unselected_new_rows:
            raise RuntimeError(
                "daily snapshot manifest contains unselected new snapshot rows: "
                f"{sorted(unselected_new_rows)}"
            )
        if missing_new_paths:
            raise RuntimeError(
                "new daily snapshot manifest rows are not closed over staged or "
                f"HEAD payloads: {sorted(missing_new_paths)}"
            )
        return exact_paths
    except BaseException as exc:
        try:
            _restore_git_index(index_path, index_payload)
        except Exception as restore_exc:
            raise RuntimeError(
                "daily snapshot exact staging failed and the prior git index "
                f"could not be restored: {restore_exc}"
            ) from exc
        raise


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Stage only exact daily snapshot paths registered by the manifest."
    )
    parser.add_argument("--report-date", required=True)
    parser.add_argument("--artifact-id", action="append", dest="artifact_ids", required=True)
    parser.add_argument("--manifest-path", type=Path, default=MANIFEST_PATH)
    parser.add_argument("--snapshot-dir", type=Path, default=SNAPSHOT_DIR)
    parser.add_argument("--repo-root", type=Path)
    args = parser.parse_args()
    staged = stage_registered_snapshot_revisions(
        report_date=args.report_date,
        artifact_ids=set(args.artifact_ids),
        manifest_path=args.manifest_path,
        snapshot_dir=args.snapshot_dir,
        repository_root=args.repo_root,
    )
    print(
        "daily snapshot exact staging passed: "
        f"report_date={args.report_date} paths={len(staged)}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
