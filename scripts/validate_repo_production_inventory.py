from __future__ import annotations

import csv
import re
import subprocess
from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
INVENTORY = ROOT / "config" / "repo_production_inventory.csv"
DAILY_WORKFLOW = ".github/workflows/daily_full_pipeline.yml"
PRODUCTION_ARTIFACT_WRITE_DEPLOY_KEY = "PRODUCTION_ARTIFACT_WRITE_DEPLOY_KEY"
PRODUCTION_ARTIFACT_WRITE_SECRET_EXPRESSION = (
    "${{ secrets.PRODUCTION_ARTIFACT_WRITE_DEPLOY_KEY }}"
)
PRODUCTION_ARTIFACT_WRITE_SSH_KEY = (
    f"ssh-key: {PRODUCTION_ARTIFACT_WRITE_SECRET_EXPRESSION}"
)
PRODUCTION_ARTIFACT_PERSIST_CREDENTIALS = "persist-credentials: true"
PRODUCTION_ARTIFACT_WRITE_PREFLIGHT_NAME = (
    "Require production artifact write deploy key"
)
PRODUCTION_ARTIFACT_WRITE_SECRET_GUARD = (
    'if [ -z "${PRODUCTION_ARTIFACT_WRITE_DEPLOY_KEY}" ]; then'
)
ARTIFACT_PUSH_JOB_MARKERS = (
    "git commit",
    "git push",
    "ci_push_with_retry.sh",
)

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
    ".github/workflows/daily_pdf_replay_pr_validation.yml": {
        "daily_production",
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
    ".github/workflows/historical_structured_source_replay.yml": {
        "official_price_data",
        "market_risk",
        "warrant",
        "repo_infrastructure",
    },
    ".github/workflows/individual_stock_data_refresh.yml": {
        "individual_stock",
        "official_price_data",
        "repo_infrastructure",
    },
    ".github/workflows/individual_stock_pr_validation.yml": {
        "individual_stock",
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
    ".github/workflows/tdcc_weekly_pr_validation.yml": {"tdcc_weekly", "repo_infrastructure"},
    ".github/workflows/tdcc_weekly.yml": {"tdcc_weekly", "repo_infrastructure"},
    ".github/workflows/test_tdcc_trend.yml": {"tdcc_weekly", "diagnostics", "repo_infrastructure"},
    ".github/workflows/warrant_flow.yml": {
        "catalyst_event",
        "daily_production",
        "official_price_data",
        "repo_infrastructure",
        "warrant",
    },
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
    ".github/workflows/individual_stock_pr_validation.yml": {
        "individual stock PR validation must remain read-only": (
            "contents: write",
            "git add ",
            "git commit",
            "git push",
            "actions/upload-pages-artifact",
            "actions/deploy-pages",
        ),
    },
    ".github/workflows/tdcc_weekly_pr_validation.yml": {
        "TDCC weekly PR validation must remain read-only": (
            "contents: write",
            "git add ",
            "git commit",
            "git push",
            "actions/upload-pages-artifact",
            "actions/deploy-pages",
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
    ".github/workflows/historical_structured_source_replay.yml": (
        "python scripts/validate_apps_script_workflow_triggers.py",
        "python scripts/validate_repo_production_inventory.py",
        "python scripts/validate_repo_file_lifecycle_inventory.py",
        "python scripts/validate_repo_semantic_integrity.py",
        "python scripts/validate_daily_production_boundaries.py",
        "python scripts/replay_historical_structured_sources.py",
        "python scripts/validate_historical_structured_source_replay.py",
        "python scripts/validate_historical_source_replay_staged_paths.py",
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
    ".github/workflows/daily_pdf_replay_pr_validation.yml": (
        "python scripts/validate_repo_production_inventory.py",
        "python scripts/validate_daily_pdf_contract_consumers.py",
        "python scripts/validate_daily_pdf_shared_path_isolation.py",
        "python scripts/validate_daily_pdf_completion_hard_gate.py",
        "python scripts/validate_daily_production_boundaries.py",
    ),
    ".github/workflows/tdcc_weekly.yml": (
        "python scripts/validate_repo_production_inventory.py",
        "python scripts/validate_tdcc_report_contract_consumers.py",
    ),
    ".github/workflows/tdcc_history_backfill.yml": ("python scripts/validate_repo_production_inventory.py",),
    ".github/workflows/tdcc_weekly_pr_validation.yml": (
        "python scripts/validate_apps_script_workflow_triggers.py",
        "python scripts/validate_repo_file_lifecycle_inventory.py",
        "python scripts/validate_repo_production_inventory.py",
        "python scripts/validate_repo_semantic_integrity.py",
        "python scripts/validate_daily_production_boundaries.py",
    ),
    ".github/workflows/repair_tdcc_monthly_history_gaps.yml": (
        "python scripts/validate_apps_script_workflow_triggers.py",
        "python scripts/validate_repo_production_inventory.py",
        "python scripts/validate_repo_file_lifecycle_inventory.py",
        "python scripts/validate_repo_semantic_integrity.py",
    ),
    ".github/workflows/individual_stock_report.yml": ("python scripts/validate_repo_production_inventory.py",),
    ".github/workflows/individual_stock_data_refresh.yml": ("python scripts/validate_repo_production_inventory.py",),
    ".github/workflows/individual_stock_pr_validation.yml": (
        "python scripts/validate_repo_file_lifecycle_inventory.py",
        "python scripts/validate_repo_production_inventory.py",
        "python scripts/validate_individual_pdf_contract_consumers.py",
    ),
    ".github/workflows/warrant_flow.yml": ("python scripts/validate_repo_production_inventory.py",),
    ".github/workflows/repair_recent_daily_price_gaps.yml": (
        "python scripts/validate_apps_script_workflow_triggers.py",
        "python scripts/validate_repo_production_inventory.py",
        "python scripts/validate_repo_file_lifecycle_inventory.py",
        "python scripts/validate_repo_semantic_integrity.py",
        "python scripts/validate_recent_structured_source_repair_workflow.py",
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


def workflow_job_blocks(text: str) -> dict[str, str]:
    blocks: dict[str, str] = {}
    in_jobs = False
    current_name = ""
    current_lines: list[str] = []

    for line in text.splitlines(keepends=True):
        stripped = line.rstrip("\r\n")
        if not in_jobs:
            if stripped == "jobs:":
                in_jobs = True
            continue
        if stripped and not line.startswith((" ", "\t")):
            break

        match = re.match(r"^  ([A-Za-z0-9_-]+):\s*$", stripped)
        if match:
            if current_name:
                blocks[current_name] = "".join(current_lines)
            current_name = match.group(1)
            current_lines = [line]
        elif current_name:
            current_lines.append(line)

    if current_name:
        blocks[current_name] = "".join(current_lines)
    return blocks


def workflow_has_pull_request_trigger(text: str) -> bool:
    lines = text.splitlines()
    for index, line in enumerate(lines):
        if re.match(r"^on:\s*(?:pull_request|\[[^]]*\bpull_request\b[^]]*\])\s*$", line):
            return True
        if line.strip() != "on:" or line.startswith((" ", "\t")):
            continue
        for trigger_line in lines[index + 1 :]:
            if trigger_line and not trigger_line.startswith((" ", "\t")):
                break
            if re.match(r"^  pull_request:\s*$", trigger_line):
                return True
        return False
    return False


def workflow_call_declared_secrets(text: str) -> set[str]:
    secrets: set[str] = set()
    in_workflow_call = False
    in_secrets = False

    for line in text.splitlines():
        if line == "  workflow_call:":
            in_workflow_call = True
            in_secrets = False
            continue
        if not in_workflow_call:
            continue
        if re.match(r"^  \S", line):
            break
        if line == "    secrets:":
            in_secrets = True
            continue
        if not in_secrets:
            continue
        if re.match(r"^    \S", line):
            in_secrets = False
            continue
        match = re.match(r"^      ([A-Za-z0-9_]+):\s*$", line)
        if match:
            secrets.add(match.group(1))

    return secrets


def local_reusable_workflow_path(job_block: str) -> str:
    match = re.search(
        r"^    uses:\s+\./(\.github/workflows/[A-Za-z0-9_.-]+\.ya?ml)\s*$",
        job_block,
        flags=re.MULTILINE,
    )
    return match.group(1) if match else ""


def workflow_job_mapping(job_block: str, section: str) -> dict[str, str]:
    lines = job_block.splitlines()
    section_line = f"    {section}:"
    mapping: dict[str, str] = {}
    in_section = False
    for line in lines:
        if not in_section:
            if line == section_line:
                in_section = True
            continue
        if re.match(r"^    \S", line):
            break
        match = re.match(r"^      ([A-Za-z0-9_]+):\s*(.*?)\s*$", line)
        if match:
            mapping[match.group(1)] = match.group(2).strip("'\"")
    return mapping


def is_registered_reusable_writer_job(
    job_block: str,
    rows_by_path: dict[str, InventoryRow],
) -> bool:
    called_path = local_reusable_workflow_path(job_block)
    called_row = rows_by_path.get(called_path)
    if not called_path or called_row is None or not called_row.allowed_stage_patterns:
        return False
    called_text = read_text(called_path)
    return workflow_call_declared_secrets(called_text) == {
        PRODUCTION_ARTIFACT_WRITE_DEPLOY_KEY
    }


def validate_reusable_writer_delegate(
    workflow_path: str,
    job_name: str,
    block: str,
    errors: list[str],
) -> None:
    secrets = workflow_job_mapping(block, "secrets")
    expected = {
        PRODUCTION_ARTIFACT_WRITE_DEPLOY_KEY: PRODUCTION_ARTIFACT_WRITE_SECRET_EXPRESSION
    }
    if secrets != expected:
        errors.append(
            f"{workflow_path} reusable writer job {job_name} must pass exactly "
            f"secrets.{PRODUCTION_ARTIFACT_WRITE_DEPLOY_KEY} and no other secrets"
        )


def workflow_step_blocks(job_block: str) -> list[str]:
    blocks: list[str] = []
    in_steps = False
    current_lines: list[str] = []

    for line in job_block.splitlines(keepends=True):
        stripped = line.rstrip("\r\n")
        if not in_steps:
            if stripped == "    steps:":
                in_steps = True
            continue

        if re.match(r"^      -\s+", stripped):
            if current_lines:
                blocks.append("".join(current_lines))
            current_lines = [line]
        elif current_lines:
            current_lines.append(line)

    if current_lines:
        blocks.append("".join(current_lines))
    return blocks


def workflow_step_name(step_block: str) -> str:
    match = re.search(r"^      - name:\s*(.+?)\s*$", step_block, flags=re.MULTILINE)
    return match.group(1) if match else ""


def workflow_step_mapping(step_block: str, section: str) -> dict[str, str]:
    lines = step_block.splitlines()
    section_line = f"        {section}:"
    mapping: dict[str, str] = {}
    in_section = False

    for line in lines:
        if not in_section:
            if line == section_line:
                in_section = True
            continue
        if not line.strip():
            continue
        indent = len(line) - len(line.lstrip(" "))
        if indent <= 8:
            break
        match = re.match(r"^          ([A-Za-z0-9_-]+):\s*(.*?)\s*$", line)
        if match:
            mapping[match.group(1)] = match.group(2)
    return mapping


def is_checkout_step(step_block: str) -> bool:
    return bool(
        re.search(
            r"^        uses:\s*actions/checkout@[^\s#]+\s*$",
            step_block,
            flags=re.MULTILINE,
        )
    )


def is_valid_writer_secret_preflight(step_block: str) -> bool:
    if workflow_step_name(step_block) != PRODUCTION_ARTIFACT_WRITE_PREFLIGHT_NAME:
        return False
    if not re.search(r"^        shell:\s*bash\s*$", step_block, flags=re.MULTILINE):
        return False
    env = workflow_step_mapping(step_block, "env")
    if (
        env.get(PRODUCTION_ARTIFACT_WRITE_DEPLOY_KEY)
        != PRODUCTION_ARTIFACT_WRITE_SECRET_EXPRESSION
    ):
        return False
    stripped_lines = {line.strip() for line in step_block.splitlines()}
    return (
        PRODUCTION_ARTIFACT_WRITE_SECRET_GUARD in stripped_lines
        and "exit 1" in stripped_lines
    )


def is_artifact_push_job(block: str) -> bool:
    return any(marker in block for marker in ARTIFACT_PUSH_JOB_MARKERS)


def validate_artifact_push_job(
    workflow_path: str,
    job_name: str,
    block: str,
    errors: list[str],
) -> None:
    steps = workflow_step_blocks(block)
    checkout_steps = [
        (index, step)
        for index, step in enumerate(steps)
        if is_checkout_step(step)
    ]
    if not checkout_steps:
        errors.append(f"{workflow_path} writer job {job_name} must checkout the repository")

    keyed_checkout_steps = [
        (index, step)
        for index, step in checkout_steps
        if workflow_step_mapping(step, "with").get("ssh-key")
        == PRODUCTION_ARTIFACT_WRITE_SECRET_EXPRESSION
    ]
    if not keyed_checkout_steps:
        errors.append(
            f"{workflow_path} writer job {job_name} must use "
            f"secrets.{PRODUCTION_ARTIFACT_WRITE_DEPLOY_KEY} as actions/checkout ssh-key"
        )

    authenticated_checkout_steps = [
        (index, step)
        for index, step in keyed_checkout_steps
        if workflow_step_mapping(step, "with").get("persist-credentials") == "true"
    ]
    if keyed_checkout_steps and not authenticated_checkout_steps:
        errors.append(
            f"{workflow_path} writer job {job_name} must set persist-credentials: true "
            "in the same actions/checkout step as the deploy key"
        )

    preflight_indices = [
        index
        for index, step in enumerate(steps)
        if is_valid_writer_secret_preflight(step)
    ]
    if not preflight_indices:
        errors.append(
            f"{workflow_path} writer job {job_name} must fail closed when "
            f"secrets.{PRODUCTION_ARTIFACT_WRITE_DEPLOY_KEY} is empty"
        )
    elif checkout_steps and min(preflight_indices) >= min(index for index, _ in checkout_steps):
        errors.append(
            f"{workflow_path} writer job {job_name} must check the deploy key "
            "before actions/checkout"
        )


def validate_production_artifact_writer_auth(
    rows_by_path: dict[str, InventoryRow],
    workflow_paths: set[str],
    errors: list[str],
) -> None:
    for workflow_path in sorted(workflow_paths):
        row = rows_by_path.get(workflow_path)
        text = read_text(workflow_path)
        job_blocks = workflow_job_blocks(text)
        artifact_push_jobs = {
            job_name: block
            for job_name, block in job_blocks.items()
            if is_artifact_push_job(block)
        }
        is_registered_writer = bool(row is not None and row.allowed_stage_patterns)
        writer_jobs = artifact_push_jobs if is_registered_writer else {}
        reusable_writer_jobs = {
            job_name: block
            for job_name, block in job_blocks.items()
            if is_registered_reusable_writer_job(block, rows_by_path)
        }

        if is_registered_writer and not artifact_push_jobs:
            errors.append(
                f"{workflow_path} has allowed_stage_patterns but no artifact push job"
            )

        for job_name, block in writer_jobs.items():
            validate_artifact_push_job(workflow_path, job_name, block, errors)
        for job_name, block in reusable_writer_jobs.items():
            validate_reusable_writer_delegate(workflow_path, job_name, block, errors)

        for job_name, block in job_blocks.items():
            if (
                job_name not in writer_jobs
                and job_name not in reusable_writer_jobs
                and PRODUCTION_ARTIFACT_WRITE_DEPLOY_KEY in block
            ):
                errors.append(
                    f"{workflow_path} non-writer job {job_name} must not use "
                    f"secrets.{PRODUCTION_ARTIFACT_WRITE_DEPLOY_KEY}"
                )

        writer_secret_count = sum(
            block.count(PRODUCTION_ARTIFACT_WRITE_DEPLOY_KEY)
            for block in writer_jobs.values()
        )
        reusable_writer_secret_count = sum(
            block.count(PRODUCTION_ARTIFACT_WRITE_DEPLOY_KEY)
            for block in reusable_writer_jobs.values()
        )
        reusable_secret_declaration_count = int(
            is_registered_writer
            and PRODUCTION_ARTIFACT_WRITE_DEPLOY_KEY
            in workflow_call_declared_secrets(text)
        )
        if (
            text.count(PRODUCTION_ARTIFACT_WRITE_DEPLOY_KEY)
            != writer_secret_count
            + reusable_writer_secret_count
            + reusable_secret_declaration_count
        ):
            errors.append(
                f"{workflow_path} must scope secrets.{PRODUCTION_ARTIFACT_WRITE_DEPLOY_KEY} "
                "to artifact push jobs only"
            )
        if workflow_has_pull_request_trigger(text) and PRODUCTION_ARTIFACT_WRITE_DEPLOY_KEY in text:
            errors.append(
                f"{workflow_path} pull_request workflow must not use "
                f"secrets.{PRODUCTION_ARTIFACT_WRITE_DEPLOY_KEY}"
            )


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
        validate_production_artifact_writer_auth(rows_by_path, workflow_paths, errors)

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
