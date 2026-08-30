from __future__ import annotations

import ast
import csv
from collections import defaultdict
from pathlib import Path
from typing import Any, Iterable


ROOT = Path(__file__).resolve().parents[1]
CONTRACT_PATH = ROOT / "config" / "daily_operation_adapter_protected_field_contract.csv"
EXPECTED_CONTRACT_VERSION = "daily_operation_adapter_protected_fields_v1"
EXPECTED_MODEL_IDS = {
    "volume_range_breakout_v2_low_position_volume_attack",
    "volume_range_breakout_v2_mid_position_momentum_attack",
    "volume_range_breakout_v2_high_position_volume_attack",
    "w_bottom_right_side",
    "neckline_volume_breakout_confirmation",
    "price_pullback_23ema",
    "revenue_unreacted_range",
}
REQUIRED_COLUMNS = {
    "contract_version",
    "model_id",
    "producer_path",
    "validator_path",
    "artifact_path",
    "lifecycle_state",
    "pdf_section",
    "row_type",
    "quality_field",
    "allowed_quality_values",
    "allowed_row_action_status_values",
    "allowed_buy_rank_eligible_values",
    "allowed_operation_status_values",
    "allowed_operation_status_zh_values",
    "allowed_adapter_note_values",
    "state_test_path",
    "required_state_test_names",
}
PROTECTED_ROW_FIELDS = {
    "pdf_section",
    "row_type",
    "operation_status",
    "operation_status_zh",
    "quality_status_zh",
    "operation_quality",
    "row_action_status",
    "buy_rank_eligible",
    "adapter_note_zh",
}
PROTECTED_MODULE_GLOBALS = {"SECTION_ZH", "SECTION_EMPTY_NOTE_ZH", "OUTPUT_COLUMNS"}


def _safe_text(value: Any) -> str:
    return "" if value is None else str(value).strip()


def _split_values(value: Any) -> set[str]:
    return {item.strip() for item in _safe_text(value).split("||") if item.strip()}


def _read_contract() -> tuple[list[str], list[dict[str, str]]]:
    if not CONTRACT_PATH.exists():
        return [], []
    with CONTRACT_PATH.open("r", encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle)
        return list(reader.fieldnames or []), [dict(row) for row in reader]


def _state_for_row(row: dict[str, Any]) -> str:
    if _safe_text(row.get("row_type")) == "empty_state":
        return "empty"
    return {
        "pending_confirmation": "pending",
        "confirmed_operation": "confirmed",
        "confirmed_unranked_operation": "confirmed_unranked",
        "active_operation": "active",
    }.get(_safe_text(row.get("pdf_section")), "")


def _contract_index(rows: Iterable[dict[str, str]]) -> dict[tuple[str, str], dict[str, str]]:
    return {(_safe_text(row.get("model_id")), _safe_text(row.get("lifecycle_state"))): row for row in rows}


def validate_adapter_frame(
    frame: Any,
    model_id: str,
    required_states: Iterable[str] = (),
) -> list[str]:
    """Validate row-level protected fields without importing producer business logic."""
    fields, contract_rows = _read_contract()
    if not fields or not contract_rows:
        return [f"missing protected-field contract: {CONTRACT_PATH.relative_to(ROOT).as_posix()}"]
    index = _contract_index(contract_rows)
    model_rows = [
        {str(key): value for key, value in row.items()}
        for row in frame.to_dict("records")
        if _safe_text(row.get("model_id")) == model_id
    ]
    errors: list[str] = []
    seen_states: set[str] = set()
    if not model_rows:
        errors.append(f"{model_id}: protected-field validation received no rows")
        return errors

    for row_number, row in enumerate(model_rows, start=1):
        state = _state_for_row(row)
        if not state:
            errors.append(
                f"{model_id} row {row_number}: unsupported lifecycle mapping "
                f"row_type={_safe_text(row.get('row_type'))!r} pdf_section={_safe_text(row.get('pdf_section'))!r}"
            )
            continue
        seen_states.add(state)
        contract = index.get((model_id, state))
        if contract is None:
            errors.append(f"{model_id} row {row_number}: lifecycle state {state!r} is not registered")
            continue

        checks = (
            (contract["quality_field"], "allowed_quality_values"),
            ("row_action_status", "allowed_row_action_status_values"),
            ("buy_rank_eligible", "allowed_buy_rank_eligible_values"),
            ("operation_status", "allowed_operation_status_values"),
            ("operation_status_zh", "allowed_operation_status_zh_values"),
            ("adapter_note_zh", "allowed_adapter_note_values"),
        )
        for field, allowed_column in checks:
            allowed = _split_values(contract.get(allowed_column))
            actual = _safe_text(row.get(field))
            if actual not in allowed:
                errors.append(
                    f"{model_id} row {row_number} state={state}: {field}={actual!r} "
                    f"not in canonical values {sorted(allowed)!r}"
                )

        expected_row_type = _safe_text(contract.get("row_type"))
        actual_row_type = _safe_text(row.get("row_type"))
        if actual_row_type != expected_row_type:
            errors.append(
                f"{model_id} row {row_number} state={state}: row_type={actual_row_type!r}; "
                f"expected {expected_row_type!r}"
            )
        expected_section = _safe_text(contract.get("pdf_section"))
        actual_section = _safe_text(row.get("pdf_section"))
        if expected_section != "*" and actual_section != expected_section:
            errors.append(
                f"{model_id} row {row_number} state={state}: pdf_section={actual_section!r}; "
                f"expected {expected_section!r}"
            )

    missing_states = set(required_states) - seen_states
    if missing_states:
        errors.append(f"{model_id}: missing required lifecycle states {sorted(missing_states)!r}")
    return errors


def _string_key(node: ast.AST) -> str:
    if isinstance(node, ast.Constant) and isinstance(node.value, str):
        return node.value
    return ""


def _subscript_field(node: ast.AST) -> tuple[str, str] | None:
    if not isinstance(node, ast.Subscript) or not isinstance(node.value, ast.Name):
        return None
    field = _string_key(node.slice)
    if not field:
        return None
    return node.value.id, field


def _dict_fields(node: ast.Dict) -> list[str]:
    return [_string_key(key) for key in node.keys if key is not None and _string_key(key)]


def _validate_producer_ast(path: Path) -> list[str]:
    errors: list[str] = []
    try:
        display_path = path.relative_to(ROOT).as_posix()
    except ValueError:
        display_path = path.as_posix()
    try:
        tree = ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
    except (OSError, SyntaxError) as exc:
        return [f"cannot parse protected operation producer {display_path}: {exc}"]

    global_writes: defaultdict[str, list[int]] = defaultdict(list)
    for node in tree.body:
        targets: list[ast.expr] = []
        if isinstance(node, ast.Assign):
            targets = list(node.targets)
        elif isinstance(node, ast.AnnAssign):
            targets = [node.target]
        for target in targets:
            if isinstance(target, ast.Name) and target.id in PROTECTED_MODULE_GLOBALS:
                global_writes[target.id].append(node.lineno)
    for name, lines in global_writes.items():
        if len(lines) > 1:
            errors.append(
                f"{display_path}: protected global {name} assigned more than once at lines {lines}"
            )

    for node in ast.walk(tree):
        if isinstance(node, ast.Dict):
            fields = [field for field in _dict_fields(node) if field in PROTECTED_ROW_FIELDS]
            duplicates = sorted({field for field in fields if fields.count(field) > 1})
            if duplicates:
                errors.append(
                    f"{display_path}:{node.lineno}: duplicate protected dict keys {duplicates}"
                )

    for function in (node for node in ast.walk(tree) if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef))):
        writes: defaultdict[tuple[str, str], list[int]] = defaultdict(list)
        for node in ast.walk(function):
            if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)) and node is not function:
                continue
            if isinstance(node, ast.Assign):
                for target in node.targets:
                    item = _subscript_field(target)
                    if item and item[1] in PROTECTED_ROW_FIELDS:
                        writes[item].append(node.lineno)
                    if isinstance(target, ast.Name) and isinstance(node.value, ast.Dict):
                        for field in _dict_fields(node.value):
                            if field in PROTECTED_ROW_FIELDS:
                                writes[(target.id, field)].append(node.lineno)
            if (
                isinstance(node, ast.Call)
                and isinstance(node.func, ast.Attribute)
                and node.func.attr == "update"
                and isinstance(node.func.value, ast.Name)
                and node.args
                and isinstance(node.args[0], ast.Dict)
            ):
                for field in _dict_fields(node.args[0]):
                    if field in PROTECTED_ROW_FIELDS:
                        writes[(node.func.value.id, field)].append(node.lineno)
        for (variable, field), lines in writes.items():
            if len(lines) > 1:
                errors.append(
                    f"{display_path}:{function.lineno} function {function.name} "
                    f"writes protected field {variable}[{field!r}] more than once at lines {lines}"
                )
    return errors


def validate() -> list[str]:
    errors: list[str] = []
    fields, rows = _read_contract()
    if not fields:
        return [f"missing protected-field contract: {CONTRACT_PATH.relative_to(ROOT).as_posix()}"]
    missing_columns = sorted(REQUIRED_COLUMNS - set(fields))
    if missing_columns:
        return [f"protected-field contract missing columns: {missing_columns}"]
    if not rows:
        return ["protected-field contract must contain rows"]

    versions = {_safe_text(row.get("contract_version")) for row in rows}
    if versions != {EXPECTED_CONTRACT_VERSION}:
        errors.append(f"protected-field contract version drift: {sorted(versions)!r}")
    model_ids = {_safe_text(row.get("model_id")) for row in rows}
    if model_ids != EXPECTED_MODEL_IDS:
        errors.append(
            "protected-field contract mature-model coverage drift: "
            f"missing={sorted(EXPECTED_MODEL_IDS - model_ids)!r} extra={sorted(model_ids - EXPECTED_MODEL_IDS)!r}"
        )

    keys: set[tuple[str, str]] = set()
    producers: set[Path] = set()
    for row_number, row in enumerate(rows, start=2):
        key = (_safe_text(row.get("model_id")), _safe_text(row.get("lifecycle_state")))
        if key in keys:
            errors.append(f"protected-field contract duplicate model/state at row {row_number}: {key!r}")
        keys.add(key)
        for field in (
            "allowed_quality_values",
            "allowed_row_action_status_values",
            "allowed_buy_rank_eligible_values",
            "allowed_operation_status_values",
            "allowed_operation_status_zh_values",
            "allowed_adapter_note_values",
        ):
            if not _split_values(row.get(field)):
                errors.append(f"protected-field contract row {row_number} has empty {field}")
        for path_field in ("producer_path", "validator_path", "artifact_path", "state_test_path"):
            path = ROOT / _safe_text(row.get(path_field))
            if not path.exists():
                errors.append(
                    f"protected-field contract row {row_number} missing {path_field}: "
                    f"{_safe_text(row.get(path_field))}"
                )
        producer = ROOT / _safe_text(row.get("producer_path"))
        if producer.exists():
            producers.add(producer)
        test_path = ROOT / _safe_text(row.get("state_test_path"))
        if test_path.exists():
            test_source = test_path.read_text(encoding="utf-8")
            for test_name in _split_values(row.get("required_state_test_names")):
                if f"def {test_name}(" not in test_source:
                    errors.append(
                        f"{test_path.relative_to(ROOT).as_posix()} missing registered state test {test_name}"
                    )

    required_states = {
        model_id: {row[1] for row in keys if row[0] == model_id}
        for model_id in EXPECTED_MODEL_IDS
    }
    for model_id in EXPECTED_MODEL_IDS:
        minimum = {"confirmed", "active", "empty"}
        if model_id.startswith("volume_range_breakout_v2_"):
            minimum |= {"pending", "confirmed_unranked"}
        if not minimum.issubset(required_states.get(model_id, set())):
            errors.append(
                f"{model_id}: protected-field contract missing lifecycle states "
                f"{sorted(minimum - required_states.get(model_id, set()))!r}"
            )

    for producer in sorted(producers):
        errors.extend(_validate_producer_ast(producer))
    return errors


def main() -> int:
    errors = validate()
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1
    print("daily operation adapter protected-field contract validation passed")
    print(f"validated_contract={CONTRACT_PATH.relative_to(ROOT).as_posix()}")
    print(f"validated_models={len(EXPECTED_MODEL_IDS)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
