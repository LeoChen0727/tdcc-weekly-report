from __future__ import annotations

import csv
import re
import subprocess
from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
INVENTORY = ROOT / "config" / "repo_production_inventory.csv"
DAILY_WORKFLOW = ".github/workflows/daily_full_pipeline.yml"

REQUIRED_COLUMNS = {
    "path",
    "kind",
    "owner",
    "status",
    "purpose",
    "allowed_workflows",
    "allowed_stage_patterns",
}

VALID_KINDS = {"python", "test_python", "workflow", "executable_script"}
VALID_STATUSES = {"active", "manual_diagnostic", "legacy_deprecated"}

VALID_OWNERS = {
    "daily_production",
    "research_backtest",
    "tdcc_weekly",
    "individual_stock",
    "catalyst_event",
    "market_risk",
    "warrant",
    "official_price_data",
    "current_holdings",
    "diagnostics",
    "repo_infrastructure",
}

WORKFLOW_ALLOWED_OWNERS = {
    ".github/workflows/current_holdings_pattern.yml": {"current_holdings", "repo_infrastructure"},
    ".github/workflows/daily_full_pipeline.yml": {
        "daily_production",
        "official_price_data",
        "warrant",
        "catalyst_event",
        "market_risk",
        "repo_infrastructure",
    },
    ".github/workflows/daily_model_maintenance_pr_validation.yml": {
        "daily_production",
        "research_backtest",
        "repo_infrastructure",
    },
    ".github/workflows/debug_tpex_fetch.yml": {"diagnostics", "official_price_data", "repo_infrastructure"},
    ".github/workflows/diagnose_stock_selection.yml": {
        "diagnostics",
        "daily_production",
        "repo_infrastructure",
    },
    ".github/workflows/event_catalyst_update.yml": {
        "catalyst_event",
        "daily_production",
        "repo_infrastructure",
    },
    ".github/workflows/individual_stock_data_refresh.yml": {
        "individual_stock",
        "official_price_data",
        "repo_infrastructure",
    },
    ".github/workflows/individual_stock_report.yml": {
        "individual_stock",
        "official_price_data",
        "repo_infrastructure",
    },
    ".github/workflows/official_price_backfill.yml": {"official_price_data", "repo_infrastructure"},
    ".github/workflows/official_price_fetch.yml": {"official_price_data", "repo_infrastructure"},
    ".github/workflows/pages.yml": {"repo_infrastructure"},
    ".github/workflows/repair_daily_price_range.yml": {"official_price_data", "repo_infrastructure"},
    ".github/workflows/repair_one_daily_price.yml": {"official_price_data", "repo_infrastructure"},
    ".github/workflows/repair_recent_daily_price_gaps.yml": {"official_price_data", "repo_infrastructure"},
    ".github/workflows/repair_tdcc_monthly_history_gaps.yml": {"tdcc_weekly", "repo_infrastructure"},
    ".github/workflows/research_backtest_pipeline.yml": {
        "research_backtest",
        "market_risk",
        "daily_production",
        "tdcc_weekly",
        "catalyst_event",
        "repo_infrastructure",
    },
    ".github/workflows/signal_performance_tracker.yml": {"research_backtest", "repo_infrastructure"},
    ".github/workflows/tdcc_history_backfill.yml": {"tdcc_weekly", "repo_infrastructure"},
    ".github/workflows/tdcc_weekly.yml": {"tdcc_weekly", "repo_infrastructure"},
    ".github/workflows/test_tdcc_trend.yml": {"tdcc_weekly", "diagnostics", "repo_infrastructure"},
    ".github/workflows/warrant_flow.yml": {"warrant", "official_price_data", "repo_infrastructure"},
    ".github/workflows/weekly_theme_review.yml": {
        "catalyst_event",
        "daily_production",
        "repo_infrastructure",
    },
}

FORBIDDEN_WORKFLOW_SNIPPETS = {
    ".github/workflows/daily_full_pipeline.yml": {
        "daily pipeline must not run TDCC weekly report builders": (
            "python scripts/build_tdcc_weekly_candidate_reports.py",
            "python scripts/build_tdcc_signal_effectiveness_report.py",
        ),
        "daily pipeline must not stage TDCC weekly PDF outputs": (
            "git add output/latest/tdcc_weekly_",
            "git add docs/latest/tdcc_weekly_",
        ),
        "daily pipeline must not stage research source/config changes": (
            "git add config/",
            "git add scripts/",
            "git add .github/workflows/",
        ),
    },
    ".github/workflows/research_backtest_pipeline.yml": {
        "research pipeline must not mutate production config or source": (
            "git add config/",
            "git add scripts/",
            "git add .github/workflows/",
        ),
        "research pipeline must not run daily production PDF entrypoints": (
            "python scripts/run_chatgpt_daily_report_entrypoint.py",
            "python scripts/generate_chatgpt_side_daily_reports.py",
            "python build_chatgpt_daily_report_packet.py",
            "python build_chatgpt_daily_report_rules.py",
        ),
        "research pipeline must not stage full-market daily PDFs": (
            "git add output/latest/mainstream_",
            "git add output/latest/non_mainstream_",
            "git add output/latest/daily_market_",
            "git add docs/latest/mainstream_",
            "git add docs/latest/non_mainstream_",
            "git add docs/latest/daily_market_",
        ),
    },
    ".github/workflows/tdcc_weekly.yml": {
        "TDCC weekly pipeline must not stage broad source or data roots": (
            "git add output/ data/",
            "git add scripts/",
            "git add .github/workflows/",
            "git add config/",
        ),
        "TDCC weekly pipeline must not run daily PDF entrypoints": (
            "python scripts/run_chatgpt_daily_report_entrypoint.py",
            "python scripts/generate_chatgpt_side_daily_reports.py",
            "python build_chatgpt_daily_report_packet.py",
        ),
        "TDCC weekly pipeline must not stage daily PDF outputs": (
            "git add output/latest/mainstream_",
            "git add output/latest/non_mainstream_",
            "git add docs/latest/mainstream_",
            "git add docs/latest/non_mainstream_",
        ),
    },
    ".github/workflows/tdcc_history_backfill.yml": {
        "TDCC history backfill must not stage broad source or data roots": (
            "git add output/ data/",
            "git add scripts/",
            "git add .github/workflows/",
            "git add config/",
        ),
        "TDCC history backfill must not stage daily PDF outputs": (
            "git add output/latest/mainstream_",
            "git add output/latest/non_mainstream_",
            "git add docs/latest/mainstream_",
            "git add docs/latest/non_mainstream_",
        ),
    },
    ".github/workflows/repair_tdcc_monthly_history_gaps.yml": {
        "TDCC monthly history gap repair must not stage broad source or data roots": (
            "git add output/ data/",
            "git add scripts/",
            "git add .github/workflows/",
            "git add config/",
        ),
        "TDCC monthly history gap repair must not stage daily PDF outputs": (
            "git add output/latest/mainstream_",
            "git add output/latest/non_mainstream_",
            "git add docs/latest/mainstream_",
            "git add docs/latest/non_mainstream_",
        ),
    },
    ".github/workflows/warrant_flow.yml": {
        "warrant flow must not stage source or workflow files": (
            "git add scripts/",
            "git add .github/workflows/",
            "git add build_warrant_flow_latest.py",
            "git add merge_warrant_flow_into_candidates.py",
            "git add build_data_freshness_latest.py",
        ),
    },
    ".github/workflows/individual_stock_report.yml": {
        "individual stock report must not publish full-market daily PDFs": (
            "git add output/latest/mainstream_",
            "git add output/latest/non_mainstream_",
            "git add output/latest/daily_market_",
            "git add docs/latest/mainstream_",
            "git add docs/latest/non_mainstream_",
            "git add docs/latest/daily_market_",
        ),
    },
    ".github/workflows/individual_stock_data_refresh.yml": {
        "individual stock data refresh must not publish full-market daily PDFs": (
            "git add output/latest/mainstream_",
            "git add output/latest/non_mainstream_",
            "git add output/latest/daily_market_",
            "git add docs/latest/mainstream_",
            "git add docs/latest/non_mainstream_",
            "git add docs/latest/daily_market_",
        ),
    },
}

REQUIRED_WORKFLOW_COMMANDS = {
    DAILY_WORKFLOW: (
        "python scripts/validate_repo_production_inventory.py",
        "python scripts/validate_pdf_production_inventory.py",
        "python scripts/validate_daily_pdf_contract_consumers.py",
        "python scripts/validate_daily_pdf_shared_path_isolation.py",
        "python scripts/validate_daily_pdf_completion_hard_gate.py",
        "python scripts/validate_repo_code_isolation_policy.py",
        "python scripts/validate_model_research_workflow_isolation.py",
    ),
    ".github/workflows/research_backtest_pipeline.yml": (
        "python scripts/validate_repo_production_inventory.py",
        "python scripts/validate_research_production_boundaries.py",
        "python scripts/validate_model_research_workflow_isolation.py",
    ),
    ".github/workflows/daily_model_maintenance_pr_validation.yml": (
        "python scripts/validate_repo_production_inventory.py",
        "python scripts/validate_daily_pdf_contract_consumers.py",
        "python scripts/validate_daily_pdf_shared_path_isolation.py",
        "python scripts/validate_daily_pdf_completion_hard_gate.py",
        "python scripts/validate_daily_production_boundaries.py",
        "python scripts/validate_model_research_workflow_isolation.py",
    ),
    ".github/workflows/tdcc_weekly.yml": (
        "python scripts/validate_repo_production_inventory.py",
        "python scripts/validate_tdcc_report_contract_consumers.py",
    ),
    ".github/workflows/tdcc_history_backfill.yml": ("python scripts/validate_repo_production_inventory.py",),
    ".github/workflows/repair_tdcc_monthly_history_gaps.yml": (
        "python scripts/validate_apps_script_workflow_triggers.py",
        "python scripts/validate_repo_production_inventory.py",
        "python scripts/validate_repo_file_lifecycle_inventory.py",
        "python scripts/validate_repo_semantic_integrity.py",
    ),
    ".github/workflows/individual_stock_report.yml": ("python scripts/validate_repo_production_inventory.py",),
    ".github/workflows/individual_stock_data_refresh.yml": ("python scripts/validate_repo_production_inventory.py",),
    ".github/workflows/warrant_flow.yml": ("python scripts/validate_repo_production_inventory.py",),
    ".github/workflows/repair_recent_daily_price_gaps.yml": (
        "python scripts/validate_apps_script_workflow_triggers.py",
        "python scripts/validate_repo_production_inventory.py",
        "python scripts/validate_repo_file_lifecycle_inventory.py",
        "python scripts/validate_repo_semantic_integrity.py",
    ),
}

PYTHON_INVOKE_RE = re.compile(r"\bpython(?:3)?\s+([A-Za-z0-9_./\\-]+\.py)")
SHELL_INVOKE_RE = re.compile(r"\b(?:bash|sh)\s+([A-Za-z0-9_./\\-]+\.sh)")

EXECUTABLE_SCRIPT_SUFFIXES = {
    ".bat",
    ".cmd",
    ".gs",
    ".js",
    ".mjs",
    ".pl",
    ".ps1",
    ".rb",
    ".sh",
    ".ts",
    ".tsx",
}

ACTIVE_GUIDANCE_ROOT_FILES = {
    "AGENTS.md",
    "README.md",
}

ACTIVE_GUIDANCE_PREFIXES = (
    "docs/latest/",
    "output/latest/",
    "rules/",
)

ACTIVE_GUIDANCE_DOCS_ROOT_SUFFIXES = {
    ".md",
    ".txt",
}

FORBIDDEN_GUIDANCE_COMMANDS = {
    r"\bpython(?:3)?\s+scripts/generate_chatgpt_side_daily_reports\.py\b": (
        "active guidance must point users to scripts/run_chatgpt_daily_report_entrypoint.py, "
        "not the renderer CLI"
    ),
    r"\bpython(?:3)?\s+generate_repo_chatgpt_side_reports\.py\b": (
        "active guidance must not point users to the retired OneDrive/helper report generator"
    ),
    r"\bpython(?:3)?\s+scripts/generate_daily_market_pdf\.py\b": (
        "active guidance must not point users to retired daily market PDF generator"
    ),
    r"\bpython(?:3)?\s+scripts/validate_daily_market_report\.py\b": (
        "active guidance must not point users to retired daily market PDF validator"
    ),
    r"\bpython(?:3)?\s+build_daily_market_report_artifacts\.py\b": (
        "active guidance must not present repo market artifacts as the formal daily PDF entrypoint"
    ),
}


@dataclass(frozen=True)
class InventoryRow:
    path: str
    kind: str
    owner: str
    status: str
    purpose: str
    allowed_workflows: tuple[str, ...]
    allowed_stage_patterns: tuple[str, ...]


def run_git_ls_files(pattern: str) -> set[str]:
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


def tracked_python_paths() -> set[str]:
    tracked = {
        path
        for path in run_git_ls_files("*.py")
        if path.startswith("scripts/") or "/" not in path
        if (ROOT / path).exists()
    }
    working_tree = {
        path.relative_to(ROOT).as_posix()
        for pattern in ("*.py", "scripts/**/*.py")
        for path in ROOT.glob(pattern)
        if "__pycache__" not in path.parts
    }
    return tracked | working_tree


def tracked_test_python_paths() -> set[str]:
    tracked = {path for path in run_git_ls_files("*.py") if path.startswith("tests/") if (ROOT / path).exists()}
    working_tree = {
        path.relative_to(ROOT).as_posix()
        for path in (ROOT / "tests").glob("**/*.py")
        if "__pycache__" not in path.parts
    }
    return tracked | working_tree


def tracked_executable_script_paths() -> set[str]:
    tracked = {
        path
        for path in run_git_ls_files("*")
        if Path(path).suffix in EXECUTABLE_SCRIPT_SUFFIXES
        if (ROOT / path).exists()
    }
    working_tree = {
        path.relative_to(ROOT).as_posix()
        for path in ROOT.glob("**/*")
        if path.is_file()
        and ".git" not in path.parts
        and "__pycache__" not in path.parts
        and path.suffix in EXECUTABLE_SCRIPT_SUFFIXES
    }
    return tracked | working_tree


def tracked_workflow_paths() -> set[str]:
    tracked = {
        *run_git_ls_files(".github/workflows/*.yml"),
        *run_git_ls_files(".github/workflows/*.yaml"),
    }
    tracked = {path for path in tracked if (ROOT / path).exists()}
    working_tree = {
        path.relative_to(ROOT).as_posix()
        for pattern in (".github/workflows/*.yml", ".github/workflows/*.yaml")
        for path in ROOT.glob(pattern)
    }
    return tracked | working_tree


def tracked_guidance_text_paths() -> set[str]:
    tracked: set[str] = set()
    for path in run_git_ls_files("*"):
        if not (ROOT / path).exists():
            continue
        suffix = Path(path).suffix.lower()
        if suffix not in {".md", ".txt"}:
            continue
        if path in ACTIVE_GUIDANCE_ROOT_FILES:
            tracked.add(path)
            continue
        if path.startswith(ACTIVE_GUIDANCE_PREFIXES):
            tracked.add(path)
            continue
        if path.startswith("docs/") and path.count("/") == 1 and suffix in ACTIVE_GUIDANCE_DOCS_ROOT_SUFFIXES:
            tracked.add(path)
    return tracked


def split_semicolon(value: str) -> tuple[str, ...]:
    return tuple(part.strip().replace("\\", "/") for part in value.split(";") if part.strip())


def load_inventory(errors: list[str]) -> dict[str, InventoryRow]:
    rows_by_path: dict[str, InventoryRow] = {}
    if not INVENTORY.exists():
        errors.append("missing repo production inventory: config/repo_production_inventory.csv")
        return rows_by_path

    with INVENTORY.open("r", encoding="utf-8-sig", newline="") as fh:
        reader = csv.DictReader(fh)
        if not reader.fieldnames:
            errors.append("repo production inventory is empty")
            return rows_by_path
        missing = REQUIRED_COLUMNS.difference(reader.fieldnames)
        if missing:
            errors.append(f"repo production inventory missing columns: {sorted(missing)}")
            return rows_by_path

        for line_no, row in enumerate(reader, start=2):
            path = (row.get("path") or "").strip().replace("\\", "/")
            if not path:
                errors.append(f"inventory row {line_no} has empty path")
                continue
            if path in rows_by_path:
                errors.append(f"inventory path listed more than once: {path}")
                continue
            inventory_row = InventoryRow(
                path=path,
                kind=(row.get("kind") or "").strip(),
                owner=(row.get("owner") or "").strip(),
                status=(row.get("status") or "").strip(),
                purpose=(row.get("purpose") or "").strip(),
                allowed_workflows=split_semicolon(row.get("allowed_workflows") or ""),
                allowed_stage_patterns=split_semicolon(row.get("allowed_stage_patterns") or ""),
            )
            rows_by_path[path] = inventory_row

    return rows_by_path


def read_text(rel_path: str) -> str:
    return (ROOT / rel_path).read_text(encoding="utf-8", errors="replace")


def normalize_invoked_python_path(path: str) -> str:
    normalized = path.strip().strip("'\"").replace("\\", "/")
    if normalized.startswith("./"):
        normalized = normalized[2:]
    return normalized


def workflow_invocations(workflow_path: str) -> set[str]:
    text = read_text(workflow_path)
    invoked = {normalize_invoked_python_path(match.group(1)) for match in PYTHON_INVOKE_RE.finditer(text)}
    invoked.update(normalize_invoked_python_path(match.group(1)) for match in SHELL_INVOKE_RE.finditer(text))
    return invoked


def validate_inventory_coverage(
    rows_by_path: dict[str, InventoryRow],
    python_paths: set[str],
    test_python_paths: set[str],
    executable_script_paths: set[str],
    workflow_paths: set[str],
    errors: list[str],
) -> None:
    expected = python_paths | test_python_paths | executable_script_paths | workflow_paths
    actual = set(rows_by_path)

    for path in sorted(expected - actual):
        errors.append(f"tracked executable/test/workflow path missing owner inventory: {path}")
    for path in sorted(actual - expected):
        errors.append(f"inventory lists untracked or out-of-scope path: {path}")


def validate_inventory_rows(rows_by_path: dict[str, InventoryRow], errors: list[str]) -> None:
    for row in rows_by_path.values():
        if row.kind not in VALID_KINDS:
            errors.append(f"{row.path} has invalid inventory kind: {row.kind}")
        if row.kind == "test_python" and not row.path.startswith("tests/"):
            errors.append(f"{row.path} has test_python kind but is not under tests/")
        if row.kind == "executable_script" and Path(row.path).suffix not in EXECUTABLE_SCRIPT_SUFFIXES:
            errors.append(f"{row.path} has executable_script kind but unsupported suffix")
        if row.owner not in VALID_OWNERS:
            errors.append(f"{row.path} has invalid or empty owner: {row.owner}")
        if row.status not in VALID_STATUSES:
            errors.append(f"{row.path} has invalid status: {row.status}")
        if not row.purpose:
            errors.append(f"{row.path} has empty purpose")
        if row.kind == "workflow" and row.path not in WORKFLOW_ALLOWED_OWNERS:
            errors.append(f"workflow has no allowed-owner boundary rule: {row.path}")
        if row.status == "legacy_deprecated" and row.allowed_workflows:
            errors.append(f"deprecated path must not list allowed workflows: {row.path}")


def validate_workflow_invocations(rows_by_path: dict[str, InventoryRow], workflow_paths: set[str], errors: list[str]) -> None:
    for workflow_path in sorted(workflow_paths):
        workflow_row = rows_by_path.get(workflow_path)
        if workflow_row is None:
            continue
        allowed_owners = WORKFLOW_ALLOWED_OWNERS.get(workflow_path, set())
        invoked_paths = workflow_invocations(workflow_path)

        for invoked_path in sorted(invoked_paths):
            if not (
                invoked_path.startswith("scripts/")
                or invoked_path.startswith("tests/")
                or invoked_path.startswith("docs/")
                or "/" not in invoked_path
            ):
                continue
            invoked_row = rows_by_path.get(invoked_path)
            if invoked_row is None:
                errors.append(f"{workflow_path} invokes Python path without inventory owner: {invoked_path}")
                continue
            if invoked_row.status == "legacy_deprecated":
                errors.append(f"{workflow_path} invokes deprecated Python path: {invoked_path}")
            if invoked_row.owner not in allowed_owners:
                errors.append(
                    f"{workflow_path} invokes {invoked_path} owned by {invoked_row.owner}; "
                    f"allowed owners are {sorted(allowed_owners)}"
                )
            if invoked_row.allowed_workflows and workflow_path not in invoked_row.allowed_workflows:
                errors.append(
                    f"{workflow_path} invokes {invoked_path}, but inventory allowed_workflows="
                    f"{list(invoked_row.allowed_workflows)}"
                )


def validate_workflow_snippets(errors: list[str]) -> None:
    for workflow_path, command_list in REQUIRED_WORKFLOW_COMMANDS.items():
        if not (ROOT / workflow_path).exists():
            continue
        text = read_text(workflow_path)
        for command in command_list:
            if command not in text:
                errors.append(f"{workflow_path} must run {command}")

    for workflow_path, grouped_snippets in FORBIDDEN_WORKFLOW_SNIPPETS.items():
        if not (ROOT / workflow_path).exists():
            continue
        text = read_text(workflow_path)
        for label, snippets in grouped_snippets.items():
            for snippet in snippets:
                if snippet in text:
                    errors.append(f"{workflow_path}: {label}: forbidden snippet found: {snippet}")


def validate_allowed_stage_patterns(rows_by_path: dict[str, InventoryRow], errors: list[str]) -> None:
    for row in rows_by_path.values():
        if row.kind != "workflow":
            continue
        text = read_text(row.path)
        for pattern in row.allowed_stage_patterns:
            if pattern and pattern not in text:
                errors.append(f"{row.path} inventory allowed_stage_patterns missing from workflow text: {pattern}")


def validate_active_guidance_commands(errors: list[str]) -> None:
    for rel_path in sorted(tracked_guidance_text_paths()):
        path = ROOT / rel_path
        if not path.exists():
            continue
        text = path.read_text(encoding="utf-8", errors="replace")
        for pattern, message in FORBIDDEN_GUIDANCE_COMMANDS.items():
            if re.search(pattern, text):
                errors.append(f"{message}: {rel_path} matches {pattern}")


def validate() -> list[str]:
    errors: list[str] = []
    rows_by_path = load_inventory(errors)
    python_paths = tracked_python_paths()
    test_python_paths = tracked_test_python_paths()
    executable_script_paths = tracked_executable_script_paths()
    workflow_paths = tracked_workflow_paths()

    if rows_by_path:
        validate_inventory_coverage(
            rows_by_path,
            python_paths,
            test_python_paths,
            executable_script_paths,
            workflow_paths,
            errors,
        )
        validate_inventory_rows(rows_by_path, errors)
        validate_workflow_invocations(rows_by_path, workflow_paths, errors)
        validate_allowed_stage_patterns(rows_by_path, errors)

    validate_workflow_snippets(errors)
    validate_active_guidance_commands(errors)
    return errors


def main() -> int:
    errors = validate()
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1

    python_count = len(tracked_python_paths())
    test_python_count = len(tracked_test_python_paths())
    executable_script_count = len(tracked_executable_script_paths())
    workflow_count = len(tracked_workflow_paths())
    print("repo production inventory validation passed")
    print(f"validated_python_paths={python_count}")
    print(f"validated_test_python_paths={test_python_count}")
    print(f"validated_executable_scripts={executable_script_count}")
    print(f"validated_workflows={workflow_count}")
    print(f"inventory={INVENTORY.relative_to(ROOT).as_posix()}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
