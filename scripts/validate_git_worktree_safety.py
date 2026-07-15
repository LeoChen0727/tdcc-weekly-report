from __future__ import annotations

import ast
import csv
import sys
from pathlib import Path


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
    "purpose",
}
EXPECTED_CONSUMERS = {
    "chatgpt_daily_report_entrypoint": "scripts/run_chatgpt_daily_report_entrypoint.py",
    "tdcc_weekly_report_entrypoint": "scripts/run_tdcc_weekly_report_entrypoint.py",
    "chatgpt_daily_report_new_conversation_replay": "scripts/validate_chatgpt_daily_report_new_conversation_replay.py",
}


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
        if row.get("materialization_mode", "").strip() != "full_temp_only":
            errors.append(f"{consumer_id}: only full_temp_only is allowed for registered full consumers")
        if row.get("checkout_workers", "").strip() != "1":
            errors.append(f"{consumer_id}: checkout_workers must be 1")
        if row.get("max_concurrent", "").strip() != "1":
            errors.append(f"{consumer_id}: max_concurrent must be 1")
        if row.get("temp_root_policy", "").strip() != "system_temp_only":
            errors.append(f"{consumer_id}: temp_root_policy must be system_temp_only")
        if not row.get("purpose", "").strip():
            errors.append(f"{consumer_id}: purpose is required")
        entrypoint_path = ROOT / entrypoint
        if not entrypoint_path.exists():
            errors.append(f"{consumer_id}: missing entrypoint {entrypoint}")
            continue
        text = entrypoint_path.read_text(encoding="utf-8-sig")
        if "create_registered_full_temp_worktree" not in text or consumer_id not in text:
            errors.append(f"{consumer_id}: entrypoint must call the guarded full-temp helper")

    if actual != EXPECTED_CONSUMERS:
        errors.append(f"full worktree consumer set drifted: expected={EXPECTED_CONSUMERS}, actual={actual}")

    safety_text = SAFETY_MODULE.read_text(encoding="utf-8-sig") if SAFETY_MODULE.exists() else ""
    for token in (
        "--no-checkout",
        "checkout.workers=1",
        "checkout_materialization_lock",
        "sparse-checkout",
        "PROTECTED_MATERIALIZATION_PREFIXES",
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
    return errors


def main() -> int:
    errors = validate()
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1
    print("git worktree materialization safety validation passed")
    print(f"registered_full_consumers={len(EXPECTED_CONSUMERS)}")
    print("checkout_workers=1")
    print("max_concurrent_materializations=1")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
