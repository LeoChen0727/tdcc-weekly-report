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
AUTHORIZED_CHECKPOINT_SOURCE_SHA = (
    "4d715065f38389752aaeaa0c511280c47ccedc08"
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
            "CHECKPOINT_SOURCE_SHA: ${{ inputs.checkpoint_source_sha }}",
            '--checkpoint-source-sha "$CHECKPOINT_SOURCE_SHA"',
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
    checkpoint_source_input = re.search(
        r"(?ms)^      checkpoint_source_sha:\s*\n"
        r"(?P<body>(?:        [^\n]*\n)+)",
        text,
    )
    if checkpoint_source_input is None:
        errors.append(
            "validation replay workflow lacks checkpoint_source_sha input"
        )
    else:
        source_input_body = checkpoint_source_input.group("body")
        expected_default = (
            f'default: "{AUTHORIZED_CHECKPOINT_SOURCE_SHA}"'
        )
        if expected_default not in source_input_body:
            errors.append(
                "validation replay checkpoint_source_sha must default to "
                "the exact immutable checkpoint source SHA"
            )
        if "required: false" not in source_input_body:
            errors.append(
                "validation replay checkpoint_source_sha must remain optional "
                "for capture_canary mode"
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


def validate_20260810_replay_workflow(
    text: str, errors: list[str]
) -> None:
    start = text.find("\n  replay-20260810:")
    end = text.find("\n  isolated-six-pdf-validation:", start + 1)
    if start < 0 or end <= start:
        errors.append(
            "validation replay workflow lacks isolated 20260810 job boundary"
        )
        return
    block = text[start:end]
    require_fragments(
        block,
        [
            'REPLAY_DATE: "20260810"',
            'DAILY_FULL_VALIDATION_REPLAY_PROFILE_DATE: "20260810"',
            'CHECKPOINT_SOURCE_SHA: "bf04304b0dafc480c690a8d5c9c53aa70634b7f2"',
            'CHECKPOINT_RUN_ID: "31384317163"',
            'CHECKPOINT_ARTIFACT_ID: "9061570264"',
            "sha256:87a586726d64300371a77fddf92f892357732cc754395aac3f3d872465ac49f4",
            "daily-full-pre-step41-checkpoint-31384317163-1",
            'CHECKPOINT_CAPTURE_CONTEXT: "production_pre_step41"',
            "scripts/run_daily_full_validation_replay.py replay",
            "daily-full-validation-replay-20260810-post-${{ github.run_id }}",
            "if-no-files-found: error",
        ],
        "20260810 validation replay workflow",
        errors,
    )
    require_fragments(
        text,
        ["contents: read", "actions: read"],
        "20260810 validation replay permissions",
        errors,
    )
    for fragment in (
        "capture-canary",
        "render-pdfs",
        "isolated-six-pdf-validation",
        "git push",
        "installAllWorkflowTriggers",
    ):
        if fragment in block:
            errors.append(
                "20260810 replay workflow contains forbidden behavior: "
                f"{fragment}"
            )


def validate_runner(text: str, errors: list[str]) -> None:
    require_fragments(
        text,
        [
            'REPLAY_PROFILE_ENV = "DAILY_FULL_VALIDATION_REPLAY_PROFILE_DATE"',
            'if replay_date == "20260807":',
            '"old_failed_run_id": "31174813266"',
            '"checkpoint_run_id": "31268964962"',
            '"checkpoint_artifact_id": "9025240156"',
            'if replay_date == "20260810":',
            '"checkpoint_run_id": "31384317163"',
            '"checkpoint_artifact_id": "9061570264"',
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
            "write_validation_only_pdf_source_readme",
            "output/latest/chatgpt_daily_report_packet_latest.txt",
            "validation-only PDF source README requires validation-only mode",
            "validation-only PDF source README identity mismatch",
            'failure_phase = "materialize validation-only PDF source README"',
            "capture_replay_failure_checkpoint",
            "require_checkpoint_structured_source_manifest_identity",
            "require_checkpoint_source_revision_manifest_identity",
            "checkpoint source revision manifest raw/canonical SHA mismatch",
            "checkpoint source revision manifest path/object mismatch",
            "checkpoint source revision manifest mode mismatch",
            'failure_phase = "verify checkpoint source revision manifest"',
            "write_minimal_replay_failure_upload_receipt",
            "minimal failure receipt written",
            "DELETION_MANIFEST_PATH",
            "source_tree_file_identity",
            '"ls-tree", "-z", source_sha',
            "write_checkpoint_deletion_manifest",
            "checkpoint_deletion_baseline_matches",
            '"hash-object", "--path", relative, "--stdin"',
            "checkpoint deletion Git canonicalization failed",
            "apply_checkpoint_deletions",
            "checkpoint deletion source identity drift",
            "checkpoint deletion baseline content drift",
            'checkpoint_kind="post_validation"',
            'capture_context="validation_replay"',
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
            "emit_utf8_safe_text",
            'binary_stream.write(payload.encode("utf-8"))',
            "emit_utf8_safe_text(rendered_stdout, stream=sys.stdout)",
            "restore_checkpoint",
            "run_registered_parity_validators",
            "scripts/validate_daily_candidate_model_layer.py",
            "scripts/validate_volume_attack_theme_layer.py",
            "scripts/validate_daily_warrant_formal_sync_scope.py",
            "REGISTERED_PARITY_VALIDATOR_ARGUMENTS",
            '"--validate-source-date"',
            "registered replay parity validator mode is missing",
            "registered_fail_closed_validators",
            "AUTHORIZED_20260810_MODEL_FIX_COMMIT",
            "AUTHORIZED_20260810_MODEL_FIX_PATHS",
            "AUTHORIZED_20260810_REPLAY_CONTROL_PATHS",
            "reconcile_checkpoint_source_state",
            "checkpoint_source_git_object",
            "immutable_checkpoint_payload",
            "replay_source_git_object",
            "mutable_latest_fallback_allowed",
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
    if "print(rendered_stdout.rstrip())" in text:
        errors.append(
            "validation replay renderer output must not use locale-bound print"
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
    validate_20260810_replay_workflow(read(REPLAY_WORKFLOW), errors)
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
