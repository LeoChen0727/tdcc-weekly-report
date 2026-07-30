from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any

from build_event_catalyst_historical_recovery_manifest import (
    BLOCKED_STATUS,
    DEFAULT_EVIDENCE_CSV,
    INDEX_SCHEMA_VERSION,
    REQUIRED_FORBIDDEN_RECONSTRUCTION,
    ROOT,
    SCHEMA_VERSION,
    TARGET_DATES,
    read_evidence,
    split_values,
)


DEFAULT_INDEX = Path(
    "output/latest/event_catalyst_historical_recovery_latest.json"
)
DEFAULT_DOCS_JSON = Path(
    "docs/latest/event_catalyst_historical_recovery_latest.json"
)
DEFAULT_DOCS_MD = Path(
    "docs/latest/event_catalyst_historical_recovery_latest.md"
)
DEFAULT_LATEST_MD = Path(
    "output/latest/event_catalyst_historical_recovery_latest.md"
)


def sha256_file(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def read_json(path: Path) -> dict[str, Any]:
    try:
        value = json.loads(path.read_text(encoding="utf-8-sig"))
    except (OSError, json.JSONDecodeError):
        return {}
    return value if isinstance(value, dict) else {}


def validate_manifest(
    root: Path,
    *,
    manifest_path: Path,
    expected_sha256: str,
    evidence: dict[str, str],
) -> list[str]:
    errors: list[str] = []
    target_date = evidence["target_date"]
    if not manifest_path.is_file():
        return [f"missing event/catalyst recovery manifest: {manifest_path}"]
    if sha256_file(manifest_path) != expected_sha256:
        errors.append(f"manifest hash mismatch: {target_date}")
    manifest = read_json(manifest_path)

    expected_values = {
        "schema_version": SCHEMA_VERSION,
        "target_date": target_date,
        "status": BLOCKED_STATUS,
        "completion_state": BLOCKED_STATUS,
        "publication_status": "historical_event_catalyst_not_as_published",
        "as_published": False,
        "authoritative_history_artifact_present": False,
        "current_value_backfill_allowed": False,
        "historical_content_reconstructed": False,
        "runner_uncommitted_sources_irrecoverable": True,
        "failed_head_sha": evidence["failed_head_sha"],
        "failed_step": evidence["failed_step"],
        "failed_gate": evidence["failed_gate"],
        "commit_step_state": evidence["commit_step_state"],
        "runner_source_state": evidence["runner_source_state"],
        "blocker_reason": evidence["blocker_reason"],
    }
    for field, expected in expected_values.items():
        if manifest.get(field) != expected:
            errors.append(f"{target_date}: {field} mismatch")

    observed_runs = manifest.get("failed_runs") or []
    expected_runs = [
        {"run_id": run_id, "url": run_url}
        for run_id, run_url in zip(
            split_values(evidence["failed_run_ids"]),
            split_values(evidence["failed_run_urls"]),
            strict=True,
        )
    ]
    if observed_runs != expected_runs:
        errors.append(f"{target_date}: failed run evidence mismatch")

    required_prohibitions = {
        "do_not_reconstruct_historical_event_content",
        "do_not_infer_historical_catalyst_content",
        "do_not_retro_date_current_source_values",
    }
    if not required_prohibitions.issubset(set(manifest.get("prohibitions") or [])):
        errors.append(f"{target_date}: historical reconstruction prohibitions missing")

    effect = manifest.get("effect_policy") or {}
    required_effect = {
        "allowed_effect": "disclosure_only",
        "score_allowed": False,
        "ranking_allowed": False,
        "reason_text_allowed": False,
        "requires_human_review": True,
    }
    for field, expected in required_effect.items():
        if effect.get(field) != expected:
            errors.append(f"{target_date}: effect_policy.{field} mismatch")

    context = manifest.get("current_source_refresh_context") or {}
    if context.get("historical_backfill_effect_allowed") is not False:
        errors.append(f"{target_date}: current refresh context permits backfill")
    status_artifacts = context.get("status_artifacts") or []
    if len(status_artifacts) != 2:
        errors.append(f"{target_date}: current source status evidence is incomplete")
    for artifact in status_artifacts:
        path = root / str(artifact.get("path", ""))
        if not path.is_file():
            errors.append(f"{target_date}: current source status path is missing")
        if not str(artifact.get("generated_at", "")).strip():
            errors.append(f"{target_date}: current source generated_at is blank")

    replay = manifest.get("historical_replay_evidence") or {}
    replay_path = root / str(replay.get("path", ""))
    forbidden = set(replay.get("forbidden_reconstruction") or [])
    if not REQUIRED_FORBIDDEN_RECONSTRUCTION.issubset(forbidden):
        errors.append(f"{target_date}: replay reconstruction blocker missing")
    if not replay_path.is_file() or sha256_file(replay_path) != replay.get("sha256"):
        errors.append(f"{target_date}: replay evidence hash mismatch")

    lineage = manifest.get("lineage") or {}
    for field in (
        "producer",
        "validator",
        "workflow",
        "workflow_run_id",
        "workflow_run_url",
        "recovery_id",
        "source_head_sha",
        "evidence_contract_path",
        "evidence_contract_sha256",
    ):
        if not str(lineage.get(field, "")).strip():
            errors.append(f"{target_date}: lineage.{field} is blank")
    return errors


def validate_index(
    root: Path,
    *,
    index_path: Path,
    evidence_csv: Path,
    docs_json: Path,
    latest_md: Path,
    docs_md: Path,
) -> list[str]:
    errors: list[str] = []
    if not index_path.is_file():
        return [f"missing event/catalyst recovery index: {index_path}"]
    evidence_rows = read_evidence(evidence_csv)
    evidence_by_date = {row["target_date"]: row for row in evidence_rows}
    index = read_json(index_path)
    if index.get("schema_version") != INDEX_SCHEMA_VERSION:
        errors.append("event/catalyst recovery index schema_version mismatch")
    if index.get("completion_state") != BLOCKED_STATUS:
        errors.append("event/catalyst recovery index must fail closed")
    if tuple(index.get("target_dates") or []) != TARGET_DATES:
        errors.append("event/catalyst recovery index target dates mismatch")

    entries = index.get("manifests") or []
    if [entry.get("target_date") for entry in entries] != list(TARGET_DATES):
        errors.append("event/catalyst recovery index entries are incomplete")
    for entry in entries:
        target_date = str(entry.get("target_date", ""))
        if entry.get("status") != BLOCKED_STATUS:
            errors.append(f"{target_date}: index entry must fail closed")
            continue
        errors.extend(
            validate_manifest(
                root,
                manifest_path=root / str(entry.get("manifest_path", "")),
                expected_sha256=str(entry.get("manifest_sha256", "")),
                evidence=evidence_by_date[target_date],
            )
        )

    mirror_pairs = ((index_path, docs_json), (latest_md, docs_md))
    for output_path, docs_path in mirror_pairs:
        if not output_path.is_file() or not docs_path.is_file():
            errors.append(f"missing recovery latest mirror: {docs_path}")
        elif output_path.read_bytes() != docs_path.read_bytes():
            errors.append(f"recovery latest mirror mismatch: {docs_path}")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo-root", type=Path, default=ROOT)
    parser.add_argument("--index", type=Path, default=DEFAULT_INDEX)
    parser.add_argument("--evidence-csv", type=Path, default=DEFAULT_EVIDENCE_CSV)
    parser.add_argument("--docs-json", type=Path, default=DEFAULT_DOCS_JSON)
    parser.add_argument("--latest-md", type=Path, default=DEFAULT_LATEST_MD)
    parser.add_argument("--docs-md", type=Path, default=DEFAULT_DOCS_MD)
    args = parser.parse_args()

    root = args.repo_root.resolve()

    def resolve(path: Path) -> Path:
        return path if path.is_absolute() else root / path

    try:
        errors = validate_index(
            root,
            index_path=resolve(args.index),
            evidence_csv=resolve(args.evidence_csv),
            docs_json=resolve(args.docs_json),
            latest_md=resolve(args.latest_md),
            docs_md=resolve(args.docs_md),
        )
    except (OSError, ValueError) as exc:
        errors = [str(exc)]
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1
    print("event/catalyst historical recovery manifest validation passed")
    print(f"validated_dates={','.join(TARGET_DATES)}")
    print(f"completion_state={BLOCKED_STATUS}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
