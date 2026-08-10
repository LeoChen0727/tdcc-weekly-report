#!/usr/bin/env python3
"""Validate the F-only local Daily Full replay workspace contract."""

from __future__ import annotations

import csv
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
HELPER = ROOT / "scripts/run_local_daily_full_validation_replay.py"
RUNNER = ROOT / "scripts/run_daily_full_validation_replay.py"
SAFETY = ROOT / "scripts/git_worktree_safety.py"
CONTRACT = ROOT / "config/git_worktree_materialization_contract.csv"
TEST = ROOT / "tests/test_git_worktree_safety.py"
PRODUCTION_INVENTORY = ROOT / "config/repo_production_inventory.csv"
LIFECYCLE_INVENTORY = ROOT / "config/repo_file_lifecycle_inventory.csv"
WORKFLOW = ROOT / ".github/workflows/daily_full_validation_replay_20260807.yml"
CONSUMER_ID = "local_daily_full_validation_replay"
APPROVED_ROOT = r"F:\CodexStorage\validation-replay-workspaces\taiwan-stock-recommendation"


def _read(path: Path) -> str:
    return path.read_text(encoding="utf-8-sig")


def _require_fragments(
    text: str, fragments: tuple[str, ...], label: str, errors: list[str]
) -> None:
    for fragment in fragments:
        if fragment not in text:
            errors.append(f"{label} missing contract fragment: {fragment}")


def validate() -> list[str]:
    errors: list[str] = []
    required = (
        HELPER,
        RUNNER,
        SAFETY,
        CONTRACT,
        TEST,
        PRODUCTION_INVENTORY,
        LIFECYCLE_INVENTORY,
        WORKFLOW,
    )
    for path in required:
        if not path.is_file():
            errors.append(f"missing local replay routing contract file: {path}")
    if errors:
        return errors

    with CONTRACT.open("r", encoding="utf-8-sig", newline="") as handle:
        rows = [
            row
            for row in csv.DictReader(handle)
            if row.get("consumer_id", "").strip() == CONSUMER_ID
        ]
    if len(rows) != 1:
        errors.append("local replay materialization contract must have exactly one row")
    else:
        expected = {
            "entrypoint": "scripts/run_local_daily_full_validation_replay.py",
            "materialization_mode": "full_local_validation_replay_only",
            "checkout_workers": "1",
            "max_concurrent": "1",
            "temp_root_policy": "approved_root_only",
            "approved_destination_root": APPROVED_ROOT,
            "approved_root_filesystem": "NTFS",
            "default_destination_policy": "approved_root_task_or_run_child",
            "minimum_free_bytes": "21474836480",
        }
        for key, expected_value in expected.items():
            observed = rows[0].get(key, "").strip()
            if key == "approved_destination_root":
                observed = observed.lower().rstrip("\\/")
                expected_value = expected_value.lower().rstrip("\\/")
            if observed != expected_value:
                errors.append(
                    f"local replay materialization contract {key} mismatch: "
                    f"expected={expected_value!r}, observed={observed!r}"
                )

    helper = _read(HELPER)
    _require_fragments(
        helper,
        (
            "approved_local_validation_replay_root",
            "create_registered_full_local_validation_replay_worktree",
            'runner_temp_root = workspace_root / "runner-temp"',
            'runner_temp_root / "price-history-extension.git-dir"',
            'runner_temp_root / "price-history-extension.git-index"',
            'render_root = workspace_root / "pdf-render"',
            'extract_root=render_root / "visual_evidence"',
            'evidence_root = workspace_root / "evidence"',
            '"--runner-temp"',
            '"--post-bundle-dir"',
            '"--output-dir"',
            "workspace collision; workspace ids are ",
            "single-use",
            "forbidden_system_temp_replay_evidence_before",
            "forbidden_system_temp_replay_evidence_after",
            '"system_temp_replay_baseline_unchanged": True',
            '"temp_environment_unchanged": True',
            "C Temp replay baseline drifted during F-only pilot",
            "TEMP/TMP environment drifted during F-only pilot",
            "checkpoint bundle must not be materialized in Windows system Temp",
            "pilot manifest path/bytes/SHA set drift",
            '"c_temp_fallback_used": False',
            '"production_not_run": True',
            '"official_pdf_published": False',
        ),
        "local replay helper",
        errors,
    )
    for forbidden in (
        "tempfile",
        "TemporaryDirectory",
        "mkdtemp",
        'os.environ["TEMP"]',
        'os.environ["TMP"]',
    ):
        if forbidden in helper:
            errors.append(
                f"local replay helper contains forbidden C Temp fallback/mutation: {forbidden}"
            )

    safety = _read(SAFETY)
    _require_fragments(
        safety,
        (
            "LOCAL_VALIDATION_REPLAY_CONSUMER_ID",
            "APPROVED_LOCAL_VALIDATION_REPLAY_ROOT_WINDOWS",
            "MINIMUM_LOCAL_VALIDATION_REPLAY_FREE_BYTES",
            "WINDOWS_FIXED_DRIVE_TYPE",
            "create_registered_full_local_validation_replay_worktree",
        ),
        "Git worktree safety",
        errors,
    )
    runner = _read(RUNNER)
    _require_fragments(
        runner,
        (
            'runner_temp / "price-history-extension.git-dir"',
            'runner_temp / "price-history-extension.git-index"',
            'evidence_root = output_dir / "visual_evidence"',
        ),
        "existing replay runner",
        errors,
    )
    workflow = _read(WORKFLOW)
    if "run_local_daily_full_validation_replay.py" in workflow:
        errors.append(
            "GitHub-hosted validation replay must not use the local F routing helper"
        )
    if "$RUNNER_TEMP/daily-full-validation-replay" not in workflow:
        errors.append("GitHub-hosted replay RUNNER_TEMP semantics drifted")

    tests = _read(TEST)
    _require_fragments(
        tests,
        (
            "test_registered_full_local_validation_replay_materializes_complete_tree",
            "test_local_replay_pilot_routes_all_large_roots_to_f_without_c_temp",
            "test_local_replay_pilot_rejects_c_temp_or_environment_delta",
            "test_local_replay_rejects_unavailable_nonfixed_non_ntfs_and_low_space",
            "test_local_replay_rejects_collision_reparse_and_path_traversal",
            "test_local_replay_manifest_rejects_bytes_or_sha_drift",
            "test_local_replay_commands_bind_every_runner_path_to_workspace",
        ),
        "local replay routing tests",
        errors,
    )
    production = _read(PRODUCTION_INVENTORY)
    lifecycle = _read(LIFECYCLE_INVENTORY)
    for path in (
        "scripts/run_local_daily_full_validation_replay.py",
        "scripts/validate_local_daily_full_validation_replay.py",
    ):
        if path not in production:
            errors.append(f"production inventory missing local replay path: {path}")
        if path not in lifecycle:
            errors.append(f"lifecycle inventory missing local replay path: {path}")
    return errors


def main() -> int:
    errors = validate()
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1
    print(
        "local Daily Full validation replay F-routing contract passed: "
        f"root={APPROVED_ROOT} c_temp_fallback=false"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
