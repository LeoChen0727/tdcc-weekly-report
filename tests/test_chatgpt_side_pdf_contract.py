from __future__ import annotations

import ast
from pathlib import Path

import pytest

from scripts import generate_chatgpt_side_daily_reports as renderer
from scripts import validate_chatgpt_side_pdf_contract as contract


ROOT = Path(__file__).resolve().parents[1]
WORKFLOW = ROOT / ".github" / "workflows" / "daily_full_pipeline.yml"
RENDERER = ROOT / "scripts" / "generate_chatgpt_side_daily_reports.py"
PACKET_BUILDER = ROOT / "build_chatgpt_daily_report_packet.py"
README_PUBLISHER = ROOT / "publish_chatgpt_report_readme_and_check.py"


def _source(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace")


def _top_level_function(tree: ast.Module, name: str) -> ast.FunctionDef:
    return next(
        node
        for node in tree.body
        if isinstance(node, ast.FunctionDef) and node.name == name
    )


def _named_call(node: ast.AST, name: str) -> bool:
    return isinstance(node, ast.Call) and isinstance(node.func, ast.Name) and node.func.id == name


def _replace_statement(root: ast.AST, target: ast.stmt, replacement: ast.stmt) -> None:
    for owner in ast.walk(root):
        for _field, value in ast.iter_fields(owner):
            if not isinstance(value, list):
                continue
            for index, child in enumerate(value):
                if child is target:
                    value[index] = replacement
                    return
    raise AssertionError("target statement was not found")


def _mutated_entrypoint(mutator) -> str:
    tree = ast.parse(_source(contract.ENTRYPOINT))
    mutator(tree)
    ast.fix_missing_locations(tree)
    return ast.unparse(tree)


def test_contract_validator_passes() -> None:
    assert contract.main() == 0


def test_official_entrypoint_uses_registered_worktree_helper() -> None:
    source = _source(contract.ENTRYPOINT)

    assert contract.official_entrypoint_worktree_contract_errors(source) == []


def test_official_entrypoint_uses_bounded_missing_only_dfkai_preflight() -> None:
    source = _source(contract.ENTRYPOINT)

    assert contract.official_entrypoint_dfkai_preflight_contract_errors(source) == []


def test_official_entrypoint_dfkai_preflight_requires_real_default_font_validator() -> None:
    source = _source(contract.ENTRYPOINT).replace(
        "validator: Callable[[Path], Path] = validate_dfkai_font_file,",
        "validator: Callable[[Path], Path] = lambda path: path,",
        1,
    )

    errors = contract.official_entrypoint_dfkai_preflight_contract_errors(source)

    assert any("default validator must remain validate_dfkai_font_file" in error for error in errors)


def test_official_entrypoint_dfkai_preflight_rejects_immediate_nonzero_failure() -> None:
    def mutate(tree: ast.Module) -> None:
        helper = _top_level_function(tree, "ensure_local_dfkai_font_for_pdf_rendering")
        missing_guard_index = next(
            index
            for index, statement in enumerate(helper.body)
            if isinstance(statement, ast.If) and ast.unparse(statement.test) == "not path.exists()"
        )
        helper.body.insert(
            missing_guard_index,
            ast.If(
                test=ast.Compare(
                    left=ast.Attribute(
                        value=ast.Name(id="proc", ctx=ast.Load()),
                        attr="returncode",
                        ctx=ast.Load(),
                    ),
                    ops=[ast.NotEq()],
                    comparators=[ast.Constant(0)],
                ),
                body=[
                    ast.Raise(
                        exc=ast.Call(
                            func=ast.Name(id="RuntimeError", ctx=ast.Load()),
                            args=[ast.Constant("immediate nonzero failure")],
                            keywords=[],
                        )
                    )
                ],
                orelse=[],
            ),
        )

    errors = contract.official_entrypoint_dfkai_preflight_contract_errors(_mutated_entrypoint(mutate))

    assert any("return code must be diagnostic-only" in error for error in errors)


def test_official_entrypoint_dfkai_preflight_rejects_nonzero_warning_before_validation() -> None:
    def mutate(tree: ast.Module) -> None:
        helper = _top_level_function(tree, "ensure_local_dfkai_font_for_pdf_rendering")
        diagnostic = next(
            statement
            for statement in helper.body
            if isinstance(statement, ast.If) and ast.unparse(statement.test) == "install_exit_code != 0"
        )
        missing_guard_index = next(
            index
            for index, statement in enumerate(helper.body)
            if isinstance(statement, ast.If) and ast.unparse(statement.test) == "not path.exists()"
        )
        helper.body.remove(diagnostic)
        helper.body.insert(missing_guard_index, diagnostic)

    errors = contract.official_entrypoint_dfkai_preflight_contract_errors(_mutated_entrypoint(mutate))

    assert any("then validate the final font state" in error for error in errors)


def test_official_entrypoint_dfkai_preflight_rejects_missing_font_warning_only() -> None:
    def mutate(tree: ast.Module) -> None:
        helper = _top_level_function(tree, "ensure_local_dfkai_font_for_pdf_rendering")
        missing_guard = next(
            statement
            for statement in helper.body
            if isinstance(statement, ast.If) and ast.unparse(statement.test) == "not path.exists()"
        )
        missing_guard.body[-1] = ast.Expr(
            value=ast.Call(
                func=ast.Name(id="print", ctx=ast.Load()),
                args=[ast.Constant("missing font warning")],
                keywords=[],
            )
        )

    errors = contract.official_entrypoint_dfkai_preflight_contract_errors(_mutated_entrypoint(mutate))

    assert any("fail closed when the font remains missing" in error for error in errors)


def test_official_entrypoint_dfkai_preflight_rejects_invalid_font_warning_only() -> None:
    def mutate(tree: ast.Module) -> None:
        helper = _top_level_function(tree, "ensure_local_dfkai_font_for_pdf_rendering")
        post_validator = next(
            statement
            for statement in helper.body
            if isinstance(statement, ast.Try)
            and any(_named_call(node, "validator") for node in ast.walk(statement))
        )
        post_validator.handlers[0].body[-1] = ast.Expr(
            value=ast.Call(
                func=ast.Name(id="print", ctx=ast.Load()),
                args=[ast.Constant("invalid font warning")],
                keywords=[],
            )
        )

    errors = contract.official_entrypoint_dfkai_preflight_contract_errors(_mutated_entrypoint(mutate))

    assert any("post-install validation must fail closed directly" in error for error in errors)


def test_official_entrypoint_dfkai_preflight_rejects_nonzero_validator_bypass() -> None:
    def mutate(tree: ast.Module) -> None:
        helper = _top_level_function(tree, "ensure_local_dfkai_font_for_pdf_rendering")
        post_validator = next(
            statement
            for statement in helper.body
            if isinstance(statement, ast.Try)
            and any(_named_call(node, "validator") for node in ast.walk(statement))
        )
        _replace_statement(
            helper,
            post_validator,
            ast.If(
                test=ast.Compare(
                    left=ast.Name(id="install_exit_code", ctx=ast.Load()),
                    ops=[ast.Eq()],
                    comparators=[ast.Constant(0)],
                ),
                body=[post_validator],
                orelse=[],
            ),
        )

    errors = contract.official_entrypoint_dfkai_preflight_contract_errors(_mutated_entrypoint(mutate))

    assert any("post-install validation must be one direct top-level try" in error for error in errors)


def test_official_entrypoint_dfkai_preflight_requires_exit_code_capture() -> None:
    def mutate(tree: ast.Module) -> None:
        helper = _top_level_function(tree, "ensure_local_dfkai_font_for_pdf_rendering")
        capture = next(
            statement
            for statement in helper.body
            if isinstance(statement, ast.Assign)
            and any(isinstance(target, ast.Name) and target.id == "install_exit_code" for target in statement.targets)
        )
        helper.body.remove(capture)

    errors = contract.official_entrypoint_dfkai_preflight_contract_errors(_mutated_entrypoint(mutate))

    assert any("capture the completed installer exit code" in error for error in errors)


def test_official_entrypoint_dfkai_preflight_rejects_policy_mutation_and_unconditional_call() -> None:
    source = '''
def ensure_local_dfkai_font_for_pdf_rendering():
    wuauserv = True
    runner(["dism.exe", "/Add-Capability"])

def main():
    ensure_local_dfkai_font_for_pdf_rendering()
    with tempfile.TemporaryDirectory(prefix="tdcc_daily_report_source_"):
        pass
'''

    errors = contract.official_entrypoint_dfkai_preflight_contract_errors(source)

    assert any("must not mutate Windows Update policy" in error for error in errors)
    assert any("must skip DFKai local preflight" in error for error in errors)


def test_official_entrypoint_dfkai_preflight_rejects_installer_before_missing_only_guards() -> None:
    tree = ast.parse(_source(contract.ENTRYPOINT))
    helper = next(
        node
        for node in tree.body
        if isinstance(node, ast.FunctionDef)
        and node.name == "ensure_local_dfkai_font_for_pdf_rendering"
    )
    installer_try = next(
        statement
        for statement in helper.body
        if isinstance(statement, ast.Try)
        and any(
            isinstance(node, ast.Call)
            and isinstance(node.func, ast.Name)
            and node.func.id == "runner"
            for node in ast.walk(statement)
        )
    )
    helper.body.remove(installer_try)
    helper.body.insert(0, installer_try)

    errors = contract.official_entrypoint_dfkai_preflight_contract_errors(ast.unparse(tree))

    assert any("every missing-only guard before the installer" in error for error in errors)


def test_official_entrypoint_dfkai_preflight_rejects_existing_guard_without_early_return() -> None:
    source = _source(contract.ENTRYPOINT)
    mutated = source.replace(
        "        return validated_path\n\n    if has_configured_path:",
        "        validated_path\n\n    if has_configured_path:",
        1,
    )

    errors = contract.official_entrypoint_dfkai_preflight_contract_errors(mutated)

    assert any("existing-path guard must return before any installer path" in error for error in errors)


def test_official_entrypoint_dfkai_preflight_rejects_dead_nested_existing_return() -> None:
    def mutate(tree: ast.Module) -> None:
        helper = _top_level_function(tree, "ensure_local_dfkai_font_for_pdf_rendering")
        guard = next(node for node in helper.body if isinstance(node, ast.If) and ast.unparse(node.test) == "path.exists()")
        terminal = guard.body[-1]
        guard.body[-1] = ast.If(test=ast.Constant(False), body=[terminal], orelse=[])

    errors = contract.official_entrypoint_dfkai_preflight_contract_errors(_mutated_entrypoint(mutate))

    assert any("existing-path guard must return before any installer path" in error for error in errors)


def test_official_entrypoint_dfkai_preflight_rejects_dead_nested_guard_raise() -> None:
    def mutate(tree: ast.Module) -> None:
        helper = _top_level_function(tree, "ensure_local_dfkai_font_for_pdf_rendering")
        guard = next(
            node
            for node in helper.body
            if isinstance(node, ast.If) and ast.unparse(node.test) == "has_configured_path"
        )
        terminal = guard.body[-1]
        guard.body[-1] = ast.If(test=ast.Constant(False), body=[terminal], orelse=[])

    errors = contract.official_entrypoint_dfkai_preflight_contract_errors(_mutated_entrypoint(mutate))

    assert any("configured-path guard must fail closed" in error for error in errors)


def test_official_entrypoint_dfkai_preflight_rejects_dead_nested_runner() -> None:
    def mutate(tree: ast.Module) -> None:
        helper = _top_level_function(tree, "ensure_local_dfkai_font_for_pdf_rendering")
        installer_try = next(
            statement
            for statement in helper.body
            if isinstance(statement, ast.Try)
            and any(_named_call(node, "runner") for node in ast.walk(statement))
        )
        direct_runner = installer_try.body[0]
        installer_try.body[0] = ast.If(test=ast.Constant(False), body=[direct_runner], orelse=[])

    errors = contract.official_entrypoint_dfkai_preflight_contract_errors(_mutated_entrypoint(mutate))

    assert any("direct top-level `proc = runner(...)`" in error for error in errors)


def test_official_entrypoint_dfkai_preflight_rejects_unbound_runner_result() -> None:
    def mutate(tree: ast.Module) -> None:
        helper = _top_level_function(tree, "ensure_local_dfkai_font_for_pdf_rendering")
        installer_try = next(
            statement
            for statement in helper.body
            if isinstance(statement, ast.Try)
            and any(_named_call(node, "runner") for node in ast.walk(statement))
        )
        assignment = installer_try.body[0]
        assert isinstance(assignment, ast.Assign)
        installer_try.body[0] = ast.Expr(value=assignment.value)

    errors = contract.official_entrypoint_dfkai_preflight_contract_errors(_mutated_entrypoint(mutate))

    assert any("direct top-level `proc = runner(...)`" in error for error in errors)


def test_official_entrypoint_dfkai_preflight_rejects_dead_nested_post_install_validator() -> None:
    def mutate(tree: ast.Module) -> None:
        helper = _top_level_function(tree, "ensure_local_dfkai_font_for_pdf_rendering")
        post_validator_try = next(
            statement
            for statement in helper.body
            if isinstance(statement, ast.Try)
            and any(_named_call(node, "validator") for node in ast.walk(statement))
        )
        direct_validator = post_validator_try.body[0]
        post_validator_try.body[0] = ast.If(test=ast.Constant(False), body=[direct_validator], orelse=[])

    errors = contract.official_entrypoint_dfkai_preflight_contract_errors(_mutated_entrypoint(mutate))

    assert any("post-install validation must be one direct top-level try" in error for error in errors)


def test_official_entrypoint_dfkai_preflight_rejects_dead_outer_source_gate_guard() -> None:
    def mutate(tree: ast.Module) -> None:
        main = _top_level_function(tree, "main")
        source_gate_guard = next(
            node
            for node in ast.walk(main)
            if isinstance(node, ast.If) and ast.unparse(node.test) == "not args.source_gate_only"
        )
        _replace_statement(
            main,
            source_gate_guard,
            ast.If(test=ast.Constant(False), body=[source_gate_guard], orelse=[]),
        )

    errors = contract.official_entrypoint_dfkai_preflight_contract_errors(_mutated_entrypoint(mutate))

    assert any("must share one execution suite" in error for error in errors)


def test_official_entrypoint_dfkai_preflight_rejects_preflight_before_source_gate() -> None:
    def mutate(tree: ast.Module) -> None:
        main = _top_level_function(tree, "main")
        main_try = next(statement for statement in main.body if isinstance(statement, ast.Try))
        state_assignment = next(
            statement
            for statement in main_try.body
            if isinstance(statement, ast.Assign)
            and _named_call(statement.value, "ensure_entrypoint_can_run")
        )
        source_gate_guard = next(
            statement
            for statement in main_try.body
            if isinstance(statement, ast.If) and ast.unparse(statement.test) == "not args.source_gate_only"
        )
        state_index = main_try.body.index(state_assignment)
        guard_index = main_try.body.index(source_gate_guard)
        main_try.body[state_index], main_try.body[guard_index] = source_gate_guard, state_assignment

    errors = contract.official_entrypoint_dfkai_preflight_contract_errors(_mutated_entrypoint(mutate))

    assert any("source gate must complete before preflight" in error for error in errors)


def test_official_entrypoint_dfkai_preflight_requires_exact_traditional_chinese_capability() -> None:
    source = _source(contract.ENTRYPOINT).replace(
        'WINDOWS_DFKAI_CAPABILITY_NAME = "Language.Fonts.Hant~~~und-HANT~0.0.1.0"',
        'WINDOWS_DFKAI_CAPABILITY_NAME = "Language.Fonts.Jpan~~~und-JPAN~0.0.1.0"',
        1,
    )

    errors = contract.official_entrypoint_dfkai_preflight_contract_errors(source)

    assert any("exact Traditional Chinese font capability" in error for error in errors)


def test_official_entrypoint_dfkai_preflight_requires_canonical_windows_font_path() -> None:
    assert contract.CHATGPT_DAILY_DEFAULT_DFKAI_FONT_PATH == Path(r"C:\Windows\Fonts\kaiu.ttf")


def test_official_entrypoint_dfkai_preflight_rejects_shell_execution() -> None:
    source = _source(contract.ENTRYPOINT).replace("            shell=False,", "            shell=True,", 1)

    errors = contract.official_entrypoint_dfkai_preflight_contract_errors(source)

    assert any("exact argv with shell=False" in error for error in errors)


def test_official_entrypoint_dfkai_preflight_rejects_second_process_launcher() -> None:
    source = _source(contract.ENTRYPOINT).replace(
        "    if path.exists():",
        '    subprocess.run(["sc.exe", "stop", "wuauserv"])\n\n    if path.exists():',
        1,
    )

    errors = contract.official_entrypoint_dfkai_preflight_contract_errors(source)

    assert any("another direct process-launch path" in error for error in errors)


@pytest.mark.parametrize(
    "mutation",
    [
        '    command[0] = "powershell.exe"\n',
        '    command[3] = "/CapabilityName:OpenSSH.Client~~~~0.0.1.0"\n',
        '    command += ["/Quiet"]\n',
    ],
)
def test_official_entrypoint_dfkai_preflight_rejects_command_mutation(mutation: str) -> None:
    source = _source(contract.ENTRYPOINT).replace(
        "    print(\n        \"dfkai_preflight_action=install_missing_windows_capability ",
        mutation + "    print(\n        \"dfkai_preflight_action=install_missing_windows_capability ",
        1,
    )

    errors = contract.official_entrypoint_dfkai_preflight_contract_errors(source)

    assert any("one construction Store and one runner-only Load" in error for error in errors)


def test_official_entrypoint_dfkai_preflight_allows_forbidden_token_in_explanatory_print() -> None:
    source = _source(contract.ENTRYPOINT).replace(
        "    if path.exists():",
        '    print("Start-Service and UseWUServer are forbidden here")\n\n    if path.exists():',
        1,
    )

    assert contract.official_entrypoint_dfkai_preflight_contract_errors(source) == []


@pytest.mark.parametrize(
    "duplicate_name",
    ["ensure_local_dfkai_font_for_pdf_rendering", "main"],
)
def test_official_entrypoint_dfkai_preflight_rejects_duplicate_runtime_definition(
    duplicate_name: str,
) -> None:
    source = _source(contract.ENTRYPOINT) + f"\n\ndef {duplicate_name}():\n    pass\n"

    errors = contract.official_entrypoint_dfkai_preflight_contract_errors(source)

    assert any("must define exactly one module-level" in error for error in errors)


def test_official_entrypoint_dfkai_preflight_allows_unrelated_loop_and_forbidden_comment() -> None:
    def mutate(tree: ast.Module) -> None:
        helper = _top_level_function(tree, "ensure_local_dfkai_font_for_pdf_rendering")
        helper.body.insert(
            0,
            ast.For(
                target=ast.Name(id="unused", ctx=ast.Store()),
                iter=ast.Tuple(elts=[], ctx=ast.Load()),
                body=[ast.Pass()],
                orelse=[],
            ),
        )

    source = _mutated_entrypoint(mutate) + "\n# Start-Service and UseWUServer are forbidden examples only\n"

    assert contract.official_entrypoint_dfkai_preflight_contract_errors(source) == []


def test_official_entrypoint_dfkai_preflight_accepts_ast_equivalent_formatting() -> None:
    reformatted = ast.unparse(ast.parse(_source(contract.ENTRYPOINT)))

    assert contract.official_entrypoint_dfkai_preflight_contract_errors(reformatted) == []


def test_official_entrypoint_worktree_contract_rejects_direct_raw_git_add() -> None:
    source = '''
def add_source_worktree(repo_root, source_ref, temp_root):
    return run_command(["git", "worktree", "add", "--detach", str(temp_root), source_ref])
'''

    errors = contract.official_entrypoint_worktree_contract_errors(source)

    assert any("must import registered full-temp worktree helper" in error for error in errors)
    assert any("must call registered full-temp worktree helper exactly once" in error for error in errors)


def test_official_entrypoint_worktree_contract_rejects_wrong_consumer() -> None:
    source = '''
from scripts.git_worktree_safety import create_registered_full_temp_worktree

def add_source_worktree(repo_root, source_ref, temp_root):
    return create_registered_full_temp_worktree(
        repo_root,
        source_ref,
        temp_root,
        leaf_name="origin_main_daily_report_source",
        consumer_id="unregistered_consumer",
    )
'''

    errors = contract.official_entrypoint_worktree_contract_errors(source)

    assert errors == [
        "official entrypoint must bind the registered full-temp worktree helper to exact consumer_id: "
        "chatgpt_daily_report_entrypoint"
    ]


def test_renderer_import_does_not_require_runtime_font_registration() -> None:
    assert renderer.FONT_NAME == contract.CHATGPT_DAILY_PDF_FONT_NAME
    assert renderer.Paragraph("標楷體繁體中文", renderer.BODY)


def test_renderer_setup_fonts_fails_closed_when_dfkai_is_missing(
    monkeypatch: pytest.MonkeyPatch,
    tmp_path: Path,
) -> None:
    missing_font = tmp_path / "missing-kaiu.ttf"
    monkeypatch.setattr(renderer, "chatgpt_daily_dfkai_font_path", lambda: missing_font)

    with pytest.raises(RuntimeError, match="requires validated kaiu.ttf / DFKai-SB"):
        renderer.setup_fonts()


def test_contract_validator_tracks_six_chatgpt_side_builders() -> None:
    assert contract.CHATGPT_SIDE_BUILDERS == (
        "build_mainstream_curated_pdf",
        "build_mainstream_full_candidate_pdf",
        "build_non_mainstream_curated_pdf",
        "build_non_mainstream_full_candidate_pdf",
        "build_warrant_market_auxiliary_pdf",
        "build_market_risk_background_pdf",
    )

    renderer = _source(RENDERER)
    for builder in contract.CHATGPT_SIDE_BUILDERS:
        assert f"def {builder}(" in renderer


def test_daily_full_pipeline_does_not_generate_or_publish_retired_repo_pdfs() -> None:
    workflow = _source(WORKFLOW)

    for literal in contract.FORBIDDEN_WORKFLOW_LITERALS:
        assert literal not in workflow
    for filename in contract.RETIRED_PUBLIC_PDF_FILENAMES:
        assert f"docs/latest/{filename}" not in workflow


def test_packet_and_readme_do_not_expose_retired_repo_pdf_links() -> None:
    packet = _source(PACKET_BUILDER)
    readme = _source(README_PUBLISHER)

    for filename in contract.RETIRED_PUBLIC_PDF_FILENAMES:
        assert f"docs/latest/{filename}" not in packet
        assert f"docs/latest/{filename}" not in readme
    for filename in contract.RETIRED_FIXED_PDF_FILENAMES:
        assert f"output/latest/{filename}" not in packet
        assert f"output/latest/{filename}" not in readme
    for forbidden in (
        "daily_market_pdf_report_manifest_latest",
        "daily_market_report_validation_latest",
    ):
        assert forbidden not in packet
        assert forbidden not in readme


def _fake_font_path(tmp_path: Path) -> Path:
    path = tmp_path / "kaiu.ttf"
    path.write_bytes(b"x" * 1_000_001)
    return path


def _six_fake_pdfs(tmp_path: Path) -> list[Path]:
    paths = []
    for index in range(6):
        path = tmp_path / f"daily_{index}.pdf"
        path.write_bytes(b"%PDF-" + b"x" * 10_001)
        paths.append(path)
    return paths


def test_dfkai_font_path_uses_exact_daily_env_var(
    monkeypatch: pytest.MonkeyPatch,
    tmp_path: Path,
) -> None:
    font_path = tmp_path / "kaiu.ttf"
    monkeypatch.setenv(contract.CHATGPT_DAILY_DFKAI_FONT_PATH_ENV, str(font_path))

    assert contract.chatgpt_daily_dfkai_font_path() == font_path


def test_dfkai_font_file_validation_fails_closed_when_path_missing(tmp_path: Path) -> None:
    missing_font = tmp_path / "missing-kaiu.ttf"

    errors = contract.dfkai_font_validation_errors(missing_font)

    assert any("font path does not exist" in error for error in errors)
    with pytest.raises(RuntimeError, match="font path does not exist"):
        contract.validate_dfkai_font_file(missing_font)


def test_dfkai_font_file_validation_requires_exact_name_table_token(
    monkeypatch: pytest.MonkeyPatch,
    tmp_path: Path,
) -> None:
    font_path = _fake_font_path(tmp_path)
    monkeypatch.setattr(contract, "font_name_records", lambda path: {"NotDFKai-SB"})
    monkeypatch.setattr(
        contract,
        "font_cmap_codepoints",
        lambda path: {ord(char) for char in contract.TRADITIONAL_CHINESE_GLYPH_CANARY},
    )

    errors = contract.dfkai_font_validation_errors(font_path)

    assert any("required exact token" in error for error in errors)


def test_dfkai_font_file_validation_rejects_empty_name_table(
    monkeypatch: pytest.MonkeyPatch,
    tmp_path: Path,
) -> None:
    font_path = _fake_font_path(tmp_path)
    monkeypatch.setattr(contract, "font_name_records", lambda path: set())
    monkeypatch.setattr(
        contract,
        "font_cmap_codepoints",
        lambda path: {ord(char) for char in contract.TRADITIONAL_CHINESE_GLYPH_CANARY},
    )

    errors = contract.dfkai_font_validation_errors(font_path)

    assert any("required exact token" in error for error in errors)


def test_dfkai_font_file_validation_rejects_missing_glyph_canary(
    monkeypatch: pytest.MonkeyPatch,
    tmp_path: Path,
) -> None:
    font_path = _fake_font_path(tmp_path)
    omitted_char = contract.TRADITIONAL_CHINESE_GLYPH_CANARY[-1]
    monkeypatch.setattr(contract, "font_name_records", lambda path: {"DFKai-SB"})
    monkeypatch.setattr(
        contract,
        "font_cmap_codepoints",
        lambda path: {
            ord(char)
            for char in contract.TRADITIONAL_CHINESE_GLYPH_CANARY
            if char != omitted_char
        },
    )

    errors = contract.dfkai_font_validation_errors(font_path)

    assert any("missing Traditional Chinese glyph canary coverage" in error for error in errors)
    assert any(omitted_char in error for error in errors)


def test_dfkai_font_file_validation_accepts_exact_name_table_token(
    monkeypatch: pytest.MonkeyPatch,
    tmp_path: Path,
) -> None:
    font_path = _fake_font_path(tmp_path)
    monkeypatch.setattr(contract, "font_name_records", lambda path: {"DFKai-SB"})
    monkeypatch.setattr(
        contract,
        "font_cmap_codepoints",
        lambda path: {ord(char) for char in contract.TRADITIONAL_CHINESE_GLYPH_CANARY},
    )

    assert contract.dfkai_font_validation_errors(font_path) == []


def test_daily_six_pdf_font_contract_rejects_substring_basefont(
    monkeypatch: pytest.MonkeyPatch,
    tmp_path: Path,
) -> None:
    paths = _six_fake_pdfs(tmp_path)
    monkeypatch.setattr(
        contract,
        "pdf_font_records",
        lambda path: [contract.PdfFontRecord("/AAAAAA+NotDFKai-SB", "/Identity-H", True, True)],
    )

    with pytest.raises(RuntimeError, match="missing required exact DFKai"):
        contract.validate_daily_six_pdf_font_contract(paths)


def test_daily_six_pdf_font_contract_rejects_generic_dfkai_basefont(
    monkeypatch: pytest.MonkeyPatch,
    tmp_path: Path,
) -> None:
    paths = _six_fake_pdfs(tmp_path)
    monkeypatch.setattr(
        contract,
        "pdf_font_records",
        lambda path: [contract.PdfFontRecord("/AAAAAA+DFKai", "/Identity-H", True, True)],
    )

    with pytest.raises(RuntimeError, match="missing required exact DFKai"):
        contract.validate_daily_six_pdf_font_contract(paths)


def test_daily_six_pdf_font_contract_accepts_exact_subset_dfkai_basefont(
    monkeypatch: pytest.MonkeyPatch,
    tmp_path: Path,
) -> None:
    paths = _six_fake_pdfs(tmp_path)
    monkeypatch.setattr(
        contract,
        "pdf_font_records",
        lambda path: [contract.PdfFontRecord("/AAAAAA+DFKai-SB", "/Identity-H", True, True)],
    )

    assert contract.validate_daily_six_pdf_font_contract(paths)


def test_daily_six_pdf_font_contract_rejects_exact_dfkai_without_embedding(
    monkeypatch: pytest.MonkeyPatch,
    tmp_path: Path,
) -> None:
    paths = _six_fake_pdfs(tmp_path)
    monkeypatch.setattr(
        contract,
        "pdf_font_records",
        lambda path: [contract.PdfFontRecord("/AAAAAA+DFKai-SB", "/Identity-H", False, True)],
    )

    with pytest.raises(RuntimeError, match="not embedded"):
        contract.validate_daily_six_pdf_font_contract(paths)


def test_daily_six_pdf_font_contract_rejects_exact_dfkai_without_tounicode(
    monkeypatch: pytest.MonkeyPatch,
    tmp_path: Path,
) -> None:
    paths = _six_fake_pdfs(tmp_path)
    monkeypatch.setattr(
        contract,
        "pdf_font_records",
        lambda path: [contract.PdfFontRecord("/AAAAAA+DFKai-SB", "/Identity-H", True, False)],
    )

    with pytest.raises(RuntimeError, match="missing ToUnicode"):
        contract.validate_daily_six_pdf_font_contract(paths)


def test_daily_six_pdf_font_contract_rejects_fallback_font(
    monkeypatch: pytest.MonkeyPatch,
    tmp_path: Path,
) -> None:
    paths = _six_fake_pdfs(tmp_path)
    monkeypatch.setattr(
        contract,
        "pdf_font_records",
        lambda path: [contract.PdfFontRecord("/MSung-Light", "/UniGB-UCS2-H", False, False)],
    )

    with pytest.raises(RuntimeError, match="MSung-Light"):
        contract.validate_daily_six_pdf_font_contract(paths)


def test_daily_six_pdf_font_contract_requires_all_six_pdfs(
    monkeypatch: pytest.MonkeyPatch,
    tmp_path: Path,
) -> None:
    paths = _six_fake_pdfs(tmp_path)[:5]
    monkeypatch.setattr(
        contract,
        "pdf_font_records",
        lambda path: [contract.PdfFontRecord("/AAAAAA+DFKaiShu-SB-Estd-BF", "/Identity-H", True, True)],
    )

    with pytest.raises(RuntimeError, match="exactly 6 PDFs"):
        contract.validate_daily_six_pdf_font_contract(paths)
