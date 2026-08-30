from __future__ import annotations

"""Independent source-level contract validator for the revenue v2 PDF consumer."""

import argparse
import ast
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_RENDERER = ROOT / "scripts" / "generate_chatgpt_side_daily_reports.py"

MODEL_ID = "revenue_unreacted_range"
SOURCE_ARTIFACT = (
    "output/latest/daily_revenue_unreacted_range_operation_section_latest.csv"
)
OPERATION_MODULE_ID = "revenue_unreacted_range_source_mid_falling_v2_operation_v2"
ADAPTER_SCHEMA_VERSION = "revenue_unreacted_range_operation_section_schema_v2"
LIFECYCLE_CONTRACT_VERSION = "revenue_unreacted_range_lifecycle_v2"
SECTIONS = (
    "confirmed_operation",
    "confirmed_unranked_operation",
    "pending_confirmation",
    "active_operation",
)

REQUIRED_FUNCTIONS = {
    "load_inputs",
    "revenue_unreacted_range_readiness_row",
    "revenue_unreacted_range_pdf_adapter_enabled",
    "revenue_unreacted_range_generic_signal_rows_removed",
    "model_uses_operation_pdf_table",
    "validate_revenue_unreacted_range_operation_artifact",
    "revenue_unreacted_range_operation_frame",
    "revenue_unreacted_range_operation_row_matches_line",
    "revenue_unreacted_range_operation_all_rows_for_pdf",
    "limit_revenue_unreacted_range_operation_rows_for_pdf_view",
    "selected_revenue_unreacted_range_operation_rows_for_pdf",
    "build_revenue_unreacted_range_confirmed_operation_table",
    "build_revenue_unreacted_range_unranked_operation_table",
    "build_revenue_unreacted_range_pending_operation_table",
    "build_revenue_unreacted_range_active_operation_table",
    "render_revenue_unreacted_range_operation_section",
    "render_model_operation_section_if_applicable",
    "operation_rendered_sections_for_inputs",
    "selected_operation_rows_for_manifest",
}

GENERIC_SIGNAL_CONSUMERS = {
    "core_model_specs",
    "model_signal_rows",
    "mainstream_curated_model_signal_rows",
    "mainstream_full_model_signal_rows",
    "non_mainstream_curated_model_signal_rows",
    "non_mainstream_full_model_signal_rows",
    "volume_operation_report_lines_for_stock",
    "model_signal_rows_for_stock",
    "build_mainstream_full_candidate_pdf",
    "build_non_mainstream_full_candidate_pdf",
    "build_warrant_market_auxiliary_pdf",
}


def _assigned_node(tree: ast.Module, name: str) -> ast.AST | None:
    for node in tree.body:
        if isinstance(node, (ast.Assign, ast.AnnAssign)):
            targets = node.targets if isinstance(node, ast.Assign) else [node.target]
            if any(isinstance(target, ast.Name) and target.id == name for target in targets):
                return node.value
    return None


def _literal(tree: ast.Module, name: str):
    node = _assigned_node(tree, name)
    if node is None:
        raise KeyError(name)
    return ast.literal_eval(node)


def _function_nodes(tree: ast.Module) -> dict[str, ast.FunctionDef]:
    return {
        node.name: node
        for node in tree.body
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef))
    }


def _segment(source: str, node: ast.AST) -> str:
    return ast.get_source_segment(source, node) or ""


def _reads_inputs_key(node: ast.AST, key: str) -> bool:
    for child in ast.walk(node):
        if (
            isinstance(child, ast.Call)
            and isinstance(child.func, ast.Attribute)
            and child.func.attr == "get"
            and isinstance(child.func.value, ast.Name)
            and child.func.value.id == "inputs"
            and child.args
            and isinstance(child.args[0], ast.Constant)
            and child.args[0].value == key
        ):
            return True
        if (
            isinstance(child, ast.Subscript)
            and isinstance(child.ctx, ast.Load)
            and isinstance(child.value, ast.Name)
            and child.value.id == "inputs"
            and isinstance(child.slice, ast.Constant)
            and child.slice.value == key
        ):
            return True
    return False


def validate_renderer(path: Path = DEFAULT_RENDERER) -> list[str]:
    errors: list[str] = []
    try:
        source = path.read_text(encoding="utf-8")
        tree = ast.parse(source, filename=str(path))
    except (OSError, SyntaxError) as exc:
        return [f"renderer cannot be parsed: {exc}"]

    expected_literals = {
        "REVENUE_UNREACTED_RANGE_MODEL_ID": MODEL_ID,
        "REVENUE_UNREACTED_RANGE_OPERATION_INPUT_KEY": "revenue_unreacted_range_operation",
        "REVENUE_UNREACTED_RANGE_OPERATION_SOURCE_ARTIFACT": SOURCE_ARTIFACT,
        "REVENUE_UNREACTED_RANGE_OPERATION_MODULE_ID": OPERATION_MODULE_ID,
        "REVENUE_UNREACTED_RANGE_ADAPTER_SCHEMA_VERSION": ADAPTER_SCHEMA_VERSION,
        "REVENUE_UNREACTED_RANGE_LIFECYCLE_CONTRACT_VERSION": LIFECYCLE_CONTRACT_VERSION,
        "REVENUE_UNREACTED_RANGE_OPERATION_SECTIONS": SECTIONS,
        "REVENUE_UNREACTED_RANGE_PDF_PRESENTATION_ORDER": 1.25,
    }
    for name, expected in expected_literals.items():
        try:
            observed = _literal(tree, name)
        except (KeyError, ValueError, TypeError):
            errors.append(f"missing literal constant: {name}")
            continue
        if observed != expected:
            errors.append(f"{name} mismatch: {observed!r}")

    functions = _function_nodes(tree)
    missing_functions = sorted(REQUIRED_FUNCTIONS - set(functions))
    if missing_functions:
        errors.append("missing revenue PDF consumer functions: " + ",".join(missing_functions))

    load_inputs = functions.get("load_inputs")
    if load_inputs:
        load_source = _segment(source, load_inputs)
        if "REVENUE_UNREACTED_RANGE_OPERATION_INPUT_KEY" not in load_source:
            errors.append("load_inputs does not register the dedicated revenue operation input key")
        if "daily_revenue_unreacted_range_operation_section_latest.csv" not in load_source:
            errors.append("load_inputs does not read the dedicated revenue operation artifact")
        for token in (
            "revenue_unreacted_range_pdf_adapter_enabled(inputs)",
            'inputs["model_signals"] = revenue_unreacted_range_generic_signal_rows_removed(inputs)',
        ):
            if token not in load_source:
                errors.append(
                    "load_inputs does not fail closed and retire legacy generic revenue rows: "
                    + token
                )

    readiness_row = functions.get("revenue_unreacted_range_readiness_row")
    if readiness_row:
        readiness_row_source = _segment(source, readiness_row)
        if "legacy generic fallback is forbidden" not in readiness_row_source:
            errors.append("missing revenue readiness does not explicitly forbid legacy generic fallback")
        if "return None" in readiness_row_source:
            errors.append("missing revenue readiness still returns a dormant/fallback state")

    readiness = functions.get("revenue_unreacted_range_pdf_adapter_enabled")
    if readiness:
        readiness_source = _segment(source, readiness)
        for token in (
            "presentation_allowed",
            "pdf_integrated_daily_adapter",
            "formal_model_use_allowed",
            "approved_for_daily",
            "production_allowed",
            "operation_module_id",
            "daily_adapter_sections",
        ):
            if token not in readiness_source:
                errors.append(f"revenue readiness gate missing token: {token}")
        for token in (
            "legacy generic fallback is forbidden",
            "validate_revenue_unreacted_range_operation_artifact",
            "section_tokens != expected_sections",
        ):
            if token not in readiness_source:
                errors.append(f"revenue exact v2 readiness gate missing token: {token}")
        if "return False" in readiness_source:
            errors.append("revenue PDF adapter gate still exposes a dormant generic fallback")

    legacy_filter = functions.get("revenue_unreacted_range_generic_signal_rows_removed")
    if legacy_filter:
        filter_source = _segment(source, legacy_filter)
        for token in (
            'inputs.get("model_signals"',
            "REVENUE_UNREACTED_RANGE_MODEL_ID",
            "revenue_unreacted_range_pdf_adapter_enabled(inputs)",
            "signals.loc[~revenue_mask]",
        ):
            if token not in filter_source:
                errors.append(f"legacy generic revenue row filter missing token: {token}")

    for function_name, node in functions.items():
        if function_name == "revenue_unreacted_range_generic_signal_rows_removed":
            continue
        if _reads_inputs_key(node, "model_signals"):
            errors.append(
                f"{function_name} contains forbidden fallback dependency: direct generic model_signals read"
            )
        if _reads_inputs_key(node, "model_summary"):
            errors.append(
                f"{function_name} contains forbidden fallback dependency: generic model_summary read"
            )

    for function_name in sorted(GENERIC_SIGNAL_CONSUMERS):
        node = functions.get(function_name)
        if not node:
            errors.append(f"missing generic PDF signal consumer: {function_name}")
            continue
        if "revenue_unreacted_range_generic_signal_rows_removed(inputs)" not in _segment(
            source, node
        ):
            errors.append(
                f"{function_name} bypasses permanent legacy revenue generic-row retirement"
            )

    artifact_validator = functions.get("validate_revenue_unreacted_range_operation_artifact")
    if artifact_validator:
        artifact_source = _segment(source, artifact_validator)
        for token in (
            "REVENUE_UNREACTED_RANGE_OPERATION_REQUIRED_COLUMNS",
            "REVENUE_UNREACTED_RANGE_OPERATION_MODULE_ID",
            "REVENUE_UNREACTED_RANGE_ADAPTER_SCHEMA_VERSION",
            "REVENUE_UNREACTED_RANGE_LIFECYCLE_CONTRACT_VERSION",
            "research|candidate_model_signals|model_signals",
            "duplicate display_order",
        ):
            if token not in artifact_source:
                errors.append(f"revenue artifact fail-closed validator missing token: {token}")

    isolated_functions = (
        "revenue_unreacted_range_operation_frame",
        "revenue_unreacted_range_operation_all_rows_for_pdf",
        "selected_revenue_unreacted_range_operation_rows_for_pdf",
        "render_revenue_unreacted_range_operation_section",
    )
    forbidden_fallback_tokens = (
        'inputs.get("model_signals"',
        'inputs.get("volume_operation"',
        'inputs.get("w_bottom',
        'inputs.get("price_pullback',
        "research_backtest",
    )
    for function_name in isolated_functions:
        node = functions.get(function_name)
        if not node:
            continue
        function_source = _segment(source, node)
        for token in forbidden_fallback_tokens:
            if token in function_source:
                errors.append(
                    f"{function_name} contains forbidden fallback dependency: {token}"
                )

    selector = functions.get("selected_revenue_unreacted_range_operation_rows_for_pdf")
    if selector:
        selector_source = _segment(source, selector)
        for token in (
            "confirmed_buy_candidate",
            "confirmed_not_buy_ranked",
            "pending_confirmation",
            "active_operation",
            "limit_revenue_unreacted_range_operation_rows_for_pdf_view",
        ):
            if token not in selector_source:
                errors.append(f"revenue row selector missing contract token: {token}")

    limiter = functions.get("limit_revenue_unreacted_range_operation_rows_for_pdf_view")
    if limiter:
        limiter_source = _segment(source, limiter)
        if ".head(OPERATION_HIGHLIGHT_ACTIVE_MAX_ROWS)" not in limiter_source:
            errors.append("revenue highlight active rows are not capped by the exact 10-row constant")
        if 'pdf_section == "confirmed_operation"' not in limiter_source:
            errors.append("revenue highlight confirmed rows do not have an uncapped dedicated branch")

    renderer = functions.get("render_revenue_unreacted_range_operation_section")
    if renderer:
        renderer_source = _segment(source, renderer)
        for token in (
            "build_revenue_unreacted_range_confirmed_operation_table",
            "build_revenue_unreacted_range_unranked_operation_table",
            "build_revenue_unreacted_range_pending_operation_table",
            "build_revenue_unreacted_range_active_operation_table",
            'pdf_view == "full"',
        ):
            if token not in renderer_source:
                errors.append(f"revenue dedicated renderer missing token: {token}")
        for forbidden in (
            "build_volume_",
            "build_w_bottom_",
            "build_price_pullback_",
        ):
            if forbidden in renderer_source:
                errors.append(f"revenue renderer reuses another model business table: {forbidden}")

    dispatcher = functions.get("render_model_operation_section_if_applicable")
    if dispatcher:
        dispatcher_source = _segment(source, dispatcher)
        for token in (
            "REVENUE_UNREACTED_RANGE_MODEL_ID",
            "revenue_unreacted_range_pdf_adapter_enabled",
            "render_revenue_unreacted_range_operation_section",
        ):
            if token not in dispatcher_source:
                errors.append(f"operation renderer dispatcher missing revenue token: {token}")
        revenue_branch = dispatcher_source.split(
            "if model_id == REVENUE_UNREACTED_RANGE_MODEL_ID:", 1
        )[-1].split("if model_id in VOLUME_BREAKOUT_OPERATION_MODEL_IDS:", 1)[0]
        if "return False" in revenue_branch:
            errors.append("operation renderer dispatcher still permits dormant revenue fallback")

    manifest_writer = functions.get("write_pdf_semantic_manifest")
    if manifest_writer and "operation_rendered_sections_for_inputs(inputs)" not in _segment(source, manifest_writer):
        errors.append("semantic manifest does not use readiness-aware operation sections")
    manifest_selector = functions.get("selected_operation_rows_for_manifest")
    if manifest_selector:
        selector_source = _segment(source, manifest_selector)
        if "selected_revenue_unreacted_range_operation_rows_for_pdf" not in selector_source:
            errors.append("semantic manifest selector does not use the dedicated revenue adapter")
        revenue_branch = selector_source.split(
            "if model_id == REVENUE_UNREACTED_RANGE_MODEL_ID:", 1
        )[-1].split("if model_id in VOLUME_BREAKOUT_OPERATION_MODEL_IDS:", 1)[0]
        if "return pd.DataFrame()" in revenue_branch:
            errors.append("semantic manifest selector still permits dormant revenue fallback")

    rendered_sections = functions.get("operation_rendered_sections_for_inputs")
    if rendered_sections:
        rendered_source = _segment(source, rendered_sections)
        if "if revenue_unreacted_range_pdf_adapter_enabled(inputs)" in rendered_source:
            errors.append("semantic manifest sections still permit dormant revenue omission")

    required_text_validator = functions.get("required_stock_model_text_missing")
    if required_text_validator and "model_uses_operation_pdf_table(inputs, model_id)" not in _segment(
        source, required_text_validator
    ):
        errors.append(
            "stock-model PDF text validation is not readiness-aware for the revenue operation table"
        )

    for container_name in ("OPERATION_TABLE_MODEL_IDS", "OPERATION_RENDERED_SECTIONS"):
        node = _assigned_node(tree, container_name)
        if node and "REVENUE_UNREACTED_RANGE_MODEL_ID" in _segment(source, node):
            errors.append(
                f"{container_name} bypasses the exact revenue v2 readiness and artifact gate"
            )

    for token, label in (
        ("\u672c\u65e5\u7121\u80a1\u7968\u63a8\u85a6", "confirmed empty state"),
        ("\u76ee\u524d\u7121\u64cd\u4f5c\u4e2d\u8ffd\u8e64\u5217", "active empty state"),
        ("D+2\u958b\u76e4\u9032\u5834", "outcome entry timing"),
        ("D+30\u6536\u76e4\u56fa\u5b9a\u51fa\u5834", "outcome exit timing"),
    ):
        if token not in source:
            errors.append(f"revenue PDF consumer missing {label}: {token}")
    return errors


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--renderer", type=Path, default=DEFAULT_RENDERER)
    args = parser.parse_args(argv)
    errors = validate_renderer(args.renderer)
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1
    print("revenue_unreacted_range PDF consumer contract validation passed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
