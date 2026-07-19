from __future__ import annotations

import argparse
import hashlib
import os
import re
import shutil
import subprocess
import sys
import tempfile
import uuid
from collections.abc import Collection
from contextlib import contextmanager
from dataclasses import dataclass
from io import BytesIO
from pathlib import Path
from typing import Iterator

import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent))

from tracking_utils import (  # noqa: E402
    HISTORY_DIR,
    LATEST_DIR,
    normalize_date,
    now_text,
    read_csv,
    safe_str,
    write_csv,
)


SNAPSHOT_DIR = HISTORY_DIR / "daily_model_snapshots"
MANIFEST_PATH = SNAPSHOT_DIR / "daily_published_model_snapshot_manifest.csv"
SNAPSHOT_REPOSITORY_PATH = Path("output/history/daily_model_snapshots")
LATEST_REPOSITORY_PATH = Path("output/latest")
REQUIRED_READY_COLUMNS = ["report_ready", "daily_pdf_ready"]
INITIAL_REVISION_REASON = "initial_publish"
LEGACY_REVISION_REASON = "legacy_v1_manifest"
REVISION_RE = re.compile(r"r([1-9][0-9]*)")
WARRANT_GRACE_COLUMNS = (
    "warrant_source_status",
    "warrant_daily_publish_allowed",
    "warrant_pdf_visibility",
    "warrant_model_effect_allowed",
    "warrant_pdf_effect_allowed",
)


@dataclass(frozen=True)
class SnapshotArtifact:
    artifact_id: str
    source_name: str
    snapshot_stem: str
    required_columns: tuple[str, ...] = ()
    date_columns: tuple[str, ...] = ()


ARTIFACTS: tuple[SnapshotArtifact, ...] = (
    SnapshotArtifact(
        artifact_id="data_freshness",
        source_name="data_freshness_latest.csv",
        snapshot_stem="data_freshness",
        required_columns=("main_price_date", "report_ready", "warrant_ready", "daily_pdf_ready"),
        date_columns=("main_price_date",),
    ),
    SnapshotArtifact(
        artifact_id="model_signals_for_report",
        source_name="daily_candidate_model_signals_for_report_latest.csv",
        snapshot_stem="daily_candidate_model_signals_for_report",
        required_columns=(
            "signal_date",
            "stock_id",
            "model_id",
            "model_name_zh",
            "model_score",
            "base_model_score",
            "operation_score",
            "tdcc_score",
            "pattern_score",
            "risk_penalty",
            "final_rank_score",
            "rank_reason_zh",
        ),
        date_columns=("signal_date",),
    ),
    SnapshotArtifact(
        artifact_id="all_candidates_source_rows",
        source_name="all_candidates_latest.csv",
        snapshot_stem="all_candidates",
        required_columns=(
            "date",
            "signal_date",
            "main_price_date",
            "stock_id",
            "stock_name",
            "category",
            "candidate_source_type",
            "candidate_line",
            "candidate_line_group",
            "source_row_index",
            "close",
            "ema23",
            "ma20",
            "distance_to_ema23_pct",
            "gap_ema23_pct",
            "platform_low",
            "short_platform_low",
            "previous_20d_low",
            "low_20",
            "ma5_turning_up_flag",
            "ma10_turning_up_flag",
            "volume_ratio",
            "return_20d",
            "latest_revenue_yoy",
            "cumulative_revenue_yoy",
            "off_60d_low_pct",
            "tdcc_judgement",
            "tdcc_accumulation_signal",
            "warrant_flow_signal",
            "false_breakout_risk",
        ),
        date_columns=("date", "signal_date", "main_price_date"),
    ),
    SnapshotArtifact(
        artifact_id="model_summary_for_report",
        source_name="daily_candidate_model_summary_for_report_latest.csv",
        snapshot_stem="daily_candidate_model_summary_for_report",
        required_columns=("signal_date", "report_line", "model_id", "model_name_zh"),
        date_columns=("signal_date",),
    ),
    SnapshotArtifact(
        artifact_id="model_registry",
        source_name="daily_report_model_registry_latest.csv",
        snapshot_stem="daily_report_model_registry",
        required_columns=("model_id", "model_name_zh", "model_registry_order"),
    ),
    SnapshotArtifact(
        artifact_id="model_parameters",
        source_name="daily_candidate_model_parameters_latest.csv",
        snapshot_stem="daily_candidate_model_parameters",
        required_columns=("model_id", "model_name_zh"),
    ),
    SnapshotArtifact(
        artifact_id="volume_breakout_operation_section",
        source_name="daily_volume_breakout_operation_section_latest.csv",
        snapshot_stem="daily_volume_breakout_operation_section",
        required_columns=(
            "model_id",
            "pdf_view",
            "pdf_section",
            "row_type",
            "buy_rank_eligible",
            "selected_trigger_id",
            "operation_score",
            "tdcc_score",
            "pattern_score",
            "risk_penalty",
            "final_rank_score",
            "entry_rule_id",
            "stop_loss_rule_id",
            "stop_loss_price",
            "exit_rule_id",
            "planned_holding_days",
        ),
    ),
    SnapshotArtifact(
        artifact_id="volume_breakout_operation_evidence_audit",
        source_name="daily_volume_breakout_operation_evidence_audit_latest.csv",
        snapshot_stem="daily_volume_breakout_operation_evidence_audit",
        required_columns=(
            "model_id",
            "operation_asof_date",
            "stock_id",
            "signal_date",
            "selected_trigger_id",
            "selected_confirmation_date",
            "operation_lifecycle_state",
            "audit_status",
            "included_in_daily_adapter",
            "reason",
        ),
    ),
    SnapshotArtifact(
        artifact_id="w_bottom_right_side_operation_section",
        source_name="daily_w_bottom_right_side_operation_section_latest.csv",
        snapshot_stem="daily_w_bottom_right_side_operation_section",
        required_columns=(
            "model_id",
            "pdf_view",
            "pdf_section",
            "row_type",
            "buy_rank_eligible",
            "row_action_status",
            "entry_rule_id",
            "stop_loss_rule_id",
            "stop_loss_price",
            "exit_rule_id",
            "planned_holding_days",
        ),
    ),
    SnapshotArtifact(
        artifact_id="neckline_volume_breakout_confirmation_operation_section",
        source_name="daily_neckline_volume_breakout_confirmation_operation_section_latest.csv",
        snapshot_stem="daily_neckline_volume_breakout_confirmation_operation_section",
        required_columns=(
            "model_id",
            "pdf_view",
            "pdf_section",
            "row_type",
            "buy_rank_eligible",
            "row_action_status",
            "entry_rule_id",
            "stop_loss_rule_id",
            "stop_loss_price",
            "exit_rule_id",
            "planned_holding_days",
        ),
    ),
)
ARTIFACTS_BY_ID = {artifact.artifact_id: artifact for artifact in ARTIFACTS}

MANIFEST_COLUMNS = [
    "snapshot_report_date",
    "snapshot_revision",
    "supersedes_snapshot_sha256",
    "revision_reason",
    "generated_at",
    "pipeline_commit_sha",
    "main_price_date",
    "report_ready",
    "warrant_ready",
    "warrant_source_status",
    "warrant_daily_publish_allowed",
    "warrant_pdf_visibility",
    "warrant_model_effect_allowed",
    "warrant_pdf_effect_allowed",
    "daily_pdf_ready",
    "artifact_id",
    "source_path",
    "snapshot_path",
    "source_sha256",
    "snapshot_sha256",
    "row_count",
    "column_count",
    "purpose",
]

REVISION_MANIFEST_COLUMNS = (
    "snapshot_revision",
    "supersedes_snapshot_sha256",
    "revision_reason",
)
WARRANT_LINEAGE_MANIFEST_COLUMNS = (
    "warrant_source_status",
    "warrant_daily_publish_allowed",
    "warrant_pdf_visibility",
    "warrant_model_effect_allowed",
    "warrant_pdf_effect_allowed",
)
LEGACY_MANIFEST_COLUMNS = [
    column for column in MANIFEST_COLUMNS if column not in REVISION_MANIFEST_COLUMNS
]
PRE_WARRANT_LEGACY_MANIFEST_COLUMNS = [
    column
    for column in LEGACY_MANIFEST_COLUMNS
    if column not in WARRANT_LINEAGE_MANIFEST_COLUMNS
]
KNOWN_MANIFEST_SCHEMAS = (
    ("revision_v2", MANIFEST_COLUMNS),
    ("legacy_v1_with_warrant_lineage", LEGACY_MANIFEST_COLUMNS),
    ("legacy_v1_pre_warrant_lineage", PRE_WARRANT_LEGACY_MANIFEST_COLUMNS),
)


def git_sha() -> str:
    env = os.environ.get("GITHUB_SHA", "").strip()
    if env:
        return env
    try:
        return subprocess.check_output(["git", "rev-parse", "HEAD"], text=True).strip()
    except Exception:
        return ""


def sha256_file(path: Path) -> str:
    # Published model snapshots are CSV/text artifacts committed from Linux
    # Actions and also validated from Windows worktrees. Normalize line endings
    # so Git checkout CRLF conversion cannot create false hash mismatches.
    # Do not strip a UTF-8 BOM here: snapshot_sha256 is an established immutable
    # manifest-v1 identity. The formal-lineage audit records its separate
    # BOM-insensitive canonical hash without rewriting historical manifests.
    digest = hashlib.sha256()
    data = path.read_bytes().replace(b"\r\n", b"\n").replace(b"\r", b"\n")
    digest.update(data)
    return digest.hexdigest()


def manifest_v1_sha256_candidates(path: Path) -> set[str]:
    """Accept immutable legacy raw/LF/CRLF identities without changing them."""

    payload = path.read_bytes()
    lf = payload.replace(b"\r\n", b"\n").replace(b"\r", b"\n")
    crlf = lf.replace(b"\n", b"\r\n")
    return {
        hashlib.sha256(candidate).hexdigest()
        for candidate in (payload, lf, crlf)
    }


def repository_root_for_snapshot_dir(snapshot_dir: Path) -> Path:
    """Return the repository root for the one approved snapshot directory."""

    resolved = Path(snapshot_dir).resolve()
    expected_parts = tuple(part.casefold() for part in SNAPSHOT_REPOSITORY_PATH.parts)
    observed_parts = tuple(part.casefold() for part in resolved.parts[-len(expected_parts) :])
    if observed_parts != expected_parts:
        raise RuntimeError(
            "daily snapshot directory must be the repository-owned path "
            f"{SNAPSHOT_REPOSITORY_PATH.as_posix()}: observed={resolved.as_posix()}"
        )
    return resolved.parents[len(expected_parts) - 1]


def _is_absolute_manifest_text(path_text: str) -> bool:
    normalized = path_text.replace("\\", "/")
    return bool(
        normalized.startswith("/")
        or normalized.startswith("//")
        or re.match(r"^[A-Za-z]:/", normalized)
    )


def resolve_approved_manifest_path(
    path_text: object,
    *,
    repository_root: Path,
    approved_relative_path: Path,
    path_kind: str,
) -> Path:
    """Resolve a portable path or a strictly identifiable legacy absolute path.

    New manifests store repository-relative POSIX paths.  A pre-existing
    absolute C:/runner path is relocatable only when its complete trailing path
    is exactly the approved repository path, so relocation never guesses a
    filename or trusts an escaped path.
    """

    raw = safe_str(path_text)
    if not raw:
        raise RuntimeError(f"daily snapshot manifest has an empty {path_kind}")
    if "\x00" in raw:
        raise RuntimeError(f"daily snapshot manifest {path_kind} contains NUL")
    normalized = raw.replace("\\", "/")
    parts = tuple(part for part in normalized.split("/") if part)
    if not parts or any(part in {".", ".."} for part in parts):
        raise RuntimeError(
            f"daily snapshot manifest {path_kind} contains a path escape: {raw}"
        )

    approved_text = approved_relative_path.as_posix()
    approved_parts = tuple(approved_relative_path.parts)
    if _is_absolute_manifest_text(raw):
        observed_tail = tuple(part.casefold() for part in parts[-len(approved_parts) :])
        expected_tail = tuple(part.casefold() for part in approved_parts)
        if observed_tail != expected_tail:
            raise RuntimeError(
                f"legacy absolute {path_kind} does not end in the approved path "
                f"{approved_text}: observed={raw}"
            )
    elif raw != approved_text:
        raise RuntimeError(
            f"daily snapshot manifest {path_kind} must be repository-relative POSIX "
            f"{approved_text}: observed={raw}"
        )

    root = Path(repository_root).resolve()
    resolved = (root / approved_relative_path).resolve()
    try:
        resolved.relative_to(root)
    except ValueError as exc:
        raise RuntimeError(
            f"daily snapshot manifest {path_kind} escapes repository root: {raw}"
        ) from exc
    return resolved


def approved_source_repository_path(artifact: SnapshotArtifact) -> Path:
    return LATEST_REPOSITORY_PATH / artifact.source_name


def approved_snapshot_repository_path(
    artifact: SnapshotArtifact,
    report_date: str,
    snapshot_revision: str,
    snapshot_sha256: str,
    *,
    legacy_r1: bool = False,
) -> Path:
    name = (
        legacy_snapshot_name(artifact, report_date)
        if legacy_r1
        else snapshot_name(artifact, report_date, snapshot_revision, snapshot_sha256)
    )
    return SNAPSHOT_REPOSITORY_PATH / name


def resolve_manifest_snapshot_path(
    path_text: object,
    *,
    repository_root: Path,
    artifact: SnapshotArtifact,
    report_date: str,
    snapshot_revision: str,
    snapshot_sha256: str,
    revision_reason: str,
) -> Path:
    legacy_r1 = bool(
        snapshot_revision == "r1" and revision_reason == LEGACY_REVISION_REASON
    )
    approved_paths = [
        approved_snapshot_repository_path(
            artifact,
            report_date,
            snapshot_revision,
            snapshot_sha256,
        )
    ]
    if legacy_r1:
        approved_paths.append(
            approved_snapshot_repository_path(
                artifact,
                report_date,
                snapshot_revision,
                snapshot_sha256,
                legacy_r1=True,
            )
        )
    errors: list[str] = []
    for approved in approved_paths:
        try:
            return resolve_approved_manifest_path(
                path_text,
                repository_root=repository_root,
                approved_relative_path=approved,
                path_kind="snapshot_path",
            )
        except RuntimeError as exc:
            errors.append(str(exc))
    raise RuntimeError("; ".join(errors))


def csv_shape(path: Path) -> tuple[int, int]:
    df = pd.read_csv(path, dtype=str)
    return len(df), len(df.columns)


def true_text(value: object) -> bool:
    return safe_str(value).lower() in {"true", "1", "yes", "y"}


def warrant_grace_allows_publish(row: pd.Series) -> bool:
    return bool(
        safe_str(row.get("warrant_source_status", "")) == "warning_grace"
        and true_text(row.get("warrant_daily_publish_allowed", ""))
        and safe_str(row.get("warrant_pdf_visibility", "")) == "hidden_unavailable"
        and not true_text(row.get("warrant_model_effect_allowed", ""))
        and not true_text(row.get("warrant_pdf_effect_allowed", ""))
    )


def freshness_state(latest_dir: Path = LATEST_DIR) -> dict[str, str]:
    path = latest_dir / "data_freshness_latest.csv"
    freshness = read_csv(path, dtype=str)
    if freshness.empty:
        raise RuntimeError(f"{path.as_posix()} is missing or empty")

    row = freshness.iloc[0]
    main_price_date = normalize_date(row.get("main_price_date", ""))
    if not main_price_date:
        raise RuntimeError("data_freshness_latest.csv does not contain main_price_date")

    state = {"main_price_date": main_price_date}
    for col in REQUIRED_READY_COLUMNS:
        value = safe_str(row.get(col, ""))
        if value != "True":
            raise RuntimeError(f"{col} must be True before publishing model snapshots; observed={value}")
        state[col] = value
    warrant_ready = safe_str(row.get("warrant_ready", ""))
    if warrant_ready != "True" and not warrant_grace_allows_publish(row):
        raise RuntimeError(
            "warrant_ready must be True before publishing model snapshots unless bounded "
            f"warrant_unavailable grace hides warrant effects; observed={warrant_ready}"
        )
    state["warrant_ready"] = warrant_ready
    if warrant_ready == "True":
        defaults = {
            "warrant_source_status": "ok",
            "warrant_daily_publish_allowed": "True",
            "warrant_pdf_visibility": "visible",
            "warrant_model_effect_allowed": "True",
            "warrant_pdf_effect_allowed": "True",
        }
    else:
        defaults = {col: "" for col in WARRANT_GRACE_COLUMNS}
    for col in WARRANT_GRACE_COLUMNS:
        state[col] = safe_str(row.get(col, "")) or defaults[col]
    return state


def validate_artifact_frame(path: Path, artifact: SnapshotArtifact, report_date: str) -> pd.DataFrame:
    df = pd.read_csv(path, dtype=str)
    missing = [col for col in artifact.required_columns if col not in df.columns]
    if missing:
        raise RuntimeError(f"{path.as_posix()} missing required columns: {missing}")

    for col in artifact.date_columns:
        if col not in df.columns:
            raise RuntimeError(f"{path.as_posix()} missing required date column: {col}")
        values = {normalize_date(value) for value in df[col].tolist()}
        values.discard("")
        if values and values != {report_date}:
            raise RuntimeError(
                f"{path.as_posix()} column {col} must match report date {report_date}; observed={sorted(values)}"
            )
    return df


def parse_snapshot_revision(value: object) -> int:
    text = safe_str(value)
    match = REVISION_RE.fullmatch(text)
    if match is None:
        raise RuntimeError(f"invalid snapshot_revision: {text!r}")
    return int(match.group(1))


def validate_known_manifest_schema(
    manifest: pd.DataFrame,
    *,
    context: str,
) -> str:
    """Accept only the exact registered current or legacy manifest headers."""

    observed = list(manifest.columns)
    for schema_name, expected in KNOWN_MANIFEST_SCHEMAS:
        if observed == list(expected):
            return schema_name

    expected_set = set(MANIFEST_COLUMNS)
    observed_set = set(observed)
    missing = [column for column in MANIFEST_COLUMNS if column not in observed_set]
    unexpected = [column for column in observed if column not in expected_set]
    if not missing and not unexpected:
        detail = "registered columns are reordered"
    else:
        detail = f"missing={missing} unexpected={unexpected}"
    raise RuntimeError(
        f"{context} has an unapproved daily snapshot manifest schema; "
        f"{detail}; refusing silent normalization"
    )


def normalize_manifest_revisions(manifest: pd.DataFrame) -> pd.DataFrame:
    """Map an exact legacy manifest schema to revision r1 without moving files."""

    normalized = manifest.copy()
    present_revision_columns = {
        column for column in REVISION_MANIFEST_COLUMNS if column in normalized.columns
    }
    if present_revision_columns and present_revision_columns != set(
        REVISION_MANIFEST_COLUMNS
    ):
        missing = sorted(set(REVISION_MANIFEST_COLUMNS) - present_revision_columns)
        raise RuntimeError(
            "daily snapshot manifest has a partial revision schema; "
            f"missing={missing}; refusing silent normalization"
        )

    legacy_revision_schema = not present_revision_columns
    if legacy_revision_schema:
        normalized["snapshot_revision"] = "r1"
        normalized["supersedes_snapshot_sha256"] = ""
        normalized["revision_reason"] = LEGACY_REVISION_REASON
        return normalized

    normalized["snapshot_revision"] = normalized["snapshot_revision"].map(safe_str)
    normalized["supersedes_snapshot_sha256"] = normalized[
        "supersedes_snapshot_sha256"
    ].map(safe_str)
    normalized["revision_reason"] = normalized["revision_reason"].map(safe_str)
    return normalized


def normalize_known_manifest_schema(
    manifest: pd.DataFrame,
    *,
    context: str,
) -> pd.DataFrame:
    """Upgrade only explicitly registered legacy schemas to the current schema."""

    schema_name = validate_known_manifest_schema(manifest, context=context)
    normalized = normalize_manifest_revisions(manifest)
    migration_defaults = {
        "warrant_source_status": "ok",
        "warrant_daily_publish_allowed": "True",
        "warrant_pdf_visibility": "visible",
        "warrant_model_effect_allowed": "True",
        "warrant_pdf_effect_allowed": "True",
    }
    warrant_ready_values = normalized["warrant_ready"].map(safe_str)
    legacy_schema = schema_name.startswith("legacy_v1_")
    for column, default in migration_defaults.items():
        if column not in normalized.columns:
            normalized[column] = warrant_ready_values.map(
                lambda value: default if value == "True" else ""
            )
        elif legacy_schema:
            normalized[column] = normalized[column].map(safe_str)
            missing_value = normalized[column].eq("") & warrant_ready_values.eq("True")
            normalized.loc[missing_value, column] = default
    return normalized[MANIFEST_COLUMNS].fillna("")


def read_existing_manifest_strict(
    manifest_path: Path,
) -> tuple[pd.DataFrame, bytes | None]:
    """Read the exact planning-time manifest bytes or fail closed.

    A missing manifest is the only state that may initialize a new revision
    registry.  An existing but unreadable, empty, or header-only file is not a
    new registry: treating it as one would erase the append-only lineage on the
    next atomic replace.
    """

    manifest_path = Path(manifest_path)
    if not manifest_path.exists():
        return pd.DataFrame(columns=MANIFEST_COLUMNS), None
    try:
        payload = manifest_path.read_bytes()
    except OSError as exc:
        raise RuntimeError(
            "existing daily snapshot manifest could not be read; refusing to "
            f"replace it: {manifest_path.as_posix()}: {exc}"
        ) from exc
    if not payload.strip():
        raise RuntimeError(
            "existing daily snapshot manifest is empty; refusing to replace it: "
            f"{manifest_path.as_posix()}"
        )
    try:
        manifest = pd.read_csv(
            BytesIO(payload),
            dtype=str,
            keep_default_na=False,
        ).fillna("")
    except Exception as exc:
        raise RuntimeError(
            "existing daily snapshot manifest is unreadable; refusing to replace it: "
            f"{manifest_path.as_posix()}: {exc}"
        ) from exc
    if manifest.empty:
        raise RuntimeError(
            "existing daily snapshot manifest has no data rows; refusing to replace it: "
            f"{manifest_path.as_posix()}"
        )
    validate_known_manifest_schema(
        manifest,
        context=f"existing daily snapshot manifest {manifest_path.as_posix()}",
    )
    return manifest, payload


def manifest_publication_lock_path(manifest_path: Path) -> Path:
    manifest_path = Path(manifest_path)
    return manifest_path.with_name(f".{manifest_path.name}.publish.lock")


@contextmanager
def manifest_publication_lock(manifest_path: Path) -> Iterator[Path]:
    """Hold one cross-platform exclusive lock for planning and publication.

    Exclusive creation works on both Windows and Linux.  A pre-existing lock is
    never guessed to be stale and is never deleted automatically.  The owner
    token also prevents this process from deleting a lock path that another
    actor replaced while publication was in progress.
    """

    manifest_path = Path(manifest_path)
    manifest_path.parent.mkdir(parents=True, exist_ok=True)
    lock_path = manifest_publication_lock_path(manifest_path)
    token = f"pid={os.getpid()} token={uuid.uuid4().hex}\n".encode("ascii")
    flags = os.O_CREAT | os.O_EXCL | os.O_WRONLY | getattr(os, "O_BINARY", 0)
    try:
        fd = os.open(lock_path, flags, 0o600)
    except FileExistsError as exc:
        raise RuntimeError(
            "daily snapshot publication lock already exists; refusing concurrent "
            f"or unknown-stale publication: {lock_path.as_posix()}"
        ) from exc
    except OSError as exc:
        raise RuntimeError(
            f"failed to create daily snapshot publication lock {lock_path.as_posix()}: {exc}"
        ) from exc

    token_ready = False
    try:
        try:
            written = os.write(fd, token)
            if written != len(token):
                raise OSError(
                    "short write while recording daily snapshot publication lock"
                )
            os.fsync(fd)
        finally:
            os.close(fd)
        token_ready = True
        yield lock_path
    finally:
        if not token_ready:
            # Exclusive creation succeeded, so this partial lock is ours.  It
            # is safe to remove; this is not an unknown pre-existing lock.
            lock_path.unlink(missing_ok=True)
        else:
            try:
                observed = lock_path.read_bytes()
            except FileNotFoundError as exc:
                raise RuntimeError(
                    "daily snapshot publication lock disappeared while held; "
                    f"refusing silent cleanup: {lock_path.as_posix()}"
                ) from exc
            except OSError as exc:
                raise RuntimeError(
                    "daily snapshot publication lock could not be verified before "
                    f"cleanup: {lock_path.as_posix()}: {exc}"
                ) from exc
            if observed != token:
                raise RuntimeError(
                    "daily snapshot publication lock ownership changed while held; "
                    f"unknown lock left in place: {lock_path.as_posix()}"
                )
            lock_path.unlink()


def assert_manifest_matches_planning_bytes(
    manifest_path: Path,
    expected_manifest_bytes: bytes | None,
) -> None:
    """CAS guard against writers that bypass the publication lock."""

    manifest_path = Path(manifest_path)
    if expected_manifest_bytes is None:
        if manifest_path.exists():
            raise RuntimeError(
                "daily snapshot manifest changed since planning: expected missing, "
                f"observed existing {manifest_path.as_posix()}"
            )
        return
    try:
        observed = manifest_path.read_bytes()
    except FileNotFoundError as exc:
        raise RuntimeError(
            "daily snapshot manifest changed since planning: expected existing, "
            f"observed missing {manifest_path.as_posix()}"
        ) from exc
    except OSError as exc:
        raise RuntimeError(
            "daily snapshot manifest could not be re-read for compare-and-swap: "
            f"{manifest_path.as_posix()}: {exc}"
        ) from exc
    if observed != expected_manifest_bytes:
        raise RuntimeError(
            "daily snapshot manifest changed since planning; refusing atomic replace: "
            f"{manifest_path.as_posix()}"
        )


def snapshot_name(
    artifact: SnapshotArtifact,
    report_date: str,
    snapshot_revision: str,
    snapshot_sha256: str,
) -> str:
    parse_snapshot_revision(snapshot_revision)
    if not re.fullmatch(r"[0-9a-f]{64}", snapshot_sha256):
        raise RuntimeError(f"invalid snapshot SHA-256 for filename: {snapshot_sha256!r}")
    return (
        f"{artifact.snapshot_stem}_{report_date}_{snapshot_revision}_"
        f"{snapshot_sha256[:12]}.csv"
    )


def legacy_snapshot_name(artifact: SnapshotArtifact, report_date: str) -> str:
    return f"{artifact.snapshot_stem}_{report_date}.csv"


def validate_revision_group(
    rows: pd.DataFrame,
    *,
    report_date: str,
    artifact_id: str,
) -> pd.DataFrame:
    if rows.empty:
        return rows.copy()

    numbered: list[tuple[int, int]] = []
    for index, row in rows.iterrows():
        try:
            number = parse_snapshot_revision(row.get("snapshot_revision", ""))
        except RuntimeError as exc:
            raise RuntimeError(
                f"{report_date}/{artifact_id}: {exc}"
            ) from exc
        numbered.append((number, index))
    numbered.sort()
    numbers = [number for number, _ in numbered]
    expected = list(range(1, len(numbered) + 1))
    if numbers != expected:
        raise RuntimeError(
            "daily snapshot revision sequence must be continuous: "
            f"report_date={report_date} artifact_id={artifact_id} "
            f"observed={numbers} expected={expected}"
        )

    ordered = rows.loc[[index for _, index in numbered]].copy().reset_index(drop=True)
    prior_sha = ""
    prior_path = ""
    seen_snapshot_shas: set[str] = set()
    for position, (_, row) in enumerate(ordered.iterrows(), start=1):
        revision = safe_str(row.get("snapshot_revision", ""))
        snapshot_sha = safe_str(row.get("snapshot_sha256", ""))
        source_sha = safe_str(row.get("source_sha256", ""))
        supersedes = safe_str(row.get("supersedes_snapshot_sha256", ""))
        reason = safe_str(row.get("revision_reason", ""))
        snapshot_path = safe_str(row.get("snapshot_path", ""))
        if not re.fullmatch(r"[0-9a-f]{64}", snapshot_sha):
            raise RuntimeError(
                f"{report_date}/{artifact_id}/{revision}: invalid snapshot_sha256"
            )
        if source_sha != snapshot_sha:
            raise RuntimeError(
                f"{report_date}/{artifact_id}/{revision}: source_sha256 must equal snapshot_sha256"
            )
        if position == 1:
            if supersedes:
                raise RuntimeError(
                    f"{report_date}/{artifact_id}/r1: supersedes_snapshot_sha256 must be empty"
                )
        else:
            if not reason:
                raise RuntimeError(
                    f"{report_date}/{artifact_id}/{revision}: revision_reason is required"
                )
            if supersedes != prior_sha:
                raise RuntimeError(
                    f"{report_date}/{artifact_id}/{revision}: supersedes_snapshot_sha256 "
                    "must equal the prior revision snapshot_sha256"
                )
            if snapshot_sha in seen_snapshot_shas:
                raise RuntimeError(
                    f"{report_date}/{artifact_id}/{revision}: duplicate payload revision is forbidden"
                )
        if snapshot_path == prior_path and prior_path:
            raise RuntimeError(
                f"{report_date}/{artifact_id}/{revision}: snapshot_path must be immutable per revision"
            )
        prior_sha = snapshot_sha
        prior_path = snapshot_path
        seen_snapshot_shas.add(snapshot_sha)
    return ordered


def publish_snapshot_transaction(
    copy_plans: Collection[tuple[Path, Path, str]],
    manifest: pd.DataFrame,
    manifest_path: Path,
    *,
    expected_manifest_bytes: bytes | None,
) -> None:
    """Publish immutable files and their manifest without partial final writes.

    Every new snapshot and the replacement manifest are fully written under
    temporary names first.  A caught promotion failure removes every final
    snapshot created by this transaction and leaves the prior manifest intact.
    Pre-existing content-addressed targets are reused only when their hashes
    match and are never removed during rollback.
    """

    manifest_path.parent.mkdir(parents=True, exist_ok=True)
    prepared: list[tuple[Path, Path, str]] = []
    temporary_paths: list[Path] = []
    promoted_targets: list[Path] = []
    manifest_temp: Path | None = None
    manifest_committed = False

    try:
        for source, target, expected_hash in copy_plans:
            if target.exists():
                if sha256_file(target) != expected_hash:
                    raise RuntimeError(
                        "immutable daily snapshot target changed before promotion: "
                        f"{target.as_posix()}"
                    )
                continue
            fd, temp_name = tempfile.mkstemp(
                dir=target.parent,
                prefix=f".{target.name}.",
                suffix=".tmp",
            )
            os.close(fd)
            temp_path = Path(temp_name)
            temporary_paths.append(temp_path)
            shutil.copyfile(source, temp_path)
            if sha256_file(temp_path) != expected_hash:
                raise RuntimeError(
                    f"new immutable daily snapshot hash mismatch: {target.as_posix()}"
                )
            prepared.append((temp_path, target, expected_hash))

        fd, manifest_temp_name = tempfile.mkstemp(
            dir=manifest_path.parent,
            prefix=f".{manifest_path.name}.",
            suffix=".tmp",
        )
        os.close(fd)
        manifest_temp = Path(manifest_temp_name)
        temporary_paths.append(manifest_temp)
        write_csv(manifest, manifest_temp)

        for temp_path, target, expected_hash in prepared:
            if target.exists():
                if sha256_file(target) != expected_hash:
                    raise RuntimeError(
                        "immutable daily snapshot target changed during promotion: "
                        f"{target.as_posix()}"
                    )
                temp_path.unlink()
                temporary_paths.remove(temp_path)
                continue
            os.replace(temp_path, target)
            promoted_targets.append(target)
            temporary_paths.remove(temp_path)

        # The exclusive lock serializes cooperating writers.  This byte-exact
        # compare-and-swap additionally rejects any writer that bypassed the
        # lock after planning but before the manifest promotion.  Snapshot
        # targets promoted above remain rollback-owned until this check passes.
        assert_manifest_matches_planning_bytes(
            manifest_path,
            expected_manifest_bytes,
        )
        os.replace(manifest_temp, manifest_path)
        manifest_committed = True
        temporary_paths.remove(manifest_temp)
    except Exception as exc:
        cleanup_errors: list[str] = []
        if not manifest_committed:
            for target in reversed(promoted_targets):
                try:
                    target.unlink(missing_ok=True)
                except OSError as cleanup_exc:
                    cleanup_errors.append(f"{target.as_posix()}: {cleanup_exc}")
        for temp_path in temporary_paths:
            try:
                temp_path.unlink(missing_ok=True)
            except OSError as cleanup_exc:
                cleanup_errors.append(f"{temp_path.as_posix()}: {cleanup_exc}")
        if cleanup_errors:
            raise RuntimeError(
                "daily snapshot transaction failed and rollback was incomplete: "
                + "; ".join(cleanup_errors)
            ) from exc
        raise


def selected_artifacts(artifact_ids: Collection[str] | None) -> tuple[SnapshotArtifact, ...]:
    if artifact_ids is None:
        return ARTIFACTS
    requested = {safe_str(artifact_id) for artifact_id in artifact_ids if safe_str(artifact_id)}
    if not requested:
        raise RuntimeError("explicit daily snapshot artifact selection must not be empty")
    unknown = sorted(requested - set(ARTIFACTS_BY_ID))
    if unknown:
        raise RuntimeError(f"unknown daily snapshot artifact ids: {unknown}")
    return tuple(artifact for artifact in ARTIFACTS if artifact.artifact_id in requested)


def _build_daily_published_model_snapshots_under_lock(
    latest_dir: Path = LATEST_DIR,
    snapshot_dir: Path = SNAPSHOT_DIR,
    manifest_path: Path = MANIFEST_PATH,
    generated_at: str | None = None,
    commit_sha: str | None = None,
    artifact_ids: Collection[str] | None = None,
    revision_reason: str = "",
) -> pd.DataFrame:
    state = freshness_state(latest_dir)
    artifacts = selected_artifacts(artifact_ids)
    report_date = state["main_price_date"]
    generated_at = generated_at or now_text()
    commit_sha = commit_sha if commit_sha is not None else git_sha()
    revision_reason = safe_str(revision_reason)
    snapshot_dir.mkdir(parents=True, exist_ok=True)
    repository_root = repository_root_for_snapshot_dir(snapshot_dir)
    approved_latest_dir = (repository_root / LATEST_REPOSITORY_PATH).resolve()
    if Path(latest_dir).resolve() != approved_latest_dir:
        raise RuntimeError(
            "daily snapshot latest_dir must be the repository-owned path "
            f"{LATEST_REPOSITORY_PATH.as_posix()}: "
            f"observed={Path(latest_dir).resolve().as_posix()}"
        )

    old_manifest, planning_manifest_bytes = read_existing_manifest_strict(
        manifest_path
    )
    if not old_manifest.empty:
        old_manifest = normalize_known_manifest_schema(
            old_manifest,
            context=f"existing daily snapshot manifest {manifest_path.as_posix()}",
        )
    else:
        old_manifest = pd.DataFrame(columns=MANIFEST_COLUMNS)

    revision_groups: dict[tuple[str, str], pd.DataFrame] = {}
    revision_canonical_hashes: dict[tuple[str, str], set[str]] = {}
    if not old_manifest.empty:
        duplicate_paths = old_manifest["snapshot_path"].astype(str).duplicated(keep=False)
        if duplicate_paths.any():
            paths = sorted(set(old_manifest.loc[duplicate_paths, "snapshot_path"].astype(str)))
            raise RuntimeError(f"daily snapshot manifest reuses immutable paths: {paths}")
        grouped_manifest = old_manifest.assign(
            _report_date=old_manifest["snapshot_report_date"].map(normalize_date)
        )
        for (existing_date, existing_artifact_id), group in grouped_manifest.groupby(
            ["_report_date", "artifact_id"],
            sort=False,
            dropna=False,
        ):
            key = (safe_str(existing_date), safe_str(existing_artifact_id))
            ordered = validate_revision_group(
                group.drop(columns=["_report_date"]),
                report_date=key[0],
                artifact_id=key[1],
            )
            artifact = ARTIFACTS_BY_ID.get(key[1])
            if artifact is None:
                raise RuntimeError(
                    f"{key[0]}/{key[1]}: unknown artifact_id in daily snapshot manifest"
                )
            canonical_payloads: set[str] = set()
            for _, existing in ordered.iterrows():
                revision = safe_str(existing.get("snapshot_revision", ""))
                snapshot_sha = safe_str(existing.get("snapshot_sha256", ""))
                reason = safe_str(existing.get("revision_reason", ""))
                resolve_approved_manifest_path(
                    existing.get("source_path", ""),
                    repository_root=repository_root,
                    approved_relative_path=approved_source_repository_path(artifact),
                    path_kind="source_path",
                )
                existing_path = resolve_manifest_snapshot_path(
                    existing.get("snapshot_path", ""),
                    repository_root=repository_root,
                    artifact=artifact,
                    report_date=key[0],
                    snapshot_revision=revision,
                    snapshot_sha256=snapshot_sha,
                    revision_reason=reason,
                )
                if not existing_path.exists():
                    raise RuntimeError(
                        f"{key[0]}/{key[1]}/{revision}: "
                        f"snapshot file is missing: {existing_path.as_posix()}"
                    )
                accepted_hashes = (
                    manifest_v1_sha256_candidates(existing_path)
                    if revision == "r1"
                    else {sha256_file(existing_path)}
                )
                if snapshot_sha not in accepted_hashes:
                    raise RuntimeError(
                        f"{key[0]}/{key[1]}/{revision}: "
                        "existing immutable snapshot hash mismatch"
                    )
                canonical_sha = sha256_file(existing_path)
                if canonical_sha in canonical_payloads:
                    raise RuntimeError(
                        f"{key[0]}/{key[1]}/{revision}: "
                        "canonical duplicate payload revision is forbidden"
                    )
                canonical_payloads.add(canonical_sha)
            revision_groups[key] = ordered
            revision_canonical_hashes[key] = canonical_payloads

    result_rows: list[dict[str, str]] = []
    new_rows: list[dict[str, str]] = []
    copy_plans: list[tuple[Path, Path, str]] = []
    for artifact in artifacts:
        source = latest_dir / artifact.source_name
        if not source.exists():
            raise RuntimeError(f"required daily published artifact is missing: {source.as_posix()}")

        validate_artifact_frame(source, artifact, report_date)
        source_hash = sha256_file(source)
        ordered = revision_groups.get(
            (report_date, artifact.artifact_id),
            pd.DataFrame(columns=MANIFEST_COLUMNS),
        )

        latest_snapshot_path = (
            resolve_manifest_snapshot_path(
                ordered.iloc[-1].get("snapshot_path", ""),
                repository_root=repository_root,
                artifact=artifact,
                report_date=report_date,
                snapshot_revision=safe_str(
                    ordered.iloc[-1].get("snapshot_revision", "")
                ),
                snapshot_sha256=safe_str(
                    ordered.iloc[-1].get("snapshot_sha256", "")
                ),
                revision_reason=safe_str(
                    ordered.iloc[-1].get("revision_reason", "")
                ),
            )
            if not ordered.empty
            else None
        )
        if (
            latest_snapshot_path is not None
            and source_hash == sha256_file(latest_snapshot_path)
        ):
            result_rows.append(
                {
                    column: safe_str(ordered.iloc[-1].get(column, ""))
                    for column in MANIFEST_COLUMNS
                }
            )
            continue
        if source_hash in revision_canonical_hashes.get(
            (report_date, artifact.artifact_id), set()
        ):
            raise RuntimeError(
                "canonical duplicate payload revision is forbidden: "
                f"report_date={report_date} artifact_id={artifact.artifact_id}"
            )

        if ordered.empty:
            revision_number = 1
            supersedes_sha = ""
            row_reason = revision_reason or INITIAL_REVISION_REASON
        else:
            if not revision_reason:
                raise RuntimeError(
                    "revision_reason is required for a non-initial daily snapshot revision: "
                    f"report_date={report_date} artifact_id={artifact.artifact_id}"
                )
            revision_number = len(ordered) + 1
            supersedes_sha = safe_str(ordered.iloc[-1].get("snapshot_sha256", ""))
            row_reason = revision_reason
        revision = f"r{revision_number}"
        target = snapshot_dir / snapshot_name(
            artifact,
            report_date,
            revision,
            source_hash,
        )
        if target.exists() and sha256_file(target) != source_hash:
            raise RuntimeError(
                "immutable daily snapshot target already exists with a different payload: "
                f"{target.as_posix()}"
            )
        row_count, column_count = csv_shape(source)
        row = {
            "snapshot_report_date": report_date,
            "snapshot_revision": revision,
            "supersedes_snapshot_sha256": supersedes_sha,
            "revision_reason": row_reason,
            "generated_at": generated_at,
            "pipeline_commit_sha": commit_sha,
            "main_price_date": state["main_price_date"],
            "report_ready": state["report_ready"],
            "warrant_ready": state["warrant_ready"],
            "warrant_source_status": state["warrant_source_status"],
            "warrant_daily_publish_allowed": state["warrant_daily_publish_allowed"],
            "warrant_pdf_visibility": state["warrant_pdf_visibility"],
            "warrant_model_effect_allowed": state["warrant_model_effect_allowed"],
            "warrant_pdf_effect_allowed": state["warrant_pdf_effect_allowed"],
            "daily_pdf_ready": state["daily_pdf_ready"],
            "artifact_id": artifact.artifact_id,
            "source_path": approved_source_repository_path(artifact).as_posix(),
            "snapshot_path": (
                SNAPSHOT_REPOSITORY_PATH / target.name
            ).as_posix(),
            "source_sha256": source_hash,
            "snapshot_sha256": source_hash,
            "row_count": str(row_count),
            "column_count": str(column_count),
            "purpose": "as_published_daily_model_snapshot",
        }
        result_rows.append(row)
        new_rows.append(row)
        copy_plans.append((source, target, source_hash))

    new_manifest = pd.DataFrame(new_rows, columns=MANIFEST_COLUMNS)
    combined = pd.concat([old_manifest, new_manifest], ignore_index=True)

    combined = combined[MANIFEST_COLUMNS]
    combined["_revision_number"] = combined["snapshot_revision"].map(
        parse_snapshot_revision
    )
    combined = combined.sort_values(
        ["snapshot_report_date", "artifact_id", "_revision_number"]
    ).drop(columns=["_revision_number"])
    combined = combined.reset_index(drop=True)
    # All existing revision chains and required reasons are checked before the
    # transaction prepares temporary snapshots and an atomic manifest update.
    publish_snapshot_transaction(
        copy_plans,
        combined,
        manifest_path,
        expected_manifest_bytes=planning_manifest_bytes,
    )
    return pd.DataFrame(result_rows, columns=MANIFEST_COLUMNS)


def build_daily_published_model_snapshots(
    latest_dir: Path = LATEST_DIR,
    snapshot_dir: Path = SNAPSHOT_DIR,
    manifest_path: Path = MANIFEST_PATH,
    generated_at: str | None = None,
    commit_sha: str | None = None,
    artifact_ids: Collection[str] | None = None,
    revision_reason: str = "",
) -> pd.DataFrame:
    """Publish under one lock spanning manifest read, planning, and commit."""

    snapshot_dir = Path(snapshot_dir)
    manifest_path = Path(manifest_path)
    snapshot_dir.mkdir(parents=True, exist_ok=True)
    with manifest_publication_lock(manifest_path):
        return _build_daily_published_model_snapshots_under_lock(
            latest_dir=latest_dir,
            snapshot_dir=snapshot_dir,
            manifest_path=manifest_path,
            generated_at=generated_at,
            commit_sha=commit_sha,
            artifact_ids=artifact_ids,
            revision_reason=revision_reason,
        )


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Publish immutable daily model snapshots")
    parser.add_argument(
        "--artifact-id",
        action="append",
        choices=sorted(ARTIFACTS_BY_ID),
        help="Publish only the named artifact family; repeat for multiple families",
    )
    parser.add_argument(
        "--revision-reason",
        default="",
        help="Required reason when a selected same-date artifact creates revision r2 or later",
    )
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    try:
        manifest_rows = build_daily_published_model_snapshots(
            artifact_ids=args.artifact_id,
            revision_reason=args.revision_reason,
        )
    except Exception as exc:
        print(f"ERROR: {exc}")
        return 1

    report_date = safe_str(manifest_rows["snapshot_report_date"].iloc[0]) if not manifest_rows.empty else ""
    print(f"saved daily published model snapshots for report_date={report_date}")
    for _, row in manifest_rows.iterrows():
        print(
            "saved "
            f"{row['artifact_id']} {row['snapshot_revision']}: {row['snapshot_path']} "
            f"rows={row['row_count']} sha256={str(row['snapshot_sha256'])[:12]}"
        )
    print(f"saved manifest: {MANIFEST_PATH.as_posix()}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
