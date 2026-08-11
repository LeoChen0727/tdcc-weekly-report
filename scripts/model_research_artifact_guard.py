from __future__ import annotations

import csv
import fnmatch
import hashlib
import subprocess
from contextlib import contextmanager
from dataclasses import dataclass
from pathlib import Path
from typing import Iterator


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_REGISTRY = ROOT / "config/model_research_artifact_ownership.csv"
DEFAULT_SENTINEL_REGISTRY = ROOT / "config/model_research_protected_sentinels.csv"


@dataclass(frozen=True)
class ArtifactOwnershipRule:
    owner_model_id: str
    producer: str
    artifact_glob: str
    artifact_class: str
    change_policy: str
    formal_evidence_status: str


@dataclass(frozen=True)
class ProtectedSentinel:
    sentinel_id: str
    artifact_glob: str
    owner: str
    sentinel_class: str
    required: bool


def _normal_path(value: str | Path) -> str:
    return Path(value).as_posix().lstrip("./")


def load_ownership_rules(path: Path = DEFAULT_REGISTRY) -> list[ArtifactOwnershipRule]:
    if not path.exists():
        raise RuntimeError(f"missing model research artifact ownership registry: {path}")
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        rows = list(csv.DictReader(handle))
    required = {
        "owner_model_id",
        "producer",
        "artifact_glob",
        "artifact_class",
        "change_policy",
        "formal_evidence_status",
    }
    if not rows or not required.issubset(rows[0]):
        raise RuntimeError("model research artifact ownership registry schema is incomplete")
    return [
        ArtifactOwnershipRule(
            owner_model_id=row["owner_model_id"].strip(),
            producer=_normal_path(row["producer"].strip()),
            artifact_glob=_normal_path(row["artifact_glob"].strip()),
            artifact_class=row["artifact_class"].strip(),
            change_policy=row["change_policy"].strip(),
            formal_evidence_status=row["formal_evidence_status"].strip(),
        )
        for row in rows
    ]


def load_protected_sentinels(path: Path = DEFAULT_SENTINEL_REGISTRY) -> list[ProtectedSentinel]:
    if not path.exists():
        raise RuntimeError(f"missing protected sentinel registry: {path}")
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        rows = list(csv.DictReader(handle))
    required = {"sentinel_id", "artifact_glob", "owner", "sentinel_class", "required"}
    if not rows or not required.issubset(rows[0]):
        raise RuntimeError("protected sentinel registry schema is incomplete")
    return [
        ProtectedSentinel(
            sentinel_id=row["sentinel_id"].strip(),
            artifact_glob=_normal_path(row["artifact_glob"].strip()),
            owner=row["owner"].strip(),
            sentinel_class=row["sentinel_class"].strip(),
            required=row["required"].strip().lower() in {"true", "1", "yes"},
        )
        for row in rows
    ]


def ownership_for_path(path: str | Path, rules: list[ArtifactOwnershipRule]) -> list[ArtifactOwnershipRule]:
    normalized = _normal_path(path)
    return [rule for rule in rules if fnmatch.fnmatchcase(normalized, rule.artifact_glob)]


def validate_changed_paths(
    model_id: str,
    producer: str,
    changed_paths: list[str],
    rules: list[ArtifactOwnershipRule],
) -> list[str]:
    errors: list[str] = []
    normalized_producer = _normal_path(producer)
    for path in sorted({_normal_path(item) for item in changed_paths}):
        matches = ownership_for_path(path, rules)
        if not matches:
            errors.append(f"unregistered artifact change: {path}")
            continue
        if len(matches) > 1:
            owners = ",".join(sorted({match.owner_model_id for match in matches}))
            errors.append(f"ambiguous artifact ownership: {path}; owners={owners}")
            continue
        rule = matches[0]
        if rule.owner_model_id != model_id:
            errors.append(
                f"cross-model artifact change: selected_model={model_id}; "
                f"artifact_owner={rule.owner_model_id}; path={path}"
            )
            continue
        if rule.producer != normalized_producer:
            errors.append(
                f"wrong producer for model-owned artifact: path={path}; "
                f"expected={rule.producer}; actual={normalized_producer}"
            )
            continue
        if rule.change_policy != "model_owned_write":
            errors.append(f"artifact change policy forbids model run: path={path}; policy={rule.change_policy}")
    return errors


def validate_stage_changed_paths(
    changed_paths: list[str],
    allowed_changed_path_globs: tuple[str, ...],
) -> list[str]:
    """Restrict one model-owned stage to its declared artifact subset."""

    allowed_globs = tuple(_normal_path(pattern) for pattern in allowed_changed_path_globs)
    errors: list[str] = []
    for path in sorted({_normal_path(item) for item in changed_paths}):
        if not any(fnmatch.fnmatchcase(path, pattern) for pattern in allowed_globs):
            errors.append(f"stage-specific artifact allowlist violation: {path}")
    return errors


def _git_status_paths(root: Path) -> set[str]:
    result = subprocess.run(
        ["git", "status", "--porcelain=v1", "--untracked-files=all"],
        cwd=root,
        check=True,
        capture_output=True,
        text=True,
        encoding="utf-8",
    )
    paths: set[str] = set()
    for raw_line in result.stdout.splitlines():
        if len(raw_line) < 4:
            continue
        path = raw_line[3:].strip()
        if " -> " in path:
            path = path.split(" -> ", 1)[1]
        paths.add(_normal_path(path.strip('"')))
    return paths


def _file_sha256(root: Path, relative_path: str) -> str:
    path = root / relative_path
    if not path.is_file():
        return "__missing__"
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def protected_sentinel_snapshot(
    root: Path,
    sentinels: list[ProtectedSentinel],
) -> tuple[dict[str, str], list[str]]:
    snapshot: dict[str, str] = {}
    errors: list[str] = []
    for sentinel in sentinels:
        matches = sorted(path for path in root.glob(sentinel.artifact_glob) if path.is_file())
        if sentinel.required and not matches:
            errors.append(
                f"required protected sentinel has no files: "
                f"sentinel_id={sentinel.sentinel_id}; glob={sentinel.artifact_glob}"
            )
        for path in matches:
            relative = path.relative_to(root).as_posix()
            if relative in snapshot:
                errors.append(f"protected sentinel path matched more than once: {relative}")
                continue
            snapshot[relative] = _file_sha256(root, relative)
    return snapshot, errors


def compare_protected_sentinel_snapshots(
    before: dict[str, str],
    after: dict[str, str],
) -> list[str]:
    errors: list[str] = []
    for path in sorted(set(before) | set(after)):
        if path not in before:
            errors.append(f"protected sentinel added during model research: {path}")
        elif path not in after:
            errors.append(f"protected sentinel deleted during model research: {path}")
        elif before[path] != after[path]:
            errors.append(f"protected sentinel hash drift during model research: {path}")
    return errors


def protected_sentinel_aggregate_sha256(snapshot: dict[str, str]) -> str:
    digest = hashlib.sha256()
    for path, file_hash in sorted(snapshot.items()):
        digest.update(path.encode("utf-8"))
        digest.update(b"\0")
        digest.update(file_hash.encode("ascii"))
        digest.update(b"\n")
    return digest.hexdigest()


def _dirty_snapshot(root: Path) -> dict[str, str]:
    return {path: _file_sha256(root, path) for path in _git_status_paths(root)}


def changed_during_run(root: Path, before: dict[str, str]) -> list[str]:
    after_paths = _git_status_paths(root)
    candidates = set(before) | after_paths
    changed: list[str] = []
    for path in candidates:
        after_hash = _file_sha256(root, path)
        before_hash = before.get(path, "__clean_before_run__")
        if before_hash == "__clean_before_run__":
            changed.append(path)
        elif before_hash != after_hash:
            changed.append(path)
    return sorted(changed)


@contextmanager
def model_owned_artifact_guard(
    model_id: str,
    producer: str,
    *,
    root: Path = ROOT,
    registry_path: Path = DEFAULT_REGISTRY,
    sentinel_registry_path: Path = DEFAULT_SENTINEL_REGISTRY,
    allowed_changed_path_globs: tuple[str, ...] | None = None,
) -> Iterator[None]:
    rules = load_ownership_rules(registry_path)
    sentinels = load_protected_sentinels(sentinel_registry_path)
    before = _dirty_snapshot(root)
    sentinel_before, sentinel_before_errors = protected_sentinel_snapshot(root, sentinels)
    sentinel_before_sha256 = protected_sentinel_aggregate_sha256(sentinel_before)
    if sentinel_before_errors:
        details = "\n".join(f"- {error}" for error in sentinel_before_errors)
        raise RuntimeError(f"protected sentinel preflight failed:\n{details}")
    try:
        yield
    finally:
        changed = changed_during_run(root, before)
        errors = validate_changed_paths(model_id, producer, changed, rules)
        if allowed_changed_path_globs is not None:
            errors.extend(
                validate_stage_changed_paths(changed, allowed_changed_path_globs)
            )
        sentinel_after, sentinel_after_errors = protected_sentinel_snapshot(root, sentinels)
        sentinel_after_sha256 = protected_sentinel_aggregate_sha256(sentinel_after)
        errors.extend(sentinel_after_errors)
        errors.extend(compare_protected_sentinel_snapshots(sentinel_before, sentinel_after))
        if errors:
            details = "\n".join(f"- {error}" for error in errors)
            raise RuntimeError(f"model-owned artifact guard failed:\n{details}")
        print(
            "model-owned artifact guard passed "
            f"model_id={model_id} producer={_normal_path(producer)} "
            f"changed_paths={len(changed)} protected_sentinels={len(sentinel_after)}"
        )
        print(f"protected_sentinel_before_sha256={sentinel_before_sha256}")
        print(f"protected_sentinel_after_sha256={sentinel_after_sha256}")
