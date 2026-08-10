from __future__ import annotations

import ast
import csv
import sys
from pathlib import Path

try:
    from scripts.validate_local_daily_full_validation_replay import (
        validate as validate_local_daily_full_validation_replay,
    )
except ModuleNotFoundError:
    from validate_local_daily_full_validation_replay import (
        validate as validate_local_daily_full_validation_replay,
    )


ROOT = Path(__file__).resolve().parents[1]
CONTRACT = ROOT / "config" / "git_worktree_materialization_contract.csv"
SAFETY_MODULE = ROOT / "scripts" / "git_worktree_safety.py"
WORKFLOW = ROOT / ".github" / "workflows" / "daily_model_maintenance_pr_validation.yml"
AGENTS = ROOT / "AGENTS.md"

REQUIRED_COLUMNS = {
    "consumer_id",
    "entrypoint",
    "materialization_mode",
    "checkout_workers",
    "max_concurrent",
    "temp_root_policy",
    "approved_destination_root",
    "approved_root_filesystem",
    "default_destination_policy",
    "minimum_free_bytes",
    "purpose",
}
EXPECTED_FULL_CONSUMERS = {
    "chatgpt_daily_report_entrypoint": "scripts/run_chatgpt_daily_report_entrypoint.py",
    "tdcc_weekly_report_entrypoint": "scripts/run_tdcc_weekly_report_entrypoint.py",
    "chatgpt_daily_report_new_conversation_replay": "scripts/validate_chatgpt_daily_report_new_conversation_replay.py",
}
EXPECTED_SPARSE_CONSUMER = {
    "sparse_task_worktree": "scripts/git_worktree_safety.py",
}
EXPECTED_LOCAL_REPLAY_CONSUMER = {
    "local_daily_full_validation_replay": "scripts/run_local_daily_full_validation_replay.py",
}
EXPECTED_CONSUMERS = {
    **EXPECTED_FULL_CONSUMERS,
    **EXPECTED_SPARSE_CONSUMER,
    **EXPECTED_LOCAL_REPLAY_CONSUMER,
}
APPROVED_SPARSE_ROOT = r"F:\CodexStorage\task-worktrees\taiwan-stock-recommendation"
APPROVED_LOCAL_REPLAY_ROOT = r"F:\CodexStorage\validation-replay-workspaces\taiwan-stock-recommendation"
DEFAULT_DESTINATION_POLICY = "approved_root_task_child"
LOCAL_REPLAY_DESTINATION_POLICY = "approved_root_task_or_run_child"
MINIMUM_FREE_BYTES = "10737418240"
LOCAL_REPLAY_MINIMUM_FREE_BYTES = "21474836480"


def _literal_words(node: ast.AST) -> list[str]:
    if not isinstance(node, (ast.List, ast.Tuple)):
        return []
    words: list[str] = []
    for item in node.elts:
        if isinstance(item, ast.Constant) and isinstance(item.value, str):
            words.append(item.value.strip().lower())
        else:
            words.append("")
    return words


def _contains_sequence(words: list[str], sequence: tuple[str, ...]) -> bool:
    width = len(sequence)
    return any(tuple(words[index : index + width]) == sequence for index in range(len(words) - width + 1))


def _raw_materialization_calls(path: Path) -> list[str]:
    try:
        tree = ast.parse(path.read_text(encoding="utf-8-sig"), filename=str(path))
    except (OSError, SyntaxError) as exc:
        return [f"cannot parse {path.relative_to(ROOT).as_posix()}: {exc}"]
    errors: list[str] = []
    for node in ast.walk(tree):
        words = _literal_words(node)
        if not words:
            continue
        if _contains_sequence(words, ("git", "worktree", "add")):
            errors.append(f"raw git worktree add is forbidden at line {getattr(node, 'lineno', '?')}")
        if _contains_sequence(words, ("git", "switch")) or _contains_sequence(words, ("git", "checkout")):
            errors.append(f"raw git ref transition is forbidden at line {getattr(node, 'lineno', '?')}")
    return errors


def validate() -> list[str]:
    errors: list[str] = []
    if not CONTRACT.exists():
        return [f"missing contract: {CONTRACT.relative_to(ROOT).as_posix()}"]

    with CONTRACT.open("r", encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle)
        columns = set(reader.fieldnames or [])
        rows = [dict(row) for row in reader]
    missing = REQUIRED_COLUMNS - columns
    if missing:
        errors.append(f"materialization contract missing columns: {sorted(missing)}")

    seen: set[str] = set()
    actual: dict[str, str] = {}
    for line_no, row in enumerate(rows, start=2):
        consumer_id = row.get("consumer_id", "").strip()
        entrypoint = row.get("entrypoint", "").strip().replace("\\", "/")
        if not consumer_id or consumer_id in seen:
            errors.append(f"contract row {line_no} has empty or duplicate consumer_id: {consumer_id!r}")
            continue
        seen.add(consumer_id)
        actual[consumer_id] = entrypoint
        if row.get("checkout_workers", "").strip() != "1":
            errors.append(f"{consumer_id}: checkout_workers must be 1")
        if row.get("max_concurrent", "").strip() != "1":
            errors.append(f"{consumer_id}: max_concurrent must be 1")
        if not row.get("purpose", "").strip():
            errors.append(f"{consumer_id}: purpose is required")
        entrypoint_path = ROOT / entrypoint
        if not entrypoint_path.exists():
            errors.append(f"{consumer_id}: missing entrypoint {entrypoint}")
            continue
        text = entrypoint_path.read_text(encoding="utf-8-sig")
        if consumer_id in EXPECTED_FULL_CONSUMERS:
            if row.get("materialization_mode", "").strip() != "full_temp_only":
                errors.append(f"{consumer_id}: registered full consumers must use full_temp_only")
            if row.get("temp_root_policy", "").strip() != "system_temp_only":
                errors.append(f"{consumer_id}: full consumers must stay system_temp_only")
            if row.get("approved_destination_root", "").strip() or row.get(
                "approved_root_filesystem", ""
            ).strip() or row.get("default_destination_policy", "").strip() or row.get(
                "minimum_free_bytes", ""
            ).strip():
                errors.append(f"{consumer_id}: full consumers must not define an approved external root")
            if "create_registered_full_temp_worktree" not in text or consumer_id not in text:
                errors.append(f"{consumer_id}: entrypoint must call the guarded full-temp helper")
        elif consumer_id in EXPECTED_SPARSE_CONSUMER:
            if row.get("materialization_mode", "").strip() != "sparse_task_only":
                errors.append(f"{consumer_id}: sparse task consumer must use sparse_task_only")
            if row.get("temp_root_policy", "").strip() != "system_temp_or_approved_root":
                errors.append(
                    f"{consumer_id}: sparse task consumer must use system_temp_or_approved_root"
                )
            if row.get("approved_destination_root", "").strip().lower().rstrip("\\/") != (
                APPROVED_SPARSE_ROOT.lower()
            ):
                errors.append(
                    f"{consumer_id}: approved_destination_root must be exactly {APPROVED_SPARSE_ROOT}"
                )
            if row.get("approved_root_filesystem", "").strip().upper() != "NTFS":
                errors.append(f"{consumer_id}: approved_root_filesystem must be NTFS")
            if row.get("default_destination_policy", "").strip() != DEFAULT_DESTINATION_POLICY:
                errors.append(
                    f"{consumer_id}: default_destination_policy must be {DEFAULT_DESTINATION_POLICY}"
                )
            if row.get("minimum_free_bytes", "").strip() != MINIMUM_FREE_BYTES:
                errors.append(
                    f"{consumer_id}: minimum_free_bytes must be {MINIMUM_FREE_BYTES}"
                )
        elif consumer_id in EXPECTED_LOCAL_REPLAY_CONSUMER:
            expected = {
                "materialization_mode": "full_local_validation_replay_only",
                "temp_root_policy": "approved_root_only",
                "approved_destination_root": APPROVED_LOCAL_REPLAY_ROOT,
                "approved_root_filesystem": "NTFS",
                "default_destination_policy": LOCAL_REPLAY_DESTINATION_POLICY,
                "minimum_free_bytes": LOCAL_REPLAY_MINIMUM_FREE_BYTES,
            }
            for key, expected_value in expected.items():
                observed = row.get(key, "").strip()
                if key == "approved_destination_root":
                    observed = observed.lower().rstrip("\\/")
                    expected_value = expected_value.lower().rstrip("\\/")
                if observed != expected_value:
                    errors.append(f"{consumer_id}: {key} must be {expected_value}")
            if (
                "create_registered_full_local_validation_replay_worktree" not in text
                or consumer_id not in text
            ):
                errors.append(
                    f"{consumer_id}: entrypoint must call the guarded F-only full helper"
                )
        else:
            errors.append(f"unexpected worktree materialization consumer: {consumer_id}")

    if actual != EXPECTED_CONSUMERS:
        errors.append(f"worktree materialization consumer set drifted: expected={EXPECTED_CONSUMERS}, actual={actual}")

    safety_text = SAFETY_MODULE.read_text(encoding="utf-8-sig") if SAFETY_MODULE.exists() else ""
    for token in (
        "--no-checkout",
        "checkout.workers=1",
        "checkout_materialization_lock",
        "sparse-checkout",
        "PROTECTED_MATERIALIZATION_PREFIXES",
        "APPROVED_SPARSE_DESTINATION_ROOT_WINDOWS",
        "approved_root_filesystem",
        "FILE_ATTRIBUTE_REPARSE_POINT",
        "worktree destination must not be a drive root",
        "default_approved_root",
        "--task-name",
        "insufficient free space",
        "APPROVED_LOCAL_VALIDATION_REPLAY_ROOT_WINDOWS",
        "WINDOWS_FIXED_DRIVE_TYPE",
        "full_local_validation_replay_only",
    ):
        if token not in safety_text:
            errors.append(f"git worktree safety module missing required token: {token}")

    for path in sorted((ROOT / "scripts").glob("*.py")):
        if path in {SAFETY_MODULE, Path(__file__).resolve()}:
            continue
        for error in _raw_materialization_calls(path):
            errors.append(f"{path.relative_to(ROOT).as_posix()}: {error}")

    agents_text = AGENTS.read_text(encoding="utf-8-sig") if AGENTS.exists() else ""
    for token in (
        "Fixed Worktree Ref Transition Safety Rule",
        "scripts/git_worktree_safety.py audit",
        "scripts/git_worktree_safety.py create-sparse",
        "Do not run `git",
        "`git checkout`",
        "`git reset --hard`",
    ):
        if token not in agents_text:
            errors.append(f"AGENTS.md missing fixed-worktree safety rule token: {token}")

    workflow_text = WORKFLOW.read_text(encoding="utf-8-sig") if WORKFLOW.exists() else ""
    for token in (
        "python scripts/validate_git_worktree_safety.py",
        "tests/test_git_worktree_safety.py",
    ):
        if token not in workflow_text:
            errors.append(f"daily model PR workflow missing checkout safety validation: {token}")
    errors.extend(
        f"local validation replay routing: {error}"
        for error in validate_local_daily_full_validation_replay()
    )
    return errors


def main() -> int:
    errors = validate()
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1
    print("git worktree materialization safety validation passed")
    print(f"registered_full_consumers={len(EXPECTED_FULL_CONSUMERS)}")
    print(f"registered_sparse_consumers={len(EXPECTED_SPARSE_CONSUMER)}")
    print(
        "registered_local_validation_replay_consumers="
        f"{len(EXPECTED_LOCAL_REPLAY_CONSUMER)}"
    )
    print(f"approved_sparse_root={APPROVED_SPARSE_ROOT}")
    print(f"default_destination_policy={DEFAULT_DESTINATION_POLICY}")
    print(f"minimum_free_bytes={MINIMUM_FREE_BYTES}")
    print("checkout_workers=1")
    print("max_concurrent_materializations=1")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
