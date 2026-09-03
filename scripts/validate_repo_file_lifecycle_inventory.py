from __future__ import annotations

import ast
import csv
import re
import subprocess
from dataclasses import dataclass
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LIFECYCLE_INVENTORY = ROOT / "config" / "repo_file_lifecycle_inventory.csv"
PRODUCTION_INVENTORY = ROOT / "config" / "repo_production_inventory.csv"
LINEAGE_CSV = ROOT / "config" / "report_artifact_lineage.csv"


REQUIRED_COLUMNS = {
    "path",
    "type",
    "owner",
    "status",
    "called_by_workflow",
    "imported_by",
    "tested_by",
    "documented_by",
    "writes_artifact",
    "reads_artifact",
    "keep_reason",
    "delete_reason",
    "removal_risk",
}

VALID_TYPES = {
    "python",
    "test_python",
    "workflow",
    "executable_script",
    "guidance_doc",
    "generated_guidance",
}

VALID_STATUSES = {
    "active",
    "manual_diagnostic",
    "generated_artifact",
    "historical_artifact",
    "deprecated",
    "delete_candidate",
}

VALID_REMOVAL_RISK = {"none", "low", "medium", "high"}

NON_PYTHON_EXECUTABLE_SUFFIXES = {".bat", ".cmd", ".gs", ".js", ".mjs", ".pl", ".ps1", ".rb", ".sh", ".ts", ".tsx"}
PYTHON_INVOKE_RE = re.compile(
    r"\bpython(?:3)?\s+(?:-[A-Za-z]+\s+)*"
    r"([A-Za-z0-9_./\\-]+\.py)"
)
SHELL_INVOKE_RE = re.compile(r"\b(?:bash|sh)\s+([A-Za-z0-9_./\\-]+\.(?:sh|cmd|bat|ps1))")
PYTHON_PATH_REFERENCE_RE = re.compile(
    r"(?<![A-Za-z0-9_./\\-])"
    r"((?:\.[/\\])?[A-Za-z0-9_.-]+(?:[/\\][A-Za-z0-9_.-]+)*\.py)"
    r"(?![A-Za-z0-9_.-])"
)
PYTHON_MODULE_REFERENCE_RE = re.compile(
    r"(?<![A-Za-z0-9_])([A-Za-z_][A-Za-z0-9_]*(?:\.[A-Za-z_][A-Za-z0-9_]*)*)"
    r"(?![A-Za-z0-9_])"
)
NON_MODULE_FILE_SUFFIXES = {
    "bat",
    "cmd",
    "csv",
    "gs",
    "html",
    "json",
    "md",
    "mjs",
    "pdf",
    "pl",
    "ps1",
    "py",
    "rb",
    "sh",
    "ts",
    "tsx",
    "txt",
    "yaml",
    "yml",
}
DATE_STAMPED_DAILY_README_RE = re.compile(r"(?:^|/)READ_ME_FIRST_DAILY_REPORT_\d{8}\.txt$")

ACTIVE_GUIDANCE_ROOT_FILES = {"AGENTS.md", "README.md"}
ACTIVE_GUIDANCE_PREFIXES = (
    "rules/",
    "docs/specs/",
    "docs/thread_templates/",
)
ACTIVE_GUIDANCE_DOCS_ROOT_SUFFIXES = {".md", ".txt"}
GENERATED_GUIDANCE_PREFIXES = (
    "docs/latest/",
    "output/latest/",
)
HISTORICAL_GUIDANCE_PREFIXES = (
    "docs/history/",
    "output/history/",
)

FORBIDDEN_ACTIVE_GUIDANCE_PATTERNS = {
    r"\bpython(?:3)?\s+generate_repo_chatgpt_side_reports\.py\b": "retired helper report generator",
    r"\bpython(?:3)?\s+scripts/generate_daily_market_pdf\.py\b": "retired daily market PDF generator",
    r"\bpython(?:3)?\s+scripts/validate_daily_market_report\.py\b": "retired daily market PDF validator",
    r"daily_market_curated_report_latest\.pdf": "retired daily market curated PDF artifact",
    r"daily_market_full_table_report_latest\.pdf": "retired daily market full-table PDF artifact",
    r"chip_flow_positive_streak": "removed chip-flow positive-streak surface",
}

CANONICAL_DAILY_REPORT_ENTRYPOINT = "scripts/run_chatgpt_daily_report_entrypoint.py"
CANONICAL_CHATGPT_PDF_RENDERER = "scripts/generate_chatgpt_side_daily_reports.py"
TDCC_STEALTH_PIT_AUDIT_ARTIFACT = (
    "output/research/tdcc_stealth_accumulation/"
    "tdcc_stealth_accumulation_pit_replay_availability_audit_v1.csv"
)
TDCC_STEALTH_PIT_AUDIT_SOURCES = {
    "output/history/daily_model_snapshots/daily_published_model_snapshot_manifest.csv",
    "output/history/daily_model_snapshots/all_candidates_*.csv",
    "output/history/daily_model_snapshots/daily_candidate_model_signals_for_report_*.csv",
    "output/history/daily_candidate_models/daily_candidate_model_signal_log.csv",
    "output/history/tdcc/tdcc_holder_ratio_*.csv",
    "output/history/tdcc/tdcc_latest_ratio_raw_*.csv",
    "output/latest/tdcc_dataset_manifest_latest.json",
    "output/history/tdcc/tdcc_dataset_manifest_*.json",
    "output/history/tdcc_signals/tdcc_signal_snapshot.csv",
    "data/tdcc_stock_history_raw/*.csv",
    "data/tdcc_stock_history/*.csv",
    "data/daily_price/[0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9].csv",
    "data/stock_price_history/*.csv",
    "config/stock_model_contract_registry.csv",
    "config/daily_model_semantic_ownership.csv",
    "config/daily_model_shared_semantic_registry.csv",
}

EXPLICIT_WORKFLOW_LIFECYCLE_REFERENCES = {
    ".github/workflows/revenue_unreacted_range_post_launch_monitoring.yml": {
        "tested_by": {
            "tests/test_revenue_unreacted_range_post_launch_workflows.py"
        },
        "reads_artifact": {
            "output/latest/model_operation_readiness_latest.csv"
        },
    },
    "scripts/validate_tdcc_stealth_accumulation_pit_replay_availability.py": {
        "reads_artifact": TDCC_STEALTH_PIT_AUDIT_SOURCES
        | {TDCC_STEALTH_PIT_AUDIT_ARTIFACT},
    },
}


@dataclass(frozen=True)
class LifecycleRow:
    path: str
    type: str
    owner: str
    status: str
    called_by_workflow: tuple[str, ...]
    imported_by: tuple[str, ...]
    tested_by: tuple[str, ...]
    documented_by: tuple[str, ...]
    writes_artifact: tuple[str, ...]
    reads_artifact: tuple[str, ...]
    keep_reason: str
    delete_reason: str
    removal_risk: str


@dataclass(frozen=True)
class ProductionRow:
    path: str
    kind: str
    owner: str
    status: str
    purpose: str


def rel(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def read_text(path: Path) -> str:
    if path.exists():
        return path.read_text(encoding="utf-8-sig", errors="replace")
    relative = rel(path)
    sparse_state = subprocess.run(
        ["git", "ls-files", "-t", "--", relative],
        cwd=ROOT,
        check=False,
        text=True,
        encoding="utf-8",
        errors="replace",
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    if sparse_state.returncode == 0 and any(
        line.startswith("S ") for line in sparse_state.stdout.splitlines()
    ):
        result = subprocess.run(
            ["git", "show", f"HEAD:{relative}"],
            cwd=ROOT,
            check=False,
            text=True,
            encoding="utf-8-sig",
            errors="replace",
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
        if result.returncode == 0:
            return result.stdout
    raise FileNotFoundError(path)


def git_ls_files(pattern: str) -> set[str]:
    result = subprocess.run(
        ["git", "ls-files", pattern],
        cwd=ROOT,
        check=True,
        text=True,
        encoding="utf-8",
        errors="replace",
        stdout=subprocess.PIPE,
    )
    return {line.strip().replace("\\", "/") for line in result.stdout.splitlines() if line.strip()}


def split_list(value: str) -> tuple[str, ...]:
    return tuple(part.strip().replace("\\", "/") for part in str(value or "").split(";") if part.strip())


def load_csv(path: Path) -> list[dict[str, str]]:
    if not path.exists():
        return []
    with path.open("r", encoding="utf-8-sig", newline="") as fh:
        return [{key: str(value or "") for key, value in row.items()} for row in csv.DictReader(fh)]


def load_production_inventory() -> dict[str, ProductionRow]:
    rows: dict[str, ProductionRow] = {}
    for row in load_csv(PRODUCTION_INVENTORY):
        path = row.get("path", "").strip().replace("\\", "/")
        if not path:
            continue
        rows[path] = ProductionRow(
            path=path,
            kind=row.get("kind", "").strip(),
            owner=row.get("owner", "").strip(),
            status=row.get("status", "").strip(),
            purpose=row.get("purpose", "").strip(),
        )
    return rows


def load_lifecycle_inventory(errors: list[str]) -> dict[str, LifecycleRow]:
    rows: dict[str, LifecycleRow] = {}
    if not LIFECYCLE_INVENTORY.exists():
        errors.append(f"missing lifecycle inventory: {rel(LIFECYCLE_INVENTORY)}")
        return rows

    with LIFECYCLE_INVENTORY.open("r", encoding="utf-8-sig", newline="") as fh:
        reader = csv.DictReader(fh)
        if not reader.fieldnames:
            errors.append(f"empty lifecycle inventory: {rel(LIFECYCLE_INVENTORY)}")
            return rows
        missing = REQUIRED_COLUMNS.difference(reader.fieldnames)
        if missing:
            errors.append(f"lifecycle inventory missing columns: {sorted(missing)}")
            return rows
        for line_no, row in enumerate(reader, start=2):
            path = row.get("path", "").strip().replace("\\", "/")
            if not path:
                errors.append(f"lifecycle inventory row {line_no} has empty path")
                continue
            if path in rows:
                errors.append(f"lifecycle inventory duplicates path: {path}")
                continue
            rows[path] = LifecycleRow(
                path=path,
                type=row.get("type", "").strip(),
                owner=row.get("owner", "").strip(),
                status=row.get("status", "").strip(),
                called_by_workflow=split_list(row.get("called_by_workflow", "")),
                imported_by=split_list(row.get("imported_by", "")),
                tested_by=split_list(row.get("tested_by", "")),
                documented_by=split_list(row.get("documented_by", "")),
                writes_artifact=split_list(row.get("writes_artifact", "")),
                reads_artifact=split_list(row.get("reads_artifact", "")),
                keep_reason=row.get("keep_reason", "").strip(),
                delete_reason=row.get("delete_reason", "").strip(),
                removal_risk=row.get("removal_risk", "").strip(),
            )
    return rows


def tracked_python_paths() -> set[str]:
    tracked = {
        path
        for path in git_ls_files("*.py")
        if path.startswith("scripts/") or "/" not in path
    }
    working_tree = {
        rel(path)
        for pattern in ("*.py", "scripts/**/*.py")
        for path in ROOT.glob(pattern)
        if "__pycache__" not in path.parts
    }
    return tracked | working_tree


def tracked_test_python_paths() -> set[str]:
    tracked = {path for path in git_ls_files("*.py") if path.startswith("tests/")}
    working_tree = {
        rel(path)
        for path in (ROOT / "tests").glob("**/*.py")
        if "__pycache__" not in path.parts
    }
    return tracked | working_tree


def tracked_workflow_paths() -> set[str]:
    tracked = {
        path
        for path in (git_ls_files(".github/workflows/*.yml") | git_ls_files(".github/workflows/*.yaml"))
    }
    working_tree = {
        rel(path)
        for pattern in (".github/workflows/*.yml", ".github/workflows/*.yaml")
        for path in ROOT.glob(pattern)
    }
    return tracked | working_tree


def tracked_executable_paths() -> set[str]:
    tracked = {
        path
        for path in git_ls_files("*")
        if Path(path).suffix in NON_PYTHON_EXECUTABLE_SUFFIXES
    }
    working_tree = {
        rel(path)
        for path in ROOT.glob("**/*")
        if path.is_file()
        and ".git" not in path.parts
        and "__pycache__" not in path.parts
        and path.suffix in NON_PYTHON_EXECUTABLE_SUFFIXES
    }
    return tracked | working_tree


def tracked_guidance_paths() -> set[str]:
    paths: set[str] = set()
    for path in git_ls_files("*"):
        suffix = Path(path).suffix.lower()
        if suffix not in {".md", ".txt"}:
            continue
        if path in ACTIVE_GUIDANCE_ROOT_FILES:
            paths.add(path)
            continue
        if path.startswith(ACTIVE_GUIDANCE_PREFIXES):
            paths.add(path)
            continue
        if path.startswith(GENERATED_GUIDANCE_PREFIXES):
            filename = Path(path).name
            if DATE_STAMPED_DAILY_README_RE.search(path):
                continue
            if filename.startswith(("READ_ME_FIRST_DAILY_REPORT", "CHATGPT_DAILY_REPORT", "chatgpt_daily_report_packet", "report_publish_check", "report_manifest")):
                paths.add(path)
            continue
        if path.startswith(HISTORICAL_GUIDANCE_PREFIXES):
            continue
        if path.startswith("docs/") and path.count("/") == 1 and suffix in ACTIVE_GUIDANCE_DOCS_ROOT_SUFFIXES:
            paths.add(path)
    return paths


def expected_lifecycle_paths() -> set[str]:
    return (
        tracked_python_paths()
        | tracked_test_python_paths()
        | tracked_workflow_paths()
        | tracked_executable_paths()
        | tracked_guidance_paths()
    )


def workflow_invocations() -> dict[str, set[str]]:
    refs: dict[str, set[str]] = {}
    for workflow in tracked_workflow_paths():
        text = read_text(ROOT / workflow)
        for pattern in (PYTHON_INVOKE_RE, SHELL_INVOKE_RE):
            for match in pattern.finditer(text):
                invoked = match.group(1).strip().strip("'\"").replace("\\", "/")
                if invoked.startswith("./"):
                    invoked = invoked[2:]
                refs.setdefault(invoked, set()).add(workflow)
    return refs


def module_name_for_path(path: str) -> str:
    p = Path(path)
    stem = p.stem
    if path.startswith("scripts/"):
        return f"scripts.{stem}"
    if path.startswith("tests/"):
        return f"tests.{stem}"
    return stem


def import_references(paths: set[str]) -> dict[str, set[str]]:
    module_to_path: dict[str, str] = {}
    for path in sorted(paths):
        if not path.endswith(".py"):
            continue
        module_to_path[module_name_for_path(path)] = path
        module_to_path[Path(path).stem] = path

    refs: dict[str, set[str]] = {}
    for source in sorted(path for path in paths if path.endswith(".py")):
        try:
            tree = ast.parse(read_text(ROOT / source), filename=source)
        except SyntaxError:
            continue
        imported_names: list[str] = []
        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                imported_names.extend(alias.name for alias in node.names)
            elif isinstance(node, ast.ImportFrom) and node.module and node.level == 0:
                imported_names.append(node.module)
        for name in imported_names:
            candidates = [name]
            parts = name.split(".")
            if parts:
                candidates.append(parts[0])
                if len(parts) >= 2:
                    candidates.append(".".join(parts[:2]))
            for candidate in candidates:
                target = module_to_path.get(candidate)
                if target and target != source:
                    refs.setdefault(target, set()).add(source)
                    break
    return refs


def documentation_references(paths: set[str]) -> dict[str, set[str]]:
    doc_paths = tracked_guidance_paths()
    refs: dict[str, set[str]] = {}
    for doc in doc_paths:
        text = read_text(ROOT / doc)
        for target in paths:
            if target in text:
                refs.setdefault(target, set()).add(doc)
    return refs


def test_reference_tokens(text: str) -> tuple[set[str], set[str]]:
    path_references = {
        match.group(1).replace("\\", "/").removeprefix("./")
        for match in PYTHON_PATH_REFERENCE_RE.finditer(text)
    }
    module_references = {
        reference
        for reference in PYTHON_MODULE_REFERENCE_RE.findall(text)
        if reference.rsplit(".", 1)[-1].lower() not in NON_MODULE_FILE_SUFFIXES
    }
    return path_references, module_references


def test_tokens_reference_target(
    path_references: set[str],
    module_references: set[str],
    target: str,
) -> bool:
    normalized_target = target.replace("\\", "/").removeprefix("./")
    module = module_name_for_path(normalized_target)
    stem = Path(normalized_target).stem
    filename = Path(normalized_target).name
    return bool(
        normalized_target in path_references
        or filename in path_references
        or stem in module_references
        or module in module_references
        or any(reference.startswith(module + ".") for reference in module_references)
        or any(stem in reference.split(".") for reference in module_references)
    )


def test_text_references_target(text: str, target: str) -> bool:
    path_references, module_references = test_reference_tokens(text)
    return test_tokens_reference_target(
        path_references,
        module_references,
        target,
    )


def test_references(paths: set[str]) -> dict[str, set[str]]:
    tests = tracked_test_python_paths()
    targets = sorted(
        target
        for target in paths
        if target.endswith(".py") and not target.startswith("tests/")
    )
    refs: dict[str, set[str]] = {}
    for test in tests:
        text = read_text(ROOT / test)
        path_references, module_references = test_reference_tokens(text)
        for target in targets:
            if test_tokens_reference_target(
                path_references,
                module_references,
                target,
            ):
                refs.setdefault(target, set()).add(test)
    return refs


def lineage_artifacts() -> tuple[dict[str, set[str]], dict[str, set[str]]]:
    writes: dict[str, set[str]] = {}
    reads: dict[str, set[str]] = {}
    for row in load_csv(LINEAGE_CSV):
        artifact = row.get("artifact_path", "").strip()
        for producer in split_list(row.get("producer", "")):
            if producer.endswith(".py"):
                writes.setdefault(producer, set()).add(artifact)
        for source in split_list(row.get("source_artifacts", "")):
            if source:
                for producer in split_list(row.get("producer", "")):
                    if producer.endswith(".py"):
                        reads.setdefault(producer, set()).add(source)
    return writes, reads


def validate_coverage(lifecycle: dict[str, LifecycleRow], production: dict[str, ProductionRow]) -> list[str]:
    errors: list[str] = []
    expected = expected_lifecycle_paths()
    actual = set(lifecycle)
    for path in sorted(expected - actual):
        errors.append(f"lifecycle inventory missing tracked executable/guidance path: {path}")
    for path in sorted(actual - expected):
        errors.append(f"lifecycle inventory lists untracked or out-of-scope path: {path}")
    for path in sorted(production):
        if path not in lifecycle:
            errors.append(f"production inventory path missing lifecycle row: {path}")
    return errors


def validate_rows(lifecycle: dict[str, LifecycleRow], production: dict[str, ProductionRow]) -> list[str]:
    errors: list[str] = []
    for row in lifecycle.values():
        if DATE_STAMPED_DAILY_README_RE.search(row.path):
            errors.append(
                f"{row.path} must not be listed in lifecycle inventory; "
                "date-stamped daily README aliases are volatile and validated by PDF inventory"
            )
        for column in [
            "called_by_workflow",
            "imported_by",
            "tested_by",
            "documented_by",
            "writes_artifact",
            "reads_artifact",
        ]:
            for ref in getattr(row, column):
                if DATE_STAMPED_DAILY_README_RE.search(ref):
                    errors.append(
                        f"{row.path} lifecycle {column} must not reference date-stamped daily README alias: {ref}"
                    )
        if row.type not in VALID_TYPES:
            errors.append(f"{row.path} has invalid lifecycle type: {row.type}")
        if row.status not in VALID_STATUSES:
            errors.append(f"{row.path} has invalid lifecycle status: {row.status}")
        if row.removal_risk not in VALID_REMOVAL_RISK:
            errors.append(f"{row.path} has invalid removal_risk: {row.removal_risk}")
        if not row.owner:
            errors.append(f"{row.path} has empty owner")
        if row.path in production:
            prod = production[row.path]
            if row.owner != prod.owner:
                errors.append(f"{row.path} owner differs from production inventory: {row.owner} != {prod.owner}")
            if row.type != prod.kind:
                errors.append(f"{row.path} type differs from production inventory: {row.type} != {prod.kind}")
        if row.status in {"active", "manual_diagnostic", "generated_artifact", "historical_artifact"} and not row.keep_reason:
            errors.append(f"{row.path} is kept but has empty keep_reason")
        if row.status in {"deprecated", "delete_candidate"}:
            if not row.delete_reason:
                errors.append(f"{row.path} is {row.status} but has empty delete_reason")
            if row.called_by_workflow or row.imported_by:
                errors.append(f"{row.path} is {row.status} but still has runtime references")
        if row.status == "delete_candidate" and row.removal_risk == "none":
            errors.append(f"{row.path} delete_candidate must declare removal_risk")
        if row.type == "workflow" and row.status not in {"active", "manual_diagnostic"}:
            errors.append(f"{row.path} workflow cannot be {row.status}")
        if row.type == "generated_guidance" and row.status != "generated_artifact":
            errors.append(f"{row.path} generated guidance must use generated_artifact status")
    return errors


def validate_no_pending_deletions(lifecycle: dict[str, LifecycleRow]) -> list[str]:
    errors: list[str] = []
    pending = sorted(
        row.path
        for row in lifecycle.values()
        if row.status in {"deprecated", "delete_candidate"}
    )
    if pending:
        errors.append(
            "main lifecycle inventory must not retain deprecated/delete_candidate files; "
            f"remove them or reclassify with evidence: {pending}"
        )
    return errors


def validate_reference_columns(lifecycle: dict[str, LifecycleRow]) -> list[str]:
    errors: list[str] = []
    paths = set(lifecycle)
    workflow_refs = workflow_invocations()
    import_refs = import_references(paths)
    doc_refs = documentation_references(paths)
    test_refs = test_references(paths)
    writes, reads = lineage_artifacts()

    for path, row in lifecycle.items():
        expected_workflows = sorted(workflow_refs.get(path, set()))
        expected_imports = sorted(import_refs.get(path, set()))
        expected_docs = sorted(doc_refs.get(path, set()))
        explicit_workflow_refs = EXPLICIT_WORKFLOW_LIFECYCLE_REFERENCES.get(path, {})
        expected_tests = sorted(
            test_refs.get(path, set())
            | set(explicit_workflow_refs.get("tested_by", set()))
        )
        expected_writes = sorted(writes.get(path, set()))
        expected_reads = sorted(
            reads.get(path, set())
            | set(explicit_workflow_refs.get("reads_artifact", set()))
        )
        comparisons = [
            ("called_by_workflow", expected_workflows, list(row.called_by_workflow)),
            ("imported_by", expected_imports, list(row.imported_by)),
            ("documented_by", expected_docs, list(row.documented_by)),
            ("tested_by", expected_tests, list(row.tested_by)),
            ("writes_artifact", expected_writes, list(row.writes_artifact)),
            ("reads_artifact", expected_reads, list(row.reads_artifact)),
        ]
        for column, expected, actual in comparisons:
            if sorted(actual) != expected:
                errors.append(f"{path} lifecycle {column} out of date: expected {expected}, got {sorted(actual)}")

    return errors


def validate_guidance_text(lifecycle: dict[str, LifecycleRow]) -> list[str]:
    errors: list[str] = []
    for path, row in lifecycle.items():
        if row.type not in {"guidance_doc", "generated_guidance"}:
            continue
        text = read_text(ROOT / path)
        for pattern, label in FORBIDDEN_ACTIVE_GUIDANCE_PATTERNS.items():
            if row.status != "historical_artifact" and re.search(pattern, text):
                errors.append(f"{path} still references {label}: {pattern}")
        if path in {"AGENTS.md", "README.md"} or path.startswith(("rules/", "docs/thread_templates/")):
            if CANONICAL_DAILY_REPORT_ENTRYPOINT in text and CANONICAL_CHATGPT_PDF_RENDERER in text:
                continue
            if "daily report" in text.lower() or "每日" in text:
                if CANONICAL_DAILY_REPORT_ENTRYPOINT not in text:
                    errors.append(f"{path} discusses daily reports but does not cite canonical entrypoint")
    return errors


def validate() -> list[str]:
    errors: list[str] = []
    production = load_production_inventory()
    lifecycle = load_lifecycle_inventory(errors)
    if not lifecycle:
        return errors
    errors.extend(validate_coverage(lifecycle, production))
    errors.extend(validate_rows(lifecycle, production))
    errors.extend(validate_no_pending_deletions(lifecycle))
    errors.extend(validate_reference_columns(lifecycle))
    errors.extend(validate_guidance_text(lifecycle))
    return errors


def main() -> int:
    errors = validate()
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1
    rows = load_lifecycle_inventory([])
    status_counts: dict[str, int] = {}
    for row in rows.values():
        status_counts[row.status] = status_counts.get(row.status, 0) + 1
    print("repo file lifecycle inventory validation passed")
    print(f"validated_rows={len(rows)}")
    for status in sorted(status_counts):
        print(f"status_{status}={status_counts[status]}")
    print(f"inventory={rel(LIFECYCLE_INVENTORY)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
