from __future__ import annotations

import argparse
import ast
import copy
import csv
import fnmatch
import hashlib
import io
import re
import subprocess
import sys
from pathlib import Path

import yaml

SCRIPT_DIR = Path(__file__).resolve().parent
if str(SCRIPT_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPT_DIR))

try:
    from . import validate_repo_advanced_integrity as strict_validator  # type: ignore
except ImportError:
    import validate_repo_advanced_integrity as strict_validator  # noqa: E402


ROOT = Path(__file__).resolve().parents[1]
FRESHNESS_RELATIVE_PATH = "output/latest/data_freshness_latest.csv"
EXTERNAL_SOURCE_CONTRACT_PATH = "config/external_data_source_contract.csv"
PRODUCTION_INVENTORY_PATH = "config/repo_production_inventory.csv"
LIFECYCLE_INVENTORY_PATH = "config/repo_file_lifecycle_inventory.csv"
BACKGROUND_DATA_REGISTRY_PATH = "config/daily_model_background_data_registry.csv"
LIFECYCLE_SEMANTIC_MIGRATIONS_PATH = (
    "config/repo_file_lifecycle_semantic_migrations.csv"
)
LIFECYCLE_SEMANTIC_MIGRATION_COLUMNS = (
    "migration_id",
    "status",
    "approval_reference",
    "row_path",
    "column",
    "base_value_sha256",
    "current_value_sha256",
    "added_values",
    "removed_values",
    "scope",
)
LIFECYCLE_SEMANTIC_MIGRATION_STATUS = "preauthorized"
LIFECYCLE_SEMANTIC_MIGRATION_SCOPE = "pr462_research_lifecycle_only"
CANONICAL_LINEAGE_REGISTRY_PATH = (
    "config/daily_model_canonical_field_lineage_registry.csv"
)
CANONICAL_LINEAGE_MIGRATIONS_PATH = (
    "config/daily_model_canonical_field_lineage_migrations.csv"
)
CANONICAL_LINEAGE_VALIDATOR_PATH = (
    "scripts/validate_daily_canonical_field_lineage.py"
)
PR_SAFE_HELPER_PATH = "scripts/validate_repo_advanced_integrity_pr_safe.py"
STRICT_VALIDATOR_PATH = "scripts/validate_repo_advanced_integrity.py"
PR_VALIDATION_WORKFLOW_PATH = (
    ".github/workflows/daily_model_maintenance_pr_validation.yml"
)
PR_BOUNDARY_VALIDATOR_PATH = "scripts/validate_daily_production_boundaries.py"

PR_SAFE_COMMAND = (
    'python scripts/validate_repo_advanced_integrity_pr_safe.py --base-ref "$BASE_SHA"'
)
STRICT_RUNTIME_TEST = (
    "tests/test_repo_advanced_integrity.py::"
    "test_repo_advanced_integrity_validator_passes"
)
STRICT_RUNTIME_TEST_DESELECT = f"--deselect {STRICT_RUNTIME_TEST}"

SOURCE_IDENTITY_GATE_SELF_UPDATE_ID = "registered-source-identity-pr-safe-v1"
SOURCE_IDENTITY_GATE_SELF_UPDATE_BASE_HELPER_SHA256 = (
    "aa21f0ed72eca64232b253a1818df7a60cf8433baf57fb6b8f06edff89cdcf7a"
)
SOURCE_IDENTITY_GATE_TEST_PATH = "tests/test_repo_advanced_integrity_pr_safe.py"
SOURCE_IDENTITY_GATE_SELF_UPDATE_TEST_MARKER = (
    "def test_registered_source_identity_gate_self_update_is_exact_and_one_time"
)
SOURCE_IDENTITY_GATE_SELF_UPDATE_PATHS = frozenset(
    {
        LIFECYCLE_INVENTORY_PATH,
        PR_SAFE_HELPER_PATH,
        SOURCE_IDENTITY_GATE_TEST_PATH,
    }
)
SOURCE_IDENTITY_ARTIFACT_ROLE = "canonical_source_identity_projection"
SOURCE_IDENTITY_MIGRATION_STATUS = "validated_user_approved_migration"
CANONICAL_LINEAGE_PR_COMMAND = (
    'python scripts/validate_daily_canonical_field_lineage.py --base-ref "$BASE_SHA"'
)

ADDITIVE_RESEARCH_GATE_SELF_UPDATE_ID = (
    "additive-research-validation-registration-pr-safe-v3"
)
ADDITIVE_RESEARCH_GATE_SELF_UPDATE_PATHS = frozenset(
    {PR_SAFE_HELPER_PATH, SOURCE_IDENTITY_GATE_TEST_PATH}
)
ADDITIVE_RESEARCH_GATE_AUTHORIZATIONS_PATH = (
    "config/daily_model_pr_safe_self_migration_authorizations.csv"
)
ADDITIVE_RESEARCH_GATE_AUTHORIZATION_COLUMNS = (
    "migration_id",
    "status",
    "approval_reference",
    "base_helper_sha256",
    "current_helper_sha256",
    "current_test_sha256",
    "changed_paths",
)
RESEARCH_OWNER = "research_backtest"
RESEARCH_WORKFLOW_PATH = ".github/workflows/research_backtest_pipeline.yml"
RESEARCH_ALLOWED_WORKFLOWS = frozenset(
    {PR_VALIDATION_WORKFLOW_PATH, RESEARCH_WORKFLOW_PATH}
)
RESEARCH_WORKFLOW_VALIDATOR_COMMAND_RE = re.compile(
    r"^python (scripts/validate_[A-Za-z0-9_]+\.py)$"
)
RESEARCH_WORKFLOW_TEST_LINE_RE = re.compile(
    r"^(tests/test_[A-Za-z0-9_]+\.py)(?:\s+\\)?$"
)
RESEARCH_WORKFLOW_PATH_FILTER_RE = re.compile(
    r"^(?:config/[a-z0-9][a-z0-9_]*_\*\.csv|"
    r"tests/test_(?:validate_)?[a-z0-9][a-z0-9_]*_\*\.py)$"
)
RESEARCH_WORKFLOW_REGRESSION_TEST_PATH = (
    "tests/test_daily_model_maintenance_pr_validation_workflow.py"
)
RESEARCH_CONTROL_PYTHON_ALLOWLIST = {
    "scripts/model_data_independence.py": ("repo_infrastructure", "python"),
    "scripts/validate_daily_model_background_data_registry.py": (
        "repo_infrastructure",
        "python",
    ),
    "scripts/validate_model_research_workflow_isolation.py": (
        "repo_infrastructure",
        "python",
    ),
    "tests/test_daily_model_background_data_registry.py": (
        "repo_infrastructure",
        "test_python",
    ),
    RESEARCH_WORKFLOW_REGRESSION_TEST_PATH: ("daily_production", "test_python"),
    "tests/test_model_data_independence.py": (
        "repo_infrastructure",
        "test_python",
    ),
    "tests/test_model_research_artifact_ownership.py": (
        "repo_infrastructure",
        "test_python",
    ),
    "tests/test_model_research_workflow_isolation.py": (
        "repo_infrastructure",
        "test_python",
    ),
}
RESEARCH_LIFECYCLE_CONTROL_ALLOWLIST = frozenset(
    {
        *RESEARCH_CONTROL_PYTHON_ALLOWLIST,
        "scripts/build_model_data_independence_audit.py",
    }
)
LIFECYCLE_ADDITIVE_LIST_COLUMNS = frozenset(
    {
        "called_by_workflow",
        "imported_by",
        "tested_by",
        "documented_by",
        "writes_artifact",
        "reads_artifact",
    }
)
REGULAR_BLOB_MODES = frozenset({"100644", "100755"})

PR_SAFE_BOOTSTRAP_SURFACES = frozenset(
    {
        PR_SAFE_HELPER_PATH,
        PR_VALIDATION_WORKFLOW_PATH,
        PRODUCTION_INVENTORY_PATH,
    }
)

STRICT_EXACT_PATHS = frozenset(
    {
        ".github/workflows/daily_full_pipeline.yml",
        ".github/workflows/historical_structured_source_replay.yml",
        PR_VALIDATION_WORKFLOW_PATH,
        "build_data_freshness_latest.py",
        "docs/latest/data_freshness_latest.csv",
        "docs/latest/data_freshness_latest.md",
        EXTERNAL_SOURCE_CONTRACT_PATH,
        FRESHNESS_RELATIVE_PATH,
        "output/latest/data_freshness_latest.md",
        PRODUCTION_INVENTORY_PATH,
        PR_BOUNDARY_VALIDATOR_PATH,
        PR_SAFE_HELPER_PATH,
        "scripts/replay_historical_structured_sources.py",
        "scripts/resolve_daily_report_source_state.py",
        "scripts/run_chatgpt_daily_report_entrypoint.py",
        STRICT_VALIDATOR_PATH,
        "output/latest/chatgpt_daily_pdf_semantic_manifest.csv",
        "output/latest/chatgpt_daily_report_runtime_manifest.json",
        "output/latest/report_manifest_latest.json",
    }
)

STRICT_PATH_PREFIXES = (
    "docs/latest/published_reports/",
    "output/history/daily_model_snapshots/",
    "output/latest/chatgpt_side_outputs_official/",
    "output/latest/published_reports/",
)

HISTORICAL_REPLAY_REPORT_READY_NOTE = (
    "historical structured-source replay updates objective-source freshness only; "
    "publish artifacts remain stale"
)
HISTORICAL_REPLAY_DAILY_PDF_READY_NOTE = (
    "historical structured-source replay must not mark stale daily PDFs ready"
)

EXPECTED_REPLAY_SOURCE_COLUMNS = {
    "official_daily_price": ("official_price_fetch_date", "report_ready"),
    "daily_stock_monitor": ("stock_monitor_price_date", "report_ready"),
    "all_candidates": ("all_candidates_date", "report_ready"),
    "daily_pdf_source": ("main_price_date", "daily_pdf_ready"),
}
ALLOWED_STALE_DATE_SOURCES = frozenset(
    {"daily_stock_monitor", "all_candidates"}
)


def split_list(value: str) -> list[str]:
    return [part.strip() for part in str(value or "").split(";") if part.strip()]


def read_csv_rows(path: Path) -> list[dict[str, str]]:
    try:
        with path.open("r", encoding="utf-8-sig", newline="") as handle:
            return [
                {key: str(value or "") for key, value in row.items()}
                for row in csv.DictReader(handle)
            ]
    except (OSError, UnicodeError, csv.Error):
        return []


def parse_csv_payload(
    payload: bytes | None,
    *,
    source: str,
) -> tuple[list[dict[str, str]], list[str]]:
    if payload is None:
        return [], [f"cannot read CSV evidence: {source}"]
    try:
        text = payload.decode("utf-8-sig")
        reader = csv.DictReader(io.StringIO(text, newline=""))
        if not reader.fieldnames:
            return [], [f"CSV evidence has no header: {source}"]
        rows: list[dict[str, str]] = []
        for line_number, row in enumerate(reader, start=2):
            if None in row:
                return [], [
                    f"CSV evidence row has extra fields: {source}:{line_number}"
                ]
            rows.append(
                {str(key): str(value or "") for key, value in row.items()}
            )
        return rows, []
    except (UnicodeError, csv.Error) as exc:
        return [], [f"cannot parse CSV evidence {source}: {exc}"]


def append_only_csv_rows(
    base_ref: str,
    path: str,
    *,
    repository_root: Path,
) -> tuple[list[dict[str, str]], list[str]]:
    base_payload = git_blob_at_ref(
        base_ref,
        path,
        repository_root=repository_root,
    )
    try:
        current_payload = (repository_root / path).read_bytes()
    except OSError as exc:
        return [], [f"cannot read current CSV evidence {path}: {exc}"]
    base_rows, base_errors = parse_csv_payload(
        base_payload,
        source=f"{base_ref}:{path}",
    )
    current_rows, current_errors = parse_csv_payload(
        current_payload,
        source=path,
    )
    if base_errors or current_errors:
        return [], [*base_errors, *current_errors]
    if len(current_rows) < len(base_rows) or current_rows[: len(base_rows)] != base_rows:
        return [], [
            f"registered source-identity evidence must be append-only: {path}"
        ]
    return current_rows[len(base_rows) :], []


def additive_csv_rows(
    base_ref: str,
    path: str,
    *,
    key: str,
    repository_root: Path,
) -> tuple[list[dict[str, str]], list[str]]:
    base_payload = git_blob_at_ref(
        base_ref,
        path,
        repository_root=repository_root,
    )
    try:
        current_payload = (repository_root / path).read_bytes()
    except OSError as exc:
        return [], [f"cannot read current CSV evidence {path}: {exc}"]
    base_rows, base_errors = parse_csv_payload(
        base_payload,
        source=f"{base_ref}:{path}",
    )
    current_rows, current_errors = parse_csv_payload(
        current_payload,
        source=path,
    )
    if base_errors or current_errors:
        return [], [*base_errors, *current_errors]
    base_by_key = {row.get(key, "").strip(): row for row in base_rows}
    current_by_key = {row.get(key, "").strip(): row for row in current_rows}
    if (
        "" in base_by_key
        or "" in current_by_key
        or len(base_by_key) != len(base_rows)
        or len(current_by_key) != len(current_rows)
    ):
        return [], [f"additive CSV evidence has blank or duplicate {key}: {path}"]
    changed_base_keys = sorted(
        observed_key
        for observed_key, base_row in base_by_key.items()
        if current_by_key.get(observed_key) != base_row
    )
    if changed_base_keys:
        return [], [
            f"registered source-identity evidence may not change base {path} row(s): "
            + ", ".join(changed_base_keys)
        ]
    return [
        row for row in current_rows if row.get(key, "").strip() not in base_by_key
    ], []


def canonical_repository_bytes(payload: bytes) -> bytes:
    return payload.replace(b"\r\n", b"\n").replace(b"\r", b"\n")


def canonical_sha256(payload: bytes) -> str:
    return hashlib.sha256(canonical_repository_bytes(payload)).hexdigest()


def assigned_expressions(nodes: list[ast.stmt]) -> dict[str, ast.expr]:
    assignments: dict[str, ast.expr] = {}
    assignment_counts: dict[str, int] = {}
    for statement in nodes:
        target: ast.expr | None = None
        value: ast.expr | None = None
        if isinstance(statement, ast.Assign) and len(statement.targets) == 1:
            target = statement.targets[0]
            value = statement.value
        elif isinstance(statement, ast.AnnAssign) and isinstance(
            statement.target, ast.Name
        ):
            target = statement.target
            value = statement.value
        if isinstance(target, ast.Name) and value is not None:
            assignments[target.id] = value
            assignment_counts[target.id] = assignment_counts.get(target.id, 0) + 1
    return {
        name: expression
        for name, expression in assignments.items()
        if assignment_counts[name] == 1
    }


def assignment_name_and_value(
    statement: ast.stmt,
) -> tuple[str, ast.expr] | None:
    if isinstance(statement, ast.Assign) and len(statement.targets) == 1:
        target = statement.targets[0]
        if isinstance(target, ast.Name):
            return target.id, statement.value
    if (
        isinstance(statement, ast.AnnAssign)
        and isinstance(statement.target, ast.Name)
        and statement.value is not None
    ):
        return statement.target.id, statement.value
    return None


def literal_string_sequence(expression: ast.expr) -> set[str] | None:
    if not isinstance(expression, (ast.Tuple, ast.List, ast.Set)):
        return None
    values = {
        element.value
        for element in expression.elts
        if isinstance(element, ast.Constant) and isinstance(element.value, str)
    }
    return values if len(values) == len(expression.elts) else None


def asserted_literal(
    expression: ast.expr,
    *,
    trusted_text_names: set[str],
    expected_left_name: str | None = None,
) -> str | None:
    if not (
        isinstance(expression, ast.Compare)
        and len(expression.ops) == 1
        and isinstance(expression.ops[0], ast.In)
        and len(expression.comparators) == 1
        and isinstance(expression.comparators[0], ast.Name)
        and expression.comparators[0].id in trusted_text_names
    ):
        return None
    if expected_left_name is not None:
        return (
            expected_left_name
            if isinstance(expression.left, ast.Name)
            and expression.left.id == expected_left_name
            else None
        )
    return (
        expression.left.value
        if isinstance(expression.left, ast.Constant)
        and isinstance(expression.left.value, str)
        else None
    )


def static_path_components(
    expression: ast.expr,
    assignments: dict[str, ast.expr],
    seen: frozenset[str] = frozenset(),
) -> tuple[str, ...]:
    if isinstance(expression, ast.Name):
        if expression.id in seen or expression.id not in assignments:
            return ()
        return static_path_components(
            assignments[expression.id],
            assignments,
            seen | {expression.id},
        )
    if isinstance(expression, ast.Constant) and isinstance(expression.value, str):
        return tuple(
            part
            for part in expression.value.replace("\\", "/").split("/")
            if part not in {"", "."}
        )
    if isinstance(expression, ast.BinOp) and isinstance(expression.op, ast.Div):
        return (
            *static_path_components(expression.left, assignments, seen),
            *static_path_components(expression.right, assignments, seen),
        )
    if (
        isinstance(expression, ast.Call)
        and isinstance(expression.func, ast.Name)
        and expression.func.id == "Path"
        and len(expression.args) == 1
    ):
        return static_path_components(expression.args[0], assignments, seen)
    return ()


def reads_pr_validation_workflow(
    expression: ast.expr,
    assignments: dict[str, ast.expr],
    seen: frozenset[str] = frozenset(),
) -> bool:
    if isinstance(expression, ast.Name):
        if expression.id in seen or expression.id not in assignments:
            return False
        return reads_pr_validation_workflow(
            assignments[expression.id],
            assignments,
            seen | {expression.id},
        )
    if not (
        isinstance(expression, ast.Call)
        and isinstance(expression.func, ast.Attribute)
        and expression.func.attr == "read_text"
    ):
        return False
    observed = static_path_components(expression.func.value, assignments)
    expected = tuple(PR_VALIDATION_WORKFLOW_PATH.split("/"))
    return len(observed) >= len(expected) and observed[-len(expected) :] == expected


def asserted_workflow_regression_literals(source: str) -> tuple[set[str], list[str]]:
    try:
        module = ast.parse(source)
    except SyntaxError as exc:
        return set(), [f"cannot parse PR workflow regression evidence: {exc}"]

    asserted: set[str] = set()
    module_assignments = assigned_expressions(module.body)
    for function in (
        node
        for node in module.body
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef))
        and node.name.startswith("test_")
    ):
        assignments = dict(module_assignments)
        sequences: dict[str, set[str]] = {}
        trusted_text_names: set[str] = set()
        for statement in function.body:
            assignment = assignment_name_and_value(statement)
            if assignment is not None:
                name, value = assignment
                assignments[name] = value
                trusted_text_names.discard(name)
                sequences.pop(name, None)
                values = literal_string_sequence(value)
                if values is not None:
                    sequences[name] = values
                if reads_pr_validation_workflow(value, assignments):
                    trusted_text_names.add(name)
                continue

            if isinstance(statement, ast.Assert):
                literal = asserted_literal(
                    statement.test,
                    trusted_text_names=trusted_text_names,
                )
                if literal is not None:
                    asserted.add(literal)
                continue

            if not (
                isinstance(statement, ast.For)
                and isinstance(statement.target, ast.Name)
                and isinstance(statement.iter, ast.Name)
                and not statement.orelse
                and len(statement.body) == 1
                and isinstance(statement.body[0], ast.Assert)
            ):
                continue
            values = sequences.get(statement.iter.id)
            if not values:
                continue
            asserted_item = asserted_literal(
                statement.body[0].test,
                trusted_text_names=trusted_text_names,
                expected_left_name=statement.target.id,
            )
            if asserted_item is not None:
                asserted.update(values)
    return asserted, []


def additive_sequence_items(
    base_items: list[str],
    current_items: list[str],
) -> list[str] | None:
    additions: list[str] = []
    base_index = 0
    for item in current_items:
        if base_index < len(base_items) and item == base_items[base_index]:
            base_index += 1
        else:
            additions.append(item)
    return additions if base_index == len(base_items) else None


def additive_text_lines(base_text: str, current_text: str) -> list[str] | None:
    return additive_sequence_items(
        canonical_repository_bytes(base_text.encode("utf-8")).decode("utf-8").splitlines(),
        canonical_repository_bytes(current_text.encode("utf-8"))
        .decode("utf-8")
        .splitlines(),
    )


def parse_workflow_document(
    payload: bytes | None,
    *,
    source: str,
) -> tuple[dict[str, object], list[str]]:
    if payload is None:
        return {}, [f"cannot read workflow evidence: {source}"]
    try:
        document = yaml.load(payload.decode("utf-8-sig"), Loader=yaml.BaseLoader)
    except (UnicodeError, yaml.YAMLError) as exc:
        return {}, [f"cannot parse workflow evidence {source}: {exc}"]
    if not isinstance(document, dict):
        return {}, [f"workflow evidence must be a mapping: {source}"]
    return document, []


def csv_rows_by_key(
    payload: bytes | None,
    *,
    source: str,
    key: str = "path",
) -> tuple[dict[str, dict[str, str]], list[str]]:
    rows, errors = parse_csv_payload(payload, source=source)
    if errors:
        return {}, errors
    rows_by_key: dict[str, dict[str, str]] = {}
    for row in rows:
        observed_key = row.get(key, "").strip()
        if not observed_key:
            errors.append(f"CSV evidence has blank {key}: {source}")
        elif observed_key in rows_by_key:
            errors.append(
                f"CSV evidence has duplicate {key}={observed_key}: {source}"
            )
        else:
            rows_by_key[observed_key] = row
    return rows_by_key, errors


def validate_research_production_inventory_delta(
    base_ref: str,
    changed_paths: set[str],
    *,
    repository_root: Path,
) -> tuple[dict[str, dict[str, str]], set[str], list[str]]:
    base_payload = git_blob_at_ref(
        base_ref,
        PRODUCTION_INVENTORY_PATH,
        repository_root=repository_root,
    )
    try:
        current_payload = (repository_root / PRODUCTION_INVENTORY_PATH).read_bytes()
    except OSError as exc:
        return {}, set(), [
            f"cannot read current research inventory evidence: {exc}"
        ]

    base_rows, base_errors = csv_rows_by_key(
        base_payload,
        source=f"{base_ref}:{PRODUCTION_INVENTORY_PATH}",
    )
    current_rows, current_errors = csv_rows_by_key(
        current_payload,
        source=PRODUCTION_INVENTORY_PATH,
    )
    errors = [*base_errors, *current_errors]
    if errors:
        return {}, set(), errors

    base_headers = list(next(iter(base_rows.values()), {}))
    current_headers = list(next(iter(current_rows.values()), {}))
    if base_headers != current_headers:
        errors.append("research inventory header may not change")

    removed_paths = sorted(set(base_rows) - set(current_rows))
    if removed_paths:
        errors.append(
            "research inventory may not delete existing row(s): "
            + ", ".join(removed_paths)
        )

    for path in sorted(set(base_rows) & set(current_rows)):
        base_row = base_rows[path]
        current_row = current_rows[path]
        changed_columns = {
            column
            for column in set(base_row) | set(current_row)
            if base_row.get(column, "") != current_row.get(column, "")
        }
        if not changed_columns:
            continue
        if changed_columns != {"purpose"}:
            errors.append(
                "research inventory existing-row semantics may not change: "
                f"{path} columns={','.join(sorted(changed_columns))}"
            )
            continue
        if base_row.get("owner", "").strip() != RESEARCH_OWNER:
            errors.append(
                "only a research_backtest row may receive a purpose-only update: "
                + path
            )
        if path not in changed_paths or not (repository_root / path).is_file():
            errors.append(
                "purpose-only research inventory update must describe a changed file: "
                + path
            )

    added_paths = set(current_rows) - set(base_rows)
    for path in sorted(added_paths):
        row = current_rows[path]
        kind = row.get("kind", "").strip()
        owner = row.get("owner", "").strip()
        status = row.get("status", "").strip()
        workflows = set(split_list(row.get("allowed_workflows", "")))
        stage_patterns = row.get("allowed_stage_patterns", "").strip()
        expected_prefix = "tests/" if kind == "test_python" else "scripts/"
        if owner != RESEARCH_OWNER or kind not in {"python", "test_python"}:
            errors.append(
                "additive inventory row must be research_backtest python/test_python: "
                + path
            )
        if status != "active":
            errors.append(f"additive research inventory row must be active: {path}")
        if not path.startswith(expected_prefix) or not path.endswith(".py"):
            errors.append(
                f"additive research inventory path/kind mismatch: {path} kind={kind}"
            )
        if workflows - set(RESEARCH_ALLOWED_WORKFLOWS):
            errors.append(
                "additive research inventory row references a non-research workflow: "
                + path
            )
        if kind == "python" and RESEARCH_WORKFLOW_PATH not in workflows:
            errors.append(
                "additive research python row lacks the research workflow: " + path
            )
        if kind == "test_python" and workflows:
            errors.append(
                "additive research test row must not be a workflow command: " + path
            )
        if stage_patterns:
            errors.append(
                "additive research inventory row may not add stage patterns: " + path
            )
        if path not in changed_paths or not (repository_root / path).is_file():
            errors.append(
                "additive research inventory row is not a changed current file: " + path
            )
        existed_at_base = git_path_exists_at_ref(
            base_ref,
            path,
            repository_root=repository_root,
        )
        if existed_at_base is not False:
            errors.append(
                "additive research inventory row must register a new file: " + path
            )

    changed_python_paths: set[str] = set()
    new_python_paths: set[str] = set()
    for path in sorted(changed_paths):
        if not (
            path.endswith(".py")
            and (path.startswith("scripts/") or path.startswith("tests/"))
            and (repository_root / path).is_file()
        ):
            continue
        changed_python_paths.add(path)
        existed_at_base = git_path_exists_at_ref(
            base_ref,
            path,
            repository_root=repository_root,
        )
        if existed_at_base is False:
            new_python_paths.add(path)
        elif existed_at_base is None:
            errors.append(f"cannot verify base existence for changed Python path: {path}")

    if new_python_paths != added_paths:
        missing_rows = sorted(new_python_paths - added_paths)
        phantom_rows = sorted(added_paths - new_python_paths)
        if missing_rows:
            errors.append(
                "new research Python path lacks production inventory registration: "
                + ", ".join(missing_rows)
            )
        if phantom_rows:
            errors.append(
                "additive research inventory row does not map to a new Python path: "
                + ", ".join(phantom_rows)
            )

    for path in sorted(changed_python_paths):
        row = current_rows.get(path)
        if row is None:
            errors.append(
                "changed Python path lacks production inventory ownership: " + path
            )
            continue
        owner = row.get("owner", "").strip()
        kind = row.get("kind", "").strip()
        status = row.get("status", "").strip()
        expected_kind = "test_python" if path.startswith("tests/") else "python"
        if owner == RESEARCH_OWNER:
            if kind != expected_kind or status != "active":
                errors.append(
                    "changed research Python path has invalid ownership metadata: "
                    f"{path} owner={owner} kind={kind} status={status}"
                )
            continue
        expected_control = RESEARCH_CONTROL_PYTHON_ALLOWLIST.get(path)
        if expected_control is None or (owner, kind) != expected_control or status != "active":
            errors.append(
                "changed Python path is outside the additive research ownership boundary: "
                f"{path} owner={owner} kind={kind} status={status}"
            )
    return current_rows, added_paths, errors


def validate_additive_research_workflow_delta(
    base_ref: str,
    changed_paths: set[str],
    *,
    repository_root: Path,
) -> tuple[set[str], set[str], set[str], list[str]]:
    base_payload = git_blob_at_ref(
        base_ref,
        PR_VALIDATION_WORKFLOW_PATH,
        repository_root=repository_root,
    )
    try:
        current_payload = (repository_root / PR_VALIDATION_WORKFLOW_PATH).read_bytes()
    except OSError as exc:
        return set(), set(), set(), [
            f"cannot read current research workflow evidence: {exc}"
        ]
    base_document, base_errors = parse_workflow_document(
        base_payload,
        source=f"{base_ref}:{PR_VALIDATION_WORKFLOW_PATH}",
    )
    current_document, current_errors = parse_workflow_document(
        current_payload,
        source=PR_VALIDATION_WORKFLOW_PATH,
    )
    errors = [*base_errors, *current_errors]
    if errors:
        return set(), set(), set(), errors

    base_copy = copy.deepcopy(base_document)
    current_copy = copy.deepcopy(current_document)
    try:
        base_paths = base_copy["on"]["pull_request"]["paths"]  # type: ignore[index]
        current_paths = current_copy["on"]["pull_request"]["paths"]  # type: ignore[index]
    except (KeyError, TypeError):
        return set(), set(), set(), [
            "research workflow must retain on.pull_request.paths structure"
        ]
    if not isinstance(base_paths, list) or not isinstance(current_paths, list):
        return set(), set(), set(), [
            "research workflow pull_request paths must remain lists"
        ]
    if not all(isinstance(value, str) for value in [*base_paths, *current_paths]):
        return set(), set(), set(), [
            "research workflow pull_request paths must contain only strings"
        ]
    path_additions = additive_sequence_items(base_paths, current_paths)
    if path_additions is None:
        errors.append("research workflow may not delete or rewrite trigger paths")
        path_additions = []
    current_copy["on"]["pull_request"]["paths"] = base_paths  # type: ignore[index]

    validator_paths: set[str] = set()
    test_paths: set[str] = set()
    base_jobs = base_copy.get("jobs")
    current_jobs = current_copy.get("jobs")
    if not isinstance(base_jobs, dict) or not isinstance(current_jobs, dict):
        errors.append("research workflow jobs must remain mappings")
    else:
        for job_name, base_job in base_jobs.items():
            current_job = current_jobs.get(job_name)
            if not isinstance(base_job, dict) or not isinstance(current_job, dict):
                continue
            base_steps = base_job.get("steps")
            current_steps = current_job.get("steps")
            if not isinstance(base_steps, list) or not isinstance(current_steps, list):
                continue
            if len(base_steps) != len(current_steps):
                errors.append(
                    f"research workflow may not add or remove job steps: {job_name}"
                )
                continue
            for index, (base_step, current_step) in enumerate(
                zip(base_steps, current_steps)
            ):
                if not isinstance(base_step, dict) or not isinstance(current_step, dict):
                    continue
                base_run = base_step.get("run")
                current_run = current_step.get("run")
                if base_run == current_run:
                    continue
                if not isinstance(base_run, str) or not isinstance(current_run, str):
                    errors.append(
                        "research workflow may change only existing run command lists: "
                        f"{job_name}[{index}]"
                    )
                    continue
                additions = additive_text_lines(base_run, current_run)
                if additions is None:
                    errors.append(
                        "research workflow may not delete or rewrite an existing command: "
                        f"{job_name}[{index}]"
                    )
                    continue
                step_validators: set[str] = set()
                step_tests: set[str] = set()
                for line in additions:
                    stripped = line.strip()
                    if not stripped:
                        continue
                    validator_match = RESEARCH_WORKFLOW_VALIDATOR_COMMAND_RE.fullmatch(
                        stripped
                    )
                    test_match = RESEARCH_WORKFLOW_TEST_LINE_RE.fullmatch(stripped)
                    if validator_match:
                        step_validators.add(validator_match.group(1))
                    elif test_match:
                        step_tests.add(test_match.group(1))
                    else:
                        errors.append(
                            "research workflow contains a non-additive-validation line: "
                            + stripped
                        )
                if step_validators and "python -m pytest" in base_run:
                    errors.append(
                        "research validator commands may not be inserted into pytest step"
                    )
                if step_tests and "python -m pytest" not in base_run:
                    errors.append(
                        "research test paths may be inserted only into existing pytest step"
                    )
                validator_paths.update(step_validators)
                test_paths.update(step_tests)
                current_step["run"] = base_run

    if base_copy != current_copy:
        errors.append(
            "research workflow changes permissions, triggers outside additive paths, "
            "jobs, steps, or other protected semantics"
        )
    if not validator_paths or not test_paths:
        errors.append(
            "additive research workflow migration requires validator commands and tests"
        )
    return set(path_additions), validator_paths, test_paths, errors


def base_governed_research_dependencies(
    base_ref: str,
    *,
    repository_root: Path,
) -> tuple[set[tuple[str, str]], list[str]]:
    payload = git_blob_at_ref(
        base_ref,
        BACKGROUND_DATA_REGISTRY_PATH,
        repository_root=repository_root,
    )
    if payload is None:
        return set(), ["base-owned background data registry is missing"]
    try:
        reader = csv.DictReader(io.StringIO(payload.decode("utf-8-sig"), newline=""))
        required = {
            "scope",
            "producer",
            "source_artifacts",
            "consumer_surfaces",
            "consumer_models",
            "forbidden_use",
            "cleanup_status",
        }
        if not required.issubset(set(reader.fieldnames or ())):
            return set(), ["base-owned background data registry header mismatch"]
        governed: set[tuple[str, str]] = set()
        for row in reader:
            if None in row:
                return set(), ["base-owned background data registry has extra fields"]
            producer = normalize_repository_path(row.get("producer", ""))
            if not (
                row.get("scope", "").strip() == "model_research_output"
                and "research_backtest" in split_list(
                    row.get("consumer_surfaces", "")
                )
                and row.get("consumer_models", "").strip() not in {"", "all_models"}
                and row.get("cleanup_status", "").strip() == "active"
                and "production" in row.get("forbidden_use", "").lower()
            ):
                continue
            governed.update(
                (producer, normalize_repository_path(source))
                for source in split_list(row.get("source_artifacts", ""))
            )
        return governed, []
    except (UnicodeError, csv.Error) as exc:
        return set(), [f"cannot parse base-owned background data registry: {exc}"]


def unchanged_base_regular_blob_dependency(
    base_ref: str,
    path: str,
    *,
    repository_root: Path,
) -> bool:
    entry = git_tree_entry_at_ref(
        base_ref,
        path,
        repository_root=repository_root,
    )
    base_payload = git_blob_at_ref(base_ref, path, repository_root=repository_root)
    try:
        current_payload = (repository_root / path).read_bytes()
    except OSError:
        return False
    if entry is None or base_payload is None:
        return False
    mode, object_type, object_id, observed_path = entry
    return bool(
        mode in REGULAR_BLOB_MODES
        and object_type == "blob"
        and re.fullmatch(r"[0-9a-f]{40}", object_id)
        and observed_path == path
        and canonical_repository_bytes(base_payload)
        == canonical_repository_bytes(current_payload)
    )


def validate_research_lifecycle_inventory_delta(
    base_ref: str,
    changed_paths: set[str],
    added_inventory_paths: set[str],
    *,
    repository_root: Path,
) -> tuple[dict[str, dict[str, str]], list[str]]:
    base_payload = git_blob_at_ref(
        base_ref,
        LIFECYCLE_INVENTORY_PATH,
        repository_root=repository_root,
    )
    try:
        current_payload = (repository_root / LIFECYCLE_INVENTORY_PATH).read_bytes()
    except OSError as exc:
        return {}, [f"cannot read current lifecycle inventory evidence: {exc}"]
    base_rows, base_errors = csv_rows_by_key(
        base_payload,
        source=f"{base_ref}:{LIFECYCLE_INVENTORY_PATH}",
    )
    current_rows, current_errors = csv_rows_by_key(
        current_payload,
        source=LIFECYCLE_INVENTORY_PATH,
    )
    errors = [*base_errors, *current_errors]
    if errors:
        return current_rows, errors
    governed_dependencies, governance_errors = base_governed_research_dependencies(
        base_ref,
        repository_root=repository_root,
    )
    errors.extend(governance_errors)

    base_migration_payload = git_blob_at_ref(
        base_ref,
        LIFECYCLE_SEMANTIC_MIGRATIONS_PATH,
        repository_root=repository_root,
    )
    try:
        current_migration_payload = (
            repository_root / LIFECYCLE_SEMANTIC_MIGRATIONS_PATH
        ).read_bytes()
    except OSError as exc:
        current_migration_payload = None
        errors.append(f"cannot read lifecycle semantic migration evidence: {exc}")

    def parse_migration_rows(
        payload: bytes | None,
        *,
        source: str,
    ) -> list[dict[str, str]]:
        if payload is None:
            errors.append(f"cannot read lifecycle semantic migration evidence: {source}")
            return []
        try:
            reader = csv.DictReader(
                io.StringIO(payload.decode("utf-8-sig"), newline="")
            )
            if tuple(reader.fieldnames or ()) != LIFECYCLE_SEMANTIC_MIGRATION_COLUMNS:
                errors.append(
                    "lifecycle semantic migration header mismatch: " + source
                )
                return []
            rows: list[dict[str, str]] = []
            for line_number, row in enumerate(reader, start=2):
                if None in row:
                    errors.append(
                        "lifecycle semantic migration row has extra fields: "
                        f"{source}:{line_number}"
                    )
                    continue
                rows.append(
                    {str(key): str(value or "") for key, value in row.items()}
                )
            return rows
        except (UnicodeError, csv.Error) as exc:
            errors.append(
                f"cannot parse lifecycle semantic migration evidence {source}: {exc}"
            )
            return []

    base_migrations = parse_migration_rows(
        base_migration_payload,
        source=f"{base_ref}:{LIFECYCLE_SEMANTIC_MIGRATIONS_PATH}",
    )
    current_migrations = parse_migration_rows(
        current_migration_payload,
        source=LIFECYCLE_SEMANTIC_MIGRATIONS_PATH,
    )
    if (
        base_migration_payload is None
        or current_migration_payload is None
        or canonical_repository_bytes(current_migration_payload)
        != canonical_repository_bytes(base_migration_payload)
        or current_migrations != base_migrations
    ):
        errors.append(
            "base-owned lifecycle semantic authorization ledger may not change in the PR"
        )

    migration_ids = [row.get("migration_id", "").strip() for row in current_migrations]
    if any(not migration_id for migration_id in migration_ids) or len(
        migration_ids
    ) != len(set(migration_ids)):
        errors.append("lifecycle semantic migration ids must be nonblank and unique")

    migrations_by_target: dict[tuple[str, str], dict[str, str]] = {}
    for migration in base_migrations:
        target = (
            normalize_repository_path(migration.get("row_path", "")),
            migration.get("column", "").strip(),
        )
        if not all(target) or target in migrations_by_target:
            errors.append(
                "base-owned lifecycle authorizations must have unique row_path/column"
            )
            continue
        migrations_by_target[target] = migration

    base_headers = list(next(iter(base_rows.values()), {}))
    current_headers = list(next(iter(current_rows.values()), {}))
    if base_headers != current_headers:
        errors.append("research lifecycle inventory header may not change")

    removed_paths = sorted(set(base_rows) - set(current_rows))
    if removed_paths:
        errors.append(
            "research lifecycle inventory may not delete existing row(s): "
            + ", ".join(removed_paths)
        )

    for path in sorted(set(base_rows) & set(current_rows)):
        base_row = base_rows[path]
        current_row = current_rows[path]
        changed_columns = {
            column
            for column in set(base_row) | set(current_row)
            if base_row.get(column, "") != current_row.get(column, "")
        }
        if not changed_columns:
            continue
        owner = current_row.get("owner", "").strip()
        if owner != RESEARCH_OWNER and path not in RESEARCH_LIFECYCLE_CONTROL_ALLOWLIST:
            errors.append(
                "existing non-research lifecycle row is outside the control allowlist: "
                + path
            )
        for column in sorted(changed_columns):
            if column in LIFECYCLE_ADDITIVE_LIST_COLUMNS:
                base_values = split_list(base_row.get(column, ""))
                current_values = split_list(current_row.get(column, ""))
                additions = additive_sequence_items(base_values, current_values)
                migration = migrations_by_target.get((path, column))
                base_value = base_row.get(column, "")
                current_value = current_row.get(column, "")
                expected_added = sorted(set(current_values) - set(base_values))
                expected_removed = sorted(set(base_values) - set(current_values))
                if migration is not None:
                    owner_is_authorized = (
                        owner == RESEARCH_OWNER
                        or path in RESEARCH_LIFECYCLE_CONTROL_ALLOWLIST
                    )
                    if not (
                        owner_is_authorized
                        and (expected_added or expected_removed)
                        and migration.get("status", "").strip()
                        == LIFECYCLE_SEMANTIC_MIGRATION_STATUS
                        and migration.get("scope", "").strip()
                        == LIFECYCLE_SEMANTIC_MIGRATION_SCOPE
                        and bool(migration.get("approval_reference", "").strip())
                        and migration.get("base_value_sha256", "").strip()
                        == canonical_sha256(base_value.encode("utf-8"))
                        and migration.get("current_value_sha256", "").strip()
                        == canonical_sha256(current_value.encode("utf-8"))
                        and split_list(migration.get("added_values", ""))
                        == expected_added
                        and split_list(migration.get("removed_values", ""))
                        == expected_removed
                    ):
                        errors.append(
                            "base-owned lifecycle authorization does not match exact "
                            "base/current evidence: "
                            f"{path} column={column}"
                        )
                    added_values = expected_added
                elif additions is not None and additions:
                    added_values = additions
                else:
                    errors.append(
                        "research lifecycle list rewrite requires base-owned exact "
                        f"authorization: {path} column={column}"
                    )
                    continue
                unchanged_governed = {
                    value
                    for value in added_values
                    if migration is not None
                    and column == "reads_artifact"
                    and value not in changed_paths
                    and (path, value) in governed_dependencies
                    and unchanged_base_regular_blob_dependency(
                        base_ref,
                        value,
                        repository_root=repository_root,
                    )
                }
                unbound = sorted(
                    value
                    for value in added_values
                    if value not in changed_paths
                    and value not in added_inventory_paths
                    and value not in unchanged_governed
                )
                if unbound:
                    errors.append(
                        "research lifecycle addition is not bound to a changed path: "
                        f"{path} column={column} values={','.join(unbound)}"
                    )
            elif (
                column == "keep_reason"
                and owner == RESEARCH_OWNER
                and path in changed_paths
            ):
                continue
            else:
                errors.append(
                    "existing lifecycle governance semantics may not change: "
                    f"{path} column={column}"
                )
    if LIFECYCLE_SEMANTIC_MIGRATIONS_PATH in changed_paths:
        errors.append(
            "base-owned lifecycle semantic authorization ledger is immutable in the PR"
        )
    return current_rows, errors


def validate_additive_research_validation_registration(
    base_ref: str,
    changed_paths: set[str],
    strict_surface_changes: set[str],
    *,
    repository_root: Path,
) -> tuple[bool, list[str]]:
    expected_strict_surfaces = {
        PR_VALIDATION_WORKFLOW_PATH,
        PRODUCTION_INVENTORY_PATH,
    }
    if strict_surface_changes != expected_strict_surfaces:
        return False, []

    current_inventory, added_inventory_paths, inventory_errors = (
        validate_research_production_inventory_delta(
            base_ref,
            changed_paths,
            repository_root=repository_root,
        )
    )
    path_patterns, validator_paths, test_paths, workflow_errors = (
        validate_additive_research_workflow_delta(
            base_ref,
            changed_paths,
            repository_root=repository_root,
        )
    )
    errors = [*inventory_errors, *workflow_errors]

    try:
        workflow_test = (
            repository_root / RESEARCH_WORKFLOW_REGRESSION_TEST_PATH
        ).read_text(encoding="utf-8")
    except (OSError, UnicodeError) as exc:
        errors.append(f"cannot read additive research registry evidence: {exc}")
        workflow_test = ""
    lifecycle_rows, lifecycle_errors = validate_research_lifecycle_inventory_delta(
        base_ref,
        changed_paths,
        added_inventory_paths,
        repository_root=repository_root,
    )
    errors.extend(lifecycle_errors)
    asserted_literals, assertion_errors = asserted_workflow_regression_literals(
        workflow_test
    )
    errors.extend(assertion_errors)
    if LIFECYCLE_INVENTORY_PATH not in changed_paths:
        errors.append("additive research migration must update lifecycle inventory")
    if RESEARCH_WORKFLOW_REGRESSION_TEST_PATH not in changed_paths:
        errors.append("additive research migration must update PR workflow regression")

    for path in sorted(added_inventory_paths):
        production = current_inventory.get(path, {})
        lifecycle = lifecycle_rows.get(path, {})
        expected_kind = production.get("kind", "").strip()
        if not (
            lifecycle.get("type", "").strip() == expected_kind
            and lifecycle.get("owner", "").strip() == RESEARCH_OWNER
            and lifecycle.get("status", "").strip() == "active"
        ):
            errors.append(
                "additive research path lacks matching lifecycle registration: " + path
            )
        if path.startswith("scripts/validate_"):
            if path not in validator_paths:
                errors.append(
                    "new research validator is not called by the PR workflow: " + path
                )
            if PR_VALIDATION_WORKFLOW_PATH not in split_list(
                production.get("allowed_workflows", "")
            ):
                errors.append(
                    "new research validator lacks PR workflow inventory permission: "
                    + path
                )
            linked_tests = set(split_list(lifecycle.get("tested_by", "")))
            if not linked_tests.intersection(test_paths):
                errors.append(
                    "new research validator lacks an added focused regression: " + path
                )
        elif expected_kind == "test_python" and path not in test_paths:
            errors.append("new research test is absent from focused pytest: " + path)
        asserted_evidence = f"python {path}" if path in validator_paths else path
        if (
            path in validator_paths or expected_kind == "test_python"
        ) and asserted_evidence not in asserted_literals:
            errors.append(
                "PR workflow regression does not assert additive research path: " + path
            )

    if validator_paths - added_inventory_paths:
        errors.append(
            "workflow invokes an unregistered additive research validator: "
            + ", ".join(sorted(validator_paths - added_inventory_paths))
        )
    if test_paths - added_inventory_paths:
        errors.append(
            "workflow invokes an unregistered additive research test: "
            + ", ".join(sorted(test_paths - added_inventory_paths))
        )

    for pattern in sorted(path_patterns):
        if pattern not in asserted_literals:
            errors.append(
                "PR workflow regression does not assert additive path filter: " + pattern
            )
        if not RESEARCH_WORKFLOW_PATH_FILTER_RE.fullmatch(pattern):
            errors.append(
                "additive research workflow path filter is not narrowly scoped: "
                + pattern
            )
            continue
        matched_paths = {
            path for path in changed_paths if fnmatch.fnmatchcase(path, pattern)
        }
        if not matched_paths:
            errors.append(
                "additive research workflow path filter matches no changed path: "
                + pattern
            )
            continue
        for path in sorted(matched_paths):
            existed_at_base = git_path_exists_at_ref(
                base_ref,
                path,
                repository_root=repository_root,
            )
            if existed_at_base is not False or not (repository_root / path).is_file():
                errors.append(
                    "additive research workflow filter may cover only new current files: "
                    + path
                )
            if path.startswith("tests/") and path not in test_paths:
                errors.append(
                    "additive research test filter path is absent from focused pytest: "
                    + path
                )
        family_token = Path(pattern).name.replace("*", "")
        family_token = family_token.removeprefix("test_").removeprefix("validate_")
        family_token = family_token.removesuffix(".csv").removesuffix(".py")
        if not any(
            family_token in Path(path).name for path in added_inventory_paths
        ):
            errors.append(
                "additive research workflow path filter lacks matching inventory family: "
                + pattern
            )
    return True, errors


def normalize_repository_path(path: str) -> str:
    normalized = str(path).replace("\\", "/")
    while normalized.startswith("./"):
        normalized = normalized[2:]
    return normalized


def changed_paths_from_base(
    base_ref: str,
    *,
    repository_root: Path = ROOT,
    head_ref: str = "HEAD",
) -> tuple[set[str], list[str]]:
    if not str(base_ref or "").strip():
        return set(), ["PR-safe advanced-integrity validation requires a base ref"]
    try:
        proc = subprocess.run(
            [
                "git",
                "diff",
                "--name-only",
                "--no-renames",
                f"{base_ref}...{head_ref}",
                "--",
            ],
            cwd=repository_root,
            capture_output=True,
            text=True,
            check=False,
            timeout=30,
        )
    except (OSError, subprocess.TimeoutExpired) as exc:
        return set(), [
            f"cannot inspect PR changed paths from base_ref={base_ref}: {exc}"
        ]
    if proc.returncode != 0:
        detail = proc.stderr.strip() or proc.stdout.strip() or "git diff failed"
        return set(), [
            f"cannot inspect PR changed paths from base_ref={base_ref}: {detail}"
        ]
    return {
        normalize_repository_path(line)
        for line in proc.stdout.splitlines()
        if normalize_repository_path(line)
    }, []


def git_blob_at_ref(
    ref: str,
    path: str,
    *,
    repository_root: Path,
) -> bytes | None:
    try:
        proc = subprocess.run(
            ["git", "show", f"{ref}:{path}"],
            cwd=repository_root,
            capture_output=True,
            check=False,
            timeout=30,
        )
    except (OSError, subprocess.TimeoutExpired):
        return None
    return proc.stdout if proc.returncode == 0 else None


def git_tree_entry_at_ref(
    ref: str,
    path: str,
    *,
    repository_root: Path,
) -> tuple[str, str, str, str] | None:
    try:
        proc = subprocess.run(
            ["git", "ls-tree", "-z", ref, "--", path],
            cwd=repository_root,
            capture_output=True,
            check=False,
            timeout=30,
        )
    except (OSError, subprocess.TimeoutExpired):
        return None
    entries = [entry for entry in proc.stdout.split(b"\0") if entry]
    if proc.returncode != 0 or len(entries) != 1 or b"\t" not in entries[0]:
        return None
    metadata, raw_path = entries[0].split(b"\t", 1)
    try:
        fields = metadata.decode("ascii", errors="strict").split()
        observed_path = raw_path.decode("utf-8").replace("\\", "/")
    except UnicodeError:
        return None
    if len(fields) != 3:
        return None
    mode, object_type, object_id = fields
    return mode, object_type, object_id, observed_path


def git_path_exists_at_ref(
    ref: str,
    path: str,
    *,
    repository_root: Path,
) -> bool | None:
    try:
        proc = subprocess.run(
            ["git", "ls-tree", "--name-only", ref, "--", path],
            cwd=repository_root,
            capture_output=True,
            text=True,
            check=False,
            timeout=30,
        )
    except (OSError, subprocess.TimeoutExpired):
        return None
    if proc.returncode != 0:
        return None
    observed = {
        normalize_repository_path(line)
        for line in proc.stdout.splitlines()
        if normalize_repository_path(line)
    }
    return normalize_repository_path(path) in observed


def validate_historical_replay_not_ready_marker(
    freshness_path: Path,
) -> list[str]:
    rows = read_csv_rows(freshness_path)
    if len(rows) != 1:
        return [
            "historical-replay freshness marker must contain exactly one row; "
            f"observed={len(rows)}"
        ]
    row = rows[0]
    expected_values = {
        "main_price_date_source": "historical_replay_override",
        "report_ready": "False",
        "daily_pdf_ready": "False",
        "report_ready_note": HISTORICAL_REPLAY_REPORT_READY_NOTE,
        "daily_pdf_ready_note": HISTORICAL_REPLAY_DAILY_PDF_READY_NOTE,
    }
    errors = [
        f"historical-replay freshness marker {column} mismatch: "
        f"expected={expected!r} observed={row.get(column, '').strip()!r}"
        for column, expected in expected_values.items()
        if row.get(column, "").strip() != expected
    ]

    main_price_date = row.get("main_price_date", "").strip()
    replay_date = row.get("historical_replay_main_price_date", "").strip()
    expected_high_water = row.get(
        "expected_price_history_high_water_date", ""
    ).strip()
    actual_high_water = row.get("actual_stock_price_history_date", "").strip()
    dates = {
        "main_price_date": main_price_date,
        "historical_replay_main_price_date": replay_date,
        "expected_price_history_high_water_date": expected_high_water,
        "actual_stock_price_history_date": actual_high_water,
    }
    for label, value in dates.items():
        if not re.fullmatch(r"20\d{6}", value):
            errors.append(
                f"historical-replay freshness marker {label} must be YYYYMMDD; "
                f"observed={value!r}"
            )
    if main_price_date and replay_date and main_price_date != replay_date:
        errors.append(
            "historical_replay_main_price_date must equal main_price_date; "
            f"observed={replay_date!r} main_price_date={main_price_date!r}"
        )
    if expected_high_water and actual_high_water and expected_high_water != actual_high_water:
        errors.append(
            "actual_stock_price_history_date must equal the replay expected high-water date; "
            f"observed={actual_high_water!r} expected={expected_high_water!r}"
        )
    if main_price_date and expected_high_water and expected_high_water < main_price_date:
        errors.append(
            "historical replay expected high-water date cannot precede main_price_date; "
            f"observed={expected_high_water!r} main_price_date={main_price_date!r}"
        )
    return errors


def validate_freshness_is_inherited_from_base(
    base_ref: str,
    *,
    repository_root: Path = ROOT,
) -> list[str]:
    current_path = repository_root / FRESHNESS_RELATIVE_PATH
    try:
        current_payload = current_path.read_bytes()
    except OSError as exc:
        return [f"cannot read current {FRESHNESS_RELATIVE_PATH}: {exc}"]
    base_payload = git_blob_at_ref(
        base_ref,
        FRESHNESS_RELATIVE_PATH,
        repository_root=repository_root,
    )
    if base_payload is None:
        return [
            f"cannot read base freshness artifact from {base_ref}: "
            + FRESHNESS_RELATIVE_PATH
        ]
    if base_payload != current_payload:
        return [
            "PR-safe advanced-integrity validation cannot inherit a changed freshness "
            f"artifact; {FRESHNESS_RELATIVE_PATH} differs from base_ref={base_ref}"
        ]
    return []


def external_source_surface_paths(repository_root: Path) -> set[str]:
    paths: set[str] = set()
    for row in read_csv_rows(repository_root / EXTERNAL_SOURCE_CONTRACT_PATH):
        artifact = normalize_repository_path(row.get("status_artifact", ""))
        if artifact:
            paths.add(artifact)
        for column in ("producer", "validator"):
            paths.update(
                normalize_repository_path(path)
                for path in split_list(row.get(column, ""))
            )
    return paths


def external_source_producer_paths(repository_root: Path) -> set[str]:
    paths: set[str] = set()
    for row in read_csv_rows(repository_root / EXTERNAL_SOURCE_CONTRACT_PATH):
        paths.update(
            normalize_repository_path(path)
            for path in split_list(row.get("producer", ""))
        )
    return {path for path in paths if path}


def requires_strict_runtime_validation(
    path: str,
    *,
    repository_root: Path = ROOT,
) -> bool:
    normalized = normalize_repository_path(path)
    return (
        normalized in STRICT_EXACT_PATHS
        or any(normalized.startswith(prefix) for prefix in STRICT_PATH_PREFIXES)
        or normalized in external_source_surface_paths(repository_root)
    )


def is_registered_source_identity_gate_self_update(
    base_ref: str,
    changed_paths: set[str],
    strict_surface_changes: set[str],
    *,
    repository_root: Path,
) -> bool:
    if changed_paths != SOURCE_IDENTITY_GATE_SELF_UPDATE_PATHS:
        return False
    if strict_surface_changes != {PR_SAFE_HELPER_PATH}:
        return False
    base_helper = git_blob_at_ref(
        base_ref,
        PR_SAFE_HELPER_PATH,
        repository_root=repository_root,
    )
    if base_helper is None:
        return False
    if (
        hashlib.sha256(base_helper).hexdigest()
        != SOURCE_IDENTITY_GATE_SELF_UPDATE_BASE_HELPER_SHA256
    ):
        return False
    try:
        current_helper = (repository_root / PR_SAFE_HELPER_PATH).read_text(
            encoding="utf-8"
        )
        current_tests = (repository_root / SOURCE_IDENTITY_GATE_TEST_PATH).read_text(
            encoding="utf-8"
        )
    except (OSError, UnicodeError):
        return False
    return bool(
        SOURCE_IDENTITY_GATE_SELF_UPDATE_ID in current_helper
        and SOURCE_IDENTITY_GATE_SELF_UPDATE_TEST_MARKER in current_tests
    )


def is_additive_research_gate_self_update(
    base_ref: str,
    changed_paths: set[str],
    strict_surface_changes: set[str],
    *,
    repository_root: Path,
) -> bool:
    if changed_paths != ADDITIVE_RESEARCH_GATE_SELF_UPDATE_PATHS:
        return False
    if strict_surface_changes != {PR_SAFE_HELPER_PATH}:
        return False
    base_authorizations = git_blob_at_ref(
        base_ref,
        ADDITIVE_RESEARCH_GATE_AUTHORIZATIONS_PATH,
        repository_root=repository_root,
    )
    base_helper = git_blob_at_ref(
        base_ref,
        PR_SAFE_HELPER_PATH,
        repository_root=repository_root,
    )
    if base_authorizations is None or base_helper is None:
        return False
    authorization_rows, authorization_errors = parse_csv_payload(
        base_authorizations,
        source=f"{base_ref}:{ADDITIVE_RESEARCH_GATE_AUTHORIZATIONS_PATH}",
    )
    if authorization_errors or not authorization_rows:
        return False
    if tuple(authorization_rows[0]) != ADDITIVE_RESEARCH_GATE_AUTHORIZATION_COLUMNS:
        return False
    matching = [
        row
        for row in authorization_rows
        if row.get("migration_id", "").strip()
        == ADDITIVE_RESEARCH_GATE_SELF_UPDATE_ID
    ]
    if len(matching) != 1:
        return False
    authorization = matching[0]
    try:
        base_helper_text = base_helper.decode("utf-8")
        current_helper = (repository_root / PR_SAFE_HELPER_PATH).read_bytes()
        current_tests = (repository_root / SOURCE_IDENTITY_GATE_TEST_PATH).read_bytes()
        current_authorizations = (
            repository_root / ADDITIVE_RESEARCH_GATE_AUTHORIZATIONS_PATH
        ).read_bytes()
    except (OSError, UnicodeError):
        return False
    sha_fields = (
        "base_helper_sha256",
        "current_helper_sha256",
        "current_test_sha256",
    )
    if any(
        not re.fullmatch(r"[0-9a-f]{64}", authorization.get(field, "").strip())
        for field in sha_fields
    ):
        return False
    return bool(
        authorization.get("status", "").strip() == "preauthorized"
        and bool(authorization.get("approval_reference", "").strip())
        and set(split_list(authorization.get("changed_paths", "")))
        == set(ADDITIVE_RESEARCH_GATE_SELF_UPDATE_PATHS)
        and canonical_repository_bytes(current_authorizations)
        == canonical_repository_bytes(base_authorizations)
        and canonical_sha256(base_helper)
        == authorization.get("base_helper_sha256", "").strip()
        and canonical_sha256(current_helper)
        == authorization.get("current_helper_sha256", "").strip()
        and canonical_sha256(current_tests)
        == authorization.get("current_test_sha256", "").strip()
        and ADDITIVE_RESEARCH_GATE_SELF_UPDATE_ID.encode("utf-8") in current_helper
        and ADDITIVE_RESEARCH_GATE_SELF_UPDATE_ID not in base_helper_text
    )


def validate_registered_source_identity_migration(
    base_ref: str,
    changed_paths: set[str],
    strict_surface_changes: set[str],
    *,
    repository_root: Path,
) -> tuple[bool, list[str]]:
    registered_producers = external_source_producer_paths(repository_root)
    changed_producers = strict_surface_changes & registered_producers
    if not changed_producers:
        return False, []
    allowed_strict_surfaces = set(changed_producers) | {PRODUCTION_INVENTORY_PATH}
    if strict_surface_changes != allowed_strict_surfaces:
        return False, []

    errors: list[str] = []
    required_evidence_paths = {
        CANONICAL_LINEAGE_MIGRATIONS_PATH,
        CANONICAL_LINEAGE_REGISTRY_PATH,
        PRODUCTION_INVENTORY_PATH,
    }
    missing_evidence_paths = sorted(required_evidence_paths - changed_paths)
    if missing_evidence_paths:
        errors.append(
            "registered source-identity migration is missing changed evidence path(s): "
            + ", ".join(missing_evidence_paths)
        )

    added_migrations, migration_errors = append_only_csv_rows(
        base_ref,
        CANONICAL_LINEAGE_MIGRATIONS_PATH,
        repository_root=repository_root,
    )
    added_registry_rows, registry_errors = append_only_csv_rows(
        base_ref,
        CANONICAL_LINEAGE_REGISTRY_PATH,
        repository_root=repository_root,
    )
    added_inventory_rows, inventory_errors = additive_csv_rows(
        base_ref,
        PRODUCTION_INVENTORY_PATH,
        key="path",
        repository_root=repository_root,
    )
    errors.extend(migration_errors)
    errors.extend(registry_errors)
    errors.extend(inventory_errors)
    if errors:
        return True, errors
    if not added_migrations:
        errors.append("registered source-identity migration adds no migration ledger row")
    if not added_registry_rows:
        errors.append("registered source-identity migration adds no lineage registry row")
    if not added_inventory_rows:
        errors.append("registered source-identity migration adds no test inventory row")

    migrations_by_id: dict[str, dict[str, str]] = {}
    migration_lineage_ids: set[str] = set()
    for migration in added_migrations:
        migration_id = migration.get("migration_id", "").strip()
        changed_ids = split_list(migration.get("changed_lineage_ids", ""))
        previous_hashes = split_list(
            migration.get("previous_contract_sha256s", "")
        )
        new_hashes = split_list(migration.get("new_contract_sha256s", ""))
        if not migration_id or migration_id in migrations_by_id:
            errors.append(
                "registered source-identity migration has blank or duplicate migration_id"
            )
            continue
        migrations_by_id[migration_id] = migration
        if migration.get("migration_status", "").strip() != SOURCE_IDENTITY_MIGRATION_STATUS:
            errors.append(
                f"registered source-identity migration is not validated: {migration_id}"
            )
        if not migration.get("user_approval_reference", "").strip():
            errors.append(
                f"registered source-identity migration lacks approval reference: {migration_id}"
            )
        if not changed_ids or not (
            len(changed_ids) == len(previous_hashes) == len(new_hashes)
        ):
            errors.append(
                f"registered source-identity migration SHA lists do not align: {migration_id}"
            )
            continue
        if any(value != "NEW" for value in previous_hashes):
            errors.append(
                f"registered source-identity migration must add new lineage rows only: {migration_id}"
            )
        if any(not re.fullmatch(r"[0-9a-f]{64}", value) for value in new_hashes):
            errors.append(
                f"registered source-identity migration has invalid contract SHA: {migration_id}"
            )
        repeated_ids = migration_lineage_ids & set(changed_ids)
        if repeated_ids:
            errors.append(
                "registered source-identity migration repeats lineage id(s): "
                + ", ".join(sorted(repeated_ids))
            )
        migration_lineage_ids.update(changed_ids)

    registry_by_id: dict[str, dict[str, str]] = {}
    identity_producers: set[str] = set()
    for row in added_registry_rows:
        lineage_id = row.get("lineage_id", "").strip()
        if not lineage_id or lineage_id in registry_by_id:
            errors.append(
                "registered source-identity registry has blank or duplicate lineage_id"
            )
            continue
        registry_by_id[lineage_id] = row
        migration_id = row.get("last_migration_id", "").strip()
        migration = migrations_by_id.get(migration_id)
        if migration is None:
            errors.append(
                f"source-identity registry row lacks an added migration: {lineage_id}"
            )
            continue
        changed_ids = split_list(migration.get("changed_lineage_ids", ""))
        new_hashes = split_list(migration.get("new_contract_sha256s", ""))
        if lineage_id not in changed_ids:
            errors.append(
                f"source-identity registry row is absent from migration: {lineage_id}"
            )
            continue
        expected_sha = new_hashes[changed_ids.index(lineage_id)]
        if row.get("contract_sha256", "").strip() != expected_sha:
            errors.append(
                f"source-identity registry contract SHA mismatch: {lineage_id}"
            )
        if (
            row.get("approval_reference", "").strip()
            != migration.get("user_approval_reference", "").strip()
        ):
            errors.append(
                f"source-identity registry approval mismatch: {lineage_id}"
            )
        producer = normalize_repository_path(row.get("producer", ""))
        if producer in changed_producers:
            if row.get("artifact_role", "").strip() != SOURCE_IDENTITY_ARTIFACT_ROLE:
                errors.append(
                    f"changed producer lineage is not source-identity evidence: {lineage_id}"
                )
            required_values = {
                "identity_columns": row.get("identity_columns", "").strip(),
                "collision_policy": row.get("collision_policy", "").strip(),
                "parity_policy": row.get("parity_policy", "").strip(),
                "forbidden_use": row.get("forbidden_use", "").strip(),
            }
            missing_values = sorted(
                key for key, value in required_values.items() if not value
            )
            allowed_use = row.get("allowed_use", "").strip().lower()
            model_family = row.get("model_family", "").strip().lower()
            if missing_values or "identity" not in allowed_use or "source_identity" not in model_family:
                errors.append(
                    f"changed producer source-identity contract is incomplete: {lineage_id}"
                )
            identity_producers.add(producer)

    if set(registry_by_id) != migration_lineage_ids:
        errors.append(
            "registered source-identity migration and appended registry lineage sets differ"
        )

    added_test_paths: list[str] = []
    for row in added_inventory_rows:
        path = normalize_repository_path(row.get("path", ""))
        if (
            not path.startswith("tests/")
            or "source_identity" not in Path(path).name
            or "test_python" not in {value.strip() for value in row.values()}
        ):
            errors.append(
                "registered source-identity inventory additions must be source-identity tests"
            )
            continue
        if path not in changed_paths or not (repository_root / path).is_file():
            errors.append(
                f"registered source-identity test is not a changed current file: {path}"
            )
        existed_at_base = git_path_exists_at_ref(
            base_ref,
            path,
            repository_root=repository_root,
        )
        if existed_at_base is not False:
            errors.append(
                f"registered source-identity test must be newly added relative to base: {path}"
            )
        added_test_paths.append(path)

    for producer in sorted(changed_producers):
        if producer not in identity_producers:
            errors.append(
                f"changed external producer lacks canonical source-identity registry evidence: {producer}"
            )
        covering_migrations = [
            migration
            for migration in added_migrations
            if producer in split_list(migration.get("affected_consumers", ""))
        ]
        if not covering_migrations:
            errors.append(
                f"changed external producer lacks migration consumer evidence: {producer}"
            )
            continue
        for migration in covering_migrations:
            commands = migration.get("validation_commands", "")
            if CANONICAL_LINEAGE_VALIDATOR_PATH not in commands:
                errors.append(
                    f"source-identity migration omits canonical lineage validator: {producer}"
                )
            if not any(test_path in commands for test_path in added_test_paths):
                errors.append(
                    f"source-identity migration omits independent source-identity test: {producer}"
                )

    try:
        workflow_text = (repository_root / PR_VALIDATION_WORKFLOW_PATH).read_text(
            encoding="utf-8"
        )
    except (OSError, UnicodeError) as exc:
        errors.append(f"cannot read PR validation workflow for migration evidence: {exc}")
    else:
        if CANONICAL_LINEAGE_PR_COMMAND not in workflow_text:
            errors.append(
                "PR workflow omits append-only canonical lineage validation with base ref"
            )
    return True, errors


def expected_historical_replay_external_errors(
    *,
    repository_root: Path = ROOT,
) -> tuple[list[str], list[str]]:
    contract_rows = read_csv_rows(repository_root / EXTERNAL_SOURCE_CONTRACT_PATH)
    freshness_rows = read_csv_rows(repository_root / FRESHNESS_RELATIVE_PATH)
    if len(freshness_rows) != 1:
        return [], [
            "PR-safe advanced-integrity freshness input must contain exactly one row; "
            f"observed={len(freshness_rows)}"
        ]

    rows_by_source = {
        row.get("source_id", "").strip(): row
        for row in contract_rows
        if row.get("source_id", "").strip()
    }
    freshness = freshness_rows[0]
    main_date = freshness.get("main_price_date", "").strip()
    expected: list[str] = []
    contract_errors: list[str] = []

    for source_id, (expected_date_column, expected_readiness_column) in (
        EXPECTED_REPLAY_SOURCE_COLUMNS.items()
    ):
        row = rows_by_source.get(source_id)
        if row is None:
            contract_errors.append(
                f"historical-replay external source contract is missing {source_id}"
            )
            continue
        observed_date_column = row.get("freshness_date_column", "").strip()
        observed_readiness_column = row.get("readiness_column", "").strip()
        if observed_date_column != expected_date_column:
            contract_errors.append(
                f"historical-replay external source {source_id} freshness column drift: "
                f"expected={expected_date_column!r} observed={observed_date_column!r}"
            )
        if observed_readiness_column != expected_readiness_column:
            contract_errors.append(
                f"historical-replay external source {source_id} readiness column drift: "
                f"expected={expected_readiness_column!r} "
                f"observed={observed_readiness_column!r}"
            )
        if row.get("require_matches_main_price_date", "").strip() != "True":
            contract_errors.append(
                f"historical-replay external source {source_id} must require main-date parity"
            )
        if contract_errors:
            continue

        observed_date = freshness.get(expected_date_column, "").strip()
        if observed_date != main_date:
            if source_id not in ALLOWED_STALE_DATE_SOURCES:
                contract_errors.append(
                    f"historical-replay external source {source_id} cannot inherit a "
                    f"stale {expected_date_column}: observed={observed_date!r} "
                    f"main_price_date={main_date!r}"
                )
            elif not re.fullmatch(r"20\d{6}", observed_date) or observed_date >= main_date:
                contract_errors.append(
                    f"historical-replay external source {source_id} stale date must be a "
                    f"prior YYYYMMDD value: observed={observed_date!r} "
                    f"main_price_date={main_date!r}"
                )
            else:
                expected.append(
                    f"external source {source_id} date "
                    f"{expected_date_column}={observed_date} does not match "
                    f"main_price_date={main_date}"
                )

        readiness = freshness.get(expected_readiness_column, "").strip()
        if readiness != "True":
            expected.append(
                f"external source {source_id} readiness "
                f"{expected_readiness_column} is not True"
            )

    if not expected and not contract_errors:
        contract_errors.append(
            "historical-replay PR-safe path requires the strict external-source gate "
            "to report at least one inherited not-ready error"
        )
    return expected, contract_errors


def is_initial_pr_safe_gate_bootstrap(
    base_ref: str,
    strict_surface_changes: set[str],
    *,
    repository_root: Path,
) -> bool:
    if strict_surface_changes != PR_SAFE_BOOTSTRAP_SURFACES:
        return False
    helper_existed_at_base = git_path_exists_at_ref(
        base_ref,
        PR_SAFE_HELPER_PATH,
        repository_root=repository_root,
    )
    if helper_existed_at_base is not False:
        return False

    base_workflow = git_blob_at_ref(
        base_ref,
        PR_VALIDATION_WORKFLOW_PATH,
        repository_root=repository_root,
    )
    base_inventory = git_blob_at_ref(
        base_ref,
        PRODUCTION_INVENTORY_PATH,
        repository_root=repository_root,
    )
    try:
        current_helper = (repository_root / PR_SAFE_HELPER_PATH).read_bytes()
        current_workflow = (repository_root / PR_VALIDATION_WORKFLOW_PATH).read_bytes()
        current_inventory = (repository_root / PRODUCTION_INVENTORY_PATH).read_bytes()
    except OSError:
        return False
    if (
        not current_helper
        or base_workflow is None
        or base_inventory is None
    ):
        return False

    command = PR_SAFE_COMMAND.encode("utf-8")
    deselect = STRICT_RUNTIME_TEST_DESELECT.encode("utf-8")
    helper_path = PR_SAFE_HELPER_PATH.encode("utf-8")
    return bool(
        command not in base_workflow
        and command in current_workflow
        and deselect not in base_workflow
        and deselect in current_workflow
        and helper_path not in base_inventory
        and helper_path in current_inventory
    )


def validate_pr_safe_advanced_integrity_contract(
    base_ref: str,
    *,
    repository_root: Path = ROOT,
) -> list[str]:
    changed_paths, git_errors = changed_paths_from_base(
        base_ref,
        repository_root=repository_root,
    )
    if git_errors:
        return git_errors

    static_errors = strict_validator.validate(include_external_sources=False)
    if static_errors:
        return [
            "PR-safe advanced-integrity validation cannot bypass static contract failures",
            *static_errors,
        ]

    external_errors = strict_validator.validate_external_source_contract()
    if not external_errors:
        return []

    strict_surface_changes = {
        path
        for path in changed_paths
        if requires_strict_runtime_validation(
            path,
            repository_root=repository_root,
        )
    }
    if is_initial_pr_safe_gate_bootstrap(
        base_ref,
        strict_surface_changes,
        repository_root=repository_root,
    ):
        strict_surface_changes = set()
    elif is_registered_source_identity_gate_self_update(
        base_ref,
        changed_paths,
        strict_surface_changes,
        repository_root=repository_root,
    ):
        strict_surface_changes = set()
    elif is_additive_research_gate_self_update(
        base_ref,
        changed_paths,
        strict_surface_changes,
        repository_root=repository_root,
    ):
        strict_surface_changes = set()
    elif strict_surface_changes:
        is_additive_research, additive_research_errors = (
            validate_additive_research_validation_registration(
                base_ref,
                changed_paths,
                strict_surface_changes,
                repository_root=repository_root,
            )
        )
        if is_additive_research:
            if additive_research_errors:
                return [
                    "additive research-only validation registration is incomplete; "
                    "full runtime repo advanced-integrity validation remains required",
                    *additive_research_errors,
                    *external_errors,
                ]
            strict_surface_changes = set()
        else:
            is_source_identity_migration, migration_errors = (
                validate_registered_source_identity_migration(
                    base_ref,
                    changed_paths,
                    strict_surface_changes,
                    repository_root=repository_root,
                )
            )
            if is_source_identity_migration:
                if migration_errors:
                    return [
                        "registered source-identity migration evidence is incomplete; "
                        "full runtime repo advanced-integrity validation remains required",
                        *migration_errors,
                        *external_errors,
                    ]
                strict_surface_changes = set()
    if strict_surface_changes:
        return [
            "full runtime repo advanced-integrity validation is required because the PR "
            "changes protected external-source/readiness surface(s): "
            + ", ".join(sorted(strict_surface_changes)),
            *external_errors,
        ]

    marker_errors = validate_historical_replay_not_ready_marker(
        repository_root / FRESHNESS_RELATIVE_PATH
    )
    base_errors = validate_freshness_is_inherited_from_base(
        base_ref,
        repository_root=repository_root,
    )
    expected_errors, expected_contract_errors = (
        expected_historical_replay_external_errors(repository_root=repository_root)
    )
    if marker_errors or base_errors or expected_contract_errors:
        return [*marker_errors, *base_errors, *expected_contract_errors]
    if sorted(external_errors) != sorted(expected_errors):
        return [
            "PR-safe advanced-integrity validation may inherit only the exact external "
            "source errors caused by the legal historical-replay not-ready state",
            *external_errors,
        ]
    return []


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Validate repository advanced integrity in PR context without treating an "
            "unchanged legal historical-replay not-ready base as a PR regression"
        )
    )
    parser.add_argument("--base-ref", required=True)
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    errors = validate_pr_safe_advanced_integrity_contract(args.base_ref)
    if errors:
        print("ERROR: PR-safe repo advanced-integrity validation failed")
        for error in errors:
            print(f"ERROR: {error}")
        return 1
    print(
        "PR-safe repo advanced-integrity validation passed; "
        f"base_ref={args.base_ref}; strict production validator remains fail closed"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
