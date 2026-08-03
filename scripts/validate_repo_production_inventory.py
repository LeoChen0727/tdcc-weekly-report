from __future__ import annotations

import argparse
import csv
import hashlib
import io
import json
import re
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
INVENTORY = ROOT / "config" / "repo_production_inventory.csv"
PR_SAFE_BASE_GUARD_WORKFLOW = ".github/workflows/individual_stock_pr_validation.yml"
PR_SAFE_BASE_GUARD_SCRIPT = "scripts/validate_repo_production_inventory.py"
PR_SAFE_REPOSITORY = "LeoChen0727/tdcc-weekly-report"
PR_SAFE_AUDIT_MANIFEST_SCHEMA_VERSION = 1
PR_SAFE_AUDIT_MODE = "base_owned_evidence_only"
PR_SAFE_AUDIT_MANIFEST_FILENAME = "pr-safe-control-plane-audit-manifest.json"
PR_SAFE_EXPECTED_WORKFLOW_REF = (
    f"{PR_SAFE_REPOSITORY}/{PR_SAFE_BASE_GUARD_WORKFLOW}@refs/heads/main"
)
PR_SAFE_ALLOWED_EVENT_ACTIONS = frozenset(
    {"opened", "synchronize", "reopened", "edited"}
)
PR_SAFE_CHECKOUT_ACTION = (
    "actions/checkout@d23441a48e516b6c34aea4fa41551a30e30af803"
)
PR_SAFE_SETUP_PYTHON_ACTION = (
    "actions/setup-python@ece7cb06caefa5fff74198d8649806c4678c61a1"
)
PR_SAFE_UPLOAD_ARTIFACT_ACTION = (
    "actions/upload-artifact@ea165f8d65b6e75b540449e92b4886f43607fa02"
)
PR_SAFE_EXPECTED_ACTION_USES = (
    PR_SAFE_CHECKOUT_ACTION,
    PR_SAFE_SETUP_PYTHON_ACTION,
    PR_SAFE_CHECKOUT_ACTION,
    PR_SAFE_UPLOAD_ARTIFACT_ACTION,
)
PR_SAFE_REQUIRED_CHECK_CONTEXT = "individual-stock-pr-validation"
PR_SAFE_TARGET_SKIP_CHECK_NAME = (
    "individual-stock-pr-validation-pull-request-target-skip"
)
PR_SAFE_REGULAR_JOB_NAME_EXPRESSION = (
    "${{ github.event_name == 'pull_request' && "
    "'individual-stock-pr-validation' || "
    "'individual-stock-pr-validation-pull-request-target-skip' }}"
)
PR_SAFE_READ_ONLY_PERMISSIONS = {"contents": "read"}
PR_SAFE_AUDIT_STEP_NAMES = (
    "Checkout pull request base only",
    "Fetch pull request head object without checkout",
    "Validate PR head blobs and write audit-only manifest",
    "Record audit manifest SHA-256",
    "Upload audit-only evidence",
    "Fail runner when audit validator rejects",
)
PR_SAFE_AUDIT_STEP_SHA256 = (
    "1cf9ca3456324b5fc20d51705d37dee3f715e528fb912eb01cc4e7497925ecf9",
    "b90af382f61aaa0f33f4aa81515e392863444446342c505d4a3098c498b89fce",
    "e301e03e3c7c6e60231a199662fd297a706f007727cc9aa249135ddd9413fb7f",
    "26bade9c4c3b3a0e8e2fcb8b293f309e359efca4904eef8c853b0f3e3c8bed24",
    "8169e8d5635859dca2c93eef7e4221c23a1f3f92d9f92efddf3a3752f4156d2a",
    "39bd97385eabe276a77d3721ff8df61c3aa3d796a3d016755454bdce823ff845",
)
PR_SAFE_AUDIT_JOB_NAME = "pr-safe-base-audit-runner"
PR_SAFE_AUDIT_JOB_RUNS_ON = "ubuntu-latest"
PR_SAFE_AUDIT_JOB_TIMEOUT_MINUTES = "10"
PR_SAFE_AUDIT_JOB_IF_BLOCK = (
    "    if: >-",
    "      github.event_name == 'pull_request_target' &&",
    "      github.event.pull_request.base.ref == 'main' &&",
    "      github.event.pull_request.base.repo.full_name == github.repository",
)
PR_SAFE_AUDIT_JOB_HEADER_SHA256 = (
    "9b2aef41c5b06cdd3b1179b71f0773ebf2ff6ce56de801786990af27b4871806"
)
PR_SAFE_AUDIT_ARTIFACT_NAME = (
    "pr-safe-control-plane-audit-${{ github.run_id }}-${{ github.run_attempt }}"
)
PR_SAFE_AUDIT_ARTIFACT_PATHS = (
    "${{ runner.temp }}/pr-safe-control-plane-audit-manifest.json",
    "${{ runner.temp }}/pr-safe-control-plane-audit-manifest.json.sha256",
)
PR_SAFE_AUDIT_RETENTION_DAYS = "30"
PR_SAFE_AUTHORIZATION_PATH = (
    "config/daily_model_pr_safe_self_migration_authorizations.csv"
)
PR_SAFE_LIFECYCLE_AUTHORIZATION_PATH = (
    "config/repo_file_lifecycle_semantic_migrations.csv"
)
PR_SAFE_LIFECYCLE_AUTHORIZATION_COLUMNS = (
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
PR_SAFE_LIFECYCLE_AUTHORIZATION_STATUS = "preauthorized"
PR_SAFE_LIFECYCLE_AUTHORIZATION_SCOPE = "pr462_research_lifecycle_only"
PR_SAFE_LIFECYCLE_AUTHORIZED_TARGETS = frozenset(
    {
        ("scripts/build_model_data_independence_audit.py", "reads_artifact"),
        ("scripts/build_revenue_unreacted_range_research.py", "reads_artifact"),
    }
)
PR_SAFE_AUTHORIZATION_COLUMNS = (
    "migration_id",
    "status",
    "approval_reference",
    "base_helper_sha256",
    "current_helper_sha256",
    "current_test_sha256",
    "changed_paths",
)
PR_SAFE_ADDITIVE_RESEARCH_MIGRATION_ID = (
    "additive-research-validation-registration-pr-safe-v2"
)
PR_SAFE_ADVANCED_HELPER = "scripts/validate_repo_advanced_integrity_pr_safe.py"
PR_SAFE_ADVANCED_TEST = "tests/test_repo_advanced_integrity_pr_safe.py"
PR_SAFE_AUTHORIZED_STAGE1_PATHS = frozenset(
    {PR_SAFE_ADVANCED_HELPER, PR_SAFE_ADVANCED_TEST}
)
PR_SAFE_RETAINED_AUTHORIZATION_ROWS = (
    {
        "migration_id": "additive-research-validation-registration-pr-safe-v1",
        "status": "preauthorized",
        "approval_reference": (
            "user_authorized_pr_safe_stage0_control_plane_trust_root_20260803"
        ),
        "base_helper_sha256": (
            "72f79f37dd8a4ece163f9f6e3c7f299f3243c8c44b66442c992bc54f38126315"
        ),
        "current_helper_sha256": (
            "b09d8063512dad3c771789e8e546ab4c1541b5f1b1ca8cb59a1bfcfb3c35982a"
        ),
        "current_test_sha256": (
            "72e308d5e8757878958ba21529298001c1888a72e9e837ed9d6057c3d8e2f50b"
        ),
        "changed_paths": f"{PR_SAFE_ADVANCED_HELPER};{PR_SAFE_ADVANCED_TEST}",
    },
)
PR_SAFE_TRIGGER_PATHS = tuple(sorted(PR_SAFE_AUTHORIZED_STAGE1_PATHS))
PR_SAFE_IMMUTABLE_TRUST_ROOT_PATHS = frozenset(
    {
        PR_SAFE_BASE_GUARD_WORKFLOW,
        PR_SAFE_BASE_GUARD_SCRIPT,
        PR_SAFE_AUTHORIZATION_PATH,
        PR_SAFE_LIFECYCLE_AUTHORIZATION_PATH,
    }
)
PR_SAFE_REGULAR_BLOB_MODES = frozenset({"100644", "100755"})
PR_SAFE_FORBIDDEN_WRITE_PERMISSION_RE = re.compile(
    r"(?im)(?:^|[{,])\s*['\"]?(?:checks|statuses)['\"]?\s*:\s*"
    r"['\"]?write['\"]?(?![A-Za-z0-9_-])|"
    r"^\s*permissions\s*:\s*['\"]?write-all['\"]?(?![A-Za-z0-9_-])"
)
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


def workflow_job_scalar_values(job_block: str, key: str) -> tuple[str, ...]:
    return tuple(
        match.group(1).strip("'\"")
        for match in re.finditer(
            rf"^    {re.escape(key)}:\s*(.*?)\s*$",
            job_block,
            flags=re.MULTILINE,
        )
    )


def workflow_job_multiline_block(
    job_block: str,
    key: str,
) -> tuple[tuple[str, ...], list[str]]:
    lines = job_block.splitlines()
    indexes = [
        index
        for index, line in enumerate(lines)
        if re.match(rf"^    {re.escape(key)}:\s*", line)
    ]
    if len(indexes) != 1:
        return (), [f"audit runner must contain exactly one {key} field"]
    block = [lines[indexes[0]]]
    for line in lines[indexes[0] + 1 :]:
        if not line.strip():
            continue
        indent = len(line) - len(line.lstrip(" "))
        if indent <= 4:
            break
        block.append(line.rstrip())
    return tuple(block), []


def canonical_workflow_job_header_sha256(
    job_block: str,
) -> tuple[str, list[str]]:
    lines = job_block.replace("\r\n", "\n").replace("\r", "\n").split("\n")
    indexes = [index for index, line in enumerate(lines) if line == "    steps:"]
    if len(indexes) != 1:
        return "", ["audit runner must contain exactly one steps mapping"]
    header_lines = [line.rstrip() for line in lines[: indexes[0]]]
    while header_lines and not header_lines[0]:
        header_lines.pop(0)
    while header_lines and not header_lines[-1]:
        header_lines.pop()
    payload = ("\n".join(header_lines) + "\n").encode("utf-8")
    return hashlib.sha256(payload).hexdigest(), []


def canonical_workflow_step_sha256(step_block: str) -> str:
    normalized = step_block.replace("\r\n", "\n").replace("\r", "\n")
    lines = [line.rstrip() for line in normalized.split("\n")]
    while lines and not lines[0]:
        lines.pop(0)
    while lines and not lines[-1]:
        lines.pop()
    payload = ("\n".join(lines) + "\n").encode("utf-8")
    return hashlib.sha256(payload).hexdigest()


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


def workflow_exact_mapping(
    text: str,
    section: str,
    *,
    section_indent: int,
    entry_indent: int,
) -> tuple[dict[str, str], list[str]]:
    lines = text.splitlines()
    section_line = f"{' ' * section_indent}{section}:"
    indexes = [index for index, line in enumerate(lines) if line == section_line]
    if len(indexes) != 1:
        return {}, [
            f"workflow must contain exactly one {section} mapping at indent "
            f"{section_indent}"
        ]

    mapping: dict[str, str] = {}
    errors: list[str] = []
    for line in lines[indexes[0] + 1 :]:
        if not line.strip():
            continue
        indent = len(line) - len(line.lstrip(" "))
        if indent <= section_indent:
            break
        match = re.fullmatch(
            rf" {{{entry_indent}}}([A-Za-z0-9_-]+):\s*(.*?)\s*",
            line,
        )
        if not match:
            errors.append(f"{section} mapping contains malformed entry: {line.strip()}")
            continue
        key = match.group(1)
        if key in mapping:
            errors.append(f"{section} mapping contains duplicate key: {key}")
            continue
        mapping[key] = match.group(2).strip("'\"")
    return mapping, errors


def workflow_action_uses(text: str) -> tuple[tuple[str, ...], list[str]]:
    refs: list[str] = []
    errors: list[str] = []
    for line in text.splitlines():
        if not re.match(r"^\s+(?:-\s+)?uses\s*:", line):
            continue
        match = re.fullmatch(r"\s+(?:-\s+)?uses:\s*(.*?)\s*", line)
        if not match or not match.group(1):
            errors.append(f"workflow contains malformed uses entry: {line.strip()}")
            continue
        refs.append(match.group(1).strip("'\""))
    return tuple(refs), errors


def workflow_step_uses(step_block: str) -> str:
    match = re.search(r"^        uses:\s*([^\s#]+)\s*$", step_block, flags=re.MULTILINE)
    return match.group(1) if match else ""


def workflow_step_condition(step_block: str) -> str:
    match = re.search(r"^        if:\s*(.+?)\s*$", step_block, flags=re.MULTILINE)
    return match.group(1) if match else ""


def workflow_step_with_values(
    step_block: str,
) -> tuple[dict[str, str | tuple[str, ...]], list[str]]:
    lines = step_block.splitlines()
    values: dict[str, str | tuple[str, ...]] = {}
    errors: list[str] = []
    try:
        start = lines.index("        with:") + 1
    except ValueError:
        return values, ["workflow step lacks an exact with mapping"]

    index = start
    while index < len(lines):
        line = lines[index]
        if not line.strip():
            index += 1
            continue
        indent = len(line) - len(line.lstrip(" "))
        if indent <= 8:
            break
        match = re.fullmatch(r" {10}([A-Za-z0-9_-]+):\s*(.*?)\s*", line)
        if not match:
            errors.append(f"workflow with mapping has malformed line: {line.strip()}")
            index += 1
            continue
        key, raw_value = match.groups()
        if key in values:
            errors.append(f"workflow with mapping repeats key: {key}")
        if raw_value in {"|", ">"}:
            block_values: list[str] = []
            index += 1
            while index < len(lines):
                block_line = lines[index]
                block_indent = len(block_line) - len(block_line.lstrip(" "))
                if block_line.strip() and block_indent <= 10:
                    break
                if block_line.strip():
                    if block_indent != 12:
                        errors.append(
                            f"workflow block value has unexpected indentation: {key}"
                        )
                    block_values.append(block_line.strip())
                index += 1
            values[key] = tuple(block_values)
            continue
        values[key] = raw_value.strip("'\"")
        index += 1
    return values, errors


def workflow_trigger_paths(text: str, trigger: str) -> tuple[tuple[str, ...], list[str]]:
    lines = text.splitlines()
    trigger_line = f"  {trigger}:"
    indexes = [index for index, line in enumerate(lines) if line == trigger_line]
    if len(indexes) != 1:
        return (), [f"workflow must contain exactly one {trigger} trigger mapping"]
    paths_indexes: list[int] = []
    for index in range(indexes[0] + 1, len(lines)):
        line = lines[index]
        if line and not line.startswith("    "):
            break
        if line == "    paths:":
            paths_indexes.append(index)
    if len(paths_indexes) != 1:
        return (), [f"{trigger} must contain exactly one paths mapping"]
    paths: list[str] = []
    for line in lines[paths_indexes[0] + 1 :]:
        if line and not line.startswith("      "):
            break
        match = re.fullmatch(r" {6}-\s*['\"]?(.+?)['\"]?\s*", line)
        if match:
            paths.append(match.group(1).strip("'\""))
        elif line.strip():
            return (), [f"{trigger} paths contains malformed entry: {line.strip()}"]
    return tuple(paths), []


def validate_pr_safe_base_guard_workflow_text(text: str) -> list[str]:
    errors: list[str] = []
    trigger_paths, trigger_errors = workflow_trigger_paths(
        text,
        "pull_request_target",
    )
    errors.extend(trigger_errors)
    if trigger_paths != PR_SAFE_TRIGGER_PATHS:
        errors.append("pull_request_target paths must match the exact Stage1 path set")
    action_uses, action_errors = workflow_action_uses(text)
    errors.extend(action_errors)
    if action_uses != PR_SAFE_EXPECTED_ACTION_USES:
        errors.append("workflow uses entries must match the exact ordered pinned action set")

    global_permissions, permission_errors = workflow_exact_mapping(
        text,
        "permissions",
        section_indent=0,
        entry_indent=2,
    )
    errors.extend(permission_errors)
    if global_permissions != PR_SAFE_READ_ONLY_PERMISSIONS:
        errors.append("workflow permissions must contain exactly contents: read")

    jobs = workflow_job_blocks(text)
    regular_job = jobs.get("individual-stock-pr-validation", "")
    if not regular_job:
        errors.append("regular individual-stock PR validation job is missing")
    else:
        regular_names = re.findall(
            r"^    name:\s*(.*?)\s*$",
            regular_job,
            flags=re.MULTILINE,
        )
        if regular_names != [PR_SAFE_REGULAR_JOB_NAME_EXPRESSION]:
            errors.append(
                "regular job name must preserve the pull_request required context and "
                "use a distinct pull_request_target skip name"
            )
        regular_timeouts = re.findall(
            r"^    timeout-minutes:\s*(.*?)\s*$",
            regular_job,
            flags=re.MULTILINE,
        )
        if regular_timeouts != ["30"]:
            errors.append("regular individual-stock PR validation job must use timeout-minutes: 30")

    audit_job = jobs.get(PR_SAFE_AUDIT_JOB_NAME, "")
    if not audit_job:
        return [*errors, "base-owned PR-safe audit runner job is missing"]
    audit_header_sha256, audit_header_errors = canonical_workflow_job_header_sha256(
        audit_job
    )
    errors.extend(audit_header_errors)
    if audit_header_sha256 != PR_SAFE_AUDIT_JOB_HEADER_SHA256:
        errors.append("audit runner job header must match the exact canonical contract")
    if workflow_job_scalar_values(audit_job, "name") != (PR_SAFE_AUDIT_JOB_NAME,):
        errors.append("audit runner name must appear once and match its non-required context")
    if workflow_job_scalar_values(audit_job, "runs-on") != (
        PR_SAFE_AUDIT_JOB_RUNS_ON,
    ):
        errors.append("audit runner runs-on must appear once and equal ubuntu-latest")
    if workflow_job_scalar_values(audit_job, "timeout-minutes") != (
        PR_SAFE_AUDIT_JOB_TIMEOUT_MINUTES,
    ):
        errors.append("audit runner timeout-minutes must appear once and equal 10")
    audit_if_block, audit_if_errors = workflow_job_multiline_block(audit_job, "if")
    errors.extend(audit_if_errors)
    if audit_if_block != PR_SAFE_AUDIT_JOB_IF_BLOCK:
        errors.append("audit runner if condition must match the exact base-owned contract")
    audit_permissions, audit_permission_errors = workflow_exact_mapping(
        audit_job,
        "permissions",
        section_indent=4,
        entry_indent=6,
    )
    errors.extend(audit_permission_errors)
    if audit_permissions != PR_SAFE_READ_ONLY_PERMISSIONS:
        errors.append("audit runner permissions must contain exactly contents: read")
    if not re.search(
        r"^    timeout-minutes:\s*10\s*$",
        audit_job,
        flags=re.MULTILINE,
    ):
        errors.append("base-owned PR-safe audit runner must use timeout-minutes: 10")
    steps = workflow_step_blocks(audit_job)
    step_names = tuple(workflow_step_name(step) for step in steps)
    if step_names != PR_SAFE_AUDIT_STEP_NAMES:
        errors.append("audit runner steps must match the exact six-step ordered name contract")
    step_sha256 = tuple(canonical_workflow_step_sha256(step) for step in steps)
    if step_sha256 != PR_SAFE_AUDIT_STEP_SHA256:
        errors.append(
            "audit runner steps must match the exact canonical security contract"
        )
    audit_checkout_steps = [
        step for step in steps if workflow_step_uses(step).startswith("actions/checkout@")
    ]
    if len(audit_checkout_steps) != 1 or workflow_step_uses(
        audit_checkout_steps[0] if audit_checkout_steps else ""
    ) != PR_SAFE_CHECKOUT_ACTION:
        errors.append("audit runner must use exactly one pinned checkout step")

    upload_steps = [
        step
        for step in steps
        if workflow_step_uses(step).startswith("actions/upload-artifact@")
    ]
    if len(upload_steps) != 1:
        errors.append("audit runner must contain exactly one upload-artifact step")
        return errors
    upload_step = upload_steps[0]
    if workflow_step_uses(upload_step) != PR_SAFE_UPLOAD_ARTIFACT_ACTION:
        errors.append("audit evidence upload must use the pinned official action SHA")
    if workflow_step_name(upload_step) != "Upload audit-only evidence":
        errors.append("audit evidence upload step name mismatch")
    if workflow_step_condition(upload_step) != "always()":
        errors.append("audit evidence upload must use if: always()")
    with_values, with_errors = workflow_step_with_values(upload_step)
    errors.extend(with_errors)
    expected_with: dict[str, str | tuple[str, ...]] = {
        "name": PR_SAFE_AUDIT_ARTIFACT_NAME,
        "path": PR_SAFE_AUDIT_ARTIFACT_PATHS,
        "if-no-files-found": "error",
        "retention-days": PR_SAFE_AUDIT_RETENTION_DAYS,
    }
    if with_values != expected_with:
        errors.append("audit evidence upload with mapping must match the exact contract")
    required_sidecar_lines = (
        'manifest_name="$(basename "$AUDIT_MANIFEST")"',
        '(cd "$manifest_dir" && sha256sum "$manifest_name" > '
        '"${manifest_name}.sha256")',
    )
    if not all(line in audit_job for line in required_sidecar_lines):
        errors.append("audit SHA-256 sidecar must reference the manifest basename")
    return errors


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


def canonical_blob_sha256(payload: bytes) -> str:
    canonical = payload.replace(b"\r\n", b"\n").replace(b"\r", b"\n")
    return hashlib.sha256(canonical).hexdigest()


def parse_pr_safe_authorizations(payload: bytes) -> tuple[list[dict[str, str]], list[str]]:
    try:
        reader = csv.DictReader(io.StringIO(payload.decode("utf-8-sig"), newline=""))
    except UnicodeError as exc:
        return [], [f"cannot decode PR-safe authorization ledger: {exc}"]
    if tuple(reader.fieldnames or ()) != PR_SAFE_AUTHORIZATION_COLUMNS:
        return [], ["PR-safe authorization ledger header mismatch"]
    rows: list[dict[str, str]] = []
    try:
        for line_number, row in enumerate(reader, start=2):
            if None in row:
                return [], [
                    f"PR-safe authorization ledger row has extra fields: {line_number}"
                ]
            rows.append({str(key): str(value or "") for key, value in row.items()})
    except csv.Error as exc:
        return [], [f"cannot parse PR-safe authorization ledger: {exc}"]
    migration_ids = [row.get("migration_id", "").strip() for row in rows]
    if any(not migration_id for migration_id in migration_ids) or len(
        migration_ids
    ) != len(set(migration_ids)):
        return [], ["PR-safe authorization migration ids must be nonblank and unique"]
    return rows, []


def validate_pr_safe_authorization_history(
    rows: list[dict[str, str]],
) -> list[str]:
    retained = list(PR_SAFE_RETAINED_AUTHORIZATION_ROWS)
    if rows[: len(retained)] != retained:
        return [
            "PR-safe authorization history must retain the exact append-only prefix"
        ]
    return []


def parse_pr_safe_lifecycle_authorizations(
    payload: bytes,
) -> tuple[list[dict[str, str]], list[str]]:
    try:
        reader = csv.DictReader(io.StringIO(payload.decode("utf-8-sig"), newline=""))
    except UnicodeError as exc:
        return [], [f"cannot decode lifecycle authorization ledger: {exc}"]
    if tuple(reader.fieldnames or ()) != PR_SAFE_LIFECYCLE_AUTHORIZATION_COLUMNS:
        return [], ["lifecycle authorization ledger header mismatch"]

    rows: list[dict[str, str]] = []
    errors: list[str] = []
    try:
        for line_number, row in enumerate(reader, start=2):
            if None in row:
                errors.append(
                    "lifecycle authorization ledger row has extra fields: "
                    f"{line_number}"
                )
                continue
            normalized = {str(key): str(value or "").strip() for key, value in row.items()}
            rows.append(normalized)
    except csv.Error as exc:
        return [], [f"cannot parse lifecycle authorization ledger: {exc}"]

    migration_ids = [row.get("migration_id", "") for row in rows]
    if any(not migration_id for migration_id in migration_ids) or len(
        migration_ids
    ) != len(set(migration_ids)):
        errors.append("lifecycle authorization migration ids must be nonblank and unique")

    observed_targets: list[tuple[str, str]] = []
    for row in rows:
        target = (
            row.get("row_path", "").replace("\\", "/"),
            row.get("column", ""),
        )
        observed_targets.append(target)
        if row.get("status", "") != PR_SAFE_LIFECYCLE_AUTHORIZATION_STATUS:
            errors.append(
                "lifecycle authorization status must be preauthorized: "
                + row.get("migration_id", "")
            )
        if row.get("scope", "") != PR_SAFE_LIFECYCLE_AUTHORIZATION_SCOPE:
            errors.append(
                "lifecycle authorization scope mismatch: "
                + row.get("migration_id", "")
            )
        if not row.get("approval_reference", ""):
            errors.append(
                "lifecycle authorization lacks approval_reference: "
                + row.get("migration_id", "")
            )
        for field in ("base_value_sha256", "current_value_sha256"):
            if not re.fullmatch(r"[0-9a-f]{64}", row.get(field, "")):
                errors.append(
                    f"lifecycle authorization {field} is not canonical SHA-256: "
                    + row.get("migration_id", "")
                )
        added_values = [
            value for value in row.get("added_values", "").split(";") if value
        ]
        removed_values = [
            value for value in row.get("removed_values", "").split(";") if value
        ]
        if added_values != sorted(set(added_values)):
            errors.append(
                "lifecycle authorization added_values must be sorted and unique: "
                + row.get("migration_id", "")
            )
        if removed_values != sorted(set(removed_values)):
            errors.append(
                "lifecycle authorization removed_values must be sorted and unique: "
                + row.get("migration_id", "")
            )
        if not added_values and not removed_values:
            errors.append(
                "lifecycle authorization must describe a semantic delta: "
                + row.get("migration_id", "")
            )
        if set(added_values) & set(removed_values):
            errors.append(
                "lifecycle authorization added/removed values overlap: "
                + row.get("migration_id", "")
            )

    if len(observed_targets) != len(set(observed_targets)):
        errors.append("lifecycle authorization targets must be unique")
    if set(observed_targets) != PR_SAFE_LIFECYCLE_AUTHORIZED_TARGETS:
        errors.append("lifecycle authorization target set mismatch")
    return rows, errors


def validate_pr_safe_control_plane_delta(
    changed_paths: set[str],
    *,
    base_helper: bytes | None,
    current_helper: bytes | None,
    current_test: bytes | None,
    authorization_payload: bytes,
    changed_workflow_blobs: dict[str, bytes | None] | None = None,
) -> list[str]:
    errors: list[str] = []
    immutable_changes = sorted(changed_paths & PR_SAFE_IMMUTABLE_TRUST_ROOT_PATHS)
    if immutable_changes:
        errors.append(
            "PR may not modify the base-owned PR-safe trust root: "
            + ", ".join(immutable_changes)
        )

    for path, payload in sorted((changed_workflow_blobs or {}).items()):
        if payload is None:
            continue
        try:
            workflow_text = payload.decode("utf-8-sig")
        except UnicodeError:
            errors.append(f"cannot decode changed workflow for spoof audit: {path}")
            continue
        if PR_SAFE_FORBIDDEN_WRITE_PERMISSION_RE.search(workflow_text):
            errors.append(
                "changed workflow requests checks/statuses write permission: " + path
            )

    protected_changes = changed_paths & PR_SAFE_AUTHORIZED_STAGE1_PATHS
    if not protected_changes:
        return errors
    if changed_paths != PR_SAFE_AUTHORIZED_STAGE1_PATHS:
        errors.append(
            "PR-safe helper migration must change exactly the preauthorized paths: "
            + ", ".join(sorted(PR_SAFE_AUTHORIZED_STAGE1_PATHS))
        )
        return errors

    authorizations, authorization_errors = parse_pr_safe_authorizations(
        authorization_payload
    )
    errors.extend(authorization_errors)
    errors.extend(validate_pr_safe_authorization_history(authorizations))
    matching = [
        row
        for row in authorizations
        if row.get("migration_id", "").strip()
        == PR_SAFE_ADDITIVE_RESEARCH_MIGRATION_ID
    ]
    if len(matching) != 1:
        errors.append(
            "base authorization ledger must contain exactly one matching PR-safe migration"
        )
        return errors
    authorization = matching[0]
    if base_helper is None or current_helper is None or current_test is None:
        errors.append("preauthorized PR-safe helper/test blobs must all exist")
        return errors

    observed_paths = {
        path.strip()
        for path in authorization.get("changed_paths", "").split(";")
        if path.strip()
    }
    expected = {
        "base_helper_sha256": canonical_blob_sha256(base_helper),
        "current_helper_sha256": canonical_blob_sha256(current_helper),
        "current_test_sha256": canonical_blob_sha256(current_test),
    }
    if authorization.get("status", "").strip() != "preauthorized":
        errors.append("PR-safe migration authorization status is not preauthorized")
    if not authorization.get("approval_reference", "").strip():
        errors.append("PR-safe migration authorization lacks approval_reference")
    if observed_paths != PR_SAFE_AUTHORIZED_STAGE1_PATHS:
        errors.append("PR-safe migration authorization changed_paths mismatch")
    for field, observed in expected.items():
        if authorization.get(field, "").strip() != observed:
            errors.append(f"PR-safe migration authorization {field} mismatch")
    marker = PR_SAFE_ADDITIVE_RESEARCH_MIGRATION_ID.encode("utf-8")
    if marker in base_helper:
        errors.append("PR-safe migration was already consumed by the base helper")
    if marker not in current_helper:
        errors.append("PR-safe migration id is absent from the current helper")
    return errors


def git_output_bytes(*args: str) -> bytes:
    result = subprocess.run(
        ["git", *args],
        cwd=ROOT,
        check=False,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    if result.returncode != 0:
        message = result.stderr.decode("utf-8", errors="replace").strip()
        raise RuntimeError(f"git {' '.join(args)} failed: {message}")
    return result.stdout


def git_blob_at_ref(ref: str, path: str) -> bytes | None:
    try:
        return git_output_bytes("show", f"{ref}:{path}")
    except RuntimeError:
        return None


def parse_git_name_status_z(payload: bytes) -> tuple[set[str], list[str]]:
    fields = payload.split(b"\0")
    if fields and fields[-1] == b"":
        fields.pop()
    paths: set[str] = set()
    errors: list[str] = []
    index = 0
    while index < len(fields):
        try:
            status = fields[index].decode("ascii")
        except UnicodeError:
            errors.append("git name-status output contains a non-ASCII status")
            break
        index += 1
        if not re.fullmatch(r"[ACDMRT][0-9]*", status):
            errors.append(f"git name-status output has unsupported status: {status!r}")
            break
        path_count = 2 if status[0] in {"R", "C"} else 1
        if index + path_count > len(fields):
            errors.append(f"git name-status output is truncated after status {status}")
            break
        for raw_path in fields[index : index + path_count]:
            try:
                path = raw_path.decode("utf-8").replace("\\", "/")
            except UnicodeError:
                errors.append(
                    f"git name-status output contains a non-UTF-8 path for {status}"
                )
                continue
            if not path:
                errors.append(f"git name-status output has a blank path for {status}")
            else:
                paths.add(path)
        index += path_count
    return paths, errors


def git_tree_entry_at_ref(ref: str, path: str) -> tuple[str, str, str, str] | None:
    payload = git_output_bytes("ls-tree", "-z", ref, "--", path)
    entries = [entry for entry in payload.split(b"\0") if entry]
    if not entries:
        return None
    if len(entries) != 1 or b"\t" not in entries[0]:
        raise RuntimeError(f"git ls-tree returned ambiguous evidence for {ref}:{path}")
    metadata, raw_path = entries[0].split(b"\t", 1)
    metadata_fields = metadata.decode("ascii").split()
    if len(metadata_fields) != 3:
        raise RuntimeError(f"git ls-tree returned malformed metadata for {ref}:{path}")
    try:
        observed_path = raw_path.decode("utf-8").replace("\\", "/")
    except UnicodeError as exc:
        raise RuntimeError(f"git ls-tree returned a non-UTF-8 path for {ref}:{path}") from exc
    mode, object_type, object_id = metadata_fields
    return mode, object_type, object_id, observed_path


def validate_pr_safe_regular_blob_modes(
    base_sha: str,
    head_sha: str,
) -> list[str]:
    errors: list[str] = []
    protected_paths = (
        PR_SAFE_IMMUTABLE_TRUST_ROOT_PATHS | PR_SAFE_AUTHORIZED_STAGE1_PATHS
    )
    for ref_label, ref in (("base", base_sha), ("head", head_sha)):
        for path in sorted(protected_paths):
            try:
                entry = git_tree_entry_at_ref(ref, path)
            except RuntimeError as exc:
                errors.append(str(exc))
                continue
            if entry is None:
                errors.append(
                    f"PR-safe protected path is missing from {ref_label}: {path}"
                )
                continue
            mode, object_type, _object_id, observed_path = entry
            if (
                observed_path != path
                or object_type != "blob"
                or mode not in PR_SAFE_REGULAR_BLOB_MODES
            ):
                errors.append(
                    "PR-safe protected path must remain a regular blob: "
                    f"ref={ref_label} path={path} mode={mode} type={object_type} "
                    f"observed_path={observed_path}"
                )
    return errors


def validate_pr_safe_control_plane_migration(base_sha: str, head_sha: str) -> list[str]:
    errors: list[str] = []
    if not re.fullmatch(r"[0-9a-fA-F]{40}", base_sha):
        return [f"invalid base SHA: {base_sha!r}"]
    if not re.fullmatch(r"[0-9a-fA-F]{40}", head_sha):
        return [f"invalid head SHA: {head_sha!r}"]
    try:
        checkout_sha = git_output_bytes("rev-parse", "HEAD").decode().strip()
        if checkout_sha.lower() != base_sha.lower():
            errors.append(
                "base-owned guard checkout does not match pull request base SHA: "
                f"checkout={checkout_sha} base={base_sha}"
            )
        diff_payload = git_output_bytes(
            "diff",
            "--name-status",
            "-z",
            "--find-renames",
            "--find-copies",
            "--diff-filter=ACDMRT",
            f"{base_sha}...{head_sha}",
            "--",
        )
        changed_paths, diff_errors = parse_git_name_status_z(diff_payload)
        errors.extend(diff_errors)
        if changed_paths != PR_SAFE_AUTHORIZED_STAGE1_PATHS:
            errors.append(
                "PR-safe audit requires exactly the preauthorized changed paths: "
                + ", ".join(sorted(PR_SAFE_AUTHORIZED_STAGE1_PATHS))
            )
        authorization_payload = git_blob_at_ref(base_sha, PR_SAFE_AUTHORIZATION_PATH)
        lifecycle_authorization_payload = git_blob_at_ref(
            base_sha,
            PR_SAFE_LIFECYCLE_AUTHORIZATION_PATH,
        )
    except (OSError, RuntimeError) as exc:
        return [*errors, f"cannot load base-owned PR-safe evidence: {exc}"]

    errors.extend(validate_pr_safe_regular_blob_modes(base_sha, head_sha))
    if authorization_payload is None:
        errors.append("base-owned PR-safe authorization ledger is missing")
        authorization_payload = b""
    if lifecycle_authorization_payload is None:
        errors.append("base-owned lifecycle authorization ledger is missing")
    else:
        _rows, lifecycle_errors = parse_pr_safe_lifecycle_authorizations(
            lifecycle_authorization_payload
        )
        errors.extend(lifecycle_errors)

    errors.extend(
        validate_pr_safe_control_plane_delta(
            changed_paths,
            base_helper=git_blob_at_ref(base_sha, PR_SAFE_ADVANCED_HELPER),
            current_helper=git_blob_at_ref(head_sha, PR_SAFE_ADVANCED_HELPER),
            current_test=git_blob_at_ref(head_sha, PR_SAFE_ADVANCED_TEST),
            authorization_payload=authorization_payload,
            changed_workflow_blobs={
                path: git_blob_at_ref(head_sha, path)
                for path in changed_paths
                if path.startswith(".github/workflows/")
                and Path(path).suffix in {".yml", ".yaml"}
            },
        )
    )
    return errors


def _positive_integer(value: str, label: str, errors: list[str]) -> int | None:
    if not re.fullmatch(r"[1-9][0-9]*", value):
        errors.append(f"audit metadata {label} must be a positive integer")
        return None
    return int(value)


def _pr_safe_blob_evidence(ref: str, path: str) -> dict[str, str | None]:
    entry = git_tree_entry_at_ref(ref, path)
    payload = git_blob_at_ref(ref, path)
    if entry is None or payload is None:
        return {
            "path": path,
            "mode": None,
            "object_type": None,
            "object_id": None,
            "raw_sha256": None,
            "canonical_sha256": None,
        }
    mode, object_type, object_id, observed_path = entry
    return {
        "path": observed_path,
        "mode": mode,
        "object_type": object_type,
        "object_id": object_id,
        "raw_sha256": hashlib.sha256(payload).hexdigest(),
        "canonical_sha256": canonical_blob_sha256(payload),
    }


def build_pr_safe_audit_manifest(
    *,
    base_sha: str,
    head_sha: str,
    validation_errors: list[str],
    repository: str,
    workflow_ref: str,
    workflow_sha: str,
    run_id: str,
    run_attempt: str,
    event_name: str,
    event_action: str,
    base_ref: str,
    base_repository: str,
    head_repository: str,
    pull_request_number: str,
) -> dict[str, object]:
    errors = list(validation_errors)
    if repository != PR_SAFE_REPOSITORY:
        errors.append(
            f"audit metadata repository mismatch: {repository!r}"
        )
    if event_name != "pull_request_target":
        errors.append(
            f"audit metadata event_name must be pull_request_target: {event_name!r}"
        )
    if event_action not in PR_SAFE_ALLOWED_EVENT_ACTIONS:
        errors.append(f"audit metadata event_action is not allowed: {event_action!r}")
    if base_ref != "main":
        errors.append(f"audit metadata base_ref must be main: {base_ref!r}")
    if base_repository != PR_SAFE_REPOSITORY:
        errors.append(
            f"audit metadata base_repository mismatch: {base_repository!r}"
        )
    if not re.fullmatch(r"[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+", head_repository):
        errors.append(
            f"audit metadata head_repository is malformed: {head_repository!r}"
        )
    if workflow_ref != PR_SAFE_EXPECTED_WORKFLOW_REF:
        errors.append(
            "audit metadata workflow_ref must identify the exact main workflow ref"
        )
    if workflow_sha.lower() != base_sha.lower():
        errors.append(
            "audit metadata workflow_sha must equal the pull request base SHA"
        )
    parsed_run_id = _positive_integer(run_id, "run_id", errors)
    parsed_run_attempt = _positive_integer(run_attempt, "run_attempt", errors)
    if parsed_run_attempt is not None and parsed_run_attempt != 1:
        errors.append("audit metadata run_attempt must be 1; reruns are not eligible")
    parsed_pr_number = _positive_integer(
        pull_request_number,
        "pull_request_number",
        errors,
    )

    changed_paths: set[str] = set()
    try:
        diff_payload = git_output_bytes(
            "diff",
            "--name-status",
            "-z",
            "--find-renames",
            "--find-copies",
            "--diff-filter=ACDMRT",
            f"{base_sha}...{head_sha}",
            "--",
        )
        changed_paths, diff_errors = parse_git_name_status_z(diff_payload)
        errors.extend(diff_errors)
        if changed_paths != PR_SAFE_AUTHORIZED_STAGE1_PATHS:
            errors.append(
                "audit manifest changed paths do not match the exact preauthorization"
            )
        checkout_sha = git_output_bytes("rev-parse", "HEAD").decode().strip()
    except (OSError, RuntimeError, UnicodeError) as exc:
        errors.append(f"cannot collect audit Git evidence: {exc}")
        checkout_sha = ""

    authorization_payload = git_blob_at_ref(base_sha, PR_SAFE_AUTHORIZATION_PATH)
    lifecycle_payload = git_blob_at_ref(
        base_sha,
        PR_SAFE_LIFECYCLE_AUTHORIZATION_PATH,
    )
    authorization_rows: list[dict[str, str]] = []
    lifecycle_rows: list[dict[str, str]] = []
    if authorization_payload is not None:
        authorization_rows, authorization_errors = parse_pr_safe_authorizations(
            authorization_payload
        )
        errors.extend(authorization_errors)
    if lifecycle_payload is not None:
        lifecycle_rows, lifecycle_errors = parse_pr_safe_lifecycle_authorizations(
            lifecycle_payload
        )
        errors.extend(lifecycle_errors)

    matching_authorizations = [
        row
        for row in authorization_rows
        if row.get("migration_id", "").strip()
        == PR_SAFE_ADDITIVE_RESEARCH_MIGRATION_ID
    ]
    migration = matching_authorizations[0] if len(matching_authorizations) == 1 else {}
    protected_blobs = {
        path: {
            "base": _pr_safe_blob_evidence(base_sha, path),
            "head": _pr_safe_blob_evidence(head_sha, path),
        }
        for path in sorted(
            PR_SAFE_IMMUTABLE_TRUST_ROOT_PATHS | PR_SAFE_AUTHORIZED_STAGE1_PATHS
        )
    }
    unique_errors = list(dict.fromkeys(errors))
    return {
        "schema_version": PR_SAFE_AUDIT_MANIFEST_SCHEMA_VERSION,
        "audit_mode": PR_SAFE_AUDIT_MODE,
        "trust_identity_claimed": False,
        "required_context_used": False,
        "workflow_path": PR_SAFE_BASE_GUARD_WORKFLOW,
        "repository": repository,
        "workflow_ref": workflow_ref,
        "workflow_sha": workflow_sha.lower(),
        "event_name": event_name,
        "event_action": event_action,
        "base_ref": base_ref,
        "base_repository": base_repository,
        "head_repository": head_repository,
        "run_id": parsed_run_id,
        "run_attempt": parsed_run_attempt,
        "pull_request_number": parsed_pr_number,
        "base_sha": base_sha.lower(),
        "head_sha": head_sha.lower(),
        "checkout_sha": checkout_sha.lower(),
        "changed_paths": sorted(changed_paths),
        "changed_path_allowlist": sorted(PR_SAFE_AUTHORIZED_STAGE1_PATHS),
        "changed_paths_match_allowlist": changed_paths
        == PR_SAFE_AUTHORIZED_STAGE1_PATHS,
        "manual_gate_eligible": not unique_errors
        and changed_paths == PR_SAFE_AUTHORIZED_STAGE1_PATHS,
        "preauthorization": {
            "path": PR_SAFE_AUTHORIZATION_PATH,
            "canonical_sha256": (
                canonical_blob_sha256(authorization_payload)
                if authorization_payload is not None
                else None
            ),
            "migration": migration,
        },
        "lifecycle_preauthorization": {
            "path": PR_SAFE_LIFECYCLE_AUTHORIZATION_PATH,
            "canonical_sha256": (
                canonical_blob_sha256(lifecycle_payload)
                if lifecycle_payload is not None
                else None
            ),
            "migrations": lifecycle_rows,
        },
        "protected_blobs": protected_blobs,
        "validation": {
            "passed": not unique_errors,
            "errors": unique_errors,
        },
    }


def write_pr_safe_audit_manifest(
    manifest: dict[str, object],
    destination: Path,
) -> str:
    payload = (
        json.dumps(manifest, ensure_ascii=False, indent=2, sort_keys=True) + "\n"
    ).encode("utf-8")
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_bytes(payload)
    return hashlib.sha256(payload).hexdigest()


def validate_pr_safe_base_guard_repository_invariants(
    workflow_paths: set[str],
    errors: list[str],
) -> None:
    try:
        authorization_payload = (ROOT / PR_SAFE_AUTHORIZATION_PATH).read_bytes()
    except OSError as exc:
        errors.append(f"cannot read PR-safe authorization ledger: {exc}")
    else:
        authorization_rows, authorization_errors = parse_pr_safe_authorizations(
            authorization_payload
        )
        errors.extend(authorization_errors)
        errors.extend(validate_pr_safe_authorization_history(authorization_rows))

    try:
        lifecycle_payload = (ROOT / PR_SAFE_LIFECYCLE_AUTHORIZATION_PATH).read_bytes()
    except OSError as exc:
        errors.append(f"cannot read lifecycle authorization ledger: {exc}")
    else:
        _rows, lifecycle_errors = parse_pr_safe_lifecycle_authorizations(
            lifecycle_payload
        )
        errors.extend(lifecycle_errors)

    write_permission_owners: list[str] = []
    for path in sorted(workflow_paths):
        try:
            text = (ROOT / path).read_text(encoding="utf-8")
        except (OSError, UnicodeError) as exc:
            errors.append(f"cannot read workflow for PR-safe collision audit: {path}: {exc}")
            continue
        if PR_SAFE_FORBIDDEN_WRITE_PERMISSION_RE.search(text):
            write_permission_owners.append(path)

    if write_permission_owners:
        errors.append(
            "audit-only workflows may not request checks/statuses write permission: "
            + ", ".join(write_permission_owners)
        )
    try:
        guard_text = (ROOT / PR_SAFE_BASE_GUARD_WORKFLOW).read_text(encoding="utf-8")
    except (OSError, UnicodeError):
        return
    if "pull_request_target:" not in guard_text:
        errors.append("base-owned PR-safe audit workflow must use pull_request_target")
    if "actions/github-script" in guard_text:
        errors.append("audit-only PR-safe workflow may not use actions/github-script")
    errors.extend(validate_pr_safe_base_guard_workflow_text(guard_text))


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
    validate_pr_safe_base_guard_repository_invariants(workflow_paths, errors)
    return errors


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--validate-pr-safe-control-plane-migration",
        action="store_true",
    )
    parser.add_argument("--base-sha", default="")
    parser.add_argument("--head-sha", default="")
    parser.add_argument("--audit-manifest", default="")
    parser.add_argument("--repository", default="")
    parser.add_argument("--workflow-ref", default="")
    parser.add_argument("--workflow-sha", default="")
    parser.add_argument("--run-id", default="")
    parser.add_argument("--run-attempt", default="")
    parser.add_argument("--event-name", default="")
    parser.add_argument("--event-action", default="")
    parser.add_argument("--base-ref", default="")
    parser.add_argument("--base-repository", default="")
    parser.add_argument("--head-repository", default="")
    parser.add_argument("--pull-request-number", default="")
    args = parser.parse_args(argv or [])
    if args.validate_pr_safe_control_plane_migration:
        errors = validate_pr_safe_control_plane_migration(
            args.base_sha.strip(),
            args.head_sha.strip(),
        )
        if args.audit_manifest:
            manifest = build_pr_safe_audit_manifest(
                base_sha=args.base_sha.strip(),
                head_sha=args.head_sha.strip(),
                validation_errors=errors,
                repository=args.repository.strip(),
                workflow_ref=args.workflow_ref.strip(),
                workflow_sha=args.workflow_sha.strip(),
                run_id=args.run_id.strip(),
                run_attempt=args.run_attempt.strip(),
                event_name=args.event_name.strip(),
                event_action=args.event_action.strip(),
                base_ref=args.base_ref.strip(),
                base_repository=args.base_repository.strip(),
                head_repository=args.head_repository.strip(),
                pull_request_number=args.pull_request_number.strip(),
            )
            errors = list(manifest["validation"]["errors"])
            manifest_path = Path(args.audit_manifest).resolve()
            manifest_sha256 = write_pr_safe_audit_manifest(manifest, manifest_path)
            print(f"audit_manifest={manifest_path}")
            print(f"audit_manifest_sha256={manifest_sha256}")
        if errors:
            for error in errors:
                print(f"ERROR: {error}")
            return 1
        print("base-owned PR-safe control-plane audit validation passed")
        print(f"audit_mode={PR_SAFE_AUDIT_MODE}")
        print(f"head_sha={args.head_sha.strip()}")
        return 0

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
    raise SystemExit(main(sys.argv[1:]))
