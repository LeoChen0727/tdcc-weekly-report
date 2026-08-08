#!/usr/bin/env python3
"""Create and verify fail-closed Daily Full validation replay checkpoints."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import shlex
import shutil
import subprocess
from pathlib import Path, PurePosixPath
from typing import Iterable, Sequence


SCHEMA_VERSION = 2
REPLAY_DATE = "20260807"
CHECKPOINT_MANIFEST = "checkpoint_manifest.json"
CHECKPOINT_MANIFEST_SHA = "checkpoint_manifest.sha256"
PAYLOAD_DIR = "payload"
REQUIRED_SOURCE_CATEGORIES = frozenset(
    {
        "market_session",
        "daily_price_raw",
        "daily_price_normalized",
        "candidate_inputs",
        "warrant_raw",
        "warrant_normalized",
        "trading_calendar",
    }
)
FORBIDDEN_COMMAND_PATTERNS = (
    re.compile(r"(^|\s)git\s+(commit|push|pull|rebase|reset|merge)(\s|$)", re.I),
    re.compile(r"(^|\s)gh\s+workflow\s+run(\s|$)", re.I),
    re.compile(r"(^|\s)gh\s+api\b.*\bdispatches\b", re.I),
    re.compile(r"run_chatgpt_daily_report_entrypoint\.py", re.I),
    re.compile(r"move_daily_reports_after_verified_copy\.py", re.I),
)
FORBIDDEN_OFFICIAL_ROOTS = (
    "chatgpt_side_outputs_official",
    "published_reports",
)


class ReplayCheckpointError(RuntimeError):
    """A fail-closed replay checkpoint contract violation."""


def _canonical_json_bytes(value: object) -> bytes:
    return (
        json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":")) + "\n"
    ).encode("utf-8")


def sha256_bytes(value: bytes) -> str:
    return hashlib.sha256(value).hexdigest()


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def _require_sha(value: str, label: str) -> str:
    normalized = str(value).strip().lower()
    if not re.fullmatch(r"[0-9a-f]{40}", normalized):
        raise ReplayCheckpointError(f"{label} must be an exact 40-character Git SHA")
    return normalized


def _normalize_relative_path(value: str | Path) -> str:
    raw = str(value).replace("\\", "/")
    path = PurePosixPath(raw)
    if (
        not raw
        or path.is_absolute()
        or any(part in {"", ".", ".."} for part in path.parts)
    ):
        raise ReplayCheckpointError(
            f"checkpoint path must be a normalized relative path: {value}"
        )
    if path.parts[0] == ".git":
        raise ReplayCheckpointError("checkpoint path cannot include .git")
    return path.as_posix()


def _run_git(
    repo_root: Path, *args: str, allow_missing: bool = False
) -> bytes | None:
    result = subprocess.run(
        ["git", *args],
        cwd=repo_root,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
    )
    if result.returncode == 0:
        return result.stdout
    if allow_missing:
        return None
    raise ReplayCheckpointError(
        f"git {' '.join(args)} failed with exit={result.returncode}: "
        f"{result.stderr.decode('utf-8', errors='replace').strip()}"
    )


def _baseline_entries(
    repo_root: Path,
    source_sha: str,
    relative_paths: Sequence[str],
) -> dict[str, dict[str, object]]:
    specifications = [
        f"{source_sha}:{relative}" for relative in relative_paths
    ]
    result = subprocess.run(
        ["git", "cat-file", "--batch"],
        cwd=repo_root,
        input=("\n".join(specifications) + "\n").encode("utf-8"),
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
    )
    if result.returncode != 0:
        raise ReplayCheckpointError(
            "git cat-file --batch failed: "
            + result.stderr.decode(
                "utf-8", errors="replace"
            ).strip()
        )
    payload = result.stdout
    cursor = 0
    entries: dict[str, dict[str, object]] = {}
    for relative in relative_paths:
        newline = payload.find(b"\n", cursor)
        if newline < 0:
            raise ReplayCheckpointError(
                "git cat-file baseline response is truncated"
            )
        header = payload[cursor:newline].decode(
            "utf-8", errors="replace"
        )
        cursor = newline + 1
        if header.endswith(" missing"):
            entries[relative] = {
                "exists": False,
                "bytes": 0,
                "sha256": None,
            }
            continue
        parts = header.split()
        if len(parts) != 3 or parts[1] != "blob":
            raise ReplayCheckpointError(
                f"unexpected Git baseline object for {relative}: "
                f"{header}"
            )
        try:
            byte_count = int(parts[2])
        except ValueError as error:
            raise ReplayCheckpointError(
                f"invalid Git baseline byte count for {relative}"
            ) from error
        end = cursor + byte_count
        if end >= len(payload) or payload[end : end + 1] != b"\n":
            raise ReplayCheckpointError(
                f"Git baseline payload is truncated for {relative}"
            )
        blob = payload[cursor:end]
        cursor = end + 1
        entries[relative] = {
            "exists": True,
            "bytes": byte_count,
            "sha256": sha256_bytes(blob),
        }
    if cursor != len(payload):
        raise ReplayCheckpointError(
            "git cat-file baseline response has trailing bytes"
        )
    return entries


def load_source_identities(path: Path) -> list[dict[str, str]]:
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as error:
        raise ReplayCheckpointError(
            f"cannot read source identity manifest {path}: {error}"
        ) from error
    identities = payload.get("sources") if isinstance(payload, dict) else None
    if not isinstance(identities, list) or not identities:
        raise ReplayCheckpointError(
            "source identity manifest must contain a non-empty sources list"
        )
    normalized: list[dict[str, str]] = []
    categories: set[str] = set()
    for index, item in enumerate(identities):
        if not isinstance(item, dict):
            raise ReplayCheckpointError(
                f"source identity row {index} must be an object"
            )
        required = (
            "category",
            "identity",
            "source_url",
            "artifact_path",
            "bytes",
            "sha256",
        )
        missing = [
            field for field in required if not str(item.get(field, "")).strip()
        ]
        if missing:
            raise ReplayCheckpointError(
                f"source identity row {index} missing fields: {missing}"
            )
        category = str(item["category"]).strip()
        digest = str(item["sha256"]).strip().lower()
        if not re.fullmatch(r"[0-9a-f]{64}", digest):
            raise ReplayCheckpointError(
                f"source identity row {index} has invalid sha256"
            )
        try:
            byte_count = int(item["bytes"])
        except (TypeError, ValueError) as error:
            raise ReplayCheckpointError(
                f"source identity row {index} has invalid bytes"
            ) from error
        if byte_count < 0:
            raise ReplayCheckpointError(
                f"source identity row {index} has negative bytes"
            )
        artifact_path = _normalize_relative_path(str(item["artifact_path"]))
        normalized.append(
            {
                "category": category,
                "identity": str(item["identity"]).strip(),
                "source_url": str(item["source_url"]).strip(),
                "artifact_path": artifact_path,
                "bytes": byte_count,
                "sha256": digest,
            }
        )
        categories.add(category)
    missing_categories = sorted(REQUIRED_SOURCE_CATEGORIES - categories)
    if missing_categories:
        raise ReplayCheckpointError(
            f"source identity manifest missing categories: {missing_categories}"
        )
    return sorted(
        normalized, key=lambda row: (row["category"], row["artifact_path"])
    )


def load_source_revision_manifest(path: Path) -> dict[str, object]:
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as error:
        raise ReplayCheckpointError(
            f"cannot read source revision manifest {path}: {error}"
        ) from error
    if not isinstance(payload, dict):
        raise ReplayCheckpointError(
            "source revision manifest must contain a JSON object"
        )
    if not re.fullmatch(
        r"20\d{6}", str(payload.get("replay_date") or "")
    ):
        raise ReplayCheckpointError(
            "source revision manifest replay_date is invalid"
        )
    if payload.get("revision_kind") not in {
        "authoritative_historical_revision",
        "live_production_capture",
    }:
        raise ReplayCheckpointError(
            "source revision manifest revision_kind is invalid"
        )
    _require_sha(
        str(payload.get("source_sha") or ""),
        "source revision source_sha",
    )
    if payload.get("byte_parity_with_run_31174813266") is not False:
        raise ReplayCheckpointError(
            "source revision manifest must reject old-run byte parity"
        )
    return payload


def discover_changed_paths(
    repo_root: Path, allowed_prefixes: Sequence[str]
) -> list[str]:
    prefixes = tuple(
        _normalize_relative_path(value).rstrip("/") + "/"
        for value in allowed_prefixes
    )
    raw = (
        _run_git(
            repo_root,
            "status",
            "--porcelain=v1",
            "-z",
            "--untracked-files=all",
        )
        or b""
    )
    paths: list[str] = []
    records = raw.decode("utf-8", errors="surrogateescape").split("\0")
    index = 0
    while index < len(records):
        record = records[index]
        index += 1
        if not record:
            continue
        status = record[:2]
        candidate = record[3:]
        if status[0] in "RC" and index < len(records):
            candidate = records[index]
            index += 1
        relative = _normalize_relative_path(candidate)
        if not any(
            relative == prefix[:-1] or relative.startswith(prefix)
            for prefix in prefixes
        ):
            raise ReplayCheckpointError(
                f"changed path is outside checkpoint allowlist prefixes: {relative}"
            )
        paths.append(relative)
    return sorted(set(paths))


def create_checkpoint(
    *,
    repo_root: Path,
    bundle_dir: Path,
    paths: Iterable[str | Path],
    replay_date: str,
    source_sha: str,
    producer_run_id: str,
    producer_head_sha: str,
    source_identity_manifest: Path,
    checkpoint_kind: str,
    producer_steps: Sequence[str],
    locked_replay_date: str | None = REPLAY_DATE,
    capture_context: str = "validation_canary",
) -> dict[str, object]:
    repo_root = repo_root.resolve()
    if not re.fullmatch(r"20\d{6}", replay_date):
        raise ReplayCheckpointError(
            f"replay_date must be YYYYMMDD; observed={replay_date}"
        )
    if locked_replay_date is not None and replay_date != locked_replay_date:
        raise ReplayCheckpointError(
            f"replay_date must equal {locked_replay_date}; "
            f"observed={replay_date}"
        )
    source_sha = _require_sha(source_sha, "source_sha")
    producer_head_sha = _require_sha(
        producer_head_sha, "producer_head_sha"
    )
    if producer_head_sha != source_sha:
        raise ReplayCheckpointError("producer_head_sha must equal source_sha")
    if not str(producer_run_id).isdigit():
        raise ReplayCheckpointError("producer_run_id must be numeric")
    if checkpoint_kind not in {"pre_step41", "post_validation"}:
        raise ReplayCheckpointError(
            f"unsupported checkpoint_kind={checkpoint_kind}"
        )
    if not producer_steps:
        raise ReplayCheckpointError("producer_steps cannot be empty")
    if capture_context not in {
        "validation_canary",
        "validation_replay",
        "production_pre_step41",
    }:
        raise ReplayCheckpointError(
            f"unsupported capture_context={capture_context}"
        )

    relative_paths = sorted(
        {_normalize_relative_path(path) for path in paths}
    )
    if not relative_paths:
        raise ReplayCheckpointError(
            "checkpoint path allowlist cannot be empty"
        )
    source_revision = load_source_revision_manifest(
        source_identity_manifest
    )
    if source_revision.get("replay_date") != replay_date:
        raise ReplayCheckpointError(
            "source revision and checkpoint dates differ"
        )
    if source_revision.get("source_sha") != source_sha:
        raise ReplayCheckpointError(
            "source revision and checkpoint source SHAs differ"
        )
    source_identities = load_source_identities(
        source_identity_manifest
    )
    identity_paths = {
        row["artifact_path"] for row in source_identities
    }
    missing_identity_paths = sorted(
        identity_paths - set(relative_paths)
    )
    if missing_identity_paths:
        raise ReplayCheckpointError(
            "source identity artifacts are not in checkpoint path "
            f"allowlist: {missing_identity_paths}"
        )

    if bundle_dir.exists():
        raise ReplayCheckpointError(
            f"checkpoint bundle destination already exists: {bundle_dir}"
        )
    payload_root = bundle_dir / PAYLOAD_DIR
    payload_root.mkdir(parents=True)
    source_revision_bytes = _canonical_json_bytes(source_revision)
    (bundle_dir / "source_revision_manifest.json").write_bytes(
        source_revision_bytes
    )
    baseline_entries = _baseline_entries(
        repo_root, source_sha, relative_paths
    )
    entries: list[dict[str, object]] = []
    for relative in relative_paths:
        source = repo_root / Path(relative)
        if not source.is_file() or source.is_symlink():
            raise ReplayCheckpointError(
                "checkpoint path must be an existing regular file: "
                f"{relative}"
            )
        destination = payload_root / Path(relative)
        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(source, destination)
        entries.append(
            {
                "path": relative,
                "bytes": destination.stat().st_size,
                "sha256": sha256_file(destination),
                "baseline": baseline_entries[relative],
            }
        )

    entries_by_path = {row["path"]: row for row in entries}
    for identity in source_identities:
        entry = entries_by_path[identity["artifact_path"]]
        if entry["sha256"] != identity["sha256"]:
            raise ReplayCheckpointError(
                f"source identity SHA mismatch for "
                f"{identity['artifact_path']}: "
                f"manifest={identity['sha256']} "
                f"payload={entry['sha256']}"
            )
        if entry["bytes"] != identity["bytes"]:
            raise ReplayCheckpointError(
                f"source identity byte count mismatch for "
                f"{identity['artifact_path']}: "
                f"manifest={identity['bytes']} "
                f"payload={entry['bytes']}"
            )

    manifest: dict[str, object] = {
        "schema_version": SCHEMA_VERSION,
        "checkpoint_kind": checkpoint_kind,
        "replay_date": replay_date,
        "source_sha": source_sha,
        "producer_run_id": str(producer_run_id),
        "producer_head_sha": producer_head_sha,
        "producer_steps": list(producer_steps),
        "capture_context": capture_context,
        "revision_kind": source_revision["revision_kind"],
        "authoritative_historical_revision": (
            source_revision["revision_kind"]
            == "authoritative_historical_revision"
        ),
        "byte_parity_with_run_31174813266": False,
        "source_revision_manifest": {
            "path": "source_revision_manifest.json",
            "bytes": len(source_revision_bytes),
            "sha256": sha256_bytes(source_revision_bytes),
        },
        "source_identities": source_identities,
        "path_allowlist": relative_paths,
        "files": entries,
        "safety": {
            "replay_consumer_validation_only": True,
            "production_not_run": (
                capture_context != "production_pre_step41"
            ),
            "official_pdf_published": False,
            "repo_artifacts_pushed_by_replay": False,
            "mutable_source_fallback_allowed": False,
        },
    }
    checkpoint_source_sha = source_revision.get("checkpoint_source_sha")
    replay_source_sha = source_revision.get("replay_source_sha")
    revision_transition = source_revision.get("revision_transition")
    if any(
        value is not None
        for value in (
            checkpoint_source_sha,
            replay_source_sha,
            revision_transition,
        )
    ):
        checkpoint_source_sha = _require_sha(
            str(checkpoint_source_sha or ""),
            "checkpoint_source_sha",
        )
        replay_source_sha = _require_sha(
            str(replay_source_sha or ""),
            "replay_source_sha",
        )
        if replay_source_sha != source_sha:
            raise ReplayCheckpointError(
                "replay source SHA must equal checkpoint producer source SHA"
            )
        if not isinstance(revision_transition, dict) or (
            revision_transition.get("checkpoint_source_sha")
            != checkpoint_source_sha
            or revision_transition.get("replay_source_sha")
            != replay_source_sha
        ):
            raise ReplayCheckpointError(
                "checkpoint revision transition metadata mismatch"
            )
        manifest["checkpoint_source_sha"] = checkpoint_source_sha
        manifest["replay_source_sha"] = replay_source_sha
        manifest["revision_transition"] = revision_transition
    manifest_bytes = _canonical_json_bytes(manifest)
    (bundle_dir / CHECKPOINT_MANIFEST).write_bytes(manifest_bytes)
    (bundle_dir / CHECKPOINT_MANIFEST_SHA).write_text(
        sha256_bytes(manifest_bytes) + "\n", encoding="ascii"
    )
    return manifest


def verify_checkpoint(
    *,
    bundle_dir: Path,
    expected_replay_date: str = REPLAY_DATE,
    expected_source_sha: str | None = None,
    expected_run_id: str | None = None,
    expected_kind: str | None = None,
    expected_capture_context: str | None = None,
) -> dict[str, object]:
    manifest_path = bundle_dir / CHECKPOINT_MANIFEST
    digest_path = bundle_dir / CHECKPOINT_MANIFEST_SHA
    if not manifest_path.is_file() or not digest_path.is_file():
        raise ReplayCheckpointError(
            "checkpoint manifest or digest is missing"
        )
    manifest_bytes = manifest_path.read_bytes()
    expected_digest = (
        digest_path.read_text(encoding="ascii").strip().lower()
    )
    if (
        not re.fullmatch(r"[0-9a-f]{64}", expected_digest)
        or sha256_bytes(manifest_bytes) != expected_digest
    ):
        raise ReplayCheckpointError(
            "checkpoint manifest SHA-256 mismatch"
        )
    try:
        manifest = json.loads(manifest_bytes)
    except json.JSONDecodeError as error:
        raise ReplayCheckpointError(
            f"checkpoint manifest is not valid JSON: {error}"
        ) from error
    if manifest.get("schema_version") != SCHEMA_VERSION:
        raise ReplayCheckpointError(
            "checkpoint schema version mismatch"
        )
    if manifest.get("replay_date") != expected_replay_date:
        raise ReplayCheckpointError("checkpoint replay date mismatch")
    if expected_source_sha and manifest.get(
        "source_sha"
    ) != _require_sha(expected_source_sha, "expected_source_sha"):
        raise ReplayCheckpointError("checkpoint source SHA mismatch")
    if expected_run_id and str(
        manifest.get("producer_run_id")
    ) != str(expected_run_id):
        raise ReplayCheckpointError(
            "checkpoint producer run id mismatch"
        )
    if (
        expected_kind
        and manifest.get("checkpoint_kind") != expected_kind
    ):
        raise ReplayCheckpointError("checkpoint kind mismatch")
    if (
        expected_capture_context
        and manifest.get("capture_context")
        != expected_capture_context
    ):
        raise ReplayCheckpointError(
            "checkpoint capture context mismatch"
        )
    if manifest.get("producer_head_sha") != manifest.get("source_sha"):
        raise ReplayCheckpointError(
            "checkpoint producer head/source SHA mismatch"
        )
    if any(
        key in manifest
        for key in (
            "checkpoint_source_sha",
            "replay_source_sha",
            "revision_transition",
        )
    ):
        checkpoint_source_sha = _require_sha(
            str(manifest.get("checkpoint_source_sha") or ""),
            "checkpoint_source_sha",
        )
        replay_source_sha = _require_sha(
            str(manifest.get("replay_source_sha") or ""),
            "replay_source_sha",
        )
        transition = manifest.get("revision_transition")
        if (
            replay_source_sha != manifest.get("source_sha")
            or not isinstance(transition, dict)
            or transition.get("checkpoint_source_sha")
            != checkpoint_source_sha
            or transition.get("replay_source_sha") != replay_source_sha
        ):
            raise ReplayCheckpointError(
                "checkpoint revision transition metadata mismatch"
            )
    revision_kind = manifest.get("revision_kind")
    if revision_kind not in {
        "authoritative_historical_revision",
        "live_production_capture",
    }:
        raise ReplayCheckpointError(
            "checkpoint revision kind is invalid"
        )
    if manifest.get("authoritative_historical_revision") is not (
        revision_kind == "authoritative_historical_revision"
    ):
        raise ReplayCheckpointError(
            "checkpoint historical revision flag mismatch"
        )
    if manifest.get("byte_parity_with_run_31174813266") is not False:
        raise ReplayCheckpointError(
            "checkpoint falsely claims old-run byte parity"
        )
    expected_safety = {
        "replay_consumer_validation_only": True,
        "production_not_run": (
            manifest.get("capture_context")
            != "production_pre_step41"
        ),
        "official_pdf_published": False,
        "repo_artifacts_pushed_by_replay": False,
        "mutable_source_fallback_allowed": False,
    }
    if manifest.get("safety") != expected_safety:
        raise ReplayCheckpointError(
            "checkpoint safety contract mismatch"
        )

    allowlist = manifest.get("path_allowlist")
    files = manifest.get("files")
    if not isinstance(allowlist, list) or not isinstance(files, list):
        raise ReplayCheckpointError(
            "checkpoint file contract is malformed"
        )
    if allowlist != sorted(set(allowlist)):
        raise ReplayCheckpointError(
            "checkpoint path allowlist must be sorted and unique"
        )
    entries = {
        row.get("path"): row
        for row in files
        if isinstance(row, dict)
    }
    if set(entries) != set(allowlist) or len(entries) != len(files):
        raise ReplayCheckpointError(
            "checkpoint file set does not match path allowlist"
        )
    payload_root = bundle_dir / PAYLOAD_DIR
    actual_paths = (
        sorted(
            path.relative_to(payload_root).as_posix()
            for path in payload_root.rglob("*")
            if path.is_file()
        )
        if payload_root.is_dir()
        else []
    )
    if actual_paths != allowlist:
        raise ReplayCheckpointError(
            "checkpoint payload path set mismatch: "
            f"actual={actual_paths}"
        )
    for relative, entry in entries.items():
        path = payload_root / Path(str(relative))
        if path.stat().st_size != entry.get("bytes"):
            raise ReplayCheckpointError(
                f"checkpoint byte count mismatch: {relative}"
            )
        if sha256_file(path) != entry.get("sha256"):
            raise ReplayCheckpointError(
                f"checkpoint SHA-256 mismatch: {relative}"
            )
        baseline = entry.get("baseline")
        if not isinstance(baseline, dict):
            raise ReplayCheckpointError(
                f"checkpoint baseline metadata missing: {relative}"
            )
        if baseline.get("exists") is True:
            if (
                not isinstance(baseline.get("bytes"), int)
                or baseline["bytes"] < 0
                or not re.fullmatch(
                    r"[0-9a-f]{64}",
                    str(baseline.get("sha256") or ""),
                )
            ):
                raise ReplayCheckpointError(
                    f"checkpoint baseline metadata invalid: {relative}"
                )
        elif baseline != {
            "exists": False,
            "bytes": 0,
            "sha256": None,
        }:
            raise ReplayCheckpointError(
                f"checkpoint absent-baseline metadata invalid: {relative}"
            )

    identities = manifest.get("source_identities")
    if not isinstance(identities, list):
        raise ReplayCheckpointError(
            "checkpoint source identities are missing"
        )
    categories = {
        row.get("category")
        for row in identities
        if isinstance(row, dict)
    }
    if not REQUIRED_SOURCE_CATEGORIES.issubset(categories):
        raise ReplayCheckpointError(
            "checkpoint source identity categories are incomplete"
        )
    for identity in identities:
        relative = identity.get("artifact_path")
        if (
            relative not in entries
            or identity.get("sha256")
            != entries[relative].get("sha256")
            or identity.get("bytes")
            != entries[relative].get("bytes")
        ):
            raise ReplayCheckpointError(
                f"checkpoint source identity mismatch: {relative}"
            )

    revision_entry = manifest.get("source_revision_manifest")
    revision_path = bundle_dir / "source_revision_manifest.json"
    if (
        not isinstance(revision_entry, dict)
        or not revision_path.is_file()
        or revision_path.stat().st_size
        != revision_entry.get("bytes")
        or sha256_file(revision_path)
        != revision_entry.get("sha256")
    ):
        raise ReplayCheckpointError(
            "checkpoint source revision manifest mismatch"
        )
    source_revision = load_source_revision_manifest(revision_path)
    if (
        source_revision.get("revision_kind") != revision_kind
        or source_revision.get("replay_date")
        != manifest.get("replay_date")
        or source_revision.get("source_sha")
        != manifest.get("source_sha")
        or source_revision.get("checkpoint_source_sha")
        != manifest.get("checkpoint_source_sha")
        or source_revision.get("replay_source_sha")
        != manifest.get("replay_source_sha")
        or source_revision.get("revision_transition")
        != manifest.get("revision_transition")
        or load_source_identities(revision_path) != identities
    ):
        raise ReplayCheckpointError(
            "checkpoint source revision metadata mismatch"
        )
    return manifest


def restore_checkpoint(
    *,
    bundle_dir: Path,
    destination_root: Path,
    expected_source_sha: str,
    expected_destination_source_sha: str | None = None,
    expected_run_id: str,
    expected_kind: str,
    expected_capture_context: str | None = None,
) -> dict[str, object]:
    manifest = verify_checkpoint(
        bundle_dir=bundle_dir,
        expected_source_sha=expected_source_sha,
        expected_run_id=expected_run_id,
        expected_kind=expected_kind,
        expected_capture_context=expected_capture_context,
    )
    destination_root = destination_root.resolve()
    source_sha = str(manifest["source_sha"])
    destination_source_sha = _require_sha(
        expected_destination_source_sha or source_sha,
        "expected_destination_source_sha",
    )
    head_result = subprocess.run(
        ["git", "rev-parse", "HEAD"],
        cwd=destination_root,
        check=False,
        capture_output=True,
        text=True,
    )
    if head_result.returncode != 0:
        raise ReplayCheckpointError(
            "cannot resolve restore destination HEAD"
        )
    destination_head = head_result.stdout.strip()
    if destination_head != destination_source_sha:
        raise ReplayCheckpointError(
            "restore destination HEAD/source SHA mismatch"
        )
    status_result = subprocess.run(
        ["git", "status", "--porcelain=v1", "--untracked-files=all"],
        cwd=destination_root,
        check=False,
        capture_output=True,
        text=True,
    )
    if status_result.returncode != 0:
        raise ReplayCheckpointError(
            "cannot resolve restore destination status"
        )
    destination_status = status_result.stdout
    if destination_status.strip():
        raise ReplayCheckpointError(
            "restore collision: destination checkout is not clean"
        )
    relative_paths = [str(entry["path"]) for entry in manifest["files"]]
    destination_entries = _baseline_entries(
        destination_root, destination_source_sha, relative_paths
    )
    for start in range(0, len(relative_paths), 100):
        chunk = relative_paths[start : start + 100]
        parity = subprocess.run(
            [
                "git",
                "diff",
                "--quiet",
                destination_source_sha,
                "--",
                *chunk,
            ],
            cwd=destination_root,
            check=False,
        )
        if parity.returncode == 1:
            raise ReplayCheckpointError(
                "restore collision against destination source SHA in "
                f"checkpoint path chunk: {chunk[:3]}"
            )
        if parity.returncode != 0:
            raise ReplayCheckpointError(
                "cannot verify restore collision against destination "
                "source SHA; "
                f"git diff exit={parity.returncode}"
            )
    for entry in manifest["files"]:
        relative = str(entry["path"])
        destination = destination_root / Path(relative)
        destination_baseline = destination_entries[relative]
        if bool(destination_baseline["exists"]):
            if not destination.is_file():
                raise ReplayCheckpointError(
                    f"restore destination baseline file is missing: {relative}"
                )
        elif destination.exists():
            raise ReplayCheckpointError(
                "restore collision on untracked checkpoint path: "
                f"{relative}"
            )
    for entry in manifest["files"]:
        relative = str(entry["path"])
        source = bundle_dir / PAYLOAD_DIR / Path(relative)
        destination = destination_root / Path(relative)
        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(source, destination)
    return manifest


def assert_validation_only_command(
    command: str | Sequence[str],
) -> None:
    rendered = (
        command
        if isinstance(command, str)
        else shlex.join([str(part) for part in command])
    )
    for pattern in FORBIDDEN_COMMAND_PATTERNS:
        if pattern.search(rendered):
            raise ReplayCheckpointError(
                f"validation-only replay forbids command: {rendered}"
            )


def assert_isolated_output_path(
    path: Path, sandbox_root: Path
) -> None:
    resolved = path.resolve()
    sandbox = sandbox_root.resolve()
    try:
        relative = resolved.relative_to(sandbox).as_posix()
    except ValueError as error:
        raise ReplayCheckpointError(
            f"validation output must stay inside sandbox: {resolved}"
        ) from error
    if any(
        part in FORBIDDEN_OFFICIAL_ROOTS
        for part in PurePosixPath(relative).parts
    ):
        raise ReplayCheckpointError(
            f"validation output uses forbidden official root: {relative}"
        )


def _parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(
        dest="command", required=True
    )
    capture = subparsers.add_parser("capture")
    capture.add_argument("--repo-root", type=Path, required=True)
    capture.add_argument("--bundle-dir", type=Path, required=True)
    capture.add_argument("--replay-date", required=True)
    capture.add_argument("--source-sha", required=True)
    capture.add_argument("--producer-run-id", required=True)
    capture.add_argument("--producer-head-sha", required=True)
    capture.add_argument(
        "--source-identity-manifest", type=Path, required=True
    )
    capture.add_argument(
        "--checkpoint-kind",
        choices=("pre_step41", "post_validation"),
        required=True,
    )
    capture.add_argument(
        "--producer-step", action="append", required=True
    )
    capture.add_argument("--path", action="append", default=[])
    capture.add_argument(
        "--discover-prefix", action="append", default=[]
    )
    verify = subparsers.add_parser("verify")
    verify.add_argument("--bundle-dir", type=Path, required=True)
    verify.add_argument("--expected-source-sha")
    verify.add_argument("--expected-run-id")
    verify.add_argument(
        "--expected-kind",
        choices=("pre_step41", "post_validation"),
    )
    restore = subparsers.add_parser("restore")
    restore.add_argument("--bundle-dir", type=Path, required=True)
    restore.add_argument(
        "--destination-root", type=Path, required=True
    )
    restore.add_argument("--expected-source-sha", required=True)
    restore.add_argument("--expected-run-id", required=True)
    restore.add_argument(
        "--expected-kind",
        choices=("pre_step41", "post_validation"),
        required=True,
    )
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    args = _parser().parse_args(argv)
    if args.command == "capture":
        paths = list(args.path)
        if args.discover_prefix:
            paths.extend(
                discover_changed_paths(
                    args.repo_root, args.discover_prefix
                )
            )
        manifest = create_checkpoint(
            repo_root=args.repo_root,
            bundle_dir=args.bundle_dir,
            paths=paths,
            replay_date=args.replay_date,
            source_sha=args.source_sha,
            producer_run_id=args.producer_run_id,
            producer_head_sha=args.producer_head_sha,
            source_identity_manifest=args.source_identity_manifest,
            checkpoint_kind=args.checkpoint_kind,
            producer_steps=args.producer_step,
        )
    elif args.command == "verify":
        manifest = verify_checkpoint(
            bundle_dir=args.bundle_dir,
            expected_source_sha=args.expected_source_sha,
            expected_run_id=args.expected_run_id,
            expected_kind=args.expected_kind,
        )
    else:
        manifest = restore_checkpoint(
            bundle_dir=args.bundle_dir,
            destination_root=args.destination_root,
            expected_source_sha=args.expected_source_sha,
            expected_run_id=args.expected_run_id,
            expected_kind=args.expected_kind,
        )
    print(
        json.dumps(
            {
                "status": "ok",
                "manifest_sha256": sha256_file(
                    args.bundle_dir / CHECKPOINT_MANIFEST
                ),
                "files": len(manifest["files"]),
            },
            sort_keys=True,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
