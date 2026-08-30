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
CONTRACT_EFFECTIVE_FROM = "2026-08-31"
LEGACY_SIGNAL_LOG = (
    "output/history/daily_candidate_models/daily_candidate_model_signal_log.csv"
)
LEGACY_ARCHIVE_MANIFEST = (
    "config/revenue_unreacted_range_legacy_runtime_evidence_manifest.csv"
)
LEGACY_ARCHIVE_PRODUCER = (
    "scripts/archive_revenue_unreacted_range_legacy_runtime_evidence.py"
)
LEGACY_ARCHIVE_VALIDATOR = (
    "scripts/validate_revenue_unreacted_range_legacy_runtime_evidence.py"
)
LEGACY_ARCHIVE_ID = (
    "legacy_revenue_unreacted_range_v1_signal_evidence_retirement_20260831"
)
LEGACY_ARCHIVE_ARTIFACT = (
    "output/history/daily_candidate_models/"
    "legacy_revenue_v1_signals_through_20260828_fad13a30ab334580.csv"
)
LEGACY_ARCHIVE_CANONICAL_SHA256 = (
    "fad13a30ab3345807c0c096c9bf928754b2105301f1c708af105187e0778474d"
)
LEGACY_ARCHIVE_FORBIDDEN_USES = {
    "daily_selection",
    "pdf",
    "ranking",
    "promotion_evidence",
    "formal_adapter",
    "production_reactivation",
}
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


def _legacy_archive_quarantine_errors(
    root: Path,
    revenue_lineage_consumers: list[dict[str, str]],
    revenue_consumer_scripts: list[Path],
) -> list[str]:
    """Allow the old signal log only as one immutable, non-runtime archive."""

    errors: list[str] = []
    allowed_lineage = [
        row
        for row in revenue_lineage_consumers
        if row.get("artifact_path") == LEGACY_ARCHIVE_MANIFEST
        and row.get("artifact_kind") == "legacy_runtime_evidence_manifest"
        and row.get("owner") == "model_governance"
        and row.get("producer") == LEGACY_ARCHIVE_PRODUCER
        and row.get("source_artifacts") == LEGACY_SIGNAL_LOG
        and row.get("validator") == LEGACY_ARCHIVE_VALIDATOR
        and row.get("public_surface") == "config"
    ]
    if len(revenue_lineage_consumers) != 1 or len(allowed_lineage) != 1:
        errors.append(
            "revenue signal-log lineage must be limited to the immutable legacy archive"
        )

    script_names = sorted(path.name for path in revenue_consumer_scripts)
    allowed_script_name = Path(LEGACY_ARCHIVE_PRODUCER).name
    if script_names != [allowed_script_name]:
        errors.append(
            "only the immutable legacy archive producer may read the old signal log: "
            + ",".join(script_names)
        )

    archive_rows = _read_rows(root / LEGACY_ARCHIVE_MANIFEST)
    archive = _single_row(
        archive_rows,
        key="archive_id",
        value=LEGACY_ARCHIVE_ID,
    )
    if archive is None:
        errors.append("legacy revenue runtime evidence archive manifest is missing")
        return errors

    archive_path = archive.get("archive_artifact", "")
    forbidden_uses = set(archive.get("forbidden_use", "").split(";"))
    if (
        archive.get("model_id") != MODEL_ID
        or archive.get("source_artifact") != LEGACY_SIGNAL_LOG
        or archive.get("source_git_commit")
        != "21fe1726757a7b60b58eb618d9500fa61c0a4c55"
        or archive.get("source_total_rows") != "15182"
        or archive.get("archived_row_count") != "4414"
        or archive.get("first_signal_date") != "20260529"
        or archive.get("last_signal_date") != "20260828"
        or archive_path != LEGACY_ARCHIVE_ARTIFACT
        or archive.get("archive_artifact_sha256")
        != LEGACY_ARCHIVE_CANONICAL_SHA256
        or archive.get("row_encoding")
        != (
            "utf-8-sig_rfc4180_canonical_lf_source_column_order_"
            "raw_newline_diagnostic_only"
        )
        or archive.get("owner_lane") != "daily_model_maintenance"
        or forbidden_uses != LEGACY_ARCHIVE_FORBIDDEN_USES
        or archive.get("authorization_ref") != "user_authorized_4A_4C_20260830"
        or not (root / archive_path).is_file()
    ):
        errors.append(
            "legacy revenue archive must stay content-addressed and forbidden from runtime reuse"
        )
    return errors


def _legacy_history_quarantine_errors(root: Path) -> tuple[list[str], int]:
    errors: list[str] = []
    controls = 0

    condition_rows = _read_rows(root / "config/daily_model_condition_spec.csv")
    condition = _single_row(condition_rows, key="model_id", value=MODEL_ID)
    if condition is None:
        errors.append("daily_model_condition_spec must contain exactly one revenue row")
    elif (
        condition.get("research_baseline_status") != "proxy_only"
        or condition.get("operation_contract")
        != "revenue_unreacted_range_source_mid_falling_v2_operation_v2"
    ):
        errors.append(
            "revenue condition spec must remain proxy_only while pinning only the frozen v2 "
            "promotion-candidate operation contract"
        )
    else:
        controls += 1

    evidence_rows = _read_rows(root / "config/formal_model_evidence_pins.csv")
    evidence = _single_row(evidence_rows, key="model_id", value=MODEL_ID)
    expected_evidence_path = (
        "config/approved_operation_evidence/"
        "revenue_unreacted_range_source_mid_falling_frozen_rule_launch_evidence_"
        "v1_20260830_manifest.csv"
    )
    if evidence is None:
        errors.append("revenue promotion candidate must have exactly one frozen evidence pin")
    elif (
        evidence.get("approval_version")
        != "revenue_unreacted_range_source_mid_falling_formal_operation_v2_20260830"
        or evidence.get("evidence_path") != expected_evidence_path
        or evidence.get("evidence_version")
        != "revenue_unreacted_range_source_mid_falling_frozen_rule_launch_evidence_v1_20260830"
        or evidence.get("pin_status") != "pinned_formal_evidence"
        or not re.fullmatch(r"[0-9a-f]{64}", evidence.get("canonical_sha256", ""))
        or not (root / expected_evidence_path).is_file()
    ):
        errors.append(
            "revenue promotion-candidate evidence pin must resolve to the frozen v2 launch manifest"
        )
    else:
        controls += 1

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
    surface_rows = _read_rows(root / "config/model_surface_registry.csv")
    surface = _single_row(surface_rows, key="surface_id", value=MODEL_ID)
    if readiness is None:
        errors.append("model operation readiness must contain exactly one revenue row")
    elif (
        readiness.get("formal_model_use_allowed") != "False"
        or readiness.get("approved_for_daily") != "False"
        or readiness.get("presentation_allowed") != "False"
        or readiness.get("production_allowed") != "False"
        or readiness.get("operation_directive_level") != "no_operation_directive"
    ):
        errors.append(
            "revenue promotion candidate must remain non-formal non-production and non-presentable"
        )
    elif surface is None:
        errors.append("model surface registry must contain exactly one revenue row")
    elif (
        surface.get("approved_for_daily_pdf") != "false"
        or surface.get("approved_for_tdcc_weekly_pdf") != "false"
        or surface.get("approved_for_individual_pdf") != "false"
        or surface.get("stock_entry_signal") != "true"
        or surface.get("research_parity_status") != "warning_research_variant_only"
        or surface.get("promotion_required") != "true"
    ):
        errors.append(
            "revenue surface must expose the stock-model identity while all PDF permissions remain false"
        )
    else:
        controls += 1

    signal_log = LEGACY_SIGNAL_LOG
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
    revenue_consumer_scripts = [
        path
        for path in (root / "scripts").glob("*revenue_unreacted_range*.py")
        if path.name != Path(__file__).name
        and "daily_candidate_model_signal_log.csv" in path.read_text(encoding="utf-8")
    ]
    archive_errors = _legacy_archive_quarantine_errors(
        root,
        revenue_lineage_consumers,
        revenue_consumer_scripts,
    )
    errors.extend(archive_errors)
    if not signal_log_background_uses:
        errors.append("expected coverage-only signal-log lineage is missing")
    if not any(
        row.get("data_family_id") == "monthly_revenue_coverage_backfill_audit"
        for row in signal_log_background_uses
    ):
        errors.append("signal-log use must remain pinned to the monthly revenue coverage audit")
    if not archive_errors:
        controls += 1

    return errors, controls


def validate(root: Path = ROOT) -> tuple[list[str], dict[str, int]]:
    errors: list[str] = []
    metrics = {
        "current_revenue_signal_rows": 0,
        "pre_v2_legacy_history_rows": 0,
        "post_v2_history_rows": 0,
        "historical_pit_audit_rows": 0,
        "quarantine_control_count": 0,
    }

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
        if contract.get("contract_version") != "v3":
            errors.append("revenue_unreacted_range promotion-candidate contract_version must be v3")
        if contract.get("effective_from") != CONTRACT_EFFECTIVE_FROM:
            errors.append(
                "revenue_unreacted_range v3 effective_from must be "
                f"{CONTRACT_EFFECTIVE_FROM}"
            )
        if contract.get("production_source_file") != (
            "scripts/build_daily_revenue_unreacted_range_operation_section.py"
        ):
            errors.append("v3 contract must use the model-owned revenue operation producer")
        if contract.get("condition_function") != "_selected_source_mid_falling":
            errors.append("v3 contract must pin the frozen source_mid_falling selector")
        if contract.get("score_function") != "build_operation_section":
            errors.append("v3 contract must use the dedicated operation-section entrypoint")
        if contract.get("score_profile_id") != (
            "revenue_unreacted_range_source_mid_falling_v2_frozen_no_score"
        ):
            errors.append("v3 contract must have no legacy score profile")
        if not {
            "latest_revenue_yoy_pct",
            "cumulative_revenue_yoy_pct",
            "source_table_date",
            "point_in_time_status",
            "date",
            "open",
            "high",
            "low",
            "close",
        }.issubset(inputs):
            errors.append("v3 contract is missing frozen monthly-revenue or OHLC inputs")
        if "fundamental_catalyst_tags" in inputs or "event_catalyst_tags" in inputs:
            errors.append("v3 contract inputs must exclude all legacy catalyst-tag scoring")
        if any(
            pattern.search(column.lower())
            for column in inputs
            for pattern in FINANCIAL_SOURCE_PATTERNS
        ):
            errors.append("v3 contract input_columns include financial-statement fields")
        if any(contract.get(column) != "false" for column in (
            "approved_for_daily_pdf",
            "approved_for_tdcc_weekly_pdf",
            "approved_for_individual_pdf",
        )):
            errors.append("promotion-candidate v3 contract must keep every PDF permission false")
        reason = contract.get("change_reason", "")
        if "source_mid_falling_v2_contract_prepared_permissions_false" not in reason:
            errors.append("contract change_reason must mark the permissions-false preparation stage")
        if "legacy_generic_selector_retired" not in reason:
            errors.append("contract change_reason must retire the legacy generic selector")

    parameter_rows = _read_rows(root / "output/latest/daily_candidate_model_parameters_latest.csv")
    parameter = _single_row(parameter_rows, key="model_id", value=MODEL_ID)
    if parameter is None:
        errors.append("daily model parameters must contain exactly one revenue_unreacted_range row")
    else:
        main_conditions = parameter.get("main_conditions", "")
        add_score = parameter.get("add_score_items", "")
        forbidden = parameter.get("forbidden_veto", "")
        guidance = parameter.get("operation_guidance", "")
        if "source_mid_falling v2" not in main_conditions:
            errors.append("parameter artifact must expose the frozen v2 selector")
        if "不設 add-score、deduct-score" not in add_score:
            errors.append("parameter artifact must forbid legacy scoring and reranking")
        for field in FINANCIAL_FIELDS:
            if field not in forbidden:
                errors.append(f"parameter artifact fail-closed text omits {field}")
        if parameter.get("score_profile_id") != (
            "revenue_unreacted_range_source_mid_falling_v2_frozen_no_score"
        ):
            errors.append("parameter artifact must expose the frozen no-score profile")
        if parameter.get("parameter_status") != "contract_prepared_permissions_false":
            errors.append("parameter artifact must remain in the permissions-false preparation stage")
        numeric_score_columns = (
            "base_score",
            "volume_ratio_bonus_per_1x",
            "volume_ratio_bonus_cap",
            "tdcc_positive_bonus",
            "warrant_bullish_bonus",
            "strong_revenue_bonus",
            "lower_position_bonus",
            "lower_position_max_off_60d_low_pct",
            "high_return_penalty_threshold_20d",
            "high_return_penalty",
            "tdcc_distribution_penalty",
            "false_breakout_penalty",
        )
        if any(parameter.get(column, "") for column in numeric_score_columns):
            errors.append("parameter artifact must not retain any legacy numeric score value")
        if "forward_holdout_v2 僅作上線後監測" not in guidance:
            errors.append("parameter artifact must expose the non-hard forward-holdout boundary")

    audit_rows = _read_rows(
        root / "docs/latest/financial_statement_historical_pit_source_audit_latest.csv"
    )
    metrics["historical_pit_audit_rows"] = len(audit_rows)
    if not audit_rows:
        errors.append("historical financial-statement PIT source audit is empty")
    for index, row in enumerate(audit_rows, start=2):
        if row.get("pit_eligible") != "False":
            errors.append(f"historical PIT audit row {index} must remain pit_eligible=False")
        if row.get("formal_model_use_allowed") != "False":
            errors.append(
                f"historical PIT audit row {index} must remain formal_model_use_allowed=False"
            )

    candidate_rows = _read_rows(root / "output/latest/all_candidates_latest.csv")
    candidate_by_source = {
        (_source_index(row.get("source_row_index", "")), row.get("stock_id", "")): row
        for row in candidate_rows
    }
    signal_rows = _read_rows(root / "output/latest/daily_candidate_model_signals_latest.csv")
    revenue_signals = [row for row in signal_rows if row.get("model_id") == MODEL_ID]
    metrics["current_revenue_signal_rows"] = len(revenue_signals)
    if revenue_signals:
        errors.append(
            "legacy revenue_unreacted_range must not emit current generic daily signal rows"
        )
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

    history_rows = _read_rows(
        root / "output/history/daily_candidate_models/daily_candidate_model_signal_log.csv"
    )
    revenue_history = [row for row in history_rows if row.get("model_id") == MODEL_ID]
    pre_v2, post_v2, date_errors = _classify_history_dates(revenue_history)
    metrics["pre_v2_legacy_history_rows"] = pre_v2
    metrics["post_v2_history_rows"] = post_v2
    errors.extend(date_errors)

    quarantine_errors, quarantine_controls = _legacy_history_quarantine_errors(root)
    errors.extend(quarantine_errors)
    metrics["quarantine_control_count"] = quarantine_controls

    return errors, metrics


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo-root", type=Path, default=ROOT)
    args = parser.parse_args()
    errors, metrics = validate(args.repo_root.resolve())
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1
    print(
        "revenue_unreacted_range financial-statement fail-closed validation passed: "
        f"current_rows={metrics['current_revenue_signal_rows']} "
        f"pre_v2_history_quarantined={metrics['pre_v2_legacy_history_rows']} "
        f"post_v2_history_rows={metrics['post_v2_history_rows']} "
        f"historical_pit_audit_rows={metrics['historical_pit_audit_rows']} "
        f"quarantine_controls={metrics['quarantine_control_count']}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
