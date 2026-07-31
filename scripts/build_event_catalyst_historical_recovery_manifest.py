from __future__ import annotations

import argparse
import csv
import hashlib
import json
import os
import subprocess
from datetime import datetime
from pathlib import Path
from typing import Any
from zoneinfo import ZoneInfo


ROOT = Path(__file__).resolve().parents[1]
SCHEMA_VERSION = "event_catalyst_historical_recovery_v1"
INDEX_SCHEMA_VERSION = "event_catalyst_historical_recovery_index_v1"
BLOCKED_STATUS = "blocked_authoritative_history"
TARGET_DATES = ("20260720", "20260721", "20260722", "20260723", "20260724")
REQUIRED_FORBIDDEN_RECONSTRUCTION = {
    "event_as_published",
    "catalyst_as_published",
}
DEFAULT_EVIDENCE_CSV = Path(
    "config/event_catalyst_historical_recovery_failures.csv"
)
SOURCE_STATUS_PATHS = (
    Path("output/latest/catalyst_data_source_status_latest.json"),
    Path("output/latest/calendar_data_source_status_latest.json"),
)
OVERLAY_CONTRACT_PATH = Path("config/event_catalyst_overlay_contract.csv")


def now_text() -> str:
    return datetime.now(ZoneInfo("Asia/Taipei")).strftime(
        "%Y-%m-%d %H:%M:%S Asia/Taipei"
    )


def sha256_file(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def read_json(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8-sig"))
    if not isinstance(value, dict):
        raise ValueError(f"JSON root must be an object: {path.as_posix()}")
    return value


def read_evidence(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        rows = [
            {key: str(value or "").strip() for key, value in row.items()}
            for row in csv.DictReader(handle)
        ]
    observed_dates = tuple(row.get("target_date", "") for row in rows)
    if observed_dates != TARGET_DATES:
        raise ValueError(
            "recovery evidence must contain only the ordered target dates "
            f"{','.join(TARGET_DATES)}"
        )
    return rows


def split_values(value: str) -> list[str]:
    return [item.strip() for item in value.split(";") if item.strip()]


def git_head(root: Path) -> str:
    result = subprocess.run(
        ["git", "rev-parse", "HEAD"],
        cwd=root,
        check=True,
        capture_output=True,
        text=True,
    )
    return result.stdout.strip()


def current_source_context(root: Path) -> list[dict[str, str]]:
    context: list[dict[str, str]] = []
    for relative_path in SOURCE_STATUS_PATHS:
        path = root / relative_path
        payload = read_json(path)
        context.append(
            {
                "path": relative_path.as_posix(),
                "generated_at": str(payload.get("generated_at", "")).strip(),
                "status": str(
                    payload.get("external_fetch_status")
                    or payload.get("status")
                    or ""
                ).strip(),
            }
        )
    return context


def validate_evidence_row(row: dict[str, str], root: Path) -> dict[str, Any]:
    target_date = row["target_date"]
    if row.get("recovery_status") != BLOCKED_STATUS:
        raise ValueError(f"{target_date}: recovery_status must fail closed")
    required_false = (
        "authoritative_history_artifact_present",
        "current_value_backfill_allowed",
        "historical_content_reconstructed",
    )
    for field in required_false:
        if row.get(field, "").lower() != "false":
            raise ValueError(f"{target_date}: {field} must be false")
    if row.get("runner_uncommitted_sources_irrecoverable", "").lower() != "true":
        raise ValueError(
            f"{target_date}: runner_uncommitted_sources_irrecoverable must be true"
        )

    run_ids = split_values(row.get("failed_run_ids", ""))
    run_urls = split_values(row.get("failed_run_urls", ""))
    if not run_ids or len(run_ids) != len(run_urls):
        raise ValueError(f"{target_date}: failed run ids and URLs must align")
    failed_runs = [
        {"run_id": run_id, "url": run_url}
        for run_id, run_url in zip(run_ids, run_urls, strict=True)
    ]

    replay_relative = Path(row.get("replay_manifest_path", ""))
    replay_path = root / replay_relative
    replay = read_json(replay_path)
    forbidden = set(replay.get("forbidden_reconstruction") or [])
    if not REQUIRED_FORBIDDEN_RECONSTRUCTION.issubset(forbidden):
        raise ValueError(
            f"{target_date}: replay evidence does not forbid event/catalyst reconstruction"
        )
    if str(replay.get("report_date", "")) != target_date:
        raise ValueError(f"{target_date}: replay evidence report_date mismatch")

    return {
        "failed_runs": failed_runs,
        "historical_replay_evidence": {
            "path": replay_relative.as_posix(),
            "sha256": sha256_file(replay_path),
            "replay_id": str(replay.get("replay_id", "")),
            "pipeline_commit_sha": str(replay.get("pipeline_commit_sha", "")),
            "publication_status": str(replay.get("publication_status", "")),
            "as_published": replay.get("as_published"),
            "forbidden_reconstruction": sorted(forbidden),
        },
    }


def write_json(path: Path, value: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(value, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )


def build_manifests(
    root: Path,
    *,
    evidence_csv: Path,
    recovery_id: str,
    workflow_run_id: str,
    workflow_run_url: str,
    output_root: Path,
    latest_json: Path,
    latest_md: Path,
) -> dict[str, Any]:
    rows = read_evidence(evidence_csv)
    generated_at = now_text()
    source_head_sha = git_head(root)
    source_context = current_source_context(root)
    overlay_contract_sha256 = sha256_file(root / OVERLAY_CONTRACT_PATH)
    entries: list[dict[str, str]] = []

    for row in rows:
        target_date = row["target_date"]
        evidence = validate_evidence_row(row, root)
        manifest = {
            "schema_version": SCHEMA_VERSION,
            "generated_at": generated_at,
            "target_date": target_date,
            "status": BLOCKED_STATUS,
            "completion_state": BLOCKED_STATUS,
            "publication_status": "historical_event_catalyst_not_as_published",
            "as_published": False,
            "authoritative_history_artifact_present": False,
            "current_value_backfill_allowed": False,
            "historical_content_reconstructed": False,
            "runner_uncommitted_sources_irrecoverable": True,
            "failed_runs": evidence["failed_runs"],
            "failed_head_sha": row["failed_head_sha"],
            "failed_step": row["failed_step"],
            "failed_gate": row["failed_gate"],
            "commit_step_state": row["commit_step_state"],
            "runner_source_state": row["runner_source_state"],
            "blocker_reason": row["blocker_reason"],
            "prohibitions": [
                "do_not_reconstruct_historical_event_content",
                "do_not_infer_historical_catalyst_content",
                "do_not_retro_date_current_source_values",
            ],
            "effect_policy": {
                "contract_path": OVERLAY_CONTRACT_PATH.as_posix(),
                "contract_sha256": overlay_contract_sha256,
                "allowed_effect": "disclosure_only",
                "score_allowed": False,
                "ranking_allowed": False,
                "reason_text_allowed": False,
                "requires_human_review": True,
            },
            "current_source_refresh_context": {
                "historical_backfill_effect_allowed": False,
                "interpretation": (
                    "Current source status proves only the current refresh and must not "
                    "be treated as target-date evidence."
                ),
                "status_artifacts": source_context,
            },
            "historical_replay_evidence": evidence[
                "historical_replay_evidence"
            ],
            "lineage": {
                "producer": (
                    "scripts/build_event_catalyst_historical_recovery_manifest.py"
                ),
                "validator": (
                    "scripts/validate_event_catalyst_historical_recovery_manifest.py"
                ),
                "workflow": ".github/workflows/event_catalyst_update.yml",
                "workflow_run_id": workflow_run_id,
                "workflow_run_url": workflow_run_url,
                "recovery_id": recovery_id,
                "source_head_sha": source_head_sha,
                "evidence_contract_path": evidence_csv.relative_to(root).as_posix(),
                "evidence_contract_sha256": sha256_file(evidence_csv),
            },
        }
        manifest_path = (
            output_root
            / recovery_id
            / target_date
            / "event_catalyst_recovery_manifest.json"
        )
        write_json(manifest_path, manifest)
        entries.append(
            {
                "target_date": target_date,
                "status": BLOCKED_STATUS,
                "manifest_path": manifest_path.relative_to(root).as_posix(),
                "manifest_sha256": sha256_file(manifest_path),
            }
        )

    index = {
        "schema_version": INDEX_SCHEMA_VERSION,
        "generated_at": generated_at,
        "recovery_id": recovery_id,
        "completion_state": BLOCKED_STATUS,
        "source_head_sha": source_head_sha,
        "workflow_run_id": workflow_run_id,
        "workflow_run_url": workflow_run_url,
        "target_dates": list(TARGET_DATES),
        "manifests": entries,
    }
    write_json(latest_json, index)

    lines = [
        "# Event/Catalyst Historical Recovery",
        "",
        f"- generated_at: `{generated_at}`",
        f"- recovery_id: `{recovery_id}`",
        f"- completion_state: `{BLOCKED_STATUS}`",
        f"- workflow_run_id: `{workflow_run_id}`",
        "",
        "No target date has a saved point-in-time/as-published event/catalyst artifact.",
        "Current values were not used as historical backfill.",
        "",
        "| target_date | status | failed_runs | failed_gate | manifest |",
        "|---|---|---|---|---|",
    ]
    for row, entry in zip(rows, entries, strict=True):
        lines.append(
            f"| {row['target_date']} | {BLOCKED_STATUS} | "
            f"{row['failed_run_ids']} | {row['failed_gate']} | "
            f"`{entry['manifest_path']}` |"
        )
    latest_md.parent.mkdir(parents=True, exist_ok=True)
    latest_md.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return index


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo-root", type=Path, default=ROOT)
    parser.add_argument("--evidence-csv", type=Path, default=DEFAULT_EVIDENCE_CSV)
    parser.add_argument("--recovery-id", required=True)
    parser.add_argument("--workflow-run-id", default=os.environ.get("GITHUB_RUN_ID", ""))
    parser.add_argument("--workflow-run-url", default="")
    parser.add_argument(
        "--output-root",
        type=Path,
        default=Path("output/history/event_catalyst_recovery"),
    )
    parser.add_argument(
        "--latest-json",
        type=Path,
        default=Path("output/latest/event_catalyst_historical_recovery_latest.json"),
    )
    parser.add_argument(
        "--latest-md",
        type=Path,
        default=Path("output/latest/event_catalyst_historical_recovery_latest.md"),
    )
    args = parser.parse_args()

    root = args.repo_root.resolve()
    evidence_csv = args.evidence_csv
    output_root = args.output_root
    latest_json = args.latest_json
    latest_md = args.latest_md
    if not evidence_csv.is_absolute():
        evidence_csv = root / evidence_csv
    if not output_root.is_absolute():
        output_root = root / output_root
    if not latest_json.is_absolute():
        latest_json = root / latest_json
    if not latest_md.is_absolute():
        latest_md = root / latest_md

    try:
        index = build_manifests(
            root,
            evidence_csv=evidence_csv,
            recovery_id=args.recovery_id,
            workflow_run_id=args.workflow_run_id,
            workflow_run_url=args.workflow_run_url,
            output_root=output_root,
            latest_json=latest_json,
            latest_md=latest_md,
        )
    except (OSError, ValueError, json.JSONDecodeError, subprocess.CalledProcessError) as exc:
        print(f"ERROR: unable to build event/catalyst recovery manifests: {exc}")
        return 1

    print("event/catalyst historical recovery manifests built")
    print(f"target_dates={','.join(index['target_dates'])}")
    print(f"completion_state={index['completion_state']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
