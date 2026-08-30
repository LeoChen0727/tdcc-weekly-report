from __future__ import annotations

import hashlib
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Callable

import pandas as pd


MANIFEST_NAME = "daily_published_model_snapshot_manifest.csv"
SNAPSHOT_REPOSITORY_PATH = Path("output/history/daily_model_snapshots")
REVISION_RE = re.compile(r"r([1-9][0-9]*)")
SHA256_RE = re.compile(r"[0-9a-f]{64}")
ARTIFACT_SNAPSHOT_STEMS = {
    "data_freshness": "data_freshness",
    "model_signals_for_report": "daily_candidate_model_signals_for_report",
    "all_candidates_source_rows": "all_candidates",
    "model_summary_for_report": "daily_candidate_model_summary_for_report",
    "model_registry": "daily_report_model_registry",
    "model_parameters": "daily_candidate_model_parameters",
    "volume_breakout_operation_section": "daily_volume_breakout_operation_section",
    "volume_breakout_operation_evidence_audit": (
        "daily_volume_breakout_operation_evidence_audit"
    ),
    "w_bottom_right_side_operation_section": (
        "daily_w_bottom_right_side_operation_section"
    ),
    "neckline_volume_breakout_confirmation_operation_section": (
        "daily_neckline_volume_breakout_confirmation_operation_section"
    ),
    "revenue_unreacted_range_operation_section": (
        "daily_revenue_unreacted_range_operation_section"
    ),
}
REQUIRED_MANIFEST_COLUMNS = {
    "snapshot_report_date",
    "artifact_id",
    "snapshot_path",
    "snapshot_sha256",
}
REVISION_MANIFEST_COLUMNS = (
    "snapshot_revision",
    "supersedes_snapshot_sha256",
    "revision_reason",
)


@dataclass(frozen=True)
class SnapshotRevision:
    """One exact immutable snapshot selected from the publisher manifest."""

    report_date: str
    artifact_id: str
    revision: str
    revision_number: int
    path: Path
    path_text: str
    snapshot_sha256: str
    supersedes_snapshot_sha256: str
    revision_reason: str


def _text(value: Any) -> str:
    if value is None:
        return ""
    try:
        if pd.isna(value):
            return ""
    except (TypeError, ValueError):
        pass
    text = str(value).replace("\ufeff", "").strip()
    return "" if text.lower() in {"nan", "none", "nat", "<na>"} else text


def normalize_revision_manifest_schema(
    manifest: pd.DataFrame,
    *,
    source: str,
) -> pd.DataFrame:
    """Normalize the all-absent legacy schema and reject every partial schema.

    These three columns form one atomic revision contract.  A pre-revision
    manifest may omit all three and is interpreted as legacy r1.  Once any one
    is present, all three must be present so a malformed modern manifest cannot
    silently acquire legacy defaults.
    """

    present = set(REVISION_MANIFEST_COLUMNS) & set(manifest.columns)
    if present and len(present) != len(REVISION_MANIFEST_COLUMNS):
        missing = sorted(set(REVISION_MANIFEST_COLUMNS) - present)
        raise RuntimeError(
            "daily snapshot manifest has a partial revision schema; "
            "snapshot_revision, supersedes_snapshot_sha256, and revision_reason "
            "must be all present or all absent for legacy r1: "
            f"source={source} present={sorted(present)} missing={missing}"
        )

    normalized = manifest.copy()
    if not present:
        normalized["snapshot_revision"] = "r1"
        normalized["supersedes_snapshot_sha256"] = ""
        normalized["revision_reason"] = "legacy_v1_manifest"
    elif normalized["snapshot_revision"].map(_text).eq("").any():
        blank_rows = normalized.index[
            normalized["snapshot_revision"].map(_text).eq("")
        ].tolist()
        raise RuntimeError(
            "daily snapshot manifest snapshot_revision must not be blank when the "
            f"revision schema is present: source={source} rows={blank_rows}"
        )
    return normalized


def normalize_report_date(value: Any) -> str:
    digits = re.sub(r"[^0-9]", "", _text(value))
    return digits if len(digits) == 8 else ""


def normalize_snapshot_revision(value: Any) -> str:
    revision = _text(value)
    match = REVISION_RE.fullmatch(revision)
    if match is None:
        raise RuntimeError(f"invalid snapshot_revision: {revision!r}")
    return f"r{int(match.group(1))}"


def snapshot_revision_number(value: Any) -> int:
    return int(normalize_snapshot_revision(value)[1:])


def snapshot_payload_sha256(payload: bytes) -> str:
    """Match the publisher's immutable text hash across LF/CRLF checkouts."""

    payload = payload.replace(b"\r\n", b"\n").replace(b"\r", b"\n")
    return hashlib.sha256(payload).hexdigest()


def snapshot_payload_sha256_candidates(payload: bytes) -> set[str]:
    """Return legacy manifest-v1 raw/LF/CRLF identity candidates."""

    lf = payload.replace(b"\r\n", b"\n").replace(b"\r", b"\n")
    crlf = lf.replace(b"\n", b"\r\n")
    return {
        hashlib.sha256(candidate).hexdigest()
        for candidate in (payload, lf, crlf)
    }


def snapshot_file_sha256(path: Path) -> str:
    return snapshot_payload_sha256(path.read_bytes())


def snapshot_file_sha256_candidates(path: Path) -> set[str]:
    return snapshot_payload_sha256_candidates(path.read_bytes())


def _resolve_snapshot_path(
    path_text: str,
    *,
    repository_root: Path,
    approved_relative_path: Path,
    snapshot_dir: Path,
) -> Path:
    if not path_text:
        raise RuntimeError("daily snapshot manifest row has an empty snapshot_path")
    if "\x00" in path_text:
        raise RuntimeError("daily snapshot manifest snapshot_path contains NUL")
    normalized = path_text.replace("\\", "/")
    parts = tuple(part for part in normalized.split("/") if part)
    if not parts or any(part in {".", ".."} for part in parts):
        raise RuntimeError(
            "daily snapshot manifest snapshot_path contains a path escape: "
            f"{path_text}"
        )
    approved_text = approved_relative_path.as_posix()
    approved_parts = tuple(approved_relative_path.parts)
    is_absolute = bool(
        normalized.startswith("/")
        or normalized.startswith("//")
        or re.match(r"^[A-Za-z]:/", normalized)
    )
    if is_absolute:
        observed_tail = tuple(part.casefold() for part in parts[-len(approved_parts) :])
        expected_tail = tuple(part.casefold() for part in approved_parts)
        if observed_tail != expected_tail:
            raise RuntimeError(
                "legacy absolute snapshot_path does not end in the approved path "
                f"{approved_text}: observed={path_text}"
            )
    elif path_text != approved_text:
        raise RuntimeError(
            "daily snapshot manifest snapshot_path must be repository-relative POSIX "
            f"{approved_text}: observed={path_text}"
        )
    return (repository_root / approved_relative_path).resolve()


def _require_path_under_snapshot_dir(path: Path, snapshot_dir: Path) -> None:
    try:
        path.relative_to(snapshot_dir.resolve())
    except ValueError as exc:
        raise RuntimeError(
            "daily snapshot manifest path escapes snapshot_dir: "
            f"path={path.as_posix()} snapshot_dir={snapshot_dir.resolve().as_posix()}"
        ) from exc


def _validate_snapshot_path_identity(
    path_text: str,
    *,
    report_date: str,
    revision: str,
    revision_number: int,
    snapshot_sha256: str,
    artifact_id: str,
    revision_reason: str,
) -> Path:
    """Bind immutable paths to the manifest identity they claim to represent."""

    stem = ARTIFACT_SNAPSHOT_STEMS.get(artifact_id)
    if stem is None:
        raise RuntimeError(f"unknown daily snapshot artifact_id: {artifact_id}")
    name = Path(path_text.replace("\\", "/")).name
    versioned_name = f"{stem}_{report_date}_{revision}_{snapshot_sha256[:12]}.csv"
    legacy_name = f"{stem}_{report_date}.csv"
    if name == versioned_name:
        return SNAPSHOT_REPOSITORY_PATH / versioned_name
    if (
        revision_number == 1
        and revision_reason == "legacy_v1_manifest"
        and name == legacy_name
    ):
        return SNAPSHOT_REPOSITORY_PATH / legacy_name
    raise RuntimeError(
        "daily snapshot manifest path identity mismatch: "
        f"report_date={report_date} revision={revision} "
        f"expected_name={versioned_name} path={path_text}"
    )


def select_latest_snapshot_revisions(
    snapshot_dir: Path,
    artifact_id: str,
    *,
    through_date: str = "",
    report_date: str = "",
    manifest_path: Path | None = None,
    repository_root: Path | None = None,
    require_files: bool = True,
    verify_hash: bool = True,
    payload_loader: Callable[[Path], bytes] | None = None,
) -> tuple[SnapshotRevision, ...]:
    """Select the maximum revision for each ``(date, artifact_id)`` key.

    This is deliberately a technical manifest/path selector.  It does not
    interpret any model fields or decide which business artifact family a
    caller should consume.
    """

    snapshot_dir = Path(snapshot_dir)
    manifest_path = Path(manifest_path or snapshot_dir / MANIFEST_NAME)
    resolved_snapshot_dir = snapshot_dir.resolve()
    expected_snapshot_parts = tuple(
        part.casefold() for part in SNAPSHOT_REPOSITORY_PATH.parts
    )
    observed_snapshot_parts = tuple(
        part.casefold()
        for part in resolved_snapshot_dir.parts[-len(expected_snapshot_parts) :]
    )
    canonical_repository_layout = observed_snapshot_parts == expected_snapshot_parts
    inferred_root = (
        resolved_snapshot_dir.parents[len(expected_snapshot_parts) - 1]
        if canonical_repository_layout
        else resolved_snapshot_dir.parent
    )
    # The canonical directory uniquely identifies its repository root. This is
    # intentionally authoritative over a caller's module-level ROOT so a
    # relocated worktree or a safely injected test repository cannot resolve
    # relative manifest paths back into the old drive/worktree.
    repository_root = (
        inferred_root
        if canonical_repository_layout
        else Path(repository_root or inferred_root).resolve()
    )
    artifact_id = _text(artifact_id)
    if not artifact_id:
        raise RuntimeError("daily snapshot artifact_id must not be empty")
    if not manifest_path.is_file():
        raise RuntimeError(
            "daily snapshot revision selection requires the publisher manifest: "
            f"{manifest_path.as_posix()}"
        )

    try:
        manifest = pd.read_csv(manifest_path, dtype=str, keep_default_na=False)
    except Exception as exc:
        raise RuntimeError(
            f"failed to read daily snapshot manifest {manifest_path.as_posix()}: {exc}"
        ) from exc
    missing = sorted(REQUIRED_MANIFEST_COLUMNS - set(manifest.columns))
    if missing:
        raise RuntimeError(
            "daily snapshot manifest is missing required columns: "
            f"manifest={manifest_path.as_posix()} missing={missing}"
        )
    manifest = normalize_revision_manifest_schema(
        manifest,
        source=manifest_path.as_posix(),
    )

    work = manifest[manifest["artifact_id"].map(_text).eq(artifact_id)].copy()
    if work.empty:
        return ()
    work["_report_date"] = work["snapshot_report_date"].map(normalize_report_date)
    invalid_dates = work[work["_report_date"].eq("")]
    if not invalid_dates.empty:
        raise RuntimeError(
            "daily snapshot manifest contains invalid snapshot_report_date values: "
            f"artifact_id={artifact_id} rows={invalid_dates.index.tolist()}"
        )
    work["_revision"] = work["snapshot_revision"].map(normalize_snapshot_revision)
    work["_revision_number"] = work["_revision"].map(snapshot_revision_number)

    normalized_report_date = normalize_report_date(report_date) if report_date else ""
    normalized_through_date = normalize_report_date(through_date) if through_date else ""
    if report_date and not normalized_report_date:
        raise RuntimeError(f"invalid requested snapshot report_date: {report_date!r}")
    if through_date and not normalized_through_date:
        raise RuntimeError(f"invalid requested snapshot through_date: {through_date!r}")
    if normalized_report_date:
        work = work[work["_report_date"].eq(normalized_report_date)].copy()
    if normalized_through_date:
        work = work[work["_report_date"].le(normalized_through_date)].copy()
    if work.empty:
        return ()

    selected: list[SnapshotRevision] = []
    for date, group in work.groupby("_report_date", sort=True, dropna=False):
        ordered = group.sort_values("_revision_number").copy()
        observed = ordered["_revision_number"].astype(int).tolist()
        expected = list(range(1, len(ordered) + 1))
        if observed != expected:
            raise RuntimeError(
                "daily snapshot revision sequence is not continuous: "
                f"report_date={date} artifact_id={artifact_id} "
                f"observed={observed} expected={expected}"
            )
        if ordered["_revision_number"].duplicated().any():
            raise RuntimeError(
                "daily snapshot manifest contains duplicate revision keys: "
                f"report_date={date} artifact_id={artifact_id}"
            )

        previous_sha = ""
        previous_path = ""
        seen_snapshot_shas: set[str] = set()
        seen_canonical_shas: set[str] = set()
        resolved_paths: dict[int, Path] = {}
        for position, (row_index, row) in enumerate(ordered.iterrows(), start=1):
            revision = _text(row.get("_revision"))
            snapshot_sha = _text(row.get("snapshot_sha256")).lower()
            supersedes_sha = _text(row.get("supersedes_snapshot_sha256")).lower()
            revision_reason = _text(row.get("revision_reason"))
            path_text = _text(row.get("snapshot_path"))
            if SHA256_RE.fullmatch(snapshot_sha) is None:
                raise RuntimeError(
                    f"{date}/{artifact_id}/{revision}: invalid snapshot_sha256"
                )
            approved_relative_path = _validate_snapshot_path_identity(
                path_text,
                report_date=str(date),
                revision=revision,
                revision_number=int(row.get("_revision_number")),
                snapshot_sha256=snapshot_sha,
                artifact_id=artifact_id,
                revision_reason=revision_reason,
            )
            path = _resolve_snapshot_path(
                path_text,
                repository_root=repository_root,
                approved_relative_path=approved_relative_path,
                snapshot_dir=snapshot_dir,
            )
            _require_path_under_snapshot_dir(path, snapshot_dir)
            resolved_paths[int(row_index)] = path
            payload: bytes | None = None
            if require_files:
                try:
                    if payload_loader is not None:
                        payload = payload_loader(path)
                    elif path.is_file():
                        payload = path.read_bytes()
                    else:
                        raise FileNotFoundError(path)
                except (FileNotFoundError, OSError) as exc:
                    raise RuntimeError(
                        "manifest-selected daily snapshot file is missing: "
                        f"report_date={date} artifact_id={artifact_id} "
                        f"revision={revision} path={path.as_posix()}"
                    ) from exc
                if not isinstance(payload, bytes):
                    raise RuntimeError(
                        "daily snapshot payload_loader must return bytes: "
                        f"report_date={date} artifact_id={artifact_id} revision={revision}"
                    )
            if require_files and verify_hash and payload is not None:
                actual_sha = snapshot_payload_sha256(payload)
                accepted_hashes = (
                    snapshot_payload_sha256_candidates(payload)
                    if int(row.get("_revision_number")) == 1
                    else {actual_sha}
                )
                if snapshot_sha not in accepted_hashes:
                    raise RuntimeError(
                        "manifest-selected daily snapshot SHA-256 mismatch: "
                        f"report_date={date} artifact_id={artifact_id} "
                        f"revision={revision} expected={snapshot_sha} actual={actual_sha}"
                    )
            canonical_sha = (
                snapshot_payload_sha256(payload)
                if payload is not None
                else ""
            )
            if position == 1:
                if supersedes_sha:
                    raise RuntimeError(
                        f"{date}/{artifact_id}/r1: supersedes_snapshot_sha256 must be empty"
                    )
            elif supersedes_sha != previous_sha:
                raise RuntimeError(
                    f"{date}/{artifact_id}/{revision}: supersedes_snapshot_sha256 "
                    "does not match the prior revision"
                )
            if position > 1 and not revision_reason:
                raise RuntimeError(
                    f"{date}/{artifact_id}/{revision}: revision_reason is required"
                )
            if position > 1 and snapshot_sha in seen_snapshot_shas:
                raise RuntimeError(
                    f"{date}/{artifact_id}/{revision}: duplicate payload revision is forbidden"
                )
            if canonical_sha and canonical_sha in seen_canonical_shas:
                raise RuntimeError(
                    f"{date}/{artifact_id}/{revision}: "
                    "canonical duplicate payload revision is forbidden"
                )
            if previous_path and path_text == previous_path:
                raise RuntimeError(
                    f"{date}/{artifact_id}/{revision}: snapshot_path is reused across revisions"
                )
            previous_sha = snapshot_sha
            previous_path = path_text
            seen_snapshot_shas.add(snapshot_sha)
            if canonical_sha:
                seen_canonical_shas.add(canonical_sha)

        latest = ordered.iloc[-1]
        path_text = _text(latest.get("snapshot_path"))
        path = resolved_paths[int(latest.name)]
        snapshot_sha = _text(latest.get("snapshot_sha256")).lower()
        selected.append(
            SnapshotRevision(
                report_date=str(date),
                artifact_id=artifact_id,
                revision=_text(latest.get("_revision")),
                revision_number=int(latest.get("_revision_number")),
                path=path,
                path_text=path_text,
                snapshot_sha256=snapshot_sha,
                supersedes_snapshot_sha256=_text(
                    latest.get("supersedes_snapshot_sha256")
                ).lower(),
                revision_reason=_text(latest.get("revision_reason")),
            )
        )
    return tuple(selected)


def latest_snapshot_revision_for_date(
    snapshot_dir: Path,
    artifact_id: str,
    report_date: str,
    **kwargs: Any,
) -> SnapshotRevision | None:
    rows = select_latest_snapshot_revisions(
        snapshot_dir,
        artifact_id,
        report_date=report_date,
        **kwargs,
    )
    return rows[0] if rows else None
