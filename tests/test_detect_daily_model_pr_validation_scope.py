from __future__ import annotations

import subprocess
from pathlib import Path

import pytest

from scripts import detect_daily_model_pr_validation_scope as scope
from scripts import validate_daily_legacy_mature_model_paths_removed as mature_legacy
from scripts import validate_daily_legacy_volume_range_breakout_removed as volume_legacy


ROOT = Path(__file__).resolve().parents[1]
WORKFLOW = ROOT / ".github" / "workflows" / "daily_model_maintenance_pr_validation.yml"

FOUR_MODEL_SHARED_RESEARCH_EXACT_PATHS = frozenset(
    {
        f"scripts/{prefix}_{model_id}_research.py"
        for model_id in (
            "hot_theme_pullback",
            "pullback_short_reclaim",
            "tdcc_stealth_accumulation",
            "tdcc_short_term_continuation_d5_d10",
        )
        for prefix in ("build", "validate")
    }
    | {
        f"tests/test_{model_id}_{suffix}.py"
        for model_id in (
            "hot_theme_pullback",
            "pullback_short_reclaim",
            "tdcc_stealth_accumulation",
            "tdcc_short_term_continuation_d5_d10",
        )
        for suffix in ("research", "scope_probe")
    }
    | {
        "scripts/audit_tdcc_stealth_accumulation_pit_replay_availability.py",
        "scripts/validate_tdcc_stealth_accumulation_pit_replay_availability.py",
        "tests/test_tdcc_stealth_accumulation_pit_replay_availability.py",
        "output/research/tdcc_stealth_accumulation/"
        "tdcc_stealth_accumulation_pit_replay_availability_audit_v1.csv",
    }
)

LEGACY_GUARD_SCOPE_CASES = (
    ("output/latest/daily_report_model_registry_latest.csv", {scope.REPO_CURRENT_CONTRACTS, scope.PRODUCTION_PDF_CONTRACTS}),
    ("output/latest/model_operation_readiness_latest.csv", {scope.REPO_CURRENT_CONTRACTS}),
    ("output/latest/daily_candidate_model_signals_for_report_latest.csv", {scope.REPO_CURRENT_CONTRACTS, scope.PRODUCTION_PDF_CONTRACTS}),
    ("output/latest/daily_candidate_model_signals_latest.csv", {scope.REPO_CURRENT_CONTRACTS, scope.PRODUCTION_PDF_CONTRACTS}),
    ("output/latest/approved_operation_patterns_latest.csv", {scope.REPO_CURRENT_CONTRACTS, scope.PRODUCTION_PDF_CONTRACTS}),
    ("output/latest/model_contract_parity_latest.csv", {scope.REPO_CURRENT_CONTRACTS, scope.PRODUCTION_PDF_CONTRACTS}),
    ("output/latest/daily_w_bottom_right_side_operation_section_latest.csv", {scope.REPO_CURRENT_CONTRACTS, scope.PRODUCTION_PDF_CONTRACTS}),
    ("output/latest/daily_price_pullback_23ema_operation_section_latest.csv", {scope.REPO_CURRENT_CONTRACTS, scope.PRODUCTION_PDF_CONTRACTS}),
    ("output/latest/chatgpt_daily_report_packet_latest.txt", {scope.REPO_CURRENT_CONTRACTS, scope.PRODUCTION_PDF_CONTRACTS}),
    ("output/latest/CHATGPT_DAILY_REPORT_PACKET.txt", {scope.REPO_CURRENT_CONTRACTS, scope.PRODUCTION_PDF_CONTRACTS}),
    ("docs/latest/chatgpt_daily_report_packet_latest.txt", {scope.REPO_CURRENT_CONTRACTS, scope.PRODUCTION_PDF_CONTRACTS}),
    ("scripts/build_approved_operation_patterns.py", {scope.REPO_CURRENT_CONTRACTS, scope.RESEARCH_SAFETY_LITE, scope.SHARED_MODEL_RESEARCH}),
    ("scripts/audit_daily_candidate_model_selection_correctness.py", {scope.REPO_CURRENT_CONTRACTS, scope.RESEARCH_SAFETY_LITE, scope.SHARED_MODEL_RESEARCH}),
    ("build_chatgpt_daily_report_packet.py", {scope.REPO_CURRENT_CONTRACTS}),
)


def legacy_validator_input_paths() -> set[str]:
    paths = set()
    for module in (volume_legacy, mature_legacy):
        paths.update(module.FORMAL_MODEL_ID_CSVS)
        paths.update(module.PACKET_TEXTS)
        paths.update(module.FORBIDDEN_SOURCE_SNIPPETS)
    paths.update(mature_legacy.EXPECTED_ADAPTER_MODELS)
    paths.add(ROOT / "config" / "daily_model_background_data_registry.csv")
    return {path.relative_to(ROOT).as_posix() for path in paths}


def run_git(repo: Path, *args: str) -> str:
    result = subprocess.run(
        ["git", "--no-replace-objects", *args],
        cwd=repo,
        check=True,
        capture_output=True,
        text=True,
    )
    return result.stdout.strip()


def write_minimal_scope_inventories(repo: Path) -> None:
    config = repo / "config"
    config.mkdir(parents=True, exist_ok=True)
    inventory_sources = {
        "repo_file_lifecycle_inventory.csv": "path,owner,called_by_workflow\n",
        "repo_production_inventory.csv": "path,owner,allowed_workflows\n",
        "report_artifact_lineage.csv": (
            "artifact_path,owner,producer,validator,publisher\n"
        ),
        "runtime_file_lineage_contract.csv": "script_path,owner\n",
    }
    for name, source in inventory_sources.items():
        (config / name).write_text(source, encoding="utf-8")


def init_repo(
    tmp_path: Path,
    changed_rel: str = ".github/workflows/daily_full_pipeline.yml",
) -> tuple[Path, str, str, str]:
    repo = tmp_path / "repo"
    repo.mkdir()
    run_git(repo, "init", "--initial-branch=main")
    run_git(repo, "config", "user.email", "scope-test@example.invalid")
    run_git(repo, "config", "user.name", "Scope Test")
    write_minimal_scope_inventories(repo)
    marker = repo / "README.md"
    marker.write_text("base\n", encoding="utf-8")
    run_git(repo, "add", "--all")
    run_git(repo, "commit", "-m", "base")
    base_sha = run_git(repo, "rev-parse", "HEAD")
    run_git(repo, "switch", "-c", "feature")
    changed = repo / changed_rel
    changed.parent.mkdir(parents=True, exist_ok=True)
    changed.write_text("feature\n", encoding="utf-8")
    run_git(repo, "add", changed_rel)
    run_git(repo, "commit", "-m", "head")
    head_sha = run_git(repo, "rev-parse", "HEAD")
    run_git(repo, "switch", "main")
    run_git(repo, "merge", "--no-ff", "feature", "-m", "synthetic merge")
    return repo, base_sha, head_sha, run_git(repo, "rev-parse", "HEAD")


def test_workflow_runs_the_cheap_scope_for_every_pull_request() -> None:
    text = WORKFLOW.read_text(encoding="utf-8")
    event_block = text[text.index("on:") : text.index("permissions:")]

    assert "  pull_request:\n" in event_block
    assert "  workflow_dispatch:\n" in event_block
    assert "paths:" not in event_block
    assert "paths-ignore:" not in event_block


def test_every_current_tracked_owned_path_has_a_declared_domain() -> None:
    result = subprocess.run(
        ["git", "--no-replace-objects", "ls-files", "-z"],
        cwd=ROOT,
        check=True,
        capture_output=True,
    )
    tracked = [
        field.decode("utf-8", errors="surrogateescape")
        for field in result.stdout.split(b"\0")
        if field
    ]
    explicit_owned = {path for path, _ in LEGACY_GUARD_SCOPE_CASES}
    assert explicit_owned <= set(tracked)
    assert explicit_owned <= legacy_validator_input_paths()
    watched = [
        path
        for path in tracked
        if scope.is_watched_path(path) or scope.is_model_like_path(path)
    ]

    assert watched
    unclassified = [
        path
        for path in sorted(set(watched) | explicit_owned)
        if not {
            scope.REPO_CURRENT_CONTRACTS,
            scope.RESEARCH_SAFETY_LITE,
        }.intersection(scope.domains_for_path(path))
    ]
    assert unclassified == []


@pytest.mark.parametrize(
    ("path", "expected"),
    (
        (
            ".github/workflows/daily_full_pipeline.yml",
            {scope.REPO_CURRENT_CONTRACTS, scope.PRODUCTION_PDF_CONTRACTS},
        ),
        (
            ".github/workflows/daily_pdf_replay_pr_validation.yml",
            {scope.REPO_CURRENT_CONTRACTS, scope.PRODUCTION_PDF_CONTRACTS},
        ),
        (
            "scripts/build_approved_operation_patterns.py",
            {
                scope.REPO_CURRENT_CONTRACTS,
                scope.PRODUCTION_PDF_CONTRACTS,
                scope.RESEARCH_SAFETY_LITE,
                scope.SHARED_MODEL_RESEARCH,
            },
        ),
        (
            "scripts/audit_daily_candidate_model_selection_correctness.py",
            {
                scope.REPO_CURRENT_CONTRACTS,
                scope.PRODUCTION_PDF_CONTRACTS,
                scope.RESEARCH_SAFETY_LITE,
                scope.SHARED_MODEL_RESEARCH,
            },
        ),
        (
            "build_chatgpt_daily_report_packet.py",
            {scope.REPO_CURRENT_CONTRACTS, scope.PRODUCTION_PDF_CONTRACTS},
        ),
        *LEGACY_GUARD_SCOPE_CASES[:11],
        (
            "scripts/model_data_independence.py",
            {scope.RESEARCH_SAFETY_LITE, scope.SHARED_MODEL_RESEARCH},
        ),
        (
            "scripts/build_volume_v2_warrant_lineage_history_audit.py",
            {scope.RESEARCH_SAFETY_LITE, scope.VOLUME_V2_RESEARCH},
        ),
        (
            "scripts/build_volume_range_breakout_v2_research.py",
            {scope.RESEARCH_SAFETY_LITE, scope.VOLUME_V2_RESEARCH},
        ),
        (
            "tests/test_volume_range_breakout_v2_scope_probe.py",
            {scope.RESEARCH_SAFETY_LITE, scope.VOLUME_V2_RESEARCH},
        ),
        (
            "scripts/validate_revenue_unreacted_range_source_snapshot_projection.py",
            {scope.RESEARCH_SAFETY_LITE, scope.REVENUE_RESEARCH},
        ),
        (
            ".github/workflows/revenue_unreacted_range_readiness_formal_sync.yml",
            {scope.RESEARCH_SAFETY_LITE, scope.REVENUE_RESEARCH},
        ),
        (
            "scripts/revenue_unreacted_range_operation_adapter.py",
            {scope.RESEARCH_SAFETY_LITE, scope.REVENUE_RESEARCH},
        ),
        (
            "tests/test_revenue_unreacted_range_operation_adapter.py",
            {scope.RESEARCH_SAFETY_LITE, scope.REVENUE_RESEARCH},
        ),
        (
            "docs/specs/revenue_unreacted_range_operation_adapter.md",
            {scope.RESEARCH_SAFETY_LITE, scope.REVENUE_RESEARCH},
        ),
        (
            "scripts/validate_revenue_unreacted_range_financial_statement_fail_closed.py",
            {scope.RESEARCH_SAFETY_LITE, scope.REVENUE_RESEARCH},
        ),
        (
            "scripts/build_financial_statement_historical_pit_source_audit.py",
            {
                scope.RESEARCH_SAFETY_LITE,
                scope.REVENUE_RESEARCH,
                scope.FINANCIAL_STATEMENT_RESEARCH,
            },
        ),
        (
            ".github/workflows/research_backtest_pipeline.yml",
            {scope.RESEARCH_SAFETY_LITE},
        ),
        (
            "scripts/build_daily_candidate_model_layer.py",
            {
                scope.REPO_CURRENT_CONTRACTS,
                scope.PRODUCTION_PDF_CONTRACTS,
                scope.RESEARCH_SAFETY_LITE,
                scope.SHARED_MODEL_RESEARCH,
                scope.VOLUME_V2_RESEARCH,
                scope.REVENUE_RESEARCH,
            },
        ),
        (
            "config/stock_model_contract_registry.csv",
            {
                scope.REPO_CURRENT_CONTRACTS,
                scope.PRODUCTION_PDF_CONTRACTS,
                scope.RESEARCH_SAFETY_LITE,
                scope.SHARED_MODEL_RESEARCH,
                scope.VOLUME_V2_RESEARCH,
                scope.REVENUE_RESEARCH,
            },
        ),
        (
            "config/formal_model_evidence_pins.csv",
            {
                scope.REPO_CURRENT_CONTRACTS,
                scope.PRODUCTION_PDF_CONTRACTS,
                scope.RESEARCH_SAFETY_LITE,
                scope.SHARED_MODEL_RESEARCH,
                scope.VOLUME_V2_RESEARCH,
                scope.REVENUE_RESEARCH,
            },
        ),
        (
            "data/monthly_revenue_history/monthly_revenue_history.csv",
            {scope.RESEARCH_SAFETY_LITE, scope.REVENUE_RESEARCH},
        ),
        (
            "docs/latest/revenue_unreacted_range_scope_probe.csv",
            {scope.RESEARCH_SAFETY_LITE, scope.REVENUE_RESEARCH},
        ),
        (
            "docs/latest/volume_v2_scope_probe.csv",
            {scope.RESEARCH_SAFETY_LITE, scope.VOLUME_V2_RESEARCH},
        ),
        (
            "output/history/daily_model_snapshots/scope_probe.csv",
            {
                scope.REPO_CURRENT_CONTRACTS,
                scope.PRODUCTION_PDF_CONTRACTS,
                scope.RESEARCH_SAFETY_LITE,
                scope.SHARED_MODEL_RESEARCH,
                scope.VOLUME_V2_RESEARCH,
            },
        ),
    ),
)
def test_paths_select_only_their_declared_domains(
    path: str, expected: set[str]
) -> None:
    assert set(scope.domains_for_path(path)) == expected


def test_four_model_research_and_tdcc_stealth_pit_audit_route_exactly() -> None:
    assert scope.MODEL_OWNED_SHARED_RESEARCH_EXACT_PATHS == (
        FOUR_MODEL_SHARED_RESEARCH_EXACT_PATHS
    )
    for path in sorted(FOUR_MODEL_SHARED_RESEARCH_EXACT_PATHS):
        assert scope.is_watched_path(path)
        assert scope.domains_for_path(path) == frozenset(
            {scope.RESEARCH_SAFETY_LITE, scope.SHARED_MODEL_RESEARCH}
        )


@pytest.mark.parametrize("path", sorted(scope.REVENUE_CONTENT_SCOPED_PATHS))
def test_marked_revenue_only_change_in_shared_readiness_file_selects_revenue_only(
    path: str,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    base = "def build(value):\n    return value\n"
    merge = (
        "def build(value):\n"
        f"    {scope.MODEL_OWNED_SCOPE_BEGIN}\n"
        "    revenue_unreacted_range_value = value\n"
        f"    {scope.MODEL_OWNED_SCOPE_END}\n"
        "    return value\n"
    )
    monkeypatch.setattr(
        scope,
        "_read_git_text",
        lambda revision, _path: base if revision == "base" else merge,
    )

    assert scope.domains_for_changed_path(
        path,
        base_sha="base",
        merge_sha="merge",
    ) == frozenset({scope.RESEARCH_SAFETY_LITE, scope.REVENUE_RESEARCH})


def test_unmarked_shared_readiness_semantic_change_keeps_broad_scope(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    path = "scripts/build_model_operation_readiness.py"
    base = "def build(value):\n    return value\n"
    merge = "def build(value):\n    return value + 1\n"
    monkeypatch.setattr(
        scope,
        "_read_git_text",
        lambda revision, _path: base if revision == "base" else merge,
    )

    assert not scope.is_revenue_owned_content_change(
        path,
        base_sha="base",
        merge_sha="merge",
    )
    assert scope.domains_for_changed_path(
        path,
        base_sha="base",
        merge_sha="merge",
        inventory_production_paths=frozenset(),
    ) == scope.domains_for_path(path)


def test_revenue_scope_marker_cannot_swallow_existing_shared_code(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    path = "scripts/validate_model_operation_readiness.py"
    base = "shared_contract = 1\ndef validate(value):\n    return value\n"
    merge = (
        f"{scope.MODEL_OWNED_SCOPE_BEGIN}\n"
        "shared_contract = 1\n"
        "revenue_unreacted_range_contract = 2\n"
        f"{scope.MODEL_OWNED_SCOPE_END}\n"
        "def validate(value):\n    return value\n"
    )
    monkeypatch.setattr(
        scope,
        "_read_git_text",
        lambda revision, _path: base if revision == "base" else merge,
    )

    assert not scope.is_revenue_owned_content_change(
        path,
        base_sha="base",
        merge_sha="merge",
    )
    assert scope.domains_for_changed_path(
        path,
        base_sha="base",
        merge_sha="merge",
        inventory_production_paths=frozenset(),
    ) == scope.domains_for_path(path)


def test_revenue_scope_marker_must_be_balanced(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    path = "tests/test_model_operation_readiness.py"
    base = "def test_existing():\n    assert True\n"
    merge = (
        "def test_existing():\n"
        "    assert True\n"
        f"{scope.MODEL_OWNED_SCOPE_BEGIN}\n"
        "def test_revenue_unreacted_range():\n    assert True\n"
    )
    monkeypatch.setattr(
        scope,
        "_read_git_text",
        lambda revision, _path: base if revision == "base" else merge,
    )

    assert not scope.is_revenue_owned_content_change(
        path,
        base_sha="base",
        merge_sha="merge",
    )
    assert scope.domains_for_changed_path(
        path,
        base_sha="base",
        merge_sha="merge",
        inventory_production_paths=frozenset(),
    ) == scope.domains_for_path(path)


def test_revenue_scope_marker_inside_string_is_not_treated_as_ownership(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    path = "scripts/build_model_operation_readiness.py"
    base = "def build(value):\n    return value\n"
    merge = (
        "ownership_text = '''\n"
        f"{scope.MODEL_OWNED_SCOPE_BEGIN}\n"
        "revenue_unreacted_range_contract = 2\n"
        f"{scope.MODEL_OWNED_SCOPE_END}\n"
        "'''\n"
        "def build(value):\n    return value\n"
    )
    monkeypatch.setattr(
        scope,
        "_read_git_text",
        lambda revision, _path: base if revision == "base" else merge,
    )

    assert scope.domains_for_changed_path(
        path,
        base_sha="base",
        merge_sha="merge",
        inventory_production_paths=frozenset(),
    ) == scope.domains_for_path(path)


def test_revenue_content_scope_missing_blob_falls_back_to_broad_scope(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    path = "scripts/build_model_operation_readiness.py"

    def fail_read(_revision: str, _path: str) -> str:
        raise scope.ScopeDetectionError("missing blob")

    monkeypatch.setattr(scope, "_read_git_text", fail_read)

    assert scope.domains_for_changed_path(
        path,
        base_sha="base",
        merge_sha="merge",
        inventory_production_paths=frozenset(),
    ) == scope.domains_for_path(path)


def test_revenue_content_scope_crlf_rewrite_outside_markers_falls_back_broad(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    path = "scripts/validate_model_operation_readiness.py"
    base = "shared_contract = 1\ndef validate(value):\n    return value\n"
    merge = (
        f"{scope.MODEL_OWNED_SCOPE_BEGIN}\r\n"
        "revenue_unreacted_range_contract = 2\r\n"
        f"{scope.MODEL_OWNED_SCOPE_END}\r\n"
        "shared_contract = 1\r\n"
        "def validate(value):\r\n    return value\r\n"
    )
    monkeypatch.setattr(
        scope,
        "_read_git_text",
        lambda revision, _path: base if revision == "base" else merge,
    )

    assert scope.domains_for_changed_path(
        path,
        base_sha="base",
        merge_sha="merge",
        inventory_production_paths=frozenset(),
    ) == scope.domains_for_path(path)


def test_existing_revenue_owned_block_can_evolve_without_broad_scope(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    path = "tests/test_model_operation_readiness.py"
    base = (
        f"{scope.MODEL_OWNED_SCOPE_BEGIN}\n"
        "revenue_unreacted_range_contract = 1\n"
        f"{scope.MODEL_OWNED_SCOPE_END}\n"
        "def test_shared():\n    assert True\n"
    )
    merge = base.replace("contract = 1", "contract = 2")
    monkeypatch.setattr(
        scope,
        "_read_git_text",
        lambda revision, _path: base if revision == "base" else merge,
    )

    assert scope.domains_for_changed_path(
        path,
        base_sha="base",
        merge_sha="merge",
    ) == frozenset({scope.RESEARCH_SAFETY_LITE, scope.REVENUE_RESEARCH})


def test_pull_request_marked_readiness_changes_select_revenue_without_core_or_shared(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    paths = sorted(scope.REVENUE_CONTENT_SCOPED_PATHS)
    base = "def existing(value):\n    return value\n"
    merge = (
        f"{scope.MODEL_OWNED_SCOPE_BEGIN}\n"
        "def revenue_unreacted_range_owned(value):\n    return value\n"
        f"{scope.MODEL_OWNED_SCOPE_END}\n"
        "def existing(value):\n    return value\n"
    )
    monkeypatch.setattr(scope, "changed_paths_from_git", lambda *_args: paths)
    monkeypatch.setattr(
        scope,
        "production_pdf_inventory_paths_for_range",
        lambda *_args: frozenset(),
    )
    monkeypatch.setattr(
        scope,
        "_read_git_text",
        lambda revision, _path: base if revision == "base" else merge,
    )

    result = scope.detect_scope(
        event_name="pull_request",
        base_sha="base",
        head_sha="head",
        merge_sha="merge",
    )

    assert result.selected_domains == (
        scope.RESEARCH_SAFETY_LITE,
        scope.REVENUE_RESEARCH,
    )


def test_all_tracked_legacy_validator_inputs_route_repo_current() -> None:
    unclassified = [
        path
        for path in sorted(legacy_validator_input_paths())
        if scope.REPO_CURRENT_CONTRACTS not in scope.domains_for_path(path)
    ]
    assert unclassified == []


@pytest.mark.parametrize("path", sorted(scope.SHARED_REGISTRY_KEY_FIELDS))
def test_shared_registry_revenue_only_change_keeps_core_and_revenue_without_production_pdf(
    path: str,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    key_field = scope.SHARED_REGISTRY_KEY_FIELDS[path]
    base = f"{key_field},owner,purpose\nscripts/revenue.py,research_backtest,old\n"
    merge = f"{key_field},owner,purpose\nscripts/revenue.py,research_backtest,revenue_unreacted_range new\n"
    monkeypatch.setattr(
        scope,
        "_read_git_text",
        lambda revision, _path: base if revision == "base" else merge,
    )

    assert scope.domains_for_changed_path(
        path,
        base_sha="base",
        merge_sha="merge",
    ) == frozenset(
        {
            scope.REPO_CURRENT_CONTRACTS,
            scope.RESEARCH_SAFETY_LITE,
            scope.REVENUE_RESEARCH,
        }
    )


@pytest.mark.parametrize("path", sorted(scope.SHARED_REGISTRY_KEY_FIELDS))
def test_shared_registry_daily_production_row_change_selects_production_pdf(
    path: str,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    key_field = scope.SHARED_REGISTRY_KEY_FIELDS[path]
    base = f"{key_field},owner,purpose\nscripts/daily.py,daily_production,old\n"
    merge = f"{key_field},owner,purpose\nscripts/daily.py,daily_production,new\n"
    monkeypatch.setattr(
        scope,
        "_read_git_text",
        lambda revision, _path: base if revision == "base" else merge,
    )

    assert scope.domains_for_changed_path(
        path,
        base_sha="base",
        merge_sha="merge",
    ) == frozenset(
        {scope.REPO_CURRENT_CONTRACTS, scope.PRODUCTION_PDF_CONTRACTS}
    )


def test_shared_registry_unchanged_pdf_edge_does_not_promote_revenue_metadata_change(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    path = "config/repo_file_lifecycle_inventory.csv"
    header = "path,owner,called_by_workflow,documented_by\n"
    base = (
        header
        + "scripts/validate_repo_production_inventory.py,repo_infrastructure,"
        ".github/workflows/daily_pdf_replay_pr_validation.yml,docs/old.md\n"
    )
    merge = (
        header
        + "scripts/validate_repo_production_inventory.py,repo_infrastructure,"
        ".github/workflows/daily_pdf_replay_pr_validation.yml,"
        "docs/old.md;docs/specs/revenue_unreacted_range_readiness_bootstrap_hardening_v1.md\n"
    )
    monkeypatch.setattr(
        scope,
        "_read_git_text",
        lambda revision, _path: base if revision == "base" else merge,
    )

    assert scope.domains_for_changed_path(
        path,
        base_sha="base",
        merge_sha="merge",
    ) == frozenset(
        {
            scope.REPO_CURRENT_CONTRACTS,
            scope.RESEARCH_SAFETY_LITE,
            scope.REVENUE_RESEARCH,
        }
    )


@pytest.mark.parametrize("edge_revision", ("base", "merge"))
def test_shared_registry_pdf_edge_delta_selects_production_pdf(
    edge_revision: str,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    path = "config/repo_production_inventory.csv"
    header = "path,owner,allowed_workflows,purpose\n"
    plain = header + "scripts/helper.py,repo_infrastructure,,metadata\n"
    with_edge = (
        header
        + "scripts/helper.py,repo_infrastructure,"
        ".github/workflows/daily_full_pipeline.yml,metadata\n"
    )
    monkeypatch.setattr(
        scope,
        "_read_git_text",
        lambda revision, _path: with_edge if revision == edge_revision else plain,
    )

    assert scope.domains_for_changed_path(
        path,
        base_sha="base",
        merge_sha="merge",
    ) == frozenset(
        {scope.REPO_CURRENT_CONTRACTS, scope.PRODUCTION_PDF_CONTRACTS}
    )


def test_shared_registry_explicit_pdf_primary_path_change_selects_production_pdf(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    path = "config/repo_file_lifecycle_inventory.csv"
    header = "path,owner,purpose\n"
    base = header + "scripts/generate_chatgpt_side_daily_reports.py,repo_infrastructure,old\n"
    merge = header + "scripts/generate_chatgpt_side_daily_reports.py,repo_infrastructure,new\n"
    monkeypatch.setattr(
        scope,
        "_read_git_text",
        lambda revision, _path: base if revision == "base" else merge,
    )

    assert scope.domains_for_changed_path(
        path,
        base_sha="base",
        merge_sha="merge",
    ) == frozenset(
        {scope.REPO_CURRENT_CONTRACTS, scope.PRODUCTION_PDF_CONTRACTS}
    )


@pytest.mark.parametrize("row_revision", ("base", "merge"))
def test_shared_registry_added_or_deleted_pdf_row_uses_complete_row_semantics(
    row_revision: str,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    path = "config/repo_file_lifecycle_inventory.csv"
    header = "path,owner,called_by_workflow\n"
    empty = header
    with_row = (
        header
        + "scripts/helper.py,repo_infrastructure,"
        ".github/workflows/daily_full_pipeline.yml\n"
    )
    monkeypatch.setattr(
        scope,
        "_read_git_text",
        lambda revision, _path: with_row if revision == row_revision else empty,
    )

    assert scope.domains_for_changed_path(
        path,
        base_sha="base",
        merge_sha="merge",
    ) == frozenset(
        {scope.REPO_CURRENT_CONTRACTS, scope.PRODUCTION_PDF_CONTRACTS}
    )


def test_shared_registry_unreadable_state_fails_closed_to_core_production_and_revenue(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.setattr(
        scope,
        "_read_git_text",
        lambda *_args: (_ for _ in ()).throw(
            scope.ScopeDetectionError("missing blob")
        ),
    )

    assert scope.domains_for_changed_path(
        "config/repo_production_inventory.csv",
        base_sha="base",
        merge_sha="merge",
    ) == frozenset(
        {
            scope.REPO_CURRENT_CONTRACTS,
            scope.PRODUCTION_PDF_CONTRACTS,
            scope.RESEARCH_SAFETY_LITE,
            scope.REVENUE_RESEARCH,
        }
    )


def test_shared_registry_crlf_only_rewrite_keeps_core_without_semantic_domains(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    path = "config/repo_production_inventory.csv"
    base = "path,owner,purpose\nscripts/revenue.py,research_backtest,revenue_unreacted_range\n"
    merge = base.replace("\n", "\r\n")
    monkeypatch.setattr(
        scope,
        "_read_git_text",
        lambda revision, _path: base if revision == "base" else merge,
    )

    assert scope.domains_for_changed_path(
        path,
        base_sha="base",
        merge_sha="merge",
    ) == frozenset({scope.REPO_CURRENT_CONTRACTS})


@pytest.mark.parametrize(
    "path",
    (
        "ensure_daily_report_readme.py",
        "build_chatgpt_daily_report_rules.py",
        "publish_chatgpt_report_readme_and_check.py",
        "scripts/validate_daily_report_source_preflight.py",
    ),
)
def test_current_inventory_relationships_select_production_pdf_without_handwritten_taxonomy(
    path: str,
) -> None:
    revision = subprocess.run(
        ["git", "rev-parse", "HEAD"],
        cwd=ROOT,
        check=True,
        text=True,
        encoding="utf-8",
        stdout=subprocess.PIPE,
    ).stdout.strip()

    assert not scope.is_production_pdf_path(path)
    assert scope.domains_for_changed_path(
        path,
        base_sha=revision,
        merge_sha=revision,
    ) == frozenset(
        {scope.REPO_CURRENT_CONTRACTS, scope.PRODUCTION_PDF_CONTRACTS}
    )


@pytest.mark.parametrize(
    "path",
    (
        "scripts/validate_revenue_unreacted_range_promotion_preparation.py",
        "tests/test_revenue_unreacted_range_source_first_condition_audit.py",
        "scripts/build_financial_statement_pit.py",
    ),
)
def test_inventory_relationships_do_not_spread_production_pdf_across_siblings(
    path: str,
) -> None:
    revision = subprocess.run(
        ["git", "rev-parse", "HEAD"],
        cwd=ROOT,
        check=True,
        text=True,
        encoding="utf-8",
        stdout=subprocess.PIPE,
    ).stdout.strip()

    assert path not in scope.production_pdf_inventory_paths_for_range(
        revision,
        revision,
    )


@pytest.mark.parametrize("relationship_revision", ("base", "head"))
def test_inventory_production_pdf_coverage_reads_both_sides_of_range(
    relationship_revision: str,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    target = "scripts/formal_report_control.py"

    def fake_read(revision: str, path: str) -> str:
        key_field = scope.SHARED_REGISTRY_KEY_FIELDS[path]
        header = f"{key_field},owner,called_by_workflow\n"
        if revision == relationship_revision:
            return (
                header
                + f"{target},repo_infrastructure,.github/workflows/daily_full_pipeline.yml\n"
            )
        return header

    monkeypatch.setattr(scope, "_read_git_text", fake_read)

    assert target in scope.production_pdf_inventory_paths_for_range("base", "head")


def test_unrelated_path_is_ignored() -> None:
    assert scope.domains_for_path("docs/unrelated_release_note.md") == frozenset()


@pytest.mark.parametrize(
    "path",
    (
        "scripts/daily_alpha_signal_engine.py",
        "output/latest/daily_alpha_signal_latest.csv",
    ),
)
def test_unknown_model_like_path_fails_closed(path: str) -> None:
    with pytest.raises(scope.ScopeDetectionError, match="no declared validation domain"):
        scope.domains_for_path(path)


def test_apps_script_research_dispatch_registry_routes_to_repo_current_contracts() -> None:
    path = "config/apps_script_research_dispatch_inputs.csv"

    assert scope.is_watched_path(path)
    assert not scope.is_model_like_path(path)
    assert scope.domains_for_path(path) == frozenset({scope.REPO_CURRENT_CONTRACTS})


@pytest.mark.parametrize(
    "path",
    (
        "scripts/build_non_revenue_momentum_watch.py",
        "scripts/research_tdcc_dataset_consumer.py",
        "tests/test_research_tdcc_dataset_consumer.py",
    ),
)
def test_known_other_lane_paths_are_fast_pass_unrelated(path: str) -> None:
    assert not scope.is_watched_path(path)
    assert not scope.is_model_like_path(path)
    assert scope.domains_for_path(path) == frozenset()


def test_workflow_dispatch_selects_all_domains_without_reading_git(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.setattr(
        scope,
        "changed_paths_from_git",
        lambda *_args: pytest.fail("workflow_dispatch must not read a PR diff"),
    )

    result = scope.detect_scope(event_name="workflow_dispatch")

    assert result.changed_paths == ()
    assert result.watched_paths == ()
    assert result.selected_domains == scope.DOMAINS


def test_workflow_dispatch_revenue_profile_selects_safety_and_revenue_only() -> None:
    result = scope.detect_scope(
        event_name="workflow_dispatch",
        validation_profile="revenue-research",
    )

    assert result.selected_domains == (
        scope.RESEARCH_SAFETY_LITE,
        scope.REVENUE_RESEARCH,
    )


def test_workflow_dispatch_rejects_unknown_profile() -> None:
    with pytest.raises(scope.ScopeDetectionError, match="unsupported.*validation profile"):
        scope.detect_scope(
            event_name="workflow_dispatch",
            validation_profile="revenue-without-safety",
        )


def test_pull_request_requires_all_three_commit_objects() -> None:
    with pytest.raises(scope.ScopeDetectionError, match="base, head, and synthetic merge"):
        scope.detect_scope(event_name="pull_request", base_sha="abc")


def test_unsupported_event_fails_closed() -> None:
    with pytest.raises(scope.ScopeDetectionError, match="unsupported event"):
        scope.detect_scope(event_name="push")


def test_unrelated_nonempty_diff_fast_passes_with_no_domains(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.setattr(
        scope, "changed_paths_from_git", lambda *_args: ["README.md"]
    )
    monkeypatch.setattr(
        scope,
        "production_pdf_inventory_paths_for_range",
        lambda *_args: frozenset(),
    )

    result = scope.detect_scope(
        event_name="pull_request",
        base_sha="base",
        head_sha="head",
        merge_sha="merge",
    )

    assert result.changed_paths == ("README.md",)
    assert result.watched_paths == ()
    assert result.selected_domains == ()


def test_empty_effective_diff_fails_closed(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr(scope, "changed_paths_from_git", lambda *_args: [])

    with pytest.raises(scope.ScopeDetectionError, match="effective tree diff is empty"):
        scope.detect_scope(
            event_name="pull_request",
            base_sha="base",
            head_sha="head",
            merge_sha="merge",
        )


def test_pull_request_fails_closed_when_production_inventory_is_unreadable(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.setattr(
        scope, "changed_paths_from_git", lambda *_args: ["README.md"]
    )
    monkeypatch.setattr(
        scope,
        "_read_git_text",
        lambda *_args: (_ for _ in ()).throw(
            scope.ScopeDetectionError("missing production inventory")
        ),
    )

    with pytest.raises(scope.ScopeDetectionError, match="missing production inventory"):
        scope.detect_scope(
            event_name="pull_request",
            base_sha="base",
            head_sha="head",
            merge_sha="merge",
        )


def test_pull_request_combines_relevant_domains_only(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    monkeypatch.setattr(
        scope,
        "changed_paths_from_git",
        lambda *_args: [
            "README.md",
            ".github/workflows/daily_full_pipeline.yml",
            "scripts/validate_revenue_unreacted_range_source_snapshot_projection.py",
        ],
    )
    monkeypatch.setattr(
        scope,
        "production_pdf_inventory_paths_for_range",
        lambda *_args: frozenset(),
    )

    result = scope.detect_scope(
        event_name="pull_request",
        base_sha="base",
        head_sha="head",
        merge_sha="merge",
    )

    assert result.watched_paths == (
        ".github/workflows/daily_full_pipeline.yml",
        "scripts/validate_revenue_unreacted_range_source_snapshot_projection.py",
    )
    assert result.selected_domains == (
        scope.REPO_CURRENT_CONTRACTS,
        scope.PRODUCTION_PDF_CONTRACTS,
        scope.RESEARCH_SAFETY_LITE,
        scope.REVENUE_RESEARCH,
    )


def test_name_status_parser_is_nul_safe_and_preserves_unusual_names() -> None:
    payload = (
        b"M\0.github/workflows/daily_full_pipeline.yml\0"
        b"A\0scripts/model file\nwith newline.py\0"
        b"D\0tests/trailing-space.py \0"
    )

    assert scope.parse_name_status_z(payload) == [
        ".github/workflows/daily_full_pipeline.yml",
        "scripts/model file\nwith newline.py",
        "tests/trailing-space.py ",
    ]


@pytest.mark.parametrize(
    "payload",
    (
        b"M\0missing-path-field",
        b"R100\0old.py\0new.py\0",
        b"M\0\0",
    ),
)
def test_name_status_parser_rejects_malformed_or_renamed_records(
    payload: bytes,
) -> None:
    with pytest.raises(scope.ScopeDetectionError):
        scope.parse_name_status_z(payload)


def test_git_diff_is_nul_delimited_no_renames_and_disables_replace_objects(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    calls: list[list[str]] = []

    def fake_run(args: list[str], **_kwargs: object) -> subprocess.CompletedProcess[bytes]:
        calls.append(args)
        if "diff" in args:
            return subprocess.CompletedProcess(
                args, 0, b"M\0.github/workflows/daily_full_pipeline.yml\0", b""
            )
        if "rev-list" in args:
            return subprocess.CompletedProcess(
                args, 0, b"merge base head\n", b""
            )
        return subprocess.CompletedProcess(args, 0, b"", b"")

    monkeypatch.setattr(scope.subprocess, "run", fake_run)

    assert scope.changed_paths_from_git("base", "head", "merge") == [
        ".github/workflows/daily_full_pipeline.yml"
    ]
    assert len(calls) == 5
    for args in calls:
        assert args[:2] == ["git", "--no-replace-objects"]
    diff_args = calls[-1]
    rev_list_args = calls[-2]
    assert rev_list_args[-1] == "merge"
    assert "--name-status" in diff_args
    assert "--no-renames" in diff_args
    assert "-z" in diff_args
    assert "base..merge" in diff_args


def test_missing_commit_object_fails_before_diff(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    calls: list[list[str]] = []

    def fake_run(args: list[str], **_kwargs: object) -> subprocess.CompletedProcess[bytes]:
        calls.append(args)
        return subprocess.CompletedProcess(args, 1, b"", b"missing")

    monkeypatch.setattr(scope.subprocess, "run", fake_run)

    with pytest.raises(scope.ScopeDetectionError, match="not an available commit"):
        scope.changed_paths_from_git("missing-base", "head", "merge")
    assert len(calls) == 1
    assert "cat-file" in calls[0]


def test_diff_failure_is_not_treated_as_an_empty_scope(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    def fake_run(args: list[str], **_kwargs: object) -> subprocess.CompletedProcess[bytes]:
        if "rev-list" in args:
            return subprocess.CompletedProcess(
                args, 0, b"merge base head\n", b""
            )
        if "diff" not in args:
            return subprocess.CompletedProcess(args, 0, b"", b"")
        return subprocess.CompletedProcess(args, 128, b"", b"diff exploded")

    monkeypatch.setattr(scope.subprocess, "run", fake_run)

    with pytest.raises(scope.ScopeDetectionError, match="git diff failed"):
        scope.changed_paths_from_git("base", "head", "merge")


def test_rev_list_failure_is_not_treated_as_a_scope_result(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    def fake_run(args: list[str], **_kwargs: object) -> subprocess.CompletedProcess[bytes]:
        if "rev-list" in args:
            return subprocess.CompletedProcess(args, 128, b"", b"cannot inspect")
        return subprocess.CompletedProcess(args, 0, b"", b"")

    monkeypatch.setattr(scope.subprocess, "run", fake_run)

    with pytest.raises(scope.ScopeDetectionError, match="cannot inspect"):
        scope.changed_paths_from_git("base", "head", "merge")


@pytest.mark.parametrize(
    ("parents", "message"),
    (
        (b"merge base\n", "two-parent"),
        (b"merge wrong-base head\n", "base parent mismatch"),
        (b"merge base wrong-head\n", "head parent mismatch"),
        (b"wrong-merge base head\n", "merge SHA mismatch"),
    ),
)
def test_synthetic_merge_identity_mismatch_fails_closed(
    parents: bytes,
    message: str,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    def fake_run(args: list[str], **_kwargs: object) -> subprocess.CompletedProcess[bytes]:
        if "rev-list" in args:
            return subprocess.CompletedProcess(args, 0, parents, b"")
        return subprocess.CompletedProcess(args, 0, b"", b"")

    monkeypatch.setattr(scope.subprocess, "run", fake_run)

    with pytest.raises(scope.ScopeDetectionError, match=message):
        scope.changed_paths_from_git("base", "head", "merge")


def test_explicit_merge_identity_does_not_require_head(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    repo, base_sha, head_sha, merge_sha = init_repo(tmp_path)
    run_git(repo, "symbolic-ref", "HEAD", "refs/heads/unborn")
    head_probe = subprocess.run(
        ["git", "--no-replace-objects", "rev-parse", "--verify", "HEAD"],
        cwd=repo,
        check=False,
        capture_output=True,
    )
    assert head_probe.returncode != 0
    monkeypatch.setattr(scope, "ROOT", repo)

    assert scope.changed_paths_from_git(base_sha, head_sha, merge_sha) == [
        ".github/workflows/daily_full_pipeline.yml"
    ]


def test_real_git_diff_detects_the_routine_workflow_as_core_and_production_pdf(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    repo, base_sha, head_sha, merge_sha = init_repo(tmp_path)
    monkeypatch.setattr(scope, "ROOT", repo)

    result = scope.detect_scope(
        event_name="pull_request",
        base_sha=base_sha,
        head_sha=head_sha,
        merge_sha=merge_sha,
    )

    assert result.watched_paths == (
        ".github/workflows/daily_full_pipeline.yml",
    )
    assert result.selected_domains == (
        scope.REPO_CURRENT_CONTRACTS,
        scope.PRODUCTION_PDF_CONTRACTS,
    )


@pytest.mark.parametrize(
    ("path", "expected"),
    (
        (
            "data/monthly_revenue_history/monthly_revenue_history.csv",
            {scope.RESEARCH_SAFETY_LITE, scope.REVENUE_RESEARCH},
        ),
        (
            "docs/latest/revenue_unreacted_range_scope_probe.csv",
            {scope.RESEARCH_SAFETY_LITE, scope.REVENUE_RESEARCH},
        ),
        (
            "docs/latest/volume_v2_scope_probe.csv",
            {scope.RESEARCH_SAFETY_LITE, scope.VOLUME_V2_RESEARCH},
        ),
        (
            "output/history/daily_model_snapshots/scope_probe.csv",
            {
                scope.REPO_CURRENT_CONTRACTS,
                scope.PRODUCTION_PDF_CONTRACTS,
                scope.RESEARCH_SAFETY_LITE,
                scope.SHARED_MODEL_RESEARCH,
                scope.VOLUME_V2_RESEARCH,
            },
        ),
    ),
)
def test_real_git_diff_routes_owned_data_docs_and_output(
    path: str,
    expected: set[str],
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    repo, base_sha, head_sha, merge_sha = init_repo(tmp_path, path)
    monkeypatch.setattr(scope, "ROOT", repo)

    result = scope.detect_scope(
        event_name="pull_request",
        base_sha=base_sha,
        head_sha=head_sha,
        merge_sha=merge_sha,
    )

    assert result.watched_paths == (path,)
    assert set(result.selected_domains) == expected


def test_real_git_rename_selects_both_old_and_new_path_domains(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    repo = tmp_path / "rename-repo"
    repo.mkdir()
    run_git(repo, "init", "--initial-branch=main")
    run_git(repo, "config", "user.email", "scope-test@example.invalid")
    run_git(repo, "config", "user.name", "Scope Test")
    write_minimal_scope_inventories(repo)
    old_path = repo / "scripts" / "build_volume_v2_warrant_lineage_history_audit.py"
    old_path.parent.mkdir(parents=True)
    old_path.write_text("old\n", encoding="utf-8")
    run_git(repo, "add", "--all")
    run_git(repo, "commit", "-m", "base")
    base_sha = run_git(repo, "rev-parse", "HEAD")
    run_git(repo, "switch", "-c", "feature")
    new_rel = "scripts/validate_revenue_unreacted_range_new_projection.py"
    run_git(repo, "mv", old_path.relative_to(repo).as_posix(), new_rel)
    run_git(repo, "commit", "-m", "rename across domains")
    head_sha = run_git(repo, "rev-parse", "HEAD")
    run_git(repo, "switch", "main")
    run_git(repo, "merge", "--no-ff", "feature", "-m", "synthetic merge")
    merge_sha = run_git(repo, "rev-parse", "HEAD")
    monkeypatch.setattr(scope, "ROOT", repo)

    result = scope.detect_scope(
        event_name="pull_request",
        base_sha=base_sha,
        head_sha=head_sha,
        merge_sha=merge_sha,
    )

    assert result.watched_paths == (
        "scripts/build_volume_v2_warrant_lineage_history_audit.py",
        new_rel,
    )
    assert result.selected_domains == (
        scope.RESEARCH_SAFETY_LITE,
        scope.VOLUME_V2_RESEARCH,
        scope.REVENUE_RESEARCH,
    )


def test_real_git_deletion_keeps_the_deleted_paths_domains(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    repo = tmp_path / "delete-repo"
    repo.mkdir()
    run_git(repo, "init", "--initial-branch=main")
    run_git(repo, "config", "user.email", "scope-test@example.invalid")
    run_git(repo, "config", "user.name", "Scope Test")
    write_minimal_scope_inventories(repo)
    deleted_rel = "scripts/build_financial_statement_historical_pit_source_audit.py"
    deleted = repo / deleted_rel
    deleted.parent.mkdir(parents=True)
    deleted.write_text("delete me\n", encoding="utf-8")
    run_git(repo, "add", "--all")
    run_git(repo, "commit", "-m", "base")
    base_sha = run_git(repo, "rev-parse", "HEAD")
    run_git(repo, "switch", "-c", "feature")
    run_git(repo, "rm", deleted_rel)
    run_git(repo, "commit", "-m", "delete financial path")
    head_sha = run_git(repo, "rev-parse", "HEAD")
    run_git(repo, "switch", "main")
    run_git(repo, "merge", "--no-ff", "feature", "-m", "synthetic merge")
    merge_sha = run_git(repo, "rev-parse", "HEAD")
    monkeypatch.setattr(scope, "ROOT", repo)

    result = scope.detect_scope(
        event_name="pull_request",
        base_sha=base_sha,
        head_sha=head_sha,
        merge_sha=merge_sha,
    )

    assert result.watched_paths == (deleted_rel,)
    assert result.selected_domains == (
        scope.RESEARCH_SAFETY_LITE,
        scope.REVENUE_RESEARCH,
        scope.FINANCIAL_STATEMENT_RESEARCH,
    )


def test_base_to_synthetic_merge_diff_excludes_base_only_advances(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    repo = tmp_path / "advanced-base-repo"
    repo.mkdir()
    run_git(repo, "init", "--initial-branch=main")
    run_git(repo, "config", "user.email", "scope-test@example.invalid")
    run_git(repo, "config", "user.name", "Scope Test")
    write_minimal_scope_inventories(repo)
    marker = repo / "README.md"
    marker.write_text("common\n", encoding="utf-8")
    run_git(repo, "add", "--all")
    run_git(repo, "commit", "-m", "common")
    run_git(repo, "switch", "-c", "feature")
    feature_path = repo / ".github" / "workflows" / "daily_full_pipeline.yml"
    feature_path.parent.mkdir(parents=True)
    feature_path.write_text("name: feature\n", encoding="utf-8")
    run_git(repo, "add", feature_path.relative_to(repo).as_posix())
    run_git(repo, "commit", "-m", "feature")
    head_sha = run_git(repo, "rev-parse", "HEAD")
    run_git(repo, "switch", "main")
    base_only_rel = "scripts/build_volume_v2_warrant_lineage_history_audit.py"
    base_only = repo / base_only_rel
    base_only.parent.mkdir(parents=True)
    base_only.write_text("base advance\n", encoding="utf-8")
    run_git(repo, "add", base_only_rel)
    run_git(repo, "commit", "-m", "advance base")
    base_sha = run_git(repo, "rev-parse", "HEAD")
    run_git(repo, "merge", "--no-ff", "feature", "-m", "synthetic merge")
    merge_sha = run_git(repo, "rev-parse", "HEAD")
    monkeypatch.setattr(scope, "ROOT", repo)

    result = scope.detect_scope(
        event_name="pull_request",
        base_sha=base_sha,
        head_sha=head_sha,
        merge_sha=merge_sha,
    )

    assert result.watched_paths == (
        ".github/workflows/daily_full_pipeline.yml",
    )
    assert base_only_rel not in result.changed_paths
    assert result.selected_domains == (
        scope.REPO_CURRENT_CONTRACTS,
        scope.PRODUCTION_PDF_CONTRACTS,
    )


def test_github_output_records_each_domain_and_counts(tmp_path: Path) -> None:
    output = tmp_path / "github-output.txt"
    result = scope.ScopeResult(
        changed_paths=("README.md", "scripts/model_data_independence.py"),
        watched_paths=("scripts/model_data_independence.py",),
        selected_domains=(
            scope.REPO_CURRENT_CONTRACTS,
            scope.RESEARCH_SAFETY_LITE,
            scope.SHARED_MODEL_RESEARCH,
        ),
    )

    scope.write_github_output(output, result)

    assert output.read_text(encoding="utf-8").splitlines() == [
        "repo_current_contracts=true",
        "production_pdf_contracts=false",
        "research_safety_lite=true",
        "shared_model_research=true",
        "volume_v2_research=false",
        "revenue_research=false",
        "financial_statement_research=false",
        "changed_count=2",
        "watched_count=1",
    ]
