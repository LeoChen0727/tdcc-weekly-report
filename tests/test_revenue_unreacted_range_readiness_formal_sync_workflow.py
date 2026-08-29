from __future__ import annotations

from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
WORKFLOW = ROOT / ".github/workflows/revenue_unreacted_range_readiness_formal_sync.yml"
SPEC = ROOT / "docs/specs/revenue_unreacted_range_readiness_formal_sync_v2.md"
TEXT = WORKFLOW.read_text(encoding="utf-8")
SPEC_TEXT = SPEC.read_text(encoding="utf-8")

PRODUCER = "scripts/sync_revenue_unreacted_range_operation_readiness.py"
VALIDATOR = "scripts/validate_revenue_unreacted_range_readiness_formal_sync_v2.py"
TARGET = "codex/revenue-unreacted-range-readiness-formal-sync-3c-v2-20260829"
CONTRACT = "revenue_readiness_sync_3c_v2_20260829"
EXCEPTION = "revenue_unreacted_range_readiness_formal_sync_3c_v2_20260829"
AUTHORIZATION = "user_authorized_3A_3C_20260829"
CONFIRMATION = "sync_revenue_unreacted_range_readiness_v2_20260829"
PUSH = (
    'git push "git@github.com:${GITHUB_REPOSITORY}.git" '
    '"HEAD:refs/heads/$TARGET_BRANCH"'
)
FOUR_PATHS = (
    "output/latest/model_operation_readiness_latest.csv",
    "output/latest/model_operation_readiness_latest.md",
    "docs/latest/model_operation_readiness_latest.csv",
    "docs/latest/model_operation_readiness_latest.md",
)


def test_fixed_contract_literals_are_coherent() -> None:
    for token in (
        f"contract_version={CONTRACT}",
        f"exception_id={EXCEPTION}",
        f"authorization_reference={AUTHORIZATION}",
        f"target_branch={TARGET}",
        f"producer={PRODUCER}",
        f"validator={VALIDATOR}",
    ):
        assert TEXT.count(token) == 2
        assert token in SPEC_TEXT
    assert f"READINESS_SYNC_CONTRACT_VERSION: {CONTRACT}" in TEXT
    assert f"READINESS_SYNC_EXCEPTION_ID: {EXCEPTION}" in TEXT
    assert f"READINESS_SYNC_AUTHORIZATION: {AUTHORIZATION}" in TEXT
    assert f"READINESS_SYNC_TARGET_BRANCH: {TARGET}" in TEXT
    assert f'[ "$CONFIRMATION" = {CONFIRMATION} ]' in TEXT
    assert f"`confirmation={CONFIRMATION}`" in SPEC_TEXT


def test_target_branch_is_never_checked_out_or_executed() -> None:
    assert 'ref: "${{ inputs.target_branch }}"' not in TEXT
    assert "ref: ${{ inputs.target_branch }}" not in TEXT
    assert "ref: main" in TEXT
    assert 'ref: "${{ inputs.expected_main_sha }}"' in TEXT
    assert TEXT.count("persist-credentials: false") == 2
    assert "git merge-base" not in TEXT


def test_workflow_calls_only_the_model_owned_producer_for_business_gates() -> None:
    assert TEXT.count(f"python -B {PRODUCER}") == 1
    assert "scripts/build_model_operation_readiness.py" not in TEXT
    for forbidden in (
        "validate_revenue_unreacted_range_anomaly_dispositions.py",
        "validate_revenue_unreacted_range_operation_adapter.py",
        "revenue_unreacted_range_operation_adapter.py",
        "revenue_unreacted_range_forward_holdout_v2.py",
    ):
        assert forbidden not in TEXT
    assert "producer owns the calls to" in SPEC_TEXT.lower()


def test_dedicated_validator_covers_every_phase() -> None:
    command = f"python -B {VALIDATOR}"
    assert TEXT.count(command) == 4
    assert TEXT.count("--phase working-tree") == 1
    assert TEXT.count("--phase staged") == 1
    assert TEXT.count("--phase committed") == 2
    assert (
        "validator 只驗 exact-four artifact/phase semantics"
        not in TEXT
    )


def test_contract_records_closed_anomalies_disabled_adapter_and_only_blocker() -> None:
    for token in (
        "verified_real_extreme=8",
        "verified_data_error_repaired=1",
        "unresolved_anomalies=0",
        "effective_anomaly_blockers=0",
        "operation_module_status=disabled_adapter_preparation_validated",
        "daily_adapter_status=disabled_no_runtime_artifact",
        (
            "operation_module_id="
            "revenue_unreacted_range_source_mid_falling_v2_operation_v1"
        ),
        "daily_adapter_row_count=0",
        "daily_adapter_data_row_count=0",
        "formal_model_use_allowed=False",
        "approved_for_daily=False",
        "presentation_allowed=False",
        "production_allowed=False",
        "blocker=forward_holdout_v2_mature=0/20",
    ):
        assert TEXT.count(f'"{token}"') == 2
        assert f"`{token}`" in SPEC_TEXT or token in SPEC_TEXT
    assert "anomaly_disposition_blockers=9" not in TEXT
    assert "formal_adapter=not_started" not in TEXT


def test_each_job_has_pinned_python_and_runtime_dependencies() -> None:
    prepare_job, apply_job = TEXT.split("  apply-bundle:\n", 1)
    setup_action = "actions/setup-python@v6.2.0"
    dependencies = (
        "python -m pip install --disable-pip-version-check pandas requests tabulate"
    )
    for job in (prepare_job, apply_job):
        assert job.count(setup_action) == 1
        assert job.count('python-version: "3.11"') == 1
        assert job.count(dependencies) == 1


def test_exact_four_bundle_hashes_and_clean_state_are_revalidated() -> None:
    for path in FOUR_PATHS:
        assert TEXT.count(path) >= 4
        assert path in SPEC_TEXT
    assert "sha256sum --check SHA256SUMS" in TEXT
    assert "find \"$bundle\" -type f -printf '%P\\n' | sort" in TEXT
    exact_file_count = (
        '[ "$(find "$bundle" -type f -printf \'%P\\n\' | sort | wc -l)" = 6 ]'
    )
    assert exact_file_count in TEXT
    assert TEXT.count("git status --porcelain=v1 -z --untracked-files=all") == 2


def test_final_step_contains_the_only_non_force_push_and_key_cleanup() -> None:
    marker = "- name: Push only validated commit to inert codex target"
    before, final = TEXT.split(marker, 1)
    assert "PRODUCTION_ARTIFACT_WRITE_DEPLOY_KEY" not in before
    assert TEXT.count("git push ") == 1
    assert PUSH in final
    assert "git push --force" not in TEXT
    assert "remote_main_before" in final
    assert "remote_target_before" in final
    assert "remote_main_after" in final
    assert "remote_target_after" in final
    assert '[ "$remote_target_after" = "$SYNC_COMMIT_SHA" ]' in final
    assert "trap 'rm -f \"$key\"' EXIT" in final
    assert "rm -f \"$key\"" in final
    assert "trap - EXIT" in final
    assert "\n      - name:" not in final
    assert "\n      - uses:" not in final


def test_workflow_has_no_automatic_or_forbidden_execution_surface() -> None:
    for token in (
        "run_chatgpt_daily_" + "report_entrypoint",
        "daily_full_" + "pipeline",
        "generate_chatgpt_side_daily_reports",
        "gh workflow run",
        "clasp ",
    ):
        assert token not in TEXT.lower()
    assert "\n  schedule:" not in TEXT
    assert "\n  push:" not in TEXT
    assert "workflow_dispatch:" in TEXT


def test_bundle_contract_is_identical_in_prepare_and_apply_jobs() -> None:
    prepare_job, apply_job = TEXT.split("  apply-bundle:\n", 1)
    contract_lines = (
        "contract_version=",
        "exception_id=",
        "authorization_reference=",
        "target_branch=",
        "model_id=",
        "producer=",
        "validator=",
        "verified_real_extreme=",
        "verified_data_error_repaired=",
        "unresolved_anomalies=",
        "effective_anomaly_blockers=",
        "operation_module_status=",
        "daily_adapter_status=",
        "operation_module_id=",
        "daily_adapter_row_count=",
        "daily_adapter_data_row_count=",
        "formal_model_use_allowed=",
        "approved_for_daily=",
        "presentation_allowed=",
        "production_allowed=",
        "blocker=",
    )
    for prefix in contract_lines:
        prepare_matches = [
            line.split('"', 2)[1]
            for line in prepare_job.splitlines()
            if prefix in line
        ]
        apply_matches = [
            line.split('"', 2)[1]
            for line in apply_job.splitlines()
            if prefix in line
        ]
        assert prepare_matches == apply_matches, prefix
