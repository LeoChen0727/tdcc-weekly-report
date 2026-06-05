from __future__ import annotations

import ast
import json
import sys
from pathlib import Path
from typing import Any

sys.path.insert(0, str(Path(__file__).resolve().parent))

from build_daily_candidate_model_layer import build_specs, model_score_common  # noqa: E402
from tracking_utils import LATEST_DIR  # noqa: E402


SOURCE_PATH = Path(__file__).resolve().parent / "build_daily_candidate_model_layer.py"
VALIDATION_JSON = LATEST_DIR / "daily_candidate_model_independence_validation_latest.json"
VALIDATION_MD = LATEST_DIR / "daily_candidate_model_independence_validation_latest.md"

FORBIDDEN_HELPERS = {
    "active_price_attack_for_early_models",
}


def called_names(node: ast.AST) -> set[str]:
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


def validate() -> dict[str, Any]:
    errors: list[str] = []
    warnings: list[str] = []

    source = SOURCE_PATH.read_text(encoding="utf-8")
    tree = ast.parse(source)
    function_nodes = {
        node.name: node
        for node in tree.body
        if isinstance(node, ast.FunctionDef)
    }
    condition_names = {name for name in function_nodes if name.startswith("cond_")}

    for name in sorted(condition_names):
        calls = called_names(function_nodes[name])
        cross_condition_calls = sorted((calls & condition_names) - {name})
        if cross_condition_calls:
            errors.append(f"{name} calls other model condition functions: {cross_condition_calls}")
        forbidden = sorted(calls & FORBIDDEN_HELPERS)
        if forbidden:
            errors.append(f"{name} calls deprecated cross-model helper functions: {forbidden}")

    present_forbidden_helpers = sorted(FORBIDDEN_HELPERS & set(function_nodes))
    if present_forbidden_helpers:
        errors.append(f"deprecated cross-model helpers still exist: {present_forbidden_helpers}")

    specs = [spec for spec in build_specs() if spec.pdf_visibility == "pdf_core_model"]
    condition_func_names = [spec.condition_func.__name__ for spec in specs]
    score_func_names = [spec.score_func.__name__ for spec in specs]
    duplicate_conditions = sorted({name for name in condition_func_names if condition_func_names.count(name) > 1})
    duplicate_scores = sorted({name for name in score_func_names if score_func_names.count(name) > 1})
    if duplicate_conditions:
        errors.append(f"duplicate pdf core condition functions: {duplicate_conditions}")
    if duplicate_scores:
        errors.append(f"duplicate pdf core score functions: {duplicate_scores}")
    if any(spec.score_func is model_score_common for spec in specs):
        errors.append("pdf core models must not use legacy shared model_score_common")

    return {
        "status": "pass" if not errors else "fail",
        "source_path": str(SOURCE_PATH),
        "pdf_core_model_count": len(specs),
        "condition_function_count": len(condition_func_names),
        "score_function_count": len(score_func_names),
        "errors": errors,
        "warnings": warnings,
    }


def write_outputs(result: dict[str, Any]) -> None:
    LATEST_DIR.mkdir(parents=True, exist_ok=True)
    VALIDATION_JSON.write_text(
        json.dumps(result, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    lines = [
        "# Daily Candidate Model Independence Validation",
        "",
        f"- status: {result['status']}",
        f"- pdf_core_model_count: {result['pdf_core_model_count']}",
        f"- condition_function_count: {result['condition_function_count']}",
        f"- score_function_count: {result['score_function_count']}",
        "",
        "## Errors",
    ]
    errors = result.get("errors") or []
    lines.extend([f"- {err}" for err in errors] or ["- none"])
    lines.append("")
    lines.append("## Warnings")
    warnings = result.get("warnings") or []
    lines.extend([f"- {warning}" for warning in warnings] or ["- none"])
    VALIDATION_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    result = validate()
    write_outputs(result)
    print(json.dumps(result, ensure_ascii=False, indent=2))
    if result["status"] != "pass":
        raise SystemExit(1)


if __name__ == "__main__":
    main()
