from __future__ import annotations

import ast
import csv
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
GENERATOR = ROOT / "scripts" / "generate_chatgpt_side_daily_reports.py"
INVENTORY = ROOT / "config" / "daily_pdf_shared_path_inventory.csv"

REQUIRED_COLUMNS = {
    "component_id",
    "file_path",
    "symbol_name",
    "component_type",
    "ownership_class",
    "allowed_callers",
    "allowed_business_semantics",
    "validator_rule",
    "status",
    "notes",
}

LOW_LEVEL_SHARED_SYMBOLS = {"table_para", "build_table", "write_pdf"}

REPORT_SPECIFIC_BUILDERS = {
    "build_mainstream_curated_pdf",
    "build_non_mainstream_curated_pdf",
    "build_mainstream_full_candidate_pdf",
    "build_non_mainstream_full_candidate_pdf",
    "build_warrant_market_auxiliary_pdf",
    "build_market_risk_background_pdf",
}

STOCK_PDF_BUILDERS = {
    "build_mainstream_curated_pdf",
    "build_non_mainstream_curated_pdf",
    "build_mainstream_full_candidate_pdf",
    "build_non_mainstream_full_candidate_pdf",
}

MODEL_SPECIFIC_OPERATION_SYMBOLS = {
    "volume_operation_frame",
    "filter_volume_operation_rows_for_line",
    "limit_volume_operation_rows_for_pdf_view",
    "volume_operation_all_rows_for_pdf",
    "selected_volume_operation_rows_for_pdf",
    "render_volume_range_breakout_operation_section",
    "build_volume_confirmed_operation_table",
    "build_volume_unranked_operation_table",
    "build_volume_pending_operation_table",
    "build_volume_active_operation_table",
    "w_bottom_operation_source_key",
    "require_w_bottom_operation_readiness",
    "w_bottom_operation_frame",
    "w_bottom_operation_row_matches_line",
    "filter_w_bottom_operation_rows_for_line",
    "limit_w_bottom_operation_rows_for_pdf_view",
    "w_bottom_operation_all_rows_for_pdf",
    "selected_w_bottom_operation_rows_for_pdf",
    "render_w_bottom_operation_section",
    "build_w_bottom_confirmed_operation_table",
    "build_w_bottom_active_operation_table",
    "require_price_pullback_operation_readiness",
    "price_pullback_operation_frame",
    "price_pullback_operation_row_matches_line",
    "filter_price_pullback_operation_rows_for_line",
    "price_pullback_operation_all_rows_for_pdf",
    "selected_price_pullback_operation_rows_for_pdf",
    "render_price_pullback_operation_section",
    "build_price_pullback_confirmed_operation_table",
    "build_price_pullback_active_operation_table",
}

OPERATION_DISPATCHER = "render_model_operation_section_if_applicable"

OWNERSHIP_CLASSES = {
    "low_level_shared",
    "report_specific_business",
    "model_specific_business",
    "operation_dispatcher_guarded",
}


def read_text(path: Path) -> str:
    if not path.exists():
        raise FileNotFoundError(path)
    return path.read_text(encoding="utf-8", errors="replace")


def read_inventory() -> list[dict[str, str]]:
    if not INVENTORY.exists():
        raise FileNotFoundError(INVENTORY)
    with INVENTORY.open("r", encoding="utf-8", newline="") as fh:
        reader = csv.DictReader(fh)
        if not reader.fieldnames:
            raise RuntimeError("daily PDF shared path inventory has no header")
        missing = sorted(REQUIRED_COLUMNS - set(reader.fieldnames))
        if missing:
            raise RuntimeError("daily PDF shared path inventory missing columns: " + ",".join(missing))
        return [{key: (value or "").strip() for key, value in row.items()} for row in reader]


def function_nodes(tree: ast.AST) -> dict[str, ast.FunctionDef]:
    return {node.name: node for node in ast.walk(tree) if isinstance(node, ast.FunctionDef)}


def function_text(source: str, node: ast.FunctionDef) -> str:
    lines = source.splitlines()
    start = max(node.lineno - 1, 0)
    end = node.end_lineno or node.lineno
    return "\n".join(lines[start:end])


def ast_call_names(node: ast.AST) -> set[str]:
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


def inventory_by_symbol(rows: list[dict[str, str]]) -> dict[str, dict[str, str]]:
    by_symbol: dict[str, dict[str, str]] = {}
    seen_ids: set[str] = set()
    for row in rows:
        component_id = row["component_id"]
        symbol = row["symbol_name"]
        if component_id in seen_ids:
            raise RuntimeError(f"duplicate daily PDF shared path component_id: {component_id}")
        seen_ids.add(component_id)
        if symbol in by_symbol:
            raise RuntimeError(f"duplicate daily PDF shared path symbol_name: {symbol}")
        by_symbol[symbol] = row
    return by_symbol


def operation_like_symbols(functions: dict[str, ast.FunctionDef]) -> set[str]:
    patterns = [
        re.compile(r"^build_.*_operation_table$"),
        re.compile(r"^render_.*operation_section"),
        re.compile(r".*_operation_frame$"),
        re.compile(r"^filter_.*operation_rows_for_line$"),
        re.compile(r"^limit_.*operation_rows_for_pdf_view$"),
        re.compile(r".*_operation_(all|selected)_rows_for_pdf$"),
        re.compile(r"^selected_.*operation_rows_for_pdf$"),
        re.compile(r".*_operation_row_matches_line$"),
    ]
    symbols = {OPERATION_DISPATCHER}
    for name in functions:
        if any(pattern.search(name) for pattern in patterns):
            symbols.add(name)
    return symbols


def validate_inventory_rows(
    rows: list[dict[str, str]],
    functions: dict[str, ast.FunctionDef],
) -> list[str]:
    errors: list[str] = []
    by_symbol = inventory_by_symbol(rows)

    required = LOW_LEVEL_SHARED_SYMBOLS | REPORT_SPECIFIC_BUILDERS | MODEL_SPECIFIC_OPERATION_SYMBOLS | {OPERATION_DISPATCHER}
    missing_required = sorted(required - set(by_symbol))
    if missing_required:
        errors.append("daily PDF shared path inventory missing required symbols: " + ",".join(missing_required))

    for symbol in sorted(operation_like_symbols(functions)):
        if symbol not in by_symbol:
            errors.append(f"operation-like PDF renderer symbol is not registered in shared path inventory: {symbol}")

    for row in rows:
        symbol = row["symbol_name"]
        path = row["file_path"]
        ownership = row["ownership_class"]
        status = row["status"]
        if ownership not in OWNERSHIP_CLASSES:
            errors.append(f"{symbol} has unsupported ownership_class: {ownership}")
        if status != "active":
            errors.append(f"{symbol} must be active in daily PDF shared path inventory")
        if path != "scripts/generate_chatgpt_side_daily_reports.py":
            errors.append(f"{symbol} must stay in the ChatGPT-side daily renderer inventory scope: {path}")
        if symbol not in functions:
            errors.append(f"{symbol} is registered but no function with that name exists in renderer")

        if symbol in LOW_LEVEL_SHARED_SYMBOLS:
            if ownership != "low_level_shared":
                errors.append(f"{symbol} must be low_level_shared")
            if row["allowed_business_semantics"] != "none":
                errors.append(f"{symbol} is low-level shared but has business semantics")

        if symbol in REPORT_SPECIFIC_BUILDERS and ownership != "report_specific_business":
            errors.append(f"{symbol} must be report_specific_business")

        if symbol in MODEL_SPECIFIC_OPERATION_SYMBOLS and ownership != "model_specific_business":
            errors.append(f"{symbol} must be model_specific_business")

        if symbol == OPERATION_DISPATCHER and ownership != "operation_dispatcher_guarded":
            errors.append(f"{symbol} must be operation_dispatcher_guarded")

    return errors


def validate_source_boundaries(source: str, functions: dict[str, ast.FunctionDef]) -> list[str]:
    errors: list[str] = []

    dispatcher = functions.get(OPERATION_DISPATCHER)
    if not dispatcher:
        errors.append(f"missing operation dispatcher: {OPERATION_DISPATCHER}")
    else:
        body = function_text(source, dispatcher)
        required_tokens = [
            "model_id == VOLUME_BREAKOUT_MODEL_ID",
            "model_id in W_BOTTOM_OPERATION_TABLE_MODEL_IDS",
            "model_id == PRICE_PULLBACK_MODEL_ID",
            "render_volume_range_breakout_operation_section",
            "render_w_bottom_operation_section",
            "render_price_pullback_operation_section",
        ]
        for token in required_tokens:
            if token not in body:
                errors.append(f"operation dispatcher missing explicit guarded route: {token}")
        forbidden_tokens = [
            "model_signal_rows",
            "candidate_model",
            "build_volume_confirmed_operation_table",
            "build_w_bottom_confirmed_operation_table",
            "build_price_pullback_confirmed_operation_table",
        ]
        for token in forbidden_tokens:
            if token in body:
                errors.append(f"operation dispatcher must not infer lifecycle or build tables directly: {token}")

    renderer_rules = {
        "render_volume_range_breakout_operation_section": {
            "required_calls": {"selected_volume_operation_rows_for_pdf"},
            "allowed_prefixes": ("volume_", "render_", "build_volume_", "filter_volume_", "limit_volume_"),
            "forbidden_tokens": ["w_bottom_", "price_pullback_", "model_signal_rows"],
        },
        "render_w_bottom_operation_section": {
            "required_calls": {"selected_w_bottom_operation_rows_for_pdf"},
            "allowed_prefixes": ("w_bottom_", "render_", "build_w_bottom_", "filter_w_bottom_", "limit_w_bottom_"),
            "forbidden_tokens": ["volume_operation_", "price_pullback_", "model_signal_rows"],
        },
        "render_price_pullback_operation_section": {
            "required_calls": {"selected_price_pullback_operation_rows_for_pdf"},
            "allowed_prefixes": (
                "price_pullback_",
                "render_",
                "build_price_pullback_",
                "filter_price_pullback_",
            ),
            "forbidden_tokens": ["volume_operation_", "w_bottom_", "model_signal_rows"],
        },
    }
    for renderer, rule in renderer_rules.items():
        node = functions.get(renderer)
        if not node:
            errors.append(f"missing model operation renderer: {renderer}")
            continue
        calls = ast_call_names(node)
        for call in sorted(rule["required_calls"] - calls):
            errors.append(f"{renderer} missing model-owned operation call: {call}")
        body = function_text(source, node)
        for token in rule["forbidden_tokens"]:
            if token in body:
                errors.append(f"{renderer} crosses model operation boundary with forbidden token: {token}")

    selector_rules = {
        "volume_operation_all_rows_for_pdf": {
            "required_calls": {"volume_operation_frame", "filter_volume_operation_rows_for_line"},
            "forbidden_tokens": ["w_bottom_", "price_pullback_", "model_signal_rows"],
        },
        "selected_volume_operation_rows_for_pdf": {
            "required_calls": {"volume_operation_all_rows_for_pdf"},
            "forbidden_tokens": ["w_bottom_", "price_pullback_", "model_signal_rows"],
        },
        "w_bottom_operation_all_rows_for_pdf": {
            "required_calls": {"w_bottom_operation_frame", "filter_w_bottom_operation_rows_for_line"},
            "forbidden_tokens": ["volume_operation_", "price_pullback_", "model_signal_rows"],
        },
        "selected_w_bottom_operation_rows_for_pdf": {
            "required_calls": {"w_bottom_operation_all_rows_for_pdf"},
            "forbidden_tokens": ["volume_operation_", "price_pullback_", "model_signal_rows"],
        },
        "price_pullback_operation_all_rows_for_pdf": {
            "required_calls": {"price_pullback_operation_frame", "filter_price_pullback_operation_rows_for_line"},
            "forbidden_tokens": ["volume_operation_", "w_bottom_", "model_signal_rows"],
        },
        "selected_price_pullback_operation_rows_for_pdf": {
            "required_calls": {"price_pullback_operation_all_rows_for_pdf"},
            "forbidden_tokens": ["volume_operation_", "w_bottom_", "model_signal_rows"],
        },
    }
    for selector, rule in selector_rules.items():
        node = functions.get(selector)
        if not node:
            errors.append(f"missing model operation selector: {selector}")
            continue
        calls = ast_call_names(node)
        for call in sorted(rule["required_calls"] - calls):
            errors.append(f"{selector} missing model-owned operation call: {call}")
        body = function_text(source, node)
        for token in rule["forbidden_tokens"]:
            if token in body:
                errors.append(f"{selector} crosses model operation boundary with forbidden token: {token}")

    for builder_name in sorted(STOCK_PDF_BUILDERS):
        node = functions.get(builder_name)
        if not node:
            errors.append(f"missing stock PDF builder: {builder_name}")
            continue
        calls = ast_call_names(node)
        if OPERATION_DISPATCHER not in calls:
            errors.append(f"{builder_name} must call {OPERATION_DISPATCHER}")
        direct_operation_renderers = {
            "render_volume_range_breakout_operation_section",
            "render_w_bottom_operation_section",
            "render_price_pullback_operation_section",
        } & calls
        if direct_operation_renderers:
            errors.append(
                f"{builder_name} must route operation sections through dispatcher only: "
                + ",".join(sorted(direct_operation_renderers))
            )

    return errors


def validate() -> list[str]:
    errors: list[str] = []
    try:
        source = read_text(GENERATOR)
        tree = ast.parse(source)
        functions = function_nodes(tree)
    except Exception as exc:
        return [f"unable to parse ChatGPT-side daily renderer: {exc}"]

    try:
        rows = read_inventory()
    except Exception as exc:
        return [f"unable to read daily PDF shared path inventory: {exc}"]

    errors.extend(validate_inventory_rows(rows, functions))
    errors.extend(validate_source_boundaries(source, functions))
    return errors


def main() -> int:
    errors = validate()
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1
    rows = read_inventory()
    print("daily PDF shared path isolation validation passed")
    print(f"validated_inventory={INVENTORY.relative_to(ROOT).as_posix()}")
    print(f"validated_components={len(rows)}")
    print(f"validated_renderer={GENERATOR.relative_to(ROOT).as_posix()}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
