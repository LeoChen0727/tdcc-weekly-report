from __future__ import annotations

import argparse
import ast
import csv
import re
from datetime import datetime
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MODEL_ID = "revenue_unreacted_range"
EFFECTIVE_FROM = "2026-07-16"
EFFECTIVE_DATE = "20260716"
VALIDATION_PHASE_FULL = "full"
VALIDATION_PHASE_RUNTIME = "runtime"
VALIDATION_PHASES = (VALIDATION_PHASE_FULL, VALIDATION_PHASE_RUNTIME)
APPROVED_NON_FINANCIAL_EVENT_TYPES = {
    "new_order",
    "customer_win",
    "capacity_expansion",
    "mass_production",
    "technology_validation",
    "product_certification",
    "policy_tailwind",
    "exhibition_catalyst",
    "sector_rotation",
    "international_peer_momentum",
}
FINANCIAL_FIELDS = (
    "EPS",
    "毛利率",
    "營益率",
    "營業利益",
    "業外",
    "淨利",
)
LEGACY_SCORE_COMPONENTS = (
    "EPS confirmation tag",
    "gross margin confirmation tag",
    "catalyst tag +3",
)
APPROVED_EVENT_COMPONENT = "核准非財務事件 +3"
FINANCIAL_CATALYST_PROXY_FIELDS = frozenset(
    {
        "fundamental_catalyst_score",
        "fundamental_catalyst_tags",
        "eps_surprise",
        "eps_surprise_flag",
        "earnings_acceleration",
        "earnings_acceleration_flag",
        "margin_improvement",
        "margin_improvement_flag",
        "profit_turnaround",
        "profit_turnaround_flag",
        "undervalued_after_eps",
        "undervalued_after_eps_flag",
        "revenue_good_eps_unconfirmed",
        "revenue_good_eps_unconfirmed_flag",
        "gross_margin",
        "operating_margin",
        "net_margin",
    }
)
FINANCIAL_SOURCE_PATTERNS = (
    re.compile(r"(^|_)eps($|_)"),
    re.compile(r"fundamental_catalyst"),
    re.compile(r"gross_margin"),
    re.compile(r"operating_margin"),
    re.compile(r"operating_income"),
    re.compile(r"non_operating"),
    re.compile(r"net_income"),
)


def _read_rows(path: Path) -> list[dict[str, str]]:
    if not path.exists():
        raise FileNotFoundError(path)
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        return [dict(row) for row in csv.DictReader(handle)]


def _financial_statement_source_fields(root: Path) -> frozenset[str]:
    mapping_rows = _read_rows(
        root / "config/daily_model_financial_statement_metric_mapping.csv"
    )
    canonical_metrics = {
        row.get("canonical_metric", "").strip().lower()
        for row in mapping_rows
        if row.get("canonical_metric", "").strip()
    }
    return frozenset(canonical_metrics | set(FINANCIAL_CATALYST_PROXY_FIELDS))


def _single_row(rows: list[dict[str, str]], *, key: str, value: str) -> dict[str, str] | None:
    matches = [row for row in rows if row.get(key, "") == value]
    return matches[0] if len(matches) == 1 else None


def _source_index(value: str) -> str:
    text = str(value or "").strip()
    if re.fullmatch(r"\d+\.0", text):
        return text[:-2]
    return text


def _function_node(tree: ast.Module, name: str) -> ast.FunctionDef | None:
    for node in tree.body:
        if isinstance(node, ast.FunctionDef) and node.name == name:
            return node
    return None


def _module_literal_string_aliases(tree: ast.Module) -> dict[str, str]:
    assignments: dict[str, ast.AST] = {}
    for node in tree.body:
        if isinstance(node, ast.Assign):
            for target in node.targets:
                if isinstance(target, ast.Name):
                    assignments[target.id] = node.value
        elif isinstance(node, ast.AnnAssign) and isinstance(node.target, ast.Name):
            assignments[node.target.id] = node.value

    resolved: dict[str, str] = {}

    def resolve(node: ast.AST | None) -> str | None:
        if isinstance(node, ast.Constant) and isinstance(node.value, str):
            return node.value
        if isinstance(node, ast.Name):
            return resolved.get(node.id)
        if isinstance(node, ast.BinOp) and isinstance(node.op, ast.Add):
            left = resolve(node.left)
            right = resolve(node.right)
            if left is not None and right is not None:
                return left + right
        return None

    for _ in range(len(assignments) + 1):
        changed = False
        for name, value_node in assignments.items():
            if name in resolved:
                continue
            value = resolve(value_node)
            if value is not None:
                resolved[name] = value
                changed = True
        if not changed:
            break
    return resolved


def _reachable_function_nodes(
    tree: ast.Module, roots: tuple[str, ...]
) -> dict[str, ast.FunctionDef]:
    functions = {
        node.name: node for node in tree.body if isinstance(node, ast.FunctionDef)
    }
    reachable: dict[str, ast.FunctionDef] = {}
    pending = list(roots)
    while pending:
        name = pending.pop()
        if name in reachable or name not in functions:
            continue
        function = functions[name]
        reachable[name] = function
        for node in ast.walk(function):
            if not isinstance(node, ast.Call) or not isinstance(node.func, ast.Name):
                continue
            if node.func.id in functions and node.func.id not in reachable:
                pending.append(node.func.id)
    return reachable


def _financial_reference_hits(
    tree: ast.Module,
    roots: tuple[str, ...],
    forbidden_fields: frozenset[str] = FINANCIAL_CATALYST_PROXY_FIELDS,
) -> list[str]:
    hits: list[str] = []
    aliases = _module_literal_string_aliases(tree)
    for function_name, function in _reachable_function_nodes(tree, roots).items():
        for node in ast.walk(function):
            values: list[str] = []
            if isinstance(node, ast.Name):
                values.append(node.id)
                if isinstance(node.ctx, ast.Load) and node.id in aliases:
                    values.append(aliases[node.id])
            elif isinstance(node, ast.Attribute):
                values.append(node.attr)
            elif isinstance(node, ast.Constant) and isinstance(node.value, str):
                values.append(node.value)
            for value in values:
                normalized = value.strip().lower()
                padded = f"_{normalized}_"
                exact_or_qualified_field = any(
                    f"_{field}_" in padded for field in forbidden_fields
                )
                if exact_or_qualified_field:
                    hits.append(f"{function_name}:{normalized}")
                    continue
                for pattern in FINANCIAL_SOURCE_PATTERNS:
                    if pattern.search(normalized):
                        hits.append(f"{function_name}:{normalized}")
                        break
    return sorted(set(hits))


def _model_spec_node(tree: ast.Module) -> ast.Call | None:
    for node in ast.walk(tree):
        if not isinstance(node, ast.Call) or not isinstance(node.func, ast.Name):
            continue
        if node.func.id != "ModelSpec" or not node.args:
            continue
        first = node.args[0]
        if isinstance(first, ast.Constant) and first.value == MODEL_ID:
            return node
    return None


def _assigned_literal_set(function: ast.FunctionDef, name: str) -> set[str] | None:
    for node in ast.walk(function):
        if not isinstance(node, ast.Assign) or len(node.targets) != 1:
            continue
        target = node.targets[0]
        if not isinstance(target, ast.Name) or target.id != name:
            continue
        try:
            value = ast.literal_eval(node.value)
        except (ValueError, TypeError):
            return None
        if isinstance(value, (set, tuple, list)):
            return {str(item) for item in value}
    return None


def _strict_event_bonus_errors(function: ast.FunctionDef) -> list[str]:
    errors: list[str] = []
    event_source_references = [
        node
        for node in ast.walk(function)
        if isinstance(node, ast.Constant)
        and isinstance(node.value, str)
        and "_event_catalyst_tags_" in f"_{node.value.strip().lower()}_"
    ]
    event_type_assignments = [
        node
        for node in ast.walk(function)
        if isinstance(node, ast.Assign)
        and any(isinstance(target, ast.Name) and target.id == "event_type" for target in node.targets)
    ]
    event_type_loads = [
        node
        for node in ast.walk(function)
        if isinstance(node, ast.Name)
        and node.id == "event_type"
        and isinstance(node.ctx, ast.Load)
    ]
    if len(event_source_references) != 1:
        errors.append("event_catalyst_tags must be read exactly once by the revenue scorer")
    if len(event_type_assignments) != 1 or len(event_type_loads) != 1:
        errors.append("event_type may be assigned once and used only by the strict allowlist branch")
    component_occurrences = sum(
        1
        for node in ast.walk(function)
        if isinstance(node, ast.Constant) and node.value == APPROVED_EVENT_COMPONENT
    )
    event_bonus_ifs: list[ast.If] = []
    for node in ast.walk(function):
        if not isinstance(node, ast.If):
            continue
        if any(
            isinstance(child, ast.Constant) and child.value == APPROVED_EVENT_COMPONENT
            for statement in node.body
            for child in ast.walk(statement)
        ):
            event_bonus_ifs.append(node)
    if component_occurrences != 1 or len(event_bonus_ifs) != 1:
        return [
            "approved non-financial event bonus must occur in exactly one guarded branch"
        ]

    branch = event_bonus_ifs[0]
    test = branch.test
    strict_membership = (
        isinstance(test, ast.Compare)
        and isinstance(test.left, ast.Name)
        and test.left.id == "event_type"
        and len(test.ops) == 1
        and isinstance(test.ops[0], ast.In)
        and len(test.comparators) == 1
        and isinstance(test.comparators[0], ast.Name)
        and test.comparators[0].id == "approved_non_financial_event_types"
    )
    if not strict_membership:
        errors.append(
            "event bonus condition must be a pure exact-membership comparison without OR bypass"
        )
    score_adds = [
        node
        for statement in branch.body
        for node in ast.walk(statement)
        if isinstance(node, ast.AugAssign)
        and isinstance(node.target, ast.Name)
        and node.target.id == "score"
        and isinstance(node.op, ast.Add)
        and isinstance(node.value, ast.Constant)
        and node.value.value == 3
    ]
    component_appends = [
        node
        for statement in branch.body
        for node in ast.walk(statement)
        if isinstance(node, ast.Call)
        and isinstance(node.func, ast.Attribute)
        and isinstance(node.func.value, ast.Name)
        and node.func.value.id == "comps"
        and node.func.attr == "append"
        and len(node.args) == 1
        and isinstance(node.args[0], ast.Constant)
        and node.args[0].value == APPROVED_EVENT_COMPONENT
    ]
    if len(branch.body) != 2 or len(score_adds) != 1 or len(component_appends) != 1:
        errors.append("event bonus branch must contain only score +3 and its approved component")
    if branch.orelse:
        errors.append("event bonus branch must not define an alternate scoring path")
    return errors


def _reachable_event_source_locations(
    functions: dict[str, ast.FunctionDef],
    aliases: dict[str, str] | None = None,
) -> list[str]:
    aliases = aliases or {}
    locations: list[str] = []
    for function_name, function in functions.items():
        for node in ast.walk(function):
            if (
                isinstance(node, ast.Constant)
                and isinstance(node.value, str)
                and "_event_catalyst_tags_" in f"_{node.value.strip().lower()}_"
            ):
                locations.append(function_name)
            elif (
                isinstance(node, ast.Name)
                and isinstance(node.ctx, ast.Load)
                and node.id in aliases
                and "_event_catalyst_tags_" in f"_{aliases[node.id].strip().lower()}_"
            ):
                locations.append(function_name)
    return sorted(locations)


def _classify_history_dates(
    revenue_history: list[dict[str, str]],
) -> tuple[int, int, list[str]]:
    errors: list[str] = []
    pre_v2 = 0
    post_v2 = 0
    effective_date = datetime.strptime(EFFECTIVE_DATE, "%Y%m%d").date()
    for index, row in enumerate(revenue_history, start=2):
        signal_date_text = row.get("signal_date", "")
        if not re.fullmatch(r"\d{8}", signal_date_text):
            errors.append(
                f"revenue history row {index} has malformed signal_date={signal_date_text!r}"
            )
            continue
        try:
            signal_date = datetime.strptime(signal_date_text, "%Y%m%d").date()
        except ValueError:
            errors.append(
                f"revenue history row {index} has invalid signal_date={signal_date_text!r}"
            )
            continue
        if signal_date < effective_date:
            pre_v2 += 1
        else:
            post_v2 += 1
    return pre_v2, post_v2, errors


def _current_promotion_block_errors(root: Path) -> tuple[list[str], int]:
    errors: list[str] = []
    controls = 0

    parity_rows = _read_rows(root / "output/latest/model_contract_parity_latest.csv")
    parity = _single_row(parity_rows, key="model_id", value=MODEL_ID)
    if parity is None:
        errors.append("model contract parity must contain exactly one revenue row")
    elif (
        parity.get("parity_status") != "warning_research_variant_only"
        or parity.get("promotion_required") != "True"
        or "do_not_promote" not in parity.get("recommended_action", "")
    ):
        errors.append("revenue parity must remain research-only and promotion-blocked")
    else:
        controls += 1

    readiness_rows = _read_rows(root / "output/latest/model_operation_readiness_latest.csv")
    readiness = _single_row(readiness_rows, key="model_id", value=MODEL_ID)
    if readiness is None:
        errors.append("model operation readiness must contain exactly one revenue row")
    elif (
        readiness.get("approved_for_daily") != "False"
        or readiness.get("presentation_allowed") != "False"
        or readiness.get("operation_directive_level") != "no_operation_directive"
    ):
        errors.append("revenue operation readiness must remain non-formal and non-presentable")
    else:
        controls += 1

    return errors, controls


def _legacy_history_quarantine_errors(root: Path) -> tuple[list[str], int]:
    errors: list[str] = []
    controls = 0

    condition_rows = _read_rows(root / "config/daily_model_condition_spec.csv")
    condition = _single_row(condition_rows, key="model_id", value=MODEL_ID)
    if condition is None:
        errors.append("daily_model_condition_spec must contain exactly one revenue row")
    elif (
        condition.get("research_baseline_status") != "proxy_only"
        or condition.get("operation_contract") != "none"
    ):
        errors.append("revenue condition spec must remain proxy_only with no operation contract")
    else:
        controls += 1

    evidence_rows = _read_rows(root / "config/formal_model_evidence_pins.csv")
    if any(row.get("model_id") == MODEL_ID for row in evidence_rows):
        errors.append("revenue_unreacted_range must not have a formal evidence pin")
    else:
        controls += 1

    current_errors, current_controls = _current_promotion_block_errors(root)
    errors.extend(current_errors)
    controls += current_controls

    signal_log = "output/history/daily_candidate_models/daily_candidate_model_signal_log.csv"
    background_rows = _read_rows(root / "config/daily_model_background_data_registry.csv")
    signal_log_background_uses = [
        row for row in background_rows if signal_log in row.get("source_artifacts", "")
    ]
    for row in signal_log_background_uses:
        if (
            row.get("point_in_time_status") != "coverage_backfill_audit_only"
            or "do not use audit rows as a model-specific gate score recommendation or production rule"
            not in row.get("forbidden_use", "")
        ):
            errors.append(
                "daily signal log background consumers must remain coverage-only and non-formal"
            )
    lineage_rows = _read_rows(root / "config/report_artifact_lineage.csv")
    revenue_lineage_consumers = [
        row
        for row in lineage_rows
        if signal_log in row.get("source_artifacts", "")
        and MODEL_ID in " ".join(row.values())
    ]
    if revenue_lineage_consumers:
        errors.append("revenue formal/report lineage must not consume the pre-v2 signal log")
    revenue_consumer_scripts = [
        path
        for path in (root / "scripts").glob("*revenue_unreacted_range*.py")
        if path.name != Path(__file__).name
        and "daily_candidate_model_signal_log.csv" in path.read_text(encoding="utf-8")
    ]
    if revenue_consumer_scripts:
        errors.append(
            "revenue-owned scripts must not consume the pre-v2 signal log: "
            + ",".join(path.name for path in revenue_consumer_scripts)
        )
    if not signal_log_background_uses:
        errors.append("expected coverage-only signal-log lineage is missing")
    if not any(
        row.get("data_family_id") == "monthly_revenue_coverage_backfill_audit"
        for row in signal_log_background_uses
    ):
        errors.append("signal-log use must remain pinned to the monthly revenue coverage audit")
    if not revenue_lineage_consumers and not revenue_consumer_scripts and not errors:
        controls += 1

    return errors, controls


def _static_semantic_errors(root: Path) -> list[str]:
    errors: list[str] = []
    source_path = root / "scripts/build_daily_candidate_model_layer.py"
    source_text = source_path.read_text(encoding="utf-8")
    tree = ast.parse(source_text, filename=str(source_path))
    semantic_roots = ("cond_revenue_unreacted", "score_revenue_unreacted")
    reachable = _reachable_function_nodes(tree, semantic_roots)
    missing_roots = sorted(set(semantic_roots) - set(reachable))
    if missing_roots:
        errors.append(
            "missing revenue_unreacted_range semantic roots: " + ",".join(missing_roots)
        )
    if "strong_revenue" not in reachable:
        errors.append("revenue_unreacted_range must retain the monthly-revenue gate")
    event_source_locations = _reachable_event_source_locations(
        reachable, _module_literal_string_aliases(tree)
    )
    if event_source_locations != ["score_revenue_unreacted"]:
        errors.append(
            "event_catalyst_tags must be consumed exactly once in score_revenue_unreacted: "
            f"actual={event_source_locations}"
        )
    financial_source_fields = _financial_statement_source_fields(root)
    financial_hits = _financial_reference_hits(
        tree, semantic_roots, financial_source_fields
    )
    if financial_hits:
        errors.append(
            "revenue_unreacted_range reachable semantics reference financial-statement inputs: "
            + ",".join(financial_hits)
        )
    score_function = _function_node(tree, "score_revenue_unreacted")
    if score_function is None:
        errors.append("missing score_revenue_unreacted")
    else:
        function_text = ast.get_source_segment(source_text, score_function) or ""
        if "fundamental_catalyst_tags" in function_text:
            errors.append("score_revenue_unreacted must not consume fundamental_catalyst_tags")
        for legacy in LEGACY_SCORE_COMPONENTS:
            if legacy in function_text:
                errors.append(f"score_revenue_unreacted retains legacy component: {legacy}")
        actual_allowlist = _assigned_literal_set(
            score_function, "approved_non_financial_event_types"
        )
        if actual_allowlist != APPROVED_NON_FINANCIAL_EVENT_TYPES:
            errors.append(
                "score_revenue_unreacted non-financial event allowlist drifted: "
                f"expected={sorted(APPROVED_NON_FINANCIAL_EVENT_TYPES)} "
                f"actual={sorted(actual_allowlist or set())}"
            )
        if 'text(row, "event_catalyst_tags").split(";", 1)[0]' not in function_text:
            errors.append("event catalyst scoring must use only the first semicolon-delimited event type")
        if "event_type in approved_non_financial_event_types" not in function_text:
            errors.append("event catalyst scoring must require exact allowlist membership")
        errors.extend(_strict_event_bonus_errors(score_function))

    spec = _model_spec_node(tree)
    if spec is None or len(spec.args) < 8:
        errors.append("missing complete revenue_unreacted_range ModelSpec")
    else:
        add_score = ast.literal_eval(spec.args[5])
        forbidden = ast.literal_eval(spec.args[6])
        guidance = ast.literal_eval(spec.args[7])
        if "核准的非財務事件類型" not in add_score:
            errors.append("ModelSpec add-score text must restrict events to approved non-financial types")
        if any(field in add_score for field in FINANCIAL_FIELDS):
            errors.append("ModelSpec add-score text still advertises financial-statement scoring")
        for field in FINANCIAL_FIELDS:
            if field not in forbidden:
                errors.append(f"ModelSpec fail-closed text omits {field}")
        if "歷史財報PIT未完整前維持fail closed" not in forbidden:
            errors.append("ModelSpec must state the historical-PIT fail-closed boundary")
        if "季／年財報維持獨立" not in guidance:
            errors.append("ModelSpec must keep monthly revenue and quarterly/annual statements separate")

    contract_rows = _read_rows(root / "config/stock_model_contract_registry.csv")
    contract = _single_row(contract_rows, key="model_id", value=MODEL_ID)
    if contract is None:
        errors.append("stock model contract must contain exactly one revenue_unreacted_range row")
    else:
        inputs = {item for item in contract.get("input_columns", "").split(";") if item}
        if contract.get("contract_version") != "v2":
            errors.append("revenue_unreacted_range contract_version must be v2")
        if contract.get("effective_from") != EFFECTIVE_FROM:
            errors.append(f"revenue_unreacted_range v2 effective_from must be {EFFECTIVE_FROM}")
        if "fundamental_catalyst_tags" in inputs:
            errors.append("contract input_columns must exclude fundamental_catalyst_tags")
        if "event_catalyst_tags" not in inputs:
            errors.append("contract input_columns must retain event_catalyst_tags for the strict allowlist")
        reason = contract.get("change_reason", "")
        if "financial_statement_features_fail_closed_until_historical_pit" not in reason:
            errors.append("contract change_reason must pin the financial-statement fail-closed decision")
        if "pre_v2_history_quarantined" not in reason:
            errors.append("contract change_reason must quarantine pre-v2 score history from formal evidence")

    return errors


def _current_parameter_errors(root: Path) -> list[str]:
    errors: list[str] = []
    parameter_rows = _read_rows(root / "output/latest/daily_candidate_model_parameters_latest.csv")
    parameter = _single_row(parameter_rows, key="model_id", value=MODEL_ID)
    if parameter is None:
        errors.append("daily model parameters must contain exactly one revenue_unreacted_range row")
    else:
        add_score = parameter.get("add_score_items", "")
        forbidden = parameter.get("forbidden_veto", "")
        guidance = parameter.get("operation_guidance", "")
        if "核准的非財務事件類型" not in add_score:
            errors.append("parameter artifact does not expose the approved non-financial allowlist boundary")
        if any(field in add_score for field in FINANCIAL_FIELDS):
            errors.append("parameter artifact still exposes financial-statement add-score semantics")
        for field in FINANCIAL_FIELDS:
            if field not in forbidden:
                errors.append(f"parameter artifact fail-closed text omits {field}")
        if "季／年財報維持獨立" not in guidance:
            errors.append("parameter artifact does not separate monthly revenue from statements")

    return errors


def _historical_pit_errors(root: Path) -> tuple[list[str], int]:
    errors: list[str] = []
    audit_rows = _read_rows(
        root / "docs/latest/financial_statement_historical_pit_source_audit_latest.csv"
    )
    if not audit_rows:
        errors.append("historical financial-statement PIT source audit is empty")
    for index, row in enumerate(audit_rows, start=2):
        if row.get("pit_eligible") != "False":
            errors.append(f"historical PIT audit row {index} must remain pit_eligible=False")
        if row.get("formal_model_use_allowed") != "False":
            errors.append(
                f"historical PIT audit row {index} must remain formal_model_use_allowed=False"
            )

    return errors, len(audit_rows)


def _current_signal_errors(root: Path) -> tuple[list[str], int]:
    errors: list[str] = []
    candidate_rows = _read_rows(root / "output/latest/all_candidates_latest.csv")
    candidate_by_source = {
        (_source_index(row.get("source_row_index", "")), row.get("stock_id", "")): row
        for row in candidate_rows
    }
    signal_rows = _read_rows(root / "output/latest/daily_candidate_model_signals_latest.csv")
    revenue_signals = [row for row in signal_rows if row.get("model_id") == MODEL_ID]
    for row in revenue_signals:
        components = row.get("score_components", "")
        for legacy in LEGACY_SCORE_COMPONENTS:
            if legacy in components:
                errors.append(
                    f"current signal {row.get('stock_id', '')} retains legacy component {legacy}"
                )
        source_key = (_source_index(row.get("source_row_index", "")), row.get("stock_id", ""))
        candidate = candidate_by_source.get(source_key)
        if candidate is None:
            errors.append(
                "current revenue signal cannot be traced to all_candidates source_row_index: "
                f"source_row_index={source_key[0]} stock_id={source_key[1]}"
            )
            continue
        event_type = candidate.get("event_catalyst_tags", "").split(";", 1)[0].strip().lower()
        has_bonus = APPROVED_EVENT_COMPONENT in components
        if has_bonus != (event_type in APPROVED_NON_FINANCIAL_EVENT_TYPES):
            errors.append(
                "current revenue signal event bonus does not match the strict first-token allowlist: "
                f"stock_id={source_key[1]} event_type={event_type or 'empty'}"
            )

    return errors, len(revenue_signals)


def _history_classification_errors(root: Path) -> tuple[list[str], int, int]:
    history_rows = _read_rows(
        root / "output/history/daily_candidate_models/daily_candidate_model_signal_log.csv"
    )
    revenue_history = [row for row in history_rows if row.get("model_id") == MODEL_ID]
    pre_v2, post_v2, date_errors = _classify_history_dates(revenue_history)

    return date_errors, pre_v2, post_v2


def validate(
    root: Path = ROOT, *, phase: str = VALIDATION_PHASE_FULL
) -> tuple[list[str], dict[str, int]]:
    if phase not in VALIDATION_PHASES:
        raise ValueError(
            f"unsupported validation phase={phase!r}; expected one of {VALIDATION_PHASES}"
        )

    errors: list[str] = []
    metrics = {
        "current_revenue_signal_rows": 0,
        "pre_v2_legacy_history_rows": 0,
        "post_v2_history_rows": 0,
        "historical_pit_audit_rows": 0,
        "quarantine_control_count": 0,
    }

    if phase == VALIDATION_PHASE_FULL:
        errors.extend(_static_semantic_errors(root))

    errors.extend(_current_parameter_errors(root))

    if phase == VALIDATION_PHASE_FULL:
        pit_errors, pit_rows = _historical_pit_errors(root)
        errors.extend(pit_errors)
        metrics["historical_pit_audit_rows"] = pit_rows

    signal_errors, signal_rows = _current_signal_errors(root)
    errors.extend(signal_errors)
    metrics["current_revenue_signal_rows"] = signal_rows

    if phase == VALIDATION_PHASE_FULL:
        history_errors, pre_v2, post_v2 = _history_classification_errors(root)
        errors.extend(history_errors)
        metrics["pre_v2_legacy_history_rows"] = pre_v2
        metrics["post_v2_history_rows"] = post_v2

        quarantine_errors, quarantine_controls = _legacy_history_quarantine_errors(root)
    else:
        quarantine_errors, quarantine_controls = _current_promotion_block_errors(root)
    errors.extend(quarantine_errors)
    metrics["quarantine_control_count"] = quarantine_controls

    return errors, metrics


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo-root", type=Path, default=ROOT)
    parser.add_argument(
        "--phase",
        choices=VALIDATION_PHASES,
        default=VALIDATION_PHASE_FULL,
        help="full keeps static and historical gates; runtime checks rebuilt current artifacts only",
    )
    args = parser.parse_args(argv)
    errors, metrics = validate(args.repo_root.resolve(), phase=args.phase)
    print(f"validation_phase={args.phase}")
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1
    if args.phase == VALIDATION_PHASE_FULL:
        print(
            "revenue_unreacted_range financial-statement fail-closed validation passed: "
            f"current_rows={metrics['current_revenue_signal_rows']} "
            f"pre_v2_history_quarantined={metrics['pre_v2_legacy_history_rows']} "
            f"post_v2_history_rows={metrics['post_v2_history_rows']} "
            f"historical_pit_audit_rows={metrics['historical_pit_audit_rows']} "
            f"quarantine_controls={metrics['quarantine_control_count']}"
        )
    else:
        print(
            "revenue_unreacted_range financial-statement fail-closed validation passed: "
            f"current_rows={metrics['current_revenue_signal_rows']} "
            f"runtime_promotion_controls={metrics['quarantine_control_count']} "
            "runtime_scope=current_parameters,current_parity,current_readiness,"
            "current_signal_trace,current_score_event "
            "skipped=static_ast,static_config,historical_pit,full_history,"
            "history_consumer_scan"
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
