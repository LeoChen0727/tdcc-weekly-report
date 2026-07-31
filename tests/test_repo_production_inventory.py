from __future__ import annotations

from pathlib import Path
import csv

from scripts import validate_repo_production_inventory as inventory


ROOT = Path(__file__).resolve().parents[1]


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


def test_all_lane_workflows_run_repo_inventory_gate() -> None:
    for workflow_path in inventory.REQUIRED_WORKFLOW_COMMANDS:
        workflow_text = (ROOT / workflow_path).read_text(encoding="utf-8")
        assert "python scripts/validate_repo_production_inventory.py" in workflow_text


def test_weekly_and_warrant_workflows_do_not_stage_source_files() -> None:
    for workflow_path in (
        ".github/workflows/tdcc_weekly.yml",
        ".github/workflows/tdcc_history_backfill.yml",
        ".github/workflows/warrant_flow.yml",
    ):
        workflow_text = (ROOT / workflow_path).read_text(encoding="utf-8")
        assert "git add scripts/" not in workflow_text
        assert "git add .github/workflows/" not in workflow_text


def test_daily_workflow_runs_repo_inventory_before_daily_generation() -> None:
    workflow_text = (ROOT / ".github" / "workflows" / "daily_full_pipeline.yml").read_text(
        encoding="utf-8"
    )

    repo_inventory_at = workflow_text.index("python scripts/validate_repo_production_inventory.py")
    price_fetch_at = workflow_text.index("python fetch_official_daily_price.py")
    assert repo_inventory_at < price_fetch_at


def test_daily_boundary_validator_runs_repo_inventory_gate() -> None:
    boundary_text = (ROOT / "scripts" / "validate_daily_production_boundaries.py").read_text(
        encoding="utf-8"
    )

    assert "validate_repo_production_inventory.py" in boundary_text


def test_historical_replay_daily_production_scope_is_one_registered_builder() -> None:
    workflow_path = ".github/workflows/historical_structured_source_replay.yml"
    expected_exceptions = {
        (
            workflow_path,
            "scripts/build_volume_attack_theme_layer.py",
        ): "daily_production"
    }
    assert inventory.WORKFLOW_CROSS_OWNER_PATH_EXCEPTIONS == expected_exceptions

    errors: list[str] = []
    rows = inventory.load_inventory(errors)
    invoked_daily_production = {
        path
        for path in inventory.workflow_invocations(workflow_path)
        if rows[path].owner == "daily_production"
    }
    assert invoked_daily_production == {
        "scripts/build_volume_attack_theme_layer.py"
    }
    inventory.validate_workflow_invocations(rows, {workflow_path}, errors)
    assert errors == []


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

    assert len(writer_rows) == 14
    assert errors == []


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
