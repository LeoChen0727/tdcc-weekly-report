from __future__ import annotations

import ast
import csv
import re
from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
INVENTORY_CSV = ROOT / "config" / "repo_production_inventory.csv"
LINEAGE_CSV = ROOT / "config" / "report_artifact_lineage.csv"
DAILY_WORKFLOW = ROOT / ".github" / "workflows" / "daily_full_pipeline.yml"
DAILY_BOUNDARY_VALIDATOR = ROOT / "scripts" / "validate_daily_production_boundaries.py"
TAXONOMY_CSV = ROOT / "output" / "latest" / "stock_theme_taxonomy_latest.csv"
MODEL_PARITY_CSV = ROOT / "output" / "latest" / "daily_model_research_parity_latest.csv"
MODEL_PARAMETERS_CSV = ROOT / "output" / "latest" / "daily_candidate_model_parameters_latest.csv"
OPERATION_SECTION_CSV = ROOT / "output" / "latest" / "daily_volume_breakout_operation_section_latest.csv"

REPORT_SURFACES = {
    "scripts/generate_chatgpt_side_daily_reports.py",
    "build_chatgpt_daily_report_packet.py",
    "build_chatgpt_daily_report_rules.py",
    "publish_chatgpt_report_readme_and_check.py",
}

PRODUCTION_OWNERS = {
    "daily_production",
    "market_risk",
    "warrant",
    "official_price_data",
    "catalyst_event",
}

DATA_SOURCE_OWNERS = PRODUCTION_OWNERS | {"repo_infrastructure"}

ALLOWED_CROSS_OWNER_IMPORTS = {
    # Low-level utilities.
    ("*", "repo_infrastructure", "*"),
    # Research may compare against the production daily model layer, but must not
    # mutate production parameters.
    (
        "scripts/validate_daily_model_research_parity.py",
        "daily_production",
        "scripts/build_daily_candidate_model_layer.py",
    ),
    (
        "scripts/build_daily_model_parameter_research.py",
        "daily_production",
        "scripts/build_daily_candidate_model_layer.py",
    ),
    (
        "scripts/build_historical_pattern_operation_registry.py",
        "daily_production",
        "scripts/build_volume_breakout_watch.py",
    ),
    (
        "scripts/build_volume_breakout_confirmed_operation_backtest.py",
        "daily_production",
        "scripts/build_volume_breakout_watch.py",
    ),
    (
        "scripts/build_tdcc_weekly_ranking_backtest.py",
        "tdcc_weekly",
        "scripts/build_tdcc_weekly_candidate_reports.py",
    ),
    # Individual-stock reports may read stock-level TDCC utilities/data, not TDCC
    # weekly PDF/report builders.
    (
        "scripts/generate_individual_stock_report.py",
        "tdcc_weekly",
        "scripts/tdcc_stock_history_utils.py",
    ),
    # Historical daily revenue model still consumes a TDCC status helper.
    (
        "build_revenue_breakout_low_response.py",
        "tdcc_weekly",
        "tdcc_trend_utils.py",
    ),
    (
        "scripts/validate_daily_candidate_regression_cases.py",
        "daily_production",
        "stock_daily_monitor.py",
    ),
}

FORBIDDEN_SOURCE_PATTERNS = {
    "daily production must not read research recommendation internals": (
        re.compile(r"output/latest/(volume_breakout_confirmed_operation_rank|volume_breakout_operation_pdf_preview|historical_pattern_operation_registry|approved_operation_patterns)_latest"),
        {"daily_production"},
    ),
    "daily production must not read research history outputs": (
        re.compile(r"output/history/(research|volume_breakout|market_timing|surge_model|msci_index_reviews|patterns)/"),
        {"daily_production"},
    ),
    "TDCC weekly must not read daily PDF artifacts": (
        re.compile(r"output/latest/(mainstream|non_mainstream|daily_market_).*\\.pdf"),
        {"tdcc_weekly"},
    ),
    "individual stock must not read full-market daily PDFs": (
        re.compile(r"output/latest/(mainstream|non_mainstream|daily_market_).*\\.pdf"),
        {"individual_stock"},
    ),
}

ALLOWED_PRODUCTION_OUTPUT_LATEST_READS = {
    "scripts/build_daily_volume_breakout_operation_section.py": {
        "output/latest/daily_candidate_model_signals_for_report_latest.csv",
        "output/latest/approved_operation_patterns_latest.csv",
        "output/latest/volume_breakout_formal_operation_backtest_latest.csv",
    },
    "scripts/build_daily_candidate_model_layer.py": {
        "output/latest/daily_model_parameter_recommendations_latest.csv",
    },
}

DATE_FORBIDDEN_CALLS = {
    "datetime.now",
    "datetime.today",
    "date.today",
}

REPORT_DATE_SENSITIVE_PATHS = {
    "scripts/generate_chatgpt_side_daily_reports.py",
    "scripts/run_chatgpt_daily_report_entrypoint.py",
    "scripts/build_theme_event_watch.py",
    "build_daily_market_report_artifacts.py",
    "build_chatgpt_daily_report_packet.py",
    "build_chatgpt_daily_report_rules.py",
    "publish_chatgpt_report_readme_and_check.py",
}

DATE_ALLOWED_PATHS = {
    # Timestamps for generated_at/logging are allowed; report-date selection is
    # separately enforced by freshness gates and source resolver checks.
    "scripts/tracking_utils.py",
    "build_data_freshness_latest.py",
    "publish_chatgpt_report_readme_and_check.py",
    "ensure_daily_report_readme.py",
    "ensure_report_aliases.py",
    "scripts/resolve_daily_report_source_state.py",
    "scripts/run_chatgpt_daily_report_entrypoint.py",
}

FORBIDDEN_REPORT_TEXT = {
    "trade_decision",
    "action_rating",
    "decision_priority",
    "entry_style",
    "position_sizing",
    "compute_action_decision",
}

FORBIDDEN_PDF_RAW_TOKENS = {
    "buy_rank_eligible",
    "row_action_status",
    "confirmed_buy_candidate",
}

EXPECTED_PARITY_STATUSES = {
    "production_parity",
    "production_proxy",
    "proxy_only",
}

EXPECTED_LINEAGE_COLUMNS = {
    "artifact_path",
    "artifact_kind",
    "owner",
    "producer",
    "source_artifacts",
    "validator",
    "publisher",
    "public_surface",
}


@dataclass(frozen=True)
class InventoryRow:
    path: str
    kind: str
    owner: str
    status: str
    purpose: str


def rel(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8-sig", errors="replace")


def load_inventory() -> dict[str, InventoryRow]:
    with INVENTORY_CSV.open("r", encoding="utf-8-sig", newline="") as fh:
        rows = {}
        for row in csv.DictReader(fh):
            rows[row["path"]] = InventoryRow(
                path=row["path"],
                kind=row["kind"],
                owner=row["owner"],
                status=row["status"],
                purpose=row["purpose"],
            )
        return rows


def load_csv_rows(path: Path) -> list[dict[str, str]]:
    if not path.exists():
        return []
    with path.open("r", encoding="utf-8-sig", newline="") as fh:
        return [{key: str(value or "") for key, value in row.items()} for row in csv.DictReader(fh)]


def module_map(inventory: dict[str, InventoryRow]) -> dict[str, str]:
    mapping: dict[str, str] = {}
    for path, row in inventory.items():
        if row.kind not in {"python", "test_python"}:
            continue
        if path.endswith("/__init__.py"):
            continue
        stem = Path(path).stem
        if path.startswith("scripts/"):
            mapping[stem] = path
            mapping[f"scripts.{stem}"] = path
        elif path.startswith("tests/"):
            mapping[f"tests.{stem}"] = path
        elif "/" not in path:
            mapping[stem] = path
    return mapping


def import_edges(inventory: dict[str, InventoryRow]) -> tuple[list[tuple[str, str, str]], list[str]]:
    mapping = module_map(inventory)
    edges: list[tuple[str, str, str]] = []
    errors: list[str] = []
    for path, row in inventory.items():
        if row.kind not in {"python", "test_python"}:
            continue
        source = ROOT / path
        try:
            tree = ast.parse(read_text(source), filename=path)
        except SyntaxError as exc:
            errors.append(f"cannot parse Python for import graph: {path}: {exc}")
            continue
        for node in ast.walk(tree):
            names: list[str] = []
            if isinstance(node, ast.Import):
                names = [alias.name for alias in node.names]
            elif isinstance(node, ast.ImportFrom) and node.module and node.level == 0:
                names = [node.module]
            for name in names:
                candidates = [name]
                parts = name.split(".")
                if parts:
                    candidates.append(parts[0])
                for candidate in candidates:
                    target = mapping.get(candidate)
                    if target and target != path:
                        edges.append((path, target, name))
                        break
    return edges, errors


def allowed_import(source: InventoryRow, target: InventoryRow) -> bool:
    if source.kind == "test_python":
        return True
    if source.owner == target.owner:
        return True
    for allowed_source, allowed_owner, allowed_target in ALLOWED_CROSS_OWNER_IMPORTS:
        source_match = allowed_source == "*" or allowed_source == source.path
        owner_match = allowed_owner == "*" or allowed_owner == target.owner
        target_match = allowed_target == "*" or allowed_target == target.path
        if source_match and owner_match and target_match:
            return True
    return False


def validate_import_graph(inventory: dict[str, InventoryRow]) -> list[str]:
    errors: list[str] = []
    edges, parse_errors = import_edges(inventory)
    errors.extend(parse_errors)
    for source_path, target_path, module_name in edges:
        source = inventory[source_path]
        target = inventory[target_path]
        if not allowed_import(source, target):
            errors.append(
                "forbidden cross-owner import: "
                f"{source_path}({source.owner}) -> {target_path}({target.owner}) via {module_name}"
            )
    return errors


def string_literals(path: Path) -> list[str]:
    try:
        tree = ast.parse(read_text(path), filename=rel(path))
    except SyntaxError:
        return []
    values: list[str] = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Constant) and isinstance(node.value, str):
            values.append(node.value.replace("\\", "/"))
    return values


def validate_data_sources(inventory: dict[str, InventoryRow]) -> list[str]:
    errors: list[str] = []
    for path, row in inventory.items():
        if row.kind != "python" or row.owner not in DATA_SOURCE_OWNERS:
            continue
        values = string_literals(ROOT / path)
        for value in values:
            normalized = value.replace("\\", "/")
            for message, (pattern, owners) in FORBIDDEN_SOURCE_PATTERNS.items():
                if row.owner in owners and pattern.search(normalized):
                    errors.append(f"{message}: {path} contains {normalized!r}")
            if row.owner == "daily_production" and "output/latest/" in normalized:
                allow = ALLOWED_PRODUCTION_OUTPUT_LATEST_READS.get(path, set())
                if normalized in allow:
                    continue
                if any(
                    token in normalized
                    for token in (
                        "historical_pattern_operation",
                        "approved_operation_patterns",
                        "volume_breakout_confirmed_operation",
                        "volume_breakout_operation_pdf_preview",
                    )
                ):
                    errors.append(f"daily production reads non-adapter research artifact without allowlist: {path} -> {normalized}")
    return errors


def call_name(node: ast.AST) -> str:
    if isinstance(node, ast.Name):
        return node.id
    if isinstance(node, ast.Attribute):
        parent = call_name(node.value)
        return f"{parent}.{node.attr}" if parent else node.attr
    return ""


def validate_date_sources(inventory: dict[str, InventoryRow]) -> list[str]:
    errors: list[str] = []
    for path, row in inventory.items():
        if row.kind != "python" or row.owner not in PRODUCTION_OWNERS:
            continue
        if path not in REPORT_DATE_SENSITIVE_PATHS:
            continue
        if path in DATE_ALLOWED_PATHS:
            continue
        try:
            tree = ast.parse(read_text(ROOT / path), filename=path)
        except SyntaxError:
            continue
        lines = read_text(ROOT / path).splitlines()
        for node in ast.walk(tree):
            if not isinstance(node, ast.Call):
                continue
            name = call_name(node.func)
            if name in DATE_FORBIDDEN_CALLS:
                line = lines[node.lineno - 1] if getattr(node, "lineno", 0) and node.lineno <= len(lines) else ""
                if "%Y%m%d" in line:
                    errors.append(
                        "production report code must not derive YYYYMMDD report dates from wall clock "
                        f"without explicit allowlist: {path} uses {name}()"
                    )
    return errors


def validate_lineage(inventory: dict[str, InventoryRow]) -> list[str]:
    errors: list[str] = []
    if not LINEAGE_CSV.exists():
        return ["missing report artifact lineage manifest: config/report_artifact_lineage.csv"]
    rows = load_csv_rows(LINEAGE_CSV)
    if not rows:
        return ["report artifact lineage manifest is empty"]
    missing_cols = EXPECTED_LINEAGE_COLUMNS - set(rows[0])
    if missing_cols:
        return [f"report artifact lineage manifest missing columns: {sorted(missing_cols)}"]
    seen: set[str] = set()
    for row in rows:
        artifact = row["artifact_path"]
        if artifact in seen:
            errors.append(f"duplicate lineage artifact path: {artifact}")
        seen.add(artifact)
        for field in ("owner", "producer", "source_artifacts", "validator", "publisher"):
            if not row[field].strip():
                errors.append(f"lineage row {artifact} missing {field}")
        for field in ("producer", "validator", "publisher"):
            for entry in [part.strip() for part in row[field].split(";") if part.strip()]:
                if entry.endswith(".py") or entry.endswith(".yml") or entry.endswith(".yaml"):
                    if not (ROOT / entry).exists():
                        errors.append(f"lineage row {artifact} references missing {field}: {entry}")
                    if entry.endswith(".py") and entry not in inventory and not entry.startswith("tests/"):
                        errors.append(f"lineage row {artifact} references non-inventoried producer/validator: {entry}")
        for entry in [part.strip() for part in row["source_artifacts"].split(";") if part.strip()]:
            if entry.endswith(".py") or entry.endswith(".md") or entry.endswith(".csv") or entry.endswith(".txt"):
                if not (ROOT / entry).exists():
                    errors.append(f"lineage row {artifact} references missing source_artifact: {entry}")
    required_artifacts = {
        "output/latest/chatgpt_daily_report_packet_latest.txt",
        "output/latest/READ_ME_FIRST_DAILY_REPORT.txt",
        "output/latest/daily_volume_breakout_operation_section_latest.csv",
        "output/latest/daily_candidate_model_signals_for_report_latest.csv",
        "output/latest/stock_theme_taxonomy_latest.csv",
    }
    missing = sorted(required_artifacts - seen)
    if missing:
        errors.append(f"lineage manifest missing required production artifacts: {missing}")
    return errors


def validate_model_parity() -> list[str]:
    errors: list[str] = []
    rows = load_csv_rows(MODEL_PARITY_CSV)
    parameters = load_csv_rows(MODEL_PARAMETERS_CSV)
    if not rows:
        return [f"missing or empty model parity CSV: {rel(MODEL_PARITY_CSV)}"]
    if not parameters:
        return [f"missing or empty daily model parameter CSV: {rel(MODEL_PARAMETERS_CSV)}"]

    parity_by_model = {row.get("model_id", "").strip(): row for row in rows if row.get("model_id", "").strip()}
    production_models = {
        row.get("model_id", "").strip()
        for row in parameters
        if row.get("model_id", "").strip()
        and row.get("pdf_visibility", "").strip() in {"pdf_core_model", "pdf_watch_model", "pdf_support_model"}
    }
    missing = sorted(production_models - set(parity_by_model))
    if missing:
        errors.append(f"daily production models missing research parity rows: {missing}")

    statuses = {row.get("research_baseline_status", "") for row in rows}
    unsupported = sorted(statuses - EXPECTED_PARITY_STATUSES)
    if unsupported:
        errors.append(f"model parity output has unsupported statuses: {unsupported}")
    for row in rows:
        status = row.get("research_baseline_status", "")
        if status in {"production_proxy", "proxy_only"} and not row.get("parity_blocker", "").strip():
            errors.append(f"model parity proxy row missing blocker: {row.get('model_id', '')}")
    return errors


def validate_orphan_code(inventory: dict[str, InventoryRow]) -> list[str]:
    errors: list[str] = []
    edges, _ = import_edges(inventory)
    inbound = {target for _, target, _ in edges}
    workflow_text = "\n".join(read_text(ROOT / path) for path, row in inventory.items() if row.kind == "workflow")
    guidance_text = ""
    for path in ("AGENTS.md", "README.md", "docs/repo_production_inventory.md", "docs/CODEX_THREAD_WORKFLOW.md"):
        candidate = ROOT / path
        if candidate.exists():
            guidance_text += "\n" + read_text(candidate)

    for path, row in inventory.items():
        if row.kind != "python" or row.status == "legacy_deprecated":
            continue
        if row.owner in {"repo_infrastructure", "diagnostics"}:
            continue
        if path in inbound or path in workflow_text or path in guidance_text:
            continue
        if Path(path).name.startswith("validate_"):
            continue
        errors.append(
            f"active script has no workflow/import/guidance reference; mark deprecated/manual or wire it explicitly: {path}"
        )
    return errors


def validate_taxonomy_semantics() -> list[str]:
    errors: list[str] = []
    rows = load_csv_rows(TAXONOMY_CSV)
    if not rows:
        return errors + [f"missing or empty taxonomy CSV: {rel(TAXONOMY_CSV)}"]
    required = {"stock_id", "mainstream_report_eligible", "non_mainstream_report_eligible", "basic_theme", "industry"}
    missing = required - set(rows[0])
    if missing:
        return errors + [f"taxonomy CSV missing columns: {sorted(missing)}"]
    for row in rows:
        stock_id = row.get("stock_id", "")
        mainstream = row.get("mainstream_report_eligible", "")
        non_mainstream = row.get("non_mainstream_report_eligible", "")
        basic_theme = row.get("basic_theme", "").strip()
        industry = row.get("industry", "").strip()
        if mainstream not in {"True", "False"} or non_mainstream not in {"True", "False"}:
            errors.append(f"stock has invalid mainstream/non-mainstream flags: {stock_id}")
        if mainstream != "True" and non_mainstream != "True":
            errors.append(f"stock has no mainstream/non-mainstream report membership: {stock_id}")
        if not basic_theme and not industry:
            errors.append(f"stock has no basic theme or industry classification: {stock_id}")
    return errors


def validate_operation_semantics() -> list[str]:
    errors: list[str] = []
    rows = load_csv_rows(OPERATION_SECTION_CSV)
    if not rows:
        return [f"missing or empty operation section CSV: {rel(OPERATION_SECTION_CSV)}"]
    required = {"pdf_section", "row_type", "row_action_status", "buy_rank_eligible", "stock_id"}
    missing = required - set(rows[0])
    if missing:
        return [f"operation section CSV missing columns: {sorted(missing)}"]
    sections = {row.get("pdf_section", "") for row in rows}
    for required_section in {
        "confirmed_operation",
        "confirmed_unranked_operation",
        "pending_confirmation",
        "active_operation",
    }:
        if required_section not in sections:
            errors.append(f"operation section CSV missing section: {required_section}")
    for row in rows:
        if row.get("pdf_view", "") == "highlight" and row.get("pdf_section", "") in {
            "confirmed_unranked_operation",
            "pending_confirmation",
        }:
            errors.append(
                "highlight operation section must not include pending or unranked rows: "
                f"{row.get('stock_id', '')}"
            )
        section = row.get("pdf_section", "")
        status = row.get("row_action_status", "")
        eligible = row.get("buy_rank_eligible", "")
        if section == "confirmed_operation" and row.get("row_type") == "data":
            if status != "confirmed_buy_candidate" or eligible != "True":
                errors.append(f"confirmed operation row is not buy-rank eligible: {row.get('stock_id', '')}")
        if section == "confirmed_unranked_operation" and row.get("row_type") == "data":
            if status != "confirmed_not_buy_ranked" or eligible != "False":
                errors.append(
                    "confirmed unranked operation row is mixed with buy-rank semantics: "
                    f"{row.get('stock_id', '')}"
                )
        if section == "pending_confirmation" and row.get("row_type") == "data":
            if status != "pending_confirmation" or eligible != "False":
                errors.append(f"pending operation row is mixed with buy-rank semantics: {row.get('stock_id', '')}")
        if section == "active_operation" and row.get("row_type") == "data":
            if eligible != "False":
                errors.append(f"active operation row must not be buy-rank eligible: {row.get('stock_id', '')}")
    return errors


def validate_report_semantics() -> list[str]:
    errors: list[str] = []
    for path in REPORT_SURFACES:
        text = read_text(ROOT / path)
        for token in FORBIDDEN_REPORT_TEXT:
            if token in text:
                errors.append(f"daily report surface contains forbidden decision-layer token: {path}: {token}")
    rendered_text_surfaces = [
        ROOT / "output" / "latest" / "READ_ME_FIRST_DAILY_REPORT.txt",
        ROOT / "output" / "latest" / "chatgpt_daily_report_packet_latest.txt",
        ROOT / "output" / "latest" / "CHATGPT_DAILY_REPORT_RULES.txt",
        ROOT / "docs" / "latest" / "READ_ME_FIRST_DAILY_REPORT.txt",
        ROOT / "docs" / "latest" / "chatgpt_daily_report_packet_latest.txt",
        ROOT / "docs" / "latest" / "CHATGPT_DAILY_REPORT_RULES.txt",
    ]
    for surface in rendered_text_surfaces:
        if not surface.exists():
            continue
        text = read_text(surface)
        for token in FORBIDDEN_PDF_RAW_TOKENS:
            if token in text:
                errors.append(f"public report text surface leaks raw operation slug: {rel(surface)}: {token}")
    return errors


def validate_model_parameter_independence() -> list[str]:
    errors: list[str] = []
    table = load_csv_rows(MODEL_PARAMETERS_CSV)
    if not table:
        return [f"missing or empty daily model parameter CSV: {rel(MODEL_PARAMETERS_CSV)}"]
    required_cols = {"model_id", "score_profile_id", "score_profile_scope"}
    if not required_cols.issubset(set(table[0])):
        return [f"daily model parameter table missing columns: {sorted(required_cols - set(table[0]))}"]

    seen_pairs: set[tuple[str, str]] = set()
    profile_models: dict[str, set[str]] = {}
    shared_allowed: set[str] = set()
    for row in table:
        model_id = row.get("model_id", "").strip()
        profile_id = row.get("score_profile_id", "").strip()
        scope = row.get("score_profile_scope", "").strip()
        pair = (model_id, profile_id)
        if pair in seen_pairs:
            errors.append(f"daily model parameter table has duplicated model/profile pair: {model_id}/{profile_id}")
        seen_pairs.add(pair)
        profile_models.setdefault(profile_id, set()).add(model_id)
        if scope == "shared_allowed":
            shared_allowed.add(profile_id)
    shared = sorted(
        profile_id
        for profile_id, model_ids in profile_models.items()
        if len(model_ids) > 1 and profile_id not in shared_allowed and profile_id not in {"default", "", "nan"}
    )
    if shared:
        errors.append(f"score_profile_id shared across multiple models without allowlist: {shared}")
    return errors


def validate_workflow_hooks() -> list[str]:
    errors: list[str] = []
    workflow = read_text(DAILY_WORKFLOW)
    command = "python scripts/validate_repo_semantic_integrity.py"
    if command not in workflow:
        errors.append(f"daily_full_pipeline.yml must run {command}")
    boundary = read_text(DAILY_BOUNDARY_VALIDATOR)
    if "validate_repo_semantic_integrity.py" not in boundary:
        errors.append("daily production boundary validator must invoke repo semantic integrity validation")
    return errors


def validate() -> list[str]:
    inventory = load_inventory()
    errors: list[str] = []
    errors.extend(validate_import_graph(inventory))
    errors.extend(validate_data_sources(inventory))
    errors.extend(validate_date_sources(inventory))
    errors.extend(validate_lineage(inventory))
    errors.extend(validate_model_parity())
    errors.extend(validate_orphan_code(inventory))
    errors.extend(validate_taxonomy_semantics())
    errors.extend(validate_operation_semantics())
    errors.extend(validate_report_semantics())
    errors.extend(validate_model_parameter_independence())
    errors.extend(validate_workflow_hooks())
    return errors


def main() -> int:
    errors = validate()
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1
    print("repo semantic integrity validation passed")
    print(f"validated_inventory={rel(INVENTORY_CSV)}")
    print(f"validated_lineage={rel(LINEAGE_CSV)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
