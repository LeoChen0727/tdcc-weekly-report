from __future__ import annotations

import ast
from dataclasses import dataclass
import os
import re
from pathlib import Path
from typing import Iterable


ROOT = Path(__file__).resolve().parents[1]
WORKFLOW = ROOT / ".github" / "workflows" / "daily_full_pipeline.yml"
PR_VALIDATION_WORKFLOW = ROOT / ".github" / "workflows" / "daily_model_maintenance_pr_validation.yml"
ENTRYPOINT = ROOT / "scripts" / "run_chatgpt_daily_report_entrypoint.py"
WORKTREE_SAFETY = ROOT / "scripts" / "git_worktree_safety.py"
RENDERER = ROOT / "scripts" / "generate_chatgpt_side_daily_reports.py"
PACKET_BUILDER = ROOT / "build_chatgpt_daily_report_packet.py"
DAILY_MARKET_ARTIFACT_BUILDER = ROOT / "build_daily_market_report_artifacts.py"
ALIAS_ENSURER = ROOT / "ensure_report_aliases.py"
README_PUBLISHER = ROOT / "publish_chatgpt_report_readme_and_check.py"
REPLAY_VALIDATOR = ROOT / "scripts" / "validate_chatgpt_daily_report_new_conversation_replay.py"

OFFICIAL_ENTRYPOINT_WORKTREE_HELPER = "create_registered_full_temp_worktree"
OFFICIAL_ENTRYPOINT_WORKTREE_CONSUMER = "chatgpt_daily_report_entrypoint"

CHATGPT_DAILY_DFKAI_FONT_PATH_ENV = "CHATGPT_DAILY_DFKAI_FONT_PATH"
CHATGPT_DAILY_DEFAULT_DFKAI_FONT_PATH = Path(r"C:\Windows\Fonts\kaiu.ttf")
CHATGPT_DAILY_PDF_FONT_NAME = "DFKai-SB"
EXPECTED_WINDOWS_DFKAI_CAPABILITY_NAME = "Language.Fonts.Hant~~~und-HANT~0.0.1.0"
EXPECTED_WINDOWS_DFKAI_INSTALL_DETAIL_LIMIT = 2000
TRADITIONAL_CHINESE_GLYPH_CANARY = "標楷體繁體中文測試買賣停損勝敗本日無股票推薦"
DFKAI_NAME_TABLE_TOKENS = {"DFKai-SB", "DFKaiShu-SB-Estd-BF"}
DFKAI_PDF_BASE_FONTS = {"/DFKai-SB", "/DFKaiShu-SB-Estd-BF"}
LEGACY_DAILY_HISTORY_ALIAS_LITERALS = (
    "{main_date}_每日全市場候選股監測報告_精華版.md",
    "{main_date}_每日全市場候選股監測報告_精華版.pdf",
    "{main_date}_完整候選股清單_完整版.md",
    "{main_date}_完整候選股清單_完整版表格.pdf",
)
FORBIDDEN_DAILY_PDF_FONT_TOKENS = (
    "MSung-Light",
    "MSung",
    "STSong-Light",
    "STSong",
    "UniGB-UCS2-H",
    "UniGB",
    "TW-Kai",
)

CHATGPT_SIDE_BUILDERS = (
    "build_mainstream_curated_pdf",
    "build_mainstream_full_candidate_pdf",
    "build_non_mainstream_curated_pdf",
    "build_non_mainstream_full_candidate_pdf",
    "build_warrant_market_auxiliary_pdf",
    "build_market_risk_background_pdf",
)

RETIRED_FIXED_PDF_FILENAMES = (
    "daily_market_curated_report_latest.pdf",
    "daily_market_full_table_report_latest.pdf",
    "mainstream_daily_recommendation_highlight_latest.pdf",
    "mainstream_full_candidate_list_latest.pdf",
    "non_mainstream_daily_recommendation_highlight_latest.pdf",
    "non_mainstream_full_candidate_list_latest.pdf",
)

RETIRED_PUBLIC_PDF_FILENAMES = (
    *RETIRED_FIXED_PDF_FILENAMES,
    "warrant_market_report_latest.pdf",
    "market_risk_dashboard_latest.pdf",
)

FORBIDDEN_WORKFLOW_LITERALS = (
    "python scripts/generate_daily_market_pdf.py",
    "python scripts/validate_daily_market_report.py",
    "Generate fixed daily market PDF reports",
    "Validate fixed daily market PDF reports",
)


@dataclass(frozen=True)
class PdfFontRecord:
    base_font: str
    encoding: str
    embedded: bool
    to_unicode: bool


def read_text(path: Path) -> str:
    if not path.exists():
        raise FileNotFoundError(path)
    return path.read_text(encoding="utf-8", errors="replace")


def daily_model_pr_scope_contract_errors(text: str) -> list[str]:
    errors: list[str] = []
    trigger = text.split("\njobs:", 1)[0]
    lines = trigger.splitlines()
    try:
        pull_request_index = lines.index("  pull_request:")
    except ValueError:
        errors.append("daily model PR validation must trigger on every pull request")
    else:
        nested = []
        for line in lines[pull_request_index + 1 :]:
            if not line.strip():
                continue
            if len(line) - len(line.lstrip()) <= 2:
                break
            nested.append(line.strip())
        if nested:
            errors.append(
                "daily model PR validation pull_request trigger must remain unfiltered"
            )
    for literal in (
        "  workflow_dispatch:",
        "  scope:",
        "python scripts/detect_daily_model_pr_validation_scope.py",
        "  daily-model-maintenance-pr-validation:",
    ):
        if literal not in text:
            errors.append(f"daily model PR validation missing scope contract: {literal}")
    return errors


def official_entrypoint_worktree_contract_errors(source: str) -> list[str]:
    errors: list[str] = []
    try:
        tree = ast.parse(source)
    except SyntaxError as exc:
        return [f"official entrypoint is not valid Python: {exc}"]

    helper_imported = any(
        isinstance(node, ast.ImportFrom)
        and node.module == "scripts.git_worktree_safety"
        and any(alias.name == OFFICIAL_ENTRYPOINT_WORKTREE_HELPER for alias in node.names)
        for node in tree.body
    )
    if not helper_imported:
        errors.append(
            "official entrypoint must import registered full-temp worktree helper: "
            f"{OFFICIAL_ENTRYPOINT_WORKTREE_HELPER}"
        )

    add_source_worktree = next(
        (
            node
            for node in tree.body
            if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)) and node.name == "add_source_worktree"
        ),
        None,
    )
    if add_source_worktree is None:
        errors.append("official entrypoint must define add_source_worktree()")
        return errors

    helper_calls = [
        node
        for node in ast.walk(add_source_worktree)
        if isinstance(node, ast.Call)
        and isinstance(node.func, ast.Name)
        and node.func.id == OFFICIAL_ENTRYPOINT_WORKTREE_HELPER
    ]
    if len(helper_calls) != 1:
        errors.append(
            "official entrypoint add_source_worktree() must call registered full-temp worktree helper exactly once: "
            f"observed={len(helper_calls)}"
        )
        return errors

    consumer_keyword = next(
        (keyword for keyword in helper_calls[0].keywords if keyword.arg == "consumer_id"),
        None,
    )
    consumer_value = consumer_keyword.value if consumer_keyword is not None else None
    if not (
        isinstance(consumer_value, ast.Constant)
        and consumer_value.value == OFFICIAL_ENTRYPOINT_WORKTREE_CONSUMER
    ):
        errors.append(
            "official entrypoint must bind the registered full-temp worktree helper to exact consumer_id: "
            f"{OFFICIAL_ENTRYPOINT_WORKTREE_CONSUMER}"
        )
    return errors


def function_text(text: str, name: str) -> str:
    match = re.search(rf"^def {re.escape(name)}\(", text, flags=re.MULTILINE)
    if not match:
        raise ValueError(name)
    start = match.start()
    next_match = re.search(r"^def \w+\(", text[start + 1 :], flags=re.MULTILINE)
    if not next_match:
        return text[start:]
    return text[start : start + 1 + next_match.start()]


def official_entrypoint_dfkai_preflight_contract_errors(source: str) -> list[str]:
    errors: list[str] = []
    try:
        tree = ast.parse(source)
    except SyntaxError as exc:
        return [f"official entrypoint is not valid Python: {exc}"]

    helper_definitions = [
        node
        for node in tree.body
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef))
        and node.name == "ensure_local_dfkai_font_for_pdf_rendering"
    ]
    if len(helper_definitions) != 1:
        return [
            "official entrypoint must define exactly one module-level "
            "ensure_local_dfkai_font_for_pdf_rendering(): "
            f"observed={len(helper_definitions)}"
        ]
    helper = helper_definitions[0]

    if CHATGPT_DAILY_DEFAULT_DFKAI_FONT_PATH != Path(r"C:\Windows\Fonts\kaiu.ttf"):
        errors.append("official DFKai canonical font path must remain C:\\Windows\\Fonts\\kaiu.ttf")
    canonical_font_imported = any(
        isinstance(node, ast.ImportFrom)
        and node.module == "scripts.validate_chatgpt_side_pdf_contract"
        and any(alias.name == "CHATGPT_DAILY_DEFAULT_DFKAI_FONT_PATH" for alias in node.names)
        for node in tree.body
    )
    kwonly_names = [argument.arg for argument in helper.args.kwonlyargs]
    canonical_default = None
    if "default_font_path" in kwonly_names:
        canonical_default = helper.args.kw_defaults[kwonly_names.index("default_font_path")]
    if not (
        canonical_font_imported
        and isinstance(canonical_default, ast.Name)
        and canonical_default.id == "CHATGPT_DAILY_DEFAULT_DFKAI_FONT_PATH"
    ):
        errors.append(
            "official DFKai local preflight must use the imported canonical C:\\Windows\\Fonts\\kaiu.ttf default"
        )
    validator_default = None
    if "validator" in kwonly_names:
        validator_default = helper.args.kw_defaults[kwonly_names.index("validator")]
    validate_dfkai_imported = any(
        isinstance(node, ast.ImportFrom)
        and node.module == "scripts.validate_chatgpt_side_pdf_contract"
        and any(alias.name == "validate_dfkai_font_file" for alias in node.names)
        for node in tree.body
    )
    if not (
        validate_dfkai_imported
        and isinstance(validator_default, ast.Name)
        and validator_default.id == "validate_dfkai_font_file"
    ):
        errors.append(
            "official DFKai local preflight default validator must remain validate_dfkai_font_file"
        )

    capability_assignments = [
        node
        for node in tree.body
        if isinstance(node, ast.Assign)
        and len(node.targets) == 1
        and isinstance(node.targets[0], ast.Name)
        and node.targets[0].id == "WINDOWS_DFKAI_CAPABILITY_NAME"
    ]
    if (
        len(capability_assignments) != 1
        or not isinstance(capability_assignments[0].value, ast.Constant)
        or capability_assignments[0].value.value != EXPECTED_WINDOWS_DFKAI_CAPABILITY_NAME
    ):
        errors.append(
            "official DFKai local preflight must bind WINDOWS_DFKAI_CAPABILITY_NAME to the exact "
            f"Traditional Chinese font capability: {EXPECTED_WINDOWS_DFKAI_CAPABILITY_NAME}"
        )
    detail_limit_assignments = [
        node
        for node in tree.body
        if isinstance(node, ast.Assign)
        and len(node.targets) == 1
        and isinstance(node.targets[0], ast.Name)
        and node.targets[0].id == "WINDOWS_DFKAI_INSTALL_DETAIL_LIMIT"
    ]
    if (
        len(detail_limit_assignments) != 1
        or not isinstance(detail_limit_assignments[0].value, ast.Constant)
        or detail_limit_assignments[0].value.value != EXPECTED_WINDOWS_DFKAI_INSTALL_DETAIL_LIMIT
    ):
        errors.append(
            "official DFKai local preflight must keep bounded DISM diagnostic detail at 2000 characters"
        )

    def named_call(node: ast.AST, name: str) -> bool:
        return isinstance(node, ast.Call) and isinstance(node.func, ast.Name) and node.func.id == name

    def path_exists_call(node: ast.AST) -> bool:
        return (
            isinstance(node, ast.Call)
            and isinstance(node.func, ast.Attribute)
            and node.func.attr == "exists"
            and isinstance(node.func.value, ast.Name)
            and node.func.value.id == "path"
            and not node.args
            and not node.keywords
        )

    def compare_names(node: ast.AST, left: str, operator: type[ast.cmpop], right: str) -> bool:
        return (
            isinstance(node, ast.Compare)
            and isinstance(node.left, ast.Name)
            and node.left.id == left
            and len(node.ops) == 1
            and isinstance(node.ops[0], operator)
            and len(node.comparators) == 1
            and isinstance(node.comparators[0], ast.Name)
            and node.comparators[0].id == right
        )

    def compare_name_constant(
        node: ast.AST,
        left: str,
        operator: type[ast.cmpop],
        right: object,
    ) -> bool:
        return (
            isinstance(node, ast.Compare)
            and isinstance(node.left, ast.Name)
            and node.left.id == left
            and len(node.ops) == 1
            and isinstance(node.ops[0], operator)
            and len(node.comparators) == 1
            and isinstance(node.comparators[0], ast.Constant)
            and node.comparators[0].value == right
        )

    def direct_assign_call(statement: ast.stmt, target: str, call_name: str) -> ast.Call | None:
        if not (
            isinstance(statement, ast.Assign)
            and len(statement.targets) == 1
            and isinstance(statement.targets[0], ast.Name)
            and statement.targets[0].id == target
            and named_call(statement.value, call_name)
        ):
            return None
        return statement.value

    def direct_terminal(body: list[ast.stmt], terminal_type: type[ast.stmt]) -> bool:
        return bool(body) and isinstance(body[-1], terminal_type)

    def statement_suite_positions(root: ast.AST) -> dict[int, tuple[ast.AST, str, int]]:
        positions: dict[int, tuple[ast.AST, str, int]] = {}

        def visit(owner: ast.AST) -> None:
            for field, value in ast.iter_fields(owner):
                if isinstance(value, list):
                    for index, child in enumerate(value):
                        if isinstance(child, ast.stmt):
                            positions[id(child)] = (owner, field, index)
                            visit(child)
                        elif isinstance(child, ast.AST):
                            visit(child)
                elif isinstance(value, ast.AST):
                    visit(value)

        visit(root)
        return positions

    def qualified_name(node: ast.AST | None) -> str:
        if isinstance(node, ast.Name):
            return node.id
        if isinstance(node, ast.Attribute):
            prefix = qualified_name(node.value)
            return f"{prefix}.{node.attr}" if prefix else node.attr
        return ""

    add_capability_literals = [
        node
        for node in ast.walk(helper)
        if isinstance(node, ast.Constant) and node.value == "/Add-Capability"
    ]
    if len(add_capability_literals) != 1:
        errors.append("official DFKai local preflight must contain exactly one DISM Add-Capability command")

    command_assignments = [
        statement
        for statement in helper.body
        if isinstance(statement, ast.Assign)
        and len(statement.targets) == 1
        and isinstance(statement.targets[0], ast.Name)
        and statement.targets[0].id == "command"
    ]
    command_elements: list[ast.expr] = []
    if len(command_assignments) == 1 and isinstance(command_assignments[0].value, ast.List):
        command_elements = command_assignments[0].value.elts
    exact_capability_argument = (
        len(command_elements) == 5
        and isinstance(command_elements[3], ast.JoinedStr)
        and len(command_elements[3].values) == 2
        and isinstance(command_elements[3].values[0], ast.Constant)
        and command_elements[3].values[0].value == "/CapabilityName:"
        and isinstance(command_elements[3].values[1], ast.FormattedValue)
        and isinstance(command_elements[3].values[1].value, ast.Name)
        and command_elements[3].values[1].value.id == "WINDOWS_DFKAI_CAPABILITY_NAME"
    )
    exact_command = (
        len(command_elements) == 5
        and isinstance(command_elements[0], ast.Call)
        and isinstance(command_elements[0].func, ast.Name)
        and command_elements[0].func.id == "str"
        and len(command_elements[0].args) == 1
        and isinstance(command_elements[0].args[0], ast.Name)
        and command_elements[0].args[0].id == "dism_path"
        and isinstance(command_elements[1], ast.Constant)
        and command_elements[1].value == "/Online"
        and isinstance(command_elements[2], ast.Constant)
        and command_elements[2].value == "/Add-Capability"
        and exact_capability_argument
        and isinstance(command_elements[4], ast.Constant)
        and command_elements[4].value == "/NoRestart"
    )
    if not exact_command:
        errors.append(
            "official DFKai installer argv must be the exact absolute DISM Hant capability command"
        )
    command_name_nodes = [
        node
        for node in ast.walk(helper)
        if isinstance(node, ast.Name) and node.id == "command"
    ]
    if not (
        len(command_name_nodes) == 2
        and sum(isinstance(node.ctx, ast.Store) for node in command_name_nodes) == 1
        and sum(isinstance(node.ctx, ast.Load) for node in command_name_nodes) == 1
    ):
        errors.append(
            "official DFKai installer command must have one construction Store and one runner-only Load"
        )

    forbidden_process_launchers = {
        "subprocess.run",
        "subprocess.Popen",
        "subprocess.call",
        "subprocess.check_call",
        "subprocess.check_output",
        "os.system",
        "os.popen",
        "os.startfile",
    }
    unexpected_process_calls = [
        node
        for node in ast.walk(helper)
        if isinstance(node, ast.Call) and qualified_name(node.func) in forbidden_process_launchers
    ]
    if unexpected_process_calls:
        errors.append(
            "official DFKai local preflight must not contain another direct process-launch path"
        )

    runner_calls = [node for node in ast.walk(helper) if named_call(node, "runner")]
    if len(runner_calls) != 1:
        errors.append(
            "official DFKai local preflight must invoke its bounded installer exactly once: "
            f"observed={len(runner_calls)}"
        )

    top_level_ifs = [node for node in helper.body if isinstance(node, ast.If)]
    existing_guard = next((node for node in top_level_ifs if path_exists_call(node.test)), None)
    configured_guard = next(
        (
            node
            for node in top_level_ifs
            if isinstance(node.test, ast.Name) and node.test.id == "has_configured_path"
        ),
        None,
    )
    platform_guard = next(
        (
            node
            for node in top_level_ifs
            if compare_name_constant(node.test, "current_platform", ast.NotEq, "win32")
        ),
        None,
    )
    canonical_guard = next(
        (
            node
            for node in top_level_ifs
            if compare_names(node.test, "path", ast.NotEq, "default_font_path")
        ),
        None,
    )

    existing_validator_call: ast.Call | None = None
    if existing_guard is None:
        errors.append("official DFKai local preflight must start with an exact existing-path guard")
    else:
        existing_validator_tries = [
            statement
            for statement in existing_guard.body
            if isinstance(statement, ast.Try)
            and len(statement.body) == 1
            and direct_assign_call(statement.body[0], "validated_path", "validator") is not None
        ]
        if (
            len(existing_validator_tries) != 1
            or not existing_validator_tries[0].handlers
            or existing_validator_tries[0].orelse
            or existing_validator_tries[0].finalbody
            or not all(direct_terminal(handler.body, ast.Raise) for handler in existing_validator_tries[0].handlers)
        ):
            errors.append(
                "official DFKai existing-path guard must directly validate the font in a fail-closed try block"
            )
        else:
            existing_validator_call = direct_assign_call(
                existing_validator_tries[0].body[0],
                "validated_path",
                "validator",
            )
        if (
            existing_guard.orelse
            or not direct_terminal(existing_guard.body, ast.Return)
            or not isinstance(existing_guard.body[-1].value, ast.Name)
            or existing_guard.body[-1].value.id != "validated_path"
        ):
            errors.append("official DFKai existing-path guard must return before any installer path")
    for guard, message in (
        (configured_guard, "configured-path"),
        (platform_guard, "non-Windows"),
        (canonical_guard, "non-canonical-path"),
    ):
        if guard is None:
            errors.append(f"official DFKai local preflight missing exact {message} fail-closed guard")
        elif guard.orelse or not direct_terminal(guard.body, ast.Raise):
            errors.append(f"official DFKai {message} guard must fail closed before installation")

    installer_candidates: list[tuple[int, ast.Try, ast.Call]] = []
    for index, statement in enumerate(helper.body):
        if not isinstance(statement, ast.Try) or len(statement.body) != 1:
            continue
        direct_runner_call = direct_assign_call(statement.body[0], "proc", "runner")
        if direct_runner_call is not None:
            installer_candidates.append((index, statement, direct_runner_call))
    if len(installer_candidates) != 1 or len(runner_calls) != 1:
        errors.append(
            "official DFKai installer must be one direct top-level `proc = runner(...)` try statement"
        )
        runner_index = None
        installer_try = None
        runner_call = runner_calls[0] if len(runner_calls) == 1 else None
    else:
        runner_index, installer_try, runner_call = installer_candidates[0]

    guard_nodes = (existing_guard, configured_guard, platform_guard, canonical_guard)
    if runner_index is not None and all(node is not None for node in guard_nodes):
        guard_indices = [helper.body.index(node) for node in guard_nodes if node is not None]
        if guard_indices != sorted(guard_indices) or len(set(guard_indices)) != len(guard_indices):
            errors.append(
                "official DFKai local preflight guards must be ordered existing, configured, non-Windows, canonical"
            )
        if any(index >= runner_index for index in guard_indices):
            errors.append("official DFKai local preflight must run every missing-only guard before the installer")
        if any(isinstance(node, (ast.Return, ast.Raise)) for node in helper.body[: guard_indices[0]]):
            errors.append("official DFKai local preflight guards must not be unreachable after an early exit")

    if runner_call is not None:
        timeout_keyword = next((keyword for keyword in runner_call.keywords if keyword.arg == "timeout"), None)
        shell_keyword = next((keyword for keyword in runner_call.keywords if keyword.arg == "shell"), None)
        if not (
            timeout_keyword is not None
            and isinstance(timeout_keyword.value, ast.Name)
            and timeout_keyword.value.id == "WINDOWS_DFKAI_INSTALL_TIMEOUT_SECONDS"
        ):
            errors.append("official DFKai installer must use the registered bounded timeout constant")
        if not (
            len(runner_call.args) == 1
            and isinstance(runner_call.args[0], ast.Name)
            and runner_call.args[0].id == "command"
            and shell_keyword is not None
            and isinstance(shell_keyword.value, ast.Constant)
            and shell_keyword.value.value is False
        ):
            errors.append("official DFKai installer must execute only the exact argv with shell=False")
    if installer_try is not None:
        handler_names = {qualified_name(handler.type) for handler in installer_try.handlers}
        if (
            handler_names != {"subprocess.TimeoutExpired", "OSError"}
            or installer_try.orelse
            or installer_try.finalbody
            or not all(direct_terminal(handler.body, ast.Raise) for handler in installer_try.handlers)
        ):
            errors.append("official DFKai installer must fail closed directly on timeout and process-start errors")

    install_exit_code_assignments = [
        (index, statement)
        for index, statement in enumerate(helper.body)
        if isinstance(statement, ast.Assign)
        and len(statement.targets) == 1
        and isinstance(statement.targets[0], ast.Name)
        and statement.targets[0].id == "install_exit_code"
        and isinstance(statement.value, ast.Attribute)
        and isinstance(statement.value.value, ast.Name)
        and statement.value.value.id == "proc"
        and statement.value.attr == "returncode"
    ]
    if len(install_exit_code_assignments) != 1:
        errors.append(
            "official DFKai local preflight must directly capture the completed installer exit code exactly once"
        )
        install_exit_code_index = None
        install_exit_code_assignment = None
    else:
        install_exit_code_index, install_exit_code_assignment = install_exit_code_assignments[0]
    proc_returncode_reads = [
        node
        for node in ast.walk(helper)
        if isinstance(node, ast.Attribute)
        and isinstance(node.value, ast.Name)
        and node.value.id == "proc"
        and node.attr == "returncode"
    ]
    if (
        install_exit_code_assignment is None
        or len(proc_returncode_reads) != 1
        or proc_returncode_reads[0] is not install_exit_code_assignment.value
    ):
        errors.append(
            "official DFKai installer return code must be diagnostic-only and read only by install_exit_code capture"
        )

    install_detail_assignments = [
        (index, statement)
        for index, statement in enumerate(helper.body)
        if isinstance(statement, ast.Assign)
        and len(statement.targets) == 1
        and isinstance(statement.targets[0], ast.Name)
        and statement.targets[0].id == "install_detail"
    ]
    if len(install_detail_assignments) != 1:
        errors.append(
            "official DFKai local preflight must directly capture bounded installer diagnostics exactly once"
        )
        install_detail_index = None
    else:
        install_detail_index, install_detail_assignment = install_detail_assignments[0]
        detail_value = install_detail_assignment.value
        detail_slice = detail_value.slice if isinstance(detail_value, ast.Subscript) else None
        detail_attributes = {
            node.attr
            for node in ast.walk(detail_value)
            if isinstance(node, ast.Attribute)
            and isinstance(node.value, ast.Name)
            and node.value.id == "proc"
        }
        detail_literals = {
            node.value
            for node in ast.walk(detail_value)
            if isinstance(node, ast.Constant) and isinstance(node.value, str)
        }
        bounded_detail = (
            isinstance(detail_slice, ast.Slice)
            and isinstance(detail_slice.lower, ast.UnaryOp)
            and isinstance(detail_slice.lower.op, ast.USub)
            and isinstance(detail_slice.lower.operand, ast.Name)
            and detail_slice.lower.operand.id == "WINDOWS_DFKAI_INSTALL_DETAIL_LIMIT"
            and detail_slice.upper is None
            and detail_slice.step is None
        )
        strips_detail = any(
            isinstance(node, ast.Call)
            and isinstance(node.func, ast.Attribute)
            and node.func.attr == "strip"
            for node in ast.walk(detail_value)
        )
        if not (
            bounded_detail
            and strips_detail
            and {"stderr", "stdout"}.issubset(detail_attributes)
            and "no DISM output" in detail_literals
        ):
            errors.append(
                "official DFKai installer diagnostics must retain bounded stderr/stdout detail"
            )

    missing_after_install_guard = next(
        (
            node
            for node in top_level_ifs
            if isinstance(node.test, ast.UnaryOp)
            and isinstance(node.test.op, ast.Not)
            and path_exists_call(node.test.operand)
        ),
        None,
    )
    validator_calls = [node for node in ast.walk(helper) if named_call(node, "validator")]
    if len(validator_calls) != 2:
        errors.append(
            "official DFKai local preflight must validate exactly once before reuse and once after install: "
            f"observed={len(validator_calls)}"
        )
    if (
        missing_after_install_guard is None
        or missing_after_install_guard.orelse
        or not direct_terminal(missing_after_install_guard.body, ast.Raise)
    ):
        errors.append("official DFKai local preflight must fail closed when the font remains missing")

    post_validator_candidates: list[tuple[int, ast.Try, ast.Call]] = []
    for index, statement in enumerate(helper.body):
        if not isinstance(statement, ast.Try) or len(statement.body) != 1:
            continue
        direct_validator_call = direct_assign_call(statement.body[0], "validated_path", "validator")
        if direct_validator_call is not None:
            post_validator_candidates.append((index, statement, direct_validator_call))
    if len(post_validator_candidates) != 1:
        errors.append("official DFKai post-install validation must be one direct top-level try statement")
        post_validator_index = None
        post_validator_try = None
        post_install_validator = None
    else:
        post_validator_index, post_validator_try, post_install_validator = post_validator_candidates[0]
        if (
            not post_validator_try.handlers
            or post_validator_try.orelse
            or post_validator_try.finalbody
            or not all(direct_terminal(handler.body, ast.Raise) for handler in post_validator_try.handlers)
        ):
            errors.append("official DFKai post-install validation must fail closed directly")
    if (
        len(validator_calls) == 2
        and existing_validator_call is not None
        and post_install_validator is not None
        and {id(existing_validator_call), id(post_install_validator)} != {id(node) for node in validator_calls}
    ):
        errors.append("official DFKai validator calls must stay on the direct reuse and post-install success paths")

    nonzero_diagnostic_guard = next(
        (
            node
            for node in top_level_ifs
            if compare_name_constant(node.test, "install_exit_code", ast.NotEq, 0)
        ),
        None,
    )
    if nonzero_diagnostic_guard is None:
        errors.append(
            "official DFKai local preflight must report completed nonzero DISM results after final validation"
        )
    else:
        warning_call = (
            nonzero_diagnostic_guard.body[0].value
            if len(nonzero_diagnostic_guard.body) == 1
            and isinstance(nonzero_diagnostic_guard.body[0], ast.Expr)
            and named_call(nonzero_diagnostic_guard.body[0].value, "print")
            else None
        )
        warning_literals = {
            node.value
            for node in ast.walk(nonzero_diagnostic_guard)
            if isinstance(node, ast.Constant) and isinstance(node.value, str)
        }
        stderr_keyword = (
            next((keyword for keyword in warning_call.keywords if keyword.arg == "file"), None)
            if warning_call is not None
            else None
        )
        warning_to_stderr = (
            stderr_keyword is not None
            and isinstance(stderr_keyword.value, ast.Attribute)
            and isinstance(stderr_keyword.value.value, ast.Name)
            and stderr_keyword.value.value.id == "sys"
            and stderr_keyword.value.attr == "stderr"
        )
        if (
            nonzero_diagnostic_guard.orelse
            or warning_call is None
            or not warning_to_stderr
            or not any(
                "dfkai_preflight_warning=nonzero_but_final_state_valid" in literal
                for literal in warning_literals
            )
        ):
            errors.append(
                "official DFKai completed nonzero result must be a stderr diagnostic, not an early failure or bypass"
            )

    if (
        runner_index is not None
        and install_exit_code_index is not None
        and install_detail_index is not None
        and missing_after_install_guard is not None
        and post_validator_index is not None
        and nonzero_diagnostic_guard is not None
    ):
        post_install_indices = (
            runner_index,
            install_exit_code_index,
            install_detail_index,
            helper.body.index(missing_after_install_guard),
            post_validator_index,
            helper.body.index(nonzero_diagnostic_guard),
        )
        if tuple(sorted(post_install_indices)) != post_install_indices or len(set(post_install_indices)) != 6:
            errors.append(
                "official DFKai local preflight must capture diagnostics, then validate the final font state, "
                "then report a completed nonzero result"
            )
        final_return = helper.body[-1] if helper.body else None
        if (
            not isinstance(final_return, ast.Return)
            or not isinstance(final_return.value, ast.Name)
            or final_return.value.id != "validated_path"
            or helper.body.index(final_return) <= post_validator_index
        ):
            errors.append("official DFKai local preflight must return only after post-install validation")

    forbidden_policy_tokens = (
        "Get-WindowsCapability",
        "WindowsUpdate",
        "UseWUServer",
        "wuauserv",
        "New-ItemProperty",
        "Set-Service",
        "Start-Service",
        "Start-Process",
        "Verb RunAs",
    )
    for forbidden in forbidden_policy_tokens:
        forbidden_nodes = [
            node
            for node in ast.walk(tree)
            if (
                isinstance(node, ast.Name)
                and node.id == forbidden
            )
            or (
                isinstance(node, ast.Attribute)
                and node.attr == forbidden
            )
        ]
        if forbidden_nodes:
            errors.append(
                "official DFKai local preflight must not mutate Windows Update policy, services, or elevation: "
                f"{forbidden!r}"
            )

    main_definitions = [
        node
        for node in tree.body
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)) and node.name == "main"
    ]
    if len(main_definitions) != 1:
        errors.append(
            "official entrypoint must define exactly one module-level main() for DFKai local preflight routing: "
            f"observed={len(main_definitions)}"
        )
        return errors
    main_function = main_definitions[0]

    main_calls = [
        node
        for node in ast.walk(main_function)
        if named_call(node, "ensure_local_dfkai_font_for_pdf_rendering")
    ]
    if len(main_calls) != 1:
        errors.append(
            "official entrypoint main() must call the DFKai local preflight exactly once: "
            f"observed={len(main_calls)}"
        )
        return errors
    main_call = main_calls[0]
    source_gate_guards = [
        node
        for node in ast.walk(main_function)
        if isinstance(node, ast.If)
        and isinstance(node.test, ast.UnaryOp)
        and isinstance(node.test.op, ast.Not)
        and isinstance(node.test.operand, ast.Attribute)
        and isinstance(node.test.operand.value, ast.Name)
        and node.test.operand.value.id == "args"
        and node.test.operand.attr == "source_gate_only"
        and not node.orelse
        and len(node.body) == 1
        and isinstance(node.body[0], ast.Expr)
        and node.body[0].value is main_call
    ]
    if len(source_gate_guards) != 1:
        errors.append(
            "official entrypoint must skip DFKai local preflight for --source-gate-only and keep the call "
            "as a direct child of that guard"
        )

    source_gate_assignments = [
        node
        for node in ast.walk(main_function)
        if isinstance(node, ast.Assign)
        and len(node.targets) == 1
        and isinstance(node.targets[0], ast.Name)
        and node.targets[0].id == "state"
        and named_call(node.value, "ensure_entrypoint_can_run")
    ]
    if len(source_gate_assignments) != 1:
        errors.append(
            "official DFKai local preflight requires one direct state = ensure_entrypoint_can_run(...) source gate"
        )

    temp_worktrees = [
        node
        for node in ast.walk(main_function)
        if isinstance(node, ast.With)
        and any(
            isinstance(item.context_expr, ast.Call)
            and isinstance(item.context_expr.func, ast.Attribute)
            and isinstance(item.context_expr.func.value, ast.Name)
            and item.context_expr.func.value.id == "tempfile"
            and item.context_expr.func.attr == "TemporaryDirectory"
            for item in node.items
        )
    ]
    if len(temp_worktrees) != 1:
        errors.append("official DFKai local preflight must run before the temporary source worktree is created")
    if len(source_gate_guards) == 1 and len(temp_worktrees) == 1 and len(source_gate_assignments) == 1:
        suite_positions = statement_suite_positions(main_function)
        source_gate_position = suite_positions.get(id(source_gate_assignments[0]))
        guard_position = suite_positions.get(id(source_gate_guards[0]))
        temp_position = suite_positions.get(id(temp_worktrees[0]))
        if (
            source_gate_position is None
            or guard_position is None
            or temp_position is None
            or source_gate_position[0] is not guard_position[0]
            or source_gate_position[1] != guard_position[1]
            or guard_position[0] is not temp_position[0]
            or guard_position[1] != temp_position[1]
            or source_gate_position[2] >= guard_position[2]
            or guard_position[2] >= temp_position[2]
        ):
            errors.append(
                "official DFKai source gate, preflight, and temporary worktree must share one execution suite; "
                "the source gate must complete before preflight and the preflight must complete before the "
                "temporary worktree"
            )
    return errors


def chatgpt_daily_dfkai_font_path() -> Path:
    configured = os.environ.get(CHATGPT_DAILY_DFKAI_FONT_PATH_ENV, "").strip()
    if configured:
        return Path(configured).expanduser()
    return CHATGPT_DAILY_DEFAULT_DFKAI_FONT_PATH


def font_name_records(font_path: Path) -> set[str]:
    try:
        from fontTools.ttLib import TTFont as FontToolsTTFont
    except Exception as exc:  # pragma: no cover - dependency gate
        raise RuntimeError(f"fontTools is required to validate DFKai font name tables: {exc}") from exc

    try:
        font = FontToolsTTFont(str(font_path), lazy=True)
    except Exception as exc:
        raise RuntimeError(f"cannot open DFKai font with fontTools: {font_path}: {exc}") from exc
    try:
        names: set[str] = set()
        name_table = font["name"]
        for record in name_table.names:
            try:
                text = record.toUnicode().strip()
            except Exception:
                continue
            if text:
                names.add(text)
        return names
    finally:
        font.close()


def font_cmap_codepoints(font_path: Path) -> set[int]:
    try:
        from fontTools.ttLib import TTFont as FontToolsTTFont
    except Exception as exc:  # pragma: no cover - dependency gate
        raise RuntimeError(f"fontTools is required to validate DFKai cmap coverage: {exc}") from exc

    try:
        font = FontToolsTTFont(str(font_path), lazy=True)
    except Exception as exc:
        raise RuntimeError(f"cannot open DFKai font with fontTools: {font_path}: {exc}") from exc
    try:
        cmap = font.getBestCmap() or {}
        return {int(codepoint) for codepoint in cmap}
    finally:
        font.close()


def dfkai_font_validation_errors(font_path: Path | None = None) -> list[str]:
    path = font_path or chatgpt_daily_dfkai_font_path()
    errors: list[str] = []
    if not path.exists():
        return [
            "daily six-PDF renderer requires kaiu.ttf / DFKai-SB and refuses CJK fallback; "
            f"font path does not exist: {path}"
        ]
    if path.stat().st_size < 1_000_000:
        errors.append(f"DFKai font path is unexpectedly small and may be a fallback stub: {path}")

    try:
        names = font_name_records(path)
    except RuntimeError as exc:
        errors.append(str(exc))
        names = set()
    if not (names & DFKAI_NAME_TABLE_TOKENS):
        sample = ", ".join(sorted(names)[:12])
        errors.append(
            "DFKai font name table missing required exact token "
            f"{sorted(DFKAI_NAME_TABLE_TOKENS)}; font_path={path}; observed={sample}"
        )
    if names and any("TW-Kai" in name for name in names):
        errors.append(f"daily six-PDF renderer must not use TW-Kai for this contract: {path}")

    try:
        cmap_codepoints = font_cmap_codepoints(path)
    except RuntimeError as exc:
        errors.append(str(exc))
        cmap_codepoints = set()
    missing_glyphs = sorted({char for char in TRADITIONAL_CHINESE_GLYPH_CANARY if ord(char) not in cmap_codepoints})
    if missing_glyphs:
        errors.append(
            "DFKai font missing Traditional Chinese glyph canary coverage; "
            f"font_path={path}; missing={''.join(missing_glyphs)}"
        )
    return errors


def validate_dfkai_font_file(font_path: Path | None = None) -> Path:
    path = font_path or chatgpt_daily_dfkai_font_path()
    errors = dfkai_font_validation_errors(path)
    if errors:
        raise RuntimeError("ChatGPT-side daily six-PDF DFKai font validation failed:\n" + "\n".join(errors))
    return path


def _pdf_object(value: object) -> object:
    if hasattr(value, "get_object"):
        try:
            return value.get_object()
        except Exception:
            return value
    return value


def _pdf_has_embedded_font_file(descriptor: object) -> bool:
    descriptor = _pdf_object(descriptor)
    if not hasattr(descriptor, "get"):
        return False
    return any(descriptor.get(key) is not None for key in ("/FontFile", "/FontFile2", "/FontFile3"))


def _font_records_from_font(font_ref: object) -> list[PdfFontRecord]:
    font = _pdf_object(font_ref)
    if not hasattr(font, "get"):
        return []

    base_font = str(font.get("/BaseFont") or "")
    encoding = str(font.get("/Encoding") or "")
    to_unicode = font.get("/ToUnicode") is not None
    descriptor = font.get("/FontDescriptor")
    embedded = _pdf_has_embedded_font_file(descriptor) if descriptor is not None else False

    descendants = _pdf_object(font.get("/DescendantFonts") or [])
    records: list[PdfFontRecord] = []
    if descendants:
        for descendant_ref in descendants:
            descendant = _pdf_object(descendant_ref)
            if not hasattr(descendant, "get"):
                continue
            descendant_base = str(descendant.get("/BaseFont") or base_font)
            descendant_descriptor = descendant.get("/FontDescriptor")
            descendant_embedded = (
                _pdf_has_embedded_font_file(descendant_descriptor)
                if descendant_descriptor is not None
                else embedded
            )
            records.append(
                PdfFontRecord(
                    base_font=descendant_base,
                    encoding=encoding,
                    embedded=descendant_embedded,
                    to_unicode=to_unicode,
                )
            )
    else:
        records.append(
            PdfFontRecord(
                base_font=base_font,
                encoding=encoding,
                embedded=embedded,
                to_unicode=to_unicode,
            )
        )
    return records


def _collect_resource_font_records(resources_ref: object, records: list[PdfFontRecord]) -> None:
    resources = _pdf_object(resources_ref)
    if not hasattr(resources, "get"):
        return

    font_dict = _pdf_object(resources.get("/Font") or {})
    if hasattr(font_dict, "values"):
        for font_ref in font_dict.values():
            records.extend(_font_records_from_font(font_ref))

    xobjects = _pdf_object(resources.get("/XObject") or {})
    if hasattr(xobjects, "values"):
        for xobject_ref in xobjects.values():
            xobject = _pdf_object(xobject_ref)
            if hasattr(xobject, "get") and xobject.get("/Resources"):
                _collect_resource_font_records(xobject.get("/Resources"), records)


def pdf_font_records(path: Path) -> list[PdfFontRecord]:
    try:
        from pypdf import PdfReader
    except Exception as exc:  # pragma: no cover - dependency gate
        raise RuntimeError(f"pypdf is required for daily six-PDF font validation: {exc}") from exc

    if not path.exists() or path.stat().st_size < 10_000:
        raise RuntimeError(f"daily PDF missing or too small for font validation: {path}")

    records: list[PdfFontRecord] = []
    reader = PdfReader(str(path))
    for page in reader.pages:
        _collect_resource_font_records(page.get("/Resources") or {}, records)
    return records


def normalized_pdf_font_name(font_name: str) -> str:
    return re.sub(r"^/[A-Z]{6}\+", "/", font_name)


def canonical_pdf_base_font_name(font_name: str) -> str:
    normalized = normalized_pdf_font_name(font_name)
    return normalized if normalized.startswith("/") else f"/{normalized}"


def validate_daily_six_pdf_font_contract(paths: Iterable[Path]) -> dict[str, list[dict[str, object]]]:
    pdf_paths = list(paths)
    errors: list[str] = []
    result: dict[str, list[dict[str, object]]] = {}
    if len(pdf_paths) != 6:
        errors.append(f"daily six-PDF font contract requires exactly 6 PDFs; observed={len(pdf_paths)}")

    for path in pdf_paths:
        try:
            records = pdf_font_records(path)
        except RuntimeError as exc:
            errors.append(str(exc))
            continue
        serializable = [
            {
                "base_font": record.base_font,
                "encoding": record.encoding,
                "embedded": record.embedded,
                "to_unicode": record.to_unicode,
            }
            for record in records
        ]
        result[str(path)] = serializable

        normalized_records = [
            PdfFontRecord(
                base_font=normalized_pdf_font_name(record.base_font),
                encoding=normalized_pdf_font_name(record.encoding),
                embedded=record.embedded,
                to_unicode=record.to_unicode,
            )
            for record in records
        ]
        all_font_text = " ".join(
            f"{record.base_font} {record.encoding}"
            for record in normalized_records
        )
        forbidden_hits = sorted(
            {
                token
                for token in FORBIDDEN_DAILY_PDF_FONT_TOKENS
                if token in all_font_text
            }
        )
        if forbidden_hits:
            errors.append(f"{path} uses forbidden daily PDF CJK fallback fonts: {forbidden_hits}")

        dfkai_records = [
            record
            for record in normalized_records
            if canonical_pdf_base_font_name(record.base_font) in DFKAI_PDF_BASE_FONTS
        ]
        if not dfkai_records:
            errors.append(
                f"{path} missing required exact DFKai/DFKaiShu BaseFont token {sorted(DFKAI_PDF_BASE_FONTS)}; "
                f"fonts={[record.base_font for record in normalized_records]}"
            )
            continue
        for record in dfkai_records:
            if not record.embedded:
                errors.append(f"{path} DFKai font is not embedded: {record.base_font}")
            if not record.to_unicode:
                errors.append(f"{path} DFKai font is missing ToUnicode mapping: {record.base_font}")

    if errors:
        raise RuntimeError("ChatGPT-side daily six-PDF font contract failed:\n" + "\n".join(errors))
    return result


def validate() -> list[str]:
    errors: list[str] = []

    for path in (
        WORKFLOW,
        PR_VALIDATION_WORKFLOW,
        ENTRYPOINT,
        WORKTREE_SAFETY,
        RENDERER,
        PACKET_BUILDER,
        DAILY_MARKET_ARTIFACT_BUILDER,
        ALIAS_ENSURER,
        README_PUBLISHER,
        REPLAY_VALIDATOR,
    ):
        if not path.exists():
            errors.append(f"missing required ChatGPT-side contract file: {path.relative_to(ROOT).as_posix()}")

    if errors:
        return errors

    workflow = read_text(WORKFLOW)
    pr_validation_workflow = read_text(PR_VALIDATION_WORKFLOW)
    entrypoint = read_text(ENTRYPOINT)
    renderer = read_text(RENDERER)
    packet = read_text(PACKET_BUILDER)
    daily_market_builder = read_text(DAILY_MARKET_ARTIFACT_BUILDER)
    alias_ensurer = read_text(ALIAS_ENSURER)
    readme = read_text(README_PUBLISHER)
    replay_validator = read_text(REPLAY_VALIDATOR)

    for literal in (
        "resolve_daily_report_source_state",
        "CHATGPT_DAILY_REPORT_ENTRYPOINT",
        "CHATGPT_DAILY_OUTPUT_DIR",
    ):
        if literal not in entrypoint:
            errors.append(f"official entrypoint missing required source gate literal: {literal}")
    errors.extend(official_entrypoint_worktree_contract_errors(entrypoint))
    errors.extend(official_entrypoint_dfkai_preflight_contract_errors(entrypoint))

    errors.extend(daily_model_pr_scope_contract_errors(pr_validation_workflow))
    for command_literal in (
        "python scripts/validate_chatgpt_side_pdf_contract.py",
        "tests/test_chatgpt_side_pdf_contract.py",
    ):
        if command_literal not in pr_validation_workflow:
            errors.append(f"daily model PR validation missing PDF contract check: {command_literal}")

    for name in CHATGPT_SIDE_BUILDERS:
        if f"def {name}(" not in renderer:
            errors.append(f"missing ChatGPT-side PDF builder: {name}")
    try:
        main_body = function_text(renderer, "main")
    except ValueError:
        errors.append("ChatGPT-side renderer missing main()")
        main_body = ""
    if "setup_fonts()" not in main_body:
        errors.append("ChatGPT-side renderer main() must validate and register DFKai before rendering")
    for name in CHATGPT_SIDE_BUILDERS:
        if f"{name}(" not in main_body:
            errors.append(f"ChatGPT-side renderer main() does not call builder: {name}")

    for literal in FORBIDDEN_WORKFLOW_LITERALS:
        if literal in workflow:
            errors.append(f"daily_full_pipeline must not run retired fixed PDF path: {literal}")

    for literal in (
        "CHATGPT_DAILY_DFKAI_FONT_PATH_ENV",
        "validate_dfkai_font_file",
        "TTFont(CHATGPT_DAILY_PDF_FONT_NAME",
    ):
        if literal not in renderer:
            errors.append(f"ChatGPT-side daily PDF renderer missing DFKai fail-closed literal: {literal}")
    for forbidden in (
        "UnicodeCIDFont",
        "MSung-Light",
        "STSong-Light",
        "UniGB-UCS2-H",
    ):
        if forbidden in renderer:
            errors.append(f"ChatGPT-side daily PDF renderer must not contain fallback font literal: {forbidden}")
    if "validate_daily_six_pdf_font_contract(paths)" not in replay_validator:
        errors.append("new-conversation replay validator must run daily six-PDF font contract")

    for name in RETIRED_PUBLIC_PDF_FILENAMES:
        docs_copy = f"docs/latest/{name}"
        if docs_copy in workflow:
            errors.append(f"daily_full_pipeline must not publish retired repo PDF artifact: {docs_copy}")
        if docs_copy in packet:
            errors.append(f"packet builder must not expose retired repo PDF artifact: {docs_copy}")
        if docs_copy in readme:
            errors.append(f"README publisher must not expose retired repo PDF artifact: {docs_copy}")

    for name in RETIRED_FIXED_PDF_FILENAMES:
        output_path = f"output/latest/{name}"
        if output_path in packet:
            errors.append(f"packet builder must not expose retired fixed PDF artifact: {output_path}")
        if output_path in readme:
            errors.append(f"README publisher must not expose retired fixed PDF artifact: {output_path}")

    for path, source in (
        (DAILY_MARKET_ARTIFACT_BUILDER, daily_market_builder),
        (PACKET_BUILDER, packet),
        (ALIAS_ENSURER, alias_ensurer),
    ):
        rel = path.relative_to(ROOT).as_posix()
        for literal in LEGACY_DAILY_HISTORY_ALIAS_LITERALS:
            if literal in source:
                errors.append(f"{rel} still generates retired Chinese history alias: {literal}")
        for literal in (
            "{main_date}_daily_market_summary.pdf",
            "{main_date}_daily_market_full.pdf",
        ):
            if literal not in source:
                errors.append(f"{rel} missing canonical daily history PDF path: {literal}")

    if "daily_market_pdf_report_manifest_latest" in packet:
        errors.append("packet builder must not read retired fixed PDF manifest")
    if "daily_market_report_validation_latest" in packet:
        errors.append("packet builder must not read retired fixed PDF validation")
    if "daily_market_pdf_report_manifest_latest" in readme:
        errors.append("README publisher must not read retired fixed PDF manifest")
    if "daily_market_report_validation_latest" in readme:
        errors.append("README publisher must not read retired fixed PDF validation")

    return errors


def main() -> int:
    errors = validate()
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1
    print("ChatGPT-side daily PDF contract validation passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
