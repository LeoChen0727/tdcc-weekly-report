from __future__ import annotations

from pathlib import Path
import urllib.error

import pandas as pd

from scripts import generate_chatgpt_side_daily_reports as renderer
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


def test_operation_table_start_room_helper_is_low_level_shared() -> None:
    rows = validator.read_inventory()
    row = {row["symbol_name"]: row for row in rows}["operation_section_table_start_min_room"]

    assert row["ownership_class"] == "low_level_shared"
    assert row["allowed_business_semantics"] == "none"
    assert "operation_section_table_start_min_room" in validator.LOW_LEVEL_SHARED_SYMBOLS


def test_low_level_shared_helpers_do_not_contain_business_tokens() -> None:
    source = (ROOT / "scripts" / "generate_chatgpt_side_daily_reports.py").read_text(
        encoding="utf-8",
        errors="replace",
    )
    functions = validator.function_nodes(validator.ast.parse(source))

    for symbol in validator.LOW_LEVEL_SHARED_SYMBOLS:
        body = validator.function_text(source, functions[symbol])
        leaked = {token for token in validator.LOW_LEVEL_FORBIDDEN_BUSINESS_TOKENS if token in body}
        assert not leaked, f"{symbol} contains business tokens: {sorted(leaked)}"


def test_operation_line_matcher_prefers_explicit_report_line_over_memberships() -> None:
    row = pd.Series(
        {
            "report_line": "non_mainstream",
            "report_line_memberships": "mainstream|non_mainstream",
        }
    )

    assert renderer.price_pullback_operation_row_matches_line(row, "non_mainstream") is True
    assert renderer.price_pullback_operation_row_matches_line(row, "mainstream") is False
    assert renderer.w_bottom_operation_row_matches_line(row, "non_mainstream") is True
    assert renderer.w_bottom_operation_row_matches_line(row, "mainstream") is False


def test_operation_line_matcher_uses_memberships_only_without_explicit_report_line() -> None:
    row = pd.Series(
        {
            "report_line": "",
            "report_line_memberships": "mainstream|non_mainstream",
        }
    )

    assert renderer.price_pullback_operation_row_matches_line(row, "mainstream") is True
    assert renderer.price_pullback_operation_row_matches_line(row, "non_mainstream") is True
    assert renderer.w_bottom_operation_row_matches_line(row, "mainstream") is True
    assert renderer.w_bottom_operation_row_matches_line(row, "non_mainstream") is True


def test_remote_latest_csv_read_falls_back_to_clean_source_latest_on_http_429(monkeypatch) -> None:
    url = renderer.remote_latest_url("futures_options_put_call_ratio_latest.csv")

    def fail_with_rate_limit(requested_url: str) -> str:
        raise urllib.error.HTTPError(requested_url, 429, "Too Many Requests", None, None)

    monkeypatch.setattr(renderer, "fetch_text_no_cache", fail_with_rate_limit)

    frame = renderer.read_csv(url)

    assert not frame.empty


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
