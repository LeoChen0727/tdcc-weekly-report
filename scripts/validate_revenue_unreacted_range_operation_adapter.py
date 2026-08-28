from __future__ import annotations

import argparse
import ast
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_MODULE = ROOT / "scripts/revenue_unreacted_range_operation_adapter.py"


def _load_module(module_path: Path):
    import importlib.util

    spec = importlib.util.spec_from_file_location(
        "revenue_unreacted_range_operation_adapter_validated",
        module_path,
    )
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load adapter module: {module_path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def _validate_no_runtime_writer(module_path: Path) -> list[str]:
    errors: list[str] = []
    tree = ast.parse(module_path.read_text(encoding="utf-8"), filename=str(module_path))
    forbidden_imports = {"pandas", "reportlab", "pypdf"}
    forbidden_calls = {
        "open",
        "write_csv",
        "write_text",
        "write_bytes",
        "to_csv",
        "to_json",
    }
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            for alias in node.names:
                if alias.name.split(".", 1)[0] in forbidden_imports:
                    errors.append(f"disabled adapter imports runtime dependency {alias.name}")
        elif isinstance(node, ast.ImportFrom):
            if (node.module or "").split(".", 1)[0] in forbidden_imports:
                errors.append(f"disabled adapter imports runtime dependency {node.module}")
        elif isinstance(node, ast.Call):
            func = node.func
            name = ""
            if isinstance(func, ast.Name):
                name = func.id
            elif isinstance(func, ast.Attribute):
                name = func.attr
            if name in forbidden_calls:
                errors.append(f"disabled adapter contains forbidden writer call {name}")
        elif isinstance(node, ast.If):
            test = node.test
            if (
                isinstance(test, ast.Compare)
                and isinstance(test.left, ast.Name)
                and test.left.id == "__name__"
            ):
                errors.append("disabled adapter must not expose a command-line entrypoint")
    return sorted(set(errors))


def validate_disabled_preparation(module_path: Path) -> list[str]:
    errors: list[str] = []
    if not module_path.is_file():
        return [f"disabled adapter module is missing: {module_path}"]
    errors.extend(_validate_no_runtime_writer(module_path))
    if errors:
        return errors
    try:
        module = _load_module(module_path)
        module.validate_disabled_preparation()
    except Exception as exc:  # fail closed at the validator boundary
        errors.append(f"disabled adapter in-memory contract failed: {exc}")
        return errors

    expected = {
        "MODEL_ID": "revenue_unreacted_range",
        "MODEL_VARIANT_ID": "source_mid_falling",
        "MODEL_VARIANT_VERSION": "v2",
        "OPERATION_MODULE_ID": (
            "revenue_unreacted_range_source_mid_falling_v2_operation_v1"
        ),
        "ADAPTER_SCHEMA_VERSION": (
            "revenue_unreacted_range_operation_section_schema_v1"
        ),
        "LIFECYCLE_CONTRACT_VERSION": "revenue_unreacted_range_lifecycle_v1",
        "ADAPTER_MODE": "disabled_preparation",
        "RULE_SPEC_ID": "revenue_unreacted_range_source_mid_falling_d30_v1",
        "RULE_CANONICAL_SHA256": (
            "1d9fd669251180d2f7edbedb30b121660a218bad232ca49573353000db155633"
        ),
        "SELECTION_POLICY": "fixed_preselected_no_reselection",
        "HOLDOUT_USE_POLICY": "natural_maturity_observation_only_no_tuning",
        "CONFIRMATION_RULE_ID": "d1_analysis_close_above_trigger_analysis_close",
        "ENTRY_RULE_ID": "d2_analysis_open",
        "EXIT_RULE_ID": "d30_analysis_close_offset29",
        "STOP_POLICY_ID": "none_no_stop_reference",
        "CONFIRMATION_OFFSET_TRADING_DAYS": 1,
        "ENTRY_OFFSET_TRADING_DAYS": 2,
        "HOLDING_DAYS": 30,
        "HOLDING_SESSION_INDEX_OFFSET": 29,
        "ENTRY_PRICE_BASIS": "analysis_open",
        "EXIT_PRICE_BASIS": "fixed_future_close",
        "PRICE_CONFIRMATION_BASIS": "close_only",
    }
    for name, value in expected.items():
        if getattr(module, name, None) != value:
            errors.append(
                f"disabled adapter fixed contract drift: {name}="
                f"{getattr(module, name, None)!r}; expected={value!r}"
            )

    rows = module.build_disabled_empty_rows()
    if len(rows) != 8:
        errors.append(f"disabled adapter must expose exactly 8 in-memory rows, got {len(rows)}")
    for field_name in module.PERMISSION_FIELDS:
        if any(row.get(field_name) is not False for row in rows):
            errors.append(f"disabled adapter permission must remain false: {field_name}")
    if any(row.get("row_type") != "empty_state" for row in rows):
        errors.append("disabled adapter must not expose operation data rows")
    return errors


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Validate revenue_unreacted_range disabled operation adapter preparation."
    )
    parser.add_argument(
        "--phase",
        choices=("disabled-preparation", "production-approval"),
        default="disabled-preparation",
    )
    parser.add_argument("--module", type=Path, default=DEFAULT_MODULE)
    # Accepted for compatibility with the future production-approval command.
    # This disabled validator never reads or writes any artifact/history path.
    parser.add_argument("--artifact", type=Path)
    parser.add_argument("--history-directory", type=Path)
    parser.add_argument("--history-base-ref", default="")
    parser.add_argument("--expected-artifact-version", default="")
    parser.add_argument("--expected-artifact-canonical-sha256", default="")
    parser.add_argument("--expected-module-canonical-sha256", default="")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    if args.phase == "production-approval":
        print(
            "ERROR: revenue_unreacted_range adapter is disabled preparation only; "
            "production approval, runtime artifacts, PDF, and packet consumption are forbidden"
        )
        return 1
    errors = validate_disabled_preparation(args.module.resolve())
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1
    print(
        "revenue_unreacted_range disabled adapter preparation validation passed: "
        "8 in-memory empty rows; no runtime artifact; all permissions false"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
