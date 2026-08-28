from __future__ import annotations

import csv
import io
from pathlib import Path
import subprocess

import pytest

from scripts import validate_repo_production_inventory as inventory


ROOT = Path(__file__).resolve().parents[1]
VOLUME_V2_ADVISORY_LINEAGE_REFRESH_WORKFLOW = (
    ".github/workflows/volume_v2_advisory_lineage_refresh.yml"
)
RESEARCH_BACKTEST_WORKFLOW = ".github/workflows/research_backtest_pipeline.yml"
MODEL_DATA_AUDIT_STAGE_PATTERNS = (
    "git add -- output/latest/model_data_independence_audit_latest.csv",
    "git add -- docs/latest/model_data_independence_audit_latest.csv",
    "git add -- output/latest/model_data_independence_audit_latest.md",
    "git add -- docs/latest/model_data_independence_audit_latest.md",
)
BASELINE_ARTIFACT_WRITER_COUNT = 14


def assert_transition_safe_artifact_writer_count(
    writer_count: int,
    workflow_paths: set[str],
) -> None:
    expected_count = BASELINE_ARTIFACT_WRITER_COUNT + int(
        VOLUME_V2_ADVISORY_LINEAGE_REFRESH_WORKFLOW in workflow_paths
    )
    assert writer_count == expected_count




def test_repo_production_inventory_validator_passes() -> None:
    assert inventory.main() == 0
































































def test_inventory_manifest_exists_and_is_authoritative() -> None:
    manifest = ROOT / "config" / "repo_production_inventory.csv"
    docs = ROOT / "docs" / "repo_production_inventory.md"

    assert manifest.exists()
    assert docs.exists()
    assert "config/repo_production_inventory.csv" in docs.read_text(encoding="utf-8")
    assert "tests/**/*.py" in docs.read_text(encoding="utf-8")
    assert "executable_script" in docs.read_text(encoding="utf-8")
































def test_required_workflow_command_validation_rejects_missing_command() -> None:
    workflow_path = ".github/workflows/fixture_required_commands.yml"
    fixture_commands = (
        "python fixtures/required_gate_fixture.py",
        "python fixtures/second_required_gate_fixture.py --required-mode",
    )
    expected_error = f"{workflow_path} must run {fixture_commands[1]}"
    for workflow_text in (
        f"{fixture_commands[0]}\n",
        (
            f"{fixture_commands[0]}\n"
            "python fixtures/second_required_gate_fixture.py "
            "--required-mode-extra\n"
        ),
    ):
        errors: list[str] = []
        inventory.validate_required_workflow_commands(
            workflow_path,
            workflow_text,
            fixture_commands,
            errors,
        )
        assert errors == [expected_error]


def test_individual_pr_static_command_contract_is_exact() -> None:
    workflow_path = ".github/workflows/individual_stock_pr_validation.yml"
    workflow_text = (ROOT / workflow_path).read_text(encoding="utf-8")

    assert inventory.validate_regular_pr_static_validation_step(workflow_text) == []
    registered = inventory.REQUIRED_WORKFLOW_COMMANDS[workflow_path]
    assert registered[: len(inventory.PR_STATIC_VALIDATION_COMMANDS)] == (
        inventory.PR_STATIC_VALIDATION_COMMANDS
    )
    assert "python scripts/validate_individual_pdf_contract_consumers.py" in registered


def test_daily_pdf_runtime_command_contract_is_owned_by_daily_production_boundaries() -> None:
    assert inventory.DAILY_WORKFLOW not in inventory.REQUIRED_WORKFLOW_COMMANDS


def test_daily_model_workflow_keeps_five_static_pdf_contracts() -> None:
    commands = inventory.REQUIRED_WORKFLOW_COMMANDS[
        ".github/workflows/daily_model_maintenance_pr_validation.yml"
    ]
    required = {
        "python scripts/validate_chatgpt_side_pdf_contract.py",
        "python scripts/validate_daily_pdf_contract_consumers.py",
        "python scripts/validate_daily_pdf_role_manifest_contract.py",
        "python scripts/validate_daily_pdf_shared_path_isolation.py",
        "python scripts/validate_daily_pdf_completion_hard_gate.py",
    }

    assert required.issubset(commands)


def test_repair_and_historical_runtime_do_not_require_repo_static_self_hooks() -> None:
    historical = ".github/workflows/historical_structured_source_replay.yml"
    repair = ".github/workflows/repair_recent_daily_price_gaps.yml"
    static_commands = {
        "python scripts/validate_apps_script_workflow_triggers.py",
        "python scripts/validate_repo_production_inventory.py",
        "python scripts/validate_repo_file_lifecycle_inventory.py",
        "python scripts/validate_repo_semantic_integrity.py",
        "python scripts/validate_daily_production_boundaries.py",
        "python scripts/validate_recent_structured_source_repair_workflow.py",
    }

    assert set(inventory.REQUIRED_WORKFLOW_COMMANDS[historical]).isdisjoint(
        static_commands
    )
    assert repair not in inventory.REQUIRED_WORKFLOW_COMMANDS


























































def test_inventory_covers_tests_and_non_python_executables() -> None:
    manifest = ROOT / "config" / "repo_production_inventory.csv"
    with manifest.open("r", encoding="utf-8-sig", newline="") as fh:
        rows = {row["path"]: row for row in csv.DictReader(fh)}

    assert rows["tests/conftest.py"]["kind"] == "test_python"
    assert rows["scripts/ci_push_with_retry.sh"]["kind"] == "executable_script"
    assert rows["docs/apps_script_workflow_trigger.gs"]["kind"] == "executable_script"


def test_inventory_covers_revenue_operation_lag_bucket_audit() -> None:
    manifest = ROOT / "config" / "repo_production_inventory.csv"
    with manifest.open("r", encoding="utf-8-sig", newline="") as fh:
        rows = {row["path"]: row for row in csv.DictReader(fh)}

    expected = {
        "scripts/revenue_unreacted_range_operation_lag_bucket_audit.py": "python",
        "scripts/validate_revenue_unreacted_range_operation_lag_bucket_audit.py": "python",
        "tests/test_revenue_unreacted_range_operation_lag_bucket_audit.py": "test_python",
    }
    for path, kind in expected.items():
        assert rows[path]["kind"] == kind
        assert rows[path]["owner"] == "research_backtest"
        assert rows[path]["status"] == "active"


def test_all_registered_workflow_commands_match_their_call_graph() -> None:
    for workflow_path, commands in inventory.REQUIRED_WORKFLOW_COMMANDS.items():
        if (ROOT / workflow_path).exists():
            workflow_text = (ROOT / workflow_path).read_text(encoding="utf-8")
        else:
            assert workflow_path == (
                ".github/workflows/volume_v2_advisory_lineage_refresh.yml"
            )
            frozen_workflow = inventory.git_blob_at_ref(
                "HEAD",
                workflow_path,
            )
            assert frozen_workflow is not None
            workflow_text = frozen_workflow.decode("utf-8")
        for command in commands:
            assert inventory.workflow_contains_required_command(workflow_text, command)


def test_weekly_and_warrant_workflows_do_not_stage_source_files() -> None:
    for workflow_path in (
        ".github/workflows/tdcc_weekly.yml",
        ".github/workflows/tdcc_history_backfill.yml",
        ".github/workflows/warrant_flow.yml",
    ):
        workflow_text = (ROOT / workflow_path).read_text(encoding="utf-8")
        assert "git add scripts/" not in workflow_text
        assert "git add .github/workflows/" not in workflow_text


def test_repo_inventory_runs_in_pr_static_job_not_daily_runtime() -> None:
    command = "python scripts/validate_repo_production_inventory.py"
    pr_workflow = (
        ROOT / ".github" / "workflows" / "individual_stock_pr_validation.yml"
    ).read_text(encoding="utf-8")
    daily_workflow = (ROOT / inventory.DAILY_WORKFLOW).read_text(encoding="utf-8")

    assert inventory.validate_regular_pr_static_validation_step(pr_workflow) == []
    static_step_start = pr_workflow.index("      - name: Validate repository static contracts")
    static_step_end = pr_workflow.index("\n      - name:", static_step_start + 1)
    static_step = pr_workflow[static_step_start:static_step_end]
    assert static_step.count(command) == 1
    assert command not in daily_workflow


def test_daily_boundary_validator_runs_repo_inventory_gate() -> None:
    boundary_text = (ROOT / "scripts" / "validate_daily_production_boundaries.py").read_text(
        encoding="utf-8"
    )

    assert "validate_repo_production_inventory.py" in boundary_text


def test_all_inventory_artifact_writers_use_the_deploy_key() -> None:
    errors: list[str] = []
    rows = inventory.load_inventory(errors)
    workflow_paths = inventory.tracked_workflow_paths()
    writer_rows = [
        row
        for row in rows.values()
        if row.kind == "workflow" and row.allowed_stage_patterns
    ]

    inventory.validate_production_artifact_writer_auth(rows, workflow_paths, errors)

    assert_transition_safe_artifact_writer_count(len(writer_rows), workflow_paths)
    assert errors == []


def test_research_writer_inventory_locks_exact_model_data_audit_mirrors() -> None:
    errors: list[str] = []
    rows = inventory.load_inventory(errors)
    workflow_text = (ROOT / RESEARCH_BACKTEST_WORKFLOW).read_text(encoding="utf-8")
    audit_patterns = tuple(
        pattern
        for pattern in rows[RESEARCH_BACKTEST_WORKFLOW].allowed_stage_patterns
        if "model_data_independence_audit_latest" in pattern
    )

    assert errors == []
    assert audit_patterns == MODEL_DATA_AUDIT_STAGE_PATTERNS
    assert all(workflow_text.count(pattern) == 1 for pattern in audit_patterns)


def test_artifact_writer_count_transition_accepts_only_the_target_workflow() -> None:
    target = VOLUME_V2_ADVISORY_LINEAGE_REFRESH_WORKFLOW
    rogue = ".github/workflows/rogue_artifact_writer.yml"

    assert_transition_safe_artifact_writer_count(14, set())
    assert_transition_safe_artifact_writer_count(15, {target})
    with pytest.raises(AssertionError):
        assert_transition_safe_artifact_writer_count(15, {rogue})
    with pytest.raises(AssertionError):
        assert_transition_safe_artifact_writer_count(16, {target, rogue})


def test_reusable_writer_may_declare_the_required_deploy_key() -> None:
    workflow_path = ".github/workflows/historical_structured_source_replay.yml"
    text = (ROOT / workflow_path).read_text(encoding="utf-8")

    assert inventory.workflow_call_declared_secrets(text) == {
        inventory.PRODUCTION_ARTIFACT_WRITE_DEPLOY_KEY
    }

    errors: list[str] = []
    rows = inventory.load_inventory(errors)
    inventory.validate_production_artifact_writer_auth(
        rows,
        {workflow_path},
        errors,
    )

    assert errors == []


def test_recent_repair_passes_only_the_named_secret_to_registered_reusable_writer() -> None:
    workflow_path = ".github/workflows/repair_recent_daily_" + "price_gaps.yml"
    text = (ROOT / workflow_path).read_text(encoding="utf-8")
    jobs = inventory.workflow_job_blocks(text)
    block = jobs["replay-structured-objective-sources"]
    errors: list[str] = []

    assert inventory.local_reusable_workflow_path(block) == (
        ".github/workflows/historical_structured_source_replay.yml"
    )
    assert inventory.workflow_job_mapping(block, "secrets") == {
        inventory.PRODUCTION_ARTIFACT_WRITE_DEPLOY_KEY: (
            inventory.PRODUCTION_ARTIFACT_WRITE_SECRET_EXPRESSION
        )
    }
    inventory.validate_reusable_writer_delegate(
        workflow_path,
        "replay-structured-objective-sources",
        block,
        errors,
    )

    assert errors == []


def test_reusable_writer_rejects_inherit_or_extra_secrets() -> None:
    workflow_path = ".github/workflows/repair_recent_daily_" + "price_gaps.yml"
    text = (ROOT / workflow_path).read_text(encoding="utf-8")
    block = inventory.workflow_job_blocks(text)["replay-structured-objective-sources"]

    for invalid_block in (
        block.replace(
            "    secrets:\n"
            "      PRODUCTION_ARTIFACT_WRITE_DEPLOY_KEY: "
            "${{ secrets.PRODUCTION_ARTIFACT_WRITE_DEPLOY_KEY }}\n",
            "    secrets: inherit\n",
        ),
        block.replace(
            "    secrets:\n",
            "    secrets:\n      OTHER_SECRET: ${{ secrets.OTHER_SECRET }}\n",
        ),
    ):
        errors: list[str] = []
        inventory.validate_reusable_writer_delegate(
            workflow_path,
            "replay-structured-objective-sources",
            invalid_block,
            errors,
        )
        assert errors == [
            f"{workflow_path} reusable writer job replay-structured-objective-sources "
            "must pass exactly secrets.PRODUCTION_ARTIFACT_WRITE_DEPLOY_KEY and no "
            "other secrets"
        ]


def test_unregistered_reusable_job_is_not_a_writer_delegate() -> None:
    block = (
        "  unregistered:\n"
        "    uses: ./.github/workflows/not_registered.yml\n"
        "    secrets:\n"
        "      PRODUCTION_ARTIFACT_WRITE_DEPLOY_KEY: "
        "${{ secrets.PRODUCTION_ARTIFACT_WRITE_DEPLOY_KEY }}\n"
    )

    assert inventory.is_registered_reusable_writer_job(block, {}) is False


def test_daily_pipeline_only_gives_the_key_to_its_two_writer_jobs() -> None:
    text = (ROOT / ".github" / "workflows" / "daily_full_pipeline.yml").read_text(
        encoding="utf-8"
    )
    jobs = inventory.workflow_job_blocks(text)
    writer_jobs = {name for name, block in jobs.items() if inventory.is_artifact_push_job(block)}
    keyed_jobs = {
        name
        for name, block in jobs.items()
        if inventory.PRODUCTION_ARTIFACT_WRITE_DEPLOY_KEY in block
    }

    assert writer_jobs == {"record-market-closure", "daily-full-pipeline"}
    assert keyed_jobs == writer_jobs


def test_missing_deploy_key_is_rejected_for_writer_job() -> None:
    workflow_path = ".github/workflows/individual_stock_data_refresh.yml"
    text = (ROOT / workflow_path).read_text(encoding="utf-8")
    block = inventory.workflow_job_blocks(text)["individual-stock-data-refresh"]
    block = block.replace(f"          {inventory.PRODUCTION_ARTIFACT_WRITE_SSH_KEY}\n", "")
    errors: list[str] = []

    inventory.validate_artifact_push_job(
        workflow_path,
        "individual-stock-data-refresh",
        block,
        errors,
    )

    assert errors == [
        f"{workflow_path} writer job individual-stock-data-refresh must use "
        "secrets.PRODUCTION_ARTIFACT_WRITE_DEPLOY_KEY as actions/checkout ssh-key"
    ]


def test_checkout_auth_cannot_be_satisfied_by_comments_or_unrelated_steps() -> None:
    workflow_path = ".github/workflows/individual_stock_data_refresh.yml"
    text = (ROOT / workflow_path).read_text(encoding="utf-8")
    block = inventory.workflow_job_blocks(text)["individual-stock-data-refresh"]
    block = block.replace(
        f"          {inventory.PRODUCTION_ARTIFACT_WRITE_SSH_KEY}\n",
        f"          # {inventory.PRODUCTION_ARTIFACT_WRITE_SSH_KEY}\n",
    )
    block += (
        "      - name: Unrelated note\n"
        "        env:\n"
        f"          NOTE: '{inventory.PRODUCTION_ARTIFACT_WRITE_SSH_KEY}'\n"
        "        run: echo ok\n"
    )
    errors: list[str] = []

    inventory.validate_artifact_push_job(
        workflow_path,
        "individual-stock-data-refresh",
        block,
        errors,
    )

    assert errors == [
        f"{workflow_path} writer job individual-stock-data-refresh must use "
        "secrets.PRODUCTION_ARTIFACT_WRITE_DEPLOY_KEY as actions/checkout ssh-key"
    ]


def test_deploy_key_and_persist_credentials_must_share_one_checkout_step() -> None:
    workflow_path = ".github/workflows/individual_stock_data_refresh.yml"
    text = (ROOT / workflow_path).read_text(encoding="utf-8")
    block = inventory.workflow_job_blocks(text)["individual-stock-data-refresh"]
    block = block.replace(
        f"          {inventory.PRODUCTION_ARTIFACT_PERSIST_CREDENTIALS}\n",
        "",
        1,
    )
    block += (
        "      - name: Unkeyed secondary checkout\n"
        "        uses: actions/checkout@v6\n"
        "        with:\n"
        f"          {inventory.PRODUCTION_ARTIFACT_PERSIST_CREDENTIALS}\n"
    )
    errors: list[str] = []

    inventory.validate_artifact_push_job(
        workflow_path,
        "individual-stock-data-refresh",
        block,
        errors,
    )

    assert errors == [
        f"{workflow_path} writer job individual-stock-data-refresh must set "
        "persist-credentials: true in the same actions/checkout step as the deploy key"
    ]


def test_writer_job_requires_nonempty_secret_preflight_before_checkout() -> None:
    workflow_path = ".github/workflows/individual_stock_data_refresh.yml"
    text = (ROOT / workflow_path).read_text(encoding="utf-8")
    block = inventory.workflow_job_blocks(text)["individual-stock-data-refresh"]
    steps = inventory.workflow_step_blocks(block)
    preflight = next(
        step
        for step in steps
        if inventory.workflow_step_name(step)
        == inventory.PRODUCTION_ARTIFACT_WRITE_PREFLIGHT_NAME
    )
    checkout = next(step for step in steps if inventory.is_checkout_step(step))

    missing_errors: list[str] = []
    inventory.validate_artifact_push_job(
        workflow_path,
        "individual-stock-data-refresh",
        block.replace(preflight, ""),
        missing_errors,
    )
    assert missing_errors == [
        f"{workflow_path} writer job individual-stock-data-refresh must fail closed when "
        "secrets.PRODUCTION_ARTIFACT_WRITE_DEPLOY_KEY is empty"
    ]

    reordered = block.replace(preflight, "__PREFLIGHT__", 1)
    reordered = reordered.replace(checkout, preflight, 1)
    reordered = reordered.replace("__PREFLIGHT__", checkout, 1)
    ordering_errors: list[str] = []
    inventory.validate_artifact_push_job(
        workflow_path,
        "individual-stock-data-refresh",
        reordered,
        ordering_errors,
    )
    assert ordering_errors == [
        f"{workflow_path} writer job individual-stock-data-refresh must check "
        "the deploy key before actions/checkout"
    ]


def test_pull_request_workflows_never_receive_the_write_deploy_key() -> None:
    for workflow_path in inventory.tracked_workflow_paths():
        text = (ROOT / workflow_path).read_text(encoding="utf-8")
        if inventory.workflow_has_pull_request_trigger(text):
            assert inventory.PRODUCTION_ARTIFACT_WRITE_DEPLOY_KEY not in text


def _install_trust_guard_git_stub(
    monkeypatch: pytest.MonkeyPatch,
    *,
    diff_payload: bytes,
    base_mode: str = "100644",
    head_mode: str = "100644",
    base_type: str = "blob",
    head_type: str = "blob",
    head_workflow: bytes | None = None,
) -> tuple[str, str]:
    base_sha = "a" * 40
    head_sha = "b" * 40

    def fake_git_output_bytes(*args: str) -> bytes:
        if args == ("rev-parse", "HEAD"):
            return (base_sha + "\n").encode("ascii")
        if args and args[0] == "diff":
            assert "--no-renames" in args
            assert args[-3:] == (base_sha, head_sha, "--")
            return diff_payload
        if args[:2] == ("ls-tree", "-z"):
            ref = args[2]
            target_path = args[-1]
            mode = base_mode if ref == base_sha else head_mode
            object_type = base_type if ref == base_sha else head_type
            object_id = ("1" if ref == base_sha else "2") * 40
            return (
                f"{mode} {object_type} {object_id}\t{target_path}\0"
            ).encode("utf-8")
        if args and args[0] == "show":
            if head_workflow is None:
                raise RuntimeError("unexpected workflow blob read")
            return head_workflow
        raise AssertionError(args)

    monkeypatch.setattr(inventory, "git_output_bytes", fake_git_output_bytes)
    return base_sha, head_sha




def test_pr_trust_root_guard_fast_passes_routine_diff(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    base_sha, head_sha = _install_trust_guard_git_stub(
        monkeypatch,
        diff_payload=b"M\0docs/routine-note.md\0",
    )
    assert inventory.validate_pr_trust_root_change(base_sha, head_sha) == []


def test_individual_scope_detector_is_a_label_guarded_trust_root(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    target_path = "scripts/detect_individual_stock_pr_scope.py"
    assert target_path in inventory.PR_SAFE_TRUST_ROOT_PATHS
    base_sha, head_sha = _install_trust_guard_git_stub(
        monkeypatch,
        diff_payload=b"M\0" + target_path.encode("utf-8") + b"\0",
    )

    missing_approval = inventory.validate_pr_trust_root_change(
        base_sha,
        head_sha,
        base_repository=inventory.PR_SAFE_REPOSITORY,
        head_repository=inventory.PR_SAFE_REPOSITORY,
        maintainer_approved="false",
    )
    assert any("requires the explicit" in error for error in missing_approval)

    assert inventory.validate_pr_trust_root_change(
        base_sha,
        head_sha,
        base_repository=inventory.PR_SAFE_REPOSITORY,
        head_repository=inventory.PR_SAFE_REPOSITORY,
        maintainer_approved="true",
    ) == []


@pytest.mark.parametrize(
    ("status", "head_mode", "head_type"),
    [
        ("D", "100644", "blob"),
        ("T", "120000", "blob"),
        ("M", "120000", "blob"),
        ("M", "160000", "commit"),
        ("M", "100755", "blob"),
    ],
)
def test_pr_trust_root_guard_rejects_delete_type_and_mode_drift(
    monkeypatch: pytest.MonkeyPatch,
    status: str,
    head_mode: str,
    head_type: str,
) -> None:
    target_path = inventory.PR_SAFE_BASE_GUARD_SCRIPT
    base_sha, head_sha = _install_trust_guard_git_stub(
        monkeypatch,
        diff_payload=(
            status.encode("ascii") + b"\0" + target_path.encode("utf-8") + b"\0"
        ),
        head_mode=head_mode,
        head_type=head_type,
    )
    errors = inventory.validate_pr_trust_root_change(
        base_sha,
        head_sha,
        base_repository=inventory.PR_SAFE_REPOSITORY,
        head_repository=inventory.PR_SAFE_REPOSITORY,
        maintainer_approved="true",
    )
    assert errors


def test_pr_trust_root_workflow_change_is_validated_from_base_code(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    workflow_payload = (
        ROOT / inventory.PR_SAFE_BASE_GUARD_WORKFLOW
    ).read_bytes().replace(b"\r\n", b"\n")
    target_path = inventory.PR_SAFE_BASE_GUARD_WORKFLOW
    diff_payload = b"M\0" + target_path.encode("utf-8") + b"\0"
    base_sha, head_sha = _install_trust_guard_git_stub(
        monkeypatch,
        diff_payload=diff_payload,
        head_workflow=workflow_payload,
    )
    assert inventory.validate_pr_trust_root_change(
        base_sha,
        head_sha,
        base_repository=inventory.PR_SAFE_REPOSITORY,
        head_repository=inventory.PR_SAFE_REPOSITORY,
        maintainer_approved="true",
    ) == []

    bad_workflow = workflow_payload.replace(
        b"permissions:\n  contents: read",
        b"permissions:\n  contents: write",
        1,
    )
    _install_trust_guard_git_stub(
        monkeypatch,
        diff_payload=diff_payload,
        head_workflow=bad_workflow,
    )
    errors = inventory.validate_pr_trust_root_change(
        base_sha,
        head_sha,
        base_repository=inventory.PR_SAFE_REPOSITORY,
        head_repository=inventory.PR_SAFE_REPOSITORY,
        maintainer_approved="true",
    )
    assert errors

def test_pr_safe_trust_root_paths_are_exact_after_ledger_retirement() -> None:
    helper_paths = {
        "/".join(
            (
                "scripts",
                "_".join(
                    ("validate", "repo", "advanced", "integrity", "pr", "safe")
                )
                + ".py",
            )
        ),
        "/".join(
            (
                "scripts",
                "_".join(
                    ("validate", "daily", "published", "model", "snapshots", "pr", "safe")
                )
                + ".py",
            )
        ),
    }
    assert inventory.PR_SAFE_TRUST_ROOT_PATHS == frozenset(
        {
            ".github/workflows/individual_stock_pr_validation.yml",
            "scripts/detect_individual_stock_pr_scope.py",
            "scripts/validate_repo_production_inventory.py",
            *helper_paths,
            "config/repo_file_lifecycle_semantic_migrations.csv",
        }
    )


def test_routine_guard_does_not_read_retired_authorization_csv() -> None:
    source = Path(inventory.__file__).read_text(encoding="utf-8")
    retired_path = (
        "config/daily_model_pr_safe_" + "self_migration_authorizations.csv"
    )
    assert retired_path not in source


def test_legacy_exact_target_authorization_symbols_are_retired() -> None:
    symbol_names = (
        "canonical_blob_" + "sha256",
        "build_daily_full_checkpoint_replay_"
        + "integrated_lifecycle_inventory",
        "pr_safe_migration_contract_" + "for_paths",
        "is_preauthorized_daily_full_checkpoint_replay_" + "migration",
        "parse_pr_safe_" + "authorizations",
        "validate_pr_safe_authorization_" + "history",
        "parse_pr_safe_lifecycle_" + "authorizations",
        "validate_pr_safe_control_plane_" + "delta",
        "validate_pr_safe_exact_migration_blob_" + "modes",
    )
    for name in symbol_names:
        assert not hasattr(inventory, name)


def test_authorization_retirement_keeps_unrelated_tool() -> None:
    assert (
        ROOT / "scripts/validate_revenue_unreacted_range_promotion_preparation.py"
    ).is_file()


def test_pr_trust_root_guard_requires_same_repo_and_label_but_allows_new_bytes(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    target_path = next(
        path for path in inventory.PR_SAFE_TRUST_ROOT_PATHS if "advanced" in path
    )
    base_sha, head_sha = _install_trust_guard_git_stub(
        monkeypatch,
        diff_payload=b"M\0" + target_path.encode("utf-8") + b"\0",
    )

    missing = inventory.validate_pr_trust_root_change(
        base_sha,
        head_sha,
        base_repository=inventory.PR_SAFE_REPOSITORY,
        head_repository=inventory.PR_SAFE_REPOSITORY,
        maintainer_approved="false",
    )
    assert any("requires the explicit" in error for error in missing)

    wrong_repo = inventory.validate_pr_trust_root_change(
        base_sha,
        head_sha,
        base_repository=inventory.PR_SAFE_REPOSITORY,
        head_repository="fork/repository",
        maintainer_approved="true",
    )
    assert any("same repository" in error for error in wrong_repo)

    assert inventory.validate_pr_trust_root_change(
        base_sha,
        head_sha,
        base_repository=inventory.PR_SAFE_REPOSITORY,
        head_repository=inventory.PR_SAFE_REPOSITORY,
        maintainer_approved="true",
    ) == []


def test_pr_safe_name_status_parser_keeps_type_change_and_both_rename_paths() -> None:
    target_path = next(
        path for path in inventory.PR_SAFE_TRUST_ROOT_PATHS if "advanced" in path
    )
    payload = (
        b"T\0" + target_path.encode("utf-8") + b"\0"
        b"R100\0.github/workflows/individual_stock_pr_validation.yml\0"
        b".github/workflows/renamed_guard.yml\0"
    )
    paths, errors = inventory.parse_git_name_status_z(payload)
    assert errors == []
    assert paths == {
        target_path,
        ".github/workflows/individual_stock_pr_validation.yml",
        ".github/workflows/renamed_guard.yml",
    }
