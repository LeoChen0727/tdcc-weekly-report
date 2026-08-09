#!/usr/bin/env python3
"""Validate the fail-closed Daily Full validation-only replay contract."""

from __future__ import annotations

import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PRODUCTION_WORKFLOW = ROOT / ".github/workflows/daily_full_pipeline.yml"
REPLAY_WORKFLOW = (
    ROOT
    / ".github/workflows/"
    "daily_full_validation_replay_20260807.yml"
)
RUNNER = ROOT / "scripts/run_daily_full_validation_replay.py"
CHECKPOINT = (
    ROOT / "scripts/daily_full_validation_replay_checkpoint.py"
)
TEST = ROOT / "tests/test_daily_full_validation_replay.py"
PRODUCTION_INVENTORY = (
    ROOT / "config/repo_production_inventory.csv"
)
LIFECYCLE_INVENTORY = (
    ROOT / "config/repo_file_lifecycle_inventory.csv"
)


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def require_fragments(
    text: str,
    fragments: list[str],
    label: str,
    errors: list[str],
) -> None:
    for fragment in fragments:
        if fragment not in text:
            errors.append(
                f"{label} missing contract fragment: {fragment}"
            )


def validate_production_workflow(
    text: str, errors: list[str]
) -> None:
    create = (
        "- name: Create failure-safe immutable pre-step41 checkpoint"
    )
    upload = (
        "- name: Upload failure-safe immutable pre-step41 checkpoint"
    )
    before = "- name: Build volume breakout watch"
    failure = "- name: Build volume attack theme layer"
    positions = {
        key: text.find(key)
        for key in (before, create, upload, failure)
    }
    if any(position < 0 for position in positions.values()):
        errors.append(
            "Daily Full Pipeline is missing the pre-step41 checkpoint "
            "sequence"
        )
    elif not (
        positions[before]
        < positions[create]
        < positions[upload]
        < positions[failure]
    ):
        errors.append(
            "Daily Full Pipeline checkpoint must upload after step40 "
            "and before original step41"
        )
    require_fragments(
        text,
        [
            "capture-production-checkpoint",
            '--replay-date "$EXPECTED_MAIN_PRICE_DATE"',
            '--source-sha "$GITHUB_SHA"',
            '--run-id "$GITHUB_RUN_ID"',
            "if: always()",
            "if-no-files-found: error",
            "retention-days: 30",
            "daily-full-pre-step41-checkpoint-${{ github.run_id }}-${{ github.run_attempt }}",
        ],
        "Daily Full Pipeline",
        errors,
    )


def validate_replay_workflow(
    text: str, errors: list[str]
) -> None:
    require_fragments(
        text,
        [
            "workflow_dispatch:",
            "capture_canary",
            "checkpoint_run_id:",
            "checkpoint_source_sha:",
            "checkpoint_artifact_id:",
            "checkpoint_artifact_digest:",
            'REPLAY_DATE: "20260807"',
            "contents: read",
            "actions: read",
            "persist-credentials: false",
            "authoritative 20260807 revision",
            "Upload immutable pre-step41 checkpoint before controlled failure",
            "if: always()",
            "if-no-files-found: error",
            "retention-days: 30",
            "steps.checkpoint_upload.outputs.artifact-id",
            "steps.checkpoint_upload.outputs.artifact-digest",
            "checkpoint_artifact_digest=sha256:$ARTIFACT_DIGEST",
            "Controlled canary failure after immutable checkpoint upload",
            "exit 86",
            "repos/$GITHUB_REPOSITORY/actions/artifacts/$CHECKPOINT_ARTIFACT_ID",
            "workflow_run.id mismatch",
            "artifact digest mismatch",
            "artifact id mismatch",
            "canary run must be completed failure",
            "canary run head SHA mismatch",
            "checkpoint replay source transition mismatch",
            "canary workflow path mismatch",
            "replay original step41 through all downstream gates",
            "post-validation-checkpoint",
            "runs-on: windows-2025",
            "render-pdfs",
            "isolated-pdfs",
            "PyMuPDF",
            "pillow",
            "six isolated PDFs and complete visual evidence",
        ],
        "validation replay workflow",
        errors,
    )
    forbidden = (
        re.compile(r"(?m)^  (push|pull_request|schedule):"),
        re.compile(r"PRODUCTION_ARTIFACT_WRITE_DEPLOY_KEY"),
        re.compile(r"(?m)^\s*contents:\s*write\s*$"),
        re.compile(
            r"(?m)^\s*git\s+(commit|push|pull|rebase|reset|merge)\b"
        ),
        re.compile(r"workflow_dispatch.*daily_full_pipeline", re.I),
    )
    for pattern in forbidden:
        if pattern.search(text):
            errors.append(
                "validation replay workflow contains forbidden "
                f"production capability: {pattern.pattern}"
            )
    canary_upload = text.find(
        "Upload immutable pre-step41 checkpoint before controlled failure"
    )
    canary_failure = text.find(
        "Controlled canary failure after immutable checkpoint upload"
    )
    if (
        canary_upload < 0
        or canary_failure < 0
        or canary_upload >= canary_failure
    ):
        errors.append(
            "controlled canary failure must occur only after upload"
        )
    post_upload = text.find(
        "Upload post-step41 validation checkpoint and gates"
    )
    pdf_job = text.find("\n  isolated-six-pdf-validation:")
    post_upload_block = (
        text[post_upload:pdf_job]
        if post_upload >= 0 and pdf_job > post_upload
        else ""
    )
    if (
        not post_upload_block
        or "if: always()" not in post_upload_block
        or "post-validation-checkpoint" not in post_upload_block
        or "if-no-files-found: error" not in post_upload_block
    ):
        errors.append(
            "replay failure checkpoint must always upload fail closed"
        )


def validate_runner(text: str, errors: list[str]) -> None:
    require_fragments(
        text,
        [
            'REPLAY_DATE = "20260807"',
            'OLD_FAILED_RUN_ID = "31174813266"',
            'AUTHORIZED_CHECKPOINT_SOURCE_SHA = "4d715065f38389752aaeaa0c511280c47ccedc08"',
            'AUTHORIZED_CHECKPOINT_RUN_ID = "31268964962"',
            'AUTHORIZED_CHECKPOINT_ARTIFACT_ID = "9025240156"',
            "AUTHORIZED_CHECKPOINT_MANIFEST_SHA256",
            "AUTHORIZED_PRODUCER_FIX_COMMIT",
            "AUTHORIZED_VALIDATOR_FIX_COMMIT",
            "AUTHORIZED_VALIDATOR_FIX_PATHS",
            "AUTHORIZED_FORMAL_LINEAGE_FIX_COMMIT",
            "AUTHORIZED_FORMAL_LINEAGE_FIX_PATHS",
            "AUTHORIZED_OPERATION_COMPLETENESS_FIX_COMMIT",
            "AUTHORIZED_OPERATION_COMPLETENESS_FIX_PATHS",
            "AUTHORIZED_FORMAL_OPERATION_SHARED_PATH",
            'AUTHORIZED_PUBLISH_BASELINE_DATE = "20260805"',
            "PUBLISH_BASELINE_DIRNAME",
            "PUBLISH_BASELINE_EVIDENCE_PATH",
            "materialize_publish_freshness_baseline",
            "current freshness artifact cannot substitute for baseline",
            "checkpoint publish freshness baseline bytes/SHA mismatch",
            "capture_replay_failure_checkpoint",
            'checkpoint_kind="post_step_failure"',
            'capture_context="validation_replay_failure"',
            "authorized_code_revision_transition",
            "require_authorized_checkpoint_bundle_identity",
            "checkpoint_source_sha",
            "replay_source_sha",
            "expected_destination_source_sha",
            'POST_START_STEP = "Build volume attack theme layer"',
            'POST_END_STEP = "Validate catalyst layer"',
            '"python scripts/fetch_futures_options_indicators.py"',
            "authoritative_historical_revision",
            "byte_parity_with_run_31174813266",
            "run_authoritative_historical_revision",
            "price_history_extension_manifest.json",
            "validation_only_authoritative_price_history_extension",
            "historical source replay planner after price extension",
            "price history extension manifest SHA mismatch",
            'producer_env["GIT_INDEX_FILE"]',
            'producer_env["GIT_DIR"]',
            "price-history-extension.git-dir",
            "verify validation-only staged baseline",
            "verify validation-only working tree baseline",
            "create validation-only synthetic baseline commit",
            '"--porcelain=v1"',
            '"--untracked-files=all"',
            "real Git index drifted during validation-only price extension",
            "real Git HEAD/ref drifted during validation-only price extension",
            "validation-only synthetic index tree drifted",
            'f"refs/replace/{source_sha}"',
            'no_replace_env["GIT_NO_REPLACE_OBJECTS"]',
            "verify validation-only source HEAD",
            "price history extension status/mode mismatch",
            "remove_validation_only_git_index",
            "2026-08-07T23:00:00+08:00",
            "historical replay market session must be open_confirmed",
            "--assessment-date",
            "expected-pipeline-sha",
            "capture-production-checkpoint",
            "capture-canary",
            "render-pdfs",
            "restore_checkpoint",
            "run_registered_parity_validators",
            "scripts/validate_daily_candidate_model_layer.py",
            "scripts/validate_volume_attack_theme_layer.py",
            "scripts/validate_daily_warrant_formal_sync_scope.py",
            "registered_fail_closed_validators",
            "report_ready",
            "daily_pdf_ready",
            "write_runtime_manifest",
            "official_entrypoint_invoked",
            "validate_daily_pdf_completion_hard_gate.py",
            "render_contact_sheets",
            "all_pages_rasterized_complete_contact_sheets",
            "production_not_run",
            "official_pdf_published",
        ],
        "validation replay runner",
        errors,
    )
    if "git commit" in text or "git push" in text:
        errors.append(
            "validation replay runner must not contain commit/push commands"
        )


def validate_checkpoint(text: str, errors: list[str]) -> None:
    require_fragments(
        text,
        [
            "CHECKPOINT_MANIFEST",
            "CHECKPOINT_MANIFEST_SHA",
            "source_revision_manifest.json",
            "path_allowlist",
            "baseline",
            "bytes",
            "sha256",
            "producer_run_id",
            "producer_head_sha",
            "capture_context",
            "mutable_source_fallback_allowed",
            "--quiet",
            "restore collision",
            "expected_destination_source_sha",
            "destination_source_sha",
            "checkpoint revision transition metadata mismatch",
            "checkpoint payload path set mismatch",
            "source identity categories are incomplete",
            "checkpoint source revision manifest mismatch",
            "production_not_run",
            "official_pdf_published",
            "repo_artifacts_pushed_by_replay",
        ],
        "checkpoint helper",
        errors,
    )


def validate_inventory(errors: list[str]) -> None:
    expected = [
        ".github/workflows/daily_full_validation_replay_20260807.yml",
        "scripts/daily_full_validation_replay_checkpoint.py",
        "scripts/run_daily_full_validation_replay.py",
        "scripts/validate_daily_full_validation_replay.py",
        "tests/test_daily_full_validation_replay.py",
    ]
    production = read(PRODUCTION_INVENTORY)
    lifecycle = read(LIFECYCLE_INVENTORY)
    for path in expected[:4]:
        if path not in production:
            errors.append(
                f"production inventory missing replay path: {path}"
            )
    for path in expected:
        if path not in lifecycle:
            errors.append(
                f"lifecycle inventory missing replay path: {path}"
            )


def validate() -> list[str]:
    errors: list[str] = []
    for path in (
        PRODUCTION_WORKFLOW,
        REPLAY_WORKFLOW,
        RUNNER,
        CHECKPOINT,
        TEST,
        PRODUCTION_INVENTORY,
        LIFECYCLE_INVENTORY,
    ):
        if not path.is_file():
            errors.append(
                "required validation replay contract file missing: "
                f"{path}"
            )
    if errors:
        return errors
    validate_production_workflow(
        read(PRODUCTION_WORKFLOW), errors
    )
    validate_replay_workflow(read(REPLAY_WORKFLOW), errors)
    validate_runner(read(RUNNER), errors)
    validate_checkpoint(read(CHECKPOINT), errors)
    validate_inventory(errors)
    return errors


def main() -> int:
    errors = validate()
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1
    print(
        "Daily Full validation-only historical replay contract passed: "
        "date=20260807 pre_step41_checkpoint=fail_safe "
        "canary=controlled_failure replay=exact_artifact "
        "pdf_count=6 production_not_run=true"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
