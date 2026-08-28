from __future__ import annotations

import argparse
import csv
import fnmatch
import io
import json
import subprocess
import tokenize
from dataclasses import dataclass
from pathlib import Path
from typing import Callable, Iterable, Mapping, Sequence


ROOT = Path(__file__).resolve().parents[1]

SHARED_REGISTRY_KEY_FIELDS = {
    "config/repo_file_lifecycle_inventory.csv": "path",
    "config/repo_production_inventory.csv": "path",
    "config/report_artifact_lineage.csv": "artifact_path",
    "config/runtime_file_lineage_contract.csv": "script_path",
}

REPO_CURRENT_CONTRACTS = "repo-current-contracts"
PRODUCTION_PDF_CONTRACTS = "production-pdf-contracts"
RESEARCH_SAFETY_LITE = "research-safety-lite"
SHARED_MODEL_RESEARCH = "shared-model-research"
VOLUME_V2_RESEARCH = "volume-v2-research"
REVENUE_RESEARCH = "revenue-research"
FINANCIAL_STATEMENT_RESEARCH = "financial-statement-research"

DOMAINS = (
    REPO_CURRENT_CONTRACTS,
    PRODUCTION_PDF_CONTRACTS,
    RESEARCH_SAFETY_LITE,
    SHARED_MODEL_RESEARCH,
    VOLUME_V2_RESEARCH,
    REVENUE_RESEARCH,
    FINANCIAL_STATEMENT_RESEARCH,
)

DOMAIN_OUTPUTS = {
    REPO_CURRENT_CONTRACTS: "repo_current_contracts",
    PRODUCTION_PDF_CONTRACTS: "production_pdf_contracts",
    RESEARCH_SAFETY_LITE: "research_safety_lite",
    SHARED_MODEL_RESEARCH: "shared_model_research",
    VOLUME_V2_RESEARCH: "volume_v2_research",
    REVENUE_RESEARCH: "revenue_research",
    FINANCIAL_STATEMENT_RESEARCH: "financial_statement_research",
}

# These patterns declare the existing Daily Model-owned validation universe. The
# workflow intentionally runs a cheap scope job for every pull request, so paths
# outside this tuple fast-pass without starting domain jobs. A narrow
# MODEL_LIKE_MARKERS safety net catches newly named Daily Model paths and fails
# closed until their domain is declared.
WATCHED_PATH_PATTERNS = (
    ".github/workflows/daily_full_pipeline.yml",
    ".github/workflows/daily_model_maintenance_pr_validation.yml",
    ".github/workflows/daily_pdf_replay_pr_validation.yml",
    ".github/workflows/warrant_flow.yml",
    ".github/workflows/event_catalyst_update.yml",
    ".github/workflows/research_backtest_pipeline.yml",
    ".github/workflows/weekly_theme_review.yml",
    "config/repo_file_lifecycle_inventory.csv",
    "config/repo_production_inventory.csv",
    "config/formal_model_evidence_pins.csv",
    "config/historical_replay_semantic_contract.csv",
    "config/git_worktree_materialization_contract.csv",
    "config/model_research_*.csv",
    "config/daily_model_*.csv",
    "config/revenue_unreacted_range_*.csv",
    "data/financial_statement_history/*.csv",
    "config/daily_pdf_rendered_model_regression_contract.csv",
    "config/daily_pdf_semantic_golden_cases.csv",
    "config/daily_pdf_shared_path_inventory.csv",
    "config/repo_hidden_coupling_audit.csv",
    "config/model_surface_registry.csv",
    "config/report_artifact_lineage.csv",
    "config/runtime_file_lineage_contract.csv",
    "config/stock_model_contract_registry.csv",
    "AGENTS.md",
    "rules/master_priority_rules.md",
    "docs/rules/master_priority_rules.md",
    "docs/latest/model_data_independence_audit_latest.*",
    "docs/latest/financial_statement_pit_coverage_latest.*",
    "docs/latest/financial_statement_historical_pit_source_audit_latest.*",
    "docs/latest/volume_v2_warrant_lineage_history_audit_latest.*",
    "output/latest/model_data_independence_audit_latest.*",
    "output/latest/research_backtest/financial_statement_pit_coverage_latest.*",
    "output/latest/research_backtest/financial_statement_historical_pit_source_audit_latest.*",
    "output/latest/volume_v2_warrant_lineage_history_audit_latest.*",
    "output/latest/daily_report_model_registry_latest.csv",
    "output/latest/model_operation_readiness_latest.csv",
    "output/latest/daily_candidate_model_signals_for_report_latest.csv",
    "output/latest/daily_candidate_model_signals_latest.csv",
    "output/latest/approved_operation_patterns_latest.csv",
    "output/latest/model_contract_parity_latest.csv",
    "output/latest/daily_w_bottom_right_side_operation_section_latest.csv",
    "output/latest/daily_price_pullback_23ema_operation_section_latest.csv",
    "output/latest/chatgpt_daily_report_packet_latest.txt",
    "output/latest/CHATGPT_DAILY_REPORT_PACKET.txt",
    "docs/latest/chatgpt_daily_report_packet_latest.txt",
    "docs/specs/*operation*.md",
    "docs/specs/revenue_unreacted_range_*.md",
    "docs/specs/daily_mature_model_row_level_metric_contract.md",
    "docs/repo_hidden_coupling_audit.md",
    "docs/rules/git_worktree_materialization_safety.md",
    "scripts/detect_daily_model_pr_validation_scope.py",
    "scripts/validate_repo_file_lifecycle_inventory.py",
    "scripts/validate_repo_production_inventory.py",
    "scripts/validate_chatgpt_side_pdf_layout_independence.py",
    "scripts/build_daily_*model*.py",
    "scripts/build_daily_*operation*.py",
    "scripts/build_daily_published_snapshot_ranking_backtest.py",
    "scripts/daily_snapshot_revision_utils.py",
    "scripts/stage_daily_published_snapshot_revisions.py",
    "scripts/backfill_historical_all_candidates_snapshots_from_git_history.py",
    "scripts/build_monthly_revenue_coverage_backfill_audit.py",
    "scripts/build_monthly_revenue_point_in_time_panel.py",
    "scripts/build_daily_report_model_summary.py",
    "scripts/build_approved_operation_patterns.py",
    "scripts/audit_daily_candidate_model_selection_correctness.py",
    "build_chatgpt_daily_report_packet.py",
    "scripts/build_model_operation_readiness.py",
    "scripts/build_model_data_independence_audit.py",
    "scripts/build_financial_statement_pit.py",
    "scripts/build_financial_statement_historical_pit_source_audit.py",
    "scripts/build_volume_breakout_watch.py",
    "scripts/build_volume_attack_theme_layer.py",
    "scripts/build_volume_v2_warrant_lineage_history_audit.py",
    "scripts/model_data_independence.py",
    "scripts/build_*_research.py",
    "scripts/price_pullback_23ema_*.py",
    "scripts/revenue_unreacted_range_*.py",
    "scripts/validate_revenue_unreacted_range_*.py",
    "scripts/volume_range_breakout_v2_*.py",
    "scripts/build_mature_model_row_level_metric_contract_audit.py",
    "scripts/generate_chatgpt_side_daily_reports.py",
    "scripts/git_worktree_safety.py",
    "scripts/resolve_daily_report_source_state.py",
    "scripts/run_chatgpt_daily_report_entrypoint.py",
    "scripts/stage_daily_latest_mirrors.py",
    "scripts/validate_chatgpt_side_pdf_contract.py",
    "scripts/update_daily_published_model_snapshots.py",
    "scripts/validate_chatgpt_daily_report_new_conversation_replay.py",
    "scripts/validate_daily_*.py",
    "scripts/validate_model_operation_readiness.py",
    "scripts/validate_model_data_independence.py",
    "scripts/validate_research_production_boundaries.py",
    "scripts/validate_financial_statement_pit.py",
    "scripts/validate_financial_statement_historical_pit_source_audit.py",
    "scripts/validate_volume_breakout_watch.py",
    "scripts/validate_volume_attack_theme_layer.py",
    "scripts/validate_volume_v2_warrant_lineage_history_audit.py",
    "scripts/validate_model_surface_registry.py",
    "scripts/validate_model_research_*.py",
    "scripts/validate_mature_model_row_level_metric_contract_audit.py",
    "scripts/validate_daily_legacy_volume_range_breakout_removed.py",
    "scripts/validate_research_against_stock_model_contract.py",
    "scripts/validate_repo_hidden_coupling_audit.py",
    "scripts/validate_git_worktree_safety.py",
    "scripts/validate_repo_code_isolation_policy.py",
    "scripts/validate_repo_advanced_integrity.py",
    "scripts/validate_repo_advanced_integrity_pr_safe.py",
    "scripts/validate_stock_model_contract_registry.py",
    "scripts/validate_warrant_source_status.py",
    "tests/test_chatgpt_daily_report_new_conversation_replay.py",
    "tests/test_chatgpt_daily_report_entrypoint.py",
    "tests/test_chatgpt_side_pdf_contract.py",
    "tests/test_catalyst_pages_sync.py",
    "tests/test_daily_*.py",
    "tests/test_daily_snapshot_revision_utils.py",
    "tests/test_stage_daily_published_snapshot_revisions.py",
    "tests/test_backfill_historical_all_candidates_snapshots.py",
    "tests/test_warrant_source_status.py",
    "tests/test_repo_hidden_coupling_audit.py",
    "tests/test_git_worktree_safety.py",
    "tests/test_model_operation_readiness.py",
    "tests/test_model_data_independence.py",
    "tests/test_financial_statement_pit.py",
    "tests/test_financial_statement_historical_pit_source_audit.py",
    "tests/test_volume_breakout_watch.py",
    "tests/test_daily_canonical_field_lineage.py",
    "tests/test_daily_model_maintenance_pr_validation_workflow.py",
    "tests/test_detect_daily_model_pr_validation_scope.py",
    "tests/test_volume_v2_warrant_lineage_history_audit.py",
    "tests/test_model_surface_registry.py",
    "tests/test_repo_code_isolation_policy.py",
    "tests/test_model_research_*.py",
    "tests/test_price_pullback_23ema_*.py",
    "tests/test_price_pullback_daily_row_parity.py",
    "tests/test_monthly_revenue_point_in_time_panel.py",
    "tests/test_repo_advanced_integrity.py",
    "tests/test_repo_advanced_integrity_pr_safe.py",
    "tests/test_revenue_unreacted_range_*.py",
    "tests/test_validate_revenue_unreacted_range_*.py",
    "tests/test_volume_range_breakout_v2_*.py",
    "tests/test_mature_model_row_level_metric_contract_audit.py",
    "tests/test_stock_model_contract_registry.py",
)

CORE_EXACT_PATHS = frozenset(
    {
        ".github/workflows/daily_full_pipeline.yml",
        ".github/workflows/daily_model_maintenance_pr_validation.yml",
        ".github/workflows/daily_pdf_replay_pr_validation.yml",
        ".github/workflows/warrant_flow.yml",
        ".github/workflows/event_catalyst_update.yml",
        ".github/workflows/weekly_theme_review.yml",
        "config/repo_file_lifecycle_inventory.csv",
        "config/repo_production_inventory.csv",
        "config/historical_replay_semantic_contract.csv",
        "config/git_worktree_materialization_contract.csv",
        "config/daily_pdf_rendered_model_regression_contract.csv",
        "config/daily_pdf_semantic_golden_cases.csv",
        "config/daily_pdf_shared_path_inventory.csv",
        "config/repo_hidden_coupling_audit.csv",
        "config/report_artifact_lineage.csv",
        "config/runtime_file_lineage_contract.csv",
        "AGENTS.md",
        "rules/master_priority_rules.md",
        "docs/rules/master_priority_rules.md",
        "docs/repo_hidden_coupling_audit.md",
        "docs/rules/git_worktree_materialization_safety.md",
        "output/latest/daily_report_model_registry_latest.csv",
        "output/latest/model_operation_readiness_latest.csv",
        "output/latest/daily_candidate_model_signals_for_report_latest.csv",
        "output/latest/daily_candidate_model_signals_latest.csv",
        "output/latest/approved_operation_patterns_latest.csv",
        "output/latest/model_contract_parity_latest.csv",
        "output/latest/daily_w_bottom_right_side_operation_section_latest.csv",
        "output/latest/daily_price_pullback_23ema_operation_section_latest.csv",
        "output/latest/chatgpt_daily_report_packet_latest.txt",
        "output/latest/CHATGPT_DAILY_REPORT_PACKET.txt",
        "docs/latest/chatgpt_daily_report_packet_latest.txt",
        "scripts/detect_daily_model_pr_validation_scope.py",
        "build_chatgpt_daily_report_packet.py",
        "scripts/validate_repo_file_lifecycle_inventory.py",
        "scripts/validate_repo_production_inventory.py",
        "scripts/validate_chatgpt_side_pdf_layout_independence.py",
        "scripts/generate_chatgpt_side_daily_reports.py",
        "scripts/git_worktree_safety.py",
        "scripts/resolve_daily_report_source_state.py",
        "scripts/run_chatgpt_daily_report_entrypoint.py",
        "scripts/stage_daily_latest_mirrors.py",
        "scripts/validate_chatgpt_side_pdf_contract.py",
        "scripts/validate_chatgpt_daily_report_new_conversation_replay.py",
        "scripts/validate_repo_hidden_coupling_audit.py",
        "scripts/validate_git_worktree_safety.py",
        "scripts/validate_repo_code_isolation_policy.py",
        "scripts/validate_repo_advanced_integrity.py",
        "scripts/validate_repo_advanced_integrity_pr_safe.py",
        "scripts/validate_warrant_source_status.py",
        "tests/test_chatgpt_daily_report_new_conversation_replay.py",
        "tests/test_chatgpt_daily_report_entrypoint.py",
        "tests/test_chatgpt_side_pdf_contract.py",
        "tests/test_catalyst_pages_sync.py",
        "tests/test_warrant_source_status.py",
        "tests/test_repo_hidden_coupling_audit.py",
        "tests/test_git_worktree_safety.py",
        "tests/test_repo_code_isolation_policy.py",
        "tests/test_repo_advanced_integrity.py",
        "tests/test_repo_advanced_integrity_pr_safe.py",
        "tests/test_daily_model_maintenance_pr_validation_workflow.py",
        "tests/test_detect_daily_model_pr_validation_scope.py",
    }
)

CORE_PREFIXES = (
    "scripts/validate_daily_",
    "tests/test_daily_",
)

PRODUCTION_PDF_EXACT_PATHS = frozenset(
    {
        ".github/workflows/daily_full_pipeline.yml",
        ".github/workflows/daily_model_maintenance_pr_validation.yml",
        ".github/workflows/daily_pdf_replay_pr_validation.yml",
        ".github/workflows/warrant_flow.yml",
        ".github/workflows/event_catalyst_update.yml",
        ".github/workflows/weekly_theme_review.yml",
        "config/stock_model_contract_registry.csv",
        "config/formal_model_evidence_pins.csv",
        "output/latest/daily_report_model_registry_latest.csv",
        "output/latest/daily_candidate_model_signals_for_report_latest.csv",
        "output/latest/daily_candidate_model_signals_latest.csv",
        "output/latest/approved_operation_patterns_latest.csv",
        "output/latest/model_contract_parity_latest.csv",
        "output/latest/daily_w_bottom_right_side_operation_section_latest.csv",
        "output/latest/daily_price_pullback_23ema_operation_section_latest.csv",
        "output/latest/chatgpt_daily_report_packet_latest.txt",
        "output/latest/CHATGPT_DAILY_REPORT_PACKET.txt",
        "docs/latest/chatgpt_daily_report_packet_latest.txt",
        "build_chatgpt_daily_report_packet.py",
        "scripts/build_approved_operation_patterns.py",
        "scripts/audit_daily_candidate_model_selection_correctness.py",
        "scripts/build_daily_candidate_model_layer.py",
        "scripts/generate_chatgpt_side_daily_reports.py",
        "scripts/resolve_daily_report_source_state.py",
        "scripts/run_chatgpt_daily_report_entrypoint.py",
        "scripts/stage_daily_latest_mirrors.py",
        "scripts/validate_chatgpt_daily_report_new_conversation_replay.py",
        "scripts/validate_chatgpt_side_pdf_contract.py",
        "scripts/validate_chatgpt_side_pdf_layout_independence.py",
    }
)

PRODUCTION_PDF_PREFIXES = (
    "config/daily_pdf_",
    "docs/specs/daily_",
    "scripts/build_daily_candidate_",
    "scripts/build_daily_published_",
    "scripts/build_daily_report_",
    "scripts/build_daily_w_bottom_",
    "scripts/build_daily_price_pullback_",
    "scripts/generate_chatgpt_side_",
    "scripts/run_chatgpt_daily_",
    "scripts/validate_chatgpt_daily_",
    "scripts/validate_chatgpt_side_pdf_",
    "scripts/validate_daily_legacy_",
    "scripts/validate_daily_operation_",
    "scripts/validate_daily_pdf_",
    "scripts/validate_daily_production_",
    "scripts/validate_daily_published_",
    "tests/test_chatgpt_daily_",
    "tests/test_chatgpt_side_pdf_",
    "tests/test_daily_legacy_",
    "tests/test_daily_operation_",
    "tests/test_daily_pdf_",
    "tests/test_daily_production_",
    "tests/test_daily_published_",
)

PRODUCTION_PDF_REGISTRY_OWNERS = frozenset({"daily_production"})
PRODUCTION_PDF_REGISTRY_RELATION_FIELDS = frozenset(
    {
        "path",
        "artifact_path",
        "script_path",
        "owner",
        "producer",
        "validator",
        "publisher",
        "allowed_workflows",
        "called_by_workflow",
        "imported_by",
        "tested_by",
        "documented_by",
        "writes_artifact",
        "purpose",
        "keep_reason",
    }
)

SHARED_MARKERS = (
    "formal_model_evidence",
    "model_research",
    "daily_model_",
    "model_data_independence",
    "model_surface_registry",
    "stock_model_contract_registry",
    "model_operation",
    "operation",
    "mature_model",
    "price_pullback",
    "published_snapshot",
    "published_model_snapshot",
    "daily_snapshot_revision",
    "stage_daily_published_snapshot",
    "backfill_historical_all_candidates",
    "daily_candidate_model",
    "daily_report_model_summary",
    "research_against_stock_model_contract",
)

VOLUME_MARKERS = (
    "volume_v2",
    "volume_range_breakout_v2",
    "volume_breakout",
    "volume_attack",
    "daily_canonical_field_lineage",
)

REVENUE_MARKERS = (
    "revenue_unreacted_range",
    "monthly_revenue",
)

FINANCIAL_STATEMENT_MARKERS = ("financial_statement",)

MODEL_LIKE_MARKERS = (
    "daily_model",
    "daily_alpha",
    "revenue_unreacted_range",
    "monthly_revenue",
    "financial_statement",
    "volume_v2",
    "volume_range_breakout",
    "volume_breakout",
)

MODEL_LIKE_PREFIXES = (
    ".github/workflows/",
    "config/",
    "data/",
    "docs/",
    "output/",
    "scripts/",
    "tests/",
)

CENTRAL_SHARED_VOLUME_REVENUE_EXACT_PATHS = frozenset(
    {
        "config/formal_model_evidence_pins.csv",
        "config/stock_model_contract_registry.csv",
        "scripts/build_daily_candidate_model_layer.py",
    }
)

RESEARCH_SAFETY_EXACT_PATHS = frozenset(
    {
        ".github/workflows/research_backtest_pipeline.yml",
        "scripts/validate_model_data_independence.py",
        "scripts/validate_model_research_artifact_ownership.py",
        "scripts/validate_model_research_workflow_isolation.py",
        "scripts/validate_research_production_boundaries.py",
        "tests/test_model_data_independence.py",
        "tests/test_model_research_artifact_ownership.py",
        "tests/test_model_research_workflow_isolation.py",
    }
)

MODEL_OWNED_VOLUME_RESEARCH_EXACT_PATHS = frozenset(
    {
        "scripts/build_volume_range_breakout_v2_research.py",
        "tests/test_volume_range_breakout_v2_scope_probe.py",
    }
)

RESEARCH_DOMAINS = frozenset(
    {
        SHARED_MODEL_RESEARCH,
        VOLUME_V2_RESEARCH,
        REVENUE_RESEARCH,
        FINANCIAL_STATEMENT_RESEARCH,
    }
)

LEGACY_REPO_CURRENT_EXACT_PATHS = frozenset(
    {
        "config/daily_model_background_data_registry.csv",
        "config/daily_model_condition_spec.csv",
        "output/latest/daily_neckline_volume_breakout_confirmation_operation_section_latest.csv",
        "output/latest/daily_volume_breakout_operation_section_latest.csv",
        "output/latest/research_backtest/daily_model_research_parity_latest.csv",
        "scripts/build_daily_price_pullback_23ema_operation_section.py",
        "scripts/build_daily_w_bottom_operation_sections.py",
        "scripts/build_model_operation_readiness.py",
        "scripts/validate_stock_model_contract_registry.py",
        "tests/test_stock_model_contract_registry.py",
    }
)

MODEL_OWNED_SCOPE_BEGIN = (
    "# BEGIN MODEL_OWNED_VALIDATION_SCOPE: revenue_unreacted_range"
)
MODEL_OWNED_SCOPE_END = "# END MODEL_OWNED_VALIDATION_SCOPE: revenue_unreacted_range"
REVENUE_CONTENT_SCOPED_PATHS = frozenset(
    {
        "scripts/build_model_operation_readiness.py",
        "scripts/validate_model_operation_readiness.py",
        "tests/test_model_operation_readiness.py",
    }
)

REPO_CURRENT_AND_SHARED_EXACT_PATHS = frozenset(
    {
        "scripts/build_approved_operation_patterns.py",
        "scripts/audit_daily_candidate_model_selection_correctness.py",
    }
)

VOLUME_SNAPSHOT_PREFIXES = ("output/history/daily_model_snapshots/",)


class ScopeDetectionError(RuntimeError):
    pass


@dataclass(frozen=True)
class ScopeResult:
    changed_paths: tuple[str, ...]
    watched_paths: tuple[str, ...]
    selected_domains: tuple[str, ...]


def normalize_path(value: str) -> str:
    path = value.replace("\\", "/")
    while path.startswith("./"):
        path = path[2:]
    return path


def matches_pattern(path: str, pattern: str) -> bool:
    return fnmatch.fnmatchcase(path, pattern)


def is_watched_path(value: str) -> bool:
    path = normalize_path(value)
    return any(matches_pattern(path, pattern) for pattern in WATCHED_PATH_PATTERNS)


def is_model_like_path(value: str) -> bool:
    path = normalize_path(value).lower()
    return path.startswith(MODEL_LIKE_PREFIXES) and any(
        marker in path for marker in MODEL_LIKE_MARKERS
    )


def is_production_pdf_path(value: str) -> bool:
    path = normalize_path(value)
    return path in PRODUCTION_PDF_EXACT_PATHS or path.startswith(
        PRODUCTION_PDF_PREFIXES
    )


def is_production_pdf_registry_row(row: Mapping[str, str]) -> bool:
    if row.get("owner", "").strip().lower() in PRODUCTION_PDF_REGISTRY_OWNERS:
        return True
    return any(
        is_production_pdf_path(value)
        for field, value in row.items()
        if field in PRODUCTION_PDF_REGISTRY_RELATION_FIELDS
        for value in value.split(";")
        if value.strip()
    )


def is_revenue_registry_row(row: Mapping[str, str]) -> bool:
    return any(
        marker in value.lower()
        for value in row.values()
        for marker in REVENUE_MARKERS
    )


def domains_for_path(value: str) -> frozenset[str]:
    path = normalize_path(value)
    lowered = path.lower()
    watched = is_watched_path(path)
    model_like = is_model_like_path(path)
    if not watched and not model_like:
        return frozenset()

    if path in RESEARCH_SAFETY_EXACT_PATHS:
        return frozenset({RESEARCH_SAFETY_LITE})
    if path in MODEL_OWNED_VOLUME_RESEARCH_EXACT_PATHS:
        return frozenset({RESEARCH_SAFETY_LITE, VOLUME_V2_RESEARCH})
    if path in REPO_CURRENT_AND_SHARED_EXACT_PATHS:
        selected = {
            REPO_CURRENT_CONTRACTS,
            RESEARCH_SAFETY_LITE,
            SHARED_MODEL_RESEARCH,
        }
        if is_production_pdf_path(path):
            selected.add(PRODUCTION_PDF_CONTRACTS)
        return frozenset(selected)
    if path in CENTRAL_SHARED_VOLUME_REVENUE_EXACT_PATHS:
        selected = {
            REPO_CURRENT_CONTRACTS,
            RESEARCH_SAFETY_LITE,
            SHARED_MODEL_RESEARCH,
            VOLUME_V2_RESEARCH,
            REVENUE_RESEARCH,
        }
        if is_production_pdf_path(path):
            selected.add(PRODUCTION_PDF_CONTRACTS)
        return frozenset(selected)
    if path.startswith(VOLUME_SNAPSHOT_PREFIXES):
        return frozenset(
            {
                REPO_CURRENT_CONTRACTS,
                PRODUCTION_PDF_CONTRACTS,
                RESEARCH_SAFETY_LITE,
                SHARED_MODEL_RESEARCH,
                VOLUME_V2_RESEARCH,
            }
        )

    # Revenue-owned modules, tests, artifacts, and specs remain one independent
    # model surface even when their names contain generic words such as
    # "operation" or "financial_statement". The revenue job owns its explicit
    # exclusion-boundary validator; only actual shared financial-statement
    # sources route to the financial-statement domain below.
    if any(marker in lowered for marker in REVENUE_MARKERS):
        return frozenset({RESEARCH_SAFETY_LITE, REVENUE_RESEARCH})

    if path in CORE_EXACT_PATHS:
        selected = {REPO_CURRENT_CONTRACTS}
        if is_production_pdf_path(path):
            selected.add(PRODUCTION_PDF_CONTRACTS)
        return frozenset(selected)

    selected: set[str] = set()
    if path in LEGACY_REPO_CURRENT_EXACT_PATHS:
        selected.add(REPO_CURRENT_CONTRACTS)
    if path.startswith(CORE_PREFIXES):
        selected.add(REPO_CURRENT_CONTRACTS)
    if is_production_pdf_path(path):
        selected.update({REPO_CURRENT_CONTRACTS, PRODUCTION_PDF_CONTRACTS})

    if any(marker in lowered for marker in SHARED_MARKERS):
        selected.add(SHARED_MODEL_RESEARCH)
    if "model" in lowered:
        selected.add(SHARED_MODEL_RESEARCH)
    if matches_pattern(path, "scripts/build_*_research.py"):
        selected.add(SHARED_MODEL_RESEARCH)
    if matches_pattern(path, "tests/test_model_research_*.py"):
        selected.add(SHARED_MODEL_RESEARCH)

    if any(marker in lowered for marker in VOLUME_MARKERS):
        selected.add(VOLUME_V2_RESEARCH)
    if any(marker in lowered for marker in REVENUE_MARKERS):
        selected.add(REVENUE_RESEARCH)
    if any(marker in lowered for marker in FINANCIAL_STATEMENT_MARKERS):
        selected.add(FINANCIAL_STATEMENT_RESEARCH)
        # Revenue's fail-closed financial-statement boundary consumes this source.
        selected.add(REVENUE_RESEARCH)

    if not selected:
        raise ScopeDetectionError(
            "changed path is watched or model-like but has no declared validation "
            f"domain: {path!r}"
        )

    # Research changes run one common, research-only safety gate. Production/PDF
    # contracts remain independently path- or registry-row-scoped.
    if selected.intersection(RESEARCH_DOMAINS):
        selected.add(RESEARCH_SAFETY_LITE)
    return frozenset(selected)


def _read_git_text(commit: str, path: str) -> str:
    result = _run_git(["show", f"{commit}:{path}"])
    if result.returncode != 0:
        stderr = result.stderr.decode("utf-8", errors="replace").strip()
        raise ScopeDetectionError(
            f"cannot read content-scoped path {path!r} at {commit!r}: {stderr}"
        )
    try:
        return result.stdout.decode("utf-8-sig", errors="strict")
    except UnicodeDecodeError as exc:
        raise ScopeDetectionError(
            f"content-scoped path must be valid UTF-8: {path!r}: {exc}"
        ) from exc


def _parse_registry(
    source: str,
    *,
    path: str,
    key_field: str,
    revision: str,
) -> tuple[tuple[str, ...], dict[str, dict[str, str]]]:
    try:
        reader = csv.DictReader(io.StringIO(source, newline=""), strict=True)
        fieldnames = tuple(reader.fieldnames or ())
        if key_field not in fieldnames or len(fieldnames) != len(set(fieldnames)):
            raise ScopeDetectionError(
                f"shared registry schema is invalid for {path!r} at {revision!r}"
            )
        rows: dict[str, dict[str, str]] = {}
        for row_number, row in enumerate(reader, start=2):
            if None in row or any(value is None for value in row.values()):
                raise ScopeDetectionError(
                    f"shared registry row is malformed: {path}:{row_number} "
                    f"at {revision!r}"
                )
            normalized = {name: value for name, value in row.items()}
            key = normalized[key_field].strip()
            if not key or key in rows:
                raise ScopeDetectionError(
                    f"shared registry key is empty or duplicated: {path}:{row_number} "
                    f"at {revision!r}"
                )
            rows[key] = normalized
    except csv.Error as exc:
        raise ScopeDetectionError(
            f"cannot parse shared registry {path!r} at {revision!r}: {exc}"
        ) from exc
    return fieldnames, rows


def registry_change_affects(
    path: str,
    *,
    base_revision: str,
    head_revision: str,
    row_is_relevant: Callable[[Mapping[str, str]], bool],
) -> bool:
    key_field = SHARED_REGISTRY_KEY_FIELDS[path]
    try:
        base_fields, base_rows = _parse_registry(
            _read_git_text(base_revision, path),
            path=path,
            key_field=key_field,
            revision=base_revision,
        )
        head_fields, head_rows = _parse_registry(
            _read_git_text(head_revision, path),
            path=path,
            key_field=key_field,
            revision=head_revision,
        )
        if base_fields != head_fields:
            raise ScopeDetectionError(f"shared registry schema changed: {path!r}")
    except ScopeDetectionError:
        return True
    return any(
        row_is_relevant(row)
        for key in set(base_rows) | set(head_rows)
        if base_rows.get(key) != head_rows.get(key)
        for row in (base_rows.get(key), head_rows.get(key))
        if row is not None
    )


def _strip_revenue_owned_scope_blocks(
    source: str,
    *,
    path: str,
    revision_label: str,
) -> tuple[str, tuple[str, ...]]:
    try:
        marker_comment_lines = {
            token.start[0]
            for token in tokenize.generate_tokens(io.StringIO(source).readline)
            if token.type == tokenize.COMMENT
            and token.string.strip() in {MODEL_OWNED_SCOPE_BEGIN, MODEL_OWNED_SCOPE_END}
        }
    except (IndentationError, SyntaxError, tokenize.TokenError) as exc:
        raise ScopeDetectionError(
            f"cannot tokenize content-scoped path: {path} ({revision_label}): {exc}"
        ) from exc
    outside: list[str] = []
    blocks: list[str] = []
    current: list[str] | None = None
    for line_number, line in enumerate(source.splitlines(keepends=True), start=1):
        marker = line.strip()
        if marker == MODEL_OWNED_SCOPE_BEGIN:
            if line_number not in marker_comment_lines:
                raise ScopeDetectionError(
                    "revenue model-owned validation scope marker is not a Python comment: "
                    f"{path}:{line_number} ({revision_label})"
                )
            if current is not None:
                raise ScopeDetectionError(
                    "nested revenue model-owned validation scope marker: "
                    f"{path}:{line_number} ({revision_label})"
                )
            current = []
            continue
        if marker == MODEL_OWNED_SCOPE_END:
            if line_number not in marker_comment_lines:
                raise ScopeDetectionError(
                    "revenue model-owned validation scope marker is not a Python comment: "
                    f"{path}:{line_number} ({revision_label})"
                )
            if current is None:
                raise ScopeDetectionError(
                    "unmatched revenue model-owned validation scope end marker: "
                    f"{path}:{line_number} ({revision_label})"
                )
            blocks.append("".join(current))
            current = None
            continue
        if current is None:
            outside.append(line)
        else:
            current.append(line)
    if current is not None:
        raise ScopeDetectionError(
            "unterminated revenue model-owned validation scope marker: "
            f"{path} ({revision_label})"
        )
    return "".join(outside), tuple(blocks)


def is_revenue_owned_content_change(
    path: str,
    *,
    base_sha: str,
    merge_sha: str,
) -> bool:
    normalized = normalize_path(path)
    if normalized not in REVENUE_CONTENT_SCOPED_PATHS:
        return False
    try:
        base_source = _read_git_text(base_sha, normalized)
        merge_source = _read_git_text(merge_sha, normalized)
        base_outside, base_blocks = _strip_revenue_owned_scope_blocks(
            base_source,
            path=normalized,
            revision_label="base",
        )
        merge_outside, merge_blocks = _strip_revenue_owned_scope_blocks(
            merge_source,
            path=normalized,
            revision_label="merge",
        )
    except ScopeDetectionError:
        return False
    if base_source == merge_source or not merge_blocks or base_blocks == merge_blocks:
        return False
    return base_outside == merge_outside


def domains_for_changed_path(
    path: str,
    *,
    base_sha: str,
    merge_sha: str,
) -> frozenset[str]:
    normalized = normalize_path(path)
    if normalized in SHARED_REGISTRY_KEY_FIELDS:
        selected = {REPO_CURRENT_CONTRACTS}
        if registry_change_affects(
            normalized,
            base_revision=base_sha,
            head_revision=merge_sha,
            row_is_relevant=is_production_pdf_registry_row,
        ):
            selected.add(PRODUCTION_PDF_CONTRACTS)
        if registry_change_affects(
            normalized,
            base_revision=base_sha,
            head_revision=merge_sha,
            row_is_relevant=is_revenue_registry_row,
        ):
            selected.update({RESEARCH_SAFETY_LITE, REVENUE_RESEARCH})
        return frozenset(selected)
    if is_revenue_owned_content_change(
        path,
        base_sha=base_sha,
        merge_sha=merge_sha,
    ):
        return frozenset({RESEARCH_SAFETY_LITE, REVENUE_RESEARCH})
    return domains_for_path(path)


def _run_git(args: Sequence[str]) -> subprocess.CompletedProcess[bytes]:
    return subprocess.run(
        ["git", "--no-replace-objects", *args],
        cwd=ROOT,
        check=False,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )


def _require_commit(value: str, label: str) -> None:
    if not value.strip():
        raise ScopeDetectionError(f"missing {label}")
    result = _run_git(["cat-file", "-e", f"{value}^{{commit}}"])
    if result.returncode != 0:
        stderr = result.stderr.decode("utf-8", errors="replace").strip()
        raise ScopeDetectionError(
            f"{label} is not an available commit object: {value!r}: {stderr}"
        )


def parse_name_status_z(payload: bytes) -> list[str]:
    if payload and not payload.endswith(b"\0"):
        raise ScopeDetectionError("malformed NUL-delimited git name-status output")
    fields = payload.split(b"\0")
    if fields and fields[-1] == b"":
        fields.pop()
    if len(fields) % 2:
        raise ScopeDetectionError("malformed NUL-delimited git name-status output")

    paths: list[str] = []
    for index in range(0, len(fields), 2):
        status = fields[index].decode("ascii", errors="strict")
        if status not in {"A", "B", "D", "M", "T", "U", "X"}:
            raise ScopeDetectionError(
                f"unexpected git diff status with rename detection disabled: {status!r}"
            )
        path = fields[index + 1].decode("utf-8", errors="surrogateescape")
        if not path:
            raise ScopeDetectionError("git diff returned an empty changed path")
        paths.append(normalize_path(path))
    return sorted(set(paths))


def _require_synthetic_merge_identity(
    *, base_sha: str, head_sha: str, merge_sha: str
) -> None:
    _require_commit(base_sha, "base SHA")
    _require_commit(head_sha, "head SHA")
    _require_commit(merge_sha, "merge SHA")
    result = _run_git(["rev-list", "--parents", "-n", "1", merge_sha])
    if result.returncode != 0:
        stderr = result.stderr.decode("utf-8", errors="replace").strip()
        raise ScopeDetectionError(f"cannot inspect pull request merge identity: {stderr}")
    fields = result.stdout.decode("ascii", errors="strict").strip().split()
    if len(fields) != 3:
        raise ScopeDetectionError(
            "pull request ref must be an exact two-parent synthetic merge"
        )
    observed_merge, observed_base, observed_head = fields
    if observed_merge != merge_sha:
        raise ScopeDetectionError(
            f"checked-out merge SHA mismatch: actual={observed_merge} expected={merge_sha}"
        )
    if observed_base != base_sha:
        raise ScopeDetectionError(
            f"synthetic merge base parent mismatch: actual={observed_base} expected={base_sha}"
        )
    if observed_head != head_sha:
        raise ScopeDetectionError(
            f"synthetic merge head parent mismatch: actual={observed_head} expected={head_sha}"
        )


def changed_paths_from_git(base_sha: str, head_sha: str, merge_sha: str) -> list[str]:
    _require_synthetic_merge_identity(
        base_sha=base_sha,
        head_sha=head_sha,
        merge_sha=merge_sha,
    )
    result = _run_git(
        [
            "diff",
            "--name-status",
            "--no-renames",
            "--diff-filter=ABDM TUX".replace(" ", ""),
            "-z",
            f"{base_sha}..{merge_sha}",
            "--",
        ]
    )
    if result.returncode != 0:
        stderr = result.stderr.decode("utf-8", errors="replace").strip()
        raise ScopeDetectionError(
            f"git diff failed for {base_sha!r}..{merge_sha!r}: {stderr}"
        )
    return parse_name_status_z(result.stdout)


def detect_scope(
    *,
    event_name: str,
    validation_profile: str = "all",
    base_sha: str | None = None,
    head_sha: str | None = None,
    merge_sha: str | None = None,
) -> ScopeResult:
    if event_name == "workflow_dispatch":
        profiles = {
            "all": DOMAINS,
            "revenue-research": (
                RESEARCH_SAFETY_LITE,
                REVENUE_RESEARCH,
            ),
        }
        if validation_profile not in profiles:
            raise ScopeDetectionError(
                f"unsupported workflow_dispatch validation profile: {validation_profile!r}"
            )
        return ScopeResult(
            changed_paths=(),
            watched_paths=(),
            selected_domains=profiles[validation_profile],
        )
    if event_name != "pull_request":
        raise ScopeDetectionError(f"unsupported event name: {event_name!r}")
    if validation_profile != "all":
        raise ScopeDetectionError(
            "pull_request validation profile must be 'all'; changed paths select the domains"
        )
    if not base_sha or not head_sha or not merge_sha:
        raise ScopeDetectionError(
            "pull_request scope requires base, head, and synthetic merge SHAs"
        )

    changed = changed_paths_from_git(base_sha, head_sha, merge_sha)
    if not changed:
        raise ScopeDetectionError("pull_request effective tree diff is empty")
    watched_paths: list[str] = []
    selected: set[str] = set()
    for path in changed:
        domains = domains_for_changed_path(
            path,
            base_sha=base_sha,
            merge_sha=merge_sha,
        )
        if domains:
            watched_paths.append(path)
            selected.update(domains)

    if selected.intersection(RESEARCH_DOMAINS) and RESEARCH_SAFETY_LITE not in selected:
        raise ScopeDetectionError("selected research scope is missing research-safety-lite")

    return ScopeResult(
        changed_paths=tuple(changed),
        watched_paths=tuple(sorted(set(watched_paths))),
        selected_domains=tuple(domain for domain in DOMAINS if domain in selected),
    )


def output_payload(result: ScopeResult) -> dict[str, object]:
    selected = set(result.selected_domains)
    return {
        "changed_count": len(result.changed_paths),
        "watched_count": len(result.watched_paths),
        "watched_paths": list(result.watched_paths),
        "selected_domains": list(result.selected_domains),
        **{DOMAIN_OUTPUTS[domain]: domain in selected for domain in DOMAINS},
    }


def write_github_output(path: Path, result: ScopeResult) -> None:
    selected = set(result.selected_domains)
    with path.open("a", encoding="utf-8", newline="\n") as handle:
        for domain in DOMAINS:
            key = DOMAIN_OUTPUTS[domain]
            handle.write(f"{key}={'true' if domain in selected else 'false'}\n")
        handle.write(f"changed_count={len(result.changed_paths)}\n")
        handle.write(f"watched_count={len(result.watched_paths)}\n")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Detect path-scoped Daily Model PR validation domains."
    )
    parser.add_argument(
        "--event-name", choices=("pull_request", "workflow_dispatch"), required=True
    )
    parser.add_argument(
        "--validation-profile",
        choices=("all", "revenue-research"),
        default="all",
    )
    parser.add_argument("--base-sha")
    parser.add_argument("--head-sha")
    parser.add_argument("--merge-sha")
    parser.add_argument("--github-output", type=Path)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    try:
        result = detect_scope(
            event_name=args.event_name,
            validation_profile=args.validation_profile,
            base_sha=args.base_sha,
            head_sha=args.head_sha,
            merge_sha=args.merge_sha,
        )
    except ScopeDetectionError as exc:
        print(json.dumps({"error": str(exc)}, ensure_ascii=True, sort_keys=True))
        return 2

    print(json.dumps(output_payload(result), ensure_ascii=True, sort_keys=True))
    if args.github_output:
        write_github_output(args.github_output, result)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
