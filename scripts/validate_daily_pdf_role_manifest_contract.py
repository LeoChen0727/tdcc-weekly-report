from __future__ import annotations

import ast
import csv
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ENTRYPOINT = ROOT / "scripts" / "run_chatgpt_daily_report_entrypoint.py"
REPLAY_VALIDATOR = ROOT / "scripts" / "validate_chatgpt_daily_report_new_conversation_replay.py"
REGRESSION_CONTRACT = ROOT / "config" / "daily_pdf_rendered_model_regression_contract.csv"
DAILY_WORKFLOW = ROOT / ".github" / "workflows" / "daily_full_pipeline.yml"
PR_WORKFLOW = ROOT / ".github" / "workflows" / "daily_model_maintenance_pr_validation.yml"

EXPECTED_PDF_ROLES = [
    "mainstream_highlight",
    "mainstream_full",
    "non_mainstream_highlight",
    "non_mainstream_full",
    "warrant_market_auxiliary",
    "market_risk_background",
]

BANNED_REPLAY_SNIPPETS = {
    "EXPECTED_TITLES": "replay validation must not require PDF Chinese title tokens",
    "HIGHLIGHT_LAYOUT_TITLES": "highlight layout validation must use pdf_role, not title tokens",
    "HIGHLIGHT_LAYOUT_ROLE_TITLES": "highlight layout validation must not map roles through titles",
    "PDF_ROLE_TITLE_TOKENS": "replay validation must not map PDF roles from title tokens",
    "title_to_pages": "PDF page text maps must be keyed by pdf_role, not title text",
    "matched_title": "PDF role validation must not carry matched title state",
    "rendered_model_regression_pdf_role": "rendered model regression must not infer roles from filenames",
    "for role, title in": "PDF role matching must not iterate role/title substring pairs",
}

REQUIRED_RENDERED_REGRESSION_CONTRACT_IDS = {
    "volume_range_breakout_mainstream_highlight_structure",
    "volume_range_breakout_non_mainstream_highlight_structure",
    "volume_range_breakout_mainstream_highlight_20260703",
    "volume_range_breakout_non_mainstream_highlight_empty_20260703",
    "w_bottom_right_side_mainstream_highlight_structure",
    "w_bottom_right_side_non_mainstream_highlight_structure",
    "w_bottom_right_side_mainstream_highlight_20260703",
    "w_bottom_right_side_non_mainstream_highlight_20260703",
    "neckline_volume_breakout_confirmation_mainstream_highlight_structure",
    "neckline_volume_breakout_confirmation_non_mainstream_highlight_structure",
    "neckline_volume_breakout_confirmation_mainstream_highlight_empty_20260703",
    "neckline_volume_breakout_confirmation_non_mainstream_highlight_empty_20260703",
    "price_pullback_23ema_mainstream_highlight_structure",
    "price_pullback_23ema_non_mainstream_highlight_structure",
    "price_pullback_23ema_mainstream_highlight_20260703",
    "price_pullback_23ema_non_mainstream_highlight_20260703",
}


def rel(path: Path) -> str:
    try:
        return path.relative_to(ROOT).as_posix()
    except ValueError:
        return path.as_posix()


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace")


def literal_assigned_to(tree: ast.AST, name: str) -> object | None:
    for node in ast.walk(tree):
        if not isinstance(node, ast.Assign):
            continue
        if any(isinstance(target, ast.Name) and target.id == name for target in node.targets):
            try:
                return ast.literal_eval(node.value)
            except Exception:
                return None
    return None


def function_node(tree: ast.AST, name: str) -> ast.FunctionDef | None:
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef) and node.name == name:
            return node
    return None


def call_names(node: ast.AST) -> set[str]:
    names: set[str] = set()
    for child in ast.walk(node):
        if not isinstance(child, ast.Call):
            continue
        func = child.func
        if isinstance(func, ast.Name):
            names.add(func.id)
        elif isinstance(func, ast.Attribute):
            names.add(func.attr)
    return names


def validate_entrypoint_manifest_contract() -> list[str]:
    errors: list[str] = []
    tree = ast.parse(read_text(ENTRYPOINT), filename=rel(ENTRYPOINT))

    roles = literal_assigned_to(tree, "PDF_OUTPUT_ROLES")
    if list(roles or []) != EXPECTED_PDF_ROLES:
        errors.append(
            f"{rel(ENTRYPOINT)} PDF_OUTPUT_ROLES must be exactly {EXPECTED_PDF_ROLES}, got {roles!r}"
        )

    helper = function_node(tree, "pdf_outputs_for_manifest")
    if helper is None:
        errors.append(f"{rel(ENTRYPOINT)} missing pdf_outputs_for_manifest()")
    else:
        helper_text = ast.get_source_segment(read_text(ENTRYPOINT), helper) or ""
        for token in ("pdf_role", "pdf_index", "path", "PDF_OUTPUT_ROLES"):
            if token not in helper_text:
                errors.append(f"{rel(ENTRYPOINT)} pdf_outputs_for_manifest() missing token {token!r}")

    writer = function_node(tree, "write_runtime_manifest")
    if writer is None:
        errors.append(f"{rel(ENTRYPOINT)} missing write_runtime_manifest()")
    else:
        writer_text = ast.get_source_segment(read_text(ENTRYPOINT), writer) or ""
        if '"pdf_outputs"' not in writer_text and "'pdf_outputs'" not in writer_text:
            errors.append(f"{rel(ENTRYPOINT)} write_runtime_manifest() must write pdf_outputs")
        if "pdf_outputs_for_manifest" not in call_names(writer):
            errors.append(f"{rel(ENTRYPOINT)} write_runtime_manifest() must call pdf_outputs_for_manifest()")

    return errors


def validate_replay_manifest_contract() -> list[str]:
    errors: list[str] = []
    replay_text = read_text(REPLAY_VALIDATOR)
    tree = ast.parse(replay_text, filename=rel(REPLAY_VALIDATOR))

    roles = literal_assigned_to(tree, "EXPECTED_PDF_ROLES")
    if list(roles or []) != EXPECTED_PDF_ROLES:
        errors.append(
            f"{rel(REPLAY_VALIDATOR)} EXPECTED_PDF_ROLES must be exactly {EXPECTED_PDF_ROLES}, got {roles!r}"
        )

    for snippet, reason in BANNED_REPLAY_SNIPPETS.items():
        if snippet in replay_text:
            errors.append(f"{rel(REPLAY_VALIDATOR)} contains banned snippet {snippet!r}: {reason}")

    for function_name in (
        "validate_pdf_highlight_layout_contract",
        "validate_rendered_model_regression_contract",
    ):
        node = function_node(tree, function_name)
        if node is None:
            errors.append(f"{rel(REPLAY_VALIDATOR)} missing {function_name}()")
            continue
        names = call_names(node)
        if "role_to_pdf_paths_from_manifest" not in names:
            errors.append(f"{rel(REPLAY_VALIDATOR)} {function_name}() must use role_to_pdf_paths_from_manifest()")
        function_text = ast.get_source_segment(replay_text, node) or ""
        if ".name" in function_text:
            errors.append(f"{rel(REPLAY_VALIDATOR)} {function_name}() must not inspect path.name for role matching")

    runtime_validator = function_node(tree, "validate_runtime_manifest")
    if runtime_validator is None:
        errors.append(f"{rel(REPLAY_VALIDATOR)} missing validate_runtime_manifest()")
    else:
        runtime_text = ast.get_source_segment(replay_text, runtime_validator) or ""
        for token in (
            "pdf_outputs",
            "EXPECTED_PDF_ROLES",
            "pdf_index",
            "role_to_pdf_paths_from_manifest",
            "pdf_outputs roles do not match expected order",
            "pdf_outputs paths do not match emitted PDF paths",
        ):
            if token not in runtime_text:
                errors.append(f"{rel(REPLAY_VALIDATOR)} validate_runtime_manifest() missing token {token!r}")

    return errors


def validate_rendered_regression_contract_roles() -> list[str]:
    errors: list[str] = []
    if not REGRESSION_CONTRACT.exists():
        return [f"missing rendered model regression contract: {rel(REGRESSION_CONTRACT)}"]
    with REGRESSION_CONTRACT.open(newline="", encoding="utf-8-sig") as handle:
        rows = list(csv.DictReader(handle))
    active_contract_ids = {
        str(row.get("contract_id", "")).strip()
        for row in rows
        if str(row.get("active", "")).strip().lower() in {"true", "1", "yes", "y"}
    }
    missing_contract_ids = sorted(REQUIRED_RENDERED_REGRESSION_CONTRACT_IDS - active_contract_ids)
    for contract_id in missing_contract_ids:
        errors.append(f"{rel(REGRESSION_CONTRACT)} missing required active contract_id={contract_id!r}")
    for index, row in enumerate(rows, start=2):
        role = str(row.get("pdf_role", "")).strip()
        if role and role not in EXPECTED_PDF_ROLES:
            errors.append(f"{rel(REGRESSION_CONTRACT)}:{index} unknown pdf_role={role!r}")
        active = str(row.get("active", "")).strip().lower() in {"true", "1", "yes", "y"}
        model_id = str(row.get("model_id", "")).strip()
        report_date = str(row.get("report_date", "")).strip()
        required_stock_ids = [
            token.strip()
            for token in str(row.get("required_stock_ids", "") or "").replace(";", "|").split("|")
            if token.strip()
        ]
        if active and model_id == "price_pullback_23ema" and report_date not in {"", "*"} and required_stock_ids:
            errors.append(
                f"{rel(REGRESSION_CONTRACT)}:{index} price_pullback_23ema date-specific regression rows "
                "must not require dynamic candidate stock ids; use stable text tokens and forbidden_stock_ids"
            )
    return errors


def validate_workflow_hooks() -> list[str]:
    errors: list[str] = []
    command = "python scripts/validate_daily_pdf_role_manifest_contract.py"
    for workflow in (DAILY_WORKFLOW, PR_WORKFLOW):
        text = read_text(workflow)
        if command not in text:
            errors.append(f"{rel(workflow)} must run {command}")
    return errors


def validate() -> list[str]:
    errors: list[str] = []
    for path in (ENTRYPOINT, REPLAY_VALIDATOR, REGRESSION_CONTRACT, DAILY_WORKFLOW, PR_WORKFLOW):
        if not path.exists():
            errors.append(f"missing required daily PDF role manifest contract file: {rel(path)}")
    if errors:
        return errors

    errors.extend(validate_entrypoint_manifest_contract())
    errors.extend(validate_replay_manifest_contract())
    errors.extend(validate_rendered_regression_contract_roles())
    errors.extend(validate_workflow_hooks())
    return errors


def main() -> int:
    errors = validate()
    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1

    print("daily PDF role manifest contract validation passed")
    print(f"validated_roles={';'.join(EXPECTED_PDF_ROLES)}")
    print(f"validated_entrypoint={rel(ENTRYPOINT)}")
    print(f"validated_replay={rel(REPLAY_VALIDATOR)}")
    print(f"validated_contract={rel(REGRESSION_CONTRACT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
