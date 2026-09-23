from __future__ import annotations

import argparse
import csv
from dataclasses import dataclass
import hashlib
import io
from pathlib import Path
import re
import stat
import subprocess
from typing import Mapping

import pandas as pd

# These are the same model's independent source-lineage algorithms, not the
# producer's condition, score, operation, or outcome implementation.
from validate_revenue_unreacted_range_source_snapshot_projection import (
    _canonical_monthly_table_sha256,
    _monthly_registry_sha256,
    _resolve_monthly,
)


ROOT = Path(__file__).resolve().parents[1]
MODEL_ID = "revenue_unreacted_range"
ARTIFACT_VERSION = "source_first_condition_v3_20260720"
BINDING_VERSION = "source_first_source_binding_v1_20260923"
APPROVAL_REF = "user_approved_revenue_source_version_binding_repair_20260923"
SOURCE_COMMIT = "0a7044debe9dbdae01b4e30910aec3d595ef4edf"
CUTOFF_DATE = "20260713"
BINDING_REL = "config/revenue_unreacted_range_source_first_source_binding.csv"
REVENUE_REL = "data/monthly_revenue_history/monthly_revenue_history.csv"
RESOLUTION_REL = "config/revenue_unreacted_range_monthly_revenue_cross_market_resolution.csv"
ARTIFACT_ID = "revenue_unreacted_range_source_first_condition_audit"
ARTIFACT_PATHS = (
    f"output/latest/research_backtest/{ARTIFACT_ID}_latest.csv",
    f"output/latest/research_backtest/{ARTIFACT_ID}_detail_latest.csv",
    f"output/latest/research_backtest/{ARTIFACT_ID}_latest.md",
    f"output/history/research/{ARTIFACT_ID}.csv",
    f"docs/latest/{ARTIFACT_ID}_latest.csv",
    f"docs/latest/{ARTIFACT_ID}_latest.md",
)
EXPECTED_ROLES = {
    REVENUE_REL: "monthly_revenue_source",
    RESOLUTION_REL: "monthly_resolution_source",
    **{path: "frozen_research_artifact" for path in ARTIFACT_PATHS},
}
BINDING_COLUMNS = (
    "binding_version",
    "model_id",
    "artifact_version",
    "approval_ref",
    "source_commit",
    "role",
    "path",
    "git_blob_oid",
    "git_bytes_sha256",
    "canonical_sha256",
    "research_only",
    "formal_model_use_allowed",
    "promotion_evidence_allowed",
    "pdf_consumption_allowed",
)
SHA256_PATTERN = re.compile(r"[0-9a-f]{64}\Z")
GIT_OID_PATTERN = re.compile(r"[0-9a-f]{40}\Z")


@dataclass(frozen=True)
class SourceBindingContext:
    source_commit: str
    full_lineage: dict[str, str]
    source_lineage: dict[tuple[str, str], dict[str, str]]
    cutoff_count: int
    cutoff_sha: str
    artifacts: dict[str, bytes]


def canonical_transport_bytes(payload: bytes) -> bytes:
    """Normalize only a leading UTF-8 BOM and CRLF, never CSV values or dates."""
    if not isinstance(payload, bytes):
        raise RuntimeError("source binding payload must be bytes")
    try:
        return payload.decode("utf-8-sig").replace("\r\n", "\n").encode("utf-8")
    except UnicodeError as exc:
        raise RuntimeError("source binding payload is not valid UTF-8") from exc


def _sha256(payload: bytes) -> str:
    return hashlib.sha256(payload).hexdigest()


def _git_blob_oid(payload: bytes) -> str:
    return hashlib.sha1(b"blob " + str(len(payload)).encode("ascii") + b"\0" + payload).hexdigest()


def _read_regular_file(path: Path, repository_root: Path) -> bytes:
    root = repository_root.absolute()
    candidate = path.absolute()
    try:
        relative = candidate.relative_to(root)
    except ValueError as exc:
        raise RuntimeError(f"source binding path is outside repository: {path}") from exc
    if not relative.parts or any(part in {".", ".."} for part in relative.parts):
        raise RuntimeError(f"unsafe source binding path: {path}")
    current = root
    for part in relative.parts:
        current = current / part
        try:
            metadata = current.lstat()
        except OSError as exc:
            raise RuntimeError(f"missing source binding file: {current}") from exc
        if stat.S_ISLNK(metadata.st_mode) or (
            getattr(metadata, "st_file_attributes", 0)
            & getattr(stat, "FILE_ATTRIBUTE_REPARSE_POINT", 0x400)
        ):
            raise RuntimeError(f"unsafe symlink/reparse source binding path: {current}")
    if not stat.S_ISREG(metadata.st_mode):
        raise RuntimeError(f"source binding path is not a regular file: {path}")
    return candidate.read_bytes()


def _git(repository_root: Path, *args: str) -> bytes:
    try:
        completed = subprocess.run(
            ["git", "--no-replace-objects", "-C", str(repository_root), *args],
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
    except (OSError, subprocess.CalledProcessError) as exc:
        raise RuntimeError(f"cannot read immutable source binding Git object: {args}") from exc
    return completed.stdout


def _binding_rows(payload: bytes) -> dict[str, dict[str, str]]:
    try:
        reader = csv.DictReader(io.StringIO(canonical_transport_bytes(payload).decode("utf-8")))
        if tuple(reader.fieldnames or ()) != BINDING_COLUMNS:
            raise RuntimeError("source binding CSV schema mismatch")
        rows = list(reader)
    except csv.Error as exc:
        raise RuntimeError("source binding CSV cannot be parsed") from exc
    if len(rows) != len(EXPECTED_ROLES):
        raise RuntimeError("source binding requires exactly two sources and six artifacts")
    paths = [row.get("path", "") for row in rows]
    if len(set(paths)) != len(paths) or set(paths) != set(EXPECTED_ROLES):
        raise RuntimeError("source binding exact path set drift")
    expected_constants = {
        "binding_version": BINDING_VERSION,
        "model_id": MODEL_ID,
        "artifact_version": ARTIFACT_VERSION,
        "approval_ref": APPROVAL_REF,
        "source_commit": SOURCE_COMMIT,
        "research_only": "true",
        "formal_model_use_allowed": "false",
        "promotion_evidence_allowed": "false",
        "pdf_consumption_allowed": "false",
    }
    for row in rows:
        if set(row) != set(BINDING_COLUMNS) or any(value is None for value in row.values()):
            raise RuntimeError("source binding row width mismatch")
        for column, expected in expected_constants.items():
            if row[column] != expected:
                raise RuntimeError(f"source binding {column} drift: {row['path']}")
        if row["role"] != EXPECTED_ROLES[row["path"]]:
            raise RuntimeError(f"source binding role drift: {row['path']}")
        for column in ("source_commit", "git_blob_oid"):
            if not GIT_OID_PATTERN.fullmatch(row[column]):
                raise RuntimeError(f"source binding invalid {column}: {row['path']}")
        for column in ("git_bytes_sha256", "canonical_sha256"):
            if not SHA256_PATTERN.fullmatch(row[column]):
                raise RuntimeError(f"source binding invalid {column}: {row['path']}")
    return {row["path"]: row for row in rows}


def _bound_git_payloads(
    repository_root: Path,
    rows: dict[str, dict[str, str]],
) -> dict[str, bytes]:
    resolved_commit = _git(repository_root, "rev-parse", "--verify", f"{SOURCE_COMMIT}^{{commit}}")
    if resolved_commit.decode("ascii").strip() != SOURCE_COMMIT:
        raise RuntimeError("source binding commit identity drift")
    payloads: dict[str, bytes] = {}
    for path, row in rows.items():
        tree = _git(repository_root, "ls-tree", "-z", SOURCE_COMMIT, "--", path)
        expected_tree = f"100644 blob {row['git_blob_oid']}\t{path}\0".encode("utf-8")
        if tree != expected_tree:
            raise RuntimeError(f"source binding Git blob identity/type drift: {path}")
        payload = _git(repository_root, "show", f"{SOURCE_COMMIT}:{path}")
        if _git_blob_oid(payload) != row["git_blob_oid"]:
            raise RuntimeError(f"source binding Git object content drift: {path}")
        if _sha256(payload) != row["git_bytes_sha256"]:
            raise RuntimeError(f"source binding Git bytes SHA-256 drift: {path}")
        payloads[path] = payload
    return payloads


def _read_csv(payload: bytes) -> pd.DataFrame:
    return pd.read_csv(io.BytesIO(payload), dtype=str, keep_default_na=False, low_memory=False)


def _check_artifact_capture(payloads: Mapping[str, bytes], full_lineage: dict[str, str]) -> None:
    for path in ARTIFACT_PATHS:
        if not path.endswith(".csv"):
            continue
        frame = _read_csv(payloads[path])
        expected = {
            "model_id": MODEL_ID,
            "artifact_id": ARTIFACT_ID,
            "artifact_version": ARTIFACT_VERSION,
            **full_lineage,
        }
        for column, value in expected.items():
            if column not in frame or set(frame[column]) != {value}:
                raise RuntimeError(f"source binding artifact capture {column} drift: {path}")
        for column in ("approved_for_daily", "production_change"):
            if column not in frame or set(frame[column].str.lower()) != {"false"}:
                raise RuntimeError(f"source binding artifact formal-use flag drift: {path}/{column}")


def load_bound_source_context(
    repository_root: Path = ROOT,
    binding_path: Path | None = None,
    artifacts: Mapping[str, bytes] | None = None,
) -> SourceBindingContext:
    """Verify the frozen capture without substituting Git bytes for missing files.

    Explicit ``artifacts`` is for callers that already obtained all six payloads
    (including read-only Git audits and synthetic tests). The default always
    requires the physical published files, even in a sparse checkout.
    """
    repository_root = Path(repository_root)
    binding_path = Path(binding_path) if binding_path is not None else repository_root / BINDING_REL
    rows = _binding_rows(_read_regular_file(binding_path, repository_root))
    if artifacts is None:
        observed = {
            path: _read_regular_file(repository_root / path, repository_root)
            for path in ARTIFACT_PATHS
        }
    else:
        if set(artifacts) != set(ARTIFACT_PATHS):
            raise RuntimeError("source binding explicit artifact exact path set drift")
        observed = dict(artifacts)
    payloads = _bound_git_payloads(repository_root, rows)
    for path in ARTIFACT_PATHS:
        expected_canonical = rows[path]["canonical_sha256"]
        if _sha256(canonical_transport_bytes(payloads[path])) != expected_canonical:
            raise RuntimeError(f"source binding immutable artifact canonical SHA-256 drift: {path}")
        if _sha256(canonical_transport_bytes(observed[path])) != expected_canonical:
            raise RuntimeError(f"source binding frozen artifact content drift: {path}")

    raw = _read_csv(payloads[REVENUE_REL])
    registry = _read_csv(payloads[RESOLUTION_REL])
    full = _resolve_monthly(raw, registry, None)
    cutoff = _resolve_monthly(raw, registry, CUTOFF_DATE)
    full_lineage = {
        "monthly_revenue_history_blob_sha256": _sha256(payloads[REVENUE_REL]),
        "monthly_revenue_canonical_table_sha256": _canonical_monthly_table_sha256(full),
        "cross_market_resolution_registry_canonical_sha256": _monthly_registry_sha256(registry),
    }
    for path, column in (
        (REVENUE_REL, "monthly_revenue_canonical_table_sha256"),
        (RESOLUTION_REL, "cross_market_resolution_registry_canonical_sha256"),
    ):
        if full_lineage[column] != rows[path]["canonical_sha256"]:
            raise RuntimeError(f"source binding source canonical SHA-256 drift: {path}")
    _check_artifact_capture(payloads, full_lineage)
    lineage: dict[tuple[str, str], dict[str, str]] = {}
    for row in full.itertuples(index=False):
        key = (str(row.stock_id), str(row.revenue_period))
        if key in lineage:
            raise RuntimeError(f"source binding canonical source duplicate key: {key}")
        lineage[key] = {
            "source_date": str(row.source_table_date),
            "cross_market_resolution_id": str(row.cross_market_resolution_id) or "none",
            "source_row_canonical_sha256": str(row.source_row_canonical_sha256),
            "canonical_source_table_date": str(row.canonical_source_table_date),
        }
    return SourceBindingContext(
        source_commit=SOURCE_COMMIT,
        full_lineage=full_lineage,
        source_lineage=lineage,
        cutoff_count=len(cutoff),
        cutoff_sha=_canonical_monthly_table_sha256(cutoff),
        artifacts={path: payloads[path] for path in ARTIFACT_PATHS},
    )


def validate(
    repository_root: Path = ROOT,
    binding_path: Path | None = None,
    artifacts: Mapping[str, bytes] | None = None,
) -> list[str]:
    try:
        load_bound_source_context(repository_root, binding_path, artifacts)
    except (OSError, RuntimeError, ValueError, KeyError, TypeError, UnicodeError) as exc:
        return [str(exc)]
    return []


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Validate the immutable monthly-revenue source-first binding.")
    parser.add_argument("--repo-root", type=Path, default=ROOT)
    parser.add_argument("--binding", type=Path, default=None)
    args = parser.parse_args(argv)
    errors = validate(args.repo_root, args.binding)
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1
    print(
        "revenue source-first source binding validation passed: "
        f"source_commit={SOURCE_COMMIT}; retained_frozen_source_evidence; "
        "research_only=true; promotion_evidence_allowed=false; no_recompute"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
