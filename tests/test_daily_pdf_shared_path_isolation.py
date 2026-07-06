from __future__ import annotations

from pathlib import Path

from scripts import validate_daily_pdf_shared_path_isolation as validator


ROOT = Path(__file__).resolve().parents[1]


def test_daily_pdf_shared_path_isolation_validator_passes() -> None:
    assert validator.main() == 0


def test_price_pullback_operation_renderer_uses_model_owned_line_filter() -> None:
    source = (ROOT / "scripts" / "generate_chatgpt_side_daily_reports.py").read_text(
        encoding="utf-8",
        errors="replace",
    )
    tree = validator.ast.parse(source)
    functions = validator.function_nodes(tree)
    body = validator.function_text(source, functions["render_price_pullback_operation_section"])
    selector_body = validator.function_text(source, functions["price_pullback_operation_all_rows_for_pdf"])

    assert "selected_price_pullback_operation_rows_for_pdf" in body
    assert "filter_price_pullback_operation_rows_for_line" in selector_body
    assert "filter_w_bottom_operation_rows_for_line" not in body
    assert "filter_w_bottom_operation_rows_for_line" not in selector_body
    assert "volume_operation_" not in body
    assert "volume_operation_" not in selector_body


def test_daily_pdf_shared_path_inventory_registers_operation_like_symbols() -> None:
    rows = validator.read_inventory()
    registered = {row["symbol_name"] for row in rows}
    source = (ROOT / "scripts" / "generate_chatgpt_side_daily_reports.py").read_text(
        encoding="utf-8",
        errors="replace",
    )
    functions = validator.function_nodes(validator.ast.parse(source))

    assert validator.operation_like_symbols(functions) <= registered


def test_daily_workflows_run_shared_path_validator() -> None:
    daily_workflow = (ROOT / ".github" / "workflows" / "daily_full_pipeline.yml").read_text(
        encoding="utf-8",
        errors="replace",
    )
    pr_workflow = (
        ROOT / ".github" / "workflows" / "daily_model_maintenance_pr_validation.yml"
    ).read_text(encoding="utf-8", errors="replace")

    command = "python scripts/validate_daily_pdf_shared_path_isolation.py"
    assert command in daily_workflow
    assert command in pr_workflow
