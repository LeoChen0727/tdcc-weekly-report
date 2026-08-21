from __future__ import annotations

import argparse
import fnmatch
import json
import subprocess
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable, Sequence


ROOT = Path(__file__).resolve().parents[1]

REPO_CURRENT_CONTRACTS = "repo-current-contracts"
SHARED_MODEL_RESEARCH = "shared-model-research"
VOLUME_V2_RESEARCH = "volume-v2-research"
REVENUE_RESEARCH = "revenue-research"
FINANCIAL_STATEMENT_RESEARCH = "financial-statement-research"

DOMAINS = (
    REPO_CURRENT_CONTRACTS,
    SHARED_MODEL_RESEARCH,
    VOLUME_V2_RESEARCH,
    REVENUE_RESEARCH,
    FINANCIAL_STATEMENT_RESEARCH,
)

DOMAIN_OUTPUTS = {
    REPO_CURRENT_CONTRACTS: "repo_current_contracts",
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


def domains_for_path(value: str) -> frozenset[str]:
    path = normalize_path(value)
    lowered = path.lower()
    watched = is_watched_path(path)
    model_like = is_model_like_path(path)
    if not watched and not model_like:
        return frozenset()

    if path == ".github/workflows/research_backtest_pipeline.yml":
        return frozenset(DOMAINS)
    if path in REPO_CURRENT_AND_SHARED_EXACT_PATHS:
        return frozenset({REPO_CURRENT_CONTRACTS, SHARED_MODEL_RESEARCH})
    if path in CENTRAL_SHARED_VOLUME_REVENUE_EXACT_PATHS:
        return frozenset(
            {
                REPO_CURRENT_CONTRACTS,
                SHARED_MODEL_RESEARCH,
                VOLUME_V2_RESEARCH,
                REVENUE_RESEARCH,
            }
        )
    if path.startswith(VOLUME_SNAPSHOT_PREFIXES):
        return frozenset(
            {
                REPO_CURRENT_CONTRACTS,
                SHARED_MODEL_RESEARCH,
                VOLUME_V2_RESEARCH,
            }
        )

    if path in CORE_EXACT_PATHS:
        return frozenset({REPO_CURRENT_CONTRACTS})

    selected: set[str] = set()
    if path.startswith(CORE_PREFIXES):
        selected.add(REPO_CURRENT_CONTRACTS)

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

    # Every selected research domain is gated by the common current-contract job.
    selected.add(REPO_CURRENT_CONTRACTS)
    return frozenset(selected)


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
    base_sha: str | None = None,
    head_sha: str | None = None,
    merge_sha: str | None = None,
) -> ScopeResult:
    if event_name == "workflow_dispatch":
        return ScopeResult(
            changed_paths=(),
            watched_paths=(),
            selected_domains=DOMAINS,
        )
    if event_name != "pull_request":
        raise ScopeDetectionError(f"unsupported event name: {event_name!r}")
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
        domains = domains_for_path(path)
        if domains:
            watched_paths.append(path)
            selected.update(domains)

    if selected and REPO_CURRENT_CONTRACTS not in selected:
        raise ScopeDetectionError("selected scope is missing repo-current-contracts")

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
